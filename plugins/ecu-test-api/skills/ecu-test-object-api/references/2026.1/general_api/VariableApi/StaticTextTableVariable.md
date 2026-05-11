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

StaticTextTableVariable [ StaticTextTableVariable ](#)

StaticTextTableVariable

- [C StaticTextTableVariable ](#ApiClient.StaticTextTableVariable)
  - [M AddEntry ](#ApiClient.StaticTextTableVariable.AddEntry)
  - [M Clone ](#ApiClient.StaticTextTableVariable.Clone)
  - [M GetDescription ](#ApiClient.StaticTextTableVariable.GetDescription)
  - [M GetEntries ](#ApiClient.StaticTextTableVariable.GetEntries)
  - [M GetEntry ](#ApiClient.StaticTextTableVariable.GetEntry)
  - [M GetInitialValue ](#ApiClient.StaticTextTableVariable.GetInitialValue)
  - [M GetName ](#ApiClient.StaticTextTableVariable.GetName)
  - [M GetType ](#ApiClient.StaticTextTableVariable.GetType)
  - [M IsParameter ](#ApiClient.StaticTextTableVariable.IsParameter)
  - [M IsRecorded ](#ApiClient.StaticTextTableVariable.IsRecorded)
  - [M IsReturn ](#ApiClient.StaticTextTableVariable.IsReturn)
  - [M RemoveEntry ](#ApiClient.StaticTextTableVariable.RemoveEntry)
  - [M SetDescription ](#ApiClient.StaticTextTableVariable.SetDescription)
  - [M SetEntry ](#ApiClient.StaticTextTableVariable.SetEntry)
  - [M SetInitialValue ](#ApiClient.StaticTextTableVariable.SetInitialValue)
  - [M SetParameter ](#ApiClient.StaticTextTableVariable.SetParameter)
  - [M SetRecorded ](#ApiClient.StaticTextTableVariable.SetRecorded)
  - [M SetReturn ](#ApiClient.StaticTextTableVariable.SetReturn)

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

StaticTextTableVariable

- [C StaticTextTableVariable ](#ApiClient.StaticTextTableVariable)
  - [M AddEntry ](#ApiClient.StaticTextTableVariable.AddEntry)
  - [M Clone ](#ApiClient.StaticTextTableVariable.Clone)
  - [M GetDescription ](#ApiClient.StaticTextTableVariable.GetDescription)
  - [M GetEntries ](#ApiClient.StaticTextTableVariable.GetEntries)
  - [M GetEntry ](#ApiClient.StaticTextTableVariable.GetEntry)
  - [M GetInitialValue ](#ApiClient.StaticTextTableVariable.GetInitialValue)
  - [M GetName ](#ApiClient.StaticTextTableVariable.GetName)
  - [M GetType ](#ApiClient.StaticTextTableVariable.GetType)
  - [M IsParameter ](#ApiClient.StaticTextTableVariable.IsParameter)
  - [M IsRecorded ](#ApiClient.StaticTextTableVariable.IsRecorded)
  - [M IsReturn ](#ApiClient.StaticTextTableVariable.IsReturn)
  - [M RemoveEntry ](#ApiClient.StaticTextTableVariable.RemoveEntry)
  - [M SetDescription ](#ApiClient.StaticTextTableVariable.SetDescription)
  - [M SetEntry ](#ApiClient.StaticTextTableVariable.SetEntry)
  - [M SetInitialValue ](#ApiClient.StaticTextTableVariable.SetInitialValue)
  - [M SetParameter ](#ApiClient.StaticTextTableVariable.SetParameter)
  - [M SetRecorded ](#ApiClient.StaticTextTableVariable.SetRecorded)
  - [M SetReturn ](#ApiClient.StaticTextTableVariable.SetReturn)

# StaticTextTableVariable[¶](#statictexttablevariable "Link to this heading")

*class* StaticTextTableVariable[¶](#ApiClient.StaticTextTableVariable "Link to this definition")  
Returned by

- [`VariableApi.CreateStaticTextTableVariable`](../VariableApi.md#ApiClient.VariableApi.CreateStaticTextTableVariable "ApiClient.VariableApi.CreateStaticTextTableVariable (Python method) — Creates a new Texttable variable with static text entries.")

AddEntry(*[value](#ApiClient.StaticTextTableVariable.AddEntry.value "ApiClient.StaticTextTableVariable.AddEntry.value (Python parameter) — The new entry")*)[¶](#ApiClient.StaticTextTableVariable.AddEntry "Link to this definition")  
Adds an entry to the Texttable.

Parameters:  value : str[¶](#ApiClient.StaticTextTableVariable.AddEntry.value "Permalink to this definition")  
The new entry

Clone()[¶](#ApiClient.StaticTextTableVariable.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`StaticTextTableVariable`](#ApiClient.StaticTextTableVariable "ApiClient.StaticTextTableVariable (Python class) — VariableApi.CreateStaticTextTableVariable")

GetDescription()[¶](#ApiClient.StaticTextTableVariable.GetDescription "Link to this definition")  
Returns the description of the variable.

Returns:  Description of variable

Return type:  str

GetEntries()[¶](#ApiClient.StaticTextTableVariable.GetEntries "Link to this definition")  
Returns all entries of the Texttable.

Returns:  All Entries of the Texttable.

Return type:  list[str]

GetEntry(*[index](#ApiClient.StaticTextTableVariable.GetEntry.index "ApiClient.StaticTextTableVariable.GetEntry.index (Python parameter) — Index of the entry whose value is to be set")*)[¶](#ApiClient.StaticTextTableVariable.GetEntry "Link to this definition")  
Returns the value at a specific index of the Texttable.

Parameters:  index : int[¶](#ApiClient.StaticTextTableVariable.GetEntry.index "Permalink to this definition")  
Index of the entry whose value is to be set

Returns:  value at the given index

Return type:  str

GetInitialValue()[¶](#ApiClient.StaticTextTableVariable.GetInitialValue "Link to this definition")  
Returns the initial value of the Texttable.

Returns:  The initial value of the Texttable

Return type:  str

GetName()[¶](#ApiClient.StaticTextTableVariable.GetName "Link to this definition")  
Returns the name of the variable.

Returns:  Name of variable

Return type:  str

GetType()[¶](#ApiClient.StaticTextTableVariable.GetType "Link to this definition")  
Returns the type of the initial value of the variable.

Returns:  type of the initial value

Return type:  str

IsParameter()[¶](#ApiClient.StaticTextTableVariable.IsParameter "Link to this definition")  
Returns whether the variable is a parameter.

Returns:  True if parameter, else False

Return type:  boolean

IsRecorded()[¶](#ApiClient.StaticTextTableVariable.IsRecorded "Link to this definition")  
Returns whether the variable is recorded during execution.

Returns:  True if recorded, else False

Return type:  boolean

IsReturn()[¶](#ApiClient.StaticTextTableVariable.IsReturn "Link to this definition")  
Returns whether the variable is a return value.

Returns:  True if return value, else False

Return type:  boolean

RemoveEntry(*[index](#ApiClient.StaticTextTableVariable.RemoveEntry.index "ApiClient.StaticTextTableVariable.RemoveEntry.index (Python parameter) — Index of the entry to remove")*)[¶](#ApiClient.StaticTextTableVariable.RemoveEntry "Link to this definition")  
Removes an entry from the Texttable.

Parameters:  index : int[¶](#ApiClient.StaticTextTableVariable.RemoveEntry.index "Permalink to this definition")  
Index of the entry to remove

SetDescription(*[description](#ApiClient.StaticTextTableVariable.SetDescription.description "ApiClient.StaticTextTableVariable.SetDescription.description (Python parameter) — Description of variable")*)[¶](#ApiClient.StaticTextTableVariable.SetDescription "Link to this definition")  
Sets the description of the variable.

Parameters:  description : str[¶](#ApiClient.StaticTextTableVariable.SetDescription.description "Permalink to this definition")  
Description of variable

SetEntry(*[index](#ApiClient.StaticTextTableVariable.SetEntry.index "ApiClient.StaticTextTableVariable.SetEntry.index (Python parameter) — Index of the entry whose value is to be set")*, *[value](#ApiClient.StaticTextTableVariable.SetEntry.value "ApiClient.StaticTextTableVariable.SetEntry.value (Python parameter) — new value")*)[¶](#ApiClient.StaticTextTableVariable.SetEntry "Link to this definition")  
Sets the value at a specific index in the Texttable.

Parameters:  index : int[¶](#ApiClient.StaticTextTableVariable.SetEntry.index "Permalink to this definition")  
Index of the entry whose value is to be set

value : str[¶](#ApiClient.StaticTextTableVariable.SetEntry.value "Permalink to this definition")  
new value

SetInitialValue(*[value](#ApiClient.StaticTextTableVariable.SetInitialValue.value "ApiClient.StaticTextTableVariable.SetInitialValue.value (Python parameter) — The initial value of the Texttable.")*)[¶](#ApiClient.StaticTextTableVariable.SetInitialValue "Link to this definition")  
Sets the initial value of the Texttable.

Parameters:  value : str[¶](#ApiClient.StaticTextTableVariable.SetInitialValue.value "Permalink to this definition")  
The initial value of the Texttable.

SetParameter(*[enable](#ApiClient.StaticTextTableVariable.SetParameter.enable "ApiClient.StaticTextTableVariable.SetParameter.enable (Python parameter) — Whether the variable is a parameter or not")=`True`*)[¶](#ApiClient.StaticTextTableVariable.SetParameter "Link to this definition")  
Sets whether the variable is a parameter or not.

Parameters:  enable : boolean[¶](#ApiClient.StaticTextTableVariable.SetParameter.enable "Permalink to this definition")  
Whether the variable is a parameter or not

SetRecorded(*[enable](#ApiClient.StaticTextTableVariable.SetRecorded.enable "ApiClient.StaticTextTableVariable.SetRecorded.enable (Python parameter) — Whether to enable the recording of the variable")=`True`*)[¶](#ApiClient.StaticTextTableVariable.SetRecorded "Link to this definition")  
Sets the recording state of the variable to the value of enable.

Parameters:  enable : boolean[¶](#ApiClient.StaticTextTableVariable.SetRecorded.enable "Permalink to this definition")  
Whether to enable the recording of the variable

SetReturn(*[enable](#ApiClient.StaticTextTableVariable.SetReturn.enable "ApiClient.StaticTextTableVariable.SetReturn.enable (Python parameter) — Whether the variable is a return value or not")=`True`*)[¶](#ApiClient.StaticTextTableVariable.SetReturn "Link to this definition")  
Sets whether the variable is a return value or not.

Parameters:  enable : boolean[¶](#ApiClient.StaticTextTableVariable.SetReturn.enable "Permalink to this definition")  
Whether the variable is a return value or not

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
