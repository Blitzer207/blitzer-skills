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

[ API for Multimedia Objects ](#)

API for Multimedia Objects

- [ Mask ](MultimediaApi/Mask.md)

API for Multimedia Objects [ API for Multimedia Objects ](#)

API for Multimedia Objects

- [C MultimediaApi ](#ApiClient.MultimediaApi)
  - [A TouchInputApi ](#ApiClient.MultimediaApi.TouchInputApi)
  - [M CreateMask ](#ApiClient.MultimediaApi.CreateMask)
  - [M OpenMask ](#ApiClient.MultimediaApi.OpenMask)
- [ Mask ](MultimediaApi/Mask.md)

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

API for Multimedia Objects

- [C MultimediaApi ](#ApiClient.MultimediaApi)
  - [A TouchInputApi ](#ApiClient.MultimediaApi.TouchInputApi)
  - [M CreateMask ](#ApiClient.MultimediaApi.CreateMask)
  - [M OpenMask ](#ApiClient.MultimediaApi.OpenMask)

# API for Multimedia Objects[¶](#api-for-multimedia-objects "Link to this heading")

Part of the [Object based program API](objectApi.md#objectapi).

*class* MultimediaApi[¶](#ApiClient.MultimediaApi "Link to this definition")  
Returned by

- [`ApiClient.MultimediaApi`](objectApi.md#ApiClient.ApiClient.MultimediaApi "ApiClient.ApiClient.MultimediaApi (Python attribute) — Returns the MultimediaApi namespace.")

TouchInputApi[¶](#ApiClient.MultimediaApi.TouchInputApi "Link to this definition")  
Returns the TouchInputApi namespace.

Returns:  TouchInputApi namespace

Return type:  [`TouchInputApi`](TouchInputApi.md#ApiClient.TouchInputApi "ApiClient.TouchInputApi (Python class) — API to create touch input actions")

CreateMask(*[x](#ApiClient.MultimediaApi.CreateMask.x "ApiClient.MultimediaApi.CreateMask.x (Python parameter) — Position of left edge")=`0`*, *[y](#ApiClient.MultimediaApi.CreateMask.y "ApiClient.MultimediaApi.CreateMask.y (Python parameter) — Position of upper edge")=`0`*, *[width](#ApiClient.MultimediaApi.CreateMask.width "ApiClient.MultimediaApi.CreateMask.width (Python parameter) — Mask width")=`0`*, *[height](#ApiClient.MultimediaApi.CreateMask.height "ApiClient.MultimediaApi.CreateMask.height (Python parameter) — Mask height")=`0`*)[¶](#ApiClient.MultimediaApi.CreateMask "Link to this definition")  
Create a new image mask.

Parameters:  x : int[¶](#ApiClient.MultimediaApi.CreateMask.x "Permalink to this definition")  
Position of left edge

y : int[¶](#ApiClient.MultimediaApi.CreateMask.y "Permalink to this definition")  
Position of upper edge

width : int[¶](#ApiClient.MultimediaApi.CreateMask.width "Permalink to this definition")  
Mask width

height : int[¶](#ApiClient.MultimediaApi.CreateMask.height "Permalink to this definition")  
Mask height

Returns:  A new mask

Return type:  [`Mask`](MultimediaApi/Mask.md#ApiClient.Mask "ApiClient.Mask (Python class) — MultimediaApi.CreateMask")

OpenMask(*[filePath](#ApiClient.MultimediaApi.OpenMask.filePath "ApiClient.MultimediaApi.OpenMask.filePath (Python parameter) — Path to the mask file.")*)[¶](#ApiClient.MultimediaApi.OpenMask "Link to this definition")  
Opens an existing image mask.

Parameters:  filePath : str[¶](#ApiClient.MultimediaApi.OpenMask.filePath "Permalink to this definition")  
Path to the mask file.

Returns:  The loaded mask

Return type:  [`Mask`](MultimediaApi/Mask.md#ApiClient.Mask "ApiClient.Mask (Python class) — MultimediaApi.CreateMask")

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
