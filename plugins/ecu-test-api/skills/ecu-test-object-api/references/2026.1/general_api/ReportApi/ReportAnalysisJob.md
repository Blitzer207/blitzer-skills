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

ReportAnalysisJob [ ReportAnalysisJob ](#)

ReportAnalysisJob

- [C ReportAnalysisJob ](#ApiClient.ReportAnalysisJob)
  - [M Clone ](#ApiClient.ReportAnalysisJob.Clone)
  - [M ExportAnalysisJob ](#ApiClient.ReportAnalysisJob.ExportAnalysisJob)
  - [M GetAllEpisodes ](#ApiClient.ReportAnalysisJob.GetAllEpisodes)
  - [M GetDuration ](#ApiClient.ReportAnalysisJob.GetDuration)
  - [M GetName ](#ApiClient.ReportAnalysisJob.GetName)
  - [M GetOriginalResult ](#ApiClient.ReportAnalysisJob.GetOriginalResult)
  - [M GetRecordingInfos ](#ApiClient.ReportAnalysisJob.GetRecordingInfos)
  - [M GetResult ](#ApiClient.ReportAnalysisJob.GetResult)
  - [M GetStimulationPackage ](#ApiClient.ReportAnalysisJob.GetStimulationPackage)
  - [M GetTraceAnalysis ](#ApiClient.ReportAnalysisJob.GetTraceAnalysis)
  - [M GetTraceSteps ](#ApiClient.ReportAnalysisJob.GetTraceSteps)
  - [M IsDownstream ](#ApiClient.ReportAnalysisJob.IsDownstream)

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

[ ReportRecordingInfo ](ReportRecordingInfo.md)

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

ReportAnalysisJob

- [C ReportAnalysisJob ](#ApiClient.ReportAnalysisJob)
  - [M Clone ](#ApiClient.ReportAnalysisJob.Clone)
  - [M ExportAnalysisJob ](#ApiClient.ReportAnalysisJob.ExportAnalysisJob)
  - [M GetAllEpisodes ](#ApiClient.ReportAnalysisJob.GetAllEpisodes)
  - [M GetDuration ](#ApiClient.ReportAnalysisJob.GetDuration)
  - [M GetName ](#ApiClient.ReportAnalysisJob.GetName)
  - [M GetOriginalResult ](#ApiClient.ReportAnalysisJob.GetOriginalResult)
  - [M GetRecordingInfos ](#ApiClient.ReportAnalysisJob.GetRecordingInfos)
  - [M GetResult ](#ApiClient.ReportAnalysisJob.GetResult)
  - [M GetStimulationPackage ](#ApiClient.ReportAnalysisJob.GetStimulationPackage)
  - [M GetTraceAnalysis ](#ApiClient.ReportAnalysisJob.GetTraceAnalysis)
  - [M GetTraceSteps ](#ApiClient.ReportAnalysisJob.GetTraceSteps)
  - [M IsDownstream ](#ApiClient.ReportAnalysisJob.IsDownstream)

# ReportAnalysisJob[¶](#reportanalysisjob "Link to this heading")

*class* ReportAnalysisJob[¶](#ApiClient.ReportAnalysisJob "Link to this definition")  
Clone()[¶](#ApiClient.ReportAnalysisJob.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`ReportAnalysisJob`](#ApiClient.ReportAnalysisJob "ApiClient.ReportAnalysisJob (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")

ExportAnalysisJob(*[path](#ApiClient.ReportAnalysisJob.ExportAnalysisJob.path "ApiClient.ReportAnalysisJob.ExportAnalysisJob.path (Python parameter) — Path where ajob-file is written to.")*)[¶](#ApiClient.ReportAnalysisJob.ExportAnalysisJob "Link to this definition")  
Writes deposited analysis job as an ajob-file for downstream analysis.

Parameters:  path : str[¶](#ApiClient.ReportAnalysisJob.ExportAnalysisJob.path "Permalink to this definition")  
Path where ajob-file is written to. Must include the file extension “.ajob”.

GetAllEpisodes()[¶](#ApiClient.ReportAnalysisJob.GetAllEpisodes "Link to this definition")  
Returns all episodes of the analysis job regardless of the position in the report.

Returns:  List of trace step results

Return type:  list[[`ReportAnalysisEpisode`](ReportAnalysisEpisode.md#ApiClient.ReportAnalysisEpisode "ApiClient.ReportAnalysisEpisode (Python class) — Add a revaluation comment to the test step.")]

GetDuration()[¶](#ApiClient.ReportAnalysisJob.GetDuration "Link to this definition")  
Returns the execution duration.

Returns:  Execution duration in seconds

Return type:  float

GetName()[¶](#ApiClient.ReportAnalysisJob.GetName "Link to this definition")  
Returns the name of the analysis job.

Returns:  name of the analysis job

Return type:  str

GetOriginalResult()[¶](#ApiClient.ReportAnalysisJob.GetOriginalResult "Link to this definition")  
Returns the result verdict of the analysis job.

Returns:  the result verdict

Return type:  str

GetRecordingInfos()[¶](#ApiClient.ReportAnalysisJob.GetRecordingInfos "Link to this definition")  
Returns an object encapsulating the recording info of the analysis job.

Returns:  The recording info table

Return type:  list[[`ReportRecordingInfo`](ReportRecordingInfo.md#ApiClient.ReportRecordingInfo "ApiClient.ReportRecordingInfo (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")]

GetResult()[¶](#ApiClient.ReportAnalysisJob.GetResult "Link to this definition")  
Returns the result verdict of the analysis job.

Returns:  the result verdict

Return type:  str

GetStimulationPackage()[¶](#ApiClient.ReportAnalysisJob.GetStimulationPackage "Link to this definition")  
This call is only valid for analysis jobs derived from analysis packages and returns the invoked stimulation package. For parameterized stimulations, the resulting package object characterizes a particular parameter set.

Returns:  stimulation package

Return type:  [`ReportPackage`](ReportPackage.md#ApiClient.ReportPackage "ApiClient.ReportPackage (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")

GetTraceAnalysis()[¶](#ApiClient.ReportAnalysisJob.GetTraceAnalysis "Link to this definition")  
Returns the root element ‘trace analysis’ (report item) of the analysis job.

Returns:  Root element of job or None if trace analysis was not executed.

Return type:  [`ReportAnalysisStep`](ReportAnalysisStep.md#ApiClient.ReportAnalysisStep "ApiClient.ReportAnalysisStep (Python class) — Add a revaluation comment to the test step.")

GetTraceSteps(*[recursive](#ApiClient.ReportAnalysisJob.GetTraceSteps.recursive "ApiClient.ReportAnalysisJob.GetTraceSteps.recursive (Python parameter) — Defines whether children of children are included, defaults to False.")=`False`*)[¶](#ApiClient.ReportAnalysisJob.GetTraceSteps "Link to this definition")  
Returns direct/all children trace steps of the trace analysis.

Parameters:  recursive : boolean[¶](#ApiClient.ReportAnalysisJob.GetTraceSteps.recursive "Permalink to this definition")  
Defines whether children of children are included, defaults to False.

Returns:  List of trace step results. If the analysis has not been executed, an empty list will be returned.

Return type:  list[[`ReportAnalysisStep`](ReportAnalysisStep.md#ApiClient.ReportAnalysisStep "ApiClient.ReportAnalysisStep (Python class) — Add a revaluation comment to the test step.")]

IsDownstream()[¶](#ApiClient.ReportAnalysisJob.IsDownstream "Link to this definition")  
Returns whether the analysis job was created as a downstream analysis. If so, it was not processed within the project execution. Instead, is has to be executed afterwards.

Note:  
A downstream analysis has the default result NONE instead of INCONCLUSIVE.

Returns:  True, if the analysis job was created as downstream analysis.

Return type:  bool

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
