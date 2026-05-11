[ Internal APIs ](api.md)

[ Advanced operations of package variable types ](variabledatastructures.md)

[ Advanced properties of bus-related objects ](busdatastructures.md)

[ Bus related objects of trace analysis ](busdatastructuresTraceanalysis.md)

[ Advanced properties of diagnostics-related objects ](diagdatastructures.md)

[ Diagnostics related objects of trace analysis ](diagdatastructuresTraceanalysis.md)

[ Advanced properties of media-related objects ](mediadatastructures.md)

[ Advanced properties of DLT logging-related objects ](dltdatastructures.md)

[ COM API ](com-api.md)

[ REST API ](rest-api.md)

[ Report API ](apireport.md)

[ Object API ](objectApi.md)

Object API

[ API entry points ](objectApi.md#api-entry-points)

API entry points

[ API for Analysis Jobs ](AnalysisJobApi.md)

[ API for Artifacts ](ArtifactApi.md)

[ API for Project Components ](ComponentApi.md)

[ API for Configurations ](ConfigurationApi.md)

[ API for Expectations ](ExpectationApi.md)

[ API for Expressions ](ExpressionApi.md)

[ API for Global Mappings ](GlobalMappingApi.md)

[ API for Mappings ](MappingApi.md)

[ API for Multimedia Objects ](MultimediaApi.md)

[ API for Packages ](PackageApi.md)

[ API for Parameters ](ParameterApi.md)

[ API for Projects ](ProjectApi.md)

[ API for Relations ](RelationApi.md)

[ API for Reports ](ReportApi.md)

[ API for Report Filters ](ReportFilterApi.md)

[ API for Settings ](SettingsApi.md)

[ API for Signals ](SignalApi.md)

[ API for Signal Descriptions ](SignalDescriptionApi.md)

[ API for Signal Recordings ](#)

API for Signal Recordings

- [ RecordingGroup ](SignalRecordingApi/RecordingGroup.md)
- [ RecordingInfo ](SignalRecordingApi/RecordingInfo.md)
- [ SignalGroup ](SignalRecordingApi/SignalGroup.md)
- [ SignalGroupBase ](SignalRecordingApi/SignalGroupBase.md)
- [ VariableRecordingGroup ](SignalRecordingApi/VariableRecordingGroup.md)

API for Signal Recordings [ API for Signal Recordings ](#)

API for Signal Recordings

- [C SignalRecordingApi ](#ApiClient.SignalRecordingApi)
  - [M CreateFormatDetailsStringASC ](#ApiClient.SignalRecordingApi.CreateFormatDetailsStringASC)
  - [M CreateFormatDetailsStringBLF ](#ApiClient.SignalRecordingApi.CreateFormatDetailsStringBLF)
  - [M CreateFormatDetailsStringCSV ](#ApiClient.SignalRecordingApi.CreateFormatDetailsStringCSV)
  - [M CreateFormatDetailsStringMatControlDesk ](#ApiClient.SignalRecordingApi.CreateFormatDetailsStringMatControlDesk)
  - [M CreateFormatDetailsStringMdf4ControlDesk ](#ApiClient.SignalRecordingApi.CreateFormatDetailsStringMdf4ControlDesk)
  - [M CreateFormatDetailsStringMdfControlDesk ](#ApiClient.SignalRecordingApi.CreateFormatDetailsStringMdfControlDesk)
  - [M CreateFormatDetailsStringPcap ](#ApiClient.SignalRecordingApi.CreateFormatDetailsStringPcap)
  - [M CreateFormatDetailsStringSTI ](#ApiClient.SignalRecordingApi.CreateFormatDetailsStringSTI)
  - [M CreateFormatDetailsStringTTL ](#ApiClient.SignalRecordingApi.CreateFormatDetailsStringTTL)
  - [M CreateRecordingGroup ](#ApiClient.SignalRecordingApi.CreateRecordingGroup)
  - [M CreateRecordingInfo ](#ApiClient.SignalRecordingApi.CreateRecordingInfo)
  - [M CreateSignalGroup ](#ApiClient.SignalRecordingApi.CreateSignalGroup)
- [ RecordingGroup ](SignalRecordingApi/RecordingGroup.md)
- [ RecordingInfo ](SignalRecordingApi/RecordingInfo.md)
- [ SignalGroup ](SignalRecordingApi/SignalGroup.md)
- [ SignalGroupBase ](SignalRecordingApi/SignalGroupBase.md)
- [ VariableRecordingGroup ](SignalRecordingApi/VariableRecordingGroup.md)

[ API for Symbols ](SymbolApi.md)

[ API for Test Steps ](TestStepApi.md)

[ API for Touch Inputs ](TouchInputApi.md)

[ API for Trace Analyses ](TraceAnalysisApi.md)

[ API for Trace Files ](TraceFileApi.md)

[ API for Trace Step Templates ](TraceStepTemplateApi.md)

[ API for Variables ](VariableApi.md)

[ API for Workspaces ](WorkspaceApi.md)

[ Trace Analysis API ](../TraceAnalysisAPI/index.md)

[ Generator APIs ](../generators/index.md)

[ Tools ](../tools/index.md)

[ User test management ](../userTestmanagement/index.md)

[ UserUtility API ](../user-utility/user-utility.md)

[ Utility Examples ](../user-utility/example-utilities.md)

API for Signal Recordings

- [C SignalRecordingApi ](#ApiClient.SignalRecordingApi)
  - [M CreateFormatDetailsStringASC ](#ApiClient.SignalRecordingApi.CreateFormatDetailsStringASC)
  - [M CreateFormatDetailsStringBLF ](#ApiClient.SignalRecordingApi.CreateFormatDetailsStringBLF)
  - [M CreateFormatDetailsStringCSV ](#ApiClient.SignalRecordingApi.CreateFormatDetailsStringCSV)
  - [M CreateFormatDetailsStringMatControlDesk ](#ApiClient.SignalRecordingApi.CreateFormatDetailsStringMatControlDesk)
  - [M CreateFormatDetailsStringMdf4ControlDesk ](#ApiClient.SignalRecordingApi.CreateFormatDetailsStringMdf4ControlDesk)
  - [M CreateFormatDetailsStringMdfControlDesk ](#ApiClient.SignalRecordingApi.CreateFormatDetailsStringMdfControlDesk)
  - [M CreateFormatDetailsStringPcap ](#ApiClient.SignalRecordingApi.CreateFormatDetailsStringPcap)
  - [M CreateFormatDetailsStringSTI ](#ApiClient.SignalRecordingApi.CreateFormatDetailsStringSTI)
  - [M CreateFormatDetailsStringTTL ](#ApiClient.SignalRecordingApi.CreateFormatDetailsStringTTL)
  - [M CreateRecordingGroup ](#ApiClient.SignalRecordingApi.CreateRecordingGroup)
  - [M CreateRecordingInfo ](#ApiClient.SignalRecordingApi.CreateRecordingInfo)
  - [M CreateSignalGroup ](#ApiClient.SignalRecordingApi.CreateSignalGroup)

# API for Signal Recordings[¶](#api-for-signal-recordings "Link to this heading")

Part of the [Object based program API](objectApi.md#objectapi).

*class* SignalRecordingApi[¶](#ApiClient.SignalRecordingApi "Link to this definition")  
Returned by

- [`PackageApi.SignalRecordingApi`](PackageApi.md#ApiClient.PackageApi.SignalRecordingApi "ApiClient.PackageApi.SignalRecordingApi (Python attribute) — Returns the SignalRecordingApi namespace.")

CreateFormatDetailsStringASC(*[medium](#ApiClient.SignalRecordingApi.CreateFormatDetailsStringASC.medium "ApiClient.SignalRecordingApi.CreateFormatDetailsStringASC.medium (Python parameter) — The medium to be read: "AUTO" (default), "CAN", "CANFD", "FlexRay" or "LIN".  If medium is "AUTO" the parser tries to guess the medium by reading the header of the ASC file.")=`'AUTO'`*, *[channel](#ApiClient.SignalRecordingApi.CreateFormatDetailsStringASC.channel "ApiClient.SignalRecordingApi.CreateFormatDetailsStringASC.channel (Python parameter) — The channel(s) to read.")=`'ALL'`*, *[direction](#ApiClient.SignalRecordingApi.CreateFormatDetailsStringASC.direction "ApiClient.SignalRecordingApi.CreateFormatDetailsStringASC.direction (Python parameter) — The communication direction: "Rx", "Tx" or "RxTx".")=`'RxTx'`*)[¶](#ApiClient.SignalRecordingApi.CreateFormatDetailsStringASC "Link to this definition")  
Creates the format details string for ASC files. The information are needed to filter the medium, a specific channel and the direction.

Parameters:  medium : str[¶](#ApiClient.SignalRecordingApi.CreateFormatDetailsStringASC.medium "Permalink to this definition")  
The medium to be read: “AUTO” (default), “CAN”, “CANFD”, “FlexRay” or “LIN”.

If medium is “AUTO” the parser tries to guess the medium by reading the header of the ASC file. Only frames of the guessed medium will be read.

channel : str[¶](#ApiClient.SignalRecordingApi.CreateFormatDetailsStringASC.channel "Permalink to this definition")  
The channel(s) to read. Possible values: “ALL” or “01” up to “99”.

For medium “FlexRay” values are typically: “ALL”, “01” or “02”.

For medium “LIN” values are “ALL” or “1” up to “64”

direction : str[¶](#ApiClient.SignalRecordingApi.CreateFormatDetailsStringASC.direction "Permalink to this definition")  
The communication direction: “Rx”, “Tx” or “RxTx”.

Returns:  The newly created format details string.

Return type:  str

CreateFormatDetailsStringBLF(*[medium](#ApiClient.SignalRecordingApi.CreateFormatDetailsStringBLF.medium "ApiClient.SignalRecordingApi.CreateFormatDetailsStringBLF.medium (Python parameter) — The medium to be read: "AUTO" (default), "CAN", "FlexRay", or "Ethernet".")=`'AUTO'`*, *[channel](#ApiClient.SignalRecordingApi.CreateFormatDetailsStringBLF.channel "ApiClient.SignalRecordingApi.CreateFormatDetailsStringBLF.channel (Python parameter) — The channel(s) to read.")=`'ALL'`*, *[direction](#ApiClient.SignalRecordingApi.CreateFormatDetailsStringBLF.direction "ApiClient.SignalRecordingApi.CreateFormatDetailsStringBLF.direction (Python parameter) — The communication direction: "Rx", "Tx" or "RxTx".")=`'RxTx'`*, *[port](#ApiClient.SignalRecordingApi.CreateFormatDetailsStringBLF.port "ApiClient.SignalRecordingApi.CreateFormatDetailsStringBLF.port (Python parameter) — The Ethernet port for reading Ethernet signals. Only used if medium is 'Ethernet'.")=`'30490'`*)[¶](#ApiClient.SignalRecordingApi.CreateFormatDetailsStringBLF "Link to this definition")  
Creates the format details string for BLF files. The information are needed to filter the medium, a specific channel, the direction and the Ethernet port (if necessary).

Parameters:  medium : str[¶](#ApiClient.SignalRecordingApi.CreateFormatDetailsStringBLF.medium "Permalink to this definition")  
The medium to be read: “AUTO” (default), “CAN”, “FlexRay”, or “Ethernet”.

channel : str[¶](#ApiClient.SignalRecordingApi.CreateFormatDetailsStringBLF.channel "Permalink to this definition")  
The channel(s) to read. Possible values: “ALL” or “01” up to “99”.

For medium “FlexRay” values are typically: “ALL”, “01” or “02”.

direction : str[¶](#ApiClient.SignalRecordingApi.CreateFormatDetailsStringBLF.direction "Permalink to this definition")  
The communication direction: “Rx”, “Tx” or “RxTx”.

port : str[¶](#ApiClient.SignalRecordingApi.CreateFormatDetailsStringBLF.port "Permalink to this definition")  
The Ethernet port for reading Ethernet signals. Only used if medium is ‘Ethernet’.

Returns:  The newly created format details string.

Return type:  str

CreateFormatDetailsStringCSV(*[columnSeparator](#ApiClient.SignalRecordingApi.CreateFormatDetailsStringCSV.columnSeparator "ApiClient.SignalRecordingApi.CreateFormatDetailsStringCSV.columnSeparator (Python parameter) — The column separator.")=`';'`*, *[decimalSeparator](#ApiClient.SignalRecordingApi.CreateFormatDetailsStringCSV.decimalSeparator "ApiClient.SignalRecordingApi.CreateFormatDetailsStringCSV.decimalSeparator (Python parameter) — The decimal separator.")=`'.'`*, *[thousandSeparator](#ApiClient.SignalRecordingApi.CreateFormatDetailsStringCSV.thousandSeparator "ApiClient.SignalRecordingApi.CreateFormatDetailsStringCSV.thousandSeparator (Python parameter) — The thousand separator.")=`','`*, *[headLineNumber](#ApiClient.SignalRecordingApi.CreateFormatDetailsStringCSV.headLineNumber "ApiClient.SignalRecordingApi.CreateFormatDetailsStringCSV.headLineNumber (Python parameter) — The line number of the header with signal names.")=`0`*, *[timeColumn](#ApiClient.SignalRecordingApi.CreateFormatDetailsStringCSV.timeColumn "ApiClient.SignalRecordingApi.CreateFormatDetailsStringCSV.timeColumn (Python parameter) — The column number of the time column.")=`0`*)[¶](#ApiClient.SignalRecordingApi.CreateFormatDetailsStringCSV "Link to this definition")  
Creates a format string for CSV files.

Parameters:  columnSeparator : str[¶](#ApiClient.SignalRecordingApi.CreateFormatDetailsStringCSV.columnSeparator "Permalink to this definition")  
The column separator.

decimalSeparator : str[¶](#ApiClient.SignalRecordingApi.CreateFormatDetailsStringCSV.decimalSeparator "Permalink to this definition")  
The decimal separator.

thousandSeparator : str[¶](#ApiClient.SignalRecordingApi.CreateFormatDetailsStringCSV.thousandSeparator "Permalink to this definition")  
The thousand separator.

headLineNumber : int[¶](#ApiClient.SignalRecordingApi.CreateFormatDetailsStringCSV.headLineNumber "Permalink to this definition")  
The line number of the header with signal names.

timeColumn : int[¶](#ApiClient.SignalRecordingApi.CreateFormatDetailsStringCSV.timeColumn "Permalink to this definition")  
The column number of the time column.

Returns:  The newly created format details string.

Return type:  str

CreateFormatDetailsStringMatControlDesk(*[platformToModelNames](#ApiClient.SignalRecordingApi.CreateFormatDetailsStringMatControlDesk.platformToModelNames "ApiClient.SignalRecordingApi.CreateFormatDetailsStringMatControlDesk.platformToModelNames (Python parameter) — Mapping of platform names to model names (in ecu.test).")*)[¶](#ApiClient.SignalRecordingApi.CreateFormatDetailsStringMatControlDesk "Link to this definition")  
Creates the format details string for MAT files created by ControlDeskNG. The devices in the file are named like the platforms defined in ControlDeskNG. To address signals via model values a dictionary with a mapping of platform names to your model names (in ecu.test) can be specified.

Parameters:  platformToModelNames : dict[string, string][¶](#ApiClient.SignalRecordingApi.CreateFormatDetailsStringMatControlDesk.platformToModelNames "Permalink to this definition")  
Mapping of platform names to model names (in ecu.test).

Returns:  The newly created format details string.

Return type:  str

CreateFormatDetailsStringMdf4ControlDesk(*[platformToModelNames](#ApiClient.SignalRecordingApi.CreateFormatDetailsStringMdf4ControlDesk.platformToModelNames "ApiClient.SignalRecordingApi.CreateFormatDetailsStringMdf4ControlDesk.platformToModelNames (Python parameter) — Mapping of platform names to model names (in ecu.test).")*)[¶](#ApiClient.SignalRecordingApi.CreateFormatDetailsStringMdf4ControlDesk "Link to this definition")  
Creates the format details string for MDF4 files created by ControlDeskNG. The devices in the file are named like the platforms defined in ControlDeskNG. To address signals via model values a dictionary with a mapping of platform names to your model names (in ecu.test) can be specified.

Parameters:  platformToModelNames : dict[string, string][¶](#ApiClient.SignalRecordingApi.CreateFormatDetailsStringMdf4ControlDesk.platformToModelNames "Permalink to this definition")  
Mapping of platform names to model names (in ecu.test).

Returns:  The newly created format details string.

Return type:  str

CreateFormatDetailsStringMdfControlDesk(*[platformToModelNames](#ApiClient.SignalRecordingApi.CreateFormatDetailsStringMdfControlDesk.platformToModelNames "ApiClient.SignalRecordingApi.CreateFormatDetailsStringMdfControlDesk.platformToModelNames (Python parameter) — Mapping of platform names to model names (in ecu.test).")*)[¶](#ApiClient.SignalRecordingApi.CreateFormatDetailsStringMdfControlDesk "Link to this definition")  
Creates the format details string for MDF files created by ControlDesk. The devices in the file are named like the platforms defined in ControlDesk. To address signals via model values a dictionary with a mapping of platform names to your model names (in ecu.test) can be specified.

Parameters:  platformToModelNames : dict[string, string][¶](#ApiClient.SignalRecordingApi.CreateFormatDetailsStringMdfControlDesk.platformToModelNames "Permalink to this definition")  
Mapping of platform names to model names (in ecu.test).

Returns:  The newly created format details string.

Return type:  str

CreateFormatDetailsStringPcap(*[port](#ApiClient.SignalRecordingApi.CreateFormatDetailsStringPcap.port "ApiClient.SignalRecordingApi.CreateFormatDetailsStringPcap.port (Python parameter) — The Ethernet port for reading Ethernet signals.")=`'30490'`*)[¶](#ApiClient.SignalRecordingApi.CreateFormatDetailsStringPcap "Link to this definition")  
Creates the format details string for PCAP files. The information is needed to filter the Ethernet port.

Parameters:  port : str[¶](#ApiClient.SignalRecordingApi.CreateFormatDetailsStringPcap.port "Permalink to this definition")  
The Ethernet port for reading Ethernet signals.

Returns:  The newly created format details string.

Return type:  str

CreateFormatDetailsStringSTI(*[sampleRate](#ApiClient.SignalRecordingApi.CreateFormatDetailsStringSTI.sampleRate "ApiClient.SignalRecordingApi.CreateFormatDetailsStringSTI.sampleRate (Python parameter) — The sample rate.")=`50.0`*)[¶](#ApiClient.SignalRecordingApi.CreateFormatDetailsStringSTI "Link to this definition")  
Creates the format details string for STI files. The information simple provides the sample rate to generate concrete samples.

Parameters:  sampleRate : float[¶](#ApiClient.SignalRecordingApi.CreateFormatDetailsStringSTI.sampleRate "Permalink to this definition")  
The sample rate. Default is 50.0.

Returns:  The newly created format details string.

Return type:  str

CreateFormatDetailsStringTTL(*[medium](#ApiClient.SignalRecordingApi.CreateFormatDetailsStringTTL.medium "ApiClient.SignalRecordingApi.CreateFormatDetailsStringTTL.medium (Python parameter) — The medium to be read: "CAN" (default), "FlexRay", "LIN" or "Ethernet".")=`'CAN'`*, *[channel](#ApiClient.SignalRecordingApi.CreateFormatDetailsStringTTL.channel "ApiClient.SignalRecordingApi.CreateFormatDetailsStringTTL.channel (Python parameter) — The channel(s) to read.")=`'01'`*, *[direction](#ApiClient.SignalRecordingApi.CreateFormatDetailsStringTTL.direction "ApiClient.SignalRecordingApi.CreateFormatDetailsStringTTL.direction (Python parameter) — The communication direction: "Rx", "Tx" or "RxTx".")=`'RxTx'`*, *[captureDevice](#ApiClient.SignalRecordingApi.CreateFormatDetailsStringTTL.captureDevice "ApiClient.SignalRecordingApi.CreateFormatDetailsStringTTL.captureDevice (Python parameter) — Not needed anymore.")=`'ANY'`*, *[port](#ApiClient.SignalRecordingApi.CreateFormatDetailsStringTTL.port "ApiClient.SignalRecordingApi.CreateFormatDetailsStringTTL.port (Python parameter) — Only for Ethernet: The port of the SOME/IP Service-Discovery (default: 30490)")=`'30490'`*, *[tap](#ApiClient.SignalRecordingApi.CreateFormatDetailsStringTTL.tap "ApiClient.SignalRecordingApi.CreateFormatDetailsStringTTL.tap (Python parameter) — TAP number (0-7), also cascade device number.")=`'0'`*)[¶](#ApiClient.SignalRecordingApi.CreateFormatDetailsStringTTL "Link to this definition")  
Creates the format details string for TTL files.

The information are needed to filter the medium, a specific channel and the direction. Please note that the recording name (“Analog”, “CAN”, “FlexRay”, “LIN”, “Ethernet”) must be specified for the recording info, too. There are no format details for “Analog” signals.

Parameters:  medium : str[¶](#ApiClient.SignalRecordingApi.CreateFormatDetailsStringTTL.medium "Permalink to this definition")  
The medium to be read: “CAN” (default), “FlexRay”, “LIN” or “Ethernet”.

channel : str[¶](#ApiClient.SignalRecordingApi.CreateFormatDetailsStringTTL.channel "Permalink to this definition")  
The channel(s) to read. Possible values if “CAN” should be read: “01” up to “24” for the main logger and “01” up to “15” for TAP devices.

If “LIN” possible values are: “01” up to “12” for the main logger and “01” up to “15” for TAP devices.

If “FlexRay” possible values are: “1A”, “1B”, “1AB”, … ,”3AB” for the main logger and “1A”, “1B”, “2A” and “2B” for TAP devices.

If “Ethernet” possible values are: “A” and “B” for the main logger and all combinations from “1” to “6” with “A” and “B”, i.e. “1A”, “1B”, “2A”, …, “6A”, “6B”, for TAP devices.

direction : str[¶](#ApiClient.SignalRecordingApi.CreateFormatDetailsStringTTL.direction "Permalink to this definition")  
The communication direction: “Rx”, “Tx” or “RxTx”.

captureDevice : str[¶](#ApiClient.SignalRecordingApi.CreateFormatDetailsStringTTL.captureDevice "Permalink to this definition")  
Not needed anymore.

port : str[¶](#ApiClient.SignalRecordingApi.CreateFormatDetailsStringTTL.port "Permalink to this definition")  
Only for Ethernet: The port of the SOME/IP Service-Discovery (default: 30490)

tap : str[¶](#ApiClient.SignalRecordingApi.CreateFormatDetailsStringTTL.tap "Permalink to this definition")  
TAP number (0-7), also cascade device number. 0 is the main logger.

Returns:  The newly created format details string.

Return type:  str

CreateRecordingGroup(*[name](#ApiClient.SignalRecordingApi.CreateRecordingGroup.name "ApiClient.SignalRecordingApi.CreateRecordingGroup.name (Python parameter) — The name of the recording group.")=`''`*)[¶](#ApiClient.SignalRecordingApi.CreateRecordingGroup "Link to this definition")  
Creates a new recording group. If no name is given, a name will be generated if the recording group is added to signal group.

Parameters:  name : str[¶](#ApiClient.SignalRecordingApi.CreateRecordingGroup.name "Permalink to this definition")  
The name of the recording group. The name must be unique for all recording groups in a package!

Returns:  The newly created recording group

Return type:  [`RecordingGroup`](SignalRecordingApi/RecordingGroup.md#ApiClient.RecordingGroup "ApiClient.RecordingGroup (Python class) — SignalRecordingApi.CreateRecordingGroup")

CreateRecordingInfo(*[path](#ApiClient.SignalRecordingApi.CreateRecordingInfo.path "ApiClient.SignalRecordingApi.CreateRecordingInfo.path (Python parameter) — Path to the recording.")*, *[recordingName](#ApiClient.SignalRecordingApi.CreateRecordingInfo.recordingName "ApiClient.SignalRecordingApi.CreateRecordingInfo.recordingName (Python parameter) — Optional: The recording name in the file (mostly the device name).")=`''`*, *[formatDetailsString](#ApiClient.SignalRecordingApi.CreateRecordingInfo.formatDetailsString "ApiClient.SignalRecordingApi.CreateRecordingInfo.formatDetailsString (Python parameter) — Optional: The format details string with information to read the file.")=`None`*, *[recordingNumber](#ApiClient.SignalRecordingApi.CreateRecordingInfo.recordingNumber "ApiClient.SignalRecordingApi.CreateRecordingInfo.recordingNumber (Python parameter) — Optional: Number of the recording.")=`0`*, *[startTime](#ApiClient.SignalRecordingApi.CreateRecordingInfo.startTime "ApiClient.SignalRecordingApi.CreateRecordingInfo.startTime (Python parameter) — Optional: First time stamp to be read in from the recording.")=`None`*, *[stopTime](#ApiClient.SignalRecordingApi.CreateRecordingInfo.stopTime "ApiClient.SignalRecordingApi.CreateRecordingInfo.stopTime (Python parameter) — Optional: Last time stamp to be read in from the recording.")=`None`*)[¶](#ApiClient.SignalRecordingApi.CreateRecordingInfo "Link to this definition")  
Creates a recording info.

Parameters:  path : str[¶](#ApiClient.SignalRecordingApi.CreateRecordingInfo.path "Permalink to this definition")  
Path to the recording.

recordingName : str[¶](#ApiClient.SignalRecordingApi.CreateRecordingInfo.recordingName "Permalink to this definition")  
Optional: The recording name in the file (mostly the device name).

formatDetailsString : str[¶](#ApiClient.SignalRecordingApi.CreateRecordingInfo.formatDetailsString "Permalink to this definition")  
Optional: The format details string with information to read the file. If the file exists it will be checked whether the given format details string is supported.

See also: CreateFormatDetailsStringXYZ().

recordingNumber : int[¶](#ApiClient.SignalRecordingApi.CreateRecordingInfo.recordingNumber "Permalink to this definition")  
Optional: Number of the recording.

startTime : float[¶](#ApiClient.SignalRecordingApi.CreateRecordingInfo.startTime "Permalink to this definition")  
Optional: First time stamp to be read in from the recording.

stopTime : float[¶](#ApiClient.SignalRecordingApi.CreateRecordingInfo.stopTime "Permalink to this definition")  
Optional: Last time stamp to be read in from the recording.

Returns:  The newly created recording info.

Return type:  [`RecordingInfo`](SignalRecordingApi/RecordingInfo.md#ApiClient.RecordingInfo "ApiClient.RecordingInfo (Python class) — SignalRecordingApi.CreateRecordingInfo")

CreateSignalGroup(*[name](#ApiClient.SignalRecordingApi.CreateSignalGroup.name "ApiClient.SignalRecordingApi.CreateSignalGroup.name (Python parameter) — The name of the signal group.")=`''`*, *[description](#ApiClient.SignalRecordingApi.CreateSignalGroup.description "ApiClient.SignalRecordingApi.CreateSignalGroup.description (Python parameter) — Description for the signal group")=`''`*)[¶](#ApiClient.SignalRecordingApi.CreateSignalGroup "Link to this definition")  
Creates a new signal group. If no name is given, a name will be generated if the signal group is added to a package.

Parameters:  name : str[¶](#ApiClient.SignalRecordingApi.CreateSignalGroup.name "Permalink to this definition")  
The name of the signal group. The name must be unique for all signal groups in a package!

description : str[¶](#ApiClient.SignalRecordingApi.CreateSignalGroup.description "Permalink to this definition")  
Description for the signal group

Returns:  The newly created signal group.

Return type:  [`SignalGroup`](SignalRecordingApi/SignalGroup.md#ApiClient.SignalGroup "ApiClient.SignalGroup (Python class) — API to access signal groups. Signals of a signal group are represented by references to mapping items.")

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
