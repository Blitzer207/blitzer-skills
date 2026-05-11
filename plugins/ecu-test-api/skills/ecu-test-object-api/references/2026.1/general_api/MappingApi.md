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

[ API for Mappings ](#)

API for Mappings

- [ AnalysisPackageMappingItem ](MappingApi/AnalysisPackageMappingItem.md)
- [ AudioChannelMappingItem ](MappingApi/AudioChannelMappingItem.md)
- [ AudioDeviceMappingItem ](MappingApi/AudioDeviceMappingItem.md)
- [ BusMonitoringMappingItem ](MappingApi/BusMonitoringMappingItem.md)
- [ BusSignalGroupMappingItem ](MappingApi/BusSignalGroupMappingItem.md)
- [ BusSignalMappingItem ](MappingApi/BusSignalMappingItem.md)
- [ CalibrationMappingItem ](MappingApi/CalibrationMappingItem.md)
- [ CallableMappingItem ](MappingApi/CallableMappingItem.md)
- [ DebugMappingItem ](MappingApi/DebugMappingItem.md)
- [ DebugRegisterMappingItem ](MappingApi/DebugRegisterMappingItem.md)
- [ DiagDidMappingItem ](MappingApi/DiagDidMappingItem.md)
- [ DiagFaultMemoryMappingItem ](MappingApi/DiagFaultMemoryMappingItem.md)
- [ DiagObdOnUdsServiceMappingItem ](MappingApi/DiagObdOnUdsServiceMappingItem.md)
- [ DiagRoutineMappingItem ](MappingApi/DiagRoutineMappingItem.md)
- [ DiagServiceMappingItem ](MappingApi/DiagServiceMappingItem.md)
- [ EdiabasVariableMappingItem ](MappingApi/EdiabasVariableMappingItem.md)
- [ EesPinVariableMappingItem ](MappingApi/EesPinVariableMappingItem.md)
- [ EnvSimMappingItem ](MappingApi/EnvSimMappingItem.md)
- [ GenericAudioMappingItem ](MappingApi/GenericAudioMappingItem.md)
- [ GenericImageMappingItem ](MappingApi/GenericImageMappingItem.md)
- [ GenericMappingItem ](MappingApi/GenericMappingItem.md)
- [ GenericPackageMappingItem ](MappingApi/GenericPackageMappingItem.md)
- [ ImageMappingItem ](MappingApi/ImageMappingItem.md)
- [ LogFilterMessageMappingItem ](MappingApi/LogFilterMessageMappingItem.md)
- [ LoggingArgumentMappingItem ](MappingApi/LoggingArgumentMappingItem.md)
- [ MappingItem ](MappingApi/MappingItem.md)
- [ MeasureMappingItem ](MappingApi/MeasureMappingItem.md)
- [ ModelMappingItem ](MappingApi/ModelMappingItem.md)
- [ PackageMappingItem ](MappingApi/PackageMappingItem.md)
- [ PortMappingItem ](MappingApi/PortMappingItem.md)
- [ ReferenceMappingItem ](MappingApi/ReferenceMappingItem.md)
- [ RunningValueMappingItem ](MappingApi/RunningValueMappingItem.md)
- [ ServiceEventLeafMappingItem ](MappingApi/ServiceEventLeafMappingItem.md)
- [ ServiceMappingItem ](MappingApi/ServiceMappingItem.md)
- [ ServiceMethodParameterMappingItem ](MappingApi/ServiceMethodParameterMappingItem.md)
- [ ServiceMethodReturnMappingItem ](MappingApi/ServiceMethodReturnMappingItem.md)
- [ ServiceServiceMappingItem ](MappingApi/ServiceServiceMappingItem.md)

API for Mappings [ API for Mappings ](#)

API for Mappings

- [C MappingApi ](#ApiClient.MappingApi)
  - [M CreateAnalysisPackageMappingItem ](#ApiClient.MappingApi.CreateAnalysisPackageMappingItem)
  - [M CreateAudioChannelMappingItem ](#ApiClient.MappingApi.CreateAudioChannelMappingItem)
  - [M CreateAudioDeviceMappingItem ](#ApiClient.MappingApi.CreateAudioDeviceMappingItem)
  - [M CreateBusMonitoringMappingItem ](#ApiClient.MappingApi.CreateBusMonitoringMappingItem)
  - [M CreateBusSignalGroupMappingItem ](#ApiClient.MappingApi.CreateBusSignalGroupMappingItem)
  - [M CreateBusSignalWithPduMappingItem ](#ApiClient.MappingApi.CreateBusSignalWithPduMappingItem)
  - [M CreateCalibrationMappingItem ](#ApiClient.MappingApi.CreateCalibrationMappingItem)
  - [M CreateDebugMappingItem ](#ApiClient.MappingApi.CreateDebugMappingItem)
  - [M CreateDebugRegisterMappingItem ](#ApiClient.MappingApi.CreateDebugRegisterMappingItem)
  - [M CreateDiagDidMappingItem ](#ApiClient.MappingApi.CreateDiagDidMappingItem)
  - [M CreateDiagFaultMemoryMappingItem ](#ApiClient.MappingApi.CreateDiagFaultMemoryMappingItem)
  - [M CreateDiagObdOnUdsServiceMappingItem ](#ApiClient.MappingApi.CreateDiagObdOnUdsServiceMappingItem)
  - [M CreateDiagRoutineMappingItem ](#ApiClient.MappingApi.CreateDiagRoutineMappingItem)
  - [M CreateDiagServiceMappingItem ](#ApiClient.MappingApi.CreateDiagServiceMappingItem)
  - [M CreateEdiabasVariableMappingItem ](#ApiClient.MappingApi.CreateEdiabasVariableMappingItem)
  - [M CreateEesPinVariableMappingItem ](#ApiClient.MappingApi.CreateEesPinVariableMappingItem)
  - [M CreateEnvSimMappingItem ](#ApiClient.MappingApi.CreateEnvSimMappingItem)
  - [M CreateGenericMappingItem ](#ApiClient.MappingApi.CreateGenericMappingItem)
  - [M CreateImageMappingItem ](#ApiClient.MappingApi.CreateImageMappingItem)
  - [M CreateJobMappingItem ](#ApiClient.MappingApi.CreateJobMappingItem)
  - [M CreateLogFilterMessageMappingItem ](#ApiClient.MappingApi.CreateLogFilterMessageMappingItem)
  - [M CreateLoggingArgumentMappingItem ](#ApiClient.MappingApi.CreateLoggingArgumentMappingItem)
  - [M CreateMappingItem ](#ApiClient.MappingApi.CreateMappingItem)
  - [M CreateMeasurementMappingItem ](#ApiClient.MappingApi.CreateMeasurementMappingItem)
  - [M CreateModelMappingItem ](#ApiClient.MappingApi.CreateModelMappingItem)
  - [M CreatePackageMappingItem ](#ApiClient.MappingApi.CreatePackageMappingItem)
  - [M CreatePortMappingItem ](#ApiClient.MappingApi.CreatePortMappingItem)
  - [M CreateReferenceMappingItem ](#ApiClient.MappingApi.CreateReferenceMappingItem)
  - [M CreateRunningValueMappingItem ](#ApiClient.MappingApi.CreateRunningValueMappingItem)
  - [M CreateServiceEventLeafMappingItem ](#ApiClient.MappingApi.CreateServiceEventLeafMappingItem)
  - [M CreateServiceMappingItem ](#ApiClient.MappingApi.CreateServiceMappingItem)
  - [M CreateServiceMethodParameterMappingItem ](#ApiClient.MappingApi.CreateServiceMethodParameterMappingItem)
  - [M CreateServiceMethodReturnMappingItem ](#ApiClient.MappingApi.CreateServiceMethodReturnMappingItem)
  - [M CreateServiceServiceMappingItem ](#ApiClient.MappingApi.CreateServiceServiceMappingItem)
  - [M CreateTraceFileMappingItem ](#ApiClient.MappingApi.CreateTraceFileMappingItem)
- [ AnalysisPackageMappingItem ](MappingApi/AnalysisPackageMappingItem.md)
- [ AudioChannelMappingItem ](MappingApi/AudioChannelMappingItem.md)
- [ AudioDeviceMappingItem ](MappingApi/AudioDeviceMappingItem.md)
- [ BusMonitoringMappingItem ](MappingApi/BusMonitoringMappingItem.md)
- [ BusSignalGroupMappingItem ](MappingApi/BusSignalGroupMappingItem.md)
- [ BusSignalMappingItem ](MappingApi/BusSignalMappingItem.md)
- [ CalibrationMappingItem ](MappingApi/CalibrationMappingItem.md)
- [ CallableMappingItem ](MappingApi/CallableMappingItem.md)
- [ DebugMappingItem ](MappingApi/DebugMappingItem.md)
- [ DebugRegisterMappingItem ](MappingApi/DebugRegisterMappingItem.md)
- [ DiagDidMappingItem ](MappingApi/DiagDidMappingItem.md)
- [ DiagFaultMemoryMappingItem ](MappingApi/DiagFaultMemoryMappingItem.md)
- [ DiagObdOnUdsServiceMappingItem ](MappingApi/DiagObdOnUdsServiceMappingItem.md)
- [ DiagRoutineMappingItem ](MappingApi/DiagRoutineMappingItem.md)
- [ DiagServiceMappingItem ](MappingApi/DiagServiceMappingItem.md)
- [ EdiabasVariableMappingItem ](MappingApi/EdiabasVariableMappingItem.md)
- [ EesPinVariableMappingItem ](MappingApi/EesPinVariableMappingItem.md)
- [ EnvSimMappingItem ](MappingApi/EnvSimMappingItem.md)
- [ GenericAudioMappingItem ](MappingApi/GenericAudioMappingItem.md)
- [ GenericImageMappingItem ](MappingApi/GenericImageMappingItem.md)
- [ GenericMappingItem ](MappingApi/GenericMappingItem.md)
- [ GenericPackageMappingItem ](MappingApi/GenericPackageMappingItem.md)
- [ ImageMappingItem ](MappingApi/ImageMappingItem.md)
- [ LogFilterMessageMappingItem ](MappingApi/LogFilterMessageMappingItem.md)
- [ LoggingArgumentMappingItem ](MappingApi/LoggingArgumentMappingItem.md)
- [ MappingItem ](MappingApi/MappingItem.md)
- [ MeasureMappingItem ](MappingApi/MeasureMappingItem.md)
- [ ModelMappingItem ](MappingApi/ModelMappingItem.md)
- [ PackageMappingItem ](MappingApi/PackageMappingItem.md)
- [ PortMappingItem ](MappingApi/PortMappingItem.md)
- [ ReferenceMappingItem ](MappingApi/ReferenceMappingItem.md)
- [ RunningValueMappingItem ](MappingApi/RunningValueMappingItem.md)
- [ ServiceEventLeafMappingItem ](MappingApi/ServiceEventLeafMappingItem.md)
- [ ServiceMappingItem ](MappingApi/ServiceMappingItem.md)
- [ ServiceMethodParameterMappingItem ](MappingApi/ServiceMethodParameterMappingItem.md)
- [ ServiceMethodReturnMappingItem ](MappingApi/ServiceMethodReturnMappingItem.md)
- [ ServiceServiceMappingItem ](MappingApi/ServiceServiceMappingItem.md)

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

[ API for Signal Recordings ](SignalRecordingApi.md)

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

API for Mappings

- [C MappingApi ](#ApiClient.MappingApi)
  - [M CreateAnalysisPackageMappingItem ](#ApiClient.MappingApi.CreateAnalysisPackageMappingItem)
  - [M CreateAudioChannelMappingItem ](#ApiClient.MappingApi.CreateAudioChannelMappingItem)
  - [M CreateAudioDeviceMappingItem ](#ApiClient.MappingApi.CreateAudioDeviceMappingItem)
  - [M CreateBusMonitoringMappingItem ](#ApiClient.MappingApi.CreateBusMonitoringMappingItem)
  - [M CreateBusSignalGroupMappingItem ](#ApiClient.MappingApi.CreateBusSignalGroupMappingItem)
  - [M CreateBusSignalWithPduMappingItem ](#ApiClient.MappingApi.CreateBusSignalWithPduMappingItem)
  - [M CreateCalibrationMappingItem ](#ApiClient.MappingApi.CreateCalibrationMappingItem)
  - [M CreateDebugMappingItem ](#ApiClient.MappingApi.CreateDebugMappingItem)
  - [M CreateDebugRegisterMappingItem ](#ApiClient.MappingApi.CreateDebugRegisterMappingItem)
  - [M CreateDiagDidMappingItem ](#ApiClient.MappingApi.CreateDiagDidMappingItem)
  - [M CreateDiagFaultMemoryMappingItem ](#ApiClient.MappingApi.CreateDiagFaultMemoryMappingItem)
  - [M CreateDiagObdOnUdsServiceMappingItem ](#ApiClient.MappingApi.CreateDiagObdOnUdsServiceMappingItem)
  - [M CreateDiagRoutineMappingItem ](#ApiClient.MappingApi.CreateDiagRoutineMappingItem)
  - [M CreateDiagServiceMappingItem ](#ApiClient.MappingApi.CreateDiagServiceMappingItem)
  - [M CreateEdiabasVariableMappingItem ](#ApiClient.MappingApi.CreateEdiabasVariableMappingItem)
  - [M CreateEesPinVariableMappingItem ](#ApiClient.MappingApi.CreateEesPinVariableMappingItem)
  - [M CreateEnvSimMappingItem ](#ApiClient.MappingApi.CreateEnvSimMappingItem)
  - [M CreateGenericMappingItem ](#ApiClient.MappingApi.CreateGenericMappingItem)
  - [M CreateImageMappingItem ](#ApiClient.MappingApi.CreateImageMappingItem)
  - [M CreateJobMappingItem ](#ApiClient.MappingApi.CreateJobMappingItem)
  - [M CreateLogFilterMessageMappingItem ](#ApiClient.MappingApi.CreateLogFilterMessageMappingItem)
  - [M CreateLoggingArgumentMappingItem ](#ApiClient.MappingApi.CreateLoggingArgumentMappingItem)
  - [M CreateMappingItem ](#ApiClient.MappingApi.CreateMappingItem)
  - [M CreateMeasurementMappingItem ](#ApiClient.MappingApi.CreateMeasurementMappingItem)
  - [M CreateModelMappingItem ](#ApiClient.MappingApi.CreateModelMappingItem)
  - [M CreatePackageMappingItem ](#ApiClient.MappingApi.CreatePackageMappingItem)
  - [M CreatePortMappingItem ](#ApiClient.MappingApi.CreatePortMappingItem)
  - [M CreateReferenceMappingItem ](#ApiClient.MappingApi.CreateReferenceMappingItem)
  - [M CreateRunningValueMappingItem ](#ApiClient.MappingApi.CreateRunningValueMappingItem)
  - [M CreateServiceEventLeafMappingItem ](#ApiClient.MappingApi.CreateServiceEventLeafMappingItem)
  - [M CreateServiceMappingItem ](#ApiClient.MappingApi.CreateServiceMappingItem)
  - [M CreateServiceMethodParameterMappingItem ](#ApiClient.MappingApi.CreateServiceMethodParameterMappingItem)
  - [M CreateServiceMethodReturnMappingItem ](#ApiClient.MappingApi.CreateServiceMethodReturnMappingItem)
  - [M CreateServiceServiceMappingItem ](#ApiClient.MappingApi.CreateServiceServiceMappingItem)
  - [M CreateTraceFileMappingItem ](#ApiClient.MappingApi.CreateTraceFileMappingItem)

# API for Mappings[¶](#api-for-mappings "Link to this heading")

Part of the [Object based program API](objectApi.md#objectapi).

*class* MappingApi[¶](#ApiClient.MappingApi "Link to this definition")  
Returned by

- [`PackageApi.MappingApi`](PackageApi.md#ApiClient.PackageApi.MappingApi "ApiClient.PackageApi.MappingApi (Python attribute) — Returns the MappingApi namespace.")

CreateAnalysisPackageMappingItem(*[pkgPath](#ApiClient.MappingApi.CreateAnalysisPackageMappingItem.pkgPath "ApiClient.MappingApi.CreateAnalysisPackageMappingItem.pkgPath (Python parameter) — Path to the referenced package, either absolute or relative to the packages directory of the current workspace or given namespace, e.g.")*, *[referenceName](#ApiClient.MappingApi.CreateAnalysisPackageMappingItem.referenceName "ApiClient.MappingApi.CreateAnalysisPackageMappingItem.referenceName (Python parameter) — Name of the mapping item")=`None`*, *[namespace](#ApiClient.MappingApi.CreateAnalysisPackageMappingItem.namespace "ApiClient.MappingApi.CreateAnalysisPackageMappingItem.namespace (Python parameter) — Identifier of the workspace to which a relative pkgPath is resolved.")=`None`*, *[checkTarget](#ApiClient.MappingApi.CreateAnalysisPackageMappingItem.checkTarget "ApiClient.MappingApi.CreateAnalysisPackageMappingItem.checkTarget (Python parameter) — Selects if path should be checked")=`True`*)[¶](#ApiClient.MappingApi.CreateAnalysisPackageMappingItem "Link to this definition")  
Creates an analysis package mapping item that references an analysis package (e.g. MyAnalysisPackage.ta). This mapping item can be used for analysis package mapping steps in a project, an analysis package reference in a test case or a referenced trace analysis. These steps do not reference a concrete analysis package. Instead, the implemented analysis label is resolved in the global mapping to get this reference.

Parameters:  pkgPath : str[¶](#ApiClient.MappingApi.CreateAnalysisPackageMappingItem.pkgPath "Permalink to this definition")  
Path to the referenced package, either absolute or relative to the packages directory of the current workspace or given namespace, e.g. ‘MyPackage.pkg’. An absolute path located in the current workspace will also be resolved to a relative workspace reference.

referenceName : str[¶](#ApiClient.MappingApi.CreateAnalysisPackageMappingItem.referenceName "Permalink to this definition")  
Name of the mapping item

namespace : str[¶](#ApiClient.MappingApi.CreateAnalysisPackageMappingItem.namespace "Permalink to this definition")  
Identifier of the workspace to which a relative pkgPath is resolved. If not present or None, the namespace is determined automatically. It is also possible to reference a library workspace using its namespace. A relative pkgPath is resolved relative to the packages directory of the given namespace. For example, the namespace parameter ‘myLibrary’ results in ‘\<libraries.myLibrary.packages\>/MyPackage.pkg’.

checkTarget : boolean[¶](#ApiClient.MappingApi.CreateAnalysisPackageMappingItem.checkTarget "Permalink to this definition")  
Selects if path should be checked

Returns:  The just created mapping item.

Return type:  [`AnalysisPackageMappingItem`](MappingApi/AnalysisPackageMappingItem.md#ApiClient.AnalysisPackageMappingItem "ApiClient.AnalysisPackageMappingItem (Python class) — MappingApi.CreateAnalysisPackageMappingItem")

CreateAudioChannelMappingItem(*[systemIdentifier](#ApiClient.MappingApi.CreateAudioChannelMappingItem.systemIdentifier "ApiClient.MappingApi.CreateAudioChannelMappingItem.systemIdentifier (Python parameter) — Name of the system according to the test configuration.")*, *[channel](#ApiClient.MappingApi.CreateAudioChannelMappingItem.channel "ApiClient.MappingApi.CreateAudioChannelMappingItem.channel (Python parameter) — Number of channel (optional).")=`1`*, *[output](#ApiClient.MappingApi.CreateAudioChannelMappingItem.output "ApiClient.MappingApi.CreateAudioChannelMappingItem.output (Python parameter) — True if this is an output channel")=`False`*, *[referenceName](#ApiClient.MappingApi.CreateAudioChannelMappingItem.referenceName "ApiClient.MappingApi.CreateAudioChannelMappingItem.referenceName (Python parameter) — Name of the mapping item (optional).")=`None`*, *[checkTarget](#ApiClient.MappingApi.CreateAudioChannelMappingItem.checkTarget "ApiClient.MappingApi.CreateAudioChannelMappingItem.checkTarget (Python parameter) — Determines if the target path should be checked (optional).")=`None`*)[¶](#ApiClient.MappingApi.CreateAudioChannelMappingItem "Link to this definition")  
Creates a mapping item pointing at a certain audio channel.

Parameters:  systemIdentifier : str[¶](#ApiClient.MappingApi.CreateAudioChannelMappingItem.systemIdentifier "Permalink to this definition")  
Name of the system according to the test configuration.

channel : int[¶](#ApiClient.MappingApi.CreateAudioChannelMappingItem.channel "Permalink to this definition")  
Number of channel (optional). Uses channel 1 if ommitted.

output : boolean[¶](#ApiClient.MappingApi.CreateAudioChannelMappingItem.output "Permalink to this definition")  
True if this is an output channel

referenceName : str[¶](#ApiClient.MappingApi.CreateAudioChannelMappingItem.referenceName "Permalink to this definition")  
Name of the mapping item (optional).

checkTarget : boolean[¶](#ApiClient.MappingApi.CreateAudioChannelMappingItem.checkTarget "Permalink to this definition")  
Determines if the target path should be checked (optional).

Returns:  The new mapping item

Return type:  [`AudioChannelMappingItem`](MappingApi/AudioChannelMappingItem.md#ApiClient.AudioChannelMappingItem "ApiClient.AudioChannelMappingItem (Python class) — MappingApi.CreateAudioChannelMappingItem")

CreateAudioDeviceMappingItem(*[systemIdentifier](#ApiClient.MappingApi.CreateAudioDeviceMappingItem.systemIdentifier "ApiClient.MappingApi.CreateAudioDeviceMappingItem.systemIdentifier (Python parameter) — Name of the system according to the test configuration.")*, *[referenceName](#ApiClient.MappingApi.CreateAudioDeviceMappingItem.referenceName "ApiClient.MappingApi.CreateAudioDeviceMappingItem.referenceName (Python parameter) — Name of the mapping item (optional).")=`None`*, *[checkTarget](#ApiClient.MappingApi.CreateAudioDeviceMappingItem.checkTarget "ApiClient.MappingApi.CreateAudioDeviceMappingItem.checkTarget (Python parameter) — Determines if the target path should be checked (optional).")=`True`*)[¶](#ApiClient.MappingApi.CreateAudioDeviceMappingItem "Link to this definition")  
Creates a mapping item pointing at a certain audio device.

Parameters:  systemIdentifier : str[¶](#ApiClient.MappingApi.CreateAudioDeviceMappingItem.systemIdentifier "Permalink to this definition")  
Name of the system according to the test configuration.

referenceName : str[¶](#ApiClient.MappingApi.CreateAudioDeviceMappingItem.referenceName "Permalink to this definition")  
Name of the mapping item (optional).

checkTarget : boolean[¶](#ApiClient.MappingApi.CreateAudioDeviceMappingItem.checkTarget "Permalink to this definition")  
Determines if the target path should be checked (optional).

Returns:  The new mapping item

Return type:  [`AudioDeviceMappingItem`](MappingApi/AudioDeviceMappingItem.md#ApiClient.AudioDeviceMappingItem "ApiClient.AudioDeviceMappingItem (Python class) — MappingApi.CreateAudioDeviceMappingItem")

CreateBusMonitoringMappingItem(*[systemIdentifier](#ApiClient.MappingApi.CreateBusMonitoringMappingItem.systemIdentifier "ApiClient.MappingApi.CreateBusMonitoringMappingItem.systemIdentifier (Python parameter) — Name of Bus system according to the test configuration")*, *[nodeName](#ApiClient.MappingApi.CreateBusMonitoringMappingItem.nodeName "ApiClient.MappingApi.CreateBusMonitoringMappingItem.nodeName (Python parameter) — Name of sending ECU")*, *[frameName](#ApiClient.MappingApi.CreateBusMonitoringMappingItem.frameName "ApiClient.MappingApi.CreateBusMonitoringMappingItem.frameName (Python parameter) — Name of the frame containing the signal")*, *[referenceName](#ApiClient.MappingApi.CreateBusMonitoringMappingItem.referenceName "ApiClient.MappingApi.CreateBusMonitoringMappingItem.referenceName (Python parameter) — Name of the mapping item (optional)")=`None`*, *[checkTarget](#ApiClient.MappingApi.CreateBusMonitoringMappingItem.checkTarget "ApiClient.MappingApi.CreateBusMonitoringMappingItem.checkTarget (Python parameter) — Selects if target path should be checked (optional)")=`True`*)[¶](#ApiClient.MappingApi.CreateBusMonitoringMappingItem "Link to this definition")  
Creates a bus monitoring mapping item of the desired variable type.

Parameters:  systemIdentifier : str[¶](#ApiClient.MappingApi.CreateBusMonitoringMappingItem.systemIdentifier "Permalink to this definition")  
Name of Bus system according to the test configuration

nodeName : str[¶](#ApiClient.MappingApi.CreateBusMonitoringMappingItem.nodeName "Permalink to this definition")  
Name of sending ECU

frameName : str[¶](#ApiClient.MappingApi.CreateBusMonitoringMappingItem.frameName "Permalink to this definition")  
Name of the frame containing the signal

referenceName : str[¶](#ApiClient.MappingApi.CreateBusMonitoringMappingItem.referenceName "Permalink to this definition")  
Name of the mapping item (optional)

checkTarget : boolean[¶](#ApiClient.MappingApi.CreateBusMonitoringMappingItem.checkTarget "Permalink to this definition")  
Selects if target path should be checked (optional)

Returns:  The just created mapping item

Return type:  [`BusMonitoringMappingItem`](MappingApi/BusMonitoringMappingItem.md#ApiClient.BusMonitoringMappingItem "ApiClient.BusMonitoringMappingItem (Python class) — MappingApi.CreateBusMonitoringMappingItem")

CreateBusSignalGroupMappingItem(*[systemIdentifier](#ApiClient.MappingApi.CreateBusSignalGroupMappingItem.systemIdentifier "ApiClient.MappingApi.CreateBusSignalGroupMappingItem.systemIdentifier (Python parameter) — Name of Bus system according to the test configuration")*, *[nodeName](#ApiClient.MappingApi.CreateBusSignalGroupMappingItem.nodeName "ApiClient.MappingApi.CreateBusSignalGroupMappingItem.nodeName (Python parameter) — Name of sending ECU (optional)")=`''`*, *[frameName](#ApiClient.MappingApi.CreateBusSignalGroupMappingItem.frameName "ApiClient.MappingApi.CreateBusSignalGroupMappingItem.frameName (Python parameter) — Name of the frame containing the signal (optional)")=`''`*, *[pduName](#ApiClient.MappingApi.CreateBusSignalGroupMappingItem.pduName "ApiClient.MappingApi.CreateBusSignalGroupMappingItem.pduName (Python parameter) — Name of the PDU containing the signal (optional)")=`''`*, *[referenceName](#ApiClient.MappingApi.CreateBusSignalGroupMappingItem.referenceName "ApiClient.MappingApi.CreateBusSignalGroupMappingItem.referenceName (Python parameter) — Name of the mapping item (optional)")=`None`*, *[checkTarget](#ApiClient.MappingApi.CreateBusSignalGroupMappingItem.checkTarget "ApiClient.MappingApi.CreateBusSignalGroupMappingItem.checkTarget (Python parameter) — Selects if target path should be checked (optional)")=`True`*, *[switchCode](#ApiClient.MappingApi.CreateBusSignalGroupMappingItem.switchCode "ApiClient.MappingApi.CreateBusSignalGroupMappingItem.switchCode (Python parameter) — In case the underlying bus database does not support PDU names, switch code can be specified to disambiguate between multiplexed PDUs")=`None`*)[¶](#ApiClient.MappingApi.CreateBusSignalGroupMappingItem "Link to this definition")  
Creates a bus signal group mapping item of the desired variable type.

Parameters:  systemIdentifier : str[¶](#ApiClient.MappingApi.CreateBusSignalGroupMappingItem.systemIdentifier "Permalink to this definition")  
Name of Bus system according to the test configuration

nodeName : str[¶](#ApiClient.MappingApi.CreateBusSignalGroupMappingItem.nodeName "Permalink to this definition")  
Name of sending ECU (optional)

frameName : str[¶](#ApiClient.MappingApi.CreateBusSignalGroupMappingItem.frameName "Permalink to this definition")  
Name of the frame containing the signal (optional)

pduName : str[¶](#ApiClient.MappingApi.CreateBusSignalGroupMappingItem.pduName "Permalink to this definition")  
Name of the PDU containing the signal (optional)

referenceName : str[¶](#ApiClient.MappingApi.CreateBusSignalGroupMappingItem.referenceName "Permalink to this definition")  
Name of the mapping item (optional)

checkTarget : boolean[¶](#ApiClient.MappingApi.CreateBusSignalGroupMappingItem.checkTarget "Permalink to this definition")  
Selects if target path should be checked (optional)

switchCode : int[¶](#ApiClient.MappingApi.CreateBusSignalGroupMappingItem.switchCode "Permalink to this definition")  
In case the underlying bus database does not support PDU names, switch code can be specified to disambiguate between multiplexed PDUs

Returns:  The just created mapping item

Return type:  [`BusSignalGroupMappingItem`](MappingApi/BusSignalGroupMappingItem.md#ApiClient.BusSignalGroupMappingItem "ApiClient.BusSignalGroupMappingItem (Python class) — MappingApi.CreateBusSignalGroupMappingItem")

CreateBusSignalWithPduMappingItem(*[systemIdentifier](#ApiClient.MappingApi.CreateBusSignalWithPduMappingItem.systemIdentifier "ApiClient.MappingApi.CreateBusSignalWithPduMappingItem.systemIdentifier (Python parameter) — Name of Bus system according to the test configuration")*, *[signalName](#ApiClient.MappingApi.CreateBusSignalWithPduMappingItem.signalName "ApiClient.MappingApi.CreateBusSignalWithPduMappingItem.signalName (Python parameter) — Name of the signal")*, *[nodeName](#ApiClient.MappingApi.CreateBusSignalWithPduMappingItem.nodeName "ApiClient.MappingApi.CreateBusSignalWithPduMappingItem.nodeName (Python parameter) — Name of sending ECU (optional)")=`''`*, *[frameName](#ApiClient.MappingApi.CreateBusSignalWithPduMappingItem.frameName "ApiClient.MappingApi.CreateBusSignalWithPduMappingItem.frameName (Python parameter) — Name of the frame containing the signal (optional)")=`''`*, *[pduName](#ApiClient.MappingApi.CreateBusSignalWithPduMappingItem.pduName "ApiClient.MappingApi.CreateBusSignalWithPduMappingItem.pduName (Python parameter) — Name of the PDU containing the signal (optional)")=`''`*, *[referenceName](#ApiClient.MappingApi.CreateBusSignalWithPduMappingItem.referenceName "ApiClient.MappingApi.CreateBusSignalWithPduMappingItem.referenceName (Python parameter) — Name of the mapping item")=`None`*, *[checkTarget](#ApiClient.MappingApi.CreateBusSignalWithPduMappingItem.checkTarget "ApiClient.MappingApi.CreateBusSignalWithPduMappingItem.checkTarget (Python parameter) — Selects if target path should be checked")=`True`*)[¶](#ApiClient.MappingApi.CreateBusSignalWithPduMappingItem "Link to this definition")  
Creates a bus signal mapping item of the desired variable type.

Parameters:  systemIdentifier : str[¶](#ApiClient.MappingApi.CreateBusSignalWithPduMappingItem.systemIdentifier "Permalink to this definition")  
Name of Bus system according to the test configuration

signalName : str[¶](#ApiClient.MappingApi.CreateBusSignalWithPduMappingItem.signalName "Permalink to this definition")  
Name of the signal

nodeName : str[¶](#ApiClient.MappingApi.CreateBusSignalWithPduMappingItem.nodeName "Permalink to this definition")  
Name of sending ECU (optional)

frameName : str[¶](#ApiClient.MappingApi.CreateBusSignalWithPduMappingItem.frameName "Permalink to this definition")  
Name of the frame containing the signal (optional)

pduName : str[¶](#ApiClient.MappingApi.CreateBusSignalWithPduMappingItem.pduName "Permalink to this definition")  
Name of the PDU containing the signal (optional)

referenceName : str[¶](#ApiClient.MappingApi.CreateBusSignalWithPduMappingItem.referenceName "Permalink to this definition")  
Name of the mapping item

checkTarget : boolean[¶](#ApiClient.MappingApi.CreateBusSignalWithPduMappingItem.checkTarget "Permalink to this definition")  
Selects if target path should be checked

Returns:  The just created mapping item

Return type:  [`BusSignalMappingItem`](MappingApi/BusSignalMappingItem.md#ApiClient.BusSignalMappingItem "ApiClient.BusSignalMappingItem (Python class) — MappingApi.CreateBusSignalWithPduMappingItem")

CreateCalibrationMappingItem(*[systemIdentifier](#ApiClient.MappingApi.CreateCalibrationMappingItem.systemIdentifier "ApiClient.MappingApi.CreateCalibrationMappingItem.systemIdentifier (Python parameter) — Name of ECU according to the test configuration")*, *[targetPath](#ApiClient.MappingApi.CreateCalibrationMappingItem.targetPath "ApiClient.MappingApi.CreateCalibrationMappingItem.targetPath (Python parameter) — Name of calibration variable to be accessed")*, *[variableType](#ApiClient.MappingApi.CreateCalibrationMappingItem.variableType "ApiClient.MappingApi.CreateCalibrationMappingItem.variableType (Python parameter) — Type of variable to be mapped (VALUE, VECTOR, MATRIX, CURVE, MAP, VECTOR-ELEMENT, MATRIX-ELEMENT)")=`None`*, *[referenceName](#ApiClient.MappingApi.CreateCalibrationMappingItem.referenceName "ApiClient.MappingApi.CreateCalibrationMappingItem.referenceName (Python parameter) — Name of the mapping item")=`None`*, *[xElement](#ApiClient.MappingApi.CreateCalibrationMappingItem.xElement "ApiClient.MappingApi.CreateCalibrationMappingItem.xElement (Python parameter) — Index on x axis if single element of VECTOR or MATRIX should be accessed")=`None`*, *[yElement](#ApiClient.MappingApi.CreateCalibrationMappingItem.yElement "ApiClient.MappingApi.CreateCalibrationMappingItem.yElement (Python parameter) — Index on y axis if single item of MATRIX should be accessed")=`None`*, *[checkTarget](#ApiClient.MappingApi.CreateCalibrationMappingItem.checkTarget "ApiClient.MappingApi.CreateCalibrationMappingItem.checkTarget (Python parameter) — Selects if target path should be checked")=`True`*)[¶](#ApiClient.MappingApi.CreateCalibrationMappingItem "Link to this definition")  
Creates a calibration mapping item of the desired variable type.

Parameters:  systemIdentifier : str[¶](#ApiClient.MappingApi.CreateCalibrationMappingItem.systemIdentifier "Permalink to this definition")  
Name of ECU according to the test configuration

targetPath : str[¶](#ApiClient.MappingApi.CreateCalibrationMappingItem.targetPath "Permalink to this definition")  
Name of calibration variable to be accessed

variableType : str[¶](#ApiClient.MappingApi.CreateCalibrationMappingItem.variableType "Permalink to this definition")  
Type of variable to be mapped (VALUE, VECTOR, MATRIX, CURVE, MAP, VECTOR-ELEMENT, MATRIX-ELEMENT)

referenceName : str[¶](#ApiClient.MappingApi.CreateCalibrationMappingItem.referenceName "Permalink to this definition")  
Name of the mapping item

xElement : integer[¶](#ApiClient.MappingApi.CreateCalibrationMappingItem.xElement "Permalink to this definition")  
Index on x axis if single element of VECTOR or MATRIX should be accessed

yElement : integer[¶](#ApiClient.MappingApi.CreateCalibrationMappingItem.yElement "Permalink to this definition")  
Index on y axis if single item of MATRIX should be accessed

checkTarget : boolean[¶](#ApiClient.MappingApi.CreateCalibrationMappingItem.checkTarget "Permalink to this definition")  
Selects if target path should be checked

Returns:  The just created mapping item

Return type:  [`CalibrationMappingItem`](MappingApi/CalibrationMappingItem.md#ApiClient.CalibrationMappingItem "ApiClient.CalibrationMappingItem (Python class) — MappingApi.CreateCalibrationMappingItem")

CreateDebugMappingItem(*[ecuKey](#ApiClient.MappingApi.CreateDebugMappingItem.ecuKey "ApiClient.MappingApi.CreateDebugMappingItem.ecuKey (Python parameter) — Name of the ECU")*, *[targetPath](#ApiClient.MappingApi.CreateDebugMappingItem.targetPath "ApiClient.MappingApi.CreateDebugMappingItem.targetPath (Python parameter) — Path to the debug variable to be accessed")*, *[variableType](#ApiClient.MappingApi.CreateDebugMappingItem.variableType "ApiClient.MappingApi.CreateDebugMappingItem.variableType (Python parameter) — Type of variable to be mapped (VALUE, VECTOR, MATRIX)")=`None`*, *[referenceName](#ApiClient.MappingApi.CreateDebugMappingItem.referenceName "ApiClient.MappingApi.CreateDebugMappingItem.referenceName (Python parameter) — Name of the mapping item (optional)")=`None`*, *[checkTarget](#ApiClient.MappingApi.CreateDebugMappingItem.checkTarget "ApiClient.MappingApi.CreateDebugMappingItem.checkTarget (Python parameter) — Selects if target path should be checked")=`True`*)[¶](#ApiClient.MappingApi.CreateDebugMappingItem "Link to this definition")  
Creates a debug mapping item.

Parameters:  ecuKey : str[¶](#ApiClient.MappingApi.CreateDebugMappingItem.ecuKey "Permalink to this definition")  
Name of the ECU

targetPath : str[¶](#ApiClient.MappingApi.CreateDebugMappingItem.targetPath "Permalink to this definition")  
Path to the debug variable to be accessed

variableType : str[¶](#ApiClient.MappingApi.CreateDebugMappingItem.variableType "Permalink to this definition")  
Type of variable to be mapped (VALUE, VECTOR, MATRIX)

referenceName : str[¶](#ApiClient.MappingApi.CreateDebugMappingItem.referenceName "Permalink to this definition")  
Name of the mapping item (optional)

checkTarget : boolean[¶](#ApiClient.MappingApi.CreateDebugMappingItem.checkTarget "Permalink to this definition")  
Selects if target path should be checked

Returns:  The just created mapping item

Return type:  [`DebugMappingItem`](MappingApi/DebugMappingItem.md#ApiClient.DebugMappingItem "ApiClient.DebugMappingItem (Python class) — Interface of MappingItems for debugging variables. Debugging registers have their own interface.")

CreateDebugRegisterMappingItem(*[ecuKey](#ApiClient.MappingApi.CreateDebugRegisterMappingItem.ecuKey "ApiClient.MappingApi.CreateDebugRegisterMappingItem.ecuKey (Python parameter) — Name of the ECU")*, *[targetPath](#ApiClient.MappingApi.CreateDebugRegisterMappingItem.targetPath "ApiClient.MappingApi.CreateDebugRegisterMappingItem.targetPath (Python parameter) — Path to the register variable to be accessed")*, *[referenceName](#ApiClient.MappingApi.CreateDebugRegisterMappingItem.referenceName "ApiClient.MappingApi.CreateDebugRegisterMappingItem.referenceName (Python parameter) — Name of the mapping item (optional)")=`None`*, *[checkTarget](#ApiClient.MappingApi.CreateDebugRegisterMappingItem.checkTarget "ApiClient.MappingApi.CreateDebugRegisterMappingItem.checkTarget (Python parameter) — Selects if target path should be checked")=`True`*)[¶](#ApiClient.MappingApi.CreateDebugRegisterMappingItem "Link to this definition")  
Creates a debug register mapping item.

Parameters:  ecuKey : str[¶](#ApiClient.MappingApi.CreateDebugRegisterMappingItem.ecuKey "Permalink to this definition")  
Name of the ECU

targetPath : str[¶](#ApiClient.MappingApi.CreateDebugRegisterMappingItem.targetPath "Permalink to this definition")  
Path to the register variable to be accessed

referenceName : str[¶](#ApiClient.MappingApi.CreateDebugRegisterMappingItem.referenceName "Permalink to this definition")  
Name of the mapping item (optional)

checkTarget : boolean[¶](#ApiClient.MappingApi.CreateDebugRegisterMappingItem.checkTarget "Permalink to this definition")  
Selects if target path should be checked

Returns:  The just created mapping item

Return type:  [`DebugRegisterMappingItem`](MappingApi/DebugRegisterMappingItem.md#ApiClient.DebugRegisterMappingItem "ApiClient.DebugRegisterMappingItem (Python class) — Interface of MappingItems for debugging registers.")

CreateDiagDidMappingItem(*[systemIdentifier](#ApiClient.MappingApi.CreateDiagDidMappingItem.systemIdentifier "ApiClient.MappingApi.CreateDiagDidMappingItem.systemIdentifier (Python parameter) — Name of the ECU according to the test configuration")*, *[name](#ApiClient.MappingApi.CreateDiagDidMappingItem.name "ApiClient.MappingApi.CreateDiagDidMappingItem.name (Python parameter) — Name of the DIAG DID signal")*, *[referenceName](#ApiClient.MappingApi.CreateDiagDidMappingItem.referenceName "ApiClient.MappingApi.CreateDiagDidMappingItem.referenceName (Python parameter) — Name of the mapping item")=`None`*, *[checkTarget](#ApiClient.MappingApi.CreateDiagDidMappingItem.checkTarget "ApiClient.MappingApi.CreateDiagDidMappingItem.checkTarget (Python parameter) — Selects if target path should be checked")=`True`*)[¶](#ApiClient.MappingApi.CreateDiagDidMappingItem "Link to this definition")  
Creates DIAG DID mapping item.

Parameters:  systemIdentifier : str[¶](#ApiClient.MappingApi.CreateDiagDidMappingItem.systemIdentifier "Permalink to this definition")  
Name of the ECU according to the test configuration

name : str[¶](#ApiClient.MappingApi.CreateDiagDidMappingItem.name "Permalink to this definition")  
Name of the DIAG DID signal

referenceName : str[¶](#ApiClient.MappingApi.CreateDiagDidMappingItem.referenceName "Permalink to this definition")  
Name of the mapping item

checkTarget : boolean[¶](#ApiClient.MappingApi.CreateDiagDidMappingItem.checkTarget "Permalink to this definition")  
Selects if target path should be checked

Returns:  The just created mapping item

Return type:  [`DiagDidMappingItem`](MappingApi/DiagDidMappingItem.md#ApiClient.DiagDidMappingItem "ApiClient.DiagDidMappingItem (Python class) — MappingApi.CreateDiagDidMappingItem")

CreateDiagFaultMemoryMappingItem(*[ecuKey](#ApiClient.MappingApi.CreateDiagFaultMemoryMappingItem.ecuKey "ApiClient.MappingApi.CreateDiagFaultMemoryMappingItem.ecuKey (Python parameter) — Name of the ECU")*, *[referenceName](#ApiClient.MappingApi.CreateDiagFaultMemoryMappingItem.referenceName "ApiClient.MappingApi.CreateDiagFaultMemoryMappingItem.referenceName (Python parameter) — Name of the mapping item (optional)")=`None`*)[¶](#ApiClient.MappingApi.CreateDiagFaultMemoryMappingItem "Link to this definition")  
Creates a fault memory mapping item.

Parameters:  ecuKey : str[¶](#ApiClient.MappingApi.CreateDiagFaultMemoryMappingItem.ecuKey "Permalink to this definition")  
Name of the ECU

referenceName : str[¶](#ApiClient.MappingApi.CreateDiagFaultMemoryMappingItem.referenceName "Permalink to this definition")  
Name of the mapping item (optional)

Returns:  The just created mapping item

Return type:  [`DiagFaultMemoryMappingItem`](MappingApi/DiagFaultMemoryMappingItem.md#ApiClient.DiagFaultMemoryMappingItem "ApiClient.DiagFaultMemoryMappingItem (Python class) — MappingApi.CreateDiagFaultMemoryMappingItem")

CreateDiagObdOnUdsServiceMappingItem(*[systemIdentifier](#ApiClient.MappingApi.CreateDiagObdOnUdsServiceMappingItem.systemIdentifier "ApiClient.MappingApi.CreateDiagObdOnUdsServiceMappingItem.systemIdentifier (Python parameter) — Name of the ECU according to the test configuration")*, *[name](#ApiClient.MappingApi.CreateDiagObdOnUdsServiceMappingItem.name "ApiClient.MappingApi.CreateDiagObdOnUdsServiceMappingItem.name (Python parameter) — Name of the DIAG service")*, *[referenceName](#ApiClient.MappingApi.CreateDiagObdOnUdsServiceMappingItem.referenceName "ApiClient.MappingApi.CreateDiagObdOnUdsServiceMappingItem.referenceName (Python parameter) — Name of the mapping item")=`None`*, *[checkTarget](#ApiClient.MappingApi.CreateDiagObdOnUdsServiceMappingItem.checkTarget "ApiClient.MappingApi.CreateDiagObdOnUdsServiceMappingItem.checkTarget (Python parameter) — Selects if target path should be checked")=`True`*)[¶](#ApiClient.MappingApi.CreateDiagObdOnUdsServiceMappingItem "Link to this definition")  
Creates a OBD Service mapping item.

Parameters:  systemIdentifier : str[¶](#ApiClient.MappingApi.CreateDiagObdOnUdsServiceMappingItem.systemIdentifier "Permalink to this definition")  
Name of the ECU according to the test configuration

name : str[¶](#ApiClient.MappingApi.CreateDiagObdOnUdsServiceMappingItem.name "Permalink to this definition")  
Name of the DIAG service

referenceName : str[¶](#ApiClient.MappingApi.CreateDiagObdOnUdsServiceMappingItem.referenceName "Permalink to this definition")  
Name of the mapping item

checkTarget : bool[¶](#ApiClient.MappingApi.CreateDiagObdOnUdsServiceMappingItem.checkTarget "Permalink to this definition")  
Selects if target path should be checked

Returns:  The just created mapping item

Return type:  [`DiagObdOnUdsServiceMappingItem`](MappingApi/DiagObdOnUdsServiceMappingItem.md#ApiClient.DiagObdOnUdsServiceMappingItem "ApiClient.DiagObdOnUdsServiceMappingItem (Python class) — MappingApi.CreateDiagObdOnUdsServiceMappingItem")

CreateDiagRoutineMappingItem(*[systemIdentifier](#ApiClient.MappingApi.CreateDiagRoutineMappingItem.systemIdentifier "ApiClient.MappingApi.CreateDiagRoutineMappingItem.systemIdentifier (Python parameter) — Name of the ECU according to the test configuration")*, *[name](#ApiClient.MappingApi.CreateDiagRoutineMappingItem.name "ApiClient.MappingApi.CreateDiagRoutineMappingItem.name (Python parameter) — Name of the DIAG RoutineControl")*, *[referenceName](#ApiClient.MappingApi.CreateDiagRoutineMappingItem.referenceName "ApiClient.MappingApi.CreateDiagRoutineMappingItem.referenceName (Python parameter) — Name of the mapping item")=`None`*, *[checkTarget](#ApiClient.MappingApi.CreateDiagRoutineMappingItem.checkTarget "ApiClient.MappingApi.CreateDiagRoutineMappingItem.checkTarget (Python parameter) — Selects if target path should be checked")=`True`*)[¶](#ApiClient.MappingApi.CreateDiagRoutineMappingItem "Link to this definition")  
Creates DIAG RoutineControl mapping item.

Parameters:  systemIdentifier : str[¶](#ApiClient.MappingApi.CreateDiagRoutineMappingItem.systemIdentifier "Permalink to this definition")  
Name of the ECU according to the test configuration

name : str[¶](#ApiClient.MappingApi.CreateDiagRoutineMappingItem.name "Permalink to this definition")  
Name of the DIAG RoutineControl

referenceName : str[¶](#ApiClient.MappingApi.CreateDiagRoutineMappingItem.referenceName "Permalink to this definition")  
Name of the mapping item

checkTarget : boolean[¶](#ApiClient.MappingApi.CreateDiagRoutineMappingItem.checkTarget "Permalink to this definition")  
Selects if target path should be checked

Returns:  The just created mapping item

Return type:  [`DiagRoutineMappingItem`](MappingApi/DiagRoutineMappingItem.md#ApiClient.DiagRoutineMappingItem "ApiClient.DiagRoutineMappingItem (Python class) — MappingApi.CreateDiagRoutineMappingItem")

CreateDiagServiceMappingItem(*[systemIdentifier](#ApiClient.MappingApi.CreateDiagServiceMappingItem.systemIdentifier "ApiClient.MappingApi.CreateDiagServiceMappingItem.systemIdentifier (Python parameter) — Name of the ECU according to the test configuration")*, *[name](#ApiClient.MappingApi.CreateDiagServiceMappingItem.name "ApiClient.MappingApi.CreateDiagServiceMappingItem.name (Python parameter) — Name of the DIAG service")*, *[protocol](#ApiClient.MappingApi.CreateDiagServiceMappingItem.protocol "ApiClient.MappingApi.CreateDiagServiceMappingItem.protocol (Python parameter) — Protocol (0 - UDS, 1 - KWP_2000)")=`0`*, *[referenceName](#ApiClient.MappingApi.CreateDiagServiceMappingItem.referenceName "ApiClient.MappingApi.CreateDiagServiceMappingItem.referenceName (Python parameter) — Name of the mapping item")=`None`*, *[checkTarget](#ApiClient.MappingApi.CreateDiagServiceMappingItem.checkTarget "ApiClient.MappingApi.CreateDiagServiceMappingItem.checkTarget (Python parameter) — Selects if target path should be checked")=`True`*)[¶](#ApiClient.MappingApi.CreateDiagServiceMappingItem "Link to this definition")  
Creates a DIAG Service mapping item.

Parameters:  systemIdentifier : str[¶](#ApiClient.MappingApi.CreateDiagServiceMappingItem.systemIdentifier "Permalink to this definition")  
Name of the ECU according to the test configuration

name : str[¶](#ApiClient.MappingApi.CreateDiagServiceMappingItem.name "Permalink to this definition")  
Name of the DIAG service

protocol : int[¶](#ApiClient.MappingApi.CreateDiagServiceMappingItem.protocol "Permalink to this definition")  
Protocol (0 - UDS, 1 - KWP_2000)

referenceName : str[¶](#ApiClient.MappingApi.CreateDiagServiceMappingItem.referenceName "Permalink to this definition")  
Name of the mapping item

checkTarget : bool[¶](#ApiClient.MappingApi.CreateDiagServiceMappingItem.checkTarget "Permalink to this definition")  
Selects if target path should be checked

Returns:  The just created mapping item

Return type:  [`DiagServiceMappingItem`](MappingApi/DiagServiceMappingItem.md#ApiClient.DiagServiceMappingItem "ApiClient.DiagServiceMappingItem (Python class) — MappingApi.CreateDiagServiceMappingItem")

CreateEdiabasVariableMappingItem(*[ecuKey](#ApiClient.MappingApi.CreateEdiabasVariableMappingItem.ecuKey "ApiClient.MappingApi.CreateEdiabasVariableMappingItem.ecuKey (Python parameter) — Name of the ECU")*, *[job](#ApiClient.MappingApi.CreateEdiabasVariableMappingItem.job "ApiClient.MappingApi.CreateEdiabasVariableMappingItem.job (Python parameter) — Name of the job")*, *[referenceName](#ApiClient.MappingApi.CreateEdiabasVariableMappingItem.referenceName "ApiClient.MappingApi.CreateEdiabasVariableMappingItem.referenceName (Python parameter) — Name of the mapping item (optional)")=`None`*, *[checkTarget](#ApiClient.MappingApi.CreateEdiabasVariableMappingItem.checkTarget "ApiClient.MappingApi.CreateEdiabasVariableMappingItem.checkTarget (Python parameter) — Selects if the target path and the job should be checked (optional)")=`True`*)[¶](#ApiClient.MappingApi.CreateEdiabasVariableMappingItem "Link to this definition")  
Creates an ediabas variable mapping item.

Parameters:  ecuKey : str[¶](#ApiClient.MappingApi.CreateEdiabasVariableMappingItem.ecuKey "Permalink to this definition")  
Name of the ECU

job : str[¶](#ApiClient.MappingApi.CreateEdiabasVariableMappingItem.job "Permalink to this definition")  
Name of the job

referenceName : str[¶](#ApiClient.MappingApi.CreateEdiabasVariableMappingItem.referenceName "Permalink to this definition")  
Name of the mapping item (optional)

checkTarget : boolean[¶](#ApiClient.MappingApi.CreateEdiabasVariableMappingItem.checkTarget "Permalink to this definition")  
Selects if the target path and the job should be checked (optional)

Returns:  The just created mapping item

Return type:  [`EdiabasVariableMappingItem`](MappingApi/EdiabasVariableMappingItem.md#ApiClient.EdiabasVariableMappingItem "ApiClient.EdiabasVariableMappingItem (Python class) — MappingApi.CreateEdiabasVariableMappingItem")

CreateEesPinVariableMappingItem(*[systemIdentifier](#ApiClient.MappingApi.CreateEesPinVariableMappingItem.systemIdentifier "ApiClient.MappingApi.CreateEesPinVariableMappingItem.systemIdentifier (Python parameter) — SUT key")*, *[name](#ApiClient.MappingApi.CreateEesPinVariableMappingItem.name "ApiClient.MappingApi.CreateEesPinVariableMappingItem.name (Python parameter) — Name of the signal")*, *[referenceName](#ApiClient.MappingApi.CreateEesPinVariableMappingItem.referenceName "ApiClient.MappingApi.CreateEesPinVariableMappingItem.referenceName (Python parameter) — Name of the mapping item (optional)")=`None`*, *[checkTarget](#ApiClient.MappingApi.CreateEesPinVariableMappingItem.checkTarget "ApiClient.MappingApi.CreateEesPinVariableMappingItem.checkTarget (Python parameter) — Selects if target path should be checked (optional)")=`True`*)[¶](#ApiClient.MappingApi.CreateEesPinVariableMappingItem "Link to this definition")  
Creates an ees pin variable mapping item.

Parameters:  systemIdentifier : str[¶](#ApiClient.MappingApi.CreateEesPinVariableMappingItem.systemIdentifier "Permalink to this definition")  
SUT key

name : str[¶](#ApiClient.MappingApi.CreateEesPinVariableMappingItem.name "Permalink to this definition")  
Name of the signal

referenceName : str[¶](#ApiClient.MappingApi.CreateEesPinVariableMappingItem.referenceName "Permalink to this definition")  
Name of the mapping item (optional)

checkTarget : boolean[¶](#ApiClient.MappingApi.CreateEesPinVariableMappingItem.checkTarget "Permalink to this definition")  
Selects if target path should be checked (optional)

Returns:  The just created mapping item

Return type:  [`EesPinVariableMappingItem`](MappingApi/EesPinVariableMappingItem.md#ApiClient.EesPinVariableMappingItem "ApiClient.EesPinVariableMappingItem (Python class) — MappingApi.CreateEesPinVariableMappingItem")

CreateEnvSimMappingItem(*[systemIdentifier](#ApiClient.MappingApi.CreateEnvSimMappingItem.systemIdentifier "ApiClient.MappingApi.CreateEnvSimMappingItem.systemIdentifier (Python parameter) — Name of system according to the test configuration, e.g.")*, *[targetPath](#ApiClient.MappingApi.CreateEnvSimMappingItem.targetPath "ApiClient.MappingApi.CreateEnvSimMappingItem.targetPath (Python parameter) — Path to the model variable to be accessed, e.g.")*, *[variableType](#ApiClient.MappingApi.CreateEnvSimMappingItem.variableType "ApiClient.MappingApi.CreateEnvSimMappingItem.variableType (Python parameter) — Type of variable to be mapped (VALUE, VECTOR, MATRIX)")=`None`*, *[isSignal](#ApiClient.MappingApi.CreateEnvSimMappingItem.isSignal "ApiClient.MappingApi.CreateEnvSimMappingItem.isSignal (Python parameter) — Selects if the mapping item should point to a model signal instead of variable")=`False`*, *[referenceName](#ApiClient.MappingApi.CreateEnvSimMappingItem.referenceName "ApiClient.MappingApi.CreateEnvSimMappingItem.referenceName (Python parameter) — Name of the mapping item")=`None`*, *[checkTarget](#ApiClient.MappingApi.CreateEnvSimMappingItem.checkTarget "ApiClient.MappingApi.CreateEnvSimMappingItem.checkTarget (Python parameter) — Selects if target path should be checked")=`True`*)[¶](#ApiClient.MappingApi.CreateEnvSimMappingItem "Link to this definition")  
Creates a mapping item of the desired variable type pointing at a certain envsim variable. The envsim has to be loaded in order to create a envsim mapping item.

Parameters:  systemIdentifier : str[¶](#ApiClient.MappingApi.CreateEnvSimMappingItem.systemIdentifier "Permalink to this definition")  
Name of system according to the test configuration, e.g. “Plant model”

targetPath : str[¶](#ApiClient.MappingApi.CreateEnvSimMappingItem.targetPath "Permalink to this definition")  
Path to the model variable to be accessed, e.g. “Model Root/varName”.

variableType : str[¶](#ApiClient.MappingApi.CreateEnvSimMappingItem.variableType "Permalink to this definition")  
Type of variable to be mapped (VALUE, VECTOR, MATRIX)

isSignal : boolean[¶](#ApiClient.MappingApi.CreateEnvSimMappingItem.isSignal "Permalink to this definition")  
Selects if the mapping item should point to a model signal instead of variable

referenceName : str[¶](#ApiClient.MappingApi.CreateEnvSimMappingItem.referenceName "Permalink to this definition")  
Name of the mapping item

checkTarget : boolean[¶](#ApiClient.MappingApi.CreateEnvSimMappingItem.checkTarget "Permalink to this definition")  
Selects if target path should be checked

Returns:  The just created mapping item

Return type:  [`EnvSimMappingItem`](MappingApi/EnvSimMappingItem.md#ApiClient.EnvSimMappingItem "ApiClient.EnvSimMappingItem (Python class) — MappingApi.CreateEnvSimMappingItem")

CreateGenericMappingItem(*[variableType](#ApiClient.MappingApi.CreateGenericMappingItem.variableType "ApiClient.MappingApi.CreateGenericMappingItem.variableType (Python parameter) — Type of variable to be mapped (VALUE, VECTOR, CURVE, MATRIX, MAP, IMAGE, AUDIO, JOB, PACKAGE)")=`None`*, *[referenceName](#ApiClient.MappingApi.CreateGenericMappingItem.referenceName "ApiClient.MappingApi.CreateGenericMappingItem.referenceName (Python parameter) — Name of the mapping item")=`None`*)[¶](#ApiClient.MappingApi.CreateGenericMappingItem "Link to this definition")  
Creates a generic mapping item of the desired variable type.

Parameters:  variableType : str[¶](#ApiClient.MappingApi.CreateGenericMappingItem.variableType "Permalink to this definition")  
Type of variable to be mapped (VALUE, VECTOR, CURVE, MATRIX, MAP, IMAGE, AUDIO, JOB, PACKAGE)

referenceName : str[¶](#ApiClient.MappingApi.CreateGenericMappingItem.referenceName "Permalink to this definition")  
Name of the mapping item

Returns:  The just created mapping item

Return type:  [`MappingItem`](MappingApi/MappingItem.md#ApiClient.MappingItem "ApiClient.MappingItem (Python class) — MappingApi.CreateGenericMappingItem")

CreateImageMappingItem(*[systemIdentifier](#ApiClient.MappingApi.CreateImageMappingItem.systemIdentifier "ApiClient.MappingApi.CreateImageMappingItem.systemIdentifier (Python parameter) — Name of system according to the test configuration, e.g.")*, *[targetPath](#ApiClient.MappingApi.CreateImageMappingItem.targetPath "ApiClient.MappingApi.CreateImageMappingItem.targetPath (Python parameter) — Path to the image variable to be accessed, e.g.")*, *[maskPath](#ApiClient.MappingApi.CreateImageMappingItem.maskPath "ApiClient.MappingApi.CreateImageMappingItem.maskPath (Python parameter) — The name of the mask, submask and index to use, e.g.")=`''`*, *[referenceName](#ApiClient.MappingApi.CreateImageMappingItem.referenceName "ApiClient.MappingApi.CreateImageMappingItem.referenceName (Python parameter) — Name of the mapping item")=`None`*, *[checkTarget](#ApiClient.MappingApi.CreateImageMappingItem.checkTarget "ApiClient.MappingApi.CreateImageMappingItem.checkTarget (Python parameter) — Selects if target path should be checked")=`True`*)[¶](#ApiClient.MappingApi.CreateImageMappingItem "Link to this definition")  
Creates a mapping item pointing at a certain image variable.

Parameters:  systemIdentifier : str[¶](#ApiClient.MappingApi.CreateImageMappingItem.systemIdentifier "Permalink to this definition")  
Name of system according to the test configuration, e.g. “CAM”

targetPath : str[¶](#ApiClient.MappingApi.CreateImageMappingItem.targetPath "Permalink to this definition")  
Path to the image variable to be accessed, e.g. “Image” to read the whole image. To access a mask in a subfolder, the path to that folder must also be specified here, e.g. “Image/mymasks/moremasks/”. The actual name of the mask (and submask) however is specified in the parameter `maskPath`.

maskPath : str[¶](#ApiClient.MappingApi.CreateImageMappingItem.maskPath "Permalink to this definition")  
The name of the mask, submask and index to use, e.g. “MyMask[1, 1]/icon” would refer to the submask “icon” of index [1, 1] of the mask “MyMask”.

referenceName : str[¶](#ApiClient.MappingApi.CreateImageMappingItem.referenceName "Permalink to this definition")  
Name of the mapping item

checkTarget : boolean[¶](#ApiClient.MappingApi.CreateImageMappingItem.checkTarget "Permalink to this definition")  
Selects if target path should be checked

Returns:  The just created mapping item

Return type:  [`ImageMappingItem`](MappingApi/ImageMappingItem.md#ApiClient.ImageMappingItem "ApiClient.ImageMappingItem (Python class) — MappingApi.CreateImageMappingItem")

CreateJobMappingItem(*[toolId](#ApiClient.MappingApi.CreateJobMappingItem.toolId "ApiClient.MappingApi.CreateJobMappingItem.toolId (Python parameter) — Name of the used tool")*, *[jobName](#ApiClient.MappingApi.CreateJobMappingItem.jobName "ApiClient.MappingApi.CreateJobMappingItem.jobName (Python parameter) — Name of the job")*, *[portId](#ApiClient.MappingApi.CreateJobMappingItem.portId "ApiClient.MappingApi.CreateJobMappingItem.portId (Python parameter) — Name of the port")=`None`*, *[checkTarget](#ApiClient.MappingApi.CreateJobMappingItem.checkTarget "ApiClient.MappingApi.CreateJobMappingItem.checkTarget (Python parameter) — Selects if target path should be checked")=`True`*, *[referenceName](#ApiClient.MappingApi.CreateJobMappingItem.referenceName "ApiClient.MappingApi.CreateJobMappingItem.referenceName (Python parameter) — Name of the mapping item")=`None`*)[¶](#ApiClient.MappingApi.CreateJobMappingItem "Link to this definition")  
Creates a tool job or port job mapping item.

Parameters:  toolId : str[¶](#ApiClient.MappingApi.CreateJobMappingItem.toolId "Permalink to this definition")  
Name of the used tool

jobName : str[¶](#ApiClient.MappingApi.CreateJobMappingItem.jobName "Permalink to this definition")  
Name of the job

portId : str[¶](#ApiClient.MappingApi.CreateJobMappingItem.portId "Permalink to this definition")  
Name of the port

checkTarget : boolean[¶](#ApiClient.MappingApi.CreateJobMappingItem.checkTarget "Permalink to this definition")  
Selects if target path should be checked

referenceName : str[¶](#ApiClient.MappingApi.CreateJobMappingItem.referenceName "Permalink to this definition")  
Name of the mapping item

Returns:  The just created mapping item

Return type:  [`MappingItem`](MappingApi/MappingItem.md#ApiClient.MappingItem "ApiClient.MappingItem (Python class) — MappingApi.CreateGenericMappingItem")

CreateLogFilterMessageMappingItem(*[ecuKey](#ApiClient.MappingApi.CreateLogFilterMessageMappingItem.ecuKey "ApiClient.MappingApi.CreateLogFilterMessageMappingItem.ecuKey (Python parameter) — name of the ECU for which the filter has been loaded")*, *[messageName](#ApiClient.MappingApi.CreateLogFilterMessageMappingItem.messageName "ApiClient.MappingApi.CreateLogFilterMessageMappingItem.messageName (Python parameter) — name of the message filter")*, *[referenceName](#ApiClient.MappingApi.CreateLogFilterMessageMappingItem.referenceName "ApiClient.MappingApi.CreateLogFilterMessageMappingItem.referenceName (Python parameter) — Name of the mapping item")=`None`*, *[checkTarget](#ApiClient.MappingApi.CreateLogFilterMessageMappingItem.checkTarget "ApiClient.MappingApi.CreateLogFilterMessageMappingItem.checkTarget (Python parameter) — Selects if target path should be checked")=`True`*)[¶](#ApiClient.MappingApi.CreateLogFilterMessageMappingItem "Link to this definition")  
Creates a DLT log filter mapping item.

Parameters:  ecuKey : str[¶](#ApiClient.MappingApi.CreateLogFilterMessageMappingItem.ecuKey "Permalink to this definition")  
name of the ECU for which the filter has been loaded

messageName : str[¶](#ApiClient.MappingApi.CreateLogFilterMessageMappingItem.messageName "Permalink to this definition")  
name of the message filter

referenceName : str[¶](#ApiClient.MappingApi.CreateLogFilterMessageMappingItem.referenceName "Permalink to this definition")  
Name of the mapping item

checkTarget : boolean[¶](#ApiClient.MappingApi.CreateLogFilterMessageMappingItem.checkTarget "Permalink to this definition")  
Selects if target path should be checked

Returns:  The just created mapping item

Return type:  [`LogFilterMessageMappingItem`](MappingApi/LogFilterMessageMappingItem.md#ApiClient.LogFilterMessageMappingItem "ApiClient.LogFilterMessageMappingItem (Python class) — MappingApi.CreateLogFilterMessageMappingItem")

CreateLoggingArgumentMappingItem(*[systemIdentifier](#ApiClient.MappingApi.CreateLoggingArgumentMappingItem.systemIdentifier "ApiClient.MappingApi.CreateLoggingArgumentMappingItem.systemIdentifier (Python parameter) — Name of logging system according to the test configuration")*, *[messageName](#ApiClient.MappingApi.CreateLoggingArgumentMappingItem.messageName "ApiClient.MappingApi.CreateLoggingArgumentMappingItem.messageName (Python parameter) — Name of the message containing the argument")*, *[argumentName](#ApiClient.MappingApi.CreateLoggingArgumentMappingItem.argumentName "ApiClient.MappingApi.CreateLoggingArgumentMappingItem.argumentName (Python parameter) — Name of the message argument")*, *[referenceName](#ApiClient.MappingApi.CreateLoggingArgumentMappingItem.referenceName "ApiClient.MappingApi.CreateLoggingArgumentMappingItem.referenceName (Python parameter) — Name of the mapping item")=`None`*, *[checkTarget](#ApiClient.MappingApi.CreateLoggingArgumentMappingItem.checkTarget "ApiClient.MappingApi.CreateLoggingArgumentMappingItem.checkTarget (Python parameter) — Selects if target path should be checked")=`True`*)[¶](#ApiClient.MappingApi.CreateLoggingArgumentMappingItem "Link to this definition")  
Creates a logging argument mapping item.

Parameters:  systemIdentifier : str[¶](#ApiClient.MappingApi.CreateLoggingArgumentMappingItem.systemIdentifier "Permalink to this definition")  
Name of logging system according to the test configuration

messageName : str[¶](#ApiClient.MappingApi.CreateLoggingArgumentMappingItem.messageName "Permalink to this definition")  
Name of the message containing the argument

argumentName : str[¶](#ApiClient.MappingApi.CreateLoggingArgumentMappingItem.argumentName "Permalink to this definition")  
Name of the message argument

referenceName : str[¶](#ApiClient.MappingApi.CreateLoggingArgumentMappingItem.referenceName "Permalink to this definition")  
Name of the mapping item

checkTarget : boolean[¶](#ApiClient.MappingApi.CreateLoggingArgumentMappingItem.checkTarget "Permalink to this definition")  
Selects if target path should be checked

Returns:  The just created mapping item

Return type:  [`LoggingArgumentMappingItem`](MappingApi/LoggingArgumentMappingItem.md#ApiClient.LoggingArgumentMappingItem "ApiClient.LoggingArgumentMappingItem (Python class) — MappingApi.CreateLoggingArgumentMappingItem")

CreateMappingItem(*[systemIdentifier](#ApiClient.MappingApi.CreateMappingItem.systemIdentifier "ApiClient.MappingApi.CreateMappingItem.systemIdentifier (Python parameter) — Name of system according to the test configuration")*, *[targetPath](#ApiClient.MappingApi.CreateMappingItem.targetPath "ApiClient.MappingApi.CreateMappingItem.targetPath (Python parameter) — Name of bus, model, calibration or measure variable to be accessed (Needs indices if datatype is VECTOR-ELEMENT label[idx_X] or if datatype is MATRIX-ELEMENT label[idx_X][idx_Y])")*, *[referenceName](#ApiClient.MappingApi.CreateMappingItem.referenceName "ApiClient.MappingApi.CreateMappingItem.referenceName (Python parameter) — Name of the mapping item")=`None`*)[¶](#ApiClient.MappingApi.CreateMappingItem "Link to this definition")  
Creates a mapping item with automatically determined type.

The desired mapping target needs to exist in the currently loaded/activated configuration!

Parameters:  systemIdentifier : str[¶](#ApiClient.MappingApi.CreateMappingItem.systemIdentifier "Permalink to this definition")  
Name of system according to the test configuration

targetPath : str[¶](#ApiClient.MappingApi.CreateMappingItem.targetPath "Permalink to this definition")  
Name of bus, model, calibration or measure variable to be accessed (Needs indices if datatype is VECTOR-ELEMENT label[idx_X] or if datatype is MATRIX-ELEMENT label[idx_X][idx_Y])

Bus signals need a target path of the following form: “\<nodeName\>/\<frameName\>/\<pduName\>/\<signalName\>” Note: \<nodeName\>, \<frameName\> and \<pduName\> are optional, that means ///\<signalName\> is also valid. Logging arguments need a target path of the form: “/\<messageName\>/\<argumentName\>/”

referenceName : str[¶](#ApiClient.MappingApi.CreateMappingItem.referenceName "Permalink to this definition")  
Name of the mapping item

Returns:  The just created mapping item

Return type:  [`MappingItem`](MappingApi/MappingItem.md#ApiClient.MappingItem "ApiClient.MappingItem (Python class) — MappingApi.CreateGenericMappingItem")

CreateMeasurementMappingItem(*[systemIdentifier](#ApiClient.MappingApi.CreateMeasurementMappingItem.systemIdentifier "ApiClient.MappingApi.CreateMeasurementMappingItem.systemIdentifier (Python parameter) — Name of ECU according to the test configuration")*, *[targetPath](#ApiClient.MappingApi.CreateMeasurementMappingItem.targetPath "ApiClient.MappingApi.CreateMeasurementMappingItem.targetPath (Python parameter) — Name of measurement variable to be accessed")*, *[variableType](#ApiClient.MappingApi.CreateMeasurementMappingItem.variableType "ApiClient.MappingApi.CreateMeasurementMappingItem.variableType (Python parameter) — Type of variable to be mapped (VALUE, VECTOR, MATRIX, VECTOR-ELEMENT, MATRIX-ELEMENT)")=`None`*, *[referenceName](#ApiClient.MappingApi.CreateMeasurementMappingItem.referenceName "ApiClient.MappingApi.CreateMeasurementMappingItem.referenceName (Python parameter) — Name of the mapping item")=`None`*, *[xElement](#ApiClient.MappingApi.CreateMeasurementMappingItem.xElement "ApiClient.MappingApi.CreateMeasurementMappingItem.xElement (Python parameter) — Index on x axis if single element of VECTOR or MATRIX should be accessed")=`None`*, *[yElement](#ApiClient.MappingApi.CreateMeasurementMappingItem.yElement "ApiClient.MappingApi.CreateMeasurementMappingItem.yElement (Python parameter) — Index on y axis if single element of MATRIX should be accessed")=`None`*, *[zElement](#ApiClient.MappingApi.CreateMeasurementMappingItem.zElement "ApiClient.MappingApi.CreateMeasurementMappingItem.zElement (Python parameter) — Index on z axis if single element of MATRIX should be accessed")=`None`*, *[checkTarget](#ApiClient.MappingApi.CreateMeasurementMappingItem.checkTarget "ApiClient.MappingApi.CreateMeasurementMappingItem.checkTarget (Python parameter) — Selects if target path should be checked")=`True`*)[¶](#ApiClient.MappingApi.CreateMeasurementMappingItem "Link to this definition")  
Creates a measurement mapping item of the desired variable type.

Parameters:  systemIdentifier : str[¶](#ApiClient.MappingApi.CreateMeasurementMappingItem.systemIdentifier "Permalink to this definition")  
Name of ECU according to the test configuration

targetPath : str[¶](#ApiClient.MappingApi.CreateMeasurementMappingItem.targetPath "Permalink to this definition")  
Name of measurement variable to be accessed

variableType : str[¶](#ApiClient.MappingApi.CreateMeasurementMappingItem.variableType "Permalink to this definition")  
Type of variable to be mapped (VALUE, VECTOR, MATRIX, VECTOR-ELEMENT, MATRIX-ELEMENT)

referenceName : str[¶](#ApiClient.MappingApi.CreateMeasurementMappingItem.referenceName "Permalink to this definition")  
Name of the mapping item

xElement : integer[¶](#ApiClient.MappingApi.CreateMeasurementMappingItem.xElement "Permalink to this definition")  
Index on x axis if single element of VECTOR or MATRIX should be accessed

yElement : integer[¶](#ApiClient.MappingApi.CreateMeasurementMappingItem.yElement "Permalink to this definition")  
Index on y axis if single element of MATRIX should be accessed

zElement : integer[¶](#ApiClient.MappingApi.CreateMeasurementMappingItem.zElement "Permalink to this definition")  
Index on z axis if single element of MATRIX should be accessed

checkTarget : boolean[¶](#ApiClient.MappingApi.CreateMeasurementMappingItem.checkTarget "Permalink to this definition")  
Selects if target path should be checked

Returns:  The just created mapping item

Return type:  [`MeasureMappingItem`](MappingApi/MeasureMappingItem.md#ApiClient.MeasureMappingItem "ApiClient.MeasureMappingItem (Python class) — MappingApi.CreateMeasurementMappingItem")

CreateModelMappingItem(*[systemIdentifier](#ApiClient.MappingApi.CreateModelMappingItem.systemIdentifier "ApiClient.MappingApi.CreateModelMappingItem.systemIdentifier (Python parameter) — Name of system according to the test configuration, e.g.")*, *[targetPath](#ApiClient.MappingApi.CreateModelMappingItem.targetPath "ApiClient.MappingApi.CreateModelMappingItem.targetPath (Python parameter) — Path to the model variable to be accessed, e.g.")*, *[variableType](#ApiClient.MappingApi.CreateModelMappingItem.variableType "ApiClient.MappingApi.CreateModelMappingItem.variableType (Python parameter) — Type of variable to be mapped (VALUE, VECTOR, MATRIX)")=`None`*, *[isSignal](#ApiClient.MappingApi.CreateModelMappingItem.isSignal "ApiClient.MappingApi.CreateModelMappingItem.isSignal (Python parameter) — Selects if the mapping item should point to a model signal instead of variable")=`False`*, *[referenceName](#ApiClient.MappingApi.CreateModelMappingItem.referenceName "ApiClient.MappingApi.CreateModelMappingItem.referenceName (Python parameter) — Name of the mapping item")=`None`*, *[checkTarget](#ApiClient.MappingApi.CreateModelMappingItem.checkTarget "ApiClient.MappingApi.CreateModelMappingItem.checkTarget (Python parameter) — Selects if target path should be checked")=`True`*)[¶](#ApiClient.MappingApi.CreateModelMappingItem "Link to this definition")  
Creates a mapping item of the desired variable type pointing at a certain model variable. The model has to be loaded in order to create a model mapping item.

Parameters:  systemIdentifier : str[¶](#ApiClient.MappingApi.CreateModelMappingItem.systemIdentifier "Permalink to this definition")  
Name of system according to the test configuration, e.g. “Plant model”

targetPath : str[¶](#ApiClient.MappingApi.CreateModelMappingItem.targetPath "Permalink to this definition")  
Path to the model variable to be accessed, e.g. “Model Root/varName”.

variableType : str[¶](#ApiClient.MappingApi.CreateModelMappingItem.variableType "Permalink to this definition")  
Type of variable to be mapped (VALUE, VECTOR, MATRIX)

isSignal : boolean[¶](#ApiClient.MappingApi.CreateModelMappingItem.isSignal "Permalink to this definition")  
Selects if the mapping item should point to a model signal instead of variable

referenceName : str[¶](#ApiClient.MappingApi.CreateModelMappingItem.referenceName "Permalink to this definition")  
Name of the mapping item

checkTarget : boolean[¶](#ApiClient.MappingApi.CreateModelMappingItem.checkTarget "Permalink to this definition")  
Selects if target path should be checked

Returns:  The just created mapping item

Return type:  [`ModelMappingItem`](MappingApi/ModelMappingItem.md#ApiClient.ModelMappingItem "ApiClient.ModelMappingItem (Python class) — MappingApi.CreateModelMappingItem")

CreatePackageMappingItem(*[pkgPath](#ApiClient.MappingApi.CreatePackageMappingItem.pkgPath "ApiClient.MappingApi.CreatePackageMappingItem.pkgPath (Python parameter) — Path to the referenced package, either absolute or relative to the packages directory of the current workspace or given namespace, e.g.")*, *[referenceName](#ApiClient.MappingApi.CreatePackageMappingItem.referenceName "ApiClient.MappingApi.CreatePackageMappingItem.referenceName (Python parameter) — Name of the mapping item")=`None`*, *[namespace](#ApiClient.MappingApi.CreatePackageMappingItem.namespace "ApiClient.MappingApi.CreatePackageMappingItem.namespace (Python parameter) — Identifier of the workspace to which a relative pkgPath is resolved.")=`None`*, *[checkTarget](#ApiClient.MappingApi.CreatePackageMappingItem.checkTarget "ApiClient.MappingApi.CreatePackageMappingItem.checkTarget (Python parameter) — Selects if target path should be checked")=`True`*)[¶](#ApiClient.MappingApi.CreatePackageMappingItem "Link to this definition")  
Creates a package mapping item referencing the given package path. For example, CreatePackageMappingItem(‘MyPackage.pkg’) results in a reference to ‘\<workspace.packages\>/MyPackage.pkg’.

Parameters:  pkgPath : str[¶](#ApiClient.MappingApi.CreatePackageMappingItem.pkgPath "Permalink to this definition")  
Path to the referenced package, either absolute or relative to the packages directory of the current workspace or given namespace, e.g. ‘MyPackage.pkg’. An absolute path located in the current workspace will also be resolved to a relative workspace reference.

referenceName : str[¶](#ApiClient.MappingApi.CreatePackageMappingItem.referenceName "Permalink to this definition")  
Name of the mapping item

namespace : str[¶](#ApiClient.MappingApi.CreatePackageMappingItem.namespace "Permalink to this definition")  
Identifier of the workspace to which a relative pkgPath is resolved. If not present or None, the namespace is determined automatically. It is also possible to reference a library workspace using its namespace. A relative pkgPath is resolved relative to the packages directory of the given namespace. For example, the namespace parameter ‘myLibrary’ results in ‘\<libraries.myLibrary.packages\>/MyPackage.pkg’.

checkTarget : boolean[¶](#ApiClient.MappingApi.CreatePackageMappingItem.checkTarget "Permalink to this definition")  
Selects if target path should be checked

Returns:  The just created mapping item

Return type:  [`PackageMappingItem`](MappingApi/PackageMappingItem.md#ApiClient.PackageMappingItem "ApiClient.PackageMappingItem (Python class) — MappingApi.CreatePackageMappingItem")

CreatePortMappingItem(*[systemIdentifier](#ApiClient.MappingApi.CreatePortMappingItem.systemIdentifier "ApiClient.MappingApi.CreatePortMappingItem.systemIdentifier (Python parameter) — SUT key")*, *[portType](#ApiClient.MappingApi.CreatePortMappingItem.portType "ApiClient.MappingApi.CreatePortMappingItem.portType (Python parameter) — type of the port - one of Bus, Service, or Logging")*, *[referenceName](#ApiClient.MappingApi.CreatePortMappingItem.referenceName "ApiClient.MappingApi.CreatePortMappingItem.referenceName (Python parameter) — Name of the mapping item (optional)")=`None`*, *[checkTarget](#ApiClient.MappingApi.CreatePortMappingItem.checkTarget "ApiClient.MappingApi.CreatePortMappingItem.checkTarget (Python parameter) — Selects if target path should be checked (optional)")=`True`*)[¶](#ApiClient.MappingApi.CreatePortMappingItem "Link to this definition")  
Creates a port mapping item.

Parameters:  systemIdentifier : str[¶](#ApiClient.MappingApi.CreatePortMappingItem.systemIdentifier "Permalink to this definition")  
SUT key

portType : str[¶](#ApiClient.MappingApi.CreatePortMappingItem.portType "Permalink to this definition")  
type of the port - one of Bus, Service, or Logging

referenceName : str[¶](#ApiClient.MappingApi.CreatePortMappingItem.referenceName "Permalink to this definition")  
Name of the mapping item (optional)

checkTarget : boolean[¶](#ApiClient.MappingApi.CreatePortMappingItem.checkTarget "Permalink to this definition")  
Selects if target path should be checked (optional)

Returns:  The just created mapping item

Return type:  [`PortMappingItem`](MappingApi/PortMappingItem.md#ApiClient.PortMappingItem "ApiClient.PortMappingItem (Python class) — MappingApi.CreatePortMappingItem")

CreateReferenceMappingItem(*[mappingItem](#ApiClient.MappingApi.CreateReferenceMappingItem.mappingItem "ApiClient.MappingApi.CreateReferenceMappingItem.mappingItem (Python parameter) — Mapping item that should be referenced")*, *[referenceName](#ApiClient.MappingApi.CreateReferenceMappingItem.referenceName "ApiClient.MappingApi.CreateReferenceMappingItem.referenceName (Python parameter) — Name of the mapping item (optional)")=`None`*)[¶](#ApiClient.MappingApi.CreateReferenceMappingItem "Link to this definition")  
Creates a mapping item that references another mapping item. The created mapping item can be assigned as the target of mappings in the context of a parameter set of a project’s test case.

Parameters:  mappingItem[¶](#ApiClient.MappingApi.CreateReferenceMappingItem.mappingItem "Permalink to this definition")  
Mapping item that should be referenced

referenceName : str[¶](#ApiClient.MappingApi.CreateReferenceMappingItem.referenceName "Permalink to this definition")  
Name of the mapping item (optional)

Returns:  The just created mapping item

Return type:  [`ReferenceMappingItem`](MappingApi/ReferenceMappingItem.md#ApiClient.ReferenceMappingItem "ApiClient.ReferenceMappingItem (Python class) — MappingApi.CreateReferenceMappingItem")

CreateRunningValueMappingItem(*[systemIdentifier](#ApiClient.MappingApi.CreateRunningValueMappingItem.systemIdentifier "ApiClient.MappingApi.CreateRunningValueMappingItem.systemIdentifier (Python parameter) — Name of ECU according to the test configuration")*, *[targetPath](#ApiClient.MappingApi.CreateRunningValueMappingItem.targetPath "ApiClient.MappingApi.CreateRunningValueMappingItem.targetPath (Python parameter) — Name of running value variable to be accessed")*, *[referenceName](#ApiClient.MappingApi.CreateRunningValueMappingItem.referenceName "ApiClient.MappingApi.CreateRunningValueMappingItem.referenceName (Python parameter) — Name of the mapping item")=`None`*, *[checkTarget](#ApiClient.MappingApi.CreateRunningValueMappingItem.checkTarget "ApiClient.MappingApi.CreateRunningValueMappingItem.checkTarget (Python parameter) — Selects if target path should be checked")=`True`*)[¶](#ApiClient.MappingApi.CreateRunningValueMappingItem "Link to this definition")  
Creates a running value mapping item of the desired variable type.

Parameters:  systemIdentifier : str[¶](#ApiClient.MappingApi.CreateRunningValueMappingItem.systemIdentifier "Permalink to this definition")  
Name of ECU according to the test configuration

targetPath : str[¶](#ApiClient.MappingApi.CreateRunningValueMappingItem.targetPath "Permalink to this definition")  
Name of running value variable to be accessed

referenceName : str[¶](#ApiClient.MappingApi.CreateRunningValueMappingItem.referenceName "Permalink to this definition")  
Name of the mapping item

checkTarget : boolean[¶](#ApiClient.MappingApi.CreateRunningValueMappingItem.checkTarget "Permalink to this definition")  
Selects if target path should be checked

Returns:  The just created mapping item

Return type:  [`RunningValueMappingItem`](MappingApi/RunningValueMappingItem.md#ApiClient.RunningValueMappingItem "ApiClient.RunningValueMappingItem (Python class) — MappingApi.CreateRunningValueMappingItem")

CreateServiceEventLeafMappingItem(*[systemIdentifier](#ApiClient.MappingApi.CreateServiceEventLeafMappingItem.systemIdentifier "ApiClient.MappingApi.CreateServiceEventLeafMappingItem.systemIdentifier (Python parameter) — SUT key")*, *[ecuName](#ApiClient.MappingApi.CreateServiceEventLeafMappingItem.ecuName "ApiClient.MappingApi.CreateServiceEventLeafMappingItem.ecuName (Python parameter) — Name of the ECU that provides the service")*, *[serviceName](#ApiClient.MappingApi.CreateServiceEventLeafMappingItem.serviceName "ApiClient.MappingApi.CreateServiceEventLeafMappingItem.serviceName (Python parameter) — Name of the service that provides the event")*, *[eventName](#ApiClient.MappingApi.CreateServiceEventLeafMappingItem.eventName "ApiClient.MappingApi.CreateServiceEventLeafMappingItem.eventName (Python parameter) — Name of the event")*, *[variablePath](#ApiClient.MappingApi.CreateServiceEventLeafMappingItem.variablePath "ApiClient.MappingApi.CreateServiceEventLeafMappingItem.variablePath (Python parameter) — Path to the return leaf node")*, *[eventgroupName](#ApiClient.MappingApi.CreateServiceEventLeafMappingItem.eventgroupName "ApiClient.MappingApi.CreateServiceEventLeafMappingItem.eventgroupName (Python parameter) — Name of the event group that contains the event (optional)")=`''`*, *[fieldName](#ApiClient.MappingApi.CreateServiceEventLeafMappingItem.fieldName "ApiClient.MappingApi.CreateServiceEventLeafMappingItem.fieldName (Python parameter) — Name of the field to which the event belongs (optional)")=`''`*, *[serviceConsumer](#ApiClient.MappingApi.CreateServiceEventLeafMappingItem.serviceConsumer "ApiClient.MappingApi.CreateServiceEventLeafMappingItem.serviceConsumer (Python parameter) — Name of the consumer ECU (optional)")=`''`*, *[referenceName](#ApiClient.MappingApi.CreateServiceEventLeafMappingItem.referenceName "ApiClient.MappingApi.CreateServiceEventLeafMappingItem.referenceName (Python parameter) — Name of the mapping item (optional)")=`None`*, *[checkTarget](#ApiClient.MappingApi.CreateServiceEventLeafMappingItem.checkTarget "ApiClient.MappingApi.CreateServiceEventLeafMappingItem.checkTarget (Python parameter) — Selects if target path should be checked (optional)")=`True`*)[¶](#ApiClient.MappingApi.CreateServiceEventLeafMappingItem "Link to this definition")  
Creates a service event leaf mapping item.

Parameters:  systemIdentifier : str[¶](#ApiClient.MappingApi.CreateServiceEventLeafMappingItem.systemIdentifier "Permalink to this definition")  
SUT key

ecuName : str[¶](#ApiClient.MappingApi.CreateServiceEventLeafMappingItem.ecuName "Permalink to this definition")  
Name of the ECU that provides the service

serviceName : str[¶](#ApiClient.MappingApi.CreateServiceEventLeafMappingItem.serviceName "Permalink to this definition")  
Name of the service that provides the event

eventName : str[¶](#ApiClient.MappingApi.CreateServiceEventLeafMappingItem.eventName "Permalink to this definition")  
Name of the event

variablePath : str[¶](#ApiClient.MappingApi.CreateServiceEventLeafMappingItem.variablePath "Permalink to this definition")  
Path to the return leaf node

eventgroupName : str[¶](#ApiClient.MappingApi.CreateServiceEventLeafMappingItem.eventgroupName "Permalink to this definition")  
Name of the event group that contains the event (optional)

fieldName : str[¶](#ApiClient.MappingApi.CreateServiceEventLeafMappingItem.fieldName "Permalink to this definition")  
Name of the field to which the event belongs (optional)

serviceConsumer : str[¶](#ApiClient.MappingApi.CreateServiceEventLeafMappingItem.serviceConsumer "Permalink to this definition")  
Name of the consumer ECU (optional)

referenceName : str[¶](#ApiClient.MappingApi.CreateServiceEventLeafMappingItem.referenceName "Permalink to this definition")  
Name of the mapping item (optional)

checkTarget : boolean[¶](#ApiClient.MappingApi.CreateServiceEventLeafMappingItem.checkTarget "Permalink to this definition")  
Selects if target path should be checked (optional)

Returns:  The just created mapping item

Return type:  [`ServiceEventLeafMappingItem`](MappingApi/ServiceEventLeafMappingItem.md#ApiClient.ServiceEventLeafMappingItem "ApiClient.ServiceEventLeafMappingItem (Python class) — MappingApi.CreateServiceEventLeafMappingItem")

CreateServiceMappingItem(*[systemIdentifier](#ApiClient.MappingApi.CreateServiceMappingItem.systemIdentifier "ApiClient.MappingApi.CreateServiceMappingItem.systemIdentifier (Python parameter) — SUT key")*, *[ecuName](#ApiClient.MappingApi.CreateServiceMappingItem.ecuName "ApiClient.MappingApi.CreateServiceMappingItem.ecuName (Python parameter) — Name of the ECU that provides the service")*, *[serviceName](#ApiClient.MappingApi.CreateServiceMappingItem.serviceName "ApiClient.MappingApi.CreateServiceMappingItem.serviceName (Python parameter) — Name of the service that provides the event")*, *[eventOrMethodName](#ApiClient.MappingApi.CreateServiceMappingItem.eventOrMethodName "ApiClient.MappingApi.CreateServiceMappingItem.eventOrMethodName (Python parameter) — Name of the event or the method")*, *[fieldName](#ApiClient.MappingApi.CreateServiceMappingItem.fieldName "ApiClient.MappingApi.CreateServiceMappingItem.fieldName (Python parameter) — Name of the field (optional)")=`''`*, *[eventGroupName](#ApiClient.MappingApi.CreateServiceMappingItem.eventGroupName "ApiClient.MappingApi.CreateServiceMappingItem.eventGroupName (Python parameter) — Name of the event group that contains the event (optional)")=`''`*, *[serviceConsumer](#ApiClient.MappingApi.CreateServiceMappingItem.serviceConsumer "ApiClient.MappingApi.CreateServiceMappingItem.serviceConsumer (Python parameter) — Name of the consumer ECU (optional)")=`''`*, *[referenceName](#ApiClient.MappingApi.CreateServiceMappingItem.referenceName "ApiClient.MappingApi.CreateServiceMappingItem.referenceName (Python parameter) — Name of the mapping item (optional)")=`None`*, *[checkTarget](#ApiClient.MappingApi.CreateServiceMappingItem.checkTarget "ApiClient.MappingApi.CreateServiceMappingItem.checkTarget (Python parameter) — Selects if target path should be checked (optional)")=`True`*)[¶](#ApiClient.MappingApi.CreateServiceMappingItem "Link to this definition")  
Creates a service field event mapping item.

Parameters:  systemIdentifier : str[¶](#ApiClient.MappingApi.CreateServiceMappingItem.systemIdentifier "Permalink to this definition")  
SUT key

ecuName : str[¶](#ApiClient.MappingApi.CreateServiceMappingItem.ecuName "Permalink to this definition")  
Name of the ECU that provides the service

serviceName : str[¶](#ApiClient.MappingApi.CreateServiceMappingItem.serviceName "Permalink to this definition")  
Name of the service that provides the event

eventOrMethodName : str[¶](#ApiClient.MappingApi.CreateServiceMappingItem.eventOrMethodName "Permalink to this definition")  
Name of the event or the method

fieldName : str[¶](#ApiClient.MappingApi.CreateServiceMappingItem.fieldName "Permalink to this definition")  
Name of the field (optional)

eventGroupName : str[¶](#ApiClient.MappingApi.CreateServiceMappingItem.eventGroupName "Permalink to this definition")  
Name of the event group that contains the event (optional)

serviceConsumer : str[¶](#ApiClient.MappingApi.CreateServiceMappingItem.serviceConsumer "Permalink to this definition")  
Name of the consumer ECU (optional)

referenceName : str[¶](#ApiClient.MappingApi.CreateServiceMappingItem.referenceName "Permalink to this definition")  
Name of the mapping item (optional)

checkTarget : boolean[¶](#ApiClient.MappingApi.CreateServiceMappingItem.checkTarget "Permalink to this definition")  
Selects if target path should be checked (optional)

Returns:  The just created mapping item

Return type:  [`ServiceMappingItem`](MappingApi/ServiceMappingItem.md#ApiClient.ServiceMappingItem "ApiClient.ServiceMappingItem (Python class) — MappingApi.CreateServiceMappingItem")

CreateServiceMethodParameterMappingItem(*[systemIdentifier](#ApiClient.MappingApi.CreateServiceMethodParameterMappingItem.systemIdentifier "ApiClient.MappingApi.CreateServiceMethodParameterMappingItem.systemIdentifier (Python parameter) — SUT key")*, *[ecuName](#ApiClient.MappingApi.CreateServiceMethodParameterMappingItem.ecuName "ApiClient.MappingApi.CreateServiceMethodParameterMappingItem.ecuName (Python parameter) — Name of the ECU that provides the service")*, *[serviceName](#ApiClient.MappingApi.CreateServiceMethodParameterMappingItem.serviceName "ApiClient.MappingApi.CreateServiceMethodParameterMappingItem.serviceName (Python parameter) — Name of the service that provides the method")*, *[methodName](#ApiClient.MappingApi.CreateServiceMethodParameterMappingItem.methodName "ApiClient.MappingApi.CreateServiceMethodParameterMappingItem.methodName (Python parameter) — Name of the method")*, *[variablePath](#ApiClient.MappingApi.CreateServiceMethodParameterMappingItem.variablePath "ApiClient.MappingApi.CreateServiceMethodParameterMappingItem.variablePath (Python parameter) — Path to the parameter leaf node")*, *[eventgroupName](#ApiClient.MappingApi.CreateServiceMethodParameterMappingItem.eventgroupName "ApiClient.MappingApi.CreateServiceMethodParameterMappingItem.eventgroupName (Python parameter) — Name of the event group that contains the method (optional)")=`''`*, *[fieldName](#ApiClient.MappingApi.CreateServiceMethodParameterMappingItem.fieldName "ApiClient.MappingApi.CreateServiceMethodParameterMappingItem.fieldName (Python parameter) — Name of the field to which the method belongs (optional)")=`''`*, *[serviceConsumer](#ApiClient.MappingApi.CreateServiceMethodParameterMappingItem.serviceConsumer "ApiClient.MappingApi.CreateServiceMethodParameterMappingItem.serviceConsumer (Python parameter) — Name of the consumer ECU (optional)")=`''`*, *[referenceName](#ApiClient.MappingApi.CreateServiceMethodParameterMappingItem.referenceName "ApiClient.MappingApi.CreateServiceMethodParameterMappingItem.referenceName (Python parameter) — Name of the mapping item (optional)")=`None`*, *[checkTarget](#ApiClient.MappingApi.CreateServiceMethodParameterMappingItem.checkTarget "ApiClient.MappingApi.CreateServiceMethodParameterMappingItem.checkTarget (Python parameter) — Selects if target path should be checked (optional)")=`True`*)[¶](#ApiClient.MappingApi.CreateServiceMethodParameterMappingItem "Link to this definition")  
Creates a service method parameter mapping item.

Parameters:  systemIdentifier : str[¶](#ApiClient.MappingApi.CreateServiceMethodParameterMappingItem.systemIdentifier "Permalink to this definition")  
SUT key

ecuName : str[¶](#ApiClient.MappingApi.CreateServiceMethodParameterMappingItem.ecuName "Permalink to this definition")  
Name of the ECU that provides the service

serviceName : str[¶](#ApiClient.MappingApi.CreateServiceMethodParameterMappingItem.serviceName "Permalink to this definition")  
Name of the service that provides the method

methodName : str[¶](#ApiClient.MappingApi.CreateServiceMethodParameterMappingItem.methodName "Permalink to this definition")  
Name of the method

variablePath : str[¶](#ApiClient.MappingApi.CreateServiceMethodParameterMappingItem.variablePath "Permalink to this definition")  
Path to the parameter leaf node

eventgroupName : str[¶](#ApiClient.MappingApi.CreateServiceMethodParameterMappingItem.eventgroupName "Permalink to this definition")  
Name of the event group that contains the method (optional)

fieldName : str[¶](#ApiClient.MappingApi.CreateServiceMethodParameterMappingItem.fieldName "Permalink to this definition")  
Name of the field to which the method belongs (optional)

serviceConsumer : str[¶](#ApiClient.MappingApi.CreateServiceMethodParameterMappingItem.serviceConsumer "Permalink to this definition")  
Name of the consumer ECU (optional)

referenceName : str[¶](#ApiClient.MappingApi.CreateServiceMethodParameterMappingItem.referenceName "Permalink to this definition")  
Name of the mapping item (optional)

checkTarget : boolean[¶](#ApiClient.MappingApi.CreateServiceMethodParameterMappingItem.checkTarget "Permalink to this definition")  
Selects if target path should be checked (optional)

Returns:  The just created mapping item

Return type:  [`ServiceMethodParameterMappingItem`](MappingApi/ServiceMethodParameterMappingItem.md#ApiClient.ServiceMethodParameterMappingItem "ApiClient.ServiceMethodParameterMappingItem (Python class) — MappingApi.CreateServiceMethodParameterMappingItem")

CreateServiceMethodReturnMappingItem(*[systemIdentifier](#ApiClient.MappingApi.CreateServiceMethodReturnMappingItem.systemIdentifier "ApiClient.MappingApi.CreateServiceMethodReturnMappingItem.systemIdentifier (Python parameter) — SUT key")*, *[ecuName](#ApiClient.MappingApi.CreateServiceMethodReturnMappingItem.ecuName "ApiClient.MappingApi.CreateServiceMethodReturnMappingItem.ecuName (Python parameter) — Name of the ECU that provides the service")*, *[serviceName](#ApiClient.MappingApi.CreateServiceMethodReturnMappingItem.serviceName "ApiClient.MappingApi.CreateServiceMethodReturnMappingItem.serviceName (Python parameter) — Name of the service that provides the method")*, *[methodName](#ApiClient.MappingApi.CreateServiceMethodReturnMappingItem.methodName "ApiClient.MappingApi.CreateServiceMethodReturnMappingItem.methodName (Python parameter) — Name of the method")*, *[variablePath](#ApiClient.MappingApi.CreateServiceMethodReturnMappingItem.variablePath "ApiClient.MappingApi.CreateServiceMethodReturnMappingItem.variablePath (Python parameter) — Path to the return leaf node")*, *[eventgroupName](#ApiClient.MappingApi.CreateServiceMethodReturnMappingItem.eventgroupName "ApiClient.MappingApi.CreateServiceMethodReturnMappingItem.eventgroupName (Python parameter) — Name of the event group that contains the method (optional)")=`''`*, *[fieldName](#ApiClient.MappingApi.CreateServiceMethodReturnMappingItem.fieldName "ApiClient.MappingApi.CreateServiceMethodReturnMappingItem.fieldName (Python parameter) — Name of the field to which the method belongs (optional)")=`''`*, *[serviceConsumer](#ApiClient.MappingApi.CreateServiceMethodReturnMappingItem.serviceConsumer "ApiClient.MappingApi.CreateServiceMethodReturnMappingItem.serviceConsumer (Python parameter) — Name of the consumer ECU (optional)")=`''`*, *[referenceName](#ApiClient.MappingApi.CreateServiceMethodReturnMappingItem.referenceName "ApiClient.MappingApi.CreateServiceMethodReturnMappingItem.referenceName (Python parameter) — Name of the mapping item (optional)")=`None`*, *[checkTarget](#ApiClient.MappingApi.CreateServiceMethodReturnMappingItem.checkTarget "ApiClient.MappingApi.CreateServiceMethodReturnMappingItem.checkTarget (Python parameter) — Selects if target path should be checked (optional)")=`True`*)[¶](#ApiClient.MappingApi.CreateServiceMethodReturnMappingItem "Link to this definition")  
Creates a service method return mapping item.

Parameters:  systemIdentifier : str[¶](#ApiClient.MappingApi.CreateServiceMethodReturnMappingItem.systemIdentifier "Permalink to this definition")  
SUT key

ecuName : str[¶](#ApiClient.MappingApi.CreateServiceMethodReturnMappingItem.ecuName "Permalink to this definition")  
Name of the ECU that provides the service

serviceName : str[¶](#ApiClient.MappingApi.CreateServiceMethodReturnMappingItem.serviceName "Permalink to this definition")  
Name of the service that provides the method

methodName : str[¶](#ApiClient.MappingApi.CreateServiceMethodReturnMappingItem.methodName "Permalink to this definition")  
Name of the method

variablePath : str[¶](#ApiClient.MappingApi.CreateServiceMethodReturnMappingItem.variablePath "Permalink to this definition")  
Path to the return leaf node

eventgroupName : str[¶](#ApiClient.MappingApi.CreateServiceMethodReturnMappingItem.eventgroupName "Permalink to this definition")  
Name of the event group that contains the method (optional)

fieldName : str[¶](#ApiClient.MappingApi.CreateServiceMethodReturnMappingItem.fieldName "Permalink to this definition")  
Name of the field to which the method belongs (optional)

serviceConsumer : str[¶](#ApiClient.MappingApi.CreateServiceMethodReturnMappingItem.serviceConsumer "Permalink to this definition")  
Name of the consumer ECU (optional)

referenceName : str[¶](#ApiClient.MappingApi.CreateServiceMethodReturnMappingItem.referenceName "Permalink to this definition")  
Name of the mapping item (optional)

checkTarget : boolean[¶](#ApiClient.MappingApi.CreateServiceMethodReturnMappingItem.checkTarget "Permalink to this definition")  
Selects if target path should be checked (optional)

Returns:  The just created mapping item

Return type:  [`ServiceMethodReturnMappingItem`](MappingApi/ServiceMethodReturnMappingItem.md#ApiClient.ServiceMethodReturnMappingItem "ApiClient.ServiceMethodReturnMappingItem (Python class) — MappingApi.CreateServiceMethodReturnMappingItem")

CreateServiceServiceMappingItem(*[systemIdentifier](#ApiClient.MappingApi.CreateServiceServiceMappingItem.systemIdentifier "ApiClient.MappingApi.CreateServiceServiceMappingItem.systemIdentifier (Python parameter) — SUT key")*, *[ecuName](#ApiClient.MappingApi.CreateServiceServiceMappingItem.ecuName "ApiClient.MappingApi.CreateServiceServiceMappingItem.ecuName (Python parameter) — Name of the ECU that provides the service")*, *[serviceName](#ApiClient.MappingApi.CreateServiceServiceMappingItem.serviceName "ApiClient.MappingApi.CreateServiceServiceMappingItem.serviceName (Python parameter) — Name of the service")*, *[referenceName](#ApiClient.MappingApi.CreateServiceServiceMappingItem.referenceName "ApiClient.MappingApi.CreateServiceServiceMappingItem.referenceName (Python parameter) — Name of the mapping item (optional)")=`None`*, *[checkTarget](#ApiClient.MappingApi.CreateServiceServiceMappingItem.checkTarget "ApiClient.MappingApi.CreateServiceServiceMappingItem.checkTarget (Python parameter) — Selects if target path should be checked (optional)")=`True`*)[¶](#ApiClient.MappingApi.CreateServiceServiceMappingItem "Link to this definition")  
Creates a service mapping item.

Parameters:  systemIdentifier : str[¶](#ApiClient.MappingApi.CreateServiceServiceMappingItem.systemIdentifier "Permalink to this definition")  
SUT key

ecuName : str[¶](#ApiClient.MappingApi.CreateServiceServiceMappingItem.ecuName "Permalink to this definition")  
Name of the ECU that provides the service

serviceName : str[¶](#ApiClient.MappingApi.CreateServiceServiceMappingItem.serviceName "Permalink to this definition")  
Name of the service

referenceName : str[¶](#ApiClient.MappingApi.CreateServiceServiceMappingItem.referenceName "Permalink to this definition")  
Name of the mapping item (optional)

checkTarget : boolean[¶](#ApiClient.MappingApi.CreateServiceServiceMappingItem.checkTarget "Permalink to this definition")  
Selects if target path should be checked (optional)

Returns:  The just created mapping item

Return type:  [`ServiceServiceMappingItem`](MappingApi/ServiceServiceMappingItem.md#ApiClient.ServiceServiceMappingItem "ApiClient.ServiceServiceMappingItem (Python class) — MappingApi.CreateServiceServiceMappingItem")

CreateTraceFileMappingItem(*[targetPath](#ApiClient.MappingApi.CreateTraceFileMappingItem.targetPath "ApiClient.MappingApi.CreateTraceFileMappingItem.targetPath (Python parameter) — Path to the trace file signal to be accessed")*, *[referenceName](#ApiClient.MappingApi.CreateTraceFileMappingItem.referenceName "ApiClient.MappingApi.CreateTraceFileMappingItem.referenceName (Python parameter) — Name of the mapping item")=`None`*, *[systemIdentifier](#ApiClient.MappingApi.CreateTraceFileMappingItem.systemIdentifier "ApiClient.MappingApi.CreateTraceFileMappingItem.systemIdentifier (Python parameter) — Name of system (relevant for automatically assignment to a signal group)")=`None`*)[¶](#ApiClient.MappingApi.CreateTraceFileMappingItem "Link to this definition")  
Creates a trace file mapping item pointing at a certain trace file signal.

Parameters:  targetPath : str[¶](#ApiClient.MappingApi.CreateTraceFileMappingItem.targetPath "Permalink to this definition")  
Path to the trace file signal to be accessed

referenceName : str[¶](#ApiClient.MappingApi.CreateTraceFileMappingItem.referenceName "Permalink to this definition")  
Name of the mapping item

systemIdentifier : str[¶](#ApiClient.MappingApi.CreateTraceFileMappingItem.systemIdentifier "Permalink to this definition")  
Name of system (relevant for automatically assignment to a signal group)

Returns:  The just created mapping item

Return type:  [`MappingItem`](MappingApi/MappingItem.md#ApiClient.MappingItem "ApiClient.MappingItem (Python class) — MappingApi.CreateGenericMappingItem")

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
