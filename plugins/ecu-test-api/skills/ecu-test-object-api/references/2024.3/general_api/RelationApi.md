# API for Relations[¶](#api-for-relations "Link to this heading")

Part of the [Object based program API](objectApi.md#objectapi)

## RelationApi[¶](#relationapi "Link to this heading")

*class* RelationApi[¶](#ApiClient.RelationApi "Link to this definition")  
API to access relations

Returned by

- [`ApiClient.RelationApi`](objectApi.md#ApiClient.ApiClient.RelationApi "ApiClient.ApiClient.RelationApi")

IMPLEMENTS[¶](#ApiClient.RelationApi.IMPLEMENTS "Link to this definition")  
Returns the constant used to specify the relation type ‘implements’:

Returns:  ‘implements’ constant

Return type:  int

IS_DERIVED_FROM[¶](#ApiClient.RelationApi.IS_DERIVED_FROM "Link to this definition")  
Returns the constant used to specify the relation type ‘is derived from’:

Returns:  ‘is derived from’ constant

Return type:  int

RELATES_TO[¶](#ApiClient.RelationApi.RELATES_TO "Link to this definition")  
Returns the constant used to specify the relation type ‘relates to’:

Returns:  ‘relates to’ constant

Return type:  int

CreateRelation(*relationType*, *packagePath*)[¶](#ApiClient.RelationApi.CreateRelation "Link to this definition")  
Creates a new relation with the current target version.

Parameters:  - **relationType** (*int*) –

  relation type e.g. ‘relatest to’ or ‘is derived from’

  - `RelationApi.RELATEST_TO`

- **packagePath** (*str*) – Path to Package

Returns:  new Relation

Return type:  [`Relation`](#ApiClient.Relation "ApiClient.Relation")

## Relation[¶](#relation "Link to this heading")

*class* Relation[¶](#ApiClient.Relation "Link to this definition")  
Returned by

- [`AnalysisPackage.GetRelations`](PackageApi.md#ApiClient.AnalysisPackage.GetRelations "ApiClient.AnalysisPackage.GetRelations")

- [`Package.GetRelations`](PackageApi.md#ApiClient.Package.GetRelations "ApiClient.Package.GetRelations")

- [`RelationApi.CreateRelation`](#ApiClient.RelationApi.CreateRelation "ApiClient.RelationApi.CreateRelation")

Clone()[¶](#ApiClient.Relation.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`Relation`](#ApiClient.Relation "ApiClient.Relation")

GetSpecifiedTargetVersion()[¶](#ApiClient.Relation.GetSpecifiedTargetVersion "Link to this definition")  
Returns the version of relation target. This version is specified at the relation creation time and could be updated later.

Returns:  specified relation target version

Return type:  string

GetTargetPath()[¶](#ApiClient.Relation.GetTargetPath "Link to this definition")  
Returns the path to the relation target.

Returns:  Path relative to the package directory

Return type:  string

GetType()[¶](#ApiClient.Relation.GetType "Link to this definition")  
Returns relation type.

Returns:  relation type e.g. ‘relatest to’ or ‘is derived from’

- `RelationApi.RELATEST_TO`

Return type:  int

IsSpecifiedVersionOutdated()[¶](#ApiClient.Relation.IsSpecifiedVersionOutdated "Link to this definition")  
Returns true if the current version of relation target is not equal to already specified relation target version.

Returns:  True if the specified relation target version is outdated.

Return type:  boolean

SetSpecifiedTargetVersion(*version*)[¶](#ApiClient.Relation.SetSpecifiedTargetVersion "Link to this definition")  
Sets the version of relation target. The specified version is stored as a property of this relation.

Parameters:  **version** (*string*) – The version of relation target to be set.

UpdateSpecifiedTargetVersion()[¶](#ApiClient.Relation.UpdateSpecifiedTargetVersion "Link to this definition")  
Updates the version of relation target to the current target value. This updated version is stored as a property of this relation.
