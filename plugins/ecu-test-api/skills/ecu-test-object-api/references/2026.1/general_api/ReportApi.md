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

[ API for Analysis Jobs ](AnalysisJobApi.md)

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

[ API for Reports ](#)

API for Reports

- [ Artifact ](ReportApi/Artifact.md)
- [ Entity ](ReportApi/Entity.md)
- [ GlobalConstant ](ReportApi/GlobalConstant.md)
- [ ImageEntity ](ReportApi/ImageEntity.md)
- [ ImageExpectationEntity ](ReportApi/ImageExpectationEntity.md)
- [ Report ](ReportApi/Report.md)
- [ ReportAnalysisEpisode ](ReportApi/ReportAnalysisEpisode.md)
- [ ReportAnalysisJob ](ReportApi/ReportAnalysisJob.md)
- [ ReportAnalysisStep ](ReportApi/ReportAnalysisStep.md)
- [ ReportConfigurationChange ](ReportApi/ReportConfigurationChange.md)
- [ ReportFolderElement ](ReportApi/ReportFolderElement.md)
- [ ReportImage ](ReportApi/ReportImage.md)
- [ ReportPackage ](ReportApi/ReportPackage.md)
- [ ReportParameterSet ](ReportApi/ReportParameterSet.md)
- [ ReportParameterizedPackage ](ReportApi/ReportParameterizedPackage.md)
- [ ReportProject ](ReportApi/ReportProject.md)
- [ ReportProjectElement ](ReportApi/ReportProjectElement.md)
- [ ReportRecording ](ReportApi/ReportRecording.md)
- [ ReportRecordingInfo ](ReportApi/ReportRecordingInfo.md)
- [ ReportTestCase ](ReportApi/ReportTestCase.md)
- [ ReportTestStep ](ReportApi/ReportTestStep.md)
- [ RevaluationComment ](ReportApi/RevaluationComment.md)
- [ TableEntity ](ReportApi/TableEntity.md)
- [ TextEntity ](ReportApi/TextEntity.md)

API for Reports [ API for Reports ](#)

API for Reports

- [C ReportApi ](#ApiClient.ReportApi)
  - [M OpenReport ](#ApiClient.ReportApi.OpenReport)
- [ Artifact ](ReportApi/Artifact.md)
- [ Entity ](ReportApi/Entity.md)
- [ GlobalConstant ](ReportApi/GlobalConstant.md)
- [ ImageEntity ](ReportApi/ImageEntity.md)
- [ ImageExpectationEntity ](ReportApi/ImageExpectationEntity.md)
- [ Report ](ReportApi/Report.md)
- [ ReportAnalysisEpisode ](ReportApi/ReportAnalysisEpisode.md)
- [ ReportAnalysisJob ](ReportApi/ReportAnalysisJob.md)
- [ ReportAnalysisStep ](ReportApi/ReportAnalysisStep.md)
- [ ReportConfigurationChange ](ReportApi/ReportConfigurationChange.md)
- [ ReportFolderElement ](ReportApi/ReportFolderElement.md)
- [ ReportImage ](ReportApi/ReportImage.md)
- [ ReportPackage ](ReportApi/ReportPackage.md)
- [ ReportParameterSet ](ReportApi/ReportParameterSet.md)
- [ ReportParameterizedPackage ](ReportApi/ReportParameterizedPackage.md)
- [ ReportProject ](ReportApi/ReportProject.md)
- [ ReportProjectElement ](ReportApi/ReportProjectElement.md)
- [ ReportRecording ](ReportApi/ReportRecording.md)
- [ ReportRecordingInfo ](ReportApi/ReportRecordingInfo.md)
- [ ReportTestCase ](ReportApi/ReportTestCase.md)
- [ ReportTestStep ](ReportApi/ReportTestStep.md)
- [ RevaluationComment ](ReportApi/RevaluationComment.md)
- [ TableEntity ](ReportApi/TableEntity.md)
- [ TextEntity ](ReportApi/TextEntity.md)

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

API for Reports

- [C ReportApi ](#ApiClient.ReportApi)
  - [M OpenReport ](#ApiClient.ReportApi.OpenReport)

# API for Reports[¶](#api-for-reports "Link to this heading")

Part of the [Object based program API](objectApi.md#objectapi).

*class* ReportApi[¶](#ApiClient.ReportApi "Link to this definition")  
API to access test reports

Returned by

- [`ApiClient.ReportApi`](objectApi.md#ApiClient.ApiClient.ReportApi "ApiClient.ApiClient.ReportApi (Python attribute) — Returns the ReportApi namespace.")

OpenReport(*[filename](#ApiClient.ReportApi.OpenReport.filename "ApiClient.ReportApi.OpenReport.filename (Python parameter) — Filename of the report file as absolute path")*)[¶](#ApiClient.ReportApi.OpenReport "Link to this definition")  
Opens the referenced report file.

Parameters:  filename : str[¶](#ApiClient.ReportApi.OpenReport.filename "Permalink to this definition")  
Filename of the report file as absolute path

Return type:  [`Report`](ReportApi/Report.md#ApiClient.Report "ApiClient.Report (Python class) — ReportApi.OpenReport")

Returns:  The report

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
