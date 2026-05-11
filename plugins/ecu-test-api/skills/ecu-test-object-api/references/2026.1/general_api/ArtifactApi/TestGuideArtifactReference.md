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

API for Artifacts

[ LocalArtifactReference ](LocalArtifactReference.md)

TestGuideArtifactReference [ TestGuideArtifactReference ](#)

TestGuideArtifactReference

- [C TestGuideArtifactReference ](#ApiClient.TestGuideArtifactReference)
  - [M Clone ](#ApiClient.TestGuideArtifactReference.Clone)
  - [M GetArtifactId ](#ApiClient.TestGuideArtifactReference.GetArtifactId)
  - [M GetArtifactName ](#ApiClient.TestGuideArtifactReference.GetArtifactName)
  - [M GetDepositoryAlias ](#ApiClient.TestGuideArtifactReference.GetDepositoryAlias)
  - [M GetSourceType ](#ApiClient.TestGuideArtifactReference.GetSourceType)

[ API for Project Components ](../ComponentApi.md)

[ API for Configurations ](../ConfigurationApi.md)

[ API for Expectations ](../ExpectationApi.md)

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

TestGuideArtifactReference

- [C TestGuideArtifactReference ](#ApiClient.TestGuideArtifactReference)
  - [M Clone ](#ApiClient.TestGuideArtifactReference.Clone)
  - [M GetArtifactId ](#ApiClient.TestGuideArtifactReference.GetArtifactId)
  - [M GetArtifactName ](#ApiClient.TestGuideArtifactReference.GetArtifactName)
  - [M GetDepositoryAlias ](#ApiClient.TestGuideArtifactReference.GetDepositoryAlias)
  - [M GetSourceType ](#ApiClient.TestGuideArtifactReference.GetSourceType)

# TestGuideArtifactReference[¶](#testguideartifactreference "Link to this heading")

*class* TestGuideArtifactReference[¶](#ApiClient.TestGuideArtifactReference "Link to this definition")  
Returned by

- [`ArtifactApi.CreateTestGuideArtifactReference`](../ArtifactApi.md#ApiClient.ArtifactApi.CreateTestGuideArtifactReference "ApiClient.ArtifactApi.CreateTestGuideArtifactReference (Python method) — Creates a new TestGuideArtifactReference.")

Clone()[¶](#ApiClient.TestGuideArtifactReference.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`TestGuideArtifactReference`](#ApiClient.TestGuideArtifactReference "ApiClient.TestGuideArtifactReference (Python class) — ArtifactApi.CreateTestGuideArtifactReference")

GetArtifactId()[¶](#ApiClient.TestGuideArtifactReference.GetArtifactId "Link to this definition")  
Returns the Artifact ID in the depository.

Returns:  Artifact ID

Return type:  str

GetArtifactName()[¶](#ApiClient.TestGuideArtifactReference.GetArtifactName "Link to this definition")  
Returns the name of the artifact.

Returns:  Artifact name.

Return type:  str

GetDepositoryAlias()[¶](#ApiClient.TestGuideArtifactReference.GetDepositoryAlias "Link to this definition")  
Returns the alias of the test.guide depository the artifact is located at. This refers to the depository name as defined in the workspace settings.

Returns:  Depository alias

Return type:  str

GetSourceType()[¶](#ApiClient.TestGuideArtifactReference.GetSourceType "Link to this definition")  
Returns artifact source type.

Returns:  name of source type

Return type:  str

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
