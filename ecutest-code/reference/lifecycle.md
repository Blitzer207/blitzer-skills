# lifecycle.md — EcuTestController

## 基本用法

```python
import os
from ecutest.lifecycle import EcuTestController

workspaceRoot = os.path.join(os.path.dirname(__file__), "ecu.test-code")
ctrl = EcuTestController()
ctrl.start(
    workspace=workspaceRoot,
    tbc=os.path.join(workspaceRoot, "Configurations", "Testlab_HiL_M.tbc"),
    tcf=os.path.join(workspaceRoot, "Configurations", "SW_Ver_1.tcf"),
)
# ... 测试 ...
ctrl.stop()
```

## Context Manager 用法

```python
with ctrl.running_ecutest(workspace=workspaceRoot, tbc=..., tcf=...):
    # ecu.test 在此块内保证运行，退出时自动 stop
    ...
```

`stop_on_exit` 参数：
- `None`（默认）：若本次启动了 ecu.test 则退出时 stop，否则保留
- `True`：始终 stop
- `False`：始终保留

## start() 关键参数

| 参数 | 类型 | 说明 |
|------|------|------|
| `workspace` | `str \| Path \| None` | workspace 目录，None 则使用上次记录的 |
| `tbc` | `str \| Path \| None` | testbench 配置文件路径 |
| `tcf` | `str \| Path \| None` | test 配置文件路径 |
| `allow_restart` | `bool` | 若已运行但 workspace/版本不匹配，是否允许重启 |
| `accept_any_version` | `bool` | 接受任意版本的已运行实例 |
| `extra_args` | `list[str] \| None` | 传给 ecu.test runner 的额外命令行参数 |

## 构造函数参数

```python
ctrl = EcuTestController(
    executable=None,      # None = 自动检测（Windows 读注册表，Linux 查 /opt）
    xmlrpc_port=None,     # None = 自动检测，默认 8000
    restapi_port=5050,    # REST API 端口
    silent=False,         # 是否抑制外部命令输出
)
```

自动检测要求版本 ≥ 2025.3。

## 其他方法

| 方法 | 说明 |
|------|------|
| `ctrl.stop(timeout=90)` | 优雅退出 ecu.test |
| `ctrl.kill(timeout=30)` | 强制退出 ecu.test |
| `ctrl.start_webapi()` | 在已运行的实例上启动 web API |
| `ctrl.is_webapi_active()` | 检查 web API 是否活跃 |
| `ctrl.get_running_ecutest_version()` | 获取当前运行版本 |
| `ctrl.get_current_workspace()` | 获取当前 workspace 路径 |
| `ctrl.get_loaded_tbc()` | 获取已加载的 TBC 路径 |
| `ctrl.get_loaded_tcf()` | 获取已加载的 TCF 路径 |
| `ctrl.is_config_started()` | 检查配置是否已启动 |

## 注意事项

- 若 ecu.test 已在正确 workspace 运行，`start()` 会复用现有实例，不会重启
- workspace/版本不匹配时，不加 `allow_restart=True` 会抛 `RuntimeError`
- `stop()` 和 `kill()` 也作用于非本实例启动的 ecu.test
