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

API for Packages

[ AnalysisPackage ](AnalysisPackage.md)

[ Argument ](Argument.md)

[ Attributes ](Attributes.md)

[ AutoAssignRecordingGroup ](AutoAssignRecordingGroup.md)

[ AutoAssignSignalGroup ](AutoAssignSignalGroup.md)

LocalMapping [ LocalMapping ](#)

LocalMapping

- [C LocalMapping ](#ApiClient.LocalMapping)
  - [M AddItem ](#ApiClient.LocalMapping.AddItem)
  - [M Clone ](#ApiClient.LocalMapping.Clone)
  - [M GetItemByName ](#ApiClient.LocalMapping.GetItemByName)
  - [M GetItems ](#ApiClient.LocalMapping.GetItems)
  - [M GetItemsByTargetPath ](#ApiClient.LocalMapping.GetItemsByTargetPath)
  - [M HasItem ](#ApiClient.LocalMapping.HasItem)
  - [M RemoveItemByName ](#ApiClient.LocalMapping.RemoveItemByName)
  - [M ReplaceItem ](#ApiClient.LocalMapping.ReplaceItem)

[ MappingTestStep ](MappingTestStep.md)

[ MappingTestStepContainer ](MappingTestStepContainer.md)

[ Package ](Package.md)

[ RecordingConfig ](RecordingConfig.md)

[ Return ](Return.md)

[ TestStep ](TestStep.md)

[ TestStepContainer ](TestStepContainer.md)

[ TestStepRWBase ](TestStepRWBase.md)

[ Testcase ](Testcase.md)

[ TsAXSCall ](TsAXSCall.md)

[ TsBlockBase ](TsBlockBase.md)

[ TsBusMonitoring ](TsBusMonitoring.md)

[ TsCaseNodeBase ](TsCaseNodeBase.md)

[ TsSignalGroupOperation ](TsSignalGroupOperation.md)

[ TsSwitchBase ](TsSwitchBase.md)

[ TsUserInterface ](TsUserInterface.md)

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

LocalMapping

- [C LocalMapping ](#ApiClient.LocalMapping)
  - [M AddItem ](#ApiClient.LocalMapping.AddItem)
  - [M Clone ](#ApiClient.LocalMapping.Clone)
  - [M GetItemByName ](#ApiClient.LocalMapping.GetItemByName)
  - [M GetItems ](#ApiClient.LocalMapping.GetItems)
  - [M GetItemsByTargetPath ](#ApiClient.LocalMapping.GetItemsByTargetPath)
  - [M HasItem ](#ApiClient.LocalMapping.HasItem)
  - [M RemoveItemByName ](#ApiClient.LocalMapping.RemoveItemByName)
  - [M ReplaceItem ](#ApiClient.LocalMapping.ReplaceItem)

# LocalMapping[¶](#localmapping "Link to this heading")

*class* LocalMapping[¶](#ApiClient.LocalMapping "Link to this definition")  
AddItem(*[mappingItem](#ApiClient.LocalMapping.AddItem.mappingItem "ApiClient.LocalMapping.AddItem.mappingItem (Python parameter) — The mapping item to be added")*)[¶](#ApiClient.LocalMapping.AddItem "Link to this definition")  
Adds a mapping item to the mapping.

Parameters:  mappingItem[¶](#ApiClient.LocalMapping.AddItem.mappingItem "Permalink to this definition")  
The mapping item to be added

Clone()[¶](#ApiClient.LocalMapping.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`LocalMapping`](#ApiClient.LocalMapping "ApiClient.LocalMapping (Python class) — Adds a mapping item to the mapping.")

GetItemByName(*[name](#ApiClient.LocalMapping.GetItemByName.name "ApiClient.LocalMapping.GetItemByName.name (Python parameter) — The name of the mapping item to be searched for")*)[¶](#ApiClient.LocalMapping.GetItemByName "Link to this definition")  
Searches the mapping for the mapping item by its name and returns it if existing.

Parameters:  name : str[¶](#ApiClient.LocalMapping.GetItemByName.name "Permalink to this definition")  
The name of the mapping item to be searched for

Returns:  mapping item with the given name or None if no such mapping item exists

Return type:  [`MappingItem`](../MappingApi/MappingItem.md#ApiClient.MappingItem "ApiClient.MappingItem (Python class) — MappingApi.CreateGenericMappingItem")

GetItems()[¶](#ApiClient.LocalMapping.GetItems "Link to this definition")  
Returns a list of all the mapping items of the mapping.

Returns:  List of all the mapping items of the mapping.

Return type:  list[[`MappingItem`](../MappingApi/MappingItem.md#ApiClient.MappingItem "ApiClient.MappingItem (Python class) — MappingApi.CreateGenericMappingItem")]

GetItemsByTargetPath(*[targetPath](#ApiClient.LocalMapping.GetItemsByTargetPath.targetPath "ApiClient.LocalMapping.GetItemsByTargetPath.targetPath (Python parameter) — The target path of the mapping items to be searched for")*)[¶](#ApiClient.LocalMapping.GetItemsByTargetPath "Link to this definition")  
Searches the mapping for all mapping items that have the target path and returns them if existing.

Parameters:  targetPath : str[¶](#ApiClient.LocalMapping.GetItemsByTargetPath.targetPath "Permalink to this definition")  
The target path of the mapping items to be searched for

Returns:  List of mapping items that have the target path.

Return type:  list[[`MappingItem`](../MappingApi/MappingItem.md#ApiClient.MappingItem "ApiClient.MappingItem (Python class) — MappingApi.CreateGenericMappingItem")]

HasItem(*[mappingItem](#ApiClient.LocalMapping.HasItem.mappingItem "ApiClient.LocalMapping.HasItem.mappingItem (Python parameter) — The mapping item to be checked")*)[¶](#ApiClient.LocalMapping.HasItem "Link to this definition")  
Checks whether the given mapping item belongs to the mapping.

Parameters:  mappingItem[¶](#ApiClient.LocalMapping.HasItem.mappingItem "Permalink to this definition")  
The mapping item to be checked

Returns:  True if the given mapping item belongs to the mapping.

Return type:  boolean

RemoveItemByName(*[name](#ApiClient.LocalMapping.RemoveItemByName.name "ApiClient.LocalMapping.RemoveItemByName.name (Python parameter) — The name of the mapping item to be removed")*)[¶](#ApiClient.LocalMapping.RemoveItemByName "Link to this definition")  
Removes a mapping item from the mapping.

Parameters:  name : str[¶](#ApiClient.LocalMapping.RemoveItemByName.name "Permalink to this definition")  
The name of the mapping item to be removed

ReplaceItem(*[mappingItem](#ApiClient.LocalMapping.ReplaceItem.mappingItem "ApiClient.LocalMapping.ReplaceItem.mappingItem (Python parameter) — The new mapping item to replace an existing one of the same name")*)[¶](#ApiClient.LocalMapping.ReplaceItem "Link to this definition")  
Replaces a mapping item from the mapping

Parameters:  mappingItem[¶](#ApiClient.LocalMapping.ReplaceItem.mappingItem "Permalink to this definition")  
The new mapping item to replace an existing one of the same name

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
