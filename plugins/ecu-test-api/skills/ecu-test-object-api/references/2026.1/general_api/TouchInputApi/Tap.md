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

[ Swipe ](Swipe.md)

Tap [ Tap ](#)

Tap

- [C Tap ](#ApiClient.Tap)
  - [M Clone ](#ApiClient.Tap.Clone)
  - [M GetInputParameterType ](#ApiClient.Tap.GetInputParameterType)
  - [M GetName ](#ApiClient.Tap.GetName)
  - [M GetPosX ](#ApiClient.Tap.GetPosX)
  - [M GetPosXUnit ](#ApiClient.Tap.GetPosXUnit)
  - [M GetPosY ](#ApiClient.Tap.GetPosY)
  - [M GetPosYUnit ](#ApiClient.Tap.GetPosYUnit)
  - [M GetPrompt ](#ApiClient.Tap.GetPrompt)
  - [M SetInputParameterType ](#ApiClient.Tap.SetInputParameterType)
  - [M SetPosX ](#ApiClient.Tap.SetPosX)
  - [M SetPosY ](#ApiClient.Tap.SetPosY)
  - [M SetPrompt ](#ApiClient.Tap.SetPrompt)

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

Tap

- [C Tap ](#ApiClient.Tap)
  - [M Clone ](#ApiClient.Tap.Clone)
  - [M GetInputParameterType ](#ApiClient.Tap.GetInputParameterType)
  - [M GetName ](#ApiClient.Tap.GetName)
  - [M GetPosX ](#ApiClient.Tap.GetPosX)
  - [M GetPosXUnit ](#ApiClient.Tap.GetPosXUnit)
  - [M GetPosY ](#ApiClient.Tap.GetPosY)
  - [M GetPosYUnit ](#ApiClient.Tap.GetPosYUnit)
  - [M GetPrompt ](#ApiClient.Tap.GetPrompt)
  - [M SetInputParameterType ](#ApiClient.Tap.SetInputParameterType)
  - [M SetPosX ](#ApiClient.Tap.SetPosX)
  - [M SetPosY ](#ApiClient.Tap.SetPosY)
  - [M SetPrompt ](#ApiClient.Tap.SetPrompt)

# Tap[¶](#tap "Link to this heading")

*class* Tap[¶](#ApiClient.Tap "Link to this definition")  
Returned by

- [`TouchInputApi.CreateTap`](../TouchInputApi.md#ApiClient.TouchInputApi.CreateTap "ApiClient.TouchInputApi.CreateTap (Python method) — Create a new tap input action object.")

Clone()[¶](#ApiClient.Tap.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`Tap`](#ApiClient.Tap "ApiClient.Tap (Python class) — TouchInputApi.CreateTap")

GetInputParameterType()[¶](#ApiClient.Tap.GetInputParameterType "Link to this definition")  
Returns the type of the touch input action parameters.

Returns:  The type of the touch input action parameters (‘Coordinates’ or ‘Prompt’)

Return type:  str

GetName()[¶](#ApiClient.Tap.GetName "Link to this definition")  
Returns the name of the touch input action

Returns:  The name of the touch input action

Return type:  str

GetPosX()[¶](#ApiClient.Tap.GetPosX "Link to this definition")  
Returns value of the first coordinate.

Returns:  Value of x-coordinate

Return type:  str

GetPosXUnit()[¶](#ApiClient.Tap.GetPosXUnit "Link to this definition")  
Returns unit of the first coordinate.

Returns:  Unit of x-coordinate

Return type:  str

GetPosY()[¶](#ApiClient.Tap.GetPosY "Link to this definition")  
Returns value of the second coordinate.

Returns:  Value of y-coordinate

Return type:  str

GetPosYUnit()[¶](#ApiClient.Tap.GetPosYUnit "Link to this definition")  
Returns unit of the second coordinate.

Returns:  Unit of y-coordinate

Return type:  str

GetPrompt()[¶](#ApiClient.Tap.GetPrompt "Link to this definition")  
Returns the prompt expression for the touch input action.

Returns:  The prompt expression for the touch input action

Return type:  str

SetInputParameterType(*[parameterType](#ApiClient.Tap.SetInputParameterType.parameterType "ApiClient.Tap.SetInputParameterType.parameterType (Python parameter) — The type of the touch input action parameters ('Coordinates' or 'Prompt')")*)[¶](#ApiClient.Tap.SetInputParameterType "Link to this definition")  
Sets the type of the touch input action parameters.

Parameters:  parameterType : str[¶](#ApiClient.Tap.SetInputParameterType.parameterType "Permalink to this definition")  
The type of the touch input action parameters (‘Coordinates’ or ‘Prompt’)

SetPosX(*[expr](#ApiClient.Tap.SetPosX.expr "ApiClient.Tap.SetPosX.expr (Python parameter) — expression for x-coordinate of position")*, *[unit](#ApiClient.Tap.SetPosX.unit "ApiClient.Tap.SetPosX.unit (Python parameter) — unit of x-coordinate, absolute 'px' or relative '%'")=`'px'`*)[¶](#ApiClient.Tap.SetPosX "Link to this definition")  
Sets first coordinate of position.

Parameters:  expr : str[¶](#ApiClient.Tap.SetPosX.expr "Permalink to this definition")  
expression for x-coordinate of position

unit : str[¶](#ApiClient.Tap.SetPosX.unit "Permalink to this definition")  
unit of x-coordinate, absolute ‘px’ or relative ‘%’

SetPosY(*[expr](#ApiClient.Tap.SetPosY.expr "ApiClient.Tap.SetPosY.expr (Python parameter) — expression for y-coordinate of position")*, *[unit](#ApiClient.Tap.SetPosY.unit "ApiClient.Tap.SetPosY.unit (Python parameter) — unit of y-coordinate, absolute 'px' or relative '%'")=`'px'`*)[¶](#ApiClient.Tap.SetPosY "Link to this definition")  
Sets second coordinate of position.

Parameters:  expr : str[¶](#ApiClient.Tap.SetPosY.expr "Permalink to this definition")  
expression for y-coordinate of position

unit : str[¶](#ApiClient.Tap.SetPosY.unit "Permalink to this definition")  
unit of y-coordinate, absolute ‘px’ or relative ‘%’

SetPrompt(*[prompt](#ApiClient.Tap.SetPrompt.prompt "ApiClient.Tap.SetPrompt.prompt (Python parameter) — The prompt expression for the touch input action")*)[¶](#ApiClient.Tap.SetPrompt "Link to this definition")  
Sets the prompt expression for the touch input action.

Parameters:  prompt : str[¶](#ApiClient.Tap.SetPrompt.prompt "Permalink to this definition")  
The prompt expression for the touch input action

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
