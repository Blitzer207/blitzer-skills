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

ReportAnalysisEpisode [ ReportAnalysisEpisode ](#)

ReportAnalysisEpisode

- [C ReportAnalysisEpisode ](#ApiClient.ReportAnalysisEpisode)
  - [M AddRevalComment ](#ApiClient.ReportAnalysisEpisode.AddRevalComment)
  - [M Clone ](#ApiClient.ReportAnalysisEpisode.Clone)
  - [M GetAbortCode ](#ApiClient.ReportAnalysisEpisode.GetAbortCode)
  - [M GetAbortComment ](#ApiClient.ReportAnalysisEpisode.GetAbortComment)
  - [M GetActivity ](#ApiClient.ReportAnalysisEpisode.GetActivity)
  - [M GetDescription ](#ApiClient.ReportAnalysisEpisode.GetDescription)
  - [M GetDuration ](#ApiClient.ReportAnalysisEpisode.GetDuration)
  - [M GetEntities ](#ApiClient.ReportAnalysisEpisode.GetEntities)
  - [M GetErrorMessage ](#ApiClient.ReportAnalysisEpisode.GetErrorMessage)
  - [M GetId ](#ApiClient.ReportAnalysisEpisode.GetId)
  - [M GetLabel ](#ApiClient.ReportAnalysisEpisode.GetLabel)
  - [M GetName ](#ApiClient.ReportAnalysisEpisode.GetName)
  - [M GetNestingLevel ](#ApiClient.ReportAnalysisEpisode.GetNestingLevel)
  - [M GetOriginalResult ](#ApiClient.ReportAnalysisEpisode.GetOriginalResult)
  - [M GetParameter ](#ApiClient.ReportAnalysisEpisode.GetParameter)
  - [M GetParentId ](#ApiClient.ReportAnalysisEpisode.GetParentId)
  - [M GetPosition ](#ApiClient.ReportAnalysisEpisode.GetPosition)
  - [M GetResult ](#ApiClient.ReportAnalysisEpisode.GetResult)
  - [M GetResultText ](#ApiClient.ReportAnalysisEpisode.GetResultText)
  - [M GetRevalComments ](#ApiClient.ReportAnalysisEpisode.GetRevalComments)
  - [M GetTags ](#ApiClient.ReportAnalysisEpisode.GetTags)
  - [M GetTextEntities ](#ApiClient.ReportAnalysisEpisode.GetTextEntities)
  - [M GetTraceSteps ](#ApiClient.ReportAnalysisEpisode.GetTraceSteps)
  - [M HasTag ](#ApiClient.ReportAnalysisEpisode.HasTag)
  - [M IsTemplateBasedTraceStep ](#ApiClient.ReportAnalysisEpisode.IsTemplateBasedTraceStep)

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

ReportAnalysisEpisode

- [C ReportAnalysisEpisode ](#ApiClient.ReportAnalysisEpisode)
  - [M AddRevalComment ](#ApiClient.ReportAnalysisEpisode.AddRevalComment)
  - [M Clone ](#ApiClient.ReportAnalysisEpisode.Clone)
  - [M GetAbortCode ](#ApiClient.ReportAnalysisEpisode.GetAbortCode)
  - [M GetAbortComment ](#ApiClient.ReportAnalysisEpisode.GetAbortComment)
  - [M GetActivity ](#ApiClient.ReportAnalysisEpisode.GetActivity)
  - [M GetDescription ](#ApiClient.ReportAnalysisEpisode.GetDescription)
  - [M GetDuration ](#ApiClient.ReportAnalysisEpisode.GetDuration)
  - [M GetEntities ](#ApiClient.ReportAnalysisEpisode.GetEntities)
  - [M GetErrorMessage ](#ApiClient.ReportAnalysisEpisode.GetErrorMessage)
  - [M GetId ](#ApiClient.ReportAnalysisEpisode.GetId)
  - [M GetLabel ](#ApiClient.ReportAnalysisEpisode.GetLabel)
  - [M GetName ](#ApiClient.ReportAnalysisEpisode.GetName)
  - [M GetNestingLevel ](#ApiClient.ReportAnalysisEpisode.GetNestingLevel)
  - [M GetOriginalResult ](#ApiClient.ReportAnalysisEpisode.GetOriginalResult)
  - [M GetParameter ](#ApiClient.ReportAnalysisEpisode.GetParameter)
  - [M GetParentId ](#ApiClient.ReportAnalysisEpisode.GetParentId)
  - [M GetPosition ](#ApiClient.ReportAnalysisEpisode.GetPosition)
  - [M GetResult ](#ApiClient.ReportAnalysisEpisode.GetResult)
  - [M GetResultText ](#ApiClient.ReportAnalysisEpisode.GetResultText)
  - [M GetRevalComments ](#ApiClient.ReportAnalysisEpisode.GetRevalComments)
  - [M GetTags ](#ApiClient.ReportAnalysisEpisode.GetTags)
  - [M GetTextEntities ](#ApiClient.ReportAnalysisEpisode.GetTextEntities)
  - [M GetTraceSteps ](#ApiClient.ReportAnalysisEpisode.GetTraceSteps)
  - [M HasTag ](#ApiClient.ReportAnalysisEpisode.HasTag)
  - [M IsTemplateBasedTraceStep ](#ApiClient.ReportAnalysisEpisode.IsTemplateBasedTraceStep)

# ReportAnalysisEpisode[¶](#reportanalysisepisode "Link to this heading")

*class* ReportAnalysisEpisode[¶](#ApiClient.ReportAnalysisEpisode "Link to this definition")  
AddRevalComment(*[author](#ApiClient.ReportAnalysisEpisode.AddRevalComment.author "ApiClient.ReportAnalysisEpisode.AddRevalComment.author (Python parameter) — author of the comment")*, *[comment](#ApiClient.ReportAnalysisEpisode.AddRevalComment.comment "ApiClient.ReportAnalysisEpisode.AddRevalComment.comment (Python parameter) — text of the comment.")*, *[revaluation](#ApiClient.ReportAnalysisEpisode.AddRevalComment.revaluation "ApiClient.ReportAnalysisEpisode.AddRevalComment.revaluation (Python parameter) — "NONE", "SUCCESS", "INCONCLUSIVE", "FAILED" or "ERROR"; None to just add a comment without changing the result")=`None`*)[¶](#ApiClient.ReportAnalysisEpisode.AddRevalComment "Link to this definition")  
Add a revaluation comment to the test step.

Parameters:  author : str[¶](#ApiClient.ReportAnalysisEpisode.AddRevalComment.author "Permalink to this definition")  
author of the comment

comment : str[¶](#ApiClient.ReportAnalysisEpisode.AddRevalComment.comment "Permalink to this definition")  
text of the comment. Must be at least 10 characters

revaluation : str[¶](#ApiClient.ReportAnalysisEpisode.AddRevalComment.revaluation "Permalink to this definition")  
“NONE”, “SUCCESS”, “INCONCLUSIVE”, “FAILED” or “ERROR”; None to just add a comment without changing the result

Clone()[¶](#ApiClient.ReportAnalysisEpisode.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`ReportAnalysisEpisode`](#ApiClient.ReportAnalysisEpisode "ApiClient.ReportAnalysisEpisode (Python class) — Add a revaluation comment to the test step.")

GetAbortCode()[¶](#ApiClient.ReportAnalysisEpisode.GetAbortCode "Link to this definition")  
Returns the abort code of the report item.

Returns:  Abort code

Return type:  str

GetAbortComment()[¶](#ApiClient.ReportAnalysisEpisode.GetAbortComment "Link to this definition")  
Returns the abort comment of the report item.

Returns:  Abort comment

Return type:  str

GetActivity()[¶](#ApiClient.ReportAnalysisEpisode.GetActivity "Link to this definition")  
Returns the content of the ‘Name’.

Returns:  Content of the Name column

Return type:  str

GetDescription()[¶](#ApiClient.ReportAnalysisEpisode.GetDescription "Link to this definition")  
Returns the content of the ‘Description’ column.

Returns:  Content of the ‘Description’ column

Return type:  str

GetDuration()[¶](#ApiClient.ReportAnalysisEpisode.GetDuration "Link to this definition")  
Returns the execution duration.

Returns:  Excecution duration in seconds

Return type:  float

GetEntities()[¶](#ApiClient.ReportAnalysisEpisode.GetEntities "Link to this definition")  
Returns a list of all entities.

Returns:  a list of all entity objects

Return type:  list[[`Entity`](Entity.md#ApiClient.Entity "ApiClient.Entity (Python class) — An entity is a set of information visible in the report details of a certain reportitem. Each test step, analysis step or project step has specific report details, that are written to the report one after another.")]

GetErrorMessage()[¶](#ApiClient.ReportAnalysisEpisode.GetErrorMessage "Link to this definition")  
Returns the episode’s error message.

Returns:  The error message if existing, else an empty string

Return type:  str

GetId()[¶](#ApiClient.ReportAnalysisEpisode.GetId "Link to this definition")  
Returns the Id of the report item.

Returns:  Id of the report item

Return type:  int

GetLabel()[¶](#ApiClient.ReportAnalysisEpisode.GetLabel "Link to this definition")  
Returns the content of the ‘Activity/Name’ column for test steps. Returns the content of the ‘Name’ column for trace steps.

Returns:  Content of the ‘Activity/Name’ column for test steps and content of the ‘Name’ column for trace steps

Return type:  str

GetName()[¶](#ApiClient.ReportAnalysisEpisode.GetName "Link to this definition")  
Returns the content of the ‘Generic signals’ column.

Returns:  Content of the ‘Generic signals’ column

Return type:  str

GetNestingLevel()[¶](#ApiClient.ReportAnalysisEpisode.GetNestingLevel "Link to this definition")  
Returns the nesting depth.

Returns:  Nesting depth

Return type:  int

GetOriginalResult()[¶](#ApiClient.ReportAnalysisEpisode.GetOriginalResult "Link to this definition")  
Returns the content of the ‘Original evaluation’ column.

Returns:  Content of the ‘Original evaluation’ column

Return type:  str

GetParameter()[¶](#ApiClient.ReportAnalysisEpisode.GetParameter "Link to this definition")  
Returns the content of the ‘Parameter’ column.

Returns:  Content of the ‘Parameter’ column

Return type:  str

GetParentId()[¶](#ApiClient.ReportAnalysisEpisode.GetParentId "Link to this definition")  
Returns the Id of the parent report item.

Returns:  Id of the parent report item

Return type:  int

GetPosition()[¶](#ApiClient.ReportAnalysisEpisode.GetPosition "Link to this definition")  
Returns the position of the step within the test case / trace analysis. Example 1: “3” is returned for the step which is at position 3 in the top level Package. Example 2: “5.13” is returned for the 13th step of the subpackage which is at position 5 in the top level Package.

Returns:  position within the test case / trace analysis

Return type:  str

GetResult()[¶](#ApiClient.ReportAnalysisEpisode.GetResult "Link to this definition")  
Returns the content of the ‘Evaluation’ column.

Returns:  Content of the ‘Evaluation’ column

Return type:  str

GetResultText()[¶](#ApiClient.ReportAnalysisEpisode.GetResultText "Link to this definition")  
Returns text illustrated in the trace step’s report details below ‘result’.

Returns:  The result text if existing, else an empty string

Return type:  str

GetRevalComments()[¶](#ApiClient.ReportAnalysisEpisode.GetRevalComments "Link to this definition")  
Returns all revaluation comments of the test step.

Returns:  List of revaluation comments

Return type:  list[[`RevaluationComment`](RevaluationComment.md#ApiClient.RevaluationComment "ApiClient.RevaluationComment (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")]

GetTags()[¶](#ApiClient.ReportAnalysisEpisode.GetTags "Link to this definition")  
Returns all tags associated with this report entry.

Returns:  Tags

Return type:  list[str]

GetTextEntities()[¶](#ApiClient.ReportAnalysisEpisode.GetTextEntities "Link to this definition")  
Returns all text entities associated with this report entry.

Returns:  text entities

Return type:  list[list[str]]

GetTraceSteps(*[recursive](#ApiClient.ReportAnalysisEpisode.GetTraceSteps.recursive "ApiClient.ReportAnalysisEpisode.GetTraceSteps.recursive (Python parameter) — Defines whether children of children are included, defaults to False.")=`False`*)[¶](#ApiClient.ReportAnalysisEpisode.GetTraceSteps "Link to this definition")  
Returns direct/all children trace steps of this step. If the trace step is no container an empty list will be returned.

Parameters:  recursive : boolean[¶](#ApiClient.ReportAnalysisEpisode.GetTraceSteps.recursive "Permalink to this definition")  
Defines whether children of children are included, defaults to False.

Returns:  List of trace steps

Return type:  list[[`ReportAnalysisStep`](ReportAnalysisStep.md#ApiClient.ReportAnalysisStep "ApiClient.ReportAnalysisStep (Python class) — Add a revaluation comment to the test step.")]

HasTag(*[tagName](#ApiClient.ReportAnalysisEpisode.HasTag.tagName "ApiClient.ReportAnalysisEpisode.HasTag.tagName (Python parameter) — The tag to check for")*)[¶](#ApiClient.ReportAnalysisEpisode.HasTag "Link to this definition")  
Returns whether this report item has set the specified tag.

Parameters:  tagName : str[¶](#ApiClient.ReportAnalysisEpisode.HasTag.tagName "Permalink to this definition")  
The tag to check for

Returns:  True, if the tag is set, otherwise False

Return type:  bool

IsTemplateBasedTraceStep()[¶](#ApiClient.ReportAnalysisEpisode.IsTemplateBasedTraceStep "Link to this definition")  
Returns whether the trace step is based on a template.

Returns:  True if trace step is based on a template

Return type:  bool

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
