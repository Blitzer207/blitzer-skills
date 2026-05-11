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

[ ReportRecordingInfo ](ReportRecordingInfo.md)

[ ReportTestCase ](ReportTestCase.md)

[ ReportTestStep ](ReportTestStep.md)

[ RevaluationComment ](RevaluationComment.md)

TableEntity [ TableEntity ](#)

TableEntity

- [C TableEntity ](#ApiClient.TableEntity)
  - [M Clone ](#ApiClient.TableEntity.Clone)
  - [M GetColumnCount ](#ApiClient.TableEntity.GetColumnCount)
  - [M GetHeaders ](#ApiClient.TableEntity.GetHeaders)
  - [M GetRowCount ](#ApiClient.TableEntity.GetRowCount)
  - [M GetType ](#ApiClient.TableEntity.GetType)
  - [M GetValue ](#ApiClient.TableEntity.GetValue)
  - [M GetValues ](#ApiClient.TableEntity.GetValues)

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

TableEntity

- [C TableEntity ](#ApiClient.TableEntity)
  - [M Clone ](#ApiClient.TableEntity.Clone)
  - [M GetColumnCount ](#ApiClient.TableEntity.GetColumnCount)
  - [M GetHeaders ](#ApiClient.TableEntity.GetHeaders)
  - [M GetRowCount ](#ApiClient.TableEntity.GetRowCount)
  - [M GetType ](#ApiClient.TableEntity.GetType)
  - [M GetValue ](#ApiClient.TableEntity.GetValue)
  - [M GetValues ](#ApiClient.TableEntity.GetValues)

# TableEntity[¶](#tableentity "Link to this heading")

*class* TableEntity[¶](#ApiClient.TableEntity "Link to this definition")  
Clone()[¶](#ApiClient.TableEntity.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`TableEntity`](#ApiClient.TableEntity "ApiClient.TableEntity (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")

GetColumnCount()[¶](#ApiClient.TableEntity.GetColumnCount "Link to this definition")  
Returns the number of columns.

Returns:  the column count

Return type:  int

GetHeaders()[¶](#ApiClient.TableEntity.GetHeaders "Link to this definition")  
Returns a list representing the header row.

Returns:  the header row

Return type:  list[str]

GetRowCount()[¶](#ApiClient.TableEntity.GetRowCount "Link to this definition")  
Returns the number of rows. (not including the header row)

Returns:  the row count (not including the header row)

Return type:  int

GetType()[¶](#ApiClient.TableEntity.GetType "Link to this definition")  
Returns the type name of the entity.

Returns:  “Table”

Return type:  str

GetValue(*[row](#ApiClient.TableEntity.GetValue.row "ApiClient.TableEntity.GetValue.row (Python parameter) — the index of the row (0-based)")*, *[column](#ApiClient.TableEntity.GetValue.column "ApiClient.TableEntity.GetValue.column (Python parameter) — the index of the column (0-based)")*)[¶](#ApiClient.TableEntity.GetValue "Link to this definition")  
Returns the value in the given position. The position has to be specified 0 based. The header row does not effect the index, so GetValue(0, 0) will not return the first header cell, but the first actual cell underneath it.

Parameters:  row : int[¶](#ApiClient.TableEntity.GetValue.row "Permalink to this definition")  
the index of the row (0-based)

column : int[¶](#ApiClient.TableEntity.GetValue.column "Permalink to this definition")  
the index of the column (0-based)

Returns:  the value of the specified cell

Return type:  str

Raises:  
**ApiError** – If row or column values are invalid

GetValues()[¶](#ApiClient.TableEntity.GetValues "Link to this definition")  
Returns a list of lists, representing the values of the table. The header row will not be included.

Returns:  a list of lists representing the table value

Return type:  list[list[str]]

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
