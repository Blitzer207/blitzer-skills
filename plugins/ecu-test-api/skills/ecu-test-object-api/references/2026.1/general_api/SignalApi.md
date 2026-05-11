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

[ API for Signals ](#)

API for Signals

- [ ConstantSegment ](SignalApi/ConstantSegment.md)
- [ DataFileSegment ](SignalApi/DataFileSegment.md)
- [ ExponentialSegment ](SignalApi/ExponentialSegment.md)
- [ IdleSegment ](SignalApi/IdleSegment.md)
- [ LoopSegment ](SignalApi/LoopSegment.md)
- [ NoiseSegment ](SignalApi/NoiseSegment.md)
- [ OperationSegment ](SignalApi/OperationSegment.md)
- [ OperationSignalDescription ](SignalApi/OperationSignalDescription.md)
- [ PulseSegment ](SignalApi/PulseSegment.md)
- [ RampSegment ](SignalApi/RampSegment.md)
- [ RampSlopeSegment ](SignalApi/RampSlopeSegment.md)
- [ SawSegment ](SignalApi/SawSegment.md)
- [ SegmentSignalDescription ](SignalApi/SegmentSignalDescription.md)
- [ SignalDescription ](SignalApi/SignalDescription.md)
- [ SignalSegment ](SignalApi/SignalSegment.md)
- [ SignalValueSegment ](SignalApi/SignalValueSegment.md)
- [ SineSegment ](SignalApi/SineSegment.md)
- [ SymbolType ](SignalApi/SymbolType.md)

API for Signals [ API for Signals ](#)

API for Signals

- [C SignalApi ](#ApiClient.SignalApi)
  - [A SymbolApi ](#ApiClient.SignalApi.SymbolApi)
  - [M CreateConstantSegment ](#ApiClient.SignalApi.CreateConstantSegment)
  - [M CreateDataFileSegment ](#ApiClient.SignalApi.CreateDataFileSegment)
  - [M CreateExponentialSegment ](#ApiClient.SignalApi.CreateExponentialSegment)
  - [M CreateIdleSegment ](#ApiClient.SignalApi.CreateIdleSegment)
  - [M CreateLoopSegment ](#ApiClient.SignalApi.CreateLoopSegment)
  - [M CreateNoiseSegment ](#ApiClient.SignalApi.CreateNoiseSegment)
  - [M CreateOperationSegment ](#ApiClient.SignalApi.CreateOperationSegment)
  - [M CreateOperationSignal ](#ApiClient.SignalApi.CreateOperationSignal)
  - [M CreatePulseSegment ](#ApiClient.SignalApi.CreatePulseSegment)
  - [M CreateRampSegment ](#ApiClient.SignalApi.CreateRampSegment)
  - [M CreateRampSlopeSegment ](#ApiClient.SignalApi.CreateRampSlopeSegment)
  - [M CreateSawSegment ](#ApiClient.SignalApi.CreateSawSegment)
  - [M CreateSignal ](#ApiClient.SignalApi.CreateSignal)
  - [M CreateSignalValueSegment ](#ApiClient.SignalApi.CreateSignalValueSegment)
  - [M CreateSineSegment ](#ApiClient.SignalApi.CreateSineSegment)
  - [M GetSignalNames ](#ApiClient.SignalApi.GetSignalNames)
- [ ConstantSegment ](SignalApi/ConstantSegment.md)
- [ DataFileSegment ](SignalApi/DataFileSegment.md)
- [ ExponentialSegment ](SignalApi/ExponentialSegment.md)
- [ IdleSegment ](SignalApi/IdleSegment.md)
- [ LoopSegment ](SignalApi/LoopSegment.md)
- [ NoiseSegment ](SignalApi/NoiseSegment.md)
- [ OperationSegment ](SignalApi/OperationSegment.md)
- [ OperationSignalDescription ](SignalApi/OperationSignalDescription.md)
- [ PulseSegment ](SignalApi/PulseSegment.md)
- [ RampSegment ](SignalApi/RampSegment.md)
- [ RampSlopeSegment ](SignalApi/RampSlopeSegment.md)
- [ SawSegment ](SignalApi/SawSegment.md)
- [ SegmentSignalDescription ](SignalApi/SegmentSignalDescription.md)
- [ SignalDescription ](SignalApi/SignalDescription.md)
- [ SignalSegment ](SignalApi/SignalSegment.md)
- [ SignalValueSegment ](SignalApi/SignalValueSegment.md)
- [ SineSegment ](SignalApi/SineSegment.md)
- [ SymbolType ](SignalApi/SymbolType.md)

[ API for Signal Descriptions ](SignalDescriptionApi.md)

[ API for Signal Recordings ](SignalRecordingApi.md)

[ API for Symbols ](SymbolApi.md)

[ API for Test Steps ](TestStepApi.md)

[ API for Touch Inputs ](TouchInputApi.md)

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

API for Signals

- [C SignalApi ](#ApiClient.SignalApi)
  - [A SymbolApi ](#ApiClient.SignalApi.SymbolApi)
  - [M CreateConstantSegment ](#ApiClient.SignalApi.CreateConstantSegment)
  - [M CreateDataFileSegment ](#ApiClient.SignalApi.CreateDataFileSegment)
  - [M CreateExponentialSegment ](#ApiClient.SignalApi.CreateExponentialSegment)
  - [M CreateIdleSegment ](#ApiClient.SignalApi.CreateIdleSegment)
  - [M CreateLoopSegment ](#ApiClient.SignalApi.CreateLoopSegment)
  - [M CreateNoiseSegment ](#ApiClient.SignalApi.CreateNoiseSegment)
  - [M CreateOperationSegment ](#ApiClient.SignalApi.CreateOperationSegment)
  - [M CreateOperationSignal ](#ApiClient.SignalApi.CreateOperationSignal)
  - [M CreatePulseSegment ](#ApiClient.SignalApi.CreatePulseSegment)
  - [M CreateRampSegment ](#ApiClient.SignalApi.CreateRampSegment)
  - [M CreateRampSlopeSegment ](#ApiClient.SignalApi.CreateRampSlopeSegment)
  - [M CreateSawSegment ](#ApiClient.SignalApi.CreateSawSegment)
  - [M CreateSignal ](#ApiClient.SignalApi.CreateSignal)
  - [M CreateSignalValueSegment ](#ApiClient.SignalApi.CreateSignalValueSegment)
  - [M CreateSineSegment ](#ApiClient.SignalApi.CreateSineSegment)
  - [M GetSignalNames ](#ApiClient.SignalApi.GetSignalNames)

# API for Signals[¶](#api-for-signals "Link to this heading")

Part of the [Object based program API](objectApi.md#objectapi).

*class* SignalApi[¶](#ApiClient.SignalApi "Link to this definition")  
Returned by

- [`SignalDescriptionApi.SignalApi`](SignalDescriptionApi.md#ApiClient.SignalDescriptionApi.SignalApi "ApiClient.SignalDescriptionApi.SignalApi (Python attribute) — Returns the SignalApi namespace.")

SymbolApi[¶](#ApiClient.SignalApi.SymbolApi "Link to this definition")  
Returns the SymbolApi namespace.

Returns:  SymbolApi namespace

Return type:  [`SymbolApi`](SymbolApi.md#ApiClient.SymbolApi "ApiClient.SymbolApi (Python class) — SignalApi.SymbolApi")

CreateConstantSegment(*[duration](#ApiClient.SignalApi.CreateConstantSegment.duration "ApiClient.SignalApi.CreateConstantSegment.duration (Python parameter) — Duration of segment")=`1.0`*, *[value](#ApiClient.SignalApi.CreateConstantSegment.value "ApiClient.SignalApi.CreateConstantSegment.value (Python parameter) — Amplitude of signal value")=`0.0`*)[¶](#ApiClient.SignalApi.CreateConstantSegment "Link to this definition")  
Creates a constant signal segment

Parameters:  duration : float[¶](#ApiClient.SignalApi.CreateConstantSegment.duration "Permalink to this definition")  
Duration of segment

value : float[¶](#ApiClient.SignalApi.CreateConstantSegment.value "Permalink to this definition")  
Amplitude of signal value

Returns:  New ConstantSegment

Return type:  [`ConstantSegment`](SignalApi/ConstantSegment.md#ApiClient.ConstantSegment "ApiClient.ConstantSegment (Python class) — SignalApi.CreateConstantSegment")

CreateDataFileSegment(*[filePath](#ApiClient.SignalApi.CreateDataFileSegment.filePath "ApiClient.SignalApi.CreateDataFileSegment.filePath (Python parameter) — Path of the trace file.")*, *[dataVectorName](#ApiClient.SignalApi.CreateDataFileSegment.dataVectorName "ApiClient.SignalApi.CreateDataFileSegment.dataVectorName (Python parameter) — Name of the signal in the trace file to be used for signal values")*, *[timeVectorName](#ApiClient.SignalApi.CreateDataFileSegment.timeVectorName "ApiClient.SignalApi.CreateDataFileSegment.timeVectorName (Python parameter) — Name of the signal in the trace file to be used as time vector")=`'time'`*, *[interpolationType](#ApiClient.SignalApi.CreateDataFileSegment.interpolationType "ApiClient.SignalApi.CreateDataFileSegment.interpolationType (Python parameter) — Interpolation method (backward, forward, linear)")=`'backward'`*, *[channelPath](#ApiClient.SignalApi.CreateDataFileSegment.channelPath "ApiClient.SignalApi.CreateDataFileSegment.channelPath (Python parameter) — Name of the channel path")=`None`*, *[channelSource](#ApiClient.SignalApi.CreateDataFileSegment.channelSource "ApiClient.SignalApi.CreateDataFileSegment.channelSource (Python parameter) — Name of the channel source")=`None`*, *[groupName](#ApiClient.SignalApi.CreateDataFileSegment.groupName "ApiClient.SignalApi.CreateDataFileSegment.groupName (Python parameter) — Name of the group")=`None`*, *[groupPath](#ApiClient.SignalApi.CreateDataFileSegment.groupPath "ApiClient.SignalApi.CreateDataFileSegment.groupPath (Python parameter) — Name of the group path")=`None`*, *[groupSource](#ApiClient.SignalApi.CreateDataFileSegment.groupSource "ApiClient.SignalApi.CreateDataFileSegment.groupSource (Python parameter) — Name of the group source")=`None`*)[¶](#ApiClient.SignalApi.CreateDataFileSegment "Link to this definition")  
Creates a signal segment which references a trace file to use a contained signal

Parameters:  filePath : string[¶](#ApiClient.SignalApi.CreateDataFileSegment.filePath "Permalink to this definition")  
Path of the trace file. Either absolute or relativ to workspace

dataVectorName : string[¶](#ApiClient.SignalApi.CreateDataFileSegment.dataVectorName "Permalink to this definition")  
Name of the signal in the trace file to be used for signal values

timeVectorName : string[¶](#ApiClient.SignalApi.CreateDataFileSegment.timeVectorName "Permalink to this definition")  
Name of the signal in the trace file to be used as time vector

interpolationType : string[¶](#ApiClient.SignalApi.CreateDataFileSegment.interpolationType "Permalink to this definition")  
Interpolation method (backward, forward, linear)

channelPath : string[¶](#ApiClient.SignalApi.CreateDataFileSegment.channelPath "Permalink to this definition")  
Name of the channel path

channelSource : string[¶](#ApiClient.SignalApi.CreateDataFileSegment.channelSource "Permalink to this definition")  
Name of the channel source

groupName : string[¶](#ApiClient.SignalApi.CreateDataFileSegment.groupName "Permalink to this definition")  
Name of the group

groupPath : string[¶](#ApiClient.SignalApi.CreateDataFileSegment.groupPath "Permalink to this definition")  
Name of the group path

groupSource : string[¶](#ApiClient.SignalApi.CreateDataFileSegment.groupSource "Permalink to this definition")  
Name of the group source

Returns:  New DataFileSegment

Return type:  [`DataFileSegment`](SignalApi/DataFileSegment.md#ApiClient.DataFileSegment "ApiClient.DataFileSegment (Python class) — SignalApi.CreateDataFileSegment")

CreateExponentialSegment(*[duration](#ApiClient.SignalApi.CreateExponentialSegment.duration "ApiClient.SignalApi.CreateExponentialSegment.duration (Python parameter) — Duration of segment")=`1.0`*, *[start](#ApiClient.SignalApi.CreateExponentialSegment.start "ApiClient.SignalApi.CreateExponentialSegment.start (Python parameter) — Start of signal")=`0.0`*, *[stop](#ApiClient.SignalApi.CreateExponentialSegment.stop "ApiClient.SignalApi.CreateExponentialSegment.stop (Python parameter) — Stop of signal")=`1.0`*, *[tau](#ApiClient.SignalApi.CreateExponentialSegment.tau "ApiClient.SignalApi.CreateExponentialSegment.tau (Python parameter) — Tau of signal")=`0.5`*)[¶](#ApiClient.SignalApi.CreateExponentialSegment "Link to this definition")  
Creates an exponential signal segment

Parameters:  duration : float[¶](#ApiClient.SignalApi.CreateExponentialSegment.duration "Permalink to this definition")  
Duration of segment

start : float[¶](#ApiClient.SignalApi.CreateExponentialSegment.start "Permalink to this definition")  
Start of signal

stop : float[¶](#ApiClient.SignalApi.CreateExponentialSegment.stop "Permalink to this definition")  
Stop of signal

tau : float[¶](#ApiClient.SignalApi.CreateExponentialSegment.tau "Permalink to this definition")  
Tau of signal

Returns:  New ExponentialSegment

Return type:  [`ExponentialSegment`](SignalApi/ExponentialSegment.md#ApiClient.ExponentialSegment "ApiClient.ExponentialSegment (Python class) — SignalApi.CreateExponentialSegment")

CreateIdleSegment(*[duration](#ApiClient.SignalApi.CreateIdleSegment.duration "ApiClient.SignalApi.CreateIdleSegment.duration (Python parameter) — Duration of segment")=`1.0`*)[¶](#ApiClient.SignalApi.CreateIdleSegment "Link to this definition")  
Creates an idle signal segment

Parameters:  duration : float[¶](#ApiClient.SignalApi.CreateIdleSegment.duration "Permalink to this definition")  
Duration of segment

Returns:  New IdleSegment

Return type:  [`IdleSegment`](SignalApi/IdleSegment.md#ApiClient.IdleSegment "ApiClient.IdleSegment (Python class) — SignalApi.CreateIdleSegment")

CreateLoopSegment(*[loopCount](#ApiClient.SignalApi.CreateLoopSegment.loopCount "ApiClient.SignalApi.CreateLoopSegment.loopCount (Python parameter) — Number of loops for segment")=`1`*)[¶](#ApiClient.SignalApi.CreateLoopSegment "Link to this definition")  
Creates a loop signal segment

Parameters:  loopCount : int[¶](#ApiClient.SignalApi.CreateLoopSegment.loopCount "Permalink to this definition")  
Number of loops for segment

Returns:  New LoopSegment

Return type:  [`LoopSegment`](SignalApi/LoopSegment.md#ApiClient.LoopSegment "ApiClient.LoopSegment (Python class) — SignalApi.CreateLoopSegment")

CreateNoiseSegment(*[duration](#ApiClient.SignalApi.CreateNoiseSegment.duration "ApiClient.SignalApi.CreateNoiseSegment.duration (Python parameter) — Duration of segment")=`1.0`*, *[mean](#ApiClient.SignalApi.CreateNoiseSegment.mean "ApiClient.SignalApi.CreateNoiseSegment.mean (Python parameter) — Mean of signal")=`0.0`*, *[sigma](#ApiClient.SignalApi.CreateNoiseSegment.sigma "ApiClient.SignalApi.CreateNoiseSegment.sigma (Python parameter) — Sigma of signal")=`1.0`*, *[seed](#ApiClient.SignalApi.CreateNoiseSegment.seed "ApiClient.SignalApi.CreateNoiseSegment.seed (Python parameter) — Seed of signal")=`0.0`*)[¶](#ApiClient.SignalApi.CreateNoiseSegment "Link to this definition")  
Creates a noise signal segment

Parameters:  duration : float[¶](#ApiClient.SignalApi.CreateNoiseSegment.duration "Permalink to this definition")  
Duration of segment

mean : float[¶](#ApiClient.SignalApi.CreateNoiseSegment.mean "Permalink to this definition")  
Mean of signal

sigma : float[¶](#ApiClient.SignalApi.CreateNoiseSegment.sigma "Permalink to this definition")  
Sigma of signal

seed : float[¶](#ApiClient.SignalApi.CreateNoiseSegment.seed "Permalink to this definition")  
Seed of signal

Returns:  New NoiseSegment

Return type:  [`NoiseSegment`](SignalApi/NoiseSegment.md#ApiClient.NoiseSegment "ApiClient.NoiseSegment (Python class) — SignalApi.CreateNoiseSegment")

CreateOperationSegment()[¶](#ApiClient.SignalApi.CreateOperationSegment "Link to this definition")  
Creates an operation signal segment

Returns:  New OperationSegment

Return type:  [`OperationSegment`](SignalApi/OperationSegment.md#ApiClient.OperationSegment "ApiClient.OperationSegment (Python class) — SignalApi.CreateOperationSegment")

CreateOperationSignal(*[name](#ApiClient.SignalApi.CreateOperationSignal.name "ApiClient.SignalApi.CreateOperationSignal.name (Python parameter) — Name for the signal")*)[¶](#ApiClient.SignalApi.CreateOperationSignal "Link to this definition")  
Creates an empty operation signal definition

Parameters:  name : str[¶](#ApiClient.SignalApi.CreateOperationSignal.name "Permalink to this definition")  
Name for the signal

Returns:  New operation signal

Return type:  [`OperationSignalDescription`](SignalApi/OperationSignalDescription.md#ApiClient.OperationSignalDescription "ApiClient.OperationSignalDescription (Python class) — SignalApi.CreateOperationSignal")

CreatePulseSegment(*[duration](#ApiClient.SignalApi.CreatePulseSegment.duration "ApiClient.SignalApi.CreatePulseSegment.duration (Python parameter) — Duration of segment")=`1.0`*, *[offset](#ApiClient.SignalApi.CreatePulseSegment.offset "ApiClient.SignalApi.CreatePulseSegment.offset (Python parameter) — Offset of signal")=`0.0`*, *[amplitude](#ApiClient.SignalApi.CreatePulseSegment.amplitude "ApiClient.SignalApi.CreatePulseSegment.amplitude (Python parameter) — Amplitude of signal")=`1.0`*, *[period](#ApiClient.SignalApi.CreatePulseSegment.period "ApiClient.SignalApi.CreatePulseSegment.period (Python parameter) — Period of signal")=`1.0`*, *[dutyCycle](#ApiClient.SignalApi.CreatePulseSegment.dutyCycle "ApiClient.SignalApi.CreatePulseSegment.dutyCycle (Python parameter) — DutyCycle of signal")=`0.5`*, *[phase](#ApiClient.SignalApi.CreatePulseSegment.phase "ApiClient.SignalApi.CreatePulseSegment.phase (Python parameter) — Phase of signal")=`0.0`*)[¶](#ApiClient.SignalApi.CreatePulseSegment "Link to this definition")  
Creates a pulse signal segment

Parameters:  duration : float[¶](#ApiClient.SignalApi.CreatePulseSegment.duration "Permalink to this definition")  
Duration of segment

offset : float[¶](#ApiClient.SignalApi.CreatePulseSegment.offset "Permalink to this definition")  
Offset of signal

amplitude : float[¶](#ApiClient.SignalApi.CreatePulseSegment.amplitude "Permalink to this definition")  
Amplitude of signal

period : float[¶](#ApiClient.SignalApi.CreatePulseSegment.period "Permalink to this definition")  
Period of signal

dutyCycle : float[¶](#ApiClient.SignalApi.CreatePulseSegment.dutyCycle "Permalink to this definition")  
DutyCycle of signal

phase : float[¶](#ApiClient.SignalApi.CreatePulseSegment.phase "Permalink to this definition")  
Phase of signal

Returns:  New PulseSegment

Return type:  [`PulseSegment`](SignalApi/PulseSegment.md#ApiClient.PulseSegment "ApiClient.PulseSegment (Python class) — SignalApi.CreatePulseSegment")

CreateRampSegment(*[duration](#ApiClient.SignalApi.CreateRampSegment.duration "ApiClient.SignalApi.CreateRampSegment.duration (Python parameter) — Duration of segment")=`1.0`*, *[startValue](#ApiClient.SignalApi.CreateRampSegment.startValue "ApiClient.SignalApi.CreateRampSegment.startValue (Python parameter) — Amplitude of signal at the start")=`0.0`*, *[stopValue](#ApiClient.SignalApi.CreateRampSegment.stopValue "ApiClient.SignalApi.CreateRampSegment.stopValue (Python parameter) — Amplitude of signal at the end")=`1.0`*)[¶](#ApiClient.SignalApi.CreateRampSegment "Link to this definition")  
Creates a ramp signal segment

Parameters:  duration : float[¶](#ApiClient.SignalApi.CreateRampSegment.duration "Permalink to this definition")  
Duration of segment

startValue : float[¶](#ApiClient.SignalApi.CreateRampSegment.startValue "Permalink to this definition")  
Amplitude of signal at the start

stopValue : float[¶](#ApiClient.SignalApi.CreateRampSegment.stopValue "Permalink to this definition")  
Amplitude of signal at the end

Returns:  New RampSegment

Return type:  [`RampSegment`](SignalApi/RampSegment.md#ApiClient.RampSegment "ApiClient.RampSegment (Python class) — SignalApi.CreateRampSegment")

CreateRampSlopeSegment(*[duration](#ApiClient.SignalApi.CreateRampSlopeSegment.duration "ApiClient.SignalApi.CreateRampSlopeSegment.duration (Python parameter) — Duration of segment")=`1.0`*, *[offset](#ApiClient.SignalApi.CreateRampSlopeSegment.offset "ApiClient.SignalApi.CreateRampSlopeSegment.offset (Python parameter) — Offset of signal at the start")=`0.0`*, *[slope](#ApiClient.SignalApi.CreateRampSlopeSegment.slope "ApiClient.SignalApi.CreateRampSlopeSegment.slope (Python parameter) — Slope of signal")=`1.0`*)[¶](#ApiClient.SignalApi.CreateRampSlopeSegment "Link to this definition")  
Creates a ramp slope signal segment

Parameters:  duration : float[¶](#ApiClient.SignalApi.CreateRampSlopeSegment.duration "Permalink to this definition")  
Duration of segment

offset : float[¶](#ApiClient.SignalApi.CreateRampSlopeSegment.offset "Permalink to this definition")  
Offset of signal at the start

slope : float[¶](#ApiClient.SignalApi.CreateRampSlopeSegment.slope "Permalink to this definition")  
Slope of signal

Returns:  New RampSlopeSegment

Return type:  [`RampSlopeSegment`](SignalApi/RampSlopeSegment.md#ApiClient.RampSlopeSegment "ApiClient.RampSlopeSegment (Python class) — SignalApi.CreateRampSlopeSegment")

CreateSawSegment(*[duration](#ApiClient.SignalApi.CreateSawSegment.duration "ApiClient.SignalApi.CreateSawSegment.duration (Python parameter) — Duration of segment")=`1.0`*, *[offset](#ApiClient.SignalApi.CreateSawSegment.offset "ApiClient.SignalApi.CreateSawSegment.offset (Python parameter) — Offset of signal")=`0.0`*, *[amplitude](#ApiClient.SignalApi.CreateSawSegment.amplitude "ApiClient.SignalApi.CreateSawSegment.amplitude (Python parameter) — Amplitude of signal")=`1.0`*, *[period](#ApiClient.SignalApi.CreateSawSegment.period "ApiClient.SignalApi.CreateSawSegment.period (Python parameter) — Period of signal")=`1.0`*, *[dutyCycle](#ApiClient.SignalApi.CreateSawSegment.dutyCycle "ApiClient.SignalApi.CreateSawSegment.dutyCycle (Python parameter) — DutyCycle of signal")=`0.5`*, *[phase](#ApiClient.SignalApi.CreateSawSegment.phase "ApiClient.SignalApi.CreateSawSegment.phase (Python parameter) — Phase of signal")=`0.0`*)[¶](#ApiClient.SignalApi.CreateSawSegment "Link to this definition")  
Creates a saw signal segment

Parameters:  duration : float[¶](#ApiClient.SignalApi.CreateSawSegment.duration "Permalink to this definition")  
Duration of segment

offset : float[¶](#ApiClient.SignalApi.CreateSawSegment.offset "Permalink to this definition")  
Offset of signal

amplitude : float[¶](#ApiClient.SignalApi.CreateSawSegment.amplitude "Permalink to this definition")  
Amplitude of signal

period : float[¶](#ApiClient.SignalApi.CreateSawSegment.period "Permalink to this definition")  
Period of signal

dutyCycle : float[¶](#ApiClient.SignalApi.CreateSawSegment.dutyCycle "Permalink to this definition")  
DutyCycle of signal

phase : float[¶](#ApiClient.SignalApi.CreateSawSegment.phase "Permalink to this definition")  
Phase of signal

Returns:  New SawSegment

Return type:  [`SawSegment`](SignalApi/SawSegment.md#ApiClient.SawSegment "ApiClient.SawSegment (Python class) — SignalApi.CreateSawSegment")

CreateSignal(*[name](#ApiClient.SignalApi.CreateSignal.name "ApiClient.SignalApi.CreateSignal.name (Python parameter) — Name for the signal")*)[¶](#ApiClient.SignalApi.CreateSignal "Link to this definition")  
Creates an empty signal definition

Parameters:  name : str[¶](#ApiClient.SignalApi.CreateSignal.name "Permalink to this definition")  
Name for the signal

Returns:  New signal

Return type:  [`SegmentSignalDescription`](SignalApi/SegmentSignalDescription.md#ApiClient.SegmentSignalDescription "ApiClient.SegmentSignalDescription (Python class) — SignalApi.CreateSignal")

CreateSignalValueSegment(*[timeVector](#ApiClient.SignalApi.CreateSignalValueSegment.timeVector "ApiClient.SignalApi.CreateSignalValueSegment.timeVector (Python parameter) — vector of timestamps")=`None`*, *[dataVector](#ApiClient.SignalApi.CreateSignalValueSegment.dataVector "ApiClient.SignalApi.CreateSignalValueSegment.dataVector (Python parameter) — vector of values")=`None`*, *[interpolationType](#ApiClient.SignalApi.CreateSignalValueSegment.interpolationType "ApiClient.SignalApi.CreateSignalValueSegment.interpolationType (Python parameter) — Interpolation method (backward, forward, linear)")=`'backward'`*)[¶](#ApiClient.SignalApi.CreateSignalValueSegment "Link to this definition")  
Creates a signal segment which explicitly takes a vector of timestamps and corresponding values. The timeVector and dataVector list must be of same length.

Parameters:  timeVector : list[float][¶](#ApiClient.SignalApi.CreateSignalValueSegment.timeVector "Permalink to this definition")  
vector of timestamps

dataVector : list[float][¶](#ApiClient.SignalApi.CreateSignalValueSegment.dataVector "Permalink to this definition")  
vector of values

interpolationType : string[¶](#ApiClient.SignalApi.CreateSignalValueSegment.interpolationType "Permalink to this definition")  
Interpolation method (backward, forward, linear)

Returns:  New SignalValueSegment

Return type:  [`SignalValueSegment`](SignalApi/SignalValueSegment.md#ApiClient.SignalValueSegment "ApiClient.SignalValueSegment (Python class) — SignalApi.CreateSignalValueSegment")

CreateSineSegment(*[duration](#ApiClient.SignalApi.CreateSineSegment.duration "ApiClient.SignalApi.CreateSineSegment.duration (Python parameter) — Duration of segment")=`1.0`*, *[offset](#ApiClient.SignalApi.CreateSineSegment.offset "ApiClient.SignalApi.CreateSineSegment.offset (Python parameter) — Offset of signal")=`0.0`*, *[amplitude](#ApiClient.SignalApi.CreateSineSegment.amplitude "ApiClient.SignalApi.CreateSineSegment.amplitude (Python parameter) — Amplitude of signal")=`1.0`*, *[period](#ApiClient.SignalApi.CreateSineSegment.period "ApiClient.SignalApi.CreateSineSegment.period (Python parameter) — Period of signal")=`1.0`*, *[phase](#ApiClient.SignalApi.CreateSineSegment.phase "ApiClient.SignalApi.CreateSineSegment.phase (Python parameter) — Phase of signal")=`0.0`*)[¶](#ApiClient.SignalApi.CreateSineSegment "Link to this definition")  
Creates a sine signal segment

Parameters:  duration : float[¶](#ApiClient.SignalApi.CreateSineSegment.duration "Permalink to this definition")  
Duration of segment

offset : float[¶](#ApiClient.SignalApi.CreateSineSegment.offset "Permalink to this definition")  
Offset of signal

amplitude : float[¶](#ApiClient.SignalApi.CreateSineSegment.amplitude "Permalink to this definition")  
Amplitude of signal

period : float[¶](#ApiClient.SignalApi.CreateSineSegment.period "Permalink to this definition")  
Period of signal

phase : float[¶](#ApiClient.SignalApi.CreateSineSegment.phase "Permalink to this definition")  
Phase of signal

Returns:  New SineSegment

Return type:  [`SineSegment`](SignalApi/SineSegment.md#ApiClient.SineSegment "ApiClient.SineSegment (Python class) — SignalApi.CreateSineSegment")

GetSignalNames(*[filePath](#ApiClient.SignalApi.GetSignalNames.filePath "ApiClient.SignalApi.GetSignalNames.filePath (Python parameter) — Path of the trace file.")*, *[signalGroupName](#ApiClient.SignalApi.GetSignalNames.signalGroupName "ApiClient.SignalApi.GetSignalNames.signalGroupName (Python parameter) — Name of the Signal Group")=`None`*)[¶](#ApiClient.SignalApi.GetSignalNames "Link to this definition")  
Returns a list of all signal names (except time signal) within the referenced tracefile.

Parameters:  filePath : string[¶](#ApiClient.SignalApi.GetSignalNames.filePath "Permalink to this definition")  
Path of the trace file. Either absolute or relativ to workspace

signalGroupName : string[¶](#ApiClient.SignalApi.GetSignalNames.signalGroupName "Permalink to this definition")  
Name of the Signal Group

Returns:  The names of all Signals

Return type:  list[str]

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
