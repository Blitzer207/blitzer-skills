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

AllExpectation [ AllExpectation ](#)

AllExpectation

- [C AllExpectation ](#ApiClient.AllExpectation)
  - [M Clone ](#ApiClient.AllExpectation.Clone)
  - [M GetExpectation ](#ApiClient.AllExpectation.GetExpectation)
  - [M GetExpectationExpression ](#ApiClient.AllExpectation.GetExpectationExpression)
  - [M SetExpectation ](#ApiClient.AllExpectation.SetExpectation)
  - [M SetExpectationExpression ](#ApiClient.AllExpectation.SetExpectationExpression)

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

AllExpectation

- [C AllExpectation ](#ApiClient.AllExpectation)
  - [M Clone ](#ApiClient.AllExpectation.Clone)
  - [M GetExpectation ](#ApiClient.AllExpectation.GetExpectation)
  - [M GetExpectationExpression ](#ApiClient.AllExpectation.GetExpectationExpression)
  - [M SetExpectation ](#ApiClient.AllExpectation.SetExpectation)
  - [M SetExpectationExpression ](#ApiClient.AllExpectation.SetExpectationExpression)

# AllExpectation[¶](#allexpectation "Link to this heading")

*class* AllExpectation[¶](#ApiClient.AllExpectation "Link to this definition")  
Represents an expectation on all elements for complex data types. All sub elements of must fulfill the expectation for this expectation to be fulfilled.

The expectation is specified as a Boolean expression in Python syntax. The special identifier “value” refers to the actual value of each element.

Clone()[¶](#ApiClient.AllExpectation.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`AllExpectation`](#ApiClient.AllExpectation "ApiClient.AllExpectation (Python class) — Represents an expectation on all elements for complex data types. All sub elements of must fulfill the expectation for this expectation to be fulfilled.")

GetExpectation()[¶](#ApiClient.AllExpectation.GetExpectation "Link to this definition")  
Returns the expectation object.

Returns:  The expectation object

Return type:  [`Expectation`](Expectation.md#ApiClient.Expectation "ApiClient.Expectation (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")

GetExpectationExpression()[¶](#ApiClient.AllExpectation.GetExpectationExpression "Link to this definition")  
Returns the expectation expression.

Returns:  The expression

Return type:  str

SetExpectation(*[expectationObject](#ApiClient.AllExpectation.SetExpectation.expectationObject "ApiClient.AllExpectation.SetExpectation.expectationObject (Python parameter) — The expectation object")*)[¶](#ApiClient.AllExpectation.SetExpectation "Link to this definition")  
Sets the expectation object.

Parameters:  expectationObject[¶](#ApiClient.AllExpectation.SetExpectation.expectationObject "Permalink to this definition")  
The expectation object

SetExpectationExpression(*[expression](#ApiClient.AllExpectation.SetExpectationExpression.expression "ApiClient.AllExpectation.SetExpectationExpression.expression (Python parameter) — The expression")*)[¶](#ApiClient.AllExpectation.SetExpectationExpression "Link to this definition")  
Sets the expectation expression.

Parameters:  expression : str[¶](#ApiClient.AllExpectation.SetExpectationExpression.expression "Permalink to this definition")  
The expression

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
