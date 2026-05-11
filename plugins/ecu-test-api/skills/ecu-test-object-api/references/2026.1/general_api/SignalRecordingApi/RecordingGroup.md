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

[ API for Signal Descriptions ](../SignalDescriptionApi.md)

[ API for Signal Recordings ](../SignalRecordingApi.md)

API for Signal Recordings

RecordingGroup [ RecordingGroup ](#)

RecordingGroup

- [C RecordingGroup ](#ApiClient.RecordingGroup)
  - [A RECORDING_MODE_AUTO ](#ApiClient.RecordingGroup.RECORDING_MODE_AUTO)
  - [A RECORDING_MODE_AUTO_RESTRICTED ](#ApiClient.RecordingGroup.RECORDING_MODE_AUTO_RESTRICTED)
  - [A RECORDING_MODE_MANUAL ](#ApiClient.RecordingGroup.RECORDING_MODE_MANUAL)
  - [A RECORDING_MODE_TRIGGER ](#ApiClient.RecordingGroup.RECORDING_MODE_TRIGGER)
  - [M AppendRecordingInfo ](#ApiClient.RecordingGroup.AppendRecordingInfo)
  - [M Clone ](#ApiClient.RecordingGroup.Clone)
  - [M GetConditionalSignalNamesForTraceAnalyses ](#ApiClient.RecordingGroup.GetConditionalSignalNamesForTraceAnalyses)
  - [M GetErrorOnEmptyStart ](#ApiClient.RecordingGroup.GetErrorOnEmptyStart)
  - [M GetErrorOnOnlyGenericSignals ](#ApiClient.RecordingGroup.GetErrorOnOnlyGenericSignals)
  - [M GetErrorOnOnlyUndefinedSystemIdentifiers ](#ApiClient.RecordingGroup.GetErrorOnOnlyUndefinedSystemIdentifiers)
  - [M GetFilenameTemplate ](#ApiClient.RecordingGroup.GetFilenameTemplate)
  - [M GetMandatorySignalNamesForTraceAnalyses ](#ApiClient.RecordingGroup.GetMandatorySignalNamesForTraceAnalyses)
  - [M GetName ](#ApiClient.RecordingGroup.GetName)
  - [M GetOptionalSignalNamesForTraceAnalyses ](#ApiClient.RecordingGroup.GetOptionalSignalNamesForTraceAnalyses)
  - [M GetPostStartTime ](#ApiClient.RecordingGroup.GetPostStartTime)
  - [M GetPostStopTime ](#ApiClient.RecordingGroup.GetPostStopTime)
  - [M GetPreTriggerTime ](#ApiClient.RecordingGroup.GetPreTriggerTime)
  - [M GetRecordingInfos ](#ApiClient.RecordingGroup.GetRecordingInfos)
  - [M GetRecordingMode ](#ApiClient.RecordingGroup.GetRecordingMode)
  - [M GetSignalGroup ](#ApiClient.RecordingGroup.GetSignalGroup)
  - [M GetStartTriggerCondition ](#ApiClient.RecordingGroup.GetStartTriggerCondition)
  - [M GetStopTriggerCondition ](#ApiClient.RecordingGroup.GetStopTriggerCondition)
  - [M RemoveRecordingInfo ](#ApiClient.RecordingGroup.RemoveRecordingInfo)
  - [M SetErrorOnEmptyStart ](#ApiClient.RecordingGroup.SetErrorOnEmptyStart)
  - [M SetErrorOnOnlyGenericSignals ](#ApiClient.RecordingGroup.SetErrorOnOnlyGenericSignals)
  - [M SetErrorOnOnlyUndefinedSystemIdentifiers ](#ApiClient.RecordingGroup.SetErrorOnOnlyUndefinedSystemIdentifiers)
  - [M SetFilenameTemplate ](#ApiClient.RecordingGroup.SetFilenameTemplate)
  - [M SetName ](#ApiClient.RecordingGroup.SetName)
  - [M SetPostStartTime ](#ApiClient.RecordingGroup.SetPostStartTime)
  - [M SetPostStopTime ](#ApiClient.RecordingGroup.SetPostStopTime)
  - [M SetPreTriggerTime ](#ApiClient.RecordingGroup.SetPreTriggerTime)
  - [M SetRecordingMode ](#ApiClient.RecordingGroup.SetRecordingMode)
  - [M SetStartTriggerCondition ](#ApiClient.RecordingGroup.SetStartTriggerCondition)
  - [M SetStopTriggerCondition ](#ApiClient.RecordingGroup.SetStopTriggerCondition)

[ RecordingInfo ](RecordingInfo.md)

[ SignalGroup ](SignalGroup.md)

[ SignalGroupBase ](SignalGroupBase.md)

[ VariableRecordingGroup ](VariableRecordingGroup.md)

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

RecordingGroup

- [C RecordingGroup ](#ApiClient.RecordingGroup)
  - [A RECORDING_MODE_AUTO ](#ApiClient.RecordingGroup.RECORDING_MODE_AUTO)
  - [A RECORDING_MODE_AUTO_RESTRICTED ](#ApiClient.RecordingGroup.RECORDING_MODE_AUTO_RESTRICTED)
  - [A RECORDING_MODE_MANUAL ](#ApiClient.RecordingGroup.RECORDING_MODE_MANUAL)
  - [A RECORDING_MODE_TRIGGER ](#ApiClient.RecordingGroup.RECORDING_MODE_TRIGGER)
  - [M AppendRecordingInfo ](#ApiClient.RecordingGroup.AppendRecordingInfo)
  - [M Clone ](#ApiClient.RecordingGroup.Clone)
  - [M GetConditionalSignalNamesForTraceAnalyses ](#ApiClient.RecordingGroup.GetConditionalSignalNamesForTraceAnalyses)
  - [M GetErrorOnEmptyStart ](#ApiClient.RecordingGroup.GetErrorOnEmptyStart)
  - [M GetErrorOnOnlyGenericSignals ](#ApiClient.RecordingGroup.GetErrorOnOnlyGenericSignals)
  - [M GetErrorOnOnlyUndefinedSystemIdentifiers ](#ApiClient.RecordingGroup.GetErrorOnOnlyUndefinedSystemIdentifiers)
  - [M GetFilenameTemplate ](#ApiClient.RecordingGroup.GetFilenameTemplate)
  - [M GetMandatorySignalNamesForTraceAnalyses ](#ApiClient.RecordingGroup.GetMandatorySignalNamesForTraceAnalyses)
  - [M GetName ](#ApiClient.RecordingGroup.GetName)
  - [M GetOptionalSignalNamesForTraceAnalyses ](#ApiClient.RecordingGroup.GetOptionalSignalNamesForTraceAnalyses)
  - [M GetPostStartTime ](#ApiClient.RecordingGroup.GetPostStartTime)
  - [M GetPostStopTime ](#ApiClient.RecordingGroup.GetPostStopTime)
  - [M GetPreTriggerTime ](#ApiClient.RecordingGroup.GetPreTriggerTime)
  - [M GetRecordingInfos ](#ApiClient.RecordingGroup.GetRecordingInfos)
  - [M GetRecordingMode ](#ApiClient.RecordingGroup.GetRecordingMode)
  - [M GetSignalGroup ](#ApiClient.RecordingGroup.GetSignalGroup)
  - [M GetStartTriggerCondition ](#ApiClient.RecordingGroup.GetStartTriggerCondition)
  - [M GetStopTriggerCondition ](#ApiClient.RecordingGroup.GetStopTriggerCondition)
  - [M RemoveRecordingInfo ](#ApiClient.RecordingGroup.RemoveRecordingInfo)
  - [M SetErrorOnEmptyStart ](#ApiClient.RecordingGroup.SetErrorOnEmptyStart)
  - [M SetErrorOnOnlyGenericSignals ](#ApiClient.RecordingGroup.SetErrorOnOnlyGenericSignals)
  - [M SetErrorOnOnlyUndefinedSystemIdentifiers ](#ApiClient.RecordingGroup.SetErrorOnOnlyUndefinedSystemIdentifiers)
  - [M SetFilenameTemplate ](#ApiClient.RecordingGroup.SetFilenameTemplate)
  - [M SetName ](#ApiClient.RecordingGroup.SetName)
  - [M SetPostStartTime ](#ApiClient.RecordingGroup.SetPostStartTime)
  - [M SetPostStopTime ](#ApiClient.RecordingGroup.SetPostStopTime)
  - [M SetPreTriggerTime ](#ApiClient.RecordingGroup.SetPreTriggerTime)
  - [M SetRecordingMode ](#ApiClient.RecordingGroup.SetRecordingMode)
  - [M SetStartTriggerCondition ](#ApiClient.RecordingGroup.SetStartTriggerCondition)
  - [M SetStopTriggerCondition ](#ApiClient.RecordingGroup.SetStopTriggerCondition)

# RecordingGroup[¶](#recordinggroup "Link to this heading")

*class* RecordingGroup[¶](#ApiClient.RecordingGroup "Link to this definition")  
Returned by

- [`SignalRecordingApi.CreateRecordingGroup`](../SignalRecordingApi.md#ApiClient.SignalRecordingApi.CreateRecordingGroup "ApiClient.SignalRecordingApi.CreateRecordingGroup (Python method) — Creates a new recording group. If no name is given, a name will be generated if the recording group is added to signal group.")

RECORDING_MODE_AUTO[¶](#ApiClient.RecordingGroup.RECORDING_MODE_AUTO "Link to this definition")  
Returns the constant used to specify the recording mode ‘Auto-Start/Stop: complete test case’.

Returns:  The constant

Return type:  int

RECORDING_MODE_AUTO_RESTRICTED[¶](#ApiClient.RecordingGroup.RECORDING_MODE_AUTO_RESTRICTED "Link to this definition")  
Returns the constant used to specify the recording mode ‘Auto-Start/Stop: without Pre-/Postcondition’.

Returns:  The constant

Return type:  int

RECORDING_MODE_MANUAL[¶](#ApiClient.RecordingGroup.RECORDING_MODE_MANUAL "Link to this definition")  
Returns the constant used to specify the recording mode ‘Manually’.

Returns:  The constant

Return type:  int

RECORDING_MODE_TRIGGER[¶](#ApiClient.RecordingGroup.RECORDING_MODE_TRIGGER "Link to this definition")  
Returns the constant used to specify the recording mode ‘Trigger-Start/Stop’.

Returns:  The constant

Return type:  int

AppendRecordingInfo(*[recordingInfo](#ApiClient.RecordingGroup.AppendRecordingInfo.recordingInfo "ApiClient.RecordingGroup.AppendRecordingInfo.recordingInfo (Python parameter) — The recording info to be added")*)[¶](#ApiClient.RecordingGroup.AppendRecordingInfo "Link to this definition")  
Adds a recording info to the recording group.

Parameters:  recordingInfo[¶](#ApiClient.RecordingGroup.AppendRecordingInfo.recordingInfo "Permalink to this definition")  
The recording info to be added

Clone()[¶](#ApiClient.RecordingGroup.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`RecordingGroup`](#ApiClient.RecordingGroup "ApiClient.RecordingGroup (Python class) — SignalRecordingApi.CreateRecordingGroup")

GetConditionalSignalNamesForTraceAnalyses()[¶](#ApiClient.RecordingGroup.GetConditionalSignalNamesForTraceAnalyses "Link to this definition")  
Returns the list of signal names that can be optional or mandatory for running the trace analyses depending on the values of global constants.

Returns:  The list of undetermined signal names.

Return type:  list[str]

GetErrorOnEmptyStart()[¶](#ApiClient.RecordingGroup.GetErrorOnEmptyStart "Link to this definition")  
Returns whether starting this recording group will lead to an error if it has no signals to record. This option is set by default.

Returns:  True if the start of the empty group will lead to an error, otherwise False.

Return type:  bool

GetErrorOnOnlyGenericSignals()[¶](#ApiClient.RecordingGroup.GetErrorOnOnlyGenericSignals "Link to this definition")  
Returns whether starting this recording group will lead to an error if it consists of only generic signals. This option is set by default.

Returns:  True if the start of group with mentioned characteristics will lead to an error, otherwise False.

Return type:  bool

GetErrorOnOnlyUndefinedSystemIdentifiers()[¶](#ApiClient.RecordingGroup.GetErrorOnOnlyUndefinedSystemIdentifiers "Link to this definition")  
Returns whether starting this recording group will lead to an error if the mapping targets of all signals of the group refer to an undefined system identifier. This option is set by default.

Returns:  True if the start of group with mentioned characteristics will lead to an error, otherwise False.

Return type:  bool

GetFilenameTemplate()[¶](#ApiClient.RecordingGroup.GetFilenameTemplate "Link to this definition")  
Returns the file name template of the recording group.

Returns:  The file name template of the recording group.

Return type:  str

GetMandatorySignalNamesForTraceAnalyses()[¶](#ApiClient.RecordingGroup.GetMandatorySignalNamesForTraceAnalyses "Link to this definition")  
Returns the list of signal names that are mandatory for running the trace analyses.

Returns:  The list of mandatory signal names.

Return type:  list[str]

GetName()[¶](#ApiClient.RecordingGroup.GetName "Link to this definition")  
Returns the name of a recording group.

Returns:  the name

Return type:  str

GetOptionalSignalNamesForTraceAnalyses()[¶](#ApiClient.RecordingGroup.GetOptionalSignalNamesForTraceAnalyses "Link to this definition")  
Returns the list of signal names that are optional for running the trace analyses.

Returns:  The list of optional signal names.

Return type:  list[str]

GetPostStartTime()[¶](#ApiClient.RecordingGroup.GetPostStartTime "Link to this definition")  
Returns the configured post start time for the start trigger of the recording.

Returns:  The post start time.

Return type:  float

GetPostStopTime()[¶](#ApiClient.RecordingGroup.GetPostStopTime "Link to this definition")  
Returns the configured post stop time for the stop trigger.

Returns:  The post stop time.

Return type:  float

GetPreTriggerTime()[¶](#ApiClient.RecordingGroup.GetPreTriggerTime "Link to this definition")  
Returns the configured pre trigger time of the start trigger of the recording.

Returns:  The pre trigger time.

Return type:  float

GetRecordingInfos()[¶](#ApiClient.RecordingGroup.GetRecordingInfos "Link to this definition")  
Returns the recording infos of the recording group.

Returns:  Recording infos

Return type:  list[[`RecordingInfo`](RecordingInfo.md#ApiClient.RecordingInfo "ApiClient.RecordingInfo (Python class) — SignalRecordingApi.CreateRecordingInfo")]

GetRecordingMode()[¶](#ApiClient.RecordingGroup.GetRecordingMode "Link to this definition")  
Returns the recording mode of the recording group as one of the following constants:

- [`RecordingGroup.RECORDING_MODE_MANUAL`](#ApiClient.RecordingGroup.RECORDING_MODE_MANUAL "ApiClient.RecordingGroup.RECORDING_MODE_MANUAL (Python attribute) — Returns the constant used to specify the recording mode 'Manually'.")

- [`RecordingGroup.RECORDING_MODE_AUTO_RESTRICTED`](#ApiClient.RecordingGroup.RECORDING_MODE_AUTO_RESTRICTED "ApiClient.RecordingGroup.RECORDING_MODE_AUTO_RESTRICTED (Python attribute) — Returns the constant used to specify the recording mode 'Auto-Start/Stop: without Pre-/Postcondition'.")

- [`RecordingGroup.RECORDING_MODE_AUTO`](#ApiClient.RecordingGroup.RECORDING_MODE_AUTO "ApiClient.RecordingGroup.RECORDING_MODE_AUTO (Python attribute) — Returns the constant used to specify the recording mode 'Auto-Start/Stop: complete test case'.")

- [`RecordingGroup.RECORDING_MODE_TRIGGER`](#ApiClient.RecordingGroup.RECORDING_MODE_TRIGGER "ApiClient.RecordingGroup.RECORDING_MODE_TRIGGER (Python attribute) — Returns the constant used to specify the recording mode 'Trigger-Start/Stop'.")

Returns:  The recording mode constant

Return type:  int

GetSignalGroup()[¶](#ApiClient.RecordingGroup.GetSignalGroup "Link to this definition")  
Returns the parent signal group.

Returns:  The parent signal group

Return type:  [`SignalGroupBase`](SignalGroupBase.md#ApiClient.SignalGroupBase "ApiClient.SignalGroupBase (Python class) — API to access signal groups. Signals of a signal group are represented by references to mapping items.")

GetStartTriggerCondition()[¶](#ApiClient.RecordingGroup.GetStartTriggerCondition "Link to this definition")  
Returns the start trigger condition.

Returns:  The start trigger condition

Return type:  str

GetStopTriggerCondition()[¶](#ApiClient.RecordingGroup.GetStopTriggerCondition "Link to this definition")  
Returns the stop trigger condition.

Returns:  The stop trigger condition

Return type:  str

RemoveRecordingInfo(*[recordingInfo](#ApiClient.RecordingGroup.RemoveRecordingInfo.recordingInfo "ApiClient.RecordingGroup.RemoveRecordingInfo.recordingInfo (Python parameter) — The recording info to be removed")*)[¶](#ApiClient.RecordingGroup.RemoveRecordingInfo "Link to this definition")  
Removes a recording info from the recording group.

Parameters:  recordingInfo[¶](#ApiClient.RecordingGroup.RemoveRecordingInfo.recordingInfo "Permalink to this definition")  
The recording info to be removed

Raises:  
ApiError: When recording info is not part of recording group

SetErrorOnEmptyStart(*[value](#ApiClient.RecordingGroup.SetErrorOnEmptyStart.value "ApiClient.RecordingGroup.SetErrorOnEmptyStart.value (Python parameter) — True if the start of the empty group shall lead to an error, otherwise False.")*)[¶](#ApiClient.RecordingGroup.SetErrorOnEmptyStart "Link to this definition")  
Sets whether starting this recording group will lead to an error if it has no signals to record.

Parameters:  value : bool[¶](#ApiClient.RecordingGroup.SetErrorOnEmptyStart.value "Permalink to this definition")  
True if the start of the empty group shall lead to an error, otherwise False.

SetErrorOnOnlyGenericSignals(*[value](#ApiClient.RecordingGroup.SetErrorOnOnlyGenericSignals.value "ApiClient.RecordingGroup.SetErrorOnOnlyGenericSignals.value (Python parameter) — True if the start of group with mentioned characteristics shall lead to an error, otherwise False.")*)[¶](#ApiClient.RecordingGroup.SetErrorOnOnlyGenericSignals "Link to this definition")  
Sets whether starting this recording group will lead to an error if it consists of only generic signals.

Parameters:  value : bool[¶](#ApiClient.RecordingGroup.SetErrorOnOnlyGenericSignals.value "Permalink to this definition")  
True if the start of group with mentioned characteristics shall lead to an error, otherwise False.

SetErrorOnOnlyUndefinedSystemIdentifiers(*[value](#ApiClient.RecordingGroup.SetErrorOnOnlyUndefinedSystemIdentifiers.value "ApiClient.RecordingGroup.SetErrorOnOnlyUndefinedSystemIdentifiers.value (Python parameter) — True if the start of group with mentioned characteristics shall lead to an error, otherwise False.")*)[¶](#ApiClient.RecordingGroup.SetErrorOnOnlyUndefinedSystemIdentifiers "Link to this definition")  
Sets whether starting this recording group will lead to an error if the mapping targets of all signals of the group refer to an undefined system identifier.

Parameters:  value : bool[¶](#ApiClient.RecordingGroup.SetErrorOnOnlyUndefinedSystemIdentifiers.value "Permalink to this definition")  
True if the start of group with mentioned characteristics shall lead to an error, otherwise False.

SetFilenameTemplate(*[template](#ApiClient.RecordingGroup.SetFilenameTemplate.template "ApiClient.RecordingGroup.SetFilenameTemplate.template (Python parameter) — The new file name template of the recording group.")*)[¶](#ApiClient.RecordingGroup.SetFilenameTemplate "Link to this definition")  
Sets the file name template of the recording group.

Parameters:  template : str[¶](#ApiClient.RecordingGroup.SetFilenameTemplate.template "Permalink to this definition")  
The new file name template of the recording group.

SetName(*[name](#ApiClient.RecordingGroup.SetName.name "ApiClient.RecordingGroup.SetName.name (Python parameter) — The new name")*)[¶](#ApiClient.RecordingGroup.SetName "Link to this definition")  
Sets the name of the recording group.

Parameters:  name : str[¶](#ApiClient.RecordingGroup.SetName.name "Permalink to this definition")  
The new name

SetPostStartTime(*[time](#ApiClient.RecordingGroup.SetPostStartTime.time "ApiClient.RecordingGroup.SetPostStartTime.time (Python parameter) — The post start time in seconds.")*)[¶](#ApiClient.RecordingGroup.SetPostStartTime "Link to this definition")  
Sets the post start time of the start trigger of the recording.

Parameters:  time : float[¶](#ApiClient.RecordingGroup.SetPostStartTime.time "Permalink to this definition")  
The post start time in seconds.

SetPostStopTime(*[time](#ApiClient.RecordingGroup.SetPostStopTime.time "ApiClient.RecordingGroup.SetPostStopTime.time (Python parameter) — The post stop time in seconds.")*)[¶](#ApiClient.RecordingGroup.SetPostStopTime "Link to this definition")  
Sets the post stop time of the stop trigger.

Parameters:  time : float[¶](#ApiClient.RecordingGroup.SetPostStopTime.time "Permalink to this definition")  
The post stop time in seconds.

SetPreTriggerTime(*[time](#ApiClient.RecordingGroup.SetPreTriggerTime.time "ApiClient.RecordingGroup.SetPreTriggerTime.time (Python parameter) — The pre trigger time in seconds.")*)[¶](#ApiClient.RecordingGroup.SetPreTriggerTime "Link to this definition")  
Sets the pre trigger time for the start trigger of the recording.

Parameters:  time : float[¶](#ApiClient.RecordingGroup.SetPreTriggerTime.time "Permalink to this definition")  
The pre trigger time in seconds.

SetRecordingMode(*[value](#ApiClient.RecordingGroup.SetRecordingMode.value "ApiClient.RecordingGroup.SetRecordingMode.value (Python parameter) — The recording mode constant")*)[¶](#ApiClient.RecordingGroup.SetRecordingMode "Link to this definition")  
Sets the recording mode of the recording group to one of the following constants:

- [`RecordingGroup.RECORDING_MODE_MANUAL`](#ApiClient.RecordingGroup.RECORDING_MODE_MANUAL "ApiClient.RecordingGroup.RECORDING_MODE_MANUAL (Python attribute) — Returns the constant used to specify the recording mode 'Manually'.")

- [`RecordingGroup.RECORDING_MODE_AUTO_RESTRICTED`](#ApiClient.RecordingGroup.RECORDING_MODE_AUTO_RESTRICTED "ApiClient.RecordingGroup.RECORDING_MODE_AUTO_RESTRICTED (Python attribute) — Returns the constant used to specify the recording mode 'Auto-Start/Stop: without Pre-/Postcondition'.")

- [`RecordingGroup.RECORDING_MODE_AUTO`](#ApiClient.RecordingGroup.RECORDING_MODE_AUTO "ApiClient.RecordingGroup.RECORDING_MODE_AUTO (Python attribute) — Returns the constant used to specify the recording mode 'Auto-Start/Stop: complete test case'.")

- [`RecordingGroup.RECORDING_MODE_TRIGGER`](#ApiClient.RecordingGroup.RECORDING_MODE_TRIGGER "ApiClient.RecordingGroup.RECORDING_MODE_TRIGGER (Python attribute) — Returns the constant used to specify the recording mode 'Trigger-Start/Stop'.")

Parameters:  value : int[¶](#ApiClient.RecordingGroup.SetRecordingMode.value "Permalink to this definition")  
The recording mode constant

SetStartTriggerCondition(*[condition](#ApiClient.RecordingGroup.SetStartTriggerCondition.condition "ApiClient.RecordingGroup.SetStartTriggerCondition.condition (Python parameter) — The start trigger condition.")*)[¶](#ApiClient.RecordingGroup.SetStartTriggerCondition "Link to this definition")  
Sets the start trigger condition.

Parameters:  condition : str[¶](#ApiClient.RecordingGroup.SetStartTriggerCondition.condition "Permalink to this definition")  
The start trigger condition.

SetStopTriggerCondition(*[condition](#ApiClient.RecordingGroup.SetStopTriggerCondition.condition "ApiClient.RecordingGroup.SetStopTriggerCondition.condition (Python parameter) — The stop trigger condition.")*)[¶](#ApiClient.RecordingGroup.SetStopTriggerCondition "Link to this definition")  
Sets the stop trigger condition.

Parameters:  condition : str[¶](#ApiClient.RecordingGroup.SetStopTriggerCondition.condition "Permalink to this definition")  
The stop trigger condition.

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
