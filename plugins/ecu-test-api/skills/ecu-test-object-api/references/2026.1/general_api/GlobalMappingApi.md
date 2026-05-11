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

[ API for Global Mappings ](#)

API for Global Mappings

- [ GlobalMapping ](GlobalMappingApi/GlobalMapping.md)

API for Global Mappings [ API for Global Mappings ](#)

API for Global Mappings

- [C GlobalMappingApi ](#ApiClient.GlobalMappingApi)
  - [M CreateMapping ](#ApiClient.GlobalMappingApi.CreateMapping)
  - [M GetChanges ](#ApiClient.GlobalMappingApi.GetChanges)
  - [M OpenMapping ](#ApiClient.GlobalMappingApi.OpenMapping)
  - [M SearchGlobalMappings ](#ApiClient.GlobalMappingApi.SearchGlobalMappings)
- [ GlobalMapping ](GlobalMappingApi/GlobalMapping.md)

[ API for Mappings ](MappingApi.md)

[ API for Multimedia Objects ](MultimediaApi.md)

[ API for Packages ](PackageApi.md)

[ API for Parameters ](ParameterApi.md)

[ API for Projects ](ProjectApi.md)

[ API for Relations ](RelationApi.md)

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

API for Global Mappings

- [C GlobalMappingApi ](#ApiClient.GlobalMappingApi)
  - [M CreateMapping ](#ApiClient.GlobalMappingApi.CreateMapping)
  - [M GetChanges ](#ApiClient.GlobalMappingApi.GetChanges)
  - [M OpenMapping ](#ApiClient.GlobalMappingApi.OpenMapping)
  - [M SearchGlobalMappings ](#ApiClient.GlobalMappingApi.SearchGlobalMappings)

# API for Global Mappings[¶](#api-for-global-mappings "Link to this heading")

Part of the [Object based program API](objectApi.md#objectapi).

*class* GlobalMappingApi[¶](#ApiClient.GlobalMappingApi "Link to this definition")  
API to access global mapping files

Returned by

- [`ApiClient.GlobalMappingApi`](objectApi.md#ApiClient.ApiClient.GlobalMappingApi "ApiClient.ApiClient.GlobalMappingApi (Python attribute) — Returns the GlobalMappingApi namespace.")

CreateMapping()[¶](#ApiClient.GlobalMappingApi.CreateMapping "Link to this definition")  
Creates an empty Mapping.

Returns:  An empty mapping

Return type:  [`GlobalMapping`](GlobalMappingApi/GlobalMapping.md#ApiClient.GlobalMapping "ApiClient.GlobalMapping (Python class) — GlobalMappingApi.CreateMapping")

GetChanges(*[oldGlobalMapping](#ApiClient.GlobalMappingApi.GetChanges.oldGlobalMapping "ApiClient.GlobalMappingApi.GetChanges.oldGlobalMapping (Python parameter) — The old global mapping to compare.")*, *[newGlobalMapping](#ApiClient.GlobalMappingApi.GetChanges.newGlobalMapping "ApiClient.GlobalMappingApi.GetChanges.newGlobalMapping (Python parameter) — The new global mapping to compare.")*)[¶](#ApiClient.GlobalMappingApi.GetChanges "Link to this definition")  
Get the changes that exist between two given global mappings.

Parameters:  oldGlobalMapping[¶](#ApiClient.GlobalMappingApi.GetChanges.oldGlobalMapping "Permalink to this definition")  
The old global mapping to compare.

newGlobalMapping[¶](#ApiClient.GlobalMappingApi.GetChanges.newGlobalMapping "Permalink to this definition")  
The new global mapping to compare.

Returns:  The changes that exist between the two global mappings.

Return type:  list[[`Change`](ConfigurationApi/Change.md#ApiClient.Change "ApiClient.Change (Python class) — Represents a change between an old element and a new element. Both elements have the same type, e.g. a certain test step and stem from two different Objects, e.g. an old Package a new Package.")]

OpenMapping(*[filename](#ApiClient.GlobalMappingApi.OpenMapping.filename "ApiClient.GlobalMappingApi.OpenMapping.filename (Python parameter) — Mapping file path.")*)[¶](#ApiClient.GlobalMappingApi.OpenMapping "Link to this definition")  
Opens an existing global mapping. Raises an ApiError if the referenced file does not exist.

Parameters:  filename : str[¶](#ApiClient.GlobalMappingApi.OpenMapping.filename "Permalink to this definition")  
Mapping file path. Can be absolute or relative to the parameters-directory.

Returns:  Opened mapping.

Return type:  [`GlobalMapping`](GlobalMappingApi/GlobalMapping.md#ApiClient.GlobalMapping "ApiClient.GlobalMapping (Python class) — GlobalMappingApi.CreateMapping")

SearchGlobalMappings(*[searchCriteria](#ApiClient.GlobalMappingApi.SearchGlobalMappings.searchCriteria "ApiClient.GlobalMappingApi.SearchGlobalMappings.searchCriteria (Python parameter) — The search criteria expressed in the ecu.test filter syntax.")*, *[useExtendedMode](#ApiClient.GlobalMappingApi.SearchGlobalMappings.useExtendedMode "ApiClient.GlobalMappingApi.SearchGlobalMappings.useExtendedMode (Python parameter) — If True, extended search strings are enabled.")=`False`*)[¶](#ApiClient.GlobalMappingApi.SearchGlobalMappings "Link to this definition")  
Searches the current workspace and library workspaces for Global Mappings matching the given search criteria.

Parameters:  searchCriteria : str[¶](#ApiClient.GlobalMappingApi.SearchGlobalMappings.searchCriteria "Permalink to this definition")  
The search criteria expressed in the ecu.test filter syntax. See section “Handling” =\> “Filter” of the ecu.test User Documentation.

useExtendedMode : boolean[¶](#ApiClient.GlobalMappingApi.SearchGlobalMappings.useExtendedMode "Permalink to this definition")  
If True, extended search strings are enabled. The default is False, meaning each word in the searchCriteria will be enclosed by wildcards and mapped to the filename. (e.g. “hello world” =\> “Name = ‘\*hello\*’ and Name = ‘\*world\*’”)

Returns:  All matching Global Mappings. If no file matches, an emtpy list is returned.

Return type:  list[[`GlobalMapping`](GlobalMappingApi/GlobalMapping.md#ApiClient.GlobalMapping "ApiClient.GlobalMapping (Python class) — GlobalMappingApi.CreateMapping")]

Raises:  
**ApiError** – If the searchCriteria has an illegal syntax.

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
