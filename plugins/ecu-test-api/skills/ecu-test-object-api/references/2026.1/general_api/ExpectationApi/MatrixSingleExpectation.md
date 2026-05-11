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

API for Expectations

[ AllExpectation ](AllExpectation.md)

[ AudioExpectation ](AudioExpectation.md)

[ BinaryExpressionExpectation ](BinaryExpressionExpectation.md)

[ BitStreamExpectation ](BitStreamExpectation.md)

[ BitStreamExpressionExpectation ](BitStreamExpressionExpectation.md)

[ BooleanExpectation ](BooleanExpectation.md)

[ ByteStreamExpectation ](ByteStreamExpectation.md)

[ ByteStreamExpressionExpectation ](ByteStreamExpressionExpectation.md)

[ CurveAllExpectation ](CurveAllExpectation.md)

[ CurveSingleExpectation ](CurveSingleExpectation.md)

[ DTCListExpectation ](DTCListExpectation.md)

[ Expectation ](Expectation.md)

[ ExpressionExpectation ](ExpressionExpectation.md)

[ ExpressionExpectationBase ](ExpressionExpectationBase.md)

[ ImageExpectation ](ImageExpectation.md)

[ ManualExpression ](ManualExpression.md)

[ MapAllExpectation ](MapAllExpectation.md)

[ MapSingleExpectation ](MapSingleExpectation.md)

[ MatrixAllExpectation ](MatrixAllExpectation.md)

MatrixSingleExpectation [ MatrixSingleExpectation ](#)

MatrixSingleExpectation

- [C MatrixSingleExpectation ](#ApiClient.MatrixSingleExpectation)
  - [M Clone ](#ApiClient.MatrixSingleExpectation.Clone)
  - [M GetExpectation ](#ApiClient.MatrixSingleExpectation.GetExpectation)
  - [M GetExpectationExpression ](#ApiClient.MatrixSingleExpectation.GetExpectationExpression)
  - [M GetExpectationExpressionLines ](#ApiClient.MatrixSingleExpectation.GetExpectationExpressionLines)
  - [M GetXDimension ](#ApiClient.MatrixSingleExpectation.GetXDimension)
  - [M GetYDimension ](#ApiClient.MatrixSingleExpectation.GetYDimension)
  - [M RemoveExpectation ](#ApiClient.MatrixSingleExpectation.RemoveExpectation)
  - [M SetExpectation ](#ApiClient.MatrixSingleExpectation.SetExpectation)
  - [M SetExpectationExpression ](#ApiClient.MatrixSingleExpectation.SetExpectationExpression)

[ NotPresentExpectation ](NotPresentExpectation.md)

[ NumericExpectation ](NumericExpectation.md)

[ NumericExpressionExpectation ](NumericExpressionExpectation.md)

[ PresentExpectation ](PresentExpectation.md)

[ StringExpectation ](StringExpectation.md)

[ StringExpressionExpectation ](StringExpressionExpectation.md)

[ StringListExpectation ](StringListExpectation.md)

[ VectorAllExpectation ](VectorAllExpectation.md)

[ VectorSingleExpectation ](VectorSingleExpectation.md)

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

[ API for Workspaces ](../WorkspaceApi.md)

[ Trace Analysis API ](../../TraceAnalysisAPI/index.md)

[ Generator APIs ](../../generators/index.md)

[ Tools ](../../tools/index.md)

[ User test management ](../../userTestmanagement/index.md)

[ UserUtility API ](../../user-utility/user-utility.md)

[ Utility Examples ](../../user-utility/example-utilities.md)

MatrixSingleExpectation

- [C MatrixSingleExpectation ](#ApiClient.MatrixSingleExpectation)
  - [M Clone ](#ApiClient.MatrixSingleExpectation.Clone)
  - [M GetExpectation ](#ApiClient.MatrixSingleExpectation.GetExpectation)
  - [M GetExpectationExpression ](#ApiClient.MatrixSingleExpectation.GetExpectationExpression)
  - [M GetExpectationExpressionLines ](#ApiClient.MatrixSingleExpectation.GetExpectationExpressionLines)
  - [M GetXDimension ](#ApiClient.MatrixSingleExpectation.GetXDimension)
  - [M GetYDimension ](#ApiClient.MatrixSingleExpectation.GetYDimension)
  - [M RemoveExpectation ](#ApiClient.MatrixSingleExpectation.RemoveExpectation)
  - [M SetExpectation ](#ApiClient.MatrixSingleExpectation.SetExpectation)
  - [M SetExpectationExpression ](#ApiClient.MatrixSingleExpectation.SetExpectationExpression)

# MatrixSingleExpectation[¶](#matrixsingleexpectation "Link to this heading")

*class* MatrixSingleExpectation[¶](#ApiClient.MatrixSingleExpectation "Link to this definition")  
Represents a sparse matrix of expectations. Each element of the matrix represents an individual expectation on the respective value. All individual expectations must be fulfilled in order for the this matrix expectation to be fulfilled.

Each individual expectation is specified as a Boolean expression in Python syntax. The special identifier “value” refers to the actual value of the matrix element.

Returned by

- [`ExpectationApi.CreateMatrixSingleExpectation`](../ExpectationApi.md#ApiClient.ExpectationApi.CreateMatrixSingleExpectation "ApiClient.ExpectationApi.CreateMatrixSingleExpectation (Python method) — Creates a matrix expectation.")

Clone()[¶](#ApiClient.MatrixSingleExpectation.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`MatrixSingleExpectation`](#ApiClient.MatrixSingleExpectation "ApiClient.MatrixSingleExpectation (Python class) — Represents a sparse matrix of expectations. Each element of the matrix represents an individual expectation on the respective value. All individual expectations must be fulfilled in order for the this matrix expectation to be fulfilled.")

GetExpectation(*[xIndex](#ApiClient.MatrixSingleExpectation.GetExpectation.xIndex "ApiClient.MatrixSingleExpectation.GetExpectation.xIndex (Python parameter) — X-Index of the expectation object.")*, *[yIndex](#ApiClient.MatrixSingleExpectation.GetExpectation.yIndex "ApiClient.MatrixSingleExpectation.GetExpectation.yIndex (Python parameter) — Y-Index of the expectation object.")*)[¶](#ApiClient.MatrixSingleExpectation.GetExpectation "Link to this definition")  
Returns the expectation object.

Parameters:  xIndex : int[¶](#ApiClient.MatrixSingleExpectation.GetExpectation.xIndex "Permalink to this definition")  
X-Index of the expectation object.

yIndex : int[¶](#ApiClient.MatrixSingleExpectation.GetExpectation.yIndex "Permalink to this definition")  
Y-Index of the expectation object.

Returns:  The expectation object

Return type:  [`Expectation`](Expectation.md#ApiClient.Expectation "ApiClient.Expectation (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")

GetExpectationExpression(*[xIndex](#ApiClient.MatrixSingleExpectation.GetExpectationExpression.xIndex "ApiClient.MatrixSingleExpectation.GetExpectationExpression.xIndex (Python parameter) — X-Index of the expression.")*, *[yIndex](#ApiClient.MatrixSingleExpectation.GetExpectationExpression.yIndex "ApiClient.MatrixSingleExpectation.GetExpectationExpression.yIndex (Python parameter) — Y-Index of the expression.")*)[¶](#ApiClient.MatrixSingleExpectation.GetExpectationExpression "Link to this definition")  
Returns the expectations expression.

Parameters:  xIndex : int[¶](#ApiClient.MatrixSingleExpectation.GetExpectationExpression.xIndex "Permalink to this definition")  
X-Index of the expression.

yIndex : int[¶](#ApiClient.MatrixSingleExpectation.GetExpectationExpression.yIndex "Permalink to this definition")  
Y-Index of the expression.

Returns:  The expression

Return type:  str

GetExpectationExpressionLines()[¶](#ApiClient.MatrixSingleExpectation.GetExpectationExpressionLines "Link to this definition")  
Returns a list of expectation expressions for all lines. Each line itself is also a list of all the expressions within the line. Elements without expectation are represented by None.

Returns:  Sorted list containing all expressions

Return type:  list[list[str]]

GetXDimension()[¶](#ApiClient.MatrixSingleExpectation.GetXDimension "Link to this definition")  
Returns the x dimension. :return: The x dimension. :rtype: int

GetYDimension()[¶](#ApiClient.MatrixSingleExpectation.GetYDimension "Link to this definition")  
Returns the y dimension. :return: The y dimension. :rtype: int

RemoveExpectation(*[xIndex](#ApiClient.MatrixSingleExpectation.RemoveExpectation.xIndex "ApiClient.MatrixSingleExpectation.RemoveExpectation.xIndex (Python parameter) — X-Index of the expression to remove.")*, *[yIndex](#ApiClient.MatrixSingleExpectation.RemoveExpectation.yIndex "ApiClient.MatrixSingleExpectation.RemoveExpectation.yIndex (Python parameter) — Y-Index of the expression to remove.")*)[¶](#ApiClient.MatrixSingleExpectation.RemoveExpectation "Link to this definition")  
Removes an expectation expression

Parameters:  xIndex : int[¶](#ApiClient.MatrixSingleExpectation.RemoveExpectation.xIndex "Permalink to this definition")  
X-Index of the expression to remove.

yIndex : int[¶](#ApiClient.MatrixSingleExpectation.RemoveExpectation.yIndex "Permalink to this definition")  
Y-Index of the expression to remove.

SetExpectation(*[xIndex](#ApiClient.MatrixSingleExpectation.SetExpectation.xIndex "ApiClient.MatrixSingleExpectation.SetExpectation.xIndex (Python parameter) — X-Index of the expectation object.")*, *[yIndex](#ApiClient.MatrixSingleExpectation.SetExpectation.yIndex "ApiClient.MatrixSingleExpectation.SetExpectation.yIndex (Python parameter) — Y-Index of the expectation object.")*, *[expectationObject](#ApiClient.MatrixSingleExpectation.SetExpectation.expectationObject "ApiClient.MatrixSingleExpectation.SetExpectation.expectationObject (Python parameter) — The expectation object")*)[¶](#ApiClient.MatrixSingleExpectation.SetExpectation "Link to this definition")  
Sets the expectation object.

Parameters:  xIndex : int[¶](#ApiClient.MatrixSingleExpectation.SetExpectation.xIndex "Permalink to this definition")  
X-Index of the expectation object.

yIndex : int[¶](#ApiClient.MatrixSingleExpectation.SetExpectation.yIndex "Permalink to this definition")  
Y-Index of the expectation object.

expectationObject[¶](#ApiClient.MatrixSingleExpectation.SetExpectation.expectationObject "Permalink to this definition")  
The expectation object

SetExpectationExpression(*[xIndex](#ApiClient.MatrixSingleExpectation.SetExpectationExpression.xIndex "ApiClient.MatrixSingleExpectation.SetExpectationExpression.xIndex (Python parameter) — X-Index of the expression.")*, *[yIndex](#ApiClient.MatrixSingleExpectation.SetExpectationExpression.yIndex "ApiClient.MatrixSingleExpectation.SetExpectationExpression.yIndex (Python parameter) — Y-Index of the expression.")*, *[expression](#ApiClient.MatrixSingleExpectation.SetExpectationExpression.expression "ApiClient.MatrixSingleExpectation.SetExpectationExpression.expression (Python parameter) — The expression")*)[¶](#ApiClient.MatrixSingleExpectation.SetExpectationExpression "Link to this definition")  
Sets the expectations expression.

Parameters:  xIndex : int[¶](#ApiClient.MatrixSingleExpectation.SetExpectationExpression.xIndex "Permalink to this definition")  
X-Index of the expression.

yIndex : int[¶](#ApiClient.MatrixSingleExpectation.SetExpectationExpression.yIndex "Permalink to this definition")  
Y-Index of the expression.

expression : str[¶](#ApiClient.MatrixSingleExpectation.SetExpectationExpression.expression "Permalink to this definition")  
The expression

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
