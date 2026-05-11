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

[ RecordingGroup ](RecordingGroup.md)

[ RecordingInfo ](RecordingInfo.md)

[ SignalGroup ](SignalGroup.md)

[ SignalGroupBase ](SignalGroupBase.md)

VariableRecordingGroup [ VariableRecordingGroup ](#)

VariableRecordingGroup

- [C VariableRecordingGroup ](#ApiClient.VariableRecordingGroup)
  - [A RECORDING_MODE_AUTO ](#ApiClient.VariableRecordingGroup.RECORDING_MODE_AUTO)
  - [A RECORDING_MODE_AUTO_RESTRICTED ](#ApiClient.VariableRecordingGroup.RECORDING_MODE_AUTO_RESTRICTED)
  - [A RECORDING_MODE_MANUAL ](#ApiClient.VariableRecordingGroup.RECORDING_MODE_MANUAL)
  - [A RECORDING_MODE_TRIGGER ](#ApiClient.VariableRecordingGroup.RECORDING_MODE_TRIGGER)
  - [M AppendRecordingInfo ](#ApiClient.VariableRecordingGroup.AppendRecordingInfo)
  - [M Clone ](#ApiClient.VariableRecordingGroup.Clone)
  - [M GetConditionalSignalNamesForTraceAnalyses ](#ApiClient.VariableRecordingGroup.GetConditionalSignalNamesForTraceAnalyses)
  - [M GetFilenameTemplate ](#ApiClient.VariableRecordingGroup.GetFilenameTemplate)
  - [M GetMandatorySignalNamesForTraceAnalyses ](#ApiClient.VariableRecordingGroup.GetMandatorySignalNamesForTraceAnalyses)
  - [M GetName ](#ApiClient.VariableRecordingGroup.GetName)
  - [M GetOptionalSignalNamesForTraceAnalyses ](#ApiClient.VariableRecordingGroup.GetOptionalSignalNamesForTraceAnalyses)
  - [M GetRecordingInfos ](#ApiClient.VariableRecordingGroup.GetRecordingInfos)
  - [M GetRecordingMode ](#ApiClient.VariableRecordingGroup.GetRecordingMode)
  - [M RemoveRecordingInfo ](#ApiClient.VariableRecordingGroup.RemoveRecordingInfo)
  - [M SetRecordingMode ](#ApiClient.VariableRecordingGroup.SetRecordingMode)

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

VariableRecordingGroup

- [C VariableRecordingGroup ](#ApiClient.VariableRecordingGroup)
  - [A RECORDING_MODE_AUTO ](#ApiClient.VariableRecordingGroup.RECORDING_MODE_AUTO)
  - [A RECORDING_MODE_AUTO_RESTRICTED ](#ApiClient.VariableRecordingGroup.RECORDING_MODE_AUTO_RESTRICTED)
  - [A RECORDING_MODE_MANUAL ](#ApiClient.VariableRecordingGroup.RECORDING_MODE_MANUAL)
  - [A RECORDING_MODE_TRIGGER ](#ApiClient.VariableRecordingGroup.RECORDING_MODE_TRIGGER)
  - [M AppendRecordingInfo ](#ApiClient.VariableRecordingGroup.AppendRecordingInfo)
  - [M Clone ](#ApiClient.VariableRecordingGroup.Clone)
  - [M GetConditionalSignalNamesForTraceAnalyses ](#ApiClient.VariableRecordingGroup.GetConditionalSignalNamesForTraceAnalyses)
  - [M GetFilenameTemplate ](#ApiClient.VariableRecordingGroup.GetFilenameTemplate)
  - [M GetMandatorySignalNamesForTraceAnalyses ](#ApiClient.VariableRecordingGroup.GetMandatorySignalNamesForTraceAnalyses)
  - [M GetName ](#ApiClient.VariableRecordingGroup.GetName)
  - [M GetOptionalSignalNamesForTraceAnalyses ](#ApiClient.VariableRecordingGroup.GetOptionalSignalNamesForTraceAnalyses)
  - [M GetRecordingInfos ](#ApiClient.VariableRecordingGroup.GetRecordingInfos)
  - [M GetRecordingMode ](#ApiClient.VariableRecordingGroup.GetRecordingMode)
  - [M RemoveRecordingInfo ](#ApiClient.VariableRecordingGroup.RemoveRecordingInfo)
  - [M SetRecordingMode ](#ApiClient.VariableRecordingGroup.SetRecordingMode)

# VariableRecordingGroup[¶](#variablerecordinggroup "Link to this heading")

*class* VariableRecordingGroup[¶](#ApiClient.VariableRecordingGroup "Link to this definition")  
RECORDING_MODE_AUTO[¶](#ApiClient.VariableRecordingGroup.RECORDING_MODE_AUTO "Link to this definition")  
Returns the constant used to specify the recording mode ‘Auto-Start/Stop: complete test case’.

Returns:  The constant

Return type:  int

RECORDING_MODE_AUTO_RESTRICTED[¶](#ApiClient.VariableRecordingGroup.RECORDING_MODE_AUTO_RESTRICTED "Link to this definition")  
Returns the constant used to specify the recording mode ‘Auto-Start/Stop: without Pre-/Postcondition’.

Returns:  The constant

Return type:  int

RECORDING_MODE_MANUAL[¶](#ApiClient.VariableRecordingGroup.RECORDING_MODE_MANUAL "Link to this definition")  
Returns the constant used to specify the recording mode ‘Manually’.

Returns:  The constant

Return type:  int

RECORDING_MODE_TRIGGER[¶](#ApiClient.VariableRecordingGroup.RECORDING_MODE_TRIGGER "Link to this definition")  
Returns the constant used to specify the recording mode ‘Trigger-Start/Stop’.

Returns:  The constant

Return type:  int

AppendRecordingInfo(*[recordingInfo](#ApiClient.VariableRecordingGroup.AppendRecordingInfo.recordingInfo "ApiClient.VariableRecordingGroup.AppendRecordingInfo.recordingInfo (Python parameter) — The recording info to be added")*)[¶](#ApiClient.VariableRecordingGroup.AppendRecordingInfo "Link to this definition")  
Adds a recording info to the recording group.

Parameters:  recordingInfo[¶](#ApiClient.VariableRecordingGroup.AppendRecordingInfo.recordingInfo "Permalink to this definition")  
The recording info to be added

Clone()[¶](#ApiClient.VariableRecordingGroup.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`VariableRecordingGroup`](#ApiClient.VariableRecordingGroup "ApiClient.VariableRecordingGroup (Python class) — Returns the constant used to specify the recording mode 'Auto-Start/Stop: complete test case'.")

GetConditionalSignalNamesForTraceAnalyses()[¶](#ApiClient.VariableRecordingGroup.GetConditionalSignalNamesForTraceAnalyses "Link to this definition")  
Returns the list of signal names that can be optional or mandatory for running the trace analyses depending on the values of global constants.

Returns:  The list of undetermined signal names.

Return type:  list[str]

GetFilenameTemplate()[¶](#ApiClient.VariableRecordingGroup.GetFilenameTemplate "Link to this definition")  
Returns the file name template of the recording group.

Returns:  The file name template of the recording group.

Return type:  str

GetMandatorySignalNamesForTraceAnalyses()[¶](#ApiClient.VariableRecordingGroup.GetMandatorySignalNamesForTraceAnalyses "Link to this definition")  
Returns the list of signal names that are mandatory for running the trace analyses.

Returns:  The list of mandatory signal names.

Return type:  list[str]

GetName()[¶](#ApiClient.VariableRecordingGroup.GetName "Link to this definition")  
Returns the name of a recording group.

Returns:  the name

Return type:  str

GetOptionalSignalNamesForTraceAnalyses()[¶](#ApiClient.VariableRecordingGroup.GetOptionalSignalNamesForTraceAnalyses "Link to this definition")  
Returns the list of signal names that are optional for running the trace analyses.

Returns:  The list of optional signal names.

Return type:  list[str]

GetRecordingInfos()[¶](#ApiClient.VariableRecordingGroup.GetRecordingInfos "Link to this definition")  
Returns the recording infos of the recording group.

Returns:  Recording infos

Return type:  list[[`RecordingInfo`](RecordingInfo.md#ApiClient.RecordingInfo "ApiClient.RecordingInfo (Python class) — SignalRecordingApi.CreateRecordingInfo")]

GetRecordingMode()[¶](#ApiClient.VariableRecordingGroup.GetRecordingMode "Link to this definition")  
Returns the recording mode of the recording group as one of the following constants:

- [`RecordingGroup.RECORDING_MODE_MANUAL`](RecordingGroup.md#ApiClient.RecordingGroup.RECORDING_MODE_MANUAL "ApiClient.RecordingGroup.RECORDING_MODE_MANUAL (Python attribute) — Returns the constant used to specify the recording mode 'Manually'.")

- [`RecordingGroup.RECORDING_MODE_AUTO_RESTRICTED`](RecordingGroup.md#ApiClient.RecordingGroup.RECORDING_MODE_AUTO_RESTRICTED "ApiClient.RecordingGroup.RECORDING_MODE_AUTO_RESTRICTED (Python attribute) — Returns the constant used to specify the recording mode 'Auto-Start/Stop: without Pre-/Postcondition'.")

- [`RecordingGroup.RECORDING_MODE_AUTO`](RecordingGroup.md#ApiClient.RecordingGroup.RECORDING_MODE_AUTO "ApiClient.RecordingGroup.RECORDING_MODE_AUTO (Python attribute) — Returns the constant used to specify the recording mode 'Auto-Start/Stop: complete test case'.")

- [`RecordingGroup.RECORDING_MODE_TRIGGER`](RecordingGroup.md#ApiClient.RecordingGroup.RECORDING_MODE_TRIGGER "ApiClient.RecordingGroup.RECORDING_MODE_TRIGGER (Python attribute) — Returns the constant used to specify the recording mode 'Trigger-Start/Stop'.")

Returns:  The recording mode constant

Return type:  int

RemoveRecordingInfo(*[recordingInfo](#ApiClient.VariableRecordingGroup.RemoveRecordingInfo.recordingInfo "ApiClient.VariableRecordingGroup.RemoveRecordingInfo.recordingInfo (Python parameter) — The recording info to be removed")*)[¶](#ApiClient.VariableRecordingGroup.RemoveRecordingInfo "Link to this definition")  
Removes a recording info from the recording group.

Parameters:  recordingInfo[¶](#ApiClient.VariableRecordingGroup.RemoveRecordingInfo.recordingInfo "Permalink to this definition")  
The recording info to be removed

Raises:  
ApiError: When recording info is not part of recording group

SetRecordingMode(*[value](#ApiClient.VariableRecordingGroup.SetRecordingMode.value "ApiClient.VariableRecordingGroup.SetRecordingMode.value (Python parameter) — The recording mode constant")*)[¶](#ApiClient.VariableRecordingGroup.SetRecordingMode "Link to this definition")  
Sets the recording mode of the recording group to one of the following constants:

- [`RecordingGroup.RECORDING_MODE_MANUAL`](RecordingGroup.md#ApiClient.RecordingGroup.RECORDING_MODE_MANUAL "ApiClient.RecordingGroup.RECORDING_MODE_MANUAL (Python attribute) — Returns the constant used to specify the recording mode 'Manually'.")

- [`RecordingGroup.RECORDING_MODE_AUTO_RESTRICTED`](RecordingGroup.md#ApiClient.RecordingGroup.RECORDING_MODE_AUTO_RESTRICTED "ApiClient.RecordingGroup.RECORDING_MODE_AUTO_RESTRICTED (Python attribute) — Returns the constant used to specify the recording mode 'Auto-Start/Stop: without Pre-/Postcondition'.")

- [`RecordingGroup.RECORDING_MODE_AUTO`](RecordingGroup.md#ApiClient.RecordingGroup.RECORDING_MODE_AUTO "ApiClient.RecordingGroup.RECORDING_MODE_AUTO (Python attribute) — Returns the constant used to specify the recording mode 'Auto-Start/Stop: complete test case'.")

- [`RecordingGroup.RECORDING_MODE_TRIGGER`](RecordingGroup.md#ApiClient.RecordingGroup.RECORDING_MODE_TRIGGER "ApiClient.RecordingGroup.RECORDING_MODE_TRIGGER (Python attribute) — Returns the constant used to specify the recording mode 'Trigger-Start/Stop'.")

Parameters:  value : int[¶](#ApiClient.VariableRecordingGroup.SetRecordingMode.value "Permalink to this definition")  
The recording mode constant

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
