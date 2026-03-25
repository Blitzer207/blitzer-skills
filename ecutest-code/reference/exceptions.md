# exceptions.md — 异常类型

所有异常继承自 `EcuTestCodeError`，可统一捕获。

```python
from ecutest.exceptions import (
    EcuTestCodeError,
    StateError,
    RemoteError,
    NotRegisteredError,
    TimeoutError,
    AuthenticationError,
    IncompatibleVersionError,
    PendingRequestError,
    SocketNotReadyError,
    EventNotSubscribedError,
)
```

## 异常速查

| 异常 | 触发场景 | 处理建议 |
|------|---------|---------|
| `StateError` | 在错误状态调用方法（如 uninitialized 时注册变量，running 时调用 `finish()`） | 检查状态机流程，确保 `init()`/`run()` 顺序正确 |
| `RemoteError` | ecu.test 内部抛出异常（路径错误、信号不存在等） | 检查变量/job 路径，查看 ecu.test 日志 |
| `NotRegisteredError` | 使用未通过工厂方法注册的变量或 job | 用 `ta.model_var()`、`ta.job()` 等方法注册后再使用 |
| `TimeoutError` | ecu.test 在 `request_timeout` 内未响应 | 增大 `ToolAccess(request_timeout=...)` 或检查 ecu.test 是否卡住 |
| `AuthenticationError` | ecu.test 无法验证客户端 | 检查 ecu.test 是否正常启动，web API 是否激活 |
| `IncompatibleVersionError` | ecutest_code 与 ecu.test 版本不兼容 | 对齐 pip 包版本与 ecu.test 安装版本 |
| `PendingRequestError` | 上一个请求未完成就发起新请求 | 串行化调用；并行需求用独立 `ToolAccess` 实例（注意：不支持并发 session） |
| `SocketNotReadyError` | 连接建立前就发送请求 | 确保 `ta.init()` 完成后再操作 |
| `EventNotSubscribedError` | 调用需要特定事件订阅的方法，但未订阅 | 通常不会出现（`ToolAccess` 已自动订阅所需事件） |

## 典型捕获模式

```python
from ecutest.exceptions import RemoteError, StateError

try:
    with ta.init():
        var = ta.model_var("some/path")
        with ta.run():
            val = var.read()
except StateError as e:
    print(f"状态错误，检查 init/run 顺序: {e}")
except RemoteError as e:
    print(f"ecu.test 内部错误，检查路径或配置: {e}")
except TimeoutError as e:
    print(f"超时，ecu.test 可能无响应: {e}")
```
