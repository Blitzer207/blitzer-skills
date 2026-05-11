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

DynamicTextTableVariable [ DynamicTextTableVariable ](#)

DynamicTextTableVariable

- [C DynamicTextTableVariable ](#ApiClient.DynamicTextTableVariable)
  - [M Clone ](#ApiClient.DynamicTextTableVariable.Clone)
  - [M GetDescription ](#ApiClient.DynamicTextTableVariable.GetDescription)
  - [M GetExpression ](#ApiClient.DynamicTextTableVariable.GetExpression)
  - [M GetInitialValue ](#ApiClient.DynamicTextTableVariable.GetInitialValue)
  - [M GetName ](#ApiClient.DynamicTextTableVariable.GetName)
  - [M GetType ](#ApiClient.DynamicTextTableVariable.GetType)
  - [M IsParameter ](#ApiClient.DynamicTextTableVariable.IsParameter)
  - [M IsRecorded ](#ApiClient.DynamicTextTableVariable.IsRecorded)
  - [M IsReturn ](#ApiClient.DynamicTextTableVariable.IsReturn)
  - [M SetDescription ](#ApiClient.DynamicTextTableVariable.SetDescription)
  - [M SetExpression ](#ApiClient.DynamicTextTableVariable.SetExpression)
  - [M SetParameter ](#ApiClient.DynamicTextTableVariable.SetParameter)
  - [M SetRecorded ](#ApiClient.DynamicTextTableVariable.SetRecorded)
  - [M SetReturn ](#ApiClient.DynamicTextTableVariable.SetReturn)

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

DynamicTextTableVariable

- [C DynamicTextTableVariable ](#ApiClient.DynamicTextTableVariable)
  - [M Clone ](#ApiClient.DynamicTextTableVariable.Clone)
  - [M GetDescription ](#ApiClient.DynamicTextTableVariable.GetDescription)
  - [M GetExpression ](#ApiClient.DynamicTextTableVariable.GetExpression)
  - [M GetInitialValue ](#ApiClient.DynamicTextTableVariable.GetInitialValue)
  - [M GetName ](#ApiClient.DynamicTextTableVariable.GetName)
  - [M GetType ](#ApiClient.DynamicTextTableVariable.GetType)
  - [M IsParameter ](#ApiClient.DynamicTextTableVariable.IsParameter)
  - [M IsRecorded ](#ApiClient.DynamicTextTableVariable.IsRecorded)
  - [M IsReturn ](#ApiClient.DynamicTextTableVariable.IsReturn)
  - [M SetDescription ](#ApiClient.DynamicTextTableVariable.SetDescription)
  - [M SetExpression ](#ApiClient.DynamicTextTableVariable.SetExpression)
  - [M SetParameter ](#ApiClient.DynamicTextTableVariable.SetParameter)
  - [M SetRecorded ](#ApiClient.DynamicTextTableVariable.SetRecorded)
  - [M SetReturn ](#ApiClient.DynamicTextTableVariable.SetReturn)

# DynamicTextTableVariable[¶](#dynamictexttablevariable "Link to this heading")

*class* DynamicTextTableVariable[¶](#ApiClient.DynamicTextTableVariable "Link to this definition")  
Returned by

- [`VariableApi.CreateDynamicTextTableVariable`](../VariableApi.md#ApiClient.VariableApi.CreateDynamicTextTableVariable "ApiClient.VariableApi.CreateDynamicTextTableVariable (Python method) — Creates a new Texttable variable with dynamic text entries.")

Clone()[¶](#ApiClient.DynamicTextTableVariable.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`DynamicTextTableVariable`](#ApiClient.DynamicTextTableVariable "ApiClient.DynamicTextTableVariable (Python class) — VariableApi.CreateDynamicTextTableVariable")

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

SetDescription(*[description](#ApiClient.DynamicTextTableVariable.SetDescription.description "ApiClient.DynamicTextTableVariable.SetDescription.description (Python parameter) — Description of variable")*)[¶](#ApiClient.DynamicTextTableVariable.SetDescription "Link to this definition")  
Sets the description of the variable.

Parameters:  description : str[¶](#ApiClient.DynamicTextTableVariable.SetDescription.description "Permalink to this definition")  
Description of variable

SetExpression(*[expression](#ApiClient.DynamicTextTableVariable.SetExpression.expression "ApiClient.DynamicTextTableVariable.SetExpression.expression (Python parameter) — Expression that evaluates to a list of strings")*)[¶](#ApiClient.DynamicTextTableVariable.SetExpression "Link to this definition")  
Sets the expression that is used to generate the list of strings for the Texttable variable.

Parameters:  expression : str[¶](#ApiClient.DynamicTextTableVariable.SetExpression.expression "Permalink to this definition")  
Expression that evaluates to a list of strings

SetParameter(*[enable](#ApiClient.DynamicTextTableVariable.SetParameter.enable "ApiClient.DynamicTextTableVariable.SetParameter.enable (Python parameter) — Whether the variable is a parameter or not")=`True`*)[¶](#ApiClient.DynamicTextTableVariable.SetParameter "Link to this definition")  
Sets whether the variable is a parameter or not.

Parameters:  enable : boolean[¶](#ApiClient.DynamicTextTableVariable.SetParameter.enable "Permalink to this definition")  
Whether the variable is a parameter or not

SetRecorded(*[enable](#ApiClient.DynamicTextTableVariable.SetRecorded.enable "ApiClient.DynamicTextTableVariable.SetRecorded.enable (Python parameter) — Whether to enable the recording of the variable")=`True`*)[¶](#ApiClient.DynamicTextTableVariable.SetRecorded "Link to this definition")  
Sets the recording state of the variable to the value of enable.

Parameters:  enable : boolean[¶](#ApiClient.DynamicTextTableVariable.SetRecorded.enable "Permalink to this definition")  
Whether to enable the recording of the variable

SetReturn(*[enable](#ApiClient.DynamicTextTableVariable.SetReturn.enable "ApiClient.DynamicTextTableVariable.SetReturn.enable (Python parameter) — Whether the variable is a return value or not")=`True`*)[¶](#ApiClient.DynamicTextTableVariable.SetReturn "Link to this definition")  
Sets whether the variable is a return value or not.

Parameters:  enable : boolean[¶](#ApiClient.DynamicTextTableVariable.SetReturn.enable "Permalink to this definition")  
Whether the variable is a return value or not

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
