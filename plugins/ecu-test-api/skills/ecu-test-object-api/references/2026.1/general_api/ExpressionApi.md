[ Internal APIs ](api.md)

[ Advanced operations of package variable types ](variabledatastructures.md)

[ Advanced properties of bus-related objects ](busdatastructures.md)

[ Bus related objects of trace analysis ](busdatastructuresTraceanalysis.md)

[ Advanced properties of diagnostics-related objects ](diagdatastructures.md)

[ Diagnostics related objects of trace analysis ](diagdatastructuresTraceanalysis.md)

[ Advanced properties of media-related objects ](mediadatastructures.md)

[ Advanced properties of DLT logging-related objects ](dltdatastructures.md)

[ COM API ](com-api.md)

[ REST API ](rest-api.md)

[ Report API ](apireport.md)

[ Object API ](objectApi.md)

Object API

[ API entry points ](objectApi.md#api-entry-points)

API entry points

[ API for Analysis Jobs ](AnalysisJobApi.md)

[ API for Artifacts ](ArtifactApi.md)

[ API for Project Components ](ComponentApi.md)

[ API for Configurations ](ConfigurationApi.md)

[ API for Expectations ](ExpectationApi.md)

[ API for Expressions ](#)

API for Expressions

- [ CurveExpression ](ExpressionApi/CurveExpression.md)
- [ Expression ](ExpressionApi/Expression.md)
- [ ExpressionValue ](ExpressionApi/ExpressionValue.md)
- [ KeywordValueExpression ](ExpressionApi/KeywordValueExpression.md)
- [ MapExpression ](ExpressionApi/MapExpression.md)
- [ MatrixExpression ](ExpressionApi/MatrixExpression.md)
- [ VectorExpression ](ExpressionApi/VectorExpression.md)

API for Expressions [ API for Expressions ](#)

API for Expressions

- [C ExpressionApi ](#ApiClient.ExpressionApi)
  - [M CreateCurveExpression ](#ApiClient.ExpressionApi.CreateCurveExpression)
  - [M CreateKeywordValueExpression ](#ApiClient.ExpressionApi.CreateKeywordValueExpression)
  - [M CreateMapExpression ](#ApiClient.ExpressionApi.CreateMapExpression)
  - [M CreateMatrixExpression ](#ApiClient.ExpressionApi.CreateMatrixExpression)
  - [M CreateVectorExpression ](#ApiClient.ExpressionApi.CreateVectorExpression)
- [ CurveExpression ](ExpressionApi/CurveExpression.md)
- [ Expression ](ExpressionApi/Expression.md)
- [ ExpressionValue ](ExpressionApi/ExpressionValue.md)
- [ KeywordValueExpression ](ExpressionApi/KeywordValueExpression.md)
- [ MapExpression ](ExpressionApi/MapExpression.md)
- [ MatrixExpression ](ExpressionApi/MatrixExpression.md)
- [ VectorExpression ](ExpressionApi/VectorExpression.md)

[ API for Global Mappings ](GlobalMappingApi.md)

[ API for Mappings ](MappingApi.md)

[ API for Multimedia Objects ](MultimediaApi.md)

[ API for Packages ](PackageApi.md)

[ API for Parameters ](ParameterApi.md)

[ API for Projects ](ProjectApi.md)

[ API for Relations ](RelationApi.md)

[ API for Reports ](ReportApi.md)

[ API for Report Filters ](ReportFilterApi.md)

[ API for Settings ](SettingsApi.md)

[ API for Signals ](SignalApi.md)

[ API for Signal Descriptions ](SignalDescriptionApi.md)

[ API for Signal Recordings ](SignalRecordingApi.md)

[ API for Symbols ](SymbolApi.md)

[ API for Test Steps ](TestStepApi.md)

[ API for Touch Inputs ](TouchInputApi.md)

[ API for Trace Analyses ](TraceAnalysisApi.md)

[ API for Trace Files ](TraceFileApi.md)

[ API for Trace Step Templates ](TraceStepTemplateApi.md)

[ API for Variables ](VariableApi.md)

[ API for Workspaces ](WorkspaceApi.md)

[ Trace Analysis API ](../TraceAnalysisAPI/index.md)

[ Generator APIs ](../generators/index.md)

[ Tools ](../tools/index.md)

[ User test management ](../userTestmanagement/index.md)

[ UserUtility API ](../user-utility/user-utility.md)

[ Utility Examples ](../user-utility/example-utilities.md)

API for Expressions

- [C ExpressionApi ](#ApiClient.ExpressionApi)
  - [M CreateCurveExpression ](#ApiClient.ExpressionApi.CreateCurveExpression)
  - [M CreateKeywordValueExpression ](#ApiClient.ExpressionApi.CreateKeywordValueExpression)
  - [M CreateMapExpression ](#ApiClient.ExpressionApi.CreateMapExpression)
  - [M CreateMatrixExpression ](#ApiClient.ExpressionApi.CreateMatrixExpression)
  - [M CreateVectorExpression ](#ApiClient.ExpressionApi.CreateVectorExpression)

# API for Expressions[¶](#api-for-expressions "Link to this heading")

Part of the [Object based program API](objectApi.md#objectapi).

*class* ExpressionApi[¶](#ApiClient.ExpressionApi "Link to this definition")  
Returned by

- [`PackageApi.ExpressionApi`](PackageApi.md#ApiClient.PackageApi.ExpressionApi "ApiClient.PackageApi.ExpressionApi (Python attribute) — Returns the ExpressionApi namespace.")

CreateCurveExpression(*[length](#ApiClient.ExpressionApi.CreateCurveExpression.length "ApiClient.ExpressionApi.CreateCurveExpression.length (Python parameter) — maximum number of elements")*, *[defaultValue](#ApiClient.ExpressionApi.CreateCurveExpression.defaultValue "ApiClient.ExpressionApi.CreateCurveExpression.defaultValue (Python parameter) — Expression to be used as default value")=`None`*, *[distributionDefaultValue](#ApiClient.ExpressionApi.CreateCurveExpression.distributionDefaultValue "ApiClient.ExpressionApi.CreateCurveExpression.distributionDefaultValue (Python parameter) — Expression to be used as default value for distribution")=`None`*)[¶](#ApiClient.ExpressionApi.CreateCurveExpression "Link to this definition")  
Creates a CurveExpression

Parameters:  length : int[¶](#ApiClient.ExpressionApi.CreateCurveExpression.length "Permalink to this definition")  
maximum number of elements

defaultValue : str[¶](#ApiClient.ExpressionApi.CreateCurveExpression.defaultValue "Permalink to this definition")  
Expression to be used as default value

distributionDefaultValue : str[¶](#ApiClient.ExpressionApi.CreateCurveExpression.distributionDefaultValue "Permalink to this definition")  
Expression to be used as default value for distribution

Returns:  The curve expression

Return type:  [`CurveExpression`](ExpressionApi/CurveExpression.md#ApiClient.CurveExpression "ApiClient.CurveExpression (Python class) — ExpressionApi.CreateCurveExpression")

CreateKeywordValueExpression(*[value](#ApiClient.ExpressionApi.CreateKeywordValueExpression.value "ApiClient.ExpressionApi.CreateKeywordValueExpression.value (Python parameter) — The value that refers to a localization identifier.")*)[¶](#ApiClient.ExpressionApi.CreateKeywordValueExpression "Link to this definition")  
Creates a KeywordValue expression that uses the identifier to a localization object.

Parameters:  value : int[¶](#ApiClient.ExpressionApi.CreateKeywordValueExpression.value "Permalink to this definition")  
The value that refers to a localization identifier.

Returns:  The KeywordValue expression

Return type:  [`KeywordValueExpression`](ExpressionApi/KeywordValueExpression.md#ApiClient.KeywordValueExpression "ApiClient.KeywordValueExpression (Python class) — ExpressionApi.CreateKeywordValueExpression")

CreateMapExpression(*[xDimension](#ApiClient.ExpressionApi.CreateMapExpression.xDimension "ApiClient.ExpressionApi.CreateMapExpression.xDimension (Python parameter) — maximum number of elements in x dimension")*, *[yDimension](#ApiClient.ExpressionApi.CreateMapExpression.yDimension "ApiClient.ExpressionApi.CreateMapExpression.yDimension (Python parameter) — maximum number of elements in y dimension")*, *[defaultValue](#ApiClient.ExpressionApi.CreateMapExpression.defaultValue "ApiClient.ExpressionApi.CreateMapExpression.defaultValue (Python parameter) — Expression to be used as default value")=`None`*, *[xDistributionDefaultValue](#ApiClient.ExpressionApi.CreateMapExpression.xDistributionDefaultValue "ApiClient.ExpressionApi.CreateMapExpression.xDistributionDefaultValue (Python parameter) — Expression to be used as default value for x distribution")=`None`*, *[yDistributionDefaultValue](#ApiClient.ExpressionApi.CreateMapExpression.yDistributionDefaultValue "ApiClient.ExpressionApi.CreateMapExpression.yDistributionDefaultValue (Python parameter) — Expression to be used as default value for y distribution")=`None`*)[¶](#ApiClient.ExpressionApi.CreateMapExpression "Link to this definition")  
Creates a MapExpression

Parameters:  xDimension : int[¶](#ApiClient.ExpressionApi.CreateMapExpression.xDimension "Permalink to this definition")  
maximum number of elements in x dimension

yDimension : int[¶](#ApiClient.ExpressionApi.CreateMapExpression.yDimension "Permalink to this definition")  
maximum number of elements in y dimension

defaultValue : str[¶](#ApiClient.ExpressionApi.CreateMapExpression.defaultValue "Permalink to this definition")  
Expression to be used as default value

xDistributionDefaultValue : str[¶](#ApiClient.ExpressionApi.CreateMapExpression.xDistributionDefaultValue "Permalink to this definition")  
Expression to be used as default value for x distribution

yDistributionDefaultValue : str[¶](#ApiClient.ExpressionApi.CreateMapExpression.yDistributionDefaultValue "Permalink to this definition")  
Expression to be used as default value for y distribution

Returns:  The map expression

Return type:  [`MapExpression`](ExpressionApi/MapExpression.md#ApiClient.MapExpression "ApiClient.MapExpression (Python class) — ExpressionApi.CreateMapExpression")

CreateMatrixExpression(*[xDimension](#ApiClient.ExpressionApi.CreateMatrixExpression.xDimension "ApiClient.ExpressionApi.CreateMatrixExpression.xDimension (Python parameter) — maximum number of elements in x dimension")*, *[yDimension](#ApiClient.ExpressionApi.CreateMatrixExpression.yDimension "ApiClient.ExpressionApi.CreateMatrixExpression.yDimension (Python parameter) — maximum number of elements in y dimension")*, *[defaultValue](#ApiClient.ExpressionApi.CreateMatrixExpression.defaultValue "ApiClient.ExpressionApi.CreateMatrixExpression.defaultValue (Python parameter) — Expression to be used as default value")=`None`*)[¶](#ApiClient.ExpressionApi.CreateMatrixExpression "Link to this definition")  
Creates a MatrixExpression

Parameters:  xDimension : int[¶](#ApiClient.ExpressionApi.CreateMatrixExpression.xDimension "Permalink to this definition")  
maximum number of elements in x dimension

yDimension : int[¶](#ApiClient.ExpressionApi.CreateMatrixExpression.yDimension "Permalink to this definition")  
maximum number of elements in y dimension

defaultValue : str[¶](#ApiClient.ExpressionApi.CreateMatrixExpression.defaultValue "Permalink to this definition")  
Expression to be used as default value

Returns:  The matrix expression

Return type:  [`MatrixExpression`](ExpressionApi/MatrixExpression.md#ApiClient.MatrixExpression "ApiClient.MatrixExpression (Python class) — ExpressionApi.CreateMatrixExpression")

CreateVectorExpression(*[length](#ApiClient.ExpressionApi.CreateVectorExpression.length "ApiClient.ExpressionApi.CreateVectorExpression.length (Python parameter) — maximum number of elements")*, *[defaultValue](#ApiClient.ExpressionApi.CreateVectorExpression.defaultValue "ApiClient.ExpressionApi.CreateVectorExpression.defaultValue (Python parameter) — Expression to be used as default value")=`None`*)[¶](#ApiClient.ExpressionApi.CreateVectorExpression "Link to this definition")  
Creates a VectorExpression

Parameters:  length : int[¶](#ApiClient.ExpressionApi.CreateVectorExpression.length "Permalink to this definition")  
maximum number of elements

defaultValue : str[¶](#ApiClient.ExpressionApi.CreateVectorExpression.defaultValue "Permalink to this definition")  
Expression to be used as default value

Returns:  The vector expression

Return type:  [`VectorExpression`](ExpressionApi/VectorExpression.md#ApiClient.VectorExpression "ApiClient.VectorExpression (Python class) — ExpressionApi.CreateVectorExpression")

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
