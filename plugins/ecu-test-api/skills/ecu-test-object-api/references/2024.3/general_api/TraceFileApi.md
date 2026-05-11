# API for Trace Files[¶](#api-for-trace-files "Link to this heading")

Part of the [Object based program API](objectApi.md#objectapi)

## TraceFileApi[¶](#tracefileapi "Link to this heading")

*class* TraceFileApi[¶](#ApiClient.TraceFileApi "Link to this definition")  
API to access trace files

Returned by

- [`ApiClient.TraceFileApi`](objectApi.md#ApiClient.ApiClient.TraceFileApi "ApiClient.ApiClient.TraceFileApi")

OpenTraceFile(*filename*)[¶](#ApiClient.TraceFileApi.OpenTraceFile "Link to this definition")  
Opens an existing recording file.

Parameters:  **filename** (*str*) – Name of the trace file to open

Returns:  Trace file

Return type:  [`TraceFile`](#ApiClient.TraceFile "ApiClient.TraceFile")

## TraceFile[¶](#tracefile "Link to this heading")

*class* TraceFile[¶](#ApiClient.TraceFile "Link to this definition")  
Returned by

- [`TraceFileApi.OpenTraceFile`](#ApiClient.TraceFileApi.OpenTraceFile "ApiClient.TraceFileApi.OpenTraceFile")

Clone()[¶](#ApiClient.TraceFile.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`TraceFile`](#ApiClient.TraceFile "ApiClient.TraceFile")

GetDeviceByName(*name*)[¶](#ApiClient.TraceFile.GetDeviceByName "Link to this definition")  
Returns the device for the given name.

Parameters:  **name** (*str*) – The device name.

Returns:  The found device

Return type:  [`Device`](#ApiClient.Device "ApiClient.Device")

GetDeviceNames()[¶](#ApiClient.TraceFile.GetDeviceNames "Link to this definition")  
Returns a list with all device names.

Returns:  The device names

Return type:  list[str]

GetDevices()[¶](#ApiClient.TraceFile.GetDevices "Link to this definition")  
Returns a list of all devices. A device object can be used to access recording infos.

Returns:  List of devices.

Return type:  list[[`Device`](#ApiClient.Device "ApiClient.Device")]

GetRecordingType()[¶](#ApiClient.TraceFile.GetRecordingType "Link to this definition")  
Returns the recording type.

Returns:  The recording type, e.g. ‘CSV’, ‘MDF_VECTOR’ etc.

Return type:  str

## Device[¶](#device "Link to this heading")

*class* Device[¶](#ApiClient.Device "Link to this definition")  
Returned by

- [`TraceFile.GetDeviceByName`](#ApiClient.TraceFile.GetDeviceByName "ApiClient.TraceFile.GetDeviceByName")

- [`TraceFile.GetDevices`](#ApiClient.TraceFile.GetDevices "ApiClient.TraceFile.GetDevices")

Clone()[¶](#ApiClient.Device.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`Device`](#ApiClient.Device "ApiClient.Device")

GetName()[¶](#ApiClient.Device.GetName "Link to this definition")  
Returns the name of the device.

Returns:  The device name.

Return type:  str

GetRecordingInfos()[¶](#ApiClient.Device.GetRecordingInfos "Link to this definition")  
Returns all recording infos for the device.

Returns:  List of all recording infos.

Return type:  list[[`RecordingInfo`](SignalRecordingApi.md#ApiClient.RecordingInfo "ApiClient.RecordingInfo")]

GetSignalNames()[¶](#ApiClient.Device.GetSignalNames "Link to this definition")  
Returns all signal names provided by the device.

Returns:  List of all signal names.

Return type:  list[str]
