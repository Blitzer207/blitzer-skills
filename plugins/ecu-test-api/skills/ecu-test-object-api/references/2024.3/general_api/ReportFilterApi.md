# API for Report Filters[¶](#api-for-report-filters "Link to this heading")

Part of the [Object based program API](objectApi.md#objectapi)

## ReportFilterApi[¶](#reportfilterapi "Link to this heading")

*class* ReportFilterApi[¶](#ApiClient.ReportFilterApi "Link to this definition")  
API to create report filter definitions

Returned by

- [`ConfigurationApi.ReportFilterApi`](ConfigurationApi.md#ApiClient.ConfigurationApi.ReportFilterApi "ApiClient.ConfigurationApi.ReportFilterApi")

CreateFilterGroupConjunction()[¶](#ApiClient.ReportFilterApi.CreateFilterGroupConjunction "Link to this definition")  
Creates an ‘AND’ report filter group. Used to group several filter elements ([`FilterElement`](#ApiClient.FilterElement "ApiClient.FilterElement")).

Returns:  The ‘AND’ report filter group

Return type:  [`FilterGroupConjunction`](#ApiClient.FilterGroupConjunction "ApiClient.FilterGroupConjunction")

CreateFilterGroupDisjunction()[¶](#ApiClient.ReportFilterApi.CreateFilterGroupDisjunction "Link to this definition")  
Creates an ‘OR’ report filter group. Used to group several filter elements ([`FilterElement`](#ApiClient.FilterElement "ApiClient.FilterElement")) or ‘AND’ filter groups ([`FilterGroupConjunction`](#ApiClient.FilterGroupConjunction "ApiClient.FilterGroupConjunction")).

Returns:  The ‘OR’ report filter group

Return type:  [`FilterGroupDisjunction`](#ApiClient.FilterGroupDisjunction "ApiClient.FilterGroupDisjunction")

GetAvailableFilters()[¶](#ApiClient.ReportFilterApi.GetAvailableFilters "Link to this definition")  
Returns a list of configured filters.

Returns:  List of filters

Return type:  list[[`FilterGroupElement`](#ApiClient.FilterGroupElement "ApiClient.FilterGroupElement")]

## FilterElement[¶](#filterelement "Link to this heading")

*class* FilterElement[¶](#ApiClient.FilterElement "Link to this definition")  
Represents a single filter criteria that can be appended to a report filter group (‘AND’ and ‘OR’).

Base class

[`FilterGroupElement`](#ApiClient.FilterGroupElement "ApiClient.FilterGroupElement")

Returned by

- [`FilterGroupConjunction.GetElements`](#ApiClient.FilterGroupConjunction.GetElements "ApiClient.FilterGroupConjunction.GetElements")

Clone()[¶](#ApiClient.FilterElement.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`FilterElement`](#ApiClient.FilterElement "ApiClient.FilterElement")

GetExpression()[¶](#ApiClient.FilterElement.GetExpression "Link to this definition")  
Returns the report filter expression.

Returns:  The report filter expression

Return type:  str

## FilterGroupConjunction[¶](#filtergroupconjunction "Link to this heading")

*class* FilterGroupConjunction[¶](#ApiClient.FilterGroupConjunction "Link to this definition")  
Represents an ‘AND’ report filter group to which report filter elements can be appended. All elements within this group are connected by the logical operator ‘AND’.

Base class

[`FilterGroupElement`](#ApiClient.FilterGroupElement "ApiClient.FilterGroupElement")

Returned by

- [`ReportFilterApi.CreateFilterGroupConjunction`](#ApiClient.ReportFilterApi.CreateFilterGroupConjunction "ApiClient.ReportFilterApi.CreateFilterGroupConjunction")

AppendElement(*filterElement*)[¶](#ApiClient.FilterGroupConjunction.AppendElement "Link to this definition")  
Appends a filter element to the ‘AND’ report filter group.

Parameters:  **filterElement** ([`FilterElement`](#ApiClient.FilterElement "ApiClient.FilterElement")) – The filter element to be appended

Clone()[¶](#ApiClient.FilterGroupConjunction.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`FilterGroupConjunction`](#ApiClient.FilterGroupConjunction "ApiClient.FilterGroupConjunction")

GetElements()[¶](#ApiClient.FilterGroupConjunction.GetElements "Link to this definition")  
Returns the report filter elements.

Returns:  The report filter elements

Return type:  list[[`FilterElement`](#ApiClient.FilterElement "ApiClient.FilterElement")]

GetExpression()[¶](#ApiClient.FilterGroupConjunction.GetExpression "Link to this definition")  
Returns the report filter expression.

Returns:  The report filter expression

Return type:  str

RemoveElement(*filterElement*)[¶](#ApiClient.FilterGroupConjunction.RemoveElement "Link to this definition")  
Removes a filter element from the ‘AND’ report filter group.

Parameters:  **filterElement** ([`FilterElement`](#ApiClient.FilterElement "ApiClient.FilterElement")) – The filter element to be removed

## FilterGroupDisjunction[¶](#filtergroupdisjunction "Link to this heading")

*class* FilterGroupDisjunction[¶](#ApiClient.FilterGroupDisjunction "Link to this definition")  
Represents an ‘OR’ report filter group to which either report filter elements ([`FilterElement`](#ApiClient.FilterElement "ApiClient.FilterElement")) or ‘AND’ report filter groups ([`FilterGroupConjunction`](#ApiClient.FilterGroupConjunction "ApiClient.FilterGroupConjunction")) can be appended. All elements within this group are connected by the logical operator ‘OR’.

Returned by

- [`ReportFilterApi.CreateFilterGroupDisjunction`](#ApiClient.ReportFilterApi.CreateFilterGroupDisjunction "ApiClient.ReportFilterApi.CreateFilterGroupDisjunction")

- [`ReportFormat.GetProjectFilter`](ConfigurationApi.md#ApiClient.ReportFormat.GetProjectFilter "ApiClient.ReportFormat.GetProjectFilter")

- [`ReportFormat.GetTestCaseFilter`](ConfigurationApi.md#ApiClient.ReportFormat.GetTestCaseFilter "ApiClient.ReportFormat.GetTestCaseFilter")

- [`ReportFormat.GetTraceAnalysesFilter`](ConfigurationApi.md#ApiClient.ReportFormat.GetTraceAnalysesFilter "ApiClient.ReportFormat.GetTraceAnalysesFilter")

AppendElement(*filterElement*)[¶](#ApiClient.FilterGroupDisjunction.AppendElement "Link to this definition")  
Appends a filter element to the ‘OR’ report filter group.

Parameters:  **filterElement** ([`FilterGroupElement`](#ApiClient.FilterGroupElement "ApiClient.FilterGroupElement")) – The filter element to be appended

Clone()[¶](#ApiClient.FilterGroupDisjunction.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`FilterGroupDisjunction`](#ApiClient.FilterGroupDisjunction "ApiClient.FilterGroupDisjunction")

GetElements()[¶](#ApiClient.FilterGroupDisjunction.GetElements "Link to this definition")  
Returns the report filter elements.

Returns:  The report filter elements

Return type:  list[[`FilterGroupElement`](#ApiClient.FilterGroupElement "ApiClient.FilterGroupElement")]

GetExpression()[¶](#ApiClient.FilterGroupDisjunction.GetExpression "Link to this definition")  
Returns the report filter expression.

Returns:  The report filter expression

Return type:  str

RemoveElement(*filterElement*)[¶](#ApiClient.FilterGroupDisjunction.RemoveElement "Link to this definition")  
Removes a filter element from the ‘OR’ report filter group.

Parameters:  **filterElement** ([`FilterGroupElement`](#ApiClient.FilterGroupElement "ApiClient.FilterGroupElement")) – The filter element to be removed

## FilterGroupElement[¶](#filtergroupelement "Link to this heading")

*class* FilterGroupElement[¶](#ApiClient.FilterGroupElement "Link to this definition")  
Represents objects that can be appended to an ‘OR’ report filter group.

Returned by

- [`FilterGroupDisjunction.GetElements`](#ApiClient.FilterGroupDisjunction.GetElements "ApiClient.FilterGroupDisjunction.GetElements")

- [`ReportFilterApi.GetAvailableFilters`](#ApiClient.ReportFilterApi.GetAvailableFilters "ApiClient.ReportFilterApi.GetAvailableFilters")

Subclasses

- [`FilterElement`](#ApiClient.FilterElement "ApiClient.FilterElement")

- [`FilterGroupConjunction`](#ApiClient.FilterGroupConjunction "ApiClient.FilterGroupConjunction")

Clone()[¶](#ApiClient.FilterGroupElement.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`FilterGroupElement`](#ApiClient.FilterGroupElement "ApiClient.FilterGroupElement")

GetExpression()[¶](#ApiClient.FilterGroupElement.GetExpression "Link to this definition")  
Returns the report filter expression.

Returns:  The report filter expression

Return type:  str
