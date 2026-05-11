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

API for Signals

[ ConstantSegment ](ConstantSegment.md)

[ DataFileSegment ](DataFileSegment.md)

[ ExponentialSegment ](ExponentialSegment.md)

[ IdleSegment ](IdleSegment.md)

[ LoopSegment ](LoopSegment.md)

[ NoiseSegment ](NoiseSegment.md)

[ OperationSegment ](OperationSegment.md)

[ OperationSignalDescription ](OperationSignalDescription.md)

[ PulseSegment ](PulseSegment.md)

RampSegment [ RampSegment ](#)

RampSegment

- [C RampSegment ](#ApiClient.RampSegment)
  - [M Clone ](#ApiClient.RampSegment.Clone)
  - [M GetComment ](#ApiClient.RampSegment.GetComment)
  - [M GetDuration ](#ApiClient.RampSegment.GetDuration)
  - [M GetDurationExpression ](#ApiClient.RampSegment.GetDurationExpression)
  - [M GetFinalValue ](#ApiClient.RampSegment.GetFinalValue)
  - [M GetFirstValue ](#ApiClient.RampSegment.GetFirstValue)
  - [M GetStart ](#ApiClient.RampSegment.GetStart)
  - [M GetStartExpression ](#ApiClient.RampSegment.GetStartExpression)
  - [M GetStartSymbol ](#ApiClient.RampSegment.GetStartSymbol)
  - [M GetStop ](#ApiClient.RampSegment.GetStop)
  - [M GetStopExpression ](#ApiClient.RampSegment.GetStopExpression)
  - [M GetStopSymbol ](#ApiClient.RampSegment.GetStopSymbol)
  - [M GetType ](#ApiClient.RampSegment.GetType)
  - [M GetValueAt ](#ApiClient.RampSegment.GetValueAt)
  - [M SetComment ](#ApiClient.RampSegment.SetComment)
  - [M SetDuration ](#ApiClient.RampSegment.SetDuration)
  - [M SetDurationExpression ](#ApiClient.RampSegment.SetDurationExpression)
  - [M SetStart ](#ApiClient.RampSegment.SetStart)
  - [M SetStartExpression ](#ApiClient.RampSegment.SetStartExpression)
  - [M SetStartSymbol ](#ApiClient.RampSegment.SetStartSymbol)
  - [M SetStop ](#ApiClient.RampSegment.SetStop)
  - [M SetStopExpression ](#ApiClient.RampSegment.SetStopExpression)
  - [M SetStopSymbol ](#ApiClient.RampSegment.SetStopSymbol)

[ RampSlopeSegment ](RampSlopeSegment.md)

[ SawSegment ](SawSegment.md)

[ SegmentSignalDescription ](SegmentSignalDescription.md)

[ SignalDescription ](SignalDescription.md)

[ SignalSegment ](SignalSegment.md)

[ SignalValueSegment ](SignalValueSegment.md)

[ SineSegment ](SineSegment.md)

[ SymbolType ](SymbolType.md)

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

RampSegment

- [C RampSegment ](#ApiClient.RampSegment)
  - [M Clone ](#ApiClient.RampSegment.Clone)
  - [M GetComment ](#ApiClient.RampSegment.GetComment)
  - [M GetDuration ](#ApiClient.RampSegment.GetDuration)
  - [M GetDurationExpression ](#ApiClient.RampSegment.GetDurationExpression)
  - [M GetFinalValue ](#ApiClient.RampSegment.GetFinalValue)
  - [M GetFirstValue ](#ApiClient.RampSegment.GetFirstValue)
  - [M GetStart ](#ApiClient.RampSegment.GetStart)
  - [M GetStartExpression ](#ApiClient.RampSegment.GetStartExpression)
  - [M GetStartSymbol ](#ApiClient.RampSegment.GetStartSymbol)
  - [M GetStop ](#ApiClient.RampSegment.GetStop)
  - [M GetStopExpression ](#ApiClient.RampSegment.GetStopExpression)
  - [M GetStopSymbol ](#ApiClient.RampSegment.GetStopSymbol)
  - [M GetType ](#ApiClient.RampSegment.GetType)
  - [M GetValueAt ](#ApiClient.RampSegment.GetValueAt)
  - [M SetComment ](#ApiClient.RampSegment.SetComment)
  - [M SetDuration ](#ApiClient.RampSegment.SetDuration)
  - [M SetDurationExpression ](#ApiClient.RampSegment.SetDurationExpression)
  - [M SetStart ](#ApiClient.RampSegment.SetStart)
  - [M SetStartExpression ](#ApiClient.RampSegment.SetStartExpression)
  - [M SetStartSymbol ](#ApiClient.RampSegment.SetStartSymbol)
  - [M SetStop ](#ApiClient.RampSegment.SetStop)
  - [M SetStopExpression ](#ApiClient.RampSegment.SetStopExpression)
  - [M SetStopSymbol ](#ApiClient.RampSegment.SetStopSymbol)

# RampSegment[¶](#rampsegment "Link to this heading")

*class* RampSegment[¶](#ApiClient.RampSegment "Link to this definition")  
Returned by

- [`SignalApi.CreateRampSegment`](../SignalApi.md#ApiClient.SignalApi.CreateRampSegment "ApiClient.SignalApi.CreateRampSegment (Python method) — Creates a ramp signal segment")

Clone()[¶](#ApiClient.RampSegment.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`RampSegment`](#ApiClient.RampSegment "ApiClient.RampSegment (Python class) — SignalApi.CreateRampSegment")

GetComment()[¶](#ApiClient.RampSegment.GetComment "Link to this definition")  
Returns the comment of the segment.

Returns:  The comment

Return type:  str

GetDuration()[¶](#ApiClient.RampSegment.GetDuration "Link to this definition")  
Returns the current duration of the signal segment.

Returns:  The duration

Return type:  float

GetDurationExpression()[¶](#ApiClient.RampSegment.GetDurationExpression "Link to this definition")  
Returns the duration expression of the segment that is conform to the ASAM XIL GES syntax for ConstSymbol expressions.

Return type:  str

Returns:  the duration expression

GetFinalValue()[¶](#ApiClient.RampSegment.GetFinalValue "Link to this definition")  
Returns the final value of the signal segment.

Returns:  the final value

Return type:  float

GetFirstValue()[¶](#ApiClient.RampSegment.GetFirstValue "Link to this definition")  
Returns the first value of the segment.

Returns:  the first value or NaN

Return type:  float

GetStart()[¶](#ApiClient.RampSegment.GetStart "Link to this definition")  
Returns the start value of the segment. If the start value is set to an expression. the expression gets evaluated. Returns nan if the expression contains unknown parameter.

Return type:  float

Returns:  the start value

GetStartExpression()[¶](#ApiClient.RampSegment.GetStartExpression "Link to this definition")  
Returns the start value expression.

Return type:  str

Returns:  the start value expression

GetStartSymbol()[¶](#ApiClient.RampSegment.GetStartSymbol "Link to this definition")  
Returns the SymbolType object of the segment start value.

Return type:  [`SymbolType`](SymbolType.md#ApiClient.SymbolType "ApiClient.SymbolType (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")

Returns:  the start value symbol

GetStop()[¶](#ApiClient.RampSegment.GetStop "Link to this definition")  
Returns the stop value of the segment.

Return type:  float

Returns:  the stop value

GetStopExpression()[¶](#ApiClient.RampSegment.GetStopExpression "Link to this definition")  
Returns the stop expression of the segment. The expression is conform to the ASAM XIL GES syntax for ConstSymbol expressions.

Return type:  str

Returns:  the stop expression

GetStopSymbol()[¶](#ApiClient.RampSegment.GetStopSymbol "Link to this definition")  
Returns the SymbolType object of the segment stop value.

Return type:  [`SymbolType`](SymbolType.md#ApiClient.SymbolType "ApiClient.SymbolType (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")

Returns:  the stop value symbol

GetType()[¶](#ApiClient.RampSegment.GetType "Link to this definition")  
Returns the type of the segment. (e.g. “Constant”)

Returns:  The type

Return type:  str

GetValueAt(*[timestamp](#ApiClient.RampSegment.GetValueAt.timestamp "ApiClient.RampSegment.GetValueAt.timestamp (Python parameter) — The timestamp")*)[¶](#ApiClient.RampSegment.GetValueAt "Link to this definition")  
Returns the value at the given timestamp.

Parameters:  timestamp : float[¶](#ApiClient.RampSegment.GetValueAt.timestamp "Permalink to this definition")  
The timestamp

Returns:  the value or NaN

Return type:  float

SetComment(*[comment](#ApiClient.RampSegment.SetComment.comment "ApiClient.RampSegment.SetComment.comment (Python parameter) — The comment")*)[¶](#ApiClient.RampSegment.SetComment "Link to this definition")  
Sets the comment of the segment.

Parameters:  comment : str[¶](#ApiClient.RampSegment.SetComment.comment "Permalink to this definition")  
The comment

SetDuration(*[duration](#ApiClient.RampSegment.SetDuration.duration "ApiClient.RampSegment.SetDuration.duration (Python parameter) — the segments duration")*)[¶](#ApiClient.RampSegment.SetDuration "Link to this definition")  
Sets the duration of the segment in seconds.If you want to set the duration value of the segment to an expression, use SetDurationExpression instead.

Parameters:  duration : float[¶](#ApiClient.RampSegment.SetDuration.duration "Permalink to this definition")  
the segments duration

SetDurationExpression(*[expression](#ApiClient.RampSegment.SetDurationExpression.expression "ApiClient.RampSegment.SetDurationExpression.expression (Python parameter) — the duration expression")*)[¶](#ApiClient.RampSegment.SetDurationExpression "Link to this definition")  
Sets the duration value as an expression. The expression needs to be conform to the ASAM XIL GES syntax for ConstSymbol expressions.

Parameters:  expression : str[¶](#ApiClient.RampSegment.SetDurationExpression.expression "Permalink to this definition")  
the duration expression

SetStart(*[start](#ApiClient.RampSegment.SetStart.start "ApiClient.RampSegment.SetStart.start (Python parameter) — the start value")*)[¶](#ApiClient.RampSegment.SetStart "Link to this definition")  
Sets the start value of the segment.

Parameters:  start : float[¶](#ApiClient.RampSegment.SetStart.start "Permalink to this definition")  
the start value

SetStartExpression(*[expression](#ApiClient.RampSegment.SetStartExpression.expression "ApiClient.RampSegment.SetStartExpression.expression (Python parameter) — the expression")*)[¶](#ApiClient.RampSegment.SetStartExpression "Link to this definition")  
Sets the start value of the segment to the given expression. The expression needs to conform to the ASAM XIL GES syntax for ConstSymbol expressions.

Parameters:  expression : str[¶](#ApiClient.RampSegment.SetStartExpression.expression "Permalink to this definition")  
the expression

SetStartSymbol(*[value](#ApiClient.RampSegment.SetStartSymbol.value "ApiClient.RampSegment.SetStartSymbol.value (Python parameter) — the start value symbol")*)[¶](#ApiClient.RampSegment.SetStartSymbol "Link to this definition")  
Sets a SymbolType object as start value of the segment. If you want to set the start value of the segment to an expression, use SetStartExpression instead.

Parameters:  value[¶](#ApiClient.RampSegment.SetStartSymbol.value "Permalink to this definition")  
the start value symbol

SetStop(*[stop](#ApiClient.RampSegment.SetStop.stop "ApiClient.RampSegment.SetStop.stop (Python parameter) — the stop value")*)[¶](#ApiClient.RampSegment.SetStop "Link to this definition")  
Set the stop value of the segment.

Parameters:  stop : float[¶](#ApiClient.RampSegment.SetStop.stop "Permalink to this definition")  
the stop value

SetStopExpression(*[expression](#ApiClient.RampSegment.SetStopExpression.expression "ApiClient.RampSegment.SetStopExpression.expression (Python parameter) — the expression")*)[¶](#ApiClient.RampSegment.SetStopExpression "Link to this definition")  
Sets the stop value to the given expression. The expression has to be conform to the ASAM XIL GES syntax for ConstSymbol expressions.

Parameters:  expression : str[¶](#ApiClient.RampSegment.SetStopExpression.expression "Permalink to this definition")  
the expression

SetStopSymbol(*[value](#ApiClient.RampSegment.SetStopSymbol.value "ApiClient.RampSegment.SetStopSymbol.value (Python parameter) — the stop value symbol")*)[¶](#ApiClient.RampSegment.SetStopSymbol "Link to this definition")  
Sets a SymbolType object as stop value of the segment. If you want to set the stop value of the segment to an expression, use SetStopExpression instead.

Parameters:  value[¶](#ApiClient.RampSegment.SetStopSymbol.value "Permalink to this definition")  
the stop value symbol

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
