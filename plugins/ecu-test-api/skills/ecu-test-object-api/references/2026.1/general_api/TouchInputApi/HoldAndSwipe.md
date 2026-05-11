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

API for Touch Inputs

[ Hold ](Hold.md)

HoldAndSwipe [ HoldAndSwipe ](#)

HoldAndSwipe

- [C HoldAndSwipe ](#ApiClient.HoldAndSwipe)
  - [M Clone ](#ApiClient.HoldAndSwipe.Clone)
  - [M GetEndX ](#ApiClient.HoldAndSwipe.GetEndX)
  - [M GetEndXUnit ](#ApiClient.HoldAndSwipe.GetEndXUnit)
  - [M GetEndY ](#ApiClient.HoldAndSwipe.GetEndY)
  - [M GetEndYUnit ](#ApiClient.HoldAndSwipe.GetEndYUnit)
  - [M GetHoldDuration ](#ApiClient.HoldAndSwipe.GetHoldDuration)
  - [M GetHoldDurationUnit ](#ApiClient.HoldAndSwipe.GetHoldDurationUnit)
  - [M GetInputParameterType ](#ApiClient.HoldAndSwipe.GetInputParameterType)
  - [M GetName ](#ApiClient.HoldAndSwipe.GetName)
  - [M GetPrompt ](#ApiClient.HoldAndSwipe.GetPrompt)
  - [M GetStartX ](#ApiClient.HoldAndSwipe.GetStartX)
  - [M GetStartXUnit ](#ApiClient.HoldAndSwipe.GetStartXUnit)
  - [M GetStartY ](#ApiClient.HoldAndSwipe.GetStartY)
  - [M GetStartYUnit ](#ApiClient.HoldAndSwipe.GetStartYUnit)
  - [M GetSwipeDuration ](#ApiClient.HoldAndSwipe.GetSwipeDuration)
  - [M GetSwipeDurationUnit ](#ApiClient.HoldAndSwipe.GetSwipeDurationUnit)
  - [M SetEndX ](#ApiClient.HoldAndSwipe.SetEndX)
  - [M SetEndY ](#ApiClient.HoldAndSwipe.SetEndY)
  - [M SetHoldDuration ](#ApiClient.HoldAndSwipe.SetHoldDuration)
  - [M SetInputParameterType ](#ApiClient.HoldAndSwipe.SetInputParameterType)
  - [M SetPrompt ](#ApiClient.HoldAndSwipe.SetPrompt)
  - [M SetStartX ](#ApiClient.HoldAndSwipe.SetStartX)
  - [M SetStartY ](#ApiClient.HoldAndSwipe.SetStartY)
  - [M SetSwipeDuration ](#ApiClient.HoldAndSwipe.SetSwipeDuration)

[ MultiSwipe ](MultiSwipe.md)

[ MultiTap ](MultiTap.md)

[ Pinch ](Pinch.md)

[ Rotate ](Rotate.md)

[ Swipe ](Swipe.md)

[ Tap ](Tap.md)

[ API for Trace Analyses ](../TraceAnalysisApi.md)

[ API for Trace Files ](../TraceFileApi.md)

[ API for Trace Step Templates ](../TraceStepTemplateApi.md)

[ API for Variables ](../VariableApi.md)

[ API for Workspaces ](../WorkspaceApi.md)

[ Trace Analysis API ](../../TraceAnalysisAPI/index.md)

[ Generator APIs ](../../generators/index.md)

[ Tools ](../../tools/index.md)

[ User test management ](../../userTestmanagement/index.md)

[ UserUtility API ](../../user-utility/user-utility.md)

[ Utility Examples ](../../user-utility/example-utilities.md)

HoldAndSwipe

- [C HoldAndSwipe ](#ApiClient.HoldAndSwipe)
  - [M Clone ](#ApiClient.HoldAndSwipe.Clone)
  - [M GetEndX ](#ApiClient.HoldAndSwipe.GetEndX)
  - [M GetEndXUnit ](#ApiClient.HoldAndSwipe.GetEndXUnit)
  - [M GetEndY ](#ApiClient.HoldAndSwipe.GetEndY)
  - [M GetEndYUnit ](#ApiClient.HoldAndSwipe.GetEndYUnit)
  - [M GetHoldDuration ](#ApiClient.HoldAndSwipe.GetHoldDuration)
  - [M GetHoldDurationUnit ](#ApiClient.HoldAndSwipe.GetHoldDurationUnit)
  - [M GetInputParameterType ](#ApiClient.HoldAndSwipe.GetInputParameterType)
  - [M GetName ](#ApiClient.HoldAndSwipe.GetName)
  - [M GetPrompt ](#ApiClient.HoldAndSwipe.GetPrompt)
  - [M GetStartX ](#ApiClient.HoldAndSwipe.GetStartX)
  - [M GetStartXUnit ](#ApiClient.HoldAndSwipe.GetStartXUnit)
  - [M GetStartY ](#ApiClient.HoldAndSwipe.GetStartY)
  - [M GetStartYUnit ](#ApiClient.HoldAndSwipe.GetStartYUnit)
  - [M GetSwipeDuration ](#ApiClient.HoldAndSwipe.GetSwipeDuration)
  - [M GetSwipeDurationUnit ](#ApiClient.HoldAndSwipe.GetSwipeDurationUnit)
  - [M SetEndX ](#ApiClient.HoldAndSwipe.SetEndX)
  - [M SetEndY ](#ApiClient.HoldAndSwipe.SetEndY)
  - [M SetHoldDuration ](#ApiClient.HoldAndSwipe.SetHoldDuration)
  - [M SetInputParameterType ](#ApiClient.HoldAndSwipe.SetInputParameterType)
  - [M SetPrompt ](#ApiClient.HoldAndSwipe.SetPrompt)
  - [M SetStartX ](#ApiClient.HoldAndSwipe.SetStartX)
  - [M SetStartY ](#ApiClient.HoldAndSwipe.SetStartY)
  - [M SetSwipeDuration ](#ApiClient.HoldAndSwipe.SetSwipeDuration)

# HoldAndSwipe[¶](#holdandswipe "Link to this heading")

*class* HoldAndSwipe[¶](#ApiClient.HoldAndSwipe "Link to this definition")  
Returned by

- [`TouchInputApi.CreateHoldAndSwipe`](../TouchInputApi.md#ApiClient.TouchInputApi.CreateHoldAndSwipe "ApiClient.TouchInputApi.CreateHoldAndSwipe (Python method) — Create a new hold-and-swipe input action object.")

Clone()[¶](#ApiClient.HoldAndSwipe.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`HoldAndSwipe`](#ApiClient.HoldAndSwipe "ApiClient.HoldAndSwipe (Python class) — TouchInputApi.CreateHoldAndSwipe")

GetEndX()[¶](#ApiClient.HoldAndSwipe.GetEndX "Link to this definition")  
Returns the value of the first coordinate of the final position.

Returns:  Value of x-coordinate

Return type:  str

GetEndXUnit()[¶](#ApiClient.HoldAndSwipe.GetEndXUnit "Link to this definition")  
Returns the unit of the first coordinate of the final position.

Returns:  Unit of x-coordinate

Return type:  str

GetEndY()[¶](#ApiClient.HoldAndSwipe.GetEndY "Link to this definition")  
Returns the value of the second coordinate of the final position.

Returns:  Value of y-coordinate

Return type:  str

GetEndYUnit()[¶](#ApiClient.HoldAndSwipe.GetEndYUnit "Link to this definition")  
Returns the unit of the second coordinate of the final position.

Returns:  Unit of y-coordinate

Return type:  str

GetHoldDuration()[¶](#ApiClient.HoldAndSwipe.GetHoldDuration "Link to this definition")  
Returns the value of the hold duration.

Returns:  Value of hold duration

Return type:  str

GetHoldDurationUnit()[¶](#ApiClient.HoldAndSwipe.GetHoldDurationUnit "Link to this definition")  
Returns the unit of the hold duration.

Returns:  Unit of hold duration

Return type:  str

GetInputParameterType()[¶](#ApiClient.HoldAndSwipe.GetInputParameterType "Link to this definition")  
Returns the type of the touch input action parameters.

Returns:  The type of the touch input action parameters (‘Coordinates’ or ‘Prompt’)

Return type:  str

GetName()[¶](#ApiClient.HoldAndSwipe.GetName "Link to this definition")  
Returns the name of the touch input action

Returns:  The name of the touch input action

Return type:  str

GetPrompt()[¶](#ApiClient.HoldAndSwipe.GetPrompt "Link to this definition")  
Returns the prompt expression for the touch input action.

Returns:  The prompt expression for the touch input action

Return type:  str

GetStartX()[¶](#ApiClient.HoldAndSwipe.GetStartX "Link to this definition")  
Returns the value of the first coordinate of the starting position.

Returns:  Value of x-coordinate

Return type:  str

GetStartXUnit()[¶](#ApiClient.HoldAndSwipe.GetStartXUnit "Link to this definition")  
Returns the unit of the first coordinate of the starting position.

Returns:  Unit of x-coordinate

Return type:  str

GetStartY()[¶](#ApiClient.HoldAndSwipe.GetStartY "Link to this definition")  
Returns the value of the second coordinate of the starting position.

Returns:  Value of y-coordinate

Return type:  str

GetStartYUnit()[¶](#ApiClient.HoldAndSwipe.GetStartYUnit "Link to this definition")  
Returns the unit of the second coordinate of the starting position.

Returns:  Unit of y-coordinate

Return type:  str

GetSwipeDuration()[¶](#ApiClient.HoldAndSwipe.GetSwipeDuration "Link to this definition")  
Returns the value of the swipe duration.

Returns:  Swipe duration

Return type:  str

GetSwipeDurationUnit()[¶](#ApiClient.HoldAndSwipe.GetSwipeDurationUnit "Link to this definition")  
Returns the unit of the swipe duration.

Returns:  Swipe duration

Return type:  str

SetEndX(*[expr](#ApiClient.HoldAndSwipe.SetEndX.expr "ApiClient.HoldAndSwipe.SetEndX.expr (Python parameter) — expression for x-coordinate of position")*, *[unit](#ApiClient.HoldAndSwipe.SetEndX.unit "ApiClient.HoldAndSwipe.SetEndX.unit (Python parameter) — unit of x-coordinate, absolute 'px' or relative '%'")=`'px'`*)[¶](#ApiClient.HoldAndSwipe.SetEndX "Link to this definition")  
Sets first coordinate of the final position.

Parameters:  expr : str[¶](#ApiClient.HoldAndSwipe.SetEndX.expr "Permalink to this definition")  
expression for x-coordinate of position

unit : str[¶](#ApiClient.HoldAndSwipe.SetEndX.unit "Permalink to this definition")  
unit of x-coordinate, absolute ‘px’ or relative ‘%’

SetEndY(*[expr](#ApiClient.HoldAndSwipe.SetEndY.expr "ApiClient.HoldAndSwipe.SetEndY.expr (Python parameter) — expression for y-coordinate of position")*, *[unit](#ApiClient.HoldAndSwipe.SetEndY.unit "ApiClient.HoldAndSwipe.SetEndY.unit (Python parameter) — unit of y-coordinate, absolute 'px' or relative '%'")=`'px'`*)[¶](#ApiClient.HoldAndSwipe.SetEndY "Link to this definition")  
Sets second coordinate of the final position.

Parameters:  expr : str[¶](#ApiClient.HoldAndSwipe.SetEndY.expr "Permalink to this definition")  
expression for y-coordinate of position

unit : str[¶](#ApiClient.HoldAndSwipe.SetEndY.unit "Permalink to this definition")  
unit of y-coordinate, absolute ‘px’ or relative ‘%’

SetHoldDuration(*[expr](#ApiClient.HoldAndSwipe.SetHoldDuration.expr "ApiClient.HoldAndSwipe.SetHoldDuration.expr (Python parameter) — Hold duration")*, *[unit](#ApiClient.HoldAndSwipe.SetHoldDuration.unit "ApiClient.HoldAndSwipe.SetHoldDuration.unit (Python parameter) — unit of duration, milliseconds 'ms' or seconds 's'")=`'s'`*)[¶](#ApiClient.HoldAndSwipe.SetHoldDuration "Link to this definition")  
Sets the hold duration.

Parameters:  expr : str[¶](#ApiClient.HoldAndSwipe.SetHoldDuration.expr "Permalink to this definition")  
Hold duration

unit : str[¶](#ApiClient.HoldAndSwipe.SetHoldDuration.unit "Permalink to this definition")  
unit of duration, milliseconds ‘ms’ or seconds ‘s’

SetInputParameterType(*[parameterType](#ApiClient.HoldAndSwipe.SetInputParameterType.parameterType "ApiClient.HoldAndSwipe.SetInputParameterType.parameterType (Python parameter) — The type of the touch input action parameters ('Coordinates' or 'Prompt')")*)[¶](#ApiClient.HoldAndSwipe.SetInputParameterType "Link to this definition")  
Sets the type of the touch input action parameters.

Parameters:  parameterType : str[¶](#ApiClient.HoldAndSwipe.SetInputParameterType.parameterType "Permalink to this definition")  
The type of the touch input action parameters (‘Coordinates’ or ‘Prompt’)

SetPrompt(*[prompt](#ApiClient.HoldAndSwipe.SetPrompt.prompt "ApiClient.HoldAndSwipe.SetPrompt.prompt (Python parameter) — The prompt expression for the touch input action")*)[¶](#ApiClient.HoldAndSwipe.SetPrompt "Link to this definition")  
Sets the prompt expression for the touch input action.

Parameters:  prompt : str[¶](#ApiClient.HoldAndSwipe.SetPrompt.prompt "Permalink to this definition")  
The prompt expression for the touch input action

SetStartX(*[expr](#ApiClient.HoldAndSwipe.SetStartX.expr "ApiClient.HoldAndSwipe.SetStartX.expr (Python parameter) — expression for x-coordinate of position")*, *[unit](#ApiClient.HoldAndSwipe.SetStartX.unit "ApiClient.HoldAndSwipe.SetStartX.unit (Python parameter) — unit of x-coordinate, absolute 'px' or relative '%'")=`'px'`*)[¶](#ApiClient.HoldAndSwipe.SetStartX "Link to this definition")  
Sets first coordinate of the starting position.

Parameters:  expr : str[¶](#ApiClient.HoldAndSwipe.SetStartX.expr "Permalink to this definition")  
expression for x-coordinate of position

unit : str[¶](#ApiClient.HoldAndSwipe.SetStartX.unit "Permalink to this definition")  
unit of x-coordinate, absolute ‘px’ or relative ‘%’

SetStartY(*[expr](#ApiClient.HoldAndSwipe.SetStartY.expr "ApiClient.HoldAndSwipe.SetStartY.expr (Python parameter) — expression for y-coordinate of position")*, *[unit](#ApiClient.HoldAndSwipe.SetStartY.unit "ApiClient.HoldAndSwipe.SetStartY.unit (Python parameter) — unit of y-coordinate, absolute 'px' or relative '%'")=`'px'`*)[¶](#ApiClient.HoldAndSwipe.SetStartY "Link to this definition")  
Sets second coordinate of the starting position.

Parameters:  expr : str[¶](#ApiClient.HoldAndSwipe.SetStartY.expr "Permalink to this definition")  
expression for y-coordinate of position

unit : str[¶](#ApiClient.HoldAndSwipe.SetStartY.unit "Permalink to this definition")  
unit of y-coordinate, absolute ‘px’ or relative ‘%’

SetSwipeDuration(*[expr](#ApiClient.HoldAndSwipe.SetSwipeDuration.expr "ApiClient.HoldAndSwipe.SetSwipeDuration.expr (Python parameter) — Swipe duration")*, *[unit](#ApiClient.HoldAndSwipe.SetSwipeDuration.unit "ApiClient.HoldAndSwipe.SetSwipeDuration.unit (Python parameter) — unit of duration, milliseconds 'ms' or seconds 's'")=`'s'`*)[¶](#ApiClient.HoldAndSwipe.SetSwipeDuration "Link to this definition")  
Sets the swipe duration.

Parameters:  expr : str[¶](#ApiClient.HoldAndSwipe.SetSwipeDuration.expr "Permalink to this definition")  
Swipe duration

unit : str[¶](#ApiClient.HoldAndSwipe.SetSwipeDuration.unit "Permalink to this definition")  
unit of duration, milliseconds ‘ms’ or seconds ‘s’

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
