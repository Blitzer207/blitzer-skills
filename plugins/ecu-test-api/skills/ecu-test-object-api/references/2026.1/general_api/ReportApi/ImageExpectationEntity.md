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

ImageExpectationEntity [ ImageExpectationEntity ](#)

ImageExpectationEntity

- [C ImageExpectationEntity ](#ApiClient.ImageExpectationEntity)
  - [M Clone ](#ApiClient.ImageExpectationEntity.Clone)
  - [M GetActualImage ](#ApiClient.ImageExpectationEntity.GetActualImage)
  - [M GetExpectedImage ](#ApiClient.ImageExpectationEntity.GetExpectedImage)
  - [M GetType ](#ApiClient.ImageExpectationEntity.GetType)

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

ImageExpectationEntity

- [C ImageExpectationEntity ](#ApiClient.ImageExpectationEntity)
  - [M Clone ](#ApiClient.ImageExpectationEntity.Clone)
  - [M GetActualImage ](#ApiClient.ImageExpectationEntity.GetActualImage)
  - [M GetExpectedImage ](#ApiClient.ImageExpectationEntity.GetExpectedImage)
  - [M GetType ](#ApiClient.ImageExpectationEntity.GetType)

# ImageExpectationEntity[¶](#imageexpectationentity "Link to this heading")

*class* ImageExpectationEntity[¶](#ApiClient.ImageExpectationEntity "Link to this definition")  
This type semantically clusters two images belonging to the same image expectation. This type is used for example when reporting the expected and resulting image of an read-image test step.

Clone()[¶](#ApiClient.ImageExpectationEntity.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`ImageExpectationEntity`](#ApiClient.ImageExpectationEntity "ApiClient.ImageExpectationEntity (Python class) — This type semantically clusters two images belonging to the same image expectation. This type is used for example when reporting the expected and resulting image of an read-image test step.")

GetActualImage()[¶](#ApiClient.ImageExpectationEntity.GetActualImage "Link to this definition")  
Returns the actual image (the resulting image)

Returns:  the actual image

Return type:  [`ReportImage`](ReportImage.md#ApiClient.ReportImage "ApiClient.ReportImage (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")

GetExpectedImage()[¶](#ApiClient.ImageExpectationEntity.GetExpectedImage "Link to this definition")  
Returns the expected image

Returns:  the expected image

Return type:  [`ReportImage`](ReportImage.md#ApiClient.ReportImage "ApiClient.ReportImage (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")

GetType()[¶](#ApiClient.ImageExpectationEntity.GetType "Link to this definition")  
Returns the type name of the entity.

Returns:  “ImageExpectation”

Return type:  str

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
