# API for Project Components[¶](#api-for-project-components "Link to this heading")

Part of the [Object based program API](objectApi.md#objectapi)

## ComponentApi[¶](#componentapi "Link to this heading")

*class* ComponentApi[¶](#ApiClient.ComponentApi "Link to this definition")  
API to access projects

Returned by

- [`ProjectApi.ComponentApi`](ProjectApi.md#ApiClient.ProjectApi.ComponentApi "ApiClient.ProjectApi.ComponentApi")

CreateAnalysisPackageCall(*name*, *packagePath*, *libraryNamespace=None*)[¶](#ApiClient.ComponentApi.CreateAnalysisPackageCall "Link to this definition")  
Returns the created analysis package call.

Parameters:  - **name** (*str*) – Name of the analysis package call

- **packagePath** (*str*) – Path to the package to be called (absolute or relative to package directory)

- **libraryNamespace** (*str*) – Namespace of a library workspace (requires feature flag; packagePath must be relative)

Returns:  Package call

Return type:  [`AnalysisPackageCall`](#ApiClient.AnalysisPackageCall "ApiClient.AnalysisPackageCall")

CreateConfigChange(*name*, *tcfFile*, *tbcFile*)[¶](#ApiClient.ComponentApi.CreateConfigChange "Link to this definition")  
Returns the created config change.

Parameters:  - **name** (*str*) – Name of the config change

- **tcfFile** (*str*) – Path of the tcf file

- **tbcFile** (*str*) – Path to the tbc file

Returns:  Config change

Return type:  [`ConfigChange`](#ApiClient.ConfigChange "ApiClient.ConfigChange")

CreateFolder(*name*)[¶](#ApiClient.ComponentApi.CreateFolder "Link to this definition")  
Returns the created folder.

Parameters:  **name** (*str*) – Name of the folder

Returns:  Project Folder

Return type:  [`ProjectFolder`](#ApiClient.ProjectFolder "ApiClient.ProjectFolder")

CreatePackageCall(*name*, *packagePath*, *libraryNamespace=None*)[¶](#ApiClient.ComponentApi.CreatePackageCall "Link to this definition")  
Returns the created package call.

Parameters:  - **name** (*str*) – Name of the package call

- **packagePath** (*str*) – Path to the package to be called (absolute or relative to package directory)

- **libraryNamespace** (*str*) – Namespace of a library workspace (requires feature flag; packagePath must be relative)

Returns:  Package call

Return type:  [`PackageCall`](#ApiClient.PackageCall "ApiClient.PackageCall")

CreatePackageGenerator(*name*, *generatorId*)[¶](#ApiClient.ComponentApi.CreatePackageGenerator "Link to this definition")  
Returns the created package generator.

Parameters:  - **name** (*str*) – Name of the generator

- **generatorId** (*str*) – Unique identifier of the generator to be created

Returns:  Package generator

Return type:  [`PackageGenerator`](#ApiClient.PackageGenerator "ApiClient.PackageGenerator")

CreateProjectCall(*name*, *projectPath*, *libraryNamespace=None*)[¶](#ApiClient.ComponentApi.CreateProjectCall "Link to this definition")  
Returns the created project call.

Parameters:  - **name** (*str*) – Name of the project call

- **projectPath** (*str*) – Path to the project to be called. In contrast to the method CreatePackageCall(), this path must be relative to the parent project. Absolute paths are also allowed. If an absolute path is used that is inside a currently defined library workspace, the project call will be a reference into this workspace.

- **libraryNamespace** (*str*) – Namespace of a library workspace (requires feature flag; projectPath must be relative)

Returns:  Project call

Return type:  [`ProjectCall`](#ApiClient.ProjectCall "ApiClient.ProjectCall")

CreateProjectGenerator(*name*, *generatorId*)[¶](#ApiClient.ComponentApi.CreateProjectGenerator "Link to this definition")  
Returns the created project generator.

Parameters:  - **name** (*str*) – Name of the generator

- **generatorId** (*str*) – Unique identifier of the generator to be created

Returns:  Project generator

Return type:  [`ProjectGenerator`](#ApiClient.ProjectGenerator "ApiClient.ProjectGenerator")

CreateStimulationPackageCall(*name*, *packagePath*, *libraryNamespace=None*)[¶](#ApiClient.ComponentApi.CreateStimulationPackageCall "Link to this definition")  
Returns the created stimulation package call.

Parameters:  - **name** (*str*) – Name of the stimulation package call

- **packagePath** (*str*) – Path to the package to be called (absolute or relative to package directory)

- **libraryNamespace** (*str*) – Namespace of a library workspace (requires feature flag; packagePath must be relative)

Returns:  Package call

Return type:  [`StimulationPackageCall`](#ApiClient.StimulationPackageCall "ApiClient.StimulationPackageCall")

## AnalysisPackageCall[¶](#analysispackagecall "Link to this heading")

*class* AnalysisPackageCall[¶](#ApiClient.AnalysisPackageCall "Link to this definition")  
An analysis package call in a project.

Base class

[`ProjectComponent`](#ApiClient.ProjectComponent "ApiClient.ProjectComponent")

Returned by

- [`ComponentApi.CreateAnalysisPackageCall`](#ApiClient.ComponentApi.CreateAnalysisPackageCall "ApiClient.ComponentApi.CreateAnalysisPackageCall")

- [`Project.GetAnalysisPackageCalls`](ProjectApi.md#ApiClient.Project.GetAnalysisPackageCalls "ApiClient.Project.GetAnalysisPackageCalls")

- [`StimulationPackageCall.GetAnalysisPackageCalls`](#ApiClient.StimulationPackageCall.GetAnalysisPackageCalls "ApiClient.StimulationPackageCall.GetAnalysisPackageCalls")

Subclasses

- [`AnalysisPackageMappingCall`](#ApiClient.AnalysisPackageMappingCall "ApiClient.AnalysisPackageMappingCall")

AddParameterGenerator(*name*, *generatorId*)[¶](#ApiClient.AnalysisPackageCall.AddParameterGenerator "Link to this definition")  
Adds a parameter generator to the package call.

Parameters:  - **name** (*str*) – Name of the parameter generator.

- **generatorId** (*str*) – Unique generator id of generator to be added.

Returns:  The parameter generator.

Return type:  [`ParameterGenerator`](#ApiClient.ParameterGenerator "ApiClient.ParameterGenerator")

AddParameterSet(*name*, *position=None*)[¶](#ApiClient.AnalysisPackageCall.AddParameterSet "Link to this definition")  
Adds a parameter set to the analysis package call.

Please note, that only parameters, mappings, and test management settings of parameters sets are permitted for parameter sets of analysis package calls!

Parameters:  - **name** (*str*) – Name of the parameter set

- **position** (*integer*) – Position to insert the parameter set inside the analysis package call

Returns:  The parameter set

Return type:  [`ParameterSetAnalysisPackage`](#ApiClient.ParameterSetAnalysisPackage "ApiClient.ParameterSetAnalysisPackage")

AddParameterVariationGenerator(*name*)[¶](#ApiClient.AnalysisPackageCall.AddParameterVariationGenerator "Link to this definition")  
Adds a parameter variation generator to the analysis package call.

Parameters:  **name** (*str*) – Name of the parameter variation generator.

Returns:  The parameter variation generator.

Return type:  [`ParameterVariationGeneratorComponent`](#ApiClient.ParameterVariationGeneratorComponent "ApiClient.ParameterVariationGeneratorComponent")

Clone()[¶](#ApiClient.AnalysisPackageCall.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`AnalysisPackageCall`](#ApiClient.AnalysisPackageCall "ApiClient.AnalysisPackageCall")

GetAbsolutePath()[¶](#ApiClient.AnalysisPackageCall.GetAbsolutePath "Link to this definition")  
Returns the absolute path to referenced package.

Returns:  Absolute path to referenced package

Return type:  str

GetAutoAssignParameters()[¶](#ApiClient.AnalysisPackageCall.GetAutoAssignParameters "Link to this definition")  
Returns whether parameters without assigned value (via parameter set/general project parameterization) should automatically use an equally named return value of the stimulation package if one exists.

Returns:  True, if the auto assignment is enabled. Otherwise, False.

Return type:  bool

GetComponents()[¶](#ApiClient.AnalysisPackageCall.GetComponents "Link to this definition")  
Returns all direct children of the package call.

Returns:  List with all children components

Return type:  list[[`ProjectComponent`](#ApiClient.ProjectComponent "ApiClient.ProjectComponent")]

GetImplementedAnalysisLabel()[¶](#ApiClient.AnalysisPackageCall.GetImplementedAnalysisLabel "Link to this definition")  
Returns the label for the trace analysis implemented by this package.

Returns:  trace analysis label

Return type:  str

GetName()[¶](#ApiClient.AnalysisPackageCall.GetName "Link to this definition")  
Returns the name of the project component.

Returns:  Name of the component

Return type:  str

GetPackage()[¶](#ApiClient.AnalysisPackageCall.GetPackage "Link to this definition")  
Returns the referenced analysis package.

Returns:  Referenced analysis package

Return type:  [`AnalysisPackage`](PackageApi.md#ApiClient.AnalysisPackage "ApiClient.AnalysisPackage")

Raises:  
**ApiError** – If the referenced analyse package file (\*.ta) can not be opened.

GetParameterGenerators(*skipDisabled=True*)[¶](#ApiClient.AnalysisPackageCall.GetParameterGenerators "Link to this definition")  
Returns all parameter generators of the analysis package call.

Parameters:  **skipDisabled** (*bool*) – Defines whether disabled components should be included.

Returns:  The parameter generators.

Return type:  list[[`ParameterGenerator`](#ApiClient.ParameterGenerator "ApiClient.ParameterGenerator")]

GetParameterSets(*skipDisabled=True*)[¶](#ApiClient.AnalysisPackageCall.GetParameterSets "Link to this definition")  
Returns all parameter sets of the analysis package call.

Parameters:  **skipDisabled** (*boolean*) – Defines whether disabled components should be included.

Returns:  Parameter sets

Return type:  list[[`ParameterSetAnalysisPackage`](#ApiClient.ParameterSetAnalysisPackage "ApiClient.ParameterSetAnalysisPackage")]

GetParameterVariationGenerators(*skipDisabled=True*)[¶](#ApiClient.AnalysisPackageCall.GetParameterVariationGenerators "Link to this definition")  
Returns all parameter variation generators of the analysis package call.

Parameters:  **skipDisabled** (*bool*) – Defines whether disabled generators should be excluded.

Returns:  The parameter variation generators.

Return type:  list[[`ParameterVariationGeneratorComponent`](#ApiClient.ParameterVariationGeneratorComponent "ApiClient.ParameterVariationGeneratorComponent")]

GetParent()[¶](#ApiClient.AnalysisPackageCall.GetParent "Link to this definition")  
Returns the parent project component.

Returns:  Parent component

Return type:  [`ProjectComponent`](#ApiClient.ProjectComponent "ApiClient.ProjectComponent")

GetPosition()[¶](#ApiClient.AnalysisPackageCall.GetPosition "Link to this definition")  
Returns the position in the parent project.

Returns:  parent position

Return type:  integer

GetProjectRelativePath()[¶](#ApiClient.AnalysisPackageCall.GetProjectRelativePath "Link to this definition")  
Returns the file project relative path of the referenced package.

The returned path is a relative path, its base is the folder where the calling project is located, just like the path is shown in the package test step’s dialog.

Returns:  File name with relative path of the package to be called.

Return type:  str

Raises:  
**ProjectNotSavedError** – If this method is called before project is saved.

GetStimulationPackageCall()[¶](#ApiClient.AnalysisPackageCall.GetStimulationPackageCall "Link to this definition")  
Returns the stimulation package call connected to this analysis package.

This method will return None if the analysis package is run for all previous stimulations (see `SetRunForPreviousStimulations()`).

Returns:  Stimulation package call. Returns None if no stimulation package call is set or the referenced stimulation package call was not found in the project.

Return type:  [`StimulationPackageCall`](#ApiClient.StimulationPackageCall "ApiClient.StimulationPackageCall")

GetStimulationPackageCalls()[¶](#ApiClient.AnalysisPackageCall.GetStimulationPackageCalls "Link to this definition")  
Returns a list containing all related stimulation package calls, i.e. either all previous stimulation package calls if the corresponding option is set or the explicitly connected stimulation package call. In the latter case, see also `GetStimulationPackageCall()`.

Returns:  list of related stimulation package calls

Return type:  list[[`StimulationPackageCall`](#ApiClient.StimulationPackageCall "ApiClient.StimulationPackageCall")]

GetTestCaseId()[¶](#ApiClient.AnalysisPackageCall.GetTestCaseId "Link to this definition")  
Returns the test case id for the analysis package call.

Returns:  Test case id

Return type:  str

GetTestScriptId()[¶](#ApiClient.AnalysisPackageCall.GetTestScriptId "Link to this definition")  
Returns the test script id of the corresponding analysis package.

Returns:  Test script id

Return type:  str

GetType()[¶](#ApiClient.AnalysisPackageCall.GetType "Link to this definition")  
Returns the type (class name) of the project component, e.g.  
- “ConfigChange”

- “ParameterSet”

- “PackageCall”

- “Project”

- “PackageGenerator”

Returns:  Type (class name) of the project component

Return type:  str

HasComponents()[¶](#ApiClient.AnalysisPackageCall.HasComponents "Link to this definition")  
Returns whether the package call has children.

Returns:  True if there are children, False otherwise.

Return type:  boolean

InsertParameterSet(*parameterSet*, *position=None*)[¶](#ApiClient.AnalysisPackageCall.InsertParameterSet "Link to this definition")  
Adds a parameter set to the analysis package call.

Please note, that only parameters and test management settings of parameters sets are permitted for parameter sets of analysis package calls!

Parameters:  - **parameterSet** ([`ParameterSetAnalysisPackage`](#ApiClient.ParameterSetAnalysisPackage "ApiClient.ParameterSetAnalysisPackage")) – parameter set

- **position** (*integer*) – Position to insert the parameter set inside the analysis package call

IsEnabled()[¶](#ApiClient.AnalysisPackageCall.IsEnabled "Link to this definition")  
Returns the state of the test step.

Returns:  True if test step is enabled, otherwise False

Return type:  bool

IsRunForPreviousStimulations()[¶](#ApiClient.AnalysisPackageCall.IsRunForPreviousStimulations "Link to this definition")  
Returns whether the analysis package call is run for all previous stimulation package calls.

Returns:  True, if run for all stimulations. Otherwise, False.

Return type:  bool

RemoveFromProject()[¶](#ApiClient.AnalysisPackageCall.RemoveFromProject "Link to this definition")  
Removes this component from the project.

Raises:  
**ApiError** – if the component is not part of any project

RemoveParameterGenerator(*paramGenerator*)[¶](#ApiClient.AnalysisPackageCall.RemoveParameterGenerator "Link to this definition")  
Removes a parameter generator from the package call.

Parameters:  **paramGenerator** ([`ParameterGenerator`](#ApiClient.ParameterGenerator "ApiClient.ParameterGenerator")) – The parameter generator to be removed.

Raises:  
**ApiError** –

- If the given parameter generator is not part of the package call

- If paramGenerator is not of type [`ParameterGenerator`](#ApiClient.ParameterGenerator "ApiClient.ParameterGenerator")

RemoveParameterSet(*paramSet*)[¶](#ApiClient.AnalysisPackageCall.RemoveParameterSet "Link to this definition")  
Removes a parameter set from the analysis package call.

Parameters:  **paramSet** ([`ParameterSetAnalysisPackage`](#ApiClient.ParameterSetAnalysisPackage "ApiClient.ParameterSetAnalysisPackage")) – The parameter set to be removed

Raises:  
**ApiError** –

- If the given parameter set is not part of the package call

- If paramGenerator is not of type [`ParameterSetAnalysisPackage`](#ApiClient.ParameterSetAnalysisPackage "ApiClient.ParameterSetAnalysisPackage")

RemoveParameterVariationGenerator(*paramVariationGenerator*)[¶](#ApiClient.AnalysisPackageCall.RemoveParameterVariationGenerator "Link to this definition")  
Removes a parameter variation generator from the analysis package call.

Parameters:  **paramVariationGenerator** ([`ParameterVariationGeneratorComponent`](#ApiClient.ParameterVariationGeneratorComponent "ApiClient.ParameterVariationGeneratorComponent")) – The parameter variation generator to be removed.

Raises:  
**ApiError** –

- If the given parameter variation generator is not part of the package call

- If paramVariationGenerator is not of type [`ParameterVariationGeneratorComponent`](#ApiClient.ParameterVariationGeneratorComponent "ApiClient.ParameterVariationGeneratorComponent")

SetAutoAssignParameters(*value*)[¶](#ApiClient.AnalysisPackageCall.SetAutoAssignParameters "Link to this definition")  
Sets whether parameters without assigned value (via parameter set/general project parameterization) should automatically use an equally named return value of the stimulation package if one exists.

Parameters:  **value** (*bool*) – True, to enable the auto assignment. Otherwise, False.

SetEnabled(*state=True*)[¶](#ApiClient.AnalysisPackageCall.SetEnabled "Link to this definition")  
Enable or disable the test step.

Parameters:  **state** (*bool*) – True (=Default) to enable, False to disable the test step.

SetImplementedAnalysisLabel(*label*)[¶](#ApiClient.AnalysisPackageCall.SetImplementedAnalysisLabel "Link to this definition")  
Sets the label for the trace analysis implemented by this package.

The label cannot be set for analysis packages that are run for all previous stimulations (see `SetRunForPreviousStimulations()`).

Parameters:  **label** (*str*) – trace analysis label

SetName(*name*)[¶](#ApiClient.AnalysisPackageCall.SetName "Link to this definition")  
Sets the name of the project component.

Parameters:  **name** (*str*) – Name of the component

SetRunForPreviousStimulations()[¶](#ApiClient.AnalysisPackageCall.SetRunForPreviousStimulations "Link to this definition")  
Sets whether the analysis package is run for all previous stimulation package calls. If this option is set, `GetStimulationPackageCall()` will return None. This option is unset automatically if a specific stimulation package call is set by `SetStimulationPackageCall()`.

SetStimulationPackageCall(*stimulationPackage*)[¶](#ApiClient.AnalysisPackageCall.SetStimulationPackageCall "Link to this definition")  
Connects the given stimulation package call with this analysis package.

Parameters:  **stimulationPackage** ([`StimulationPackageCall`](#ApiClient.StimulationPackageCall "ApiClient.StimulationPackageCall")) – Stimulation package

SetTestCaseId(*testCaseId*)[¶](#ApiClient.AnalysisPackageCall.SetTestCaseId "Link to this definition")  
Sets the test case id for the analysis package call.

Parameters:  **testCaseId** (*str*) – Test case id

## ParameterGenerator[¶](#parametergenerator "Link to this heading")

*class* ParameterGenerator[¶](#ApiClient.ParameterGenerator "Link to this definition")  
Base class

[`ProjectComponent`](#ApiClient.ProjectComponent "ApiClient.ProjectComponent")

Returned by

- [`AnalysisPackageCall.AddParameterGenerator`](#ApiClient.AnalysisPackageCall.AddParameterGenerator "ApiClient.AnalysisPackageCall.AddParameterGenerator")

- [`AnalysisPackageCall.GetParameterGenerators`](#ApiClient.AnalysisPackageCall.GetParameterGenerators "ApiClient.AnalysisPackageCall.GetParameterGenerators")

- [`AnalysisPackageMappingCall.AddParameterGenerator`](#ApiClient.AnalysisPackageMappingCall.AddParameterGenerator "ApiClient.AnalysisPackageMappingCall.AddParameterGenerator")

- [`AnalysisPackageMappingCall.GetParameterGenerators`](#ApiClient.AnalysisPackageMappingCall.GetParameterGenerators "ApiClient.AnalysisPackageMappingCall.GetParameterGenerators")

- [`PackageCall.AddParameterGenerator`](#ApiClient.PackageCall.AddParameterGenerator "ApiClient.PackageCall.AddParameterGenerator")

- [`PackageCall.GetParameterGenerators`](#ApiClient.PackageCall.GetParameterGenerators "ApiClient.PackageCall.GetParameterGenerators")

- [`Project.GetParameterGenerators`](ProjectApi.md#ApiClient.Project.GetParameterGenerators "ApiClient.Project.GetParameterGenerators")

- [`StimulationPackageCall.AddParameterGenerator`](#ApiClient.StimulationPackageCall.AddParameterGenerator "ApiClient.StimulationPackageCall.AddParameterGenerator")

- [`StimulationPackageCall.GetParameterGenerators`](#ApiClient.StimulationPackageCall.GetParameterGenerators "ApiClient.StimulationPackageCall.GetParameterGenerators")

Subclasses

- [`PackageGenerator`](#ApiClient.PackageGenerator "ApiClient.PackageGenerator")

- [`ProjectGenerator`](#ApiClient.ProjectGenerator "ApiClient.ProjectGenerator")

Clone()[¶](#ApiClient.ParameterGenerator.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`ParameterGenerator`](#ApiClient.ParameterGenerator "ApiClient.ParameterGenerator")

GenerateProject(*destinationPath*)[¶](#ApiClient.ParameterGenerator.GenerateProject "Link to this definition")  
Initiates the execution of the generator and stores the result as a new project file.

Parameters:  **destinationPath** (*str*) – Absolute destination path to store the project file

GetAttribute(*attributeName*)[¶](#ApiClient.ParameterGenerator.GetAttribute "Link to this definition")  
Returns the value of the attribute of the given name. Value is returned as str. Examples: int 5 –\> u”5” string “5” –\> u“‘5’” list [1,2,3] –\> u”[1,2,3]”

Parameters:  **attributeName** (*str*) – Name of attribute to be returned

Returns:  attribute value

Return type:  str

GetGeneratorAttributes()[¶](#ApiClient.ParameterGenerator.GetGeneratorAttributes "Link to this definition")  
Returns all the stored attributes of the generator. Values are returned as str. Examples: int 5 –\> u”5” string “5” –\> u“‘5’” list [1,2,3] –\> u”[1,2,3]”

Returns:  Dictionary mapping attributes names to values

Return type:  dict[str, str]

GetGeneratorId()[¶](#ApiClient.ParameterGenerator.GetGeneratorId "Link to this definition")  
Returns the unique generator id of the referenced parameter generator.

Returns:  generator id

Return type:  str

GetName()[¶](#ApiClient.ParameterGenerator.GetName "Link to this definition")  
Returns the name of the project component.

Returns:  Name of the component

Return type:  str

GetParent()[¶](#ApiClient.ParameterGenerator.GetParent "Link to this definition")  
Returns the parent project component.

Returns:  Parent component

Return type:  [`ProjectComponent`](#ApiClient.ProjectComponent "ApiClient.ProjectComponent")

GetPosition()[¶](#ApiClient.ParameterGenerator.GetPosition "Link to this definition")  
Returns the position in the parent project.

Returns:  parent position

Return type:  integer

GetType()[¶](#ApiClient.ParameterGenerator.GetType "Link to this definition")  
Returns the type (class name) of the project component, e.g.  
- “ConfigChange”

- “ParameterSet”

- “PackageCall”

- “Project”

- “PackageGenerator”

Returns:  Type (class name) of the project component

Return type:  str

IsEnabled()[¶](#ApiClient.ParameterGenerator.IsEnabled "Link to this definition")  
Returns the state of the test step.

Returns:  True if test step is enabled, otherwise False

Return type:  bool

RemoveFromProject()[¶](#ApiClient.ParameterGenerator.RemoveFromProject "Link to this definition")  
Removes this component from the project.

Raises:  
**ApiError** – if the component is not part of any project

SetAttribute(*attributeName*, *value*)[¶](#ApiClient.ParameterGenerator.SetAttribute "Link to this definition")  
Sets the value of the attribute of the given name. Value has to be provided as str. Examples: int 5 –\> u”5” string “5” –\> u“‘5’” list [1,2,3] –\> u”[1,2,3]”

Parameters:  - **attributeName** (*str*) – Name of attribute to be returned

- **value** (*str*) – attribute value

SetEnabled(*state=True*)[¶](#ApiClient.ParameterGenerator.SetEnabled "Link to this definition")  
Enable or disable the test step.

Parameters:  **state** (*bool*) – True (=Default) to enable, False to disable the test step.

SetGeneratorAttributes(*attributesDict*)[¶](#ApiClient.ParameterGenerator.SetGeneratorAttributes "Link to this definition")  
Overwrites the existing attributes of the generator with the provided ones. Values have to be provided as str. Examples: int 5 –\> u”5” string “5” –\> u“‘5’” list [1,2,3] –\> u”[1,2,3]”

Parameters:  **attributesDict** (*dict[str,* *str]*) – Dictionary mapping attribute names to values

SetName(*name*)[¶](#ApiClient.ParameterGenerator.SetName "Link to this definition")  
Sets the name of the project component.

Parameters:  **name** (*str*) – Name of the component

## ProjectComponent[¶](#projectcomponent "Link to this heading")

*class* ProjectComponent[¶](#ApiClient.ProjectComponent "Link to this definition")  
Returned by

- [`AnalysisPackageCall.GetComponents`](#ApiClient.AnalysisPackageCall.GetComponents "ApiClient.AnalysisPackageCall.GetComponents")

- [`AnalysisPackageCall.GetParent`](#ApiClient.AnalysisPackageCall.GetParent "ApiClient.AnalysisPackageCall.GetParent")

- [`AnalysisPackageMappingCall.GetComponents`](#ApiClient.AnalysisPackageMappingCall.GetComponents "ApiClient.AnalysisPackageMappingCall.GetComponents")

- [`AnalysisPackageMappingCall.GetParent`](#ApiClient.AnalysisPackageMappingCall.GetParent "ApiClient.AnalysisPackageMappingCall.GetParent")

- [`ConfigChange.GetParent`](#ApiClient.ConfigChange.GetParent "ApiClient.ConfigChange.GetParent")

- [`PackageCall.GetComponents`](#ApiClient.PackageCall.GetComponents "ApiClient.PackageCall.GetComponents")

- [`PackageCall.GetParent`](#ApiClient.PackageCall.GetParent "ApiClient.PackageCall.GetParent")

- [`PackageGenerator.GetParent`](#ApiClient.PackageGenerator.GetParent "ApiClient.PackageGenerator.GetParent")

- [`ParameterGenerator.GetParent`](#ApiClient.ParameterGenerator.GetParent "ApiClient.ParameterGenerator.GetParent")

- [`ParameterSet.GetParent`](ProjectApi.md#ApiClient.ParameterSet.GetParent "ApiClient.ParameterSet.GetParent")

- [`ParameterSetAnalysisPackage.GetParent`](#ApiClient.ParameterSetAnalysisPackage.GetParent "ApiClient.ParameterSetAnalysisPackage.GetParent")

- [`ParameterSetBase.GetParent`](#ApiClient.ParameterSetBase.GetParent "ApiClient.ParameterSetBase.GetParent")

- [`ParameterVariationGeneratorComponent.GetParent`](#ApiClient.ParameterVariationGeneratorComponent.GetParent "ApiClient.ParameterVariationGeneratorComponent.GetParent")

- [`Project.GetAllComponents`](ProjectApi.md#ApiClient.Project.GetAllComponents "ApiClient.Project.GetAllComponents")

- [`Project.GetComponentByPosition`](ProjectApi.md#ApiClient.Project.GetComponentByPosition "ApiClient.Project.GetComponentByPosition")

- [`Project.GetComponents`](ProjectApi.md#ApiClient.Project.GetComponents "ApiClient.Project.GetComponents")

- [`Project.GetParent`](ProjectApi.md#ApiClient.Project.GetParent "ApiClient.Project.GetParent")

- [`ProjectCall.GetParent`](#ApiClient.ProjectCall.GetParent "ApiClient.ProjectCall.GetParent")

- [`ProjectComponent.GetParent`](#ApiClient.ProjectComponent.GetParent "ApiClient.ProjectComponent.GetParent")

- [`ProjectFolder.GetComponents`](#ApiClient.ProjectFolder.GetComponents "ApiClient.ProjectFolder.GetComponents")

- [`ProjectFolder.GetParent`](#ApiClient.ProjectFolder.GetParent "ApiClient.ProjectFolder.GetParent")

- [`ProjectGenerator.GetParent`](#ApiClient.ProjectGenerator.GetParent "ApiClient.ProjectGenerator.GetParent")

- [`StimulationPackageCall.GetComponents`](#ApiClient.StimulationPackageCall.GetComponents "ApiClient.StimulationPackageCall.GetComponents")

- [`StimulationPackageCall.GetParent`](#ApiClient.StimulationPackageCall.GetParent "ApiClient.StimulationPackageCall.GetParent")

Subclasses

- [`AnalysisPackageCall`](#ApiClient.AnalysisPackageCall "ApiClient.AnalysisPackageCall")

- [`AnalysisPackageMappingCall`](#ApiClient.AnalysisPackageMappingCall "ApiClient.AnalysisPackageMappingCall")

- [`ConfigChange`](#ApiClient.ConfigChange "ApiClient.ConfigChange")

- [`PackageCall`](#ApiClient.PackageCall "ApiClient.PackageCall")

- [`PackageGenerator`](#ApiClient.PackageGenerator "ApiClient.PackageGenerator")

- [`ParameterGenerator`](#ApiClient.ParameterGenerator "ApiClient.ParameterGenerator")

- [`ParameterSet`](ProjectApi.md#ApiClient.ParameterSet "ApiClient.ParameterSet")

- [`ParameterSetAnalysisPackage`](#ApiClient.ParameterSetAnalysisPackage "ApiClient.ParameterSetAnalysisPackage")

- [`ParameterSetBase`](#ApiClient.ParameterSetBase "ApiClient.ParameterSetBase")

- [`ParameterVariationGeneratorComponent`](#ApiClient.ParameterVariationGeneratorComponent "ApiClient.ParameterVariationGeneratorComponent")

- [`Project`](ProjectApi.md#ApiClient.Project "ApiClient.Project")

- [`ProjectCall`](#ApiClient.ProjectCall "ApiClient.ProjectCall")

- [`ProjectFolder`](#ApiClient.ProjectFolder "ApiClient.ProjectFolder")

- [`ProjectGenerator`](#ApiClient.ProjectGenerator "ApiClient.ProjectGenerator")

- [`StimulationPackageCall`](#ApiClient.StimulationPackageCall "ApiClient.StimulationPackageCall")

Clone()[¶](#ApiClient.ProjectComponent.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`ProjectComponent`](#ApiClient.ProjectComponent "ApiClient.ProjectComponent")

GetName()[¶](#ApiClient.ProjectComponent.GetName "Link to this definition")  
Returns the name of the project component.

Returns:  Name of the component

Return type:  str

GetParent()[¶](#ApiClient.ProjectComponent.GetParent "Link to this definition")  
Returns the parent project component.

Returns:  Parent component

Return type:  [`ProjectComponent`](#ApiClient.ProjectComponent "ApiClient.ProjectComponent")

GetPosition()[¶](#ApiClient.ProjectComponent.GetPosition "Link to this definition")  
Returns the position in the parent project.

Returns:  parent position

Return type:  integer

GetType()[¶](#ApiClient.ProjectComponent.GetType "Link to this definition")  
Returns the type (class name) of the project component, e.g.  
- “ConfigChange”

- “ParameterSet”

- “PackageCall”

- “Project”

- “PackageGenerator”

Returns:  Type (class name) of the project component

Return type:  str

IsEnabled()[¶](#ApiClient.ProjectComponent.IsEnabled "Link to this definition")  
Returns the state of the test step.

Returns:  True if test step is enabled, otherwise False

Return type:  bool

RemoveFromProject()[¶](#ApiClient.ProjectComponent.RemoveFromProject "Link to this definition")  
Removes this component from the project.

Raises:  
**ApiError** – if the component is not part of any project

SetEnabled(*state=True*)[¶](#ApiClient.ProjectComponent.SetEnabled "Link to this definition")  
Enable or disable the test step.

Parameters:  **state** (*bool*) – True (=Default) to enable, False to disable the test step.

SetName(*name*)[¶](#ApiClient.ProjectComponent.SetName "Link to this definition")  
Sets the name of the project component.

Parameters:  **name** (*str*) – Name of the component

## ParameterSetAnalysisPackage[¶](#parametersetanalysispackage "Link to this heading")

*class* ParameterSetAnalysisPackage[¶](#ApiClient.ParameterSetAnalysisPackage "Link to this definition")  
Base classes

- [`ProjectComponent`](#ApiClient.ProjectComponent "ApiClient.ProjectComponent")

- [`ParameterSetBase`](#ApiClient.ParameterSetBase "ApiClient.ParameterSetBase")

Returned by

- [`AnalysisPackageCall.AddParameterSet`](#ApiClient.AnalysisPackageCall.AddParameterSet "ApiClient.AnalysisPackageCall.AddParameterSet")

- [`AnalysisPackageCall.GetParameterSets`](#ApiClient.AnalysisPackageCall.GetParameterSets "ApiClient.AnalysisPackageCall.GetParameterSets")

- [`AnalysisPackageMappingCall.AddParameterSet`](#ApiClient.AnalysisPackageMappingCall.AddParameterSet "ApiClient.AnalysisPackageMappingCall.AddParameterSet")

- [`AnalysisPackageMappingCall.GetParameterSets`](#ApiClient.AnalysisPackageMappingCall.GetParameterSets "ApiClient.AnalysisPackageMappingCall.GetParameterSets")

Attributes[¶](#ApiClient.ParameterSetAnalysisPackage.Attributes "Link to this definition")  
Returns access to the package attributes definitions specified within the parameter set and the referenced package attribute definition files.

Returns:  Package attribute interface of the parameter set

Return type:  [`Attributes`](ProjectApi.md#ApiClient.Attributes "ApiClient.Attributes")

GlobalConstants[¶](#ApiClient.ParameterSetAnalysisPackage.GlobalConstants "Link to this definition")  
Returns access to the global constants definitions specified within the parameter set and the referenced global constants definition files.

Returns:  Global constants interface of the parameter set

Return type:  [`GlobalConstants`](#ApiClient.GlobalConstants "ApiClient.GlobalConstants")

Mapping[¶](#ApiClient.ParameterSetAnalysisPackage.Mapping "Link to this definition")  
Returns access to the mapping of the parameter set.

Returns:  Mapping interface of the parameter set

Return type:  [`ParameterSetMapping`](#ApiClient.ParameterSetMapping "ApiClient.ParameterSetMapping")

MappingFiles[¶](#ApiClient.ParameterSetAnalysisPackage.MappingFiles "Link to this definition")  
Returns access to the mapping file list of the parameter set.

Returns:  Mapping file list object of the parameter set

Return type:  [`MappingFiles`](#ApiClient.MappingFiles "ApiClient.MappingFiles")

Parameters[¶](#ApiClient.ParameterSetAnalysisPackage.Parameters "Link to this definition")  
Returns access to the package parameters definitions specified within the parameter set and the referenced package parameters definition files.

Returns:  Package parameters interface of the parameter set

Return type:  [`PackageParameters`](#ApiClient.PackageParameters "ApiClient.PackageParameters")

Clone()[¶](#ApiClient.ParameterSetAnalysisPackage.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`ParameterSetAnalysisPackage`](#ApiClient.ParameterSetAnalysisPackage "ApiClient.ParameterSetAnalysisPackage")

GetName()[¶](#ApiClient.ParameterSetAnalysisPackage.GetName "Link to this definition")  
Returns the name of the project component.

Returns:  Name of the component

Return type:  str

GetPackage()[¶](#ApiClient.ParameterSetAnalysisPackage.GetPackage "Link to this definition")  
Returns the referenced package.

Returns:  The referenced package of type [`Package`](PackageApi.md#ApiClient.Package "ApiClient.Package") or the referenced analysis package of type [`AnalysisPackage`](PackageApi.md#ApiClient.AnalysisPackage "ApiClient.AnalysisPackage")

Return type:  [`PackageBase`](TraceAnalysisApi.md#ApiClient.PackageBase "ApiClient.PackageBase")

GetParent()[¶](#ApiClient.ParameterSetAnalysisPackage.GetParent "Link to this definition")  
Returns the parent project component.

Returns:  Parent component

Return type:  [`ProjectComponent`](#ApiClient.ProjectComponent "ApiClient.ProjectComponent")

GetPosition()[¶](#ApiClient.ParameterSetAnalysisPackage.GetPosition "Link to this definition")  
Returns the position in the parent project.

Returns:  parent position

Return type:  integer

GetTestCaseId()[¶](#ApiClient.ParameterSetAnalysisPackage.GetTestCaseId "Link to this definition")  
Returns the test case id of the parameter record.

Returns:  Test case id

Return type:  str

GetTestScriptId()[¶](#ApiClient.ParameterSetAnalysisPackage.GetTestScriptId "Link to this definition")  
Returns the test script id of the corresponding package.

Returns:  Test script id

Return type:  str

GetType()[¶](#ApiClient.ParameterSetAnalysisPackage.GetType "Link to this definition")  
Returns the type (class name) of the project component, e.g.  
- “ConfigChange”

- “ParameterSet”

- “PackageCall”

- “Project”

- “PackageGenerator”

Returns:  Type (class name) of the project component

Return type:  str

IsEnabled()[¶](#ApiClient.ParameterSetAnalysisPackage.IsEnabled "Link to this definition")  
Returns the state of the test step.

Returns:  True if test step is enabled, otherwise False

Return type:  bool

RemoveFromProject()[¶](#ApiClient.ParameterSetAnalysisPackage.RemoveFromProject "Link to this definition")  
Removes this component from the project.

Raises:  
**ApiError** – if the component is not part of any project

SetEnabled(*state=True*)[¶](#ApiClient.ParameterSetAnalysisPackage.SetEnabled "Link to this definition")  
Enable or disable the test step.

Parameters:  **state** (*bool*) – True (=Default) to enable, False to disable the test step.

SetName(*name*)[¶](#ApiClient.ParameterSetAnalysisPackage.SetName "Link to this definition")  
Sets the name of the project component.

Parameters:  **name** (*str*) – Name of the component

SetTestCaseId(*testCaseId*)[¶](#ApiClient.ParameterSetAnalysisPackage.SetTestCaseId "Link to this definition")  
Sets the independent test case id of the parameter record.

Parameters:  **testCaseId** (*str*) – Test case id

Returns:  True if the update was successful

Return type:  boolean

## GlobalConstants[¶](#globalconstants "Link to this heading")

*class* GlobalConstants[¶](#ApiClient.GlobalConstants "Link to this definition")  
Returned by

- [`ParameterSet.GlobalConstants`](ProjectApi.md#ApiClient.ParameterSet.GlobalConstants "ApiClient.ParameterSet.GlobalConstants")

- [`ParameterSetAnalysisPackage.GlobalConstants`](#ApiClient.ParameterSetAnalysisPackage.GlobalConstants "ApiClient.ParameterSetAnalysisPackage.GlobalConstants")

- [`ParameterSetBase.GlobalConstants`](#ApiClient.ParameterSetBase.GlobalConstants "ApiClient.ParameterSetBase.GlobalConstants")

- [`Project.GlobalConstants`](ProjectApi.md#ApiClient.Project.GlobalConstants "ApiClient.Project.GlobalConstants")

- [`ProjectFolder.GlobalConstants`](#ApiClient.ProjectFolder.GlobalConstants "ApiClient.ProjectFolder.GlobalConstants")

- [`TestConfiguration.GlobalConstants`](ConfigurationApi.md#ApiClient.TestConfiguration.GlobalConstants "ApiClient.TestConfiguration.GlobalConstants")

AppendReferencedFile(*filename*)[¶](#ApiClient.GlobalConstants.AppendReferencedFile "Link to this definition")  
Appends a global constants definition file at the end of the list of referenced global constants definition files.

Parameters:  **filename** (*str*) – Path to the global constants definition file. Absolute or relative to the current workspace directory.

ClearReferencedFiles()[¶](#ApiClient.GlobalConstants.ClearReferencedFiles "Link to this definition")  
Removes all referenced global constants definition files from the list.

Clone()[¶](#ApiClient.GlobalConstants.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`GlobalConstants`](#ApiClient.GlobalConstants "ApiClient.GlobalConstants")

GetGlobalConstantsDefinition()[¶](#ApiClient.GlobalConstants.GetGlobalConstantsDefinition "Link to this definition")  
Returns the container for defining global constants statically.

Returns:  Container for global constants

Return type:  [`GlobalConstantsDefinition`](ParameterApi.md#ApiClient.GlobalConstantsDefinition "ApiClient.GlobalConstantsDefinition")

GetReferencedFiles()[¶](#ApiClient.GlobalConstants.GetReferencedFiles "Link to this definition")  
Returns a list of all referenced global constants definition files. The list is ordered by priority, i.e. global constants from files in the beginning of the list overwrite constants from later files.

Returns:  List of all referenced global constants definition files (\*.gcd)

Return type:  list[str]

GetStaticConstantsPriority()[¶](#ApiClient.GlobalConstants.GetStaticConstantsPriority "Link to this definition")  
Returns the priority of statically defined constants with regard to the constants from referenced files.

Returns:  Priority value

Return type:  int

RemoveReferencedFile(*filename*)[¶](#ApiClient.GlobalConstants.RemoveReferencedFile "Link to this definition")  
Removes a global constants definition file from the list of referenced global constants definition files.

Parameters:  **filename** (*str*) – Path to the global constants definition file to be removed

Raises:  
**ApiError** – When the given file is not referenced in this test configuration

SetStaticConstantsPriority(*priority*)[¶](#ApiClient.GlobalConstants.SetStaticConstantsPriority "Link to this definition")  
Specifies the priority of the statically defined constants with regard to the constants from referenced files.

Note:  
If the given value is out of the valid range, it will be coerced to the closest reasonable value.

Parameters:  **priority** (*int*) –

Priority of the statically defined constants. Should be between

- 0: highest priority and

- length of referenced files list: lowest priority

## ParameterSetMapping[¶](#parametersetmapping "Link to this heading")

*class* ParameterSetMapping[¶](#ApiClient.ParameterSetMapping "Link to this definition")  
Returned by

- [`ParameterSet.Mapping`](ProjectApi.md#ApiClient.ParameterSet.Mapping "ApiClient.ParameterSet.Mapping")

- [`ParameterSetAnalysisPackage.Mapping`](#ApiClient.ParameterSetAnalysisPackage.Mapping "ApiClient.ParameterSetAnalysisPackage.Mapping")

- [`ParameterSetBase.Mapping`](#ApiClient.ParameterSetBase.Mapping "ApiClient.ParameterSetBase.Mapping")

Clone()[¶](#ApiClient.ParameterSetMapping.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`ParameterSetMapping`](#ApiClient.ParameterSetMapping "ApiClient.ParameterSetMapping")

CreateAlternativeMapping()[¶](#ApiClient.ParameterSetMapping.CreateAlternativeMapping "Link to this definition")  
Creates an empty mapping within the parameter set. If the parameter set already has an alternative mapping, it will be replaced.

Returns:  The mapping

Return type:  [`Mapping`](MappingApi.md#ApiClient.Mapping "ApiClient.Mapping")

GetAlternativeMapping()[¶](#ApiClient.ParameterSetMapping.GetAlternativeMapping "Link to this definition")  
Returns the alternative mapping of the parameter set or None if no the parameter set does not have an alternative mapping.

Returns:  The mapping

Return type:  [`Mapping`](MappingApi.md#ApiClient.Mapping "ApiClient.Mapping")

GetMappingFromPackage()[¶](#ApiClient.ParameterSetMapping.GetMappingFromPackage "Link to this definition")  
Returns the mapping of the package.

Returns:  Mapping to be set

Return type:  [`Mapping`](MappingApi.md#ApiClient.Mapping "ApiClient.Mapping")

HasAlternativeMapping()[¶](#ApiClient.ParameterSetMapping.HasAlternativeMapping "Link to this definition")  
Checks whether the parameter set has an alternative mapping.

Returns:  True if the parameter set has an alternative mapping.

Return type:  boolean

RemoveAlternativeMapping()[¶](#ApiClient.ParameterSetMapping.RemoveAlternativeMapping "Link to this definition")  
Removes the alternative mapping from the parameter set.

SetAlternativeMapping(*mapping*)[¶](#ApiClient.ParameterSetMapping.SetAlternativeMapping "Link to this definition")  
Sets the alternative mapping of the parameter set.

Parameters:  **mapping** ([`Mapping`](MappingApi.md#ApiClient.Mapping "ApiClient.Mapping")) – Mapping to be set

## MappingFiles[¶](#mappingfiles "Link to this heading")

*class* MappingFiles[¶](#ApiClient.MappingFiles "Link to this definition")  
Returned by

- [`ParameterSet.MappingFiles`](ProjectApi.md#ApiClient.ParameterSet.MappingFiles "ApiClient.ParameterSet.MappingFiles")

- [`ParameterSetAnalysisPackage.MappingFiles`](#ApiClient.ParameterSetAnalysisPackage.MappingFiles "ApiClient.ParameterSetAnalysisPackage.MappingFiles")

- [`ParameterSetBase.MappingFiles`](#ApiClient.ParameterSetBase.MappingFiles "ApiClient.ParameterSetBase.MappingFiles")

- [`Project.MappingFiles`](ProjectApi.md#ApiClient.Project.MappingFiles "ApiClient.Project.MappingFiles")

- [`ProjectFolder.MappingFiles`](#ApiClient.ProjectFolder.MappingFiles "ApiClient.ProjectFolder.MappingFiles")

Subclasses

- [`Common`](ConfigurationApi.md#ApiClient.Common "ApiClient.Common")

AddMappingArtifactReference(*mappingReference*)[¶](#ApiClient.MappingFiles.AddMappingArtifactReference "Link to this definition")  
Adds an artifact reference to a mapping file to the list.

Parameters:  **mappingReference** ([`ArtifactReference`](#ApiClient.ArtifactReference "ApiClient.ArtifactReference")) – Artifact reference to a mapping file

AddMappingFile(*filename*)[¶](#ApiClient.MappingFiles.AddMappingFile "Link to this definition")  
Adds a mapping file to the list.

Parameters:  **filename** (*str*) – Name of the mapping file

ClearMappingFiles()[¶](#ApiClient.MappingFiles.ClearMappingFiles "Link to this definition")  
Clears all entries from the mapping file list.

Clone()[¶](#ApiClient.MappingFiles.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`MappingFiles`](#ApiClient.MappingFiles "ApiClient.MappingFiles")

GetMappingArtifactReferences()[¶](#ApiClient.MappingFiles.GetMappingArtifactReferences "Link to this definition")  
Returns artifact references to mapping files.

Returns:  A list of all artifact references

Return type:  list[[`ArtifactReference`](#ApiClient.ArtifactReference "ApiClient.ArtifactReference")]

RemoveMappingArtifactReference(*mappingReference*)[¶](#ApiClient.MappingFiles.RemoveMappingArtifactReference "Link to this definition")  
Removes an artifact reference to a mapping file from the list.

Parameters:  **mappingReference** ([`ArtifactReference`](#ApiClient.ArtifactReference "ApiClient.ArtifactReference")) – Artifact reference to a mapping file

RemoveMappingFile(*index*)[¶](#ApiClient.MappingFiles.RemoveMappingFile "Link to this definition")  
Removes a mapping file from the list.

Parameters:  **index** (*int*) – The index of the mapping file to remove

GetMappingFiles()[¶](#ApiClient.MappingFiles.GetMappingFiles "Link to this definition")  
Returns the mapping file paths, relative to the workspace directory.

Returns:  A list of all mapping files

Return type:  list[str]

Deprecated since version 2024.2: Use [`GetMappingArtifactReferences()`](#ApiClient.MappingFiles.GetMappingArtifactReferences "ApiClient.MappingFiles.GetMappingArtifactReferences") instead

## ArtifactReference[¶](#artifactreference "Link to this heading")

*class* ArtifactReference[¶](#ApiClient.ArtifactReference "Link to this definition")  
Returned by

- [`Bus.GetDatabaseArtifactReference`](ConfigurationApi.md#ApiClient.Bus.GetDatabaseArtifactReference "ApiClient.Bus.GetDatabaseArtifactReference")

- [`Common.GetMappingArtifactReferences`](ConfigurationApi.md#ApiClient.Common.GetMappingArtifactReferences "ApiClient.Common.GetMappingArtifactReferences")

- [`ControlUnit.GetApplicationA2lArtifactReference`](ConfigurationApi.md#ApiClient.ControlUnit.GetApplicationA2lArtifactReference "ApiClient.ControlUnit.GetApplicationA2lArtifactReference")

- [`ControlUnit.GetApplicationHexArtifactReference`](ConfigurationApi.md#ApiClient.ControlUnit.GetApplicationHexArtifactReference "ApiClient.ControlUnit.GetApplicationHexArtifactReference")

- [`ControlUnit.GetDebuggingHexArtifactReference`](ConfigurationApi.md#ApiClient.ControlUnit.GetDebuggingHexArtifactReference "ApiClient.ControlUnit.GetDebuggingHexArtifactReference")

- [`MappingFiles.GetMappingArtifactReferences`](#ApiClient.MappingFiles.GetMappingArtifactReferences "ApiClient.MappingFiles.GetMappingArtifactReferences")

Subclasses

- [`LocalArtifactReference`](ArtifactApi.md#ApiClient.LocalArtifactReference "ApiClient.LocalArtifactReference")

- [`TestGuideArtifactReference`](ArtifactApi.md#ApiClient.TestGuideArtifactReference "ApiClient.TestGuideArtifactReference")

Clone()[¶](#ApiClient.ArtifactReference.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`ArtifactReference`](#ApiClient.ArtifactReference "ApiClient.ArtifactReference")

## PackageParameters[¶](#packageparameters "Link to this heading")

*class* PackageParameters[¶](#ApiClient.PackageParameters "Link to this definition")  
Returned by

- [`ParameterSet.Parameters`](ProjectApi.md#ApiClient.ParameterSet.Parameters "ApiClient.ParameterSet.Parameters")

- [`ParameterSetAnalysisPackage.Parameters`](#ApiClient.ParameterSetAnalysisPackage.Parameters "ApiClient.ParameterSetAnalysisPackage.Parameters")

- [`ParameterSetBase.Parameters`](#ApiClient.ParameterSetBase.Parameters "ApiClient.ParameterSetBase.Parameters")

- [`Project.PackageParameters`](ProjectApi.md#ApiClient.Project.PackageParameters "ApiClient.Project.PackageParameters")

- [`ProjectFolder.PackageParameters`](#ApiClient.ProjectFolder.PackageParameters "ApiClient.ProjectFolder.PackageParameters")

AppendReferencedFile(*filename*)[¶](#ApiClient.PackageParameters.AppendReferencedFile "Link to this definition")  
Appends a package parameters definition file at the end of the list of referenced package parameters definition files.

Parameters:  **filename** (*str*) – Path to the package parameters definition file. Absolute or relative to the current workspace directory.

ClearReferencedFiles()[¶](#ApiClient.PackageParameters.ClearReferencedFiles "Link to this definition")  
Removes all referenced package parameters definition files from the list.

Clone()[¶](#ApiClient.PackageParameters.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`PackageParameters`](#ApiClient.PackageParameters "ApiClient.PackageParameters")

GetPackageParametersDefinition()[¶](#ApiClient.PackageParameters.GetPackageParametersDefinition "Link to this definition")  
Returns the container for defining package parameters statically.

Returns:  Container for package parameters

Return type:  [`PackageParametersDefinition`](ParameterApi.md#ApiClient.PackageParametersDefinition "ApiClient.PackageParametersDefinition")

GetReferencedFiles()[¶](#ApiClient.PackageParameters.GetReferencedFiles "Link to this definition")  
Returns a list of all referenced package parameters definition files. The list is ordered by priority, i.e. package parameters from files in the beginning of the list overwrite parameters from later files.

Returns:  List of all referenced package parameters definition files (\*.ppd)

Return type:  list[str]

GetStaticParametersPriority()[¶](#ApiClient.PackageParameters.GetStaticParametersPriority "Link to this definition")  
Returns the priority of statically defined parameters with regard to the parameters from referenced files.

Returns:  Priority value

Return type:  int

RemoveReferencedFile(*filename*)[¶](#ApiClient.PackageParameters.RemoveReferencedFile "Link to this definition")  
Removes a package parameters definition file from the list of referenced package parameters definition files.

Parameters:  **filename** (*str*) – Path to the package parameters definition file to be removed. Absolute or relative to the current workspace directory.

Raises:  
**ApiError** – When the given file is not referenced in this parameter set

SetStaticParametersPriority(*priority*)[¶](#ApiClient.PackageParameters.SetStaticParametersPriority "Link to this definition")  
Specifies the priority of the statically defined parameters with regard to the parameters from referenced files.

Note:  
If the given value is out of the valid range, it will be coerced to the closest reasonable value.

Parameters:  **priority** (*int*) –

Priority of the statically defined parameters. Should be between

- 0: highest priority and

- length of referenced files list: lowest priority

## ParameterSetBase[¶](#parametersetbase "Link to this heading")

*class* ParameterSetBase[¶](#ApiClient.ParameterSetBase "Link to this definition")  
Base class

[`ProjectComponent`](#ApiClient.ProjectComponent "ApiClient.ProjectComponent")

Subclasses

- [`ParameterSet`](ProjectApi.md#ApiClient.ParameterSet "ApiClient.ParameterSet")

- [`ParameterSetAnalysisPackage`](#ApiClient.ParameterSetAnalysisPackage "ApiClient.ParameterSetAnalysisPackage")

Attributes[¶](#ApiClient.ParameterSetBase.Attributes "Link to this definition")  
Returns access to the package attributes definitions specified within the parameter set and the referenced package attribute definition files.

Returns:  Package attribute interface of the parameter set

Return type:  [`Attributes`](ProjectApi.md#ApiClient.Attributes "ApiClient.Attributes")

GlobalConstants[¶](#ApiClient.ParameterSetBase.GlobalConstants "Link to this definition")  
Returns access to the global constants definitions specified within the parameter set and the referenced global constants definition files.

Returns:  Global constants interface of the parameter set

Return type:  [`GlobalConstants`](#ApiClient.GlobalConstants "ApiClient.GlobalConstants")

Mapping[¶](#ApiClient.ParameterSetBase.Mapping "Link to this definition")  
Returns access to the mapping of the parameter set.

Returns:  Mapping interface of the parameter set

Return type:  [`ParameterSetMapping`](#ApiClient.ParameterSetMapping "ApiClient.ParameterSetMapping")

MappingFiles[¶](#ApiClient.ParameterSetBase.MappingFiles "Link to this definition")  
Returns access to the mapping file list of the parameter set.

Returns:  Mapping file list object of the parameter set

Return type:  [`MappingFiles`](#ApiClient.MappingFiles "ApiClient.MappingFiles")

Parameters[¶](#ApiClient.ParameterSetBase.Parameters "Link to this definition")  
Returns access to the package parameters definitions specified within the parameter set and the referenced package parameters definition files.

Returns:  Package parameters interface of the parameter set

Return type:  [`PackageParameters`](#ApiClient.PackageParameters "ApiClient.PackageParameters")

Clone()[¶](#ApiClient.ParameterSetBase.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`ParameterSetBase`](#ApiClient.ParameterSetBase "ApiClient.ParameterSetBase")

GetName()[¶](#ApiClient.ParameterSetBase.GetName "Link to this definition")  
Returns the name of the project component.

Returns:  Name of the component

Return type:  str

GetPackage()[¶](#ApiClient.ParameterSetBase.GetPackage "Link to this definition")  
Returns the referenced package.

Returns:  The referenced package of type [`Package`](PackageApi.md#ApiClient.Package "ApiClient.Package") or the referenced analysis package of type [`AnalysisPackage`](PackageApi.md#ApiClient.AnalysisPackage "ApiClient.AnalysisPackage")

Return type:  [`PackageBase`](TraceAnalysisApi.md#ApiClient.PackageBase "ApiClient.PackageBase")

GetParent()[¶](#ApiClient.ParameterSetBase.GetParent "Link to this definition")  
Returns the parent project component.

Returns:  Parent component

Return type:  [`ProjectComponent`](#ApiClient.ProjectComponent "ApiClient.ProjectComponent")

GetPosition()[¶](#ApiClient.ParameterSetBase.GetPosition "Link to this definition")  
Returns the position in the parent project.

Returns:  parent position

Return type:  integer

GetTestCaseId()[¶](#ApiClient.ParameterSetBase.GetTestCaseId "Link to this definition")  
Returns the test case id of the parameter record.

Returns:  Test case id

Return type:  str

GetTestScriptId()[¶](#ApiClient.ParameterSetBase.GetTestScriptId "Link to this definition")  
Returns the test script id of the corresponding package.

Returns:  Test script id

Return type:  str

GetType()[¶](#ApiClient.ParameterSetBase.GetType "Link to this definition")  
Returns the type (class name) of the project component, e.g.  
- “ConfigChange”

- “ParameterSet”

- “PackageCall”

- “Project”

- “PackageGenerator”

Returns:  Type (class name) of the project component

Return type:  str

IsEnabled()[¶](#ApiClient.ParameterSetBase.IsEnabled "Link to this definition")  
Returns the state of the test step.

Returns:  True if test step is enabled, otherwise False

Return type:  bool

RemoveFromProject()[¶](#ApiClient.ParameterSetBase.RemoveFromProject "Link to this definition")  
Removes this component from the project.

Raises:  
**ApiError** – if the component is not part of any project

SetEnabled(*state=True*)[¶](#ApiClient.ParameterSetBase.SetEnabled "Link to this definition")  
Enable or disable the test step.

Parameters:  **state** (*bool*) – True (=Default) to enable, False to disable the test step.

SetName(*name*)[¶](#ApiClient.ParameterSetBase.SetName "Link to this definition")  
Sets the name of the project component.

Parameters:  **name** (*str*) – Name of the component

SetTestCaseId(*testCaseId*)[¶](#ApiClient.ParameterSetBase.SetTestCaseId "Link to this definition")  
Sets the independent test case id of the parameter record.

Parameters:  **testCaseId** (*str*) – Test case id

Returns:  True if the update was successful

Return type:  boolean

## StimulationPackageCall[¶](#stimulationpackagecall "Link to this heading")

*class* StimulationPackageCall[¶](#ApiClient.StimulationPackageCall "Link to this definition")  
A stimulation package call (of a package) in a project.

Base class

[`ProjectComponent`](#ApiClient.ProjectComponent "ApiClient.ProjectComponent")

Returned by

- [`AnalysisPackageCall.GetStimulationPackageCall`](#ApiClient.AnalysisPackageCall.GetStimulationPackageCall "ApiClient.AnalysisPackageCall.GetStimulationPackageCall")

- [`AnalysisPackageCall.GetStimulationPackageCalls`](#ApiClient.AnalysisPackageCall.GetStimulationPackageCalls "ApiClient.AnalysisPackageCall.GetStimulationPackageCalls")

- [`AnalysisPackageMappingCall.GetStimulationPackageCall`](#ApiClient.AnalysisPackageMappingCall.GetStimulationPackageCall "ApiClient.AnalysisPackageMappingCall.GetStimulationPackageCall")

- [`AnalysisPackageMappingCall.GetStimulationPackageCalls`](#ApiClient.AnalysisPackageMappingCall.GetStimulationPackageCalls "ApiClient.AnalysisPackageMappingCall.GetStimulationPackageCalls")

- [`ComponentApi.CreateStimulationPackageCall`](#ApiClient.ComponentApi.CreateStimulationPackageCall "ApiClient.ComponentApi.CreateStimulationPackageCall")

- [`Project.GetStimulationPackageCalls`](ProjectApi.md#ApiClient.Project.GetStimulationPackageCalls "ApiClient.Project.GetStimulationPackageCalls")

ActivateAutomaticValueRestore()[¶](#ApiClient.StimulationPackageCall.ActivateAutomaticValueRestore "Link to this definition")  
Activates value restore of test quantities after the execution of every Package.

AddParameterGenerator(*name*, *generatorId*)[¶](#ApiClient.StimulationPackageCall.AddParameterGenerator "Link to this definition")  
Adds a parameter generator to the package call

Parameters:  - **name** (*str*) – Name of the parameter generator

- **generatorId** (*str*) – Unique generator id of generator to be added

Returns:  The parameter generator

Return type:  [`ParameterGenerator`](#ApiClient.ParameterGenerator "ApiClient.ParameterGenerator")

AddParameterSet(*name*, *position=None*)[¶](#ApiClient.StimulationPackageCall.AddParameterSet "Link to this definition")  
Adds a parameter set to the stimulation package call

Parameters:  - **name** (*str*) – Name of the parameter set

- **position** (*integer*) – Position to insert the parameter set inside the package call

Returns:  The parameter set

Return type:  [`ParameterSet`](ProjectApi.md#ApiClient.ParameterSet "ApiClient.ParameterSet")

AddParameterVariationGenerator(*name*)[¶](#ApiClient.StimulationPackageCall.AddParameterVariationGenerator "Link to this definition")  
Adds a parameter variation generator to the stimulation package call.

Parameters:  **name** (*str*) – Name of the parameter variation generator.

Returns:  The parameter variation generator.

Return type:  [`ParameterVariationGeneratorComponent`](#ApiClient.ParameterVariationGeneratorComponent "ApiClient.ParameterVariationGeneratorComponent")

Clone()[¶](#ApiClient.StimulationPackageCall.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`StimulationPackageCall`](#ApiClient.StimulationPackageCall "ApiClient.StimulationPackageCall")

CreateAnalysisPackageMappingCalls(*onlyMissing=False*)[¶](#ApiClient.StimulationPackageCall.CreateAnalysisPackageMappingCalls "Link to this definition")  
Creates an analysis package mapping call for each analysis requested in the stimulation package.

Parameters:  **onlyMissing** (*bool*) – If True, only analysis package mapping calls not yet added to the project are created.

Returns:  list of analysis package mapping calls

Return type:  list[[`AnalysisPackageMappingCall`](#ApiClient.AnalysisPackageMappingCall "ApiClient.AnalysisPackageMappingCall")]

Raises:  
**ApiError** – If called with onlyMissing=True, without adding the stimulation call to the project first.

DeactivateAutomaticValueRestore()[¶](#ApiClient.StimulationPackageCall.DeactivateAutomaticValueRestore "Link to this definition")  
Deactivate value restore of test quantities after the execution of every Package.

GetAbsolutePath()[¶](#ApiClient.StimulationPackageCall.GetAbsolutePath "Link to this definition")  
Returns the absolute path to referenced package.

Returns:  Absolute path to referenced package

Return type:  str

GetAnalysisBindings()[¶](#ApiClient.StimulationPackageCall.GetAnalysisBindings "Link to this definition")  
Returns the configured bindings between this stimulation package and the attached analysis packages.

Returns:  All signal group references

Return type:  [`AnalysisBindings`](#ApiClient.AnalysisBindings "ApiClient.AnalysisBindings")

GetAnalysisPackageCalls(*skipDisabled=True*, *noParameterSets=False*)[¶](#ApiClient.StimulationPackageCall.GetAnalysisPackageCalls "Link to this definition")  
Returns all analysis package calls of the project referencing this stimulation package call. Analysis package calls that reference “all previous stimulations” are included (if they are inserted behind the stimulation package call in the project).

Parameters:  - **skipDisabled** (*boolean*) – Defines whether disabled package calls should be excluded.

- **noParameterSets** (*boolean*) – Defines whether package calls with parameter sets should be excluded.

Returns:  Package calls

Return type:  list[[`AnalysisPackageCall`](#ApiClient.AnalysisPackageCall "ApiClient.AnalysisPackageCall")]

GetComponents()[¶](#ApiClient.StimulationPackageCall.GetComponents "Link to this definition")  
Returns all direct children of the package call.

Returns:  List with all children components

Return type:  list[[`ProjectComponent`](#ApiClient.ProjectComponent "ApiClient.ProjectComponent")]

GetCustomRetryCondition()[¶](#ApiClient.StimulationPackageCall.GetCustomRetryCondition "Link to this definition")  
Returns the condition of the custom retries. Returns one of the following:

- ‘ERROR’

- ‘FAILED’

- ‘ERROR/FAILED’

Returns:  The condition of the custom retry

Return type:  str

GetCustomRetryCount()[¶](#ApiClient.StimulationPackageCall.GetCustomRetryCount "Link to this definition")  
Returns the number of the retries defined on the project component.

Returns:  Number of the custom retries

Return type:  integer

GetErrorRecoveryPkgLevel()[¶](#ApiClient.StimulationPackageCall.GetErrorRecoveryPkgLevel "Link to this definition")  
Returns the conditions under which the error recovery package (configured via [`SetErrorRecoveryPkgPath()`](#ApiClient.StimulationPackageCall.SetErrorRecoveryPkgPath "ApiClient.StimulationPackageCall.SetErrorRecoveryPkgPath")) will be executed

This overrides settings from the parent element or from the test configuration.

Returns:  - -1 = disabled

- 0 = on abort only

- 1 = on ERROR and on abort

- 2 = on FAILED, ERROR and abort.

- None: use inherited setting from parent element or test configuration

Return type:  int

GetErrorRecoveryPkgPath()[¶](#ApiClient.StimulationPackageCall.GetErrorRecoveryPkgPath "Link to this definition")  
Returns the path of the error recovery Package to be executed upon abort of test execution or ERROR/FAILED, if this element has a custom setting which overrides inherited settings from the parent element or from the test configuration.

see also [`GetErrorRecoveryPkgLevel()`](#ApiClient.StimulationPackageCall.GetErrorRecoveryPkgLevel "ApiClient.StimulationPackageCall.GetErrorRecoveryPkgLevel")

Returns:  Absolute path to Package file; None if inherited or explicitly disabled

Return type:  str

GetName()[¶](#ApiClient.StimulationPackageCall.GetName "Link to this definition")  
Returns the name of the project component.

Returns:  Name of the component

Return type:  str

GetPackage()[¶](#ApiClient.StimulationPackageCall.GetPackage "Link to this definition")  
Returns the referenced stimulation package.

Returns:  referenced package

Return type:  [`Package`](PackageApi.md#ApiClient.Package "ApiClient.Package")

Raises:  
**ApiError** – If the referenced package file (\*.pkg) does not exist.

GetParameterGenerators(*skipDisabled=True*)[¶](#ApiClient.StimulationPackageCall.GetParameterGenerators "Link to this definition")  
Returns all parameter generators of the package call.

Parameters:  **skipDisabled** (*bool*) – Defines whether disabled components should be included.

Returns:  The parameter generators.

Return type:  list[[`ParameterGenerator`](#ApiClient.ParameterGenerator "ApiClient.ParameterGenerator")]

GetParameterSets(*skipDisabled=True*)[¶](#ApiClient.StimulationPackageCall.GetParameterSets "Link to this definition")  
Returns all parameter sets of the package call.

Parameters:  **skipDisabled** (*bool*) – Defines whether disabled components should be included.

Returns:  Parameter sets

Return type:  list[[`ParameterSet`](ProjectApi.md#ApiClient.ParameterSet "ApiClient.ParameterSet")]

GetParameterVariationGenerators(*skipDisabled=True*)[¶](#ApiClient.StimulationPackageCall.GetParameterVariationGenerators "Link to this definition")  
Returns all parameter variation generators of the stimulation package call.

Parameters:  **skipDisabled** (*bool*) – Defines whether disabled generators should be excluded.

Returns:  The parameter variation generators.

Return type:  list[[`ParameterVariationGeneratorComponent`](#ApiClient.ParameterVariationGeneratorComponent "ApiClient.ParameterVariationGeneratorComponent")]

GetParent()[¶](#ApiClient.StimulationPackageCall.GetParent "Link to this definition")  
Returns the parent project component.

Returns:  Parent component

Return type:  [`ProjectComponent`](#ApiClient.ProjectComponent "ApiClient.ProjectComponent")

GetPosition()[¶](#ApiClient.StimulationPackageCall.GetPosition "Link to this definition")  
Returns the position in the parent project.

Returns:  parent position

Return type:  integer

GetProjectRelativePath()[¶](#ApiClient.StimulationPackageCall.GetProjectRelativePath "Link to this definition")  
Returns the file project relative path of the referenced package.

The returned path is a relative path, its base is the folder where the calling project is located, just like the path is shown in the package test step’s dialog.

Returns:  File name with relative path of the package to be called.

Return type:  str

Raises:  
**ProjectNotSavedError** – If this method is called before project is saved.

GetRequestedAnalysisLabels()[¶](#ApiClient.StimulationPackageCall.GetRequestedAnalysisLabels "Link to this definition")  
Returns the trace analysis label that are requested by this package.

Returns:  The list for requested analysis labels.

Return type:  list[str]

GetTestCaseId()[¶](#ApiClient.StimulationPackageCall.GetTestCaseId "Link to this definition")  
Returns the test case id of the package test component.

Returns:  Test case id.

Return type:  str

GetTestScriptId()[¶](#ApiClient.StimulationPackageCall.GetTestScriptId "Link to this definition")  
Returns the test script id of the corresponding package will be returned.

Returns:  Test script id.

Return type:  str

GetType()[¶](#ApiClient.StimulationPackageCall.GetType "Link to this definition")  
Returns the type (class name) of the project component, e.g.  
- “ConfigChange”

- “ParameterSet”

- “PackageCall”

- “Project”

- “PackageGenerator”

Returns:  Type (class name) of the project component

Return type:  str

HasComponents()[¶](#ApiClient.StimulationPackageCall.HasComponents "Link to this definition")  
Returns whether the package call has children.

Returns:  True if there are children, False otherwise.

Return type:  bool

HasCustomErrorRecoveryPackageSettings()[¶](#ApiClient.StimulationPackageCall.HasCustomErrorRecoveryPackageSettings "Link to this definition")  
Returns whether the Package execution settings in case of test abort or ERROR/FAILED of the parent element are overridden

Returns:  True if this element has custom error recovery package settings that override the parent element’s settings or those from the test configuration

Return type:  boolean

HasCustomRestoreSettings()[¶](#ApiClient.StimulationPackageCall.HasCustomRestoreSettings "Link to this definition")  
Returns if the value restore settings of the parent element are used or overridden by custom settings

Returns:  True if custom settings used, False if parent settings used

Return type:  boolean

HasCustomRetrySettings()[¶](#ApiClient.StimulationPackageCall.HasCustomRetrySettings "Link to this definition")  
Returns if the retry settings of the parent element are used

Returns:  True if parent settings used, False if custom settings defined

Return type:  boolean

InsertParameterSet(*parameterSet*, *position=None*)[¶](#ApiClient.StimulationPackageCall.InsertParameterSet "Link to this definition")  
Adds a parameter set to the package call

Parameters:  - **parameterSet** ([`ParameterSet`](ProjectApi.md#ApiClient.ParameterSet "ApiClient.ParameterSet")) – parameter set

- **position** (*integer*) – Position to insert the parameter set inside the package call

IsAutomaticValueRestoreActivated()[¶](#ApiClient.StimulationPackageCall.IsAutomaticValueRestoreActivated "Link to this definition")  
Returns if the automatic value restore is activated

Returns:  True if activated, else False

Return type:  boolean

IsAutomaticValueRestoreDeactivated()[¶](#ApiClient.StimulationPackageCall.IsAutomaticValueRestoreDeactivated "Link to this definition")  
Returns if the automatic value restore is deactivated

Returns:  True if deactivated, else False

Return type:  boolean

IsEnabled()[¶](#ApiClient.StimulationPackageCall.IsEnabled "Link to this definition")  
Returns the state of the test step.

Returns:  True if test step is enabled, otherwise False

Return type:  bool

RemoveFromProject()[¶](#ApiClient.StimulationPackageCall.RemoveFromProject "Link to this definition")  
Removes this component from the project.

Raises:  
**ApiError** – if the component is not part of any project

RemoveParameterGenerator(*paramGenerator*)[¶](#ApiClient.StimulationPackageCall.RemoveParameterGenerator "Link to this definition")  
Removes a parameter generator from the package call.

Parameters:  **paramGenerator** ([`ParameterGenerator`](#ApiClient.ParameterGenerator "ApiClient.ParameterGenerator")) – The parameter generator to be removed

Raises:  
**ApiError** –

- If the given parameter generator is not part if the package call

- If paramGenerator ist not of type [`ParameterGenerator`](#ApiClient.ParameterGenerator "ApiClient.ParameterGenerator")

RemoveParameterSet(*paramSet*)[¶](#ApiClient.StimulationPackageCall.RemoveParameterSet "Link to this definition")  
Removes a parameter set from the stimulation package call.

Parameters:  **paramSet** ([`ParameterSet`](ProjectApi.md#ApiClient.ParameterSet "ApiClient.ParameterSet")) – The parameter set to be removed

Raises:  
**ApiError** –

- If the given parameter set is not part if the package call

- If paramGenerator ist not of type [`ParameterSet`](ProjectApi.md#ApiClient.ParameterSet "ApiClient.ParameterSet")

RemoveParameterVariationGenerator(*paramVariationGenerator*)[¶](#ApiClient.StimulationPackageCall.RemoveParameterVariationGenerator "Link to this definition")  
Removes a parameter variation generator from the stimulation package call.

Parameters:  **paramVariationGenerator** ([`ParameterVariationGeneratorComponent`](#ApiClient.ParameterVariationGeneratorComponent "ApiClient.ParameterVariationGeneratorComponent")) – The parameter variation generator to be removed.

Raises:  
**ApiError** –

- If the given parameter variation generator is not part of the package call

- If paramVariationGenerator is not of type [`ParameterVariationGeneratorComponent`](#ApiClient.ParameterVariationGeneratorComponent "ApiClient.ParameterVariationGeneratorComponent")

SetCustomRetryCondition(*condition*)[¶](#ApiClient.StimulationPackageCall.SetCustomRetryCondition "Link to this definition")  
Sets the condition of the custom retry. Must be one of the following:

- ‘ERROR’

- ‘FAILED’

- ‘ERROR/FAILED’

Parameters:  **condition** (*str*) – The condition of the custom retry

SetCustomRetryCount(*count*)[¶](#ApiClient.StimulationPackageCall.SetCustomRetryCount "Link to this definition")  
Sets the number of the retries for all Packages within the project component.

Parameters:  **count** (*integer*) – Number of the custom retries

SetEnabled(*state=True*)[¶](#ApiClient.StimulationPackageCall.SetEnabled "Link to this definition")  
Enable or disable the test step.

Parameters:  **state** (*bool*) – True (=Default) to enable, False to disable the test step.

SetErrorRecoveryPkgLevel(*level*)[¶](#ApiClient.StimulationPackageCall.SetErrorRecoveryPkgLevel "Link to this definition")  
Sets the conditions under which the error recovery package (configured via [`SetErrorRecoveryPkgPath()`](#ApiClient.StimulationPackageCall.SetErrorRecoveryPkgPath "ApiClient.StimulationPackageCall.SetErrorRecoveryPkgPath")) will be executed

This overrides settings from the parent element or from the test configuration.

Parameters:  **level** (*int*) –

- -1  
  disabled

- 0 on abort only

- 1 on ERROR and on abort

- 2 on FAILED, ERROR and abort.

SetErrorRecoveryPkgPath(*packagePath*)[¶](#ApiClient.StimulationPackageCall.SetErrorRecoveryPkgPath "Link to this definition")  
Sets the path for a Package to be executed upon abort of test execution or ERROR/FAILED.

This overrides settings from the parent element or from the test configuration.

See also [`SetErrorRecoveryPkgLevel()`](#ApiClient.StimulationPackageCall.SetErrorRecoveryPkgLevel "ApiClient.StimulationPackageCall.SetErrorRecoveryPkgLevel")

Parameters:  **packagePath** (*str*) – Absolute path to Package file

SetName(*name*)[¶](#ApiClient.StimulationPackageCall.SetName "Link to this definition")  
Sets the name of the project component.

Parameters:  **name** (*str*) – Name of the component

SetTestCaseId(*testCaseId*)[¶](#ApiClient.StimulationPackageCall.SetTestCaseId "Link to this definition")  
Sets the test case id of the current package test.

Parameters:  **testCaseId** (*str*) – Test case id

UseParentErrorRecoveryPackageSettings()[¶](#ApiClient.StimulationPackageCall.UseParentErrorRecoveryPackageSettings "Link to this definition")  
Sets that the Package execution settings in case of test abort or ERROR/FAILED of the parent element are used. Existing custom settings are deleted.

UseParentRetrySettings()[¶](#ApiClient.StimulationPackageCall.UseParentRetrySettings "Link to this definition")  
Sets that the retry settings of the parent element are used. Existing custom settings are deleted.

UseParentValueRestoreSettings()[¶](#ApiClient.StimulationPackageCall.UseParentValueRestoreSettings "Link to this definition")  
Sets that the settings whether to restore the value of test quantities after the execution of every Package of the parent element are used. Existing custom settings are deleted.

## ParameterVariationGeneratorComponent[¶](#parametervariationgeneratorcomponent "Link to this heading")

*class* ParameterVariationGeneratorComponent[¶](#ApiClient.ParameterVariationGeneratorComponent "Link to this definition")  
Base class

[`ProjectComponent`](#ApiClient.ProjectComponent "ApiClient.ProjectComponent")

Returned by

- [`AnalysisPackageCall.AddParameterVariationGenerator`](#ApiClient.AnalysisPackageCall.AddParameterVariationGenerator "ApiClient.AnalysisPackageCall.AddParameterVariationGenerator")

- [`AnalysisPackageCall.GetParameterVariationGenerators`](#ApiClient.AnalysisPackageCall.GetParameterVariationGenerators "ApiClient.AnalysisPackageCall.GetParameterVariationGenerators")

- [`AnalysisPackageMappingCall.AddParameterVariationGenerator`](#ApiClient.AnalysisPackageMappingCall.AddParameterVariationGenerator "ApiClient.AnalysisPackageMappingCall.AddParameterVariationGenerator")

- [`AnalysisPackageMappingCall.GetParameterVariationGenerators`](#ApiClient.AnalysisPackageMappingCall.GetParameterVariationGenerators "ApiClient.AnalysisPackageMappingCall.GetParameterVariationGenerators")

- [`PackageCall.AddParameterVariationGenerator`](#ApiClient.PackageCall.AddParameterVariationGenerator "ApiClient.PackageCall.AddParameterVariationGenerator")

- [`PackageCall.GetParameterVariationGenerators`](#ApiClient.PackageCall.GetParameterVariationGenerators "ApiClient.PackageCall.GetParameterVariationGenerators")

- [`Project.GetParameterVariationGenerators`](ProjectApi.md#ApiClient.Project.GetParameterVariationGenerators "ApiClient.Project.GetParameterVariationGenerators")

- [`StimulationPackageCall.AddParameterVariationGenerator`](#ApiClient.StimulationPackageCall.AddParameterVariationGenerator "ApiClient.StimulationPackageCall.AddParameterVariationGenerator")

- [`StimulationPackageCall.GetParameterVariationGenerators`](#ApiClient.StimulationPackageCall.GetParameterVariationGenerators "ApiClient.StimulationPackageCall.GetParameterVariationGenerators")

Clone()[¶](#ApiClient.ParameterVariationGeneratorComponent.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`ParameterVariationGeneratorComponent`](#ApiClient.ParameterVariationGeneratorComponent "ApiClient.ParameterVariationGeneratorComponent")

GetAlgorithm()[¶](#ApiClient.ParameterVariationGeneratorComponent.GetAlgorithm "Link to this definition")  
Returns the id of the algorithm to use. Id mapping: 0 - cartesian product, 1 - classification tree method, 2 - n-wise method

Returns:  id of the algorithm choice

Return type:  int

GetNWiseFactor()[¶](#ApiClient.ParameterVariationGeneratorComponent.GetNWiseFactor "Link to this definition")  
Returns the n-wise factor used within the n-wise algorithm.

Returns:  n wise factor

Return type:  int

GetName()[¶](#ApiClient.ParameterVariationGeneratorComponent.GetName "Link to this definition")  
Returns the name of the project component.

Returns:  Name of the component

Return type:  str

GetParameters()[¶](#ApiClient.ParameterVariationGeneratorComponent.GetParameters "Link to this definition")  
Returns all stored parameters of the parameter variation generator. Parameters are returned as an OrderedDict with parameter name as key and the parameter value and parameter type in a list. The parameter value is returned as a str Examples: parameter ‘a’ with value int 5 –\> {‘a’: [‘5’, ‘Numeric’]} parameter ‘b’ with string values ‘5’, ‘6’ –\> {‘b’: [‘“5”, “6”’, ‘String’]}

Returns:  OrderedDict mapping attributes names to values

Return type:  dict[str, list[str]]

GetParent()[¶](#ApiClient.ParameterVariationGeneratorComponent.GetParent "Link to this definition")  
Returns the parent project component.

Returns:  Parent component

Return type:  [`ProjectComponent`](#ApiClient.ProjectComponent "ApiClient.ProjectComponent")

GetPosition()[¶](#ApiClient.ParameterVariationGeneratorComponent.GetPosition "Link to this definition")  
Returns the position in the parent project.

Returns:  parent position

Return type:  integer

GetRandomVariationMethod()[¶](#ApiClient.ParameterVariationGeneratorComponent.GetRandomVariationMethod "Link to this definition")  
Returns the id of the random variation method to use. Id mapping: 0 - non-deterministic, 1 - deterministic

Returns:  id of the random variation method to use

Return type:  int

GetRandomVariationSeed()[¶](#ApiClient.ParameterVariationGeneratorComponent.GetRandomVariationSeed "Link to this definition")  
Returns the random number generator seed for the random variation.

Returns:  random variation seed

Return type:  str

GetType()[¶](#ApiClient.ParameterVariationGeneratorComponent.GetType "Link to this definition")  
Returns the type (class name) of the project component, e.g.  
- “ConfigChange”

- “ParameterSet”

- “PackageCall”

- “Project”

- “PackageGenerator”

Returns:  Type (class name) of the project component

Return type:  str

GetVariationLimit()[¶](#ApiClient.ParameterVariationGeneratorComponent.GetVariationLimit "Link to this definition")  
Returns the variation limit of the variation generator.

Returns:  variation limit

Return type:  int

IsEnabled()[¶](#ApiClient.ParameterVariationGeneratorComponent.IsEnabled "Link to this definition")  
Returns the state of the test step.

Returns:  True if test step is enabled, otherwise False

Return type:  bool

IsParameterSetNumbering()[¶](#ApiClient.ParameterVariationGeneratorComponent.IsParameterSetNumbering "Link to this definition")  
Returns the setting of the parameter set numbering.

Returns:  parameter set numbering

Return type:  bool

IsRandomVariation()[¶](#ApiClient.ParameterVariationGeneratorComponent.IsRandomVariation "Link to this definition")  
Returns the setting of the random variation.

Returns:  random variation setting

Return type:  bool

RemoveFromProject()[¶](#ApiClient.ParameterVariationGeneratorComponent.RemoveFromProject "Link to this definition")  
Removes this component from the project.

Raises:  
**ApiError** – if the component is not part of any project

SetAlgorithm(*algorithm*)[¶](#ApiClient.ParameterVariationGeneratorComponent.SetAlgorithm "Link to this definition")  
Sets the id of the algorithm to use. Id mapping: 0 - cartesian product, 1 - classification tree method, 2 - n-wise method

Parameters:  **algorithm** (*int*) – algorithm id

SetEnabled(*state=True*)[¶](#ApiClient.ParameterVariationGeneratorComponent.SetEnabled "Link to this definition")  
Enable or disable the test step.

Parameters:  **state** (*bool*) – True (=Default) to enable, False to disable the test step.

SetNWiseFactor(*nWiseFactor*)[¶](#ApiClient.ParameterVariationGeneratorComponent.SetNWiseFactor "Link to this definition")  
Sets the n-wise factor used within the n-wise algorithm.

Parameters:  **nWiseFactor** (*int*) – n wise factor

SetName(*name*)[¶](#ApiClient.ParameterVariationGeneratorComponent.SetName "Link to this definition")  
Sets the name of the project component.

Parameters:  **name** (*str*) – Name of the component

SetParameterSetNumbering(*parameterSetNumbering*)[¶](#ApiClient.ParameterVariationGeneratorComponent.SetParameterSetNumbering "Link to this definition")  
Sets the parameter set numbering.

Parameters:  **parameterSetNumbering** (*bool*) – parameter set numbering

SetParameters(*parameters*)[¶](#ApiClient.ParameterVariationGeneratorComponent.SetParameters "Link to this definition")  
Overwrites the existing attributes of the generator with the provided ones. Parameters are returned as an OrderedDict with parameter name as key and the parameter value and parameter type in a list. The parameter value is returned as a str Examples: parameter ‘a’ with value int 5 –\> {‘a’: [‘5’, ‘Numeric’]} parameter ‘b’ with string values ‘5’, ‘6’ –\> {‘b’: [‘“5”, “6”’, ‘String’]}

Parameters:  **parameters** (*dict[str,* *list[str]]*) – Dictionary mapping attribute names to tuple with value and value type

SetRandomVariation(*randomVariation*)[¶](#ApiClient.ParameterVariationGeneratorComponent.SetRandomVariation "Link to this definition")  
Activates or deactivates the random variation of the parameter variation generator.

Parameters:  **randomVariation** (*bool*) – random variation setting

SetRandomVariationMethod(*randomVariationMethod*)[¶](#ApiClient.ParameterVariationGeneratorComponent.SetRandomVariationMethod "Link to this definition")  
Sets the random variation method to use for random variation in the generator. Id mapping: 0 - non-deterministic, 1 - deterministic

Parameters:  **randomVariationMethod** (*int*) – id of the random variation method to use

SetRandomVariationSeed(*randomSeed*)[¶](#ApiClient.ParameterVariationGeneratorComponent.SetRandomVariationSeed "Link to this definition")  
Sets the random number generator seed for the random variation.

Parameters:  **randomSeed** (*str*) – seed for random number generator

SetVariationLimit(*limit*)[¶](#ApiClient.ParameterVariationGeneratorComponent.SetVariationLimit "Link to this definition")  
Sets the variation limit of the parameter variation generator.

Parameters:  **limit** (*int*) – variation limit

## AnalysisPackageMappingCall[¶](#analysispackagemappingcall "Link to this heading")

*class* AnalysisPackageMappingCall[¶](#ApiClient.AnalysisPackageMappingCall "Link to this definition")  
An analysis package mapping call in a project.

Base classes

- [`AnalysisPackageCall`](#ApiClient.AnalysisPackageCall "ApiClient.AnalysisPackageCall")

- [`ProjectComponent`](#ApiClient.ProjectComponent "ApiClient.ProjectComponent")

Returned by

- [`StimulationPackageCall.CreateAnalysisPackageMappingCalls`](#ApiClient.StimulationPackageCall.CreateAnalysisPackageMappingCalls "ApiClient.StimulationPackageCall.CreateAnalysisPackageMappingCalls")

AddParameterGenerator(*name*, *generatorId*)[¶](#ApiClient.AnalysisPackageMappingCall.AddParameterGenerator "Link to this definition")  
Adds a parameter generator to the package call.

Parameters:  - **name** (*str*) – Name of the parameter generator.

- **generatorId** (*str*) – Unique generator id of generator to be added.

Returns:  The parameter generator.

Return type:  [`ParameterGenerator`](#ApiClient.ParameterGenerator "ApiClient.ParameterGenerator")

AddParameterSet(*name*, *position=None*)[¶](#ApiClient.AnalysisPackageMappingCall.AddParameterSet "Link to this definition")  
Adds a parameter set to the analysis package call.

Please note, that only parameters, mappings, and test management settings of parameters sets are permitted for parameter sets of analysis package calls!

Parameters:  - **name** (*str*) – Name of the parameter set

- **position** (*integer*) – Position to insert the parameter set inside the analysis package call

Returns:  The parameter set

Return type:  [`ParameterSetAnalysisPackage`](#ApiClient.ParameterSetAnalysisPackage "ApiClient.ParameterSetAnalysisPackage")

AddParameterVariationGenerator(*name*)[¶](#ApiClient.AnalysisPackageMappingCall.AddParameterVariationGenerator "Link to this definition")  
Adds a parameter variation generator to the analysis package call.

Parameters:  **name** (*str*) – Name of the parameter variation generator.

Returns:  The parameter variation generator.

Return type:  [`ParameterVariationGeneratorComponent`](#ApiClient.ParameterVariationGeneratorComponent "ApiClient.ParameterVariationGeneratorComponent")

Clone()[¶](#ApiClient.AnalysisPackageMappingCall.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`AnalysisPackageMappingCall`](#ApiClient.AnalysisPackageMappingCall "ApiClient.AnalysisPackageMappingCall")

GetAbsolutePath()[¶](#ApiClient.AnalysisPackageMappingCall.GetAbsolutePath "Link to this definition")  
Returns the absolute path to referenced package or None if the mapping has not yet been resolved.

Returns:  Absolute path to referenced package

Return type:  str

GetAutoAssignParameters()[¶](#ApiClient.AnalysisPackageMappingCall.GetAutoAssignParameters "Link to this definition")  
Returns whether parameters without assigned value (via parameter set/general project parameterization) should automatically use an equally named return value of the stimulation package if one exists.

Returns:  True, if the auto assignment is enabled. Otherwise, False.

Return type:  bool

GetComponents()[¶](#ApiClient.AnalysisPackageMappingCall.GetComponents "Link to this definition")  
Returns all direct children of the package call.

Returns:  List with all children components

Return type:  list[[`ProjectComponent`](#ApiClient.ProjectComponent "ApiClient.ProjectComponent")]

GetImplementedAnalysisLabel()[¶](#ApiClient.AnalysisPackageMappingCall.GetImplementedAnalysisLabel "Link to this definition")  
Returns the label for the trace analysis implemented by this package.

Returns:  trace analysis label

Return type:  str

GetName()[¶](#ApiClient.AnalysisPackageMappingCall.GetName "Link to this definition")  
Returns the name of the project component.

Returns:  Name of the component

Return type:  str

GetPackage()[¶](#ApiClient.AnalysisPackageMappingCall.GetPackage "Link to this definition")  
Returns the referenced analysis package or None if the mapping has not yet been resolved.

Returns:  Referenced analysis package

Return type:  [`AnalysisPackage`](PackageApi.md#ApiClient.AnalysisPackage "ApiClient.AnalysisPackage")

Raises:  
**ApiError** – If the referenced package file (\*.ta) does not exist.

GetParameterGenerators(*skipDisabled=True*)[¶](#ApiClient.AnalysisPackageMappingCall.GetParameterGenerators "Link to this definition")  
Returns all parameter generators of the analysis package call.

Parameters:  **skipDisabled** (*bool*) – Defines whether disabled components should be included.

Returns:  The parameter generators.

Return type:  list[[`ParameterGenerator`](#ApiClient.ParameterGenerator "ApiClient.ParameterGenerator")]

GetParameterSets(*skipDisabled=True*)[¶](#ApiClient.AnalysisPackageMappingCall.GetParameterSets "Link to this definition")  
Returns all parameter sets of the analysis package call.

Parameters:  **skipDisabled** (*boolean*) – Defines whether disabled components should be included.

Returns:  Parameter sets

Return type:  list[[`ParameterSetAnalysisPackage`](#ApiClient.ParameterSetAnalysisPackage "ApiClient.ParameterSetAnalysisPackage")]

GetParameterVariationGenerators(*skipDisabled=True*)[¶](#ApiClient.AnalysisPackageMappingCall.GetParameterVariationGenerators "Link to this definition")  
Returns all parameter variation generators of the analysis package call.

Parameters:  **skipDisabled** (*bool*) – Defines whether disabled generators should be excluded.

Returns:  The parameter variation generators.

Return type:  list[[`ParameterVariationGeneratorComponent`](#ApiClient.ParameterVariationGeneratorComponent "ApiClient.ParameterVariationGeneratorComponent")]

GetParent()[¶](#ApiClient.AnalysisPackageMappingCall.GetParent "Link to this definition")  
Returns the parent project component.

Returns:  Parent component

Return type:  [`ProjectComponent`](#ApiClient.ProjectComponent "ApiClient.ProjectComponent")

GetPosition()[¶](#ApiClient.AnalysisPackageMappingCall.GetPosition "Link to this definition")  
Returns the position in the parent project.

Returns:  parent position

Return type:  integer

GetProjectRelativePath()[¶](#ApiClient.AnalysisPackageMappingCall.GetProjectRelativePath "Link to this definition")  
Returns the file project relative path of the referenced package.

The returned path is a relative path, its base is the folder where the calling project is located, just like the path is shown in the package test step’s dialog.

Returns:  File name with relative path of the package to be called.

Return type:  str

Raises:  
**ProjectNotSavedError** – If this method is called before project is saved.

GetStimulationPackageCall()[¶](#ApiClient.AnalysisPackageMappingCall.GetStimulationPackageCall "Link to this definition")  
Returns the stimulation package call connected to this analysis package.

This method will return None if the analysis package is run for all previous stimulations (see `SetRunForPreviousStimulations()`).

Returns:  Stimulation package call. Returns None if no stimulation package call is set or the referenced stimulation package call was not found in the project.

Return type:  [`StimulationPackageCall`](#ApiClient.StimulationPackageCall "ApiClient.StimulationPackageCall")

GetStimulationPackageCalls()[¶](#ApiClient.AnalysisPackageMappingCall.GetStimulationPackageCalls "Link to this definition")  
Returns a list containing all related stimulation package calls, i.e. either all previous stimulation package calls if the corresponding option is set or the explicitly connected stimulation package call. In the latter case, see also `GetStimulationPackageCall()`.

Returns:  list of related stimulation package calls

Return type:  list[[`StimulationPackageCall`](#ApiClient.StimulationPackageCall "ApiClient.StimulationPackageCall")]

GetTestCaseId()[¶](#ApiClient.AnalysisPackageMappingCall.GetTestCaseId "Link to this definition")  
Returns the test case id for the analysis package call.

Returns:  Test case id

Return type:  str

GetTestScriptId()[¶](#ApiClient.AnalysisPackageMappingCall.GetTestScriptId "Link to this definition")  
Returns the test script id of the corresponding analysis package.

Returns:  Test script id

Return type:  str

GetType()[¶](#ApiClient.AnalysisPackageMappingCall.GetType "Link to this definition")  
Returns the type (class name) of the project component, e.g.  
- “ConfigChange”

- “ParameterSet”

- “PackageCall”

- “Project”

- “PackageGenerator”

Returns:  Type (class name) of the project component

Return type:  str

HasComponents()[¶](#ApiClient.AnalysisPackageMappingCall.HasComponents "Link to this definition")  
Returns whether the package call has children.

Returns:  True if there are children, False otherwise.

Return type:  boolean

InsertParameterSet(*parameterSet*, *position=None*)[¶](#ApiClient.AnalysisPackageMappingCall.InsertParameterSet "Link to this definition")  
Adds a parameter set to the analysis package call.

Please note, that only parameters and test management settings of parameters sets are permitted for parameter sets of analysis package calls!

Parameters:  - **parameterSet** ([`ParameterSetAnalysisPackage`](#ApiClient.ParameterSetAnalysisPackage "ApiClient.ParameterSetAnalysisPackage")) – parameter set

- **position** (*integer*) – Position to insert the parameter set inside the analysis package call

IsEnabled()[¶](#ApiClient.AnalysisPackageMappingCall.IsEnabled "Link to this definition")  
Returns the state of the test step.

Returns:  True if test step is enabled, otherwise False

Return type:  bool

IsRunForPreviousStimulations()[¶](#ApiClient.AnalysisPackageMappingCall.IsRunForPreviousStimulations "Link to this definition")  
Returns whether the analysis package call is run for all previous stimulation package calls.

Returns:  True, if run for all stimulations. Otherwise, False.

Return type:  bool

RemoveFromProject()[¶](#ApiClient.AnalysisPackageMappingCall.RemoveFromProject "Link to this definition")  
Removes this component from the project.

Raises:  
**ApiError** – if the component is not part of any project

RemoveParameterGenerator(*paramGenerator*)[¶](#ApiClient.AnalysisPackageMappingCall.RemoveParameterGenerator "Link to this definition")  
Removes a parameter generator from the package call.

Parameters:  **paramGenerator** ([`ParameterGenerator`](#ApiClient.ParameterGenerator "ApiClient.ParameterGenerator")) – The parameter generator to be removed.

Raises:  
**ApiError** –

- If the given parameter generator is not part of the package call

- If paramGenerator is not of type [`ParameterGenerator`](#ApiClient.ParameterGenerator "ApiClient.ParameterGenerator")

RemoveParameterSet(*paramSet*)[¶](#ApiClient.AnalysisPackageMappingCall.RemoveParameterSet "Link to this definition")  
Removes a parameter set from the analysis package call.

Parameters:  **paramSet** ([`ParameterSetAnalysisPackage`](#ApiClient.ParameterSetAnalysisPackage "ApiClient.ParameterSetAnalysisPackage")) – The parameter set to be removed

Raises:  
**ApiError** –

- If the given parameter set is not part of the package call

- If paramGenerator is not of type [`ParameterSetAnalysisPackage`](#ApiClient.ParameterSetAnalysisPackage "ApiClient.ParameterSetAnalysisPackage")

RemoveParameterVariationGenerator(*paramVariationGenerator*)[¶](#ApiClient.AnalysisPackageMappingCall.RemoveParameterVariationGenerator "Link to this definition")  
Removes a parameter variation generator from the analysis package call.

Parameters:  **paramVariationGenerator** ([`ParameterVariationGeneratorComponent`](#ApiClient.ParameterVariationGeneratorComponent "ApiClient.ParameterVariationGeneratorComponent")) – The parameter variation generator to be removed.

Raises:  
**ApiError** –

- If the given parameter variation generator is not part of the package call

- If paramVariationGenerator is not of type [`ParameterVariationGeneratorComponent`](#ApiClient.ParameterVariationGeneratorComponent "ApiClient.ParameterVariationGeneratorComponent")

SetAutoAssignParameters(*value*)[¶](#ApiClient.AnalysisPackageMappingCall.SetAutoAssignParameters "Link to this definition")  
Sets whether parameters without assigned value (via parameter set/general project parameterization) should automatically use an equally named return value of the stimulation package if one exists.

Parameters:  **value** (*bool*) – True, to enable the auto assignment. Otherwise, False.

SetEnabled(*state=True*)[¶](#ApiClient.AnalysisPackageMappingCall.SetEnabled "Link to this definition")  
Enable or disable the test step.

Parameters:  **state** (*bool*) – True (=Default) to enable, False to disable the test step.

SetImplementedAnalysisLabel(*label*)[¶](#ApiClient.AnalysisPackageMappingCall.SetImplementedAnalysisLabel "Link to this definition")  
Sets the label for the trace analysis implemented by this package.

The label cannot be set for analysis packages that are run for all previous stimulations (see `SetRunForPreviousStimulations()`).

Parameters:  **label** (*str*) – trace analysis label

SetName(*name*)[¶](#ApiClient.AnalysisPackageMappingCall.SetName "Link to this definition")  
Sets the name of the project component.

Parameters:  **name** (*str*) – Name of the component

SetStimulationPackageCall(*stimulationPackage*)[¶](#ApiClient.AnalysisPackageMappingCall.SetStimulationPackageCall "Link to this definition")  
Connects the given stimulation package call with this analysis package.

Parameters:  **stimulationPackage** ([`StimulationPackageCall`](#ApiClient.StimulationPackageCall "ApiClient.StimulationPackageCall")) – Stimulation package

SetTestCaseId(*testCaseId*)[¶](#ApiClient.AnalysisPackageMappingCall.SetTestCaseId "Link to this definition")  
Sets the test case id for the analysis package call.

Parameters:  **testCaseId** (*str*) – Test case id

## AnalysisBindings[¶](#analysisbindings "Link to this heading")

*class* AnalysisBindings[¶](#ApiClient.AnalysisBindings "Link to this definition")  
The configured bindings between a stimulation package and its attached analysis packages.

Returned by

- [`StimulationPackageCall.GetAnalysisBindings`](#ApiClient.StimulationPackageCall.GetAnalysisBindings "ApiClient.StimulationPackageCall.GetAnalysisBindings")

AddSignalGroupReference(*signalGroupName*)[¶](#ApiClient.AnalysisBindings.AddSignalGroupReference "Link to this definition")  
Adds a signal group reference.

Note: It is only necessary to add signal group references and manually assign a signal if the signal cannot be assigned automatically (e.g. signals of type trace file).

Parameters:  **signalGroupName** (*str*) – Name of the signal group to be referenced.

Clone()[¶](#ApiClient.AnalysisBindings.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`AnalysisBindings`](#ApiClient.AnalysisBindings "ApiClient.AnalysisBindings")

GetAvailableSignalGroupNames()[¶](#ApiClient.AnalysisBindings.GetAvailableSignalGroupNames "Link to this definition")  
Returns all available signal group names of the stimulation package step that can be referenced. The returned list includes the names of regular signal groups, the testcase variable group (if active) and generated signal groups from event stores in trace analyses.

Returns:  The list of available signal group names that can be referenced.

Return type:  list[str]

GetSignalGroupReference(*signalGroupName*)[¶](#ApiClient.AnalysisBindings.GetSignalGroupReference "Link to this definition")  
Returns the reference to the given signal group.

Parameters:  **signalGroupName** (*str*) – Name of the desired signal group reference.

Returns:  Desired signal group reference.

Return type:  [`SignalGroupReference`](#ApiClient.SignalGroupReference "ApiClient.SignalGroupReference")

GetSignalGroupReferences()[¶](#ApiClient.AnalysisBindings.GetSignalGroupReferences "Link to this definition")  
Returns all signal group references of the analysis binding.

Returns:  Signal group references

Return type:  list[[`SignalGroupReference`](#ApiClient.SignalGroupReference "ApiClient.SignalGroupReference")]

## SignalGroupReference[¶](#signalgroupreference "Link to this heading")

*class* SignalGroupReference[¶](#ApiClient.SignalGroupReference "Link to this definition")  
A signal group reference of the [`AnalysisBindings`](#ApiClient.AnalysisBindings "ApiClient.AnalysisBindings") between a stimulation package and its attached analysis packages containing manually assigned signals.

Returned by

- [`AnalysisBindings.GetSignalGroupReference`](#ApiClient.AnalysisBindings.GetSignalGroupReference "ApiClient.AnalysisBindings.GetSignalGroupReference")

- [`AnalysisBindings.GetSignalGroupReferences`](#ApiClient.AnalysisBindings.GetSignalGroupReferences "ApiClient.AnalysisBindings.GetSignalGroupReferences")

AppendSignal(*mappingItem*)[¶](#ApiClient.SignalGroupReference.AppendSignal "Link to this definition")  
Assigns a signal to the signal group. The signal is defined by the given mapping item. Its name and target variable are adopted.

Mapping items can be created using the [`MappingApi`](MappingApi.md#ApiClient.MappingApi "ApiClient.MappingApi").

Parameters:  **mappingItem** ([`MappingItem`](MappingApi.md#ApiClient.MappingItem "ApiClient.MappingItem")) – The mapping item whose information is used to create and append the manually assigned signal.

AppendTraceFileSignal(*referenceName*, *targetPath*)[¶](#ApiClient.SignalGroupReference.AppendTraceFileSignal "Link to this definition")  
Convenience method that works like [`AppendSignal()`](#ApiClient.SignalGroupReference.AppendSignal "ApiClient.SignalGroupReference.AppendSignal") without the necessity to create a mapping item first. Instead, referenceName and targetPath are passed directly to address a trace file signal.

Parameters:  - **referenceName** (*str*) – Name of the mapping item

- **targetPath** (*str*) – Path to the trace file signal to be accessed

Clear()[¶](#ApiClient.SignalGroupReference.Clear "Link to this definition")  
Removes all manually assigned signals from this signal group reference.

Clone()[¶](#ApiClient.SignalGroupReference.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`SignalGroupReference`](#ApiClient.SignalGroupReference "ApiClient.SignalGroupReference")

GetName()[¶](#ApiClient.SignalGroupReference.GetName "Link to this definition")  
Returns the name of the given signal group.

Returns:  Signal group name.

Return type:  str

GetSignals()[¶](#ApiClient.SignalGroupReference.GetSignals "Link to this definition")  
Returns all signals manually assigned to the given signal group reference.

Returns:  List of signals manually assigned to signal group reference.

Return type:  list[[`AssignedSignal`](#ApiClient.AssignedSignal "ApiClient.AssignedSignal")]

## AssignedSignal[¶](#assignedsignal "Link to this heading")

*class* AssignedSignal[¶](#ApiClient.AssignedSignal "Link to this definition")  
A signal assigned to a signal group reference.

Returned by

- [`SignalGroupReference.GetSignals`](#ApiClient.SignalGroupReference.GetSignals "ApiClient.SignalGroupReference.GetSignals")

Clone()[¶](#ApiClient.AssignedSignal.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`AssignedSignal`](#ApiClient.AssignedSignal "ApiClient.AssignedSignal")

GetAccessType()[¶](#ApiClient.AssignedSignal.GetAccessType "Link to this definition")  
Returns a string identifying the mapping item’s type. (such as MODEL, BUS, MEASUREMENT, …)

Returns:  access type

Return type:  str

GetDisplayedType()[¶](#ApiClient.AssignedSignal.GetDisplayedType "Link to this definition")  
Returns a “nice” representation of the type as displayed in the “type” column of the mapping panel

Returns:  the displayed mapping type

Return type:  str

GetReferenceName()[¶](#ApiClient.AssignedSignal.GetReferenceName "Link to this definition")  
Returns the reference name of mapping corresponding to the assigned signal.

Returns:  The reference name of the mapping

Return type:  str

GetSystemIdentifier()[¶](#ApiClient.AssignedSignal.GetSystemIdentifier "Link to this definition")  
Returns the system identifier providing the currently mapped test quantity

Returns:  system identifier

Return type:  str

GetTargetPath()[¶](#ApiClient.AssignedSignal.GetTargetPath "Link to this definition")  
Returns the path this mapping item is currently pointing at

Returns:  complete path to the destination test quantity

Return type:  str

GetVariableType()[¶](#ApiClient.AssignedSignal.GetVariableType "Link to this definition")  
Returns the type of the target variable or None if target has no type.

Returns:  The type of the target variable. (e.g. VALUE, MATRIX, CURVE, …)

Return type:  str

## ConfigChange[¶](#configchange "Link to this heading")

*class* ConfigChange[¶](#ApiClient.ConfigChange "Link to this definition")  
Base class

[`ProjectComponent`](#ApiClient.ProjectComponent "ApiClient.ProjectComponent")

Returned by

- [`ComponentApi.CreateConfigChange`](#ApiClient.ComponentApi.CreateConfigChange "ApiClient.ComponentApi.CreateConfigChange")

- [`Project.GetConfigChanges`](ProjectApi.md#ApiClient.Project.GetConfigChanges "ApiClient.Project.GetConfigChanges")

ACTION_TYPE_RESTART[¶](#ApiClient.ConfigChange.ACTION_TYPE_RESTART "Link to this definition")  
Returns the constant used to specify the action type ‘RESTART’.

Returns:  The constant

Return type:  str

ACTION_TYPE_START[¶](#ApiClient.ConfigChange.ACTION_TYPE_START "Link to this definition")  
Returns the constant used to specify the action type ‘START’.

Returns:  The constant

Return type:  str

ACTION_TYPE_STOP[¶](#ApiClient.ConfigChange.ACTION_TYPE_STOP "Link to this definition")  
Returns the constant used to specify the action type ‘STOP’.

Returns:  The constant

Return type:  str

Clone()[¶](#ApiClient.ConfigChange.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`ConfigChange`](#ApiClient.ConfigChange "ApiClient.ConfigChange")

GetActionType()[¶](#ApiClient.ConfigChange.GetActionType "Link to this definition")  
Returns the configuration change action type.

Returns:  The configuration change action type. Possible values are: \* [`ConfigChange.ACTION_TYPE_START`](#ApiClient.ConfigChange.ACTION_TYPE_START "ApiClient.ConfigChange.ACTION_TYPE_START") \* [`ConfigChange.ACTION_TYPE_RESTART`](#ApiClient.ConfigChange.ACTION_TYPE_RESTART "ApiClient.ConfigChange.ACTION_TYPE_RESTART") \* [`ConfigChange.ACTION_TYPE_STOP`](#ApiClient.ConfigChange.ACTION_TYPE_STOP "ApiClient.ConfigChange.ACTION_TYPE_STOP")

Return type:  str

GetKeepTbc()[¶](#ApiClient.ConfigChange.GetKeepTbc "Link to this definition")  
Returns True if the TBC selection keeps unchanged.

Returns:  True if the TBC selection keeps unchanged, else False.

Return type:  bool

GetKeepTcf()[¶](#ApiClient.ConfigChange.GetKeepTcf "Link to this definition")  
Returns True if the TCF selection keeps unchanged.

Returns:  True if the TCF selection keeps unchanged, else False.

Return type:  bool

GetName()[¶](#ApiClient.ConfigChange.GetName "Link to this definition")  
Returns the name of the project component.

Returns:  Name of the component

Return type:  str

GetParent()[¶](#ApiClient.ConfigChange.GetParent "Link to this definition")  
Returns the parent project component.

Returns:  Parent component

Return type:  [`ProjectComponent`](#ApiClient.ProjectComponent "ApiClient.ProjectComponent")

GetPosition()[¶](#ApiClient.ConfigChange.GetPosition "Link to this definition")  
Returns the position in the parent project.

Returns:  parent position

Return type:  integer

GetTestConfigurationPath()[¶](#ApiClient.ConfigChange.GetTestConfigurationPath "Link to this definition")  
Returns the path to the test configuration file, absolute or relative to the ‘Configuration’ directory.

Returns:  Path to the test configuration

Return type:  str

GetTestbenchConfigurationPath()[¶](#ApiClient.ConfigChange.GetTestbenchConfigurationPath "Link to this definition")  
Returns the path to the test bench configuration file, absolute or relative to the ‘Configuration’ directory.

Returns:  Path to the test bench configuration

Return type:  str

GetToolAction(*toolAlias*)[¶](#ApiClient.ConfigChange.GetToolAction "Link to this definition")  
Returns the action of the specified tool if it is different from ‘AUTO’ else None.

Parameters:  **toolAlias** (*str*) – Alias of the tool

Returns:  Action of the specified tool

Return type:  str

GetTools()[¶](#ApiClient.ConfigChange.GetTools "Link to this definition")  
Returns a list of the configured tools. If the test bench configuration file can not be determined or does not exist, only tools with an action different from ‘AUTO’ will be returned.

Returns:  Configured tools

Return type:  list[str]

GetType()[¶](#ApiClient.ConfigChange.GetType "Link to this definition")  
Returns the type (class name) of the project component, e.g.  
- “ConfigChange”

- “ParameterSet”

- “PackageCall”

- “Project”

- “PackageGenerator”

Returns:  Type (class name) of the project component

Return type:  str

IsEnabled()[¶](#ApiClient.ConfigChange.IsEnabled "Link to this definition")  
Returns the state of the test step.

Returns:  True if test step is enabled, otherwise False

Return type:  bool

RemoveFromProject()[¶](#ApiClient.ConfigChange.RemoveFromProject "Link to this definition")  
Removes this component from the project.

Raises:  
**ApiError** – if the component is not part of any project

SetActionType(*actionType*)[¶](#ApiClient.ConfigChange.SetActionType "Link to this definition")  
Sets the configuration change action type.

Parameters:  **actionType** (*str*) – The configuration change action type. Valid values are: \* [`ConfigChange.ACTION_TYPE_START`](#ApiClient.ConfigChange.ACTION_TYPE_START "ApiClient.ConfigChange.ACTION_TYPE_START") \* [`ConfigChange.ACTION_TYPE_RESTART`](#ApiClient.ConfigChange.ACTION_TYPE_RESTART "ApiClient.ConfigChange.ACTION_TYPE_RESTART") \* [`ConfigChange.ACTION_TYPE_STOP`](#ApiClient.ConfigChange.ACTION_TYPE_STOP "ApiClient.ConfigChange.ACTION_TYPE_STOP")

SetEnabled(*state=True*)[¶](#ApiClient.ConfigChange.SetEnabled "Link to this definition")  
Enable or disable the test step.

Parameters:  **state** (*bool*) – True (=Default) to enable, False to disable the test step.

SetKeepTbc(*keepTbc*)[¶](#ApiClient.ConfigChange.SetKeepTbc "Link to this definition")  
Defines if the TBC keeps unchanged.

Parameters:  **keepTbc** (*bool*) – True to keep the TBC unchanged. False to apply the given TBC path, see [`SetTestbenchConfigurationPath()`](#ApiClient.ConfigChange.SetTestbenchConfigurationPath "ApiClient.ConfigChange.SetTestbenchConfigurationPath"). False and no given TBC path will deselect the current TBC.

SetKeepTcf(*keepTcf*)[¶](#ApiClient.ConfigChange.SetKeepTcf "Link to this definition")  
Defines if the TCF keeps unchanged.

Parameters:  **keepTcf** (*bool*) – True to keep the TCF unchanged. False to apply the given TCF path, see [`SetTestConfigurationPath()`](#ApiClient.ConfigChange.SetTestConfigurationPath "ApiClient.ConfigChange.SetTestConfigurationPath"). False and no given TCF path will deselect the current TCF.

SetName(*name*)[¶](#ApiClient.ConfigChange.SetName "Link to this definition")  
Sets the name of the project component.

Parameters:  **name** (*str*) – Name of the component

SetTestConfigurationPath(*testConfiguration*)[¶](#ApiClient.ConfigChange.SetTestConfigurationPath "Link to this definition")  
Sets the path to the test configuration file, absolute or relative to the ‘Configuration’ directory.

Parameters:  **testConfiguration** (*str*) – Path to the test configuration file

SetTestbenchConfigurationPath(*testbenchConfiguration*)[¶](#ApiClient.ConfigChange.SetTestbenchConfigurationPath "Link to this definition")  
Sets the path to the test bench configuration file, absolute or relative to the ‘Configuration’ directory.

Parameters:  **testbenchConfiguration** (*str*) – Path to the test bench configuration file

SetToolAction(*toolAlias*, *action*)[¶](#ApiClient.ConfigChange.SetToolAction "Link to this definition")  
Sets the action of the specified tool. Has to be one of the following:

> - ‘AUTO’: Automatic (removes tool from component as ‘AUTO’ is the default value)
>
> - ‘RE_START’: Start if stopped, restart if started
>
> - ‘START’: Start if stopped, leave as is if started
>
> - ‘STOP’: Stop if started, leave as is if stopped
>
> - ‘NONE’: Leave as is

Parameters:  - **toolAlias** (*str*) – Alias of the tool

- **action** (*str*) – The action to set the tool to

Raises:  
**ApiError** – When the specified action is not supported.

## PackageCall[¶](#packagecall "Link to this heading")

*class* PackageCall[¶](#ApiClient.PackageCall "Link to this definition")  
Base class

[`ProjectComponent`](#ApiClient.ProjectComponent "ApiClient.ProjectComponent")

Returned by

- [`ComponentApi.CreatePackageCall`](#ApiClient.ComponentApi.CreatePackageCall "ApiClient.ComponentApi.CreatePackageCall")

- [`Project.GetPackageCalls`](ProjectApi.md#ApiClient.Project.GetPackageCalls "ApiClient.Project.GetPackageCalls")

ActivateAutomaticValueRestore()[¶](#ApiClient.PackageCall.ActivateAutomaticValueRestore "Link to this definition")  
Activates value restore of test quantities after the execution of every Package.

AddParameterGenerator(*name*, *generatorId*)[¶](#ApiClient.PackageCall.AddParameterGenerator "Link to this definition")  
Adds a parameter generator to the package call.

Parameters:  - **name** (*str*) – Name of the parameter generator

- **generatorId** (*str*) – Unique generator id of generator to be added

Returns:  The parameter generator

Return type:  [`ParameterGenerator`](#ApiClient.ParameterGenerator "ApiClient.ParameterGenerator")

AddParameterSet(*name*, *position=None*)[¶](#ApiClient.PackageCall.AddParameterSet "Link to this definition")  
Adds a parameter set to the package call.

Parameters:  - **name** (*str*) – Name of the parameter set

- **position** (*integer*) – Position to insert the parameter set inside the package call

Returns:  The parameter set

Return type:  [`ParameterSet`](ProjectApi.md#ApiClient.ParameterSet "ApiClient.ParameterSet")

AddParameterVariationGenerator(*name*)[¶](#ApiClient.PackageCall.AddParameterVariationGenerator "Link to this definition")  
Adds a parameter variation generator to the package call.

Parameters:  **name** (*str*) – Name of the parameter generator

Returns:  The parameter variation generator

Return type:  [`ParameterVariationGeneratorComponent`](#ApiClient.ParameterVariationGeneratorComponent "ApiClient.ParameterVariationGeneratorComponent")

Clone()[¶](#ApiClient.PackageCall.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`PackageCall`](#ApiClient.PackageCall "ApiClient.PackageCall")

DeactivateAutomaticValueRestore()[¶](#ApiClient.PackageCall.DeactivateAutomaticValueRestore "Link to this definition")  
Deactivate value restore of test quantities after the execution of every Package.

GetAbsolutePath()[¶](#ApiClient.PackageCall.GetAbsolutePath "Link to this definition")  
Returns the absolute path to referenced package.

Returns:  Absolute path to referenced package

Return type:  str

GetComponents()[¶](#ApiClient.PackageCall.GetComponents "Link to this definition")  
Returns all direct children of the package call.

Returns:  List with all children components

Return type:  list[[`ProjectComponent`](#ApiClient.ProjectComponent "ApiClient.ProjectComponent")]

GetCustomRetryCondition()[¶](#ApiClient.PackageCall.GetCustomRetryCondition "Link to this definition")  
Returns the condition of the custom retries. Returns one of the following:

- ‘ERROR’

- ‘FAILED’

- ‘ERROR/FAILED’

Returns:  The condition of the custom retry

Return type:  str

GetCustomRetryCount()[¶](#ApiClient.PackageCall.GetCustomRetryCount "Link to this definition")  
Returns the number of the retries defined on the project component.

Returns:  Number of the custom retries

Return type:  integer

GetErrorRecoveryPkgLevel()[¶](#ApiClient.PackageCall.GetErrorRecoveryPkgLevel "Link to this definition")  
Returns the conditions under which the error recovery package (configured via [`SetErrorRecoveryPkgPath()`](#ApiClient.PackageCall.SetErrorRecoveryPkgPath "ApiClient.PackageCall.SetErrorRecoveryPkgPath")) will be executed

This overrides settings from the parent element or from the test configuration.

Returns:  - -1 = disabled

- 0 = on abort only

- 1 = on ERROR and on abort

- 2 = on FAILED, ERROR and abort.

- None: use inherited setting from parent element or test configuration

Return type:  int

GetErrorRecoveryPkgPath()[¶](#ApiClient.PackageCall.GetErrorRecoveryPkgPath "Link to this definition")  
Returns the path of the error recovery Package to be executed upon abort of test execution or ERROR/FAILED, if this element has a custom setting which overrides inherited settings from the parent element or from the test configuration.

see also [`GetErrorRecoveryPkgLevel()`](#ApiClient.PackageCall.GetErrorRecoveryPkgLevel "ApiClient.PackageCall.GetErrorRecoveryPkgLevel")

Returns:  Absolute path to Package file; None if inherited or explicitly disabled

Return type:  str

GetName()[¶](#ApiClient.PackageCall.GetName "Link to this definition")  
Returns the name of the project component.

Returns:  Name of the component

Return type:  str

GetPackage()[¶](#ApiClient.PackageCall.GetPackage "Link to this definition")  
Returns the referenced package.

Returns:  referenced package

Return type:  [`Package`](PackageApi.md#ApiClient.Package "ApiClient.Package")

Raises:  
**ApiError** – If the referenced package file (\*.pkg) does not exist.

GetParameterGenerators(*skipDisabled=True*)[¶](#ApiClient.PackageCall.GetParameterGenerators "Link to this definition")  
Returns all parameter generators of the package call.

Parameters:  **skipDisabled** (*boolean*) – Defines whether disabled components should be included.

Returns:  Parameter sets

Return type:  list[[`ParameterGenerator`](#ApiClient.ParameterGenerator "ApiClient.ParameterGenerator")]

GetParameterSets(*skipDisabled=True*)[¶](#ApiClient.PackageCall.GetParameterSets "Link to this definition")  
Returns all parameter sets of the package call.

Parameters:  **skipDisabled** (*boolean*) – Defines whether disabled components should be included.

Returns:  Parameter sets

Return type:  list[[`ParameterSet`](ProjectApi.md#ApiClient.ParameterSet "ApiClient.ParameterSet")]

GetParameterVariationGenerators(*skipDisabled=True*)[¶](#ApiClient.PackageCall.GetParameterVariationGenerators "Link to this definition")  
Returns all parameter variation generators of the package call.

Parameters:  **skipDisabled** (*bool*) – Defines whether disabled generators should be excluded.

Returns:  The parameter variation generators.

Return type:  list[[`ParameterVariationGeneratorComponent`](#ApiClient.ParameterVariationGeneratorComponent "ApiClient.ParameterVariationGeneratorComponent")]

GetParent()[¶](#ApiClient.PackageCall.GetParent "Link to this definition")  
Returns the parent project component.

Returns:  Parent component

Return type:  [`ProjectComponent`](#ApiClient.ProjectComponent "ApiClient.ProjectComponent")

GetPosition()[¶](#ApiClient.PackageCall.GetPosition "Link to this definition")  
Returns the position in the parent project.

Returns:  parent position

Return type:  integer

GetProjectRelativePath()[¶](#ApiClient.PackageCall.GetProjectRelativePath "Link to this definition")  
Returns the file project relative path of the referenced package.

The returned path is a relative path, its base is the folder where the calling project is located, just like the path is shown in the package test step’s dialog.

Returns:  File name with relative path of the package to be called.

Return type:  str

Raises:  
**ProjectNotSavedError** – If this method is called before project is saved.

GetTestCaseId()[¶](#ApiClient.PackageCall.GetTestCaseId "Link to this definition")  
Returns the test case id of the package test component.

Returns:  Test case id.

Return type:  str

GetTestScriptId()[¶](#ApiClient.PackageCall.GetTestScriptId "Link to this definition")  
Returns the test script id of the corresponding package.

Returns:  Test script id.

Return type:  str

GetType()[¶](#ApiClient.PackageCall.GetType "Link to this definition")  
Returns the type (class name) of the project component, e.g.  
- “ConfigChange”

- “ParameterSet”

- “PackageCall”

- “Project”

- “PackageGenerator”

Returns:  Type (class name) of the project component

Return type:  str

HasComponents()[¶](#ApiClient.PackageCall.HasComponents "Link to this definition")  
Returns whether the package call has children.

Returns:  True if there are children, False otherwise.

Return type:  boolean

HasCustomErrorRecoveryPackageSettings()[¶](#ApiClient.PackageCall.HasCustomErrorRecoveryPackageSettings "Link to this definition")  
Returns whether the Package execution settings in case of test abort or ERROR/FAILED of the parent element are overridden

Returns:  True if this element has custom error recovery package settings that override the parent element’s settings or those from the test configuration

Return type:  boolean

HasCustomRestoreSettings()[¶](#ApiClient.PackageCall.HasCustomRestoreSettings "Link to this definition")  
Returns if the value restore settings of the parent element are used or overridden by custom settings

Returns:  True if custom settings used, False if parent settings used

Return type:  boolean

HasCustomRetrySettings()[¶](#ApiClient.PackageCall.HasCustomRetrySettings "Link to this definition")  
Returns if the retry settings of the parent element are used

Returns:  True if parent settings used, False if custom settings defined

Return type:  boolean

InsertParameterSet(*parameterSet*, *position=None*)[¶](#ApiClient.PackageCall.InsertParameterSet "Link to this definition")  
Adds a parameter set to the package call.

Parameters:  - **parameterSet** ([`ParameterSet`](ProjectApi.md#ApiClient.ParameterSet "ApiClient.ParameterSet")) – parameter set

- **position** (*integer*) – Position to insert the parameter set inside the package call

IsAutomaticValueRestoreActivated()[¶](#ApiClient.PackageCall.IsAutomaticValueRestoreActivated "Link to this definition")  
Returns if the automatic value restore is activated

Returns:  True if activated, else False

Return type:  boolean

IsAutomaticValueRestoreDeactivated()[¶](#ApiClient.PackageCall.IsAutomaticValueRestoreDeactivated "Link to this definition")  
Returns if the automatic value restore is deactivated

Returns:  True if deactivated, else False

Return type:  boolean

IsEnabled()[¶](#ApiClient.PackageCall.IsEnabled "Link to this definition")  
Returns the state of the test step.

Returns:  True if test step is enabled, otherwise False

Return type:  bool

RemoveFromProject()[¶](#ApiClient.PackageCall.RemoveFromProject "Link to this definition")  
Removes this component from the project.

Raises:  
**ApiError** – if the component is not part of any project

RemoveParameterGenerator(*paramGenerator*)[¶](#ApiClient.PackageCall.RemoveParameterGenerator "Link to this definition")  
Removes a parameter generator from the package call.

Parameters:  **paramGenerator** ([`ParameterGenerator`](#ApiClient.ParameterGenerator "ApiClient.ParameterGenerator")) – The parameter generator to be removed

Raises:  
**ApiError** –

- If the given parameter generator is not part if the package call

- If paramGenerator ist not of type [`ParameterGenerator`](#ApiClient.ParameterGenerator "ApiClient.ParameterGenerator")

RemoveParameterSet(*paramSet*)[¶](#ApiClient.PackageCall.RemoveParameterSet "Link to this definition")  
Removes a parameter set from the package call.

Parameters:  **paramSet** ([`ParameterSet`](ProjectApi.md#ApiClient.ParameterSet "ApiClient.ParameterSet")) – The parameter set to be removed

Raises:  
**ApiError** –

- If the given parameter set is not part if the package call

- If paramGenerator ist not of type [`ParameterSet`](ProjectApi.md#ApiClient.ParameterSet "ApiClient.ParameterSet")

RemoveParameterVariationGenerator(*paramVariationGenerator*)[¶](#ApiClient.PackageCall.RemoveParameterVariationGenerator "Link to this definition")  
Removes a parameter variation generator from the package call.

Parameters:  **paramVariationGenerator** ([`ParameterVariationGeneratorComponent`](#ApiClient.ParameterVariationGeneratorComponent "ApiClient.ParameterVariationGeneratorComponent")) – The parameter variation generator to be removed

Raises:  
**ApiError** –

- If the given parameter variation generator is not part if the package call

- If paramVariationGenerator is not of type [`ParameterVariationGeneratorComponent`](#ApiClient.ParameterVariationGeneratorComponent "ApiClient.ParameterVariationGeneratorComponent")

SetCustomRetryCondition(*condition*)[¶](#ApiClient.PackageCall.SetCustomRetryCondition "Link to this definition")  
Sets the condition of the custom retry. Must be one of the following:

- ‘ERROR’

- ‘FAILED’

- ‘ERROR/FAILED’

Parameters:  **condition** (*str*) – The condition of the custom retry

SetCustomRetryCount(*count*)[¶](#ApiClient.PackageCall.SetCustomRetryCount "Link to this definition")  
Sets the number of the retries for all Packages within the project component.

Parameters:  **count** (*integer*) – Number of the custom retries

SetEnabled(*state=True*)[¶](#ApiClient.PackageCall.SetEnabled "Link to this definition")  
Enable or disable the test step.

Parameters:  **state** (*bool*) – True (=Default) to enable, False to disable the test step.

SetErrorRecoveryPkgLevel(*level*)[¶](#ApiClient.PackageCall.SetErrorRecoveryPkgLevel "Link to this definition")  
Sets the conditions under which the error recovery package (configured via [`SetErrorRecoveryPkgPath()`](#ApiClient.PackageCall.SetErrorRecoveryPkgPath "ApiClient.PackageCall.SetErrorRecoveryPkgPath")) will be executed

This overrides settings from the parent element or from the test configuration.

Parameters:  **level** (*int*) –

- -1  
  disabled

- 0 on abort only

- 1 on ERROR and on abort

- 2 on FAILED, ERROR and abort.

SetErrorRecoveryPkgPath(*packagePath*)[¶](#ApiClient.PackageCall.SetErrorRecoveryPkgPath "Link to this definition")  
Sets the path for a Package to be executed upon abort of test execution or ERROR/FAILED.

This overrides settings from the parent element or from the test configuration.

See also [`SetErrorRecoveryPkgLevel()`](#ApiClient.PackageCall.SetErrorRecoveryPkgLevel "ApiClient.PackageCall.SetErrorRecoveryPkgLevel")

Parameters:  **packagePath** (*str*) – Absolute path to Package file

SetName(*name*)[¶](#ApiClient.PackageCall.SetName "Link to this definition")  
Sets the name of the project component.

Parameters:  **name** (*str*) – Name of the component

SetTestCaseId(*testCaseId*)[¶](#ApiClient.PackageCall.SetTestCaseId "Link to this definition")  
Sets the test case id of the current package test.

Parameters:  **testCaseId** (*str*) – Test case id

UseParentErrorRecoveryPackageSettings()[¶](#ApiClient.PackageCall.UseParentErrorRecoveryPackageSettings "Link to this definition")  
Sets that the Package execution settings in case of test abort or ERROR/FAILED of the parent element are used. Existing custom settings are deleted.

UseParentRetrySettings()[¶](#ApiClient.PackageCall.UseParentRetrySettings "Link to this definition")  
Sets that the retry settings of the parent element are used. Existing custom settings are deleted.

UseParentValueRestoreSettings()[¶](#ApiClient.PackageCall.UseParentValueRestoreSettings "Link to this definition")  
Sets that the settings whether to restore the value of test quantities after the execution of every Package of the parent element are used. Existing custom settings are deleted.

## ProjectCall[¶](#projectcall "Link to this heading")

*class* ProjectCall[¶](#ApiClient.ProjectCall "Link to this definition")  
Base class

[`ProjectComponent`](#ApiClient.ProjectComponent "ApiClient.ProjectComponent")

Returned by

- [`ComponentApi.CreateProjectCall`](#ApiClient.ComponentApi.CreateProjectCall "ApiClient.ComponentApi.CreateProjectCall")

- [`Project.GetProjectCalls`](ProjectApi.md#ApiClient.Project.GetProjectCalls "ApiClient.Project.GetProjectCalls")

ActivateAbortOnSubprojectAbort()[¶](#ApiClient.ProjectCall.ActivateAbortOnSubprojectAbort "Link to this definition")  
Activates abort of whole project on abort of subprojects.

ActivateAutomaticValueRestore()[¶](#ApiClient.ProjectCall.ActivateAutomaticValueRestore "Link to this definition")  
Activates value restore of test quantities after the execution of every Package.

ActivateIndependentSubprojectExecution()[¶](#ApiClient.ProjectCall.ActivateIndependentSubprojectExecution "Link to this definition")  
Activates independent execution of subprojects.

Clone()[¶](#ApiClient.ProjectCall.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`ProjectCall`](#ApiClient.ProjectCall "ApiClient.ProjectCall")

DeactivateAbortOnSubprojectAbort()[¶](#ApiClient.ProjectCall.DeactivateAbortOnSubprojectAbort "Link to this definition")  
Deactivate abort of whole project on abort of subprojects.

DeactivateAutomaticValueRestore()[¶](#ApiClient.ProjectCall.DeactivateAutomaticValueRestore "Link to this definition")  
Deactivate value restore of test quantities after the execution of every Package.

DeactivateIndependentSubprojectExecution()[¶](#ApiClient.ProjectCall.DeactivateIndependentSubprojectExecution "Link to this definition")  
Deactivate independent execution of subprojects.

GetAbsolutePath()[¶](#ApiClient.ProjectCall.GetAbsolutePath "Link to this definition")  
Returns the absolute path to referenced project.

Returns:  absolute path to referenced project

Return type:  str

GetAlternativeReportDirectory()[¶](#ApiClient.ProjectCall.GetAlternativeReportDirectory "Link to this definition")  
Returns the name of the directory within the report directory, in which the results of the separate project execution should be saved.

Returns:  name of directory to store results

Return type:  str

GetCustomRetryCondition()[¶](#ApiClient.ProjectCall.GetCustomRetryCondition "Link to this definition")  
Returns the condition of the custom retries. Returns one of the following:

- ‘ERROR’

- ‘FAILED’

- ‘ERROR/FAILED’

Returns:  The condition of the custom retry

Return type:  str

GetCustomRetryCount()[¶](#ApiClient.ProjectCall.GetCustomRetryCount "Link to this definition")  
Returns the number of the retries defined on the project component.

Returns:  Number of the custom retries

Return type:  integer

GetErrorRecoveryPkgLevel()[¶](#ApiClient.ProjectCall.GetErrorRecoveryPkgLevel "Link to this definition")  
Returns the conditions under which the error recovery package (configured via [`SetErrorRecoveryPkgPath()`](#ApiClient.ProjectCall.SetErrorRecoveryPkgPath "ApiClient.ProjectCall.SetErrorRecoveryPkgPath")) will be executed

This overrides settings from the parent element or from the test configuration.

Returns:  - -1 = disabled

- 0 = on abort only

- 1 = on ERROR and on abort

- 2 = on FAILED, ERROR and abort.

- None: use inherited setting from parent element or test configuration

Return type:  int

GetErrorRecoveryPkgPath()[¶](#ApiClient.ProjectCall.GetErrorRecoveryPkgPath "Link to this definition")  
Returns the path of the error recovery Package to be executed upon abort of test execution or ERROR/FAILED, if this element has a custom setting which overrides inherited settings from the parent element or from the test configuration.

see also [`GetErrorRecoveryPkgLevel()`](#ApiClient.ProjectCall.GetErrorRecoveryPkgLevel "ApiClient.ProjectCall.GetErrorRecoveryPkgLevel")

Returns:  Absolute path to Package file; None if inherited or explicitly disabled

Return type:  str

GetName()[¶](#ApiClient.ProjectCall.GetName "Link to this definition")  
Returns the name of the project component.

Returns:  Name of the component

Return type:  str

GetParent()[¶](#ApiClient.ProjectCall.GetParent "Link to this definition")  
Returns the parent project component.

Returns:  Parent component

Return type:  [`ProjectComponent`](#ApiClient.ProjectComponent "ApiClient.ProjectComponent")

GetPosition()[¶](#ApiClient.ProjectCall.GetPosition "Link to this definition")  
Returns the position in the parent project.

Returns:  parent position

Return type:  integer

GetProject()[¶](#ApiClient.ProjectCall.GetProject "Link to this definition")  
Returns the referenced project.

Returns:  Referenced project

Return type:  [`Project`](ProjectApi.md#ApiClient.Project "ApiClient.Project")

Raises:  
**ApiError** – If the referenced project file (\*.prj) does not exist.

GetProjectRelativePath()[¶](#ApiClient.ProjectCall.GetProjectRelativePath "Link to this definition")  
Returns the path of the referenced project, relative to its containing project.

The returned path is a relative path, its base is the folder where the calling project is located.

Returns:  File name with relative path of the project to be called.

Return type:  str

Raises:  
**ProjectNotSavedError** – If this method is called before project is saved.

GetRandomExecutionOrderState()[¶](#ApiClient.ProjectCall.GetRandomExecutionOrderState "Link to this definition")  
Returns the random execution state of this container.

Returns:  True if activated, False if deactivated or None if it is inherit from parent.

Return type:  boolean

GetType()[¶](#ApiClient.ProjectCall.GetType "Link to this definition")  
Returns the type (class name) of the project component, e.g.  
- “ConfigChange”

- “ParameterSet”

- “PackageCall”

- “Project”

- “PackageGenerator”

Returns:  Type (class name) of the project component

Return type:  str

HasCustomErrorRecoveryPackageSettings()[¶](#ApiClient.ProjectCall.HasCustomErrorRecoveryPackageSettings "Link to this definition")  
Returns whether the Package execution settings in case of test abort or ERROR/FAILED of the parent element are overridden

Returns:  True if this element has custom error recovery package settings that override the parent element’s settings or those from the test configuration

Return type:  boolean

HasCustomRestoreSettings()[¶](#ApiClient.ProjectCall.HasCustomRestoreSettings "Link to this definition")  
Returns if the value restore settings of the parent element are used or overridden by custom settings

Returns:  True if custom settings used, False if parent settings used

Return type:  boolean

HasCustomRetrySettings()[¶](#ApiClient.ProjectCall.HasCustomRetrySettings "Link to this definition")  
Returns if the retry settings of the parent element are used

Returns:  True if parent settings used, False if custom settings defined

Return type:  boolean

HasCustomSubprojectAbortSettings()[¶](#ApiClient.ProjectCall.HasCustomSubprojectAbortSettings "Link to this definition")  
Returns if the subprojects abort settings of the parent element are used or overridden by custom settings

Returns:  True if custom settings used, False if parent settings used

Return type:  boolean

HasCustomSubprojectExecutionSettings()[¶](#ApiClient.ProjectCall.HasCustomSubprojectExecutionSettings "Link to this definition")  
Returns if the subprojects execution settings of the parent element are used or overridden by custom settings

Returns:  True if custom settings used, False if parent settings used

Return type:  boolean

IsAbortOnSubprojectAbortActivated()[¶](#ApiClient.ProjectCall.IsAbortOnSubprojectAbortActivated "Link to this definition")  
Returns if the abort of whole project on abort of subprojects is activated

Returns:  True if activated, else False

Return type:  boolean

IsAbortOnSubprojectAbortDeactivated()[¶](#ApiClient.ProjectCall.IsAbortOnSubprojectAbortDeactivated "Link to this definition")  
Returns if abort of whole project on abort of subprojects is deactivated

Returns:  True if deactivated, else False

Return type:  boolean

IsAutomaticValueRestoreActivated()[¶](#ApiClient.ProjectCall.IsAutomaticValueRestoreActivated "Link to this definition")  
Returns if the automatic value restore is activated

Returns:  True if activated, else False

Return type:  boolean

IsAutomaticValueRestoreDeactivated()[¶](#ApiClient.ProjectCall.IsAutomaticValueRestoreDeactivated "Link to this definition")  
Returns if the automatic value restore is deactivated

Returns:  True if deactivated, else False

Return type:  boolean

IsEnabled()[¶](#ApiClient.ProjectCall.IsEnabled "Link to this definition")  
Returns the state of the test step.

Returns:  True if test step is enabled, otherwise False

Return type:  bool

IsIndependentSubprojectExecutionActivated()[¶](#ApiClient.ProjectCall.IsIndependentSubprojectExecutionActivated "Link to this definition")  
Returns if the independent execution of subprojects is activated

Returns:  True if activated, else False

Return type:  boolean

IsIndependentSubprojectExecutionDeactivated()[¶](#ApiClient.ProjectCall.IsIndependentSubprojectExecutionDeactivated "Link to this definition")  
Returns if the independent execution of subprojects is deactivated

Returns:  True if deactivated, else False

Return type:  boolean

RemoveFromProject()[¶](#ApiClient.ProjectCall.RemoveFromProject "Link to this definition")  
Removes this component from the project.

Raises:  
**ApiError** – if the component is not part of any project

SetAlternativeReportDirectory(*dirName*)[¶](#ApiClient.ProjectCall.SetAlternativeReportDirectory "Link to this definition")  
Sets the name of the directory within the report directory, in which the results of the separate project execution should be saved.

Parameters:  **dirName** (*str*) – name of directory to store results

SetCustomRetryCondition(*condition*)[¶](#ApiClient.ProjectCall.SetCustomRetryCondition "Link to this definition")  
Sets the condition of the custom retry. Must be one of the following:

- ‘ERROR’

- ‘FAILED’

- ‘ERROR/FAILED’

Parameters:  **condition** (*str*) – The condition of the custom retry

SetCustomRetryCount(*count*)[¶](#ApiClient.ProjectCall.SetCustomRetryCount "Link to this definition")  
Sets the number of the retries for all Packages within the project component.

Parameters:  **count** (*integer*) – Number of the custom retries

SetEnabled(*state=True*)[¶](#ApiClient.ProjectCall.SetEnabled "Link to this definition")  
Enable or disable the test step.

Parameters:  **state** (*bool*) – True (=Default) to enable, False to disable the test step.

SetErrorRecoveryPkgLevel(*level*)[¶](#ApiClient.ProjectCall.SetErrorRecoveryPkgLevel "Link to this definition")  
Sets the conditions under which the error recovery package (configured via [`SetErrorRecoveryPkgPath()`](#ApiClient.ProjectCall.SetErrorRecoveryPkgPath "ApiClient.ProjectCall.SetErrorRecoveryPkgPath")) will be executed

This overrides settings from the parent element or from the test configuration.

Parameters:  **level** (*int*) –

- -1  
  disabled

- 0 on abort only

- 1 on ERROR and on abort

- 2 on FAILED, ERROR and abort.

SetErrorRecoveryPkgPath(*packagePath*)[¶](#ApiClient.ProjectCall.SetErrorRecoveryPkgPath "Link to this definition")  
Sets the path for a Package to be executed upon abort of test execution or ERROR/FAILED.

This overrides settings from the parent element or from the test configuration.

See also [`SetErrorRecoveryPkgLevel()`](#ApiClient.ProjectCall.SetErrorRecoveryPkgLevel "ApiClient.ProjectCall.SetErrorRecoveryPkgLevel")

Parameters:  **packagePath** (*str*) – Absolute path to Package file

SetName(*name*)[¶](#ApiClient.ProjectCall.SetName "Link to this definition")  
Sets the name of the project component.

Parameters:  **name** (*str*) – Name of the component

SetRandomExecutionState(*state*)[¶](#ApiClient.ProjectCall.SetRandomExecutionState "Link to this definition")  
Sets the random execution state of this container.

Parameters:  **state** (*boolean*) – True to activate, False to deactivate or None for inheritance from parent.

UseParentErrorRecoveryPackageSettings()[¶](#ApiClient.ProjectCall.UseParentErrorRecoveryPackageSettings "Link to this definition")  
Sets that the Package execution settings in case of test abort or ERROR/FAILED of the parent element are used. Existing custom settings are deleted.

UseParentRetrySettings()[¶](#ApiClient.ProjectCall.UseParentRetrySettings "Link to this definition")  
Sets that the retry settings of the parent element are used. Existing custom settings are deleted.

UseParentSubprojectAbortSettings()[¶](#ApiClient.ProjectCall.UseParentSubprojectAbortSettings "Link to this definition")  
Sets that the settings whether to cancel or end the whole project execution on abort of a separately executed subproject of the parent element are used. Existing custom settings are deleted.

UseParentSubprojectExecutionSettings()[¶](#ApiClient.ProjectCall.UseParentSubprojectExecutionSettings "Link to this definition")  
Sets that the settings whether to execute subprojects independently of the parent element are used. Existing custom settings are deleted.

UseParentValueRestoreSettings()[¶](#ApiClient.ProjectCall.UseParentValueRestoreSettings "Link to this definition")  
Sets that the settings whether to restore the value of test quantities after the execution of every Package of the parent element are used. Existing custom settings are deleted.

GetPath()[¶](#ApiClient.ProjectCall.GetPath "Link to this definition")  
Returns the file system path of the referenced project.

If this method returns a relative path, its base is the folder where the calling project is located, just like the path is shown in the project call project step’s dialog.

If this method returns an empty string, the parent project has not been saved yet.

Returns:  File name with relative path of the project to be called.

Return type:  str

Deprecated since version 2024.3.0: Use [`GetProjectRelativePath()`](#ApiClient.ProjectCall.GetProjectRelativePath "ApiClient.ProjectCall.GetProjectRelativePath") or [`GetAbsolutePath()`](#ApiClient.ProjectCall.GetAbsolutePath "ApiClient.ProjectCall.GetAbsolutePath") instead.

## ProjectFolder[¶](#projectfolder "Link to this heading")

*class* ProjectFolder[¶](#ApiClient.ProjectFolder "Link to this definition")  
Base class

[`ProjectComponent`](#ApiClient.ProjectComponent "ApiClient.ProjectComponent")

Returned by

- [`ComponentApi.CreateFolder`](#ApiClient.ComponentApi.CreateFolder "ApiClient.ComponentApi.CreateFolder")

- [`Project.GetFolders`](ProjectApi.md#ApiClient.Project.GetFolders "ApiClient.Project.GetFolders")

Subclasses

- [`Project`](ProjectApi.md#ApiClient.Project "ApiClient.Project")

GlobalConstants[¶](#ApiClient.ProjectFolder.GlobalConstants "Link to this definition")  
Returns access to the global constants specified on the project component.

Returns:  Global constants interface of the project component

Return type:  [`GlobalConstants`](#ApiClient.GlobalConstants "ApiClient.GlobalConstants")

MappingFiles[¶](#ApiClient.ProjectFolder.MappingFiles "Link to this definition")  
Returns access to the mapping file list

Returns:  Mapping file list object

Return type:  [`MappingFiles`](#ApiClient.MappingFiles "ApiClient.MappingFiles")

PackageParameters[¶](#ApiClient.ProjectFolder.PackageParameters "Link to this definition")  
Returns access to the package parameters specified on the project component.

Returns:  Package parameters interface of the project component

Return type:  [`PackageParameters`](#ApiClient.PackageParameters "ApiClient.PackageParameters")

ActivateAbortOnSubprojectAbort()[¶](#ApiClient.ProjectFolder.ActivateAbortOnSubprojectAbort "Link to this definition")  
Activates abort of whole project on abort of subprojects.

ActivateAutomaticValueRestore()[¶](#ApiClient.ProjectFolder.ActivateAutomaticValueRestore "Link to this definition")  
Activates value restore of test quantities after the execution of every Package.

ActivateIndependentSubprojectExecution()[¶](#ApiClient.ProjectFolder.ActivateIndependentSubprojectExecution "Link to this definition")  
Activates independent execution of subprojects.

AppendComponent(*component*)[¶](#ApiClient.ProjectFolder.AppendComponent "Link to this definition")  
Adds a previously created component at the end of the folder.

Parameters:  **component** ([`ProjectComponent`](#ApiClient.ProjectComponent "ApiClient.ProjectComponent")) – The project component to be appended

Clone()[¶](#ApiClient.ProjectFolder.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`ProjectFolder`](#ApiClient.ProjectFolder "ApiClient.ProjectFolder")

DeactivateAbortOnSubprojectAbort()[¶](#ApiClient.ProjectFolder.DeactivateAbortOnSubprojectAbort "Link to this definition")  
Deactivate abort of whole project on abort of subprojects.

DeactivateAutomaticValueRestore()[¶](#ApiClient.ProjectFolder.DeactivateAutomaticValueRestore "Link to this definition")  
Deactivate value restore of test quantities after the execution of every Package.

DeactivateIndependentSubprojectExecution()[¶](#ApiClient.ProjectFolder.DeactivateIndependentSubprojectExecution "Link to this definition")  
Deactivate independent execution of subprojects.

GetComponents()[¶](#ApiClient.ProjectFolder.GetComponents "Link to this definition")  
Returns all direct children of the folder.

Returns:  List with all children components

Return type:  list[[`ProjectComponent`](#ApiClient.ProjectComponent "ApiClient.ProjectComponent")]

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
Returns the conditions under which the error recovery package (configured via [`SetErrorRecoveryPkgPath()`](#ApiClient.ProjectFolder.SetErrorRecoveryPkgPath "ApiClient.ProjectFolder.SetErrorRecoveryPkgPath")) will be executed

This overrides settings from the parent element or from the test configuration.

Returns:  - -1 = disabled

- 0 = on abort only

- 1 = on ERROR and on abort

- 2 = on FAILED, ERROR and abort.

- None: use inherited setting from parent element or test configuration

Return type:  int

GetErrorRecoveryPkgPath()[¶](#ApiClient.ProjectFolder.GetErrorRecoveryPkgPath "Link to this definition")  
Returns the path of the error recovery Package to be executed upon abort of test execution or ERROR/FAILED, if this element has a custom setting which overrides inherited settings from the parent element or from the test configuration.

see also [`GetErrorRecoveryPkgLevel()`](#ApiClient.ProjectFolder.GetErrorRecoveryPkgLevel "ApiClient.ProjectFolder.GetErrorRecoveryPkgLevel")

Returns:  Absolute path to Package file; None if inherited or explicitly disabled

Return type:  str

GetName()[¶](#ApiClient.ProjectFolder.GetName "Link to this definition")  
Returns the name of the project component.

Returns:  Name of the component

Return type:  str

GetParent()[¶](#ApiClient.ProjectFolder.GetParent "Link to this definition")  
Returns the parent project component.

Returns:  Parent component

Return type:  [`ProjectComponent`](#ApiClient.ProjectComponent "ApiClient.ProjectComponent")

GetPosition()[¶](#ApiClient.ProjectFolder.GetPosition "Link to this definition")  
Returns the position in the parent project.

Returns:  parent position

Return type:  integer

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

InsertComponent(*component*, *position*)[¶](#ApiClient.ProjectFolder.InsertComponent "Link to this definition")  
Inserts a previously created component into the folder at the given position.

Parameters:  - **component** ([`ProjectComponent`](#ApiClient.ProjectComponent "ApiClient.ProjectComponent")) – The project component to be inserted

- **position** (*integer*) – Position to insert the project component

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

RemoveComponent(*component*)[¶](#ApiClient.ProjectFolder.RemoveComponent "Link to this definition")  
Removes a component from the folder.

Parameters:  **component** ([`ProjectComponent`](#ApiClient.ProjectComponent "ApiClient.ProjectComponent")) – The project component to be removed

Raises:  
**ApiError** – When the given component is not part of the project

RemoveFromProject()[¶](#ApiClient.ProjectFolder.RemoveFromProject "Link to this definition")  
Removes this component from the project.

Raises:  
**ApiError** – if the component is not part of any project

SetCustomRetryCondition(*condition*)[¶](#ApiClient.ProjectFolder.SetCustomRetryCondition "Link to this definition")  
Sets the condition of the custom retry. Must be one of the following:

- ‘ERROR’

- ‘FAILED’

- ‘ERROR/FAILED’

Parameters:  **condition** (*str*) – The condition of the custom retry

SetCustomRetryCount(*count*)[¶](#ApiClient.ProjectFolder.SetCustomRetryCount "Link to this definition")  
Sets the number of the retries for all Packages within the project component.

Parameters:  **count** (*integer*) – Number of the custom retries

SetEnabled(*state=True*)[¶](#ApiClient.ProjectFolder.SetEnabled "Link to this definition")  
Enable or disable the test step.

Parameters:  **state** (*bool*) – True (=Default) to enable, False to disable the test step.

SetErrorRecoveryPkgLevel(*level*)[¶](#ApiClient.ProjectFolder.SetErrorRecoveryPkgLevel "Link to this definition")  
Sets the conditions under which the error recovery package (configured via [`SetErrorRecoveryPkgPath()`](#ApiClient.ProjectFolder.SetErrorRecoveryPkgPath "ApiClient.ProjectFolder.SetErrorRecoveryPkgPath")) will be executed

This overrides settings from the parent element or from the test configuration.

Parameters:  **level** (*int*) –

- -1  
  disabled

- 0 on abort only

- 1 on ERROR and on abort

- 2 on FAILED, ERROR and abort.

SetErrorRecoveryPkgPath(*packagePath*)[¶](#ApiClient.ProjectFolder.SetErrorRecoveryPkgPath "Link to this definition")  
Sets the path for a Package to be executed upon abort of test execution or ERROR/FAILED.

This overrides settings from the parent element or from the test configuration.

See also [`SetErrorRecoveryPkgLevel()`](#ApiClient.ProjectFolder.SetErrorRecoveryPkgLevel "ApiClient.ProjectFolder.SetErrorRecoveryPkgLevel")

Parameters:  **packagePath** (*str*) – Absolute path to Package file

SetName(*name*)[¶](#ApiClient.ProjectFolder.SetName "Link to this definition")  
Sets the name of the project component.

Parameters:  **name** (*str*) – Name of the component

SetRandomExecutionState(*state*)[¶](#ApiClient.ProjectFolder.SetRandomExecutionState "Link to this definition")  
Sets the random execution state of this container.

Parameters:  **state** (*boolean*) – True to activate, False to deactivate or None for inheritance from parent.

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

## PackageGenerator[¶](#packagegenerator "Link to this heading")

*class* PackageGenerator[¶](#ApiClient.PackageGenerator "Link to this definition")  
Base classes

- [`ParameterGenerator`](#ApiClient.ParameterGenerator "ApiClient.ParameterGenerator")

- [`ProjectComponent`](#ApiClient.ProjectComponent "ApiClient.ProjectComponent")

Returned by

- [`ComponentApi.CreatePackageGenerator`](#ApiClient.ComponentApi.CreatePackageGenerator "ApiClient.ComponentApi.CreatePackageGenerator")

- [`Project.GetPackageGenerators`](ProjectApi.md#ApiClient.Project.GetPackageGenerators "ApiClient.Project.GetPackageGenerators")

Clone()[¶](#ApiClient.PackageGenerator.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`PackageGenerator`](#ApiClient.PackageGenerator "ApiClient.PackageGenerator")

GenerateProject(*destinationPath*)[¶](#ApiClient.PackageGenerator.GenerateProject "Link to this definition")  
Initiates the execution of the generator and stores the result as a new project file.

Parameters:  **destinationPath** (*str*) – Absolute destination path to store the project file

GetAttribute(*attributeName*)[¶](#ApiClient.PackageGenerator.GetAttribute "Link to this definition")  
Returns the value of the attribute of the given name. Value is returned as str. Examples: int 5 –\> u”5” string “5” –\> u“‘5’” list [1,2,3] –\> u”[1,2,3]”

Parameters:  **attributeName** (*str*) – Name of attribute to be returned

Returns:  attribute value

Return type:  str

GetGeneratorAttributes()[¶](#ApiClient.PackageGenerator.GetGeneratorAttributes "Link to this definition")  
Returns all the stored attributes of the generator. Values are returned as str. Examples: int 5 –\> u”5” string “5” –\> u“‘5’” list [1,2,3] –\> u”[1,2,3]”

Returns:  Dictionary mapping attributes names to values

Return type:  dict[str, str]

GetGeneratorId()[¶](#ApiClient.PackageGenerator.GetGeneratorId "Link to this definition")  
Returns the unique generator id of the referenced parameter generator.

Returns:  generator id

Return type:  str

GetName()[¶](#ApiClient.PackageGenerator.GetName "Link to this definition")  
Returns the name of the project component.

Returns:  Name of the component

Return type:  str

GetParent()[¶](#ApiClient.PackageGenerator.GetParent "Link to this definition")  
Returns the parent project component.

Returns:  Parent component

Return type:  [`ProjectComponent`](#ApiClient.ProjectComponent "ApiClient.ProjectComponent")

GetPosition()[¶](#ApiClient.PackageGenerator.GetPosition "Link to this definition")  
Returns the position in the parent project.

Returns:  parent position

Return type:  integer

GetType()[¶](#ApiClient.PackageGenerator.GetType "Link to this definition")  
Returns the type (class name) of the project component, e.g.  
- “ConfigChange”

- “ParameterSet”

- “PackageCall”

- “Project”

- “PackageGenerator”

Returns:  Type (class name) of the project component

Return type:  str

IsEnabled()[¶](#ApiClient.PackageGenerator.IsEnabled "Link to this definition")  
Returns the state of the test step.

Returns:  True if test step is enabled, otherwise False

Return type:  bool

RemoveFromProject()[¶](#ApiClient.PackageGenerator.RemoveFromProject "Link to this definition")  
Removes this component from the project.

Raises:  
**ApiError** – if the component is not part of any project

SetAttribute(*attributeName*, *value*)[¶](#ApiClient.PackageGenerator.SetAttribute "Link to this definition")  
Sets the value of the attribute of the given name. Value has to be provided as str. Examples: int 5 –\> u”5” string “5” –\> u“‘5’” list [1,2,3] –\> u”[1,2,3]”

Parameters:  - **attributeName** (*str*) – Name of attribute to be returned

- **value** (*str*) – attribute value

SetEnabled(*state=True*)[¶](#ApiClient.PackageGenerator.SetEnabled "Link to this definition")  
Enable or disable the test step.

Parameters:  **state** (*bool*) – True (=Default) to enable, False to disable the test step.

SetGeneratorAttributes(*attributesDict*)[¶](#ApiClient.PackageGenerator.SetGeneratorAttributes "Link to this definition")  
Overwrites the existing attributes of the generator with the provided ones. Values have to be provided as str. Examples: int 5 –\> u”5” string “5” –\> u“‘5’” list [1,2,3] –\> u”[1,2,3]”

Parameters:  **attributesDict** (*dict[str,* *str]*) – Dictionary mapping attribute names to values

SetName(*name*)[¶](#ApiClient.PackageGenerator.SetName "Link to this definition")  
Sets the name of the project component.

Parameters:  **name** (*str*) – Name of the component

## ProjectGenerator[¶](#projectgenerator "Link to this heading")

*class* ProjectGenerator[¶](#ApiClient.ProjectGenerator "Link to this definition")  
Base classes

- [`ParameterGenerator`](#ApiClient.ParameterGenerator "ApiClient.ParameterGenerator")

- [`ProjectComponent`](#ApiClient.ProjectComponent "ApiClient.ProjectComponent")

Returned by

- [`ComponentApi.CreateProjectGenerator`](#ApiClient.ComponentApi.CreateProjectGenerator "ApiClient.ComponentApi.CreateProjectGenerator")

- [`Project.GetProjectGenerators`](ProjectApi.md#ApiClient.Project.GetProjectGenerators "ApiClient.Project.GetProjectGenerators")

Clone()[¶](#ApiClient.ProjectGenerator.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`ProjectGenerator`](#ApiClient.ProjectGenerator "ApiClient.ProjectGenerator")

GenerateProject(*destinationPath*)[¶](#ApiClient.ProjectGenerator.GenerateProject "Link to this definition")  
Initiates the execution of the generator and stores the result as a new project file.

Parameters:  **destinationPath** (*str*) – Absolute destination path to store the project file

GetAttribute(*attributeName*)[¶](#ApiClient.ProjectGenerator.GetAttribute "Link to this definition")  
Returns the value of the attribute of the given name. Value is returned as str. Examples: int 5 –\> u”5” string “5” –\> u“‘5’” list [1,2,3] –\> u”[1,2,3]”

Parameters:  **attributeName** (*str*) – Name of attribute to be returned

Returns:  attribute value

Return type:  str

GetGeneratorAttributes()[¶](#ApiClient.ProjectGenerator.GetGeneratorAttributes "Link to this definition")  
Returns all the stored attributes of the generator. Values are returned as str. Examples: int 5 –\> u”5” string “5” –\> u“‘5’” list [1,2,3] –\> u”[1,2,3]”

Returns:  Dictionary mapping attributes names to values

Return type:  dict[str, str]

GetGeneratorId()[¶](#ApiClient.ProjectGenerator.GetGeneratorId "Link to this definition")  
Returns the unique generator id of the referenced parameter generator.

Returns:  generator id

Return type:  str

GetName()[¶](#ApiClient.ProjectGenerator.GetName "Link to this definition")  
Returns the name of the project component.

Returns:  Name of the component

Return type:  str

GetParent()[¶](#ApiClient.ProjectGenerator.GetParent "Link to this definition")  
Returns the parent project component.

Returns:  Parent component

Return type:  [`ProjectComponent`](#ApiClient.ProjectComponent "ApiClient.ProjectComponent")

GetPosition()[¶](#ApiClient.ProjectGenerator.GetPosition "Link to this definition")  
Returns the position in the parent project.

Returns:  parent position

Return type:  integer

GetType()[¶](#ApiClient.ProjectGenerator.GetType "Link to this definition")  
Returns the type (class name) of the project component, e.g.  
- “ConfigChange”

- “ParameterSet”

- “PackageCall”

- “Project”

- “PackageGenerator”

Returns:  Type (class name) of the project component

Return type:  str

IsEnabled()[¶](#ApiClient.ProjectGenerator.IsEnabled "Link to this definition")  
Returns the state of the test step.

Returns:  True if test step is enabled, otherwise False

Return type:  bool

RemoveFromProject()[¶](#ApiClient.ProjectGenerator.RemoveFromProject "Link to this definition")  
Removes this component from the project.

Raises:  
**ApiError** – if the component is not part of any project

SetAttribute(*attributeName*, *value*)[¶](#ApiClient.ProjectGenerator.SetAttribute "Link to this definition")  
Sets the value of the attribute of the given name. Value has to be provided as str. Examples: int 5 –\> u”5” string “5” –\> u“‘5’” list [1,2,3] –\> u”[1,2,3]”

Parameters:  - **attributeName** (*str*) – Name of attribute to be returned

- **value** (*str*) – attribute value

SetEnabled(*state=True*)[¶](#ApiClient.ProjectGenerator.SetEnabled "Link to this definition")  
Enable or disable the test step.

Parameters:  **state** (*bool*) – True (=Default) to enable, False to disable the test step.

SetGeneratorAttributes(*attributesDict*)[¶](#ApiClient.ProjectGenerator.SetGeneratorAttributes "Link to this definition")  
Overwrites the existing attributes of the generator with the provided ones. Values have to be provided as str. Examples: int 5 –\> u”5” string “5” –\> u“‘5’” list [1,2,3] –\> u”[1,2,3]”

Parameters:  **attributesDict** (*dict[str,* *str]*) – Dictionary mapping attribute names to values

SetName(*name*)[¶](#ApiClient.ProjectGenerator.SetName "Link to this definition")  
Sets the name of the project component.

Parameters:  **name** (*str*) – Name of the component
