# User Tool API[¶](#user-tool-api "Link to this heading")

## UserTool[¶](#module-tts.core.toolingFramework.userTool.interfaces.UserTool "Link to this heading")

*class* UserTool[¶](#tts.core.toolingFramework.userTool.interfaces.UserTool.UserTool "Link to this definition")  
This class describes the interface of a user tool.

In order for ecu.test to recognize a class as a user tool, the class must meet the requirements of this interface. In addition, the `MODULE_TYPE` must be set to `USER_TOOL`.

    import ...

    MODULE_TYPE = 'USER_TOOL'

    class UserTool:
        def __init__(self, properties: dict[str, str | bool]) -> None:
            ...

`\_\_init\_\_`(*properties*)[¶](#tts.core.toolingFramework.userTool.interfaces.UserTool.UserTool.__init__ "Link to this definition")  
Parameters:  **properties** (*dict[str,* *str* *|* *bool]*) – Dictionary with the properties from the test bench configuration for this tool and the configured values. The possible properties are defined by the return value of the [`GetProperties()`](#tts.core.toolingFramework.userTool.interfaces.UserTool.UserTool.GetProperties "tts.core.toolingFramework.userTool.interfaces.UserTool.UserTool.GetProperties") method.

*classmethod* GetToolName()[¶](#tts.core.toolingFramework.userTool.interfaces.UserTool.UserTool.GetToolName "Link to this definition")  
Returns:  The name of the tool. This name is displayed in the test bench configuration.

Return type:  str

*classmethod* IsInstalled()[¶](#tts.core.toolingFramework.userTool.interfaces.UserTool.UserTool.IsInstalled "Link to this definition")  
*Optional (does not have to be implemented)*

Checks whether the tool to be connected is installed on the system. If not implemented, the tool will always be considered installed.

Is called when a new local tool host is created in the test bench configuration. If the tool is installed, the user tool is displayed in the test bench configuration, otherwise not.

If the user tool does not connect to an external tool, it is safe to omit this method.

Returns:  True if the tool is installed, otherwise False.

Return type:  bool

*classmethod* GetPorts()[¶](#tts.core.toolingFramework.userTool.interfaces.UserTool.UserTool.GetPorts "Link to this definition")  
*Optional (does not have to be implemented)*

Provides a list of ports offered by this user tool. These ports can be selected in the test bench configuration when a new port is created for the user tool.

Port classes must fulfill a certain interface in order to be accepted by ecu.test.

Returns:  List of supported port classes.

Return type:  list[type[[UserPort](#tts.core.toolingFramework.userTool.interfaces.UserPort.UserPort "tts.core.toolingFramework.userTool.interfaces.UserPort.UserPort")]]

*classmethod* GetProperties()[¶](#tts.core.toolingFramework.userTool.interfaces.UserTool.UserTool.GetProperties "Link to this definition")  
*Optional (does not have to be implemented)*

Properties of the tool. These properties can be configured in the test bench configuration. The configured properties are passed to the user tool when the configuration is started. Available property types are STRING, BOOL and CHOICE. Properties may be sorted into groups to improve visual separation in the test bench configuration.

Example:

    @classmethod
    def GetProperties(cls) -> dict[str, dict]:
        return {
            'Group 1': {
                'Option 1': {
                    'Description': 'This is Option 1',
                    'Type': 'STRING',
                    'Default': 'default value',
                },
                'Option 2': {
                    'Description': 'This is Option 2',
                    'Type': 'BOOL',
                    'Default': True,
                },
                'Option 3': {
                    'Description': 'This is Option 3',
                    'Type': 'CHOICE',
                    'Choices': ['c1', 'c2', 'c3'],
                    'Default': 'c2',
                },
            }
        }

The above example will generate the following properties:

![](../../_images/UserTool_GetProperties.png)

\

Returns:  Dictionary with properties of the user tool.

Return type:  dict[str, dict]

*classmethod* GetJobs()[¶](#tts.core.toolingFramework.userTool.interfaces.UserTool.UserTool.GetJobs "Link to this definition")  
*Optional (does not have to be implemented)*

Provides a list of methods that are offered in ecu.test as a tool job for this user tool.

Note

The properties of the tool job are generated using the docstring and the Python type hints of the method.

Example:

    @classmethod
    def GetJobs(cls) -> list[Callable]:
        return [cls.MyToolJob]

    def MyToolJob(self, param1: str, param2: int) -> bool:
        '''
        :param param1: description of param 1
        :param param2: description of param 2
        :return: description of the returned value
        '''
        return True

Returns:  List of job methods.

Return type:  list[Callable]

GetVersion()[¶](#tts.core.toolingFramework.userTool.interfaces.UserTool.UserTool.GetVersion "Link to this definition")  
Version of the external tool. This version will be documented in the test report.

Returns:  version

Return type:  str

IsBroken()[¶](#tts.core.toolingFramework.userTool.interfaces.UserTool.UserTool.IsBroken "Link to this definition")  
*Optional (does not have to be implemented)*

Indicates a broken tool state. Called before test execution and on configuration window update. Should return True if any of the external tools used by this user tool cannot be used anymore (e.g. connection lost, tool locked up).

Otherwise or if no external tool is used, False should be returned.

Returns:  True if tool is broken (not usable), otherwise False.

Return type:  bool

Dispose()[¶](#tts.core.toolingFramework.userTool.interfaces.UserTool.UserTool.Dispose "Link to this definition")  
*Optional (does not have to be implemented)*

Gracefully terminates the connection to the external tool and/or other shutdown sequences.

Is called when the configuration is stopped in ecu.test.

## UserPort[¶](#module-tts.core.toolingFramework.userTool.interfaces.UserPort "Link to this heading")

*class* UserPort[¶](#tts.core.toolingFramework.userTool.interfaces.UserPort.UserPort "Link to this definition")  
This class describes the interface of a user port. Classes that fulfill this interface can be used as port of a user tool.

`\_\_init\_\_`(*tool*, *properties*)[¶](#tts.core.toolingFramework.userTool.interfaces.UserPort.UserPort.__init__ "Link to this definition")  
Parameters:  - **tool** ([*UserTool*](#tts.core.toolingFramework.userTool.interfaces.UserTool.UserTool "tts.core.toolingFramework.userTool.interfaces.UserTool.UserTool")) – Tool providing this port. Can be used to query the properties of the tool, for example.

- **properties** (*dict[str,* *str* *|* *bool]*) – Dictionary with the properties from the testbench configuration for this port and the configured values. The possible properties are defined by the return value of the [`GetProperties()`](#tts.core.toolingFramework.userTool.interfaces.UserPort.UserPort.GetProperties "tts.core.toolingFramework.userTool.interfaces.UserPort.UserPort.GetProperties") method.

*classmethod* GetPortType()[¶](#tts.core.toolingFramework.userTool.interfaces.UserPort.UserPort.GetPortType "Link to this definition")  
Returns the type of the port. This type defines which interface the port must fulfill and therefore which range of functions it offers. Valid types are

> - BASE (must fulfill the [`UserPort`](#tts.core.toolingFramework.userTool.interfaces.UserPort.UserPort "tts.core.toolingFramework.userTool.interfaces.UserPort.UserPort") interface)
>
> - IMAGE (must fulfill the [`UserImagePort`](#tts.core.toolingFramework.userTool.interfaces.UserImagePort.UserImagePort "tts.core.toolingFramework.userTool.interfaces.UserImagePort.UserImagePort") interface)

Returns:  Type of the port.

Return type:  *Literal*[‘BASE’, ‘IMAGE’]

*classmethod* GetImplementationType()[¶](#tts.core.toolingFramework.userTool.interfaces.UserPort.UserPort.GetImplementationType "Link to this definition")  
*Optional (does not have to be implemented)*

Returns the implementation type of the port.

By setting an implementation type, several ports of the same type (see [`GetPortType()`](#tts.core.toolingFramework.userTool.interfaces.UserPort.UserPort.GetPortType "tts.core.toolingFramework.userTool.interfaces.UserPort.UserPort.GetPortType")) can be offered with different implementations.

Returns:  implementation type of the port

Return type:  str

*classmethod* GetProperties()[¶](#tts.core.toolingFramework.userTool.interfaces.UserPort.UserPort.GetProperties "Link to this definition")  
*Optional (does not have to be implemented)*

Properties of the port. These properties can be configured in the testbench configuration. The configured properties are passed to the user port when the configuration is started. Available property types are STRING, BOOL and CHOICE. Properties may be sorted into groups to improve visual separation in the test bench configuration.

Example:

    @classmethod
    def GetProperties(cls) -> dict[str, dict]:
        return {
            'Group 1': {
                'Option 1': {
                    'Description': 'This is Option 1',
                    'Type': 'STRING',
                    'Default': 'default value',
                },
                'Option 2': {
                    'Description': 'This is Option 2',
                    'Type': 'BOOL',
                    'Default': True,
                },
                'Option 3': {
                    'Description': 'This is Option 3',
                    'Type': 'CHOICE',
                    'Choices': ['c1', 'c2', 'c3'],
                    'Default': 'c2',
                },
            }
        }

The above example will generate the following properties:

![](../../_images/UserTool_GetProperties.png)

Returns:  Dictionary with properties of the user port.

Return type:  dict[str, dict]

*classmethod* GetJobs()[¶](#tts.core.toolingFramework.userTool.interfaces.UserPort.UserPort.GetJobs "Link to this definition")  
*Optional (does not have to be implemented)*

Provides a list of methods that are offered in ecu.test as a port job for this user port.

Note

The properties of the tool job are generated using the docstring and the Python type hints of the method.

Example:

    @classmethod
    def GetJobs(cls) -> list[Callable]:
        return [cls.MyPortJob]

    def MyPortJob(self, param1: str, param2: int) -> bool:
        '''
        :param param1: description of param 1
        :param param2: description of param 2
        :return: description of the returned value
        '''
        return True

Returns:  List of job methods.

Return type:  list[Callable]

IsBroken()[¶](#tts.core.toolingFramework.userTool.interfaces.UserPort.UserPort.IsBroken "Link to this definition")  
*Optional (does not have to be implemented)*

Optional method to indicate a broken port state. Called before test execution and on configuration window update. Should return True if any of the external tools used by this port cannot be used anymore (e.g. connection lost, tool locked up).

Otherwise or if no external tool is used, False should be returned.

Returns:  True if tool is broken (not usable), otherwise False.

Return type:  bool

Dispose()[¶](#tts.core.toolingFramework.userTool.interfaces.UserPort.UserPort.Dispose "Link to this definition")  
*Optional (does not have to be implemented)*

Gracefully terminates the connection to the external tool and/or other shutdown sequences.

Is called when the configuration is stopped in ecu.test.

## UserImagePort[¶](#module-tts.core.toolingFramework.userTool.interfaces.UserImagePort "Link to this heading")

*class* UserImagePort[¶](#tts.core.toolingFramework.userTool.interfaces.UserImagePort.UserImagePort "Link to this definition")  
Bases: [`UserPort`](#tts.core.toolingFramework.userTool.interfaces.UserPort.UserPort "tts.core.toolingFramework.userTool.interfaces.UserPort.UserPort")

ReadImage()[¶](#tts.core.toolingFramework.userTool.interfaces.UserImagePort.UserImagePort.ReadImage "Link to this definition")  
Reads an image from e.g. an external source and makes it available as a numpy array.

Returns:  Tuple of two numpy arrays. The first contains the image data, the second contains alpha values or None. Note that if alpha values are returned, the array must have the same size as the image data array.

Return type:  tuple[NDArray[Any], NDArray[Any] | None]

GetTouchInput()[¶](#tts.core.toolingFramework.userTool.interfaces.UserImagePort.UserImagePort.GetTouchInput "Link to this definition")  
*Optional (does not have to be implemented)*

Returns an object that provides the interface for processing touch inputs. Implementing this method indicates that this port supports touch input test steps. Can be omitted if the port does not support touch input.

Returns:  Object that fulfills the [`UserTouchInput`](#tts.core.toolingFramework.userTool.interfaces.UserTouchInput.UserTouchInput "tts.core.toolingFramework.userTool.interfaces.UserTouchInput.UserTouchInput") interface.

Return type:  [UserTouchInput](#tts.core.toolingFramework.userTool.interfaces.UserTouchInput.UserTouchInput "tts.core.toolingFramework.userTool.interfaces.UserTouchInput.UserTouchInput")

StartRecording(*recordingId*)[¶](#tts.core.toolingFramework.userTool.interfaces.UserImagePort.UserImagePort.StartRecording "Link to this definition")  
*Optional (does not have to be implemented)*

Starts a recording. For recording to work, both [`StartRecording()`](#tts.core.toolingFramework.userTool.interfaces.UserImagePort.UserImagePort.StartRecording "tts.core.toolingFramework.userTool.interfaces.UserImagePort.UserImagePort.StartRecording") and [`StopRecording()`](#tts.core.toolingFramework.userTool.interfaces.UserImagePort.UserImagePort.StopRecording "tts.core.toolingFramework.userTool.interfaces.UserImagePort.UserImagePort.StopRecording") must be implemented.

Example:

    def StartRecording(self, recordingId: str) -> None:
        # Start recording within the user tool
        self._myUserToolApi.StartRecording()

Parameters:  **recordingId** (*str*) – Identifier for the recording to be started. Correlates with a recording group in ecu.test.

StopRecording(*recordingId*)[¶](#tts.core.toolingFramework.userTool.interfaces.UserImagePort.UserImagePort.StopRecording "Link to this definition")  
*Optional (does not have to be implemented)*

Stops the recording for the given recordingId. Should return the path of the created recording file. For recording to work, both [`StartRecording()`](#tts.core.toolingFramework.userTool.interfaces.UserImagePort.UserImagePort.StartRecording "tts.core.toolingFramework.userTool.interfaces.UserImagePort.UserImagePort.StartRecording") and [`StopRecording()`](#tts.core.toolingFramework.userTool.interfaces.UserImagePort.UserImagePort.StopRecording "tts.core.toolingFramework.userTool.interfaces.UserImagePort.UserImagePort.StopRecording") must be implemented.

Example:

    def StopRecording(self, recordingId: str) -> str:
        # Stop the recording on your tool
        recordingFilePath = self._myUserToolApi.StopRecording()
        return recordingFilePath

Parameters:  **recordingId** (*str*) – Identifier for the recording to be stopped. Matches with the recordingId the recording was previously started for.

Returns:  Path to a video file

Return type:  str

## UserTouchInput[¶](#module-tts.core.toolingFramework.userTool.interfaces.UserTouchInput "Link to this heading")

*class* UserTouchInput[¶](#tts.core.toolingFramework.userTool.interfaces.UserTouchInput.UserTouchInput "Link to this definition")  
Describes the interface for touch inputs.

A class that fulfills this interface can be used to extend a [`UserImagePort`](#tts.core.toolingFramework.userTool.interfaces.UserImagePort.UserImagePort "tts.core.toolingFramework.userTool.interfaces.UserImagePort.UserImagePort") to allow touch inputs.

GetScreenResolution()[¶](#tts.core.toolingFramework.userTool.interfaces.UserTouchInput.UserTouchInput.GetScreenResolution "Link to this definition")  
Returns the resolution of the screen.

Returns:  Width and height of the screen (width, height).

Return type:  tuple[int, int]

PerformTap(*action*)[¶](#tts.core.toolingFramework.userTool.interfaces.UserTouchInput.UserTouchInput.PerformTap "Link to this definition")  
*Optional (does not have to be implemented)*

Performs the “Tap” action. Implementing this method indicates that the “Tap” action is supported by this port.

Parameters:  **action** (*dict[str,* *int* *|* *float]*) –

Dictionary that contains parameters for the “Tap” action:

- `posX`: x coordinate in pixels

- `posY`: y coordinate in pixels

PerformHold(*action*)[¶](#tts.core.toolingFramework.userTool.interfaces.UserTouchInput.UserTouchInput.PerformHold "Link to this definition")  
*Optional (does not have to be implemented)*

Performs the “Hold” action. Implementing this method indicates that the “Hold” action is supported by this port.

Parameters:  **action** (*dict[str,* *int* *|* *float]*) –

Dictionary that contains parameters for the “Hold” action:

- `posX`: x coordinate in pixels

- `posY`: y coordinate in pixels

- `holdDuration`: hold duration in seconds

PerformMultiTap(*action*)[¶](#tts.core.toolingFramework.userTool.interfaces.UserTouchInput.UserTouchInput.PerformMultiTap "Link to this definition")  
*Optional (does not have to be implemented)*

Performs the “MultiTap” action. Implementing this method indicates that the “MultiTap” action is supported by this port.

Parameters:  **action** (*dict[str,* *int* *|* *float]*) –

Dictionary that contains parameters for the “MultiTap” action:

- `posX`: x coordinate in pixels

- `posY`: y coordinate in pixels

- `count`: number of consecutive taps

- `interval`: interval of consecutive taps in seconds

PerformSwipe(*action*)[¶](#tts.core.toolingFramework.userTool.interfaces.UserTouchInput.UserTouchInput.PerformSwipe "Link to this definition")  
*Optional (does not have to be implemented)*

Performs the “Swipe” action. Implementing this method indicates that the “Swipe” action is supported by this port.

Parameters:  **action** (*dict[str,* *int* *|* *float]*) –

Dictionary that contains parameters for the “Swipe” action:

- `posX`: x coordinate of the start position in pixels

- `posY`: y coordinate of the start position in pixels

- `swipedPosX`: x coordinate of the end position in pixels

- `swipedPosY`: y coordinate of the end position in pixels

- `swipeDuration`: duration of the swipe movement in seconds

PerformMultiSwipe(*action*)[¶](#tts.core.toolingFramework.userTool.interfaces.UserTouchInput.UserTouchInput.PerformMultiSwipe "Link to this definition")  
*Optional (does not have to be implemented)*

Performs the “MultiSwipe” action. Implementing this method indicates that the “MultiSwipe” action is supported by this port.

Parameters:  **action** (*dict[str,* *int* *|* *float]*) –

Dictionary that contains parameters for the “MultiSwipe” action:

- `posX`: x coordinate of the start position in pixels

- `posY`: y coordinate of the start position in pixels

- `swipedPosX`: x coordinate of the end position in pixels

- `swipedPosY`: y coordinate of the end position in pixels

- `swipeDuration`: duration of the swipe movement in seconds

- `fingerCount`: number of parallel fingers that perform the action

- `fingerDistance`: distance between two parallel fingers

PerformHoldAndSwipe(*action*)[¶](#tts.core.toolingFramework.userTool.interfaces.UserTouchInput.UserTouchInput.PerformHoldAndSwipe "Link to this definition")  
*Optional (does not have to be implemented)*

Performs the “HoldAndSwipe” action. Implementing this method indicates that the “HoldAndSwipe” action is supported by this port.

Parameters:  **action** (*dict[str,* *int* *|* *float]*) –

Dictionary that contains parameters for the “HoldAndSwipe” action:

- `posX`: x coordinate of the start position in pixels

- `posY`: y coordinate of the start position in pixels

- `swipedPosX`: x coordinate of the end position in pixels

- `swipedPosY`: y coordinate of the end position in pixels

- `holdDuration`: duration of the initial hold in seconds

- `swipeDuration`: duration of the swipe movement in seconds

PerformPinch(*action*)[¶](#tts.core.toolingFramework.userTool.interfaces.UserTouchInput.UserTouchInput.PerformPinch "Link to this definition")  
*Optional (does not have to be implemented)*

Performs the “Pinch” action. Implementing this method indicates that the “Pinch” action is supported by this port.

Parameters:  **action** (*dict[str,* *int* *|* *float]*) –

Dictionary that contains parameters for the “Pinch” action:

- `finger1PosX`: x coordinate of the first finger in pixels

- `finger1PosY`: Y coordinate of the first finger in pixels

- `finger2PosX`: X coordinate of the second finger in pixels

- `finger2PosY`: Y coordinate of the second finger in pixels

- `pinchDuration`: duration of the pinch movement in seconds

- `scaleFactor`: a factor \< 1 means that the fingers are moving towards each other (zoom out) and a factor \> 1 means that the fingers are moving away from each other (zoom in).

PerformRotate(*action*)[¶](#tts.core.toolingFramework.userTool.interfaces.UserTouchInput.UserTouchInput.PerformRotate "Link to this definition")  
*Optional (does not have to be implemented)*

Performs the “Rotate” action. Implementing this method indicates that the “Rotate” action is supported by this port.

Parameters:  **action** (*dict[str,* *int* *|* *float]*) –

Dictionary that contains parameters for the “Rotate” action:

- `finger1PosX`: x coordinate of the first finger in pixels

- `finger1PosY`: Y coordinate of the first finger in pixels

- `finger2PosX`: X coordinate of the second finger in pixels

- `finger2PosY`: Y coordinate of the second finger in pixels

- `rotationDuration`: duration of the rotate movement in seconds

- `rotationAngle`: rotation angle in degrees
