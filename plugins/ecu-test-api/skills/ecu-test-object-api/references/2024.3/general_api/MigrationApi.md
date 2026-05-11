# API for Migrations[¶](#api-for-migrations "Link to this heading")

Part of the [Object based program API](objectApi.md#objectapi)

## MigrationApi[¶](#migrationapi "Link to this heading")

*class* MigrationApi[¶](#ApiClient.MigrationApi "Link to this definition")  
API access for migrations

Returned by

- [`ApiClient.MigrationApi`](objectApi.md#ApiClient.ApiClient.MigrationApi "ApiClient.ApiClient.MigrationApi")

MigrateOdxTestSteps(*folder=None*, *removeLegacyTestSteps=True*)[¶](#ApiClient.MigrationApi.MigrateOdxTestSteps "Link to this definition")  
Replaces deprecated odx test steps with its generic service test step

Parameters:  - **folder** (*str*) – folder that shall be migrated. If empty, the current workspace is used

- **removeLegacyTestSteps** (*bool*) – if True, converted legacy test steps are removed, otherwise they will only be deactivated

MigrateOpenDiagSession(*folder=None*)[¶](#ApiClient.MigrationApi.MigrateOpenDiagSession "Link to this definition")  
Renames deprecated jobs to `OpenDiagSession`

Parameters:  **folder** (*str*) – folder that shall be migrated. If empty, the current workspace is used
