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

StringListExpectation [ StringListExpectation ](#)

StringListExpectation

- [C StringListExpectation ](#ApiClient.StringListExpectation)
  - [M Clone ](#ApiClient.StringListExpectation.Clone)
  - [M GetCaseSensitive ](#ApiClient.StringListExpectation.GetCaseSensitive)
  - [M GetExpressionList ](#ApiClient.StringListExpectation.GetExpressionList)
  - [M GetStringList ](#ApiClient.StringListExpectation.GetStringList)
  - [M GetStringListVariableName ](#ApiClient.StringListExpectation.GetStringListVariableName)
  - [M SetCaseSensitive ](#ApiClient.StringListExpectation.SetCaseSensitive)
  - [M SetExpressionList ](#ApiClient.StringListExpectation.SetExpressionList)
  - [M SetStringList ](#ApiClient.StringListExpectation.SetStringList)
  - [M SetStringListVariableName ](#ApiClient.StringListExpectation.SetStringListVariableName)

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

StringListExpectation

- [C StringListExpectation ](#ApiClient.StringListExpectation)
  - [M Clone ](#ApiClient.StringListExpectation.Clone)
  - [M GetCaseSensitive ](#ApiClient.StringListExpectation.GetCaseSensitive)
  - [M GetExpressionList ](#ApiClient.StringListExpectation.GetExpressionList)
  - [M GetStringList ](#ApiClient.StringListExpectation.GetStringList)
  - [M GetStringListVariableName ](#ApiClient.StringListExpectation.GetStringListVariableName)
  - [M SetCaseSensitive ](#ApiClient.StringListExpectation.SetCaseSensitive)
  - [M SetExpressionList ](#ApiClient.StringListExpectation.SetExpressionList)
  - [M SetStringList ](#ApiClient.StringListExpectation.SetStringList)
  - [M SetStringListVariableName ](#ApiClient.StringListExpectation.SetStringListVariableName)

# StringListExpectation[¶](#stringlistexpectation "Link to this heading")

*class* StringListExpectation[¶](#ApiClient.StringListExpectation "Link to this definition")  
Returned by

- [`ExpectationApi.CreateStringListExpectation`](../ExpectationApi.md#ApiClient.ExpectationApi.CreateStringListExpectation "ApiClient.ExpectationApi.CreateStringListExpectation (Python method) — Creates a string list expectation.")

Clone()[¶](#ApiClient.StringListExpectation.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`StringListExpectation`](#ApiClient.StringListExpectation "ApiClient.StringListExpectation (Python class) — ExpectationApi.CreateStringListExpectation")

GetCaseSensitive()[¶](#ApiClient.StringListExpectation.GetCaseSensitive "Link to this definition")  
Returns whether the comparison should be case-sensitive.

Returns:  True if case-sensitive, else False.

Return type:  boolean

GetExpressionList()[¶](#ApiClient.StringListExpectation.GetExpressionList "Link to this definition")  
Returns the list of expressions if set, otherwise an empty list. Currently only KeywordValueExpression are supported!

Returns:  The list of expressions

Return type:  list[[`KeywordValueExpression`](../ExpressionApi/KeywordValueExpression.md#ApiClient.KeywordValueExpression "ApiClient.KeywordValueExpression (Python class) — ExpressionApi.CreateKeywordValueExpression")]

GetStringList()[¶](#ApiClient.StringListExpectation.GetStringList "Link to this definition")  
Returns the list of strings if set, otherwise an empty list.

Returns:  The list of strings

Return type:  list[str]

GetStringListVariableName()[¶](#ApiClient.StringListExpectation.GetStringListVariableName "Link to this definition")  
Returns the variable that stores the list of strings if set else None.

Returns:  The variable name

Return type:  str

SetCaseSensitive(*[caseSensitive](#ApiClient.StringListExpectation.SetCaseSensitive.caseSensitive "ApiClient.StringListExpectation.SetCaseSensitive.caseSensitive (Python parameter) — True if case-sensitive, else False.")*)[¶](#ApiClient.StringListExpectation.SetCaseSensitive "Link to this definition")  
Sets whether the comparison should be case-sensitive.

Parameters:  caseSensitive : boolean[¶](#ApiClient.StringListExpectation.SetCaseSensitive.caseSensitive "Permalink to this definition")  
True if case-sensitive, else False.

SetExpressionList(*[exprList](#ApiClient.StringListExpectation.SetExpressionList.exprList "ApiClient.StringListExpectation.SetExpressionList.exprList (Python parameter) — The list of expressions")*)[¶](#ApiClient.StringListExpectation.SetExpressionList "Link to this definition")  
Sets the expectations expression. Currently only KeywordValueExpression are supported!

Parameters:  exprList[¶](#ApiClient.StringListExpectation.SetExpressionList.exprList "Permalink to this definition")  
The list of expressions

SetStringList(*[stringList](#ApiClient.StringListExpectation.SetStringList.stringList "ApiClient.StringListExpectation.SetStringList.stringList (Python parameter) — The list of strings")*)[¶](#ApiClient.StringListExpectation.SetStringList "Link to this definition")  
Sets the list of strings the actual value has to be contained in.

Parameters:  stringList : list[str][¶](#ApiClient.StringListExpectation.SetStringList.stringList "Permalink to this definition")  
The list of strings

SetStringListVariableName(*[variableName](#ApiClient.StringListExpectation.SetStringListVariableName.variableName "ApiClient.StringListExpectation.SetStringListVariableName.variableName (Python parameter) — Name of the variable")*)[¶](#ApiClient.StringListExpectation.SetStringListVariableName "Link to this definition")  
Sets the variable that stores the list of strings the actual value has to be contained in.

Parameters:  variableName : str[¶](#ApiClient.StringListExpectation.SetStringListVariableName.variableName "Permalink to this definition")  
Name of the variable

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
