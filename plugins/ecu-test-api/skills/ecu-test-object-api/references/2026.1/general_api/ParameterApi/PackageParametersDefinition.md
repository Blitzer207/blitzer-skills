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

[ GlobalConstantsDefinition ](GlobalConstantsDefinition.md)

PackageParametersDefinition [ PackageParametersDefinition ](#)

PackageParametersDefinition

- [C PackageParametersDefinition ](#ApiClient.PackageParametersDefinition)
  - [M AppendParameter ](#ApiClient.PackageParametersDefinition.AppendParameter)
  - [M Clone ](#ApiClient.PackageParametersDefinition.Clone)
  - [M GetAllParameterNames ](#ApiClient.PackageParametersDefinition.GetAllParameterNames)
  - [M GetDescription ](#ApiClient.PackageParametersDefinition.GetDescription)
  - [M GetFilename ](#ApiClient.PackageParametersDefinition.GetFilename)
  - [M GetValue ](#ApiClient.PackageParametersDefinition.GetValue)
  - [M RemoveParameter ](#ApiClient.PackageParametersDefinition.RemoveParameter)
  - [M Save ](#ApiClient.PackageParametersDefinition.Save)
  - [M SetDescription ](#ApiClient.PackageParametersDefinition.SetDescription)
  - [M SetValue ](#ApiClient.PackageParametersDefinition.SetValue)

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

PackageParametersDefinition

- [C PackageParametersDefinition ](#ApiClient.PackageParametersDefinition)
  - [M AppendParameter ](#ApiClient.PackageParametersDefinition.AppendParameter)
  - [M Clone ](#ApiClient.PackageParametersDefinition.Clone)
  - [M GetAllParameterNames ](#ApiClient.PackageParametersDefinition.GetAllParameterNames)
  - [M GetDescription ](#ApiClient.PackageParametersDefinition.GetDescription)
  - [M GetFilename ](#ApiClient.PackageParametersDefinition.GetFilename)
  - [M GetValue ](#ApiClient.PackageParametersDefinition.GetValue)
  - [M RemoveParameter ](#ApiClient.PackageParametersDefinition.RemoveParameter)
  - [M Save ](#ApiClient.PackageParametersDefinition.Save)
  - [M SetDescription ](#ApiClient.PackageParametersDefinition.SetDescription)
  - [M SetValue ](#ApiClient.PackageParametersDefinition.SetValue)

# PackageParametersDefinition[¶](#packageparametersdefinition "Link to this heading")

*class* PackageParametersDefinition[¶](#ApiClient.PackageParametersDefinition "Link to this definition")  
Returned by

- [`ParameterApi.CreatePackageParametersDefinition`](../ParameterApi.md#ApiClient.ParameterApi.CreatePackageParametersDefinition "ApiClient.ParameterApi.CreatePackageParametersDefinition (Python method) — Creates a new package parameters definition.")

- [`ParameterApi.OpenPackageParametersDefinition`](../ParameterApi.md#ApiClient.ParameterApi.OpenPackageParametersDefinition "ApiClient.ParameterApi.OpenPackageParametersDefinition (Python method) — Opens an existing package parameters definition file (*.ppd).")

- [`ParameterApi.SearchPackageParametersDefinitions`](../ParameterApi.md#ApiClient.ParameterApi.SearchPackageParametersDefinitions "ApiClient.ParameterApi.SearchPackageParametersDefinitions (Python method) — Searches the current workspace and library workspaces for Package Parameter Definitions matching the given search criteria.")

AppendParameter(*[name](#ApiClient.PackageParametersDefinition.AppendParameter.name "ApiClient.PackageParametersDefinition.AppendParameter.name (Python parameter) — Name of the parameter")*, *[value](#ApiClient.PackageParametersDefinition.AppendParameter.value "ApiClient.PackageParametersDefinition.AppendParameter.value (Python parameter) — Value of the parameter as you would type it in the dialog (i.e.")=`None`*, *[description](#ApiClient.PackageParametersDefinition.AppendParameter.description "ApiClient.PackageParametersDefinition.AppendParameter.description (Python parameter) — Description of the parameter")=`None`*)[¶](#ApiClient.PackageParametersDefinition.AppendParameter "Link to this definition")  
Appends a new package parameter. If a parameter with the same name already exists, it will be overwritten.

Parameters:  name : str[¶](#ApiClient.PackageParametersDefinition.AppendParameter.name "Permalink to this definition")  
Name of the parameter

value : string[¶](#ApiClient.PackageParametersDefinition.AppendParameter.value "Permalink to this definition")  
Value of the parameter as you would type it in the dialog (i.e. for strings you need to include the quotes!)

description : str[¶](#ApiClient.PackageParametersDefinition.AppendParameter.description "Permalink to this definition")  
Description of the parameter

Raises:  
**ApiError** – If parameter with the given name (and value/description) could not be appended, e.g. if the value or description are invalid.

Clone()[¶](#ApiClient.PackageParametersDefinition.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`PackageParametersDefinition`](#ApiClient.PackageParametersDefinition "ApiClient.PackageParametersDefinition (Python class) — ParameterApi.CreatePackageParametersDefinition")

GetAllParameterNames()[¶](#ApiClient.PackageParametersDefinition.GetAllParameterNames "Link to this definition")  
Returns a list of all parameterized package parameter names.

Returns:  List of all parameterized parameter names

Return type:  list[str]

GetDescription(*[name](#ApiClient.PackageParametersDefinition.GetDescription.name "ApiClient.PackageParametersDefinition.GetDescription.name (Python parameter) — Name of the parameter to get the description of")*)[¶](#ApiClient.PackageParametersDefinition.GetDescription "Link to this definition")  
Returns the description of the parameter specified by the given name.

Parameters:  name : str[¶](#ApiClient.PackageParametersDefinition.GetDescription.name "Permalink to this definition")  
Name of the parameter to get the description of

Returns:  The desription of the parameter

Return type:  str

GetFilename()[¶](#ApiClient.PackageParametersDefinition.GetFilename "Link to this definition")  
Returns the file name of the package parameters definition file, if this is a file. Returns None if this is part of a parameter set or an unsaved file.

Returns:  The file name of the saved file or None, if not a file

Return type:  str

GetValue(*[name](#ApiClient.PackageParametersDefinition.GetValue.name "ApiClient.PackageParametersDefinition.GetValue.name (Python parameter) — Name of the parameter to get the value of")*)[¶](#ApiClient.PackageParametersDefinition.GetValue "Link to this definition")  
Returns the value of the given parameter. If the value of an existing parameter is empty it will return None, if the value is defined as None it will return ‘None’.

Parameters:  name : str[¶](#ApiClient.PackageParametersDefinition.GetValue.name "Permalink to this definition")  
Name of the parameter to get the value of

Returns:  Value of the given parameter

Return type:  str

Raises:  
**ApiError** – If the parameter with the given name does not exist

RemoveParameter(*[name](#ApiClient.PackageParametersDefinition.RemoveParameter.name "ApiClient.PackageParametersDefinition.RemoveParameter.name (Python parameter) — Name of the parameter to remove")*)[¶](#ApiClient.PackageParametersDefinition.RemoveParameter "Link to this definition")  
Removes the parameter specified by the given name.

Parameters:  name : str[¶](#ApiClient.PackageParametersDefinition.RemoveParameter.name "Permalink to this definition")  
Name of the parameter to remove

Returns:  If removing of the given parameter was successful

Return type:  boolean

Save(*[filename](#ApiClient.PackageParametersDefinition.Save.filename "ApiClient.PackageParametersDefinition.Save.filename (Python parameter) — File name of the package parameters definition file (*.ppd); Either absolute or relative to the 'Parameter' directory. Leave out to save the definitions to its existing file (previously set with Save() or from ParameterApi.OpenPackageParametersDefinition())")=`None`*)[¶](#ApiClient.PackageParametersDefinition.Save "Link to this definition")  
Saves the package parameters definition to a file. Appends file ending if needed.

Parameters:  filename : str[¶](#ApiClient.PackageParametersDefinition.Save.filename "Permalink to this definition")  
File name of the package parameters definition file (\*.ppd); Either absolute or relative to the ‘Parameter’ directory. Leave out to save the definitions to its existing file (previously set with [`Save()`](#ApiClient.PackageParametersDefinition.Save "ApiClient.PackageParametersDefinition.Save (Python method) — Saves the package parameters definition to a file. Appends file ending if needed.") or from [`ParameterApi.OpenPackageParametersDefinition()`](../ParameterApi.md#ApiClient.ParameterApi.OpenPackageParametersDefinition "ApiClient.ParameterApi.OpenPackageParametersDefinition (Python method) — Opens an existing package parameters definition file (*.ppd)."))

SetDescription(*[name](#ApiClient.PackageParametersDefinition.SetDescription.name "ApiClient.PackageParametersDefinition.SetDescription.name (Python parameter) — Name of the parameter to set the description of")*, *[description](#ApiClient.PackageParametersDefinition.SetDescription.description "ApiClient.PackageParametersDefinition.SetDescription.description (Python parameter) — Description of the parameter to be set")*)[¶](#ApiClient.PackageParametersDefinition.SetDescription "Link to this definition")  
Sets the description of the parameter specified by the given name.

Parameters:  name : str[¶](#ApiClient.PackageParametersDefinition.SetDescription.name "Permalink to this definition")  
Name of the parameter to set the description of

description : str[¶](#ApiClient.PackageParametersDefinition.SetDescription.description "Permalink to this definition")  
Description of the parameter to be set

Raises:  
- **ApiError** – If the parameter with the given name does not exist

- **ApiError** – If description is no str

SetValue(*[name](#ApiClient.PackageParametersDefinition.SetValue.name "ApiClient.PackageParametersDefinition.SetValue.name (Python parameter) — Name of the parameter to set the value of")*, *[value](#ApiClient.PackageParametersDefinition.SetValue.value "ApiClient.PackageParametersDefinition.SetValue.value (Python parameter) — Value of the parameter as you would type it in the editor (i.e.")=`None`*)[¶](#ApiClient.PackageParametersDefinition.SetValue "Link to this definition")  
Sets the value of the parameter specified by the given name.

Parameters:  name : str[¶](#ApiClient.PackageParametersDefinition.SetValue.name "Permalink to this definition")  
Name of the parameter to set the value of

value : str[¶](#ApiClient.PackageParametersDefinition.SetValue.value "Permalink to this definition")  
Value of the parameter as you would type it in the editor (i.e. for strings you need to include the quotes!) Can be set to ‘None’ to reset the parameter value.

Raises:  
- **ApiError** – If the parameter with the given name does not exist

- **ApiError** – If the value is no valid expression

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
