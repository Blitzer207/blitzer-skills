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

API for Project Components

[ AnalysisBindings ](AnalysisBindings.md)

[ AnalysisPackageCall ](AnalysisPackageCall.md)

[ AnalysisPackageMappingCall ](AnalysisPackageMappingCall.md)

[ ArtifactReference ](ArtifactReference.md)

[ AssignedSignal ](AssignedSignal.md)

[ ConfigChange ](ConfigChange.md)

[ GlobalConstants ](GlobalConstants.md)

[ MappingFiles ](MappingFiles.md)

[ PackageCall ](PackageCall.md)

[ PackageGenerator ](PackageGenerator.md)

[ PackageParameters ](PackageParameters.md)

[ ParameterGenerator ](ParameterGenerator.md)

[ ParameterSet ](ParameterSet.md)

[ ParameterSetAnalysisPackage ](ParameterSetAnalysisPackage.md)

[ ParameterSetBase ](ParameterSetBase.md)

[ ParameterSetMapping ](ParameterSetMapping.md)

ParameterSetRecordings [ ParameterSetRecordings ](#)

ParameterSetRecordings

- [C ParameterSetRecordings ](#ApiClient.ParameterSetRecordings)
  - [M AddRecordingInfos ](#ApiClient.ParameterSetRecordings.AddRecordingInfos)
  - [M Clone ](#ApiClient.ParameterSetRecordings.Clone)
  - [M GetRecordingInfos ](#ApiClient.ParameterSetRecordings.GetRecordingInfos)
  - [M RemoveRecordingInfoByIndex ](#ApiClient.ParameterSetRecordings.RemoveRecordingInfoByIndex)

[ ParameterVariationGeneratorComponent ](ParameterVariationGeneratorComponent.md)

[ ProjectCall ](ProjectCall.md)

[ ProjectComponent ](ProjectComponent.md)

[ ProjectFolder ](ProjectFolder.md)

[ ProjectGenerator ](ProjectGenerator.md)

[ SignalGroupReference ](SignalGroupReference.md)

[ StimulationPackageCall ](StimulationPackageCall.md)

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

[ API for Trace Step Templates ](../TraceStepTemplateApi.md)

[ API for Variables ](../VariableApi.md)

[ API for Workspaces ](../WorkspaceApi.md)

[ Trace Analysis API ](../../TraceAnalysisAPI/index.md)

[ Generator APIs ](../../generators/index.md)

[ Tools ](../../tools/index.md)

[ User test management ](../../userTestmanagement/index.md)

[ UserUtility API ](../../user-utility/user-utility.md)

[ Utility Examples ](../../user-utility/example-utilities.md)

ParameterSetRecordings

- [C ParameterSetRecordings ](#ApiClient.ParameterSetRecordings)
  - [M AddRecordingInfos ](#ApiClient.ParameterSetRecordings.AddRecordingInfos)
  - [M Clone ](#ApiClient.ParameterSetRecordings.Clone)
  - [M GetRecordingInfos ](#ApiClient.ParameterSetRecordings.GetRecordingInfos)
  - [M RemoveRecordingInfoByIndex ](#ApiClient.ParameterSetRecordings.RemoveRecordingInfoByIndex)

# ParameterSetRecordings[¶](#parametersetrecordings "Link to this heading")

*class* ParameterSetRecordings[¶](#ApiClient.ParameterSetRecordings "Link to this definition")  
AddRecordingInfos(*[recordingGroupName](#ApiClient.ParameterSetRecordings.AddRecordingInfos.recordingGroupName "ApiClient.ParameterSetRecordings.AddRecordingInfos.recordingGroupName (Python parameter) — Name of the recording group to add the recording item")*, *[recordingInfos](#ApiClient.ParameterSetRecordings.AddRecordingInfos.recordingInfos "ApiClient.ParameterSetRecordings.AddRecordingInfos.recordingInfos (Python parameter) — The recording items to be added")*)[¶](#ApiClient.ParameterSetRecordings.AddRecordingInfos "Link to this definition")  
Adds a recording info item to a specified recording group in the parameter set.

Parameters:  recordingGroupName : str[¶](#ApiClient.ParameterSetRecordings.AddRecordingInfos.recordingGroupName "Permalink to this definition")  
Name of the recording group to add the recording item

recordingInfos[¶](#ApiClient.ParameterSetRecordings.AddRecordingInfos.recordingInfos "Permalink to this definition")  
The recording items to be added

Clone()[¶](#ApiClient.ParameterSetRecordings.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`ParameterSetRecordings`](#ApiClient.ParameterSetRecordings "ApiClient.ParameterSetRecordings (Python class) — Adds a recording info item to a specified recording group in the parameter set.")

GetRecordingInfos(*[recordingGroupName](#ApiClient.ParameterSetRecordings.GetRecordingInfos.recordingGroupName "ApiClient.ParameterSetRecordings.GetRecordingInfos.recordingGroupName (Python parameter) — Name of the recording group to return the info items of")=`None`*)[¶](#ApiClient.ParameterSetRecordings.GetRecordingInfos "Link to this definition")  
Returns recording information of the parameter set. If a recording group name is given returns only those items of the group

Parameters:  recordingGroupName : str[¶](#ApiClient.ParameterSetRecordings.GetRecordingInfos.recordingGroupName "Permalink to this definition")  
Name of the recording group to return the info items of

Returns:  recording info items

Return type:  list[[`RecordingInfo`](../SignalRecordingApi/RecordingInfo.md#ApiClient.RecordingInfo "ApiClient.RecordingInfo (Python class) — SignalRecordingApi.CreateRecordingInfo")]

RemoveRecordingInfoByIndex(*[groupName](#ApiClient.ParameterSetRecordings.RemoveRecordingInfoByIndex.groupName "ApiClient.ParameterSetRecordings.RemoveRecordingInfoByIndex.groupName (Python parameter) — Recording group name")*, *[infoIndex](#ApiClient.ParameterSetRecordings.RemoveRecordingInfoByIndex.infoIndex "ApiClient.ParameterSetRecordings.RemoveRecordingInfoByIndex.infoIndex (Python parameter) — Index of the recording info item in the recording group to be removed")*)[¶](#ApiClient.ParameterSetRecordings.RemoveRecordingInfoByIndex "Link to this definition")  
Removes a recording info item from the parameter set by recording group name and recording info index.

Parameters:  groupName : str[¶](#ApiClient.ParameterSetRecordings.RemoveRecordingInfoByIndex.groupName "Permalink to this definition")  
Recording group name

infoIndex : integer[¶](#ApiClient.ParameterSetRecordings.RemoveRecordingInfoByIndex.infoIndex "Permalink to this definition")  
Index of the recording info item in the recording group to be removed

Raise:  
ApiError: - When there is no group matching the given name - When the recording info index is out of range

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
