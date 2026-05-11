# API for Expressions[¶](#api-for-expressions "Link to this heading")

Part of the [Object based program API](objectApi.md#objectapi)

## ExpressionApi[¶](#expressionapi "Link to this heading")

*class* ExpressionApi[¶](#ApiClient.ExpressionApi "Link to this definition")  
Returned by

- [`PackageApi.ExpressionApi`](PackageApi.md#ApiClient.PackageApi.ExpressionApi "ApiClient.PackageApi.ExpressionApi")

CreateCurveExpression(*length*, *defaultValue=None*, *distributionDefaultValue=None*)[¶](#ApiClient.ExpressionApi.CreateCurveExpression "Link to this definition")  
Creates a CurveExpression

Parameters:  - **length** (*int*) – maximum number of elements

- **defaultValue** (*str*) – Expression to be used as default value

- **distributionDefaultValue** (*str*) – Expression to be used as default value for distribution

Returns:  The curve expression

Return type:  [`CurveExpression`](#ApiClient.CurveExpression "ApiClient.CurveExpression")

CreateKeywordValueExpression(*value*)[¶](#ApiClient.ExpressionApi.CreateKeywordValueExpression "Link to this definition")  
Creates a KeywordValue expression that uses the identifier to a localization object.

Parameters:  **value** (*int*) – The value that refers to a localization identifier.

Returns:  The KeywordValue expression

Return type:  [`KeywordValueExpression`](#ApiClient.KeywordValueExpression "ApiClient.KeywordValueExpression")

CreateMapExpression(*xDimension*, *yDimension*, *defaultValue=None*, *xDistributionDefaultValue=None*, *yDistributionDefaultValue=None*)[¶](#ApiClient.ExpressionApi.CreateMapExpression "Link to this definition")  
Creates a MapExpression

Parameters:  - **xDimension** (*int*) – maximum number of elements in x dimension

- **yDimension** (*int*) – maximum number of elements in y dimension

- **defaultValue** (*str*) – Expression to be used as default value

- **xDistributionDefaultValue** (*str*) – Expression to be used as default value for x distribution

- **yDistributionDefaultValue** (*str*) – Expression to be used as default value for y distribution

Returns:  The map expression

Return type:  [`MapExpression`](#ApiClient.MapExpression "ApiClient.MapExpression")

CreateMatrixExpression(*xDimension*, *yDimension*, *defaultValue=None*)[¶](#ApiClient.ExpressionApi.CreateMatrixExpression "Link to this definition")  
Creates a MatrixExpression

Parameters:  - **xDimension** (*int*) – maximum number of elements in x dimension

- **yDimension** (*int*) – maximum number of elements in y dimension

- **defaultValue** (*str*) – Expression to be used as default value

Returns:  The matrix expression

Return type:  [`MatrixExpression`](#ApiClient.MatrixExpression "ApiClient.MatrixExpression")

CreateVectorExpression(*length*, *defaultValue=None*)[¶](#ApiClient.ExpressionApi.CreateVectorExpression "Link to this definition")  
Creates a VectorExpression

Parameters:  - **length** (*int*) – maximum number of elements

- **defaultValue** (*str*) – Expression to be used as default value

Returns:  The vector expression

Return type:  [`VectorExpression`](#ApiClient.VectorExpression "ApiClient.VectorExpression")

## CurveExpression[¶](#curveexpression "Link to this heading")

*class* CurveExpression[¶](#ApiClient.CurveExpression "Link to this definition")  
Base classes

- [`Expression`](#ApiClient.Expression "ApiClient.Expression")

- [`VectorExpression`](#ApiClient.VectorExpression "ApiClient.VectorExpression")

Returned by

- [`ExpressionApi.CreateCurveExpression`](#ApiClient.ExpressionApi.CreateCurveExpression "ApiClient.ExpressionApi.CreateCurveExpression")

Clone()[¶](#ApiClient.CurveExpression.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`CurveExpression`](#ApiClient.CurveExpression "ApiClient.CurveExpression")

GetDefaultValue()[¶](#ApiClient.CurveExpression.GetDefaultValue "Link to this definition")  
Returns the default value which is used as a fallback if no explicit value for an element is defined.

Returns:  Expression used as default value

Return type:  str

GetDimension()[¶](#ApiClient.CurveExpression.GetDimension "Link to this definition")  
Returns the length of the vector.

Returns:  maximum number of elements

Return type:  int

GetDistributionDefaultValue()[¶](#ApiClient.CurveExpression.GetDistributionDefaultValue "Link to this definition")  
Returns the default value which is used as a fallback if no explicit value for a distribution element is defined.

Returns:  Expression to be used as default value for distribution

Return type:  str

GetDistributionValue(*index*)[¶](#ApiClient.CurveExpression.GetDistributionValue "Link to this definition")  
Gets the distribution level of the given position.

Parameters:  **index** (*int*) – Element position to return

Returns:  distribution value

Return type:  str

GetDistributionValues()[¶](#ApiClient.CurveExpression.GetDistributionValues "Link to this definition")  
Returns a list of all distribution values. Values not explicitely set are represented by the default value.

Returns:  Sorted list containing all distribution values

Return type:  list[str]

GetValue(*index*)[¶](#ApiClient.CurveExpression.GetValue "Link to this definition")  
Returns the expression defining an elements value.

Parameters:  **index** (*int*) – Element position to get

Returns:  Expression

Return type:  str

GetValues()[¶](#ApiClient.CurveExpression.GetValues "Link to this definition")  
Returns a list of all values. Values not explicitely set are represented by the default value.

Returns:  Sorted list containing all values

Return type:  list[str]

RemoveDistributionValue(*index*)[¶](#ApiClient.CurveExpression.RemoveDistributionValue "Link to this definition")  
Removess the distribution value of the given index.

Parameters:  **index** (*int*) – Element position to remove

RemoveValue(*index*)[¶](#ApiClient.CurveExpression.RemoveValue "Link to this definition")  
Removess the expression defining an elements value.

Parameters:  **index** (*int*) – Element position to remove

SetDefaultValue(*value*)[¶](#ApiClient.CurveExpression.SetDefaultValue "Link to this definition")  
Sets the default value which is used as a fallback if no explicit value for an element is defined.

Parameters:  **value** (*str*) – Expression to be used as default value

SetDistributionDefaultValue(*value*)[¶](#ApiClient.CurveExpression.SetDistributionDefaultValue "Link to this definition")  
Sets the default value which is used as a fallback if no explicit value for a distribution element is defined.

Parameters:  **value** (*str*) – Expression to be used as default value for distribution

SetDistributionValue(*index*, *value*)[¶](#ApiClient.CurveExpression.SetDistributionValue "Link to this definition")  
Sets the distribution value of the given position.

Parameters:  - **index** (*int*) – Element position to set

- **value** (*str*) – Expression

SetValue(*index*, *value*)[¶](#ApiClient.CurveExpression.SetValue "Link to this definition")  
Sets the expression defining an elements value.

Parameters:  - **index** (*int*) – Element position to set

- **value** (*str*) – Expression

## Expression[¶](#expression "Link to this heading")

*class* Expression[¶](#ApiClient.Expression "Link to this definition")  
Returned by

- [`TsWrite.GetComplexValue`](TestStepApi.md#ApiClient.TsWrite.GetComplexValue "ApiClient.TsWrite.GetComplexValue")

Subclasses

- [`CurveExpression`](#ApiClient.CurveExpression "ApiClient.CurveExpression")

- [`ExpressionValue`](#ApiClient.ExpressionValue "ApiClient.ExpressionValue")

- [`KeywordValueExpression`](#ApiClient.KeywordValueExpression "ApiClient.KeywordValueExpression")

- [`MapExpression`](#ApiClient.MapExpression "ApiClient.MapExpression")

- [`MatrixExpression`](#ApiClient.MatrixExpression "ApiClient.MatrixExpression")

- [`VectorExpression`](#ApiClient.VectorExpression "ApiClient.VectorExpression")

Clone()[¶](#ApiClient.Expression.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`Expression`](#ApiClient.Expression "ApiClient.Expression")

## KeywordValueExpression[¶](#keywordvalueexpression "Link to this heading")

*class* KeywordValueExpression[¶](#ApiClient.KeywordValueExpression "Link to this definition")  
Base classes

- [`Expression`](#ApiClient.Expression "ApiClient.Expression")

- [`ExpressionValue`](#ApiClient.ExpressionValue "ApiClient.ExpressionValue")

Returned by

- [`ExpressionApi.CreateKeywordValueExpression`](#ApiClient.ExpressionApi.CreateKeywordValueExpression "ApiClient.ExpressionApi.CreateKeywordValueExpression")

- [`StringExpectation.GetExpressionObject`](ExpectationApi.md#ApiClient.StringExpectation.GetExpressionObject "ApiClient.StringExpectation.GetExpressionObject")

- [`StringListExpectation.GetExpressionList`](ExpectationApi.md#ApiClient.StringListExpectation.GetExpressionList "ApiClient.StringListExpectation.GetExpressionList")

- [`TsKeywordArgument.GetKeywordValueExpression`](TestStepApi.md#ApiClient.TsKeywordArgument.GetKeywordValueExpression "ApiClient.TsKeywordArgument.GetKeywordValueExpression")

Clone()[¶](#ApiClient.KeywordValueExpression.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`KeywordValueExpression`](#ApiClient.KeywordValueExpression "ApiClient.KeywordValueExpression")

GetValue()[¶](#ApiClient.KeywordValueExpression.GetValue "Link to this definition")  
Returns the value that refers to a localization identifier.

Returns:  The localization identifier

Return type:  int

## ExpressionValue[¶](#expressionvalue "Link to this heading")

*class* ExpressionValue[¶](#ApiClient.ExpressionValue "Link to this definition")  
Base class

[`Expression`](#ApiClient.Expression "ApiClient.Expression")

Subclasses

- [`KeywordValueExpression`](#ApiClient.KeywordValueExpression "ApiClient.KeywordValueExpression")

Clone()[¶](#ApiClient.ExpressionValue.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`ExpressionValue`](#ApiClient.ExpressionValue "ApiClient.ExpressionValue")

## MatrixExpression[¶](#matrixexpression "Link to this heading")

*class* MatrixExpression[¶](#ApiClient.MatrixExpression "Link to this definition")  
Base class

[`Expression`](#ApiClient.Expression "ApiClient.Expression")

Returned by

- [`ExpressionApi.CreateMatrixExpression`](#ApiClient.ExpressionApi.CreateMatrixExpression "ApiClient.ExpressionApi.CreateMatrixExpression")

- [`TsReport.GetTable`](TestStepApi.md#ApiClient.TsReport.GetTable "ApiClient.TsReport.GetTable")

Subclasses

- [`MapExpression`](#ApiClient.MapExpression "ApiClient.MapExpression")

Clone()[¶](#ApiClient.MatrixExpression.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`MatrixExpression`](#ApiClient.MatrixExpression "ApiClient.MatrixExpression")

GetDefaultValue()[¶](#ApiClient.MatrixExpression.GetDefaultValue "Link to this definition")  
Returns the default value which is used as a fallback if no explicit value for an element is defined.

Returns:  Expression used as default value

Return type:  str

GetLines()[¶](#ApiClient.MatrixExpression.GetLines "Link to this definition")  
Returns a list of values for all lines. Each line itself is also a list of all the values within the line. Values not explicitely set are represented by the default value.

Returns:  Sorted list containing all values

Return type:  list[list[str]]

GetValue(*xIndex*, *yIndex*)[¶](#ApiClient.MatrixExpression.GetValue "Link to this definition")  
Returns the expression defining an element’s value.

Parameters:  - **xIndex** (*int*) – Elements x position

- **yIndex** (*int*) – Elements y position

Returns:  Expression

Return type:  str

GetXDimension()[¶](#ApiClient.MatrixExpression.GetXDimension "Link to this definition")  
Returns the x dimension of the matrix.

Returns:  maximum number of elements in x dimension

Return type:  int

GetYDimension()[¶](#ApiClient.MatrixExpression.GetYDimension "Link to this definition")  
Returns the y dimension of the matrix.

Returns:  maximum number of elements in y dimension

Return type:  int

RemoveValue(*xIndex*, *yIndex*)[¶](#ApiClient.MatrixExpression.RemoveValue "Link to this definition")  
Removes the expression defining an element’s value.

Parameters:  - **xIndex** (*int*) – Elements x position

- **yIndex** (*int*) – Elements y position

SetDefaultValue(*value*)[¶](#ApiClient.MatrixExpression.SetDefaultValue "Link to this definition")  
Sets the default value which is used as a fallback if no explicit value for an element is defined.

Parameters:  **value** (*str*) – Expression to be used as default value

SetValue(*xIndex*, *yIndex*, *value*)[¶](#ApiClient.MatrixExpression.SetValue "Link to this definition")  
Sets the expression defining an element’s value.

Parameters:  - **xIndex** (*int*) – Elements x position

- **yIndex** (*int*) – Elements y position

- **value** (*str*) – Expression

## MapExpression[¶](#mapexpression "Link to this heading")

*class* MapExpression[¶](#ApiClient.MapExpression "Link to this definition")  
Base classes

- [`Expression`](#ApiClient.Expression "ApiClient.Expression")

- [`MatrixExpression`](#ApiClient.MatrixExpression "ApiClient.MatrixExpression")

Returned by

- [`ExpressionApi.CreateMapExpression`](#ApiClient.ExpressionApi.CreateMapExpression "ApiClient.ExpressionApi.CreateMapExpression")

Clone()[¶](#ApiClient.MapExpression.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`MapExpression`](#ApiClient.MapExpression "ApiClient.MapExpression")

GetDefaultValue()[¶](#ApiClient.MapExpression.GetDefaultValue "Link to this definition")  
Returns the default value which is used as a fallback if no explicit value for an element is defined.

Returns:  Expression used as default value

Return type:  str

GetLines()[¶](#ApiClient.MapExpression.GetLines "Link to this definition")  
Returns a list of values for all lines. Each line itself is also a list of all the values within the line. Values not explicitely set are represented by the default value.

Returns:  Sorted list containing all values

Return type:  list[list[str]]

GetValue(*xIndex*, *yIndex*)[¶](#ApiClient.MapExpression.GetValue "Link to this definition")  
Returns the expression defining an element’s value.

Parameters:  - **xIndex** (*int*) – Elements x position

- **yIndex** (*int*) – Elements y position

Returns:  Expression

Return type:  str

GetXDimension()[¶](#ApiClient.MapExpression.GetXDimension "Link to this definition")  
Returns the x dimension of the matrix.

Returns:  maximum number of elements in x dimension

Return type:  int

GetXDistributionDefaultValue()[¶](#ApiClient.MapExpression.GetXDistributionDefaultValue "Link to this definition")  
Returns the default value which is used as a fallback if no explicit value for a distribution element on the x axis is defined.

Returns:  Expression to be used as default value for distribution

Return type:  str

GetXDistributionValue(*index*)[¶](#ApiClient.MapExpression.GetXDistributionValue "Link to this definition")  
Gets the x distribution level of the given position.

Parameters:  **index** (*int*) – Element position to return

Returns:  distribution value

Return type:  str

GetXDistributionValues()[¶](#ApiClient.MapExpression.GetXDistributionValues "Link to this definition")  
Returns a list of all x distribution values. Values not explicitely set are represented by the default value.

Returns:  Sorted list containing all x distribution values

Return type:  list[str]

GetYDimension()[¶](#ApiClient.MapExpression.GetYDimension "Link to this definition")  
Returns the y dimension of the matrix.

Returns:  maximum number of elements in y dimension

Return type:  int

GetYDistributionDefaultValue()[¶](#ApiClient.MapExpression.GetYDistributionDefaultValue "Link to this definition")  
Returns the default value which is used as a fallback if no explicit value for a distribution element on the y axis is defined.

Returns:  Expression to be used as default value for distribution

Return type:  str

GetYDistributionValue(*index*)[¶](#ApiClient.MapExpression.GetYDistributionValue "Link to this definition")  
Gets the y distribution level of the given position.

Parameters:  **index** (*int*) – Element position to return

Returns:  distribution value

Return type:  str

GetYDistributionValues()[¶](#ApiClient.MapExpression.GetYDistributionValues "Link to this definition")  
Returns a list of all y distribution values. Values not explicitely set are represented by the default value.

Returns:  Sorted list containing all y distribution values

Return type:  list[str]

RemoveValue(*xIndex*, *yIndex*)[¶](#ApiClient.MapExpression.RemoveValue "Link to this definition")  
Removes the expression defining an element’s value.

Parameters:  - **xIndex** (*int*) – Elements x position

- **yIndex** (*int*) – Elements y position

RemoveXDistributionValue(*index*)[¶](#ApiClient.MapExpression.RemoveXDistributionValue "Link to this definition")  
Removes the x distribution value of the given index.

Parameters:  **index** (*int*) – Element position to remove

RemoveYDistributionValue(*index*)[¶](#ApiClient.MapExpression.RemoveYDistributionValue "Link to this definition")  
Removes the y distribution value of the given index.

Parameters:  **index** (*int*) – Element position to remove

SetDefaultValue(*value*)[¶](#ApiClient.MapExpression.SetDefaultValue "Link to this definition")  
Sets the default value which is used as a fallback if no explicit value for an element is defined.

Parameters:  **value** (*str*) – Expression to be used as default value

SetValue(*xIndex*, *yIndex*, *value*)[¶](#ApiClient.MapExpression.SetValue "Link to this definition")  
Sets the expression defining an element’s value.

Parameters:  - **xIndex** (*int*) – Elements x position

- **yIndex** (*int*) – Elements y position

- **value** (*str*) – Expression

SetXDistributionDefaultValue(*value*)[¶](#ApiClient.MapExpression.SetXDistributionDefaultValue "Link to this definition")  
Sets the default value which is used as a fallback if no explicit value for a distribution element on the x axis is defined.

Parameters:  **value** (*str*) – Expression to be used as default value for distribution

SetXDistributionValue(*index*, *value*)[¶](#ApiClient.MapExpression.SetXDistributionValue "Link to this definition")  
Sets the y distribution value of the given position.

Parameters:  - **index** (*int*) – Element position to set

- **value** (*str*) – Expression

SetYDistributionDefaultValue(*value*)[¶](#ApiClient.MapExpression.SetYDistributionDefaultValue "Link to this definition")  
Sets the default value which is used as a fallback if no explicit value for a distribution element on the y axis is defined.

Parameters:  **value** (*str*) – Expression to be used as default value for distribution

SetYDistributionValue(*index*, *value*)[¶](#ApiClient.MapExpression.SetYDistributionValue "Link to this definition")  
Sets the y distribution value of the given position.

Parameters:  - **index** (*int*) – Element position to set

- **value** (*str*) – Expression

## VectorExpression[¶](#vectorexpression "Link to this heading")

*class* VectorExpression[¶](#ApiClient.VectorExpression "Link to this definition")  
Base class

[`Expression`](#ApiClient.Expression "ApiClient.Expression")

Returned by

- [`ExpressionApi.CreateVectorExpression`](#ApiClient.ExpressionApi.CreateVectorExpression "ApiClient.ExpressionApi.CreateVectorExpression")

Subclasses

- [`CurveExpression`](#ApiClient.CurveExpression "ApiClient.CurveExpression")

Clone()[¶](#ApiClient.VectorExpression.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`VectorExpression`](#ApiClient.VectorExpression "ApiClient.VectorExpression")

GetDefaultValue()[¶](#ApiClient.VectorExpression.GetDefaultValue "Link to this definition")  
Returns the default value which is used as a fallback if no explicit value for an element is defined.

Returns:  Expression used as default value

Return type:  str

GetDimension()[¶](#ApiClient.VectorExpression.GetDimension "Link to this definition")  
Returns the length of the vector.

Returns:  maximum number of elements

Return type:  int

GetValue(*index*)[¶](#ApiClient.VectorExpression.GetValue "Link to this definition")  
Returns the expression defining an elements value.

Parameters:  **index** (*int*) – Element position to get

Returns:  Expression

Return type:  str

GetValues()[¶](#ApiClient.VectorExpression.GetValues "Link to this definition")  
Returns a list of all values. Values not explicitely set are represented by the default value.

Returns:  Sorted list containing all values

Return type:  list[str]

RemoveValue(*index*)[¶](#ApiClient.VectorExpression.RemoveValue "Link to this definition")  
Removess the expression defining an elements value.

Parameters:  **index** (*int*) – Element position to remove

SetDefaultValue(*value*)[¶](#ApiClient.VectorExpression.SetDefaultValue "Link to this definition")  
Sets the default value which is used as a fallback if no explicit value for an element is defined.

Parameters:  **value** (*str*) – Expression to be used as default value

SetValue(*index*, *value*)[¶](#ApiClient.VectorExpression.SetValue "Link to this definition")  
Sets the expression defining an elements value.

Parameters:  - **index** (*int*) – Element position to set

- **value** (*str*) – Expression
