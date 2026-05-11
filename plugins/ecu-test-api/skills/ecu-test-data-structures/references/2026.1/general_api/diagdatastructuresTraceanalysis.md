[ Internal APIs ](api.md)

[ Advanced operations of package variable types ](variabledatastructures.md)

[ Advanced properties of bus-related objects ](busdatastructures.md)

[ Bus related objects of trace analysis ](busdatastructuresTraceanalysis.md)

[ Advanced properties of diagnostics-related objects ](diagdatastructures.md)

Diagnostics related objects of trace analysis [ Diagnostics related objects of trace analysis ](#)

Diagnostics related objects of trace analysis

- [ UDS ](#uds)
  - [C UdsCanMessage ](#tts.traceRecording.parser.protocols.diag.UdsOnCanDiag.UdsCanMessage)
    - [A canId ](#tts.traceRecording.parser.protocols.diag.UdsOnCanDiag.UdsCanMessage.canId)
    - [A rawBytes ](#tts.traceRecording.parser.protocols.diag.UdsOnCanDiag.UdsCanMessage.rawBytes)
    - [A tsStart ](#tts.traceRecording.parser.protocols.diag.UdsOnCanDiag.UdsCanMessage.tsStart)
    - [A tsEnd ](#tts.traceRecording.parser.protocols.diag.UdsOnCanDiag.UdsCanMessage.tsEnd)
    - [A isResponse ](#tts.traceRecording.parser.protocols.diag.UdsOnCanDiag.UdsCanMessage.isResponse)
    - [A responseTime ](#tts.traceRecording.parser.protocols.diag.UdsOnCanDiag.UdsCanMessage.responseTime)
    - [A serviceId ](#tts.traceRecording.parser.protocols.diag.UdsOnCanDiag.UdsCanMessage.serviceId)
    - [A subFunction ](#tts.traceRecording.parser.protocols.diag.UdsOnCanDiag.UdsCanMessage.subFunction)
    - [A subId ](#tts.traceRecording.parser.protocols.diag.UdsOnCanDiag.UdsCanMessage.subId)
    - [A suppressPositiveResponse ](#tts.traceRecording.parser.protocols.diag.UdsOnCanDiag.UdsCanMessage.suppressPositiveResponse)
    - [A responseCode ](#tts.traceRecording.parser.protocols.diag.UdsOnCanDiag.UdsCanMessage.responseCode)
    - [A data ](#tts.traceRecording.parser.protocols.diag.UdsOnCanDiag.UdsCanMessage.data)

[ Advanced properties of media-related objects ](mediadatastructures.md)

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

Diagnostics related objects of trace analysis

- [ UDS ](#uds)
  - [C UdsCanMessage ](#tts.traceRecording.parser.protocols.diag.UdsOnCanDiag.UdsCanMessage)
    - [A canId ](#tts.traceRecording.parser.protocols.diag.UdsOnCanDiag.UdsCanMessage.canId)
    - [A rawBytes ](#tts.traceRecording.parser.protocols.diag.UdsOnCanDiag.UdsCanMessage.rawBytes)
    - [A tsStart ](#tts.traceRecording.parser.protocols.diag.UdsOnCanDiag.UdsCanMessage.tsStart)
    - [A tsEnd ](#tts.traceRecording.parser.protocols.diag.UdsOnCanDiag.UdsCanMessage.tsEnd)
    - [A isResponse ](#tts.traceRecording.parser.protocols.diag.UdsOnCanDiag.UdsCanMessage.isResponse)
    - [A responseTime ](#tts.traceRecording.parser.protocols.diag.UdsOnCanDiag.UdsCanMessage.responseTime)
    - [A serviceId ](#tts.traceRecording.parser.protocols.diag.UdsOnCanDiag.UdsCanMessage.serviceId)
    - [A subFunction ](#tts.traceRecording.parser.protocols.diag.UdsOnCanDiag.UdsCanMessage.subFunction)
    - [A subId ](#tts.traceRecording.parser.protocols.diag.UdsOnCanDiag.UdsCanMessage.subId)
    - [A suppressPositiveResponse ](#tts.traceRecording.parser.protocols.diag.UdsOnCanDiag.UdsCanMessage.suppressPositiveResponse)
    - [A responseCode ](#tts.traceRecording.parser.protocols.diag.UdsOnCanDiag.UdsCanMessage.responseCode)
    - [A data ](#tts.traceRecording.parser.protocols.diag.UdsOnCanDiag.UdsCanMessage.data)

# Diagnostics related objects of trace analysis[¶](#diagnostics-related-objects-of-trace-analysis "Link to this heading")

The following diag objects are supported for bus recordings.

## UDS[¶](#uds "Link to this heading")

*class* UdsCanMessage[¶](#tts.traceRecording.parser.protocols.diag.UdsOnCanDiag.UdsCanMessage "Link to this definition")  

canId : int[¶](#tts.traceRecording.parser.protocols.diag.UdsOnCanDiag.UdsCanMessage.canId "Link to this definition")  
The CAN ID.

rawBytes : bytes[¶](#tts.traceRecording.parser.protocols.diag.UdsOnCanDiag.UdsCanMessage.rawBytes "Link to this definition")  
The raw bytes of the UDS message.

tsStart : float[¶](#tts.traceRecording.parser.protocols.diag.UdsOnCanDiag.UdsCanMessage.tsStart "Link to this definition")  
The timestamp of the first CAN message that contains (parts of) the UDS message.

tsEnd : float[¶](#tts.traceRecording.parser.protocols.diag.UdsOnCanDiag.UdsCanMessage.tsEnd "Link to this definition")  
The timestamp of the last CAN message that contains (parts of) the UDS message.

isResponse : bool[¶](#tts.traceRecording.parser.protocols.diag.UdsOnCanDiag.UdsCanMessage.isResponse "Link to this definition")  
True, if the UDS message is a response message. False, if it is a request message.

responseTime : float | None[¶](#tts.traceRecording.parser.protocols.diag.UdsOnCanDiag.UdsCanMessage.responseTime "Link to this definition")  
Time between last frame of request and first frame of response (tStart - request.tEnd)

None for requests or responses without a preceding request in the recording.

serviceId : int[¶](#tts.traceRecording.parser.protocols.diag.UdsOnCanDiag.UdsCanMessage.serviceId "Link to this definition")  
The service ID (SID).

subFunction : int | None[¶](#tts.traceRecording.parser.protocols.diag.UdsOnCanDiag.UdsCanMessage.subFunction "Link to this definition")  
The sub function (SUBFUNC, Bit 6-0 of LEV) or None if there is no sub function.

subId : int | None[¶](#tts.traceRecording.parser.protocols.diag.UdsOnCanDiag.UdsCanMessage.subId "Link to this definition")  
The sub ID (DID, IOI, RI) or None if there is no sub ID.

suppressPositiveResponse : bool[¶](#tts.traceRecording.parser.protocols.diag.UdsOnCanDiag.UdsCanMessage.suppressPositiveResponse "Link to this definition")  
True, if a positive response message shall be suppressed (Bit 7 of LEV).

responseCode : int[¶](#tts.traceRecording.parser.protocols.diag.UdsOnCanDiag.UdsCanMessage.responseCode "Link to this definition")  
The response code of the UDS message.

- zero for requests and positive responses

- negative response code (NRC) for negative responses

data : dict[str, Any][¶](#tts.traceRecording.parser.protocols.diag.UdsOnCanDiag.UdsCanMessage.data "Link to this definition")  
The decoded UDS data. The values can be scalar types, dicts or lists.

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
