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

ReportData [ ReportData ](#)

ReportData

- [C ReportData ](#ApiClient.ReportData)
  - [M AddReportFormat ](#ApiClient.ReportData.AddReportFormat)
  - [M Clone ](#ApiClient.ReportData.Clone)
  - [M CreateReportFormat ](#ApiClient.ReportData.CreateReportFormat)
  - [M GetAvailableOutputFormats ](#ApiClient.ReportData.GetAvailableOutputFormats)
  - [M GetConfiguredOutputFormats ](#ApiClient.ReportData.GetConfiguredOutputFormats)
  - [M GetCopyLogFilesToReportFolder ](#ApiClient.ReportData.GetCopyLogFilesToReportFolder)
  - [M GetDirectory ](#ApiClient.ReportData.GetDirectory)
  - [M GetReportFormat ](#ApiClient.ReportData.GetReportFormat)
  - [M GetReportFormats ](#ApiClient.ReportData.GetReportFormats)
  - [M GetUserDefinedInfoScript ](#ApiClient.ReportData.GetUserDefinedInfoScript)
  - [M GetUserReportData ](#ApiClient.ReportData.GetUserReportData)
  - [M RemoveReportFormat ](#ApiClient.ReportData.RemoveReportFormat)
  - [M RemoveReportFormatByName ](#ApiClient.ReportData.RemoveReportFormatByName)
  - [M SetCopyLogFilesToReportFolder ](#ApiClient.ReportData.SetCopyLogFilesToReportFolder)
  - [M SetDirectory ](#ApiClient.ReportData.SetDirectory)
  - [M SetUserDefinedInfoScript ](#ApiClient.ReportData.SetUserDefinedInfoScript)

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

ReportData

- [C ReportData ](#ApiClient.ReportData)
  - [M AddReportFormat ](#ApiClient.ReportData.AddReportFormat)
  - [M Clone ](#ApiClient.ReportData.Clone)
  - [M CreateReportFormat ](#ApiClient.ReportData.CreateReportFormat)
  - [M GetAvailableOutputFormats ](#ApiClient.ReportData.GetAvailableOutputFormats)
  - [M GetConfiguredOutputFormats ](#ApiClient.ReportData.GetConfiguredOutputFormats)
  - [M GetCopyLogFilesToReportFolder ](#ApiClient.ReportData.GetCopyLogFilesToReportFolder)
  - [M GetDirectory ](#ApiClient.ReportData.GetDirectory)
  - [M GetReportFormat ](#ApiClient.ReportData.GetReportFormat)
  - [M GetReportFormats ](#ApiClient.ReportData.GetReportFormats)
  - [M GetUserDefinedInfoScript ](#ApiClient.ReportData.GetUserDefinedInfoScript)
  - [M GetUserReportData ](#ApiClient.ReportData.GetUserReportData)
  - [M RemoveReportFormat ](#ApiClient.ReportData.RemoveReportFormat)
  - [M RemoveReportFormatByName ](#ApiClient.ReportData.RemoveReportFormatByName)
  - [M SetCopyLogFilesToReportFolder ](#ApiClient.ReportData.SetCopyLogFilesToReportFolder)
  - [M SetDirectory ](#ApiClient.ReportData.SetDirectory)
  - [M SetUserDefinedInfoScript ](#ApiClient.ReportData.SetUserDefinedInfoScript)

# ReportData[¶](#reportdata "Link to this heading")

*class* ReportData[¶](#ApiClient.ReportData "Link to this definition")  
AddReportFormat(*[reportFormat](#ApiClient.ReportData.AddReportFormat.reportFormat "ApiClient.ReportData.AddReportFormat.reportFormat (Python parameter) — Report format to be added")*)[¶](#ApiClient.ReportData.AddReportFormat "Link to this definition")  
Adds a report format to your configuration.

Parameters:  reportFormat[¶](#ApiClient.ReportData.AddReportFormat.reportFormat "Permalink to this definition")  
Report format to be added

Clone()[¶](#ApiClient.ReportData.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`ReportData`](#ApiClient.ReportData "ApiClient.ReportData (Python class) — Adds a report format to your configuration.")

CreateReportFormat(*[formatName](#ApiClient.ReportData.CreateReportFormat.formatName "ApiClient.ReportData.CreateReportFormat.formatName (Python parameter) — Format handler (e.g.")*)[¶](#ApiClient.ReportData.CreateReportFormat "Link to this definition")  
Create a new Output format.

Parameters:  formatName : str[¶](#ApiClient.ReportData.CreateReportFormat.formatName "Permalink to this definition")  
Format handler (e.g. “HTML”, “EXCEL”, …)

Returns:  New report format

Return type:  [`ReportFormat`](ReportFormat.md#ApiClient.ReportFormat "ApiClient.ReportFormat (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")

GetAvailableOutputFormats()[¶](#ApiClient.ReportData.GetAvailableOutputFormats "Link to this definition")  
Returns a list of available output formats.

Returns:  List of report format names

Return type:  list[str]

GetConfiguredOutputFormats(*[showActiveOnly](#ApiClient.ReportData.GetConfiguredOutputFormats.showActiveOnly "ApiClient.ReportData.GetConfiguredOutputFormats.showActiveOnly (Python parameter) — If True only formats that will be automatically generated are shown.")=`False`*)[¶](#ApiClient.ReportData.GetConfiguredOutputFormats "Link to this definition")  
Returns a list of display names from configured output formats.

Parameters:  showActiveOnly : bool[¶](#ApiClient.ReportData.GetConfiguredOutputFormats.showActiveOnly "Permalink to this definition")  
If True only formats that will be automatically generated are shown.

Returns:  List of report format names

Return type:  list[str]

GetCopyLogFilesToReportFolder()[¶](#ApiClient.ReportData.GetCopyLogFilesToReportFolder "Link to this definition")  
Gets the state of the option to copy log files to report folder.

Returns:  State of the option.

Return type:  bool

GetDirectory()[¶](#ApiClient.ReportData.GetDirectory "Link to this definition")  
Returns the report directory.

Returns:  Report directory

Return type:  str

GetReportFormat(*[displayName](#ApiClient.ReportData.GetReportFormat.displayName "ApiClient.ReportData.GetReportFormat.displayName (Python parameter) — Name of the report format")*)[¶](#ApiClient.ReportData.GetReportFormat "Link to this definition")  
Return the report format with the given displayname.

Parameters:  displayName : string[¶](#ApiClient.ReportData.GetReportFormat.displayName "Permalink to this definition")  
Name of the report format

Returns:  Report format object

Return type:  [`ReportFormat`](ReportFormat.md#ApiClient.ReportFormat "ApiClient.ReportFormat (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")

GetReportFormats(*[autoGenerateOnly](#ApiClient.ReportData.GetReportFormats.autoGenerateOnly "ApiClient.ReportData.GetReportFormats.autoGenerateOnly (Python parameter) — If True only formats that will be automatically generated are shown.")*)[¶](#ApiClient.ReportData.GetReportFormats "Link to this definition")  
Returns a list of configured report formats.

Parameters:  autoGenerateOnly : bool[¶](#ApiClient.ReportData.GetReportFormats.autoGenerateOnly "Permalink to this definition")  
If True only formats that will be automatically generated are shown.

Returns:  List of report format display names

Return type:  list[[`ReportFormat`](ReportFormat.md#ApiClient.ReportFormat "ApiClient.ReportFormat (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")]

GetUserDefinedInfoScript()[¶](#ApiClient.ReportData.GetUserDefinedInfoScript "Link to this definition")  
Returns the script file for generating user defined report information.

Returns:  Path to the \*.py file. Absolute or relative to workspace.

Return type:  str

GetUserReportData()[¶](#ApiClient.ReportData.GetUserReportData "Link to this definition")  
Returns user defined report information.

Returns:  User defined report information

Return type:  [`UserReportData`](UserReportData.md#ApiClient.UserReportData "ApiClient.UserReportData (Python class) — Appends a new entry. If a entry with the same name already exists, it will be overwritten.")

RemoveReportFormat(*[reportFormat](#ApiClient.ReportData.RemoveReportFormat.reportFormat "ApiClient.ReportData.RemoveReportFormat.reportFormat (Python parameter) — Report format to be removed")*)[¶](#ApiClient.ReportData.RemoveReportFormat "Link to this definition")  
Removes the report format.

Parameters:  reportFormat[¶](#ApiClient.ReportData.RemoveReportFormat.reportFormat "Permalink to this definition")  
Report format to be removed

RemoveReportFormatByName(*[displayedName](#ApiClient.ReportData.RemoveReportFormatByName.displayedName "ApiClient.ReportData.RemoveReportFormatByName.displayedName (Python parameter) — Format name (e.g.")*)[¶](#ApiClient.ReportData.RemoveReportFormatByName "Link to this definition")  
Removes an report format by name.

Parameters:  displayedName : str[¶](#ApiClient.ReportData.RemoveReportFormatByName.displayedName "Permalink to this definition")  
Format name (e.g. “New HTML report”)

SetCopyLogFilesToReportFolder(*[state](#ApiClient.ReportData.SetCopyLogFilesToReportFolder.state "ApiClient.ReportData.SetCopyLogFilesToReportFolder.state (Python parameter) — Enable or disable copy")*)[¶](#ApiClient.ReportData.SetCopyLogFilesToReportFolder "Link to this definition")  
Enable or disable the option to copy log files to report folder.

Parameters:  state : bool[¶](#ApiClient.ReportData.SetCopyLogFilesToReportFolder.state "Permalink to this definition")  
Enable or disable copy

SetDirectory(*[reportDir](#ApiClient.ReportData.SetDirectory.reportDir "ApiClient.ReportData.SetDirectory.reportDir (Python parameter) — Report directory to be set")*)[¶](#ApiClient.ReportData.SetDirectory "Link to this definition")  
Sets the report directory.

Parameters:  reportDir : str[¶](#ApiClient.ReportData.SetDirectory.reportDir "Permalink to this definition")  
Report directory to be set

SetUserDefinedInfoScript(*[filepath](#ApiClient.ReportData.SetUserDefinedInfoScript.filepath "ApiClient.ReportData.SetUserDefinedInfoScript.filepath (Python parameter) — Path to the *.py file.")*)[¶](#ApiClient.ReportData.SetUserDefinedInfoScript "Link to this definition")  
Sets the script file for generating user defined report information.

Parameters:  filepath : str[¶](#ApiClient.ReportData.SetUserDefinedInfoScript.filepath "Permalink to this definition")  
Path to the \*.py file. Absolute or relative to the workspace. If an empty string is passed, the script path will be reset.

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
