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

[ Project Generator API ](../projectgenerator-api/projectgenerator-api.md)

Package Generator API [ Package Generator API ](#)

Package Generator API

- [ PackageGenerator ](#packagegenerator)
  - [C PackageGenerator ](#tts.core.project.generator.PackageGenerator.PackageGenerator)
    - [A DESCRIPTION ](#tts.core.project.generator.PackageGenerator.PackageGenerator.DESCRIPTION)
    - [A FORMAT_REV ](#tts.core.project.generator.PackageGenerator.PackageGenerator.FORMAT_REV)
    - [A ID ](#tts.core.project.generator.PackageGenerator.PackageGenerator.ID)
    - [A NAME ](#tts.core.project.generator.PackageGenerator.PackageGenerator.NAME)
    - [A SERIALIZE ](#tts.core.project.generator.PackageGenerator.PackageGenerator.SERIALIZE)
    - [A api ](#tts.core.project.generator.PackageGenerator.PackageGenerator.api)
    - [A projectPath ](#tts.core.project.generator.PackageGenerator.PackageGenerator.projectPath)
    - [M GetDescription ](#tts.core.project.generator.PackageGenerator.PackageGenerator.GetDescription)
    - [M GetFormatRev ](#tts.core.project.generator.PackageGenerator.PackageGenerator.GetFormatRev)
    - [M GetId ](#tts.core.project.generator.PackageGenerator.PackageGenerator.GetId)
    - [M GetName ](#tts.core.project.generator.PackageGenerator.PackageGenerator.GetName)
    - [M Check ](#tts.core.project.generator.PackageGenerator.PackageGenerator.Check)
    - [M CreateCycleData ](#tts.core.project.generator.PackageGenerator.PackageGenerator.CreateCycleData)
    - [M DryGenerationEnabled ](#tts.core.project.generator.PackageGenerator.PackageGenerator.DryGenerationEnabled)
    - [M GenerationIterator ](#tts.core.project.generator.PackageGenerator.PackageGenerator.GenerationIterator)
    - [M GetDialog ](#tts.core.project.generator.PackageGenerator.PackageGenerator.GetDialog)
    - [M GetParameterText ](#tts.core.project.generator.PackageGenerator.PackageGenerator.GetParameterText)
    - [M GetTargetItemCount ](#tts.core.project.generator.PackageGenerator.PackageGenerator.GetTargetItemCount)
    - [M PostGeneration ](#tts.core.project.generator.PackageGenerator.PackageGenerator.PostGeneration)
    - [M PreGeneration ](#tts.core.project.generator.PackageGenerator.PackageGenerator.PreGeneration)
  - [C CycleData ](#tts.core.project.generator.PackageGenerator.CycleData)
    - [A objectApi ](#tts.core.project.generator.PackageGenerator.CycleData.objectApi)
    - [A packageInstance ](#tts.core.project.generator.PackageGenerator.CycleData.packageInstance)
    - [M AppendParameterSet ](#tts.core.project.generator.PackageGenerator.CycleData.AppendParameterSet)
    - [M GetParameterSets ](#tts.core.project.generator.PackageGenerator.CycleData.GetParameterSets)
- [ ReferenceTestPackageGenerator ](#referencetestpackagegenerator)
  - [C ReferenceTestPackageGeneratorTools ](#tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.ReferenceTestPackageGeneratorTools)
    - [M AppendTraceAnalysisReference ](#tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.ReferenceTestPackageGeneratorTools.AppendTraceAnalysisReference)
    - [M ApplyPattern ](#tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.ReferenceTestPackageGeneratorTools.ApplyPattern)
    - [M EnablePlot ](#tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.ReferenceTestPackageGeneratorTools.EnablePlot)
    - [M Filter ](#tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.ReferenceTestPackageGeneratorTools.Filter)
    - [M GetOrCreateEpisode ](#tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.ReferenceTestPackageGeneratorTools.GetOrCreateEpisode)
    - [M GetSynchronizationConfiguration ](#tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.ReferenceTestPackageGeneratorTools.GetSynchronizationConfiguration)
  - [C Signal ](#tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.Signal)
    - [A device ](#tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.Signal.device)
    - [A name ](#tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.Signal.name)
    - [A type ](#tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.Signal.type)
    - [M GetSignalGroupName ](#tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.Signal.GetSignalGroupName)

[ Parameter Set Generator API ](../parametersetgenerator-api/parametersetgenerator-api.md)

[ Tools ](../../tools/index.md)

[ User test management ](../../userTestmanagement/index.md)

[ UserUtility API ](../../user-utility/user-utility.md)

[ Utility Examples ](../../user-utility/example-utilities.md)

Package Generator API

- [ PackageGenerator ](#packagegenerator)
  - [C PackageGenerator ](#tts.core.project.generator.PackageGenerator.PackageGenerator)
    - [A DESCRIPTION ](#tts.core.project.generator.PackageGenerator.PackageGenerator.DESCRIPTION)
    - [A FORMAT_REV ](#tts.core.project.generator.PackageGenerator.PackageGenerator.FORMAT_REV)
    - [A ID ](#tts.core.project.generator.PackageGenerator.PackageGenerator.ID)
    - [A NAME ](#tts.core.project.generator.PackageGenerator.PackageGenerator.NAME)
    - [A SERIALIZE ](#tts.core.project.generator.PackageGenerator.PackageGenerator.SERIALIZE)
    - [A api ](#tts.core.project.generator.PackageGenerator.PackageGenerator.api)
    - [A projectPath ](#tts.core.project.generator.PackageGenerator.PackageGenerator.projectPath)
    - [M GetDescription ](#tts.core.project.generator.PackageGenerator.PackageGenerator.GetDescription)
    - [M GetFormatRev ](#tts.core.project.generator.PackageGenerator.PackageGenerator.GetFormatRev)
    - [M GetId ](#tts.core.project.generator.PackageGenerator.PackageGenerator.GetId)
    - [M GetName ](#tts.core.project.generator.PackageGenerator.PackageGenerator.GetName)
    - [M Check ](#tts.core.project.generator.PackageGenerator.PackageGenerator.Check)
    - [M CreateCycleData ](#tts.core.project.generator.PackageGenerator.PackageGenerator.CreateCycleData)
    - [M DryGenerationEnabled ](#tts.core.project.generator.PackageGenerator.PackageGenerator.DryGenerationEnabled)
    - [M GenerationIterator ](#tts.core.project.generator.PackageGenerator.PackageGenerator.GenerationIterator)
    - [M GetDialog ](#tts.core.project.generator.PackageGenerator.PackageGenerator.GetDialog)
    - [M GetParameterText ](#tts.core.project.generator.PackageGenerator.PackageGenerator.GetParameterText)
    - [M GetTargetItemCount ](#tts.core.project.generator.PackageGenerator.PackageGenerator.GetTargetItemCount)
    - [M PostGeneration ](#tts.core.project.generator.PackageGenerator.PackageGenerator.PostGeneration)
    - [M PreGeneration ](#tts.core.project.generator.PackageGenerator.PackageGenerator.PreGeneration)
  - [C CycleData ](#tts.core.project.generator.PackageGenerator.CycleData)
    - [A objectApi ](#tts.core.project.generator.PackageGenerator.CycleData.objectApi)
    - [A packageInstance ](#tts.core.project.generator.PackageGenerator.CycleData.packageInstance)
    - [M AppendParameterSet ](#tts.core.project.generator.PackageGenerator.CycleData.AppendParameterSet)
    - [M GetParameterSets ](#tts.core.project.generator.PackageGenerator.CycleData.GetParameterSets)
- [ ReferenceTestPackageGenerator ](#referencetestpackagegenerator)
  - [C ReferenceTestPackageGeneratorTools ](#tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.ReferenceTestPackageGeneratorTools)
    - [M AppendTraceAnalysisReference ](#tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.ReferenceTestPackageGeneratorTools.AppendTraceAnalysisReference)
    - [M ApplyPattern ](#tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.ReferenceTestPackageGeneratorTools.ApplyPattern)
    - [M EnablePlot ](#tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.ReferenceTestPackageGeneratorTools.EnablePlot)
    - [M Filter ](#tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.ReferenceTestPackageGeneratorTools.Filter)
    - [M GetOrCreateEpisode ](#tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.ReferenceTestPackageGeneratorTools.GetOrCreateEpisode)
    - [M GetSynchronizationConfiguration ](#tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.ReferenceTestPackageGeneratorTools.GetSynchronizationConfiguration)
  - [C Signal ](#tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.Signal)
    - [A device ](#tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.Signal.device)
    - [A name ](#tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.Signal.name)
    - [A type ](#tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.Signal.type)
    - [M GetSignalGroupName ](#tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.Signal.GetSignalGroupName)

# Package Generator API[¶](#package-generator-api "Link to this heading")

An overview of commands for [Package generator](../../../en/Extensions/Package-generator.html).

## PackageGenerator[¶](#packagegenerator "Link to this heading")

*class* PackageGenerator[¶](#tts.core.project.generator.PackageGenerator.PackageGenerator "Link to this definition")  
This is the base class for user defined package generators. All package generators should be derived form this class. It defines specific methods that are called during generation of packages. The required behaviour of a package generator is implemented by overwriting these methods.

Some fields and methods *must* be overridden (**mandatory**), others *may* be overridden (**optional**). There are also methods that are only to be called by the user implementation and should not be overridden (those without a note).

DESCRIPTION = `''`[¶](#tts.core.project.generator.PackageGenerator.PackageGenerator.DESCRIPTION "Link to this definition")  
A short description of the package generator.

Type:  str

FORMAT_REV = `0`[¶](#tts.core.project.generator.PackageGenerator.PackageGenerator.FORMAT_REV "Link to this definition")  
The format revision identifies structure and type of the generator data that is saved in project files. Do not return any other value than 0 if you do not also provide for conversion of outdated versions into the current one. It is recommended keeping changes in your generation data structure compatible with former versions and always keep 0 for the format revision.

ID = `''`[¶](#tts.core.project.generator.PackageGenerator.PackageGenerator.ID "Link to this definition")  
A universally unique identifier to make the package generator unique. The ID should be generated automatically to be unique.

Type:  str

Info: Setting this field is **mandatory**
NAME = `''`[¶](#tts.core.project.generator.PackageGenerator.PackageGenerator.NAME "Link to this definition")  
The display name of the package generator.

Type:  str

Info: Setting this field is **mandatory**
SERIALIZE : dict[str, tuple[str, str] | tuple[str, str, object]] = `{}`[¶](#tts.core.project.generator.PackageGenerator.PackageGenerator.SERIALIZE "Link to this definition")  
Declaration of instance variables of the package generator, that are to be exported/imported to/from xml format (e.g. during saving/loading a project). The declaration contains an item for each instance variable in form of an dictionary. Example:

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

PLEASE NOTE: Keys of dictionaries being (de-)serialized must be strings. Furthermore values of dictionaries and lists are required to be of type `bool`, `int`, `float`, `str`, `list` or `dict`. The same restrictions apply to embedded lists and dictionaries. The types `long` and `unicode` are only kept for compatibility. Do not use these in new code.

- **\<default value\>** is an optional element. It specifies the variable’s default value. If the variable’s value equals its default value during export the variable is not exported at all. Conversely, the variable is assigned its default value during import if the xml data does not provide an value for the variable.

Type:  dict

api = `None`[¶](#tts.core.project.generator.PackageGenerator.PackageGenerator.api "Link to this definition")  
Access to the internal ecu.test API. The API will be assigned at runtime, in order to be independent from ecu.test for testing purposes.

See also

[Internal APIs](../../general_api/api.md#internalapi)

projectPath = `None`[¶](#tts.core.project.generator.PackageGenerator.PackageGenerator.projectPath "Link to this definition")  
Absolute path to the project file containing the generator. In case of direct execution, this is the source project. In case of static generation it is the destination project.

*classmethod* GetDescription()[¶](#tts.core.project.generator.PackageGenerator.PackageGenerator.GetDescription "Link to this definition")  
Returns the description of the package generator. The description can be specified by setting the class variable [`DESCRIPTION`](#tts.core.project.generator.PackageGenerator.PackageGenerator.DESCRIPTION "tts.core.project.generator.PackageGenerator.PackageGenerator.DESCRIPTION (Python attribute) — A short description of the package generator.").

Return type:  str

*classmethod* GetFormatRev()[¶](#tts.core.project.generator.PackageGenerator.PackageGenerator.GetFormatRev "Link to this definition")  
Returns the format revision of the package generator. The format revision can be specified by setting the class variable [`FORMAT_REV`](#tts.core.project.generator.PackageGenerator.PackageGenerator.FORMAT_REV "tts.core.project.generator.PackageGenerator.PackageGenerator.FORMAT_REV (Python attribute) — The format revision identifies structure and type of the generator data that is saved in project files. Do not return any other value than 0 if you do not also provide for conversion of outdated versions into the current one. It is recommended keeping changes in your generation data structure compatible with former versions and always keep 0 for the format revision."). This is an optional parameter.

Return type:  int

*classmethod* GetId()[¶](#tts.core.project.generator.PackageGenerator.PackageGenerator.GetId "Link to this definition")  
Returns the universally unique identifier of the package generator. The identifier should be specified by setting the class variable [`ID`](#tts.core.project.generator.PackageGenerator.PackageGenerator.ID "tts.core.project.generator.PackageGenerator.PackageGenerator.ID (Python attribute) — A universally unique identifier to make the package generator unique. The ID should be generated automatically to be unique.").

Return type:  str

*classmethod* GetName()[¶](#tts.core.project.generator.PackageGenerator.PackageGenerator.GetName "Link to this definition")  
Returns the name of the package generator. The name should be specified by setting the class variable [`NAME`](#tts.core.project.generator.PackageGenerator.PackageGenerator.NAME "tts.core.project.generator.PackageGenerator.PackageGenerator.NAME (Python attribute) — The display name of the package generator.").

Return type:  str

Check()[¶](#tts.core.project.generator.PackageGenerator.PackageGenerator.Check "Link to this definition")  
Implement this method to allow checking of of the user-implemented generator.

Returns:  A list of error messages or an empty list if everything is fine.

Return type:  list\<str\>

Info

Overriding this method is **optional**

CreateCycleData(*[name](#tts.core.project.generator.PackageGenerator.PackageGenerator.CreateCycleData.name "tts.core.project.generator.PackageGenerator.PackageGenerator.CreateCycleData.name (Python parameter) — A name for this cycle that will be displayed in the report.")=`None`*, *[template](#tts.core.project.generator.PackageGenerator.PackageGenerator.CreateCycleData.template "tts.core.project.generator.PackageGenerator.PackageGenerator.CreateCycleData.template (Python parameter) — Path to template package file to be used as base for generator.")=`None`*)[¶](#tts.core.project.generator.PackageGenerator.PackageGenerator.CreateCycleData "Link to this definition")  
Creates an instance of class CycleData.

Parameters:  name : str[¶](#tts.core.project.generator.PackageGenerator.PackageGenerator.CreateCycleData.name "Permalink to this definition")  
A name for this cycle that will be displayed in the report. (optional)

template : str[¶](#tts.core.project.generator.PackageGenerator.PackageGenerator.CreateCycleData.template "Permalink to this definition")  
Path to template package file to be used as base for generator. (optional)

Returns:  The cycle data object

Return type:  [`CycleData`](#tts.core.project.generator.PackageGenerator.CycleData "tts.core.project.generator.PackageGenerator.CycleData (Python class) — A container for all data that can be generated during one cycle.")

DryGenerationEnabled()[¶](#tts.core.project.generator.PackageGenerator.PackageGenerator.DryGenerationEnabled "Link to this definition")  
Returns True, if the generator runs in dry generation mode. In this mode, the generator is used to generate a project with static packages.

Return type:  bool

GenerationIterator()[¶](#tts.core.project.generator.PackageGenerator.PackageGenerator.GenerationIterator "Link to this definition")  
Implement this method for the generation of the data for on cycle. This is an iterator and it should return an [`CycleData`](#tts.core.project.generator.PackageGenerator.CycleData "tts.core.project.generator.PackageGenerator.CycleData (Python class) — A container for all data that can be generated during one cycle.") object with the python keyword ‘yield’. To create an [`CycleData`](#tts.core.project.generator.PackageGenerator.CycleData "tts.core.project.generator.PackageGenerator.CycleData (Python class) — A container for all data that can be generated during one cycle.") object, use the method [`CreateCycleData()`](#tts.core.project.generator.PackageGenerator.PackageGenerator.CreateCycleData "tts.core.project.generator.PackageGenerator.PackageGenerator.CreateCycleData (Python method) — Creates an instance of class CycleData.") and store all information in this object. Example:

    def GenerationIterator(self):
        for line in file:
            yield CreateCycleData({'lineData': line})

Info

Overriding this method is **mandatory**

GetDialog()[¶](#tts.core.project.generator.PackageGenerator.PackageGenerator.GetDialog "Link to this definition")  
Implement this method to return the configuration dialog of your package generator. The dialog should set the generator data.

Return type:  wx.Dialog, None

Info

Overriding this method is **optional**

GetParameterText()[¶](#tts.core.project.generator.PackageGenerator.PackageGenerator.GetParameterText "Link to this definition")  
Implement this method to show the parameters of your package generator in properties column.

Returns:  parameter text

Return type:  str

Info

Overriding this method is **optional**

GetTargetItemCount()[¶](#tts.core.project.generator.PackageGenerator.PackageGenerator.GetTargetItemCount "Link to this definition")  
Implement this method to define the expected number of cycle sets to be generated as information for progress indicators. Will be called for updates throughout the generation. Therefore, you can dynamically return the size of the current task.

Returns:  expected count of cycle sets to be generated

Return type:  int

PostGeneration()[¶](#tts.core.project.generator.PackageGenerator.PackageGenerator.PostGeneration "Link to this definition")  
Implement this method to specify post generation behavior. This method is called after the generation. This method will be called even if an exception occurs during generation (incl. PreGeneration), but not if the project execution is aborted (by the user or because of an “abort on error” setting).

Info

Overriding this method is **optional**

PreGeneration()[¶](#tts.core.project.generator.PackageGenerator.PackageGenerator.PreGeneration "Link to this definition")  
Implement this method to specify pre generation behavior. This method is called before the generation.

Info

Overriding this method is **optional**

*class* CycleData[¶](#tts.core.project.generator.PackageGenerator.CycleData "Link to this definition")  
A container for all data that can be generated during one cycle.

objectApi = `None`[¶](#tts.core.project.generator.PackageGenerator.CycleData.objectApi "Link to this definition")  
The Object API which is used to create test steps.

Type:  [`ApiClient.ApiClient`](../../general_api/objectApi.md#ApiClient.ApiClient "ApiClient.ApiClient (Python class) — Entry point for object based api.")

packageInstance = `None`[¶](#tts.core.project.generator.PackageGenerator.CycleData.packageInstance "Link to this definition")  
The package instance to be completed and executed. Based on a provided template or empty.

Type:  [`ApiClient.Package`](../../general_api/PackageApi/Package.md#ApiClient.Package "ApiClient.Package (Python class) — PackageApi.CreatePackage")

AppendParameterSet(*[name](#tts.core.project.generator.PackageGenerator.CycleData.AppendParameterSet.name "tts.core.project.generator.PackageGenerator.CycleData.AppendParameterSet.name (Python parameter) — Name of the parameter set that will be displayed in the report.")*)[¶](#tts.core.project.generator.PackageGenerator.CycleData.AppendParameterSet "Link to this definition")  
Appends a parameter set for this cycle.

Parameters:  name : str[¶](#tts.core.project.generator.PackageGenerator.CycleData.AppendParameterSet.name "Permalink to this definition")  
Name of the parameter set that will be displayed in the report.

Returns:  Parameter set

Return type:  [`ApiClient.ParameterSet`](../../general_api/ComponentApi/ParameterSet.md#ApiClient.ParameterSet "ApiClient.ParameterSet (Python class) — Returns access to the package attributes definitions specified within the parameter set and the referenced package attribute definition files.")

GetParameterSets()[¶](#tts.core.project.generator.PackageGenerator.CycleData.GetParameterSets "Link to this definition")  
Returns a list of all parameter sets assigned to this cycle.

Returns:  List of parameter sets for this cycle.

Return type:  list\<[`ApiClient.ParameterSet`](../../general_api/ComponentApi/ParameterSet.md#ApiClient.ParameterSet "ApiClient.ParameterSet (Python class) — Returns access to the package attributes definitions specified within the parameter set and the referenced package attribute definition files.")\>

## ReferenceTestPackageGenerator[¶](#referencetestpackagegenerator "Link to this heading")

*class* ReferenceTestPackageGeneratorTools[¶](#tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.ReferenceTestPackageGeneratorTools "Link to this definition")  
This class provides convenience methods that can be used within the user code section of the Reference Test Package Generator.

An instance of this class is globally available as variable ‘tools’

*static* AppendTraceAnalysisReference(*[traceAnalysis](#tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.ReferenceTestPackageGeneratorTools.AppendTraceAnalysisReference.traceAnalysis "tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.ReferenceTestPackageGeneratorTools.AppendTraceAnalysisReference.traceAnalysis (Python parameter) — the current reference test trace analysis object")*, *[analysisReference](#tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.ReferenceTestPackageGeneratorTools.AppendTraceAnalysisReference.analysisReference "tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.ReferenceTestPackageGeneratorTools.AppendTraceAnalysisReference.analysisReference (Python parameter) — name of the episode")*, *[refName](#tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.ReferenceTestPackageGeneratorTools.AppendTraceAnalysisReference.refName "tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.ReferenceTestPackageGeneratorTools.AppendTraceAnalysisReference.refName (Python parameter) — name of the reference signal")*, *[testName](#tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.ReferenceTestPackageGeneratorTools.AppendTraceAnalysisReference.testName "tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.ReferenceTestPackageGeneratorTools.AppendTraceAnalysisReference.testName (Python parameter) — name of the test signal")*)[¶](#tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.ReferenceTestPackageGeneratorTools.AppendTraceAnalysisReference "Link to this definition")  
Adds analysis reference trace step to the current trace analysis. The created [`ApiClient.TraceAnalysisReference`](../../general_api/TraceAnalysisApi/TraceAnalysisReference.md#ApiClient.TraceAnalysisReference "ApiClient.TraceAnalysisReference (Python class) — Most methods of the TraceAnalysisReference can only be used if it is assigned to a package."). object is returned.

Parameters:  traceAnalysis[¶](#tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.ReferenceTestPackageGeneratorTools.AppendTraceAnalysisReference.traceAnalysis "Permalink to this definition")  
the current reference test trace analysis object

analysisReference : string[¶](#tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.ReferenceTestPackageGeneratorTools.AppendTraceAnalysisReference.analysisReference "Permalink to this definition")  
name of the episode

refName : string[¶](#tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.ReferenceTestPackageGeneratorTools.AppendTraceAnalysisReference.refName "Permalink to this definition")  
name of the reference signal

testName : string[¶](#tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.ReferenceTestPackageGeneratorTools.AppendTraceAnalysisReference.testName "Permalink to this definition")  
name of the test signal

Returns:  object of the analysis reference trace step

Return type:  [`ApiClient.TraceAnalysisReference`](../../general_api/TraceAnalysisApi/TraceAnalysisReference.md#ApiClient.TraceAnalysisReference "ApiClient.TraceAnalysisReference (Python class) — Most methods of the TraceAnalysisReference can only be used if it is assigned to a package.")

*static* ApplyPattern(*[string](#tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.ReferenceTestPackageGeneratorTools.ApplyPattern.string "tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.ReferenceTestPackageGeneratorTools.ApplyPattern.string (Python parameter) — String that is to be reduced")*, *[pattern](#tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.ReferenceTestPackageGeneratorTools.ApplyPattern.pattern "tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.ReferenceTestPackageGeneratorTools.ApplyPattern.pattern (Python parameter) — Pattern that is to be applied to the string")*, *[debug](#tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.ReferenceTestPackageGeneratorTools.ApplyPattern.debug "tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.ReferenceTestPackageGeneratorTools.ApplyPattern.debug (Python parameter) — Set to True to create debug prints")=`False`*)[¶](#tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.ReferenceTestPackageGeneratorTools.ApplyPattern "Link to this definition")  
Reduces a string according to a wildcard pattern.

Pattern syntax:  
`( )`… denotes part of the string that is of interest

`*` … substitute for any string

`?` … substitute for any character

If the pattern does not match the string, the full string is returned as is.

Example:  
`string = 'Signal_XY', pattern = 'Signal_(*)', result: 'XY'`Parameters:  
string : str[¶](#tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.ReferenceTestPackageGeneratorTools.ApplyPattern.string "Permalink to this definition")  
String that is to be reduced

pattern : str[¶](#tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.ReferenceTestPackageGeneratorTools.ApplyPattern.pattern "Permalink to this definition")  
Pattern that is to be applied to the string

debug=`False`[¶](#tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.ReferenceTestPackageGeneratorTools.ApplyPattern.debug "Permalink to this definition")  
Set to True to create debug prints

Returns:  Reduced substring or full string, if pattern does not match

*static* EnablePlot(*[traceStep](#tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.ReferenceTestPackageGeneratorTools.EnablePlot.traceStep "tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.ReferenceTestPackageGeneratorTools.EnablePlot.traceStep (Python parameter) — the traceStep for which the plot will be enabled")*, *[plotName](#tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.ReferenceTestPackageGeneratorTools.EnablePlot.plotName "tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.ReferenceTestPackageGeneratorTools.EnablePlot.plotName (Python parameter) — name of the plot, defaults to 'Signal plot'")=`''`*, *[condition](#tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.ReferenceTestPackageGeneratorTools.EnablePlot.condition "tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.ReferenceTestPackageGeneratorTools.EnablePlot.condition (Python parameter) — Condition that must be matched to create a plot. Possible parameter values are 'ALWAYS', 'SUCCESS', 'INCONCLUSIVE', 'FAILED' or 'NEVER'.")=`'SUCCESS'`*)[¶](#tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.ReferenceTestPackageGeneratorTools.EnablePlot "Link to this definition")  
Adds a plot to the given traceStep with all signals used by the traceStep.

Parameters:  traceStep[¶](#tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.ReferenceTestPackageGeneratorTools.EnablePlot.traceStep "Permalink to this definition")  
the traceStep for which the plot will be enabled

plotName : string, optional[¶](#tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.ReferenceTestPackageGeneratorTools.EnablePlot.plotName "Permalink to this definition")  
name of the plot, defaults to ‘Signal plot’

condition=`'SUCCESS'`[¶](#tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.ReferenceTestPackageGeneratorTools.EnablePlot.condition "Permalink to this definition")  
Condition that must be matched to create a plot. Possible parameter values are ‘ALWAYS’, ‘SUCCESS’, ‘INCONCLUSIVE’, ‘FAILED’ or ‘NEVER’. Defaults to ‘SUCCESS’.

*static* Filter(*[signalList](#tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.ReferenceTestPackageGeneratorTools.Filter.signalList "tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.ReferenceTestPackageGeneratorTools.Filter.signalList (Python parameter) — List with Signal objects that is to be reduced")*, *[includeFilter](#tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.ReferenceTestPackageGeneratorTools.Filter.includeFilter "tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.ReferenceTestPackageGeneratorTools.Filter.includeFilter (Python parameter) — Filter to include certain signals.")*, *[excludeFilter](#tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.ReferenceTestPackageGeneratorTools.Filter.excludeFilter "tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.ReferenceTestPackageGeneratorTools.Filter.excludeFilter (Python parameter) — Filter to exclude certain signals.")=`''`*)[¶](#tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.ReferenceTestPackageGeneratorTools.Filter "Link to this definition")  
Removes signals from a list according to certain criteria.

The filter syntax corresponds to the Filter syntax as described in the ecu.test User Documentation under “Handling \> Filter”.

Parameters:  signalList[¶](#tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.ReferenceTestPackageGeneratorTools.Filter.signalList "Permalink to this definition")  
List with [`Signal`](#tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.Signal "tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.Signal (Python class) — Represents a single signal inside a trace file. Signals can be easily compared with other Signal objects. Signals can also be used as a set for bulk operations.") objects that is to be reduced

includeFilter : str[¶](#tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.ReferenceTestPackageGeneratorTools.Filter.includeFilter "Permalink to this definition")  
Filter to include certain signals. An empty filter includes everything.

E.g.: `"name = '*_important'"`(this can also be abbreviated to `"'*_important'"`)

excludeFilter : str[¶](#tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.ReferenceTestPackageGeneratorTools.Filter.excludeFilter "Permalink to this definition")  
Filter to exclude certain signals. An empty filter excludes nothing.

E.g.: `"device != 'Primary'"`Returns:  
List of filtered [`Signal`](#tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.Signal "tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.Signal (Python class) — Represents a single signal inside a trace file. Signals can be easily compared with other Signal objects. Signals can also be used as a set for bulk operations.") objects

*static* GetOrCreateEpisode(*[traceAnalysis](#tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.ReferenceTestPackageGeneratorTools.GetOrCreateEpisode.traceAnalysis "tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.ReferenceTestPackageGeneratorTools.GetOrCreateEpisode.traceAnalysis (Python parameter) — the current reference test trace analysis object")*, *[episodeName](#tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.ReferenceTestPackageGeneratorTools.GetOrCreateEpisode.episodeName "tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.ReferenceTestPackageGeneratorTools.GetOrCreateEpisode.episodeName (Python parameter) — name of the episode")=`None`*)[¶](#tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.ReferenceTestPackageGeneratorTools.GetOrCreateEpisode "Link to this definition")  
The episode with the specified name is returned. If no name is specified, the first episode is returned. If no episode (with the specified name) yet exists, a new episode will be created and appended to the traceAnalysis. The newly created [`ApiClient.Episode`](../../general_api/TraceAnalysisApi/Episode.md#ApiClient.Episode "ApiClient.Episode (Python class) — TraceAnalysisApi.CreateEpisode") object is returned.

Parameters:  traceAnalysis[¶](#tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.ReferenceTestPackageGeneratorTools.GetOrCreateEpisode.traceAnalysis "Permalink to this definition")  
the current reference test trace analysis object

episodeName : string, optional[¶](#tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.ReferenceTestPackageGeneratorTools.GetOrCreateEpisode.episodeName "Permalink to this definition")  
name of the episode

Returns:  object of the episode

Return type:  [`ApiClient.Episode`](../../general_api/TraceAnalysisApi/Episode.md#ApiClient.Episode "ApiClient.Episode (Python class) — TraceAnalysisApi.CreateEpisode")

GetSynchronizationConfiguration(*[packageObject](#tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.ReferenceTestPackageGeneratorTools.GetSynchronizationConfiguration.packageObject "tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.ReferenceTestPackageGeneratorTools.GetSynchronizationConfiguration.packageObject (Python parameter) — object of the generated reference test package (ApiClient.Package)")*, *[signals](#tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.ReferenceTestPackageGeneratorTools.GetSynchronizationConfiguration.signals "tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.ReferenceTestPackageGeneratorTools.GetSynchronizationConfiguration.signals (Python parameter) — list of tuples of refSignal and testSignal. One of those can be 'None' if no matching signal was found.")*)[¶](#tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.ReferenceTestPackageGeneratorTools.GetSynchronizationConfiguration "Link to this definition")  
Returns the synchronization configuration and recording groups for the specified package based on the provided signals. The returned objects can be used to synchronize reference and test traces before comparison.

Parameters:  packageObject[¶](#tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.ReferenceTestPackageGeneratorTools.GetSynchronizationConfiguration.packageObject "Permalink to this definition")  
object of the generated reference test package ([`ApiClient.Package`](../../general_api/PackageApi/Package.md#ApiClient.Package "ApiClient.Package (Python class) — PackageApi.CreatePackage"))

signals : list[tuple[[Signal](#tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.Signal "tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.Signal (Python class) — Represents a single signal inside a trace file. Signals can be easily compared with other Signal objects. Signals can also be used as a set for bulk operations."), [Signal](#tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.Signal "tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.Signal (Python class) — Represents a single signal inside a trace file. Signals can be easily compared with other Signal objects. Signals can also be used as a set for bulk operations.")]][¶](#tts.extension.referenceTestPackageGenerator.standard.ReferenceTestPackageGeneratorTools.ReferenceTestPackageGeneratorTools.GetSynchronizationConfiguration.signals "Permalink to this definition")  
list of tuples of refSignal and testSignal. One of those can be ‘None’ if no matching signal was found.

Returns:  tuple of synchronization configuration, reference recording group and test recording group

Return type:  tuple of [`ApiClient.SyncConfig`](../../general_api/TraceAnalysisApi/SyncConfig.md#ApiClient.SyncConfig "ApiClient.SyncConfig (Python class) — Assigns an AUTOSAR Time Synchronization that synchronizes recordingGroup with masterGroup. If there is already a synchronization assigned to recordingGroup it will be unassigned."), referenceRecordingGroup\<[`ApiClient.RecordingGroup`](../../general_api/SignalRecordingApi/RecordingGroup.md#ApiClient.RecordingGroup "ApiClient.RecordingGroup (Python class) — SignalRecordingApi.CreateRecordingGroup")\> and testRecordingGroup\<[`ApiClient.RecordingGroup`](../../general_api/SignalRecordingApi/RecordingGroup.md#ApiClient.RecordingGroup "ApiClient.RecordingGroup (Python class) — SignalRecordingApi.CreateRecordingGroup")\>

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

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
