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

[ PyObjectVariable ](PyObjectVariable.md)

[ StaticTextTableVariable ](StaticTextTableVariable.md)

[ StringVariable ](StringVariable.md)

[ StructureVariable ](StructureVariable.md)

[ Variable ](Variable.md)

VectorVariable [ VectorVariable ](#)

VectorVariable

- [C VectorVariable ](#ApiClient.VectorVariable)
  - [M Clone ](#ApiClient.VectorVariable.Clone)
  - [M DeleteInitialElementValue ](#ApiClient.VectorVariable.DeleteInitialElementValue)
  - [M GetDescription ](#ApiClient.VectorVariable.GetDescription)
  - [M GetDimension ](#ApiClient.VectorVariable.GetDimension)
  - [M GetInitialElementValue ](#ApiClient.VectorVariable.GetInitialElementValue)
  - [M GetInitialValue ](#ApiClient.VectorVariable.GetInitialValue)
  - [M GetName ](#ApiClient.VectorVariable.GetName)
  - [M GetType ](#ApiClient.VectorVariable.GetType)
  - [M IsParameter ](#ApiClient.VectorVariable.IsParameter)
  - [M IsRecorded ](#ApiClient.VectorVariable.IsRecorded)
  - [M IsReturn ](#ApiClient.VectorVariable.IsReturn)
  - [M SetDescription ](#ApiClient.VectorVariable.SetDescription)
  - [M SetDimension ](#ApiClient.VectorVariable.SetDimension)
  - [M SetInitialElementValue ](#ApiClient.VectorVariable.SetInitialElementValue)
  - [M SetInitialValue ](#ApiClient.VectorVariable.SetInitialValue)
  - [M SetParameter ](#ApiClient.VectorVariable.SetParameter)
  - [M SetRecorded ](#ApiClient.VectorVariable.SetRecorded)
  - [M SetReturn ](#ApiClient.VectorVariable.SetReturn)

[ API for Workspaces ](../WorkspaceApi.md)

[ Trace Analysis API ](../../TraceAnalysisAPI/index.md)

[ Generator APIs ](../../generators/index.md)

[ Tools ](../../tools/index.md)

[ User test management ](../../userTestmanagement/index.md)

[ UserUtility API ](../../user-utility/user-utility.md)

[ Utility Examples ](../../user-utility/example-utilities.md)

VectorVariable

- [C VectorVariable ](#ApiClient.VectorVariable)
  - [M Clone ](#ApiClient.VectorVariable.Clone)
  - [M DeleteInitialElementValue ](#ApiClient.VectorVariable.DeleteInitialElementValue)
  - [M GetDescription ](#ApiClient.VectorVariable.GetDescription)
  - [M GetDimension ](#ApiClient.VectorVariable.GetDimension)
  - [M GetInitialElementValue ](#ApiClient.VectorVariable.GetInitialElementValue)
  - [M GetInitialValue ](#ApiClient.VectorVariable.GetInitialValue)
  - [M GetName ](#ApiClient.VectorVariable.GetName)
  - [M GetType ](#ApiClient.VectorVariable.GetType)
  - [M IsParameter ](#ApiClient.VectorVariable.IsParameter)
  - [M IsRecorded ](#ApiClient.VectorVariable.IsRecorded)
  - [M IsReturn ](#ApiClient.VectorVariable.IsReturn)
  - [M SetDescription ](#ApiClient.VectorVariable.SetDescription)
  - [M SetDimension ](#ApiClient.VectorVariable.SetDimension)
  - [M SetInitialElementValue ](#ApiClient.VectorVariable.SetInitialElementValue)
  - [M SetInitialValue ](#ApiClient.VectorVariable.SetInitialValue)
  - [M SetParameter ](#ApiClient.VectorVariable.SetParameter)
  - [M SetRecorded ](#ApiClient.VectorVariable.SetRecorded)
  - [M SetReturn ](#ApiClient.VectorVariable.SetReturn)

# VectorVariable[¶](#vectorvariable "Link to this heading")

*class* VectorVariable[¶](#ApiClient.VectorVariable "Link to this definition")  
Returned by

- [`VariableApi.CreateVectorVariable`](../VariableApi.md#ApiClient.VariableApi.CreateVectorVariable "ApiClient.VariableApi.CreateVectorVariable (Python method) — Creates a new Vector variable.")

Clone()[¶](#ApiClient.VectorVariable.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`VectorVariable`](#ApiClient.VectorVariable "ApiClient.VectorVariable (Python class) — VariableApi.CreateVectorVariable")

DeleteInitialElementValue(*[x](#ApiClient.VectorVariable.DeleteInitialElementValue.x "ApiClient.VectorVariable.DeleteInitialElementValue.x (Python parameter) — Element position to delete.")*)[¶](#ApiClient.VectorVariable.DeleteInitialElementValue "Link to this definition")  
Deletes the expression defining an element’s value.

Parameters:  x : int[¶](#ApiClient.VectorVariable.DeleteInitialElementValue.x "Permalink to this definition")  
Element position to delete.

GetDescription()[¶](#ApiClient.VectorVariable.GetDescription "Link to this definition")  
Returns the description of the variable.

Returns:  Description of variable

Return type:  str

GetDimension()[¶](#ApiClient.VectorVariable.GetDimension "Link to this definition")  
Returns the length of the vector.

Returns:  Maximum number of elements.

Return type:  int

GetInitialElementValue(*[x](#ApiClient.VectorVariable.GetInitialElementValue.x "ApiClient.VectorVariable.GetInitialElementValue.x (Python parameter) — Element position to get.")*)[¶](#ApiClient.VectorVariable.GetInitialElementValue "Link to this definition")  
Returns the value expression at the index x of a vector.

Parameters:  x : int[¶](#ApiClient.VectorVariable.GetInitialElementValue.x "Permalink to this definition")  
Element position to get.

Returns:  Expression

Return type:  str

GetInitialValue()[¶](#ApiClient.VectorVariable.GetInitialValue "Link to this definition")  
Returns the initial value of the vector.

Returns:  The initial value of the vector as a list of string expressions.

Return type:  str

GetName()[¶](#ApiClient.VectorVariable.GetName "Link to this definition")  
Returns the name of the variable.

Returns:  Name of variable

Return type:  str

GetType()[¶](#ApiClient.VectorVariable.GetType "Link to this definition")  
Returns the type of the initial value of the variable.

Returns:  type of the initial value

Return type:  str

IsParameter()[¶](#ApiClient.VectorVariable.IsParameter "Link to this definition")  
Returns whether the variable is a parameter.

Returns:  True if parameter, else False

Return type:  boolean

IsRecorded()[¶](#ApiClient.VectorVariable.IsRecorded "Link to this definition")  
Returns whether the variable is recorded during execution.

Returns:  True if recorded, else False

Return type:  boolean

IsReturn()[¶](#ApiClient.VectorVariable.IsReturn "Link to this definition")  
Returns whether the variable is a return value.

Returns:  True if return value, else False

Return type:  boolean

SetDescription(*[description](#ApiClient.VectorVariable.SetDescription.description "ApiClient.VectorVariable.SetDescription.description (Python parameter) — Description of variable")*)[¶](#ApiClient.VectorVariable.SetDescription "Link to this definition")  
Sets the description of the variable.

Parameters:  description : str[¶](#ApiClient.VectorVariable.SetDescription.description "Permalink to this definition")  
Description of variable

SetDimension(*[dimension](#ApiClient.VectorVariable.SetDimension.dimension "ApiClient.VectorVariable.SetDimension.dimension (Python parameter) — The new dimension size.")*)[¶](#ApiClient.VectorVariable.SetDimension "Link to this definition")  
Sets a new dimension for the vector variable. If the new dimension is smaller than the pre-existing vector, then the right-most values will be cut off.

Parameters:  dimension : int[¶](#ApiClient.VectorVariable.SetDimension.dimension "Permalink to this definition")  
The new dimension size.

SetInitialElementValue(*[x](#ApiClient.VectorVariable.SetInitialElementValue.x "ApiClient.VectorVariable.SetInitialElementValue.x (Python parameter) — Element position to set.")*, *[value](#ApiClient.VectorVariable.SetInitialElementValue.value "ApiClient.VectorVariable.SetInitialElementValue.value (Python parameter) — Any Python expression as a string.")*)[¶](#ApiClient.VectorVariable.SetInitialElementValue "Link to this definition")  
Sets the value at a specific index.

Parameters:  x : int[¶](#ApiClient.VectorVariable.SetInitialElementValue.x "Permalink to this definition")  
Element position to set.

value : str[¶](#ApiClient.VectorVariable.SetInitialElementValue.value "Permalink to this definition")  
Any Python expression as a string.

SetInitialValue(*[value](#ApiClient.VectorVariable.SetInitialValue.value "ApiClient.VectorVariable.SetInitialValue.value (Python parameter) — Initial values of the vector in the form of a list of string expressions.")*)[¶](#ApiClient.VectorVariable.SetInitialValue "Link to this definition")  
Sets the initial values of the vector.

Parameters:  value : str[¶](#ApiClient.VectorVariable.SetInitialValue.value "Permalink to this definition")  
Initial values of the vector in the form of a list of string expressions.

SetParameter(*[enable](#ApiClient.VectorVariable.SetParameter.enable "ApiClient.VectorVariable.SetParameter.enable (Python parameter) — Whether the variable is a parameter or not")=`True`*)[¶](#ApiClient.VectorVariable.SetParameter "Link to this definition")  
Sets whether the variable is a parameter or not.

Parameters:  enable : boolean[¶](#ApiClient.VectorVariable.SetParameter.enable "Permalink to this definition")  
Whether the variable is a parameter or not

SetRecorded(*[enable](#ApiClient.VectorVariable.SetRecorded.enable "ApiClient.VectorVariable.SetRecorded.enable (Python parameter) — Whether to enable the recording of the variable")=`True`*)[¶](#ApiClient.VectorVariable.SetRecorded "Link to this definition")  
Sets the recording state of the variable to the value of enable.

Parameters:  enable : boolean[¶](#ApiClient.VectorVariable.SetRecorded.enable "Permalink to this definition")  
Whether to enable the recording of the variable

SetReturn(*[enable](#ApiClient.VectorVariable.SetReturn.enable "ApiClient.VectorVariable.SetReturn.enable (Python parameter) — Whether the variable is a return value or not")=`True`*)[¶](#ApiClient.VectorVariable.SetReturn "Link to this definition")  
Sets whether the variable is a return value or not.

Parameters:  enable : boolean[¶](#ApiClient.VectorVariable.SetReturn.enable "Permalink to this definition")  
Whether the variable is a return value or not

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
