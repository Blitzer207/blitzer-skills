[ Internal APIs ](api.md)

[ Advanced operations of package variable types ](variabledatastructures.md)

[ Advanced properties of bus-related objects ](busdatastructures.md)

[ Bus related objects of trace analysis ](busdatastructuresTraceanalysis.md)

[ Advanced properties of diagnostics-related objects ](diagdatastructures.md)

[ Diagnostics related objects of trace analysis ](diagdatastructuresTraceanalysis.md)

[ Advanced properties of media-related objects ](mediadatastructures.md)

[ Advanced properties of DLT logging-related objects ](dltdatastructures.md)

[ COM API ](com-api.md)

[ REST API ](#)

[ Report API ](apireport.md)

[ Object API ](objectApi.md)

[ Trace Analysis API ](../TraceAnalysisAPI/index.md)

[ Generator APIs ](../generators/index.md)

[ Tools ](../tools/index.md)

[ User test management ](../userTestmanagement/index.md)

[ UserUtility API ](../user-utility/user-utility.md)

[ Utility Examples ](../user-utility/example-utilities.md)

# REST API[¶](#rest-api "Link to this heading")

To control the test execution remote of ecu.test, an OpenAPI based REST API exists as an alternative to the COM API. It is available on both Windows and Linux.

When ecu.test is started, the API base path is locally available at http://127.0.0.1:5050/api/v2. An interactive OpenAPI documentation is accessible at [127.0.0.1:5050/api/v2/ui](http://127.0.0.1:5050/api/v2/ui). By default, the API is only available locally. For remote access, start ecu.test with the command line option `--restApiEnableRemoteAccess`. In order to change the default port use the command line option `--restApiPort PORT`and replace “PORT” with a suitable port number.

A sample workflow with Python can look like this:

    from time import sleep
    import requests

    def WaitForOperationEnd(infoEndpoint):
        while True:
            info = requests.get(infoEndpoint)
            currentStatus = info.json()['status']['key']
            if currentStatus not in ['WAITING', 'RUNNING']:
                print(f'Finished! The status is {currentStatus}.')
                return info
            sleep(1)

    BASE_URL = 'http://127.0.0.1:5050/api/v2'
    LIVE_ENDPOINT = f'{BASE_URL}/live'
    CONFIGURATION_ENDPOINT = f'{BASE_URL}/configuration'
    EXECUTION_ENDPOINT = f'{BASE_URL}/execution'

    # Check if API is reachable
    try:
        requests.get(LIVE_ENDPOINT)
    except requests.exceptions.ConnectionError:
        raise RuntimeError('Cannot connect to ecu.test')

    # Load a TBC and TCF
    myConfigurationOrder = {
        'action': 'Start',
        'tbc': {
            'tbcPath': 'MyTestbenchConfiguration.tbc',
        },
        'tcf': {
            'tcfPath': 'MyTestConfiguration.tcf'
        }
    }
    response = requests.put(CONFIGURATION_ENDPOINT, json=myConfigurationOrder)
    response.raise_for_status()  # Check if something went wrong

    # Check if TBC and TCF are started
    configurationInfo = WaitForOperationEnd(CONFIGURATION_ENDPOINT)

    # Trigger a test run
    myExecutionOrder = {
        'testCasePath': 'MyPackage.pkg',
    }
    response = requests.put(EXECUTION_ENDPOINT, json=myExecutionOrder)
    response.raise_for_status()  # Check if something went wrong

    # Check if test run has finished
    executionInfo = WaitForOperationEnd(EXECUTION_ENDPOINT)

    # Upload the report to a test.guide instance
    reportId = executionInfo.json()['result']['testReportId']
    uploadEndpoint = f'{BASE_URL}/reports/{reportId}/upload'
    myUploadOrder = {
        'testGuideUrl': 'https://myTestGuideHost:1234',
        'authKey': 'abc123',
        'projectId': 3,
    }
    response = requests.put(uploadEndpoint, json=myUploadOrder)
    response.raise_for_status()  # Check if something went wrong

    # Check if upload has finished
    WaitForOperationEnd(uploadEndpoint)

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
