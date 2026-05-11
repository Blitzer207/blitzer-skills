# Array-based NumPy trace step templates[¶](#array-based-numpy-trace-step-templates "Link to this heading")

## NumpyBasedTraceStep[¶](#numpybasedtracestep "Link to this heading")

*class* traceAnalysisAPI.arraybased.NumpyBasedTraceStep[¶](#traceAnalysisAPI.arraybased.NumpyBasedTraceStep "Link to this definition")  
*abstract static* GetInterfaceRevision()[¶](#traceAnalysisAPI.arraybased.NumpyBasedTraceStep.GetInterfaceRevision "Link to this definition")  
Returns the interface revision of the trace step template.

Note:  
This method is auto-generated for new implementations of NumpyBasedTraceStep. So do not delete or modify this method!

Return type:  int

Note

**Interface method:** Has to be overridden by child class.

*classmethod* GetDescription()[¶](#traceAnalysisAPI.arraybased.NumpyBasedTraceStep.GetDescription "Link to this definition")  
Returns the description of the trace step.

Return type:  str

Note

**Interface method:** Can be overridden by child class.

*abstract classmethod* GetSignals()[¶](#traceAnalysisAPI.arraybased.NumpyBasedTraceStep.GetSignals "Link to this definition")  
Returns the incoming and outgoing signals of the trace step.

Return type:  list[[SignalDefinition](#traceAnalysisAPI.arraybased.SignalDefinition "traceAnalysisAPI.arraybased.SignalDefinition")]

Note

**Interface method:** Has to be overridden by child class in order to use signals in trace step template.

*classmethod* GetParameters()[¶](#traceAnalysisAPI.arraybased.NumpyBasedTraceStep.GetParameters "Link to this definition")  
Returns the input and return parameters of the trace step.

Return type:  list[[ParameterDefinition](#traceAnalysisAPI.arraybased.ParameterDefinition "traceAnalysisAPI.arraybased.ParameterDefinition")]

Note

**Interface method:** Has to be overridden by child class in order to use parameters in trace step template.

*classmethod* GetTimeAxisDefinition()[¶](#traceAnalysisAPI.arraybased.NumpyBasedTraceStep.GetTimeAxisDefinition "Link to this definition")  
Returns how the common time axis is determined. Only the logical operators **and** and **or** as well as references to the time axes of the signals by using the signal name are permitted. The use of brackets is allowed.

Note:  
If a signal is not defined on the common time axis, its value is determined according to its interpolation rule.

Returns:  Convention for building the common time axis (e.g. **‘Sig1 or Sig2’**). If an empty string is returned, all time axes are merged into one common time axis. This corresponds to an OR concatenation of the individual time axes.

Return type:  str

Note

**Interface method:** Can be overridden by child class.

Check(*parameters*)[¶](#traceAnalysisAPI.arraybased.NumpyBasedTraceStep.Check "Link to this definition")  
Is called initially before trace analysis execution and should check the parameterization. In case of error, raise a TypeError or ValueError.

Parameters:  **parameters** (*dict[str,* *object]*) – Dictionary of parameter values.

Raises:  
- **TypeError** – Invalid type of a parameter.

- **ValueError** – Invalid value of a parameter.

Note

**Interface method:** Should be overridden by child class.

*abstract* Process(*parameters*, *report*, *timeAxis*, *ranges*, *signals*)[¶](#traceAnalysisAPI.arraybased.NumpyBasedTraceStep.Process "Link to this definition")  
Method for executing the trace step template. Calculations can be performed based on the given signal values and their results can be stored in outgoing signals. Evaluation results and return parameters can be set.

Note:  
It is recommended to evaluate over the given trigger ranges and set the result for each trigger range. The overall result will be automatically determined.

It is possible to manually set the overall result using the [`Report`](#traceAnalysisAPI.arraybased.Report "traceAnalysisAPI.arraybased.Report") object; the automatic mechanism will be deactivated if used.

Detailed spots are also reported on trigger ranges.

Note:  
Access to values: All signal values within a trigger range can be accessed by its [`TriggerRange`](#traceAnalysisAPI.arraybased.TriggerRange "traceAnalysisAPI.arraybased.TriggerRange") object. Alternatively, all values of a signal can be accessed by the [`Signal`](#traceAnalysisAPI.arraybased.Signal "traceAnalysisAPI.arraybased.Signal") object.

Note:  
To store calculated values in an outgoing signal the [`Signal`](#traceAnalysisAPI.arraybased.Signal "traceAnalysisAPI.arraybased.Signal") object is used: Signal.Emit(timestamps, values)

Parameters:  - **parameters** (*dict[str,* *object]*) – Dictionary of parameter values.

- **report** ([`Report`](#traceAnalysisAPI.arraybased.Report "traceAnalysisAPI.arraybased.Report")) – The report object.

- **timeAxis** (*numpy.ndarray*) – The common time axis of the signals over the entire trace. A limitation to the trigger ranges can be provided by a [`TriggerRange`](#traceAnalysisAPI.arraybased.TriggerRange "traceAnalysisAPI.arraybased.TriggerRange") object.

- **ranges** (*list[*[*TriggerRange*](#traceAnalysisAPI.arraybased.TriggerRange "traceAnalysisAPI.arraybased.TriggerRange")*]*) – List of trigger ranges.

- **signals** (dict[str, [`Signal`](#traceAnalysisAPI.arraybased.Signal "traceAnalysisAPI.arraybased.Signal")]) – Dictionary of signals.

Note

**Interface method:** Has to be overridden by child class.

*static* FitToAxis(*timestamps*, *values*, *targetTimeArray*, *leftFillValue=None*, *rightFillValue=None*)[¶](#traceAnalysisAPI.arraybased.NumpyBasedTraceStep.FitToAxis "Link to this definition")  
Maps a signal to a target time axis. Interpolates between timestamps using sample-and-hold if necessary.

Parameters:  - **timestamps** (*numpy.ndarray*) – Time axis of the signal.

- **values** (*numpy.ndarray*) – Values of the signal.

- **targetTimeArray** (*numpy.ndarray*) – Target time axis.

- **leftFillValue** (*object*) – Values before the first sample of the signal are defined by this value. If None, numpy.NAN is used. If values is a Boolean array and any numpy.NAN is applied the resulting array will be converted from bool to float!

- **rightFillValue** (*object*) – Values after the last sample of the signal are defined by this value. If None, the last signal value is used.

Returns:  Value array containing the signal values mapped to targetTimeArray.

Return type:  numpy.ndarray

*static* CalculateRanges(*boolArray*)[¶](#traceAnalysisAPI.arraybased.NumpyBasedTraceStep.CalculateRanges "Link to this definition")  
Searches boolArray for ‘True ranges’ and ‘False ranges’ and creates ‘from-to-tuples’.

Parameters:  **boolArray** (*numpy.ndarray*) – Array containing truth values.

Returns:  List with a (start, stop, truth value) tuple per range.

Return type:  list[tuple[int, int, bool]]

*static* CalculateMaskForRange(*array*, *minVal=None*, *maxVal=None*, *leftOpen=False*, *rightOpen=False*)[¶](#traceAnalysisAPI.arraybased.NumpyBasedTraceStep.CalculateMaskForRange "Link to this definition")  
Calculate a mask that fits all values that are in the interval [minVal, maxVal]. Both minVal and maxVal are optional.The interval is closed per default. The parameters leftOpen and rightOpen can be used to change this behavior.

Note:  
This method can be used to calculate the mask for a signal’s time axis which then is applied to the signal values to get all values in a given time range.

Note:  
There is no special handling for NaN values. Avoid NaNs by masking beforehand. There will be a RuntimeWarning if the array contains NaNs.

Parameters:  - **array** (*numpy.ndarray*) – The value array.

- **minVal** (*int|float*) – The minimum value to be included in the new array.

- **maxVal** (*int|float*) – The maximum value to be included in the new array.

- **leftOpen** (*bool*) – If False (default), the left interval limit, defined by minVal, is left closed. This means that values greater than or equal minVal are masked valid. If True, the left interval limit is left opened and only values greater than minVal are masked valid.

- **rightOpen** (*bool*) – If False (default), the right interval limit, defined by maxVal, is right closed. This means that values less than or equal maxVal are masked valid. If True, the right interval limit is right opened and only values less than maxVal are masked valid.

Returns:  The mask

Return type:  numpy.ndarray

*static* GetParameterPanel(*parent*)[¶](#traceAnalysisAPI.arraybased.NumpyBasedTraceStep.GetParameterPanel "Link to this definition")  
This method can be implemented to create a custom parameterization panel for the trace step dialog. It is designated to edit trace step parameters (no signals). The panel must inherit from wx.Panel or any subclass, and must implement the methods of the interface ‘ParameterPanel’ (no inheritance required). See TraceanalysisAPI documentation section ‘Custom GUI for parameters’ for more information.

Note:  
Keep imports of GUI frameworks locally, please.

Returns:  Returns a subclass of wx.Panel that implements the methods defined by the interface of ParameterPanel. The return value can be None if no custom GUI is defined.

Return type:  wx.Panel

Note

**Interface method:** Can be overridden by child class.

## SignalDefinition[¶](#signaldefinition "Link to this heading")

*class* traceAnalysisAPI.arraybased.SignalDefinition[¶](#traceAnalysisAPI.arraybased.SignalDefinition "Link to this definition")  
Definition of an incoming or outgoing signal of the trace step.

`\_\_init\_\_`(*name*, *direction*, *optional=False*, *description=''*)[¶](#traceAnalysisAPI.arraybased.SignalDefinition.__init__ "Link to this definition")  
Parameters:  - **name** (*str*) – Name of the signal. Must be a valid Python identifier.

- **direction** (*str*) – Direction of the signal: ‘IN’, ‘OUT’.

- **optional** (*bool*) – This parameter only applies to signals with direction IN. OUT signals will always be optional. If True, the signal is optional. When using the trace step, it is allowed that the signal is not assigned or not found in the trace or no trace is given.

- **description** (*str*) – Description of the signal.

## ParameterDefinition[¶](#parameterdefinition "Link to this heading")

*class* traceAnalysisAPI.arraybased.ParameterDefinition[¶](#traceAnalysisAPI.arraybased.ParameterDefinition "Link to this definition")  
Definition of an input or return parameter of the trace step.

`\_\_init\_\_`(*name*, *direction*, *default=None*, *description=''*)[¶](#traceAnalysisAPI.arraybased.ParameterDefinition.__init__ "Link to this definition")  
Parameters:  - **name** (*str*) – Name of the parameter. Must be a valid Python identifier.

- **direction** (*str*) – Direction of the signal: ‘IN’, ‘OUT’.

- **default** (*object*) – Default value if no parameter value (value None) is specified when used.

- **description** (*str*) – Description of the parameter.

## Report[¶](#report "Link to this heading")

*class* traceAnalysisAPI.arraybased.Report[¶](#traceAnalysisAPI.arraybased.Report "Link to this definition")  
This class represents the overall report of the trace step.

Note:  
In general, results should be set on TriggerRanges. The overall result will be determined automatically. If you set the result via this class, the result is fixed and will not change even if a TriggerRange has a worse result.

ImageFromBytes(*dataBytes*, *name=None*, *title=None*)[¶](#traceAnalysisAPI.arraybased.Report.ImageFromBytes "Link to this definition")  
Parameters:  - **dataBytes** (*bytes*) – byte stream (see: [https://docs.python.org/3.7/library/io.html](https://docs.python.org/3.7/library/io.html) and [https://docs.python.org/3/library/stdtypes.html#bytes](https://docs.python.org/3/library/stdtypes.html#bytes))

- **name** (*str*) – name of the image (e.g. used as file name in html/json report)

- **title** (*str*) – the image title

Note

**Deprecated:** Please use [`Report.Image()`](#traceAnalysisAPI.arraybased.Report.Image "traceAnalysisAPI.arraybased.Report.Image") instead.

AddResultColumn(*name: str*) → None[¶](#traceAnalysisAPI.arraybased.Report.AddResultColumn "Link to this definition")  
Adds a new column with the given name to the result table. It is appended at the end of the table. Values can be inserted into this column by using the parameter “additionalInfo” of the methods `Spot()` and `Range()`. The entries in the list “additionalInfo” list are inserted into the additional result columns in sequence.

Parameters:  **name** (*str*) – name of the new column

GetResultId()[¶](#traceAnalysisAPI.arraybased.Report.GetResultId "Link to this definition")  
Return type:  int

Image(*imageSource: str | Path | ImageInterface | ndarray | bytes*, *\**, *name: str | None = None*, *title: str | None = None*, *embedded: bool = False*, *limitPreviewSize: bool = True*, *autoDelete: bool = False*, *useTemp: bool = True*) → ReportImage[¶](#traceAnalysisAPI.arraybased.Report.Image "Link to this definition")  
Adds the given image to the test report. If the image is not embedded in the test report, the file will be stored in the report folder. If there is already an image with the same name, the image files will be enumerated.

Parameters:  - **imageSource** (*str|Path|Image|Frame|numpy.ndarray|bytes*) –

  The image source can be one of the following:

  - an absolute file path

  - an Image or Frame object

  - a NumPy array in OpenCV style: shape is (height, width, 3) of type numpy.uint8, the three colors have the order BGR!

  - bytes object with image data

- **name** (*str*) – The filename (with correct extension). Will be used as filename if an image file is created in the report folder. If name is None and the source is a path or an Image or Frame, the name of the imageSource is used.

- **title** (*str*) – the image title

- **embedded** (*bool*) – True, if the image file should be embedded in the test report, else the image file is stored in the test report folder.

- **limitPreviewSize** (*bool*) – If True (default), the preview image shown in the report will be limited to a maximum size.

- **autoDelete** (*bool*) – Only applicable if imageSource is a file path. True, if the image file should be automatically deleted, else False.

- **useTemp** (*bool*) – Only applicable if imageSource is a file path. True, if the image file should be copied into a temporary directory, False, if it should be used directly. Using a temporary copy might be necessary to avoid overriding the image before the final report gets assembled later on.

Log(*level*, *time*, *message*, *\*formatArgs*, *\*\*formatKwargs*)[¶](#traceAnalysisAPI.arraybased.Report.Log "Link to this definition")  
Adds a log message to the trace analysis log file. Use [`SetLogComponent()`](#traceAnalysisAPI.arraybased.Report.SetLogComponent "traceAnalysisAPI.arraybased.Report.SetLogComponent") to set the component part of the log entry.

Parameters:  - **level** (*int*) – log level - report.LOG_LEVEL_DEBUG - report.LOG_LEVEL_INFO - report.LOG_LEVEL_WARNING - report.LOG_LEVEL_ERROR

- **time** (*float*) – timestamp of the log message

- **message** (*str*) – log message or format string.

- **formatArgs** – additional non-keyword arguments used when message is a format string

- **formatKwargs** – additional keyword arguments used when message is a format string

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

LogDebug(*time*, *message*, *\*formatArgs*, *\*\*formatKwargs*)[¶](#traceAnalysisAPI.arraybased.Report.LogDebug "Link to this definition")  
Convenience method to add a debug log message. See [`Log()`](#traceAnalysisAPI.arraybased.Report.Log "traceAnalysisAPI.arraybased.Report.Log") for further usage.

LogError(*time*, *message*, *\*formatArgs*, *\*\*formatKwargs*)[¶](#traceAnalysisAPI.arraybased.Report.LogError "Link to this definition")  
Convenience method to add an error log message. See [`Log()`](#traceAnalysisAPI.arraybased.Report.Log "traceAnalysisAPI.arraybased.Report.Log") for further usage.

LogInfo(*time*, *message*, *\*formatArgs*, *\*\*formatKwargs*)[¶](#traceAnalysisAPI.arraybased.Report.LogInfo "Link to this definition")  
Convenience method to add an info log message. See [`Log()`](#traceAnalysisAPI.arraybased.Report.Log "traceAnalysisAPI.arraybased.Report.Log") for further usage.

LogWarning(*time*, *message*, *\*formatArgs*, *\*\*formatKwargs*)[¶](#traceAnalysisAPI.arraybased.Report.LogWarning "Link to this definition")  
Convenience method to add a warning log message. See [`Log()`](#traceAnalysisAPI.arraybased.Report.Log "traceAnalysisAPI.arraybased.Report.Log") for further usage.

SetLogComponent(*component*)[¶](#traceAnalysisAPI.arraybased.Report.SetLogComponent "Link to this definition")  
Sets the component that will be used in logging entries created by calling log methods.

Parameters:  **component** (*str*) – name of the component

SetResultError()[¶](#traceAnalysisAPI.arraybased.Report.SetResultError "Link to this definition")  
Convenience method for report.SetResultId(report.RESULT_ID_ERROR)

SetResultFailed()[¶](#traceAnalysisAPI.arraybased.Report.SetResultFailed "Link to this definition")  
Convenience method for report.SetResultId(report.RESULT_ID_FAILED)

SetResultId(*resultId*)[¶](#traceAnalysisAPI.arraybased.Report.SetResultId "Link to this definition")  
Sets the result id for the current trace step.

The result id can be one of:

> - report.RESULT_ID_NONE
>
> - report.RESULT_ID_SUCCESS
>
> - report.RESULT_ID_INCONCLUSIVE
>
> - report.RESULT_ID_FAILED
>
> - report.RESULT_ID_ERROR

The result id is set directly. It is not affected by earlier calls to [`SetResultId()`](#traceAnalysisAPI.arraybased.Report.SetResultId "traceAnalysisAPI.arraybased.Report.SetResultId").

Example:

    report.SetResultId(report.RESULT_ID_ERROR)
    report.SetResultId(report.RESULT_ID_NONE)

    report.GetResultId() # this will result in report.RESULT_ID_NONE

Parameters:  **resultId** (*result id*) – the result id to set

SetResultInconclusive()[¶](#traceAnalysisAPI.arraybased.Report.SetResultInconclusive "Link to this definition")  
Convenience method for report.SetResultId(report.RESULT_ID_INCONCLUSIVE)

SetResultSuccess()[¶](#traceAnalysisAPI.arraybased.Report.SetResultSuccess "Link to this definition")  
Convenience method for report.SetResultId(report.RESULT_ID_SUCCESS)

SetResultText(*text: str | None*) → None[¶](#traceAnalysisAPI.arraybased.Report.SetResultText "Link to this definition")  
Sets a user-defined text for the result of the report.

Parameters:  **text** (*str*) – the text

Table(*tableId: str | int | None = None*, *headerValues: Iterable[str | int] | None = None*) → ReportTable[¶](#traceAnalysisAPI.arraybased.Report.Table "Link to this definition")  
Creates a table in the test report.

Example:

    table = report.Table("table1", ["time", "description"])
    table.AddRow(["1.3", "A rising edge detected"])
    table.AddRow(["3.8", "A falling edge detected"])

Parameters:  - **tableId** (*str*) – id to identify the table

- **headerValues** (*iterable*) – iterable with the entries of the table header

Returns:  the report table object

Return type:  [`ReportTable`](#traceAnalysisAPI.arraybased.ReportTable "traceAnalysisAPI.arraybased.ReportTable")

UpdateResultId(*resultId*)[¶](#traceAnalysisAPI.arraybased.Report.UpdateResultId "Link to this definition")  
Updates the result id for the current trace step.

The result id can be one of:

> - report.RESULT_ID_NONE
>
> - report.RESULT_ID_SUCCESS
>
> - report.RESULT_ID_INCONCLUSIVE
>
> - report.RESULT_ID_FAILED
>
> - report.RESULT_ID_ERROR

In contrast to [`SetResultId()`](#traceAnalysisAPI.arraybased.Report.SetResultId "traceAnalysisAPI.arraybased.Report.SetResultId"), which sets the resultId directly, [`UpdateResultId()`](#traceAnalysisAPI.arraybased.Report.UpdateResultId "traceAnalysisAPI.arraybased.Report.UpdateResultId") can only increase the resultId according to the following ordering:

RESULT_ID_NONE \< RESULT_ID_SUCCESS \< RESULT_ID_INCONCLUSIVE \< RESULT_ID_FAILED \< RESULT_ID_ERROR

Note

[`UpdateResultId()`](#traceAnalysisAPI.arraybased.Report.UpdateResultId "traceAnalysisAPI.arraybased.Report.UpdateResultId") can bee seen as equivalent to SetResultId(max(resultId, GetResultId()))

Example:

    report.UpdateResultId(report.RESULT_ID_SUCCESS)
    ...
    report.UpdateResultId(report.RESULT_ID_FAILED)
    ...
    report.UpdateResultId(report.RESULT_ID_SUCCESS)

    report.GetResultId() # this will result in report.RESULT_ID_FAILED

Parameters:  **resultId** (*result id*) – the result id to set

## TriggerRange[¶](#triggerrange "Link to this heading")

*class* traceAnalysisAPI.arraybased.TriggerRange[¶](#traceAnalysisAPI.arraybased.TriggerRange "Link to this definition")  
Representation of a trigger range. Contains timestamps and values of signals on the common time axis within the range as well as report information of a trigger range.

ImageFromBytes(*dataBytes*, *name=None*, *title=None*)[¶](#traceAnalysisAPI.arraybased.TriggerRange.ImageFromBytes "Link to this definition")  
Parameters:  - **dataBytes** (*bytes*) – byte stream (see: [https://docs.python.org/3.7/library/io.html](https://docs.python.org/3.7/library/io.html) and [https://docs.python.org/3/library/stdtypes.html#bytes](https://docs.python.org/3/library/stdtypes.html#bytes))

- **name** (*str*) – name of the image (e.g. used as file name in html/json report)

- **title** (*str*) – the image title

Note

**Deprecated:** Please use [`TriggerRange.Image()`](#traceAnalysisAPI.arraybased.TriggerRange.Image "traceAnalysisAPI.arraybased.TriggerRange.Image") instead.

GetRelativeTimestamps()[¶](#traceAnalysisAPI.arraybased.TriggerRange.GetRelativeTimestamps "Link to this definition")  
Returns the timestamps of the common time axis within the trigger range relative to the start trigger time.

Return type:  numpy.ndarray

GetResultId()[¶](#traceAnalysisAPI.arraybased.TriggerRange.GetResultId "Link to this definition")  
Gets the current result id.

The result id passed to an earlier call to [`SetResultId()`](#traceAnalysisAPI.arraybased.TriggerRange.SetResultId "traceAnalysisAPI.arraybased.TriggerRange.SetResultId") is returned. If [`SetResultId()`](#traceAnalysisAPI.arraybased.TriggerRange.SetResultId "traceAnalysisAPI.arraybased.TriggerRange.SetResultId") wasn’t called before, `RESULT_ID_NONE` is returned.

Returns:  the result id

Return type:  int

GetSlice()[¶](#traceAnalysisAPI.arraybased.TriggerRange.GetSlice "Link to this definition")  
Returns a slice [from, to] that can be used to slice from arrays that are based on the main time axis.

Return type:  slice

GetStartTime()[¶](#traceAnalysisAPI.arraybased.TriggerRange.GetStartTime "Link to this definition")  
Returns the start time of the trigger range.

Note:  
The value can be different to the first sample of the common time axis or any signal time axis for the following cases:

> - used in a trigger block that uses different signals
>
> - not in a trigger block: The first sample of all signals of the episode will be taken.

Returns:  The start time or None if it could not be determined (e.g. no signal with samples)

Return type:  float

GetStartValue(*sigName*, *deltaT=0.0*)[¶](#traceAnalysisAPI.arraybased.TriggerRange.GetStartValue "Link to this definition")  
Returns the value of the given signal at the timestamp of the start trigger plus deltaT.

Parameters:  - **sigName** (*str*) – The regarded signal

- **deltaT** (*float*) – Offset to the start trigger timestamp.

Return type:  any

GetStopTime()[¶](#traceAnalysisAPI.arraybased.TriggerRange.GetStopTime "Link to this definition")  
Returns the timestamp where the trigger range ends.

Note:  
This can be different to the last sample of the common time axis or any signal time axis for the following cases:

> - used in a trigger block that uses different signals
>
> - not in a trigger block: The first sample of all signals of the episode will be taken.

Note:  
There is no evaluation at the stop time. Exception: stop at end of trace.

Returns:  The stop time or None if it could not be determined (e.g. no signal with samples)

Return type:  float

GetStopValue(*sigName*, *deltaT=0.0*)[¶](#traceAnalysisAPI.arraybased.TriggerRange.GetStopValue "Link to this definition")  
Returns the value of the given signal at the timestamp of the stop trigger plus deltaT.

Parameters:  - **sigName** (*str*) – The regarded signal

- **deltaT** (*float*) – Offset to the stop trigger timestamp.

Return type:  any

GetTimestamps()[¶](#traceAnalysisAPI.arraybased.TriggerRange.GetTimestamps "Link to this definition")  
Returns the timestamps of the common time axis within the trigger range.

Return type:  numpy.ndarray

GetValues(*sigName*)[¶](#traceAnalysisAPI.arraybased.TriggerRange.GetValues "Link to this definition")  
Returns the values of a signal on the common time axis within the trigger range.

Return type:  numpy.ndarray

Image(*imageSource: str | Path | ImageInterface | ndarray | bytes*, *\**, *name: str | None = None*, *title: str | None = None*, *embedded: bool = False*, *limitPreviewSize: bool = True*, *autoDelete: bool = False*, *useTemp: bool = True*) → ReportImage[¶](#traceAnalysisAPI.arraybased.TriggerRange.Image "Link to this definition")  
Adds the given image to the test report. If the image is not embedded in the test report, the file will be stored in the report folder. If there is already an image with the same name, the image files will be enumerated.

Parameters:  - **imageSource** (*str|Path|Image|Frame|numpy.ndarray|bytes*) –

  The image source can be one of the following:

  - an absolute file path

  - an Image or Frame object

  - a NumPy array in OpenCV style: shape is (height, width, 3) of type numpy.uint8, the three colors have the order BGR!

  - bytes object with image data

- **name** (*str*) – The filename (with correct extension). Will be used as filename if an image file is created in the report folder. If name is None and the source is a path or an Image or Frame, the name of the imageSource is used.

- **title** (*str*) – the image title

- **embedded** (*bool*) – True, if the image file should be embedded in the test report, else the image file is stored in the test report folder.

- **limitPreviewSize** (*bool*) – If True (default), the preview image shown in the report will be limited to a maximum size.

- **autoDelete** (*bool*) – Only applicable if imageSource is a file path. True, if the image file should be automatically deleted, else False.

- **useTemp** (*bool*) – Only applicable if imageSource is a file path. True, if the image file should be copied into a temporary directory, False, if it should be used directly. Using a temporary copy might be necessary to avoid overriding the image before the final report gets assembled later on.

IsWholeTrace()[¶](#traceAnalysisAPI.arraybased.TriggerRange.IsWholeTrace "Link to this definition")  
Returns True if the trace step has no trigger block as ancestor. In this case there will only be one trigger range that represents the entire time domain of the trace analysis.

Correspondingly, if the trace step is contained in a trigger block, this method will return False for all trigger ranges.

Return type:  bool

Range(*startTime*, *stopTime*, *message=''*, *resultId=0*, *additionalInfo=None*)[¶](#traceAnalysisAPI.arraybased.TriggerRange.Range "Link to this definition")  
Adds a sub range to the trigger range.

Parameters:  - **startTime** (*float*) – timestamp at which the sub range begins

- **stopTime** (*float*) – timestamp at which the sub range ends

- **message** (*string*) – a textual message describing the sub range

- **resultId** (*int*) – the verdict for the sub range

- **additionalInfo** (*list[str]*) – a list of additional information, that will be shown in the custom result columns (see [`Report.AddResultColumn()`](#traceAnalysisAPI.arraybased.Report.AddResultColumn "traceAnalysisAPI.arraybased.Report.AddResultColumn"))

SetResultError()[¶](#traceAnalysisAPI.arraybased.TriggerRange.SetResultError "Link to this definition")  
Convenience method for triggerRange.SetResultId(triggerRange.RESULT_ID_ERROR)

SetResultFailed()[¶](#traceAnalysisAPI.arraybased.TriggerRange.SetResultFailed "Link to this definition")  
Convenience method for triggerRange.SetResultId(triggerRange.RESULT_ID_FAILED)

SetResultId(*resultId*)[¶](#traceAnalysisAPI.arraybased.TriggerRange.SetResultId "Link to this definition")  
Sets the result id for the trigger range.

The result id can be one of:

> - triggerRange.RESULT_ID_NONE
>
> - triggerRange.RESULT_ID_SUCCESS
>
> - triggerRange.RESULT_ID_INCONCLUSIVE
>
> - triggerRange.RESULT_ID_FAILED
>
> - triggerRange.RESULT_ID_ERROR

The result id is set directly. It is not affected by earlier calls to [`SetResultId()`](#traceAnalysisAPI.arraybased.TriggerRange.SetResultId "traceAnalysisAPI.arraybased.TriggerRange.SetResultId").

Example:

    triggerRange.SetResultId(triggerRange.RESULT_ID_ERROR)
    triggerRange.SetResultId(triggerRange.RESULT_ID_NONE)

    triggerRange.GetResultId() # this will result in triggerRange.RESULT_ID_NONE

Parameters:  **resultId** (*int*) – the result id to set

SetResultInconclusive()[¶](#traceAnalysisAPI.arraybased.TriggerRange.SetResultInconclusive "Link to this definition")  
Convenience method for triggerRange.SetResultId(triggerRange.RESULT_ID_INCONCLUSIVE)

SetResultNone()[¶](#traceAnalysisAPI.arraybased.TriggerRange.SetResultNone "Link to this definition")  
Convenience method for triggerRange.SetResultId(triggerRange.RESULT_ID_NONE)

SetResultSuccess()[¶](#traceAnalysisAPI.arraybased.TriggerRange.SetResultSuccess "Link to this definition")  
Convenience method for triggerRange.SetResultId(triggerRange.RESULT_ID_SUCCESS)

SetResultText(*resultText*)[¶](#traceAnalysisAPI.arraybased.TriggerRange.SetResultText "Link to this definition")  
Sets a user-defined result text of the trigger range.

Parameters:  **resultText** (*str*) – the text

Spot(*time*, *message=''*, *resultId=0*, *additionalInfo=None*)[¶](#traceAnalysisAPI.arraybased.TriggerRange.Spot "Link to this definition")  
Adds a signal spot to the trigger range.

Parameters:  - **time** (*float*) – timestamp of the spot

- **message** (*string*) – a textual message describing the spot

- **resultId** (*int*) – the verdict for the spot

- **additionalInfo** (*list[str]*) – a list of additional information, that will be shown in the custom result columns ([`Report.AddResultColumn`](#traceAnalysisAPI.arraybased.Report.AddResultColumn "traceAnalysisAPI.arraybased.Report.AddResultColumn"))

Table(*tableId: str | int | None = None*, *headerValues: Iterable[str | int] | None = None*) → ReportTable[¶](#traceAnalysisAPI.arraybased.TriggerRange.Table "Link to this definition")  
Creates a table in the test report.

Example:

    table = report.Table("table1", ["time", "description"])
    table.AddRow(["1.3", "A rising edge detected"])
    table.AddRow(["3.8", "A falling edge detected"])

Parameters:  - **tableId** (*str*) – id to identify the table

- **headerValues** (*iterable*) – iterable with the entries of the table header

Returns:  the report table object

Return type:  [`ReportTable`](#traceAnalysisAPI.arraybased.ReportTable "traceAnalysisAPI.arraybased.ReportTable")

UpdateResultId(*resultId*)[¶](#traceAnalysisAPI.arraybased.TriggerRange.UpdateResultId "Link to this definition")  
Updates the result id for the trigger range.

The result id can be one of:

> - triggerRange.RESULT_ID_NONE
>
> - triggerRange.RESULT_ID_SUCCESS
>
> - triggerRange.RESULT_ID_INCONCLUSIVE
>
> - triggerRange.RESULT_ID_FAILED
>
> - triggerRange.RESULT_ID_ERROR

In contrast to [`SetResultId()`](#traceAnalysisAPI.arraybased.TriggerRange.SetResultId "traceAnalysisAPI.arraybased.TriggerRange.SetResultId"), which sets the resultId directly, [`UpdateResultId()`](#traceAnalysisAPI.arraybased.TriggerRange.UpdateResultId "traceAnalysisAPI.arraybased.TriggerRange.UpdateResultId") can only increase the resultId according to the following ordering:

RESULT_ID_NONE \< RESULT_ID_SUCCESS \< RESULT_ID_INCONCLUSIVE \< RESULT_ID_FAILED \< RESULT_ID_ERROR

Note

[`UpdateResultId()`](#traceAnalysisAPI.arraybased.TriggerRange.UpdateResultId "traceAnalysisAPI.arraybased.TriggerRange.UpdateResultId") can bee seen as equivalent to SetResultId(max(resultId, GetResultId()))

Example:

    triggerRange.UpdateResultId(triggerRange.RESULT_ID_SUCCESS)
    ...
    triggerRange.UpdateResultId(triggerRange.RESULT_ID_FAILED)
    ...
    triggerRange.UpdateResultId(triggerRange.RESULT_ID_SUCCESS)

    triggerRange.GetResultId() # this will result in triggerRange.RESULT_ID_FAILED

Parameters:  **resultId** (*int*) – the result id to set

## Signal[¶](#signal "Link to this heading")

*class* traceAnalysisAPI.arraybased.Signal[¶](#traceAnalysisAPI.arraybased.Signal "Link to this definition")  
A signal provides access to meta information, such as the physical unit. You can also access the specific time axis of the signal and the corresponding signal values. For outgoing signals the method Emit() can be called to set timestamps and values.

Emit(*timestamps*, *values*)[¶](#traceAnalysisAPI.arraybased.Signal.Emit "Link to this definition")  
Sets timestamps and values of an outgoing (calculated signal).

Parameters:  - **timestamps** (*numpy.ndarray*) – Time axis of the signal.

- **values** (*numpy.ndarray*) – Values of the signal.

Raises:  
**ValueError** – Called on an incoming signal or with arrays of different length.

GetGenericName()[¶](#traceAnalysisAPI.arraybased.Signal.GetGenericName "Link to this definition")  
Returns the name of the generic signal this signal is bound to. If the signal is not bound, it will return an empty string.

Return type:  str

GetInterpolatedValues()[¶](#traceAnalysisAPI.arraybased.Signal.GetInterpolatedValues "Link to this definition")  
Returns the values interpolated on the common time axis of the trace step.

Returns:  The interpolated values. Will return None for outgoing signals!

Return type:  numpy.ndarray|None

GetMappingItemName()[¶](#traceAnalysisAPI.arraybased.Signal.GetMappingItemName "Link to this definition")  
Returns the name of the mapping item this signal relates to. If the signal is not bound or it is bound to an calculated signal, it will return an empty string.

Return type:  str

GetTimestamps(*fromTo=None*, *\**, *leftOpen=False*, *rightOpen=True*)[¶](#traceAnalysisAPI.arraybased.Signal.GetTimestamps "Link to this definition")  
Returns the time axis of the signal. The parameter fromTo can be used to only timestamps in a given time range.

Parameters:  - **fromTo** (*tuple[float]*) – An optional tuple with timestamps (from, to) to get only the timestamps in a given time range. By default, the time range is handled as right open interval. Use the parameters leftOpen and rightOpen to change this behavior. It is possible to set one of the limits to None to restrict the time axis only in one direction.

- **leftOpen** (*bool*) – Only valid if fromTo is given. Sets whether fromTo will be handled as left open interval (default False).

- **rightOpen** (*bool*) – Only valid if fromTo is given. Sets whether fromTo will be handled as right open interval (default True).

Note:  
The parameters leftOpen and rightOpen are keyword only arguments!

Return type:  numpy.ndarray

GetTraceFileSignalName()[¶](#traceAnalysisAPI.arraybased.Signal.GetTraceFileSignalName "Link to this definition")  
Returns the name of the signal in the trace file the signals comes from. Will be an empty string if the signal is not bound / not present.

Return type:  str

GetUnit()[¶](#traceAnalysisAPI.arraybased.Signal.GetUnit "Link to this definition")  
Returns the unit of the signal.

Return type:  str

GetValueAt(*timestamp*)[¶](#traceAnalysisAPI.arraybased.Signal.GetValueAt "Link to this definition")  
Returns the signal value at a given timestamp.

Note:  
This method is not intended to be used in an iterative manner. To get multiple interpolated values use the static method [`NumpyBasedTraceStep.FitToAxis()`](#traceAnalysisAPI.arraybased.NumpyBasedTraceStep.FitToAxis "traceAnalysisAPI.arraybased.NumpyBasedTraceStep.FitToAxis").

Returns:  The signal value. Values will be interpolated by sample-and-hold. Returns None if the signal has no sample until timestamp.

Return type:  float|None

GetValues(*fromTo=None*, *\**, *leftOpen=False*, *rightOpen=True*)[¶](#traceAnalysisAPI.arraybased.Signal.GetValues "Link to this definition")  
Returns the values of the signal. The parameter fromTo can be used to only values in a given time range.

Parameters:  - **fromTo** (*tuple[float]*) – An optional tuple with timestamps (from, to) to get only the values in a given time range. By default, the time range is handled as right open interval. Use the parameters leftOpen and rightOpen to change this behavior. It is possible to set one of the limits to None to restrict the time axis only in one direction.

- **leftOpen** (*bool*) – Only valid if fromTo is given. Sets whether fromTo will be handled as left open interval (default False).

- **rightOpen** (*bool*) – Only valid if fromTo is given. Sets whether fromTo will be handled as right open interval (default True).

Note:  
The parameters leftOpen and rightOpen are keyword only arguments!

Return type:  numpy.ndarray

IsBound()[¶](#traceAnalysisAPI.arraybased.Signal.IsBound "Link to this definition")  
Returns if the trace step signal is bound to a generic signal of the trace analysis.

Return type:  bool

IsFound()[¶](#traceAnalysisAPI.arraybased.Signal.IsFound "Link to this definition")  
Returns if the signal is found (is bound, and is calculated or is found in the existing trace file).

Return type:  bool

IsOutSignal()[¶](#traceAnalysisAPI.arraybased.Signal.IsOutSignal "Link to this definition")  
Returns if the signal is an output signal.

Return type:  bool

## ReportTable[¶](#reporttable "Link to this heading")

*class* traceAnalysisAPI.arraybased.ReportTable[¶](#traceAnalysisAPI.arraybased.ReportTable "Link to this definition")  
A ReportTable object represents a table in the test report.

AddRow(*values: Iterable[str]*, *resultId: int | None = None*) → None[¶](#traceAnalysisAPI.arraybased.ReportTable.AddRow "Link to this definition")  
Appends a row to the table.

Parameters:  - **values** (*iterable*) – iterable with the entries for each column of the new row

- **resultId** (*result id* *or* *None*) – the result id of the row

SetHeader(*values: Iterable[str | int] | None*) → None[¶](#traceAnalysisAPI.arraybased.ReportTable.SetHeader "Link to this definition")  
Sets the table header.

Parameters:  **values** (*iterable*) – iterable with the entries for each column of the table header
