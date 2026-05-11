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

API for Multimedia Objects

Mask [ Mask ](#)

Mask

- [C Mask ](#ApiClient.Mask)
  - [M Clone ](#ApiClient.Mask.Clone)
  - [M GetDistanceX ](#ApiClient.Mask.GetDistanceX)
  - [M GetDistanceY ](#ApiClient.Mask.GetDistanceY)
  - [M GetHeight ](#ApiClient.Mask.GetHeight)
  - [M GetName ](#ApiClient.Mask.GetName)
  - [M GetRepetitionX ](#ApiClient.Mask.GetRepetitionX)
  - [M GetRepetitionY ](#ApiClient.Mask.GetRepetitionY)
  - [M GetWidth ](#ApiClient.Mask.GetWidth)
  - [M GetX ](#ApiClient.Mask.GetX)
  - [M GetY ](#ApiClient.Mask.GetY)
  - [M Save ](#ApiClient.Mask.Save)
  - [M SetDistanceX ](#ApiClient.Mask.SetDistanceX)
  - [M SetDistanceY ](#ApiClient.Mask.SetDistanceY)
  - [M SetHeight ](#ApiClient.Mask.SetHeight)
  - [M SetRepetitionX ](#ApiClient.Mask.SetRepetitionX)
  - [M SetRepetitionY ](#ApiClient.Mask.SetRepetitionY)
  - [M SetWidth ](#ApiClient.Mask.SetWidth)
  - [M SetX ](#ApiClient.Mask.SetX)
  - [M SetY ](#ApiClient.Mask.SetY)

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

[ API for Variables ](../VariableApi.md)

[ API for Workspaces ](../WorkspaceApi.md)

[ Trace Analysis API ](../../TraceAnalysisAPI/index.md)

[ Generator APIs ](../../generators/index.md)

[ Tools ](../../tools/index.md)

[ User test management ](../../userTestmanagement/index.md)

[ UserUtility API ](../../user-utility/user-utility.md)

[ Utility Examples ](../../user-utility/example-utilities.md)

Mask

- [C Mask ](#ApiClient.Mask)
  - [M Clone ](#ApiClient.Mask.Clone)
  - [M GetDistanceX ](#ApiClient.Mask.GetDistanceX)
  - [M GetDistanceY ](#ApiClient.Mask.GetDistanceY)
  - [M GetHeight ](#ApiClient.Mask.GetHeight)
  - [M GetName ](#ApiClient.Mask.GetName)
  - [M GetRepetitionX ](#ApiClient.Mask.GetRepetitionX)
  - [M GetRepetitionY ](#ApiClient.Mask.GetRepetitionY)
  - [M GetWidth ](#ApiClient.Mask.GetWidth)
  - [M GetX ](#ApiClient.Mask.GetX)
  - [M GetY ](#ApiClient.Mask.GetY)
  - [M Save ](#ApiClient.Mask.Save)
  - [M SetDistanceX ](#ApiClient.Mask.SetDistanceX)
  - [M SetDistanceY ](#ApiClient.Mask.SetDistanceY)
  - [M SetHeight ](#ApiClient.Mask.SetHeight)
  - [M SetRepetitionX ](#ApiClient.Mask.SetRepetitionX)
  - [M SetRepetitionY ](#ApiClient.Mask.SetRepetitionY)
  - [M SetWidth ](#ApiClient.Mask.SetWidth)
  - [M SetX ](#ApiClient.Mask.SetX)
  - [M SetY ](#ApiClient.Mask.SetY)

# Mask[¶](#mask "Link to this heading")

*class* Mask[¶](#ApiClient.Mask "Link to this definition")  
Returned by

- [`MultimediaApi.CreateMask`](../MultimediaApi.md#ApiClient.MultimediaApi.CreateMask "ApiClient.MultimediaApi.CreateMask (Python method) — Create a new image mask.")

- [`MultimediaApi.OpenMask`](../MultimediaApi.md#ApiClient.MultimediaApi.OpenMask "ApiClient.MultimediaApi.OpenMask (Python method) — Opens an existing image mask.")

Clone()[¶](#ApiClient.Mask.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`Mask`](#ApiClient.Mask "ApiClient.Mask (Python class) — MultimediaApi.CreateMask")

GetDistanceX()[¶](#ApiClient.Mask.GetDistanceX "Link to this definition")  
Returns the horizontal offset between each duplicated instance of this mask. See [`SetRepetitionX()`](#ApiClient.Mask.SetRepetitionX "ApiClient.Mask.SetRepetitionX (Python method) — Sets how many times the mask will be duplicated in horizontal direction.") to configure horizontal repetition.

Returns:  Horizontal distance between repetitions

Return type:  int

GetDistanceY()[¶](#ApiClient.Mask.GetDistanceY "Link to this definition")  
Returns the vertical offset between each duplicated instance of this mask. See [`SetRepetitionY()`](#ApiClient.Mask.SetRepetitionY "ApiClient.Mask.SetRepetitionY (Python method) — Sets how many times the mask will be duplicated in vertical direction.") to configure vertical repetition.

Returns:  Vertical distance between repetitions

Return type:  int

GetHeight()[¶](#ApiClient.Mask.GetHeight "Link to this definition")  
Returns the mask height.

Returns:  Mask height

Return type:  int

GetName()[¶](#ApiClient.Mask.GetName "Link to this definition")  
Returns the name of this mask. Only applicable for submasks. The root mask of a mask file has no name. Instead, it will be referenced at runtime using its filename.

Returns:  The mask name if it is a submask, otherwise None

Return type:  str

GetRepetitionX()[¶](#ApiClient.Mask.GetRepetitionX "Link to this definition")  
Returns the horizontal repetition. The mask will be duplicated this amount of times in horizontal direction.

Returns:  Horizontal repetition

Return type:  int

GetRepetitionY()[¶](#ApiClient.Mask.GetRepetitionY "Link to this definition")  
Returns the vertical repetition. The mask will be duplicated this amount of times in vertical direction.

Returns:  Vertical repetition

Return type:  int

GetWidth()[¶](#ApiClient.Mask.GetWidth "Link to this definition")  
Returns the mask width.

Returns:  Mask width

Return type:  int

GetX()[¶](#ApiClient.Mask.GetX "Link to this definition")  
Returns the x position.

Returns:  x position

Return type:  int

GetY()[¶](#ApiClient.Mask.GetY "Link to this definition")  
Returns the y position.

Returns:  y position

Return type:  int

Save(*[filePath](#ApiClient.Mask.Save.filePath "ApiClient.Mask.Save.filePath (Python parameter) — Filename or path to the mask file.")*)[¶](#ApiClient.Mask.Save "Link to this definition")  
Saves the mask to a file.

Parameters:  filePath : str[¶](#ApiClient.Mask.Save.filePath "Permalink to this definition")  
Filename or path to the mask file. A relative path will be resolved to the ‘Images’ directory of the current workspace.

SetDistanceX(*[distanceX](#ApiClient.Mask.SetDistanceX.distanceX "ApiClient.Mask.SetDistanceX.distanceX (Python parameter) — New horizontal distance between repetitions")*)[¶](#ApiClient.Mask.SetDistanceX "Link to this definition")  
Sets the horizontal offset between each duplicated instance of this mask. See [`SetRepetitionX()`](#ApiClient.Mask.SetRepetitionX "ApiClient.Mask.SetRepetitionX (Python method) — Sets how many times the mask will be duplicated in horizontal direction.") to configure horizontal repetition.

Parameters:  distanceX : int[¶](#ApiClient.Mask.SetDistanceX.distanceX "Permalink to this definition")  
New horizontal distance between repetitions

SetDistanceY(*[distanceY](#ApiClient.Mask.SetDistanceY.distanceY "ApiClient.Mask.SetDistanceY.distanceY (Python parameter) — New vertical distance between repetitions")*)[¶](#ApiClient.Mask.SetDistanceY "Link to this definition")  
Sets the vertical offset between each duplicated instance of this mask. See [`SetRepetitionY()`](#ApiClient.Mask.SetRepetitionY "ApiClient.Mask.SetRepetitionY (Python method) — Sets how many times the mask will be duplicated in vertical direction.") to configure vertical repetition.

Parameters:  distanceY : int[¶](#ApiClient.Mask.SetDistanceY.distanceY "Permalink to this definition")  
New vertical distance between repetitions

SetHeight(*[height](#ApiClient.Mask.SetHeight.height "ApiClient.Mask.SetHeight.height (Python parameter) — New height")*)[¶](#ApiClient.Mask.SetHeight "Link to this definition")  
Sets the mask height.

Parameters:  height : int[¶](#ApiClient.Mask.SetHeight.height "Permalink to this definition")  
New height

SetRepetitionX(*[repetitionX](#ApiClient.Mask.SetRepetitionX.repetitionX "ApiClient.Mask.SetRepetitionX.repetitionX (Python parameter) — New horizontal repetition")*)[¶](#ApiClient.Mask.SetRepetitionX "Link to this definition")  
Sets how many times the mask will be duplicated in horizontal direction.

Parameters:  repetitionX : int[¶](#ApiClient.Mask.SetRepetitionX.repetitionX "Permalink to this definition")  
New horizontal repetition

SetRepetitionY(*[repetitionY](#ApiClient.Mask.SetRepetitionY.repetitionY "ApiClient.Mask.SetRepetitionY.repetitionY (Python parameter) — New vertical repetition")*)[¶](#ApiClient.Mask.SetRepetitionY "Link to this definition")  
Sets how many times the mask will be duplicated in vertical direction.

Parameters:  repetitionY : int[¶](#ApiClient.Mask.SetRepetitionY.repetitionY "Permalink to this definition")  
New vertical repetition

SetWidth(*[width](#ApiClient.Mask.SetWidth.width "ApiClient.Mask.SetWidth.width (Python parameter) — New width")*)[¶](#ApiClient.Mask.SetWidth "Link to this definition")  
Sets the mask width.

Parameters:  width : int[¶](#ApiClient.Mask.SetWidth.width "Permalink to this definition")  
New width

SetX(*[x](#ApiClient.Mask.SetX.x "ApiClient.Mask.SetX.x (Python parameter) — New x position")*)[¶](#ApiClient.Mask.SetX "Link to this definition")  
Sets the x position. If repetition is active, this defines the left edge of the first instance of this mask.

Parameters:  x : int[¶](#ApiClient.Mask.SetX.x "Permalink to this definition")  
New x position

SetY(*[y](#ApiClient.Mask.SetY.y "ApiClient.Mask.SetY.y (Python parameter) — New y position")*)[¶](#ApiClient.Mask.SetY "Link to this definition")  
Sets the y position. If repetition is active, this defines the upper edge of the first instance of this mask.

Parameters:  y : int[¶](#ApiClient.Mask.SetY.y "Permalink to this definition")  
New y position

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
