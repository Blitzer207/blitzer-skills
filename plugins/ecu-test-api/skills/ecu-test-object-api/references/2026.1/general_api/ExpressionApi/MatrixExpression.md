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

MatrixExpression [ MatrixExpression ](#)

MatrixExpression

- [C MatrixExpression ](#ApiClient.MatrixExpression)
  - [M Clone ](#ApiClient.MatrixExpression.Clone)
  - [M GetDefaultValue ](#ApiClient.MatrixExpression.GetDefaultValue)
  - [M GetLines ](#ApiClient.MatrixExpression.GetLines)
  - [M GetValue ](#ApiClient.MatrixExpression.GetValue)
  - [M GetXDimension ](#ApiClient.MatrixExpression.GetXDimension)
  - [M GetYDimension ](#ApiClient.MatrixExpression.GetYDimension)
  - [M RemoveValue ](#ApiClient.MatrixExpression.RemoveValue)
  - [M SetDefaultValue ](#ApiClient.MatrixExpression.SetDefaultValue)
  - [M SetValue ](#ApiClient.MatrixExpression.SetValue)

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

MatrixExpression

- [C MatrixExpression ](#ApiClient.MatrixExpression)
  - [M Clone ](#ApiClient.MatrixExpression.Clone)
  - [M GetDefaultValue ](#ApiClient.MatrixExpression.GetDefaultValue)
  - [M GetLines ](#ApiClient.MatrixExpression.GetLines)
  - [M GetValue ](#ApiClient.MatrixExpression.GetValue)
  - [M GetXDimension ](#ApiClient.MatrixExpression.GetXDimension)
  - [M GetYDimension ](#ApiClient.MatrixExpression.GetYDimension)
  - [M RemoveValue ](#ApiClient.MatrixExpression.RemoveValue)
  - [M SetDefaultValue ](#ApiClient.MatrixExpression.SetDefaultValue)
  - [M SetValue ](#ApiClient.MatrixExpression.SetValue)

# MatrixExpression[¶](#matrixexpression "Link to this heading")

*class* MatrixExpression[¶](#ApiClient.MatrixExpression "Link to this definition")  
Returned by

- [`ExpressionApi.CreateMatrixExpression`](../ExpressionApi.md#ApiClient.ExpressionApi.CreateMatrixExpression "ApiClient.ExpressionApi.CreateMatrixExpression (Python method) — Creates a MatrixExpression")

Clone()[¶](#ApiClient.MatrixExpression.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`MatrixExpression`](#ApiClient.MatrixExpression "ApiClient.MatrixExpression (Python class) — ExpressionApi.CreateMatrixExpression")

GetDefaultValue()[¶](#ApiClient.MatrixExpression.GetDefaultValue "Link to this definition")  
Returns the default value which is used as a fallback if no explicit value for an element is defined.

Returns:  Expression used as default value

Return type:  str

GetLines()[¶](#ApiClient.MatrixExpression.GetLines "Link to this definition")  
Returns a list of values for all lines. Each line itself is also a list of all the values within the line. Values not explicitely set are represented by the default value.

Returns:  Sorted list containing all values

Return type:  list[list[str]]

GetValue(*[xIndex](#ApiClient.MatrixExpression.GetValue.xIndex "ApiClient.MatrixExpression.GetValue.xIndex (Python parameter) — Elements x position")*, *[yIndex](#ApiClient.MatrixExpression.GetValue.yIndex "ApiClient.MatrixExpression.GetValue.yIndex (Python parameter) — Elements y position")*)[¶](#ApiClient.MatrixExpression.GetValue "Link to this definition")  
Returns the expression defining an element’s value.

Parameters:  xIndex : int[¶](#ApiClient.MatrixExpression.GetValue.xIndex "Permalink to this definition")  
Elements x position

yIndex : int[¶](#ApiClient.MatrixExpression.GetValue.yIndex "Permalink to this definition")  
Elements y position

Returns:  Expression

Return type:  str

GetXDimension()[¶](#ApiClient.MatrixExpression.GetXDimension "Link to this definition")  
Returns the x dimension of the matrix.

Returns:  maximum number of elements in x dimension

Return type:  int

GetYDimension()[¶](#ApiClient.MatrixExpression.GetYDimension "Link to this definition")  
Returns the y dimension of the matrix.

Returns:  maximum number of elements in y dimension

Return type:  int

RemoveValue(*[xIndex](#ApiClient.MatrixExpression.RemoveValue.xIndex "ApiClient.MatrixExpression.RemoveValue.xIndex (Python parameter) — Elements x position")*, *[yIndex](#ApiClient.MatrixExpression.RemoveValue.yIndex "ApiClient.MatrixExpression.RemoveValue.yIndex (Python parameter) — Elements y position")*)[¶](#ApiClient.MatrixExpression.RemoveValue "Link to this definition")  
Removes the expression defining an element’s value.

Parameters:  xIndex : int[¶](#ApiClient.MatrixExpression.RemoveValue.xIndex "Permalink to this definition")  
Elements x position

yIndex : int[¶](#ApiClient.MatrixExpression.RemoveValue.yIndex "Permalink to this definition")  
Elements y position

SetDefaultValue(*[value](#ApiClient.MatrixExpression.SetDefaultValue.value "ApiClient.MatrixExpression.SetDefaultValue.value (Python parameter) — Expression to be used as default value")*)[¶](#ApiClient.MatrixExpression.SetDefaultValue "Link to this definition")  
Sets the default value which is used as a fallback if no explicit value for an element is defined.

Parameters:  value : str[¶](#ApiClient.MatrixExpression.SetDefaultValue.value "Permalink to this definition")  
Expression to be used as default value

SetValue(*[xIndex](#ApiClient.MatrixExpression.SetValue.xIndex "ApiClient.MatrixExpression.SetValue.xIndex (Python parameter) — Elements x position")*, *[yIndex](#ApiClient.MatrixExpression.SetValue.yIndex "ApiClient.MatrixExpression.SetValue.yIndex (Python parameter) — Elements y position")*, *[value](#ApiClient.MatrixExpression.SetValue.value "ApiClient.MatrixExpression.SetValue.value (Python parameter) — Expression")*)[¶](#ApiClient.MatrixExpression.SetValue "Link to this definition")  
Sets the expression defining an element’s value.

Parameters:  xIndex : int[¶](#ApiClient.MatrixExpression.SetValue.xIndex "Permalink to this definition")  
Elements x position

yIndex : int[¶](#ApiClient.MatrixExpression.SetValue.yIndex "Permalink to this definition")  
Elements y position

value : str[¶](#ApiClient.MatrixExpression.SetValue.value "Permalink to this definition")  
Expression

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
