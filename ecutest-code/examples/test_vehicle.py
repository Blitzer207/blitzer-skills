import os
import pytest
from ecutest.lifecycle import EcuTestController
from ecutest.toolaccess import ToolAccess

class TestVehicle:
    ta: ToolAccess

    @pytest.fixture(scope="module", autouse=True)
    def setup_ecutest(self):
        """
        starts and stops ecu.test for the test module via the lifecycle api.
        """
        workspaceRoot = os.path.join(os.path.dirname(__file__), "ecu.test-code")
        ctrl = EcuTestController()
        ctrl.start(workspace=workspaceRoot,
                tbc=os.path.join(workspaceRoot, 'Configurations', 'Testlab_HiL_M.tbc'),
                tcf=os.path.join(workspaceRoot, 'Configurations', 'SW_Ver_1.tcf'),
                allow_restart=True
                )
        yield
        ctrl.stop()

    @pytest.fixture(scope="class", autouse=True)
    def ta_setup(self, request):
        # connect to ecu.test once for the test class
        request.cls.ta = ToolAccess()
        request.cls.ta.init()
        self.register_vars()
        yield
        request.cls.ta.deinit()

    @pytest.fixture(autouse=True)
    def ta_run(self):
        # start ToolAccess execution before each test function again to reset
        # overwritten model variables.
        self.ta.run()
        yield
        self.ta.stop()

    @classmethod
    def register_vars(cls) -> None:
        # model variables
        cls.starter_button = cls.ta.model_var('Plant model/Model Root/CTRL_VEH/StarterButton [-1|0|1]/Value')
        cls.traction_standby = cls.ta.model_var('Plant model/Model Root/STATUS_VEH/VehicleTractionStandby [0|1]/In1')
        cls.driver_req = cls.ta.model_var('Plant model/Model Root/CTRL_VEH/DriverRequest [%]/Value')
        cls.drive_mode = cls.ta.model_var('Plant model/Model Root/CTRL_VEH/DriveMode [0|1|2|3|4]/Value')

        # measurement variables
        cls.velocity_ecu = cls.ta.meas_var('Engine-Control/speed')
        cls.recuperation = cls.ta.meas_var('Engine-Control/recup')
        cls.soc = cls.ta.meas_var('Battery-Control/SoC')

        # bus signal
        cls.velocity_bus = cls.ta.bus_signal('EPT-CAN/ELECTRIC_POWER_TRAIN/VEH_DATA/VEH_DATA/VEHICLE_VELOCITY')


    def start_ignition(self) -> None:
        self.starter_button.write(1)
        self.ta.simu_wait(1)
        self.starter_button.write(0)

    def test_ignition_on(self):
        self.start_ignition()
        assert self.traction_standby.read() == 1

    def test_ignition_off(self):
        self.starter_button.write(-1)
        self.ta.simu_wait(1)
        self.starter_button.write(0)
        self.ta.simu_wait(1)
        assert self.traction_standby.read() == 0

    def test_acceleration(self):
        self.starter_button.write(1)
        self.ta.simu_wait(1)
        self.starter_button.write(0)
        self.ta.simu_wait(1)
        # accelerate for 10 seconds
        self.driver_req.write(50)
        self.ta.simu_wait(10)
        # check vehicle speed
        assert self.velocity_bus.read() > 30
        assert self.velocity_ecu.read() > 30

    def test_recuperation(self):
        self.start_ignition()
        self.ta.simu_wait(1)
        # set drive mode
        self.drive_mode.write(4)
        self.ta.simu_wait(1)
        # accelerate
        self.driver_req.write(50)
        self.ta.simu_wait(10)
        # stop acceleration and check whether recuperation is active
        self.driver_req.write(0)
        self.ta.simu_wait(2)
        assert self.recuperation.read() == 1

    def test_soc_decreasing(self):
        self.start_ignition()
        self.ta.simu_wait(1)
        # accelerate
        self.driver_req.write(50)
        self.ta.simu_wait(5)
        # ensure the vehicle's state of charge is decreasing over time
        soc = self.soc.read()
        self.ta.simu_wait(5)
        assert self.soc.read() < soc
