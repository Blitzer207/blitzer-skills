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

DoSoAdSettings [ DoSoAdSettings ](#)

DoSoAdSettings

- [C DoSoAdSettings ](#ApiClient.DoSoAdSettings)
  - [M Clone ](#ApiClient.DoSoAdSettings.Clone)
  - [M GetDiagTimeoutDoSoAd ](#ApiClient.DoSoAdSettings.GetDiagTimeoutDoSoAd)
  - [M GetRemotePort ](#ApiClient.DoSoAdSettings.GetRemotePort)
  - [M GetSourceAddress ](#ApiClient.DoSoAdSettings.GetSourceAddress)
  - [M GetTargetAddress ](#ApiClient.DoSoAdSettings.GetTargetAddress)
  - [M GetTargetIp ](#ApiClient.DoSoAdSettings.GetTargetIp)
  - [M SetDiagTimeoutDoSoAd ](#ApiClient.DoSoAdSettings.SetDiagTimeoutDoSoAd)
  - [M SetRemotePort ](#ApiClient.DoSoAdSettings.SetRemotePort)
  - [M SetSourceAddress ](#ApiClient.DoSoAdSettings.SetSourceAddress)
  - [M SetTargetAddress ](#ApiClient.DoSoAdSettings.SetTargetAddress)
  - [M SetTargetIp ](#ApiClient.DoSoAdSettings.SetTargetIp)

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

DoSoAdSettings

- [C DoSoAdSettings ](#ApiClient.DoSoAdSettings)
  - [M Clone ](#ApiClient.DoSoAdSettings.Clone)
  - [M GetDiagTimeoutDoSoAd ](#ApiClient.DoSoAdSettings.GetDiagTimeoutDoSoAd)
  - [M GetRemotePort ](#ApiClient.DoSoAdSettings.GetRemotePort)
  - [M GetSourceAddress ](#ApiClient.DoSoAdSettings.GetSourceAddress)
  - [M GetTargetAddress ](#ApiClient.DoSoAdSettings.GetTargetAddress)
  - [M GetTargetIp ](#ApiClient.DoSoAdSettings.GetTargetIp)
  - [M SetDiagTimeoutDoSoAd ](#ApiClient.DoSoAdSettings.SetDiagTimeoutDoSoAd)
  - [M SetRemotePort ](#ApiClient.DoSoAdSettings.SetRemotePort)
  - [M SetSourceAddress ](#ApiClient.DoSoAdSettings.SetSourceAddress)
  - [M SetTargetAddress ](#ApiClient.DoSoAdSettings.SetTargetAddress)
  - [M SetTargetIp ](#ApiClient.DoSoAdSettings.SetTargetIp)

# DoSoAdSettings[¶](#dosoadsettings "Link to this heading")

*class* DoSoAdSettings[¶](#ApiClient.DoSoAdSettings "Link to this definition")  
Clone()[¶](#ApiClient.DoSoAdSettings.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`DoSoAdSettings`](#ApiClient.DoSoAdSettings "ApiClient.DoSoAdSettings (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")

GetDiagTimeoutDoSoAd()[¶](#ApiClient.DoSoAdSettings.GetDiagTimeoutDoSoAd "Link to this definition")  
Returns the DiagTimeoutDoSoAd.

Timeout in milliseconds when waiting for responses on diagnostic requests via the DoSoAd protocol - Integer

Returns:  DiagTimeoutDoSoAd

Return type:  int

GetRemotePort()[¶](#ApiClient.DoSoAdSettings.GetRemotePort "Link to this definition")  
Returns the RemotePort.

TCP port of DoSoAd server

Returns:  RemotePort

Return type:  int

GetSourceAddress()[¶](#ApiClient.DoSoAdSettings.GetSourceAddress "Link to this definition")  
Returns the SourceAddress.

Here: Only the byte sequence in format “AA:BB:01”.

Address of DoSoAd client

Returns:  SourceAddress

Return type:  str

GetTargetAddress()[¶](#ApiClient.DoSoAdSettings.GetTargetAddress "Link to this definition")  
Returns the TargetAddress.

Here: Only the byte sequence in format “AA:BB:01”.

Address of DoSoAd server

Returns:  TargetAddress

Return type:  str

GetTargetIp()[¶](#ApiClient.DoSoAdSettings.GetTargetIp "Link to this definition")  
Returns the TargetIp.

IP address of DoSoAd server

Returns:  TargetIp

Return type:  str

SetDiagTimeoutDoSoAd(*[value](#ApiClient.DoSoAdSettings.SetDiagTimeoutDoSoAd.value "ApiClient.DoSoAdSettings.SetDiagTimeoutDoSoAd.value (Python parameter) — DiagTimeoutDoSoAd")*)[¶](#ApiClient.DoSoAdSettings.SetDiagTimeoutDoSoAd "Link to this definition")  
Sets the DiagTimeoutDoSoAd.

Timeout in milliseconds when waiting for responses on diagnostic requests via the DoSoAd protocol - Integer

Parameters:  value : int[¶](#ApiClient.DoSoAdSettings.SetDiagTimeoutDoSoAd.value "Permalink to this definition")  
DiagTimeoutDoSoAd

SetRemotePort(*[value](#ApiClient.DoSoAdSettings.SetRemotePort.value "ApiClient.DoSoAdSettings.SetRemotePort.value (Python parameter) — RemotePort")*)[¶](#ApiClient.DoSoAdSettings.SetRemotePort "Link to this definition")  
Sets the RemotePort.

TCP port of DoSoAd server

Parameters:  value : int[¶](#ApiClient.DoSoAdSettings.SetRemotePort.value "Permalink to this definition")  
RemotePort

SetSourceAddress(*[value](#ApiClient.DoSoAdSettings.SetSourceAddress.value "ApiClient.DoSoAdSettings.SetSourceAddress.value (Python parameter) — SourceAddress")*)[¶](#ApiClient.DoSoAdSettings.SetSourceAddress "Link to this definition")  
Sets the SourceAddress.

Here: Only the byte sequence in format “AA:BB:01”.

Address of DoSoAd client

Parameters:  value : str[¶](#ApiClient.DoSoAdSettings.SetSourceAddress.value "Permalink to this definition")  
SourceAddress

SetTargetAddress(*[value](#ApiClient.DoSoAdSettings.SetTargetAddress.value "ApiClient.DoSoAdSettings.SetTargetAddress.value (Python parameter) — TargetAddress")*)[¶](#ApiClient.DoSoAdSettings.SetTargetAddress "Link to this definition")  
Sets the TargetAddress.

Here: Only the byte sequence in format “AA:BB:01”.

Address of DoSoAd server

Parameters:  value : str[¶](#ApiClient.DoSoAdSettings.SetTargetAddress.value "Permalink to this definition")  
TargetAddress

SetTargetIp(*[value](#ApiClient.DoSoAdSettings.SetTargetIp.value "ApiClient.DoSoAdSettings.SetTargetIp.value (Python parameter) — TargetIp")*)[¶](#ApiClient.DoSoAdSettings.SetTargetIp "Link to this definition")  
Sets the TargetIp.

IP address of DoSoAd server

Parameters:  value : str[¶](#ApiClient.DoSoAdSettings.SetTargetIp.value "Permalink to this definition")  
TargetIp

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
