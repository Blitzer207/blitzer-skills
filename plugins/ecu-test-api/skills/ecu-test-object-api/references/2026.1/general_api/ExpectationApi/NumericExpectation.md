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

NumericExpectation [ NumericExpectation ](#)

NumericExpectation

- [C NumericExpectation ](#ApiClient.NumericExpectation)
  - [M Clone ](#ApiClient.NumericExpectation.Clone)
  - [M DeactivateTolerance ](#ApiClient.NumericExpectation.DeactivateTolerance)
  - [M GetDontEvalNotPresent ](#ApiClient.NumericExpectation.GetDontEvalNotPresent)
  - [M GetExpression ](#ApiClient.NumericExpectation.GetExpression)
  - [M GetRelation ](#ApiClient.NumericExpectation.GetRelation)
  - [M GetToleranceType ](#ApiClient.NumericExpectation.GetToleranceType)
  - [M GetToleranceValue ](#ApiClient.NumericExpectation.GetToleranceValue)
  - [M SetDontEvalNotPresent ](#ApiClient.NumericExpectation.SetDontEvalNotPresent)
  - [M SetExpression ](#ApiClient.NumericExpectation.SetExpression)
  - [M SetRelation ](#ApiClient.NumericExpectation.SetRelation)
  - [M SetTolerance ](#ApiClient.NumericExpectation.SetTolerance)

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

NumericExpectation

- [C NumericExpectation ](#ApiClient.NumericExpectation)
  - [M Clone ](#ApiClient.NumericExpectation.Clone)
  - [M DeactivateTolerance ](#ApiClient.NumericExpectation.DeactivateTolerance)
  - [M GetDontEvalNotPresent ](#ApiClient.NumericExpectation.GetDontEvalNotPresent)
  - [M GetExpression ](#ApiClient.NumericExpectation.GetExpression)
  - [M GetRelation ](#ApiClient.NumericExpectation.GetRelation)
  - [M GetToleranceType ](#ApiClient.NumericExpectation.GetToleranceType)
  - [M GetToleranceValue ](#ApiClient.NumericExpectation.GetToleranceValue)
  - [M SetDontEvalNotPresent ](#ApiClient.NumericExpectation.SetDontEvalNotPresent)
  - [M SetExpression ](#ApiClient.NumericExpectation.SetExpression)
  - [M SetRelation ](#ApiClient.NumericExpectation.SetRelation)
  - [M SetTolerance ](#ApiClient.NumericExpectation.SetTolerance)

# NumericExpectation[¶](#numericexpectation "Link to this heading")

*class* NumericExpectation[¶](#ApiClient.NumericExpectation "Link to this definition")  
Returned by

- [`ExpectationApi.CreateNumericExpectation`](../ExpectationApi.md#ApiClient.ExpectationApi.CreateNumericExpectation "ApiClient.ExpectationApi.CreateNumericExpectation (Python method) — Creates a numeric expectation.")

Clone()[¶](#ApiClient.NumericExpectation.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`NumericExpectation`](#ApiClient.NumericExpectation "ApiClient.NumericExpectation (Python class) — ExpectationApi.CreateNumericExpectation")

DeactivateTolerance()[¶](#ApiClient.NumericExpectation.DeactivateTolerance "Link to this definition")  
Deactivates the tolerance for this expectation.

GetDontEvalNotPresent()[¶](#ApiClient.NumericExpectation.GetDontEvalNotPresent "Link to this definition")  
Returns whether the option to evaluate this expectation if the expected value is NotPresent is set or not.

Returns:  True if the described behavior is enabled otherwise False.

Return type:  boolean

GetExpression()[¶](#ApiClient.NumericExpectation.GetExpression "Link to this definition")  
Returns the expectations expression.

Returns:  The expression

Return type:  str

GetRelation()[¶](#ApiClient.NumericExpectation.GetRelation "Link to this definition")  
Returns the relation for this expectation.

Returns:  The relation

Return type:  str

GetToleranceType()[¶](#ApiClient.NumericExpectation.GetToleranceType "Link to this definition")  
Returns the type of the set tolerance. Returns ‘absolute-value’, ‘percentage’, ‘decimal-places’, or ‘none’.

Returns:  The type of the tolerence

Return type:  str

GetToleranceValue()[¶](#ApiClient.NumericExpectation.GetToleranceValue "Link to this definition")  
Returns the expression for the tolerance or None if the tolerance type is ‘none’.

Returns:  The expression for the tolerance

Return type:  str

SetDontEvalNotPresent(*[dontEvalNotPresent](#ApiClient.NumericExpectation.SetDontEvalNotPresent.dontEvalNotPresent "ApiClient.NumericExpectation.SetDontEvalNotPresent.dontEvalNotPresent (Python parameter) — True to enable the described behavior.")*)[¶](#ApiClient.NumericExpectation.SetDontEvalNotPresent "Link to this definition")  
Enables or disables the option to evaluate this expectation if the expected value is NotPresent.

Parameters:  dontEvalNotPresent : boolean[¶](#ApiClient.NumericExpectation.SetDontEvalNotPresent.dontEvalNotPresent "Permalink to this definition")  
True to enable the described behavior. False to disable it.

SetExpression(*[expression](#ApiClient.NumericExpectation.SetExpression.expression "ApiClient.NumericExpectation.SetExpression.expression (Python parameter) — The expression")*)[¶](#ApiClient.NumericExpectation.SetExpression "Link to this definition")  
Sets the expectations expression.

Parameters:  expression : str[¶](#ApiClient.NumericExpectation.SetExpression.expression "Permalink to this definition")  
The expression

SetRelation(*[relation](#ApiClient.NumericExpectation.SetRelation.relation "ApiClient.NumericExpectation.SetRelation.relation (Python parameter) — The relation")*)[¶](#ApiClient.NumericExpectation.SetRelation "Link to this definition")  
Sets the relation for this expectation. Allowed values are:  
- ‘\<’

- ‘\<=’

- ‘==’

- ‘\>=’

- ‘\>’

- ‘!=’

- ‘\<\>’ (results in ‘!=’)

Parameters:  relation : str[¶](#ApiClient.NumericExpectation.SetRelation.relation "Permalink to this definition")  
The relation

SetTolerance(*[toleranceType](#ApiClient.NumericExpectation.SetTolerance.toleranceType "ApiClient.NumericExpectation.SetTolerance.toleranceType (Python parameter) — Possible types are: - 'absolute-value' - 'percentage' - 'decimal-places'")*, *[toleranceExpr](#ApiClient.NumericExpectation.SetTolerance.toleranceExpr "ApiClient.NumericExpectation.SetTolerance.toleranceExpr (Python parameter) — The expression for the tolerance")*)[¶](#ApiClient.NumericExpectation.SetTolerance "Link to this definition")  
Sets the type and value of the tolerance for this expectation.

Parameters:  toleranceType : str[¶](#ApiClient.NumericExpectation.SetTolerance.toleranceType "Permalink to this definition")  
Possible types are: - ‘absolute-value’ - ‘percentage’ - ‘decimal-places’

toleranceExpr : str[¶](#ApiClient.NumericExpectation.SetTolerance.toleranceExpr "Permalink to this definition")  
The expression for the tolerance

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
