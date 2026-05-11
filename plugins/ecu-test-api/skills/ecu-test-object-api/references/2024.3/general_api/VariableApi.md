# API for Variables[¶](#api-for-variables "Link to this heading")

Part of the [Object based program API](objectApi.md#objectapi)

## VariableApi[¶](#variableapi "Link to this heading")

*class* VariableApi[¶](#ApiClient.VariableApi "Link to this definition")  
Returned by

- [`PackageApi.VariableApi`](PackageApi.md#ApiClient.PackageApi.VariableApi "ApiClient.PackageApi.VariableApi")

CreateBooleanVariable(*name*)[¶](#ApiClient.VariableApi.CreateBooleanVariable "Link to this definition")  
Creates a new boolean variable.

Parameters:  **name** (*str*) – Variable name

Returns:  New boolean variable

Return type:  [`BooleanVariable`](#ApiClient.BooleanVariable "ApiClient.BooleanVariable")

CreateDynamicEnumVariable(*name*)[¶](#ApiClient.VariableApi.CreateDynamicEnumVariable "Link to this definition")  
Creates a new Enum variable with dynamic entries.

Parameters:  **name** (*str*) – Variable name

Returns:  New dynamic enum variable

Return type:  [`DynamicEnumVariable`](#ApiClient.DynamicEnumVariable "ApiClient.DynamicEnumVariable")

CreateDynamicTextTableVariable(*name*)[¶](#ApiClient.VariableApi.CreateDynamicTextTableVariable "Link to this definition")  
Creates a new Texttable variable with dynamic text entries.

Parameters:  **name** (*str*) – Variable name

Returns:  New Texttable variable

Return type:  [`DynamicTextTableVariable`](#ApiClient.DynamicTextTableVariable "ApiClient.DynamicTextTableVariable")

CreateEnumVariable(*name*)[¶](#ApiClient.VariableApi.CreateEnumVariable "Link to this definition")  
Creates a new Enum variable.

Parameters:  **name** (*str*) – Variable name

Returns:  New Enum variable

Return type:  [`EnumVariable`](#ApiClient.EnumVariable "ApiClient.EnumVariable")

CreateFunctionVariable(*name*)[¶](#ApiClient.VariableApi.CreateFunctionVariable "Link to this definition")  
Creates a new function variable.

Parameters:  **name** (*str*) – Variable name

Returns:  New function variable

Return type:  [`FunctionVariable`](#ApiClient.FunctionVariable "ApiClient.FunctionVariable")

CreateNumericVariable(*name*)[¶](#ApiClient.VariableApi.CreateNumericVariable "Link to this definition")  
Creates a new numeric variable.

Parameters:  **name** (*str*) – Variable name

Returns:  New numeric variable

Return type:  [`NumericVariable`](#ApiClient.NumericVariable "ApiClient.NumericVariable")

CreatePyObjectVariable(*name*)[¶](#ApiClient.VariableApi.CreatePyObjectVariable "Link to this definition")  
Creates a new PyObject variable.

Parameters:  **name** (*str*) – Variable name

Returns:  New PyObject variable

Return type:  [`PyObjectVariable`](#ApiClient.PyObjectVariable "ApiClient.PyObjectVariable")

CreateStaticTextTableVariable(*name*)[¶](#ApiClient.VariableApi.CreateStaticTextTableVariable "Link to this definition")  
Creates a new Texttable variable with static text entries.

Parameters:  **name** (*str*) – Variable name

Returns:  New Texttable variable

Return type:  [`StaticTextTableVariable`](#ApiClient.StaticTextTableVariable "ApiClient.StaticTextTableVariable")

CreateStringVariable(*name*)[¶](#ApiClient.VariableApi.CreateStringVariable "Link to this definition")  
Creates a new string variable.

Parameters:  **name** (*str*) – Variable name

Returns:  New string variable

Return type:  [`StringVariable`](#ApiClient.StringVariable "ApiClient.StringVariable")

CreateStructureVariable(*name*)[¶](#ApiClient.VariableApi.CreateStructureVariable "Link to this definition")  
Creates a new Structure variable.

Parameters:  **name** (*str*) – Variable name

Returns:  New Structure variable

Return type:  [`StructureVariable`](#ApiClient.StructureVariable "ApiClient.StructureVariable")

CreateVariable(*name*)[¶](#ApiClient.VariableApi.CreateVariable "Link to this definition")  
Creates a new \<Undefined\> variable.

Parameters:  **name** (*str*) – Variable name

Returns:  New variable

Return type:  [`Variable`](#ApiClient.Variable "ApiClient.Variable")

CreateVectorVariable(*name*, *length=1*)[¶](#ApiClient.VariableApi.CreateVectorVariable "Link to this definition")  
Creates a new Vector variable.

Parameters:  - **name** (*str*) – Variable name

- **length** (*int*) – The maximum length of the Vector

Returns:  A new Vector variable

Return type:  [`VectorVariable`](#ApiClient.VectorVariable "ApiClient.VectorVariable")

## BooleanVariable[¶](#booleanvariable "Link to this heading")

*class* BooleanVariable[¶](#ApiClient.BooleanVariable "Link to this definition")  
Base class

[`Variable`](#ApiClient.Variable "ApiClient.Variable")

Returned by

- [`VariableApi.CreateBooleanVariable`](#ApiClient.VariableApi.CreateBooleanVariable "ApiClient.VariableApi.CreateBooleanVariable")

Clone()[¶](#ApiClient.BooleanVariable.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`BooleanVariable`](#ApiClient.BooleanVariable "ApiClient.BooleanVariable")

GetDescription()[¶](#ApiClient.BooleanVariable.GetDescription "Link to this definition")  
Returns the description of the variable.

Returns:  Description of variable

Return type:  str

GetInitialValue()[¶](#ApiClient.BooleanVariable.GetInitialValue "Link to this definition")  
Returns the initial value of the variable or None if it is not a Boolean.

Returns:  Initial value of the variable

Return type:  bool

GetName()[¶](#ApiClient.BooleanVariable.GetName "Link to this definition")  
Returns the name of the variable.

Returns:  Name of variable

Return type:  str

GetType()[¶](#ApiClient.BooleanVariable.GetType "Link to this definition")  
Returns the type of the initial value of the variable.

Returns:  type of the initial value

Return type:  str

IsParameter()[¶](#ApiClient.BooleanVariable.IsParameter "Link to this definition")  
Returns whether the variable is a parameter.

Returns:  True if parameter, else False

Return type:  boolean

IsRecorded()[¶](#ApiClient.BooleanVariable.IsRecorded "Link to this definition")  
Returns whether the variable is recorded during execution.

Returns:  True if recorded, else False

Return type:  boolean

IsReturn()[¶](#ApiClient.BooleanVariable.IsReturn "Link to this definition")  
Returns whether the variable is a return value.

Returns:  True if return value, else False

Return type:  boolean

SetDescription(*description*)[¶](#ApiClient.BooleanVariable.SetDescription "Link to this definition")  
Sets the description of the variable.

Parameters:  **description** (*str*) – Description of variable

SetInitialValue(*value*)[¶](#ApiClient.BooleanVariable.SetInitialValue "Link to this definition")  
Sets the initial value of the variable.

Parameters:  **value** (*bool*) – Initial value of the variable

SetParameter(*enable=True*)[¶](#ApiClient.BooleanVariable.SetParameter "Link to this definition")  
Sets whether the variable is a parameter or not.

Parameters:  **enable** (*boolean*) – Whether the variable is a parameter or not

SetRecorded(*enable=True*)[¶](#ApiClient.BooleanVariable.SetRecorded "Link to this definition")  
Sets the recording state of the variable to the value of enable.

Parameters:  **enable** (*boolean*) – Whether to enable the recording of the variable

SetReturn(*enable=True*)[¶](#ApiClient.BooleanVariable.SetReturn "Link to this definition")  
Sets whether the variable is a return value or not.

Parameters:  **enable** (*boolean*) – Whether the variable is a return value or not

GetInitialBooleanValue()[¶](#ApiClient.BooleanVariable.GetInitialBooleanValue "Link to this definition")  
Returns the initial value of the variable or None if it is not a Boolean.

Returns:  Initial value of the variable

Return type:  bool

Deprecated since version 2021.1: Method is deprecated. Use GetInitialValue instead.

GetInitialFunctionValue()[¶](#ApiClient.BooleanVariable.GetInitialFunctionValue "Link to this definition")  
Returns the code of the function variable or None if it is not a function variable.

Returns:  Initial code of the function variable

Return type:  string

Deprecated since version 2021.1: Method is deprecated. Use GetInitialValue instead.

GetInitialNumericValue()[¶](#ApiClient.BooleanVariable.GetInitialNumericValue "Link to this definition")  
Returns the initial value of the variable or None if it is not a Numeric.

Returns:  Initial value of the variable

Return type:  int/float

Deprecated since version 2021.1: Method is deprecated. Use GetInitialValue instead.

GetInitialNumericValueString()[¶](#ApiClient.BooleanVariable.GetInitialNumericValueString "Link to this definition")  
Returns the initial value string of the variable, or None if it is not a Numeric.

The initial value is returned exactly as it has been typed in (e.g. in hex, or with additional zeroes), unless it has been set via [`SetInitialNumericValue()`](#ApiClient.BooleanVariable.SetInitialNumericValue "ApiClient.BooleanVariable.SetInitialNumericValue"), which stores only the numeric value itself.

Returns:  Initial value of the variable

Return type:  str

Deprecated since version 2021.1: Method is only supported for numeric variable type in future versions.

GetInitialPyObjectValue()[¶](#ApiClient.BooleanVariable.GetInitialPyObjectValue "Link to this definition")  
Returns the initial value of the variable or None if it is not a PyObject.

Returns:  Initial value of the variable

Return type:  str

Deprecated since version 2021.1: Method is deprecated. Use GetInitialValue instead.

GetInitialStringValue()[¶](#ApiClient.BooleanVariable.GetInitialStringValue "Link to this definition")  
Returns the initial value of the variable or None if it is not a String.

Returns:  Initial value of the variable

Return type:  str

Deprecated since version 2021.1: Method is deprecated. Use GetInitialValue instead.

GetInitialStructureValue()[¶](#ApiClient.BooleanVariable.GetInitialStructureValue "Link to this definition")  
Returns the type of the initial value of the variable or None if it is not a structure.

Returns:  mappingName and structurePath of the variable’s initial value

Return type:  dict[str, str]

Deprecated since version 2021.1: Method is deprecated. Use GetInitialValue instead.

GetInitialTextTableValue()[¶](#ApiClient.BooleanVariable.GetInitialTextTableValue "Link to this definition")  
Returns the initial value of the variable or None if it is not a Texttable.

Returns:  Initial value of the variable

Return type:  list[str]

Deprecated since version 2021.1: Method is deprecated. Use GetEntries instead.

GetInitialValueType()[¶](#ApiClient.BooleanVariable.GetInitialValueType "Link to this definition")  
Returns the type of the initial value of the variable.

Returns:  type of the initial value

Return type:  str

Deprecated since version 2021.1: Method is deprecated. Use GetType instead.

SetInitialBooleanValue(*value*)[¶](#ApiClient.BooleanVariable.SetInitialBooleanValue "Link to this definition")  
Sets the initial value of the variable.

Parameters:  **value** (*bool*) – Initial value of the variable

Deprecated since version 2021.1: Method is deprecated. Use SetInitialValue instead.

SetInitialFunctionValue(*code*)[¶](#ApiClient.BooleanVariable.SetInitialFunctionValue "Link to this definition")  
Sets the code of the Function.

Parameters:  **code** (*string*) – Python code to be executed

Deprecated since version 2021.1: Method is deprecated. Use SetInitialValue instead.

SetInitialNumericValue(*value*)[¶](#ApiClient.BooleanVariable.SetInitialNumericValue "Link to this definition")  
Sets the initial value of the variable.

Only the numeric value itself will be stored, not the way it has been typed in (e.g. in hex, or with additional zeroes).

Parameters:  **value** (*int/float*) – Initial value of the variable

Deprecated since version 2021.1: Method is deprecated. Use SetInitialValue instead.

SetInitialNumericValueString(*value*)[¶](#ApiClient.BooleanVariable.SetInitialNumericValueString "Link to this definition")  
Sets the initial value of the variable as string.

The string will be stored exactly as typed (e.g. in hex, or with additional zeroes).

Parameters:  **value** (*str*) – Initial value of the variable

Deprecated since version 2021.1: Method is only supported for numeric variable type in future versions.

SetInitialPyObjectValue(*value*)[¶](#ApiClient.BooleanVariable.SetInitialPyObjectValue "Link to this definition")  
Sets the initial value of the variable.

Parameters:  **value** (*string*) – May only consist of the following Python literal structures: strings, numbers, tuples, lists, dicts, booleans, and None.

Deprecated since version 2021.1: Method is deprecated. Use SetInitialValue instead.

SetInitialStringValue(*value*)[¶](#ApiClient.BooleanVariable.SetInitialStringValue "Link to this definition")  
Sets the initial value of the variable.

Parameters:  **value** (*string*) – Initial value of the variable

Deprecated since version 2021.1: Method is deprecated. Use SetInitialValue instead.

SetInitialStructureValue(*mappingName*, *structurePath*)[¶](#ApiClient.BooleanVariable.SetInitialStructureValue "Link to this definition")  
Sets the initial value of the variable.

Parameters:  - **mappingName** (*str*) – Mapping name to be assigned to the structure variable

- **structurePath** (*str*) – path inside the structure

Deprecated since version 2021.1: Method is deprecated. Use SetInitialValue instead.

SetInitialTextTableValue(*value*, *defaultValue*)[¶](#ApiClient.BooleanVariable.SetInitialTextTableValue "Link to this definition")  
Sets the initial value of the variable.

Parameters:  - **value** (*list[str]*) – A list of strings.

- **defaultValue** (*str*) – The string which should be used as the current value.

Deprecated since version 2021.1: Method is deprecated. Use AddEntry instead.

## DynamicEnumVariable[¶](#dynamicenumvariable "Link to this heading")

*class* DynamicEnumVariable[¶](#ApiClient.DynamicEnumVariable "Link to this definition")  
Base class

[`Variable`](#ApiClient.Variable "ApiClient.Variable")

Returned by

- [`VariableApi.CreateDynamicEnumVariable`](#ApiClient.VariableApi.CreateDynamicEnumVariable "ApiClient.VariableApi.CreateDynamicEnumVariable")

Clone()[¶](#ApiClient.DynamicEnumVariable.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`DynamicEnumVariable`](#ApiClient.DynamicEnumVariable "ApiClient.DynamicEnumVariable")

GetDescription()[¶](#ApiClient.DynamicEnumVariable.GetDescription "Link to this definition")  
Returns the description of the variable.

Returns:  Description of variable

Return type:  str

GetExpression()[¶](#ApiClient.DynamicEnumVariable.GetExpression "Link to this definition")  
Returns the expression that is used for the Enum variable.

Returns:  Enum expression

Return type:  str

GetInitialText()[¶](#ApiClient.DynamicEnumVariable.GetInitialText "Link to this definition")  
Returns the initial text of the variable. For dynamic Enums the initial text always corresponds to the first element of the evaluated expression or an empty string if no expression is given.

Returns:  The initial text of the variable

Return type:  str

GetInitialValue()[¶](#ApiClient.DynamicEnumVariable.GetInitialValue "Link to this definition")  
Returns the initial value of the enum. For dynamic Texttables the initial numeric value always corresponds to the first element of the evaluated expression or 0 if no expression is given.

Returns:  The initial value of the enum

Return type:  int

GetName()[¶](#ApiClient.DynamicEnumVariable.GetName "Link to this definition")  
Returns the name of the variable.

Returns:  Name of variable

Return type:  str

GetType()[¶](#ApiClient.DynamicEnumVariable.GetType "Link to this definition")  
Returns the type of the initial value of the variable.

Returns:  type of the initial value

Return type:  str

IsParameter()[¶](#ApiClient.DynamicEnumVariable.IsParameter "Link to this definition")  
Returns whether the variable is a parameter.

Returns:  True if parameter, else False

Return type:  boolean

IsRecorded()[¶](#ApiClient.DynamicEnumVariable.IsRecorded "Link to this definition")  
Returns whether the variable is recorded during execution.

Returns:  True if recorded, else False

Return type:  boolean

IsReturn()[¶](#ApiClient.DynamicEnumVariable.IsReturn "Link to this definition")  
Returns whether the variable is a return value.

Returns:  True if return value, else False

Return type:  boolean

SetDescription(*description*)[¶](#ApiClient.DynamicEnumVariable.SetDescription "Link to this definition")  
Sets the description of the variable.

Parameters:  **description** (*str*) – Description of variable

SetExpression(*expression*)[¶](#ApiClient.DynamicEnumVariable.SetExpression "Link to this definition")  
Sets the expression that is used to generate the list of strings for the Enum variable.

Parameters:  **expression** (*str*) – Expression that evaluates to a list of strings

SetParameter(*enable=True*)[¶](#ApiClient.DynamicEnumVariable.SetParameter "Link to this definition")  
Sets whether the variable is a parameter or not.

Parameters:  **enable** (*boolean*) – Whether the variable is a parameter or not

SetRecorded(*enable=True*)[¶](#ApiClient.DynamicEnumVariable.SetRecorded "Link to this definition")  
Sets the recording state of the variable to the value of enable.

Parameters:  **enable** (*boolean*) – Whether to enable the recording of the variable

SetReturn(*enable=True*)[¶](#ApiClient.DynamicEnumVariable.SetReturn "Link to this definition")  
Sets whether the variable is a return value or not.

Parameters:  **enable** (*boolean*) – Whether the variable is a return value or not

GetInitialBooleanValue()[¶](#ApiClient.DynamicEnumVariable.GetInitialBooleanValue "Link to this definition")  
Returns the initial value of the variable or None if it is not a Boolean.

Returns:  Initial value of the variable

Return type:  bool

Deprecated since version 2021.1: Method is deprecated. Use GetInitialValue instead.

GetInitialFunctionValue()[¶](#ApiClient.DynamicEnumVariable.GetInitialFunctionValue "Link to this definition")  
Returns the code of the function variable or None if it is not a function variable.

Returns:  Initial code of the function variable

Return type:  string

Deprecated since version 2021.1: Method is deprecated. Use GetInitialValue instead.

GetInitialNumericValue()[¶](#ApiClient.DynamicEnumVariable.GetInitialNumericValue "Link to this definition")  
Returns the initial value of the variable or None if it is not a Numeric.

Returns:  Initial value of the variable

Return type:  int/float

Deprecated since version 2021.1: Method is deprecated. Use GetInitialValue instead.

GetInitialNumericValueString()[¶](#ApiClient.DynamicEnumVariable.GetInitialNumericValueString "Link to this definition")  
Returns the initial value string of the variable, or None if it is not a Numeric.

The initial value is returned exactly as it has been typed in (e.g. in hex, or with additional zeroes), unless it has been set via [`SetInitialNumericValue()`](#ApiClient.DynamicEnumVariable.SetInitialNumericValue "ApiClient.DynamicEnumVariable.SetInitialNumericValue"), which stores only the numeric value itself.

Returns:  Initial value of the variable

Return type:  str

Deprecated since version 2021.1: Method is only supported for numeric variable type in future versions.

GetInitialPyObjectValue()[¶](#ApiClient.DynamicEnumVariable.GetInitialPyObjectValue "Link to this definition")  
Returns the initial value of the variable or None if it is not a PyObject.

Returns:  Initial value of the variable

Return type:  str

Deprecated since version 2021.1: Method is deprecated. Use GetInitialValue instead.

GetInitialStringValue()[¶](#ApiClient.DynamicEnumVariable.GetInitialStringValue "Link to this definition")  
Returns the initial value of the variable or None if it is not a String.

Returns:  Initial value of the variable

Return type:  str

Deprecated since version 2021.1: Method is deprecated. Use GetInitialValue instead.

GetInitialStructureValue()[¶](#ApiClient.DynamicEnumVariable.GetInitialStructureValue "Link to this definition")  
Returns the type of the initial value of the variable or None if it is not a structure.

Returns:  mappingName and structurePath of the variable’s initial value

Return type:  dict[str, str]

Deprecated since version 2021.1: Method is deprecated. Use GetInitialValue instead.

GetInitialTextTableValue()[¶](#ApiClient.DynamicEnumVariable.GetInitialTextTableValue "Link to this definition")  
Returns the initial value of the variable or None if it is not a Texttable.

Returns:  Initial value of the variable

Return type:  list[str]

Deprecated since version 2021.1: Method is deprecated. Use GetEntries instead.

GetInitialValueType()[¶](#ApiClient.DynamicEnumVariable.GetInitialValueType "Link to this definition")  
Returns the type of the initial value of the variable.

Returns:  type of the initial value

Return type:  str

Deprecated since version 2021.1: Method is deprecated. Use GetType instead.

SetInitialBooleanValue(*value*)[¶](#ApiClient.DynamicEnumVariable.SetInitialBooleanValue "Link to this definition")  
Sets the initial value of the variable.

Parameters:  **value** (*bool*) – Initial value of the variable

Deprecated since version 2021.1: Method is deprecated. Use SetInitialValue instead.

SetInitialFunctionValue(*code*)[¶](#ApiClient.DynamicEnumVariable.SetInitialFunctionValue "Link to this definition")  
Sets the code of the Function.

Parameters:  **code** (*string*) – Python code to be executed

Deprecated since version 2021.1: Method is deprecated. Use SetInitialValue instead.

SetInitialNumericValue(*value*)[¶](#ApiClient.DynamicEnumVariable.SetInitialNumericValue "Link to this definition")  
Sets the initial value of the variable.

Only the numeric value itself will be stored, not the way it has been typed in (e.g. in hex, or with additional zeroes).

Parameters:  **value** (*int/float*) – Initial value of the variable

Deprecated since version 2021.1: Method is deprecated. Use SetInitialValue instead.

SetInitialNumericValueString(*value*)[¶](#ApiClient.DynamicEnumVariable.SetInitialNumericValueString "Link to this definition")  
Sets the initial value of the variable as string.

The string will be stored exactly as typed (e.g. in hex, or with additional zeroes).

Parameters:  **value** (*str*) – Initial value of the variable

Deprecated since version 2021.1: Method is only supported for numeric variable type in future versions.

SetInitialPyObjectValue(*value*)[¶](#ApiClient.DynamicEnumVariable.SetInitialPyObjectValue "Link to this definition")  
Sets the initial value of the variable.

Parameters:  **value** (*string*) – May only consist of the following Python literal structures: strings, numbers, tuples, lists, dicts, booleans, and None.

Deprecated since version 2021.1: Method is deprecated. Use SetInitialValue instead.

SetInitialStringValue(*value*)[¶](#ApiClient.DynamicEnumVariable.SetInitialStringValue "Link to this definition")  
Sets the initial value of the variable.

Parameters:  **value** (*string*) – Initial value of the variable

Deprecated since version 2021.1: Method is deprecated. Use SetInitialValue instead.

SetInitialStructureValue(*mappingName*, *structurePath*)[¶](#ApiClient.DynamicEnumVariable.SetInitialStructureValue "Link to this definition")  
Sets the initial value of the variable.

Parameters:  - **mappingName** (*str*) – Mapping name to be assigned to the structure variable

- **structurePath** (*str*) – path inside the structure

Deprecated since version 2021.1: Method is deprecated. Use SetInitialValue instead.

SetInitialTextTableValue(*value*, *defaultValue*)[¶](#ApiClient.DynamicEnumVariable.SetInitialTextTableValue "Link to this definition")  
Sets the initial value of the variable.

Parameters:  - **value** (*list[str]*) – A list of strings.

- **defaultValue** (*str*) – The string which should be used as the current value.

Deprecated since version 2021.1: Method is deprecated. Use AddEntry instead.

## DynamicTextTableVariable[¶](#dynamictexttablevariable "Link to this heading")

*class* DynamicTextTableVariable[¶](#ApiClient.DynamicTextTableVariable "Link to this definition")  
Base class

[`Variable`](#ApiClient.Variable "ApiClient.Variable")

Returned by

- [`VariableApi.CreateDynamicTextTableVariable`](#ApiClient.VariableApi.CreateDynamicTextTableVariable "ApiClient.VariableApi.CreateDynamicTextTableVariable")

Clone()[¶](#ApiClient.DynamicTextTableVariable.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`DynamicTextTableVariable`](#ApiClient.DynamicTextTableVariable "ApiClient.DynamicTextTableVariable")

GetDescription()[¶](#ApiClient.DynamicTextTableVariable.GetDescription "Link to this definition")  
Returns the description of the variable.

Returns:  Description of variable

Return type:  str

GetExpression()[¶](#ApiClient.DynamicTextTableVariable.GetExpression "Link to this definition")  
Returns the expression that is used for the Texttable variable.

Returns:  Texttable expression

Return type:  str

GetInitialValue()[¶](#ApiClient.DynamicTextTableVariable.GetInitialValue "Link to this definition")  
Returns the initial value of the Texttable variable. For dynamic Texttables the initial value always corresponds to the first element of the evaluated expression or an empty string if no expression is given.

Returns:  The initial value of the Texttable

Return type:  str

GetName()[¶](#ApiClient.DynamicTextTableVariable.GetName "Link to this definition")  
Returns the name of the variable.

Returns:  Name of variable

Return type:  str

GetType()[¶](#ApiClient.DynamicTextTableVariable.GetType "Link to this definition")  
Returns the type of the initial value of the variable.

Returns:  type of the initial value

Return type:  str

IsParameter()[¶](#ApiClient.DynamicTextTableVariable.IsParameter "Link to this definition")  
Returns whether the variable is a parameter.

Returns:  True if parameter, else False

Return type:  boolean

IsRecorded()[¶](#ApiClient.DynamicTextTableVariable.IsRecorded "Link to this definition")  
Returns whether the variable is recorded during execution.

Returns:  True if recorded, else False

Return type:  boolean

IsReturn()[¶](#ApiClient.DynamicTextTableVariable.IsReturn "Link to this definition")  
Returns whether the variable is a return value.

Returns:  True if return value, else False

Return type:  boolean

SetDescription(*description*)[¶](#ApiClient.DynamicTextTableVariable.SetDescription "Link to this definition")  
Sets the description of the variable.

Parameters:  **description** (*str*) – Description of variable

SetExpression(*expression*)[¶](#ApiClient.DynamicTextTableVariable.SetExpression "Link to this definition")  
Sets the expression that is used to generate the list of strings for the Texttable variable.

Parameters:  **expression** (*str*) – Expression that evaluates to a list of strings

SetParameter(*enable=True*)[¶](#ApiClient.DynamicTextTableVariable.SetParameter "Link to this definition")  
Sets whether the variable is a parameter or not.

Parameters:  **enable** (*boolean*) – Whether the variable is a parameter or not

SetRecorded(*enable=True*)[¶](#ApiClient.DynamicTextTableVariable.SetRecorded "Link to this definition")  
Sets the recording state of the variable to the value of enable.

Parameters:  **enable** (*boolean*) – Whether to enable the recording of the variable

SetReturn(*enable=True*)[¶](#ApiClient.DynamicTextTableVariable.SetReturn "Link to this definition")  
Sets whether the variable is a return value or not.

Parameters:  **enable** (*boolean*) – Whether the variable is a return value or not

GetInitialBooleanValue()[¶](#ApiClient.DynamicTextTableVariable.GetInitialBooleanValue "Link to this definition")  
Returns the initial value of the variable or None if it is not a Boolean.

Returns:  Initial value of the variable

Return type:  bool

Deprecated since version 2021.1: Method is deprecated. Use GetInitialValue instead.

GetInitialFunctionValue()[¶](#ApiClient.DynamicTextTableVariable.GetInitialFunctionValue "Link to this definition")  
Returns the code of the function variable or None if it is not a function variable.

Returns:  Initial code of the function variable

Return type:  string

Deprecated since version 2021.1: Method is deprecated. Use GetInitialValue instead.

GetInitialNumericValue()[¶](#ApiClient.DynamicTextTableVariable.GetInitialNumericValue "Link to this definition")  
Returns the initial value of the variable or None if it is not a Numeric.

Returns:  Initial value of the variable

Return type:  int/float

Deprecated since version 2021.1: Method is deprecated. Use GetInitialValue instead.

GetInitialNumericValueString()[¶](#ApiClient.DynamicTextTableVariable.GetInitialNumericValueString "Link to this definition")  
Returns the initial value string of the variable, or None if it is not a Numeric.

The initial value is returned exactly as it has been typed in (e.g. in hex, or with additional zeroes), unless it has been set via [`SetInitialNumericValue()`](#ApiClient.DynamicTextTableVariable.SetInitialNumericValue "ApiClient.DynamicTextTableVariable.SetInitialNumericValue"), which stores only the numeric value itself.

Returns:  Initial value of the variable

Return type:  str

Deprecated since version 2021.1: Method is only supported for numeric variable type in future versions.

GetInitialPyObjectValue()[¶](#ApiClient.DynamicTextTableVariable.GetInitialPyObjectValue "Link to this definition")  
Returns the initial value of the variable or None if it is not a PyObject.

Returns:  Initial value of the variable

Return type:  str

Deprecated since version 2021.1: Method is deprecated. Use GetInitialValue instead.

GetInitialStringValue()[¶](#ApiClient.DynamicTextTableVariable.GetInitialStringValue "Link to this definition")  
Returns the initial value of the variable or None if it is not a String.

Returns:  Initial value of the variable

Return type:  str

Deprecated since version 2021.1: Method is deprecated. Use GetInitialValue instead.

GetInitialStructureValue()[¶](#ApiClient.DynamicTextTableVariable.GetInitialStructureValue "Link to this definition")  
Returns the type of the initial value of the variable or None if it is not a structure.

Returns:  mappingName and structurePath of the variable’s initial value

Return type:  dict[str, str]

Deprecated since version 2021.1: Method is deprecated. Use GetInitialValue instead.

GetInitialTextTableValue()[¶](#ApiClient.DynamicTextTableVariable.GetInitialTextTableValue "Link to this definition")  
Returns the initial value of the variable or None if it is not a Texttable.

Returns:  Initial value of the variable

Return type:  list[str]

Deprecated since version 2021.1: Method is deprecated. Use GetEntries instead.

GetInitialValueType()[¶](#ApiClient.DynamicTextTableVariable.GetInitialValueType "Link to this definition")  
Returns the type of the initial value of the variable.

Returns:  type of the initial value

Return type:  str

Deprecated since version 2021.1: Method is deprecated. Use GetType instead.

SetInitialBooleanValue(*value*)[¶](#ApiClient.DynamicTextTableVariable.SetInitialBooleanValue "Link to this definition")  
Sets the initial value of the variable.

Parameters:  **value** (*bool*) – Initial value of the variable

Deprecated since version 2021.1: Method is deprecated. Use SetInitialValue instead.

SetInitialFunctionValue(*code*)[¶](#ApiClient.DynamicTextTableVariable.SetInitialFunctionValue "Link to this definition")  
Sets the code of the Function.

Parameters:  **code** (*string*) – Python code to be executed

Deprecated since version 2021.1: Method is deprecated. Use SetInitialValue instead.

SetInitialNumericValue(*value*)[¶](#ApiClient.DynamicTextTableVariable.SetInitialNumericValue "Link to this definition")  
Sets the initial value of the variable.

Only the numeric value itself will be stored, not the way it has been typed in (e.g. in hex, or with additional zeroes).

Parameters:  **value** (*int/float*) – Initial value of the variable

Deprecated since version 2021.1: Method is deprecated. Use SetInitialValue instead.

SetInitialNumericValueString(*value*)[¶](#ApiClient.DynamicTextTableVariable.SetInitialNumericValueString "Link to this definition")  
Sets the initial value of the variable as string.

The string will be stored exactly as typed (e.g. in hex, or with additional zeroes).

Parameters:  **value** (*str*) – Initial value of the variable

Deprecated since version 2021.1: Method is only supported for numeric variable type in future versions.

SetInitialPyObjectValue(*value*)[¶](#ApiClient.DynamicTextTableVariable.SetInitialPyObjectValue "Link to this definition")  
Sets the initial value of the variable.

Parameters:  **value** (*string*) – May only consist of the following Python literal structures: strings, numbers, tuples, lists, dicts, booleans, and None.

Deprecated since version 2021.1: Method is deprecated. Use SetInitialValue instead.

SetInitialStringValue(*value*)[¶](#ApiClient.DynamicTextTableVariable.SetInitialStringValue "Link to this definition")  
Sets the initial value of the variable.

Parameters:  **value** (*string*) – Initial value of the variable

Deprecated since version 2021.1: Method is deprecated. Use SetInitialValue instead.

SetInitialStructureValue(*mappingName*, *structurePath*)[¶](#ApiClient.DynamicTextTableVariable.SetInitialStructureValue "Link to this definition")  
Sets the initial value of the variable.

Parameters:  - **mappingName** (*str*) – Mapping name to be assigned to the structure variable

- **structurePath** (*str*) – path inside the structure

Deprecated since version 2021.1: Method is deprecated. Use SetInitialValue instead.

SetInitialTextTableValue(*value*, *defaultValue*)[¶](#ApiClient.DynamicTextTableVariable.SetInitialTextTableValue "Link to this definition")  
Sets the initial value of the variable.

Parameters:  - **value** (*list[str]*) – A list of strings.

- **defaultValue** (*str*) – The string which should be used as the current value.

Deprecated since version 2021.1: Method is deprecated. Use AddEntry instead.

## EnumVariable[¶](#enumvariable "Link to this heading")

*class* EnumVariable[¶](#ApiClient.EnumVariable "Link to this definition")  
Base class

[`Variable`](#ApiClient.Variable "ApiClient.Variable")

Returned by

- [`VariableApi.CreateEnumVariable`](#ApiClient.VariableApi.CreateEnumVariable "ApiClient.VariableApi.CreateEnumVariable")

AddEntry(*value*, *text*)[¶](#ApiClient.EnumVariable.AddEntry "Link to this definition")  
Adds an entry to the Enum initial entries. Raises an exception if the value is already contained in the enum.

Parameters:  - **value** (*int*) – The value of the entry

- **text** (*str*) – The text of the entry

Returns:  The created enum

Return type:  [`EnumVariableElement`](#ApiClient.EnumVariableElement "ApiClient.EnumVariableElement")

Clone()[¶](#ApiClient.EnumVariable.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`EnumVariable`](#ApiClient.EnumVariable "ApiClient.EnumVariable")

GetDescription()[¶](#ApiClient.EnumVariable.GetDescription "Link to this definition")  
Returns the description of the variable.

Returns:  Description of variable

Return type:  str

GetEntries()[¶](#ApiClient.EnumVariable.GetEntries "Link to this definition")  
Returns the initial value of the variable or an empty list if it is not an Enum.

Returns:  Initial value of the variable

Return type:  list[[`EnumVariableElement`](#ApiClient.EnumVariableElement "ApiClient.EnumVariableElement")]

GetInitialText()[¶](#ApiClient.EnumVariable.GetInitialText "Link to this definition")  
Returns the initial text of the variable.

Returns:  The initial text of the variable

Return type:  str

GetInitialValue()[¶](#ApiClient.EnumVariable.GetInitialValue "Link to this definition")  
Returns the initial value of the enum.

Returns:  The initial value of the enum

Return type:  int

GetName()[¶](#ApiClient.EnumVariable.GetName "Link to this definition")  
Returns the name of the variable.

Returns:  Name of variable

Return type:  str

GetType()[¶](#ApiClient.EnumVariable.GetType "Link to this definition")  
Returns the type of the initial value of the variable.

Returns:  type of the initial value

Return type:  str

IsParameter()[¶](#ApiClient.EnumVariable.IsParameter "Link to this definition")  
Returns whether the variable is a parameter.

Returns:  True if parameter, else False

Return type:  boolean

IsRecorded()[¶](#ApiClient.EnumVariable.IsRecorded "Link to this definition")  
Returns whether the variable is recorded during execution.

Returns:  True if recorded, else False

Return type:  boolean

IsReturn()[¶](#ApiClient.EnumVariable.IsReturn "Link to this definition")  
Returns whether the variable is a return value.

Returns:  True if return value, else False

Return type:  boolean

RemoveEntry(*value*)[¶](#ApiClient.EnumVariable.RemoveEntry "Link to this definition")  
Deletes an entry from the enum.

Parameters:  **value** (*int*) – The value of the entry

SetDescription(*description*)[¶](#ApiClient.EnumVariable.SetDescription "Link to this definition")  
Sets the description of the variable.

Parameters:  **description** (*str*) – Description of variable

SetInitialValue(*value*)[¶](#ApiClient.EnumVariable.SetInitialValue "Link to this definition")  
Selects the initial value of the enum. The entry needs to be added by using AddEntry before.

Parameters:  **value** (*int*) – The number that should initially be used as the current value.

SetParameter(*enable=True*)[¶](#ApiClient.EnumVariable.SetParameter "Link to this definition")  
Sets whether the variable is a parameter or not.

Parameters:  **enable** (*boolean*) – Whether the variable is a parameter or not

SetRecorded(*enable=True*)[¶](#ApiClient.EnumVariable.SetRecorded "Link to this definition")  
Sets the recording state of the variable to the value of enable.

Parameters:  **enable** (*boolean*) – Whether to enable the recording of the variable

SetReturn(*enable=True*)[¶](#ApiClient.EnumVariable.SetReturn "Link to this definition")  
Sets whether the variable is a return value or not.

Parameters:  **enable** (*boolean*) – Whether the variable is a return value or not

GetInitialBooleanValue()[¶](#ApiClient.EnumVariable.GetInitialBooleanValue "Link to this definition")  
Returns the initial value of the variable or None if it is not a Boolean.

Returns:  Initial value of the variable

Return type:  bool

Deprecated since version 2021.1: Method is deprecated. Use GetInitialValue instead.

GetInitialFunctionValue()[¶](#ApiClient.EnumVariable.GetInitialFunctionValue "Link to this definition")  
Returns the code of the function variable or None if it is not a function variable.

Returns:  Initial code of the function variable

Return type:  string

Deprecated since version 2021.1: Method is deprecated. Use GetInitialValue instead.

GetInitialNumericValue()[¶](#ApiClient.EnumVariable.GetInitialNumericValue "Link to this definition")  
Returns the initial value of the variable or None if it is not a Numeric.

Returns:  Initial value of the variable

Return type:  int/float

Deprecated since version 2021.1: Method is deprecated. Use GetInitialValue instead.

GetInitialNumericValueString()[¶](#ApiClient.EnumVariable.GetInitialNumericValueString "Link to this definition")  
Returns the initial value string of the variable, or None if it is not a Numeric.

The initial value is returned exactly as it has been typed in (e.g. in hex, or with additional zeroes), unless it has been set via [`SetInitialNumericValue()`](#ApiClient.EnumVariable.SetInitialNumericValue "ApiClient.EnumVariable.SetInitialNumericValue"), which stores only the numeric value itself.

Returns:  Initial value of the variable

Return type:  str

Deprecated since version 2021.1: Method is only supported for numeric variable type in future versions.

GetInitialPyObjectValue()[¶](#ApiClient.EnumVariable.GetInitialPyObjectValue "Link to this definition")  
Returns the initial value of the variable or None if it is not a PyObject.

Returns:  Initial value of the variable

Return type:  str

Deprecated since version 2021.1: Method is deprecated. Use GetInitialValue instead.

GetInitialStringValue()[¶](#ApiClient.EnumVariable.GetInitialStringValue "Link to this definition")  
Returns the initial value of the variable or None if it is not a String.

Returns:  Initial value of the variable

Return type:  str

Deprecated since version 2021.1: Method is deprecated. Use GetInitialValue instead.

GetInitialStructureValue()[¶](#ApiClient.EnumVariable.GetInitialStructureValue "Link to this definition")  
Returns the type of the initial value of the variable or None if it is not a structure.

Returns:  mappingName and structurePath of the variable’s initial value

Return type:  dict[str, str]

Deprecated since version 2021.1: Method is deprecated. Use GetInitialValue instead.

GetInitialTextTableValue()[¶](#ApiClient.EnumVariable.GetInitialTextTableValue "Link to this definition")  
Returns the initial value of the variable or None if it is not a Texttable.

Returns:  Initial value of the variable

Return type:  list[str]

Deprecated since version 2021.1: Method is deprecated. Use GetEntries instead.

GetInitialValueType()[¶](#ApiClient.EnumVariable.GetInitialValueType "Link to this definition")  
Returns the type of the initial value of the variable.

Returns:  type of the initial value

Return type:  str

Deprecated since version 2021.1: Method is deprecated. Use GetType instead.

SetInitialBooleanValue(*value*)[¶](#ApiClient.EnumVariable.SetInitialBooleanValue "Link to this definition")  
Sets the initial value of the variable.

Parameters:  **value** (*bool*) – Initial value of the variable

Deprecated since version 2021.1: Method is deprecated. Use SetInitialValue instead.

SetInitialFunctionValue(*code*)[¶](#ApiClient.EnumVariable.SetInitialFunctionValue "Link to this definition")  
Sets the code of the Function.

Parameters:  **code** (*string*) – Python code to be executed

Deprecated since version 2021.1: Method is deprecated. Use SetInitialValue instead.

SetInitialNumericValue(*value*)[¶](#ApiClient.EnumVariable.SetInitialNumericValue "Link to this definition")  
Sets the initial value of the variable.

Only the numeric value itself will be stored, not the way it has been typed in (e.g. in hex, or with additional zeroes).

Parameters:  **value** (*int/float*) – Initial value of the variable

Deprecated since version 2021.1: Method is deprecated. Use SetInitialValue instead.

SetInitialNumericValueString(*value*)[¶](#ApiClient.EnumVariable.SetInitialNumericValueString "Link to this definition")  
Sets the initial value of the variable as string.

The string will be stored exactly as typed (e.g. in hex, or with additional zeroes).

Parameters:  **value** (*str*) – Initial value of the variable

Deprecated since version 2021.1: Method is only supported for numeric variable type in future versions.

SetInitialPyObjectValue(*value*)[¶](#ApiClient.EnumVariable.SetInitialPyObjectValue "Link to this definition")  
Sets the initial value of the variable.

Parameters:  **value** (*string*) – May only consist of the following Python literal structures: strings, numbers, tuples, lists, dicts, booleans, and None.

Deprecated since version 2021.1: Method is deprecated. Use SetInitialValue instead.

SetInitialStringValue(*value*)[¶](#ApiClient.EnumVariable.SetInitialStringValue "Link to this definition")  
Sets the initial value of the variable.

Parameters:  **value** (*string*) – Initial value of the variable

Deprecated since version 2021.1: Method is deprecated. Use SetInitialValue instead.

SetInitialStructureValue(*mappingName*, *structurePath*)[¶](#ApiClient.EnumVariable.SetInitialStructureValue "Link to this definition")  
Sets the initial value of the variable.

Parameters:  - **mappingName** (*str*) – Mapping name to be assigned to the structure variable

- **structurePath** (*str*) – path inside the structure

Deprecated since version 2021.1: Method is deprecated. Use SetInitialValue instead.

SetInitialTextTableValue(*value*, *defaultValue*)[¶](#ApiClient.EnumVariable.SetInitialTextTableValue "Link to this definition")  
Sets the initial value of the variable.

Parameters:  - **value** (*list[str]*) – A list of strings.

- **defaultValue** (*str*) – The string which should be used as the current value.

Deprecated since version 2021.1: Method is deprecated. Use AddEntry instead.

## EnumVariableElement[¶](#enumvariableelement "Link to this heading")

*class* EnumVariableElement[¶](#ApiClient.EnumVariableElement "Link to this definition")  
Returned by

- [`EnumVariable.AddEntry`](#ApiClient.EnumVariable.AddEntry "ApiClient.EnumVariable.AddEntry")

- [`EnumVariable.GetEntries`](#ApiClient.EnumVariable.GetEntries "ApiClient.EnumVariable.GetEntries")

Clone()[¶](#ApiClient.EnumVariableElement.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`EnumVariableElement`](#ApiClient.EnumVariableElement "ApiClient.EnumVariableElement")

GetText()[¶](#ApiClient.EnumVariableElement.GetText "Link to this definition")  
Returns the text of the entry.

Returns:  The text of the entry

Return type:  str

GetValue()[¶](#ApiClient.EnumVariableElement.GetValue "Link to this definition")  
Returns the value of the entry.

Returns:  The value of the entry

Return type:  int

## FunctionVariable[¶](#functionvariable "Link to this heading")

*class* FunctionVariable[¶](#ApiClient.FunctionVariable "Link to this definition")  
Base class

[`Variable`](#ApiClient.Variable "ApiClient.Variable")

Returned by

- [`VariableApi.CreateFunctionVariable`](#ApiClient.VariableApi.CreateFunctionVariable "ApiClient.VariableApi.CreateFunctionVariable")

Clone()[¶](#ApiClient.FunctionVariable.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`FunctionVariable`](#ApiClient.FunctionVariable "ApiClient.FunctionVariable")

GetDescription()[¶](#ApiClient.FunctionVariable.GetDescription "Link to this definition")  
Returns the description of the variable.

Returns:  Description of variable

Return type:  str

GetInitialValue()[¶](#ApiClient.FunctionVariable.GetInitialValue "Link to this definition")  
Returns the code of the function variable or None if it is not a function variable.

Returns:  Initial code of the function variable

Return type:  string

GetName()[¶](#ApiClient.FunctionVariable.GetName "Link to this definition")  
Returns the name of the variable.

Returns:  Name of variable

Return type:  str

GetType()[¶](#ApiClient.FunctionVariable.GetType "Link to this definition")  
Returns the type of the initial value of the variable.

Returns:  type of the initial value

Return type:  str

IsParameter()[¶](#ApiClient.FunctionVariable.IsParameter "Link to this definition")  
Returns whether the variable is a parameter.

Returns:  True if parameter, else False

Return type:  boolean

IsRecorded()[¶](#ApiClient.FunctionVariable.IsRecorded "Link to this definition")  
Returns whether the variable is recorded during execution.

Returns:  True if recorded, else False

Return type:  boolean

IsReturn()[¶](#ApiClient.FunctionVariable.IsReturn "Link to this definition")  
Returns whether the variable is a return value.

Returns:  True if return value, else False

Return type:  boolean

SetDescription(*description*)[¶](#ApiClient.FunctionVariable.SetDescription "Link to this definition")  
Sets the description of the variable.

Parameters:  **description** (*str*) – Description of variable

SetInitialValue(*value*)[¶](#ApiClient.FunctionVariable.SetInitialValue "Link to this definition")  
Sets the code of the Function.

Parameters:  **value** (*string*) – Python code to be executed

SetParameter(*enable=True*)[¶](#ApiClient.FunctionVariable.SetParameter "Link to this definition")  
Sets whether the variable is a parameter or not.

Parameters:  **enable** (*boolean*) – Whether the variable is a parameter or not

SetRecorded(*enable=True*)[¶](#ApiClient.FunctionVariable.SetRecorded "Link to this definition")  
Sets the recording state of the variable to the value of enable.

Parameters:  **enable** (*boolean*) – Whether to enable the recording of the variable

SetReturn(*enable=True*)[¶](#ApiClient.FunctionVariable.SetReturn "Link to this definition")  
Sets whether the variable is a return value or not.

Parameters:  **enable** (*boolean*) – Whether the variable is a return value or not

GetInitialBooleanValue()[¶](#ApiClient.FunctionVariable.GetInitialBooleanValue "Link to this definition")  
Returns the initial value of the variable or None if it is not a Boolean.

Returns:  Initial value of the variable

Return type:  bool

Deprecated since version 2021.1: Method is deprecated. Use GetInitialValue instead.

GetInitialFunctionValue()[¶](#ApiClient.FunctionVariable.GetInitialFunctionValue "Link to this definition")  
Returns the code of the function variable or None if it is not a function variable.

Returns:  Initial code of the function variable

Return type:  string

Deprecated since version 2021.1: Method is deprecated. Use GetInitialValue instead.

GetInitialNumericValue()[¶](#ApiClient.FunctionVariable.GetInitialNumericValue "Link to this definition")  
Returns the initial value of the variable or None if it is not a Numeric.

Returns:  Initial value of the variable

Return type:  int/float

Deprecated since version 2021.1: Method is deprecated. Use GetInitialValue instead.

GetInitialNumericValueString()[¶](#ApiClient.FunctionVariable.GetInitialNumericValueString "Link to this definition")  
Returns the initial value string of the variable, or None if it is not a Numeric.

The initial value is returned exactly as it has been typed in (e.g. in hex, or with additional zeroes), unless it has been set via [`SetInitialNumericValue()`](#ApiClient.FunctionVariable.SetInitialNumericValue "ApiClient.FunctionVariable.SetInitialNumericValue"), which stores only the numeric value itself.

Returns:  Initial value of the variable

Return type:  str

Deprecated since version 2021.1: Method is only supported for numeric variable type in future versions.

GetInitialPyObjectValue()[¶](#ApiClient.FunctionVariable.GetInitialPyObjectValue "Link to this definition")  
Returns the initial value of the variable or None if it is not a PyObject.

Returns:  Initial value of the variable

Return type:  str

Deprecated since version 2021.1: Method is deprecated. Use GetInitialValue instead.

GetInitialStringValue()[¶](#ApiClient.FunctionVariable.GetInitialStringValue "Link to this definition")  
Returns the initial value of the variable or None if it is not a String.

Returns:  Initial value of the variable

Return type:  str

Deprecated since version 2021.1: Method is deprecated. Use GetInitialValue instead.

GetInitialStructureValue()[¶](#ApiClient.FunctionVariable.GetInitialStructureValue "Link to this definition")  
Returns the type of the initial value of the variable or None if it is not a structure.

Returns:  mappingName and structurePath of the variable’s initial value

Return type:  dict[str, str]

Deprecated since version 2021.1: Method is deprecated. Use GetInitialValue instead.

GetInitialTextTableValue()[¶](#ApiClient.FunctionVariable.GetInitialTextTableValue "Link to this definition")  
Returns the initial value of the variable or None if it is not a Texttable.

Returns:  Initial value of the variable

Return type:  list[str]

Deprecated since version 2021.1: Method is deprecated. Use GetEntries instead.

GetInitialValueType()[¶](#ApiClient.FunctionVariable.GetInitialValueType "Link to this definition")  
Returns the type of the initial value of the variable.

Returns:  type of the initial value

Return type:  str

Deprecated since version 2021.1: Method is deprecated. Use GetType instead.

SetInitialBooleanValue(*value*)[¶](#ApiClient.FunctionVariable.SetInitialBooleanValue "Link to this definition")  
Sets the initial value of the variable.

Parameters:  **value** (*bool*) – Initial value of the variable

Deprecated since version 2021.1: Method is deprecated. Use SetInitialValue instead.

SetInitialFunctionValue(*code*)[¶](#ApiClient.FunctionVariable.SetInitialFunctionValue "Link to this definition")  
Sets the code of the Function.

Parameters:  **code** (*string*) – Python code to be executed

Deprecated since version 2021.1: Method is deprecated. Use SetInitialValue instead.

SetInitialNumericValue(*value*)[¶](#ApiClient.FunctionVariable.SetInitialNumericValue "Link to this definition")  
Sets the initial value of the variable.

Only the numeric value itself will be stored, not the way it has been typed in (e.g. in hex, or with additional zeroes).

Parameters:  **value** (*int/float*) – Initial value of the variable

Deprecated since version 2021.1: Method is deprecated. Use SetInitialValue instead.

SetInitialNumericValueString(*value*)[¶](#ApiClient.FunctionVariable.SetInitialNumericValueString "Link to this definition")  
Sets the initial value of the variable as string.

The string will be stored exactly as typed (e.g. in hex, or with additional zeroes).

Parameters:  **value** (*str*) – Initial value of the variable

Deprecated since version 2021.1: Method is only supported for numeric variable type in future versions.

SetInitialPyObjectValue(*value*)[¶](#ApiClient.FunctionVariable.SetInitialPyObjectValue "Link to this definition")  
Sets the initial value of the variable.

Parameters:  **value** (*string*) – May only consist of the following Python literal structures: strings, numbers, tuples, lists, dicts, booleans, and None.

Deprecated since version 2021.1: Method is deprecated. Use SetInitialValue instead.

SetInitialStringValue(*value*)[¶](#ApiClient.FunctionVariable.SetInitialStringValue "Link to this definition")  
Sets the initial value of the variable.

Parameters:  **value** (*string*) – Initial value of the variable

Deprecated since version 2021.1: Method is deprecated. Use SetInitialValue instead.

SetInitialStructureValue(*mappingName*, *structurePath*)[¶](#ApiClient.FunctionVariable.SetInitialStructureValue "Link to this definition")  
Sets the initial value of the variable.

Parameters:  - **mappingName** (*str*) – Mapping name to be assigned to the structure variable

- **structurePath** (*str*) – path inside the structure

Deprecated since version 2021.1: Method is deprecated. Use SetInitialValue instead.

SetInitialTextTableValue(*value*, *defaultValue*)[¶](#ApiClient.FunctionVariable.SetInitialTextTableValue "Link to this definition")  
Sets the initial value of the variable.

Parameters:  - **value** (*list[str]*) – A list of strings.

- **defaultValue** (*str*) – The string which should be used as the current value.

Deprecated since version 2021.1: Method is deprecated. Use AddEntry instead.

## NumericVariable[¶](#numericvariable "Link to this heading")

*class* NumericVariable[¶](#ApiClient.NumericVariable "Link to this definition")  
Base class

[`Variable`](#ApiClient.Variable "ApiClient.Variable")

Returned by

- [`VariableApi.CreateNumericVariable`](#ApiClient.VariableApi.CreateNumericVariable "ApiClient.VariableApi.CreateNumericVariable")

Clone()[¶](#ApiClient.NumericVariable.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`NumericVariable`](#ApiClient.NumericVariable "ApiClient.NumericVariable")

GetDescription()[¶](#ApiClient.NumericVariable.GetDescription "Link to this definition")  
Returns the description of the variable.

Returns:  Description of variable

Return type:  str

GetInitialNumericValueString()[¶](#ApiClient.NumericVariable.GetInitialNumericValueString "Link to this definition")  
Returns the initial value string of the variable, or None if it is not a Numeric.

The initial value is returned exactly as it has been typed in (e.g. in hex, or with additional zeroes), unless it has been set via [`SetInitialNumericValue()`](#ApiClient.NumericVariable.SetInitialNumericValue "ApiClient.NumericVariable.SetInitialNumericValue"), which stores only the numeric value itself.

Returns:  Initial value of the variable

Return type:  str

GetInitialValue()[¶](#ApiClient.NumericVariable.GetInitialValue "Link to this definition")  
Returns the initial value of the variable or None if it is not a Numeric.

Returns:  Initial value of the variable

Return type:  int/float

GetName()[¶](#ApiClient.NumericVariable.GetName "Link to this definition")  
Returns the name of the variable.

Returns:  Name of variable

Return type:  str

GetType()[¶](#ApiClient.NumericVariable.GetType "Link to this definition")  
Returns the type of the initial value of the variable.

Returns:  type of the initial value

Return type:  str

IsParameter()[¶](#ApiClient.NumericVariable.IsParameter "Link to this definition")  
Returns whether the variable is a parameter.

Returns:  True if parameter, else False

Return type:  boolean

IsRecorded()[¶](#ApiClient.NumericVariable.IsRecorded "Link to this definition")  
Returns whether the variable is recorded during execution.

Returns:  True if recorded, else False

Return type:  boolean

IsReturn()[¶](#ApiClient.NumericVariable.IsReturn "Link to this definition")  
Returns whether the variable is a return value.

Returns:  True if return value, else False

Return type:  boolean

SetDescription(*description*)[¶](#ApiClient.NumericVariable.SetDescription "Link to this definition")  
Sets the description of the variable.

Parameters:  **description** (*str*) – Description of variable

SetInitialNumericValueString(*value*)[¶](#ApiClient.NumericVariable.SetInitialNumericValueString "Link to this definition")  
Sets the initial value of the variable as string.

The string will be stored exactly as typed (e.g. in hex, or with additional zeroes).

Parameters:  **value** (*str*) – Initial value of the variable

SetInitialValue(*value*)[¶](#ApiClient.NumericVariable.SetInitialValue "Link to this definition")  
Sets the initial value of the variable.

Only the numeric value itself will be stored, not the way it has been typed in (e.g. in hex, or with additional zeroes).

Parameters:  **value** (*int/float*) – Initial value of the variable

SetParameter(*enable=True*)[¶](#ApiClient.NumericVariable.SetParameter "Link to this definition")  
Sets whether the variable is a parameter or not.

Parameters:  **enable** (*boolean*) – Whether the variable is a parameter or not

SetRecorded(*enable=True*)[¶](#ApiClient.NumericVariable.SetRecorded "Link to this definition")  
Sets the recording state of the variable to the value of enable.

Parameters:  **enable** (*boolean*) – Whether to enable the recording of the variable

SetReturn(*enable=True*)[¶](#ApiClient.NumericVariable.SetReturn "Link to this definition")  
Sets whether the variable is a return value or not.

Parameters:  **enable** (*boolean*) – Whether the variable is a return value or not

GetInitialBooleanValue()[¶](#ApiClient.NumericVariable.GetInitialBooleanValue "Link to this definition")  
Returns the initial value of the variable or None if it is not a Boolean.

Returns:  Initial value of the variable

Return type:  bool

Deprecated since version 2021.1: Method is deprecated. Use GetInitialValue instead.

GetInitialFunctionValue()[¶](#ApiClient.NumericVariable.GetInitialFunctionValue "Link to this definition")  
Returns the code of the function variable or None if it is not a function variable.

Returns:  Initial code of the function variable

Return type:  string

Deprecated since version 2021.1: Method is deprecated. Use GetInitialValue instead.

GetInitialNumericValue()[¶](#ApiClient.NumericVariable.GetInitialNumericValue "Link to this definition")  
Returns the initial value of the variable or None if it is not a Numeric.

Returns:  Initial value of the variable

Return type:  int/float

Deprecated since version 2021.1: Method is deprecated. Use GetInitialValue instead.

GetInitialPyObjectValue()[¶](#ApiClient.NumericVariable.GetInitialPyObjectValue "Link to this definition")  
Returns the initial value of the variable or None if it is not a PyObject.

Returns:  Initial value of the variable

Return type:  str

Deprecated since version 2021.1: Method is deprecated. Use GetInitialValue instead.

GetInitialStringValue()[¶](#ApiClient.NumericVariable.GetInitialStringValue "Link to this definition")  
Returns the initial value of the variable or None if it is not a String.

Returns:  Initial value of the variable

Return type:  str

Deprecated since version 2021.1: Method is deprecated. Use GetInitialValue instead.

GetInitialStructureValue()[¶](#ApiClient.NumericVariable.GetInitialStructureValue "Link to this definition")  
Returns the type of the initial value of the variable or None if it is not a structure.

Returns:  mappingName and structurePath of the variable’s initial value

Return type:  dict[str, str]

Deprecated since version 2021.1: Method is deprecated. Use GetInitialValue instead.

GetInitialTextTableValue()[¶](#ApiClient.NumericVariable.GetInitialTextTableValue "Link to this definition")  
Returns the initial value of the variable or None if it is not a Texttable.

Returns:  Initial value of the variable

Return type:  list[str]

Deprecated since version 2021.1: Method is deprecated. Use GetEntries instead.

GetInitialValueType()[¶](#ApiClient.NumericVariable.GetInitialValueType "Link to this definition")  
Returns the type of the initial value of the variable.

Returns:  type of the initial value

Return type:  str

Deprecated since version 2021.1: Method is deprecated. Use GetType instead.

SetInitialBooleanValue(*value*)[¶](#ApiClient.NumericVariable.SetInitialBooleanValue "Link to this definition")  
Sets the initial value of the variable.

Parameters:  **value** (*bool*) – Initial value of the variable

Deprecated since version 2021.1: Method is deprecated. Use SetInitialValue instead.

SetInitialFunctionValue(*code*)[¶](#ApiClient.NumericVariable.SetInitialFunctionValue "Link to this definition")  
Sets the code of the Function.

Parameters:  **code** (*string*) – Python code to be executed

Deprecated since version 2021.1: Method is deprecated. Use SetInitialValue instead.

SetInitialNumericValue(*value*)[¶](#ApiClient.NumericVariable.SetInitialNumericValue "Link to this definition")  
Sets the initial value of the variable.

Only the numeric value itself will be stored, not the way it has been typed in (e.g. in hex, or with additional zeroes).

Parameters:  **value** (*int/float*) – Initial value of the variable

Deprecated since version 2021.1: Method is deprecated. Use SetInitialValue instead.

SetInitialPyObjectValue(*value*)[¶](#ApiClient.NumericVariable.SetInitialPyObjectValue "Link to this definition")  
Sets the initial value of the variable.

Parameters:  **value** (*string*) – May only consist of the following Python literal structures: strings, numbers, tuples, lists, dicts, booleans, and None.

Deprecated since version 2021.1: Method is deprecated. Use SetInitialValue instead.

SetInitialStringValue(*value*)[¶](#ApiClient.NumericVariable.SetInitialStringValue "Link to this definition")  
Sets the initial value of the variable.

Parameters:  **value** (*string*) – Initial value of the variable

Deprecated since version 2021.1: Method is deprecated. Use SetInitialValue instead.

SetInitialStructureValue(*mappingName*, *structurePath*)[¶](#ApiClient.NumericVariable.SetInitialStructureValue "Link to this definition")  
Sets the initial value of the variable.

Parameters:  - **mappingName** (*str*) – Mapping name to be assigned to the structure variable

- **structurePath** (*str*) – path inside the structure

Deprecated since version 2021.1: Method is deprecated. Use SetInitialValue instead.

SetInitialTextTableValue(*value*, *defaultValue*)[¶](#ApiClient.NumericVariable.SetInitialTextTableValue "Link to this definition")  
Sets the initial value of the variable.

Parameters:  - **value** (*list[str]*) – A list of strings.

- **defaultValue** (*str*) – The string which should be used as the current value.

Deprecated since version 2021.1: Method is deprecated. Use AddEntry instead.

## PyObjectVariable[¶](#pyobjectvariable "Link to this heading")

*class* PyObjectVariable[¶](#ApiClient.PyObjectVariable "Link to this definition")  
Base class

[`Variable`](#ApiClient.Variable "ApiClient.Variable")

Returned by

- [`VariableApi.CreatePyObjectVariable`](#ApiClient.VariableApi.CreatePyObjectVariable "ApiClient.VariableApi.CreatePyObjectVariable")

Clone()[¶](#ApiClient.PyObjectVariable.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`PyObjectVariable`](#ApiClient.PyObjectVariable "ApiClient.PyObjectVariable")

GetDescription()[¶](#ApiClient.PyObjectVariable.GetDescription "Link to this definition")  
Returns the description of the variable.

Returns:  Description of variable

Return type:  str

GetInitialValue()[¶](#ApiClient.PyObjectVariable.GetInitialValue "Link to this definition")  
Returns the initial value of the variable or None if it is not a PyObject.

Returns:  Initial value of the variable

Return type:  str

GetName()[¶](#ApiClient.PyObjectVariable.GetName "Link to this definition")  
Returns the name of the variable.

Returns:  Name of variable

Return type:  str

GetType()[¶](#ApiClient.PyObjectVariable.GetType "Link to this definition")  
Returns the type of the initial value of the variable.

Returns:  type of the initial value

Return type:  str

IsParameter()[¶](#ApiClient.PyObjectVariable.IsParameter "Link to this definition")  
Returns whether the variable is a parameter.

Returns:  True if parameter, else False

Return type:  boolean

IsRecorded()[¶](#ApiClient.PyObjectVariable.IsRecorded "Link to this definition")  
Returns whether the variable is recorded during execution.

Returns:  True if recorded, else False

Return type:  boolean

IsReturn()[¶](#ApiClient.PyObjectVariable.IsReturn "Link to this definition")  
Returns whether the variable is a return value.

Returns:  True if return value, else False

Return type:  boolean

SetDescription(*description*)[¶](#ApiClient.PyObjectVariable.SetDescription "Link to this definition")  
Sets the description of the variable.

Parameters:  **description** (*str*) – Description of variable

SetInitialValue(*value*)[¶](#ApiClient.PyObjectVariable.SetInitialValue "Link to this definition")  
Sets the initial value of the variable.

Parameters:  **value** (*string*) – May only consist of the following Python literal structures: strings, numbers, tuples, lists, dicts, booleans, and None

SetParameter(*enable=True*)[¶](#ApiClient.PyObjectVariable.SetParameter "Link to this definition")  
Sets whether the variable is a parameter or not.

Parameters:  **enable** (*boolean*) – Whether the variable is a parameter or not

SetRecorded(*enable=True*)[¶](#ApiClient.PyObjectVariable.SetRecorded "Link to this definition")  
Sets the recording state of the variable to the value of enable.

Parameters:  **enable** (*boolean*) – Whether to enable the recording of the variable

SetReturn(*enable=True*)[¶](#ApiClient.PyObjectVariable.SetReturn "Link to this definition")  
Sets whether the variable is a return value or not.

Parameters:  **enable** (*boolean*) – Whether the variable is a return value or not

GetInitialBooleanValue()[¶](#ApiClient.PyObjectVariable.GetInitialBooleanValue "Link to this definition")  
Returns the initial value of the variable or None if it is not a Boolean.

Returns:  Initial value of the variable

Return type:  bool

Deprecated since version 2021.1: Method is deprecated. Use GetInitialValue instead.

GetInitialFunctionValue()[¶](#ApiClient.PyObjectVariable.GetInitialFunctionValue "Link to this definition")  
Returns the code of the function variable or None if it is not a function variable.

Returns:  Initial code of the function variable

Return type:  string

Deprecated since version 2021.1: Method is deprecated. Use GetInitialValue instead.

GetInitialNumericValue()[¶](#ApiClient.PyObjectVariable.GetInitialNumericValue "Link to this definition")  
Returns the initial value of the variable or None if it is not a Numeric.

Returns:  Initial value of the variable

Return type:  int/float

Deprecated since version 2021.1: Method is deprecated. Use GetInitialValue instead.

GetInitialNumericValueString()[¶](#ApiClient.PyObjectVariable.GetInitialNumericValueString "Link to this definition")  
Returns the initial value string of the variable, or None if it is not a Numeric.

The initial value is returned exactly as it has been typed in (e.g. in hex, or with additional zeroes), unless it has been set via [`SetInitialNumericValue()`](#ApiClient.PyObjectVariable.SetInitialNumericValue "ApiClient.PyObjectVariable.SetInitialNumericValue"), which stores only the numeric value itself.

Returns:  Initial value of the variable

Return type:  str

Deprecated since version 2021.1: Method is only supported for numeric variable type in future versions.

GetInitialPyObjectValue()[¶](#ApiClient.PyObjectVariable.GetInitialPyObjectValue "Link to this definition")  
Returns the initial value of the variable or None if it is not a PyObject.

Returns:  Initial value of the variable

Return type:  str

Deprecated since version 2021.1: Method is deprecated. Use GetInitialValue instead.

GetInitialStringValue()[¶](#ApiClient.PyObjectVariable.GetInitialStringValue "Link to this definition")  
Returns the initial value of the variable or None if it is not a String.

Returns:  Initial value of the variable

Return type:  str

Deprecated since version 2021.1: Method is deprecated. Use GetInitialValue instead.

GetInitialStructureValue()[¶](#ApiClient.PyObjectVariable.GetInitialStructureValue "Link to this definition")  
Returns the type of the initial value of the variable or None if it is not a structure.

Returns:  mappingName and structurePath of the variable’s initial value

Return type:  dict[str, str]

Deprecated since version 2021.1: Method is deprecated. Use GetInitialValue instead.

GetInitialTextTableValue()[¶](#ApiClient.PyObjectVariable.GetInitialTextTableValue "Link to this definition")  
Returns the initial value of the variable or None if it is not a Texttable.

Returns:  Initial value of the variable

Return type:  list[str]

Deprecated since version 2021.1: Method is deprecated. Use GetEntries instead.

GetInitialValueType()[¶](#ApiClient.PyObjectVariable.GetInitialValueType "Link to this definition")  
Returns the type of the initial value of the variable.

Returns:  type of the initial value

Return type:  str

Deprecated since version 2021.1: Method is deprecated. Use GetType instead.

SetInitialBooleanValue(*value*)[¶](#ApiClient.PyObjectVariable.SetInitialBooleanValue "Link to this definition")  
Sets the initial value of the variable.

Parameters:  **value** (*bool*) – Initial value of the variable

Deprecated since version 2021.1: Method is deprecated. Use SetInitialValue instead.

SetInitialFunctionValue(*code*)[¶](#ApiClient.PyObjectVariable.SetInitialFunctionValue "Link to this definition")  
Sets the code of the Function.

Parameters:  **code** (*string*) – Python code to be executed

Deprecated since version 2021.1: Method is deprecated. Use SetInitialValue instead.

SetInitialNumericValue(*value*)[¶](#ApiClient.PyObjectVariable.SetInitialNumericValue "Link to this definition")  
Sets the initial value of the variable.

Only the numeric value itself will be stored, not the way it has been typed in (e.g. in hex, or with additional zeroes).

Parameters:  **value** (*int/float*) – Initial value of the variable

Deprecated since version 2021.1: Method is deprecated. Use SetInitialValue instead.

SetInitialNumericValueString(*value*)[¶](#ApiClient.PyObjectVariable.SetInitialNumericValueString "Link to this definition")  
Sets the initial value of the variable as string.

The string will be stored exactly as typed (e.g. in hex, or with additional zeroes).

Parameters:  **value** (*str*) – Initial value of the variable

Deprecated since version 2021.1: Method is only supported for numeric variable type in future versions.

SetInitialPyObjectValue(*value*)[¶](#ApiClient.PyObjectVariable.SetInitialPyObjectValue "Link to this definition")  
Sets the initial value of the variable.

Parameters:  **value** (*string*) – May only consist of the following Python literal structures: strings, numbers, tuples, lists, dicts, booleans, and None.

Deprecated since version 2021.1: Method is deprecated. Use SetInitialValue instead.

SetInitialStringValue(*value*)[¶](#ApiClient.PyObjectVariable.SetInitialStringValue "Link to this definition")  
Sets the initial value of the variable.

Parameters:  **value** (*string*) – Initial value of the variable

Deprecated since version 2021.1: Method is deprecated. Use SetInitialValue instead.

SetInitialStructureValue(*mappingName*, *structurePath*)[¶](#ApiClient.PyObjectVariable.SetInitialStructureValue "Link to this definition")  
Sets the initial value of the variable.

Parameters:  - **mappingName** (*str*) – Mapping name to be assigned to the structure variable

- **structurePath** (*str*) – path inside the structure

Deprecated since version 2021.1: Method is deprecated. Use SetInitialValue instead.

SetInitialTextTableValue(*value*, *defaultValue*)[¶](#ApiClient.PyObjectVariable.SetInitialTextTableValue "Link to this definition")  
Sets the initial value of the variable.

Parameters:  - **value** (*list[str]*) – A list of strings.

- **defaultValue** (*str*) – The string which should be used as the current value.

Deprecated since version 2021.1: Method is deprecated. Use AddEntry instead.

## StaticTextTableVariable[¶](#statictexttablevariable "Link to this heading")

*class* StaticTextTableVariable[¶](#ApiClient.StaticTextTableVariable "Link to this definition")  
Base class

[`Variable`](#ApiClient.Variable "ApiClient.Variable")

Returned by

- [`VariableApi.CreateStaticTextTableVariable`](#ApiClient.VariableApi.CreateStaticTextTableVariable "ApiClient.VariableApi.CreateStaticTextTableVariable")

AddEntry(*value*)[¶](#ApiClient.StaticTextTableVariable.AddEntry "Link to this definition")  
Adds an entry to the Texttable.

Parameters:  **value** (*str*) – The new entry

Clone()[¶](#ApiClient.StaticTextTableVariable.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`StaticTextTableVariable`](#ApiClient.StaticTextTableVariable "ApiClient.StaticTextTableVariable")

GetDescription()[¶](#ApiClient.StaticTextTableVariable.GetDescription "Link to this definition")  
Returns the description of the variable.

Returns:  Description of variable

Return type:  str

GetEntries()[¶](#ApiClient.StaticTextTableVariable.GetEntries "Link to this definition")  
Returns all entries of the Texttable.

Returns:  All Entries of the Texttable.

Return type:  list[str]

GetEntry(*index*)[¶](#ApiClient.StaticTextTableVariable.GetEntry "Link to this definition")  
Returns the value at a specific index of the Texttable.

Parameters:  **index** (*int*) – Index of the entry whose value is to be set

Returns:  value at the given index

Return type:  str

GetInitialValue()[¶](#ApiClient.StaticTextTableVariable.GetInitialValue "Link to this definition")  
Returns the initial value of the Texttable.

Returns:  The initial value of the Texttable

Return type:  str

GetName()[¶](#ApiClient.StaticTextTableVariable.GetName "Link to this definition")  
Returns the name of the variable.

Returns:  Name of variable

Return type:  str

GetType()[¶](#ApiClient.StaticTextTableVariable.GetType "Link to this definition")  
Returns the type of the initial value of the variable.

Returns:  type of the initial value

Return type:  str

IsParameter()[¶](#ApiClient.StaticTextTableVariable.IsParameter "Link to this definition")  
Returns whether the variable is a parameter.

Returns:  True if parameter, else False

Return type:  boolean

IsRecorded()[¶](#ApiClient.StaticTextTableVariable.IsRecorded "Link to this definition")  
Returns whether the variable is recorded during execution.

Returns:  True if recorded, else False

Return type:  boolean

IsReturn()[¶](#ApiClient.StaticTextTableVariable.IsReturn "Link to this definition")  
Returns whether the variable is a return value.

Returns:  True if return value, else False

Return type:  boolean

RemoveEntry(*index*)[¶](#ApiClient.StaticTextTableVariable.RemoveEntry "Link to this definition")  
Removes an entry from the Texttable.

Parameters:  **index** (*int*) – Index of the entry to remove

SetDescription(*description*)[¶](#ApiClient.StaticTextTableVariable.SetDescription "Link to this definition")  
Sets the description of the variable.

Parameters:  **description** (*str*) – Description of variable

SetEntry(*index*, *value*)[¶](#ApiClient.StaticTextTableVariable.SetEntry "Link to this definition")  
Sets the value at a specific index in the Texttable.

Parameters:  - **index** (*int*) – Index of the entry whose value is to be set

- **value** (*str*) – new value

SetInitialValue(*value*)[¶](#ApiClient.StaticTextTableVariable.SetInitialValue "Link to this definition")  
Sets the initial value of the Texttable.

Parameters:  **value** (*str*) – The initial value of the Texttable.

SetParameter(*enable=True*)[¶](#ApiClient.StaticTextTableVariable.SetParameter "Link to this definition")  
Sets whether the variable is a parameter or not.

Parameters:  **enable** (*boolean*) – Whether the variable is a parameter or not

SetRecorded(*enable=True*)[¶](#ApiClient.StaticTextTableVariable.SetRecorded "Link to this definition")  
Sets the recording state of the variable to the value of enable.

Parameters:  **enable** (*boolean*) – Whether to enable the recording of the variable

SetReturn(*enable=True*)[¶](#ApiClient.StaticTextTableVariable.SetReturn "Link to this definition")  
Sets whether the variable is a return value or not.

Parameters:  **enable** (*boolean*) – Whether the variable is a return value or not

GetInitialBooleanValue()[¶](#ApiClient.StaticTextTableVariable.GetInitialBooleanValue "Link to this definition")  
Returns the initial value of the variable or None if it is not a Boolean.

Returns:  Initial value of the variable

Return type:  bool

Deprecated since version 2021.1: Method is deprecated. Use GetInitialValue instead.

GetInitialFunctionValue()[¶](#ApiClient.StaticTextTableVariable.GetInitialFunctionValue "Link to this definition")  
Returns the code of the function variable or None if it is not a function variable.

Returns:  Initial code of the function variable

Return type:  string

Deprecated since version 2021.1: Method is deprecated. Use GetInitialValue instead.

GetInitialNumericValue()[¶](#ApiClient.StaticTextTableVariable.GetInitialNumericValue "Link to this definition")  
Returns the initial value of the variable or None if it is not a Numeric.

Returns:  Initial value of the variable

Return type:  int/float

Deprecated since version 2021.1: Method is deprecated. Use GetInitialValue instead.

GetInitialNumericValueString()[¶](#ApiClient.StaticTextTableVariable.GetInitialNumericValueString "Link to this definition")  
Returns the initial value string of the variable, or None if it is not a Numeric.

The initial value is returned exactly as it has been typed in (e.g. in hex, or with additional zeroes), unless it has been set via [`SetInitialNumericValue()`](#ApiClient.StaticTextTableVariable.SetInitialNumericValue "ApiClient.StaticTextTableVariable.SetInitialNumericValue"), which stores only the numeric value itself.

Returns:  Initial value of the variable

Return type:  str

Deprecated since version 2021.1: Method is only supported for numeric variable type in future versions.

GetInitialPyObjectValue()[¶](#ApiClient.StaticTextTableVariable.GetInitialPyObjectValue "Link to this definition")  
Returns the initial value of the variable or None if it is not a PyObject.

Returns:  Initial value of the variable

Return type:  str

Deprecated since version 2021.1: Method is deprecated. Use GetInitialValue instead.

GetInitialStringValue()[¶](#ApiClient.StaticTextTableVariable.GetInitialStringValue "Link to this definition")  
Returns the initial value of the variable or None if it is not a String.

Returns:  Initial value of the variable

Return type:  str

Deprecated since version 2021.1: Method is deprecated. Use GetInitialValue instead.

GetInitialStructureValue()[¶](#ApiClient.StaticTextTableVariable.GetInitialStructureValue "Link to this definition")  
Returns the type of the initial value of the variable or None if it is not a structure.

Returns:  mappingName and structurePath of the variable’s initial value

Return type:  dict[str, str]

Deprecated since version 2021.1: Method is deprecated. Use GetInitialValue instead.

GetInitialTextTableValue()[¶](#ApiClient.StaticTextTableVariable.GetInitialTextTableValue "Link to this definition")  
Returns the initial value of the variable or None if it is not a Texttable.

Returns:  Initial value of the variable

Return type:  list[str]

Deprecated since version 2021.1: Method is deprecated. Use GetEntries instead.

GetInitialValueType()[¶](#ApiClient.StaticTextTableVariable.GetInitialValueType "Link to this definition")  
Returns the type of the initial value of the variable.

Returns:  type of the initial value

Return type:  str

Deprecated since version 2021.1: Method is deprecated. Use GetType instead.

SetInitialBooleanValue(*value*)[¶](#ApiClient.StaticTextTableVariable.SetInitialBooleanValue "Link to this definition")  
Sets the initial value of the variable.

Parameters:  **value** (*bool*) – Initial value of the variable

Deprecated since version 2021.1: Method is deprecated. Use SetInitialValue instead.

SetInitialFunctionValue(*code*)[¶](#ApiClient.StaticTextTableVariable.SetInitialFunctionValue "Link to this definition")  
Sets the code of the Function.

Parameters:  **code** (*string*) – Python code to be executed

Deprecated since version 2021.1: Method is deprecated. Use SetInitialValue instead.

SetInitialNumericValue(*value*)[¶](#ApiClient.StaticTextTableVariable.SetInitialNumericValue "Link to this definition")  
Sets the initial value of the variable.

Only the numeric value itself will be stored, not the way it has been typed in (e.g. in hex, or with additional zeroes).

Parameters:  **value** (*int/float*) – Initial value of the variable

Deprecated since version 2021.1: Method is deprecated. Use SetInitialValue instead.

SetInitialNumericValueString(*value*)[¶](#ApiClient.StaticTextTableVariable.SetInitialNumericValueString "Link to this definition")  
Sets the initial value of the variable as string.

The string will be stored exactly as typed (e.g. in hex, or with additional zeroes).

Parameters:  **value** (*str*) – Initial value of the variable

Deprecated since version 2021.1: Method is only supported for numeric variable type in future versions.

SetInitialPyObjectValue(*value*)[¶](#ApiClient.StaticTextTableVariable.SetInitialPyObjectValue "Link to this definition")  
Sets the initial value of the variable.

Parameters:  **value** (*string*) – May only consist of the following Python literal structures: strings, numbers, tuples, lists, dicts, booleans, and None.

Deprecated since version 2021.1: Method is deprecated. Use SetInitialValue instead.

SetInitialStringValue(*value*)[¶](#ApiClient.StaticTextTableVariable.SetInitialStringValue "Link to this definition")  
Sets the initial value of the variable.

Parameters:  **value** (*string*) – Initial value of the variable

Deprecated since version 2021.1: Method is deprecated. Use SetInitialValue instead.

SetInitialStructureValue(*mappingName*, *structurePath*)[¶](#ApiClient.StaticTextTableVariable.SetInitialStructureValue "Link to this definition")  
Sets the initial value of the variable.

Parameters:  - **mappingName** (*str*) – Mapping name to be assigned to the structure variable

- **structurePath** (*str*) – path inside the structure

Deprecated since version 2021.1: Method is deprecated. Use SetInitialValue instead.

SetInitialTextTableValue(*value*, *defaultValue*)[¶](#ApiClient.StaticTextTableVariable.SetInitialTextTableValue "Link to this definition")  
Sets the initial value of the variable.

Parameters:  - **value** (*list[str]*) – A list of strings.

- **defaultValue** (*str*) – The string which should be used as the current value.

Deprecated since version 2021.1: Method is deprecated. Use AddEntry instead.

## StringVariable[¶](#stringvariable "Link to this heading")

*class* StringVariable[¶](#ApiClient.StringVariable "Link to this definition")  
Base class

[`Variable`](#ApiClient.Variable "ApiClient.Variable")

Returned by

- [`VariableApi.CreateStringVariable`](#ApiClient.VariableApi.CreateStringVariable "ApiClient.VariableApi.CreateStringVariable")

Clone()[¶](#ApiClient.StringVariable.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`StringVariable`](#ApiClient.StringVariable "ApiClient.StringVariable")

GetDescription()[¶](#ApiClient.StringVariable.GetDescription "Link to this definition")  
Returns the description of the variable.

Returns:  Description of variable

Return type:  str

GetInitialValue()[¶](#ApiClient.StringVariable.GetInitialValue "Link to this definition")  
Returns the initial value of the variable or None if it is not a String.

Returns:  Initial value of the variable

Return type:  str

GetName()[¶](#ApiClient.StringVariable.GetName "Link to this definition")  
Returns the name of the variable.

Returns:  Name of variable

Return type:  str

GetTranslatedInitialValue(*language*)[¶](#ApiClient.StringVariable.GetTranslatedInitialValue "Link to this definition")  
Returns the initial value of the variable for the specified language.

Returns:  Initial value of the variable

Return type:  str

Parameters:  **language** (*str*) – Language of the value (‘en_US’, ‘de_DE’, ‘zh_CN’)

GetType()[¶](#ApiClient.StringVariable.GetType "Link to this definition")  
Returns the type of the initial value of the variable.

Returns:  type of the initial value

Return type:  str

IsParameter()[¶](#ApiClient.StringVariable.IsParameter "Link to this definition")  
Returns whether the variable is a parameter.

Returns:  True if parameter, else False

Return type:  boolean

IsRecorded()[¶](#ApiClient.StringVariable.IsRecorded "Link to this definition")  
Returns whether the variable is recorded during execution.

Returns:  True if recorded, else False

Return type:  boolean

IsReturn()[¶](#ApiClient.StringVariable.IsReturn "Link to this definition")  
Returns whether the variable is a return value.

Returns:  True if return value, else False

Return type:  boolean

SetDescription(*description*)[¶](#ApiClient.StringVariable.SetDescription "Link to this definition")  
Sets the description of the variable.

Parameters:  **description** (*str*) – Description of variable

SetInitialValue(*value*)[¶](#ApiClient.StringVariable.SetInitialValue "Link to this definition")  
Sets the initial value of the variable.

Parameters:  **value** (*str*) – Initial value of the variable

SetParameter(*enable=True*)[¶](#ApiClient.StringVariable.SetParameter "Link to this definition")  
Sets whether the variable is a parameter or not.

Parameters:  **enable** (*boolean*) – Whether the variable is a parameter or not

SetRecorded(*enable=True*)[¶](#ApiClient.StringVariable.SetRecorded "Link to this definition")  
Sets the recording state of the variable to the value of enable.

Parameters:  **enable** (*boolean*) – Whether to enable the recording of the variable

SetReturn(*enable=True*)[¶](#ApiClient.StringVariable.SetReturn "Link to this definition")  
Sets whether the variable is a return value or not.

Parameters:  **enable** (*boolean*) – Whether the variable is a return value or not

SetTranslatedInitialValue(*value*, *language*)[¶](#ApiClient.StringVariable.SetTranslatedInitialValue "Link to this definition")  
Sets the initial value of the variable for the specified language.

Parameters:  - **value** (*str*) – Initial value of the variable

- **language** (*str*) – Language of the value (‘en_US’, ‘de_DE’, ‘zh_CN’)

GetInitialBooleanValue()[¶](#ApiClient.StringVariable.GetInitialBooleanValue "Link to this definition")  
Returns the initial value of the variable or None if it is not a Boolean.

Returns:  Initial value of the variable

Return type:  bool

Deprecated since version 2021.1: Method is deprecated. Use GetInitialValue instead.

GetInitialFunctionValue()[¶](#ApiClient.StringVariable.GetInitialFunctionValue "Link to this definition")  
Returns the code of the function variable or None if it is not a function variable.

Returns:  Initial code of the function variable

Return type:  string

Deprecated since version 2021.1: Method is deprecated. Use GetInitialValue instead.

GetInitialNumericValue()[¶](#ApiClient.StringVariable.GetInitialNumericValue "Link to this definition")  
Returns the initial value of the variable or None if it is not a Numeric.

Returns:  Initial value of the variable

Return type:  int/float

Deprecated since version 2021.1: Method is deprecated. Use GetInitialValue instead.

GetInitialNumericValueString()[¶](#ApiClient.StringVariable.GetInitialNumericValueString "Link to this definition")  
Returns the initial value string of the variable, or None if it is not a Numeric.

The initial value is returned exactly as it has been typed in (e.g. in hex, or with additional zeroes), unless it has been set via [`SetInitialNumericValue()`](#ApiClient.StringVariable.SetInitialNumericValue "ApiClient.StringVariable.SetInitialNumericValue"), which stores only the numeric value itself.

Returns:  Initial value of the variable

Return type:  str

Deprecated since version 2021.1: Method is only supported for numeric variable type in future versions.

GetInitialPyObjectValue()[¶](#ApiClient.StringVariable.GetInitialPyObjectValue "Link to this definition")  
Returns the initial value of the variable or None if it is not a PyObject.

Returns:  Initial value of the variable

Return type:  str

Deprecated since version 2021.1: Method is deprecated. Use GetInitialValue instead.

GetInitialStringValue()[¶](#ApiClient.StringVariable.GetInitialStringValue "Link to this definition")  
Returns the initial value of the variable or None if it is not a String.

Returns:  Initial value of the variable

Return type:  str

Deprecated since version 2021.1: Method is deprecated. Use GetInitialValue instead.

GetInitialStructureValue()[¶](#ApiClient.StringVariable.GetInitialStructureValue "Link to this definition")  
Returns the type of the initial value of the variable or None if it is not a structure.

Returns:  mappingName and structurePath of the variable’s initial value

Return type:  dict[str, str]

Deprecated since version 2021.1: Method is deprecated. Use GetInitialValue instead.

GetInitialTextTableValue()[¶](#ApiClient.StringVariable.GetInitialTextTableValue "Link to this definition")  
Returns the initial value of the variable or None if it is not a Texttable.

Returns:  Initial value of the variable

Return type:  list[str]

Deprecated since version 2021.1: Method is deprecated. Use GetEntries instead.

GetInitialValueType()[¶](#ApiClient.StringVariable.GetInitialValueType "Link to this definition")  
Returns the type of the initial value of the variable.

Returns:  type of the initial value

Return type:  str

Deprecated since version 2021.1: Method is deprecated. Use GetType instead.

SetInitialBooleanValue(*value*)[¶](#ApiClient.StringVariable.SetInitialBooleanValue "Link to this definition")  
Sets the initial value of the variable.

Parameters:  **value** (*bool*) – Initial value of the variable

Deprecated since version 2021.1: Method is deprecated. Use SetInitialValue instead.

SetInitialFunctionValue(*code*)[¶](#ApiClient.StringVariable.SetInitialFunctionValue "Link to this definition")  
Sets the code of the Function.

Parameters:  **code** (*string*) – Python code to be executed

Deprecated since version 2021.1: Method is deprecated. Use SetInitialValue instead.

SetInitialNumericValue(*value*)[¶](#ApiClient.StringVariable.SetInitialNumericValue "Link to this definition")  
Sets the initial value of the variable.

Only the numeric value itself will be stored, not the way it has been typed in (e.g. in hex, or with additional zeroes).

Parameters:  **value** (*int/float*) – Initial value of the variable

Deprecated since version 2021.1: Method is deprecated. Use SetInitialValue instead.

SetInitialNumericValueString(*value*)[¶](#ApiClient.StringVariable.SetInitialNumericValueString "Link to this definition")  
Sets the initial value of the variable as string.

The string will be stored exactly as typed (e.g. in hex, or with additional zeroes).

Parameters:  **value** (*str*) – Initial value of the variable

Deprecated since version 2021.1: Method is only supported for numeric variable type in future versions.

SetInitialPyObjectValue(*value*)[¶](#ApiClient.StringVariable.SetInitialPyObjectValue "Link to this definition")  
Sets the initial value of the variable.

Parameters:  **value** (*string*) – May only consist of the following Python literal structures: strings, numbers, tuples, lists, dicts, booleans, and None.

Deprecated since version 2021.1: Method is deprecated. Use SetInitialValue instead.

SetInitialStringValue(*value*)[¶](#ApiClient.StringVariable.SetInitialStringValue "Link to this definition")  
Sets the initial value of the variable.

Parameters:  **value** (*string*) – Initial value of the variable

Deprecated since version 2021.1: Method is deprecated. Use SetInitialValue instead.

SetInitialStructureValue(*mappingName*, *structurePath*)[¶](#ApiClient.StringVariable.SetInitialStructureValue "Link to this definition")  
Sets the initial value of the variable.

Parameters:  - **mappingName** (*str*) – Mapping name to be assigned to the structure variable

- **structurePath** (*str*) – path inside the structure

Deprecated since version 2021.1: Method is deprecated. Use SetInitialValue instead.

SetInitialTextTableValue(*value*, *defaultValue*)[¶](#ApiClient.StringVariable.SetInitialTextTableValue "Link to this definition")  
Sets the initial value of the variable.

Parameters:  - **value** (*list[str]*) – A list of strings.

- **defaultValue** (*str*) – The string which should be used as the current value.

Deprecated since version 2021.1: Method is deprecated. Use AddEntry instead.

## StructureVariable[¶](#structurevariable "Link to this heading")

*class* StructureVariable[¶](#ApiClient.StructureVariable "Link to this definition")  
Base class

[`Variable`](#ApiClient.Variable "ApiClient.Variable")

Returned by

- [`VariableApi.CreateStructureVariable`](#ApiClient.VariableApi.CreateStructureVariable "ApiClient.VariableApi.CreateStructureVariable")

Clone()[¶](#ApiClient.StructureVariable.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`StructureVariable`](#ApiClient.StructureVariable "ApiClient.StructureVariable")

GetDescription()[¶](#ApiClient.StructureVariable.GetDescription "Link to this definition")  
Returns the description of the variable.

Returns:  Description of variable

Return type:  str

GetInitialValue()[¶](#ApiClient.StructureVariable.GetInitialValue "Link to this definition")  
Returns the type of the initial value of the variable or None if it is not a structure.

Returns:  mappingName and structurePath of the variable’s initial value

Return type:  dict[str, str]

GetName()[¶](#ApiClient.StructureVariable.GetName "Link to this definition")  
Returns the name of the variable.

Returns:  Name of variable

Return type:  str

GetType()[¶](#ApiClient.StructureVariable.GetType "Link to this definition")  
Returns the type of the initial value of the variable.

Returns:  type of the initial value

Return type:  str

IsParameter()[¶](#ApiClient.StructureVariable.IsParameter "Link to this definition")  
Returns whether the variable is a parameter.

Returns:  True if parameter, else False

Return type:  boolean

IsRecorded()[¶](#ApiClient.StructureVariable.IsRecorded "Link to this definition")  
Returns whether the variable is recorded during execution.

Returns:  True if recorded, else False

Return type:  boolean

IsReturn()[¶](#ApiClient.StructureVariable.IsReturn "Link to this definition")  
Returns whether the variable is a return value.

Returns:  True if return value, else False

Return type:  boolean

SetDescription(*description*)[¶](#ApiClient.StructureVariable.SetDescription "Link to this definition")  
Sets the description of the variable.

Parameters:  **description** (*str*) – Description of variable

SetInitialValue(*mappingName*, *structurePath*)[¶](#ApiClient.StructureVariable.SetInitialValue "Link to this definition")  
Sets the initial value of the variable.

Parameters:  - **mappingName** (*str*) – Mapping name to be assigned to the structure variable

- **structurePath** (*str*) – path inside the structure

SetParameter(*enable=True*)[¶](#ApiClient.StructureVariable.SetParameter "Link to this definition")  
Sets whether the variable is a parameter or not.

Parameters:  **enable** (*boolean*) – Whether the variable is a parameter or not

SetRecorded(*enable=True*)[¶](#ApiClient.StructureVariable.SetRecorded "Link to this definition")  
Sets the recording state of the variable to the value of enable.

Parameters:  **enable** (*boolean*) – Whether to enable the recording of the variable

SetReturn(*enable=True*)[¶](#ApiClient.StructureVariable.SetReturn "Link to this definition")  
Sets whether the variable is a return value or not.

Parameters:  **enable** (*boolean*) – Whether the variable is a return value or not

GetInitialBooleanValue()[¶](#ApiClient.StructureVariable.GetInitialBooleanValue "Link to this definition")  
Returns the initial value of the variable or None if it is not a Boolean.

Returns:  Initial value of the variable

Return type:  bool

Deprecated since version 2021.1: Method is deprecated. Use GetInitialValue instead.

GetInitialFunctionValue()[¶](#ApiClient.StructureVariable.GetInitialFunctionValue "Link to this definition")  
Returns the code of the function variable or None if it is not a function variable.

Returns:  Initial code of the function variable

Return type:  string

Deprecated since version 2021.1: Method is deprecated. Use GetInitialValue instead.

GetInitialNumericValue()[¶](#ApiClient.StructureVariable.GetInitialNumericValue "Link to this definition")  
Returns the initial value of the variable or None if it is not a Numeric.

Returns:  Initial value of the variable

Return type:  int/float

Deprecated since version 2021.1: Method is deprecated. Use GetInitialValue instead.

GetInitialNumericValueString()[¶](#ApiClient.StructureVariable.GetInitialNumericValueString "Link to this definition")  
Returns the initial value string of the variable, or None if it is not a Numeric.

The initial value is returned exactly as it has been typed in (e.g. in hex, or with additional zeroes), unless it has been set via [`SetInitialNumericValue()`](#ApiClient.StructureVariable.SetInitialNumericValue "ApiClient.StructureVariable.SetInitialNumericValue"), which stores only the numeric value itself.

Returns:  Initial value of the variable

Return type:  str

Deprecated since version 2021.1: Method is only supported for numeric variable type in future versions.

GetInitialPyObjectValue()[¶](#ApiClient.StructureVariable.GetInitialPyObjectValue "Link to this definition")  
Returns the initial value of the variable or None if it is not a PyObject.

Returns:  Initial value of the variable

Return type:  str

Deprecated since version 2021.1: Method is deprecated. Use GetInitialValue instead.

GetInitialStringValue()[¶](#ApiClient.StructureVariable.GetInitialStringValue "Link to this definition")  
Returns the initial value of the variable or None if it is not a String.

Returns:  Initial value of the variable

Return type:  str

Deprecated since version 2021.1: Method is deprecated. Use GetInitialValue instead.

GetInitialStructureValue()[¶](#ApiClient.StructureVariable.GetInitialStructureValue "Link to this definition")  
Returns the type of the initial value of the variable or None if it is not a structure.

Returns:  mappingName and structurePath of the variable’s initial value

Return type:  dict[str, str]

Deprecated since version 2021.1: Method is deprecated. Use GetInitialValue instead.

GetInitialTextTableValue()[¶](#ApiClient.StructureVariable.GetInitialTextTableValue "Link to this definition")  
Returns the initial value of the variable or None if it is not a Texttable.

Returns:  Initial value of the variable

Return type:  list[str]

Deprecated since version 2021.1: Method is deprecated. Use GetEntries instead.

GetInitialValueType()[¶](#ApiClient.StructureVariable.GetInitialValueType "Link to this definition")  
Returns the type of the initial value of the variable.

Returns:  type of the initial value

Return type:  str

Deprecated since version 2021.1: Method is deprecated. Use GetType instead.

SetInitialBooleanValue(*value*)[¶](#ApiClient.StructureVariable.SetInitialBooleanValue "Link to this definition")  
Sets the initial value of the variable.

Parameters:  **value** (*bool*) – Initial value of the variable

Deprecated since version 2021.1: Method is deprecated. Use SetInitialValue instead.

SetInitialFunctionValue(*code*)[¶](#ApiClient.StructureVariable.SetInitialFunctionValue "Link to this definition")  
Sets the code of the Function.

Parameters:  **code** (*string*) – Python code to be executed

Deprecated since version 2021.1: Method is deprecated. Use SetInitialValue instead.

SetInitialNumericValue(*value*)[¶](#ApiClient.StructureVariable.SetInitialNumericValue "Link to this definition")  
Sets the initial value of the variable.

Only the numeric value itself will be stored, not the way it has been typed in (e.g. in hex, or with additional zeroes).

Parameters:  **value** (*int/float*) – Initial value of the variable

Deprecated since version 2021.1: Method is deprecated. Use SetInitialValue instead.

SetInitialNumericValueString(*value*)[¶](#ApiClient.StructureVariable.SetInitialNumericValueString "Link to this definition")  
Sets the initial value of the variable as string.

The string will be stored exactly as typed (e.g. in hex, or with additional zeroes).

Parameters:  **value** (*str*) – Initial value of the variable

Deprecated since version 2021.1: Method is only supported for numeric variable type in future versions.

SetInitialPyObjectValue(*value*)[¶](#ApiClient.StructureVariable.SetInitialPyObjectValue "Link to this definition")  
Sets the initial value of the variable.

Parameters:  **value** (*string*) – May only consist of the following Python literal structures: strings, numbers, tuples, lists, dicts, booleans, and None.

Deprecated since version 2021.1: Method is deprecated. Use SetInitialValue instead.

SetInitialStringValue(*value*)[¶](#ApiClient.StructureVariable.SetInitialStringValue "Link to this definition")  
Sets the initial value of the variable.

Parameters:  **value** (*string*) – Initial value of the variable

Deprecated since version 2021.1: Method is deprecated. Use SetInitialValue instead.

SetInitialStructureValue(*mappingName*, *structurePath*)[¶](#ApiClient.StructureVariable.SetInitialStructureValue "Link to this definition")  
Sets the initial value of the variable.

Parameters:  - **mappingName** (*str*) – Mapping name to be assigned to the structure variable

- **structurePath** (*str*) – path inside the structure

Deprecated since version 2021.1: Method is deprecated. Use SetInitialValue instead.

SetInitialTextTableValue(*value*, *defaultValue*)[¶](#ApiClient.StructureVariable.SetInitialTextTableValue "Link to this definition")  
Sets the initial value of the variable.

Parameters:  - **value** (*list[str]*) – A list of strings.

- **defaultValue** (*str*) – The string which should be used as the current value.

Deprecated since version 2021.1: Method is deprecated. Use AddEntry instead.

## Variable[¶](#variable "Link to this heading")

*class* Variable[¶](#ApiClient.Variable "Link to this definition")  
Returned by

- [`AnalysisPackage.GetParameterVariables`](PackageApi.md#ApiClient.AnalysisPackage.GetParameterVariables "ApiClient.AnalysisPackage.GetParameterVariables")

- [`AnalysisPackage.GetReturnVariables`](PackageApi.md#ApiClient.AnalysisPackage.GetReturnVariables "ApiClient.AnalysisPackage.GetReturnVariables")

- [`AnalysisPackage.GetUnusedVariables`](PackageApi.md#ApiClient.AnalysisPackage.GetUnusedVariables "ApiClient.AnalysisPackage.GetUnusedVariables")

- [`AnalysisPackage.GetVariable`](PackageApi.md#ApiClient.AnalysisPackage.GetVariable "ApiClient.AnalysisPackage.GetVariable")

- [`AnalysisPackage.GetVariables`](PackageApi.md#ApiClient.AnalysisPackage.GetVariables "ApiClient.AnalysisPackage.GetVariables")

- [`Package.GetParameterVariables`](PackageApi.md#ApiClient.Package.GetParameterVariables "ApiClient.Package.GetParameterVariables")

- [`Package.GetRecordedVariables`](PackageApi.md#ApiClient.Package.GetRecordedVariables "ApiClient.Package.GetRecordedVariables")

- [`Package.GetReturnVariables`](PackageApi.md#ApiClient.Package.GetReturnVariables "ApiClient.Package.GetReturnVariables")

- [`Package.GetUnusedVariables`](PackageApi.md#ApiClient.Package.GetUnusedVariables "ApiClient.Package.GetUnusedVariables")

- [`Package.GetVariable`](PackageApi.md#ApiClient.Package.GetVariable "ApiClient.Package.GetVariable")

- [`Package.GetVariables`](PackageApi.md#ApiClient.Package.GetVariables "ApiClient.Package.GetVariables")

- [`PackageBase.GetParameterVariables`](TraceAnalysisApi.md#ApiClient.PackageBase.GetParameterVariables "ApiClient.PackageBase.GetParameterVariables")

- [`PackageBase.GetReturnVariables`](TraceAnalysisApi.md#ApiClient.PackageBase.GetReturnVariables "ApiClient.PackageBase.GetReturnVariables")

- [`PackageBase.GetUnusedVariables`](TraceAnalysisApi.md#ApiClient.PackageBase.GetUnusedVariables "ApiClient.PackageBase.GetUnusedVariables")

- [`PackageBase.GetVariable`](TraceAnalysisApi.md#ApiClient.PackageBase.GetVariable "ApiClient.PackageBase.GetVariable")

- [`PackageBase.GetVariables`](TraceAnalysisApi.md#ApiClient.PackageBase.GetVariables "ApiClient.PackageBase.GetVariables")

- [`VariableApi.CreateVariable`](#ApiClient.VariableApi.CreateVariable "ApiClient.VariableApi.CreateVariable")

Subclasses

- [`BooleanVariable`](#ApiClient.BooleanVariable "ApiClient.BooleanVariable")

- [`DynamicEnumVariable`](#ApiClient.DynamicEnumVariable "ApiClient.DynamicEnumVariable")

- [`DynamicTextTableVariable`](#ApiClient.DynamicTextTableVariable "ApiClient.DynamicTextTableVariable")

- [`EnumVariable`](#ApiClient.EnumVariable "ApiClient.EnumVariable")

- [`FunctionVariable`](#ApiClient.FunctionVariable "ApiClient.FunctionVariable")

- [`NumericVariable`](#ApiClient.NumericVariable "ApiClient.NumericVariable")

- [`PyObjectVariable`](#ApiClient.PyObjectVariable "ApiClient.PyObjectVariable")

- [`StaticTextTableVariable`](#ApiClient.StaticTextTableVariable "ApiClient.StaticTextTableVariable")

- [`StringVariable`](#ApiClient.StringVariable "ApiClient.StringVariable")

- [`StructureVariable`](#ApiClient.StructureVariable "ApiClient.StructureVariable")

- [`VectorVariable`](#ApiClient.VectorVariable "ApiClient.VectorVariable")

Clone()[¶](#ApiClient.Variable.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`Variable`](#ApiClient.Variable "ApiClient.Variable")

GetDescription()[¶](#ApiClient.Variable.GetDescription "Link to this definition")  
Returns the description of the variable.

Returns:  Description of variable

Return type:  str

GetName()[¶](#ApiClient.Variable.GetName "Link to this definition")  
Returns the name of the variable.

Returns:  Name of variable

Return type:  str

GetType()[¶](#ApiClient.Variable.GetType "Link to this definition")  
Returns the type of the initial value of the variable.

Returns:  type of the initial value

Return type:  str

IsParameter()[¶](#ApiClient.Variable.IsParameter "Link to this definition")  
Returns whether the variable is a parameter.

Returns:  True if parameter, else False

Return type:  boolean

IsRecorded()[¶](#ApiClient.Variable.IsRecorded "Link to this definition")  
Returns whether the variable is recorded during execution.

Returns:  True if recorded, else False

Return type:  boolean

IsReturn()[¶](#ApiClient.Variable.IsReturn "Link to this definition")  
Returns whether the variable is a return value.

Returns:  True if return value, else False

Return type:  boolean

SetDescription(*description*)[¶](#ApiClient.Variable.SetDescription "Link to this definition")  
Sets the description of the variable.

Parameters:  **description** (*str*) – Description of variable

SetParameter(*enable=True*)[¶](#ApiClient.Variable.SetParameter "Link to this definition")  
Sets whether the variable is a parameter or not.

Parameters:  **enable** (*boolean*) – Whether the variable is a parameter or not

SetRecorded(*enable=True*)[¶](#ApiClient.Variable.SetRecorded "Link to this definition")  
Sets the recording state of the variable to the value of enable.

Parameters:  **enable** (*boolean*) – Whether to enable the recording of the variable

SetReturn(*enable=True*)[¶](#ApiClient.Variable.SetReturn "Link to this definition")  
Sets whether the variable is a return value or not.

Parameters:  **enable** (*boolean*) – Whether the variable is a return value or not

GetInitialBooleanValue()[¶](#ApiClient.Variable.GetInitialBooleanValue "Link to this definition")  
Returns the initial value of the variable or None if it is not a Boolean.

Returns:  Initial value of the variable

Return type:  bool

Deprecated since version 2021.1: Method is deprecated. Use GetInitialValue instead.

GetInitialFunctionValue()[¶](#ApiClient.Variable.GetInitialFunctionValue "Link to this definition")  
Returns the code of the function variable or None if it is not a function variable.

Returns:  Initial code of the function variable

Return type:  string

Deprecated since version 2021.1: Method is deprecated. Use GetInitialValue instead.

GetInitialNumericValue()[¶](#ApiClient.Variable.GetInitialNumericValue "Link to this definition")  
Returns the initial value of the variable or None if it is not a Numeric.

Returns:  Initial value of the variable

Return type:  int/float

Deprecated since version 2021.1: Method is deprecated. Use GetInitialValue instead.

GetInitialNumericValueString()[¶](#ApiClient.Variable.GetInitialNumericValueString "Link to this definition")  
Returns the initial value string of the variable, or None if it is not a Numeric.

The initial value is returned exactly as it has been typed in (e.g. in hex, or with additional zeroes), unless it has been set via [`SetInitialNumericValue()`](#ApiClient.Variable.SetInitialNumericValue "ApiClient.Variable.SetInitialNumericValue"), which stores only the numeric value itself.

Returns:  Initial value of the variable

Return type:  str

Deprecated since version 2021.1: Method is only supported for numeric variable type in future versions.

GetInitialPyObjectValue()[¶](#ApiClient.Variable.GetInitialPyObjectValue "Link to this definition")  
Returns the initial value of the variable or None if it is not a PyObject.

Returns:  Initial value of the variable

Return type:  str

Deprecated since version 2021.1: Method is deprecated. Use GetInitialValue instead.

GetInitialStringValue()[¶](#ApiClient.Variable.GetInitialStringValue "Link to this definition")  
Returns the initial value of the variable or None if it is not a String.

Returns:  Initial value of the variable

Return type:  str

Deprecated since version 2021.1: Method is deprecated. Use GetInitialValue instead.

GetInitialStructureValue()[¶](#ApiClient.Variable.GetInitialStructureValue "Link to this definition")  
Returns the type of the initial value of the variable or None if it is not a structure.

Returns:  mappingName and structurePath of the variable’s initial value

Return type:  dict[str, str]

Deprecated since version 2021.1: Method is deprecated. Use GetInitialValue instead.

GetInitialTextTableValue()[¶](#ApiClient.Variable.GetInitialTextTableValue "Link to this definition")  
Returns the initial value of the variable or None if it is not a Texttable.

Returns:  Initial value of the variable

Return type:  list[str]

Deprecated since version 2021.1: Method is deprecated. Use GetEntries instead.

GetInitialValueType()[¶](#ApiClient.Variable.GetInitialValueType "Link to this definition")  
Returns the type of the initial value of the variable.

Returns:  type of the initial value

Return type:  str

Deprecated since version 2021.1: Method is deprecated. Use GetType instead.

SetInitialBooleanValue(*value*)[¶](#ApiClient.Variable.SetInitialBooleanValue "Link to this definition")  
Sets the initial value of the variable.

Parameters:  **value** (*bool*) – Initial value of the variable

Deprecated since version 2021.1: Method is deprecated. Use SetInitialValue instead.

SetInitialFunctionValue(*code*)[¶](#ApiClient.Variable.SetInitialFunctionValue "Link to this definition")  
Sets the code of the Function.

Parameters:  **code** (*string*) – Python code to be executed

Deprecated since version 2021.1: Method is deprecated. Use SetInitialValue instead.

SetInitialNumericValue(*value*)[¶](#ApiClient.Variable.SetInitialNumericValue "Link to this definition")  
Sets the initial value of the variable.

Only the numeric value itself will be stored, not the way it has been typed in (e.g. in hex, or with additional zeroes).

Parameters:  **value** (*int/float*) – Initial value of the variable

Deprecated since version 2021.1: Method is deprecated. Use SetInitialValue instead.

SetInitialNumericValueString(*value*)[¶](#ApiClient.Variable.SetInitialNumericValueString "Link to this definition")  
Sets the initial value of the variable as string.

The string will be stored exactly as typed (e.g. in hex, or with additional zeroes).

Parameters:  **value** (*str*) – Initial value of the variable

Deprecated since version 2021.1: Method is only supported for numeric variable type in future versions.

SetInitialPyObjectValue(*value*)[¶](#ApiClient.Variable.SetInitialPyObjectValue "Link to this definition")  
Sets the initial value of the variable.

Parameters:  **value** (*string*) – May only consist of the following Python literal structures: strings, numbers, tuples, lists, dicts, booleans, and None.

Deprecated since version 2021.1: Method is deprecated. Use SetInitialValue instead.

SetInitialStringValue(*value*)[¶](#ApiClient.Variable.SetInitialStringValue "Link to this definition")  
Sets the initial value of the variable.

Parameters:  **value** (*string*) – Initial value of the variable

Deprecated since version 2021.1: Method is deprecated. Use SetInitialValue instead.

SetInitialStructureValue(*mappingName*, *structurePath*)[¶](#ApiClient.Variable.SetInitialStructureValue "Link to this definition")  
Sets the initial value of the variable.

Parameters:  - **mappingName** (*str*) – Mapping name to be assigned to the structure variable

- **structurePath** (*str*) – path inside the structure

Deprecated since version 2021.1: Method is deprecated. Use SetInitialValue instead.

SetInitialTextTableValue(*value*, *defaultValue*)[¶](#ApiClient.Variable.SetInitialTextTableValue "Link to this definition")  
Sets the initial value of the variable.

Parameters:  - **value** (*list[str]*) – A list of strings.

- **defaultValue** (*str*) – The string which should be used as the current value.

Deprecated since version 2021.1: Method is deprecated. Use AddEntry instead.

## VectorVariable[¶](#vectorvariable "Link to this heading")

*class* VectorVariable[¶](#ApiClient.VectorVariable "Link to this definition")  
Base class

[`Variable`](#ApiClient.Variable "ApiClient.Variable")

Returned by

- [`VariableApi.CreateVectorVariable`](#ApiClient.VariableApi.CreateVectorVariable "ApiClient.VariableApi.CreateVectorVariable")

Clone()[¶](#ApiClient.VectorVariable.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`VectorVariable`](#ApiClient.VectorVariable "ApiClient.VectorVariable")

DeleteInitialValue(*x*)[¶](#ApiClient.VectorVariable.DeleteInitialValue "Link to this definition")  
Deletes the expression defining an element’s value.

Parameters:  **x** (*int*) – Element position to delete.

GetDescription()[¶](#ApiClient.VectorVariable.GetDescription "Link to this definition")  
Returns the description of the variable.

Returns:  Description of variable

Return type:  str

GetDimension()[¶](#ApiClient.VectorVariable.GetDimension "Link to this definition")  
Returns the length of the vector.

Returns:  Maximum number of elements.

Return type:  int

GetInitialValue(*x*)[¶](#ApiClient.VectorVariable.GetInitialValue "Link to this definition")  
Returns the value expression at the index x of a vector.

Parameters:  **x** (*int*) – Element position to get.

Returns:  Expression

Return type:  str

GetInitialValues()[¶](#ApiClient.VectorVariable.GetInitialValues "Link to this definition")  
Returns the initial values of the vector.

Returns:  The initial value of the vector as a list of string expressions.

Return type:  list[str]

GetName()[¶](#ApiClient.VectorVariable.GetName "Link to this definition")  
Returns the name of the variable.

Returns:  Name of variable

Return type:  str

GetType()[¶](#ApiClient.VectorVariable.GetType "Link to this definition")  
Returns the type of the initial value of the variable.

Returns:  type of the initial value

Return type:  str

IsParameter()[¶](#ApiClient.VectorVariable.IsParameter "Link to this definition")  
Returns whether the variable is a parameter.

Returns:  True if parameter, else False

Return type:  boolean

IsRecorded()[¶](#ApiClient.VectorVariable.IsRecorded "Link to this definition")  
Returns whether the variable is recorded during execution.

Returns:  True if recorded, else False

Return type:  boolean

IsReturn()[¶](#ApiClient.VectorVariable.IsReturn "Link to this definition")  
Returns whether the variable is a return value.

Returns:  True if return value, else False

Return type:  boolean

SetDescription(*description*)[¶](#ApiClient.VectorVariable.SetDescription "Link to this definition")  
Sets the description of the variable.

Parameters:  **description** (*str*) – Description of variable

SetDimension(*dimension*)[¶](#ApiClient.VectorVariable.SetDimension "Link to this definition")  
Sets a new dimension for the vector variable. If the new dimension is smaller than the pre-existing vector, then the right-most values will be cut off.

Parameters:  **dimension** (*int*) – The new dimension size.

SetInitialValue(*x*, *value*)[¶](#ApiClient.VectorVariable.SetInitialValue "Link to this definition")  
Sets the value at a specific index.

Parameters:  - **x** (*int*) – Element position to set.

- **value** (*str*) – Any Python expression as a string.

SetInitialValues(*values*)[¶](#ApiClient.VectorVariable.SetInitialValues "Link to this definition")  
Sets the initial values of the vector.

Parameters:  **values** (*list[str]*) – Initial values of the vector in the form of a list of string expressions.

SetParameter(*enable=True*)[¶](#ApiClient.VectorVariable.SetParameter "Link to this definition")  
Sets whether the variable is a parameter or not.

Parameters:  **enable** (*boolean*) – Whether the variable is a parameter or not

SetRecorded(*enable=True*)[¶](#ApiClient.VectorVariable.SetRecorded "Link to this definition")  
Sets the recording state of the variable to the value of enable.

Parameters:  **enable** (*boolean*) – Whether to enable the recording of the variable

SetReturn(*enable=True*)[¶](#ApiClient.VectorVariable.SetReturn "Link to this definition")  
Sets whether the variable is a return value or not.

Parameters:  **enable** (*boolean*) – Whether the variable is a return value or not

GetInitialBooleanValue()[¶](#ApiClient.VectorVariable.GetInitialBooleanValue "Link to this definition")  
Returns the initial value of the variable or None if it is not a Boolean.

Returns:  Initial value of the variable

Return type:  bool

Deprecated since version 2021.1: Method is deprecated. Use GetInitialValue instead.

GetInitialFunctionValue()[¶](#ApiClient.VectorVariable.GetInitialFunctionValue "Link to this definition")  
Returns the code of the function variable or None if it is not a function variable.

Returns:  Initial code of the function variable

Return type:  string

Deprecated since version 2021.1: Method is deprecated. Use GetInitialValue instead.

GetInitialNumericValue()[¶](#ApiClient.VectorVariable.GetInitialNumericValue "Link to this definition")  
Returns the initial value of the variable or None if it is not a Numeric.

Returns:  Initial value of the variable

Return type:  int/float

Deprecated since version 2021.1: Method is deprecated. Use GetInitialValue instead.

GetInitialNumericValueString()[¶](#ApiClient.VectorVariable.GetInitialNumericValueString "Link to this definition")  
Returns the initial value string of the variable, or None if it is not a Numeric.

The initial value is returned exactly as it has been typed in (e.g. in hex, or with additional zeroes), unless it has been set via [`SetInitialNumericValue()`](#ApiClient.VectorVariable.SetInitialNumericValue "ApiClient.VectorVariable.SetInitialNumericValue"), which stores only the numeric value itself.

Returns:  Initial value of the variable

Return type:  str

Deprecated since version 2021.1: Method is only supported for numeric variable type in future versions.

GetInitialPyObjectValue()[¶](#ApiClient.VectorVariable.GetInitialPyObjectValue "Link to this definition")  
Returns the initial value of the variable or None if it is not a PyObject.

Returns:  Initial value of the variable

Return type:  str

Deprecated since version 2021.1: Method is deprecated. Use GetInitialValue instead.

GetInitialStringValue()[¶](#ApiClient.VectorVariable.GetInitialStringValue "Link to this definition")  
Returns the initial value of the variable or None if it is not a String.

Returns:  Initial value of the variable

Return type:  str

Deprecated since version 2021.1: Method is deprecated. Use GetInitialValue instead.

GetInitialStructureValue()[¶](#ApiClient.VectorVariable.GetInitialStructureValue "Link to this definition")  
Returns the type of the initial value of the variable or None if it is not a structure.

Returns:  mappingName and structurePath of the variable’s initial value

Return type:  dict[str, str]

Deprecated since version 2021.1: Method is deprecated. Use GetInitialValue instead.

GetInitialTextTableValue()[¶](#ApiClient.VectorVariable.GetInitialTextTableValue "Link to this definition")  
Returns the initial value of the variable or None if it is not a Texttable.

Returns:  Initial value of the variable

Return type:  list[str]

Deprecated since version 2021.1: Method is deprecated. Use GetEntries instead.

GetInitialValueType()[¶](#ApiClient.VectorVariable.GetInitialValueType "Link to this definition")  
Returns the type of the initial value of the variable.

Returns:  type of the initial value

Return type:  str

Deprecated since version 2021.1: Method is deprecated. Use GetType instead.

SetInitialBooleanValue(*value*)[¶](#ApiClient.VectorVariable.SetInitialBooleanValue "Link to this definition")  
Sets the initial value of the variable.

Parameters:  **value** (*bool*) – Initial value of the variable

Deprecated since version 2021.1: Method is deprecated. Use SetInitialValue instead.

SetInitialFunctionValue(*code*)[¶](#ApiClient.VectorVariable.SetInitialFunctionValue "Link to this definition")  
Sets the code of the Function.

Parameters:  **code** (*string*) – Python code to be executed

Deprecated since version 2021.1: Method is deprecated. Use SetInitialValue instead.

SetInitialNumericValue(*value*)[¶](#ApiClient.VectorVariable.SetInitialNumericValue "Link to this definition")  
Sets the initial value of the variable.

Only the numeric value itself will be stored, not the way it has been typed in (e.g. in hex, or with additional zeroes).

Parameters:  **value** (*int/float*) – Initial value of the variable

Deprecated since version 2021.1: Method is deprecated. Use SetInitialValue instead.

SetInitialNumericValueString(*value*)[¶](#ApiClient.VectorVariable.SetInitialNumericValueString "Link to this definition")  
Sets the initial value of the variable as string.

The string will be stored exactly as typed (e.g. in hex, or with additional zeroes).

Parameters:  **value** (*str*) – Initial value of the variable

Deprecated since version 2021.1: Method is only supported for numeric variable type in future versions.

SetInitialPyObjectValue(*value*)[¶](#ApiClient.VectorVariable.SetInitialPyObjectValue "Link to this definition")  
Sets the initial value of the variable.

Parameters:  **value** (*string*) – May only consist of the following Python literal structures: strings, numbers, tuples, lists, dicts, booleans, and None.

Deprecated since version 2021.1: Method is deprecated. Use SetInitialValue instead.

SetInitialStringValue(*value*)[¶](#ApiClient.VectorVariable.SetInitialStringValue "Link to this definition")  
Sets the initial value of the variable.

Parameters:  **value** (*string*) – Initial value of the variable

Deprecated since version 2021.1: Method is deprecated. Use SetInitialValue instead.

SetInitialStructureValue(*mappingName*, *structurePath*)[¶](#ApiClient.VectorVariable.SetInitialStructureValue "Link to this definition")  
Sets the initial value of the variable.

Parameters:  - **mappingName** (*str*) – Mapping name to be assigned to the structure variable

- **structurePath** (*str*) – path inside the structure

Deprecated since version 2021.1: Method is deprecated. Use SetInitialValue instead.

SetInitialTextTableValue(*value*, *defaultValue*)[¶](#ApiClient.VectorVariable.SetInitialTextTableValue "Link to this definition")  
Sets the initial value of the variable.

Parameters:  - **value** (*list[str]*) – A list of strings.

- **defaultValue** (*str*) – The string which should be used as the current value.

Deprecated since version 2021.1: Method is deprecated. Use AddEntry instead.
