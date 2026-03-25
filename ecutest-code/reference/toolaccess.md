# toolaccess.md — ToolAccess

## 两种用法

### Context Manager（推荐，函数式测试）

```python
from ecutest.toolaccess import ToolAccess

ta = ToolAccess()
with ta.init() as ta:               # → initialized
    job = ta.job("PORT/MyJob")
    var = ta.model_var("Model/Root/Signal/Value")
    with ta.run():                  # → running
        result = job(1, 2)
        val = var.read()
        var.write(42)
    # 自动 stop → initialized
# 自动 deinit → uninitialized
```

### 显式调用（类式测试，pytest class fixture 中使用）

```python
ta = ToolAccess()
ta.init()                           # → initialized
job = ta.job("PORT/MyJob")
ta.run()                            # → running
result = job(1, 2)
ta.stop()                           # → initialized
ta.deinit()                         # → uninitialized
```

## 构造函数参数

```python
ta = ToolAccess(
    init_timeout=10.0,      # 建立连接的最大等待时间（秒）
    request_timeout=10.0    # 每次 API 调用超时（秒），长耗时 job 需增大
)
```

## 变量类型速查

所有变量必须在 **initialized** 状态注册，在 **running** 状态读写。

| 方法 | 返回类型 | 用途 |
|------|---------|------|
| `ta.model_var(path)` | `ModelVar` | 仿真模型信号 |
| `ta.meas_var(path)` | `MeasVar` | ECU 测量值 |
| `ta.calib_var(path)` | `CalibVar` | 标定变量 |
| `ta.bus_signal(path)` | `BusSignal` | 总线信号（CAN 等） |
| `ta.job(path)` | `Job` | 可调用的 ecu.test job |
| `ta.diag_var(path)` | `DiagVar` | 诊断服务（需诊断 license） |
| `ta.package(path)` | `Package` | ecu.test package |
| `ta.recording(dest, vars)` | `Recording` | 信号录制 |

路径格式示例：
```python
ta.model_var("Plant model/Model Root/CTRL_VEH/DriveMode [0|1|2|3|4]/Value")
ta.meas_var("Engine-Control/speed")
ta.bus_signal("EPT-CAN/ELECTRIC_POWER_TRAIN/VEH_DATA/VEH_DATA/VEHICLE_VELOCITY")
ta.job("INCA/CheckAllConnections")
ta.diag_var("Engine-Control/Read_data_by_identifier")
ta.package("RunPackage.pkg")        # 相对 workspace 的路径
```

## 读写操作

```python
# 在 running 状态
val = var.read()                    # 返回 str | int | float | list | tuple | None
var.write(42)
var.write("ON")

ta.simu_wait(1.0)                   # 等待 1 秒（基于 ecu.test 时间基准）
```

## 注意事项

- 所有变量/job 必须通过工厂方法创建，**不要手动实例化** `ModelVar`、`Job` 等类
- 重复调用同名注册方法返回已注册实例，不会重复注册（幂等）
- 进程意外终止时，ecu.test 自动检测连接断开并恢复初始状态
