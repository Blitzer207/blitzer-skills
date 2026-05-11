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

LoopSegment [ LoopSegment ](#)

LoopSegment

- [C LoopSegment ](#ApiClient.LoopSegment)
  - [M AppendSegment ](#ApiClient.LoopSegment.AppendSegment)
  - [M Clone ](#ApiClient.LoopSegment.Clone)
  - [M GetComment ](#ApiClient.LoopSegment.GetComment)
  - [M GetDuration ](#ApiClient.LoopSegment.GetDuration)
  - [M GetDurationExpression ](#ApiClient.LoopSegment.GetDurationExpression)
  - [M GetFinalValue ](#ApiClient.LoopSegment.GetFinalValue)
  - [M GetFirstValue ](#ApiClient.LoopSegment.GetFirstValue)
  - [M GetLoopCount ](#ApiClient.LoopSegment.GetLoopCount)
  - [M GetName ](#ApiClient.LoopSegment.GetName)
  - [M GetSignalSegments ](#ApiClient.LoopSegment.GetSignalSegments)
  - [M GetType ](#ApiClient.LoopSegment.GetType)
  - [M GetValueAt ](#ApiClient.LoopSegment.GetValueAt)
  - [M RemoveSegment ](#ApiClient.LoopSegment.RemoveSegment)
  - [M SetComment ](#ApiClient.LoopSegment.SetComment)
  - [M SetDuration ](#ApiClient.LoopSegment.SetDuration)
  - [M SetDurationExpression ](#ApiClient.LoopSegment.SetDurationExpression)
  - [M SetLoopCount ](#ApiClient.LoopSegment.SetLoopCount)

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

LoopSegment

- [C LoopSegment ](#ApiClient.LoopSegment)
  - [M AppendSegment ](#ApiClient.LoopSegment.AppendSegment)
  - [M Clone ](#ApiClient.LoopSegment.Clone)
  - [M GetComment ](#ApiClient.LoopSegment.GetComment)
  - [M GetDuration ](#ApiClient.LoopSegment.GetDuration)
  - [M GetDurationExpression ](#ApiClient.LoopSegment.GetDurationExpression)
  - [M GetFinalValue ](#ApiClient.LoopSegment.GetFinalValue)
  - [M GetFirstValue ](#ApiClient.LoopSegment.GetFirstValue)
  - [M GetLoopCount ](#ApiClient.LoopSegment.GetLoopCount)
  - [M GetName ](#ApiClient.LoopSegment.GetName)
  - [M GetSignalSegments ](#ApiClient.LoopSegment.GetSignalSegments)
  - [M GetType ](#ApiClient.LoopSegment.GetType)
  - [M GetValueAt ](#ApiClient.LoopSegment.GetValueAt)
  - [M RemoveSegment ](#ApiClient.LoopSegment.RemoveSegment)
  - [M SetComment ](#ApiClient.LoopSegment.SetComment)
  - [M SetDuration ](#ApiClient.LoopSegment.SetDuration)
  - [M SetDurationExpression ](#ApiClient.LoopSegment.SetDurationExpression)
  - [M SetLoopCount ](#ApiClient.LoopSegment.SetLoopCount)

# LoopSegment[¶](#loopsegment "Link to this heading")

*class* LoopSegment[¶](#ApiClient.LoopSegment "Link to this definition")  
Returned by

- [`SignalApi.CreateLoopSegment`](../SignalApi.md#ApiClient.SignalApi.CreateLoopSegment "ApiClient.SignalApi.CreateLoopSegment (Python method) — Creates a loop signal segment")

AppendSegment(*[signalSegment](#ApiClient.LoopSegment.AppendSegment.signalSegment "ApiClient.LoopSegment.AppendSegment.signalSegment (Python parameter) — The signalSegment")*)[¶](#ApiClient.LoopSegment.AppendSegment "Link to this definition")  
Appends a segment to the LoopSegment

Parameters:  signalSegment[¶](#ApiClient.LoopSegment.AppendSegment.signalSegment "Permalink to this definition")  
The signalSegment

Clone()[¶](#ApiClient.LoopSegment.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`LoopSegment`](#ApiClient.LoopSegment "ApiClient.LoopSegment (Python class) — SignalApi.CreateLoopSegment")

GetComment()[¶](#ApiClient.LoopSegment.GetComment "Link to this definition")  
Returns the comment of the signal description

Returns:  Signal description comment

Return type:  str

GetDuration()[¶](#ApiClient.LoopSegment.GetDuration "Link to this definition")  
Returns the current duration of the signal segment.

Returns:  The duration

Return type:  float

GetDurationExpression()[¶](#ApiClient.LoopSegment.GetDurationExpression "Link to this definition")  
Returns the duration expression of the segment that is conform to the ASAM XIL GES syntax for ConstSymbol expressions.

Return type:  str

Returns:  the duration expression

GetFinalValue()[¶](#ApiClient.LoopSegment.GetFinalValue "Link to this definition")  
Returns the final value of the signal segment.

Returns:  the final value

Return type:  float

GetFirstValue()[¶](#ApiClient.LoopSegment.GetFirstValue "Link to this definition")  
Returns the first value of the segment.

Returns:  the first value or NaN

Return type:  float

GetLoopCount()[¶](#ApiClient.LoopSegment.GetLoopCount "Link to this definition")  
Returns the No. of loops for the segment.

Returns:  No. of loops

Return type:  int

GetName()[¶](#ApiClient.LoopSegment.GetName "Link to this definition")  
Returns the name of the signal description.

Returns:  Signal description name

Return type:  str

GetSignalSegments()[¶](#ApiClient.LoopSegment.GetSignalSegments "Link to this definition")  
Returns all segments of the LoopSegment

Returns:  signalSegments

Return type:  list[[`SignalSegment`](SignalSegment.md#ApiClient.SignalSegment "ApiClient.SignalSegment (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")]

GetType()[¶](#ApiClient.LoopSegment.GetType "Link to this definition")  
Returns the type of the segment. (e.g. “Constant”)

Returns:  The type

Return type:  str

GetValueAt(*[timestamp](#ApiClient.LoopSegment.GetValueAt.timestamp "ApiClient.LoopSegment.GetValueAt.timestamp (Python parameter) — The timestamp")*)[¶](#ApiClient.LoopSegment.GetValueAt "Link to this definition")  
Returns the value at the given timestamp.

Parameters:  timestamp : float[¶](#ApiClient.LoopSegment.GetValueAt.timestamp "Permalink to this definition")  
The timestamp

Returns:  the value or NaN

Return type:  float

RemoveSegment(*[signalSegment](#ApiClient.LoopSegment.RemoveSegment.signalSegment "ApiClient.LoopSegment.RemoveSegment.signalSegment (Python parameter) — The signalSegment to be removed")*)[¶](#ApiClient.LoopSegment.RemoveSegment "Link to this definition")  
Removes a segment of the LoopSegment

Parameters:  signalSegment[¶](#ApiClient.LoopSegment.RemoveSegment.signalSegment "Permalink to this definition")  
The signalSegment to be removed

SetComment(*[comment](#ApiClient.LoopSegment.SetComment.comment "ApiClient.LoopSegment.SetComment.comment (Python parameter) — Signal description comment")*)[¶](#ApiClient.LoopSegment.SetComment "Link to this definition")  
Sets the comment of the signal description

Parameters:  comment : str[¶](#ApiClient.LoopSegment.SetComment.comment "Permalink to this definition")  
Signal description comment

SetDuration(*[duration](#ApiClient.LoopSegment.SetDuration.duration "ApiClient.LoopSegment.SetDuration.duration (Python parameter) — the segments duration")*)[¶](#ApiClient.LoopSegment.SetDuration "Link to this definition")  
Sets the duration of the segment in seconds.If you want to set the duration value of the segment to an expression, use SetDurationExpression instead.

Parameters:  duration : float[¶](#ApiClient.LoopSegment.SetDuration.duration "Permalink to this definition")  
the segments duration

SetDurationExpression(*[expression](#ApiClient.LoopSegment.SetDurationExpression.expression "ApiClient.LoopSegment.SetDurationExpression.expression (Python parameter) — the duration expression")*)[¶](#ApiClient.LoopSegment.SetDurationExpression "Link to this definition")  
Sets the duration value as an expression. The expression needs to be conform to the ASAM XIL GES syntax for ConstSymbol expressions.

Parameters:  expression : str[¶](#ApiClient.LoopSegment.SetDurationExpression.expression "Permalink to this definition")  
the duration expression

SetLoopCount(*[loopCount](#ApiClient.LoopSegment.SetLoopCount.loopCount "ApiClient.LoopSegment.SetLoopCount.loopCount (Python parameter) — No.")*)[¶](#ApiClient.LoopSegment.SetLoopCount "Link to this definition")  
Sets the No. of loops for the segment

Parameters:  loopCount : int[¶](#ApiClient.LoopSegment.SetLoopCount.loopCount "Permalink to this definition")  
No. of loops

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
