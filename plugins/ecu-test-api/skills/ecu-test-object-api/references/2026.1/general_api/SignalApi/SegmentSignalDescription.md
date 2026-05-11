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

SegmentSignalDescription [ SegmentSignalDescription ](#)

SegmentSignalDescription

- [C SegmentSignalDescription ](#ApiClient.SegmentSignalDescription)
  - [M AppendSegment ](#ApiClient.SegmentSignalDescription.AppendSegment)
  - [M Clone ](#ApiClient.SegmentSignalDescription.Clone)
  - [M GetComment ](#ApiClient.SegmentSignalDescription.GetComment)
  - [M GetDuration ](#ApiClient.SegmentSignalDescription.GetDuration)
  - [M GetFinalValue ](#ApiClient.SegmentSignalDescription.GetFinalValue)
  - [M GetFirstValue ](#ApiClient.SegmentSignalDescription.GetFirstValue)
  - [M GetName ](#ApiClient.SegmentSignalDescription.GetName)
  - [M GetSegments ](#ApiClient.SegmentSignalDescription.GetSegments)
  - [M GetValueAt ](#ApiClient.SegmentSignalDescription.GetValueAt)
  - [M RemoveSegment ](#ApiClient.SegmentSignalDescription.RemoveSegment)
  - [M SetComment ](#ApiClient.SegmentSignalDescription.SetComment)

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

SegmentSignalDescription

- [C SegmentSignalDescription ](#ApiClient.SegmentSignalDescription)
  - [M AppendSegment ](#ApiClient.SegmentSignalDescription.AppendSegment)
  - [M Clone ](#ApiClient.SegmentSignalDescription.Clone)
  - [M GetComment ](#ApiClient.SegmentSignalDescription.GetComment)
  - [M GetDuration ](#ApiClient.SegmentSignalDescription.GetDuration)
  - [M GetFinalValue ](#ApiClient.SegmentSignalDescription.GetFinalValue)
  - [M GetFirstValue ](#ApiClient.SegmentSignalDescription.GetFirstValue)
  - [M GetName ](#ApiClient.SegmentSignalDescription.GetName)
  - [M GetSegments ](#ApiClient.SegmentSignalDescription.GetSegments)
  - [M GetValueAt ](#ApiClient.SegmentSignalDescription.GetValueAt)
  - [M RemoveSegment ](#ApiClient.SegmentSignalDescription.RemoveSegment)
  - [M SetComment ](#ApiClient.SegmentSignalDescription.SetComment)

# SegmentSignalDescription[¶](#segmentsignaldescription "Link to this heading")

*class* SegmentSignalDescription[¶](#ApiClient.SegmentSignalDescription "Link to this definition")  
Returned by

- [`SignalApi.CreateSignal`](../SignalApi.md#ApiClient.SignalApi.CreateSignal "ApiClient.SignalApi.CreateSignal (Python method) — Creates an empty signal definition")

AppendSegment(*[segment](#ApiClient.SegmentSignalDescription.AppendSegment.segment "ApiClient.SegmentSignalDescription.AppendSegment.segment (Python parameter) — Signal segment")*)[¶](#ApiClient.SegmentSignalDescription.AppendSegment "Link to this definition")  
Appends a signal segment as last element.

Parameters:  segment[¶](#ApiClient.SegmentSignalDescription.AppendSegment.segment "Permalink to this definition")  
Signal segment

Clone()[¶](#ApiClient.SegmentSignalDescription.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`SegmentSignalDescription`](#ApiClient.SegmentSignalDescription "ApiClient.SegmentSignalDescription (Python class) — SignalApi.CreateSignal")

GetComment()[¶](#ApiClient.SegmentSignalDescription.GetComment "Link to this definition")  
Returns the comment of the signal description

Returns:  Signal description comment

Return type:  str

GetDuration()[¶](#ApiClient.SegmentSignalDescription.GetDuration "Link to this definition")  
Returns the duration of the signal description.

Returns:  Duration of signal description

Return type:  float

GetFinalValue()[¶](#ApiClient.SegmentSignalDescription.GetFinalValue "Link to this definition")  
Returns the final value of the signal description.

Returns:  the final value

Return type:  float

GetFirstValue()[¶](#ApiClient.SegmentSignalDescription.GetFirstValue "Link to this definition")  
Returns the first value of the segment.

Returns:  the first value or NaN

Return type:  float

GetName()[¶](#ApiClient.SegmentSignalDescription.GetName "Link to this definition")  
Returns the name of the signal description.

Returns:  Signal description name

Return type:  str

GetSegments()[¶](#ApiClient.SegmentSignalDescription.GetSegments "Link to this definition")  
Returns a list of all segments in the signal description.

Returns:  The segments

Return type:  list[[`SignalSegment`](SignalSegment.md#ApiClient.SignalSegment "ApiClient.SignalSegment (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")]

GetValueAt(*[timestamp](#ApiClient.SegmentSignalDescription.GetValueAt.timestamp "ApiClient.SegmentSignalDescription.GetValueAt.timestamp (Python parameter) — The timestamp")*)[¶](#ApiClient.SegmentSignalDescription.GetValueAt "Link to this definition")  
Returns the value at the given timestamp. If timestamp is bigger than duration, NaN will be returned.

Parameters:  timestamp : float[¶](#ApiClient.SegmentSignalDescription.GetValueAt.timestamp "Permalink to this definition")  
The timestamp

Returns:  the value or NaN

Return type:  float

RemoveSegment(*[segment](#ApiClient.SegmentSignalDescription.RemoveSegment.segment "ApiClient.SegmentSignalDescription.RemoveSegment.segment (Python parameter) — Signal segment")*)[¶](#ApiClient.SegmentSignalDescription.RemoveSegment "Link to this definition")  
Removes a signal segment.

Parameters:  segment[¶](#ApiClient.SegmentSignalDescription.RemoveSegment.segment "Permalink to this definition")  
Signal segment

SetComment(*[comment](#ApiClient.SegmentSignalDescription.SetComment.comment "ApiClient.SegmentSignalDescription.SetComment.comment (Python parameter) — Signal description comment")*)[¶](#ApiClient.SegmentSignalDescription.SetComment "Link to this definition")  
Sets the comment of the signal description

Parameters:  comment : str[¶](#ApiClient.SegmentSignalDescription.SetComment.comment "Permalink to this definition")  
Signal description comment

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
