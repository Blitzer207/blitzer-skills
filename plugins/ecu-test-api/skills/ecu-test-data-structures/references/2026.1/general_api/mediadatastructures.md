[ Internal APIs ](api.md)

[ Advanced operations of package variable types ](variabledatastructures.md)

[ Advanced properties of bus-related objects ](busdatastructures.md)

[ Bus related objects of trace analysis ](busdatastructuresTraceanalysis.md)

[ Advanced properties of diagnostics-related objects ](diagdatastructures.md)

[ Diagnostics related objects of trace analysis ](diagdatastructuresTraceanalysis.md)

Advanced properties of media-related objects [ Advanced properties of media-related objects ](#)

Advanced properties of media-related objects

- [ Image ](#image)
  - [C Image ](#tts.testModule.multimedia.dataElements.Image.Image)
    - [M GetData ](#tts.testModule.multimedia.dataElements.Image.Image.GetData)
    - [M GetDataWithAlpha ](#tts.testModule.multimedia.dataElements.Image.Image.GetDataWithAlpha)
    - [M GetAlpha ](#tts.testModule.multimedia.dataElements.Image.Image.GetAlpha)
    - [M GetDimensions ](#tts.testModule.multimedia.dataElements.Image.Image.GetDimensions)
    - [M Save ](#tts.testModule.multimedia.dataElements.Image.Image.Save)
    - [M Crop ](#tts.testModule.multimedia.dataElements.Image.Image.Crop)
    - [M GetSimilarity ](#tts.testModule.multimedia.dataElements.Image.Image.GetSimilarity)
    - [M IsEqual ](#tts.testModule.multimedia.dataElements.Image.Image.IsEqual)
    - [M Contains ](#tts.testModule.multimedia.dataElements.Image.Image.Contains)
    - [M FindImage ](#tts.testModule.multimedia.dataElements.Image.Image.FindImage)
    - [M FindImages ](#tts.testModule.multimedia.dataElements.Image.Image.FindImages)
    - [M FindImageByFeatures ](#tts.testModule.multimedia.dataElements.Image.Image.FindImageByFeatures)
    - [M FindObjectByColor ](#tts.testModule.multimedia.dataElements.Image.Image.FindObjectByColor)
    - [M FindWord ](#tts.testModule.multimedia.dataElements.Image.Image.FindWord)
    - [M FindText ](#tts.testModule.multimedia.dataElements.Image.Image.FindText)
    - [M FindBestTextMatches ](#tts.testModule.multimedia.dataElements.Image.Image.FindBestTextMatches)
    - [M RecognizeText ](#tts.testModule.multimedia.dataElements.Image.Image.RecognizeText)
    - [M EmbedInReport ](#tts.testModule.multimedia.dataElements.Image.Image.EmbedInReport)
- [ Mask ](#mask)
  - [C Mask ](#tts.testModule.multimedia.dataElements.Mask.Mask)
    - [M Apply ](#tts.testModule.multimedia.dataElements.Mask.Mask.Apply)
- [ Frame ](#frame)
  - [C Frame ](#tts.traceRecording.parser.formats.video.VideoRecording.Frame)
    - [M GetCaptureInfo ](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.GetCaptureInfo)
    - [M GetNumber ](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.GetNumber)
    - [M GetTime ](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.GetTime)
    - [M GetData ](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.GetData)
    - [M GetAlpha ](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.GetAlpha)
    - [M GetDataWithAlpha ](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.GetDataWithAlpha)
    - [M GetDimensions ](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.GetDimensions)
    - [M Save ](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.Save)
    - [M Crop ](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.Crop)
    - [M Contains ](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.Contains)
    - [M IsEqual ](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.IsEqual)
    - [M GetSimilarity ](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.GetSimilarity)
    - [M RecognizeText ](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.RecognizeText)
    - [M FindWord ](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindWord)
    - [M FindText ](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindText)
    - [M FindImage ](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindImage)
    - [M FindImages ](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindImages)
    - [M FindImageByFeatures ](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindImageByFeatures)
    - [M FindObjectByColor ](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindObjectByColor)
    - [M FindBestTextMatches ](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindBestTextMatches)
    - [M EmbedInReport ](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.EmbedInReport)
- [ OCRService ](#ocrservice)
  - [C OCRService ](#tts.lib.ocr.OCRService.OCRService)
    - [M GetServiceId ](#tts.lib.ocr.OCRService.OCRService.GetServiceId)
    - [M ImageToText ](#tts.lib.ocr.OCRService.OCRService.ImageToText)
    - [M FindTextPositions ](#tts.lib.ocr.OCRService.OCRService.FindTextPositions)
    - [M GetAvailableParameters ](#tts.lib.ocr.OCRService.OCRService.GetAvailableParameters)
    - [M GetParameter ](#tts.lib.ocr.OCRService.OCRService.GetParameter)
    - [M SetParameter ](#tts.lib.ocr.OCRService.OCRService.SetParameter)
- [ TextMatch ](#textmatch)
  - [C TextMatch ](#tts.testModule.multimedia.dataElements.MatchObjects.TextMatch)
    - [M GetText ](#tts.testModule.multimedia.dataElements.MatchObjects.TextMatch.GetText)
    - [M GetPosition ](#tts.testModule.multimedia.dataElements.MatchObjects.TextMatch.GetPosition)
    - [M GetDimensions ](#tts.testModule.multimedia.dataElements.MatchObjects.TextMatch.GetDimensions)
    - [M GetCenter ](#tts.testModule.multimedia.dataElements.MatchObjects.TextMatch.GetCenter)
    - [M GetConfidence ](#tts.testModule.multimedia.dataElements.MatchObjects.TextMatch.GetConfidence)
- [ ImageMatch ](#imagematch)
  - [C ImageMatch ](#tts.testModule.multimedia.dataElements.MatchObjects.ImageMatch)
    - [M GetImage ](#tts.testModule.multimedia.dataElements.MatchObjects.ImageMatch.GetImage)
    - [M GetPosition ](#tts.testModule.multimedia.dataElements.MatchObjects.ImageMatch.GetPosition)
    - [M GetDimensions ](#tts.testModule.multimedia.dataElements.MatchObjects.ImageMatch.GetDimensions)
    - [M GetCenter ](#tts.testModule.multimedia.dataElements.MatchObjects.ImageMatch.GetCenter)
    - [M GetConfidence ](#tts.testModule.multimedia.dataElements.MatchObjects.ImageMatch.GetConfidence)
- [ MatchList ](#matchlist)
  - [C ImageMatchList ](#tts.testModule.multimedia.dataElements.MatchObjects.ImageMatchList)
    - [M Filter ](#tts.testModule.multimedia.dataElements.MatchObjects.ImageMatchList.Filter)
  - [C TextMatchList ](#tts.testModule.multimedia.dataElements.MatchObjects.TextMatchList)
    - [M ContainsText ](#tts.testModule.multimedia.dataElements.MatchObjects.TextMatchList.ContainsText)
    - [M FilterByText ](#tts.testModule.multimedia.dataElements.MatchObjects.TextMatchList.FilterByText)
    - [M Filter ](#tts.testModule.multimedia.dataElements.MatchObjects.TextMatchList.Filter)
- [ AudioBlock ](#audioblock)
  - [C AudioBlock ](#tts.testModule.multimedia.dataElements.AudioBlock.AudioBlock)
    - [M GetData ](#tts.testModule.multimedia.dataElements.AudioBlock.AudioBlock.GetData)
    - [M GetChannelData ](#tts.testModule.multimedia.dataElements.AudioBlock.AudioBlock.GetChannelData)
    - [M GetChannelCount ](#tts.testModule.multimedia.dataElements.AudioBlock.AudioBlock.GetChannelCount)
    - [M GetDuration ](#tts.testModule.multimedia.dataElements.AudioBlock.AudioBlock.GetDuration)
    - [M GetSampleRate ](#tts.testModule.multimedia.dataElements.AudioBlock.AudioBlock.GetSampleRate)
    - [M FindSnippet ](#tts.testModule.multimedia.dataElements.AudioBlock.AudioBlock.FindSnippet)
    - [M Save ](#tts.testModule.multimedia.dataElements.AudioBlock.AudioBlock.Save)

[ Advanced properties of DLT logging-related objects ](dltdatastructures.md)

[ COM API ](com-api.md)

[ REST API ](rest-api.md)

[ Report API ](apireport.md)

[ Object API ](objectApi.md)

[ Trace Analysis API ](../TraceAnalysisAPI/index.md)

[ Generator APIs ](../generators/index.md)

[ Tools ](../tools/index.md)

[ User test management ](../userTestmanagement/index.md)

[ UserUtility API ](../user-utility/user-utility.md)

[ Utility Examples ](../user-utility/example-utilities.md)

Advanced properties of media-related objects

- [ Image ](#image)
  - [C Image ](#tts.testModule.multimedia.dataElements.Image.Image)
    - [M GetData ](#tts.testModule.multimedia.dataElements.Image.Image.GetData)
    - [M GetDataWithAlpha ](#tts.testModule.multimedia.dataElements.Image.Image.GetDataWithAlpha)
    - [M GetAlpha ](#tts.testModule.multimedia.dataElements.Image.Image.GetAlpha)
    - [M GetDimensions ](#tts.testModule.multimedia.dataElements.Image.Image.GetDimensions)
    - [M Save ](#tts.testModule.multimedia.dataElements.Image.Image.Save)
    - [M Crop ](#tts.testModule.multimedia.dataElements.Image.Image.Crop)
    - [M GetSimilarity ](#tts.testModule.multimedia.dataElements.Image.Image.GetSimilarity)
    - [M IsEqual ](#tts.testModule.multimedia.dataElements.Image.Image.IsEqual)
    - [M Contains ](#tts.testModule.multimedia.dataElements.Image.Image.Contains)
    - [M FindImage ](#tts.testModule.multimedia.dataElements.Image.Image.FindImage)
    - [M FindImages ](#tts.testModule.multimedia.dataElements.Image.Image.FindImages)
    - [M FindImageByFeatures ](#tts.testModule.multimedia.dataElements.Image.Image.FindImageByFeatures)
    - [M FindObjectByColor ](#tts.testModule.multimedia.dataElements.Image.Image.FindObjectByColor)
    - [M FindWord ](#tts.testModule.multimedia.dataElements.Image.Image.FindWord)
    - [M FindText ](#tts.testModule.multimedia.dataElements.Image.Image.FindText)
    - [M FindBestTextMatches ](#tts.testModule.multimedia.dataElements.Image.Image.FindBestTextMatches)
    - [M RecognizeText ](#tts.testModule.multimedia.dataElements.Image.Image.RecognizeText)
    - [M EmbedInReport ](#tts.testModule.multimedia.dataElements.Image.Image.EmbedInReport)
- [ Mask ](#mask)
  - [C Mask ](#tts.testModule.multimedia.dataElements.Mask.Mask)
    - [M Apply ](#tts.testModule.multimedia.dataElements.Mask.Mask.Apply)
- [ Frame ](#frame)
  - [C Frame ](#tts.traceRecording.parser.formats.video.VideoRecording.Frame)
    - [M GetCaptureInfo ](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.GetCaptureInfo)
    - [M GetNumber ](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.GetNumber)
    - [M GetTime ](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.GetTime)
    - [M GetData ](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.GetData)
    - [M GetAlpha ](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.GetAlpha)
    - [M GetDataWithAlpha ](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.GetDataWithAlpha)
    - [M GetDimensions ](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.GetDimensions)
    - [M Save ](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.Save)
    - [M Crop ](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.Crop)
    - [M Contains ](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.Contains)
    - [M IsEqual ](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.IsEqual)
    - [M GetSimilarity ](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.GetSimilarity)
    - [M RecognizeText ](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.RecognizeText)
    - [M FindWord ](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindWord)
    - [M FindText ](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindText)
    - [M FindImage ](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindImage)
    - [M FindImages ](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindImages)
    - [M FindImageByFeatures ](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindImageByFeatures)
    - [M FindObjectByColor ](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindObjectByColor)
    - [M FindBestTextMatches ](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindBestTextMatches)
    - [M EmbedInReport ](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.EmbedInReport)
- [ OCRService ](#ocrservice)
  - [C OCRService ](#tts.lib.ocr.OCRService.OCRService)
    - [M GetServiceId ](#tts.lib.ocr.OCRService.OCRService.GetServiceId)
    - [M ImageToText ](#tts.lib.ocr.OCRService.OCRService.ImageToText)
    - [M FindTextPositions ](#tts.lib.ocr.OCRService.OCRService.FindTextPositions)
    - [M GetAvailableParameters ](#tts.lib.ocr.OCRService.OCRService.GetAvailableParameters)
    - [M GetParameter ](#tts.lib.ocr.OCRService.OCRService.GetParameter)
    - [M SetParameter ](#tts.lib.ocr.OCRService.OCRService.SetParameter)
- [ TextMatch ](#textmatch)
  - [C TextMatch ](#tts.testModule.multimedia.dataElements.MatchObjects.TextMatch)
    - [M GetText ](#tts.testModule.multimedia.dataElements.MatchObjects.TextMatch.GetText)
    - [M GetPosition ](#tts.testModule.multimedia.dataElements.MatchObjects.TextMatch.GetPosition)
    - [M GetDimensions ](#tts.testModule.multimedia.dataElements.MatchObjects.TextMatch.GetDimensions)
    - [M GetCenter ](#tts.testModule.multimedia.dataElements.MatchObjects.TextMatch.GetCenter)
    - [M GetConfidence ](#tts.testModule.multimedia.dataElements.MatchObjects.TextMatch.GetConfidence)
- [ ImageMatch ](#imagematch)
  - [C ImageMatch ](#tts.testModule.multimedia.dataElements.MatchObjects.ImageMatch)
    - [M GetImage ](#tts.testModule.multimedia.dataElements.MatchObjects.ImageMatch.GetImage)
    - [M GetPosition ](#tts.testModule.multimedia.dataElements.MatchObjects.ImageMatch.GetPosition)
    - [M GetDimensions ](#tts.testModule.multimedia.dataElements.MatchObjects.ImageMatch.GetDimensions)
    - [M GetCenter ](#tts.testModule.multimedia.dataElements.MatchObjects.ImageMatch.GetCenter)
    - [M GetConfidence ](#tts.testModule.multimedia.dataElements.MatchObjects.ImageMatch.GetConfidence)
- [ MatchList ](#matchlist)
  - [C ImageMatchList ](#tts.testModule.multimedia.dataElements.MatchObjects.ImageMatchList)
    - [M Filter ](#tts.testModule.multimedia.dataElements.MatchObjects.ImageMatchList.Filter)
  - [C TextMatchList ](#tts.testModule.multimedia.dataElements.MatchObjects.TextMatchList)
    - [M ContainsText ](#tts.testModule.multimedia.dataElements.MatchObjects.TextMatchList.ContainsText)
    - [M FilterByText ](#tts.testModule.multimedia.dataElements.MatchObjects.TextMatchList.FilterByText)
    - [M Filter ](#tts.testModule.multimedia.dataElements.MatchObjects.TextMatchList.Filter)
- [ AudioBlock ](#audioblock)
  - [C AudioBlock ](#tts.testModule.multimedia.dataElements.AudioBlock.AudioBlock)
    - [M GetData ](#tts.testModule.multimedia.dataElements.AudioBlock.AudioBlock.GetData)
    - [M GetChannelData ](#tts.testModule.multimedia.dataElements.AudioBlock.AudioBlock.GetChannelData)
    - [M GetChannelCount ](#tts.testModule.multimedia.dataElements.AudioBlock.AudioBlock.GetChannelCount)
    - [M GetDuration ](#tts.testModule.multimedia.dataElements.AudioBlock.AudioBlock.GetDuration)
    - [M GetSampleRate ](#tts.testModule.multimedia.dataElements.AudioBlock.AudioBlock.GetSampleRate)
    - [M FindSnippet ](#tts.testModule.multimedia.dataElements.AudioBlock.AudioBlock.FindSnippet)
    - [M Save ](#tts.testModule.multimedia.dataElements.AudioBlock.AudioBlock.Save)

# Advanced properties of media-related objects[¶](#advanced-properties-of-media-related-objects "Link to this heading")

The following types are globally available. E.g. in function variables, UserPyModules or other user code:

- [`Image`](#tts.testModule.multimedia.dataElements.Image.Image "tts.testModule.multimedia.dataElements.Image.Image (Python class) — Represents an image.")

- [`Mask`](#tts.testModule.multimedia.dataElements.Mask.Mask "tts.testModule.multimedia.dataElements.Mask.Mask (Python class) — The mask file to load")

- [`AudioBlock`](#tts.testModule.multimedia.dataElements.AudioBlock.AudioBlock "tts.testModule.multimedia.dataElements.AudioBlock.AudioBlock (Python class) — The source from which to load audio data (a file path or a NumPy array). In case of a file path it has to be an absolute path or a path relative to the workspace. In case of a NumPy array, the audio channels must either be a 1D NumPy array of shape (<frames>) for a one channel stream or a 2D NumPy array of shape (<frames>, <channels>) for a multiple channel stream. Array members must be of type np.int16 or float. The former will be internally normalized to float between -1.0 and 1.0.")

## Image[¶](#image "Link to this heading")

*class* Image[¶](#tts.testModule.multimedia.dataElements.Image.Image "Link to this definition")  
Represents an image.

Parameters:  arg : str | numpy.ndarray  
The data from which to load an image (a file path or a numpy array)

Creates a new Image object either from a file or from a given numpy array. The following filetypes are supported when passing a file path:

- Windows bitmaps (\*.bmp, \*.dib)

- JPEG files (\*.jpeg, \*.jpg, \*.jpe)

- JPEG 2000 files (\*.jp2)

- Portable Network Graphics (\*.png)

- WebP (\*.webp)

- Portable image format (\*.pbm, \*.pgm, \*.ppm, \*.pxm, \*.pnm)

- PFM files (\*.pfm)

- Sun rasters (\*.sr, \*.ras)

- TIFF files (\*.tiff, \*.tif)

- OpenEXR Image files (\*.exr)

- Radiance HDR (\*.hdr, \*.pic)

The file path can be a path relative to the workspace directory. When passing a numpy array, the array must be three-dimensional, i.e. its shape must be of the form `(<height>, <width>, <channels>)`. It must have either one, three, or four channels. Alternatively, if the array holds only a single channel the last dimension may be omitted, passing in only a two-dimensional array, i.e. its shape may be of the form `(<height>, <width>)`. Depending on the number of channels provided, the image will be constructed in a different manner:

- One channel: each value will be copied to all three color channels, resulting in a grayscale image (with three color channels).

- Three channels: The channels are interpreted as color channels (blue, green, red).

- Four channels: The first three channels will be interpreted as color channels, the values of the fourth will be stored as an alpha channel for transparency.

Example usage:

- `Image("path/to/image.png")  # Loads the file "image.png"`- `Image(numpy.zeros((768, 1024)))  # an empty Image that is 1024px wide and 768px high`GetData()[¶](#tts.testModule.multimedia.dataElements.Image.Image.GetData "Link to this definition")  
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

Save(*[path](#tts.testModule.multimedia.dataElements.Image.Image.Save.path "tts.testModule.multimedia.dataElements.Image.Image.Save.path (Python parameter) — Path where the image file should be saved.")*)[¶](#tts.testModule.multimedia.dataElements.Image.Image.Save "Link to this definition")  
Saves the image as file.

Parameters:  path : str[¶](#tts.testModule.multimedia.dataElements.Image.Image.Save.path "Permalink to this definition")  
Path where the image file should be saved. The path must include the file extension. A relative path is resolved relative to the workspace path.

Crop(*[x](#tts.testModule.multimedia.dataElements.Image.Image.Crop.x "tts.testModule.multimedia.dataElements.Image.Image.Crop.x (Python parameter) — x position of the upper left corner of the cutout")*, *[y](#tts.testModule.multimedia.dataElements.Image.Image.Crop.y "tts.testModule.multimedia.dataElements.Image.Image.Crop.y (Python parameter) — y position of the upper left corner of the cutout")*, *[width](#tts.testModule.multimedia.dataElements.Image.Image.Crop.width "tts.testModule.multimedia.dataElements.Image.Image.Crop.width (Python parameter) — Width of the cutout")*, *[height](#tts.testModule.multimedia.dataElements.Image.Image.Crop.height "tts.testModule.multimedia.dataElements.Image.Image.Crop.height (Python parameter) — Height of the cutout")*)[¶](#tts.testModule.multimedia.dataElements.Image.Image.Crop "Link to this definition")  
Crops the image.

Parameters:  x : int[¶](#tts.testModule.multimedia.dataElements.Image.Image.Crop.x "Permalink to this definition")  
x position of the upper left corner of the cutout

y : int[¶](#tts.testModule.multimedia.dataElements.Image.Image.Crop.y "Permalink to this definition")  
y position of the upper left corner of the cutout

width : int[¶](#tts.testModule.multimedia.dataElements.Image.Image.Crop.width "Permalink to this definition")  
Width of the cutout

height : int[¶](#tts.testModule.multimedia.dataElements.Image.Image.Crop.height "Permalink to this definition")  
Height of the cutout

Returns:  Cropped image

Return type:  [`Image`](#tts.testModule.multimedia.dataElements.Image.Image "tts.testModule.multimedia.dataElements.Image.Image (Python class) — Represents an image.")

GetSimilarity(*[otherPic](#tts.testModule.multimedia.dataElements.Image.Image.GetSimilarity.otherPic "tts.testModule.multimedia.dataElements.Image.Image.GetSimilarity.otherPic (Python parameter) — Image or an iterable of Images to compare.")*, *[colorTolerance](#tts.testModule.multimedia.dataElements.Image.Image.GetSimilarity.colorTolerance "tts.testModule.multimedia.dataElements.Image.Image.GetSimilarity.colorTolerance (Python parameter) — The maximum allowed color difference (0...255) of a pixel to be considered as equal")=`0`*)[¶](#tts.testModule.multimedia.dataElements.Image.Image.GetSimilarity "Link to this definition")  
Calculates the similarity between two images as a value between 0.0 and 1.0. The similarity can be calculated as follows:

- Calculation of the absolute difference for each color for each pixel of the two images

- If the difference of the color is less than or equal to parameter colorTolerance, the color is considered as equal

- If otherPic is a transparent image, then all pixels that are not completely visible are considered equal

- The return value is the quotient of all equal pixel colors divided by the number of all pixel colors

If otherPic is an iterable object of Images, the highest value over all calculated similarities is returned.

Parameters:  otherPic[¶](#tts.testModule.multimedia.dataElements.Image.Image.GetSimilarity.otherPic "Permalink to this definition")  
Image or an iterable of Images to compare. The image(s) need to have the same size as the image they are compared with.

colorTolerance : int[¶](#tts.testModule.multimedia.dataElements.Image.Image.GetSimilarity.colorTolerance "Permalink to this definition")  
The maximum allowed color difference (0…255) of a pixel to be considered as equal

Returns:  Similarity in range 0.0 to 1.0

Return type:  float

IsEqual(*[otherPic](#tts.testModule.multimedia.dataElements.Image.Image.IsEqual.otherPic "tts.testModule.multimedia.dataElements.Image.Image.IsEqual.otherPic (Python parameter) — The image to compare.")*, *[colorTolerance](#tts.testModule.multimedia.dataElements.Image.Image.IsEqual.colorTolerance "tts.testModule.multimedia.dataElements.Image.Image.IsEqual.colorTolerance (Python parameter) — The maximum allowed color difference (0...255) of a pixel to be considered as equal.")=`0`*, *[tolerance](#tts.testModule.multimedia.dataElements.Image.Image.IsEqual.tolerance "tts.testModule.multimedia.dataElements.Image.Image.IsEqual.tolerance (Python parameter) — Tolerance in percent (from 0.0 to 1.0) that indicates how much the images are allowed to differ.")=`0`*)[¶](#tts.testModule.multimedia.dataElements.Image.Image.IsEqual "Link to this definition")  
Determines via [`GetSimilarity()`](#tts.testModule.multimedia.dataElements.Image.Image.GetSimilarity "tts.testModule.multimedia.dataElements.Image.Image.GetSimilarity (Python method) — Calculates the similarity between two images as a value between 0.0 and 1.0. The similarity can be calculated as follows:") the similarity to otherPic. If the similarity is within the specified tolerance then True is returned. Otherwise, False.

Parameters:  otherPic[¶](#tts.testModule.multimedia.dataElements.Image.Image.IsEqual.otherPic "Permalink to this definition")  
The image to compare. The image needs to have the same size as the image it is compared with.

colorTolerance : int[¶](#tts.testModule.multimedia.dataElements.Image.Image.IsEqual.colorTolerance "Permalink to this definition")  
The maximum allowed color difference (0…255) of a pixel to be considered as equal.

tolerance : float[¶](#tts.testModule.multimedia.dataElements.Image.Image.IsEqual.tolerance "Permalink to this definition")  
Tolerance in percent (from 0.0 to 1.0) that indicates how much the images are allowed to differ. A higher value will make the comparison more tolerant. Defaults to 0.

Returns:  True if the images are equal, else False

Return type:  bool

Contains(*[otherPic](#tts.testModule.multimedia.dataElements.Image.Image.Contains.otherPic "tts.testModule.multimedia.dataElements.Image.Image.Contains.otherPic (Python parameter) — The searched image or an iterator over multiple searched images")*, *[colorTolerance](#tts.testModule.multimedia.dataElements.Image.Image.Contains.colorTolerance "tts.testModule.multimedia.dataElements.Image.Image.Contains.colorTolerance (Python parameter) — The maximum allowed color difference (0...255) of a pixel to be considered as equal.")=`0`*, *[tolerance](#tts.testModule.multimedia.dataElements.Image.Image.Contains.tolerance "tts.testModule.multimedia.dataElements.Image.Image.Contains.tolerance (Python parameter) — Tolerance in percent (from 0.0 to 1.0) that indicates how much the image is allowed to differ from a potential match.")=`0`*)[¶](#tts.testModule.multimedia.dataElements.Image.Image.Contains "Link to this definition")  
Checks if otherPic is contained in this image.

At first, the closest matching section to otherPic is determined. Then, the similarity between the cropped image and otherPic is calculated. If the similarity is within the specified tolerance then True is returned. Otherwise, False.

If otherPic is an iterable object of Images, this method returns True if at least one Image of otherPic is considered as contained.

Parameters:  otherPic[¶](#tts.testModule.multimedia.dataElements.Image.Image.Contains.otherPic "Permalink to this definition")  
The searched image or an iterator over multiple searched images

colorTolerance : int[¶](#tts.testModule.multimedia.dataElements.Image.Image.Contains.colorTolerance "Permalink to this definition")  
The maximum allowed color difference (0…255) of a pixel to be considered as equal.

tolerance : float[¶](#tts.testModule.multimedia.dataElements.Image.Image.Contains.tolerance "Permalink to this definition")  
Tolerance in percent (from 0.0 to 1.0) that indicates how much the image is allowed to differ from a potential match. A higher value will make the search more tolerant. Defaults to 0.

Returns:  True if otherPic is contained in this image, else False

Return type:  bool

FindImage(*[image](#tts.testModule.multimedia.dataElements.Image.Image.FindImage.image "tts.testModule.multimedia.dataElements.Image.Image.FindImage.image (Python parameter) — The image that will be searched for in the larger image.")*, *[maxOccurrences](#tts.testModule.multimedia.dataElements.Image.Image.FindImage.maxOccurrences "tts.testModule.multimedia.dataElements.Image.Image.FindImage.maxOccurrences (Python parameter) — The maximum number of occurrences to find.")=`100`*, *[threshold](#tts.testModule.multimedia.dataElements.Image.Image.FindImage.threshold "tts.testModule.multimedia.dataElements.Image.Image.FindImage.threshold (Python parameter) — The similarity threshold in percent from 0 to 1 (Defaults to 0.9999 to avoid rounding errors). Determines how similar an image must be to be considered a match.")=`0.9999`*)[¶](#tts.testModule.multimedia.dataElements.Image.Image.FindImage "Link to this definition")  
Searches for a sub-image in this image. Returns a list of matches, containing information about the position of the sub-image.

Parameters:  image[¶](#tts.testModule.multimedia.dataElements.Image.Image.FindImage.image "Permalink to this definition")  
The image that will be searched for in the larger image. Its dimensions must not be greater than the source image.

maxOccurrences : int[¶](#tts.testModule.multimedia.dataElements.Image.Image.FindImage.maxOccurrences "Permalink to this definition")  
The maximum number of occurrences to find. Set to 0 to find all occurrences. Limiting this number can improve performance when using low thresholds. Defaults to 100.

threshold : float[¶](#tts.testModule.multimedia.dataElements.Image.Image.FindImage.threshold "Permalink to this definition")  
The similarity threshold in percent from 0 to 1 (Defaults to 0.9999 to avoid rounding errors). Determines how similar an image must be to be considered a match. A threshold of 1 will search only for perfect matches. Values of 0.9 and above will usually find closely matching regions in the image while ignoring noise. Note that a too low threshold might lead to wrong matches.

Returns:  List of image matches sorted by their position.

Return type:  [ImageMatchList](#tts.testModule.multimedia.dataElements.MatchObjects.ImageMatchList "tts.testModule.multimedia.dataElements.MatchObjects.ImageMatchList (Python class) — This is a list containing ImageMatch objects. It can be used like a normal python list object, but offers some additional features.")

FindImages(*[images](#tts.testModule.multimedia.dataElements.Image.Image.FindImages.images "tts.testModule.multimedia.dataElements.Image.Image.FindImages.images (Python parameter) — The images to be searched for in the larger image.")*, *[maxOccurrences](#tts.testModule.multimedia.dataElements.Image.Image.FindImages.maxOccurrences "tts.testModule.multimedia.dataElements.Image.Image.FindImages.maxOccurrences (Python parameter) — The maximum number of occurrences to find.")=`100`*, *[threshold](#tts.testModule.multimedia.dataElements.Image.Image.FindImages.threshold "tts.testModule.multimedia.dataElements.Image.Image.FindImages.threshold (Python parameter) — The similarity threshold in percent from 0 to 1 (Defaults to 0.9999 to avoid rounding errors). Determines how similar an image must be to be considered a match.")=`0.9999`*)[¶](#tts.testModule.multimedia.dataElements.Image.Image.FindImages "Link to this definition")  
Searches for a list of sub-images in this image. Returns a list of matches, containing information about the position of the sub-image.

Parameters:  images[¶](#tts.testModule.multimedia.dataElements.Image.Image.FindImages.images "Permalink to this definition")  
The images to be searched for in the larger image. Their dimensions must not be greater than the source image.

maxOccurrences : int[¶](#tts.testModule.multimedia.dataElements.Image.Image.FindImages.maxOccurrences "Permalink to this definition")  
The maximum number of occurrences to find. Set to 0 to find all occurrences. Limiting this number can improve performance when using low thresholds. Defaults to 100.

threshold : float[¶](#tts.testModule.multimedia.dataElements.Image.Image.FindImages.threshold "Permalink to this definition")  
The similarity threshold in percent from 0 to 1 (Defaults to 0.9999 to avoid rounding errors). Determines how similar an image must be to be considered a match. A threshold of 1 will search only for perfect matches. Values of 0.9 and above will usually find closely matching regions in the image while ignoring noise. Note that a too low threshold might lead to wrong matches.

Returns:  List of image matches sorted by their position.

Return type:  [ImageMatchList](#tts.testModule.multimedia.dataElements.MatchObjects.ImageMatchList "tts.testModule.multimedia.dataElements.MatchObjects.ImageMatchList (Python class) — This is a list containing ImageMatch objects. It can be used like a normal python list object, but offers some additional features.")

FindImageByFeatures(*[image](#tts.testModule.multimedia.dataElements.Image.Image.FindImageByFeatures.image "tts.testModule.multimedia.dataElements.Image.Image.FindImageByFeatures.image (Python parameter) — The sub-image that will be searched for within the larger image.")*, *[threshold](#tts.testModule.multimedia.dataElements.Image.Image.FindImageByFeatures.threshold "tts.testModule.multimedia.dataElements.Image.Image.FindImageByFeatures.threshold (Python parameter) — The minimum confidence that a match must have to be considered a match. Values are in percent from 0 to 1 (defaults to 0.2).")=`0.2`*)[¶](#tts.testModule.multimedia.dataElements.Image.Image.FindImageByFeatures "Link to this definition")  
Searches for a sub-image within this image. This method does not compare every pixel. Instead, it looks for distinct features in both images and tries to match them. This makes it invariant to scale, rotation, color, and perspective. The features are detected by analyzing black/white color gradients. Therefore, complex patterns with hard edges between light and dark areas will be found best. This also means that an image with inverted colors will not be found. Dark areas must still be dark, and light areas light between source image and sub-image. Note that execution time will increase linearly with the number of sub-image occurences in the scene. E.g. if your scene contains the searched image twice then it will take twice as long to find all occurences compared to a scene where the sub-image occurs only once.

Parameters:  image[¶](#tts.testModule.multimedia.dataElements.Image.Image.FindImageByFeatures.image "Permalink to this definition")  
The sub-image that will be searched for within the larger image.

threshold : float[¶](#tts.testModule.multimedia.dataElements.Image.Image.FindImageByFeatures.threshold "Permalink to this definition")  
The minimum confidence that a match must have to be considered a match. Values are in percent from 0 to 1 (defaults to 0.2). Higher values will filter out bad results but will also make the search less invariant to changes regarding scale, rotation, color, and perspective.

Returns:  A list of ImageMatches.

Return type:  [ImageMatchList](#tts.testModule.multimedia.dataElements.MatchObjects.ImageMatchList "tts.testModule.multimedia.dataElements.MatchObjects.ImageMatchList (Python class) — This is a list containing ImageMatch objects. It can be used like a normal python list object, but offers some additional features.")

FindObjectByColor(*[color](#tts.testModule.multimedia.dataElements.Image.Image.FindObjectByColor.color "tts.testModule.multimedia.dataElements.Image.Image.FindObjectByColor.color (Python parameter) — A color string.")*, *[tolH](#tts.testModule.multimedia.dataElements.Image.Image.FindObjectByColor.tolH "tts.testModule.multimedia.dataElements.Image.Image.FindObjectByColor.tolH (Python parameter) — The tolerance applied to the expected hue.")*, *[tolS](#tts.testModule.multimedia.dataElements.Image.Image.FindObjectByColor.tolS "tts.testModule.multimedia.dataElements.Image.Image.FindObjectByColor.tolS (Python parameter) — The tolerance applied to the expected saturation.")*, *[tolV](#tts.testModule.multimedia.dataElements.Image.Image.FindObjectByColor.tolV "tts.testModule.multimedia.dataElements.Image.Image.FindObjectByColor.tolV (Python parameter) — The tolerance applied to the expected value.")*, *[kernelSize](#tts.testModule.multimedia.dataElements.Image.Image.FindObjectByColor.kernelSize "tts.testModule.multimedia.dataElements.Image.Image.FindObjectByColor.kernelSize (Python parameter) — The size of the kernel that is used to connect separated pixel areas to one object (dilation).")=`5`*)[¶](#tts.testModule.multimedia.dataElements.Image.Image.FindObjectByColor "Link to this definition")  
Searches for objects with a given color (Color Detection). After applying a color filter, a dilation step connects identified pixel areas that lie within a distance of kernelSize. Each resulting pixel area will be represented by an [`ImageMatch`](#tts.testModule.multimedia.dataElements.MatchObjects.ImageMatch "tts.testModule.multimedia.dataElements.MatchObjects.ImageMatch (Python class) — Represents an image match.") (rectangular area) of the returned `MatchList`.

The color filter is applied in HSV color schema. Therefore, the tolerances of the color filter must be provided in HSV schema.

Provided HSV parameters (tolH, tolS, tolV, color) must match the following conditions:

- *Hue* is an integer between 0 and 180 and represents the position (in 2 degree steps) on the color circle. 180 corresponds to 360 degrees or a full circle and therefore is semantically equal to 0. (Please note: Some graphic programs provide different value ranges from 0 to 255 or from 0 to 360.)

- *Saturation* is an integer between 0 and 255.

- *Value* is an integer between 0 and 255

Parameters:  color : str[¶](#tts.testModule.multimedia.dataElements.Image.Image.FindObjectByColor.color "Permalink to this definition")  
A color string. Either an RGB hex string (e.g. ‘#FF0000’ for red) or an HSV color string in the form ‘hsv(hue, saturation, value)’ (e.g. ‘hsv(120, 255, 255)’ for blue).

tolH : tuple[int, int] | int[¶](#tts.testModule.multimedia.dataElements.Image.Image.FindObjectByColor.tolH "Permalink to this definition")  
The tolerance applied to the expected hue. The value can either be a tuple of integers for defining an asymmetric tolerance window (Hue(color) - tolH[0], Hue(color) + tolH[1]), or an integer for defining a symmetric tolerance window (Hue(color) - tolH, Hue(color) + tolH).

tolS : tuple[int, int] | int[¶](#tts.testModule.multimedia.dataElements.Image.Image.FindObjectByColor.tolS "Permalink to this definition")  
The tolerance applied to the expected saturation. The value can either be a tuple of integers for defining an asymmetric tolerance window (Saturation(color) - tolS[0], Saturation(color) + tolS[1]), or an integer for defining a symmetric tolerance window (Saturation(color) - tolS, Saturation(color) + tolS).

tolV : tuple[int, int] | int[¶](#tts.testModule.multimedia.dataElements.Image.Image.FindObjectByColor.tolV "Permalink to this definition")  
The tolerance applied to the expected value. It can either be a tuple of integers for defining an asymmetric tolerance window (Value(color) - tolV[0], Value(color) + tolV[1]), or an integer for defining a symmetric tolerance window (Value(color) - tolV, Value(color) + tolV).

kernelSize : int[¶](#tts.testModule.multimedia.dataElements.Image.Image.FindObjectByColor.kernelSize "Permalink to this definition")  
The size of the kernel that is used to connect separated pixel areas to one object (dilation). A larger kernel connects pixel areas that have more distance to each other. Odd numbers must be provided! Defaults to 5.

Returns:  A list of ImageMatches.

Return type:  [ImageMatchList](#tts.testModule.multimedia.dataElements.MatchObjects.ImageMatchList "tts.testModule.multimedia.dataElements.MatchObjects.ImageMatchList (Python class) — This is a list containing ImageMatch objects. It can be used like a normal python list object, but offers some additional features.")

FindWord(*[wordList](#tts.testModule.multimedia.dataElements.Image.Image.FindWord.wordList "tts.testModule.multimedia.dataElements.Image.Image.FindWord.wordList (Python parameter) — (List of) desired word(s).")=`None`*, *[maxOccurrences](#tts.testModule.multimedia.dataElements.Image.Image.FindWord.maxOccurrences "tts.testModule.multimedia.dataElements.Image.Image.FindWord.maxOccurrences (Python parameter) — Maximum number of matches to be found.")=`0`*, *[langList](#tts.testModule.multimedia.dataElements.Image.Image.FindWord.langList "tts.testModule.multimedia.dataElements.Image.Image.FindWord.langList (Python parameter) — List of language modules to use for text recognition. ecu.test comes with a preset list of available languages.")=`None`*, *[ocrDataPath](#tts.testModule.multimedia.dataElements.Image.Image.FindWord.ocrDataPath "tts.testModule.multimedia.dataElements.Image.Image.FindWord.ocrDataPath (Python parameter) — The path to the directory containing your custom tesseract language files.")=`None`*, *[isRegex](#tts.testModule.multimedia.dataElements.Image.Image.FindWord.isRegex "tts.testModule.multimedia.dataElements.Image.Image.FindWord.isRegex (Python parameter) — Set True to use regular expression as search strings.")=`False`*, *[threshold](#tts.testModule.multimedia.dataElements.Image.Image.FindWord.threshold "tts.testModule.multimedia.dataElements.Image.Image.FindWord.threshold (Python parameter) — Only results with a confidence larger than this threshold will be returned (between 0.0 and 1.0).")=`0.4`*)[¶](#tts.testModule.multimedia.dataElements.Image.Image.FindWord "Link to this definition")  
Find single words in an image. Returns a list of matches containing information about the position of the desired word. This method applies various preprocessing steps, such as automatically inverting the colors to ensure the background is always white.

Parameters:  wordList : str | list[str][¶](#tts.testModule.multimedia.dataElements.Image.Image.FindWord.wordList "Permalink to this definition")  
(List of) desired word(s).

maxOccurrences : int[¶](#tts.testModule.multimedia.dataElements.Image.Image.FindWord.maxOccurrences "Permalink to this definition")  
Maximum number of matches to be found. Use this, if you expect a string to occur exactly n times. The analysis will be stopped as soon as this number is reached. Can improve performance. If the value is 0, the full image will be analyzed.

langList : list[str][¶](#tts.testModule.multimedia.dataElements.Image.Image.FindWord.langList "Permalink to this definition")  
List of language modules to use for text recognition. ecu.test comes with a preset list of available languages. For example use [‘eng’, ‘deu’] to recognize english and german text (in that order). The full list of default languages can be seen in the test configuration window. Additional language modules are available online, please refer to the tesseract documentation to download new language packs. If no language is specified then the languages from the currently active test configuration will be used. Note that if your test configuration contains more than one media node, the first node (in alphabetical order) will be used to load the ocr data.

ocrDataPath : str | None[¶](#tts.testModule.multimedia.dataElements.Image.Image.FindWord.ocrDataPath "Permalink to this definition")  
The path to the directory containing your custom tesseract language files. If specified, all \*.traineddata files present in that directory will be added to the default languages as valid inputs for the langList parameter. Leave blank to use ecu.test’s default directory with its preset range of languages.

isRegex : bool[¶](#tts.testModule.multimedia.dataElements.Image.Image.FindWord.isRegex "Permalink to this definition")  
Set True to use regular expression as search strings.

threshold : float[¶](#tts.testModule.multimedia.dataElements.Image.Image.FindWord.threshold "Permalink to this definition")  
Only results with a confidence larger than this threshold will be returned (between 0.0 and 1.0).

Returns:  List of matches that contain information about the text position sorted by their position.

Return type:  [TextMatchList](#tts.testModule.multimedia.dataElements.MatchObjects.TextMatchList "tts.testModule.multimedia.dataElements.MatchObjects.TextMatchList (Python class) — This is a list containing TextMatch objects. It can be used like a normal python list object, but offers some additional features.")

FindText(*[searchStrings](#tts.testModule.multimedia.dataElements.Image.Image.FindText.searchStrings "tts.testModule.multimedia.dataElements.Image.Image.FindText.searchStrings (Python parameter) — List of desired text values.")=`None`*, *[maxOccurrences](#tts.testModule.multimedia.dataElements.Image.Image.FindText.maxOccurrences "tts.testModule.multimedia.dataElements.Image.Image.FindText.maxOccurrences (Python parameter) — Maximum number of matches to be found.")=`0`*, *[langList](#tts.testModule.multimedia.dataElements.Image.Image.FindText.langList "tts.testModule.multimedia.dataElements.Image.Image.FindText.langList (Python parameter) — List of language modules to use for text recognition. ecu.test comes with a preset list of available languages.")=`None`*, *[ocrDataPath](#tts.testModule.multimedia.dataElements.Image.Image.FindText.ocrDataPath "tts.testModule.multimedia.dataElements.Image.Image.FindText.ocrDataPath (Python parameter) — The path to the directory containing your custom tesseract language files.")=`None`*, *[isRegex](#tts.testModule.multimedia.dataElements.Image.Image.FindText.isRegex "tts.testModule.multimedia.dataElements.Image.Image.FindText.isRegex (Python parameter) — Set True to use regular expression as search strings.")=`False`*, *[strict](#tts.testModule.multimedia.dataElements.Image.Image.FindText.strict "tts.testModule.multimedia.dataElements.Image.Image.FindText.strict (Python parameter) — If False, this method will return all text matches that contain the search string.")=`False`*, *[threshold](#tts.testModule.multimedia.dataElements.Image.Image.FindText.threshold "tts.testModule.multimedia.dataElements.Image.Image.FindText.threshold (Python parameter) — Only results with a confidence larger than this threshold will be returned (between 0.0 and 1.0).")=`0.4`*)[¶](#tts.testModule.multimedia.dataElements.Image.Image.FindText "Link to this definition")  
Find a text in an image. Returns a list of matches containing information about the position of the desired text. This method applies various preprocessing steps, such as automatically inverting the colors to ensure the background is always white. See [`RecognizeText()`](#tts.testModule.multimedia.dataElements.Image.Image.RecognizeText "tts.testModule.multimedia.dataElements.Image.Image.RecognizeText (Python method) — Tries to recognize text inside the image. This method does not apply any preprocessing to the image. To achieve best results you should ensure that the image uses black text on white background. You can use one of the builtin ImageFilters to manipulate your image (see ImageFiltersApi). Alternatively see FindText() for a more sophisticated approach that applies automatic preprocessing.") for a more basic approach without any preprocessing.

Parameters:  searchStrings : list[str][¶](#tts.testModule.multimedia.dataElements.Image.Image.FindText.searchStrings "Permalink to this definition")  
List of desired text values.

maxOccurrences : int[¶](#tts.testModule.multimedia.dataElements.Image.Image.FindText.maxOccurrences "Permalink to this definition")  
Maximum number of matches to be found. Use this, if you expect a string to occur exactly n times. The analysis will be stopped as soon as this number is reached. Can improve performance. If the value is 0, the full image will be analyzed.

langList : list[str][¶](#tts.testModule.multimedia.dataElements.Image.Image.FindText.langList "Permalink to this definition")  
List of language modules to use for text recognition. ecu.test comes with a preset list of available languages. For example use [‘eng’, ‘deu’] to recognize english and german text (in that order). The full list of default languages can be seen in the test configuration window. Additional language modules are available online, please refer to the tesseract documentation to download new language packs. If no language is specified then the languages from the currently active test configuration will be used. Note that if your test configuration contains more than one media node, the first node (in alphabetical order) will be used to load the ocr data.

ocrDataPath : str | None[¶](#tts.testModule.multimedia.dataElements.Image.Image.FindText.ocrDataPath "Permalink to this definition")  
The path to the directory containing your custom tesseract language files. If specified, all \*.traineddata files present in that directory will be added to the default languages as valid inputs for the langList parameter. Leave blank to use ecu.test’s default directory with its preset range of languages.

isRegex : bool[¶](#tts.testModule.multimedia.dataElements.Image.Image.FindText.isRegex "Permalink to this definition")  
Set True to use regular expression as search strings.

strict : bool[¶](#tts.testModule.multimedia.dataElements.Image.Image.FindText.strict "Permalink to this definition")  
If False, this method will return all text matches that contain the search string. If True, it will only return results that exactly match the search string.

threshold : float[¶](#tts.testModule.multimedia.dataElements.Image.Image.FindText.threshold "Permalink to this definition")  
Only results with a confidence larger than this threshold will be returned (between 0.0 and 1.0).

Returns:  List of matches that contain information about the text position sorted by their position.

Return type:  [TextMatchList](#tts.testModule.multimedia.dataElements.MatchObjects.TextMatchList "tts.testModule.multimedia.dataElements.MatchObjects.TextMatchList (Python class) — This is a list containing TextMatch objects. It can be used like a normal python list object, but offers some additional features.")

FindBestTextMatches(*[searchStrings](#tts.testModule.multimedia.dataElements.Image.Image.FindBestTextMatches.searchStrings "tts.testModule.multimedia.dataElements.Image.Image.FindBestTextMatches.searchStrings (Python parameter) — List with texts to find")=`None`*, *[maxOccurrences](#tts.testModule.multimedia.dataElements.Image.Image.FindBestTextMatches.maxOccurrences "tts.testModule.multimedia.dataElements.Image.Image.FindBestTextMatches.maxOccurrences (Python parameter) — Limits the number of matches to n items.")=`100`*, *[langList](#tts.testModule.multimedia.dataElements.Image.Image.FindBestTextMatches.langList "tts.testModule.multimedia.dataElements.Image.Image.FindBestTextMatches.langList (Python parameter) — List of language modules to use for text recognition. ecu.test comes with a preset list of available languages.")=`None`*, *[ocrDataPath](#tts.testModule.multimedia.dataElements.Image.Image.FindBestTextMatches.ocrDataPath "tts.testModule.multimedia.dataElements.Image.Image.FindBestTextMatches.ocrDataPath (Python parameter) — The path to the directory containing your custom tesseract language files.")=`None`*, *[isRegex](#tts.testModule.multimedia.dataElements.Image.Image.FindBestTextMatches.isRegex "tts.testModule.multimedia.dataElements.Image.Image.FindBestTextMatches.isRegex (Python parameter) — Set True to use regular expression as search strings.")=`False`*)[¶](#tts.testModule.multimedia.dataElements.Image.Image.FindBestTextMatches "Link to this definition")  
Finds texts in an image. Returns a list of matches sorted by the confidence.

Parameters:  searchStrings : list[str][¶](#tts.testModule.multimedia.dataElements.Image.Image.FindBestTextMatches.searchStrings "Permalink to this definition")  
List with texts to find

maxOccurrences : int[¶](#tts.testModule.multimedia.dataElements.Image.Image.FindBestTextMatches.maxOccurrences "Permalink to this definition")  
Limits the number of matches to n items.

langList : list[str][¶](#tts.testModule.multimedia.dataElements.Image.Image.FindBestTextMatches.langList "Permalink to this definition")  
List of language modules to use for text recognition. ecu.test comes with a preset list of available languages. For example use [‘eng’, ‘deu’] to recognize english and german text (in that order). The full list of default languages can be seen in the test configuration window. Additional language modules are available online, please refer to the tesseract documentation to download new language packs. If no language is specified then the languages from the currently active test configuration will be used. Note that if your test configuration contains more than one media node, the first node (in alphabetical order) will be used to load the ocr data.

ocrDataPath : str | None[¶](#tts.testModule.multimedia.dataElements.Image.Image.FindBestTextMatches.ocrDataPath "Permalink to this definition")  
The path to the directory containing your custom tesseract language files. If specified, all \*.traineddata files present in that directory will be added to the default languages as valid inputs for the langList parameter. Leave blank to use ecu.test’s default directory with its preset range of languages.

isRegex : bool[¶](#tts.testModule.multimedia.dataElements.Image.Image.FindBestTextMatches.isRegex "Permalink to this definition")  
Set True to use regular expression as search strings.

Returns:  List of matches that contain information about the text position sorted by their confidence.

Return type:  [TextMatchList](#tts.testModule.multimedia.dataElements.MatchObjects.TextMatchList "tts.testModule.multimedia.dataElements.MatchObjects.TextMatchList (Python class) — This is a list containing TextMatch objects. It can be used like a normal python list object, but offers some additional features.")

RecognizeText(*[langList](#tts.testModule.multimedia.dataElements.Image.Image.RecognizeText.langList "tts.testModule.multimedia.dataElements.Image.Image.RecognizeText.langList (Python parameter) — List of language modules to use for text recognition. ecu.test comes with a preset list of available languages.")=`None`*, *[ocrDataPath](#tts.testModule.multimedia.dataElements.Image.Image.RecognizeText.ocrDataPath "tts.testModule.multimedia.dataElements.Image.Image.RecognizeText.ocrDataPath (Python parameter) — The path to the directory containing your custom tesseract language files.")=`None`*)[¶](#tts.testModule.multimedia.dataElements.Image.Image.RecognizeText "Link to this definition")  
Tries to recognize text inside the image. This method does not apply any preprocessing to the image. To achieve best results you should ensure that the image uses black text on white background. You can use one of the builtin ImageFilters to manipulate your image (see [`ImageFiltersApi`](api.md#tts.testModule.multimedia.api.MultimediaApi.ImageFiltersApi "tts.testModule.multimedia.api.MultimediaApi.ImageFiltersApi (Python class) — Provides access to image filters. Filters are grouped into the two namespaces default and user. The following filters are provided by ecu.test out of the box:")). Alternatively see [`FindText()`](#tts.testModule.multimedia.dataElements.Image.Image.FindText "tts.testModule.multimedia.dataElements.Image.Image.FindText (Python method) — Find a text in an image. Returns a list of matches containing information about the position of the desired text. This method applies various preprocessing steps, such as automatically inverting the colors to ensure the background is always white. See RecognizeText() for a more basic approach without any preprocessing.") for a more sophisticated approach that applies automatic preprocessing.

Parameters:  langList : list\<str\>[¶](#tts.testModule.multimedia.dataElements.Image.Image.RecognizeText.langList "Permalink to this definition")  
List of language modules to use for text recognition. ecu.test comes with a preset list of available languages. For example use [‘eng’, ‘deu’] to recognize english and german text (in that order). The full list of default languages can be seen in the test configuration window. Additional language modules are available online, please refer to the tesseract documentation to download new language packs. If no language is specified then the languages from the currently active test configuration will be used. Note that if your test configuration contains more than one media node, the first node (in alphabetical order) will be used to load the ocr data.

ocrDataPath : str[¶](#tts.testModule.multimedia.dataElements.Image.Image.RecognizeText.ocrDataPath "Permalink to this definition")  
The path to the directory containing your custom tesseract language files. If specified, all \*.traineddata files present in that directory will be added to the default languages as valid inputs for the langList parameter. Leave blank to use ecu.test’s default directory with its preset range of languages.

Returns:  The recognized text

Return type:  str

EmbedInReport(*[embedInReport](#tts.testModule.multimedia.dataElements.Image.Image.EmbedInReport.embedInReport "tts.testModule.multimedia.dataElements.Image.Image.EmbedInReport.embedInReport (Python parameter) — True if image should be saved in report file")=`True`*)[¶](#tts.testModule.multimedia.dataElements.Image.Image.EmbedInReport "Link to this definition")  
If activated, the image is embedded in the TRF report instead of creating a referenced image file in report directory. Warning: This can considerably increase the file size of the report.

Parameters:  embedInReport : bool[¶](#tts.testModule.multimedia.dataElements.Image.Image.EmbedInReport.embedInReport "Permalink to this definition")  
True if image should be saved in report file

## Mask[¶](#mask "Link to this heading")

*class* Mask[¶](#tts.testModule.multimedia.dataElements.Mask.Mask "Link to this definition")  
Parameters:  path  
The mask file to load

Creates a new Mask object from a given file.

Example usage: `Mask("path/to/file.mask")`

Apply(*[image](#tts.testModule.multimedia.dataElements.Mask.Mask.Apply.image "tts.testModule.multimedia.dataElements.Mask.Mask.Apply.image (Python parameter) — The image to be masked")*)[¶](#tts.testModule.multimedia.dataElements.Mask.Mask.Apply "Link to this definition")  
Crops an image using the region defined by this mask.

Parameters:  image[¶](#tts.testModule.multimedia.dataElements.Mask.Mask.Apply.image "Permalink to this definition")  
The image to be masked

Returns:  A new cropped image

Return type:  [`Image`](#tts.testModule.multimedia.dataElements.Image.Image "tts.testModule.multimedia.dataElements.Image.Image (Python class) — Represents an image.")

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

Save(*[path](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.Save.path "tts.traceRecording.parser.formats.video.VideoRecording.Frame.Save.path (Python parameter) — Path where the image file should be saved.")*)[¶](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.Save "Link to this definition")  
Saves the image as file.

Parameters:  path : str[¶](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.Save.path "Permalink to this definition")  
Path where the image file should be saved. The path must include the file extension. A relative path is resolved relative to the workspace path.

Crop(*[x](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.Crop.x "tts.traceRecording.parser.formats.video.VideoRecording.Frame.Crop.x (Python parameter) — x position of the upper left corner of the cutout")*, *[y](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.Crop.y "tts.traceRecording.parser.formats.video.VideoRecording.Frame.Crop.y (Python parameter) — y position of the upper left corner of the cutout")*, *[width](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.Crop.width "tts.traceRecording.parser.formats.video.VideoRecording.Frame.Crop.width (Python parameter) — Width of the cutout")*, *[height](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.Crop.height "tts.traceRecording.parser.formats.video.VideoRecording.Frame.Crop.height (Python parameter) — Height of the cutout")*)[¶](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.Crop "Link to this definition")  
Crops the image.

Parameters:  x : int[¶](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.Crop.x "Permalink to this definition")  
x position of the upper left corner of the cutout

y : int[¶](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.Crop.y "Permalink to this definition")  
y position of the upper left corner of the cutout

width : int[¶](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.Crop.width "Permalink to this definition")  
Width of the cutout

height : int[¶](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.Crop.height "Permalink to this definition")  
Height of the cutout

Returns:  Cropped image

Return type:  [`Image`](apireport.md#tts.core.report.db.Image.Image "tts.core.report.db.Image.Image (Python class) — Represents a ReportItem-Image.")

Contains(*[otherPic](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.Contains.otherPic "tts.traceRecording.parser.formats.video.VideoRecording.Frame.Contains.otherPic (Python parameter) — The searched image or an iterator over multiple searched images")*, *[colorTolerance](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.Contains.colorTolerance "tts.traceRecording.parser.formats.video.VideoRecording.Frame.Contains.colorTolerance (Python parameter) — The maximum allowed color difference (0...255) of a pixel to be considered as equal.")=`0`*, *[tolerance](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.Contains.tolerance "tts.traceRecording.parser.formats.video.VideoRecording.Frame.Contains.tolerance (Python parameter) — Tolerance in percent (from 0.0 to 1.0) that indicates how much the image is allowed to differ from a potential match.")=`0`*)[¶](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.Contains "Link to this definition")  
Checks if otherPic is contained in this image.

At first, the closest matching section to otherPic is determined. Then, the similarity between the cropped image and otherPic is calculated. If the similarity is within the specified tolerance then True is returned. Otherwise, False.

If otherPic is an iterable object of Images, this method returns True if at least one Image of otherPic is considered as contained.

Parameters:  otherPic[¶](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.Contains.otherPic "Permalink to this definition")  
The searched image or an iterator over multiple searched images

colorTolerance : int[¶](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.Contains.colorTolerance "Permalink to this definition")  
The maximum allowed color difference (0…255) of a pixel to be considered as equal.

tolerance : float[¶](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.Contains.tolerance "Permalink to this definition")  
Tolerance in percent (from 0.0 to 1.0) that indicates how much the image is allowed to differ from a potential match. A higher value will make the search more tolerant. Defaults to 0.

Returns:  True if otherPic is contained in this image, else False

Return type:  bool

IsEqual(*[otherPic](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.IsEqual.otherPic "tts.traceRecording.parser.formats.video.VideoRecording.Frame.IsEqual.otherPic (Python parameter) — The image to compare.")*, *[colorTolerance](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.IsEqual.colorTolerance "tts.traceRecording.parser.formats.video.VideoRecording.Frame.IsEqual.colorTolerance (Python parameter) — The maximum allowed color difference (0...255) of a pixel to be considered as equal.")=`0`*, *[tolerance](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.IsEqual.tolerance "tts.traceRecording.parser.formats.video.VideoRecording.Frame.IsEqual.tolerance (Python parameter) — Tolerance in percent (from 0.0 to 1.0) that indicates how much the images are allowed to differ.")=`0`*)[¶](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.IsEqual "Link to this definition")  
Determines via [`GetSimilarity()`](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.GetSimilarity "tts.traceRecording.parser.formats.video.VideoRecording.Frame.GetSimilarity (Python method) — Calculates the similarity between two images as a value between 0.0 and 1.0. The similarity can be calculated as follows:") the similarity to otherPic. If the similarity is within the specified tolerance then True is returned. Otherwise, False.

Parameters:  otherPic[¶](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.IsEqual.otherPic "Permalink to this definition")  
The image to compare. The image needs to have the same size as the image it is compared with.

colorTolerance : int[¶](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.IsEqual.colorTolerance "Permalink to this definition")  
The maximum allowed color difference (0…255) of a pixel to be considered as equal.

tolerance : float[¶](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.IsEqual.tolerance "Permalink to this definition")  
Tolerance in percent (from 0.0 to 1.0) that indicates how much the images are allowed to differ. A higher value will make the comparison more tolerant. Defaults to 0.

Returns:  True if the images are equal, else False

Return type:  bool

GetSimilarity(*[otherPic](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.GetSimilarity.otherPic "tts.traceRecording.parser.formats.video.VideoRecording.Frame.GetSimilarity.otherPic (Python parameter) — Image or an iterable of Images to compare.")*, *[colorTolerance](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.GetSimilarity.colorTolerance "tts.traceRecording.parser.formats.video.VideoRecording.Frame.GetSimilarity.colorTolerance (Python parameter) — The maximum allowed color difference (0...255) of a pixel to be considered as equal")=`0`*)[¶](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.GetSimilarity "Link to this definition")  
Calculates the similarity between two images as a value between 0.0 and 1.0. The similarity can be calculated as follows:

- Calculation of the absolute difference for each color for each pixel of the two images

- If the difference of the color is less than or equal to parameter colorTolerance, the color is considered as equal

- If otherPic is a transparent image, then all pixels that are not completely visible are considered equal

- The return value is the quotient of all equal pixel colors divided by the number of all pixel colors

If otherPic is an iterable object of Images, the highest value over all calculated similarities is returned.

Parameters:  otherPic[¶](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.GetSimilarity.otherPic "Permalink to this definition")  
Image or an iterable of Images to compare. The image(s) need to have the same size as the image they are compared with.

colorTolerance : int[¶](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.GetSimilarity.colorTolerance "Permalink to this definition")  
The maximum allowed color difference (0…255) of a pixel to be considered as equal

Returns:  Similarity in range 0.0 to 1.0

Return type:  float

RecognizeText(*[langList](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.RecognizeText.langList "tts.traceRecording.parser.formats.video.VideoRecording.Frame.RecognizeText.langList (Python parameter) — List of language modules to use for text recognition. ecu.test comes with a preset list of available languages.")=`None`*, *[ocrDataPath](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.RecognizeText.ocrDataPath "tts.traceRecording.parser.formats.video.VideoRecording.Frame.RecognizeText.ocrDataPath (Python parameter) — The path to the directory containing your custom tesseract language files.")=`None`*)[¶](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.RecognizeText "Link to this definition")  
Tries to recognize text inside the image. This method does not apply any preprocessing to the image. To achieve best results you should ensure that the image uses black text on white background. You can use one of the builtin ImageFilters to manipulate your image (see [`ImageFiltersApi`](api.md#tts.testModule.multimedia.api.MultimediaApi.ImageFiltersApi "tts.testModule.multimedia.api.MultimediaApi.ImageFiltersApi (Python class) — Provides access to image filters. Filters are grouped into the two namespaces default and user. The following filters are provided by ecu.test out of the box:")). Alternatively see [`FindText()`](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindText "tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindText (Python method) — Find a text in an image. Returns a list of matches containing information about the position of the desired text. This method applies various preprocessing steps, such as automatically inverting the colors to ensure the background is always white. See RecognizeText() for a more basic approach without any preprocessing.") for a more sophisticated approach that applies automatic preprocessing.

Parameters:  langList : list\<str\>[¶](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.RecognizeText.langList "Permalink to this definition")  
List of language modules to use for text recognition. ecu.test comes with a preset list of available languages. For example use [‘eng’, ‘deu’] to recognize english and german text (in that order). The full list of default languages can be seen in the test configuration window. Additional language modules are available online, please refer to the tesseract documentation to download new language packs. If no language is specified then the languages from the currently active test configuration will be used. Note that if your test configuration contains more than one media node, the first node (in alphabetical order) will be used to load the ocr data.

ocrDataPath : str[¶](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.RecognizeText.ocrDataPath "Permalink to this definition")  
The path to the directory containing your custom tesseract language files. If specified, all \*.traineddata files present in that directory will be added to the default languages as valid inputs for the langList parameter. Leave blank to use ecu.test’s default directory with its preset range of languages.

Returns:  The recognized text

Return type:  str

FindWord(*[wordList](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindWord.wordList "tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindWord.wordList (Python parameter) — (List of) desired word(s).")=`None`*, *[maxOccurrences](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindWord.maxOccurrences "tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindWord.maxOccurrences (Python parameter) — Maximum number of matches to be found.")=`0`*, *[langList](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindWord.langList "tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindWord.langList (Python parameter) — List of language modules to use for text recognition. ecu.test comes with a preset list of available languages.")=`None`*, *[ocrDataPath](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindWord.ocrDataPath "tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindWord.ocrDataPath (Python parameter) — The path to the directory containing your custom tesseract language files.")=`None`*, *[isRegex](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindWord.isRegex "tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindWord.isRegex (Python parameter) — Set True to use regular expression as search strings.")=`False`*, *[threshold](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindWord.threshold "tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindWord.threshold (Python parameter) — Only results with a confidence larger than this threshold will be returned (between 0.0 and 1.0).")=`0.4`*)[¶](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindWord "Link to this definition")  
Find single words in an image. Returns a list of matches containing information about the position of the desired word. This method applies various preprocessing steps, such as automatically inverting the colors to ensure the background is always white.

Parameters:  wordList : str | list[str][¶](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindWord.wordList "Permalink to this definition")  
(List of) desired word(s).

maxOccurrences : int[¶](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindWord.maxOccurrences "Permalink to this definition")  
Maximum number of matches to be found. Use this, if you expect a string to occur exactly n times. The analysis will be stopped as soon as this number is reached. Can improve performance. If the value is 0, the full image will be analyzed.

langList : list[str][¶](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindWord.langList "Permalink to this definition")  
List of language modules to use for text recognition. ecu.test comes with a preset list of available languages. For example use [‘eng’, ‘deu’] to recognize english and german text (in that order). The full list of default languages can be seen in the test configuration window. Additional language modules are available online, please refer to the tesseract documentation to download new language packs. If no language is specified then the languages from the currently active test configuration will be used. Note that if your test configuration contains more than one media node, the first node (in alphabetical order) will be used to load the ocr data.

ocrDataPath : str | None[¶](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindWord.ocrDataPath "Permalink to this definition")  
The path to the directory containing your custom tesseract language files. If specified, all \*.traineddata files present in that directory will be added to the default languages as valid inputs for the langList parameter. Leave blank to use ecu.test’s default directory with its preset range of languages.

isRegex : bool[¶](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindWord.isRegex "Permalink to this definition")  
Set True to use regular expression as search strings.

threshold : float[¶](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindWord.threshold "Permalink to this definition")  
Only results with a confidence larger than this threshold will be returned (between 0.0 and 1.0).

Returns:  List of matches that contain information about the text position sorted by their position.

Return type:  [TextMatchList](#tts.testModule.multimedia.dataElements.MatchObjects.TextMatchList "tts.testModule.multimedia.dataElements.MatchObjects.TextMatchList (Python class) — This is a list containing TextMatch objects. It can be used like a normal python list object, but offers some additional features.")

FindText(*[searchStrings](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindText.searchStrings "tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindText.searchStrings (Python parameter) — List of desired text values.")=`None`*, *[maxOccurrences](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindText.maxOccurrences "tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindText.maxOccurrences (Python parameter) — Maximum number of matches to be found.")=`0`*, *[langList](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindText.langList "tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindText.langList (Python parameter) — List of language modules to use for text recognition. ecu.test comes with a preset list of available languages.")=`None`*, *[ocrDataPath](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindText.ocrDataPath "tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindText.ocrDataPath (Python parameter) — The path to the directory containing your custom tesseract language files.")=`None`*, *[isRegex](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindText.isRegex "tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindText.isRegex (Python parameter) — Set True to use regular expression as search strings.")=`False`*, *[strict](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindText.strict "tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindText.strict (Python parameter) — If False, this method will return all text matches that contain the search string.")=`False`*, *[threshold](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindText.threshold "tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindText.threshold (Python parameter) — Only results with a confidence larger than this threshold will be returned (between 0.0 and 1.0).")=`0.4`*)[¶](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindText "Link to this definition")  
Find a text in an image. Returns a list of matches containing information about the position of the desired text. This method applies various preprocessing steps, such as automatically inverting the colors to ensure the background is always white. See [`RecognizeText()`](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.RecognizeText "tts.traceRecording.parser.formats.video.VideoRecording.Frame.RecognizeText (Python method) — Tries to recognize text inside the image. This method does not apply any preprocessing to the image. To achieve best results you should ensure that the image uses black text on white background. You can use one of the builtin ImageFilters to manipulate your image (see ImageFiltersApi). Alternatively see FindText() for a more sophisticated approach that applies automatic preprocessing.") for a more basic approach without any preprocessing.

Parameters:  searchStrings : list[str][¶](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindText.searchStrings "Permalink to this definition")  
List of desired text values.

maxOccurrences : int[¶](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindText.maxOccurrences "Permalink to this definition")  
Maximum number of matches to be found. Use this, if you expect a string to occur exactly n times. The analysis will be stopped as soon as this number is reached. Can improve performance. If the value is 0, the full image will be analyzed.

langList : list[str][¶](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindText.langList "Permalink to this definition")  
List of language modules to use for text recognition. ecu.test comes with a preset list of available languages. For example use [‘eng’, ‘deu’] to recognize english and german text (in that order). The full list of default languages can be seen in the test configuration window. Additional language modules are available online, please refer to the tesseract documentation to download new language packs. If no language is specified then the languages from the currently active test configuration will be used. Note that if your test configuration contains more than one media node, the first node (in alphabetical order) will be used to load the ocr data.

ocrDataPath : str | None[¶](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindText.ocrDataPath "Permalink to this definition")  
The path to the directory containing your custom tesseract language files. If specified, all \*.traineddata files present in that directory will be added to the default languages as valid inputs for the langList parameter. Leave blank to use ecu.test’s default directory with its preset range of languages.

isRegex : bool[¶](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindText.isRegex "Permalink to this definition")  
Set True to use regular expression as search strings.

strict : bool[¶](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindText.strict "Permalink to this definition")  
If False, this method will return all text matches that contain the search string. If True, it will only return results that exactly match the search string.

threshold : float[¶](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindText.threshold "Permalink to this definition")  
Only results with a confidence larger than this threshold will be returned (between 0.0 and 1.0).

Returns:  List of matches that contain information about the text position sorted by their position.

Return type:  [TextMatchList](#tts.testModule.multimedia.dataElements.MatchObjects.TextMatchList "tts.testModule.multimedia.dataElements.MatchObjects.TextMatchList (Python class) — This is a list containing TextMatch objects. It can be used like a normal python list object, but offers some additional features.")

FindImage(*[image](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindImage.image "tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindImage.image (Python parameter) — The image that will be searched for in the larger image.")*, *[maxOccurrences](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindImage.maxOccurrences "tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindImage.maxOccurrences (Python parameter) — The maximum number of occurrences to find.")=`100`*, *[threshold](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindImage.threshold "tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindImage.threshold (Python parameter) — The similarity threshold in percent from 0 to 1 (Defaults to 0.9999 to avoid rounding errors). Determines how similar an image must be to be considered a match.")=`0.9999`*)[¶](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindImage "Link to this definition")  
Searches for a sub-image in this image. Returns a list of matches, containing information about the position of the sub-image.

Parameters:  image[¶](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindImage.image "Permalink to this definition")  
The image that will be searched for in the larger image. Its dimensions must not be greater than the source image.

maxOccurrences : int[¶](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindImage.maxOccurrences "Permalink to this definition")  
The maximum number of occurrences to find. Set to 0 to find all occurrences. Limiting this number can improve performance when using low thresholds. Defaults to 100.

threshold : float[¶](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindImage.threshold "Permalink to this definition")  
The similarity threshold in percent from 0 to 1 (Defaults to 0.9999 to avoid rounding errors). Determines how similar an image must be to be considered a match. A threshold of 1 will search only for perfect matches. Values of 0.9 and above will usually find closely matching regions in the image while ignoring noise. Note that a too low threshold might lead to wrong matches.

Returns:  List of image matches sorted by their position.

Return type:  [ImageMatchList](#tts.testModule.multimedia.dataElements.MatchObjects.ImageMatchList "tts.testModule.multimedia.dataElements.MatchObjects.ImageMatchList (Python class) — This is a list containing ImageMatch objects. It can be used like a normal python list object, but offers some additional features.")

FindImages(*[images](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindImages.images "tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindImages.images (Python parameter) — The images to be searched for in the larger image.")*, *[maxOccurrences](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindImages.maxOccurrences "tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindImages.maxOccurrences (Python parameter) — The maximum number of occurrences to find.")=`100`*, *[threshold](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindImages.threshold "tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindImages.threshold (Python parameter) — The similarity threshold in percent from 0 to 1 (Defaults to 0.9999 to avoid rounding errors). Determines how similar an image must be to be considered a match.")=`0.9999`*)[¶](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindImages "Link to this definition")  
Searches for a list of sub-images in this image. Returns a list of matches, containing information about the position of the sub-image.

Parameters:  images[¶](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindImages.images "Permalink to this definition")  
The images to be searched for in the larger image. Their dimensions must not be greater than the source image.

maxOccurrences : int[¶](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindImages.maxOccurrences "Permalink to this definition")  
The maximum number of occurrences to find. Set to 0 to find all occurrences. Limiting this number can improve performance when using low thresholds. Defaults to 100.

threshold : float[¶](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindImages.threshold "Permalink to this definition")  
The similarity threshold in percent from 0 to 1 (Defaults to 0.9999 to avoid rounding errors). Determines how similar an image must be to be considered a match. A threshold of 1 will search only for perfect matches. Values of 0.9 and above will usually find closely matching regions in the image while ignoring noise. Note that a too low threshold might lead to wrong matches.

Returns:  List of image matches sorted by their position.

Return type:  [ImageMatchList](#tts.testModule.multimedia.dataElements.MatchObjects.ImageMatchList "tts.testModule.multimedia.dataElements.MatchObjects.ImageMatchList (Python class) — This is a list containing ImageMatch objects. It can be used like a normal python list object, but offers some additional features.")

FindImageByFeatures(*[image](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindImageByFeatures.image "tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindImageByFeatures.image (Python parameter) — The sub-image that will be searched for within the larger image.")*, *[threshold](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindImageByFeatures.threshold "tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindImageByFeatures.threshold (Python parameter) — The minimum confidence that a match must have to be considered a match. Values are in percent from 0 to 1 (defaults to 0.2).")=`0.2`*)[¶](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindImageByFeatures "Link to this definition")  
Searches for a sub-image within this image. This method does not compare every pixel. Instead, it looks for distinct features in both images and tries to match them. This makes it invariant to scale, rotation, color, and perspective. The features are detected by analyzing black/white color gradients. Therefore, complex patterns with hard edges between light and dark areas will be found best. This also means that an image with inverted colors will not be found. Dark areas must still be dark, and light areas light between source image and sub-image. Note that execution time will increase linearly with the number of sub-image occurences in the scene. E.g. if your scene contains the searched image twice then it will take twice as long to find all occurences compared to a scene where the sub-image occurs only once.

Parameters:  image[¶](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindImageByFeatures.image "Permalink to this definition")  
The sub-image that will be searched for within the larger image.

threshold : float[¶](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindImageByFeatures.threshold "Permalink to this definition")  
The minimum confidence that a match must have to be considered a match. Values are in percent from 0 to 1 (defaults to 0.2). Higher values will filter out bad results but will also make the search less invariant to changes regarding scale, rotation, color, and perspective.

Returns:  A list of ImageMatches.

Return type:  [ImageMatchList](#tts.testModule.multimedia.dataElements.MatchObjects.ImageMatchList "tts.testModule.multimedia.dataElements.MatchObjects.ImageMatchList (Python class) — This is a list containing ImageMatch objects. It can be used like a normal python list object, but offers some additional features.")

FindObjectByColor(*[color](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindObjectByColor.color "tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindObjectByColor.color (Python parameter) — A color string.")*, *[tolH](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindObjectByColor.tolH "tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindObjectByColor.tolH (Python parameter) — The tolerance applied to the expected hue.")*, *[tolS](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindObjectByColor.tolS "tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindObjectByColor.tolS (Python parameter) — The tolerance applied to the expected saturation.")*, *[tolV](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindObjectByColor.tolV "tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindObjectByColor.tolV (Python parameter) — The tolerance applied to the expected value.")*, *[kernelSize](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindObjectByColor.kernelSize "tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindObjectByColor.kernelSize (Python parameter) — The size of the kernel that is used to connect separated pixel areas to one object (dilation).")=`5`*)[¶](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindObjectByColor "Link to this definition")  
Searches for objects with a given color (Color Detection). After applying a color filter, a dilation step connects identified pixel areas that lie within a distance of kernelSize. Each resulting pixel area will be represented by an [`ImageMatch`](#tts.testModule.multimedia.dataElements.MatchObjects.ImageMatch "tts.testModule.multimedia.dataElements.MatchObjects.ImageMatch (Python class) — Represents an image match.") (rectangular area) of the returned `MatchList`.

The color filter is applied in HSV color schema. Therefore, the tolerances of the color filter must be provided in HSV schema.

Provided HSV parameters (tolH, tolS, tolV, color) must match the following conditions:

- *Hue* is an integer between 0 and 180 and represents the position (in 2 degree steps) on the color circle. 180 corresponds to 360 degrees or a full circle and therefore is semantically equal to 0. (Please note: Some graphic programs provide different value ranges from 0 to 255 or from 0 to 360.)

- *Saturation* is an integer between 0 and 255.

- *Value* is an integer between 0 and 255

Parameters:  color : str[¶](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindObjectByColor.color "Permalink to this definition")  
A color string. Either an RGB hex string (e.g. ‘#FF0000’ for red) or an HSV color string in the form ‘hsv(hue, saturation, value)’ (e.g. ‘hsv(120, 255, 255)’ for blue).

tolH : tuple[int, int] | int[¶](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindObjectByColor.tolH "Permalink to this definition")  
The tolerance applied to the expected hue. The value can either be a tuple of integers for defining an asymmetric tolerance window (Hue(color) - tolH[0], Hue(color) + tolH[1]), or an integer for defining a symmetric tolerance window (Hue(color) - tolH, Hue(color) + tolH).

tolS : tuple[int, int] | int[¶](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindObjectByColor.tolS "Permalink to this definition")  
The tolerance applied to the expected saturation. The value can either be a tuple of integers for defining an asymmetric tolerance window (Saturation(color) - tolS[0], Saturation(color) + tolS[1]), or an integer for defining a symmetric tolerance window (Saturation(color) - tolS, Saturation(color) + tolS).

tolV : tuple[int, int] | int[¶](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindObjectByColor.tolV "Permalink to this definition")  
The tolerance applied to the expected value. It can either be a tuple of integers for defining an asymmetric tolerance window (Value(color) - tolV[0], Value(color) + tolV[1]), or an integer for defining a symmetric tolerance window (Value(color) - tolV, Value(color) + tolV).

kernelSize : int[¶](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindObjectByColor.kernelSize "Permalink to this definition")  
The size of the kernel that is used to connect separated pixel areas to one object (dilation). A larger kernel connects pixel areas that have more distance to each other. Odd numbers must be provided! Defaults to 5.

Returns:  A list of ImageMatches.

Return type:  [ImageMatchList](#tts.testModule.multimedia.dataElements.MatchObjects.ImageMatchList "tts.testModule.multimedia.dataElements.MatchObjects.ImageMatchList (Python class) — This is a list containing ImageMatch objects. It can be used like a normal python list object, but offers some additional features.")

FindBestTextMatches(*[searchStrings](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindBestTextMatches.searchStrings "tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindBestTextMatches.searchStrings (Python parameter) — List with texts to find")=`None`*, *[maxOccurrences](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindBestTextMatches.maxOccurrences "tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindBestTextMatches.maxOccurrences (Python parameter) — Limits the number of matches to n items.")=`100`*, *[langList](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindBestTextMatches.langList "tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindBestTextMatches.langList (Python parameter) — List of language modules to use for text recognition. ecu.test comes with a preset list of available languages.")=`None`*, *[ocrDataPath](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindBestTextMatches.ocrDataPath "tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindBestTextMatches.ocrDataPath (Python parameter) — The path to the directory containing your custom tesseract language files.")=`None`*, *[isRegex](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindBestTextMatches.isRegex "tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindBestTextMatches.isRegex (Python parameter) — Set True to use regular expression as search strings.")=`False`*)[¶](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindBestTextMatches "Link to this definition")  
Finds texts in an image. Returns a list of matches sorted by the confidence.

Parameters:  searchStrings : list[str][¶](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindBestTextMatches.searchStrings "Permalink to this definition")  
List with texts to find

maxOccurrences : int[¶](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindBestTextMatches.maxOccurrences "Permalink to this definition")  
Limits the number of matches to n items.

langList : list[str][¶](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindBestTextMatches.langList "Permalink to this definition")  
List of language modules to use for text recognition. ecu.test comes with a preset list of available languages. For example use [‘eng’, ‘deu’] to recognize english and german text (in that order). The full list of default languages can be seen in the test configuration window. Additional language modules are available online, please refer to the tesseract documentation to download new language packs. If no language is specified then the languages from the currently active test configuration will be used. Note that if your test configuration contains more than one media node, the first node (in alphabetical order) will be used to load the ocr data.

ocrDataPath : str | None[¶](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindBestTextMatches.ocrDataPath "Permalink to this definition")  
The path to the directory containing your custom tesseract language files. If specified, all \*.traineddata files present in that directory will be added to the default languages as valid inputs for the langList parameter. Leave blank to use ecu.test’s default directory with its preset range of languages.

isRegex : bool[¶](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.FindBestTextMatches.isRegex "Permalink to this definition")  
Set True to use regular expression as search strings.

Returns:  List of matches that contain information about the text position sorted by their confidence.

Return type:  [TextMatchList](#tts.testModule.multimedia.dataElements.MatchObjects.TextMatchList "tts.testModule.multimedia.dataElements.MatchObjects.TextMatchList (Python class) — This is a list containing TextMatch objects. It can be used like a normal python list object, but offers some additional features.")

EmbedInReport(*[embedInReport](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.EmbedInReport.embedInReport "tts.traceRecording.parser.formats.video.VideoRecording.Frame.EmbedInReport.embedInReport (Python parameter) — True if image should be saved in report file")=`True`*)[¶](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.EmbedInReport "Link to this definition")  
If activated, the image is embedded in the TRF report instead of creating a referenced image file in report directory. Warning: This can considerably increase the file size of the report.

Parameters:  embedInReport : bool[¶](#tts.traceRecording.parser.formats.video.VideoRecording.Frame.EmbedInReport.embedInReport "Permalink to this definition")  
True if image should be saved in report file

## OCRService[¶](#ocrservice "Link to this heading")

*class* OCRService[¶](#tts.lib.ocr.OCRService.OCRService "Link to this definition")  
*abstractmethod* GetServiceId()[¶](#tts.lib.ocr.OCRService.OCRService.GetServiceId "Link to this definition")  
Returns the name of the service as a unique ID.

Returns:  Service identifier

Return type:  str

*abstractmethod* ImageToText(*[img](#tts.lib.ocr.OCRService.OCRService.ImageToText.img "tts.lib.ocr.OCRService.OCRService.ImageToText.img (Python parameter) — Input image as instance of class Image")*)[¶](#tts.lib.ocr.OCRService.OCRService.ImageToText "Link to this definition")  
Converts all text in the image into a single string.

Parameters:  img[¶](#tts.lib.ocr.OCRService.OCRService.ImageToText.img "Permalink to this definition")  
Input image as instance of class Image

Returns:  String representing the image’s text content

Return type:  str

*abstractmethod* FindTextPositions(*[img](#tts.lib.ocr.OCRService.OCRService.FindTextPositions.img "tts.lib.ocr.OCRService.OCRService.FindTextPositions.img (Python parameter) — Input image as instance of class Image")*)[¶](#tts.lib.ocr.OCRService.OCRService.FindTextPositions "Link to this definition")  
Looks for text in the image and return all text matches including found text, bounding box and confidence.

Parameters:  img[¶](#tts.lib.ocr.OCRService.OCRService.FindTextPositions.img "Permalink to this definition")  
Input image as instance of class Image

Returns:  List of found text positions

Return type:  [TextMatchList](#tts.testModule.multimedia.dataElements.MatchObjects.TextMatchList "tts.testModule.multimedia.dataElements.MatchObjects.TextMatchList (Python class) — This is a list containing TextMatch objects. It can be used like a normal python list object, but offers some additional features.")

*abstractmethod* GetAvailableParameters()[¶](#tts.lib.ocr.OCRService.OCRService.GetAvailableParameters "Link to this definition")  
Returns a list of all available parameters. The dictionary representing a parameter must contain the fields ‘name’ and ‘default’ and may have an optional parameter ‘description’.

Returns:  List of all parameters of the service

Return type:  list[dict[str, *Any*]]

*abstractmethod* GetParameter(*[name](#tts.lib.ocr.OCRService.OCRService.GetParameter.name "tts.lib.ocr.OCRService.OCRService.GetParameter.name (Python parameter) — Name of the queried parameter")*)[¶](#tts.lib.ocr.OCRService.OCRService.GetParameter "Link to this definition")  
Returns current value of parameter with given name.

Parameters:  name : str[¶](#tts.lib.ocr.OCRService.OCRService.GetParameter.name "Permalink to this definition")  
Name of the queried parameter

Returns:  Current value of the queried parameter

Return type:  *Any*

*abstractmethod* SetParameter(*[name](#tts.lib.ocr.OCRService.OCRService.SetParameter.name "tts.lib.ocr.OCRService.OCRService.SetParameter.name (Python parameter) — Name of the parameter to be set")*, *[value](#tts.lib.ocr.OCRService.OCRService.SetParameter.value "tts.lib.ocr.OCRService.OCRService.SetParameter.value (Python parameter) — New value for the parameter")*)[¶](#tts.lib.ocr.OCRService.OCRService.SetParameter "Link to this definition")  
Modifies existing default parameters of the OCR service.

Parameters:  name : str[¶](#tts.lib.ocr.OCRService.OCRService.SetParameter.name "Permalink to this definition")  
Name of the parameter to be set

value : Any[¶](#tts.lib.ocr.OCRService.OCRService.SetParameter.value "Permalink to this definition")  
New value for the parameter

## TextMatch[¶](#textmatch "Link to this heading")

*class* TextMatch[¶](#tts.testModule.multimedia.dataElements.MatchObjects.TextMatch "Link to this definition")  
Represents a text match.

GetText()[¶](#tts.testModule.multimedia.dataElements.MatchObjects.TextMatch.GetText "Link to this definition")  
Returns:  The found text.

Return type:  str

GetPosition(*[absolutePosition](#tts.testModule.multimedia.dataElements.MatchObjects.TextMatch.GetPosition.absolutePosition "tts.testModule.multimedia.dataElements.MatchObjects.TextMatch.GetPosition.absolutePosition (Python parameter) — If True, the position relates to the original (unmasked) image.")=`False`*)[¶](#tts.testModule.multimedia.dataElements.MatchObjects.TextMatch.GetPosition "Link to this definition")  
Parameters:  absolutePosition : bool[¶](#tts.testModule.multimedia.dataElements.MatchObjects.TextMatch.GetPosition.absolutePosition "Permalink to this definition")  
If True, the position relates to the original (unmasked) image.

Returns:  Position of the top left corner of the match (x, y).

Return type:  tuple[int, int]

GetDimensions()[¶](#tts.testModule.multimedia.dataElements.MatchObjects.TextMatch.GetDimensions "Link to this definition")  
Returns:  The width and height of the found match (w, h).

Return type:  tuple[int, int]

GetCenter(*[absolutePosition](#tts.testModule.multimedia.dataElements.MatchObjects.TextMatch.GetCenter.absolutePosition "tts.testModule.multimedia.dataElements.MatchObjects.TextMatch.GetCenter.absolutePosition (Python parameter) — If True, the position relates to the original (unmasked) image.")=`False`*)[¶](#tts.testModule.multimedia.dataElements.MatchObjects.TextMatch.GetCenter "Link to this definition")  
Parameters:  absolutePosition : bool[¶](#tts.testModule.multimedia.dataElements.MatchObjects.TextMatch.GetCenter.absolutePosition "Permalink to this definition")  
If True, the position relates to the original (unmasked) image.

Returns:  Position of the center of the match in the image (x, y).

Return type:  tuple[int, int]

GetConfidence()[¶](#tts.testModule.multimedia.dataElements.MatchObjects.TextMatch.GetConfidence "Link to this definition")  
Returns:  The confidence of this match object.

Return type:  float

## ImageMatch[¶](#imagematch "Link to this heading")

*class* ImageMatch[¶](#tts.testModule.multimedia.dataElements.MatchObjects.ImageMatch "Link to this definition")  
Represents an image match.

GetImage()[¶](#tts.testModule.multimedia.dataElements.MatchObjects.ImageMatch.GetImage "Link to this definition")  
Returns:  The searched image

Return type:  [`Image`](#tts.testModule.multimedia.dataElements.Image.Image "tts.testModule.multimedia.dataElements.Image.Image (Python class) — Represents an image.")

GetPosition(*[absolutePosition](#tts.testModule.multimedia.dataElements.MatchObjects.ImageMatch.GetPosition.absolutePosition "tts.testModule.multimedia.dataElements.MatchObjects.ImageMatch.GetPosition.absolutePosition (Python parameter) — If True, the position relates to the original (unmasked) image.")=`False`*)[¶](#tts.testModule.multimedia.dataElements.MatchObjects.ImageMatch.GetPosition "Link to this definition")  
Parameters:  absolutePosition : bool[¶](#tts.testModule.multimedia.dataElements.MatchObjects.ImageMatch.GetPosition.absolutePosition "Permalink to this definition")  
If True, the position relates to the original (unmasked) image.

Returns:  Position of the top left corner of the match (x, y).

Return type:  tuple[int, int]

GetDimensions()[¶](#tts.testModule.multimedia.dataElements.MatchObjects.ImageMatch.GetDimensions "Link to this definition")  
Returns:  The width and height of the found match (w, h).

Return type:  tuple[int, int]

GetCenter(*[absolutePosition](#tts.testModule.multimedia.dataElements.MatchObjects.ImageMatch.GetCenter.absolutePosition "tts.testModule.multimedia.dataElements.MatchObjects.ImageMatch.GetCenter.absolutePosition (Python parameter) — If True, the position relates to the original (unmasked) image.")=`False`*)[¶](#tts.testModule.multimedia.dataElements.MatchObjects.ImageMatch.GetCenter "Link to this definition")  
Parameters:  absolutePosition : bool[¶](#tts.testModule.multimedia.dataElements.MatchObjects.ImageMatch.GetCenter.absolutePosition "Permalink to this definition")  
If True, the position relates to the original (unmasked) image.

Returns:  Position of the center of the match in the image (x, y).

Return type:  tuple[int, int]

GetConfidence()[¶](#tts.testModule.multimedia.dataElements.MatchObjects.ImageMatch.GetConfidence "Link to this definition")  
Returns:  The confidence of this match object.

Return type:  float

## MatchList[¶](#matchlist "Link to this heading")

*class* ImageMatchList[¶](#tts.testModule.multimedia.dataElements.MatchObjects.ImageMatchList "Link to this definition")  
This is a list containing [`ImageMatch`](#tts.testModule.multimedia.dataElements.MatchObjects.ImageMatch "tts.testModule.multimedia.dataElements.MatchObjects.ImageMatch (Python class) — Represents an image match.") objects. It can be used like a normal python list object, but offers some additional features.

Filter(*[predicate](#tts.testModule.multimedia.dataElements.MatchObjects.ImageMatchList.Filter.predicate "tts.testModule.multimedia.dataElements.MatchObjects.ImageMatchList.Filter.predicate (Python parameter) — A function to execute for each element in the list.")*)[¶](#tts.testModule.multimedia.dataElements.MatchObjects.ImageMatchList.Filter "Link to this definition")  
Filters the current match list based on a user defined filter predicate.

Parameters:  predicate : Callable[¶](#tts.testModule.multimedia.dataElements.MatchObjects.ImageMatchList.Filter.predicate "Permalink to this definition")  
A function to execute for each element in the list. It should return True to keep the element in the resulting list, and False otherwise.

Returns:  A new match list containing just the elements that pass the test

Return type:  MatchList

*class* TextMatchList[¶](#tts.testModule.multimedia.dataElements.MatchObjects.TextMatchList "Link to this definition")  
This is a list containing [`TextMatch`](#tts.testModule.multimedia.dataElements.MatchObjects.TextMatch "tts.testModule.multimedia.dataElements.MatchObjects.TextMatch (Python class) — Represents a text match.") objects. It can be used like a normal python list object, but offers some additional features.

ContainsText(*[text](#tts.testModule.multimedia.dataElements.MatchObjects.TextMatchList.ContainsText.text "tts.testModule.multimedia.dataElements.MatchObjects.TextMatchList.ContainsText.text (Python parameter) — The text that will be searched in the list (case-sensitive).")*)[¶](#tts.testModule.multimedia.dataElements.MatchObjects.TextMatchList.ContainsText "Link to this definition")  
Checks if a list of TextMatches contains a given string.

Parameters:  text : str[¶](#tts.testModule.multimedia.dataElements.MatchObjects.TextMatchList.ContainsText.text "Permalink to this definition")  
The text that will be searched in the list (case-sensitive).

Returns:  Returns True if the list contains any element with the given text.

Return type:  bool

FilterByText(*[searchString](#tts.testModule.multimedia.dataElements.MatchObjects.TextMatchList.FilterByText.searchString "tts.testModule.multimedia.dataElements.MatchObjects.TextMatchList.FilterByText.searchString (Python parameter) — The text or regex pattern that will be searched in the list (case-sensitive).")*, *[isRegex](#tts.testModule.multimedia.dataElements.MatchObjects.TextMatchList.FilterByText.isRegex "tts.testModule.multimedia.dataElements.MatchObjects.TextMatchList.FilterByText.isRegex (Python parameter) — Set to True if the given search string is a regex pattern.")=`False`*)[¶](#tts.testModule.multimedia.dataElements.MatchObjects.TextMatchList.FilterByText "Link to this definition")  
Filters the TextMatchList by the given text or regex pattern.

Parameters:  searchString : str[¶](#tts.testModule.multimedia.dataElements.MatchObjects.TextMatchList.FilterByText.searchString "Permalink to this definition")  
The text or regex pattern that will be searched in the list (case-sensitive).

isRegex : bool[¶](#tts.testModule.multimedia.dataElements.MatchObjects.TextMatchList.FilterByText.isRegex "Permalink to this definition")  
Set to True if the given search string is a regex pattern.

Returns:  Returns the filtered TextMatchList.

Return type:  [TextMatchList](#tts.testModule.multimedia.dataElements.MatchObjects.TextMatchList "tts.testModule.multimedia.dataElements.MatchObjects.TextMatchList (Python class) — This is a list containing TextMatch objects. It can be used like a normal python list object, but offers some additional features.")

Filter(*[predicate](#tts.testModule.multimedia.dataElements.MatchObjects.TextMatchList.Filter.predicate "tts.testModule.multimedia.dataElements.MatchObjects.TextMatchList.Filter.predicate (Python parameter) — A function to execute for each element in the list.")*)[¶](#tts.testModule.multimedia.dataElements.MatchObjects.TextMatchList.Filter "Link to this definition")  
Filters the current match list based on a user defined filter predicate.

Parameters:  predicate : Callable[¶](#tts.testModule.multimedia.dataElements.MatchObjects.TextMatchList.Filter.predicate "Permalink to this definition")  
A function to execute for each element in the list. It should return True to keep the element in the resulting list, and False otherwise.

Returns:  A new match list containing just the elements that pass the test

Return type:  MatchList

## AudioBlock[¶](#audioblock "Link to this heading")

*class* AudioBlock[¶](#tts.testModule.multimedia.dataElements.AudioBlock.AudioBlock "Link to this definition")  
Parameters:  data : str | npt.NDArray[np.int16] | npt.NDArray[float]  
The source from which to load audio data (a file path or a NumPy array). In case of a file path it has to be an absolute path or a path relative to the workspace. In case of a NumPy array, the audio channels must either be a 1D NumPy array of shape `(<frames>)` for a one channel stream or a 2D NumPy array of shape `(<frames>, <channels>)`for a multiple channel stream. Array members must be of type np.int16 or float. The former will be internally normalized to float between -1.0 and 1.0.

sampleRate : int | None  
The sample rate of the audio data. If the AudioBlock is created from a NumPy array, the sample rate can be passed. If the audio data is loaded from file, the sample rate will be extracted.

Creates a new AudioBlock object from a given NumPy array or a file. Is also returned by the read step of a mapping of type audio device being accessible via the media access tab. However, the audio recording feature is still in development, and thus hidden behind a feature flag.

The supported audio formats are (according to soundfile version 0.12.1):

- ‘AIFF’: ‘AIFF (Apple/SGI)’,

- ‘AU’: ‘AU (Sun/NeXT)’,

- ‘AVR’: ‘AVR (Audio Visual Research)’,

- ‘CAF’: ‘CAF (Apple Core Audio File)’,

- ‘FLAC’: ‘FLAC (Free Lossless Audio Codec)’,

- ‘HTK’: ‘HTK (HMM Tool Kit)’,

- ‘SVX’: ‘IFF (Amiga IFF/SVX8/SV16)’,

- ‘MAT4’: ‘MAT4 (GNU Octave 2.0 / Matlab 4.2)’,

- ‘MAT5’: ‘MAT5 (GNU Octave 2.1 / Matlab 5.0)’,

- ‘MPC2K’: ‘MPC (Akai MPC 2k)’,

- ‘MP3’: ‘MPEG-1/2 Audio’,

- ‘OGG’: ‘OGG (OGG Container format)’,

- ‘PAF’: ‘PAF (Ensoniq PARIS)’,

- ‘PVF’: ‘PVF (Portable Voice Format)’,

- ‘RAW’: ‘RAW (header-less)’,

- ‘RF64’: ‘RF64 (RIFF 64)’,

- ‘SD2’: ‘SD2 (Sound Designer II)’,

- ‘SDS’: ‘SDS (Midi Sample Dump Standard)’,

- ‘IRCAM’: ‘SF (Berkeley/IRCAM/CARL)’,

- ‘VOC’: ‘VOC (Creative Labs)’,

- ‘W64’: ‘W64 (SoundFoundry WAVE 64)’,

- ‘WAV’: ‘WAV (Microsoft)’,

- ‘NIST’: ‘WAV (NIST Sphere)’,

- ‘WAVEX’: ‘WAVEX (Microsoft)’,

- ‘WVE’: ‘WVE (Psion Series 3)’,

- ‘XI’: ‘XI (FastTracker 2)’

Example usage:

- `AudioBlock(numpy.array([1, 2, 3, ... 98, 99, 100]), 44100) # AudioBlock with one channel`- `AudioBlock(numpy.array([[8, 3], [2, 6], ... [5, 7]]), 88200) # AudioBlock with two channels`- `AudioBlock('path/to/file/filename.extension') # AudioBlock from file`GetData()[¶](#tts.testModule.multimedia.dataElements.AudioBlock.AudioBlock.GetData "Link to this definition")  
Returns the data of the audio channel(s).

Returns:  Data of the audio channels as 1D NumPy array (frames) if only one channel exists in case of multiple channels a 2D NumPy array (frames x channels).

Return type:  npt.NDArray[np.float64]

GetChannelData(*[channel](#tts.testModule.multimedia.dataElements.AudioBlock.AudioBlock.GetChannelData.channel "tts.testModule.multimedia.dataElements.AudioBlock.AudioBlock.GetChannelData.channel (Python parameter) — Channel number starting with 1.")*)[¶](#tts.testModule.multimedia.dataElements.AudioBlock.AudioBlock.GetChannelData "Link to this definition")  
Returns the data of the specified audio channel.

Parameters:  channel : int[¶](#tts.testModule.multimedia.dataElements.AudioBlock.AudioBlock.GetChannelData.channel "Permalink to this definition")  
Channel number starting with 1.

Returns:  Audio data of the specified audio channel as 1D NumPy array.

Raises:  
**IndexError** – Channel does not exist.

Return type:  npt.NDArray[np.float64]

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

FindSnippet(*[snippet](#tts.testModule.multimedia.dataElements.AudioBlock.AudioBlock.FindSnippet.snippet "tts.testModule.multimedia.dataElements.AudioBlock.AudioBlock.FindSnippet.snippet (Python parameter) — The searched snippet.")*, *[threshold](#tts.testModule.multimedia.dataElements.AudioBlock.AudioBlock.FindSnippet.threshold "tts.testModule.multimedia.dataElements.AudioBlock.AudioBlock.FindSnippet.threshold (Python parameter) — Threshold for the confidence value.")=`0.35`*, *[noiseResistantComparison](#tts.testModule.multimedia.dataElements.AudioBlock.AudioBlock.FindSnippet.noiseResistantComparison "tts.testModule.multimedia.dataElements.AudioBlock.AudioBlock.FindSnippet.noiseResistantComparison (Python parameter) — Specifies whether the noise resistant algorithm shall be used.")=`False`*)[¶](#tts.testModule.multimedia.dataElements.AudioBlock.AudioBlock.FindSnippet "Link to this definition")  
Searches in the data of the AudioBlock for the passed snippet. If the noiseResistantComparison flag is set, it is possible to search the snippet within noisy data, but the confidence value is generally lower.

Parameters:  snippet : [AudioBlock](#tts.testModule.multimedia.dataElements.AudioBlock.AudioBlock "tts.testModule.multimedia.dataElements.AudioBlock.AudioBlock (Python class) — The source from which to load audio data (a file path or a NumPy array). In case of a file path it has to be an absolute path or a path relative to the workspace. In case of a NumPy array, the audio channels must either be a 1D NumPy array of shape (<frames>) for a one channel stream or a 2D NumPy array of shape (<frames>, <channels>) for a multiple channel stream. Array members must be of type np.int16 or float. The former will be internally normalized to float between -1.0 and 1.0.")[¶](#tts.testModule.multimedia.dataElements.AudioBlock.AudioBlock.FindSnippet.snippet "Permalink to this definition")  
The searched snippet.

threshold : float[¶](#tts.testModule.multimedia.dataElements.AudioBlock.AudioBlock.FindSnippet.threshold "Permalink to this definition")  
Threshold for the confidence value. Only matches with a higher confidence value will be returned.

noiseResistantComparison : bool[¶](#tts.testModule.multimedia.dataElements.AudioBlock.AudioBlock.FindSnippet.noiseResistantComparison "Permalink to this definition")  
Specifies whether the noise resistant algorithm shall be used.

Returns:  Confidence values and positions at which the snippet was found.

Return type:  list[tuple[float, float]]

Save(*[path](#tts.testModule.multimedia.dataElements.AudioBlock.AudioBlock.Save.path "tts.testModule.multimedia.dataElements.AudioBlock.AudioBlock.Save.path (Python parameter) — Save location of the AudioBlock with filename and file ending.")*, *[fileFormat](#tts.testModule.multimedia.dataElements.AudioBlock.AudioBlock.Save.fileFormat "tts.testModule.multimedia.dataElements.AudioBlock.AudioBlock.Save.fileFormat (Python parameter) — Audio file format, default: FLAC")=`'FLAC'`*, *[mono](#tts.testModule.multimedia.dataElements.AudioBlock.AudioBlock.Save.mono "tts.testModule.multimedia.dataElements.AudioBlock.AudioBlock.Save.mono (Python parameter) — Convert multichannel data to mono")=`False`*)[¶](#tts.testModule.multimedia.dataElements.AudioBlock.AudioBlock.Save "Link to this definition")  
Saves the AudioBlock as an audio file.

The format of the audio file is FLAC either with the given sample rate or the default value of 44100 Hz, a bit depth of 16 bits and is limited to a maximum of 8 channels.

Parameters:  path : str[¶](#tts.testModule.multimedia.dataElements.AudioBlock.AudioBlock.Save.path "Permalink to this definition")  
Save location of the AudioBlock with filename and file ending.

fileFormat : str[¶](#tts.testModule.multimedia.dataElements.AudioBlock.AudioBlock.Save.fileFormat "Permalink to this definition")  
Audio file format, default: FLAC

mono : bool[¶](#tts.testModule.multimedia.dataElements.AudioBlock.AudioBlock.Save.mono "Permalink to this definition")  
Convert multichannel data to mono

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
