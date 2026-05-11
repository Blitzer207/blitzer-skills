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

[ MatrixSingleExpectation ](MatrixSingleExpectation.md)

[ NotPresentExpectation ](NotPresentExpectation.md)

[ NumericExpectation ](NumericExpectation.md)

[ NumericExpressionExpectation ](NumericExpressionExpectation.md)

[ PresentExpectation ](PresentExpectation.md)

[ StringExpectation ](StringExpectation.md)

[ StringExpressionExpectation ](StringExpressionExpectation.md)

[ StringListExpectation ](StringListExpectation.md)

[ VectorAllExpectation ](VectorAllExpectation.md)

VectorSingleExpectation [ VectorSingleExpectation ](#)

VectorSingleExpectation

- [C VectorSingleExpectation ](#ApiClient.VectorSingleExpectation)
  - [M Clone ](#ApiClient.VectorSingleExpectation.Clone)
  - [M GetDimension ](#ApiClient.VectorSingleExpectation.GetDimension)
  - [M GetExpectation ](#ApiClient.VectorSingleExpectation.GetExpectation)
  - [M GetExpectationExpression ](#ApiClient.VectorSingleExpectation.GetExpectationExpression)
  - [M GetExpectationExpressions ](#ApiClient.VectorSingleExpectation.GetExpectationExpressions)
  - [M RemoveExpectation ](#ApiClient.VectorSingleExpectation.RemoveExpectation)
  - [M SetExpectation ](#ApiClient.VectorSingleExpectation.SetExpectation)
  - [M SetExpectationExpression ](#ApiClient.VectorSingleExpectation.SetExpectationExpression)

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

VectorSingleExpectation

- [C VectorSingleExpectation ](#ApiClient.VectorSingleExpectation)
  - [M Clone ](#ApiClient.VectorSingleExpectation.Clone)
  - [M GetDimension ](#ApiClient.VectorSingleExpectation.GetDimension)
  - [M GetExpectation ](#ApiClient.VectorSingleExpectation.GetExpectation)
  - [M GetExpectationExpression ](#ApiClient.VectorSingleExpectation.GetExpectationExpression)
  - [M GetExpectationExpressions ](#ApiClient.VectorSingleExpectation.GetExpectationExpressions)
  - [M RemoveExpectation ](#ApiClient.VectorSingleExpectation.RemoveExpectation)
  - [M SetExpectation ](#ApiClient.VectorSingleExpectation.SetExpectation)
  - [M SetExpectationExpression ](#ApiClient.VectorSingleExpectation.SetExpectationExpression)

# VectorSingleExpectation[¶](#vectorsingleexpectation "Link to this heading")

*class* VectorSingleExpectation[¶](#ApiClient.VectorSingleExpectation "Link to this definition")  
Represents a sparse vector of expectations. Each element of the vector represents an individual expectation on the respective value. All individual expectations must be fulfilled in order for the this vector expectation to be fulfilled.

Each individual expectation is specified as a Boolean expression in Python syntax. The special identifier “value” refers to the actual value of the vector element.

Returned by

- [`ExpectationApi.CreateVectorSingleExpectation`](../ExpectationApi.md#ApiClient.ExpectationApi.CreateVectorSingleExpectation "ApiClient.ExpectationApi.CreateVectorSingleExpectation (Python method) — Creates a vector expectation.")

Clone()[¶](#ApiClient.VectorSingleExpectation.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`VectorSingleExpectation`](#ApiClient.VectorSingleExpectation "ApiClient.VectorSingleExpectation (Python class) — Represents a sparse vector of expectations. Each element of the vector represents an individual expectation on the respective value. All individual expectations must be fulfilled in order for the this vector expectation to be fulfilled.")

GetDimension()[¶](#ApiClient.VectorSingleExpectation.GetDimension "Link to this definition")  
Returns the dimension of the element.

Returns:  Dimension of the element.

Return type:  int

GetExpectation(*[index](#ApiClient.VectorSingleExpectation.GetExpectation.index "ApiClient.VectorSingleExpectation.GetExpectation.index (Python parameter) — Index of the expectation object.")*)[¶](#ApiClient.VectorSingleExpectation.GetExpectation "Link to this definition")  
Returns the expectation object for the specified element.

Parameters:  index : int[¶](#ApiClient.VectorSingleExpectation.GetExpectation.index "Permalink to this definition")  
Index of the expectation object.

Returns:  The expectation object

Return type:  [`Expectation`](Expectation.md#ApiClient.Expectation "ApiClient.Expectation (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")

GetExpectationExpression(*[index](#ApiClient.VectorSingleExpectation.GetExpectationExpression.index "ApiClient.VectorSingleExpectation.GetExpectationExpression.index (Python parameter) — Index of the expression.")*)[¶](#ApiClient.VectorSingleExpectation.GetExpectationExpression "Link to this definition")  
Returns the expectation expression for the specified element.

Parameters:  index : int[¶](#ApiClient.VectorSingleExpectation.GetExpectationExpression.index "Permalink to this definition")  
Index of the expression.

Returns:  The expression

Return type:  str

GetExpectationExpressions()[¶](#ApiClient.VectorSingleExpectation.GetExpectationExpressions "Link to this definition")  
Returns a list of all expectation expression. Elements without expectation are represented by None

Returns:  Sorted list containing all expectation expressions

Return type:  list[str]

RemoveExpectation(*[index](#ApiClient.VectorSingleExpectation.RemoveExpectation.index "ApiClient.VectorSingleExpectation.RemoveExpectation.index (Python parameter) — Index of the expression to remove.")*)[¶](#ApiClient.VectorSingleExpectation.RemoveExpectation "Link to this definition")  
Removes the expectation expression for the specified element.

Parameters:  index : int[¶](#ApiClient.VectorSingleExpectation.RemoveExpectation.index "Permalink to this definition")  
Index of the expression to remove.

SetExpectation(*[index](#ApiClient.VectorSingleExpectation.SetExpectation.index "ApiClient.VectorSingleExpectation.SetExpectation.index (Python parameter) — Index of the expectation object.")*, *[expectationObject](#ApiClient.VectorSingleExpectation.SetExpectation.expectationObject "ApiClient.VectorSingleExpectation.SetExpectation.expectationObject (Python parameter) — The expectation object")*)[¶](#ApiClient.VectorSingleExpectation.SetExpectation "Link to this definition")  
Sets the expectation object for the specified element.

Parameters:  index : int[¶](#ApiClient.VectorSingleExpectation.SetExpectation.index "Permalink to this definition")  
Index of the expectation object.

expectationObject[¶](#ApiClient.VectorSingleExpectation.SetExpectation.expectationObject "Permalink to this definition")  
The expectation object

SetExpectationExpression(*[index](#ApiClient.VectorSingleExpectation.SetExpectationExpression.index "ApiClient.VectorSingleExpectation.SetExpectationExpression.index (Python parameter) — Index of the expression.")*, *[expression](#ApiClient.VectorSingleExpectation.SetExpectationExpression.expression "ApiClient.VectorSingleExpectation.SetExpectationExpression.expression (Python parameter) — The expression")*)[¶](#ApiClient.VectorSingleExpectation.SetExpectationExpression "Link to this definition")  
Sets the expectation expression for the specified element.

Parameters:  index : int[¶](#ApiClient.VectorSingleExpectation.SetExpectationExpression.index "Permalink to this definition")  
Index of the expression.

expression : str[¶](#ApiClient.VectorSingleExpectation.SetExpectationExpression.expression "Permalink to this definition")  
The expression

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
