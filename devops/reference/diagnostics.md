# 诊断手册

> 系统化排查流程。每一步都有明确目的，每一个结论都有证据支撑。

## 黄金诊断流程

```
Step 0: 确认现象（别信，自己看）
Step 1: 系统资源快照（排除资源瓶颈）
Step 2: 服务状态检查（定位哪一层出问题）
Step 3: 日志分析（找到具体错误）
Step 4: 配置验证（排除配置问题）
Step 5: 关联分析（时间线 + 因果链）
Step 6: 定向验证（验证假设）
```

---

## Step 0: 确认现象

**目的**：把主观描述变成客观数据。

用户说 "服务挂了"：
```bash
# 1. 进程在不在
ps aux | grep <service>
systemctl status <service>

# 2. 端口通不通
ss -tlnp | grep <port>
curl -sI http://localhost:<port>

# 3. 能不能从外部访问
curl -sI http://<external_ip>:<port>
```

用户说 "访问慢"：
```bash
# 量化：到底多慢
curl -o /dev/null -s -w "DNS: %{time_namelookup}s\nTCP: %{time_connect}s\nTLS: %{time_appconnect}s\nFirstByte: %{time_starttransfer}s\nTotal: %{time_total}s\n" http://target

# 对比：正常应该多快（历史基线）
# 定位：哪一段慢（DNS？TCP？应用处理？）
```

用户说 "报错了"：
```bash
# 获取完整错误
journalctl -u <service> --since "5 min ago" --no-pager
docker logs --tail 100 <container>

# 不要只看最后一行，要看上下文
# 错误往往是一连串事件的结果，根因在前面
```

---

## Step 1: 系统资源快照

**目的**：排除/确认资源瓶颈。这是第一步，因为很多上层问题的根因在这。

### 一键快照命令
```bash
echo "=== UPTIME ===" && uptime && \
echo "=== MEMORY ===" && free -h && \
echo "=== DISK ===" && df -h && \
echo "=== CPU TOP5 ===" && ps aux --sort=-%cpu | head -6 && \
echo "=== MEM TOP5 ===" && ps aux --sort=-%mem | head -6 && \
echo "=== DISK IO ===" && iostat -x 1 1 2>/dev/null || echo "iostat not available" && \
echo "=== LOAD ===" && cat /proc/loadavg
```

### 判断标准

| 指标 | 正常 | 需关注 | 紧急 |
|------|------|--------|------|
| CPU使用率 | < 70% | 70-90% | > 90% |
| 内存使用率 | < 80% | 80-90% | > 90% |
| 磁盘使用率 | < 80% | 80-90% | > 90% |
| 系统负载 | < CPU核数 | 1-2x核数 | > 2x核数 |
| IO等待 | < 10% | 10-30% | > 30% |
| Swap使用 | 0 | < 500MB | > 500MB |

### 常见资源问题处理

**OOM Kill**：
```bash
# 查看OOM记录
dmesg | grep -i "oom\|out of memory" | tail -10
journalctl -k | grep -i oom | tail -10

# 查看被kill的进程
dmesg | grep "Killed process" | tail -5
```

**磁盘满**：
```bash
# 找大文件
du -sh /* 2>/dev/null | sort -rh | head -10
du -sh /var/log/* 2>/dev/null | sort -rh | head -10

# Docker占用
docker system df
```

**高CPU**：
```bash
# 找占CPU的进程
top -bn1 -o %CPU | head -15

# 如果是Docker容器
docker stats --no-stream --format "table {{.Name}}\t{{.CPUPerc}}\t{{.MemUsage}}"
```

---

## Step 2: 服务状态检查

**目的**：确认各层服务的运行状态。

### Docker 容器检查
```bash
# 容器状态概览
docker ps -a --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}\t{{.Image}}"

# 最近退出的容器（可能是crash了）
docker ps -a --filter "status=exited" --format "table {{.Names}}\t{{.Status}}\t{{.Image}}" | head -10

# 容器资源使用
docker stats --no-stream

# 特定容器健康检查
docker inspect --format='{{.State.Health.Status}}' <container> 2>/dev/null || echo "No healthcheck"
```

### Nginx 检查
```bash
# 配置语法
nginx -t

# 运行状态
systemctl status nginx
# 或
ps aux | grep nginx

# 连接数
ss -s
ss -tlnp | grep :80
ss -tlnp | grep :443

# 最近错误
tail -50 /var/log/nginx/error.log
```

### 系统服务检查
```bash
# 失败的服务
systemctl --failed

# 特定服务
systemctl status <service>
journalctl -u <service> --since "10 min ago" --no-pager | tail -30
```

---

## Step 3: 日志分析

**目的**：从日志中找到具体错误信息和时间线。

### 日志分析原则
1. **先看时间**：问题什么时候开始的？
2. **先看错误**：过滤 error/fatal/panic/exception
3. **看上下文**：错误发生前发生了什么？
4. **看频率**：是偶发还是持续？
5. **看关联**：多个服务的日志时间是否对得上？

### 常用日志命令
```bash
# 系统日志 — 最近10分钟的错误
journalctl -p err --since "10 min ago" --no-pager

# Nginx错误日志 — 最近的错误
tail -100 /var/log/nginx/error.log

# Nginx访问日志 — 统计状态码
awk '{print $9}' /var/log/nginx/access.log | sort | uniq -c | sort -rn | head

# Docker容器日志
docker logs --tail 100 --timestamps <container>

# 按时间过滤Docker日志
docker logs --since "10m" <container>

# 多容器日志（docker compose）
docker compose logs --tail 50 --timestamps

# 查找特定错误
grep -i "error\|fatal\|panic\|exception\|fail" /var/log/syslog | tail -20
```

### 日志时间线分析
```bash
# 找到问题开始的时间点
grep -i "error" /var/log/nginx/error.log | tail -1  # 最新错误
grep -i "error" /var/log/nginx/error.log | head -1   # 最早错误

# 统计每分钟错误数（看趋势）
grep -i "error" /var/log/nginx/error.log | \
  awk '{print $1, $2}' | cut -d: -f1,2 | sort | uniq -c | tail -20
```

---

## Step 4: 配置验证

**目的**：排除配置错误。

### Nginx 配置验证
```bash
# 语法检查
nginx -t

# 查看生效配置
nginx -T  # 输出完整配置（包含所有include）

# 检查upstream是否可达
# 从nginx配置中提取upstream地址，然后curl测试
```

### Docker Compose 配置验证
```bash
# 语法检查
docker compose config

# 查看实际环境变量
docker compose config --format json | jq '.services[].environment'

# 对比运行中的配置和文件中的配置
docker inspect <container> | jq '.[0].Config.Env'
```

### 配置变更追溯
```bash
# 文件最后修改时间
stat /etc/nginx/nginx.conf
ls -la /etc/nginx/conf.d/

# 如果有git管理
git -C /path/to/config log --oneline -5
git -C /path/to/config diff HEAD~1
```

---

## Step 5: 关联分析

**目的**：将多个证据串联，找出因果关系。

### 时间线对齐法
```
10:00 — 磁盘使用率开始上升
10:15 — 数据库慢查询增加
10:20 — 应用响应时间变长
10:25 — Nginx开始报502
10:30 — 用户报告"网站挂了"

→ 根因：磁盘问题 → 数据库受影响 → 应用受影响 → 用户可见
```

### 关联检查清单
- [ ] 最近有没有做过变更？（部署、配置修改、系统更新）
- [ ] 有没有定时任务在这个时间运行？（crontab、备份）
- [ ] 是不是流量突增？（访问日志统计）
- [ ] 是不是外部依赖出了问题？（第三方API、DNS、CDN）
- [ ] 有没有证书过期？（SSL证书、API密钥）

---

## Step 6: 定向验证

**目的**：验证你的假设是否正确。

### 验证模板
```
假设：[你认为的根因]
验证方法：[怎么证明/推翻这个假设]
验证结果：[实际观察到的]
结论：[假设成立/不成立]
```

### 验证手段
```bash
# 网络连通性验证
ping -c 3 <target>
traceroute <target>
curl -v http://<target>

# DNS验证
dig <domain>
nslookup <domain>

# 端口验证
nc -zv <host> <port>
telnet <host> <port>

# 服务响应验证
curl -sI http://localhost:<port>/health
curl -w "%{http_code}" -s -o /dev/null http://target

# 权限验证
ls -la <file>
namei -l <path>
```

---

## 常见场景速查

### 场景1：Nginx 502 Bad Gateway

**排查顺序**：
1. upstream服务是否运行 → `docker ps` / `systemctl status`
2. upstream端口是否监听 → `ss -tlnp | grep <port>`
3. Nginx到upstream是否可达 → `curl http://127.0.0.1:<upstream_port>`
4. 系统资源是否正常 → `free -h` / `df -h`
5. 看Nginx错误日志 → `tail /var/log/nginx/error.log`

### 场景2：Docker 容器启动失败

**排查顺序**：
1. 看退出码 → `docker ps -a | grep <name>`
   - 退出码 0: 正常退出（可能是启动命令问题）
   - 退出码 1: 应用错误
   - 退出码 137: OOM Kill (128+9)
   - 退出码 139: Segfault (128+11)
2. 看容器日志 → `docker logs <container>`
3. 检查镜像是否存在 → `docker images | grep <image>`
4. 检查端口冲突 → `ss -tlnp | grep <port>`
5. 检查卷挂载 → `docker inspect <container> | jq '.[0].Mounts'`
6. 检查磁盘空间 → `df -h` + `docker system df`

### 场景3：SSH 连接失败

**排查顺序**：
1. 网络可达 → `ping <ip>`
2. 端口开放 → `nc -zv <ip> 22`（或 `Test-NetConnection <ip> -Port 22`）
3. SSH服务运行 → 如有其他途径检查 `systemctl status sshd`
4. 防火墙规则 → `iptables -L -n` / `ufw status`
5. SSH配置 → `/etc/ssh/sshd_config`
6. 认证问题 → 密码/密钥是否正确

### 场景4：磁盘空间不足

**排查顺序**：
1. 总体使用 → `df -h`
2. 大目录定位 → `du -sh /* | sort -rh | head`
3. Docker占用 → `docker system df`
4. 日志文件 → `du -sh /var/log/* | sort -rh | head`
5. 临时文件 → `du -sh /tmp/* | sort -rh | head`

**常见解法**：
```bash
# 清理Docker（低风险）
docker system prune -f           # 清理停止的容器、悬挂镜像
docker image prune -f            # 清理悬挂镜像

# 清理日志（需确认）
journalctl --vacuum-size=500M    # 限制系统日志大小
truncate -s 0 /var/log/xxx.log   # 清空特定日志（不删除文件）

# Docker日志限制（永久解决）
# /etc/docker/daemon.json
{
  "log-driver": "json-file",
  "log-opts": {
    "max-size": "10m",
    "max-file": "3"
  }
}
```

### 场景5：服务性能下降

**排查顺序**：
1. 确认影响范围 → 所有请求还是特定请求？
2. 系统资源 → CPU/内存/磁盘IO/网络
3. 数据库 → 慢查询、连接数、锁等待
4. 应用层 → 线程数、GC、连接池
5. 外部依赖 → 第三方API响应时间

```bash
# 数据库慢查询（MySQL）
mysql -e "SHOW PROCESSLIST;" | grep -v Sleep
mysql -e "SHOW GLOBAL STATUS LIKE 'Slow_queries';"

# 数据库慢查询（PostgreSQL）
psql -c "SELECT pid, now() - pg_stat_activity.query_start AS duration, query FROM pg_stat_activity WHERE state != 'idle' ORDER BY duration DESC LIMIT 10;"

# 连接数检查
ss -s
ss -tlnp | wc -l
```

### 场景6：Docker Compose 部署失败

**排查顺序**：
1. compose文件语法 → `docker compose config`
2. 镜像拉取 → `docker compose pull`
3. 端口冲突 → `ss -tlnp`
4. 卷权限 → `ls -la` 相关目录
5. 网络冲突 → `docker network ls`
6. 启动日志 → `docker compose up` (不加 -d，看实时输出)

---

## 巡检清单

### 日常巡检（快速版，2分钟）
```bash
echo "=== $(hostname) 巡检 $(date) ===" && \
echo "--- 系统 ---" && uptime && free -h | grep Mem && df -h / && \
echo "--- Docker ---" && docker ps --format "{{.Names}}: {{.Status}}" && \
echo "--- 最近错误 ---" && journalctl -p err --since "1 hour ago" --no-pager 2>/dev/null | tail -5
```

### 全面巡检（详细版，5-10分钟）
1. 系统资源（CPU、内存、磁盘、IO、负载）
2. Docker服务（所有容器状态、资源使用、日志异常）
3. Nginx（配置语法、连接数、错误日志）
4. 数据库（连接数、慢查询、存储空间）
5. 安全检查（登录失败记录、开放端口、证书有效期）
6. 备份验证（备份是否正常执行、文件是否完整）
7. 网络检查（DNS解析、外部连通性、内网互通）
