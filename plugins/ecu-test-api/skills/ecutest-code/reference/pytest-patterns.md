# pytest-patterns.md — pytest Fixture 模式

## 模式一：函数式测试（module 级 fixture）

适用于独立的测试函数，每个测试函数内部自己管理 `ToolAccess`。

```python
import os
import pytest
from ecutest.lifecycle import EcuTestController
from ecutest.toolaccess import ToolAccess

@pytest.fixture(scope="module", autouse=True)
def setup_ecutest():
    """启动/停止 ecu.test（整个模块共享一个实例）"""
    workspaceRoot = os.path.join(os.path.dirname(__file__), "ecu.test-code")
    ctrl = EcuTestController()
    ctrl.start(
        workspace=workspaceRoot,
        tbc=os.path.join(workspaceRoot, "Configurations", "Testlab_HiL_M.tbc"),
        tcf=os.path.join(workspaceRoot, "Configurations", "SW_Ver_1.tcf"),
    )
    yield
    ctrl.stop()

def test_driving_mode():
    ta = ToolAccess()
    with ta.init():
        terminal = ta.model_var("Plant model/Model Root/TERMS/Term30 [0|1]/Value")
        battery_soc = ta.meas_var("Battery-Control/SoC")
        with ta.run():
            terminal.write(1)
            assert battery_soc.read() >= 70
```

## 模式二：类式测试（class + function 级 fixture）

适用于多个测试方法共享同一个 `ToolAccess` 连接，每个测试前重置 running 状态。

```python
import os
import pytest
from ecutest.lifecycle import EcuTestController
from ecutest.toolaccess import ToolAccess

class TestVehicle:
    ta: ToolAccess

    @pytest.fixture(scope="module", autouse=True)
    def setup_ecutest(self):
        """启动/停止 ecu.test（module 级）"""
        workspaceRoot = os.path.join(os.path.dirname(__file__), "ecu.test-code")
        ctrl = EcuTestController()
        ctrl.start(
            workspace=workspaceRoot,
            tbc=os.path.join(workspaceRoot, "Configurations", "Testlab_HiL_M.tbc"),
            tcf=os.path.join(workspaceRoot, "Configurations", "SW_Ver_1.tcf"),
            allow_restart=True,
        )
        yield
        ctrl.stop()

    @pytest.fixture(scope="class", autouse=True)
    def ta_setup(self, request):
        """整个 class 共享一个 ToolAccess 连接（initialized 状态）"""
        request.cls.ta = ToolAccess()
        request.cls.ta.init()
        self.register_vars()        # 在 initialized 状态注册所有变量
        yield
        request.cls.ta.deinit()

    @pytest.fixture(autouse=True)
    def ta_run(self):
        """每个测试函数前 run，结束后 stop（重置模型变量）"""
        self.ta.run()
        yield
        self.ta.stop()

    @classmethod
    def register_vars(cls) -> None:
        # model variables
        cls.starter_button = cls.ta.model_var(
            "Plant model/Model Root/CTRL_VEH/StarterButton [-1|0|1]/Value"
        )
        cls.driver_req = cls.ta.model_var(
            "Plant model/Model Root/CTRL_VEH/DriverRequest [%]/Value"
        )
        # measurement variables
        cls.velocity_ecu = cls.ta.meas_var("Engine-Control/speed")
        # bus signal
        cls.velocity_bus = cls.ta.bus_signal(
            "EPT-CAN/ELECTRIC_POWER_TRAIN/VEH_DATA/VEH_DATA/VEHICLE_VELOCITY"
        )

    def test_acceleration(self):
        self.starter_button.write(1)
        self.ta.simu_wait(1)
        self.starter_button.write(0)
        self.driver_req.write(50)
        self.ta.simu_wait(10)
        assert self.velocity_bus.read() > 30
        assert self.velocity_ecu.read() > 30
```

## 两种模式对比

| | 函数式 | 类式 |
|--|--------|------|
| ToolAccess 生命周期 | 每个测试函数独立 | class 内共享（init 一次） |
| 变量注册 | 每个测试函数内注册 | `register_vars()` 统一注册 |
| 适用场景 | 测试间无共享状态 | 多测试共享同一组变量 |
| fixture scope | module（ecu.test）| module + class + function |

## 注意事项

- `scope="module"` 的 fixture 在类方法中需要声明为实例方法（`self`），但实际 scope 仍是 module
- `ta_run` fixture 每次 `stop()` 会触发 ecu.test 恢复模型变量默认值，适合需要隔离的测试
- 类式模式中 `register_vars` 必须在 `ta.init()` 之后、`ta.run()` 之前调用
