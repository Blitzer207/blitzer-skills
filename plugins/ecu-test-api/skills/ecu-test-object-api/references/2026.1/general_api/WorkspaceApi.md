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

[ API for Trace Step Templates ](TraceStepTemplateApi.md)

[ API for Variables ](VariableApi.md)

API for Workspaces [ API for Workspaces ](#)

API for Workspaces

- [C WorkspaceApi ](#ApiClient.WorkspaceApi)
  - [M GetReferencesIn ](#ApiClient.WorkspaceApi.GetReferencesIn)
  - [M GetReferencesTo ](#ApiClient.WorkspaceApi.GetReferencesTo)
  - [M SearchFiles ](#ApiClient.WorkspaceApi.SearchFiles)

[ Trace Analysis API ](../TraceAnalysisAPI/index.md)

[ Generator APIs ](../generators/index.md)

[ Tools ](../tools/index.md)

[ User test management ](../userTestmanagement/index.md)

[ UserUtility API ](../user-utility/user-utility.md)

[ Utility Examples ](../user-utility/example-utilities.md)

API for Workspaces

- [C WorkspaceApi ](#ApiClient.WorkspaceApi)
  - [M GetReferencesIn ](#ApiClient.WorkspaceApi.GetReferencesIn)
  - [M GetReferencesTo ](#ApiClient.WorkspaceApi.GetReferencesTo)
  - [M SearchFiles ](#ApiClient.WorkspaceApi.SearchFiles)

# API for Workspaces[¶](#api-for-workspaces "Link to this heading")

Part of the [Object based program API](objectApi.md#objectapi).

*class* WorkspaceApi[¶](#ApiClient.WorkspaceApi "Link to this definition")  
API to access the workspace

Returned by

- [`ApiClient.WorkspaceApi`](objectApi.md#ApiClient.ApiClient.WorkspaceApi "ApiClient.ApiClient.WorkspaceApi (Python attribute) — Returns the WorkspaceApi namespace.")

GetReferencesIn(*[filePath](#ApiClient.WorkspaceApi.GetReferencesIn.filePath "ApiClient.WorkspaceApi.GetReferencesIn.filePath (Python parameter) — References in this package/project are searched for.")*)[¶](#ApiClient.WorkspaceApi.GetReferencesIn "Link to this definition")  
Checks the passed file whether it contains references and returns the contained references as a list of absolute file paths.

Parameters:  filePath : str[¶](#ApiClient.WorkspaceApi.GetReferencesIn.filePath "Permalink to this definition")  
References in this package/project are searched for.

Returns:  The absolute paths of all references to packages/projects within filePath. If no references are found, an empty list is returned.

Return type:  list[str]

GetReferencesTo(*[filePath](#ApiClient.WorkspaceApi.GetReferencesTo.filePath "ApiClient.WorkspaceApi.GetReferencesTo.filePath (Python parameter) — References to this package/project path are searched for.")*)[¶](#ApiClient.WorkspaceApi.GetReferencesTo "Link to this definition")  
Traverses the workspace and searches in all packages and projects for references to the passed package/project and returns the references as a list of absolute file paths.

Parameters:  filePath : str[¶](#ApiClient.WorkspaceApi.GetReferencesTo.filePath "Permalink to this definition")  
References to this package/project path are searched for.

Returns:  The absolute paths of all packages/projects referencing to filePath. If no references are found, an empty list is returned.

Return type:  list[str]

SearchFiles(*[searchCriteria](#ApiClient.WorkspaceApi.SearchFiles.searchCriteria "ApiClient.WorkspaceApi.SearchFiles.searchCriteria (Python parameter) — The search criteria expressed in the ecu.test filter syntax.")*, *[useExtendedMode](#ApiClient.WorkspaceApi.SearchFiles.useExtendedMode "ApiClient.WorkspaceApi.SearchFiles.useExtendedMode (Python parameter) — If True, extended search strings are enabled.")=`False`*)[¶](#ApiClient.WorkspaceApi.SearchFiles "Link to this definition")  
Searches the current workspace and library workspaces for files matching the given search criteria.

Parameters:  searchCriteria : str[¶](#ApiClient.WorkspaceApi.SearchFiles.searchCriteria "Permalink to this definition")  
The search criteria expressed in the ecu.test filter syntax. See section “Handling” =\> “Filter” of the ecu.test User Documentation.

useExtendedMode : boolean[¶](#ApiClient.WorkspaceApi.SearchFiles.useExtendedMode "Permalink to this definition")  
If True, extended search strings are enabled. The default is False, meaning each word in the searchCriteria will be enclosed by wildcards and mapped to the filename. (e.g. “hello world” =\> “Name = ‘\*hello\*’ and Name = ‘\*world\*’”)

Returns:  The absolute paths of all matching files in the workspace. If no file matches, an empty list is returned.

Return type:  list[str]

Raises:  
**ApiError** – If the searchCriteria has an illegal syntax.

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
