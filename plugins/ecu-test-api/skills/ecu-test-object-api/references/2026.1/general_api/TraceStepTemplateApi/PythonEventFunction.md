[![logo](../../_static/ecu.test.svg)](../../index.html "API  documentation") API documentation

[ Internal APIs ](../api.md)

[ Advanced operations of package variable types ](../variabledatastructures.md)

[ Advanced properties of bus-related objects ](../busdatastructures.md)

[ Bus related objects of trace analysis ](../busdatastructuresTraceanalysis.md)

[ Advanced properties of diagnostics-related objects ](../diagdatastructures.md)

[ Diagnostics related objects of trace analysis ](../diagdatastructuresTraceanalysis.md)

[ Advanced properties of media-related objects ](../mediadatastructures.md)

[ Advanced properties of DLT logging-related objects ](../dltdatastructures.md)

[ COM API ](../com-api.md)

[ REST API ](../rest-api.md)

[ Report API ](../apireport.md)

[ Object API ](../objectApi.md)

Object API

[ API entry points ](../objectApi.md#api-entry-points)

API entry points

[ API for Analysis Jobs ](../AnalysisJobApi.md)

[ API for Artifacts ](../ArtifactApi.md)

[ API for Project Components ](../ComponentApi.md)

[ API for Configurations ](../ConfigurationApi.md)

[ API for Expectations ](../ExpectationApi.md)

[ API for Expressions ](../ExpressionApi.md)

[ API for Global Mappings ](../GlobalMappingApi.md)

[ API for Mappings ](../MappingApi.md)

[ API for Multimedia Objects ](../MultimediaApi.md)

[ API for Packages ](../PackageApi.md)

[ API for Parameters ](../ParameterApi.md)

[ API for Projects ](../ProjectApi.md)

[ API for Relations ](../RelationApi.md)

[ API for Reports ](../ReportApi.md)

[ API for Report Filters ](../ReportFilterApi.md)

[ API for Settings ](../SettingsApi.md)

[ API for Signals ](../SignalApi.md)

[ API for Signal Descriptions ](../SignalDescriptionApi.md)

[ API for Signal Recordings ](../SignalRecordingApi.md)

[ API for Symbols ](../SymbolApi.md)

[ API for Test Steps ](../TestStepApi.md)

[ API for Touch Inputs ](../TouchInputApi.md)

[ API for Trace Analyses ](../TraceAnalysisApi.md)

[ API for Trace Files ](../TraceFileApi.md)

[ API for Trace Step Templates ](../TraceStepTemplateApi.md)

API for Trace Step Templates

PythonEventFunction [ PythonEventFunction ](#)

PythonEventFunction

- [C PythonEventFunction ](#ApiClient.PythonEventFunction)
  - [M Clone ](#ApiClient.PythonEventFunction.Clone)
  - [M GetCode ](#ApiClient.PythonEventFunction.GetCode)
  - [M GetName ](#ApiClient.PythonEventFunction.GetName)
  - [M GetSignalNames ](#ApiClient.PythonEventFunction.GetSignalNames)

[ TraceStepTemplate ](TraceStepTemplate.md)

[ TraceStepTemplatePythonEvent ](TraceStepTemplatePythonEvent.md)

[ API for Variables ](../VariableApi.md)

[ API for Workspaces ](../WorkspaceApi.md)

[ Trace Analysis API ](../../TraceAnalysisAPI/index.md)

[ Generator APIs ](../../generators/index.md)

[ Tools ](../../tools/index.md)

[ User test management ](../../userTestmanagement/index.md)

[ UserUtility API ](../../user-utility/user-utility.md)

[ Utility Examples ](../../user-utility/example-utilities.md)

PythonEventFunction

- [C PythonEventFunction ](#ApiClient.PythonEventFunction)
  - [M Clone ](#ApiClient.PythonEventFunction.Clone)
  - [M GetCode ](#ApiClient.PythonEventFunction.GetCode)
  - [M GetName ](#ApiClient.PythonEventFunction.GetName)
  - [M GetSignalNames ](#ApiClient.PythonEventFunction.GetSignalNames)

# PythonEventFunction[¶](#pythoneventfunction "Link to this heading")

*class* PythonEventFunction[¶](#ApiClient.PythonEventFunction "Link to this definition")  
Clone()[¶](#ApiClient.PythonEventFunction.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`PythonEventFunction`](#ApiClient.PythonEventFunction "ApiClient.PythonEventFunction (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")

GetCode()[¶](#ApiClient.PythonEventFunction.GetCode "Link to this definition")  
Returns the code used in the function.

Returns:  The code

Return type:  str

GetName()[¶](#ApiClient.PythonEventFunction.GetName "Link to this definition")  
Returns the name of the function.

Returns:  The name

Return type:  str

GetSignalNames()[¶](#ApiClient.PythonEventFunction.GetSignalNames "Link to this definition")  
Returns the names of the registered signals.

Returns:  The registered signal names

Return type:  list[str]

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
