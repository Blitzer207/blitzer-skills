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

EnumVariable [ EnumVariable ](#)

EnumVariable

- [C EnumVariable ](#ApiClient.EnumVariable)
  - [M AddEntry ](#ApiClient.EnumVariable.AddEntry)
  - [M Clone ](#ApiClient.EnumVariable.Clone)
  - [M GetDescription ](#ApiClient.EnumVariable.GetDescription)
  - [M GetEntries ](#ApiClient.EnumVariable.GetEntries)
  - [M GetInitialText ](#ApiClient.EnumVariable.GetInitialText)
  - [M GetInitialValue ](#ApiClient.EnumVariable.GetInitialValue)
  - [M GetName ](#ApiClient.EnumVariable.GetName)
  - [M GetType ](#ApiClient.EnumVariable.GetType)
  - [M IsParameter ](#ApiClient.EnumVariable.IsParameter)
  - [M IsRecorded ](#ApiClient.EnumVariable.IsRecorded)
  - [M IsReturn ](#ApiClient.EnumVariable.IsReturn)
  - [M RemoveEntry ](#ApiClient.EnumVariable.RemoveEntry)
  - [M SetDescription ](#ApiClient.EnumVariable.SetDescription)
  - [M SetInitialValue ](#ApiClient.EnumVariable.SetInitialValue)
  - [M SetParameter ](#ApiClient.EnumVariable.SetParameter)
  - [M SetRecorded ](#ApiClient.EnumVariable.SetRecorded)
  - [M SetReturn ](#ApiClient.EnumVariable.SetReturn)

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

EnumVariable

- [C EnumVariable ](#ApiClient.EnumVariable)
  - [M AddEntry ](#ApiClient.EnumVariable.AddEntry)
  - [M Clone ](#ApiClient.EnumVariable.Clone)
  - [M GetDescription ](#ApiClient.EnumVariable.GetDescription)
  - [M GetEntries ](#ApiClient.EnumVariable.GetEntries)
  - [M GetInitialText ](#ApiClient.EnumVariable.GetInitialText)
  - [M GetInitialValue ](#ApiClient.EnumVariable.GetInitialValue)
  - [M GetName ](#ApiClient.EnumVariable.GetName)
  - [M GetType ](#ApiClient.EnumVariable.GetType)
  - [M IsParameter ](#ApiClient.EnumVariable.IsParameter)
  - [M IsRecorded ](#ApiClient.EnumVariable.IsRecorded)
  - [M IsReturn ](#ApiClient.EnumVariable.IsReturn)
  - [M RemoveEntry ](#ApiClient.EnumVariable.RemoveEntry)
  - [M SetDescription ](#ApiClient.EnumVariable.SetDescription)
  - [M SetInitialValue ](#ApiClient.EnumVariable.SetInitialValue)
  - [M SetParameter ](#ApiClient.EnumVariable.SetParameter)
  - [M SetRecorded ](#ApiClient.EnumVariable.SetRecorded)
  - [M SetReturn ](#ApiClient.EnumVariable.SetReturn)

# EnumVariable[¶](#enumvariable "Link to this heading")

*class* EnumVariable[¶](#ApiClient.EnumVariable "Link to this definition")  
Returned by

- [`VariableApi.CreateEnumVariable`](../VariableApi.md#ApiClient.VariableApi.CreateEnumVariable "ApiClient.VariableApi.CreateEnumVariable (Python method) — Creates a new Enum variable.")

AddEntry(*[value](#ApiClient.EnumVariable.AddEntry.value "ApiClient.EnumVariable.AddEntry.value (Python parameter) — The value of the entry")*, *[text](#ApiClient.EnumVariable.AddEntry.text "ApiClient.EnumVariable.AddEntry.text (Python parameter) — The text of the entry")*)[¶](#ApiClient.EnumVariable.AddEntry "Link to this definition")  
Adds an entry to the Enum initial entries. Raises an exception if the value is already contained in the enum.

Parameters:  value : int[¶](#ApiClient.EnumVariable.AddEntry.value "Permalink to this definition")  
The value of the entry

text : str[¶](#ApiClient.EnumVariable.AddEntry.text "Permalink to this definition")  
The text of the entry

Returns:  The created enum

Return type:  [`EnumVariableElement`](EnumVariableElement.md#ApiClient.EnumVariableElement "ApiClient.EnumVariableElement (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")

Clone()[¶](#ApiClient.EnumVariable.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`EnumVariable`](#ApiClient.EnumVariable "ApiClient.EnumVariable (Python class) — VariableApi.CreateEnumVariable")

GetDescription()[¶](#ApiClient.EnumVariable.GetDescription "Link to this definition")  
Returns the description of the variable.

Returns:  Description of variable

Return type:  str

GetEntries()[¶](#ApiClient.EnumVariable.GetEntries "Link to this definition")  
Returns the initial value of the variable or an empty list if it is not an Enum.

Returns:  Initial value of the variable

Return type:  list[[`EnumVariableElement`](EnumVariableElement.md#ApiClient.EnumVariableElement "ApiClient.EnumVariableElement (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")]

GetInitialText()[¶](#ApiClient.EnumVariable.GetInitialText "Link to this definition")  
Returns the initial text of the variable.

Returns:  The initial text of the variable

Return type:  str

GetInitialValue()[¶](#ApiClient.EnumVariable.GetInitialValue "Link to this definition")  
Returns the initial value of the enum.

Returns:  The initial value of the enum

Return type:  int

GetName()[¶](#ApiClient.EnumVariable.GetName "Link to this definition")  
Returns the name of the variable.

Returns:  Name of variable

Return type:  str

GetType()[¶](#ApiClient.EnumVariable.GetType "Link to this definition")  
Returns the type of the initial value of the variable.

Returns:  type of the initial value

Return type:  str

IsParameter()[¶](#ApiClient.EnumVariable.IsParameter "Link to this definition")  
Returns whether the variable is a parameter.

Returns:  True if parameter, else False

Return type:  boolean

IsRecorded()[¶](#ApiClient.EnumVariable.IsRecorded "Link to this definition")  
Returns whether the variable is recorded during execution.

Returns:  True if recorded, else False

Return type:  boolean

IsReturn()[¶](#ApiClient.EnumVariable.IsReturn "Link to this definition")  
Returns whether the variable is a return value.

Returns:  True if return value, else False

Return type:  boolean

RemoveEntry(*[value](#ApiClient.EnumVariable.RemoveEntry.value "ApiClient.EnumVariable.RemoveEntry.value (Python parameter) — The value of the entry")*)[¶](#ApiClient.EnumVariable.RemoveEntry "Link to this definition")  
Deletes an entry from the enum.

Parameters:  value : int[¶](#ApiClient.EnumVariable.RemoveEntry.value "Permalink to this definition")  
The value of the entry

SetDescription(*[description](#ApiClient.EnumVariable.SetDescription.description "ApiClient.EnumVariable.SetDescription.description (Python parameter) — Description of variable")*)[¶](#ApiClient.EnumVariable.SetDescription "Link to this definition")  
Sets the description of the variable.

Parameters:  description : str[¶](#ApiClient.EnumVariable.SetDescription.description "Permalink to this definition")  
Description of variable

SetInitialValue(*[value](#ApiClient.EnumVariable.SetInitialValue.value "ApiClient.EnumVariable.SetInitialValue.value (Python parameter) — The number that should initially be used as the current value.")*)[¶](#ApiClient.EnumVariable.SetInitialValue "Link to this definition")  
Selects the initial value of the enum. The entry needs to be added by using AddEntry before.

Parameters:  value : int[¶](#ApiClient.EnumVariable.SetInitialValue.value "Permalink to this definition")  
The number that should initially be used as the current value.

SetParameter(*[enable](#ApiClient.EnumVariable.SetParameter.enable "ApiClient.EnumVariable.SetParameter.enable (Python parameter) — Whether the variable is a parameter or not")=`True`*)[¶](#ApiClient.EnumVariable.SetParameter "Link to this definition")  
Sets whether the variable is a parameter or not.

Parameters:  enable : boolean[¶](#ApiClient.EnumVariable.SetParameter.enable "Permalink to this definition")  
Whether the variable is a parameter or not

SetRecorded(*[enable](#ApiClient.EnumVariable.SetRecorded.enable "ApiClient.EnumVariable.SetRecorded.enable (Python parameter) — Whether to enable the recording of the variable")=`True`*)[¶](#ApiClient.EnumVariable.SetRecorded "Link to this definition")  
Sets the recording state of the variable to the value of enable.

Parameters:  enable : boolean[¶](#ApiClient.EnumVariable.SetRecorded.enable "Permalink to this definition")  
Whether to enable the recording of the variable

SetReturn(*[enable](#ApiClient.EnumVariable.SetReturn.enable "ApiClient.EnumVariable.SetReturn.enable (Python parameter) — Whether the variable is a return value or not")=`True`*)[¶](#ApiClient.EnumVariable.SetReturn "Link to this definition")  
Sets whether the variable is a return value or not.

Parameters:  enable : boolean[¶](#ApiClient.EnumVariable.SetReturn.enable "Permalink to this definition")  
Whether the variable is a return value or not

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
