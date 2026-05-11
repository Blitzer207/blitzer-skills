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

AudioExpectation [ AudioExpectation ](#)

AudioExpectation

- [C AudioExpectation ](#ApiClient.AudioExpectation)
  - [M Clone ](#ApiClient.AudioExpectation.Clone)
  - [M GetComparisonMethod ](#ApiClient.AudioExpectation.GetComparisonMethod)
  - [M GetNoiseResistantComparison ](#ApiClient.AudioExpectation.GetNoiseResistantComparison)
  - [M GetReference ](#ApiClient.AudioExpectation.GetReference)
  - [M GetReferenceType ](#ApiClient.AudioExpectation.GetReferenceType)
  - [M GetThreshold ](#ApiClient.AudioExpectation.GetThreshold)
  - [M SetComparisonMethod ](#ApiClient.AudioExpectation.SetComparisonMethod)
  - [M SetNoiseResistantComparison ](#ApiClient.AudioExpectation.SetNoiseResistantComparison)
  - [M SetReference ](#ApiClient.AudioExpectation.SetReference)
  - [M SetReferenceType ](#ApiClient.AudioExpectation.SetReferenceType)
  - [M SetThreshold ](#ApiClient.AudioExpectation.SetThreshold)

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

AudioExpectation

- [C AudioExpectation ](#ApiClient.AudioExpectation)
  - [M Clone ](#ApiClient.AudioExpectation.Clone)
  - [M GetComparisonMethod ](#ApiClient.AudioExpectation.GetComparisonMethod)
  - [M GetNoiseResistantComparison ](#ApiClient.AudioExpectation.GetNoiseResistantComparison)
  - [M GetReference ](#ApiClient.AudioExpectation.GetReference)
  - [M GetReferenceType ](#ApiClient.AudioExpectation.GetReferenceType)
  - [M GetThreshold ](#ApiClient.AudioExpectation.GetThreshold)
  - [M SetComparisonMethod ](#ApiClient.AudioExpectation.SetComparisonMethod)
  - [M SetNoiseResistantComparison ](#ApiClient.AudioExpectation.SetNoiseResistantComparison)
  - [M SetReference ](#ApiClient.AudioExpectation.SetReference)
  - [M SetReferenceType ](#ApiClient.AudioExpectation.SetReferenceType)
  - [M SetThreshold ](#ApiClient.AudioExpectation.SetThreshold)

# AudioExpectation[¶](#audioexpectation "Link to this heading")

*class* AudioExpectation[¶](#ApiClient.AudioExpectation "Link to this definition")  
Returned by

- [`ExpectationApi.CreateAudioExpectation`](../ExpectationApi.md#ApiClient.ExpectationApi.CreateAudioExpectation "ApiClient.ExpectationApi.CreateAudioExpectation (Python method) — Creates an audio expectation.")

Clone()[¶](#ApiClient.AudioExpectation.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`AudioExpectation`](#ApiClient.AudioExpectation "ApiClient.AudioExpectation (Python class) — ExpectationApi.CreateAudioExpectation")

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

SetComparisonMethod(*[comparisonMethod](#ApiClient.AudioExpectation.SetComparisonMethod.comparisonMethod "ApiClient.AudioExpectation.SetComparisonMethod.comparisonMethod (Python parameter) — Either "contains" or "containsNot"")*)[¶](#ApiClient.AudioExpectation.SetComparisonMethod "Link to this definition")  
Sets the method that will be used to compare the two audio blocks.

Parameters:  comparisonMethod : str[¶](#ApiClient.AudioExpectation.SetComparisonMethod.comparisonMethod "Permalink to this definition")  
Either “contains” or “containsNot”

SetNoiseResistantComparison(*[noiseResistantComparison](#ApiClient.AudioExpectation.SetNoiseResistantComparison.noiseResistantComparison "ApiClient.AudioExpectation.SetNoiseResistantComparison.noiseResistantComparison (Python parameter) — Whether to activate the noise resistant comparison.")*)[¶](#ApiClient.AudioExpectation.SetNoiseResistantComparison "Link to this definition")  
Specifies whether the audio samples should be campared with an algorithm that is designed to be resistant to noise. This option should only be activated if the recording actually contains noise. For recordings without noise the normal comparison provides more robust results. Pleae note that the confidence values will generally be lower when using the noise resistant comparison since a different metric will be used.

Parameters:  noiseResistantComparison : bool[¶](#ApiClient.AudioExpectation.SetNoiseResistantComparison.noiseResistantComparison "Permalink to this definition")  
Whether to activate the noise resistant comparison.

SetReference(*[reference](#ApiClient.AudioExpectation.SetReference.reference "ApiClient.AudioExpectation.SetReference.reference (Python parameter) — Path to an audio file or name of a variable.")*)[¶](#ApiClient.AudioExpectation.SetReference "Link to this definition")  
Sets the current audio reference expression. Depending on the configured reference type this may be either a path to an audio file or the name of an AudioBlock variable.

Parameters:  reference : str[¶](#ApiClient.AudioExpectation.SetReference.reference "Permalink to this definition")  
Path to an audio file or name of a variable.

SetReferenceType(*[referenceType](#ApiClient.AudioExpectation.SetReferenceType.referenceType "ApiClient.AudioExpectation.SetReferenceType.referenceType (Python parameter) — Either "object" or "workspace"")*)[¶](#ApiClient.AudioExpectation.SetReferenceType "Link to this definition")  
Sets how the audio is referenced. If the type is set to “object”, the reference expression is expected to contain a variable name. The variable must contain an AudioBlock. If the type is set to “workspace” the reference should contain a path relative to the current workspace. The actual audio reference expression can be set with `SetReference()`.

Parameters:  referenceType : str[¶](#ApiClient.AudioExpectation.SetReferenceType.referenceType "Permalink to this definition")  
Either “object” or “workspace”

SetThreshold(*[threshold](#ApiClient.AudioExpectation.SetThreshold.threshold "ApiClient.AudioExpectation.SetThreshold.threshold (Python parameter) — Expression for the confidence threshold")*)[¶](#ApiClient.AudioExpectation.SetThreshold "Link to this definition")  
Sets the minimum confidence value that a match should have to be considered a match. Only if the reference sample is found with a confidence higher than the given threshold will the test step be evaluated with SUCCES.

Parameters:  threshold : str[¶](#ApiClient.AudioExpectation.SetThreshold.threshold "Permalink to this definition")  
Expression for the confidence threshold

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
