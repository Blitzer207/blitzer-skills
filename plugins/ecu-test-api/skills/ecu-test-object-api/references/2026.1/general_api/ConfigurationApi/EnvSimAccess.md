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

EnvSimAccess [ EnvSimAccess ](#)

EnvSimAccess

- [C EnvSimAccess ](#ApiClient.EnvSimAccess)
  - [M Add ](#ApiClient.EnvSimAccess.Add)
  - [M Clone ](#ApiClient.EnvSimAccess.Clone)
  - [M Delete ](#ApiClient.EnvSimAccess.Delete)
  - [M Get ](#ApiClient.EnvSimAccess.Get)
  - [M GetAll ](#ApiClient.EnvSimAccess.GetAll)

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

EnvSimAccess

- [C EnvSimAccess ](#ApiClient.EnvSimAccess)
  - [M Add ](#ApiClient.EnvSimAccess.Add)
  - [M Clone ](#ApiClient.EnvSimAccess.Clone)
  - [M Delete ](#ApiClient.EnvSimAccess.Delete)
  - [M Get ](#ApiClient.EnvSimAccess.Get)
  - [M GetAll ](#ApiClient.EnvSimAccess.GetAll)

# EnvSimAccess[¶](#envsimaccess "Link to this heading")

*class* EnvSimAccess[¶](#ApiClient.EnvSimAccess "Link to this definition")  
Add(*[environmentSimulationKey](#ApiClient.EnvSimAccess.Add.environmentSimulationKey "ApiClient.EnvSimAccess.Add.environmentSimulationKey (Python parameter) — Name of the environment simulation to add")*)[¶](#ApiClient.EnvSimAccess.Add "Link to this definition")  
Adds a environment simulation

Parameters:  environmentSimulationKey : str[¶](#ApiClient.EnvSimAccess.Add.environmentSimulationKey "Permalink to this definition")  
Name of the environment simulation to add

Returns:  The environment simulation which was added

Return type:  [`EnvSimData`](EnvSimData.md#ApiClient.EnvSimData "ApiClient.EnvSimData (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")

Clone()[¶](#ApiClient.EnvSimAccess.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`EnvSimAccess`](#ApiClient.EnvSimAccess "ApiClient.EnvSimAccess (Python class) — Adds a environment simulation")

Delete(*[enviromentalSimulationKey](#ApiClient.EnvSimAccess.Delete.enviromentalSimulationKey "ApiClient.EnvSimAccess.Delete.enviromentalSimulationKey (Python parameter) — Name of envriomental simulation to delete")*)[¶](#ApiClient.EnvSimAccess.Delete "Link to this definition")  
Deletes a enviromental simulation from enviromental simulation access.

Parameters:  enviromentalSimulationKey : str[¶](#ApiClient.EnvSimAccess.Delete.enviromentalSimulationKey "Permalink to this definition")  
Name of envriomental simulation to delete

Get(*[environmentSimulationKey](#ApiClient.EnvSimAccess.Get.environmentSimulationKey "ApiClient.EnvSimAccess.Get.environmentSimulationKey (Python parameter) — Name of the environment simulation")*)[¶](#ApiClient.EnvSimAccess.Get "Link to this definition")  
Retrieves a environment simulation object.

Parameters:  environmentSimulationKey : str[¶](#ApiClient.EnvSimAccess.Get.environmentSimulationKey "Permalink to this definition")  
Name of the environment simulation

Returns:  The environment simulations object

Return type:  [`EnvSimData`](EnvSimData.md#ApiClient.EnvSimData "ApiClient.EnvSimData (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")

GetAll()[¶](#ApiClient.EnvSimAccess.GetAll "Link to this definition")  
Returns a list of the names of all the accessed environment simulations.

Returns:  list of names of all accessed environment simulations

Return type:  list[str]

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
