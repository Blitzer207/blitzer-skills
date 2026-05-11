[ Array-based NumPy trace step templates ](array_based_templates.md)

Event based tracestep templates [ Event based tracestep templates ](#)

Event based tracestep templates

- [ DataContainer ](#datacontainer)
  - [C traceAnalysisAPI.DataContainer ](#traceAnalysisAPI.DataContainer)
    - [M EmitSignal ](#traceAnalysisAPI.DataContainer.EmitSignal)
    - [M GetTemplateSignalNames ](#traceAnalysisAPI.DataContainer.GetTemplateSignalNames)
    - [M GetGenericSignalName ](#traceAnalysisAPI.DataContainer.GetGenericSignalName)
    - [M GetMappingItemName ](#traceAnalysisAPI.DataContainer.GetMappingItemName)
    - [M GetOriginalSignalName ](#traceAnalysisAPI.DataContainer.GetOriginalSignalName)
    - [M GetRecordingInfo ](#traceAnalysisAPI.DataContainer.GetRecordingInfo)
    - [M GetGlobalConstantNames ](#traceAnalysisAPI.DataContainer.GetGlobalConstantNames)
    - [M GetGlobalConstant ](#traceAnalysisAPI.DataContainer.GetGlobalConstant)
    - [M IsSignalInRecording ](#traceAnalysisAPI.DataContainer.IsSignalInRecording)
    - [M GetUnit ](#traceAnalysisAPI.DataContainer.GetUnit)
    - [M GetTextTable ](#traceAnalysisAPI.DataContainer.GetTextTable)
- [ Report ](#report)
  - [C traceAnalysisAPI.Report ](#traceAnalysisAPI.Report)
    - [M AddResultColumn ](#traceAnalysisAPI.Report.AddResultColumn)
    - [M GetLastTable ](#traceAnalysisAPI.Report.GetLastTable)
    - [M GetResultId ](#traceAnalysisAPI.Report.GetResultId)
    - [M GetTable ](#traceAnalysisAPI.Report.GetTable)
    - [M GetTableByIndex ](#traceAnalysisAPI.Report.GetTableByIndex)
    - [M GetTableCount ](#traceAnalysisAPI.Report.GetTableCount)
    - [M HasTable ](#traceAnalysisAPI.Report.HasTable)
    - [M Image ](#traceAnalysisAPI.Report.Image)
    - [M Log ](#traceAnalysisAPI.Report.Log)
    - [M LogDebug ](#traceAnalysisAPI.Report.LogDebug)
    - [M LogError ](#traceAnalysisAPI.Report.LogError)
    - [M LogInfo ](#traceAnalysisAPI.Report.LogInfo)
    - [M LogWarning ](#traceAnalysisAPI.Report.LogWarning)
    - [M Range ](#traceAnalysisAPI.Report.Range)
    - [M RemoveTable ](#traceAnalysisAPI.Report.RemoveTable)
    - [M SetLogComponent ](#traceAnalysisAPI.Report.SetLogComponent)
    - [M SetResultError ](#traceAnalysisAPI.Report.SetResultError)
    - [M SetResultFailed ](#traceAnalysisAPI.Report.SetResultFailed)
    - [M SetResultId ](#traceAnalysisAPI.Report.SetResultId)
    - [M SetResultInconclusive ](#traceAnalysisAPI.Report.SetResultInconclusive)
    - [M SetResultSuccess ](#traceAnalysisAPI.Report.SetResultSuccess)
    - [M SetResultText ](#traceAnalysisAPI.Report.SetResultText)
    - [M Spot ](#traceAnalysisAPI.Report.Spot)
    - [M Table ](#traceAnalysisAPI.Report.Table)
    - [M UpdateResultId ](#traceAnalysisAPI.Report.UpdateResultId)
- [ SignalEvent ](#signalevent)
  - [C traceAnalysisAPI.SignalEvent ](#traceAnalysisAPI.SignalEvent)
    - [M GetSignal ](#traceAnalysisAPI.SignalEvent.GetSignal)
    - [M GetSignals ](#traceAnalysisAPI.SignalEvent.GetSignals)
    - [M GetTime ](#traceAnalysisAPI.SignalEvent.GetTime)
    - [M GetValue ](#traceAnalysisAPI.SignalEvent.GetValue)
- [ Hold ](#hold)
  - [C traceAnalysisAPI.Hold ](#traceAnalysisAPI.Hold)
    - [M GetSignal ](#traceAnalysisAPI.Hold.GetSignal)
    - [M GetSignals ](#traceAnalysisAPI.Hold.GetSignals)
    - [M GetValue ](#traceAnalysisAPI.Hold.GetValue)
- [ Parameters ](#parameters)
  - [A TraceStep.parameters ](#traceAnalysisAPI.TraceStep.parameters)
- [ Signal ](#signal)
  - [C traceAnalysisAPI.Signal ](#traceAnalysisAPI.Signal)
    - [M GetName ](#traceAnalysisAPI.Signal.GetName)
    - [M GetPrevValue ](#traceAnalysisAPI.Signal.GetPrevValue)
    - [M GetTime ](#traceAnalysisAPI.Signal.GetTime)
    - [M GetValue ](#traceAnalysisAPI.Signal.GetValue)
- [ RecordingInfo ](#recordinginfo)
  - [C traceAnalysisAPI.RecordingInfo ](#traceAnalysisAPI.RecordingInfo)
    - [M GetFirstPath ](#traceAnalysisAPI.RecordingInfo.GetFirstPath)
    - [M GetPath ](#traceAnalysisAPI.RecordingInfo.GetPath)
    - [M GetPathList ](#traceAnalysisAPI.RecordingInfo.GetPathList)
    - [M GetRecordingName ](#traceAnalysisAPI.RecordingInfo.GetRecordingName)
    - [M GetRecordingNumber ](#traceAnalysisAPI.RecordingInfo.GetRecordingNumber)
    - [M GetRecordingType ](#traceAnalysisAPI.RecordingInfo.GetRecordingType)
    - [M GetStartTimeNs ](#traceAnalysisAPI.RecordingInfo.GetStartTimeNs)
- [ ReportTable ](#reporttable)
  - [C traceAnalysisAPI.ReportTable ](#traceAnalysisAPI.ReportTable)
    - [M AddRow ](#traceAnalysisAPI.ReportTable.AddRow)
    - [M SetHeader ](#traceAnalysisAPI.ReportTable.SetHeader)
- [ Range ](#range)
  - [C traceAnalysisAPI.Range ](#traceAnalysisAPI.Range)
    - [M Range ](#traceAnalysisAPI.Range.Range)
    - [M Spot ](#traceAnalysisAPI.Range.Spot)

[ Stream based tracestep templates ](stream_based_templates.md)

[ Custom GUI for parameters ](custom_param_gui.md)

[ Custom trace synchronization ](custom_trace_synchronization.md)

[ Available python libraries and APIs ](python_libraries.md)

Event based tracestep templates

- [ DataContainer ](#datacontainer)
  - [C traceAnalysisAPI.DataContainer ](#traceAnalysisAPI.DataContainer)
    - [M EmitSignal ](#traceAnalysisAPI.DataContainer.EmitSignal)
    - [M GetTemplateSignalNames ](#traceAnalysisAPI.DataContainer.GetTemplateSignalNames)
    - [M GetGenericSignalName ](#traceAnalysisAPI.DataContainer.GetGenericSignalName)
    - [M GetMappingItemName ](#traceAnalysisAPI.DataContainer.GetMappingItemName)
    - [M GetOriginalSignalName ](#traceAnalysisAPI.DataContainer.GetOriginalSignalName)
    - [M GetRecordingInfo ](#traceAnalysisAPI.DataContainer.GetRecordingInfo)
    - [M GetGlobalConstantNames ](#traceAnalysisAPI.DataContainer.GetGlobalConstantNames)
    - [M GetGlobalConstant ](#traceAnalysisAPI.DataContainer.GetGlobalConstant)
    - [M IsSignalInRecording ](#traceAnalysisAPI.DataContainer.IsSignalInRecording)
    - [M GetUnit ](#traceAnalysisAPI.DataContainer.GetUnit)
    - [M GetTextTable ](#traceAnalysisAPI.DataContainer.GetTextTable)
- [ Report ](#report)
  - [C traceAnalysisAPI.Report ](#traceAnalysisAPI.Report)
    - [M AddResultColumn ](#traceAnalysisAPI.Report.AddResultColumn)
    - [M GetLastTable ](#traceAnalysisAPI.Report.GetLastTable)
    - [M GetResultId ](#traceAnalysisAPI.Report.GetResultId)
    - [M GetTable ](#traceAnalysisAPI.Report.GetTable)
    - [M GetTableByIndex ](#traceAnalysisAPI.Report.GetTableByIndex)
    - [M GetTableCount ](#traceAnalysisAPI.Report.GetTableCount)
    - [M HasTable ](#traceAnalysisAPI.Report.HasTable)
    - [M Image ](#traceAnalysisAPI.Report.Image)
    - [M Log ](#traceAnalysisAPI.Report.Log)
    - [M LogDebug ](#traceAnalysisAPI.Report.LogDebug)
    - [M LogError ](#traceAnalysisAPI.Report.LogError)
    - [M LogInfo ](#traceAnalysisAPI.Report.LogInfo)
    - [M LogWarning ](#traceAnalysisAPI.Report.LogWarning)
    - [M Range ](#traceAnalysisAPI.Report.Range)
    - [M RemoveTable ](#traceAnalysisAPI.Report.RemoveTable)
    - [M SetLogComponent ](#traceAnalysisAPI.Report.SetLogComponent)
    - [M SetResultError ](#traceAnalysisAPI.Report.SetResultError)
    - [M SetResultFailed ](#traceAnalysisAPI.Report.SetResultFailed)
    - [M SetResultId ](#traceAnalysisAPI.Report.SetResultId)
    - [M SetResultInconclusive ](#traceAnalysisAPI.Report.SetResultInconclusive)
    - [M SetResultSuccess ](#traceAnalysisAPI.Report.SetResultSuccess)
    - [M SetResultText ](#traceAnalysisAPI.Report.SetResultText)
    - [M Spot ](#traceAnalysisAPI.Report.Spot)
    - [M Table ](#traceAnalysisAPI.Report.Table)
    - [M UpdateResultId ](#traceAnalysisAPI.Report.UpdateResultId)
- [ SignalEvent ](#signalevent)
  - [C traceAnalysisAPI.SignalEvent ](#traceAnalysisAPI.SignalEvent)
    - [M GetSignal ](#traceAnalysisAPI.SignalEvent.GetSignal)
    - [M GetSignals ](#traceAnalysisAPI.SignalEvent.GetSignals)
    - [M GetTime ](#traceAnalysisAPI.SignalEvent.GetTime)
    - [M GetValue ](#traceAnalysisAPI.SignalEvent.GetValue)
- [ Hold ](#hold)
  - [C traceAnalysisAPI.Hold ](#traceAnalysisAPI.Hold)
    - [M GetSignal ](#traceAnalysisAPI.Hold.GetSignal)
    - [M GetSignals ](#traceAnalysisAPI.Hold.GetSignals)
    - [M GetValue ](#traceAnalysisAPI.Hold.GetValue)
- [ Parameters ](#parameters)
  - [A TraceStep.parameters ](#traceAnalysisAPI.TraceStep.parameters)
- [ Signal ](#signal)
  - [C traceAnalysisAPI.Signal ](#traceAnalysisAPI.Signal)
    - [M GetName ](#traceAnalysisAPI.Signal.GetName)
    - [M GetPrevValue ](#traceAnalysisAPI.Signal.GetPrevValue)
    - [M GetTime ](#traceAnalysisAPI.Signal.GetTime)
    - [M GetValue ](#traceAnalysisAPI.Signal.GetValue)
- [ RecordingInfo ](#recordinginfo)
  - [C traceAnalysisAPI.RecordingInfo ](#traceAnalysisAPI.RecordingInfo)
    - [M GetFirstPath ](#traceAnalysisAPI.RecordingInfo.GetFirstPath)
    - [M GetPath ](#traceAnalysisAPI.RecordingInfo.GetPath)
    - [M GetPathList ](#traceAnalysisAPI.RecordingInfo.GetPathList)
    - [M GetRecordingName ](#traceAnalysisAPI.RecordingInfo.GetRecordingName)
    - [M GetRecordingNumber ](#traceAnalysisAPI.RecordingInfo.GetRecordingNumber)
    - [M GetRecordingType ](#traceAnalysisAPI.RecordingInfo.GetRecordingType)
    - [M GetStartTimeNs ](#traceAnalysisAPI.RecordingInfo.GetStartTimeNs)
- [ ReportTable ](#reporttable)
  - [C traceAnalysisAPI.ReportTable ](#traceAnalysisAPI.ReportTable)
    - [M AddRow ](#traceAnalysisAPI.ReportTable.AddRow)
    - [M SetHeader ](#traceAnalysisAPI.ReportTable.SetHeader)
- [ Range ](#range)
  - [C traceAnalysisAPI.Range ](#traceAnalysisAPI.Range)
    - [M Range ](#traceAnalysisAPI.Range.Range)
    - [M Spot ](#traceAnalysisAPI.Range.Spot)

# Event based tracestep templates[¶](#event-based-tracestep-templates "Link to this heading")

## DataContainer[¶](#datacontainer "Link to this heading")

*class* traceAnalysisAPI.DataContainer[¶](#traceAnalysisAPI.DataContainer "Link to this definition")  
The DataContainer is a container to buffer values during the execution of Python based trace steps.

To assign a \<value\> to an arbitrary \<key\> just write:

    dataContainer.<key> = <value>

Example:

    dataContainer.index = 0

EmitSignal(*[time](#traceAnalysisAPI.DataContainer.EmitSignal.time "traceAnalysisAPI.DataContainer.EmitSignal.time (Python parameter) — timeStamp of the emitted signal event")*, *[traceStepSignalName](#traceAnalysisAPI.DataContainer.EmitSignal.traceStepSignalName "traceAnalysisAPI.DataContainer.EmitSignal.traceStepSignalName (Python parameter) — the name of the tracesteps output signal that should be emitted (see TraceStep.DefineOutSignals())")*, *[value](#traceAnalysisAPI.DataContainer.EmitSignal.value "traceAnalysisAPI.DataContainer.EmitSignal.value (Python parameter) — the value of the emitted signal")*)[¶](#traceAnalysisAPI.DataContainer.EmitSignal "Link to this definition")  
Emits a signal event back into the current trace analysis session.

Parameters:  time : float[¶](#traceAnalysisAPI.DataContainer.EmitSignal.time "Permalink to this definition")  
timeStamp of the emitted signal event

traceStepSignalName : string[¶](#traceAnalysisAPI.DataContainer.EmitSignal.traceStepSignalName "Permalink to this definition")  
the name of the tracesteps output signal that should be emitted (see `TraceStep.DefineOutSignals()`)

value : float[¶](#traceAnalysisAPI.DataContainer.EmitSignal.value "Permalink to this definition")  
the value of the emitted signal

GetTemplateSignalNames()[¶](#traceAnalysisAPI.DataContainer.GetTemplateSignalNames "Link to this definition")  
Returns the names of all user defined signal names in the trace step template.

Returns:  names of all user defined signal names in the trace step template

Return type:  list of strings

GetGenericSignalName(*[templateSignalName](#traceAnalysisAPI.DataContainer.GetGenericSignalName.templateSignalName "traceAnalysisAPI.DataContainer.GetGenericSignalName.templateSignalName (Python parameter) — name of the template signal")*)[¶](#traceAnalysisAPI.DataContainer.GetGenericSignalName "Link to this definition")  
Returns the name of the assigned generic signal for a given signal name of the trace step template.

Parameters:  templateSignalName : string[¶](#traceAnalysisAPI.DataContainer.GetGenericSignalName.templateSignalName "Permalink to this definition")  
name of the template signal

Returns:  name of the generic signal

Return type:  string

GetMappingItemName(*[templateSignalName](#traceAnalysisAPI.DataContainer.GetMappingItemName.templateSignalName "traceAnalysisAPI.DataContainer.GetMappingItemName.templateSignalName (Python parameter) — name of the template signal")*)[¶](#traceAnalysisAPI.DataContainer.GetMappingItemName "Link to this definition")  
Returns the name (of the reference (= source)) of the mapping item which corresponds to the assigned generic signal for a given signal name of the trace step template.

Parameters:  templateSignalName : string[¶](#traceAnalysisAPI.DataContainer.GetMappingItemName.templateSignalName "Permalink to this definition")  
name of the template signal

Returns:  name (of the reference (= source)) of the mapping item

Return type:  string

GetOriginalSignalName(*[templateSignalName](#traceAnalysisAPI.DataContainer.GetOriginalSignalName.templateSignalName "traceAnalysisAPI.DataContainer.GetOriginalSignalName.templateSignalName (Python parameter) — name of the template signal")*)[¶](#traceAnalysisAPI.DataContainer.GetOriginalSignalName "Link to this definition")  
Returns the original signal name of the assigned generic signal for a given signal name of the trace step template.

Parameters:  templateSignalName : string[¶](#traceAnalysisAPI.DataContainer.GetOriginalSignalName.templateSignalName "Permalink to this definition")  
name of the template signal

Returns:  name of the original signal

Return type:  string

GetRecordingInfo(*[templateSignalName](#traceAnalysisAPI.DataContainer.GetRecordingInfo.templateSignalName "traceAnalysisAPI.DataContainer.GetRecordingInfo.templateSignalName (Python parameter) — name of the template signal")*)[¶](#traceAnalysisAPI.DataContainer.GetRecordingInfo "Link to this definition")  
Returns the RecordingInfo of the assigned generic signal for a given signal name of the trace step template. If the returned value is not None, one can call the methods [`GetPath()`](#traceAnalysisAPI.RecordingInfo.GetPath "traceAnalysisAPI.RecordingInfo.GetPath (Python method) — Returns the path (or the first path if there is a list of paths) for the recording."), [`GetRecordingName()`](#traceAnalysisAPI.RecordingInfo.GetRecordingName "traceAnalysisAPI.RecordingInfo.GetRecordingName (Python method) — Returns the name of the recording."), [`GetRecordingNumber()`](#traceAnalysisAPI.RecordingInfo.GetRecordingNumber "traceAnalysisAPI.RecordingInfo.GetRecordingNumber (Python method) — Returns the number of the recording.") and [`GetRecordingType()`](#traceAnalysisAPI.RecordingInfo.GetRecordingType "traceAnalysisAPI.RecordingInfo.GetRecordingType (Python method) — Returns the type of the recording.") on the returned RecordingInfo object to obtain further information.

Parameters:  templateSignalName : string[¶](#traceAnalysisAPI.DataContainer.GetRecordingInfo.templateSignalName "Permalink to this definition")  
name of the template signal

Returns:  [`RecordingInfo`](#traceAnalysisAPI.RecordingInfo "traceAnalysisAPI.RecordingInfo (Python class) — A RecordingInfo object contains information about the name, number, type and path of the underlying recording from which the signal stems.") if the source of the assigned generic signal is a recording else None

Return type:  [`RecordingInfo`](#traceAnalysisAPI.RecordingInfo "traceAnalysisAPI.RecordingInfo (Python class) — A RecordingInfo object contains information about the name, number, type and path of the underlying recording from which the signal stems.") or None

GetGlobalConstantNames()[¶](#traceAnalysisAPI.DataContainer.GetGlobalConstantNames "Link to this definition")  
Returns a list of names containing all global constants.

Returns:  A list of names.

Return type:  list

GetGlobalConstant(*[name](#traceAnalysisAPI.DataContainer.GetGlobalConstant.name "traceAnalysisAPI.DataContainer.GetGlobalConstant.name (Python parameter) — The name of the constant to retrieve the value.")*)[¶](#traceAnalysisAPI.DataContainer.GetGlobalConstant "Link to this definition")  
Returns the value of the given global constant.

Parameters:  name : string[¶](#traceAnalysisAPI.DataContainer.GetGlobalConstant.name "Permalink to this definition")  
The name of the constant to retrieve the value.

Returns:  The value of the constant.

Return type:  object

IsSignalInRecording(*[templateSignalName](#traceAnalysisAPI.DataContainer.IsSignalInRecording.templateSignalName "traceAnalysisAPI.DataContainer.IsSignalInRecording.templateSignalName (Python parameter) — name of the template signal")*)[¶](#traceAnalysisAPI.DataContainer.IsSignalInRecording "Link to this definition")  
Returns whether the signal associated with the given template signal was found in the recording specified by [`GetRecordingInfo()`](#traceAnalysisAPI.DataContainer.GetRecordingInfo "traceAnalysisAPI.DataContainer.GetRecordingInfo (Python method) — Returns the RecordingInfo of the assigned generic signal for a given signal name of the trace step template. If the returned value is not None, one can call the methods GetPath(), GetRecordingName(), GetRecordingNumber() and GetRecordingType() on the returned RecordingInfo object to obtain further information.").

Parameters:  templateSignalName : string[¶](#traceAnalysisAPI.DataContainer.IsSignalInRecording.templateSignalName "Permalink to this definition")  
name of the template signal

Returns:  True if the associated signal was found in the corresponding recording else False

Return type:  bool

GetUnit(*[templateSignalName](#traceAnalysisAPI.DataContainer.GetUnit.templateSignalName "traceAnalysisAPI.DataContainer.GetUnit.templateSignalName (Python parameter) — name of the template signal"): str*)[¶](#traceAnalysisAPI.DataContainer.GetUnit "Link to this definition")  
Returns the unit of the signal with the given name.

Parameters:  templateSignalName : string[¶](#traceAnalysisAPI.DataContainer.GetUnit.templateSignalName "Permalink to this definition")  
name of the template signal

Returns:  The unit of the given signal.

Return type:  str

GetTextTable(*[templateSignalName](#traceAnalysisAPI.DataContainer.GetTextTable.templateSignalName "traceAnalysisAPI.DataContainer.GetTextTable.templateSignalName (Python parameter) — name of the template signal"): str*)[¶](#traceAnalysisAPI.DataContainer.GetTextTable "Link to this definition")  
Returns the text table and the default value of the signal with the given name as tuple.

Parameters:  templateSignalName : string[¶](#traceAnalysisAPI.DataContainer.GetTextTable.templateSignalName "Permalink to this definition")  
name of the template signal

Returns:  The text table and the default text table as tuple.

Return type:  tuple

## Report[¶](#report "Link to this heading")

*class* traceAnalysisAPI.Report[¶](#traceAnalysisAPI.Report "Link to this definition")  
AddResultColumn(*[name](#traceAnalysisAPI.Report.AddResultColumn.name "traceAnalysisAPI.Report.AddResultColumn.name (Python parameter) — name of the new column"): str*) → None[¶](#traceAnalysisAPI.Report.AddResultColumn "Link to this definition")  
Adds a new column with the given name to the result table. It is appended at the end of the table. Values can be inserted into this column by using the parameter “additionalInfo” of the methods [`Spot()`](#traceAnalysisAPI.Report.Spot "traceAnalysisAPI.Report.Spot (Python method) — Adds a signal spot to the test report.") and [`Range()`](#traceAnalysisAPI.Report.Range "traceAnalysisAPI.Report.Range (Python method) — Adds a range to the test report and returns a range object."). The entries in the list “additionalInfo” list are inserted into the additional result columns in sequence.

Parameters:  name : str[¶](#traceAnalysisAPI.Report.AddResultColumn.name "Permalink to this definition")  
name of the new column

GetLastTable() → ReportTable[¶](#traceAnalysisAPI.Report.GetLastTable "Link to this definition")  
Returns the last table created.

Return type:  [`ReportTable`](#traceAnalysisAPI.ReportTable "traceAnalysisAPI.ReportTable (Python class) — A ReportTable object represents a table in the test report.")

GetResultId() → int | None[¶](#traceAnalysisAPI.Report.GetResultId "Link to this definition")  
Gets the current result id.

The result id passed to an earlier call to [`SetResultId()`](#traceAnalysisAPI.Report.SetResultId "traceAnalysisAPI.Report.SetResultId (Python method) — Sets the result id for the current trace step.") is returned. If [`SetResultId()`](#traceAnalysisAPI.Report.SetResultId "traceAnalysisAPI.Report.SetResultId (Python method) — Sets the result id for the current trace step.") wasn’t called before, `dataContainer.RESULT_ID_NONE` is returned.

Returns:  the result id

Return type:  int

GetTable(*[tableId](#traceAnalysisAPI.Report.GetTable.tableId "traceAnalysisAPI.Report.GetTable.tableId (Python parameter) — id of the table"): str*) → ReportTable[¶](#traceAnalysisAPI.Report.GetTable "Link to this definition")  
Returns the table with the given id.

Parameters:  tableId : str[¶](#traceAnalysisAPI.Report.GetTable.tableId "Permalink to this definition")  
id of the table

Return type:  [`ReportTable`](#traceAnalysisAPI.ReportTable "traceAnalysisAPI.ReportTable (Python class) — A ReportTable object represents a table in the test report.")

GetTableByIndex(*[index](#traceAnalysisAPI.Report.GetTableByIndex.index "traceAnalysisAPI.Report.GetTableByIndex.index (Python parameter) — the position of the table"): int*) → ReportTable[¶](#traceAnalysisAPI.Report.GetTableByIndex "Link to this definition")  
Returns the table by the given position in the list of user-defined tables.

Parameters:  index : int[¶](#traceAnalysisAPI.Report.GetTableByIndex.index "Permalink to this definition")  
the position of the table

Return type:  [`ReportTable`](#traceAnalysisAPI.ReportTable "traceAnalysisAPI.ReportTable (Python class) — A ReportTable object represents a table in the test report.")

GetTableCount() → int[¶](#traceAnalysisAPI.Report.GetTableCount "Link to this definition")  
Returns the count of tables.

Returns:  The count of tables.

Return type:  int

HasTable(*[tableId](#traceAnalysisAPI.Report.HasTable.tableId "traceAnalysisAPI.Report.HasTable.tableId (Python parameter) — id of the table"): str*) → bool[¶](#traceAnalysisAPI.Report.HasTable "Link to this definition")  
Returns whether a particular table exists for the trace step.

Parameters:  tableId : str[¶](#traceAnalysisAPI.Report.HasTable.tableId "Permalink to this definition")  
id of the table

Returns:  True if a table with the given id exists, else False

Return type:  bool

Image(*[imageSource](#traceAnalysisAPI.Report.Image.imageSource "traceAnalysisAPI.Report.Image.imageSource (Python parameter) — The image source can be one of the following:"): str | Path | ImageInterface | ndarray | bytes*, *\**, *[name](#traceAnalysisAPI.Report.Image.name "traceAnalysisAPI.Report.Image.name (Python parameter) — The filename (with correct extension)."): str | None = `None`*, *[title](#traceAnalysisAPI.Report.Image.title "traceAnalysisAPI.Report.Image.title (Python parameter) — the image title"): str | None = `None`*, *[embedded](#traceAnalysisAPI.Report.Image.embedded "traceAnalysisAPI.Report.Image.embedded (Python parameter) — True, if the image file should be embedded in the test report, else the image file is stored in the test report folder."): bool = `False`*, *[limitPreviewSize](#traceAnalysisAPI.Report.Image.limitPreviewSize "traceAnalysisAPI.Report.Image.limitPreviewSize (Python parameter) — If True (default), the preview image shown in the report will be limited to a maximum size."): bool = `True`*, *[autoDelete](#traceAnalysisAPI.Report.Image.autoDelete "traceAnalysisAPI.Report.Image.autoDelete (Python parameter) — Only applicable if imageSource is a file path."): bool = `False`*, *[useTemp](#traceAnalysisAPI.Report.Image.useTemp "traceAnalysisAPI.Report.Image.useTemp (Python parameter) — Only applicable if imageSource is a file path."): bool = `True`*) → ReportImage[¶](#traceAnalysisAPI.Report.Image "Link to this definition")  
Adds the given image to the test report. If the image is not embedded in the test report, the file will be stored in the report folder. If there is already an image with the same name, the image files will be enumerated.

Parameters:  imageSource : str|Path|Image|Frame|numpy.ndarray|bytes[¶](#traceAnalysisAPI.Report.Image.imageSource "Permalink to this definition")  
The image source can be one of the following:

- an absolute file path

- an Image or Frame object

- a NumPy array in OpenCV style: shape is (height, width, 3) of type numpy.uint8, the three colors have the order BGR!

- bytes object with image data

name : str[¶](#traceAnalysisAPI.Report.Image.name "Permalink to this definition")  
The filename (with correct extension). Will be used as filename if an image file is created in the report folder. If name is None and the source is a path or an Image or Frame, the name of the imageSource is used.

title : str[¶](#traceAnalysisAPI.Report.Image.title "Permalink to this definition")  
the image title

embedded : bool[¶](#traceAnalysisAPI.Report.Image.embedded "Permalink to this definition")  
True, if the image file should be embedded in the test report, else the image file is stored in the test report folder.

limitPreviewSize : bool[¶](#traceAnalysisAPI.Report.Image.limitPreviewSize "Permalink to this definition")  
If True (default), the preview image shown in the report will be limited to a maximum size.

autoDelete : bool[¶](#traceAnalysisAPI.Report.Image.autoDelete "Permalink to this definition")  
Only applicable if imageSource is a file path. True, if the image file should be automatically deleted, else False.

useTemp : bool[¶](#traceAnalysisAPI.Report.Image.useTemp "Permalink to this definition")  
Only applicable if imageSource is a file path. True, if the image file should be copied into a temporary directory, False, if it should be used directly. Using a temporary copy might be necessary to avoid overriding the image before the final report gets assembled later on.

Log(*[level](#traceAnalysisAPI.Report.Log.level "traceAnalysisAPI.Report.Log.level (Python parameter) — log level")*, *[time](#traceAnalysisAPI.Report.Log.time "traceAnalysisAPI.Report.Log.time (Python parameter) — timestamp of the log message")*, *[message](#traceAnalysisAPI.Report.Log.message "traceAnalysisAPI.Report.Log.message (Python parameter) — log message or format string.")*, *\*[formatArgs](#traceAnalysisAPI.Report.Log.formatArgs "traceAnalysisAPI.Report.Log.formatArgs (Python parameter) — additional non-keyword arguments used when message is a format string")*, *\*\*[formatKwargs](#traceAnalysisAPI.Report.Log.formatKwargs "traceAnalysisAPI.Report.Log.formatKwargs (Python parameter) — additional keyword arguments used when message is a format string")*)[¶](#traceAnalysisAPI.Report.Log "Link to this definition")  
Adds a log message to the trace analysis log file. Use [`SetLogComponent()`](#traceAnalysisAPI.Report.SetLogComponent "traceAnalysisAPI.Report.SetLogComponent (Python method) — Sets the component that will be used in logging entries created by calling log methods.") to set the component part of the log entry.

Parameters:  level : int[¶](#traceAnalysisAPI.Report.Log.level "Permalink to this definition")  
log level

- report.LOG_LEVEL_DEBUG

- report.LOG_LEVEL_INFO

- report.LOG_LEVEL_WARNING

- report.LOG_LEVEL_ERROR

time : float[¶](#traceAnalysisAPI.Report.Log.time "Permalink to this definition")  
timestamp of the log message

message : str[¶](#traceAnalysisAPI.Report.Log.message "Permalink to this definition")  
log message or format string.

\*formatArgs[¶](#traceAnalysisAPI.Report.Log.formatArgs "Permalink to this definition")  
additional non-keyword arguments used when message is a format string

\*\*formatKwargs[¶](#traceAnalysisAPI.Report.Log.formatKwargs "Permalink to this definition")  
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

LogDebug(*[time](#traceAnalysisAPI.Report.LogDebug "traceAnalysisAPI.Report.LogDebug.time (Python parameter)")*, *[message](#traceAnalysisAPI.Report.LogDebug "traceAnalysisAPI.Report.LogDebug.message (Python parameter)")*, *\*[formatArgs](#traceAnalysisAPI.Report.LogDebug "traceAnalysisAPI.Report.LogDebug.formatArgs (Python parameter)")*, *\*\*[formatKwargs](#traceAnalysisAPI.Report.LogDebug "traceAnalysisAPI.Report.LogDebug.formatKwargs (Python parameter)")*)[¶](#traceAnalysisAPI.Report.LogDebug "Link to this definition")  
Convenience method to add a debug log message. See [`Log()`](#traceAnalysisAPI.Report.Log "traceAnalysisAPI.Report.Log (Python method) — Adds a log message to the trace analysis log file. Use SetLogComponent() to set the component part of the log entry.") for further usage.

LogError(*[time](#traceAnalysisAPI.Report.LogError "traceAnalysisAPI.Report.LogError.time (Python parameter)")*, *[message](#traceAnalysisAPI.Report.LogError "traceAnalysisAPI.Report.LogError.message (Python parameter)")*, *\*[formatArgs](#traceAnalysisAPI.Report.LogError "traceAnalysisAPI.Report.LogError.formatArgs (Python parameter)")*, *\*\*[formatKwargs](#traceAnalysisAPI.Report.LogError "traceAnalysisAPI.Report.LogError.formatKwargs (Python parameter)")*)[¶](#traceAnalysisAPI.Report.LogError "Link to this definition")  
Convenience method to add an error log message. See [`Log()`](#traceAnalysisAPI.Report.Log "traceAnalysisAPI.Report.Log (Python method) — Adds a log message to the trace analysis log file. Use SetLogComponent() to set the component part of the log entry.") for further usage.

LogInfo(*[time](#traceAnalysisAPI.Report.LogInfo "traceAnalysisAPI.Report.LogInfo.time (Python parameter)")*, *[message](#traceAnalysisAPI.Report.LogInfo "traceAnalysisAPI.Report.LogInfo.message (Python parameter)")*, *\*[formatArgs](#traceAnalysisAPI.Report.LogInfo "traceAnalysisAPI.Report.LogInfo.formatArgs (Python parameter)")*, *\*\*[formatKwargs](#traceAnalysisAPI.Report.LogInfo "traceAnalysisAPI.Report.LogInfo.formatKwargs (Python parameter)")*)[¶](#traceAnalysisAPI.Report.LogInfo "Link to this definition")  
Convenience method to add an info log message. See [`Log()`](#traceAnalysisAPI.Report.Log "traceAnalysisAPI.Report.Log (Python method) — Adds a log message to the trace analysis log file. Use SetLogComponent() to set the component part of the log entry.") for further usage.

LogWarning(*[time](#traceAnalysisAPI.Report.LogWarning "traceAnalysisAPI.Report.LogWarning.time (Python parameter)")*, *[message](#traceAnalysisAPI.Report.LogWarning "traceAnalysisAPI.Report.LogWarning.message (Python parameter)")*, *\*[formatArgs](#traceAnalysisAPI.Report.LogWarning "traceAnalysisAPI.Report.LogWarning.formatArgs (Python parameter)")*, *\*\*[formatKwargs](#traceAnalysisAPI.Report.LogWarning "traceAnalysisAPI.Report.LogWarning.formatKwargs (Python parameter)")*)[¶](#traceAnalysisAPI.Report.LogWarning "Link to this definition")  
Convenience method to add a warning log message. See [`Log()`](#traceAnalysisAPI.Report.Log "traceAnalysisAPI.Report.Log (Python method) — Adds a log message to the trace analysis log file. Use SetLogComponent() to set the component part of the log entry.") for further usage.

Range(*[startTime](#traceAnalysisAPI.Report.Range.startTime "traceAnalysisAPI.Report.Range.startTime (Python parameter) — timestamp at which the range begins"): float | numpy.integer | numpy.floating*, *[endTime](#traceAnalysisAPI.Report.Range.endTime "traceAnalysisAPI.Report.Range.endTime (Python parameter) — timestamp at which the range ends"): float | numpy.integer | numpy.floating*, *[message](#traceAnalysisAPI.Report.Range.message "traceAnalysisAPI.Report.Range.message (Python parameter) — a textual message describing the range"): str = `''`*, *[resultId](#traceAnalysisAPI.Report.Range.resultId "traceAnalysisAPI.Report.Range.resultId (Python parameter) — the verdict for the range"): int | None = `None`*, *[additionalInfo](#traceAnalysisAPI.Report.Range.additionalInfo "traceAnalysisAPI.Report.Range.additionalInfo (Python parameter) — a list of additional information, that will be shown in the custom result columns (see AddResultColumn())"): list[str] | None = `None`*) → RangeEntity[¶](#traceAnalysisAPI.Report.Range "Link to this definition")  
Adds a range to the test report and returns a range object.

Parameters:  startTime : float[¶](#traceAnalysisAPI.Report.Range.startTime "Permalink to this definition")  
timestamp at which the range begins

endTime : float[¶](#traceAnalysisAPI.Report.Range.endTime "Permalink to this definition")  
timestamp at which the range ends

message : str[¶](#traceAnalysisAPI.Report.Range.message "Permalink to this definition")  
a textual message describing the range

resultId : int[¶](#traceAnalysisAPI.Report.Range.resultId "Permalink to this definition")  
the verdict for the range

additionalInfo : list of strings[¶](#traceAnalysisAPI.Report.Range.additionalInfo "Permalink to this definition")  
a list of additional information, that will be shown in the custom result columns (see [`AddResultColumn()`](#traceAnalysisAPI.Report.AddResultColumn "traceAnalysisAPI.Report.AddResultColumn (Python method) — Adds a new column with the given name to the result table. It is appended at the end of the table. Values can be inserted into this column by using the parameter "additionalInfo" of the methods Spot() and Range(). The entries in the list "additionalInfo" list are inserted into the additional result columns in sequence."))

Return type:  [`Range`](#traceAnalysisAPI.Range "traceAnalysisAPI.Range (Python class) — Class representing a range in the test report. An instance of Range is returned by the call of Report.Range(). To specify the range in more detail, it is possible to add spots and sub ranges as children to a range object.")

RemoveTable(*[tableId](#traceAnalysisAPI.Report.RemoveTable.tableId "traceAnalysisAPI.Report.RemoveTable.tableId (Python parameter) — id of the table"): str*) → None[¶](#traceAnalysisAPI.Report.RemoveTable "Link to this definition")  
Removes a table from the test report.

Parameters:  tableId : str[¶](#traceAnalysisAPI.Report.RemoveTable.tableId "Permalink to this definition")  
id of the table

SetLogComponent(*[component](#traceAnalysisAPI.Report.SetLogComponent.component "traceAnalysisAPI.Report.SetLogComponent.component (Python parameter) — name of the component")*)[¶](#traceAnalysisAPI.Report.SetLogComponent "Link to this definition")  
Sets the component that will be used in logging entries created by calling log methods.

Parameters:  component : str[¶](#traceAnalysisAPI.Report.SetLogComponent.component "Permalink to this definition")  
name of the component

SetResultError()[¶](#traceAnalysisAPI.Report.SetResultError "Link to this definition")  
Convenience method for report.SetResultId(report.RESULT_ID_ERROR)

SetResultFailed()[¶](#traceAnalysisAPI.Report.SetResultFailed "Link to this definition")  
Convenience method for report.SetResultId(report.RESULT_ID_FAILED)

SetResultId(*[resultId](#traceAnalysisAPI.Report.SetResultId.resultId "traceAnalysisAPI.Report.SetResultId.resultId (Python parameter) — the result id to set")*)[¶](#traceAnalysisAPI.Report.SetResultId "Link to this definition")  
Sets the result id for the current trace step.

The result id can be one of:

- report.RESULT_ID_NONE

- report.RESULT_ID_SUCCESS

- report.RESULT_ID_INCONCLUSIVE

- report.RESULT_ID_FAILED

- report.RESULT_ID_ERROR

The result id is set directly. It is not affected by earlier calls to [`SetResultId()`](#traceAnalysisAPI.Report.SetResultId "traceAnalysisAPI.Report.SetResultId (Python method) — Sets the result id for the current trace step.").

Example:

    report.SetResultId(report.RESULT_ID_ERROR)
    report.SetResultId(report.RESULT_ID_NONE)

    report.GetResultId() # this will result in report.RESULT_ID_NONE

Parameters:  resultId : result id[¶](#traceAnalysisAPI.Report.SetResultId.resultId "Permalink to this definition")  
the result id to set

SetResultInconclusive()[¶](#traceAnalysisAPI.Report.SetResultInconclusive "Link to this definition")  
Convenience method for report.SetResultId(report.RESULT_ID_INCONCLUSIVE)

SetResultSuccess()[¶](#traceAnalysisAPI.Report.SetResultSuccess "Link to this definition")  
Convenience method for report.SetResultId(report.RESULT_ID_SUCCESS)

SetResultText(*[text](#traceAnalysisAPI.Report.SetResultText.text "traceAnalysisAPI.Report.SetResultText.text (Python parameter) — the text"): str | None*) → None[¶](#traceAnalysisAPI.Report.SetResultText "Link to this definition")  
Sets a user-defined text for the result of the report.

Parameters:  text : str[¶](#traceAnalysisAPI.Report.SetResultText.text "Permalink to this definition")  
the text

Spot(*[time](#traceAnalysisAPI.Report.Spot.time "traceAnalysisAPI.Report.Spot.time (Python parameter) — timestamp of the spot")*, *[message](#traceAnalysisAPI.Report.Spot.message "traceAnalysisAPI.Report.Spot.message (Python parameter) — a textual message describing the spot")=`''`*, *[resultId](#traceAnalysisAPI.Report.Spot.resultId "traceAnalysisAPI.Report.Spot.resultId (Python parameter) — the verdict for the spot")=`None`*, *[additionalInfo](#traceAnalysisAPI.Report.Spot.additionalInfo "traceAnalysisAPI.Report.Spot.additionalInfo (Python parameter) — a list of additional information, that will be shown in the custom result columns (see AddResultColumn())")=`None`*)[¶](#traceAnalysisAPI.Report.Spot "Link to this definition")  
Adds a signal spot to the test report.

Parameters:  time : float[¶](#traceAnalysisAPI.Report.Spot.time "Permalink to this definition")  
timestamp of the spot

message : an object, that can be converted to via str(message)[¶](#traceAnalysisAPI.Report.Spot.message "Permalink to this definition")  
a textual message describing the spot

resultId : result id[¶](#traceAnalysisAPI.Report.Spot.resultId "Permalink to this definition")  
the verdict for the spot

additionalInfo : list of strings[¶](#traceAnalysisAPI.Report.Spot.additionalInfo "Permalink to this definition")  
a list of additional information, that will be shown in the custom result columns (see [`AddResultColumn()`](#traceAnalysisAPI.Report.AddResultColumn "traceAnalysisAPI.Report.AddResultColumn (Python method) — Adds a new column with the given name to the result table. It is appended at the end of the table. Values can be inserted into this column by using the parameter "additionalInfo" of the methods Spot() and Range(). The entries in the list "additionalInfo" list are inserted into the additional result columns in sequence."))

Table(*[tableId](#traceAnalysisAPI.Report.Table.tableId "traceAnalysisAPI.Report.Table.tableId (Python parameter) — id to identify the table"): str | int | None = `None`*, *[headerValues](#traceAnalysisAPI.Report.Table.headerValues "traceAnalysisAPI.Report.Table.headerValues (Python parameter) — iterable with the entries of the table header"): Iterable[str | int] | None = `None`*) → ReportTable[¶](#traceAnalysisAPI.Report.Table "Link to this definition")  
Creates a table in the test report.

Example:

    table = report.Table("table1", ["time", "description"])
    table.AddRow(["1.3", "A rising edge detected"])
    table.AddRow(["3.8", "A falling edge detected"])

Parameters:  tableId : str[¶](#traceAnalysisAPI.Report.Table.tableId "Permalink to this definition")  
id to identify the table

headerValues : iterable[¶](#traceAnalysisAPI.Report.Table.headerValues "Permalink to this definition")  
iterable with the entries of the table header

Returns:  the report table object

Return type:  [`ReportTable`](#traceAnalysisAPI.ReportTable "traceAnalysisAPI.ReportTable (Python class) — A ReportTable object represents a table in the test report.")

UpdateResultId(*[resultId](#traceAnalysisAPI.Report.UpdateResultId.resultId "traceAnalysisAPI.Report.UpdateResultId.resultId (Python parameter) — the result id to set")*)[¶](#traceAnalysisAPI.Report.UpdateResultId "Link to this definition")  
Updates the result id for the current trace step.

The result id can be one of:

- report.RESULT_ID_NONE

- report.RESULT_ID_SUCCESS

- report.RESULT_ID_INCONCLUSIVE

- report.RESULT_ID_FAILED

- report.RESULT_ID_ERROR

In contrast to [`SetResultId()`](#traceAnalysisAPI.Report.SetResultId "traceAnalysisAPI.Report.SetResultId (Python method) — Sets the result id for the current trace step."), which sets the resultId directly, [`UpdateResultId()`](#traceAnalysisAPI.Report.UpdateResultId "traceAnalysisAPI.Report.UpdateResultId (Python method) — Updates the result id for the current trace step.") can only increase the resultId according to the following ordering:

RESULT_ID_NONE \< RESULT_ID_SUCCESS \< RESULT_ID_INCONCLUSIVE \< RESULT_ID_FAILED \< RESULT_ID_ERROR

Info

[`UpdateResultId()`](#traceAnalysisAPI.Report.UpdateResultId "traceAnalysisAPI.Report.UpdateResultId (Python method) — Updates the result id for the current trace step.") can bee seen as equivalent to SetResultId(max(resultId, GetResultId()))

..example:

    report.UpdateResultId(report.RESULT_ID_SUCCESS)
    ...
    report.UpdateResultId(report.RESULT_ID_FAILED)
    ...
    report.UpdateResultId(report.RESULT_ID_SUCCESS)

    report.GetResultId() # this will result in report.RESULT_ID_FAILED

Parameters:  resultId : result id[¶](#traceAnalysisAPI.Report.UpdateResultId.resultId "Permalink to this definition")  
the result id to set

## SignalEvent[¶](#signalevent "Link to this heading")

*class* traceAnalysisAPI.SignalEvent[¶](#traceAnalysisAPI.SignalEvent "Link to this definition")  
A SignalEvent consists of a time stamp and multiple signal values. From the perspective of a `TraceStep` there is a constant stream of SignalEvent objects coming in, whose time stamps follow a strict partial order (that is, there are no duplicate time stamps).

GetSignal(*[name](#traceAnalysisAPI.SignalEvent.GetSignal.name "traceAnalysisAPI.SignalEvent.GetSignal.name (Python parameter) — the name of the desired signal"): str*) → [Signal](#traceAnalysisAPI.Signal "ttTraceCheckLib.signalEvent.Signal (Python class)") | None[¶](#traceAnalysisAPI.SignalEvent.GetSignal "Link to this definition")  
Returns the current signal (see [`Signal`](#traceAnalysisAPI.Signal "traceAnalysisAPI.Signal (Python class) — A Signal object encapsulates the measurement value of one signal at a given point of time.")) for a given signal name (see `TraceStep.DefineInSignals()`) if it is contained in this SignalEvent.

Parameters:  name : string[¶](#traceAnalysisAPI.SignalEvent.GetSignal.name "Permalink to this definition")  
the name of the desired signal

Return type:  [`Signal`](#traceAnalysisAPI.Signal "traceAnalysisAPI.Signal (Python class) — A Signal object encapsulates the measurement value of one signal at a given point of time.") or None

GetSignals() → dict[str, [Signal](#traceAnalysisAPI.Signal "ttTraceCheckLib.signalEvent.Signal (Python class)")][¶](#traceAnalysisAPI.SignalEvent.GetSignals "Link to this definition")  
Returns a dictionary mapping signal names (see `TraceStep.DefineInSignals()`) to signals (see [`Signal`](#traceAnalysisAPI.Signal "traceAnalysisAPI.Signal (Python class) — A Signal object encapsulates the measurement value of one signal at a given point of time."))

Return type:  dict(string -> [`Signal`](#traceAnalysisAPI.Signal "traceAnalysisAPI.Signal (Python class) — A Signal object encapsulates the measurement value of one signal at a given point of time."))

GetTime() → float[¶](#traceAnalysisAPI.SignalEvent.GetTime "Link to this definition")  
Returns the time stamp of the SignalEvent

Return type:  float

GetValue(*[name](#traceAnalysisAPI.SignalEvent.GetValue.name "traceAnalysisAPI.SignalEvent.GetValue.name (Python parameter) — the name of the desired signal"): str*) → float | dict[str, float | dict[str | None, float]] | None[¶](#traceAnalysisAPI.SignalEvent.GetValue "Link to this definition")  
Returns the current signal value (see [`Signal.GetValue()`](#traceAnalysisAPI.Signal.GetValue "traceAnalysisAPI.Signal.GetValue (Python method) — Returns the value of the signal.")) for a given signal name (see `TraceStep.DefineInSignals()`) if it is contained in this SignalEvent.

Parameters:  name : string[¶](#traceAnalysisAPI.SignalEvent.GetValue.name "Permalink to this definition")  
the name of the desired signal

Return type:  float/string or None

## Hold[¶](#hold "Link to this heading")

*class* traceAnalysisAPI.Hold[¶](#traceAnalysisAPI.Hold "Link to this definition")  
GetSignal(*[name](#traceAnalysisAPI.Hold.GetSignal.name "traceAnalysisAPI.Hold.GetSignal.name (Python parameter) — the name of the desired signal")*)[¶](#traceAnalysisAPI.Hold.GetSignal "Link to this definition")  
Returns the last known signal (see [`Signal`](#traceAnalysisAPI.Signal "traceAnalysisAPI.Signal (Python class) — A Signal object encapsulates the measurement value of one signal at a given point of time.")) for a given signal name (see `TraceStep.DefineInSignals()`) if it is contained in this SignalEvent.

Parameters:  name : str[¶](#traceAnalysisAPI.Hold.GetSignal.name "Permalink to this definition")  
the name of the desired signal

Return type:  [`Signal`](#traceAnalysisAPI.Signal "traceAnalysisAPI.Signal (Python class) — A Signal object encapsulates the measurement value of one signal at a given point of time.") or None

GetSignals()[¶](#traceAnalysisAPI.Hold.GetSignals "Link to this definition")  
Returns a dictionary mapping signal names (see `TraceStep.DefineInSignals()`) to the last known signals (see [`Signal`](#traceAnalysisAPI.Signal "traceAnalysisAPI.Signal (Python class) — A Signal object encapsulates the measurement value of one signal at a given point of time."))

Return type:  dict(str -> [`Signal`](#traceAnalysisAPI.Signal "traceAnalysisAPI.Signal (Python class) — A Signal object encapsulates the measurement value of one signal at a given point of time."))

GetValue(*[name](#traceAnalysisAPI.Hold.GetValue.name "traceAnalysisAPI.Hold.GetValue.name (Python parameter) — the name of the desired signal")*)[¶](#traceAnalysisAPI.Hold.GetValue "Link to this definition")  
Returns the last known signal value (see [`Signal.GetValue()`](#traceAnalysisAPI.Signal.GetValue "traceAnalysisAPI.Signal.GetValue (Python method) — Returns the value of the signal.")) for a given signal name (see `TraceStep.DefineInSignals()`).

Parameters:  name : str[¶](#traceAnalysisAPI.Hold.GetValue.name "Permalink to this definition")  
the name of the desired signal

Return type:  float or None

## Parameters[¶](#parameters "Link to this heading")

TraceStep.parameters = `{}`[¶](#traceAnalysisAPI.TraceStep.parameters "Link to this definition")  
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

GetPrevValue(*[restricted](#traceAnalysisAPI.Signal.GetPrevValue.restricted "traceAnalysisAPI.Signal.GetPrevValue.restricted (Python parameter) — if True only previous values within the current trigger range are returned, the parameter has only an effect at the beginning of a trigger range"): bool = `False`*) → object | None[¶](#traceAnalysisAPI.Signal.GetPrevValue "Link to this definition")  
Returns last known value of the signal before the current signal event.

Note

GetPrevValue() and GetValue() can return the same value,

if the signal has been measured with the same value twice in a row, which is not uncommon, especially for signals, that have been upsampled before trace analysis by means of value duplication

Parameters:  restricted : bool[¶](#traceAnalysisAPI.Signal.GetPrevValue.restricted "Permalink to this definition")  
if True only previous values within the current trigger range are returned, the parameter has only an effect at the beginning of a trigger range

Return type:  float or None

GetTime() → float | None[¶](#traceAnalysisAPI.Signal.GetTime "Link to this definition")  
Returns the timestamp of the [`SignalEvent`](#traceAnalysisAPI.SignalEvent "traceAnalysisAPI.SignalEvent (Python class) — A SignalEvent consists of a time stamp and multiple signal values. From the perspective of a TraceStep there is a constant stream of SignalEvent objects coming in, whose time stamps follow a strict partial order (that is, there are no duplicate time stamps).") from which the signal stems.

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

GetPath(*[idx](#traceAnalysisAPI.RecordingInfo.GetPath "traceAnalysisAPI.RecordingInfo.GetPath.idx (Python parameter)")=`0`*) → str | None[¶](#traceAnalysisAPI.RecordingInfo.GetPath "Link to this definition")  
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

GetStartTimeNs(*\**, *[synchronized](#traceAnalysisAPI.RecordingInfo.GetStartTimeNs.synchronized "traceAnalysisAPI.RecordingInfo.GetStartTimeNs.synchronized (Python parameter) — If True, the start time is adjusted by the deltaT if available."): bool = `True`*) → int | None[¶](#traceAnalysisAPI.RecordingInfo.GetStartTimeNs "Link to this definition")  
Returns the start time of the recording in nanoseconds since 1970-01-01T00:00:00Z.

This information is useful to calculate absolute timestamps, e.g.:

absoluteTimestampsInNs = int(relativeTimestampsInSeconds \* 1e9) + startTimeNs

If the traces have not been synchronized, the value of the parameter synchronized does not matter. If the traces have been sychronized, this method should normally be called with synchronized=True (default) so that the start time is adjusted to the deltaT and the adjusted start time can just be added to the synchronized timestamps to get the absolute timestamps. However, if you want to get the real start time without any adjustments, you should call this method with synchronized=False.

Parameters:  synchronized: bool = `True`[¶](#traceAnalysisAPI.RecordingInfo.GetStartTimeNs.synchronized "Permalink to this definition")  
If True, the start time is adjusted by the deltaT if available.

Returns:  start time in nanoseconds or None if the recording format does not support it

Raises:  
**ValueError** – if the start time cannot be determined (e.g., empty file or missing metadata)

## ReportTable[¶](#reporttable "Link to this heading")

*class* traceAnalysisAPI.ReportTable[¶](#traceAnalysisAPI.ReportTable "Link to this definition")  
A ReportTable object represents a table in the test report.

AddRow(*[values](#traceAnalysisAPI.ReportTable.AddRow.values "traceAnalysisAPI.ReportTable.AddRow.values (Python parameter) — iterable with the entries for each column of the new row"): Iterable[str]*, *[resultId](#traceAnalysisAPI.ReportTable.AddRow.resultId "traceAnalysisAPI.ReportTable.AddRow.resultId (Python parameter) — the result id of the row"): int | None = `None`*) → None[¶](#traceAnalysisAPI.ReportTable.AddRow "Link to this definition")  
Appends a row to the table.

Parameters:  values : iterable[¶](#traceAnalysisAPI.ReportTable.AddRow.values "Permalink to this definition")  
iterable with the entries for each column of the new row

resultId : result id or None[¶](#traceAnalysisAPI.ReportTable.AddRow.resultId "Permalink to this definition")  
the result id of the row

SetHeader(*[values](#traceAnalysisAPI.ReportTable.SetHeader.values "traceAnalysisAPI.ReportTable.SetHeader.values (Python parameter) — iterable with the entries for each column of the table header"): Iterable[str | int] | None*) → None[¶](#traceAnalysisAPI.ReportTable.SetHeader "Link to this definition")  
Sets the table header.

Parameters:  values : iterable[¶](#traceAnalysisAPI.ReportTable.SetHeader.values "Permalink to this definition")  
iterable with the entries for each column of the table header

## Range[¶](#range "Link to this heading")

*class* traceAnalysisAPI.Range[¶](#traceAnalysisAPI.Range "Link to this definition")  
Class representing a range in the test report. An instance of Range is returned by the call of [`Report.Range()`](#traceAnalysisAPI.Report.Range "traceAnalysisAPI.Report.Range (Python method) — Adds a range to the test report and returns a range object."). To specify the range in more detail, it is possible to add spots and sub ranges as children to a range object.

Range(*[startTime](#traceAnalysisAPI.Range.Range.startTime "traceAnalysisAPI.Range.Range.startTime (Python parameter) — timestamp at which the sub range begins")*, *[endTime](#traceAnalysisAPI.Range.Range.endTime "traceAnalysisAPI.Range.Range.endTime (Python parameter) — timestamp at which the sub range ends")*, *[message](#traceAnalysisAPI.Range.Range.message "traceAnalysisAPI.Range.Range.message (Python parameter) — a textual message describing the sub range")=`''`*, *[resultId](#traceAnalysisAPI.Range.Range.resultId "traceAnalysisAPI.Range.Range.resultId (Python parameter) — the verdict for the sub range")=`None`*, *[additionalInfo](#traceAnalysisAPI.Range.Range.additionalInfo "traceAnalysisAPI.Range.Range.additionalInfo (Python parameter) — a list of additional information, that will be shown in the custom result columns (see Report.AddResultColumn())")=`None`*)[¶](#traceAnalysisAPI.Range.Range "Link to this definition")  
Adds a sub range to the range.

Parameters:  startTime : float[¶](#traceAnalysisAPI.Range.Range.startTime "Permalink to this definition")  
timestamp at which the sub range begins

endTime : float[¶](#traceAnalysisAPI.Range.Range.endTime "Permalink to this definition")  
timestamp at which the sub range ends

message : string[¶](#traceAnalysisAPI.Range.Range.message "Permalink to this definition")  
a textual message describing the sub range

resultId : int[¶](#traceAnalysisAPI.Range.Range.resultId "Permalink to this definition")  
the verdict for the sub range

additionalInfo : list of strings[¶](#traceAnalysisAPI.Range.Range.additionalInfo "Permalink to this definition")  
a list of additional information, that will be shown in the custom result columns (see [`Report.AddResultColumn()`](#traceAnalysisAPI.Report.AddResultColumn "traceAnalysisAPI.Report.AddResultColumn (Python method) — Adds a new column with the given name to the result table. It is appended at the end of the table. Values can be inserted into this column by using the parameter "additionalInfo" of the methods Spot() and Range(). The entries in the list "additionalInfo" list are inserted into the additional result columns in sequence."))

Spot(*[time](#traceAnalysisAPI.Range.Spot.time "traceAnalysisAPI.Range.Spot.time (Python parameter) — timestamp of the spot")*, *[message](#traceAnalysisAPI.Range.Spot.message "traceAnalysisAPI.Range.Spot.message (Python parameter) — a textual message describing the spot")=`None`*, *[resultId](#traceAnalysisAPI.Range.Spot.resultId "traceAnalysisAPI.Range.Spot.resultId (Python parameter) — the verdict for the spot")=`None`*, *[additionalInfo](#traceAnalysisAPI.Range.Spot.additionalInfo "traceAnalysisAPI.Range.Spot.additionalInfo (Python parameter) — a list of additional information, that will be shown in the custom result columns (see Report.AddResultColumn())")=`None`*)[¶](#traceAnalysisAPI.Range.Spot "Link to this definition")  
Adds a signal spot to a range.

Parameters:  time : float[¶](#traceAnalysisAPI.Range.Spot.time "Permalink to this definition")  
timestamp of the spot

message : string[¶](#traceAnalysisAPI.Range.Spot.message "Permalink to this definition")  
a textual message describing the spot

resultId : int[¶](#traceAnalysisAPI.Range.Spot.resultId "Permalink to this definition")  
the verdict for the spot

additionalInfo : list of strings[¶](#traceAnalysisAPI.Range.Spot.additionalInfo "Permalink to this definition")  
a list of additional information, that will be shown in the custom result columns (see [`Report.AddResultColumn()`](#traceAnalysisAPI.Report.AddResultColumn "traceAnalysisAPI.Report.AddResultColumn (Python method) — Adds a new column with the given name to the result table. It is appended at the end of the table. Values can be inserted into this column by using the parameter "additionalInfo" of the methods Spot() and Range(). The entries in the list "additionalInfo" list are inserted into the additional result columns in sequence."))

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
