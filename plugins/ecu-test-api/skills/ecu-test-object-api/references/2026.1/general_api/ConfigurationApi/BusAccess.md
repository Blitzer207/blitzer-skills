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

BusAccess [ BusAccess ](#)

BusAccess

- [C BusAccess ](#ApiClient.BusAccess)
  - [M Add ](#ApiClient.BusAccess.Add)
  - [M Clone ](#ApiClient.BusAccess.Clone)
  - [M Delete ](#ApiClient.BusAccess.Delete)
  - [M Get ](#ApiClient.BusAccess.Get)
  - [M GetAll ](#ApiClient.BusAccess.GetAll)

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

BusAccess

- [C BusAccess ](#ApiClient.BusAccess)
  - [M Add ](#ApiClient.BusAccess.Add)
  - [M Clone ](#ApiClient.BusAccess.Clone)
  - [M Delete ](#ApiClient.BusAccess.Delete)
  - [M Get ](#ApiClient.BusAccess.Get)
  - [M GetAll ](#ApiClient.BusAccess.GetAll)

# BusAccess[¶](#busaccess "Link to this heading")

*class* BusAccess[¶](#ApiClient.BusAccess "Link to this definition")  
Add(*[busKey](#ApiClient.BusAccess.Add.busKey "ApiClient.BusAccess.Add.busKey (Python parameter) — Name of the bus")*)[¶](#ApiClient.BusAccess.Add "Link to this definition")  
Adds a bus to the bus access.

Parameters:  busKey : str[¶](#ApiClient.BusAccess.Add.busKey "Permalink to this definition")  
Name of the bus

Returns:  The bus which was added

Return type:  [`Bus`](Bus.md#ApiClient.Bus "ApiClient.Bus (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")

Clone()[¶](#ApiClient.BusAccess.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`BusAccess`](#ApiClient.BusAccess "ApiClient.BusAccess (Python class) — Adds a bus to the bus access.")

Delete(*[busKey](#ApiClient.BusAccess.Delete.busKey "ApiClient.BusAccess.Delete.busKey (Python parameter) — Name of bus to delete")*)[¶](#ApiClient.BusAccess.Delete "Link to this definition")  
Deletes a bus from bus access.

Parameters:  busKey : str[¶](#ApiClient.BusAccess.Delete.busKey "Permalink to this definition")  
Name of bus to delete

Get(*[busKey](#ApiClient.BusAccess.Get.busKey "ApiClient.BusAccess.Get.busKey (Python parameter) — Name of the bus")*)[¶](#ApiClient.BusAccess.Get "Link to this definition")  
Returns a bus object.

Parameters:  busKey : str[¶](#ApiClient.BusAccess.Get.busKey "Permalink to this definition")  
Name of the bus

Returns:  The bus object

Return type:  [`Bus`](Bus.md#ApiClient.Bus "ApiClient.Bus (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")

GetAll()[¶](#ApiClient.BusAccess.GetAll "Link to this definition")  
Returns a list of the names of all the accessed buses.

Returns:  List of names of all accessed buses

Return type:  list[str]

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
