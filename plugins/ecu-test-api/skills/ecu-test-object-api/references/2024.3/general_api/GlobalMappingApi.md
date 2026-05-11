# API for Global Mappings[¶](#api-for-global-mappings "Link to this heading")

Part of the [Object based program API](objectApi.md#objectapi)

## GlobalMappingApi[¶](#globalmappingapi "Link to this heading")

*class* GlobalMappingApi[¶](#ApiClient.GlobalMappingApi "Link to this definition")  
API to access global mapping files

Returned by

- [`ApiClient.GlobalMappingApi`](objectApi.md#ApiClient.ApiClient.GlobalMappingApi "ApiClient.ApiClient.GlobalMappingApi")

CreateMapping()[¶](#ApiClient.GlobalMappingApi.CreateMapping "Link to this definition")  
Creates an empty Mapping.

Returns:  An empty mapping

Return type:  [`GlobalMapping`](#ApiClient.GlobalMapping "ApiClient.GlobalMapping")

GetChanges(*oldGlobalMapping*, *newGlobalMapping*)[¶](#ApiClient.GlobalMappingApi.GetChanges "Link to this definition")  
Get the changes that exist between two given global mappings.

Parameters:  - **oldGlobalMapping** ([`GlobalMapping`](#ApiClient.GlobalMapping "ApiClient.GlobalMapping")) – The old global mapping to compare.

- **newGlobalMapping** ([`GlobalMapping`](#ApiClient.GlobalMapping "ApiClient.GlobalMapping")) – The new global mapping to compare.

Returns:  The changes that exist between the two global mappings.

Return type:  list[[`Change`](ConfigurationApi.md#ApiClient.Change "ApiClient.Change")]

OpenMapping(*filename*)[¶](#ApiClient.GlobalMappingApi.OpenMapping "Link to this definition")  
Opens an existing global mapping. Raises an ApiError if the referenced file does not exist.

Parameters:  **filename** (*str*) – Mapping file path. Can be absolute or relative to the parameters-directory.

Returns:  Opened mapping.

Return type:  [`GlobalMapping`](#ApiClient.GlobalMapping "ApiClient.GlobalMapping")

SearchGlobalMappings(*searchCriteria*, *useExtendedMode=False*)[¶](#ApiClient.GlobalMappingApi.SearchGlobalMappings "Link to this definition")  
Searches the current workspace and library workspaces for Global Mappings matching the given search criteria.

Parameters:  - **searchCriteria** (*str*) – The search criteria expressed in the ecu.test filter syntax. See section “Handling” =\> “Filter” of the ecu.test User Documentation.

- **useExtendedMode** (*boolean*) – If True, extended search strings are enabled. The default is False, meaning each word in the searchCriteria will be enclosed by wildcards and mapped to the filename. (e.g. “hello world” =\> “Name = ‘\*hello\*’ and Name = ‘\*world\*’”)

Returns:  All matching Global Mappings. If no file matches, an emtpy list is returned.

Return type:  list[[`GlobalMapping`](#ApiClient.GlobalMapping "ApiClient.GlobalMapping")]

Raises:  
**ApiError** – If the searchCriteria has an illegal syntax.

## GlobalMapping[¶](#globalmapping "Link to this heading")

*class* GlobalMapping[¶](#ApiClient.GlobalMapping "Link to this definition")  
Base class

[`Mapping`](MappingApi.md#ApiClient.Mapping "ApiClient.Mapping")

Returned by

- [`GlobalMappingApi.CreateMapping`](#ApiClient.GlobalMappingApi.CreateMapping "ApiClient.GlobalMappingApi.CreateMapping")

- [`GlobalMappingApi.OpenMapping`](#ApiClient.GlobalMappingApi.OpenMapping "ApiClient.GlobalMappingApi.OpenMapping")

- [`GlobalMappingApi.SearchGlobalMappings`](#ApiClient.GlobalMappingApi.SearchGlobalMappings "ApiClient.GlobalMappingApi.SearchGlobalMappings")

AddItem(*mappingItem*)[¶](#ApiClient.GlobalMapping.AddItem "Link to this definition")  
Adds a mapping item to the mapping.

Parameters:  **mappingItem** ([`MappingItem`](MappingApi.md#ApiClient.MappingItem "ApiClient.MappingItem")) – The mapping item to be added

Clone()[¶](#ApiClient.GlobalMapping.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`GlobalMapping`](#ApiClient.GlobalMapping "ApiClient.GlobalMapping")

GetFilename()[¶](#ApiClient.GlobalMapping.GetFilename "Link to this definition")  
Returns the path to the .xam file.

Returns:  Path to the .xam file or None if mapping is not saved yet.

Return type:  str

GetItemByName(*name*)[¶](#ApiClient.GlobalMapping.GetItemByName "Link to this definition")  
Searches the mapping for the mapping item by its name and returns it if existing.

Parameters:  **name** (*str*) – The name of the mapping item to be searched for

Returns:  mapping item with the given name or None if no such mapping item exists

Return type:  [`MappingItem`](MappingApi.md#ApiClient.MappingItem "ApiClient.MappingItem")

GetItems()[¶](#ApiClient.GlobalMapping.GetItems "Link to this definition")  
Returns a list of all the mapping items of the mapping.

Returns:  List of all the mapping items of the mapping.

Return type:  list[[`MappingItem`](MappingApi.md#ApiClient.MappingItem "ApiClient.MappingItem")]

GetItemsByTargetPath(*targetPath*)[¶](#ApiClient.GlobalMapping.GetItemsByTargetPath "Link to this definition")  
Searches the mapping for all mapping items that have the target path and returns them if existing.

Parameters:  **targetPath** (*str*) – The target path of the mapping items to be searched for

Returns:  List of mapping items that have the target path.

Return type:  list[[`MappingItem`](MappingApi.md#ApiClient.MappingItem "ApiClient.MappingItem")]

HasItem(*mappingItem*)[¶](#ApiClient.GlobalMapping.HasItem "Link to this definition")  
Checks whether the given mapping item belongs to the mapping.

Parameters:  **mappingItem** ([`MappingItem`](MappingApi.md#ApiClient.MappingItem "ApiClient.MappingItem")) – The mapping item to be checked

Returns:  True if the given mapping item belongs to the mapping.

Return type:  boolean

RemoveItemByName(*name*)[¶](#ApiClient.GlobalMapping.RemoveItemByName "Link to this definition")  
Removes a mapping item from the mapping.

Parameters:  **name** (*str*) – The name of the mapping item to be removed

ReplaceItem(*mappingItem*)[¶](#ApiClient.GlobalMapping.ReplaceItem "Link to this definition")  
Replaces a mapping item from the mapping

Parameters:  **mappingItem** ([`MappingItem`](MappingApi.md#ApiClient.MappingItem "ApiClient.MappingItem")) – The new mapping item to replace an existing one of the same name

Save(*filename=''*)[¶](#ApiClient.GlobalMapping.Save "Link to this definition")  
Saves the mapping space as an .xam file. Appends file ending if needed.

Parameters:  **filename** (*str*) – File name of the mapping file; Either absolute or relative to the ‘Parameters’ directory. If left out, use the existing file name and path (from a previous call of [`Save()`](#ApiClient.GlobalMapping.Save "ApiClient.GlobalMapping.Save") or `MappingApi.OpenMapping()`)
