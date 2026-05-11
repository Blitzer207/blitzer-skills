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

ControlUnits [ ControlUnits ](#)

ControlUnits

- [C ControlUnits ](#ApiClient.ControlUnits)
  - [M Add ](#ApiClient.ControlUnits.Add)
  - [M Clone ](#ApiClient.ControlUnits.Clone)
  - [M Delete ](#ApiClient.ControlUnits.Delete)
  - [M Get ](#ApiClient.ControlUnits.Get)
  - [M GetAll ](#ApiClient.ControlUnits.GetAll)

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

ControlUnits

- [C ControlUnits ](#ApiClient.ControlUnits)
  - [M Add ](#ApiClient.ControlUnits.Add)
  - [M Clone ](#ApiClient.ControlUnits.Clone)
  - [M Delete ](#ApiClient.ControlUnits.Delete)
  - [M Get ](#ApiClient.ControlUnits.Get)
  - [M GetAll ](#ApiClient.ControlUnits.GetAll)

# ControlUnits[¶](#controlunits "Link to this heading")

*class* ControlUnits[¶](#ApiClient.ControlUnits "Link to this definition")  
Add(*[controlUnitKey](#ApiClient.ControlUnits.Add.controlUnitKey "ApiClient.ControlUnits.Add.controlUnitKey (Python parameter) — Name of the control unit")*)[¶](#ApiClient.ControlUnits.Add "Link to this definition")  
Adds a control unit.

Parameters:  controlUnitKey : str[¶](#ApiClient.ControlUnits.Add.controlUnitKey "Permalink to this definition")  
Name of the control unit

Returns:  The control unit which was added

Return type:  [`ControlUnit`](ControlUnit.md#ApiClient.ControlUnit "ApiClient.ControlUnit (Python class) — Access to the diagnostics settings")

Clone()[¶](#ApiClient.ControlUnits.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`ControlUnits`](#ApiClient.ControlUnits "ApiClient.ControlUnits (Python class) — Adds a control unit.")

Delete(*[controlUnitKey](#ApiClient.ControlUnits.Delete.controlUnitKey "ApiClient.ControlUnits.Delete.controlUnitKey (Python parameter) — Name of control unit to delete")*)[¶](#ApiClient.ControlUnits.Delete "Link to this definition")  
Deletes a control unit.

Parameters:  controlUnitKey : str[¶](#ApiClient.ControlUnits.Delete.controlUnitKey "Permalink to this definition")  
Name of control unit to delete

Get(*[controlUnitKey](#ApiClient.ControlUnits.Get.controlUnitKey "ApiClient.ControlUnits.Get.controlUnitKey (Python parameter) — Name of the control unit")*)[¶](#ApiClient.ControlUnits.Get "Link to this definition")  
Returns a control unit object.

Parameters:  controlUnitKey : str[¶](#ApiClient.ControlUnits.Get.controlUnitKey "Permalink to this definition")  
Name of the control unit

Returns:  The control unit object

Return type:  [`ControlUnit`](ControlUnit.md#ApiClient.ControlUnit "ApiClient.ControlUnit (Python class) — Access to the diagnostics settings")

GetAll()[¶](#ApiClient.ControlUnits.GetAll "Link to this definition")  
Returns a list of the names of all the accessed control units.

Returns:  List of names of all accessed control units

Return type:  list[str]

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
