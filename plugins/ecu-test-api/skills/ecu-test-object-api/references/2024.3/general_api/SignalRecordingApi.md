# API for Signal Recordings[¶](#api-for-signal-recordings "Link to this heading")

Part of the [Object based program API](objectApi.md#objectapi)

## SignalRecordingApi[¶](#signalrecordingapi "Link to this heading")

*class* SignalRecordingApi[¶](#ApiClient.SignalRecordingApi "Link to this definition")  
Returned by

- [`PackageApi.SignalRecordingApi`](PackageApi.md#ApiClient.PackageApi.SignalRecordingApi "ApiClient.PackageApi.SignalRecordingApi")

CreateFormatDetailsStringASC(*medium='AUTO'*, *channel='ALL'*, *direction='RxTx'*)[¶](#ApiClient.SignalRecordingApi.CreateFormatDetailsStringASC "Link to this definition")  
Creates the format details string for ASC files. The information are needed to filter the medium, a specific channel and the direction.

Parameters:  - **medium** (*str*) –

  The medium to be read: “AUTO” (default), “CAN”, “CANFD”, “FlexRay” or “LIN”.

  If medium is “AUTO” the parser tries to guess the medium by reading the header of the ASC file. Only frames of the guessed medium will be read.

- **channel** (*str*) –

  The channel(s) to read. Possible values: “ALL” or “01” up to “99”.

  For medium “FlexRay” values are typically: “ALL”, “01” or “02”.

  For medium “LIN” values are “ALL” or “1” up to “64”

- **direction** (*str*) – The communication direction: “Rx”, “Tx” or “RxTx”.

Returns:  The newly created format details string.

Return type:  str

CreateFormatDetailsStringBLF(*medium='AUTO'*, *channel='ALL'*, *direction='RxTx'*, *port='30490'*)[¶](#ApiClient.SignalRecordingApi.CreateFormatDetailsStringBLF "Link to this definition")  
Creates the format details string for BLF files. The information are needed to filter the medium, a specific channel, the direction and the Ethernet port (if necessary).

Parameters:  - **medium** (*str*) – The medium to be read: “AUTO” (default), “CAN”, “FlexRay”, or “Ethernet”.

- **channel** (*str*) –

  The channel(s) to read. Possible values: “ALL” or “01” up to “99”.

  For medium “FlexRay” values are typically: “ALL”, “01” or “02”.

- **direction** (*str*) – The communication direction: “Rx”, “Tx” or “RxTx”.

- **port** (*str*) – The Ethernet port for reading Ethernet signals. Only used if medium is ‘Ethernet’.

Returns:  The newly created format details string.

Return type:  str

CreateFormatDetailsStringCSV(*columnSeparator=';'*, *decimalSeparator='.'*, *thousandSeparator=','*, *headLineNumber=0*, *timeColumn=0*)[¶](#ApiClient.SignalRecordingApi.CreateFormatDetailsStringCSV "Link to this definition")  
Creates a format string for CSV files.

Parameters:  - **columnSeparator** (*str*) – The column separator.

- **decimalSeparator** (*str*) – The decimal separator.

- **thousandSeparator** (*str*) – The thousand separator.

- **headLineNumber** (*int*) – The line number of the header with signal names.

- **timeColumn** (*int*) – The column number of the time column.

Returns:  The newly created format details string.

Return type:  str

CreateFormatDetailsStringMatControlDesk(*platformToModelNames*)[¶](#ApiClient.SignalRecordingApi.CreateFormatDetailsStringMatControlDesk "Link to this definition")  
Creates the format details string for MAT files created by ControlDeskNG. The devices in the file are named like the platforms defined in ControlDeskNG. To address signals via model values a dictionary with a mapping of platform names to your model names (in ecu.test) can be specified.

Parameters:  **platformToModelNames** (*dict[string,* *string]*) – Mapping of platform names to model names (in ecu.test).

Returns:  The newly created format details string.

Return type:  str

CreateFormatDetailsStringMdf4ControlDesk(*platformToModelNames*)[¶](#ApiClient.SignalRecordingApi.CreateFormatDetailsStringMdf4ControlDesk "Link to this definition")  
Creates the format details string for MDF4 files created by ControlDeskNG. The devices in the file are named like the platforms defined in ControlDeskNG. To address signals via model values a dictionary with a mapping of platform names to your model names (in ecu.test) can be specified.

Parameters:  **platformToModelNames** (*dict[string,* *string]*) – Mapping of platform names to model names (in ecu.test).

Returns:  The newly created format details string.

Return type:  str

CreateFormatDetailsStringMdfControlDesk(*platformToModelNames*)[¶](#ApiClient.SignalRecordingApi.CreateFormatDetailsStringMdfControlDesk "Link to this definition")  
Creates the format details string for MDF files created by ControlDesk. The devices in the file are named like the platforms defined in ControlDesk. To address signals via model values a dictionary with a mapping of platform names to your model names (in ecu.test) can be specified.

Parameters:  **platformToModelNames** (*dict[string,* *string]*) – Mapping of platform names to model names (in ecu.test).

Returns:  The newly created format details string.

Return type:  str

CreateFormatDetailsStringPcap(*port='30490'*)[¶](#ApiClient.SignalRecordingApi.CreateFormatDetailsStringPcap "Link to this definition")  
Creates the format details string for PCAP files. The information is needed to filter the Ethernet port.

Parameters:  **port** (*str*) – The Ethernet port for reading Ethernet signals.

Returns:  The newly created format details string.

Return type:  str

CreateFormatDetailsStringSTI(*sampleRate=50.0*)[¶](#ApiClient.SignalRecordingApi.CreateFormatDetailsStringSTI "Link to this definition")  
Creates the format details string for STI files. The information simple provides the sample rate to generate concrete samples.

Parameters:  **sampleRate** (*float*) – The sample rate. Default is 50.0.

Returns:  The newly created format details string.

Return type:  str

CreateFormatDetailsStringTTL(*medium='CAN'*, *channel='01'*, *direction='RxTx'*, *captureDevice='ANY'*, *port='30490'*, *tap='0'*)[¶](#ApiClient.SignalRecordingApi.CreateFormatDetailsStringTTL "Link to this definition")  
Creates the format details string for TTL files.

The information are needed to filter the medium, a specific channel and the direction. Please note that the recording name (“Analog”, “CAN”, “Flexray”) must be specified for the recording info, too.

Parameters:  - **medium** (*str*) – The medium to be read: “CAN” (default), “Flexray” or “LIN”.

- **channel** (*str*) –

  The channel(s) to read. Possible values if “CAN” should be read: “01” up to “24”.

  If “LIN” possible values are: “01” up to “12”.

  If “Flexray” possible values are: “1A”, “1B”, “1AB”, … ,”3AB”.

- **direction** (*str*) – The communication direction: “Rx”, “Tx” or “RxTx”.

- **captureDevice** (*str*) – Possible values are “ANY” (default), “FPGA” and “Tricore”.

- **port** (*str*) – Only for Ethernet: The port of the SOME/IP Service-Discovery (default: 30490)

- **tap** (*str*) – Only for Ethernet: The number of the TAP Extension board (1-7). 0 for the main logger.

Returns:  The newly created format details string.

Return type:  str

CreateRecordingGroup(*name=''*, *description=''*)[¶](#ApiClient.SignalRecordingApi.CreateRecordingGroup "Link to this definition")  
Creates a new recording group. If no name is given, a name will be generated if the recording group is added to signal group.

Parameters:  - **name** (*str*) – The name of the recording group. The name must be unique for all recording groups in a package!

- **description** (*str*) – **Deprecated**: description for the signal group

Returns:  The newly created recording group

Return type:  [`RecordingGroup`](#ApiClient.RecordingGroup "ApiClient.RecordingGroup")

CreateRecordingInfo(*path*, *recordingName=''*, *formatDetailsString=None*, *recordingNumber=0*, *startTime=None*, *stopTime=None*)[¶](#ApiClient.SignalRecordingApi.CreateRecordingInfo "Link to this definition")  
Creates a recording info.

Parameters:  - **path** (*str*) – Path to the recording.

- **recordingName** (*str*) – Optional: The recording name in the file (mostly the device name).

- **formatDetailsString** (*str*) –

  Optional: The format details string with information to read the file. If the file exists it will be checked whether the given format details string is supported.

  See also: CreateFormatDetailsStringXYZ().

- **recordingNumber** (*int*) – Optional: Number of the recording.

- **startTime** (*float*) – Optional: First time stamp to be read in from the recording.

- **stopTime** (*float*) – Optional: Last time stamp to be read in from the recording.

Returns:  The newly created recording info.

Return type:  [`RecordingInfo`](#ApiClient.RecordingInfo "ApiClient.RecordingInfo")

CreateSignalGroup(*name=''*, *description=''*)[¶](#ApiClient.SignalRecordingApi.CreateSignalGroup "Link to this definition")  
Creates a new signal group. If no name is given, a name will be generated if the signal group is added to a package.

Parameters:  - **name** (*str*) – The name of the signal group. The name must be unique for all signal groups in a package!

- **description** (*str*) – Description for the signal group

Returns:  The newly created signal group.

Return type:  [`SignalGroup`](#ApiClient.SignalGroup "ApiClient.SignalGroup")

## RecordingGroup[¶](#recordinggroup "Link to this heading")

*class* RecordingGroup[¶](#ApiClient.RecordingGroup "Link to this definition")  
Base class

[`RecordingGroupBase`](TraceAnalysisApi.md#ApiClient.RecordingGroupBase "ApiClient.RecordingGroupBase")

Returned by

- [`AutosarTimeSynchronization.GetMaster`](TraceAnalysisApi.md#ApiClient.AutosarTimeSynchronization.GetMaster "ApiClient.AutosarTimeSynchronization.GetMaster")

- [`CrossCorrelationSynchronization.GetMaster`](TraceAnalysisApi.md#ApiClient.CrossCorrelationSynchronization.GetMaster "ApiClient.CrossCorrelationSynchronization.GetMaster")

- [`EqualnessMatchingSynchronization.GetMaster`](TraceAnalysisApi.md#ApiClient.EqualnessMatchingSynchronization.GetMaster "ApiClient.EqualnessMatchingSynchronization.GetMaster")

- [`ExpectationSynchronization.GetMaster`](TraceAnalysisApi.md#ApiClient.ExpectationSynchronization.GetMaster "ApiClient.ExpectationSynchronization.GetMaster")

- [`LeastSquaresSynchronization.GetMaster`](TraceAnalysisApi.md#ApiClient.LeastSquaresSynchronization.GetMaster "ApiClient.LeastSquaresSynchronization.GetMaster")

- [`OffsetSynchronization.GetMaster`](TraceAnalysisApi.md#ApiClient.OffsetSynchronization.GetMaster "ApiClient.OffsetSynchronization.GetMaster")

- [`SignalGroup.GetRecordingGroups`](#ApiClient.SignalGroup.GetRecordingGroups "ApiClient.SignalGroup.GetRecordingGroups")

- [`SignalGroupBase.GetRecordingGroups`](#ApiClient.SignalGroupBase.GetRecordingGroups "ApiClient.SignalGroupBase.GetRecordingGroups")

- [`SignalRecordingApi.CreateRecordingGroup`](#ApiClient.SignalRecordingApi.CreateRecordingGroup "ApiClient.SignalRecordingApi.CreateRecordingGroup")

- [`SyncConfig.GetMaster`](TraceAnalysisApi.md#ApiClient.SyncConfig.GetMaster "ApiClient.SyncConfig.GetMaster")

- [`Synchronization.GetMaster`](TraceAnalysisApi.md#ApiClient.Synchronization.GetMaster "ApiClient.Synchronization.GetMaster")

- [`TsAddTrace.GetRecordingGroup`](TestStepApi.md#ApiClient.TsAddTrace.GetRecordingGroup "ApiClient.TsAddTrace.GetRecordingGroup")

- [`TsStartTrace.GetRecordingGroup`](TestStepApi.md#ApiClient.TsStartTrace.GetRecordingGroup "ApiClient.TsStartTrace.GetRecordingGroup")

- [`TsStopTrace.GetRecordingGroup`](TestStepApi.md#ApiClient.TsStopTrace.GetRecordingGroup "ApiClient.TsStopTrace.GetRecordingGroup")

- [`UtcTimestampSynchronization.GetMaster`](TraceAnalysisApi.md#ApiClient.UtcTimestampSynchronization.GetMaster "ApiClient.UtcTimestampSynchronization.GetMaster")

Subclasses

- [`VariableRecordingGroup`](PackageApi.md#ApiClient.VariableRecordingGroup "ApiClient.VariableRecordingGroup")

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

AppendRecordingInfo(*recordingInfo*)[¶](#ApiClient.RecordingGroup.AppendRecordingInfo "Link to this definition")  
Adds a recording info to the recording group.

Parameters:  **recordingInfo** ([`RecordingInfo`](#ApiClient.RecordingInfo "ApiClient.RecordingInfo")) – The recording info to be added

Clone()[¶](#ApiClient.RecordingGroup.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`RecordingGroup`](#ApiClient.RecordingGroup "ApiClient.RecordingGroup")

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

Return type:  list[[`RecordingInfo`](#ApiClient.RecordingInfo "ApiClient.RecordingInfo")]

GetRecordingMode()[¶](#ApiClient.RecordingGroup.GetRecordingMode "Link to this definition")  
Returns the recording mode of the recording group as one of the following constants:

> - [`RecordingGroup.RECORDING_MODE_MANUAL`](#ApiClient.RecordingGroup.RECORDING_MODE_MANUAL "ApiClient.RecordingGroup.RECORDING_MODE_MANUAL")
>
> - [`RecordingGroup.RECORDING_MODE_AUTO_RESTRICTED`](#ApiClient.RecordingGroup.RECORDING_MODE_AUTO_RESTRICTED "ApiClient.RecordingGroup.RECORDING_MODE_AUTO_RESTRICTED")
>
> - [`RecordingGroup.RECORDING_MODE_AUTO`](#ApiClient.RecordingGroup.RECORDING_MODE_AUTO "ApiClient.RecordingGroup.RECORDING_MODE_AUTO")
>
> - [`RecordingGroup.RECORDING_MODE_TRIGGER`](#ApiClient.RecordingGroup.RECORDING_MODE_TRIGGER "ApiClient.RecordingGroup.RECORDING_MODE_TRIGGER")

Returns:  The recording mode constant

Return type:  int

GetSignalGroup()[¶](#ApiClient.RecordingGroup.GetSignalGroup "Link to this definition")  
Returns the parent signal group.

Returns:  The parent signal group

Return type:  [`SignalGroupBase`](#ApiClient.SignalGroupBase "ApiClient.SignalGroupBase")

GetStartTriggerCondition()[¶](#ApiClient.RecordingGroup.GetStartTriggerCondition "Link to this definition")  
Returns the start trigger condition.

Returns:  The start trigger condition

Return type:  str

GetStopTriggerCondition()[¶](#ApiClient.RecordingGroup.GetStopTriggerCondition "Link to this definition")  
Returns the stop trigger condition.

Returns:  The stop trigger condition

Return type:  str

RemoveRecordingInfo(*recordingInfo*)[¶](#ApiClient.RecordingGroup.RemoveRecordingInfo "Link to this definition")  
Removes a recording info from the recording group.

Parameters:  **recordingInfo** ([`RecordingInfo`](#ApiClient.RecordingInfo "ApiClient.RecordingInfo")) – The recording info to be removed

Raises:  
ApiError: When recording info is not part of recording group

SetErrorOnEmptyStart(*value*)[¶](#ApiClient.RecordingGroup.SetErrorOnEmptyStart "Link to this definition")  
Sets whether starting this recording group will lead to an error if it has no signals to record.

Parameters:  **value** (*bool*) – True if the start of the empty group shall lead to an error, otherwise False.

SetErrorOnOnlyGenericSignals(*value*)[¶](#ApiClient.RecordingGroup.SetErrorOnOnlyGenericSignals "Link to this definition")  
Sets whether starting this recording group will lead to an error if it consists of only generic signals.

Parameters:  **value** (*bool*) – True if the start of group with mentioned characteristics shall lead to an error, otherwise False.

SetErrorOnOnlyUndefinedSystemIdentifiers(*value*)[¶](#ApiClient.RecordingGroup.SetErrorOnOnlyUndefinedSystemIdentifiers "Link to this definition")  
Sets whether starting this recording group will lead to an error if the mapping targets of all signals of the group refer to an undefined system identifier.

Parameters:  **value** (*bool*) – True if the start of group with mentioned characteristics shall lead to an error, otherwise False.

SetFilenameTemplate(*template*)[¶](#ApiClient.RecordingGroup.SetFilenameTemplate "Link to this definition")  
Sets the file name template of the recording group.

Parameters:  **template** (*str*) – The new file name template of the recording group.

SetName(*name*)[¶](#ApiClient.RecordingGroup.SetName "Link to this definition")  
Sets the name of the recording group.

Parameters:  **name** (*str*) – The new name

SetPostStartTime(*time*)[¶](#ApiClient.RecordingGroup.SetPostStartTime "Link to this definition")  
Sets the post start time of the start trigger of the recording.

Parameters:  **time** (*float*) – The post start time in seconds.

SetPostStopTime(*time*)[¶](#ApiClient.RecordingGroup.SetPostStopTime "Link to this definition")  
Sets the post stop time of the stop trigger.

Parameters:  **time** (*float*) – The post stop time in seconds.

SetPreTriggerTime(*time*)[¶](#ApiClient.RecordingGroup.SetPreTriggerTime "Link to this definition")  
Sets the pre trigger time for the start trigger of the recording.

Parameters:  **time** (*float*) – The pre trigger time in seconds.

SetRecordingMode(*value*)[¶](#ApiClient.RecordingGroup.SetRecordingMode "Link to this definition")  
Sets the recording mode of the recording group to one of the following constants:

> - [`RecordingGroup.RECORDING_MODE_MANUAL`](#ApiClient.RecordingGroup.RECORDING_MODE_MANUAL "ApiClient.RecordingGroup.RECORDING_MODE_MANUAL")
>
> - [`RecordingGroup.RECORDING_MODE_AUTO_RESTRICTED`](#ApiClient.RecordingGroup.RECORDING_MODE_AUTO_RESTRICTED "ApiClient.RecordingGroup.RECORDING_MODE_AUTO_RESTRICTED")
>
> - [`RecordingGroup.RECORDING_MODE_AUTO`](#ApiClient.RecordingGroup.RECORDING_MODE_AUTO "ApiClient.RecordingGroup.RECORDING_MODE_AUTO")
>
> - [`RecordingGroup.RECORDING_MODE_TRIGGER`](#ApiClient.RecordingGroup.RECORDING_MODE_TRIGGER "ApiClient.RecordingGroup.RECORDING_MODE_TRIGGER")

Parameters:  **value** (*int*) – The recording mode constant

SetStartTriggerCondition(*condition*)[¶](#ApiClient.RecordingGroup.SetStartTriggerCondition "Link to this definition")  
Sets the start trigger condition.

Parameters:  **condition** (*str*) – The start trigger condition.

SetStopTriggerCondition(*condition*)[¶](#ApiClient.RecordingGroup.SetStopTriggerCondition "Link to this definition")  
Sets the stop trigger condition.

Parameters:  **condition** (*str*) – The stop trigger condition.

EnableAutoStartStop(*enable=True*)[¶](#ApiClient.RecordingGroup.EnableAutoStartStop "Link to this definition")  
Enables or disables automatic recording of this recording group during test execution.

Parameters:  **enable** (*bool*) – True to enable automatic recording, False to disable it

Deprecated since version 2020.1: Please use [`SetRecordingMode()`](#ApiClient.RecordingGroup.SetRecordingMode "ApiClient.RecordingGroup.SetRecordingMode") instead.

EnableTriggerStartStop(*enable=True*)[¶](#ApiClient.RecordingGroup.EnableTriggerStartStop "Link to this definition")  
Enables or disables triggered start and stop of this recording group.

Parameters:  **enable** (*bool*) – True to enable triggered recording, False to disable it.

Deprecated since version 2020.1: Please use [`SetRecordingMode()`](#ApiClient.RecordingGroup.SetRecordingMode "ApiClient.RecordingGroup.SetRecordingMode") instead.

GetDescription()[¶](#ApiClient.RecordingGroup.GetDescription "Link to this definition")  
Returns the description of the recording group.

Returns:  The description of the recording group.

Return type:  str

Deprecated since version 2020.1: The description of the recording group is not visible in the GUI. Please use the description of the signal group instead.

IsAutoStartStopEnabled()[¶](#ApiClient.RecordingGroup.IsAutoStartStopEnabled "Link to this definition")  
Returns whether the recording group is configured to be recorded automatically during test execution.

Returns:  True if automatic recording is enabled, else False

Return type:  bool

Deprecated since version 2020.1: Please use [`GetRecordingMode()`](#ApiClient.RecordingGroup.GetRecordingMode "ApiClient.RecordingGroup.GetRecordingMode") instead.

IsLogRecording()[¶](#ApiClient.RecordingGroup.IsLogRecording "Link to this definition")  
Returns whether the recording group is a log recording.

Returns:  True if the recording group is a log recording else False

Return type:  bool

Deprecated since version 2022.1: LogRecording was removed. All recording groups are SignalRecordings.

IsSignalRecording()[¶](#ApiClient.RecordingGroup.IsSignalRecording "Link to this definition")  
Returns whether the recording group is a signal recording.

Returns:  True if the recording group is a signal recording else False

Return type:  bool

Deprecated since version 2022.1: LogRecording was removed. All recording groups are SignalRecordings.

IsTriggerStartStopEnabled()[¶](#ApiClient.RecordingGroup.IsTriggerStartStopEnabled "Link to this definition")  
Returns if the recording group is configured to be start and stopped by a trigger.

Returns:  True if triggered start and stop is enabled, else False

Return type:  bool

Deprecated since version 2020.1: Please use [`GetRecordingMode()`](#ApiClient.RecordingGroup.GetRecordingMode "ApiClient.RecordingGroup.GetRecordingMode") instead.

SetDescription(*description*)[¶](#ApiClient.RecordingGroup.SetDescription "Link to this definition")  
Sets the description of the recording group.

Parameters:  **description** (*str*) – The new description of the recording group.

Deprecated since version 2020.1: The description of the recording group is not visible in the GUI. Please use the description of the signal group instead.

## RecordingInfo[¶](#recordinginfo "Link to this heading")

*class* RecordingInfo[¶](#ApiClient.RecordingInfo "Link to this definition")  
Returned by

- [`AnalysisJobRecording.GetRecordingInfo`](AnalysisJobApi.md#ApiClient.AnalysisJobRecording.GetRecordingInfo "ApiClient.AnalysisJobRecording.GetRecordingInfo")

- [`Device.GetRecordingInfos`](TraceFileApi.md#ApiClient.Device.GetRecordingInfos "ApiClient.Device.GetRecordingInfos")

- [`ParameterSetRecordings.GetRecordingInfos`](ProjectApi.md#ApiClient.ParameterSetRecordings.GetRecordingInfos "ApiClient.ParameterSetRecordings.GetRecordingInfos")

- [`RecordingGroup.GetRecordingInfos`](#ApiClient.RecordingGroup.GetRecordingInfos "ApiClient.RecordingGroup.GetRecordingInfos")

- [`SignalRecordingApi.CreateRecordingInfo`](#ApiClient.SignalRecordingApi.CreateRecordingInfo "ApiClient.SignalRecordingApi.CreateRecordingInfo")

- [`VariableRecordingGroup.GetRecordingInfos`](PackageApi.md#ApiClient.VariableRecordingGroup.GetRecordingInfos "ApiClient.VariableRecordingGroup.GetRecordingInfos")

Clone()[¶](#ApiClient.RecordingInfo.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`RecordingInfo`](#ApiClient.RecordingInfo "ApiClient.RecordingInfo")

DeleteFormatDetails()[¶](#ApiClient.RecordingInfo.DeleteFormatDetails "Link to this definition")  
Deletes the format details of the existing recording.

GetFormatDetailsString()[¶](#ApiClient.RecordingInfo.GetFormatDetailsString "Link to this definition")  
Returns the recording type specific format details as string.

Returns:  The format details as string, None if there aren’t any format details

Return type:  str

GetPath()[¶](#ApiClient.RecordingInfo.GetPath "Link to this definition")  
Returns the path (or the first path if there is a list of paths) for the recording.

Returns:  The path

Return type:  str

GetPathList()[¶](#ApiClient.RecordingInfo.GetPathList "Link to this definition")  
Returns the list of paths of the recording as a sequence of multiple files.

Returns:  The list of paths

Return type:  list[str]

GetRecordingName()[¶](#ApiClient.RecordingInfo.GetRecordingName "Link to this definition")  
Returns the name of the recording.

Returns:  The name

Return type:  str

GetRecordingNumber()[¶](#ApiClient.RecordingInfo.GetRecordingNumber "Link to this definition")  
Returns the recording number.

Returns:  The recording number

Return type:  int

GetRecordingType()[¶](#ApiClient.RecordingInfo.GetRecordingType "Link to this definition")  
Returns the recording type as string.

Returns:  The recording type, e.g. ‘CSV’, ‘MDF_VECTOR’

Return type:  str

GetStartTime()[¶](#ApiClient.RecordingInfo.GetStartTime "Link to this definition")  
Returns the first time stamp to be read in from the recording.

Raises:  
**ApiError** – Underlying data value can not be returned as float.

Returns:  First time stamp to be read in from the recording

Return type:  float

GetStopTime()[¶](#ApiClient.RecordingInfo.GetStopTime "Link to this definition")  
Returns the last time stamp to be read in from the recording.

Raises:  
**ApiError** – Underlying data value can not be returned as float.

Returns:  Last time stamp to be read in from the recording

Return type:  float

GetSyncDeltaT()[¶](#ApiClient.RecordingInfo.GetSyncDeltaT "Link to this definition")  
Get the time axis shift determined by the synchronization.

Note:  
Only use in the context of a analysis job.

Returns:  Shift of time axis determined by the synchronization or None, when no synchronization information exists.

Return type:  float

SetFormatDetailsString(*formatDetails*)[¶](#ApiClient.RecordingInfo.SetFormatDetailsString "Link to this definition")  
Sets the format details of the existing recording. If the file of this recording info exists, it will be checked whether the format details string is supported.

Parameters:  **formatDetails** (*str*) – Format details of the recording.

SetSyncDeltaT(*deltaT*)[¶](#ApiClient.RecordingInfo.SetSyncDeltaT "Link to this definition")  
Set the time axis shift determined by the synchronization.

Note:  
Only use in the context of a analysis job. Synchronization is ignored when this information is set.

Parameters:  **deltaT** (*float*) – Shift of time axis determined by the synchronization or None, when no synchronization information exists.

## SignalGroupBase[¶](#signalgroupbase "Link to this heading")

*class* SignalGroupBase[¶](#ApiClient.SignalGroupBase "Link to this definition")  
API to access signal groups. Signals of a signal group are represented by references to mapping items.

Returned by

- [`AutoAssignRecordingGroup.GetSignalGroup`](PackageApi.md#ApiClient.AutoAssignRecordingGroup.GetSignalGroup "ApiClient.AutoAssignRecordingGroup.GetSignalGroup")

- [`RecordingGroup.GetSignalGroup`](#ApiClient.RecordingGroup.GetSignalGroup "ApiClient.RecordingGroup.GetSignalGroup")

- [`RecordingGroupBase.GetSignalGroup`](TraceAnalysisApi.md#ApiClient.RecordingGroupBase.GetSignalGroup "ApiClient.RecordingGroupBase.GetSignalGroup")

Subclasses

- [`AutoAssignSignalGroup`](PackageApi.md#ApiClient.AutoAssignSignalGroup "ApiClient.AutoAssignSignalGroup")

- [`SignalGroup`](#ApiClient.SignalGroup "ApiClient.SignalGroup")

AppendMappingItem(*mappingItem*)[¶](#ApiClient.SignalGroupBase.AppendMappingItem "Link to this definition")  
Adds a mapping item to the signal group.

Parameters:  **mappingItem** ([`MappingItem`](MappingApi.md#ApiClient.MappingItem "ApiClient.MappingItem")) – The mapping item to be added

AppendRecordingGroup(*recordingGroup*)[¶](#ApiClient.SignalGroupBase.AppendRecordingGroup "Link to this definition")  
Adds a recording group to the signal group.

Parameters:  **recordingGroup** ([`RecordingGroup`](#ApiClient.RecordingGroup "ApiClient.RecordingGroup")) – The recording group to be added

Clone()[¶](#ApiClient.SignalGroupBase.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`SignalGroupBase`](#ApiClient.SignalGroupBase "ApiClient.SignalGroupBase")

GetDescription()[¶](#ApiClient.SignalGroupBase.GetDescription "Link to this definition")  
Returns the description of the signal group.

Returns:  The description of the signal group.

Return type:  str

GetMappingItemNames()[¶](#ApiClient.SignalGroupBase.GetMappingItemNames "Link to this definition")  
Returns the names of all the mapping Items within the signal group.

Returns:  List of all the mapping item names

Return type:  list[str]

GetMappingItems()[¶](#ApiClient.SignalGroupBase.GetMappingItems "Link to this definition")  
Returns a list of all resolved mapping items (representing the signals) within the signal group. Mapping items can be a part of the package’s mapping or of the global mapping if any is loaded.

Returns:  List of all resolved mapping items.

Return type:  list[[`MappingItem`](MappingApi.md#ApiClient.MappingItem "ApiClient.MappingItem")]

GetName()[¶](#ApiClient.SignalGroupBase.GetName "Link to this definition")  
Returns the name of the signal group.

Returns:  The name

Return type:  str

GetRecordingGroupNames()[¶](#ApiClient.SignalGroupBase.GetRecordingGroupNames "Link to this definition")  
Returns the names of all the recording groups within the signal group.

Returns:  List of all the recording group names

Return type:  list[str]

GetRecordingGroups()[¶](#ApiClient.SignalGroupBase.GetRecordingGroups "Link to this definition")  
Returns a list of all the signal recording groups within the signal group.

Returns:  List of all the signal recording groups

Return type:  list[[`RecordingGroup`](#ApiClient.RecordingGroup "ApiClient.RecordingGroup")]

RemoveMappingItem(*mappingItemName*)[¶](#ApiClient.SignalGroupBase.RemoveMappingItem "Link to this definition")  
Removes a mapping item from the signal group.

Parameters:  **mappingItemName** (*str*) – The mapping item name

RemoveRecordingGroup(*recordingGroup*)[¶](#ApiClient.SignalGroupBase.RemoveRecordingGroup "Link to this definition")  
Removes a recording group from the signalGroup.

Parameters:  **recordingGroup** ([`RecordingGroup`](#ApiClient.RecordingGroup "ApiClient.RecordingGroup")) – The recording group to be removed

SetDescription(*description*)[¶](#ApiClient.SignalGroupBase.SetDescription "Link to this definition")  
Sets the description of the signal group.

Parameters:  **description** (*str*) – The new description of the signal group.

SetName(*name*)[¶](#ApiClient.SignalGroupBase.SetName "Link to this definition")  
Sets the name of the signal group.

Parameters:  **name** (*str*) – The new name

## SignalGroup[¶](#signalgroup "Link to this heading")

*class* SignalGroup[¶](#ApiClient.SignalGroup "Link to this definition")  
API to access signal groups. Signals of a signal group are represented by references to mapping items.

Base class

[`SignalGroupBase`](#ApiClient.SignalGroupBase "ApiClient.SignalGroupBase")

Returned by

- [`RecordingConfig.GetSignalGroups`](PackageApi.md#ApiClient.RecordingConfig.GetSignalGroups "ApiClient.RecordingConfig.GetSignalGroups")

- [`SignalRecordingApi.CreateSignalGroup`](#ApiClient.SignalRecordingApi.CreateSignalGroup "ApiClient.SignalRecordingApi.CreateSignalGroup")

AppendMappingItem(*mappingItem*)[¶](#ApiClient.SignalGroup.AppendMappingItem "Link to this definition")  
Adds a mapping item to the signal group.

Parameters:  **mappingItem** ([`MappingItem`](MappingApi.md#ApiClient.MappingItem "ApiClient.MappingItem")) – The mapping item to be added

AppendRecordingGroup(*recordingGroup*)[¶](#ApiClient.SignalGroup.AppendRecordingGroup "Link to this definition")  
Adds a recording group to the signal group.

Parameters:  **recordingGroup** ([`RecordingGroup`](#ApiClient.RecordingGroup "ApiClient.RecordingGroup")) – The recording group to be added

Clone()[¶](#ApiClient.SignalGroup.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`SignalGroup`](#ApiClient.SignalGroup "ApiClient.SignalGroup")

GetDescription()[¶](#ApiClient.SignalGroup.GetDescription "Link to this definition")  
Returns the description of the signal group.

Returns:  The description of the signal group.

Return type:  str

GetMappingItemNames()[¶](#ApiClient.SignalGroup.GetMappingItemNames "Link to this definition")  
Returns the names of all the mapping Items within the signal group.

Returns:  List of all the mapping item names

Return type:  list[str]

GetMappingItems()[¶](#ApiClient.SignalGroup.GetMappingItems "Link to this definition")  
Returns a list of all resolved mapping items (representing the signals) within the signal group. Mapping items can be a part of the package’s mapping or of the global mapping if any is loaded.

Returns:  List of all resolved mapping items.

Return type:  list[[`MappingItem`](MappingApi.md#ApiClient.MappingItem "ApiClient.MappingItem")]

GetName()[¶](#ApiClient.SignalGroup.GetName "Link to this definition")  
Returns the name of the signal group.

Returns:  The name

Return type:  str

GetRecordingGroupNames()[¶](#ApiClient.SignalGroup.GetRecordingGroupNames "Link to this definition")  
Returns the names of all the recording groups within the signal group.

Returns:  List of all the recording group names

Return type:  list[str]

GetRecordingGroups()[¶](#ApiClient.SignalGroup.GetRecordingGroups "Link to this definition")  
Returns a list of all the signal recording groups within the signal group.

Returns:  List of all the signal recording groups

Return type:  list[[`RecordingGroup`](#ApiClient.RecordingGroup "ApiClient.RecordingGroup")]

RemoveMappingItem(*mappingItemName*)[¶](#ApiClient.SignalGroup.RemoveMappingItem "Link to this definition")  
Removes a mapping item from the signal group.

Parameters:  **mappingItemName** (*str*) – The mapping item name

RemoveRecordingGroup(*recordingGroup*)[¶](#ApiClient.SignalGroup.RemoveRecordingGroup "Link to this definition")  
Removes a recording group from the signalGroup.

Parameters:  **recordingGroup** ([`RecordingGroup`](#ApiClient.RecordingGroup "ApiClient.RecordingGroup")) – The recording group to be removed

SetDescription(*description*)[¶](#ApiClient.SignalGroup.SetDescription "Link to this definition")  
Sets the description of the signal group.

Parameters:  **description** (*str*) – The new description of the signal group.

SetName(*name*)[¶](#ApiClient.SignalGroup.SetName "Link to this definition")  
Sets the name of the signal group.

Parameters:  **name** (*str*) – The new name
