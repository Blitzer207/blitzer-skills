# Generator APIs[¶](#generator-apis "Link to this heading")

## Project generator API[¶](#project-generator-api "Link to this heading")

### ProjectGenerator[¶](#module-tts.core.project.generator.ProjectGenerator "Link to this heading")

*class* CycleData[¶](#tts.core.project.generator.ProjectGenerator.CycleData "Link to this definition")  
A container for all data that can be generated during one cycle.

Name[¶](#tts.core.project.generator.ProjectGenerator.CycleData.Name "Link to this definition")  
Returns the name of this cycle

Returns:  The name of this cycle

Return type:  str

objectApi *= None*[¶](#tts.core.project.generator.ProjectGenerator.CycleData.objectApi "Link to this definition")  
The Object API which is used to create test steps.

Type:  [`ApiClient.ApiClient`](../general_api/objectApi.md#ApiClient.ApiClient "ApiClient.ApiClient")

projectInstance *= None*[¶](#tts.core.project.generator.ProjectGenerator.CycleData.projectInstance "Link to this definition")  
The project instance to be completed and executed. Based on a provided template or empty.

Type:  [`ApiClient.Project`](../general_api/ProjectApi.md#ApiClient.Project "ApiClient.Project")

GetName()[¶](#tts.core.project.generator.ProjectGenerator.CycleData.GetName "Link to this definition")  
Returns the name of this cycle

Returns:  The name of this cycle

Return type:  str

SetName(*value*)[¶](#tts.core.project.generator.ProjectGenerator.CycleData.SetName "Link to this definition")  
Sets the name of this cycle.

Parameters:  **value** (*str*) – Name for this cycle.

*class* ProjectGenerator[¶](#tts.core.project.generator.ProjectGenerator.ProjectGenerator "Link to this definition")  
This is the base class for user defined project generators. All project generators should be derived form this class. It defines specific methods that are called during generation of projects. The required behaviour of a project generator is implemented by overwriting these methods.

Some fields and methods *must* be overridden (**mandatory**), others *may* be overridden (**optional**). There are also methods that are only to be called by the user implementation and should not be overridden (those without a note).

DESCRIPTION *= ''*[¶](#tts.core.project.generator.ProjectGenerator.ProjectGenerator.DESCRIPTION "Link to this definition")  
A short description of the project generator.

Type:  str

ID *= ''*[¶](#tts.core.project.generator.ProjectGenerator.ProjectGenerator.ID "Link to this definition")  
A universally unique identifier to make the project generator unique. The ID should be generated automatically to be unique.

Type:  str

Note

Setting this field is **mandatory**

NAME *= ''*[¶](#tts.core.project.generator.ProjectGenerator.ProjectGenerator.NAME "Link to this definition")  
The display name of the project generator.

Type:  str

Note

Setting this field is **mandatory**

SERIALIZE*: dict[str, tuple[str, str] | tuple[str, str, object]] = {}*[¶](#tts.core.project.generator.ProjectGenerator.ProjectGenerator.SERIALIZE "Link to this definition")  
Declaration of instance variables of the project generator, that are to be exported/imported to/from xml format (e.g. during saving/loading a project). The declaration contains an item for each instance variable in form of an dictionary. Example:

    SERIALIZE = {
                    "foo": ("FOO-VAR", "integer", 23),
                    "bar": ("BAR", "string"),
                    "params: ("PARAMETERS", "list")
                }

The declaration items key must match the name of the corresponding instance variable (e.g. for an instance variable self.foo the item’s key must be “foo”). The item’s value must be a tuple containing at least 2 elements. So the general syntax for a declaration item is:

    <variable name>: (<variable alias>, <type alias>, [default value])

Syntax and meaning of the tuple’s elements are:  
- **\<variable alias\>** declares the name of the xml element that is used for the variable’s xml representation.

- **\<type alias\>** keyword specifing the python variable’s type. The following table gives all keywords and their corresponding python type respectively:

  > - `boolean`: bool
  >
  > - `integer`: int
  >
  > - `long`: int
  >
  > - `float`: float
  >
  > - `string`: str
  >
  > - `unicode`: str
  >
  > - `list`: list
  >
  > - `dict`: dict

PLEASE NOTE: Keys of dictionaries being (de-)serialized must be strings. Furthermore values of dictionaries and lists are required to be of type `bool`, `int`, `float`, `str`, `list` or `dict`. The same restrictions apply to embedded lists and dictionaries. The types `long` and `unicode` are only keept for compatibility. Do not use these in new code.

- **\<default value\>** is an optional element. It specifies the variable’s default value. If the variable’s value equals its default value during export the variable is not exported at all. Conversely, the variable is assigned its default value during import if the xml data does not provide an value for the variable.

Type:  dict

api *= None*[¶](#tts.core.project.generator.ProjectGenerator.ProjectGenerator.api "Link to this definition")  
Access to the internal ecu.test API. The API will be assigned at runtime, in order to be independent from ecu.test for testing purposes.

See also

[Internal APIs](../general_api/api.md#internalapi)

projectPath*: str | None = None*[¶](#tts.core.project.generator.ProjectGenerator.ProjectGenerator.projectPath "Link to this definition")  
Absolute path to the project file containing the generator. In case of direct execution, this is the source project. In case of static generation it is the destination project.

sourceProjectPath*: str | None = None*[¶](#tts.core.project.generator.ProjectGenerator.ProjectGenerator.sourceProjectPath "Link to this definition")  
Absolute path to the source project file containing the generator.

Check()[¶](#tts.core.project.generator.ProjectGenerator.ProjectGenerator.Check "Link to this definition")  
Implement this method to allow checking of of the user-implemented generator.

Returns:  A list of error messages or an empty list if everything is fine.

Return type:  list\<str\>

Note

Overriding this method is **optional**

CreateCycleData(*name=None*, *template=None*)[¶](#tts.core.project.generator.ProjectGenerator.ProjectGenerator.CreateCycleData "Link to this definition")  
Creates an instance of class CycleData.

Parameters:  - **name** (*str*) – A name for this cycle that will be displayed in the report. (optional)

- **template** (*str*) – Path to template project file to be used as base for generator. (optional)

Returns:  The cycle data object

Return type:  [`CycleData`](#tts.core.project.generator.ProjectGenerator.CycleData "tts.core.project.generator.ProjectGenerator.CycleData")

DryGenerationEnabled()[¶](#tts.core.project.generator.ProjectGenerator.ProjectGenerator.DryGenerationEnabled "Link to this definition")  
Returns True, if the generator runs in dry generation mode. In this mode, the generator is used to generate a project with static projects.

Return type:  bool

GenerationIterator()[¶](#tts.core.project.generator.ProjectGenerator.ProjectGenerator.GenerationIterator "Link to this definition")  
Implement this method for the generation of the data for on cycle. This is an iterator and it should return an [`CycleData`](#tts.core.project.generator.ProjectGenerator.CycleData "tts.core.project.generator.ProjectGenerator.CycleData") object with the python keyword ‘yield’. To create an [`CycleData`](#tts.core.project.generator.ProjectGenerator.CycleData "tts.core.project.generator.ProjectGenerator.CycleData") object, use the method [`CreateCycleData()`](#tts.core.project.generator.ProjectGenerator.ProjectGenerator.CreateCycleData "tts.core.project.generator.ProjectGenerator.ProjectGenerator.CreateCycleData") and store all information in this object. Example:

    def GenerationIterator(self):
        for line in file:
            yield CreateCycleData({'lineData': line})

Note

Overriding this method is **mandatory**

*classmethod* GetDescription()[¶](#tts.core.project.generator.ProjectGenerator.ProjectGenerator.GetDescription "Link to this definition")  
Returns the description of the project generator. The description can be specified by setting the class variable [`DESCRIPTION`](#tts.core.project.generator.ProjectGenerator.ProjectGenerator.DESCRIPTION "tts.core.project.generator.ProjectGenerator.ProjectGenerator.DESCRIPTION").

Return type:  str

GetDialog()[¶](#tts.core.project.generator.ProjectGenerator.ProjectGenerator.GetDialog "Link to this definition")  
Implement this method to return the configuration dialog of your project generator. The dialog should set the generator data.

Return type:  wx.Dialog, None

Note

Overriding this method is **optional**

*classmethod* GetFormatRev()[¶](#tts.core.project.generator.ProjectGenerator.ProjectGenerator.GetFormatRev "Link to this definition")  
Returns the format revision of the project generator. The format revision can be specified by setting the class variable `FORMAT_REV`. This is an optional parameter.

Return type:  int

*classmethod* GetId()[¶](#tts.core.project.generator.ProjectGenerator.ProjectGenerator.GetId "Link to this definition")  
Returns the universally unique identifier of the project generator. The identifier should be specified by setting the class variable [`ID`](#tts.core.project.generator.ProjectGenerator.ProjectGenerator.ID "tts.core.project.generator.ProjectGenerator.ProjectGenerator.ID").

Return type:  str

*classmethod* GetName()[¶](#tts.core.project.generator.ProjectGenerator.ProjectGenerator.GetName "Link to this definition")  
Returns the name of the project generator. The name should be specified by setting the class variable [`NAME`](#tts.core.project.generator.ProjectGenerator.ProjectGenerator.NAME "tts.core.project.generator.ProjectGenerator.ProjectGenerator.NAME").

Return type:  str

GetParameterText()[¶](#tts.core.project.generator.ProjectGenerator.ProjectGenerator.GetParameterText "Link to this definition")  
Implement this method to show the parameters of your project generator in properties column.

Returns:  parameter text

Return type:  str

Note

Overriding this method is **optional**

GetTargetItemCount()[¶](#tts.core.project.generator.ProjectGenerator.ProjectGenerator.GetTargetItemCount "Link to this definition")  
Implement this method to define the expected number of cycle sets to be generated as information for progress indicators. Will be called for updates throughout the generation. Therefore you can dynamically return the size of the current task.

Returns:  expected count of cycle sets to be generated

Return type:  int

PostGeneration()[¶](#tts.core.project.generator.ProjectGenerator.ProjectGenerator.PostGeneration "Link to this definition")  
Implement this method to specify post generation behavior. This method is called after the generation. This method will be called even if an exception occurs during generation (incl. PreGeneration), but not if the project execution is aborted (by the user or because of an “abort on error” setting).

Note

Overriding this method is **optional**

PreGeneration()[¶](#tts.core.project.generator.ProjectGenerator.ProjectGenerator.PreGeneration "Link to this definition")  
Implement this method to specify pre generation behavior. This method is called before the generation.

Note

Overriding this method is **optional**

## Project parameter generator API[¶](#project-parameter-generator-api "Link to this heading")

### AbortError[¶](#aborterror "Link to this heading")

*class* AbortError[¶](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.AbortError "Link to this definition")  

### CallbackParamGenerator[¶](#module-tts.core.project.generator.paramGenerator.CallbackParamGenerator "Link to this heading")

*class* CallbackParamGenerator[¶](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator "Link to this definition")  
This is an alternative base class for user-defined parameter generators. The interface corresponds to that of the ParamGenerator class with the only difference that the Generate method must be implemented instead of the GenerationIterator method.

DESCRIPTION *= ''*[¶](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.DESCRIPTION "Link to this definition")  
A short description of the parameter generator.

Type:  str

Note

Setting this field is **optional**

ID *= ''*[¶](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.ID "Link to this definition")  
A universally unique identifier to make the parameter generator unique. The ID should be generated using a UUID generator to be unique.

Type:  str

Note

Setting this field is **mandatory**

NAME *= ''*[¶](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.NAME "Link to this definition")  
The display name of the parameter generator.

Type:  str

Note

Setting this field is **mandatory**

SERIALIZE*: dict[str, tuple[str, str] | tuple[str, str, object]] = {}*[¶](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.SERIALIZE "Link to this definition")  
Declaration of instance variables of the parameter generator, that are to be exported/imported to/from xml format (e.g. during saving/loading a project). The declaration contains an item for each instance variable in form of an dictionary. Example:

    SERIALIZE = {
                    "foo": ("FOO-VAR", "integer", 23),
                    "bar": ("BAR", "string"),
                    "params: ("PARAMETERS", "list")
                }

The declaration items key must match the name of the corresponding instance variable (e.g. for an instance variable self.foo the item’s key must be “foo”). The item’s value must be a tuple containing at least 2 elements. So the general syntax for a declaration item is:

    <variable name>: (<variable alias>, <type alias>, [default value])

Syntax and meaning of the tuple’s elements are:  
- **\<variable alias\>** declares the name of the xml element that is used for the variable’s xml representation.

- **\<type alias\>** keyword specifing the python variable’s type. The following table gives all keywords and their corresponding python type respectively:

  > - `boolean`: bool
  >
  > - `integer`: int
  >
  > - `long`: long
  >
  > - `float`: float
  >
  > - `string`: str
  >
  > - `unicode`: str
  >
  > - `list`: list
  >
  > - `dict`: dict

PLEASE NOTE: Keys of dictionaries being (de-)serialized must be strings. Furthermore values of dictionaries and lists are required to be of type `bool`, `int`, `float`, `str`, `list` or `dict`. The same restrictions apply to embedded lists and dictionaries. The types `long` and `unicode` are only kept for compatibility. Do not use these in new code.

- **\<default value\>** is an optional element. It specifies the variable’s default value. If the variable’s value equals its default value during export the variable is not exported at all. Conversely, the variable is assigned its default value during import if the xml data does not provide an value for the variable.

Type:  dict

Note

Setting this field is **optional**

api *= None*[¶](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.api "Link to this definition")  
Access to the internal ecu.test API. The API will be assigned at runtime, in order to be independent from ecu.test for testing purposes.

See also

[Internal APIs](../general_api/api.md#internalapi)

projectPath*: str | None = None*[¶](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.projectPath "Link to this definition")  
Absolute path to the project file containing the generator. In case of direct execution, this is the source project. In case of static generation it is the destination project.

Check()[¶](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.Check "Link to this definition")  
Implement this method to allow the user-implemented generator to be checked.

Returns:  A list of error messages or an empty list if everything is fine.

Return type:  list\<str\>

Note

Overriding this method is **optional**.

CreateCycleData(*paramSet=None*, *constSet=None*, *name=None*)[¶](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.CreateCycleData "Link to this definition")  
Method, to create an instance of class CycleData.

Parameters:  - **paramSet** (*dict*) – A set of parameters to parameterize a package.

- **constSet** (*dict*) – A set of constants that will be set before running a package. (optional)

- **name** (*str*) – A name for this cycle that will be displayed in the report. (optional)

Returns:  The cycle data object

Return type:  [`CycleData`](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData "tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData")

DryGenerationEnabled()[¶](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.DryGenerationEnabled "Link to this definition")  
Returns True, if the generator runs in dry generation mode. In this mode, the generator is used to generate a project with static parameter records.

Return type:  bool

Generate(*testRunFunction*)[¶](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.Generate "Link to this definition")  
Implement this method for generating parameter sets. Each parameter set must be an object of [`CycleData`](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData "tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData") and can be created with the method [`CreateCycleData()`](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.CreateCycleData "tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.CreateCycleData"). A test run is executed by calling the testRunFunction.

Parameters:  **testRunFunction** – If this function is called, an ecu.test test run is started. The function expects one or more parameter sets and returns a list of dictionaries containing the return variables of the package with their result values. A parameter set must be an instance of [`CycleData`](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData "tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData") which can be created with the method [`CreateCycleData()`](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.CreateCycleData "tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.CreateCycleData"). If the test run is aborted by ecu.test, an abort error occurs. This error should only be caught for the purpose of cleaning up.

Note

Overriding this method is **mandatory**

*classmethod* GetDescription()[¶](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.GetDescription "Link to this definition")  
Returns the description of the parameter generator. The description can be specified by setting the class variable [`DESCRIPTION`](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.DESCRIPTION "tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.DESCRIPTION").

Return type:  str

GetDialog()[¶](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.GetDialog "Link to this definition")  
Implement this method to return the configuration dialog of your parameter generator. The dialog should set the generator data.

Return type:  wx.Dialog or None

Note

Overriding this method is **optional**.

*classmethod* GetId()[¶](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.GetId "Link to this definition")  
Returns the universally unique identifier of the parameter generator. The identifier should be specified by setting the class variable [`ID`](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.ID "tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.ID").

Return type:  str

GetLastReturnSets()[¶](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.GetLastReturnSets "Link to this definition")  
Returns a list of all return sets from the last ecu.test test run.

This method only returns a result if the generator is not running in dry generation mode and it is called within the L{Generate()} method after at least one parameter set has been executed (by calling the testRunFunction in the L{Generate()} method). In all other circumstances, the method always returns an empty list.

Return type:  list of dicts

*classmethod* GetName()[¶](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.GetName "Link to this definition")  
Returns the name of the parameter generator. The name should be specified by setting the class variable [`NAME`](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.NAME "tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.NAME").

Return type:  str

GetParameterText()[¶](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.GetParameterText "Link to this definition")  
Implement this method to show the parameters of your param generator in properties column.

Returns:  parameter text

Return type:  str

Note

Overriding this method is **optional**.

GetReportData()[¶](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.GetReportData "Link to this definition")  
Implement this method to set the information for the generator test step in the report. An object of type [`ReportData`](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.ReportData "tts.core.project.generator.paramGenerator.ParamGeneratorBase.ReportData") must be returned.

Return type:  [`ReportData`](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.ReportData "tts.core.project.generator.paramGenerator.ParamGeneratorBase.ReportData") or None

Note

Overriding this method is **optional**.

GetTargetItemCount()[¶](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.GetTargetItemCount "Link to this definition")  
Implement this method to define the expected number of cycle sets to be generated as information for progress indicators. Will be called for updates throughout the generation. Therefore, you can dynamically return the size of the current task.

Returns:  expected count of cycle sets to be generated

Return type:  int

GetUsedMappingItems()[¶](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.GetUsedMappingItems "Link to this definition")  
Returns the mapping items that will be used during generation.

If mapping items are to be added to the generated parameter sets of an analysis package, they have to be defined here in order to be registered for the stimulation package. Mapping items can be defined here directly, parsed from a file or whatever source, but the complete set of mapping items used during generation has to be returned by this method.

Note

Overriding this method is **optional** and only necessary for parameter set generators used with analysis packages and overwriting mapping items.

Attention

This method is called before any other method (e.g., PreGeneration)! If you read in required data for the mapping during PreGeneration, you have to redesign your code to be called at least once during GetUsedMappingItems.

Returns:  list of mapping items

Return type:  list[[ApiClient.MappingItem](../general_api/MappingApi.md#ApiClient.MappingItem "ApiClient.MappingItem")]

IsValidForAnalysisPackages()[¶](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.IsValidForAnalysisPackages "Link to this definition")  
Returns if usage of parameter set generator is feasible for analysis packages.

If set to ‘True’ and parameter set generator is not feasible for analysis packages, errors will be raised during runtime. If set to ‘False’, the GUI will give direct feedback if the parameter set generator is used for an analysis package.

Returns:  True, if valid for analysis package usage, else False

Return type:  bool

Note

Overriding this method is **optional**.

OnInit(*packageInfo*)[¶](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.OnInit "Link to this definition")  
Implement this method to process information about the package to which the generator belongs. It will be called before [`PreGeneration()`](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.PreGeneration "tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.PreGeneration") or [`GetDialog()`](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.GetDialog "tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.GetDialog") is called.

Parameters:  **packageInfo** ([`PackageInfo`](#tts.core.project.projectStep.PackageInfo.PackageInfo "tts.core.project.projectStep.PackageInfo.PackageInfo")) – The package info object.

Note

Overriding this method is **optional**

PostGeneration()[¶](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.PostGeneration "Link to this definition")  
Implement this method to specify post generation behavior. This method is called after the generation. This method will be called even if an exception occurs during generation (incl. PreGeneration), but not if the project execution is aborted (by the user or because of an “abort on error” setting).

Note

Overriding this method is **optional**.

PreGeneration()[¶](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.PreGeneration "Link to this definition")  
Implement this method to specify pre generation behavior. This method is called before the generation.

Note

Overriding this method is **optional**.

### CycleData[¶](#cycledata "Link to this heading")

*class* CycleData[¶](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData "Link to this definition")  
This class is a container for all data, that can be generated during one cycle.

RECORDING_INFO_CLASS[¶](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.RECORDING_INFO_CLASS "Link to this definition")  
alias of [`RecordingInfo`](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.RecordingInfo "tts.core.project.generator.paramGenerator.ParamGeneratorBase.RecordingInfo")

Attributes[¶](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.Attributes "Link to this definition")  
Returns the dict of attributes.

Returns:  The dict of attributes

Return type:  dict

ConstSet[¶](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.ConstSet "Link to this definition")  
Returns the set of constants.

Returns:  The set of constants.

Return type:  dict

Name[¶](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.Name "Link to this definition")  
Returns the name of this cycle

Returns:  The name of this cycle

Return type:  str

ParamSet[¶](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.ParamSet "Link to this definition")  
Returns the set of parameters.

Returns:  The set of parameters.

Return type:  dict

RecordingInfos[¶](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.RecordingInfos "Link to this definition")  
Returns the dict of recording infos.

Returns:  The dict of recording infos.

Return type:  dict

AddAttribute(*name*, *value*)[¶](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.AddAttribute "Link to this definition")  
Adds an attribute to this cycle.

Parameters:  - **name** (*str*) – Name of the attribute

- **value** (*str*) – Value of the attribute

AddConst(*name*, *value*)[¶](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.AddConst "Link to this definition")  
Adds a constant to this cycle.

Parameters:  - **name** (*str*) – Name for the constant.

- **value** (*str,* *float,* *int,* *bool*) – Value to assign to this constant.

AddMappingItem(*mappingItem*)[¶](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.AddMappingItem "Link to this definition")  
Adds mapping item to the mapping space for this cycle.

See also

[Object API](../general_api/objectApi.md#objectapi)

Parameters:  **mappingItem** ([*ApiClient.MappingItem*](../general_api/MappingApi.md#ApiClient.MappingItem "ApiClient.MappingItem")) – MappingItem originating from e.g api.GetObjectApi().PackageApi.MappingApi

AddParameter(*name*, *value*)[¶](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.AddParameter "Link to this definition")  
Adds a parameter to this cycle.

Parameters:  - **name** (*str*) – Name for the parameter.

- **value** (*str,* *float,* *int,* *bool*) – Value to assign to this parameter.

AddRecordingInfo(*recordingGroupName*, *path*)[¶](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.AddRecordingInfo "Link to this definition")  
Adds a recording info into a recording group for this cycle. A recording info consists of a recording (path) and some additional information depending on the recording type. The method returns a recording info object, so the additional information can be specified in this object.

Parameters:  - **recordingGroupName** (*str*) – Name of the recording group.

- **path** (*str*) – Path to the recording.

Returns:  The recording info object.

Return type:  [*RecordingInfo*](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.RecordingInfo "tts.core.project.generator.paramGenerator.ParamGeneratorBase.RecordingInfo")

GetAttributes()[¶](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.GetAttributes "Link to this definition")  
Returns the dict of attributes.

Returns:  The dict of attributes

Return type:  dict

GetConstSet()[¶](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.GetConstSet "Link to this definition")  
Returns the set of constants.

Returns:  The set of constants.

Return type:  dict

GetName()[¶](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.GetName "Link to this definition")  
Returns the name of this cycle

Returns:  The name of this cycle

Return type:  str

GetParamSet()[¶](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.GetParamSet "Link to this definition")  
Returns the set of parameters.

Returns:  The set of parameters.

Return type:  dict

GetRecordingInfos()[¶](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.GetRecordingInfos "Link to this definition")  
Returns the dict of recording infos.

Returns:  The dict of recording infos.

Return type:  dict

SetName(*value*)[¶](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.SetName "Link to this definition")  
Sets the name of this cycle.

Parameters:  **value** (*str*) – Name for this cycle.

UpdateAttribute(*name*, *value*)[¶](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.UpdateAttribute "Link to this definition")  
Update an attribute

Parameters:  - **name** (*str*) – Name of the attribute

- **value** (*str*) – Value of the attribute

### OptimizerBase[¶](#module-tts.core.project.generator.paramGenerator.OptimizerBase "Link to this heading")

*class* OptimizerBase[¶](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase "Link to this definition")  
This is the base class for user-defined optimizers. The class is based on the CallbackParamGenerator and extends its functionality with new features:

> - Management of minimum and maximum values for the package parameters
>
> - Optional parameter variation before the actual optimization
>
> - A dialog for managing minimum and maximum values, parameter variation and optimizer-specific settings

If a parameter variation is activated, it is executed after calling PreGeneration and before calling Generate. With GetVariationResults the results of the variation can be accessed in the Generate method.

DESCRIPTION *= ''*[¶](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.DESCRIPTION "Link to this definition")  
A short description of the parameter generator.

Type:  str

Note

Setting this field is **optional**

ENABLE_PARAMETER_VARIATION *= True*[¶](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.ENABLE_PARAMETER_VARIATION "Link to this definition")  
Enables or disables the support of a parameter variation before the optimization starts.

Type:  boolean

ID *= ''*[¶](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.ID "Link to this definition")  
A universally unique identifier to make the parameter generator unique. The ID should be generated using a UUID generator to be unique.

Type:  str

Note

Setting this field is **mandatory**

NAME *= ''*[¶](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.NAME "Link to this definition")  
The display name of the parameter generator.

Type:  str

Note

Setting this field is **mandatory**

SERIALIZE*: dict[str, tuple[str, str] | tuple[str, str, object]] = {}*[¶](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.SERIALIZE "Link to this definition")  
Declaration of instance variables of the parameter generator, that are to be exported/imported to/from xml format (e.g. during saving/loading a project). The declaration contains an item for each instance variable in form of an dictionary. Example:

    SERIALIZE = {
                    "foo": ("FOO-VAR", "integer", 23),
                    "bar": ("BAR", "string"),
                    "params: ("PARAMETERS", "list")
                }

The declaration items key must match the name of the corresponding instance variable (e.g. for an instance variable self.foo the item’s key must be “foo”). The item’s value must be a tuple containing at least 2 elements. So the general syntax for a declaration item is:

    <variable name>: (<variable alias>, <type alias>, [default value])

Syntax and meaning of the tuple’s elements are:  
- **\<variable alias\>** declares the name of the xml element that is used for the variable’s xml representation.

- **\<type alias\>** keyword specifing the python variable’s type. The following table gives all keywords and their corresponding python type respectively:

  > - `boolean`: bool
  >
  > - `integer`: int
  >
  > - `long`: long
  >
  > - `float`: float
  >
  > - `string`: str
  >
  > - `unicode`: str

PLEASE NOTE: The types `long` and `unicode` are only kept for compatibility. Do not use these in new code.

- **\<default value\>** is an optional element. It specifies the variable’s default value. If the variable’s value equals its default value during export the variable is not exported at all. Conversely, the variable is assigned its default value during import if the xml data does not provide an value for the variable.

Type:  dict

Note

Setting this field is **optional**

api *= None*[¶](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.api "Link to this definition")  
Access to the internal ecu.test API. The API will be assigned at runtime, in order to be independent from ecu.test for testing purposes.

See also

[Internal APIs](../general_api/api.md#internalapi)

projectPath*: str | None = None*[¶](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.projectPath "Link to this definition")  
Absolute path to the project file containing the generator. In case of direct execution, this is the source project. In case of static generation it is the destination project.

Check()[¶](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.Check "Link to this definition")  
Implement this method to allow the user-implemented generator to be checked.

Returns:  A list of error messages or an empty list if everything is fine.

Return type:  list\<str\>

Note

Overriding this method is **optional**.

CreateCycleData(*paramSet=None*, *constSet=None*, *name=None*)[¶](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.CreateCycleData "Link to this definition")  
Method, to create an instance of class CycleData.

Parameters:  - **paramSet** (*dict*) – A set of parameters to parameterize a package.

- **constSet** (*dict*) – A set of constants that will be set before running a package. (optional)

- **name** (*str*) – A name for this cycle that will be displayed in the report. (optional)

Returns:  The cycle data object

Return type:  [`CycleData`](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData "tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData")

DryGenerationEnabled()[¶](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.DryGenerationEnabled "Link to this definition")  
Returns True, if the generator runs in dry generation mode. In this mode, the generator is used to generate a project with static parameter records.

Return type:  bool

Generate(*testRunFunction*)[¶](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.Generate "Link to this definition")  
Implement this method for generating parameter sets. Each parameter set must be an object of [`CycleData`](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData "tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData") and can be created with the method [`CreateCycleData()`](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.CreateCycleData "tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.CreateCycleData"). A test run is executed by calling the testRunFunction.

Parameters:  **testRunFunction** – If this function is called, an ecu.test test run is started. The function expects one or more parameter sets and returns a list of dictionaries containing the return variables of the package with their result values. A parameter set must be an instance of [`CycleData`](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData "tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData") which can be created with the method [`CreateCycleData()`](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.CreateCycleData "tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.CreateCycleData"). If the test run is aborted by ecu.test, an abort error occurs. This error should only be caught for the purpose of cleaning up.

Note

Overriding this method is **mandatory**

*classmethod* GetDescription()[¶](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.GetDescription "Link to this definition")  
Returns the description of the parameter generator. The description can be specified by setting the class variable [`DESCRIPTION`](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.DESCRIPTION "tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.DESCRIPTION").

Return type:  str

GetDialog()[¶](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.GetDialog "Link to this definition")  
Implement this method to return the configuration dialog of your parameter generator. The dialog should set the generator data.

Return type:  wx.Dialog or None

Note

Overriding this method is **optional**.

*classmethod* GetId()[¶](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.GetId "Link to this definition")  
Returns the universally unique identifier of the parameter generator. The identifier should be specified by setting the class variable [`ID`](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.ID "tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.ID").

Return type:  str

GetLastReturnSets()[¶](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.GetLastReturnSets "Link to this definition")  
Returns a list of all return sets from the last ecu.test test run.

This method only returns a result if the generator is not running in dry generation mode and it is called within the L{Generate()} method after at least one parameter set has been executed (by calling the testRunFunction in the L{Generate()} method). In all other circumstances, the method always returns an empty list.

Return type:  list of dicts

GetMinMaxValues()[¶](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.GetMinMaxValues "Link to this definition")  
Returns the specified minimum and maximum values for the package parameters. A dictionary is returned with the parameter names as keys and lists with minimum and maximum as values. Example:

    {'speed': [100, 120],
     'distance': [1000, 1500]
    }

Return type:  dict

*classmethod* GetName()[¶](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.GetName "Link to this definition")  
Returns the name of the parameter generator. The name should be specified by setting the class variable [`NAME`](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.NAME "tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.NAME").

Return type:  str

GetParameterText()[¶](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.GetParameterText "Link to this definition")  
Implement this method to show the parameters of your param generator in properties column.

Returns:  parameter text

Return type:  str

Note

Overriding this method is **optional**.

GetReportData()[¶](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.GetReportData "Link to this definition")  
Implement this method to set the information for the generator test step in the report. An object of type [`ReportData`](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.ReportData "tts.core.project.generator.paramGenerator.ParamGeneratorBase.ReportData") must be returned.

Return type:  [`ReportData`](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.ReportData "tts.core.project.generator.paramGenerator.ParamGeneratorBase.ReportData") or None

Note

Overriding this method is **optional**.

GetTargetItemCount()[¶](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.GetTargetItemCount "Link to this definition")  
Implement this method to define the expected number of cycle sets to be generated as information for progress indicators. Will be called for updates throughout the generation. Therefore, you can dynamically return the size of the current task.

Returns:  expected count of cycle sets to be generated

Return type:  int

GetUsedMappingItems()[¶](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.GetUsedMappingItems "Link to this definition")  
Returns the mapping items that will be used during generation.

If mapping items are to be added to the generated parameter sets of an analysis package, they have to be defined here in order to be registered for the stimulation package. Mapping items can be defined here directly, parsed from a file or whatever source, but the complete set of mapping items used during generation has to be returned by this method.

Note

Overriding this method is **optional** and only necessary for parameter set generators used with analysis packages and overwriting mapping items.

Attention

This method is called before any other method (e.g., PreGeneration)! If you read in required data for the mapping during PreGeneration, you have to redesign your code to be called at least once during GetUsedMappingItems.

Returns:  list of mapping items

Return type:  list[[ApiClient.MappingItem](../general_api/MappingApi.md#ApiClient.MappingItem "ApiClient.MappingItem")]

GetVariationResults()[¶](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.GetVariationResults "Link to this definition")  
Returns the results of the parameter variation as a list of [`VariationResult`](#tts.core.project.generator.paramGenerator.OptimizerBase.VariationResult "tts.core.project.generator.paramGenerator.OptimizerBase.VariationResult") objects. The method only returns results if it is called in the generator method and the parameter variation is activated. In all other circumstances, an empty list is returned.

Return type:  list\<[`VariationResult`](#tts.core.project.generator.paramGenerator.OptimizerBase.VariationResult "tts.core.project.generator.paramGenerator.OptimizerBase.VariationResult")\>

IsValidForAnalysisPackages()[¶](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.IsValidForAnalysisPackages "Link to this definition")  
Returns if usage of parameter set generator is feasible for analysis packages.

If set to ‘True’ and parameter set generator is not feasible for analysis packages, errors will be raised during runtime. If set to ‘False’, the GUI will give direct feedback if the parameter set generator is used for an analysis package.

Returns:  True, if valid for analysis package usage, else False

Return type:  bool

Note

Overriding this method is **optional**.

OnInit(*packageInfo*)[¶](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.OnInit "Link to this definition")  
Implement this method to process information about the package to which the generator belongs. It will be called before [`PreGeneration()`](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.PreGeneration "tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.PreGeneration") or [`GetDialog()`](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.GetDialog "tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.GetDialog") is called.

Parameters:  **packageInfo** ([`PackageInfo`](#tts.core.project.projectStep.PackageInfo.PackageInfo "tts.core.project.projectStep.PackageInfo.PackageInfo")) – The package info object.

Note

Overriding this method is **optional**

PostGeneration()[¶](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.PostGeneration "Link to this definition")  
Implement this method to specify post generation behavior. This method is called after the generation. This method will be called even if an exception occurs during generation (incl. PreGeneration), but not if the project execution is aborted (by the user or because of an “abort on error” setting).

Note

Overriding this method is **optional**.

PreGeneration()[¶](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.PreGeneration "Link to this definition")  
Implement this method to specify pre generation behavior. This method is called before the generation.

Note

Overriding this method is **optional**.

*class* VariationResult[¶](#tts.core.project.generator.paramGenerator.OptimizerBase.VariationResult "Link to this definition")  
This class is a container for the input and result data of one variation.

CycleData[¶](#tts.core.project.generator.paramGenerator.OptimizerBase.VariationResult.CycleData "Link to this definition")  
Returns the cycle data object that contains the input data for the variation.

Returns:  The cycle data object

Return type:  [`CycleData`](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData "tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData")

ReturnSet[¶](#tts.core.project.generator.paramGenerator.OptimizerBase.VariationResult.ReturnSet "Link to this definition")  
Returns the return set of the package execution for the variation.

Returns:  The return set as a dictionary

Return type:  dict, None

### PackageInfo[¶](#module-tts.core.project.projectStep.PackageInfo "Link to this heading")

*class* PackageInfo[¶](#tts.core.project.projectStep.PackageInfo.PackageInfo "Link to this definition")  
Provides information about a package, like name, variables, etc.

GetName()[¶](#tts.core.project.projectStep.PackageInfo.PackageInfo.GetName "Link to this definition")  
Returns the package name.

Returns:  package name without extension

Return type:  str

GetParameterVariables()[¶](#tts.core.project.projectStep.PackageInfo.PackageInfo.GetParameterVariables "Link to this definition")  
Returns a list of all variables defined in the package and set as a parameter.

Returns:  List of all defined parameters

Return type:  list \<`Variable`\>

GetPath()[¶](#tts.core.project.projectStep.PackageInfo.PackageInfo.GetPath "Link to this definition")  
Returns the path of the package file as absolute path.

Returns:  absolute package path

Return type:  str

GetReturnVariables()[¶](#tts.core.project.projectStep.PackageInfo.PackageInfo.GetReturnVariables "Link to this definition")  
Returns a list of all variables defined in the package and set as a return variable.

Returns:  List of all defined return variables

Return type:  list \<`Variable`\>

GetVariables()[¶](#tts.core.project.projectStep.PackageInfo.PackageInfo.GetVariables "Link to this definition")  
Returns a list of all variables defined in the package.

Returns:  List of all defined variables

Return type:  list \<`Variable`\>

### ParamGenerator[¶](#module-tts.core.project.generator.paramGenerator.ParamGenerator "Link to this heading")

*class* ParamGenerator[¶](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator "Link to this definition")  
This is the base class for user-defined parameter generators and all implementations should be derived from this class. It defines specific methods that are called during generation of parameter sets. The desired behavior of a parameter generator is achieved by overwriting the methods provided for this purpose.

Some fields and methods *must* be overridden (**mandatory**), others *may* be overridden (**optional**). There are also methods that are only to be called by the user implementation and should not be overridden (those without a note).

DESCRIPTION *= ''*[¶](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.DESCRIPTION "Link to this definition")  
A short description of the parameter generator.

Type:  str

Note

Setting this field is **optional**

ID *= ''*[¶](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.ID "Link to this definition")  
A universally unique identifier to make the parameter generator unique. The ID should be generated using a UUID generator to be unique.

Type:  str

Note

Setting this field is **mandatory**

NAME *= ''*[¶](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.NAME "Link to this definition")  
The display name of the parameter generator.

Type:  str

Note

Setting this field is **mandatory**

SERIALIZE*: dict[str, tuple[str, str] | tuple[str, str, object]] = {}*[¶](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.SERIALIZE "Link to this definition")  
Declaration of instance variables of the parameter generator, that are to be exported/imported to/from xml format (e.g. during saving/loading a project). The declaration contains an item for each instance variable in form of an dictionary. Example:

    SERIALIZE = {
                    "foo": ("FOO-VAR", "integer", 23),
                    "bar": ("BAR", "string"),
                    "params: ("PARAMETERS", "list")
                }

The declaration items key must match the name of the corresponding instance variable (e.g. for an instance variable self.foo the item’s key must be “foo”). The item’s value must be a tuple containing at least 2 elements. So the general syntax for a declaration item is:

    <variable name>: (<variable alias>, <type alias>, [default value])

Syntax and meaning of the tuple’s elements are:  
- **\<variable alias\>** declares the name of the xml element that is used for the variable’s xml representation.

- **\<type alias\>** keyword specifing the python variable’s type. The following table gives all keywords and their corresponding python type respectively:

  > - `boolean`: bool
  >
  > - `integer`: int
  >
  > - `long`: int
  >
  > - `float`: float
  >
  > - `string`: str
  >
  > - `unicode`: str
  >
  > - `list`: list
  >
  > - `dict`: dict

PLEASE NOTE: Keys of dictionaries being (de-)serialized must be strings. Furthermore values of dictionaries and lists are required to be of type `bool`, `int`, `float`, `str`, `list` or `dict`. The same restrictions apply to embedded lists and dictionaries. The types `long` and `unicode` are only kept for compatibility. Do not use these in new code.

- **\<default value\>** is an optional element. It specifies the variable’s default value. If the variable’s value equals its default value during export the variable is not exported at all. Conversely, the variable is assigned its default value during import if the xml data does not provide an value for the variable.

Type:  dict

Note

Setting this field is **optional**

api *= None*[¶](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.api "Link to this definition")  
Access to the internal ecu.test API. The API will be assigned at runtime, in order to be independent from ecu.test for testing purposes.

See also

[Internal APIs](../general_api/api.md#internalapi)

projectPath*: str | None = None*[¶](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.projectPath "Link to this definition")  
Absolute path to the project file containing the generator. In case of direct execution, this is the source project. In case of static generation it is the destination project.

Check()[¶](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.Check "Link to this definition")  
Implement this method to allow the user-implemented generator to be checked.

Returns:  A list of error messages or an empty list if everything is fine.

Return type:  list\<str\>

Note

Overriding this method is **optional**.

CreateCycleData(*paramSet=None*, *constSet=None*, *name=None*)[¶](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.CreateCycleData "Link to this definition")  
Method, to create an instance of class CycleData.

Parameters:  - **paramSet** (*dict*) – A set of parameters to parameterize a package.

- **constSet** (*dict*) – A set of constants that will be set before running a package. (optional)

- **name** (*str*) – A name for this cycle that will be displayed in the report. (optional)

Returns:  The cycle data object

Return type:  [`CycleData`](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData "tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData")

DryGenerationEnabled()[¶](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.DryGenerationEnabled "Link to this definition")  
Returns True, if the generator runs in dry generation mode. In this mode, the generator is used to generate a project with static parameter records.

Return type:  bool

GenerationIterator()[¶](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.GenerationIterator "Link to this definition")  
Implement this method for generating parameter sets. Each parameter set must be an object of [`CycleData`](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData "tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData") and can be created with the method [`CreateCycleData()`](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.CreateCycleData "tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.CreateCycleData"). Since this is a python iterator, the parameter sets must be returned with the keyword ‘yield’. Either a single parameter set or a list of parameter sets can be yielded.

Example:

    def GenerationIterator(self):
        for line in file:
            yield CreateCycleData({'lineData': line})

Note

Overriding this method is **mandatory**

*classmethod* GetDescription()[¶](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.GetDescription "Link to this definition")  
Returns the description of the parameter generator. The description can be specified by setting the class variable [`DESCRIPTION`](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.DESCRIPTION "tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.DESCRIPTION").

Return type:  str

GetDialog()[¶](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.GetDialog "Link to this definition")  
Implement this method to return the configuration dialog of your parameter generator. The dialog should set the generator data.

Return type:  wx.Dialog or None

Note

Overriding this method is **optional**.

*classmethod* GetId()[¶](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.GetId "Link to this definition")  
Returns the universally unique identifier of the parameter generator. The identifier should be specified by setting the class variable [`ID`](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.ID "tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.ID").

Return type:  str

GetLastReturnSet()[¶](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.GetLastReturnSet "Link to this definition")  
Returns the return set of the last package execution.

This method only returns a result if the generator is not running in dry generation mode and it is called within the [`GenerationIterator()`](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.GenerationIterator "tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.GenerationIterator") method after at least one parameter set has been executed (by a yield in the [`GenerationIterator()`](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.GenerationIterator "tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.GenerationIterator") method). In all other circumstances, the method always returns None.

Return type:  dict, None

*classmethod* GetName()[¶](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.GetName "Link to this definition")  
Returns the name of the parameter generator. The name should be specified by setting the class variable [`NAME`](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.NAME "tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.NAME").

Return type:  str

GetParameterText()[¶](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.GetParameterText "Link to this definition")  
Implement this method to show the parameters of your param generator in properties column.

Returns:  parameter text

Return type:  str

Note

Overriding this method is **optional**.

GetReportData()[¶](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.GetReportData "Link to this definition")  
Implement this method to set the information for the generator test step in the report. An object of type [`ReportData`](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.ReportData "tts.core.project.generator.paramGenerator.ParamGeneratorBase.ReportData") must be returned.

Return type:  [`ReportData`](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.ReportData "tts.core.project.generator.paramGenerator.ParamGeneratorBase.ReportData") or None

Note

Overriding this method is **optional**.

GetTargetItemCount()[¶](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.GetTargetItemCount "Link to this definition")  
Implement this method to define the expected number of cycle sets to be generated as information for progress indicators. Will be called for updates throughout the generation. Therefore, you can dynamically return the size of the current task.

Returns:  expected count of cycle sets to be generated

Return type:  int

GetUsedMappingItems()[¶](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.GetUsedMappingItems "Link to this definition")  
Returns the mapping items that will be used during generation.

If mapping items are to be added to the generated parameter sets of an analysis package, they have to be defined here in order to be registered for the stimulation package. Mapping items can be defined here directly, parsed from a file or whatever source, but the complete set of mapping items used during generation has to be returned by this method.

Note

Overriding this method is **optional** and only necessary for parameter set generators used with analysis packages and overwriting mapping items.

Attention

This method is called before any other method (e.g., PreGeneration)! If you read in required data for the mapping during PreGeneration, you have to redesign your code to be called at least once during GetUsedMappingItems.

Returns:  list of mapping items

Return type:  list[[ApiClient.MappingItem](../general_api/MappingApi.md#ApiClient.MappingItem "ApiClient.MappingItem")]

IsValidForAnalysisPackages()[¶](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.IsValidForAnalysisPackages "Link to this definition")  
Returns if usage of parameter set generator is feasible for analysis packages.

If set to ‘True’ and parameter set generator is not feasible for analysis packages, errors will be raised during runtime. If set to ‘False’, the GUI will give direct feedback if the parameter set generator is used for an analysis package.

Returns:  True, if valid for analysis package usage, else False

Return type:  bool

Note

Overriding this method is **optional**.

OnInit(*packageInfo*)[¶](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.OnInit "Link to this definition")  
Implement this method to process information about the package to which the generator belongs. It will be called before [`PreGeneration()`](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.PreGeneration "tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.PreGeneration") or [`GetDialog()`](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.GetDialog "tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.GetDialog") is called.

Parameters:  **packageInfo** ([`PackageInfo`](#tts.core.project.projectStep.PackageInfo.PackageInfo "tts.core.project.projectStep.PackageInfo.PackageInfo")) – The package info object.

Note

Overriding this method is **optional**

PostGeneration()[¶](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.PostGeneration "Link to this definition")  
Implement this method to specify post generation behavior. This method is called after the generation. This method will be called even if an exception occurs during generation (incl. PreGeneration), but not if the project execution is aborted (by the user or because of an “abort on error” setting).

Note

Overriding this method is **optional**.

PreGeneration()[¶](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.PreGeneration "Link to this definition")  
Implement this method to specify pre generation behavior. This method is called before the generation.

Note

Overriding this method is **optional**.

### RecordingInfo[¶](#recordinginfo "Link to this heading")

*class* RecordingInfo[¶](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.RecordingInfo "Link to this definition")  
This class is a container for the information of a recording.

FormatDetails[¶](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.RecordingInfo.FormatDetails "Link to this definition")  
Returns the format details of the recording.

Returns:  Format details of the recording.

Return type:  str

Path[¶](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.RecordingInfo.Path "Link to this definition")  
Returns the path to the recording.

Returns:  Path to the recording.

Return type:  str

RecordingName[¶](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.RecordingInfo.RecordingName "Link to this definition")  
Returns the name of the recording.

Returns:  Name of the recording.

Return type:  str

RecordingNumber[¶](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.RecordingInfo.RecordingNumber "Link to this definition")  
Returns the number of the recording.

Returns:  Number of the recording.

Return type:  int

RecordingType[¶](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.RecordingInfo.RecordingType "Link to this definition")  
Returns the type of the recording.

Returns:  Type of the recording.

Return type:  str

GetFormatDetails()[¶](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.RecordingInfo.GetFormatDetails "Link to this definition")  
Returns the format details of the recording.

Returns:  Format details of the recording.

Return type:  str

GetPath()[¶](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.RecordingInfo.GetPath "Link to this definition")  
Returns the path to the recording.

Returns:  Path to the recording.

Return type:  str

GetRecordingName()[¶](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.RecordingInfo.GetRecordingName "Link to this definition")  
Returns the name of the recording.

Returns:  Name of the recording.

Return type:  str

GetRecordingNumber()[¶](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.RecordingInfo.GetRecordingNumber "Link to this definition")  
Returns the number of the recording.

Returns:  Number of the recording.

Return type:  int

GetRecordingType()[¶](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.RecordingInfo.GetRecordingType "Link to this definition")  
Returns the type of the recording.

Returns:  Type of the recording.

Return type:  str

SetFormatDetails(*formatDetails*)[¶](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.RecordingInfo.SetFormatDetails "Link to this definition")  
Sets the format details of the recording.

Parameters:  **formatDetails** (*str*) – Format details of the recording.

SetRecordingName(*recordingName*)[¶](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.RecordingInfo.SetRecordingName "Link to this definition")  
Sets the name of the recording.

Parameters:  **recordingName** (*str*) – Name of the recording.

SetRecordingNumber(*recordingNumber*)[¶](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.RecordingInfo.SetRecordingNumber "Link to this definition")  
Sets the number of the recording.

Parameters:  **recordingNumber** (*str*) – Number of the recording.

SetRecordingType(*recordingType*)[¶](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.RecordingInfo.SetRecordingType "Link to this definition")  
Sets the type of the recording.

Parameters:  **recordingType** (*str*) – Type of the recording.

`\_\_init\_\_`(*path*)[¶](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.RecordingInfo.__init__ "Link to this definition")  
Method, to initialize an instance of this class.

Parameters:  **path** (*str*) – Path to the recording.

### ReportData[¶](#reportdata "Link to this heading")

*class* ReportData[¶](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.ReportData "Link to this definition")  
This class is a container for the information of the generator test step shown in the report

Comment[¶](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.ReportData.Comment "Link to this definition")  
Returns the string for the comment column

Returns:  String for the comment column

Return type:  str

Value[¶](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.ReportData.Value "Link to this definition")  
Returns the string for the value column

Returns:  String for the value column

Return type:  str

GetComment()[¶](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.ReportData.GetComment "Link to this definition")  
Returns the string for the comment column

Returns:  String for the comment column

Return type:  str

GetValue()[¶](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.ReportData.GetValue "Link to this definition")  
Returns the string for the value column

Returns:  String for the value column

Return type:  str

SetComment(*comment*)[¶](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.ReportData.SetComment "Link to this definition")  
Sets the string for the comment column

Parameters:  **comment** (*str*) – String for the comment column

SetValue(*value*)[¶](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.ReportData.SetValue "Link to this definition")  
Sets the string for the value column

Parameters:  **value** (*str*) – String for the value column

### Variable[¶](#variable "Link to this heading")

*class* Variable  
Description  
returns the description of this variable.

Returns:  the description of this variable

Return type:  str

InitValue  
returns the initial value of this variable.

Returns:  the initial value of this variable

Return type:  str

Name  
returns the name of this variable.

Returns:  the name of this variable

Return type:  str

VariableType  
Returns:  type of this variable

Return type:  str

GetDescription()  
returns the description of this variable.

Returns:  the description of this variable

Return type:  str

GetInitValue()  
returns the initial value of this variable.

Returns:  the initial value of this variable

Return type:  str

GetName()  
returns the name of this variable.

Returns:  the name of this variable

Return type:  str

GetVariableType()  
Returns:  type of this variable

Return type:  str

IsInput()  
Returns True if this variable is an input parameter, otherwise False

IsOutput()  
Returns True if this variable is an output parameter, otherwise False

*class* VariableType  
Defines type of the variable

Variables:  
- **UNDEFINED** – u”Undefined”

- **NUMERIC** – u”Numeric”

- **STRING** – u”String”

- **ENUM** – u”Enum”

- **TEXTTABLE** – u”Texttable”

- **BOOL** – u”Boolean”

### VariationResult[¶](#variationresult "Link to this heading")

*class* VariationResult  
This class is a container for the input and result data of one variation.

CycleData  
Returns the cycle data object that contains the input data for the variation.

Returns:  The cycle data object

Return type:  [`CycleData`](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData "tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData")

ReturnSet  
Returns the return set of the package execution for the variation.

Returns:  The return set as a dictionary

Return type:  dict, None

## Project package generator API[¶](#project-package-generator-api "Link to this heading")

### PackageGenerator[¶](#module-tts.core.project.generator.PackageGenerator "Link to this heading")

*class* CycleData[¶](#tts.core.project.generator.PackageGenerator.CycleData "Link to this definition")  
A container for all data that can be generated during one cycle.

Name[¶](#tts.core.project.generator.PackageGenerator.CycleData.Name "Link to this definition")  
Returns the name of this cycle

Returns:  The name of this cycle

Return type:  str

objectApi *= None*[¶](#tts.core.project.generator.PackageGenerator.CycleData.objectApi "Link to this definition")  
The Object API which is used to create test steps.

Type:  [`ApiClient.ApiClient`](../general_api/objectApi.md#ApiClient.ApiClient "ApiClient.ApiClient")

packageInstance *= None*[¶](#tts.core.project.generator.PackageGenerator.CycleData.packageInstance "Link to this definition")  
The package instance to be completed and executed. Based on a provided template or empty.

Type:  [`ApiClient.Package`](../general_api/PackageApi.md#ApiClient.Package "ApiClient.Package")

AppendParameterSet(*name*)[¶](#tts.core.project.generator.PackageGenerator.CycleData.AppendParameterSet "Link to this definition")  
Appends a parameter set for this cycle.

Parameters:  **name** (*str*) – Name of the parameter set that will be displayed in the report.

Returns:  Parameter set

Return type:  [`ApiClient.ParameterSet`](../general_api/ProjectApi.md#ApiClient.ParameterSet "ApiClient.ParameterSet")

GetName()[¶](#tts.core.project.generator.PackageGenerator.CycleData.GetName "Link to this definition")  
Returns the name of this cycle

Returns:  The name of this cycle

Return type:  str

GetParameterSets()[¶](#tts.core.project.generator.PackageGenerator.CycleData.GetParameterSets "Link to this definition")  
Returns a list of all parameter sets assigned to this cycle.

Returns:  List of parameter sets for this cycle.

Return type:  list\<[`ApiClient.ParameterSet`](../general_api/ProjectApi.md#ApiClient.ParameterSet "ApiClient.ParameterSet")\>

SetName(*value*)[¶](#tts.core.project.generator.PackageGenerator.CycleData.SetName "Link to this definition")  
Sets the name of this cycle.

Parameters:  **value** (*str*) – Name for this cycle.

*class* PackageGenerator[¶](#tts.core.project.generator.PackageGenerator.PackageGenerator "Link to this definition")  
This is the base class for user defined package generators. All package generators should be derived form this class. It defines specific methods that are called during generation of packages. The required behaviour of a package generator is implemented by overwriting these methods.

Some fields and methods *must* be overridden (**mandatory**), others *may* be overridden (**optional**). There are also methods that are only to be called by the user implementation and should not be overridden (those without a note).

DESCRIPTION *= ''*[¶](#tts.core.project.generator.PackageGenerator.PackageGenerator.DESCRIPTION "Link to this definition")  
A short description of the package generator.

Type:  str

ID *= ''*[¶](#tts.core.project.generator.PackageGenerator.PackageGenerator.ID "Link to this definition")  
A universally unique identifier to make the package generator unique. The ID should be generated automatically to be unique.

Type:  str

Note

Setting this field is **mandatory**

NAME *= ''*[¶](#tts.core.project.generator.PackageGenerator.PackageGenerator.NAME "Link to this definition")  
The display name of the package generator.

Type:  str

Note

Setting this field is **mandatory**

SERIALIZE*: dict[str, tuple[str, str] | tuple[str, str, object]] = {}*[¶](#tts.core.project.generator.PackageGenerator.PackageGenerator.SERIALIZE "Link to this definition")  
Declaration of instance variables of the package generator, that are to be exported/imported to/from xml format (e.g. during saving/loading a project). The declaration contains an item for each instance variable in form of an dictionary. Example:

    SERIALIZE = {
                    "foo": ("FOO-VAR", "integer", 23),
                    "bar": ("BAR", "string"),
                    "params: ("PARAMETERS", "list")
                }

The declaration items key must match the name of the corresponding instance variable (e.g. for an instance variable self.foo the item’s key must be “foo”). The item’s value must be a tuple containing at least 2 elements. So the general syntax for a declaration item is:

    <variable name>: (<variable alias>, <type alias>, [default value])

Syntax and meaning of the tuple’s elements are:

> - **\<variable alias\>** declares the name of the xml element that is used for the variable’s xml representation.
>
> - **\<type alias\>** keyword specifing the python variable’s type. The following table gives all keywords and their corresponding python type respectively:
>
>   > - `boolean`: bool
>   >
>   > - `integer`: int
>   >
>   > - `long`: int
>   >
>   > - `float`: float
>   >
>   > - `string`: str
>   >
>   > - `unicode`: str
>   >
>   > - `list`: list
>   >
>   > - `dict`: dict
>
> PLEASE NOTE: Keys of dictionaries being (de-)serialized must be strings. Furthermore values of dictionaries and lists are required to be of type `bool`, `int`, `float`, `str`, `list` or `dict`. The same restrictions apply to embedded lists and dictionaries. The types `long` and `unicode` are only kept for compatibility. Do not use these in new code.
>
> - **\<default value\>** is an optional element. It specifies the variable’s default value. If the variable’s value equals its default value during export the variable is not exported at all. Conversely, the variable is assigned its default value during import if the xml data does not provide an value for the variable.

Type:  dict

api *= None*[¶](#tts.core.project.generator.PackageGenerator.PackageGenerator.api "Link to this definition")  
Access to the internal ecu.test API. The API will be assigned at runtime, in order to be independent from ecu.test for testing purposes.

See also

[Internal APIs](../general_api/api.md#internalapi)

projectPath *= None*[¶](#tts.core.project.generator.PackageGenerator.PackageGenerator.projectPath "Link to this definition")  
Absolute path to the project file containing the generator. In case of direct execution, this is the source project. In case of static generation it is the destination project.

Check()[¶](#tts.core.project.generator.PackageGenerator.PackageGenerator.Check "Link to this definition")  
Implement this method to allow checking of of the user-implemented generator.

Returns:  A list of error messages or an empty list if everything is fine.

Return type:  list\<str\>

Note

Overriding this method is **optional**

CreateCycleData(*name=None*, *template=None*)[¶](#tts.core.project.generator.PackageGenerator.PackageGenerator.CreateCycleData "Link to this definition")  
Creates an instance of class CycleData.

Parameters:  - **name** (*str*) – A name for this cycle that will be displayed in the report. (optional)

- **template** (*str*) – Path to template package file to be used as base for generator. (optional)

Returns:  The cycle data object

Return type:  [`CycleData`](#tts.core.project.generator.PackageGenerator.CycleData "tts.core.project.generator.PackageGenerator.CycleData")

DryGenerationEnabled()[¶](#tts.core.project.generator.PackageGenerator.PackageGenerator.DryGenerationEnabled "Link to this definition")  
Returns True, if the generator runs in dry generation mode. In this mode, the generator is used to generate a project with static packages.

Return type:  bool

GenerationIterator()[¶](#tts.core.project.generator.PackageGenerator.PackageGenerator.GenerationIterator "Link to this definition")  
Implement this method for the generation of the data for on cycle. This is an iterator and it should return an [`CycleData`](#tts.core.project.generator.PackageGenerator.CycleData "tts.core.project.generator.PackageGenerator.CycleData") object with the python keyword ‘yield’. To create an [`CycleData`](#tts.core.project.generator.PackageGenerator.CycleData "tts.core.project.generator.PackageGenerator.CycleData") object, use the method [`CreateCycleData()`](#tts.core.project.generator.PackageGenerator.PackageGenerator.CreateCycleData "tts.core.project.generator.PackageGenerator.PackageGenerator.CreateCycleData") and store all information in this object. Example:

    def GenerationIterator(self):
        for line in file:
            yield CreateCycleData({'lineData': line})

Note

Overriding this method is **mandatory**

*classmethod* GetDescription()[¶](#tts.core.project.generator.PackageGenerator.PackageGenerator.GetDescription "Link to this definition")  
Returns the description of the package generator. The description can be specified by setting the class variable [`DESCRIPTION`](#tts.core.project.generator.PackageGenerator.PackageGenerator.DESCRIPTION "tts.core.project.generator.PackageGenerator.PackageGenerator.DESCRIPTION").

Return type:  str

GetDialog()[¶](#tts.core.project.generator.PackageGenerator.PackageGenerator.GetDialog "Link to this definition")  
Implement this method to return the configuration dialog of your package generator. The dialog should set the generator data.

Return type:  wx.Dialog, None

Note

Overriding this method is **optional**

*classmethod* GetFormatRev()[¶](#tts.core.project.generator.PackageGenerator.PackageGenerator.GetFormatRev "Link to this definition")  
Returns the format revision of the package generator. The format revision can be specified by setting the class variable `FORMAT_REV`. This is an optional parameter.

Return type:  int

*classmethod* GetId()[¶](#tts.core.project.generator.PackageGenerator.PackageGenerator.GetId "Link to this definition")  
Returns the universally unique identifier of the package generator. The identifier should be specified by setting the class variable [`ID`](#tts.core.project.generator.PackageGenerator.PackageGenerator.ID "tts.core.project.generator.PackageGenerator.PackageGenerator.ID").

Return type:  str

*classmethod* GetName()[¶](#tts.core.project.generator.PackageGenerator.PackageGenerator.GetName "Link to this definition")  
Returns the name of the package generator. The name should be specified by setting the class variable [`NAME`](#tts.core.project.generator.PackageGenerator.PackageGenerator.NAME "tts.core.project.generator.PackageGenerator.PackageGenerator.NAME").

Return type:  str

GetParameterText()[¶](#tts.core.project.generator.PackageGenerator.PackageGenerator.GetParameterText "Link to this definition")  
Implement this method to show the parameters of your package generator in properties column.

Returns:  parameter text

Return type:  str

Note

Overriding this method is **optional**

GetTargetItemCount()[¶](#tts.core.project.generator.PackageGenerator.PackageGenerator.GetTargetItemCount "Link to this definition")  
Implement this method to define the expected number of cycle sets to be generated as information for progress indicators. Will be called for updates throughout the generation. Therefore you can dynamically return the size of the current task.

Returns:  expected count of cycle sets to be generated

Return type:  int

PostGeneration()[¶](#tts.core.project.generator.PackageGenerator.PackageGenerator.PostGeneration "Link to this definition")  
Implement this method to specify post generation behavior. This method is called after the generation. This method will be called even if an exception occurs during generation (incl. PreGeneration), but not if the project execution is aborted (by the user or because of an “abort on error” setting).

Note

Overriding this method is **optional**

PreGeneration()[¶](#tts.core.project.generator.PackageGenerator.PackageGenerator.PreGeneration "Link to this definition")  
Implement this method to specify pre generation behavior. This method is called before the generation.

Note

Overriding this method is **optional**

## ReferenceTestPackageGenerator[¶](#referencetestpackagegenerator "Link to this heading")

### ReferenceTestPackageGeneratorTools[¶](#referencetestpackagegeneratortools "Link to this heading")

*class* ReferenceTestPackageGeneratorTools[¶](#tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.ReferenceTestPackageGeneratorTools "Link to this definition")  
This class provides convenience methods that can be used within the user code section of the Reference Test Package Generator.

An instance of this class is globally available as variable ‘tools’

*static* AppendTraceAnalysisReference(*traceAnalysis*, *analysisReference*, *refName*, *testName*)[¶](#tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.ReferenceTestPackageGeneratorTools.AppendTraceAnalysisReference "Link to this definition")  
Adds analysis reference trace step to the current trace analysis. The created [`ApiClient.TraceAnalysisReference`](../general_api/TraceAnalysisApi.md#ApiClient.TraceAnalysisReference "ApiClient.TraceAnalysisReference"). object is returned.

Parameters:  - **traceAnalysis** ([`ApiClient.TraceAnalysis`](../general_api/TraceAnalysisApi.md#ApiClient.TraceAnalysis "ApiClient.TraceAnalysis")) – the current reference test trace analysis object

- **analysisReference** (*string*) – name of the episode

- **refName** (*string*) – name of the reference signal

- **testName** (*string*) – name of the test signal

Returns:  object of the analysis reference trace step

Return type:  [`ApiClient.TraceAnalysisReference`](../general_api/TraceAnalysisApi.md#ApiClient.TraceAnalysisReference "ApiClient.TraceAnalysisReference")

*static* ApplyPattern(*string*, *pattern*, *debug=False*)[¶](#tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.ReferenceTestPackageGeneratorTools.ApplyPattern "Link to this definition")  
Reduces a string according to a wildcard pattern.

Pattern syntax:  
`( )`… denotes part of the string that is of interest

`*` … substitute for any string

`?` … substitute for any character

If the pattern does not match the string, the full string is returned as is.

Example:  
`string = 'Signal_XY', pattern = 'Signal_(*)', result: 'XY'`Parameters:  
- **string** (*str*) – String that is to be reduced

- **pattern** (*str*) – Pattern that is to be applied to the string

- **debug** – Set to True to create debug prints

Returns:  Reduced substring or full string, if pattern does not match

*static* EnablePlot(*traceStep*, *plotName=''*)[¶](#tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.ReferenceTestPackageGeneratorTools.EnablePlot "Link to this definition")  
Adds a plot to the given traceStep with all signals used by the traceStep.

Parameters:  - **traceStep** ([`ApiClient.TraceStep`](../general_api/TraceAnalysisApi.md#ApiClient.TraceStep "ApiClient.TraceStep")) – the traceStep for which the plot will be enabled

- **plotName** (*string,* *optional*) – name of the plot, defaults to ‘Signal plot’

*static* Filter(*signalList*, *includeFilter*, *excludeFilter=''*)[¶](#tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.ReferenceTestPackageGeneratorTools.Filter "Link to this definition")  
Removes signals from a list according to certain criteria.

The filter syntax corresponds to the Filter syntax as described in the ecu.test User Documentation under “Handling \> Filter”.

Parameters:  - **signalList** (List of [`Signal`](#tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.Signal "tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.Signal") objects) – List with [`Signal`](#tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.Signal "tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.Signal") objects that is to be reduced

- **includeFilter** (*str*) –

  Filter to include certain signals. An empty filter includes everything.

  E.g.: `"name = '*_important'"`(this can also be abbreviated to `"'*_important'"`)

- **excludeFilter** (*str*) –

  Filter to exclude certain signals. An empty filter excludes nothing.

  E.g.: `"device != 'Primary'"`Returns:  
List of filtered [`Signal`](#tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.Signal "tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.Signal") objects

*static* GetOrCreateEpisode(*traceAnalysis*, *episodeName=None*)[¶](#tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.ReferenceTestPackageGeneratorTools.GetOrCreateEpisode "Link to this definition")  
The episode with the specified name is returned. If no name is specified, the first episode is returned. If no episode (with the specified name) yet exists, a new episode will be created and appended to the traceAnalysis. The newly created [`ApiClient.Episode`](../general_api/TraceAnalysisApi.md#ApiClient.Episode "ApiClient.Episode") object is returned.

Parameters:  - **traceAnalysis** ([`ApiClient.TraceAnalysis`](../general_api/TraceAnalysisApi.md#ApiClient.TraceAnalysis "ApiClient.TraceAnalysis")) – the current reference test trace analysis object

- **episodeName** (*string,* *optional*) – name of the episode

Returns:  object of the episode

Return type:  [`ApiClient.Episode`](../general_api/TraceAnalysisApi.md#ApiClient.Episode "ApiClient.Episode")

### Signal[¶](#signal "Link to this heading")

*class* Signal[¶](#tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.Signal "Link to this definition")  
Represents a single signal inside a trace file. Signals can be easily compared with other Signal objects. Signals can also be used as a set for bulk operations.

device[¶](#tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.Signal.device "Link to this definition")  
Returns:  device name within trace file

Return type:  string

name[¶](#tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.Signal.name "Link to this definition")  
Returns:  signal name

Return type:  string

type[¶](#tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.Signal.type "Link to this definition")  
Returns:  type of trace file (ref|test)

Return type:  string

GetSignalGroupName()[¶](#tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.Signal.GetSignalGroupName "Link to this definition")  
Returns the signal group name of this signal.

Returns:  signal group name

Return type:  string
