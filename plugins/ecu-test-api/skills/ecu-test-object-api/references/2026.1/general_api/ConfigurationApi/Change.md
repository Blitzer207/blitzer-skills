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

Change [ Change ](#)

Change

- [C Change ](#ApiClient.Change)
  - [M Clone ](#ApiClient.Change.Clone)
  - [M GetComparedProperties ](#ApiClient.Change.GetComparedProperties)
  - [M GetNewPath ](#ApiClient.Change.GetNewPath)
  - [M GetOldPath ](#ApiClient.Change.GetOldPath)
  - [M GetType ](#ApiClient.Change.GetType)
  - [M GetValueDifferences ](#ApiClient.Change.GetValueDifferences)

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

Change

- [C Change ](#ApiClient.Change)
  - [M Clone ](#ApiClient.Change.Clone)
  - [M GetComparedProperties ](#ApiClient.Change.GetComparedProperties)
  - [M GetNewPath ](#ApiClient.Change.GetNewPath)
  - [M GetOldPath ](#ApiClient.Change.GetOldPath)
  - [M GetType ](#ApiClient.Change.GetType)
  - [M GetValueDifferences ](#ApiClient.Change.GetValueDifferences)

# Change[¶](#change "Link to this heading")

*class* Change[¶](#ApiClient.Change "Link to this definition")  
Represents a change between an old element and a new element. Both elements have the same type, e.g. a certain test step and stem from two different Objects, e.g. an old Package a new Package.

Returned by

- [`ConfigurationApi.GetChangesForTestBenchConfigurations`](../ConfigurationApi.md#ApiClient.ConfigurationApi.GetChangesForTestBenchConfigurations "ApiClient.ConfigurationApi.GetChangesForTestBenchConfigurations (Python method) — Get the changes that exist between two given test bench configurations.")

- [`ConfigurationApi.GetChangesForTestConfigurations`](../ConfigurationApi.md#ApiClient.ConfigurationApi.GetChangesForTestConfigurations "ApiClient.ConfigurationApi.GetChangesForTestConfigurations (Python method) — Get the changes that exist between two given test configurations.")

- [`GlobalMappingApi.GetChanges`](../GlobalMappingApi.md#ApiClient.GlobalMappingApi.GetChanges "ApiClient.GlobalMappingApi.GetChanges (Python method) — Get the changes that exist between two given global mappings.")

- [`PackageApi.GetAnalysisPackageChanges`](../PackageApi.md#ApiClient.PackageApi.GetAnalysisPackageChanges "ApiClient.PackageApi.GetAnalysisPackageChanges (Python method) — Get the changes that exist between two given analysis packages.")

- [`PackageApi.GetChanges`](../PackageApi.md#ApiClient.PackageApi.GetChanges "ApiClient.PackageApi.GetChanges (Python method) — Get the changes that exist between two given packages.")

- [`ParameterApi.GetChangesForGlobalConstantsDefinitions`](../ParameterApi.md#ApiClient.ParameterApi.GetChangesForGlobalConstantsDefinitions "ApiClient.ParameterApi.GetChangesForGlobalConstantsDefinitions (Python method) — Get the changes that exist between two given constants definitions.")

- [`ParameterApi.GetChangesForPackageParametersDefinitions`](../ParameterApi.md#ApiClient.ParameterApi.GetChangesForPackageParametersDefinitions "ApiClient.ParameterApi.GetChangesForPackageParametersDefinitions (Python method) — Get the differences that exist between two given package parameters definitions.")

- [`ProjectApi.GetChanges`](../ProjectApi.md#ApiClient.ProjectApi.GetChanges "ApiClient.ProjectApi.GetChanges (Python method) — Get the changes that exist between two given projects.")

- [`TestStepApi.GetChanges`](../TestStepApi.md#ApiClient.TestStepApi.GetChanges "ApiClient.TestStepApi.GetChanges (Python method) — Get the changes that exist between two given test steps. :param oldTestStep: The original test step :type oldTestStep: TestStep :param newTestStep: The modified test step :type newTestStep: TestStep")

Clone()[¶](#ApiClient.Change.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`Change`](#ApiClient.Change "ApiClient.Change (Python class) — Represents a change between an old element and a new element. Both elements have the same type, e.g. a certain test step and stem from two different Objects, e.g. an old Package a new Package.")

GetComparedProperties()[¶](#ApiClient.Change.GetComparedProperties "Link to this definition")  
Return the properties based on which the old element and the new element were compared.

Returns:  A list of names of compared properties.

Return type:  list[str]

GetNewPath()[¶](#ApiClient.Change.GetNewPath "Link to this definition")  
Returns the path to the new element, e.g. ‘0:Package/2:Testcase/0:Block 1/5:Comment 3’.

Returns:  The path to the new element.

Return type:  str

GetOldPath()[¶](#ApiClient.Change.GetOldPath "Link to this definition")  
Returns the path to the old element, e.g. ‘0:Package/2:Testcase/0:Block 1/5:Comment 3’.

Returns:  The path to the old element.

Return type:  str

GetType()[¶](#ApiClient.Change.GetType "Link to this definition")  
Returns the type of action that is associated with this change. The action type can be one of the following:

- INSERT - The new element was inserted.

- DELETE - The old element was deleted.

- MOVE - The new element was moved with respect to the old one.

- UPDATE - The new element differs in certain values with respect to the old one.

- POTENTIALUPDATE - The elements can’t be compared completely. There may exist a change.

Returns:  The type of action that is associated with this change.

Return type:  str

GetValueDifferences()[¶](#ApiClient.Change.GetValueDifferences "Link to this definition")  
Returns a list with differences that exist between values of the old and the new element.

Returns:  A list of changed values.

Return type:  list[[`ValueDifference`](ValueDifference.md#ApiClient.ValueDifference "ApiClient.ValueDifference (Python class) — Represents a difference in a certain value between two elements after a change occured.")]

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
