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

AutoAssignSignalGroup [ AutoAssignSignalGroup ](#)

AutoAssignSignalGroup

- [C AutoAssignSignalGroup ](#ApiClient.AutoAssignSignalGroup)
  - [M AppendMappingItem ](#ApiClient.AutoAssignSignalGroup.AppendMappingItem)
  - [M GetDescription ](#ApiClient.AutoAssignSignalGroup.GetDescription)
  - [M GetMappingItemNames ](#ApiClient.AutoAssignSignalGroup.GetMappingItemNames)
  - [M GetMappingItems ](#ApiClient.AutoAssignSignalGroup.GetMappingItems)
  - [M GetName ](#ApiClient.AutoAssignSignalGroup.GetName)
  - [M GetRecordingGroup ](#ApiClient.AutoAssignSignalGroup.GetRecordingGroup)
  - [M RemoveMappingItem ](#ApiClient.AutoAssignSignalGroup.RemoveMappingItem)
  - [M SetDescription ](#ApiClient.AutoAssignSignalGroup.SetDescription)

[ LocalMapping ](LocalMapping.md)

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

AutoAssignSignalGroup

- [C AutoAssignSignalGroup ](#ApiClient.AutoAssignSignalGroup)
  - [M AppendMappingItem ](#ApiClient.AutoAssignSignalGroup.AppendMappingItem)
  - [M GetDescription ](#ApiClient.AutoAssignSignalGroup.GetDescription)
  - [M GetMappingItemNames ](#ApiClient.AutoAssignSignalGroup.GetMappingItemNames)
  - [M GetMappingItems ](#ApiClient.AutoAssignSignalGroup.GetMappingItems)
  - [M GetName ](#ApiClient.AutoAssignSignalGroup.GetName)
  - [M GetRecordingGroup ](#ApiClient.AutoAssignSignalGroup.GetRecordingGroup)
  - [M RemoveMappingItem ](#ApiClient.AutoAssignSignalGroup.RemoveMappingItem)
  - [M SetDescription ](#ApiClient.AutoAssignSignalGroup.SetDescription)

# AutoAssignSignalGroup[¶](#autoassignsignalgroup "Link to this heading")

*class* AutoAssignSignalGroup[¶](#ApiClient.AutoAssignSignalGroup "Link to this definition")  
API to access the auto assign signal group. Signals of a signal group are represented by references to mapping items. This signal group is available per default. Signals added to this group will be automatically assigned to matching existing signal groups during package execution.

AppendMappingItem(*[mappingItem](#ApiClient.AutoAssignSignalGroup.AppendMappingItem.mappingItem "ApiClient.AutoAssignSignalGroup.AppendMappingItem.mappingItem (Python parameter) — The mapping item to be added")*)[¶](#ApiClient.AutoAssignSignalGroup.AppendMappingItem "Link to this definition")  
Adds a mapping item to the signal group.

Parameters:  mappingItem[¶](#ApiClient.AutoAssignSignalGroup.AppendMappingItem.mappingItem "Permalink to this definition")  
The mapping item to be added

GetDescription()[¶](#ApiClient.AutoAssignSignalGroup.GetDescription "Link to this definition")  
Returns the description of the signal group.

Returns:  The description of the signal group.

Return type:  str

GetMappingItemNames()[¶](#ApiClient.AutoAssignSignalGroup.GetMappingItemNames "Link to this definition")  
Returns the names of all the mapping Items within the signal group.

Returns:  List of all the mapping item names

Return type:  list[str]

GetMappingItems()[¶](#ApiClient.AutoAssignSignalGroup.GetMappingItems "Link to this definition")  
Returns a list of all resolved mapping items (representing the signals) within the signal group. Mapping items can be a part of the package’s mapping or of the global mapping if any is loaded.

Returns:  List of all resolved mapping items.

Return type:  list[[`MappingItem`](../MappingApi/MappingItem.md#ApiClient.MappingItem "ApiClient.MappingItem (Python class) — MappingApi.CreateGenericMappingItem")]

GetName()[¶](#ApiClient.AutoAssignSignalGroup.GetName "Link to this definition")  
Returns the name of the signal group.

Returns:  The name

Return type:  str

GetRecordingGroup()[¶](#ApiClient.AutoAssignSignalGroup.GetRecordingGroup "Link to this definition")  
Returns the recording group of the auto assign signal group. This group is needed to bind signals to trace analyses.

Returns:  The auto assign recording group

Return type:  [`AutoAssignRecordingGroup`](AutoAssignRecordingGroup.md#ApiClient.AutoAssignRecordingGroup "ApiClient.AutoAssignRecordingGroup (Python class) — Returns the list of signal names that can be optional or mandatory for running the trace analyses depending on the values of global constants.")

RemoveMappingItem(*[mappingItemName](#ApiClient.AutoAssignSignalGroup.RemoveMappingItem.mappingItemName "ApiClient.AutoAssignSignalGroup.RemoveMappingItem.mappingItemName (Python parameter) — The mapping item name")*)[¶](#ApiClient.AutoAssignSignalGroup.RemoveMappingItem "Link to this definition")  
Removes a mapping item from the signal group.

Parameters:  mappingItemName : str[¶](#ApiClient.AutoAssignSignalGroup.RemoveMappingItem.mappingItemName "Permalink to this definition")  
The mapping item name

SetDescription(*[description](#ApiClient.AutoAssignSignalGroup.SetDescription.description "ApiClient.AutoAssignSignalGroup.SetDescription.description (Python parameter) — The new description of the signal group.")*)[¶](#ApiClient.AutoAssignSignalGroup.SetDescription "Link to this definition")  
Sets the description of the signal group.

Parameters:  description : str[¶](#ApiClient.AutoAssignSignalGroup.SetDescription.description "Permalink to this definition")  
The new description of the signal group.

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
