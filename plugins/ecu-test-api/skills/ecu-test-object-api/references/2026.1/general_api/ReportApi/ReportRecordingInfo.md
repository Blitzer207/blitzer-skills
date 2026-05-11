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

API for Reports

[ Artifact ](Artifact.md)

[ Entity ](Entity.md)

[ GlobalConstant ](GlobalConstant.md)

[ ImageEntity ](ImageEntity.md)

[ ImageExpectationEntity ](ImageExpectationEntity.md)

[ Report ](Report.md)

[ ReportAnalysisEpisode ](ReportAnalysisEpisode.md)

[ ReportAnalysisJob ](ReportAnalysisJob.md)

[ ReportAnalysisStep ](ReportAnalysisStep.md)

[ ReportConfigurationChange ](ReportConfigurationChange.md)

[ ReportFolderElement ](ReportFolderElement.md)

[ ReportImage ](ReportImage.md)

[ ReportPackage ](ReportPackage.md)

[ ReportParameterSet ](ReportParameterSet.md)

[ ReportParameterizedPackage ](ReportParameterizedPackage.md)

[ ReportProject ](ReportProject.md)

[ ReportProjectElement ](ReportProjectElement.md)

[ ReportRecording ](ReportRecording.md)

ReportRecordingInfo [ ReportRecordingInfo ](#)

ReportRecordingInfo

- [C ReportRecordingInfo ](#ApiClient.ReportRecordingInfo)
  - [M Clone ](#ApiClient.ReportRecordingInfo.Clone)
  - [M GetRecording ](#ApiClient.ReportRecordingInfo.GetRecording)
  - [M GetStartTime ](#ApiClient.ReportRecordingInfo.GetStartTime)
  - [M GetStopTime ](#ApiClient.ReportRecordingInfo.GetStopTime)
  - [M GetSyncDeltaT ](#ApiClient.ReportRecordingInfo.GetSyncDeltaT)

[ ReportTestCase ](ReportTestCase.md)

[ ReportTestStep ](ReportTestStep.md)

[ RevaluationComment ](RevaluationComment.md)

[ TableEntity ](TableEntity.md)

[ TextEntity ](TextEntity.md)

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

ReportRecordingInfo

- [C ReportRecordingInfo ](#ApiClient.ReportRecordingInfo)
  - [M Clone ](#ApiClient.ReportRecordingInfo.Clone)
  - [M GetRecording ](#ApiClient.ReportRecordingInfo.GetRecording)
  - [M GetStartTime ](#ApiClient.ReportRecordingInfo.GetStartTime)
  - [M GetStopTime ](#ApiClient.ReportRecordingInfo.GetStopTime)
  - [M GetSyncDeltaT ](#ApiClient.ReportRecordingInfo.GetSyncDeltaT)

# ReportRecordingInfo[¶](#reportrecordinginfo "Link to this heading")

*class* ReportRecordingInfo[¶](#ApiClient.ReportRecordingInfo "Link to this definition")  
Clone()[¶](#ApiClient.ReportRecordingInfo.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`ReportRecordingInfo`](#ApiClient.ReportRecordingInfo "ApiClient.ReportRecordingInfo (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")

GetRecording()[¶](#ApiClient.ReportRecordingInfo.GetRecording "Link to this definition")  
Returns the recording that is referenced by the recording info.

Returns:  The recording object

Return type:  [`ReportRecording`](ReportRecording.md#ApiClient.ReportRecording "ApiClient.ReportRecording (Python class) — The constant used to specify that the recording path is stored as absolute path.")

GetStartTime()[¶](#ApiClient.ReportRecordingInfo.GetStartTime "Link to this definition")  
Returns the first time stamp read in from the recording.

Returns:  First time stamp read in from the recording. Returns None if no start time was set.

Return type:  float

GetStopTime()[¶](#ApiClient.ReportRecordingInfo.GetStopTime "Link to this definition")  
Returns the last time stamp read in from the recording.

Returns:  Last time stamp read in from the recording. Returns None if no stop time was set.

Return type:  float

GetSyncDeltaT()[¶](#ApiClient.ReportRecordingInfo.GetSyncDeltaT "Link to this definition")  
Returns the time offset set by the synchronization of traces.

Returns:  The deltaT

Return type:  float

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
