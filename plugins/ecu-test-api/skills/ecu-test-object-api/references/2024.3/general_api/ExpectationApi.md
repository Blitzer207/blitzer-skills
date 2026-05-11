# API for Expectations[¶](#api-for-expectations "Link to this heading")

Part of the [Object based program API](objectApi.md#objectapi)

## ExpectationApi[¶](#expectationapi "Link to this heading")

*class* ExpectationApi[¶](#ApiClient.ExpectationApi "Link to this definition")  
Returned by

- [`PackageApi.ExpectationApi`](PackageApi.md#ApiClient.PackageApi.ExpectationApi "ApiClient.PackageApi.ExpectationApi")

CreateAudioExpectation()[¶](#ApiClient.ExpectationApi.CreateAudioExpectation "Link to this definition")  
Creates an audio expectation.

Returns:  The audio expectation

Return type:  [`AudioExpectation`](#ApiClient.AudioExpectation "ApiClient.AudioExpectation")

CreateBinaryExpressionExpectation(*expression*)[¶](#ApiClient.ExpectationApi.CreateBinaryExpressionExpectation "Link to this definition")  
Creates a binary expectation to be used in TsEdiabas.

Parameters:  **expression** (*str*) – String expression

Returns:  The binary expression expectation

Return type:  [`BinaryExpressionExpectation`](#ApiClient.BinaryExpressionExpectation "ApiClient.BinaryExpressionExpectation")

CreateBitStreamExpectation()[¶](#ApiClient.ExpectationApi.CreateBitStreamExpectation "Link to this definition")  
Creates a bit stream expectation.

Returns:  Bit stream expectation

Return type:  [`BitStreamExpectation`](#ApiClient.BitStreamExpectation "ApiClient.BitStreamExpectation")

CreateBitStreamExpressionExpectation(*expression*)[¶](#ApiClient.ExpectationApi.CreateBitStreamExpressionExpectation "Link to this definition")  
Creates a bit stream expression expectation.

Parameters:  **expression** (*str*) – The expression text

Returns:  The bit stream expectation

Return type:  [`BitStreamExpressionExpectation`](#ApiClient.BitStreamExpressionExpectation "ApiClient.BitStreamExpressionExpectation")

CreateBooleanExpectation(*truthValue*)[¶](#ApiClient.ExpectationApi.CreateBooleanExpectation "Link to this definition")  
Creates a boolean expectation.

Parameters:  **truthValue** (*bool*) – The truth value of the expectation

Returns:  The boolean expression expectation

Return type:  [`BooleanExpectation`](#ApiClient.BooleanExpectation "ApiClient.BooleanExpectation")

CreateByteStreamExpectation()[¶](#ApiClient.ExpectationApi.CreateByteStreamExpectation "Link to this definition")  
Creates a byte stream expectation.

Returns:  Byte stream expectation

Return type:  [`ByteStreamExpectation`](#ApiClient.ByteStreamExpectation "ApiClient.ByteStreamExpectation")

CreateByteStreamExpressionExpectation(*expression*)[¶](#ApiClient.ExpectationApi.CreateByteStreamExpressionExpectation "Link to this definition")  
Creates a byte stream expression expectation.

Parameters:  **expression** (*str*) – The expression text.

Returns:  The byte stream expectation

Return type:  [`ByteStreamExpressionExpectation`](#ApiClient.ByteStreamExpressionExpectation "ApiClient.ByteStreamExpressionExpectation")

CreateCurveAllExpectation(*expectationObject*)[¶](#ApiClient.ExpectationApi.CreateCurveAllExpectation "Link to this definition")  
Creates a curve expectation. All values of the curve have to fulfill the given expectation.

Parameters:  **expectationObject** ([`Expectation`](#ApiClient.Expectation "ApiClient.Expectation")) – The expectation object

Returns:  The curve expectation

Return type:  [`CurveAllExpectation`](#ApiClient.CurveAllExpectation "ApiClient.CurveAllExpectation")

CreateCurveAllExpressionExpectation(*expression*)[¶](#ApiClient.ExpectationApi.CreateCurveAllExpressionExpectation "Link to this definition")  
Creates a curve expectation. All values of the curve have to fulfill the given expression.

Parameters:  **expression** (*str*) – String expression

Returns:  The curve expression expectation

Return type:  [`CurveAllExpectation`](#ApiClient.CurveAllExpectation "ApiClient.CurveAllExpectation")

CreateCurveSingleExpectation(*dimension*)[¶](#ApiClient.ExpectationApi.CreateCurveSingleExpectation "Link to this definition")  
Creates a curve expectation.

Parameters:  **dimension** (*int*) – Curve dimension

Returns:  The curve expectation

Return type:  [`CurveSingleExpectation`](#ApiClient.CurveSingleExpectation "ApiClient.CurveSingleExpectation")

CreateDTCListExpectation()[¶](#ApiClient.ExpectationApi.CreateDTCListExpectation "Link to this definition")  
Creates a DTC list expectation.

Returns:  DTC list expectation, initialized with default values

Return type:  [`DTCListExpectation`](#ApiClient.DTCListExpectation "ApiClient.DTCListExpectation")

CreateExpressionExpectation(*expression=None*)[¶](#ApiClient.ExpectationApi.CreateExpressionExpectation "Link to this definition")  
Creates an unspecific expression expectation.

Parameters:  **expression** (*str*) – Optional. The expression text.

Returns:  The unspecific expression expectation

Return type:  [`ExpressionExpectation`](#ApiClient.ExpressionExpectation "ApiClient.ExpressionExpectation")

CreateImageExpectation()[¶](#ApiClient.ExpectationApi.CreateImageExpectation "Link to this definition")  
Creates an image expectation.

Returns:  The image expectation

Return type:  [`ImageExpectation`](#ApiClient.ImageExpectation "ApiClient.ImageExpectation")

CreateMapAllExpectation(*expectationObject*)[¶](#ApiClient.ExpectationApi.CreateMapAllExpectation "Link to this definition")  
Creates a map expectation. All values of the map have to fulfill the given expectation.

Parameters:  **expectationObject** ([`Expectation`](#ApiClient.Expectation "ApiClient.Expectation")) – The expectation object

Returns:  The map expectation

Return type:  [`MapAllExpectation`](#ApiClient.MapAllExpectation "ApiClient.MapAllExpectation")

CreateMapAllExpressionExpectation(*expression*)[¶](#ApiClient.ExpectationApi.CreateMapAllExpressionExpectation "Link to this definition")  
Creates a map expectation. All values of the map have to fulfill the given expression.

Parameters:  **expression** (*str*) – String expression

Returns:  The map expectation

Return type:  [`MapAllExpectation`](#ApiClient.MapAllExpectation "ApiClient.MapAllExpectation")

CreateMapSingleExpectation(*xDimension*, *yDimension*)[¶](#ApiClient.ExpectationApi.CreateMapSingleExpectation "Link to this definition")  
Creates a map expectation.

Parameters:  - **xDimension** (*int*) – Map x-axis dimension

- **yDimension** (*int*) – Map y-axis dimension

Returns:  The map expectation

Return type:  [`MapSingleExpectation`](#ApiClient.MapSingleExpectation "ApiClient.MapSingleExpectation")

CreateMatrixAllExpectation(*expectationObject*)[¶](#ApiClient.ExpectationApi.CreateMatrixAllExpectation "Link to this definition")  
Creates a matrix expectation. All values of the matrix have to fulfill the given expectation.

Parameters:  **expectationObject** ([`Expectation`](#ApiClient.Expectation "ApiClient.Expectation")) – The expectation object

Returns:  The matrix expectation

Return type:  [`MatrixAllExpectation`](#ApiClient.MatrixAllExpectation "ApiClient.MatrixAllExpectation")

CreateMatrixAllExpressionExpectation(*expression*)[¶](#ApiClient.ExpectationApi.CreateMatrixAllExpressionExpectation "Link to this definition")  
Creates a matrix expectation. All values of the matrix have to fulfill the given expression.

Parameters:  **expression** (*str*) – String expression

Returns:  The matrix expression expectation

Return type:  [`MatrixAllExpectation`](#ApiClient.MatrixAllExpectation "ApiClient.MatrixAllExpectation")

CreateMatrixSingleExpectation(*xDimension*, *yDimension*)[¶](#ApiClient.ExpectationApi.CreateMatrixSingleExpectation "Link to this definition")  
Creates a matrix expectation.

Parameters:  - **xDimension** (*int*) – Matrix x-axis dimension

- **yDimension** (*int*) – Matrix y-axis dimension

Returns:  The matrix expectation

Return type:  [`MatrixSingleExpectation`](#ApiClient.MatrixSingleExpectation "ApiClient.MatrixSingleExpectation")

CreateNotPresentExpectation()[¶](#ApiClient.ExpectationApi.CreateNotPresentExpectation "Link to this definition")  
Creates a ~Not Present~ expectation.

Returns:  The NotPresent expectation

Return type:  [`NotPresentExpectation`](#ApiClient.NotPresentExpectation "ApiClient.NotPresentExpectation")

CreateNumericExpectation()[¶](#ApiClient.ExpectationApi.CreateNumericExpectation "Link to this definition")  
Creates a numeric expectation.

Returns:  The numeric expectation

Return type:  [`NumericExpectation`](#ApiClient.NumericExpectation "ApiClient.NumericExpectation")

CreateNumericExpressionExpectation(*expression=None*)[¶](#ApiClient.ExpectationApi.CreateNumericExpressionExpectation "Link to this definition")  
Creates a manual numeric expectation.

Parameters:  **expression** (*str*) – Optional. The expression text.

Returns:  The numeric expectation

Return type:  [`NumericExpressionExpectation`](#ApiClient.NumericExpressionExpectation "ApiClient.NumericExpressionExpectation")

CreatePresentExpectation()[¶](#ApiClient.ExpectationApi.CreatePresentExpectation "Link to this definition")  
Creates a ~Present~ expectation.

Returns:  The Present expectation

Return type:  [`PresentExpectation`](#ApiClient.PresentExpectation "ApiClient.PresentExpectation")

CreateStringExpectation()[¶](#ApiClient.ExpectationApi.CreateStringExpectation "Link to this definition")  
Creates a string expectation.

Returns:  The string expectation

Return type:  [`StringExpectation`](#ApiClient.StringExpectation "ApiClient.StringExpectation")

CreateStringExpressionExpectation(*expression=None*)[¶](#ApiClient.ExpectationApi.CreateStringExpressionExpectation "Link to this definition")  
Creates a string expression expectation.

Parameters:  **expression** (*str*) – Optional. The expression text.

Returns:  The string expression expectation

Return type:  [`StringExpressionExpectation`](#ApiClient.StringExpressionExpectation "ApiClient.StringExpressionExpectation")

CreateStringListExpectation()[¶](#ApiClient.ExpectationApi.CreateStringListExpectation "Link to this definition")  
Creates a string list expectation.

Returns:  The string list expectation

Return type:  [`StringListExpectation`](#ApiClient.StringListExpectation "ApiClient.StringListExpectation")

CreateVectorAllExpectation(*expectationObject*)[¶](#ApiClient.ExpectationApi.CreateVectorAllExpectation "Link to this definition")  
Creates a vector expectation. All values of the vector have to fulfill the given expectation.

Parameters:  **expectationObject** ([`Expectation`](#ApiClient.Expectation "ApiClient.Expectation")) – The expectation object

Returns:  The vector expectation

Return type:  [`VectorAllExpectation`](#ApiClient.VectorAllExpectation "ApiClient.VectorAllExpectation")

CreateVectorAllExpressionExpectation(*expression*)[¶](#ApiClient.ExpectationApi.CreateVectorAllExpressionExpectation "Link to this definition")  
Creates a vector expectation. All values of the vector have to fulfill the given expression.

Parameters:  **expression** (*str*) – String expression

Returns:  The vector expectation

Return type:  [`VectorAllExpectation`](#ApiClient.VectorAllExpectation "ApiClient.VectorAllExpectation")

CreateVectorSingleExpectation(*dimension*)[¶](#ApiClient.ExpectationApi.CreateVectorSingleExpectation "Link to this definition")  
Creates a vector expectation.

Parameters:  **dimension** (*int*) – Vector dimension

Returns:  The vector expectation

Return type:  [`VectorSingleExpectation`](#ApiClient.VectorSingleExpectation "ApiClient.VectorSingleExpectation")

## AudioExpectation[¶](#audioexpectation "Link to this heading")

*class* AudioExpectation[¶](#ApiClient.AudioExpectation "Link to this definition")  
Base class

[`Expectation`](#ApiClient.Expectation "ApiClient.Expectation")

Returned by

- [`ExpectationApi.CreateAudioExpectation`](#ApiClient.ExpectationApi.CreateAudioExpectation "ApiClient.ExpectationApi.CreateAudioExpectation")

Clone()[¶](#ApiClient.AudioExpectation.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`AudioExpectation`](#ApiClient.AudioExpectation "ApiClient.AudioExpectation")

GetComparisonMethod()[¶](#ApiClient.AudioExpectation.GetComparisonMethod "Link to this definition")  
Returns the method that will be used to compare the two images.

Returns:  The method of comparison

Return type:  str

GetNoiseResistantComparison()[¶](#ApiClient.AudioExpectation.GetNoiseResistantComparison "Link to this definition")  
Returns whether a noise resistant comparison method will be used.

Returns:  True if a noise resistant comparison is used. False otherwise.

Return type:  bool

GetReference()[¶](#ApiClient.AudioExpectation.GetReference "Link to this definition")  
Returns the current audio reference expression. Depending on the reference type, this can be the path to an audio file or the name of a variable.

Returns:  Path to an audio file or name of a variable.

Return type:  str

GetReferenceType()[¶](#ApiClient.AudioExpectation.GetReferenceType "Link to this definition")  
Returns the method by which the audio reference is resolved.

Returns:  The type of reference

Return type:  str

GetThreshold()[¶](#ApiClient.AudioExpectation.GetThreshold "Link to this definition")  
Returns the minimum confidence value used during comparison.

Returns:  The threhold expression

Return type:  str

SetComparisonMethod(*comparisonMethod*)[¶](#ApiClient.AudioExpectation.SetComparisonMethod "Link to this definition")  
Sets the method that will be used to compare the two audio blocks.

Parameters:  **comparisonMethod** (*str*) – Either “contains” or “containsNot”

SetNoiseResistantComparison(*noiseResistantComparison*)[¶](#ApiClient.AudioExpectation.SetNoiseResistantComparison "Link to this definition")  
Specifies whether the audio samples should be campared with an algorithm that is designed to be resistant to noise. This option should only be activated if the recording actually contains noise. For recordings without noise the normal comparison provides more robust results. Pleae note that the confidence values will generally be lower when using the noise resistant comparison since a different metric will be used.

Parameters:  **noiseResistantComparison** (*bool*) – Whether to activate the noise resistant comparison.

SetReference(*reference*)[¶](#ApiClient.AudioExpectation.SetReference "Link to this definition")  
Sets the current audio reference expression. Depending on the configured reference type this may be either a path to an audio file or the name of an AudioBlock variable.

Parameters:  **reference** (*str*) – Path to an audio file or name of a variable.

SetReferenceType(*referenceType*)[¶](#ApiClient.AudioExpectation.SetReferenceType "Link to this definition")  
Sets how the audio is referenced. If the type is set to “object”, the reference expression is expected to contain a variable name. The variable must contain an AudioBlock. If the type is set to “workspace” the reference should contain a path relative to the current workspace. The actual audio reference expression can be set with `SetReference()`.

Parameters:  **referenceType** (*str*) – Either “object” or “workspace”

SetThreshold(*threshold*)[¶](#ApiClient.AudioExpectation.SetThreshold "Link to this definition")  
Sets the minimum confidence value that a match should have to be considered a match. Only if the reference sample is found with a confidence higher than the given threshold will the test step be evaluated with SUCCES.

Parameters:  **threshold** (*str*) – Expression for the confidence threshold

## BinaryExpressionExpectation[¶](#binaryexpressionexpectation "Link to this heading")

*class* BinaryExpressionExpectation[¶](#ApiClient.BinaryExpressionExpectation "Link to this definition")  
Base classes

- [`Expectation`](#ApiClient.Expectation "ApiClient.Expectation")

- [`ExpressionExpectationBase`](#ApiClient.ExpressionExpectationBase "ApiClient.ExpressionExpectationBase")

Returned by

- [`ExpectationApi.CreateBinaryExpressionExpectation`](#ApiClient.ExpectationApi.CreateBinaryExpressionExpectation "ApiClient.ExpectationApi.CreateBinaryExpressionExpectation")

Clone()[¶](#ApiClient.BinaryExpressionExpectation.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`BinaryExpressionExpectation`](#ApiClient.BinaryExpressionExpectation "ApiClient.BinaryExpressionExpectation")

GetExpression()[¶](#ApiClient.BinaryExpressionExpectation.GetExpression "Link to this definition")  
Returns the expectations expression.

Returns:  The expression

Return type:  str

SetExpression(*expression*)[¶](#ApiClient.BinaryExpressionExpectation.SetExpression "Link to this definition")  
Sets the expectations expression.

Parameters:  **expression** (*str*) – The expression

## BitStreamExpectation[¶](#bitstreamexpectation "Link to this heading")

*class* BitStreamExpectation[¶](#ApiClient.BitStreamExpectation "Link to this definition")  
Base class

[`Expectation`](#ApiClient.Expectation "ApiClient.Expectation")

Returned by

- [`ExpectationApi.CreateBitStreamExpectation`](#ApiClient.ExpectationApi.CreateBitStreamExpectation "ApiClient.ExpectationApi.CreateBitStreamExpectation")

Clone()[¶](#ApiClient.BitStreamExpectation.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`BitStreamExpectation`](#ApiClient.BitStreamExpectation "ApiClient.BitStreamExpectation")

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

Return type:  [`NumericExpectation`](#ApiClient.NumericExpectation "ApiClient.NumericExpectation")

RemoveSizeExpectation()[¶](#ApiClient.BitStreamExpectation.RemoveSizeExpectation "Link to this definition")  
Removes the size expectation.

SetExpression(*expression*)[¶](#ApiClient.BitStreamExpectation.SetExpression "Link to this definition")  
Sets the expectation expression.

Parameters:  **expression** (*str*) – The expectation expression, e.g. ‘BitStream(0x0, 32)’

SetMaskExpression(*expression*)[¶](#ApiClient.BitStreamExpectation.SetMaskExpression "Link to this definition")  
Sets the mask expression.

Parameters:  **expression** (*str*) – The mask expression, e.g. ‘BitStream(0x0, 32)’

SetSizeExpectation(*expectation*)[¶](#ApiClient.BitStreamExpectation.SetSizeExpectation "Link to this definition")  
Sets the size expectation.

Parameters:  **expectation** ([`NumericExpectation`](#ApiClient.NumericExpectation "ApiClient.NumericExpectation")) – The numeric expectation

## NumericExpectation[¶](#numericexpectation "Link to this heading")

*class* NumericExpectation[¶](#ApiClient.NumericExpectation "Link to this definition")  
Base class

[`Expectation`](#ApiClient.Expectation "ApiClient.Expectation")

Returned by

- [`BitStreamExpectation.GetSizeExpectation`](#ApiClient.BitStreamExpectation.GetSizeExpectation "ApiClient.BitStreamExpectation.GetSizeExpectation")

- [`ExpectationApi.CreateNumericExpectation`](#ApiClient.ExpectationApi.CreateNumericExpectation "ApiClient.ExpectationApi.CreateNumericExpectation")

Clone()[¶](#ApiClient.NumericExpectation.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`NumericExpectation`](#ApiClient.NumericExpectation "ApiClient.NumericExpectation")

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

SetDontEvalNotPresent(*dontEvalNotPresent*)[¶](#ApiClient.NumericExpectation.SetDontEvalNotPresent "Link to this definition")  
Enables or disables the option to evaluate this expectation if the expected value is NotPresent.

Parameters:  **dontEvalNotPresent** (*boolean*) – True to enable the described behavior. False to disable it.

SetExpression(*expression*)[¶](#ApiClient.NumericExpectation.SetExpression "Link to this definition")  
Sets the expectations expression.

Parameters:  **expression** (*str*) – The expression

SetRelation(*relation*)[¶](#ApiClient.NumericExpectation.SetRelation "Link to this definition")  
Sets the relation for this expectation. Allowed values are:  
- ‘\<’

- ‘\<=’

- ‘==’

- ‘\>=’

- ‘\>’

- ‘!=’

- ‘\<\>’ (results in ‘!=’)

Parameters:  **relation** (*str*) – The relation

SetTolerance(*toleranceType*, *toleranceExpr*)[¶](#ApiClient.NumericExpectation.SetTolerance "Link to this definition")  
Sets the type and value of the tolerance for this expectation.

Parameters:  - **toleranceType** (*str*) – Possible types are: - ‘absolute-value’ - ‘percentage’ - ‘decimal-places’

- **toleranceExpr** (*str*) – The expression for the tolerance

## BitStreamExpressionExpectation[¶](#bitstreamexpressionexpectation "Link to this heading")

*class* BitStreamExpressionExpectation[¶](#ApiClient.BitStreamExpressionExpectation "Link to this definition")  
Base classes

- [`Expectation`](#ApiClient.Expectation "ApiClient.Expectation")

- [`ExpressionExpectationBase`](#ApiClient.ExpressionExpectationBase "ApiClient.ExpressionExpectationBase")

Returned by

- [`ExpectationApi.CreateBitStreamExpressionExpectation`](#ApiClient.ExpectationApi.CreateBitStreamExpressionExpectation "ApiClient.ExpectationApi.CreateBitStreamExpressionExpectation")

Clone()[¶](#ApiClient.BitStreamExpressionExpectation.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`BitStreamExpressionExpectation`](#ApiClient.BitStreamExpressionExpectation "ApiClient.BitStreamExpressionExpectation")

GetExpression()[¶](#ApiClient.BitStreamExpressionExpectation.GetExpression "Link to this definition")  
Returns the expectations expression.

Returns:  The expression

Return type:  str

SetExpression(*expression*)[¶](#ApiClient.BitStreamExpressionExpectation.SetExpression "Link to this definition")  
Sets the expectations expression.

Parameters:  **expression** (*str*) – The expression

## BooleanExpectation[¶](#booleanexpectation "Link to this heading")

*class* BooleanExpectation[¶](#ApiClient.BooleanExpectation "Link to this definition")  
Base classes

- [`Expectation`](#ApiClient.Expectation "ApiClient.Expectation")

- [`ExpressionExpectationBase`](#ApiClient.ExpressionExpectationBase "ApiClient.ExpressionExpectationBase")

Returned by

- [`ExpectationApi.CreateBooleanExpectation`](#ApiClient.ExpectationApi.CreateBooleanExpectation "ApiClient.ExpectationApi.CreateBooleanExpectation")

Clone()[¶](#ApiClient.BooleanExpectation.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`BooleanExpectation`](#ApiClient.BooleanExpectation "ApiClient.BooleanExpectation")

GetExpression()[¶](#ApiClient.BooleanExpectation.GetExpression "Link to this definition")  
Returns the expectations expression.

Returns:  The expression

Return type:  str

GetValue()[¶](#ApiClient.BooleanExpectation.GetValue "Link to this definition")  
Returns the truth value.

Returns:  The truth value

Return type:  boolean

SetExpression(*expression*)[¶](#ApiClient.BooleanExpectation.SetExpression "Link to this definition")  
Sets the expectations expression. Allowed expressions: ‘value’ for boolean True and ‘not value’ for boolean False.

Parameters:  **expression** (*str*) – The expression

SetValue(*truthValue*)[¶](#ApiClient.BooleanExpectation.SetValue "Link to this definition")  
Sets the truth value.

Parameters:  **truthValue** (*boolean*) – The new truth value

## ByteStreamExpectation[¶](#bytestreamexpectation "Link to this heading")

*class* ByteStreamExpectation[¶](#ApiClient.ByteStreamExpectation "Link to this definition")  
Base class

[`Expectation`](#ApiClient.Expectation "ApiClient.Expectation")

Returned by

- [`ExpectationApi.CreateByteStreamExpectation`](#ApiClient.ExpectationApi.CreateByteStreamExpectation "ApiClient.ExpectationApi.CreateByteStreamExpectation")

Clone()[¶](#ApiClient.ByteStreamExpectation.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`ByteStreamExpectation`](#ApiClient.ByteStreamExpectation "ApiClient.ByteStreamExpectation")

GetExpression()[¶](#ApiClient.ByteStreamExpectation.GetExpression "Link to this definition")  
Returns the expectation expression.

Returns:  The expectation expression

Return type:  str

GetMaskExpression()[¶](#ApiClient.ByteStreamExpectation.GetMaskExpression "Link to this definition")  
Returns the mask expression.

Returns:  The mask expression

Return type:  str

SetExpression(*expression*)[¶](#ApiClient.ByteStreamExpectation.SetExpression "Link to this definition")  
Sets the expectation expression.

Parameters:  **expression** (*str*) – The expectation expression, e.g. “ByteStream(‘00:00:00:00:00:00:00:00’)”

SetMaskExpression(*expression*)[¶](#ApiClient.ByteStreamExpectation.SetMaskExpression "Link to this definition")  
Sets the mask expression.

Parameters:  **expression** (*str*) – The mask expression, e.g. “ByteStream(‘FF:FF:FF:FF:FF:FF:FF:FF’)”

## ByteStreamExpressionExpectation[¶](#bytestreamexpressionexpectation "Link to this heading")

*class* ByteStreamExpressionExpectation[¶](#ApiClient.ByteStreamExpressionExpectation "Link to this definition")  
Base classes

- [`Expectation`](#ApiClient.Expectation "ApiClient.Expectation")

- [`ExpressionExpectationBase`](#ApiClient.ExpressionExpectationBase "ApiClient.ExpressionExpectationBase")

Returned by

- [`ExpectationApi.CreateByteStreamExpressionExpectation`](#ApiClient.ExpectationApi.CreateByteStreamExpressionExpectation "ApiClient.ExpectationApi.CreateByteStreamExpressionExpectation")

Clone()[¶](#ApiClient.ByteStreamExpressionExpectation.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`ByteStreamExpressionExpectation`](#ApiClient.ByteStreamExpressionExpectation "ApiClient.ByteStreamExpressionExpectation")

GetExpression()[¶](#ApiClient.ByteStreamExpressionExpectation.GetExpression "Link to this definition")  
Returns the expectations expression.

Returns:  The expression

Return type:  str

SetExpression(*expression*)[¶](#ApiClient.ByteStreamExpressionExpectation.SetExpression "Link to this definition")  
Sets the expectations expression.

Parameters:  **expression** (*str*) – The expression

## CurveAllExpectation[¶](#curveallexpectation "Link to this heading")

*class* CurveAllExpectation[¶](#ApiClient.CurveAllExpectation "Link to this definition")  
Represents an expectation on all elements of a curve. All elements of the curve must fulfill the expectation for this curve expectation to be fulfilled.

The expectation is specified as a Boolean expression in Python syntax. The special identifier “value” refers to the actual value of each curve element.

Base classes

- [`Expectation`](#ApiClient.Expectation "ApiClient.Expectation")

- [`AllExpectation`](#ApiClient.AllExpectation "ApiClient.AllExpectation")

Returned by

- [`ExpectationApi.CreateCurveAllExpectation`](#ApiClient.ExpectationApi.CreateCurveAllExpectation "ApiClient.ExpectationApi.CreateCurveAllExpectation")

- [`ExpectationApi.CreateCurveAllExpressionExpectation`](#ApiClient.ExpectationApi.CreateCurveAllExpressionExpectation "ApiClient.ExpectationApi.CreateCurveAllExpressionExpectation")

Clone()[¶](#ApiClient.CurveAllExpectation.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`CurveAllExpectation`](#ApiClient.CurveAllExpectation "ApiClient.CurveAllExpectation")

GetExpectation()[¶](#ApiClient.CurveAllExpectation.GetExpectation "Link to this definition")  
Returns the expectation object.

Returns:  The expectation object

Return type:  [`Expectation`](#ApiClient.Expectation "ApiClient.Expectation")

GetExpectationExpression()[¶](#ApiClient.CurveAllExpectation.GetExpectationExpression "Link to this definition")  
Returns the expectation expression.

Returns:  The expression

Return type:  str

SetExpectation(*expectationObject*)[¶](#ApiClient.CurveAllExpectation.SetExpectation "Link to this definition")  
Sets the expectation object.

Parameters:  **expectationObject** ([`Expectation`](#ApiClient.Expectation "ApiClient.Expectation")) – The expectation object

SetExpectationExpression(*expression*)[¶](#ApiClient.CurveAllExpectation.SetExpectationExpression "Link to this definition")  
Sets the expectation expression.

Parameters:  **expression** (*str*) – The expression

## Expectation[¶](#expectation "Link to this heading")

*class* Expectation[¶](#ApiClient.Expectation "Link to this definition")  
Returned by

- [`AllExpectation.GetExpectation`](#ApiClient.AllExpectation.GetExpectation "ApiClient.AllExpectation.GetExpectation")

- [`Calculation.GetExpectation`](TraceAnalysisApi.md#ApiClient.Calculation.GetExpectation "ApiClient.Calculation.GetExpectation")

- [`CurveAllExpectation.GetExpectation`](#ApiClient.CurveAllExpectation.GetExpectation "ApiClient.CurveAllExpectation.GetExpectation")

- [`CurveSingleExpectation.GetDistributionExpectation`](#ApiClient.CurveSingleExpectation.GetDistributionExpectation "ApiClient.CurveSingleExpectation.GetDistributionExpectation")

- [`CurveSingleExpectation.GetExpectation`](#ApiClient.CurveSingleExpectation.GetExpectation "ApiClient.CurveSingleExpectation.GetExpectation")

- [`EdiabasResult.GetExpectation`](TestStepApi.md#ApiClient.EdiabasResult.GetExpectation "ApiClient.EdiabasResult.GetExpectation")

- [`MapAllExpectation.GetExpectation`](#ApiClient.MapAllExpectation.GetExpectation "ApiClient.MapAllExpectation.GetExpectation")

- [`MapSingleExpectation.GetExpectation`](#ApiClient.MapSingleExpectation.GetExpectation "ApiClient.MapSingleExpectation.GetExpectation")

- [`MapSingleExpectation.GetXDistributionExpectation`](#ApiClient.MapSingleExpectation.GetXDistributionExpectation "ApiClient.MapSingleExpectation.GetXDistributionExpectation")

- [`MapSingleExpectation.GetYDistributionExpectation`](#ApiClient.MapSingleExpectation.GetYDistributionExpectation "ApiClient.MapSingleExpectation.GetYDistributionExpectation")

- [`MatrixAllExpectation.GetExpectation`](#ApiClient.MatrixAllExpectation.GetExpectation "ApiClient.MatrixAllExpectation.GetExpectation")

- [`MatrixSingleExpectation.GetExpectation`](#ApiClient.MatrixSingleExpectation.GetExpectation "ApiClient.MatrixSingleExpectation.GetExpectation")

- [`Return.GetExpectation`](TestStepApi.md#ApiClient.Return.GetExpectation "ApiClient.Return.GetExpectation")

- [`TsBusFirstSignalCheck.GetExpectation`](TestStepApi.md#ApiClient.TsBusFirstSignalCheck.GetExpectation "ApiClient.TsBusFirstSignalCheck.GetExpectation")

- [`TsCalculation.GetExpectation`](TestStepApi.md#ApiClient.TsCalculation.GetExpectation "ApiClient.TsCalculation.GetExpectation")

- [`TsCall.GetPacketExpectation`](TestStepApi.md#ApiClient.TsCall.GetPacketExpectation "ApiClient.TsCall.GetPacketExpectation")

- [`TsCall.GetReturnValueExpectation`](TestStepApi.md#ApiClient.TsCall.GetReturnValueExpectation "ApiClient.TsCall.GetReturnValueExpectation")

- [`TsCallDiagService.GetPacketExpectation`](TestStepApi.md#ApiClient.TsCallDiagService.GetPacketExpectation "ApiClient.TsCallDiagService.GetPacketExpectation")

- [`TsCallDiagService.GetReturnValueExpectation`](TestStepApi.md#ApiClient.TsCallDiagService.GetReturnValueExpectation "ApiClient.TsCallDiagService.GetReturnValueExpectation")

- [`TsCallIOControl.GetPacketExpectation`](TestStepApi.md#ApiClient.TsCallIOControl.GetPacketExpectation "ApiClient.TsCallIOControl.GetPacketExpectation")

- [`TsCallIOControl.GetReturnValueExpectation`](TestStepApi.md#ApiClient.TsCallIOControl.GetReturnValueExpectation "ApiClient.TsCallIOControl.GetReturnValueExpectation")

- [`TsCallIOControlFreezeCurrentState.GetPacketExpectation`](TestStepApi.md#ApiClient.TsCallIOControlFreezeCurrentState.GetPacketExpectation "ApiClient.TsCallIOControlFreezeCurrentState.GetPacketExpectation")

- [`TsCallIOControlFreezeCurrentState.GetReturnValueExpectation`](TestStepApi.md#ApiClient.TsCallIOControlFreezeCurrentState.GetReturnValueExpectation "ApiClient.TsCallIOControlFreezeCurrentState.GetReturnValueExpectation")

- [`TsCallIOControlISOSAEReserved.GetPacketExpectation`](TestStepApi.md#ApiClient.TsCallIOControlISOSAEReserved.GetPacketExpectation "ApiClient.TsCallIOControlISOSAEReserved.GetPacketExpectation")

- [`TsCallIOControlISOSAEReserved.GetReturnValueExpectation`](TestStepApi.md#ApiClient.TsCallIOControlISOSAEReserved.GetReturnValueExpectation "ApiClient.TsCallIOControlISOSAEReserved.GetReturnValueExpectation")

- [`TsCallIOControlResetToDefault.GetPacketExpectation`](TestStepApi.md#ApiClient.TsCallIOControlResetToDefault.GetPacketExpectation "ApiClient.TsCallIOControlResetToDefault.GetPacketExpectation")

- [`TsCallIOControlResetToDefault.GetReturnValueExpectation`](TestStepApi.md#ApiClient.TsCallIOControlResetToDefault.GetReturnValueExpectation "ApiClient.TsCallIOControlResetToDefault.GetReturnValueExpectation")

- [`TsCallIOControlReturnControlToEcu.GetPacketExpectation`](TestStepApi.md#ApiClient.TsCallIOControlReturnControlToEcu.GetPacketExpectation "ApiClient.TsCallIOControlReturnControlToEcu.GetPacketExpectation")

- [`TsCallIOControlReturnControlToEcu.GetReturnValueExpectation`](TestStepApi.md#ApiClient.TsCallIOControlReturnControlToEcu.GetReturnValueExpectation "ApiClient.TsCallIOControlReturnControlToEcu.GetReturnValueExpectation")

- [`TsCallIOControlShortTermAdjustment.GetPacketExpectation`](TestStepApi.md#ApiClient.TsCallIOControlShortTermAdjustment.GetPacketExpectation "ApiClient.TsCallIOControlShortTermAdjustment.GetPacketExpectation")

- [`TsCallIOControlShortTermAdjustment.GetReturnValueExpectation`](TestStepApi.md#ApiClient.TsCallIOControlShortTermAdjustment.GetReturnValueExpectation "ApiClient.TsCallIOControlShortTermAdjustment.GetReturnValueExpectation")

- [`TsCallKwpIOControlFreeze.GetPacketExpectation`](TestStepApi.md#ApiClient.TsCallKwpIOControlFreeze.GetPacketExpectation "ApiClient.TsCallKwpIOControlFreeze.GetPacketExpectation")

- [`TsCallKwpIOControlFreeze.GetReturnValueExpectation`](TestStepApi.md#ApiClient.TsCallKwpIOControlFreeze.GetReturnValueExpectation "ApiClient.TsCallKwpIOControlFreeze.GetReturnValueExpectation")

- [`TsCallKwpIOControlLongTermAdjustment.GetPacketExpectation`](TestStepApi.md#ApiClient.TsCallKwpIOControlLongTermAdjustment.GetPacketExpectation "ApiClient.TsCallKwpIOControlLongTermAdjustment.GetPacketExpectation")

- [`TsCallKwpIOControlLongTermAdjustment.GetReturnValueExpectation`](TestStepApi.md#ApiClient.TsCallKwpIOControlLongTermAdjustment.GetReturnValueExpectation "ApiClient.TsCallKwpIOControlLongTermAdjustment.GetReturnValueExpectation")

- [`TsCallKwpIOControlReportCurrentState.GetPacketExpectation`](TestStepApi.md#ApiClient.TsCallKwpIOControlReportCurrentState.GetPacketExpectation "ApiClient.TsCallKwpIOControlReportCurrentState.GetPacketExpectation")

- [`TsCallKwpIOControlReportCurrentState.GetReturnValueExpectation`](TestStepApi.md#ApiClient.TsCallKwpIOControlReportCurrentState.GetReturnValueExpectation "ApiClient.TsCallKwpIOControlReportCurrentState.GetReturnValueExpectation")

- [`TsCallKwpIOControlResetToDefault.GetPacketExpectation`](TestStepApi.md#ApiClient.TsCallKwpIOControlResetToDefault.GetPacketExpectation "ApiClient.TsCallKwpIOControlResetToDefault.GetPacketExpectation")

- [`TsCallKwpIOControlResetToDefault.GetReturnValueExpectation`](TestStepApi.md#ApiClient.TsCallKwpIOControlResetToDefault.GetReturnValueExpectation "ApiClient.TsCallKwpIOControlResetToDefault.GetReturnValueExpectation")

- [`TsCallKwpIOControlReturnControlToEcu.GetPacketExpectation`](TestStepApi.md#ApiClient.TsCallKwpIOControlReturnControlToEcu.GetPacketExpectation "ApiClient.TsCallKwpIOControlReturnControlToEcu.GetPacketExpectation")

- [`TsCallKwpIOControlReturnControlToEcu.GetReturnValueExpectation`](TestStepApi.md#ApiClient.TsCallKwpIOControlReturnControlToEcu.GetReturnValueExpectation "ApiClient.TsCallKwpIOControlReturnControlToEcu.GetReturnValueExpectation")

- [`TsCallKwpIOControlShortTermAdjustment.GetPacketExpectation`](TestStepApi.md#ApiClient.TsCallKwpIOControlShortTermAdjustment.GetPacketExpectation "ApiClient.TsCallKwpIOControlShortTermAdjustment.GetPacketExpectation")

- [`TsCallKwpIOControlShortTermAdjustment.GetReturnValueExpectation`](TestStepApi.md#ApiClient.TsCallKwpIOControlShortTermAdjustment.GetReturnValueExpectation "ApiClient.TsCallKwpIOControlShortTermAdjustment.GetReturnValueExpectation")

- [`TsCallRead.GetPacketExpectation`](TestStepApi.md#ApiClient.TsCallRead.GetPacketExpectation "ApiClient.TsCallRead.GetPacketExpectation")

- [`TsCallRead.GetReturnValueExpectation`](TestStepApi.md#ApiClient.TsCallRead.GetReturnValueExpectation "ApiClient.TsCallRead.GetReturnValueExpectation")

- [`TsCallWrite.GetPacketExpectation`](TestStepApi.md#ApiClient.TsCallWrite.GetPacketExpectation "ApiClient.TsCallWrite.GetPacketExpectation")

- [`TsCallWrite.GetReturnValueExpectation`](TestStepApi.md#ApiClient.TsCallWrite.GetReturnValueExpectation "ApiClient.TsCallWrite.GetReturnValueExpectation")

- [`TsInboxFetch.GetExpectation`](TestStepApi.md#ApiClient.TsInboxFetch.GetExpectation "ApiClient.TsInboxFetch.GetExpectation")

- [`TsJob.GetExpectation`](TestStepApi.md#ApiClient.TsJob.GetExpectation "ApiClient.TsJob.GetExpectation")

- [`TsKeywordReturn.GetExpectation`](TestStepApi.md#ApiClient.TsKeywordReturn.GetExpectation "ApiClient.TsKeywordReturn.GetExpectation")

- [`TsRead.GetExpectation`](TestStepApi.md#ApiClient.TsRead.GetExpectation "ApiClient.TsRead.GetExpectation")

- [`TsReadAudio.GetExpectation`](TestStepApi.md#ApiClient.TsReadAudio.GetExpectation "ApiClient.TsReadAudio.GetExpectation")

- [`TsReadFaultMemory.GetExpectation`](TestStepApi.md#ApiClient.TsReadFaultMemory.GetExpectation "ApiClient.TsReadFaultMemory.GetExpectation")

- [`TsReadImage.GetExpectation`](TestStepApi.md#ApiClient.TsReadImage.GetExpectation "ApiClient.TsReadImage.GetExpectation")

- [`VectorAllExpectation.GetExpectation`](#ApiClient.VectorAllExpectation.GetExpectation "ApiClient.VectorAllExpectation.GetExpectation")

- [`VectorSingleExpectation.GetExpectation`](#ApiClient.VectorSingleExpectation.GetExpectation "ApiClient.VectorSingleExpectation.GetExpectation")

Subclasses

- [`AllExpectation`](#ApiClient.AllExpectation "ApiClient.AllExpectation")

- [`AudioExpectation`](#ApiClient.AudioExpectation "ApiClient.AudioExpectation")

- [`BinaryExpressionExpectation`](#ApiClient.BinaryExpressionExpectation "ApiClient.BinaryExpressionExpectation")

- [`BitStreamExpectation`](#ApiClient.BitStreamExpectation "ApiClient.BitStreamExpectation")

- [`BitStreamExpressionExpectation`](#ApiClient.BitStreamExpressionExpectation "ApiClient.BitStreamExpressionExpectation")

- [`BooleanExpectation`](#ApiClient.BooleanExpectation "ApiClient.BooleanExpectation")

- [`ByteStreamExpectation`](#ApiClient.ByteStreamExpectation "ApiClient.ByteStreamExpectation")

- [`ByteStreamExpressionExpectation`](#ApiClient.ByteStreamExpressionExpectation "ApiClient.ByteStreamExpressionExpectation")

- [`CurveAllExpectation`](#ApiClient.CurveAllExpectation "ApiClient.CurveAllExpectation")

- [`CurveSingleExpectation`](#ApiClient.CurveSingleExpectation "ApiClient.CurveSingleExpectation")

- [`DTCListExpectation`](#ApiClient.DTCListExpectation "ApiClient.DTCListExpectation")

- [`ExpressionExpectation`](#ApiClient.ExpressionExpectation "ApiClient.ExpressionExpectation")

- [`ExpressionExpectationBase`](#ApiClient.ExpressionExpectationBase "ApiClient.ExpressionExpectationBase")

- [`ImageExpectation`](#ApiClient.ImageExpectation "ApiClient.ImageExpectation")

- [`ManualExpression`](#ApiClient.ManualExpression "ApiClient.ManualExpression")

- [`MapAllExpectation`](#ApiClient.MapAllExpectation "ApiClient.MapAllExpectation")

- [`MapSingleExpectation`](#ApiClient.MapSingleExpectation "ApiClient.MapSingleExpectation")

- [`MatrixAllExpectation`](#ApiClient.MatrixAllExpectation "ApiClient.MatrixAllExpectation")

- [`MatrixSingleExpectation`](#ApiClient.MatrixSingleExpectation "ApiClient.MatrixSingleExpectation")

- [`NotPresentExpectation`](#ApiClient.NotPresentExpectation "ApiClient.NotPresentExpectation")

- [`NumericExpectation`](#ApiClient.NumericExpectation "ApiClient.NumericExpectation")

- [`NumericExpressionExpectation`](#ApiClient.NumericExpressionExpectation "ApiClient.NumericExpressionExpectation")

- [`PresentExpectation`](#ApiClient.PresentExpectation "ApiClient.PresentExpectation")

- [`StringExpectation`](#ApiClient.StringExpectation "ApiClient.StringExpectation")

- [`StringExpressionExpectation`](#ApiClient.StringExpressionExpectation "ApiClient.StringExpressionExpectation")

- [`StringListExpectation`](#ApiClient.StringListExpectation "ApiClient.StringListExpectation")

- [`VectorAllExpectation`](#ApiClient.VectorAllExpectation "ApiClient.VectorAllExpectation")

- [`VectorSingleExpectation`](#ApiClient.VectorSingleExpectation "ApiClient.VectorSingleExpectation")

Clone()[¶](#ApiClient.Expectation.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`Expectation`](#ApiClient.Expectation "ApiClient.Expectation")

## DTCListExpectation[¶](#dtclistexpectation "Link to this heading")

*class* DTCListExpectation[¶](#ApiClient.DTCListExpectation "Link to this definition")  
Base class

[`Expectation`](#ApiClient.Expectation "ApiClient.Expectation")

Returned by

- [`ExpectationApi.CreateDTCListExpectation`](#ApiClient.ExpectationApi.CreateDTCListExpectation "ApiClient.ExpectationApi.CreateDTCListExpectation")

AppendDtc(*dtc*)[¶](#ApiClient.DTCListExpectation.AppendDtc "Link to this definition")  
Appends the given DTC to the DTC list.

Note

if a numeric representation is chosen, you must provide a hex string with prefix 0x.

Parameters:  **dtc** (*str*) – The DTC to append, in the format specified via [`SetRepresentation()`](#ApiClient.DTCListExpectation.SetRepresentation "ApiClient.DTCListExpectation.SetRepresentation")

AppendToleratedDtc(*dtc*)[¶](#ApiClient.DTCListExpectation.AppendToleratedDtc "Link to this definition")  
Appends the given DTC to the list of tolerated DTCs.

This automatically disables “tolerate all”.

Note

if a numeric representation is chosen, you must provide a hex string with prefix 0x.

Parameters:  **dtc** (*str*) – The DTC to append, in the format specified via [`SetRepresentation()`](#ApiClient.DTCListExpectation.SetRepresentation "ApiClient.DTCListExpectation.SetRepresentation")

ClearDtcList()[¶](#ApiClient.DTCListExpectation.ClearDtcList "Link to this definition")  
Removes all DTCs from the DTC list.

ClearToleratedDtcList()[¶](#ApiClient.DTCListExpectation.ClearToleratedDtcList "Link to this definition")  
Removes all DTCs from the list of tolerated DTCs.

Clone()[¶](#ApiClient.DTCListExpectation.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`DTCListExpectation`](#ApiClient.DTCListExpectation "ApiClient.DTCListExpectation")

GetDtcList()[¶](#ApiClient.DTCListExpectation.GetDtcList "Link to this definition")  
Retrieves the list of expected DTCs.

Returns:  List of expected DTCs

Return type:  list[str]

GetDtcListExpression()[¶](#ApiClient.DTCListExpectation.GetDtcListExpression "Link to this definition")  
Returns the DTC list expression.

Returns:  DTC list expression

Return type:  str

GetRepresentation()[¶](#ApiClient.DTCListExpectation.GetRepresentation "Link to this definition")  
Returns the DTC representation.

Returns:  name of the representation for DTCs

Return type:  str

GetToleratedDtcList()[¶](#ApiClient.DTCListExpectation.GetToleratedDtcList "Link to this definition")  
Retrieves the list of tolerated DTCs.

Returns:  List of tolerated DTCs

Return type:  list[str]

GetToleratedDtcListExpression()[¶](#ApiClient.DTCListExpectation.GetToleratedDtcListExpression "Link to this definition")  
Returns the tolerated DTC list expression.

Returns:  tolerated DTC list expression

Return type:  str

IsExpectPresent()[¶](#ApiClient.DTCListExpectation.IsExpectPresent "Link to this definition")  
Returns whether the specified list of DTCs will be expected to be present (True) or absent (False)

Returns:  Specified DTCs will be expected to be present (True) or absent (False)

Return type:  bool

IsTolerateAll()[¶](#ApiClient.DTCListExpectation.IsTolerateAll "Link to this definition")  
Returns whether all other DTCs (which are not in the DTC list) should be tolerated.

Returns:  tolerate all (True) or only those in the tolerated list (False)

Return type:  bool

SetDtcListExpression(*dtcListExpression*)[¶](#ApiClient.DTCListExpectation.SetDtcListExpression "Link to this definition")  
Sets the DTC list expression.

Parameters:  **dtcListExpression** (*str*) – DTC list expression

SetExpectAbsent()[¶](#ApiClient.DTCListExpectation.SetExpectAbsent "Link to this definition")  
Declares that the DTCs specified via [`AppendDtc()`](#ApiClient.DTCListExpectation.AppendDtc "ApiClient.DTCListExpectation.AppendDtc") as well `SetDynamicDtcList()` are expected to be absent.

SetExpectPresent()[¶](#ApiClient.DTCListExpectation.SetExpectPresent "Link to this definition")  
Declares that the DTCs specified via [`AppendDtc()`](#ApiClient.DTCListExpectation.AppendDtc "ApiClient.DTCListExpectation.AppendDtc") as well `SetDynamicDtcList()` are expected to be present.

SetRepresentation(*representation*)[¶](#ApiClient.DTCListExpectation.SetRepresentation "Link to this definition")  
Sets the DTC representation.

Parameters:  **representation** (*str*) – Name of the representation for DTCs. Possible values: - ‘Display Trouble Code including FTB ([PCBU]-Code)’ - ‘Display Trouble Code without FTB ([PCBU]-Code)’ - ‘Short Name’ - ‘Description’ - ‘Number (3 Byte)’ - ‘Number (2 Byte)’

SetTolerateAll()[¶](#ApiClient.DTCListExpectation.SetTolerateAll "Link to this definition")  
Declares that all all other DTCs (not mentioned in the DTC list) shall be tolerated.

This automatically clears the list and expression of tolerated DTCs

SetToleratedDtcListExpression(*toleratedDtcListExpression*)[¶](#ApiClient.DTCListExpectation.SetToleratedDtcListExpression "Link to this definition")  
Sets the tolerated DTC list expression.

This automatically disables “tolerate all”.

Parameters:  **toleratedDtcListExpression** (*str*) – tolerated DTC list expression

## ExpressionExpectationBase[¶](#expressionexpectationbase "Link to this heading")

*class* ExpressionExpectationBase[¶](#ApiClient.ExpressionExpectationBase "Link to this definition")  
Base class

[`Expectation`](#ApiClient.Expectation "ApiClient.Expectation")

Subclasses

- [`BinaryExpressionExpectation`](#ApiClient.BinaryExpressionExpectation "ApiClient.BinaryExpressionExpectation")

- [`BitStreamExpressionExpectation`](#ApiClient.BitStreamExpressionExpectation "ApiClient.BitStreamExpressionExpectation")

- [`BooleanExpectation`](#ApiClient.BooleanExpectation "ApiClient.BooleanExpectation")

- [`ByteStreamExpressionExpectation`](#ApiClient.ByteStreamExpressionExpectation "ApiClient.ByteStreamExpressionExpectation")

- [`ExpressionExpectation`](#ApiClient.ExpressionExpectation "ApiClient.ExpressionExpectation")

- [`ManualExpression`](#ApiClient.ManualExpression "ApiClient.ManualExpression")

- [`NumericExpressionExpectation`](#ApiClient.NumericExpressionExpectation "ApiClient.NumericExpressionExpectation")

- [`StringExpressionExpectation`](#ApiClient.StringExpressionExpectation "ApiClient.StringExpressionExpectation")

Clone()[¶](#ApiClient.ExpressionExpectationBase.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`ExpressionExpectationBase`](#ApiClient.ExpressionExpectationBase "ApiClient.ExpressionExpectationBase")

GetExpression()[¶](#ApiClient.ExpressionExpectationBase.GetExpression "Link to this definition")  
Returns the expectations expression.

Returns:  The expression

Return type:  str

SetExpression(*expression*)[¶](#ApiClient.ExpressionExpectationBase.SetExpression "Link to this definition")  
Sets the expectations expression.

Parameters:  **expression** (*str*) – The expression

## ExpressionExpectation[¶](#expressionexpectation "Link to this heading")

*class* ExpressionExpectation[¶](#ApiClient.ExpressionExpectation "Link to this definition")  
Base classes

- [`Expectation`](#ApiClient.Expectation "ApiClient.Expectation")

- [`ExpressionExpectationBase`](#ApiClient.ExpressionExpectationBase "ApiClient.ExpressionExpectationBase")

Returned by

- [`ExpectationApi.CreateExpressionExpectation`](#ApiClient.ExpectationApi.CreateExpressionExpectation "ApiClient.ExpectationApi.CreateExpressionExpectation")

Clone()[¶](#ApiClient.ExpressionExpectation.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`ExpressionExpectation`](#ApiClient.ExpressionExpectation "ApiClient.ExpressionExpectation")

GetExpression()[¶](#ApiClient.ExpressionExpectation.GetExpression "Link to this definition")  
Returns the expectations expression.

Returns:  The expression

Return type:  str

SetExpression(*expression*)[¶](#ApiClient.ExpressionExpectation.SetExpression "Link to this definition")  
Sets the expectations expression.

Parameters:  **expression** (*str*) – The expression

## ManualExpression[¶](#manualexpression "Link to this heading")

*class* ManualExpression[¶](#ApiClient.ManualExpression "Link to this definition")  
Base classes

- [`Expectation`](#ApiClient.Expectation "ApiClient.Expectation")

- [`ExpressionExpectationBase`](#ApiClient.ExpressionExpectationBase "ApiClient.ExpressionExpectationBase")

Clone()[¶](#ApiClient.ManualExpression.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`ManualExpression`](#ApiClient.ManualExpression "ApiClient.ManualExpression")

GetExpression()[¶](#ApiClient.ManualExpression.GetExpression "Link to this definition")  
Returns the expectations expression.

Returns:  The expression

Return type:  str

SetExpression(*expression*)[¶](#ApiClient.ManualExpression.SetExpression "Link to this definition")  
Sets the expectations expression.

Parameters:  **expression** (*str*) – The expression

## NumericExpressionExpectation[¶](#numericexpressionexpectation "Link to this heading")

*class* NumericExpressionExpectation[¶](#ApiClient.NumericExpressionExpectation "Link to this definition")  
Base classes

- [`Expectation`](#ApiClient.Expectation "ApiClient.Expectation")

- [`ExpressionExpectationBase`](#ApiClient.ExpressionExpectationBase "ApiClient.ExpressionExpectationBase")

Returned by

- [`ExpectationApi.CreateNumericExpressionExpectation`](#ApiClient.ExpectationApi.CreateNumericExpressionExpectation "ApiClient.ExpectationApi.CreateNumericExpressionExpectation")

Clone()[¶](#ApiClient.NumericExpressionExpectation.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`NumericExpressionExpectation`](#ApiClient.NumericExpressionExpectation "ApiClient.NumericExpressionExpectation")

GetExpression()[¶](#ApiClient.NumericExpressionExpectation.GetExpression "Link to this definition")  
Returns the expectations expression.

Returns:  The expression

Return type:  str

SetExpression(*expression*)[¶](#ApiClient.NumericExpressionExpectation.SetExpression "Link to this definition")  
Sets the expectations expression.

Parameters:  **expression** (*str*) – The expression

## StringExpressionExpectation[¶](#stringexpressionexpectation "Link to this heading")

*class* StringExpressionExpectation[¶](#ApiClient.StringExpressionExpectation "Link to this definition")  
Base classes

- [`Expectation`](#ApiClient.Expectation "ApiClient.Expectation")

- [`ExpressionExpectationBase`](#ApiClient.ExpressionExpectationBase "ApiClient.ExpressionExpectationBase")

Returned by

- [`ExpectationApi.CreateStringExpressionExpectation`](#ApiClient.ExpectationApi.CreateStringExpressionExpectation "ApiClient.ExpectationApi.CreateStringExpressionExpectation")

Clone()[¶](#ApiClient.StringExpressionExpectation.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`StringExpressionExpectation`](#ApiClient.StringExpressionExpectation "ApiClient.StringExpressionExpectation")

GetCaseSensitive()[¶](#ApiClient.StringExpressionExpectation.GetCaseSensitive "Link to this definition")  
Returns whether the comparison should be case-sensitive.

Returns:  True if case-sensitive, else False.

Return type:  boolean

GetExpression()[¶](#ApiClient.StringExpressionExpectation.GetExpression "Link to this definition")  
Returns the expectations expression.

Returns:  The expression

Return type:  str

SetCaseSensitive(*caseSensitive*)[¶](#ApiClient.StringExpressionExpectation.SetCaseSensitive "Link to this definition")  
Sets whether the comparison should be case-sensitive.

Parameters:  **caseSensitive** (*boolean*) – True if case-sensitive, else False.

SetExpression(*expression*)[¶](#ApiClient.StringExpressionExpectation.SetExpression "Link to this definition")  
Sets the expectations expression.

Parameters:  **expression** (*str*) – The expression

## PresentExpectation[¶](#presentexpectation "Link to this heading")

*class* PresentExpectation[¶](#ApiClient.PresentExpectation "Link to this definition")  
Base class

[`Expectation`](#ApiClient.Expectation "ApiClient.Expectation")

Returned by

- [`ExpectationApi.CreatePresentExpectation`](#ApiClient.ExpectationApi.CreatePresentExpectation "ApiClient.ExpectationApi.CreatePresentExpectation")

Clone()[¶](#ApiClient.PresentExpectation.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`PresentExpectation`](#ApiClient.PresentExpectation "ApiClient.PresentExpectation")

GetExpression()[¶](#ApiClient.PresentExpectation.GetExpression "Link to this definition")  
Returns the expectations expression.

Returns:  The expression

Return type:  str

## NotPresentExpectation[¶](#notpresentexpectation "Link to this heading")

*class* NotPresentExpectation[¶](#ApiClient.NotPresentExpectation "Link to this definition")  
Base class

[`Expectation`](#ApiClient.Expectation "ApiClient.Expectation")

Returned by

- [`ExpectationApi.CreateNotPresentExpectation`](#ApiClient.ExpectationApi.CreateNotPresentExpectation "ApiClient.ExpectationApi.CreateNotPresentExpectation")

Clone()[¶](#ApiClient.NotPresentExpectation.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`NotPresentExpectation`](#ApiClient.NotPresentExpectation "ApiClient.NotPresentExpectation")

GetExpression()[¶](#ApiClient.NotPresentExpectation.GetExpression "Link to this definition")  
Returns the expectations expression.

Returns:  The expression

Return type:  str

## StringExpectation[¶](#stringexpectation "Link to this heading")

*class* StringExpectation[¶](#ApiClient.StringExpectation "Link to this definition")  
Base class

[`Expectation`](#ApiClient.Expectation "ApiClient.Expectation")

Returned by

- [`ExpectationApi.CreateStringExpectation`](#ApiClient.ExpectationApi.CreateStringExpectation "ApiClient.ExpectationApi.CreateStringExpectation")

Clone()[¶](#ApiClient.StringExpectation.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`StringExpectation`](#ApiClient.StringExpectation "ApiClient.StringExpectation")

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

Return type:  [`KeywordValueExpression`](ExpressionApi.md#ApiClient.KeywordValueExpression "ApiClient.KeywordValueExpression")

GetExpressionType()[¶](#ApiClient.StringExpectation.GetExpressionType "Link to this definition")  
Returns how the actual value and the expression value will be compared.

Returns:  The expression type

Return type:  str

SetCaseSensitive(*caseSensitive*)[¶](#ApiClient.StringExpectation.SetCaseSensitive "Link to this definition")  
Sets whether the comparison should be case-sensitive.

Parameters:  **caseSensitive** (*boolean*) – True if case-sensitive, else False.

SetDontEvalNotPresent(*dontEvalNotPresent*)[¶](#ApiClient.StringExpectation.SetDontEvalNotPresent "Link to this definition")  
Enables or disables the option to evaluate this expectation if the expected value is NotPresent.

Parameters:  **dontEvalNotPresent** (*boolean*) – True to enable the described behavior. False to disable it.

SetExpression(*expression*)[¶](#ApiClient.StringExpectation.SetExpression "Link to this definition")  
Sets the expectations expression.

Parameters:  **expression** (*str*) – The expression

SetExpressionObject(*expression*)[¶](#ApiClient.StringExpectation.SetExpressionObject "Link to this definition")  
Sets the expectations expression. Currently only KeywordValueExpression are supported!

Parameters:  **expression** ([`KeywordValueExpression`](ExpressionApi.md#ApiClient.KeywordValueExpression "ApiClient.KeywordValueExpression")) – The KeywordValue expression

SetExpressionType(*expressionType*)[¶](#ApiClient.StringExpectation.SetExpressionType "Link to this definition")  
Sets how the actual value and the expression value will be compared.

Parameters:  **expressionType** (*str*) – The expression type. Possible values: - ‘identical’ (default) - ‘starts with’ - ‘ends with’ - ‘contains’ - ‘constains not’ - ‘dissimilar’

## StringListExpectation[¶](#stringlistexpectation "Link to this heading")

*class* StringListExpectation[¶](#ApiClient.StringListExpectation "Link to this definition")  
Base class

[`Expectation`](#ApiClient.Expectation "ApiClient.Expectation")

Returned by

- [`ExpectationApi.CreateStringListExpectation`](#ApiClient.ExpectationApi.CreateStringListExpectation "ApiClient.ExpectationApi.CreateStringListExpectation")

Clone()[¶](#ApiClient.StringListExpectation.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`StringListExpectation`](#ApiClient.StringListExpectation "ApiClient.StringListExpectation")

GetCaseSensitive()[¶](#ApiClient.StringListExpectation.GetCaseSensitive "Link to this definition")  
Returns whether the comparison should be case-sensitive.

Returns:  True if case-sensitive, else False.

Return type:  boolean

GetExpressionList()[¶](#ApiClient.StringListExpectation.GetExpressionList "Link to this definition")  
Returns the list of expressions if set, otherwise an empty list. Currently only KeywordValueExpression are supported!

Returns:  The list of expressions

Return type:  list[[`KeywordValueExpression`](ExpressionApi.md#ApiClient.KeywordValueExpression "ApiClient.KeywordValueExpression")]

GetStringList()[¶](#ApiClient.StringListExpectation.GetStringList "Link to this definition")  
Returns the list of strings if set, otherwise an empty list.

Returns:  The list of strings

Return type:  list[str]

GetStringListVariableName()[¶](#ApiClient.StringListExpectation.GetStringListVariableName "Link to this definition")  
Returns the variable that stores the list of strings if set else None.

Returns:  The variable name

Return type:  str

SetCaseSensitive(*caseSensitive*)[¶](#ApiClient.StringListExpectation.SetCaseSensitive "Link to this definition")  
Sets whether the comparison should be case-sensitive.

Parameters:  **caseSensitive** (*boolean*) – True if case-sensitive, else False.

SetExpressionList(*exprList*)[¶](#ApiClient.StringListExpectation.SetExpressionList "Link to this definition")  
Sets the expectations expression. Currently only KeywordValueExpression are supported!

Parameters:  **exprList** (list[[`KeywordValueExpression`](ExpressionApi.md#ApiClient.KeywordValueExpression "ApiClient.KeywordValueExpression")]) – The list of expressions

SetStringList(*stringList*)[¶](#ApiClient.StringListExpectation.SetStringList "Link to this definition")  
Sets the list of strings the actual value has to be contained in.

Parameters:  **stringList** (*list[str]*) – The list of strings

SetStringListVariableName(*variableName*)[¶](#ApiClient.StringListExpectation.SetStringListVariableName "Link to this definition")  
Sets the variable that stores the list of strings the actual value has to be contained in.

Parameters:  **variableName** (*str*) – Name of the variable

## VectorSingleExpectation[¶](#vectorsingleexpectation "Link to this heading")

*class* VectorSingleExpectation[¶](#ApiClient.VectorSingleExpectation "Link to this definition")  
Represents a sparse vector of expectations. Each element of the vector represents an individual expectation on the respective value. All individual expectations must be fulfilled in order for the this vector expectation to be fulfilled.

Each individual expectation is specified as a Boolean expression in Python syntax. The special identifier “value” refers to the actual value of the vector element.

Base class

[`Expectation`](#ApiClient.Expectation "ApiClient.Expectation")

Returned by

- [`ExpectationApi.CreateVectorSingleExpectation`](#ApiClient.ExpectationApi.CreateVectorSingleExpectation "ApiClient.ExpectationApi.CreateVectorSingleExpectation")

Subclasses

- [`CurveSingleExpectation`](#ApiClient.CurveSingleExpectation "ApiClient.CurveSingleExpectation")

Clone()[¶](#ApiClient.VectorSingleExpectation.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`VectorSingleExpectation`](#ApiClient.VectorSingleExpectation "ApiClient.VectorSingleExpectation")

GetDimension()[¶](#ApiClient.VectorSingleExpectation.GetDimension "Link to this definition")  
Returns the dimension of the element.

Returns:  Dimension of the element.

Return type:  int

GetExpectation(*index*)[¶](#ApiClient.VectorSingleExpectation.GetExpectation "Link to this definition")  
Returns the expectation object for the specified element.

Parameters:  **index** (*int*) – Index of the expectation object.

Returns:  The expectation object

Return type:  [`Expectation`](#ApiClient.Expectation "ApiClient.Expectation")

GetExpectationExpression(*index*)[¶](#ApiClient.VectorSingleExpectation.GetExpectationExpression "Link to this definition")  
Returns the expectation expression for the specified element.

Parameters:  **index** (*int*) – Index of the expression.

Returns:  The expression

Return type:  str

GetExpectationExpressions()[¶](#ApiClient.VectorSingleExpectation.GetExpectationExpressions "Link to this definition")  
Returns a list of all expectation expression. Elements without expectation are represented by None

Returns:  Sorted list containing all expectation expressions

Return type:  list[str]

RemoveExpectation(*index*)[¶](#ApiClient.VectorSingleExpectation.RemoveExpectation "Link to this definition")  
Removes the expectation expression for the specified element.

Parameters:  **index** (*int*) – Index of the expression to remove.

SetExpectation(*index*, *expectationObject*)[¶](#ApiClient.VectorSingleExpectation.SetExpectation "Link to this definition")  
Sets the expectation object for the specified element.

Parameters:  - **index** (*int*) – Index of the expectation object.

- **expectationObject** ([`Expectation`](#ApiClient.Expectation "ApiClient.Expectation")) – The expectation object

SetExpectationExpression(*index*, *expression*)[¶](#ApiClient.VectorSingleExpectation.SetExpectationExpression "Link to this definition")  
Sets the expectation expression for the specified element.

Parameters:  - **index** (*int*) – Index of the expression.

- **expression** (*str*) – The expression

## CurveSingleExpectation[¶](#curvesingleexpectation "Link to this heading")

*class* CurveSingleExpectation[¶](#ApiClient.CurveSingleExpectation "Link to this definition")  
Represents a sparse curve of expectations. Each element of the curve represents an individual expectation on the respective value. All individual expectations must be fulfilled in order for the this curve expectation to be fulfilled.

Each individual expectation is specified as a Boolean expression in Python syntax. The special identifier “value” refers to the actual value of the curve element.

Base classes

- [`Expectation`](#ApiClient.Expectation "ApiClient.Expectation")

- [`VectorSingleExpectation`](#ApiClient.VectorSingleExpectation "ApiClient.VectorSingleExpectation")

Returned by

- [`ExpectationApi.CreateCurveSingleExpectation`](#ApiClient.ExpectationApi.CreateCurveSingleExpectation "ApiClient.ExpectationApi.CreateCurveSingleExpectation")

Clone()[¶](#ApiClient.CurveSingleExpectation.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`CurveSingleExpectation`](#ApiClient.CurveSingleExpectation "ApiClient.CurveSingleExpectation")

GetDimension()[¶](#ApiClient.CurveSingleExpectation.GetDimension "Link to this definition")  
Returns the dimension of the element.

Returns:  Dimension of the element.

Return type:  int

GetDistributionExpectation(*index*)[¶](#ApiClient.CurveSingleExpectation.GetDistributionExpectation "Link to this definition")  
Gets the distribution level of the given position.

Parameters:  **index** (*int*) – Index of the expectation object.

Returns:  Distribution level expectation object

Return type:  [`Expectation`](#ApiClient.Expectation "ApiClient.Expectation")

GetDistributionExpectationExpression(*index*)[¶](#ApiClient.CurveSingleExpectation.GetDistributionExpectationExpression "Link to this definition")  
Gets the distribution level of the given position.

Parameters:  **index** (*int*) – index

Returns:  Distribution level expectation expression

Return type:  str

GetDistributionExpectationExpressions()[¶](#ApiClient.CurveSingleExpectation.GetDistributionExpectationExpressions "Link to this definition")  
Returns a list of all distribution level expectation expression. Elements without expectation are represented by None

Returns:  Sorted list containing all distribution level expectation expressions

Return type:  list[str]

GetExpectation(*index*)[¶](#ApiClient.CurveSingleExpectation.GetExpectation "Link to this definition")  
Returns the expectation object for the specified element.

Parameters:  **index** (*int*) – Index of the expectation object.

Returns:  The expectation object

Return type:  [`Expectation`](#ApiClient.Expectation "ApiClient.Expectation")

GetExpectationExpression(*index*)[¶](#ApiClient.CurveSingleExpectation.GetExpectationExpression "Link to this definition")  
Returns the expectation expression for the specified element.

Parameters:  **index** (*int*) – Index of the expression.

Returns:  The expression

Return type:  str

GetExpectationExpressions()[¶](#ApiClient.CurveSingleExpectation.GetExpectationExpressions "Link to this definition")  
Returns a list of all expectation expression. Elements without expectation are represented by None

Returns:  Sorted list containing all expectation expressions

Return type:  list[str]

RemoveDistributionExpectation(*index*)[¶](#ApiClient.CurveSingleExpectation.RemoveDistributionExpectation "Link to this definition")  
Deletes the distribution level of the given position.

Parameters:  **index** (*int*) – index

RemoveExpectation(*index*)[¶](#ApiClient.CurveSingleExpectation.RemoveExpectation "Link to this definition")  
Removes the expectation expression for the specified element.

Parameters:  **index** (*int*) – Index of the expression to remove.

SetDistributionExpectation(*index*, *expectationObject*)[¶](#ApiClient.CurveSingleExpectation.SetDistributionExpectation "Link to this definition")  
Sets the distribution level of the given position.

Parameters:  - **index** (*int*) – Index of the expectation object.

- **expectationObject** ([`Expectation`](#ApiClient.Expectation "ApiClient.Expectation")) – Distribution level expectation object

SetDistributionExpectationExpression(*index*, *expression*)[¶](#ApiClient.CurveSingleExpectation.SetDistributionExpectationExpression "Link to this definition")  
Sets the distribution level of the given position.

Parameters:  - **index** (*int*) – index

- **expression** (*str*) – Distribution level expectation expression

SetExpectation(*index*, *expectationObject*)[¶](#ApiClient.CurveSingleExpectation.SetExpectation "Link to this definition")  
Sets the expectation object for the specified element.

Parameters:  - **index** (*int*) – Index of the expectation object.

- **expectationObject** ([`Expectation`](#ApiClient.Expectation "ApiClient.Expectation")) – The expectation object

SetExpectationExpression(*index*, *expression*)[¶](#ApiClient.CurveSingleExpectation.SetExpectationExpression "Link to this definition")  
Sets the expectation expression for the specified element.

Parameters:  - **index** (*int*) – Index of the expression.

- **expression** (*str*) – The expression

## MatrixSingleExpectation[¶](#matrixsingleexpectation "Link to this heading")

*class* MatrixSingleExpectation[¶](#ApiClient.MatrixSingleExpectation "Link to this definition")  
Represents a sparse matrix of expectations. Each element of the matrix represents an individual expectation on the respective value. All individual expectations must be fulfilled in order for the this matrix expectation to be fulfilled.

Each individual expectation is specified as a Boolean expression in Python syntax. The special identifier “value” refers to the actual value of the matrix element.

Base class

[`Expectation`](#ApiClient.Expectation "ApiClient.Expectation")

Returned by

- [`ExpectationApi.CreateMatrixSingleExpectation`](#ApiClient.ExpectationApi.CreateMatrixSingleExpectation "ApiClient.ExpectationApi.CreateMatrixSingleExpectation")

Subclasses

- [`MapSingleExpectation`](#ApiClient.MapSingleExpectation "ApiClient.MapSingleExpectation")

Clone()[¶](#ApiClient.MatrixSingleExpectation.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`MatrixSingleExpectation`](#ApiClient.MatrixSingleExpectation "ApiClient.MatrixSingleExpectation")

GetExpectation(*xIndex*, *yIndex*)[¶](#ApiClient.MatrixSingleExpectation.GetExpectation "Link to this definition")  
Returns the expectation object.

Parameters:  - **xIndex** (*int*) – X-Index of the expectation object.

- **yIndex** (*int*) – Y-Index of the expectation object.

Returns:  The expectation object

Return type:  [`Expectation`](#ApiClient.Expectation "ApiClient.Expectation")

GetExpectationExpression(*xIndex*, *yIndex*)[¶](#ApiClient.MatrixSingleExpectation.GetExpectationExpression "Link to this definition")  
Returns the expectations expression.

Parameters:  - **xIndex** (*int*) – X-Index of the expression.

- **yIndex** (*int*) – Y-Index of the expression.

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

RemoveExpectation(*xIndex*, *yIndex*)[¶](#ApiClient.MatrixSingleExpectation.RemoveExpectation "Link to this definition")  
Removes an expectation expression

Parameters:  - **xIndex** (*int*) – X-Index of the expression to remove.

- **yIndex** (*int*) – Y-Index of the expression to remove.

SetExpectation(*xIndex*, *yIndex*, *expectationObject*)[¶](#ApiClient.MatrixSingleExpectation.SetExpectation "Link to this definition")  
Sets the expectation object.

Parameters:  - **xIndex** (*int*) – X-Index of the expectation object.

- **yIndex** (*int*) – Y-Index of the expectation object.

- **expectationObject** ([`Expectation`](#ApiClient.Expectation "ApiClient.Expectation")) – The expectation object

SetExpectationExpression(*xIndex*, *yIndex*, *expression*)[¶](#ApiClient.MatrixSingleExpectation.SetExpectationExpression "Link to this definition")  
Sets the expectations expression.

Parameters:  - **xIndex** (*int*) – X-Index of the expression.

- **yIndex** (*int*) – Y-Index of the expression.

- **expression** (*str*) – The expression

## MapSingleExpectation[¶](#mapsingleexpectation "Link to this heading")

*class* MapSingleExpectation[¶](#ApiClient.MapSingleExpectation "Link to this definition")  
Represents a sparse map of expectations. Each element of the map represents an individual expectation on the respective value. All individual expectations must be fulfilled in order for the this map expectation to be fulfilled.

Each individual expectation is specified as a Boolean expression in Python syntax. The special identifier “value” refers to the actual value of the map element.

Base classes

- [`Expectation`](#ApiClient.Expectation "ApiClient.Expectation")

- [`MatrixSingleExpectation`](#ApiClient.MatrixSingleExpectation "ApiClient.MatrixSingleExpectation")

Returned by

- [`ExpectationApi.CreateMapSingleExpectation`](#ApiClient.ExpectationApi.CreateMapSingleExpectation "ApiClient.ExpectationApi.CreateMapSingleExpectation")

Clone()[¶](#ApiClient.MapSingleExpectation.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`MapSingleExpectation`](#ApiClient.MapSingleExpectation "ApiClient.MapSingleExpectation")

GetExpectation(*xIndex*, *yIndex*)[¶](#ApiClient.MapSingleExpectation.GetExpectation "Link to this definition")  
Returns the expectation object.

Parameters:  - **xIndex** (*int*) – X-Index of the expectation object.

- **yIndex** (*int*) – Y-Index of the expectation object.

Returns:  The expectation object

Return type:  [`Expectation`](#ApiClient.Expectation "ApiClient.Expectation")

GetExpectationExpression(*xIndex*, *yIndex*)[¶](#ApiClient.MapSingleExpectation.GetExpectationExpression "Link to this definition")  
Returns the expectations expression.

Parameters:  - **xIndex** (*int*) – X-Index of the expression.

- **yIndex** (*int*) – Y-Index of the expression.

Returns:  The expression

Return type:  str

GetExpectationExpressionLines()[¶](#ApiClient.MapSingleExpectation.GetExpectationExpressionLines "Link to this definition")  
Returns a list of expectation expressions for all lines. Each line itself is also a list of all the expressions within the line. Elements without expectation are represented by None.

Returns:  Sorted list containing all expressions

Return type:  list[list[str]]

GetXDimension()[¶](#ApiClient.MapSingleExpectation.GetXDimension "Link to this definition")  
Returns the x dimension. :return: The x dimension. :rtype: int

GetXDistributionExpectation(*index*)[¶](#ApiClient.MapSingleExpectation.GetXDistributionExpectation "Link to this definition")  
Returns the expectation object.

Parameters:  **index** (*int*) – X-index of the expectation object.

Returns:  The expectation object

Return type:  [`Expectation`](#ApiClient.Expectation "ApiClient.Expectation")

GetXDistributionExpectationExpression(*index*)[¶](#ApiClient.MapSingleExpectation.GetXDistributionExpectationExpression "Link to this definition")  
Gets the distribution level of the given position.

Parameters:  **index** (*int*) – index

Returns:  distribution level expression

Return type:  str

GetXDistributionExpectationExpressions()[¶](#ApiClient.MapSingleExpectation.GetXDistributionExpectationExpressions "Link to this definition")  
Returns a list of all distribution level expectation expression. Elements without expectation are represented by None

Returns:  Sorted list containing all distribution level expectation expressions

Return type:  list[str]

GetYDimension()[¶](#ApiClient.MapSingleExpectation.GetYDimension "Link to this definition")  
Returns the y dimension. :return: The y dimension. :rtype: int

GetYDistributionExpectation(*index*)[¶](#ApiClient.MapSingleExpectation.GetYDistributionExpectation "Link to this definition")  
Returns the expectation object.

Parameters:  **index** (*int*) – Y-index of the expectation object.

Returns:  The expectation object

Return type:  [`Expectation`](#ApiClient.Expectation "ApiClient.Expectation")

GetYDistributionExpectationExpression(*index*)[¶](#ApiClient.MapSingleExpectation.GetYDistributionExpectationExpression "Link to this definition")  
Gets the distribution level of the given position.

Parameters:  **index** (*int*) – index

Returns:  distribution level expression

Return type:  str

GetYDistributionExpectationExpressions()[¶](#ApiClient.MapSingleExpectation.GetYDistributionExpectationExpressions "Link to this definition")  
Returns a list of all distribution level expectation expression. Elements without expectation are represented by None

Returns:  Sorted list containing all distribution level expectation expressions

Return type:  list[str]

RemoveExpectation(*xIndex*, *yIndex*)[¶](#ApiClient.MapSingleExpectation.RemoveExpectation "Link to this definition")  
Removes an expectation expression

Parameters:  - **xIndex** (*int*) – X-Index of the expression to remove.

- **yIndex** (*int*) – Y-Index of the expression to remove.

RemoveXDistributionExpectation(*index*)[¶](#ApiClient.MapSingleExpectation.RemoveXDistributionExpectation "Link to this definition")  
Deletes the distribution level of the given position.

Parameters:  **index** (*int*) – index

RemoveYDistributionExpectation(*index*)[¶](#ApiClient.MapSingleExpectation.RemoveYDistributionExpectation "Link to this definition")  
Deletes the distribution level of the given position.

Parameters:  **index** (*int*) – index

SetExpectation(*xIndex*, *yIndex*, *expectationObject*)[¶](#ApiClient.MapSingleExpectation.SetExpectation "Link to this definition")  
Sets the expectation object.

Parameters:  - **xIndex** (*int*) – X-Index of the expectation object.

- **yIndex** (*int*) – Y-Index of the expectation object.

- **expectationObject** ([`Expectation`](#ApiClient.Expectation "ApiClient.Expectation")) – The expectation object

SetExpectationExpression(*xIndex*, *yIndex*, *expression*)[¶](#ApiClient.MapSingleExpectation.SetExpectationExpression "Link to this definition")  
Sets the expectations expression.

Parameters:  - **xIndex** (*int*) – X-Index of the expression.

- **yIndex** (*int*) – Y-Index of the expression.

- **expression** (*str*) – The expression

SetXDistributionExpectation(*index*, *expectationObject*)[¶](#ApiClient.MapSingleExpectation.SetXDistributionExpectation "Link to this definition")  
Sets the expectations object.

Parameters:  - **index** (*int*) – X-Index of the expectation object.

- **expectationObject** ([`Expectation`](#ApiClient.Expectation "ApiClient.Expectation")) – The expectation object

SetXDistributionExpectationExpression(*index*, *expression*)[¶](#ApiClient.MapSingleExpectation.SetXDistributionExpectationExpression "Link to this definition")  
Sets the distribution level of the given position.

Parameters:  - **index** (*int*) – index

- **expression** (*str*) – distribution level value

SetYDistributionExpectation(*index*, *expectationObject*)[¶](#ApiClient.MapSingleExpectation.SetYDistributionExpectation "Link to this definition")  
Sets the expectations object.

Parameters:  - **index** (*int*) – Y-Index of the expectation object.

- **expectationObject** ([`Expectation`](#ApiClient.Expectation "ApiClient.Expectation")) – The expectation object

SetYDistributionExpectationExpression(*index*, *expression*)[¶](#ApiClient.MapSingleExpectation.SetYDistributionExpectationExpression "Link to this definition")  
Sets the distribution level of the given position.

Parameters:  - **index** (*int*) – index

- **expression** (*str*) – distribution level value

## AllExpectation[¶](#allexpectation "Link to this heading")

*class* AllExpectation[¶](#ApiClient.AllExpectation "Link to this definition")  
Represents an expectation on all elements for complex data types. All sub elements of must fulfill the expectation for this expectation to be fulfilled.

The expectation is specified as a Boolean expression in Python syntax. The special identifier “value” refers to the actual value of each element.

Base class

[`Expectation`](#ApiClient.Expectation "ApiClient.Expectation")

Subclasses

- [`CurveAllExpectation`](#ApiClient.CurveAllExpectation "ApiClient.CurveAllExpectation")

- [`MapAllExpectation`](#ApiClient.MapAllExpectation "ApiClient.MapAllExpectation")

- [`MatrixAllExpectation`](#ApiClient.MatrixAllExpectation "ApiClient.MatrixAllExpectation")

- [`VectorAllExpectation`](#ApiClient.VectorAllExpectation "ApiClient.VectorAllExpectation")

Clone()[¶](#ApiClient.AllExpectation.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`AllExpectation`](#ApiClient.AllExpectation "ApiClient.AllExpectation")

GetExpectation()[¶](#ApiClient.AllExpectation.GetExpectation "Link to this definition")  
Returns the expectation object.

Returns:  The expectation object

Return type:  [`Expectation`](#ApiClient.Expectation "ApiClient.Expectation")

GetExpectationExpression()[¶](#ApiClient.AllExpectation.GetExpectationExpression "Link to this definition")  
Returns the expectation expression.

Returns:  The expression

Return type:  str

SetExpectation(*expectationObject*)[¶](#ApiClient.AllExpectation.SetExpectation "Link to this definition")  
Sets the expectation object.

Parameters:  **expectationObject** ([`Expectation`](#ApiClient.Expectation "ApiClient.Expectation")) – The expectation object

SetExpectationExpression(*expression*)[¶](#ApiClient.AllExpectation.SetExpectationExpression "Link to this definition")  
Sets the expectation expression.

Parameters:  **expression** (*str*) – The expression

## VectorAllExpectation[¶](#vectorallexpectation "Link to this heading")

*class* VectorAllExpectation[¶](#ApiClient.VectorAllExpectation "Link to this definition")  
Represents an expectation on all elements of a vector. All elements of the vector must fulfill the expectation for this vector expectation to be fulfilled.

The expectation is specified as a Boolean expression in Python syntax. The special identifier “value” refers to the actual value of each vector element.

Base classes

- [`Expectation`](#ApiClient.Expectation "ApiClient.Expectation")

- [`AllExpectation`](#ApiClient.AllExpectation "ApiClient.AllExpectation")

Returned by

- [`ExpectationApi.CreateVectorAllExpectation`](#ApiClient.ExpectationApi.CreateVectorAllExpectation "ApiClient.ExpectationApi.CreateVectorAllExpectation")

- [`ExpectationApi.CreateVectorAllExpressionExpectation`](#ApiClient.ExpectationApi.CreateVectorAllExpressionExpectation "ApiClient.ExpectationApi.CreateVectorAllExpressionExpectation")

Clone()[¶](#ApiClient.VectorAllExpectation.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`VectorAllExpectation`](#ApiClient.VectorAllExpectation "ApiClient.VectorAllExpectation")

GetExpectation()[¶](#ApiClient.VectorAllExpectation.GetExpectation "Link to this definition")  
Returns the expectation object.

Returns:  The expectation object

Return type:  [`Expectation`](#ApiClient.Expectation "ApiClient.Expectation")

GetExpectationExpression()[¶](#ApiClient.VectorAllExpectation.GetExpectationExpression "Link to this definition")  
Returns the expectation expression.

Returns:  The expression

Return type:  str

SetExpectation(*expectationObject*)[¶](#ApiClient.VectorAllExpectation.SetExpectation "Link to this definition")  
Sets the expectation object.

Parameters:  **expectationObject** ([`Expectation`](#ApiClient.Expectation "ApiClient.Expectation")) – The expectation object

SetExpectationExpression(*expression*)[¶](#ApiClient.VectorAllExpectation.SetExpectationExpression "Link to this definition")  
Sets the expectation expression.

Parameters:  **expression** (*str*) – The expression

## MatrixAllExpectation[¶](#matrixallexpectation "Link to this heading")

*class* MatrixAllExpectation[¶](#ApiClient.MatrixAllExpectation "Link to this definition")  
Represents an expectation on all elements of a matrix. All elements of the matrix must fulfill the expectation for this matrix expectation to be fulfilled.

The expectation is specified as a Boolean expression in Python syntax. The special identifier “value” refers to the actual value of each matrix element.

Base classes

- [`Expectation`](#ApiClient.Expectation "ApiClient.Expectation")

- [`AllExpectation`](#ApiClient.AllExpectation "ApiClient.AllExpectation")

Returned by

- [`ExpectationApi.CreateMatrixAllExpectation`](#ApiClient.ExpectationApi.CreateMatrixAllExpectation "ApiClient.ExpectationApi.CreateMatrixAllExpectation")

- [`ExpectationApi.CreateMatrixAllExpressionExpectation`](#ApiClient.ExpectationApi.CreateMatrixAllExpressionExpectation "ApiClient.ExpectationApi.CreateMatrixAllExpressionExpectation")

Clone()[¶](#ApiClient.MatrixAllExpectation.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`MatrixAllExpectation`](#ApiClient.MatrixAllExpectation "ApiClient.MatrixAllExpectation")

GetExpectation()[¶](#ApiClient.MatrixAllExpectation.GetExpectation "Link to this definition")  
Returns the expectation object.

Returns:  The expectation object

Return type:  [`Expectation`](#ApiClient.Expectation "ApiClient.Expectation")

GetExpectationExpression()[¶](#ApiClient.MatrixAllExpectation.GetExpectationExpression "Link to this definition")  
Returns the expectation expression.

Returns:  The expression

Return type:  str

SetExpectation(*expectationObject*)[¶](#ApiClient.MatrixAllExpectation.SetExpectation "Link to this definition")  
Sets the expectation object.

Parameters:  **expectationObject** ([`Expectation`](#ApiClient.Expectation "ApiClient.Expectation")) – The expectation object

SetExpectationExpression(*expression*)[¶](#ApiClient.MatrixAllExpectation.SetExpectationExpression "Link to this definition")  
Sets the expectation expression.

Parameters:  **expression** (*str*) – The expression

## MapAllExpectation[¶](#mapallexpectation "Link to this heading")

*class* MapAllExpectation[¶](#ApiClient.MapAllExpectation "Link to this definition")  
Represents an expectation on all elements of a map. All elements of the map must fulfill the expectation for this map expectation to be fulfilled.

The expectation is specified as a Boolean expression in Python syntax. The special identifier “value” refers to the actual value of each map element.

Base classes

- [`Expectation`](#ApiClient.Expectation "ApiClient.Expectation")

- [`AllExpectation`](#ApiClient.AllExpectation "ApiClient.AllExpectation")

Returned by

- [`ExpectationApi.CreateMapAllExpectation`](#ApiClient.ExpectationApi.CreateMapAllExpectation "ApiClient.ExpectationApi.CreateMapAllExpectation")

- [`ExpectationApi.CreateMapAllExpressionExpectation`](#ApiClient.ExpectationApi.CreateMapAllExpressionExpectation "ApiClient.ExpectationApi.CreateMapAllExpressionExpectation")

Clone()[¶](#ApiClient.MapAllExpectation.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`MapAllExpectation`](#ApiClient.MapAllExpectation "ApiClient.MapAllExpectation")

GetExpectation()[¶](#ApiClient.MapAllExpectation.GetExpectation "Link to this definition")  
Returns the expectation object.

Returns:  The expectation object

Return type:  [`Expectation`](#ApiClient.Expectation "ApiClient.Expectation")

GetExpectationExpression()[¶](#ApiClient.MapAllExpectation.GetExpectationExpression "Link to this definition")  
Returns the expectation expression.

Returns:  The expression

Return type:  str

SetExpectation(*expectationObject*)[¶](#ApiClient.MapAllExpectation.SetExpectation "Link to this definition")  
Sets the expectation object.

Parameters:  **expectationObject** ([`Expectation`](#ApiClient.Expectation "ApiClient.Expectation")) – The expectation object

SetExpectationExpression(*expression*)[¶](#ApiClient.MapAllExpectation.SetExpectationExpression "Link to this definition")  
Sets the expectation expression.

Parameters:  **expression** (*str*) – The expression

## ImageExpectation[¶](#imageexpectation "Link to this heading")

*class* ImageExpectation[¶](#ApiClient.ImageExpectation "Link to this definition")  
Base class

[`Expectation`](#ApiClient.Expectation "ApiClient.Expectation")

Returned by

- [`ExpectationApi.CreateImageExpectation`](#ApiClient.ExpectationApi.CreateImageExpectation "ApiClient.ExpectationApi.CreateImageExpectation")

Clone()[¶](#ApiClient.ImageExpectation.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`ImageExpectation`](#ApiClient.ImageExpectation "ApiClient.ImageExpectation")

GetColorTolerance()[¶](#ApiClient.ImageExpectation.GetColorTolerance "Link to this definition")  
Returns the color tolerance for pixel comparison.

Returns:  Per-pixel color tolerance (from 0 to 255)

Return type:  str

GetComparisonMethod()[¶](#ApiClient.ImageExpectation.GetComparisonMethod "Link to this definition")  
Returns the method that will be used to compare the two images.

Returns:  The method of comparison

Return type:  str

GetMediaReference()[¶](#ApiClient.ImageExpectation.GetMediaReference "Link to this definition")  
Returns the media access that will be used if the reference type is set to ‘media’.

Returns:  The media reference

Return type:  str

GetReference()[¶](#ApiClient.ImageExpectation.GetReference "Link to this definition")  
Returns the path to the reference image.

Returns:  Path to an image file

Return type:  str

GetReferenceType()[¶](#ApiClient.ImageExpectation.GetReferenceType "Link to this definition")  
Returns the method by which the image is referenced.

Returns:  Type of reference

Return type:  str

GetTolerance()[¶](#ApiClient.ImageExpectation.GetTolerance "Link to this definition")  
Returns the tolerance.

Returns:  The tolerance in percent from 0 to 100

Return type:  str

SetColorTolerance(*tolerance*)[¶](#ApiClient.ImageExpectation.SetColorTolerance "Link to this definition")  
Sets the color tolerance for pixel comparison. The tolerance defines the maximum deviation allowed for each color channel of a pixel. If any color deviates by more than this value from the reference pixel, the two pixels will be considered different.

Parameters:  **tolerance** (*str*) – Maximum allowed deviation for each color channel in each pixel (from 0 to 255)

SetComparisonMethod(*comparisonMethod*)[¶](#ApiClient.ImageExpectation.SetComparisonMethod "Link to this definition")  
Sets the method that will be used to compare the two images, i.e. if they should be equal or if the image should be contained within the reference image.

Parameters:  **comparisonMethod** (*str*) – One of “equal”, “notEqual”, “contains”, “containsNot”

SetMediaReference(*mediaReference*)[¶](#ApiClient.ImageExpectation.SetMediaReference "Link to this definition")  
Specifies which media reference to use. This will only have effect if the reference type is set to ‘media’ (see `SetReferenceType()`). E.g. if the active Test Configuration (.tcf) defines a media source called ‘CAM’ then the media reference should also be set to ‘CAM’ in order to access images relative to the ‘CAM’ media source.

Parameters:  **mediaReference** (*str*) – The reference to the media access

SetReference(*reference*)[¶](#ApiClient.ImageExpectation.SetReference "Link to this definition")  
Sets the path to the reference image that will be used for comparison.

Parameters:  **reference** (*str*) – Path to an image file

SetReferenceType(*referenceType*)[¶](#ApiClient.ImageExpectation.SetReferenceType "Link to this definition")  
Sets how the image path is referenced. If set to “object” the reference image is expected to be an absolute path. If set to “workspace” the path is evaluated relative to the workspace directory. If set to “media” the path is relative to one of the media directories defined in the current Test Configuration (.tcf). The concrete media reference can be specified with `SetMediaReference()`. Setting the reference type to ‘media’ will set the media reference to the first found media source if no other reference was specified.

Parameters:  **referenceType** (*str*) – One of “media”, “workspace”, “object”

SetTolerance(*tolerance*)[¶](#ApiClient.ImageExpectation.SetTolerance "Link to this definition")  
Sets the tolerance for image comparison. The tolerance defines the maximum percentage of pixels that may be different from the reference image, for which the two images will still be evaluated as equal. A tolerance of 0 signifies that no deviation will be tolerated - all pixels must be equal. With a tolerance of 100 all pixels could be different and the images would still be considered equal.

Parameters:  **tolerance** (*str*) – The tolerance in percent from 0 to 100
