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

Report [ Report ](#)

Report

- [C Report ](#ApiClient.Report)
  - [M Clone ](#ApiClient.Report.Clone)
  - [M Close ](#ApiClient.Report.Close)
  - [M GetArtifacts ](#ApiClient.Report.GetArtifacts)
  - [M GetAuthor ](#ApiClient.Report.GetAuthor)
  - [M GetDuration ](#ApiClient.Report.GetDuration)
  - [M GetExecutionTime ](#ApiClient.Report.GetExecutionTime)
  - [M GetKeywordCatalog ](#ApiClient.Report.GetKeywordCatalog)
  - [M GetMainProject ](#ApiClient.Report.GetMainProject)
  - [M GetProjectExecutionPath ](#ApiClient.Report.GetProjectExecutionPath)
  - [M GetProjectName ](#ApiClient.Report.GetProjectName)
  - [M GetResult ](#ApiClient.Report.GetResult)
  - [M GetTestManagementId ](#ApiClient.Report.GetTestManagementId)
  - [M GetTeststand ](#ApiClient.Report.GetTeststand)
  - [M GetTimeZoneUTCOffset ](#ApiClient.Report.GetTimeZoneUTCOffset)
  - [M GetTopLevelPackages ](#ApiClient.Report.GetTopLevelPackages)
  - [M GetVersion ](#ApiClient.Report.GetVersion)
  - [M IsProjectReport ](#ApiClient.Report.IsProjectReport)

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

Report

- [C Report ](#ApiClient.Report)
  - [M Clone ](#ApiClient.Report.Clone)
  - [M Close ](#ApiClient.Report.Close)
  - [M GetArtifacts ](#ApiClient.Report.GetArtifacts)
  - [M GetAuthor ](#ApiClient.Report.GetAuthor)
  - [M GetDuration ](#ApiClient.Report.GetDuration)
  - [M GetExecutionTime ](#ApiClient.Report.GetExecutionTime)
  - [M GetKeywordCatalog ](#ApiClient.Report.GetKeywordCatalog)
  - [M GetMainProject ](#ApiClient.Report.GetMainProject)
  - [M GetProjectExecutionPath ](#ApiClient.Report.GetProjectExecutionPath)
  - [M GetProjectName ](#ApiClient.Report.GetProjectName)
  - [M GetResult ](#ApiClient.Report.GetResult)
  - [M GetTestManagementId ](#ApiClient.Report.GetTestManagementId)
  - [M GetTeststand ](#ApiClient.Report.GetTeststand)
  - [M GetTimeZoneUTCOffset ](#ApiClient.Report.GetTimeZoneUTCOffset)
  - [M GetTopLevelPackages ](#ApiClient.Report.GetTopLevelPackages)
  - [M GetVersion ](#ApiClient.Report.GetVersion)
  - [M IsProjectReport ](#ApiClient.Report.IsProjectReport)

# Report[¶](#report "Link to this heading")

*class* Report[¶](#ApiClient.Report "Link to this definition")  
Returned by

- [`ReportApi.OpenReport`](../ReportApi.md#ApiClient.ReportApi.OpenReport "ApiClient.ReportApi.OpenReport (Python method) — Opens the referenced report file.")

Clone()[¶](#ApiClient.Report.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`Report`](#ApiClient.Report "ApiClient.Report (Python class) — ReportApi.OpenReport")

Close()[¶](#ApiClient.Report.Close "Link to this definition")  
Closes the report. After closing the report it can not be modified/accessed anymore.

GetArtifacts()[¶](#ApiClient.Report.GetArtifacts "Link to this definition")  
Returns all artifacts that are referenced by any package in the report.

Returns:  A list of all artifacts.

Return type:  list[[`Artifact`](Artifact.md#ApiClient.Artifact "ApiClient.Artifact (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")]

GetAuthor()[¶](#ApiClient.Report.GetAuthor "Link to this definition")  
Returns the test author.

Returns:  Test author

Return type:  str

GetDuration()[¶](#ApiClient.Report.GetDuration "Link to this definition")  
Returns the duration of the test execution.

Returns:  Execution duration in seconds

Return type:  float

GetExecutionTime()[¶](#ApiClient.Report.GetExecutionTime "Link to this definition")  
Returns the test execution date and time as string representation.

Returns:  Test execution date and time

Return type:  str

GetKeywordCatalog()[¶](#ApiClient.Report.GetKeywordCatalog "Link to this definition")  
Returns the name of the keyword catalog used during test execution.

Returns:  The catalog name or an empty string if no catalog was present at test execution.

Return type:  str

GetMainProject()[¶](#ApiClient.Report.GetMainProject "Link to this definition")  
Returns the main project. Raises an ApiError if the report is not the result of a project execution.

Returns:  List of direct project sub components

Return type:  [`ReportProject`](ReportProject.md#ApiClient.ReportProject "ApiClient.ReportProject (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")

GetProjectExecutionPath()[¶](#ApiClient.Report.GetProjectExecutionPath "Link to this definition")  
Returns the execution path in relation to the calling project if executed as separate subproject or the name of the project, if not not executed separately.

Returns:  Path in the project execution stack

Return type:  str

GetProjectName()[¶](#ApiClient.Report.GetProjectName "Link to this definition")  
Returns the name of the root project if it is a project report, otherwise empty string.

Returns:  Name of the project

Return type:  str

GetResult()[¶](#ApiClient.Report.GetResult "Link to this definition")  
Returns the total test result.

Returns:  Total test result

Return type:  str

GetTestManagementId()[¶](#ApiClient.Report.GetTestManagementId "Link to this definition")  
Returns the corresponding testmanagement Id of the root level project.

Returns:  Testmanagement Id or an empty string if no Id defined. If no project was executed None will be returned.

Return type:  str

GetTeststand()[¶](#ApiClient.Report.GetTeststand "Link to this definition")  
Returns the computer name where the test was executed.

Returns:  Name of the computer

Return type:  str

GetTimeZoneUTCOffset()[¶](#ApiClient.Report.GetTimeZoneUTCOffset "Link to this definition")  
Returns the offset from UTC in seconds based on the time zone in which the test report was generated. If no time zone is set in the report, None will be returned.

Returns:  Offset from UTC in seconds, or None

Return type:  int

GetTopLevelPackages()[¶](#ApiClient.Report.GetTopLevelPackages "Link to this definition")  
Convenience method for the testmanagement synchronization.

On a package report one package report will be returned. On a project report all package reports will be returned in a flat list regardless of directories. Packages of sub projects will be ignored.

Returns:  List of package objects

Return type:  list[[`ReportPackage`](ReportPackage.md#ApiClient.ReportPackage "ApiClient.ReportPackage (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")]

GetVersion()[¶](#ApiClient.Report.GetVersion "Link to this definition")  
Returns the ecu.test Version which created this report.

Returns:  Version of ecu.test

Return type:  str

IsProjectReport()[¶](#ApiClient.Report.IsProjectReport "Link to this definition")  
Checks if the report is from a project execution or not.

Returns:  True if the report is the result of a project execution, otherwise False

Return type:  bool

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
