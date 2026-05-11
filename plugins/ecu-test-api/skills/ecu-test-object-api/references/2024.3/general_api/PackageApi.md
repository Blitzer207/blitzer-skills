# API for Packages[¶](#api-for-packages "Link to this heading")

Part of the [Object based program API](objectApi.md#objectapi)

## PackageApi[¶](#packageapi "Link to this heading")

*class* PackageApi[¶](#ApiClient.PackageApi "Link to this definition")  
API to access Packages

Returned by

- [`ApiClient.PackageApi`](objectApi.md#ApiClient.ApiClient.PackageApi "ApiClient.ApiClient.PackageApi")

ExpectationApi[¶](#ApiClient.PackageApi.ExpectationApi "Link to this definition")  
Returns the ExpectationApi namespace.

Returns:  ExpectationApi namespace

Return type:  [`ExpectationApi`](ExpectationApi.md#ApiClient.ExpectationApi "ApiClient.ExpectationApi")

ExpressionApi[¶](#ApiClient.PackageApi.ExpressionApi "Link to this definition")  
Returns the ExpressionApi namespace.

Returns:  ExpressionApi namespace

Return type:  [`ExpressionApi`](ExpressionApi.md#ApiClient.ExpressionApi "ApiClient.ExpressionApi")

MappingApi[¶](#ApiClient.PackageApi.MappingApi "Link to this definition")  
Returns the MappingApi namespace.

Returns:  MappingApi namespace

Return type:  [`MappingApi`](MappingApi.md#ApiClient.MappingApi "ApiClient.MappingApi")

SignalRecordingApi[¶](#ApiClient.PackageApi.SignalRecordingApi "Link to this definition")  
Returns the SignalRecordingApi namespace.

Returns:  SignalRecordingApi namespace

Return type:  [`SignalRecordingApi`](SignalRecordingApi.md#ApiClient.SignalRecordingApi "ApiClient.SignalRecordingApi")

TestStepApi[¶](#ApiClient.PackageApi.TestStepApi "Link to this definition")  
Returns the TestStepApi namespace.

Returns:  TestStepApi namespace

Return type:  [`TestStepApi`](TestStepApi.md#ApiClient.TestStepApi "ApiClient.TestStepApi")

TraceAnalysisApi[¶](#ApiClient.PackageApi.TraceAnalysisApi "Link to this definition")  
Returns the TraceAnalysisApi namespace.

Returns:  TraceAnalysisApi namespace

Return type:  [`TraceAnalysisApi`](TraceAnalysisApi.md#ApiClient.TraceAnalysisApi "ApiClient.TraceAnalysisApi")

VariableApi[¶](#ApiClient.PackageApi.VariableApi "Link to this definition")  
Returns the VariableApi namespace.

Returns:  VariableApi namespace

Return type:  [`VariableApi`](VariableApi.md#ApiClient.VariableApi "ApiClient.VariableApi")

CreateAnalysisPackage()[¶](#ApiClient.PackageApi.CreateAnalysisPackage "Link to this definition")  
Creates a new analysis package.

Returns:  New empty analysis package

Return type:  [`AnalysisPackage`](#ApiClient.AnalysisPackage "ApiClient.AnalysisPackage")

CreatePackage()[¶](#ApiClient.PackageApi.CreatePackage "Link to this definition")  
Creates a new package.

Returns:  New empty package

Return type:  [`Package`](#ApiClient.Package "ApiClient.Package")

GetAnalysisPackageByTestManagementId(*testManagementId*)[¶](#ApiClient.PackageApi.GetAnalysisPackageByTestManagementId "Link to this definition")  
Returns an existing analysis package holding the given test management id or None, if no matching analysis package exists in the workspace. If found, the analysis package will be opened.

Parameters:  **testManagementId** (*str*) – The test management id identifying the analysis package

Returns:  the analysis package or None, if no matching item exists within the workspace

Return type:  [`AnalysisPackage`](#ApiClient.AnalysisPackage "ApiClient.AnalysisPackage")

GetAnalysisPackageChanges(*oldPackage*, *newPackage*)[¶](#ApiClient.PackageApi.GetAnalysisPackageChanges "Link to this definition")  
Get the changes that exist between two given analysis packages.

Parameters:  - **oldPackage** ([`AnalysisPackage`](#ApiClient.AnalysisPackage "ApiClient.AnalysisPackage")) – The old package to compare.

- **newPackage** ([`AnalysisPackage`](#ApiClient.AnalysisPackage "ApiClient.AnalysisPackage")) – The new package to compare.

Returns:  The changes that exist between the two analysis packages.

Return type:  list[[`Change`](ConfigurationApi.md#ApiClient.Change "ApiClient.Change")]

GetAnalysisPackagePathsByTestscriptId(*testscriptId*)[¶](#ApiClient.PackageApi.GetAnalysisPackagePathsByTestscriptId "Link to this definition")  
Returns paths of packages which holding the given test script id.

Parameters:  **testscriptId** (*str*) – The test management id identifying the package

Returns:  list of file paths

Return type:  list[str]

GetChanges(*oldPackage*, *newPackage*)[¶](#ApiClient.PackageApi.GetChanges "Link to this definition")  
Get the changes that exist between two given packages.

Parameters:  - **oldPackage** ([`Package`](#ApiClient.Package "ApiClient.Package")) – The old package to compare.

- **newPackage** ([`Package`](#ApiClient.Package "ApiClient.Package")) – The new package to compare.

Returns:  The changes that exist between the two packages.

Return type:  list[[`Change`](ConfigurationApi.md#ApiClient.Change "ApiClient.Change")]

GetPackageByTestManagementId(*testManagementId*)[¶](#ApiClient.PackageApi.GetPackageByTestManagementId "Link to this definition")  
Returns an existing package holding the given test management id or None, if no matching package exists in the workspace. If found, the package will be opened.

Parameters:  **testManagementId** (*str*) – The test management id identifying the package

Returns:  the package or None, if no matching package exists within the workspace

Return type:  [`Package`](#ApiClient.Package "ApiClient.Package")

GetPackagePathsByTestscriptId(*testscriptId*)[¶](#ApiClient.PackageApi.GetPackagePathsByTestscriptId "Link to this definition")  
Returns paths of packages which holding the given test script id.

Parameters:  **testscriptId** (*str*) – The test management id identifying the package

Returns:  list of file paths

Return type:  list[str]

GetTestManagementIdByPath(*filename*)[¶](#ApiClient.PackageApi.GetTestManagementIdByPath "Link to this definition")  
Returns the test script id for a given Package or Analysis Package filename. If the corresponding item has no id or if it does not exist, an empty string is returned.

Parameters:  **filename** (*str*) – Absolute path to the package or analysis package file or relative path in regard to the package directory

Returns:  The test script id of an empty string

Return type:  str

OpenAnalysisPackage(*filename*)[¶](#ApiClient.PackageApi.OpenAnalysisPackage "Link to this definition")  
Opens an existing analysis package. The analysis package may not be opened in ecu.test.

Parameters:  **filename** (*str*) – Absolute path to the analysis package file or relative path in regard to the package directory

Returns:  Existing package

Return type:  [`AnalysisPackage`](#ApiClient.AnalysisPackage "ApiClient.AnalysisPackage")

OpenPackage(*filename*)[¶](#ApiClient.PackageApi.OpenPackage "Link to this definition")  
Opens an existing package. The package may not be opened in ecu.test.

Parameters:  **filename** (*str*) – Absolute path to the package file or relative path in regard to the package directory

Returns:  Existing package

Return type:  [`Package`](#ApiClient.Package "ApiClient.Package")

SearchAnalysisPackages(*searchCriteria*, *useExtendedMode=False*)[¶](#ApiClient.PackageApi.SearchAnalysisPackages "Link to this definition")  
Searches the current workspace and library workspaces for analysis packages matching  
the given search criteria.

Parameters:  - **searchCriteria** (*str*) – The search criteria expressed in the ecu.test filter syntax. See section “Handling” =\> “Filter” of the ecu.test User Documentation.

- **useExtendedMode** (*boolean*) – If True, extended search strings are enabled. The default is False, meaning each word in the searchCriteria will be enclosed by wildcards and mapped to the filename. (e.g. “hello world” =\> “Name = ‘\*hello\*’ and Name = ‘\*world\*’”)

Returns:  All matching analysis packages. If no item matches, an empty list is returned.

Return type:  list[[`AnalysisPackage`](#ApiClient.AnalysisPackage "ApiClient.AnalysisPackage")]

Raises:  
**ApiError** – If the searchCriteria has an illegal syntax.

SearchPackages(*searchCriteria*, *useExtendedMode=False*)[¶](#ApiClient.PackageApi.SearchPackages "Link to this definition")  
Searches the current workspace and library workspaces for packages matching the given search criteria.

Parameters:  - **searchCriteria** (*str*) – The search criteria expressed in the ecu.test filter syntax. See section “Handling” =\> “Filter” of the ecu.test User Documentation.

- **useExtendedMode** (*boolean*) – If True, extended search strings are enabled. The default is False, meaning each word in the searchCriteria will be enclosed by wildcards and mapped to the filename. (e.g. “hello world” =\> “Name = ‘\*hello\*’ and Name = ‘\*world\*’”)

Returns:  All matching packages. If no package matches, an empty list is returned.

Return type:  list[[`Package`](#ApiClient.Package "ApiClient.Package")]

Raises:  
**ApiError** – If the searchCriteria has an illegal syntax.

## AnalysisPackage[¶](#analysispackage "Link to this heading")

*class* AnalysisPackage[¶](#ApiClient.AnalysisPackage "Link to this definition")  
Base class

[`PackageBase`](TraceAnalysisApi.md#ApiClient.PackageBase "ApiClient.PackageBase")

Returned by

- [`AnalysisPackageCall.GetPackage`](ComponentApi.md#ApiClient.AnalysisPackageCall.GetPackage "ApiClient.AnalysisPackageCall.GetPackage")

- [`AnalysisPackageMappingCall.GetPackage`](ComponentApi.md#ApiClient.AnalysisPackageMappingCall.GetPackage "ApiClient.AnalysisPackageMappingCall.GetPackage")

- [`PackageApi.CreateAnalysisPackage`](#ApiClient.PackageApi.CreateAnalysisPackage "ApiClient.PackageApi.CreateAnalysisPackage")

- [`PackageApi.GetAnalysisPackageByTestManagementId`](#ApiClient.PackageApi.GetAnalysisPackageByTestManagementId "ApiClient.PackageApi.GetAnalysisPackageByTestManagementId")

- [`PackageApi.OpenAnalysisPackage`](#ApiClient.PackageApi.OpenAnalysisPackage "ApiClient.PackageApi.OpenAnalysisPackage")

- [`PackageApi.SearchAnalysisPackages`](#ApiClient.PackageApi.SearchAnalysisPackages "ApiClient.PackageApi.SearchAnalysisPackages")

Attributes[¶](#ApiClient.AnalysisPackage.Attributes "Link to this definition")  
Returns access to the package attributes definitions specified within the parameter set and the referenced package attribute definition files.

Returns:  Package attribute interface of the parameter set

Return type:  [`Attributes`](ProjectApi.md#ApiClient.Attributes "ApiClient.Attributes")

AddRelation(*relation*)[¶](#ApiClient.AnalysisPackage.AddRelation "Link to this definition")  
Add relation :param relation: :type relation: [`Relation`](RelationApi.md#ApiClient.Relation "ApiClient.Relation")

AddVariable(*variable*)[¶](#ApiClient.AnalysisPackage.AddVariable "Link to this definition")  
Adds a variable to the package.

Parameters:  **variable** ([`Variable`](VariableApi.md#ApiClient.Variable "ApiClient.Variable")) – Variable to be added

Close()[¶](#ApiClient.AnalysisPackage.Close "Link to this definition")  
Closes the package. After closing the package it can not be modified/accessed anymore.

GetActivationCondition()[¶](#ApiClient.AnalysisPackage.GetActivationCondition "Link to this definition")  
Gets the activation condition for this package.

Returns:  The expression defining the activation condition

Return type:  str

GetDescription()[¶](#ApiClient.AnalysisPackage.GetDescription "Link to this definition")  
Returns the package description.

Returns:  Description shown in the package properties

Return type:  str

GetFilename()[¶](#ApiClient.AnalysisPackage.GetFilename "Link to this definition")  
Returns the file name of the package file as absolute path, if this is a file. If not it may be unsaved.

Returns:  The file name of the saved file or None, if not a file

Return type:  str

GetMapping()[¶](#ApiClient.AnalysisPackage.GetMapping "Link to this definition")  
Returns the local mapping of the analysis package.

Returns:  Mapping of the package

Return type:  [`LocalMapping`](#ApiClient.LocalMapping "ApiClient.LocalMapping")

GetName()[¶](#ApiClient.AnalysisPackage.GetName "Link to this definition")  
Returns the package name.

Returns:  Package name.

Return type:  str

GetParameterVariables()[¶](#ApiClient.AnalysisPackage.GetParameterVariables "Link to this definition")  
Returns a list of all variables defined in the analysis package and set as a parameter.

Returns:  List of all defined parameters

Return type:  list[[`Variable`](VariableApi.md#ApiClient.Variable "ApiClient.Variable")]

GetRelations()[¶](#ApiClient.AnalysisPackage.GetRelations "Link to this definition")  
Returns relations :return: relations :rtype: list[[`Relation`](RelationApi.md#ApiClient.Relation "ApiClient.Relation")]

GetReturnVariables()[¶](#ApiClient.AnalysisPackage.GetReturnVariables "Link to this definition")  
Returns a list of all variables defined in the package and set as a return variable.

Returns:  List of all defined return variables

Return type:  list[[`Variable`](VariableApi.md#ApiClient.Variable "ApiClient.Variable")]

GetTestScriptId()[¶](#ApiClient.AnalysisPackage.GetTestScriptId "Link to this definition")  
Returns the test script id of the package.

Returns:  Test script id.

Return type:  str

GetTraceAnalysis()[¶](#ApiClient.AnalysisPackage.GetTraceAnalysis "Link to this definition")  
Returns the trace analysis of the analysis package.

Returns:  The trace analysis of the analysis package

Return type:  [`TraceAnalysis`](TraceAnalysisApi.md#ApiClient.TraceAnalysis "ApiClient.TraceAnalysis")

GetType()[¶](#ApiClient.AnalysisPackage.GetType "Link to this definition")  
Returns the type (class name) of the package, e.g.  
- “Package”

- “AnalysisPackage”

Returns:  Type (class name) of the package

Return type:  str

GetUnusedVariables()[¶](#ApiClient.AnalysisPackage.GetUnusedVariables "Link to this definition")  
Returns the list of unused variables defined in the package.

Returns:  List of all unused defined variables

Return type:  list[[`Variable`](VariableApi.md#ApiClient.Variable "ApiClient.Variable")]

GetVariable(*name*)[¶](#ApiClient.AnalysisPackage.GetVariable "Link to this definition")  
Returns the variable defined in the package with a specific name.

Parameters:  **name** (*string*) – The name of the variable

Returns:  Variable with the specified name or None

Return type:  [`Variable`](VariableApi.md#ApiClient.Variable "ApiClient.Variable")

GetVariables()[¶](#ApiClient.AnalysisPackage.GetVariables "Link to this definition")  
Returns a list of all variables defined in the package.

Returns:  List of all defined variables

Return type:  list[[`Variable`](VariableApi.md#ApiClient.Variable "ApiClient.Variable")]

GetVersion()[¶](#ApiClient.AnalysisPackage.GetVersion "Link to this definition")  
Returns the package version.

Returns:  Version shown in the package properties

Return type:  str

HasSpecificationFlag()[¶](#ApiClient.AnalysisPackage.HasSpecificationFlag "Link to this definition")  
Returns the state of the specification flag.

Returns:  True if specification flag is enabled, otherwise False

Return type:  bool

HasTestCaseFlag()[¶](#ApiClient.AnalysisPackage.HasTestCaseFlag "Link to this definition")  
Returns the state of the test case flag.

Returns:  True if test case flag is enabled, otherwise False

Return type:  bool

IsActivationConditionFulfilled()[¶](#ApiClient.AnalysisPackage.IsActivationConditionFulfilled "Link to this definition")  
Evaluates the activation condition defined in the package.

Returns:  True, if the activation condition is fulfilled.

Return type:  bool

Raises:  
**ApiError** – If the activation condition is not evaluable

RemoveRelation(*relation*)[¶](#ApiClient.AnalysisPackage.RemoveRelation "Link to this definition")  
Remove relation :param relation: :type relation: [`Relation`](RelationApi.md#ApiClient.Relation "ApiClient.Relation")

RemoveVariable(*variableName*)[¶](#ApiClient.AnalysisPackage.RemoveVariable "Link to this definition")  
Removes a variable from the package.

Parameters:  **variableName** (*str*) – Name of variable to be removed

RenameVariable(*oldVarName*, *newVarName*)[¶](#ApiClient.AnalysisPackage.RenameVariable "Link to this definition")  
Renames a existing variable of the package.

Parameters:  - **oldVarName** (*str*) – The old variable name

- **newVarName** (*str*) – The new variable name

Save(*filename=None*)[¶](#ApiClient.AnalysisPackage.Save "Link to this definition")  
Saves the package. Appends file ending if needed.

Parameters:  **filename** (*str*) – File name of the package; Either absolute or relative to the ‘Packages’ directory. Leave out to save the package to its existing file (previously set with [`Save()`](#ApiClient.Package.Save "ApiClient.Package.Save") or from [`PackageApi.OpenPackage()`](#ApiClient.PackageApi.OpenPackage "ApiClient.PackageApi.OpenPackage"))

SetActivationCondition(*expression*)[¶](#ApiClient.AnalysisPackage.SetActivationCondition "Link to this definition")  
Sets the activation condition for this package.

Parameters:  **expression** (*str*) – The expression defining the activation condition

SetDescription(*description*)[¶](#ApiClient.AnalysisPackage.SetDescription "Link to this definition")  
Sets the package description.

Parameters:  **description** (*str*) – Description to be shown in the package properties

SetSpecificationFlag(*state=True*)[¶](#ApiClient.AnalysisPackage.SetSpecificationFlag "Link to this definition")  
Sets the specification flag.

Parameters:  **state** (*bool*) – True to enable, False to disable the specification flag

SetTestCaseFlag(*state=True*)[¶](#ApiClient.AnalysisPackage.SetTestCaseFlag "Link to this definition")  
Sets the test case flag.

Parameters:  **state** (*bool*) – True to enable, False to disable the test case flag

SetTestScriptId(*testSriptId*)[¶](#ApiClient.AnalysisPackage.SetTestScriptId "Link to this definition")  
Sets the test script id of the package.

Parameters:  **testSriptId** (*str*) – Test script id

SetTraceAnalysis(*traceAnalysis*)[¶](#ApiClient.AnalysisPackage.SetTraceAnalysis "Link to this definition")  
Sets the trace analysis of the analysis package.

Parameters:  **traceAnalysis** ([`TraceAnalysis`](TraceAnalysisApi.md#ApiClient.TraceAnalysis "ApiClient.TraceAnalysis")) – Trace analysis to be set

SetVersion(*version*)[¶](#ApiClient.AnalysisPackage.SetVersion "Link to this definition")  
Sets the package version.

Parameters:  **version** (*str*) – Version to be shown in the package properties

## LocalMapping[¶](#localmapping "Link to this heading")

*class* LocalMapping[¶](#ApiClient.LocalMapping "Link to this definition")  
Base class

[`Mapping`](MappingApi.md#ApiClient.Mapping "ApiClient.Mapping")

Returned by

- [`AnalysisPackage.GetMapping`](#ApiClient.AnalysisPackage.GetMapping "ApiClient.AnalysisPackage.GetMapping")

- [`Package.GetMapping`](#ApiClient.Package.GetMapping "ApiClient.Package.GetMapping")

- [`PackageBase.GetMapping`](TraceAnalysisApi.md#ApiClient.PackageBase.GetMapping "ApiClient.PackageBase.GetMapping")

AddItem(*mappingItem*)[¶](#ApiClient.LocalMapping.AddItem "Link to this definition")  
Adds a mapping item to the mapping.

Parameters:  **mappingItem** ([`MappingItem`](MappingApi.md#ApiClient.MappingItem "ApiClient.MappingItem")) – The mapping item to be added

Clone()[¶](#ApiClient.LocalMapping.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`LocalMapping`](#ApiClient.LocalMapping "ApiClient.LocalMapping")

GetItemByName(*name*)[¶](#ApiClient.LocalMapping.GetItemByName "Link to this definition")  
Searches the mapping for the mapping item by its name and returns it if existing.

Parameters:  **name** (*str*) – The name of the mapping item to be searched for

Returns:  mapping item with the given name or None if no such mapping item exists

Return type:  [`MappingItem`](MappingApi.md#ApiClient.MappingItem "ApiClient.MappingItem")

GetItems()[¶](#ApiClient.LocalMapping.GetItems "Link to this definition")  
Returns a list of all the mapping items of the mapping.

Returns:  List of all the mapping items of the mapping.

Return type:  list[[`MappingItem`](MappingApi.md#ApiClient.MappingItem "ApiClient.MappingItem")]

GetItemsByTargetPath(*targetPath*)[¶](#ApiClient.LocalMapping.GetItemsByTargetPath "Link to this definition")  
Searches the mapping for all mapping items that have the target path and returns them if existing.

Parameters:  **targetPath** (*str*) – The target path of the mapping items to be searched for

Returns:  List of mapping items that have the target path.

Return type:  list[[`MappingItem`](MappingApi.md#ApiClient.MappingItem "ApiClient.MappingItem")]

HasItem(*mappingItem*)[¶](#ApiClient.LocalMapping.HasItem "Link to this definition")  
Checks whether the given mapping item belongs to the mapping.

Parameters:  **mappingItem** ([`MappingItem`](MappingApi.md#ApiClient.MappingItem "ApiClient.MappingItem")) – The mapping item to be checked

Returns:  True if the given mapping item belongs to the mapping.

Return type:  boolean

RemoveItemByName(*name*)[¶](#ApiClient.LocalMapping.RemoveItemByName "Link to this definition")  
Removes a mapping item from the mapping.

Parameters:  **name** (*str*) – The name of the mapping item to be removed

ReplaceItem(*mappingItem*)[¶](#ApiClient.LocalMapping.ReplaceItem "Link to this definition")  
Replaces a mapping item from the mapping

Parameters:  **mappingItem** ([`MappingItem`](MappingApi.md#ApiClient.MappingItem "ApiClient.MappingItem")) – The new mapping item to replace an existing one of the same name

## VariableRecordingGroup[¶](#variablerecordinggroup "Link to this heading")

*class* VariableRecordingGroup[¶](#ApiClient.VariableRecordingGroup "Link to this definition")  
Base classes

- [`RecordingGroup`](SignalRecordingApi.md#ApiClient.RecordingGroup "ApiClient.RecordingGroup")

- [`RecordingGroupBase`](TraceAnalysisApi.md#ApiClient.RecordingGroupBase "ApiClient.RecordingGroupBase")

Returned by

- [`RecordingConfig.GetVariableRecordingGroup`](#ApiClient.RecordingConfig.GetVariableRecordingGroup "ApiClient.RecordingConfig.GetVariableRecordingGroup")

RECORDING_MODE_AUTO[¶](#ApiClient.VariableRecordingGroup.RECORDING_MODE_AUTO "Link to this definition")  
Returns the constant used to specify the recording mode ‘Auto-Start/Stop: complete test case’.

Returns:  The constant

Return type:  int

RECORDING_MODE_AUTO_RESTRICTED[¶](#ApiClient.VariableRecordingGroup.RECORDING_MODE_AUTO_RESTRICTED "Link to this definition")  
Returns the constant used to specify the recording mode ‘Auto-Start/Stop: without Pre-/Postcondition’.

Returns:  The constant

Return type:  int

RECORDING_MODE_MANUAL[¶](#ApiClient.VariableRecordingGroup.RECORDING_MODE_MANUAL "Link to this definition")  
Returns the constant used to specify the recording mode ‘Manually’.

Returns:  The constant

Return type:  int

RECORDING_MODE_TRIGGER[¶](#ApiClient.VariableRecordingGroup.RECORDING_MODE_TRIGGER "Link to this definition")  
Returns the constant used to specify the recording mode ‘Trigger-Start/Stop’.

Returns:  The constant

Return type:  int

AppendRecordingInfo(*recordingInfo*)[¶](#ApiClient.VariableRecordingGroup.AppendRecordingInfo "Link to this definition")  
Adds a recording info to the recording group.

Parameters:  **recordingInfo** ([`RecordingInfo`](SignalRecordingApi.md#ApiClient.RecordingInfo "ApiClient.RecordingInfo")) – The recording info to be added

Clone()[¶](#ApiClient.VariableRecordingGroup.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`VariableRecordingGroup`](#ApiClient.VariableRecordingGroup "ApiClient.VariableRecordingGroup")

GetConditionalSignalNamesForTraceAnalyses()[¶](#ApiClient.VariableRecordingGroup.GetConditionalSignalNamesForTraceAnalyses "Link to this definition")  
Returns the list of signal names that can be optional or mandatory for running the trace analyses depending on the values of global constants.

Returns:  The list of undetermined signal names.

Return type:  list[str]

GetFilenameTemplate()[¶](#ApiClient.VariableRecordingGroup.GetFilenameTemplate "Link to this definition")  
Returns the file name template of the recording group.

Returns:  The file name template of the recording group.

Return type:  str

GetMandatorySignalNamesForTraceAnalyses()[¶](#ApiClient.VariableRecordingGroup.GetMandatorySignalNamesForTraceAnalyses "Link to this definition")  
Returns the list of signal names that are mandatory for running the trace analyses.

Returns:  The list of mandatory signal names.

Return type:  list[str]

GetName()[¶](#ApiClient.VariableRecordingGroup.GetName "Link to this definition")  
Returns the name of a recording group.

Returns:  the name

Return type:  str

GetOptionalSignalNamesForTraceAnalyses()[¶](#ApiClient.VariableRecordingGroup.GetOptionalSignalNamesForTraceAnalyses "Link to this definition")  
Returns the list of signal names that are optional for running the trace analyses.

Returns:  The list of optional signal names.

Return type:  list[str]

GetRecordingInfos()[¶](#ApiClient.VariableRecordingGroup.GetRecordingInfos "Link to this definition")  
Returns the recording infos of the recording group.

Returns:  Recording infos

Return type:  list[[`RecordingInfo`](SignalRecordingApi.md#ApiClient.RecordingInfo "ApiClient.RecordingInfo")]

GetRecordingMode()[¶](#ApiClient.VariableRecordingGroup.GetRecordingMode "Link to this definition")  
Returns the recording mode of the recording group as one of the following constants:

> - [`RecordingGroup.RECORDING_MODE_MANUAL`](SignalRecordingApi.md#ApiClient.RecordingGroup.RECORDING_MODE_MANUAL "ApiClient.RecordingGroup.RECORDING_MODE_MANUAL")
>
> - [`RecordingGroup.RECORDING_MODE_AUTO_RESTRICTED`](SignalRecordingApi.md#ApiClient.RecordingGroup.RECORDING_MODE_AUTO_RESTRICTED "ApiClient.RecordingGroup.RECORDING_MODE_AUTO_RESTRICTED")
>
> - [`RecordingGroup.RECORDING_MODE_AUTO`](SignalRecordingApi.md#ApiClient.RecordingGroup.RECORDING_MODE_AUTO "ApiClient.RecordingGroup.RECORDING_MODE_AUTO")
>
> - [`RecordingGroup.RECORDING_MODE_TRIGGER`](SignalRecordingApi.md#ApiClient.RecordingGroup.RECORDING_MODE_TRIGGER "ApiClient.RecordingGroup.RECORDING_MODE_TRIGGER")

Returns:  The recording mode constant

Return type:  int

RemoveRecordingInfo(*recordingInfo*)[¶](#ApiClient.VariableRecordingGroup.RemoveRecordingInfo "Link to this definition")  
Removes a recording info from the recording group.

Parameters:  **recordingInfo** ([`RecordingInfo`](SignalRecordingApi.md#ApiClient.RecordingInfo "ApiClient.RecordingInfo")) – The recording info to be removed

Raises:  
ApiError: When recording info is not part of recording group

SetRecordingMode(*value*)[¶](#ApiClient.VariableRecordingGroup.SetRecordingMode "Link to this definition")  
Sets the recording mode of the recording group to one of the following constants:

> - [`RecordingGroup.RECORDING_MODE_MANUAL`](SignalRecordingApi.md#ApiClient.RecordingGroup.RECORDING_MODE_MANUAL "ApiClient.RecordingGroup.RECORDING_MODE_MANUAL")
>
> - [`RecordingGroup.RECORDING_MODE_AUTO_RESTRICTED`](SignalRecordingApi.md#ApiClient.RecordingGroup.RECORDING_MODE_AUTO_RESTRICTED "ApiClient.RecordingGroup.RECORDING_MODE_AUTO_RESTRICTED")
>
> - [`RecordingGroup.RECORDING_MODE_AUTO`](SignalRecordingApi.md#ApiClient.RecordingGroup.RECORDING_MODE_AUTO "ApiClient.RecordingGroup.RECORDING_MODE_AUTO")
>
> - [`RecordingGroup.RECORDING_MODE_TRIGGER`](SignalRecordingApi.md#ApiClient.RecordingGroup.RECORDING_MODE_TRIGGER "ApiClient.RecordingGroup.RECORDING_MODE_TRIGGER")

Parameters:  **value** (*int*) – The recording mode constant

EnableAutoStartStop(*enable=True*)[¶](#ApiClient.VariableRecordingGroup.EnableAutoStartStop "Link to this definition")  
Enables or disables automatic recording of this recording group during test execution.

Parameters:  **enable** (*bool*) – True to enable automatic recording, False to disable it

Deprecated since version 2020.1: Please use [`SetRecordingMode()`](#ApiClient.VariableRecordingGroup.SetRecordingMode "ApiClient.VariableRecordingGroup.SetRecordingMode") instead.

GetDescription()[¶](#ApiClient.VariableRecordingGroup.GetDescription "Link to this definition")  
Returns the description of the recording group.

Returns:  The description of the recording group.

Return type:  str

Deprecated since version 2020.1: The description of the recording group is not visible in the GUI. Please use the description of the signal group instead.

IsAutoStartStopEnabled()[¶](#ApiClient.VariableRecordingGroup.IsAutoStartStopEnabled "Link to this definition")  
Returns whether the recording group is configured to be recorded automatically during test execution.

Returns:  True if automatic recording is enabled, else False

Return type:  bool

Deprecated since version 2020.1: Please use [`GetRecordingMode()`](#ApiClient.VariableRecordingGroup.GetRecordingMode "ApiClient.VariableRecordingGroup.GetRecordingMode") instead.

IsLogRecording()[¶](#ApiClient.VariableRecordingGroup.IsLogRecording "Link to this definition")  
Returns whether the recording group is a log recording.

Returns:  True if the recording group is a log recording else False

Return type:  bool

Deprecated since version 2022.1: LogRecording was removed. All recording groups are SignalRecordings.

IsSignalRecording()[¶](#ApiClient.VariableRecordingGroup.IsSignalRecording "Link to this definition")  
Returns whether the recording group is a signal recording.

Returns:  True if the recording group is a signal recording else False

Return type:  bool

Deprecated since version 2022.1: LogRecording was removed. All recording groups are SignalRecordings.

IsTriggerStartStopEnabled()[¶](#ApiClient.VariableRecordingGroup.IsTriggerStartStopEnabled "Link to this definition")  
Returns if the recording group is configured to be start and stopped by a trigger.

Returns:  True if triggered start and stop is enabled, else False

Return type:  bool

Deprecated since version 2020.1: Please use [`GetRecordingMode()`](#ApiClient.VariableRecordingGroup.GetRecordingMode "ApiClient.VariableRecordingGroup.GetRecordingMode") instead.

SetDescription(*description*)[¶](#ApiClient.VariableRecordingGroup.SetDescription "Link to this definition")  
Sets the description of the recording group.

Parameters:  **description** (*str*) – The new description of the recording group.

Deprecated since version 2020.1: The description of the recording group is not visible in the GUI. Please use the description of the signal group instead.

## AutoAssignSignalGroup[¶](#autoassignsignalgroup "Link to this heading")

*class* AutoAssignSignalGroup[¶](#ApiClient.AutoAssignSignalGroup "Link to this definition")  
API to access the auto assign signal group. Signals of a signal group are represented by references to mapping items. This signal group is available per default. Signals added to this group will be automatically assigned to matching existing signal groups during package execution.

Base class

[`SignalGroupBase`](SignalRecordingApi.md#ApiClient.SignalGroupBase "ApiClient.SignalGroupBase")

Returned by

- [`RecordingConfig.GetAutoAssignSignalGroup`](#ApiClient.RecordingConfig.GetAutoAssignSignalGroup "ApiClient.RecordingConfig.GetAutoAssignSignalGroup")

AppendMappingItem(*mappingItem*)[¶](#ApiClient.AutoAssignSignalGroup.AppendMappingItem "Link to this definition")  
Adds a mapping item to the signal group.

Parameters:  **mappingItem** ([`MappingItem`](MappingApi.md#ApiClient.MappingItem "ApiClient.MappingItem")) – The mapping item to be added

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

Return type:  list[[`MappingItem`](MappingApi.md#ApiClient.MappingItem "ApiClient.MappingItem")]

GetName()[¶](#ApiClient.AutoAssignSignalGroup.GetName "Link to this definition")  
Returns the name of the signal group.

Returns:  The name

Return type:  str

GetRecordingGroup()[¶](#ApiClient.AutoAssignSignalGroup.GetRecordingGroup "Link to this definition")  
Returns the recording group of the auto assign signal group. This group is needed to bind signals to trace analyzes.

Returns:  The auto assign recording group

Return type:  [`AutoAssignRecordingGroup`](#ApiClient.AutoAssignRecordingGroup "ApiClient.AutoAssignRecordingGroup")

RemoveMappingItem(*mappingItemName*)[¶](#ApiClient.AutoAssignSignalGroup.RemoveMappingItem "Link to this definition")  
Removes a mapping item from the signal group.

Parameters:  **mappingItemName** (*str*) – The mapping item name

SetDescription(*description*)[¶](#ApiClient.AutoAssignSignalGroup.SetDescription "Link to this definition")  
Sets the description of the signal group.

Parameters:  **description** (*str*) – The new description of the signal group.

## AutoAssignRecordingGroup[¶](#autoassignrecordinggroup "Link to this heading")

*class* AutoAssignRecordingGroup[¶](#ApiClient.AutoAssignRecordingGroup "Link to this definition")  
Base class

[`RecordingGroupBase`](TraceAnalysisApi.md#ApiClient.RecordingGroupBase "ApiClient.RecordingGroupBase")

Returned by

- [`AutoAssignSignalGroup.GetRecordingGroup`](#ApiClient.AutoAssignSignalGroup.GetRecordingGroup "ApiClient.AutoAssignSignalGroup.GetRecordingGroup")

GetConditionalSignalNamesForTraceAnalyses()[¶](#ApiClient.AutoAssignRecordingGroup.GetConditionalSignalNamesForTraceAnalyses "Link to this definition")  
Returns the list of signal names that can be optional or mandatory for running the trace analyses depending on the values of global constants.

Returns:  The list of undetermined signal names.

Return type:  list[str]

GetMandatorySignalNamesForTraceAnalyses()[¶](#ApiClient.AutoAssignRecordingGroup.GetMandatorySignalNamesForTraceAnalyses "Link to this definition")  
Returns the list of signal names that are mandatory for running the trace analyses.

Returns:  The list of mandatory signal names.

Return type:  list[str]

GetName()[¶](#ApiClient.AutoAssignRecordingGroup.GetName "Link to this definition")  
Returns the name of a recording group.

Returns:  the name

Return type:  str

GetOptionalSignalNamesForTraceAnalyses()[¶](#ApiClient.AutoAssignRecordingGroup.GetOptionalSignalNamesForTraceAnalyses "Link to this definition")  
Returns the list of signal names that are optional for running the trace analyses.

Returns:  The list of optional signal names.

Return type:  list[str]

GetSignalGroup()[¶](#ApiClient.AutoAssignRecordingGroup.GetSignalGroup "Link to this definition")  
Returns the parent signal group.

Returns:  The parent signal group

Return type:  [`SignalGroupBase`](SignalRecordingApi.md#ApiClient.SignalGroupBase "ApiClient.SignalGroupBase")

GetDescription()[¶](#ApiClient.AutoAssignRecordingGroup.GetDescription "Link to this definition")  
Returns the description of the recording group.

Returns:  The description of the recording group.

Return type:  str

Deprecated since version 2020.1: The description of the recording group is not visible in the GUI. Please use the description of the signal group instead.

IsLogRecording()[¶](#ApiClient.AutoAssignRecordingGroup.IsLogRecording "Link to this definition")  
Returns whether the recording group is a log recording.

Returns:  True if the recording group is a log recording else False

Return type:  bool

Deprecated since version 2022.1: LogRecording was removed. All recording groups are SignalRecordings.

IsSignalRecording()[¶](#ApiClient.AutoAssignRecordingGroup.IsSignalRecording "Link to this definition")  
Returns whether the recording group is a signal recording.

Returns:  True if the recording group is a signal recording else False

Return type:  bool

Deprecated since version 2022.1: LogRecording was removed. All recording groups are SignalRecordings.

SetDescription(*description*)[¶](#ApiClient.AutoAssignRecordingGroup.SetDescription "Link to this definition")  
Sets the description of the recording group.

Parameters:  **description** (*str*) – The new description of the recording group.

Deprecated since version 2020.1: The description of the recording group is not visible in the GUI. Please use the description of the signal group instead.

## Package[¶](#package "Link to this heading")

*class* Package[¶](#ApiClient.Package "Link to this definition")  
Base class

[`PackageBase`](TraceAnalysisApi.md#ApiClient.PackageBase "ApiClient.PackageBase")

Returned by

- [`PackageApi.CreatePackage`](#ApiClient.PackageApi.CreatePackage "ApiClient.PackageApi.CreatePackage")

- [`PackageApi.GetPackageByTestManagementId`](#ApiClient.PackageApi.GetPackageByTestManagementId "ApiClient.PackageApi.GetPackageByTestManagementId")

- [`PackageApi.OpenPackage`](#ApiClient.PackageApi.OpenPackage "ApiClient.PackageApi.OpenPackage")

- [`PackageApi.SearchPackages`](#ApiClient.PackageApi.SearchPackages "ApiClient.PackageApi.SearchPackages")

- [`PackageCall.GetPackage`](ComponentApi.md#ApiClient.PackageCall.GetPackage "ApiClient.PackageCall.GetPackage")

- [`StimulationPackageCall.GetPackage`](ComponentApi.md#ApiClient.StimulationPackageCall.GetPackage "ApiClient.StimulationPackageCall.GetPackage")

- [`TsPackage.GetReferencedPackage`](TestStepApi.md#ApiClient.TsPackage.GetReferencedPackage "ApiClient.TsPackage.GetReferencedPackage")

- [`TsPackageCall.GetReferencedPackage`](TestStepApi.md#ApiClient.TsPackageCall.GetReferencedPackage "ApiClient.TsPackageCall.GetReferencedPackage")

- [`TsParallelPackage.GetReferencedPackage`](TestStepApi.md#ApiClient.TsParallelPackage.GetReferencedPackage "ApiClient.TsParallelPackage.GetReferencedPackage")

- [`TsParallelPackageCall.GetReferencedPackage`](TestStepApi.md#ApiClient.TsParallelPackageCall.GetReferencedPackage "ApiClient.TsParallelPackageCall.GetReferencedPackage")

- [`TsParallelRttPackage.GetReferencedPackage`](TestStepApi.md#ApiClient.TsParallelRttPackage.GetReferencedPackage "ApiClient.TsParallelRttPackage.GetReferencedPackage")

- [`TsParallelRttPackageCall.GetReferencedPackage`](TestStepApi.md#ApiClient.TsParallelRttPackageCall.GetReferencedPackage "ApiClient.TsParallelRttPackageCall.GetReferencedPackage")

- [`TsRttPackage.GetReferencedPackage`](TestStepApi.md#ApiClient.TsRttPackage.GetReferencedPackage "ApiClient.TsRttPackage.GetReferencedPackage")

- [`TsRttPackageCall.GetReferencedPackage`](TestStepApi.md#ApiClient.TsRttPackageCall.GetReferencedPackage "ApiClient.TsRttPackageCall.GetReferencedPackage")

Attributes[¶](#ApiClient.Package.Attributes "Link to this definition")  
Returns access to the package attributes definitions specified within the parameter set and the referenced package attribute definition files.

Returns:  Package attribute interface of the parameter set

Return type:  [`Attributes`](ProjectApi.md#ApiClient.Attributes "ApiClient.Attributes")

AddRelation(*relation*)[¶](#ApiClient.Package.AddRelation "Link to this definition")  
Add relation :param relation: :type relation: [`Relation`](RelationApi.md#ApiClient.Relation "ApiClient.Relation")

AddVariable(*variable*)[¶](#ApiClient.Package.AddVariable "Link to this definition")  
Adds a variable to the package.

Parameters:  **variable** ([`Variable`](VariableApi.md#ApiClient.Variable "ApiClient.Variable")) – Variable to be added

AppendTestStep(*testStep*)[¶](#ApiClient.Package.AppendTestStep "Link to this definition")  
Adds a test step at the end of the test case.

Parameters:  **testStep** ([`TestStep`](TestStepApi.md#ApiClient.TestStep "ApiClient.TestStep")) – Test step to be added

AppendTraceAnalysis(*traceAnalysis*)[¶](#ApiClient.Package.AppendTraceAnalysis "Link to this definition")  
Adds a trace analysis to the trace analyses list.

Parameters:  **traceAnalysis** ([`TraceAnalysis`](TraceAnalysisApi.md#ApiClient.TraceAnalysis "ApiClient.TraceAnalysis")) – Trace analysis to be added

Close()[¶](#ApiClient.Package.Close "Link to this definition")  
Closes the package. After closing the package it can not be modified/accessed anymore.

GetActivationCondition()[¶](#ApiClient.Package.GetActivationCondition "Link to this definition")  
Gets the activation condition for this package.

Returns:  The expression defining the activation condition

Return type:  str

GetAlternativeCallRepresentationAction()[¶](#ApiClient.Package.GetAlternativeCallRepresentationAction "Link to this definition")  
Returns the alternative representation of the action column when the package is called in another package.

Returns:  The alternative representation of the action column.

Return type:  str

GetAlternativeCallRepresentationExpectation()[¶](#ApiClient.Package.GetAlternativeCallRepresentationExpectation "Link to this definition")  
Returns the alternative representation of the expectation column when the package is called in another package.

Returns:  The alternative representation of the expectation.

Return type:  str

GetDescription()[¶](#ApiClient.Package.GetDescription "Link to this definition")  
Returns the package description.

Returns:  Description shown in the package properties

Return type:  str

GetFilename()[¶](#ApiClient.Package.GetFilename "Link to this definition")  
Returns the file name of the package file as absolute path, if this is a file. If not it may be unsaved.

Returns:  The file name of the saved file or None, if not a file

Return type:  str

GetImplementedKeywordInterfaceId()[¶](#ApiClient.Package.GetImplementedKeywordInterfaceId "Link to this definition")  
Returns the ID of the implemented keyword interface, if set and the package is marked as keyword implementation.

Returns:  Implemented keyword interface ID. If not yet set, an empty string will be returned.

Return type:  str

Raises:  
**ApiError** – If the “keyword implementation” flag is not set.

GetKeywordImplementationLanguage()[¶](#ApiClient.Package.GetKeywordImplementationLanguage "Link to this definition")  
Returns the implementation language (“de_DE” or “en_US”) of the current package, if it is marked as keyword implementation.

Returns:  The implementation language of this package, if explicitly set. “None” will be returned otherwise.

Return type:  str

Raises:  
**ApiError** – If the “keyword implementation” flag is not set.

GetMapping()[¶](#ApiClient.Package.GetMapping "Link to this definition")  
Returns the local mapping of the package.

Returns:  Mapping of the package

Return type:  [`LocalMapping`](#ApiClient.LocalMapping "ApiClient.LocalMapping")

GetName()[¶](#ApiClient.Package.GetName "Link to this definition")  
Returns the package name.

Returns:  Package name.

Return type:  str

GetParameterVariables()[¶](#ApiClient.Package.GetParameterVariables "Link to this definition")  
Returns a list of all variables defined in the analysis package and set as a parameter.

Returns:  List of all defined parameters

Return type:  list[[`Variable`](VariableApi.md#ApiClient.Variable "ApiClient.Variable")]

GetPostconditionBlock()[¶](#ApiClient.Package.GetPostconditionBlock "Link to this definition")  
Returns the postcondition block.

Returns:  Postcondition block or None, if none existing

Return type:  [`TsPostconditionBlock`](TestStepApi.md#ApiClient.TsPostconditionBlock "ApiClient.TsPostconditionBlock")

GetPreconditionBlock()[¶](#ApiClient.Package.GetPreconditionBlock "Link to this definition")  
Returns the precondition block.

Returns:  Precondition block or None, if none existing

Return type:  [`TsPreconditionBlock`](TestStepApi.md#ApiClient.TsPreconditionBlock "ApiClient.TsPreconditionBlock")

GetRecordedVariables()[¶](#ApiClient.Package.GetRecordedVariables "Link to this definition")  
Returns a list of all variables defined in the package and set as a recorded variable.

Returns:  List of all recorded variables

Return type:  list[[`Variable`](VariableApi.md#ApiClient.Variable "ApiClient.Variable")]

GetRecordingConfig()[¶](#ApiClient.Package.GetRecordingConfig "Link to this definition")  
Returns the recording configuration to configure signal groups, recording groups, signals to record, synchronizations and other settings.

Returns:  The recording configuration

Return type:  [`RecordingConfig`](#ApiClient.RecordingConfig "ApiClient.RecordingConfig")

GetRelations()[¶](#ApiClient.Package.GetRelations "Link to this definition")  
Returns relations :return: relations :rtype: list[[`Relation`](RelationApi.md#ApiClient.Relation "ApiClient.Relation")]

GetReturnVariables()[¶](#ApiClient.Package.GetReturnVariables "Link to this definition")  
Returns a list of all variables defined in the package and set as a return variable.

Returns:  List of all defined return variables

Return type:  list[[`Variable`](VariableApi.md#ApiClient.Variable "ApiClient.Variable")]

GetTestScriptId()[¶](#ApiClient.Package.GetTestScriptId "Link to this definition")  
Returns the test script id of the package.

Returns:  Test script id.

Return type:  str

GetTestStepByLineNo(*lineNo*)[¶](#ApiClient.Package.GetTestStepByLineNo "Link to this definition")  
Searches for the line number and returns the test step, if existing.

Parameters:  **lineNo** (*integer*) – Line number of the test step to be retrieved

Returns:  Test step at the current line number or None if no test step exists

Return type:  [`TestStep`](TestStepApi.md#ApiClient.TestStep "ApiClient.TestStep")

GetTestSteps(*skipDisabledSteps=True*, *recursive=False*, *whiteList=None*, *blackList=None*)[¶](#ApiClient.Package.GetTestSteps "Link to this definition")  
Returns the children of the test step.

Parameters:  - **skipDisabledSteps** (*boolean*) – Defines whether disabled test steps should be excluded.

- **recursive** (*boolean*) – Specifies whether only the direct children of the test step or recursively all test steps from the complete test step tree should be returned.

- **whiteList** (*list[str]*) – If specified, only those test steps whose class name is on this list are returned.

- **blackList** (*list[str]*) – If specified, only those test steps whose class name is not on this list are returned.

Returns:  List with all children test steps

Return type:  list[[`TestStep`](TestStepApi.md#ApiClient.TestStep "ApiClient.TestStep")]

GetTraceAnalyses()[¶](#ApiClient.Package.GetTraceAnalyses "Link to this definition")  
Returns all trace analyses of the package.

Returns:  The trace analyses of the package

Return type:  list[[`TraceAnalysis`](TraceAnalysisApi.md#ApiClient.TraceAnalysis "ApiClient.TraceAnalysis")]

GetType()[¶](#ApiClient.Package.GetType "Link to this definition")  
Returns the type (class name) of the package, e.g.  
- “Package”

- “AnalysisPackage”

Returns:  Type (class name) of the package

Return type:  str

GetUnusedVariables()[¶](#ApiClient.Package.GetUnusedVariables "Link to this definition")  
Returns the list of unused variables defined in the package.

Returns:  List of all unused defined variables

Return type:  list[[`Variable`](VariableApi.md#ApiClient.Variable "ApiClient.Variable")]

GetVariable(*name*)[¶](#ApiClient.Package.GetVariable "Link to this definition")  
Returns the variable defined in the package with a specific name.

Parameters:  **name** (*string*) – The name of the variable

Returns:  Variable with the specified name or None

Return type:  [`Variable`](VariableApi.md#ApiClient.Variable "ApiClient.Variable")

GetVariables()[¶](#ApiClient.Package.GetVariables "Link to this definition")  
Returns a list of all variables defined in the package.

Returns:  List of all defined variables

Return type:  list[[`Variable`](VariableApi.md#ApiClient.Variable "ApiClient.Variable")]

GetVersion()[¶](#ApiClient.Package.GetVersion "Link to this definition")  
Returns the package version.

Returns:  Version shown in the package properties

Return type:  str

HasSegmentationPackageFlag()[¶](#ApiClient.Package.HasSegmentationPackageFlag "Link to this definition")  
Returns the state of the segmentation package flag.

Returns:  True if the segmenation package flag is enabled, otherwise False.

Return type:  bool

HasSpecificationFlag()[¶](#ApiClient.Package.HasSpecificationFlag "Link to this definition")  
Returns the state of the specification flag.

Returns:  True if specification flag is enabled, otherwise False

Return type:  bool

HasStimulationPackageFlag()[¶](#ApiClient.Package.HasStimulationPackageFlag "Link to this definition")  
Returns the state of the stimulation package flag.

Returns:  True if stimulation package flag is enabled, otherwise False

Return type:  bool

HasTestCaseFlag()[¶](#ApiClient.Package.HasTestCaseFlag "Link to this definition")  
Returns the state of the test case flag.

Returns:  True if test case flag is enabled, otherwise False

Return type:  bool

HasTraceAnalyses()[¶](#ApiClient.Package.HasTraceAnalyses "Link to this definition")  
Returns True if the package has trace analyses.

Returns:  True if the package has trace analyses

Return type:  boolean

ImplementsKeyword()[¶](#ApiClient.Package.ImplementsKeyword "Link to this definition")  
Checks if current package is marked as a keyword interface implementation.

Returns:  “True”, if package is marked as a keyword interface implementation else “False”.

Return type:  boolean

InsertTestStep(*testStep*, *position*)[¶](#ApiClient.Package.InsertTestStep "Link to this definition")  
Adds a test step at a certain line of the test case.

Parameters:  - **testStep** ([`TestStep`](TestStepApi.md#ApiClient.TestStep "ApiClient.TestStep")) – Test step to be added

- **position** (*integer*) – Target index of child beginning with 0

IsActivationConditionFulfilled()[¶](#ApiClient.Package.IsActivationConditionFulfilled "Link to this definition")  
Evaluates the activation condition defined in the package.

Returns:  True, if the activation condition is fulfilled.

Return type:  bool

Raises:  
**ApiError** – If the activation condition is not evaluable

RemoveRelation(*relation*)[¶](#ApiClient.Package.RemoveRelation "Link to this definition")  
Remove relation :param relation: :type relation: [`Relation`](RelationApi.md#ApiClient.Relation "ApiClient.Relation")

RemoveTestStep(*testStep*)[¶](#ApiClient.Package.RemoveTestStep "Link to this definition")  
Removes the given test step from the test case.

Parameters:  **testStep** ([`TestStep`](TestStepApi.md#ApiClient.TestStep "ApiClient.TestStep")) – Test step to be removed

RemoveTraceAnalysis(*traceAnalysisName*)[¶](#ApiClient.Package.RemoveTraceAnalysis "Link to this definition")  
Removes a trace analysis from the trace analyses list.

Parameters:  **traceAnalysisName** (*str*) – Name of trace analysis to be removed

RemoveVariable(*variableName*)[¶](#ApiClient.Package.RemoveVariable "Link to this definition")  
Removes a variable from the package.

Parameters:  **variableName** (*str*) – Name of variable to be removed

RenameVariable(*oldVarName*, *newVarName*)[¶](#ApiClient.Package.RenameVariable "Link to this definition")  
Renames a existing variable of the package.

Parameters:  - **oldVarName** (*str*) – The old variable name

- **newVarName** (*str*) – The new variable name

Save(*filename=None*)[¶](#ApiClient.Package.Save "Link to this definition")  
Saves the package. Appends file ending if needed.

Parameters:  **filename** (*str*) – File name of the package; Either absolute or relative to the ‘Packages’ directory. Leave out to save the package to its existing file (previously set with [`Save()`](#ApiClient.Package.Save "ApiClient.Package.Save") or from [`PackageApi.OpenPackage()`](#ApiClient.PackageApi.OpenPackage "ApiClient.PackageApi.OpenPackage"))

SetActivationCondition(*expression*)[¶](#ApiClient.Package.SetActivationCondition "Link to this definition")  
Sets the activation condition for this package.

Parameters:  **expression** (*str*) – The expression defining the activation condition

SetAlternativeCallRepresentationAction(*action*)[¶](#ApiClient.Package.SetAlternativeCallRepresentationAction "Link to this definition")  
Sets the alternative representation of the action column when the package is called in another package.

Parameters:  **action** (*str*) – The alternative representation for the action.

SetAlternativeCallRepresentationExpectation(*expectation*)[¶](#ApiClient.Package.SetAlternativeCallRepresentationExpectation "Link to this definition")  
Sets the alternative representation of the expectation column when the package is called in another package.

Parameters:  **expectation** (*str*) – The alternative representation for the expectation.

SetDescription(*description*)[¶](#ApiClient.Package.SetDescription "Link to this definition")  
Sets the package description.

Parameters:  **description** (*str*) – Description to be shown in the package properties

SetImplementedKeywordInterfaceId(*implId*)[¶](#ApiClient.Package.SetImplementedKeywordInterfaceId "Link to this definition")  
Sets the ID of the implemented keyword interface, package must be marked as a keyword implementation before.

Parameters:  **implId** (*str*) – ID of the implemented keyword interfaces or empty.

Raises:  
**ApiError** – If the “keyword implementation” flag is not set.

SetImplementsKeywordFlag(*state*)[¶](#ApiClient.Package.SetImplementsKeywordFlag "Link to this definition")  
Sets the state of the “keyword implementation” flag.

Parameters:  **state** (*boolean*) – If “state” is “True”, this package will be marked as a keyword interface implementation, otherwise an eventually existing mark will be removed.

SetKeywordImplementationLanguage(*implLanguage*)[¶](#ApiClient.Package.SetKeywordImplementationLanguage "Link to this definition")  
Sets the implementation language of the current package. Package must be marked as a keyword implementation before.

Parameters:  **implLanguage** (*str*) – Implementation language “de_DE” or “en_US”. Or “None” to reset the current setting to program language.

Raises:  
**ApiError** – If the “keyword implementation” flag is not set.

SetSegmentationPackageFlag(*state=True*)[¶](#ApiClient.Package.SetSegmentationPackageFlag "Link to this definition")  
Sets the segmentation package flag.

Parameters:  **state** (*bool*) – True to enable, False to disable the segmentation package flag.

SetSpecificationFlag(*state=True*)[¶](#ApiClient.Package.SetSpecificationFlag "Link to this definition")  
Sets the specification flag.

Parameters:  **state** (*bool*) – True to enable, False to disable the specification flag

SetStimulationPackageFlag(*state=True*)[¶](#ApiClient.Package.SetStimulationPackageFlag "Link to this definition")  
Sets the stimulation package flag.

Parameters:  **state** (*bool*) – True to enable, False to disable the stimulation package flag

SetTestCaseFlag(*state=True*)[¶](#ApiClient.Package.SetTestCaseFlag "Link to this definition")  
Sets the test case flag.

Parameters:  **state** (*bool*) – True to enable, False to disable the test case flag

SetTestScriptId(*testSriptId*)[¶](#ApiClient.Package.SetTestScriptId "Link to this definition")  
Sets the test script id of the package.

Parameters:  **testSriptId** (*str*) – Test script id

SetVersion(*version*)[¶](#ApiClient.Package.SetVersion "Link to this definition")  
Sets the package version.

Parameters:  **version** (*str*) – Version to be shown in the package properties

GetSignalGroups()[¶](#ApiClient.Package.GetSignalGroups "Link to this definition")  
Returns a list of all the signal groups within the package. Signals and signal recording groups are attributed to their corresponding signal group.

Returns:  List of all the signal groups

Return type:  list[[`SignalGroup`](SignalRecordingApi.md#ApiClient.SignalGroup "ApiClient.SignalGroup")]

Deprecated since version 2020.1: Please use [`GetRecordingConfig().GetSignalGroups()`](#ApiClient.RecordingConfig.GetSignalGroups "ApiClient.RecordingConfig.GetSignalGroups") instead.

GetSyncConfig()[¶](#ApiClient.Package.GetSyncConfig "Link to this definition")  
Returns the synchronization configuration.

Returns:  The synchronization configuration

Return type:  [`SyncConfig`](TraceAnalysisApi.md#ApiClient.SyncConfig "ApiClient.SyncConfig")

Raises:  
**ApiError** – when synchronization is done in trace analysis. Please migrate package with [`GetRecordingConfig().MigrateSyncConfig()`](#ApiClient.RecordingConfig.MigrateSyncConfig "ApiClient.RecordingConfig.MigrateSyncConfig").

Deprecated since version 2020.1: Please use [`GetRecordingConfig().GetSyncConfig()`](#ApiClient.RecordingConfig.GetSyncConfig "ApiClient.RecordingConfig.GetSyncConfig") instead.

GetTraceMergeFilePathExpression()[¶](#ApiClient.Package.GetTraceMergeFilePathExpression "Link to this definition")  
Returns the path expression of the file where the MDF3 traces are merged into.

Returns:  The path expression

Return type:  str

Deprecated since version 2020.1: Please use [`GetRecordingConfig().GetTraceMergeFilePathExpression()`](#ApiClient.RecordingConfig.GetTraceMergeFilePathExpression "ApiClient.RecordingConfig.GetTraceMergeFilePathExpression") instead.

GetVariableRecordingGroup()[¶](#ApiClient.Package.GetVariableRecordingGroup "Link to this definition")  
Returns the recording group representing recorded variables.

It can be used for the generic signal binding and trace synchronization of trace analyses as well as the assignment of recordings containing test case variables for the offline analysis.

Returns:  The variable recording group

Return type:  [`VariableRecordingGroup`](#ApiClient.VariableRecordingGroup "ApiClient.VariableRecordingGroup")

Deprecated since version 2020.1: Please use [`GetRecordingConfig().GetVariableRecordingGroup()`](#ApiClient.RecordingConfig.GetVariableRecordingGroup "ApiClient.RecordingConfig.GetVariableRecordingGroup") instead.

IsTraceMergeActive()[¶](#ApiClient.Package.IsTraceMergeActive "Link to this definition")  
Returns whether the merging of MDF3 traces is activated.

Returns:  Activation status of trace merge

Return type:  boolean

Deprecated since version 2020.1: Please use [`GetRecordingConfig().IsTraceMergeActive()`](#ApiClient.RecordingConfig.IsTraceMergeActive "ApiClient.RecordingConfig.IsTraceMergeActive") instead.

MigrateSyncConfig()[¶](#ApiClient.Package.MigrateSyncConfig "Link to this definition")  
Migrates synchronization and MDF3 merge configuration from trace analyses to the recording configuration.

If several trace analyses contain differing settings for synchronization and MDF3 merge, migration will fail. In this case, use [`GetRecordingConfig().MigrateSyncConfigUsing()`](#ApiClient.RecordingConfig.MigrateSyncConfigUsing "ApiClient.RecordingConfig.MigrateSyncConfigUsing").

Raises:  
**ApiError** – when migration is not possible.

Deprecated since version 2020.1: Please use [`GetRecordingConfig().MigrateSyncConfig()`](#ApiClient.RecordingConfig.MigrateSyncConfig "ApiClient.RecordingConfig.MigrateSyncConfig") instead.

MigrateSyncConfigUsing(*traceAnalysis*)[¶](#ApiClient.Package.MigrateSyncConfigUsing "Link to this definition")  
Migrates synchronization and MDF3 merge configuration from a specific trace analysis to the recording configuration.

Parameters:  **traceAnalysis** ([`TraceAnalysis`](TraceAnalysisApi.md#ApiClient.TraceAnalysis "ApiClient.TraceAnalysis")) – Use configuration from this trace analysis as new configuration.

Deprecated since version 2020.1: Please use [`GetRecordingConfig().MigrateSyncConfigUsing()`](#ApiClient.RecordingConfig.MigrateSyncConfigUsing "ApiClient.RecordingConfig.MigrateSyncConfigUsing") instead.

RemoveSignalGroup(*signalGroup*)[¶](#ApiClient.Package.RemoveSignalGroup "Link to this definition")  
Removes a signal group from the package. All relations to recording groups of the signal group will be lost.

Parameters:  **signalGroup** ([`SignalGroup`](SignalRecordingApi.md#ApiClient.SignalGroup "ApiClient.SignalGroup")) – The signal group to be removed

Deprecated since version 2020.1: Please use [`GetRecordingConfig().RemoveSignalGroup()`](#ApiClient.RecordingConfig.RemoveSignalGroup "ApiClient.RecordingConfig.RemoveSignalGroup") instead.

SetTraceMergeActive(*active=True*)[¶](#ApiClient.Package.SetTraceMergeActive "Link to this definition")  
Enables or disables the merging of MDF3 traces.

Parameters:  **active** (*boolean*) – If set to False, trace merge will be deactivated. Otherwise trace merge will be activated.

Deprecated since version 2020.1: Please use [`GetRecordingConfig().SetTraceMergeActive()`](#ApiClient.RecordingConfig.SetTraceMergeActive "ApiClient.RecordingConfig.SetTraceMergeActive") instead.

SetTraceMergeFilePathExpression(*expression*)[¶](#ApiClient.Package.SetTraceMergeFilePathExpression "Link to this definition")  
Sets the path expression of the file where the MDF3 traces are merged into.

Parameters:  **expression** (*str*) – The path expression

Deprecated since version 2020.1: Please use [`GetRecordingConfig().SetTraceMergeFilePathExpression()`](#ApiClient.RecordingConfig.SetTraceMergeFilePathExpression "ApiClient.RecordingConfig.SetTraceMergeFilePathExpression") instead.

## RecordingConfig[¶](#recordingconfig "Link to this heading")

*class* RecordingConfig[¶](#ApiClient.RecordingConfig "Link to this definition")  
Returned by

- [`Package.GetRecordingConfig`](#ApiClient.Package.GetRecordingConfig "ApiClient.Package.GetRecordingConfig")

TRACE_MERGE_MODE_DEPRECATED_MDF3[¶](#ApiClient.RecordingConfig.TRACE_MERGE_MODE_DEPRECATED_MDF3 "Link to this definition")  
Returns the constant used to specify the trace merge mode to the deprecated legacy MDF3 trace merge.

Returns:  The constant

Return type:  int

TRACE_MERGE_MODE_SIGNAL_BASED[¶](#ApiClient.RecordingConfig.TRACE_MERGE_MODE_SIGNAL_BASED "Link to this definition")  
Returns the constant used to specify the trace merge mode ‘signal based’.

Returns:  The constant

Return type:  int

AppendSignalGroup(*signalGroup*, *defaultRecordingGroup=None*, *allowNewName=False*)[¶](#ApiClient.RecordingConfig.AppendSignalGroup "Link to this definition")  
Adds a signal group to the package. If no default recording group is given, a new recording group will be created.

Parameters:  - **signalGroup** ([`SignalGroup`](SignalRecordingApi.md#ApiClient.SignalGroup "ApiClient.SignalGroup")) – The signal group to be added

- **defaultRecordingGroup** ([`RecordingGroup`](SignalRecordingApi.md#ApiClient.RecordingGroup "ApiClient.RecordingGroup")) – The default recording group of the signal group

- **allowNewName** (*boolean*) – If True, a new name will be generated for the signal group if there already exists a signal group with the same name in the package. Default value is False, so an error will be raised if the name already exists.

Clone()[¶](#ApiClient.RecordingConfig.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`RecordingConfig`](#ApiClient.RecordingConfig "ApiClient.RecordingConfig")

GetAutoAssignSignalGroup()[¶](#ApiClient.RecordingConfig.GetAutoAssignSignalGroup "Link to this definition")  
Returns the special auto assign signal group. This signal group is available per default. Signals added to this group will be automatically assigned to matching existing signal groups during package execution.

Returns:  The auto assign signal group

Return type:  [`AutoAssignSignalGroup`](#ApiClient.AutoAssignSignalGroup "ApiClient.AutoAssignSignalGroup")

GetSignalGroups()[¶](#ApiClient.RecordingConfig.GetSignalGroups "Link to this definition")  
Returns a list of all the signal groups within the package. Signals and signal recording groups are attributed to their corresponding signal group.

Returns:  List of all the signal groups

Return type:  list[[`SignalGroup`](SignalRecordingApi.md#ApiClient.SignalGroup "ApiClient.SignalGroup")]

GetSyncConfig()[¶](#ApiClient.RecordingConfig.GetSyncConfig "Link to this definition")  
Returns the synchronization configuration.

Returns:  The synchronization configuration

Return type:  [`SyncConfig`](TraceAnalysisApi.md#ApiClient.SyncConfig "ApiClient.SyncConfig")

Raises:  
**ApiError** – when synchronization is done in trace analysis. Please migrate package with `MigrateSyncConfig()`.

GetTraceMergeFilePathExpression()[¶](#ApiClient.RecordingConfig.GetTraceMergeFilePathExpression "Link to this definition")  
Returns the path expression of the file where the traces are merged into.

Returns:  The path expression

Return type:  str

GetTraceMergeMode()[¶](#ApiClient.RecordingConfig.GetTraceMergeMode "Link to this definition")  
Returns the mode used to merged traces.

Returns:  The mode. One of [`RecordingConfig.TRACE_MERGE_MODE_SIGNAL_BASED`](#ApiClient.RecordingConfig.TRACE_MERGE_MODE_SIGNAL_BASED "ApiClient.RecordingConfig.TRACE_MERGE_MODE_SIGNAL_BASED"), [`RecordingConfig.TRACE_MERGE_MODE_DEPRECATED_MDF3`](#ApiClient.RecordingConfig.TRACE_MERGE_MODE_DEPRECATED_MDF3 "ApiClient.RecordingConfig.TRACE_MERGE_MODE_DEPRECATED_MDF3")

Return type:  int

GetVariableRecordingGroup()[¶](#ApiClient.RecordingConfig.GetVariableRecordingGroup "Link to this definition")  
Returns the recording group representing recorded variables.

It can be used for the generic signal binding and trace synchronization of trace analyses as well as the assignment of recordings containing test case variables for the offline analysis.

Returns:  The variable recording group

Return type:  [`VariableRecordingGroup`](#ApiClient.VariableRecordingGroup "ApiClient.VariableRecordingGroup")

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

MigrateSyncConfigUsing(*traceAnalysis*)[¶](#ApiClient.RecordingConfig.MigrateSyncConfigUsing "Link to this definition")  
Migrates synchronization and MDF3 merge configuration from a specific trace analysis to the recording configuration.

Parameters:  **traceAnalysis** ([`TraceAnalysis`](TraceAnalysisApi.md#ApiClient.TraceAnalysis "ApiClient.TraceAnalysis")) – Use configuration from this trace analysis as new configuration.

RemoveSignalGroup(*signalGroup*)[¶](#ApiClient.RecordingConfig.RemoveSignalGroup "Link to this definition")  
Removes a signal group from the package. All relations to recording groups of the signal group will be lost.

Parameters:  **signalGroup** ([`SignalGroup`](SignalRecordingApi.md#ApiClient.SignalGroup "ApiClient.SignalGroup")) – The signal group to be removed

SetRecordAllTestQuantities(*value*)[¶](#ApiClient.RecordingConfig.SetRecordAllTestQuantities "Link to this definition")  
Sets whether all test quantities shall be recorded.

For each test quantity there must be an existing signal group whose name matches the test quantity’s system under test or whose contained signals address the same system under test.

Parameters:  **value** (*bool*) – True if all test quantities shall be recorded.

SetRecordAllTestQuantitiesRecursive(*value*)[¶](#ApiClient.RecordingConfig.SetRecordAllTestQuantitiesRecursive "Link to this definition")  
Sets whether test quantities shall be collected recursively (including test quantities from sub packages) if the option to record all test quantities is set.

Parameters:  **value** (*bool*) – True if test quantities shall be collected recursively.

SetTraceMergeActive(*active=True*)[¶](#ApiClient.RecordingConfig.SetTraceMergeActive "Link to this definition")  
Enables or disables the merging of traces.

Parameters:  **active** (*boolean*) – If set to False, trace merge will be deactivated. Otherwise trace merge will be activated.

SetTraceMergeFilePathExpression(*expression*)[¶](#ApiClient.RecordingConfig.SetTraceMergeFilePathExpression "Link to this definition")  
Sets the path expression of the file where the traces are merged into.

Parameters:  **expression** (*str*) – The path expression

SetTraceMergeMode(*mode*)[¶](#ApiClient.RecordingConfig.SetTraceMergeMode "Link to this definition")  
Sets the mode used to merged traces.

Parameters:  **mode** (*int*) – The mode. One of [`RecordingConfig.TRACE_MERGE_MODE_SIGNAL_BASED`](#ApiClient.RecordingConfig.TRACE_MERGE_MODE_SIGNAL_BASED "ApiClient.RecordingConfig.TRACE_MERGE_MODE_SIGNAL_BASED"), [`RecordingConfig.TRACE_MERGE_MODE_DEPRECATED_MDF3`](#ApiClient.RecordingConfig.TRACE_MERGE_MODE_DEPRECATED_MDF3 "ApiClient.RecordingConfig.TRACE_MERGE_MODE_DEPRECATED_MDF3")
