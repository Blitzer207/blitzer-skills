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

StringExpectation [ StringExpectation ](#)

StringExpectation

- [C StringExpectation ](#ApiClient.StringExpectation)
  - [M Clone ](#ApiClient.StringExpectation.Clone)
  - [M GetCaseSensitive ](#ApiClient.StringExpectation.GetCaseSensitive)
  - [M GetDontEvalNotPresent ](#ApiClient.StringExpectation.GetDontEvalNotPresent)
  - [M GetExpression ](#ApiClient.StringExpectation.GetExpression)
  - [M GetExpressionObject ](#ApiClient.StringExpectation.GetExpressionObject)
  - [M GetExpressionType ](#ApiClient.StringExpectation.GetExpressionType)
  - [M SetCaseSensitive ](#ApiClient.StringExpectation.SetCaseSensitive)
  - [M SetDontEvalNotPresent ](#ApiClient.StringExpectation.SetDontEvalNotPresent)
  - [M SetExpression ](#ApiClient.StringExpectation.SetExpression)
  - [M SetExpressionObject ](#ApiClient.StringExpectation.SetExpressionObject)
  - [M SetExpressionType ](#ApiClient.StringExpectation.SetExpressionType)

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

StringExpectation

- [C StringExpectation ](#ApiClient.StringExpectation)
  - [M Clone ](#ApiClient.StringExpectation.Clone)
  - [M GetCaseSensitive ](#ApiClient.StringExpectation.GetCaseSensitive)
  - [M GetDontEvalNotPresent ](#ApiClient.StringExpectation.GetDontEvalNotPresent)
  - [M GetExpression ](#ApiClient.StringExpectation.GetExpression)
  - [M GetExpressionObject ](#ApiClient.StringExpectation.GetExpressionObject)
  - [M GetExpressionType ](#ApiClient.StringExpectation.GetExpressionType)
  - [M SetCaseSensitive ](#ApiClient.StringExpectation.SetCaseSensitive)
  - [M SetDontEvalNotPresent ](#ApiClient.StringExpectation.SetDontEvalNotPresent)
  - [M SetExpression ](#ApiClient.StringExpectation.SetExpression)
  - [M SetExpressionObject ](#ApiClient.StringExpectation.SetExpressionObject)
  - [M SetExpressionType ](#ApiClient.StringExpectation.SetExpressionType)

# StringExpectation[¶](#stringexpectation "Link to this heading")

*class* StringExpectation[¶](#ApiClient.StringExpectation "Link to this definition")  
Returned by

- [`ExpectationApi.CreateStringExpectation`](../ExpectationApi.md#ApiClient.ExpectationApi.CreateStringExpectation "ApiClient.ExpectationApi.CreateStringExpectation (Python method) — Creates a string expectation.")

Clone()[¶](#ApiClient.StringExpectation.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`StringExpectation`](#ApiClient.StringExpectation "ApiClient.StringExpectation (Python class) — ExpectationApi.CreateStringExpectation")

GetCaseSensitive()[¶](#ApiClient.StringExpectation.GetCaseSensitive "Link to this definition")  
Returns whether the comparison should be case-sensitive.

Returns:  True if case-sensitive, else False.

Return type:  boolean

GetDontEvalNotPresent()[¶](#ApiClient.StringExpectation.GetDontEvalNotPresent "Link to this definition")  
Returns whether the option to evaluate this expectation if the expected value is NotPresent is set or not.

Returns:  True if the described behavior is enabled otherwise False.

Return type:  boolean

GetExpression()[¶](#ApiClient.StringExpectation.GetExpression "Link to this definition")  
Returns the expectations expression.

Returns:  The expression

Return type:  str

GetExpressionObject()[¶](#ApiClient.StringExpectation.GetExpressionObject "Link to this definition")  
Returns the expectations expression. Currently only KeywordValueExpression are supported!

Returns:  The expression

Return type:  [`KeywordValueExpression`](../ExpressionApi/KeywordValueExpression.md#ApiClient.KeywordValueExpression "ApiClient.KeywordValueExpression (Python class) — ExpressionApi.CreateKeywordValueExpression")

GetExpressionType()[¶](#ApiClient.StringExpectation.GetExpressionType "Link to this definition")  
Returns how the actual value and the expression value will be compared.

Returns:  The expression type

Return type:  str

SetCaseSensitive(*[caseSensitive](#ApiClient.StringExpectation.SetCaseSensitive.caseSensitive "ApiClient.StringExpectation.SetCaseSensitive.caseSensitive (Python parameter) — True if case-sensitive, else False.")*)[¶](#ApiClient.StringExpectation.SetCaseSensitive "Link to this definition")  
Sets whether the comparison should be case-sensitive.

Parameters:  caseSensitive : boolean[¶](#ApiClient.StringExpectation.SetCaseSensitive.caseSensitive "Permalink to this definition")  
True if case-sensitive, else False.

SetDontEvalNotPresent(*[dontEvalNotPresent](#ApiClient.StringExpectation.SetDontEvalNotPresent.dontEvalNotPresent "ApiClient.StringExpectation.SetDontEvalNotPresent.dontEvalNotPresent (Python parameter) — True to enable the described behavior.")*)[¶](#ApiClient.StringExpectation.SetDontEvalNotPresent "Link to this definition")  
Enables or disables the option to evaluate this expectation if the expected value is NotPresent.

Parameters:  dontEvalNotPresent : boolean[¶](#ApiClient.StringExpectation.SetDontEvalNotPresent.dontEvalNotPresent "Permalink to this definition")  
True to enable the described behavior. False to disable it.

SetExpression(*[expression](#ApiClient.StringExpectation.SetExpression.expression "ApiClient.StringExpectation.SetExpression.expression (Python parameter) — The expression")*)[¶](#ApiClient.StringExpectation.SetExpression "Link to this definition")  
Sets the expectations expression.

Parameters:  expression : str[¶](#ApiClient.StringExpectation.SetExpression.expression "Permalink to this definition")  
The expression

SetExpressionObject(*[expression](#ApiClient.StringExpectation.SetExpressionObject.expression "ApiClient.StringExpectation.SetExpressionObject.expression (Python parameter) — The KeywordValue expression")*)[¶](#ApiClient.StringExpectation.SetExpressionObject "Link to this definition")  
Sets the expectations expression. Currently only KeywordValueExpression are supported!

Parameters:  expression[¶](#ApiClient.StringExpectation.SetExpressionObject.expression "Permalink to this definition")  
The KeywordValue expression

SetExpressionType(*[expressionType](#ApiClient.StringExpectation.SetExpressionType.expressionType "ApiClient.StringExpectation.SetExpressionType.expressionType (Python parameter) — The expression type.")*)[¶](#ApiClient.StringExpectation.SetExpressionType "Link to this definition")  
Sets how the actual value and the expression value will be compared.

Parameters:  expressionType : str[¶](#ApiClient.StringExpectation.SetExpressionType.expressionType "Permalink to this definition")  
The expression type. Possible values: - ‘identical’ (default) - ‘starts with’ - ‘ends with’ - ‘contains’ - ‘constains not’ - ‘dissimilar’

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
