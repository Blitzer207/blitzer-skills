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

[ API for Trace Files ](#)

API for Trace Files

- [ Device ](TraceFileApi/Device.md)
- [ TraceFile ](TraceFileApi/TraceFile.md)

API for Trace Files [ API for Trace Files ](#)

API for Trace Files

- [C TraceFileApi ](#ApiClient.TraceFileApi)
  - [M OpenTraceFile ](#ApiClient.TraceFileApi.OpenTraceFile)
- [ Device ](TraceFileApi/Device.md)
- [ TraceFile ](TraceFileApi/TraceFile.md)

[ API for Trace Step Templates ](TraceStepTemplateApi.md)

[ API for Variables ](VariableApi.md)

[ API for Workspaces ](WorkspaceApi.md)

[ Trace Analysis API ](../TraceAnalysisAPI/index.md)

[ Generator APIs ](../generators/index.md)

[ Tools ](../tools/index.md)

[ User test management ](../userTestmanagement/index.md)

[ UserUtility API ](../user-utility/user-utility.md)

[ Utility Examples ](../user-utility/example-utilities.md)

API for Trace Files

- [C TraceFileApi ](#ApiClient.TraceFileApi)
  - [M OpenTraceFile ](#ApiClient.TraceFileApi.OpenTraceFile)

# API for Trace Files[¶](#api-for-trace-files "Link to this heading")

Part of the [Object based program API](objectApi.md#objectapi).

*class* TraceFileApi[¶](#ApiClient.TraceFileApi "Link to this definition")  
API to access trace files

Returned by

- [`ApiClient.TraceFileApi`](objectApi.md#ApiClient.ApiClient.TraceFileApi "ApiClient.ApiClient.TraceFileApi (Python attribute) — Returns the TraceFileApi namespace.")

OpenTraceFile(*[filename](#ApiClient.TraceFileApi.OpenTraceFile.filename "ApiClient.TraceFileApi.OpenTraceFile.filename (Python parameter) — Name of the trace file to open")*)[¶](#ApiClient.TraceFileApi.OpenTraceFile "Link to this definition")  
Opens an existing recording file.

Parameters:  filename : str[¶](#ApiClient.TraceFileApi.OpenTraceFile.filename "Permalink to this definition")  
Name of the trace file to open

Returns:  Trace file

Return type:  [`TraceFile`](TraceFileApi/TraceFile.md#ApiClient.TraceFile "ApiClient.TraceFile (Python class) — TraceFileApi.OpenTraceFile")

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
