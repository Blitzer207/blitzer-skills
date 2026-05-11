# Advanced properties of media related objects[¶](#advanced-properties-of-media-related-objects "Link to this heading")

The following types are globally available. E.g. in function variables, UserPyModules or other user code:

> - [`Image`](#tts.testModule.multimedia.dataElements.Image.Image "tts.testModule.multimedia.dataElements.Image.Image")
>
> - [`Mask`](#tts.testModule.multimedia.dataElements.Mask.Mask "tts.testModule.multimedia.dataElements.Mask.Mask")
>
> - [`AudioBlock`](#tts.testModule.multimedia.dataElements.AudioBlock.AudioBlock "tts.testModule.multimedia.dataElements.AudioBlock.AudioBlock")

## Image[¶](#image "Link to this heading")

*class* Image[¶](#tts.testModule.multimedia.dataElements.Image.Image "Link to this definition")  
Represents an image.

Parameters:  **arg** (*str* *|* *numpy.ndarray*) – The data from which to load an image (a file path or a numpy array)

Creates a new Image object either from a file or from a given numpy array. The following filetypes are supported when passing a file path:

> - Windows bitmaps (\*.bmp, \*.dib)
>
> - JPEG files (\*.jpeg, \*.jpg, \*.jpe)
>
> - JPEG 2000 files (\*.jp2)
>
> - Portable Network Graphics (\*.png)
>
> - WebP (\*.webp)
>
> - Portable image format (\*.pbm, \*.pgm, \*.ppm, \*.pxm, \*.pnm)
>
> - PFM files (\*.pfm)
>
> - Sun rasters (\*.sr, \*.ras)
>
> - TIFF files (\*.tiff, \*.tif)
>
> - OpenEXR Image files (\*.exr)
>
> - Radiance HDR (\*.hdr, \*.pic)

The file path can be a path relative to the workspace directory. When passing a numpy array, the array must be three-dimensional, i.e. its shape must be of the form `(<height>, <width>, <channels>)`. It must have either one, three, or four channels. Alternatively, if the array holds only a single channel the last dimension may be omitted, passing in only a two-dimensional array, i.e. its shape may be of the form `(<height>, <width>)`. Depending on the number of channels provided, the image will be constructed in a different manner:

> - One channel: each value will be copied to all three color channels, resulting in a grayscale image (with three color channels).
>
> - Three channels: The channels are interpreted as color channels (blue, green, red).
>
> - Four channels: The first three channels will be interpreted as color channels, the values of the fourth will be stored as an alpha channel for transparency.

Example usage:

> - `Image("path/to/image.png")  # Loads the file "image.png"`>
> - `Image(numpy.zeros((768, 1024)))  # an empty Image that is 1024px wide and 768px high`GetData()[¶](#tts.testModule.multimedia.dataElements.Image.Image.GetData "Link to this definition")  
Returns the image data as OpenCV-compatible NumPy array. Please note that ecu.test uses GetDataWithAlpha() when calling \<UserFilter\>.ProcessImage, so it is strongly recommended to use that method instead of this one when calling the UserFilter directly.

Returns:  The image data as NumPy array in BGR-format.

Return type:  numpy.ndarray

GetDataWithAlpha()[¶](#tts.testModule.multimedia.dataElements.Image.Image.GetDataWithAlpha "Link to this definition")  
Returns the image data as OpenCV-compatible NumPy array. This method will merge GetData() and GetAlpha() into one array and return the result. Please note that this function will create an alpha layer if GetAlpha() returns None.

Returns:  The image data (BGR) and alpha channel, merged into one array.

Return type:  numpy.ndarray

GetAlpha()[¶](#tts.testModule.multimedia.dataElements.Image.Image.GetAlpha "Link to this definition")  
Returns the alpha channel if the image has transparency, otherwise None.

Returns:  The alpha channel as NumPy array

Return type:  numpy.ndarray|None

GetDimensions()[¶](#tts.testModule.multimedia.dataElements.Image.Image.GetDimensions "Link to this definition")  
Returns the image dimensions (w, h).

Returns:  Dimensions (w, h)

Returns:  tuple[int, int]

Save(*path*)[¶](#tts.testModule.multimedia.dataElements.Image.Image.Save "Link to this definition")  
Saves the image as file.

Parameters:  **path** (*str*) – Path where the image file should be saved. The path must include the file extension. A relative path is resolved relative to the workspace path.

Crop(*x*, *y*, *width*, *height*)[¶](#tts.testModule.multimedia.dataElements.Image.Image.Crop "Link to this definition")  
Crops the image.

Parameters:  - **x** (*int*) – x position of the upper left corner of the cutout

- **y** (*int*) – y position of the upper left corner of the cutout

- **width** (*int*) – Width of the cutout

- **height** (*int*) – Height of the cutout

Returns:  Cropped image

Return type:  [`Image`](#tts.testModule.multimedia.dataElements.Image.Image "tts.testModule.multimedia.dataElements.Image.Image")

GetSimilarity(*otherPic*, *colorTolerance=0*)[¶](#tts.testModule.multimedia.dataElements.Image.Image.GetSimilarity "Link to this definition")  
Calculates the similarity between two images as a value between 0.0 and 1.0. The similarity can be calculated as follows:

- Calculation of the absolute difference for each color for each pixel of the two images

- If the difference of the color is less than or equal to parameter colorTolerance, the color is considered as equal

- If otherPic is a transparent image, then all pixels that are not completely visible are considered equal

- The return value is the quotient of all equal pixel colors divided by the number of all pixel colors

If otherPic is an iterable object of Images, the highest value over all calculated similarities is returned.

Parameters:  - **otherPic** ([`Image`](#tts.testModule.multimedia.dataElements.Image.Image "tts.testModule.multimedia.dataElements.Image.Image") | iterable[[`Image`](#tts.testModule.multimedia.dataElements.Image.Image "tts.testModule.multimedia.dataElements.Image.Image")]) – Image or an iterable of Images to compare. The image(s) need to have the same size as the image they are compared with.

- **colorTolerance** (*int*) – The maximum allowed color difference (0…255) of a pixel to be considered as equal

Returns:  Similarity in range 0.0 to 1.0

Return type:  float

IsEqual(*otherPic*, *colorTolerance=0*, *tolerance=0*)[¶](#tts.testModule.multimedia.dataElements.Image.Image.IsEqual "Link to this definition")  
Determines via [`GetSimilarity()`](#tts.testModule.multimedia.dataElements.Image.Image.GetSimilarity "tts.testModule.multimedia.dataElements.Image.Image.GetSimilarity") the similarity to otherPic. If the similarity is within the specified tolerance then True is returned. Otherwise, False.

Parameters:  - **otherPic** ([`Image`](#tts.testModule.multimedia.dataElements.Image.Image "tts.testModule.multimedia.dataElements.Image.Image")) – The image to compare. The image needs to have the same size as the image it is compared with.

- **colorTolerance** (*int*) – The maximum allowed color difference (0…255) of a pixel to be considered as equal.

- **tolerance** (*float*) – Tolerance in percent (from 0.0 to 1.0) that indicates how much the images are allowed to differ. A higher value will make the comparison more tolerant. Defaults to 0.

Returns:  True if the images are equal, else False

Return type:  bool

Contains(*otherPic*, *colorTolerance=0*, *tolerance=0*)[¶](#tts.testModule.multimedia.dataElements.Image.Image.Contains "Link to this definition")  
Checks if otherPic is contained in this image.

At first, the closest matching section to otherPic is determined. Then, the similarity between the cropped image and otherPic is calculated. If the similarity is within the specified tolerance then True is returned. Otherwise, False.

If otherPic is an iterable object of Images, this method returns True if at least one Image of otherPic is considered as contained.

Parameters:  - **otherPic** ([`Image`](#tts.testModule.multimedia.dataElements.Image.Image "tts.testModule.multimedia.dataElements.Image.Image") | Iterable[[`Image`](#tts.testModule.multimedia.dataElements.Image.Image "tts.testModule.multimedia.dataElements.Image.Image")]) – The searched image or an iterator over multiple searched images

- **colorTolerance** (*int*) – The maximum allowed color difference (0…255) of a pixel to be considered as equal.

- **tolerance** (*float*) – Tolerance in percent (from 0.0 to 1.0) that indicates how much the image is allowed to differ from a potential match. A higher value will make the search more tolerant. Defaults to 0.

Returns:  True if otherPic is contained in this image, else False

Return type:  bool

FindImage(*image*, *maxOccurrences=100*, *threshold=0.9999*)[¶](#tts.testModule.multimedia.dataElements.Image.Image.FindImage "Link to this definition")  
Searches for a sub-image in this image. Returns a list of matches, containing information about the position of the sub-image.

Parameters:  - **image** ([`Image`](#tts.testModule.multimedia.dataElements.Image.Image "tts.testModule.multimedia.dataElements.Image.Image")) – The image that will be searched for in the larger image. Its dimensions must not be greater than the source image.

- **maxOccurrences** (*int*) – The maximum number of occurrences to find. Set to 0 to find all occurrences. Limiting this number can improve performance when using low thresholds. Defaults to 100.

- **threshold** (*float*) – The similarity threshold in percent from 0 to 1 (Defaults to 0.9999 to avoid rounding errors). Determines how similar an image must be to be considered a match. A threshold of 1 will search only for perfect matches. Values of 0.9 and above will usually find closely matching regions in the image while ignoring noise. Note that a too low threshold might lead to wrong matches.

Returns:  List of image matches sorted by their position.

Return type:  [ImageMatchList](#tts.testModule.multimedia.dataElements.MatchObjects.ImageMatchList "tts.testModule.multimedia.dataElements.MatchObjects.ImageMatchList")

FindImages(*images*, *maxOccurrences=100*, *threshold=0.9999*)[¶](#tts.testModule.multimedia.dataElements.Image.Image.FindImages "Link to this definition")  
Searches for a list of sub-images in this image. Returns a list of matches, containing information about the position of the sub-image.

Parameters:  - **images** (list[[`Image`](#tts.testModule.multimedia.dataElements.Image.Image "tts.testModule.multimedia.dataElements.Image.Image")]) – The images to be searched for in the larger image. Their dimensions must not be greater than the source image.

- **maxOccurrences** (*int*) – The maximum number of occurrences to find. Set to 0 to find all occurrences. Limiting this number can improve performance when using low thresholds. Defaults to 100.

- **threshold** (*float*) – The similarity threshold in percent from 0 to 1 (Defaults to 0.9999 to avoid rounding errors). Determines how similar an image must be to be considered a match. A threshold of 1 will search only for perfect matches. Values of 0.9 and above will usually find closely matching regions in the image while ignoring noise. Note that a too low threshold might lead to wrong matches.

Returns:  List of image matches sorted by their position.

Return type:  [ImageMatchList](#tts.testModule.multimedia.dataElements.MatchObjects.ImageMatchList "tts.testModule.multimedia.dataElements.MatchObjects.ImageMatchList")

FindImageByFeatures(*image*, *threshold=0.2*)[¶](#tts.testModule.multimedia.dataElements.Image.Image.FindImageByFeatures "Link to this definition")  
Searches for a sub-image within this image. This method does not compare every pixel. Instead, it looks for distinct features in both images and tries to match them. This makes it invariant to scale, rotation, color, and perspective. The features are detected by analyzing black/white color gradients. Therefore, complex patterns with hard edges between light and dark areas will be found best. This also means that an image with inverted colors will not be found. Dark areas must still be dark, and light areas light between source image and sub-image. Note that execution time will increase linearly with the number of sub-image occurences in the scene. E.g. if your scene contains the searched image twice then it will take twice as long to find all occurences compared to a scene where the sub-image occurs only once.

Parameters:  - **image** ([`Image`](#tts.testModule.multimedia.dataElements.Image.Image "tts.testModule.multimedia.dataElements.Image.Image")) – The sub-image that will be searched for within the larger image.

- **threshold** (*float*) – The minimum confidence that a match must have to be considered a match. Values are in percent from 0 to 1 (defaults to 0.2). Higher values will filter out bad results but will also make the search less invariant to changes regarding scale, rotation, color, and perspective.

Returns:  A list of ImageMatches.

Return type:  [ImageMatchList](#tts.testModule.multimedia.dataElements.MatchObjects.ImageMatchList "tts.testModule.multimedia.dataElements.MatchObjects.ImageMatchList")

FindObjectByColor(*color*, *tolH*, *tolS*, *tolV*, *kernelSize=5*)[¶](#tts.testModule.multimedia.dataElements.Image.Image.FindObjectByColor "Link to this definition")  
Searches for objects with a given color (Color Detection). After applying a color filter, a dilation step connects identified pixel areas that lie within a distance of kernelSize. Each resulting pixel area will be represented by an [`ImageMatch`](#tts.testModule.multimedia.dataElements.MatchObjects.ImageMatch "tts.testModule.multimedia.dataElements.MatchObjects.ImageMatch") (rectangular area) of the returned `MatchList`.

The color filter is applied in HSV color schema. Therefore, the tolerances of the color filter must be provided in HSV schema.

Provided HSV parameters (tolH, tolS, tolV, color) must match the following conditions:

> - *Hue* is an integer between 0 and 180 and represents the position (in 2 degree steps) on the color circle. 180 corresponds to 360 degrees or a full circle and therefore is semantically equal to 0. (Please note: Some graphic programs provide different value ranges from 0 to 255 or from 0 to 360.)
>
> - *Saturation* is an integer between 0 and 255.
>
> - *Value* is an integer between 0 and 255

Parameters:  - **color** (*str*) – A color string. Either an RGB hex string (e.g. ‘#FF0000’ for red) or an HSV color string in the form ‘hsv(hue, saturation, value)’ (e.g. ‘hsv(120, 255, 255)’ for blue).

- **tolH** (*tuple[int,* *int]* *|* *int*) – The tolerance applied to the expected hue. The value can either be a tuple of integers for defining an asymmetric tolerance window (Hue(color) - tolH[0], Hue(color) + tolH[1]), or an integer for defining a symmetric tolerance window (Hue(color) - tolH, Hue(color) + tolH).

- **tolS** (*tuple[int,* *int]* *|* *int*) – The tolerance applied to the expected saturation. The value can either be a tuple of integers for defining an asymmetric tolerance window (Saturation(color) - tolS[0], Saturation(color) + tolS[1]), or an integer for defining a symmetric tolerance window (Saturation(color) - tolS, Saturation(color) + tolS).

- **tolV** (*tuple[int,* *int]* *|* *int*) – The tolerance applied to the expected value. It can either be a tuple of integers for defining an asymmetric tolerance window (Value(color) - tolV[0], Value(color) + tolV[1]), or an integer for defining a symmetric tolerance window (Value(color) - tolV, Value(color) + tolV).

- **kernelSize** (*int*) – The size of the kernel that is used to connect separated pixel areas to one object (dilation). A larger kernel connects pixel areas that have more distance to each other. Odd numbers must be provided! Defaults to 5.

Returns:  A list of ImageMatches.

Return type:  [ImageMatchList](#tts.testModule.multimedia.dataElements.MatchObjects.ImageMatchList "tts.testModule.multimedia.dataElements.MatchObjects.ImageMatchList")

FindWord(*wordList=None*, *maxOccurrences=0*, *langList=None*, *ocrDataPath=None*, *isRegex=False*, *threshold=0.4*)[¶](#tts.testModule.multimedia.dataElements.Image.Image.FindWord "Link to this definition")  
Find single words in an image. Returns a list of matches containing information about the position of the desired word. This method applies various preprocessing steps, such as automatically inverting the colors to ensure the background is always white.

Parameters:  - **wordList** (*str* *|* *list[str]*) – (List of) desired word(s).

- **maxOccurrences** (*int*) – Maximum number of matches to be found. Use this, if you expect a string to occur exactly n times. The analysis will be stopped as soon as this number is reached. Can improve performance. If the value is 0, the full image will be analyzed.

- **langList** (*list[str]*) – List of language modules to use for text recognition. ecu.test comes with a preset list of available languages. For example use [‘eng’, ‘deu’] to recognize english and german text (in that order). The full list of default languages can be seen in the test configuration window. Additional language modules are available online, please refer to the tesseract documentation to download new language packs. If no language is specified then the languages from the currently active test configuration will be used. Note that if your test configuration contains more than one media node, the first node (in alphabetical order) will be used to load the ocr data.

- **ocrDataPath** (*str* *|* *None*) – The path to the directory containing your custom tesseract language files. If specified, all \*.traineddata files present in that directory will be added to the default languages as valid inputs for the langList parameter. Leave blank to use ecu.test’s default directory with its preset range of languages.

- **isRegex** (*bool*) – Set True to use regular expression as search strings.

- **threshold** (*float*) – Only results with a confidence larger than this threshold will be returned (between 0.0 and 1.0).

Returns:  List of matches that contain information about the text position sorted by their position.

Return type:  [TextMatchList](#tts.testModule.multimedia.dataElements.MatchObjects.TextMatchList "tts.testModule.multimedia.dataElements.MatchObjects.TextMatchList")

FindText(*searchStrings=None*, *maxOccurrences=0*, *langList=None*, *ocrDataPath=None*, *isRegex=False*, *strict=False*, *threshold=0.4*)[¶](#tts.testModule.multimedia.dataElements.Image.Image.FindText "Link to this definition")  
Find a text in an image. Returns a list of matches containing information about the position of the desired text. This method applies various preprocessing steps, such as automatically inverting the colors to ensure the background is always white. See [`RecognizeText()`](#tts.testModule.multimedia.dataElements.Image.Image.RecognizeText "tts.testModule.multimedia.dataElements.Image.Image.RecognizeText") for a more basic approach without any preprocessing.

Parameters:  - **searchStrings** (*list[str]*) – List of desired text values.

- **maxOccurrences** (*int*) – Maximum number of matches to be found. Use this, if you expect a string to occur exactly n times. The analysis will be stopped as soon as this number is reached. Can improve performance. If the value is 0, the full image will be analyzed.

- **langList** (*list[str]*) – List of language modules to use for text recognition. ecu.test comes with a preset list of available languages. For example use [‘eng’, ‘deu’] to recognize english and german text (in that order). The full list of default languages can be seen in the test configuration window. Additional language modules are available online, please refer to the tesseract documentation to download new language packs. If no language is specified then the languages from the currently active test configuration will be used. Note that if your test configuration contains more than one media node, the first node (in alphabetical order) will be used to load the ocr data.

- **ocrDataPath** (*str* *|* *None*) – The path to the directory containing your custom tesseract language files. If specified, all \*.traineddata files present in that directory will be added to the default languages as valid inputs for the langList parameter. Leave blank to use ecu.test’s default directory with its preset range of languages.

- **isRegex** (*bool*) – Set True to use regular expression as search strings.

- **strict** (*bool*) – If False, this method will return all text matches that contain the search string. If True, it will only return results that exactly match the search string.

- **threshold** (*float*) – Only results with a confidence larger than this threshold will be returned (between 0.0 and 1.0).

Returns:  List of matches that contain information about the text position sorted by their position.

Return type:  [TextMatchList](#tts.testModule.multimedia.dataElements.MatchObjects.TextMatchList "tts.testModule.multimedia.dataElements.MatchObjects.TextMatchList")

FindBestTextMatches(*searchStrings=None*, *maxOccurrences=100*, *langList=None*, *ocrDataPath=None*, *isRegex=False*)[¶](#tts.testModule.multimedia.dataElements.Image.Image.FindBestTextMatches "Link to this definition")  
Finds texts in an image. Returns a list of matches sorted by the confidence.

Parameters:  - **searchStrings** (*list[str]*) – List with texts to find

- **maxOccurrences** (*int*) – Limits the number of matches to n items.

- **langList** (*list[str]*) – List of language modules to use for text recognition. ecu.test comes with a preset list of available languages. For example use [‘eng’, ‘deu’] to recognize english and german text (in that order). The full list of default languages can be seen in the test configuration window. Additional language modules are available online, please refer to the tesseract documentation to download new language packs. If no language is specified then the languages from the currently active test configuration will be used. Note that if your test configuration contains more than one media node, the first node (in alphabetical order) will be used to load the ocr data.

- **ocrDataPath** (*str* *|* *None*) – The path to the directory containing your custom tesseract language files. If specified, all \*.traineddata files present in that directory will be added to the default languages as valid inputs for the langList parameter. Leave blank to use ecu.test’s default directory with its preset range of languages.

- **isRegex** (*bool*) – Set True to use regular expression as search strings.

Returns:  List of matches that contain information about the text position sorted by their confidence.

Return type:  [TextMatchList](#tts.testModule.multimedia.dataElements.MatchObjects.TextMatchList "tts.testModule.multimedia.dataElements.MatchObjects.TextMatchList")

RecognizeText(*langList=None*, *ocrDataPath=None*)[¶](#tts.testModule.multimedia.dataElements.Image.Image.RecognizeText "Link to this definition")  
Tries to recognize text inside the image. This method does not apply any preprocessing to the image. To achieve best results you should ensure that the image uses black text on white background. You can use one of the builtin ImageFilters to manipulate your image (see [`ImageFiltersApi`](api.md#tts.testModule.multimedia.api.MultimediaApi.ImageFiltersApi "tts.testModule.multimedia.api.MultimediaApi.ImageFiltersApi")). Alternatively see [`FindText()`](#tts.testModule.multimedia.dataElements.Image.Image.FindText "tts.testModule.multimedia.dataElements.Image.Image.FindText") for a more sophisticated approach that applies automatic preprocessing.

Parameters:  - **langList** (*list\<str\>*) – List of language modules to use for text recognition. ecu.test comes with a preset list of available languages. For example use [‘eng’, ‘deu’] to recognize english and german text (in that order). The full list of default languages can be seen in the test configuration window. Additional language modules are available online, please refer to the tesseract documentation to download new language packs. If no language is specified then the languages from the currently active test configuration will be used. Note that if your test configuration contains more than one media node, the first node (in alphabetical order) will be used to load the ocr data.

- **ocrDataPath** (*str*) – The path to the directory containing your custom tesseract language files. If specified, all \*.traineddata files present in that directory will be added to the default languages as valid inputs for the langList parameter. Leave blank to use ecu.test’s default directory with its preset range of languages.

Returns:  The recognized text

Return type:  str

## Mask[¶](#mask "Link to this heading")

*class* Mask[¶](#tts.testModule.multimedia.dataElements.Mask.Mask "Link to this definition")  
Parameters:  **path** – The mask file to load

Creates a new Mask object from a given file.

Example usage: `Mask("path/to/file.mask")`

Apply(*image*)[¶](#tts.testModule.multimedia.dataElements.Mask.Mask.Apply "Link to this definition")  
Crops an image using the region defined by this mask.

Parameters:  **image** ([`Image`](#tts.testModule.multimedia.dataElements.Image.Image "tts.testModule.multimedia.dataElements.Image.Image")) – The image to be masked

Returns:  A new cropped image

Return type:  [`Image`](#tts.testModule.multimedia.dataElements.Image.Image "tts.testModule.multimedia.dataElements.Image.Image")

## Frame[¶](#frame "Link to this heading")

*class* Frame[¶](#tts.traceRecording.parser.formats.video.VideoRecording.Frame "Link to this definition")  
A Frame is an Image read from a video file. Therefore, it has information about the video capture, a frame number and a timestamp in the file. Working with manipulating methods will result in an object of type Image instead of Frame.

GetCaptureInfo()[¶](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.GetCaptureInfo "Link to this definition")  
Returns a dictionary with information about the capture. Keys: fps, width, height, frame_count, filename.

Return type:  dict[str, float]

GetNumber()[¶](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.GetNumber "Link to this definition")  
Returns the zero-based number of the frame.

Return type:  int

GetTime()[¶](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.GetTime "Link to this definition")  
Returns the frame time in seconds (rounded according to the current time stamp rounding settings).

Return type:  float

GetData()[¶](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.GetData "Link to this definition")  
Reads and returns the image data.

Returns:  The image data as numpy array

Return type:  numpy.ndarray

GetAlpha()[¶](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.GetAlpha "Link to this definition")  
Alpha channel for video frames are not supported.

Returns:  Returns always None

Return type:  NoneType

GetDataWithAlpha()[¶](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.GetDataWithAlpha "Link to this definition")  
Returns the image data as OpenCV-compatible NumPy array. This method will merge GetData() and GetAlpha() into one array and return the result. Please note that this function will create an alpha layer if GetAlpha() returns None.

Returns:  The image data (BGR) and alpha channel, merged into one array.

Return type:  numpy.ndarray

GetDimensions()[¶](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.GetDimensions "Link to this definition")  
Returns the image dimensions (w, h).

Returns:  Dimensions (w, h)

Returns:  tuple[int, int]

Save(*path*)[¶](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.Save "Link to this definition")  
Saves the image as file.

Parameters:  **path** (*str*) – Path where the image file should be saved. The path must include the file extension. A relative path is resolved relative to the workspace path.

Crop(*x*, *y*, *width*, *height*)[¶](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.Crop "Link to this definition")  
Crops the image.

Parameters:  - **x** (*int*) – x position of the upper left corner of the cutout

- **y** (*int*) – y position of the upper left corner of the cutout

- **width** (*int*) – Width of the cutout

- **height** (*int*) – Height of the cutout

Returns:  Cropped image

Return type:  [`Image`](apireport.md#tts.core.report.db.Image.Image "tts.core.report.db.Image.Image")

Contains(*otherPic*, *colorTolerance=0*, *tolerance=0*)[¶](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.Contains "Link to this definition")  
Checks if otherPic is contained in this image.

At first, the closest matching section to otherPic is determined. Then, the similarity between the cropped image and otherPic is calculated. If the similarity is within the specified tolerance then True is returned. Otherwise, False.

If otherPic is an iterable object of Images, this method returns True if at least one Image of otherPic is considered as contained.

Parameters:  - **otherPic** ([`Image`](apireport.md#tts.core.report.db.Image.Image "tts.core.report.db.Image.Image") | Iterable[[`Image`](apireport.md#tts.core.report.db.Image.Image "tts.core.report.db.Image.Image")]) – The searched image or an iterator over multiple searched images

- **colorTolerance** (*int*) – The maximum allowed color difference (0…255) of a pixel to be considered as equal.

- **tolerance** (*float*) – Tolerance in percent (from 0.0 to 1.0) that indicates how much the image is allowed to differ from a potential match. A higher value will make the search more tolerant. Defaults to 0.

Returns:  True if otherPic is contained in this image, else False

Return type:  bool

IsEqual(*otherPic*, *colorTolerance=0*, *tolerance=0*)[¶](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.IsEqual "Link to this definition")  
Determines via [`GetSimilarity()`](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.GetSimilarity "tts.traceRecording.parser.formats.video.VideoRecording.Frame.GetSimilarity") the similarity to otherPic. If the similarity is within the specified tolerance then True is returned. Otherwise, False.

Parameters:  - **otherPic** ([`Image`](apireport.md#tts.core.report.db.Image.Image "tts.core.report.db.Image.Image")) – The image to compare. The image needs to have the same size as the image it is compared with.

- **colorTolerance** (*int*) – The maximum allowed color difference (0…255) of a pixel to be considered as equal.

- **tolerance** (*float*) – Tolerance in percent (from 0.0 to 1.0) that indicates how much the images are allowed to differ. A higher value will make the comparison more tolerant. Defaults to 0.

Returns:  True if the images are equal, else False

Return type:  bool

GetSimilarity(*otherPic*, *colorTolerance=0*)[¶](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.GetSimilarity "Link to this definition")  
Calculates the similarity between two images as a value between 0.0 and 1.0. The similarity can be calculated as follows:

- Calculation of the absolute difference for each color for each pixel of the two images

- If the difference of the color is less than or equal to parameter colorTolerance, the color is considered as equal

- If otherPic is a transparent image, then all pixels that are not completely visible are considered equal

- The return value is the quotient of all equal pixel colors divided by the number of all pixel colors

If otherPic is an iterable object of Images, the highest value over all calculated similarities is returned.

Parameters:  - **otherPic** ([`Image`](apireport.md#tts.core.report.db.Image.Image "tts.core.report.db.Image.Image") | iterable[[`Image`](apireport.md#tts.core.report.db.Image.Image "tts.core.report.db.Image.Image")]) – Image or an iterable of Images to compare. The image(s) need to have the same size as the image they are compared with.

- **colorTolerance** (*int*) – The maximum allowed color difference (0…255) of a pixel to be considered as equal

Returns:  Similarity in range 0.0 to 1.0

Return type:  float

RecognizeText(*langList=None*, *ocrDataPath=None*)[¶](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.RecognizeText "Link to this definition")  
Tries to recognize text inside the image. This method does not apply any preprocessing to the image. To achieve best results you should ensure that the image uses black text on white background. You can use one of the builtin ImageFilters to manipulate your image (see [`ImageFiltersApi`](api.md#tts.testModule.multimedia.api.MultimediaApi.ImageFiltersApi "tts.testModule.multimedia.api.MultimediaApi.ImageFiltersApi")). Alternatively see [`FindText()`](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindText "tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindText") for a more sophisticated approach that applies automatic preprocessing.

Parameters:  - **langList** (*list\<str\>*) – List of language modules to use for text recognition. ecu.test comes with a preset list of available languages. For example use [‘eng’, ‘deu’] to recognize english and german text (in that order). The full list of default languages can be seen in the test configuration window. Additional language modules are available online, please refer to the tesseract documentation to download new language packs. If no language is specified then the languages from the currently active test configuration will be used. Note that if your test configuration contains more than one media node, the first node (in alphabetical order) will be used to load the ocr data.

- **ocrDataPath** (*str*) – The path to the directory containing your custom tesseract language files. If specified, all \*.traineddata files present in that directory will be added to the default languages as valid inputs for the langList parameter. Leave blank to use ecu.test’s default directory with its preset range of languages.

Returns:  The recognized text

Return type:  str

FindWord(*wordList=None*, *maxOccurrences=0*, *langList=None*, *ocrDataPath=None*, *isRegex=False*, *threshold=0.4*)[¶](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindWord "Link to this definition")  
Find single words in an image. Returns a list of matches containing information about the position of the desired word. This method applies various preprocessing steps, such as automatically inverting the colors to ensure the background is always white.

Parameters:  - **wordList** (*str* *|* *list[str]*) – (List of) desired word(s).

- **maxOccurrences** (*int*) – Maximum number of matches to be found. Use this, if you expect a string to occur exactly n times. The analysis will be stopped as soon as this number is reached. Can improve performance. If the value is 0, the full image will be analyzed.

- **langList** (*list[str]*) – List of language modules to use for text recognition. ecu.test comes with a preset list of available languages. For example use [‘eng’, ‘deu’] to recognize english and german text (in that order). The full list of default languages can be seen in the test configuration window. Additional language modules are available online, please refer to the tesseract documentation to download new language packs. If no language is specified then the languages from the currently active test configuration will be used. Note that if your test configuration contains more than one media node, the first node (in alphabetical order) will be used to load the ocr data.

- **ocrDataPath** (*str* *|* *None*) – The path to the directory containing your custom tesseract language files. If specified, all \*.traineddata files present in that directory will be added to the default languages as valid inputs for the langList parameter. Leave blank to use ecu.test’s default directory with its preset range of languages.

- **isRegex** (*bool*) – Set True to use regular expression as search strings.

- **threshold** (*float*) – Only results with a confidence larger than this threshold will be returned (between 0.0 and 1.0).

Returns:  List of matches that contain information about the text position sorted by their position.

Return type:  [TextMatchList](#tts.testModule.multimedia.dataElements.MatchObjects.TextMatchList "tts.testModule.multimedia.dataElements.MatchObjects.TextMatchList")

FindText(*searchStrings=None*, *maxOccurrences=0*, *langList=None*, *ocrDataPath=None*, *isRegex=False*, *strict=False*, *threshold=0.4*)[¶](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindText "Link to this definition")  
Find a text in an image. Returns a list of matches containing information about the position of the desired text. This method applies various preprocessing steps, such as automatically inverting the colors to ensure the background is always white. See [`RecognizeText()`](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.RecognizeText "tts.traceRecording.parser.formats.video.VideoRecording.Frame.RecognizeText") for a more basic approach without any preprocessing.

Parameters:  - **searchStrings** (*list[str]*) – List of desired text values.

- **maxOccurrences** (*int*) – Maximum number of matches to be found. Use this, if you expect a string to occur exactly n times. The analysis will be stopped as soon as this number is reached. Can improve performance. If the value is 0, the full image will be analyzed.

- **langList** (*list[str]*) – List of language modules to use for text recognition. ecu.test comes with a preset list of available languages. For example use [‘eng’, ‘deu’] to recognize english and german text (in that order). The full list of default languages can be seen in the test configuration window. Additional language modules are available online, please refer to the tesseract documentation to download new language packs. If no language is specified then the languages from the currently active test configuration will be used. Note that if your test configuration contains more than one media node, the first node (in alphabetical order) will be used to load the ocr data.

- **ocrDataPath** (*str* *|* *None*) – The path to the directory containing your custom tesseract language files. If specified, all \*.traineddata files present in that directory will be added to the default languages as valid inputs for the langList parameter. Leave blank to use ecu.test’s default directory with its preset range of languages.

- **isRegex** (*bool*) – Set True to use regular expression as search strings.

- **strict** (*bool*) – If False, this method will return all text matches that contain the search string. If True, it will only return results that exactly match the search string.

- **threshold** (*float*) – Only results with a confidence larger than this threshold will be returned (between 0.0 and 1.0).

Returns:  List of matches that contain information about the text position sorted by their position.

Return type:  [TextMatchList](#tts.testModule.multimedia.dataElements.MatchObjects.TextMatchList "tts.testModule.multimedia.dataElements.MatchObjects.TextMatchList")

FindImage(*image*, *maxOccurrences=100*, *threshold=0.9999*)[¶](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindImage "Link to this definition")  
Searches for a sub-image in this image. Returns a list of matches, containing information about the position of the sub-image.

Parameters:  - **image** ([`Image`](apireport.md#tts.core.report.db.Image.Image "tts.core.report.db.Image.Image")) – The image that will be searched for in the larger image. Its dimensions must not be greater than the source image.

- **maxOccurrences** (*int*) – The maximum number of occurrences to find. Set to 0 to find all occurrences. Limiting this number can improve performance when using low thresholds. Defaults to 100.

- **threshold** (*float*) – The similarity threshold in percent from 0 to 1 (Defaults to 0.9999 to avoid rounding errors). Determines how similar an image must be to be considered a match. A threshold of 1 will search only for perfect matches. Values of 0.9 and above will usually find closely matching regions in the image while ignoring noise. Note that a too low threshold might lead to wrong matches.

Returns:  List of image matches sorted by their position.

Return type:  [ImageMatchList](#tts.testModule.multimedia.dataElements.MatchObjects.ImageMatchList "tts.testModule.multimedia.dataElements.MatchObjects.ImageMatchList")

FindImages(*images*, *maxOccurrences=100*, *threshold=0.9999*)[¶](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindImages "Link to this definition")  
Searches for a list of sub-images in this image. Returns a list of matches, containing information about the position of the sub-image.

Parameters:  - **images** (list[[`Image`](apireport.md#tts.core.report.db.Image.Image "tts.core.report.db.Image.Image")]) – The images to be searched for in the larger image. Their dimensions must not be greater than the source image.

- **maxOccurrences** (*int*) – The maximum number of occurrences to find. Set to 0 to find all occurrences. Limiting this number can improve performance when using low thresholds. Defaults to 100.

- **threshold** (*float*) – The similarity threshold in percent from 0 to 1 (Defaults to 0.9999 to avoid rounding errors). Determines how similar an image must be to be considered a match. A threshold of 1 will search only for perfect matches. Values of 0.9 and above will usually find closely matching regions in the image while ignoring noise. Note that a too low threshold might lead to wrong matches.

Returns:  List of image matches sorted by their position.

Return type:  [ImageMatchList](#tts.testModule.multimedia.dataElements.MatchObjects.ImageMatchList "tts.testModule.multimedia.dataElements.MatchObjects.ImageMatchList")

FindImageByFeatures(*image*, *threshold=0.2*)[¶](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindImageByFeatures "Link to this definition")  
Searches for a sub-image within this image. This method does not compare every pixel. Instead, it looks for distinct features in both images and tries to match them. This makes it invariant to scale, rotation, color, and perspective. The features are detected by analyzing black/white color gradients. Therefore, complex patterns with hard edges between light and dark areas will be found best. This also means that an image with inverted colors will not be found. Dark areas must still be dark, and light areas light between source image and sub-image. Note that execution time will increase linearly with the number of sub-image occurences in the scene. E.g. if your scene contains the searched image twice then it will take twice as long to find all occurences compared to a scene where the sub-image occurs only once.

Parameters:  - **image** ([`Image`](apireport.md#tts.core.report.db.Image.Image "tts.core.report.db.Image.Image")) – The sub-image that will be searched for within the larger image.

- **threshold** (*float*) – The minimum confidence that a match must have to be considered a match. Values are in percent from 0 to 1 (defaults to 0.2). Higher values will filter out bad results but will also make the search less invariant to changes regarding scale, rotation, color, and perspective.

Returns:  A list of ImageMatches.

Return type:  [ImageMatchList](#tts.testModule.multimedia.dataElements.MatchObjects.ImageMatchList "tts.testModule.multimedia.dataElements.MatchObjects.ImageMatchList")

FindObjectByColor(*color*, *tolH*, *tolS*, *tolV*, *kernelSize=5*)[¶](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindObjectByColor "Link to this definition")  
Searches for objects with a given color (Color Detection). After applying a color filter, a dilation step connects identified pixel areas that lie within a distance of kernelSize. Each resulting pixel area will be represented by an [`ImageMatch`](#tts.testModule.multimedia.dataElements.MatchObjects.ImageMatch "tts.testModule.multimedia.dataElements.MatchObjects.ImageMatch") (rectangular area) of the returned `MatchList`.

The color filter is applied in HSV color schema. Therefore, the tolerances of the color filter must be provided in HSV schema.

Provided HSV parameters (tolH, tolS, tolV, color) must match the following conditions:

> - *Hue* is an integer between 0 and 180 and represents the position (in 2 degree steps) on the color circle. 180 corresponds to 360 degrees or a full circle and therefore is semantically equal to 0. (Please note: Some graphic programs provide different value ranges from 0 to 255 or from 0 to 360.)
>
> - *Saturation* is an integer between 0 and 255.
>
> - *Value* is an integer between 0 and 255

Parameters:  - **color** (*str*) – A color string. Either an RGB hex string (e.g. ‘#FF0000’ for red) or an HSV color string in the form ‘hsv(hue, saturation, value)’ (e.g. ‘hsv(120, 255, 255)’ for blue).

- **tolH** (*tuple[int,* *int]* *|* *int*) – The tolerance applied to the expected hue. The value can either be a tuple of integers for defining an asymmetric tolerance window (Hue(color) - tolH[0], Hue(color) + tolH[1]), or an integer for defining a symmetric tolerance window (Hue(color) - tolH, Hue(color) + tolH).

- **tolS** (*tuple[int,* *int]* *|* *int*) – The tolerance applied to the expected saturation. The value can either be a tuple of integers for defining an asymmetric tolerance window (Saturation(color) - tolS[0], Saturation(color) + tolS[1]), or an integer for defining a symmetric tolerance window (Saturation(color) - tolS, Saturation(color) + tolS).

- **tolV** (*tuple[int,* *int]* *|* *int*) – The tolerance applied to the expected value. It can either be a tuple of integers for defining an asymmetric tolerance window (Value(color) - tolV[0], Value(color) + tolV[1]), or an integer for defining a symmetric tolerance window (Value(color) - tolV, Value(color) + tolV).

- **kernelSize** (*int*) – The size of the kernel that is used to connect separated pixel areas to one object (dilation). A larger kernel connects pixel areas that have more distance to each other. Odd numbers must be provided! Defaults to 5.

Returns:  A list of ImageMatches.

Return type:  [ImageMatchList](#tts.testModule.multimedia.dataElements.MatchObjects.ImageMatchList "tts.testModule.multimedia.dataElements.MatchObjects.ImageMatchList")

FindBestTextMatches(*searchStrings=None*, *maxOccurrences=100*, *langList=None*, *ocrDataPath=None*, *isRegex=False*)[¶](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindBestTextMatches "Link to this definition")  
Finds texts in an image. Returns a list of matches sorted by the confidence.

Parameters:  - **searchStrings** (*list[str]*) – List with texts to find

- **maxOccurrences** (*int*) – Limits the number of matches to n items.

- **langList** (*list[str]*) – List of language modules to use for text recognition. ecu.test comes with a preset list of available languages. For example use [‘eng’, ‘deu’] to recognize english and german text (in that order). The full list of default languages can be seen in the test configuration window. Additional language modules are available online, please refer to the tesseract documentation to download new language packs. If no language is specified then the languages from the currently active test configuration will be used. Note that if your test configuration contains more than one media node, the first node (in alphabetical order) will be used to load the ocr data.

- **ocrDataPath** (*str* *|* *None*) – The path to the directory containing your custom tesseract language files. If specified, all \*.traineddata files present in that directory will be added to the default languages as valid inputs for the langList parameter. Leave blank to use ecu.test’s default directory with its preset range of languages.

- **isRegex** (*bool*) – Set True to use regular expression as search strings.

Returns:  List of matches that contain information about the text position sorted by their confidence.

Return type:  [TextMatchList](#tts.testModule.multimedia.dataElements.MatchObjects.TextMatchList "tts.testModule.multimedia.dataElements.MatchObjects.TextMatchList")

## OCRService[¶](#ocrservice "Link to this heading")

*class* OCRService[¶](#tts.lib.ocr.OCRService.OCRService "Link to this definition")  
*abstract* GetServiceId()[¶](#tts.lib.ocr.OCRService.OCRService.GetServiceId "Link to this definition")  
Returns the name of the service as a unique ID.

Returns:  Service identifier

Return type:  str

*abstract* ImageToText(*img*)[¶](#tts.lib.ocr.OCRService.OCRService.ImageToText "Link to this definition")  
Converts all text in the image into a single string.

Parameters:  **img** ([`Image`](#tts.testModule.multimedia.dataElements.Image.Image "tts.testModule.multimedia.dataElements.Image.Image")) – Input image as instance of class Image

Returns:  String representing the image’s text content

Return type:  str

*abstract* FindTextPositions(*img*)[¶](#tts.lib.ocr.OCRService.OCRService.FindTextPositions "Link to this definition")  
Looks for text in the image and return all text matches including found text, bounding box and confidence.

Parameters:  **img** ([`Image`](#tts.testModule.multimedia.dataElements.Image.Image "tts.testModule.multimedia.dataElements.Image.Image")) – Input image as instance of class Image

Returns:  List of found text positions

Return type:  [TextMatchList](#tts.testModule.multimedia.dataElements.MatchObjects.TextMatchList "tts.testModule.multimedia.dataElements.MatchObjects.TextMatchList")

*abstract* GetAvailableParameters()[¶](#tts.lib.ocr.OCRService.OCRService.GetAvailableParameters "Link to this definition")  
Returns a list of all available parameters. The dictionary representing a parameter must contain the fields ‘name’ and ‘default’ and may have an optional parameter ‘description’.

Returns:  List of all parameters of the service

Return type:  list[dict[str, *Any*]]

*abstract* GetParameter(*name*)[¶](#tts.lib.ocr.OCRService.OCRService.GetParameter "Link to this definition")  
Returns current value of parameter with given name.

Parameters:  **name** (*str*) – Name of the queried parameter

Returns:  Current value of the queried parameter

Return type:  *Any*

*abstract* SetParameter(*name*, *value*)[¶](#tts.lib.ocr.OCRService.OCRService.SetParameter "Link to this definition")  
Modifies existing default parameters of the OCR service.

Parameters:  - **name** (*str*) – Name of the parameter to be set

- **value** (*Any*) – New value for the parameter

## TextMatch[¶](#textmatch "Link to this heading")

*class* TextMatch[¶](#tts.testModule.multimedia.dataElements.MatchObjects.TextMatch "Link to this definition")  
Represents a text match.

GetText()[¶](#tts.testModule.multimedia.dataElements.MatchObjects.TextMatch.GetText "Link to this definition")  
Returns:  The found text.

Return type:  str

GetPosition(*absolutePosition=False*)[¶](#tts.testModule.multimedia.dataElements.MatchObjects.TextMatch.GetPosition "Link to this definition")  
Parameters:  **absolutePosition** (*bool*) – If True, the position relates to the original (unmasked) image.

Returns:  Position of the top left corner of the match (x, y).

Return type:  tuple[int, int]

GetDimensions()[¶](#tts.testModule.multimedia.dataElements.MatchObjects.TextMatch.GetDimensions "Link to this definition")  
Returns:  The width and height of the found match (w, h).

Return type:  tuple[int, int]

GetCenter(*absolutePosition=False*)[¶](#tts.testModule.multimedia.dataElements.MatchObjects.TextMatch.GetCenter "Link to this definition")  
Parameters:  **absolutePosition** (*bool*) – If True, the position relates to the original (unmasked) image.

Returns:  Position of the center of the match in the image (x, y).

Return type:  tuple[int, int]

## ImageMatch[¶](#imagematch "Link to this heading")

*class* ImageMatch[¶](#tts.testModule.multimedia.dataElements.MatchObjects.ImageMatch "Link to this definition")  
Represents an image match.

GetImage()[¶](#tts.testModule.multimedia.dataElements.MatchObjects.ImageMatch.GetImage "Link to this definition")  
Returns:  The searched image

Return type:  [`Image`](#tts.testModule.multimedia.dataElements.Image.Image "tts.testModule.multimedia.dataElements.Image.Image")

GetPosition(*absolutePosition=False*)[¶](#tts.testModule.multimedia.dataElements.MatchObjects.ImageMatch.GetPosition "Link to this definition")  
Parameters:  **absolutePosition** (*bool*) – If True, the position relates to the original (unmasked) image.

Returns:  Position of the top left corner of the match (x, y).

Return type:  tuple[int, int]

GetDimensions()[¶](#tts.testModule.multimedia.dataElements.MatchObjects.ImageMatch.GetDimensions "Link to this definition")  
Returns:  The width and height of the found match (w, h).

Return type:  tuple[int, int]

GetCenter(*absolutePosition=False*)[¶](#tts.testModule.multimedia.dataElements.MatchObjects.ImageMatch.GetCenter "Link to this definition")  
Parameters:  **absolutePosition** (*bool*) – If True, the position relates to the original (unmasked) image.

Returns:  Position of the center of the match in the image (x, y).

Return type:  tuple[int, int]

## MatchList[¶](#matchlist "Link to this heading")

*class* ImageMatchList[¶](#tts.testModule.multimedia.dataElements.MatchObjects.ImageMatchList "Link to this definition")  
This is a list containing [`ImageMatch`](#tts.testModule.multimedia.dataElements.MatchObjects.ImageMatch "tts.testModule.multimedia.dataElements.MatchObjects.ImageMatch") objects. It can be used like a normal python list object, but offers some additional features.

Filter(*predicate*)[¶](#tts.testModule.multimedia.dataElements.MatchObjects.ImageMatchList.Filter "Link to this definition")  
Filters the current match list based on a user defined filter predicate.

Parameters:  **predicate** (*Callable*) – A function to execute for each element in the list. It should return True to keep the element in the resulting list, and False otherwise.

Returns:  A new match list containing just the elements that pass the test

Return type:  MatchList

*class* TextMatchList[¶](#tts.testModule.multimedia.dataElements.MatchObjects.TextMatchList "Link to this definition")  
This is a list containing [`TextMatch`](#tts.testModule.multimedia.dataElements.MatchObjects.TextMatch "tts.testModule.multimedia.dataElements.MatchObjects.TextMatch") objects. It can be used like a normal python list object, but offers some additional features.

ContainsText(*text*)[¶](#tts.testModule.multimedia.dataElements.MatchObjects.TextMatchList.ContainsText "Link to this definition")  
Checks if a list of TextMatches contains a given string.

Parameters:  **text** (*str*) – The text that will be searched in the list (case-sensitive).

Returns:  Returns True if the list contains any element with the given text.

Return type:  bool

Filter(*predicate*)[¶](#tts.testModule.multimedia.dataElements.MatchObjects.TextMatchList.Filter "Link to this definition")  
Filters the current match list based on a user defined filter predicate.

Parameters:  **predicate** (*Callable*) – A function to execute for each element in the list. It should return True to keep the element in the resulting list, and False otherwise.

Returns:  A new match list containing just the elements that pass the test

Return type:  MatchList

## AudioBlock[¶](#audioblock "Link to this heading")

*class* AudioBlock[¶](#tts.testModule.multimedia.dataElements.AudioBlock.AudioBlock "Link to this definition")  
Parameters:  - **data** (*str* *|* *npt.NDArray[np.int16]* *|* *npt.NDArray[float]*) – The source from which to load audio data (a file path or a NumPy array). In case of a file path it has to be an absolute path or a path relative to the workspace. In case of a NumPy array, the audio channels must either be a 1D NumPy array of shape `(<frames>)` for a one channel stream or a 2D NumPy array of shape `(<frames>, <channels>)`for a multiple channel stream. Array members must be of type np.int16 or float. The former will be internally normalized to float between -1.0 and 1.0.

- **sampleRate** (*Optional[int]*) – The sample rate of the audio data. If the AudioBlock is created from a NumPy array, the sample rate can be passed. If the audio data is loaded from file, the sample rate will be extracted.

Creates a new AudioBlock object from a given NumPy array or a file. Is also returned by the read step of a mapping of type audio device being accessible via the media access tab. However, the audio recording feature is still in development, and thus hidden behind a feature flag.

The supported audio formats are (according to soundfile version 0.12.1):

> - ‘AIFF’: ‘AIFF (Apple/SGI)’,
>
> - ‘AU’: ‘AU (Sun/NeXT)’,
>
> - ‘AVR’: ‘AVR (Audio Visual Research)’,
>
> - ‘CAF’: ‘CAF (Apple Core Audio File)’,
>
> - ‘FLAC’: ‘FLAC (Free Lossless Audio Codec)’,
>
> - ‘HTK’: ‘HTK (HMM Tool Kit)’,
>
> - ‘SVX’: ‘IFF (Amiga IFF/SVX8/SV16)’,
>
> - ‘MAT4’: ‘MAT4 (GNU Octave 2.0 / Matlab 4.2)’,
>
> - ‘MAT5’: ‘MAT5 (GNU Octave 2.1 / Matlab 5.0)’,
>
> - ‘MPC2K’: ‘MPC (Akai MPC 2k)’,
>
> - ‘MP3’: ‘MPEG-1/2 Audio’,
>
> - ‘OGG’: ‘OGG (OGG Container format)’,
>
> - ‘PAF’: ‘PAF (Ensoniq PARIS)’,
>
> - ‘PVF’: ‘PVF (Portable Voice Format)’,
>
> - ‘RAW’: ‘RAW (header-less)’,
>
> - ‘RF64’: ‘RF64 (RIFF 64)’,
>
> - ‘SD2’: ‘SD2 (Sound Designer II)’,
>
> - ‘SDS’: ‘SDS (Midi Sample Dump Standard)’,
>
> - ‘IRCAM’: ‘SF (Berkeley/IRCAM/CARL)’,
>
> - ‘VOC’: ‘VOC (Creative Labs)’,
>
> - ‘W64’: ‘W64 (SoundFoundry WAVE 64)’,
>
> - ‘WAV’: ‘WAV (Microsoft)’,
>
> - ‘NIST’: ‘WAV (NIST Sphere)’,
>
> - ‘WAVEX’: ‘WAVEX (Microsoft)’,
>
> - ‘WVE’: ‘WVE (Psion Series 3)’,
>
> - ‘XI’: ‘XI (FastTracker 2)’

Example usage:

> - `AudioBlock(numpy.array([1, 2, 3, ... 98, 99, 100]), 44100) # AudioBlock with one channel`>
> - `AudioBlock(numpy.array([[8, 3], [2, 6], ... [5, 7]]), 88200) # AudioBlock with two channels`>
> - `AudioBlock('path/to/file/filename.extension') # AudioBlock from file`GetData()[¶](#tts.testModule.multimedia.dataElements.AudioBlock.AudioBlock.GetData "Link to this definition")  
Returns the data of the audio channel(s).

Returns:  Data of the audio channels as 1D NumPy array (frames) if only one channel exists in case of multiple channels a 2D NumPy array (frames x channels).

Return type:  *ndarray*[*Any*, *dtype*[float]]

GetChannelData(*channel*)[¶](#tts.testModule.multimedia.dataElements.AudioBlock.AudioBlock.GetChannelData "Link to this definition")  
Returns the data of the specified audio channel.

Parameters:  **channel** (*int*) – Channel number starting with 1.

Returns:  Audio data of the specified audio channel as 1D NumPy array.

Raises:  
**IndexError** – Channel does not exist.

Return type:  *ndarray*[*Any*, *dtype*[float]]

GetChannelCount()[¶](#tts.testModule.multimedia.dataElements.AudioBlock.AudioBlock.GetChannelCount "Link to this definition")  
Returns the number of channels.

Returns:  Number of channels

Return type:  int

GetDuration()[¶](#tts.testModule.multimedia.dataElements.AudioBlock.AudioBlock.GetDuration "Link to this definition")  
Returns the duration of the audio block in seconds if data and sample rate are defined. Otherwise 0.0 is returned.

Returns:  Duration in seconds

Return type:  float

GetSampleRate()[¶](#tts.testModule.multimedia.dataElements.AudioBlock.AudioBlock.GetSampleRate "Link to this definition")  
Returns the sample rate.

Returns:  Sample rate

Return type:  int | None

FindSnippet(*snippet*, *threshold=0.35*, *noiseResistantComparison=False*)[¶](#tts.testModule.multimedia.dataElements.AudioBlock.AudioBlock.FindSnippet "Link to this definition")  
Searches in the data of the AudioBlock for the passed snippet. If the noiseResistantComparison flag is set, it is possible to search the snippet within noisy data, but the confidence value is generally lower.

Parameters:  - **snippet** ([*AudioBlock*](#tts.testModule.multimedia.dataElements.AudioBlock.AudioBlock "tts.testModule.multimedia.dataElements.AudioBlock.AudioBlock")) – The searched snippet.

- **threshold** (*float*) – Threshold for the confidence value. Only matches with a higher confidence value will be returned.

- **noiseResistantComparison** (*bool*) – Specifies whether the noise resistant algorithm shall be used.

Returns:  Confidence values and positions at which the snippet was found.

Return type:  list[tuple[float, float]]

Save(*path*, *fileFormat='FLAC'*, *mono=False*)[¶](#tts.testModule.multimedia.dataElements.AudioBlock.AudioBlock.Save "Link to this definition")  
Saves the AudioBlock as an audio file.

The format of the audio file is FLAC either with the given sample rate or the default value of 44100 Hz, a bit depth of 16 bits and is limited to a maximum of 8 channels.

Parameters:  - **path** (*str*) – Save location of the AudioBlock with filename and file ending.

- **fileFormat** (*str*) – Audio file format, default: FLAC

- **mono** (*bool*) – Convert multichannel data to mono
