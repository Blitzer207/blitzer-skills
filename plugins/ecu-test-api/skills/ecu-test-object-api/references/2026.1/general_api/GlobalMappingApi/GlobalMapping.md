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

API for Global Mappings

GlobalMapping [ GlobalMapping ](#)

GlobalMapping

- [C GlobalMapping ](#ApiClient.GlobalMapping)
  - [M AddItem ](#ApiClient.GlobalMapping.AddItem)
  - [M Clone ](#ApiClient.GlobalMapping.Clone)
  - [M GetFilename ](#ApiClient.GlobalMapping.GetFilename)
  - [M GetItemByName ](#ApiClient.GlobalMapping.GetItemByName)
  - [M GetItems ](#ApiClient.GlobalMapping.GetItems)
  - [M GetItemsByTargetPath ](#ApiClient.GlobalMapping.GetItemsByTargetPath)
  - [M HasItem ](#ApiClient.GlobalMapping.HasItem)
  - [M RemoveItemByName ](#ApiClient.GlobalMapping.RemoveItemByName)
  - [M ReplaceItem ](#ApiClient.GlobalMapping.ReplaceItem)
  - [M Save ](#ApiClient.GlobalMapping.Save)

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

GlobalMapping

- [C GlobalMapping ](#ApiClient.GlobalMapping)
  - [M AddItem ](#ApiClient.GlobalMapping.AddItem)
  - [M Clone ](#ApiClient.GlobalMapping.Clone)
  - [M GetFilename ](#ApiClient.GlobalMapping.GetFilename)
  - [M GetItemByName ](#ApiClient.GlobalMapping.GetItemByName)
  - [M GetItems ](#ApiClient.GlobalMapping.GetItems)
  - [M GetItemsByTargetPath ](#ApiClient.GlobalMapping.GetItemsByTargetPath)
  - [M HasItem ](#ApiClient.GlobalMapping.HasItem)
  - [M RemoveItemByName ](#ApiClient.GlobalMapping.RemoveItemByName)
  - [M ReplaceItem ](#ApiClient.GlobalMapping.ReplaceItem)
  - [M Save ](#ApiClient.GlobalMapping.Save)

# GlobalMapping[¶](#globalmapping "Link to this heading")

*class* GlobalMapping[¶](#ApiClient.GlobalMapping "Link to this definition")  
Returned by

- [`GlobalMappingApi.CreateMapping`](../GlobalMappingApi.md#ApiClient.GlobalMappingApi.CreateMapping "ApiClient.GlobalMappingApi.CreateMapping (Python method) — Creates an empty Mapping.")

- [`GlobalMappingApi.OpenMapping`](../GlobalMappingApi.md#ApiClient.GlobalMappingApi.OpenMapping "ApiClient.GlobalMappingApi.OpenMapping (Python method) — Opens an existing global mapping. Raises an ApiError if the referenced file does not exist.")

- [`GlobalMappingApi.SearchGlobalMappings`](../GlobalMappingApi.md#ApiClient.GlobalMappingApi.SearchGlobalMappings "ApiClient.GlobalMappingApi.SearchGlobalMappings (Python method) — Searches the current workspace and library workspaces for Global Mappings matching the given search criteria.")

AddItem(*[mappingItem](#ApiClient.GlobalMapping.AddItem.mappingItem "ApiClient.GlobalMapping.AddItem.mappingItem (Python parameter) — The mapping item to be added")*)[¶](#ApiClient.GlobalMapping.AddItem "Link to this definition")  
Adds a mapping item to the mapping.

Parameters:  mappingItem[¶](#ApiClient.GlobalMapping.AddItem.mappingItem "Permalink to this definition")  
The mapping item to be added

Clone()[¶](#ApiClient.GlobalMapping.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`GlobalMapping`](#ApiClient.GlobalMapping "ApiClient.GlobalMapping (Python class) — GlobalMappingApi.CreateMapping")

GetFilename()[¶](#ApiClient.GlobalMapping.GetFilename "Link to this definition")  
Returns the path to the .xam file.

Returns:  Path to the .xam file or None if mapping is not saved yet.

Return type:  str

GetItemByName(*[name](#ApiClient.GlobalMapping.GetItemByName.name "ApiClient.GlobalMapping.GetItemByName.name (Python parameter) — The name of the mapping item to be searched for")*)[¶](#ApiClient.GlobalMapping.GetItemByName "Link to this definition")  
Searches the mapping for the mapping item by its name and returns it if existing.

Parameters:  name : str[¶](#ApiClient.GlobalMapping.GetItemByName.name "Permalink to this definition")  
The name of the mapping item to be searched for

Returns:  mapping item with the given name or None if no such mapping item exists

Return type:  [`MappingItem`](../MappingApi/MappingItem.md#ApiClient.MappingItem "ApiClient.MappingItem (Python class) — MappingApi.CreateGenericMappingItem")

GetItems()[¶](#ApiClient.GlobalMapping.GetItems "Link to this definition")  
Returns a list of all the mapping items of the mapping.

Returns:  List of all the mapping items of the mapping.

Return type:  list[[`MappingItem`](../MappingApi/MappingItem.md#ApiClient.MappingItem "ApiClient.MappingItem (Python class) — MappingApi.CreateGenericMappingItem")]

GetItemsByTargetPath(*[targetPath](#ApiClient.GlobalMapping.GetItemsByTargetPath.targetPath "ApiClient.GlobalMapping.GetItemsByTargetPath.targetPath (Python parameter) — The target path of the mapping items to be searched for")*)[¶](#ApiClient.GlobalMapping.GetItemsByTargetPath "Link to this definition")  
Searches the mapping for all mapping items that have the target path and returns them if existing.

Parameters:  targetPath : str[¶](#ApiClient.GlobalMapping.GetItemsByTargetPath.targetPath "Permalink to this definition")  
The target path of the mapping items to be searched for

Returns:  List of mapping items that have the target path.

Return type:  list[[`MappingItem`](../MappingApi/MappingItem.md#ApiClient.MappingItem "ApiClient.MappingItem (Python class) — MappingApi.CreateGenericMappingItem")]

HasItem(*[mappingItem](#ApiClient.GlobalMapping.HasItem.mappingItem "ApiClient.GlobalMapping.HasItem.mappingItem (Python parameter) — The mapping item to be checked")*)[¶](#ApiClient.GlobalMapping.HasItem "Link to this definition")  
Checks whether the given mapping item belongs to the mapping.

Parameters:  mappingItem[¶](#ApiClient.GlobalMapping.HasItem.mappingItem "Permalink to this definition")  
The mapping item to be checked

Returns:  True if the given mapping item belongs to the mapping.

Return type:  boolean

RemoveItemByName(*[name](#ApiClient.GlobalMapping.RemoveItemByName.name "ApiClient.GlobalMapping.RemoveItemByName.name (Python parameter) — The name of the mapping item to be removed")*)[¶](#ApiClient.GlobalMapping.RemoveItemByName "Link to this definition")  
Removes a mapping item from the mapping.

Parameters:  name : str[¶](#ApiClient.GlobalMapping.RemoveItemByName.name "Permalink to this definition")  
The name of the mapping item to be removed

ReplaceItem(*[mappingItem](#ApiClient.GlobalMapping.ReplaceItem.mappingItem "ApiClient.GlobalMapping.ReplaceItem.mappingItem (Python parameter) — The new mapping item to replace an existing one of the same name")*)[¶](#ApiClient.GlobalMapping.ReplaceItem "Link to this definition")  
Replaces a mapping item from the mapping

Parameters:  mappingItem[¶](#ApiClient.GlobalMapping.ReplaceItem.mappingItem "Permalink to this definition")  
The new mapping item to replace an existing one of the same name

Save(*[filename](#ApiClient.GlobalMapping.Save.filename "ApiClient.GlobalMapping.Save.filename (Python parameter) — File name of the mapping file; Either absolute or relative to the 'Parameters' directory.")=`''`*)[¶](#ApiClient.GlobalMapping.Save "Link to this definition")  
Saves the mapping space as an .xam file. Appends file ending if needed.

Parameters:  filename : str[¶](#ApiClient.GlobalMapping.Save.filename "Permalink to this definition")  
File name of the mapping file; Either absolute or relative to the ‘Parameters’ directory. If left out, use the existing file name and path (from a previous call of [`Save()`](#ApiClient.GlobalMapping.Save "ApiClient.GlobalMapping.Save (Python method) — Saves the mapping space as an .xam file. Appends file ending if needed.") or `MappingApi.OpenMapping()`)

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
