# API for Touch Inputs[¶](#api-for-touch-inputs "Link to this heading")

Part of the [Object based program API](objectApi.md#objectapi)

## TouchInputApi[¶](#touchinputapi "Link to this heading")

*class* TouchInputApi[¶](#ApiClient.TouchInputApi "Link to this definition")  
API to create touch input actions

Returned by

- [`MultimediaApi.TouchInputApi`](MultimediaApi.md#ApiClient.MultimediaApi.TouchInputApi "ApiClient.MultimediaApi.TouchInputApi")

CreateHold(*posX='0'*, *posY='0'*, *duration='1.0'*)[¶](#ApiClient.TouchInputApi.CreateHold "Link to this definition")  
Create a new hold input action object.

Parameters:  - **posX** (*str*) – Pixel position of first coordinate

- **posY** (*str*) – Pixel position of second coordinate

- **duration** (*str*) – Hold duration in seconds

Returns:  A new hold object

Return type:  [`Hold`](#ApiClient.Hold "ApiClient.Hold")

CreateHoldAndSwipe(*startX='0'*, *startY='0'*, *endX='0'*, *endY='0'*, *holdDuration='1.0'*, *swipeDuration='1.0'*)[¶](#ApiClient.TouchInputApi.CreateHoldAndSwipe "Link to this definition")  
Create a new hold-and-swipe input action object.

Parameters:  - **startX** (*str*) – Starting pixel position of first coordinate

- **startY** (*str*) – Starting pixel position of second coordinate

- **endX** (*str*) – Final pixel position of first coordinate

- **endY** (*str*) – Final pixel position of second coordinate

- **holdDuration** (*str*) – Duration of initial hold in seconds

- **swipeDuration** (*str*) – Duration of swipe gesture in seconds

Returns:  A new hold-and-swipe object

Return type:  [`HoldAndSwipe`](#ApiClient.HoldAndSwipe "ApiClient.HoldAndSwipe")

CreateMultiSwipe(*startX='0'*, *startY='0'*, *endX='0'*, *endY='0'*, *duration='1.0'*, *fingerCount='2'*, *distance='10'*)[¶](#ApiClient.TouchInputApi.CreateMultiSwipe "Link to this definition")  
Create a new multiswipe input action object.

Parameters:  - **startX** (*str*) – Starting pixel position of first coordinate

- **startY** (*str*) – Starting pixel position of second coordinate

- **endX** (*str*) – Final pixel position of first coordinate

- **endY** (*str*) – Final pixel position of second coordinate

- **duration** (*str*) – Duration of gesture in seconds

- **fingerCount** (*str*) – Number of fingers performing the swipe

- **distance** (*str*) – Mean Euclidean pixel distance between fingers

Returns:  A new multiswipe object

Return type:  [`MultiSwipe`](#ApiClient.MultiSwipe "ApiClient.MultiSwipe")

CreateMultiTap(*posX='0'*, *posY='0'*, *count='2'*, *interval='1.0'*)[¶](#ApiClient.TouchInputApi.CreateMultiTap "Link to this definition")  
Create a new multitap input action object.

Parameters:  - **posX** (*str*) – Pixel position of first coordinate

- **posY** (*str*) – Pixel position of second coordinate

- **count** (*str*) – Number of successive taps

- **interval** (*str*) – Time interval between successive taps in seconds

Returns:  A new multitap object

Return type:  [`MultiTap`](#ApiClient.MultiTap "ApiClient.MultiTap")

CreatePinch(*pos1X='0'*, *pos1Y='0'*, *pos2X='0'*, *pos2Y='0'*, *duration='1.0'*, *scale='1.5'*)[¶](#ApiClient.TouchInputApi.CreatePinch "Link to this definition")  
Create a new pinch input action object.

Parameters:  - **pos1X** (*str*) – x-coordinate of first finger’s pixel position

- **pos1Y** (*str*) – y-coordinate of first finger’s pixel position

- **pos2X** (*str*) – x-coordinate of second finger’s pixel position

- **pos2Y** (*str*) – y-coordinate of second finger’s pixel position

- **duration** (*str*) – Duration of gesture in seconds

- **scale** (*str*) – Scaling factor of gesture

Returns:  A new pinch object

Return type:  [`Pinch`](#ApiClient.Pinch "ApiClient.Pinch")

CreateRotate(*pos1X='0'*, *pos1Y='0'*, *pos2X='0'*, *pos2Y='0'*, *duration='1.0'*, *angle='90'*)[¶](#ApiClient.TouchInputApi.CreateRotate "Link to this definition")  
Create a new rotate input action object.

Parameters:  - **pos1X** (*str*) – x-coordinate of first finger’s pixel position

- **pos1Y** (*str*) – y-coordinate of first finger’s pixel position

- **pos2X** (*str*) – x-coordinate of second finger’s pixel position

- **pos2Y** (*str*) – y-coordinate of second finger’s pixel position

- **duration** (*str*) – Duration of gesture in seconds

- **angle** (*str*) – Rotation angle in degree

Returns:  A new rotate object

Return type:  [`Rotate`](#ApiClient.Rotate "ApiClient.Rotate")

CreateSwipe(*startX='0'*, *startY='0'*, *endX='10'*, *endY='10'*, *duration='1.0'*)[¶](#ApiClient.TouchInputApi.CreateSwipe "Link to this definition")  
Create a new swipe input action object.

Parameters:  - **startX** (*str*) – Starting pixel position of first coordinate

- **startY** (*str*) – Starting pixel position of second coordinate

- **endX** (*str*) – Final pixel position of first coordinate

- **endY** (*str*) – Final pixel position of second coordinate

- **duration** (*str*) – Duration of gesture in seconds

Returns:  A new swipe object

Return type:  [`Swipe`](#ApiClient.Swipe "ApiClient.Swipe")

CreateTap(*posX='0'*, *posY='0'*)[¶](#ApiClient.TouchInputApi.CreateTap "Link to this definition")  
Create a new tap input action object.

Parameters:  - **posX** (*str*) – Pixel position of first coordinate

- **posY** (*str*) – Pixel position of second coordinate

Returns:  A new tap object

Return type:  [`Tap`](#ApiClient.Tap "ApiClient.Tap")

## Hold[¶](#hold "Link to this heading")

*class* Hold[¶](#ApiClient.Hold "Link to this definition")  
Base class

[`TouchInputAction`](TestStepApi.md#ApiClient.TouchInputAction "ApiClient.TouchInputAction")

Returned by

- [`TouchInputApi.CreateHold`](#ApiClient.TouchInputApi.CreateHold "ApiClient.TouchInputApi.CreateHold")

Clone()[¶](#ApiClient.Hold.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`Hold`](#ApiClient.Hold "ApiClient.Hold")

GetHoldDuration()[¶](#ApiClient.Hold.GetHoldDuration "Link to this definition")  
Returns the value of the hold duration.

Returns:  Value of hold duration

Return type:  str

GetHoldDurationUnit()[¶](#ApiClient.Hold.GetHoldDurationUnit "Link to this definition")  
Returns the unit of the hold duration.

Returns:  Unit of hold duration

Return type:  str

GetName()[¶](#ApiClient.Hold.GetName "Link to this definition")  
Returns the name of the touch input action

Returns:  The name of the touch input action

Return type:  str

GetPosX()[¶](#ApiClient.Hold.GetPosX "Link to this definition")  
Returns value of the first coordinate.

Returns:  Value of x-coordinate

Return type:  str

GetPosXUnit()[¶](#ApiClient.Hold.GetPosXUnit "Link to this definition")  
Returns unit of the first coordinate.

Returns:  Unit of x-coordinate

Return type:  str

GetPosY()[¶](#ApiClient.Hold.GetPosY "Link to this definition")  
Returns value of the second coordinate.

Returns:  Value of y-coordinate

Return type:  str

GetPosYUnit()[¶](#ApiClient.Hold.GetPosYUnit "Link to this definition")  
Returns unit of the second coordinate.

Returns:  Unit of y-coordinate

Return type:  str

SetHoldDuration(*expr*, *unit='s'*)[¶](#ApiClient.Hold.SetHoldDuration "Link to this definition")  
Sets the hold duration.

Parameters:  - **expr** (*str*) – Hold duration

- **unit** (*str*) – unit of duration, milliseconds ‘ms’ or seconds ‘s’

SetPosX(*expr*, *unit='px'*)[¶](#ApiClient.Hold.SetPosX "Link to this definition")  
Sets first coordinate of position.

Parameters:  - **expr** (*str*) – expression for x-coordinate of position

- **unit** (*str*) – unit of x-coordinate, absolute ‘px’ or relative ‘%’

SetPosY(*expr*, *unit='px'*)[¶](#ApiClient.Hold.SetPosY "Link to this definition")  
Sets second coordinate of position.

Parameters:  - **expr** (*str*) – expression for y-coordinate of position

- **unit** (*str*) – unit of y-coordinate, absolute ‘px’ or relative ‘%’

## HoldAndSwipe[¶](#holdandswipe "Link to this heading")

*class* HoldAndSwipe[¶](#ApiClient.HoldAndSwipe "Link to this definition")  
Base class

[`TouchInputAction`](TestStepApi.md#ApiClient.TouchInputAction "ApiClient.TouchInputAction")

Returned by

- [`TouchInputApi.CreateHoldAndSwipe`](#ApiClient.TouchInputApi.CreateHoldAndSwipe "ApiClient.TouchInputApi.CreateHoldAndSwipe")

Clone()[¶](#ApiClient.HoldAndSwipe.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`HoldAndSwipe`](#ApiClient.HoldAndSwipe "ApiClient.HoldAndSwipe")

GetEndX()[¶](#ApiClient.HoldAndSwipe.GetEndX "Link to this definition")  
Returns the value of the first coordinate of the final position.

Returns:  Value of x-coordinate

Return type:  str

GetEndXUnit()[¶](#ApiClient.HoldAndSwipe.GetEndXUnit "Link to this definition")  
Returns the unit of the first coordinate of the final position.

Returns:  Unit of x-coordinate

Return type:  str

GetEndY()[¶](#ApiClient.HoldAndSwipe.GetEndY "Link to this definition")  
Returns the value of the second coordinate of the final position.

Returns:  Value of y-coordinate

Return type:  str

GetEndYUnit()[¶](#ApiClient.HoldAndSwipe.GetEndYUnit "Link to this definition")  
Returns the unit of the second coordinate of the final position.

Returns:  Unit of y-coordinate

Return type:  str

GetHoldDuration()[¶](#ApiClient.HoldAndSwipe.GetHoldDuration "Link to this definition")  
Returns the value of the hold duration.

Returns:  Value of hold duration

Return type:  str

GetHoldDurationUnit()[¶](#ApiClient.HoldAndSwipe.GetHoldDurationUnit "Link to this definition")  
Returns the unit of the hold duration.

Returns:  Unit of hold duration

Return type:  str

GetName()[¶](#ApiClient.HoldAndSwipe.GetName "Link to this definition")  
Returns the name of the touch input action

Returns:  The name of the touch input action

Return type:  str

GetStartX()[¶](#ApiClient.HoldAndSwipe.GetStartX "Link to this definition")  
Returns the value of the first coordinate of the starting position.

Returns:  Value of x-coordinate

Return type:  str

GetStartXUnit()[¶](#ApiClient.HoldAndSwipe.GetStartXUnit "Link to this definition")  
Returns the unit of the first coordinate of the starting position.

Returns:  Unit of x-coordinate

Return type:  str

GetStartY()[¶](#ApiClient.HoldAndSwipe.GetStartY "Link to this definition")  
Returns the value of the second coordinate of the starting position.

Returns:  Value of y-coordinate

Return type:  str

GetStartYUnit()[¶](#ApiClient.HoldAndSwipe.GetStartYUnit "Link to this definition")  
Returns the unit of the second coordinate of the starting position.

Returns:  Unit of y-coordinate

Return type:  str

GetSwipeDuration()[¶](#ApiClient.HoldAndSwipe.GetSwipeDuration "Link to this definition")  
Returns the value of the swipe duration.

Returns:  Swipe duration

Return type:  str

GetSwipeDurationUnit()[¶](#ApiClient.HoldAndSwipe.GetSwipeDurationUnit "Link to this definition")  
Returns the unit of the swipe duration.

Returns:  Swipe duration

Return type:  str

SetEndX(*expr*, *unit='px'*)[¶](#ApiClient.HoldAndSwipe.SetEndX "Link to this definition")  
Sets first coordinate of the final position.

Parameters:  - **expr** (*str*) – expression for x-coordinate of position

- **unit** (*str*) – unit of x-coordinate, absolute ‘px’ or relative ‘%’

SetEndY(*expr*, *unit='px'*)[¶](#ApiClient.HoldAndSwipe.SetEndY "Link to this definition")  
Sets second coordinate of the final position.

Parameters:  - **expr** (*str*) – expression for y-coordinate of position

- **unit** (*str*) – unit of y-coordinate, absolute ‘px’ or relative ‘%’

SetHoldDuration(*expr*, *unit='s'*)[¶](#ApiClient.HoldAndSwipe.SetHoldDuration "Link to this definition")  
Sets the hold duration.

Parameters:  - **expr** (*str*) – Hold duration

- **unit** (*str*) – unit of duration, milliseconds ‘ms’ or seconds ‘s’

SetStartX(*expr*, *unit='px'*)[¶](#ApiClient.HoldAndSwipe.SetStartX "Link to this definition")  
Sets first coordinate of the starting position.

Parameters:  - **expr** (*str*) – expression for x-coordinate of position

- **unit** (*str*) – unit of x-coordinate, absolute ‘px’ or relative ‘%’

SetStartY(*expr*, *unit='px'*)[¶](#ApiClient.HoldAndSwipe.SetStartY "Link to this definition")  
Sets second coordinate of the starting position.

Parameters:  - **expr** (*str*) – expression for y-coordinate of position

- **unit** (*str*) – unit of y-coordinate, absolute ‘px’ or relative ‘%’

SetSwipeDuration(*expr*, *unit='s'*)[¶](#ApiClient.HoldAndSwipe.SetSwipeDuration "Link to this definition")  
Sets the swipe duration.

Parameters:  - **expr** (*str*) – Swipe duration

- **unit** (*str*) – unit of duration, milliseconds ‘ms’ or seconds ‘s’

## MultiSwipe[¶](#multiswipe "Link to this heading")

*class* MultiSwipe[¶](#ApiClient.MultiSwipe "Link to this definition")  
Base class

[`TouchInputAction`](TestStepApi.md#ApiClient.TouchInputAction "ApiClient.TouchInputAction")

Returned by

- [`TouchInputApi.CreateMultiSwipe`](#ApiClient.TouchInputApi.CreateMultiSwipe "ApiClient.TouchInputApi.CreateMultiSwipe")

Clone()[¶](#ApiClient.MultiSwipe.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`MultiSwipe`](#ApiClient.MultiSwipe "ApiClient.MultiSwipe")

GetEndX()[¶](#ApiClient.MultiSwipe.GetEndX "Link to this definition")  
Returns the value of the first coordinate of the final position.

Returns:  Value of x-coordinate

Return type:  str

GetEndXUnit()[¶](#ApiClient.MultiSwipe.GetEndXUnit "Link to this definition")  
Returns the unit of the first coordinate of the final position.

Returns:  Unit of x-coordinate

Return type:  str

GetEndY()[¶](#ApiClient.MultiSwipe.GetEndY "Link to this definition")  
Returns the value of the second coordinate of the final position.

Returns:  Value of y-coordinate

Return type:  str

GetEndYUnit()[¶](#ApiClient.MultiSwipe.GetEndYUnit "Link to this definition")  
Returns the unit of the second coordinate of the final position.

Returns:  Unit of y-coordinate

Return type:  str

GetFingerCount()[¶](#ApiClient.MultiSwipe.GetFingerCount "Link to this definition")  
Returns the number of fingers involved.

Returns:  Number of fingers

Return type:  str

GetFingerDistance()[¶](#ApiClient.MultiSwipe.GetFingerDistance "Link to this definition")  
Returns the value of the mean distance of fingers.

Returns:  Value of mean distance of fingers

Return type:  str

GetFingerDistanceUnit()[¶](#ApiClient.MultiSwipe.GetFingerDistanceUnit "Link to this definition")  
Returns the unit of the mean distance of fingers.

Returns:  Unit of mean distance of fingers

Return type:  str

GetName()[¶](#ApiClient.MultiSwipe.GetName "Link to this definition")  
Returns the name of the touch input action

Returns:  The name of the touch input action

Return type:  str

GetStartX()[¶](#ApiClient.MultiSwipe.GetStartX "Link to this definition")  
Returns the value of the first coordinate of the starting position.

Returns:  Value of x-coordinate

Return type:  str

GetStartXUnit()[¶](#ApiClient.MultiSwipe.GetStartXUnit "Link to this definition")  
Returns the unit of the first coordinate of the starting position.

Returns:  Unit of x-coordinate

Return type:  str

GetStartY()[¶](#ApiClient.MultiSwipe.GetStartY "Link to this definition")  
Returns the value of the second coordinate of the starting position.

Returns:  Value of y-coordinate

Return type:  str

GetStartYUnit()[¶](#ApiClient.MultiSwipe.GetStartYUnit "Link to this definition")  
Returns the unit of the second coordinate of the starting position.

Returns:  Unit of y-coordinate

Return type:  str

GetSwipeDuration()[¶](#ApiClient.MultiSwipe.GetSwipeDuration "Link to this definition")  
Returns the value of the swipe duration.

Returns:  Swipe duration

Return type:  str

GetSwipeDurationUnit()[¶](#ApiClient.MultiSwipe.GetSwipeDurationUnit "Link to this definition")  
Returns the unit of the swipe duration.

Returns:  Swipe duration

Return type:  str

SetEndX(*expr*, *unit='px'*)[¶](#ApiClient.MultiSwipe.SetEndX "Link to this definition")  
Sets first coordinate of the final position.

Parameters:  - **expr** (*str*) – expression for x-coordinate of position

- **unit** (*str*) – unit of x-coordinate, absolute ‘px’ or relative ‘%’

SetEndY(*expr*, *unit='px'*)[¶](#ApiClient.MultiSwipe.SetEndY "Link to this definition")  
Sets second coordinate of the final position.

Parameters:  - **expr** (*str*) – expression for y-coordinate of position

- **unit** (*str*) – unit of y-coordinate, absolute ‘px’ or relative ‘%’

SetFingerCount(*expr*)[¶](#ApiClient.MultiSwipe.SetFingerCount "Link to this definition")  
Sets the number of fingers involved.

Parameters:  **expr** (*str*) – Number of fingers

SetFingerDistance(*expr*, *unit='px'*)[¶](#ApiClient.MultiSwipe.SetFingerDistance "Link to this definition")  
Sets the mean finger distance

Parameters:  - **expr** (*str*) – Mean finger distance

- **unit** (*str*) – unit of distance, absolute ‘px’ or relative ‘%’

SetStartX(*expr*, *unit='px'*)[¶](#ApiClient.MultiSwipe.SetStartX "Link to this definition")  
Sets first coordinate of the starting position.

Parameters:  - **expr** (*str*) – expression for x-coordinate of position

- **unit** (*str*) – unit of x-coordinate, absolute ‘px’ or relative ‘%’

SetStartY(*expr*, *unit='px'*)[¶](#ApiClient.MultiSwipe.SetStartY "Link to this definition")  
Sets second coordinate of the starting position.

Parameters:  - **expr** (*str*) – expression for y-coordinate of position

- **unit** (*str*) – unit of y-coordinate, absolute ‘px’ or relative ‘%’

SetSwipeDuration(*expr*, *unit='s'*)[¶](#ApiClient.MultiSwipe.SetSwipeDuration "Link to this definition")  
Sets the swipe duration.

Parameters:  - **expr** (*str*) – Swipe duration

- **unit** (*str*) – unit of duration, milliseconds ‘ms’ or seconds ‘s’

## MultiTap[¶](#multitap "Link to this heading")

*class* MultiTap[¶](#ApiClient.MultiTap "Link to this definition")  
Base class

[`TouchInputAction`](TestStepApi.md#ApiClient.TouchInputAction "ApiClient.TouchInputAction")

Returned by

- [`TouchInputApi.CreateMultiTap`](#ApiClient.TouchInputApi.CreateMultiTap "ApiClient.TouchInputApi.CreateMultiTap")

Clone()[¶](#ApiClient.MultiTap.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`MultiTap`](#ApiClient.MultiTap "ApiClient.MultiTap")

GetCount()[¶](#ApiClient.MultiTap.GetCount "Link to this definition")  
Returns the number of successive taps.

Returns:  Number of taps

Return type:  str

GetInterval()[¶](#ApiClient.MultiTap.GetInterval "Link to this definition")  
Returns the value of the time interval between successive taps.

Returns:  Value of time interval between taps

Return type:  str

GetIntervalUnit()[¶](#ApiClient.MultiTap.GetIntervalUnit "Link to this definition")  
Returns the unit of the time interval between successive taps.

:return:Unit of time interval between taps :rtype: str

GetName()[¶](#ApiClient.MultiTap.GetName "Link to this definition")  
Returns the name of the touch input action

Returns:  The name of the touch input action

Return type:  str

GetPosX()[¶](#ApiClient.MultiTap.GetPosX "Link to this definition")  
Returns value of the first coordinate.

Returns:  Value of x-coordinate

Return type:  str

GetPosXUnit()[¶](#ApiClient.MultiTap.GetPosXUnit "Link to this definition")  
Returns unit of the first coordinate.

Returns:  Unit of x-coordinate

Return type:  str

GetPosY()[¶](#ApiClient.MultiTap.GetPosY "Link to this definition")  
Returns value of the second coordinate.

Returns:  Value of y-coordinate

Return type:  str

GetPosYUnit()[¶](#ApiClient.MultiTap.GetPosYUnit "Link to this definition")  
Returns unit of the second coordinate.

Returns:  Unit of y-coordinate

Return type:  str

SetCount(*expr*)[¶](#ApiClient.MultiTap.SetCount "Link to this definition")  
Sets the number of successive taps.

Parameters:  **expr** (*str*) – Number of taps

SetInterval(*expr*, *unit='s'*)[¶](#ApiClient.MultiTap.SetInterval "Link to this definition")  
Sets the time interval between successive taps.

Parameters:  - **expr** (*str*) – Time interval between taps

- **unit** (*str*) – unit of time interval, milliseconds ‘ms’ or seconds ‘s’

SetPosX(*expr*, *unit='px'*)[¶](#ApiClient.MultiTap.SetPosX "Link to this definition")  
Sets first coordinate of position.

Parameters:  - **expr** (*str*) – expression for x-coordinate of position

- **unit** (*str*) – unit of x-coordinate, absolute ‘px’ or relative ‘%’

SetPosY(*expr*, *unit='px'*)[¶](#ApiClient.MultiTap.SetPosY "Link to this definition")  
Sets second coordinate of position.

Parameters:  - **expr** (*str*) – expression for y-coordinate of position

- **unit** (*str*) – unit of y-coordinate, absolute ‘px’ or relative ‘%’

## Pinch[¶](#pinch "Link to this heading")

*class* Pinch[¶](#ApiClient.Pinch "Link to this definition")  
Base class

[`TouchInputAction`](TestStepApi.md#ApiClient.TouchInputAction "ApiClient.TouchInputAction")

Returned by

- [`TouchInputApi.CreatePinch`](#ApiClient.TouchInputApi.CreatePinch "ApiClient.TouchInputApi.CreatePinch")

Clone()[¶](#ApiClient.Pinch.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`Pinch`](#ApiClient.Pinch "ApiClient.Pinch")

GetName()[¶](#ApiClient.Pinch.GetName "Link to this definition")  
Returns the name of the touch input action

Returns:  The name of the touch input action

Return type:  str

GetPinchDuration()[¶](#ApiClient.Pinch.GetPinchDuration "Link to this definition")  
Returns the value of the pinch duration.

Returns:  Value of pinch duration

Return type:  str

GetPinchDurationUnit()[¶](#ApiClient.Pinch.GetPinchDurationUnit "Link to this definition")  
Returns the unit of the pinch duration.

Returns:  Unit of pinch duration

Return type:  str

GetPos1X()[¶](#ApiClient.Pinch.GetPos1X "Link to this definition")  
Returns the value of the first coordinate of first finger.

Returns:  Value of first finger’s x-coordinate

Return type:  str

GetPos1XUnit()[¶](#ApiClient.Pinch.GetPos1XUnit "Link to this definition")  
Returns the unit of the first coordinate of first finger.

Returns:  Unit of first finger’s x-coordinate

Return type:  str

GetPos1Y()[¶](#ApiClient.Pinch.GetPos1Y "Link to this definition")  
Returns the value of the seconed coordinate of first finger.

Returns:  Value of first finger’s y-coordinate

Return type:  str

GetPos1YUnit()[¶](#ApiClient.Pinch.GetPos1YUnit "Link to this definition")  
Returns the unit of the seconed coordinate of first finger.

Returns:  Unit of first finger’s y-coordinate

Return type:  str

GetPos2X()[¶](#ApiClient.Pinch.GetPos2X "Link to this definition")  
Returns the value of the first coordinate of second finger.

Returns:  Value of second finger’s x-coordinate

Return type:  str

GetPos2XUnit()[¶](#ApiClient.Pinch.GetPos2XUnit "Link to this definition")  
Returns the unit of the first coordinate of second finger.

Returns:  Unit of second finger’s x-coordinate

Return type:  str

GetPos2Y()[¶](#ApiClient.Pinch.GetPos2Y "Link to this definition")  
Returns the value of the second coordinate of second finger.

Returns:  Value of second finger’s y-coordinate

Return type:  str

GetPos2YUnit()[¶](#ApiClient.Pinch.GetPos2YUnit "Link to this definition")  
Returns the unit of the second coordinate of second finger.

Returns:  Unit of second finger’s y-coordinate

Return type:  str

GetScaleFactor()[¶](#ApiClient.Pinch.GetScaleFactor "Link to this definition")  
Returns the scaling factor of gesture.

Returns:  Scale factor

Return type:  str

SetPinchDuration(*expr*, *unit='s'*)[¶](#ApiClient.Pinch.SetPinchDuration "Link to this definition")  
Sets the pinch duration.

Parameters:  - **expr** (*str*) – Pinch duration

- **unit** (*str*) – unit of duration, milliseconds ‘ms’ or seconds ‘s’

SetPos1X(*expr*, *unit='px'*)[¶](#ApiClient.Pinch.SetPos1X "Link to this definition")  
Sets first coordinate of first finger.

Parameters:  - **expr** (*str*) – x-coordinate of first finger as expression or numeric value

- **unit** (*str*) – unit of x-coordinate, absolute ‘px’ or relative ‘%’

SetPos1Y(*expr*, *unit='px'*)[¶](#ApiClient.Pinch.SetPos1Y "Link to this definition")  
Sets second coordinate of first finger.

Parameters:  - **expr** (*str*) – y-coordinate of first finger as expression string or numeric value

- **unit** (*str*) – unit of y-coordinate, absolute ‘px’ or relative ‘%’

SetPos2X(*expr*, *unit='px'*)[¶](#ApiClient.Pinch.SetPos2X "Link to this definition")  
Sets first coordinate of second finger.

Parameters:  - **expr** (*str*) – x-coordinate of second finger as expression or numeric value

- **unit** (*str*) – unit of x-coordinate, absolute ‘px’ or relative ‘%’

SetPos2Y(*expr*, *unit='px'*)[¶](#ApiClient.Pinch.SetPos2Y "Link to this definition")  
Sets second coordinate of second finger.

Parameters:  - **expr** (*str*) – y-coordinate of second finger as expression string or numeric value

- **unit** (*str*) – unit of y-coordinate, absolute ‘px’ or relative ‘%’

SetScaleFactor(*expr*)[¶](#ApiClient.Pinch.SetScaleFactor "Link to this definition")  
Sets the scaling factor of gesture

Parameters:  **expr** (*str*) – Scaling factor

## Rotate[¶](#rotate "Link to this heading")

*class* Rotate[¶](#ApiClient.Rotate "Link to this definition")  
Base class

[`TouchInputAction`](TestStepApi.md#ApiClient.TouchInputAction "ApiClient.TouchInputAction")

Returned by

- [`TouchInputApi.CreateRotate`](#ApiClient.TouchInputApi.CreateRotate "ApiClient.TouchInputApi.CreateRotate")

Clone()[¶](#ApiClient.Rotate.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`Rotate`](#ApiClient.Rotate "ApiClient.Rotate")

GetName()[¶](#ApiClient.Rotate.GetName "Link to this definition")  
Returns the name of the touch input action

Returns:  The name of the touch input action

Return type:  str

GetPos1X()[¶](#ApiClient.Rotate.GetPos1X "Link to this definition")  
Returns the value of the first coordinate of first finger.

Returns:  Value of first finger’s x-coordinate

Return type:  str

GetPos1XUnit()[¶](#ApiClient.Rotate.GetPos1XUnit "Link to this definition")  
Returns the unit of the first coordinate of first finger.

Returns:  Unit of first finger’s x-coordinate

Return type:  str

GetPos1Y()[¶](#ApiClient.Rotate.GetPos1Y "Link to this definition")  
Returns the value of the seconed coordinate of first finger.

Returns:  Value of first finger’s y-coordinate

Return type:  str

GetPos1YUnit()[¶](#ApiClient.Rotate.GetPos1YUnit "Link to this definition")  
Returns the unit of the seconed coordinate of first finger.

Returns:  Unit of first finger’s y-coordinate

Return type:  str

GetPos2X()[¶](#ApiClient.Rotate.GetPos2X "Link to this definition")  
Returns the value of the first coordinate of second finger.

Returns:  Value of second finger’s x-coordinate

Return type:  str

GetPos2XUnit()[¶](#ApiClient.Rotate.GetPos2XUnit "Link to this definition")  
Returns the unit of the first coordinate of second finger.

Returns:  Unit of second finger’s x-coordinate

Return type:  str

GetPos2Y()[¶](#ApiClient.Rotate.GetPos2Y "Link to this definition")  
Returns the value of the second coordinate of second finger.

Returns:  Value of second finger’s y-coordinate

Return type:  str

GetPos2YUnit()[¶](#ApiClient.Rotate.GetPos2YUnit "Link to this definition")  
Returns the unit of the second coordinate of second finger.

Returns:  Unit of second finger’s y-coordinate

Return type:  str

GetRotationAngle()[¶](#ApiClient.Rotate.GetRotationAngle "Link to this definition")  
Returns the value of the rotation angle.

Returns:  Value of rotation angle

Return type:  str

GetRotationAngleUnit()[¶](#ApiClient.Rotate.GetRotationAngleUnit "Link to this definition")  
Returns the unit of the rotation angle.

Returns:  Unit of rotation angle

Return type:  str

GetRotationDuration()[¶](#ApiClient.Rotate.GetRotationDuration "Link to this definition")  
Returns the value of the rotation duration.

Returns:  Value of rotation duration

Return type:  str

GetRotationDurationUnit()[¶](#ApiClient.Rotate.GetRotationDurationUnit "Link to this definition")  
Returns the unit of the rotation duration.

Returns:  Unit of rotation duration

Return type:  str

SetPos1X(*expr*, *unit='px'*)[¶](#ApiClient.Rotate.SetPos1X "Link to this definition")  
Sets first coordinate of first finger.

Parameters:  - **expr** (*str*) – x-coordinate of first finger as expression or numeric value

- **unit** (*str*) – unit of x-coordinate, absolute ‘px’ or relative ‘%’

SetPos1Y(*expr*, *unit='px'*)[¶](#ApiClient.Rotate.SetPos1Y "Link to this definition")  
Sets second coordinate of first finger.

Parameters:  - **expr** (*str*) – y-coordinate of first finger as expression string or numeric value

- **unit** (*str*) – unit of y-coordinate, absolute ‘px’ or relative ‘%’

SetPos2X(*expr*, *unit='px'*)[¶](#ApiClient.Rotate.SetPos2X "Link to this definition")  
Sets first coordinate of second finger.

Parameters:  - **expr** (*str*) – x-coordinate of second finger as expression or numeric value

- **unit** (*str*) – unit of x-coordinate, absolute ‘px’ or relative ‘%’

SetPos2Y(*expr*, *unit='px'*)[¶](#ApiClient.Rotate.SetPos2Y "Link to this definition")  
Sets second coordinate of second finger.

Parameters:  - **expr** (*str*) – y-coordinate of second finger as expression string or numeric value

- **unit** (*str*) – unit of y-coordinate, absolute ‘px’ or relative ‘%’

SetRotationAngle(*expr*, *unit='deg'*)[¶](#ApiClient.Rotate.SetRotationAngle "Link to this definition")  
Sets the rotation angle.

Parameters:  - **expr** (*str*) – Rotation angle

- **unit** (*str*) – unit of angle, degree ‘deg’ or radiant ‘rad’

SetRotationDuration(*expr*, *unit='s'*)[¶](#ApiClient.Rotate.SetRotationDuration "Link to this definition")  
Sets the rotation duration.

Parameters:  - **expr** (*str*) – Rotation duration

- **unit** (*str*) – unit of duration, milliseconds ‘ms’ or seconds ‘s’

## Swipe[¶](#swipe "Link to this heading")

*class* Swipe[¶](#ApiClient.Swipe "Link to this definition")  
Base class

[`TouchInputAction`](TestStepApi.md#ApiClient.TouchInputAction "ApiClient.TouchInputAction")

Returned by

- [`TouchInputApi.CreateSwipe`](#ApiClient.TouchInputApi.CreateSwipe "ApiClient.TouchInputApi.CreateSwipe")

Clone()[¶](#ApiClient.Swipe.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`Swipe`](#ApiClient.Swipe "ApiClient.Swipe")

GetEndX()[¶](#ApiClient.Swipe.GetEndX "Link to this definition")  
Returns the value of the first coordinate of the final position.

Returns:  Value of x-coordinate

Return type:  str

GetEndXUnit()[¶](#ApiClient.Swipe.GetEndXUnit "Link to this definition")  
Returns the unit of the first coordinate of the final position.

Returns:  Unit of x-coordinate

Return type:  str

GetEndY()[¶](#ApiClient.Swipe.GetEndY "Link to this definition")  
Returns the value of the second coordinate of the final position.

Returns:  Value of y-coordinate

Return type:  str

GetEndYUnit()[¶](#ApiClient.Swipe.GetEndYUnit "Link to this definition")  
Returns the unit of the second coordinate of the final position.

Returns:  Unit of y-coordinate

Return type:  str

GetName()[¶](#ApiClient.Swipe.GetName "Link to this definition")  
Returns the name of the touch input action

Returns:  The name of the touch input action

Return type:  str

GetStartX()[¶](#ApiClient.Swipe.GetStartX "Link to this definition")  
Returns the value of the first coordinate of the starting position.

Returns:  Value of x-coordinate

Return type:  str

GetStartXUnit()[¶](#ApiClient.Swipe.GetStartXUnit "Link to this definition")  
Returns the unit of the first coordinate of the starting position.

Returns:  Unit of x-coordinate

Return type:  str

GetStartY()[¶](#ApiClient.Swipe.GetStartY "Link to this definition")  
Returns the value of the second coordinate of the starting position.

Returns:  Value of y-coordinate

Return type:  str

GetStartYUnit()[¶](#ApiClient.Swipe.GetStartYUnit "Link to this definition")  
Returns the unit of the second coordinate of the starting position.

Returns:  Unit of y-coordinate

Return type:  str

GetSwipeDuration()[¶](#ApiClient.Swipe.GetSwipeDuration "Link to this definition")  
Returns the value of the swipe duration.

Returns:  Swipe duration

Return type:  str

GetSwipeDurationUnit()[¶](#ApiClient.Swipe.GetSwipeDurationUnit "Link to this definition")  
Returns the unit of the swipe duration.

Returns:  Swipe duration

Return type:  str

SetEndX(*expr*, *unit='px'*)[¶](#ApiClient.Swipe.SetEndX "Link to this definition")  
Sets first coordinate of the final position.

Parameters:  - **expr** (*str*) – expression for x-coordinate of position

- **unit** (*str*) – unit of x-coordinate, absolute ‘px’ or relative ‘%’

SetEndY(*expr*, *unit='px'*)[¶](#ApiClient.Swipe.SetEndY "Link to this definition")  
Sets second coordinate of the final position.

Parameters:  - **expr** (*str*) – expression for y-coordinate of position

- **unit** (*str*) – unit of y-coordinate, absolute ‘px’ or relative ‘%’

SetStartX(*expr*, *unit='px'*)[¶](#ApiClient.Swipe.SetStartX "Link to this definition")  
Sets first coordinate of the starting position.

Parameters:  - **expr** (*str*) – expression for x-coordinate of position

- **unit** (*str*) – unit of x-coordinate, absolute ‘px’ or relative ‘%’

SetStartY(*expr*, *unit='px'*)[¶](#ApiClient.Swipe.SetStartY "Link to this definition")  
Sets second coordinate of the starting position.

Parameters:  - **expr** (*str*) – expression for y-coordinate of position

- **unit** (*str*) – unit of y-coordinate, absolute ‘px’ or relative ‘%’

SetSwipeDuration(*expr*, *unit='s'*)[¶](#ApiClient.Swipe.SetSwipeDuration "Link to this definition")  
Sets the swipe duration.

Parameters:  - **expr** (*str*) – Swipe duration

- **unit** (*str*) – unit of duration, milliseconds ‘ms’ or seconds ‘s’

## Tap[¶](#tap "Link to this heading")

*class* Tap[¶](#ApiClient.Tap "Link to this definition")  
Base class

[`TouchInputAction`](TestStepApi.md#ApiClient.TouchInputAction "ApiClient.TouchInputAction")

Returned by

- [`TouchInputApi.CreateTap`](#ApiClient.TouchInputApi.CreateTap "ApiClient.TouchInputApi.CreateTap")

Clone()[¶](#ApiClient.Tap.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`Tap`](#ApiClient.Tap "ApiClient.Tap")

GetName()[¶](#ApiClient.Tap.GetName "Link to this definition")  
Returns the name of the touch input action

Returns:  The name of the touch input action

Return type:  str

GetPosX()[¶](#ApiClient.Tap.GetPosX "Link to this definition")  
Returns value of the first coordinate.

Returns:  Value of x-coordinate

Return type:  str

GetPosXUnit()[¶](#ApiClient.Tap.GetPosXUnit "Link to this definition")  
Returns unit of the first coordinate.

Returns:  Unit of x-coordinate

Return type:  str

GetPosY()[¶](#ApiClient.Tap.GetPosY "Link to this definition")  
Returns value of the second coordinate.

Returns:  Value of y-coordinate

Return type:  str

GetPosYUnit()[¶](#ApiClient.Tap.GetPosYUnit "Link to this definition")  
Returns unit of the second coordinate.

Returns:  Unit of y-coordinate

Return type:  str

SetPosX(*expr*, *unit='px'*)[¶](#ApiClient.Tap.SetPosX "Link to this definition")  
Sets first coordinate of position.

Parameters:  - **expr** (*str*) – expression for x-coordinate of position

- **unit** (*str*) – unit of x-coordinate, absolute ‘px’ or relative ‘%’

SetPosY(*expr*, *unit='px'*)[¶](#ApiClient.Tap.SetPosY "Link to this definition")  
Sets second coordinate of position.

Parameters:  - **expr** (*str*) – expression for y-coordinate of position

- **unit** (*str*) – unit of y-coordinate, absolute ‘px’ or relative ‘%’
