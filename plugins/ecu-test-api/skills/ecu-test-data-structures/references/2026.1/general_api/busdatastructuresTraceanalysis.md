[ Internal APIs ](api.md)

[ Advanced operations of package variable types ](variabledatastructures.md)

[ Advanced properties of bus-related objects ](busdatastructures.md)

Bus related objects of trace analysis [ Bus related objects of trace analysis ](#)

Bus related objects of trace analysis

- [ CAN ](#can)
  - [C CanMessageEvent ](#CanMessageEvent)
    - [A id ](#CanMessageEvent.id)
    - [A payload ](#CanMessageEvent.payload)
    - [A payloadArray ](#CanMessageEvent.payloadArray)
    - [A length ](#CanMessageEvent.length)
    - [A timestamp ](#CanMessageEvent.timestamp)
    - [A flags ](#CanMessageEvent.flags)
    - [A canID ](#CanMessageEvent.canID)
    - [A channelID ](#CanMessageEvent.channelID)
    - [A ecc ](#CanMessageEvent.ecc)
    - [A dlc ](#CanMessageEvent.dlc)
  - [C CanBusStatisticsEvent ](#CanBusStatisticsEvent)
    - [A dataFrames ](#CanBusStatisticsEvent.dataFrames)
    - [A remoteFrames ](#CanBusStatisticsEvent.remoteFrames)
    - [A extendedDataFrames ](#CanBusStatisticsEvent.extendedDataFrames)
    - [A extendedRemoteFrames ](#CanBusStatisticsEvent.extendedRemoteFrames)
    - [A errorFrames ](#CanBusStatisticsEvent.errorFrames)
    - [A overloadFrames ](#CanBusStatisticsEvent.overloadFrames)
    - [A busload ](#CanBusStatisticsEvent.busload)
    - [A timestamp ](#CanBusStatisticsEvent.timestamp)
    - [A channelID ](#CanBusStatisticsEvent.channelID)
  - [C CanErrorEvent ](#CanErrorEvent)
    - [A error ](#CanErrorEvent.error)
    - [A timestamp ](#CanErrorEvent.timestamp)
    - [A channelID ](#CanErrorEvent.channelID)
  - [C CanOverloadFrameEvent ](#CanOverloadFrameEvent)
    - [A timestamp ](#CanOverloadFrameEvent.timestamp)
    - [A channelID ](#CanOverloadFrameEvent.channelID)
- [ FlexRay ](#flexray)
  - [C FlexRayMessageEvent ](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayMessageEvent)
    - [A timestamp ](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayMessageEvent.timestamp)
    - [A id ](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayMessageEvent.id)
    - [A payload ](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayMessageEvent.payload)
    - [A payloadArray ](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayMessageEvent.payloadArray)
    - [A frameCRC ](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayMessageEvent.frameCRC)
    - [A slotID ](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayMessageEvent.slotID)
    - [A cycleNumber ](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayMessageEvent.cycleNumber)
    - [A headerCRC ](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayMessageEvent.headerCRC)
    - [A channelID ](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayMessageEvent.channelID)
    - [A channelMask ](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayMessageEvent.channelMask)
    - [A flags ](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayMessageEvent.flags)
    - [A ccType ](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayMessageEvent.ccType)
    - [A ccData ](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayMessageEvent.ccData)
  - [C FlexRayStartCycleEvent ](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayStartCycleEvent)
    - [A isSelfReceived ](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayStartCycleEvent.isSelfReceived)
    - [A cycleNumber ](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayStartCycleEvent.cycleNumber)
    - [A nmVect ](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayStartCycleEvent.nmVect)
    - [A nmVectArray ](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayStartCycleEvent.nmVectArray)
    - [A timestamp ](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayStartCycleEvent.timestamp)
    - [A channelID ](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayStartCycleEvent.channelID)
    - [A channelMask ](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayStartCycleEvent.channelMask)
    - [A ccType ](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayStartCycleEvent.ccType)
    - [A ccData ](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayStartCycleEvent.ccData)
    - [A ccDataArray ](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayStartCycleEvent.ccDataArray)
  - [C FlexRayStatusEvent ](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayStatusEvent)
    - [A cycleNumber ](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayStatusEvent.cycleNumber)
    - [A syncState ](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayStatusEvent.syncState)
    - [A symbol ](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayStatusEvent.symbol)
    - [A wakeUpState ](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayStatusEvent.wakeUpState)
    - [A timestamp ](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayStatusEvent.timestamp)
    - [A channelID ](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayStatusEvent.channelID)
    - [A channelMask ](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayStatusEvent.channelMask)
    - [A ccType ](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayStatusEvent.ccType)
    - [A ccData ](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayStatusEvent.ccData)
    - [A ccDataArray ](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayStatusEvent.ccDataArray)
  - [C FlexRayErrorEvent ](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayErrorEvent)
    - [A timestamp ](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayErrorEvent.timestamp)
    - [A channelID ](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayErrorEvent.channelID)
    - [A channelMask ](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayErrorEvent.channelMask)
    - [A ccType ](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayErrorEvent.ccType)
    - [A ccData ](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayErrorEvent.ccData)
    - [A ccDataArray ](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayErrorEvent.ccDataArray)
- [ LIN ](#lin)
  - [C LinMessageEvent ](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageEvent)
    - [A timestamp ](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageEvent.timestamp)
    - [A id ](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageEvent.id)
    - [A payload ](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageEvent.payload)
    - [A payloadArray ](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageEvent.payloadArray)
    - [A messageInfo ](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageEvent.messageInfo)
    - [A length ](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageEvent.length)
    - [A flags ](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageEvent.flags)
    - [A linID ](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageEvent.linID)
    - [A channelID ](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageEvent.channelID)
    - [A crc ](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageEvent.crc)
  - [C LinMessageInfo ](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageInfo)
    - [A slaveId ](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageInfo.slaveId)
    - [A state ](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageInfo.state)
    - [A checksum ](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageInfo.checksum)
    - [A headerTime ](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageInfo.headerTime)
    - [A fullTime ](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageInfo.fullTime)
    - [A startOfFrame ](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageInfo.startOfFrame)
    - [A baudrate ](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageInfo.baudrate)
    - [A syncBreak ](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageInfo.syncBreak)
    - [A syncDel ](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageInfo.syncDel)
    - [A nodeAddress ](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageInfo.nodeAddress)
    - [A messageId ](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageInfo.messageId)
    - [A supplierId ](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageInfo.supplierId)
    - [A endOfHeader ](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageInfo.endOfHeader)
    - [A endOfBytes ](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageInfo.endOfBytes)
    - [A simulated ](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageInfo.simulated)
    - [A endOfFrame ](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageInfo.endOfFrame)
    - [A responseBaudrate ](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageInfo.responseBaudrate)
    - [A headerBaudrate ](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageInfo.headerBaudrate)
    - [A stopBitOffsetInHeader ](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageInfo.stopBitOffsetInHeader)
    - [A stopBitOffsetInResponse ](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageInfo.stopBitOffsetInResponse)
    - [A checksumModel ](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageInfo.checksumModel)
  - [C LinSleepModeEvent ](#tts.traceRecording.parser.formats.BusParserObjects.LinSleepModeEvent)
    - [A reason ](#tts.traceRecording.parser.formats.BusParserObjects.LinSleepModeEvent.reason)
    - [A timestamp ](#tts.traceRecording.parser.formats.BusParserObjects.LinSleepModeEvent.timestamp)
    - [A channelID ](#tts.traceRecording.parser.formats.BusParserObjects.LinSleepModeEvent.channelID)
    - [A description ](#tts.traceRecording.parser.formats.BusParserObjects.LinSleepModeEvent.description)
    - [A flags ](#tts.traceRecording.parser.formats.BusParserObjects.LinSleepModeEvent.flags)
  - [C LinSleepModeFlags ](#tts.traceRecording.parser.formats.BusParserObjects.LinSleepModeFlags)
    - [A isAwakeBefore ](#tts.traceRecording.parser.formats.BusParserObjects.LinSleepModeFlags.isAwakeBefore)
    - [A isAwake ](#tts.traceRecording.parser.formats.BusParserObjects.LinSleepModeFlags.isAwake)
    - [A isExternalEvent ](#tts.traceRecording.parser.formats.BusParserObjects.LinSleepModeFlags.isExternalEvent)
  - [C LinWakeupFrame ](#tts.traceRecording.parser.formats.BusParserObjects.LinWakeupFrame)
    - [A isSelfReceived ](#tts.traceRecording.parser.formats.BusParserObjects.LinWakeupFrame.isSelfReceived)
    - [A wakeupByte ](#tts.traceRecording.parser.formats.BusParserObjects.LinWakeupFrame.wakeupByte)
    - [A messageInfo ](#tts.traceRecording.parser.formats.BusParserObjects.LinWakeupFrame.messageInfo)
    - [A timestamp ](#tts.traceRecording.parser.formats.BusParserObjects.LinWakeupFrame.timestamp)
    - [A channelID ](#tts.traceRecording.parser.formats.BusParserObjects.LinWakeupFrame.channelID)
  - [C LinUnexpectedWakeup ](#tts.traceRecording.parser.formats.BusParserObjects.LinUnexpectedWakeup)
    - [A timestamp ](#tts.traceRecording.parser.formats.BusParserObjects.LinUnexpectedWakeup.timestamp)
    - [A channelID ](#tts.traceRecording.parser.formats.BusParserObjects.LinUnexpectedWakeup.channelID)
    - [A wakeupByte ](#tts.traceRecording.parser.formats.BusParserObjects.LinUnexpectedWakeup.wakeupByte)
    - [A messageInfo ](#tts.traceRecording.parser.formats.BusParserObjects.LinUnexpectedWakeup.messageInfo)
  - [C LinWakeupFrameInfo ](#tts.traceRecording.parser.formats.BusParserObjects.LinWakeupFrameInfo)
    - [A startOfFrame ](#tts.traceRecording.parser.formats.BusParserObjects.LinWakeupFrameInfo.startOfFrame)
    - [A baudrate ](#tts.traceRecording.parser.formats.BusParserObjects.LinWakeupFrameInfo.baudrate)
    - [A lengthcode ](#tts.traceRecording.parser.formats.BusParserObjects.LinWakeupFrameInfo.lengthcode)
    - [A width ](#tts.traceRecording.parser.formats.BusParserObjects.LinWakeupFrameInfo.width)
- [ Ethernet ](#ethernet)
  - [C OsiProtocol ](#tts.lib.ethernet.PacketEthernet.OsiProtocol)
    - [A ETH ](#tts.lib.ethernet.PacketEthernet.OsiProtocol.ETH)
    - [A IP4 ](#tts.lib.ethernet.PacketEthernet.OsiProtocol.IP4)
    - [A IP6 ](#tts.lib.ethernet.PacketEthernet.OsiProtocol.IP6)
    - [A TCP ](#tts.lib.ethernet.PacketEthernet.OsiProtocol.TCP)
    - [A UDP ](#tts.lib.ethernet.PacketEthernet.OsiProtocol.UDP)
    - [A PTP ](#tts.lib.ethernet.PacketEthernet.OsiProtocol.PTP)
    - [A SOMEIP ](#tts.lib.ethernet.PacketEthernet.OsiProtocol.SOMEIP)
  - [ EthernetProtocolBase ](#ethernetprotocolbase)
    - [C EthernetProtocolBase ](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase)
      - [A timestamp ](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase.timestamp)
      - [A parent ](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase.parent)
      - [M AssertExists ](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase.AssertExists)
      - [M FindParent ](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase.FindParent)
  - [ NoProtocol ](#noprotocol)
    - [C NoProtocol ](#tts.lib.ethernet.PacketEthernet.NoProtocol)
      - [M AssertExists ](#tts.lib.ethernet.PacketEthernet.NoProtocol.AssertExists)
      - [M FindParent ](#tts.lib.ethernet.PacketEthernet.NoProtocol.FindParent)
      - [A parent ](#tts.lib.ethernet.PacketEthernet.NoProtocol.parent)
      - [A timestamp ](#tts.lib.ethernet.PacketEthernet.NoProtocol.timestamp)
  - [ EthernetProtocol ](#ethernetprotocol)
    - [C EthernetProtocol ](#tts.lib.ethernet.PacketEthernet.EthernetProtocol)
      - [A dst ](#tts.lib.ethernet.PacketEthernet.EthernetProtocol.dst)
      - [A src ](#tts.lib.ethernet.PacketEthernet.EthernetProtocol.src)
      - [M AssertExists ](#tts.lib.ethernet.PacketEthernet.EthernetProtocol.AssertExists)
      - [M FindParent ](#tts.lib.ethernet.PacketEthernet.EthernetProtocol.FindParent)
      - [A parent ](#tts.lib.ethernet.PacketEthernet.EthernetProtocol.parent)
      - [A type ](#tts.lib.ethernet.PacketEthernet.EthernetProtocol.type)
      - [A timestamp ](#tts.lib.ethernet.PacketEthernet.EthernetProtocol.timestamp)
      - [A vlanTags ](#tts.lib.ethernet.PacketEthernet.EthernetProtocol.vlanTags)
  - [ Ipv4Protocol ](#ipv4protocol)
    - [C Ipv4Protocol ](#tts.lib.ethernet.PacketIp4.Ipv4Protocol)
      - [A version ](#tts.lib.ethernet.PacketIp4.Ipv4Protocol.version)
      - [A headerLength ](#tts.lib.ethernet.PacketIp4.Ipv4Protocol.headerLength)
      - [A tos ](#tts.lib.ethernet.PacketIp4.Ipv4Protocol.tos)
      - [A packetLength ](#tts.lib.ethernet.PacketIp4.Ipv4Protocol.packetLength)
      - [A id ](#tts.lib.ethernet.PacketIp4.Ipv4Protocol.id)
      - [A ttl ](#tts.lib.ethernet.PacketIp4.Ipv4Protocol.ttl)
      - [A protocol ](#tts.lib.ethernet.PacketIp4.Ipv4Protocol.protocol)
      - [A checksum ](#tts.lib.ethernet.PacketIp4.Ipv4Protocol.checksum)
      - [A src ](#tts.lib.ethernet.PacketIp4.Ipv4Protocol.src)
      - [A dst ](#tts.lib.ethernet.PacketIp4.Ipv4Protocol.dst)
      - [A ahSpi ](#tts.lib.ethernet.PacketIp4.Ipv4Protocol.ahSpi)
      - [A ahSeq ](#tts.lib.ethernet.PacketIp4.Ipv4Protocol.ahSeq)
      - [A ahIcv ](#tts.lib.ethernet.PacketIp4.Ipv4Protocol.ahIcv)
      - [A ahNxt ](#tts.lib.ethernet.PacketIp4.Ipv4Protocol.ahNxt)
      - [A ahLen ](#tts.lib.ethernet.PacketIp4.Ipv4Protocol.ahLen)
      - [A ahRsvd ](#tts.lib.ethernet.PacketIp4.Ipv4Protocol.ahRsvd)
      - [M AssertExists ](#tts.lib.ethernet.PacketIp4.Ipv4Protocol.AssertExists)
      - [M FindParent ](#tts.lib.ethernet.PacketIp4.Ipv4Protocol.FindParent)
      - [A parent ](#tts.lib.ethernet.PacketIp4.Ipv4Protocol.parent)
      - [A timestamp ](#tts.lib.ethernet.PacketIp4.Ipv4Protocol.timestamp)
  - [ Ipv6Protocol ](#ipv6protocol)
    - [C Ipv6Protocol ](#tts.lib.ethernet.PacketIp6.Ipv6Protocol)
      - [A src ](#tts.lib.ethernet.PacketIp6.Ipv6Protocol.src)
      - [A dst ](#tts.lib.ethernet.PacketIp6.Ipv6Protocol.dst)
      - [A protocol ](#tts.lib.ethernet.PacketIp6.Ipv6Protocol.protocol)
      - [A hopLimit ](#tts.lib.ethernet.PacketIp6.Ipv6Protocol.hopLimit)
      - [A payloadLength ](#tts.lib.ethernet.PacketIp6.Ipv6Protocol.payloadLength)
      - [A trafficClass ](#tts.lib.ethernet.PacketIp6.Ipv6Protocol.trafficClass)
      - [A flowLabel ](#tts.lib.ethernet.PacketIp6.Ipv6Protocol.flowLabel)
      - [M AssertExists ](#tts.lib.ethernet.PacketIp6.Ipv6Protocol.AssertExists)
      - [M FindParent ](#tts.lib.ethernet.PacketIp6.Ipv6Protocol.FindParent)
      - [A parent ](#tts.lib.ethernet.PacketIp6.Ipv6Protocol.parent)
      - [A timestamp ](#tts.lib.ethernet.PacketIp6.Ipv6Protocol.timestamp)
  - [ UdpProtocol ](#udpprotocol)
    - [C UdpProtocol ](#tts.lib.ethernet.PacketUdp.UdpProtocol)
      - [A srcPort ](#tts.lib.ethernet.PacketUdp.UdpProtocol.srcPort)
      - [A dstPort ](#tts.lib.ethernet.PacketUdp.UdpProtocol.dstPort)
      - [M AssertExists ](#tts.lib.ethernet.PacketUdp.UdpProtocol.AssertExists)
      - [M FindParent ](#tts.lib.ethernet.PacketUdp.UdpProtocol.FindParent)
      - [A parent ](#tts.lib.ethernet.PacketUdp.UdpProtocol.parent)
      - [A packetLength ](#tts.lib.ethernet.PacketUdp.UdpProtocol.packetLength)
      - [A timestamp ](#tts.lib.ethernet.PacketUdp.UdpProtocol.timestamp)
      - [A checksum ](#tts.lib.ethernet.PacketUdp.UdpProtocol.checksum)
  - [ TcpProtocol ](#tcpprotocol)
    - [C TcpProtocol ](#tts.lib.ethernet.PacketTcp.TcpProtocol)
      - [A srcPort ](#tts.lib.ethernet.PacketTcp.TcpProtocol.srcPort)
      - [A dstPort ](#tts.lib.ethernet.PacketTcp.TcpProtocol.dstPort)
      - [A seq ](#tts.lib.ethernet.PacketTcp.TcpProtocol.seq)
      - [A packetLength ](#tts.lib.ethernet.PacketTcp.TcpProtocol.packetLength)
      - [A ack ](#tts.lib.ethernet.PacketTcp.TcpProtocol.ack)
      - [A headerLength ](#tts.lib.ethernet.PacketTcp.TcpProtocol.headerLength)
      - [A flags ](#tts.lib.ethernet.PacketTcp.TcpProtocol.flags)
      - [M AssertExists ](#tts.lib.ethernet.PacketTcp.TcpProtocol.AssertExists)
      - [M FindParent ](#tts.lib.ethernet.PacketTcp.TcpProtocol.FindParent)
      - [A parent ](#tts.lib.ethernet.PacketTcp.TcpProtocol.parent)
      - [A window ](#tts.lib.ethernet.PacketTcp.TcpProtocol.window)
      - [A timestamp ](#tts.lib.ethernet.PacketTcp.TcpProtocol.timestamp)
      - [A checksum ](#tts.lib.ethernet.PacketTcp.TcpProtocol.checksum)
      - [A urgentPointer ](#tts.lib.ethernet.PacketTcp.TcpProtocol.urgentPointer)
  - [ PtpProtocol ](#ptpprotocol)
    - [C PtpProtocol ](#tts.lib.ethernet.PacketPtp.PtpProtocol)
      - [A messageType ](#tts.lib.ethernet.PacketPtp.PtpProtocol.messageType)
      - [A version ](#tts.lib.ethernet.PacketPtp.PtpProtocol.version)
      - [A messageLength ](#tts.lib.ethernet.PacketPtp.PtpProtocol.messageLength)
      - [A domainNumber ](#tts.lib.ethernet.PacketPtp.PtpProtocol.domainNumber)
      - [A flags ](#tts.lib.ethernet.PacketPtp.PtpProtocol.flags)
      - [A correctionField ](#tts.lib.ethernet.PacketPtp.PtpProtocol.correctionField)
      - [A sourcePortIdentity ](#tts.lib.ethernet.PacketPtp.PtpProtocol.sourcePortIdentity)
      - [A sequenceId ](#tts.lib.ethernet.PacketPtp.PtpProtocol.sequenceId)
      - [A controlField ](#tts.lib.ethernet.PacketPtp.PtpProtocol.controlField)
      - [A logMessagePeriod ](#tts.lib.ethernet.PacketPtp.PtpProtocol.logMessagePeriod)
      - [M AssertExists ](#tts.lib.ethernet.PacketPtp.PtpProtocol.AssertExists)
      - [M FindParent ](#tts.lib.ethernet.PacketPtp.PtpProtocol.FindParent)
      - [A parent ](#tts.lib.ethernet.PacketPtp.PtpProtocol.parent)
      - [A timestamp ](#tts.lib.ethernet.PacketPtp.PtpProtocol.timestamp)
  - [ SomeIpProtocol ](#someipprotocol)
    - [C SomeIpProtocol ](#tts.lib.ethernet.PacketSomeIp.SomeIpProtocol)
      - [A messageId ](#tts.lib.ethernet.PacketSomeIp.SomeIpProtocol.messageId)
      - [A serviceId ](#tts.lib.ethernet.PacketSomeIp.SomeIpProtocol.serviceId)
      - [M AssertExists ](#tts.lib.ethernet.PacketSomeIp.SomeIpProtocol.AssertExists)
      - [M FindParent ](#tts.lib.ethernet.PacketSomeIp.SomeIpProtocol.FindParent)
      - [A parent ](#tts.lib.ethernet.PacketSomeIp.SomeIpProtocol.parent)
      - [A methodId ](#tts.lib.ethernet.PacketSomeIp.SomeIpProtocol.methodId)
      - [A timestamp ](#tts.lib.ethernet.PacketSomeIp.SomeIpProtocol.timestamp)
      - [A length ](#tts.lib.ethernet.PacketSomeIp.SomeIpProtocol.length)
      - [A requestId ](#tts.lib.ethernet.PacketSomeIp.SomeIpProtocol.requestId)
      - [A clientId ](#tts.lib.ethernet.PacketSomeIp.SomeIpProtocol.clientId)
      - [A sessionId ](#tts.lib.ethernet.PacketSomeIp.SomeIpProtocol.sessionId)
      - [A protocolVersion ](#tts.lib.ethernet.PacketSomeIp.SomeIpProtocol.protocolVersion)
      - [A interfaceVersion ](#tts.lib.ethernet.PacketSomeIp.SomeIpProtocol.interfaceVersion)
      - [A messageType ](#tts.lib.ethernet.PacketSomeIp.SomeIpProtocol.messageType)
      - [A returnCode ](#tts.lib.ethernet.PacketSomeIp.SomeIpProtocol.returnCode)

[ Advanced properties of diagnostics-related objects ](diagdatastructures.md)

[ Diagnostics related objects of trace analysis ](diagdatastructuresTraceanalysis.md)

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

Bus related objects of trace analysis

- [ CAN ](#can)
  - [C CanMessageEvent ](#CanMessageEvent)
    - [A id ](#CanMessageEvent.id)
    - [A payload ](#CanMessageEvent.payload)
    - [A payloadArray ](#CanMessageEvent.payloadArray)
    - [A length ](#CanMessageEvent.length)
    - [A timestamp ](#CanMessageEvent.timestamp)
    - [A flags ](#CanMessageEvent.flags)
    - [A canID ](#CanMessageEvent.canID)
    - [A channelID ](#CanMessageEvent.channelID)
    - [A ecc ](#CanMessageEvent.ecc)
    - [A dlc ](#CanMessageEvent.dlc)
  - [C CanBusStatisticsEvent ](#CanBusStatisticsEvent)
    - [A dataFrames ](#CanBusStatisticsEvent.dataFrames)
    - [A remoteFrames ](#CanBusStatisticsEvent.remoteFrames)
    - [A extendedDataFrames ](#CanBusStatisticsEvent.extendedDataFrames)
    - [A extendedRemoteFrames ](#CanBusStatisticsEvent.extendedRemoteFrames)
    - [A errorFrames ](#CanBusStatisticsEvent.errorFrames)
    - [A overloadFrames ](#CanBusStatisticsEvent.overloadFrames)
    - [A busload ](#CanBusStatisticsEvent.busload)
    - [A timestamp ](#CanBusStatisticsEvent.timestamp)
    - [A channelID ](#CanBusStatisticsEvent.channelID)
  - [C CanErrorEvent ](#CanErrorEvent)
    - [A error ](#CanErrorEvent.error)
    - [A timestamp ](#CanErrorEvent.timestamp)
    - [A channelID ](#CanErrorEvent.channelID)
  - [C CanOverloadFrameEvent ](#CanOverloadFrameEvent)
    - [A timestamp ](#CanOverloadFrameEvent.timestamp)
    - [A channelID ](#CanOverloadFrameEvent.channelID)
- [ FlexRay ](#flexray)
  - [C FlexRayMessageEvent ](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayMessageEvent)
    - [A timestamp ](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayMessageEvent.timestamp)
    - [A id ](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayMessageEvent.id)
    - [A payload ](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayMessageEvent.payload)
    - [A payloadArray ](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayMessageEvent.payloadArray)
    - [A frameCRC ](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayMessageEvent.frameCRC)
    - [A slotID ](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayMessageEvent.slotID)
    - [A cycleNumber ](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayMessageEvent.cycleNumber)
    - [A headerCRC ](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayMessageEvent.headerCRC)
    - [A channelID ](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayMessageEvent.channelID)
    - [A channelMask ](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayMessageEvent.channelMask)
    - [A flags ](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayMessageEvent.flags)
    - [A ccType ](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayMessageEvent.ccType)
    - [A ccData ](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayMessageEvent.ccData)
  - [C FlexRayStartCycleEvent ](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayStartCycleEvent)
    - [A isSelfReceived ](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayStartCycleEvent.isSelfReceived)
    - [A cycleNumber ](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayStartCycleEvent.cycleNumber)
    - [A nmVect ](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayStartCycleEvent.nmVect)
    - [A nmVectArray ](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayStartCycleEvent.nmVectArray)
    - [A timestamp ](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayStartCycleEvent.timestamp)
    - [A channelID ](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayStartCycleEvent.channelID)
    - [A channelMask ](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayStartCycleEvent.channelMask)
    - [A ccType ](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayStartCycleEvent.ccType)
    - [A ccData ](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayStartCycleEvent.ccData)
    - [A ccDataArray ](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayStartCycleEvent.ccDataArray)
  - [C FlexRayStatusEvent ](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayStatusEvent)
    - [A cycleNumber ](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayStatusEvent.cycleNumber)
    - [A syncState ](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayStatusEvent.syncState)
    - [A symbol ](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayStatusEvent.symbol)
    - [A wakeUpState ](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayStatusEvent.wakeUpState)
    - [A timestamp ](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayStatusEvent.timestamp)
    - [A channelID ](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayStatusEvent.channelID)
    - [A channelMask ](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayStatusEvent.channelMask)
    - [A ccType ](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayStatusEvent.ccType)
    - [A ccData ](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayStatusEvent.ccData)
    - [A ccDataArray ](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayStatusEvent.ccDataArray)
  - [C FlexRayErrorEvent ](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayErrorEvent)
    - [A timestamp ](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayErrorEvent.timestamp)
    - [A channelID ](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayErrorEvent.channelID)
    - [A channelMask ](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayErrorEvent.channelMask)
    - [A ccType ](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayErrorEvent.ccType)
    - [A ccData ](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayErrorEvent.ccData)
    - [A ccDataArray ](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayErrorEvent.ccDataArray)
- [ LIN ](#lin)
  - [C LinMessageEvent ](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageEvent)
    - [A timestamp ](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageEvent.timestamp)
    - [A id ](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageEvent.id)
    - [A payload ](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageEvent.payload)
    - [A payloadArray ](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageEvent.payloadArray)
    - [A messageInfo ](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageEvent.messageInfo)
    - [A length ](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageEvent.length)
    - [A flags ](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageEvent.flags)
    - [A linID ](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageEvent.linID)
    - [A channelID ](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageEvent.channelID)
    - [A crc ](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageEvent.crc)
  - [C LinMessageInfo ](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageInfo)
    - [A slaveId ](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageInfo.slaveId)
    - [A state ](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageInfo.state)
    - [A checksum ](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageInfo.checksum)
    - [A headerTime ](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageInfo.headerTime)
    - [A fullTime ](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageInfo.fullTime)
    - [A startOfFrame ](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageInfo.startOfFrame)
    - [A baudrate ](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageInfo.baudrate)
    - [A syncBreak ](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageInfo.syncBreak)
    - [A syncDel ](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageInfo.syncDel)
    - [A nodeAddress ](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageInfo.nodeAddress)
    - [A messageId ](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageInfo.messageId)
    - [A supplierId ](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageInfo.supplierId)
    - [A endOfHeader ](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageInfo.endOfHeader)
    - [A endOfBytes ](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageInfo.endOfBytes)
    - [A simulated ](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageInfo.simulated)
    - [A endOfFrame ](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageInfo.endOfFrame)
    - [A responseBaudrate ](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageInfo.responseBaudrate)
    - [A headerBaudrate ](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageInfo.headerBaudrate)
    - [A stopBitOffsetInHeader ](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageInfo.stopBitOffsetInHeader)
    - [A stopBitOffsetInResponse ](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageInfo.stopBitOffsetInResponse)
    - [A checksumModel ](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageInfo.checksumModel)
  - [C LinSleepModeEvent ](#tts.traceRecording.parser.formats.BusParserObjects.LinSleepModeEvent)
    - [A reason ](#tts.traceRecording.parser.formats.BusParserObjects.LinSleepModeEvent.reason)
    - [A timestamp ](#tts.traceRecording.parser.formats.BusParserObjects.LinSleepModeEvent.timestamp)
    - [A channelID ](#tts.traceRecording.parser.formats.BusParserObjects.LinSleepModeEvent.channelID)
    - [A description ](#tts.traceRecording.parser.formats.BusParserObjects.LinSleepModeEvent.description)
    - [A flags ](#tts.traceRecording.parser.formats.BusParserObjects.LinSleepModeEvent.flags)
  - [C LinSleepModeFlags ](#tts.traceRecording.parser.formats.BusParserObjects.LinSleepModeFlags)
    - [A isAwakeBefore ](#tts.traceRecording.parser.formats.BusParserObjects.LinSleepModeFlags.isAwakeBefore)
    - [A isAwake ](#tts.traceRecording.parser.formats.BusParserObjects.LinSleepModeFlags.isAwake)
    - [A isExternalEvent ](#tts.traceRecording.parser.formats.BusParserObjects.LinSleepModeFlags.isExternalEvent)
  - [C LinWakeupFrame ](#tts.traceRecording.parser.formats.BusParserObjects.LinWakeupFrame)
    - [A isSelfReceived ](#tts.traceRecording.parser.formats.BusParserObjects.LinWakeupFrame.isSelfReceived)
    - [A wakeupByte ](#tts.traceRecording.parser.formats.BusParserObjects.LinWakeupFrame.wakeupByte)
    - [A messageInfo ](#tts.traceRecording.parser.formats.BusParserObjects.LinWakeupFrame.messageInfo)
    - [A timestamp ](#tts.traceRecording.parser.formats.BusParserObjects.LinWakeupFrame.timestamp)
    - [A channelID ](#tts.traceRecording.parser.formats.BusParserObjects.LinWakeupFrame.channelID)
  - [C LinUnexpectedWakeup ](#tts.traceRecording.parser.formats.BusParserObjects.LinUnexpectedWakeup)
    - [A timestamp ](#tts.traceRecording.parser.formats.BusParserObjects.LinUnexpectedWakeup.timestamp)
    - [A channelID ](#tts.traceRecording.parser.formats.BusParserObjects.LinUnexpectedWakeup.channelID)
    - [A wakeupByte ](#tts.traceRecording.parser.formats.BusParserObjects.LinUnexpectedWakeup.wakeupByte)
    - [A messageInfo ](#tts.traceRecording.parser.formats.BusParserObjects.LinUnexpectedWakeup.messageInfo)
  - [C LinWakeupFrameInfo ](#tts.traceRecording.parser.formats.BusParserObjects.LinWakeupFrameInfo)
    - [A startOfFrame ](#tts.traceRecording.parser.formats.BusParserObjects.LinWakeupFrameInfo.startOfFrame)
    - [A baudrate ](#tts.traceRecording.parser.formats.BusParserObjects.LinWakeupFrameInfo.baudrate)
    - [A lengthcode ](#tts.traceRecording.parser.formats.BusParserObjects.LinWakeupFrameInfo.lengthcode)
    - [A width ](#tts.traceRecording.parser.formats.BusParserObjects.LinWakeupFrameInfo.width)
- [ Ethernet ](#ethernet)
  - [C OsiProtocol ](#tts.lib.ethernet.PacketEthernet.OsiProtocol)
    - [A ETH ](#tts.lib.ethernet.PacketEthernet.OsiProtocol.ETH)
    - [A IP4 ](#tts.lib.ethernet.PacketEthernet.OsiProtocol.IP4)
    - [A IP6 ](#tts.lib.ethernet.PacketEthernet.OsiProtocol.IP6)
    - [A TCP ](#tts.lib.ethernet.PacketEthernet.OsiProtocol.TCP)
    - [A UDP ](#tts.lib.ethernet.PacketEthernet.OsiProtocol.UDP)
    - [A PTP ](#tts.lib.ethernet.PacketEthernet.OsiProtocol.PTP)
    - [A SOMEIP ](#tts.lib.ethernet.PacketEthernet.OsiProtocol.SOMEIP)
  - [ EthernetProtocolBase ](#ethernetprotocolbase)
    - [C EthernetProtocolBase ](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase)
      - [A timestamp ](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase.timestamp)
      - [A parent ](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase.parent)
      - [M AssertExists ](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase.AssertExists)
      - [M FindParent ](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase.FindParent)
  - [ NoProtocol ](#noprotocol)
    - [C NoProtocol ](#tts.lib.ethernet.PacketEthernet.NoProtocol)
      - [M AssertExists ](#tts.lib.ethernet.PacketEthernet.NoProtocol.AssertExists)
      - [M FindParent ](#tts.lib.ethernet.PacketEthernet.NoProtocol.FindParent)
      - [A parent ](#tts.lib.ethernet.PacketEthernet.NoProtocol.parent)
      - [A timestamp ](#tts.lib.ethernet.PacketEthernet.NoProtocol.timestamp)
  - [ EthernetProtocol ](#ethernetprotocol)
    - [C EthernetProtocol ](#tts.lib.ethernet.PacketEthernet.EthernetProtocol)
      - [A dst ](#tts.lib.ethernet.PacketEthernet.EthernetProtocol.dst)
      - [A src ](#tts.lib.ethernet.PacketEthernet.EthernetProtocol.src)
      - [M AssertExists ](#tts.lib.ethernet.PacketEthernet.EthernetProtocol.AssertExists)
      - [M FindParent ](#tts.lib.ethernet.PacketEthernet.EthernetProtocol.FindParent)
      - [A parent ](#tts.lib.ethernet.PacketEthernet.EthernetProtocol.parent)
      - [A type ](#tts.lib.ethernet.PacketEthernet.EthernetProtocol.type)
      - [A timestamp ](#tts.lib.ethernet.PacketEthernet.EthernetProtocol.timestamp)
      - [A vlanTags ](#tts.lib.ethernet.PacketEthernet.EthernetProtocol.vlanTags)
  - [ Ipv4Protocol ](#ipv4protocol)
    - [C Ipv4Protocol ](#tts.lib.ethernet.PacketIp4.Ipv4Protocol)
      - [A version ](#tts.lib.ethernet.PacketIp4.Ipv4Protocol.version)
      - [A headerLength ](#tts.lib.ethernet.PacketIp4.Ipv4Protocol.headerLength)
      - [A tos ](#tts.lib.ethernet.PacketIp4.Ipv4Protocol.tos)
      - [A packetLength ](#tts.lib.ethernet.PacketIp4.Ipv4Protocol.packetLength)
      - [A id ](#tts.lib.ethernet.PacketIp4.Ipv4Protocol.id)
      - [A ttl ](#tts.lib.ethernet.PacketIp4.Ipv4Protocol.ttl)
      - [A protocol ](#tts.lib.ethernet.PacketIp4.Ipv4Protocol.protocol)
      - [A checksum ](#tts.lib.ethernet.PacketIp4.Ipv4Protocol.checksum)
      - [A src ](#tts.lib.ethernet.PacketIp4.Ipv4Protocol.src)
      - [A dst ](#tts.lib.ethernet.PacketIp4.Ipv4Protocol.dst)
      - [A ahSpi ](#tts.lib.ethernet.PacketIp4.Ipv4Protocol.ahSpi)
      - [A ahSeq ](#tts.lib.ethernet.PacketIp4.Ipv4Protocol.ahSeq)
      - [A ahIcv ](#tts.lib.ethernet.PacketIp4.Ipv4Protocol.ahIcv)
      - [A ahNxt ](#tts.lib.ethernet.PacketIp4.Ipv4Protocol.ahNxt)
      - [A ahLen ](#tts.lib.ethernet.PacketIp4.Ipv4Protocol.ahLen)
      - [A ahRsvd ](#tts.lib.ethernet.PacketIp4.Ipv4Protocol.ahRsvd)
      - [M AssertExists ](#tts.lib.ethernet.PacketIp4.Ipv4Protocol.AssertExists)
      - [M FindParent ](#tts.lib.ethernet.PacketIp4.Ipv4Protocol.FindParent)
      - [A parent ](#tts.lib.ethernet.PacketIp4.Ipv4Protocol.parent)
      - [A timestamp ](#tts.lib.ethernet.PacketIp4.Ipv4Protocol.timestamp)
  - [ Ipv6Protocol ](#ipv6protocol)
    - [C Ipv6Protocol ](#tts.lib.ethernet.PacketIp6.Ipv6Protocol)
      - [A src ](#tts.lib.ethernet.PacketIp6.Ipv6Protocol.src)
      - [A dst ](#tts.lib.ethernet.PacketIp6.Ipv6Protocol.dst)
      - [A protocol ](#tts.lib.ethernet.PacketIp6.Ipv6Protocol.protocol)
      - [A hopLimit ](#tts.lib.ethernet.PacketIp6.Ipv6Protocol.hopLimit)
      - [A payloadLength ](#tts.lib.ethernet.PacketIp6.Ipv6Protocol.payloadLength)
      - [A trafficClass ](#tts.lib.ethernet.PacketIp6.Ipv6Protocol.trafficClass)
      - [A flowLabel ](#tts.lib.ethernet.PacketIp6.Ipv6Protocol.flowLabel)
      - [M AssertExists ](#tts.lib.ethernet.PacketIp6.Ipv6Protocol.AssertExists)
      - [M FindParent ](#tts.lib.ethernet.PacketIp6.Ipv6Protocol.FindParent)
      - [A parent ](#tts.lib.ethernet.PacketIp6.Ipv6Protocol.parent)
      - [A timestamp ](#tts.lib.ethernet.PacketIp6.Ipv6Protocol.timestamp)
  - [ UdpProtocol ](#udpprotocol)
    - [C UdpProtocol ](#tts.lib.ethernet.PacketUdp.UdpProtocol)
      - [A srcPort ](#tts.lib.ethernet.PacketUdp.UdpProtocol.srcPort)
      - [A dstPort ](#tts.lib.ethernet.PacketUdp.UdpProtocol.dstPort)
      - [M AssertExists ](#tts.lib.ethernet.PacketUdp.UdpProtocol.AssertExists)
      - [M FindParent ](#tts.lib.ethernet.PacketUdp.UdpProtocol.FindParent)
      - [A parent ](#tts.lib.ethernet.PacketUdp.UdpProtocol.parent)
      - [A packetLength ](#tts.lib.ethernet.PacketUdp.UdpProtocol.packetLength)
      - [A timestamp ](#tts.lib.ethernet.PacketUdp.UdpProtocol.timestamp)
      - [A checksum ](#tts.lib.ethernet.PacketUdp.UdpProtocol.checksum)
  - [ TcpProtocol ](#tcpprotocol)
    - [C TcpProtocol ](#tts.lib.ethernet.PacketTcp.TcpProtocol)
      - [A srcPort ](#tts.lib.ethernet.PacketTcp.TcpProtocol.srcPort)
      - [A dstPort ](#tts.lib.ethernet.PacketTcp.TcpProtocol.dstPort)
      - [A seq ](#tts.lib.ethernet.PacketTcp.TcpProtocol.seq)
      - [A packetLength ](#tts.lib.ethernet.PacketTcp.TcpProtocol.packetLength)
      - [A ack ](#tts.lib.ethernet.PacketTcp.TcpProtocol.ack)
      - [A headerLength ](#tts.lib.ethernet.PacketTcp.TcpProtocol.headerLength)
      - [A flags ](#tts.lib.ethernet.PacketTcp.TcpProtocol.flags)
      - [M AssertExists ](#tts.lib.ethernet.PacketTcp.TcpProtocol.AssertExists)
      - [M FindParent ](#tts.lib.ethernet.PacketTcp.TcpProtocol.FindParent)
      - [A parent ](#tts.lib.ethernet.PacketTcp.TcpProtocol.parent)
      - [A window ](#tts.lib.ethernet.PacketTcp.TcpProtocol.window)
      - [A timestamp ](#tts.lib.ethernet.PacketTcp.TcpProtocol.timestamp)
      - [A checksum ](#tts.lib.ethernet.PacketTcp.TcpProtocol.checksum)
      - [A urgentPointer ](#tts.lib.ethernet.PacketTcp.TcpProtocol.urgentPointer)
  - [ PtpProtocol ](#ptpprotocol)
    - [C PtpProtocol ](#tts.lib.ethernet.PacketPtp.PtpProtocol)
      - [A messageType ](#tts.lib.ethernet.PacketPtp.PtpProtocol.messageType)
      - [A version ](#tts.lib.ethernet.PacketPtp.PtpProtocol.version)
      - [A messageLength ](#tts.lib.ethernet.PacketPtp.PtpProtocol.messageLength)
      - [A domainNumber ](#tts.lib.ethernet.PacketPtp.PtpProtocol.domainNumber)
      - [A flags ](#tts.lib.ethernet.PacketPtp.PtpProtocol.flags)
      - [A correctionField ](#tts.lib.ethernet.PacketPtp.PtpProtocol.correctionField)
      - [A sourcePortIdentity ](#tts.lib.ethernet.PacketPtp.PtpProtocol.sourcePortIdentity)
      - [A sequenceId ](#tts.lib.ethernet.PacketPtp.PtpProtocol.sequenceId)
      - [A controlField ](#tts.lib.ethernet.PacketPtp.PtpProtocol.controlField)
      - [A logMessagePeriod ](#tts.lib.ethernet.PacketPtp.PtpProtocol.logMessagePeriod)
      - [M AssertExists ](#tts.lib.ethernet.PacketPtp.PtpProtocol.AssertExists)
      - [M FindParent ](#tts.lib.ethernet.PacketPtp.PtpProtocol.FindParent)
      - [A parent ](#tts.lib.ethernet.PacketPtp.PtpProtocol.parent)
      - [A timestamp ](#tts.lib.ethernet.PacketPtp.PtpProtocol.timestamp)
  - [ SomeIpProtocol ](#someipprotocol)
    - [C SomeIpProtocol ](#tts.lib.ethernet.PacketSomeIp.SomeIpProtocol)
      - [A messageId ](#tts.lib.ethernet.PacketSomeIp.SomeIpProtocol.messageId)
      - [A serviceId ](#tts.lib.ethernet.PacketSomeIp.SomeIpProtocol.serviceId)
      - [M AssertExists ](#tts.lib.ethernet.PacketSomeIp.SomeIpProtocol.AssertExists)
      - [M FindParent ](#tts.lib.ethernet.PacketSomeIp.SomeIpProtocol.FindParent)
      - [A parent ](#tts.lib.ethernet.PacketSomeIp.SomeIpProtocol.parent)
      - [A methodId ](#tts.lib.ethernet.PacketSomeIp.SomeIpProtocol.methodId)
      - [A timestamp ](#tts.lib.ethernet.PacketSomeIp.SomeIpProtocol.timestamp)
      - [A length ](#tts.lib.ethernet.PacketSomeIp.SomeIpProtocol.length)
      - [A requestId ](#tts.lib.ethernet.PacketSomeIp.SomeIpProtocol.requestId)
      - [A clientId ](#tts.lib.ethernet.PacketSomeIp.SomeIpProtocol.clientId)
      - [A sessionId ](#tts.lib.ethernet.PacketSomeIp.SomeIpProtocol.sessionId)
      - [A protocolVersion ](#tts.lib.ethernet.PacketSomeIp.SomeIpProtocol.protocolVersion)
      - [A interfaceVersion ](#tts.lib.ethernet.PacketSomeIp.SomeIpProtocol.interfaceVersion)
      - [A messageType ](#tts.lib.ethernet.PacketSomeIp.SomeIpProtocol.messageType)
      - [A returnCode ](#tts.lib.ethernet.PacketSomeIp.SomeIpProtocol.returnCode)

# Bus related objects of trace analysis[¶](#bus-related-objects-of-trace-analysis "Link to this heading")

The following bus objects are supported for ASC recordings.

## CAN[¶](#can "Link to this heading")

*class* CanMessageEvent[¶](#CanMessageEvent "Link to this definition")  
Class for multiple types of bus events:

- CAN Message Event

- CAN Extended Message Event

- CAN Error Frame

- CAN Remote Frame Event

- CAN FD Message Event

- CAN FD Extended Message Event

- CAN FD Error Frame

id[¶](#CanMessageEvent.id "Link to this definition")  
Alias for [`CanMessageEvent.canID`](#CanMessageEvent.canID "CanMessageEvent.canID (Python attribute) — The CAN ID of the frame."). The slot ID of the frame.

Type:  int

payload[¶](#CanMessageEvent.payload "Link to this definition")  
The frame’s payload.

Type:  ByteStream

payloadArray[¶](#CanMessageEvent.payloadArray "Link to this definition")  
The frame’s payload as numpy array (especially useful in trace step templates).

Type:  numpy.ndarray

length[¶](#CanMessageEvent.length "Link to this definition")  
The frame’s length in bytes.

Type:  int

timestamp[¶](#CanMessageEvent.timestamp "Link to this definition")  
The frame’s timestamp in ms.

Type:  float

flags[¶](#CanMessageEvent.flags "Link to this definition")  
Any of the frame’s flags defined in the corresponding flags class can be accessed directly on the frame object, i.e. theFrame.aFlag instead of theFrame.flags.aFlag.

Some of the flags can take the value False if the driver does not support the respective attribute.

Type:  [`CanFlags`](busdatastructures.md#tts.testModule.bus.busObjects.CAN.CanFlags "tts.testModule.bus.busObjects.CAN.CanFlags (Python class) — Is this an error frame?")

canID[¶](#CanMessageEvent.canID "Link to this definition")  
The CAN ID of the frame.

Type:  int

channelID[¶](#CanMessageEvent.channelID "Link to this definition")  
The ID of the bus channel on which this frame was received.

Type:  int

ecc[¶](#CanMessageEvent.ecc "Link to this definition")  
The ECC of the frame.

Type:  int

dlc[¶](#CanMessageEvent.dlc "Link to this definition")  
The DLC of the frame.

Type:  int

*class* CanBusStatisticsEvent[¶](#CanBusStatisticsEvent "Link to this definition")  
dataFrames[¶](#CanBusStatisticsEvent.dataFrames "Link to this definition")  
The number of data frames.

Type:  int

remoteFrames[¶](#CanBusStatisticsEvent.remoteFrames "Link to this definition")  
The number of remote frames.

Type:  int

extendedDataFrames[¶](#CanBusStatisticsEvent.extendedDataFrames "Link to this definition")  
The number of extended data frames.

Type:  int

extendedRemoteFrames[¶](#CanBusStatisticsEvent.extendedRemoteFrames "Link to this definition")  
The number of extended remote frames.

Type:  int

errorFrames[¶](#CanBusStatisticsEvent.errorFrames "Link to this definition")  
The number of error frames.

Type:  int

overloadFrames[¶](#CanBusStatisticsEvent.overloadFrames "Link to this definition")  
The number of overload frames.

Type:  int

busload[¶](#CanBusStatisticsEvent.busload "Link to this definition")  
The busload.

Type:  float

timestamp[¶](#CanBusStatisticsEvent.timestamp "Link to this definition")  
The frame’s raw timestamp. The determined offset of trace synchronization is not considered.

Type:  float

channelID[¶](#CanBusStatisticsEvent.channelID "Link to this definition")  
The ID of the bus channel on which this frame was received.

Type:  int

*class* CanErrorEvent[¶](#CanErrorEvent "Link to this definition")  
error[¶](#CanErrorEvent.error "Link to this definition")  
The error.

Type:  str

timestamp[¶](#CanErrorEvent.timestamp "Link to this definition")  
The frame’s raw timestamp. The determined offset of trace synchronization is not considered.

Type:  float

channelID[¶](#CanErrorEvent.channelID "Link to this definition")  
The ID of the bus channel on which this frame was received.

Type:  int

*class* CanOverloadFrameEvent[¶](#CanOverloadFrameEvent "Link to this definition")  
timestamp[¶](#CanOverloadFrameEvent.timestamp "Link to this definition")  
The frame’s raw timestamp. The determined offset of trace synchronization is not considered.

Type:  float

channelID[¶](#CanOverloadFrameEvent.channelID "Link to this definition")  
The ID of the bus channel on which this frame was received.

Type:  int

## FlexRay[¶](#flexray "Link to this heading")

*class* FlexRayMessageEvent[¶](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayMessageEvent "Link to this definition")  
timestamp[¶](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayMessageEvent.timestamp "Link to this definition")  
The frame’s raw timestamp. The determined offset of trace synchronization is not considered.

Type:  float

id[¶](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayMessageEvent.id "Link to this definition")  
Alias for [`slotID()`](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayMessageEvent.slotID "tts.traceRecording.parser.formats.BusParserObjects.FlexRayMessageEvent.slotID (Python attribute) — The slot ID of the frame."). The FlexRay Slot-ID of the frame.

Type:  int

payload[¶](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayMessageEvent.payload "Link to this definition")  
The frame’s payload.

Type:  ByteStream

payloadArray[¶](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayMessageEvent.payloadArray "Link to this definition")  
The frame’s payload as numpy array (especially useful in trace step templates).

Type:  numpy.ndarray

frameCRC[¶](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayMessageEvent.frameCRC "Link to this definition")  
The CRC of the frame. Will be 0 if the CRC is not available.

Type:  int

slotID[¶](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayMessageEvent.slotID "Link to this definition")  
The slot ID of the frame.

Type:  int

cycleNumber[¶](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayMessageEvent.cycleNumber "Link to this definition")  
The cycle number of the frame.

Type:  int

headerCRC[¶](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayMessageEvent.headerCRC "Link to this definition")  
The header CRC of the frame.

Type:  int

channelID[¶](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayMessageEvent.channelID "Link to this definition")  
The ID of the FlexRay channel on which this frame was received.

Type:  int

channelMask[¶](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayMessageEvent.channelMask "Link to this definition")  
The FlexRay channel mask, e.g. “A”, “B”, or “AB”.

Type:  str

flags[¶](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayMessageEvent.flags "Link to this definition")  
Any of the frame’s flags defined in the corresponding flags class can be accessed directly on the frame object, i.e. theFrame.aFlag instead of theFrame.flags.aFlag.

Some of the flags can take the value False if the driver does not support the respective attribute.

Type:  [`FlexRayFlags`](busdatastructures.md#tts.testModule.bus.busObjects.FlexRay.FlexRayFlags "tts.testModule.bus.busObjects.FlexRay.FlexRayFlags (Python class) — Was this frame sent by the controller that received it?")

ccType[¶](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayMessageEvent.ccType "Link to this definition")  
Type of the communication controller.

Type:  int

ccData[¶](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayMessageEvent.ccData "Link to this definition")  
Communication controller specific data.

Type:  int

*class* FlexRayStartCycleEvent[¶](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayStartCycleEvent "Link to this definition")  
isSelfReceived[¶](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayStartCycleEvent.isSelfReceived "Link to this definition")  
Was this frame sent by the controller that received it?

Type:  bool

cycleNumber[¶](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayStartCycleEvent.cycleNumber "Link to this definition")  
The cycle number of the frame.

Type:  int

nmVect[¶](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayStartCycleEvent.nmVect "Link to this definition")  
The network management vector.

Type:  list

nmVectArray[¶](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayStartCycleEvent.nmVectArray "Link to this definition")  
The frame’s network management vector as numpy array (especially useful in trace step templates).

Type:  numpy.ndarray

timestamp[¶](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayStartCycleEvent.timestamp "Link to this definition")  
The frame’s raw timestamp. The determined offset of trace synchronization is not considered.

Type:  float

channelID[¶](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayStartCycleEvent.channelID "Link to this definition")  
The ID of the bus channel on which this frame was received.

Type:  int

channelMask[¶](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayStartCycleEvent.channelMask "Link to this definition")  
The FlexRay channel mask, e.g. “A”, “B”, or “AB”.

Type:  str

ccType[¶](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayStartCycleEvent.ccType "Link to this definition")  
Type of the communication controller.

Type:  int

ccData[¶](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayStartCycleEvent.ccData "Link to this definition")  
Communication controller specific data.

Type:  list

ccDataArray[¶](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayStartCycleEvent.ccDataArray "Link to this definition")  
The frame’s communication controller specific data as numpy array (especially useful in trace step templates).

Type:  numpy.ndarray

*class* FlexRayStatusEvent[¶](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayStatusEvent "Link to this definition")  
cycleNumber[¶](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayStatusEvent.cycleNumber "Link to this definition")  
The cycle number of the frame.

Type:  int

syncState[¶](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayStatusEvent.syncState "Link to this definition")  
The sync state.

Type:  int

symbol[¶](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayStatusEvent.symbol "Link to this definition")  
The symbol of the event.

Type:  int

wakeUpState[¶](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayStatusEvent.wakeUpState "Link to this definition")  
The wake up state.

Type:  int

timestamp[¶](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayStatusEvent.timestamp "Link to this definition")  
The frame’s raw timestamp. The determined offset of trace synchronization is not considered.

Type:  float

channelID[¶](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayStatusEvent.channelID "Link to this definition")  
The ID of the bus channel on which this frame was received.

Type:  int

channelMask[¶](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayStatusEvent.channelMask "Link to this definition")  
The FlexRay channel mask, e.g. “A”, “B”, or “AB”.

Type:  str

ccType[¶](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayStatusEvent.ccType "Link to this definition")  
Type of the communication controller.

Type:  int

ccData[¶](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayStatusEvent.ccData "Link to this definition")  
Communication controller specific data.

Type:  list

ccDataArray[¶](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayStatusEvent.ccDataArray "Link to this definition")  
The frame’s communication controller specific data as numpy array (especially useful in trace step templates).

Type:  numpy.ndarray

*class* FlexRayErrorEvent[¶](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayErrorEvent "Link to this definition")  
timestamp[¶](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayErrorEvent.timestamp "Link to this definition")  
The frame’s raw timestamp. The determined offset of trace synchronization is not considered.

Type:  float

channelID[¶](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayErrorEvent.channelID "Link to this definition")  
The ID of the bus channel on which this frame was received.

Type:  int

channelMask[¶](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayErrorEvent.channelMask "Link to this definition")  
The FlexRay channel mask, e.g. “A”, “B”, or “AB”.

Type:  str

ccType[¶](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayErrorEvent.ccType "Link to this definition")  
Type of the communication controller.

Type:  int

ccData[¶](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayErrorEvent.ccData "Link to this definition")  
Communication controller specific data.

Type:  list

ccDataArray[¶](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayErrorEvent.ccDataArray "Link to this definition")  
The frame’s communication controller specific data as numpy array (especially useful in trace step templates).

Type:  numpy.ndarray

## LIN[¶](#lin "Link to this heading")

*class* LinMessageEvent[¶](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageEvent "Link to this definition")  

timestamp[¶](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageEvent.timestamp "Link to this definition")  
The frame’s raw timestamp. The determined offset of trace synchronization is not considered.

Type:  float

id[¶](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageEvent.id "Link to this definition")  
Alias for [`linID()`](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageEvent.linID "tts.traceRecording.parser.formats.BusParserObjects.LinMessageEvent.linID (Python attribute) — The LIN ID of the frame."). The slot ID of the frame.

Type:  int

payload[¶](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageEvent.payload "Link to this definition")  
The frame’s payload.

Type:  ByteStream

payloadArray[¶](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageEvent.payloadArray "Link to this definition")  
The frame’s payload as numpy array (especially useful in trace step templates).

Type:  numpy.ndarray

messageInfo[¶](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageEvent.messageInfo "Link to this definition")  
Additional message information, for instance related to timings.

Type:  [`LinMessageInfo`](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageInfo "tts.traceRecording.parser.formats.BusParserObjects.LinMessageInfo (Python class) — FSM Identifier (Available with FSMs only).")

length[¶](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageEvent.length "Link to this definition")  
The frame’s length in bytes.

Type:  int

flags[¶](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageEvent.flags "Link to this definition")  
Any of the frame’s flags defined in the corresponding flags class can be accessed directly on the frame object, i.e. theFrame.aFlag instead of theFrame.flags.aFlag.

Some of the flags can take the value False if the driver does not support the respective attribute.

Type:  [`LinFlags`](busdatastructures.md#tts.testModule.bus.busObjects.LIN.LinFlags "tts.testModule.bus.busObjects.LIN.LinFlags (Python class) — Does this frame have a CRC error?")

linID[¶](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageEvent.linID "Link to this definition")  
The LIN ID of the frame.

Type:  int

channelID[¶](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageEvent.channelID "Link to this definition")  
The ID of the bus channel on which this frame was received.

Type:  int

crc[¶](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageEvent.crc "Link to this definition")  
The CRC of the frame.

Type:  int

*class* LinMessageInfo[¶](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageInfo "Link to this definition")  
slaveId[¶](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageInfo.slaveId "Link to this definition")  
FSM Identifier (Available with FSMs only).

Type:  int or numpy.ma.masked if not present

state[¶](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageInfo.state "Link to this definition")  
Current state of the FSM (Available with FSMs only).

Type:  int or numpy.ma.masked if not present

checksum[¶](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageInfo.checksum "Link to this definition")  
Checksum byte value

Type:  int or numpy.ma.masked if not present.

headerTime[¶](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageInfo.headerTime "Link to this definition")  
Duration of the frame header (in bit times).

Obsolete: Used up to CANoe/CANalyzer version 6.0.

Type:  int or numpy.ma.masked if not present

fullTime[¶](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageInfo.fullTime "Link to this definition")  
Duration of the entire frame (in bit times).

Obsolete: Used up to CANoe/CANalyzer version 6.0.

Type:  int or numpy.ma.masked if not present

startOfFrame[¶](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageInfo.startOfFrame "Link to this definition")  
Absolute timestamp indicating start of event (in seconds).

Type:  float or numpy.ma.masked if not present

baudrate[¶](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageInfo.baudrate "Link to this definition")  
Event’s baudrate (in bits/sec).

Type:  int or numpy.ma.masked if not present

syncBreak[¶](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageInfo.syncBreak "Link to this definition")  
Break length (in ns).

Type:  int or numpy.ma.masked if not present

syncDel[¶](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageInfo.syncDel "Link to this definition")  
Break delimiter length (in ns).

Type:  int or numpy.ma.masked if not present

nodeAddress[¶](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageInfo.nodeAddress "Link to this definition")  
Node address (available for dynamic frames only).

Type:  int or numpy.ma.masked if not present

messageId[¶](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageInfo.messageId "Link to this definition")  
16 bit message identifier (available for dynamic frames only).

Type:  int or numpy.ma.masked if not present

supplierId[¶](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageInfo.supplierId "Link to this definition")  
Supplier identifier (available for dynamic frames only).

Type:  int or numpy.ma.masked if not present

endOfHeader[¶](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageInfo.endOfHeader "Link to this definition")  
Absolute timestamp indicating end of LIN frame (in seconds).

Type:  float or numpy.ma.masked if not present

endOfBytes[¶](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageInfo.endOfBytes "Link to this definition")  
Absolute timestamps indicating end of data byte (in seconds).

Type:  numpy.ndarray(float) or numpy.ma.masked if not present

simulated[¶](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageInfo.simulated "Link to this definition")  
Flag indicating whether event has been simulated by CANoe/CANalyzer.

Type:  int or numpy.ma.masked if not present

endOfFrame[¶](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageInfo.endOfFrame "Link to this definition")  
Absolute timestamp indicating end of LIN frame (in seconds).

Type:  float or numpy.ma.masked if not present

responseBaudrate[¶](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageInfo.responseBaudrate "Link to this definition")  
Event’s baudrate measured in response (in bits/sec).

Type:  int or numpy.ma.masked if not present

headerBaudrate[¶](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageInfo.headerBaudrate "Link to this definition")  
Event’s baudrate measured in header (in bits/sec as float value).

Type:  float or numpy.ma.masked if not present

stopBitOffsetInHeader[¶](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageInfo.stopBitOffsetInHeader "Link to this definition")  
Early stop bit offset in frame header for UART timestamps (in ns).

Type:  int or numpy.ma.masked if not present

stopBitOffsetInResponse[¶](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageInfo.stopBitOffsetInResponse "Link to this definition")  
Early stop bit offset in frame response for UART timestamps (in ns).

Type:  int or numpy.ma.masked if not present

checksumModel[¶](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageInfo.checksumModel "Link to this definition")  
Expected checksum model for checksum value. Possible values: ‘unknown’, ‘classic’, ‘enhanced’, ‘error’.

Type:  str or numpy.ma.masked if not present

*class* LinSleepModeEvent[¶](#tts.traceRecording.parser.formats.BusParserObjects.LinSleepModeEvent "Link to this definition")  
reason[¶](#tts.traceRecording.parser.formats.BusParserObjects.LinSleepModeEvent.reason "Link to this definition")  
The reason of a sleep mode event as integer.

- 0: Start state

Transition to sleep mode

- 1: Go-to-Sleep frame

- 2: Bus Idle Timeout

- 3: Silent SleepMode command (for shortening the BusIdle Timeout)

Leaving sleep mode

- 9: External Wakeup signal

- 10: Internal Wakeup signal

- 11: Bus traffic (can only occur if the LIN hardware does not have a Master function)

LIN hardware does not go into sleep mode inspite of request to do so

- 18: Bus traffic (can only occur if the LIN hardware does not have a Master function)

Type:  int

timestamp[¶](#tts.traceRecording.parser.formats.BusParserObjects.LinSleepModeEvent.timestamp "Link to this definition")  
The frame’s raw timestamp. The determined offset of trace synchronization is not considered.

Type:  float

channelID[¶](#tts.traceRecording.parser.formats.BusParserObjects.LinSleepModeEvent.channelID "Link to this definition")  
The ID of the bus channel on which this frame was received.

Type:  int

description[¶](#tts.traceRecording.parser.formats.BusParserObjects.LinSleepModeEvent.description "Link to this definition")  
The description of a sleep mode event.

Type:  str

flags[¶](#tts.traceRecording.parser.formats.BusParserObjects.LinSleepModeEvent.flags "Link to this definition")  
Any of the frame’s flags defined in the corresponding flags class can be accessed directly on the frame object, i.e. theFrame.aFlag instead of theFrame.flags.aFlag.

Some of the flags can take the value False if the driver does not support the respective attribute.

Type:  [`LinSleepModeFlags`](#tts.traceRecording.parser.formats.BusParserObjects.LinSleepModeFlags "tts.traceRecording.parser.formats.BusParserObjects.LinSleepModeFlags (Python class) — The awake state before this event. True if awake, False if asleep.")

*class* LinSleepModeFlags[¶](#tts.traceRecording.parser.formats.BusParserObjects.LinSleepModeFlags "Link to this definition")  
isAwakeBefore[¶](#tts.traceRecording.parser.formats.BusParserObjects.LinSleepModeFlags.isAwakeBefore "Link to this definition")  
The awake state before this event. True if awake, False if asleep.

Type:  bool

isAwake[¶](#tts.traceRecording.parser.formats.BusParserObjects.LinSleepModeFlags.isAwake "Link to this definition")  
The current awake state. True if awake, False if asleep.

Type:  bool

isExternalEvent[¶](#tts.traceRecording.parser.formats.BusParserObjects.LinSleepModeFlags.isExternalEvent "Link to this definition")  
Flag whether the this event is caused by an external (True) or internal (False) event.

Type:  bool

*class* LinWakeupFrame[¶](#tts.traceRecording.parser.formats.BusParserObjects.LinWakeupFrame "Link to this definition")  
isSelfReceived[¶](#tts.traceRecording.parser.formats.BusParserObjects.LinWakeupFrame.isSelfReceived "Link to this definition")  
Was this frame sent by the controller that received it?

Type:  bool

wakeupByte[¶](#tts.traceRecording.parser.formats.BusParserObjects.LinWakeupFrame.wakeupByte "Link to this definition")  
The wakeup byte. This value will be 0 for LIN 2.0.

Type:  int

messageInfo[¶](#tts.traceRecording.parser.formats.BusParserObjects.LinWakeupFrame.messageInfo "Link to this definition")  
Additional message information, for instance related to timings.

Type:  [`LinWakeupFrameInfo`](#tts.traceRecording.parser.formats.BusParserObjects.LinWakeupFrameInfo "tts.traceRecording.parser.formats.BusParserObjects.LinWakeupFrameInfo (Python class) — Absolute timestamp indicating start of event (in seconds).")

timestamp[¶](#tts.traceRecording.parser.formats.BusParserObjects.LinWakeupFrame.timestamp "Link to this definition")  
The frame’s raw timestamp. The determined offset of trace synchronization is not considered.

Type:  float

channelID[¶](#tts.traceRecording.parser.formats.BusParserObjects.LinWakeupFrame.channelID "Link to this definition")  
The ID of the bus channel on which this frame was received.

Type:  int

*class* LinUnexpectedWakeup[¶](#tts.traceRecording.parser.formats.BusParserObjects.LinUnexpectedWakeup "Link to this definition")  
timestamp[¶](#tts.traceRecording.parser.formats.BusParserObjects.LinUnexpectedWakeup.timestamp "Link to this definition")  
The frame’s raw timestamp. The determined offset of trace synchronization is not considered.

Type:  float

channelID[¶](#tts.traceRecording.parser.formats.BusParserObjects.LinUnexpectedWakeup.channelID "Link to this definition")  
The ID of the bus channel on which this frame was received.

Type:  int

wakeupByte[¶](#tts.traceRecording.parser.formats.BusParserObjects.LinUnexpectedWakeup.wakeupByte "Link to this definition")  
The wakeup byte. This value will be 0 for LIN 2.0.

Type:  int

messageInfo[¶](#tts.traceRecording.parser.formats.BusParserObjects.LinUnexpectedWakeup.messageInfo "Link to this definition")  
Additional message information, for instance related to timings.

Type:  [`LinWakeupFrameInfo`](#tts.traceRecording.parser.formats.BusParserObjects.LinWakeupFrameInfo "tts.traceRecording.parser.formats.BusParserObjects.LinWakeupFrameInfo (Python class) — Absolute timestamp indicating start of event (in seconds).")

*class* LinWakeupFrameInfo[¶](#tts.traceRecording.parser.formats.BusParserObjects.LinWakeupFrameInfo "Link to this definition")  
startOfFrame[¶](#tts.traceRecording.parser.formats.BusParserObjects.LinWakeupFrameInfo.startOfFrame "Link to this definition")  
Absolute timestamp indicating start of event (in seconds).

Type:  float or np.ma.masked if not present

baudrate[¶](#tts.traceRecording.parser.formats.BusParserObjects.LinWakeupFrameInfo.baudrate "Link to this definition")  
Event’s baudrate (in bits/sec).

Type:  int or np.ma.masked if not present

lengthcode[¶](#tts.traceRecording.parser.formats.BusParserObjects.LinWakeupFrameInfo.lengthcode "Link to this definition")  
This value is only valid for instances of [`LinWakeupFrame`](#tts.traceRecording.parser.formats.BusParserObjects.LinWakeupFrame "tts.traceRecording.parser.formats.BusParserObjects.LinWakeupFrame (Python class) — Was this frame sent by the controller that received it?").

Wake-up length validity indicator:

- 0: Wake-up length is OK

- 1: Wake-up is too short

- 2: Wake-up is too long

Type:  int or np.ma.masked if not present

width[¶](#tts.traceRecording.parser.formats.BusParserObjects.LinWakeupFrameInfo.width "Link to this definition")  
The width of a wakeup signal in us. This value is only valid for instances of [`LinUnexpectedWakeup`](#tts.traceRecording.parser.formats.BusParserObjects.LinUnexpectedWakeup "tts.traceRecording.parser.formats.BusParserObjects.LinUnexpectedWakeup (Python class) — The frame’s raw timestamp. The determined offset of trace synchronization is not considered.") with LIN 2.0.

Type:  int or np.ma.masked if not present

## Ethernet[¶](#ethernet "Link to this heading")

The following classes are created through calls of .parent, .FindParent(protocolName) or direct attribute access on a pseudo signal during trace analysis. protocolName is a string enum value from [OsiProtocol](#osiprotocolenum).

Examples:

- PacketSomeIp.udp.srcPort

- PacketUdp.FindParent(“eth”)

- PacketIp.parent

Info

Access to `EthernetProtocolBase.parent` can return None, while the other variants to protocols will return a `NoProtocol` instance if the given protocol is not present.

*class* OsiProtocol[¶](#tts.lib.ethernet.PacketEthernet.OsiProtocol "Link to this definition")  
String Enumeration class representing the supported protocol layers.

ETH = `'eth'`[¶](#tts.lib.ethernet.PacketEthernet.OsiProtocol.ETH "Link to this definition")  

IP4 = `'ip4'`[¶](#tts.lib.ethernet.PacketEthernet.OsiProtocol.IP4 "Link to this definition")  

IP6 = `'ip6'`[¶](#tts.lib.ethernet.PacketEthernet.OsiProtocol.IP6 "Link to this definition")  

TCP = `'tcp'`[¶](#tts.lib.ethernet.PacketEthernet.OsiProtocol.TCP "Link to this definition")  

UDP = `'udp'`[¶](#tts.lib.ethernet.PacketEthernet.OsiProtocol.UDP "Link to this definition")  

PTP = `'ptp'`[¶](#tts.lib.ethernet.PacketEthernet.OsiProtocol.PTP "Link to this definition")  

SOMEIP = `'someip'`[¶](#tts.lib.ethernet.PacketEthernet.OsiProtocol.SOMEIP "Link to this definition")  

### EthernetProtocolBase[¶](#ethernetprotocolbase "Link to this heading")

*class* EthernetProtocolBase[¶](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "Link to this definition")  
Base class for all protocol classes.

\<protocol\>  
Equivalent to method [`FindParent(protocol)`](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase.FindParent "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase.FindParent (Python method) — Returns a specific given protocol object if present, otherwise a NoProtocol object."). Direct access to parent protocols. *protocol* is one of [`OsiProtocol`](#tts.lib.ethernet.PacketEthernet.OsiProtocol "tts.lib.ethernet.PacketEthernet.OsiProtocol (Python class) — String Enumeration class representing the supported protocol layers.").

Example: Signal.eth.src provides the source MAC address of the Ethernet protocol layer.

Type:  [`EthernetProtocolBase`](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase (Python class) — Base class for all protocol classes.")

timestamp : float[¶](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase.timestamp "Link to this definition")  
current timestamp

parent[¶](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase.parent "Link to this definition")  
Returns the parent protocol object if there is one present, otherwise None.

Return type:  [EthernetProtocolBase](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase (Python class) — Base class for all protocol classes.") | None

AssertExists()[¶](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase.AssertExists "Link to this definition")  
Raises an AssertionError if the accessed protocol does not exist at some time stamp. Example: Signal.tcp.AssertExists()

Returns:  The protocol itself, to support attribut chaining.

Raises:  
AssertionError

Return type:  *Self*

FindParent(*[protocol](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase.FindParent.protocol "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase.FindParent.protocol (Python parameter) — The required protocol name.")*)[¶](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase.FindParent "Link to this definition")  
Returns a specific given protocol object if present, otherwise a [`NoProtocol`](#tts.lib.ethernet.PacketEthernet.NoProtocol "tts.lib.ethernet.PacketEthernet.NoProtocol (Python class) — Represents a non-present protocol. Accessing any other parent of a non-present protocol will also yield a NoProtocol object. Accessing any protocol specific attributes will lead to an AttributeError since the specific protocol is not available. The boolean value of a NoProtocol object is always False, such that it can be used to check for the precense/absence of a protocol layer.") object.

Parameters:  protocol : [OsiProtocol](#tts.lib.ethernet.PacketEthernet.OsiProtocol "tts.lib.ethernet.PacketEthernet.OsiProtocol (Python class) — String Enumeration class representing the supported protocol layers.")[¶](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase.FindParent.protocol "Permalink to this definition")  
The required protocol name.

Returns:  The required parent protocol object.

Return type:  [EthernetProtocolBase](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase (Python class) — Base class for all protocol classes.")

### NoProtocol[¶](#noprotocol "Link to this heading")

*class* NoProtocol[¶](#tts.lib.ethernet.PacketEthernet.NoProtocol "Link to this definition")  
Represents a non-present protocol. Accessing any other parent of a non-present protocol will also yield a NoProtocol object. Accessing any protocol specific attributes will lead to an AttributeError since the specific protocol is not available. The boolean value of a NoProtocol object is always False, such that it can be used to check for the precense/absence of a protocol layer.

Examples:

- SigPacketSomeIp.tcp yields True for packets that were transmitted via TCP and False otherwise. This can be used in trigger blocks that trigger only when the TCP protcol layer is present.

- SigPacketSomeIp.tcp.srcPort will raise an AttributeError for packets that were not transmitted via TCP.

- SigPacketSomeIp.tcp.AssertExists() can be used to provoke an AssertionError for packets that were not transmitted via TCP.

\<protocol\>  
Equivalent to method [`FindParent(protocol)`](#tts.lib.ethernet.PacketEthernet.NoProtocol.FindParent "tts.lib.ethernet.PacketEthernet.NoProtocol.FindParent (Python method) — Returns another NoProtocol instance."). Direct access to parent protocols. *protocol* is one of [`OsiProtocol`](#tts.lib.ethernet.PacketEthernet.OsiProtocol "tts.lib.ethernet.PacketEthernet.OsiProtocol (Python class) — String Enumeration class representing the supported protocol layers.").

Example: Signal.eth.src provides the source MAC address of the Ethernet protocol layer.

Type:  [`EthernetProtocolBase`](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase (Python class) — Base class for all protocol classes.")

AssertExists()[¶](#tts.lib.ethernet.PacketEthernet.NoProtocol.AssertExists "Link to this definition")  
Raises an AssertionError if the accessed protocol does not exist at some time stamp. Example: Signal.tcp.AssertExists()

Returns:  The protocol itself, to support attribut chaining.

Raises:  
AssertionError

Return type:  *Self*

FindParent(*[protocol](#tts.lib.ethernet.PacketEthernet.NoProtocol.FindParent "tts.lib.ethernet.PacketEthernet.NoProtocol.FindParent.protocol (Python parameter)")*)[¶](#tts.lib.ethernet.PacketEthernet.NoProtocol.FindParent "Link to this definition")  
Returns another NoProtocol instance.

Return type:  [NoProtocol](#tts.lib.ethernet.PacketEthernet.NoProtocol "tts.lib.ethernet.PacketEthernet.NoProtocol (Python class) — Represents a non-present protocol. Accessing any other parent of a non-present protocol will also yield a NoProtocol object. Accessing any protocol specific attributes will lead to an AttributeError since the specific protocol is not available. The boolean value of a NoProtocol object is always False, such that it can be used to check for the precense/absence of a protocol layer.")

parent[¶](#tts.lib.ethernet.PacketEthernet.NoProtocol.parent "Link to this definition")  
Returns another NoProtocol instance.

Return type:  [NoProtocol](#tts.lib.ethernet.PacketEthernet.NoProtocol "tts.lib.ethernet.PacketEthernet.NoProtocol (Python class) — Represents a non-present protocol. Accessing any other parent of a non-present protocol will also yield a NoProtocol object. Accessing any protocol specific attributes will lead to an AttributeError since the specific protocol is not available. The boolean value of a NoProtocol object is always False, such that it can be used to check for the precense/absence of a protocol layer.")

timestamp : float[¶](#tts.lib.ethernet.PacketEthernet.NoProtocol.timestamp "Link to this definition")  
current timestamp

### EthernetProtocol[¶](#ethernetprotocol "Link to this heading")

*class* EthernetProtocol[¶](#tts.lib.ethernet.PacketEthernet.EthernetProtocol "Link to this definition")  

\<protocol\>  
Equivalent to method [`FindParent(protocol)`](#tts.lib.ethernet.PacketEthernet.EthernetProtocol.FindParent "tts.lib.ethernet.PacketEthernet.EthernetProtocol.FindParent (Python method) — Returns a specific given protocol object if present, otherwise a NoProtocol object."). Direct access to parent protocols. *protocol* is one of [`OsiProtocol`](#tts.lib.ethernet.PacketEthernet.OsiProtocol "tts.lib.ethernet.PacketEthernet.OsiProtocol (Python class) — String Enumeration class representing the supported protocol layers.").

Example: Signal.eth.src provides the source MAC address of the Ethernet protocol layer.

Type:  [`EthernetProtocolBase`](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase (Python class) — Base class for all protocol classes.")

dst : str[¶](#tts.lib.ethernet.PacketEthernet.EthernetProtocol.dst "Link to this definition")  
target MAC address e.g. DE:AD:BE:EF:FF:00

src : str[¶](#tts.lib.ethernet.PacketEthernet.EthernetProtocol.src "Link to this definition")  
source MAC address e.g. DE:AD:BE:EF:FF:00

AssertExists()[¶](#tts.lib.ethernet.PacketEthernet.EthernetProtocol.AssertExists "Link to this definition")  
Raises an AssertionError if the accessed protocol does not exist at some time stamp. Example: Signal.tcp.AssertExists()

Returns:  The protocol itself, to support attribut chaining.

Raises:  
AssertionError

Return type:  *Self*

FindParent(*[protocol](#tts.lib.ethernet.PacketEthernet.EthernetProtocol.FindParent.protocol "tts.lib.ethernet.PacketEthernet.EthernetProtocol.FindParent.protocol (Python parameter) — The required protocol name.")*)[¶](#tts.lib.ethernet.PacketEthernet.EthernetProtocol.FindParent "Link to this definition")  
Returns a specific given protocol object if present, otherwise a [`NoProtocol`](#tts.lib.ethernet.PacketEthernet.NoProtocol "tts.lib.ethernet.PacketEthernet.NoProtocol (Python class) — Represents a non-present protocol. Accessing any other parent of a non-present protocol will also yield a NoProtocol object. Accessing any protocol specific attributes will lead to an AttributeError since the specific protocol is not available. The boolean value of a NoProtocol object is always False, such that it can be used to check for the precense/absence of a protocol layer.") object.

Parameters:  protocol : [OsiProtocol](#tts.lib.ethernet.PacketEthernet.OsiProtocol "tts.lib.ethernet.PacketEthernet.OsiProtocol (Python class) — String Enumeration class representing the supported protocol layers.")[¶](#tts.lib.ethernet.PacketEthernet.EthernetProtocol.FindParent.protocol "Permalink to this definition")  
The required protocol name.

Returns:  The required parent protocol object.

Return type:  [EthernetProtocolBase](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase (Python class) — Base class for all protocol classes.")

parent[¶](#tts.lib.ethernet.PacketEthernet.EthernetProtocol.parent "Link to this definition")  
Returns the parent protocol object if there is one present, otherwise None.

Return type:  [EthernetProtocolBase](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase (Python class) — Base class for all protocol classes.") | None

type : int[¶](#tts.lib.ethernet.PacketEthernet.EthernetProtocol.type "Link to this definition")  
ethernet protocol type

timestamp : float[¶](#tts.lib.ethernet.PacketEthernet.EthernetProtocol.timestamp "Link to this definition")  
current timestamp

vlanTags : None | list[VlanTag] = `None`[¶](#tts.lib.ethernet.PacketEthernet.EthernetProtocol.vlanTags "Link to this definition")  
list of VLAN tags, use vlanTags[-1] to get the inner vlan tag

### Ipv4Protocol[¶](#ipv4protocol "Link to this heading")

*class* Ipv4Protocol[¶](#tts.lib.ethernet.PacketIp4.Ipv4Protocol "Link to this definition")  

\<protocol\>  
Equivalent to method [`FindParent(protocol)`](#tts.lib.ethernet.PacketIp4.Ipv4Protocol.FindParent "tts.lib.ethernet.PacketIp4.Ipv4Protocol.FindParent (Python method) — Returns a specific given protocol object if present, otherwise a NoProtocol object."). Direct access to parent protocols. *protocol* is one of [`OsiProtocol`](#tts.lib.ethernet.PacketEthernet.OsiProtocol "tts.lib.ethernet.PacketEthernet.OsiProtocol (Python class) — String Enumeration class representing the supported protocol layers.").

Example: Signal.eth.src provides the source MAC address of the Ethernet protocol layer.

Type:  [`EthernetProtocolBase`](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase (Python class) — Base class for all protocol classes.")

version : int[¶](#tts.lib.ethernet.PacketIp4.Ipv4Protocol.version "Link to this definition")  
protocol version

headerLength : int[¶](#tts.lib.ethernet.PacketIp4.Ipv4Protocol.headerLength "Link to this definition")  
header length

tos : int[¶](#tts.lib.ethernet.PacketIp4.Ipv4Protocol.tos "Link to this definition")  
type of service

packetLength : int[¶](#tts.lib.ethernet.PacketIp4.Ipv4Protocol.packetLength "Link to this definition")  
packet length

id : int[¶](#tts.lib.ethernet.PacketIp4.Ipv4Protocol.id "Link to this definition")  
identifier

ttl : int[¶](#tts.lib.ethernet.PacketIp4.Ipv4Protocol.ttl "Link to this definition")  
TTL

protocol : int[¶](#tts.lib.ethernet.PacketIp4.Ipv4Protocol.protocol "Link to this definition")  
protocol type / next header field

checksum : int[¶](#tts.lib.ethernet.PacketIp4.Ipv4Protocol.checksum "Link to this definition")  
checksum

src : str[¶](#tts.lib.ethernet.PacketIp4.Ipv4Protocol.src "Link to this definition")  
source IP address e.g. 127.0.0.1

dst : str[¶](#tts.lib.ethernet.PacketIp4.Ipv4Protocol.dst "Link to this definition")  
destination IP address e.g. 127.0.0.1

ahSpi : int | None = `None`[¶](#tts.lib.ethernet.PacketIp4.Ipv4Protocol.ahSpi "Link to this definition")  
Security parameters index of IP authentication header (see RFC 4302)

ahSeq : int | None = `None`[¶](#tts.lib.ethernet.PacketIp4.Ipv4Protocol.ahSeq "Link to this definition")  
Sequence number field of IP authentication header (see RFC 4302)

ahIcv : bytes | None = `None`[¶](#tts.lib.ethernet.PacketIp4.Ipv4Protocol.ahIcv "Link to this definition")  
Integrity check value of IP authentication header (see RFC 4302)

ahNxt : int | None = `None`[¶](#tts.lib.ethernet.PacketIp4.Ipv4Protocol.ahNxt "Link to this definition")  
Next header value of IP authentication header (see RFC 4302)

ahLen : int | None = `None`[¶](#tts.lib.ethernet.PacketIp4.Ipv4Protocol.ahLen "Link to this definition")  
Length value of IP authentication header (see RFC 4302) =\> len(ICV)/4+1’

ahRsvd : int | None = `None`[¶](#tts.lib.ethernet.PacketIp4.Ipv4Protocol.ahRsvd "Link to this definition")  
Reserved value of IP authentication header (see RFC 4302

AssertExists()[¶](#tts.lib.ethernet.PacketIp4.Ipv4Protocol.AssertExists "Link to this definition")  
Raises an AssertionError if the accessed protocol does not exist at some time stamp. Example: Signal.tcp.AssertExists()

Returns:  The protocol itself, to support attribut chaining.

Raises:  
AssertionError

Return type:  *Self*

FindParent(*[protocol](#tts.lib.ethernet.PacketIp4.Ipv4Protocol.FindParent.protocol "tts.lib.ethernet.PacketIp4.Ipv4Protocol.FindParent.protocol (Python parameter) — The required protocol name.")*)[¶](#tts.lib.ethernet.PacketIp4.Ipv4Protocol.FindParent "Link to this definition")  
Returns a specific given protocol object if present, otherwise a [`NoProtocol`](#tts.lib.ethernet.PacketEthernet.NoProtocol "tts.lib.ethernet.PacketEthernet.NoProtocol (Python class) — Represents a non-present protocol. Accessing any other parent of a non-present protocol will also yield a NoProtocol object. Accessing any protocol specific attributes will lead to an AttributeError since the specific protocol is not available. The boolean value of a NoProtocol object is always False, such that it can be used to check for the precense/absence of a protocol layer.") object.

Parameters:  protocol : [OsiProtocol](#tts.lib.ethernet.PacketEthernet.OsiProtocol "tts.lib.ethernet.PacketEthernet.OsiProtocol (Python class) — String Enumeration class representing the supported protocol layers.")[¶](#tts.lib.ethernet.PacketIp4.Ipv4Protocol.FindParent.protocol "Permalink to this definition")  
The required protocol name.

Returns:  The required parent protocol object.

Return type:  [EthernetProtocolBase](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase (Python class) — Base class for all protocol classes.")

parent[¶](#tts.lib.ethernet.PacketIp4.Ipv4Protocol.parent "Link to this definition")  
Returns the parent protocol object if there is one present, otherwise None.

Return type:  [EthernetProtocolBase](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase (Python class) — Base class for all protocol classes.") | None

timestamp : float[¶](#tts.lib.ethernet.PacketIp4.Ipv4Protocol.timestamp "Link to this definition")  
current timestamp

### Ipv6Protocol[¶](#ipv6protocol "Link to this heading")

*class* Ipv6Protocol[¶](#tts.lib.ethernet.PacketIp6.Ipv6Protocol "Link to this definition")  

\<protocol\>  
Equivalent to method [`FindParent(protocol)`](#tts.lib.ethernet.PacketIp6.Ipv6Protocol.FindParent "tts.lib.ethernet.PacketIp6.Ipv6Protocol.FindParent (Python method) — Returns a specific given protocol object if present, otherwise a NoProtocol object."). Direct access to parent protocols. *protocol* is one of [`OsiProtocol`](#tts.lib.ethernet.PacketEthernet.OsiProtocol "tts.lib.ethernet.PacketEthernet.OsiProtocol (Python class) — String Enumeration class representing the supported protocol layers.").

Example: Signal.eth.src provides the source MAC address of the Ethernet protocol layer.

Type:  [`EthernetProtocolBase`](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase (Python class) — Base class for all protocol classes.")

src : str[¶](#tts.lib.ethernet.PacketIp6.Ipv6Protocol.src "Link to this definition")  
source IP address e.g. 2001:db8::1428:57ab

dst : str[¶](#tts.lib.ethernet.PacketIp6.Ipv6Protocol.dst "Link to this definition")  
destination IP address e.g. 2001:db8::1428:57ab

protocol : int[¶](#tts.lib.ethernet.PacketIp6.Ipv6Protocol.protocol "Link to this definition")  
protocol type / next header field

hopLimit : int[¶](#tts.lib.ethernet.PacketIp6.Ipv6Protocol.hopLimit "Link to this definition")  
hop limit field

payloadLength : int[¶](#tts.lib.ethernet.PacketIp6.Ipv6Protocol.payloadLength "Link to this definition")  
payload length from IPv6 header

trafficClass : int[¶](#tts.lib.ethernet.PacketIp6.Ipv6Protocol.trafficClass "Link to this definition")  
traffic class from IPv6 header

flowLabel : int[¶](#tts.lib.ethernet.PacketIp6.Ipv6Protocol.flowLabel "Link to this definition")  
flow label from IPv6 header

AssertExists()[¶](#tts.lib.ethernet.PacketIp6.Ipv6Protocol.AssertExists "Link to this definition")  
Raises an AssertionError if the accessed protocol does not exist at some time stamp. Example: Signal.tcp.AssertExists()

Returns:  The protocol itself, to support attribut chaining.

Raises:  
AssertionError

Return type:  *Self*

FindParent(*[protocol](#tts.lib.ethernet.PacketIp6.Ipv6Protocol.FindParent.protocol "tts.lib.ethernet.PacketIp6.Ipv6Protocol.FindParent.protocol (Python parameter) — The required protocol name.")*)[¶](#tts.lib.ethernet.PacketIp6.Ipv6Protocol.FindParent "Link to this definition")  
Returns a specific given protocol object if present, otherwise a [`NoProtocol`](#tts.lib.ethernet.PacketEthernet.NoProtocol "tts.lib.ethernet.PacketEthernet.NoProtocol (Python class) — Represents a non-present protocol. Accessing any other parent of a non-present protocol will also yield a NoProtocol object. Accessing any protocol specific attributes will lead to an AttributeError since the specific protocol is not available. The boolean value of a NoProtocol object is always False, such that it can be used to check for the precense/absence of a protocol layer.") object.

Parameters:  protocol : [OsiProtocol](#tts.lib.ethernet.PacketEthernet.OsiProtocol "tts.lib.ethernet.PacketEthernet.OsiProtocol (Python class) — String Enumeration class representing the supported protocol layers.")[¶](#tts.lib.ethernet.PacketIp6.Ipv6Protocol.FindParent.protocol "Permalink to this definition")  
The required protocol name.

Returns:  The required parent protocol object.

Return type:  [EthernetProtocolBase](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase (Python class) — Base class for all protocol classes.")

parent[¶](#tts.lib.ethernet.PacketIp6.Ipv6Protocol.parent "Link to this definition")  
Returns the parent protocol object if there is one present, otherwise None.

Return type:  [EthernetProtocolBase](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase (Python class) — Base class for all protocol classes.") | None

timestamp : float[¶](#tts.lib.ethernet.PacketIp6.Ipv6Protocol.timestamp "Link to this definition")  
current timestamp

### UdpProtocol[¶](#udpprotocol "Link to this heading")

*class* UdpProtocol[¶](#tts.lib.ethernet.PacketUdp.UdpProtocol "Link to this definition")  

\<protocol\>  
Equivalent to method [`FindParent(protocol)`](#tts.lib.ethernet.PacketUdp.UdpProtocol.FindParent "tts.lib.ethernet.PacketUdp.UdpProtocol.FindParent (Python method) — Returns a specific given protocol object if present, otherwise a NoProtocol object."). Direct access to parent protocols. *protocol* is one of [`OsiProtocol`](#tts.lib.ethernet.PacketEthernet.OsiProtocol "tts.lib.ethernet.PacketEthernet.OsiProtocol (Python class) — String Enumeration class representing the supported protocol layers.").

Example: Signal.eth.src provides the source MAC address of the Ethernet protocol layer.

Type:  [`EthernetProtocolBase`](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase (Python class) — Base class for all protocol classes.")

srcPort : int[¶](#tts.lib.ethernet.PacketUdp.UdpProtocol.srcPort "Link to this definition")  
source port

dstPort : int[¶](#tts.lib.ethernet.PacketUdp.UdpProtocol.dstPort "Link to this definition")  
destination port

AssertExists()[¶](#tts.lib.ethernet.PacketUdp.UdpProtocol.AssertExists "Link to this definition")  
Raises an AssertionError if the accessed protocol does not exist at some time stamp. Example: Signal.tcp.AssertExists()

Returns:  The protocol itself, to support attribut chaining.

Raises:  
AssertionError

Return type:  *Self*

FindParent(*[protocol](#tts.lib.ethernet.PacketUdp.UdpProtocol.FindParent.protocol "tts.lib.ethernet.PacketUdp.UdpProtocol.FindParent.protocol (Python parameter) — The required protocol name.")*)[¶](#tts.lib.ethernet.PacketUdp.UdpProtocol.FindParent "Link to this definition")  
Returns a specific given protocol object if present, otherwise a [`NoProtocol`](#tts.lib.ethernet.PacketEthernet.NoProtocol "tts.lib.ethernet.PacketEthernet.NoProtocol (Python class) — Represents a non-present protocol. Accessing any other parent of a non-present protocol will also yield a NoProtocol object. Accessing any protocol specific attributes will lead to an AttributeError since the specific protocol is not available. The boolean value of a NoProtocol object is always False, such that it can be used to check for the precense/absence of a protocol layer.") object.

Parameters:  protocol : [OsiProtocol](#tts.lib.ethernet.PacketEthernet.OsiProtocol "tts.lib.ethernet.PacketEthernet.OsiProtocol (Python class) — String Enumeration class representing the supported protocol layers.")[¶](#tts.lib.ethernet.PacketUdp.UdpProtocol.FindParent.protocol "Permalink to this definition")  
The required protocol name.

Returns:  The required parent protocol object.

Return type:  [EthernetProtocolBase](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase (Python class) — Base class for all protocol classes.")

parent[¶](#tts.lib.ethernet.PacketUdp.UdpProtocol.parent "Link to this definition")  
Returns the parent protocol object if there is one present, otherwise None.

Return type:  [EthernetProtocolBase](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase (Python class) — Base class for all protocol classes.") | None

packetLength : int[¶](#tts.lib.ethernet.PacketUdp.UdpProtocol.packetLength "Link to this definition")  
length of the UDP segment including the header length (8 Byte)

timestamp : float[¶](#tts.lib.ethernet.PacketUdp.UdpProtocol.timestamp "Link to this definition")  
current timestamp

checksum : int[¶](#tts.lib.ethernet.PacketUdp.UdpProtocol.checksum "Link to this definition")  
checksum

### TcpProtocol[¶](#tcpprotocol "Link to this heading")

*class* TcpProtocol[¶](#tts.lib.ethernet.PacketTcp.TcpProtocol "Link to this definition")  

\<protocol\>  
Equivalent to method [`FindParent(protocol)`](#tts.lib.ethernet.PacketTcp.TcpProtocol.FindParent "tts.lib.ethernet.PacketTcp.TcpProtocol.FindParent (Python method) — Returns a specific given protocol object if present, otherwise a NoProtocol object."). Direct access to parent protocols. *protocol* is one of [`OsiProtocol`](#tts.lib.ethernet.PacketEthernet.OsiProtocol "tts.lib.ethernet.PacketEthernet.OsiProtocol (Python class) — String Enumeration class representing the supported protocol layers.").

Example: Signal.eth.src provides the source MAC address of the Ethernet protocol layer.

Type:  [`EthernetProtocolBase`](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase (Python class) — Base class for all protocol classes.")

srcPort : int[¶](#tts.lib.ethernet.PacketTcp.TcpProtocol.srcPort "Link to this definition")  
source port

dstPort : int[¶](#tts.lib.ethernet.PacketTcp.TcpProtocol.dstPort "Link to this definition")  
destination port

seq : int[¶](#tts.lib.ethernet.PacketTcp.TcpProtocol.seq "Link to this definition")  
sequence number

packetLength : int[¶](#tts.lib.ethernet.PacketTcp.TcpProtocol.packetLength "Link to this definition")  
length of the whole TCP segment including header length

ack : int[¶](#tts.lib.ethernet.PacketTcp.TcpProtocol.ack "Link to this definition")  
Ack number

headerLength : int[¶](#tts.lib.ethernet.PacketTcp.TcpProtocol.headerLength "Link to this definition")  
TCP header length (data offset)

flags : int[¶](#tts.lib.ethernet.PacketTcp.TcpProtocol.flags "Link to this definition")  
flags

AssertExists()[¶](#tts.lib.ethernet.PacketTcp.TcpProtocol.AssertExists "Link to this definition")  
Raises an AssertionError if the accessed protocol does not exist at some time stamp. Example: Signal.tcp.AssertExists()

Returns:  The protocol itself, to support attribut chaining.

Raises:  
AssertionError

Return type:  *Self*

FindParent(*[protocol](#tts.lib.ethernet.PacketTcp.TcpProtocol.FindParent.protocol "tts.lib.ethernet.PacketTcp.TcpProtocol.FindParent.protocol (Python parameter) — The required protocol name.")*)[¶](#tts.lib.ethernet.PacketTcp.TcpProtocol.FindParent "Link to this definition")  
Returns a specific given protocol object if present, otherwise a [`NoProtocol`](#tts.lib.ethernet.PacketEthernet.NoProtocol "tts.lib.ethernet.PacketEthernet.NoProtocol (Python class) — Represents a non-present protocol. Accessing any other parent of a non-present protocol will also yield a NoProtocol object. Accessing any protocol specific attributes will lead to an AttributeError since the specific protocol is not available. The boolean value of a NoProtocol object is always False, such that it can be used to check for the precense/absence of a protocol layer.") object.

Parameters:  protocol : [OsiProtocol](#tts.lib.ethernet.PacketEthernet.OsiProtocol "tts.lib.ethernet.PacketEthernet.OsiProtocol (Python class) — String Enumeration class representing the supported protocol layers.")[¶](#tts.lib.ethernet.PacketTcp.TcpProtocol.FindParent.protocol "Permalink to this definition")  
The required protocol name.

Returns:  The required parent protocol object.

Return type:  [EthernetProtocolBase](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase (Python class) — Base class for all protocol classes.")

parent[¶](#tts.lib.ethernet.PacketTcp.TcpProtocol.parent "Link to this definition")  
Returns the parent protocol object if there is one present, otherwise None.

Return type:  [EthernetProtocolBase](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase (Python class) — Base class for all protocol classes.") | None

window : int[¶](#tts.lib.ethernet.PacketTcp.TcpProtocol.window "Link to this definition")  
window

timestamp : float[¶](#tts.lib.ethernet.PacketTcp.TcpProtocol.timestamp "Link to this definition")  
current timestamp

checksum : int[¶](#tts.lib.ethernet.PacketTcp.TcpProtocol.checksum "Link to this definition")  
checksum

urgentPointer : int[¶](#tts.lib.ethernet.PacketTcp.TcpProtocol.urgentPointer "Link to this definition")  
urgent pointer

### PtpProtocol[¶](#ptpprotocol "Link to this heading")

*class* PtpProtocol[¶](#tts.lib.ethernet.PacketPtp.PtpProtocol "Link to this definition")  

\<protocol\>  
Equivalent to method [`FindParent(protocol)`](#tts.lib.ethernet.PacketPtp.PtpProtocol.FindParent "tts.lib.ethernet.PacketPtp.PtpProtocol.FindParent (Python method) — Returns a specific given protocol object if present, otherwise a NoProtocol object."). Direct access to parent protocols. *protocol* is one of [`OsiProtocol`](#tts.lib.ethernet.PacketEthernet.OsiProtocol "tts.lib.ethernet.PacketEthernet.OsiProtocol (Python class) — String Enumeration class representing the supported protocol layers.").

Example: Signal.eth.src provides the source MAC address of the Ethernet protocol layer.

Type:  [`EthernetProtocolBase`](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase (Python class) — Base class for all protocol classes.")

messageType : int[¶](#tts.lib.ethernet.PacketPtp.PtpProtocol.messageType "Link to this definition")  
PTP message type

version : int[¶](#tts.lib.ethernet.PacketPtp.PtpProtocol.version "Link to this definition")  
PTP version

messageLength : int[¶](#tts.lib.ethernet.PacketPtp.PtpProtocol.messageLength "Link to this definition")  
PTP message length

domainNumber : int[¶](#tts.lib.ethernet.PacketPtp.PtpProtocol.domainNumber "Link to this definition")  
PTP domain number

flags : int[¶](#tts.lib.ethernet.PacketPtp.PtpProtocol.flags "Link to this definition")  
PTP flags

correctionField : int[¶](#tts.lib.ethernet.PacketPtp.PtpProtocol.correctionField "Link to this definition")  
PTP correctionField

sourcePortIdentity : bytes[¶](#tts.lib.ethernet.PacketPtp.PtpProtocol.sourcePortIdentity "Link to this definition")  
PTP source port identity

sequenceId : int[¶](#tts.lib.ethernet.PacketPtp.PtpProtocol.sequenceId "Link to this definition")  
PTP sequence ID

controlField : int[¶](#tts.lib.ethernet.PacketPtp.PtpProtocol.controlField "Link to this definition")  
PTP control field

logMessagePeriod : int[¶](#tts.lib.ethernet.PacketPtp.PtpProtocol.logMessagePeriod "Link to this definition")  
PTP log message interval

AssertExists()[¶](#tts.lib.ethernet.PacketPtp.PtpProtocol.AssertExists "Link to this definition")  
Raises an AssertionError if the accessed protocol does not exist at some time stamp. Example: Signal.tcp.AssertExists()

Returns:  The protocol itself, to support attribut chaining.

Raises:  
AssertionError

Return type:  *Self*

FindParent(*[protocol](#tts.lib.ethernet.PacketPtp.PtpProtocol.FindParent.protocol "tts.lib.ethernet.PacketPtp.PtpProtocol.FindParent.protocol (Python parameter) — The required protocol name.")*)[¶](#tts.lib.ethernet.PacketPtp.PtpProtocol.FindParent "Link to this definition")  
Returns a specific given protocol object if present, otherwise a [`NoProtocol`](#tts.lib.ethernet.PacketEthernet.NoProtocol "tts.lib.ethernet.PacketEthernet.NoProtocol (Python class) — Represents a non-present protocol. Accessing any other parent of a non-present protocol will also yield a NoProtocol object. Accessing any protocol specific attributes will lead to an AttributeError since the specific protocol is not available. The boolean value of a NoProtocol object is always False, such that it can be used to check for the precense/absence of a protocol layer.") object.

Parameters:  protocol : [OsiProtocol](#tts.lib.ethernet.PacketEthernet.OsiProtocol "tts.lib.ethernet.PacketEthernet.OsiProtocol (Python class) — String Enumeration class representing the supported protocol layers.")[¶](#tts.lib.ethernet.PacketPtp.PtpProtocol.FindParent.protocol "Permalink to this definition")  
The required protocol name.

Returns:  The required parent protocol object.

Return type:  [EthernetProtocolBase](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase (Python class) — Base class for all protocol classes.")

parent[¶](#tts.lib.ethernet.PacketPtp.PtpProtocol.parent "Link to this definition")  
Returns the parent protocol object if there is one present, otherwise None.

Return type:  [EthernetProtocolBase](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase (Python class) — Base class for all protocol classes.") | None

timestamp : float[¶](#tts.lib.ethernet.PacketPtp.PtpProtocol.timestamp "Link to this definition")  
current timestamp

### SomeIpProtocol[¶](#someipprotocol "Link to this heading")

*class* SomeIpProtocol[¶](#tts.lib.ethernet.PacketSomeIp.SomeIpProtocol "Link to this definition")  

\<protocol\>  
Equivalent to method [`FindParent(protocol)`](#tts.lib.ethernet.PacketSomeIp.SomeIpProtocol.FindParent "tts.lib.ethernet.PacketSomeIp.SomeIpProtocol.FindParent (Python method) — Returns a specific given protocol object if present, otherwise a NoProtocol object."). Direct access to parent protocols. *protocol* is one of [`OsiProtocol`](#tts.lib.ethernet.PacketEthernet.OsiProtocol "tts.lib.ethernet.PacketEthernet.OsiProtocol (Python class) — String Enumeration class representing the supported protocol layers.").

Example: Signal.eth.src provides the source MAC address of the Ethernet protocol layer.

Type:  [`EthernetProtocolBase`](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase (Python class) — Base class for all protocol classes.")

messageId : int[¶](#tts.lib.ethernet.PacketSomeIp.SomeIpProtocol.messageId "Link to this definition")  
message ID

serviceId : int[¶](#tts.lib.ethernet.PacketSomeIp.SomeIpProtocol.serviceId "Link to this definition")  
service ID (highest 16 bit from message id)

AssertExists()[¶](#tts.lib.ethernet.PacketSomeIp.SomeIpProtocol.AssertExists "Link to this definition")  
Raises an AssertionError if the accessed protocol does not exist at some time stamp. Example: Signal.tcp.AssertExists()

Returns:  The protocol itself, to support attribut chaining.

Raises:  
AssertionError

Return type:  *Self*

FindParent(*[protocol](#tts.lib.ethernet.PacketSomeIp.SomeIpProtocol.FindParent.protocol "tts.lib.ethernet.PacketSomeIp.SomeIpProtocol.FindParent.protocol (Python parameter) — The required protocol name.")*)[¶](#tts.lib.ethernet.PacketSomeIp.SomeIpProtocol.FindParent "Link to this definition")  
Returns a specific given protocol object if present, otherwise a [`NoProtocol`](#tts.lib.ethernet.PacketEthernet.NoProtocol "tts.lib.ethernet.PacketEthernet.NoProtocol (Python class) — Represents a non-present protocol. Accessing any other parent of a non-present protocol will also yield a NoProtocol object. Accessing any protocol specific attributes will lead to an AttributeError since the specific protocol is not available. The boolean value of a NoProtocol object is always False, such that it can be used to check for the precense/absence of a protocol layer.") object.

Parameters:  protocol : [OsiProtocol](#tts.lib.ethernet.PacketEthernet.OsiProtocol "tts.lib.ethernet.PacketEthernet.OsiProtocol (Python class) — String Enumeration class representing the supported protocol layers.")[¶](#tts.lib.ethernet.PacketSomeIp.SomeIpProtocol.FindParent.protocol "Permalink to this definition")  
The required protocol name.

Returns:  The required parent protocol object.

Return type:  [EthernetProtocolBase](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase (Python class) — Base class for all protocol classes.")

parent[¶](#tts.lib.ethernet.PacketSomeIp.SomeIpProtocol.parent "Link to this definition")  
Returns the parent protocol object if there is one present, otherwise None.

Return type:  [EthernetProtocolBase](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase (Python class) — Base class for all protocol classes.") | None

methodId : int[¶](#tts.lib.ethernet.PacketSomeIp.SomeIpProtocol.methodId "Link to this definition")  
method ID (lowest 16 bit from message id)

timestamp : float[¶](#tts.lib.ethernet.PacketSomeIp.SomeIpProtocol.timestamp "Link to this definition")  
current timestamp

length : int[¶](#tts.lib.ethernet.PacketSomeIp.SomeIpProtocol.length "Link to this definition")  
length from this header position

requestId : int[¶](#tts.lib.ethernet.PacketSomeIp.SomeIpProtocol.requestId "Link to this definition")  
request ID

clientId : int[¶](#tts.lib.ethernet.PacketSomeIp.SomeIpProtocol.clientId "Link to this definition")  
client id (highest 16 bit from request id)

sessionId : int[¶](#tts.lib.ethernet.PacketSomeIp.SomeIpProtocol.sessionId "Link to this definition")  
session id (lowest 16 bit from request id)

protocolVersion : int[¶](#tts.lib.ethernet.PacketSomeIp.SomeIpProtocol.protocolVersion "Link to this definition")  
SOME/IP Protocol version

interfaceVersion : int[¶](#tts.lib.ethernet.PacketSomeIp.SomeIpProtocol.interfaceVersion "Link to this definition")  
SOME/IP interface version

messageType : int[¶](#tts.lib.ethernet.PacketSomeIp.SomeIpProtocol.messageType "Link to this definition")  
message Type

returnCode : int[¶](#tts.lib.ethernet.PacketSomeIp.SomeIpProtocol.returnCode "Link to this definition")  
return code

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
