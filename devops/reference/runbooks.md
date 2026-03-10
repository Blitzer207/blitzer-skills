# 运维操作手册 (Runbooks)

> 标准化操作流程。每个操作都有前置检查、执行步骤和验证方法。

---

## 一、Docker 操作

### 1.1 容器生命周期管理

#### 查看容器状态
```bash
# 运行中的容器
docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}\t{{.Image}}"

# 所有容器（含已停止）
docker ps -a --format "table {{.Names}}\t{{.Status}}\t{{.Image}}"

# 容器资源使用
docker stats --no-stream --format "table {{.Name}}\t{{.CPUPerc}}\t{{.MemUsage}}\t{{.NetIO}}\t{{.BlockIO}}"
```

#### 重启容器 [Level 1]
```bash
# 前置：记录当前状态
docker inspect --format='{{.State.StartedAt}}' <container>

# 执行
docker restart <container>

# 验证
docker ps | grep <container>
docker logs --tail 10 <container>
```

#### 查看容器日志
```bash
# 最近N行
docker logs --tail 100 <container>

# 带时间戳
docker logs --tail 100 --timestamps <container>

# 实时跟踪
docker logs -f <container>

# 按时间过滤
docker logs --since "2024-01-01T10:00:00" <container>
docker logs --since "30m" <container>
```

#### 进入容器调试
```bash
# 进入运行中的容器
docker exec -it <container> /bin/bash
# 如果没有bash
docker exec -it <container> /bin/sh

# 以root身份进入
docker exec -u root -it <container> /bin/bash
```

### 1.2 Docker Compose 操作

#### 部署/更新服务 [Level 1]
```bash
# 前置检查
docker compose config          # 验证配置语法
docker compose ps              # 记录当前状态

# 拉取最新镜像
docker compose pull

# 更新部署（仅重建变更的服务）
docker compose up -d

# 强制重建
docker compose up -d --force-recreate

# 验证
docker compose ps
docker compose logs --tail 20
```

#### 回滚部署 [Level 2]
```bash
# 如果有git管理配置
git -C /path/to/project log --oneline -5    # 查看历史
git -C /path/to/project checkout HEAD~1 -- docker-compose.yml  # 回滚配置

# 如果知道之前的镜像tag
docker compose down
# 修改 docker-compose.yml 中的镜像tag
docker compose up -d

# 验证
docker compose ps
curl -sI http://localhost:<port>
```

#### 查看 Compose 项目状态
```bash
# 服务状态
docker compose ps

# 服务日志
docker compose logs --tail 50

# 特定服务日志
docker compose logs --tail 50 <service_name>

# 资源使用
docker compose top
```

### 1.3 Docker 清理

#### 安全清理 [Level 1]
```bash
# 查看空间占用
docker system df

# 清理已停止的容器和悬挂镜像（安全）
docker system prune -f

# 清理悬挂镜像
docker image prune -f
```

#### 深度清理 [Level 2 — 需确认]
```bash
# ⚠️ 清理所有未使用的镜像（不仅是悬挂的）
docker system prune -a -f

# ⚠️ 清理所有，包括卷
docker system prune -a --volumes -f

# 清理特定时间之前的
docker image prune -a --filter "until=720h" -f  # 30天前
```

### 1.4 Docker 网络排查

```bash
# 查看网络列表
docker network ls

# 查看网络详情（含连接的容器）
docker network inspect <network>

# 容器间连通性测试
docker exec <container1> ping <container2_name>
docker exec <container1> curl http://<container2_name>:<port>

# DNS解析测试（容器内）
docker exec <container> nslookup <service_name>
```

---

## 二、Nginx 操作

### 2.1 配置管理

#### 检查配置 [Level 0]
```bash
# 语法检查
nginx -t

# 查看完整生效配置
nginx -T

# 查看配置文件列表
ls -la /etc/nginx/conf.d/
ls -la /etc/nginx/sites-enabled/
```

#### 修改配置 [Level 2]
```bash
# 1. 备份当前配置
cp /etc/nginx/conf.d/target.conf /etc/nginx/conf.d/target.conf.bak.$(date +%Y%m%d%H%M)

# 2. 修改配置（使用你的编辑工具）

# 3. 验证语法
nginx -t

# 4. 如果语法正确，重载
nginx -s reload
# 或
systemctl reload nginx

# 5. 验证生效
curl -sI http://localhost
tail -5 /var/log/nginx/error.log

# 回滚（如果出问题）
cp /etc/nginx/conf.d/target.conf.bak.XXXXXX /etc/nginx/conf.d/target.conf
nginx -t && nginx -s reload
```

### 2.2 常用配置模板

#### 反向代理
```nginx
server {
    listen 80;
    server_name example.com;

    location / {
        proxy_pass http://127.0.0.1:3000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;

        # 超时设置
        proxy_connect_timeout 60s;
        proxy_send_timeout 60s;
        proxy_read_timeout 60s;
    }
}
```

#### HTTPS + 反向代理
```nginx
server {
    listen 80;
    server_name example.com;
    return 301 https://$host$request_uri;
}

server {
    listen 443 ssl http2;
    server_name example.com;

    ssl_certificate /etc/letsencrypt/live/example.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/example.com/privkey.pem;

    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers HIGH:!aNULL:!MD5;

    location / {
        proxy_pass http://127.0.0.1:3000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

#### WebSocket 代理
```nginx
location /ws {
    proxy_pass http://127.0.0.1:3000;
    proxy_http_version 1.1;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection "upgrade";
    proxy_set_header Host $host;
    proxy_read_timeout 86400;
}
```

### 2.3 Nginx 日志分析

```bash
# 状态码统计
awk '{print $9}' /var/log/nginx/access.log | sort | uniq -c | sort -rn

# 最多访问的URL
awk '{print $7}' /var/log/nginx/access.log | sort | uniq -c | sort -rn | head -20

# 最多访问的IP
awk '{print $1}' /var/log/nginx/access.log | sort | uniq -c | sort -rn | head -20

# 特定时间段的请求
awk '$4 >= "[01/Jan/2024:10:00" && $4 <= "[01/Jan/2024:11:00"' /var/log/nginx/access.log

# 502错误的upstream
grep "502" /var/log/nginx/error.log | tail -20

# 每分钟请求数（QPS趋势）
awk '{print $4}' /var/log/nginx/access.log | cut -d: -f1-3 | sort | uniq -c | tail -20
```

### 2.4 SSL 证书管理

```bash
# 查看证书信息
openssl x509 -in /etc/letsencrypt/live/domain/fullchain.pem -noout -dates -subject

# 检查证书过期时间
echo | openssl s_client -connect localhost:443 -servername domain.com 2>/dev/null | openssl x509 -noout -dates

# Let's Encrypt 续期（如果使用certbot）
certbot renew --dry-run     # 测试续期
certbot renew               # 实际续期
```

---

## 三、数据库操作

### 3.1 MySQL/MariaDB

#### 健康检查 [Level 0]
```bash
# 连接测试
mysql -u root -p -e "SELECT 1;"

# 连接数
mysql -e "SHOW STATUS LIKE 'Threads_connected';"
mysql -e "SHOW STATUS LIKE 'Max_used_connections';"

# 慢查询
mysql -e "SHOW GLOBAL STATUS LIKE 'Slow_queries';"
mysql -e "SHOW VARIABLES LIKE 'slow_query_log%';"

# 当前运行的查询
mysql -e "SHOW PROCESSLIST;" | grep -v Sleep

# 数据库大小
mysql -e "SELECT table_schema AS 'Database', ROUND(SUM(data_length + index_length) / 1024 / 1024, 2) AS 'Size (MB)' FROM information_schema.tables GROUP BY table_schema ORDER BY SUM(data_length + index_length) DESC;"
```

#### 备份 [Level 1]
```bash
# 全量备份
mysqldump -u root -p --all-databases --single-transaction > backup_$(date +%Y%m%d_%H%M).sql

# 单库备份
mysqldump -u root -p --single-transaction <dbname> > <dbname>_$(date +%Y%m%d_%H%M).sql

# 压缩备份
mysqldump -u root -p --single-transaction <dbname> | gzip > <dbname>_$(date +%Y%m%d_%H%M).sql.gz
```

#### 恢复 [Level 3 — 危险]
```bash
# ⚠️ 恢复会覆盖现有数据
mysql -u root -p <dbname> < backup.sql

# 从压缩文件恢复
gunzip < backup.sql.gz | mysql -u root -p <dbname>
```

### 3.2 PostgreSQL

#### 健康检查 [Level 0]
```bash
# 连接测试
psql -U postgres -c "SELECT 1;"

# 连接数
psql -U postgres -c "SELECT count(*) FROM pg_stat_activity;"

# 活跃查询
psql -U postgres -c "SELECT pid, now() - pg_stat_activity.query_start AS duration, query, state FROM pg_stat_activity WHERE state != 'idle' ORDER BY duration DESC LIMIT 10;"

# 数据库大小
psql -U postgres -c "SELECT pg_database.datname, pg_size_pretty(pg_database_size(pg_database.datname)) FROM pg_database ORDER BY pg_database_size(pg_database.datname) DESC;"

# 锁等待
psql -U postgres -c "SELECT * FROM pg_locks WHERE NOT granted;"
```

### 3.3 Redis

#### 健康检查 [Level 0]
```bash
# 连接测试
redis-cli ping

# 内存使用
redis-cli info memory | grep -E "used_memory_human|maxmemory_human"

# 连接数
redis-cli info clients | grep connected_clients

# 慢查询
redis-cli slowlog get 10

# Key统计
redis-cli info keyspace
```

---

## 四、部署操作

### 4.1 标准部署流程

#### Docker Compose 项目部署 [Level 1]
```bash
# === 前置检查 ===
# 1. 验证配置
docker compose config

# 2. 检查磁盘空间
df -h /

# 3. 记录当前状态（用于回滚对比）
docker compose ps > /tmp/pre-deploy-state.txt

# === 部署 ===
# 4. 拉取最新镜像
docker compose pull

# 5. 应用更新（仅重建变更的服务）
docker compose up -d

# === 验证 ===
# 6. 检查容器状态
docker compose ps

# 7. 检查日志（无报错）
docker compose logs --tail 30

# 8. 健康检查
curl -sI http://localhost:<port>

# === 回滚（如果验证失败） ===
# docker compose down
# git checkout HEAD~1 -- docker-compose.yml  （或恢复备份的配置）
# docker compose up -d
```

### 4.2 零停机部署（滚动更新）

#### 使用 Docker Compose
```bash
# 单服务更新（不影响其他服务）
docker compose pull <service>
docker compose up -d --no-deps <service>

# 验证
docker compose ps
curl -sI http://localhost:<port>
```

### 4.3 数据迁移 [Level 3]

```bash
# 1. 备份源数据
mysqldump -h source_host -u user -p dbname > migration_backup.sql

# 2. 验证备份完整性
mysql -e "SELECT COUNT(*) FROM important_table;" -h source_host
grep "INSERT INTO \`important_table\`" migration_backup.sql | wc -l

# 3. 导入目标库
mysql -h target_host -u user -p dbname < migration_backup.sql

# 4. 验证数据完整性
mysql -e "SELECT COUNT(*) FROM important_table;" -h target_host
```

---

## 五、安全操作

### 5.1 防火墙管理

#### UFW（Ubuntu）
```bash
# 查看规则
ufw status verbose

# 开放端口 [Level 2]
ufw allow 80/tcp
ufw allow 443/tcp
ufw allow from 10.0.0.0/24      # 允许内网网段（按实际修改）

# 关闭端口 [Level 2]
ufw deny 3306/tcp    # 禁止外部访问MySQL

# 启用防火墙 [Level 3 — 可能断开SSH！]
ufw enable
```

#### iptables
```bash
# 查看规则
iptables -L -n --line-numbers

# 开放端口 [Level 2]
iptables -A INPUT -p tcp --dport 80 -j ACCEPT

# 保存规则
iptables-save > /etc/iptables.rules
```

### 5.2 安全检查

```bash
# 最近登录失败
grep "Failed password" /var/log/auth.log | tail -20
lastb | head -20

# 最近成功登录
last | head -20

# 开放端口（是否有不该开放的）
ss -tlnp

# 可疑进程
ps aux --sort=-%cpu | head -20

# 检查定时任务
crontab -l
ls -la /etc/cron.d/
```

### 5.3 SSL/TLS 证书

```bash
# 检查远程证书
echo | openssl s_client -connect domain:443 2>/dev/null | openssl x509 -noout -dates

# 检查本地证书
openssl x509 -in cert.pem -noout -text

# 检查证书链
openssl verify -CAfile ca.pem cert.pem
```

---

## 六、监控与告警

### 6.1 实时监控命令

```bash
# CPU + 内存 + 进程（实时）
top -bn1 | head -20

# 磁盘IO（实时）
iostat -x 1 3

# 网络连接（实时）
ss -s

# Docker 容器资源（实时）
docker stats --no-stream

# 综合监控（一次性）
echo "=== $(date) ===" && \
echo "Load: $(cat /proc/loadavg)" && \
echo "Memory: $(free -h | grep Mem | awk '{print $3"/"$2}')" && \
echo "Disk: $(df -h / | tail -1 | awk '{print $3"/"$2" ("$5")"}')" && \
echo "Docker: $(docker ps -q | wc -l) containers running"
```

### 6.2 日志监控

```bash
# 实时跟踪错误
tail -f /var/log/nginx/error.log

# 实时跟踪多个日志
tail -f /var/log/nginx/error.log /var/log/syslog

# Docker 实时日志
docker compose logs -f --tail 0
```

---

## 七、故障恢复

### 7.1 服务恢复优先级

1. **网络/SSH** — 最先恢复（否则无法远程操作）
2. **存储/数据库** — 数据安全第一
3. **核心服务** — 反向代理、认证服务
4. **应用服务** — 业务应用
5. **辅助服务** — 监控、日志收集

### 7.2 常见恢复操作

#### 服务无法启动
```bash
# 1. 看状态和日志
systemctl status <service>
journalctl -u <service> --since "5 min ago" --no-pager

# 2. 检查配置
<service> -t  # 如果支持配置检查

# 3. 检查依赖
# 端口被占用？
ss -tlnp | grep <port>
# 依赖服务是否正常？
systemctl status <dependency>

# 4. 尝试重启
systemctl restart <service>
```

#### Docker Compose 项目恢复
```bash
# 1. 停止所有服务
docker compose down

# 2. 清理可能的问题
docker compose rm -f

# 3. 重新启动
docker compose up -d

# 4. 如果还有问题，重建
docker compose up -d --force-recreate --build
```

#### 磁盘空间紧急恢复
```bash
# 快速释放空间（安全操作）
docker system prune -f                              # Docker垃圾
journalctl --vacuum-size=200M                        # 系统日志
find /tmp -type f -mtime +7 -delete 2>/dev/null      # 7天前的临时文件
find /var/log -name "*.gz" -mtime +30 -delete         # 30天前的压缩日志
```
