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

API for Signal Recordings

[ RecordingGroup ](RecordingGroup.md)

RecordingInfo [ RecordingInfo ](#)

RecordingInfo

- [C RecordingInfo ](#ApiClient.RecordingInfo)
  - [M Clone ](#ApiClient.RecordingInfo.Clone)
  - [M DeleteFormatDetails ](#ApiClient.RecordingInfo.DeleteFormatDetails)
  - [M GetFormatDetailsString ](#ApiClient.RecordingInfo.GetFormatDetailsString)
  - [M GetPath ](#ApiClient.RecordingInfo.GetPath)
  - [M GetPathList ](#ApiClient.RecordingInfo.GetPathList)
  - [M GetRecordingName ](#ApiClient.RecordingInfo.GetRecordingName)
  - [M GetRecordingNumber ](#ApiClient.RecordingInfo.GetRecordingNumber)
  - [M GetRecordingType ](#ApiClient.RecordingInfo.GetRecordingType)
  - [M GetStartTime ](#ApiClient.RecordingInfo.GetStartTime)
  - [M GetStopTime ](#ApiClient.RecordingInfo.GetStopTime)
  - [M GetSyncDeltaT ](#ApiClient.RecordingInfo.GetSyncDeltaT)
  - [M SetFormatDetailsString ](#ApiClient.RecordingInfo.SetFormatDetailsString)
  - [M SetSyncDeltaT ](#ApiClient.RecordingInfo.SetSyncDeltaT)

[ SignalGroup ](SignalGroup.md)

[ SignalGroupBase ](SignalGroupBase.md)

[ VariableRecordingGroup ](VariableRecordingGroup.md)

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

RecordingInfo

- [C RecordingInfo ](#ApiClient.RecordingInfo)
  - [M Clone ](#ApiClient.RecordingInfo.Clone)
  - [M DeleteFormatDetails ](#ApiClient.RecordingInfo.DeleteFormatDetails)
  - [M GetFormatDetailsString ](#ApiClient.RecordingInfo.GetFormatDetailsString)
  - [M GetPath ](#ApiClient.RecordingInfo.GetPath)
  - [M GetPathList ](#ApiClient.RecordingInfo.GetPathList)
  - [M GetRecordingName ](#ApiClient.RecordingInfo.GetRecordingName)
  - [M GetRecordingNumber ](#ApiClient.RecordingInfo.GetRecordingNumber)
  - [M GetRecordingType ](#ApiClient.RecordingInfo.GetRecordingType)
  - [M GetStartTime ](#ApiClient.RecordingInfo.GetStartTime)
  - [M GetStopTime ](#ApiClient.RecordingInfo.GetStopTime)
  - [M GetSyncDeltaT ](#ApiClient.RecordingInfo.GetSyncDeltaT)
  - [M SetFormatDetailsString ](#ApiClient.RecordingInfo.SetFormatDetailsString)
  - [M SetSyncDeltaT ](#ApiClient.RecordingInfo.SetSyncDeltaT)

# RecordingInfo[¶](#recordinginfo "Link to this heading")

*class* RecordingInfo[¶](#ApiClient.RecordingInfo "Link to this definition")  
Returned by

- [`SignalRecordingApi.CreateRecordingInfo`](../SignalRecordingApi.md#ApiClient.SignalRecordingApi.CreateRecordingInfo "ApiClient.SignalRecordingApi.CreateRecordingInfo (Python method) — Creates a recording info.")

Clone()[¶](#ApiClient.RecordingInfo.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`RecordingInfo`](#ApiClient.RecordingInfo "ApiClient.RecordingInfo (Python class) — SignalRecordingApi.CreateRecordingInfo")

DeleteFormatDetails()[¶](#ApiClient.RecordingInfo.DeleteFormatDetails "Link to this definition")  
Deletes the format details of the existing recording.

GetFormatDetailsString()[¶](#ApiClient.RecordingInfo.GetFormatDetailsString "Link to this definition")  
Returns the recording type specific format details as string.

Returns:  The format details as string, None if there aren’t any format details

Return type:  str

GetPath()[¶](#ApiClient.RecordingInfo.GetPath "Link to this definition")  
Returns the path (or the first path if there is a list of paths) for the recording.

Returns:  The path

Return type:  str

GetPathList()[¶](#ApiClient.RecordingInfo.GetPathList "Link to this definition")  
Returns the list of paths of the recording as a sequence of multiple files.

Returns:  The list of paths

Return type:  list[str]

GetRecordingName()[¶](#ApiClient.RecordingInfo.GetRecordingName "Link to this definition")  
Returns the name of the recording.

Returns:  The name

Return type:  str

GetRecordingNumber()[¶](#ApiClient.RecordingInfo.GetRecordingNumber "Link to this definition")  
Returns the recording number.

Returns:  The recording number

Return type:  int

GetRecordingType()[¶](#ApiClient.RecordingInfo.GetRecordingType "Link to this definition")  
Returns the recording type as string.

Returns:  The recording type, e.g. ‘CSV’, ‘MDF_VECTOR’

Return type:  str

GetStartTime()[¶](#ApiClient.RecordingInfo.GetStartTime "Link to this definition")  
Returns the first time stamp to be read in from the recording.

Raises:  
**ApiError** – Underlying data value can not be returned as float.

Returns:  First time stamp to be read in from the recording

Return type:  float

GetStopTime()[¶](#ApiClient.RecordingInfo.GetStopTime "Link to this definition")  
Returns the last time stamp to be read in from the recording.

Raises:  
**ApiError** – Underlying data value can not be returned as float.

Returns:  Last time stamp to be read in from the recording

Return type:  float

GetSyncDeltaT()[¶](#ApiClient.RecordingInfo.GetSyncDeltaT "Link to this definition")  
Get the time axis shift determined by the synchronization.

Note:  
Only use in the context of a analysis job.

Returns:  Shift of time axis determined by the synchronization or None, when no synchronization information exists.

Return type:  float

SetFormatDetailsString(*[formatDetails](#ApiClient.RecordingInfo.SetFormatDetailsString.formatDetails "ApiClient.RecordingInfo.SetFormatDetailsString.formatDetails (Python parameter) — Format details of the recording.")*)[¶](#ApiClient.RecordingInfo.SetFormatDetailsString "Link to this definition")  
Sets the format details of the existing recording. If the file of this recording info exists, it will be checked whether the format details string is supported.

Parameters:  formatDetails : str[¶](#ApiClient.RecordingInfo.SetFormatDetailsString.formatDetails "Permalink to this definition")  
Format details of the recording.

SetSyncDeltaT(*[deltaT](#ApiClient.RecordingInfo.SetSyncDeltaT.deltaT "ApiClient.RecordingInfo.SetSyncDeltaT.deltaT (Python parameter) — Shift of time axis determined by the synchronization or None, when no synchronization information exists.")*)[¶](#ApiClient.RecordingInfo.SetSyncDeltaT "Link to this definition")  
Set the time axis shift determined by the synchronization.

Note:  
Only use in the context of a analysis job. Synchronization is ignored when this information is set.

Parameters:  deltaT : float[¶](#ApiClient.RecordingInfo.SetSyncDeltaT.deltaT "Permalink to this definition")  
Shift of time axis determined by the synchronization or None, when no synchronization information exists.

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
