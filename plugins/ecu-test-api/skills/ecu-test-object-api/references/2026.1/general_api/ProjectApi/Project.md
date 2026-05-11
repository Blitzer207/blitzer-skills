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

API for Projects

Project [ Project ](#)

Project

- [C Project ](#ApiClient.Project)
  - [A Attributes ](#ApiClient.Project.Attributes)
  - [A GlobalConstants ](#ApiClient.Project.GlobalConstants)
  - [A MappingFiles ](#ApiClient.Project.MappingFiles)
  - [A PackageParameters ](#ApiClient.Project.PackageParameters)
  - [M ActivateAbortOnSubprojectAbort ](#ApiClient.Project.ActivateAbortOnSubprojectAbort)
  - [M ActivateAutomaticValueRestore ](#ApiClient.Project.ActivateAutomaticValueRestore)
  - [M ActivateIndependentSubprojectExecution ](#ApiClient.Project.ActivateIndependentSubprojectExecution)
  - [M AppendComponent ](#ApiClient.Project.AppendComponent)
  - [M Clone ](#ApiClient.Project.Clone)
  - [M Close ](#ApiClient.Project.Close)
  - [M DeactivateAbortOnSubprojectAbort ](#ApiClient.Project.DeactivateAbortOnSubprojectAbort)
  - [M DeactivateAutomaticValueRestore ](#ApiClient.Project.DeactivateAutomaticValueRestore)
  - [M DeactivateIndependentSubprojectExecution ](#ApiClient.Project.DeactivateIndependentSubprojectExecution)
  - [M GetAllComponents ](#ApiClient.Project.GetAllComponents)
  - [M GetAnalysisPackageCalls ](#ApiClient.Project.GetAnalysisPackageCalls)
  - [M GetComponentByLineNo ](#ApiClient.Project.GetComponentByLineNo)
  - [M GetComponents ](#ApiClient.Project.GetComponents)
  - [M GetConfigChanges ](#ApiClient.Project.GetConfigChanges)
  - [M GetCustomRetryCondition ](#ApiClient.Project.GetCustomRetryCondition)
  - [M GetCustomRetryCount ](#ApiClient.Project.GetCustomRetryCount)
  - [M GetDescription ](#ApiClient.Project.GetDescription)
  - [M GetErrorRecoveryPkgLevel ](#ApiClient.Project.GetErrorRecoveryPkgLevel)
  - [M GetErrorRecoveryPkgPath ](#ApiClient.Project.GetErrorRecoveryPkgPath)
  - [M GetFilename ](#ApiClient.Project.GetFilename)
  - [M GetFolders ](#ApiClient.Project.GetFolders)
  - [M GetIndex ](#ApiClient.Project.GetIndex)
  - [M GetLineNo ](#ApiClient.Project.GetLineNo)
  - [M GetName ](#ApiClient.Project.GetName)
  - [M GetPackageCalls ](#ApiClient.Project.GetPackageCalls)
  - [M GetPackageGenerators ](#ApiClient.Project.GetPackageGenerators)
  - [M GetParameterGenerators ](#ApiClient.Project.GetParameterGenerators)
  - [M GetParameterSets ](#ApiClient.Project.GetParameterSets)
  - [M GetParameterVariationGenerators ](#ApiClient.Project.GetParameterVariationGenerators)
  - [M GetParent ](#ApiClient.Project.GetParent)
  - [M GetProjectCalls ](#ApiClient.Project.GetProjectCalls)
  - [M GetProjectGenerators ](#ApiClient.Project.GetProjectGenerators)
  - [M GetRandomExecutionOrderState ](#ApiClient.Project.GetRandomExecutionOrderState)
  - [M GetStimulationPackageCalls ](#ApiClient.Project.GetStimulationPackageCalls)
  - [M GetTestSuiteId ](#ApiClient.Project.GetTestSuiteId)
  - [M GetType ](#ApiClient.Project.GetType)
  - [M HasComponents ](#ApiClient.Project.HasComponents)
  - [M HasCustomErrorRecoveryPackageSettings ](#ApiClient.Project.HasCustomErrorRecoveryPackageSettings)
  - [M HasCustomRestoreSettings ](#ApiClient.Project.HasCustomRestoreSettings)
  - [M HasCustomRetrySettings ](#ApiClient.Project.HasCustomRetrySettings)
  - [M HasCustomSubprojectAbortSettings ](#ApiClient.Project.HasCustomSubprojectAbortSettings)
  - [M HasCustomSubprojectExecutionSettings ](#ApiClient.Project.HasCustomSubprojectExecutionSettings)
  - [M InsertComponent ](#ApiClient.Project.InsertComponent)
  - [M IsAbortOnSubprojectAbortActivated ](#ApiClient.Project.IsAbortOnSubprojectAbortActivated)
  - [M IsAbortOnSubprojectAbortDeactivated ](#ApiClient.Project.IsAbortOnSubprojectAbortDeactivated)
  - [M IsAutomaticValueRestoreActivated ](#ApiClient.Project.IsAutomaticValueRestoreActivated)
  - [M IsAutomaticValueRestoreDeactivated ](#ApiClient.Project.IsAutomaticValueRestoreDeactivated)
  - [M IsEnabled ](#ApiClient.Project.IsEnabled)
  - [M IsIndependentSubprojectExecutionActivated ](#ApiClient.Project.IsIndependentSubprojectExecutionActivated)
  - [M IsIndependentSubprojectExecutionDeactivated ](#ApiClient.Project.IsIndependentSubprojectExecutionDeactivated)
  - [M IsReported ](#ApiClient.Project.IsReported)
  - [M RemoveComponent ](#ApiClient.Project.RemoveComponent)
  - [M Save ](#ApiClient.Project.Save)
  - [M SaveAsArchive ](#ApiClient.Project.SaveAsArchive)
  - [M SetCustomRetryCondition ](#ApiClient.Project.SetCustomRetryCondition)
  - [M SetCustomRetryCount ](#ApiClient.Project.SetCustomRetryCount)
  - [M SetDescription ](#ApiClient.Project.SetDescription)
  - [M SetEnabled ](#ApiClient.Project.SetEnabled)
  - [M SetErrorRecoveryPkgLevel ](#ApiClient.Project.SetErrorRecoveryPkgLevel)
  - [M SetErrorRecoveryPkgPath ](#ApiClient.Project.SetErrorRecoveryPkgPath)
  - [M SetName ](#ApiClient.Project.SetName)
  - [M SetRandomExecutionState ](#ApiClient.Project.SetRandomExecutionState)
  - [M SetReported ](#ApiClient.Project.SetReported)
  - [M SetTestSuiteId ](#ApiClient.Project.SetTestSuiteId)
  - [M UseParentErrorRecoveryPackageSettings ](#ApiClient.Project.UseParentErrorRecoveryPackageSettings)
  - [M UseParentRetrySettings ](#ApiClient.Project.UseParentRetrySettings)
  - [M UseParentSubprojectAbortSettings ](#ApiClient.Project.UseParentSubprojectAbortSettings)
  - [M UseParentSubprojectExecutionSettings ](#ApiClient.Project.UseParentSubprojectExecutionSettings)
  - [M UseParentValueRestoreSettings ](#ApiClient.Project.UseParentValueRestoreSettings)
  - [M GetComponentByPosition ](#ApiClient.Project.GetComponentByPosition)
  - [M GetPosition ](#ApiClient.Project.GetPosition)

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

Project

- [C Project ](#ApiClient.Project)
  - [A Attributes ](#ApiClient.Project.Attributes)
  - [A GlobalConstants ](#ApiClient.Project.GlobalConstants)
  - [A MappingFiles ](#ApiClient.Project.MappingFiles)
  - [A PackageParameters ](#ApiClient.Project.PackageParameters)
  - [M ActivateAbortOnSubprojectAbort ](#ApiClient.Project.ActivateAbortOnSubprojectAbort)
  - [M ActivateAutomaticValueRestore ](#ApiClient.Project.ActivateAutomaticValueRestore)
  - [M ActivateIndependentSubprojectExecution ](#ApiClient.Project.ActivateIndependentSubprojectExecution)
  - [M AppendComponent ](#ApiClient.Project.AppendComponent)
  - [M Clone ](#ApiClient.Project.Clone)
  - [M Close ](#ApiClient.Project.Close)
  - [M DeactivateAbortOnSubprojectAbort ](#ApiClient.Project.DeactivateAbortOnSubprojectAbort)
  - [M DeactivateAutomaticValueRestore ](#ApiClient.Project.DeactivateAutomaticValueRestore)
  - [M DeactivateIndependentSubprojectExecution ](#ApiClient.Project.DeactivateIndependentSubprojectExecution)
  - [M GetAllComponents ](#ApiClient.Project.GetAllComponents)
  - [M GetAnalysisPackageCalls ](#ApiClient.Project.GetAnalysisPackageCalls)
  - [M GetComponentByLineNo ](#ApiClient.Project.GetComponentByLineNo)
  - [M GetComponents ](#ApiClient.Project.GetComponents)
  - [M GetConfigChanges ](#ApiClient.Project.GetConfigChanges)
  - [M GetCustomRetryCondition ](#ApiClient.Project.GetCustomRetryCondition)
  - [M GetCustomRetryCount ](#ApiClient.Project.GetCustomRetryCount)
  - [M GetDescription ](#ApiClient.Project.GetDescription)
  - [M GetErrorRecoveryPkgLevel ](#ApiClient.Project.GetErrorRecoveryPkgLevel)
  - [M GetErrorRecoveryPkgPath ](#ApiClient.Project.GetErrorRecoveryPkgPath)
  - [M GetFilename ](#ApiClient.Project.GetFilename)
  - [M GetFolders ](#ApiClient.Project.GetFolders)
  - [M GetIndex ](#ApiClient.Project.GetIndex)
  - [M GetLineNo ](#ApiClient.Project.GetLineNo)
  - [M GetName ](#ApiClient.Project.GetName)
  - [M GetPackageCalls ](#ApiClient.Project.GetPackageCalls)
  - [M GetPackageGenerators ](#ApiClient.Project.GetPackageGenerators)
  - [M GetParameterGenerators ](#ApiClient.Project.GetParameterGenerators)
  - [M GetParameterSets ](#ApiClient.Project.GetParameterSets)
  - [M GetParameterVariationGenerators ](#ApiClient.Project.GetParameterVariationGenerators)
  - [M GetParent ](#ApiClient.Project.GetParent)
  - [M GetProjectCalls ](#ApiClient.Project.GetProjectCalls)
  - [M GetProjectGenerators ](#ApiClient.Project.GetProjectGenerators)
  - [M GetRandomExecutionOrderState ](#ApiClient.Project.GetRandomExecutionOrderState)
  - [M GetStimulationPackageCalls ](#ApiClient.Project.GetStimulationPackageCalls)
  - [M GetTestSuiteId ](#ApiClient.Project.GetTestSuiteId)
  - [M GetType ](#ApiClient.Project.GetType)
  - [M HasComponents ](#ApiClient.Project.HasComponents)
  - [M HasCustomErrorRecoveryPackageSettings ](#ApiClient.Project.HasCustomErrorRecoveryPackageSettings)
  - [M HasCustomRestoreSettings ](#ApiClient.Project.HasCustomRestoreSettings)
  - [M HasCustomRetrySettings ](#ApiClient.Project.HasCustomRetrySettings)
  - [M HasCustomSubprojectAbortSettings ](#ApiClient.Project.HasCustomSubprojectAbortSettings)
  - [M HasCustomSubprojectExecutionSettings ](#ApiClient.Project.HasCustomSubprojectExecutionSettings)
  - [M InsertComponent ](#ApiClient.Project.InsertComponent)
  - [M IsAbortOnSubprojectAbortActivated ](#ApiClient.Project.IsAbortOnSubprojectAbortActivated)
  - [M IsAbortOnSubprojectAbortDeactivated ](#ApiClient.Project.IsAbortOnSubprojectAbortDeactivated)
  - [M IsAutomaticValueRestoreActivated ](#ApiClient.Project.IsAutomaticValueRestoreActivated)
  - [M IsAutomaticValueRestoreDeactivated ](#ApiClient.Project.IsAutomaticValueRestoreDeactivated)
  - [M IsEnabled ](#ApiClient.Project.IsEnabled)
  - [M IsIndependentSubprojectExecutionActivated ](#ApiClient.Project.IsIndependentSubprojectExecutionActivated)
  - [M IsIndependentSubprojectExecutionDeactivated ](#ApiClient.Project.IsIndependentSubprojectExecutionDeactivated)
  - [M IsReported ](#ApiClient.Project.IsReported)
  - [M RemoveComponent ](#ApiClient.Project.RemoveComponent)
  - [M Save ](#ApiClient.Project.Save)
  - [M SaveAsArchive ](#ApiClient.Project.SaveAsArchive)
  - [M SetCustomRetryCondition ](#ApiClient.Project.SetCustomRetryCondition)
  - [M SetCustomRetryCount ](#ApiClient.Project.SetCustomRetryCount)
  - [M SetDescription ](#ApiClient.Project.SetDescription)
  - [M SetEnabled ](#ApiClient.Project.SetEnabled)
  - [M SetErrorRecoveryPkgLevel ](#ApiClient.Project.SetErrorRecoveryPkgLevel)
  - [M SetErrorRecoveryPkgPath ](#ApiClient.Project.SetErrorRecoveryPkgPath)
  - [M SetName ](#ApiClient.Project.SetName)
  - [M SetRandomExecutionState ](#ApiClient.Project.SetRandomExecutionState)
  - [M SetReported ](#ApiClient.Project.SetReported)
  - [M SetTestSuiteId ](#ApiClient.Project.SetTestSuiteId)
  - [M UseParentErrorRecoveryPackageSettings ](#ApiClient.Project.UseParentErrorRecoveryPackageSettings)
  - [M UseParentRetrySettings ](#ApiClient.Project.UseParentRetrySettings)
  - [M UseParentSubprojectAbortSettings ](#ApiClient.Project.UseParentSubprojectAbortSettings)
  - [M UseParentSubprojectExecutionSettings ](#ApiClient.Project.UseParentSubprojectExecutionSettings)
  - [M UseParentValueRestoreSettings ](#ApiClient.Project.UseParentValueRestoreSettings)
  - [M GetComponentByPosition ](#ApiClient.Project.GetComponentByPosition)
  - [M GetPosition ](#ApiClient.Project.GetPosition)

# Project[¶](#project "Link to this heading")

*class* Project[¶](#ApiClient.Project "Link to this definition")  
Returned by

- [`ProjectApi.CreateProject`](../ProjectApi.md#ApiClient.ProjectApi.CreateProject "ApiClient.ProjectApi.CreateProject (Python method) — Creates a new project.")

- [`ProjectApi.OpenProject`](../ProjectApi.md#ApiClient.ProjectApi.OpenProject "ApiClient.ProjectApi.OpenProject (Python method) — Opens an existing project. The project may not be opened in ecu.test.")

- [`ProjectApi.OpenProjectFromArchive`](../ProjectApi.md#ApiClient.ProjectApi.OpenProjectFromArchive "ApiClient.ProjectApi.OpenProjectFromArchive (Python method) — Extracts an existing project archive into the current workspace and opens the main project.")

- [`ProjectApi.SearchProjects`](../ProjectApi.md#ApiClient.ProjectApi.SearchProjects "ApiClient.ProjectApi.SearchProjects (Python method) — Searches the current workspace and library workspaces for projects matching the given search criteria.")

Attributes[¶](#ApiClient.Project.Attributes "Link to this definition")  
Returns access to the package attributes definitions specified within the parameter set and the referenced package attribute definition files.

Returns:  Package attribute interface of the parameter set

Return type:  [`Attributes`](../PackageApi/Attributes.md#ApiClient.Attributes "ApiClient.Attributes (Python class) — API to access attributes")

GlobalConstants[¶](#ApiClient.Project.GlobalConstants "Link to this definition")  
Returns access to the global constants specified on the project component.

Returns:  Global constants interface of the project component

Return type:  [`GlobalConstants`](../ComponentApi/GlobalConstants.md#ApiClient.GlobalConstants "ApiClient.GlobalConstants (Python class) — Contains the global constants definition and references to global constants definition files.")

MappingFiles[¶](#ApiClient.Project.MappingFiles "Link to this definition")  
Returns access to the mapping file list

Returns:  Mapping file list object

Return type:  [`MappingFiles`](../ComponentApi/MappingFiles.md#ApiClient.MappingFiles "ApiClient.MappingFiles (Python class) — Adds an artifact reference to a mapping file to the list.")

PackageParameters[¶](#ApiClient.Project.PackageParameters "Link to this definition")  
Returns access to the package parameters specified on the project component.

Returns:  Package parameters interface of the project component

Return type:  [`PackageParameters`](../ComponentApi/PackageParameters.md#ApiClient.PackageParameters "ApiClient.PackageParameters (Python class) — Appends a package parameters definition file at the end of the list of referenced package parameters definition files.")

ActivateAbortOnSubprojectAbort()[¶](#ApiClient.Project.ActivateAbortOnSubprojectAbort "Link to this definition")  
Activates abort of whole project on abort of subprojects.

ActivateAutomaticValueRestore()[¶](#ApiClient.Project.ActivateAutomaticValueRestore "Link to this definition")  
Activates value restore of test quantities after the execution of every Package.

ActivateIndependentSubprojectExecution()[¶](#ApiClient.Project.ActivateIndependentSubprojectExecution "Link to this definition")  
Activates independent execution of subprojects.

AppendComponent(*[component](#ApiClient.Project.AppendComponent.component "ApiClient.Project.AppendComponent.component (Python parameter) — The project component to be appended")*)[¶](#ApiClient.Project.AppendComponent "Link to this definition")  
Adds a previously created component at the end of the project.

Parameters:  component[¶](#ApiClient.Project.AppendComponent.component "Permalink to this definition")  
The project component to be appended

Clone()[¶](#ApiClient.Project.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`Project`](#ApiClient.Project "ApiClient.Project (Python class) — ProjectApi.CreateProject")

Close()[¶](#ApiClient.Project.Close "Link to this definition")  
Closes the project. After closing the project it can not be modified/accessed anymore.

DeactivateAbortOnSubprojectAbort()[¶](#ApiClient.Project.DeactivateAbortOnSubprojectAbort "Link to this definition")  
Deactivate abort of whole project on abort of subprojects.

DeactivateAutomaticValueRestore()[¶](#ApiClient.Project.DeactivateAutomaticValueRestore "Link to this definition")  
Deactivate value restore of test quantities after the execution of every Package.

DeactivateIndependentSubprojectExecution()[¶](#ApiClient.Project.DeactivateIndependentSubprojectExecution "Link to this definition")  
Deactivate independent execution of subprojects.

GetAllComponents(*[skipDisabled](#ApiClient.Project.GetAllComponents.skipDisabled "ApiClient.Project.GetAllComponents.skipDisabled (Python parameter) — Defines whether disabled components should be excluded.")=`True`*)[¶](#ApiClient.Project.GetAllComponents "Link to this definition")  
Returns all components of the project

Parameters:  skipDisabled : boolean[¶](#ApiClient.Project.GetAllComponents.skipDisabled "Permalink to this definition")  
Defines whether disabled components should be excluded.

Returns:  Project components

Return type:  list[[`ProjectComponent`](../ComponentApi/ProjectComponent.md#ApiClient.ProjectComponent "ApiClient.ProjectComponent (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")]

GetAnalysisPackageCalls(*[skipDisabled](#ApiClient.Project.GetAnalysisPackageCalls.skipDisabled "ApiClient.Project.GetAnalysisPackageCalls.skipDisabled (Python parameter) — Defines whether disabled package calls should be excluded.")=`True`*, *[noParameterSets](#ApiClient.Project.GetAnalysisPackageCalls.noParameterSets "ApiClient.Project.GetAnalysisPackageCalls.noParameterSets (Python parameter) — Defines whether package calls with parameter sets should be excluded.")=`False`*)[¶](#ApiClient.Project.GetAnalysisPackageCalls "Link to this definition")  
Returns all analysis package calls of the project.

Parameters:  skipDisabled : boolean[¶](#ApiClient.Project.GetAnalysisPackageCalls.skipDisabled "Permalink to this definition")  
Defines whether disabled package calls should be excluded.

noParameterSets : boolean[¶](#ApiClient.Project.GetAnalysisPackageCalls.noParameterSets "Permalink to this definition")  
Defines whether package calls with parameter sets should be excluded.

Returns:  Package calls

Return type:  list[[`AnalysisPackageCall`](../ComponentApi/AnalysisPackageCall.md#ApiClient.AnalysisPackageCall "ApiClient.AnalysisPackageCall (Python class) — An analysis package call in a project.")]

GetComponentByLineNo(*[lineNo](#ApiClient.Project.GetComponentByLineNo.lineNo "ApiClient.Project.GetComponentByLineNo.lineNo (Python parameter) — Line number of component to be returned")*)[¶](#ApiClient.Project.GetComponentByLineNo "Link to this definition")  
Returns the component at a given line number of the project

Parameters:  lineNo : int[¶](#ApiClient.Project.GetComponentByLineNo.lineNo "Permalink to this definition")  
Line number of component to be returned

Returns:  Project component

Return type:  [`ProjectComponent`](../ComponentApi/ProjectComponent.md#ApiClient.ProjectComponent "ApiClient.ProjectComponent (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")

GetComponents()[¶](#ApiClient.Project.GetComponents "Link to this definition")  
Returns all direct children of the project.

Returns:  List with all children components

Return type:  list[[`ProjectComponent`](../ComponentApi/ProjectComponent.md#ApiClient.ProjectComponent "ApiClient.ProjectComponent (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")]

GetConfigChanges(*[skipDisabled](#ApiClient.Project.GetConfigChanges.skipDisabled "ApiClient.Project.GetConfigChanges.skipDisabled (Python parameter) — Defines whether disabled config changes should be excluded.")=`True`*)[¶](#ApiClient.Project.GetConfigChanges "Link to this definition")  
Returns all config changes of the project.

Parameters:  skipDisabled : boolean[¶](#ApiClient.Project.GetConfigChanges.skipDisabled "Permalink to this definition")  
Defines whether disabled config changes should be excluded.

Returns:  Config changes

Return type:  list[[`ConfigChange`](../ComponentApi/ConfigChange.md#ApiClient.ConfigChange "ApiClient.ConfigChange (Python class) — ComponentApi.CreateConfigChange")]

GetCustomRetryCondition()[¶](#ApiClient.Project.GetCustomRetryCondition "Link to this definition")  
Returns the condition of the custom retries. Returns one of the following:

- ‘ERROR’

- ‘FAILED’

- ‘ERROR/FAILED’

Returns:  The condition of the custom retry

Return type:  str

GetCustomRetryCount()[¶](#ApiClient.Project.GetCustomRetryCount "Link to this definition")  
Returns the number of the retries defined on the project component.

Returns:  Number of the custom retries

Return type:  integer

GetDescription()[¶](#ApiClient.Project.GetDescription "Link to this definition")  
Returns the description of the project.

Returns:  description text

Return type:  str

GetErrorRecoveryPkgLevel()[¶](#ApiClient.Project.GetErrorRecoveryPkgLevel "Link to this definition")  
Returns the conditions under which the error recovery package (configured via [`SetErrorRecoveryPkgPath()`](#ApiClient.Project.SetErrorRecoveryPkgPath "ApiClient.Project.SetErrorRecoveryPkgPath (Python method) — Sets the path for a Package to be executed upon abort of test execution or ERROR/FAILED.")) will be executed

This overrides settings from the parent element or from the test configuration.

Returns:  - -1 = disabled

- 0 = on abort only

- 1 = on ERROR and on abort

- 2 = on FAILED, ERROR and abort.

- None: use inherited setting from parent element or test configuration

Return type:  int

GetErrorRecoveryPkgPath()[¶](#ApiClient.Project.GetErrorRecoveryPkgPath "Link to this definition")  
Returns the path of the error recovery Package to be executed upon abort of test execution or ERROR/FAILED, if this element has a custom setting which overrides inherited settings from the parent element or from the test configuration.

see also [`GetErrorRecoveryPkgLevel()`](#ApiClient.Project.GetErrorRecoveryPkgLevel "ApiClient.Project.GetErrorRecoveryPkgLevel (Python method) — Returns the conditions under which the error recovery package (configured via SetErrorRecoveryPkgPath()) will be executed")

Returns:  Absolute path to Package file; None if inherited or explicitly disabled

Return type:  str

GetFilename()[¶](#ApiClient.Project.GetFilename "Link to this definition")  
Returns the file name of the project file as absolute path, if this is a file. If not it may be unsaved.

Returns:  The file name of the saved file or None, if not a file

Return type:  str

GetFolders(*[skipDisabled](#ApiClient.Project.GetFolders.skipDisabled "ApiClient.Project.GetFolders.skipDisabled (Python parameter) — Defines whether disabled folders should be excluded.")=`True`*)[¶](#ApiClient.Project.GetFolders "Link to this definition")  
Returns all folders of the project.

Parameters:  skipDisabled : boolean[¶](#ApiClient.Project.GetFolders.skipDisabled "Permalink to this definition")  
Defines whether disabled folders should be excluded.

Returns:  Folders

Return type:  list[[`ProjectFolder`](../ComponentApi/ProjectFolder.md#ApiClient.ProjectFolder "ApiClient.ProjectFolder (Python class) — ComponentApi.CreateFolder")]

GetIndex()[¶](#ApiClient.Project.GetIndex "Link to this definition")  
Returns the zero based index in the parent.

Returns:  Zero based index

Return type:  int

GetLineNo()[¶](#ApiClient.Project.GetLineNo "Link to this definition")  
Returns the line number within its project.

Returns:  Line number

Return type:  int

GetName()[¶](#ApiClient.Project.GetName "Link to this definition")  
Returns the name of the project component.

Returns:  Name of the component

Return type:  str

GetPackageCalls(*[skipDisabled](#ApiClient.Project.GetPackageCalls.skipDisabled "ApiClient.Project.GetPackageCalls.skipDisabled (Python parameter) — Defines whether disabled package calls should be excluded.")=`True`*, *[noParameterSets](#ApiClient.Project.GetPackageCalls.noParameterSets "ApiClient.Project.GetPackageCalls.noParameterSets (Python parameter) — Defines whether package calls with parameter sets should be excluded.")=`False`*)[¶](#ApiClient.Project.GetPackageCalls "Link to this definition")  
Returns all package calls of the project. This method excludes stimulation package calls and analysis package calls.

Parameters:  skipDisabled : boolean[¶](#ApiClient.Project.GetPackageCalls.skipDisabled "Permalink to this definition")  
Defines whether disabled package calls should be excluded.

noParameterSets : boolean[¶](#ApiClient.Project.GetPackageCalls.noParameterSets "Permalink to this definition")  
Defines whether package calls with parameter sets should be excluded.

Returns:  Package calls

Return type:  list[[`PackageCall`](../ComponentApi/PackageCall.md#ApiClient.PackageCall "ApiClient.PackageCall (Python class) — ComponentApi.CreatePackageCall")]

GetPackageGenerators(*[skipDisabled](#ApiClient.Project.GetPackageGenerators.skipDisabled "ApiClient.Project.GetPackageGenerators.skipDisabled (Python parameter) — Defines whether disabled generators should be excluded.")=`True`*)[¶](#ApiClient.Project.GetPackageGenerators "Link to this definition")  
Returns all package generators of the project.

Parameters:  skipDisabled : boolean[¶](#ApiClient.Project.GetPackageGenerators.skipDisabled "Permalink to this definition")  
Defines whether disabled generators should be excluded.

Returns:  PackageGenerator

Return type:  list[[`PackageGenerator`](../ComponentApi/PackageGenerator.md#ApiClient.PackageGenerator "ApiClient.PackageGenerator (Python class) — ComponentApi.CreatePackageGenerator")]

GetParameterGenerators(*[skipDisabled](#ApiClient.Project.GetParameterGenerators.skipDisabled "ApiClient.Project.GetParameterGenerators.skipDisabled (Python parameter) — Defines whether disabled generators should be excluded.")=`True`*)[¶](#ApiClient.Project.GetParameterGenerators "Link to this definition")  
Returns all parameter generators of the project.

Parameters:  skipDisabled : boolean[¶](#ApiClient.Project.GetParameterGenerators.skipDisabled "Permalink to this definition")  
Defines whether disabled generators should be excluded.

Returns:  ParameterGenerator

Return type:  list[[`ParameterGenerator`](../ComponentApi/ParameterGenerator.md#ApiClient.ParameterGenerator "ApiClient.ParameterGenerator (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")]

GetParameterSets(*[skipDisabled](#ApiClient.Project.GetParameterSets.skipDisabled "ApiClient.Project.GetParameterSets.skipDisabled (Python parameter) — Defines whether disabled parameter sets should be excluded.")=`True`*)[¶](#ApiClient.Project.GetParameterSets "Link to this definition")  
Returns all parameter sets of the project.

Parameters:  skipDisabled : boolean[¶](#ApiClient.Project.GetParameterSets.skipDisabled "Permalink to this definition")  
Defines whether disabled parameter sets should be excluded.

Returns:  Parameter records

Return type:  list[[`ParameterSet`](../ComponentApi/ParameterSet.md#ApiClient.ParameterSet "ApiClient.ParameterSet (Python class) — Returns access to the package attributes definitions specified within the parameter set and the referenced package attribute definition files.")]

GetParameterVariationGenerators(*[skipDisabled](#ApiClient.Project.GetParameterVariationGenerators.skipDisabled "ApiClient.Project.GetParameterVariationGenerators.skipDisabled (Python parameter) — Defines whether disabled generators should be excluded.")=`True`*)[¶](#ApiClient.Project.GetParameterVariationGenerators "Link to this definition")  
Returns all parameter generators of the project.

Parameters:  skipDisabled : boolean[¶](#ApiClient.Project.GetParameterVariationGenerators.skipDisabled "Permalink to this definition")  
Defines whether disabled generators should be excluded.

Returns:  ParameterGenerator

Return type:  list[[`ParameterVariationGeneratorComponent`](../ComponentApi/ParameterVariationGeneratorComponent.md#ApiClient.ParameterVariationGeneratorComponent "ApiClient.ParameterVariationGeneratorComponent (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")]

GetParent()[¶](#ApiClient.Project.GetParent "Link to this definition")  
Returns the parent project component.

Returns:  Parent component

Return type:  [`ProjectComponent`](../ComponentApi/ProjectComponent.md#ApiClient.ProjectComponent "ApiClient.ProjectComponent (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")

GetProjectCalls(*[skipDisabled](#ApiClient.Project.GetProjectCalls.skipDisabled "ApiClient.Project.GetProjectCalls.skipDisabled (Python parameter) — Defines whether disabled project calls should be excluded.")=`True`*)[¶](#ApiClient.Project.GetProjectCalls "Link to this definition")  
Returns all project calls of the project.

Parameters:  skipDisabled : boolean[¶](#ApiClient.Project.GetProjectCalls.skipDisabled "Permalink to this definition")  
Defines whether disabled project calls should be excluded.

Returns:  Project calls

Return type:  list[[`ProjectCall`](../ComponentApi/ProjectCall.md#ApiClient.ProjectCall "ApiClient.ProjectCall (Python class) — ComponentApi.CreateProjectCall")]

GetProjectGenerators(*[skipDisabled](#ApiClient.Project.GetProjectGenerators.skipDisabled "ApiClient.Project.GetProjectGenerators.skipDisabled (Python parameter) — Defines whether disabled generators should be excluded.")=`True`*)[¶](#ApiClient.Project.GetProjectGenerators "Link to this definition")  
Returns all project generators of the project.

Parameters:  skipDisabled : boolean[¶](#ApiClient.Project.GetProjectGenerators.skipDisabled "Permalink to this definition")  
Defines whether disabled generators should be excluded.

Returns:  ProjectGenerator

Return type:  list[[`ProjectGenerator`](../ComponentApi/ProjectGenerator.md#ApiClient.ProjectGenerator "ApiClient.ProjectGenerator (Python class) — ComponentApi.CreateProjectGenerator")]

GetRandomExecutionOrderState()[¶](#ApiClient.Project.GetRandomExecutionOrderState "Link to this definition")  
Returns the random execution state of this container.

Returns:  True if activated, False if deactivated or None if it is inherit from parent.

Return type:  boolean

GetStimulationPackageCalls(*[skipDisabled](#ApiClient.Project.GetStimulationPackageCalls.skipDisabled "ApiClient.Project.GetStimulationPackageCalls.skipDisabled (Python parameter) — Defines whether disabled package calls should be excluded.")=`True`*, *[noParameterSets](#ApiClient.Project.GetStimulationPackageCalls.noParameterSets "ApiClient.Project.GetStimulationPackageCalls.noParameterSets (Python parameter) — Defines whether package calls with parameter sets should be excluded.")=`False`*)[¶](#ApiClient.Project.GetStimulationPackageCalls "Link to this definition")  
Returns all stimulation package calls of the project.

Parameters:  skipDisabled : boolean[¶](#ApiClient.Project.GetStimulationPackageCalls.skipDisabled "Permalink to this definition")  
Defines whether disabled package calls should be excluded.

noParameterSets : boolean[¶](#ApiClient.Project.GetStimulationPackageCalls.noParameterSets "Permalink to this definition")  
Defines whether package calls with parameter sets should be excluded.

Returns:  Package calls

Return type:  list[[`StimulationPackageCall`](../ComponentApi/StimulationPackageCall.md#ApiClient.StimulationPackageCall "ApiClient.StimulationPackageCall (Python class) — A stimulation package call (of a package) in a project.")]

GetTestSuiteId()[¶](#ApiClient.Project.GetTestSuiteId "Link to this definition")  
Returns the test suite id of the project, if defined.

Returns:  Test suite id

Return type:  str

GetType()[¶](#ApiClient.Project.GetType "Link to this definition")  
Returns the type (class name) of the project component, e.g.  
- “ConfigChange”

- “ParameterSet”

- “PackageCall”

- “Project”

- “PackageGenerator”

Returns:  Type (class name) of the project component

Return type:  str

HasComponents()[¶](#ApiClient.Project.HasComponents "Link to this definition")  
Returns whether the project has children.

Returns:  True if there are children, False otherwise.

Return type:  boolean

HasCustomErrorRecoveryPackageSettings()[¶](#ApiClient.Project.HasCustomErrorRecoveryPackageSettings "Link to this definition")  
Returns whether the Package execution settings in case of test abort or ERROR/FAILED of the parent element are overridden

Returns:  True if this element has custom error recovery package settings that override the parent element’s settings or those from the test configuration

Return type:  boolean

HasCustomRestoreSettings()[¶](#ApiClient.Project.HasCustomRestoreSettings "Link to this definition")  
Returns if the value restore settings of the parent element are used or overridden by custom settings

Returns:  True if custom settings used, False if parent settings used

Return type:  boolean

HasCustomRetrySettings()[¶](#ApiClient.Project.HasCustomRetrySettings "Link to this definition")  
Returns if the retry settings of the parent element are used

Returns:  True if parent settings used, False if custom settings defined

Return type:  boolean

HasCustomSubprojectAbortSettings()[¶](#ApiClient.Project.HasCustomSubprojectAbortSettings "Link to this definition")  
Returns if the subprojects abort settings of the parent element are used or overridden by custom settings

Returns:  True if custom settings used, False if parent settings used

Return type:  boolean

HasCustomSubprojectExecutionSettings()[¶](#ApiClient.Project.HasCustomSubprojectExecutionSettings "Link to this definition")  
Returns if the subprojects execution settings of the parent element are used or overridden by custom settings

Returns:  True if custom settings used, False if parent settings used

Return type:  boolean

InsertComponent(*[component](#ApiClient.Project.InsertComponent.component "ApiClient.Project.InsertComponent.component (Python parameter) — The project component to be inserted")*, *[index](#ApiClient.Project.InsertComponent.index "ApiClient.Project.InsertComponent.index (Python parameter) — Index to insert the project component")*)[¶](#ApiClient.Project.InsertComponent "Link to this definition")  
Inserts a previously created component into the project at the given index.

Parameters:  component[¶](#ApiClient.Project.InsertComponent.component "Permalink to this definition")  
The project component to be inserted

index : int[¶](#ApiClient.Project.InsertComponent.index "Permalink to this definition")  
Index to insert the project component

IsAbortOnSubprojectAbortActivated()[¶](#ApiClient.Project.IsAbortOnSubprojectAbortActivated "Link to this definition")  
Returns if the abort of whole project on abort of subprojects is activated

Returns:  True if activated, else False

Return type:  boolean

IsAbortOnSubprojectAbortDeactivated()[¶](#ApiClient.Project.IsAbortOnSubprojectAbortDeactivated "Link to this definition")  
Returns if abort of whole project on abort of subprojects is deactivated

Returns:  True if deactivated, else False

Return type:  boolean

IsAutomaticValueRestoreActivated()[¶](#ApiClient.Project.IsAutomaticValueRestoreActivated "Link to this definition")  
Returns if the automatic value restore is activated

Returns:  True if activated, else False

Return type:  boolean

IsAutomaticValueRestoreDeactivated()[¶](#ApiClient.Project.IsAutomaticValueRestoreDeactivated "Link to this definition")  
Returns if the automatic value restore is deactivated

Returns:  True if deactivated, else False

Return type:  boolean

IsEnabled()[¶](#ApiClient.Project.IsEnabled "Link to this definition")  
Returns the state of the test step.

Returns:  True if test step is enabled, otherwise False

Return type:  bool

IsIndependentSubprojectExecutionActivated()[¶](#ApiClient.Project.IsIndependentSubprojectExecutionActivated "Link to this definition")  
Returns if the independent execution of subprojects is activated

Returns:  True if activated, else False

Return type:  boolean

IsIndependentSubprojectExecutionDeactivated()[¶](#ApiClient.Project.IsIndependentSubprojectExecutionDeactivated "Link to this definition")  
Returns if the independent execution of subprojects is deactivated

Returns:  True if deactivated, else False

Return type:  boolean

IsReported()[¶](#ApiClient.Project.IsReported "Link to this definition")  
Returns whether the test step will be reported. If it has a parent test step, this function will only return true if both this test step and the parent test step should be reported.

Returns:  True if test step will be reported, otherwise False

Return type:  bool

RemoveComponent(*[component](#ApiClient.Project.RemoveComponent.component "ApiClient.Project.RemoveComponent.component (Python parameter) — The project component to be removed")*)[¶](#ApiClient.Project.RemoveComponent "Link to this definition")  
Removes a previously created component from the project.

Parameters:  component[¶](#ApiClient.Project.RemoveComponent.component "Permalink to this definition")  
The project component to be removed

Raises:  
ApiError: - When component is not of type “ProjectComponent” - When the component is not part of the project

Save(*[filename](#ApiClient.Project.Save.filename "ApiClient.Project.Save.filename (Python parameter) — File name of the project; Either absolute or relative to the 'Packages' directory.")=`None`*)[¶](#ApiClient.Project.Save "Link to this definition")  
Saves the project. Appends file ending if needed.

Parameters:  filename : str[¶](#ApiClient.Project.Save.filename "Permalink to this definition")  
File name of the project; Either absolute or relative to the ‘Packages’ directory. If left out, use the existing file name and path (from a previous call of [`Save()`](#ApiClient.Project.Save "ApiClient.Project.Save (Python method) — Saves the project. Appends file ending if needed.") or [`ProjectApi.OpenProject()`](../ProjectApi.md#ApiClient.ProjectApi.OpenProject "ApiClient.ProjectApi.OpenProject (Python method) — Opens an existing project. The project may not be opened in ecu.test."))

SaveAsArchive(*[filename](#ApiClient.Project.SaveAsArchive.filename "ApiClient.Project.SaveAsArchive.filename (Python parameter) — File name of the project archive; either absolute or relative to the 'Packages' directory.")*)[¶](#ApiClient.Project.SaveAsArchive "Link to this definition")  
Saves the project and it’s dependencies as archive. Appends file ending if needed.

Parameters:  filename : str[¶](#ApiClient.Project.SaveAsArchive.filename "Permalink to this definition")  
File name of the project archive; either absolute or relative to the ‘Packages’ directory.

SetCustomRetryCondition(*[condition](#ApiClient.Project.SetCustomRetryCondition.condition "ApiClient.Project.SetCustomRetryCondition.condition (Python parameter) — The condition of the custom retry")*)[¶](#ApiClient.Project.SetCustomRetryCondition "Link to this definition")  
Sets the condition of the custom retry. Must be one of the following:

- ‘ERROR’

- ‘FAILED’

- ‘ERROR/FAILED’

Parameters:  condition : str[¶](#ApiClient.Project.SetCustomRetryCondition.condition "Permalink to this definition")  
The condition of the custom retry

SetCustomRetryCount(*[count](#ApiClient.Project.SetCustomRetryCount.count "ApiClient.Project.SetCustomRetryCount.count (Python parameter) — Number of the custom retries")*)[¶](#ApiClient.Project.SetCustomRetryCount "Link to this definition")  
Sets the number of the retries for all Packages within the project component.

Parameters:  count : integer[¶](#ApiClient.Project.SetCustomRetryCount.count "Permalink to this definition")  
Number of the custom retries

SetDescription(*[description](#ApiClient.Project.SetDescription.description "ApiClient.Project.SetDescription.description (Python parameter) — description text")*)[¶](#ApiClient.Project.SetDescription "Link to this definition")  
Sets the description of the project.

Parameters:  description : str[¶](#ApiClient.Project.SetDescription.description "Permalink to this definition")  
description text

SetEnabled(*[state](#ApiClient.Project.SetEnabled.state "ApiClient.Project.SetEnabled.state (Python parameter) — True (=Default) to enable, False to disable the test step.")=`True`*)[¶](#ApiClient.Project.SetEnabled "Link to this definition")  
Enable or disable the test step.

Parameters:  state : bool[¶](#ApiClient.Project.SetEnabled.state "Permalink to this definition")  
True (=Default) to enable, False to disable the test step.

SetErrorRecoveryPkgLevel(*[level](#ApiClient.Project.SetErrorRecoveryPkgLevel.level "ApiClient.Project.SetErrorRecoveryPkgLevel.level (Python parameter) — disabled")*)[¶](#ApiClient.Project.SetErrorRecoveryPkgLevel "Link to this definition")  
Sets the conditions under which the error recovery package (configured via [`SetErrorRecoveryPkgPath()`](#ApiClient.Project.SetErrorRecoveryPkgPath "ApiClient.Project.SetErrorRecoveryPkgPath (Python method) — Sets the path for a Package to be executed upon abort of test execution or ERROR/FAILED.")) will be executed

This overrides settings from the parent element or from the test configuration.

Parameters:  level : int[¶](#ApiClient.Project.SetErrorRecoveryPkgLevel.level "Permalink to this definition")  
- -1  
  disabled

- 0 on abort only

- 1 on ERROR and on abort

- 2 on FAILED, ERROR and abort.

SetErrorRecoveryPkgPath(*[packagePath](#ApiClient.Project.SetErrorRecoveryPkgPath.packagePath "ApiClient.Project.SetErrorRecoveryPkgPath.packagePath (Python parameter) — Absolute path to Package file")*)[¶](#ApiClient.Project.SetErrorRecoveryPkgPath "Link to this definition")  
Sets the path for a Package to be executed upon abort of test execution or ERROR/FAILED.

This overrides settings from the parent element or from the test configuration.

See also [`SetErrorRecoveryPkgLevel()`](#ApiClient.Project.SetErrorRecoveryPkgLevel "ApiClient.Project.SetErrorRecoveryPkgLevel (Python method) — Sets the conditions under which the error recovery package (configured via SetErrorRecoveryPkgPath()) will be executed")

Parameters:  packagePath : str[¶](#ApiClient.Project.SetErrorRecoveryPkgPath.packagePath "Permalink to this definition")  
Absolute path to Package file

SetName(*[name](#ApiClient.Project.SetName.name "ApiClient.Project.SetName.name (Python parameter) — Name of the component")*)[¶](#ApiClient.Project.SetName "Link to this definition")  
Sets the name of the project component.

Parameters:  name : str[¶](#ApiClient.Project.SetName.name "Permalink to this definition")  
Name of the component

SetRandomExecutionState(*[state](#ApiClient.Project.SetRandomExecutionState.state "ApiClient.Project.SetRandomExecutionState.state (Python parameter) — True to activate, False to deactivate or None for inheritance from parent.")*)[¶](#ApiClient.Project.SetRandomExecutionState "Link to this definition")  
Sets the random execution state of this container.

Parameters:  state : boolean[¶](#ApiClient.Project.SetRandomExecutionState.state "Permalink to this definition")  
True to activate, False to deactivate or None for inheritance from parent.

SetReported(*[state](#ApiClient.Project.SetReported.state "ApiClient.Project.SetReported.state (Python parameter) — True (=Default) to enable, False to disable the reporting of the test step.")=`True`*)[¶](#ApiClient.Project.SetReported "Link to this definition")  
Enable or disable the reporting of the test step. If it has a parent test step, its reporting must also be enabled in order to have this test step appear in the report.

Parameters:  state : bool[¶](#ApiClient.Project.SetReported.state "Permalink to this definition")  
True (=Default) to enable, False to disable the reporting of the test step.

SetTestSuiteId(*[tmId](#ApiClient.Project.SetTestSuiteId.tmId "ApiClient.Project.SetTestSuiteId.tmId (Python parameter) — Test suite id")*)[¶](#ApiClient.Project.SetTestSuiteId "Link to this definition")  
Sets the test suite id of the project.

Parameters:  tmId : str[¶](#ApiClient.Project.SetTestSuiteId.tmId "Permalink to this definition")  
Test suite id

UseParentErrorRecoveryPackageSettings()[¶](#ApiClient.Project.UseParentErrorRecoveryPackageSettings "Link to this definition")  
Sets that the Package execution settings in case of test abort or ERROR/FAILED of the parent element are used. Existing custom settings are deleted.

UseParentRetrySettings()[¶](#ApiClient.Project.UseParentRetrySettings "Link to this definition")  
Sets that the retry settings of the parent element are used. Existing custom settings are deleted.

UseParentSubprojectAbortSettings()[¶](#ApiClient.Project.UseParentSubprojectAbortSettings "Link to this definition")  
Sets that the settings whether to cancel or end the whole project execution on abort of a separately executed subproject of the parent element are used. Existing custom settings are deleted.

UseParentSubprojectExecutionSettings()[¶](#ApiClient.Project.UseParentSubprojectExecutionSettings "Link to this definition")  
Sets that the settings whether to execute subprojects independently of the parent element are used. Existing custom settings are deleted.

UseParentValueRestoreSettings()[¶](#ApiClient.Project.UseParentValueRestoreSettings "Link to this definition")  
Sets that the settings whether to restore the value of test quantities after the execution of every Package of the parent element are used. Existing custom settings are deleted.

GetComponentByPosition(*[position](#ApiClient.Project.GetComponentByPosition.position "ApiClient.Project.GetComponentByPosition.position (Python parameter) — Position of component to be returned")*)[¶](#ApiClient.Project.GetComponentByPosition "Link to this definition")  
Returns the component at a given position of the project

Parameters:  position : int[¶](#ApiClient.Project.GetComponentByPosition.position "Permalink to this definition")  
Position of component to be returned

Returns:  Project component

Return type:  [`ProjectComponent`](../ComponentApi/ProjectComponent.md#ApiClient.ProjectComponent "ApiClient.ProjectComponent (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")

Deprecated since version 2024.3: Please use method [`GetComponentByLineNo`](#ApiClient.Project.GetComponentByLineNo "ApiClient.Project.GetComponentByLineNo (Python method) — Returns the component at a given line number of the project") instead.

GetPosition()[¶](#ApiClient.Project.GetPosition "Link to this definition")  
Returns the position in the parent project.

Returns:  parent position

Return type:  int

Deprecated since version 2024.4: Please use method [`GetLineNo`](#ApiClient.Project.GetLineNo "ApiClient.Project.GetLineNo (Python method) — Returns the line number within its project.") instead.

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
