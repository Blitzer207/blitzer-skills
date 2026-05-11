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

[ API for Parameters ](#)

API for Parameters

- [ GlobalConstantsDefinition ](ParameterApi/GlobalConstantsDefinition.md)
- [ PackageParametersDefinition ](ParameterApi/PackageParametersDefinition.md)

API for Parameters [ API for Parameters ](#)

API for Parameters

- [C ParameterApi ](#ApiClient.ParameterApi)
  - [M CreateGlobalConstantsDefinition ](#ApiClient.ParameterApi.CreateGlobalConstantsDefinition)
  - [M CreatePackageParametersDefinition ](#ApiClient.ParameterApi.CreatePackageParametersDefinition)
  - [M GetChangesForGlobalConstantsDefinitions ](#ApiClient.ParameterApi.GetChangesForGlobalConstantsDefinitions)
  - [M GetChangesForPackageParametersDefinitions ](#ApiClient.ParameterApi.GetChangesForPackageParametersDefinitions)
  - [M OpenGlobalConstantsDefinition ](#ApiClient.ParameterApi.OpenGlobalConstantsDefinition)
  - [M OpenPackageParametersDefinition ](#ApiClient.ParameterApi.OpenPackageParametersDefinition)
  - [M SearchGlobalConstantsDefinitions ](#ApiClient.ParameterApi.SearchGlobalConstantsDefinitions)
  - [M SearchPackageParametersDefinitions ](#ApiClient.ParameterApi.SearchPackageParametersDefinitions)
- [ GlobalConstantsDefinition ](ParameterApi/GlobalConstantsDefinition.md)
- [ PackageParametersDefinition ](ParameterApi/PackageParametersDefinition.md)

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

API for Parameters

- [C ParameterApi ](#ApiClient.ParameterApi)
  - [M CreateGlobalConstantsDefinition ](#ApiClient.ParameterApi.CreateGlobalConstantsDefinition)
  - [M CreatePackageParametersDefinition ](#ApiClient.ParameterApi.CreatePackageParametersDefinition)
  - [M GetChangesForGlobalConstantsDefinitions ](#ApiClient.ParameterApi.GetChangesForGlobalConstantsDefinitions)
  - [M GetChangesForPackageParametersDefinitions ](#ApiClient.ParameterApi.GetChangesForPackageParametersDefinitions)
  - [M OpenGlobalConstantsDefinition ](#ApiClient.ParameterApi.OpenGlobalConstantsDefinition)
  - [M OpenPackageParametersDefinition ](#ApiClient.ParameterApi.OpenPackageParametersDefinition)
  - [M SearchGlobalConstantsDefinitions ](#ApiClient.ParameterApi.SearchGlobalConstantsDefinitions)
  - [M SearchPackageParametersDefinitions ](#ApiClient.ParameterApi.SearchPackageParametersDefinitions)

# API for Parameters[¶](#api-for-parameters "Link to this heading")

Part of the [Object based program API](objectApi.md#objectapi).

*class* ParameterApi[¶](#ApiClient.ParameterApi "Link to this definition")  
API to access parameter files

Returned by

- [`ApiClient.ParameterApi`](objectApi.md#ApiClient.ApiClient.ParameterApi "ApiClient.ApiClient.ParameterApi (Python attribute) — Returns the ParameterApi namespace.")

CreateGlobalConstantsDefinition()[¶](#ApiClient.ParameterApi.CreateGlobalConstantsDefinition "Link to this definition")  
Creates a new global constants definition.

Returns:  New empty global constants definition

Return type:  [`GlobalConstantsDefinition`](ParameterApi/GlobalConstantsDefinition.md#ApiClient.GlobalConstantsDefinition "ApiClient.GlobalConstantsDefinition (Python class) — ParameterApi.CreateGlobalConstantsDefinition")

CreatePackageParametersDefinition()[¶](#ApiClient.ParameterApi.CreatePackageParametersDefinition "Link to this definition")  
Creates a new package parameters definition.

Returns:  New empty package parameters definition

Return type:  [`PackageParametersDefinition`](ParameterApi/PackageParametersDefinition.md#ApiClient.PackageParametersDefinition "ApiClient.PackageParametersDefinition (Python class) — ParameterApi.CreatePackageParametersDefinition")

GetChangesForGlobalConstantsDefinitions(*[oldConstDefinition](#ApiClient.ParameterApi.GetChangesForGlobalConstantsDefinitions.oldConstDefinition "ApiClient.ParameterApi.GetChangesForGlobalConstantsDefinitions.oldConstDefinition (Python parameter) — The old constants definition to compare.")*, *[newConstDefinition](#ApiClient.ParameterApi.GetChangesForGlobalConstantsDefinitions.newConstDefinition "ApiClient.ParameterApi.GetChangesForGlobalConstantsDefinitions.newConstDefinition (Python parameter) — The new constants definition to compare.")*)[¶](#ApiClient.ParameterApi.GetChangesForGlobalConstantsDefinitions "Link to this definition")  
Get the changes that exist between two given constants definitions.

Parameters:  oldConstDefinition[¶](#ApiClient.ParameterApi.GetChangesForGlobalConstantsDefinitions.oldConstDefinition "Permalink to this definition")  
The old constants definition to compare.

newConstDefinition[¶](#ApiClient.ParameterApi.GetChangesForGlobalConstantsDefinitions.newConstDefinition "Permalink to this definition")  
The new constants definition to compare.

Returns:  The changes that exist between the two constants definitions.

Return type:  list[[`Change`](ConfigurationApi/Change.md#ApiClient.Change "ApiClient.Change (Python class) — Represents a change between an old element and a new element. Both elements have the same type, e.g. a certain test step and stem from two different Objects, e.g. an old Package a new Package.")]

GetChangesForPackageParametersDefinitions(*[oldParamDefinition](#ApiClient.ParameterApi.GetChangesForPackageParametersDefinitions.oldParamDefinition "ApiClient.ParameterApi.GetChangesForPackageParametersDefinitions.oldParamDefinition (Python parameter) — The old package parameters definition to compare.")*, *[newParamDefinition](#ApiClient.ParameterApi.GetChangesForPackageParametersDefinitions.newParamDefinition "ApiClient.ParameterApi.GetChangesForPackageParametersDefinitions.newParamDefinition (Python parameter) — The new package parameters definition to compare.")*)[¶](#ApiClient.ParameterApi.GetChangesForPackageParametersDefinitions "Link to this definition")  
Get the differences that exist between two given package parameters definitions.

Parameters:  oldParamDefinition[¶](#ApiClient.ParameterApi.GetChangesForPackageParametersDefinitions.oldParamDefinition "Permalink to this definition")  
The old package parameters definition to compare.

newParamDefinition[¶](#ApiClient.ParameterApi.GetChangesForPackageParametersDefinitions.newParamDefinition "Permalink to this definition")  
The new package parameters definition to compare.

Returns:  The differences that exist between the two package parameters definitions.

Return type:  list[[`Change`](ConfigurationApi/Change.md#ApiClient.Change "ApiClient.Change (Python class) — Represents a change between an old element and a new element. Both elements have the same type, e.g. a certain test step and stem from two different Objects, e.g. an old Package a new Package.")]

OpenGlobalConstantsDefinition(*[filename](#ApiClient.ParameterApi.OpenGlobalConstantsDefinition.filename "ApiClient.ParameterApi.OpenGlobalConstantsDefinition.filename (Python parameter) — File name of the global constants definition file; Either absolute or relative to the 'Parameter' directory")*)[¶](#ApiClient.ParameterApi.OpenGlobalConstantsDefinition "Link to this definition")  
Opens an existing global constants definition file (\*.gcd).

Parameters:  filename : str[¶](#ApiClient.ParameterApi.OpenGlobalConstantsDefinition.filename "Permalink to this definition")  
File name of the global constants definition file; Either absolute or relative to the ‘Parameter’ directory

Returns:  Loaded global constants definition

Return type:  [`GlobalConstantsDefinition`](ParameterApi/GlobalConstantsDefinition.md#ApiClient.GlobalConstantsDefinition "ApiClient.GlobalConstantsDefinition (Python class) — ParameterApi.CreateGlobalConstantsDefinition")

Raises:  
**ApiError** – If the global constants definition file (\*.gcd) does not exist.

OpenPackageParametersDefinition(*[filename](#ApiClient.ParameterApi.OpenPackageParametersDefinition.filename "ApiClient.ParameterApi.OpenPackageParametersDefinition.filename (Python parameter) — File name of the package parameters definition file; Either absolute or relative to the 'Parameter' directory")*)[¶](#ApiClient.ParameterApi.OpenPackageParametersDefinition "Link to this definition")  
Opens an existing package parameters definition file (\*.ppd).

Parameters:  filename : str[¶](#ApiClient.ParameterApi.OpenPackageParametersDefinition.filename "Permalink to this definition")  
File name of the package parameters definition file; Either absolute or relative to the ‘Parameter’ directory

Returns:  Loaded package parameters definition

Return type:  [`PackageParametersDefinition`](ParameterApi/PackageParametersDefinition.md#ApiClient.PackageParametersDefinition "ApiClient.PackageParametersDefinition (Python class) — ParameterApi.CreatePackageParametersDefinition")

Raises:  
**ApiError** – If the package parameters definition file (\*.ppd) does not exist.

SearchGlobalConstantsDefinitions(*[searchCriteria](#ApiClient.ParameterApi.SearchGlobalConstantsDefinitions.searchCriteria "ApiClient.ParameterApi.SearchGlobalConstantsDefinitions.searchCriteria (Python parameter) — The search criteria expressed in the ecu.test filter syntax.")*, *[useExtendedMode](#ApiClient.ParameterApi.SearchGlobalConstantsDefinitions.useExtendedMode "ApiClient.ParameterApi.SearchGlobalConstantsDefinitions.useExtendedMode (Python parameter) — If True, extended search strings are enabled.")=`False`*)[¶](#ApiClient.ParameterApi.SearchGlobalConstantsDefinitions "Link to this definition")  
Searches the current workspace and library workspaces for Global Constant Definitions matching the given search criteria.

Parameters:  searchCriteria : str[¶](#ApiClient.ParameterApi.SearchGlobalConstantsDefinitions.searchCriteria "Permalink to this definition")  
The search criteria expressed in the ecu.test filter syntax. See section “Handling” =\> “Filter” of the ecu.test User Documentation.

useExtendedMode : boolean[¶](#ApiClient.ParameterApi.SearchGlobalConstantsDefinitions.useExtendedMode "Permalink to this definition")  
If True, extended search strings are enabled. The default is False, meaning each word in the searchCriteria will be enclosed by wildcards and mapped to the filename. (e.g. “hello world” =\> “Name = ‘\*hello\*’ and Name = ‘\*world\*’”)

Returns:  All matching global constant defintions. If no project matches, an emtpy list is returned.

Return type:  list[[`GlobalConstantsDefinition`](ParameterApi/GlobalConstantsDefinition.md#ApiClient.GlobalConstantsDefinition "ApiClient.GlobalConstantsDefinition (Python class) — ParameterApi.CreateGlobalConstantsDefinition")]

Raises:  
**ApiError** – If the searchCriteria has an illegal syntax.

SearchPackageParametersDefinitions(*[searchCriteria](#ApiClient.ParameterApi.SearchPackageParametersDefinitions.searchCriteria "ApiClient.ParameterApi.SearchPackageParametersDefinitions.searchCriteria (Python parameter) — The search criteria expressed in the ecu.test filter syntax.")*, *[useExtendedMode](#ApiClient.ParameterApi.SearchPackageParametersDefinitions.useExtendedMode "ApiClient.ParameterApi.SearchPackageParametersDefinitions.useExtendedMode (Python parameter) — If True, extended search strings are enabled.")=`False`*)[¶](#ApiClient.ParameterApi.SearchPackageParametersDefinitions "Link to this definition")  
Searches the current workspace and library workspaces for Package Parameter Definitions matching the given search criteria.

Parameters:  searchCriteria : str[¶](#ApiClient.ParameterApi.SearchPackageParametersDefinitions.searchCriteria "Permalink to this definition")  
The search criteria expressed in the ecu.test filter syntax. See section “Handling” =\> “Filter” of the ecu.test User Documentation.

useExtendedMode : boolean[¶](#ApiClient.ParameterApi.SearchPackageParametersDefinitions.useExtendedMode "Permalink to this definition")  
If True, extended search strings are enabled. The default is False, meaning each word in the searchCriteria will be enclosed by wildcards and mapped to the filename. (e.g. “hello world” =\> “Name = ‘\*hello\*’ and Name = ‘\*world\*’”)

Returns:  All matching Package Parameter Definitions. If no file matches, an emtpy list is returned.

Return type:  list[[`PackageParametersDefinition`](ParameterApi/PackageParametersDefinition.md#ApiClient.PackageParametersDefinition "ApiClient.PackageParametersDefinition (Python class) — ParameterApi.CreatePackageParametersDefinition")]

Raises:  
**ApiError** – If the searchCriteria has an illegal syntax.

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
