import os
import pytest
from ecutest.lifecycle import EcuTestController
from ecutest.toolaccess import ToolAccess, ExecutionResult

os.environ["WEBSOCKETS_MAX_LOG_SIZE"] = "4096"

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

def test_package_run():
    """ Integration test to run a package.
    """
    ta = ToolAccess(request_timeout=10)

    # init test environment
    with ta.init():
        package_path = "RunPackage.pkg"
        # load package
        package = ta.package(package_path)

        with ta.run():
            result = package.run({"a": 2, "b": 3})
        assert result.result_code == ExecutionResult.SUCCESS
        assert result.return_values["result"] == 5


if __name__ == "__main__":
    pytest.main()
