# Stream based tracestep templates[¶](#stream-based-tracestep-templates "Link to this heading")

## DataContainer[¶](#datacontainer "Link to this heading")

*class* traceAnalysisAPI.streambased.DataContainer[¶](#traceAnalysisAPI.streambased.DataContainer "Link to this definition")  
The DataContainer is a container to buffer values during the execution of Python based trace steps.

To assign a \<value\> to an arbitrary \<key\> just write:

    dataContainer.<key> = <value>

Example:

    dataContainer.index = 0

GetTemplateSignalNames()[¶](#traceAnalysisAPI.streambased.DataContainer.GetTemplateSignalNames "Link to this definition")  
Returns the names of all user defined signal names in the trace step template.

Returns:  names of all user defined signal names in the trace step template

Return type:  list of strings

GetGenericSignalName(*templateSignalName*)[¶](#traceAnalysisAPI.streambased.DataContainer.GetGenericSignalName "Link to this definition")  
Returns the name of the assigned generic signal for a given signal name of the trace step template.

Parameters:  **templateSignalName** (*string*) – name of the template signal

Returns:  name of the generic signal

Return type:  string

GetMappingItemName(*templateSignalName*)[¶](#traceAnalysisAPI.streambased.DataContainer.GetMappingItemName "Link to this definition")  
Returns the name (of the reference (= source)) of the mapping item which corresponds to the assigned generic signal for a given signal name of the trace step template.

Parameters:  **templateSignalName** (*string*) – name of the template signal

Returns:  name (of the reference (= source)) of the mapping item

Return type:  string

GetOriginalSignalName(*templateSignalName*)[¶](#traceAnalysisAPI.streambased.DataContainer.GetOriginalSignalName "Link to this definition")  
Returns the original signal name of the assigned generic signal for a given signal name of the trace step template.

Parameters:  **templateSignalName** (*string*) – name of the template signal

Returns:  name of the original signal

Return type:  string

GetGlobalConstantNames()[¶](#traceAnalysisAPI.streambased.DataContainer.GetGlobalConstantNames "Link to this definition")  
Returns a list of names containing all global constants.

Returns:  A list of names.

Return type:  list

GetGlobalConstant(*name*)[¶](#traceAnalysisAPI.streambased.DataContainer.GetGlobalConstant "Link to this definition")  
Returns the value of the given global constant.

Parameters:  **name** (*string*) – The name of the constant to retrieve the value.

Returns:  The value of the constant.

Return type:  object

SetVariableValue(*name*, *value*)[¶](#traceAnalysisAPI.streambased.DataContainer.SetVariableValue "Link to this definition")  
Note

Please consider using parameters and return values in your trace step template instead of using this method. This method should only be used for special use cases where an uncertain amount of variables shall be initialized.

Sets the value of the package variable with the given name.

If no variable with the given name exists in the trace analysis namespace, an error is raised. The new value of the variable cannot be accessed from within the same episode.

Parameters:  - **name** (*string*) – name of the package variable that shall be set

- **value** (*Python object*) – value to be set

## Report[¶](#report "Link to this heading")

*class* traceAnalysisAPI.streambased.Report[¶](#traceAnalysisAPI.streambased.Report "Link to this definition")  
AddResultColumn(*name: str*) → None[¶](#traceAnalysisAPI.streambased.Report.AddResultColumn "Link to this definition")  
Adds a new column with the given name to the result table. It is appended at the end of the table. Values can be inserted into this column by using the parameter “additionalInfo” of the methods [`Spot()`](#traceAnalysisAPI.streambased.Report.Spot "traceAnalysisAPI.streambased.Report.Spot") and [`Range()`](#traceAnalysisAPI.streambased.Report.Range "traceAnalysisAPI.streambased.Report.Range"). The entries in the list “additionalInfo” list are inserted into the additional result columns in sequence.

Parameters:  **name** (*str*) – name of the new column

GetLastTable() → ReportTable[¶](#traceAnalysisAPI.streambased.Report.GetLastTable "Link to this definition")  
Returns the last table created.

Return type:  [`ReportTable`](#traceAnalysisAPI.streambased.ReportTable "traceAnalysisAPI.streambased.ReportTable")

GetResultId() → int | None[¶](#traceAnalysisAPI.streambased.Report.GetResultId "Link to this definition")  
Gets the current result id.

The result id passed to an earlier call to [`SetResultId()`](#traceAnalysisAPI.streambased.Report.SetResultId "traceAnalysisAPI.streambased.Report.SetResultId") is returned. If [`SetResultId()`](#traceAnalysisAPI.streambased.Report.SetResultId "traceAnalysisAPI.streambased.Report.SetResultId") wasn’t called before, `dataContainer.RESULT_ID_NONE` is returned.

Returns:  the result id

Return type:  int

GetTable(*tableId: str*) → ReportTable[¶](#traceAnalysisAPI.streambased.Report.GetTable "Link to this definition")  
Returns the table with the given id.

Parameters:  **tableId** (*str*) – id of the table

Return type:  [`ReportTable`](#traceAnalysisAPI.streambased.ReportTable "traceAnalysisAPI.streambased.ReportTable")

GetTableByIndex(*index: int*) → ReportTable[¶](#traceAnalysisAPI.streambased.Report.GetTableByIndex "Link to this definition")  
Returns the table by the given position in the list of user-defined tables.

Parameters:  **index** (*int*) – the position of the table

Return type:  [`ReportTable`](#traceAnalysisAPI.streambased.ReportTable "traceAnalysisAPI.streambased.ReportTable")

GetTableCount() → int[¶](#traceAnalysisAPI.streambased.Report.GetTableCount "Link to this definition")  
Returns the count of tables.

Returns:  The count of tables.

Return type:  int

HasTable(*tableId: str*) → bool[¶](#traceAnalysisAPI.streambased.Report.HasTable "Link to this definition")  
Returns whether a particular table exists for the trace step.

Parameters:  **tableId** (*str*) – id of the table

Returns:  True if a table with the given id exists, else False

Return type:  bool

Image(*imageSource: str | Path | ImageInterface | ndarray | bytes*, *\**, *name: str | None = None*, *title: str | None = None*, *embedded: bool = False*, *limitPreviewSize: bool = True*, *autoDelete: bool = False*, *useTemp: bool = True*) → ReportImage[¶](#traceAnalysisAPI.streambased.Report.Image "Link to this definition")  
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

Log(*level*, *time*, *message*, *\*formatArgs*, *\*\*formatKwargs*)[¶](#traceAnalysisAPI.streambased.Report.Log "Link to this definition")  
Adds a log message to the trace analysis log file. Use [`SetLogComponent()`](#traceAnalysisAPI.streambased.Report.SetLogComponent "traceAnalysisAPI.streambased.Report.SetLogComponent") to set the component part of the log entry.

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

LogDebug(*time*, *message*, *\*formatArgs*, *\*\*formatKwargs*)[¶](#traceAnalysisAPI.streambased.Report.LogDebug "Link to this definition")  
Convenience method to add a debug log message. See [`Log()`](#traceAnalysisAPI.streambased.Report.Log "traceAnalysisAPI.streambased.Report.Log") for further usage.

LogError(*time*, *message*, *\*formatArgs*, *\*\*formatKwargs*)[¶](#traceAnalysisAPI.streambased.Report.LogError "Link to this definition")  
Convenience method to add an error log message. See [`Log()`](#traceAnalysisAPI.streambased.Report.Log "traceAnalysisAPI.streambased.Report.Log") for further usage.

LogInfo(*time*, *message*, *\*formatArgs*, *\*\*formatKwargs*)[¶](#traceAnalysisAPI.streambased.Report.LogInfo "Link to this definition")  
Convenience method to add an info log message. See [`Log()`](#traceAnalysisAPI.streambased.Report.Log "traceAnalysisAPI.streambased.Report.Log") for further usage.

LogWarning(*time*, *message*, *\*formatArgs*, *\*\*formatKwargs*)[¶](#traceAnalysisAPI.streambased.Report.LogWarning "Link to this definition")  
Convenience method to add a warning log message. See [`Log()`](#traceAnalysisAPI.streambased.Report.Log "traceAnalysisAPI.streambased.Report.Log") for further usage.

Range(*startTime: float | numpy.integer | numpy.floating*, *endTime: float | numpy.integer | numpy.floating*, *message: str = ''*, *resultId: int | None = None*, *additionalInfo: list[str] | None = None*) → RangeEntity[¶](#traceAnalysisAPI.streambased.Report.Range "Link to this definition")  
Adds a range to the test report and returns a range object.

Parameters:  - **startTime** (*float*) – timestamp at which the range begins

- **endTime** (*float*) – timestamp at which the range ends

- **message** (*str*) – a textual message describing the range

- **resultId** (*int*) – the verdict for the range

- **additionalInfo** (*list* *of* *strings*) – a list of additional information, that will be shown in the custom result columns (see [`AddResultColumn()`](#traceAnalysisAPI.streambased.Report.AddResultColumn "traceAnalysisAPI.streambased.Report.AddResultColumn"))

Return type:  [`Range`](#traceAnalysisAPI.streambased.Range "traceAnalysisAPI.streambased.Range")

RemoveTable(*tableId: str*) → None[¶](#traceAnalysisAPI.streambased.Report.RemoveTable "Link to this definition")  
Removes a table from the test report.

Parameters:  **tableId** (*str*) – id of the table

SetLogComponent(*component*)[¶](#traceAnalysisAPI.streambased.Report.SetLogComponent "Link to this definition")  
Sets the component that will be used in logging entries created by calling log methods.

Parameters:  **component** (*str*) – name of the component

SetResultError()[¶](#traceAnalysisAPI.streambased.Report.SetResultError "Link to this definition")  
Convenience method for report.SetResultId(report.RESULT_ID_ERROR)

SetResultFailed()[¶](#traceAnalysisAPI.streambased.Report.SetResultFailed "Link to this definition")  
Convenience method for report.SetResultId(report.RESULT_ID_FAILED)

SetResultId(*resultId*)[¶](#traceAnalysisAPI.streambased.Report.SetResultId "Link to this definition")  
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

The result id is set directly. It is not affected by earlier calls to [`SetResultId()`](#traceAnalysisAPI.streambased.Report.SetResultId "traceAnalysisAPI.streambased.Report.SetResultId").

Example:

    report.SetResultId(report.RESULT_ID_ERROR)
    report.SetResultId(report.RESULT_ID_NONE)

    report.GetResultId() # this will result in report.RESULT_ID_NONE

Parameters:  **resultId** (*result id*) – the result id to set

SetResultInconclusive()[¶](#traceAnalysisAPI.streambased.Report.SetResultInconclusive "Link to this definition")  
Convenience method for report.SetResultId(report.RESULT_ID_INCONCLUSIVE)

SetResultSuccess()[¶](#traceAnalysisAPI.streambased.Report.SetResultSuccess "Link to this definition")  
Convenience method for report.SetResultId(report.RESULT_ID_SUCCESS)

SetResultText(*text: str | None*) → None[¶](#traceAnalysisAPI.streambased.Report.SetResultText "Link to this definition")  
Sets a user-defined text for the result of the report.

Parameters:  **text** (*str*) – the text

Spot(*time*, *message=''*, *resultId=None*, *additionalInfo=None*)[¶](#traceAnalysisAPI.streambased.Report.Spot "Link to this definition")  
Adds a signal spot to the test report.

Parameters:  - **time** (*float*) – timestamp of the spot

- **message** (*an object,* *that can be converted to via str(message)*) – a textual message describing the spot

- **resultId** (*result id*) – the verdict for the spot

- **additionalInfo** (*list* *of* *strings*) – a list of additional information, that will be shown in the custom result columns (see [`AddResultColumn()`](#traceAnalysisAPI.streambased.Report.AddResultColumn "traceAnalysisAPI.streambased.Report.AddResultColumn"))

Table(*tableId: str | int | None = None*, *headerValues: Iterable[str | int] | None = None*) → ReportTable[¶](#traceAnalysisAPI.streambased.Report.Table "Link to this definition")  
Creates a table in the test report.

Example:

    table = report.Table("table1", ["time", "description"])
    table.AddRow(["1.3", "A rising edge detected"])
    table.AddRow(["3.8", "A falling edge detected"])

Parameters:  - **tableId** (*str*) – id to identify the table

- **headerValues** (*iterable*) – iterable with the entries of the table header

Returns:  the report table object

Return type:  [`ReportTable`](#traceAnalysisAPI.streambased.ReportTable "traceAnalysisAPI.streambased.ReportTable")

UpdateResultId(*resultId*)[¶](#traceAnalysisAPI.streambased.Report.UpdateResultId "Link to this definition")  
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

In contrast to [`SetResultId()`](#traceAnalysisAPI.streambased.Report.SetResultId "traceAnalysisAPI.streambased.Report.SetResultId"), which sets the resultId directly, [`UpdateResultId()`](#traceAnalysisAPI.streambased.Report.UpdateResultId "traceAnalysisAPI.streambased.Report.UpdateResultId") can only increase the resultId according to the following ordering:

RESULT_ID_NONE \< RESULT_ID_SUCCESS \< RESULT_ID_INCONCLUSIVE \< RESULT_ID_FAILED \< RESULT_ID_ERROR

Note

[`UpdateResultId()`](#traceAnalysisAPI.streambased.Report.UpdateResultId "traceAnalysisAPI.streambased.Report.UpdateResultId") can bee seen as equivalent to SetResultId(max(resultId, GetResultId()))

Example:

    report.UpdateResultId(report.RESULT_ID_SUCCESS)
    ...
    report.UpdateResultId(report.RESULT_ID_FAILED)
    ...
    report.UpdateResultId(report.RESULT_ID_SUCCESS)

    report.GetResultId() # this will result in report.RESULT_ID_FAILED

Parameters:  **resultId** (*result id*) – the result id to set

## Parameters[¶](#parameters "Link to this heading")

TraceStep.parameters *= {}*[¶](#traceAnalysisAPI.streambased.TraceStep.parameters "Link to this definition")  
A dictionary mapping the names of the user defined trace step parameters to their values.

Example:

The tracestep has a parameter “Parameter_0” with integer value 100:

    parameters["Parameter_0"] # returns 100 

## RecordingInfo[¶](#recordinginfo "Link to this heading")

*class* traceAnalysisAPI.streambased.RecordingInfo[¶](#traceAnalysisAPI.streambased.RecordingInfo "Link to this definition")  
A RecordingInfo object contains information about the name, number, type and path of the underlying recording from which the signal stems.

GetFirstPath() → str | None[¶](#traceAnalysisAPI.streambased.RecordingInfo.GetFirstPath "Link to this definition")  
Returns the first path of the path list of the recordings or None, if the list is empty.

Returns:  path of the first recording, if exists

GetPath(*idx=0*) → str | None[¶](#traceAnalysisAPI.streambased.RecordingInfo.GetPath "Link to this definition")  
Returns the path (or the first path if there is a list of paths) for the recording.

Returns:  The path

GetPathList() → list[str][¶](#traceAnalysisAPI.streambased.RecordingInfo.GetPathList "Link to this definition")  
Returns the path list of the recordings.

Returns:  path list of the recordings

GetRecordingName() → str | None[¶](#traceAnalysisAPI.streambased.RecordingInfo.GetRecordingName "Link to this definition")  
Returns the name of the recording.

Returns:  the name of the recording

GetRecordingNumber() → int[¶](#traceAnalysisAPI.streambased.RecordingInfo.GetRecordingNumber "Link to this definition")  
Returns the number of the recording.

Returns:  the number of the recording (\>=0, and \< the total number of the associated recording group)

GetRecordingType() → str[¶](#traceAnalysisAPI.streambased.RecordingInfo.GetRecordingType "Link to this definition")  
Returns the type of the recording.

Returns:  type of the recording

## ReportTable[¶](#reporttable "Link to this heading")

*class* traceAnalysisAPI.streambased.ReportTable[¶](#traceAnalysisAPI.streambased.ReportTable "Link to this definition")  
A ReportTable object represents a table in the test report.

AddRow(*values: Iterable[str]*, *resultId: int | None = None*) → None[¶](#traceAnalysisAPI.streambased.ReportTable.AddRow "Link to this definition")  
Appends a row to the table.

Parameters:  - **values** (*iterable*) – iterable with the entries for each column of the new row

- **resultId** (*result id* *or* *None*) – the result id of the row

SetHeader(*values: Iterable[str | int] | None*) → None[¶](#traceAnalysisAPI.streambased.ReportTable.SetHeader "Link to this definition")  
Sets the table header.

Parameters:  **values** (*iterable*) – iterable with the entries for each column of the table header

## Range[¶](#range "Link to this heading")

*class* traceAnalysisAPI.streambased.Range[¶](#traceAnalysisAPI.streambased.Range "Link to this definition")  
Class representing a range in the test report. An instance of Range is returned by the call of [`Report.Range()`](#traceAnalysisAPI.streambased.Report.Range "traceAnalysisAPI.streambased.Report.Range"). To specify the range in more detail, it is possible to add spots and sub ranges as children to a range object.

Range(*startTime*, *endTime*, *message=''*, *resultId=None*, *additionalInfo=None*)[¶](#traceAnalysisAPI.streambased.Range.Range "Link to this definition")  
Adds a sub range to the range.

Parameters:  - **startTime** (*float*) – timestamp at which the sub range begins

- **endTime** (*float*) – timestamp at which the sub range ends

- **message** (*string*) – a textual message describing the sub range

- **resultId** (*int*) – the verdict for the sub range

- **additionalInfo** (*list* *of* *strings*) – a list of additional information, that will be shown in the custom result columns (see [`Report.AddResultColumn()`](#traceAnalysisAPI.streambased.Report.AddResultColumn "traceAnalysisAPI.streambased.Report.AddResultColumn"))

Spot(*time*, *message=None*, *resultId=None*, *additionalInfo=None*)[¶](#traceAnalysisAPI.streambased.Range.Spot "Link to this definition")  
Adds a signal spot to a range.

Parameters:  - **time** (*float*) – timestamp of the spot

- **message** (*string*) – a textual message describing the spot

- **resultId** (*int*) – the verdict for the spot

- **additionalInfo** (*list* *of* *strings*) – a list of additional information, that will be shown in the custom result columns (see [`Report.AddResultColumn()`](#traceAnalysisAPI.streambased.Report.AddResultColumn "traceAnalysisAPI.streambased.Report.AddResultColumn"))
