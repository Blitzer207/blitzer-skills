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

ImageExpectation [ ImageExpectation ](#)

ImageExpectation

- [C ImageExpectation ](#ApiClient.ImageExpectation)
  - [M Clone ](#ApiClient.ImageExpectation.Clone)
  - [M GetColorTolerance ](#ApiClient.ImageExpectation.GetColorTolerance)
  - [M GetComparisonMethod ](#ApiClient.ImageExpectation.GetComparisonMethod)
  - [M GetMediaReference ](#ApiClient.ImageExpectation.GetMediaReference)
  - [M GetReference ](#ApiClient.ImageExpectation.GetReference)
  - [M GetReferenceType ](#ApiClient.ImageExpectation.GetReferenceType)
  - [M GetTolerance ](#ApiClient.ImageExpectation.GetTolerance)
  - [M SetColorTolerance ](#ApiClient.ImageExpectation.SetColorTolerance)
  - [M SetComparisonMethod ](#ApiClient.ImageExpectation.SetComparisonMethod)
  - [M SetMediaReference ](#ApiClient.ImageExpectation.SetMediaReference)
  - [M SetReference ](#ApiClient.ImageExpectation.SetReference)
  - [M SetReferenceType ](#ApiClient.ImageExpectation.SetReferenceType)
  - [M SetTolerance ](#ApiClient.ImageExpectation.SetTolerance)

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

ImageExpectation

- [C ImageExpectation ](#ApiClient.ImageExpectation)
  - [M Clone ](#ApiClient.ImageExpectation.Clone)
  - [M GetColorTolerance ](#ApiClient.ImageExpectation.GetColorTolerance)
  - [M GetComparisonMethod ](#ApiClient.ImageExpectation.GetComparisonMethod)
  - [M GetMediaReference ](#ApiClient.ImageExpectation.GetMediaReference)
  - [M GetReference ](#ApiClient.ImageExpectation.GetReference)
  - [M GetReferenceType ](#ApiClient.ImageExpectation.GetReferenceType)
  - [M GetTolerance ](#ApiClient.ImageExpectation.GetTolerance)
  - [M SetColorTolerance ](#ApiClient.ImageExpectation.SetColorTolerance)
  - [M SetComparisonMethod ](#ApiClient.ImageExpectation.SetComparisonMethod)
  - [M SetMediaReference ](#ApiClient.ImageExpectation.SetMediaReference)
  - [M SetReference ](#ApiClient.ImageExpectation.SetReference)
  - [M SetReferenceType ](#ApiClient.ImageExpectation.SetReferenceType)
  - [M SetTolerance ](#ApiClient.ImageExpectation.SetTolerance)

# ImageExpectation[¶](#imageexpectation "Link to this heading")

*class* ImageExpectation[¶](#ApiClient.ImageExpectation "Link to this definition")  
Returned by

- [`ExpectationApi.CreateImageExpectation`](../ExpectationApi.md#ApiClient.ExpectationApi.CreateImageExpectation "ApiClient.ExpectationApi.CreateImageExpectation (Python method) — Creates an image expectation.")

Clone()[¶](#ApiClient.ImageExpectation.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`ImageExpectation`](#ApiClient.ImageExpectation "ApiClient.ImageExpectation (Python class) — ExpectationApi.CreateImageExpectation")

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

SetColorTolerance(*[tolerance](#ApiClient.ImageExpectation.SetColorTolerance.tolerance "ApiClient.ImageExpectation.SetColorTolerance.tolerance (Python parameter) — Maximum allowed deviation for each color channel in each pixel (from 0 to 255)")*)[¶](#ApiClient.ImageExpectation.SetColorTolerance "Link to this definition")  
Sets the color tolerance for pixel comparison. The tolerance defines the maximum deviation allowed for each color channel of a pixel. If any color deviates by more than this value from the reference pixel, the two pixels will be considered different.

Parameters:  tolerance : str[¶](#ApiClient.ImageExpectation.SetColorTolerance.tolerance "Permalink to this definition")  
Maximum allowed deviation for each color channel in each pixel (from 0 to 255)

SetComparisonMethod(*[comparisonMethod](#ApiClient.ImageExpectation.SetComparisonMethod.comparisonMethod "ApiClient.ImageExpectation.SetComparisonMethod.comparisonMethod (Python parameter) — One of "equal", "notEqual", "contains", "containsNot"")*)[¶](#ApiClient.ImageExpectation.SetComparisonMethod "Link to this definition")  
Sets the method that will be used to compare the two images, i.e. if they should be equal or if the image should be contained within the reference image.

Parameters:  comparisonMethod : str[¶](#ApiClient.ImageExpectation.SetComparisonMethod.comparisonMethod "Permalink to this definition")  
One of “equal”, “notEqual”, “contains”, “containsNot”

SetMediaReference(*[mediaReference](#ApiClient.ImageExpectation.SetMediaReference.mediaReference "ApiClient.ImageExpectation.SetMediaReference.mediaReference (Python parameter) — The reference to the media access")*)[¶](#ApiClient.ImageExpectation.SetMediaReference "Link to this definition")  
Specifies which media reference to use. This will only have effect if the reference type is set to ‘media’ (see `SetReferenceType()`). E.g. if the active Test Configuration (.tcf) defines a media source called ‘CAM’ then the media reference should also be set to ‘CAM’ in order to access images relative to the ‘CAM’ media source.

Parameters:  mediaReference : str[¶](#ApiClient.ImageExpectation.SetMediaReference.mediaReference "Permalink to this definition")  
The reference to the media access

SetReference(*[reference](#ApiClient.ImageExpectation.SetReference.reference "ApiClient.ImageExpectation.SetReference.reference (Python parameter) — Path to an image file")*)[¶](#ApiClient.ImageExpectation.SetReference "Link to this definition")  
Sets the path to the reference image that will be used for comparison.

Parameters:  reference : str[¶](#ApiClient.ImageExpectation.SetReference.reference "Permalink to this definition")  
Path to an image file

SetReferenceType(*[referenceType](#ApiClient.ImageExpectation.SetReferenceType.referenceType "ApiClient.ImageExpectation.SetReferenceType.referenceType (Python parameter) — One of "media", "workspace", "object"")*)[¶](#ApiClient.ImageExpectation.SetReferenceType "Link to this definition")  
Sets how the image path is referenced. If set to “object” the reference image is expected to be an absolute path. If set to “workspace” the path is evaluated relative to the workspace directory. If set to “media” the path is relative to one of the media directories defined in the current Test Configuration (.tcf). The concrete media reference can be specified with `SetMediaReference()`. Setting the reference type to ‘media’ will set the media reference to the first found media source if no other reference was specified.

Parameters:  referenceType : str[¶](#ApiClient.ImageExpectation.SetReferenceType.referenceType "Permalink to this definition")  
One of “media”, “workspace”, “object”

SetTolerance(*[tolerance](#ApiClient.ImageExpectation.SetTolerance.tolerance "ApiClient.ImageExpectation.SetTolerance.tolerance (Python parameter) — The tolerance in percent from 0 to 100")*)[¶](#ApiClient.ImageExpectation.SetTolerance "Link to this definition")  
Sets the tolerance for image comparison. The tolerance defines the maximum percentage of pixels that may be different from the reference image, for which the two images will still be evaluated as equal. A tolerance of 0 signifies that no deviation will be tolerated - all pixels must be equal. With a tolerance of 100 all pixels could be different and the images would still be considered equal.

Parameters:  tolerance : str[¶](#ApiClient.ImageExpectation.SetTolerance.tolerance "Permalink to this definition")  
The tolerance in percent from 0 to 100

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
