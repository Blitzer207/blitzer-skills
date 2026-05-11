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

MultiSwipe [ MultiSwipe ](#)

MultiSwipe

- [C MultiSwipe ](#ApiClient.MultiSwipe)
  - [M Clone ](#ApiClient.MultiSwipe.Clone)
  - [M GetEndX ](#ApiClient.MultiSwipe.GetEndX)
  - [M GetEndXUnit ](#ApiClient.MultiSwipe.GetEndXUnit)
  - [M GetEndY ](#ApiClient.MultiSwipe.GetEndY)
  - [M GetEndYUnit ](#ApiClient.MultiSwipe.GetEndYUnit)
  - [M GetFingerCount ](#ApiClient.MultiSwipe.GetFingerCount)
  - [M GetFingerDistance ](#ApiClient.MultiSwipe.GetFingerDistance)
  - [M GetFingerDistanceUnit ](#ApiClient.MultiSwipe.GetFingerDistanceUnit)
  - [M GetInputParameterType ](#ApiClient.MultiSwipe.GetInputParameterType)
  - [M GetName ](#ApiClient.MultiSwipe.GetName)
  - [M GetPrompt ](#ApiClient.MultiSwipe.GetPrompt)
  - [M GetStartX ](#ApiClient.MultiSwipe.GetStartX)
  - [M GetStartXUnit ](#ApiClient.MultiSwipe.GetStartXUnit)
  - [M GetStartY ](#ApiClient.MultiSwipe.GetStartY)
  - [M GetStartYUnit ](#ApiClient.MultiSwipe.GetStartYUnit)
  - [M GetSwipeDuration ](#ApiClient.MultiSwipe.GetSwipeDuration)
  - [M GetSwipeDurationUnit ](#ApiClient.MultiSwipe.GetSwipeDurationUnit)
  - [M SetEndX ](#ApiClient.MultiSwipe.SetEndX)
  - [M SetEndY ](#ApiClient.MultiSwipe.SetEndY)
  - [M SetFingerCount ](#ApiClient.MultiSwipe.SetFingerCount)
  - [M SetFingerDistance ](#ApiClient.MultiSwipe.SetFingerDistance)
  - [M SetInputParameterType ](#ApiClient.MultiSwipe.SetInputParameterType)
  - [M SetPrompt ](#ApiClient.MultiSwipe.SetPrompt)
  - [M SetStartX ](#ApiClient.MultiSwipe.SetStartX)
  - [M SetStartY ](#ApiClient.MultiSwipe.SetStartY)
  - [M SetSwipeDuration ](#ApiClient.MultiSwipe.SetSwipeDuration)

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

MultiSwipe

- [C MultiSwipe ](#ApiClient.MultiSwipe)
  - [M Clone ](#ApiClient.MultiSwipe.Clone)
  - [M GetEndX ](#ApiClient.MultiSwipe.GetEndX)
  - [M GetEndXUnit ](#ApiClient.MultiSwipe.GetEndXUnit)
  - [M GetEndY ](#ApiClient.MultiSwipe.GetEndY)
  - [M GetEndYUnit ](#ApiClient.MultiSwipe.GetEndYUnit)
  - [M GetFingerCount ](#ApiClient.MultiSwipe.GetFingerCount)
  - [M GetFingerDistance ](#ApiClient.MultiSwipe.GetFingerDistance)
  - [M GetFingerDistanceUnit ](#ApiClient.MultiSwipe.GetFingerDistanceUnit)
  - [M GetInputParameterType ](#ApiClient.MultiSwipe.GetInputParameterType)
  - [M GetName ](#ApiClient.MultiSwipe.GetName)
  - [M GetPrompt ](#ApiClient.MultiSwipe.GetPrompt)
  - [M GetStartX ](#ApiClient.MultiSwipe.GetStartX)
  - [M GetStartXUnit ](#ApiClient.MultiSwipe.GetStartXUnit)
  - [M GetStartY ](#ApiClient.MultiSwipe.GetStartY)
  - [M GetStartYUnit ](#ApiClient.MultiSwipe.GetStartYUnit)
  - [M GetSwipeDuration ](#ApiClient.MultiSwipe.GetSwipeDuration)
  - [M GetSwipeDurationUnit ](#ApiClient.MultiSwipe.GetSwipeDurationUnit)
  - [M SetEndX ](#ApiClient.MultiSwipe.SetEndX)
  - [M SetEndY ](#ApiClient.MultiSwipe.SetEndY)
  - [M SetFingerCount ](#ApiClient.MultiSwipe.SetFingerCount)
  - [M SetFingerDistance ](#ApiClient.MultiSwipe.SetFingerDistance)
  - [M SetInputParameterType ](#ApiClient.MultiSwipe.SetInputParameterType)
  - [M SetPrompt ](#ApiClient.MultiSwipe.SetPrompt)
  - [M SetStartX ](#ApiClient.MultiSwipe.SetStartX)
  - [M SetStartY ](#ApiClient.MultiSwipe.SetStartY)
  - [M SetSwipeDuration ](#ApiClient.MultiSwipe.SetSwipeDuration)

# MultiSwipe[¶](#multiswipe "Link to this heading")

*class* MultiSwipe[¶](#ApiClient.MultiSwipe "Link to this definition")  
Returned by

- [`TouchInputApi.CreateMultiSwipe`](../TouchInputApi.md#ApiClient.TouchInputApi.CreateMultiSwipe "ApiClient.TouchInputApi.CreateMultiSwipe (Python method) — Create a new multiswipe input action object.")

Clone()[¶](#ApiClient.MultiSwipe.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`MultiSwipe`](#ApiClient.MultiSwipe "ApiClient.MultiSwipe (Python class) — TouchInputApi.CreateMultiSwipe")

GetEndX()[¶](#ApiClient.MultiSwipe.GetEndX "Link to this definition")  
Returns the value of the first coordinate of the final position.

Returns:  Value of x-coordinate

Return type:  str

GetEndXUnit()[¶](#ApiClient.MultiSwipe.GetEndXUnit "Link to this definition")  
Returns the unit of the first coordinate of the final position.

Returns:  Unit of x-coordinate

Return type:  str

GetEndY()[¶](#ApiClient.MultiSwipe.GetEndY "Link to this definition")  
Returns the value of the second coordinate of the final position.

Returns:  Value of y-coordinate

Return type:  str

GetEndYUnit()[¶](#ApiClient.MultiSwipe.GetEndYUnit "Link to this definition")  
Returns the unit of the second coordinate of the final position.

Returns:  Unit of y-coordinate

Return type:  str

GetFingerCount()[¶](#ApiClient.MultiSwipe.GetFingerCount "Link to this definition")  
Returns the number of fingers involved.

Returns:  Number of fingers

Return type:  str

GetFingerDistance()[¶](#ApiClient.MultiSwipe.GetFingerDistance "Link to this definition")  
Returns the value of the mean distance of fingers.

Returns:  Value of mean distance of fingers

Return type:  str

GetFingerDistanceUnit()[¶](#ApiClient.MultiSwipe.GetFingerDistanceUnit "Link to this definition")  
Returns the unit of the mean distance of fingers.

Returns:  Unit of mean distance of fingers

Return type:  str

GetInputParameterType()[¶](#ApiClient.MultiSwipe.GetInputParameterType "Link to this definition")  
Returns the type of the touch input action parameters.

Returns:  The type of the touch input action parameters (‘Coordinates’ or ‘Prompt’)

Return type:  str

GetName()[¶](#ApiClient.MultiSwipe.GetName "Link to this definition")  
Returns the name of the touch input action

Returns:  The name of the touch input action

Return type:  str

GetPrompt()[¶](#ApiClient.MultiSwipe.GetPrompt "Link to this definition")  
Returns the prompt expression for the touch input action.

Returns:  The prompt expression for the touch input action

Return type:  str

GetStartX()[¶](#ApiClient.MultiSwipe.GetStartX "Link to this definition")  
Returns the value of the first coordinate of the starting position.

Returns:  Value of x-coordinate

Return type:  str

GetStartXUnit()[¶](#ApiClient.MultiSwipe.GetStartXUnit "Link to this definition")  
Returns the unit of the first coordinate of the starting position.

Returns:  Unit of x-coordinate

Return type:  str

GetStartY()[¶](#ApiClient.MultiSwipe.GetStartY "Link to this definition")  
Returns the value of the second coordinate of the starting position.

Returns:  Value of y-coordinate

Return type:  str

GetStartYUnit()[¶](#ApiClient.MultiSwipe.GetStartYUnit "Link to this definition")  
Returns the unit of the second coordinate of the starting position.

Returns:  Unit of y-coordinate

Return type:  str

GetSwipeDuration()[¶](#ApiClient.MultiSwipe.GetSwipeDuration "Link to this definition")  
Returns the value of the swipe duration.

Returns:  Swipe duration

Return type:  str

GetSwipeDurationUnit()[¶](#ApiClient.MultiSwipe.GetSwipeDurationUnit "Link to this definition")  
Returns the unit of the swipe duration.

Returns:  Swipe duration

Return type:  str

SetEndX(*[expr](#ApiClient.MultiSwipe.SetEndX.expr "ApiClient.MultiSwipe.SetEndX.expr (Python parameter) — expression for x-coordinate of position")*, *[unit](#ApiClient.MultiSwipe.SetEndX.unit "ApiClient.MultiSwipe.SetEndX.unit (Python parameter) — unit of x-coordinate, absolute 'px' or relative '%'")=`'px'`*)[¶](#ApiClient.MultiSwipe.SetEndX "Link to this definition")  
Sets first coordinate of the final position.

Parameters:  expr : str[¶](#ApiClient.MultiSwipe.SetEndX.expr "Permalink to this definition")  
expression for x-coordinate of position

unit : str[¶](#ApiClient.MultiSwipe.SetEndX.unit "Permalink to this definition")  
unit of x-coordinate, absolute ‘px’ or relative ‘%’

SetEndY(*[expr](#ApiClient.MultiSwipe.SetEndY.expr "ApiClient.MultiSwipe.SetEndY.expr (Python parameter) — expression for y-coordinate of position")*, *[unit](#ApiClient.MultiSwipe.SetEndY.unit "ApiClient.MultiSwipe.SetEndY.unit (Python parameter) — unit of y-coordinate, absolute 'px' or relative '%'")=`'px'`*)[¶](#ApiClient.MultiSwipe.SetEndY "Link to this definition")  
Sets second coordinate of the final position.

Parameters:  expr : str[¶](#ApiClient.MultiSwipe.SetEndY.expr "Permalink to this definition")  
expression for y-coordinate of position

unit : str[¶](#ApiClient.MultiSwipe.SetEndY.unit "Permalink to this definition")  
unit of y-coordinate, absolute ‘px’ or relative ‘%’

SetFingerCount(*[expr](#ApiClient.MultiSwipe.SetFingerCount.expr "ApiClient.MultiSwipe.SetFingerCount.expr (Python parameter) — Number of fingers")*)[¶](#ApiClient.MultiSwipe.SetFingerCount "Link to this definition")  
Sets the number of fingers involved.

Parameters:  expr : str[¶](#ApiClient.MultiSwipe.SetFingerCount.expr "Permalink to this definition")  
Number of fingers

SetFingerDistance(*[expr](#ApiClient.MultiSwipe.SetFingerDistance.expr "ApiClient.MultiSwipe.SetFingerDistance.expr (Python parameter) — Mean finger distance")*, *[unit](#ApiClient.MultiSwipe.SetFingerDistance.unit "ApiClient.MultiSwipe.SetFingerDistance.unit (Python parameter) — unit of distance, absolute 'px' or relative '%'")=`'px'`*)[¶](#ApiClient.MultiSwipe.SetFingerDistance "Link to this definition")  
Sets the mean finger distance

Parameters:  expr : str[¶](#ApiClient.MultiSwipe.SetFingerDistance.expr "Permalink to this definition")  
Mean finger distance

unit : str[¶](#ApiClient.MultiSwipe.SetFingerDistance.unit "Permalink to this definition")  
unit of distance, absolute ‘px’ or relative ‘%’

SetInputParameterType(*[parameterType](#ApiClient.MultiSwipe.SetInputParameterType.parameterType "ApiClient.MultiSwipe.SetInputParameterType.parameterType (Python parameter) — The type of the touch input action parameters ('Coordinates' or 'Prompt')")*)[¶](#ApiClient.MultiSwipe.SetInputParameterType "Link to this definition")  
Sets the type of the touch input action parameters.

Parameters:  parameterType : str[¶](#ApiClient.MultiSwipe.SetInputParameterType.parameterType "Permalink to this definition")  
The type of the touch input action parameters (‘Coordinates’ or ‘Prompt’)

SetPrompt(*[prompt](#ApiClient.MultiSwipe.SetPrompt.prompt "ApiClient.MultiSwipe.SetPrompt.prompt (Python parameter) — The prompt expression for the touch input action")*)[¶](#ApiClient.MultiSwipe.SetPrompt "Link to this definition")  
Sets the prompt expression for the touch input action.

Parameters:  prompt : str[¶](#ApiClient.MultiSwipe.SetPrompt.prompt "Permalink to this definition")  
The prompt expression for the touch input action

SetStartX(*[expr](#ApiClient.MultiSwipe.SetStartX.expr "ApiClient.MultiSwipe.SetStartX.expr (Python parameter) — expression for x-coordinate of position")*, *[unit](#ApiClient.MultiSwipe.SetStartX.unit "ApiClient.MultiSwipe.SetStartX.unit (Python parameter) — unit of x-coordinate, absolute 'px' or relative '%'")=`'px'`*)[¶](#ApiClient.MultiSwipe.SetStartX "Link to this definition")  
Sets first coordinate of the starting position.

Parameters:  expr : str[¶](#ApiClient.MultiSwipe.SetStartX.expr "Permalink to this definition")  
expression for x-coordinate of position

unit : str[¶](#ApiClient.MultiSwipe.SetStartX.unit "Permalink to this definition")  
unit of x-coordinate, absolute ‘px’ or relative ‘%’

SetStartY(*[expr](#ApiClient.MultiSwipe.SetStartY.expr "ApiClient.MultiSwipe.SetStartY.expr (Python parameter) — expression for y-coordinate of position")*, *[unit](#ApiClient.MultiSwipe.SetStartY.unit "ApiClient.MultiSwipe.SetStartY.unit (Python parameter) — unit of y-coordinate, absolute 'px' or relative '%'")=`'px'`*)[¶](#ApiClient.MultiSwipe.SetStartY "Link to this definition")  
Sets second coordinate of the starting position.

Parameters:  expr : str[¶](#ApiClient.MultiSwipe.SetStartY.expr "Permalink to this definition")  
expression for y-coordinate of position

unit : str[¶](#ApiClient.MultiSwipe.SetStartY.unit "Permalink to this definition")  
unit of y-coordinate, absolute ‘px’ or relative ‘%’

SetSwipeDuration(*[expr](#ApiClient.MultiSwipe.SetSwipeDuration.expr "ApiClient.MultiSwipe.SetSwipeDuration.expr (Python parameter) — Swipe duration")*, *[unit](#ApiClient.MultiSwipe.SetSwipeDuration.unit "ApiClient.MultiSwipe.SetSwipeDuration.unit (Python parameter) — unit of duration, milliseconds 'ms' or seconds 's'")=`'s'`*)[¶](#ApiClient.MultiSwipe.SetSwipeDuration "Link to this definition")  
Sets the swipe duration.

Parameters:  expr : str[¶](#ApiClient.MultiSwipe.SetSwipeDuration.expr "Permalink to this definition")  
Swipe duration

unit : str[¶](#ApiClient.MultiSwipe.SetSwipeDuration.unit "Permalink to this definition")  
unit of duration, milliseconds ‘ms’ or seconds ‘s’

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
