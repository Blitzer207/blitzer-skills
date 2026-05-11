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

API for Analysis Jobs

[ AnalysisJob ](AnalysisJob.md)

AnalysisJobGenericSignal [ AnalysisJobGenericSignal ](#)

AnalysisJobGenericSignal

- [C AnalysisJobGenericSignal ](#ApiClient.AnalysisJobGenericSignal)
  - [M Clone ](#ApiClient.AnalysisJobGenericSignal.Clone)
  - [M GetMappingName ](#ApiClient.AnalysisJobGenericSignal.GetMappingName)
  - [M GetName ](#ApiClient.AnalysisJobGenericSignal.GetName)
  - [M GetRecording ](#ApiClient.AnalysisJobGenericSignal.GetRecording)
  - [M SetMappingName ](#ApiClient.AnalysisJobGenericSignal.SetMappingName)
  - [M SetRecording ](#ApiClient.AnalysisJobGenericSignal.SetRecording)

[ AnalysisJobRecording ](AnalysisJobRecording.md)

[ Mapping ](Mapping.md)

[ API for Artifacts ](../ArtifactApi.md)

[ API for Project Components ](../ComponentApi.md)

[ API for Configurations ](../ConfigurationApi.md)

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

AnalysisJobGenericSignal

- [C AnalysisJobGenericSignal ](#ApiClient.AnalysisJobGenericSignal)
  - [M Clone ](#ApiClient.AnalysisJobGenericSignal.Clone)
  - [M GetMappingName ](#ApiClient.AnalysisJobGenericSignal.GetMappingName)
  - [M GetName ](#ApiClient.AnalysisJobGenericSignal.GetName)
  - [M GetRecording ](#ApiClient.AnalysisJobGenericSignal.GetRecording)
  - [M SetMappingName ](#ApiClient.AnalysisJobGenericSignal.SetMappingName)
  - [M SetRecording ](#ApiClient.AnalysisJobGenericSignal.SetRecording)

# AnalysisJobGenericSignal[¶](#analysisjobgenericsignal "Link to this heading")

*class* AnalysisJobGenericSignal[¶](#ApiClient.AnalysisJobGenericSignal "Link to this definition")  
Returned by

- [`AnalysisJobApi.CreateGenericSignal`](../AnalysisJobApi.md#ApiClient.AnalysisJobApi.CreateGenericSignal "ApiClient.AnalysisJobApi.CreateGenericSignal (Python method) — Create a generic signal with a given name for a analysis job.")

Clone()[¶](#ApiClient.AnalysisJobGenericSignal.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`AnalysisJobGenericSignal`](#ApiClient.AnalysisJobGenericSignal "ApiClient.AnalysisJobGenericSignal (Python class) — AnalysisJobApi.CreateGenericSignal")

GetMappingName()[¶](#ApiClient.AnalysisJobGenericSignal.GetMappingName "Link to this definition")  
Returns the name of the mapping item of the recoding assigned to the generic signal.

Returns:  mapping name assigned to this signal, which is used to resolve the real signal.

Return type:  str

GetName()[¶](#ApiClient.AnalysisJobGenericSignal.GetName "Link to this definition")  
Returns the name of the generic signal.

Returns:  name of generic signal

Return type:  str

GetRecording(*[analysisJob](#ApiClient.AnalysisJobGenericSignal.GetRecording.analysisJob "ApiClient.AnalysisJobGenericSignal.GetRecording.analysisJob (Python parameter) — analysis job from which the assigned recording should be extracted.")*)[¶](#ApiClient.AnalysisJobGenericSignal.GetRecording "Link to this definition")  
Get assigned recording from analysis job.

Note:  
Do not use in the context of a analysis package (\*.ta)

Parameters:  analysisJob[¶](#ApiClient.AnalysisJobGenericSignal.GetRecording.analysisJob "Permalink to this definition")  
analysis job from which the assigned recording should be extracted.

Returns:  recording from analysis job which is assigned to the signal

Return type:  [`AnalysisJobRecording`](AnalysisJobRecording.md#ApiClient.AnalysisJobRecording "ApiClient.AnalysisJobRecording (Python class) — AnalysisJobApi.CreateRecording")

SetMappingName(*[mappingName](#ApiClient.AnalysisJobGenericSignal.SetMappingName.mappingName "ApiClient.AnalysisJobGenericSignal.SetMappingName.mappingName (Python parameter) — name of an existing mapping.")*)[¶](#ApiClient.AnalysisJobGenericSignal.SetMappingName "Link to this definition")  
Sets mapping name, which should be used to resolve the signal.

Parameters:  mappingName : str[¶](#ApiClient.AnalysisJobGenericSignal.SetMappingName.mappingName "Permalink to this definition")  
name of an existing mapping.

SetRecording(*[recording](#ApiClient.AnalysisJobGenericSignal.SetRecording.recording "ApiClient.AnalysisJobGenericSignal.SetRecording.recording (Python parameter) — recording or None, when signal should be resolved only from the mapping item name.")*)[¶](#ApiClient.AnalysisJobGenericSignal.SetRecording "Link to this definition")  
Set reference to recording which the signal will use.

Note:  
Do not use in the context of a analysis package (\*.ta)

Parameters:  recording[¶](#ApiClient.AnalysisJobGenericSignal.SetRecording.recording "Permalink to this definition")  
recording or None, when signal should be resolved only from the mapping item name. In the last case the mapping name must be unique in the analysis job.

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
