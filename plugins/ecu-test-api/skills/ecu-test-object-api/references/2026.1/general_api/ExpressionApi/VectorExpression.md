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

API for Expressions

[ CurveExpression ](CurveExpression.md)

[ Expression ](Expression.md)

[ ExpressionValue ](ExpressionValue.md)

[ KeywordValueExpression ](KeywordValueExpression.md)

[ MapExpression ](MapExpression.md)

[ MatrixExpression ](MatrixExpression.md)

VectorExpression [ VectorExpression ](#)

VectorExpression

- [C VectorExpression ](#ApiClient.VectorExpression)
  - [M Clone ](#ApiClient.VectorExpression.Clone)
  - [M GetDefaultValue ](#ApiClient.VectorExpression.GetDefaultValue)
  - [M GetDimension ](#ApiClient.VectorExpression.GetDimension)
  - [M GetValue ](#ApiClient.VectorExpression.GetValue)
  - [M GetValues ](#ApiClient.VectorExpression.GetValues)
  - [M RemoveValue ](#ApiClient.VectorExpression.RemoveValue)
  - [M SetDefaultValue ](#ApiClient.VectorExpression.SetDefaultValue)
  - [M SetValue ](#ApiClient.VectorExpression.SetValue)

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

[ API for Workspaces ](../WorkspaceApi.md)

[ Trace Analysis API ](../../TraceAnalysisAPI/index.md)

[ Generator APIs ](../../generators/index.md)

[ Tools ](../../tools/index.md)

[ User test management ](../../userTestmanagement/index.md)

[ UserUtility API ](../../user-utility/user-utility.md)

[ Utility Examples ](../../user-utility/example-utilities.md)

VectorExpression

- [C VectorExpression ](#ApiClient.VectorExpression)
  - [M Clone ](#ApiClient.VectorExpression.Clone)
  - [M GetDefaultValue ](#ApiClient.VectorExpression.GetDefaultValue)
  - [M GetDimension ](#ApiClient.VectorExpression.GetDimension)
  - [M GetValue ](#ApiClient.VectorExpression.GetValue)
  - [M GetValues ](#ApiClient.VectorExpression.GetValues)
  - [M RemoveValue ](#ApiClient.VectorExpression.RemoveValue)
  - [M SetDefaultValue ](#ApiClient.VectorExpression.SetDefaultValue)
  - [M SetValue ](#ApiClient.VectorExpression.SetValue)

# VectorExpression[¶](#vectorexpression "Link to this heading")

*class* VectorExpression[¶](#ApiClient.VectorExpression "Link to this definition")  
Returned by

- [`ExpressionApi.CreateVectorExpression`](../ExpressionApi.md#ApiClient.ExpressionApi.CreateVectorExpression "ApiClient.ExpressionApi.CreateVectorExpression (Python method) — Creates a VectorExpression")

Clone()[¶](#ApiClient.VectorExpression.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`VectorExpression`](#ApiClient.VectorExpression "ApiClient.VectorExpression (Python class) — ExpressionApi.CreateVectorExpression")

GetDefaultValue()[¶](#ApiClient.VectorExpression.GetDefaultValue "Link to this definition")  
Returns the default value which is used as a fallback if no explicit value for an element is defined.

Returns:  Expression used as default value

Return type:  str

GetDimension()[¶](#ApiClient.VectorExpression.GetDimension "Link to this definition")  
Returns the length of the vector.

Returns:  maximum number of elements

Return type:  int

GetValue(*[index](#ApiClient.VectorExpression.GetValue.index "ApiClient.VectorExpression.GetValue.index (Python parameter) — Element position to get")*)[¶](#ApiClient.VectorExpression.GetValue "Link to this definition")  
Returns the expression defining an elements value.

Parameters:  index : int[¶](#ApiClient.VectorExpression.GetValue.index "Permalink to this definition")  
Element position to get

Returns:  Expression

Return type:  str

GetValues()[¶](#ApiClient.VectorExpression.GetValues "Link to this definition")  
Returns a list of all values. Values not explicitely set are represented by the default value.

Returns:  Sorted list containing all values

Return type:  list[str]

RemoveValue(*[index](#ApiClient.VectorExpression.RemoveValue.index "ApiClient.VectorExpression.RemoveValue.index (Python parameter) — Element position to remove")*)[¶](#ApiClient.VectorExpression.RemoveValue "Link to this definition")  
Removess the expression defining an elements value.

Parameters:  index : int[¶](#ApiClient.VectorExpression.RemoveValue.index "Permalink to this definition")  
Element position to remove

SetDefaultValue(*[value](#ApiClient.VectorExpression.SetDefaultValue.value "ApiClient.VectorExpression.SetDefaultValue.value (Python parameter) — Expression to be used as default value")*)[¶](#ApiClient.VectorExpression.SetDefaultValue "Link to this definition")  
Sets the default value which is used as a fallback if no explicit value for an element is defined.

Parameters:  value : str[¶](#ApiClient.VectorExpression.SetDefaultValue.value "Permalink to this definition")  
Expression to be used as default value

SetValue(*[index](#ApiClient.VectorExpression.SetValue.index "ApiClient.VectorExpression.SetValue.index (Python parameter) — Element position to set")*, *[value](#ApiClient.VectorExpression.SetValue.value "ApiClient.VectorExpression.SetValue.value (Python parameter) — Expression")*)[¶](#ApiClient.VectorExpression.SetValue "Link to this definition")  
Sets the expression defining an elements value.

Parameters:  index : int[¶](#ApiClient.VectorExpression.SetValue.index "Permalink to this definition")  
Element position to set

value : str[¶](#ApiClient.VectorExpression.SetValue.value "Permalink to this definition")  
Expression

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
