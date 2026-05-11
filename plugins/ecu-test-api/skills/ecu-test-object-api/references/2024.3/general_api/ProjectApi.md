# API for Projects[¶](#api-for-projects "Link to this heading")

Part of the [Object based program API](objectApi.md#objectapi)

## ProjectApi[¶](#projectapi "Link to this heading")

*class* ProjectApi[¶](#ApiClient.ProjectApi "Link to this definition")  
API to access projects

Returned by

- [`ApiClient.ProjectApi`](objectApi.md#ApiClient.ApiClient.ProjectApi "ApiClient.ApiClient.ProjectApi")

ComponentApi[¶](#ApiClient.ProjectApi.ComponentApi "Link to this definition")  
Returns the ComponentApi namespace.

Returns:  ComponentApi namespace

Return type:  [`ComponentApi`](ComponentApi.md#ApiClient.ComponentApi "ApiClient.ComponentApi")

CreateProject()[¶](#ApiClient.ProjectApi.CreateProject "Link to this definition")  
Creates a new project.

Returns:  New empty project

Return type:  [`Project`](#ApiClient.Project "ApiClient.Project")

GetChanges(*oldProject*, *newProject*)[¶](#ApiClient.ProjectApi.GetChanges "Link to this definition")  
Get the changes that exist between two given projects.

Parameters:  - **oldProject** ([`Project`](#ApiClient.Project "ApiClient.Project")) – The old project to compare.

- **newProject** ([`Project`](#ApiClient.Project "ApiClient.Project")) – The new project to compare.

Returns:  The changes that exist between the two projects.

Return type:  list[[`Change`](ConfigurationApi.md#ApiClient.Change "ApiClient.Change")]

OpenProject(*filename*, *execInCurrentPkgDir=False*, *filterExpression=''*)[¶](#ApiClient.ProjectApi.OpenProject "Link to this definition")  
Opens an existing project. The project may not be opened in ecu.test.

Parameters:  - **filename** (*str*) – Absolute path to the project file or relative path in regard to the package directory

- **execInCurrentPkgDir** (*boolean*) – Whether to treat relative references in the project like the project file “belongs” in the root of the current workspace’s package folder instead of its actual location.

- **filterExpression** (*str*) – A valid project filter expression

Returns:  Existing project

Return type:  [`Project`](#ApiClient.Project "ApiClient.Project")

OpenProjectFromArchive(*filename*)[¶](#ApiClient.ProjectApi.OpenProjectFromArchive "Link to this definition")  
Extracts an existing project archive into the current workspace and opens the main project.

Parameters:  **filename** (*str*) – Absolute path to the project archive file.

Returns:  Opened main project from extracted project archive

Return type:  [`Project`](#ApiClient.Project "ApiClient.Project")

SearchProjects(*searchCriteria*, *useExtendedMode=False*)[¶](#ApiClient.ProjectApi.SearchProjects "Link to this definition")  
Searches the current workspace and library workspaces for projects matching the given search criteria.

Parameters:  - **searchCriteria** (*str*) – The search criteria expressed in the ecu.test filter syntax. See section “Handling” =\> “Filter” of the ecu.test User Documentation.

- **useExtendedMode** (*boolean*) – If True, extended search strings are enabled. The default is False, meaning each word in the searchCriteria will be enclosed by wildcards and mapped to the filename. (e.g. “hello world” =\> “Name = ‘\*hello\*’ and Name = ‘\*world\*’”)

Returns:  All matching projects. If no project matches, an emtpy list is returned.

Return type:  list[[`Project`](#ApiClient.Project "ApiClient.Project")]

Raises:  
**ApiError** – If the searchCriteria has an illegal syntax.

## Project[¶](#project "Link to this heading")

*class* Project[¶](#ApiClient.Project "Link to this definition")  
Base classes

- [`ProjectComponent`](ComponentApi.md#ApiClient.ProjectComponent "ApiClient.ProjectComponent")

- [`ProjectFolder`](ComponentApi.md#ApiClient.ProjectFolder "ApiClient.ProjectFolder")

Returned by

- [`ProjectApi.CreateProject`](#ApiClient.ProjectApi.CreateProject "ApiClient.ProjectApi.CreateProject")

- [`ProjectApi.OpenProject`](#ApiClient.ProjectApi.OpenProject "ApiClient.ProjectApi.OpenProject")

- [`ProjectApi.OpenProjectFromArchive`](#ApiClient.ProjectApi.OpenProjectFromArchive "ApiClient.ProjectApi.OpenProjectFromArchive")

- [`ProjectApi.SearchProjects`](#ApiClient.ProjectApi.SearchProjects "ApiClient.ProjectApi.SearchProjects")

- [`ProjectCall.GetProject`](ComponentApi.md#ApiClient.ProjectCall.GetProject "ApiClient.ProjectCall.GetProject")

Attributes[¶](#ApiClient.Project.Attributes "Link to this definition")  
Returns access to the package attributes definitions specified within the parameter set and the referenced package attribute definition files.

Returns:  Package attribute interface of the parameter set

Return type:  [`Attributes`](#ApiClient.Attributes "ApiClient.Attributes")

GlobalConstants[¶](#ApiClient.Project.GlobalConstants "Link to this definition")  
Returns access to the global constants specified on the project component.

Returns:  Global constants interface of the project component

Return type:  [`GlobalConstants`](ComponentApi.md#ApiClient.GlobalConstants "ApiClient.GlobalConstants")

MappingFiles[¶](#ApiClient.Project.MappingFiles "Link to this definition")  
Returns access to the mapping file list

Returns:  Mapping file list object

Return type:  [`MappingFiles`](ComponentApi.md#ApiClient.MappingFiles "ApiClient.MappingFiles")

PackageParameters[¶](#ApiClient.Project.PackageParameters "Link to this definition")  
Returns access to the package parameters specified on the project component.

Returns:  Package parameters interface of the project component

Return type:  [`PackageParameters`](ComponentApi.md#ApiClient.PackageParameters "ApiClient.PackageParameters")

ActivateAbortOnSubprojectAbort()[¶](#ApiClient.Project.ActivateAbortOnSubprojectAbort "Link to this definition")  
Activates abort of whole project on abort of subprojects.

ActivateAutomaticValueRestore()[¶](#ApiClient.Project.ActivateAutomaticValueRestore "Link to this definition")  
Activates value restore of test quantities after the execution of every Package.

ActivateIndependentSubprojectExecution()[¶](#ApiClient.Project.ActivateIndependentSubprojectExecution "Link to this definition")  
Activates independent execution of subprojects.

AppendComponent(*component*)[¶](#ApiClient.Project.AppendComponent "Link to this definition")  
Adds a previously created component at the end of the project.

Parameters:  **component** ([`ProjectComponent`](ComponentApi.md#ApiClient.ProjectComponent "ApiClient.ProjectComponent")) – The project component to be appended

Clone()[¶](#ApiClient.Project.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`Project`](#ApiClient.Project "ApiClient.Project")

Close()[¶](#ApiClient.Project.Close "Link to this definition")  
Closes the project. After closing the project it can not be modified/accessed anymore.

DeactivateAbortOnSubprojectAbort()[¶](#ApiClient.Project.DeactivateAbortOnSubprojectAbort "Link to this definition")  
Deactivate abort of whole project on abort of subprojects.

DeactivateAutomaticValueRestore()[¶](#ApiClient.Project.DeactivateAutomaticValueRestore "Link to this definition")  
Deactivate value restore of test quantities after the execution of every Package.

DeactivateIndependentSubprojectExecution()[¶](#ApiClient.Project.DeactivateIndependentSubprojectExecution "Link to this definition")  
Deactivate independent execution of subprojects.

GetAllComponents(*skipDisabled=True*)[¶](#ApiClient.Project.GetAllComponents "Link to this definition")  
Returns all components of the project

Parameters:  **skipDisabled** (*boolean*) – Defines whether disabled components should be excluded.

Returns:  Project components

Return type:  list[[`ProjectComponent`](ComponentApi.md#ApiClient.ProjectComponent "ApiClient.ProjectComponent")]

GetAnalysisPackageCalls(*skipDisabled=True*, *noParameterSets=False*)[¶](#ApiClient.Project.GetAnalysisPackageCalls "Link to this definition")  
Returns all analysis package calls of the project.

Parameters:  - **skipDisabled** (*boolean*) – Defines whether disabled package calls should be excluded.

- **noParameterSets** (*boolean*) – Defines whether package calls with parameter sets should be excluded.

Returns:  Package calls

Return type:  list[[`AnalysisPackageCall`](ComponentApi.md#ApiClient.AnalysisPackageCall "ApiClient.AnalysisPackageCall")]

GetComponentByPosition(*position*)[¶](#ApiClient.Project.GetComponentByPosition "Link to this definition")  
Returns the component at a given position of the project

Parameters:  **position** (*integer*) – Position of component to be returned

Returns:  Project component

Return type:  [`ProjectComponent`](ComponentApi.md#ApiClient.ProjectComponent "ApiClient.ProjectComponent")

GetComponents()[¶](#ApiClient.Project.GetComponents "Link to this definition")  
Returns all direct children of the project.

Returns:  List with all children components

Return type:  list[[`ProjectComponent`](ComponentApi.md#ApiClient.ProjectComponent "ApiClient.ProjectComponent")]

GetConfigChanges(*skipDisabled=True*)[¶](#ApiClient.Project.GetConfigChanges "Link to this definition")  
Returns all config changes of the project.

Parameters:  **skipDisabled** (*boolean*) – Defines whether disabled config changes should be excluded.

Returns:  Config changes

Return type:  list[[`ConfigChange`](ComponentApi.md#ApiClient.ConfigChange "ApiClient.ConfigChange")]

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
Returns the conditions under which the error recovery package (configured via [`SetErrorRecoveryPkgPath()`](#ApiClient.Project.SetErrorRecoveryPkgPath "ApiClient.Project.SetErrorRecoveryPkgPath")) will be executed

This overrides settings from the parent element or from the test configuration.

Returns:  - -1 = disabled

- 0 = on abort only

- 1 = on ERROR and on abort

- 2 = on FAILED, ERROR and abort.

- None: use inherited setting from parent element or test configuration

Return type:  int

GetErrorRecoveryPkgPath()[¶](#ApiClient.Project.GetErrorRecoveryPkgPath "Link to this definition")  
Returns the path of the error recovery Package to be executed upon abort of test execution or ERROR/FAILED, if this element has a custom setting which overrides inherited settings from the parent element or from the test configuration.

see also [`GetErrorRecoveryPkgLevel()`](#ApiClient.Project.GetErrorRecoveryPkgLevel "ApiClient.Project.GetErrorRecoveryPkgLevel")

Returns:  Absolute path to Package file; None if inherited or explicitly disabled

Return type:  str

GetFilename()[¶](#ApiClient.Project.GetFilename "Link to this definition")  
Returns the file name of the project file as absolute path, if this is a file. If not it may be unsaved.

Returns:  The file name of the saved file or None, if not a file

Return type:  str

GetFolders(*skipDisabled=True*)[¶](#ApiClient.Project.GetFolders "Link to this definition")  
Returns all folders of the project.

Parameters:  **skipDisabled** (*boolean*) – Defines whether disabled folders should be excluded.

Returns:  Folders

Return type:  list[[`ProjectFolder`](ComponentApi.md#ApiClient.ProjectFolder "ApiClient.ProjectFolder")]

GetName()[¶](#ApiClient.Project.GetName "Link to this definition")  
Returns the name of the project component.

Returns:  Name of the component

Return type:  str

GetPackageCalls(*skipDisabled=True*, *noParameterSets=False*)[¶](#ApiClient.Project.GetPackageCalls "Link to this definition")  
Returns all package calls of the project. This method excludes stimulation package calls and analysis package calls.

Parameters:  - **skipDisabled** (*boolean*) – Defines whether disabled package calls should be excluded.

- **noParameterSets** (*boolean*) – Defines whether package calls with parameter sets should be excluded.

Returns:  Package calls

Return type:  list[[`PackageCall`](ComponentApi.md#ApiClient.PackageCall "ApiClient.PackageCall")]

GetPackageGenerators(*skipDisabled=True*)[¶](#ApiClient.Project.GetPackageGenerators "Link to this definition")  
Returns all package generators of the project.

Parameters:  **skipDisabled** (*boolean*) – Defines whether disabled generators should be excluded.

Returns:  PackageGenerator

Return type:  list[[`PackageGenerator`](ComponentApi.md#ApiClient.PackageGenerator "ApiClient.PackageGenerator")]

GetParameterGenerators(*skipDisabled=True*)[¶](#ApiClient.Project.GetParameterGenerators "Link to this definition")  
Returns all parameter generators of the project.

Parameters:  **skipDisabled** (*boolean*) – Defines whether disabled generators should be excluded.

Returns:  ParameterGenerator

Return type:  list[[`ParameterGenerator`](ComponentApi.md#ApiClient.ParameterGenerator "ApiClient.ParameterGenerator")]

GetParameterSets(*skipDisabled=True*)[¶](#ApiClient.Project.GetParameterSets "Link to this definition")  
Returns all parameter sets of the project.

Parameters:  **skipDisabled** (*boolean*) – Defines whether disabled parameter sets should be excluded.

Returns:  Parameter records

Return type:  list[[`ParameterSet`](#ApiClient.ParameterSet "ApiClient.ParameterSet")]

GetParameterVariationGenerators(*skipDisabled=True*)[¶](#ApiClient.Project.GetParameterVariationGenerators "Link to this definition")  
Returns all parameter generators of the project.

Parameters:  **skipDisabled** (*boolean*) – Defines whether disabled generators should be excluded.

Returns:  ParameterGenerator

Return type:  list[[`ParameterVariationGeneratorComponent`](ComponentApi.md#ApiClient.ParameterVariationGeneratorComponent "ApiClient.ParameterVariationGeneratorComponent")]

GetParent()[¶](#ApiClient.Project.GetParent "Link to this definition")  
Returns the parent project component.

Returns:  Parent component

Return type:  [`ProjectComponent`](ComponentApi.md#ApiClient.ProjectComponent "ApiClient.ProjectComponent")

GetPosition()[¶](#ApiClient.Project.GetPosition "Link to this definition")  
Returns the position in the parent project.

Returns:  parent position

Return type:  integer

GetProjectCalls(*skipDisabled=True*)[¶](#ApiClient.Project.GetProjectCalls "Link to this definition")  
Returns all project calls of the project.

Parameters:  **skipDisabled** (*boolean*) – Defines whether disabled project calls should be excluded.

Returns:  Project calls

Return type:  list[[`ProjectCall`](ComponentApi.md#ApiClient.ProjectCall "ApiClient.ProjectCall")]

GetProjectGenerators(*skipDisabled=True*)[¶](#ApiClient.Project.GetProjectGenerators "Link to this definition")  
Returns all project generators of the project.

Parameters:  **skipDisabled** (*boolean*) – Defines whether disabled generators should be excluded.

Returns:  ProjectGenerator

Return type:  list[[`ProjectGenerator`](ComponentApi.md#ApiClient.ProjectGenerator "ApiClient.ProjectGenerator")]

GetRandomExecutionOrderState()[¶](#ApiClient.Project.GetRandomExecutionOrderState "Link to this definition")  
Returns the random execution state of this container.

Returns:  True if activated, False if deactivated or None if it is inherit from parent.

Return type:  boolean

GetStimulationPackageCalls(*skipDisabled=True*, *noParameterSets=False*)[¶](#ApiClient.Project.GetStimulationPackageCalls "Link to this definition")  
Returns all stimulation package calls of the project.

Parameters:  - **skipDisabled** (*boolean*) – Defines whether disabled package calls should be excluded.

- **noParameterSets** (*boolean*) – Defines whether package calls with parameter sets should be excluded.

Returns:  Package calls

Return type:  list[[`StimulationPackageCall`](ComponentApi.md#ApiClient.StimulationPackageCall "ApiClient.StimulationPackageCall")]

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

InsertComponent(*component*, *position*)[¶](#ApiClient.Project.InsertComponent "Link to this definition")  
Inserts a previously created component into the project at the given position.

Parameters:  - **component** ([`ProjectComponent`](ComponentApi.md#ApiClient.ProjectComponent "ApiClient.ProjectComponent")) – The project component to be inserted

- **position** (*integer*) – Position to insert the project component

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

RemoveComponent(*component*)[¶](#ApiClient.Project.RemoveComponent "Link to this definition")  
Removes a previously created component from the project.

Parameters:  **component** ([`ProjectComponent`](ComponentApi.md#ApiClient.ProjectComponent "ApiClient.ProjectComponent")) – The project component to be removed

Raises:  
ApiError: - When component is not of type “ProjectComponent” - When the component is not part of the project

Save(*filename=None*)[¶](#ApiClient.Project.Save "Link to this definition")  
Saves the project. Appends file ending if needed.

Parameters:  **filename** (*str*) – File name of the project; Either absolute or relative to the ‘Packages’ directory. If left out, use the existing file name and path (from a previous call of [`Save()`](#ApiClient.Project.Save "ApiClient.Project.Save") or [`ProjectApi.OpenProject()`](#ApiClient.ProjectApi.OpenProject "ApiClient.ProjectApi.OpenProject"))

SaveAsArchive(*filename*)[¶](#ApiClient.Project.SaveAsArchive "Link to this definition")  
Saves the project and it’s dependencies as archive. Appends file ending if needed.

Parameters:  **filename** (*str*) – File name of the project archive; either absolute or relative to the ‘Packages’ directory.

SetCustomRetryCondition(*condition*)[¶](#ApiClient.Project.SetCustomRetryCondition "Link to this definition")  
Sets the condition of the custom retry. Must be one of the following:

- ‘ERROR’

- ‘FAILED’

- ‘ERROR/FAILED’

Parameters:  **condition** (*str*) – The condition of the custom retry

SetCustomRetryCount(*count*)[¶](#ApiClient.Project.SetCustomRetryCount "Link to this definition")  
Sets the number of the retries for all Packages within the project component.

Parameters:  **count** (*integer*) – Number of the custom retries

SetDescription(*description*)[¶](#ApiClient.Project.SetDescription "Link to this definition")  
Sets the description of the project.

Parameters:  **description** (*str*) – description text

SetEnabled(*state=True*)[¶](#ApiClient.Project.SetEnabled "Link to this definition")  
Enable or disable the test step.

Parameters:  **state** (*bool*) – True (=Default) to enable, False to disable the test step.

SetErrorRecoveryPkgLevel(*level*)[¶](#ApiClient.Project.SetErrorRecoveryPkgLevel "Link to this definition")  
Sets the conditions under which the error recovery package (configured via [`SetErrorRecoveryPkgPath()`](#ApiClient.Project.SetErrorRecoveryPkgPath "ApiClient.Project.SetErrorRecoveryPkgPath")) will be executed

This overrides settings from the parent element or from the test configuration.

Parameters:  **level** (*int*) –

- -1  
  disabled

- 0 on abort only

- 1 on ERROR and on abort

- 2 on FAILED, ERROR and abort.

SetErrorRecoveryPkgPath(*packagePath*)[¶](#ApiClient.Project.SetErrorRecoveryPkgPath "Link to this definition")  
Sets the path for a Package to be executed upon abort of test execution or ERROR/FAILED.

This overrides settings from the parent element or from the test configuration.

See also [`SetErrorRecoveryPkgLevel()`](#ApiClient.Project.SetErrorRecoveryPkgLevel "ApiClient.Project.SetErrorRecoveryPkgLevel")

Parameters:  **packagePath** (*str*) – Absolute path to Package file

SetName(*name*)[¶](#ApiClient.Project.SetName "Link to this definition")  
Sets the name of the project component.

Parameters:  **name** (*str*) – Name of the component

SetRandomExecutionState(*state*)[¶](#ApiClient.Project.SetRandomExecutionState "Link to this definition")  
Sets the random execution state of this container.

Parameters:  **state** (*boolean*) – True to activate, False to deactivate or None for inheritance from parent.

SetTestSuiteId(*tmId*)[¶](#ApiClient.Project.SetTestSuiteId "Link to this definition")  
Sets the test suite id of the project.

Parameters:  **tmId** (*str*) – Test suite id

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

## Attributes[¶](#attributes "Link to this heading")

*class* Attributes[¶](#ApiClient.Attributes "Link to this definition")  
API to access attributes

Returned by

- [`AnalysisPackage.Attributes`](PackageApi.md#ApiClient.AnalysisPackage.Attributes "ApiClient.AnalysisPackage.Attributes")

- [`Package.Attributes`](PackageApi.md#ApiClient.Package.Attributes "ApiClient.Package.Attributes")

- [`PackageBase.Attributes`](TraceAnalysisApi.md#ApiClient.PackageBase.Attributes "ApiClient.PackageBase.Attributes")

- [`ParameterSet.Attributes`](#ApiClient.ParameterSet.Attributes "ApiClient.ParameterSet.Attributes")

- [`ParameterSetAnalysisPackage.Attributes`](ComponentApi.md#ApiClient.ParameterSetAnalysisPackage.Attributes "ApiClient.ParameterSetAnalysisPackage.Attributes")

- [`ParameterSetBase.Attributes`](ComponentApi.md#ApiClient.ParameterSetBase.Attributes "ApiClient.ParameterSetBase.Attributes")

- [`Project.Attributes`](#ApiClient.Project.Attributes "ApiClient.Project.Attributes")

Clone()[¶](#ApiClient.Attributes.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`Attributes`](#ApiClient.Attributes "ApiClient.Attributes")

GetNames()[¶](#ApiClient.Attributes.GetNames "Link to this definition")  
Returns the names of all attributes available

Returns:  List of attribute names

Return type:  list[str]

GetNamesAndValues()[¶](#ApiClient.Attributes.GetNamesAndValues "Link to this definition")  
Returns all attributes with their values.

Returns:  Dictionary of attributes with values

Return type:  dict[str, str]

GetValue(*name*)[¶](#ApiClient.Attributes.GetValue "Link to this definition")  
Returns the value of the attribute of the provided name

Parameters:  **name** (*str*) – Name of attribute

Returns:  Value of attribute

Return type:  str

SetValue(*name*, *value*)[¶](#ApiClient.Attributes.SetValue "Link to this definition")  
Sets the value of an attribute with the provided name.

Parameters:  - **name** (*str*) – Name of attribute

- **value** (*str*) – Value of attribute

## ParameterSet[¶](#parameterset "Link to this heading")

*class* ParameterSet[¶](#ApiClient.ParameterSet "Link to this definition")  
Base classes

- [`ProjectComponent`](ComponentApi.md#ApiClient.ProjectComponent "ApiClient.ProjectComponent")

- [`ParameterSetBase`](ComponentApi.md#ApiClient.ParameterSetBase "ApiClient.ParameterSetBase")

Returned by

- [`PackageCall.AddParameterSet`](ComponentApi.md#ApiClient.PackageCall.AddParameterSet "ApiClient.PackageCall.AddParameterSet")

- [`PackageCall.GetParameterSets`](ComponentApi.md#ApiClient.PackageCall.GetParameterSets "ApiClient.PackageCall.GetParameterSets")

- [`Project.GetParameterSets`](#ApiClient.Project.GetParameterSets "ApiClient.Project.GetParameterSets")

- [`StimulationPackageCall.AddParameterSet`](ComponentApi.md#ApiClient.StimulationPackageCall.AddParameterSet "ApiClient.StimulationPackageCall.AddParameterSet")

- [`StimulationPackageCall.GetParameterSets`](ComponentApi.md#ApiClient.StimulationPackageCall.GetParameterSets "ApiClient.StimulationPackageCall.GetParameterSets")

Attributes[¶](#ApiClient.ParameterSet.Attributes "Link to this definition")  
Returns access to the package attributes definitions specified within the parameter set and the referenced package attribute definition files.

Returns:  Package attribute interface of the parameter set

Return type:  [`Attributes`](#ApiClient.Attributes "ApiClient.Attributes")

GlobalConstants[¶](#ApiClient.ParameterSet.GlobalConstants "Link to this definition")  
Returns access to the global constants definitions specified within the parameter set and the referenced global constants definition files.

Returns:  Global constants interface of the parameter set

Return type:  [`GlobalConstants`](ComponentApi.md#ApiClient.GlobalConstants "ApiClient.GlobalConstants")

Mapping[¶](#ApiClient.ParameterSet.Mapping "Link to this definition")  
Returns access to the mapping of the parameter set.

Returns:  Mapping interface of the parameter set

Return type:  [`ParameterSetMapping`](ComponentApi.md#ApiClient.ParameterSetMapping "ApiClient.ParameterSetMapping")

MappingFiles[¶](#ApiClient.ParameterSet.MappingFiles "Link to this definition")  
Returns access to the mapping file list of the parameter set.

Returns:  Mapping file list object of the parameter set

Return type:  [`MappingFiles`](ComponentApi.md#ApiClient.MappingFiles "ApiClient.MappingFiles")

Parameters[¶](#ApiClient.ParameterSet.Parameters "Link to this definition")  
Returns access to the package parameters definitions specified within the parameter set and the referenced package parameters definition files.

Returns:  Package parameters interface of the parameter set

Return type:  [`PackageParameters`](ComponentApi.md#ApiClient.PackageParameters "ApiClient.PackageParameters")

Recordings[¶](#ApiClient.ParameterSet.Recordings "Link to this definition")  
Returns access to the recordings of the parameter set.

Returns:  Recording interface of the parameter set

Return type:  [`ParameterSetRecordings`](#ApiClient.ParameterSetRecordings "ApiClient.ParameterSetRecordings")

Clone()[¶](#ApiClient.ParameterSet.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`ParameterSet`](#ApiClient.ParameterSet "ApiClient.ParameterSet")

GetAvailableRecordingGroupNames()[¶](#ApiClient.ParameterSet.GetAvailableRecordingGroupNames "Link to this definition")  
Returns the available names of the recording groups of the package.

Returns:  Recording group names

Return type:  list[str]

GetName()[¶](#ApiClient.ParameterSet.GetName "Link to this definition")  
Returns the name of the project component.

Returns:  Name of the component

Return type:  str

GetPackage()[¶](#ApiClient.ParameterSet.GetPackage "Link to this definition")  
Returns the referenced package.

Returns:  The referenced package of type [`Package`](PackageApi.md#ApiClient.Package "ApiClient.Package") or the referenced analysis package of type [`AnalysisPackage`](PackageApi.md#ApiClient.AnalysisPackage "ApiClient.AnalysisPackage")

Return type:  [`PackageBase`](TraceAnalysisApi.md#ApiClient.PackageBase "ApiClient.PackageBase")

GetParent()[¶](#ApiClient.ParameterSet.GetParent "Link to this definition")  
Returns the parent project component.

Returns:  Parent component

Return type:  [`ProjectComponent`](ComponentApi.md#ApiClient.ProjectComponent "ApiClient.ProjectComponent")

GetPosition()[¶](#ApiClient.ParameterSet.GetPosition "Link to this definition")  
Returns the position in the parent project.

Returns:  parent position

Return type:  integer

GetTestCaseId()[¶](#ApiClient.ParameterSet.GetTestCaseId "Link to this definition")  
Returns the test case id of the parameter record.

Returns:  Test case id

Return type:  str

GetTestScriptId()[¶](#ApiClient.ParameterSet.GetTestScriptId "Link to this definition")  
Returns the test script id of the corresponding package.

Returns:  Test script id

Return type:  str

GetType()[¶](#ApiClient.ParameterSet.GetType "Link to this definition")  
Returns the type (class name) of the project component, e.g.  
- “ConfigChange”

- “ParameterSet”

- “PackageCall”

- “Project”

- “PackageGenerator”

Returns:  Type (class name) of the project component

Return type:  str

IsEnabled()[¶](#ApiClient.ParameterSet.IsEnabled "Link to this definition")  
Returns the state of the test step.

Returns:  True if test step is enabled, otherwise False

Return type:  bool

RemoveFromProject()[¶](#ApiClient.ParameterSet.RemoveFromProject "Link to this definition")  
Removes this component from the project.

Raises:  
**ApiError** – if the component is not part of any project

SetEnabled(*state=True*)[¶](#ApiClient.ParameterSet.SetEnabled "Link to this definition")  
Enable or disable the test step.

Parameters:  **state** (*bool*) – True (=Default) to enable, False to disable the test step.

SetName(*name*)[¶](#ApiClient.ParameterSet.SetName "Link to this definition")  
Sets the name of the project component.

Parameters:  **name** (*str*) – Name of the component

SetTestCaseId(*testCaseId*)[¶](#ApiClient.ParameterSet.SetTestCaseId "Link to this definition")  
Sets the independent test case id of the parameter record.

Parameters:  **testCaseId** (*str*) – Test case id

Returns:  True if the update was successful

Return type:  boolean

## ParameterSetRecordings[¶](#parametersetrecordings "Link to this heading")

*class* ParameterSetRecordings[¶](#ApiClient.ParameterSetRecordings "Link to this definition")  
Returned by

- [`ParameterSet.Recordings`](#ApiClient.ParameterSet.Recordings "ApiClient.ParameterSet.Recordings")

AddRecordingInfos(*recordingGroupName*, *recordingInfos*)[¶](#ApiClient.ParameterSetRecordings.AddRecordingInfos "Link to this definition")  
Adds a recording info item to a specified recording group in the parameter set.

Parameters:  - **recordingGroupName** (*str*) – Name of the recording group to add the recording item

- **recordingInfos** (list[[`RecordingInfo`](SignalRecordingApi.md#ApiClient.RecordingInfo "ApiClient.RecordingInfo")]) – The recording items to be added

Clone()[¶](#ApiClient.ParameterSetRecordings.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`ParameterSetRecordings`](#ApiClient.ParameterSetRecordings "ApiClient.ParameterSetRecordings")

GetRecordingInfos(*recordingGroupName=None*)[¶](#ApiClient.ParameterSetRecordings.GetRecordingInfos "Link to this definition")  
Returns recording information of the parameter set. If a recording group name is given returns only those items of the group

Parameters:  **recordingGroupName** (*str*) – Name of the recording group to return the info items of

Returns:  recording info items

Return type:  list[[`RecordingInfo`](SignalRecordingApi.md#ApiClient.RecordingInfo "ApiClient.RecordingInfo")]

RemoveRecordingInfoByIndex(*groupName*, *infoIndex*)[¶](#ApiClient.ParameterSetRecordings.RemoveRecordingInfoByIndex "Link to this definition")  
Removes a recording info item from the parameter set by recording group name and recording info index.

Parameters:  - **groupName** (*str*) – Recording group name

- **infoIndex** (*integer*) – Index of the recording info item in the recording group to be removed

Raise:  
ApiError: - When there is no group matching the given name - When the recording info index is out of range
