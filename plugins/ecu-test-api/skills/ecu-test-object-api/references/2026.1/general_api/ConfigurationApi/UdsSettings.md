[![logo](../../_static/ecu.test.svg)](../../index.html "API  documentation") API documentation

[ Internal APIs ](../api.md)

[ Advanced operations of package variable types ](../variabledatastructures.md)

[ Advanced properties of bus-related objects ](../busdatastructures.md)

[ Bus related objects of trace analysis ](../busdatastructuresTraceanalysis.md)

[ Advanced properties of diagnostics-related objects ](../diagdatastructures.md)

[ Diagnostics related objects of trace analysis ](../diagdatastructuresTraceanalysis.md)

[ Advanced properties of media-related objects ](../mediadatastructures.md)

[ Advanced properties of DLT logging-related objects ](../dltdatastructures.md)

[ COM API ](../com-api.md)

[ REST API ](../rest-api.md)

[ Report API ](../apireport.md)

[ Object API ](../objectApi.md)

Object API

[ API entry points ](../objectApi.md#api-entry-points)

API entry points

[ API for Analysis Jobs ](../AnalysisJobApi.md)

[ API for Artifacts ](../ArtifactApi.md)

[ API for Project Components ](../ComponentApi.md)

[ API for Configurations ](../ConfigurationApi.md)

API for Configurations

[ Bus ](Bus.md)

[ BusAccess ](BusAccess.md)

[ CanIsoTpSettings ](CanIsoTpSettings.md)

[ Change ](Change.md)

[ Common ](Common.md)

[ ControlUnit ](ControlUnit.md)

[ ControlUnits ](ControlUnits.md)

[ DiagSettings ](DiagSettings.md)

[ DoIpSettings ](DoIpSettings.md)

[ DoSoAdSettings ](DoSoAdSettings.md)

[ EnvComAccess ](EnvComAccess.md)

[ EnvComData ](EnvComData.md)

[ EnvSimAccess ](EnvSimAccess.md)

[ EnvSimData ](EnvSimData.md)

[ Environment ](Environment.md)

[ Execution ](Execution.md)

[ FailureSimulation ](FailureSimulation.md)

[ FailureSimulationAccess ](FailureSimulationAccess.md)

[ FrTpSettings ](FrTpSettings.md)

[ Function ](Function.md)

[ FunctionAccess ](FunctionAccess.md)

[ HSFZSettings ](HSFZSettings.md)

[ Media ](Media.md)

[ MediaAccess ](MediaAccess.md)

[ Model ](Model.md)

[ ModelAccess ](ModelAccess.md)

[ Platform ](Platform.md)

[ Port ](Port.md)

[ Property ](Property.md)

[ PropertySet ](PropertySet.md)

[ ReportData ](ReportData.md)

[ ReportFormat ](ReportFormat.md)

[ TestBenchConfiguration ](TestBenchConfiguration.md)

[ TestConfiguration ](TestConfiguration.md)

[ TestConfigurationGlobalConstants ](TestConfigurationGlobalConstants.md)

[ Tool ](Tool.md)

[ ToolHost ](ToolHost.md)

UdsSettings [ UdsSettings ](#)

UdsSettings

- [C UdsSettings ](#ApiClient.UdsSettings)
  - [M Clone ](#ApiClient.UdsSettings.Clone)
  - [M GetAutostart ](#ApiClient.UdsSettings.GetAutostart)
  - [M GetStartRequest ](#ApiClient.UdsSettings.GetStartRequest)
  - [M GetStopRequest ](#ApiClient.UdsSettings.GetStopRequest)
  - [M GetTesterPresentCycleTime ](#ApiClient.UdsSettings.GetTesterPresentCycleTime)
  - [M GetTesterPresentRequest ](#ApiClient.UdsSettings.GetTesterPresentRequest)
  - [M SetAutostart ](#ApiClient.UdsSettings.SetAutostart)
  - [M SetStartRequest ](#ApiClient.UdsSettings.SetStartRequest)
  - [M SetStopRequest ](#ApiClient.UdsSettings.SetStopRequest)
  - [M SetTesterPresentCycleTime ](#ApiClient.UdsSettings.SetTesterPresentCycleTime)
  - [M SetTesterPresentRequest ](#ApiClient.UdsSettings.SetTesterPresentRequest)

[ UserReportData ](UserReportData.md)

[ ValueDifference ](ValueDifference.md)

[ API for Expectations ](../ExpectationApi.md)

[ API for Expressions ](../ExpressionApi.md)

[ API for Global Mappings ](../GlobalMappingApi.md)

[ API for Mappings ](../MappingApi.md)

[ API for Multimedia Objects ](../MultimediaApi.md)

[ API for Packages ](../PackageApi.md)

[ API for Parameters ](../ParameterApi.md)

[ API for Projects ](../ProjectApi.md)

[ API for Relations ](../RelationApi.md)

[ API for Reports ](../ReportApi.md)

[ API for Report Filters ](../ReportFilterApi.md)

[ API for Settings ](../SettingsApi.md)

[ API for Signals ](../SignalApi.md)

[ API for Signal Descriptions ](../SignalDescriptionApi.md)

[ API for Signal Recordings ](../SignalRecordingApi.md)

[ API for Symbols ](../SymbolApi.md)

[ API for Test Steps ](../TestStepApi.md)

[ API for Touch Inputs ](../TouchInputApi.md)

[ API for Trace Analyses ](../TraceAnalysisApi.md)

[ API for Trace Files ](../TraceFileApi.md)

[ API for Trace Step Templates ](../TraceStepTemplateApi.md)

[ API for Variables ](../VariableApi.md)

[ API for Workspaces ](../WorkspaceApi.md)

[ Trace Analysis API ](../../TraceAnalysisAPI/index.md)

[ Generator APIs ](../../generators/index.md)

[ Tools ](../../tools/index.md)

[ User test management ](../../userTestmanagement/index.md)

[ UserUtility API ](../../user-utility/user-utility.md)

[ Utility Examples ](../../user-utility/example-utilities.md)

UdsSettings

- [C UdsSettings ](#ApiClient.UdsSettings)
  - [M Clone ](#ApiClient.UdsSettings.Clone)
  - [M GetAutostart ](#ApiClient.UdsSettings.GetAutostart)
  - [M GetStartRequest ](#ApiClient.UdsSettings.GetStartRequest)
  - [M GetStopRequest ](#ApiClient.UdsSettings.GetStopRequest)
  - [M GetTesterPresentCycleTime ](#ApiClient.UdsSettings.GetTesterPresentCycleTime)
  - [M GetTesterPresentRequest ](#ApiClient.UdsSettings.GetTesterPresentRequest)
  - [M SetAutostart ](#ApiClient.UdsSettings.SetAutostart)
  - [M SetStartRequest ](#ApiClient.UdsSettings.SetStartRequest)
  - [M SetStopRequest ](#ApiClient.UdsSettings.SetStopRequest)
  - [M SetTesterPresentCycleTime ](#ApiClient.UdsSettings.SetTesterPresentCycleTime)
  - [M SetTesterPresentRequest ](#ApiClient.UdsSettings.SetTesterPresentRequest)

# UdsSettings[¶](#udssettings "Link to this heading")

*class* UdsSettings[¶](#ApiClient.UdsSettings "Link to this definition")  
Clone()[¶](#ApiClient.UdsSettings.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`UdsSettings`](#ApiClient.UdsSettings "ApiClient.UdsSettings (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")

GetAutostart()[¶](#ApiClient.UdsSettings.GetAutostart "Link to this definition")  
Returns the Autostart.

Automatically start the diagnostic session at the beginning of the test case. Use the job OpenTCFDiagSession to start the session if this option is not checked.

Returns:  Autostart

Return type:  bool

GetStartRequest()[¶](#ApiClient.UdsSettings.GetStartRequest "Link to this definition")  
Returns the StartRequest.

Here: Only the byte sequence in format “AA:BB:01”.

Diagnostic request to open a session (optional) - ByteStream

Returns:  StartRequest

Return type:  str

GetStopRequest()[¶](#ApiClient.UdsSettings.GetStopRequest "Link to this definition")  
Returns the StopRequest.

Here: Only the byte sequence in format “AA:BB:01”.

Diagnostic request to end a session (optional) - ByteStream

Returns:  StopRequest

Return type:  str

GetTesterPresentCycleTime()[¶](#ApiClient.UdsSettings.GetTesterPresentCycleTime "Link to this definition")  
Returns the TesterPresentCycleTime.

Period length (ms) for cyclic tester-available signaling (optional) - Integer

Returns:  TesterPresentCycleTime

Return type:  int

GetTesterPresentRequest()[¶](#ApiClient.UdsSettings.GetTesterPresentRequest "Link to this definition")  
Returns the TesterPresentRequest.

Here: Only the byte sequence in format “AA:BB:01”.

Diagnostic request for periodic tester-available signaling (optional) - ByteStream

Returns:  TesterPresentRequest

Return type:  str

SetAutostart(*[value](#ApiClient.UdsSettings.SetAutostart.value "ApiClient.UdsSettings.SetAutostart.value (Python parameter) — Autostart")*)[¶](#ApiClient.UdsSettings.SetAutostart "Link to this definition")  
Sets the Autostart.

Automatically start the diagnostic session at the beginning of the test case. Use the job OpenTCFDiagSession to start the session if this option is not checked.

Parameters:  value : bool[¶](#ApiClient.UdsSettings.SetAutostart.value "Permalink to this definition")  
Autostart

SetStartRequest(*[value](#ApiClient.UdsSettings.SetStartRequest.value "ApiClient.UdsSettings.SetStartRequest.value (Python parameter) — StartRequest")*)[¶](#ApiClient.UdsSettings.SetStartRequest "Link to this definition")  
Sets the StartRequest.

Here: Only the byte sequence in format “AA:BB:01”.

Diagnostic request to open a session (optional) - ByteStream

Parameters:  value : str[¶](#ApiClient.UdsSettings.SetStartRequest.value "Permalink to this definition")  
StartRequest

SetStopRequest(*[value](#ApiClient.UdsSettings.SetStopRequest.value "ApiClient.UdsSettings.SetStopRequest.value (Python parameter) — StopRequest")*)[¶](#ApiClient.UdsSettings.SetStopRequest "Link to this definition")  
Sets the StopRequest.

Here: Only the byte sequence in format “AA:BB:01”.

Diagnostic request to end a session (optional) - ByteStream

Parameters:  value : str[¶](#ApiClient.UdsSettings.SetStopRequest.value "Permalink to this definition")  
StopRequest

SetTesterPresentCycleTime(*[value](#ApiClient.UdsSettings.SetTesterPresentCycleTime.value "ApiClient.UdsSettings.SetTesterPresentCycleTime.value (Python parameter) — TesterPresentCycleTime")*)[¶](#ApiClient.UdsSettings.SetTesterPresentCycleTime "Link to this definition")  
Sets the TesterPresentCycleTime.

Period length (ms) for cyclic tester-available signaling (optional) - Integer

Parameters:  value : int[¶](#ApiClient.UdsSettings.SetTesterPresentCycleTime.value "Permalink to this definition")  
TesterPresentCycleTime

SetTesterPresentRequest(*[value](#ApiClient.UdsSettings.SetTesterPresentRequest.value "ApiClient.UdsSettings.SetTesterPresentRequest.value (Python parameter) — TesterPresentRequest")*)[¶](#ApiClient.UdsSettings.SetTesterPresentRequest "Link to this definition")  
Sets the TesterPresentRequest.

Here: Only the byte sequence in format “AA:BB:01”.

Diagnostic request for periodic tester-available signaling (optional) - ByteStream

Parameters:  value : str[¶](#ApiClient.UdsSettings.SetTesterPresentRequest.value "Permalink to this definition")  
TesterPresentRequest

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
