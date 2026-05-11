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

API for Analysis Jobs

[ AnalysisJob ](AnalysisJob.md)

[ AnalysisJobGenericSignal ](AnalysisJobGenericSignal.md)

[ AnalysisJobRecording ](AnalysisJobRecording.md)

Mapping [ Mapping ](#)

Mapping

- [C Mapping ](#ApiClient.Mapping)
  - [M AddItem ](#ApiClient.Mapping.AddItem)
  - [M Clone ](#ApiClient.Mapping.Clone)
  - [M GetItemByName ](#ApiClient.Mapping.GetItemByName)
  - [M GetItems ](#ApiClient.Mapping.GetItems)
  - [M GetItemsByTargetPath ](#ApiClient.Mapping.GetItemsByTargetPath)
  - [M HasItem ](#ApiClient.Mapping.HasItem)
  - [M RemoveItemByName ](#ApiClient.Mapping.RemoveItemByName)
  - [M ReplaceItem ](#ApiClient.Mapping.ReplaceItem)

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

[ API for Trace Step Templates ](../TraceStepTemplateApi.md)

[ API for Variables ](../VariableApi.md)

[ API for Workspaces ](../WorkspaceApi.md)

[ Trace Analysis API ](../../TraceAnalysisAPI/index.md)

[ Generator APIs ](../../generators/index.md)

[ Tools ](../../tools/index.md)

[ User test management ](../../userTestmanagement/index.md)

[ UserUtility API ](../../user-utility/user-utility.md)

[ Utility Examples ](../../user-utility/example-utilities.md)

Mapping

- [C Mapping ](#ApiClient.Mapping)
  - [M AddItem ](#ApiClient.Mapping.AddItem)
  - [M Clone ](#ApiClient.Mapping.Clone)
  - [M GetItemByName ](#ApiClient.Mapping.GetItemByName)
  - [M GetItems ](#ApiClient.Mapping.GetItems)
  - [M GetItemsByTargetPath ](#ApiClient.Mapping.GetItemsByTargetPath)
  - [M HasItem ](#ApiClient.Mapping.HasItem)
  - [M RemoveItemByName ](#ApiClient.Mapping.RemoveItemByName)
  - [M ReplaceItem ](#ApiClient.Mapping.ReplaceItem)

# Mapping[¶](#mapping "Link to this heading")

*class* Mapping[¶](#ApiClient.Mapping "Link to this definition")  
AddItem(*[mappingItem](#ApiClient.Mapping.AddItem.mappingItem "ApiClient.Mapping.AddItem.mappingItem (Python parameter) — The mapping item to be added")*)[¶](#ApiClient.Mapping.AddItem "Link to this definition")  
Adds a mapping item to the mapping.

Parameters:  mappingItem[¶](#ApiClient.Mapping.AddItem.mappingItem "Permalink to this definition")  
The mapping item to be added

Clone()[¶](#ApiClient.Mapping.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`Mapping`](#ApiClient.Mapping "ApiClient.Mapping (Python class) — Adds a mapping item to the mapping.")

GetItemByName(*[name](#ApiClient.Mapping.GetItemByName.name "ApiClient.Mapping.GetItemByName.name (Python parameter) — The name of the mapping item to be searched for")*)[¶](#ApiClient.Mapping.GetItemByName "Link to this definition")  
Searches the mapping for the mapping item by its name and returns it if existing.

Parameters:  name : str[¶](#ApiClient.Mapping.GetItemByName.name "Permalink to this definition")  
The name of the mapping item to be searched for

Returns:  mapping item with the given name or None if no such mapping item exists

Return type:  [`MappingItem`](../MappingApi/MappingItem.md#ApiClient.MappingItem "ApiClient.MappingItem (Python class) — MappingApi.CreateGenericMappingItem")

GetItems()[¶](#ApiClient.Mapping.GetItems "Link to this definition")  
Returns a list of all the mapping items of the mapping.

Returns:  List of all the mapping items of the mapping.

Return type:  list[[`MappingItem`](../MappingApi/MappingItem.md#ApiClient.MappingItem "ApiClient.MappingItem (Python class) — MappingApi.CreateGenericMappingItem")]

GetItemsByTargetPath(*[targetPath](#ApiClient.Mapping.GetItemsByTargetPath.targetPath "ApiClient.Mapping.GetItemsByTargetPath.targetPath (Python parameter) — The target path of the mapping items to be searched for")*)[¶](#ApiClient.Mapping.GetItemsByTargetPath "Link to this definition")  
Searches the mapping for all mapping items that have the target path and returns them if existing.

Parameters:  targetPath : str[¶](#ApiClient.Mapping.GetItemsByTargetPath.targetPath "Permalink to this definition")  
The target path of the mapping items to be searched for

Returns:  List of mapping items that have the target path.

Return type:  list[[`MappingItem`](../MappingApi/MappingItem.md#ApiClient.MappingItem "ApiClient.MappingItem (Python class) — MappingApi.CreateGenericMappingItem")]

HasItem(*[mappingItem](#ApiClient.Mapping.HasItem.mappingItem "ApiClient.Mapping.HasItem.mappingItem (Python parameter) — The mapping item to be checked")*)[¶](#ApiClient.Mapping.HasItem "Link to this definition")  
Checks whether the given mapping item belongs to the mapping.

Parameters:  mappingItem[¶](#ApiClient.Mapping.HasItem.mappingItem "Permalink to this definition")  
The mapping item to be checked

Returns:  True if the given mapping item belongs to the mapping.

Return type:  boolean

RemoveItemByName(*[name](#ApiClient.Mapping.RemoveItemByName.name "ApiClient.Mapping.RemoveItemByName.name (Python parameter) — The name of the mapping item to be removed")*)[¶](#ApiClient.Mapping.RemoveItemByName "Link to this definition")  
Removes a mapping item from the mapping.

Parameters:  name : str[¶](#ApiClient.Mapping.RemoveItemByName.name "Permalink to this definition")  
The name of the mapping item to be removed

ReplaceItem(*[mappingItem](#ApiClient.Mapping.ReplaceItem.mappingItem "ApiClient.Mapping.ReplaceItem.mappingItem (Python parameter) — The new mapping item to replace an existing one of the same name")*)[¶](#ApiClient.Mapping.ReplaceItem "Link to this definition")  
Replaces a mapping item from the mapping

Parameters:  mappingItem[¶](#ApiClient.Mapping.ReplaceItem.mappingItem "Permalink to this definition")  
The new mapping item to replace an existing one of the same name

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
