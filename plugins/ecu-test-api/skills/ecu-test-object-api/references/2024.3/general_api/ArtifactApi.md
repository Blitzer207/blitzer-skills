# API for Artifacts[¶](#api-for-artifacts "Link to this heading")

Part of the [Object based program API](objectApi.md#objectapi)

## ArtifactApi[¶](#artifactapi "Link to this heading")

*class* ArtifactApi[¶](#ApiClient.ArtifactApi "Link to this definition")  
Returned by

- [`ApiClient.ArtifactApi`](objectApi.md#ApiClient.ApiClient.ArtifactApi "ApiClient.ApiClient.ArtifactApi")

CreateLocalArtifactReference(*filePath*)[¶](#ApiClient.ArtifactApi.CreateLocalArtifactReference "Link to this definition")  
Creates a new LocalArtifactReference.

Parameters:  **filePath** (*str*) – Path of the file.

Returns:  LocalArtifactReference object.

Return type:  [`LocalArtifactReference`](#ApiClient.LocalArtifactReference "ApiClient.LocalArtifactReference")

CreateTestGuideArtifactReference(*depositoryName*, *artifactId*, *artifactName*)[¶](#ApiClient.ArtifactApi.CreateTestGuideArtifactReference "Link to this definition")  
Creates a new TestGuideArtifactReference.

Parameters:  - **depositoryName** (*str*) – Name of the depository as defined in the workspace settings.

- **artifactId** (*str*) – ID of the artifact in the depository.

- **artifactName** (*str*) – Name of the artifact.

Returns:  TestGuideArtifactReference object.

Return type:  [`TestGuideArtifactReference`](#ApiClient.TestGuideArtifactReference "ApiClient.TestGuideArtifactReference")

## LocalArtifactReference[¶](#localartifactreference "Link to this heading")

*class* LocalArtifactReference[¶](#ApiClient.LocalArtifactReference "Link to this definition")  
Base class

[`ArtifactReference`](ComponentApi.md#ApiClient.ArtifactReference "ApiClient.ArtifactReference")

Returned by

- [`ArtifactApi.CreateLocalArtifactReference`](#ApiClient.ArtifactApi.CreateLocalArtifactReference "ApiClient.ArtifactApi.CreateLocalArtifactReference")

Clone()[¶](#ApiClient.LocalArtifactReference.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`LocalArtifactReference`](#ApiClient.LocalArtifactReference "ApiClient.LocalArtifactReference")

GetPath()[¶](#ApiClient.LocalArtifactReference.GetPath "Link to this definition")  
Returns the file path to the artifact.

Returns:  Path.

Return type:  str

GetSourceType()[¶](#ApiClient.LocalArtifactReference.GetSourceType "Link to this definition")  
Returns artifact source type.

Returns:  name of source type

Return type:  str

## TestGuideArtifactReference[¶](#testguideartifactreference "Link to this heading")

*class* TestGuideArtifactReference[¶](#ApiClient.TestGuideArtifactReference "Link to this definition")  
Base class

[`ArtifactReference`](ComponentApi.md#ApiClient.ArtifactReference "ApiClient.ArtifactReference")

Returned by

- [`ArtifactApi.CreateTestGuideArtifactReference`](#ApiClient.ArtifactApi.CreateTestGuideArtifactReference "ApiClient.ArtifactApi.CreateTestGuideArtifactReference")

Clone()[¶](#ApiClient.TestGuideArtifactReference.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`TestGuideArtifactReference`](#ApiClient.TestGuideArtifactReference "ApiClient.TestGuideArtifactReference")

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
