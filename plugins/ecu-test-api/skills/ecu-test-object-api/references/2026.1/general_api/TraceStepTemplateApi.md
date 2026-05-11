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

[ API for Trace Step Templates ](#)

API for Trace Step Templates

- [ PythonEventFunction ](TraceStepTemplateApi/PythonEventFunction.md)
- [ TraceStepTemplate ](TraceStepTemplateApi/TraceStepTemplate.md)
- [ TraceStepTemplatePythonEvent ](TraceStepTemplateApi/TraceStepTemplatePythonEvent.md)

API for Trace Step Templates [ API for Trace Step Templates ](#)

API for Trace Step Templates

- [C TraceStepTemplateApi ](#ApiClient.TraceStepTemplateApi)
  - [M OpenTraceStepTemplate ](#ApiClient.TraceStepTemplateApi.OpenTraceStepTemplate)
  - [M SearchTraceStepTemplates ](#ApiClient.TraceStepTemplateApi.SearchTraceStepTemplates)
- [ PythonEventFunction ](TraceStepTemplateApi/PythonEventFunction.md)
- [ TraceStepTemplate ](TraceStepTemplateApi/TraceStepTemplate.md)
- [ TraceStepTemplatePythonEvent ](TraceStepTemplateApi/TraceStepTemplatePythonEvent.md)

[ API for Variables ](VariableApi.md)

[ API for Workspaces ](WorkspaceApi.md)

[ Trace Analysis API ](../TraceAnalysisAPI/index.md)

[ Generator APIs ](../generators/index.md)

[ Tools ](../tools/index.md)

[ User test management ](../userTestmanagement/index.md)

[ UserUtility API ](../user-utility/user-utility.md)

[ Utility Examples ](../user-utility/example-utilities.md)

API for Trace Step Templates

- [C TraceStepTemplateApi ](#ApiClient.TraceStepTemplateApi)
  - [M OpenTraceStepTemplate ](#ApiClient.TraceStepTemplateApi.OpenTraceStepTemplate)
  - [M SearchTraceStepTemplates ](#ApiClient.TraceStepTemplateApi.SearchTraceStepTemplates)

# API for Trace Step Templates[¶](#api-for-trace-step-templates "Link to this heading")

Part of the [Object based program API](objectApi.md#objectapi).

*class* TraceStepTemplateApi[¶](#ApiClient.TraceStepTemplateApi "Link to this definition")  
API to access trace step template files

Returned by

- [`ApiClient.TraceStepTemplateApi`](objectApi.md#ApiClient.ApiClient.TraceStepTemplateApi "ApiClient.ApiClient.TraceStepTemplateApi (Python attribute) — Returns the TraceStepTemplateApi namespace.")

OpenTraceStepTemplate(*[filename](#ApiClient.TraceStepTemplateApi.OpenTraceStepTemplate.filename "ApiClient.TraceStepTemplateApi.OpenTraceStepTemplate.filename (Python parameter) — Absolute or relative path of the trace step template file. If relative the file must be located in the user defined trace step template directory.")*)[¶](#ApiClient.TraceStepTemplateApi.OpenTraceStepTemplate "Link to this definition")  
Opens a trace step template file.

Parameters:  filename : str[¶](#ApiClient.TraceStepTemplateApi.OpenTraceStepTemplate.filename "Permalink to this definition")  
Absolute or relative path of the trace step template file. If relative the file must be located in the user defined trace step template directory.

Returns:  Trace step template

Return type:  [`TraceStepTemplate`](TraceStepTemplateApi/TraceStepTemplate.md#ApiClient.TraceStepTemplate "ApiClient.TraceStepTemplate (Python class) — TraceStepTemplateApi.OpenTraceStepTemplate")

SearchTraceStepTemplates(*[searchCriteria](#ApiClient.TraceStepTemplateApi.SearchTraceStepTemplates.searchCriteria "ApiClient.TraceStepTemplateApi.SearchTraceStepTemplates.searchCriteria (Python parameter) — The search criteria expressed in the ecu.test filter syntax.")*, *[useExtendedMode](#ApiClient.TraceStepTemplateApi.SearchTraceStepTemplates.useExtendedMode "ApiClient.TraceStepTemplateApi.SearchTraceStepTemplates.useExtendedMode (Python parameter) — If True, extended search strings are enabled.")=`False`*)[¶](#ApiClient.TraceStepTemplateApi.SearchTraceStepTemplates "Link to this definition")  
Searches the current workspace and library workspaces for trace step templates matching the given search criteria.

Parameters:  searchCriteria : str[¶](#ApiClient.TraceStepTemplateApi.SearchTraceStepTemplates.searchCriteria "Permalink to this definition")  
The search criteria expressed in the ecu.test filter syntax. See section “Handling” =\> “Filter” of the ecu.test User Documentation.

useExtendedMode : boolean[¶](#ApiClient.TraceStepTemplateApi.SearchTraceStepTemplates.useExtendedMode "Permalink to this definition")  
If True, extended search strings are enabled. The default is False, meaning each word in the searchCriteria will be enclosed by wildcards and mapped to the filename. (e.g. “hello world” =\> “Name = ‘\*hello\*’ and Name = ‘\*world\*’”)

Returns:  All matching trace step templates. If no template matches, an empty list is returned.

Return type:  list[[`TraceStepTemplate`](TraceStepTemplateApi/TraceStepTemplate.md#ApiClient.TraceStepTemplate "ApiClient.TraceStepTemplate (Python class) — TraceStepTemplateApi.OpenTraceStepTemplate")]

Raises:  
**ApiError** – If the searchCriteria has an illegal syntax.

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
