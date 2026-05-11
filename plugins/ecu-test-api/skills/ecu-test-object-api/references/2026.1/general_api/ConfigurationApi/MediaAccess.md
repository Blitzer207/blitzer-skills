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

MediaAccess [ MediaAccess ](#)

MediaAccess

- [C MediaAccess ](#ApiClient.MediaAccess)
  - [M Add ](#ApiClient.MediaAccess.Add)
  - [M Clone ](#ApiClient.MediaAccess.Clone)
  - [M Delete ](#ApiClient.MediaAccess.Delete)
  - [M Get ](#ApiClient.MediaAccess.Get)
  - [M GetAll ](#ApiClient.MediaAccess.GetAll)
  - [M GetOcrDataProvidedByEcuTest ](#ApiClient.MediaAccess.GetOcrDataProvidedByEcuTest)

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

MediaAccess

- [C MediaAccess ](#ApiClient.MediaAccess)
  - [M Add ](#ApiClient.MediaAccess.Add)
  - [M Clone ](#ApiClient.MediaAccess.Clone)
  - [M Delete ](#ApiClient.MediaAccess.Delete)
  - [M Get ](#ApiClient.MediaAccess.Get)
  - [M GetAll ](#ApiClient.MediaAccess.GetAll)
  - [M GetOcrDataProvidedByEcuTest ](#ApiClient.MediaAccess.GetOcrDataProvidedByEcuTest)

# MediaAccess[¶](#mediaaccess "Link to this heading")

*class* MediaAccess[¶](#ApiClient.MediaAccess "Link to this definition")  
Add(*[mediaKey](#ApiClient.MediaAccess.Add.mediaKey "ApiClient.MediaAccess.Add.mediaKey (Python parameter) — Name of the media")*)[¶](#ApiClient.MediaAccess.Add "Link to this definition")  
Adds a media object.

Parameters:  mediaKey : str[¶](#ApiClient.MediaAccess.Add.mediaKey "Permalink to this definition")  
Name of the media

Returns:  The media object

Return type:  [`Media`](Media.md#ApiClient.Media "ApiClient.Media (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")

Clone()[¶](#ApiClient.MediaAccess.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`MediaAccess`](#ApiClient.MediaAccess "ApiClient.MediaAccess (Python class) — Adds a media object.")

Delete(*[mediaKey](#ApiClient.MediaAccess.Delete.mediaKey "ApiClient.MediaAccess.Delete.mediaKey (Python parameter) — Name of media to delete")*)[¶](#ApiClient.MediaAccess.Delete "Link to this definition")  
Deletes a media from media access.

Parameters:  mediaKey : str[¶](#ApiClient.MediaAccess.Delete.mediaKey "Permalink to this definition")  
Name of media to delete

Raises:  
**ApiError** – If there is no media with the given name

Get(*[mediaKey](#ApiClient.MediaAccess.Get.mediaKey "ApiClient.MediaAccess.Get.mediaKey (Python parameter) — Name of the media")*)[¶](#ApiClient.MediaAccess.Get "Link to this definition")  
Returns a media object.

Parameters:  mediaKey : str[¶](#ApiClient.MediaAccess.Get.mediaKey "Permalink to this definition")  
Name of the media

Returns:  The media object

Return type:  [`Media`](Media.md#ApiClient.Media "ApiClient.Media (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")

Raises:  
**ApiError** – If no media with the given name is configured.

GetAll()[¶](#ApiClient.MediaAccess.GetAll "Link to this definition")  
Returns a list of names of all medias.

Returns:  Names of all medias.

Return type:  list[str]

GetOcrDataProvidedByEcuTest()[¶](#ApiClient.MediaAccess.GetOcrDataProvidedByEcuTest "Link to this definition")  
Returns a list with all ocr data names provided by ecu.test.

Returns:  List with ocr data names

Return type:  list[str]

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
