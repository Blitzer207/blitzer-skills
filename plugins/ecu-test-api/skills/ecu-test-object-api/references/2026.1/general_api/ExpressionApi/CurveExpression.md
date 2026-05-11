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

CurveExpression [ CurveExpression ](#)

CurveExpression

- [C CurveExpression ](#ApiClient.CurveExpression)
  - [M Clone ](#ApiClient.CurveExpression.Clone)
  - [M GetDefaultValue ](#ApiClient.CurveExpression.GetDefaultValue)
  - [M GetDimension ](#ApiClient.CurveExpression.GetDimension)
  - [M GetDistributionDefaultValue ](#ApiClient.CurveExpression.GetDistributionDefaultValue)
  - [M GetDistributionValue ](#ApiClient.CurveExpression.GetDistributionValue)
  - [M GetDistributionValues ](#ApiClient.CurveExpression.GetDistributionValues)
  - [M GetValue ](#ApiClient.CurveExpression.GetValue)
  - [M GetValues ](#ApiClient.CurveExpression.GetValues)
  - [M RemoveDistributionValue ](#ApiClient.CurveExpression.RemoveDistributionValue)
  - [M RemoveValue ](#ApiClient.CurveExpression.RemoveValue)
  - [M SetDefaultValue ](#ApiClient.CurveExpression.SetDefaultValue)
  - [M SetDistributionDefaultValue ](#ApiClient.CurveExpression.SetDistributionDefaultValue)
  - [M SetDistributionValue ](#ApiClient.CurveExpression.SetDistributionValue)
  - [M SetValue ](#ApiClient.CurveExpression.SetValue)

[ Expression ](Expression.md)

[ ExpressionValue ](ExpressionValue.md)

[ KeywordValueExpression ](KeywordValueExpression.md)

[ MapExpression ](MapExpression.md)

[ MatrixExpression ](MatrixExpression.md)

[ VectorExpression ](VectorExpression.md)

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

CurveExpression

- [C CurveExpression ](#ApiClient.CurveExpression)
  - [M Clone ](#ApiClient.CurveExpression.Clone)
  - [M GetDefaultValue ](#ApiClient.CurveExpression.GetDefaultValue)
  - [M GetDimension ](#ApiClient.CurveExpression.GetDimension)
  - [M GetDistributionDefaultValue ](#ApiClient.CurveExpression.GetDistributionDefaultValue)
  - [M GetDistributionValue ](#ApiClient.CurveExpression.GetDistributionValue)
  - [M GetDistributionValues ](#ApiClient.CurveExpression.GetDistributionValues)
  - [M GetValue ](#ApiClient.CurveExpression.GetValue)
  - [M GetValues ](#ApiClient.CurveExpression.GetValues)
  - [M RemoveDistributionValue ](#ApiClient.CurveExpression.RemoveDistributionValue)
  - [M RemoveValue ](#ApiClient.CurveExpression.RemoveValue)
  - [M SetDefaultValue ](#ApiClient.CurveExpression.SetDefaultValue)
  - [M SetDistributionDefaultValue ](#ApiClient.CurveExpression.SetDistributionDefaultValue)
  - [M SetDistributionValue ](#ApiClient.CurveExpression.SetDistributionValue)
  - [M SetValue ](#ApiClient.CurveExpression.SetValue)

# CurveExpression[¶](#curveexpression "Link to this heading")

*class* CurveExpression[¶](#ApiClient.CurveExpression "Link to this definition")  
Returned by

- [`ExpressionApi.CreateCurveExpression`](../ExpressionApi.md#ApiClient.ExpressionApi.CreateCurveExpression "ApiClient.ExpressionApi.CreateCurveExpression (Python method) — Creates a CurveExpression")

Clone()[¶](#ApiClient.CurveExpression.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`CurveExpression`](#ApiClient.CurveExpression "ApiClient.CurveExpression (Python class) — ExpressionApi.CreateCurveExpression")

GetDefaultValue()[¶](#ApiClient.CurveExpression.GetDefaultValue "Link to this definition")  
Returns the default value which is used as a fallback if no explicit value for an element is defined.

Returns:  Expression used as default value

Return type:  str

GetDimension()[¶](#ApiClient.CurveExpression.GetDimension "Link to this definition")  
Returns the length of the vector.

Returns:  maximum number of elements

Return type:  int

GetDistributionDefaultValue()[¶](#ApiClient.CurveExpression.GetDistributionDefaultValue "Link to this definition")  
Returns the default value which is used as a fallback if no explicit value for a distribution element is defined.

Returns:  Expression to be used as default value for distribution

Return type:  str

GetDistributionValue(*[index](#ApiClient.CurveExpression.GetDistributionValue.index "ApiClient.CurveExpression.GetDistributionValue.index (Python parameter) — Element position to return")*)[¶](#ApiClient.CurveExpression.GetDistributionValue "Link to this definition")  
Gets the distribution level of the given position.

Parameters:  index : int[¶](#ApiClient.CurveExpression.GetDistributionValue.index "Permalink to this definition")  
Element position to return

Returns:  distribution value

Return type:  str

GetDistributionValues()[¶](#ApiClient.CurveExpression.GetDistributionValues "Link to this definition")  
Returns a list of all distribution values. Values not explicitely set are represented by the default value.

Returns:  Sorted list containing all distribution values

Return type:  list[str]

GetValue(*[index](#ApiClient.CurveExpression.GetValue.index "ApiClient.CurveExpression.GetValue.index (Python parameter) — Element position to get")*)[¶](#ApiClient.CurveExpression.GetValue "Link to this definition")  
Returns the expression defining an elements value.

Parameters:  index : int[¶](#ApiClient.CurveExpression.GetValue.index "Permalink to this definition")  
Element position to get

Returns:  Expression

Return type:  str

GetValues()[¶](#ApiClient.CurveExpression.GetValues "Link to this definition")  
Returns a list of all values. Values not explicitely set are represented by the default value.

Returns:  Sorted list containing all values

Return type:  list[str]

RemoveDistributionValue(*[index](#ApiClient.CurveExpression.RemoveDistributionValue.index "ApiClient.CurveExpression.RemoveDistributionValue.index (Python parameter) — Element position to remove")*)[¶](#ApiClient.CurveExpression.RemoveDistributionValue "Link to this definition")  
Removess the distribution value of the given index.

Parameters:  index : int[¶](#ApiClient.CurveExpression.RemoveDistributionValue.index "Permalink to this definition")  
Element position to remove

RemoveValue(*[index](#ApiClient.CurveExpression.RemoveValue.index "ApiClient.CurveExpression.RemoveValue.index (Python parameter) — Element position to remove")*)[¶](#ApiClient.CurveExpression.RemoveValue "Link to this definition")  
Removess the expression defining an elements value.

Parameters:  index : int[¶](#ApiClient.CurveExpression.RemoveValue.index "Permalink to this definition")  
Element position to remove

SetDefaultValue(*[value](#ApiClient.CurveExpression.SetDefaultValue.value "ApiClient.CurveExpression.SetDefaultValue.value (Python parameter) — Expression to be used as default value")*)[¶](#ApiClient.CurveExpression.SetDefaultValue "Link to this definition")  
Sets the default value which is used as a fallback if no explicit value for an element is defined.

Parameters:  value : str[¶](#ApiClient.CurveExpression.SetDefaultValue.value "Permalink to this definition")  
Expression to be used as default value

SetDistributionDefaultValue(*[value](#ApiClient.CurveExpression.SetDistributionDefaultValue.value "ApiClient.CurveExpression.SetDistributionDefaultValue.value (Python parameter) — Expression to be used as default value for distribution")*)[¶](#ApiClient.CurveExpression.SetDistributionDefaultValue "Link to this definition")  
Sets the default value which is used as a fallback if no explicit value for a distribution element is defined.

Parameters:  value : str[¶](#ApiClient.CurveExpression.SetDistributionDefaultValue.value "Permalink to this definition")  
Expression to be used as default value for distribution

SetDistributionValue(*[index](#ApiClient.CurveExpression.SetDistributionValue.index "ApiClient.CurveExpression.SetDistributionValue.index (Python parameter) — Element position to set")*, *[value](#ApiClient.CurveExpression.SetDistributionValue.value "ApiClient.CurveExpression.SetDistributionValue.value (Python parameter) — Expression")*)[¶](#ApiClient.CurveExpression.SetDistributionValue "Link to this definition")  
Sets the distribution value of the given position.

Parameters:  index : int[¶](#ApiClient.CurveExpression.SetDistributionValue.index "Permalink to this definition")  
Element position to set

value : str[¶](#ApiClient.CurveExpression.SetDistributionValue.value "Permalink to this definition")  
Expression

SetValue(*[index](#ApiClient.CurveExpression.SetValue.index "ApiClient.CurveExpression.SetValue.index (Python parameter) — Element position to set")*, *[value](#ApiClient.CurveExpression.SetValue.value "ApiClient.CurveExpression.SetValue.value (Python parameter) — Expression")*)[¶](#ApiClient.CurveExpression.SetValue "Link to this definition")  
Sets the expression defining an elements value.

Parameters:  index : int[¶](#ApiClient.CurveExpression.SetValue.index "Permalink to this definition")  
Element position to set

value : str[¶](#ApiClient.CurveExpression.SetValue.value "Permalink to this definition")  
Expression

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
