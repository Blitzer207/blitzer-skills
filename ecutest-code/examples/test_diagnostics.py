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
               tbc=os.path.join(workspaceRoot, 'Configurations', 'Testlab_HiL_M_Diag.tbc'),
               tcf=os.path.join(workspaceRoot, 'Configurations', 'SW_Ver_1.tcf')
               )
    yield
    ctrl.stop()

def test_driving_mode():
    """ Integration test to check diagnostics calls. 

    Important note: This test case requires an ecu.test diagnostics license.
    """
    ta = ToolAccess()

    # init test environment
    with ta.init():
        # declare/ register variables
        diagService = ta.diag_var("Engine-Control/Engine_Calib_Start")

        # start execution
        with ta.run():
            # excute diagnostic service
            response = diagService({'Engine_Status': 'OFF', 'Engine_Speed': 0})

            decoded = response.get('decodedResponse')
            assert isinstance(decoded, dict)

            assert decoded.get('SID_PR') == 113
            assert decoded.get('RoutineControlType') == 1
            assert decoded.get('RoutineIdentifier') == 41
            assert decoded.get('Vehicle_Speed') == 42.0
            assert decoded.get('Routine_Start_Status') == 'OK'

if __name__ == "__main__":
    pytest.main()
