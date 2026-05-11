# Event based tracestep templates[¶](#event-based-tracestep-templates "Link to this heading")

## DataContainer[¶](#datacontainer "Link to this heading")

*class* traceAnalysisAPI.DataContainer[¶](#traceAnalysisAPI.DataContainer "Link to this definition")  
The DataContainer is a container to buffer values during the execution of Python based trace steps.

To assign a \<value\> to an arbitrary \<key\> just write:

    dataContainer.<key> = <value>

Example:

    dataContainer.index = 0

EmitSignal(*time*, *traceStepSignalName*, *value*)[¶](#traceAnalysisAPI.DataContainer.EmitSignal "Link to this definition")  
Emits a signal event back into the current trace analysis session.

Parameters:  - **time** (*float*) – timeStamp of the emitted signal event

- **traceStepSignalName** (*string*) – the name of the tracesteps output signal that should be emitted (see `TraceStep.DefineOutSignals()`)

- **value** (*float*) – the value of the emitted signal

GetTemplateSignalNames()[¶](#traceAnalysisAPI.DataContainer.GetTemplateSignalNames "Link to this definition")  
Returns the names of all user defined signal names in the trace step template.

Returns:  names of all user defined signal names in the trace step template

Return type:  list of strings

GetGenericSignalName(*templateSignalName*)[¶](#traceAnalysisAPI.DataContainer.GetGenericSignalName "Link to this definition")  
Returns the name of the assigned generic signal for a given signal name of the trace step template.

Parameters:  **templateSignalName** (*string*) – name of the template signal

Returns:  name of the generic signal

Return type:  string

GetMappingItemName(*templateSignalName*)[¶](#traceAnalysisAPI.DataContainer.GetMappingItemName "Link to this definition")  
Returns the name (of the reference (= source)) of the mapping item which corresponds to the assigned generic signal for a given signal name of the trace step template.

Parameters:  **templateSignalName** (*string*) – name of the template signal

Returns:  name (of the reference (= source)) of the mapping item

Return type:  string

GetOriginalSignalName(*templateSignalName*)[¶](#traceAnalysisAPI.DataContainer.GetOriginalSignalName "Link to this definition")  
Returns the original signal name of the assigned generic signal for a given signal name of the trace step template.

Parameters:  **templateSignalName** (*string*) – name of the template signal

Returns:  name of the original signal

Return type:  string

GetRecordingInfo(*templateSignalName*)[¶](#traceAnalysisAPI.DataContainer.GetRecordingInfo "Link to this definition")  
Returns the RecordingInfo of the assigned generic signal for a given signal name of the trace step template. If the returned value is not None, one can call the methods [`GetPath()`](#traceAnalysisAPI.RecordingInfo.GetPath "traceAnalysisAPI.RecordingInfo.GetPath"), [`GetRecordingName()`](#traceAnalysisAPI.RecordingInfo.GetRecordingName "traceAnalysisAPI.RecordingInfo.GetRecordingName"), [`GetRecordingNumber()`](#traceAnalysisAPI.RecordingInfo.GetRecordingNumber "traceAnalysisAPI.RecordingInfo.GetRecordingNumber") and [`GetRecordingType()`](#traceAnalysisAPI.RecordingInfo.GetRecordingType "traceAnalysisAPI.RecordingInfo.GetRecordingType") on the returned RecordingInfo object to obtain further information.

Parameters:  **templateSignalName** (*string*) – name of the template signal

Returns:  [`RecordingInfo`](#traceAnalysisAPI.RecordingInfo "traceAnalysisAPI.RecordingInfo") if the source of the assigned generic signal is a recording else None

Return type:  [`RecordingInfo`](#traceAnalysisAPI.RecordingInfo "traceAnalysisAPI.RecordingInfo") or None

GetGlobalConstantNames()[¶](#traceAnalysisAPI.DataContainer.GetGlobalConstantNames "Link to this definition")  
Returns a list of names containing all global constants.

Returns:  A list of names.

Return type:  list

GetGlobalConstant(*name*)[¶](#traceAnalysisAPI.DataContainer.GetGlobalConstant "Link to this definition")  
Returns the value of the given global constant.

Parameters:  **name** (*string*) – The name of the constant to retrieve the value.

Returns:  The value of the constant.

Return type:  object

IsSignalInRecording(*templateSignalName*)[¶](#traceAnalysisAPI.DataContainer.IsSignalInRecording "Link to this definition")  
Returns whether the signal associated with the given template signal was found in the recording specified by [`GetRecordingInfo()`](#traceAnalysisAPI.DataContainer.GetRecordingInfo "traceAnalysisAPI.DataContainer.GetRecordingInfo").

Parameters:  **templateSignalName** (*string*) – name of the template signal

Returns:  True if the associated signal was found in the corresponding recording else False

Return type:  bool

## Report[¶](#report "Link to this heading")

*class* traceAnalysisAPI.Report[¶](#traceAnalysisAPI.Report "Link to this definition")  
AddResultColumn(*name: str*) → None[¶](#traceAnalysisAPI.Report.AddResultColumn "Link to this definition")  
Adds a new column with the given name to the result table. It is appended at the end of the table. Values can be inserted into this column by using the parameter “additionalInfo” of the methods [`Spot()`](#traceAnalysisAPI.Report.Spot "traceAnalysisAPI.Report.Spot") and [`Range()`](#traceAnalysisAPI.Report.Range "traceAnalysisAPI.Report.Range"). The entries in the list “additionalInfo” list are inserted into the additional result columns in sequence.

Parameters:  **name** (*str*) – name of the new column

GetLastTable() → ReportTable[¶](#traceAnalysisAPI.Report.GetLastTable "Link to this definition")  
Returns the last table created.

Return type:  [`ReportTable`](#traceAnalysisAPI.ReportTable "traceAnalysisAPI.ReportTable")

GetResultId() → int | None[¶](#traceAnalysisAPI.Report.GetResultId "Link to this definition")  
Gets the current result id.

The result id passed to an earlier call to [`SetResultId()`](#traceAnalysisAPI.Report.SetResultId "traceAnalysisAPI.Report.SetResultId") is returned. If [`SetResultId()`](#traceAnalysisAPI.Report.SetResultId "traceAnalysisAPI.Report.SetResultId") wasn’t called before, `dataContainer.RESULT_ID_NONE` is returned.

Returns:  the result id

Return type:  int

GetTable(*tableId: str*) → ReportTable[¶](#traceAnalysisAPI.Report.GetTable "Link to this definition")  
Returns the table with the given id.

Parameters:  **tableId** (*str*) – id of the table

Return type:  [`ReportTable`](#traceAnalysisAPI.ReportTable "traceAnalysisAPI.ReportTable")

GetTableByIndex(*index: int*) → ReportTable[¶](#traceAnalysisAPI.Report.GetTableByIndex "Link to this definition")  
Returns the table by the given position in the list of user-defined tables.

Parameters:  **index** (*int*) – the position of the table

Return type:  [`ReportTable`](#traceAnalysisAPI.ReportTable "traceAnalysisAPI.ReportTable")

GetTableCount() → int[¶](#traceAnalysisAPI.Report.GetTableCount "Link to this definition")  
Returns the count of tables.

Returns:  The count of tables.

Return type:  int

HasTable(*tableId: str*) → bool[¶](#traceAnalysisAPI.Report.HasTable "Link to this definition")  
Returns whether a particular table exists for the trace step.

Parameters:  **tableId** (*str*) – id of the table

Returns:  True if a table with the given id exists, else False

Return type:  bool

Image(*imageSource: str | Path | ImageInterface | ndarray | bytes*, *\**, *name: str | None = None*, *title: str | None = None*, *embedded: bool = False*, *limitPreviewSize: bool = True*, *autoDelete: bool = False*, *useTemp: bool = True*) → ReportImage[¶](#traceAnalysisAPI.Report.Image "Link to this definition")  
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

Log(*level*, *time*, *message*, *\*formatArgs*, *\*\*formatKwargs*)[¶](#traceAnalysisAPI.Report.Log "Link to this definition")  
Adds a log message to the trace analysis log file. Use [`SetLogComponent()`](#traceAnalysisAPI.Report.SetLogComponent "traceAnalysisAPI.Report.SetLogComponent") to set the component part of the log entry.

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

LogDebug(*time*, *message*, *\*formatArgs*, *\*\*formatKwargs*)[¶](#traceAnalysisAPI.Report.LogDebug "Link to this definition")  
Convenience method to add a debug log message. See [`Log()`](#traceAnalysisAPI.Report.Log "traceAnalysisAPI.Report.Log") for further usage.

LogError(*time*, *message*, *\*formatArgs*, *\*\*formatKwargs*)[¶](#traceAnalysisAPI.Report.LogError "Link to this definition")  
Convenience method to add an error log message. See [`Log()`](#traceAnalysisAPI.Report.Log "traceAnalysisAPI.Report.Log") for further usage.

LogInfo(*time*, *message*, *\*formatArgs*, *\*\*formatKwargs*)[¶](#traceAnalysisAPI.Report.LogInfo "Link to this definition")  
Convenience method to add an info log message. See [`Log()`](#traceAnalysisAPI.Report.Log "traceAnalysisAPI.Report.Log") for further usage.

LogWarning(*time*, *message*, *\*formatArgs*, *\*\*formatKwargs*)[¶](#traceAnalysisAPI.Report.LogWarning "Link to this definition")  
Convenience method to add a warning log message. See [`Log()`](#traceAnalysisAPI.Report.Log "traceAnalysisAPI.Report.Log") for further usage.

Range(*startTime: float | numpy.integer | numpy.floating*, *endTime: float | numpy.integer | numpy.floating*, *message: str = ''*, *resultId: int | None = None*, *additionalInfo: list[str] | None = None*) → RangeEntity[¶](#traceAnalysisAPI.Report.Range "Link to this definition")  
Adds a range to the test report and returns a range object.

Parameters:  - **startTime** (*float*) – timestamp at which the range begins

- **endTime** (*float*) – timestamp at which the range ends

- **message** (*str*) – a textual message describing the range

- **resultId** (*int*) – the verdict for the range

- **additionalInfo** (*list* *of* *strings*) – a list of additional information, that will be shown in the custom result columns (see [`AddResultColumn()`](#traceAnalysisAPI.Report.AddResultColumn "traceAnalysisAPI.Report.AddResultColumn"))

Return type:  [`Range`](#traceAnalysisAPI.Range "traceAnalysisAPI.Range")

RemoveTable(*tableId: str*) → None[¶](#traceAnalysisAPI.Report.RemoveTable "Link to this definition")  
Removes a table from the test report.

Parameters:  **tableId** (*str*) – id of the table

SetLogComponent(*component*)[¶](#traceAnalysisAPI.Report.SetLogComponent "Link to this definition")  
Sets the component that will be used in logging entries created by calling log methods.

Parameters:  **component** (*str*) – name of the component

SetResultError()[¶](#traceAnalysisAPI.Report.SetResultError "Link to this definition")  
Convenience method for report.SetResultId(report.RESULT_ID_ERROR)

SetResultFailed()[¶](#traceAnalysisAPI.Report.SetResultFailed "Link to this definition")  
Convenience method for report.SetResultId(report.RESULT_ID_FAILED)

SetResultId(*resultId*)[¶](#traceAnalysisAPI.Report.SetResultId "Link to this definition")  
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

The result id is set directly. It is not affected by earlier calls to [`SetResultId()`](#traceAnalysisAPI.Report.SetResultId "traceAnalysisAPI.Report.SetResultId").

Example:

    report.SetResultId(report.RESULT_ID_ERROR)
    report.SetResultId(report.RESULT_ID_NONE)

    report.GetResultId() # this will result in report.RESULT_ID_NONE

Parameters:  **resultId** (*result id*) – the result id to set

SetResultInconclusive()[¶](#traceAnalysisAPI.Report.SetResultInconclusive "Link to this definition")  
Convenience method for report.SetResultId(report.RESULT_ID_INCONCLUSIVE)

SetResultSuccess()[¶](#traceAnalysisAPI.Report.SetResultSuccess "Link to this definition")  
Convenience method for report.SetResultId(report.RESULT_ID_SUCCESS)

SetResultText(*text: str | None*) → None[¶](#traceAnalysisAPI.Report.SetResultText "Link to this definition")  
Sets a user-defined text for the result of the report.

Parameters:  **text** (*str*) – the text

Spot(*time*, *message=''*, *resultId=None*, *additionalInfo=None*)[¶](#traceAnalysisAPI.Report.Spot "Link to this definition")  
Adds a signal spot to the test report.

Parameters:  - **time** (*float*) – timestamp of the spot

- **message** (*an object,* *that can be converted to via str(message)*) – a textual message describing the spot

- **resultId** (*result id*) – the verdict for the spot

- **additionalInfo** (*list* *of* *strings*) – a list of additional information, that will be shown in the custom result columns (see [`AddResultColumn()`](#traceAnalysisAPI.Report.AddResultColumn "traceAnalysisAPI.Report.AddResultColumn"))

Table(*tableId: str | int | None = None*, *headerValues: Iterable[str | int] | None = None*) → ReportTable[¶](#traceAnalysisAPI.Report.Table "Link to this definition")  
Creates a table in the test report.

Example:

    table = report.Table("table1", ["time", "description"])
    table.AddRow(["1.3", "A rising edge detected"])
    table.AddRow(["3.8", "A falling edge detected"])

Parameters:  - **tableId** (*str*) – id to identify the table

- **headerValues** (*iterable*) – iterable with the entries of the table header

Returns:  the report table object

Return type:  [`ReportTable`](#traceAnalysisAPI.ReportTable "traceAnalysisAPI.ReportTable")

UpdateResultId(*resultId*)[¶](#traceAnalysisAPI.Report.UpdateResultId "Link to this definition")  
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

In contrast to [`SetResultId()`](#traceAnalysisAPI.Report.SetResultId "traceAnalysisAPI.Report.SetResultId"), which sets the resultId directly, [`UpdateResultId()`](#traceAnalysisAPI.Report.UpdateResultId "traceAnalysisAPI.Report.UpdateResultId") can only increase the resultId according to the following ordering:

RESULT_ID_NONE \< RESULT_ID_SUCCESS \< RESULT_ID_INCONCLUSIVE \< RESULT_ID_FAILED \< RESULT_ID_ERROR

Note

[`UpdateResultId()`](#traceAnalysisAPI.Report.UpdateResultId "traceAnalysisAPI.Report.UpdateResultId") can bee seen as equivalent to SetResultId(max(resultId, GetResultId()))

Example:

    report.UpdateResultId(report.RESULT_ID_SUCCESS)
    ...
    report.UpdateResultId(report.RESULT_ID_FAILED)
    ...
    report.UpdateResultId(report.RESULT_ID_SUCCESS)

    report.GetResultId() # this will result in report.RESULT_ID_FAILED

Parameters:  **resultId** (*result id*) – the result id to set

## SignalEvent[¶](#signalevent "Link to this heading")

*class* traceAnalysisAPI.SignalEvent[¶](#traceAnalysisAPI.SignalEvent "Link to this definition")  
A SignalEvent consists of a time stamp and multiple signal values. From the perspective of a `TraceStep` there is a constant stream of SignalEvent objects coming in, whose time stamps follow a strict partial order (that is, there are no duplicate time stamps).

GetSignal(*name: str*) → [Signal](#traceAnalysisAPI.Signal "ttTraceCheckLib.signalEvent.Signal") | None[¶](#traceAnalysisAPI.SignalEvent.GetSignal "Link to this definition")  
Returns the current signal (see [`Signal`](#traceAnalysisAPI.Signal "traceAnalysisAPI.Signal")) for a given signal name (see `TraceStep.DefineInSignals()`) if it is contained in this SignalEvent.

Parameters:  **name** (*string*) – the name of the desired signal

Return type:  [`Signal`](#traceAnalysisAPI.Signal "traceAnalysisAPI.Signal") or None

GetSignals() → dict[str, [Signal](#traceAnalysisAPI.Signal "ttTraceCheckLib.signalEvent.Signal")][¶](#traceAnalysisAPI.SignalEvent.GetSignals "Link to this definition")  
Returns a dictionary mapping signal names (see `TraceStep.DefineInSignals()`) to signals (see [`Signal`](#traceAnalysisAPI.Signal "traceAnalysisAPI.Signal"))

Return type:  dict(string -> [`Signal`](#traceAnalysisAPI.Signal "traceAnalysisAPI.Signal"))

GetTime() → float[¶](#traceAnalysisAPI.SignalEvent.GetTime "Link to this definition")  
Returns the time stamp of the SignalEvent

Return type:  float

GetValue(*name: str*) → float | dict[str, float | dict[str | None, float]] | None[¶](#traceAnalysisAPI.SignalEvent.GetValue "Link to this definition")  
Returns the current signal value (see [`Signal.GetValue()`](#traceAnalysisAPI.Signal.GetValue "traceAnalysisAPI.Signal.GetValue")) for a given signal name (see `TraceStep.DefineInSignals()`) if it is contained in this SignalEvent.

Parameters:  **name** (*string*) – the name of the desired signal

Return type:  float/string or None

## Hold[¶](#hold "Link to this heading")

*class* traceAnalysisAPI.Hold[¶](#traceAnalysisAPI.Hold "Link to this definition")  
GetSignal(*name*)[¶](#traceAnalysisAPI.Hold.GetSignal "Link to this definition")  
Returns the last known signal (see [`Signal`](#traceAnalysisAPI.Signal "traceAnalysisAPI.Signal")) for a given signal name (see `TraceStep.DefineInSignals()`) if it is contained in this SignalEvent.

Parameters:  **name** (*str*) – the name of the desired signal

Return type:  [`Signal`](#traceAnalysisAPI.Signal "traceAnalysisAPI.Signal") or None

GetSignals()[¶](#traceAnalysisAPI.Hold.GetSignals "Link to this definition")  
Returns a dictionary mapping signal names (see `TraceStep.DefineInSignals()`) to the last known signals (see [`Signal`](#traceAnalysisAPI.Signal "traceAnalysisAPI.Signal"))

Return type:  dict(str -> [`Signal`](#traceAnalysisAPI.Signal "traceAnalysisAPI.Signal"))

GetValue(*name*)[¶](#traceAnalysisAPI.Hold.GetValue "Link to this definition")  
Returns the last known signal value (see [`Signal.GetValue()`](#traceAnalysisAPI.Signal.GetValue "traceAnalysisAPI.Signal.GetValue")) for a given signal name (see `TraceStep.DefineInSignals()`).

Parameters:  **name** (*str*) – the name of the desired signal

Return type:  float or None

## Parameters[¶](#parameters "Link to this heading")

TraceStep.parameters *= {}*[¶](#traceAnalysisAPI.TraceStep.parameters "Link to this definition")  
A dictionary mapping the names of the user defined trace step parameters to their values.

Example:

The tracestep has a parameter “Parameter_0” with integer value 100:

    parameters["Parameter_0"] # returns 100 

## Signal[¶](#signal "Link to this heading")

*class* traceAnalysisAPI.Signal[¶](#traceAnalysisAPI.Signal "Link to this definition")  
A Signal object encapsulates the measurement value of one signal at a given point of time.

GetName() → str[¶](#traceAnalysisAPI.Signal.GetName "Link to this definition")  
Returns the name of the signal.

Return type:  string

GetPrevValue(*restricted: bool = False*) → object | None[¶](#traceAnalysisAPI.Signal.GetPrevValue "Link to this definition")  
Returns last known value of the signal before the current signal event.

Note

GetPrevValue() and GetValue() can return the same value,

if the signal has been measured with the same value twice in a row, which is not uncommon, especially for signals, that have been upsampled before traceanalysis by means of value duplication

Parameters:  **restricted** (*bool*) – if True only previous values within the current trigger range are returned, the parameter has only an effect at the beginning of a trigger range

Return type:  float or None

GetTime() → float | None[¶](#traceAnalysisAPI.Signal.GetTime "Link to this definition")  
Returns the timestamp of the [`SignalEvent`](#traceAnalysisAPI.SignalEvent "traceAnalysisAPI.SignalEvent") from which the signal stems.

Return type:  string

GetValue() → float | dict[str, float | dict[str | None, float]] | None[¶](#traceAnalysisAPI.Signal.GetValue "Link to this definition")  
Returns the value of the signal.

Return type:  float

## RecordingInfo[¶](#recordinginfo "Link to this heading")

*class* traceAnalysisAPI.RecordingInfo[¶](#traceAnalysisAPI.RecordingInfo "Link to this definition")  
A RecordingInfo object contains information about the name, number, type and path of the underlying recording from which the signal stems.

GetFirstPath() → str | None[¶](#traceAnalysisAPI.RecordingInfo.GetFirstPath "Link to this definition")  
Returns the first path of the path list of the recordings or None, if the list is empty.

Returns:  path of the first recording, if exists

GetPath(*idx=0*) → str | None[¶](#traceAnalysisAPI.RecordingInfo.GetPath "Link to this definition")  
Returns the path (or the first path if there is a list of paths) for the recording.

Returns:  The path

GetPathList() → list[str][¶](#traceAnalysisAPI.RecordingInfo.GetPathList "Link to this definition")  
Returns the path list of the recordings.

Returns:  path list of the recordings

GetRecordingName() → str | None[¶](#traceAnalysisAPI.RecordingInfo.GetRecordingName "Link to this definition")  
Returns the name of the recording.

Returns:  the name of the recording

GetRecordingNumber() → int[¶](#traceAnalysisAPI.RecordingInfo.GetRecordingNumber "Link to this definition")  
Returns the number of the recording.

Returns:  the number of the recording (\>=0, and \< the total number of the associated recording group)

GetRecordingType() → str[¶](#traceAnalysisAPI.RecordingInfo.GetRecordingType "Link to this definition")  
Returns the type of the recording.

Returns:  type of the recording

## ReportTable[¶](#reporttable "Link to this heading")

*class* traceAnalysisAPI.ReportTable[¶](#traceAnalysisAPI.ReportTable "Link to this definition")  
A ReportTable object represents a table in the test report.

AddRow(*values: Iterable[str]*, *resultId: int | None = None*) → None[¶](#traceAnalysisAPI.ReportTable.AddRow "Link to this definition")  
Appends a row to the table.

Parameters:  - **values** (*iterable*) – iterable with the entries for each column of the new row

- **resultId** (*result id* *or* *None*) – the result id of the row

SetHeader(*values: Iterable[str | int] | None*) → None[¶](#traceAnalysisAPI.ReportTable.SetHeader "Link to this definition")  
Sets the table header.

Parameters:  **values** (*iterable*) – iterable with the entries for each column of the table header

## Range[¶](#range "Link to this heading")

*class* traceAnalysisAPI.Range[¶](#traceAnalysisAPI.Range "Link to this definition")  
Class representing a range in the test report. An instance of Range is returned by the call of [`Report.Range()`](#traceAnalysisAPI.Report.Range "traceAnalysisAPI.Report.Range"). To specify the range in more detail, it is possible to add spots and sub ranges as children to a range object.

Range(*startTime*, *endTime*, *message=''*, *resultId=None*, *additionalInfo=None*)[¶](#traceAnalysisAPI.Range.Range "Link to this definition")  
Adds a sub range to the range.

Parameters:  - **startTime** (*float*) – timestamp at which the sub range begins

- **endTime** (*float*) – timestamp at which the sub range ends

- **message** (*string*) – a textual message describing the sub range

- **resultId** (*int*) – the verdict for the sub range

- **additionalInfo** (*list* *of* *strings*) – a list of additional information, that will be shown in the custom result columns (see [`Report.AddResultColumn()`](#traceAnalysisAPI.Report.AddResultColumn "traceAnalysisAPI.Report.AddResultColumn"))

Spot(*time*, *message=None*, *resultId=None*, *additionalInfo=None*)[¶](#traceAnalysisAPI.Range.Spot "Link to this definition")  
Adds a signal spot to a range.

Parameters:  - **time** (*float*) – timestamp of the spot

- **message** (*string*) – a textual message describing the spot

- **resultId** (*int*) – the verdict for the spot

- **additionalInfo** (*list* *of* *strings*) – a list of additional information, that will be shown in the custom result columns (see [`Report.AddResultColumn()`](#traceAnalysisAPI.Report.AddResultColumn "traceAnalysisAPI.Report.AddResultColumn"))
