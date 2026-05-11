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

TestBenchConfiguration [ TestBenchConfiguration ](#)

TestBenchConfiguration

- [C TestBenchConfiguration ](#ApiClient.TestBenchConfiguration)
  - [M CreateToolHost ](#ApiClient.TestBenchConfiguration.CreateToolHost)
  - [M GetFilename ](#ApiClient.TestBenchConfiguration.GetFilename)
  - [M GetPort ](#ApiClient.TestBenchConfiguration.GetPort)
  - [M GetTool ](#ApiClient.TestBenchConfiguration.GetTool)
  - [M GetToolHost ](#ApiClient.TestBenchConfiguration.GetToolHost)
  - [M GetToolHosts ](#ApiClient.TestBenchConfiguration.GetToolHosts)
  - [M Refresh ](#ApiClient.TestBenchConfiguration.Refresh)
  - [M RemoveToolHost ](#ApiClient.TestBenchConfiguration.RemoveToolHost)
  - [M Save ](#ApiClient.TestBenchConfiguration.Save)

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

TestBenchConfiguration

- [C TestBenchConfiguration ](#ApiClient.TestBenchConfiguration)
  - [M CreateToolHost ](#ApiClient.TestBenchConfiguration.CreateToolHost)
  - [M GetFilename ](#ApiClient.TestBenchConfiguration.GetFilename)
  - [M GetPort ](#ApiClient.TestBenchConfiguration.GetPort)
  - [M GetTool ](#ApiClient.TestBenchConfiguration.GetTool)
  - [M GetToolHost ](#ApiClient.TestBenchConfiguration.GetToolHost)
  - [M GetToolHosts ](#ApiClient.TestBenchConfiguration.GetToolHosts)
  - [M Refresh ](#ApiClient.TestBenchConfiguration.Refresh)
  - [M RemoveToolHost ](#ApiClient.TestBenchConfiguration.RemoveToolHost)
  - [M Save ](#ApiClient.TestBenchConfiguration.Save)

# TestBenchConfiguration[¶](#testbenchconfiguration "Link to this heading")

*class* TestBenchConfiguration[¶](#ApiClient.TestBenchConfiguration "Link to this definition")  
Returned by

- [`ConfigurationApi.CreateTestBenchConfiguration`](../ConfigurationApi.md#ApiClient.ConfigurationApi.CreateTestBenchConfiguration "ApiClient.ConfigurationApi.CreateTestBenchConfiguration (Python method) — Creates new test bench configuration.")

- [`ConfigurationApi.OpenTestBenchConfiguration`](../ConfigurationApi.md#ApiClient.ConfigurationApi.OpenTestBenchConfiguration "ApiClient.ConfigurationApi.OpenTestBenchConfiguration (Python method) — Opens an existing test bench configuration (*.tbc).")

- [`ConfigurationApi.SearchTestBenchConfigurations`](../ConfigurationApi.md#ApiClient.ConfigurationApi.SearchTestBenchConfigurations "ApiClient.ConfigurationApi.SearchTestBenchConfigurations (Python method) — Searches the current workspace and library workspaces for Testbenchconfigurations matching the given search criteria.")

CreateToolHost(*[toolHostUrl](#ApiClient.TestBenchConfiguration.CreateToolHost.toolHostUrl "ApiClient.TestBenchConfiguration.CreateToolHost.toolHostUrl (Python parameter) — The URL of the created tool host")*)[¶](#ApiClient.TestBenchConfiguration.CreateToolHost "Link to this definition")  
Creates a new tool host with the given URL. E.g.:

- ‘local’

- ‘tsp:127.0.0.1:5017’

- ‘tsp:hostname:5017’

Parameters:  toolHostUrl : str[¶](#ApiClient.TestBenchConfiguration.CreateToolHost.toolHostUrl "Permalink to this definition")  
The URL of the created tool host

Returns:  The newly created tool host object

Return type:  [`ToolHost`](ToolHost.md#ApiClient.ToolHost "ApiClient.ToolHost (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")

GetFilename()[¶](#ApiClient.TestBenchConfiguration.GetFilename "Link to this definition")  
Returns the absolute path to the test bench configuration file. If empty, the file has not been saved yet.

Returns:  filename with extension

Return type:  str

GetPort(*[portId](#ApiClient.TestBenchConfiguration.GetPort.portId "ApiClient.TestBenchConfiguration.GetPort.portId (Python parameter) — Name of the port")*)[¶](#ApiClient.TestBenchConfiguration.GetPort "Link to this definition")  
Returns the port with the given portId.

Parameters:  portId : str[¶](#ApiClient.TestBenchConfiguration.GetPort.portId "Permalink to this definition")  
Name of the port

Returns:  The port object.

Return type:  [`Port`](Port.md#ApiClient.Port "ApiClient.Port (Python class) — Returns the constant used to specify the autostart option 'always': The port will always be started.")

Raises:  
**ApiError** – If there is no port with this Id.

GetTool(*[toolId](#ApiClient.TestBenchConfiguration.GetTool.toolId "ApiClient.TestBenchConfiguration.GetTool.toolId (Python parameter) — ID of the tool")*)[¶](#ApiClient.TestBenchConfiguration.GetTool "Link to this definition")  
Returns the tool with the given toolId.

Parameters:  toolId : str[¶](#ApiClient.TestBenchConfiguration.GetTool.toolId "Permalink to this definition")  
ID of the tool

Returns:  The tool object.

Return type:  [`Tool`](Tool.md#ApiClient.Tool "ApiClient.Tool (Python class) — The properties of this tool.")

Raises:  
**ApiError** – If there is no tool with this Id.

GetToolHost(*[url](#ApiClient.TestBenchConfiguration.GetToolHost.url "ApiClient.TestBenchConfiguration.GetToolHost.url (Python parameter) — URL of the tool host")*)[¶](#ApiClient.TestBenchConfiguration.GetToolHost "Link to this definition")  
Returns the tool host with the given URL.

Parameters:  url : str[¶](#ApiClient.TestBenchConfiguration.GetToolHost.url "Permalink to this definition")  
URL of the tool host

Returns:  The tool host object.

Return type:  [`ToolHost`](ToolHost.md#ApiClient.ToolHost "ApiClient.ToolHost (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")

Raises:  
**ApiError** – If there is no host using this URL.

GetToolHosts()[¶](#ApiClient.TestBenchConfiguration.GetToolHosts "Link to this definition")  
Returns a list of all tool hosts belonging to this testbench configuration.

Returns:  The list of all tool host objects

Return type:  list[[`ToolHost`](ToolHost.md#ApiClient.ToolHost "ApiClient.ToolHost (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")]

Refresh()[¶](#ApiClient.TestBenchConfiguration.Refresh "Link to this definition")  
Refreshes all hosts, tools and ports in the configuration

RemoveToolHost(*[toolHost](#ApiClient.TestBenchConfiguration.RemoveToolHost.toolHost "ApiClient.TestBenchConfiguration.RemoveToolHost.toolHost (Python parameter) — The tool host object to be removed")*)[¶](#ApiClient.TestBenchConfiguration.RemoveToolHost "Link to this definition")  
Removes the tool host and all configured tools and ports connected to it.

Parameters:  toolHost[¶](#ApiClient.TestBenchConfiguration.RemoveToolHost.toolHost "Permalink to this definition")  
The tool host object to be removed

Save(*[filename](#ApiClient.TestBenchConfiguration.Save.filename "ApiClient.TestBenchConfiguration.Save.filename (Python parameter) — The file name used for storing the test bench configuration file; Either absolute or relative to the 'Configuration' directory. Leave out to save the configuration to its existing file (from a previous call of Save() or from ConfigurationApi.OpenTestBenchConfiguration())")=`None`*)[¶](#ApiClient.TestBenchConfiguration.Save "Link to this definition")  
Saves the test bench configuration. Appends file ending if needed.

Parameters:  filename : str[¶](#ApiClient.TestBenchConfiguration.Save.filename "Permalink to this definition")  
The file name used for storing the test bench configuration file; Either absolute or relative to the ‘Configuration’ directory. Leave out to save the configuration to its existing file (from a previous call of [`Save()`](#ApiClient.TestBenchConfiguration.Save "ApiClient.TestBenchConfiguration.Save (Python method) — Saves the test bench configuration. Appends file ending if needed.") or from [`ConfigurationApi.OpenTestBenchConfiguration()`](../ConfigurationApi.md#ApiClient.ConfigurationApi.OpenTestBenchConfiguration "ApiClient.ConfigurationApi.OpenTestBenchConfiguration (Python method) — Opens an existing test bench configuration (*.tbc)."))

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
