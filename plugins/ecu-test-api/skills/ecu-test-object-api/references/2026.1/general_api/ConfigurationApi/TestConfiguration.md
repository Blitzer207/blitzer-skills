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

TestConfiguration [ TestConfiguration ](#)

TestConfiguration

- [C TestConfiguration ](#ApiClient.TestConfiguration)
  - [A BusAccess ](#ApiClient.TestConfiguration.BusAccess)
  - [A Common ](#ApiClient.TestConfiguration.Common)
  - [A ControlUnits ](#ApiClient.TestConfiguration.ControlUnits)
  - [A EnvironmentAccess ](#ApiClient.TestConfiguration.EnvironmentAccess)
  - [A Execution ](#ApiClient.TestConfiguration.Execution)
  - [A GlobalConstants ](#ApiClient.TestConfiguration.GlobalConstants)
  - [A MediaAccess ](#ApiClient.TestConfiguration.MediaAccess)
  - [A Platform ](#ApiClient.TestConfiguration.Platform)
  - [A Report ](#ApiClient.TestConfiguration.Report)
  - [M Clone ](#ApiClient.TestConfiguration.Clone)
  - [M GetFilename ](#ApiClient.TestConfiguration.GetFilename)
  - [M Save ](#ApiClient.TestConfiguration.Save)

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

TestConfiguration

- [C TestConfiguration ](#ApiClient.TestConfiguration)
  - [A BusAccess ](#ApiClient.TestConfiguration.BusAccess)
  - [A Common ](#ApiClient.TestConfiguration.Common)
  - [A ControlUnits ](#ApiClient.TestConfiguration.ControlUnits)
  - [A EnvironmentAccess ](#ApiClient.TestConfiguration.EnvironmentAccess)
  - [A Execution ](#ApiClient.TestConfiguration.Execution)
  - [A GlobalConstants ](#ApiClient.TestConfiguration.GlobalConstants)
  - [A MediaAccess ](#ApiClient.TestConfiguration.MediaAccess)
  - [A Platform ](#ApiClient.TestConfiguration.Platform)
  - [A Report ](#ApiClient.TestConfiguration.Report)
  - [M Clone ](#ApiClient.TestConfiguration.Clone)
  - [M GetFilename ](#ApiClient.TestConfiguration.GetFilename)
  - [M Save ](#ApiClient.TestConfiguration.Save)

# TestConfiguration[¶](#testconfiguration "Link to this heading")

*class* TestConfiguration[¶](#ApiClient.TestConfiguration "Link to this definition")  
Returned by

- [`ConfigurationApi.CreateTestConfiguration`](../ConfigurationApi.md#ApiClient.ConfigurationApi.CreateTestConfiguration "ApiClient.ConfigurationApi.CreateTestConfiguration (Python method) — Creates a new test configuration.")

- [`ConfigurationApi.OpenTestConfiguration`](../ConfigurationApi.md#ApiClient.ConfigurationApi.OpenTestConfiguration "ApiClient.ConfigurationApi.OpenTestConfiguration (Python method) — Opens an existing test configuration.")

- [`ConfigurationApi.SearchTestConfigurations`](../ConfigurationApi.md#ApiClient.ConfigurationApi.SearchTestConfigurations "ApiClient.ConfigurationApi.SearchTestConfigurations (Python method) — Searches the current workspace and library workspaces for Testconfigurations matching the given search criteria.")

BusAccess[¶](#ApiClient.TestConfiguration.BusAccess "Link to this definition")  
Bus access configuration

Returns:  Bus access configuration

Return type:  [`BusAccess`](BusAccess.md#ApiClient.BusAccess "ApiClient.BusAccess (Python class) — Adds a bus to the bus access.")

Common[¶](#ApiClient.TestConfiguration.Common "Link to this definition")  
Common configuration

Returns:  Common configuration

Return type:  [`Common`](Common.md#ApiClient.Common "ApiClient.Common (Python class) — Adds an artifact reference to a mapping file to the list.")

ControlUnits[¶](#ApiClient.TestConfiguration.ControlUnits "Link to this definition")  
Control units configuration

Returns:  Control units configuration

Return type:  [`ControlUnits`](ControlUnits.md#ApiClient.ControlUnits "ApiClient.ControlUnits (Python class) — Adds a control unit.")

EnvironmentAccess[¶](#ApiClient.TestConfiguration.EnvironmentAccess "Link to this definition")  
Environment access configuration

Returns:  Environment access configuration

Return type:  [`Environment`](Environment.md#ApiClient.Environment "ApiClient.Environment (Python class) — Environment communication access")

Execution[¶](#ApiClient.TestConfiguration.Execution "Link to this definition")  
Execution configuration

Returns:  Execution configuration

Return type:  [`Execution`](Execution.md#ApiClient.Execution "ApiClient.Execution (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")

GlobalConstants[¶](#ApiClient.TestConfiguration.GlobalConstants "Link to this definition")  
Global constants configuration

Returns:  Global constants configuration

Return type:  [`TestConfigurationGlobalConstants`](TestConfigurationGlobalConstants.md#ApiClient.TestConfigurationGlobalConstants "ApiClient.TestConfigurationGlobalConstants (Python class) — Contains the global constants definition and references to global constants definition files.")

MediaAccess[¶](#ApiClient.TestConfiguration.MediaAccess "Link to this definition")  
Media access configuration

Returns:  Media access configuration

Return type:  [`MediaAccess`](MediaAccess.md#ApiClient.MediaAccess "ApiClient.MediaAccess (Python class) — Adds a media object.")

Platform[¶](#ApiClient.TestConfiguration.Platform "Link to this definition")  
Platform configuration

Returns:  Platform configuration

Return type:  [`Platform`](Platform.md#ApiClient.Platform "ApiClient.Platform (Python class) — Failure Simulation access")

Report[¶](#ApiClient.TestConfiguration.Report "Link to this definition")  
Report configuration

Returns:  Report configuration

Return type:  [`ReportData`](ReportData.md#ApiClient.ReportData "ApiClient.ReportData (Python class) — Adds a report format to your configuration.")

Clone()[¶](#ApiClient.TestConfiguration.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`TestConfiguration`](#ApiClient.TestConfiguration "ApiClient.TestConfiguration (Python class) — ConfigurationApi.CreateTestConfiguration")

GetFilename()[¶](#ApiClient.TestConfiguration.GetFilename "Link to this definition")  
Returns the absolute path to the test configuration file. If empty, the file has not been saved yet.

Returns:  filename with extension

Return type:  str

Save(*[filename](#ApiClient.TestConfiguration.Save.filename "ApiClient.TestConfiguration.Save.filename (Python parameter) — The file name used for storing the test configuration file; Either absolute or relative to the 'Configuration' directory. Leave out to save the configuration to its existing file (previously set with Save() or from ConfigurationApi.OpenTestConfiguration())")=`None`*)[¶](#ApiClient.TestConfiguration.Save "Link to this definition")  
Saves the test configuration to a file. Appends file ending if needed.

Parameters:  filename : str[¶](#ApiClient.TestConfiguration.Save.filename "Permalink to this definition")  
The file name used for storing the test configuration file; Either absolute or relative to the ‘Configuration’ directory. Leave out to save the configuration to its existing file (previously set with [`Save()`](#ApiClient.TestConfiguration.Save "ApiClient.TestConfiguration.Save (Python method) — Saves the test configuration to a file. Appends file ending if needed.") or from [`ConfigurationApi.OpenTestConfiguration()`](../ConfigurationApi.md#ApiClient.ConfigurationApi.OpenTestConfiguration "ApiClient.ConfigurationApi.OpenTestConfiguration (Python method) — Opens an existing test configuration."))

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
