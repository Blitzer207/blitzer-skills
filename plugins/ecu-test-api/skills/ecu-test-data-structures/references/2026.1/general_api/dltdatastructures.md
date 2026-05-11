[ Internal APIs ](api.md)

[ Advanced operations of package variable types ](variabledatastructures.md)

[ Advanced properties of bus-related objects ](busdatastructures.md)

[ Bus related objects of trace analysis ](busdatastructuresTraceanalysis.md)

[ Advanced properties of diagnostics-related objects ](diagdatastructures.md)

[ Diagnostics related objects of trace analysis ](diagdatastructuresTraceanalysis.md)

[ Advanced properties of media-related objects ](mediadatastructures.md)

Advanced properties of DLT logging-related objects [ Advanced properties of DLT logging-related objects ](#)

Advanced properties of DLT logging-related objects

- [ DLT message object ](#dlt-message-object)
  - [C DltMessage ](#tts.testModule.logging.logObjects.DltMessage.DltMessage)
    - [A messageCounter ](#tts.testModule.logging.logObjects.DltMessage.DltMessage.messageCounter)
    - [A ecuId ](#tts.testModule.logging.logObjects.DltMessage.DltMessage.ecuId)
    - [A sessionId ](#tts.testModule.logging.logObjects.DltMessage.DltMessage.sessionId)
    - [A messageTimestamp ](#tts.testModule.logging.logObjects.DltMessage.DltMessage.messageTimestamp)
    - [A verbose ](#tts.testModule.logging.logObjects.DltMessage.DltMessage.verbose)
    - [A applicationId ](#tts.testModule.logging.logObjects.DltMessage.DltMessage.applicationId)
    - [A contextId ](#tts.testModule.logging.logObjects.DltMessage.DltMessage.contextId)
    - [M GetIndex ](#tts.testModule.logging.logObjects.DltMessage.DltMessage.GetIndex)
    - [M GetAbsoluteTimeString ](#tts.testModule.logging.logObjects.DltMessage.DltMessage.GetAbsoluteTimeString)
    - [M GetMessageTimestamp ](#tts.testModule.logging.logObjects.DltMessage.DltMessage.GetMessageTimestamp)
    - [M GetArgumentCount ](#tts.testModule.logging.logObjects.DltMessage.DltMessage.GetArgumentCount)
    - [M GetArgumentsString ](#tts.testModule.logging.logObjects.DltMessage.DltMessage.GetArgumentsString)
    - [M HasArgument ](#tts.testModule.logging.logObjects.DltMessage.DltMessage.HasArgument)
    - [M `\_\_getitem\_\_` ](#tts.testModule.logging.logObjects.DltMessage.DltMessage.__getitem__)
    - [M get ](#tts.testModule.logging.logObjects.DltMessage.DltMessage.get)
    - [M GetArgumentValue ](#tts.testModule.logging.logObjects.DltMessage.DltMessage.GetArgumentValue)
    - [M GetArgumentUnit ](#tts.testModule.logging.logObjects.DltMessage.DltMessage.GetArgumentUnit)
    - [M GetArgumentName ](#tts.testModule.logging.logObjects.DltMessage.DltMessage.GetArgumentName)
    - [M GetLogLevel ](#tts.testModule.logging.logObjects.DltMessage.DltMessage.GetLogLevel)
    - [M GetMessageID ](#tts.testModule.logging.logObjects.DltMessage.DltMessage.GetMessageID)
    - [M GetPayloadBytes ](#tts.testModule.logging.logObjects.DltMessage.DltMessage.GetPayloadBytes)

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

Advanced properties of DLT logging-related objects

- [ DLT message object ](#dlt-message-object)
  - [C DltMessage ](#tts.testModule.logging.logObjects.DltMessage.DltMessage)
    - [A messageCounter ](#tts.testModule.logging.logObjects.DltMessage.DltMessage.messageCounter)
    - [A ecuId ](#tts.testModule.logging.logObjects.DltMessage.DltMessage.ecuId)
    - [A sessionId ](#tts.testModule.logging.logObjects.DltMessage.DltMessage.sessionId)
    - [A messageTimestamp ](#tts.testModule.logging.logObjects.DltMessage.DltMessage.messageTimestamp)
    - [A verbose ](#tts.testModule.logging.logObjects.DltMessage.DltMessage.verbose)
    - [A applicationId ](#tts.testModule.logging.logObjects.DltMessage.DltMessage.applicationId)
    - [A contextId ](#tts.testModule.logging.logObjects.DltMessage.DltMessage.contextId)
    - [M GetIndex ](#tts.testModule.logging.logObjects.DltMessage.DltMessage.GetIndex)
    - [M GetAbsoluteTimeString ](#tts.testModule.logging.logObjects.DltMessage.DltMessage.GetAbsoluteTimeString)
    - [M GetMessageTimestamp ](#tts.testModule.logging.logObjects.DltMessage.DltMessage.GetMessageTimestamp)
    - [M GetArgumentCount ](#tts.testModule.logging.logObjects.DltMessage.DltMessage.GetArgumentCount)
    - [M GetArgumentsString ](#tts.testModule.logging.logObjects.DltMessage.DltMessage.GetArgumentsString)
    - [M HasArgument ](#tts.testModule.logging.logObjects.DltMessage.DltMessage.HasArgument)
    - [M `\_\_getitem\_\_` ](#tts.testModule.logging.logObjects.DltMessage.DltMessage.__getitem__)
    - [M get ](#tts.testModule.logging.logObjects.DltMessage.DltMessage.get)
    - [M GetArgumentValue ](#tts.testModule.logging.logObjects.DltMessage.DltMessage.GetArgumentValue)
    - [M GetArgumentUnit ](#tts.testModule.logging.logObjects.DltMessage.DltMessage.GetArgumentUnit)
    - [M GetArgumentName ](#tts.testModule.logging.logObjects.DltMessage.DltMessage.GetArgumentName)
    - [M GetLogLevel ](#tts.testModule.logging.logObjects.DltMessage.DltMessage.GetLogLevel)
    - [M GetMessageID ](#tts.testModule.logging.logObjects.DltMessage.DltMessage.GetMessageID)
    - [M GetPayloadBytes ](#tts.testModule.logging.logObjects.DltMessage.DltMessage.GetPayloadBytes)

# Advanced properties of DLT logging-related objects[¶](#advanced-properties-of-dlt-logging-related-objects "Link to this heading")

## DLT message object[¶](#dlt-message-object "Link to this heading")

*class* DltMessage[¶](#tts.testModule.logging.logObjects.DltMessage.DltMessage "Link to this definition")  
DltMessage objects represent DLT messages. For non-verbose DLT messages, loading an appropriate Fibex file and using their individual signals is recommended. For verbose DLT messages, you can use the attributes described here to query information about the DLT message.

messageCounter = `None`[¶](#tts.testModule.logging.logObjects.DltMessage.DltMessage.messageCounter "Link to this definition")  
Type:  int|None

ecuId = `None`[¶](#tts.testModule.logging.logObjects.DltMessage.DltMessage.ecuId "Link to this definition")  
Type:  str|None

sessionId = `None`[¶](#tts.testModule.logging.logObjects.DltMessage.DltMessage.sessionId "Link to this definition")  
Type:  int|None

messageTimestamp = `None`[¶](#tts.testModule.logging.logObjects.DltMessage.DltMessage.messageTimestamp "Link to this definition")  
in 0.1ms increments.

See also [`GetMessageTimestamp()`](#tts.testModule.logging.logObjects.DltMessage.DltMessage.GetMessageTimestamp "tts.testModule.logging.logObjects.DltMessage.DltMessage.GetMessageTimestamp (Python method) — Returns the message timestamp if it is part of the message. This timestamp is set by the sending ECU.")

Type:  int|None

verbose = `False`[¶](#tts.testModule.logging.logObjects.DltMessage.DltMessage.verbose "Link to this definition")  
Type:  bool

applicationId = `None`[¶](#tts.testModule.logging.logObjects.DltMessage.DltMessage.applicationId "Link to this definition")  
Type:  str|None

contextId = `None`[¶](#tts.testModule.logging.logObjects.DltMessage.DltMessage.contextId "Link to this definition")  
Type:  str|None

GetIndex()[¶](#tts.testModule.logging.logObjects.DltMessage.DltMessage.GetIndex "Link to this definition")  
Returns the zero-based storage index of the message. The index indicates the sequential position in a DLT file.

Note:  
The index is determined by the DLT file parser and is not part of the message itself. Therefore, the index is only valid for messages read from DLT files!

Returns:  The index or None if the message is not read from a DLT file.

Return type:  Optional[int]

GetAbsoluteTimeString(*[utc](#tts.testModule.logging.logObjects.DltMessage.DltMessage.GetAbsoluteTimeString.utc "tts.testModule.logging.logObjects.DltMessage.DltMessage.GetAbsoluteTimeString.utc (Python parameter) — If True, the UTC time is returned.")=`True`*)[¶](#tts.testModule.logging.logObjects.DltMessage.DltMessage.GetAbsoluteTimeString "Link to this definition")  
Returns the ISO format representation of the absolute timestamp when the message was received.

Note:  
The absolute timestamp is only available for messages read from DLT files and is independent from the message timestamp.

Example  
‘2019-05-18T15:17:08.132263+00:00’ if utc=True; otherwise, ‘2019-05-18T15:19:08.132263+02:00’ if the local timezone is UTC+2, for example.

Parameters:  utc : bool[¶](#tts.testModule.logging.logObjects.DltMessage.DltMessage.GetAbsoluteTimeString.utc "Permalink to this definition")  
If True, the UTC time is returned. Otherwise, the local time is returned. In both cases. The returned ISO string does include the timezone offset.

Returns:  The absolute timestamp as ISO string. None if not available.

Return type:  Optional[str]

GetMessageTimestamp()[¶](#tts.testModule.logging.logObjects.DltMessage.DltMessage.GetMessageTimestamp "Link to this definition")  
Returns the message timestamp if it is part of the message. This timestamp is set by the sending ECU.

Returns:  Timestamp in seconds

Return type:  Optional[float]

GetArgumentCount()[¶](#tts.testModule.logging.logObjects.DltMessage.DltMessage.GetArgumentCount "Link to this definition")  
(**verbose**) Returns the Number of arguments of this DLT message.

Returns:  Number of arguments of this DLT message.

Return type:  int

GetArgumentsString(*[includeArgNames](#tts.testModule.logging.logObjects.DltMessage.DltMessage.GetArgumentsString.includeArgNames "tts.testModule.logging.logObjects.DltMessage.DltMessage.GetArgumentsString.includeArgNames (Python parameter) — Specifies whether argument names are to be included.")=`True`*)[¶](#tts.testModule.logging.logObjects.DltMessage.DltMessage.GetArgumentsString "Link to this definition")  
(**verbose**) Returns a string representation of all arguments.

Parameters:  includeArgNames : bool[¶](#tts.testModule.logging.logObjects.DltMessage.DltMessage.GetArgumentsString.includeArgNames "Permalink to this definition")  
Specifies whether argument names are to be included.

Returns:  A string representing all arguments

Return type:  str

HasArgument(*[argName](#tts.testModule.logging.logObjects.DltMessage.DltMessage.HasArgument.argName "tts.testModule.logging.logObjects.DltMessage.DltMessage.HasArgument.argName (Python parameter) — Name/index of the argument to check for existence")*)[¶](#tts.testModule.logging.logObjects.DltMessage.DltMessage.HasArgument "Link to this definition")  
(**verbose**) Tests whether an argument of the given name/index exists.

Parameters:  argName : str|int[¶](#tts.testModule.logging.logObjects.DltMessage.DltMessage.HasArgument.argName "Permalink to this definition")  
Name/index of the argument to check for existence

Returns:  Whether an argument of the given name exists

Return type:  bool

`\_\_getitem\_\_`(*[key](#tts.testModule.logging.logObjects.DltMessage.DltMessage.__getitem__.key "tts.testModule.logging.logObjects.DltMessage.DltMessage.__getitem__.key (Python parameter) — name or position")*)[¶](#tts.testModule.logging.logObjects.DltMessage.DltMessage.__getitem__ "Link to this definition")  
(**verbose**) Arguments can be accessed by position via `dltMessageObj[idx]` or by name via `dltMessageObj[argName]`.

Complex values are currently not supported.

Parameters:  key : str|int[¶](#tts.testModule.logging.logObjects.DltMessage.DltMessage.__getitem__.key "Permalink to this definition")  
name or position

Returns:  The argument’s payload value. In case of a fixed-point number, the physical value.

Return type:  int|float|str

get(*[key](#tts.testModule.logging.logObjects.DltMessage.DltMessage.get.key "tts.testModule.logging.logObjects.DltMessage.DltMessage.get.key (Python parameter) — name or position")*, *[default](#tts.testModule.logging.logObjects.DltMessage.DltMessage.get.default "tts.testModule.logging.logObjects.DltMessage.DltMessage.get.default (Python parameter) — default value that should be returned if key does not exist")=`None`*)[¶](#tts.testModule.logging.logObjects.DltMessage.DltMessage.get "Link to this definition")  
(**verbose**) Gets an argument or the default value, if the name resp. position does not exist.

Parameters:  key : str|int[¶](#tts.testModule.logging.logObjects.DltMessage.DltMessage.get.key "Permalink to this definition")  
name or position

default : object[¶](#tts.testModule.logging.logObjects.DltMessage.DltMessage.get.default "Permalink to this definition")  
default value that should be returned if key does not exist

Returns:  The argument’s payload value. In case of a fixed-point number, the physical value.

Return type:  int|float|str|object

GetArgumentValue(*[argName](#tts.testModule.logging.logObjects.DltMessage.DltMessage.GetArgumentValue.argName "tts.testModule.logging.logObjects.DltMessage.DltMessage.GetArgumentValue.argName (Python parameter) — Name/index of the argument")*)[¶](#tts.testModule.logging.logObjects.DltMessage.DltMessage.GetArgumentValue "Link to this definition")  
(**verbose**) Returns the value of an argument.

Parameters:  argName : str|int[¶](#tts.testModule.logging.logObjects.DltMessage.DltMessage.GetArgumentValue.argName "Permalink to this definition")  
Name/index of the argument

Returns:  The argument’s payload value. In case of a fixed-point number, the physical value.

Return type:  int|float|str

Raises:  
- **KeyError** – argName is of type str and cannot be found.

- **IndexError** – argName is of type in and cannot be found.

GetArgumentUnit(*[argName](#tts.testModule.logging.logObjects.DltMessage.DltMessage.GetArgumentUnit.argName "tts.testModule.logging.logObjects.DltMessage.DltMessage.GetArgumentUnit.argName (Python parameter) — Name/index of the argument whose unit to determine")*)[¶](#tts.testModule.logging.logObjects.DltMessage.DltMessage.GetArgumentUnit "Link to this definition")  
(**verbose**) Determines the unit of an argument.

Parameters:  argName : str|int[¶](#tts.testModule.logging.logObjects.DltMessage.DltMessage.GetArgumentUnit.argName "Permalink to this definition")  
Name/index of the argument whose unit to determine

Returns:  Unit of the specified argument

Return type:  str

GetArgumentName(*[argIdx](#tts.testModule.logging.logObjects.DltMessage.DltMessage.GetArgumentName.argIdx "tts.testModule.logging.logObjects.DltMessage.DltMessage.GetArgumentName.argIdx (Python parameter) — Number/index (zero-based) of the argument")*)[¶](#tts.testModule.logging.logObjects.DltMessage.DltMessage.GetArgumentName "Link to this definition")  
(**verbose**) Determines the name of an argument.

Parameters:  argIdx : int[¶](#tts.testModule.logging.logObjects.DltMessage.DltMessage.GetArgumentName.argIdx "Permalink to this definition")  
Number/index (zero-based) of the argument

Returns:  Name of the specified argument

Return type:  str

GetLogLevel()[¶](#tts.testModule.logging.logObjects.DltMessage.DltMessage.GetLogLevel "Link to this definition")  
Returns the log level if the message is a DLT Log Message. Values:

- 0x1: DLT_LOG_FATAL (Fatal system error)

- 0x2: DLT_LOG_DLT_ERROR(Application error)

- 0x3: DLT_LOG_WARN(Correct behavior cannot be ensured)

- 0x4: DLT_LOGINFO(Message of LogLevel type “Information”)

- 0x5: DLT_LOG_DEBUG(Message of LogLevel type “Debug”)

- 0x6: DLT_LOG_VERBOSE(Message of LogLevel type “Verbose”)

- 0x7 - 0xF: Reserved

Return type:  Optional[int]

GetMessageID()[¶](#tts.testModule.logging.logObjects.DltMessage.DltMessage.GetMessageID "Link to this definition")  
(**non-verbose**) Returns the message ID of a message.

Returns:  The message ID. Value None for verbose messages.

Return type:  Optional[int]

GetPayloadBytes()[¶](#tts.testModule.logging.logObjects.DltMessage.DltMessage.GetPayloadBytes "Link to this definition")  
Returns the payload of the DLT message.

Returns:  message payload

Return type:  bytes

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
