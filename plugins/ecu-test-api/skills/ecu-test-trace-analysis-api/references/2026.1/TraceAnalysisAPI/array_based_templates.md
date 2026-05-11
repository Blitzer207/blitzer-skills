Array-based NumPy trace step templates [ Array-based NumPy trace step templates ](#)

Array-based NumPy trace step templates

- [ NumpyBasedTraceStep ](#numpybasedtracestep)
  - [C traceAnalysisAPI.arraybased.NumpyBasedTraceStep ](#traceAnalysisAPI.arraybased.NumpyBasedTraceStep)
    - [M GetInterfaceRevision ](#traceAnalysisAPI.arraybased.NumpyBasedTraceStep.GetInterfaceRevision)
    - [M GetDescription ](#traceAnalysisAPI.arraybased.NumpyBasedTraceStep.GetDescription)
    - [M GetSignals ](#traceAnalysisAPI.arraybased.NumpyBasedTraceStep.GetSignals)
    - [M GetParameters ](#traceAnalysisAPI.arraybased.NumpyBasedTraceStep.GetParameters)
    - [M GetTimeAxisDefinition ](#traceAnalysisAPI.arraybased.NumpyBasedTraceStep.GetTimeAxisDefinition)
    - [M Check ](#traceAnalysisAPI.arraybased.NumpyBasedTraceStep.Check)
    - [M Process ](#traceAnalysisAPI.arraybased.NumpyBasedTraceStep.Process)
    - [M FitToAxis ](#traceAnalysisAPI.arraybased.NumpyBasedTraceStep.FitToAxis)
    - [M CalculateRanges ](#traceAnalysisAPI.arraybased.NumpyBasedTraceStep.CalculateRanges)
    - [M CalculateMaskForRange ](#traceAnalysisAPI.arraybased.NumpyBasedTraceStep.CalculateMaskForRange)
    - [M GetParameterPanel ](#traceAnalysisAPI.arraybased.NumpyBasedTraceStep.GetParameterPanel)
- [ SignalDefinition ](#signaldefinition)
  - [C traceAnalysisAPI.arraybased.SignalDefinition ](#traceAnalysisAPI.arraybased.SignalDefinition)
    - [M `\_\_init\_\_` ](#traceAnalysisAPI.arraybased.SignalDefinition.__init__)
- [ ParameterDefinition ](#parameterdefinition)
  - [C traceAnalysisAPI.arraybased.ParameterDefinition ](#traceAnalysisAPI.arraybased.ParameterDefinition)
    - [M `\_\_init\_\_` ](#traceAnalysisAPI.arraybased.ParameterDefinition.__init__)
- [ Report ](#report)
  - [C traceAnalysisAPI.arraybased.Report ](#traceAnalysisAPI.arraybased.Report)
    - [M ImageFromBytes ](#traceAnalysisAPI.arraybased.Report.ImageFromBytes)
    - [M AddResultColumn ](#traceAnalysisAPI.arraybased.Report.AddResultColumn)
    - [M GetResultId ](#traceAnalysisAPI.arraybased.Report.GetResultId)
    - [M Image ](#traceAnalysisAPI.arraybased.Report.Image)
    - [M Log ](#traceAnalysisAPI.arraybased.Report.Log)
    - [M LogDebug ](#traceAnalysisAPI.arraybased.Report.LogDebug)
    - [M LogError ](#traceAnalysisAPI.arraybased.Report.LogError)
    - [M LogInfo ](#traceAnalysisAPI.arraybased.Report.LogInfo)
    - [M LogWarning ](#traceAnalysisAPI.arraybased.Report.LogWarning)
    - [M SetLogComponent ](#traceAnalysisAPI.arraybased.Report.SetLogComponent)
    - [M SetResultError ](#traceAnalysisAPI.arraybased.Report.SetResultError)
    - [M SetResultFailed ](#traceAnalysisAPI.arraybased.Report.SetResultFailed)
    - [M SetResultId ](#traceAnalysisAPI.arraybased.Report.SetResultId)
    - [M SetResultInconclusive ](#traceAnalysisAPI.arraybased.Report.SetResultInconclusive)
    - [M SetResultSuccess ](#traceAnalysisAPI.arraybased.Report.SetResultSuccess)
    - [M SetResultText ](#traceAnalysisAPI.arraybased.Report.SetResultText)
    - [M Table ](#traceAnalysisAPI.arraybased.Report.Table)
    - [M UpdateResultId ](#traceAnalysisAPI.arraybased.Report.UpdateResultId)
- [ TriggerRange ](#triggerrange)
  - [C traceAnalysisAPI.arraybased.TriggerRange ](#traceAnalysisAPI.arraybased.TriggerRange)
    - [M ImageFromBytes ](#traceAnalysisAPI.arraybased.TriggerRange.ImageFromBytes)
    - [M GetRelativeTimestamps ](#traceAnalysisAPI.arraybased.TriggerRange.GetRelativeTimestamps)
    - [M GetResultId ](#traceAnalysisAPI.arraybased.TriggerRange.GetResultId)
    - [M GetSlice ](#traceAnalysisAPI.arraybased.TriggerRange.GetSlice)
    - [M GetStartTime ](#traceAnalysisAPI.arraybased.TriggerRange.GetStartTime)
    - [M GetStartValue ](#traceAnalysisAPI.arraybased.TriggerRange.GetStartValue)
    - [M GetStopTime ](#traceAnalysisAPI.arraybased.TriggerRange.GetStopTime)
    - [M GetStopValue ](#traceAnalysisAPI.arraybased.TriggerRange.GetStopValue)
    - [M GetTimestamps ](#traceAnalysisAPI.arraybased.TriggerRange.GetTimestamps)
    - [M GetValues ](#traceAnalysisAPI.arraybased.TriggerRange.GetValues)
    - [M Image ](#traceAnalysisAPI.arraybased.TriggerRange.Image)
    - [M IsWholeTrace ](#traceAnalysisAPI.arraybased.TriggerRange.IsWholeTrace)
    - [M Range ](#traceAnalysisAPI.arraybased.TriggerRange.Range)
    - [M SetResultError ](#traceAnalysisAPI.arraybased.TriggerRange.SetResultError)
    - [M SetResultFailed ](#traceAnalysisAPI.arraybased.TriggerRange.SetResultFailed)
    - [M SetResultId ](#traceAnalysisAPI.arraybased.TriggerRange.SetResultId)
    - [M SetResultInconclusive ](#traceAnalysisAPI.arraybased.TriggerRange.SetResultInconclusive)
    - [M SetResultNone ](#traceAnalysisAPI.arraybased.TriggerRange.SetResultNone)
    - [M SetResultSuccess ](#traceAnalysisAPI.arraybased.TriggerRange.SetResultSuccess)
    - [M SetResultText ](#traceAnalysisAPI.arraybased.TriggerRange.SetResultText)
    - [M Spot ](#traceAnalysisAPI.arraybased.TriggerRange.Spot)
    - [M Table ](#traceAnalysisAPI.arraybased.TriggerRange.Table)
    - [M UpdateResultId ](#traceAnalysisAPI.arraybased.TriggerRange.UpdateResultId)
- [ Signal ](#signal)
  - [C traceAnalysisAPI.arraybased.Signal ](#traceAnalysisAPI.arraybased.Signal)
    - [M Emit ](#traceAnalysisAPI.arraybased.Signal.Emit)
    - [M GetGenericName ](#traceAnalysisAPI.arraybased.Signal.GetGenericName)
    - [M GetInterpolatedValues ](#traceAnalysisAPI.arraybased.Signal.GetInterpolatedValues)
    - [M GetMappingItemName ](#traceAnalysisAPI.arraybased.Signal.GetMappingItemName)
    - [M GetRecordingInfo ](#traceAnalysisAPI.arraybased.Signal.GetRecordingInfo)
    - [M GetTextTable ](#traceAnalysisAPI.arraybased.Signal.GetTextTable)
    - [M GetTimestamps ](#traceAnalysisAPI.arraybased.Signal.GetTimestamps)
    - [M GetTraceFileSignalName ](#traceAnalysisAPI.arraybased.Signal.GetTraceFileSignalName)
    - [M GetUnit ](#traceAnalysisAPI.arraybased.Signal.GetUnit)
    - [M GetValueAt ](#traceAnalysisAPI.arraybased.Signal.GetValueAt)
    - [M GetValues ](#traceAnalysisAPI.arraybased.Signal.GetValues)
    - [M IsBound ](#traceAnalysisAPI.arraybased.Signal.IsBound)
    - [M IsFound ](#traceAnalysisAPI.arraybased.Signal.IsFound)
    - [M IsOutSignal ](#traceAnalysisAPI.arraybased.Signal.IsOutSignal)
- [ RecordingInfo ](#recordinginfo)
  - [C traceAnalysisAPI.arraybased.RecordingInfo ](#traceAnalysisAPI.arraybased.RecordingInfo)
    - [M GetFirstPath ](#traceAnalysisAPI.arraybased.RecordingInfo.GetFirstPath)
    - [M GetPath ](#traceAnalysisAPI.arraybased.RecordingInfo.GetPath)
    - [M GetPathList ](#traceAnalysisAPI.arraybased.RecordingInfo.GetPathList)
    - [M GetRecordingName ](#traceAnalysisAPI.arraybased.RecordingInfo.GetRecordingName)
    - [M GetRecordingNumber ](#traceAnalysisAPI.arraybased.RecordingInfo.GetRecordingNumber)
    - [M GetRecordingType ](#traceAnalysisAPI.arraybased.RecordingInfo.GetRecordingType)
    - [M GetStartTimeNs ](#traceAnalysisAPI.arraybased.RecordingInfo.GetStartTimeNs)
- [ ReportTable ](#reporttable)
  - [C traceAnalysisAPI.arraybased.ReportTable ](#traceAnalysisAPI.arraybased.ReportTable)
    - [M AddRow ](#traceAnalysisAPI.arraybased.ReportTable.AddRow)
    - [M SetHeader ](#traceAnalysisAPI.arraybased.ReportTable.SetHeader)

[ Event based tracestep templates ](event_based_templates.md)

[ Stream based tracestep templates ](stream_based_templates.md)

[ Custom GUI for parameters ](custom_param_gui.md)

[ Custom trace synchronization ](custom_trace_synchronization.md)

[ Available python libraries and APIs ](python_libraries.md)

Array-based NumPy trace step templates

- [ NumpyBasedTraceStep ](#numpybasedtracestep)
  - [C traceAnalysisAPI.arraybased.NumpyBasedTraceStep ](#traceAnalysisAPI.arraybased.NumpyBasedTraceStep)
    - [M GetInterfaceRevision ](#traceAnalysisAPI.arraybased.NumpyBasedTraceStep.GetInterfaceRevision)
    - [M GetDescription ](#traceAnalysisAPI.arraybased.NumpyBasedTraceStep.GetDescription)
    - [M GetSignals ](#traceAnalysisAPI.arraybased.NumpyBasedTraceStep.GetSignals)
    - [M GetParameters ](#traceAnalysisAPI.arraybased.NumpyBasedTraceStep.GetParameters)
    - [M GetTimeAxisDefinition ](#traceAnalysisAPI.arraybased.NumpyBasedTraceStep.GetTimeAxisDefinition)
    - [M Check ](#traceAnalysisAPI.arraybased.NumpyBasedTraceStep.Check)
    - [M Process ](#traceAnalysisAPI.arraybased.NumpyBasedTraceStep.Process)
    - [M FitToAxis ](#traceAnalysisAPI.arraybased.NumpyBasedTraceStep.FitToAxis)
    - [M CalculateRanges ](#traceAnalysisAPI.arraybased.NumpyBasedTraceStep.CalculateRanges)
    - [M CalculateMaskForRange ](#traceAnalysisAPI.arraybased.NumpyBasedTraceStep.CalculateMaskForRange)
    - [M GetParameterPanel ](#traceAnalysisAPI.arraybased.NumpyBasedTraceStep.GetParameterPanel)
- [ SignalDefinition ](#signaldefinition)
  - [C traceAnalysisAPI.arraybased.SignalDefinition ](#traceAnalysisAPI.arraybased.SignalDefinition)
    - [M `\_\_init\_\_` ](#traceAnalysisAPI.arraybased.SignalDefinition.__init__)
- [ ParameterDefinition ](#parameterdefinition)
  - [C traceAnalysisAPI.arraybased.ParameterDefinition ](#traceAnalysisAPI.arraybased.ParameterDefinition)
    - [M `\_\_init\_\_` ](#traceAnalysisAPI.arraybased.ParameterDefinition.__init__)
- [ Report ](#report)
  - [C traceAnalysisAPI.arraybased.Report ](#traceAnalysisAPI.arraybased.Report)
    - [M ImageFromBytes ](#traceAnalysisAPI.arraybased.Report.ImageFromBytes)
    - [M AddResultColumn ](#traceAnalysisAPI.arraybased.Report.AddResultColumn)
    - [M GetResultId ](#traceAnalysisAPI.arraybased.Report.GetResultId)
    - [M Image ](#traceAnalysisAPI.arraybased.Report.Image)
    - [M Log ](#traceAnalysisAPI.arraybased.Report.Log)
    - [M LogDebug ](#traceAnalysisAPI.arraybased.Report.LogDebug)
    - [M LogError ](#traceAnalysisAPI.arraybased.Report.LogError)
    - [M LogInfo ](#traceAnalysisAPI.arraybased.Report.LogInfo)
    - [M LogWarning ](#traceAnalysisAPI.arraybased.Report.LogWarning)
    - [M SetLogComponent ](#traceAnalysisAPI.arraybased.Report.SetLogComponent)
    - [M SetResultError ](#traceAnalysisAPI.arraybased.Report.SetResultError)
    - [M SetResultFailed ](#traceAnalysisAPI.arraybased.Report.SetResultFailed)
    - [M SetResultId ](#traceAnalysisAPI.arraybased.Report.SetResultId)
    - [M SetResultInconclusive ](#traceAnalysisAPI.arraybased.Report.SetResultInconclusive)
    - [M SetResultSuccess ](#traceAnalysisAPI.arraybased.Report.SetResultSuccess)
    - [M SetResultText ](#traceAnalysisAPI.arraybased.Report.SetResultText)
    - [M Table ](#traceAnalysisAPI.arraybased.Report.Table)
    - [M UpdateResultId ](#traceAnalysisAPI.arraybased.Report.UpdateResultId)
- [ TriggerRange ](#triggerrange)
  - [C traceAnalysisAPI.arraybased.TriggerRange ](#traceAnalysisAPI.arraybased.TriggerRange)
    - [M ImageFromBytes ](#traceAnalysisAPI.arraybased.TriggerRange.ImageFromBytes)
    - [M GetRelativeTimestamps ](#traceAnalysisAPI.arraybased.TriggerRange.GetRelativeTimestamps)
    - [M GetResultId ](#traceAnalysisAPI.arraybased.TriggerRange.GetResultId)
    - [M GetSlice ](#traceAnalysisAPI.arraybased.TriggerRange.GetSlice)
    - [M GetStartTime ](#traceAnalysisAPI.arraybased.TriggerRange.GetStartTime)
    - [M GetStartValue ](#traceAnalysisAPI.arraybased.TriggerRange.GetStartValue)
    - [M GetStopTime ](#traceAnalysisAPI.arraybased.TriggerRange.GetStopTime)
    - [M GetStopValue ](#traceAnalysisAPI.arraybased.TriggerRange.GetStopValue)
    - [M GetTimestamps ](#traceAnalysisAPI.arraybased.TriggerRange.GetTimestamps)
    - [M GetValues ](#traceAnalysisAPI.arraybased.TriggerRange.GetValues)
    - [M Image ](#traceAnalysisAPI.arraybased.TriggerRange.Image)
    - [M IsWholeTrace ](#traceAnalysisAPI.arraybased.TriggerRange.IsWholeTrace)
    - [M Range ](#traceAnalysisAPI.arraybased.TriggerRange.Range)
    - [M SetResultError ](#traceAnalysisAPI.arraybased.TriggerRange.SetResultError)
    - [M SetResultFailed ](#traceAnalysisAPI.arraybased.TriggerRange.SetResultFailed)
    - [M SetResultId ](#traceAnalysisAPI.arraybased.TriggerRange.SetResultId)
    - [M SetResultInconclusive ](#traceAnalysisAPI.arraybased.TriggerRange.SetResultInconclusive)
    - [M SetResultNone ](#traceAnalysisAPI.arraybased.TriggerRange.SetResultNone)
    - [M SetResultSuccess ](#traceAnalysisAPI.arraybased.TriggerRange.SetResultSuccess)
    - [M SetResultText ](#traceAnalysisAPI.arraybased.TriggerRange.SetResultText)
    - [M Spot ](#traceAnalysisAPI.arraybased.TriggerRange.Spot)
    - [M Table ](#traceAnalysisAPI.arraybased.TriggerRange.Table)
    - [M UpdateResultId ](#traceAnalysisAPI.arraybased.TriggerRange.UpdateResultId)
- [ Signal ](#signal)
  - [C traceAnalysisAPI.arraybased.Signal ](#traceAnalysisAPI.arraybased.Signal)
    - [M Emit ](#traceAnalysisAPI.arraybased.Signal.Emit)
    - [M GetGenericName ](#traceAnalysisAPI.arraybased.Signal.GetGenericName)
    - [M GetInterpolatedValues ](#traceAnalysisAPI.arraybased.Signal.GetInterpolatedValues)
    - [M GetMappingItemName ](#traceAnalysisAPI.arraybased.Signal.GetMappingItemName)
    - [M GetRecordingInfo ](#traceAnalysisAPI.arraybased.Signal.GetRecordingInfo)
    - [M GetTextTable ](#traceAnalysisAPI.arraybased.Signal.GetTextTable)
    - [M GetTimestamps ](#traceAnalysisAPI.arraybased.Signal.GetTimestamps)
    - [M GetTraceFileSignalName ](#traceAnalysisAPI.arraybased.Signal.GetTraceFileSignalName)
    - [M GetUnit ](#traceAnalysisAPI.arraybased.Signal.GetUnit)
    - [M GetValueAt ](#traceAnalysisAPI.arraybased.Signal.GetValueAt)
    - [M GetValues ](#traceAnalysisAPI.arraybased.Signal.GetValues)
    - [M IsBound ](#traceAnalysisAPI.arraybased.Signal.IsBound)
    - [M IsFound ](#traceAnalysisAPI.arraybased.Signal.IsFound)
    - [M IsOutSignal ](#traceAnalysisAPI.arraybased.Signal.IsOutSignal)
- [ RecordingInfo ](#recordinginfo)
  - [C traceAnalysisAPI.arraybased.RecordingInfo ](#traceAnalysisAPI.arraybased.RecordingInfo)
    - [M GetFirstPath ](#traceAnalysisAPI.arraybased.RecordingInfo.GetFirstPath)
    - [M GetPath ](#traceAnalysisAPI.arraybased.RecordingInfo.GetPath)
    - [M GetPathList ](#traceAnalysisAPI.arraybased.RecordingInfo.GetPathList)
    - [M GetRecordingName ](#traceAnalysisAPI.arraybased.RecordingInfo.GetRecordingName)
    - [M GetRecordingNumber ](#traceAnalysisAPI.arraybased.RecordingInfo.GetRecordingNumber)
    - [M GetRecordingType ](#traceAnalysisAPI.arraybased.RecordingInfo.GetRecordingType)
    - [M GetStartTimeNs ](#traceAnalysisAPI.arraybased.RecordingInfo.GetStartTimeNs)
- [ ReportTable ](#reporttable)
  - [C traceAnalysisAPI.arraybased.ReportTable ](#traceAnalysisAPI.arraybased.ReportTable)
    - [M AddRow ](#traceAnalysisAPI.arraybased.ReportTable.AddRow)
    - [M SetHeader ](#traceAnalysisAPI.arraybased.ReportTable.SetHeader)

# Array-based NumPy trace step templates[¶](#array-based-numpy-trace-step-templates "Link to this heading")

## NumpyBasedTraceStep[¶](#numpybasedtracestep "Link to this heading")

*class* traceAnalysisAPI.arraybased.NumpyBasedTraceStep[¶](#traceAnalysisAPI.arraybased.NumpyBasedTraceStep "Link to this definition")  
*abstractmethod static* GetInterfaceRevision()[¶](#traceAnalysisAPI.arraybased.NumpyBasedTraceStep.GetInterfaceRevision "Link to this definition")  
Returns the interface revision of the trace step template.

Note:  
This method is auto-generated for new implementations of NumpyBasedTraceStep. So do not delete or modify this method!

Return type:  int

Info

**Interface method:** Has to be overridden by child class.

*classmethod* GetDescription()[¶](#traceAnalysisAPI.arraybased.NumpyBasedTraceStep.GetDescription "Link to this definition")  
Returns the description of the trace step.

Return type:  str

Info

**Interface method:** Can be overridden by child class.

*abstractmethod classmethod* GetSignals()[¶](#traceAnalysisAPI.arraybased.NumpyBasedTraceStep.GetSignals "Link to this definition")  
Returns the incoming and outgoing signals of the trace step.

Return type:  list[[SignalDefinition](#traceAnalysisAPI.arraybased.SignalDefinition "traceAnalysisAPI.arraybased.SignalDefinition (Python class) — Definition of an incoming or outgoing signal of the trace step.")]

Info

**Interface method:** Has to be overridden by child class in order  
to use signals in trace step template.

*classmethod* GetParameters()[¶](#traceAnalysisAPI.arraybased.NumpyBasedTraceStep.GetParameters "Link to this definition")  
Returns the input and return parameters of the trace step.

Return type:  list[[ParameterDefinition](#traceAnalysisAPI.arraybased.ParameterDefinition "traceAnalysisAPI.arraybased.ParameterDefinition (Python class) — Definition of an input or return parameter of the trace step.")]

Info

**Interface method:** Has to be overridden by child class in order  
to use parameters in trace step template.

*classmethod* GetTimeAxisDefinition()[¶](#traceAnalysisAPI.arraybased.NumpyBasedTraceStep.GetTimeAxisDefinition "Link to this definition")  
Returns how the common time axis is determined. Only the logical operators **and** and **or** as well as references to the time axes of the signals by using the signal name are permitted. The use of brackets is allowed.

Note:  
If a signal is not defined on the common time axis, its value is determined according to its interpolation rule.

Returns:  Convention for building the common time axis (e.g. **‘Sig1 or Sig2’**). If an empty string is returned, all time axes are merged into one common time axis. This corresponds to an OR concatenation of the individual time axes.

Return type:  str

Info

**Interface method:** Can be overridden by child class.

Check(*[parameters](#traceAnalysisAPI.arraybased.NumpyBasedTraceStep.Check.parameters "traceAnalysisAPI.arraybased.NumpyBasedTraceStep.Check.parameters (Python parameter) — Dictionary of parameter values.")*)[¶](#traceAnalysisAPI.arraybased.NumpyBasedTraceStep.Check "Link to this definition")  
Is called initially before trace analysis execution and should check the parameterization. In case of error, raise a TypeError or ValueError.

Parameters:  parameters : dict[str, object][¶](#traceAnalysisAPI.arraybased.NumpyBasedTraceStep.Check.parameters "Permalink to this definition")  
Dictionary of parameter values.

Raises:  
- **TypeError** – Invalid type of a parameter.

- **ValueError** – Invalid value of a parameter.

Info

**Interface method:** Should be overridden by child class.

*abstractmethod* Process(*[parameters](#traceAnalysisAPI.arraybased.NumpyBasedTraceStep.Process.parameters "traceAnalysisAPI.arraybased.NumpyBasedTraceStep.Process.parameters (Python parameter) — Dictionary of parameter values.")*, *[report](#traceAnalysisAPI.arraybased.NumpyBasedTraceStep.Process.report "traceAnalysisAPI.arraybased.NumpyBasedTraceStep.Process.report (Python parameter) — The report object.")*, *[timeAxis](#traceAnalysisAPI.arraybased.NumpyBasedTraceStep.Process.timeAxis "traceAnalysisAPI.arraybased.NumpyBasedTraceStep.Process.timeAxis (Python parameter) — The common time axis of the signals over the entire trace.")*, *[ranges](#traceAnalysisAPI.arraybased.NumpyBasedTraceStep.Process.ranges "traceAnalysisAPI.arraybased.NumpyBasedTraceStep.Process.ranges (Python parameter) — List of trigger ranges.")*, *[signals](#traceAnalysisAPI.arraybased.NumpyBasedTraceStep.Process.signals "traceAnalysisAPI.arraybased.NumpyBasedTraceStep.Process.signals (Python parameter) — Dictionary of signals.")*)[¶](#traceAnalysisAPI.arraybased.NumpyBasedTraceStep.Process "Link to this definition")  
Method for executing the trace step template. Calculations can be performed based on the given signal values and their results can be stored in outgoing signals. Evaluation results and return parameters can be set.

Note:  
It is recommended to evaluate over the given trigger ranges and set the result for each trigger range. The overall result will be automatically determined.

It is possible to manually set the overall result using the [`Report`](#traceAnalysisAPI.arraybased.Report "traceAnalysisAPI.arraybased.Report (Python class) — This class represents the overall report of the trace step.") object; the automatic mechanism will be deactivated if used.

Detailed spots are also reported on trigger ranges.

Note:  
Access to values: All signal values within a trigger range can be accessed by its [`TriggerRange`](#traceAnalysisAPI.arraybased.TriggerRange "traceAnalysisAPI.arraybased.TriggerRange (Python class) — Representation of a trigger range. Contains timestamps and values of signals on the common time axis within the range as well as report information of a trigger range.") object. Alternatively, all values of a signal can be accessed by the [`Signal`](#traceAnalysisAPI.arraybased.Signal "traceAnalysisAPI.arraybased.Signal (Python class) — A signal provides access to meta information, such as the physical unit. You can also access the specific time axis of the signal and the corresponding signal values. For outgoing signals the method Emit() can be called to set timestamps and values.") object.

Note:  
To store calculated values in an outgoing signal the [`Signal`](#traceAnalysisAPI.arraybased.Signal "traceAnalysisAPI.arraybased.Signal (Python class) — A signal provides access to meta information, such as the physical unit. You can also access the specific time axis of the signal and the corresponding signal values. For outgoing signals the method Emit() can be called to set timestamps and values.") object is used: Signal.Emit(timestamps, values)

Parameters:  parameters : dict[str, object][¶](#traceAnalysisAPI.arraybased.NumpyBasedTraceStep.Process.parameters "Permalink to this definition")  
Dictionary of parameter values.

report[¶](#traceAnalysisAPI.arraybased.NumpyBasedTraceStep.Process.report "Permalink to this definition")  
The report object.

timeAxis : numpy.ndarray[¶](#traceAnalysisAPI.arraybased.NumpyBasedTraceStep.Process.timeAxis "Permalink to this definition")  
The common time axis of the signals over the entire trace. A limitation to the trigger ranges can be provided by a [`TriggerRange`](#traceAnalysisAPI.arraybased.TriggerRange "traceAnalysisAPI.arraybased.TriggerRange (Python class) — Representation of a trigger range. Contains timestamps and values of signals on the common time axis within the range as well as report information of a trigger range.") object.

ranges : list[[TriggerRange](#traceAnalysisAPI.arraybased.TriggerRange "traceAnalysisAPI.arraybased.TriggerRange (Python class) — Representation of a trigger range. Contains timestamps and values of signals on the common time axis within the range as well as report information of a trigger range.")][¶](#traceAnalysisAPI.arraybased.NumpyBasedTraceStep.Process.ranges "Permalink to this definition")  
List of trigger ranges.

signals[¶](#traceAnalysisAPI.arraybased.NumpyBasedTraceStep.Process.signals "Permalink to this definition")  
Dictionary of signals.

Info

**Interface method:** Has to be overridden by child class.

*static* FitToAxis(*[timestamps](#traceAnalysisAPI.arraybased.NumpyBasedTraceStep.FitToAxis.timestamps "traceAnalysisAPI.arraybased.NumpyBasedTraceStep.FitToAxis.timestamps (Python parameter) — Time axis of the signal.")*, *[values](#traceAnalysisAPI.arraybased.NumpyBasedTraceStep.FitToAxis.values "traceAnalysisAPI.arraybased.NumpyBasedTraceStep.FitToAxis.values (Python parameter) — Values of the signal.")*, *[targetTimeArray](#traceAnalysisAPI.arraybased.NumpyBasedTraceStep.FitToAxis.targetTimeArray "traceAnalysisAPI.arraybased.NumpyBasedTraceStep.FitToAxis.targetTimeArray (Python parameter) — Target time axis.")*, *[leftFillValue](#traceAnalysisAPI.arraybased.NumpyBasedTraceStep.FitToAxis.leftFillValue "traceAnalysisAPI.arraybased.NumpyBasedTraceStep.FitToAxis.leftFillValue (Python parameter) — Values before the first sample of the signal are defined by this value.")=`None`*, *[rightFillValue](#traceAnalysisAPI.arraybased.NumpyBasedTraceStep.FitToAxis.rightFillValue "traceAnalysisAPI.arraybased.NumpyBasedTraceStep.FitToAxis.rightFillValue (Python parameter) — Values after the last sample of the signal are defined by this value.")=`None`*)[¶](#traceAnalysisAPI.arraybased.NumpyBasedTraceStep.FitToAxis "Link to this definition")  
Maps a signal to a target time axis. Interpolates between timestamps using sample-and-hold if necessary.

Parameters:  timestamps : numpy.ndarray[¶](#traceAnalysisAPI.arraybased.NumpyBasedTraceStep.FitToAxis.timestamps "Permalink to this definition")  
Time axis of the signal.

values : numpy.ndarray[¶](#traceAnalysisAPI.arraybased.NumpyBasedTraceStep.FitToAxis.values "Permalink to this definition")  
Values of the signal.

targetTimeArray : numpy.ndarray[¶](#traceAnalysisAPI.arraybased.NumpyBasedTraceStep.FitToAxis.targetTimeArray "Permalink to this definition")  
Target time axis.

leftFillValue : object[¶](#traceAnalysisAPI.arraybased.NumpyBasedTraceStep.FitToAxis.leftFillValue "Permalink to this definition")  
Values before the first sample of the signal are defined by this value. If None, numpy.NAN is used. If values is a Boolean array and any numpy.NAN is applied the resulting array will be converted from bool to float!

rightFillValue : object[¶](#traceAnalysisAPI.arraybased.NumpyBasedTraceStep.FitToAxis.rightFillValue "Permalink to this definition")  
Values after the last sample of the signal are defined by this value. If None, the last signal value is used.

Returns:  Value array containing the signal values mapped to targetTimeArray.

Return type:  numpy.ndarray

*static* CalculateRanges(*[boolArray](#traceAnalysisAPI.arraybased.NumpyBasedTraceStep.CalculateRanges.boolArray "traceAnalysisAPI.arraybased.NumpyBasedTraceStep.CalculateRanges.boolArray (Python parameter) — Array containing truth values.")*)[¶](#traceAnalysisAPI.arraybased.NumpyBasedTraceStep.CalculateRanges "Link to this definition")  
Searches boolArray for ‘True ranges’ and ‘False ranges’ and creates ‘from-to-tuples’.

Parameters:  boolArray : numpy.ndarray[¶](#traceAnalysisAPI.arraybased.NumpyBasedTraceStep.CalculateRanges.boolArray "Permalink to this definition")  
Array containing truth values.

Returns:  List with a (start, stop, truth value) tuple per range.

Return type:  list[tuple[int, int, bool]]

*static* CalculateMaskForRange(*[array](#traceAnalysisAPI.arraybased.NumpyBasedTraceStep.CalculateMaskForRange.array "traceAnalysisAPI.arraybased.NumpyBasedTraceStep.CalculateMaskForRange.array (Python parameter) — The value array.")*, *[minVal](#traceAnalysisAPI.arraybased.NumpyBasedTraceStep.CalculateMaskForRange.minVal "traceAnalysisAPI.arraybased.NumpyBasedTraceStep.CalculateMaskForRange.minVal (Python parameter) — The minimum value to be included in the new array.")=`None`*, *[maxVal](#traceAnalysisAPI.arraybased.NumpyBasedTraceStep.CalculateMaskForRange.maxVal "traceAnalysisAPI.arraybased.NumpyBasedTraceStep.CalculateMaskForRange.maxVal (Python parameter) — The maximum value to be included in the new array.")=`None`*, *[leftOpen](#traceAnalysisAPI.arraybased.NumpyBasedTraceStep.CalculateMaskForRange.leftOpen "traceAnalysisAPI.arraybased.NumpyBasedTraceStep.CalculateMaskForRange.leftOpen (Python parameter) — If False (default), the left interval limit, defined by minVal, is left closed.")=`False`*, *[rightOpen](#traceAnalysisAPI.arraybased.NumpyBasedTraceStep.CalculateMaskForRange.rightOpen "traceAnalysisAPI.arraybased.NumpyBasedTraceStep.CalculateMaskForRange.rightOpen (Python parameter) — If False (default), the right interval limit, defined by maxVal, is right closed.")=`False`*)[¶](#traceAnalysisAPI.arraybased.NumpyBasedTraceStep.CalculateMaskForRange "Link to this definition")  
Calculate a mask that fits all values that are in the interval [minVal, maxVal]. Both minVal and maxVal are optional.The interval is closed per default. The parameters leftOpen and rightOpen can be used to change this behavior.

Note:  
This method can be used to calculate the mask for a signal’s time axis which then is applied to the signal values to get all values in a given time range.

Note:  
There is no special handling for NaN values. Avoid NaNs by masking beforehand. There will be a RuntimeWarning if the array contains NaNs.

Parameters:  array : numpy.ndarray[¶](#traceAnalysisAPI.arraybased.NumpyBasedTraceStep.CalculateMaskForRange.array "Permalink to this definition")  
The value array.

minVal : int|float[¶](#traceAnalysisAPI.arraybased.NumpyBasedTraceStep.CalculateMaskForRange.minVal "Permalink to this definition")  
The minimum value to be included in the new array.

maxVal : int|float[¶](#traceAnalysisAPI.arraybased.NumpyBasedTraceStep.CalculateMaskForRange.maxVal "Permalink to this definition")  
The maximum value to be included in the new array.

leftOpen : bool[¶](#traceAnalysisAPI.arraybased.NumpyBasedTraceStep.CalculateMaskForRange.leftOpen "Permalink to this definition")  
If False (default), the left interval limit, defined by minVal, is left closed. This means that values greater than or equal minVal are masked valid. If True, the left interval limit is left opened and only values greater than minVal are masked valid.

rightOpen : bool[¶](#traceAnalysisAPI.arraybased.NumpyBasedTraceStep.CalculateMaskForRange.rightOpen "Permalink to this definition")  
If False (default), the right interval limit, defined by maxVal, is right closed. This means that values less than or equal maxVal are masked valid. If True, the right interval limit is right opened and only values less than maxVal are masked valid.

Returns:  The mask

Return type:  numpy.ndarray

*static* GetParameterPanel(*[parent](#traceAnalysisAPI.arraybased.NumpyBasedTraceStep.GetParameterPanel "traceAnalysisAPI.arraybased.NumpyBasedTraceStep.GetParameterPanel.parent (Python parameter)")*)[¶](#traceAnalysisAPI.arraybased.NumpyBasedTraceStep.GetParameterPanel "Link to this definition")  
This method can be implemented to create a custom parameterization panel for the trace step dialog. It is designated to edit trace step parameters (no signals). The panel must inherit from wx.Panel or any subclass, and must implement the methods of the interface ‘ParameterPanel’ (no inheritance required). See TraceanalysisAPI documentation section ‘Custom GUI for parameters’ for more information.

Note:  
Keep imports of GUI frameworks locally, please.

Returns:  Returns a subclass of wx.Panel that implements the methods defined by the interface of ParameterPanel. The return value can be None if no custom GUI is defined.

Return type:  wx.Panel

Info

**Interface method:** Can be overridden by child class.

## SignalDefinition[¶](#signaldefinition "Link to this heading")

*class* traceAnalysisAPI.arraybased.SignalDefinition[¶](#traceAnalysisAPI.arraybased.SignalDefinition "Link to this definition")  
Definition of an incoming or outgoing signal of the trace step.

`\_\_init\_\_`(*[name](#traceAnalysisAPI.arraybased.SignalDefinition.__init__.name "traceAnalysisAPI.arraybased.SignalDefinition.__init__.name (Python parameter) — Name of the signal.")*, *[direction](#traceAnalysisAPI.arraybased.SignalDefinition.__init__.direction "traceAnalysisAPI.arraybased.SignalDefinition.__init__.direction (Python parameter) — Direction of the signal: 'IN', 'OUT'.")*, *[optional](#traceAnalysisAPI.arraybased.SignalDefinition.__init__.optional "traceAnalysisAPI.arraybased.SignalDefinition.__init__.optional (Python parameter) — This parameter only applies to signals with direction IN.")=`False`*, *[description](#traceAnalysisAPI.arraybased.SignalDefinition.__init__.description "traceAnalysisAPI.arraybased.SignalDefinition.__init__.description (Python parameter) — Description of the signal.")=`''`*)[¶](#traceAnalysisAPI.arraybased.SignalDefinition.__init__ "Link to this definition")  
Parameters:  name : str[¶](#traceAnalysisAPI.arraybased.SignalDefinition.__init__.name "Permalink to this definition")  
Name of the signal. Must be a valid Python identifier.

direction : str[¶](#traceAnalysisAPI.arraybased.SignalDefinition.__init__.direction "Permalink to this definition")  
Direction of the signal: ‘IN’, ‘OUT’.

optional : bool[¶](#traceAnalysisAPI.arraybased.SignalDefinition.__init__.optional "Permalink to this definition")  
This parameter only applies to signals with direction IN. OUT signals will always be optional. If True, the signal is optional. When using the trace step, it is allowed that the signal is not assigned or not found in the trace or no trace is given.

description : str[¶](#traceAnalysisAPI.arraybased.SignalDefinition.__init__.description "Permalink to this definition")  
Description of the signal.

## ParameterDefinition[¶](#parameterdefinition "Link to this heading")

*class* traceAnalysisAPI.arraybased.ParameterDefinition[¶](#traceAnalysisAPI.arraybased.ParameterDefinition "Link to this definition")  
Definition of an input or return parameter of the trace step.

`\_\_init\_\_`(*[name](#traceAnalysisAPI.arraybased.ParameterDefinition.__init__.name "traceAnalysisAPI.arraybased.ParameterDefinition.__init__.name (Python parameter) — Name of the parameter.")*, *[direction](#traceAnalysisAPI.arraybased.ParameterDefinition.__init__.direction "traceAnalysisAPI.arraybased.ParameterDefinition.__init__.direction (Python parameter) — Direction of the parameter: 'IN', 'OUT'.")*, *[default](#traceAnalysisAPI.arraybased.ParameterDefinition.__init__.default "traceAnalysisAPI.arraybased.ParameterDefinition.__init__.default (Python parameter) — Default value if no parameter value (value None) is specified when used.")=`None`*, *[description](#traceAnalysisAPI.arraybased.ParameterDefinition.__init__.description "traceAnalysisAPI.arraybased.ParameterDefinition.__init__.description (Python parameter) — Description of the parameter.")=`''`*)[¶](#traceAnalysisAPI.arraybased.ParameterDefinition.__init__ "Link to this definition")  
Parameters:  name : str[¶](#traceAnalysisAPI.arraybased.ParameterDefinition.__init__.name "Permalink to this definition")  
Name of the parameter. Must be a valid Python identifier.

direction : str[¶](#traceAnalysisAPI.arraybased.ParameterDefinition.__init__.direction "Permalink to this definition")  
Direction of the parameter: ‘IN’, ‘OUT’.

default : object[¶](#traceAnalysisAPI.arraybased.ParameterDefinition.__init__.default "Permalink to this definition")  
Default value if no parameter value (value None) is specified when used.

description : str[¶](#traceAnalysisAPI.arraybased.ParameterDefinition.__init__.description "Permalink to this definition")  
Description of the parameter.

## Report[¶](#report "Link to this heading")

*class* traceAnalysisAPI.arraybased.Report[¶](#traceAnalysisAPI.arraybased.Report "Link to this definition")  
This class represents the overall report of the trace step.

Note:  
In general, results should be set on TriggerRanges. The overall result will be determined automatically. If you set the result via this class, the result is fixed and will not change even if a TriggerRange has a worse result.

ImageFromBytes(*[dataBytes](#traceAnalysisAPI.arraybased.Report.ImageFromBytes.dataBytes "traceAnalysisAPI.arraybased.Report.ImageFromBytes.dataBytes (Python parameter) — byte stream (see: https://docs.python.org/3.7/library/io.html and https://docs.python.org/3/library/stdtypes.html#bytes)")*, *[name](#traceAnalysisAPI.arraybased.Report.ImageFromBytes.name "traceAnalysisAPI.arraybased.Report.ImageFromBytes.name (Python parameter) — name of the image (e.g.")=`None`*, *[title](#traceAnalysisAPI.arraybased.Report.ImageFromBytes.title "traceAnalysisAPI.arraybased.Report.ImageFromBytes.title (Python parameter) — the image title")=`None`*)[¶](#traceAnalysisAPI.arraybased.Report.ImageFromBytes "Link to this definition")  
Parameters:  dataBytes : bytes[¶](#traceAnalysisAPI.arraybased.Report.ImageFromBytes.dataBytes "Permalink to this definition")  
byte stream (see: [https://docs.python.org/3.7/library/io.html](https://docs.python.org/3.7/library/io.html) and [https://docs.python.org/3/library/stdtypes.html#bytes](https://docs.python.org/3/library/stdtypes.html#bytes))

name : str[¶](#traceAnalysisAPI.arraybased.Report.ImageFromBytes.name "Permalink to this definition")  
name of the image (e.g. used as file name in html/json report)

title : str[¶](#traceAnalysisAPI.arraybased.Report.ImageFromBytes.title "Permalink to this definition")  
the image title

Info

**Deprecated:** Please use [`Report.Image()`](#traceAnalysisAPI.arraybased.Report.Image "traceAnalysisAPI.arraybased.Report.Image (Python method) — Adds the given image to the test report. If the image is not embedded in the test report, the file will be stored in the report folder. If there is already an image with the same name, the image files will be enumerated.") instead.

AddResultColumn(*[name](#traceAnalysisAPI.arraybased.Report.AddResultColumn.name "traceAnalysisAPI.arraybased.Report.AddResultColumn.name (Python parameter) — name of the new column"): str*) → None[¶](#traceAnalysisAPI.arraybased.Report.AddResultColumn "Link to this definition")  
Adds a new column with the given name to the result table. It is appended at the end of the table. Values can be inserted into this column by using the parameter “additionalInfo” of the methods `Spot()` and `Range()`. The entries in the list “additionalInfo” list are inserted into the additional result columns in sequence.

Parameters:  name : str[¶](#traceAnalysisAPI.arraybased.Report.AddResultColumn.name "Permalink to this definition")  
name of the new column

GetResultId() → int[¶](#traceAnalysisAPI.arraybased.Report.GetResultId "Link to this definition")  
Gets the current result id.

The result id passed to an earlier call to [`SetResultId()`](#traceAnalysisAPI.arraybased.Report.SetResultId "traceAnalysisAPI.arraybased.Report.SetResultId (Python method) — Sets the result id for the current trace step.") is returned. If [`SetResultId()`](#traceAnalysisAPI.arraybased.Report.SetResultId "traceAnalysisAPI.arraybased.Report.SetResultId (Python method) — Sets the result id for the current trace step.") wasn’t called before, `dataContainer.RESULT_ID_NONE` is returned.

Returns:  the result id

Return type:  int

Image(*[imageSource](#traceAnalysisAPI.arraybased.Report.Image.imageSource "traceAnalysisAPI.arraybased.Report.Image.imageSource (Python parameter) — The image source can be one of the following:"): str | Path | ImageInterface | ndarray | bytes*, *\**, *[name](#traceAnalysisAPI.arraybased.Report.Image.name "traceAnalysisAPI.arraybased.Report.Image.name (Python parameter) — The filename (with correct extension)."): str | None = `None`*, *[title](#traceAnalysisAPI.arraybased.Report.Image.title "traceAnalysisAPI.arraybased.Report.Image.title (Python parameter) — the image title"): str | None = `None`*, *[embedded](#traceAnalysisAPI.arraybased.Report.Image.embedded "traceAnalysisAPI.arraybased.Report.Image.embedded (Python parameter) — True, if the image file should be embedded in the test report, else the image file is stored in the test report folder."): bool = `False`*, *[limitPreviewSize](#traceAnalysisAPI.arraybased.Report.Image.limitPreviewSize "traceAnalysisAPI.arraybased.Report.Image.limitPreviewSize (Python parameter) — If True (default), the preview image shown in the report will be limited to a maximum size."): bool = `True`*, *[autoDelete](#traceAnalysisAPI.arraybased.Report.Image.autoDelete "traceAnalysisAPI.arraybased.Report.Image.autoDelete (Python parameter) — Only applicable if imageSource is a file path."): bool = `False`*, *[useTemp](#traceAnalysisAPI.arraybased.Report.Image.useTemp "traceAnalysisAPI.arraybased.Report.Image.useTemp (Python parameter) — Only applicable if imageSource is a file path."): bool = `True`*) → ReportImage[¶](#traceAnalysisAPI.arraybased.Report.Image "Link to this definition")  
Adds the given image to the test report. If the image is not embedded in the test report, the file will be stored in the report folder. If there is already an image with the same name, the image files will be enumerated.

Parameters:  imageSource : str|Path|Image|Frame|numpy.ndarray|bytes[¶](#traceAnalysisAPI.arraybased.Report.Image.imageSource "Permalink to this definition")  
The image source can be one of the following:

- an absolute file path

- an Image or Frame object

- a NumPy array in OpenCV style: shape is (height, width, 3) of type numpy.uint8, the three colors have the order BGR!

- bytes object with image data

name : str[¶](#traceAnalysisAPI.arraybased.Report.Image.name "Permalink to this definition")  
The filename (with correct extension). Will be used as filename if an image file is created in the report folder. If name is None and the source is a path or an Image or Frame, the name of the imageSource is used.

title : str[¶](#traceAnalysisAPI.arraybased.Report.Image.title "Permalink to this definition")  
the image title

embedded : bool[¶](#traceAnalysisAPI.arraybased.Report.Image.embedded "Permalink to this definition")  
True, if the image file should be embedded in the test report, else the image file is stored in the test report folder.

limitPreviewSize : bool[¶](#traceAnalysisAPI.arraybased.Report.Image.limitPreviewSize "Permalink to this definition")  
If True (default), the preview image shown in the report will be limited to a maximum size.

autoDelete : bool[¶](#traceAnalysisAPI.arraybased.Report.Image.autoDelete "Permalink to this definition")  
Only applicable if imageSource is a file path. True, if the image file should be automatically deleted, else False.

useTemp : bool[¶](#traceAnalysisAPI.arraybased.Report.Image.useTemp "Permalink to this definition")  
Only applicable if imageSource is a file path. True, if the image file should be copied into a temporary directory, False, if it should be used directly. Using a temporary copy might be necessary to avoid overriding the image before the final report gets assembled later on.

Log(*[level](#traceAnalysisAPI.arraybased.Report.Log.level "traceAnalysisAPI.arraybased.Report.Log.level (Python parameter) — log level")*, *[time](#traceAnalysisAPI.arraybased.Report.Log.time "traceAnalysisAPI.arraybased.Report.Log.time (Python parameter) — timestamp of the log message")*, *[message](#traceAnalysisAPI.arraybased.Report.Log.message "traceAnalysisAPI.arraybased.Report.Log.message (Python parameter) — log message or format string.")*, *\*[formatArgs](#traceAnalysisAPI.arraybased.Report.Log.formatArgs "traceAnalysisAPI.arraybased.Report.Log.formatArgs (Python parameter) — additional non-keyword arguments used when message is a format string")*, *\*\*[formatKwargs](#traceAnalysisAPI.arraybased.Report.Log.formatKwargs "traceAnalysisAPI.arraybased.Report.Log.formatKwargs (Python parameter) — additional keyword arguments used when message is a format string")*)[¶](#traceAnalysisAPI.arraybased.Report.Log "Link to this definition")  
Adds a log message to the trace analysis log file. Use [`SetLogComponent()`](#traceAnalysisAPI.arraybased.Report.SetLogComponent "traceAnalysisAPI.arraybased.Report.SetLogComponent (Python method) — Sets the component that will be used in logging entries created by calling log methods.") to set the component part of the log entry.

Parameters:  level : int[¶](#traceAnalysisAPI.arraybased.Report.Log.level "Permalink to this definition")  
log level

- report.LOG_LEVEL_DEBUG

- report.LOG_LEVEL_INFO

- report.LOG_LEVEL_WARNING

- report.LOG_LEVEL_ERROR

time : float[¶](#traceAnalysisAPI.arraybased.Report.Log.time "Permalink to this definition")  
timestamp of the log message

message : str[¶](#traceAnalysisAPI.arraybased.Report.Log.message "Permalink to this definition")  
log message or format string.

\*formatArgs[¶](#traceAnalysisAPI.arraybased.Report.Log.formatArgs "Permalink to this definition")  
additional non-keyword arguments used when message is a format string

\*\*formatKwargs[¶](#traceAnalysisAPI.arraybased.Report.Log.formatKwargs "Permalink to this definition")  
additional keyword arguments used when message is a format string

Note:  
The usage of a format string and its arguments is corresponding to [str.format](https://docs.python.org/2/library/stdtypes.html#str.format) (external link).

Example:

    report.Log(
        report.LOG_LEVEL_WARNING,
        1.3,
        "Signal exceeds threshold {1:f}! Value {0:.5f}",
        currentValue,
        myThreshold,
    )
    report.Log(
        report.LOG_LEVEL_ERROR,
        1.3,
        "Signal exceeds threshold {threshold:f}! Value {value:.5f}",
        threshold=myThreshold,
        value=currentValue,
    )

LogDebug(*[time](#traceAnalysisAPI.arraybased.Report.LogDebug "traceAnalysisAPI.arraybased.Report.LogDebug.time (Python parameter)")*, *[message](#traceAnalysisAPI.arraybased.Report.LogDebug "traceAnalysisAPI.arraybased.Report.LogDebug.message (Python parameter)")*, *\*[formatArgs](#traceAnalysisAPI.arraybased.Report.LogDebug "traceAnalysisAPI.arraybased.Report.LogDebug.formatArgs (Python parameter)")*, *\*\*[formatKwargs](#traceAnalysisAPI.arraybased.Report.LogDebug "traceAnalysisAPI.arraybased.Report.LogDebug.formatKwargs (Python parameter)")*)[¶](#traceAnalysisAPI.arraybased.Report.LogDebug "Link to this definition")  
Convenience method to add a debug log message. See [`Log()`](#traceAnalysisAPI.arraybased.Report.Log "traceAnalysisAPI.arraybased.Report.Log (Python method) — Adds a log message to the trace analysis log file. Use SetLogComponent() to set the component part of the log entry.") for further usage.

LogError(*[time](#traceAnalysisAPI.arraybased.Report.LogError "traceAnalysisAPI.arraybased.Report.LogError.time (Python parameter)")*, *[message](#traceAnalysisAPI.arraybased.Report.LogError "traceAnalysisAPI.arraybased.Report.LogError.message (Python parameter)")*, *\*[formatArgs](#traceAnalysisAPI.arraybased.Report.LogError "traceAnalysisAPI.arraybased.Report.LogError.formatArgs (Python parameter)")*, *\*\*[formatKwargs](#traceAnalysisAPI.arraybased.Report.LogError "traceAnalysisAPI.arraybased.Report.LogError.formatKwargs (Python parameter)")*)[¶](#traceAnalysisAPI.arraybased.Report.LogError "Link to this definition")  
Convenience method to add an error log message. See [`Log()`](#traceAnalysisAPI.arraybased.Report.Log "traceAnalysisAPI.arraybased.Report.Log (Python method) — Adds a log message to the trace analysis log file. Use SetLogComponent() to set the component part of the log entry.") for further usage.

LogInfo(*[time](#traceAnalysisAPI.arraybased.Report.LogInfo "traceAnalysisAPI.arraybased.Report.LogInfo.time (Python parameter)")*, *[message](#traceAnalysisAPI.arraybased.Report.LogInfo "traceAnalysisAPI.arraybased.Report.LogInfo.message (Python parameter)")*, *\*[formatArgs](#traceAnalysisAPI.arraybased.Report.LogInfo "traceAnalysisAPI.arraybased.Report.LogInfo.formatArgs (Python parameter)")*, *\*\*[formatKwargs](#traceAnalysisAPI.arraybased.Report.LogInfo "traceAnalysisAPI.arraybased.Report.LogInfo.formatKwargs (Python parameter)")*)[¶](#traceAnalysisAPI.arraybased.Report.LogInfo "Link to this definition")  
Convenience method to add an info log message. See [`Log()`](#traceAnalysisAPI.arraybased.Report.Log "traceAnalysisAPI.arraybased.Report.Log (Python method) — Adds a log message to the trace analysis log file. Use SetLogComponent() to set the component part of the log entry.") for further usage.

LogWarning(*[time](#traceAnalysisAPI.arraybased.Report.LogWarning "traceAnalysisAPI.arraybased.Report.LogWarning.time (Python parameter)")*, *[message](#traceAnalysisAPI.arraybased.Report.LogWarning "traceAnalysisAPI.arraybased.Report.LogWarning.message (Python parameter)")*, *\*[formatArgs](#traceAnalysisAPI.arraybased.Report.LogWarning "traceAnalysisAPI.arraybased.Report.LogWarning.formatArgs (Python parameter)")*, *\*\*[formatKwargs](#traceAnalysisAPI.arraybased.Report.LogWarning "traceAnalysisAPI.arraybased.Report.LogWarning.formatKwargs (Python parameter)")*)[¶](#traceAnalysisAPI.arraybased.Report.LogWarning "Link to this definition")  
Convenience method to add a warning log message. See [`Log()`](#traceAnalysisAPI.arraybased.Report.Log "traceAnalysisAPI.arraybased.Report.Log (Python method) — Adds a log message to the trace analysis log file. Use SetLogComponent() to set the component part of the log entry.") for further usage.

SetLogComponent(*[component](#traceAnalysisAPI.arraybased.Report.SetLogComponent.component "traceAnalysisAPI.arraybased.Report.SetLogComponent.component (Python parameter) — name of the component")*)[¶](#traceAnalysisAPI.arraybased.Report.SetLogComponent "Link to this definition")  
Sets the component that will be used in logging entries created by calling log methods.

Parameters:  component : str[¶](#traceAnalysisAPI.arraybased.Report.SetLogComponent.component "Permalink to this definition")  
name of the component

SetResultError()[¶](#traceAnalysisAPI.arraybased.Report.SetResultError "Link to this definition")  
Convenience method for report.SetResultId(report.RESULT_ID_ERROR)

SetResultFailed()[¶](#traceAnalysisAPI.arraybased.Report.SetResultFailed "Link to this definition")  
Convenience method for report.SetResultId(report.RESULT_ID_FAILED)

SetResultId(*[resultId](#traceAnalysisAPI.arraybased.Report.SetResultId.resultId "traceAnalysisAPI.arraybased.Report.SetResultId.resultId (Python parameter) — the result id to set")*)[¶](#traceAnalysisAPI.arraybased.Report.SetResultId "Link to this definition")  
Sets the result id for the current trace step.

The result id can be one of:

- report.RESULT_ID_NONE

- report.RESULT_ID_SUCCESS

- report.RESULT_ID_INCONCLUSIVE

- report.RESULT_ID_FAILED

- report.RESULT_ID_ERROR

The result id is set directly. It is not affected by earlier calls to [`SetResultId()`](#traceAnalysisAPI.arraybased.Report.SetResultId "traceAnalysisAPI.arraybased.Report.SetResultId (Python method) — Sets the result id for the current trace step.").

Example:

    report.SetResultId(report.RESULT_ID_ERROR)
    report.SetResultId(report.RESULT_ID_NONE)

    report.GetResultId() # this will result in report.RESULT_ID_NONE

Parameters:  resultId : result id[¶](#traceAnalysisAPI.arraybased.Report.SetResultId.resultId "Permalink to this definition")  
the result id to set

SetResultInconclusive()[¶](#traceAnalysisAPI.arraybased.Report.SetResultInconclusive "Link to this definition")  
Convenience method for report.SetResultId(report.RESULT_ID_INCONCLUSIVE)

SetResultSuccess()[¶](#traceAnalysisAPI.arraybased.Report.SetResultSuccess "Link to this definition")  
Convenience method for report.SetResultId(report.RESULT_ID_SUCCESS)

SetResultText(*[text](#traceAnalysisAPI.arraybased.Report.SetResultText.text "traceAnalysisAPI.arraybased.Report.SetResultText.text (Python parameter) — the text"): str | None*) → None[¶](#traceAnalysisAPI.arraybased.Report.SetResultText "Link to this definition")  
Sets a user-defined text for the result of the report.

Parameters:  text : str[¶](#traceAnalysisAPI.arraybased.Report.SetResultText.text "Permalink to this definition")  
the text

Table(*[tableId](#traceAnalysisAPI.arraybased.Report.Table.tableId "traceAnalysisAPI.arraybased.Report.Table.tableId (Python parameter) — id to identify the table"): str | int | None = `None`*, *[headerValues](#traceAnalysisAPI.arraybased.Report.Table.headerValues "traceAnalysisAPI.arraybased.Report.Table.headerValues (Python parameter) — iterable with the entries of the table header"): Iterable[str | int] | None = `None`*) → ReportTable[¶](#traceAnalysisAPI.arraybased.Report.Table "Link to this definition")  
Creates a table in the test report.

Example:

    table = report.Table("table1", ["time", "description"])
    table.AddRow(["1.3", "A rising edge detected"])
    table.AddRow(["3.8", "A falling edge detected"])

Parameters:  tableId : str[¶](#traceAnalysisAPI.arraybased.Report.Table.tableId "Permalink to this definition")  
id to identify the table

headerValues : iterable[¶](#traceAnalysisAPI.arraybased.Report.Table.headerValues "Permalink to this definition")  
iterable with the entries of the table header

Returns:  the report table object

Return type:  [`ReportTable`](#traceAnalysisAPI.arraybased.ReportTable "traceAnalysisAPI.arraybased.ReportTable (Python class) — A ReportTable object represents a table in the test report.")

UpdateResultId(*[resultId](#traceAnalysisAPI.arraybased.Report.UpdateResultId.resultId "traceAnalysisAPI.arraybased.Report.UpdateResultId.resultId (Python parameter) — the result id to set")*)[¶](#traceAnalysisAPI.arraybased.Report.UpdateResultId "Link to this definition")  
Updates the result id for the current trace step.

The result id can be one of:

- report.RESULT_ID_NONE

- report.RESULT_ID_SUCCESS

- report.RESULT_ID_INCONCLUSIVE

- report.RESULT_ID_FAILED

- report.RESULT_ID_ERROR

In contrast to [`SetResultId()`](#traceAnalysisAPI.arraybased.Report.SetResultId "traceAnalysisAPI.arraybased.Report.SetResultId (Python method) — Sets the result id for the current trace step."), which sets the resultId directly, [`UpdateResultId()`](#traceAnalysisAPI.arraybased.Report.UpdateResultId "traceAnalysisAPI.arraybased.Report.UpdateResultId (Python method) — Updates the result id for the current trace step.") can only increase the resultId according to the following ordering:

RESULT_ID_NONE \< RESULT_ID_SUCCESS \< RESULT_ID_INCONCLUSIVE \< RESULT_ID_FAILED \< RESULT_ID_ERROR

Info

[`UpdateResultId()`](#traceAnalysisAPI.arraybased.Report.UpdateResultId "traceAnalysisAPI.arraybased.Report.UpdateResultId (Python method) — Updates the result id for the current trace step.") can bee seen as equivalent to SetResultId(max(resultId, GetResultId()))

..example:

    report.UpdateResultId(report.RESULT_ID_SUCCESS)
    ...
    report.UpdateResultId(report.RESULT_ID_FAILED)
    ...
    report.UpdateResultId(report.RESULT_ID_SUCCESS)

    report.GetResultId() # this will result in report.RESULT_ID_FAILED

Parameters:  resultId : result id[¶](#traceAnalysisAPI.arraybased.Report.UpdateResultId.resultId "Permalink to this definition")  
the result id to set

## TriggerRange[¶](#triggerrange "Link to this heading")

*class* traceAnalysisAPI.arraybased.TriggerRange[¶](#traceAnalysisAPI.arraybased.TriggerRange "Link to this definition")  
Representation of a trigger range. Contains timestamps and values of signals on the common time axis within the range as well as report information of a trigger range.

ImageFromBytes(*[dataBytes](#traceAnalysisAPI.arraybased.TriggerRange.ImageFromBytes.dataBytes "traceAnalysisAPI.arraybased.TriggerRange.ImageFromBytes.dataBytes (Python parameter) — byte stream (see: https://docs.python.org/3.7/library/io.html and https://docs.python.org/3/library/stdtypes.html#bytes)"): bytes*, *[name](#traceAnalysisAPI.arraybased.TriggerRange.ImageFromBytes.name "traceAnalysisAPI.arraybased.TriggerRange.ImageFromBytes.name (Python parameter) — name of the image (e.g."): str | None = `None`*, *[title](#traceAnalysisAPI.arraybased.TriggerRange.ImageFromBytes.title "traceAnalysisAPI.arraybased.TriggerRange.ImageFromBytes.title (Python parameter) — the image title"): str | None = `None`*) → ReportImage[¶](#traceAnalysisAPI.arraybased.TriggerRange.ImageFromBytes "Link to this definition")  
Parameters:  dataBytes: bytes[¶](#traceAnalysisAPI.arraybased.TriggerRange.ImageFromBytes.dataBytes "Permalink to this definition")  
byte stream (see: [https://docs.python.org/3.7/library/io.html](https://docs.python.org/3.7/library/io.html) and [https://docs.python.org/3/library/stdtypes.html#bytes](https://docs.python.org/3/library/stdtypes.html#bytes))

name: str | None = `None`[¶](#traceAnalysisAPI.arraybased.TriggerRange.ImageFromBytes.name "Permalink to this definition")  
name of the image (e.g. used as file name in html/json report)

title: str | None = `None`[¶](#traceAnalysisAPI.arraybased.TriggerRange.ImageFromBytes.title "Permalink to this definition")  
the image title

Info

**Deprecated:** Please use [`TriggerRange.Image()`](#traceAnalysisAPI.arraybased.TriggerRange.Image "traceAnalysisAPI.arraybased.TriggerRange.Image (Python method) — Adds the given image to the test report. If the image is not embedded in the test report, the file will be stored in the report folder. If there is already an image with the same name, the image files will be enumerated.") instead.

GetRelativeTimestamps() → ndarray[¶](#traceAnalysisAPI.arraybased.TriggerRange.GetRelativeTimestamps "Link to this definition")  
Returns the timestamps of the common time axis within the trigger range relative to the start trigger time.

GetResultId() → int[¶](#traceAnalysisAPI.arraybased.TriggerRange.GetResultId "Link to this definition")  
Gets the current result id.

The result id passed to an earlier call to [`SetResultId()`](#traceAnalysisAPI.arraybased.TriggerRange.SetResultId "traceAnalysisAPI.arraybased.TriggerRange.SetResultId (Python method) — Sets the result id for the trigger range.") is returned. If [`SetResultId()`](#traceAnalysisAPI.arraybased.TriggerRange.SetResultId "traceAnalysisAPI.arraybased.TriggerRange.SetResultId (Python method) — Sets the result id for the trigger range.") wasn’t called before, `RESULT_ID_NONE` is returned.

Returns:  the result id

GetSlice() → slice[¶](#traceAnalysisAPI.arraybased.TriggerRange.GetSlice "Link to this definition")  
Returns a slice [from, to] that can be used to slice from arrays that are based on the main time axis.

GetStartTime() → float[¶](#traceAnalysisAPI.arraybased.TriggerRange.GetStartTime "Link to this definition")  
Returns the start time of the trigger range.

Note:  
The value can be different to the first sample of the common time axis or any signal time axis for the following cases:

- used in a trigger block that uses different signals

- not in a trigger block: The first sample of all signals of the episode will be taken.

Returns:  The start time or None if it could not be determined (e.g. no signal with samples)

GetStartValue(*[sigName](#traceAnalysisAPI.arraybased.TriggerRange.GetStartValue.sigName "traceAnalysisAPI.arraybased.TriggerRange.GetStartValue.sigName (Python parameter) — The regarded signal"): str*, *[deltaT](#traceAnalysisAPI.arraybased.TriggerRange.GetStartValue.deltaT "traceAnalysisAPI.arraybased.TriggerRange.GetStartValue.deltaT (Python parameter) — Offset to the start trigger timestamp."): float = `0.0`*) → Any[¶](#traceAnalysisAPI.arraybased.TriggerRange.GetStartValue "Link to this definition")  
Returns the value of the given signal at the timestamp of the start trigger plus deltaT.

Parameters:  sigName: str[¶](#traceAnalysisAPI.arraybased.TriggerRange.GetStartValue.sigName "Permalink to this definition")  
The regarded signal

deltaT: float = `0.0`[¶](#traceAnalysisAPI.arraybased.TriggerRange.GetStartValue.deltaT "Permalink to this definition")  
Offset to the start trigger timestamp.

GetStopTime() → float[¶](#traceAnalysisAPI.arraybased.TriggerRange.GetStopTime "Link to this definition")  
Returns the timestamp where the trigger range ends.

Note:  
This can be different to the last sample of the common time axis or any signal time axis for the following cases:

- used in a trigger block that uses different signals

- not in a trigger block: The first sample of all signals of the episode will be taken.

Note:  
There is no evaluation at the stop time. Exception: stop at end of trace.

Returns:  The stop time or None if it could not be determined (e.g. no signal with samples)

GetStopValue(*[sigName](#traceAnalysisAPI.arraybased.TriggerRange.GetStopValue.sigName "traceAnalysisAPI.arraybased.TriggerRange.GetStopValue.sigName (Python parameter) — The regarded signal"): str*, *[deltaT](#traceAnalysisAPI.arraybased.TriggerRange.GetStopValue.deltaT "traceAnalysisAPI.arraybased.TriggerRange.GetStopValue.deltaT (Python parameter) — Offset to the stop trigger timestamp."): float = `0.0`*) → Any[¶](#traceAnalysisAPI.arraybased.TriggerRange.GetStopValue "Link to this definition")  
Returns the value of the given signal at the timestamp of the stop trigger plus deltaT.

Parameters:  sigName: str[¶](#traceAnalysisAPI.arraybased.TriggerRange.GetStopValue.sigName "Permalink to this definition")  
The regarded signal

deltaT: float = `0.0`[¶](#traceAnalysisAPI.arraybased.TriggerRange.GetStopValue.deltaT "Permalink to this definition")  
Offset to the stop trigger timestamp.

GetTimestamps() → ndarray[¶](#traceAnalysisAPI.arraybased.TriggerRange.GetTimestamps "Link to this definition")  
Returns the timestamps of the common time axis within the trigger range.

GetValues(*[sigName](#traceAnalysisAPI.arraybased.TriggerRange.GetValues "traceAnalysisAPI.arraybased.TriggerRange.GetValues.sigName (Python parameter)"): str*) → ndarray[¶](#traceAnalysisAPI.arraybased.TriggerRange.GetValues "Link to this definition")  
Returns the values of a signal on the common time axis within the trigger range.

Image(*[imageSource](#traceAnalysisAPI.arraybased.TriggerRange.Image.imageSource "traceAnalysisAPI.arraybased.TriggerRange.Image.imageSource (Python parameter) — The image source can be one of the following:"): str | Path | ImageInterface | ndarray | bytes*, *\**, *[name](#traceAnalysisAPI.arraybased.TriggerRange.Image.name "traceAnalysisAPI.arraybased.TriggerRange.Image.name (Python parameter) — The filename (with correct extension)."): str | None = `None`*, *[title](#traceAnalysisAPI.arraybased.TriggerRange.Image.title "traceAnalysisAPI.arraybased.TriggerRange.Image.title (Python parameter) — the image title"): str | None = `None`*, *[embedded](#traceAnalysisAPI.arraybased.TriggerRange.Image.embedded "traceAnalysisAPI.arraybased.TriggerRange.Image.embedded (Python parameter) — True, if the image file should be embedded in the test report, else the image file is stored in the test report folder."): bool = `False`*, *[limitPreviewSize](#traceAnalysisAPI.arraybased.TriggerRange.Image.limitPreviewSize "traceAnalysisAPI.arraybased.TriggerRange.Image.limitPreviewSize (Python parameter) — If True (default), the preview image shown in the report will be limited to a maximum size."): bool = `True`*, *[autoDelete](#traceAnalysisAPI.arraybased.TriggerRange.Image.autoDelete "traceAnalysisAPI.arraybased.TriggerRange.Image.autoDelete (Python parameter) — Only applicable if imageSource is a file path."): bool = `False`*, *[useTemp](#traceAnalysisAPI.arraybased.TriggerRange.Image.useTemp "traceAnalysisAPI.arraybased.TriggerRange.Image.useTemp (Python parameter) — Only applicable if imageSource is a file path."): bool = `True`*) → ReportImage[¶](#traceAnalysisAPI.arraybased.TriggerRange.Image "Link to this definition")  
Adds the given image to the test report. If the image is not embedded in the test report, the file will be stored in the report folder. If there is already an image with the same name, the image files will be enumerated.

Parameters:  imageSource : str|Path|Image|Frame|numpy.ndarray|bytes[¶](#traceAnalysisAPI.arraybased.TriggerRange.Image.imageSource "Permalink to this definition")  
The image source can be one of the following:

- an absolute file path

- an Image or Frame object

- a NumPy array in OpenCV style: shape is (height, width, 3) of type numpy.uint8, the three colors have the order BGR!

- bytes object with image data

name : str[¶](#traceAnalysisAPI.arraybased.TriggerRange.Image.name "Permalink to this definition")  
The filename (with correct extension). Will be used as filename if an image file is created in the report folder. If name is None and the source is a path or an Image or Frame, the name of the imageSource is used.

title : str[¶](#traceAnalysisAPI.arraybased.TriggerRange.Image.title "Permalink to this definition")  
the image title

embedded : bool[¶](#traceAnalysisAPI.arraybased.TriggerRange.Image.embedded "Permalink to this definition")  
True, if the image file should be embedded in the test report, else the image file is stored in the test report folder.

limitPreviewSize : bool[¶](#traceAnalysisAPI.arraybased.TriggerRange.Image.limitPreviewSize "Permalink to this definition")  
If True (default), the preview image shown in the report will be limited to a maximum size.

autoDelete : bool[¶](#traceAnalysisAPI.arraybased.TriggerRange.Image.autoDelete "Permalink to this definition")  
Only applicable if imageSource is a file path. True, if the image file should be automatically deleted, else False.

useTemp : bool[¶](#traceAnalysisAPI.arraybased.TriggerRange.Image.useTemp "Permalink to this definition")  
Only applicable if imageSource is a file path. True, if the image file should be copied into a temporary directory, False, if it should be used directly. Using a temporary copy might be necessary to avoid overriding the image before the final report gets assembled later on.

IsWholeTrace() → bool[¶](#traceAnalysisAPI.arraybased.TriggerRange.IsWholeTrace "Link to this definition")  
Returns True if the trace step has no trigger block as ancestor. In this case there will only be one trigger range that represents the entire time domain of the trace analysis.

Correspondingly, if the trace step is contained in a trigger block, this method will return False for all trigger ranges.

Range(*[startTime](#traceAnalysisAPI.arraybased.TriggerRange.Range.startTime "traceAnalysisAPI.arraybased.TriggerRange.Range.startTime (Python parameter) — timestamp at which the sub range begins"): float*, *[stopTime](#traceAnalysisAPI.arraybased.TriggerRange.Range.stopTime "traceAnalysisAPI.arraybased.TriggerRange.Range.stopTime (Python parameter) — timestamp at which the sub range ends"): float*, *[message](#traceAnalysisAPI.arraybased.TriggerRange.Range.message "traceAnalysisAPI.arraybased.TriggerRange.Range.message (Python parameter) — a textual message describing the sub range"): str = `''`*, *[resultId](#traceAnalysisAPI.arraybased.TriggerRange.Range.resultId "traceAnalysisAPI.arraybased.TriggerRange.Range.resultId (Python parameter) — the verdict for the sub range"): int = `0`*, *[additionalInfo](#traceAnalysisAPI.arraybased.TriggerRange.Range.additionalInfo "traceAnalysisAPI.arraybased.TriggerRange.Range.additionalInfo (Python parameter) — a list of additional information, that will be shown in the custom result columns (see Report.AddResultColumn())"): list[str] | None = `None`*) → None[¶](#traceAnalysisAPI.arraybased.TriggerRange.Range "Link to this definition")  
Adds a sub range to the trigger range.

Parameters:  startTime: float[¶](#traceAnalysisAPI.arraybased.TriggerRange.Range.startTime "Permalink to this definition")  
timestamp at which the sub range begins

stopTime: float[¶](#traceAnalysisAPI.arraybased.TriggerRange.Range.stopTime "Permalink to this definition")  
timestamp at which the sub range ends

message: str = `''`[¶](#traceAnalysisAPI.arraybased.TriggerRange.Range.message "Permalink to this definition")  
a textual message describing the sub range

resultId: int = `0`[¶](#traceAnalysisAPI.arraybased.TriggerRange.Range.resultId "Permalink to this definition")  
the verdict for the sub range

additionalInfo: list[str] | None = `None`[¶](#traceAnalysisAPI.arraybased.TriggerRange.Range.additionalInfo "Permalink to this definition")  
a list of additional information, that will be shown in the custom result columns (see [`Report.AddResultColumn()`](#traceAnalysisAPI.arraybased.Report.AddResultColumn "traceAnalysisAPI.arraybased.Report.AddResultColumn (Python method) — Adds a new column with the given name to the result table. It is appended at the end of the table. Values can be inserted into this column by using the parameter "additionalInfo" of the methods Spot() and Range(). The entries in the list "additionalInfo" list are inserted into the additional result columns in sequence."))

SetResultError() → None[¶](#traceAnalysisAPI.arraybased.TriggerRange.SetResultError "Link to this definition")  
Convenience method for triggerRange.SetResultId(triggerRange.RESULT_ID_ERROR)

SetResultFailed() → None[¶](#traceAnalysisAPI.arraybased.TriggerRange.SetResultFailed "Link to this definition")  
Convenience method for triggerRange.SetResultId(triggerRange.RESULT_ID_FAILED)

SetResultId(*[resultId](#traceAnalysisAPI.arraybased.TriggerRange.SetResultId.resultId "traceAnalysisAPI.arraybased.TriggerRange.SetResultId.resultId (Python parameter) — the result id to set"): int*) → None[¶](#traceAnalysisAPI.arraybased.TriggerRange.SetResultId "Link to this definition")  
Sets the result id for the trigger range.

The result id can be one of:

- triggerRange.RESULT_ID_NONE

- triggerRange.RESULT_ID_SUCCESS

- triggerRange.RESULT_ID_INCONCLUSIVE

- triggerRange.RESULT_ID_FAILED

- triggerRange.RESULT_ID_ERROR

The result id is set directly. It is not affected by earlier calls to [`SetResultId()`](#traceAnalysisAPI.arraybased.TriggerRange.SetResultId "traceAnalysisAPI.arraybased.TriggerRange.SetResultId (Python method) — Sets the result id for the trigger range.").

Example:

    triggerRange.SetResultId(triggerRange.RESULT_ID_ERROR)
    triggerRange.SetResultId(triggerRange.RESULT_ID_NONE)

    triggerRange.GetResultId() # this will result in triggerRange.RESULT_ID_NONE

Parameters:  resultId: int[¶](#traceAnalysisAPI.arraybased.TriggerRange.SetResultId.resultId "Permalink to this definition")  
the result id to set

SetResultInconclusive() → None[¶](#traceAnalysisAPI.arraybased.TriggerRange.SetResultInconclusive "Link to this definition")  
Convenience method for triggerRange.SetResultId(triggerRange.RESULT_ID_INCONCLUSIVE)

SetResultNone() → None[¶](#traceAnalysisAPI.arraybased.TriggerRange.SetResultNone "Link to this definition")  
Convenience method for triggerRange.SetResultId(triggerRange.RESULT_ID_NONE)

SetResultSuccess() → None[¶](#traceAnalysisAPI.arraybased.TriggerRange.SetResultSuccess "Link to this definition")  
Convenience method for triggerRange.SetResultId(triggerRange.RESULT_ID_SUCCESS)

SetResultText(*[resultText](#traceAnalysisAPI.arraybased.TriggerRange.SetResultText.resultText "traceAnalysisAPI.arraybased.TriggerRange.SetResultText.resultText (Python parameter) — the text"): str | None*) → None[¶](#traceAnalysisAPI.arraybased.TriggerRange.SetResultText "Link to this definition")  
Sets a user-defined result text of the trigger range.

Parameters:  resultText: str | None[¶](#traceAnalysisAPI.arraybased.TriggerRange.SetResultText.resultText "Permalink to this definition")  
the text

Spot(*[time](#traceAnalysisAPI.arraybased.TriggerRange.Spot.time "traceAnalysisAPI.arraybased.TriggerRange.Spot.time (Python parameter) — timestamp of the spot"): float*, *[message](#traceAnalysisAPI.arraybased.TriggerRange.Spot.message "traceAnalysisAPI.arraybased.TriggerRange.Spot.message (Python parameter) — a textual message describing the spot"): str = `''`*, *[resultId](#traceAnalysisAPI.arraybased.TriggerRange.Spot.resultId "traceAnalysisAPI.arraybased.TriggerRange.Spot.resultId (Python parameter) — the verdict for the spot"): int = `0`*, *[additionalInfo](#traceAnalysisAPI.arraybased.TriggerRange.Spot.additionalInfo "traceAnalysisAPI.arraybased.TriggerRange.Spot.additionalInfo (Python parameter) — a list of additional information, that will be shown in the custom result columns (Report.AddResultColumn)"): list[str] | None = `None`*) → None[¶](#traceAnalysisAPI.arraybased.TriggerRange.Spot "Link to this definition")  
Adds a signal spot to the trigger range.

Parameters:  time: float[¶](#traceAnalysisAPI.arraybased.TriggerRange.Spot.time "Permalink to this definition")  
timestamp of the spot

message: str = `''`[¶](#traceAnalysisAPI.arraybased.TriggerRange.Spot.message "Permalink to this definition")  
a textual message describing the spot

resultId: int = `0`[¶](#traceAnalysisAPI.arraybased.TriggerRange.Spot.resultId "Permalink to this definition")  
the verdict for the spot

additionalInfo: list[str] | None = `None`[¶](#traceAnalysisAPI.arraybased.TriggerRange.Spot.additionalInfo "Permalink to this definition")  
a list of additional information, that will be shown in the custom result columns ([`Report.AddResultColumn`](#traceAnalysisAPI.arraybased.Report.AddResultColumn "traceAnalysisAPI.arraybased.Report.AddResultColumn (Python method) — Adds a new column with the given name to the result table. It is appended at the end of the table. Values can be inserted into this column by using the parameter "additionalInfo" of the methods Spot() and Range(). The entries in the list "additionalInfo" list are inserted into the additional result columns in sequence."))

Table(*[tableId](#traceAnalysisAPI.arraybased.TriggerRange.Table.tableId "traceAnalysisAPI.arraybased.TriggerRange.Table.tableId (Python parameter) — id to identify the table"): str | int | None = `None`*, *[headerValues](#traceAnalysisAPI.arraybased.TriggerRange.Table.headerValues "traceAnalysisAPI.arraybased.TriggerRange.Table.headerValues (Python parameter) — iterable with the entries of the table header"): Iterable[str | int] | None = `None`*) → ReportTable[¶](#traceAnalysisAPI.arraybased.TriggerRange.Table "Link to this definition")  
Creates a table in the test report.

Example:

    table = report.Table("table1", ["time", "description"])
    table.AddRow(["1.3", "A rising edge detected"])
    table.AddRow(["3.8", "A falling edge detected"])

Parameters:  tableId : str[¶](#traceAnalysisAPI.arraybased.TriggerRange.Table.tableId "Permalink to this definition")  
id to identify the table

headerValues : iterable[¶](#traceAnalysisAPI.arraybased.TriggerRange.Table.headerValues "Permalink to this definition")  
iterable with the entries of the table header

Returns:  the report table object

Return type:  [`ReportTable`](#traceAnalysisAPI.arraybased.ReportTable "traceAnalysisAPI.arraybased.ReportTable (Python class) — A ReportTable object represents a table in the test report.")

UpdateResultId(*[resultId](#traceAnalysisAPI.arraybased.TriggerRange.UpdateResultId.resultId "traceAnalysisAPI.arraybased.TriggerRange.UpdateResultId.resultId (Python parameter) — the result id to set"): int*) → None[¶](#traceAnalysisAPI.arraybased.TriggerRange.UpdateResultId "Link to this definition")  
Updates the result id for the trigger range.

The result id can be one of:

- triggerRange.RESULT_ID_NONE

- triggerRange.RESULT_ID_SUCCESS

- triggerRange.RESULT_ID_INCONCLUSIVE

- triggerRange.RESULT_ID_FAILED

- triggerRange.RESULT_ID_ERROR

In contrast to [`SetResultId()`](#traceAnalysisAPI.arraybased.TriggerRange.SetResultId "traceAnalysisAPI.arraybased.TriggerRange.SetResultId (Python method) — Sets the result id for the trigger range."), which sets the resultId directly, [`UpdateResultId()`](#traceAnalysisAPI.arraybased.TriggerRange.UpdateResultId "traceAnalysisAPI.arraybased.TriggerRange.UpdateResultId (Python method) — Updates the result id for the trigger range.") can only increase the resultId according to the following ordering:

RESULT_ID_NONE \< RESULT_ID_SUCCESS \< RESULT_ID_INCONCLUSIVE \< RESULT_ID_FAILED \< RESULT_ID_ERROR

Info

[`UpdateResultId()`](#traceAnalysisAPI.arraybased.TriggerRange.UpdateResultId "traceAnalysisAPI.arraybased.TriggerRange.UpdateResultId (Python method) — Updates the result id for the trigger range.") can bee seen as equivalent to SetResultId(max(resultId, GetResultId()))

Example

triggerRange.UpdateResultId(triggerRange.RESULT_ID_SUCCESS) … triggerRange.UpdateResultId(triggerRange.RESULT_ID_FAILED) … triggerRange.UpdateResultId(triggerRange.RESULT_ID_SUCCESS)

triggerRange.GetResultId() \# this will result in triggerRange.RESULT_ID_FAILED

Parameters:  resultId: int[¶](#traceAnalysisAPI.arraybased.TriggerRange.UpdateResultId.resultId "Permalink to this definition")  
the result id to set

## Signal[¶](#signal "Link to this heading")

*class* traceAnalysisAPI.arraybased.Signal[¶](#traceAnalysisAPI.arraybased.Signal "Link to this definition")  
A signal provides access to meta information, such as the physical unit. You can also access the specific time axis of the signal and the corresponding signal values. For outgoing signals the method Emit() can be called to set timestamps and values.

Emit(*[timestamps](#traceAnalysisAPI.arraybased.Signal.Emit.timestamps "traceAnalysisAPI.arraybased.Signal.Emit.timestamps (Python parameter) — Time axis of the signal."): ndarray*, *[values](#traceAnalysisAPI.arraybased.Signal.Emit.values "traceAnalysisAPI.arraybased.Signal.Emit.values (Python parameter) — Values of the signal."): ndarray*) → None[¶](#traceAnalysisAPI.arraybased.Signal.Emit "Link to this definition")  
Sets timestamps and values of an outgoing (calculated signal).

Parameters:  timestamps: ndarray[¶](#traceAnalysisAPI.arraybased.Signal.Emit.timestamps "Permalink to this definition")  
Time axis of the signal.

values: ndarray[¶](#traceAnalysisAPI.arraybased.Signal.Emit.values "Permalink to this definition")  
Values of the signal.

Raises:  
**ValueError** – Called on an incoming signal or with arrays of different length.

GetGenericName() → str[¶](#traceAnalysisAPI.arraybased.Signal.GetGenericName "Link to this definition")  
Returns the name of the generic signal this signal is bound to. If the signal is not bound, it will return an empty string.

GetInterpolatedValues() → ndarray | None[¶](#traceAnalysisAPI.arraybased.Signal.GetInterpolatedValues "Link to this definition")  
Returns the values interpolated on the common time axis of the trace step.

Returns:  The interpolated values. Will return None for outgoing signals!

GetMappingItemName() → str[¶](#traceAnalysisAPI.arraybased.Signal.GetMappingItemName "Link to this definition")  
Returns the name of the mapping item this signal relates to. If the signal is not bound or it is bound to a calculated signal, it will return an empty string.

GetRecordingInfo() → [RecordingInfo](#traceAnalysisAPI.arraybased.RecordingInfo "traceAnalysisAPI.arraybased.RecordingInfo (Python class) — A RecordingInfo object contains information about the name, number, type and path of the underlying recording from which the signal stems.") | None[¶](#traceAnalysisAPI.arraybased.Signal.GetRecordingInfo "Link to this definition")  
Returns the RecordingInfo of the assigned generic signal.

If the returned value is not None, the documented methods on the returned RecordingInfo object can be called to obtain further information.

Returns:  [`RecordingInfo`](#traceAnalysisAPI.arraybased.RecordingInfo "traceAnalysisAPI.arraybased.RecordingInfo (Python class) — A RecordingInfo object contains information about the name, number, type and path of the underlying recording from which the signal stems.") if the source of the assigned generic signal is a recording else None

GetTextTable() → tuple[Mapping[int, str] | None, str | None][¶](#traceAnalysisAPI.arraybased.Signal.GetTextTable "Link to this definition")  
Returns the text table and the default value of the signal as tuple.

GetTimestamps(*[fromTo](#traceAnalysisAPI.arraybased.Signal.GetTimestamps.fromTo "traceAnalysisAPI.arraybased.Signal.GetTimestamps.fromTo (Python parameter) — An optional tuple with timestamps (from, to) to get only the timestamps in a given time range."): tuple[float | None, float | None] | None = `None`*, *\**, *[leftOpen](#traceAnalysisAPI.arraybased.Signal.GetTimestamps.leftOpen "traceAnalysisAPI.arraybased.Signal.GetTimestamps.leftOpen (Python parameter) — Only valid if fromTo is given."): bool = `False`*, *[rightOpen](#traceAnalysisAPI.arraybased.Signal.GetTimestamps.rightOpen "traceAnalysisAPI.arraybased.Signal.GetTimestamps.rightOpen (Python parameter) — Only valid if fromTo is given."): bool = `True`*) → ndarray[¶](#traceAnalysisAPI.arraybased.Signal.GetTimestamps "Link to this definition")  
Returns the time axis of the signal. The parameter fromTo can be used to only timestamps in a given time range.

Parameters:  fromTo: tuple[float | None, float | None] | None = `None`[¶](#traceAnalysisAPI.arraybased.Signal.GetTimestamps.fromTo "Permalink to this definition")  
An optional tuple with timestamps (from, to) to get only the timestamps in a given time range. By default, the time range is handled as right open interval. Use the parameters leftOpen and rightOpen to change this behavior. It is possible to set one of the limits to None to restrict the time axis only in one direction.

leftOpen: bool = `False`[¶](#traceAnalysisAPI.arraybased.Signal.GetTimestamps.leftOpen "Permalink to this definition")  
Only valid if fromTo is given. Sets whether fromTo will be handled as left open interval (default False).

rightOpen: bool = `True`[¶](#traceAnalysisAPI.arraybased.Signal.GetTimestamps.rightOpen "Permalink to this definition")  
Only valid if fromTo is given. Sets whether fromTo will be handled as right open interval (default True).

Note:  
The parameters leftOpen and rightOpen are keyword only arguments!

GetTraceFileSignalName() → str[¶](#traceAnalysisAPI.arraybased.Signal.GetTraceFileSignalName "Link to this definition")  
Returns the name of the signal in the trace file the signals comes from. Will be an empty string if the signal is not bound / not present.

GetUnit() → str[¶](#traceAnalysisAPI.arraybased.Signal.GetUnit "Link to this definition")  
Returns the unit of the signal.

GetValueAt(*[timestamp](#traceAnalysisAPI.arraybased.Signal.GetValueAt "traceAnalysisAPI.arraybased.Signal.GetValueAt.timestamp (Python parameter)"): float*) → float | None[¶](#traceAnalysisAPI.arraybased.Signal.GetValueAt "Link to this definition")  
Returns the signal value at a given timestamp.

Note:  
This method is not intended to be used in an iterative manner. To get multiple interpolated values use the static method [`NumpyBasedTraceStep.FitToAxis()`](#traceAnalysisAPI.arraybased.NumpyBasedTraceStep.FitToAxis "traceAnalysisAPI.arraybased.NumpyBasedTraceStep.FitToAxis (Python method) — Maps a signal to a target time axis. Interpolates between timestamps using sample-and-hold if necessary.").

Returns:  The signal value. Values will be interpolated by sample-and-hold. Returns None if the signal has no sample until timestamp.

GetValues(*[fromTo](#traceAnalysisAPI.arraybased.Signal.GetValues.fromTo "traceAnalysisAPI.arraybased.Signal.GetValues.fromTo (Python parameter) — An optional tuple with timestamps (from, to) to get only the values in a given time range."): tuple[float | None, float | None] | None = `None`*, *\**, *[leftOpen](#traceAnalysisAPI.arraybased.Signal.GetValues.leftOpen "traceAnalysisAPI.arraybased.Signal.GetValues.leftOpen (Python parameter) — Only valid if fromTo is given."): bool = `False`*, *[rightOpen](#traceAnalysisAPI.arraybased.Signal.GetValues.rightOpen "traceAnalysisAPI.arraybased.Signal.GetValues.rightOpen (Python parameter) — Only valid if fromTo is given."): bool = `True`*) → ndarray[¶](#traceAnalysisAPI.arraybased.Signal.GetValues "Link to this definition")  
Returns the values of the signal. The parameter fromTo can be used to only values in a given time range.

Parameters:  fromTo: tuple[float | None, float | None] | None = `None`[¶](#traceAnalysisAPI.arraybased.Signal.GetValues.fromTo "Permalink to this definition")  
An optional tuple with timestamps (from, to) to get only the values in a given time range. By default, the time range is handled as right open interval. Use the parameters leftOpen and rightOpen to change this behavior. It is possible to set one of the limits to None to restrict the time axis only in one direction.

leftOpen: bool = `False`[¶](#traceAnalysisAPI.arraybased.Signal.GetValues.leftOpen "Permalink to this definition")  
Only valid if fromTo is given. Sets whether fromTo will be handled as left open interval (default False).

rightOpen: bool = `True`[¶](#traceAnalysisAPI.arraybased.Signal.GetValues.rightOpen "Permalink to this definition")  
Only valid if fromTo is given. Sets whether fromTo will be handled as right open interval (default True).

Note:  
The parameters leftOpen and rightOpen are keyword only arguments!

IsBound() → bool[¶](#traceAnalysisAPI.arraybased.Signal.IsBound "Link to this definition")  
Returns if the trace step signal is bound to a generic signal of the trace analysis.

IsFound() → bool[¶](#traceAnalysisAPI.arraybased.Signal.IsFound "Link to this definition")  
Returns if the signal is found (is bound, and is calculated or is found in the existing trace file).

IsOutSignal() → bool[¶](#traceAnalysisAPI.arraybased.Signal.IsOutSignal "Link to this definition")  
Returns if the signal is an output signal.

## RecordingInfo[¶](#recordinginfo "Link to this heading")

*class* traceAnalysisAPI.arraybased.RecordingInfo[¶](#traceAnalysisAPI.arraybased.RecordingInfo "Link to this definition")  
A RecordingInfo object contains information about the name, number, type and path of the underlying recording from which the signal stems.

GetFirstPath() → str | None[¶](#traceAnalysisAPI.arraybased.RecordingInfo.GetFirstPath "Link to this definition")  
Returns the first path of the path list of the recordings or None, if the list is empty.

Returns:  path of the first recording, if exists

GetPath(*[idx](#traceAnalysisAPI.arraybased.RecordingInfo.GetPath "traceAnalysisAPI.arraybased.RecordingInfo.GetPath.idx (Python parameter)")=`0`*) → str | None[¶](#traceAnalysisAPI.arraybased.RecordingInfo.GetPath "Link to this definition")  
Returns the path (or the first path if there is a list of paths) for the recording.

Returns:  The path

GetPathList() → list[str][¶](#traceAnalysisAPI.arraybased.RecordingInfo.GetPathList "Link to this definition")  
Returns the path list of the recordings.

Returns:  path list of the recordings

GetRecordingName() → str | None[¶](#traceAnalysisAPI.arraybased.RecordingInfo.GetRecordingName "Link to this definition")  
Returns the name of the recording.

Returns:  the name of the recording

GetRecordingNumber() → int[¶](#traceAnalysisAPI.arraybased.RecordingInfo.GetRecordingNumber "Link to this definition")  
Returns the number of the recording.

Returns:  the number of the recording (\>=0, and \< the total number of the associated recording group)

GetRecordingType() → str[¶](#traceAnalysisAPI.arraybased.RecordingInfo.GetRecordingType "Link to this definition")  
Returns the type of the recording.

Returns:  type of the recording

GetStartTimeNs(*\**, *[synchronized](#traceAnalysisAPI.arraybased.RecordingInfo.GetStartTimeNs.synchronized "traceAnalysisAPI.arraybased.RecordingInfo.GetStartTimeNs.synchronized (Python parameter) — If True, the start time is adjusted by the deltaT if available."): bool = `True`*) → int | None[¶](#traceAnalysisAPI.arraybased.RecordingInfo.GetStartTimeNs "Link to this definition")  
Returns the start time of the recording in nanoseconds since 1970-01-01T00:00:00Z.

This information is useful to calculate absolute timestamps, e.g.:

absoluteTimestampsInNs = int(relativeTimestampsInSeconds \* 1e9) + startTimeNs

If the traces have not been synchronized, the value of the parameter synchronized does not matter. If the traces have been sychronized, this method should normally be called with synchronized=True (default) so that the start time is adjusted to the deltaT and the adjusted start time can just be added to the synchronized timestamps to get the absolute timestamps. However, if you want to get the real start time without any adjustments, you should call this method with synchronized=False.

Parameters:  synchronized: bool = `True`[¶](#traceAnalysisAPI.arraybased.RecordingInfo.GetStartTimeNs.synchronized "Permalink to this definition")  
If True, the start time is adjusted by the deltaT if available.

Returns:  start time in nanoseconds or None if the recording format does not support it

Raises:  
**ValueError** – if the start time cannot be determined (e.g., empty file or missing metadata)

## ReportTable[¶](#reporttable "Link to this heading")

*class* traceAnalysisAPI.arraybased.ReportTable[¶](#traceAnalysisAPI.arraybased.ReportTable "Link to this definition")  
A ReportTable object represents a table in the test report.

AddRow(*[values](#traceAnalysisAPI.arraybased.ReportTable.AddRow.values "traceAnalysisAPI.arraybased.ReportTable.AddRow.values (Python parameter) — iterable with the entries for each column of the new row"): Iterable[str]*, *[resultId](#traceAnalysisAPI.arraybased.ReportTable.AddRow.resultId "traceAnalysisAPI.arraybased.ReportTable.AddRow.resultId (Python parameter) — the result id of the row"): int | None = `None`*) → None[¶](#traceAnalysisAPI.arraybased.ReportTable.AddRow "Link to this definition")  
Appends a row to the table.

Parameters:  values : iterable[¶](#traceAnalysisAPI.arraybased.ReportTable.AddRow.values "Permalink to this definition")  
iterable with the entries for each column of the new row

resultId : result id or None[¶](#traceAnalysisAPI.arraybased.ReportTable.AddRow.resultId "Permalink to this definition")  
the result id of the row

SetHeader(*[values](#traceAnalysisAPI.arraybased.ReportTable.SetHeader.values "traceAnalysisAPI.arraybased.ReportTable.SetHeader.values (Python parameter) — iterable with the entries for each column of the table header"): Iterable[str | int] | None*) → None[¶](#traceAnalysisAPI.arraybased.ReportTable.SetHeader "Link to this definition")  
Sets the table header.

Parameters:  values : iterable[¶](#traceAnalysisAPI.arraybased.ReportTable.SetHeader.values "Permalink to this definition")  
iterable with the entries for each column of the table header

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
