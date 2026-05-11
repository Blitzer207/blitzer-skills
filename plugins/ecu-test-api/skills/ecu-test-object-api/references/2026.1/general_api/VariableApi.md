[ Internal APIs ](api.md)

[ Advanced operations of package variable types ](variabledatastructures.md)

[ Advanced properties of bus-related objects ](busdatastructures.md)

[ Bus related objects of trace analysis ](busdatastructuresTraceanalysis.md)

[ Advanced properties of diagnostics-related objects ](diagdatastructures.md)

[ Diagnostics related objects of trace analysis ](diagdatastructuresTraceanalysis.md)

[ Advanced properties of media-related objects ](mediadatastructures.md)

[ Advanced properties of DLT logging-related objects ](dltdatastructures.md)

[ COM API ](com-api.md)

[ REST API ](rest-api.md)

[ Report API ](apireport.md)

[ Object API ](objectApi.md)

Object API

[ API entry points ](objectApi.md#api-entry-points)

API entry points

[ API for Analysis Jobs ](AnalysisJobApi.md)

[ API for Artifacts ](ArtifactApi.md)

[ API for Project Components ](ComponentApi.md)

[ API for Configurations ](ConfigurationApi.md)

[ API for Expectations ](ExpectationApi.md)

[ API for Expressions ](ExpressionApi.md)

[ API for Global Mappings ](GlobalMappingApi.md)

[ API for Mappings ](MappingApi.md)

[ API for Multimedia Objects ](MultimediaApi.md)

[ API for Packages ](PackageApi.md)

[ API for Parameters ](ParameterApi.md)

[ API for Projects ](ProjectApi.md)

[ API for Relations ](RelationApi.md)

[ API for Reports ](ReportApi.md)

[ API for Report Filters ](ReportFilterApi.md)

[ API for Settings ](SettingsApi.md)

[ API for Signals ](SignalApi.md)

[ API for Signal Descriptions ](SignalDescriptionApi.md)

[ API for Signal Recordings ](SignalRecordingApi.md)

[ API for Symbols ](SymbolApi.md)

[ API for Test Steps ](TestStepApi.md)

[ API for Touch Inputs ](TouchInputApi.md)

[ API for Trace Analyses ](TraceAnalysisApi.md)

[ API for Trace Files ](TraceFileApi.md)

[ API for Trace Step Templates ](TraceStepTemplateApi.md)

[ API for Variables ](#)

API for Variables

- [ BooleanVariable ](VariableApi/BooleanVariable.md)
- [ DynamicEnumVariable ](VariableApi/DynamicEnumVariable.md)
- [ DynamicTextTableVariable ](VariableApi/DynamicTextTableVariable.md)
- [ EnumVariable ](VariableApi/EnumVariable.md)
- [ EnumVariableElement ](VariableApi/EnumVariableElement.md)
- [ FunctionVariable ](VariableApi/FunctionVariable.md)
- [ NumericVariable ](VariableApi/NumericVariable.md)
- [ PyObjectVariable ](VariableApi/PyObjectVariable.md)
- [ StaticTextTableVariable ](VariableApi/StaticTextTableVariable.md)
- [ StringVariable ](VariableApi/StringVariable.md)
- [ StructureVariable ](VariableApi/StructureVariable.md)
- [ Variable ](VariableApi/Variable.md)
- [ VectorVariable ](VariableApi/VectorVariable.md)

API for Variables [ API for Variables ](#)

API for Variables

- [C VariableApi ](#ApiClient.VariableApi)
  - [M CreateBooleanVariable ](#ApiClient.VariableApi.CreateBooleanVariable)
  - [M CreateDynamicEnumVariable ](#ApiClient.VariableApi.CreateDynamicEnumVariable)
  - [M CreateDynamicTextTableVariable ](#ApiClient.VariableApi.CreateDynamicTextTableVariable)
  - [M CreateEnumVariable ](#ApiClient.VariableApi.CreateEnumVariable)
  - [M CreateFunctionVariable ](#ApiClient.VariableApi.CreateFunctionVariable)
  - [M CreateNumericVariable ](#ApiClient.VariableApi.CreateNumericVariable)
  - [M CreatePyObjectVariable ](#ApiClient.VariableApi.CreatePyObjectVariable)
  - [M CreateStaticTextTableVariable ](#ApiClient.VariableApi.CreateStaticTextTableVariable)
  - [M CreateStringVariable ](#ApiClient.VariableApi.CreateStringVariable)
  - [M CreateStructureVariable ](#ApiClient.VariableApi.CreateStructureVariable)
  - [M CreateVariable ](#ApiClient.VariableApi.CreateVariable)
  - [M CreateVectorVariable ](#ApiClient.VariableApi.CreateVectorVariable)
- [ BooleanVariable ](VariableApi/BooleanVariable.md)
- [ DynamicEnumVariable ](VariableApi/DynamicEnumVariable.md)
- [ DynamicTextTableVariable ](VariableApi/DynamicTextTableVariable.md)
- [ EnumVariable ](VariableApi/EnumVariable.md)
- [ EnumVariableElement ](VariableApi/EnumVariableElement.md)
- [ FunctionVariable ](VariableApi/FunctionVariable.md)
- [ NumericVariable ](VariableApi/NumericVariable.md)
- [ PyObjectVariable ](VariableApi/PyObjectVariable.md)
- [ StaticTextTableVariable ](VariableApi/StaticTextTableVariable.md)
- [ StringVariable ](VariableApi/StringVariable.md)
- [ StructureVariable ](VariableApi/StructureVariable.md)
- [ Variable ](VariableApi/Variable.md)
- [ VectorVariable ](VariableApi/VectorVariable.md)

[ API for Workspaces ](WorkspaceApi.md)

[ Trace Analysis API ](../TraceAnalysisAPI/index.md)

[ Generator APIs ](../generators/index.md)

[ Tools ](../tools/index.md)

[ User test management ](../userTestmanagement/index.md)

[ UserUtility API ](../user-utility/user-utility.md)

[ Utility Examples ](../user-utility/example-utilities.md)

API for Variables

- [C VariableApi ](#ApiClient.VariableApi)
  - [M CreateBooleanVariable ](#ApiClient.VariableApi.CreateBooleanVariable)
  - [M CreateDynamicEnumVariable ](#ApiClient.VariableApi.CreateDynamicEnumVariable)
  - [M CreateDynamicTextTableVariable ](#ApiClient.VariableApi.CreateDynamicTextTableVariable)
  - [M CreateEnumVariable ](#ApiClient.VariableApi.CreateEnumVariable)
  - [M CreateFunctionVariable ](#ApiClient.VariableApi.CreateFunctionVariable)
  - [M CreateNumericVariable ](#ApiClient.VariableApi.CreateNumericVariable)
  - [M CreatePyObjectVariable ](#ApiClient.VariableApi.CreatePyObjectVariable)
  - [M CreateStaticTextTableVariable ](#ApiClient.VariableApi.CreateStaticTextTableVariable)
  - [M CreateStringVariable ](#ApiClient.VariableApi.CreateStringVariable)
  - [M CreateStructureVariable ](#ApiClient.VariableApi.CreateStructureVariable)
  - [M CreateVariable ](#ApiClient.VariableApi.CreateVariable)
  - [M CreateVectorVariable ](#ApiClient.VariableApi.CreateVectorVariable)

# API for Variables[¶](#api-for-variables "Link to this heading")

Part of the [Object based program API](objectApi.md#objectapi).

*class* VariableApi[¶](#ApiClient.VariableApi "Link to this definition")  
Returned by

- [`PackageApi.VariableApi`](PackageApi.md#ApiClient.PackageApi.VariableApi "ApiClient.PackageApi.VariableApi (Python attribute) — Returns the VariableApi namespace.")

CreateBooleanVariable(*[name](#ApiClient.VariableApi.CreateBooleanVariable.name "ApiClient.VariableApi.CreateBooleanVariable.name (Python parameter) — Variable name")*)[¶](#ApiClient.VariableApi.CreateBooleanVariable "Link to this definition")  
Creates a new boolean variable.

Parameters:  name : str[¶](#ApiClient.VariableApi.CreateBooleanVariable.name "Permalink to this definition")  
Variable name

Returns:  New boolean variable

Return type:  [`BooleanVariable`](VariableApi/BooleanVariable.md#ApiClient.BooleanVariable "ApiClient.BooleanVariable (Python class) — VariableApi.CreateBooleanVariable")

CreateDynamicEnumVariable(*[name](#ApiClient.VariableApi.CreateDynamicEnumVariable.name "ApiClient.VariableApi.CreateDynamicEnumVariable.name (Python parameter) — Variable name")*)[¶](#ApiClient.VariableApi.CreateDynamicEnumVariable "Link to this definition")  
Creates a new Enum variable with dynamic entries.

Parameters:  name : str[¶](#ApiClient.VariableApi.CreateDynamicEnumVariable.name "Permalink to this definition")  
Variable name

Returns:  New dynamic enum variable

Return type:  [`DynamicEnumVariable`](VariableApi/DynamicEnumVariable.md#ApiClient.DynamicEnumVariable "ApiClient.DynamicEnumVariable (Python class) — VariableApi.CreateDynamicEnumVariable")

CreateDynamicTextTableVariable(*[name](#ApiClient.VariableApi.CreateDynamicTextTableVariable.name "ApiClient.VariableApi.CreateDynamicTextTableVariable.name (Python parameter) — Variable name")*)[¶](#ApiClient.VariableApi.CreateDynamicTextTableVariable "Link to this definition")  
Creates a new Texttable variable with dynamic text entries.

Parameters:  name : str[¶](#ApiClient.VariableApi.CreateDynamicTextTableVariable.name "Permalink to this definition")  
Variable name

Returns:  New Texttable variable

Return type:  [`DynamicTextTableVariable`](VariableApi/DynamicTextTableVariable.md#ApiClient.DynamicTextTableVariable "ApiClient.DynamicTextTableVariable (Python class) — VariableApi.CreateDynamicTextTableVariable")

CreateEnumVariable(*[name](#ApiClient.VariableApi.CreateEnumVariable.name "ApiClient.VariableApi.CreateEnumVariable.name (Python parameter) — Variable name")*)[¶](#ApiClient.VariableApi.CreateEnumVariable "Link to this definition")  
Creates a new Enum variable.

Parameters:  name : str[¶](#ApiClient.VariableApi.CreateEnumVariable.name "Permalink to this definition")  
Variable name

Returns:  New Enum variable

Return type:  [`EnumVariable`](VariableApi/EnumVariable.md#ApiClient.EnumVariable "ApiClient.EnumVariable (Python class) — VariableApi.CreateEnumVariable")

CreateFunctionVariable(*[name](#ApiClient.VariableApi.CreateFunctionVariable.name "ApiClient.VariableApi.CreateFunctionVariable.name (Python parameter) — Variable name")*)[¶](#ApiClient.VariableApi.CreateFunctionVariable "Link to this definition")  
Creates a new function variable.

Parameters:  name : str[¶](#ApiClient.VariableApi.CreateFunctionVariable.name "Permalink to this definition")  
Variable name

Returns:  New function variable

Return type:  [`FunctionVariable`](VariableApi/FunctionVariable.md#ApiClient.FunctionVariable "ApiClient.FunctionVariable (Python class) — VariableApi.CreateFunctionVariable")

CreateNumericVariable(*[name](#ApiClient.VariableApi.CreateNumericVariable.name "ApiClient.VariableApi.CreateNumericVariable.name (Python parameter) — Variable name")*)[¶](#ApiClient.VariableApi.CreateNumericVariable "Link to this definition")  
Creates a new numeric variable.

Parameters:  name : str[¶](#ApiClient.VariableApi.CreateNumericVariable.name "Permalink to this definition")  
Variable name

Returns:  New numeric variable

Return type:  [`NumericVariable`](VariableApi/NumericVariable.md#ApiClient.NumericVariable "ApiClient.NumericVariable (Python class) — VariableApi.CreateNumericVariable")

CreatePyObjectVariable(*[name](#ApiClient.VariableApi.CreatePyObjectVariable.name "ApiClient.VariableApi.CreatePyObjectVariable.name (Python parameter) — Variable name")*)[¶](#ApiClient.VariableApi.CreatePyObjectVariable "Link to this definition")  
Creates a new PyObject variable.

Parameters:  name : str[¶](#ApiClient.VariableApi.CreatePyObjectVariable.name "Permalink to this definition")  
Variable name

Returns:  New PyObject variable

Return type:  [`PyObjectVariable`](VariableApi/PyObjectVariable.md#ApiClient.PyObjectVariable "ApiClient.PyObjectVariable (Python class) — VariableApi.CreatePyObjectVariable")

CreateStaticTextTableVariable(*[name](#ApiClient.VariableApi.CreateStaticTextTableVariable.name "ApiClient.VariableApi.CreateStaticTextTableVariable.name (Python parameter) — Variable name")*)[¶](#ApiClient.VariableApi.CreateStaticTextTableVariable "Link to this definition")  
Creates a new Texttable variable with static text entries.

Parameters:  name : str[¶](#ApiClient.VariableApi.CreateStaticTextTableVariable.name "Permalink to this definition")  
Variable name

Returns:  New Texttable variable

Return type:  [`StaticTextTableVariable`](VariableApi/StaticTextTableVariable.md#ApiClient.StaticTextTableVariable "ApiClient.StaticTextTableVariable (Python class) — VariableApi.CreateStaticTextTableVariable")

CreateStringVariable(*[name](#ApiClient.VariableApi.CreateStringVariable.name "ApiClient.VariableApi.CreateStringVariable.name (Python parameter) — Variable name")*)[¶](#ApiClient.VariableApi.CreateStringVariable "Link to this definition")  
Creates a new string variable.

Parameters:  name : str[¶](#ApiClient.VariableApi.CreateStringVariable.name "Permalink to this definition")  
Variable name

Returns:  New string variable

Return type:  [`StringVariable`](VariableApi/StringVariable.md#ApiClient.StringVariable "ApiClient.StringVariable (Python class) — VariableApi.CreateStringVariable")

CreateStructureVariable(*[name](#ApiClient.VariableApi.CreateStructureVariable.name "ApiClient.VariableApi.CreateStructureVariable.name (Python parameter) — Variable name")*)[¶](#ApiClient.VariableApi.CreateStructureVariable "Link to this definition")  
Creates a new Structure variable.

Parameters:  name : str[¶](#ApiClient.VariableApi.CreateStructureVariable.name "Permalink to this definition")  
Variable name

Returns:  New Structure variable

Return type:  [`StructureVariable`](VariableApi/StructureVariable.md#ApiClient.StructureVariable "ApiClient.StructureVariable (Python class) — VariableApi.CreateStructureVariable")

CreateVariable(*[name](#ApiClient.VariableApi.CreateVariable.name "ApiClient.VariableApi.CreateVariable.name (Python parameter) — Variable name")*)[¶](#ApiClient.VariableApi.CreateVariable "Link to this definition")  
Creates a new \<Undefined\> variable.

Parameters:  name : str[¶](#ApiClient.VariableApi.CreateVariable.name "Permalink to this definition")  
Variable name

Returns:  New variable

Return type:  [`Variable`](VariableApi/Variable.md#ApiClient.Variable "ApiClient.Variable (Python class) — VariableApi.CreateVariable")

CreateVectorVariable(*[name](#ApiClient.VariableApi.CreateVectorVariable.name "ApiClient.VariableApi.CreateVectorVariable.name (Python parameter) — Variable name")*, *[length](#ApiClient.VariableApi.CreateVectorVariable.length "ApiClient.VariableApi.CreateVectorVariable.length (Python parameter) — The maximum length of the Vector")=`1`*)[¶](#ApiClient.VariableApi.CreateVectorVariable "Link to this definition")  
Creates a new Vector variable.

Parameters:  name : str[¶](#ApiClient.VariableApi.CreateVectorVariable.name "Permalink to this definition")  
Variable name

length : int[¶](#ApiClient.VariableApi.CreateVectorVariable.length "Permalink to this definition")  
The maximum length of the Vector

Returns:  A new Vector variable

Return type:  [`VectorVariable`](VariableApi/VectorVariable.md#ApiClient.VectorVariable "ApiClient.VectorVariable (Python class) — VariableApi.CreateVectorVariable")

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
