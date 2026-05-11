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

DynamicEnumVariable [ DynamicEnumVariable ](#)

DynamicEnumVariable

- [C DynamicEnumVariable ](#ApiClient.DynamicEnumVariable)
  - [M Clone ](#ApiClient.DynamicEnumVariable.Clone)
  - [M GetDescription ](#ApiClient.DynamicEnumVariable.GetDescription)
  - [M GetExpression ](#ApiClient.DynamicEnumVariable.GetExpression)
  - [M GetInitialText ](#ApiClient.DynamicEnumVariable.GetInitialText)
  - [M GetInitialValue ](#ApiClient.DynamicEnumVariable.GetInitialValue)
  - [M GetName ](#ApiClient.DynamicEnumVariable.GetName)
  - [M GetType ](#ApiClient.DynamicEnumVariable.GetType)
  - [M IsParameter ](#ApiClient.DynamicEnumVariable.IsParameter)
  - [M IsRecorded ](#ApiClient.DynamicEnumVariable.IsRecorded)
  - [M IsReturn ](#ApiClient.DynamicEnumVariable.IsReturn)
  - [M SetDescription ](#ApiClient.DynamicEnumVariable.SetDescription)
  - [M SetExpression ](#ApiClient.DynamicEnumVariable.SetExpression)
  - [M SetParameter ](#ApiClient.DynamicEnumVariable.SetParameter)
  - [M SetRecorded ](#ApiClient.DynamicEnumVariable.SetRecorded)
  - [M SetReturn ](#ApiClient.DynamicEnumVariable.SetReturn)

[ DynamicTextTableVariable ](DynamicTextTableVariable.md)

[ EnumVariable ](EnumVariable.md)

[ EnumVariableElement ](EnumVariableElement.md)

[ FunctionVariable ](FunctionVariable.md)

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

DynamicEnumVariable

- [C DynamicEnumVariable ](#ApiClient.DynamicEnumVariable)
  - [M Clone ](#ApiClient.DynamicEnumVariable.Clone)
  - [M GetDescription ](#ApiClient.DynamicEnumVariable.GetDescription)
  - [M GetExpression ](#ApiClient.DynamicEnumVariable.GetExpression)
  - [M GetInitialText ](#ApiClient.DynamicEnumVariable.GetInitialText)
  - [M GetInitialValue ](#ApiClient.DynamicEnumVariable.GetInitialValue)
  - [M GetName ](#ApiClient.DynamicEnumVariable.GetName)
  - [M GetType ](#ApiClient.DynamicEnumVariable.GetType)
  - [M IsParameter ](#ApiClient.DynamicEnumVariable.IsParameter)
  - [M IsRecorded ](#ApiClient.DynamicEnumVariable.IsRecorded)
  - [M IsReturn ](#ApiClient.DynamicEnumVariable.IsReturn)
  - [M SetDescription ](#ApiClient.DynamicEnumVariable.SetDescription)
  - [M SetExpression ](#ApiClient.DynamicEnumVariable.SetExpression)
  - [M SetParameter ](#ApiClient.DynamicEnumVariable.SetParameter)
  - [M SetRecorded ](#ApiClient.DynamicEnumVariable.SetRecorded)
  - [M SetReturn ](#ApiClient.DynamicEnumVariable.SetReturn)

# DynamicEnumVariable[¶](#dynamicenumvariable "Link to this heading")

*class* DynamicEnumVariable[¶](#ApiClient.DynamicEnumVariable "Link to this definition")  
Returned by

- [`VariableApi.CreateDynamicEnumVariable`](../VariableApi.md#ApiClient.VariableApi.CreateDynamicEnumVariable "ApiClient.VariableApi.CreateDynamicEnumVariable (Python method) — Creates a new Enum variable with dynamic entries.")

Clone()[¶](#ApiClient.DynamicEnumVariable.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`DynamicEnumVariable`](#ApiClient.DynamicEnumVariable "ApiClient.DynamicEnumVariable (Python class) — VariableApi.CreateDynamicEnumVariable")

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

SetDescription(*[description](#ApiClient.DynamicEnumVariable.SetDescription.description "ApiClient.DynamicEnumVariable.SetDescription.description (Python parameter) — Description of variable")*)[¶](#ApiClient.DynamicEnumVariable.SetDescription "Link to this definition")  
Sets the description of the variable.

Parameters:  description : str[¶](#ApiClient.DynamicEnumVariable.SetDescription.description "Permalink to this definition")  
Description of variable

SetExpression(*[expression](#ApiClient.DynamicEnumVariable.SetExpression.expression "ApiClient.DynamicEnumVariable.SetExpression.expression (Python parameter) — Expression that evaluates to a list of strings")*)[¶](#ApiClient.DynamicEnumVariable.SetExpression "Link to this definition")  
Sets the expression that is used to generate the list of strings for the Enum variable.

Parameters:  expression : str[¶](#ApiClient.DynamicEnumVariable.SetExpression.expression "Permalink to this definition")  
Expression that evaluates to a list of strings

SetParameter(*[enable](#ApiClient.DynamicEnumVariable.SetParameter.enable "ApiClient.DynamicEnumVariable.SetParameter.enable (Python parameter) — Whether the variable is a parameter or not")=`True`*)[¶](#ApiClient.DynamicEnumVariable.SetParameter "Link to this definition")  
Sets whether the variable is a parameter or not.

Parameters:  enable : boolean[¶](#ApiClient.DynamicEnumVariable.SetParameter.enable "Permalink to this definition")  
Whether the variable is a parameter or not

SetRecorded(*[enable](#ApiClient.DynamicEnumVariable.SetRecorded.enable "ApiClient.DynamicEnumVariable.SetRecorded.enable (Python parameter) — Whether to enable the recording of the variable")=`True`*)[¶](#ApiClient.DynamicEnumVariable.SetRecorded "Link to this definition")  
Sets the recording state of the variable to the value of enable.

Parameters:  enable : boolean[¶](#ApiClient.DynamicEnumVariable.SetRecorded.enable "Permalink to this definition")  
Whether to enable the recording of the variable

SetReturn(*[enable](#ApiClient.DynamicEnumVariable.SetReturn.enable "ApiClient.DynamicEnumVariable.SetReturn.enable (Python parameter) — Whether the variable is a return value or not")=`True`*)[¶](#ApiClient.DynamicEnumVariable.SetReturn "Link to this definition")  
Sets whether the variable is a return value or not.

Parameters:  enable : boolean[¶](#ApiClient.DynamicEnumVariable.SetReturn.enable "Permalink to this definition")  
Whether the variable is a return value or not

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
