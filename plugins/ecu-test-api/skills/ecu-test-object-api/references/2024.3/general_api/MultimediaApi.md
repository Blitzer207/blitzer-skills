# API for Multimedia Objects[¶](#api-for-multimedia-objects "Link to this heading")

Part of the [Object based program API](objectApi.md#objectapi)

## MultimediaApi[¶](#multimediaapi "Link to this heading")

*class* MultimediaApi[¶](#ApiClient.MultimediaApi "Link to this definition")  
Returned by

- [`ApiClient.MultimediaApi`](objectApi.md#ApiClient.ApiClient.MultimediaApi "ApiClient.ApiClient.MultimediaApi")

TouchInputApi[¶](#ApiClient.MultimediaApi.TouchInputApi "Link to this definition")  
Returns the TouchInputApi namespace.

Returns:  TouchInputApi namespace

Return type:  [`TouchInputApi`](TouchInputApi.md#ApiClient.TouchInputApi "ApiClient.TouchInputApi")

CreateMask(*x=0*, *y=0*, *width=0*, *height=0*)[¶](#ApiClient.MultimediaApi.CreateMask "Link to this definition")  
Create a new image mask.

Parameters:  - **x** (*int*) – Position of left edge

- **y** (*int*) – Position of upper edge

- **width** (*int*) – Mask width

- **height** (*int*) – Mask height

Returns:  A new mask

Return type:  [`Mask`](#ApiClient.Mask "ApiClient.Mask")

OpenMask(*filePath*)[¶](#ApiClient.MultimediaApi.OpenMask "Link to this definition")  
Opens an existing image mask.

Parameters:  **filePath** (*str*) – Path to the mask file.

Returns:  The loaded mask

Return type:  [`Mask`](#ApiClient.Mask "ApiClient.Mask")

## Mask[¶](#mask "Link to this heading")

*class* Mask[¶](#ApiClient.Mask "Link to this definition")  
Returned by

- [`MultimediaApi.CreateMask`](#ApiClient.MultimediaApi.CreateMask "ApiClient.MultimediaApi.CreateMask")

- [`MultimediaApi.OpenMask`](#ApiClient.MultimediaApi.OpenMask "ApiClient.MultimediaApi.OpenMask")

Clone()[¶](#ApiClient.Mask.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`Mask`](#ApiClient.Mask "ApiClient.Mask")

GetDistanceX()[¶](#ApiClient.Mask.GetDistanceX "Link to this definition")  
Returns the horizontal offset between each duplicated instance of this mask. See [`SetRepetitionX()`](#ApiClient.Mask.SetRepetitionX "ApiClient.Mask.SetRepetitionX") to configure horizontal repetition.

Returns:  Horizontal distance between repetitions

Return type:  int

GetDistanceY()[¶](#ApiClient.Mask.GetDistanceY "Link to this definition")  
Returns the vertical offset between each duplicated instance of this mask. See [`SetRepetitionY()`](#ApiClient.Mask.SetRepetitionY "ApiClient.Mask.SetRepetitionY") to configure vertical repetition.

Returns:  Vertical distance between repetitions

Return type:  int

GetHeight()[¶](#ApiClient.Mask.GetHeight "Link to this definition")  
Returns the mask height.

Returns:  Mask height

Return type:  int

GetName()[¶](#ApiClient.Mask.GetName "Link to this definition")  
Returns the name of this mask. Only applicable for submasks. The root mask of a mask file has no name. Instead, it will be referenced at runtime using its filename.

Returns:  The mask name if it is a submask, otherwise None

Return type:  str

GetRepetitionX()[¶](#ApiClient.Mask.GetRepetitionX "Link to this definition")  
Returns the horizontal repetition. The mask will be duplicated this amount of times in horizontal direction.

Returns:  Horizontal repetition

Return type:  int

GetRepetitionY()[¶](#ApiClient.Mask.GetRepetitionY "Link to this definition")  
Returns the vertical repetition. The mask will be duplicated this amount of times in vertical direction.

Returns:  Vertical repetition

Return type:  int

GetWidth()[¶](#ApiClient.Mask.GetWidth "Link to this definition")  
Returns the mask width.

Returns:  Mask width

Return type:  int

GetX()[¶](#ApiClient.Mask.GetX "Link to this definition")  
Returns the x position.

Returns:  x position

Return type:  int

GetY()[¶](#ApiClient.Mask.GetY "Link to this definition")  
Returns the y position.

Returns:  y position

Return type:  int

Save(*filePath*)[¶](#ApiClient.Mask.Save "Link to this definition")  
Saves the mask to a file.

Parameters:  **filePath** (*str*) – Filename or path to the mask file. A relative path will be resolved to the ‘Images’ directory of the current workspace.

SetDistanceX(*distanceX*)[¶](#ApiClient.Mask.SetDistanceX "Link to this definition")  
Sets the horizontal offset between each duplicated instance of this mask. See [`SetRepetitionX()`](#ApiClient.Mask.SetRepetitionX "ApiClient.Mask.SetRepetitionX") to configure horizontal repetition.

Parameters:  **distanceX** (*int*) – New horizontal distance between repetitions

SetDistanceY(*distanceY*)[¶](#ApiClient.Mask.SetDistanceY "Link to this definition")  
Sets the vertical offset between each duplicated instance of this mask. See [`SetRepetitionY()`](#ApiClient.Mask.SetRepetitionY "ApiClient.Mask.SetRepetitionY") to configure vertical repetition.

Parameters:  **distanceY** (*int*) – New vertical distance between repetitions

SetHeight(*height*)[¶](#ApiClient.Mask.SetHeight "Link to this definition")  
Sets the mask height.

Parameters:  **height** (*int*) – New height

SetRepetitionX(*repetitionX*)[¶](#ApiClient.Mask.SetRepetitionX "Link to this definition")  
Sets how many times the mask will be duplicated in horizontal direction.

Parameters:  **repetitionX** (*int*) – New horizontal repetition

SetRepetitionY(*repetitionY*)[¶](#ApiClient.Mask.SetRepetitionY "Link to this definition")  
Sets how many times the mask will be duplicated in vertical direction.

Parameters:  **repetitionY** (*int*) – New vertical repetition

SetWidth(*width*)[¶](#ApiClient.Mask.SetWidth "Link to this definition")  
Sets the mask width.

Parameters:  **width** (*int*) – New width

SetX(*x*)[¶](#ApiClient.Mask.SetX "Link to this definition")  
Sets the x position. If repetition is active, this defines the left edge of the first instance of this mask.

Parameters:  **x** (*int*) – New x position

SetY(*y*)[¶](#ApiClient.Mask.SetY "Link to this definition")  
Sets the y position. If repetition is active, this defines the upper edge of the first instance of this mask.

Parameters:  **y** (*int*) – New y position
