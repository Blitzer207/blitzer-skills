[![logo](../../_static/ecu.test.svg)](../../index.html "API  documentation") API documentation

[ Internal APIs ](../../general_api/api.md)

[ Advanced operations of package variable types ](../../general_api/variabledatastructures.md)

[ Advanced properties of bus-related objects ](../../general_api/busdatastructures.md)

[ Bus related objects of trace analysis ](../../general_api/busdatastructuresTraceanalysis.md)

[ Advanced properties of diagnostics-related objects ](../../general_api/diagdatastructures.md)

[ Diagnostics related objects of trace analysis ](../../general_api/diagdatastructuresTraceanalysis.md)

[ Advanced properties of media-related objects ](../../general_api/mediadatastructures.md)

[ Advanced properties of DLT logging-related objects ](../../general_api/dltdatastructures.md)

[ COM API ](../../general_api/com-api.md)

[ REST API ](../../general_api/rest-api.md)

[ Report API ](../../general_api/apireport.md)

[ Object API ](../../general_api/objectApi.md)

[ Trace Analysis API ](../../TraceAnalysisAPI/index.md)

[ Generator APIs ](../index.md)

Generator APIs

Project Generator API [ Project Generator API ](#)

Project Generator API

- [ ProjectGenerator ](#projectgenerator)
  - [C ProjectGenerator ](#tts.core.project.generator.ProjectGenerator.ProjectGenerator)
    - [A DESCRIPTION ](#tts.core.project.generator.ProjectGenerator.ProjectGenerator.DESCRIPTION)
    - [A FORMAT_REV ](#tts.core.project.generator.ProjectGenerator.ProjectGenerator.FORMAT_REV)
    - [A ID ](#tts.core.project.generator.ProjectGenerator.ProjectGenerator.ID)
    - [A NAME ](#tts.core.project.generator.ProjectGenerator.ProjectGenerator.NAME)
    - [A SERIALIZE ](#tts.core.project.generator.ProjectGenerator.ProjectGenerator.SERIALIZE)
    - [A api ](#tts.core.project.generator.ProjectGenerator.ProjectGenerator.api)
    - [A projectPath ](#tts.core.project.generator.ProjectGenerator.ProjectGenerator.projectPath)
    - [A sourceProjectPath ](#tts.core.project.generator.ProjectGenerator.ProjectGenerator.sourceProjectPath)
    - [M GetDescription ](#tts.core.project.generator.ProjectGenerator.ProjectGenerator.GetDescription)
    - [M GetFormatRev ](#tts.core.project.generator.ProjectGenerator.ProjectGenerator.GetFormatRev)
    - [M GetId ](#tts.core.project.generator.ProjectGenerator.ProjectGenerator.GetId)
    - [M GetName ](#tts.core.project.generator.ProjectGenerator.ProjectGenerator.GetName)
    - [M Check ](#tts.core.project.generator.ProjectGenerator.ProjectGenerator.Check)
    - [M CreateCycleData ](#tts.core.project.generator.ProjectGenerator.ProjectGenerator.CreateCycleData)
    - [M DryGenerationEnabled ](#tts.core.project.generator.ProjectGenerator.ProjectGenerator.DryGenerationEnabled)
    - [M GenerationIterator ](#tts.core.project.generator.ProjectGenerator.ProjectGenerator.GenerationIterator)
    - [M GetDialog ](#tts.core.project.generator.ProjectGenerator.ProjectGenerator.GetDialog)
    - [M GetParameterText ](#tts.core.project.generator.ProjectGenerator.ProjectGenerator.GetParameterText)
    - [M GetTargetItemCount ](#tts.core.project.generator.ProjectGenerator.ProjectGenerator.GetTargetItemCount)
    - [M PostGeneration ](#tts.core.project.generator.ProjectGenerator.ProjectGenerator.PostGeneration)
    - [M PreGeneration ](#tts.core.project.generator.ProjectGenerator.ProjectGenerator.PreGeneration)
  - [C CycleData ](#tts.core.project.generator.ProjectGenerator.CycleData)
    - [A objectApi ](#tts.core.project.generator.ProjectGenerator.CycleData.objectApi)
    - [A projectInstance ](#tts.core.project.generator.ProjectGenerator.CycleData.projectInstance)

[ Package Generator API ](../packagegenerator-api/packagegenerator-api.md)

[ Parameter Set Generator API ](../parametersetgenerator-api/parametersetgenerator-api.md)

[ Tools ](../../tools/index.md)

[ User test management ](../../userTestmanagement/index.md)

[ UserUtility API ](../../user-utility/user-utility.md)

[ Utility Examples ](../../user-utility/example-utilities.md)

Project Generator API

- [ ProjectGenerator ](#projectgenerator)
  - [C ProjectGenerator ](#tts.core.project.generator.ProjectGenerator.ProjectGenerator)
    - [A DESCRIPTION ](#tts.core.project.generator.ProjectGenerator.ProjectGenerator.DESCRIPTION)
    - [A FORMAT_REV ](#tts.core.project.generator.ProjectGenerator.ProjectGenerator.FORMAT_REV)
    - [A ID ](#tts.core.project.generator.ProjectGenerator.ProjectGenerator.ID)
    - [A NAME ](#tts.core.project.generator.ProjectGenerator.ProjectGenerator.NAME)
    - [A SERIALIZE ](#tts.core.project.generator.ProjectGenerator.ProjectGenerator.SERIALIZE)
    - [A api ](#tts.core.project.generator.ProjectGenerator.ProjectGenerator.api)
    - [A projectPath ](#tts.core.project.generator.ProjectGenerator.ProjectGenerator.projectPath)
    - [A sourceProjectPath ](#tts.core.project.generator.ProjectGenerator.ProjectGenerator.sourceProjectPath)
    - [M GetDescription ](#tts.core.project.generator.ProjectGenerator.ProjectGenerator.GetDescription)
    - [M GetFormatRev ](#tts.core.project.generator.ProjectGenerator.ProjectGenerator.GetFormatRev)
    - [M GetId ](#tts.core.project.generator.ProjectGenerator.ProjectGenerator.GetId)
    - [M GetName ](#tts.core.project.generator.ProjectGenerator.ProjectGenerator.GetName)
    - [M Check ](#tts.core.project.generator.ProjectGenerator.ProjectGenerator.Check)
    - [M CreateCycleData ](#tts.core.project.generator.ProjectGenerator.ProjectGenerator.CreateCycleData)
    - [M DryGenerationEnabled ](#tts.core.project.generator.ProjectGenerator.ProjectGenerator.DryGenerationEnabled)
    - [M GenerationIterator ](#tts.core.project.generator.ProjectGenerator.ProjectGenerator.GenerationIterator)
    - [M GetDialog ](#tts.core.project.generator.ProjectGenerator.ProjectGenerator.GetDialog)
    - [M GetParameterText ](#tts.core.project.generator.ProjectGenerator.ProjectGenerator.GetParameterText)
    - [M GetTargetItemCount ](#tts.core.project.generator.ProjectGenerator.ProjectGenerator.GetTargetItemCount)
    - [M PostGeneration ](#tts.core.project.generator.ProjectGenerator.ProjectGenerator.PostGeneration)
    - [M PreGeneration ](#tts.core.project.generator.ProjectGenerator.ProjectGenerator.PreGeneration)
  - [C CycleData ](#tts.core.project.generator.ProjectGenerator.CycleData)
    - [A objectApi ](#tts.core.project.generator.ProjectGenerator.CycleData.objectApi)
    - [A projectInstance ](#tts.core.project.generator.ProjectGenerator.CycleData.projectInstance)

# Project Generator API[¶](#project-generator-api "Link to this heading")

An overview of commands for [Project generator](../../../en/Extensions/Project-generator.html).

## ProjectGenerator[¶](#projectgenerator "Link to this heading")

*class* ProjectGenerator[¶](#tts.core.project.generator.ProjectGenerator.ProjectGenerator "Link to this definition")  
This is the base class for user defined project generators. All project generators should be derived form this class. It defines specific methods that are called during generation of projects. The required behaviour of a project generator is implemented by overwriting these methods.

Some fields and methods *must* be overridden (**mandatory**), others *may* be overridden (**optional**). There are also methods that are only to be called by the user implementation and should not be overridden (those without a note).

DESCRIPTION = `''`[¶](#tts.core.project.generator.ProjectGenerator.ProjectGenerator.DESCRIPTION "Link to this definition")  
A short description of the project generator.

Type:  str

FORMAT_REV = `0`[¶](#tts.core.project.generator.ProjectGenerator.ProjectGenerator.FORMAT_REV "Link to this definition")  
The format revision identifies structure and type of the generator data that is saved in project files. Do not return any other value than 0 if you do not also provide for conversion of outdated versions into the current one. It is recommended keeping changes in your generation data structure compatible with former versions and always keep 0 for the format revision.

ID = `''`[¶](#tts.core.project.generator.ProjectGenerator.ProjectGenerator.ID "Link to this definition")  
A universally unique identifier to make the project generator unique. The ID should be generated automatically to be unique.

Type:  str

Info: Setting this field is **mandatory**
NAME = `''`[¶](#tts.core.project.generator.ProjectGenerator.ProjectGenerator.NAME "Link to this definition")  
The display name of the project generator.

Type:  str

Info: Setting this field is **mandatory**
SERIALIZE : dict[str, tuple[str, str] | tuple[str, str, object]] = `{}`[¶](#tts.core.project.generator.ProjectGenerator.ProjectGenerator.SERIALIZE "Link to this definition")  
Declaration of instance variables of the project generator, that are to be exported/imported to/from xml format (e.g. during saving/loading a project). The declaration contains an item for each instance variable in form of an dictionary. Example:

    SERIALIZE = {
                    "foo": ("FOO-VAR", "integer", 23),
                    "bar": ("BAR", "string"),
                    "params: ("PARAMETERS", "list")
                }

The declaration items key must match the name of the corresponding instance variable (e.g. for an instance variable self.foo the item’s key must be “foo”). The item’s value must be a tuple containing at least 2 elements. So the general syntax for a declaration item is:

    ``<variable name>: (<variable alias>, <type alias>, [default value])``

Syntax and meaning of the tuple’s elements are:

- **\<variable alias\>** declares the name of the xml element that is used for the variable’s xml representation.

- **\<type alias\>** keyword specifing the python variable’s type. The following table gives all keywords and their corresponding python type respectively:

  - `boolean`: bool

  - `integer`: int

  - `long`: int

  - `float`: float

  - `string`: str

  - `unicode`: str

  - `list`: list

  - `dict`: dict

PLEASE NOTE: Keys of dictionaries being (de-)serialized must be strings. Furthermore values of dictionaries and lists are required to be of type `bool`, `int`, `float`, `str`, `list` or `dict`. The same restrictions apply to embedded lists and dictionaries. The types `long` and `unicode` are only keept for compatibility. Do not use these in new code.

- **\<default value\>** is an optional element. It specifies the variable’s default value. If the variable’s value equals its default value during export the variable is not exported at all. Conversely, the variable is assigned its default value during import if the xml data does not provide an value for the variable.

Type:  dict

api = `None`[¶](#tts.core.project.generator.ProjectGenerator.ProjectGenerator.api "Link to this definition")  
Access to the internal ecu.test API. The API will be assigned at runtime, in order to be independent from ecu.test for testing purposes.

See also

[Internal APIs](../../general_api/api.md#internalapi)

projectPath : str | None = `None`[¶](#tts.core.project.generator.ProjectGenerator.ProjectGenerator.projectPath "Link to this definition")  
Absolute path to the project file containing the generator. In case of direct execution, this is the source project. In case of static generation it is the destination project.

sourceProjectPath : str | None = `None`[¶](#tts.core.project.generator.ProjectGenerator.ProjectGenerator.sourceProjectPath "Link to this definition")  
Absolute path to the source project file containing the generator.

*classmethod* GetDescription()[¶](#tts.core.project.generator.ProjectGenerator.ProjectGenerator.GetDescription "Link to this definition")  
Returns the description of the project generator. The description can be specified by setting the class variable [`DESCRIPTION`](#tts.core.project.generator.ProjectGenerator.ProjectGenerator.DESCRIPTION "tts.core.project.generator.ProjectGenerator.ProjectGenerator.DESCRIPTION (Python attribute) — A short description of the project generator.").

Return type:  str

*classmethod* GetFormatRev()[¶](#tts.core.project.generator.ProjectGenerator.ProjectGenerator.GetFormatRev "Link to this definition")  
Returns the format revision of the project generator. The format revision can be specified by setting the class variable [`FORMAT_REV`](#tts.core.project.generator.ProjectGenerator.ProjectGenerator.FORMAT_REV "tts.core.project.generator.ProjectGenerator.ProjectGenerator.FORMAT_REV (Python attribute) — The format revision identifies structure and type of the generator data that is saved in project files. Do not return any other value than 0 if you do not also provide for conversion of outdated versions into the current one. It is recommended keeping changes in your generation data structure compatible with former versions and always keep 0 for the format revision."). This is an optional parameter.

Return type:  int

*classmethod* GetId()[¶](#tts.core.project.generator.ProjectGenerator.ProjectGenerator.GetId "Link to this definition")  
Returns the universally unique identifier of the project generator. The identifier should be specified by setting the class variable [`ID`](#tts.core.project.generator.ProjectGenerator.ProjectGenerator.ID "tts.core.project.generator.ProjectGenerator.ProjectGenerator.ID (Python attribute) — A universally unique identifier to make the project generator unique. The ID should be generated automatically to be unique.").

Return type:  str

*classmethod* GetName()[¶](#tts.core.project.generator.ProjectGenerator.ProjectGenerator.GetName "Link to this definition")  
Returns the name of the project generator. The name should be specified by setting the class variable [`NAME`](#tts.core.project.generator.ProjectGenerator.ProjectGenerator.NAME "tts.core.project.generator.ProjectGenerator.ProjectGenerator.NAME (Python attribute) — The display name of the project generator.").

Return type:  str

Check()[¶](#tts.core.project.generator.ProjectGenerator.ProjectGenerator.Check "Link to this definition")  
Implement this method to allow checking of of the user-implemented generator.

Returns:  A list of error messages or an empty list if everything is fine.

Return type:  list\<str\>

Info

Overriding this method is **optional**

CreateCycleData(*[name](#tts.core.project.generator.ProjectGenerator.ProjectGenerator.CreateCycleData.name "tts.core.project.generator.ProjectGenerator.ProjectGenerator.CreateCycleData.name (Python parameter) — A name for this cycle that will be displayed in the report.")=`None`*, *[template](#tts.core.project.generator.ProjectGenerator.ProjectGenerator.CreateCycleData.template "tts.core.project.generator.ProjectGenerator.ProjectGenerator.CreateCycleData.template (Python parameter) — Path to template project file to be used as base for generator.")=`None`*)[¶](#tts.core.project.generator.ProjectGenerator.ProjectGenerator.CreateCycleData "Link to this definition")  
Creates an instance of class CycleData.

Parameters:  name : str[¶](#tts.core.project.generator.ProjectGenerator.ProjectGenerator.CreateCycleData.name "Permalink to this definition")  
A name for this cycle that will be displayed in the report. (optional)

template : str[¶](#tts.core.project.generator.ProjectGenerator.ProjectGenerator.CreateCycleData.template "Permalink to this definition")  
Path to template project file to be used as base for generator. (optional)

Returns:  The cycle data object

Return type:  [`CycleData`](#tts.core.project.generator.ProjectGenerator.CycleData "tts.core.project.generator.ProjectGenerator.CycleData (Python class) — A container for all data that can be generated during one cycle.")

DryGenerationEnabled()[¶](#tts.core.project.generator.ProjectGenerator.ProjectGenerator.DryGenerationEnabled "Link to this definition")  
Returns True, if the generator runs in dry generation mode. In this mode, the generator is used to generate a project with static projects.

Return type:  bool

GenerationIterator()[¶](#tts.core.project.generator.ProjectGenerator.ProjectGenerator.GenerationIterator "Link to this definition")  
Implement this method for the generation of the data for on cycle. This is an iterator and it should return an [`CycleData`](#tts.core.project.generator.ProjectGenerator.CycleData "tts.core.project.generator.ProjectGenerator.CycleData (Python class) — A container for all data that can be generated during one cycle.") object with the python keyword ‘yield’. To create an [`CycleData`](#tts.core.project.generator.ProjectGenerator.CycleData "tts.core.project.generator.ProjectGenerator.CycleData (Python class) — A container for all data that can be generated during one cycle.") object, use the method [`CreateCycleData()`](#tts.core.project.generator.ProjectGenerator.ProjectGenerator.CreateCycleData "tts.core.project.generator.ProjectGenerator.ProjectGenerator.CreateCycleData (Python method) — Creates an instance of class CycleData.") and store all information in this object. Example:

    def GenerationIterator(self):
        for line in file:
            yield CreateCycleData({'lineData': line})

Info

Overriding this method is **mandatory**

GetDialog()[¶](#tts.core.project.generator.ProjectGenerator.ProjectGenerator.GetDialog "Link to this definition")  
Implement this method to return the configuration dialog of your project generator. The dialog should set the generator data.

Return type:  wx.Dialog, None

Info

Overriding this method is **optional**

GetParameterText()[¶](#tts.core.project.generator.ProjectGenerator.ProjectGenerator.GetParameterText "Link to this definition")  
Implement this method to show the parameters of your project generator in properties column.

Returns:  parameter text

Return type:  str

Info

Overriding this method is **optional**

GetTargetItemCount()[¶](#tts.core.project.generator.ProjectGenerator.ProjectGenerator.GetTargetItemCount "Link to this definition")  
Implement this method to define the expected number of cycle sets to be generated as information for progress indicators. Will be called for updates throughout the generation. Therefore you can dynamically return the size of the current task.

Returns:  expected count of cycle sets to be generated

Return type:  int

PostGeneration()[¶](#tts.core.project.generator.ProjectGenerator.ProjectGenerator.PostGeneration "Link to this definition")  
Implement this method to specify post generation behavior. This method is called after the generation. This method will be called even if an exception occurs during generation (incl. PreGeneration), but not if the project execution is aborted (by the user or because of an “abort on error” setting).

Info

Overriding this method is **optional**

PreGeneration()[¶](#tts.core.project.generator.ProjectGenerator.ProjectGenerator.PreGeneration "Link to this definition")  
Implement this method to specify pre generation behavior. This method is called before the generation.

Info

Overriding this method is **optional**

*class* CycleData[¶](#tts.core.project.generator.ProjectGenerator.CycleData "Link to this definition")  
A container for all data that can be generated during one cycle.

objectApi = `None`[¶](#tts.core.project.generator.ProjectGenerator.CycleData.objectApi "Link to this definition")  
The Object API which is used to create test steps.

Type:  [`ApiClient.ApiClient`](../../general_api/objectApi.md#ApiClient.ApiClient "ApiClient.ApiClient (Python class) — Entry point for object based api.")

projectInstance = `None`[¶](#tts.core.project.generator.ProjectGenerator.CycleData.projectInstance "Link to this definition")  
The project instance to be completed and executed. Based on a provided template or empty.

Type:  [`ApiClient.Project`](../../general_api/ProjectApi/Project.md#ApiClient.Project "ApiClient.Project (Python class) — ProjectApi.CreateProject")

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
