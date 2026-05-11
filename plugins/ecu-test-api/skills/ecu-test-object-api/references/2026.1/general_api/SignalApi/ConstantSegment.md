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

ConstantSegment [ ConstantSegment ](#)

ConstantSegment

- [C ConstantSegment ](#ApiClient.ConstantSegment)
  - [M Clone ](#ApiClient.ConstantSegment.Clone)
  - [M GetComment ](#ApiClient.ConstantSegment.GetComment)
  - [M GetDuration ](#ApiClient.ConstantSegment.GetDuration)
  - [M GetDurationExpression ](#ApiClient.ConstantSegment.GetDurationExpression)
  - [M GetFinalValue ](#ApiClient.ConstantSegment.GetFinalValue)
  - [M GetFirstValue ](#ApiClient.ConstantSegment.GetFirstValue)
  - [M GetStopTrigger ](#ApiClient.ConstantSegment.GetStopTrigger)
  - [M GetTimeout ](#ApiClient.ConstantSegment.GetTimeout)
  - [M GetType ](#ApiClient.ConstantSegment.GetType)
  - [M GetValue ](#ApiClient.ConstantSegment.GetValue)
  - [M GetValueAt ](#ApiClient.ConstantSegment.GetValueAt)
  - [M GetValueExpression ](#ApiClient.ConstantSegment.GetValueExpression)
  - [M GetValueSymbol ](#ApiClient.ConstantSegment.GetValueSymbol)
  - [M RemoveStopTrigger ](#ApiClient.ConstantSegment.RemoveStopTrigger)
  - [M RemoveTimeout ](#ApiClient.ConstantSegment.RemoveTimeout)
  - [M SetComment ](#ApiClient.ConstantSegment.SetComment)
  - [M SetDuration ](#ApiClient.ConstantSegment.SetDuration)
  - [M SetDurationExpression ](#ApiClient.ConstantSegment.SetDurationExpression)
  - [M SetStopTrigger ](#ApiClient.ConstantSegment.SetStopTrigger)
  - [M SetTimeout ](#ApiClient.ConstantSegment.SetTimeout)
  - [M SetValue ](#ApiClient.ConstantSegment.SetValue)
  - [M SetValueExpression ](#ApiClient.ConstantSegment.SetValueExpression)
  - [M SetValueSymbol ](#ApiClient.ConstantSegment.SetValueSymbol)

[ DataFileSegment ](DataFileSegment.md)

[ ExponentialSegment ](ExponentialSegment.md)

[ IdleSegment ](IdleSegment.md)

[ LoopSegment ](LoopSegment.md)

[ NoiseSegment ](NoiseSegment.md)

[ OperationSegment ](OperationSegment.md)

[ OperationSignalDescription ](OperationSignalDescription.md)

[ PulseSegment ](PulseSegment.md)

[ RampSegment ](RampSegment.md)

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

ConstantSegment

- [C ConstantSegment ](#ApiClient.ConstantSegment)
  - [M Clone ](#ApiClient.ConstantSegment.Clone)
  - [M GetComment ](#ApiClient.ConstantSegment.GetComment)
  - [M GetDuration ](#ApiClient.ConstantSegment.GetDuration)
  - [M GetDurationExpression ](#ApiClient.ConstantSegment.GetDurationExpression)
  - [M GetFinalValue ](#ApiClient.ConstantSegment.GetFinalValue)
  - [M GetFirstValue ](#ApiClient.ConstantSegment.GetFirstValue)
  - [M GetStopTrigger ](#ApiClient.ConstantSegment.GetStopTrigger)
  - [M GetTimeout ](#ApiClient.ConstantSegment.GetTimeout)
  - [M GetType ](#ApiClient.ConstantSegment.GetType)
  - [M GetValue ](#ApiClient.ConstantSegment.GetValue)
  - [M GetValueAt ](#ApiClient.ConstantSegment.GetValueAt)
  - [M GetValueExpression ](#ApiClient.ConstantSegment.GetValueExpression)
  - [M GetValueSymbol ](#ApiClient.ConstantSegment.GetValueSymbol)
  - [M RemoveStopTrigger ](#ApiClient.ConstantSegment.RemoveStopTrigger)
  - [M RemoveTimeout ](#ApiClient.ConstantSegment.RemoveTimeout)
  - [M SetComment ](#ApiClient.ConstantSegment.SetComment)
  - [M SetDuration ](#ApiClient.ConstantSegment.SetDuration)
  - [M SetDurationExpression ](#ApiClient.ConstantSegment.SetDurationExpression)
  - [M SetStopTrigger ](#ApiClient.ConstantSegment.SetStopTrigger)
  - [M SetTimeout ](#ApiClient.ConstantSegment.SetTimeout)
  - [M SetValue ](#ApiClient.ConstantSegment.SetValue)
  - [M SetValueExpression ](#ApiClient.ConstantSegment.SetValueExpression)
  - [M SetValueSymbol ](#ApiClient.ConstantSegment.SetValueSymbol)

# ConstantSegment[¶](#constantsegment "Link to this heading")

*class* ConstantSegment[¶](#ApiClient.ConstantSegment "Link to this definition")  
Returned by

- [`SignalApi.CreateConstantSegment`](../SignalApi.md#ApiClient.SignalApi.CreateConstantSegment "ApiClient.SignalApi.CreateConstantSegment (Python method) — Creates a constant signal segment")

Clone()[¶](#ApiClient.ConstantSegment.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`ConstantSegment`](#ApiClient.ConstantSegment "ApiClient.ConstantSegment (Python class) — SignalApi.CreateConstantSegment")

GetComment()[¶](#ApiClient.ConstantSegment.GetComment "Link to this definition")  
Returns the comment of the segment.

Returns:  The comment

Return type:  str

GetDuration()[¶](#ApiClient.ConstantSegment.GetDuration "Link to this definition")  
Returns the current duration of the signal segment.

Returns:  The duration

Return type:  float

GetDurationExpression()[¶](#ApiClient.ConstantSegment.GetDurationExpression "Link to this definition")  
Returns the duration expression of the segment that is conform to the ASAM XIL GES syntax for ConstSymbol expressions.

Return type:  str

Returns:  the duration expression

GetFinalValue()[¶](#ApiClient.ConstantSegment.GetFinalValue "Link to this definition")  
Returns the final value of the signal segment.

Returns:  the final value

Return type:  float

GetFirstValue()[¶](#ApiClient.ConstantSegment.GetFirstValue "Link to this definition")  
Returns the first value of the segment.

Returns:  the first value or NaN

Return type:  float

GetStopTrigger()[¶](#ApiClient.ConstantSegment.GetStopTrigger "Link to this definition")  
Returns the stop trigger of the segment

Returns:  stop trigger

Return type:  str

GetTimeout()[¶](#ApiClient.ConstantSegment.GetTimeout "Link to this definition")  
Returns the timeout of the segment

Returns:  timeout

Return type:  float

GetType()[¶](#ApiClient.ConstantSegment.GetType "Link to this definition")  
Returns the type of the segment. (e.g. “Constant”)

Returns:  The type

Return type:  str

GetValue()[¶](#ApiClient.ConstantSegment.GetValue "Link to this definition")  
Returns the value of the segment. If the value is set to an expression, the expression gets calculated. Returns nan if the value expression contains unknown parameter.

Return type:  float

Returns:  the value

GetValueAt(*[timestamp](#ApiClient.ConstantSegment.GetValueAt.timestamp "ApiClient.ConstantSegment.GetValueAt.timestamp (Python parameter) — The timestamp")*)[¶](#ApiClient.ConstantSegment.GetValueAt "Link to this definition")  
Returns the value at the given timestamp.

Parameters:  timestamp : float[¶](#ApiClient.ConstantSegment.GetValueAt.timestamp "Permalink to this definition")  
The timestamp

Returns:  the value or NaN

Return type:  float

GetValueExpression()[¶](#ApiClient.ConstantSegment.GetValueExpression "Link to this definition")  
Returns the expression of the value of the segment. The expression is conform to the ASAM XIL GES syntax for ConstSymbol expressions.

Return type:  str

Returns:  the value expression.

GetValueSymbol()[¶](#ApiClient.ConstantSegment.GetValueSymbol "Link to this definition")  
Returns the SymbolType object of the segment value.

Return type:  [`SymbolType`](SymbolType.md#ApiClient.SymbolType "ApiClient.SymbolType (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")

Returns:  the value symbol

RemoveStopTrigger()[¶](#ApiClient.ConstantSegment.RemoveStopTrigger "Link to this definition")  
Removes the stop trigger of the segment

RemoveTimeout()[¶](#ApiClient.ConstantSegment.RemoveTimeout "Link to this definition")  
Removes the timeout of the segment

SetComment(*[comment](#ApiClient.ConstantSegment.SetComment.comment "ApiClient.ConstantSegment.SetComment.comment (Python parameter) — The comment")*)[¶](#ApiClient.ConstantSegment.SetComment "Link to this definition")  
Sets the comment of the segment.

Parameters:  comment : str[¶](#ApiClient.ConstantSegment.SetComment.comment "Permalink to this definition")  
The comment

SetDuration(*[duration](#ApiClient.ConstantSegment.SetDuration.duration "ApiClient.ConstantSegment.SetDuration.duration (Python parameter) — the segments duration")*)[¶](#ApiClient.ConstantSegment.SetDuration "Link to this definition")  
Sets the duration of the segment in seconds.If you want to set the duration value of the segment to an expression, use SetDurationExpression instead.

Parameters:  duration : float[¶](#ApiClient.ConstantSegment.SetDuration.duration "Permalink to this definition")  
the segments duration

SetDurationExpression(*[expression](#ApiClient.ConstantSegment.SetDurationExpression.expression "ApiClient.ConstantSegment.SetDurationExpression.expression (Python parameter) — the duration expression")*)[¶](#ApiClient.ConstantSegment.SetDurationExpression "Link to this definition")  
Sets the duration value as an expression. The expression needs to be conform to the ASAM XIL GES syntax for ConstSymbol expressions.

Parameters:  expression : str[¶](#ApiClient.ConstantSegment.SetDurationExpression.expression "Permalink to this definition")  
the duration expression

SetStopTrigger(*[stopTrigger](#ApiClient.ConstantSegment.SetStopTrigger.stopTrigger "ApiClient.ConstantSegment.SetStopTrigger.stopTrigger (Python parameter) — The stop trigger")*)[¶](#ApiClient.ConstantSegment.SetStopTrigger "Link to this definition")  
Sets the stop trigger of the segment

Parameters:  stopTrigger : str[¶](#ApiClient.ConstantSegment.SetStopTrigger.stopTrigger "Permalink to this definition")  
The stop trigger

SetTimeout(*[timeout](#ApiClient.ConstantSegment.SetTimeout.timeout "ApiClient.ConstantSegment.SetTimeout.timeout (Python parameter) — The timeout")*)[¶](#ApiClient.ConstantSegment.SetTimeout "Link to this definition")  
Sets the timeout of the segment

Parameters:  timeout : float[¶](#ApiClient.ConstantSegment.SetTimeout.timeout "Permalink to this definition")  
The timeout

SetValue(*[value](#ApiClient.ConstantSegment.SetValue.value "ApiClient.ConstantSegment.SetValue.value (Python parameter) — the value")*)[¶](#ApiClient.ConstantSegment.SetValue "Link to this definition")  
Sets the value of the segment. If you want to set the value of the segment to an expression, use SetValueExpression instead.

Parameters:  value : float[¶](#ApiClient.ConstantSegment.SetValue.value "Permalink to this definition")  
the value

SetValueExpression(*[expression](#ApiClient.ConstantSegment.SetValueExpression.expression "ApiClient.ConstantSegment.SetValueExpression.expression (Python parameter) — the expression")*)[¶](#ApiClient.ConstantSegment.SetValueExpression "Link to this definition")  
Sets the value expression of the segment. The expression has to be conform to the ASAM XIL GES syntax for ConstSymbol expressions.

Parameters:  expression : str[¶](#ApiClient.ConstantSegment.SetValueExpression.expression "Permalink to this definition")  
the expression

SetValueSymbol(*[value](#ApiClient.ConstantSegment.SetValueSymbol.value "ApiClient.ConstantSegment.SetValueSymbol.value (Python parameter) — the value symbol")*)[¶](#ApiClient.ConstantSegment.SetValueSymbol "Link to this definition")  
Sets a SymbolType object as value of the segment. If you want to set the value of the segment to an expression, use SetValueExpression instead.

Parameters:  value[¶](#ApiClient.ConstantSegment.SetValueSymbol.value "Permalink to this definition")  
the value symbol

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
