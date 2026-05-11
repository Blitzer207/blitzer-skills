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

[ LocalMapping ](LocalMapping.md)

[ MappingTestStep ](MappingTestStep.md)

[ MappingTestStepContainer ](MappingTestStepContainer.md)

[ Package ](Package.md)

RecordingConfig [ RecordingConfig ](#)

RecordingConfig

- [C RecordingConfig ](#ApiClient.RecordingConfig)
  - [A TRACE_MERGE_MODE_DEPRECATED_MDF3 ](#ApiClient.RecordingConfig.TRACE_MERGE_MODE_DEPRECATED_MDF3)
  - [A TRACE_MERGE_MODE_MDF4_FILE_BASED ](#ApiClient.RecordingConfig.TRACE_MERGE_MODE_MDF4_FILE_BASED)
  - [A TRACE_MERGE_MODE_SIGNAL_BASED ](#ApiClient.RecordingConfig.TRACE_MERGE_MODE_SIGNAL_BASED)
  - [M AppendSignalGroup ](#ApiClient.RecordingConfig.AppendSignalGroup)
  - [M Clone ](#ApiClient.RecordingConfig.Clone)
  - [M GetAutoAssignSignalGroup ](#ApiClient.RecordingConfig.GetAutoAssignSignalGroup)
  - [M GetSignalGroups ](#ApiClient.RecordingConfig.GetSignalGroups)
  - [M GetSyncConfig ](#ApiClient.RecordingConfig.GetSyncConfig)
  - [M GetTraceMergeFilePathExpression ](#ApiClient.RecordingConfig.GetTraceMergeFilePathExpression)
  - [M GetTraceMergeMode ](#ApiClient.RecordingConfig.GetTraceMergeMode)
  - [M GetVariableRecordingGroup ](#ApiClient.RecordingConfig.GetVariableRecordingGroup)
  - [M IsRecordAllTestQuantities ](#ApiClient.RecordingConfig.IsRecordAllTestQuantities)
  - [M IsRecordAllTestQuantitiesRecursive ](#ApiClient.RecordingConfig.IsRecordAllTestQuantitiesRecursive)
  - [M IsTraceMergeActive ](#ApiClient.RecordingConfig.IsTraceMergeActive)
  - [M MigrateSyncConfig ](#ApiClient.RecordingConfig.MigrateSyncConfig)
  - [M MigrateSyncConfigUsing ](#ApiClient.RecordingConfig.MigrateSyncConfigUsing)
  - [M RemoveSignalGroup ](#ApiClient.RecordingConfig.RemoveSignalGroup)
  - [M SetRecordAllTestQuantities ](#ApiClient.RecordingConfig.SetRecordAllTestQuantities)
  - [M SetRecordAllTestQuantitiesRecursive ](#ApiClient.RecordingConfig.SetRecordAllTestQuantitiesRecursive)
  - [M SetTraceMergeActive ](#ApiClient.RecordingConfig.SetTraceMergeActive)
  - [M SetTraceMergeFilePathExpression ](#ApiClient.RecordingConfig.SetTraceMergeFilePathExpression)
  - [M SetTraceMergeMode ](#ApiClient.RecordingConfig.SetTraceMergeMode)

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

RecordingConfig

- [C RecordingConfig ](#ApiClient.RecordingConfig)
  - [A TRACE_MERGE_MODE_DEPRECATED_MDF3 ](#ApiClient.RecordingConfig.TRACE_MERGE_MODE_DEPRECATED_MDF3)
  - [A TRACE_MERGE_MODE_MDF4_FILE_BASED ](#ApiClient.RecordingConfig.TRACE_MERGE_MODE_MDF4_FILE_BASED)
  - [A TRACE_MERGE_MODE_SIGNAL_BASED ](#ApiClient.RecordingConfig.TRACE_MERGE_MODE_SIGNAL_BASED)
  - [M AppendSignalGroup ](#ApiClient.RecordingConfig.AppendSignalGroup)
  - [M Clone ](#ApiClient.RecordingConfig.Clone)
  - [M GetAutoAssignSignalGroup ](#ApiClient.RecordingConfig.GetAutoAssignSignalGroup)
  - [M GetSignalGroups ](#ApiClient.RecordingConfig.GetSignalGroups)
  - [M GetSyncConfig ](#ApiClient.RecordingConfig.GetSyncConfig)
  - [M GetTraceMergeFilePathExpression ](#ApiClient.RecordingConfig.GetTraceMergeFilePathExpression)
  - [M GetTraceMergeMode ](#ApiClient.RecordingConfig.GetTraceMergeMode)
  - [M GetVariableRecordingGroup ](#ApiClient.RecordingConfig.GetVariableRecordingGroup)
  - [M IsRecordAllTestQuantities ](#ApiClient.RecordingConfig.IsRecordAllTestQuantities)
  - [M IsRecordAllTestQuantitiesRecursive ](#ApiClient.RecordingConfig.IsRecordAllTestQuantitiesRecursive)
  - [M IsTraceMergeActive ](#ApiClient.RecordingConfig.IsTraceMergeActive)
  - [M MigrateSyncConfig ](#ApiClient.RecordingConfig.MigrateSyncConfig)
  - [M MigrateSyncConfigUsing ](#ApiClient.RecordingConfig.MigrateSyncConfigUsing)
  - [M RemoveSignalGroup ](#ApiClient.RecordingConfig.RemoveSignalGroup)
  - [M SetRecordAllTestQuantities ](#ApiClient.RecordingConfig.SetRecordAllTestQuantities)
  - [M SetRecordAllTestQuantitiesRecursive ](#ApiClient.RecordingConfig.SetRecordAllTestQuantitiesRecursive)
  - [M SetTraceMergeActive ](#ApiClient.RecordingConfig.SetTraceMergeActive)
  - [M SetTraceMergeFilePathExpression ](#ApiClient.RecordingConfig.SetTraceMergeFilePathExpression)
  - [M SetTraceMergeMode ](#ApiClient.RecordingConfig.SetTraceMergeMode)

# RecordingConfig[¶](#recordingconfig "Link to this heading")

*class* RecordingConfig[¶](#ApiClient.RecordingConfig "Link to this definition")  
TRACE_MERGE_MODE_DEPRECATED_MDF3[¶](#ApiClient.RecordingConfig.TRACE_MERGE_MODE_DEPRECATED_MDF3 "Link to this definition")  
Returns the constant used to specify the trace merge mode to the deprecated legacy MDF3 trace merge.

Returns:  The constant

Return type:  int

TRACE_MERGE_MODE_MDF4_FILE_BASED[¶](#ApiClient.RecordingConfig.TRACE_MERGE_MODE_MDF4_FILE_BASED "Link to this definition")  
Returns the constant used to specify the trace merge mode ‘signal-based in general, but file-based for MDF4 traces’.

Returns:  The constant

Return type:  int

TRACE_MERGE_MODE_SIGNAL_BASED[¶](#ApiClient.RecordingConfig.TRACE_MERGE_MODE_SIGNAL_BASED "Link to this definition")  
Returns the constant used to specify the trace merge mode ‘signal based’.

Returns:  The constant

Return type:  int

AppendSignalGroup(*[signalGroup](#ApiClient.RecordingConfig.AppendSignalGroup.signalGroup "ApiClient.RecordingConfig.AppendSignalGroup.signalGroup (Python parameter) — The signal group to be added")*, *[defaultRecordingGroup](#ApiClient.RecordingConfig.AppendSignalGroup.defaultRecordingGroup "ApiClient.RecordingConfig.AppendSignalGroup.defaultRecordingGroup (Python parameter) — The default recording group of the signal group")=`None`*, *[allowNewName](#ApiClient.RecordingConfig.AppendSignalGroup.allowNewName "ApiClient.RecordingConfig.AppendSignalGroup.allowNewName (Python parameter) — If True, a new name will be generated for the signal group if there already exists a signal group with the same name in the package. Default value is False, so an error will be raised if the name already exists.")=`False`*)[¶](#ApiClient.RecordingConfig.AppendSignalGroup "Link to this definition")  
Adds a signal group to the package. If no default recording group is given, a new recording group will be created.

Parameters:  signalGroup[¶](#ApiClient.RecordingConfig.AppendSignalGroup.signalGroup "Permalink to this definition")  
The signal group to be added

defaultRecordingGroup=`None`[¶](#ApiClient.RecordingConfig.AppendSignalGroup.defaultRecordingGroup "Permalink to this definition")  
The default recording group of the signal group

allowNewName : boolean[¶](#ApiClient.RecordingConfig.AppendSignalGroup.allowNewName "Permalink to this definition")  
If True, a new name will be generated for the signal group if there already exists a signal group with the same name in the package. Default value is False, so an error will be raised if the name already exists.

Clone()[¶](#ApiClient.RecordingConfig.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`RecordingConfig`](#ApiClient.RecordingConfig "ApiClient.RecordingConfig (Python class) — Returns the constant used to specify the trace merge mode to the deprecated legacy MDF3 trace merge.")

GetAutoAssignSignalGroup()[¶](#ApiClient.RecordingConfig.GetAutoAssignSignalGroup "Link to this definition")  
Returns the special auto assign signal group. This signal group is available per default. Signals added to this group will be automatically assigned to matching existing signal groups during package execution.

Returns:  The auto assign signal group

Return type:  [`AutoAssignSignalGroup`](AutoAssignSignalGroup.md#ApiClient.AutoAssignSignalGroup "ApiClient.AutoAssignSignalGroup (Python class) — API to access the auto assign signal group. Signals of a signal group are represented by references to mapping items. This signal group is available per default. Signals added to this group will be automatically assigned to matching existing signal groups during package execution.")

GetSignalGroups()[¶](#ApiClient.RecordingConfig.GetSignalGroups "Link to this definition")  
Returns a list of all the signal groups within the package. Signals and signal recording groups are attributed to their corresponding signal group.

Returns:  List of all the signal groups

Return type:  list[[`SignalGroup`](../SignalRecordingApi/SignalGroup.md#ApiClient.SignalGroup "ApiClient.SignalGroup (Python class) — API to access signal groups. Signals of a signal group are represented by references to mapping items.")]

GetSyncConfig()[¶](#ApiClient.RecordingConfig.GetSyncConfig "Link to this definition")  
Returns the synchronization configuration.

Returns:  The synchronization configuration

Return type:  [`SyncConfig`](../TraceAnalysisApi/SyncConfig.md#ApiClient.SyncConfig "ApiClient.SyncConfig (Python class) — Assigns an AUTOSAR Time Synchronization that synchronizes recordingGroup with masterGroup. If there is already a synchronization assigned to recordingGroup it will be unassigned.")

Raises:  
**ApiError** – when synchronization is done in trace analysis. Please migrate package with `MigrateSyncConfig()`.

GetTraceMergeFilePathExpression()[¶](#ApiClient.RecordingConfig.GetTraceMergeFilePathExpression "Link to this definition")  
Returns the path expression of the file where the traces are merged into.

Returns:  The path expression

Return type:  str

GetTraceMergeMode()[¶](#ApiClient.RecordingConfig.GetTraceMergeMode "Link to this definition")  
Returns the mode used to merged traces.

Returns:  The mode. One of [`RecordingConfig.TRACE_MERGE_MODE_SIGNAL_BASED`](#ApiClient.RecordingConfig.TRACE_MERGE_MODE_SIGNAL_BASED "ApiClient.RecordingConfig.TRACE_MERGE_MODE_SIGNAL_BASED (Python attribute) — Returns the constant used to specify the trace merge mode 'signal based'."), [`RecordingConfig.TRACE_MERGE_MODE_MDF4_FILE_BASED`](#ApiClient.RecordingConfig.TRACE_MERGE_MODE_MDF4_FILE_BASED "ApiClient.RecordingConfig.TRACE_MERGE_MODE_MDF4_FILE_BASED (Python attribute) — Returns the constant used to specify the trace merge mode 'signal-based in general, but file-based for MDF4 traces'."), [`RecordingConfig.TRACE_MERGE_MODE_DEPRECATED_MDF3`](#ApiClient.RecordingConfig.TRACE_MERGE_MODE_DEPRECATED_MDF3 "ApiClient.RecordingConfig.TRACE_MERGE_MODE_DEPRECATED_MDF3 (Python attribute) — Returns the constant used to specify the trace merge mode to the deprecated legacy MDF3 trace merge.")

Return type:  int

GetVariableRecordingGroup()[¶](#ApiClient.RecordingConfig.GetVariableRecordingGroup "Link to this definition")  
Returns the recording group representing recorded variables.

It can be used for the generic signal binding and trace synchronization of trace analyses as well as the assignment of recordings containing test case variables for the offline analysis.

Returns:  The variable recording group

Return type:  [`VariableRecordingGroup`](../SignalRecordingApi/VariableRecordingGroup.md#ApiClient.VariableRecordingGroup "ApiClient.VariableRecordingGroup (Python class) — Returns the constant used to specify the recording mode 'Auto-Start/Stop: complete test case'.")

IsRecordAllTestQuantities()[¶](#ApiClient.RecordingConfig.IsRecordAllTestQuantities "Link to this definition")  
Returns whether all test quantities shall be recorded.

For each test quantity there must be an existing signal group whose name matches the test quantity’s system under test or whose contained signals address the same system under test.

Returns:  True if all test quantities are recorded, else False.

Return type:  bool

IsRecordAllTestQuantitiesRecursive()[¶](#ApiClient.RecordingConfig.IsRecordAllTestQuantitiesRecursive "Link to this definition")  
Returns whether test quantities shall be collected recursively (including test quantities from sub packages) if the option to record all test quantities is set.

Returns:  True if test quantities shall be collected recursively.

Return type:  bool

IsTraceMergeActive()[¶](#ApiClient.RecordingConfig.IsTraceMergeActive "Link to this definition")  
Returns whether the merging of traces is activated.

Returns:  Activation status of trace merge

Return type:  boolean

MigrateSyncConfig()[¶](#ApiClient.RecordingConfig.MigrateSyncConfig "Link to this definition")  
Migrates synchronization and MDF3 merge configuration from trace analyses to the recording configuration.

The migration tries to be robust against differing settings for synchronizations, but if a conflict cannot be handled the migration will fail. In this case, use `MigrateSyncConfigUsing()`.

MDF3 merge and the adjustment of time axes in copied trace files will be set if any trace analysis uses them.

Raises:  
**ApiError** – when migration is not possible.

MigrateSyncConfigUsing(*[traceAnalysis](#ApiClient.RecordingConfig.MigrateSyncConfigUsing.traceAnalysis "ApiClient.RecordingConfig.MigrateSyncConfigUsing.traceAnalysis (Python parameter) — Use configuration from this trace analysis as new configuration.")*)[¶](#ApiClient.RecordingConfig.MigrateSyncConfigUsing "Link to this definition")  
Migrates synchronization and MDF3 merge configuration from a specific trace analysis to the recording configuration.

Parameters:  traceAnalysis[¶](#ApiClient.RecordingConfig.MigrateSyncConfigUsing.traceAnalysis "Permalink to this definition")  
Use configuration from this trace analysis as new configuration.

RemoveSignalGroup(*[signalGroup](#ApiClient.RecordingConfig.RemoveSignalGroup.signalGroup "ApiClient.RecordingConfig.RemoveSignalGroup.signalGroup (Python parameter) — The signal group to be removed")*)[¶](#ApiClient.RecordingConfig.RemoveSignalGroup "Link to this definition")  
Removes a signal group from the package. All relations to recording groups of the signal group will be lost.

Parameters:  signalGroup[¶](#ApiClient.RecordingConfig.RemoveSignalGroup.signalGroup "Permalink to this definition")  
The signal group to be removed

SetRecordAllTestQuantities(*[value](#ApiClient.RecordingConfig.SetRecordAllTestQuantities.value "ApiClient.RecordingConfig.SetRecordAllTestQuantities.value (Python parameter) — True if all test quantities shall be recorded.")*)[¶](#ApiClient.RecordingConfig.SetRecordAllTestQuantities "Link to this definition")  
Sets whether all test quantities shall be recorded.

For each test quantity there must be an existing signal group whose name matches the test quantity’s system under test or whose contained signals address the same system under test.

Parameters:  value : bool[¶](#ApiClient.RecordingConfig.SetRecordAllTestQuantities.value "Permalink to this definition")  
True if all test quantities shall be recorded.

SetRecordAllTestQuantitiesRecursive(*[value](#ApiClient.RecordingConfig.SetRecordAllTestQuantitiesRecursive.value "ApiClient.RecordingConfig.SetRecordAllTestQuantitiesRecursive.value (Python parameter) — True if test quantities shall be collected recursively.")*)[¶](#ApiClient.RecordingConfig.SetRecordAllTestQuantitiesRecursive "Link to this definition")  
Sets whether test quantities shall be collected recursively (including test quantities from sub packages) if the option to record all test quantities is set.

Parameters:  value : bool[¶](#ApiClient.RecordingConfig.SetRecordAllTestQuantitiesRecursive.value "Permalink to this definition")  
True if test quantities shall be collected recursively.

SetTraceMergeActive(*[active](#ApiClient.RecordingConfig.SetTraceMergeActive.active "ApiClient.RecordingConfig.SetTraceMergeActive.active (Python parameter) — If set to False, trace merge will be deactivated.")=`True`*)[¶](#ApiClient.RecordingConfig.SetTraceMergeActive "Link to this definition")  
Enables or disables the merging of traces.

Parameters:  active : boolean[¶](#ApiClient.RecordingConfig.SetTraceMergeActive.active "Permalink to this definition")  
If set to False, trace merge will be deactivated. Otherwise trace merge will be activated.

SetTraceMergeFilePathExpression(*[expression](#ApiClient.RecordingConfig.SetTraceMergeFilePathExpression.expression "ApiClient.RecordingConfig.SetTraceMergeFilePathExpression.expression (Python parameter) — The path expression")*)[¶](#ApiClient.RecordingConfig.SetTraceMergeFilePathExpression "Link to this definition")  
Sets the path expression of the file where the traces are merged into.

Parameters:  expression : str[¶](#ApiClient.RecordingConfig.SetTraceMergeFilePathExpression.expression "Permalink to this definition")  
The path expression

SetTraceMergeMode(*[mode](#ApiClient.RecordingConfig.SetTraceMergeMode.mode "ApiClient.RecordingConfig.SetTraceMergeMode.mode (Python parameter) — The mode.")*)[¶](#ApiClient.RecordingConfig.SetTraceMergeMode "Link to this definition")  
Sets the mode used to merged traces.

Parameters:  mode : int[¶](#ApiClient.RecordingConfig.SetTraceMergeMode.mode "Permalink to this definition")  
The mode. One of [`RecordingConfig.TRACE_MERGE_MODE_SIGNAL_BASED`](#ApiClient.RecordingConfig.TRACE_MERGE_MODE_SIGNAL_BASED "ApiClient.RecordingConfig.TRACE_MERGE_MODE_SIGNAL_BASED (Python attribute) — Returns the constant used to specify the trace merge mode 'signal based'."), [`RecordingConfig.TRACE_MERGE_MODE_MDF4_FILE_BASED`](#ApiClient.RecordingConfig.TRACE_MERGE_MODE_MDF4_FILE_BASED "ApiClient.RecordingConfig.TRACE_MERGE_MODE_MDF4_FILE_BASED (Python attribute) — Returns the constant used to specify the trace merge mode 'signal-based in general, but file-based for MDF4 traces'."), [`RecordingConfig.TRACE_MERGE_MODE_DEPRECATED_MDF3`](#ApiClient.RecordingConfig.TRACE_MERGE_MODE_DEPRECATED_MDF3 "ApiClient.RecordingConfig.TRACE_MERGE_MODE_DEPRECATED_MDF3 (Python attribute) — Returns the constant used to specify the trace merge mode to the deprecated legacy MDF3 trace merge.")

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
