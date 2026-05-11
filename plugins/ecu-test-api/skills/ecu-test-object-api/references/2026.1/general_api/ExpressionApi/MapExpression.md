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

[ API for Expressions ](../ExpressionApi.md)

API for Expressions

[ CurveExpression ](CurveExpression.md)

[ Expression ](Expression.md)

[ ExpressionValue ](ExpressionValue.md)

[ KeywordValueExpression ](KeywordValueExpression.md)

MapExpression [ MapExpression ](#)

MapExpression

- [C MapExpression ](#ApiClient.MapExpression)
  - [M Clone ](#ApiClient.MapExpression.Clone)
  - [M GetDefaultValue ](#ApiClient.MapExpression.GetDefaultValue)
  - [M GetLines ](#ApiClient.MapExpression.GetLines)
  - [M GetValue ](#ApiClient.MapExpression.GetValue)
  - [M GetXDimension ](#ApiClient.MapExpression.GetXDimension)
  - [M GetXDistributionDefaultValue ](#ApiClient.MapExpression.GetXDistributionDefaultValue)
  - [M GetXDistributionValue ](#ApiClient.MapExpression.GetXDistributionValue)
  - [M GetXDistributionValues ](#ApiClient.MapExpression.GetXDistributionValues)
  - [M GetYDimension ](#ApiClient.MapExpression.GetYDimension)
  - [M GetYDistributionDefaultValue ](#ApiClient.MapExpression.GetYDistributionDefaultValue)
  - [M GetYDistributionValue ](#ApiClient.MapExpression.GetYDistributionValue)
  - [M GetYDistributionValues ](#ApiClient.MapExpression.GetYDistributionValues)
  - [M RemoveValue ](#ApiClient.MapExpression.RemoveValue)
  - [M RemoveXDistributionValue ](#ApiClient.MapExpression.RemoveXDistributionValue)
  - [M RemoveYDistributionValue ](#ApiClient.MapExpression.RemoveYDistributionValue)
  - [M SetDefaultValue ](#ApiClient.MapExpression.SetDefaultValue)
  - [M SetValue ](#ApiClient.MapExpression.SetValue)
  - [M SetXDistributionDefaultValue ](#ApiClient.MapExpression.SetXDistributionDefaultValue)
  - [M SetXDistributionValue ](#ApiClient.MapExpression.SetXDistributionValue)
  - [M SetYDistributionDefaultValue ](#ApiClient.MapExpression.SetYDistributionDefaultValue)
  - [M SetYDistributionValue ](#ApiClient.MapExpression.SetYDistributionValue)

[ MatrixExpression ](MatrixExpression.md)

[ VectorExpression ](VectorExpression.md)

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

MapExpression

- [C MapExpression ](#ApiClient.MapExpression)
  - [M Clone ](#ApiClient.MapExpression.Clone)
  - [M GetDefaultValue ](#ApiClient.MapExpression.GetDefaultValue)
  - [M GetLines ](#ApiClient.MapExpression.GetLines)
  - [M GetValue ](#ApiClient.MapExpression.GetValue)
  - [M GetXDimension ](#ApiClient.MapExpression.GetXDimension)
  - [M GetXDistributionDefaultValue ](#ApiClient.MapExpression.GetXDistributionDefaultValue)
  - [M GetXDistributionValue ](#ApiClient.MapExpression.GetXDistributionValue)
  - [M GetXDistributionValues ](#ApiClient.MapExpression.GetXDistributionValues)
  - [M GetYDimension ](#ApiClient.MapExpression.GetYDimension)
  - [M GetYDistributionDefaultValue ](#ApiClient.MapExpression.GetYDistributionDefaultValue)
  - [M GetYDistributionValue ](#ApiClient.MapExpression.GetYDistributionValue)
  - [M GetYDistributionValues ](#ApiClient.MapExpression.GetYDistributionValues)
  - [M RemoveValue ](#ApiClient.MapExpression.RemoveValue)
  - [M RemoveXDistributionValue ](#ApiClient.MapExpression.RemoveXDistributionValue)
  - [M RemoveYDistributionValue ](#ApiClient.MapExpression.RemoveYDistributionValue)
  - [M SetDefaultValue ](#ApiClient.MapExpression.SetDefaultValue)
  - [M SetValue ](#ApiClient.MapExpression.SetValue)
  - [M SetXDistributionDefaultValue ](#ApiClient.MapExpression.SetXDistributionDefaultValue)
  - [M SetXDistributionValue ](#ApiClient.MapExpression.SetXDistributionValue)
  - [M SetYDistributionDefaultValue ](#ApiClient.MapExpression.SetYDistributionDefaultValue)
  - [M SetYDistributionValue ](#ApiClient.MapExpression.SetYDistributionValue)

# MapExpression[¶](#mapexpression "Link to this heading")

*class* MapExpression[¶](#ApiClient.MapExpression "Link to this definition")  
Returned by

- [`ExpressionApi.CreateMapExpression`](../ExpressionApi.md#ApiClient.ExpressionApi.CreateMapExpression "ApiClient.ExpressionApi.CreateMapExpression (Python method) — Creates a MapExpression")

Clone()[¶](#ApiClient.MapExpression.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`MapExpression`](#ApiClient.MapExpression "ApiClient.MapExpression (Python class) — ExpressionApi.CreateMapExpression")

GetDefaultValue()[¶](#ApiClient.MapExpression.GetDefaultValue "Link to this definition")  
Returns the default value which is used as a fallback if no explicit value for an element is defined.

Returns:  Expression used as default value

Return type:  str

GetLines()[¶](#ApiClient.MapExpression.GetLines "Link to this definition")  
Returns a list of values for all lines. Each line itself is also a list of all the values within the line. Values not explicitely set are represented by the default value.

Returns:  Sorted list containing all values

Return type:  list[list[str]]

GetValue(*[xIndex](#ApiClient.MapExpression.GetValue.xIndex "ApiClient.MapExpression.GetValue.xIndex (Python parameter) — Elements x position")*, *[yIndex](#ApiClient.MapExpression.GetValue.yIndex "ApiClient.MapExpression.GetValue.yIndex (Python parameter) — Elements y position")*)[¶](#ApiClient.MapExpression.GetValue "Link to this definition")  
Returns the expression defining an element’s value.

Parameters:  xIndex : int[¶](#ApiClient.MapExpression.GetValue.xIndex "Permalink to this definition")  
Elements x position

yIndex : int[¶](#ApiClient.MapExpression.GetValue.yIndex "Permalink to this definition")  
Elements y position

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

GetXDistributionValue(*[index](#ApiClient.MapExpression.GetXDistributionValue.index "ApiClient.MapExpression.GetXDistributionValue.index (Python parameter) — Element position to return")*)[¶](#ApiClient.MapExpression.GetXDistributionValue "Link to this definition")  
Gets the x distribution level of the given position.

Parameters:  index : int[¶](#ApiClient.MapExpression.GetXDistributionValue.index "Permalink to this definition")  
Element position to return

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

GetYDistributionValue(*[index](#ApiClient.MapExpression.GetYDistributionValue.index "ApiClient.MapExpression.GetYDistributionValue.index (Python parameter) — Element position to return")*)[¶](#ApiClient.MapExpression.GetYDistributionValue "Link to this definition")  
Gets the y distribution level of the given position.

Parameters:  index : int[¶](#ApiClient.MapExpression.GetYDistributionValue.index "Permalink to this definition")  
Element position to return

Returns:  distribution value

Return type:  str

GetYDistributionValues()[¶](#ApiClient.MapExpression.GetYDistributionValues "Link to this definition")  
Returns a list of all y distribution values. Values not explicitely set are represented by the default value.

Returns:  Sorted list containing all y distribution values

Return type:  list[str]

RemoveValue(*[xIndex](#ApiClient.MapExpression.RemoveValue.xIndex "ApiClient.MapExpression.RemoveValue.xIndex (Python parameter) — Elements x position")*, *[yIndex](#ApiClient.MapExpression.RemoveValue.yIndex "ApiClient.MapExpression.RemoveValue.yIndex (Python parameter) — Elements y position")*)[¶](#ApiClient.MapExpression.RemoveValue "Link to this definition")  
Removes the expression defining an element’s value.

Parameters:  xIndex : int[¶](#ApiClient.MapExpression.RemoveValue.xIndex "Permalink to this definition")  
Elements x position

yIndex : int[¶](#ApiClient.MapExpression.RemoveValue.yIndex "Permalink to this definition")  
Elements y position

RemoveXDistributionValue(*[index](#ApiClient.MapExpression.RemoveXDistributionValue.index "ApiClient.MapExpression.RemoveXDistributionValue.index (Python parameter) — Element position to remove")*)[¶](#ApiClient.MapExpression.RemoveXDistributionValue "Link to this definition")  
Removes the x distribution value of the given index.

Parameters:  index : int[¶](#ApiClient.MapExpression.RemoveXDistributionValue.index "Permalink to this definition")  
Element position to remove

RemoveYDistributionValue(*[index](#ApiClient.MapExpression.RemoveYDistributionValue.index "ApiClient.MapExpression.RemoveYDistributionValue.index (Python parameter) — Element position to remove")*)[¶](#ApiClient.MapExpression.RemoveYDistributionValue "Link to this definition")  
Removes the y distribution value of the given index.

Parameters:  index : int[¶](#ApiClient.MapExpression.RemoveYDistributionValue.index "Permalink to this definition")  
Element position to remove

SetDefaultValue(*[value](#ApiClient.MapExpression.SetDefaultValue.value "ApiClient.MapExpression.SetDefaultValue.value (Python parameter) — Expression to be used as default value")*)[¶](#ApiClient.MapExpression.SetDefaultValue "Link to this definition")  
Sets the default value which is used as a fallback if no explicit value for an element is defined.

Parameters:  value : str[¶](#ApiClient.MapExpression.SetDefaultValue.value "Permalink to this definition")  
Expression to be used as default value

SetValue(*[xIndex](#ApiClient.MapExpression.SetValue.xIndex "ApiClient.MapExpression.SetValue.xIndex (Python parameter) — Elements x position")*, *[yIndex](#ApiClient.MapExpression.SetValue.yIndex "ApiClient.MapExpression.SetValue.yIndex (Python parameter) — Elements y position")*, *[value](#ApiClient.MapExpression.SetValue.value "ApiClient.MapExpression.SetValue.value (Python parameter) — Expression")*)[¶](#ApiClient.MapExpression.SetValue "Link to this definition")  
Sets the expression defining an element’s value.

Parameters:  xIndex : int[¶](#ApiClient.MapExpression.SetValue.xIndex "Permalink to this definition")  
Elements x position

yIndex : int[¶](#ApiClient.MapExpression.SetValue.yIndex "Permalink to this definition")  
Elements y position

value : str[¶](#ApiClient.MapExpression.SetValue.value "Permalink to this definition")  
Expression

SetXDistributionDefaultValue(*[value](#ApiClient.MapExpression.SetXDistributionDefaultValue.value "ApiClient.MapExpression.SetXDistributionDefaultValue.value (Python parameter) — Expression to be used as default value for distribution")*)[¶](#ApiClient.MapExpression.SetXDistributionDefaultValue "Link to this definition")  
Sets the default value which is used as a fallback if no explicit value for a distribution element on the x axis is defined.

Parameters:  value : str[¶](#ApiClient.MapExpression.SetXDistributionDefaultValue.value "Permalink to this definition")  
Expression to be used as default value for distribution

SetXDistributionValue(*[index](#ApiClient.MapExpression.SetXDistributionValue.index "ApiClient.MapExpression.SetXDistributionValue.index (Python parameter) — Element position to set")*, *[value](#ApiClient.MapExpression.SetXDistributionValue.value "ApiClient.MapExpression.SetXDistributionValue.value (Python parameter) — Expression")*)[¶](#ApiClient.MapExpression.SetXDistributionValue "Link to this definition")  
Sets the y distribution value of the given position.

Parameters:  index : int[¶](#ApiClient.MapExpression.SetXDistributionValue.index "Permalink to this definition")  
Element position to set

value : str[¶](#ApiClient.MapExpression.SetXDistributionValue.value "Permalink to this definition")  
Expression

SetYDistributionDefaultValue(*[value](#ApiClient.MapExpression.SetYDistributionDefaultValue.value "ApiClient.MapExpression.SetYDistributionDefaultValue.value (Python parameter) — Expression to be used as default value for distribution")*)[¶](#ApiClient.MapExpression.SetYDistributionDefaultValue "Link to this definition")  
Sets the default value which is used as a fallback if no explicit value for a distribution element on the y axis is defined.

Parameters:  value : str[¶](#ApiClient.MapExpression.SetYDistributionDefaultValue.value "Permalink to this definition")  
Expression to be used as default value for distribution

SetYDistributionValue(*[index](#ApiClient.MapExpression.SetYDistributionValue.index "ApiClient.MapExpression.SetYDistributionValue.index (Python parameter) — Element position to set")*, *[value](#ApiClient.MapExpression.SetYDistributionValue.value "ApiClient.MapExpression.SetYDistributionValue.value (Python parameter) — Expression")*)[¶](#ApiClient.MapExpression.SetYDistributionValue "Link to this definition")  
Sets the y distribution value of the given position.

Parameters:  index : int[¶](#ApiClient.MapExpression.SetYDistributionValue.index "Permalink to this definition")  
Element position to set

value : str[¶](#ApiClient.MapExpression.SetYDistributionValue.value "Permalink to this definition")  
Expression

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
