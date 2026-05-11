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

Hold [ Hold ](#)

Hold

- [C Hold ](#ApiClient.Hold)
  - [M Clone ](#ApiClient.Hold.Clone)
  - [M GetHoldDuration ](#ApiClient.Hold.GetHoldDuration)
  - [M GetHoldDurationUnit ](#ApiClient.Hold.GetHoldDurationUnit)
  - [M GetInputParameterType ](#ApiClient.Hold.GetInputParameterType)
  - [M GetName ](#ApiClient.Hold.GetName)
  - [M GetPosX ](#ApiClient.Hold.GetPosX)
  - [M GetPosXUnit ](#ApiClient.Hold.GetPosXUnit)
  - [M GetPosY ](#ApiClient.Hold.GetPosY)
  - [M GetPosYUnit ](#ApiClient.Hold.GetPosYUnit)
  - [M GetPrompt ](#ApiClient.Hold.GetPrompt)
  - [M SetHoldDuration ](#ApiClient.Hold.SetHoldDuration)
  - [M SetInputParameterType ](#ApiClient.Hold.SetInputParameterType)
  - [M SetPosX ](#ApiClient.Hold.SetPosX)
  - [M SetPosY ](#ApiClient.Hold.SetPosY)
  - [M SetPrompt ](#ApiClient.Hold.SetPrompt)

[ HoldAndSwipe ](HoldAndSwipe.md)

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

Hold

- [C Hold ](#ApiClient.Hold)
  - [M Clone ](#ApiClient.Hold.Clone)
  - [M GetHoldDuration ](#ApiClient.Hold.GetHoldDuration)
  - [M GetHoldDurationUnit ](#ApiClient.Hold.GetHoldDurationUnit)
  - [M GetInputParameterType ](#ApiClient.Hold.GetInputParameterType)
  - [M GetName ](#ApiClient.Hold.GetName)
  - [M GetPosX ](#ApiClient.Hold.GetPosX)
  - [M GetPosXUnit ](#ApiClient.Hold.GetPosXUnit)
  - [M GetPosY ](#ApiClient.Hold.GetPosY)
  - [M GetPosYUnit ](#ApiClient.Hold.GetPosYUnit)
  - [M GetPrompt ](#ApiClient.Hold.GetPrompt)
  - [M SetHoldDuration ](#ApiClient.Hold.SetHoldDuration)
  - [M SetInputParameterType ](#ApiClient.Hold.SetInputParameterType)
  - [M SetPosX ](#ApiClient.Hold.SetPosX)
  - [M SetPosY ](#ApiClient.Hold.SetPosY)
  - [M SetPrompt ](#ApiClient.Hold.SetPrompt)

# Hold[¶](#hold "Link to this heading")

*class* Hold[¶](#ApiClient.Hold "Link to this definition")  
Returned by

- [`TouchInputApi.CreateHold`](../TouchInputApi.md#ApiClient.TouchInputApi.CreateHold "ApiClient.TouchInputApi.CreateHold (Python method) — Create a new hold input action object.")

Clone()[¶](#ApiClient.Hold.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`Hold`](#ApiClient.Hold "ApiClient.Hold (Python class) — TouchInputApi.CreateHold")

GetHoldDuration()[¶](#ApiClient.Hold.GetHoldDuration "Link to this definition")  
Returns the value of the hold duration.

Returns:  Value of hold duration

Return type:  str

GetHoldDurationUnit()[¶](#ApiClient.Hold.GetHoldDurationUnit "Link to this definition")  
Returns the unit of the hold duration.

Returns:  Unit of hold duration

Return type:  str

GetInputParameterType()[¶](#ApiClient.Hold.GetInputParameterType "Link to this definition")  
Returns the type of the touch input action parameters.

Returns:  The type of the touch input action parameters (‘Coordinates’ or ‘Prompt’)

Return type:  str

GetName()[¶](#ApiClient.Hold.GetName "Link to this definition")  
Returns the name of the touch input action

Returns:  The name of the touch input action

Return type:  str

GetPosX()[¶](#ApiClient.Hold.GetPosX "Link to this definition")  
Returns value of the first coordinate.

Returns:  Value of x-coordinate

Return type:  str

GetPosXUnit()[¶](#ApiClient.Hold.GetPosXUnit "Link to this definition")  
Returns unit of the first coordinate.

Returns:  Unit of x-coordinate

Return type:  str

GetPosY()[¶](#ApiClient.Hold.GetPosY "Link to this definition")  
Returns value of the second coordinate.

Returns:  Value of y-coordinate

Return type:  str

GetPosYUnit()[¶](#ApiClient.Hold.GetPosYUnit "Link to this definition")  
Returns unit of the second coordinate.

Returns:  Unit of y-coordinate

Return type:  str

GetPrompt()[¶](#ApiClient.Hold.GetPrompt "Link to this definition")  
Returns the prompt expression for the touch input action.

Returns:  The prompt expression for the touch input action

Return type:  str

SetHoldDuration(*[expr](#ApiClient.Hold.SetHoldDuration.expr "ApiClient.Hold.SetHoldDuration.expr (Python parameter) — Hold duration")*, *[unit](#ApiClient.Hold.SetHoldDuration.unit "ApiClient.Hold.SetHoldDuration.unit (Python parameter) — unit of duration, milliseconds 'ms' or seconds 's'")=`'s'`*)[¶](#ApiClient.Hold.SetHoldDuration "Link to this definition")  
Sets the hold duration.

Parameters:  expr : str[¶](#ApiClient.Hold.SetHoldDuration.expr "Permalink to this definition")  
Hold duration

unit : str[¶](#ApiClient.Hold.SetHoldDuration.unit "Permalink to this definition")  
unit of duration, milliseconds ‘ms’ or seconds ‘s’

SetInputParameterType(*[parameterType](#ApiClient.Hold.SetInputParameterType.parameterType "ApiClient.Hold.SetInputParameterType.parameterType (Python parameter) — The type of the touch input action parameters ('Coordinates' or 'Prompt')")*)[¶](#ApiClient.Hold.SetInputParameterType "Link to this definition")  
Sets the type of the touch input action parameters.

Parameters:  parameterType : str[¶](#ApiClient.Hold.SetInputParameterType.parameterType "Permalink to this definition")  
The type of the touch input action parameters (‘Coordinates’ or ‘Prompt’)

SetPosX(*[expr](#ApiClient.Hold.SetPosX.expr "ApiClient.Hold.SetPosX.expr (Python parameter) — expression for x-coordinate of position")*, *[unit](#ApiClient.Hold.SetPosX.unit "ApiClient.Hold.SetPosX.unit (Python parameter) — unit of x-coordinate, absolute 'px' or relative '%'")=`'px'`*)[¶](#ApiClient.Hold.SetPosX "Link to this definition")  
Sets first coordinate of position.

Parameters:  expr : str[¶](#ApiClient.Hold.SetPosX.expr "Permalink to this definition")  
expression for x-coordinate of position

unit : str[¶](#ApiClient.Hold.SetPosX.unit "Permalink to this definition")  
unit of x-coordinate, absolute ‘px’ or relative ‘%’

SetPosY(*[expr](#ApiClient.Hold.SetPosY.expr "ApiClient.Hold.SetPosY.expr (Python parameter) — expression for y-coordinate of position")*, *[unit](#ApiClient.Hold.SetPosY.unit "ApiClient.Hold.SetPosY.unit (Python parameter) — unit of y-coordinate, absolute 'px' or relative '%'")=`'px'`*)[¶](#ApiClient.Hold.SetPosY "Link to this definition")  
Sets second coordinate of position.

Parameters:  expr : str[¶](#ApiClient.Hold.SetPosY.expr "Permalink to this definition")  
expression for y-coordinate of position

unit : str[¶](#ApiClient.Hold.SetPosY.unit "Permalink to this definition")  
unit of y-coordinate, absolute ‘px’ or relative ‘%’

SetPrompt(*[prompt](#ApiClient.Hold.SetPrompt.prompt "ApiClient.Hold.SetPrompt.prompt (Python parameter) — The prompt expression for the touch input action")*)[¶](#ApiClient.Hold.SetPrompt "Link to this definition")  
Sets the prompt expression for the touch input action.

Parameters:  prompt : str[¶](#ApiClient.Hold.SetPrompt.prompt "Permalink to this definition")  
The prompt expression for the touch input action

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
