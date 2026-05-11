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

SignalGroupBase [ SignalGroupBase ](#)

SignalGroupBase

- [C SignalGroupBase ](#ApiClient.SignalGroupBase)
  - [M AppendMappingItem ](#ApiClient.SignalGroupBase.AppendMappingItem)
  - [M AppendRecordingGroup ](#ApiClient.SignalGroupBase.AppendRecordingGroup)
  - [M Clone ](#ApiClient.SignalGroupBase.Clone)
  - [M GetDescription ](#ApiClient.SignalGroupBase.GetDescription)
  - [M GetMappingItemNames ](#ApiClient.SignalGroupBase.GetMappingItemNames)
  - [M GetMappingItems ](#ApiClient.SignalGroupBase.GetMappingItems)
  - [M GetName ](#ApiClient.SignalGroupBase.GetName)
  - [M GetRecordingGroupNames ](#ApiClient.SignalGroupBase.GetRecordingGroupNames)
  - [M GetRecordingGroups ](#ApiClient.SignalGroupBase.GetRecordingGroups)
  - [M RemoveMappingItem ](#ApiClient.SignalGroupBase.RemoveMappingItem)
  - [M RemoveRecordingGroup ](#ApiClient.SignalGroupBase.RemoveRecordingGroup)
  - [M SetDescription ](#ApiClient.SignalGroupBase.SetDescription)
  - [M SetName ](#ApiClient.SignalGroupBase.SetName)

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

SignalGroupBase

- [C SignalGroupBase ](#ApiClient.SignalGroupBase)
  - [M AppendMappingItem ](#ApiClient.SignalGroupBase.AppendMappingItem)
  - [M AppendRecordingGroup ](#ApiClient.SignalGroupBase.AppendRecordingGroup)
  - [M Clone ](#ApiClient.SignalGroupBase.Clone)
  - [M GetDescription ](#ApiClient.SignalGroupBase.GetDescription)
  - [M GetMappingItemNames ](#ApiClient.SignalGroupBase.GetMappingItemNames)
  - [M GetMappingItems ](#ApiClient.SignalGroupBase.GetMappingItems)
  - [M GetName ](#ApiClient.SignalGroupBase.GetName)
  - [M GetRecordingGroupNames ](#ApiClient.SignalGroupBase.GetRecordingGroupNames)
  - [M GetRecordingGroups ](#ApiClient.SignalGroupBase.GetRecordingGroups)
  - [M RemoveMappingItem ](#ApiClient.SignalGroupBase.RemoveMappingItem)
  - [M RemoveRecordingGroup ](#ApiClient.SignalGroupBase.RemoveRecordingGroup)
  - [M SetDescription ](#ApiClient.SignalGroupBase.SetDescription)
  - [M SetName ](#ApiClient.SignalGroupBase.SetName)

# SignalGroupBase[¶](#signalgroupbase "Link to this heading")

*class* SignalGroupBase[¶](#ApiClient.SignalGroupBase "Link to this definition")  
API to access signal groups. Signals of a signal group are represented by references to mapping items.

AppendMappingItem(*[mappingItem](#ApiClient.SignalGroupBase.AppendMappingItem.mappingItem "ApiClient.SignalGroupBase.AppendMappingItem.mappingItem (Python parameter) — The mapping item to be added")*)[¶](#ApiClient.SignalGroupBase.AppendMappingItem "Link to this definition")  
Adds a mapping item to the signal group.

Parameters:  mappingItem[¶](#ApiClient.SignalGroupBase.AppendMappingItem.mappingItem "Permalink to this definition")  
The mapping item to be added

AppendRecordingGroup(*[recordingGroup](#ApiClient.SignalGroupBase.AppendRecordingGroup.recordingGroup "ApiClient.SignalGroupBase.AppendRecordingGroup.recordingGroup (Python parameter) — The recording group to be added")*)[¶](#ApiClient.SignalGroupBase.AppendRecordingGroup "Link to this definition")  
Adds a recording group to the signal group.

Parameters:  recordingGroup[¶](#ApiClient.SignalGroupBase.AppendRecordingGroup.recordingGroup "Permalink to this definition")  
The recording group to be added

Clone()[¶](#ApiClient.SignalGroupBase.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`SignalGroupBase`](#ApiClient.SignalGroupBase "ApiClient.SignalGroupBase (Python class) — API to access signal groups. Signals of a signal group are represented by references to mapping items.")

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

Return type:  list[[`MappingItem`](../MappingApi/MappingItem.md#ApiClient.MappingItem "ApiClient.MappingItem (Python class) — MappingApi.CreateGenericMappingItem")]

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

Return type:  list[[`RecordingGroup`](RecordingGroup.md#ApiClient.RecordingGroup "ApiClient.RecordingGroup (Python class) — SignalRecordingApi.CreateRecordingGroup")]

RemoveMappingItem(*[mappingItemName](#ApiClient.SignalGroupBase.RemoveMappingItem.mappingItemName "ApiClient.SignalGroupBase.RemoveMappingItem.mappingItemName (Python parameter) — The mapping item name")*)[¶](#ApiClient.SignalGroupBase.RemoveMappingItem "Link to this definition")  
Removes a mapping item from the signal group.

Parameters:  mappingItemName : str[¶](#ApiClient.SignalGroupBase.RemoveMappingItem.mappingItemName "Permalink to this definition")  
The mapping item name

RemoveRecordingGroup(*[recordingGroup](#ApiClient.SignalGroupBase.RemoveRecordingGroup.recordingGroup "ApiClient.SignalGroupBase.RemoveRecordingGroup.recordingGroup (Python parameter) — The recording group to be removed")*)[¶](#ApiClient.SignalGroupBase.RemoveRecordingGroup "Link to this definition")  
Removes a recording group from the signalGroup.

Parameters:  recordingGroup[¶](#ApiClient.SignalGroupBase.RemoveRecordingGroup.recordingGroup "Permalink to this definition")  
The recording group to be removed

SetDescription(*[description](#ApiClient.SignalGroupBase.SetDescription.description "ApiClient.SignalGroupBase.SetDescription.description (Python parameter) — The new description of the signal group.")*)[¶](#ApiClient.SignalGroupBase.SetDescription "Link to this definition")  
Sets the description of the signal group.

Parameters:  description : str[¶](#ApiClient.SignalGroupBase.SetDescription.description "Permalink to this definition")  
The new description of the signal group.

SetName(*[name](#ApiClient.SignalGroupBase.SetName.name "ApiClient.SignalGroupBase.SetName.name (Python parameter) — The new name")*)[¶](#ApiClient.SignalGroupBase.SetName "Link to this definition")  
Sets the name of the signal group.

Parameters:  name : str[¶](#ApiClient.SignalGroupBase.SetName.name "Permalink to this definition")  
The new name

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
