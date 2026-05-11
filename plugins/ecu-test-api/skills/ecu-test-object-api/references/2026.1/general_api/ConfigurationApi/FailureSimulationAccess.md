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

FailureSimulationAccess [ FailureSimulationAccess ](#)

FailureSimulationAccess

- [C FailureSimulationAccess ](#ApiClient.FailureSimulationAccess)
  - [M Add ](#ApiClient.FailureSimulationAccess.Add)
  - [M Clone ](#ApiClient.FailureSimulationAccess.Clone)
  - [M Delete ](#ApiClient.FailureSimulationAccess.Delete)
  - [M Get ](#ApiClient.FailureSimulationAccess.Get)
  - [M GetAll ](#ApiClient.FailureSimulationAccess.GetAll)

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

FailureSimulationAccess

- [C FailureSimulationAccess ](#ApiClient.FailureSimulationAccess)
  - [M Add ](#ApiClient.FailureSimulationAccess.Add)
  - [M Clone ](#ApiClient.FailureSimulationAccess.Clone)
  - [M Delete ](#ApiClient.FailureSimulationAccess.Delete)
  - [M Get ](#ApiClient.FailureSimulationAccess.Get)
  - [M GetAll ](#ApiClient.FailureSimulationAccess.GetAll)

# FailureSimulationAccess[¶](#failuresimulationaccess "Link to this heading")

*class* FailureSimulationAccess[¶](#ApiClient.FailureSimulationAccess "Link to this definition")  
Add(*[failureSimulationKey](#ApiClient.FailureSimulationAccess.Add.failureSimulationKey "ApiClient.FailureSimulationAccess.Add.failureSimulationKey (Python parameter) — Name of the failure simulation to add")*, *[failureSimulationFile](#ApiClient.FailureSimulationAccess.Add.failureSimulationFile "ApiClient.FailureSimulationAccess.Add.failureSimulationFile (Python parameter) — Name of the failure simulation file")=`''`*, *[failureSimulationPort](#ApiClient.FailureSimulationAccess.Add.failureSimulationPort "ApiClient.FailureSimulationAccess.Add.failureSimulationPort (Python parameter) — Name of the failure simulation port")=`''`*)[¶](#ApiClient.FailureSimulationAccess.Add "Link to this definition")  
Adds a failure simulation

Parameters:  failureSimulationKey : str[¶](#ApiClient.FailureSimulationAccess.Add.failureSimulationKey "Permalink to this definition")  
Name of the failure simulation to add

failureSimulationFile : str[¶](#ApiClient.FailureSimulationAccess.Add.failureSimulationFile "Permalink to this definition")  
Name of the failure simulation file

failureSimulationPort : str[¶](#ApiClient.FailureSimulationAccess.Add.failureSimulationPort "Permalink to this definition")  
Name of the failure simulation port

Returns:  The failure simulation which was added

Return type:  [`FailureSimulation`](FailureSimulation.md#ApiClient.FailureSimulation "ApiClient.FailureSimulation (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")

Clone()[¶](#ApiClient.FailureSimulationAccess.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`FailureSimulationAccess`](#ApiClient.FailureSimulationAccess "ApiClient.FailureSimulationAccess (Python class) — Adds a failure simulation")

Delete(*[failureSimulationKey](#ApiClient.FailureSimulationAccess.Delete.failureSimulationKey "ApiClient.FailureSimulationAccess.Delete.failureSimulationKey (Python parameter) — Name of failure simulation to delete")*)[¶](#ApiClient.FailureSimulationAccess.Delete "Link to this definition")  
Deletes a failure simulation.

Parameters:  failureSimulationKey : str[¶](#ApiClient.FailureSimulationAccess.Delete.failureSimulationKey "Permalink to this definition")  
Name of failure simulation to delete

Get(*[failureSimulationKey](#ApiClient.FailureSimulationAccess.Get.failureSimulationKey "ApiClient.FailureSimulationAccess.Get.failureSimulationKey (Python parameter) — Name of the failure simulation")*)[¶](#ApiClient.FailureSimulationAccess.Get "Link to this definition")  
Returns the failure simulation object specified by the given key.

Parameters:  failureSimulationKey : str[¶](#ApiClient.FailureSimulationAccess.Get.failureSimulationKey "Permalink to this definition")  
Name of the failure simulation

Returns:  The failure simulation object

Return type:  [`FailureSimulation`](FailureSimulation.md#ApiClient.FailureSimulation "ApiClient.FailureSimulation (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")

GetAll()[¶](#ApiClient.FailureSimulationAccess.GetAll "Link to this definition")  
Returns a list of the names of all the failure simulations.

Returns:  List of names of all failure simulations

Return type:  list[str]

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
