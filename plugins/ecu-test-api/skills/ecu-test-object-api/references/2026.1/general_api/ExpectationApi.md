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

[ API for Expectations ](#)

API for Expectations

- [ AllExpectation ](ExpectationApi/AllExpectation.md)
- [ AudioExpectation ](ExpectationApi/AudioExpectation.md)
- [ BinaryExpressionExpectation ](ExpectationApi/BinaryExpressionExpectation.md)
- [ BitStreamExpectation ](ExpectationApi/BitStreamExpectation.md)
- [ BitStreamExpressionExpectation ](ExpectationApi/BitStreamExpressionExpectation.md)
- [ BooleanExpectation ](ExpectationApi/BooleanExpectation.md)
- [ ByteStreamExpectation ](ExpectationApi/ByteStreamExpectation.md)
- [ ByteStreamExpressionExpectation ](ExpectationApi/ByteStreamExpressionExpectation.md)
- [ CurveAllExpectation ](ExpectationApi/CurveAllExpectation.md)
- [ CurveSingleExpectation ](ExpectationApi/CurveSingleExpectation.md)
- [ DTCListExpectation ](ExpectationApi/DTCListExpectation.md)
- [ Expectation ](ExpectationApi/Expectation.md)
- [ ExpressionExpectation ](ExpectationApi/ExpressionExpectation.md)
- [ ExpressionExpectationBase ](ExpectationApi/ExpressionExpectationBase.md)
- [ ImageExpectation ](ExpectationApi/ImageExpectation.md)
- [ ManualExpression ](ExpectationApi/ManualExpression.md)
- [ MapAllExpectation ](ExpectationApi/MapAllExpectation.md)
- [ MapSingleExpectation ](ExpectationApi/MapSingleExpectation.md)
- [ MatrixAllExpectation ](ExpectationApi/MatrixAllExpectation.md)
- [ MatrixSingleExpectation ](ExpectationApi/MatrixSingleExpectation.md)
- [ NotPresentExpectation ](ExpectationApi/NotPresentExpectation.md)
- [ NumericExpectation ](ExpectationApi/NumericExpectation.md)
- [ NumericExpressionExpectation ](ExpectationApi/NumericExpressionExpectation.md)
- [ PresentExpectation ](ExpectationApi/PresentExpectation.md)
- [ StringExpectation ](ExpectationApi/StringExpectation.md)
- [ StringExpressionExpectation ](ExpectationApi/StringExpressionExpectation.md)
- [ StringListExpectation ](ExpectationApi/StringListExpectation.md)
- [ VectorAllExpectation ](ExpectationApi/VectorAllExpectation.md)
- [ VectorSingleExpectation ](ExpectationApi/VectorSingleExpectation.md)

API for Expectations [ API for Expectations ](#)

API for Expectations

- [C ExpectationApi ](#ApiClient.ExpectationApi)
  - [M CreateAudioExpectation ](#ApiClient.ExpectationApi.CreateAudioExpectation)
  - [M CreateBinaryExpressionExpectation ](#ApiClient.ExpectationApi.CreateBinaryExpressionExpectation)
  - [M CreateBitStreamExpectation ](#ApiClient.ExpectationApi.CreateBitStreamExpectation)
  - [M CreateBitStreamExpressionExpectation ](#ApiClient.ExpectationApi.CreateBitStreamExpressionExpectation)
  - [M CreateBooleanExpectation ](#ApiClient.ExpectationApi.CreateBooleanExpectation)
  - [M CreateByteStreamExpectation ](#ApiClient.ExpectationApi.CreateByteStreamExpectation)
  - [M CreateByteStreamExpressionExpectation ](#ApiClient.ExpectationApi.CreateByteStreamExpressionExpectation)
  - [M CreateCurveAllExpectation ](#ApiClient.ExpectationApi.CreateCurveAllExpectation)
  - [M CreateCurveAllExpressionExpectation ](#ApiClient.ExpectationApi.CreateCurveAllExpressionExpectation)
  - [M CreateCurveSingleExpectation ](#ApiClient.ExpectationApi.CreateCurveSingleExpectation)
  - [M CreateDTCListExpectation ](#ApiClient.ExpectationApi.CreateDTCListExpectation)
  - [M CreateExpressionExpectation ](#ApiClient.ExpectationApi.CreateExpressionExpectation)
  - [M CreateImageExpectation ](#ApiClient.ExpectationApi.CreateImageExpectation)
  - [M CreateMapAllExpectation ](#ApiClient.ExpectationApi.CreateMapAllExpectation)
  - [M CreateMapAllExpressionExpectation ](#ApiClient.ExpectationApi.CreateMapAllExpressionExpectation)
  - [M CreateMapSingleExpectation ](#ApiClient.ExpectationApi.CreateMapSingleExpectation)
  - [M CreateMatrixAllExpectation ](#ApiClient.ExpectationApi.CreateMatrixAllExpectation)
  - [M CreateMatrixAllExpressionExpectation ](#ApiClient.ExpectationApi.CreateMatrixAllExpressionExpectation)
  - [M CreateMatrixSingleExpectation ](#ApiClient.ExpectationApi.CreateMatrixSingleExpectation)
  - [M CreateNotPresentExpectation ](#ApiClient.ExpectationApi.CreateNotPresentExpectation)
  - [M CreateNumericExpectation ](#ApiClient.ExpectationApi.CreateNumericExpectation)
  - [M CreateNumericExpressionExpectation ](#ApiClient.ExpectationApi.CreateNumericExpressionExpectation)
  - [M CreatePresentExpectation ](#ApiClient.ExpectationApi.CreatePresentExpectation)
  - [M CreateStringExpectation ](#ApiClient.ExpectationApi.CreateStringExpectation)
  - [M CreateStringExpressionExpectation ](#ApiClient.ExpectationApi.CreateStringExpressionExpectation)
  - [M CreateStringListExpectation ](#ApiClient.ExpectationApi.CreateStringListExpectation)
  - [M CreateVectorAllExpectation ](#ApiClient.ExpectationApi.CreateVectorAllExpectation)
  - [M CreateVectorAllExpressionExpectation ](#ApiClient.ExpectationApi.CreateVectorAllExpressionExpectation)
  - [M CreateVectorSingleExpectation ](#ApiClient.ExpectationApi.CreateVectorSingleExpectation)
- [ AllExpectation ](ExpectationApi/AllExpectation.md)
- [ AudioExpectation ](ExpectationApi/AudioExpectation.md)
- [ BinaryExpressionExpectation ](ExpectationApi/BinaryExpressionExpectation.md)
- [ BitStreamExpectation ](ExpectationApi/BitStreamExpectation.md)
- [ BitStreamExpressionExpectation ](ExpectationApi/BitStreamExpressionExpectation.md)
- [ BooleanExpectation ](ExpectationApi/BooleanExpectation.md)
- [ ByteStreamExpectation ](ExpectationApi/ByteStreamExpectation.md)
- [ ByteStreamExpressionExpectation ](ExpectationApi/ByteStreamExpressionExpectation.md)
- [ CurveAllExpectation ](ExpectationApi/CurveAllExpectation.md)
- [ CurveSingleExpectation ](ExpectationApi/CurveSingleExpectation.md)
- [ DTCListExpectation ](ExpectationApi/DTCListExpectation.md)
- [ Expectation ](ExpectationApi/Expectation.md)
- [ ExpressionExpectation ](ExpectationApi/ExpressionExpectation.md)
- [ ExpressionExpectationBase ](ExpectationApi/ExpressionExpectationBase.md)
- [ ImageExpectation ](ExpectationApi/ImageExpectation.md)
- [ ManualExpression ](ExpectationApi/ManualExpression.md)
- [ MapAllExpectation ](ExpectationApi/MapAllExpectation.md)
- [ MapSingleExpectation ](ExpectationApi/MapSingleExpectation.md)
- [ MatrixAllExpectation ](ExpectationApi/MatrixAllExpectation.md)
- [ MatrixSingleExpectation ](ExpectationApi/MatrixSingleExpectation.md)
- [ NotPresentExpectation ](ExpectationApi/NotPresentExpectation.md)
- [ NumericExpectation ](ExpectationApi/NumericExpectation.md)
- [ NumericExpressionExpectation ](ExpectationApi/NumericExpressionExpectation.md)
- [ PresentExpectation ](ExpectationApi/PresentExpectation.md)
- [ StringExpectation ](ExpectationApi/StringExpectation.md)
- [ StringExpressionExpectation ](ExpectationApi/StringExpressionExpectation.md)
- [ StringListExpectation ](ExpectationApi/StringListExpectation.md)
- [ VectorAllExpectation ](ExpectationApi/VectorAllExpectation.md)
- [ VectorSingleExpectation ](ExpectationApi/VectorSingleExpectation.md)

[ API for Expressions ](ExpressionApi.md)

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

API for Expectations

- [C ExpectationApi ](#ApiClient.ExpectationApi)
  - [M CreateAudioExpectation ](#ApiClient.ExpectationApi.CreateAudioExpectation)
  - [M CreateBinaryExpressionExpectation ](#ApiClient.ExpectationApi.CreateBinaryExpressionExpectation)
  - [M CreateBitStreamExpectation ](#ApiClient.ExpectationApi.CreateBitStreamExpectation)
  - [M CreateBitStreamExpressionExpectation ](#ApiClient.ExpectationApi.CreateBitStreamExpressionExpectation)
  - [M CreateBooleanExpectation ](#ApiClient.ExpectationApi.CreateBooleanExpectation)
  - [M CreateByteStreamExpectation ](#ApiClient.ExpectationApi.CreateByteStreamExpectation)
  - [M CreateByteStreamExpressionExpectation ](#ApiClient.ExpectationApi.CreateByteStreamExpressionExpectation)
  - [M CreateCurveAllExpectation ](#ApiClient.ExpectationApi.CreateCurveAllExpectation)
  - [M CreateCurveAllExpressionExpectation ](#ApiClient.ExpectationApi.CreateCurveAllExpressionExpectation)
  - [M CreateCurveSingleExpectation ](#ApiClient.ExpectationApi.CreateCurveSingleExpectation)
  - [M CreateDTCListExpectation ](#ApiClient.ExpectationApi.CreateDTCListExpectation)
  - [M CreateExpressionExpectation ](#ApiClient.ExpectationApi.CreateExpressionExpectation)
  - [M CreateImageExpectation ](#ApiClient.ExpectationApi.CreateImageExpectation)
  - [M CreateMapAllExpectation ](#ApiClient.ExpectationApi.CreateMapAllExpectation)
  - [M CreateMapAllExpressionExpectation ](#ApiClient.ExpectationApi.CreateMapAllExpressionExpectation)
  - [M CreateMapSingleExpectation ](#ApiClient.ExpectationApi.CreateMapSingleExpectation)
  - [M CreateMatrixAllExpectation ](#ApiClient.ExpectationApi.CreateMatrixAllExpectation)
  - [M CreateMatrixAllExpressionExpectation ](#ApiClient.ExpectationApi.CreateMatrixAllExpressionExpectation)
  - [M CreateMatrixSingleExpectation ](#ApiClient.ExpectationApi.CreateMatrixSingleExpectation)
  - [M CreateNotPresentExpectation ](#ApiClient.ExpectationApi.CreateNotPresentExpectation)
  - [M CreateNumericExpectation ](#ApiClient.ExpectationApi.CreateNumericExpectation)
  - [M CreateNumericExpressionExpectation ](#ApiClient.ExpectationApi.CreateNumericExpressionExpectation)
  - [M CreatePresentExpectation ](#ApiClient.ExpectationApi.CreatePresentExpectation)
  - [M CreateStringExpectation ](#ApiClient.ExpectationApi.CreateStringExpectation)
  - [M CreateStringExpressionExpectation ](#ApiClient.ExpectationApi.CreateStringExpressionExpectation)
  - [M CreateStringListExpectation ](#ApiClient.ExpectationApi.CreateStringListExpectation)
  - [M CreateVectorAllExpectation ](#ApiClient.ExpectationApi.CreateVectorAllExpectation)
  - [M CreateVectorAllExpressionExpectation ](#ApiClient.ExpectationApi.CreateVectorAllExpressionExpectation)
  - [M CreateVectorSingleExpectation ](#ApiClient.ExpectationApi.CreateVectorSingleExpectation)

# API for Expectations[¶](#api-for-expectations "Link to this heading")

Part of the [Object based program API](objectApi.md#objectapi).

*class* ExpectationApi[¶](#ApiClient.ExpectationApi "Link to this definition")  
Returned by

- [`PackageApi.ExpectationApi`](PackageApi.md#ApiClient.PackageApi.ExpectationApi "ApiClient.PackageApi.ExpectationApi (Python attribute) — Returns the ExpectationApi namespace.")

CreateAudioExpectation()[¶](#ApiClient.ExpectationApi.CreateAudioExpectation "Link to this definition")  
Creates an audio expectation.

Returns:  The audio expectation

Return type:  [`AudioExpectation`](ExpectationApi/AudioExpectation.md#ApiClient.AudioExpectation "ApiClient.AudioExpectation (Python class) — ExpectationApi.CreateAudioExpectation")

CreateBinaryExpressionExpectation(*[expression](#ApiClient.ExpectationApi.CreateBinaryExpressionExpectation.expression "ApiClient.ExpectationApi.CreateBinaryExpressionExpectation.expression (Python parameter) — String expression")*)[¶](#ApiClient.ExpectationApi.CreateBinaryExpressionExpectation "Link to this definition")  
Creates a binary expectation to be used in TsEdiabas.

Parameters:  expression : str[¶](#ApiClient.ExpectationApi.CreateBinaryExpressionExpectation.expression "Permalink to this definition")  
String expression

Returns:  The binary expression expectation

Return type:  [`BinaryExpressionExpectation`](ExpectationApi/BinaryExpressionExpectation.md#ApiClient.BinaryExpressionExpectation "ApiClient.BinaryExpressionExpectation (Python class) — ExpectationApi.CreateBinaryExpressionExpectation")

CreateBitStreamExpectation()[¶](#ApiClient.ExpectationApi.CreateBitStreamExpectation "Link to this definition")  
Creates a bit stream expectation.

Returns:  Bit stream expectation

Return type:  [`BitStreamExpectation`](ExpectationApi/BitStreamExpectation.md#ApiClient.BitStreamExpectation "ApiClient.BitStreamExpectation (Python class) — ExpectationApi.CreateBitStreamExpectation")

CreateBitStreamExpressionExpectation(*[expression](#ApiClient.ExpectationApi.CreateBitStreamExpressionExpectation.expression "ApiClient.ExpectationApi.CreateBitStreamExpressionExpectation.expression (Python parameter) — The expression text")*)[¶](#ApiClient.ExpectationApi.CreateBitStreamExpressionExpectation "Link to this definition")  
Creates a bit stream expression expectation.

Parameters:  expression : str[¶](#ApiClient.ExpectationApi.CreateBitStreamExpressionExpectation.expression "Permalink to this definition")  
The expression text

Returns:  The bit stream expectation

Return type:  [`BitStreamExpressionExpectation`](ExpectationApi/BitStreamExpressionExpectation.md#ApiClient.BitStreamExpressionExpectation "ApiClient.BitStreamExpressionExpectation (Python class) — ExpectationApi.CreateBitStreamExpressionExpectation")

CreateBooleanExpectation(*[truthValue](#ApiClient.ExpectationApi.CreateBooleanExpectation.truthValue "ApiClient.ExpectationApi.CreateBooleanExpectation.truthValue (Python parameter) — The truth value of the expectation")*)[¶](#ApiClient.ExpectationApi.CreateBooleanExpectation "Link to this definition")  
Creates a boolean expectation.

Parameters:  truthValue : bool[¶](#ApiClient.ExpectationApi.CreateBooleanExpectation.truthValue "Permalink to this definition")  
The truth value of the expectation

Returns:  The boolean expression expectation

Return type:  [`BooleanExpectation`](ExpectationApi/BooleanExpectation.md#ApiClient.BooleanExpectation "ApiClient.BooleanExpectation (Python class) — ExpectationApi.CreateBooleanExpectation")

CreateByteStreamExpectation()[¶](#ApiClient.ExpectationApi.CreateByteStreamExpectation "Link to this definition")  
Creates a byte stream expectation.

Returns:  Byte stream expectation

Return type:  [`ByteStreamExpectation`](ExpectationApi/ByteStreamExpectation.md#ApiClient.ByteStreamExpectation "ApiClient.ByteStreamExpectation (Python class) — ExpectationApi.CreateByteStreamExpectation")

CreateByteStreamExpressionExpectation(*[expression](#ApiClient.ExpectationApi.CreateByteStreamExpressionExpectation.expression "ApiClient.ExpectationApi.CreateByteStreamExpressionExpectation.expression (Python parameter) — The expression text.")*)[¶](#ApiClient.ExpectationApi.CreateByteStreamExpressionExpectation "Link to this definition")  
Creates a byte stream expression expectation.

Parameters:  expression : str[¶](#ApiClient.ExpectationApi.CreateByteStreamExpressionExpectation.expression "Permalink to this definition")  
The expression text.

Returns:  The byte stream expectation

Return type:  [`ByteStreamExpressionExpectation`](ExpectationApi/ByteStreamExpressionExpectation.md#ApiClient.ByteStreamExpressionExpectation "ApiClient.ByteStreamExpressionExpectation (Python class) — ExpectationApi.CreateByteStreamExpressionExpectation")

CreateCurveAllExpectation(*[expectationObject](#ApiClient.ExpectationApi.CreateCurveAllExpectation.expectationObject "ApiClient.ExpectationApi.CreateCurveAllExpectation.expectationObject (Python parameter) — The expectation object")*)[¶](#ApiClient.ExpectationApi.CreateCurveAllExpectation "Link to this definition")  
Creates a curve expectation. All values of the curve have to fulfill the given expectation.

Parameters:  expectationObject[¶](#ApiClient.ExpectationApi.CreateCurveAllExpectation.expectationObject "Permalink to this definition")  
The expectation object

Returns:  The curve expectation

Return type:  [`CurveAllExpectation`](ExpectationApi/CurveAllExpectation.md#ApiClient.CurveAllExpectation "ApiClient.CurveAllExpectation (Python class) — Represents an expectation on all elements of a curve. All elements of the curve must fulfill the expectation for this curve expectation to be fulfilled.")

CreateCurveAllExpressionExpectation(*[expression](#ApiClient.ExpectationApi.CreateCurveAllExpressionExpectation.expression "ApiClient.ExpectationApi.CreateCurveAllExpressionExpectation.expression (Python parameter) — String expression")*)[¶](#ApiClient.ExpectationApi.CreateCurveAllExpressionExpectation "Link to this definition")  
Creates a curve expectation. All values of the curve have to fulfill the given expression.

Parameters:  expression : str[¶](#ApiClient.ExpectationApi.CreateCurveAllExpressionExpectation.expression "Permalink to this definition")  
String expression

Returns:  The curve expression expectation

Return type:  [`CurveAllExpectation`](ExpectationApi/CurveAllExpectation.md#ApiClient.CurveAllExpectation "ApiClient.CurveAllExpectation (Python class) — Represents an expectation on all elements of a curve. All elements of the curve must fulfill the expectation for this curve expectation to be fulfilled.")

CreateCurveSingleExpectation(*[dimension](#ApiClient.ExpectationApi.CreateCurveSingleExpectation.dimension "ApiClient.ExpectationApi.CreateCurveSingleExpectation.dimension (Python parameter) — Curve dimension")*)[¶](#ApiClient.ExpectationApi.CreateCurveSingleExpectation "Link to this definition")  
Creates a curve expectation.

Parameters:  dimension : int[¶](#ApiClient.ExpectationApi.CreateCurveSingleExpectation.dimension "Permalink to this definition")  
Curve dimension

Returns:  The curve expectation

Return type:  [`CurveSingleExpectation`](ExpectationApi/CurveSingleExpectation.md#ApiClient.CurveSingleExpectation "ApiClient.CurveSingleExpectation (Python class) — Represents a sparse curve of expectations. Each element of the curve represents an individual expectation on the respective value. All individual expectations must be fulfilled in order for the this curve expectation to be fulfilled.")

CreateDTCListExpectation()[¶](#ApiClient.ExpectationApi.CreateDTCListExpectation "Link to this definition")  
Creates a DTC list expectation.

Returns:  DTC list expectation, initialized with default values

Return type:  [`DTCListExpectation`](ExpectationApi/DTCListExpectation.md#ApiClient.DTCListExpectation "ApiClient.DTCListExpectation (Python class) — ExpectationApi.CreateDTCListExpectation")

CreateExpressionExpectation(*[expression](#ApiClient.ExpectationApi.CreateExpressionExpectation.expression "ApiClient.ExpectationApi.CreateExpressionExpectation.expression (Python parameter) — Optional.")=`None`*)[¶](#ApiClient.ExpectationApi.CreateExpressionExpectation "Link to this definition")  
Creates an unspecific expression expectation.

Parameters:  expression : str[¶](#ApiClient.ExpectationApi.CreateExpressionExpectation.expression "Permalink to this definition")  
Optional. The expression text.

Returns:  The unspecific expression expectation

Return type:  [`ExpressionExpectation`](ExpectationApi/ExpressionExpectation.md#ApiClient.ExpressionExpectation "ApiClient.ExpressionExpectation (Python class) — ExpectationApi.CreateExpressionExpectation")

CreateImageExpectation()[¶](#ApiClient.ExpectationApi.CreateImageExpectation "Link to this definition")  
Creates an image expectation.

Returns:  The image expectation

Return type:  [`ImageExpectation`](ExpectationApi/ImageExpectation.md#ApiClient.ImageExpectation "ApiClient.ImageExpectation (Python class) — ExpectationApi.CreateImageExpectation")

CreateMapAllExpectation(*[expectationObject](#ApiClient.ExpectationApi.CreateMapAllExpectation.expectationObject "ApiClient.ExpectationApi.CreateMapAllExpectation.expectationObject (Python parameter) — The expectation object")*)[¶](#ApiClient.ExpectationApi.CreateMapAllExpectation "Link to this definition")  
Creates a map expectation. All values of the map have to fulfill the given expectation.

Parameters:  expectationObject[¶](#ApiClient.ExpectationApi.CreateMapAllExpectation.expectationObject "Permalink to this definition")  
The expectation object

Returns:  The map expectation

Return type:  [`MapAllExpectation`](ExpectationApi/MapAllExpectation.md#ApiClient.MapAllExpectation "ApiClient.MapAllExpectation (Python class) — Represents an expectation on all elements of a map. All elements of the map must fulfill the expectation for this map expectation to be fulfilled.")

CreateMapAllExpressionExpectation(*[expression](#ApiClient.ExpectationApi.CreateMapAllExpressionExpectation.expression "ApiClient.ExpectationApi.CreateMapAllExpressionExpectation.expression (Python parameter) — String expression")*)[¶](#ApiClient.ExpectationApi.CreateMapAllExpressionExpectation "Link to this definition")  
Creates a map expectation. All values of the map have to fulfill the given expression.

Parameters:  expression : str[¶](#ApiClient.ExpectationApi.CreateMapAllExpressionExpectation.expression "Permalink to this definition")  
String expression

Returns:  The map expectation

Return type:  [`MapAllExpectation`](ExpectationApi/MapAllExpectation.md#ApiClient.MapAllExpectation "ApiClient.MapAllExpectation (Python class) — Represents an expectation on all elements of a map. All elements of the map must fulfill the expectation for this map expectation to be fulfilled.")

CreateMapSingleExpectation(*[xDimension](#ApiClient.ExpectationApi.CreateMapSingleExpectation.xDimension "ApiClient.ExpectationApi.CreateMapSingleExpectation.xDimension (Python parameter) — Map x-axis dimension")*, *[yDimension](#ApiClient.ExpectationApi.CreateMapSingleExpectation.yDimension "ApiClient.ExpectationApi.CreateMapSingleExpectation.yDimension (Python parameter) — Map y-axis dimension")*)[¶](#ApiClient.ExpectationApi.CreateMapSingleExpectation "Link to this definition")  
Creates a map expectation.

Parameters:  xDimension : int[¶](#ApiClient.ExpectationApi.CreateMapSingleExpectation.xDimension "Permalink to this definition")  
Map x-axis dimension

yDimension : int[¶](#ApiClient.ExpectationApi.CreateMapSingleExpectation.yDimension "Permalink to this definition")  
Map y-axis dimension

Returns:  The map expectation

Return type:  [`MapSingleExpectation`](ExpectationApi/MapSingleExpectation.md#ApiClient.MapSingleExpectation "ApiClient.MapSingleExpectation (Python class) — Represents a sparse map of expectations. Each element of the map represents an individual expectation on the respective value. All individual expectations must be fulfilled in order for the this map expectation to be fulfilled.")

CreateMatrixAllExpectation(*[expectationObject](#ApiClient.ExpectationApi.CreateMatrixAllExpectation.expectationObject "ApiClient.ExpectationApi.CreateMatrixAllExpectation.expectationObject (Python parameter) — The expectation object")*)[¶](#ApiClient.ExpectationApi.CreateMatrixAllExpectation "Link to this definition")  
Creates a matrix expectation. All values of the matrix have to fulfill the given expectation.

Parameters:  expectationObject[¶](#ApiClient.ExpectationApi.CreateMatrixAllExpectation.expectationObject "Permalink to this definition")  
The expectation object

Returns:  The matrix expectation

Return type:  [`MatrixAllExpectation`](ExpectationApi/MatrixAllExpectation.md#ApiClient.MatrixAllExpectation "ApiClient.MatrixAllExpectation (Python class) — Represents an expectation on all elements of a matrix. All elements of the matrix must fulfill the expectation for this matrix expectation to be fulfilled.")

CreateMatrixAllExpressionExpectation(*[expression](#ApiClient.ExpectationApi.CreateMatrixAllExpressionExpectation.expression "ApiClient.ExpectationApi.CreateMatrixAllExpressionExpectation.expression (Python parameter) — String expression")*)[¶](#ApiClient.ExpectationApi.CreateMatrixAllExpressionExpectation "Link to this definition")  
Creates a matrix expectation. All values of the matrix have to fulfill the given expression.

Parameters:  expression : str[¶](#ApiClient.ExpectationApi.CreateMatrixAllExpressionExpectation.expression "Permalink to this definition")  
String expression

Returns:  The matrix expression expectation

Return type:  [`MatrixAllExpectation`](ExpectationApi/MatrixAllExpectation.md#ApiClient.MatrixAllExpectation "ApiClient.MatrixAllExpectation (Python class) — Represents an expectation on all elements of a matrix. All elements of the matrix must fulfill the expectation for this matrix expectation to be fulfilled.")

CreateMatrixSingleExpectation(*[xDimension](#ApiClient.ExpectationApi.CreateMatrixSingleExpectation.xDimension "ApiClient.ExpectationApi.CreateMatrixSingleExpectation.xDimension (Python parameter) — Matrix x-axis dimension")*, *[yDimension](#ApiClient.ExpectationApi.CreateMatrixSingleExpectation.yDimension "ApiClient.ExpectationApi.CreateMatrixSingleExpectation.yDimension (Python parameter) — Matrix y-axis dimension")*)[¶](#ApiClient.ExpectationApi.CreateMatrixSingleExpectation "Link to this definition")  
Creates a matrix expectation.

Parameters:  xDimension : int[¶](#ApiClient.ExpectationApi.CreateMatrixSingleExpectation.xDimension "Permalink to this definition")  
Matrix x-axis dimension

yDimension : int[¶](#ApiClient.ExpectationApi.CreateMatrixSingleExpectation.yDimension "Permalink to this definition")  
Matrix y-axis dimension

Returns:  The matrix expectation

Return type:  [`MatrixSingleExpectation`](ExpectationApi/MatrixSingleExpectation.md#ApiClient.MatrixSingleExpectation "ApiClient.MatrixSingleExpectation (Python class) — Represents a sparse matrix of expectations. Each element of the matrix represents an individual expectation on the respective value. All individual expectations must be fulfilled in order for the this matrix expectation to be fulfilled.")

CreateNotPresentExpectation()[¶](#ApiClient.ExpectationApi.CreateNotPresentExpectation "Link to this definition")  
Creates a ~Not Present~ expectation.

Returns:  The NotPresent expectation

Return type:  [`NotPresentExpectation`](ExpectationApi/NotPresentExpectation.md#ApiClient.NotPresentExpectation "ApiClient.NotPresentExpectation (Python class) — ExpectationApi.CreateNotPresentExpectation")

CreateNumericExpectation()[¶](#ApiClient.ExpectationApi.CreateNumericExpectation "Link to this definition")  
Creates a numeric expectation.

Returns:  The numeric expectation

Return type:  [`NumericExpectation`](ExpectationApi/NumericExpectation.md#ApiClient.NumericExpectation "ApiClient.NumericExpectation (Python class) — ExpectationApi.CreateNumericExpectation")

CreateNumericExpressionExpectation(*[expression](#ApiClient.ExpectationApi.CreateNumericExpressionExpectation.expression "ApiClient.ExpectationApi.CreateNumericExpressionExpectation.expression (Python parameter) — Optional.")=`None`*)[¶](#ApiClient.ExpectationApi.CreateNumericExpressionExpectation "Link to this definition")  
Creates a manual numeric expectation.

Parameters:  expression : str[¶](#ApiClient.ExpectationApi.CreateNumericExpressionExpectation.expression "Permalink to this definition")  
Optional. The expression text.

Returns:  The numeric expectation

Return type:  [`NumericExpressionExpectation`](ExpectationApi/NumericExpressionExpectation.md#ApiClient.NumericExpressionExpectation "ApiClient.NumericExpressionExpectation (Python class) — ExpectationApi.CreateNumericExpressionExpectation")

CreatePresentExpectation()[¶](#ApiClient.ExpectationApi.CreatePresentExpectation "Link to this definition")  
Creates a ~Present~ expectation.

Returns:  The Present expectation

Return type:  [`PresentExpectation`](ExpectationApi/PresentExpectation.md#ApiClient.PresentExpectation "ApiClient.PresentExpectation (Python class) — ExpectationApi.CreatePresentExpectation")

CreateStringExpectation()[¶](#ApiClient.ExpectationApi.CreateStringExpectation "Link to this definition")  
Creates a string expectation.

Returns:  The string expectation

Return type:  [`StringExpectation`](ExpectationApi/StringExpectation.md#ApiClient.StringExpectation "ApiClient.StringExpectation (Python class) — ExpectationApi.CreateStringExpectation")

CreateStringExpressionExpectation(*[expression](#ApiClient.ExpectationApi.CreateStringExpressionExpectation.expression "ApiClient.ExpectationApi.CreateStringExpressionExpectation.expression (Python parameter) — Optional.")=`None`*)[¶](#ApiClient.ExpectationApi.CreateStringExpressionExpectation "Link to this definition")  
Creates a string expression expectation.

Parameters:  expression : str[¶](#ApiClient.ExpectationApi.CreateStringExpressionExpectation.expression "Permalink to this definition")  
Optional. The expression text.

Returns:  The string expression expectation

Return type:  [`StringExpressionExpectation`](ExpectationApi/StringExpressionExpectation.md#ApiClient.StringExpressionExpectation "ApiClient.StringExpressionExpectation (Python class) — ExpectationApi.CreateStringExpressionExpectation")

CreateStringListExpectation()[¶](#ApiClient.ExpectationApi.CreateStringListExpectation "Link to this definition")  
Creates a string list expectation.

Returns:  The string list expectation

Return type:  [`StringListExpectation`](ExpectationApi/StringListExpectation.md#ApiClient.StringListExpectation "ApiClient.StringListExpectation (Python class) — ExpectationApi.CreateStringListExpectation")

CreateVectorAllExpectation(*[expectationObject](#ApiClient.ExpectationApi.CreateVectorAllExpectation.expectationObject "ApiClient.ExpectationApi.CreateVectorAllExpectation.expectationObject (Python parameter) — The expectation object")*)[¶](#ApiClient.ExpectationApi.CreateVectorAllExpectation "Link to this definition")  
Creates a vector expectation. All values of the vector have to fulfill the given expectation.

Parameters:  expectationObject[¶](#ApiClient.ExpectationApi.CreateVectorAllExpectation.expectationObject "Permalink to this definition")  
The expectation object

Returns:  The vector expectation

Return type:  [`VectorAllExpectation`](ExpectationApi/VectorAllExpectation.md#ApiClient.VectorAllExpectation "ApiClient.VectorAllExpectation (Python class) — Represents an expectation on all elements of a vector. All elements of the vector must fulfill the expectation for this vector expectation to be fulfilled.")

CreateVectorAllExpressionExpectation(*[expression](#ApiClient.ExpectationApi.CreateVectorAllExpressionExpectation.expression "ApiClient.ExpectationApi.CreateVectorAllExpressionExpectation.expression (Python parameter) — String expression")*)[¶](#ApiClient.ExpectationApi.CreateVectorAllExpressionExpectation "Link to this definition")  
Creates a vector expectation. All values of the vector have to fulfill the given expression.

Parameters:  expression : str[¶](#ApiClient.ExpectationApi.CreateVectorAllExpressionExpectation.expression "Permalink to this definition")  
String expression

Returns:  The vector expectation

Return type:  [`VectorAllExpectation`](ExpectationApi/VectorAllExpectation.md#ApiClient.VectorAllExpectation "ApiClient.VectorAllExpectation (Python class) — Represents an expectation on all elements of a vector. All elements of the vector must fulfill the expectation for this vector expectation to be fulfilled.")

CreateVectorSingleExpectation(*[dimension](#ApiClient.ExpectationApi.CreateVectorSingleExpectation.dimension "ApiClient.ExpectationApi.CreateVectorSingleExpectation.dimension (Python parameter) — Vector dimension")*)[¶](#ApiClient.ExpectationApi.CreateVectorSingleExpectation "Link to this definition")  
Creates a vector expectation.

Parameters:  dimension : int[¶](#ApiClient.ExpectationApi.CreateVectorSingleExpectation.dimension "Permalink to this definition")  
Vector dimension

Returns:  The vector expectation

Return type:  [`VectorSingleExpectation`](ExpectationApi/VectorSingleExpectation.md#ApiClient.VectorSingleExpectation "ApiClient.VectorSingleExpectation (Python class) — Represents a sparse vector of expectations. Each element of the vector represents an individual expectation on the respective value. All individual expectations must be fulfilled in order for the this vector expectation to be fulfilled.")

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
