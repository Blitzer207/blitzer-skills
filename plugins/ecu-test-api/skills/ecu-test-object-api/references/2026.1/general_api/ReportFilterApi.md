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

[ API for Reports ](ReportApi.md)

[ API for Report Filters ](#)

API for Report Filters

- [ FilterElement ](ReportFilterApi/FilterElement.md)
- [ FilterGroupConjunction ](ReportFilterApi/FilterGroupConjunction.md)
- [ FilterGroupDisjunction ](ReportFilterApi/FilterGroupDisjunction.md)
- [ FilterGroupElement ](ReportFilterApi/FilterGroupElement.md)

API for Report Filters [ API for Report Filters ](#)

API for Report Filters

- [C ReportFilterApi ](#ApiClient.ReportFilterApi)
  - [M CreateFilterGroupConjunction ](#ApiClient.ReportFilterApi.CreateFilterGroupConjunction)
  - [M CreateFilterGroupDisjunction ](#ApiClient.ReportFilterApi.CreateFilterGroupDisjunction)
  - [M GetAvailableFilters ](#ApiClient.ReportFilterApi.GetAvailableFilters)
- [ FilterElement ](ReportFilterApi/FilterElement.md)
- [ FilterGroupConjunction ](ReportFilterApi/FilterGroupConjunction.md)
- [ FilterGroupDisjunction ](ReportFilterApi/FilterGroupDisjunction.md)
- [ FilterGroupElement ](ReportFilterApi/FilterGroupElement.md)

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

API for Report Filters

- [C ReportFilterApi ](#ApiClient.ReportFilterApi)
  - [M CreateFilterGroupConjunction ](#ApiClient.ReportFilterApi.CreateFilterGroupConjunction)
  - [M CreateFilterGroupDisjunction ](#ApiClient.ReportFilterApi.CreateFilterGroupDisjunction)
  - [M GetAvailableFilters ](#ApiClient.ReportFilterApi.GetAvailableFilters)

# API for Report Filters[¶](#api-for-report-filters "Link to this heading")

Part of the [Object based program API](objectApi.md#objectapi).

*class* ReportFilterApi[¶](#ApiClient.ReportFilterApi "Link to this definition")  
API to create report filter definitions

Returned by

- [`ConfigurationApi.ReportFilterApi`](ConfigurationApi.md#ApiClient.ConfigurationApi.ReportFilterApi "ApiClient.ConfigurationApi.ReportFilterApi (Python attribute) — Returns the ReportFilterApi namespace.")

CreateFilterGroupConjunction()[¶](#ApiClient.ReportFilterApi.CreateFilterGroupConjunction "Link to this definition")  
Creates an ‘AND’ report filter group. Used to group several filter elements ([`FilterElement`](ReportFilterApi/FilterElement.md#ApiClient.FilterElement "ApiClient.FilterElement (Python class) — Represents a single filter criteria that can be appended to a report filter group ('AND' and 'OR').")).

Returns:  The ‘AND’ report filter group

Return type:  [`FilterGroupConjunction`](ReportFilterApi/FilterGroupConjunction.md#ApiClient.FilterGroupConjunction "ApiClient.FilterGroupConjunction (Python class) — Represents an 'AND' report filter group to which report filter elements can be appended. All elements within this group are connected by the logical operator 'AND'.")

CreateFilterGroupDisjunction()[¶](#ApiClient.ReportFilterApi.CreateFilterGroupDisjunction "Link to this definition")  
Creates an ‘OR’ report filter group. Used to group several filter elements ([`FilterElement`](ReportFilterApi/FilterElement.md#ApiClient.FilterElement "ApiClient.FilterElement (Python class) — Represents a single filter criteria that can be appended to a report filter group ('AND' and 'OR').")) or ‘AND’ filter groups ([`FilterGroupConjunction`](ReportFilterApi/FilterGroupConjunction.md#ApiClient.FilterGroupConjunction "ApiClient.FilterGroupConjunction (Python class) — Represents an 'AND' report filter group to which report filter elements can be appended. All elements within this group are connected by the logical operator 'AND'.")).

Returns:  The ‘OR’ report filter group

Return type:  [`FilterGroupDisjunction`](ReportFilterApi/FilterGroupDisjunction.md#ApiClient.FilterGroupDisjunction "ApiClient.FilterGroupDisjunction (Python class) — Represents an 'OR' report filter group to which either report filter elements (FilterElement) or 'AND' report filter groups (FilterGroupConjunction) can be appended. All elements within this group are connected by the logical operator 'OR'.")

GetAvailableFilters()[¶](#ApiClient.ReportFilterApi.GetAvailableFilters "Link to this definition")  
Returns a list of configured filters.

Returns:  List of filters

Return type:  list[[`FilterGroupElement`](ReportFilterApi/FilterGroupElement.md#ApiClient.FilterGroupElement "ApiClient.FilterGroupElement (Python class) — Represents objects that can be appended to an 'OR' report filter group.")]

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
