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

BitStreamExpectation [ BitStreamExpectation ](#)

BitStreamExpectation

- [C BitStreamExpectation ](#ApiClient.BitStreamExpectation)
  - [M Clone ](#ApiClient.BitStreamExpectation.Clone)
  - [M GetExpression ](#ApiClient.BitStreamExpectation.GetExpression)
  - [M GetMaskExpression ](#ApiClient.BitStreamExpectation.GetMaskExpression)
  - [M GetSizeExpectation ](#ApiClient.BitStreamExpectation.GetSizeExpectation)
  - [M RemoveSizeExpectation ](#ApiClient.BitStreamExpectation.RemoveSizeExpectation)
  - [M SetExpression ](#ApiClient.BitStreamExpectation.SetExpression)
  - [M SetMaskExpression ](#ApiClient.BitStreamExpectation.SetMaskExpression)
  - [M SetSizeExpectation ](#ApiClient.BitStreamExpectation.SetSizeExpectation)

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

BitStreamExpectation

- [C BitStreamExpectation ](#ApiClient.BitStreamExpectation)
  - [M Clone ](#ApiClient.BitStreamExpectation.Clone)
  - [M GetExpression ](#ApiClient.BitStreamExpectation.GetExpression)
  - [M GetMaskExpression ](#ApiClient.BitStreamExpectation.GetMaskExpression)
  - [M GetSizeExpectation ](#ApiClient.BitStreamExpectation.GetSizeExpectation)
  - [M RemoveSizeExpectation ](#ApiClient.BitStreamExpectation.RemoveSizeExpectation)
  - [M SetExpression ](#ApiClient.BitStreamExpectation.SetExpression)
  - [M SetMaskExpression ](#ApiClient.BitStreamExpectation.SetMaskExpression)
  - [M SetSizeExpectation ](#ApiClient.BitStreamExpectation.SetSizeExpectation)

# BitStreamExpectation[¶](#bitstreamexpectation "Link to this heading")

*class* BitStreamExpectation[¶](#ApiClient.BitStreamExpectation "Link to this definition")  
Returned by

- [`ExpectationApi.CreateBitStreamExpectation`](../ExpectationApi.md#ApiClient.ExpectationApi.CreateBitStreamExpectation "ApiClient.ExpectationApi.CreateBitStreamExpectation (Python method) — Creates a bit stream expectation.")

Clone()[¶](#ApiClient.BitStreamExpectation.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`BitStreamExpectation`](#ApiClient.BitStreamExpectation "ApiClient.BitStreamExpectation (Python class) — ExpectationApi.CreateBitStreamExpectation")

GetExpression()[¶](#ApiClient.BitStreamExpectation.GetExpression "Link to this definition")  
Returns the expectation expression.

Returns:  The expectation expression

Return type:  str

GetMaskExpression()[¶](#ApiClient.BitStreamExpectation.GetMaskExpression "Link to this definition")  
Returns the mask expression.

Returns:  The mask expression

Return type:  str

GetSizeExpectation()[¶](#ApiClient.BitStreamExpectation.GetSizeExpectation "Link to this definition")  
Returns the size expectation, or None, if the size of the BitStream has no expectation.

Returns:  The size expectation

Return type:  [`NumericExpectation`](NumericExpectation.md#ApiClient.NumericExpectation "ApiClient.NumericExpectation (Python class) — ExpectationApi.CreateNumericExpectation")

RemoveSizeExpectation()[¶](#ApiClient.BitStreamExpectation.RemoveSizeExpectation "Link to this definition")  
Removes the size expectation.

SetExpression(*[expression](#ApiClient.BitStreamExpectation.SetExpression.expression "ApiClient.BitStreamExpectation.SetExpression.expression (Python parameter) — The expectation expression, e.g.")*)[¶](#ApiClient.BitStreamExpectation.SetExpression "Link to this definition")  
Sets the expectation expression.

Parameters:  expression : str[¶](#ApiClient.BitStreamExpectation.SetExpression.expression "Permalink to this definition")  
The expectation expression, e.g. ‘BitStream(0x0, 32)’

SetMaskExpression(*[expression](#ApiClient.BitStreamExpectation.SetMaskExpression.expression "ApiClient.BitStreamExpectation.SetMaskExpression.expression (Python parameter) — The mask expression, e.g.")*)[¶](#ApiClient.BitStreamExpectation.SetMaskExpression "Link to this definition")  
Sets the mask expression.

Parameters:  expression : str[¶](#ApiClient.BitStreamExpectation.SetMaskExpression.expression "Permalink to this definition")  
The mask expression, e.g. ‘BitStream(0x0, 32)’

SetSizeExpectation(*[expectation](#ApiClient.BitStreamExpectation.SetSizeExpectation.expectation "ApiClient.BitStreamExpectation.SetSizeExpectation.expectation (Python parameter) — The numeric expectation")*)[¶](#ApiClient.BitStreamExpectation.SetSizeExpectation "Link to this definition")  
Sets the size expectation.

Parameters:  expectation[¶](#ApiClient.BitStreamExpectation.SetSizeExpectation.expectation "Permalink to this definition")  
The numeric expectation

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
