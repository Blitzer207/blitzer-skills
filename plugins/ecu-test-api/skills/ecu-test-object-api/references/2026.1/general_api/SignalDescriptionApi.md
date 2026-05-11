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

[ API for Signal Descriptions ](#)

API for Signal Descriptions

- [ SignalDescriptionFile ](SignalDescriptionApi/SignalDescriptionFile.md)

API for Signal Descriptions [ API for Signal Descriptions ](#)

API for Signal Descriptions

- [C SignalDescriptionApi ](#ApiClient.SignalDescriptionApi)
  - [A SignalApi ](#ApiClient.SignalDescriptionApi.SignalApi)
  - [M CreateSignalDescriptionFile ](#ApiClient.SignalDescriptionApi.CreateSignalDescriptionFile)
  - [M OpenSignalDescriptionFile ](#ApiClient.SignalDescriptionApi.OpenSignalDescriptionFile)
- [ SignalDescriptionFile ](SignalDescriptionApi/SignalDescriptionFile.md)

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

API for Signal Descriptions

- [C SignalDescriptionApi ](#ApiClient.SignalDescriptionApi)
  - [A SignalApi ](#ApiClient.SignalDescriptionApi.SignalApi)
  - [M CreateSignalDescriptionFile ](#ApiClient.SignalDescriptionApi.CreateSignalDescriptionFile)
  - [M OpenSignalDescriptionFile ](#ApiClient.SignalDescriptionApi.OpenSignalDescriptionFile)

# API for Signal Descriptions[¶](#api-for-signal-descriptions "Link to this heading")

Part of the [Object based program API](objectApi.md#objectapi).

*class* SignalDescriptionApi[¶](#ApiClient.SignalDescriptionApi "Link to this definition")  
API to access signal description files

Returned by

- [`ApiClient.SignalDescriptionApi`](objectApi.md#ApiClient.ApiClient.SignalDescriptionApi "ApiClient.ApiClient.SignalDescriptionApi (Python attribute) — Returns the SignalDescriptionApi namespace.")

SignalApi[¶](#ApiClient.SignalDescriptionApi.SignalApi "Link to this definition")  
Returns the SignalApi namespace.

Returns:  SignalApi namespace

Return type:  [`SignalApi`](SignalApi.md#ApiClient.SignalApi "ApiClient.SignalApi (Python class) — SignalDescriptionApi.SignalApi")

CreateSignalDescriptionFile()[¶](#ApiClient.SignalDescriptionApi.CreateSignalDescriptionFile "Link to this definition")  
Creates a new sti or stz file.

Returns:  Signal description

Return type:  [`SignalDescriptionFile`](SignalDescriptionApi/SignalDescriptionFile.md#ApiClient.SignalDescriptionFile "ApiClient.SignalDescriptionFile (Python class) — SignalDescriptionApi.CreateSignalDescriptionFile")

OpenSignalDescriptionFile(*[filename](#ApiClient.SignalDescriptionApi.OpenSignalDescriptionFile.filename "ApiClient.SignalDescriptionApi.OpenSignalDescriptionFile.filename (Python parameter) — Name of the signal description file to open")*, *[upgradeLegacyFile](#ApiClient.SignalDescriptionApi.OpenSignalDescriptionFile.upgradeLegacyFile "ApiClient.SignalDescriptionApi.OpenSignalDescriptionFile.upgradeLegacyFile (Python parameter) — Selects whether a sti in version 1.0 should be upgraded or if loading should be aborted.")=`True`*)[¶](#ApiClient.SignalDescriptionApi.OpenSignalDescriptionFile "Link to this definition")  
Opens an existing sti or stz file.

Parameters:  filename : str[¶](#ApiClient.SignalDescriptionApi.OpenSignalDescriptionFile.filename "Permalink to this definition")  
Name of the signal description file to open

upgradeLegacyFile : bool[¶](#ApiClient.SignalDescriptionApi.OpenSignalDescriptionFile.upgradeLegacyFile "Permalink to this definition")  
Selects whether a sti in version 1.0 should be upgraded or if loading should be aborted. A backup copy of the original file is saved at the same location with the suffix “.bak”.

Returns:  Signal description

Return type:  [`SignalDescriptionFile`](SignalDescriptionApi/SignalDescriptionFile.md#ApiClient.SignalDescriptionFile "ApiClient.SignalDescriptionFile (Python class) — SignalDescriptionApi.CreateSignalDescriptionFile")

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
