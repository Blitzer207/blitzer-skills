# API for Parameters[¶](#api-for-parameters "Link to this heading")

Part of the [Object based program API](objectApi.md#objectapi)

## ParameterApi[¶](#parameterapi "Link to this heading")

*class* ParameterApi[¶](#ApiClient.ParameterApi "Link to this definition")  
API to access parameter files

Returned by

- [`ApiClient.ParameterApi`](objectApi.md#ApiClient.ApiClient.ParameterApi "ApiClient.ApiClient.ParameterApi")

CreateGlobalConstantsDefinition()[¶](#ApiClient.ParameterApi.CreateGlobalConstantsDefinition "Link to this definition")  
Creates a new global constants definition.

Returns:  New empty global constants definition

Return type:  [`GlobalConstantsDefinition`](#ApiClient.GlobalConstantsDefinition "ApiClient.GlobalConstantsDefinition")

CreatePackageParametersDefinition()[¶](#ApiClient.ParameterApi.CreatePackageParametersDefinition "Link to this definition")  
Creates a new package parameters definition.

Returns:  New empty package parameters definition

Return type:  [`PackageParametersDefinition`](#ApiClient.PackageParametersDefinition "ApiClient.PackageParametersDefinition")

GetChangesForGlobalConstantsDefinitions(*oldConstDefinition*, *newConstDefinition*)[¶](#ApiClient.ParameterApi.GetChangesForGlobalConstantsDefinitions "Link to this definition")  
Get the changes that exist between two given constants definitions.

Parameters:  - **oldConstDefinition** ([`GlobalConstantsDefinition`](#ApiClient.GlobalConstantsDefinition "ApiClient.GlobalConstantsDefinition")) – The old constants definition to compare.

- **newConstDefinition** ([`GlobalConstantsDefinition`](#ApiClient.GlobalConstantsDefinition "ApiClient.GlobalConstantsDefinition")) – The new constants definition to compare.

Returns:  The changes that exist between the two constants definitions.

Return type:  list[[`Change`](ConfigurationApi.md#ApiClient.Change "ApiClient.Change")]

GetChangesForPackageParametersDefinitions(*oldParamDefinition*, *newParamDefinition*)[¶](#ApiClient.ParameterApi.GetChangesForPackageParametersDefinitions "Link to this definition")  
Get the differences that exist between two given package parameters definitions.

Parameters:  - **oldParamDefinition** ([`PackageParametersDefinition`](#ApiClient.PackageParametersDefinition "ApiClient.PackageParametersDefinition")) – The old package parameters definition to compare.

- **newParamDefinition** ([`PackageParametersDefinition`](#ApiClient.PackageParametersDefinition "ApiClient.PackageParametersDefinition")) – The new package parameters definition to compare.

Returns:  The differences that exist between the two package parameters definitions.

Return type:  list[[`Change`](ConfigurationApi.md#ApiClient.Change "ApiClient.Change")]

OpenGlobalConstantsDefinition(*filename*)[¶](#ApiClient.ParameterApi.OpenGlobalConstantsDefinition "Link to this definition")  
Opens an existing global constants definition file (\*.gcd).

Parameters:  **filename** (*str*) – File name of the global constants definition file; Either absolute or relative to the ‘Parameter’ directory

Returns:  Loaded global constants definition

Return type:  [`GlobalConstantsDefinition`](#ApiClient.GlobalConstantsDefinition "ApiClient.GlobalConstantsDefinition")

Raises:  
**ApiError** – If the global constants definition file (\*.gcd) does not exist.

OpenPackageParametersDefinition(*filename*)[¶](#ApiClient.ParameterApi.OpenPackageParametersDefinition "Link to this definition")  
Opens an existing package parameters definition file (\*.ppd).

Parameters:  **filename** (*str*) – File name of the package parameters definition file; Either absolute or relative to the ‘Parameter’ directory

Returns:  Loaded package parameters definition

Return type:  [`PackageParametersDefinition`](#ApiClient.PackageParametersDefinition "ApiClient.PackageParametersDefinition")

Raises:  
**ApiError** – If the package parameters definition file (\*.ppd) does not exist.

SearchGlobalConstantsDefinitions(*searchCriteria*, *useExtendedMode=False*)[¶](#ApiClient.ParameterApi.SearchGlobalConstantsDefinitions "Link to this definition")  
Searches the current workspace and library workspaces for Global Constant Definitions matching the given search criteria.

Parameters:  - **searchCriteria** (*str*) – The search criteria expressed in the ecu.test filter syntax. See section “Handling” =\> “Filter” of the ecu.test User Documentation.

- **useExtendedMode** (*boolean*) – If True, extended search strings are enabled. The default is False, meaning each word in the searchCriteria will be enclosed by wildcards and mapped to the filename. (e.g. “hello world” =\> “Name = ‘\*hello\*’ and Name = ‘\*world\*’”)

Returns:  All matching global constant defintions. If no project matches, an emtpy list is returned.

Return type:  list[[`GlobalConstantsDefinition`](#ApiClient.GlobalConstantsDefinition "ApiClient.GlobalConstantsDefinition")]

Raises:  
**ApiError** – If the searchCriteria has an illegal syntax.

SearchPackageParametersDefinitions(*searchCriteria*, *useExtendedMode=False*)[¶](#ApiClient.ParameterApi.SearchPackageParametersDefinitions "Link to this definition")  
Searches the current workspace and library workspaces for Package Parameter Definitions matching the given search criteria.

Parameters:  - **searchCriteria** (*str*) – The search criteria expressed in the ecu.test filter syntax. See section “Handling” =\> “Filter” of the ecu.test User Documentation.

- **useExtendedMode** (*boolean*) – If True, extended search strings are enabled. The default is False, meaning each word in the searchCriteria will be enclosed by wildcards and mapped to the filename. (e.g. “hello world” =\> “Name = ‘\*hello\*’ and Name = ‘\*world\*’”)

Returns:  All matching Package Parameter Definitions. If no file matches, an emtpy list is returned.

Return type:  list[[`PackageParametersDefinition`](#ApiClient.PackageParametersDefinition "ApiClient.PackageParametersDefinition")]

Raises:  
**ApiError** – If the searchCriteria has an illegal syntax.

## GlobalConstantsDefinition[¶](#globalconstantsdefinition "Link to this heading")

*class* GlobalConstantsDefinition[¶](#ApiClient.GlobalConstantsDefinition "Link to this definition")  
Returned by

- [`AnalysisJob.GetGlobalConstants`](AnalysisJobApi.md#ApiClient.AnalysisJob.GetGlobalConstants "ApiClient.AnalysisJob.GetGlobalConstants")

- [`GlobalConstants.GetGlobalConstantsDefinition`](ComponentApi.md#ApiClient.GlobalConstants.GetGlobalConstantsDefinition "ApiClient.GlobalConstants.GetGlobalConstantsDefinition")

- [`ParameterApi.CreateGlobalConstantsDefinition`](#ApiClient.ParameterApi.CreateGlobalConstantsDefinition "ApiClient.ParameterApi.CreateGlobalConstantsDefinition")

- [`ParameterApi.OpenGlobalConstantsDefinition`](#ApiClient.ParameterApi.OpenGlobalConstantsDefinition "ApiClient.ParameterApi.OpenGlobalConstantsDefinition")

- [`ParameterApi.SearchGlobalConstantsDefinitions`](#ApiClient.ParameterApi.SearchGlobalConstantsDefinitions "ApiClient.ParameterApi.SearchGlobalConstantsDefinitions")

AppendConstant(*name*, *value=None*, *description=None*)[¶](#ApiClient.GlobalConstantsDefinition.AppendConstant "Link to this definition")  
Appends a new global constant. If a constant with the same name already exists, it will be overwritten.

Parameters:  - **name** (*str*) – Name of the constant

- **value** (*string*) – Value expression for the constant. (for strings you need to include quotes!) Can be left empty to create new constant without value.

- **description** (*str*) – Description of the constant

Raises:  
**ApiError** – If constant with the given name and value could not be appended, e.g. if the name is no valid identifier, or the value can not be parsed.

Clone()[¶](#ApiClient.GlobalConstantsDefinition.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`GlobalConstantsDefinition`](#ApiClient.GlobalConstantsDefinition "ApiClient.GlobalConstantsDefinition")

GetAllConstantNames()[¶](#ApiClient.GlobalConstantsDefinition.GetAllConstantNames "Link to this definition")  
Returns a list of all global constant names.

Returns:  List of all global constant names

Return type:  list[str]

GetDescription(*name*)[¶](#ApiClient.GlobalConstantsDefinition.GetDescription "Link to this definition")  
Returns the description of the constant specified by the given name.

Parameters:  **name** (*str*) – Name of the constant

Returns:  Description text

Return type:  str

GetFilename()[¶](#ApiClient.GlobalConstantsDefinition.GetFilename "Link to this definition")  
Returns the file name of the global constants definition file, if this is a file. Returns None if this is part of the test configuration, a parameter set or an unsaved file.

Returns:  The file name of the saved file or None, if not a file

Return type:  str

GetValue(*name*)[¶](#ApiClient.GlobalConstantsDefinition.GetValue "Link to this definition")  
Returns the string representation of the value expression of the constant, specified by the given name.

Parameters:  **name** (*str*) – Name of the constant

Returns:  Expression for the constant value

Return type:  str

Raises:  
**ApiError** – If the constant with the given name does not exist

RemoveConstant(*name*)[¶](#ApiClient.GlobalConstantsDefinition.RemoveConstant "Link to this definition")  
Removes the global constant specified by the given name.

Parameters:  **name** (*str*) – Name of the constant

Returns:  True if successful. False if no constant with such name exists.

Return type:  boolean

Save(*filename=''*)[¶](#ApiClient.GlobalConstantsDefinition.Save "Link to this definition")  
Saves the global constants definition to a file. Appends file ending if needed.

Parameters:  **filename** (*str*) – File name for the global constants definition file (\*.gcd); Either absolute or relative to the ‘Parameter’ directory. If left out, use the existing file name and path (previously set with [`Save()`](#ApiClient.GlobalConstantsDefinition.Save "ApiClient.GlobalConstantsDefinition.Save") or from [`ParameterApi.OpenGlobalConstantsDefinition()`](#ApiClient.ParameterApi.OpenGlobalConstantsDefinition "ApiClient.ParameterApi.OpenGlobalConstantsDefinition"))

SetDescription(*name*, *description*)[¶](#ApiClient.GlobalConstantsDefinition.SetDescription "Link to this definition")  
Sets the description of the constant specified by the given name.

Parameters:  - **name** (*str*) – Name of the constant

- **description** (*str*) – Description text

Raises:  
- **ApiError** – If the constant with the given name does not exist

- **ApiError** – If description is no str

SetValue(*name*, *value*)[¶](#ApiClient.GlobalConstantsDefinition.SetValue "Link to this definition")  
Sets the value expression of the constant specified by the given name.

Parameters:  - **name** (*str*) – Name of the constant

- **value** (*str*) – Value expression for the constant value (for strings you need to include quotes!) Can be set to ‘None’ to reset the constant’s value.

Raises:  
- **ApiError** – If the constant with the given name does not exist

- **ApiError** – If the value is no valid expression

## PackageParametersDefinition[¶](#packageparametersdefinition "Link to this heading")

*class* PackageParametersDefinition[¶](#ApiClient.PackageParametersDefinition "Link to this definition")  
Returned by

- [`PackageParameters.GetPackageParametersDefinition`](ComponentApi.md#ApiClient.PackageParameters.GetPackageParametersDefinition "ApiClient.PackageParameters.GetPackageParametersDefinition")

- [`ParameterApi.CreatePackageParametersDefinition`](#ApiClient.ParameterApi.CreatePackageParametersDefinition "ApiClient.ParameterApi.CreatePackageParametersDefinition")

- [`ParameterApi.OpenPackageParametersDefinition`](#ApiClient.ParameterApi.OpenPackageParametersDefinition "ApiClient.ParameterApi.OpenPackageParametersDefinition")

- [`ParameterApi.SearchPackageParametersDefinitions`](#ApiClient.ParameterApi.SearchPackageParametersDefinitions "ApiClient.ParameterApi.SearchPackageParametersDefinitions")

AppendParameter(*name*, *value=None*, *description=None*)[¶](#ApiClient.PackageParametersDefinition.AppendParameter "Link to this definition")  
Appends a new package parameter. If a parameter with the same name already exists, it will be overwritten.

Parameters:  - **name** (*str*) – Name of the parameter

- **value** (*string*) – Value of the parameter as you would type it in the dialog (i.e. for strings you need to include the quotes!)

- **description** (*str*) – Description of the parameter

Raises:  
**ApiError** – If parameter with the given name (and value/description) could not be appended, e.g. if the value or description are invalid.

Clone()[¶](#ApiClient.PackageParametersDefinition.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`PackageParametersDefinition`](#ApiClient.PackageParametersDefinition "ApiClient.PackageParametersDefinition")

GetAllParameterNames()[¶](#ApiClient.PackageParametersDefinition.GetAllParameterNames "Link to this definition")  
Returns a list of all parameterized package parameter names.

Returns:  List of all parameterized parameter names

Return type:  list[str]

GetDescription(*name*)[¶](#ApiClient.PackageParametersDefinition.GetDescription "Link to this definition")  
Returns the description of the parameter specified by the given name.

Parameters:  **name** (*str*) – Name of the parameter to get the description of

Returns:  The desription of the parameter

Return type:  str

GetFilename()[¶](#ApiClient.PackageParametersDefinition.GetFilename "Link to this definition")  
Returns the file name of the package parameters definition file, if this is a file. Returns None if this is part of a parameter set or an unsaved file.

Returns:  The file name of the saved file or None, if not a file

Return type:  str

GetValue(*name*)[¶](#ApiClient.PackageParametersDefinition.GetValue "Link to this definition")  
Returns the value of the given parameter. If the value of an existing parameter is empty it will return None, if the value is defined as None it will return ‘None’.

Parameters:  **name** (*str*) – Name of the parameter to get the value of

Returns:  Value of the given parameter

Return type:  str

Raises:  
**ApiError** – If the parameter with the given name does not exist

RemoveParameter(*name*)[¶](#ApiClient.PackageParametersDefinition.RemoveParameter "Link to this definition")  
Removes the parameter specified by the given name.

Parameters:  **name** (*str*) – Name of the parameter to remove

Returns:  If removing of the given parameter was successful

Return type:  boolean

Save(*filename=None*)[¶](#ApiClient.PackageParametersDefinition.Save "Link to this definition")  
Saves the package parameters definition to a file. Appends file ending if needed.

Parameters:  **filename** (*str*) – File name of the package parameters definition file (\*.ppd); Either absolute or relative to the ‘Parameter’ directory. Leave out to save the definitions to its existing file (previously set with [`Save()`](#ApiClient.PackageParametersDefinition.Save "ApiClient.PackageParametersDefinition.Save") or from [`ParameterApi.OpenPackageParametersDefinition()`](#ApiClient.ParameterApi.OpenPackageParametersDefinition "ApiClient.ParameterApi.OpenPackageParametersDefinition"))

SetDescription(*name*, *description*)[¶](#ApiClient.PackageParametersDefinition.SetDescription "Link to this definition")  
Sets the description of the parameter specified by the given name.

Parameters:  - **name** (*str*) – Name of the parameter to set the description of

- **description** (*str*) – Description of the parameter to be set

Raises:  
- **ApiError** – If the parameter with the given name does not exist

- **ApiError** – If description is no str

SetValue(*name*, *value=None*)[¶](#ApiClient.PackageParametersDefinition.SetValue "Link to this definition")  
Sets the value of the parameter specified by the given name.

Parameters:  - **name** (*str*) – Name of the parameter to set the value of

- **value** (*str*) – Value of the parameter as you would type it in the editor (i.e. for strings you need to include the quotes!) Can be set to ‘None’ to reset the parameter value.

Raises:  
- **ApiError** – If the parameter with the given name does not exist

- **ApiError** – If the value is no valid expression
