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

[ API for Symbols ](#)

API for Symbols

- [ ConstSymbol ](SymbolApi/ConstSymbol.md)
- [ SignalSymbol ](SymbolApi/SignalSymbol.md)
- [ StringSymbol ](SymbolApi/StringSymbol.md)

API for Symbols [ API for Symbols ](#)

API for Symbols

- [C SymbolApi ](#ApiClient.SymbolApi)
  - [M CreateConstSymbol ](#ApiClient.SymbolApi.CreateConstSymbol)
  - [M CreateSignalSymbol ](#ApiClient.SymbolApi.CreateSignalSymbol)
  - [M CreateStringSymbol ](#ApiClient.SymbolApi.CreateStringSymbol)
- [ ConstSymbol ](SymbolApi/ConstSymbol.md)
- [ SignalSymbol ](SymbolApi/SignalSymbol.md)
- [ StringSymbol ](SymbolApi/StringSymbol.md)

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

API for Symbols

- [C SymbolApi ](#ApiClient.SymbolApi)
  - [M CreateConstSymbol ](#ApiClient.SymbolApi.CreateConstSymbol)
  - [M CreateSignalSymbol ](#ApiClient.SymbolApi.CreateSignalSymbol)
  - [M CreateStringSymbol ](#ApiClient.SymbolApi.CreateStringSymbol)

# API for Symbols[¶](#api-for-symbols "Link to this heading")

Part of the [Object based program API](objectApi.md#objectapi).

*class* SymbolApi[¶](#ApiClient.SymbolApi "Link to this definition")  
Returned by

- [`SignalApi.SymbolApi`](SignalApi.md#ApiClient.SignalApi.SymbolApi "ApiClient.SignalApi.SymbolApi (Python attribute) — Returns the SymbolApi namespace.")

CreateConstSymbol(*[expression](#ApiClient.SymbolApi.CreateConstSymbol.expression "ApiClient.SymbolApi.CreateConstSymbol.expression (Python parameter) — the expression")*)[¶](#ApiClient.SymbolApi.CreateConstSymbol "Link to this definition")  
Creates constant symbol

Parameters:  expression : str[¶](#ApiClient.SymbolApi.CreateConstSymbol.expression "Permalink to this definition")  
the expression

Returns:  New ConstSymbol

Return type:  [`ConstSymbol`](SymbolApi/ConstSymbol.md#ApiClient.ConstSymbol "ApiClient.ConstSymbol (Python class) — SymbolApi.CreateConstSymbol")

CreateSignalSymbol(*[signalName](#ApiClient.SymbolApi.CreateSignalSymbol.signalName "ApiClient.SymbolApi.CreateSignalSymbol.signalName (Python parameter) — The signal description name")*)[¶](#ApiClient.SymbolApi.CreateSignalSymbol "Link to this definition")  
Creates string symbol

Parameters:  signalName : str[¶](#ApiClient.SymbolApi.CreateSignalSymbol.signalName "Permalink to this definition")  
The signal description name

Returns:  New SignalSymbol

Return type:  [`SignalSymbol`](SymbolApi/SignalSymbol.md#ApiClient.SignalSymbol "ApiClient.SignalSymbol (Python class) — SymbolApi.CreateSignalSymbol")

CreateStringSymbol(*[value](#ApiClient.SymbolApi.CreateStringSymbol.value "ApiClient.SymbolApi.CreateStringSymbol.value (Python parameter) — the string symbol name")*)[¶](#ApiClient.SymbolApi.CreateStringSymbol "Link to this definition")  
Creates string symbol

Parameters:  value : str[¶](#ApiClient.SymbolApi.CreateStringSymbol.value "Permalink to this definition")  
the string symbol name

Returns:  New StringSymbol

Return type:  [`StringSymbol`](SymbolApi/StringSymbol.md#ApiClient.StringSymbol "ApiClient.StringSymbol (Python class) — SymbolApi.CreateStringSymbol")

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
