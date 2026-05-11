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

[ API for Projects ](#)

API for Projects

- [ Project ](ProjectApi/Project.md)

API for Projects [ API for Projects ](#)

API for Projects

- [C ProjectApi ](#ApiClient.ProjectApi)
  - [A ComponentApi ](#ApiClient.ProjectApi.ComponentApi)
  - [M CreateProject ](#ApiClient.ProjectApi.CreateProject)
  - [M GetChanges ](#ApiClient.ProjectApi.GetChanges)
  - [M OpenProject ](#ApiClient.ProjectApi.OpenProject)
  - [M OpenProjectFromArchive ](#ApiClient.ProjectApi.OpenProjectFromArchive)
  - [M SearchProjects ](#ApiClient.ProjectApi.SearchProjects)
- [ Project ](ProjectApi/Project.md)

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

API for Projects

- [C ProjectApi ](#ApiClient.ProjectApi)
  - [A ComponentApi ](#ApiClient.ProjectApi.ComponentApi)
  - [M CreateProject ](#ApiClient.ProjectApi.CreateProject)
  - [M GetChanges ](#ApiClient.ProjectApi.GetChanges)
  - [M OpenProject ](#ApiClient.ProjectApi.OpenProject)
  - [M OpenProjectFromArchive ](#ApiClient.ProjectApi.OpenProjectFromArchive)
  - [M SearchProjects ](#ApiClient.ProjectApi.SearchProjects)

# API for Projects[¶](#api-for-projects "Link to this heading")

Part of the [Object based program API](objectApi.md#objectapi).

*class* ProjectApi[¶](#ApiClient.ProjectApi "Link to this definition")  
API to access projects

Returned by

- [`ApiClient.ProjectApi`](objectApi.md#ApiClient.ApiClient.ProjectApi "ApiClient.ApiClient.ProjectApi (Python attribute) — Returns the ProjectApi namespace.")

ComponentApi[¶](#ApiClient.ProjectApi.ComponentApi "Link to this definition")  
Returns the ComponentApi namespace.

Returns:  ComponentApi namespace

Return type:  [`ComponentApi`](ComponentApi.md#ApiClient.ComponentApi "ApiClient.ComponentApi (Python class) — API to access projects")

CreateProject()[¶](#ApiClient.ProjectApi.CreateProject "Link to this definition")  
Creates a new project.

Returns:  New empty project

Return type:  [`Project`](ProjectApi/Project.md#ApiClient.Project "ApiClient.Project (Python class) — ProjectApi.CreateProject")

GetChanges(*[oldProject](#ApiClient.ProjectApi.GetChanges.oldProject "ApiClient.ProjectApi.GetChanges.oldProject (Python parameter) — The old project to compare.")*, *[newProject](#ApiClient.ProjectApi.GetChanges.newProject "ApiClient.ProjectApi.GetChanges.newProject (Python parameter) — The new project to compare.")*)[¶](#ApiClient.ProjectApi.GetChanges "Link to this definition")  
Get the changes that exist between two given projects.

Parameters:  oldProject[¶](#ApiClient.ProjectApi.GetChanges.oldProject "Permalink to this definition")  
The old project to compare.

newProject[¶](#ApiClient.ProjectApi.GetChanges.newProject "Permalink to this definition")  
The new project to compare.

Returns:  The changes that exist between the two projects.

Return type:  list[[`Change`](ConfigurationApi/Change.md#ApiClient.Change "ApiClient.Change (Python class) — Represents a change between an old element and a new element. Both elements have the same type, e.g. a certain test step and stem from two different Objects, e.g. an old Package a new Package.")]

OpenProject(*[filename](#ApiClient.ProjectApi.OpenProject.filename "ApiClient.ProjectApi.OpenProject.filename (Python parameter) — Absolute path to the project file or relative path in regard to the package directory")*, *[execInCurrentPkgDir](#ApiClient.ProjectApi.OpenProject.execInCurrentPkgDir "ApiClient.ProjectApi.OpenProject.execInCurrentPkgDir (Python parameter) — Whether to treat relative references in the project like the project file "belongs" in the root of the current workspace's package folder instead of its actual location.")=`False`*, *[filterExpression](#ApiClient.ProjectApi.OpenProject.filterExpression "ApiClient.ProjectApi.OpenProject.filterExpression (Python parameter) — A valid project filter expression")=`''`*)[¶](#ApiClient.ProjectApi.OpenProject "Link to this definition")  
Opens an existing project. The project may not be opened in ecu.test.

Parameters:  filename : str[¶](#ApiClient.ProjectApi.OpenProject.filename "Permalink to this definition")  
Absolute path to the project file or relative path in regard to the package directory

execInCurrentPkgDir : boolean[¶](#ApiClient.ProjectApi.OpenProject.execInCurrentPkgDir "Permalink to this definition")  
Whether to treat relative references in the project like the project file “belongs” in the root of the current workspace’s package folder instead of its actual location.

filterExpression : str[¶](#ApiClient.ProjectApi.OpenProject.filterExpression "Permalink to this definition")  
A valid project filter expression

Returns:  Existing project

Return type:  [`Project`](ProjectApi/Project.md#ApiClient.Project "ApiClient.Project (Python class) — ProjectApi.CreateProject")

OpenProjectFromArchive(*[filename](#ApiClient.ProjectApi.OpenProjectFromArchive.filename "ApiClient.ProjectApi.OpenProjectFromArchive.filename (Python parameter) — Absolute path to the project archive file.")*)[¶](#ApiClient.ProjectApi.OpenProjectFromArchive "Link to this definition")  
Extracts an existing project archive into the current workspace and opens the main project.

Parameters:  filename : str[¶](#ApiClient.ProjectApi.OpenProjectFromArchive.filename "Permalink to this definition")  
Absolute path to the project archive file.

Returns:  Opened main project from extracted project archive

Return type:  [`Project`](ProjectApi/Project.md#ApiClient.Project "ApiClient.Project (Python class) — ProjectApi.CreateProject")

SearchProjects(*[searchCriteria](#ApiClient.ProjectApi.SearchProjects.searchCriteria "ApiClient.ProjectApi.SearchProjects.searchCriteria (Python parameter) — The search criteria expressed in the ecu.test filter syntax.")*, *[useExtendedMode](#ApiClient.ProjectApi.SearchProjects.useExtendedMode "ApiClient.ProjectApi.SearchProjects.useExtendedMode (Python parameter) — If True, extended search strings are enabled.")=`False`*)[¶](#ApiClient.ProjectApi.SearchProjects "Link to this definition")  
Searches the current workspace and library workspaces for projects matching the given search criteria.

Parameters:  searchCriteria : str[¶](#ApiClient.ProjectApi.SearchProjects.searchCriteria "Permalink to this definition")  
The search criteria expressed in the ecu.test filter syntax. See section “Handling” =\> “Filter” of the ecu.test User Documentation.

useExtendedMode : boolean[¶](#ApiClient.ProjectApi.SearchProjects.useExtendedMode "Permalink to this definition")  
If True, extended search strings are enabled. The default is False, meaning each word in the searchCriteria will be enclosed by wildcards and mapped to the filename. (e.g. “hello world” =\> “Name = ‘\*hello\*’ and Name = ‘\*world\*’”)

Returns:  All matching projects. If no project matches, an emtpy list is returned.

Return type:  list[[`Project`](ProjectApi/Project.md#ApiClient.Project "ApiClient.Project (Python class) — ProjectApi.CreateProject")]

Raises:  
**ApiError** – If the searchCriteria has an illegal syntax.

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
