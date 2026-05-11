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

MultiTap [ MultiTap ](#)

MultiTap

- [C MultiTap ](#ApiClient.MultiTap)
  - [M Clone ](#ApiClient.MultiTap.Clone)
  - [M GetCount ](#ApiClient.MultiTap.GetCount)
  - [M GetInputParameterType ](#ApiClient.MultiTap.GetInputParameterType)
  - [M GetInterval ](#ApiClient.MultiTap.GetInterval)
  - [M GetIntervalUnit ](#ApiClient.MultiTap.GetIntervalUnit)
  - [M GetName ](#ApiClient.MultiTap.GetName)
  - [M GetPosX ](#ApiClient.MultiTap.GetPosX)
  - [M GetPosXUnit ](#ApiClient.MultiTap.GetPosXUnit)
  - [M GetPosY ](#ApiClient.MultiTap.GetPosY)
  - [M GetPosYUnit ](#ApiClient.MultiTap.GetPosYUnit)
  - [M GetPrompt ](#ApiClient.MultiTap.GetPrompt)
  - [M SetCount ](#ApiClient.MultiTap.SetCount)
  - [M SetInputParameterType ](#ApiClient.MultiTap.SetInputParameterType)
  - [M SetInterval ](#ApiClient.MultiTap.SetInterval)
  - [M SetPosX ](#ApiClient.MultiTap.SetPosX)
  - [M SetPosY ](#ApiClient.MultiTap.SetPosY)
  - [M SetPrompt ](#ApiClient.MultiTap.SetPrompt)

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

MultiTap

- [C MultiTap ](#ApiClient.MultiTap)
  - [M Clone ](#ApiClient.MultiTap.Clone)
  - [M GetCount ](#ApiClient.MultiTap.GetCount)
  - [M GetInputParameterType ](#ApiClient.MultiTap.GetInputParameterType)
  - [M GetInterval ](#ApiClient.MultiTap.GetInterval)
  - [M GetIntervalUnit ](#ApiClient.MultiTap.GetIntervalUnit)
  - [M GetName ](#ApiClient.MultiTap.GetName)
  - [M GetPosX ](#ApiClient.MultiTap.GetPosX)
  - [M GetPosXUnit ](#ApiClient.MultiTap.GetPosXUnit)
  - [M GetPosY ](#ApiClient.MultiTap.GetPosY)
  - [M GetPosYUnit ](#ApiClient.MultiTap.GetPosYUnit)
  - [M GetPrompt ](#ApiClient.MultiTap.GetPrompt)
  - [M SetCount ](#ApiClient.MultiTap.SetCount)
  - [M SetInputParameterType ](#ApiClient.MultiTap.SetInputParameterType)
  - [M SetInterval ](#ApiClient.MultiTap.SetInterval)
  - [M SetPosX ](#ApiClient.MultiTap.SetPosX)
  - [M SetPosY ](#ApiClient.MultiTap.SetPosY)
  - [M SetPrompt ](#ApiClient.MultiTap.SetPrompt)

# MultiTap[¶](#multitap "Link to this heading")

*class* MultiTap[¶](#ApiClient.MultiTap "Link to this definition")  
Returned by

- [`TouchInputApi.CreateMultiTap`](../TouchInputApi.md#ApiClient.TouchInputApi.CreateMultiTap "ApiClient.TouchInputApi.CreateMultiTap (Python method) — Create a new multitap input action object.")

Clone()[¶](#ApiClient.MultiTap.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`MultiTap`](#ApiClient.MultiTap "ApiClient.MultiTap (Python class) — TouchInputApi.CreateMultiTap")

GetCount()[¶](#ApiClient.MultiTap.GetCount "Link to this definition")  
Returns the number of successive taps.

Returns:  Number of taps

Return type:  str

GetInputParameterType()[¶](#ApiClient.MultiTap.GetInputParameterType "Link to this definition")  
Returns the type of the touch input action parameters.

Returns:  The type of the touch input action parameters (‘Coordinates’ or ‘Prompt’)

Return type:  str

GetInterval()[¶](#ApiClient.MultiTap.GetInterval "Link to this definition")  
Returns the value of the time interval between successive taps.

Returns:  Value of time interval between taps

Return type:  str

GetIntervalUnit()[¶](#ApiClient.MultiTap.GetIntervalUnit "Link to this definition")  
Returns the unit of the time interval between successive taps.

:return:Unit of time interval between taps :rtype: str

GetName()[¶](#ApiClient.MultiTap.GetName "Link to this definition")  
Returns the name of the touch input action

Returns:  The name of the touch input action

Return type:  str

GetPosX()[¶](#ApiClient.MultiTap.GetPosX "Link to this definition")  
Returns value of the first coordinate.

Returns:  Value of x-coordinate

Return type:  str

GetPosXUnit()[¶](#ApiClient.MultiTap.GetPosXUnit "Link to this definition")  
Returns unit of the first coordinate.

Returns:  Unit of x-coordinate

Return type:  str

GetPosY()[¶](#ApiClient.MultiTap.GetPosY "Link to this definition")  
Returns value of the second coordinate.

Returns:  Value of y-coordinate

Return type:  str

GetPosYUnit()[¶](#ApiClient.MultiTap.GetPosYUnit "Link to this definition")  
Returns unit of the second coordinate.

Returns:  Unit of y-coordinate

Return type:  str

GetPrompt()[¶](#ApiClient.MultiTap.GetPrompt "Link to this definition")  
Returns the prompt expression for the touch input action.

Returns:  The prompt expression for the touch input action

Return type:  str

SetCount(*[expr](#ApiClient.MultiTap.SetCount.expr "ApiClient.MultiTap.SetCount.expr (Python parameter) — Number of taps")*)[¶](#ApiClient.MultiTap.SetCount "Link to this definition")  
Sets the number of successive taps.

Parameters:  expr : str[¶](#ApiClient.MultiTap.SetCount.expr "Permalink to this definition")  
Number of taps

SetInputParameterType(*[parameterType](#ApiClient.MultiTap.SetInputParameterType.parameterType "ApiClient.MultiTap.SetInputParameterType.parameterType (Python parameter) — The type of the touch input action parameters ('Coordinates' or 'Prompt')")*)[¶](#ApiClient.MultiTap.SetInputParameterType "Link to this definition")  
Sets the type of the touch input action parameters.

Parameters:  parameterType : str[¶](#ApiClient.MultiTap.SetInputParameterType.parameterType "Permalink to this definition")  
The type of the touch input action parameters (‘Coordinates’ or ‘Prompt’)

SetInterval(*[expr](#ApiClient.MultiTap.SetInterval.expr "ApiClient.MultiTap.SetInterval.expr (Python parameter) — Time interval between taps")*, *[unit](#ApiClient.MultiTap.SetInterval.unit "ApiClient.MultiTap.SetInterval.unit (Python parameter) — unit of time interval, milliseconds 'ms' or seconds 's'")=`'s'`*)[¶](#ApiClient.MultiTap.SetInterval "Link to this definition")  
Sets the time interval between successive taps.

Parameters:  expr : str[¶](#ApiClient.MultiTap.SetInterval.expr "Permalink to this definition")  
Time interval between taps

unit : str[¶](#ApiClient.MultiTap.SetInterval.unit "Permalink to this definition")  
unit of time interval, milliseconds ‘ms’ or seconds ‘s’

SetPosX(*[expr](#ApiClient.MultiTap.SetPosX.expr "ApiClient.MultiTap.SetPosX.expr (Python parameter) — expression for x-coordinate of position")*, *[unit](#ApiClient.MultiTap.SetPosX.unit "ApiClient.MultiTap.SetPosX.unit (Python parameter) — unit of x-coordinate, absolute 'px' or relative '%'")=`'px'`*)[¶](#ApiClient.MultiTap.SetPosX "Link to this definition")  
Sets first coordinate of position.

Parameters:  expr : str[¶](#ApiClient.MultiTap.SetPosX.expr "Permalink to this definition")  
expression for x-coordinate of position

unit : str[¶](#ApiClient.MultiTap.SetPosX.unit "Permalink to this definition")  
unit of x-coordinate, absolute ‘px’ or relative ‘%’

SetPosY(*[expr](#ApiClient.MultiTap.SetPosY.expr "ApiClient.MultiTap.SetPosY.expr (Python parameter) — expression for y-coordinate of position")*, *[unit](#ApiClient.MultiTap.SetPosY.unit "ApiClient.MultiTap.SetPosY.unit (Python parameter) — unit of y-coordinate, absolute 'px' or relative '%'")=`'px'`*)[¶](#ApiClient.MultiTap.SetPosY "Link to this definition")  
Sets second coordinate of position.

Parameters:  expr : str[¶](#ApiClient.MultiTap.SetPosY.expr "Permalink to this definition")  
expression for y-coordinate of position

unit : str[¶](#ApiClient.MultiTap.SetPosY.unit "Permalink to this definition")  
unit of y-coordinate, absolute ‘px’ or relative ‘%’

SetPrompt(*[prompt](#ApiClient.MultiTap.SetPrompt.prompt "ApiClient.MultiTap.SetPrompt.prompt (Python parameter) — The prompt expression for the touch input action")*)[¶](#ApiClient.MultiTap.SetPrompt "Link to this definition")  
Sets the prompt expression for the touch input action.

Parameters:  prompt : str[¶](#ApiClient.MultiTap.SetPrompt.prompt "Permalink to this definition")  
The prompt expression for the touch input action

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
