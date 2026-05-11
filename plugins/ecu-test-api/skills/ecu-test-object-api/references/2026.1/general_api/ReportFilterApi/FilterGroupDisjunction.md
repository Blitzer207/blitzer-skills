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

[ API for Report Filters ](../ReportFilterApi.md)

API for Report Filters

[ FilterElement ](FilterElement.md)

[ FilterGroupConjunction ](FilterGroupConjunction.md)

FilterGroupDisjunction [ FilterGroupDisjunction ](#)

FilterGroupDisjunction

- [C FilterGroupDisjunction ](#ApiClient.FilterGroupDisjunction)
  - [M AppendElement ](#ApiClient.FilterGroupDisjunction.AppendElement)
  - [M Clone ](#ApiClient.FilterGroupDisjunction.Clone)
  - [M GetElements ](#ApiClient.FilterGroupDisjunction.GetElements)
  - [M GetExpression ](#ApiClient.FilterGroupDisjunction.GetExpression)
  - [M RemoveElement ](#ApiClient.FilterGroupDisjunction.RemoveElement)

[ FilterGroupElement ](FilterGroupElement.md)

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

FilterGroupDisjunction

- [C FilterGroupDisjunction ](#ApiClient.FilterGroupDisjunction)
  - [M AppendElement ](#ApiClient.FilterGroupDisjunction.AppendElement)
  - [M Clone ](#ApiClient.FilterGroupDisjunction.Clone)
  - [M GetElements ](#ApiClient.FilterGroupDisjunction.GetElements)
  - [M GetExpression ](#ApiClient.FilterGroupDisjunction.GetExpression)
  - [M RemoveElement ](#ApiClient.FilterGroupDisjunction.RemoveElement)

# FilterGroupDisjunction[¶](#filtergroupdisjunction "Link to this heading")

*class* FilterGroupDisjunction[¶](#ApiClient.FilterGroupDisjunction "Link to this definition")  
Represents an ‘OR’ report filter group to which either report filter elements ([`FilterElement`](FilterElement.md#ApiClient.FilterElement "ApiClient.FilterElement (Python class) — Represents a single filter criteria that can be appended to a report filter group ('AND' and 'OR').")) or ‘AND’ report filter groups ([`FilterGroupConjunction`](FilterGroupConjunction.md#ApiClient.FilterGroupConjunction "ApiClient.FilterGroupConjunction (Python class) — Represents an 'AND' report filter group to which report filter elements can be appended. All elements within this group are connected by the logical operator 'AND'.")) can be appended. All elements within this group are connected by the logical operator ‘OR’.

Returned by

- [`ReportFilterApi.CreateFilterGroupDisjunction`](../ReportFilterApi.md#ApiClient.ReportFilterApi.CreateFilterGroupDisjunction "ApiClient.ReportFilterApi.CreateFilterGroupDisjunction (Python method) — Creates an 'OR' report filter group. Used to group several filter elements (FilterElement) or 'AND' filter groups (FilterGroupConjunction).")

AppendElement(*[filterElement](#ApiClient.FilterGroupDisjunction.AppendElement.filterElement "ApiClient.FilterGroupDisjunction.AppendElement.filterElement (Python parameter) — The filter element to be appended")*)[¶](#ApiClient.FilterGroupDisjunction.AppendElement "Link to this definition")  
Appends a filter element to the ‘OR’ report filter group.

Parameters:  filterElement[¶](#ApiClient.FilterGroupDisjunction.AppendElement.filterElement "Permalink to this definition")  
The filter element to be appended

Clone()[¶](#ApiClient.FilterGroupDisjunction.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`FilterGroupDisjunction`](#ApiClient.FilterGroupDisjunction "ApiClient.FilterGroupDisjunction (Python class) — Represents an 'OR' report filter group to which either report filter elements (FilterElement) or 'AND' report filter groups (FilterGroupConjunction) can be appended. All elements within this group are connected by the logical operator 'OR'.")

GetElements()[¶](#ApiClient.FilterGroupDisjunction.GetElements "Link to this definition")  
Returns the report filter elements.

Returns:  The report filter elements

Return type:  list[[`FilterGroupElement`](FilterGroupElement.md#ApiClient.FilterGroupElement "ApiClient.FilterGroupElement (Python class) — Represents objects that can be appended to an 'OR' report filter group.")]

GetExpression()[¶](#ApiClient.FilterGroupDisjunction.GetExpression "Link to this definition")  
Returns the report filter expression.

Returns:  The report filter expression

Return type:  str

RemoveElement(*[filterElement](#ApiClient.FilterGroupDisjunction.RemoveElement.filterElement "ApiClient.FilterGroupDisjunction.RemoveElement.filterElement (Python parameter) — The filter element to be removed")*)[¶](#ApiClient.FilterGroupDisjunction.RemoveElement "Link to this definition")  
Removes a filter element from the ‘OR’ report filter group.

Parameters:  filterElement[¶](#ApiClient.FilterGroupDisjunction.RemoveElement.filterElement "Permalink to this definition")  
The filter element to be removed

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
