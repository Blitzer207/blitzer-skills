# advanced.md — Recording / Package / DiagVar

## Recording

```python
with ta.init():
    var1 = ta.model_var("Plant model/Model Root/CTRL_VEH/DriveMode [0|1|2|3|4]/Value")
    var2 = ta.model_var("Plant model/Model Root/TERMS/Term30 [0|1]/Value")

    # 在 initialized 状态创建（变量自动注册到 recording）
    rec = ta.recording("C:\\temp\\output", [var1, var2])

    with ta.run():
        rec.start()
        # ... 操作 ...
        rec.stop()

        # 可多次 start/stop
        rec.start()
        ta.simu_wait(1)
        rec.stop()

    # finish() 必须在 ta.run() context 外（initialized 状态）调用
    recording_infos = rec.finish()

for info in recording_infos:       # 每个 start/stop 对对应一个元素
    print(info["type"])            # 录制格式
    for file in info["files"]:     # 通常一个文件，极少情况多个
        print(file)
        os.unlink(file)            # 处理完后可删除
```

注意：
- `rec.finish()` 返回 `list[dict]`，每个元素对应一次 start/stop 对
- 文件扩展名由 ecu.test 自动添加，若文件已存在会自动加后缀避免覆盖
- 所有变量必须来自同一个 port；跨 port 时只录制多数 port 的变量
- `ta.stop()` 时所有未 finish 的 recording 自动 stop，但数据会丢失

## Package

```python
from ecutest.toolaccess import ToolAccess, ExecutionResult

ta = ToolAccess(request_timeout=30)     # 长耗时 package 需增大超时

with ta.init():
    pkg = ta.package("RunPackage.pkg")  # 相对 workspace 的路径

    with ta.run():
        result = pkg.run({"a": 2, "b": 3})  # 参数字典，无参数传 None 或省略

    assert result.result_code == ExecutionResult.SUCCESS
    assert result.return_values["result"] == 5
```

`ExecutionResult` 枚举值：

| 值 | 含义 |
|----|------|
| `NONE` (0) | 无结果 |
| `SUCCESS` (1) | 成功 |
| `INCONCLUSIVE` (2) | 不确定 |
| `FAILED` (4) | 失败 |
| `ERROR` (8) | 错误 |

Package 不支持的步骤类型：
- 子 package 调用
- 打开对话框的步骤
- 并行 package / Inbox/Outbox 变量
- Report、Log File Entry、Assertion、Exit、Precondition、Postcondition
- Start/Stop/Add Trace、Set Trace Comment、Request Analysis
- Start/Stop Stimulus、EES/FIU 步骤

## DiagVar（诊断服务）

> 需要 ecu.test 诊断 license

```python
with ta.init():
    svc = ta.diag_var("Engine-Control/Engine_Calib_Start")
    # 路径格式：<控制单元标识符>/<诊断服务名>

    with ta.run():
        # 传入参数字典
        response = svc({"Engine_Status": "OFF", "Engine_Speed": 0})
        # 或用 param 关键字
        response = svc(param={"Engine_Status": "OFF", "Engine_Speed": 0})

        decoded = response.get("decodedResponse")   # dict
        assert decoded["SID_PR"] == 113
        assert decoded["Routine_Start_Status"] == "OK"
```

## 常见错误速查

| 错误 | 原因 | 解决 |
|------|------|------|
| `StateError: Initialize with ToolAccess.init()` | 在 uninitialized 状态注册变量 | 先调用 `ta.init()` |
| `StateError: Start with ToolAccess.run()` | 在 initialized 状态读写变量 | 先调用 `ta.run()` |
| `StateError: only allowed in a stopped state` | 在 running 状态调用 `recording.finish()` 或注册变量 | 在 `ta.run()` context 外调用 |
| `NotRegisteredError` | 使用未注册的变量 | 用 `ta.model_var()` 等工厂方法注册 |
| `RemoteError` | ecu.test 内部抛出异常 | 检查路径是否正确，查看 ecu.test 日志 |
| `TimeoutError` | ecu.test 无响应 | 增大 `request_timeout`，确认 ecu.test 正在运行 |
| `AuthenticationError` | ecu.test 无法验证客户端 | 检查 ecu.test 是否正常启动 |
| `IncompatibleVersionError` | ecutest_code 与 ecu.test 版本不兼容 | 对齐版本 |
| `RuntimeError: ecu.test is already running, but in the wrong workspace` | workspace 不匹配 | 添加 `allow_restart=True` |
| `PendingRequestError` | 上一个请求未完成就发起新请求 | 串行化调用，或使用独立的 ToolAccess 实例 |
