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

FunctionVariable [ FunctionVariable ](#)

FunctionVariable

- [C FunctionVariable ](#ApiClient.FunctionVariable)
  - [M Clone ](#ApiClient.FunctionVariable.Clone)
  - [M GetDescription ](#ApiClient.FunctionVariable.GetDescription)
  - [M GetInitialValue ](#ApiClient.FunctionVariable.GetInitialValue)
  - [M GetName ](#ApiClient.FunctionVariable.GetName)
  - [M GetType ](#ApiClient.FunctionVariable.GetType)
  - [M IsParameter ](#ApiClient.FunctionVariable.IsParameter)
  - [M IsRecorded ](#ApiClient.FunctionVariable.IsRecorded)
  - [M IsReturn ](#ApiClient.FunctionVariable.IsReturn)
  - [M SetDescription ](#ApiClient.FunctionVariable.SetDescription)
  - [M SetInitialValue ](#ApiClient.FunctionVariable.SetInitialValue)
  - [M SetParameter ](#ApiClient.FunctionVariable.SetParameter)
  - [M SetRecorded ](#ApiClient.FunctionVariable.SetRecorded)
  - [M SetReturn ](#ApiClient.FunctionVariable.SetReturn)

[ NumericVariable ](NumericVariable.md)

[ PyObjectVariable ](PyObjectVariable.md)

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

FunctionVariable

- [C FunctionVariable ](#ApiClient.FunctionVariable)
  - [M Clone ](#ApiClient.FunctionVariable.Clone)
  - [M GetDescription ](#ApiClient.FunctionVariable.GetDescription)
  - [M GetInitialValue ](#ApiClient.FunctionVariable.GetInitialValue)
  - [M GetName ](#ApiClient.FunctionVariable.GetName)
  - [M GetType ](#ApiClient.FunctionVariable.GetType)
  - [M IsParameter ](#ApiClient.FunctionVariable.IsParameter)
  - [M IsRecorded ](#ApiClient.FunctionVariable.IsRecorded)
  - [M IsReturn ](#ApiClient.FunctionVariable.IsReturn)
  - [M SetDescription ](#ApiClient.FunctionVariable.SetDescription)
  - [M SetInitialValue ](#ApiClient.FunctionVariable.SetInitialValue)
  - [M SetParameter ](#ApiClient.FunctionVariable.SetParameter)
  - [M SetRecorded ](#ApiClient.FunctionVariable.SetRecorded)
  - [M SetReturn ](#ApiClient.FunctionVariable.SetReturn)

# FunctionVariable[¶](#functionvariable "Link to this heading")

*class* FunctionVariable[¶](#ApiClient.FunctionVariable "Link to this definition")  
Returned by

- [`VariableApi.CreateFunctionVariable`](../VariableApi.md#ApiClient.VariableApi.CreateFunctionVariable "ApiClient.VariableApi.CreateFunctionVariable (Python method) — Creates a new function variable.")

Clone()[¶](#ApiClient.FunctionVariable.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`FunctionVariable`](#ApiClient.FunctionVariable "ApiClient.FunctionVariable (Python class) — VariableApi.CreateFunctionVariable")

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

SetDescription(*[description](#ApiClient.FunctionVariable.SetDescription.description "ApiClient.FunctionVariable.SetDescription.description (Python parameter) — Description of variable")*)[¶](#ApiClient.FunctionVariable.SetDescription "Link to this definition")  
Sets the description of the variable.

Parameters:  description : str[¶](#ApiClient.FunctionVariable.SetDescription.description "Permalink to this definition")  
Description of variable

SetInitialValue(*[value](#ApiClient.FunctionVariable.SetInitialValue.value "ApiClient.FunctionVariable.SetInitialValue.value (Python parameter) — Python code to be executed")*)[¶](#ApiClient.FunctionVariable.SetInitialValue "Link to this definition")  
Sets the code of the Function.

Parameters:  value : string[¶](#ApiClient.FunctionVariable.SetInitialValue.value "Permalink to this definition")  
Python code to be executed

SetParameter(*[enable](#ApiClient.FunctionVariable.SetParameter.enable "ApiClient.FunctionVariable.SetParameter.enable (Python parameter) — Whether the variable is a parameter or not")=`True`*)[¶](#ApiClient.FunctionVariable.SetParameter "Link to this definition")  
Sets whether the variable is a parameter or not.

Parameters:  enable : boolean[¶](#ApiClient.FunctionVariable.SetParameter.enable "Permalink to this definition")  
Whether the variable is a parameter or not

SetRecorded(*[enable](#ApiClient.FunctionVariable.SetRecorded.enable "ApiClient.FunctionVariable.SetRecorded.enable (Python parameter) — Whether to enable the recording of the variable")=`True`*)[¶](#ApiClient.FunctionVariable.SetRecorded "Link to this definition")  
Sets the recording state of the variable to the value of enable.

Parameters:  enable : boolean[¶](#ApiClient.FunctionVariable.SetRecorded.enable "Permalink to this definition")  
Whether to enable the recording of the variable

SetReturn(*[enable](#ApiClient.FunctionVariable.SetReturn.enable "ApiClient.FunctionVariable.SetReturn.enable (Python parameter) — Whether the variable is a return value or not")=`True`*)[¶](#ApiClient.FunctionVariable.SetReturn "Link to this definition")  
Sets whether the variable is a return value or not.

Parameters:  enable : boolean[¶](#ApiClient.FunctionVariable.SetReturn.enable "Permalink to this definition")  
Whether the variable is a return value or not

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
