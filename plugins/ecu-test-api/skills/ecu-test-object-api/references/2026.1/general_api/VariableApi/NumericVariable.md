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

NumericVariable [ NumericVariable ](#)

NumericVariable

- [C NumericVariable ](#ApiClient.NumericVariable)
  - [M Clone ](#ApiClient.NumericVariable.Clone)
  - [M GetDescription ](#ApiClient.NumericVariable.GetDescription)
  - [M GetInitialNumericValueString ](#ApiClient.NumericVariable.GetInitialNumericValueString)
  - [M GetInitialValue ](#ApiClient.NumericVariable.GetInitialValue)
  - [M GetName ](#ApiClient.NumericVariable.GetName)
  - [M GetType ](#ApiClient.NumericVariable.GetType)
  - [M IsParameter ](#ApiClient.NumericVariable.IsParameter)
  - [M IsRecorded ](#ApiClient.NumericVariable.IsRecorded)
  - [M IsReturn ](#ApiClient.NumericVariable.IsReturn)
  - [M SetDescription ](#ApiClient.NumericVariable.SetDescription)
  - [M SetInitialNumericValueString ](#ApiClient.NumericVariable.SetInitialNumericValueString)
  - [M SetInitialValue ](#ApiClient.NumericVariable.SetInitialValue)
  - [M SetParameter ](#ApiClient.NumericVariable.SetParameter)
  - [M SetRecorded ](#ApiClient.NumericVariable.SetRecorded)
  - [M SetReturn ](#ApiClient.NumericVariable.SetReturn)

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

NumericVariable

- [C NumericVariable ](#ApiClient.NumericVariable)
  - [M Clone ](#ApiClient.NumericVariable.Clone)
  - [M GetDescription ](#ApiClient.NumericVariable.GetDescription)
  - [M GetInitialNumericValueString ](#ApiClient.NumericVariable.GetInitialNumericValueString)
  - [M GetInitialValue ](#ApiClient.NumericVariable.GetInitialValue)
  - [M GetName ](#ApiClient.NumericVariable.GetName)
  - [M GetType ](#ApiClient.NumericVariable.GetType)
  - [M IsParameter ](#ApiClient.NumericVariable.IsParameter)
  - [M IsRecorded ](#ApiClient.NumericVariable.IsRecorded)
  - [M IsReturn ](#ApiClient.NumericVariable.IsReturn)
  - [M SetDescription ](#ApiClient.NumericVariable.SetDescription)
  - [M SetInitialNumericValueString ](#ApiClient.NumericVariable.SetInitialNumericValueString)
  - [M SetInitialValue ](#ApiClient.NumericVariable.SetInitialValue)
  - [M SetParameter ](#ApiClient.NumericVariable.SetParameter)
  - [M SetRecorded ](#ApiClient.NumericVariable.SetRecorded)
  - [M SetReturn ](#ApiClient.NumericVariable.SetReturn)

# NumericVariable[¶](#numericvariable "Link to this heading")

*class* NumericVariable[¶](#ApiClient.NumericVariable "Link to this definition")  
Returned by

- [`VariableApi.CreateNumericVariable`](../VariableApi.md#ApiClient.VariableApi.CreateNumericVariable "ApiClient.VariableApi.CreateNumericVariable (Python method) — Creates a new numeric variable.")

Clone()[¶](#ApiClient.NumericVariable.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`NumericVariable`](#ApiClient.NumericVariable "ApiClient.NumericVariable (Python class) — VariableApi.CreateNumericVariable")

GetDescription()[¶](#ApiClient.NumericVariable.GetDescription "Link to this definition")  
Returns the description of the variable.

Returns:  Description of variable

Return type:  str

GetInitialNumericValueString()[¶](#ApiClient.NumericVariable.GetInitialNumericValueString "Link to this definition")  
Returns the initial value string of the variable, or None if it is not a Numeric.

The initial value is returned exactly as it has been typed in (e.g. in hex, or with additional zeroes), unless it has been set via `SetInitialNumericValue()`, which stores only the numeric value itself.

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

SetDescription(*[description](#ApiClient.NumericVariable.SetDescription.description "ApiClient.NumericVariable.SetDescription.description (Python parameter) — Description of variable")*)[¶](#ApiClient.NumericVariable.SetDescription "Link to this definition")  
Sets the description of the variable.

Parameters:  description : str[¶](#ApiClient.NumericVariable.SetDescription.description "Permalink to this definition")  
Description of variable

SetInitialNumericValueString(*[value](#ApiClient.NumericVariable.SetInitialNumericValueString.value "ApiClient.NumericVariable.SetInitialNumericValueString.value (Python parameter) — Initial value of the variable")*)[¶](#ApiClient.NumericVariable.SetInitialNumericValueString "Link to this definition")  
Sets the initial value of the variable as string.

The string will be stored exactly as typed (e.g. in hex, or with additional zeroes).

Parameters:  value : str[¶](#ApiClient.NumericVariable.SetInitialNumericValueString.value "Permalink to this definition")  
Initial value of the variable

SetInitialValue(*[value](#ApiClient.NumericVariable.SetInitialValue.value "ApiClient.NumericVariable.SetInitialValue.value (Python parameter) — Initial value of the variable")*)[¶](#ApiClient.NumericVariable.SetInitialValue "Link to this definition")  
Sets the initial value of the variable.

Only the numeric value itself will be stored, not the way it has been typed in (e.g. in hex, or with additional zeroes).

Parameters:  value : int/float[¶](#ApiClient.NumericVariable.SetInitialValue.value "Permalink to this definition")  
Initial value of the variable

SetParameter(*[enable](#ApiClient.NumericVariable.SetParameter.enable "ApiClient.NumericVariable.SetParameter.enable (Python parameter) — Whether the variable is a parameter or not")=`True`*)[¶](#ApiClient.NumericVariable.SetParameter "Link to this definition")  
Sets whether the variable is a parameter or not.

Parameters:  enable : boolean[¶](#ApiClient.NumericVariable.SetParameter.enable "Permalink to this definition")  
Whether the variable is a parameter or not

SetRecorded(*[enable](#ApiClient.NumericVariable.SetRecorded.enable "ApiClient.NumericVariable.SetRecorded.enable (Python parameter) — Whether to enable the recording of the variable")=`True`*)[¶](#ApiClient.NumericVariable.SetRecorded "Link to this definition")  
Sets the recording state of the variable to the value of enable.

Parameters:  enable : boolean[¶](#ApiClient.NumericVariable.SetRecorded.enable "Permalink to this definition")  
Whether to enable the recording of the variable

SetReturn(*[enable](#ApiClient.NumericVariable.SetReturn.enable "ApiClient.NumericVariable.SetReturn.enable (Python parameter) — Whether the variable is a return value or not")=`True`*)[¶](#ApiClient.NumericVariable.SetReturn "Link to this definition")  
Sets whether the variable is a return value or not.

Parameters:  enable : boolean[¶](#ApiClient.NumericVariable.SetReturn.enable "Permalink to this definition")  
Whether the variable is a return value or not

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
