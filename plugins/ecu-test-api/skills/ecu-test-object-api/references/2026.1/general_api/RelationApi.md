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

[ API for Relations ](#)

API for Relations

- [ Relation ](RelationApi/Relation.md)

API for Relations [ API for Relations ](#)

API for Relations

- [C RelationApi ](#ApiClient.RelationApi)
  - [A IMPLEMENTS ](#ApiClient.RelationApi.IMPLEMENTS)
  - [A IS_DERIVED_FROM ](#ApiClient.RelationApi.IS_DERIVED_FROM)
  - [A RELATES_TO ](#ApiClient.RelationApi.RELATES_TO)
  - [M CreateRelation ](#ApiClient.RelationApi.CreateRelation)
- [ Relation ](RelationApi/Relation.md)

[ API for Reports ](ReportApi.md)

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

API for Relations

- [C RelationApi ](#ApiClient.RelationApi)
  - [A IMPLEMENTS ](#ApiClient.RelationApi.IMPLEMENTS)
  - [A IS_DERIVED_FROM ](#ApiClient.RelationApi.IS_DERIVED_FROM)
  - [A RELATES_TO ](#ApiClient.RelationApi.RELATES_TO)
  - [M CreateRelation ](#ApiClient.RelationApi.CreateRelation)

# API for Relations[¶](#api-for-relations "Link to this heading")

Part of the [Object based program API](objectApi.md#objectapi).

*class* RelationApi[¶](#ApiClient.RelationApi "Link to this definition")  
API to access relations

Returned by

- [`ApiClient.RelationApi`](objectApi.md#ApiClient.ApiClient.RelationApi "ApiClient.ApiClient.RelationApi (Python attribute) — Returns the RelationApi namespace.")

IMPLEMENTS[¶](#ApiClient.RelationApi.IMPLEMENTS "Link to this definition")  
Returns the constant used to specify the relation type ‘implements’:

Returns:  ‘implements’ constant

Return type:  int

IS_DERIVED_FROM[¶](#ApiClient.RelationApi.IS_DERIVED_FROM "Link to this definition")  
Returns the constant used to specify the relation type ‘is derived from’:

Returns:  ‘is derived from’ constant

Return type:  int

RELATES_TO[¶](#ApiClient.RelationApi.RELATES_TO "Link to this definition")  
Returns the constant used to specify the relation type ‘relates to’:

Returns:  ‘relates to’ constant

Return type:  int

CreateRelation(*[relationType](#ApiClient.RelationApi.CreateRelation.relationType "ApiClient.RelationApi.CreateRelation.relationType (Python parameter) — relation type e.g.")*, *[packagePath](#ApiClient.RelationApi.CreateRelation.packagePath "ApiClient.RelationApi.CreateRelation.packagePath (Python parameter) — Path to Package")*)[¶](#ApiClient.RelationApi.CreateRelation "Link to this definition")  
Creates a new relation with the current target version.

Parameters:  relationType : int[¶](#ApiClient.RelationApi.CreateRelation.relationType "Permalink to this definition")  
relation type e.g. ‘relatest to’ or ‘is derived from’

- `RelationApi.RELATEST_TO`

packagePath : str[¶](#ApiClient.RelationApi.CreateRelation.packagePath "Permalink to this definition")  
Path to Package

Returns:  new Relation

Return type:  [`Relation`](RelationApi/Relation.md#ApiClient.Relation "ApiClient.Relation (Python class) — RelationApi.CreateRelation")

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
