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

API for Relations

Relation [ Relation ](#)

Relation

- [C Relation ](#ApiClient.Relation)
  - [M Clone ](#ApiClient.Relation.Clone)
  - [M GetSpecifiedTargetVersion ](#ApiClient.Relation.GetSpecifiedTargetVersion)
  - [M GetTargetPath ](#ApiClient.Relation.GetTargetPath)
  - [M GetType ](#ApiClient.Relation.GetType)
  - [M IsSpecifiedVersionOutdated ](#ApiClient.Relation.IsSpecifiedVersionOutdated)
  - [M SetSpecifiedTargetVersion ](#ApiClient.Relation.SetSpecifiedTargetVersion)
  - [M UpdateSpecifiedTargetVersion ](#ApiClient.Relation.UpdateSpecifiedTargetVersion)

[ API for Reports ](../ReportApi.md)

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

Relation

- [C Relation ](#ApiClient.Relation)
  - [M Clone ](#ApiClient.Relation.Clone)
  - [M GetSpecifiedTargetVersion ](#ApiClient.Relation.GetSpecifiedTargetVersion)
  - [M GetTargetPath ](#ApiClient.Relation.GetTargetPath)
  - [M GetType ](#ApiClient.Relation.GetType)
  - [M IsSpecifiedVersionOutdated ](#ApiClient.Relation.IsSpecifiedVersionOutdated)
  - [M SetSpecifiedTargetVersion ](#ApiClient.Relation.SetSpecifiedTargetVersion)
  - [M UpdateSpecifiedTargetVersion ](#ApiClient.Relation.UpdateSpecifiedTargetVersion)

# Relation[¶](#relation "Link to this heading")

*class* Relation[¶](#ApiClient.Relation "Link to this definition")  
Returned by

- [`RelationApi.CreateRelation`](../RelationApi.md#ApiClient.RelationApi.CreateRelation "ApiClient.RelationApi.CreateRelation (Python method) — Creates a new relation with the current target version.")

Clone()[¶](#ApiClient.Relation.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`Relation`](#ApiClient.Relation "ApiClient.Relation (Python class) — RelationApi.CreateRelation")

GetSpecifiedTargetVersion()[¶](#ApiClient.Relation.GetSpecifiedTargetVersion "Link to this definition")  
Returns the version of relation target. This version is specified at the relation creation time and could be updated later.

Returns:  specified relation target version

Return type:  string

GetTargetPath()[¶](#ApiClient.Relation.GetTargetPath "Link to this definition")  
Returns the path to the relation target.

Returns:  Path relative to the package directory

Return type:  string

GetType()[¶](#ApiClient.Relation.GetType "Link to this definition")  
Returns the relation type.

Returns:  relation type e.g. ‘relatest to’ or ‘is derived from’

- `RelationApi.RELATEST_TO`

Return type:  int

IsSpecifiedVersionOutdated()[¶](#ApiClient.Relation.IsSpecifiedVersionOutdated "Link to this definition")  
Returns true if the current version of relation target is not equal to already specified relation target version.

Returns:  True if the specified relation target version is outdated.

Return type:  boolean

SetSpecifiedTargetVersion(*[version](#ApiClient.Relation.SetSpecifiedTargetVersion.version "ApiClient.Relation.SetSpecifiedTargetVersion.version (Python parameter) — The version of relation target to be set.")*)[¶](#ApiClient.Relation.SetSpecifiedTargetVersion "Link to this definition")  
Sets the version of relation target. The specified version is stored as a property of this relation.

Parameters:  version : string[¶](#ApiClient.Relation.SetSpecifiedTargetVersion.version "Permalink to this definition")  
The version of relation target to be set.

UpdateSpecifiedTargetVersion()[¶](#ApiClient.Relation.UpdateSpecifiedTargetVersion "Link to this definition")  
Updates the version of relation target to the current target value. This updated version is stored as a property of this relation.

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
