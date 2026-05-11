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

[ HoldAndSwipe ](HoldAndSwipe.md)

[ MultiSwipe ](MultiSwipe.md)

[ MultiTap ](MultiTap.md)

[ Pinch ](Pinch.md)

[ Rotate ](Rotate.md)

Swipe [ Swipe ](#)

Swipe

- [C Swipe ](#ApiClient.Swipe)
  - [M Clone ](#ApiClient.Swipe.Clone)
  - [M GetEndX ](#ApiClient.Swipe.GetEndX)
  - [M GetEndXUnit ](#ApiClient.Swipe.GetEndXUnit)
  - [M GetEndY ](#ApiClient.Swipe.GetEndY)
  - [M GetEndYUnit ](#ApiClient.Swipe.GetEndYUnit)
  - [M GetInputParameterType ](#ApiClient.Swipe.GetInputParameterType)
  - [M GetName ](#ApiClient.Swipe.GetName)
  - [M GetPrompt ](#ApiClient.Swipe.GetPrompt)
  - [M GetStartX ](#ApiClient.Swipe.GetStartX)
  - [M GetStartXUnit ](#ApiClient.Swipe.GetStartXUnit)
  - [M GetStartY ](#ApiClient.Swipe.GetStartY)
  - [M GetStartYUnit ](#ApiClient.Swipe.GetStartYUnit)
  - [M GetSwipeDuration ](#ApiClient.Swipe.GetSwipeDuration)
  - [M GetSwipeDurationUnit ](#ApiClient.Swipe.GetSwipeDurationUnit)
  - [M SetEndX ](#ApiClient.Swipe.SetEndX)
  - [M SetEndY ](#ApiClient.Swipe.SetEndY)
  - [M SetInputParameterType ](#ApiClient.Swipe.SetInputParameterType)
  - [M SetPrompt ](#ApiClient.Swipe.SetPrompt)
  - [M SetStartX ](#ApiClient.Swipe.SetStartX)
  - [M SetStartY ](#ApiClient.Swipe.SetStartY)
  - [M SetSwipeDuration ](#ApiClient.Swipe.SetSwipeDuration)

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

Swipe

- [C Swipe ](#ApiClient.Swipe)
  - [M Clone ](#ApiClient.Swipe.Clone)
  - [M GetEndX ](#ApiClient.Swipe.GetEndX)
  - [M GetEndXUnit ](#ApiClient.Swipe.GetEndXUnit)
  - [M GetEndY ](#ApiClient.Swipe.GetEndY)
  - [M GetEndYUnit ](#ApiClient.Swipe.GetEndYUnit)
  - [M GetInputParameterType ](#ApiClient.Swipe.GetInputParameterType)
  - [M GetName ](#ApiClient.Swipe.GetName)
  - [M GetPrompt ](#ApiClient.Swipe.GetPrompt)
  - [M GetStartX ](#ApiClient.Swipe.GetStartX)
  - [M GetStartXUnit ](#ApiClient.Swipe.GetStartXUnit)
  - [M GetStartY ](#ApiClient.Swipe.GetStartY)
  - [M GetStartYUnit ](#ApiClient.Swipe.GetStartYUnit)
  - [M GetSwipeDuration ](#ApiClient.Swipe.GetSwipeDuration)
  - [M GetSwipeDurationUnit ](#ApiClient.Swipe.GetSwipeDurationUnit)
  - [M SetEndX ](#ApiClient.Swipe.SetEndX)
  - [M SetEndY ](#ApiClient.Swipe.SetEndY)
  - [M SetInputParameterType ](#ApiClient.Swipe.SetInputParameterType)
  - [M SetPrompt ](#ApiClient.Swipe.SetPrompt)
  - [M SetStartX ](#ApiClient.Swipe.SetStartX)
  - [M SetStartY ](#ApiClient.Swipe.SetStartY)
  - [M SetSwipeDuration ](#ApiClient.Swipe.SetSwipeDuration)

# Swipe[¶](#swipe "Link to this heading")

*class* Swipe[¶](#ApiClient.Swipe "Link to this definition")  
Returned by

- [`TouchInputApi.CreateSwipe`](../TouchInputApi.md#ApiClient.TouchInputApi.CreateSwipe "ApiClient.TouchInputApi.CreateSwipe (Python method) — Create a new swipe input action object.")

Clone()[¶](#ApiClient.Swipe.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`Swipe`](#ApiClient.Swipe "ApiClient.Swipe (Python class) — TouchInputApi.CreateSwipe")

GetEndX()[¶](#ApiClient.Swipe.GetEndX "Link to this definition")  
Returns the value of the first coordinate of the final position.

Returns:  Value of x-coordinate

Return type:  str

GetEndXUnit()[¶](#ApiClient.Swipe.GetEndXUnit "Link to this definition")  
Returns the unit of the first coordinate of the final position.

Returns:  Unit of x-coordinate

Return type:  str

GetEndY()[¶](#ApiClient.Swipe.GetEndY "Link to this definition")  
Returns the value of the second coordinate of the final position.

Returns:  Value of y-coordinate

Return type:  str

GetEndYUnit()[¶](#ApiClient.Swipe.GetEndYUnit "Link to this definition")  
Returns the unit of the second coordinate of the final position.

Returns:  Unit of y-coordinate

Return type:  str

GetInputParameterType()[¶](#ApiClient.Swipe.GetInputParameterType "Link to this definition")  
Returns the type of the touch input action parameters.

Returns:  The type of the touch input action parameters (‘Coordinates’ or ‘Prompt’)

Return type:  str

GetName()[¶](#ApiClient.Swipe.GetName "Link to this definition")  
Returns the name of the touch input action

Returns:  The name of the touch input action

Return type:  str

GetPrompt()[¶](#ApiClient.Swipe.GetPrompt "Link to this definition")  
Returns the prompt expression for the touch input action.

Returns:  The prompt expression for the touch input action

Return type:  str

GetStartX()[¶](#ApiClient.Swipe.GetStartX "Link to this definition")  
Returns the value of the first coordinate of the starting position.

Returns:  Value of x-coordinate

Return type:  str

GetStartXUnit()[¶](#ApiClient.Swipe.GetStartXUnit "Link to this definition")  
Returns the unit of the first coordinate of the starting position.

Returns:  Unit of x-coordinate

Return type:  str

GetStartY()[¶](#ApiClient.Swipe.GetStartY "Link to this definition")  
Returns the value of the second coordinate of the starting position.

Returns:  Value of y-coordinate

Return type:  str

GetStartYUnit()[¶](#ApiClient.Swipe.GetStartYUnit "Link to this definition")  
Returns the unit of the second coordinate of the starting position.

Returns:  Unit of y-coordinate

Return type:  str

GetSwipeDuration()[¶](#ApiClient.Swipe.GetSwipeDuration "Link to this definition")  
Returns the value of the swipe duration.

Returns:  Swipe duration

Return type:  str

GetSwipeDurationUnit()[¶](#ApiClient.Swipe.GetSwipeDurationUnit "Link to this definition")  
Returns the unit of the swipe duration.

Returns:  Swipe duration

Return type:  str

SetEndX(*[expr](#ApiClient.Swipe.SetEndX.expr "ApiClient.Swipe.SetEndX.expr (Python parameter) — expression for x-coordinate of position")*, *[unit](#ApiClient.Swipe.SetEndX.unit "ApiClient.Swipe.SetEndX.unit (Python parameter) — unit of x-coordinate, absolute 'px' or relative '%'")=`'px'`*)[¶](#ApiClient.Swipe.SetEndX "Link to this definition")  
Sets first coordinate of the final position.

Parameters:  expr : str[¶](#ApiClient.Swipe.SetEndX.expr "Permalink to this definition")  
expression for x-coordinate of position

unit : str[¶](#ApiClient.Swipe.SetEndX.unit "Permalink to this definition")  
unit of x-coordinate, absolute ‘px’ or relative ‘%’

SetEndY(*[expr](#ApiClient.Swipe.SetEndY.expr "ApiClient.Swipe.SetEndY.expr (Python parameter) — expression for y-coordinate of position")*, *[unit](#ApiClient.Swipe.SetEndY.unit "ApiClient.Swipe.SetEndY.unit (Python parameter) — unit of y-coordinate, absolute 'px' or relative '%'")=`'px'`*)[¶](#ApiClient.Swipe.SetEndY "Link to this definition")  
Sets second coordinate of the final position.

Parameters:  expr : str[¶](#ApiClient.Swipe.SetEndY.expr "Permalink to this definition")  
expression for y-coordinate of position

unit : str[¶](#ApiClient.Swipe.SetEndY.unit "Permalink to this definition")  
unit of y-coordinate, absolute ‘px’ or relative ‘%’

SetInputParameterType(*[parameterType](#ApiClient.Swipe.SetInputParameterType.parameterType "ApiClient.Swipe.SetInputParameterType.parameterType (Python parameter) — The type of the touch input action parameters ('Coordinates' or 'Prompt')")*)[¶](#ApiClient.Swipe.SetInputParameterType "Link to this definition")  
Sets the type of the touch input action parameters.

Parameters:  parameterType : str[¶](#ApiClient.Swipe.SetInputParameterType.parameterType "Permalink to this definition")  
The type of the touch input action parameters (‘Coordinates’ or ‘Prompt’)

SetPrompt(*[prompt](#ApiClient.Swipe.SetPrompt.prompt "ApiClient.Swipe.SetPrompt.prompt (Python parameter) — The prompt expression for the touch input action")*)[¶](#ApiClient.Swipe.SetPrompt "Link to this definition")  
Sets the prompt expression for the touch input action.

Parameters:  prompt : str[¶](#ApiClient.Swipe.SetPrompt.prompt "Permalink to this definition")  
The prompt expression for the touch input action

SetStartX(*[expr](#ApiClient.Swipe.SetStartX.expr "ApiClient.Swipe.SetStartX.expr (Python parameter) — expression for x-coordinate of position")*, *[unit](#ApiClient.Swipe.SetStartX.unit "ApiClient.Swipe.SetStartX.unit (Python parameter) — unit of x-coordinate, absolute 'px' or relative '%'")=`'px'`*)[¶](#ApiClient.Swipe.SetStartX "Link to this definition")  
Sets first coordinate of the starting position.

Parameters:  expr : str[¶](#ApiClient.Swipe.SetStartX.expr "Permalink to this definition")  
expression for x-coordinate of position

unit : str[¶](#ApiClient.Swipe.SetStartX.unit "Permalink to this definition")  
unit of x-coordinate, absolute ‘px’ or relative ‘%’

SetStartY(*[expr](#ApiClient.Swipe.SetStartY.expr "ApiClient.Swipe.SetStartY.expr (Python parameter) — expression for y-coordinate of position")*, *[unit](#ApiClient.Swipe.SetStartY.unit "ApiClient.Swipe.SetStartY.unit (Python parameter) — unit of y-coordinate, absolute 'px' or relative '%'")=`'px'`*)[¶](#ApiClient.Swipe.SetStartY "Link to this definition")  
Sets second coordinate of the starting position.

Parameters:  expr : str[¶](#ApiClient.Swipe.SetStartY.expr "Permalink to this definition")  
expression for y-coordinate of position

unit : str[¶](#ApiClient.Swipe.SetStartY.unit "Permalink to this definition")  
unit of y-coordinate, absolute ‘px’ or relative ‘%’

SetSwipeDuration(*[expr](#ApiClient.Swipe.SetSwipeDuration.expr "ApiClient.Swipe.SetSwipeDuration.expr (Python parameter) — Swipe duration")*, *[unit](#ApiClient.Swipe.SetSwipeDuration.unit "ApiClient.Swipe.SetSwipeDuration.unit (Python parameter) — unit of duration, milliseconds 'ms' or seconds 's'")=`'s'`*)[¶](#ApiClient.Swipe.SetSwipeDuration "Link to this definition")  
Sets the swipe duration.

Parameters:  expr : str[¶](#ApiClient.Swipe.SetSwipeDuration.expr "Permalink to this definition")  
Swipe duration

unit : str[¶](#ApiClient.Swipe.SetSwipeDuration.unit "Permalink to this definition")  
unit of duration, milliseconds ‘ms’ or seconds ‘s’

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
