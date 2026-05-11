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

[ RampSegment ](RampSegment.md)

[ RampSlopeSegment ](RampSlopeSegment.md)

[ SawSegment ](SawSegment.md)

[ SegmentSignalDescription ](SegmentSignalDescription.md)

[ SignalDescription ](SignalDescription.md)

SignalSegment [ SignalSegment ](#)

SignalSegment

- [C SignalSegment ](#ApiClient.SignalSegment)
  - [M Clone ](#ApiClient.SignalSegment.Clone)
  - [M GetComment ](#ApiClient.SignalSegment.GetComment)
  - [M GetDuration ](#ApiClient.SignalSegment.GetDuration)
  - [M GetDurationExpression ](#ApiClient.SignalSegment.GetDurationExpression)
  - [M GetFinalValue ](#ApiClient.SignalSegment.GetFinalValue)
  - [M GetFirstValue ](#ApiClient.SignalSegment.GetFirstValue)
  - [M GetType ](#ApiClient.SignalSegment.GetType)
  - [M GetValueAt ](#ApiClient.SignalSegment.GetValueAt)
  - [M SetComment ](#ApiClient.SignalSegment.SetComment)
  - [M SetDuration ](#ApiClient.SignalSegment.SetDuration)
  - [M SetDurationExpression ](#ApiClient.SignalSegment.SetDurationExpression)

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

SignalSegment

- [C SignalSegment ](#ApiClient.SignalSegment)
  - [M Clone ](#ApiClient.SignalSegment.Clone)
  - [M GetComment ](#ApiClient.SignalSegment.GetComment)
  - [M GetDuration ](#ApiClient.SignalSegment.GetDuration)
  - [M GetDurationExpression ](#ApiClient.SignalSegment.GetDurationExpression)
  - [M GetFinalValue ](#ApiClient.SignalSegment.GetFinalValue)
  - [M GetFirstValue ](#ApiClient.SignalSegment.GetFirstValue)
  - [M GetType ](#ApiClient.SignalSegment.GetType)
  - [M GetValueAt ](#ApiClient.SignalSegment.GetValueAt)
  - [M SetComment ](#ApiClient.SignalSegment.SetComment)
  - [M SetDuration ](#ApiClient.SignalSegment.SetDuration)
  - [M SetDurationExpression ](#ApiClient.SignalSegment.SetDurationExpression)

# SignalSegment[¶](#signalsegment "Link to this heading")

*class* SignalSegment[¶](#ApiClient.SignalSegment "Link to this definition")  
Clone()[¶](#ApiClient.SignalSegment.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`SignalSegment`](#ApiClient.SignalSegment "ApiClient.SignalSegment (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")

GetComment()[¶](#ApiClient.SignalSegment.GetComment "Link to this definition")  
Returns the comment of the segment.

Returns:  The comment

Return type:  str

GetDuration()[¶](#ApiClient.SignalSegment.GetDuration "Link to this definition")  
Returns the current duration of the signal segment.

Returns:  The duration

Return type:  float

GetDurationExpression()[¶](#ApiClient.SignalSegment.GetDurationExpression "Link to this definition")  
Returns the duration expression of the segment that is conform to the ASAM XIL GES syntax for ConstSymbol expressions.

Return type:  str

Returns:  the duration expression

GetFinalValue()[¶](#ApiClient.SignalSegment.GetFinalValue "Link to this definition")  
Returns the final value of the signal segment.

Returns:  the final value

Return type:  float

GetFirstValue()[¶](#ApiClient.SignalSegment.GetFirstValue "Link to this definition")  
Returns the first value of the segment.

Returns:  the first value or NaN

Return type:  float

GetType()[¶](#ApiClient.SignalSegment.GetType "Link to this definition")  
Returns the type of the segment. (e.g. “Constant”)

Returns:  The type

Return type:  str

GetValueAt(*[timestamp](#ApiClient.SignalSegment.GetValueAt.timestamp "ApiClient.SignalSegment.GetValueAt.timestamp (Python parameter) — The timestamp")*)[¶](#ApiClient.SignalSegment.GetValueAt "Link to this definition")  
Returns the value at the given timestamp.

Parameters:  timestamp : float[¶](#ApiClient.SignalSegment.GetValueAt.timestamp "Permalink to this definition")  
The timestamp

Returns:  the value or NaN

Return type:  float

SetComment(*[comment](#ApiClient.SignalSegment.SetComment.comment "ApiClient.SignalSegment.SetComment.comment (Python parameter) — The comment")*)[¶](#ApiClient.SignalSegment.SetComment "Link to this definition")  
Sets the comment of the segment.

Parameters:  comment : str[¶](#ApiClient.SignalSegment.SetComment.comment "Permalink to this definition")  
The comment

SetDuration(*[duration](#ApiClient.SignalSegment.SetDuration.duration "ApiClient.SignalSegment.SetDuration.duration (Python parameter) — the segments duration")*)[¶](#ApiClient.SignalSegment.SetDuration "Link to this definition")  
Sets the duration of the segment in seconds.If you want to set the duration value of the segment to an expression, use SetDurationExpression instead.

Parameters:  duration : float[¶](#ApiClient.SignalSegment.SetDuration.duration "Permalink to this definition")  
the segments duration

SetDurationExpression(*[expression](#ApiClient.SignalSegment.SetDurationExpression.expression "ApiClient.SignalSegment.SetDurationExpression.expression (Python parameter) — the duration expression")*)[¶](#ApiClient.SignalSegment.SetDurationExpression "Link to this definition")  
Sets the duration value as an expression. The expression needs to be conform to the ASAM XIL GES syntax for ConstSymbol expressions.

Parameters:  expression : str[¶](#ApiClient.SignalSegment.SetDurationExpression.expression "Permalink to this definition")  
the duration expression

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
