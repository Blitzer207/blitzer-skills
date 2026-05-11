[ Array-based NumPy trace step templates ](array_based_templates.md)

[ Event based tracestep templates ](event_based_templates.md)

Stream based tracestep templates [ Stream based tracestep templates ](#)

Stream based tracestep templates

- [ DataContainer ](#datacontainer)
  - [C traceAnalysisAPI.streambased.DataContainer ](#traceAnalysisAPI.streambased.DataContainer)
    - [M GetTemplateSignalNames ](#traceAnalysisAPI.streambased.DataContainer.GetTemplateSignalNames)
    - [M GetGenericSignalName ](#traceAnalysisAPI.streambased.DataContainer.GetGenericSignalName)
    - [M GetMappingItemName ](#traceAnalysisAPI.streambased.DataContainer.GetMappingItemName)
    - [M GetOriginalSignalName ](#traceAnalysisAPI.streambased.DataContainer.GetOriginalSignalName)
    - [M GetGlobalConstantNames ](#traceAnalysisAPI.streambased.DataContainer.GetGlobalConstantNames)
    - [M GetGlobalConstant ](#traceAnalysisAPI.streambased.DataContainer.GetGlobalConstant)
    - [M SetVariableValue ](#traceAnalysisAPI.streambased.DataContainer.SetVariableValue)
    - [M GetUnit ](#traceAnalysisAPI.streambased.DataContainer.GetUnit)
    - [M GetTextTable ](#traceAnalysisAPI.streambased.DataContainer.GetTextTable)
- [ Report ](#report)
  - [C traceAnalysisAPI.streambased.Report ](#traceAnalysisAPI.streambased.Report)
    - [M AddResultColumn ](#traceAnalysisAPI.streambased.Report.AddResultColumn)
    - [M GetLastTable ](#traceAnalysisAPI.streambased.Report.GetLastTable)
    - [M GetResultId ](#traceAnalysisAPI.streambased.Report.GetResultId)
    - [M GetTable ](#traceAnalysisAPI.streambased.Report.GetTable)
    - [M GetTableByIndex ](#traceAnalysisAPI.streambased.Report.GetTableByIndex)
    - [M GetTableCount ](#traceAnalysisAPI.streambased.Report.GetTableCount)
    - [M HasTable ](#traceAnalysisAPI.streambased.Report.HasTable)
    - [M Image ](#traceAnalysisAPI.streambased.Report.Image)
    - [M Log ](#traceAnalysisAPI.streambased.Report.Log)
    - [M LogDebug ](#traceAnalysisAPI.streambased.Report.LogDebug)
    - [M LogError ](#traceAnalysisAPI.streambased.Report.LogError)
    - [M LogInfo ](#traceAnalysisAPI.streambased.Report.LogInfo)
    - [M LogWarning ](#traceAnalysisAPI.streambased.Report.LogWarning)
    - [M Range ](#traceAnalysisAPI.streambased.Report.Range)
    - [M RemoveTable ](#traceAnalysisAPI.streambased.Report.RemoveTable)
    - [M SetLogComponent ](#traceAnalysisAPI.streambased.Report.SetLogComponent)
    - [M SetResultError ](#traceAnalysisAPI.streambased.Report.SetResultError)
    - [M SetResultFailed ](#traceAnalysisAPI.streambased.Report.SetResultFailed)
    - [M SetResultId ](#traceAnalysisAPI.streambased.Report.SetResultId)
    - [M SetResultInconclusive ](#traceAnalysisAPI.streambased.Report.SetResultInconclusive)
    - [M SetResultSuccess ](#traceAnalysisAPI.streambased.Report.SetResultSuccess)
    - [M SetResultText ](#traceAnalysisAPI.streambased.Report.SetResultText)
    - [M Spot ](#traceAnalysisAPI.streambased.Report.Spot)
    - [M Table ](#traceAnalysisAPI.streambased.Report.Table)
    - [M UpdateResultId ](#traceAnalysisAPI.streambased.Report.UpdateResultId)
- [ Parameters ](#parameters)
  - [A TraceStep.parameters ](#traceAnalysisAPI.streambased.TraceStep.parameters)
- [ RecordingInfo ](#recordinginfo)
  - [C traceAnalysisAPI.streambased.RecordingInfo ](#traceAnalysisAPI.streambased.RecordingInfo)
    - [M GetFirstPath ](#traceAnalysisAPI.streambased.RecordingInfo.GetFirstPath)
    - [M GetPath ](#traceAnalysisAPI.streambased.RecordingInfo.GetPath)
    - [M GetPathList ](#traceAnalysisAPI.streambased.RecordingInfo.GetPathList)
    - [M GetRecordingName ](#traceAnalysisAPI.streambased.RecordingInfo.GetRecordingName)
    - [M GetRecordingNumber ](#traceAnalysisAPI.streambased.RecordingInfo.GetRecordingNumber)
    - [M GetRecordingType ](#traceAnalysisAPI.streambased.RecordingInfo.GetRecordingType)
    - [M GetStartTimeNs ](#traceAnalysisAPI.streambased.RecordingInfo.GetStartTimeNs)
- [ ReportTable ](#reporttable)
  - [C traceAnalysisAPI.streambased.ReportTable ](#traceAnalysisAPI.streambased.ReportTable)
    - [M AddRow ](#traceAnalysisAPI.streambased.ReportTable.AddRow)
    - [M SetHeader ](#traceAnalysisAPI.streambased.ReportTable.SetHeader)
- [ Range ](#range)
  - [C traceAnalysisAPI.streambased.Range ](#traceAnalysisAPI.streambased.Range)
    - [M Range ](#traceAnalysisAPI.streambased.Range.Range)
    - [M Spot ](#traceAnalysisAPI.streambased.Range.Spot)

[ Custom GUI for parameters ](custom_param_gui.md)

[ Custom trace synchronization ](custom_trace_synchronization.md)

[ Available python libraries and APIs ](python_libraries.md)

Stream based tracestep templates

- [ DataContainer ](#datacontainer)
  - [C traceAnalysisAPI.streambased.DataContainer ](#traceAnalysisAPI.streambased.DataContainer)
    - [M GetTemplateSignalNames ](#traceAnalysisAPI.streambased.DataContainer.GetTemplateSignalNames)
    - [M GetGenericSignalName ](#traceAnalysisAPI.streambased.DataContainer.GetGenericSignalName)
    - [M GetMappingItemName ](#traceAnalysisAPI.streambased.DataContainer.GetMappingItemName)
    - [M GetOriginalSignalName ](#traceAnalysisAPI.streambased.DataContainer.GetOriginalSignalName)
    - [M GetGlobalConstantNames ](#traceAnalysisAPI.streambased.DataContainer.GetGlobalConstantNames)
    - [M GetGlobalConstant ](#traceAnalysisAPI.streambased.DataContainer.GetGlobalConstant)
    - [M SetVariableValue ](#traceAnalysisAPI.streambased.DataContainer.SetVariableValue)
    - [M GetUnit ](#traceAnalysisAPI.streambased.DataContainer.GetUnit)
    - [M GetTextTable ](#traceAnalysisAPI.streambased.DataContainer.GetTextTable)
- [ Report ](#report)
  - [C traceAnalysisAPI.streambased.Report ](#traceAnalysisAPI.streambased.Report)
    - [M AddResultColumn ](#traceAnalysisAPI.streambased.Report.AddResultColumn)
    - [M GetLastTable ](#traceAnalysisAPI.streambased.Report.GetLastTable)
    - [M GetResultId ](#traceAnalysisAPI.streambased.Report.GetResultId)
    - [M GetTable ](#traceAnalysisAPI.streambased.Report.GetTable)
    - [M GetTableByIndex ](#traceAnalysisAPI.streambased.Report.GetTableByIndex)
    - [M GetTableCount ](#traceAnalysisAPI.streambased.Report.GetTableCount)
    - [M HasTable ](#traceAnalysisAPI.streambased.Report.HasTable)
    - [M Image ](#traceAnalysisAPI.streambased.Report.Image)
    - [M Log ](#traceAnalysisAPI.streambased.Report.Log)
    - [M LogDebug ](#traceAnalysisAPI.streambased.Report.LogDebug)
    - [M LogError ](#traceAnalysisAPI.streambased.Report.LogError)
    - [M LogInfo ](#traceAnalysisAPI.streambased.Report.LogInfo)
    - [M LogWarning ](#traceAnalysisAPI.streambased.Report.LogWarning)
    - [M Range ](#traceAnalysisAPI.streambased.Report.Range)
    - [M RemoveTable ](#traceAnalysisAPI.streambased.Report.RemoveTable)
    - [M SetLogComponent ](#traceAnalysisAPI.streambased.Report.SetLogComponent)
    - [M SetResultError ](#traceAnalysisAPI.streambased.Report.SetResultError)
    - [M SetResultFailed ](#traceAnalysisAPI.streambased.Report.SetResultFailed)
    - [M SetResultId ](#traceAnalysisAPI.streambased.Report.SetResultId)
    - [M SetResultInconclusive ](#traceAnalysisAPI.streambased.Report.SetResultInconclusive)
    - [M SetResultSuccess ](#traceAnalysisAPI.streambased.Report.SetResultSuccess)
    - [M SetResultText ](#traceAnalysisAPI.streambased.Report.SetResultText)
    - [M Spot ](#traceAnalysisAPI.streambased.Report.Spot)
    - [M Table ](#traceAnalysisAPI.streambased.Report.Table)
    - [M UpdateResultId ](#traceAnalysisAPI.streambased.Report.UpdateResultId)
- [ Parameters ](#parameters)
  - [A TraceStep.parameters ](#traceAnalysisAPI.streambased.TraceStep.parameters)
- [ RecordingInfo ](#recordinginfo)
  - [C traceAnalysisAPI.streambased.RecordingInfo ](#traceAnalysisAPI.streambased.RecordingInfo)
    - [M GetFirstPath ](#traceAnalysisAPI.streambased.RecordingInfo.GetFirstPath)
    - [M GetPath ](#traceAnalysisAPI.streambased.RecordingInfo.GetPath)
    - [M GetPathList ](#traceAnalysisAPI.streambased.RecordingInfo.GetPathList)
    - [M GetRecordingName ](#traceAnalysisAPI.streambased.RecordingInfo.GetRecordingName)
    - [M GetRecordingNumber ](#traceAnalysisAPI.streambased.RecordingInfo.GetRecordingNumber)
    - [M GetRecordingType ](#traceAnalysisAPI.streambased.RecordingInfo.GetRecordingType)
    - [M GetStartTimeNs ](#traceAnalysisAPI.streambased.RecordingInfo.GetStartTimeNs)
- [ ReportTable ](#reporttable)
  - [C traceAnalysisAPI.streambased.ReportTable ](#traceAnalysisAPI.streambased.ReportTable)
    - [M AddRow ](#traceAnalysisAPI.streambased.ReportTable.AddRow)
    - [M SetHeader ](#traceAnalysisAPI.streambased.ReportTable.SetHeader)
- [ Range ](#range)
  - [C traceAnalysisAPI.streambased.Range ](#traceAnalysisAPI.streambased.Range)
    - [M Range ](#traceAnalysisAPI.streambased.Range.Range)
    - [M Spot ](#traceAnalysisAPI.streambased.Range.Spot)

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

GetGenericSignalName(*[templateSignalName](#traceAnalysisAPI.streambased.DataContainer.GetGenericSignalName.templateSignalName "traceAnalysisAPI.streambased.DataContainer.GetGenericSignalName.templateSignalName (Python parameter) — name of the template signal")*)[¶](#traceAnalysisAPI.streambased.DataContainer.GetGenericSignalName "Link to this definition")  
Returns the name of the assigned generic signal for a given signal name of the trace step template.

Parameters:  templateSignalName : string[¶](#traceAnalysisAPI.streambased.DataContainer.GetGenericSignalName.templateSignalName "Permalink to this definition")  
name of the template signal

Returns:  name of the generic signal

Return type:  string

GetMappingItemName(*[templateSignalName](#traceAnalysisAPI.streambased.DataContainer.GetMappingItemName.templateSignalName "traceAnalysisAPI.streambased.DataContainer.GetMappingItemName.templateSignalName (Python parameter) — name of the template signal")*)[¶](#traceAnalysisAPI.streambased.DataContainer.GetMappingItemName "Link to this definition")  
Returns the name (of the reference (= source)) of the mapping item which corresponds to the assigned generic signal for a given signal name of the trace step template.

Parameters:  templateSignalName : string[¶](#traceAnalysisAPI.streambased.DataContainer.GetMappingItemName.templateSignalName "Permalink to this definition")  
name of the template signal

Returns:  name (of the reference (= source)) of the mapping item

Return type:  string

GetOriginalSignalName(*[templateSignalName](#traceAnalysisAPI.streambased.DataContainer.GetOriginalSignalName.templateSignalName "traceAnalysisAPI.streambased.DataContainer.GetOriginalSignalName.templateSignalName (Python parameter) — name of the template signal")*)[¶](#traceAnalysisAPI.streambased.DataContainer.GetOriginalSignalName "Link to this definition")  
Returns the original signal name of the assigned generic signal for a given signal name of the trace step template.

Parameters:  templateSignalName : string[¶](#traceAnalysisAPI.streambased.DataContainer.GetOriginalSignalName.templateSignalName "Permalink to this definition")  
name of the template signal

Returns:  name of the original signal

Return type:  string

GetGlobalConstantNames()[¶](#traceAnalysisAPI.streambased.DataContainer.GetGlobalConstantNames "Link to this definition")  
Returns a list of names containing all global constants.

Returns:  A list of names.

Return type:  list

GetGlobalConstant(*[name](#traceAnalysisAPI.streambased.DataContainer.GetGlobalConstant.name "traceAnalysisAPI.streambased.DataContainer.GetGlobalConstant.name (Python parameter) — The name of the constant to retrieve the value.")*)[¶](#traceAnalysisAPI.streambased.DataContainer.GetGlobalConstant "Link to this definition")  
Returns the value of the given global constant.

Parameters:  name : string[¶](#traceAnalysisAPI.streambased.DataContainer.GetGlobalConstant.name "Permalink to this definition")  
The name of the constant to retrieve the value.

Returns:  The value of the constant.

Return type:  object

SetVariableValue(*[name](#traceAnalysisAPI.streambased.DataContainer.SetVariableValue.name "traceAnalysisAPI.streambased.DataContainer.SetVariableValue.name (Python parameter) — name of the package variable that shall be set")*, *[value](#traceAnalysisAPI.streambased.DataContainer.SetVariableValue.value "traceAnalysisAPI.streambased.DataContainer.SetVariableValue.value (Python parameter) — value to be set")*)[¶](#traceAnalysisAPI.streambased.DataContainer.SetVariableValue "Link to this definition")  
Info

Please consider using parameters and return values in your trace step template instead of using this method. This method should only be used for special use cases where an uncertain amount of variables shall be initialized.

Sets the value of the package variable with the given name.

If no variable with the given name exists in the trace analysis namespace, an error is raised. The new value of the variable cannot be accessed from within the same episode.

Parameters:  name : string[¶](#traceAnalysisAPI.streambased.DataContainer.SetVariableValue.name "Permalink to this definition")  
name of the package variable that shall be set

value : Python object[¶](#traceAnalysisAPI.streambased.DataContainer.SetVariableValue.value "Permalink to this definition")  
value to be set

GetUnit(*[templateSignalName](#traceAnalysisAPI.streambased.DataContainer.GetUnit.templateSignalName "traceAnalysisAPI.streambased.DataContainer.GetUnit.templateSignalName (Python parameter) — name of the template signal"): str*)[¶](#traceAnalysisAPI.streambased.DataContainer.GetUnit "Link to this definition")  
Returns the unit of the signal with the given name.

Parameters:  templateSignalName : string[¶](#traceAnalysisAPI.streambased.DataContainer.GetUnit.templateSignalName "Permalink to this definition")  
name of the template signal

Returns:  The unit of the given signal.

Return type:  str

GetTextTable(*[templateSignalName](#traceAnalysisAPI.streambased.DataContainer.GetTextTable.templateSignalName "traceAnalysisAPI.streambased.DataContainer.GetTextTable.templateSignalName (Python parameter) — name of the template signal"): str*)[¶](#traceAnalysisAPI.streambased.DataContainer.GetTextTable "Link to this definition")  
Returns the text table and the default value of the signal with the given name as tuple.

Parameters:  templateSignalName : string[¶](#traceAnalysisAPI.streambased.DataContainer.GetTextTable.templateSignalName "Permalink to this definition")  
name of the template signal

Returns:  The text table and the default text table as tuple.

Return type:  tuple

## Report[¶](#report "Link to this heading")

*class* traceAnalysisAPI.streambased.Report[¶](#traceAnalysisAPI.streambased.Report "Link to this definition")  
AddResultColumn(*[name](#traceAnalysisAPI.streambased.Report.AddResultColumn.name "traceAnalysisAPI.streambased.Report.AddResultColumn.name (Python parameter) — name of the new column"): str*) → None[¶](#traceAnalysisAPI.streambased.Report.AddResultColumn "Link to this definition")  
Adds a new column with the given name to the result table. It is appended at the end of the table. Values can be inserted into this column by using the parameter “additionalInfo” of the methods [`Spot()`](#traceAnalysisAPI.streambased.Report.Spot "traceAnalysisAPI.streambased.Report.Spot (Python method) — Adds a signal spot to the test report.") and [`Range()`](#traceAnalysisAPI.streambased.Report.Range "traceAnalysisAPI.streambased.Report.Range (Python method) — Adds a range to the test report and returns a range object."). The entries in the list “additionalInfo” list are inserted into the additional result columns in sequence.

Parameters:  name : str[¶](#traceAnalysisAPI.streambased.Report.AddResultColumn.name "Permalink to this definition")  
name of the new column

GetLastTable() → ReportTable[¶](#traceAnalysisAPI.streambased.Report.GetLastTable "Link to this definition")  
Returns the last table created.

Return type:  [`ReportTable`](#traceAnalysisAPI.streambased.ReportTable "traceAnalysisAPI.streambased.ReportTable (Python class) — A ReportTable object represents a table in the test report.")

GetResultId() → int | None[¶](#traceAnalysisAPI.streambased.Report.GetResultId "Link to this definition")  
Gets the current result id.

The result id passed to an earlier call to [`SetResultId()`](#traceAnalysisAPI.streambased.Report.SetResultId "traceAnalysisAPI.streambased.Report.SetResultId (Python method) — Sets the result id for the current trace step.") is returned. If [`SetResultId()`](#traceAnalysisAPI.streambased.Report.SetResultId "traceAnalysisAPI.streambased.Report.SetResultId (Python method) — Sets the result id for the current trace step.") wasn’t called before, `dataContainer.RESULT_ID_NONE` is returned.

Returns:  the result id

Return type:  int

GetTable(*[tableId](#traceAnalysisAPI.streambased.Report.GetTable.tableId "traceAnalysisAPI.streambased.Report.GetTable.tableId (Python parameter) — id of the table"): str*) → ReportTable[¶](#traceAnalysisAPI.streambased.Report.GetTable "Link to this definition")  
Returns the table with the given id.

Parameters:  tableId : str[¶](#traceAnalysisAPI.streambased.Report.GetTable.tableId "Permalink to this definition")  
id of the table

Return type:  [`ReportTable`](#traceAnalysisAPI.streambased.ReportTable "traceAnalysisAPI.streambased.ReportTable (Python class) — A ReportTable object represents a table in the test report.")

GetTableByIndex(*[index](#traceAnalysisAPI.streambased.Report.GetTableByIndex.index "traceAnalysisAPI.streambased.Report.GetTableByIndex.index (Python parameter) — the position of the table"): int*) → ReportTable[¶](#traceAnalysisAPI.streambased.Report.GetTableByIndex "Link to this definition")  
Returns the table by the given position in the list of user-defined tables.

Parameters:  index : int[¶](#traceAnalysisAPI.streambased.Report.GetTableByIndex.index "Permalink to this definition")  
the position of the table

Return type:  [`ReportTable`](#traceAnalysisAPI.streambased.ReportTable "traceAnalysisAPI.streambased.ReportTable (Python class) — A ReportTable object represents a table in the test report.")

GetTableCount() → int[¶](#traceAnalysisAPI.streambased.Report.GetTableCount "Link to this definition")  
Returns the count of tables.

Returns:  The count of tables.

Return type:  int

HasTable(*[tableId](#traceAnalysisAPI.streambased.Report.HasTable.tableId "traceAnalysisAPI.streambased.Report.HasTable.tableId (Python parameter) — id of the table"): str*) → bool[¶](#traceAnalysisAPI.streambased.Report.HasTable "Link to this definition")  
Returns whether a particular table exists for the trace step.

Parameters:  tableId : str[¶](#traceAnalysisAPI.streambased.Report.HasTable.tableId "Permalink to this definition")  
id of the table

Returns:  True if a table with the given id exists, else False

Return type:  bool

Image(*[imageSource](#traceAnalysisAPI.streambased.Report.Image.imageSource "traceAnalysisAPI.streambased.Report.Image.imageSource (Python parameter) — The image source can be one of the following:"): str | Path | ImageInterface | ndarray | bytes*, *\**, *[name](#traceAnalysisAPI.streambased.Report.Image.name "traceAnalysisAPI.streambased.Report.Image.name (Python parameter) — The filename (with correct extension)."): str | None = `None`*, *[title](#traceAnalysisAPI.streambased.Report.Image.title "traceAnalysisAPI.streambased.Report.Image.title (Python parameter) — the image title"): str | None = `None`*, *[embedded](#traceAnalysisAPI.streambased.Report.Image.embedded "traceAnalysisAPI.streambased.Report.Image.embedded (Python parameter) — True, if the image file should be embedded in the test report, else the image file is stored in the test report folder."): bool = `False`*, *[limitPreviewSize](#traceAnalysisAPI.streambased.Report.Image.limitPreviewSize "traceAnalysisAPI.streambased.Report.Image.limitPreviewSize (Python parameter) — If True (default), the preview image shown in the report will be limited to a maximum size."): bool = `True`*, *[autoDelete](#traceAnalysisAPI.streambased.Report.Image.autoDelete "traceAnalysisAPI.streambased.Report.Image.autoDelete (Python parameter) — Only applicable if imageSource is a file path."): bool = `False`*, *[useTemp](#traceAnalysisAPI.streambased.Report.Image.useTemp "traceAnalysisAPI.streambased.Report.Image.useTemp (Python parameter) — Only applicable if imageSource is a file path."): bool = `True`*) → ReportImage[¶](#traceAnalysisAPI.streambased.Report.Image "Link to this definition")  
Adds the given image to the test report. If the image is not embedded in the test report, the file will be stored in the report folder. If there is already an image with the same name, the image files will be enumerated.

Parameters:  imageSource : str|Path|Image|Frame|numpy.ndarray|bytes[¶](#traceAnalysisAPI.streambased.Report.Image.imageSource "Permalink to this definition")  
The image source can be one of the following:

- an absolute file path

- an Image or Frame object

- a NumPy array in OpenCV style: shape is (height, width, 3) of type numpy.uint8, the three colors have the order BGR!

- bytes object with image data

name : str[¶](#traceAnalysisAPI.streambased.Report.Image.name "Permalink to this definition")  
The filename (with correct extension). Will be used as filename if an image file is created in the report folder. If name is None and the source is a path or an Image or Frame, the name of the imageSource is used.

title : str[¶](#traceAnalysisAPI.streambased.Report.Image.title "Permalink to this definition")  
the image title

embedded : bool[¶](#traceAnalysisAPI.streambased.Report.Image.embedded "Permalink to this definition")  
True, if the image file should be embedded in the test report, else the image file is stored in the test report folder.

limitPreviewSize : bool[¶](#traceAnalysisAPI.streambased.Report.Image.limitPreviewSize "Permalink to this definition")  
If True (default), the preview image shown in the report will be limited to a maximum size.

autoDelete : bool[¶](#traceAnalysisAPI.streambased.Report.Image.autoDelete "Permalink to this definition")  
Only applicable if imageSource is a file path. True, if the image file should be automatically deleted, else False.

useTemp : bool[¶](#traceAnalysisAPI.streambased.Report.Image.useTemp "Permalink to this definition")  
Only applicable if imageSource is a file path. True, if the image file should be copied into a temporary directory, False, if it should be used directly. Using a temporary copy might be necessary to avoid overriding the image before the final report gets assembled later on.

Log(*[level](#traceAnalysisAPI.streambased.Report.Log.level "traceAnalysisAPI.streambased.Report.Log.level (Python parameter) — log level")*, *[time](#traceAnalysisAPI.streambased.Report.Log.time "traceAnalysisAPI.streambased.Report.Log.time (Python parameter) — timestamp of the log message")*, *[message](#traceAnalysisAPI.streambased.Report.Log.message "traceAnalysisAPI.streambased.Report.Log.message (Python parameter) — log message or format string.")*, *\*[formatArgs](#traceAnalysisAPI.streambased.Report.Log.formatArgs "traceAnalysisAPI.streambased.Report.Log.formatArgs (Python parameter) — additional non-keyword arguments used when message is a format string")*, *\*\*[formatKwargs](#traceAnalysisAPI.streambased.Report.Log.formatKwargs "traceAnalysisAPI.streambased.Report.Log.formatKwargs (Python parameter) — additional keyword arguments used when message is a format string")*)[¶](#traceAnalysisAPI.streambased.Report.Log "Link to this definition")  
Adds a log message to the trace analysis log file. Use [`SetLogComponent()`](#traceAnalysisAPI.streambased.Report.SetLogComponent "traceAnalysisAPI.streambased.Report.SetLogComponent (Python method) — Sets the component that will be used in logging entries created by calling log methods.") to set the component part of the log entry.

Parameters:  level : int[¶](#traceAnalysisAPI.streambased.Report.Log.level "Permalink to this definition")  
log level

- report.LOG_LEVEL_DEBUG

- report.LOG_LEVEL_INFO

- report.LOG_LEVEL_WARNING

- report.LOG_LEVEL_ERROR

time : float[¶](#traceAnalysisAPI.streambased.Report.Log.time "Permalink to this definition")  
timestamp of the log message

message : str[¶](#traceAnalysisAPI.streambased.Report.Log.message "Permalink to this definition")  
log message or format string.

\*formatArgs[¶](#traceAnalysisAPI.streambased.Report.Log.formatArgs "Permalink to this definition")  
additional non-keyword arguments used when message is a format string

\*\*formatKwargs[¶](#traceAnalysisAPI.streambased.Report.Log.formatKwargs "Permalink to this definition")  
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

LogDebug(*[time](#traceAnalysisAPI.streambased.Report.LogDebug "traceAnalysisAPI.streambased.Report.LogDebug.time (Python parameter)")*, *[message](#traceAnalysisAPI.streambased.Report.LogDebug "traceAnalysisAPI.streambased.Report.LogDebug.message (Python parameter)")*, *\*[formatArgs](#traceAnalysisAPI.streambased.Report.LogDebug "traceAnalysisAPI.streambased.Report.LogDebug.formatArgs (Python parameter)")*, *\*\*[formatKwargs](#traceAnalysisAPI.streambased.Report.LogDebug "traceAnalysisAPI.streambased.Report.LogDebug.formatKwargs (Python parameter)")*)[¶](#traceAnalysisAPI.streambased.Report.LogDebug "Link to this definition")  
Convenience method to add a debug log message. See [`Log()`](#traceAnalysisAPI.streambased.Report.Log "traceAnalysisAPI.streambased.Report.Log (Python method) — Adds a log message to the trace analysis log file. Use SetLogComponent() to set the component part of the log entry.") for further usage.

LogError(*[time](#traceAnalysisAPI.streambased.Report.LogError "traceAnalysisAPI.streambased.Report.LogError.time (Python parameter)")*, *[message](#traceAnalysisAPI.streambased.Report.LogError "traceAnalysisAPI.streambased.Report.LogError.message (Python parameter)")*, *\*[formatArgs](#traceAnalysisAPI.streambased.Report.LogError "traceAnalysisAPI.streambased.Report.LogError.formatArgs (Python parameter)")*, *\*\*[formatKwargs](#traceAnalysisAPI.streambased.Report.LogError "traceAnalysisAPI.streambased.Report.LogError.formatKwargs (Python parameter)")*)[¶](#traceAnalysisAPI.streambased.Report.LogError "Link to this definition")  
Convenience method to add an error log message. See [`Log()`](#traceAnalysisAPI.streambased.Report.Log "traceAnalysisAPI.streambased.Report.Log (Python method) — Adds a log message to the trace analysis log file. Use SetLogComponent() to set the component part of the log entry.") for further usage.

LogInfo(*[time](#traceAnalysisAPI.streambased.Report.LogInfo "traceAnalysisAPI.streambased.Report.LogInfo.time (Python parameter)")*, *[message](#traceAnalysisAPI.streambased.Report.LogInfo "traceAnalysisAPI.streambased.Report.LogInfo.message (Python parameter)")*, *\*[formatArgs](#traceAnalysisAPI.streambased.Report.LogInfo "traceAnalysisAPI.streambased.Report.LogInfo.formatArgs (Python parameter)")*, *\*\*[formatKwargs](#traceAnalysisAPI.streambased.Report.LogInfo "traceAnalysisAPI.streambased.Report.LogInfo.formatKwargs (Python parameter)")*)[¶](#traceAnalysisAPI.streambased.Report.LogInfo "Link to this definition")  
Convenience method to add an info log message. See [`Log()`](#traceAnalysisAPI.streambased.Report.Log "traceAnalysisAPI.streambased.Report.Log (Python method) — Adds a log message to the trace analysis log file. Use SetLogComponent() to set the component part of the log entry.") for further usage.

LogWarning(*[time](#traceAnalysisAPI.streambased.Report.LogWarning "traceAnalysisAPI.streambased.Report.LogWarning.time (Python parameter)")*, *[message](#traceAnalysisAPI.streambased.Report.LogWarning "traceAnalysisAPI.streambased.Report.LogWarning.message (Python parameter)")*, *\*[formatArgs](#traceAnalysisAPI.streambased.Report.LogWarning "traceAnalysisAPI.streambased.Report.LogWarning.formatArgs (Python parameter)")*, *\*\*[formatKwargs](#traceAnalysisAPI.streambased.Report.LogWarning "traceAnalysisAPI.streambased.Report.LogWarning.formatKwargs (Python parameter)")*)[¶](#traceAnalysisAPI.streambased.Report.LogWarning "Link to this definition")  
Convenience method to add a warning log message. See [`Log()`](#traceAnalysisAPI.streambased.Report.Log "traceAnalysisAPI.streambased.Report.Log (Python method) — Adds a log message to the trace analysis log file. Use SetLogComponent() to set the component part of the log entry.") for further usage.

Range(*[startTime](#traceAnalysisAPI.streambased.Report.Range.startTime "traceAnalysisAPI.streambased.Report.Range.startTime (Python parameter) — timestamp at which the range begins"): float | numpy.integer | numpy.floating*, *[endTime](#traceAnalysisAPI.streambased.Report.Range.endTime "traceAnalysisAPI.streambased.Report.Range.endTime (Python parameter) — timestamp at which the range ends"): float | numpy.integer | numpy.floating*, *[message](#traceAnalysisAPI.streambased.Report.Range.message "traceAnalysisAPI.streambased.Report.Range.message (Python parameter) — a textual message describing the range"): str = `''`*, *[resultId](#traceAnalysisAPI.streambased.Report.Range.resultId "traceAnalysisAPI.streambased.Report.Range.resultId (Python parameter) — the verdict for the range"): int | None = `None`*, *[additionalInfo](#traceAnalysisAPI.streambased.Report.Range.additionalInfo "traceAnalysisAPI.streambased.Report.Range.additionalInfo (Python parameter) — a list of additional information, that will be shown in the custom result columns (see AddResultColumn())"): list[str] | None = `None`*) → RangeEntity[¶](#traceAnalysisAPI.streambased.Report.Range "Link to this definition")  
Adds a range to the test report and returns a range object.

Parameters:  startTime : float[¶](#traceAnalysisAPI.streambased.Report.Range.startTime "Permalink to this definition")  
timestamp at which the range begins

endTime : float[¶](#traceAnalysisAPI.streambased.Report.Range.endTime "Permalink to this definition")  
timestamp at which the range ends

message : str[¶](#traceAnalysisAPI.streambased.Report.Range.message "Permalink to this definition")  
a textual message describing the range

resultId : int[¶](#traceAnalysisAPI.streambased.Report.Range.resultId "Permalink to this definition")  
the verdict for the range

additionalInfo : list of strings[¶](#traceAnalysisAPI.streambased.Report.Range.additionalInfo "Permalink to this definition")  
a list of additional information, that will be shown in the custom result columns (see [`AddResultColumn()`](#traceAnalysisAPI.streambased.Report.AddResultColumn "traceAnalysisAPI.streambased.Report.AddResultColumn (Python method) — Adds a new column with the given name to the result table. It is appended at the end of the table. Values can be inserted into this column by using the parameter "additionalInfo" of the methods Spot() and Range(). The entries in the list "additionalInfo" list are inserted into the additional result columns in sequence."))

Return type:  [`Range`](#traceAnalysisAPI.streambased.Range "traceAnalysisAPI.streambased.Range (Python class) — Class representing a range in the test report. An instance of Range is returned by the call of Report.Range(). To specify the range in more detail, it is possible to add spots and sub ranges as children to a range object.")

RemoveTable(*[tableId](#traceAnalysisAPI.streambased.Report.RemoveTable.tableId "traceAnalysisAPI.streambased.Report.RemoveTable.tableId (Python parameter) — id of the table"): str*) → None[¶](#traceAnalysisAPI.streambased.Report.RemoveTable "Link to this definition")  
Removes a table from the test report.

Parameters:  tableId : str[¶](#traceAnalysisAPI.streambased.Report.RemoveTable.tableId "Permalink to this definition")  
id of the table

SetLogComponent(*[component](#traceAnalysisAPI.streambased.Report.SetLogComponent.component "traceAnalysisAPI.streambased.Report.SetLogComponent.component (Python parameter) — name of the component")*)[¶](#traceAnalysisAPI.streambased.Report.SetLogComponent "Link to this definition")  
Sets the component that will be used in logging entries created by calling log methods.

Parameters:  component : str[¶](#traceAnalysisAPI.streambased.Report.SetLogComponent.component "Permalink to this definition")  
name of the component

SetResultError()[¶](#traceAnalysisAPI.streambased.Report.SetResultError "Link to this definition")  
Convenience method for report.SetResultId(report.RESULT_ID_ERROR)

SetResultFailed()[¶](#traceAnalysisAPI.streambased.Report.SetResultFailed "Link to this definition")  
Convenience method for report.SetResultId(report.RESULT_ID_FAILED)

SetResultId(*[resultId](#traceAnalysisAPI.streambased.Report.SetResultId.resultId "traceAnalysisAPI.streambased.Report.SetResultId.resultId (Python parameter) — the result id to set")*)[¶](#traceAnalysisAPI.streambased.Report.SetResultId "Link to this definition")  
Sets the result id for the current trace step.

The result id can be one of:

- report.RESULT_ID_NONE

- report.RESULT_ID_SUCCESS

- report.RESULT_ID_INCONCLUSIVE

- report.RESULT_ID_FAILED

- report.RESULT_ID_ERROR

The result id is set directly. It is not affected by earlier calls to [`SetResultId()`](#traceAnalysisAPI.streambased.Report.SetResultId "traceAnalysisAPI.streambased.Report.SetResultId (Python method) — Sets the result id for the current trace step.").

Example:

    report.SetResultId(report.RESULT_ID_ERROR)
    report.SetResultId(report.RESULT_ID_NONE)

    report.GetResultId() # this will result in report.RESULT_ID_NONE

Parameters:  resultId : result id[¶](#traceAnalysisAPI.streambased.Report.SetResultId.resultId "Permalink to this definition")  
the result id to set

SetResultInconclusive()[¶](#traceAnalysisAPI.streambased.Report.SetResultInconclusive "Link to this definition")  
Convenience method for report.SetResultId(report.RESULT_ID_INCONCLUSIVE)

SetResultSuccess()[¶](#traceAnalysisAPI.streambased.Report.SetResultSuccess "Link to this definition")  
Convenience method for report.SetResultId(report.RESULT_ID_SUCCESS)

SetResultText(*[text](#traceAnalysisAPI.streambased.Report.SetResultText.text "traceAnalysisAPI.streambased.Report.SetResultText.text (Python parameter) — the text"): str | None*) → None[¶](#traceAnalysisAPI.streambased.Report.SetResultText "Link to this definition")  
Sets a user-defined text for the result of the report.

Parameters:  text : str[¶](#traceAnalysisAPI.streambased.Report.SetResultText.text "Permalink to this definition")  
the text

Spot(*[time](#traceAnalysisAPI.streambased.Report.Spot.time "traceAnalysisAPI.streambased.Report.Spot.time (Python parameter) — timestamp of the spot")*, *[message](#traceAnalysisAPI.streambased.Report.Spot.message "traceAnalysisAPI.streambased.Report.Spot.message (Python parameter) — a textual message describing the spot")=`''`*, *[resultId](#traceAnalysisAPI.streambased.Report.Spot.resultId "traceAnalysisAPI.streambased.Report.Spot.resultId (Python parameter) — the verdict for the spot")=`None`*, *[additionalInfo](#traceAnalysisAPI.streambased.Report.Spot.additionalInfo "traceAnalysisAPI.streambased.Report.Spot.additionalInfo (Python parameter) — a list of additional information, that will be shown in the custom result columns (see AddResultColumn())")=`None`*)[¶](#traceAnalysisAPI.streambased.Report.Spot "Link to this definition")  
Adds a signal spot to the test report.

Parameters:  time : float[¶](#traceAnalysisAPI.streambased.Report.Spot.time "Permalink to this definition")  
timestamp of the spot

message : an object, that can be converted to via str(message)[¶](#traceAnalysisAPI.streambased.Report.Spot.message "Permalink to this definition")  
a textual message describing the spot

resultId : result id[¶](#traceAnalysisAPI.streambased.Report.Spot.resultId "Permalink to this definition")  
the verdict for the spot

additionalInfo : list of strings[¶](#traceAnalysisAPI.streambased.Report.Spot.additionalInfo "Permalink to this definition")  
a list of additional information, that will be shown in the custom result columns (see [`AddResultColumn()`](#traceAnalysisAPI.streambased.Report.AddResultColumn "traceAnalysisAPI.streambased.Report.AddResultColumn (Python method) — Adds a new column with the given name to the result table. It is appended at the end of the table. Values can be inserted into this column by using the parameter "additionalInfo" of the methods Spot() and Range(). The entries in the list "additionalInfo" list are inserted into the additional result columns in sequence."))

Table(*[tableId](#traceAnalysisAPI.streambased.Report.Table.tableId "traceAnalysisAPI.streambased.Report.Table.tableId (Python parameter) — id to identify the table"): str | int | None = `None`*, *[headerValues](#traceAnalysisAPI.streambased.Report.Table.headerValues "traceAnalysisAPI.streambased.Report.Table.headerValues (Python parameter) — iterable with the entries of the table header"): Iterable[str | int] | None = `None`*) → ReportTable[¶](#traceAnalysisAPI.streambased.Report.Table "Link to this definition")  
Creates a table in the test report.

Example:

    table = report.Table("table1", ["time", "description"])
    table.AddRow(["1.3", "A rising edge detected"])
    table.AddRow(["3.8", "A falling edge detected"])

Parameters:  tableId : str[¶](#traceAnalysisAPI.streambased.Report.Table.tableId "Permalink to this definition")  
id to identify the table

headerValues : iterable[¶](#traceAnalysisAPI.streambased.Report.Table.headerValues "Permalink to this definition")  
iterable with the entries of the table header

Returns:  the report table object

Return type:  [`ReportTable`](#traceAnalysisAPI.streambased.ReportTable "traceAnalysisAPI.streambased.ReportTable (Python class) — A ReportTable object represents a table in the test report.")

UpdateResultId(*[resultId](#traceAnalysisAPI.streambased.Report.UpdateResultId.resultId "traceAnalysisAPI.streambased.Report.UpdateResultId.resultId (Python parameter) — the result id to set")*)[¶](#traceAnalysisAPI.streambased.Report.UpdateResultId "Link to this definition")  
Updates the result id for the current trace step.

The result id can be one of:

- report.RESULT_ID_NONE

- report.RESULT_ID_SUCCESS

- report.RESULT_ID_INCONCLUSIVE

- report.RESULT_ID_FAILED

- report.RESULT_ID_ERROR

In contrast to [`SetResultId()`](#traceAnalysisAPI.streambased.Report.SetResultId "traceAnalysisAPI.streambased.Report.SetResultId (Python method) — Sets the result id for the current trace step."), which sets the resultId directly, [`UpdateResultId()`](#traceAnalysisAPI.streambased.Report.UpdateResultId "traceAnalysisAPI.streambased.Report.UpdateResultId (Python method) — Updates the result id for the current trace step.") can only increase the resultId according to the following ordering:

RESULT_ID_NONE \< RESULT_ID_SUCCESS \< RESULT_ID_INCONCLUSIVE \< RESULT_ID_FAILED \< RESULT_ID_ERROR

Info

[`UpdateResultId()`](#traceAnalysisAPI.streambased.Report.UpdateResultId "traceAnalysisAPI.streambased.Report.UpdateResultId (Python method) — Updates the result id for the current trace step.") can bee seen as equivalent to SetResultId(max(resultId, GetResultId()))

..example:

    report.UpdateResultId(report.RESULT_ID_SUCCESS)
    ...
    report.UpdateResultId(report.RESULT_ID_FAILED)
    ...
    report.UpdateResultId(report.RESULT_ID_SUCCESS)

    report.GetResultId() # this will result in report.RESULT_ID_FAILED

Parameters:  resultId : result id[¶](#traceAnalysisAPI.streambased.Report.UpdateResultId.resultId "Permalink to this definition")  
the result id to set

## Parameters[¶](#parameters "Link to this heading")

TraceStep.parameters = `{}`[¶](#traceAnalysisAPI.streambased.TraceStep.parameters "Link to this definition")  
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

GetPath(*[idx](#traceAnalysisAPI.streambased.RecordingInfo.GetPath "traceAnalysisAPI.streambased.RecordingInfo.GetPath.idx (Python parameter)")=`0`*) → str | None[¶](#traceAnalysisAPI.streambased.RecordingInfo.GetPath "Link to this definition")  
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

GetStartTimeNs(*\**, *[synchronized](#traceAnalysisAPI.streambased.RecordingInfo.GetStartTimeNs.synchronized "traceAnalysisAPI.streambased.RecordingInfo.GetStartTimeNs.synchronized (Python parameter) — If True, the start time is adjusted by the deltaT if available."): bool = `True`*) → int | None[¶](#traceAnalysisAPI.streambased.RecordingInfo.GetStartTimeNs "Link to this definition")  
Returns the start time of the recording in nanoseconds since 1970-01-01T00:00:00Z.

This information is useful to calculate absolute timestamps, e.g.:

absoluteTimestampsInNs = int(relativeTimestampsInSeconds \* 1e9) + startTimeNs

If the traces have not been synchronized, the value of the parameter synchronized does not matter. If the traces have been sychronized, this method should normally be called with synchronized=True (default) so that the start time is adjusted to the deltaT and the adjusted start time can just be added to the synchronized timestamps to get the absolute timestamps. However, if you want to get the real start time without any adjustments, you should call this method with synchronized=False.

Parameters:  synchronized: bool = `True`[¶](#traceAnalysisAPI.streambased.RecordingInfo.GetStartTimeNs.synchronized "Permalink to this definition")  
If True, the start time is adjusted by the deltaT if available.

Returns:  start time in nanoseconds or None if the recording format does not support it

Raises:  
**ValueError** – if the start time cannot be determined (e.g., empty file or missing metadata)

## ReportTable[¶](#reporttable "Link to this heading")

*class* traceAnalysisAPI.streambased.ReportTable[¶](#traceAnalysisAPI.streambased.ReportTable "Link to this definition")  
A ReportTable object represents a table in the test report.

AddRow(*[values](#traceAnalysisAPI.streambased.ReportTable.AddRow.values "traceAnalysisAPI.streambased.ReportTable.AddRow.values (Python parameter) — iterable with the entries for each column of the new row"): Iterable[str]*, *[resultId](#traceAnalysisAPI.streambased.ReportTable.AddRow.resultId "traceAnalysisAPI.streambased.ReportTable.AddRow.resultId (Python parameter) — the result id of the row"): int | None = `None`*) → None[¶](#traceAnalysisAPI.streambased.ReportTable.AddRow "Link to this definition")  
Appends a row to the table.

Parameters:  values : iterable[¶](#traceAnalysisAPI.streambased.ReportTable.AddRow.values "Permalink to this definition")  
iterable with the entries for each column of the new row

resultId : result id or None[¶](#traceAnalysisAPI.streambased.ReportTable.AddRow.resultId "Permalink to this definition")  
the result id of the row

SetHeader(*[values](#traceAnalysisAPI.streambased.ReportTable.SetHeader.values "traceAnalysisAPI.streambased.ReportTable.SetHeader.values (Python parameter) — iterable with the entries for each column of the table header"): Iterable[str | int] | None*) → None[¶](#traceAnalysisAPI.streambased.ReportTable.SetHeader "Link to this definition")  
Sets the table header.

Parameters:  values : iterable[¶](#traceAnalysisAPI.streambased.ReportTable.SetHeader.values "Permalink to this definition")  
iterable with the entries for each column of the table header

## Range[¶](#range "Link to this heading")

*class* traceAnalysisAPI.streambased.Range[¶](#traceAnalysisAPI.streambased.Range "Link to this definition")  
Class representing a range in the test report. An instance of Range is returned by the call of [`Report.Range()`](#traceAnalysisAPI.streambased.Report.Range "traceAnalysisAPI.streambased.Report.Range (Python method) — Adds a range to the test report and returns a range object."). To specify the range in more detail, it is possible to add spots and sub ranges as children to a range object.

Range(*[startTime](#traceAnalysisAPI.streambased.Range.Range.startTime "traceAnalysisAPI.streambased.Range.Range.startTime (Python parameter) — timestamp at which the sub range begins")*, *[endTime](#traceAnalysisAPI.streambased.Range.Range.endTime "traceAnalysisAPI.streambased.Range.Range.endTime (Python parameter) — timestamp at which the sub range ends")*, *[message](#traceAnalysisAPI.streambased.Range.Range.message "traceAnalysisAPI.streambased.Range.Range.message (Python parameter) — a textual message describing the sub range")=`''`*, *[resultId](#traceAnalysisAPI.streambased.Range.Range.resultId "traceAnalysisAPI.streambased.Range.Range.resultId (Python parameter) — the verdict for the sub range")=`None`*, *[additionalInfo](#traceAnalysisAPI.streambased.Range.Range.additionalInfo "traceAnalysisAPI.streambased.Range.Range.additionalInfo (Python parameter) — a list of additional information, that will be shown in the custom result columns (see Report.AddResultColumn())")=`None`*)[¶](#traceAnalysisAPI.streambased.Range.Range "Link to this definition")  
Adds a sub range to the range.

Parameters:  startTime : float[¶](#traceAnalysisAPI.streambased.Range.Range.startTime "Permalink to this definition")  
timestamp at which the sub range begins

endTime : float[¶](#traceAnalysisAPI.streambased.Range.Range.endTime "Permalink to this definition")  
timestamp at which the sub range ends

message : string[¶](#traceAnalysisAPI.streambased.Range.Range.message "Permalink to this definition")  
a textual message describing the sub range

resultId : int[¶](#traceAnalysisAPI.streambased.Range.Range.resultId "Permalink to this definition")  
the verdict for the sub range

additionalInfo : list of strings[¶](#traceAnalysisAPI.streambased.Range.Range.additionalInfo "Permalink to this definition")  
a list of additional information, that will be shown in the custom result columns (see [`Report.AddResultColumn()`](#traceAnalysisAPI.streambased.Report.AddResultColumn "traceAnalysisAPI.streambased.Report.AddResultColumn (Python method) — Adds a new column with the given name to the result table. It is appended at the end of the table. Values can be inserted into this column by using the parameter "additionalInfo" of the methods Spot() and Range(). The entries in the list "additionalInfo" list are inserted into the additional result columns in sequence."))

Spot(*[time](#traceAnalysisAPI.streambased.Range.Spot.time "traceAnalysisAPI.streambased.Range.Spot.time (Python parameter) — timestamp of the spot")*, *[message](#traceAnalysisAPI.streambased.Range.Spot.message "traceAnalysisAPI.streambased.Range.Spot.message (Python parameter) — a textual message describing the spot")=`None`*, *[resultId](#traceAnalysisAPI.streambased.Range.Spot.resultId "traceAnalysisAPI.streambased.Range.Spot.resultId (Python parameter) — the verdict for the spot")=`None`*, *[additionalInfo](#traceAnalysisAPI.streambased.Range.Spot.additionalInfo "traceAnalysisAPI.streambased.Range.Spot.additionalInfo (Python parameter) — a list of additional information, that will be shown in the custom result columns (see Report.AddResultColumn())")=`None`*)[¶](#traceAnalysisAPI.streambased.Range.Spot "Link to this definition")  
Adds a signal spot to a range.

Parameters:  time : float[¶](#traceAnalysisAPI.streambased.Range.Spot.time "Permalink to this definition")  
timestamp of the spot

message : string[¶](#traceAnalysisAPI.streambased.Range.Spot.message "Permalink to this definition")  
a textual message describing the spot

resultId : int[¶](#traceAnalysisAPI.streambased.Range.Spot.resultId "Permalink to this definition")  
the verdict for the spot

additionalInfo : list of strings[¶](#traceAnalysisAPI.streambased.Range.Spot.additionalInfo "Permalink to this definition")  
a list of additional information, that will be shown in the custom result columns (see [`Report.AddResultColumn()`](#traceAnalysisAPI.streambased.Report.AddResultColumn "traceAnalysisAPI.streambased.Report.AddResultColumn (Python method) — Adds a new column with the given name to the result table. It is appended at the end of the table. Values can be inserted into this column by using the parameter "additionalInfo" of the methods Spot() and Range(). The entries in the list "additionalInfo" list are inserted into the additional result columns in sequence."))

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
