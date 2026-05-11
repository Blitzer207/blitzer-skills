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

SignalGroup [ SignalGroup ](#)

SignalGroup

- [C SignalGroup ](#ApiClient.SignalGroup)
  - [M AppendMappingItem ](#ApiClient.SignalGroup.AppendMappingItem)
  - [M AppendRecordingGroup ](#ApiClient.SignalGroup.AppendRecordingGroup)
  - [M Clone ](#ApiClient.SignalGroup.Clone)
  - [M GetDescription ](#ApiClient.SignalGroup.GetDescription)
  - [M GetMappingItemNames ](#ApiClient.SignalGroup.GetMappingItemNames)
  - [M GetMappingItems ](#ApiClient.SignalGroup.GetMappingItems)
  - [M GetMeasurementListFile ](#ApiClient.SignalGroup.GetMeasurementListFile)
  - [M GetName ](#ApiClient.SignalGroup.GetName)
  - [M GetRecordingGroupNames ](#ApiClient.SignalGroup.GetRecordingGroupNames)
  - [M GetRecordingGroups ](#ApiClient.SignalGroup.GetRecordingGroups)
  - [M RemoveMappingItem ](#ApiClient.SignalGroup.RemoveMappingItem)
  - [M RemoveMeasurementListFile ](#ApiClient.SignalGroup.RemoveMeasurementListFile)
  - [M RemoveRecordingGroup ](#ApiClient.SignalGroup.RemoveRecordingGroup)
  - [M SetDescription ](#ApiClient.SignalGroup.SetDescription)
  - [M SetMeasurementListFile ](#ApiClient.SignalGroup.SetMeasurementListFile)
  - [M SetName ](#ApiClient.SignalGroup.SetName)

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

SignalGroup

- [C SignalGroup ](#ApiClient.SignalGroup)
  - [M AppendMappingItem ](#ApiClient.SignalGroup.AppendMappingItem)
  - [M AppendRecordingGroup ](#ApiClient.SignalGroup.AppendRecordingGroup)
  - [M Clone ](#ApiClient.SignalGroup.Clone)
  - [M GetDescription ](#ApiClient.SignalGroup.GetDescription)
  - [M GetMappingItemNames ](#ApiClient.SignalGroup.GetMappingItemNames)
  - [M GetMappingItems ](#ApiClient.SignalGroup.GetMappingItems)
  - [M GetMeasurementListFile ](#ApiClient.SignalGroup.GetMeasurementListFile)
  - [M GetName ](#ApiClient.SignalGroup.GetName)
  - [M GetRecordingGroupNames ](#ApiClient.SignalGroup.GetRecordingGroupNames)
  - [M GetRecordingGroups ](#ApiClient.SignalGroup.GetRecordingGroups)
  - [M RemoveMappingItem ](#ApiClient.SignalGroup.RemoveMappingItem)
  - [M RemoveMeasurementListFile ](#ApiClient.SignalGroup.RemoveMeasurementListFile)
  - [M RemoveRecordingGroup ](#ApiClient.SignalGroup.RemoveRecordingGroup)
  - [M SetDescription ](#ApiClient.SignalGroup.SetDescription)
  - [M SetMeasurementListFile ](#ApiClient.SignalGroup.SetMeasurementListFile)
  - [M SetName ](#ApiClient.SignalGroup.SetName)

# SignalGroup[¶](#signalgroup "Link to this heading")

*class* SignalGroup[¶](#ApiClient.SignalGroup "Link to this definition")  
API to access signal groups. Signals of a signal group are represented by references to mapping items.

Returned by

- [`SignalRecordingApi.CreateSignalGroup`](../SignalRecordingApi.md#ApiClient.SignalRecordingApi.CreateSignalGroup "ApiClient.SignalRecordingApi.CreateSignalGroup (Python method) — Creates a new signal group. If no name is given, a name will be generated if the signal group is added to a package.")

AppendMappingItem(*[mappingItem](#ApiClient.SignalGroup.AppendMappingItem.mappingItem "ApiClient.SignalGroup.AppendMappingItem.mappingItem (Python parameter) — The mapping item to be added")*)[¶](#ApiClient.SignalGroup.AppendMappingItem "Link to this definition")  
Adds a mapping item to the signal group.

Parameters:  mappingItem[¶](#ApiClient.SignalGroup.AppendMappingItem.mappingItem "Permalink to this definition")  
The mapping item to be added

AppendRecordingGroup(*[recordingGroup](#ApiClient.SignalGroup.AppendRecordingGroup.recordingGroup "ApiClient.SignalGroup.AppendRecordingGroup.recordingGroup (Python parameter) — The recording group to be added")*)[¶](#ApiClient.SignalGroup.AppendRecordingGroup "Link to this definition")  
Adds a recording group to the signal group.

Parameters:  recordingGroup[¶](#ApiClient.SignalGroup.AppendRecordingGroup.recordingGroup "Permalink to this definition")  
The recording group to be added

Clone()[¶](#ApiClient.SignalGroup.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`SignalGroup`](#ApiClient.SignalGroup "ApiClient.SignalGroup (Python class) — API to access signal groups. Signals of a signal group are represented by references to mapping items.")

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

Return type:  list[[`MappingItem`](../MappingApi/MappingItem.md#ApiClient.MappingItem "ApiClient.MappingItem (Python class) — MappingApi.CreateGenericMappingItem")]

GetMeasurementListFile()[¶](#ApiClient.SignalGroup.GetMeasurementListFile "Link to this definition")  
Returns the path to the measurement list file (.xam).

Returns:  Returns the absolute path to the measurement list file.

Return type:  str

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

Return type:  list[[`RecordingGroup`](RecordingGroup.md#ApiClient.RecordingGroup "ApiClient.RecordingGroup (Python class) — SignalRecordingApi.CreateRecordingGroup")]

RemoveMappingItem(*[mappingItemName](#ApiClient.SignalGroup.RemoveMappingItem.mappingItemName "ApiClient.SignalGroup.RemoveMappingItem.mappingItemName (Python parameter) — The mapping item name")*)[¶](#ApiClient.SignalGroup.RemoveMappingItem "Link to this definition")  
Removes a mapping item from the signal group.

Parameters:  mappingItemName : str[¶](#ApiClient.SignalGroup.RemoveMappingItem.mappingItemName "Permalink to this definition")  
The mapping item name

RemoveMeasurementListFile()[¶](#ApiClient.SignalGroup.RemoveMeasurementListFile "Link to this definition")  
Removes the measurement list file (.xam) from the signal group.

RemoveRecordingGroup(*[recordingGroup](#ApiClient.SignalGroup.RemoveRecordingGroup.recordingGroup "ApiClient.SignalGroup.RemoveRecordingGroup.recordingGroup (Python parameter) — The recording group to be removed")*)[¶](#ApiClient.SignalGroup.RemoveRecordingGroup "Link to this definition")  
Removes a recording group from the signalGroup.

Parameters:  recordingGroup[¶](#ApiClient.SignalGroup.RemoveRecordingGroup.recordingGroup "Permalink to this definition")  
The recording group to be removed

SetDescription(*[description](#ApiClient.SignalGroup.SetDescription.description "ApiClient.SignalGroup.SetDescription.description (Python parameter) — The new description of the signal group.")*)[¶](#ApiClient.SignalGroup.SetDescription "Link to this definition")  
Sets the description of the signal group.

Parameters:  description : str[¶](#ApiClient.SignalGroup.SetDescription.description "Permalink to this definition")  
The new description of the signal group.

SetMeasurementListFile(*[path](#ApiClient.SignalGroup.SetMeasurementListFile.path "ApiClient.SignalGroup.SetMeasurementListFile.path (Python parameter) — The filepath to the measurement list file (.xam)")*, *[namespace](#ApiClient.SignalGroup.SetMeasurementListFile.namespace "ApiClient.SignalGroup.SetMeasurementListFile.namespace (Python parameter) — Identifier of the workspace to which a relative filePath is resolved.")=`None`*)[¶](#ApiClient.SignalGroup.SetMeasurementListFile "Link to this definition")  
Sets a measurement list file to the signal group.

Parameters:  path : str[¶](#ApiClient.SignalGroup.SetMeasurementListFile.path "Permalink to this definition")  
The filepath to the measurement list file (.xam)

namespace : str[¶](#ApiClient.SignalGroup.SetMeasurementListFile.namespace "Permalink to this definition")  
Identifier of the workspace to which a relative filePath is resolved. If not present or None, the namespace is determined automatically. It is also possible to reference a library workspace using its namespace. A relative filePath is resolved relative to the parameters directory of the given namespace. For example, the namespace parameter ‘myLibrary’ results in ‘\<libraries.myLibrary.parameters\>/MyMapping.xam’.

SetName(*[name](#ApiClient.SignalGroup.SetName.name "ApiClient.SignalGroup.SetName.name (Python parameter) — The new name")*)[¶](#ApiClient.SignalGroup.SetName "Link to this definition")  
Sets the name of the signal group.

Parameters:  name : str[¶](#ApiClient.SignalGroup.SetName.name "Permalink to this definition")  
The new name

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
