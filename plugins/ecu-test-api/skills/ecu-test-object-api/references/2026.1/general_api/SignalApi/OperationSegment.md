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

OperationSegment [ OperationSegment ](#)

OperationSegment

- [C OperationSegment ](#ApiClient.OperationSegment)
  - [M AppendSegment ](#ApiClient.OperationSegment.AppendSegment)
  - [M Clone ](#ApiClient.OperationSegment.Clone)
  - [M GetComment ](#ApiClient.OperationSegment.GetComment)
  - [M GetDuration ](#ApiClient.OperationSegment.GetDuration)
  - [M GetDurationExpression ](#ApiClient.OperationSegment.GetDurationExpression)
  - [M GetFinalValue ](#ApiClient.OperationSegment.GetFinalValue)
  - [M GetFirstValue ](#ApiClient.OperationSegment.GetFirstValue)
  - [M GetName ](#ApiClient.OperationSegment.GetName)
  - [M GetOperation ](#ApiClient.OperationSegment.GetOperation)
  - [M GetSignalSegments ](#ApiClient.OperationSegment.GetSignalSegments)
  - [M GetType ](#ApiClient.OperationSegment.GetType)
  - [M GetValueAt ](#ApiClient.OperationSegment.GetValueAt)
  - [M RemoveSegment ](#ApiClient.OperationSegment.RemoveSegment)
  - [M SetComment ](#ApiClient.OperationSegment.SetComment)
  - [M SetDuration ](#ApiClient.OperationSegment.SetDuration)
  - [M SetDurationExpression ](#ApiClient.OperationSegment.SetDurationExpression)
  - [M SetOperation ](#ApiClient.OperationSegment.SetOperation)

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

OperationSegment

- [C OperationSegment ](#ApiClient.OperationSegment)
  - [M AppendSegment ](#ApiClient.OperationSegment.AppendSegment)
  - [M Clone ](#ApiClient.OperationSegment.Clone)
  - [M GetComment ](#ApiClient.OperationSegment.GetComment)
  - [M GetDuration ](#ApiClient.OperationSegment.GetDuration)
  - [M GetDurationExpression ](#ApiClient.OperationSegment.GetDurationExpression)
  - [M GetFinalValue ](#ApiClient.OperationSegment.GetFinalValue)
  - [M GetFirstValue ](#ApiClient.OperationSegment.GetFirstValue)
  - [M GetName ](#ApiClient.OperationSegment.GetName)
  - [M GetOperation ](#ApiClient.OperationSegment.GetOperation)
  - [M GetSignalSegments ](#ApiClient.OperationSegment.GetSignalSegments)
  - [M GetType ](#ApiClient.OperationSegment.GetType)
  - [M GetValueAt ](#ApiClient.OperationSegment.GetValueAt)
  - [M RemoveSegment ](#ApiClient.OperationSegment.RemoveSegment)
  - [M SetComment ](#ApiClient.OperationSegment.SetComment)
  - [M SetDuration ](#ApiClient.OperationSegment.SetDuration)
  - [M SetDurationExpression ](#ApiClient.OperationSegment.SetDurationExpression)
  - [M SetOperation ](#ApiClient.OperationSegment.SetOperation)

# OperationSegment[¶](#operationsegment "Link to this heading")

*class* OperationSegment[¶](#ApiClient.OperationSegment "Link to this definition")  
Returned by

- [`SignalApi.CreateOperationSegment`](../SignalApi.md#ApiClient.SignalApi.CreateOperationSegment "ApiClient.SignalApi.CreateOperationSegment (Python method) — Creates an operation signal segment")

AppendSegment(*[signalSegment](#ApiClient.OperationSegment.AppendSegment.signalSegment "ApiClient.OperationSegment.AppendSegment.signalSegment (Python parameter) — The signalSegment")*)[¶](#ApiClient.OperationSegment.AppendSegment "Link to this definition")  
Appends a segment to the OperationSegment

Parameters:  signalSegment[¶](#ApiClient.OperationSegment.AppendSegment.signalSegment "Permalink to this definition")  
The signalSegment

Clone()[¶](#ApiClient.OperationSegment.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`OperationSegment`](#ApiClient.OperationSegment "ApiClient.OperationSegment (Python class) — SignalApi.CreateOperationSegment")

GetComment()[¶](#ApiClient.OperationSegment.GetComment "Link to this definition")  
Returns the comment of the signal description

Returns:  Signal description comment

Return type:  str

GetDuration()[¶](#ApiClient.OperationSegment.GetDuration "Link to this definition")  
Returns the current duration of the signal segment.

Returns:  The duration

Return type:  float

GetDurationExpression()[¶](#ApiClient.OperationSegment.GetDurationExpression "Link to this definition")  
Returns the duration expression of the segment that is conform to the ASAM XIL GES syntax for ConstSymbol expressions.

Return type:  str

Returns:  the duration expression

GetFinalValue()[¶](#ApiClient.OperationSegment.GetFinalValue "Link to this definition")  
Returns the final value of the signal segment.

Returns:  the final value

Return type:  float

GetFirstValue()[¶](#ApiClient.OperationSegment.GetFirstValue "Link to this definition")  
Returns the first value of the segment.

Returns:  the first value or NaN

Return type:  float

GetName()[¶](#ApiClient.OperationSegment.GetName "Link to this definition")  
Returns the name of the signal description.

Returns:  Signal description name

Return type:  str

GetOperation()[¶](#ApiClient.OperationSegment.GetOperation "Link to this definition")  
Returns the operation of the segment

Returns:  operation

Return type:  str

GetSignalSegments()[¶](#ApiClient.OperationSegment.GetSignalSegments "Link to this definition")  
Returns all segments of the OperationSegment

Returns:  signalSegments

Return type:  list[[`SignalSegment`](SignalSegment.md#ApiClient.SignalSegment "ApiClient.SignalSegment (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")]

GetType()[¶](#ApiClient.OperationSegment.GetType "Link to this definition")  
Returns the type of the segment. (e.g. “Constant”)

Returns:  The type

Return type:  str

GetValueAt(*[timestamp](#ApiClient.OperationSegment.GetValueAt.timestamp "ApiClient.OperationSegment.GetValueAt.timestamp (Python parameter) — The timestamp")*)[¶](#ApiClient.OperationSegment.GetValueAt "Link to this definition")  
Returns the value at the given timestamp.

Parameters:  timestamp : float[¶](#ApiClient.OperationSegment.GetValueAt.timestamp "Permalink to this definition")  
The timestamp

Returns:  the value or NaN

Return type:  float

RemoveSegment(*[signalSegment](#ApiClient.OperationSegment.RemoveSegment.signalSegment "ApiClient.OperationSegment.RemoveSegment.signalSegment (Python parameter) — The signalSegment to be removed")*)[¶](#ApiClient.OperationSegment.RemoveSegment "Link to this definition")  
Removes a segment of the OperationSegment

Parameters:  signalSegment[¶](#ApiClient.OperationSegment.RemoveSegment.signalSegment "Permalink to this definition")  
The signalSegment to be removed

SetComment(*[comment](#ApiClient.OperationSegment.SetComment.comment "ApiClient.OperationSegment.SetComment.comment (Python parameter) — Signal description comment")*)[¶](#ApiClient.OperationSegment.SetComment "Link to this definition")  
Sets the comment of the signal description

Parameters:  comment : str[¶](#ApiClient.OperationSegment.SetComment.comment "Permalink to this definition")  
Signal description comment

SetDuration(*[duration](#ApiClient.OperationSegment.SetDuration.duration "ApiClient.OperationSegment.SetDuration.duration (Python parameter) — the segments duration")*)[¶](#ApiClient.OperationSegment.SetDuration "Link to this definition")  
Sets the duration of the segment in seconds.If you want to set the duration value of the segment to an expression, use SetDurationExpression instead.

Parameters:  duration : float[¶](#ApiClient.OperationSegment.SetDuration.duration "Permalink to this definition")  
the segments duration

SetDurationExpression(*[expression](#ApiClient.OperationSegment.SetDurationExpression.expression "ApiClient.OperationSegment.SetDurationExpression.expression (Python parameter) — the duration expression")*)[¶](#ApiClient.OperationSegment.SetDurationExpression "Link to this definition")  
Sets the duration value as an expression. The expression needs to be conform to the ASAM XIL GES syntax for ConstSymbol expressions.

Parameters:  expression : str[¶](#ApiClient.OperationSegment.SetDurationExpression.expression "Permalink to this definition")  
the duration expression

SetOperation(*[operation](#ApiClient.OperationSegment.SetOperation.operation "ApiClient.OperationSegment.SetOperation.operation (Python parameter) — The operation.")*)[¶](#ApiClient.OperationSegment.SetOperation "Link to this definition")  
Sets the operation of the segment

Parameters:  operation : str[¶](#ApiClient.OperationSegment.SetOperation.operation "Permalink to this definition")  
The operation. ‘ADD’ or ‘MULT’

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
