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

EnvComAccess [ EnvComAccess ](#)

EnvComAccess

- [C EnvComAccess ](#ApiClient.EnvComAccess)
  - [M Add ](#ApiClient.EnvComAccess.Add)
  - [M Clone ](#ApiClient.EnvComAccess.Clone)
  - [M Delete ](#ApiClient.EnvComAccess.Delete)
  - [M Get ](#ApiClient.EnvComAccess.Get)
  - [M GetAll ](#ApiClient.EnvComAccess.GetAll)

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

EnvComAccess

- [C EnvComAccess ](#ApiClient.EnvComAccess)
  - [M Add ](#ApiClient.EnvComAccess.Add)
  - [M Clone ](#ApiClient.EnvComAccess.Clone)
  - [M Delete ](#ApiClient.EnvComAccess.Delete)
  - [M Get ](#ApiClient.EnvComAccess.Get)
  - [M GetAll ](#ApiClient.EnvComAccess.GetAll)

# EnvComAccess[¶](#envcomaccess "Link to this heading")

*class* EnvComAccess[¶](#ApiClient.EnvComAccess "Link to this definition")  
Add(*[environmentCommunicationKey](#ApiClient.EnvComAccess.Add.environmentCommunicationKey "ApiClient.EnvComAccess.Add.environmentCommunicationKey (Python parameter) — Name of the environment communication system to add")*)[¶](#ApiClient.EnvComAccess.Add "Link to this definition")  
Adds an environment communication system

Parameters:  environmentCommunicationKey : str[¶](#ApiClient.EnvComAccess.Add.environmentCommunicationKey "Permalink to this definition")  
Name of the environment communication system to add

Returns:  The environment communication system which was added

Return type:  [`EnvComData`](EnvComData.md#ApiClient.EnvComData "ApiClient.EnvComData (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")

Clone()[¶](#ApiClient.EnvComAccess.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`EnvComAccess`](#ApiClient.EnvComAccess "ApiClient.EnvComAccess (Python class) — Adds an environment communication system")

Delete(*[environmentCommunicationKey](#ApiClient.EnvComAccess.Delete.environmentCommunicationKey "ApiClient.EnvComAccess.Delete.environmentCommunicationKey (Python parameter) — Name of environment simulation to delete")*)[¶](#ApiClient.EnvComAccess.Delete "Link to this definition")  
Deletes an enviroment communication system from enviroment communication access.

Parameters:  environmentCommunicationKey : str[¶](#ApiClient.EnvComAccess.Delete.environmentCommunicationKey "Permalink to this definition")  
Name of environment simulation to delete

Get(*[environmentCommunicationKey](#ApiClient.EnvComAccess.Get.environmentCommunicationKey "ApiClient.EnvComAccess.Get.environmentCommunicationKey (Python parameter) — Name of the environment communication")*)[¶](#ApiClient.EnvComAccess.Get "Link to this definition")  
Retrieves an environment communication object.

Parameters:  environmentCommunicationKey : str[¶](#ApiClient.EnvComAccess.Get.environmentCommunicationKey "Permalink to this definition")  
Name of the environment communication

Returns:  The environment communication object

Return type:  [`EnvComData`](EnvComData.md#ApiClient.EnvComData "ApiClient.EnvComData (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")

GetAll()[¶](#ApiClient.EnvComAccess.GetAll "Link to this definition")  
Returns a list of the names of all the accessed environment communication systems.

Returns:  list of names of all accessed environment communication systems

Return type:  list[str]

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
