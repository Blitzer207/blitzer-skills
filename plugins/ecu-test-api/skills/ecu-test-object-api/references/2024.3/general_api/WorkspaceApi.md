# API for Workspaces[¶](#api-for-workspaces "Link to this heading")

Part of the [Object based program API](objectApi.md#objectapi)

## WorkspaceApi[¶](#workspaceapi "Link to this heading")

*class* WorkspaceApi[¶](#ApiClient.WorkspaceApi "Link to this definition")  
API to access the workspace

Returned by

- [`ApiClient.WorkspaceApi`](objectApi.md#ApiClient.ApiClient.WorkspaceApi "ApiClient.ApiClient.WorkspaceApi")

GetReferencesIn(*filePath*)[¶](#ApiClient.WorkspaceApi.GetReferencesIn "Link to this definition")  
Checks the passed file whether it contains references and returns the contained references as a list of absolute file paths.

Parameters:  **filePath** (*str*) – References in this package/project are searched for.

Returns:  The absolute paths of all references to packages/projects within filePath. If no references are found, an empty list is returned.

Return type:  list[str]

GetReferencesTo(*filePath*)[¶](#ApiClient.WorkspaceApi.GetReferencesTo "Link to this definition")  
Traverses the workspace and searches in all packages and projects for references to the passed package/project and returns the references as a list of absolute file paths.

Parameters:  **filePath** (*str*) – References to this package/project path are searched for.

Returns:  The absolute paths of all packages/projects referencing to filePath. If no references are found, an empty list is returned.

Return type:  list[str]

SearchFiles(*searchCriteria*, *useExtendedMode=False*)[¶](#ApiClient.WorkspaceApi.SearchFiles "Link to this definition")  
Searches the current workspace and library workspaces for files matching the given search criteria.

Parameters:  - **searchCriteria** (*str*) – The search criteria expressed in the ecu.test filter syntax. See section “Handling” =\> “Filter” of the ecu.test User Documentation.

- **useExtendedMode** (*boolean*) – If True, extended search strings are enabled. The default is False, meaning each word in the searchCriteria will be enclosed by wildcards and mapped to the filename. (e.g. “hello world” =\> “Name = ‘\*hello\*’ and Name = ‘\*world\*’”)

Returns:  The absolute paths of all matching files in the workspace. If no file matches, an empty list is returned.

Return type:  list[str]

Raises:  
**ApiError** – If the searchCriteria has an illegal syntax.
