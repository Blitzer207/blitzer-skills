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

[ AnalysisJobGenericSignal ](AnalysisJobGenericSignal.md)

AnalysisJobRecording [ AnalysisJobRecording ](#)

AnalysisJobRecording

- [C AnalysisJobRecording ](#ApiClient.AnalysisJobRecording)
  - [M AddMappingName ](#ApiClient.AnalysisJobRecording.AddMappingName)
  - [M Clone ](#ApiClient.AnalysisJobRecording.Clone)
  - [M GetDescription ](#ApiClient.AnalysisJobRecording.GetDescription)
  - [M GetMappingNames ](#ApiClient.AnalysisJobRecording.GetMappingNames)
  - [M GetName ](#ApiClient.AnalysisJobRecording.GetName)
  - [M GetRecordingInfo ](#ApiClient.AnalysisJobRecording.GetRecordingInfo)
  - [M RemoveMappingName ](#ApiClient.AnalysisJobRecording.RemoveMappingName)
  - [M SetDescription ](#ApiClient.AnalysisJobRecording.SetDescription)
  - [M SetMappingNames ](#ApiClient.AnalysisJobRecording.SetMappingNames)
  - [M SetRecordingInfo ](#ApiClient.AnalysisJobRecording.SetRecordingInfo)

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

AnalysisJobRecording

- [C AnalysisJobRecording ](#ApiClient.AnalysisJobRecording)
  - [M AddMappingName ](#ApiClient.AnalysisJobRecording.AddMappingName)
  - [M Clone ](#ApiClient.AnalysisJobRecording.Clone)
  - [M GetDescription ](#ApiClient.AnalysisJobRecording.GetDescription)
  - [M GetMappingNames ](#ApiClient.AnalysisJobRecording.GetMappingNames)
  - [M GetName ](#ApiClient.AnalysisJobRecording.GetName)
  - [M GetRecordingInfo ](#ApiClient.AnalysisJobRecording.GetRecordingInfo)
  - [M RemoveMappingName ](#ApiClient.AnalysisJobRecording.RemoveMappingName)
  - [M SetDescription ](#ApiClient.AnalysisJobRecording.SetDescription)
  - [M SetMappingNames ](#ApiClient.AnalysisJobRecording.SetMappingNames)
  - [M SetRecordingInfo ](#ApiClient.AnalysisJobRecording.SetRecordingInfo)

# AnalysisJobRecording[¶](#analysisjobrecording "Link to this heading")

*class* AnalysisJobRecording[¶](#ApiClient.AnalysisJobRecording "Link to this definition")  
Returned by

- [`AnalysisJobApi.CreateRecording`](../AnalysisJobApi.md#ApiClient.AnalysisJobApi.CreateRecording "ApiClient.AnalysisJobApi.CreateRecording (Python method) — Create a recording for a analysis job.")

AddMappingName(*[mappingName](#ApiClient.AnalysisJobRecording.AddMappingName.mappingName "ApiClient.AnalysisJobRecording.AddMappingName.mappingName (Python parameter) — Mapping name to add")*)[¶](#ApiClient.AnalysisJobRecording.AddMappingName "Link to this definition")  
Adds mapping name to this recording.

Note:  
Only use in the context of a analysis package (\*.ta)

Parameters:  mappingName : str[¶](#ApiClient.AnalysisJobRecording.AddMappingName.mappingName "Permalink to this definition")  
Mapping name to add

Clone()[¶](#ApiClient.AnalysisJobRecording.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`AnalysisJobRecording`](#ApiClient.AnalysisJobRecording "ApiClient.AnalysisJobRecording (Python class) — AnalysisJobApi.CreateRecording")

GetDescription()[¶](#ApiClient.AnalysisJobRecording.GetDescription "Link to this definition")  
Returns description of recording (corresponds to recording group description in trace analysis)

Returns:  Description of this recording

Return type:  str

GetMappingNames()[¶](#ApiClient.AnalysisJobRecording.GetMappingNames "Link to this definition")  
Returns all mapping names of this recording.

Note:  
Only use in the context of a analysis package (\*.ta)

Returns:  Mapping names

Return type:  list[str]

GetName()[¶](#ApiClient.AnalysisJobRecording.GetName "Link to this definition")  
Returns name of recording (corresponds to recording group name in trace analysis)

Returns:  Name of this recording

Return type:  str

GetRecordingInfo()[¶](#ApiClient.AnalysisJobRecording.GetRecordingInfo "Link to this definition")  
Returns recording info object of the recording

Returns:  Recording info object of the recording

Return type:  [`RecordingInfo`](../SignalRecordingApi/RecordingInfo.md#ApiClient.RecordingInfo "ApiClient.RecordingInfo (Python class) — SignalRecordingApi.CreateRecordingInfo")

RemoveMappingName(*[mappingName](#ApiClient.AnalysisJobRecording.RemoveMappingName.mappingName "ApiClient.AnalysisJobRecording.RemoveMappingName.mappingName (Python parameter) — Mapping name to remove")*)[¶](#ApiClient.AnalysisJobRecording.RemoveMappingName "Link to this definition")  
Removes mapping name from this recording.

Note:  
Only use in the context of a analysis package (\*.ta)

Parameters:  mappingName : str[¶](#ApiClient.AnalysisJobRecording.RemoveMappingName.mappingName "Permalink to this definition")  
Mapping name to remove

SetDescription(*[value](#ApiClient.AnalysisJobRecording.SetDescription.value "ApiClient.AnalysisJobRecording.SetDescription.value (Python parameter) — New description")*)[¶](#ApiClient.AnalysisJobRecording.SetDescription "Link to this definition")  
Sets description of recording.

Parameters:  value : str[¶](#ApiClient.AnalysisJobRecording.SetDescription.value "Permalink to this definition")  
New description

SetMappingNames(*[mappingNames](#ApiClient.AnalysisJobRecording.SetMappingNames.mappingNames "ApiClient.AnalysisJobRecording.SetMappingNames.mappingNames (Python parameter) — New mapping names")*)[¶](#ApiClient.AnalysisJobRecording.SetMappingNames "Link to this definition")  
Sets mapping names of this recording.

Note:  
Only use in the context of a analysis package (\*.ta)

Parameters:  mappingNames : list[str][¶](#ApiClient.AnalysisJobRecording.SetMappingNames.mappingNames "Permalink to this definition")  
New mapping names

SetRecordingInfo(*[value](#ApiClient.AnalysisJobRecording.SetRecordingInfo.value "ApiClient.AnalysisJobRecording.SetRecordingInfo.value (Python parameter) — New recording info object")*)[¶](#ApiClient.AnalysisJobRecording.SetRecordingInfo "Link to this definition")  
Sets recording info object of the recording

Parameters:  value[¶](#ApiClient.AnalysisJobRecording.SetRecordingInfo.value "Permalink to this definition")  
New recording info object

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
