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

BooleanExpectation [ BooleanExpectation ](#)

BooleanExpectation

- [C BooleanExpectation ](#ApiClient.BooleanExpectation)
  - [M Clone ](#ApiClient.BooleanExpectation.Clone)
  - [M GetExpression ](#ApiClient.BooleanExpectation.GetExpression)
  - [M GetValue ](#ApiClient.BooleanExpectation.GetValue)
  - [M SetExpression ](#ApiClient.BooleanExpectation.SetExpression)
  - [M SetValue ](#ApiClient.BooleanExpectation.SetValue)

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

BooleanExpectation

- [C BooleanExpectation ](#ApiClient.BooleanExpectation)
  - [M Clone ](#ApiClient.BooleanExpectation.Clone)
  - [M GetExpression ](#ApiClient.BooleanExpectation.GetExpression)
  - [M GetValue ](#ApiClient.BooleanExpectation.GetValue)
  - [M SetExpression ](#ApiClient.BooleanExpectation.SetExpression)
  - [M SetValue ](#ApiClient.BooleanExpectation.SetValue)

# BooleanExpectation[¶](#booleanexpectation "Link to this heading")

*class* BooleanExpectation[¶](#ApiClient.BooleanExpectation "Link to this definition")  
Returned by

- [`ExpectationApi.CreateBooleanExpectation`](../ExpectationApi.md#ApiClient.ExpectationApi.CreateBooleanExpectation "ApiClient.ExpectationApi.CreateBooleanExpectation (Python method) — Creates a boolean expectation.")

Clone()[¶](#ApiClient.BooleanExpectation.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`BooleanExpectation`](#ApiClient.BooleanExpectation "ApiClient.BooleanExpectation (Python class) — ExpectationApi.CreateBooleanExpectation")

GetExpression()[¶](#ApiClient.BooleanExpectation.GetExpression "Link to this definition")  
Returns the expectations expression.

Returns:  The expression

Return type:  str

GetValue()[¶](#ApiClient.BooleanExpectation.GetValue "Link to this definition")  
Returns the truth value.

Returns:  The truth value

Return type:  boolean

SetExpression(*[expression](#ApiClient.BooleanExpectation.SetExpression.expression "ApiClient.BooleanExpectation.SetExpression.expression (Python parameter) — The expression")*)[¶](#ApiClient.BooleanExpectation.SetExpression "Link to this definition")  
Sets the expectations expression. Allowed expressions: ‘value’ for boolean True and ‘not value’ for boolean False.

Parameters:  expression : str[¶](#ApiClient.BooleanExpectation.SetExpression.expression "Permalink to this definition")  
The expression

SetValue(*[truthValue](#ApiClient.BooleanExpectation.SetValue.truthValue "ApiClient.BooleanExpectation.SetValue.truthValue (Python parameter) — The new truth value")*)[¶](#ApiClient.BooleanExpectation.SetValue "Link to this definition")  
Sets the truth value.

Parameters:  truthValue : boolean[¶](#ApiClient.BooleanExpectation.SetValue.truthValue "Permalink to this definition")  
The new truth value

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
