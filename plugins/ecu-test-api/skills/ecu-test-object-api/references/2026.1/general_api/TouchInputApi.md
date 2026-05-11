[ Internal APIs ](api.md)

[ Advanced operations of package variable types ](variabledatastructures.md)

[ Advanced properties of bus-related objects ](busdatastructures.md)

[ Bus related objects of trace analysis ](busdatastructuresTraceanalysis.md)

[ Advanced properties of diagnostics-related objects ](diagdatastructures.md)

[ Diagnostics related objects of trace analysis ](diagdatastructuresTraceanalysis.md)

[ Advanced properties of media-related objects ](mediadatastructures.md)

[ Advanced properties of DLT logging-related objects ](dltdatastructures.md)

[ COM API ](com-api.md)

[ REST API ](rest-api.md)

[ Report API ](apireport.md)

[ Object API ](objectApi.md)

Object API

[ API entry points ](objectApi.md#api-entry-points)

API entry points

[ API for Analysis Jobs ](AnalysisJobApi.md)

[ API for Artifacts ](ArtifactApi.md)

[ API for Project Components ](ComponentApi.md)

[ API for Configurations ](ConfigurationApi.md)

[ API for Expectations ](ExpectationApi.md)

[ API for Expressions ](ExpressionApi.md)

[ API for Global Mappings ](GlobalMappingApi.md)

[ API for Mappings ](MappingApi.md)

[ API for Multimedia Objects ](MultimediaApi.md)

[ API for Packages ](PackageApi.md)

[ API for Parameters ](ParameterApi.md)

[ API for Projects ](ProjectApi.md)

[ API for Relations ](RelationApi.md)

[ API for Reports ](ReportApi.md)

[ API for Report Filters ](ReportFilterApi.md)

[ API for Settings ](SettingsApi.md)

[ API for Signals ](SignalApi.md)

[ API for Signal Descriptions ](SignalDescriptionApi.md)

[ API for Signal Recordings ](SignalRecordingApi.md)

[ API for Symbols ](SymbolApi.md)

[ API for Test Steps ](TestStepApi.md)

[ API for Touch Inputs ](#)

API for Touch Inputs

- [ Hold ](TouchInputApi/Hold.md)
- [ HoldAndSwipe ](TouchInputApi/HoldAndSwipe.md)
- [ MultiSwipe ](TouchInputApi/MultiSwipe.md)
- [ MultiTap ](TouchInputApi/MultiTap.md)
- [ Pinch ](TouchInputApi/Pinch.md)
- [ Rotate ](TouchInputApi/Rotate.md)
- [ Swipe ](TouchInputApi/Swipe.md)
- [ Tap ](TouchInputApi/Tap.md)

API for Touch Inputs [ API for Touch Inputs ](#)

API for Touch Inputs

- [C TouchInputApi ](#ApiClient.TouchInputApi)
  - [M CreateHold ](#ApiClient.TouchInputApi.CreateHold)
  - [M CreateHoldAndSwipe ](#ApiClient.TouchInputApi.CreateHoldAndSwipe)
  - [M CreateMultiSwipe ](#ApiClient.TouchInputApi.CreateMultiSwipe)
  - [M CreateMultiTap ](#ApiClient.TouchInputApi.CreateMultiTap)
  - [M CreatePinch ](#ApiClient.TouchInputApi.CreatePinch)
  - [M CreateRotate ](#ApiClient.TouchInputApi.CreateRotate)
  - [M CreateSwipe ](#ApiClient.TouchInputApi.CreateSwipe)
  - [M CreateTap ](#ApiClient.TouchInputApi.CreateTap)
- [ Hold ](TouchInputApi/Hold.md)
- [ HoldAndSwipe ](TouchInputApi/HoldAndSwipe.md)
- [ MultiSwipe ](TouchInputApi/MultiSwipe.md)
- [ MultiTap ](TouchInputApi/MultiTap.md)
- [ Pinch ](TouchInputApi/Pinch.md)
- [ Rotate ](TouchInputApi/Rotate.md)
- [ Swipe ](TouchInputApi/Swipe.md)
- [ Tap ](TouchInputApi/Tap.md)

[ API for Trace Analyses ](TraceAnalysisApi.md)

[ API for Trace Files ](TraceFileApi.md)

[ API for Trace Step Templates ](TraceStepTemplateApi.md)

[ API for Variables ](VariableApi.md)

[ API for Workspaces ](WorkspaceApi.md)

[ Trace Analysis API ](../TraceAnalysisAPI/index.md)

[ Generator APIs ](../generators/index.md)

[ Tools ](../tools/index.md)

[ User test management ](../userTestmanagement/index.md)

[ UserUtility API ](../user-utility/user-utility.md)

[ Utility Examples ](../user-utility/example-utilities.md)

API for Touch Inputs

- [C TouchInputApi ](#ApiClient.TouchInputApi)
  - [M CreateHold ](#ApiClient.TouchInputApi.CreateHold)
  - [M CreateHoldAndSwipe ](#ApiClient.TouchInputApi.CreateHoldAndSwipe)
  - [M CreateMultiSwipe ](#ApiClient.TouchInputApi.CreateMultiSwipe)
  - [M CreateMultiTap ](#ApiClient.TouchInputApi.CreateMultiTap)
  - [M CreatePinch ](#ApiClient.TouchInputApi.CreatePinch)
  - [M CreateRotate ](#ApiClient.TouchInputApi.CreateRotate)
  - [M CreateSwipe ](#ApiClient.TouchInputApi.CreateSwipe)
  - [M CreateTap ](#ApiClient.TouchInputApi.CreateTap)

# API for Touch Inputs[¶](#api-for-touch-inputs "Link to this heading")

Part of the [Object based program API](objectApi.md#objectapi).

*class* TouchInputApi[¶](#ApiClient.TouchInputApi "Link to this definition")  
API to create touch input actions

Returned by

- [`MultimediaApi.TouchInputApi`](MultimediaApi.md#ApiClient.MultimediaApi.TouchInputApi "ApiClient.MultimediaApi.TouchInputApi (Python attribute) — Returns the TouchInputApi namespace.")

CreateHold(*[posX](#ApiClient.TouchInputApi.CreateHold.posX "ApiClient.TouchInputApi.CreateHold.posX (Python parameter) — Pixel position of first coordinate")=`'0'`*, *[posY](#ApiClient.TouchInputApi.CreateHold.posY "ApiClient.TouchInputApi.CreateHold.posY (Python parameter) — Pixel position of second coordinate")=`'0'`*, *[duration](#ApiClient.TouchInputApi.CreateHold.duration "ApiClient.TouchInputApi.CreateHold.duration (Python parameter) — Hold duration in seconds")=`'1.0'`*, *[prompt](#ApiClient.TouchInputApi.CreateHold.prompt "ApiClient.TouchInputApi.CreateHold.prompt (Python parameter) — Prompt text to use instead of coordinates")=`None`*)[¶](#ApiClient.TouchInputApi.CreateHold "Link to this definition")  
Create a new hold input action object.

Parameters:  posX : str[¶](#ApiClient.TouchInputApi.CreateHold.posX "Permalink to this definition")  
Pixel position of first coordinate

posY : str[¶](#ApiClient.TouchInputApi.CreateHold.posY "Permalink to this definition")  
Pixel position of second coordinate

duration : str[¶](#ApiClient.TouchInputApi.CreateHold.duration "Permalink to this definition")  
Hold duration in seconds

prompt : str[¶](#ApiClient.TouchInputApi.CreateHold.prompt "Permalink to this definition")  
Prompt text to use instead of coordinates

Returns:  A new hold object

Return type:  [`Hold`](TouchInputApi/Hold.md#ApiClient.Hold "ApiClient.Hold (Python class) — TouchInputApi.CreateHold")

CreateHoldAndSwipe(*[startX](#ApiClient.TouchInputApi.CreateHoldAndSwipe.startX "ApiClient.TouchInputApi.CreateHoldAndSwipe.startX (Python parameter) — Starting pixel position of first coordinate")=`'0'`*, *[startY](#ApiClient.TouchInputApi.CreateHoldAndSwipe.startY "ApiClient.TouchInputApi.CreateHoldAndSwipe.startY (Python parameter) — Starting pixel position of second coordinate")=`'0'`*, *[endX](#ApiClient.TouchInputApi.CreateHoldAndSwipe.endX "ApiClient.TouchInputApi.CreateHoldAndSwipe.endX (Python parameter) — Final pixel position of first coordinate")=`'0'`*, *[endY](#ApiClient.TouchInputApi.CreateHoldAndSwipe.endY "ApiClient.TouchInputApi.CreateHoldAndSwipe.endY (Python parameter) — Final pixel position of second coordinate")=`'0'`*, *[holdDuration](#ApiClient.TouchInputApi.CreateHoldAndSwipe.holdDuration "ApiClient.TouchInputApi.CreateHoldAndSwipe.holdDuration (Python parameter) — Duration of initial hold in seconds")=`'1.0'`*, *[swipeDuration](#ApiClient.TouchInputApi.CreateHoldAndSwipe.swipeDuration "ApiClient.TouchInputApi.CreateHoldAndSwipe.swipeDuration (Python parameter) — Duration of swipe gesture in seconds")=`'1.0'`*, *[prompt](#ApiClient.TouchInputApi.CreateHoldAndSwipe.prompt "ApiClient.TouchInputApi.CreateHoldAndSwipe.prompt (Python parameter) — Prompt text to use instead of coordinates")=`None`*)[¶](#ApiClient.TouchInputApi.CreateHoldAndSwipe "Link to this definition")  
Create a new hold-and-swipe input action object.

Parameters:  startX : str[¶](#ApiClient.TouchInputApi.CreateHoldAndSwipe.startX "Permalink to this definition")  
Starting pixel position of first coordinate

startY : str[¶](#ApiClient.TouchInputApi.CreateHoldAndSwipe.startY "Permalink to this definition")  
Starting pixel position of second coordinate

endX : str[¶](#ApiClient.TouchInputApi.CreateHoldAndSwipe.endX "Permalink to this definition")  
Final pixel position of first coordinate

endY : str[¶](#ApiClient.TouchInputApi.CreateHoldAndSwipe.endY "Permalink to this definition")  
Final pixel position of second coordinate

holdDuration : str[¶](#ApiClient.TouchInputApi.CreateHoldAndSwipe.holdDuration "Permalink to this definition")  
Duration of initial hold in seconds

swipeDuration : str[¶](#ApiClient.TouchInputApi.CreateHoldAndSwipe.swipeDuration "Permalink to this definition")  
Duration of swipe gesture in seconds

prompt : str[¶](#ApiClient.TouchInputApi.CreateHoldAndSwipe.prompt "Permalink to this definition")  
Prompt text to use instead of coordinates

Returns:  A new hold-and-swipe object

Return type:  [`HoldAndSwipe`](TouchInputApi/HoldAndSwipe.md#ApiClient.HoldAndSwipe "ApiClient.HoldAndSwipe (Python class) — TouchInputApi.CreateHoldAndSwipe")

CreateMultiSwipe(*[startX](#ApiClient.TouchInputApi.CreateMultiSwipe.startX "ApiClient.TouchInputApi.CreateMultiSwipe.startX (Python parameter) — Starting pixel position of first coordinate")=`'0'`*, *[startY](#ApiClient.TouchInputApi.CreateMultiSwipe.startY "ApiClient.TouchInputApi.CreateMultiSwipe.startY (Python parameter) — Starting pixel position of second coordinate")=`'0'`*, *[endX](#ApiClient.TouchInputApi.CreateMultiSwipe.endX "ApiClient.TouchInputApi.CreateMultiSwipe.endX (Python parameter) — Final pixel position of first coordinate")=`'0'`*, *[endY](#ApiClient.TouchInputApi.CreateMultiSwipe.endY "ApiClient.TouchInputApi.CreateMultiSwipe.endY (Python parameter) — Final pixel position of second coordinate")=`'0'`*, *[duration](#ApiClient.TouchInputApi.CreateMultiSwipe.duration "ApiClient.TouchInputApi.CreateMultiSwipe.duration (Python parameter) — Duration of gesture in seconds")=`'1.0'`*, *[fingerCount](#ApiClient.TouchInputApi.CreateMultiSwipe.fingerCount "ApiClient.TouchInputApi.CreateMultiSwipe.fingerCount (Python parameter) — Number of fingers performing the swipe")=`'2'`*, *[distance](#ApiClient.TouchInputApi.CreateMultiSwipe.distance "ApiClient.TouchInputApi.CreateMultiSwipe.distance (Python parameter) — Mean Euclidean pixel distance between fingers")=`'10'`*, *[prompt](#ApiClient.TouchInputApi.CreateMultiSwipe.prompt "ApiClient.TouchInputApi.CreateMultiSwipe.prompt (Python parameter) — Prompt text to use instead of coordinates")=`None`*)[¶](#ApiClient.TouchInputApi.CreateMultiSwipe "Link to this definition")  
Create a new multiswipe input action object.

Parameters:  startX : str[¶](#ApiClient.TouchInputApi.CreateMultiSwipe.startX "Permalink to this definition")  
Starting pixel position of first coordinate

startY : str[¶](#ApiClient.TouchInputApi.CreateMultiSwipe.startY "Permalink to this definition")  
Starting pixel position of second coordinate

endX : str[¶](#ApiClient.TouchInputApi.CreateMultiSwipe.endX "Permalink to this definition")  
Final pixel position of first coordinate

endY : str[¶](#ApiClient.TouchInputApi.CreateMultiSwipe.endY "Permalink to this definition")  
Final pixel position of second coordinate

duration : str[¶](#ApiClient.TouchInputApi.CreateMultiSwipe.duration "Permalink to this definition")  
Duration of gesture in seconds

fingerCount : str[¶](#ApiClient.TouchInputApi.CreateMultiSwipe.fingerCount "Permalink to this definition")  
Number of fingers performing the swipe

distance : str[¶](#ApiClient.TouchInputApi.CreateMultiSwipe.distance "Permalink to this definition")  
Mean Euclidean pixel distance between fingers

prompt : str[¶](#ApiClient.TouchInputApi.CreateMultiSwipe.prompt "Permalink to this definition")  
Prompt text to use instead of coordinates

Returns:  A new multiswipe object

Return type:  [`MultiSwipe`](TouchInputApi/MultiSwipe.md#ApiClient.MultiSwipe "ApiClient.MultiSwipe (Python class) — TouchInputApi.CreateMultiSwipe")

CreateMultiTap(*[posX](#ApiClient.TouchInputApi.CreateMultiTap.posX "ApiClient.TouchInputApi.CreateMultiTap.posX (Python parameter) — Pixel position of first coordinate")=`'0'`*, *[posY](#ApiClient.TouchInputApi.CreateMultiTap.posY "ApiClient.TouchInputApi.CreateMultiTap.posY (Python parameter) — Pixel position of second coordinate")=`'0'`*, *[count](#ApiClient.TouchInputApi.CreateMultiTap.count "ApiClient.TouchInputApi.CreateMultiTap.count (Python parameter) — Number of successive taps")=`'2'`*, *[interval](#ApiClient.TouchInputApi.CreateMultiTap.interval "ApiClient.TouchInputApi.CreateMultiTap.interval (Python parameter) — Time interval between successive taps in seconds")=`'1.0'`*, *[prompt](#ApiClient.TouchInputApi.CreateMultiTap.prompt "ApiClient.TouchInputApi.CreateMultiTap.prompt (Python parameter) — Prompt text to use instead of coordinates")=`None`*)[¶](#ApiClient.TouchInputApi.CreateMultiTap "Link to this definition")  
Create a new multitap input action object.

Parameters:  posX : str[¶](#ApiClient.TouchInputApi.CreateMultiTap.posX "Permalink to this definition")  
Pixel position of first coordinate

posY : str[¶](#ApiClient.TouchInputApi.CreateMultiTap.posY "Permalink to this definition")  
Pixel position of second coordinate

count : str[¶](#ApiClient.TouchInputApi.CreateMultiTap.count "Permalink to this definition")  
Number of successive taps

interval : str[¶](#ApiClient.TouchInputApi.CreateMultiTap.interval "Permalink to this definition")  
Time interval between successive taps in seconds

prompt : str[¶](#ApiClient.TouchInputApi.CreateMultiTap.prompt "Permalink to this definition")  
Prompt text to use instead of coordinates

Returns:  A new multitap object

Return type:  [`MultiTap`](TouchInputApi/MultiTap.md#ApiClient.MultiTap "ApiClient.MultiTap (Python class) — TouchInputApi.CreateMultiTap")

CreatePinch(*[pos1X](#ApiClient.TouchInputApi.CreatePinch.pos1X "ApiClient.TouchInputApi.CreatePinch.pos1X (Python parameter) — x-coordinate of first finger's pixel position")=`'0'`*, *[pos1Y](#ApiClient.TouchInputApi.CreatePinch.pos1Y "ApiClient.TouchInputApi.CreatePinch.pos1Y (Python parameter) — y-coordinate of first finger's pixel position")=`'0'`*, *[pos2X](#ApiClient.TouchInputApi.CreatePinch.pos2X "ApiClient.TouchInputApi.CreatePinch.pos2X (Python parameter) — x-coordinate of second finger's pixel position")=`'0'`*, *[pos2Y](#ApiClient.TouchInputApi.CreatePinch.pos2Y "ApiClient.TouchInputApi.CreatePinch.pos2Y (Python parameter) — y-coordinate of second finger's pixel position")=`'0'`*, *[duration](#ApiClient.TouchInputApi.CreatePinch.duration "ApiClient.TouchInputApi.CreatePinch.duration (Python parameter) — Duration of gesture in seconds")=`'1.0'`*, *[scale](#ApiClient.TouchInputApi.CreatePinch.scale "ApiClient.TouchInputApi.CreatePinch.scale (Python parameter) — Scaling factor of gesture")=`'1.5'`*, *[prompt](#ApiClient.TouchInputApi.CreatePinch.prompt "ApiClient.TouchInputApi.CreatePinch.prompt (Python parameter) — Prompt text to use instead of coordinates")=`None`*)[¶](#ApiClient.TouchInputApi.CreatePinch "Link to this definition")  
Create a new pinch input action object.

Parameters:  pos1X : str[¶](#ApiClient.TouchInputApi.CreatePinch.pos1X "Permalink to this definition")  
x-coordinate of first finger’s pixel position

pos1Y : str[¶](#ApiClient.TouchInputApi.CreatePinch.pos1Y "Permalink to this definition")  
y-coordinate of first finger’s pixel position

pos2X : str[¶](#ApiClient.TouchInputApi.CreatePinch.pos2X "Permalink to this definition")  
x-coordinate of second finger’s pixel position

pos2Y : str[¶](#ApiClient.TouchInputApi.CreatePinch.pos2Y "Permalink to this definition")  
y-coordinate of second finger’s pixel position

duration : str[¶](#ApiClient.TouchInputApi.CreatePinch.duration "Permalink to this definition")  
Duration of gesture in seconds

scale : str[¶](#ApiClient.TouchInputApi.CreatePinch.scale "Permalink to this definition")  
Scaling factor of gesture

prompt : str[¶](#ApiClient.TouchInputApi.CreatePinch.prompt "Permalink to this definition")  
Prompt text to use instead of coordinates

Returns:  A new pinch object

Return type:  [`Pinch`](TouchInputApi/Pinch.md#ApiClient.Pinch "ApiClient.Pinch (Python class) — TouchInputApi.CreatePinch")

CreateRotate(*[pos1X](#ApiClient.TouchInputApi.CreateRotate.pos1X "ApiClient.TouchInputApi.CreateRotate.pos1X (Python parameter) — x-coordinate of first finger's pixel position")=`'0'`*, *[pos1Y](#ApiClient.TouchInputApi.CreateRotate.pos1Y "ApiClient.TouchInputApi.CreateRotate.pos1Y (Python parameter) — y-coordinate of first finger's pixel position")=`'0'`*, *[pos2X](#ApiClient.TouchInputApi.CreateRotate.pos2X "ApiClient.TouchInputApi.CreateRotate.pos2X (Python parameter) — x-coordinate of second finger's pixel position")=`'0'`*, *[pos2Y](#ApiClient.TouchInputApi.CreateRotate.pos2Y "ApiClient.TouchInputApi.CreateRotate.pos2Y (Python parameter) — y-coordinate of second finger's pixel position")=`'0'`*, *[duration](#ApiClient.TouchInputApi.CreateRotate.duration "ApiClient.TouchInputApi.CreateRotate.duration (Python parameter) — Duration of gesture in seconds")=`'1.0'`*, *[angle](#ApiClient.TouchInputApi.CreateRotate.angle "ApiClient.TouchInputApi.CreateRotate.angle (Python parameter) — Rotation angle in degree")=`'90'`*, *[prompt](#ApiClient.TouchInputApi.CreateRotate.prompt "ApiClient.TouchInputApi.CreateRotate.prompt (Python parameter) — Prompt text to use instead of coordinates")=`None`*)[¶](#ApiClient.TouchInputApi.CreateRotate "Link to this definition")  
Create a new rotate input action object.

Parameters:  pos1X : str[¶](#ApiClient.TouchInputApi.CreateRotate.pos1X "Permalink to this definition")  
x-coordinate of first finger’s pixel position

pos1Y : str[¶](#ApiClient.TouchInputApi.CreateRotate.pos1Y "Permalink to this definition")  
y-coordinate of first finger’s pixel position

pos2X : str[¶](#ApiClient.TouchInputApi.CreateRotate.pos2X "Permalink to this definition")  
x-coordinate of second finger’s pixel position

pos2Y : str[¶](#ApiClient.TouchInputApi.CreateRotate.pos2Y "Permalink to this definition")  
y-coordinate of second finger’s pixel position

duration : str[¶](#ApiClient.TouchInputApi.CreateRotate.duration "Permalink to this definition")  
Duration of gesture in seconds

angle : str[¶](#ApiClient.TouchInputApi.CreateRotate.angle "Permalink to this definition")  
Rotation angle in degree

prompt : str[¶](#ApiClient.TouchInputApi.CreateRotate.prompt "Permalink to this definition")  
Prompt text to use instead of coordinates

Returns:  A new rotate object

Return type:  [`Rotate`](TouchInputApi/Rotate.md#ApiClient.Rotate "ApiClient.Rotate (Python class) — TouchInputApi.CreateRotate")

CreateSwipe(*[startX](#ApiClient.TouchInputApi.CreateSwipe.startX "ApiClient.TouchInputApi.CreateSwipe.startX (Python parameter) — Starting pixel position of first coordinate")=`'0'`*, *[startY](#ApiClient.TouchInputApi.CreateSwipe.startY "ApiClient.TouchInputApi.CreateSwipe.startY (Python parameter) — Starting pixel position of second coordinate")=`'0'`*, *[endX](#ApiClient.TouchInputApi.CreateSwipe.endX "ApiClient.TouchInputApi.CreateSwipe.endX (Python parameter) — Final pixel position of first coordinate")=`'10'`*, *[endY](#ApiClient.TouchInputApi.CreateSwipe.endY "ApiClient.TouchInputApi.CreateSwipe.endY (Python parameter) — Final pixel position of second coordinate")=`'10'`*, *[duration](#ApiClient.TouchInputApi.CreateSwipe.duration "ApiClient.TouchInputApi.CreateSwipe.duration (Python parameter) — Duration of gesture in seconds")=`'1.0'`*, *[prompt](#ApiClient.TouchInputApi.CreateSwipe.prompt "ApiClient.TouchInputApi.CreateSwipe.prompt (Python parameter) — Prompt text to use instead of coordinates")=`None`*)[¶](#ApiClient.TouchInputApi.CreateSwipe "Link to this definition")  
Create a new swipe input action object.

Parameters:  startX : str[¶](#ApiClient.TouchInputApi.CreateSwipe.startX "Permalink to this definition")  
Starting pixel position of first coordinate

startY : str[¶](#ApiClient.TouchInputApi.CreateSwipe.startY "Permalink to this definition")  
Starting pixel position of second coordinate

endX : str[¶](#ApiClient.TouchInputApi.CreateSwipe.endX "Permalink to this definition")  
Final pixel position of first coordinate

endY : str[¶](#ApiClient.TouchInputApi.CreateSwipe.endY "Permalink to this definition")  
Final pixel position of second coordinate

duration : str[¶](#ApiClient.TouchInputApi.CreateSwipe.duration "Permalink to this definition")  
Duration of gesture in seconds

prompt : str[¶](#ApiClient.TouchInputApi.CreateSwipe.prompt "Permalink to this definition")  
Prompt text to use instead of coordinates

Returns:  A new swipe object

Return type:  [`Swipe`](TouchInputApi/Swipe.md#ApiClient.Swipe "ApiClient.Swipe (Python class) — TouchInputApi.CreateSwipe")

CreateTap(*[posX](#ApiClient.TouchInputApi.CreateTap.posX "ApiClient.TouchInputApi.CreateTap.posX (Python parameter) — Pixel position of first coordinate")=`'0'`*, *[posY](#ApiClient.TouchInputApi.CreateTap.posY "ApiClient.TouchInputApi.CreateTap.posY (Python parameter) — Pixel position of second coordinate")=`'0'`*, *[prompt](#ApiClient.TouchInputApi.CreateTap.prompt "ApiClient.TouchInputApi.CreateTap.prompt (Python parameter) — Prompt text to use instead of coordinates")=`None`*)[¶](#ApiClient.TouchInputApi.CreateTap "Link to this definition")  
Create a new tap input action object.

Parameters:  posX : str[¶](#ApiClient.TouchInputApi.CreateTap.posX "Permalink to this definition")  
Pixel position of first coordinate

posY : str[¶](#ApiClient.TouchInputApi.CreateTap.posY "Permalink to this definition")  
Pixel position of second coordinate

prompt : str[¶](#ApiClient.TouchInputApi.CreateTap.prompt "Permalink to this definition")  
Prompt text to use instead of coordinates

Returns:  A new tap object

Return type:  [`Tap`](TouchInputApi/Tap.md#ApiClient.Tap "ApiClient.Tap (Python class) — TouchInputApi.CreateTap")

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
