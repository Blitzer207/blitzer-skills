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

[ API for Artifacts ](#)

API for Artifacts

- [ LocalArtifactReference ](ArtifactApi/LocalArtifactReference.md)
- [ TestGuideArtifactReference ](ArtifactApi/TestGuideArtifactReference.md)

API for Artifacts [ API for Artifacts ](#)

API for Artifacts

- [C ArtifactApi ](#ApiClient.ArtifactApi)
  - [M CreateLocalArtifactReference ](#ApiClient.ArtifactApi.CreateLocalArtifactReference)
  - [M CreateTestGuideArtifactReference ](#ApiClient.ArtifactApi.CreateTestGuideArtifactReference)
- [ LocalArtifactReference ](ArtifactApi/LocalArtifactReference.md)
- [ TestGuideArtifactReference ](ArtifactApi/TestGuideArtifactReference.md)

[ API for Project Components ](ComponentApi.md)

[ API for Configurations ](ConfigurationApi.md)

[ API for Expectations ](ExpectationApi.md)

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

API for Artifacts

- [C ArtifactApi ](#ApiClient.ArtifactApi)
  - [M CreateLocalArtifactReference ](#ApiClient.ArtifactApi.CreateLocalArtifactReference)
  - [M CreateTestGuideArtifactReference ](#ApiClient.ArtifactApi.CreateTestGuideArtifactReference)

# API for Artifacts[¶](#api-for-artifacts "Link to this heading")

Part of the [Object based program API](objectApi.md#objectapi).

*class* ArtifactApi[¶](#ApiClient.ArtifactApi "Link to this definition")  
Returned by

- [`ApiClient.ArtifactApi`](objectApi.md#ApiClient.ApiClient.ArtifactApi "ApiClient.ApiClient.ArtifactApi (Python attribute) — Returns the ArtifactApi namespace.")

CreateLocalArtifactReference(*[filePath](#ApiClient.ArtifactApi.CreateLocalArtifactReference.filePath "ApiClient.ArtifactApi.CreateLocalArtifactReference.filePath (Python parameter) — Path of the file.")*, *[namespace](#ApiClient.ArtifactApi.CreateLocalArtifactReference.namespace "ApiClient.ArtifactApi.CreateLocalArtifactReference.namespace (Python parameter) — Identifier of the workspace to which a relative filePath is resolved.")=`None`*)[¶](#ApiClient.ArtifactApi.CreateLocalArtifactReference "Link to this definition")  
Creates a new LocalArtifactReference.

Parameters:  filePath : str[¶](#ApiClient.ArtifactApi.CreateLocalArtifactReference.filePath "Permalink to this definition")  
Path of the file.

namespace : str[¶](#ApiClient.ArtifactApi.CreateLocalArtifactReference.namespace "Permalink to this definition")  
Identifier of the workspace to which a relative filePath is resolved. If not present or None, the namespace is determined automatically. It is also possible to reference a library workspace using its namespace. A relative filePath is resolved relative to the parameters directory of the given namespace. For example, the namespace parameter ‘myLibrary’ results in ‘\<libraries.myLibrary.parameters\>/MyMapping.xam’.

Returns:  LocalArtifactReference object.

Return type:  [`LocalArtifactReference`](ArtifactApi/LocalArtifactReference.md#ApiClient.LocalArtifactReference "ApiClient.LocalArtifactReference (Python class) — ArtifactApi.CreateLocalArtifactReference")

CreateTestGuideArtifactReference(*[depositoryName](#ApiClient.ArtifactApi.CreateTestGuideArtifactReference.depositoryName "ApiClient.ArtifactApi.CreateTestGuideArtifactReference.depositoryName (Python parameter) — Name of the depository as defined in the workspace settings.")*, *[artifactId](#ApiClient.ArtifactApi.CreateTestGuideArtifactReference.artifactId "ApiClient.ArtifactApi.CreateTestGuideArtifactReference.artifactId (Python parameter) — ID of the artifact in the depository.")*, *[artifactName](#ApiClient.ArtifactApi.CreateTestGuideArtifactReference.artifactName "ApiClient.ArtifactApi.CreateTestGuideArtifactReference.artifactName (Python parameter) — Name of the artifact (including extension).")*)[¶](#ApiClient.ArtifactApi.CreateTestGuideArtifactReference "Link to this definition")  
Creates a new TestGuideArtifactReference.

Parameters:  depositoryName : str[¶](#ApiClient.ArtifactApi.CreateTestGuideArtifactReference.depositoryName "Permalink to this definition")  
Name of the depository as defined in the workspace settings.

artifactId : str[¶](#ApiClient.ArtifactApi.CreateTestGuideArtifactReference.artifactId "Permalink to this definition")  
ID of the artifact in the depository.

artifactName : str[¶](#ApiClient.ArtifactApi.CreateTestGuideArtifactReference.artifactName "Permalink to this definition")  
Name of the artifact (including extension).

Returns:  TestGuideArtifactReference object.

Return type:  [`TestGuideArtifactReference`](ArtifactApi/TestGuideArtifactReference.md#ApiClient.TestGuideArtifactReference "ApiClient.TestGuideArtifactReference (Python class) — ArtifactApi.CreateTestGuideArtifactReference")

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
