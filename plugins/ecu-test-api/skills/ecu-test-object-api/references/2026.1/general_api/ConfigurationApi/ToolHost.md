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

[ TestConfiguration ](TestConfiguration.md)

[ TestConfigurationGlobalConstants ](TestConfigurationGlobalConstants.md)

[ Tool ](Tool.md)

ToolHost [ ToolHost ](#)

ToolHost

- [C ToolHost ](#ApiClient.ToolHost)
  - [M Clone ](#ApiClient.ToolHost.Clone)
  - [M GetBasePath ](#ApiClient.ToolHost.GetBasePath)
  - [M GetTools ](#ApiClient.ToolHost.GetTools)
  - [M GetUrl ](#ApiClient.ToolHost.GetUrl)
  - [M InsertTool ](#ApiClient.ToolHost.InsertTool)
  - [M Refresh ](#ApiClient.ToolHost.Refresh)
  - [M RemoveTool ](#ApiClient.ToolHost.RemoveTool)
  - [M Rename ](#ApiClient.ToolHost.Rename)
  - [M SetBasePath ](#ApiClient.ToolHost.SetBasePath)
  - [M AddTool ](#ApiClient.ToolHost.AddTool)
  - [M CreateTool ](#ApiClient.ToolHost.CreateTool)
  - [M GetAvailableToolNames ](#ApiClient.ToolHost.GetAvailableToolNames)
  - [M GetToolAccessTimeout ](#ApiClient.ToolHost.GetToolAccessTimeout)
  - [M SetToolAccessTimeout ](#ApiClient.ToolHost.SetToolAccessTimeout)

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

ToolHost

- [C ToolHost ](#ApiClient.ToolHost)
  - [M Clone ](#ApiClient.ToolHost.Clone)
  - [M GetBasePath ](#ApiClient.ToolHost.GetBasePath)
  - [M GetTools ](#ApiClient.ToolHost.GetTools)
  - [M GetUrl ](#ApiClient.ToolHost.GetUrl)
  - [M InsertTool ](#ApiClient.ToolHost.InsertTool)
  - [M Refresh ](#ApiClient.ToolHost.Refresh)
  - [M RemoveTool ](#ApiClient.ToolHost.RemoveTool)
  - [M Rename ](#ApiClient.ToolHost.Rename)
  - [M SetBasePath ](#ApiClient.ToolHost.SetBasePath)
  - [M AddTool ](#ApiClient.ToolHost.AddTool)
  - [M CreateTool ](#ApiClient.ToolHost.CreateTool)
  - [M GetAvailableToolNames ](#ApiClient.ToolHost.GetAvailableToolNames)
  - [M GetToolAccessTimeout ](#ApiClient.ToolHost.GetToolAccessTimeout)
  - [M SetToolAccessTimeout ](#ApiClient.ToolHost.SetToolAccessTimeout)

# ToolHost[¶](#toolhost "Link to this heading")

*class* ToolHost[¶](#ApiClient.ToolHost "Link to this definition")  
Clone()[¶](#ApiClient.ToolHost.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`ToolHost`](#ApiClient.ToolHost "ApiClient.ToolHost (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")

GetBasePath()[¶](#ApiClient.ToolHost.GetBasePath "Link to this definition")  
Returns the tool host base path that is used for several tool property settings.

Returns:  The tool host base path

Return type:  str

GetTools()[¶](#ApiClient.ToolHost.GetTools "Link to this definition")  
Returns all tools used by this tool host.

Returns:  A list of the used tools.

Return type:  list[[`Tool`](Tool.md#ApiClient.Tool "ApiClient.Tool (Python class) — The properties of this tool.")]

GetUrl()[¶](#ApiClient.ToolHost.GetUrl "Link to this definition")  
Returns the tool host URL.

Returns:  The URL

Return type:  str

InsertTool(*[tool](#ApiClient.ToolHost.InsertTool.tool "ApiClient.ToolHost.InsertTool.tool (Python parameter) — Tool to be copied")*)[¶](#ApiClient.ToolHost.InsertTool "Link to this definition")  
Adds a copy of the given tool to the toolhost. If the tool ID (alias) is already present in the destination test bench configuration, a new ID will automatically be assigned. The same applies to port IDs that are already taken. If a port of the given tool can’t be copied, it will be omitted.

Parameters:  tool[¶](#ApiClient.ToolHost.InsertTool.tool "Permalink to this definition")  
Tool to be copied

Returns:  Tool that was copied to the toolhost

Return type:  [Tool](Tool.md#ApiClient.Tool "ApiClient.Tool (Python class) — The properties of this tool.")

Raises:  
**ApiError** – If tool could not be inserted

Refresh()[¶](#ApiClient.ToolHost.Refresh "Link to this definition")  
Refreshes the tool and all its ports

RemoveTool(*[tool](#ApiClient.ToolHost.RemoveTool.tool "ApiClient.ToolHost.RemoveTool.tool (Python parameter) — The tool to be removed")*)[¶](#ApiClient.ToolHost.RemoveTool "Link to this definition")  
Removes the tool and all configured ports from the tool host.

Parameters:  tool[¶](#ApiClient.ToolHost.RemoveTool.tool "Permalink to this definition")  
The tool to be removed

Rename(*[newUrl](#ApiClient.ToolHost.Rename.newUrl "ApiClient.ToolHost.Rename.newUrl (Python parameter) — New URL")*)[¶](#ApiClient.ToolHost.Rename "Link to this definition")  
Sets the URL of a given tool host. E.g.:

- ‘local’

- ‘tsp:127.0.0.1:5017’

- ‘tsp:hostname:5017’

Parameters:  newUrl : str[¶](#ApiClient.ToolHost.Rename.newUrl "Permalink to this definition")  
New URL

SetBasePath(*[basePath](#ApiClient.ToolHost.SetBasePath.basePath "ApiClient.ToolHost.SetBasePath.basePath (Python parameter) — Base path on the tool host")*)[¶](#ApiClient.ToolHost.SetBasePath "Link to this definition")  
Sets the tool host base path. A value of ‘\<workspace\>’ represents the current workspace path and can be combined with sub-paths (e.g., ‘\<workspace\>/Models’).

Parameters:  basePath : str[¶](#ApiClient.ToolHost.SetBasePath.basePath "Permalink to this definition")  
Base path on the tool host

AddTool(*[toolName](#ApiClient.ToolHost.AddTool.toolName "ApiClient.ToolHost.AddTool.toolName (Python parameter) — The name of the tool to use.")*, *[useLegacyName](#ApiClient.ToolHost.AddTool.useLegacyName "ApiClient.ToolHost.AddTool.useLegacyName (Python parameter) — Prefer short legacy/internal name for the tool instead of combination of vendor and tool name")=`True`*)[¶](#ApiClient.ToolHost.AddTool "Link to this definition")  
Configures a tool to be used by the corresponding test bench configuration.

Parameters:  toolName : str[¶](#ApiClient.ToolHost.AddTool.toolName "Permalink to this definition")  
The name of the tool to use. Use [`GetAvailableToolNames()`](#ApiClient.ToolHost.GetAvailableToolNames "ApiClient.ToolHost.GetAvailableToolNames (Python method) — Returns a list of all tools that are available on this tool host.") to get a list of all available tool names.

useLegacyName : bool[¶](#ApiClient.ToolHost.AddTool.useLegacyName "Permalink to this definition")  
Prefer short legacy/internal name for the tool instead of combination of vendor and tool name

Returns:  The created tool object

Return type:  [`Tool`](Tool.md#ApiClient.Tool "ApiClient.Tool (Python class) — The properties of this tool.")

Deprecated since version 2025.2: Please use method `CreateTool` instead.

CreateTool(*[toolName](#ApiClient.ToolHost.CreateTool.toolName "ApiClient.ToolHost.CreateTool.toolName (Python parameter) — The name of the tool to use.")*, *[useLegacyName](#ApiClient.ToolHost.CreateTool.useLegacyName "ApiClient.ToolHost.CreateTool.useLegacyName (Python parameter) — (deprecated) Prefer short legacy/internal name for the tool instead of combination of vendor and tool name")=`True`*)[¶](#ApiClient.ToolHost.CreateTool "Link to this definition")  
Creates and configures a tool to be used by the corresponding test bench configuration.

Parameters:  toolName : str[¶](#ApiClient.ToolHost.CreateTool.toolName "Permalink to this definition")  
The name of the tool to use. Use [`GetAvailableToolNames()`](#ApiClient.ToolHost.GetAvailableToolNames "ApiClient.ToolHost.GetAvailableToolNames (Python method) — Returns a list of all tools that are available on this tool host.") to get a list of all available tool names.

useLegacyName : bool[¶](#ApiClient.ToolHost.CreateTool.useLegacyName "Permalink to this definition")  
**(deprecated)** Prefer short legacy/internal name for the tool instead of combination of vendor and tool name

Returns:  The created tool object

Return type:  [`Tool`](Tool.md#ApiClient.Tool "ApiClient.Tool (Python class) — The properties of this tool.")

Raises:  
**ApiError** –

If tool could not be created

Deprecated since version 2026.1: The parameter `useLegacyName` will be removed in a future version.

GetAvailableToolNames(*[getLegacyNames](#ApiClient.ToolHost.GetAvailableToolNames.getLegacyNames "ApiClient.ToolHost.GetAvailableToolNames.getLegacyNames (Python parameter) — (deprecated) Get short legacy/internal names for the tool instead of combination of vendor and tool name")=`False`*)[¶](#ApiClient.ToolHost.GetAvailableToolNames "Link to this definition")  
Returns a list of all tools that are available on this tool host.

Parameters:  getLegacyNames : bool[¶](#ApiClient.ToolHost.GetAvailableToolNames.getLegacyNames "Permalink to this definition")  
**(deprecated)** Get short legacy/internal names for the tool instead of combination of vendor and tool name

Returns:  The list of available tools

Return type:  list[str]

Deprecated since version 2026.1: The parameter `getLegacyNames` will be removed in a future version.

GetToolAccessTimeout()[¶](#ApiClient.ToolHost.GetToolAccessTimeout "Link to this definition")  
Returns the minimum of timeouts for all tool calls.

Returns:  timeout in seconds

Return type:  int

Deprecated since version 2024.2: Tool access timeout can now be accessed as a property on the tool.

SetToolAccessTimeout(*[timeout](#ApiClient.ToolHost.SetToolAccessTimeout.timeout "ApiClient.ToolHost.SetToolAccessTimeout.timeout (Python parameter) — timeout in seconds")*)[¶](#ApiClient.ToolHost.SetToolAccessTimeout "Link to this definition")  
Sets the timeout for tool calls. After that time, a tool call will be terminated with an error.

Parameters:  timeout[¶](#ApiClient.ToolHost.SetToolAccessTimeout.timeout "Permalink to this definition")  
timeout in seconds

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
