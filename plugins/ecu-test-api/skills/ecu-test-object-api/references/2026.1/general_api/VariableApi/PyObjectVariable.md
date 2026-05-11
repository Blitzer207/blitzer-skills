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

API for Variables

[ BooleanVariable ](BooleanVariable.md)

[ DynamicEnumVariable ](DynamicEnumVariable.md)

[ DynamicTextTableVariable ](DynamicTextTableVariable.md)

[ EnumVariable ](EnumVariable.md)

[ EnumVariableElement ](EnumVariableElement.md)

[ FunctionVariable ](FunctionVariable.md)

[ NumericVariable ](NumericVariable.md)

PyObjectVariable [ PyObjectVariable ](#)

PyObjectVariable

- [C PyObjectVariable ](#ApiClient.PyObjectVariable)
  - [M Clone ](#ApiClient.PyObjectVariable.Clone)
  - [M GetDescription ](#ApiClient.PyObjectVariable.GetDescription)
  - [M GetInitialValue ](#ApiClient.PyObjectVariable.GetInitialValue)
  - [M GetName ](#ApiClient.PyObjectVariable.GetName)
  - [M GetType ](#ApiClient.PyObjectVariable.GetType)
  - [M IsParameter ](#ApiClient.PyObjectVariable.IsParameter)
  - [M IsRecorded ](#ApiClient.PyObjectVariable.IsRecorded)
  - [M IsReturn ](#ApiClient.PyObjectVariable.IsReturn)
  - [M SetDescription ](#ApiClient.PyObjectVariable.SetDescription)
  - [M SetInitialValue ](#ApiClient.PyObjectVariable.SetInitialValue)
  - [M SetParameter ](#ApiClient.PyObjectVariable.SetParameter)
  - [M SetRecorded ](#ApiClient.PyObjectVariable.SetRecorded)
  - [M SetReturn ](#ApiClient.PyObjectVariable.SetReturn)

[ StaticTextTableVariable ](StaticTextTableVariable.md)

[ StringVariable ](StringVariable.md)

[ StructureVariable ](StructureVariable.md)

[ Variable ](Variable.md)

[ VectorVariable ](VectorVariable.md)

[ API for Workspaces ](../WorkspaceApi.md)

[ Trace Analysis API ](../../TraceAnalysisAPI/index.md)

[ Generator APIs ](../../generators/index.md)

[ Tools ](../../tools/index.md)

[ User test management ](../../userTestmanagement/index.md)

[ UserUtility API ](../../user-utility/user-utility.md)

[ Utility Examples ](../../user-utility/example-utilities.md)

PyObjectVariable

- [C PyObjectVariable ](#ApiClient.PyObjectVariable)
  - [M Clone ](#ApiClient.PyObjectVariable.Clone)
  - [M GetDescription ](#ApiClient.PyObjectVariable.GetDescription)
  - [M GetInitialValue ](#ApiClient.PyObjectVariable.GetInitialValue)
  - [M GetName ](#ApiClient.PyObjectVariable.GetName)
  - [M GetType ](#ApiClient.PyObjectVariable.GetType)
  - [M IsParameter ](#ApiClient.PyObjectVariable.IsParameter)
  - [M IsRecorded ](#ApiClient.PyObjectVariable.IsRecorded)
  - [M IsReturn ](#ApiClient.PyObjectVariable.IsReturn)
  - [M SetDescription ](#ApiClient.PyObjectVariable.SetDescription)
  - [M SetInitialValue ](#ApiClient.PyObjectVariable.SetInitialValue)
  - [M SetParameter ](#ApiClient.PyObjectVariable.SetParameter)
  - [M SetRecorded ](#ApiClient.PyObjectVariable.SetRecorded)
  - [M SetReturn ](#ApiClient.PyObjectVariable.SetReturn)

# PyObjectVariable[¶](#pyobjectvariable "Link to this heading")

*class* PyObjectVariable[¶](#ApiClient.PyObjectVariable "Link to this definition")  
Returned by

- [`VariableApi.CreatePyObjectVariable`](../VariableApi.md#ApiClient.VariableApi.CreatePyObjectVariable "ApiClient.VariableApi.CreatePyObjectVariable (Python method) — Creates a new PyObject variable.")

Clone()[¶](#ApiClient.PyObjectVariable.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`PyObjectVariable`](#ApiClient.PyObjectVariable "ApiClient.PyObjectVariable (Python class) — VariableApi.CreatePyObjectVariable")

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

SetDescription(*[description](#ApiClient.PyObjectVariable.SetDescription.description "ApiClient.PyObjectVariable.SetDescription.description (Python parameter) — Description of variable")*)[¶](#ApiClient.PyObjectVariable.SetDescription "Link to this definition")  
Sets the description of the variable.

Parameters:  description : str[¶](#ApiClient.PyObjectVariable.SetDescription.description "Permalink to this definition")  
Description of variable

SetInitialValue(*[value](#ApiClient.PyObjectVariable.SetInitialValue.value "ApiClient.PyObjectVariable.SetInitialValue.value (Python parameter) — May only consist of the following Python literal structures: strings, numbers, tuples, lists, dicts, booleans, and None")*)[¶](#ApiClient.PyObjectVariable.SetInitialValue "Link to this definition")  
Sets the initial value of the variable.

Parameters:  value : string[¶](#ApiClient.PyObjectVariable.SetInitialValue.value "Permalink to this definition")  
May only consist of the following Python literal structures: strings, numbers, tuples, lists, dicts, booleans, and None

SetParameter(*[enable](#ApiClient.PyObjectVariable.SetParameter.enable "ApiClient.PyObjectVariable.SetParameter.enable (Python parameter) — Whether the variable is a parameter or not")=`True`*)[¶](#ApiClient.PyObjectVariable.SetParameter "Link to this definition")  
Sets whether the variable is a parameter or not.

Parameters:  enable : boolean[¶](#ApiClient.PyObjectVariable.SetParameter.enable "Permalink to this definition")  
Whether the variable is a parameter or not

SetRecorded(*[enable](#ApiClient.PyObjectVariable.SetRecorded.enable "ApiClient.PyObjectVariable.SetRecorded.enable (Python parameter) — Whether to enable the recording of the variable")=`True`*)[¶](#ApiClient.PyObjectVariable.SetRecorded "Link to this definition")  
Sets the recording state of the variable to the value of enable.

Parameters:  enable : boolean[¶](#ApiClient.PyObjectVariable.SetRecorded.enable "Permalink to this definition")  
Whether to enable the recording of the variable

SetReturn(*[enable](#ApiClient.PyObjectVariable.SetReturn.enable "ApiClient.PyObjectVariable.SetReturn.enable (Python parameter) — Whether the variable is a return value or not")=`True`*)[¶](#ApiClient.PyObjectVariable.SetReturn "Link to this definition")  
Sets whether the variable is a return value or not.

Parameters:  enable : boolean[¶](#ApiClient.PyObjectVariable.SetReturn.enable "Permalink to this definition")  
Whether the variable is a return value or not

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
