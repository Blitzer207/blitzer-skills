# API for Signals[¶](#api-for-signals "Link to this heading")

Part of the [Object based program API](objectApi.md#objectapi)

## SignalApi[¶](#signalapi "Link to this heading")

*class* SignalApi[¶](#ApiClient.SignalApi "Link to this definition")  
Returned by

- [`SignalDescriptionApi.SignalApi`](SignalDescriptionApi.md#ApiClient.SignalDescriptionApi.SignalApi "ApiClient.SignalDescriptionApi.SignalApi")

SymbolApi[¶](#ApiClient.SignalApi.SymbolApi "Link to this definition")  
Returns the SymbolApi namespace.

Returns:  SymbolApi namespace

Return type:  [`SymbolApi`](SymbolApi.md#ApiClient.SymbolApi "ApiClient.SymbolApi")

CreateConstantSegment(*duration=1.0*, *value=0.0*)[¶](#ApiClient.SignalApi.CreateConstantSegment "Link to this definition")  
Creates a constant signal segment

Parameters:  - **duration** (*float*) – Duration of segment

- **value** (*float*) – Amplitude of signal value

Returns:  New ConstantSegment

Return type:  [`ConstantSegment`](#ApiClient.ConstantSegment "ApiClient.ConstantSegment")

CreateDataFileSegment(*filePath*, *dataVectorName*, *timeVectorName='time'*, *interpolationType='backward'*, *channelPath=None*, *channelSource=None*, *groupName=None*, *groupPath=None*, *groupSource=None*)[¶](#ApiClient.SignalApi.CreateDataFileSegment "Link to this definition")  
Creates a signal segment which references a trace file to use a contained signal

Parameters:  - **filePath** (*string*) – Path of the trace file. Either absolute or relativ to workspace

- **dataVectorName** (*string*) – Name of the signal in the trace file to be used for signal values

- **timeVectorName** (*string*) – Name of the signal in the trace file to be used as time vector

- **interpolationType** (*string*) – Interpolation method (backward, forward, linear)

- **channelPath** (*string*) – Name of the channel path

- **channelSource** (*string*) – Name of the channel source

- **groupName** (*string*) – Name of the group

- **groupPath** (*string*) – Name of the group path

- **groupSource** (*string*) – Name of the group source

Returns:  New DataFileSegment

Return type:  [`DataFileSegment`](#ApiClient.DataFileSegment "ApiClient.DataFileSegment")

CreateExponentialSegment(*duration=1.0*, *start=0.0*, *stop=1.0*, *tau=0.5*)[¶](#ApiClient.SignalApi.CreateExponentialSegment "Link to this definition")  
Creates an exponential signal segment

Parameters:  - **duration** (*float*) – Duration of segment

- **start** (*float*) – Start of signal

- **stop** (*float*) – Stop of signal

- **tau** (*float*) – Tau of signal

Returns:  New ExponentialSegment

Return type:  [`ExponentialSegment`](#ApiClient.ExponentialSegment "ApiClient.ExponentialSegment")

CreateIdleSegment(*duration=1.0*)[¶](#ApiClient.SignalApi.CreateIdleSegment "Link to this definition")  
Creates an idle signal segment

Parameters:  **duration** (*float*) – Duration of segment

Returns:  New IdleSegment

Return type:  [`IdleSegment`](#ApiClient.IdleSegment "ApiClient.IdleSegment")

CreateLoopSegment(*loopCount=1*)[¶](#ApiClient.SignalApi.CreateLoopSegment "Link to this definition")  
Creates a loop signal segment

Parameters:  **loopCount** (*int*) – Number of loops for segment

Returns:  New LoopSegment

Return type:  [`LoopSegment`](#ApiClient.LoopSegment "ApiClient.LoopSegment")

CreateNoiseSegment(*duration=1.0*, *mean=0.0*, *sigma=1.0*, *seed=0.0*)[¶](#ApiClient.SignalApi.CreateNoiseSegment "Link to this definition")  
Creates a noise signal segment

Parameters:  - **duration** (*float*) – Duration of segment

- **mean** (*float*) – Mean of signal

- **sigma** (*float*) – Sigma of signal

- **seed** (*float*) – Seed of signal

Returns:  New NoiseSegment

Return type:  [`NoiseSegment`](#ApiClient.NoiseSegment "ApiClient.NoiseSegment")

CreateOperationSegment()[¶](#ApiClient.SignalApi.CreateOperationSegment "Link to this definition")  
Creates an operation signal segment

Returns:  New OperationSegment

Return type:  [`OperationSegment`](#ApiClient.OperationSegment "ApiClient.OperationSegment")

CreateOperationSignal(*name*)[¶](#ApiClient.SignalApi.CreateOperationSignal "Link to this definition")  
Creates an empty operation signal definition

Parameters:  **name** (*str*) – Name for the signal

Returns:  New operation signal

Return type:  [`OperationSignalDescription`](#ApiClient.OperationSignalDescription "ApiClient.OperationSignalDescription")

CreatePulseSegment(*duration=1.0*, *offset=0.0*, *amplitude=1.0*, *period=1.0*, *dutyCycle=0.5*, *phase=0.0*)[¶](#ApiClient.SignalApi.CreatePulseSegment "Link to this definition")  
Creates a pulse signal segment

Parameters:  - **duration** (*float*) – Duration of segment

- **offset** (*float*) – Offset of signal

- **amplitude** (*float*) – Amplitude of signal

- **period** (*float*) – Period of signal

- **dutyCycle** (*float*) – DutyCycle of signal

- **phase** (*float*) – Phase of signal

Returns:  New PulseSegment

Return type:  [`PulseSegment`](#ApiClient.PulseSegment "ApiClient.PulseSegment")

CreateRampSegment(*duration=1.0*, *startValue=0.0*, *stopValue=1.0*)[¶](#ApiClient.SignalApi.CreateRampSegment "Link to this definition")  
Creates a ramp signal segment

Parameters:  - **duration** (*float*) – Duration of segment

- **startValue** (*float*) – Amplitude of signal at the start

- **stopValue** (*float*) – Amplitude of signal at the end

Returns:  New RampSegment

Return type:  [`RampSegment`](#ApiClient.RampSegment "ApiClient.RampSegment")

CreateRampSlopeSegment(*duration=1.0*, *offset=0.0*, *slope=1.0*)[¶](#ApiClient.SignalApi.CreateRampSlopeSegment "Link to this definition")  
Creates a ramp slope signal segment

Parameters:  - **duration** (*float*) – Duration of segment

- **offset** (*float*) – Offset of signal at the start

- **slope** (*float*) – Slope of signal

Returns:  New RampSlopeSegment

Return type:  [`RampSlopeSegment`](#ApiClient.RampSlopeSegment "ApiClient.RampSlopeSegment")

CreateSawSegment(*duration=1.0*, *offset=0.0*, *amplitude=1.0*, *period=1.0*, *dutyCycle=0.5*, *phase=0.0*)[¶](#ApiClient.SignalApi.CreateSawSegment "Link to this definition")  
Creates a saw signal segment

Parameters:  - **duration** (*float*) – Duration of segment

- **offset** (*float*) – Offset of signal

- **amplitude** (*float*) – Amplitude of signal

- **period** (*float*) – Period of signal

- **dutyCycle** (*float*) – DutyCycle of signal

- **phase** (*float*) – Phase of signal

Returns:  New SawSegment

Return type:  [`SawSegment`](#ApiClient.SawSegment "ApiClient.SawSegment")

CreateSignal(*name*)[¶](#ApiClient.SignalApi.CreateSignal "Link to this definition")  
Creates an empty signal definition

Parameters:  **name** (*str*) – Name for the signal

Returns:  New signal

Return type:  [`SegmentSignalDescription`](#ApiClient.SegmentSignalDescription "ApiClient.SegmentSignalDescription")

CreateSignalValueSegment(*timeVector=None*, *dataVector=None*, *interpolationType='backward'*)[¶](#ApiClient.SignalApi.CreateSignalValueSegment "Link to this definition")  
Creates a signal segment which explicitly takes a vector of timestamps and corresponding values. The timeVector and dataVector list must be of same length.

Parameters:  - **timeVector** (*list[float]*) – vector of timestamps

- **dataVector** (*list[float]*) – vector of values

- **interpolationType** (*string*) – Interpolation method (backward, forward, linear)

Returns:  New SignalValueSegment

Return type:  [`SignalValueSegment`](#ApiClient.SignalValueSegment "ApiClient.SignalValueSegment")

CreateSineSegment(*duration=1.0*, *offset=0.0*, *amplitude=1.0*, *period=1.0*, *phase=0.0*)[¶](#ApiClient.SignalApi.CreateSineSegment "Link to this definition")  
Creates a sine signal segment

Parameters:  - **duration** (*float*) – Duration of segment

- **offset** (*float*) – Offset of signal

- **amplitude** (*float*) – Amplitude of signal

- **period** (*float*) – Period of signal

- **phase** (*float*) – Phase of signal

Returns:  New SineSegment

Return type:  [`SineSegment`](#ApiClient.SineSegment "ApiClient.SineSegment")

GetSignalNames(*filePath*, *signalGroupName=None*)[¶](#ApiClient.SignalApi.GetSignalNames "Link to this definition")  
Returns a list of all signal names (except time signal) within the referenced tracefile.

Parameters:  - **filePath** (*string*) – Path of the trace file. Either absolute or relativ to workspace

- **signalGroupName** (*string*) – Name of the Signal Group

Returns:  The names of all Signals

Return type:  list[str]

## ConstantSegment[¶](#constantsegment "Link to this heading")

*class* ConstantSegment[¶](#ApiClient.ConstantSegment "Link to this definition")  
Base class

[`SignalSegment`](#ApiClient.SignalSegment "ApiClient.SignalSegment")

Returned by

- [`SignalApi.CreateConstantSegment`](#ApiClient.SignalApi.CreateConstantSegment "ApiClient.SignalApi.CreateConstantSegment")

Clone()[¶](#ApiClient.ConstantSegment.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`ConstantSegment`](#ApiClient.ConstantSegment "ApiClient.ConstantSegment")

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

GetValueAt(*timestamp*)[¶](#ApiClient.ConstantSegment.GetValueAt "Link to this definition")  
Returns the value at the given timestamp.

Parameters:  **timestamp** (*float*) – The timestamp

Returns:  the value or NaN

Return type:  float

GetValueExpression()[¶](#ApiClient.ConstantSegment.GetValueExpression "Link to this definition")  
Returns the expression of the value of the segment. The expression is conform to the ASAM XIL GES syntax for ConstSymbol expressions.

Return type:  str

Returns:  the value expression.

GetValueSymbol()[¶](#ApiClient.ConstantSegment.GetValueSymbol "Link to this definition")  
Returns the SymbolType object of the segment value.

Return type:  [`SymbolType`](#ApiClient.SymbolType "ApiClient.SymbolType")

Returns:  the value symbol

RemoveStopTrigger()[¶](#ApiClient.ConstantSegment.RemoveStopTrigger "Link to this definition")  
Removes the stop trigger of the segment

RemoveTimeout()[¶](#ApiClient.ConstantSegment.RemoveTimeout "Link to this definition")  
Removes the timeout of the segment

SetComment(*comment*)[¶](#ApiClient.ConstantSegment.SetComment "Link to this definition")  
Sets the comment of the segment.

Parameters:  **comment** (*str*) – The comment

SetDuration(*duration*)[¶](#ApiClient.ConstantSegment.SetDuration "Link to this definition")  
Sets the duration of the segment in seconds.If you want to set the duration value of the segment to an expression, use SetDurationExpression instead.

Parameters:  **duration** (*float*) – the segments duration

SetDurationExpression(*expression*)[¶](#ApiClient.ConstantSegment.SetDurationExpression "Link to this definition")  
Sets the duration value as an expression. The expression needs to be conform to the ASAM XIL GES syntax for ConstSymbol expressions.

Parameters:  **expression** (*str*) – the duration expression

SetStopTrigger(*stopTrigger*)[¶](#ApiClient.ConstantSegment.SetStopTrigger "Link to this definition")  
Sets the stop trigger of the segment

Parameters:  **stopTrigger** (*str*) – The stop trigger

SetTimeout(*timeout*)[¶](#ApiClient.ConstantSegment.SetTimeout "Link to this definition")  
Sets the timeout of the segment

Parameters:  **timeout** (*float*) – The timeout

SetValue(*value*)[¶](#ApiClient.ConstantSegment.SetValue "Link to this definition")  
Sets the value of the segment. If you want to set the value of the segment to an expression, use SetValueExpression instead.

Parameters:  **value** (*float*) – the value

SetValueExpression(*expression*)[¶](#ApiClient.ConstantSegment.SetValueExpression "Link to this definition")  
Sets the value expression of the segment. The expression has to be conform to the ASAM XIL GES syntax for ConstSymbol expressions.

Parameters:  **expression** (*str*) – the expression

SetValueSymbol(*value*)[¶](#ApiClient.ConstantSegment.SetValueSymbol "Link to this definition")  
Sets a SymbolType object as value of the segment. If you want to set the value of the segment to an expression, use SetValueExpression instead.

Parameters:  **value** ([`SymbolType`](#ApiClient.SymbolType "ApiClient.SymbolType")) – the value symbol

## SymbolType[¶](#symboltype "Link to this heading")

*class* SymbolType[¶](#ApiClient.SymbolType "Link to this definition")  
Returned by

- [`ConstantSegment.GetValueSymbol`](#ApiClient.ConstantSegment.GetValueSymbol "ApiClient.ConstantSegment.GetValueSymbol")

- [`ExponentialSegment.GetStartSymbol`](#ApiClient.ExponentialSegment.GetStartSymbol "ApiClient.ExponentialSegment.GetStartSymbol")

- [`ExponentialSegment.GetStopSymbol`](#ApiClient.ExponentialSegment.GetStopSymbol "ApiClient.ExponentialSegment.GetStopSymbol")

- [`ExponentialSegment.GetTauSymbol`](#ApiClient.ExponentialSegment.GetTauSymbol "ApiClient.ExponentialSegment.GetTauSymbol")

- [`NoiseSegment.GetMeanSymbol`](#ApiClient.NoiseSegment.GetMeanSymbol "ApiClient.NoiseSegment.GetMeanSymbol")

- [`NoiseSegment.GetSigmaSymbol`](#ApiClient.NoiseSegment.GetSigmaSymbol "ApiClient.NoiseSegment.GetSigmaSymbol")

- [`PulseSegment.GetAmplitudeSymbol`](#ApiClient.PulseSegment.GetAmplitudeSymbol "ApiClient.PulseSegment.GetAmplitudeSymbol")

- [`PulseSegment.GetDutyCycleSymbol`](#ApiClient.PulseSegment.GetDutyCycleSymbol "ApiClient.PulseSegment.GetDutyCycleSymbol")

- [`PulseSegment.GetOffsetSymbol`](#ApiClient.PulseSegment.GetOffsetSymbol "ApiClient.PulseSegment.GetOffsetSymbol")

- [`PulseSegment.GetPeriodSymbol`](#ApiClient.PulseSegment.GetPeriodSymbol "ApiClient.PulseSegment.GetPeriodSymbol")

- [`PulseSegment.GetPhaseSymbol`](#ApiClient.PulseSegment.GetPhaseSymbol "ApiClient.PulseSegment.GetPhaseSymbol")

- [`RampSegment.GetStartSymbol`](#ApiClient.RampSegment.GetStartSymbol "ApiClient.RampSegment.GetStartSymbol")

- [`RampSegment.GetStopSymbol`](#ApiClient.RampSegment.GetStopSymbol "ApiClient.RampSegment.GetStopSymbol")

- [`RampSlopeSegment.GetOffsetSymbol`](#ApiClient.RampSlopeSegment.GetOffsetSymbol "ApiClient.RampSlopeSegment.GetOffsetSymbol")

- [`RampSlopeSegment.GetSlopeSymbol`](#ApiClient.RampSlopeSegment.GetSlopeSymbol "ApiClient.RampSlopeSegment.GetSlopeSymbol")

- [`SawSegment.GetAmplitudeSymbol`](#ApiClient.SawSegment.GetAmplitudeSymbol "ApiClient.SawSegment.GetAmplitudeSymbol")

- [`SawSegment.GetDutyCycleSymbol`](#ApiClient.SawSegment.GetDutyCycleSymbol "ApiClient.SawSegment.GetDutyCycleSymbol")

- [`SawSegment.GetOffsetSymbol`](#ApiClient.SawSegment.GetOffsetSymbol "ApiClient.SawSegment.GetOffsetSymbol")

- [`SawSegment.GetPeriodSymbol`](#ApiClient.SawSegment.GetPeriodSymbol "ApiClient.SawSegment.GetPeriodSymbol")

- [`SawSegment.GetPhaseSymbol`](#ApiClient.SawSegment.GetPhaseSymbol "ApiClient.SawSegment.GetPhaseSymbol")

- [`SineSegment.GetAmplitudeSymbol`](#ApiClient.SineSegment.GetAmplitudeSymbol "ApiClient.SineSegment.GetAmplitudeSymbol")

- [`SineSegment.GetOffsetSymbol`](#ApiClient.SineSegment.GetOffsetSymbol "ApiClient.SineSegment.GetOffsetSymbol")

- [`SineSegment.GetPeriodSymbol`](#ApiClient.SineSegment.GetPeriodSymbol "ApiClient.SineSegment.GetPeriodSymbol")

- [`SineSegment.GetPhaseSymbol`](#ApiClient.SineSegment.GetPhaseSymbol "ApiClient.SineSegment.GetPhaseSymbol")

Subclasses

- [`ConstSymbol`](SymbolApi.md#ApiClient.ConstSymbol "ApiClient.ConstSymbol")

- [`SignalSymbol`](SymbolApi.md#ApiClient.SignalSymbol "ApiClient.SignalSymbol")

- [`StringSymbol`](SymbolApi.md#ApiClient.StringSymbol "ApiClient.StringSymbol")

Clone()[¶](#ApiClient.SymbolType.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`SymbolType`](#ApiClient.SymbolType "ApiClient.SymbolType")

## DataFileSegment[¶](#datafilesegment "Link to this heading")

*class* DataFileSegment[¶](#ApiClient.DataFileSegment "Link to this definition")  
Base class

[`SignalSegment`](#ApiClient.SignalSegment "ApiClient.SignalSegment")

Returned by

- [`SignalApi.CreateDataFileSegment`](#ApiClient.SignalApi.CreateDataFileSegment "ApiClient.SignalApi.CreateDataFileSegment")

Clone()[¶](#ApiClient.DataFileSegment.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`DataFileSegment`](#ApiClient.DataFileSegment "ApiClient.DataFileSegment")

GetActualDuration()[¶](#ApiClient.DataFileSegment.GetActualDuration "Link to this definition")  
Returns the current duration of the DataFileSegment.

Returns:  The calculated duration

Return type:  float

GetChannelPath()[¶](#ApiClient.DataFileSegment.GetChannelPath "Link to this definition")  
Returns the name of the currently set channel path.

Returns:  the name of the channel path

Return type:  str

GetChannelSource()[¶](#ApiClient.DataFileSegment.GetChannelSource "Link to this definition")  
Returns the name of the currently set channel source.

Returns:  the name of the channel source

Return type:  str

GetComment()[¶](#ApiClient.DataFileSegment.GetComment "Link to this definition")  
Returns the comment of the segment.

Returns:  The comment

Return type:  str

GetDataVectorName()[¶](#ApiClient.DataFileSegment.GetDataVectorName "Link to this definition")  
Returns the name of the currently set data vector.

Returns:  the name of the data vector

Return type:  str

GetDuration()[¶](#ApiClient.DataFileSegment.GetDuration "Link to this definition")  
Returns the current duration of the signal segment.

Returns:  The duration

Return type:  float

GetDurationExpression()[¶](#ApiClient.DataFileSegment.GetDurationExpression "Link to this definition")  
Returns the duration expression of the segment that is conform to the ASAM XIL GES syntax for ConstSymbol expressions.

Return type:  str

Returns:  the duration expression

GetFinalValue()[¶](#ApiClient.DataFileSegment.GetFinalValue "Link to this definition")  
Returns the final value of the signal segment.

Returns:  the final value

Return type:  float

GetFirstValue()[¶](#ApiClient.DataFileSegment.GetFirstValue "Link to this definition")  
Returns the first value of the segment.

Returns:  the first value or NaN

Return type:  float

GetGroupName()[¶](#ApiClient.DataFileSegment.GetGroupName "Link to this definition")  
Returns the name of the currently set group name.

Returns:  the name of the group name

Return type:  str

GetGroupPath()[¶](#ApiClient.DataFileSegment.GetGroupPath "Link to this definition")  
Returns the name of the currently set group path.

Returns:  the name of the group path

Return type:  str

GetGroupSource()[¶](#ApiClient.DataFileSegment.GetGroupSource "Link to this definition")  
Returns the name of the currently set group source.

Returns:  the name of the group source

Return type:  str

GetStart()[¶](#ApiClient.DataFileSegment.GetStart "Link to this definition")  
Returns the start property of the DataFileSegment.

Returns:  the start property

Return type:  float

GetStartExpression()[¶](#ApiClient.DataFileSegment.GetStartExpression "Link to this definition")  
Returns the start expression of the segment.

Return type:  str

Returns:  the start expression

GetStopTrigger()[¶](#ApiClient.DataFileSegment.GetStopTrigger "Link to this definition")  
Returns the stop trigger of the segment

Returns:  stop trigger

Return type:  str

GetTimeVectorName()[¶](#ApiClient.DataFileSegment.GetTimeVectorName "Link to this definition")  
Returns the name of the currently set time vector.

Returns:  the name of the time vector

Return type:  str

GetTimeout()[¶](#ApiClient.DataFileSegment.GetTimeout "Link to this definition")  
Returns the timeout of the segment

Returns:  timeout

Return type:  float

GetType()[¶](#ApiClient.DataFileSegment.GetType "Link to this definition")  
Returns the type of the segment. (e.g. “Constant”)

Returns:  The type

Return type:  str

GetValueAt(*timestamp*)[¶](#ApiClient.DataFileSegment.GetValueAt "Link to this definition")  
Returns the value at the given timestamp.

Parameters:  **timestamp** (*float*) – The timestamp

Returns:  the value or NaN

Return type:  float

RemoveStopTrigger()[¶](#ApiClient.DataFileSegment.RemoveStopTrigger "Link to this definition")  
Removes the stop trigger of the segment

RemoveTimeout()[¶](#ApiClient.DataFileSegment.RemoveTimeout "Link to this definition")  
Removes the timeout of the segment

SetChannelPath(*channelPath*)[¶](#ApiClient.DataFileSegment.SetChannelPath "Link to this definition")  
Sets the name of the channel path.

Parameters:  **channelPath** (*str*) – the name of the channel path

SetChannelSource(*channelSource*)[¶](#ApiClient.DataFileSegment.SetChannelSource "Link to this definition")  
Sets the name of the channel source.

Parameters:  **channelSource** (*str*) – the name of the channel source

SetComment(*comment*)[¶](#ApiClient.DataFileSegment.SetComment "Link to this definition")  
Sets the comment of the segment.

Parameters:  **comment** (*str*) – The comment

SetDataVectorName(*dataVectorName*)[¶](#ApiClient.DataFileSegment.SetDataVectorName "Link to this definition")  
Sets the name of the data vector.

Parameters:  **dataVectorName** (*str*) – the name of the data vector

SetDuration(*duration*)[¶](#ApiClient.DataFileSegment.SetDuration "Link to this definition")  
Sets the duration of the segment in seconds.If you want to set the duration value of the segment to an expression, use SetDurationExpression instead.

Parameters:  **duration** (*float*) – the segments duration

SetDurationExpression(*expression*)[¶](#ApiClient.DataFileSegment.SetDurationExpression "Link to this definition")  
Sets the duration of the segment in seconds. duration is also allowed to be a string which is an expression that is conform to the ASAM XIL GES syntax for ConstSymbol expressions. If you want to pass such an expression, use SetDurationExpression instead.

Parameters:  **expression** (*str*) – the segments duration

Raises:  
**ValueError** – the duration is not in range

SetGroupName(*groupName*)[¶](#ApiClient.DataFileSegment.SetGroupName "Link to this definition")  
Sets the name of the group name.

Parameters:  **groupName** (*str*) – the name of the group name

SetGroupPath(*groupPath*)[¶](#ApiClient.DataFileSegment.SetGroupPath "Link to this definition")  
Sets the name of the group path.

Parameters:  **groupPath** (*str*) – the name of the group path

SetGroupSource(*groupSource*)[¶](#ApiClient.DataFileSegment.SetGroupSource "Link to this definition")  
Sets the name of the group source.

Parameters:  **groupSource** (*str*) – the name of the group source

SetStart(*start*)[¶](#ApiClient.DataFileSegment.SetStart "Link to this definition")  
Sets the start property of the DataFileSegment.

Parameters:  **start** (*float*) – the start value such that start is between the min and max value of the timeVector of the referenced DataFile or -inf

SetStartExpression(*expression*)[¶](#ApiClient.DataFileSegment.SetStartExpression "Link to this definition")  
Sets the expression for the start value of the DataFileSegment. The expression needs to be conform to the ASAM XIL GES syntax for ConstSymbol expressions.

Parameters:  **expression** (*str*) – the start value expression

SetStopTrigger(*stopTrigger*)[¶](#ApiClient.DataFileSegment.SetStopTrigger "Link to this definition")  
Sets the stop trigger of the segment

Parameters:  **stopTrigger** (*str*) – The stop trigger

SetTimeVectorName(*timeVectorName*)[¶](#ApiClient.DataFileSegment.SetTimeVectorName "Link to this definition")  
Sets the timeVectorName of the segment

Parameters:  **timeVectorName** (*str*) – the name of the time vector

SetTimeout(*timeout*)[¶](#ApiClient.DataFileSegment.SetTimeout "Link to this definition")  
Sets the timeout of the segment

Parameters:  **timeout** (*float*) – The timeout

## ExponentialSegment[¶](#exponentialsegment "Link to this heading")

*class* ExponentialSegment[¶](#ApiClient.ExponentialSegment "Link to this definition")  
Base class

[`SignalSegment`](#ApiClient.SignalSegment "ApiClient.SignalSegment")

Returned by

- [`SignalApi.CreateExponentialSegment`](#ApiClient.SignalApi.CreateExponentialSegment "ApiClient.SignalApi.CreateExponentialSegment")

Clone()[¶](#ApiClient.ExponentialSegment.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`ExponentialSegment`](#ApiClient.ExponentialSegment "ApiClient.ExponentialSegment")

GetComment()[¶](#ApiClient.ExponentialSegment.GetComment "Link to this definition")  
Returns the comment of the segment.

Returns:  The comment

Return type:  str

GetDuration()[¶](#ApiClient.ExponentialSegment.GetDuration "Link to this definition")  
Returns the current duration of the signal segment.

Returns:  The duration

Return type:  float

GetDurationExpression()[¶](#ApiClient.ExponentialSegment.GetDurationExpression "Link to this definition")  
Returns the duration expression of the segment that is conform to the ASAM XIL GES syntax for ConstSymbol expressions.

Return type:  str

Returns:  the duration expression

GetFinalValue()[¶](#ApiClient.ExponentialSegment.GetFinalValue "Link to this definition")  
Returns the final value of the signal segment.

Returns:  the final value

Return type:  float

GetFirstValue()[¶](#ApiClient.ExponentialSegment.GetFirstValue "Link to this definition")  
Returns the first value of the segment.

Returns:  the first value or NaN

Return type:  float

GetStart()[¶](#ApiClient.ExponentialSegment.GetStart "Link to this definition")  
Returns the start value of the segment. If the start value is set to an expression. the expression gets evaluated. Returns nan if the expression contains unknown parameter.

Return type:  float

Returns:  the start value

GetStartExpression()[¶](#ApiClient.ExponentialSegment.GetStartExpression "Link to this definition")  
Returns the start value expression.

Return type:  str

Returns:  the start value expression

GetStartSymbol()[¶](#ApiClient.ExponentialSegment.GetStartSymbol "Link to this definition")  
Returns the SymbolType object of the segment start value.

Return type:  [`SymbolType`](#ApiClient.SymbolType "ApiClient.SymbolType")

Returns:  the start value symbol

GetStop()[¶](#ApiClient.ExponentialSegment.GetStop "Link to this definition")  
Returns the stop value of the segment.

Return type:  float

Returns:  the stop value

GetStopExpression()[¶](#ApiClient.ExponentialSegment.GetStopExpression "Link to this definition")  
Returns the stop expression of the segment. The expression is conform to the ASAM XIL GES syntax for ConstSymbol expressions.

Return type:  str

Returns:  the stop expression

GetStopSymbol()[¶](#ApiClient.ExponentialSegment.GetStopSymbol "Link to this definition")  
Returns the SymbolType object of the segment stop value.

Return type:  [`SymbolType`](#ApiClient.SymbolType "ApiClient.SymbolType")

Returns:  the stop value symbol

GetStopTrigger()[¶](#ApiClient.ExponentialSegment.GetStopTrigger "Link to this definition")  
Returns the stop trigger of the segment

Returns:  stop trigger

Return type:  str

GetTau()[¶](#ApiClient.ExponentialSegment.GetTau "Link to this definition")  
Returns the current tau value of the segment.

Return type:  float

Returns:  the tau value

GetTauExpression()[¶](#ApiClient.ExponentialSegment.GetTauExpression "Link to this definition")  
Returns the tau value expression of the segment. The expression conforms to the ASAM XIL GES syntax for ConstSymbol expressions

Return type:  str

Returns:  the tau value expression

GetTauSymbol()[¶](#ApiClient.ExponentialSegment.GetTauSymbol "Link to this definition")  
Returns the SymbolType object of the segment tau value.

Return type:  [`SymbolType`](#ApiClient.SymbolType "ApiClient.SymbolType")

Returns:  the tau value symbol

GetTimeout()[¶](#ApiClient.ExponentialSegment.GetTimeout "Link to this definition")  
Returns the timeout of the segment

Returns:  timeout

Return type:  float

GetType()[¶](#ApiClient.ExponentialSegment.GetType "Link to this definition")  
Returns the type of the segment. (e.g. “Constant”)

Returns:  The type

Return type:  str

GetValueAt(*timestamp*)[¶](#ApiClient.ExponentialSegment.GetValueAt "Link to this definition")  
Returns the value at the given timestamp.

Parameters:  **timestamp** (*float*) – The timestamp

Returns:  the value or NaN

Return type:  float

RemoveStopTrigger()[¶](#ApiClient.ExponentialSegment.RemoveStopTrigger "Link to this definition")  
Removes the stop trigger of the segment

RemoveTimeout()[¶](#ApiClient.ExponentialSegment.RemoveTimeout "Link to this definition")  
Removes the timeout of the segment

SetComment(*comment*)[¶](#ApiClient.ExponentialSegment.SetComment "Link to this definition")  
Sets the comment of the segment.

Parameters:  **comment** (*str*) – The comment

SetDuration(*duration*)[¶](#ApiClient.ExponentialSegment.SetDuration "Link to this definition")  
Sets the duration of the segment in seconds.If you want to set the duration value of the segment to an expression, use SetDurationExpression instead.

Parameters:  **duration** (*float*) – the segments duration

SetDurationExpression(*expression*)[¶](#ApiClient.ExponentialSegment.SetDurationExpression "Link to this definition")  
Sets the duration value as an expression. The expression needs to be conform to the ASAM XIL GES syntax for ConstSymbol expressions.

Parameters:  **expression** (*str*) – the duration expression

SetStart(*start*)[¶](#ApiClient.ExponentialSegment.SetStart "Link to this definition")  
Sets the start value of the segment.

Parameters:  **start** (*float*) – the start value

SetStartExpression(*expression*)[¶](#ApiClient.ExponentialSegment.SetStartExpression "Link to this definition")  
Sets the start value of the segment to the given expression. The expression needs to conform to the ASAM XIL GES syntax for ConstSymbol expressions.

Parameters:  **expression** (*str*) – the expression

SetStartSymbol(*value*)[¶](#ApiClient.ExponentialSegment.SetStartSymbol "Link to this definition")  
Sets a SymbolType object as start value of the segment. If you want to set the start value of the segment to an expression, use SetStartExpression instead.

Parameters:  **value** ([`SymbolType`](#ApiClient.SymbolType "ApiClient.SymbolType")) – the start value symbol

SetStop(*stop*)[¶](#ApiClient.ExponentialSegment.SetStop "Link to this definition")  
Set the stop value of the segment.

Parameters:  **stop** (*float*) – the stop value

SetStopExpression(*expression*)[¶](#ApiClient.ExponentialSegment.SetStopExpression "Link to this definition")  
Sets the stop value to the given expression. The expression has to be conform to the ASAM XIL GES syntax for ConstSymbol expressions.

Parameters:  **expression** (*str*) – the expression

SetStopSymbol(*value*)[¶](#ApiClient.ExponentialSegment.SetStopSymbol "Link to this definition")  
Sets a SymbolType object as stop value of the segment. If you want to set the stop value of the segment to an expression, use SetStopExpression instead.

Parameters:  **value** ([`SymbolType`](#ApiClient.SymbolType "ApiClient.SymbolType")) – the stop value symbol

SetStopTrigger(*stopTrigger*)[¶](#ApiClient.ExponentialSegment.SetStopTrigger "Link to this definition")  
Sets the stop trigger of the segment

Parameters:  **stopTrigger** (*str*) – The stop trigger

SetTau(*tau*)[¶](#ApiClient.ExponentialSegment.SetTau "Link to this definition")  
Sets the tau value of the segment.

Parameters:  **tau** (*float*) – the tau value

SetTauExpression(*expression*)[¶](#ApiClient.ExponentialSegment.SetTauExpression "Link to this definition")  
Sets the tau value of the segment to the given expression. The expression has to be conform to the ASAM XIL GES syntax for ConstSymbol expressions.

Parameters:  **expression** (*str*) – the expression

SetTauSymbol(*value*)[¶](#ApiClient.ExponentialSegment.SetTauSymbol "Link to this definition")  
Sets a SymbolType object as tau value of the segment. If you want to set the tau value of the segment to an expression, use SetTauExpression instead.

Parameters:  **value** ([`SymbolType`](#ApiClient.SymbolType "ApiClient.SymbolType")) – the tau value symbol

SetTimeout(*timeout*)[¶](#ApiClient.ExponentialSegment.SetTimeout "Link to this definition")  
Sets the timeout of the segment

Parameters:  **timeout** (*float*) – The timeout

## IdleSegment[¶](#signalapi-idlesegment "Link to this heading")

*class* IdleSegment[¶](#ApiClient.IdleSegment "Link to this definition")  
Base class

[`SignalSegment`](#ApiClient.SignalSegment "ApiClient.SignalSegment")

Returned by

- [`SignalApi.CreateIdleSegment`](#ApiClient.SignalApi.CreateIdleSegment "ApiClient.SignalApi.CreateIdleSegment")

Clone()[¶](#ApiClient.IdleSegment.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`IdleSegment`](#ApiClient.IdleSegment "ApiClient.IdleSegment")

GetComment()[¶](#ApiClient.IdleSegment.GetComment "Link to this definition")  
Returns the comment of the segment.

Returns:  The comment

Return type:  str

GetDuration()[¶](#ApiClient.IdleSegment.GetDuration "Link to this definition")  
Returns the current duration of the signal segment.

Returns:  The duration

Return type:  float

GetDurationExpression()[¶](#ApiClient.IdleSegment.GetDurationExpression "Link to this definition")  
Returns the duration expression of the segment that is conform to the ASAM XIL GES syntax for ConstSymbol expressions.

Return type:  str

Returns:  the duration expression

GetFinalValue()[¶](#ApiClient.IdleSegment.GetFinalValue "Link to this definition")  
Returns the final value of the signal segment.

Returns:  the final value

Return type:  float

GetFirstValue()[¶](#ApiClient.IdleSegment.GetFirstValue "Link to this definition")  
Returns the first value of the segment.

Returns:  the first value or NaN

Return type:  float

GetStopTrigger()[¶](#ApiClient.IdleSegment.GetStopTrigger "Link to this definition")  
Returns the stop trigger of the segment

Returns:  stop trigger

Return type:  str

GetTimeout()[¶](#ApiClient.IdleSegment.GetTimeout "Link to this definition")  
Returns the timeout of the segment

Returns:  timeout

Return type:  float

GetType()[¶](#ApiClient.IdleSegment.GetType "Link to this definition")  
Returns the type of the segment. (e.g. “Constant”)

Returns:  The type

Return type:  str

GetValueAt(*timestamp*)[¶](#ApiClient.IdleSegment.GetValueAt "Link to this definition")  
Returns the value at the given timestamp.

Parameters:  **timestamp** (*float*) – The timestamp

Returns:  the value or NaN

Return type:  float

RemoveStopTrigger()[¶](#ApiClient.IdleSegment.RemoveStopTrigger "Link to this definition")  
Removes the stop trigger of the segment

RemoveTimeout()[¶](#ApiClient.IdleSegment.RemoveTimeout "Link to this definition")  
Removes the timeout of the segment

SetComment(*comment*)[¶](#ApiClient.IdleSegment.SetComment "Link to this definition")  
Sets the comment of the segment.

Parameters:  **comment** (*str*) – The comment

SetDuration(*duration*)[¶](#ApiClient.IdleSegment.SetDuration "Link to this definition")  
Sets the duration of the segment in seconds.If you want to set the duration value of the segment to an expression, use SetDurationExpression instead.

Parameters:  **duration** (*float*) – the segments duration

SetDurationExpression(*expression*)[¶](#ApiClient.IdleSegment.SetDurationExpression "Link to this definition")  
Sets the duration value as an expression. The expression needs to be conform to the ASAM XIL GES syntax for ConstSymbol expressions.

Parameters:  **expression** (*str*) – the duration expression

SetStopTrigger(*stopTrigger*)[¶](#ApiClient.IdleSegment.SetStopTrigger "Link to this definition")  
Sets the stop trigger of the segment

Parameters:  **stopTrigger** (*str*) – The stop trigger

SetTimeout(*timeout*)[¶](#ApiClient.IdleSegment.SetTimeout "Link to this definition")  
Sets the timeout of the segment

Parameters:  **timeout** (*float*) – The timeout

## LoopSegment[¶](#loopsegment "Link to this heading")

*class* LoopSegment[¶](#ApiClient.LoopSegment "Link to this definition")  
Base class

[`SignalSegment`](#ApiClient.SignalSegment "ApiClient.SignalSegment")

Returned by

- [`SignalApi.CreateLoopSegment`](#ApiClient.SignalApi.CreateLoopSegment "ApiClient.SignalApi.CreateLoopSegment")

AppendSegment(*signalSegment*)[¶](#ApiClient.LoopSegment.AppendSegment "Link to this definition")  
Appends a segment to the LoopSegment

Parameters:  **signalSegment** ([`SignalSegment`](#ApiClient.SignalSegment "ApiClient.SignalSegment")) – The signalSegment

Clone()[¶](#ApiClient.LoopSegment.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`LoopSegment`](#ApiClient.LoopSegment "ApiClient.LoopSegment")

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

Return type:  list[[`SignalSegment`](#ApiClient.SignalSegment "ApiClient.SignalSegment")]

GetType()[¶](#ApiClient.LoopSegment.GetType "Link to this definition")  
Returns the type of the segment. (e.g. “Constant”)

Returns:  The type

Return type:  str

GetValueAt(*timestamp*)[¶](#ApiClient.LoopSegment.GetValueAt "Link to this definition")  
Returns the value at the given timestamp.

Parameters:  **timestamp** (*float*) – The timestamp

Returns:  the value or NaN

Return type:  float

RemoveSegment(*signalSegment*)[¶](#ApiClient.LoopSegment.RemoveSegment "Link to this definition")  
Removes a segment of the LoopSegment

Parameters:  **signalSegment** ([`SignalSegment`](#ApiClient.SignalSegment "ApiClient.SignalSegment")) – The signalSegment to be removed

SetComment(*comment*)[¶](#ApiClient.LoopSegment.SetComment "Link to this definition")  
Sets the comment of the signal description

Parameters:  **comment** (*str*) – Signal description comment

SetDuration(*duration*)[¶](#ApiClient.LoopSegment.SetDuration "Link to this definition")  
Sets the duration of the segment in seconds.If you want to set the duration value of the segment to an expression, use SetDurationExpression instead.

Parameters:  **duration** (*float*) – the segments duration

SetDurationExpression(*expression*)[¶](#ApiClient.LoopSegment.SetDurationExpression "Link to this definition")  
Sets the duration value as an expression. The expression needs to be conform to the ASAM XIL GES syntax for ConstSymbol expressions.

Parameters:  **expression** (*str*) – the duration expression

SetLoopCount(*loopCount*)[¶](#ApiClient.LoopSegment.SetLoopCount "Link to this definition")  
Sets the No. of loops for the segment

Parameters:  **loopCount** (*int*) – No. of loops

## SignalSegment[¶](#signalsegment "Link to this heading")

*class* SignalSegment[¶](#ApiClient.SignalSegment "Link to this definition")  
Returned by

- [`LoopSegment.GetSignalSegments`](#ApiClient.LoopSegment.GetSignalSegments "ApiClient.LoopSegment.GetSignalSegments")

- [`OperationSegment.GetSignalSegments`](#ApiClient.OperationSegment.GetSignalSegments "ApiClient.OperationSegment.GetSignalSegments")

- [`SegmentSignalDescription.GetSegments`](#ApiClient.SegmentSignalDescription.GetSegments "ApiClient.SegmentSignalDescription.GetSegments")

Subclasses

- [`ConstantSegment`](#ApiClient.ConstantSegment "ApiClient.ConstantSegment")

- [`DataFileSegment`](#ApiClient.DataFileSegment "ApiClient.DataFileSegment")

- [`ExponentialSegment`](#ApiClient.ExponentialSegment "ApiClient.ExponentialSegment")

- [`IdleSegment`](#ApiClient.IdleSegment "ApiClient.IdleSegment")

- [`LoopSegment`](#ApiClient.LoopSegment "ApiClient.LoopSegment")

- [`NoiseSegment`](#ApiClient.NoiseSegment "ApiClient.NoiseSegment")

- [`OperationSegment`](#ApiClient.OperationSegment "ApiClient.OperationSegment")

- [`PulseSegment`](#ApiClient.PulseSegment "ApiClient.PulseSegment")

- [`RampSegment`](#ApiClient.RampSegment "ApiClient.RampSegment")

- [`RampSlopeSegment`](#ApiClient.RampSlopeSegment "ApiClient.RampSlopeSegment")

- [`SawSegment`](#ApiClient.SawSegment "ApiClient.SawSegment")

- [`SignalValueSegment`](#ApiClient.SignalValueSegment "ApiClient.SignalValueSegment")

- [`SineSegment`](#ApiClient.SineSegment "ApiClient.SineSegment")

Clone()[¶](#ApiClient.SignalSegment.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`SignalSegment`](#ApiClient.SignalSegment "ApiClient.SignalSegment")

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

GetValueAt(*timestamp*)[¶](#ApiClient.SignalSegment.GetValueAt "Link to this definition")  
Returns the value at the given timestamp.

Parameters:  **timestamp** (*float*) – The timestamp

Returns:  the value or NaN

Return type:  float

SetComment(*comment*)[¶](#ApiClient.SignalSegment.SetComment "Link to this definition")  
Sets the comment of the segment.

Parameters:  **comment** (*str*) – The comment

SetDuration(*duration*)[¶](#ApiClient.SignalSegment.SetDuration "Link to this definition")  
Sets the duration of the segment in seconds.If you want to set the duration value of the segment to an expression, use SetDurationExpression instead.

Parameters:  **duration** (*float*) – the segments duration

SetDurationExpression(*expression*)[¶](#ApiClient.SignalSegment.SetDurationExpression "Link to this definition")  
Sets the duration value as an expression. The expression needs to be conform to the ASAM XIL GES syntax for ConstSymbol expressions.

Parameters:  **expression** (*str*) – the duration expression

## RampSegment[¶](#rampsegment "Link to this heading")

*class* RampSegment[¶](#ApiClient.RampSegment "Link to this definition")  
Base class

[`SignalSegment`](#ApiClient.SignalSegment "ApiClient.SignalSegment")

Returned by

- [`SignalApi.CreateRampSegment`](#ApiClient.SignalApi.CreateRampSegment "ApiClient.SignalApi.CreateRampSegment")

Clone()[¶](#ApiClient.RampSegment.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`RampSegment`](#ApiClient.RampSegment "ApiClient.RampSegment")

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

Return type:  [`SymbolType`](#ApiClient.SymbolType "ApiClient.SymbolType")

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

Return type:  [`SymbolType`](#ApiClient.SymbolType "ApiClient.SymbolType")

Returns:  the stop value symbol

GetType()[¶](#ApiClient.RampSegment.GetType "Link to this definition")  
Returns the type of the segment. (e.g. “Constant”)

Returns:  The type

Return type:  str

GetValueAt(*timestamp*)[¶](#ApiClient.RampSegment.GetValueAt "Link to this definition")  
Returns the value at the given timestamp.

Parameters:  **timestamp** (*float*) – The timestamp

Returns:  the value or NaN

Return type:  float

SetComment(*comment*)[¶](#ApiClient.RampSegment.SetComment "Link to this definition")  
Sets the comment of the segment.

Parameters:  **comment** (*str*) – The comment

SetDuration(*duration*)[¶](#ApiClient.RampSegment.SetDuration "Link to this definition")  
Sets the duration of the segment in seconds.If you want to set the duration value of the segment to an expression, use SetDurationExpression instead.

Parameters:  **duration** (*float*) – the segments duration

SetDurationExpression(*expression*)[¶](#ApiClient.RampSegment.SetDurationExpression "Link to this definition")  
Sets the duration value as an expression. The expression needs to be conform to the ASAM XIL GES syntax for ConstSymbol expressions.

Parameters:  **expression** (*str*) – the duration expression

SetStart(*start*)[¶](#ApiClient.RampSegment.SetStart "Link to this definition")  
Sets the start value of the segment.

Parameters:  **start** (*float*) – the start value

SetStartExpression(*expression*)[¶](#ApiClient.RampSegment.SetStartExpression "Link to this definition")  
Sets the start value of the segment to the given expression. The expression needs to conform to the ASAM XIL GES syntax for ConstSymbol expressions.

Parameters:  **expression** (*str*) – the expression

SetStartSymbol(*value*)[¶](#ApiClient.RampSegment.SetStartSymbol "Link to this definition")  
Sets a SymbolType object as start value of the segment. If you want to set the start value of the segment to an expression, use SetStartExpression instead.

Parameters:  **value** ([`SymbolType`](#ApiClient.SymbolType "ApiClient.SymbolType")) – the start value symbol

SetStop(*stop*)[¶](#ApiClient.RampSegment.SetStop "Link to this definition")  
Set the stop value of the segment.

Parameters:  **stop** (*float*) – the stop value

SetStopExpression(*expression*)[¶](#ApiClient.RampSegment.SetStopExpression "Link to this definition")  
Sets the stop value to the given expression. The expression has to be conform to the ASAM XIL GES syntax for ConstSymbol expressions.

Parameters:  **expression** (*str*) – the expression

SetStopSymbol(*value*)[¶](#ApiClient.RampSegment.SetStopSymbol "Link to this definition")  
Sets a SymbolType object as stop value of the segment. If you want to set the stop value of the segment to an expression, use SetStopExpression instead.

Parameters:  **value** ([`SymbolType`](#ApiClient.SymbolType "ApiClient.SymbolType")) – the stop value symbol

GetStartValue()[¶](#ApiClient.RampSegment.GetStartValue "Link to this definition")  
Use GetStart instead

Return type:  float

Returns:  the start value

Deprecated since version 2022.1: Use ‘GetStart’ instead

GetStopValue()[¶](#ApiClient.RampSegment.GetStopValue "Link to this definition")  
Use GetStop instead.

Return type:  float

Returns:  the stop value

Deprecated since version 2022.1: Use ‘GetStop’ instead

SetStartValue(*startValue*)[¶](#ApiClient.RampSegment.SetStartValue "Link to this definition")  
Use SetStart instead

Parameters:  **startValue** (*float*) – the start value

Deprecated since version 2022.1: Use ‘SetStart’ instead

SetStopValue(*stopValue*)[¶](#ApiClient.RampSegment.SetStopValue "Link to this definition")  
Use SetStop instead

Parameters:  **stopValue** (*float*) – the stop value

Deprecated since version 2022.1: Use ‘SetStop’ instead

## RampSlopeSegment[¶](#rampslopesegment "Link to this heading")

*class* RampSlopeSegment[¶](#ApiClient.RampSlopeSegment "Link to this definition")  
Base class

[`SignalSegment`](#ApiClient.SignalSegment "ApiClient.SignalSegment")

Returned by

- [`SignalApi.CreateRampSlopeSegment`](#ApiClient.SignalApi.CreateRampSlopeSegment "ApiClient.SignalApi.CreateRampSlopeSegment")

Clone()[¶](#ApiClient.RampSlopeSegment.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`RampSlopeSegment`](#ApiClient.RampSlopeSegment "ApiClient.RampSlopeSegment")

GetComment()[¶](#ApiClient.RampSlopeSegment.GetComment "Link to this definition")  
Returns the comment of the segment.

Returns:  The comment

Return type:  str

GetDuration()[¶](#ApiClient.RampSlopeSegment.GetDuration "Link to this definition")  
Returns the current duration of the signal segment.

Returns:  The duration

Return type:  float

GetDurationExpression()[¶](#ApiClient.RampSlopeSegment.GetDurationExpression "Link to this definition")  
Returns the duration expression of the segment that is conform to the ASAM XIL GES syntax for ConstSymbol expressions.

Return type:  str

Returns:  the duration expression

GetFinalValue()[¶](#ApiClient.RampSlopeSegment.GetFinalValue "Link to this definition")  
Returns the final value of the signal segment.

Returns:  the final value

Return type:  float

GetFirstValue()[¶](#ApiClient.RampSlopeSegment.GetFirstValue "Link to this definition")  
Returns the first value of the segment.

Returns:  the first value or NaN

Return type:  float

GetOffset()[¶](#ApiClient.RampSlopeSegment.GetOffset "Link to this definition")  
Returns the offset value of the segment.

Return type:  float

Returns:  the offset value

GetOffsetExpression()[¶](#ApiClient.RampSlopeSegment.GetOffsetExpression "Link to this definition")  
Returns the offset value expression. The expression conforms to the ASAM XIL GES syntax for ConstSymbol expressions.

Return type:  str

Returns:  the offset value expression

GetOffsetSymbol()[¶](#ApiClient.RampSlopeSegment.GetOffsetSymbol "Link to this definition")  
Returns the SymbolType object of the segment offset value.

Return type:  [`SymbolType`](#ApiClient.SymbolType "ApiClient.SymbolType")

Returns:  the offset value symbol

GetSlope()[¶](#ApiClient.RampSlopeSegment.GetSlope "Link to this definition")  
Returns the slope value of the segment.

Return type:  float

Returns:  the slope value

GetSlopeExpression()[¶](#ApiClient.RampSlopeSegment.GetSlopeExpression "Link to this definition")  
Returns the slope value expression. The expression conforms to the ASAM XIL GES syntax for ConstSymbol expressions.

Return type:  str

Returns:  the slope value expression

GetSlopeSymbol()[¶](#ApiClient.RampSlopeSegment.GetSlopeSymbol "Link to this definition")  
Returns the SymbolType object of the segment slope value.

Return type:  [`SymbolType`](#ApiClient.SymbolType "ApiClient.SymbolType")

Returns:  the slope value symbol

GetStopTrigger()[¶](#ApiClient.RampSlopeSegment.GetStopTrigger "Link to this definition")  
Returns the stop trigger of the segment

Returns:  stop trigger

Return type:  str

GetTimeout()[¶](#ApiClient.RampSlopeSegment.GetTimeout "Link to this definition")  
Returns the timeout of the segment

Returns:  timeout

Return type:  float

GetType()[¶](#ApiClient.RampSlopeSegment.GetType "Link to this definition")  
Returns the type of the segment. (e.g. “Constant”)

Returns:  The type

Return type:  str

GetValueAt(*timestamp*)[¶](#ApiClient.RampSlopeSegment.GetValueAt "Link to this definition")  
Returns the value at the given timestamp.

Parameters:  **timestamp** (*float*) – The timestamp

Returns:  the value or NaN

Return type:  float

RemoveStopTrigger()[¶](#ApiClient.RampSlopeSegment.RemoveStopTrigger "Link to this definition")  
Removes the stop trigger of the segment

RemoveTimeout()[¶](#ApiClient.RampSlopeSegment.RemoveTimeout "Link to this definition")  
Removes the timeout of the segment

SetComment(*comment*)[¶](#ApiClient.RampSlopeSegment.SetComment "Link to this definition")  
Sets the comment of the segment.

Parameters:  **comment** (*str*) – The comment

SetDuration(*duration*)[¶](#ApiClient.RampSlopeSegment.SetDuration "Link to this definition")  
Sets the duration of the segment in seconds.If you want to set the duration value of the segment to an expression, use SetDurationExpression instead.

Parameters:  **duration** (*float*) – the segments duration

SetDurationExpression(*expression*)[¶](#ApiClient.RampSlopeSegment.SetDurationExpression "Link to this definition")  
Sets the duration value as an expression. The expression needs to be conform to the ASAM XIL GES syntax for ConstSymbol expressions.

Parameters:  **expression** (*str*) – the duration expression

SetOffset(*offset*)[¶](#ApiClient.RampSlopeSegment.SetOffset "Link to this definition")  
Sets the offset value of the segment.

Parameters:  **offset** (*float*) – the offset value

SetOffsetExpression(*expression*)[¶](#ApiClient.RampSlopeSegment.SetOffsetExpression "Link to this definition")  
Sets the offset value expression. The expression has to conform to the ASAM XIL GES syntax for ConstSymbol expressions.

Parameters:  **expression** (*str*) – the expression

SetOffsetSymbol(*value*)[¶](#ApiClient.RampSlopeSegment.SetOffsetSymbol "Link to this definition")  
Sets a SymbolType object as offset value of the segment. If you want to set the offset value of the segment to an expression, use SetOffsetExpression instead.

Parameters:  **value** ([`SymbolType`](#ApiClient.SymbolType "ApiClient.SymbolType")) – the offset value symbol

SetSlope(*slope*)[¶](#ApiClient.RampSlopeSegment.SetSlope "Link to this definition")  
Sets the slope value of the segment.

Parameters:  **slope** (*float*) – the slope value

SetSlopeExpression(*expression*)[¶](#ApiClient.RampSlopeSegment.SetSlopeExpression "Link to this definition")  
Sets the slope value expression. The expression has to conform to the ASAM XIL GES syntax for ConstSymbol expressions.

Parameters:  **expression** (*str*) – the expression

SetSlopeSymbol(*value*)[¶](#ApiClient.RampSlopeSegment.SetSlopeSymbol "Link to this definition")  
Sets a SymbolType object as slope value of the segment. If you want to set the slope value of the segment to an expression, use SetSlopeExpression instead.

Parameters:  **value** ([`SymbolType`](#ApiClient.SymbolType "ApiClient.SymbolType")) – the slope value symbol

SetStopTrigger(*stopTrigger*)[¶](#ApiClient.RampSlopeSegment.SetStopTrigger "Link to this definition")  
Sets the stop trigger of the segment

Parameters:  **stopTrigger** (*str*) – The stop trigger

SetTimeout(*timeout*)[¶](#ApiClient.RampSlopeSegment.SetTimeout "Link to this definition")  
Sets the timeout of the segment

Parameters:  **timeout** (*float*) – The timeout

## NoiseSegment[¶](#noisesegment "Link to this heading")

*class* NoiseSegment[¶](#ApiClient.NoiseSegment "Link to this definition")  
Base class

[`SignalSegment`](#ApiClient.SignalSegment "ApiClient.SignalSegment")

Returned by

- [`SignalApi.CreateNoiseSegment`](#ApiClient.SignalApi.CreateNoiseSegment "ApiClient.SignalApi.CreateNoiseSegment")

Clone()[¶](#ApiClient.NoiseSegment.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`NoiseSegment`](#ApiClient.NoiseSegment "ApiClient.NoiseSegment")

GetComment()[¶](#ApiClient.NoiseSegment.GetComment "Link to this definition")  
Returns the comment of the segment.

Returns:  The comment

Return type:  str

GetDuration()[¶](#ApiClient.NoiseSegment.GetDuration "Link to this definition")  
Returns the current duration of the signal segment.

Returns:  The duration

Return type:  float

GetDurationExpression()[¶](#ApiClient.NoiseSegment.GetDurationExpression "Link to this definition")  
Returns the duration expression of the segment that is conform to the ASAM XIL GES syntax for ConstSymbol expressions.

Return type:  str

Returns:  the duration expression

GetFinalValue()[¶](#ApiClient.NoiseSegment.GetFinalValue "Link to this definition")  
Returns the final value of the signal segment.

Returns:  the final value

Return type:  float

GetFirstValue()[¶](#ApiClient.NoiseSegment.GetFirstValue "Link to this definition")  
Returns the first value of the segment.

Returns:  the first value or NaN

Return type:  float

GetMean()[¶](#ApiClient.NoiseSegment.GetMean "Link to this definition")  
Returns the mean value of the segment.

Return type:  float

Returns:  the mean value

GetMeanExpression()[¶](#ApiClient.NoiseSegment.GetMeanExpression "Link to this definition")  
Returns the mean value expression. The expression conforms to the ASAM XIL GES syntax for ConstSymbol expressions.

Return type:  str

Returns:  the mean value expression

GetMeanSymbol()[¶](#ApiClient.NoiseSegment.GetMeanSymbol "Link to this definition")  
Returns the SymbolType object of the segment mean value.

Return type:  [`SymbolType`](#ApiClient.SymbolType "ApiClient.SymbolType")

Returns:  the mean value symbol

GetSeed()[¶](#ApiClient.NoiseSegment.GetSeed "Link to this definition")  
Returns the seed value of the segment.

Return type:  float

Returns:  the seed value

GetSeedExpression()[¶](#ApiClient.NoiseSegment.GetSeedExpression "Link to this definition")  
Returns the seed value expression. The expression conforms to the ASAM XIL GES syntax for ConstSymbol expressions.

Return type:  str

Returns:  the seed value expression

GetSigma()[¶](#ApiClient.NoiseSegment.GetSigma "Link to this definition")  
Returns the sigma value of the segment.

Return type:  float

Returns:  the sigma value

GetSigmaExpression()[¶](#ApiClient.NoiseSegment.GetSigmaExpression "Link to this definition")  
Returns the sigma value expression. The expression conforms to the ASAM XIL GES syntax for ConstSymbol expressions.

Return type:  str

Returns:  the sigma value expression

GetSigmaSymbol()[¶](#ApiClient.NoiseSegment.GetSigmaSymbol "Link to this definition")  
Returns the SymbolType object of the segment sigma value.

Return type:  [`SymbolType`](#ApiClient.SymbolType "ApiClient.SymbolType")

Returns:  the sigma value symbol

GetStopTrigger()[¶](#ApiClient.NoiseSegment.GetStopTrigger "Link to this definition")  
Returns the stop trigger of the segment

Returns:  stop trigger

Return type:  str

GetTimeout()[¶](#ApiClient.NoiseSegment.GetTimeout "Link to this definition")  
Returns the timeout of the segment

Returns:  timeout

Return type:  float

GetType()[¶](#ApiClient.NoiseSegment.GetType "Link to this definition")  
Returns the type of the segment. (e.g. “Constant”)

Returns:  The type

Return type:  str

GetValueAt(*timestamp*)[¶](#ApiClient.NoiseSegment.GetValueAt "Link to this definition")  
Returns the value at the given timestamp.

Parameters:  **timestamp** (*float*) – The timestamp

Returns:  the value or NaN

Return type:  float

RemoveStopTrigger()[¶](#ApiClient.NoiseSegment.RemoveStopTrigger "Link to this definition")  
Removes the stop trigger of the segment

RemoveTimeout()[¶](#ApiClient.NoiseSegment.RemoveTimeout "Link to this definition")  
Removes the timeout of the segment

SetComment(*comment*)[¶](#ApiClient.NoiseSegment.SetComment "Link to this definition")  
Sets the comment of the segment.

Parameters:  **comment** (*str*) – The comment

SetDuration(*duration*)[¶](#ApiClient.NoiseSegment.SetDuration "Link to this definition")  
Sets the duration of the segment in seconds.If you want to set the duration value of the segment to an expression, use SetDurationExpression instead.

Parameters:  **duration** (*float*) – the segments duration

SetDurationExpression(*expression*)[¶](#ApiClient.NoiseSegment.SetDurationExpression "Link to this definition")  
Sets the duration value as an expression. The expression needs to be conform to the ASAM XIL GES syntax for ConstSymbol expressions.

Parameters:  **expression** (*str*) – the duration expression

SetMean(*mean*)[¶](#ApiClient.NoiseSegment.SetMean "Link to this definition")  
Sets the mean value of the segment.

Parameters:  **mean** (*float*) – the mean value

SetMeanExpression(*expression*)[¶](#ApiClient.NoiseSegment.SetMeanExpression "Link to this definition")  
Sets the mean value expression. The expression has to conform to the ASAM XIL GES syntax for ConstSymbol expressions.

Parameters:  **expression** (*str*) – the expression

SetMeanSymbol(*value*)[¶](#ApiClient.NoiseSegment.SetMeanSymbol "Link to this definition")  
Sets a SymbolType object as mean value of the segment. If you want to set the mean value of the segment to an expression, use SetMeanExpression instead.

Parameters:  **value** ([`SymbolType`](#ApiClient.SymbolType "ApiClient.SymbolType")) – the mean value symbol

SetSeed(*seed*)[¶](#ApiClient.NoiseSegment.SetSeed "Link to this definition")  
Sets the seed value of the segment.

Parameters:  **seed** (*float*) – the seed value

SetSeedExpression(*expression*)[¶](#ApiClient.NoiseSegment.SetSeedExpression "Link to this definition")  
Sets the mean value expression. The expression has to conform to the ASAM XIL GES syntax for ConstSymbol expressions.

Parameters:  **expression** (*str*) – the mean expression

SetSigma(*sigma*)[¶](#ApiClient.NoiseSegment.SetSigma "Link to this definition")  
Sets the sigma value of the segment.

Parameters:  **sigma** (*float*) – the sigma value

SetSigmaExpression(*expression*)[¶](#ApiClient.NoiseSegment.SetSigmaExpression "Link to this definition")  
Sets the sigma value expression. The expression has to conform to the ASAM XIL GES syntax for ConstSymbol expressions.

Parameters:  **expression** (*str*) – the expression

SetSigmaSymbol(*value*)[¶](#ApiClient.NoiseSegment.SetSigmaSymbol "Link to this definition")  
Sets a SymbolType object as sigma value of the segment. If you want to set the sigma value of the segment to an expression, use SetSigmaExpression instead.

Parameters:  **value** ([`SymbolType`](#ApiClient.SymbolType "ApiClient.SymbolType")) – the sigma value symbol

SetStopTrigger(*stopTrigger*)[¶](#ApiClient.NoiseSegment.SetStopTrigger "Link to this definition")  
Sets the stop trigger of the segment

Parameters:  **stopTrigger** (*str*) – The stop trigger

SetTimeout(*timeout*)[¶](#ApiClient.NoiseSegment.SetTimeout "Link to this definition")  
Sets the timeout of the segment

Parameters:  **timeout** (*float*) – The timeout

## SineSegment[¶](#sinesegment "Link to this heading")

*class* SineSegment[¶](#ApiClient.SineSegment "Link to this definition")  
Base class

[`SignalSegment`](#ApiClient.SignalSegment "ApiClient.SignalSegment")

Returned by

- [`SignalApi.CreateSineSegment`](#ApiClient.SignalApi.CreateSineSegment "ApiClient.SignalApi.CreateSineSegment")

Clone()[¶](#ApiClient.SineSegment.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`SineSegment`](#ApiClient.SineSegment "ApiClient.SineSegment")

GetAmplitude()[¶](#ApiClient.SineSegment.GetAmplitude "Link to this definition")  
Returns the amplitude value of the segment.

Return type:  float

Returns:  the amplitude value

GetAmplitudeExpression()[¶](#ApiClient.SineSegment.GetAmplitudeExpression "Link to this definition")  
Returns the amplitude value expression. The expression conforms to the ASAM XIL GES syntax for ConstSymbol expressions.

Return type:  str

Returns:  the amplitude expression

GetAmplitudeSymbol()[¶](#ApiClient.SineSegment.GetAmplitudeSymbol "Link to this definition")  
Returns the SymbolType object of the segment amplitude value.

Return type:  [`SymbolType`](#ApiClient.SymbolType "ApiClient.SymbolType")

Returns:  the amplitude value symbol

GetComment()[¶](#ApiClient.SineSegment.GetComment "Link to this definition")  
Returns the comment of the segment.

Returns:  The comment

Return type:  str

GetDuration()[¶](#ApiClient.SineSegment.GetDuration "Link to this definition")  
Returns the current duration of the signal segment.

Returns:  The duration

Return type:  float

GetDurationExpression()[¶](#ApiClient.SineSegment.GetDurationExpression "Link to this definition")  
Returns the duration expression of the segment that is conform to the ASAM XIL GES syntax for ConstSymbol expressions.

Return type:  str

Returns:  the duration expression

GetFinalValue()[¶](#ApiClient.SineSegment.GetFinalValue "Link to this definition")  
Returns the final value of the signal segment.

Returns:  the final value

Return type:  float

GetFirstValue()[¶](#ApiClient.SineSegment.GetFirstValue "Link to this definition")  
Returns the first value of the segment.

Returns:  the first value or NaN

Return type:  float

GetOffset()[¶](#ApiClient.SineSegment.GetOffset "Link to this definition")  
Returns the offset value of the segment.

Return type:  float

Returns:  the offset value

GetOffsetExpression()[¶](#ApiClient.SineSegment.GetOffsetExpression "Link to this definition")  
Returns the offset value expression. The expression conforms to the ASAM XIL GES syntax for ConstSymbol expressions.

Return type:  str

Returns:  the offset value expression

GetOffsetSymbol()[¶](#ApiClient.SineSegment.GetOffsetSymbol "Link to this definition")  
Returns the SymbolType object of the segment offset value.

Return type:  [`SymbolType`](#ApiClient.SymbolType "ApiClient.SymbolType")

Returns:  the offset value symbol

GetPeriod()[¶](#ApiClient.SineSegment.GetPeriod "Link to this definition")  
Returns the period value of the segment.

Return type:  float

Returns:  the period value

GetPeriodExpression()[¶](#ApiClient.SineSegment.GetPeriodExpression "Link to this definition")  
Returns the period value expression. The expression conforms to the ASAM XIL GES syntax for ConstSymbol expressions.

Return type:  str

Returns:  the period value expression

GetPeriodSymbol()[¶](#ApiClient.SineSegment.GetPeriodSymbol "Link to this definition")  
Returns the SymbolType object of the segment period value.

Return type:  [`SymbolType`](#ApiClient.SymbolType "ApiClient.SymbolType")

Returns:  the period value symbol

GetPhase()[¶](#ApiClient.SineSegment.GetPhase "Link to this definition")  
Returns the phase value of the segment.

Return type:  float

Returns:  the phase value

GetPhaseExpression()[¶](#ApiClient.SineSegment.GetPhaseExpression "Link to this definition")  
Returns the phase value expression. The expression conforms to the ASAM XIL GES syntax for ConstSymbol expressions.

Return type:  str

Returns:  the phase value expression

GetPhaseSymbol()[¶](#ApiClient.SineSegment.GetPhaseSymbol "Link to this definition")  
Returns the SymbolType object of the segment phase value.

Return type:  [`SymbolType`](#ApiClient.SymbolType "ApiClient.SymbolType")

Returns:  the phase value symbol

GetStopTrigger()[¶](#ApiClient.SineSegment.GetStopTrigger "Link to this definition")  
Returns the stop trigger of the segment

Returns:  stop trigger

Return type:  str

GetTimeout()[¶](#ApiClient.SineSegment.GetTimeout "Link to this definition")  
Returns the timeout of the segment

Returns:  timeout

Return type:  float

GetType()[¶](#ApiClient.SineSegment.GetType "Link to this definition")  
Returns the type of the segment. (e.g. “Constant”)

Returns:  The type

Return type:  str

GetValueAt(*timestamp*)[¶](#ApiClient.SineSegment.GetValueAt "Link to this definition")  
Returns the value at the given timestamp.

Parameters:  **timestamp** (*float*) – The timestamp

Returns:  the value or NaN

Return type:  float

RemoveStopTrigger()[¶](#ApiClient.SineSegment.RemoveStopTrigger "Link to this definition")  
Removes the stop trigger of the segment

RemoveTimeout()[¶](#ApiClient.SineSegment.RemoveTimeout "Link to this definition")  
Removes the timeout of the segment

SetAmplitude(*amplitude*)[¶](#ApiClient.SineSegment.SetAmplitude "Link to this definition")  
Sets the amplitude value of the segment.

Parameters:  **amplitude** (*float*) – the amplitude value

SetAmplitudeExpression(*expression*)[¶](#ApiClient.SineSegment.SetAmplitudeExpression "Link to this definition")  
Sets the amplitude expression of the segment. The expression has to conform to the ASAM XIL GES syntax for ConstSymbol expressions.

Parameters:  **expression** (*str*) – the amplitude expression

SetAmplitudeSymbol(*value*)[¶](#ApiClient.SineSegment.SetAmplitudeSymbol "Link to this definition")  
Sets a SymbolType object as amplitude value of the segment. If you want to set the amplitude value of the segment to an expression, use SetAmplitudeExpression instead.

Parameters:  **value** ([`SymbolType`](#ApiClient.SymbolType "ApiClient.SymbolType")) – the amplitude value symbol

SetComment(*comment*)[¶](#ApiClient.SineSegment.SetComment "Link to this definition")  
Sets the comment of the segment.

Parameters:  **comment** (*str*) – The comment

SetDuration(*duration*)[¶](#ApiClient.SineSegment.SetDuration "Link to this definition")  
Sets the duration of the segment in seconds.If you want to set the duration value of the segment to an expression, use SetDurationExpression instead.

Parameters:  **duration** (*float*) – the segments duration

SetDurationExpression(*expression*)[¶](#ApiClient.SineSegment.SetDurationExpression "Link to this definition")  
Sets the duration value as an expression. The expression needs to be conform to the ASAM XIL GES syntax for ConstSymbol expressions.

Parameters:  **expression** (*str*) – the duration expression

SetOffset(*offset*)[¶](#ApiClient.SineSegment.SetOffset "Link to this definition")  
Sets the offset value of the segment.

Parameters:  **offset** (*float*) – the offset value

SetOffsetExpression(*expression*)[¶](#ApiClient.SineSegment.SetOffsetExpression "Link to this definition")  
Sets the offset value expression. The expression has to conform to the ASAM XIL GES syntax for ConstSymbol expressions.

Parameters:  **expression** (*str*) – the expression

SetOffsetSymbol(*value*)[¶](#ApiClient.SineSegment.SetOffsetSymbol "Link to this definition")  
Sets a SymbolType object as offset value of the segment. If you want to set the offset value of the segment to an expression, use SetOffsetExpression instead.

Parameters:  **value** ([`SymbolType`](#ApiClient.SymbolType "ApiClient.SymbolType")) – the offset value symbol

SetPeriod(*period*)[¶](#ApiClient.SineSegment.SetPeriod "Link to this definition")  
Sets the period value of the segment.

Parameters:  **period** (*float*) – the period value

SetPeriodExpression(*expression*)[¶](#ApiClient.SineSegment.SetPeriodExpression "Link to this definition")  
Sets the period value expression. The expression has to conform to the ASAM XIL GES syntax for ConstSymbol expressions.

Parameters:  **expression** (*str*) – the period expression

SetPeriodSymbol(*value*)[¶](#ApiClient.SineSegment.SetPeriodSymbol "Link to this definition")  
Sets a SymbolType object as period value of the segment. If you want to set the period value of the segment to an expression, use SetPeriodExpression instead.

Parameters:  **value** ([`SymbolType`](#ApiClient.SymbolType "ApiClient.SymbolType")) – the period value symbol

SetPhase(*phase*)[¶](#ApiClient.SineSegment.SetPhase "Link to this definition")  
Sets the phase value of the segment.

Parameters:  **phase** (*float*) – the phase value

SetPhaseExpression(*expression*)[¶](#ApiClient.SineSegment.SetPhaseExpression "Link to this definition")  
Sets the phase value expression. The expression has to conform to the ASAM XIL GES syntax for ConstSymbol expressions.

Parameters:  **expression** (*str*) – the phase expression

SetPhaseSymbol(*value*)[¶](#ApiClient.SineSegment.SetPhaseSymbol "Link to this definition")  
Sets a SymbolType object as phase value of the segment. If you want to set the phase value of the segment to an expression, use SetPhaseExpression instead.

Parameters:  **value** ([`SymbolType`](#ApiClient.SymbolType "ApiClient.SymbolType")) – the phase value symbol

SetStopTrigger(*stopTrigger*)[¶](#ApiClient.SineSegment.SetStopTrigger "Link to this definition")  
Sets the stop trigger of the segment

Parameters:  **stopTrigger** (*str*) – The stop trigger

SetTimeout(*timeout*)[¶](#ApiClient.SineSegment.SetTimeout "Link to this definition")  
Sets the timeout of the segment

Parameters:  **timeout** (*float*) – The timeout

## SawSegment[¶](#sawsegment "Link to this heading")

*class* SawSegment[¶](#ApiClient.SawSegment "Link to this definition")  
Base class

[`SignalSegment`](#ApiClient.SignalSegment "ApiClient.SignalSegment")

Returned by

- [`SignalApi.CreateSawSegment`](#ApiClient.SignalApi.CreateSawSegment "ApiClient.SignalApi.CreateSawSegment")

Clone()[¶](#ApiClient.SawSegment.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`SawSegment`](#ApiClient.SawSegment "ApiClient.SawSegment")

GetAmplitude()[¶](#ApiClient.SawSegment.GetAmplitude "Link to this definition")  
Returns the amplitude value of the segment.

Return type:  float

Returns:  the amplitude value

GetAmplitudeExpression()[¶](#ApiClient.SawSegment.GetAmplitudeExpression "Link to this definition")  
Returns the amplitude value expression. The expression conforms to the ASAM XIL GES syntax for ConstSymbol expressions.

Return type:  str

Returns:  the amplitude expression

GetAmplitudeSymbol()[¶](#ApiClient.SawSegment.GetAmplitudeSymbol "Link to this definition")  
Returns the SymbolType object of the segment amplitude value.

Return type:  [`SymbolType`](#ApiClient.SymbolType "ApiClient.SymbolType")

Returns:  the amplitude value symbol

GetComment()[¶](#ApiClient.SawSegment.GetComment "Link to this definition")  
Returns the comment of the segment.

Returns:  The comment

Return type:  str

GetDuration()[¶](#ApiClient.SawSegment.GetDuration "Link to this definition")  
Returns the current duration of the signal segment.

Returns:  The duration

Return type:  float

GetDurationExpression()[¶](#ApiClient.SawSegment.GetDurationExpression "Link to this definition")  
Returns the duration expression of the segment that is conform to the ASAM XIL GES syntax for ConstSymbol expressions.

Return type:  str

Returns:  the duration expression

GetDutyCycle()[¶](#ApiClient.SawSegment.GetDutyCycle "Link to this definition")  
Returns the dutyCycle value of the segment.

Return type:  float

Returns:  the dutyCycle value

GetDutyCycleExpression()[¶](#ApiClient.SawSegment.GetDutyCycleExpression "Link to this definition")  
Returns the dutyCycle value expression. The expression conforms to the ASAM XIL GES syntax for ConstSymbol expressions.

Return type:  str

Returns:  the dutyCycle value expression

GetDutyCycleSymbol()[¶](#ApiClient.SawSegment.GetDutyCycleSymbol "Link to this definition")  
Returns the SymbolType object of the segment dutyCycle value.

Return type:  [`SymbolType`](#ApiClient.SymbolType "ApiClient.SymbolType")

Returns:  the dutyCycle value symbol

GetFinalValue()[¶](#ApiClient.SawSegment.GetFinalValue "Link to this definition")  
Returns the final value of the signal segment.

Returns:  the final value

Return type:  float

GetFirstValue()[¶](#ApiClient.SawSegment.GetFirstValue "Link to this definition")  
Returns the first value of the segment.

Returns:  the first value or NaN

Return type:  float

GetOffset()[¶](#ApiClient.SawSegment.GetOffset "Link to this definition")  
Returns the offset value of the segment.

Return type:  float

Returns:  the offset value

GetOffsetExpression()[¶](#ApiClient.SawSegment.GetOffsetExpression "Link to this definition")  
Returns the offset value expression. The expression conforms to the ASAM XIL GES syntax for ConstSymbol expressions.

Return type:  str

Returns:  the offset value expression

GetOffsetSymbol()[¶](#ApiClient.SawSegment.GetOffsetSymbol "Link to this definition")  
Returns the SymbolType object of the segment offset value.

Return type:  [`SymbolType`](#ApiClient.SymbolType "ApiClient.SymbolType")

Returns:  the offset value symbol

GetPeriod()[¶](#ApiClient.SawSegment.GetPeriod "Link to this definition")  
Returns the period value of the segment.

Return type:  float

Returns:  the period value

GetPeriodExpression()[¶](#ApiClient.SawSegment.GetPeriodExpression "Link to this definition")  
Returns the period value expression. The expression conforms to the ASAM XIL GES syntax for ConstSymbol expressions.

Return type:  str

Returns:  the period value expression

GetPeriodSymbol()[¶](#ApiClient.SawSegment.GetPeriodSymbol "Link to this definition")  
Returns the SymbolType object of the segment period value.

Return type:  [`SymbolType`](#ApiClient.SymbolType "ApiClient.SymbolType")

Returns:  the period value symbol

GetPhase()[¶](#ApiClient.SawSegment.GetPhase "Link to this definition")  
Returns the phase value of the segment.

Return type:  float

Returns:  the phase value

GetPhaseExpression()[¶](#ApiClient.SawSegment.GetPhaseExpression "Link to this definition")  
Returns the phase value expression. The expression conforms to the ASAM XIL GES syntax for ConstSymbol expressions.

Return type:  str

Returns:  the phase value expression

GetPhaseSymbol()[¶](#ApiClient.SawSegment.GetPhaseSymbol "Link to this definition")  
Returns the SymbolType object of the segment phase value.

Return type:  [`SymbolType`](#ApiClient.SymbolType "ApiClient.SymbolType")

Returns:  the phase value symbol

GetStopTrigger()[¶](#ApiClient.SawSegment.GetStopTrigger "Link to this definition")  
Returns the stop trigger of the segment

Returns:  stop trigger

Return type:  str

GetTimeout()[¶](#ApiClient.SawSegment.GetTimeout "Link to this definition")  
Returns the timeout of the segment

Returns:  timeout

Return type:  float

GetType()[¶](#ApiClient.SawSegment.GetType "Link to this definition")  
Returns the type of the segment. (e.g. “Constant”)

Returns:  The type

Return type:  str

GetValueAt(*timestamp*)[¶](#ApiClient.SawSegment.GetValueAt "Link to this definition")  
Returns the value at the given timestamp.

Parameters:  **timestamp** (*float*) – The timestamp

Returns:  the value or NaN

Return type:  float

RemoveStopTrigger()[¶](#ApiClient.SawSegment.RemoveStopTrigger "Link to this definition")  
Removes the stop trigger of the segment

RemoveTimeout()[¶](#ApiClient.SawSegment.RemoveTimeout "Link to this definition")  
Removes the timeout of the segment

SetAmplitude(*amplitude*)[¶](#ApiClient.SawSegment.SetAmplitude "Link to this definition")  
Sets the amplitude value of the segment.

Parameters:  **amplitude** (*float*) – the amplitude value

SetAmplitudeExpression(*expression*)[¶](#ApiClient.SawSegment.SetAmplitudeExpression "Link to this definition")  
Sets the amplitude expression of the segment. The expression has to conform to the ASAM XIL GES syntax for ConstSymbol expressions.

Parameters:  **expression** (*str*) – the amplitude expression

SetAmplitudeSymbol(*value*)[¶](#ApiClient.SawSegment.SetAmplitudeSymbol "Link to this definition")  
Sets a SymbolType object as amplitude value of the segment. If you want to set the amplitude value of the segment to an expression, use SetAmplitudeExpression instead.

Parameters:  **value** ([`SymbolType`](#ApiClient.SymbolType "ApiClient.SymbolType")) – the amplitude value symbol

SetComment(*comment*)[¶](#ApiClient.SawSegment.SetComment "Link to this definition")  
Sets the comment of the segment.

Parameters:  **comment** (*str*) – The comment

SetDuration(*duration*)[¶](#ApiClient.SawSegment.SetDuration "Link to this definition")  
Sets the duration of the segment in seconds.If you want to set the duration value of the segment to an expression, use SetDurationExpression instead.

Parameters:  **duration** (*float*) – the segments duration

SetDurationExpression(*expression*)[¶](#ApiClient.SawSegment.SetDurationExpression "Link to this definition")  
Sets the duration value as an expression. The expression needs to be conform to the ASAM XIL GES syntax for ConstSymbol expressions.

Parameters:  **expression** (*str*) – the duration expression

SetDutyCycle(*dutyCycle*)[¶](#ApiClient.SawSegment.SetDutyCycle "Link to this definition")  
Sets the dutyCycle value of the segment.

Parameters:  **dutyCycle** (*float*) – the dutyCycle value

SetDutyCycleExpression(*expression*)[¶](#ApiClient.SawSegment.SetDutyCycleExpression "Link to this definition")  
Sets the dutyCycle value expression. The expression has to conform to the ASAM XIL GES syntax for ConstSymbol expressions.

Parameters:  **expression** (*str*) – the dutyCycle expression

SetDutyCycleSymbol(*value*)[¶](#ApiClient.SawSegment.SetDutyCycleSymbol "Link to this definition")  
Sets a SymbolType object as dutyCycle value of the segment. If you want to set the dutyCycle value of the segment to an expression, use SetDutyCycleExpression instead.

Parameters:  **value** ([`SymbolType`](#ApiClient.SymbolType "ApiClient.SymbolType")) – the dutyCycle value symbol

SetOffset(*offset*)[¶](#ApiClient.SawSegment.SetOffset "Link to this definition")  
Sets the offset value of the segment.

Parameters:  **offset** (*float*) – the offset value

SetOffsetExpression(*expression*)[¶](#ApiClient.SawSegment.SetOffsetExpression "Link to this definition")  
Sets the offset value expression. The expression has to conform to the ASAM XIL GES syntax for ConstSymbol expressions.

Parameters:  **expression** (*str*) – the expression

SetOffsetSymbol(*value*)[¶](#ApiClient.SawSegment.SetOffsetSymbol "Link to this definition")  
Sets a SymbolType object as offset value of the segment. If you want to set the offset value of the segment to an expression, use SetOffsetExpression instead.

Parameters:  **value** ([`SymbolType`](#ApiClient.SymbolType "ApiClient.SymbolType")) – the offset value symbol

SetPeriod(*period*)[¶](#ApiClient.SawSegment.SetPeriod "Link to this definition")  
Sets the period value of the segment.

Parameters:  **period** (*float*) – the period value

SetPeriodExpression(*expression*)[¶](#ApiClient.SawSegment.SetPeriodExpression "Link to this definition")  
Sets the period value expression. The expression has to conform to the ASAM XIL GES syntax for ConstSymbol expressions.

Parameters:  **expression** (*str*) – the period expression

SetPeriodSymbol(*value*)[¶](#ApiClient.SawSegment.SetPeriodSymbol "Link to this definition")  
Sets a SymbolType object as period value of the segment. If you want to set the period value of the segment to an expression, use SetPeriodExpression instead.

Parameters:  **value** ([`SymbolType`](#ApiClient.SymbolType "ApiClient.SymbolType")) – the period value symbol

SetPhase(*phase*)[¶](#ApiClient.SawSegment.SetPhase "Link to this definition")  
Sets the phase value of the segment.

Parameters:  **phase** (*float*) – the phase value

SetPhaseExpression(*expression*)[¶](#ApiClient.SawSegment.SetPhaseExpression "Link to this definition")  
Sets the phase value expression. The expression has to conform to the ASAM XIL GES syntax for ConstSymbol expressions.

Parameters:  **expression** (*str*) – the phase expression

SetPhaseSymbol(*value*)[¶](#ApiClient.SawSegment.SetPhaseSymbol "Link to this definition")  
Sets a SymbolType object as phase value of the segment. If you want to set the phase value of the segment to an expression, use SetPhaseExpression instead.

Parameters:  **value** ([`SymbolType`](#ApiClient.SymbolType "ApiClient.SymbolType")) – the phase value symbol

SetStopTrigger(*stopTrigger*)[¶](#ApiClient.SawSegment.SetStopTrigger "Link to this definition")  
Sets the stop trigger of the segment

Parameters:  **stopTrigger** (*str*) – The stop trigger

SetTimeout(*timeout*)[¶](#ApiClient.SawSegment.SetTimeout "Link to this definition")  
Sets the timeout of the segment

Parameters:  **timeout** (*float*) – The timeout

## PulseSegment[¶](#pulsesegment "Link to this heading")

*class* PulseSegment[¶](#ApiClient.PulseSegment "Link to this definition")  
Base class

[`SignalSegment`](#ApiClient.SignalSegment "ApiClient.SignalSegment")

Returned by

- [`SignalApi.CreatePulseSegment`](#ApiClient.SignalApi.CreatePulseSegment "ApiClient.SignalApi.CreatePulseSegment")

Clone()[¶](#ApiClient.PulseSegment.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`PulseSegment`](#ApiClient.PulseSegment "ApiClient.PulseSegment")

GetAmplitude()[¶](#ApiClient.PulseSegment.GetAmplitude "Link to this definition")  
Returns the amplitude value of the segment.

Return type:  float

Returns:  the amplitude value

GetAmplitudeExpression()[¶](#ApiClient.PulseSegment.GetAmplitudeExpression "Link to this definition")  
Returns the amplitude value expression. The expression conforms to the ASAM XIL GES syntax for ConstSymbol expressions.

Return type:  str

Returns:  the amplitude expression

GetAmplitudeSymbol()[¶](#ApiClient.PulseSegment.GetAmplitudeSymbol "Link to this definition")  
Returns the SymbolType object of the segment amplitude value.

Return type:  [`SymbolType`](#ApiClient.SymbolType "ApiClient.SymbolType")

Returns:  the amplitude value symbol

GetComment()[¶](#ApiClient.PulseSegment.GetComment "Link to this definition")  
Returns the comment of the segment.

Returns:  The comment

Return type:  str

GetDuration()[¶](#ApiClient.PulseSegment.GetDuration "Link to this definition")  
Returns the current duration of the signal segment.

Returns:  The duration

Return type:  float

GetDurationExpression()[¶](#ApiClient.PulseSegment.GetDurationExpression "Link to this definition")  
Returns the duration expression of the segment that is conform to the ASAM XIL GES syntax for ConstSymbol expressions.

Return type:  str

Returns:  the duration expression

GetDutyCycle()[¶](#ApiClient.PulseSegment.GetDutyCycle "Link to this definition")  
Returns the dutyCycle value of the segment.

Return type:  float

Returns:  the dutyCycle value

GetDutyCycleExpression()[¶](#ApiClient.PulseSegment.GetDutyCycleExpression "Link to this definition")  
Returns the dutyCycle value expression. The expression conforms to the ASAM XIL GES syntax for ConstSymbol expressions.

Return type:  str

Returns:  the dutyCycle value expression

GetDutyCycleSymbol()[¶](#ApiClient.PulseSegment.GetDutyCycleSymbol "Link to this definition")  
Returns the SymbolType object of the segment dutyCycle value.

Return type:  [`SymbolType`](#ApiClient.SymbolType "ApiClient.SymbolType")

Returns:  the dutyCycle value symbol

GetFinalValue()[¶](#ApiClient.PulseSegment.GetFinalValue "Link to this definition")  
Returns the final value of the signal segment.

Returns:  the final value

Return type:  float

GetFirstValue()[¶](#ApiClient.PulseSegment.GetFirstValue "Link to this definition")  
Returns the first value of the segment.

Returns:  the first value or NaN

Return type:  float

GetOffset()[¶](#ApiClient.PulseSegment.GetOffset "Link to this definition")  
Returns the offset value of the segment.

Return type:  float

Returns:  the offset value

GetOffsetExpression()[¶](#ApiClient.PulseSegment.GetOffsetExpression "Link to this definition")  
Returns the offset value expression. The expression conforms to the ASAM XIL GES syntax for ConstSymbol expressions.

Return type:  str

Returns:  the offset value expression

GetOffsetSymbol()[¶](#ApiClient.PulseSegment.GetOffsetSymbol "Link to this definition")  
Returns the SymbolType object of the segment offset value.

Return type:  [`SymbolType`](#ApiClient.SymbolType "ApiClient.SymbolType")

Returns:  the offset value symbol

GetPeriod()[¶](#ApiClient.PulseSegment.GetPeriod "Link to this definition")  
Returns the period value of the segment.

Return type:  float

Returns:  the period value

GetPeriodExpression()[¶](#ApiClient.PulseSegment.GetPeriodExpression "Link to this definition")  
Returns the period value expression. The expression conforms to the ASAM XIL GES syntax for ConstSymbol expressions.

Return type:  str

Returns:  the period value expression

GetPeriodSymbol()[¶](#ApiClient.PulseSegment.GetPeriodSymbol "Link to this definition")  
Returns the SymbolType object of the segment period value.

Return type:  [`SymbolType`](#ApiClient.SymbolType "ApiClient.SymbolType")

Returns:  the period value symbol

GetPhase()[¶](#ApiClient.PulseSegment.GetPhase "Link to this definition")  
Returns the phase value of the segment.

Return type:  float

Returns:  the phase value

GetPhaseExpression()[¶](#ApiClient.PulseSegment.GetPhaseExpression "Link to this definition")  
Returns the phase value expression. The expression conforms to the ASAM XIL GES syntax for ConstSymbol expressions.

Return type:  str

Returns:  the phase value expression

GetPhaseSymbol()[¶](#ApiClient.PulseSegment.GetPhaseSymbol "Link to this definition")  
Returns the SymbolType object of the segment phase value.

Return type:  [`SymbolType`](#ApiClient.SymbolType "ApiClient.SymbolType")

Returns:  the phase value symbol

GetStopTrigger()[¶](#ApiClient.PulseSegment.GetStopTrigger "Link to this definition")  
Returns the stop trigger of the segment

Returns:  stop trigger

Return type:  str

GetTimeout()[¶](#ApiClient.PulseSegment.GetTimeout "Link to this definition")  
Returns the timeout of the segment

Returns:  timeout

Return type:  float

GetType()[¶](#ApiClient.PulseSegment.GetType "Link to this definition")  
Returns the type of the segment. (e.g. “Constant”)

Returns:  The type

Return type:  str

GetValueAt(*timestamp*)[¶](#ApiClient.PulseSegment.GetValueAt "Link to this definition")  
Returns the value at the given timestamp.

Parameters:  **timestamp** (*float*) – The timestamp

Returns:  the value or NaN

Return type:  float

RemoveStopTrigger()[¶](#ApiClient.PulseSegment.RemoveStopTrigger "Link to this definition")  
Removes the stop trigger of the segment

RemoveTimeout()[¶](#ApiClient.PulseSegment.RemoveTimeout "Link to this definition")  
Removes the timeout of the segment

SetAmplitude(*amplitude*)[¶](#ApiClient.PulseSegment.SetAmplitude "Link to this definition")  
Sets the amplitude value of the segment.

Parameters:  **amplitude** (*float*) – the amplitude value

SetAmplitudeExpression(*expression*)[¶](#ApiClient.PulseSegment.SetAmplitudeExpression "Link to this definition")  
Sets the amplitude expression of the segment. The expression has to conform to the ASAM XIL GES syntax for ConstSymbol expressions.

Parameters:  **expression** (*str*) – the amplitude expression

SetAmplitudeSymbol(*value*)[¶](#ApiClient.PulseSegment.SetAmplitudeSymbol "Link to this definition")  
Sets a SymbolType object as amplitude value of the segment. If you want to set the amplitude value of the segment to an expression, use SetAmplitudeExpression instead.

Parameters:  **value** ([`SymbolType`](#ApiClient.SymbolType "ApiClient.SymbolType")) – the amplitude value symbol

SetComment(*comment*)[¶](#ApiClient.PulseSegment.SetComment "Link to this definition")  
Sets the comment of the segment.

Parameters:  **comment** (*str*) – The comment

SetDuration(*duration*)[¶](#ApiClient.PulseSegment.SetDuration "Link to this definition")  
Sets the duration of the segment in seconds.If you want to set the duration value of the segment to an expression, use SetDurationExpression instead.

Parameters:  **duration** (*float*) – the segments duration

SetDurationExpression(*expression*)[¶](#ApiClient.PulseSegment.SetDurationExpression "Link to this definition")  
Sets the duration value as an expression. The expression needs to be conform to the ASAM XIL GES syntax for ConstSymbol expressions.

Parameters:  **expression** (*str*) – the duration expression

SetDutyCycle(*dutyCycle*)[¶](#ApiClient.PulseSegment.SetDutyCycle "Link to this definition")  
Sets the dutyCycle value of the segment.

Parameters:  **dutyCycle** (*float*) – the dutyCycle value

SetDutyCycleExpression(*expression*)[¶](#ApiClient.PulseSegment.SetDutyCycleExpression "Link to this definition")  
Sets the dutyCycle value expression. The expression has to conform to the ASAM XIL GES syntax for ConstSymbol expressions.

Parameters:  **expression** (*str*) – the dutyCycle expression

SetDutyCycleSymbol(*value*)[¶](#ApiClient.PulseSegment.SetDutyCycleSymbol "Link to this definition")  
Sets a SymbolType object as dutyCycle value of the segment. If you want to set the dutyCycle value of the segment to an expression, use SetDutyCycleExpression instead.

Parameters:  **value** ([`SymbolType`](#ApiClient.SymbolType "ApiClient.SymbolType")) – the dutyCycle value symbol

SetOffset(*offset*)[¶](#ApiClient.PulseSegment.SetOffset "Link to this definition")  
Sets the offset value of the segment.

Parameters:  **offset** (*float*) – the offset value

SetOffsetExpression(*expression*)[¶](#ApiClient.PulseSegment.SetOffsetExpression "Link to this definition")  
Sets the offset value expression. The expression has to conform to the ASAM XIL GES syntax for ConstSymbol expressions.

Parameters:  **expression** (*str*) – the expression

SetOffsetSymbol(*value*)[¶](#ApiClient.PulseSegment.SetOffsetSymbol "Link to this definition")  
Sets a SymbolType object as offset value of the segment. If you want to set the offset value of the segment to an expression, use SetOffsetExpression instead.

Parameters:  **value** ([`SymbolType`](#ApiClient.SymbolType "ApiClient.SymbolType")) – the offset value symbol

SetPeriod(*period*)[¶](#ApiClient.PulseSegment.SetPeriod "Link to this definition")  
Sets the period value of the segment.

Parameters:  **period** (*float*) – the period value

SetPeriodExpression(*expression*)[¶](#ApiClient.PulseSegment.SetPeriodExpression "Link to this definition")  
Sets the period value expression. The expression has to conform to the ASAM XIL GES syntax for ConstSymbol expressions.

Parameters:  **expression** (*str*) – the period expression

SetPeriodSymbol(*value*)[¶](#ApiClient.PulseSegment.SetPeriodSymbol "Link to this definition")  
Sets a SymbolType object as period value of the segment. If you want to set the period value of the segment to an expression, use SetPeriodExpression instead.

Parameters:  **value** ([`SymbolType`](#ApiClient.SymbolType "ApiClient.SymbolType")) – the period value symbol

SetPhase(*phase*)[¶](#ApiClient.PulseSegment.SetPhase "Link to this definition")  
Sets the phase value of the segment.

Parameters:  **phase** (*float*) – the phase value

SetPhaseExpression(*expression*)[¶](#ApiClient.PulseSegment.SetPhaseExpression "Link to this definition")  
Sets the phase value expression. The expression has to conform to the ASAM XIL GES syntax for ConstSymbol expressions.

Parameters:  **expression** (*str*) – the phase expression

SetPhaseSymbol(*value*)[¶](#ApiClient.PulseSegment.SetPhaseSymbol "Link to this definition")  
Sets a SymbolType object as phase value of the segment. If you want to set the phase value of the segment to an expression, use SetPhaseExpression instead.

Parameters:  **value** ([`SymbolType`](#ApiClient.SymbolType "ApiClient.SymbolType")) – the phase value symbol

SetStopTrigger(*stopTrigger*)[¶](#ApiClient.PulseSegment.SetStopTrigger "Link to this definition")  
Sets the stop trigger of the segment

Parameters:  **stopTrigger** (*str*) – The stop trigger

SetTimeout(*timeout*)[¶](#ApiClient.PulseSegment.SetTimeout "Link to this definition")  
Sets the timeout of the segment

Parameters:  **timeout** (*float*) – The timeout

## OperationSegment[¶](#operationsegment "Link to this heading")

*class* OperationSegment[¶](#ApiClient.OperationSegment "Link to this definition")  
Base class

[`SignalSegment`](#ApiClient.SignalSegment "ApiClient.SignalSegment")

Returned by

- [`SignalApi.CreateOperationSegment`](#ApiClient.SignalApi.CreateOperationSegment "ApiClient.SignalApi.CreateOperationSegment")

AppendSegment(*signalSegment*)[¶](#ApiClient.OperationSegment.AppendSegment "Link to this definition")  
Appends a segment to the OperationSegment

Parameters:  **signalSegment** ([`SignalSegment`](#ApiClient.SignalSegment "ApiClient.SignalSegment")) – The signalSegment

Clone()[¶](#ApiClient.OperationSegment.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`OperationSegment`](#ApiClient.OperationSegment "ApiClient.OperationSegment")

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

Return type:  list[[`SignalSegment`](#ApiClient.SignalSegment "ApiClient.SignalSegment")]

GetType()[¶](#ApiClient.OperationSegment.GetType "Link to this definition")  
Returns the type of the segment. (e.g. “Constant”)

Returns:  The type

Return type:  str

GetValueAt(*timestamp*)[¶](#ApiClient.OperationSegment.GetValueAt "Link to this definition")  
Returns the value at the given timestamp.

Parameters:  **timestamp** (*float*) – The timestamp

Returns:  the value or NaN

Return type:  float

RemoveSegment(*signalSegment*)[¶](#ApiClient.OperationSegment.RemoveSegment "Link to this definition")  
Removes a segment of the OperationSegment

Parameters:  **signalSegment** ([`SignalSegment`](#ApiClient.SignalSegment "ApiClient.SignalSegment")) – The signalSegment to be removed

SetComment(*comment*)[¶](#ApiClient.OperationSegment.SetComment "Link to this definition")  
Sets the comment of the signal description

Parameters:  **comment** (*str*) – Signal description comment

SetDuration(*duration*)[¶](#ApiClient.OperationSegment.SetDuration "Link to this definition")  
Sets the duration of the segment in seconds.If you want to set the duration value of the segment to an expression, use SetDurationExpression instead.

Parameters:  **duration** (*float*) – the segments duration

SetDurationExpression(*expression*)[¶](#ApiClient.OperationSegment.SetDurationExpression "Link to this definition")  
Sets the duration value as an expression. The expression needs to be conform to the ASAM XIL GES syntax for ConstSymbol expressions.

Parameters:  **expression** (*str*) – the duration expression

SetOperation(*operation*)[¶](#ApiClient.OperationSegment.SetOperation "Link to this definition")  
Sets the operation of the segment

Parameters:  **operation** (*str*) – The operation. ‘ADD’ or ‘MULT’

## SignalValueSegment[¶](#signalvaluesegment "Link to this heading")

*class* SignalValueSegment[¶](#ApiClient.SignalValueSegment "Link to this definition")  
Base class

[`SignalSegment`](#ApiClient.SignalSegment "ApiClient.SignalSegment")

Returned by

- [`SignalApi.CreateSignalValueSegment`](#ApiClient.SignalApi.CreateSignalValueSegment "ApiClient.SignalApi.CreateSignalValueSegment")

Clone()[¶](#ApiClient.SignalValueSegment.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`SignalValueSegment`](#ApiClient.SignalValueSegment "ApiClient.SignalValueSegment")

GetComment()[¶](#ApiClient.SignalValueSegment.GetComment "Link to this definition")  
Returns the comment of the segment.

Returns:  The comment

Return type:  str

GetDataSignalName()[¶](#ApiClient.SignalValueSegment.GetDataSignalName "Link to this definition")  
Returns the name of the data signal

Returns:  Name of data signal

Return type:  str

GetDataVector()[¶](#ApiClient.SignalValueSegment.GetDataVector "Link to this definition")  
Returns the dataVector of the segment.

Returns:  the dataVector

Return type:  list[float]

GetDuration()[¶](#ApiClient.SignalValueSegment.GetDuration "Link to this definition")  
Returns the current duration of the signal segment.

Returns:  The duration

Return type:  float

GetDurationExpression()[¶](#ApiClient.SignalValueSegment.GetDurationExpression "Link to this definition")  
Returns the duration expression of the segment that is conform to the ASAM XIL GES syntax for ConstSymbol expressions.

Return type:  str

Returns:  the duration expression

GetFinalValue()[¶](#ApiClient.SignalValueSegment.GetFinalValue "Link to this definition")  
Returns the final value of the signal segment.

Returns:  the final value

Return type:  float

GetFirstValue()[¶](#ApiClient.SignalValueSegment.GetFirstValue "Link to this definition")  
Returns the first value of the segment.

Returns:  the first value or NaN

Return type:  float

GetTimeSignalName()[¶](#ApiClient.SignalValueSegment.GetTimeSignalName "Link to this definition")  
Returns the name of the time signal

Returns:  Name of time signal

Return type:  str

GetTimeVector()[¶](#ApiClient.SignalValueSegment.GetTimeVector "Link to this definition")  
Returns the timeVector of the segment.

Returns:  the timeVctor

Return type:  list[float]

GetType()[¶](#ApiClient.SignalValueSegment.GetType "Link to this definition")  
Returns the type of the segment. (e.g. “Constant”)

Returns:  The type

Return type:  str

GetValueAt(*timestamp*)[¶](#ApiClient.SignalValueSegment.GetValueAt "Link to this definition")  
Returns the value at the given timestamp.

Parameters:  **timestamp** (*float*) – The timestamp

Returns:  the value or NaN

Return type:  float

SetComment(*comment*)[¶](#ApiClient.SignalValueSegment.SetComment "Link to this definition")  
Sets the comment of the segment.

Parameters:  **comment** (*str*) – The comment

SetDataVector(*dataVector*)[¶](#ApiClient.SignalValueSegment.SetDataVector "Link to this definition")  
Sets the dataVector of the segment.

Parameters:  **dataVector** (*list[float]*) – the dataVector to set

SetDuration(*duration*)[¶](#ApiClient.SignalValueSegment.SetDuration "Link to this definition")  
Sets the duration of the segment in seconds.If you want to set the duration value of the segment to an expression, use SetDurationExpression instead.

Parameters:  **duration** (*float*) – the segments duration

SetDurationExpression(*expression*)[¶](#ApiClient.SignalValueSegment.SetDurationExpression "Link to this definition")  
Sets the duration value as an expression. The expression needs to be conform to the ASAM XIL GES syntax for ConstSymbol expressions.

Parameters:  **expression** (*str*) – the duration expression

SetExportDataAsOriginal(*asOriginal=True*)[¶](#ApiClient.SignalValueSegment.SetExportDataAsOriginal "Link to this definition")  
Conversion to MAT-File will export all samples with changed values.

Parameters:  **asOriginal** (*bool*) – original values will be exported

SetTimeVector(*timeVector*)[¶](#ApiClient.SignalValueSegment.SetTimeVector "Link to this definition")  
Sets the timeVector of the segment.

Parameters:  **timeVector** (*list[float]*) – the timeVector to set

## OperationSignalDescription[¶](#operationsignaldescription "Link to this heading")

*class* OperationSignalDescription[¶](#ApiClient.OperationSignalDescription "Link to this definition")  
Base class

[`SignalDescription`](#ApiClient.SignalDescription "ApiClient.SignalDescription")

Returned by

- [`SignalApi.CreateOperationSignal`](#ApiClient.SignalApi.CreateOperationSignal "ApiClient.SignalApi.CreateOperationSignal")

AppendSignal(*signal*)[¶](#ApiClient.OperationSignalDescription.AppendSignal "Link to this definition")  
Appends a signal to the OperationSignalDescription

Parameters:  **signal** ([`SignalDescription`](#ApiClient.SignalDescription "ApiClient.SignalDescription")) – The signal

Clone()[¶](#ApiClient.OperationSignalDescription.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`OperationSignalDescription`](#ApiClient.OperationSignalDescription "ApiClient.OperationSignalDescription")

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

Return type:  list[[`SignalDescription`](#ApiClient.SignalDescription "ApiClient.SignalDescription")]

GetValueAt(*timestamp*)[¶](#ApiClient.OperationSignalDescription.GetValueAt "Link to this definition")  
Returns the value at the given timestamp. If timestamp is bigger than duration, NaN will be returned.

Parameters:  **timestamp** (*float*) – The timestamp

Returns:  the value or NaN

Return type:  float

RemoveSignal(*signalDescription*)[¶](#ApiClient.OperationSignalDescription.RemoveSignal "Link to this definition")  
Removes a signal of the OperationSignalDescription

Parameters:  **signalDescription** ([`SignalDescription`](#ApiClient.SignalDescription "ApiClient.SignalDescription")) – The signal to be removed

SetComment(*comment*)[¶](#ApiClient.OperationSignalDescription.SetComment "Link to this definition")  
Sets the comment of the signal description

Parameters:  **comment** (*str*) – Signal description comment

SetOperation(*operation*)[¶](#ApiClient.OperationSignalDescription.SetOperation "Link to this definition")  
Sets the operation of the operation signal

Parameters:  **operation** (*str*) – The operation. ‘ADD’ or ‘MULT’

## SignalDescription[¶](#signaldescription "Link to this heading")

*class* SignalDescription[¶](#ApiClient.SignalDescription "Link to this definition")  
Returned by

- [`OperationSignalDescription.GetSignalDescriptions`](#ApiClient.OperationSignalDescription.GetSignalDescriptions "ApiClient.OperationSignalDescription.GetSignalDescriptions")

- [`SignalDescriptionFile.GetAllSignals`](SignalDescriptionApi.md#ApiClient.SignalDescriptionFile.GetAllSignals "ApiClient.SignalDescriptionFile.GetAllSignals")

Subclasses

- [`OperationSignalDescription`](#ApiClient.OperationSignalDescription "ApiClient.OperationSignalDescription")

- [`SegmentSignalDescription`](#ApiClient.SegmentSignalDescription "ApiClient.SegmentSignalDescription")

Clone()[¶](#ApiClient.SignalDescription.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`SignalDescription`](#ApiClient.SignalDescription "ApiClient.SignalDescription")

GetComment()[¶](#ApiClient.SignalDescription.GetComment "Link to this definition")  
Returns the comment of the signal description

Returns:  Signal description comment

Return type:  str

GetDuration()[¶](#ApiClient.SignalDescription.GetDuration "Link to this definition")  
Returns the duration of the signal description.

Returns:  Duration of signal description

Return type:  float

GetFinalValue()[¶](#ApiClient.SignalDescription.GetFinalValue "Link to this definition")  
Returns the final value of the signal description.

Returns:  the final value

Return type:  float

GetFirstValue()[¶](#ApiClient.SignalDescription.GetFirstValue "Link to this definition")  
Returns the first value of the segment.

Returns:  the first value or NaN

Return type:  float

GetName()[¶](#ApiClient.SignalDescription.GetName "Link to this definition")  
Returns the name of the signal description.

Returns:  Signal description name

Return type:  str

GetValueAt(*timestamp*)[¶](#ApiClient.SignalDescription.GetValueAt "Link to this definition")  
Returns the value at the given timestamp. If timestamp is bigger than duration, NaN will be returned.

Parameters:  **timestamp** (*float*) – The timestamp

Returns:  the value or NaN

Return type:  float

SetComment(*comment*)[¶](#ApiClient.SignalDescription.SetComment "Link to this definition")  
Sets the comment of the signal description

Parameters:  **comment** (*str*) – Signal description comment

## SegmentSignalDescription[¶](#segmentsignaldescription "Link to this heading")

*class* SegmentSignalDescription[¶](#ApiClient.SegmentSignalDescription "Link to this definition")  
Base class

[`SignalDescription`](#ApiClient.SignalDescription "ApiClient.SignalDescription")

Returned by

- [`SignalApi.CreateSignal`](#ApiClient.SignalApi.CreateSignal "ApiClient.SignalApi.CreateSignal")

AppendSegment(*segment*)[¶](#ApiClient.SegmentSignalDescription.AppendSegment "Link to this definition")  
Appends a signal segment as last element.

Parameters:  **segment** ([`SignalSegment`](#ApiClient.SignalSegment "ApiClient.SignalSegment")) – Signal segment

Clone()[¶](#ApiClient.SegmentSignalDescription.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`SegmentSignalDescription`](#ApiClient.SegmentSignalDescription "ApiClient.SegmentSignalDescription")

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

Return type:  list[[`SignalSegment`](#ApiClient.SignalSegment "ApiClient.SignalSegment")]

GetValueAt(*timestamp*)[¶](#ApiClient.SegmentSignalDescription.GetValueAt "Link to this definition")  
Returns the value at the given timestamp. If timestamp is bigger than duration, NaN will be returned.

Parameters:  **timestamp** (*float*) – The timestamp

Returns:  the value or NaN

Return type:  float

RemoveSegment(*segment*)[¶](#ApiClient.SegmentSignalDescription.RemoveSegment "Link to this definition")  
Removes a signal segment.

Parameters:  **segment** ([`SignalSegment`](#ApiClient.SignalSegment "ApiClient.SignalSegment")) – Signal segment

SetComment(*comment*)[¶](#ApiClient.SegmentSignalDescription.SetComment "Link to this definition")  
Sets the comment of the signal description

Parameters:  **comment** (*str*) – Signal description comment
