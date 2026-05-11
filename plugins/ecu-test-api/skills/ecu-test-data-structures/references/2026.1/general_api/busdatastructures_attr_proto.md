- [ Internal APIs ](api.md)
- [ Advanced operations of package variable types ](variabledatastructures.md)
- [ Advanced properties of bus-related objects ](busdatastructures.md)
- [ Bus related objects of trace analysis ](busdatastructuresTraceanalysis.md)
- [ Advanced properties of diagnostics-related objects ](diagdatastructures.md)
- [ Diagnostics related objects of trace analysis ](diagdatastructuresTraceanalysis.md)
- [ Advanced properties of media-related objects ](mediadatastructures.md)
- [ Advanced properties of DLT logging-related objects ](dltdatastructures.md)
- [ COM API ](com-api.md)
- [ REST API ](rest-api.md)
- [ Report API ](apireport.md)
- [ Object API ](objectApi.md)
- [ Trace Analysis API ](../TraceAnalysisAPI/index.md)
- [ Generator APIs ](../generators/index.md)
- [ Tools ](../tools/index.md)
- [ User test management ](../userTestmanagement/index.md)
- [ UserUtility API ](../user-utility/user-utility.md)
- [ Utility Examples ](../user-utility/example-utilities.md)

\<protocol\>  
Equivalent to method [`FindParent(protocol)`](busdatastructures.md#tts.lib.ethernet.PacketEthernet.PacketEthernet.FindParent "tts.lib.ethernet.PacketEthernet.PacketEthernet.FindParent (Python method) — Only for pseudo signals in trace analysis! Returns the requested protocol object if present, otherwise a NoProtocol object."). Direct access to parent protocols. *protocol* is one of [`OsiProtocol`](busdatastructuresTraceanalysis.md#tts.lib.ethernet.PacketEthernet.OsiProtocol "tts.lib.ethernet.PacketEthernet.OsiProtocol (Python class) — String Enumeration class representing the supported protocol layers.").

Example: Signal.eth.src provides the source MAC address of the Ethernet protocol layer.

Type:  [`EthernetProtocolBase`](busdatastructuresTraceanalysis.md#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase (Python class) — Base class for all protocol classes.")

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
