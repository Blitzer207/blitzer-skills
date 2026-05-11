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

[ ParameterSetRecordings ](ParameterSetRecordings.md)

[ ParameterVariationGeneratorComponent ](ParameterVariationGeneratorComponent.md)

[ ProjectCall ](ProjectCall.md)

[ ProjectComponent ](ProjectComponent.md)

ProjectFolder [ ProjectFolder ](#)

ProjectFolder

- [C ProjectFolder ](#ApiClient.ProjectFolder)
  - [A GlobalConstants ](#ApiClient.ProjectFolder.GlobalConstants)
  - [A MappingFiles ](#ApiClient.ProjectFolder.MappingFiles)
  - [A PackageParameters ](#ApiClient.ProjectFolder.PackageParameters)
  - [M ActivateAbortOnSubprojectAbort ](#ApiClient.ProjectFolder.ActivateAbortOnSubprojectAbort)
  - [M ActivateAutomaticValueRestore ](#ApiClient.ProjectFolder.ActivateAutomaticValueRestore)
  - [M ActivateIndependentSubprojectExecution ](#ApiClient.ProjectFolder.ActivateIndependentSubprojectExecution)
  - [M AppendComponent ](#ApiClient.ProjectFolder.AppendComponent)
  - [M Clone ](#ApiClient.ProjectFolder.Clone)
  - [M DeactivateAbortOnSubprojectAbort ](#ApiClient.ProjectFolder.DeactivateAbortOnSubprojectAbort)
  - [M DeactivateAutomaticValueRestore ](#ApiClient.ProjectFolder.DeactivateAutomaticValueRestore)
  - [M DeactivateIndependentSubprojectExecution ](#ApiClient.ProjectFolder.DeactivateIndependentSubprojectExecution)
  - [M GetComponents ](#ApiClient.ProjectFolder.GetComponents)
  - [M GetCustomRetryCondition ](#ApiClient.ProjectFolder.GetCustomRetryCondition)
  - [M GetCustomRetryCount ](#ApiClient.ProjectFolder.GetCustomRetryCount)
  - [M GetErrorRecoveryPkgLevel ](#ApiClient.ProjectFolder.GetErrorRecoveryPkgLevel)
  - [M GetErrorRecoveryPkgPath ](#ApiClient.ProjectFolder.GetErrorRecoveryPkgPath)
  - [M GetIndex ](#ApiClient.ProjectFolder.GetIndex)
  - [M GetLineNo ](#ApiClient.ProjectFolder.GetLineNo)
  - [M GetName ](#ApiClient.ProjectFolder.GetName)
  - [M GetParent ](#ApiClient.ProjectFolder.GetParent)
  - [M GetRandomExecutionOrderState ](#ApiClient.ProjectFolder.GetRandomExecutionOrderState)
  - [M GetType ](#ApiClient.ProjectFolder.GetType)
  - [M HasComponents ](#ApiClient.ProjectFolder.HasComponents)
  - [M HasCustomErrorRecoveryPackageSettings ](#ApiClient.ProjectFolder.HasCustomErrorRecoveryPackageSettings)
  - [M HasCustomRestoreSettings ](#ApiClient.ProjectFolder.HasCustomRestoreSettings)
  - [M HasCustomRetrySettings ](#ApiClient.ProjectFolder.HasCustomRetrySettings)
  - [M HasCustomSubprojectAbortSettings ](#ApiClient.ProjectFolder.HasCustomSubprojectAbortSettings)
  - [M HasCustomSubprojectExecutionSettings ](#ApiClient.ProjectFolder.HasCustomSubprojectExecutionSettings)
  - [M InsertComponent ](#ApiClient.ProjectFolder.InsertComponent)
  - [M IsAbortOnSubprojectAbortActivated ](#ApiClient.ProjectFolder.IsAbortOnSubprojectAbortActivated)
  - [M IsAbortOnSubprojectAbortDeactivated ](#ApiClient.ProjectFolder.IsAbortOnSubprojectAbortDeactivated)
  - [M IsAutomaticValueRestoreActivated ](#ApiClient.ProjectFolder.IsAutomaticValueRestoreActivated)
  - [M IsAutomaticValueRestoreDeactivated ](#ApiClient.ProjectFolder.IsAutomaticValueRestoreDeactivated)
  - [M IsEnabled ](#ApiClient.ProjectFolder.IsEnabled)
  - [M IsIndependentSubprojectExecutionActivated ](#ApiClient.ProjectFolder.IsIndependentSubprojectExecutionActivated)
  - [M IsIndependentSubprojectExecutionDeactivated ](#ApiClient.ProjectFolder.IsIndependentSubprojectExecutionDeactivated)
  - [M IsReported ](#ApiClient.ProjectFolder.IsReported)
  - [M RemoveComponent ](#ApiClient.ProjectFolder.RemoveComponent)
  - [M RemoveFromProject ](#ApiClient.ProjectFolder.RemoveFromProject)
  - [M SetCustomRetryCondition ](#ApiClient.ProjectFolder.SetCustomRetryCondition)
  - [M SetCustomRetryCount ](#ApiClient.ProjectFolder.SetCustomRetryCount)
  - [M SetEnabled ](#ApiClient.ProjectFolder.SetEnabled)
  - [M SetErrorRecoveryPkgLevel ](#ApiClient.ProjectFolder.SetErrorRecoveryPkgLevel)
  - [M SetErrorRecoveryPkgPath ](#ApiClient.ProjectFolder.SetErrorRecoveryPkgPath)
  - [M SetName ](#ApiClient.ProjectFolder.SetName)
  - [M SetRandomExecutionState ](#ApiClient.ProjectFolder.SetRandomExecutionState)
  - [M SetReported ](#ApiClient.ProjectFolder.SetReported)
  - [M UseParentErrorRecoveryPackageSettings ](#ApiClient.ProjectFolder.UseParentErrorRecoveryPackageSettings)
  - [M UseParentRetrySettings ](#ApiClient.ProjectFolder.UseParentRetrySettings)
  - [M UseParentSubprojectAbortSettings ](#ApiClient.ProjectFolder.UseParentSubprojectAbortSettings)
  - [M UseParentSubprojectExecutionSettings ](#ApiClient.ProjectFolder.UseParentSubprojectExecutionSettings)
  - [M UseParentValueRestoreSettings ](#ApiClient.ProjectFolder.UseParentValueRestoreSettings)
  - [M GetPosition ](#ApiClient.ProjectFolder.GetPosition)

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

ProjectFolder

- [C ProjectFolder ](#ApiClient.ProjectFolder)
  - [A GlobalConstants ](#ApiClient.ProjectFolder.GlobalConstants)
  - [A MappingFiles ](#ApiClient.ProjectFolder.MappingFiles)
  - [A PackageParameters ](#ApiClient.ProjectFolder.PackageParameters)
  - [M ActivateAbortOnSubprojectAbort ](#ApiClient.ProjectFolder.ActivateAbortOnSubprojectAbort)
  - [M ActivateAutomaticValueRestore ](#ApiClient.ProjectFolder.ActivateAutomaticValueRestore)
  - [M ActivateIndependentSubprojectExecution ](#ApiClient.ProjectFolder.ActivateIndependentSubprojectExecution)
  - [M AppendComponent ](#ApiClient.ProjectFolder.AppendComponent)
  - [M Clone ](#ApiClient.ProjectFolder.Clone)
  - [M DeactivateAbortOnSubprojectAbort ](#ApiClient.ProjectFolder.DeactivateAbortOnSubprojectAbort)
  - [M DeactivateAutomaticValueRestore ](#ApiClient.ProjectFolder.DeactivateAutomaticValueRestore)
  - [M DeactivateIndependentSubprojectExecution ](#ApiClient.ProjectFolder.DeactivateIndependentSubprojectExecution)
  - [M GetComponents ](#ApiClient.ProjectFolder.GetComponents)
  - [M GetCustomRetryCondition ](#ApiClient.ProjectFolder.GetCustomRetryCondition)
  - [M GetCustomRetryCount ](#ApiClient.ProjectFolder.GetCustomRetryCount)
  - [M GetErrorRecoveryPkgLevel ](#ApiClient.ProjectFolder.GetErrorRecoveryPkgLevel)
  - [M GetErrorRecoveryPkgPath ](#ApiClient.ProjectFolder.GetErrorRecoveryPkgPath)
  - [M GetIndex ](#ApiClient.ProjectFolder.GetIndex)
  - [M GetLineNo ](#ApiClient.ProjectFolder.GetLineNo)
  - [M GetName ](#ApiClient.ProjectFolder.GetName)
  - [M GetParent ](#ApiClient.ProjectFolder.GetParent)
  - [M GetRandomExecutionOrderState ](#ApiClient.ProjectFolder.GetRandomExecutionOrderState)
  - [M GetType ](#ApiClient.ProjectFolder.GetType)
  - [M HasComponents ](#ApiClient.ProjectFolder.HasComponents)
  - [M HasCustomErrorRecoveryPackageSettings ](#ApiClient.ProjectFolder.HasCustomErrorRecoveryPackageSettings)
  - [M HasCustomRestoreSettings ](#ApiClient.ProjectFolder.HasCustomRestoreSettings)
  - [M HasCustomRetrySettings ](#ApiClient.ProjectFolder.HasCustomRetrySettings)
  - [M HasCustomSubprojectAbortSettings ](#ApiClient.ProjectFolder.HasCustomSubprojectAbortSettings)
  - [M HasCustomSubprojectExecutionSettings ](#ApiClient.ProjectFolder.HasCustomSubprojectExecutionSettings)
  - [M InsertComponent ](#ApiClient.ProjectFolder.InsertComponent)
  - [M IsAbortOnSubprojectAbortActivated ](#ApiClient.ProjectFolder.IsAbortOnSubprojectAbortActivated)
  - [M IsAbortOnSubprojectAbortDeactivated ](#ApiClient.ProjectFolder.IsAbortOnSubprojectAbortDeactivated)
  - [M IsAutomaticValueRestoreActivated ](#ApiClient.ProjectFolder.IsAutomaticValueRestoreActivated)
  - [M IsAutomaticValueRestoreDeactivated ](#ApiClient.ProjectFolder.IsAutomaticValueRestoreDeactivated)
  - [M IsEnabled ](#ApiClient.ProjectFolder.IsEnabled)
  - [M IsIndependentSubprojectExecutionActivated ](#ApiClient.ProjectFolder.IsIndependentSubprojectExecutionActivated)
  - [M IsIndependentSubprojectExecutionDeactivated ](#ApiClient.ProjectFolder.IsIndependentSubprojectExecutionDeactivated)
  - [M IsReported ](#ApiClient.ProjectFolder.IsReported)
  - [M RemoveComponent ](#ApiClient.ProjectFolder.RemoveComponent)
  - [M RemoveFromProject ](#ApiClient.ProjectFolder.RemoveFromProject)
  - [M SetCustomRetryCondition ](#ApiClient.ProjectFolder.SetCustomRetryCondition)
  - [M SetCustomRetryCount ](#ApiClient.ProjectFolder.SetCustomRetryCount)
  - [M SetEnabled ](#ApiClient.ProjectFolder.SetEnabled)
  - [M SetErrorRecoveryPkgLevel ](#ApiClient.ProjectFolder.SetErrorRecoveryPkgLevel)
  - [M SetErrorRecoveryPkgPath ](#ApiClient.ProjectFolder.SetErrorRecoveryPkgPath)
  - [M SetName ](#ApiClient.ProjectFolder.SetName)
  - [M SetRandomExecutionState ](#ApiClient.ProjectFolder.SetRandomExecutionState)
  - [M SetReported ](#ApiClient.ProjectFolder.SetReported)
  - [M UseParentErrorRecoveryPackageSettings ](#ApiClient.ProjectFolder.UseParentErrorRecoveryPackageSettings)
  - [M UseParentRetrySettings ](#ApiClient.ProjectFolder.UseParentRetrySettings)
  - [M UseParentSubprojectAbortSettings ](#ApiClient.ProjectFolder.UseParentSubprojectAbortSettings)
  - [M UseParentSubprojectExecutionSettings ](#ApiClient.ProjectFolder.UseParentSubprojectExecutionSettings)
  - [M UseParentValueRestoreSettings ](#ApiClient.ProjectFolder.UseParentValueRestoreSettings)
  - [M GetPosition ](#ApiClient.ProjectFolder.GetPosition)

# ProjectFolder[¶](#projectfolder "Link to this heading")

*class* ProjectFolder[¶](#ApiClient.ProjectFolder "Link to this definition")  
Returned by

- [`ComponentApi.CreateFolder`](../ComponentApi.md#ApiClient.ComponentApi.CreateFolder "ApiClient.ComponentApi.CreateFolder (Python method) — Returns the created folder.")

GlobalConstants[¶](#ApiClient.ProjectFolder.GlobalConstants "Link to this definition")  
Returns access to the global constants specified on the project component.

Returns:  Global constants interface of the project component

Return type:  [`GlobalConstants`](GlobalConstants.md#ApiClient.GlobalConstants "ApiClient.GlobalConstants (Python class) — Contains the global constants definition and references to global constants definition files.")

MappingFiles[¶](#ApiClient.ProjectFolder.MappingFiles "Link to this definition")  
Returns access to the mapping file list

Returns:  Mapping file list object

Return type:  [`MappingFiles`](MappingFiles.md#ApiClient.MappingFiles "ApiClient.MappingFiles (Python class) — Adds an artifact reference to a mapping file to the list.")

PackageParameters[¶](#ApiClient.ProjectFolder.PackageParameters "Link to this definition")  
Returns access to the package parameters specified on the project component.

Returns:  Package parameters interface of the project component

Return type:  [`PackageParameters`](PackageParameters.md#ApiClient.PackageParameters "ApiClient.PackageParameters (Python class) — Appends a package parameters definition file at the end of the list of referenced package parameters definition files.")

ActivateAbortOnSubprojectAbort()[¶](#ApiClient.ProjectFolder.ActivateAbortOnSubprojectAbort "Link to this definition")  
Activates abort of whole project on abort of subprojects.

ActivateAutomaticValueRestore()[¶](#ApiClient.ProjectFolder.ActivateAutomaticValueRestore "Link to this definition")  
Activates value restore of test quantities after the execution of every Package.

ActivateIndependentSubprojectExecution()[¶](#ApiClient.ProjectFolder.ActivateIndependentSubprojectExecution "Link to this definition")  
Activates independent execution of subprojects.

AppendComponent(*[component](#ApiClient.ProjectFolder.AppendComponent.component "ApiClient.ProjectFolder.AppendComponent.component (Python parameter) — The project component to be appended")*)[¶](#ApiClient.ProjectFolder.AppendComponent "Link to this definition")  
Adds a previously created component at the end of the folder.

Parameters:  component[¶](#ApiClient.ProjectFolder.AppendComponent.component "Permalink to this definition")  
The project component to be appended

Clone()[¶](#ApiClient.ProjectFolder.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`ProjectFolder`](#ApiClient.ProjectFolder "ApiClient.ProjectFolder (Python class) — ComponentApi.CreateFolder")

DeactivateAbortOnSubprojectAbort()[¶](#ApiClient.ProjectFolder.DeactivateAbortOnSubprojectAbort "Link to this definition")  
Deactivate abort of whole project on abort of subprojects.

DeactivateAutomaticValueRestore()[¶](#ApiClient.ProjectFolder.DeactivateAutomaticValueRestore "Link to this definition")  
Deactivate value restore of test quantities after the execution of every Package.

DeactivateIndependentSubprojectExecution()[¶](#ApiClient.ProjectFolder.DeactivateIndependentSubprojectExecution "Link to this definition")  
Deactivate independent execution of subprojects.

GetComponents()[¶](#ApiClient.ProjectFolder.GetComponents "Link to this definition")  
Returns all direct children of the folder.

Returns:  List with all children components

Return type:  list[[`ProjectComponent`](ProjectComponent.md#ApiClient.ProjectComponent "ApiClient.ProjectComponent (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")]

GetCustomRetryCondition()[¶](#ApiClient.ProjectFolder.GetCustomRetryCondition "Link to this definition")  
Returns the condition of the custom retries. Returns one of the following:

- ‘ERROR’

- ‘FAILED’

- ‘ERROR/FAILED’

Returns:  The condition of the custom retry

Return type:  str

GetCustomRetryCount()[¶](#ApiClient.ProjectFolder.GetCustomRetryCount "Link to this definition")  
Returns the number of the retries defined on the project component.

Returns:  Number of the custom retries

Return type:  integer

GetErrorRecoveryPkgLevel()[¶](#ApiClient.ProjectFolder.GetErrorRecoveryPkgLevel "Link to this definition")  
Returns the conditions under which the error recovery package (configured via [`SetErrorRecoveryPkgPath()`](#ApiClient.ProjectFolder.SetErrorRecoveryPkgPath "ApiClient.ProjectFolder.SetErrorRecoveryPkgPath (Python method) — Sets the path for a Package to be executed upon abort of test execution or ERROR/FAILED.")) will be executed

This overrides settings from the parent element or from the test configuration.

Returns:  - -1 = disabled

- 0 = on abort only

- 1 = on ERROR and on abort

- 2 = on FAILED, ERROR and abort.

- None: use inherited setting from parent element or test configuration

Return type:  int

GetErrorRecoveryPkgPath()[¶](#ApiClient.ProjectFolder.GetErrorRecoveryPkgPath "Link to this definition")  
Returns the path of the error recovery Package to be executed upon abort of test execution or ERROR/FAILED, if this element has a custom setting which overrides inherited settings from the parent element or from the test configuration.

see also [`GetErrorRecoveryPkgLevel()`](#ApiClient.ProjectFolder.GetErrorRecoveryPkgLevel "ApiClient.ProjectFolder.GetErrorRecoveryPkgLevel (Python method) — Returns the conditions under which the error recovery package (configured via SetErrorRecoveryPkgPath()) will be executed")

Returns:  Absolute path to Package file; None if inherited or explicitly disabled

Return type:  str

GetIndex()[¶](#ApiClient.ProjectFolder.GetIndex "Link to this definition")  
Returns the zero based index in the parent.

Returns:  Zero based index

Return type:  int

GetLineNo()[¶](#ApiClient.ProjectFolder.GetLineNo "Link to this definition")  
Returns the line number within its project.

Returns:  Line number

Return type:  int

GetName()[¶](#ApiClient.ProjectFolder.GetName "Link to this definition")  
Returns the name of the project component.

Returns:  Name of the component

Return type:  str

GetParent()[¶](#ApiClient.ProjectFolder.GetParent "Link to this definition")  
Returns the parent project component.

Returns:  Parent component

Return type:  [`ProjectComponent`](ProjectComponent.md#ApiClient.ProjectComponent "ApiClient.ProjectComponent (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")

GetRandomExecutionOrderState()[¶](#ApiClient.ProjectFolder.GetRandomExecutionOrderState "Link to this definition")  
Returns the random execution state of this container.

Returns:  True if activated, False if deactivated or None if it is inherit from parent.

Return type:  boolean

GetType()[¶](#ApiClient.ProjectFolder.GetType "Link to this definition")  
Returns the type (class name) of the project component, e.g.  
- “ConfigChange”

- “ParameterSet”

- “PackageCall”

- “Project”

- “PackageGenerator”

Returns:  Type (class name) of the project component

Return type:  str

HasComponents()[¶](#ApiClient.ProjectFolder.HasComponents "Link to this definition")  
Returns whether the folder has children.

Returns:  True if there are children, False otherwise.

Return type:  boolean

HasCustomErrorRecoveryPackageSettings()[¶](#ApiClient.ProjectFolder.HasCustomErrorRecoveryPackageSettings "Link to this definition")  
Returns whether the Package execution settings in case of test abort or ERROR/FAILED of the parent element are overridden

Returns:  True if this element has custom error recovery package settings that override the parent element’s settings or those from the test configuration

Return type:  boolean

HasCustomRestoreSettings()[¶](#ApiClient.ProjectFolder.HasCustomRestoreSettings "Link to this definition")  
Returns if the value restore settings of the parent element are used or overridden by custom settings

Returns:  True if custom settings used, False if parent settings used

Return type:  boolean

HasCustomRetrySettings()[¶](#ApiClient.ProjectFolder.HasCustomRetrySettings "Link to this definition")  
Returns if the retry settings of the parent element are used

Returns:  True if parent settings used, False if custom settings defined

Return type:  boolean

HasCustomSubprojectAbortSettings()[¶](#ApiClient.ProjectFolder.HasCustomSubprojectAbortSettings "Link to this definition")  
Returns if the subprojects abort settings of the parent element are used or overridden by custom settings

Returns:  True if custom settings used, False if parent settings used

Return type:  boolean

HasCustomSubprojectExecutionSettings()[¶](#ApiClient.ProjectFolder.HasCustomSubprojectExecutionSettings "Link to this definition")  
Returns if the subprojects execution settings of the parent element are used or overridden by custom settings

Returns:  True if custom settings used, False if parent settings used

Return type:  boolean

InsertComponent(*[component](#ApiClient.ProjectFolder.InsertComponent.component "ApiClient.ProjectFolder.InsertComponent.component (Python parameter) — The project component to be inserted")*, *[index](#ApiClient.ProjectFolder.InsertComponent.index "ApiClient.ProjectFolder.InsertComponent.index (Python parameter) — Zero based index to insert the project component")*)[¶](#ApiClient.ProjectFolder.InsertComponent "Link to this definition")  
Inserts a previously created component into the folder at the given index.

Parameters:  component[¶](#ApiClient.ProjectFolder.InsertComponent.component "Permalink to this definition")  
The project component to be inserted

index : int[¶](#ApiClient.ProjectFolder.InsertComponent.index "Permalink to this definition")  
Zero based index to insert the project component

IsAbortOnSubprojectAbortActivated()[¶](#ApiClient.ProjectFolder.IsAbortOnSubprojectAbortActivated "Link to this definition")  
Returns if the abort of whole project on abort of subprojects is activated

Returns:  True if activated, else False

Return type:  boolean

IsAbortOnSubprojectAbortDeactivated()[¶](#ApiClient.ProjectFolder.IsAbortOnSubprojectAbortDeactivated "Link to this definition")  
Returns if abort of whole project on abort of subprojects is deactivated

Returns:  True if deactivated, else False

Return type:  boolean

IsAutomaticValueRestoreActivated()[¶](#ApiClient.ProjectFolder.IsAutomaticValueRestoreActivated "Link to this definition")  
Returns if the automatic value restore is activated

Returns:  True if activated, else False

Return type:  boolean

IsAutomaticValueRestoreDeactivated()[¶](#ApiClient.ProjectFolder.IsAutomaticValueRestoreDeactivated "Link to this definition")  
Returns if the automatic value restore is deactivated

Returns:  True if deactivated, else False

Return type:  boolean

IsEnabled()[¶](#ApiClient.ProjectFolder.IsEnabled "Link to this definition")  
Returns the state of the test step.

Returns:  True if test step is enabled, otherwise False

Return type:  bool

IsIndependentSubprojectExecutionActivated()[¶](#ApiClient.ProjectFolder.IsIndependentSubprojectExecutionActivated "Link to this definition")  
Returns if the independent execution of subprojects is activated

Returns:  True if activated, else False

Return type:  boolean

IsIndependentSubprojectExecutionDeactivated()[¶](#ApiClient.ProjectFolder.IsIndependentSubprojectExecutionDeactivated "Link to this definition")  
Returns if the independent execution of subprojects is deactivated

Returns:  True if deactivated, else False

Return type:  boolean

IsReported()[¶](#ApiClient.ProjectFolder.IsReported "Link to this definition")  
Returns whether the test step will be reported. If it has a parent test step, this function will only return true if both this test step and the parent test step should be reported.

Returns:  True if test step will be reported, otherwise False

Return type:  bool

RemoveComponent(*[component](#ApiClient.ProjectFolder.RemoveComponent.component "ApiClient.ProjectFolder.RemoveComponent.component (Python parameter) — The project component to be removed")*)[¶](#ApiClient.ProjectFolder.RemoveComponent "Link to this definition")  
Removes a component from the folder.

Parameters:  component[¶](#ApiClient.ProjectFolder.RemoveComponent.component "Permalink to this definition")  
The project component to be removed

Raises:  
**ApiError** – When the given component is not part of the project

RemoveFromProject()[¶](#ApiClient.ProjectFolder.RemoveFromProject "Link to this definition")  
Removes this component from the project.

Raises:  
**ApiError** – if the component is not part of any project

SetCustomRetryCondition(*[condition](#ApiClient.ProjectFolder.SetCustomRetryCondition.condition "ApiClient.ProjectFolder.SetCustomRetryCondition.condition (Python parameter) — The condition of the custom retry")*)[¶](#ApiClient.ProjectFolder.SetCustomRetryCondition "Link to this definition")  
Sets the condition of the custom retry. Must be one of the following:

- ‘ERROR’

- ‘FAILED’

- ‘ERROR/FAILED’

Parameters:  condition : str[¶](#ApiClient.ProjectFolder.SetCustomRetryCondition.condition "Permalink to this definition")  
The condition of the custom retry

SetCustomRetryCount(*[count](#ApiClient.ProjectFolder.SetCustomRetryCount.count "ApiClient.ProjectFolder.SetCustomRetryCount.count (Python parameter) — Number of the custom retries")*)[¶](#ApiClient.ProjectFolder.SetCustomRetryCount "Link to this definition")  
Sets the number of the retries for all Packages within the project component.

Parameters:  count : integer[¶](#ApiClient.ProjectFolder.SetCustomRetryCount.count "Permalink to this definition")  
Number of the custom retries

SetEnabled(*[state](#ApiClient.ProjectFolder.SetEnabled.state "ApiClient.ProjectFolder.SetEnabled.state (Python parameter) — True (=Default) to enable, False to disable the test step.")=`True`*)[¶](#ApiClient.ProjectFolder.SetEnabled "Link to this definition")  
Enable or disable the test step.

Parameters:  state : bool[¶](#ApiClient.ProjectFolder.SetEnabled.state "Permalink to this definition")  
True (=Default) to enable, False to disable the test step.

SetErrorRecoveryPkgLevel(*[level](#ApiClient.ProjectFolder.SetErrorRecoveryPkgLevel.level "ApiClient.ProjectFolder.SetErrorRecoveryPkgLevel.level (Python parameter) — disabled")*)[¶](#ApiClient.ProjectFolder.SetErrorRecoveryPkgLevel "Link to this definition")  
Sets the conditions under which the error recovery package (configured via [`SetErrorRecoveryPkgPath()`](#ApiClient.ProjectFolder.SetErrorRecoveryPkgPath "ApiClient.ProjectFolder.SetErrorRecoveryPkgPath (Python method) — Sets the path for a Package to be executed upon abort of test execution or ERROR/FAILED.")) will be executed

This overrides settings from the parent element or from the test configuration.

Parameters:  level : int[¶](#ApiClient.ProjectFolder.SetErrorRecoveryPkgLevel.level "Permalink to this definition")  
- -1  
  disabled

- 0 on abort only

- 1 on ERROR and on abort

- 2 on FAILED, ERROR and abort.

SetErrorRecoveryPkgPath(*[packagePath](#ApiClient.ProjectFolder.SetErrorRecoveryPkgPath.packagePath "ApiClient.ProjectFolder.SetErrorRecoveryPkgPath.packagePath (Python parameter) — Absolute path to Package file")*)[¶](#ApiClient.ProjectFolder.SetErrorRecoveryPkgPath "Link to this definition")  
Sets the path for a Package to be executed upon abort of test execution or ERROR/FAILED.

This overrides settings from the parent element or from the test configuration.

See also [`SetErrorRecoveryPkgLevel()`](#ApiClient.ProjectFolder.SetErrorRecoveryPkgLevel "ApiClient.ProjectFolder.SetErrorRecoveryPkgLevel (Python method) — Sets the conditions under which the error recovery package (configured via SetErrorRecoveryPkgPath()) will be executed")

Parameters:  packagePath : str[¶](#ApiClient.ProjectFolder.SetErrorRecoveryPkgPath.packagePath "Permalink to this definition")  
Absolute path to Package file

SetName(*[name](#ApiClient.ProjectFolder.SetName.name "ApiClient.ProjectFolder.SetName.name (Python parameter) — Name of the component")*)[¶](#ApiClient.ProjectFolder.SetName "Link to this definition")  
Sets the name of the project component.

Parameters:  name : str[¶](#ApiClient.ProjectFolder.SetName.name "Permalink to this definition")  
Name of the component

SetRandomExecutionState(*[state](#ApiClient.ProjectFolder.SetRandomExecutionState.state "ApiClient.ProjectFolder.SetRandomExecutionState.state (Python parameter) — True to activate, False to deactivate or None for inheritance from parent.")*)[¶](#ApiClient.ProjectFolder.SetRandomExecutionState "Link to this definition")  
Sets the random execution state of this container.

Parameters:  state : boolean[¶](#ApiClient.ProjectFolder.SetRandomExecutionState.state "Permalink to this definition")  
True to activate, False to deactivate or None for inheritance from parent.

SetReported(*[state](#ApiClient.ProjectFolder.SetReported.state "ApiClient.ProjectFolder.SetReported.state (Python parameter) — True (=Default) to enable, False to disable the reporting of the test step.")=`True`*)[¶](#ApiClient.ProjectFolder.SetReported "Link to this definition")  
Enable or disable the reporting of the test step. If it has a parent test step, its reporting must also be enabled in order to have this test step appear in the report.

Parameters:  state : bool[¶](#ApiClient.ProjectFolder.SetReported.state "Permalink to this definition")  
True (=Default) to enable, False to disable the reporting of the test step.

UseParentErrorRecoveryPackageSettings()[¶](#ApiClient.ProjectFolder.UseParentErrorRecoveryPackageSettings "Link to this definition")  
Sets that the Package execution settings in case of test abort or ERROR/FAILED of the parent element are used. Existing custom settings are deleted.

UseParentRetrySettings()[¶](#ApiClient.ProjectFolder.UseParentRetrySettings "Link to this definition")  
Sets that the retry settings of the parent element are used. Existing custom settings are deleted.

UseParentSubprojectAbortSettings()[¶](#ApiClient.ProjectFolder.UseParentSubprojectAbortSettings "Link to this definition")  
Sets that the settings whether to cancel or end the whole project execution on abort of a separately executed subproject of the parent element are used. Existing custom settings are deleted.

UseParentSubprojectExecutionSettings()[¶](#ApiClient.ProjectFolder.UseParentSubprojectExecutionSettings "Link to this definition")  
Sets that the settings whether to execute subprojects independently of the parent element are used. Existing custom settings are deleted.

UseParentValueRestoreSettings()[¶](#ApiClient.ProjectFolder.UseParentValueRestoreSettings "Link to this definition")  
Sets that the settings whether to restore the value of test quantities after the execution of every Package of the parent element are used. Existing custom settings are deleted.

GetPosition()[¶](#ApiClient.ProjectFolder.GetPosition "Link to this definition")  
Returns the position in the parent project.

Returns:  parent position

Return type:  int

Deprecated since version 2024.4: Please use method [`GetLineNo`](#ApiClient.ProjectFolder.GetLineNo "ApiClient.ProjectFolder.GetLineNo (Python method) — Returns the line number within its project.") instead.

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
