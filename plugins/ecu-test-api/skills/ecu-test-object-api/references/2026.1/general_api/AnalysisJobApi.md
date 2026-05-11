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

[ API for Analysis Jobs ](#)

API for Analysis Jobs

- [ AnalysisJob ](AnalysisJobApi/AnalysisJob.md)
- [ AnalysisJobGenericSignal ](AnalysisJobApi/AnalysisJobGenericSignal.md)
- [ AnalysisJobRecording ](AnalysisJobApi/AnalysisJobRecording.md)
- [ Mapping ](AnalysisJobApi/Mapping.md)

API for Analysis Jobs [ API for Analysis Jobs ](#)

API for Analysis Jobs

- [C AnalysisJobApi ](#ApiClient.AnalysisJobApi)
  - [M CreateAnalysisJob ](#ApiClient.AnalysisJobApi.CreateAnalysisJob)
  - [M CreateGenericSignal ](#ApiClient.AnalysisJobApi.CreateGenericSignal)
  - [M CreateRecording ](#ApiClient.AnalysisJobApi.CreateRecording)
  - [M OpenAnalysisJob ](#ApiClient.AnalysisJobApi.OpenAnalysisJob)
- [ AnalysisJob ](AnalysisJobApi/AnalysisJob.md)
- [ AnalysisJobGenericSignal ](AnalysisJobApi/AnalysisJobGenericSignal.md)
- [ AnalysisJobRecording ](AnalysisJobApi/AnalysisJobRecording.md)
- [ Mapping ](AnalysisJobApi/Mapping.md)

[ API for Artifacts ](ArtifactApi.md)

[ API for Project Components ](ComponentApi.md)

[ API for Configurations ](ConfigurationApi.md)

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

API for Analysis Jobs

- [C AnalysisJobApi ](#ApiClient.AnalysisJobApi)
  - [M CreateAnalysisJob ](#ApiClient.AnalysisJobApi.CreateAnalysisJob)
  - [M CreateGenericSignal ](#ApiClient.AnalysisJobApi.CreateGenericSignal)
  - [M CreateRecording ](#ApiClient.AnalysisJobApi.CreateRecording)
  - [M OpenAnalysisJob ](#ApiClient.AnalysisJobApi.OpenAnalysisJob)

# API for Analysis Jobs[¶](#api-for-analysis-jobs "Link to this heading")

Part of the [Object based program API](objectApi.md#objectapi).

*class* AnalysisJobApi[¶](#ApiClient.AnalysisJobApi "Link to this definition")  
Returned by

- [`ApiClient.AnalysisJobApi`](objectApi.md#ApiClient.ApiClient.AnalysisJobApi "ApiClient.ApiClient.AnalysisJobApi (Python attribute) — Returns the AnalysisJobApi namespace")

CreateAnalysisJob()[¶](#ApiClient.AnalysisJobApi.CreateAnalysisJob "Link to this definition")  
Creates a new analysis job

Returns:  A newly created analysis job

Return type:  [`AnalysisJob`](AnalysisJobApi/AnalysisJob.md#ApiClient.AnalysisJob "ApiClient.AnalysisJob (Python class) — AnalysisJobApi.CreateAnalysisJob")

CreateGenericSignal(*[signalName](#ApiClient.AnalysisJobApi.CreateGenericSignal.signalName "ApiClient.AnalysisJobApi.CreateGenericSignal.signalName (Python parameter) — signal name")*)[¶](#ApiClient.AnalysisJobApi.CreateGenericSignal "Link to this definition")  
Create a generic signal with a given name for a analysis job.

Parameters:  signalName : str[¶](#ApiClient.AnalysisJobApi.CreateGenericSignal.signalName "Permalink to this definition")  
signal name

Returns:  newly created generic analysis job signal

Return type:  [`AnalysisJobGenericSignal`](AnalysisJobApi/AnalysisJobGenericSignal.md#ApiClient.AnalysisJobGenericSignal "ApiClient.AnalysisJobGenericSignal (Python class) — AnalysisJobApi.CreateGenericSignal")

CreateRecording(*[recordingName](#ApiClient.AnalysisJobApi.CreateRecording.recordingName "ApiClient.AnalysisJobApi.CreateRecording.recordingName (Python parameter) — recording name")*)[¶](#ApiClient.AnalysisJobApi.CreateRecording "Link to this definition")  
Create a recording for a analysis job.

Parameters:  recordingName : str[¶](#ApiClient.AnalysisJobApi.CreateRecording.recordingName "Permalink to this definition")  
recording name

Returns:  newly created analysis job recording

Return type:  [`AnalysisJobRecording`](AnalysisJobApi/AnalysisJobRecording.md#ApiClient.AnalysisJobRecording "ApiClient.AnalysisJobRecording (Python class) — AnalysisJobApi.CreateRecording")

OpenAnalysisJob(*[filename](#ApiClient.AnalysisJobApi.OpenAnalysisJob.filename "ApiClient.AnalysisJobApi.OpenAnalysisJob.filename (Python parameter) — Absolute path to the analysis job file (.ajob) or relative path in regard to the workspace directory")*)[¶](#ApiClient.AnalysisJobApi.OpenAnalysisJob "Link to this definition")  
Opens an existing analysis job

Parameters:  filename : str[¶](#ApiClient.AnalysisJobApi.OpenAnalysisJob.filename "Permalink to this definition")  
Absolute path to the analysis job file (.ajob) or relative path in regard to the workspace directory

Returns:  Existing analysis job

Return type:  [`AnalysisJob`](AnalysisJobApi/AnalysisJob.md#ApiClient.AnalysisJob "ApiClient.AnalysisJob (Python class) — AnalysisJobApi.CreateAnalysisJob")

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
