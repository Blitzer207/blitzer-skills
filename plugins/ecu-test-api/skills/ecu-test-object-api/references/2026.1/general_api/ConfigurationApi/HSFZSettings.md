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

HSFZSettings [ HSFZSettings ](#)

HSFZSettings

- [C HSFZSettings ](#ApiClient.HSFZSettings)
  - [M Clone ](#ApiClient.HSFZSettings.Clone)
  - [M GetDiagTimeoutHsfz ](#ApiClient.HSFZSettings.GetDiagTimeoutHsfz)
  - [M GetRemotePort ](#ApiClient.HSFZSettings.GetRemotePort)
  - [M GetSourceAddress ](#ApiClient.HSFZSettings.GetSourceAddress)
  - [M GetTargetAddress ](#ApiClient.HSFZSettings.GetTargetAddress)
  - [M GetTargetIp ](#ApiClient.HSFZSettings.GetTargetIp)
  - [M SetDiagTimeoutHsfz ](#ApiClient.HSFZSettings.SetDiagTimeoutHsfz)
  - [M SetRemotePort ](#ApiClient.HSFZSettings.SetRemotePort)
  - [M SetSourceAddress ](#ApiClient.HSFZSettings.SetSourceAddress)
  - [M SetTargetAddress ](#ApiClient.HSFZSettings.SetTargetAddress)
  - [M SetTargetIp ](#ApiClient.HSFZSettings.SetTargetIp)

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

[ UdsSettings ](UdsSettings.md)

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

HSFZSettings

- [C HSFZSettings ](#ApiClient.HSFZSettings)
  - [M Clone ](#ApiClient.HSFZSettings.Clone)
  - [M GetDiagTimeoutHsfz ](#ApiClient.HSFZSettings.GetDiagTimeoutHsfz)
  - [M GetRemotePort ](#ApiClient.HSFZSettings.GetRemotePort)
  - [M GetSourceAddress ](#ApiClient.HSFZSettings.GetSourceAddress)
  - [M GetTargetAddress ](#ApiClient.HSFZSettings.GetTargetAddress)
  - [M GetTargetIp ](#ApiClient.HSFZSettings.GetTargetIp)
  - [M SetDiagTimeoutHsfz ](#ApiClient.HSFZSettings.SetDiagTimeoutHsfz)
  - [M SetRemotePort ](#ApiClient.HSFZSettings.SetRemotePort)
  - [M SetSourceAddress ](#ApiClient.HSFZSettings.SetSourceAddress)
  - [M SetTargetAddress ](#ApiClient.HSFZSettings.SetTargetAddress)
  - [M SetTargetIp ](#ApiClient.HSFZSettings.SetTargetIp)

# HSFZSettings[¶](#hsfzsettings "Link to this heading")

*class* HSFZSettings[¶](#ApiClient.HSFZSettings "Link to this definition")  
Clone()[¶](#ApiClient.HSFZSettings.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`HSFZSettings`](#ApiClient.HSFZSettings "ApiClient.HSFZSettings (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")

GetDiagTimeoutHsfz()[¶](#ApiClient.HSFZSettings.GetDiagTimeoutHsfz "Link to this definition")  
Returns the DiagTimeoutHsfz.

Timeout in milliseconds when waiting for responses on diagnostic requests via the HSFZ protocol - Integer

Returns:  DiagTimeoutHsfz

Return type:  int

GetRemotePort()[¶](#ApiClient.HSFZSettings.GetRemotePort "Link to this definition")  
Returns the RemotePort.

HSFZ destination port - Integer

Returns:  RemotePort

Return type:  int

GetSourceAddress()[¶](#ApiClient.HSFZSettings.GetSourceAddress "Link to this definition")  
Returns the SourceAddress.

Here: Only the byte sequence in format “AA:BB:01”.

Diagnostic address from which diagnostic requests are sent - ByteStream

Returns:  SourceAddress

Return type:  str

GetTargetAddress()[¶](#ApiClient.HSFZSettings.GetTargetAddress "Link to this definition")  
Returns the TargetAddress.

Here: Only the byte sequence in format “AA:BB:01”.

Diagnostic address to which diagnostic requests are sent - ByteStream

Returns:  TargetAddress

Return type:  str

GetTargetIp()[¶](#ApiClient.HSFZSettings.GetTargetIp "Link to this definition")  
Returns the TargetIp.

Remote IP address - String

Returns:  TargetIp

Return type:  str

SetDiagTimeoutHsfz(*[value](#ApiClient.HSFZSettings.SetDiagTimeoutHsfz.value "ApiClient.HSFZSettings.SetDiagTimeoutHsfz.value (Python parameter) — DiagTimeoutHsfz")*)[¶](#ApiClient.HSFZSettings.SetDiagTimeoutHsfz "Link to this definition")  
Sets the DiagTimeoutHsfz.

Timeout in milliseconds when waiting for responses on diagnostic requests via the HSFZ protocol - Integer

Parameters:  value : int[¶](#ApiClient.HSFZSettings.SetDiagTimeoutHsfz.value "Permalink to this definition")  
DiagTimeoutHsfz

SetRemotePort(*[value](#ApiClient.HSFZSettings.SetRemotePort.value "ApiClient.HSFZSettings.SetRemotePort.value (Python parameter) — RemotePort")*)[¶](#ApiClient.HSFZSettings.SetRemotePort "Link to this definition")  
Sets the RemotePort.

HSFZ destination port - Integer

Parameters:  value : int[¶](#ApiClient.HSFZSettings.SetRemotePort.value "Permalink to this definition")  
RemotePort

SetSourceAddress(*[value](#ApiClient.HSFZSettings.SetSourceAddress.value "ApiClient.HSFZSettings.SetSourceAddress.value (Python parameter) — SourceAddress")*)[¶](#ApiClient.HSFZSettings.SetSourceAddress "Link to this definition")  
Sets the SourceAddress.

Here: Only the byte sequence in format “AA:BB:01”.

Diagnostic address from which diagnostic requests are sent - ByteStream

Parameters:  value : str[¶](#ApiClient.HSFZSettings.SetSourceAddress.value "Permalink to this definition")  
SourceAddress

SetTargetAddress(*[value](#ApiClient.HSFZSettings.SetTargetAddress.value "ApiClient.HSFZSettings.SetTargetAddress.value (Python parameter) — TargetAddress")*)[¶](#ApiClient.HSFZSettings.SetTargetAddress "Link to this definition")  
Sets the TargetAddress.

Here: Only the byte sequence in format “AA:BB:01”.

Diagnostic address to which diagnostic requests are sent - ByteStream

Parameters:  value : str[¶](#ApiClient.HSFZSettings.SetTargetAddress.value "Permalink to this definition")  
TargetAddress

SetTargetIp(*[value](#ApiClient.HSFZSettings.SetTargetIp.value "ApiClient.HSFZSettings.SetTargetIp.value (Python parameter) — TargetIp")*)[¶](#ApiClient.HSFZSettings.SetTargetIp "Link to this definition")  
Sets the TargetIp.

Remote IP address - String

Parameters:  value : str[¶](#ApiClient.HSFZSettings.SetTargetIp.value "Permalink to this definition")  
TargetIp

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
