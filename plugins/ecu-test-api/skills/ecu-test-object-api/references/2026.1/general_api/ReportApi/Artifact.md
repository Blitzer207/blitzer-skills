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

Artifact [ Artifact ](#)

Artifact

- [C Artifact ](#ApiClient.Artifact)
  - [M Clone ](#ApiClient.Artifact.Clone)
  - [M GetContext ](#ApiClient.Artifact.GetContext)
  - [M GetFileHash ](#ApiClient.Artifact.GetFileHash)
  - [M GetFileName ](#ApiClient.Artifact.GetFileName)
  - [M GetFilePath ](#ApiClient.Artifact.GetFilePath)
  - [M GetMainPackageReportItemId ](#ApiClient.Artifact.GetMainPackageReportItemId)

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

Artifact

- [C Artifact ](#ApiClient.Artifact)
  - [M Clone ](#ApiClient.Artifact.Clone)
  - [M GetContext ](#ApiClient.Artifact.GetContext)
  - [M GetFileHash ](#ApiClient.Artifact.GetFileHash)
  - [M GetFileName ](#ApiClient.Artifact.GetFileName)
  - [M GetFilePath ](#ApiClient.Artifact.GetFilePath)
  - [M GetMainPackageReportItemId ](#ApiClient.Artifact.GetMainPackageReportItemId)

# Artifact[¶](#artifact "Link to this heading")

*class* Artifact[¶](#ApiClient.Artifact "Link to this definition")  
Clone()[¶](#ApiClient.Artifact.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`Artifact`](#ApiClient.Artifact "ApiClient.Artifact (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")

GetContext()[¶](#ApiClient.Artifact.GetContext "Link to this definition")  
Returns the artifact’s context.

Returns:  the artifact’s context

Return type:  str

GetFileHash()[¶](#ApiClient.Artifact.GetFileHash "Link to this definition")  
Returns the md5 hashsum if the file was stored on local file system.

Returns:  the md5 hashsum or empty string

Return type:  str

GetFileName()[¶](#ApiClient.Artifact.GetFileName "Link to this definition")  
Returns the name of the artifact.

Returns:  the artifact’s file name

Return type:  str

GetFilePath()[¶](#ApiClient.Artifact.GetFilePath "Link to this definition")  
Returns the path to the artifact. This can be a path on the local file system or an url.

Returns:  the file path

Return type:  str

GetMainPackageReportItemId()[¶](#ApiClient.Artifact.GetMainPackageReportItemId "Link to this definition")  
Returns the report item Id of the main package where the artifact was created.

Returns:  the report item Id of the main package

Return type:  int

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
