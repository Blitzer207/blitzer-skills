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

[ PythonEventFunction ](PythonEventFunction.md)

TraceStepTemplate [ TraceStepTemplate ](#)

TraceStepTemplate

- [C TraceStepTemplate ](#ApiClient.TraceStepTemplate)
  - [M Clone ](#ApiClient.TraceStepTemplate.Clone)
  - [M GetDescription ](#ApiClient.TraceStepTemplate.GetDescription)
  - [M GetName ](#ApiClient.TraceStepTemplate.GetName)
  - [M GetParameterDefaultValues ](#ApiClient.TraceStepTemplate.GetParameterDefaultValues)
  - [M GetParameterDescriptions ](#ApiClient.TraceStepTemplate.GetParameterDescriptions)
  - [M GetParameterDirections ](#ApiClient.TraceStepTemplate.GetParameterDirections)
  - [M GetParameterNames ](#ApiClient.TraceStepTemplate.GetParameterNames)
  - [M GetParameterTypes ](#ApiClient.TraceStepTemplate.GetParameterTypes)
  - [M GetSignalDescriptions ](#ApiClient.TraceStepTemplate.GetSignalDescriptions)
  - [M GetSignalDirections ](#ApiClient.TraceStepTemplate.GetSignalDirections)
  - [M GetSignalNames ](#ApiClient.TraceStepTemplate.GetSignalNames)
  - [M GetSignalOptionalFlags ](#ApiClient.TraceStepTemplate.GetSignalOptionalFlags)
  - [M GetType ](#ApiClient.TraceStepTemplate.GetType)
  - [M IsBroken ](#ApiClient.TraceStepTemplate.IsBroken)
  - [M IsMissing ](#ApiClient.TraceStepTemplate.IsMissing)

[ TraceStepTemplatePythonEvent ](TraceStepTemplatePythonEvent.md)

[ API for Variables ](../VariableApi.md)

[ API for Workspaces ](../WorkspaceApi.md)

[ Trace Analysis API ](../../TraceAnalysisAPI/index.md)

[ Generator APIs ](../../generators/index.md)

[ Tools ](../../tools/index.md)

[ User test management ](../../userTestmanagement/index.md)

[ UserUtility API ](../../user-utility/user-utility.md)

[ Utility Examples ](../../user-utility/example-utilities.md)

TraceStepTemplate

- [C TraceStepTemplate ](#ApiClient.TraceStepTemplate)
  - [M Clone ](#ApiClient.TraceStepTemplate.Clone)
  - [M GetDescription ](#ApiClient.TraceStepTemplate.GetDescription)
  - [M GetName ](#ApiClient.TraceStepTemplate.GetName)
  - [M GetParameterDefaultValues ](#ApiClient.TraceStepTemplate.GetParameterDefaultValues)
  - [M GetParameterDescriptions ](#ApiClient.TraceStepTemplate.GetParameterDescriptions)
  - [M GetParameterDirections ](#ApiClient.TraceStepTemplate.GetParameterDirections)
  - [M GetParameterNames ](#ApiClient.TraceStepTemplate.GetParameterNames)
  - [M GetParameterTypes ](#ApiClient.TraceStepTemplate.GetParameterTypes)
  - [M GetSignalDescriptions ](#ApiClient.TraceStepTemplate.GetSignalDescriptions)
  - [M GetSignalDirections ](#ApiClient.TraceStepTemplate.GetSignalDirections)
  - [M GetSignalNames ](#ApiClient.TraceStepTemplate.GetSignalNames)
  - [M GetSignalOptionalFlags ](#ApiClient.TraceStepTemplate.GetSignalOptionalFlags)
  - [M GetType ](#ApiClient.TraceStepTemplate.GetType)
  - [M IsBroken ](#ApiClient.TraceStepTemplate.IsBroken)
  - [M IsMissing ](#ApiClient.TraceStepTemplate.IsMissing)

# TraceStepTemplate[¶](#tracesteptemplate "Link to this heading")

*class* TraceStepTemplate[¶](#ApiClient.TraceStepTemplate "Link to this definition")  
Returned by

- [`TraceStepTemplateApi.OpenTraceStepTemplate`](../TraceStepTemplateApi.md#ApiClient.TraceStepTemplateApi.OpenTraceStepTemplate "ApiClient.TraceStepTemplateApi.OpenTraceStepTemplate (Python method) — Opens a trace step template file.")

- [`TraceStepTemplateApi.SearchTraceStepTemplates`](../TraceStepTemplateApi.md#ApiClient.TraceStepTemplateApi.SearchTraceStepTemplates "ApiClient.TraceStepTemplateApi.SearchTraceStepTemplates (Python method) — Searches the current workspace and library workspaces for trace step templates matching the given search criteria.")

Clone()[¶](#ApiClient.TraceStepTemplate.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`TraceStepTemplate`](#ApiClient.TraceStepTemplate "ApiClient.TraceStepTemplate (Python class) — TraceStepTemplateApi.OpenTraceStepTemplate")

GetDescription()[¶](#ApiClient.TraceStepTemplate.GetDescription "Link to this definition")  
Returns the description of the trace step template.

Returns:  The Description

Return type:  str

GetName()[¶](#ApiClient.TraceStepTemplate.GetName "Link to this definition")  
Returns the name of the trace step template.

Returns:  The name

Return type:  str

GetParameterDefaultValues()[¶](#ApiClient.TraceStepTemplate.GetParameterDefaultValues "Link to this definition")  
Returns text representation of the default parameter values of the trace step template. Those values are applied of value None is passed to a trace step.

Returns:  The text representations of the default values of all parameters

Return type:  list[str]

GetParameterDescriptions()[¶](#ApiClient.TraceStepTemplate.GetParameterDescriptions "Link to this definition")  
Returns the descriptions of all parameters of a trace step template.

Returns:  The descriptions of all parameters

Return type:  list[str]

GetParameterDirections()[¶](#ApiClient.TraceStepTemplate.GetParameterDirections "Link to this definition")  
Returns the direction of all parameters of a trace step template.

Returns:  The direction of all parameters

Return type:  list[str]

GetParameterNames()[¶](#ApiClient.TraceStepTemplate.GetParameterNames "Link to this definition")  
Returns the names of all parameters of a trace step template.

Returns:  The names of all parameters

Return type:  list[str]

GetParameterTypes()[¶](#ApiClient.TraceStepTemplate.GetParameterTypes "Link to this definition")  
Returns the types of all parameters of a trace step template.

Returns:  The types of all parameters

Return type:  list[str]

GetSignalDescriptions()[¶](#ApiClient.TraceStepTemplate.GetSignalDescriptions "Link to this definition")  
Returns the descriptions of all signals of a trace step template.

Returns:  The Descriptions of all signals

Return type:  list[str]

GetSignalDirections()[¶](#ApiClient.TraceStepTemplate.GetSignalDirections "Link to this definition")  
Returns the direction of all signals of a trace step template.

Returns:  The direction of all signals

Return type:  list[str]

GetSignalNames()[¶](#ApiClient.TraceStepTemplate.GetSignalNames "Link to this definition")  
Returns the names of all signals of the trace step template.

Returns:  The Names of all signals

Return type:  list[str]

GetSignalOptionalFlags()[¶](#ApiClient.TraceStepTemplate.GetSignalOptionalFlags "Link to this definition")  
Returns the “is optional” flags of all signals of a trace step template.

Returns:  The “is optional” flags of all signals

Return type:  list[boolean]

GetType()[¶](#ApiClient.TraceStepTemplate.GetType "Link to this definition")  
Returns the specific type of the trace step template, i.e.

- “TraceStepTemplatePythonEvent”

- “TraceStepTemplatePythonEventDeprecated”

- “TraceStepTemplatePythonStream”

- “TraceStepTemplateTimingDiagram”

- “TraceStepTemplateLogic”

- “TraceStepTemplateNumpy”

- “TraceStepTemplateInternal”

- “TraceStepTemplateMissing”

- “TraceStepTemplateBroken”

If the particular type cannot be resolved, the method will return

- “TraceStepTemplate”

Returns:  The type of the template

Return type:  str

IsBroken()[¶](#ApiClient.TraceStepTemplate.IsBroken "Link to this definition")  
Returns whether the trace step template represents a broken trace step template.

Note:  
This status is set initially and will not be changed if the trace step template is fixed later on. You need to close and re-open the package, obtain the trace step from the re-opened package using `Package.GetTraceAnalyses`, [`TraceStepContainer.GetTraceSteps()`](../TraceAnalysisApi/TraceStepContainer.md#ApiClient.TraceStepContainer.GetTraceSteps "ApiClient.TraceStepContainer.GetTraceSteps (Python method) — Returns either direct or all children of the trace step."), etc., and call [`TemplateBasedTraceStep.GetTemplate()`](../TraceAnalysisApi/TemplateBasedTraceStep.md#ApiClient.TemplateBasedTraceStep.GetTemplate "ApiClient.TemplateBasedTraceStep.GetTemplate (Python method) — Returns the assigned trace step template.") on the new instance.

Returns:  True if the trace step template is broken

Return type:  boolean

IsMissing()[¶](#ApiClient.TraceStepTemplate.IsMissing "Link to this definition")  
Returns whether the trace step template represents a missing trace step template.

Note:  
This status is set initially and will not be changed if the trace step template becomes available later on. You need to close and re-open the package, obtain the trace step from the re-opened package using `Package.GetTraceAnalyses`, [`TraceStepContainer.GetTraceSteps()`](../TraceAnalysisApi/TraceStepContainer.md#ApiClient.TraceStepContainer.GetTraceSteps "ApiClient.TraceStepContainer.GetTraceSteps (Python method) — Returns either direct or all children of the trace step."), etc., and call [`TemplateBasedTraceStep.GetTemplate()`](../TraceAnalysisApi/TemplateBasedTraceStep.md#ApiClient.TemplateBasedTraceStep.GetTemplate "ApiClient.TemplateBasedTraceStep.GetTemplate (Python method) — Returns the assigned trace step template.") on the new instance.

Returns:  True if the file of the trace step template is not found

Return type:  boolean

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
