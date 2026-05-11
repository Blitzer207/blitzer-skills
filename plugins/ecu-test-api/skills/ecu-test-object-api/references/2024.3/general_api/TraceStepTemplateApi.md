# API for Trace Step Templates[¶](#api-for-trace-step-templates "Link to this heading")

Part of the [Object based program API](objectApi.md#objectapi)

## TraceStepTemplateApi[¶](#tracesteptemplateapi "Link to this heading")

*class* TraceStepTemplateApi[¶](#ApiClient.TraceStepTemplateApi "Link to this definition")  
API to access trace step template files

Returned by

- [`ApiClient.TraceStepTemplateApi`](objectApi.md#ApiClient.ApiClient.TraceStepTemplateApi "ApiClient.ApiClient.TraceStepTemplateApi")

OpenTraceStepTemplate(*filename*)[¶](#ApiClient.TraceStepTemplateApi.OpenTraceStepTemplate "Link to this definition")  
Opens a trace step template file.

Parameters:  **filename** (*str*) – Absolute or relative path of the trace step template file. If relative the file must be located in the user defined trace step template directory.

Returns:  Trace step template

Return type:  [`TraceStepTemplate`](#ApiClient.TraceStepTemplate "ApiClient.TraceStepTemplate")

SearchTraceStepTemplates(*searchCriteria*, *useExtendedMode=False*)[¶](#ApiClient.TraceStepTemplateApi.SearchTraceStepTemplates "Link to this definition")  
Searches the current workspace and library workspaces for trace step templates matching the given search criteria.

Parameters:  - **searchCriteria** (*str*) – The search criteria expressed in the ecu.test filter syntax. See section “Handling” =\> “Filter” of the ecu.test User Documentation.

- **useExtendedMode** (*boolean*) – If True, extended search strings are enabled. The default is False, meaning each word in the searchCriteria will be enclosed by wildcards and mapped to the filename. (e.g. “hello world” =\> “Name = ‘\*hello\*’ and Name = ‘\*world\*’”)

Returns:  All matching trace step templates. If no template matches, an empty list is returned.

Return type:  list[[`TraceStepTemplate`](#ApiClient.TraceStepTemplate "ApiClient.TraceStepTemplate")]

Raises:  
**ApiError** – If the searchCriteria has an illegal syntax.

## TraceStepTemplate[¶](#tracesteptemplate "Link to this heading")

*class* TraceStepTemplate[¶](#ApiClient.TraceStepTemplate "Link to this definition")  
Returned by

- [`TemplateBasedTraceStep.GetTemplate`](TraceAnalysisApi.md#ApiClient.TemplateBasedTraceStep.GetTemplate "ApiClient.TemplateBasedTraceStep.GetTemplate")

- [`TraceStepTemplateApi.OpenTraceStepTemplate`](#ApiClient.TraceStepTemplateApi.OpenTraceStepTemplate "ApiClient.TraceStepTemplateApi.OpenTraceStepTemplate")

- [`TraceStepTemplateApi.SearchTraceStepTemplates`](#ApiClient.TraceStepTemplateApi.SearchTraceStepTemplates "ApiClient.TraceStepTemplateApi.SearchTraceStepTemplates")

Subclasses

- [`TraceStepTemplatePythonEvent`](#ApiClient.TraceStepTemplatePythonEvent "ApiClient.TraceStepTemplatePythonEvent")

Clone()[¶](#ApiClient.TraceStepTemplate.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`TraceStepTemplate`](#ApiClient.TraceStepTemplate "ApiClient.TraceStepTemplate")

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
This status is set initially and will not be changed if the trace step template is fixed later on. You need to close and re-open the package, obtain the trace step from the re-opened package using `Package.GetTraceAnalyses`, [`TraceStepContainer.GetTraceSteps()`](TraceAnalysisApi.md#ApiClient.TraceStepContainer.GetTraceSteps "ApiClient.TraceStepContainer.GetTraceSteps"), etc., and call [`TemplateBasedTraceStep.GetTemplate()`](TraceAnalysisApi.md#ApiClient.TemplateBasedTraceStep.GetTemplate "ApiClient.TemplateBasedTraceStep.GetTemplate") on the new instance.

Returns:  True if the trace step template is broken

Return type:  boolean

IsMissing()[¶](#ApiClient.TraceStepTemplate.IsMissing "Link to this definition")  
Returns whether the trace step template represents a missing trace step template.

Note:  
This status is set initially and will not be changed if the trace step template becomes available later on. You need to close and re-open the package, obtain the trace step from the re-opened package using `Package.GetTraceAnalyses`, [`TraceStepContainer.GetTraceSteps()`](TraceAnalysisApi.md#ApiClient.TraceStepContainer.GetTraceSteps "ApiClient.TraceStepContainer.GetTraceSteps"), etc., and call [`TemplateBasedTraceStep.GetTemplate()`](TraceAnalysisApi.md#ApiClient.TemplateBasedTraceStep.GetTemplate "ApiClient.TemplateBasedTraceStep.GetTemplate") on the new instance.

Returns:  True if the file of the trace step template is not found

Return type:  boolean

## TraceStepTemplatePythonEvent[¶](#tracesteptemplatepythonevent "Link to this heading")

*class* TraceStepTemplatePythonEvent[¶](#ApiClient.TraceStepTemplatePythonEvent "Link to this definition")  
Base class

[`TraceStepTemplate`](#ApiClient.TraceStepTemplate "ApiClient.TraceStepTemplate")

Clone()[¶](#ApiClient.TraceStepTemplatePythonEvent.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`TraceStepTemplatePythonEvent`](#ApiClient.TraceStepTemplatePythonEvent "ApiClient.TraceStepTemplatePythonEvent")

GetDescription()[¶](#ApiClient.TraceStepTemplatePythonEvent.GetDescription "Link to this definition")  
Returns the description of the trace step template.

Returns:  The Description

Return type:  str

GetEventFunctions()[¶](#ApiClient.TraceStepTemplatePythonEvent.GetEventFunctions "Link to this definition")  
Returns the functions associated with signal events, i.e. the next functions.

Returns:  List of the event functions

Return type:  list[[`PythonEventFunction`](#ApiClient.PythonEventFunction "ApiClient.PythonEventFunction")]

GetFinalizeFunctionCode()[¶](#ApiClient.TraceStepTemplatePythonEvent.GetFinalizeFunctionCode "Link to this definition")  
Returns the code used in the finalize function.

Returns:  The finalize function code

Return type:  str

GetInitFunctionCode()[¶](#ApiClient.TraceStepTemplatePythonEvent.GetInitFunctionCode "Link to this definition")  
Returns the code used in the init function.

Returns:  The init function code

Return type:  str

GetName()[¶](#ApiClient.TraceStepTemplatePythonEvent.GetName "Link to this definition")  
Returns the name of the trace step template.

Returns:  The name

Return type:  str

GetParameterDefaultValues()[¶](#ApiClient.TraceStepTemplatePythonEvent.GetParameterDefaultValues "Link to this definition")  
Returns text representation of the default parameter values of the trace step template. Those values are applied of value None is passed to a trace step.

Returns:  The text representations of the default values of all parameters

Return type:  list[str]

GetParameterDescriptions()[¶](#ApiClient.TraceStepTemplatePythonEvent.GetParameterDescriptions "Link to this definition")  
Returns the descriptions of all parameters of a trace step template.

Returns:  The descriptions of all parameters

Return type:  list[str]

GetParameterDirections()[¶](#ApiClient.TraceStepTemplatePythonEvent.GetParameterDirections "Link to this definition")  
Returns the direction of all parameters of a trace step template.

Returns:  The direction of all parameters

Return type:  list[str]

GetParameterNames()[¶](#ApiClient.TraceStepTemplatePythonEvent.GetParameterNames "Link to this definition")  
Returns the names of all parameters of a trace step template.

Returns:  The names of all parameters

Return type:  list[str]

GetParameterTypes()[¶](#ApiClient.TraceStepTemplatePythonEvent.GetParameterTypes "Link to this definition")  
Returns the types of all parameters of a trace step template.

Returns:  The types of all parameters

Return type:  list[str]

GetSignalDescriptions()[¶](#ApiClient.TraceStepTemplatePythonEvent.GetSignalDescriptions "Link to this definition")  
Returns the descriptions of all signals of a trace step template.

Returns:  The Descriptions of all signals

Return type:  list[str]

GetSignalDirections()[¶](#ApiClient.TraceStepTemplatePythonEvent.GetSignalDirections "Link to this definition")  
Returns the direction of all signals of a trace step template.

Returns:  The direction of all signals

Return type:  list[str]

GetSignalNames()[¶](#ApiClient.TraceStepTemplatePythonEvent.GetSignalNames "Link to this definition")  
Returns the names of all signals of the trace step template.

Returns:  The Names of all signals

Return type:  list[str]

GetSignalOptionalFlags()[¶](#ApiClient.TraceStepTemplatePythonEvent.GetSignalOptionalFlags "Link to this definition")  
Returns the “is optional” flags of all signals of a trace step template.

Returns:  The “is optional” flags of all signals

Return type:  list[boolean]

GetType()[¶](#ApiClient.TraceStepTemplatePythonEvent.GetType "Link to this definition")  
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

IsBroken()[¶](#ApiClient.TraceStepTemplatePythonEvent.IsBroken "Link to this definition")  
Returns whether the trace step template represents a broken trace step template.

Note:  
This status is set initially and will not be changed if the trace step template is fixed later on. You need to close and re-open the package, obtain the trace step from the re-opened package using `Package.GetTraceAnalyses`, [`TraceStepContainer.GetTraceSteps()`](TraceAnalysisApi.md#ApiClient.TraceStepContainer.GetTraceSteps "ApiClient.TraceStepContainer.GetTraceSteps"), etc., and call [`TemplateBasedTraceStep.GetTemplate()`](TraceAnalysisApi.md#ApiClient.TemplateBasedTraceStep.GetTemplate "ApiClient.TemplateBasedTraceStep.GetTemplate") on the new instance.

Returns:  True if the trace step template is broken

Return type:  boolean

IsMissing()[¶](#ApiClient.TraceStepTemplatePythonEvent.IsMissing "Link to this definition")  
Returns whether the trace step template represents a missing trace step template.

Note:  
This status is set initially and will not be changed if the trace step template becomes available later on. You need to close and re-open the package, obtain the trace step from the re-opened package using `Package.GetTraceAnalyses`, [`TraceStepContainer.GetTraceSteps()`](TraceAnalysisApi.md#ApiClient.TraceStepContainer.GetTraceSteps "ApiClient.TraceStepContainer.GetTraceSteps"), etc., and call [`TemplateBasedTraceStep.GetTemplate()`](TraceAnalysisApi.md#ApiClient.TemplateBasedTraceStep.GetTemplate "ApiClient.TemplateBasedTraceStep.GetTemplate") on the new instance.

Returns:  True if the file of the trace step template is not found

Return type:  boolean

## PythonEventFunction[¶](#pythoneventfunction "Link to this heading")

*class* PythonEventFunction[¶](#ApiClient.PythonEventFunction "Link to this definition")  
Returned by

- [`TraceStepTemplatePythonEvent.GetEventFunctions`](#ApiClient.TraceStepTemplatePythonEvent.GetEventFunctions "ApiClient.TraceStepTemplatePythonEvent.GetEventFunctions")

Clone()[¶](#ApiClient.PythonEventFunction.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`PythonEventFunction`](#ApiClient.PythonEventFunction "ApiClient.PythonEventFunction")

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
