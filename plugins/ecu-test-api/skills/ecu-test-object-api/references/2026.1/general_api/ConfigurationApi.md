[ Internal APIs ](api.md)

[ Advanced operations of package variable types ](variabledatastructures.md)

[ Advanced properties of bus-related objects ](busdatastructures.md)

[ Bus related objects of trace analysis ](busdatastructuresTraceanalysis.md)

[ Advanced properties of diagnostics-related objects ](diagdatastructures.md)

[ Diagnostics related objects of trace analysis ](diagdatastructuresTraceanalysis.md)

[ Advanced properties of media-related objects ](mediadatastructures.md)

[ Advanced properties of DLT logging-related objects ](dltdatastructures.md)

[ COM API ](com-api.md)

[ REST API ](rest-api.md)

[ Report API ](apireport.md)

[ Object API ](objectApi.md)

Object API

[ API entry points ](objectApi.md#api-entry-points)

API entry points

[ API for Analysis Jobs ](AnalysisJobApi.md)

[ API for Artifacts ](ArtifactApi.md)

[ API for Project Components ](ComponentApi.md)

[ API for Configurations ](#)

API for Configurations

- [ Bus ](ConfigurationApi/Bus.md)
- [ BusAccess ](ConfigurationApi/BusAccess.md)
- [ CanIsoTpSettings ](ConfigurationApi/CanIsoTpSettings.md)
- [ Change ](ConfigurationApi/Change.md)
- [ Common ](ConfigurationApi/Common.md)
- [ ControlUnit ](ConfigurationApi/ControlUnit.md)
- [ ControlUnits ](ConfigurationApi/ControlUnits.md)
- [ DiagSettings ](ConfigurationApi/DiagSettings.md)
- [ DoIpSettings ](ConfigurationApi/DoIpSettings.md)
- [ DoSoAdSettings ](ConfigurationApi/DoSoAdSettings.md)
- [ EnvComAccess ](ConfigurationApi/EnvComAccess.md)
- [ EnvComData ](ConfigurationApi/EnvComData.md)
- [ EnvSimAccess ](ConfigurationApi/EnvSimAccess.md)
- [ EnvSimData ](ConfigurationApi/EnvSimData.md)
- [ Environment ](ConfigurationApi/Environment.md)
- [ Execution ](ConfigurationApi/Execution.md)
- [ FailureSimulation ](ConfigurationApi/FailureSimulation.md)
- [ FailureSimulationAccess ](ConfigurationApi/FailureSimulationAccess.md)
- [ FrTpSettings ](ConfigurationApi/FrTpSettings.md)
- [ Function ](ConfigurationApi/Function.md)
- [ FunctionAccess ](ConfigurationApi/FunctionAccess.md)
- [ HSFZSettings ](ConfigurationApi/HSFZSettings.md)
- [ Media ](ConfigurationApi/Media.md)
- [ MediaAccess ](ConfigurationApi/MediaAccess.md)
- [ Model ](ConfigurationApi/Model.md)
- [ ModelAccess ](ConfigurationApi/ModelAccess.md)
- [ Platform ](ConfigurationApi/Platform.md)
- [ Port ](ConfigurationApi/Port.md)
- [ Property ](ConfigurationApi/Property.md)
- [ PropertySet ](ConfigurationApi/PropertySet.md)
- [ ReportData ](ConfigurationApi/ReportData.md)
- [ ReportFormat ](ConfigurationApi/ReportFormat.md)
- [ TestBenchConfiguration ](ConfigurationApi/TestBenchConfiguration.md)
- [ TestConfiguration ](ConfigurationApi/TestConfiguration.md)
- [ TestConfigurationGlobalConstants ](ConfigurationApi/TestConfigurationGlobalConstants.md)
- [ Tool ](ConfigurationApi/Tool.md)
- [ ToolHost ](ConfigurationApi/ToolHost.md)
- [ UdsSettings ](ConfigurationApi/UdsSettings.md)
- [ UserReportData ](ConfigurationApi/UserReportData.md)
- [ ValueDifference ](ConfigurationApi/ValueDifference.md)

API for Configurations [ API for Configurations ](#)

API for Configurations

- [C ConfigurationApi ](#ApiClient.ConfigurationApi)
  - [A ReportFilterApi ](#ApiClient.ConfigurationApi.ReportFilterApi)
  - [M CreateTestBenchConfiguration ](#ApiClient.ConfigurationApi.CreateTestBenchConfiguration)
  - [M CreateTestConfiguration ](#ApiClient.ConfigurationApi.CreateTestConfiguration)
  - [M GetChangesForTestBenchConfigurations ](#ApiClient.ConfigurationApi.GetChangesForTestBenchConfigurations)
  - [M GetChangesForTestConfigurations ](#ApiClient.ConfigurationApi.GetChangesForTestConfigurations)
  - [M OpenTestBenchConfiguration ](#ApiClient.ConfigurationApi.OpenTestBenchConfiguration)
  - [M OpenTestConfiguration ](#ApiClient.ConfigurationApi.OpenTestConfiguration)
  - [M SearchTestBenchConfigurations ](#ApiClient.ConfigurationApi.SearchTestBenchConfigurations)
  - [M SearchTestConfigurations ](#ApiClient.ConfigurationApi.SearchTestConfigurations)
- [ Bus ](ConfigurationApi/Bus.md)
- [ BusAccess ](ConfigurationApi/BusAccess.md)
- [ CanIsoTpSettings ](ConfigurationApi/CanIsoTpSettings.md)
- [ Change ](ConfigurationApi/Change.md)
- [ Common ](ConfigurationApi/Common.md)
- [ ControlUnit ](ConfigurationApi/ControlUnit.md)
- [ ControlUnits ](ConfigurationApi/ControlUnits.md)
- [ DiagSettings ](ConfigurationApi/DiagSettings.md)
- [ DoIpSettings ](ConfigurationApi/DoIpSettings.md)
- [ DoSoAdSettings ](ConfigurationApi/DoSoAdSettings.md)
- [ EnvComAccess ](ConfigurationApi/EnvComAccess.md)
- [ EnvComData ](ConfigurationApi/EnvComData.md)
- [ EnvSimAccess ](ConfigurationApi/EnvSimAccess.md)
- [ EnvSimData ](ConfigurationApi/EnvSimData.md)
- [ Environment ](ConfigurationApi/Environment.md)
- [ Execution ](ConfigurationApi/Execution.md)
- [ FailureSimulation ](ConfigurationApi/FailureSimulation.md)
- [ FailureSimulationAccess ](ConfigurationApi/FailureSimulationAccess.md)
- [ FrTpSettings ](ConfigurationApi/FrTpSettings.md)
- [ Function ](ConfigurationApi/Function.md)
- [ FunctionAccess ](ConfigurationApi/FunctionAccess.md)
- [ HSFZSettings ](ConfigurationApi/HSFZSettings.md)
- [ Media ](ConfigurationApi/Media.md)
- [ MediaAccess ](ConfigurationApi/MediaAccess.md)
- [ Model ](ConfigurationApi/Model.md)
- [ ModelAccess ](ConfigurationApi/ModelAccess.md)
- [ Platform ](ConfigurationApi/Platform.md)
- [ Port ](ConfigurationApi/Port.md)
- [ Property ](ConfigurationApi/Property.md)
- [ PropertySet ](ConfigurationApi/PropertySet.md)
- [ ReportData ](ConfigurationApi/ReportData.md)
- [ ReportFormat ](ConfigurationApi/ReportFormat.md)
- [ TestBenchConfiguration ](ConfigurationApi/TestBenchConfiguration.md)
- [ TestConfiguration ](ConfigurationApi/TestConfiguration.md)
- [ TestConfigurationGlobalConstants ](ConfigurationApi/TestConfigurationGlobalConstants.md)
- [ Tool ](ConfigurationApi/Tool.md)
- [ ToolHost ](ConfigurationApi/ToolHost.md)
- [ UdsSettings ](ConfigurationApi/UdsSettings.md)
- [ UserReportData ](ConfigurationApi/UserReportData.md)
- [ ValueDifference ](ConfigurationApi/ValueDifference.md)

[ API for Expectations ](ExpectationApi.md)

[ API for Expressions ](ExpressionApi.md)

[ API for Global Mappings ](GlobalMappingApi.md)

[ API for Mappings ](MappingApi.md)

[ API for Multimedia Objects ](MultimediaApi.md)

[ API for Packages ](PackageApi.md)

[ API for Parameters ](ParameterApi.md)

[ API for Projects ](ProjectApi.md)

[ API for Relations ](RelationApi.md)

[ API for Reports ](ReportApi.md)

[ API for Report Filters ](ReportFilterApi.md)

[ API for Settings ](SettingsApi.md)

[ API for Signals ](SignalApi.md)

[ API for Signal Descriptions ](SignalDescriptionApi.md)

[ API for Signal Recordings ](SignalRecordingApi.md)

[ API for Symbols ](SymbolApi.md)

[ API for Test Steps ](TestStepApi.md)

[ API for Touch Inputs ](TouchInputApi.md)

[ API for Trace Analyses ](TraceAnalysisApi.md)

[ API for Trace Files ](TraceFileApi.md)

[ API for Trace Step Templates ](TraceStepTemplateApi.md)

[ API for Variables ](VariableApi.md)

[ API for Workspaces ](WorkspaceApi.md)

[ Trace Analysis API ](../TraceAnalysisAPI/index.md)

[ Generator APIs ](../generators/index.md)

[ Tools ](../tools/index.md)

[ User test management ](../userTestmanagement/index.md)

[ UserUtility API ](../user-utility/user-utility.md)

[ Utility Examples ](../user-utility/example-utilities.md)

API for Configurations

- [C ConfigurationApi ](#ApiClient.ConfigurationApi)
  - [A ReportFilterApi ](#ApiClient.ConfigurationApi.ReportFilterApi)
  - [M CreateTestBenchConfiguration ](#ApiClient.ConfigurationApi.CreateTestBenchConfiguration)
  - [M CreateTestConfiguration ](#ApiClient.ConfigurationApi.CreateTestConfiguration)
  - [M GetChangesForTestBenchConfigurations ](#ApiClient.ConfigurationApi.GetChangesForTestBenchConfigurations)
  - [M GetChangesForTestConfigurations ](#ApiClient.ConfigurationApi.GetChangesForTestConfigurations)
  - [M OpenTestBenchConfiguration ](#ApiClient.ConfigurationApi.OpenTestBenchConfiguration)
  - [M OpenTestConfiguration ](#ApiClient.ConfigurationApi.OpenTestConfiguration)
  - [M SearchTestBenchConfigurations ](#ApiClient.ConfigurationApi.SearchTestBenchConfigurations)
  - [M SearchTestConfigurations ](#ApiClient.ConfigurationApi.SearchTestConfigurations)

# API for Configurations[¶](#api-for-configurations "Link to this heading")

Part of the [Object based program API](objectApi.md#objectapi).

*class* ConfigurationApi[¶](#ApiClient.ConfigurationApi "Link to this definition")  
API to access configuration files

Returned by

- [`ApiClient.ConfigurationApi`](objectApi.md#ApiClient.ApiClient.ConfigurationApi "ApiClient.ApiClient.ConfigurationApi (Python attribute) — Returns the ConfigurationApi namespace.")

ReportFilterApi[¶](#ApiClient.ConfigurationApi.ReportFilterApi "Link to this definition")  
Returns the ReportFilterApi namespace.

Returns:  ReportFilterApi namespace

Return type:  [`ReportFilterApi`](ReportFilterApi.md#ApiClient.ReportFilterApi "ApiClient.ReportFilterApi (Python class) — API to create report filter definitions")

CreateTestBenchConfiguration()[¶](#ApiClient.ConfigurationApi.CreateTestBenchConfiguration "Link to this definition")  
Creates new test bench configuration.

Returns:  New empty test bench configuration

Return type:  [`TestBenchConfiguration`](ConfigurationApi/TestBenchConfiguration.md#ApiClient.TestBenchConfiguration "ApiClient.TestBenchConfiguration (Python class) — ConfigurationApi.CreateTestBenchConfiguration")

CreateTestConfiguration()[¶](#ApiClient.ConfigurationApi.CreateTestConfiguration "Link to this definition")  
Creates a new test configuration.

Returns:  New empty test configuration

Return type:  [`TestConfiguration`](ConfigurationApi/TestConfiguration.md#ApiClient.TestConfiguration "ApiClient.TestConfiguration (Python class) — ConfigurationApi.CreateTestConfiguration")

GetChangesForTestBenchConfigurations(*[oldTestBenchConfig](#ApiClient.ConfigurationApi.GetChangesForTestBenchConfigurations.oldTestBenchConfig "ApiClient.ConfigurationApi.GetChangesForTestBenchConfigurations.oldTestBenchConfig (Python parameter) — The old test bench configuration to compare.")*, *[newTestBenchConfig](#ApiClient.ConfigurationApi.GetChangesForTestBenchConfigurations.newTestBenchConfig "ApiClient.ConfigurationApi.GetChangesForTestBenchConfigurations.newTestBenchConfig (Python parameter) — The new test bench configuration to compare.")*)[¶](#ApiClient.ConfigurationApi.GetChangesForTestBenchConfigurations "Link to this definition")  
Get the changes that exist between two given test bench configurations.

Parameters:  oldTestBenchConfig[¶](#ApiClient.ConfigurationApi.GetChangesForTestBenchConfigurations.oldTestBenchConfig "Permalink to this definition")  
The old test bench configuration to compare.

newTestBenchConfig[¶](#ApiClient.ConfigurationApi.GetChangesForTestBenchConfigurations.newTestBenchConfig "Permalink to this definition")  
The new test bench configuration to compare.

Returns:  The changes that exist between the two test bench configurations.

Return type:  list[[`Change`](ConfigurationApi/Change.md#ApiClient.Change "ApiClient.Change (Python class) — Represents a change between an old element and a new element. Both elements have the same type, e.g. a certain test step and stem from two different Objects, e.g. an old Package a new Package.")]

GetChangesForTestConfigurations(*[oldTestConfig](#ApiClient.ConfigurationApi.GetChangesForTestConfigurations.oldTestConfig "ApiClient.ConfigurationApi.GetChangesForTestConfigurations.oldTestConfig (Python parameter) — The old test configuration to compare.")*, *[newTestConfig](#ApiClient.ConfigurationApi.GetChangesForTestConfigurations.newTestConfig "ApiClient.ConfigurationApi.GetChangesForTestConfigurations.newTestConfig (Python parameter) — The new test configuration to compare.")*)[¶](#ApiClient.ConfigurationApi.GetChangesForTestConfigurations "Link to this definition")  
Get the changes that exist between two given test configurations.

Parameters:  oldTestConfig[¶](#ApiClient.ConfigurationApi.GetChangesForTestConfigurations.oldTestConfig "Permalink to this definition")  
The old test configuration to compare.

newTestConfig[¶](#ApiClient.ConfigurationApi.GetChangesForTestConfigurations.newTestConfig "Permalink to this definition")  
The new test configuration to compare.

Returns:  The changes that exist between the two test configurations.

Return type:  list[[`Change`](ConfigurationApi/Change.md#ApiClient.Change "ApiClient.Change (Python class) — Represents a change between an old element and a new element. Both elements have the same type, e.g. a certain test step and stem from two different Objects, e.g. an old Package a new Package.")]

OpenTestBenchConfiguration(*[filename](#ApiClient.ConfigurationApi.OpenTestBenchConfiguration.filename "ApiClient.ConfigurationApi.OpenTestBenchConfiguration.filename (Python parameter) — File name of the test bench configuration file (*.tbc); Either absolute or relative to the 'Configuration' directory")*)[¶](#ApiClient.ConfigurationApi.OpenTestBenchConfiguration "Link to this definition")  
Opens an existing test bench configuration (\*.tbc).

Parameters:  filename : str[¶](#ApiClient.ConfigurationApi.OpenTestBenchConfiguration.filename "Permalink to this definition")  
File name of the test bench configuration file (\*.tbc); Either absolute or relative to the ‘Configuration’ directory

Returns:  Loaded test bench configuration

Return type:  [`TestBenchConfiguration`](ConfigurationApi/TestBenchConfiguration.md#ApiClient.TestBenchConfiguration "ApiClient.TestBenchConfiguration (Python class) — ConfigurationApi.CreateTestBenchConfiguration")

Raises:  
**ApiError** – If the test bench configuration file (\*.tbc) does not exist.

OpenTestConfiguration(*[filename](#ApiClient.ConfigurationApi.OpenTestConfiguration.filename "ApiClient.ConfigurationApi.OpenTestConfiguration.filename (Python parameter) — File name of the test configuration file (*.tcf); Either absolute or relative to the 'Configuration' directory")*)[¶](#ApiClient.ConfigurationApi.OpenTestConfiguration "Link to this definition")  
Opens an existing test configuration.

Parameters:  filename : str[¶](#ApiClient.ConfigurationApi.OpenTestConfiguration.filename "Permalink to this definition")  
File name of the test configuration file (\*.tcf); Either absolute or relative to the ‘Configuration’ directory

Returns:  Loaded test configuration

Return type:  [`TestConfiguration`](ConfigurationApi/TestConfiguration.md#ApiClient.TestConfiguration "ApiClient.TestConfiguration (Python class) — ConfigurationApi.CreateTestConfiguration")

Raises:  
**ApiError** – If the test configuration file (\*.tcf) does not exist.

SearchTestBenchConfigurations(*[searchCriteria](#ApiClient.ConfigurationApi.SearchTestBenchConfigurations.searchCriteria "ApiClient.ConfigurationApi.SearchTestBenchConfigurations.searchCriteria (Python parameter) — The search criteria expressed in the ecu.test filter syntax.")*, *[useExtendedMode](#ApiClient.ConfigurationApi.SearchTestBenchConfigurations.useExtendedMode "ApiClient.ConfigurationApi.SearchTestBenchConfigurations.useExtendedMode (Python parameter) — If True, extended search strings are enabled.")=`False`*)[¶](#ApiClient.ConfigurationApi.SearchTestBenchConfigurations "Link to this definition")  
Searches the current workspace and library workspaces for Testbenchconfigurations matching the given search criteria.

Parameters:  searchCriteria : str[¶](#ApiClient.ConfigurationApi.SearchTestBenchConfigurations.searchCriteria "Permalink to this definition")  
The search criteria expressed in the ecu.test filter syntax. See section “Handling” =\> “Filter” of the ecu.test User Documentation.

useExtendedMode : boolean[¶](#ApiClient.ConfigurationApi.SearchTestBenchConfigurations.useExtendedMode "Permalink to this definition")  
If True, extended search strings are enabled. The default is False, meaning each word in the searchCriteria will be enclosed by wildcards and mapped to the filename. (e.g. “hello world” =\> “Name = ‘\*hello\*’ and Name = ‘\*world\*’”)

Returns:  All matching Testbenchconfigurations. If no file matches, an emtpy list is returned.

Return type:  list[[`TestBenchConfiguration`](ConfigurationApi/TestBenchConfiguration.md#ApiClient.TestBenchConfiguration "ApiClient.TestBenchConfiguration (Python class) — ConfigurationApi.CreateTestBenchConfiguration")]

Raises:  
**ApiError** – If the searchCriteria has an illegal syntax.

SearchTestConfigurations(*[searchCriteria](#ApiClient.ConfigurationApi.SearchTestConfigurations.searchCriteria "ApiClient.ConfigurationApi.SearchTestConfigurations.searchCriteria (Python parameter) — The search criteria expressed in the ecu.test filter syntax.")*, *[useExtendedMode](#ApiClient.ConfigurationApi.SearchTestConfigurations.useExtendedMode "ApiClient.ConfigurationApi.SearchTestConfigurations.useExtendedMode (Python parameter) — If True, extended search strings are enabled.")=`False`*)[¶](#ApiClient.ConfigurationApi.SearchTestConfigurations "Link to this definition")  
Searches the current workspace and library workspaces for Testconfigurations matching the given search criteria.

Parameters:  searchCriteria : str[¶](#ApiClient.ConfigurationApi.SearchTestConfigurations.searchCriteria "Permalink to this definition")  
The search criteria expressed in the ecu.test filter syntax. See section “Handling” =\> “Filter” of the ecu.test User Documentation.

useExtendedMode : boolean[¶](#ApiClient.ConfigurationApi.SearchTestConfigurations.useExtendedMode "Permalink to this definition")  
If True, extended search strings are enabled. The default is False, meaning each word in the searchCriteria will be enclosed by wildcards and mapped to the filename. (e.g. “hello world” =\> “Name = ‘\*hello\*’ and Name = ‘\*world\*’”)

Returns:  All matching Testconfigurations. If no file matches, an emtpy list is returned.

Return type:  list[[`TestConfiguration`](ConfigurationApi/TestConfiguration.md#ApiClient.TestConfiguration "ApiClient.TestConfiguration (Python class) — ConfigurationApi.CreateTestConfiguration")]

Raises:  
**ApiError** – If the searchCriteria has an illegal syntax.

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
