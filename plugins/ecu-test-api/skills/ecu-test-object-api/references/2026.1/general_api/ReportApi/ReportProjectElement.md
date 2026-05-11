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

ReportProjectElement [ ReportProjectElement ](#)

ReportProjectElement

- [C ReportProjectElement ](#ApiClient.ReportProjectElement)
  - [M Clone ](#ApiClient.ReportProjectElement.Clone)
  - [M GetComment ](#ApiClient.ReportProjectElement.GetComment)
  - [M GetElementName ](#ApiClient.ReportProjectElement.GetElementName)
  - [M GetProjectElements ](#ApiClient.ReportProjectElement.GetProjectElements)
  - [M GetReportItemId ](#ApiClient.ReportProjectElement.GetReportItemId)
  - [M GetResult ](#ApiClient.ReportProjectElement.GetResult)
  - [M GetType ](#ApiClient.ReportProjectElement.GetType)

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

ReportProjectElement

- [C ReportProjectElement ](#ApiClient.ReportProjectElement)
  - [M Clone ](#ApiClient.ReportProjectElement.Clone)
  - [M GetComment ](#ApiClient.ReportProjectElement.GetComment)
  - [M GetElementName ](#ApiClient.ReportProjectElement.GetElementName)
  - [M GetProjectElements ](#ApiClient.ReportProjectElement.GetProjectElements)
  - [M GetReportItemId ](#ApiClient.ReportProjectElement.GetReportItemId)
  - [M GetResult ](#ApiClient.ReportProjectElement.GetResult)
  - [M GetType ](#ApiClient.ReportProjectElement.GetType)

# ReportProjectElement[¶](#reportprojectelement "Link to this heading")

*class* ReportProjectElement[¶](#ApiClient.ReportProjectElement "Link to this definition")  
Clone()[¶](#ApiClient.ReportProjectElement.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`ReportProjectElement`](#ApiClient.ReportProjectElement "ApiClient.ReportProjectElement (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")

GetComment()[¶](#ApiClient.ReportProjectElement.GetComment "Link to this definition")  
Returns the comment of the project element.

Returns:  Project element comment

Return type:  str

GetElementName()[¶](#ApiClient.ReportProjectElement.GetElementName "Link to this definition")  
Returns the name of the project element.

Returns:  Element name

Return type:  str

GetProjectElements()[¶](#ApiClient.ReportProjectElement.GetProjectElements "Link to this definition")  
Returns a list of all direct project child elements.

Returns:  List of direct project child elements

Return type:  list[[`ReportProjectElement`](#ApiClient.ReportProjectElement "ApiClient.ReportProjectElement (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")]

GetReportItemId()[¶](#ApiClient.ReportProjectElement.GetReportItemId "Link to this definition")  
Returns the ReportItem Id of the project element.

Returns:  ReportItem Id

Return type:  int

GetResult()[¶](#ApiClient.ReportProjectElement.GetResult "Link to this definition")  
Returns the result of the project element.

Returns:  Project element result

Return type:  str

GetType()[¶](#ApiClient.ReportProjectElement.GetType "Link to this definition")  
Returns the type (class name) of the project element, e.g.  
- “ReportConfigurationChange”

- “ReportFolderElement”

- “ReportPackage”

- “ReportParameterizedPackage”

- “ReportParameterSet”

- “ReportProjectElement”

- “ReportProject”

Returns:  Type (class name) of the test step

Return type:  str

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
