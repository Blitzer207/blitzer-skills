import os
import pytest
from ecutest.lifecycle import EcuTestController
from ecutest.toolaccess import ToolAccess

@pytest.fixture(scope="module", autouse=True)
def setup_ecutest():
    """
    starts and stops ecu.test for the test module via the lifecycle api.
    """
    workspaceRoot = os.path.join(os.path.dirname(__file__), "ecu.test-code")
    ctrl = EcuTestController()
    ctrl.start(workspace=workspaceRoot,
               tbc=os.path.join(workspaceRoot, 'Configurations', 'Testlab_HiL_M.tbc'),
               tcf=os.path.join(workspaceRoot, 'Configurations', 'SW_Ver_1.tcf')
               )
    yield
    ctrl.stop()

def test_driving_mode():
    """ Integration test to check driving mode.
    It's using bus, model and measurement interfaces based on arxml, a2l and model description.
    """
    ta = ToolAccess()

    # init test environment
    with ta.init():
        # declare/ register variables
        terminal = ta.model_var("Plant model/Model Root/TERMS/Term30 [0|1]/Value")
        battery_soc = ta.meas_var("Battery-Control/SoC")
        bus_driving_mode = ta.bus_signal("EPT-CAN/ELECTRIC_POWER_TRAIN/CONTROL_SIGNALS_BUS/CONTROL_SIGNALS_BUS/DRIVING_MODE")
        model_driving_mode = ta.model_var("Plant model/Model Root/CTRL_VEH/DriveMode [0|1|2|3|4]/Value")
        inca_check_connection = ta.job("INCA/CheckAllConnections")

        rec = ta.recording("C:\\temp\\recording", [terminal, model_driving_mode])

        # start execution
        with ta.run():
            rec.start()
            # precondition
            print(inca_check_connection())
            terminal.write(1)
            print(f"SoC: {battery_soc.read()}")
            assert battery_soc.read() >= 70

            # action
            model_driving_mode.write(1)
            assert bus_driving_mode.read() == model_driving_mode.read() == 1
            rec.stop()

            # create a second recording
            rec.start()
            ta.simu_wait(1)
            rec.stop()
        recordingInfos = rec.finish()
    for recIdx, recording in enumerate(recordingInfos):
        print(f"Recording #{recIdx} is in { recording['type']} format")
        for fileIdx, recordedFile in enumerate(recording['files']):
            print(f"    File #{fileIdx} is at {recordedFile}")
            # TODO: inspect or archive the file
            os.unlink(recordedFile)


if __name__ == "__main__":
    pytest.main()
