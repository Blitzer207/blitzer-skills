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

[ API for Symbols ](../SymbolApi.md)

[ API for Test Steps ](../TestStepApi.md)

[ API for Touch Inputs ](../TouchInputApi.md)

[ API for Trace Analyses ](../TraceAnalysisApi.md)

[ API for Trace Files ](../TraceFileApi.md)

API for Trace Files

[ Device ](Device.md)

TraceFile [ TraceFile ](#)

TraceFile

- [C TraceFile ](#ApiClient.TraceFile)
  - [M Clone ](#ApiClient.TraceFile.Clone)
  - [M GetDeviceByName ](#ApiClient.TraceFile.GetDeviceByName)
  - [M GetDeviceNames ](#ApiClient.TraceFile.GetDeviceNames)
  - [M GetDevices ](#ApiClient.TraceFile.GetDevices)
  - [M GetRecordingType ](#ApiClient.TraceFile.GetRecordingType)

[ API for Trace Step Templates ](../TraceStepTemplateApi.md)

[ API for Variables ](../VariableApi.md)

[ API for Workspaces ](../WorkspaceApi.md)

[ Trace Analysis API ](../../TraceAnalysisAPI/index.md)

[ Generator APIs ](../../generators/index.md)

[ Tools ](../../tools/index.md)

[ User test management ](../../userTestmanagement/index.md)

[ UserUtility API ](../../user-utility/user-utility.md)

[ Utility Examples ](../../user-utility/example-utilities.md)

TraceFile

- [C TraceFile ](#ApiClient.TraceFile)
  - [M Clone ](#ApiClient.TraceFile.Clone)
  - [M GetDeviceByName ](#ApiClient.TraceFile.GetDeviceByName)
  - [M GetDeviceNames ](#ApiClient.TraceFile.GetDeviceNames)
  - [M GetDevices ](#ApiClient.TraceFile.GetDevices)
  - [M GetRecordingType ](#ApiClient.TraceFile.GetRecordingType)

# TraceFile[¶](#tracefile "Link to this heading")

*class* TraceFile[¶](#ApiClient.TraceFile "Link to this definition")  
Returned by

- [`TraceFileApi.OpenTraceFile`](../TraceFileApi.md#ApiClient.TraceFileApi.OpenTraceFile "ApiClient.TraceFileApi.OpenTraceFile (Python method) — Opens an existing recording file.")

Clone()[¶](#ApiClient.TraceFile.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`TraceFile`](#ApiClient.TraceFile "ApiClient.TraceFile (Python class) — TraceFileApi.OpenTraceFile")

GetDeviceByName(*[name](#ApiClient.TraceFile.GetDeviceByName.name "ApiClient.TraceFile.GetDeviceByName.name (Python parameter) — The device name.")*)[¶](#ApiClient.TraceFile.GetDeviceByName "Link to this definition")  
Returns the device for the given name.

Parameters:  name : str[¶](#ApiClient.TraceFile.GetDeviceByName.name "Permalink to this definition")  
The device name.

Returns:  The found device

Return type:  [`Device`](Device.md#ApiClient.Device "ApiClient.Device (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")

GetDeviceNames()[¶](#ApiClient.TraceFile.GetDeviceNames "Link to this definition")  
Returns a list with all device names.

Returns:  The device names

Return type:  list[str]

GetDevices()[¶](#ApiClient.TraceFile.GetDevices "Link to this definition")  
Returns a list of all devices. A device object can be used to access recording infos.

Returns:  List of devices.

Return type:  list[[`Device`](Device.md#ApiClient.Device "ApiClient.Device (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")]

GetRecordingType()[¶](#ApiClient.TraceFile.GetRecordingType "Link to this definition")  
Returns the recording type.

Returns:  The recording type, e.g. ‘CSV’, ‘MDF_VECTOR’ etc.

Return type:  str

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
