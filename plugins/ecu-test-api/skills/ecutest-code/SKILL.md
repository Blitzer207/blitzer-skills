---
name: ecutest-code
description: Use when writing Python automation tests with ecutest_code library for ecu.test. Covers ToolAccess state lifecycle, variable registration, job/diag calls, recording, packages, pytest fixture patterns, and test.guide integration.
---

# ecutest-code

## Overview

`ecutest_code` 是驱动 ecu.test 自动化测试的 Python 库。核心是 `ToolAccess`，通过三态状态机管理与 ecu.test 的连接。

- pip 包名: `ecutest_code`，import 名: `ecutest`
- 最低要求: Python 3.12，ecu.test 2026.1

```python
from ecutest.lifecycle import EcuTestController
from ecutest.toolaccess import ToolAccess, ExecutionResult
from ecutest.exceptions import StateError, RemoteError, NotRegisteredError
```

## 状态模型（核心）

```
uninitialized  →(init)→  initialized  →(run)→  running
               ←(deinit)←             ←(stop)←
```

| 状态 | 可做的事 |
|------|---------|
| uninitialized | 无连接，仅可调用 `init()` |
| initialized | 注册变量/job/package，创建 recording，调用 `recording.finish()` |
| running | 读写变量，调用 job，`simu_wait`，start/stop recording |

## LSP 使用规则（必读）

**写代码前必须用 LSP 验证 API，不要凭记忆猜方法名或参数。**

目标文件（在实际使用处操作，不要在 import 行操作）：
- `ToolAccess` 方法：`.venv/Lib/site-packages/ecutest/toolaccess.py`
- `EcuTestController` 方法：`.venv/Lib/site-packages/ecutest/lifecycle.py`
- 异常类型：`.venv/Lib/site-packages/ecutest/exceptions.py`

常用操作：
- `documentSymbol` — 列出文件中所有类和方法，快速确认方法是否存在
- `hover` — 查看方法签名、参数类型、返回值
- `goToDefinition` — 跳转到类/方法定义，查看完整实现
- `findReferences` — 确认某个类/方法的实际用法

> LSP 首次调用可能返回 "server is starting"，等几秒后重试。

## 文件索引

### reference/

| 文件 | 内容 |
|------|------|
| `reference/lifecycle.md` | EcuTestController：启动/停止 ecu.test，workspace/tbc/tcf 配置 |
| `reference/toolaccess.md` | ToolAccess 两种用法，变量类型速查，超时参数 |
| `reference/pytest-patterns.md` | pytest fixture 两种完整模板（函数式 / 类式） |
| `reference/advanced.md` | Recording、Package、DiagVar 用法，常见错误表 |
| `reference/exceptions.md` | 所有异常类型及含义 |
| `reference/testguide-plugin.md` | test.guide 上传插件：CLI 选项、环境变量、ini 配置 |

### examples/

| 文件 | 内容 |
|------|------|
| `examples/test_driving_mode.py` | 函数式测试：model_var、meas_var、bus_signal、job、recording |
| `examples/test_vehicle.py` | 类式测试：class fixture、多变量共享、simu_wait |
| `examples/test_packages.py` | Package 调用：参数传递、ExecutionResult 检查 |
| `examples/test_diagnostics.py` | DiagVar 调用：诊断服务请求与响应解析 |
