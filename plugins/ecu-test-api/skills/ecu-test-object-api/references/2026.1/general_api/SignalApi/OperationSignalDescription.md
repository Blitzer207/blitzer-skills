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

OperationSignalDescription [ OperationSignalDescription ](#)

OperationSignalDescription

- [C OperationSignalDescription ](#ApiClient.OperationSignalDescription)
  - [M AppendSignal ](#ApiClient.OperationSignalDescription.AppendSignal)
  - [M Clone ](#ApiClient.OperationSignalDescription.Clone)
  - [M GetComment ](#ApiClient.OperationSignalDescription.GetComment)
  - [M GetDuration ](#ApiClient.OperationSignalDescription.GetDuration)
  - [M GetFinalValue ](#ApiClient.OperationSignalDescription.GetFinalValue)
  - [M GetFirstValue ](#ApiClient.OperationSignalDescription.GetFirstValue)
  - [M GetName ](#ApiClient.OperationSignalDescription.GetName)
  - [M GetOperation ](#ApiClient.OperationSignalDescription.GetOperation)
  - [M GetSignalDescriptions ](#ApiClient.OperationSignalDescription.GetSignalDescriptions)
  - [M GetValueAt ](#ApiClient.OperationSignalDescription.GetValueAt)
  - [M RemoveSignal ](#ApiClient.OperationSignalDescription.RemoveSignal)
  - [M SetComment ](#ApiClient.OperationSignalDescription.SetComment)
  - [M SetOperation ](#ApiClient.OperationSignalDescription.SetOperation)

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

OperationSignalDescription

- [C OperationSignalDescription ](#ApiClient.OperationSignalDescription)
  - [M AppendSignal ](#ApiClient.OperationSignalDescription.AppendSignal)
  - [M Clone ](#ApiClient.OperationSignalDescription.Clone)
  - [M GetComment ](#ApiClient.OperationSignalDescription.GetComment)
  - [M GetDuration ](#ApiClient.OperationSignalDescription.GetDuration)
  - [M GetFinalValue ](#ApiClient.OperationSignalDescription.GetFinalValue)
  - [M GetFirstValue ](#ApiClient.OperationSignalDescription.GetFirstValue)
  - [M GetName ](#ApiClient.OperationSignalDescription.GetName)
  - [M GetOperation ](#ApiClient.OperationSignalDescription.GetOperation)
  - [M GetSignalDescriptions ](#ApiClient.OperationSignalDescription.GetSignalDescriptions)
  - [M GetValueAt ](#ApiClient.OperationSignalDescription.GetValueAt)
  - [M RemoveSignal ](#ApiClient.OperationSignalDescription.RemoveSignal)
  - [M SetComment ](#ApiClient.OperationSignalDescription.SetComment)
  - [M SetOperation ](#ApiClient.OperationSignalDescription.SetOperation)

# OperationSignalDescription[¶](#operationsignaldescription "Link to this heading")

*class* OperationSignalDescription[¶](#ApiClient.OperationSignalDescription "Link to this definition")  
Returned by

- [`SignalApi.CreateOperationSignal`](../SignalApi.md#ApiClient.SignalApi.CreateOperationSignal "ApiClient.SignalApi.CreateOperationSignal (Python method) — Creates an empty operation signal definition")

AppendSignal(*[signal](#ApiClient.OperationSignalDescription.AppendSignal.signal "ApiClient.OperationSignalDescription.AppendSignal.signal (Python parameter) — The signal")*)[¶](#ApiClient.OperationSignalDescription.AppendSignal "Link to this definition")  
Appends a signal to the OperationSignalDescription

Parameters:  signal[¶](#ApiClient.OperationSignalDescription.AppendSignal.signal "Permalink to this definition")  
The signal

Clone()[¶](#ApiClient.OperationSignalDescription.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`OperationSignalDescription`](#ApiClient.OperationSignalDescription "ApiClient.OperationSignalDescription (Python class) — SignalApi.CreateOperationSignal")

GetComment()[¶](#ApiClient.OperationSignalDescription.GetComment "Link to this definition")  
Returns the comment of the signal description

Returns:  Signal description comment

Return type:  str

GetDuration()[¶](#ApiClient.OperationSignalDescription.GetDuration "Link to this definition")  
Returns the duration of the signal description.

Returns:  Duration of signal description

Return type:  float

GetFinalValue()[¶](#ApiClient.OperationSignalDescription.GetFinalValue "Link to this definition")  
Returns the final value of the signal description.

Returns:  the final value

Return type:  float

GetFirstValue()[¶](#ApiClient.OperationSignalDescription.GetFirstValue "Link to this definition")  
Returns the first value of the segment.

Returns:  the first value or NaN

Return type:  float

GetName()[¶](#ApiClient.OperationSignalDescription.GetName "Link to this definition")  
Returns the name of the signal description.

Returns:  Signal description name

Return type:  str

GetOperation()[¶](#ApiClient.OperationSignalDescription.GetOperation "Link to this definition")  
Returns the operation of the operation signal

Returns:  The operation. ‘ADD’ or ‘MULT’

Return type:  str

GetSignalDescriptions()[¶](#ApiClient.OperationSignalDescription.GetSignalDescriptions "Link to this definition")  
Returns all signals of the OperationSignalDescription

Returns:  signals

Return type:  list[[`SignalDescription`](SignalDescription.md#ApiClient.SignalDescription "ApiClient.SignalDescription (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")]

GetValueAt(*[timestamp](#ApiClient.OperationSignalDescription.GetValueAt.timestamp "ApiClient.OperationSignalDescription.GetValueAt.timestamp (Python parameter) — The timestamp")*)[¶](#ApiClient.OperationSignalDescription.GetValueAt "Link to this definition")  
Returns the value at the given timestamp. If timestamp is bigger than duration, NaN will be returned.

Parameters:  timestamp : float[¶](#ApiClient.OperationSignalDescription.GetValueAt.timestamp "Permalink to this definition")  
The timestamp

Returns:  the value or NaN

Return type:  float

RemoveSignal(*[signalDescription](#ApiClient.OperationSignalDescription.RemoveSignal.signalDescription "ApiClient.OperationSignalDescription.RemoveSignal.signalDescription (Python parameter) — The signal to be removed")*)[¶](#ApiClient.OperationSignalDescription.RemoveSignal "Link to this definition")  
Removes a signal of the OperationSignalDescription

Parameters:  signalDescription[¶](#ApiClient.OperationSignalDescription.RemoveSignal.signalDescription "Permalink to this definition")  
The signal to be removed

SetComment(*[comment](#ApiClient.OperationSignalDescription.SetComment.comment "ApiClient.OperationSignalDescription.SetComment.comment (Python parameter) — Signal description comment")*)[¶](#ApiClient.OperationSignalDescription.SetComment "Link to this definition")  
Sets the comment of the signal description

Parameters:  comment : str[¶](#ApiClient.OperationSignalDescription.SetComment.comment "Permalink to this definition")  
Signal description comment

SetOperation(*[operation](#ApiClient.OperationSignalDescription.SetOperation.operation "ApiClient.OperationSignalDescription.SetOperation.operation (Python parameter) — The operation.")*)[¶](#ApiClient.OperationSignalDescription.SetOperation "Link to this definition")  
Sets the operation of the operation signal

Parameters:  operation : str[¶](#ApiClient.OperationSignalDescription.SetOperation.operation "Permalink to this definition")  
The operation. ‘ADD’ or ‘MULT’

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
