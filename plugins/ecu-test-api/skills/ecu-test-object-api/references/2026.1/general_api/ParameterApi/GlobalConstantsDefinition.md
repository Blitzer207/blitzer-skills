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

API for Parameters

GlobalConstantsDefinition [ GlobalConstantsDefinition ](#)

GlobalConstantsDefinition

- [C GlobalConstantsDefinition ](#ApiClient.GlobalConstantsDefinition)
  - [M AppendConstant ](#ApiClient.GlobalConstantsDefinition.AppendConstant)
  - [M Clone ](#ApiClient.GlobalConstantsDefinition.Clone)
  - [M GetAllConstantNames ](#ApiClient.GlobalConstantsDefinition.GetAllConstantNames)
  - [M GetDescription ](#ApiClient.GlobalConstantsDefinition.GetDescription)
  - [M GetFilename ](#ApiClient.GlobalConstantsDefinition.GetFilename)
  - [M GetValue ](#ApiClient.GlobalConstantsDefinition.GetValue)
  - [M RemoveConstant ](#ApiClient.GlobalConstantsDefinition.RemoveConstant)
  - [M Save ](#ApiClient.GlobalConstantsDefinition.Save)
  - [M SetDescription ](#ApiClient.GlobalConstantsDefinition.SetDescription)
  - [M SetValue ](#ApiClient.GlobalConstantsDefinition.SetValue)

[ PackageParametersDefinition ](PackageParametersDefinition.md)

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

GlobalConstantsDefinition

- [C GlobalConstantsDefinition ](#ApiClient.GlobalConstantsDefinition)
  - [M AppendConstant ](#ApiClient.GlobalConstantsDefinition.AppendConstant)
  - [M Clone ](#ApiClient.GlobalConstantsDefinition.Clone)
  - [M GetAllConstantNames ](#ApiClient.GlobalConstantsDefinition.GetAllConstantNames)
  - [M GetDescription ](#ApiClient.GlobalConstantsDefinition.GetDescription)
  - [M GetFilename ](#ApiClient.GlobalConstantsDefinition.GetFilename)
  - [M GetValue ](#ApiClient.GlobalConstantsDefinition.GetValue)
  - [M RemoveConstant ](#ApiClient.GlobalConstantsDefinition.RemoveConstant)
  - [M Save ](#ApiClient.GlobalConstantsDefinition.Save)
  - [M SetDescription ](#ApiClient.GlobalConstantsDefinition.SetDescription)
  - [M SetValue ](#ApiClient.GlobalConstantsDefinition.SetValue)

# GlobalConstantsDefinition[¶](#globalconstantsdefinition "Link to this heading")

*class* GlobalConstantsDefinition[¶](#ApiClient.GlobalConstantsDefinition "Link to this definition")  
Returned by

- [`ParameterApi.CreateGlobalConstantsDefinition`](../ParameterApi.md#ApiClient.ParameterApi.CreateGlobalConstantsDefinition "ApiClient.ParameterApi.CreateGlobalConstantsDefinition (Python method) — Creates a new global constants definition.")

- [`ParameterApi.OpenGlobalConstantsDefinition`](../ParameterApi.md#ApiClient.ParameterApi.OpenGlobalConstantsDefinition "ApiClient.ParameterApi.OpenGlobalConstantsDefinition (Python method) — Opens an existing global constants definition file (*.gcd).")

- [`ParameterApi.SearchGlobalConstantsDefinitions`](../ParameterApi.md#ApiClient.ParameterApi.SearchGlobalConstantsDefinitions "ApiClient.ParameterApi.SearchGlobalConstantsDefinitions (Python method) — Searches the current workspace and library workspaces for Global Constant Definitions matching the given search criteria.")

AppendConstant(*[name](#ApiClient.GlobalConstantsDefinition.AppendConstant.name "ApiClient.GlobalConstantsDefinition.AppendConstant.name (Python parameter) — Name of the constant")*, *[value](#ApiClient.GlobalConstantsDefinition.AppendConstant.value "ApiClient.GlobalConstantsDefinition.AppendConstant.value (Python parameter) — Value expression for the constant. (for strings you need to include quotes!) Can be left empty to create new constant without value.")=`None`*, *[description](#ApiClient.GlobalConstantsDefinition.AppendConstant.description "ApiClient.GlobalConstantsDefinition.AppendConstant.description (Python parameter) — Description of the constant")=`None`*)[¶](#ApiClient.GlobalConstantsDefinition.AppendConstant "Link to this definition")  
Appends a new global constant. If a constant with the same name already exists, it will be overwritten.

Parameters:  name : str[¶](#ApiClient.GlobalConstantsDefinition.AppendConstant.name "Permalink to this definition")  
Name of the constant

value : string[¶](#ApiClient.GlobalConstantsDefinition.AppendConstant.value "Permalink to this definition")  
Value expression for the constant. (for strings you need to include quotes!) Can be left empty to create new constant without value.

description : str[¶](#ApiClient.GlobalConstantsDefinition.AppendConstant.description "Permalink to this definition")  
Description of the constant

Raises:  
**ApiError** – If constant with the given name and value could not be appended, e.g. if the name is no valid identifier, or the value can not be parsed.

Clone()[¶](#ApiClient.GlobalConstantsDefinition.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`GlobalConstantsDefinition`](#ApiClient.GlobalConstantsDefinition "ApiClient.GlobalConstantsDefinition (Python class) — ParameterApi.CreateGlobalConstantsDefinition")

GetAllConstantNames()[¶](#ApiClient.GlobalConstantsDefinition.GetAllConstantNames "Link to this definition")  
Returns a list of all global constant names.

Returns:  List of all global constant names

Return type:  list[str]

GetDescription(*[name](#ApiClient.GlobalConstantsDefinition.GetDescription.name "ApiClient.GlobalConstantsDefinition.GetDescription.name (Python parameter) — Name of the constant")*)[¶](#ApiClient.GlobalConstantsDefinition.GetDescription "Link to this definition")  
Returns the description of the constant specified by the given name.

Parameters:  name : str[¶](#ApiClient.GlobalConstantsDefinition.GetDescription.name "Permalink to this definition")  
Name of the constant

Returns:  Description text

Return type:  str

GetFilename()[¶](#ApiClient.GlobalConstantsDefinition.GetFilename "Link to this definition")  
Returns the file name of the global constants definition file, if this is a file. Returns None if this is part of the test configuration, a parameter set or an unsaved file.

Returns:  The file name of the saved file or None, if not a file

Return type:  str

GetValue(*[name](#ApiClient.GlobalConstantsDefinition.GetValue.name "ApiClient.GlobalConstantsDefinition.GetValue.name (Python parameter) — Name of the constant")*)[¶](#ApiClient.GlobalConstantsDefinition.GetValue "Link to this definition")  
Returns the string representation of the value expression of the constant, specified by the given name.

Parameters:  name : str[¶](#ApiClient.GlobalConstantsDefinition.GetValue.name "Permalink to this definition")  
Name of the constant

Returns:  Expression for the constant value

Return type:  str

Raises:  
**ApiError** – If the constant with the given name does not exist

RemoveConstant(*[name](#ApiClient.GlobalConstantsDefinition.RemoveConstant.name "ApiClient.GlobalConstantsDefinition.RemoveConstant.name (Python parameter) — Name of the constant")*)[¶](#ApiClient.GlobalConstantsDefinition.RemoveConstant "Link to this definition")  
Removes the global constant specified by the given name.

Parameters:  name : str[¶](#ApiClient.GlobalConstantsDefinition.RemoveConstant.name "Permalink to this definition")  
Name of the constant

Returns:  True if successful. False if no constant with such name exists.

Return type:  boolean

Save(*[filename](#ApiClient.GlobalConstantsDefinition.Save.filename "ApiClient.GlobalConstantsDefinition.Save.filename (Python parameter) — File name for the global constants definition file (*.gcd); Either absolute or relative to the 'Parameter' directory. If left out, use the existing file name and path (previously set with Save() or from ParameterApi.OpenGlobalConstantsDefinition())")=`''`*)[¶](#ApiClient.GlobalConstantsDefinition.Save "Link to this definition")  
Saves the global constants definition to a file. Appends file ending if needed.

Parameters:  filename : str[¶](#ApiClient.GlobalConstantsDefinition.Save.filename "Permalink to this definition")  
File name for the global constants definition file (\*.gcd); Either absolute or relative to the ‘Parameter’ directory. If left out, use the existing file name and path (previously set with [`Save()`](#ApiClient.GlobalConstantsDefinition.Save "ApiClient.GlobalConstantsDefinition.Save (Python method) — Saves the global constants definition to a file. Appends file ending if needed.") or from [`ParameterApi.OpenGlobalConstantsDefinition()`](../ParameterApi.md#ApiClient.ParameterApi.OpenGlobalConstantsDefinition "ApiClient.ParameterApi.OpenGlobalConstantsDefinition (Python method) — Opens an existing global constants definition file (*.gcd)."))

SetDescription(*[name](#ApiClient.GlobalConstantsDefinition.SetDescription.name "ApiClient.GlobalConstantsDefinition.SetDescription.name (Python parameter) — Name of the constant")*, *[description](#ApiClient.GlobalConstantsDefinition.SetDescription.description "ApiClient.GlobalConstantsDefinition.SetDescription.description (Python parameter) — Description text")*)[¶](#ApiClient.GlobalConstantsDefinition.SetDescription "Link to this definition")  
Sets the description of the constant specified by the given name.

Parameters:  name : str[¶](#ApiClient.GlobalConstantsDefinition.SetDescription.name "Permalink to this definition")  
Name of the constant

description : str[¶](#ApiClient.GlobalConstantsDefinition.SetDescription.description "Permalink to this definition")  
Description text

Raises:  
- **ApiError** – If the constant with the given name does not exist

- **ApiError** – If description is no str

SetValue(*[name](#ApiClient.GlobalConstantsDefinition.SetValue.name "ApiClient.GlobalConstantsDefinition.SetValue.name (Python parameter) — Name of the constant")*, *[value](#ApiClient.GlobalConstantsDefinition.SetValue.value "ApiClient.GlobalConstantsDefinition.SetValue.value (Python parameter) — Value expression for the constant value (for strings you need to include quotes!) Can be set to 'None' to reset the constant's value.")*)[¶](#ApiClient.GlobalConstantsDefinition.SetValue "Link to this definition")  
Sets the value expression of the constant specified by the given name.

Parameters:  name : str[¶](#ApiClient.GlobalConstantsDefinition.SetValue.name "Permalink to this definition")  
Name of the constant

value : str[¶](#ApiClient.GlobalConstantsDefinition.SetValue.value "Permalink to this definition")  
Value expression for the constant value (for strings you need to include quotes!) Can be set to ‘None’ to reset the constant’s value.

Raises:  
- **ApiError** – If the constant with the given name does not exist

- **ApiError** – If the value is no valid expression

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
