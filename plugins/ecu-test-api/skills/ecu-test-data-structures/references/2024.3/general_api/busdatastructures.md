# Advanced properties of bus related objects[¶](#advanced-properties-of-bus-related-objects "Link to this heading")

## CAN[¶](#can "Link to this heading")

*class* CanFrame[¶](#tts.testModule.bus.busObjects.CAN.CanFrame "Link to this definition")  
canID[¶](#tts.testModule.bus.busObjects.CAN.CanFrame.canID "Link to this definition")  
The CAN ID of the Frame

Type:  int

flags[¶](#tts.testModule.bus.busObjects.CAN.CanFrame.flags "Link to this definition")  
Any of the frame’s flags defined in the corresponding flags class can be accessed directly on the frame object, i.e. theFrame.aFlag instead of theFrame.flags.aFlag

Some of the flags can take the value False if the driver does not support the respective attribute.

Type:  [`CanFlags`](#tts.testModule.bus.busObjects.CAN.CanFlags "tts.testModule.bus.busObjects.CAN.CanFlags")

length[¶](#tts.testModule.bus.busObjects.CAN.CanFrame.length "Link to this definition")  
The frame’s length in Bytes

Type:  int

payload[¶](#tts.testModule.bus.busObjects.CAN.CanFrame.payload "Link to this definition")  
The frame’s payload

Type:  ByteStream

timestamp[¶](#tts.testModule.bus.busObjects.CAN.CanFrame.timestamp "Link to this definition")  
The frame’s timestamp in ms

Type:  float

*class* CanFlags[¶](#tts.testModule.bus.busObjects.CAN.CanFlags "Link to this definition")  
isError[¶](#tts.testModule.bus.busObjects.CAN.CanFlags.isError "Link to this definition")  
Is this an error frame?

Type:  bool

isRemote[¶](#tts.testModule.bus.busObjects.CAN.CanFlags.isRemote "Link to this definition")  
Is this an remote frame?

Type:  bool

isExtended[¶](#tts.testModule.bus.busObjects.CAN.CanFlags.isExtended "Link to this definition")  
Is this an extended-(29-Bit-)ID-frame?

Type:  bool

isSelfReceived[¶](#tts.testModule.bus.busObjects.CAN.CanFlags.isSelfReceived "Link to this definition")  
Was this frame sent by the controller that received it?

Type:  bool

isTx[¶](#tts.testModule.bus.busObjects.CAN.CanFlags.isTx "Link to this definition")  
Was this frame sent by the controller that received it? (alias for isSelfReceived)

Type:  bool

isEDL[¶](#tts.testModule.bus.busObjects.CAN.CanFlags.isEDL "Link to this definition")  
Does this frame has an extended data length?

Type:  bool

isBRS[¶](#tts.testModule.bus.busObjects.CAN.CanFlags.isBRS "Link to this definition")  
Was this frame received by using bit rate switching?

Type:  bool

## FlexRay[¶](#flexray "Link to this heading")

*class* FlexRayFrame[¶](#tts.testModule.bus.busObjects.FlexRay.FlexRayFrame "Link to this definition")  
slotID[¶](#tts.testModule.bus.busObjects.FlexRay.FlexRayFrame.slotID "Link to this definition")  
The slot ID of the Frame

Type:  int

cycleNumber[¶](#tts.testModule.bus.busObjects.FlexRay.FlexRayFrame.cycleNumber "Link to this definition")  
The cycle number of the Frame

Type:  int

headerCRC[¶](#tts.testModule.bus.busObjects.FlexRay.FlexRayFrame.headerCRC "Link to this definition")  
The header CRC of the Frame

Type:  int

channelID[¶](#tts.testModule.bus.busObjects.FlexRay.FlexRayFrame.channelID "Link to this definition")  
The ID of the FlexRay channel on which this frame was received

Type:  int

flags[¶](#tts.testModule.bus.busObjects.FlexRay.FlexRayFrame.flags "Link to this definition")  
Any of the frame’s flags defined in the corresponding flags class can be accessed directly on the frame object, i.e. theFrame.aFlag instead of theFrame.flags.aFlag

Some of the flags can take the value False if the driver does not support the respective attribute.

Type:  [`FlexRayFlags`](#tts.testModule.bus.busObjects.FlexRay.FlexRayFlags "tts.testModule.bus.busObjects.FlexRay.FlexRayFlags")

payload[¶](#tts.testModule.bus.busObjects.FlexRay.FlexRayFrame.payload "Link to this definition")  
The frame’s payload

Type:  ByteStream

timestamp[¶](#tts.testModule.bus.busObjects.FlexRay.FlexRayFrame.timestamp "Link to this definition")  
The frame’s timestamp in ms

Type:  float

*class* FlexRayFlags[¶](#tts.testModule.bus.busObjects.FlexRay.FlexRayFlags "Link to this definition")  
isSelfReceived[¶](#tts.testModule.bus.busObjects.FlexRay.FlexRayFlags.isSelfReceived "Link to this definition")  
Was this frame sent by the controller that received it?

Type:  bool

isTx[¶](#tts.testModule.bus.busObjects.FlexRay.FlexRayFlags.isTx "Link to this definition")  
Was this frame sent by the controller that received it? (alias for isSelfReceived)

Type:  bool

isNull[¶](#tts.testModule.bus.busObjects.FlexRay.FlexRayFlags.isNull "Link to this definition")  
Is this a null frame?

Type:  bool

isValid[¶](#tts.testModule.bus.busObjects.FlexRay.FlexRayFlags.isValid "Link to this definition")  
Is this frame valid?

Type:  bool

isSync[¶](#tts.testModule.bus.busObjects.FlexRay.FlexRayFlags.isSync "Link to this definition")  
Is this a sync frame?

Type:  bool

isStartup[¶](#tts.testModule.bus.busObjects.FlexRay.FlexRayFlags.isStartup "Link to this definition")  
Is this a startup frame?

Type:  bool

hasPayloadPreamble[¶](#tts.testModule.bus.busObjects.FlexRay.FlexRayFlags.hasPayloadPreamble "Link to this definition")  
Does this frame have a payload preamble?

Type:  bool

isError[¶](#tts.testModule.bus.busObjects.FlexRay.FlexRayFlags.isError "Link to this definition")  
Is this an error frame?

Type:  bool

isAsync[¶](#tts.testModule.bus.busObjects.FlexRay.FlexRayFlags.isAsync "Link to this definition")  
Was this frame received in asynchronous mode?

Type:  bool

isDynamic[¶](#tts.testModule.bus.busObjects.FlexRay.FlexRayFlags.isDynamic "Link to this definition")  
Is this a dynamic frame?

Type:  bool

## LIN[¶](#lin "Link to this heading")

*class* LinFrame[¶](#tts.testModule.bus.busObjects.LIN.LinFrame "Link to this definition")  
linID[¶](#tts.testModule.bus.busObjects.LIN.LinFrame.linID "Link to this definition")  
The LIN ID of the Frame

Type:  int

crc[¶](#tts.testModule.bus.busObjects.LIN.LinFrame.crc "Link to this definition")  
The CRC of the Frame

Type:  int

flags[¶](#tts.testModule.bus.busObjects.LIN.LinFrame.flags "Link to this definition")  
Any of the frame’s flags defined in the corresponding flags class can be accessed directly on the frame object, i.e. theFrame.aFlag instead of theFrame.flags.aFlag

Some of the flags can take the value False if the driver does not support the respective attribute.

Type:  [`LinFlags`](#tts.testModule.bus.busObjects.LIN.LinFlags "tts.testModule.bus.busObjects.LIN.LinFlags")

payload[¶](#tts.testModule.bus.busObjects.LIN.LinFrame.payload "Link to this definition")  
The frame’s payload

Type:  ByteStream

timestamp[¶](#tts.testModule.bus.busObjects.LIN.LinFrame.timestamp "Link to this definition")  
The frame’s timestamp in ms

Type:  float

*class* LinFlags[¶](#tts.testModule.bus.busObjects.LIN.LinFlags "Link to this definition")  
isCrcError[¶](#tts.testModule.bus.busObjects.LIN.LinFlags.isCrcError "Link to this definition")  
Does this frame have a CRC error?

Type:  bool

isSelfReceived[¶](#tts.testModule.bus.busObjects.LIN.LinFlags.isSelfReceived "Link to this definition")  
Was this frame sent by the controller that received it?

Type:  bool

isTx[¶](#tts.testModule.bus.busObjects.LIN.LinFlags.isTx "Link to this definition")  
Was this frame sent by the controller that received it? (alias for isSelfReceived)

Type:  bool

## Ethernet[¶](#ethernet "Link to this heading")

*class* Ethernet[¶](#tts.core.api.internalApi.Ethernet.Ethernet "Link to this definition")  
Access to various Ethernet related packet types and constants

UDP *= 17*[¶](#tts.core.api.internalApi.Ethernet.Ethernet.UDP "Link to this definition")  

TCP *= 6*[¶](#tts.core.api.internalApi.Ethernet.Ethernet.TCP "Link to this definition")  

PacketEthernet[¶](#tts.core.api.internalApi.Ethernet.Ethernet.PacketEthernet "Link to this definition")  
[`PacketEthernet`](#tts.lib.ethernet.PacketEthernet.PacketEthernet "tts.lib.ethernet.PacketEthernet.PacketEthernet")

PacketIp4[¶](#tts.core.api.internalApi.Ethernet.Ethernet.PacketIp4 "Link to this definition")  
[`PacketIp4`](#tts.lib.ethernet.PacketIp4.PacketIp4 "tts.lib.ethernet.PacketIp4.PacketIp4")

PacketIp6[¶](#tts.core.api.internalApi.Ethernet.Ethernet.PacketIp6 "Link to this definition")  
[`PacketIp6`](#tts.lib.ethernet.PacketIp6.PacketIp6 "tts.lib.ethernet.PacketIp6.PacketIp6")

PacketIcmp[¶](#tts.core.api.internalApi.Ethernet.Ethernet.PacketIcmp "Link to this definition")  
[`PacketIcmp`](#tts.lib.ethernet.PacketIcmp.PacketIcmp "tts.lib.ethernet.PacketIcmp.PacketIcmp")

PacketMka[¶](#tts.core.api.internalApi.Ethernet.Ethernet.PacketMka "Link to this definition")  
[`PacketMka`](#tts.lib.ethernet.PacketMka.PacketMka "tts.lib.ethernet.PacketMka.PacketMka")

PacketIke[¶](#tts.core.api.internalApi.Ethernet.Ethernet.PacketIke "Link to this definition")  
[`PacketIke`](#tts.lib.ethernet.PacketIke.PacketIke "tts.lib.ethernet.PacketIke.PacketIke")

PacketTcp[¶](#tts.core.api.internalApi.Ethernet.Ethernet.PacketTcp "Link to this definition")  
[`PacketTcp`](#tts.lib.ethernet.PacketTcp.PacketTcp "tts.lib.ethernet.PacketTcp.PacketTcp")

PacketUdp[¶](#tts.core.api.internalApi.Ethernet.Ethernet.PacketUdp "Link to this definition")  
[`PacketUdp`](#tts.lib.ethernet.PacketUdp.PacketUdp "tts.lib.ethernet.PacketUdp.PacketUdp")

PacketPtpSync[¶](#tts.core.api.internalApi.Ethernet.Ethernet.PacketPtpSync "Link to this definition")  
[`PacketPtpSync`](#tts.lib.ethernet.PacketPtp.PacketPtpSync "tts.lib.ethernet.PacketPtp.PacketPtpSync")

PacketPtpFollowUp[¶](#tts.core.api.internalApi.Ethernet.Ethernet.PacketPtpFollowUp "Link to this definition")  
[`PacketPtpFollowUp`](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp "tts.lib.ethernet.PacketPtp.PacketPtpFollowUp")

PacketPdelayReq[¶](#tts.core.api.internalApi.Ethernet.Ethernet.PacketPdelayReq "Link to this definition")  
[`PacketPdelayReq`](#tts.lib.ethernet.PacketPtp.PacketPdelayReq "tts.lib.ethernet.PacketPtp.PacketPdelayReq")

PacketPdelayResp[¶](#tts.core.api.internalApi.Ethernet.Ethernet.PacketPdelayResp "Link to this definition")  
[`PacketPdelayResp`](#tts.lib.ethernet.PacketPtp.PacketPdelayResp "tts.lib.ethernet.PacketPtp.PacketPdelayResp")

PacketPdelayRespFollowUp[¶](#tts.core.api.internalApi.Ethernet.Ethernet.PacketPdelayRespFollowUp "Link to this definition")  
[`PacketPdelayRespFollowUp`](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp "tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp")

PacketSomeIp[¶](#tts.core.api.internalApi.Ethernet.Ethernet.PacketSomeIp "Link to this definition")  
[`PacketSomeIp`](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp "tts.lib.ethernet.PacketSomeIp.PacketSomeIp")

PacketSomeIpSd[¶](#tts.core.api.internalApi.Ethernet.Ethernet.PacketSomeIpSd "Link to this definition")  
[`PacketSomeIpSd`](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSd "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSd")

PacketSomeIpSdEntry[¶](#tts.core.api.internalApi.Ethernet.Ethernet.PacketSomeIpSdEntry "Link to this definition")  
[`PacketSomeIpSdEntry`](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntry "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntry")

PacketSomeIpSdEntryService[¶](#tts.core.api.internalApi.Ethernet.Ethernet.PacketSomeIpSdEntryService "Link to this definition")  
[`PacketSomeIpSdEntryService`](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryService "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryService")

PacketSomeIpSdEntryEventgroup[¶](#tts.core.api.internalApi.Ethernet.Ethernet.PacketSomeIpSdEntryEventgroup "Link to this definition")  
[`PacketSomeIpSdEntryEventgroup`](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryEventgroup "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryEventgroup")

PacketSomeIpSdOptionIpv4[¶](#tts.core.api.internalApi.Ethernet.Ethernet.PacketSomeIpSdOptionIpv4 "Link to this definition")  
[`PacketSomeIpSdOptionIpv4`](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4 "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4")

PacketSomeIpSdOption[¶](#tts.core.api.internalApi.Ethernet.Ethernet.PacketSomeIpSdOption "Link to this definition")  
[`PacketSomeIpSdOption`](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOption "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOption")

PacketSomeIpSdOptionIpv6[¶](#tts.core.api.internalApi.Ethernet.Ethernet.PacketSomeIpSdOptionIpv6 "Link to this definition")  
[`PacketSomeIpSdOptionIpv6`](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6 "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6")

PacketSomeIpSdOptionIpv4Multicast[¶](#tts.core.api.internalApi.Ethernet.Ethernet.PacketSomeIpSdOptionIpv4Multicast "Link to this definition")  
[`PacketSomeIpSdOptionIpv4Multicast`](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4Multicast "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4Multicast")

PacketSomeIpSdOptionIpv6Multicast[¶](#tts.core.api.internalApi.Ethernet.Ethernet.PacketSomeIpSdOptionIpv6Multicast "Link to this definition")  
[`PacketSomeIpSdOptionIpv6Multicast`](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6Multicast "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6Multicast")

PacketSomeIpSdOptionIpv4SD[¶](#tts.core.api.internalApi.Ethernet.Ethernet.PacketSomeIpSdOptionIpv4SD "Link to this definition")  
[`PacketSomeIpSdOptionIpv4SD`](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4SD "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4SD")

PacketSomeIpSdOptionIpv6SD[¶](#tts.core.api.internalApi.Ethernet.Ethernet.PacketSomeIpSdOptionIpv6SD "Link to this definition")  
[`PacketSomeIpSdOptionIpv6SD`](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6SD "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6SD")

PacketSomeIpSdOptionConfig[¶](#tts.core.api.internalApi.Ethernet.Ethernet.PacketSomeIpSdOptionConfig "Link to this definition")  
[`PacketSomeIpSdOptionConfig`](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionConfig "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionConfig")

### PacketEthernet[¶](#packetethernet "Link to this heading")

*class* PacketEthernet[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet "Link to this definition")  
In the test case, use `api.Ethernet.PacketEthernet`; in UserPyModules, use `from tts.lib.ethernet.PacketEthernet import PacketEthernet`.

\<protocol\>  
Equivalent to method [`FindParent(protocol)`](#tts.lib.ethernet.PacketEthernet.PacketEthernet.FindParent "tts.lib.ethernet.PacketEthernet.PacketEthernet.FindParent"). Direct access to parent protocols. *protocol* is one of [`OsiProtocol`](#tts.lib.ethernet.PacketEthernet.OsiProtocol "tts.lib.ethernet.PacketEthernet.OsiProtocol").

Example: Signal.eth.src provides the source MAC address of the Ethernet protocol layer.

Type:  [`EthernetProtocolBase`](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase")

GetEthDstMac()[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.GetEthDstMac "Link to this definition")  
Returns:  target MAC address e.g. DE:AD:BE:EF:FF:00

Return type:  str

SetEthDstMac(*mac*)[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.SetEthDstMac "Link to this definition")  
Parameters:  **mac** (*str*) – target MAC address e.g. DE:AD:BE:EF:FF:00

ethDstMac[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.ethDstMac "Link to this definition")  
target MAC address e.g. DE:AD:BE:EF:FF:00

Type:  str

GetEthSrcMac()[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.GetEthSrcMac "Link to this definition")  
Returns:  source MAC address e.g. DE:AD:BE:EF:FF:00

Return type:  str

SetEthSrcMac(*mac*)[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.SetEthSrcMac "Link to this definition")  
Parameters:  **mac** (*str*) – source MAC addres e.g. DE:AD:BE:EF:FF:00

ethSrcMac[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.ethSrcMac "Link to this definition")  
source MAC address e.g. DE:AD:BE:EF:FF:00

Type:  str

GetEthType()[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.GetEthType "Link to this definition")  
Returns:  ethernet protocol type

Return type:  int

SetEthType(*ethType*)[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.SetEthType "Link to this definition")  
Parameters:  **ethType** (*int*) – ethernet protocol type

ethType[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.ethType "Link to this definition")  
ethernet protocol type

Type:  int

GetVlanPcp(*ixVlanTags*)[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.GetVlanPcp "Link to this definition")  
Returns:  802.1a priority code point

Return type:  int

SetVlanPcp(*pcp*)[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.SetVlanPcp "Link to this definition")  
Parameters:  **pcp** (*int*) – 802.1a priority code point

vlanPcp[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.vlanPcp "Link to this definition")  
802.1a priority code point

Type:  int

GetVlanCfi(*ixVlanTags*)[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.GetVlanCfi "Link to this definition")  
Returns:  802.1a canonical format indicator

Return type:  int

SetVlanCfi(*cfi*)[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.SetVlanCfi "Link to this definition")  
Parameters:  **cfi** (*int*) – 802.1a canonical format indicator

vlanCfi[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.vlanCfi "Link to this definition")  
802.1a canonical format indicator

Type:  int

GetVlanVid(*ixVlanTags*)[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.GetVlanVid "Link to this definition")  
Returns:  802.1a VLAN id

Return type:  int

SetVlanVid(*vid*)[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.SetVlanVid "Link to this definition")  
Parameters:  **vid** (*int*) – 802.1a VLAN id

vlanVid[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.vlanVid "Link to this definition")  
802.1a VLAN id

Type:  int

GetVlanPcpOuter(*ixVlanTags*)[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.GetVlanPcpOuter "Link to this definition")  
Returns:  802.1ad priority code point

Return type:  int

SetVlanPcpOuter(*pcp*)[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.SetVlanPcpOuter "Link to this definition")  
Parameters:  **pcp** (*int*) – 802.1ad priority code point

vlanPcpOuter[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.vlanPcpOuter "Link to this definition")  
802.1ad priority code point

Type:  int

GetVlanCfiOuter(*ixVlanTags*)[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.GetVlanCfiOuter "Link to this definition")  
Returns:  802.1ad canonical format indicator

Return type:  int

SetVlanCfiOuter(*cfi*)[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.SetVlanCfiOuter "Link to this definition")  
Parameters:  **cfi** (*int*) – 802.1ad canonical format indicator

vlanCfiOuter[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.vlanCfiOuter "Link to this definition")  
802.1ad canonical format indicator

Type:  int

GetVlanVidOuter(*ixVlanTags*)[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.GetVlanVidOuter "Link to this definition")  
Returns:  802.1ad VLAN id

Return type:  int

SetVlanVidOuter(*vid*)[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.SetVlanVidOuter "Link to this definition")  
Parameters:  **vid** (*int*) – 802.1ad VLAN id

vlanVidOuter[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.vlanVidOuter "Link to this definition")  
802.1ad VLAN id

Type:  int

GetEthPayload()[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.GetEthPayload "Link to this definition")  
Returns:  Ethernet payload

Return type:  bytes

SetEthPayload(*payload*)[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.SetEthPayload "Link to this definition")  
Parameters:  **payload** (*bytes*) – Ethernet payload

ethPayload[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.ethPayload "Link to this definition")  
Ethernet payload

Type:  bytes

GetMacSecTciAn()[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.GetMacSecTciAn "Link to this definition")  
Returns:  TCI_AN byte of MACsec header (see IEEE 802.1AE)

Return type:  int

macSecTciAn[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.macSecTciAn "Link to this definition")  
TCI_AN byte of MACsec header (see IEEE 802.1AE)

Type:  int

GetMacSecTci()[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.GetMacSecTci "Link to this definition")  
Returns:  TAG Control Information of MACsec header (see IEEE 802.1AE)

Return type:  int

macSecTci[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.macSecTci "Link to this definition")  
TAG Control Information of MACsec header (see IEEE 802.1AE)

Type:  int

GetMacSecTciV()[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.GetMacSecTciV "Link to this definition")  
Returns:  Version bit in TCI of MACsec header (see IEEE 802.1AE)

Return type:  bool

macSecTciV[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.macSecTciV "Link to this definition")  
Version bit in TCI of MACsec header (see IEEE 802.1AE)

Type:  bool

GetMacSecTciEs()[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.GetMacSecTciEs "Link to this definition")  
Returns:  End station bit in TCI of MACsec header (see IEEE 802.1AE)

Return type:  bool

macSecTciEs[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.macSecTciEs "Link to this definition")  
End station bit in TCI of MACsec header (see IEEE 802.1AE)

Type:  bool

GetMacSecTciSc()[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.GetMacSecTciSc "Link to this definition")  
Returns:  SCI indication bit in TCI of MACsec header (see IEEE 802.1AE)

Return type:  bool

macSecTciSc[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.macSecTciSc "Link to this definition")  
SCI indication bit in TCI of MACsec header (see IEEE 802.1AE)

Type:  bool

GetMacSecTciScb()[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.GetMacSecTciScb "Link to this definition")  
Returns:  Single copy broadcast capability bit in TCI of MACsec header (see IEEE 802.1AE)

Return type:  bool

macSecTciScb[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.macSecTciScb "Link to this definition")  
Single copy broadcast capability bit in TCI of MACsec header (see IEEE 802.1AE)

Type:  bool

GetMacSecTciE()[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.GetMacSecTciE "Link to this definition")  
Returns:  Encryption bit in TCI of MACsec header (see IEEE 802.1AE)

Return type:  bool

macSecTciE[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.macSecTciE "Link to this definition")  
Encryption bit in TCI of MACsec header (see IEEE 802.1AE)

Type:  bool

GetMacSecTciC()[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.GetMacSecTciC "Link to this definition")  
Returns:  Changed text bit in TCI of MACsec header (see IEEE 802.1AE)

Return type:  bool

macSecTciC[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.macSecTciC "Link to this definition")  
Changed text bit in TCI of MACsec header (see IEEE 802.1AE)

Type:  bool

GetMacSecAn()[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.GetMacSecAn "Link to this definition")  
Returns:  Association Number of MACsec header (see IEEE 802.1AE)

Return type:  int

macSecAn[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.macSecAn "Link to this definition")  
Association Number of MACsec header (see IEEE 802.1AE)

Type:  int

GetMacSecSl()[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.GetMacSecSl "Link to this definition")  
Returns:  Short Length of MACsec header (see IEEE 802.1AE)

Return type:  int

macSecSl[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.macSecSl "Link to this definition")  
Short Length of MACsec header (see IEEE 802.1AE)

Type:  int

GetMacSecPn()[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.GetMacSecPn "Link to this definition")  
Returns:  Packet Number of MACsec header (see IEEE 802.1AE)

Return type:  int

macSecPn[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.macSecPn "Link to this definition")  
Packet Number of MACsec header (see IEEE 802.1AE)

Type:  int

GetMacSecSci()[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.GetMacSecSci "Link to this definition")  
Returns:  Secure Channel Identifier of MACsec header (see IEEE 802.1AE)

Return type:  bytes

macSecSci[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.macSecSci "Link to this definition")  
Secure Channel Identifier of MACsec header (see IEEE 802.1AE)

Type:  bytes

GetMacSecIcv()[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.GetMacSecIcv "Link to this definition")  
Returns:  Integrity check value of MACsec header (see IEEE 802.1AE)

Return type:  bytes

macSecIcv[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.macSecIcv "Link to this definition")  
Integrity check value of MACsec header (see IEEE 802.1AE)

Type:  bytes

FindParent(*protocol*)[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.FindParent "Link to this definition")  
*Only for pseudo signals in trace analysis!* Returns the requested protocol object if present, otherwise a [`NoProtocol`](#tts.lib.ethernet.PacketEthernet.NoProtocol "tts.lib.ethernet.PacketEthernet.NoProtocol") object.

Parameters:  **protocol** ([*OsiProtocol*](#tts.lib.ethernet.PacketEthernet.OsiProtocol "tts.lib.ethernet.PacketEthernet.OsiProtocol")) – The required protocol name.

Returns:  The required parent protocol object.

Return type:  [EthernetProtocolBase](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase")

GetTimestamp()[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.GetTimestamp "Link to this definition")  
Returns:  Receive timestamp in sec., None if not available

Return type:  float | None

SetTimestamp(*timestamp*)[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.SetTimestamp "Link to this definition")  
Parameters:  **timestamp** (*float* *|* *None*) – Receive timestamp in sec., None if not available

parent[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.parent "Link to this definition")  
*Only for pseudo signals in trace analysis!* Returns the parent protocol object if there is one present, otherwise None.

Return type:  [EthernetProtocolBase](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase") | None

timestamp[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.timestamp "Link to this definition")  
Receive timestamp in sec., None if not available

Type:  Optional[float]

### PacketIp4[¶](#packetip4 "Link to this heading")

*class* PacketIp4[¶](#tts.lib.ethernet.PacketIp4.PacketIp4 "Link to this definition")  
In the test case, use `api.Ethernet.PacPacketIp4`; in UserPyModules, use `from tts.lib.ethernet.PacketIp4 import PacketIp4`.

\<protocol\>  
Equivalent to method [`FindParent(protocol)`](#tts.lib.ethernet.PacketIp4.PacketIp4.FindParent "tts.lib.ethernet.PacketIp4.PacketIp4.FindParent"). Direct access to parent protocols. *protocol* is one of [`OsiProtocol`](#tts.lib.ethernet.PacketEthernet.OsiProtocol "tts.lib.ethernet.PacketEthernet.OsiProtocol").

Example: Signal.eth.src provides the source MAC address of the Ethernet protocol layer.

Type:  [`EthernetProtocolBase`](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase")

GetIpVersionAndHeaderLength()[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.GetIpVersionAndHeaderLength "Link to this definition")  
Returns:  protocol version and header length

Return type:  int

SetIpVersionAndHeaderLength(*versionHeader*)[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.SetIpVersionAndHeaderLength "Link to this definition")  
Parameters:  **versionHeader** (*int*) – protocol version and header length

ipVersionHeader[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.ipVersionHeader "Link to this definition")  
protocol version and header length

Type:  int

GetIpTos()[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.GetIpTos "Link to this definition")  
Returns:  type of service

Return type:  int

SetIpTos(*tos*)[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.SetIpTos "Link to this definition")  
Parameters:  **tos** (*int*) – type of service

ipTos[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.ipTos "Link to this definition")  
type of service

Type:  int

GetIpLen()[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.GetIpLen "Link to this definition")  
Returns:  packet length

Return type:  int

SetIpLen(*length*)[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.SetIpLen "Link to this definition")  
Parameters:  **length** (*int*) – packet length

ipLen[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.ipLen "Link to this definition")  
packet length

Type:  int

GetIpIdent()[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.GetIpIdent "Link to this definition")  
Returns:  identifier

Return type:  int

SetIpIdent(*ident*)[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.SetIpIdent "Link to this definition")  
Parameters:  **ident** (*int*) – identifier

ipIdent[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.ipIdent "Link to this definition")  
identifier

Type:  int

GetIpOffset()[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.GetIpOffset "Link to this definition")  
Returns:  flags and offset combined

Return type:  int

SetIpOffset(*offset*)[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.SetIpOffset "Link to this definition")  
Parameters:  **offset** (*int*) – flags and offset combined

ipOffset[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.ipOffset "Link to this definition")  
flags and offset combined

Type:  int

GetIpTtl()[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.GetIpTtl "Link to this definition")  
Returns:  TTL

Return type:  int

SetIpTtl(*ttl*)[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.SetIpTtl "Link to this definition")  
Parameters:  **ttl** (*int*) – TTL

ipTtl[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.ipTtl "Link to this definition")  
TTL

Type:  int

GetIpProt()[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.GetIpProt "Link to this definition")  
Returns:  protocol type / next header field

Return type:  int

SetIpProt(*prot*)[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.SetIpProt "Link to this definition")  
Parameters:  **prot** (*int*) – protocol type

ipProt[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.ipProt "Link to this definition")  
protocol type / next header field

Type:  int

GetIpChecksum()[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.GetIpChecksum "Link to this definition")  
Returns:  checksum

Return type:  int

SetIpChecksum(*checksum*)[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.SetIpChecksum "Link to this definition")  
Parameters:  **checksum** (*int*) – checksum

ipChecksum[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.ipChecksum "Link to this definition")  
checksum

Type:  int

GetIpSrc()[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.GetIpSrc "Link to this definition")  
Returns:  source IP address e.g. 127.0.0.1

Return type:  str

SetIpSrc(*addr*)[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.SetIpSrc "Link to this definition")  
Parameters:  **addr** (*str*) – source IP address e.g. 127.0.0.1

ipSrc[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.ipSrc "Link to this definition")  
source IP address e.g. 127.0.0.1

Type:  str

GetIpDst()[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.GetIpDst "Link to this definition")  
Returns:  target IP address e.g. 127.0.0.1

Return type:  str

SetIpDst(*addr*)[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.SetIpDst "Link to this definition")  
Parameters:  **addr** (*str*) – target IP address e.g. 127.0.0.1

ipDst[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.ipDst "Link to this definition")  
target IP address e.g. 127.0.0.1

Type:  str

GetIpPayload()[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.GetIpPayload "Link to this definition")  
Returns:  IP payload

Return type:  bytes

SetIpPayload(*payload*)[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.SetIpPayload "Link to this definition")  
Parameters:  **payload** (*bytes*) – IP payload

ipPayload[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.ipPayload "Link to this definition")  
IP payload

Type:  bytes

GetIpAhSpi()[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.GetIpAhSpi "Link to this definition")  
Returns:  Security parameters index of IP authentication header (see RFC 4302)

Return type:  int

ipAhSpi[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.ipAhSpi "Link to this definition")  
Security parameters index of IP authentication header (see RFC 4302)

Type:  int

GetIpAhSeq()[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.GetIpAhSeq "Link to this definition")  
Returns:  Sequence number field of IP authentication header (see RFC 4302)

Return type:  int

ipAhSeq[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.ipAhSeq "Link to this definition")  
Sequence number field of IP authentication header (see RFC 4302)

Type:  int

GetIpAhIcv()[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.GetIpAhIcv "Link to this definition")  
Returns:  Integrity check value of IP authentication header (see RFC 4302)

Return type:  bytes

ipAhIcv[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.ipAhIcv "Link to this definition")  
Integrity check value of IP authentication header (see RFC 4302)

Type:  bytes

GetIpAhNxt()[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.GetIpAhNxt "Link to this definition")  
Returns:  Next header value of IP authentication header (see RFC 4302)

Return type:  int

ipAhNxt[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.ipAhNxt "Link to this definition")  
Next header value of IP authentication header (see RFC 4302)

Type:  int

GetIpAhLen()[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.GetIpAhLen "Link to this definition")  
Returns:  Length value of IP authentication header (see RFC 4302) =\> len(ICV)/4+1

Return type:  int

ipAhLen[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.ipAhLen "Link to this definition")  
Length value of IP authentication header (see RFC 4302) =\> len(ICV)/4+1

Type:  int

GetIpAhRsvd()[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.GetIpAhRsvd "Link to this definition")  
Returns:  Reserved value of IP authentication header (see RFC 4302)

Return type:  int

ipAhRsvd[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.ipAhRsvd "Link to this definition")  
Reserved value of IP authentication header (see RFC 4302)

Type:  int

CalcIpLen()[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.CalcIpLen "Link to this definition")  
Calculate and set the current length of this IP packet

FindParent(*protocol*)[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.FindParent "Link to this definition")  
*Only for pseudo signals in trace analysis!* Returns the requested protocol object if present, otherwise a [`NoProtocol`](#tts.lib.ethernet.PacketEthernet.NoProtocol "tts.lib.ethernet.PacketEthernet.NoProtocol") object.

Parameters:  **protocol** ([*OsiProtocol*](#tts.lib.ethernet.PacketEthernet.OsiProtocol "tts.lib.ethernet.PacketEthernet.OsiProtocol")) – The required protocol name.

Returns:  The required parent protocol object.

Return type:  [EthernetProtocolBase](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase")

GetEthDstMac()[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.GetEthDstMac "Link to this definition")  
Returns:  target MAC address e.g. DE:AD:BE:EF:FF:00

Return type:  str

GetEthPayload()[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.GetEthPayload "Link to this definition")  
Returns:  Ethernet payload

Return type:  bytes

GetEthSrcMac()[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.GetEthSrcMac "Link to this definition")  
Returns:  source MAC address e.g. DE:AD:BE:EF:FF:00

Return type:  str

GetEthType()[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.GetEthType "Link to this definition")  
Returns:  ethernet protocol type

Return type:  int

GetMacSecAn()[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.GetMacSecAn "Link to this definition")  
Returns:  Association Number of MACsec header (see IEEE 802.1AE)

Return type:  int

GetMacSecIcv()[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.GetMacSecIcv "Link to this definition")  
Returns:  Integrity check value of MACsec header (see IEEE 802.1AE)

Return type:  bytes

GetMacSecPn()[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.GetMacSecPn "Link to this definition")  
Returns:  Packet Number of MACsec header (see IEEE 802.1AE)

Return type:  int

GetMacSecSci()[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.GetMacSecSci "Link to this definition")  
Returns:  Secure Channel Identifier of MACsec header (see IEEE 802.1AE)

Return type:  bytes

GetMacSecSl()[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.GetMacSecSl "Link to this definition")  
Returns:  Short Length of MACsec header (see IEEE 802.1AE)

Return type:  int

GetMacSecTci()[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.GetMacSecTci "Link to this definition")  
Returns:  TAG Control Information of MACsec header (see IEEE 802.1AE)

Return type:  int

GetMacSecTciAn()[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.GetMacSecTciAn "Link to this definition")  
Returns:  TCI_AN byte of MACsec header (see IEEE 802.1AE)

Return type:  int

GetMacSecTciC()[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.GetMacSecTciC "Link to this definition")  
Returns:  Changed text bit in TCI of MACsec header (see IEEE 802.1AE)

Return type:  bool

GetMacSecTciE()[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.GetMacSecTciE "Link to this definition")  
Returns:  Encryption bit in TCI of MACsec header (see IEEE 802.1AE)

Return type:  bool

GetMacSecTciEs()[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.GetMacSecTciEs "Link to this definition")  
Returns:  End station bit in TCI of MACsec header (see IEEE 802.1AE)

Return type:  bool

GetMacSecTciSc()[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.GetMacSecTciSc "Link to this definition")  
Returns:  SCI indication bit in TCI of MACsec header (see IEEE 802.1AE)

Return type:  bool

GetMacSecTciScb()[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.GetMacSecTciScb "Link to this definition")  
Returns:  Single copy broadcast capability bit in TCI of MACsec header (see IEEE 802.1AE)

Return type:  bool

GetMacSecTciV()[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.GetMacSecTciV "Link to this definition")  
Returns:  Version bit in TCI of MACsec header (see IEEE 802.1AE)

Return type:  bool

GetTimestamp()[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.GetTimestamp "Link to this definition")  
Returns:  Receive timestamp in sec., None if not available

Return type:  float | None

GetVlanCfi(*ixVlanTags*)[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.GetVlanCfi "Link to this definition")  
Returns:  802.1a canonical format indicator

Return type:  int

GetVlanCfiOuter(*ixVlanTags*)[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.GetVlanCfiOuter "Link to this definition")  
Returns:  802.1ad canonical format indicator

Return type:  int

GetVlanPcp(*ixVlanTags*)[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.GetVlanPcp "Link to this definition")  
Returns:  802.1a priority code point

Return type:  int

GetVlanPcpOuter(*ixVlanTags*)[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.GetVlanPcpOuter "Link to this definition")  
Returns:  802.1ad priority code point

Return type:  int

GetVlanVid(*ixVlanTags*)[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.GetVlanVid "Link to this definition")  
Returns:  802.1a VLAN id

Return type:  int

GetVlanVidOuter(*ixVlanTags*)[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.GetVlanVidOuter "Link to this definition")  
Returns:  802.1ad VLAN id

Return type:  int

SetEthDstMac(*mac*)[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.SetEthDstMac "Link to this definition")  
Parameters:  **mac** (*str*) – target MAC address e.g. DE:AD:BE:EF:FF:00

SetEthPayload(*payload*)[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.SetEthPayload "Link to this definition")  
Parameters:  **payload** (*bytes*) – Ethernet payload

SetEthSrcMac(*mac*)[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.SetEthSrcMac "Link to this definition")  
Parameters:  **mac** (*str*) – source MAC addres e.g. DE:AD:BE:EF:FF:00

SetEthType(*ethType*)[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.SetEthType "Link to this definition")  
Parameters:  **ethType** (*int*) – ethernet protocol type

SetTimestamp(*timestamp*)[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.SetTimestamp "Link to this definition")  
Parameters:  **timestamp** (*float* *|* *None*) – Receive timestamp in sec., None if not available

SetVlanCfi(*cfi*)[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.SetVlanCfi "Link to this definition")  
Parameters:  **cfi** (*int*) – 802.1a canonical format indicator

SetVlanCfiOuter(*cfi*)[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.SetVlanCfiOuter "Link to this definition")  
Parameters:  **cfi** (*int*) – 802.1ad canonical format indicator

SetVlanPcp(*pcp*)[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.SetVlanPcp "Link to this definition")  
Parameters:  **pcp** (*int*) – 802.1a priority code point

SetVlanPcpOuter(*pcp*)[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.SetVlanPcpOuter "Link to this definition")  
Parameters:  **pcp** (*int*) – 802.1ad priority code point

SetVlanVid(*vid*)[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.SetVlanVid "Link to this definition")  
Parameters:  **vid** (*int*) – 802.1a VLAN id

SetVlanVidOuter(*vid*)[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.SetVlanVidOuter "Link to this definition")  
Parameters:  **vid** (*int*) – 802.1ad VLAN id

ethDstMac[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.ethDstMac "Link to this definition")  
target MAC address e.g. DE:AD:BE:EF:FF:00

Type:  str

ethPayload[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.ethPayload "Link to this definition")  
Ethernet payload

Type:  bytes

ethSrcMac[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.ethSrcMac "Link to this definition")  
source MAC address e.g. DE:AD:BE:EF:FF:00

Type:  str

ethType[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.ethType "Link to this definition")  
ethernet protocol type

Type:  int

macSecAn[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.macSecAn "Link to this definition")  
Association Number of MACsec header (see IEEE 802.1AE)

Type:  int

macSecIcv[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.macSecIcv "Link to this definition")  
Integrity check value of MACsec header (see IEEE 802.1AE)

Type:  bytes

macSecPn[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.macSecPn "Link to this definition")  
Packet Number of MACsec header (see IEEE 802.1AE)

Type:  int

macSecSci[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.macSecSci "Link to this definition")  
Secure Channel Identifier of MACsec header (see IEEE 802.1AE)

Type:  bytes

macSecSl[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.macSecSl "Link to this definition")  
Short Length of MACsec header (see IEEE 802.1AE)

Type:  int

macSecTci[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.macSecTci "Link to this definition")  
TAG Control Information of MACsec header (see IEEE 802.1AE)

Type:  int

macSecTciAn[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.macSecTciAn "Link to this definition")  
TCI_AN byte of MACsec header (see IEEE 802.1AE)

Type:  int

macSecTciC[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.macSecTciC "Link to this definition")  
Changed text bit in TCI of MACsec header (see IEEE 802.1AE)

Type:  bool

macSecTciE[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.macSecTciE "Link to this definition")  
Encryption bit in TCI of MACsec header (see IEEE 802.1AE)

Type:  bool

macSecTciEs[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.macSecTciEs "Link to this definition")  
End station bit in TCI of MACsec header (see IEEE 802.1AE)

Type:  bool

macSecTciSc[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.macSecTciSc "Link to this definition")  
SCI indication bit in TCI of MACsec header (see IEEE 802.1AE)

Type:  bool

macSecTciScb[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.macSecTciScb "Link to this definition")  
Single copy broadcast capability bit in TCI of MACsec header (see IEEE 802.1AE)

Type:  bool

macSecTciV[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.macSecTciV "Link to this definition")  
Version bit in TCI of MACsec header (see IEEE 802.1AE)

Type:  bool

parent[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.parent "Link to this definition")  
*Only for pseudo signals in trace analysis!* Returns the parent protocol object if there is one present, otherwise None.

Return type:  [EthernetProtocolBase](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase") | None

timestamp[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.timestamp "Link to this definition")  
Receive timestamp in sec., None if not available

Type:  Optional[float]

vlanCfi[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.vlanCfi "Link to this definition")  
802.1a canonical format indicator

Type:  int

vlanCfiOuter[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.vlanCfiOuter "Link to this definition")  
802.1ad canonical format indicator

Type:  int

vlanPcp[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.vlanPcp "Link to this definition")  
802.1a priority code point

Type:  int

vlanPcpOuter[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.vlanPcpOuter "Link to this definition")  
802.1ad priority code point

Type:  int

vlanVid[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.vlanVid "Link to this definition")  
802.1a VLAN id

Type:  int

vlanVidOuter[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.vlanVidOuter "Link to this definition")  
802.1ad VLAN id

Type:  int

### PacketIp6[¶](#packetip6 "Link to this heading")

*class* PacketIp6[¶](#tts.lib.ethernet.PacketIp6.PacketIp6 "Link to this definition")  
In the test case, use `api.Ethernet.PacketIp6`; in UserPyModules, use `from tts.lib.ethernet.PacketIp6 import PacketIp6`.

\<protocol\>  
Equivalent to method [`FindParent(protocol)`](#tts.lib.ethernet.PacketIp6.PacketIp6.FindParent "tts.lib.ethernet.PacketIp6.PacketIp6.FindParent"). Direct access to parent protocols. *protocol* is one of [`OsiProtocol`](#tts.lib.ethernet.PacketEthernet.OsiProtocol "tts.lib.ethernet.PacketEthernet.OsiProtocol").

Example: Signal.eth.src provides the source MAC address of the Ethernet protocol layer.

Type:  [`EthernetProtocolBase`](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase")

GetIpProt()[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.GetIpProt "Link to this definition")  
Returns:  protocol type / next header field

Return type:  int

SetIpProt(*prot*)[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.SetIpProt "Link to this definition")  
Set the next header field

Parameters:  **prot** (*int*) – next header field

ipProt[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.ipProt "Link to this definition")  
protocol type / next header field

Type:  int

GetIpHopLimit()[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.GetIpHopLimit "Link to this definition")  
Returns:  hop limit field

Return type:  int

SetIpHopLimit(*hopLimit*)[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.SetIpHopLimit "Link to this definition")  
Set the hop limit field

Parameters:  **hopLimit** (*int*) – hop limit field

ipHopLimit[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.ipHopLimit "Link to this definition")  
hop limit field

Type:  int

GetIpSrc()[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.GetIpSrc "Link to this definition")  
Returns:  source IP address e.g. 2001:db8::1428:57ab

Return type:  str

SetIpSrc(*addr*)[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.SetIpSrc "Link to this definition")  
Parameters:  **addr** (*str*) – source IP address e.g. 2001:db8::1428:57ab

ipSrc[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.ipSrc "Link to this definition")  
source IP address e.g. 2001:db8::1428:57ab

Type:  str

GetIpDst()[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.GetIpDst "Link to this definition")  
Returns:  target IP address e.g. 2001:db8::1428:57ab

Return type:  str

SetIpDst(*addr*)[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.SetIpDst "Link to this definition")  
Parameters:  **addr** (*str*) – target IP address e.g. 2001:db8::1428:57ab

ipDst[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.ipDst "Link to this definition")  
target IP address e.g. 2001:db8::1428:57ab

Type:  str

GetIpPayload()[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.GetIpPayload "Link to this definition")  
Returns:  IP payload

Return type:  bytes

SetIpPayload(*payload*)[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.SetIpPayload "Link to this definition")  
Parameters:  **payload** (*bytes*) – IP payload

ipPayload[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.ipPayload "Link to this definition")  
IP payload

Type:  bytes

GetIpLen()[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.GetIpLen "Link to this definition")  
Returns:  payload length from IPv6 header

Return type:  int

ipLen[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.ipLen "Link to this definition")  
payload length from IPv6 header

Type:  int

GetIpTrafficClass()[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.GetIpTrafficClass "Link to this definition")  
Returns:  traffic class from IPv6 header

Return type:  int

ipTrafficClass[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.ipTrafficClass "Link to this definition")  
traffic class from IPv6 header

Type:  int

GetIpFlowLabel()[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.GetIpFlowLabel "Link to this definition")  
Returns:  flow label from IPv6 header

Return type:  int

ipFlowLabel[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.ipFlowLabel "Link to this definition")  
flow label from IPv6 header

Type:  int

CalcIpLen()[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.CalcIpLen "Link to this definition")  
Calculate and set the current length of this IP packet

FindParent(*protocol*)[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.FindParent "Link to this definition")  
*Only for pseudo signals in trace analysis!* Returns the requested protocol object if present, otherwise a [`NoProtocol`](#tts.lib.ethernet.PacketEthernet.NoProtocol "tts.lib.ethernet.PacketEthernet.NoProtocol") object.

Parameters:  **protocol** ([*OsiProtocol*](#tts.lib.ethernet.PacketEthernet.OsiProtocol "tts.lib.ethernet.PacketEthernet.OsiProtocol")) – The required protocol name.

Returns:  The required parent protocol object.

Return type:  [EthernetProtocolBase](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase")

GetEthDstMac()[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.GetEthDstMac "Link to this definition")  
Returns:  target MAC address e.g. DE:AD:BE:EF:FF:00

Return type:  str

GetEthPayload()[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.GetEthPayload "Link to this definition")  
Returns:  Ethernet payload

Return type:  bytes

GetEthSrcMac()[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.GetEthSrcMac "Link to this definition")  
Returns:  source MAC address e.g. DE:AD:BE:EF:FF:00

Return type:  str

GetEthType()[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.GetEthType "Link to this definition")  
Returns:  ethernet protocol type

Return type:  int

GetMacSecAn()[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.GetMacSecAn "Link to this definition")  
Returns:  Association Number of MACsec header (see IEEE 802.1AE)

Return type:  int

GetMacSecIcv()[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.GetMacSecIcv "Link to this definition")  
Returns:  Integrity check value of MACsec header (see IEEE 802.1AE)

Return type:  bytes

GetMacSecPn()[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.GetMacSecPn "Link to this definition")  
Returns:  Packet Number of MACsec header (see IEEE 802.1AE)

Return type:  int

GetMacSecSci()[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.GetMacSecSci "Link to this definition")  
Returns:  Secure Channel Identifier of MACsec header (see IEEE 802.1AE)

Return type:  bytes

GetMacSecSl()[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.GetMacSecSl "Link to this definition")  
Returns:  Short Length of MACsec header (see IEEE 802.1AE)

Return type:  int

GetMacSecTci()[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.GetMacSecTci "Link to this definition")  
Returns:  TAG Control Information of MACsec header (see IEEE 802.1AE)

Return type:  int

GetMacSecTciAn()[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.GetMacSecTciAn "Link to this definition")  
Returns:  TCI_AN byte of MACsec header (see IEEE 802.1AE)

Return type:  int

GetMacSecTciC()[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.GetMacSecTciC "Link to this definition")  
Returns:  Changed text bit in TCI of MACsec header (see IEEE 802.1AE)

Return type:  bool

GetMacSecTciE()[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.GetMacSecTciE "Link to this definition")  
Returns:  Encryption bit in TCI of MACsec header (see IEEE 802.1AE)

Return type:  bool

GetMacSecTciEs()[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.GetMacSecTciEs "Link to this definition")  
Returns:  End station bit in TCI of MACsec header (see IEEE 802.1AE)

Return type:  bool

GetMacSecTciSc()[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.GetMacSecTciSc "Link to this definition")  
Returns:  SCI indication bit in TCI of MACsec header (see IEEE 802.1AE)

Return type:  bool

GetMacSecTciScb()[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.GetMacSecTciScb "Link to this definition")  
Returns:  Single copy broadcast capability bit in TCI of MACsec header (see IEEE 802.1AE)

Return type:  bool

GetMacSecTciV()[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.GetMacSecTciV "Link to this definition")  
Returns:  Version bit in TCI of MACsec header (see IEEE 802.1AE)

Return type:  bool

GetTimestamp()[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.GetTimestamp "Link to this definition")  
Returns:  Receive timestamp in sec., None if not available

Return type:  float | None

GetVlanCfi(*ixVlanTags*)[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.GetVlanCfi "Link to this definition")  
Returns:  802.1a canonical format indicator

Return type:  int

GetVlanCfiOuter(*ixVlanTags*)[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.GetVlanCfiOuter "Link to this definition")  
Returns:  802.1ad canonical format indicator

Return type:  int

GetVlanPcp(*ixVlanTags*)[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.GetVlanPcp "Link to this definition")  
Returns:  802.1a priority code point

Return type:  int

GetVlanPcpOuter(*ixVlanTags*)[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.GetVlanPcpOuter "Link to this definition")  
Returns:  802.1ad priority code point

Return type:  int

GetVlanVid(*ixVlanTags*)[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.GetVlanVid "Link to this definition")  
Returns:  802.1a VLAN id

Return type:  int

GetVlanVidOuter(*ixVlanTags*)[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.GetVlanVidOuter "Link to this definition")  
Returns:  802.1ad VLAN id

Return type:  int

SetEthDstMac(*mac*)[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.SetEthDstMac "Link to this definition")  
Parameters:  **mac** (*str*) – target MAC address e.g. DE:AD:BE:EF:FF:00

SetEthPayload(*payload*)[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.SetEthPayload "Link to this definition")  
Parameters:  **payload** (*bytes*) – Ethernet payload

SetEthSrcMac(*mac*)[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.SetEthSrcMac "Link to this definition")  
Parameters:  **mac** (*str*) – source MAC addres e.g. DE:AD:BE:EF:FF:00

SetEthType(*ethType*)[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.SetEthType "Link to this definition")  
Parameters:  **ethType** (*int*) – ethernet protocol type

SetTimestamp(*timestamp*)[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.SetTimestamp "Link to this definition")  
Parameters:  **timestamp** (*float* *|* *None*) – Receive timestamp in sec., None if not available

SetVlanCfi(*cfi*)[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.SetVlanCfi "Link to this definition")  
Parameters:  **cfi** (*int*) – 802.1a canonical format indicator

SetVlanCfiOuter(*cfi*)[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.SetVlanCfiOuter "Link to this definition")  
Parameters:  **cfi** (*int*) – 802.1ad canonical format indicator

SetVlanPcp(*pcp*)[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.SetVlanPcp "Link to this definition")  
Parameters:  **pcp** (*int*) – 802.1a priority code point

SetVlanPcpOuter(*pcp*)[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.SetVlanPcpOuter "Link to this definition")  
Parameters:  **pcp** (*int*) – 802.1ad priority code point

SetVlanVid(*vid*)[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.SetVlanVid "Link to this definition")  
Parameters:  **vid** (*int*) – 802.1a VLAN id

SetVlanVidOuter(*vid*)[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.SetVlanVidOuter "Link to this definition")  
Parameters:  **vid** (*int*) – 802.1ad VLAN id

ethDstMac[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.ethDstMac "Link to this definition")  
target MAC address e.g. DE:AD:BE:EF:FF:00

Type:  str

ethPayload[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.ethPayload "Link to this definition")  
Ethernet payload

Type:  bytes

ethSrcMac[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.ethSrcMac "Link to this definition")  
source MAC address e.g. DE:AD:BE:EF:FF:00

Type:  str

ethType[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.ethType "Link to this definition")  
ethernet protocol type

Type:  int

macSecAn[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.macSecAn "Link to this definition")  
Association Number of MACsec header (see IEEE 802.1AE)

Type:  int

macSecIcv[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.macSecIcv "Link to this definition")  
Integrity check value of MACsec header (see IEEE 802.1AE)

Type:  bytes

macSecPn[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.macSecPn "Link to this definition")  
Packet Number of MACsec header (see IEEE 802.1AE)

Type:  int

macSecSci[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.macSecSci "Link to this definition")  
Secure Channel Identifier of MACsec header (see IEEE 802.1AE)

Type:  bytes

macSecSl[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.macSecSl "Link to this definition")  
Short Length of MACsec header (see IEEE 802.1AE)

Type:  int

macSecTci[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.macSecTci "Link to this definition")  
TAG Control Information of MACsec header (see IEEE 802.1AE)

Type:  int

macSecTciAn[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.macSecTciAn "Link to this definition")  
TCI_AN byte of MACsec header (see IEEE 802.1AE)

Type:  int

macSecTciC[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.macSecTciC "Link to this definition")  
Changed text bit in TCI of MACsec header (see IEEE 802.1AE)

Type:  bool

macSecTciE[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.macSecTciE "Link to this definition")  
Encryption bit in TCI of MACsec header (see IEEE 802.1AE)

Type:  bool

macSecTciEs[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.macSecTciEs "Link to this definition")  
End station bit in TCI of MACsec header (see IEEE 802.1AE)

Type:  bool

macSecTciSc[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.macSecTciSc "Link to this definition")  
SCI indication bit in TCI of MACsec header (see IEEE 802.1AE)

Type:  bool

macSecTciScb[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.macSecTciScb "Link to this definition")  
Single copy broadcast capability bit in TCI of MACsec header (see IEEE 802.1AE)

Type:  bool

macSecTciV[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.macSecTciV "Link to this definition")  
Version bit in TCI of MACsec header (see IEEE 802.1AE)

Type:  bool

parent[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.parent "Link to this definition")  
*Only for pseudo signals in trace analysis!* Returns the parent protocol object if there is one present, otherwise None.

Return type:  [EthernetProtocolBase](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase") | None

timestamp[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.timestamp "Link to this definition")  
Receive timestamp in sec., None if not available

Type:  Optional[float]

vlanCfi[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.vlanCfi "Link to this definition")  
802.1a canonical format indicator

Type:  int

vlanCfiOuter[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.vlanCfiOuter "Link to this definition")  
802.1ad canonical format indicator

Type:  int

vlanPcp[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.vlanPcp "Link to this definition")  
802.1a priority code point

Type:  int

vlanPcpOuter[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.vlanPcpOuter "Link to this definition")  
802.1ad priority code point

Type:  int

vlanVid[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.vlanVid "Link to this definition")  
802.1a VLAN id

Type:  int

vlanVidOuter[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.vlanVidOuter "Link to this definition")  
802.1ad VLAN id

Type:  int

### PacketIcmp[¶](#packeticmp "Link to this heading")

*class* PacketIcmp[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp "Link to this definition")  
In the test case, use `api.Ethernet.PacketIcmp`; in UserPyModules, use `from tts.lib.ethernet.PacketIcmp import PacketIcmp`.

\<protocol\>  
Equivalent to method [`FindParent(protocol)`](#tts.lib.ethernet.PacketIcmp.PacketIcmp.FindParent "tts.lib.ethernet.PacketIcmp.PacketIcmp.FindParent"). Direct access to parent protocols. *protocol* is one of [`OsiProtocol`](#tts.lib.ethernet.PacketEthernet.OsiProtocol "tts.lib.ethernet.PacketEthernet.OsiProtocol").

Example: Signal.eth.src provides the source MAC address of the Ethernet protocol layer.

Type:  [`EthernetProtocolBase`](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase")

GetIcmpType()[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetIcmpType "Link to this definition")  
Returns:  ICMP type

Return type:  int

SetIcmpType(*icmpType*)[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetIcmpType "Link to this definition")  
Parameters:  **icmpType** (*int*) – ICMP type

icmpType[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.icmpType "Link to this definition")  
ICMP type

Type:  int

GetIcmpCode()[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetIcmpCode "Link to this definition")  
Returns:  ICMP code

Return type:  int

SetIcmpCode(*code*)[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetIcmpCode "Link to this definition")  
Parameters:  **code** (*int*) – ICMP code

icmpCode[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.icmpCode "Link to this definition")  
ICMP code

Type:  int

GetIcmpChecksum()[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetIcmpChecksum "Link to this definition")  
Returns:  checksum

Return type:  int

SetIcmpChecksum(*checksum*)[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetIcmpChecksum "Link to this definition")  
Parameters:  **checksum** (*int*) – checksum

icmpChecksum[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.icmpChecksum "Link to this definition")  
checksum

Type:  int

GetIcmpPayload()[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetIcmpPayload "Link to this definition")  
Returns:  ICMP payload

Return type:  bytes

CalcIpLen()[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.CalcIpLen "Link to this definition")  
Calculate and set the current length of this IP packet

FindParent(*protocol*)[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.FindParent "Link to this definition")  
*Only for pseudo signals in trace analysis!* Returns the requested protocol object if present, otherwise a [`NoProtocol`](#tts.lib.ethernet.PacketEthernet.NoProtocol "tts.lib.ethernet.PacketEthernet.NoProtocol") object.

Parameters:  **protocol** ([*OsiProtocol*](#tts.lib.ethernet.PacketEthernet.OsiProtocol "tts.lib.ethernet.PacketEthernet.OsiProtocol")) – The required protocol name.

Returns:  The required parent protocol object.

Return type:  [EthernetProtocolBase](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase")

GetEthDstMac()[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetEthDstMac "Link to this definition")  
Returns:  target MAC address e.g. DE:AD:BE:EF:FF:00

Return type:  str

GetEthPayload()[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetEthPayload "Link to this definition")  
Returns:  Ethernet payload

Return type:  bytes

GetEthSrcMac()[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetEthSrcMac "Link to this definition")  
Returns:  source MAC address e.g. DE:AD:BE:EF:FF:00

Return type:  str

GetEthType()[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetEthType "Link to this definition")  
Returns:  ethernet protocol type

Return type:  int

GetIpAhIcv()[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetIpAhIcv "Link to this definition")  
Returns:  Integrity check value of IP authentication header (see RFC 4302)

Return type:  bytes

GetIpAhLen()[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetIpAhLen "Link to this definition")  
Returns:  Length value of IP authentication header (see RFC 4302) =\> len(ICV)/4+1

Return type:  int

GetIpAhNxt()[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetIpAhNxt "Link to this definition")  
Returns:  Next header value of IP authentication header (see RFC 4302)

Return type:  int

GetIpAhRsvd()[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetIpAhRsvd "Link to this definition")  
Returns:  Reserved value of IP authentication header (see RFC 4302)

Return type:  int

GetIpAhSeq()[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetIpAhSeq "Link to this definition")  
Returns:  Sequence number field of IP authentication header (see RFC 4302)

Return type:  int

GetIpAhSpi()[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetIpAhSpi "Link to this definition")  
Returns:  Security parameters index of IP authentication header (see RFC 4302)

Return type:  int

GetIpChecksum()[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetIpChecksum "Link to this definition")  
Returns:  checksum

Return type:  int

GetIpDst()[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetIpDst "Link to this definition")  
Returns:  target IP address e.g. 127.0.0.1

Return type:  str

GetIpIdent()[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetIpIdent "Link to this definition")  
Returns:  identifier

Return type:  int

GetIpLen()[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetIpLen "Link to this definition")  
Returns:  packet length

Return type:  int

GetIpOffset()[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetIpOffset "Link to this definition")  
Returns:  flags and offset combined

Return type:  int

GetIpPayload()[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetIpPayload "Link to this definition")  
Returns:  IP payload

Return type:  bytes

GetIpProt()[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetIpProt "Link to this definition")  
Returns:  protocol type / next header field

Return type:  int

GetIpSrc()[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetIpSrc "Link to this definition")  
Returns:  source IP address e.g. 127.0.0.1

Return type:  str

GetIpTos()[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetIpTos "Link to this definition")  
Returns:  type of service

Return type:  int

GetIpTtl()[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetIpTtl "Link to this definition")  
Returns:  TTL

Return type:  int

GetIpVersionAndHeaderLength()[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetIpVersionAndHeaderLength "Link to this definition")  
Returns:  protocol version and header length

Return type:  int

GetMacSecAn()[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetMacSecAn "Link to this definition")  
Returns:  Association Number of MACsec header (see IEEE 802.1AE)

Return type:  int

GetMacSecIcv()[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetMacSecIcv "Link to this definition")  
Returns:  Integrity check value of MACsec header (see IEEE 802.1AE)

Return type:  bytes

GetMacSecPn()[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetMacSecPn "Link to this definition")  
Returns:  Packet Number of MACsec header (see IEEE 802.1AE)

Return type:  int

GetMacSecSci()[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetMacSecSci "Link to this definition")  
Returns:  Secure Channel Identifier of MACsec header (see IEEE 802.1AE)

Return type:  bytes

GetMacSecSl()[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetMacSecSl "Link to this definition")  
Returns:  Short Length of MACsec header (see IEEE 802.1AE)

Return type:  int

GetMacSecTci()[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetMacSecTci "Link to this definition")  
Returns:  TAG Control Information of MACsec header (see IEEE 802.1AE)

Return type:  int

GetMacSecTciAn()[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetMacSecTciAn "Link to this definition")  
Returns:  TCI_AN byte of MACsec header (see IEEE 802.1AE)

Return type:  int

GetMacSecTciC()[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetMacSecTciC "Link to this definition")  
Returns:  Changed text bit in TCI of MACsec header (see IEEE 802.1AE)

Return type:  bool

GetMacSecTciE()[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetMacSecTciE "Link to this definition")  
Returns:  Encryption bit in TCI of MACsec header (see IEEE 802.1AE)

Return type:  bool

GetMacSecTciEs()[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetMacSecTciEs "Link to this definition")  
Returns:  End station bit in TCI of MACsec header (see IEEE 802.1AE)

Return type:  bool

GetMacSecTciSc()[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetMacSecTciSc "Link to this definition")  
Returns:  SCI indication bit in TCI of MACsec header (see IEEE 802.1AE)

Return type:  bool

GetMacSecTciScb()[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetMacSecTciScb "Link to this definition")  
Returns:  Single copy broadcast capability bit in TCI of MACsec header (see IEEE 802.1AE)

Return type:  bool

GetMacSecTciV()[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetMacSecTciV "Link to this definition")  
Returns:  Version bit in TCI of MACsec header (see IEEE 802.1AE)

Return type:  bool

GetTimestamp()[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetTimestamp "Link to this definition")  
Returns:  Receive timestamp in sec., None if not available

Return type:  float | None

GetVlanCfi(*ixVlanTags*)[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetVlanCfi "Link to this definition")  
Returns:  802.1a canonical format indicator

Return type:  int

GetVlanCfiOuter(*ixVlanTags*)[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetVlanCfiOuter "Link to this definition")  
Returns:  802.1ad canonical format indicator

Return type:  int

GetVlanPcp(*ixVlanTags*)[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetVlanPcp "Link to this definition")  
Returns:  802.1a priority code point

Return type:  int

GetVlanPcpOuter(*ixVlanTags*)[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetVlanPcpOuter "Link to this definition")  
Returns:  802.1ad priority code point

Return type:  int

GetVlanVid(*ixVlanTags*)[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetVlanVid "Link to this definition")  
Returns:  802.1a VLAN id

Return type:  int

GetVlanVidOuter(*ixVlanTags*)[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetVlanVidOuter "Link to this definition")  
Returns:  802.1ad VLAN id

Return type:  int

PK_CLASS[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.PK_CLASS "Link to this definition")  
alias of `IP`

SetEthDstMac(*mac*)[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetEthDstMac "Link to this definition")  
Parameters:  **mac** (*str*) – target MAC address e.g. DE:AD:BE:EF:FF:00

SetEthPayload(*payload*)[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetEthPayload "Link to this definition")  
Parameters:  **payload** (*bytes*) – Ethernet payload

SetEthSrcMac(*mac*)[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetEthSrcMac "Link to this definition")  
Parameters:  **mac** (*str*) – source MAC addres e.g. DE:AD:BE:EF:FF:00

SetEthType(*ethType*)[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetEthType "Link to this definition")  
Parameters:  **ethType** (*int*) – ethernet protocol type

SetIcmpPayload(*payload*)[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetIcmpPayload "Link to this definition")  
Parameters:  **payload** (*bytes*) – ICMP payload

SetIpChecksum(*checksum*)[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetIpChecksum "Link to this definition")  
Parameters:  **checksum** (*int*) – checksum

SetIpDst(*addr*)[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetIpDst "Link to this definition")  
Parameters:  **addr** (*str*) – target IP address e.g. 127.0.0.1

SetIpIdent(*ident*)[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetIpIdent "Link to this definition")  
Parameters:  **ident** (*int*) – identifier

SetIpLen(*length*)[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetIpLen "Link to this definition")  
Parameters:  **length** (*int*) – packet length

SetIpOffset(*offset*)[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetIpOffset "Link to this definition")  
Parameters:  **offset** (*int*) – flags and offset combined

SetIpPayload(*payload*)[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetIpPayload "Link to this definition")  
Parameters:  **payload** (*bytes*) – IP payload

SetIpProt(*prot*)[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetIpProt "Link to this definition")  
Parameters:  **prot** (*int*) – protocol type

SetIpSrc(*addr*)[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetIpSrc "Link to this definition")  
Parameters:  **addr** (*str*) – source IP address e.g. 127.0.0.1

SetIpTos(*tos*)[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetIpTos "Link to this definition")  
Parameters:  **tos** (*int*) – type of service

SetIpTtl(*ttl*)[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetIpTtl "Link to this definition")  
Parameters:  **ttl** (*int*) – TTL

SetIpVersionAndHeaderLength(*versionHeader*)[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetIpVersionAndHeaderLength "Link to this definition")  
Parameters:  **versionHeader** (*int*) – protocol version and header length

SetTimestamp(*timestamp*)[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetTimestamp "Link to this definition")  
Parameters:  **timestamp** (*float* *|* *None*) – Receive timestamp in sec., None if not available

SetVlanCfi(*cfi*)[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetVlanCfi "Link to this definition")  
Parameters:  **cfi** (*int*) – 802.1a canonical format indicator

SetVlanCfiOuter(*cfi*)[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetVlanCfiOuter "Link to this definition")  
Parameters:  **cfi** (*int*) – 802.1ad canonical format indicator

SetVlanPcp(*pcp*)[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetVlanPcp "Link to this definition")  
Parameters:  **pcp** (*int*) – 802.1a priority code point

SetVlanPcpOuter(*pcp*)[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetVlanPcpOuter "Link to this definition")  
Parameters:  **pcp** (*int*) – 802.1ad priority code point

SetVlanVid(*vid*)[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetVlanVid "Link to this definition")  
Parameters:  **vid** (*int*) – 802.1a VLAN id

SetVlanVidOuter(*vid*)[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetVlanVidOuter "Link to this definition")  
Parameters:  **vid** (*int*) – 802.1ad VLAN id

ethDstMac[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.ethDstMac "Link to this definition")  
target MAC address e.g. DE:AD:BE:EF:FF:00

Type:  str

ethPayload[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.ethPayload "Link to this definition")  
Ethernet payload

Type:  bytes

ethSrcMac[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.ethSrcMac "Link to this definition")  
source MAC address e.g. DE:AD:BE:EF:FF:00

Type:  str

ethType[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.ethType "Link to this definition")  
ethernet protocol type

Type:  int

ipAhIcv[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.ipAhIcv "Link to this definition")  
Integrity check value of IP authentication header (see RFC 4302)

Type:  bytes

ipAhLen[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.ipAhLen "Link to this definition")  
Length value of IP authentication header (see RFC 4302) =\> len(ICV)/4+1

Type:  int

ipAhNxt[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.ipAhNxt "Link to this definition")  
Next header value of IP authentication header (see RFC 4302)

Type:  int

ipAhRsvd[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.ipAhRsvd "Link to this definition")  
Reserved value of IP authentication header (see RFC 4302)

Type:  int

ipAhSeq[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.ipAhSeq "Link to this definition")  
Sequence number field of IP authentication header (see RFC 4302)

Type:  int

ipAhSpi[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.ipAhSpi "Link to this definition")  
Security parameters index of IP authentication header (see RFC 4302)

Type:  int

ipChecksum[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.ipChecksum "Link to this definition")  
checksum

Type:  int

ipDst[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.ipDst "Link to this definition")  
target IP address e.g. 127.0.0.1

Type:  str

ipIdent[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.ipIdent "Link to this definition")  
identifier

Type:  int

ipLen[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.ipLen "Link to this definition")  
packet length

Type:  int

ipOffset[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.ipOffset "Link to this definition")  
flags and offset combined

Type:  int

ipPayload[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.ipPayload "Link to this definition")  
IP payload

Type:  bytes

ipProt[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.ipProt "Link to this definition")  
protocol type / next header field

Type:  int

ipSrc[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.ipSrc "Link to this definition")  
source IP address e.g. 127.0.0.1

Type:  str

ipTos[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.ipTos "Link to this definition")  
type of service

Type:  int

ipTtl[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.ipTtl "Link to this definition")  
TTL

Type:  int

ipVersionHeader[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.ipVersionHeader "Link to this definition")  
protocol version and header length

Type:  int

macSecAn[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.macSecAn "Link to this definition")  
Association Number of MACsec header (see IEEE 802.1AE)

Type:  int

macSecIcv[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.macSecIcv "Link to this definition")  
Integrity check value of MACsec header (see IEEE 802.1AE)

Type:  bytes

macSecPn[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.macSecPn "Link to this definition")  
Packet Number of MACsec header (see IEEE 802.1AE)

Type:  int

macSecSci[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.macSecSci "Link to this definition")  
Secure Channel Identifier of MACsec header (see IEEE 802.1AE)

Type:  bytes

macSecSl[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.macSecSl "Link to this definition")  
Short Length of MACsec header (see IEEE 802.1AE)

Type:  int

macSecTci[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.macSecTci "Link to this definition")  
TAG Control Information of MACsec header (see IEEE 802.1AE)

Type:  int

macSecTciAn[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.macSecTciAn "Link to this definition")  
TCI_AN byte of MACsec header (see IEEE 802.1AE)

Type:  int

macSecTciC[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.macSecTciC "Link to this definition")  
Changed text bit in TCI of MACsec header (see IEEE 802.1AE)

Type:  bool

macSecTciE[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.macSecTciE "Link to this definition")  
Encryption bit in TCI of MACsec header (see IEEE 802.1AE)

Type:  bool

macSecTciEs[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.macSecTciEs "Link to this definition")  
End station bit in TCI of MACsec header (see IEEE 802.1AE)

Type:  bool

macSecTciSc[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.macSecTciSc "Link to this definition")  
SCI indication bit in TCI of MACsec header (see IEEE 802.1AE)

Type:  bool

macSecTciScb[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.macSecTciScb "Link to this definition")  
Single copy broadcast capability bit in TCI of MACsec header (see IEEE 802.1AE)

Type:  bool

macSecTciV[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.macSecTciV "Link to this definition")  
Version bit in TCI of MACsec header (see IEEE 802.1AE)

Type:  bool

parent[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.parent "Link to this definition")  
*Only for pseudo signals in trace analysis!* Returns the parent protocol object if there is one present, otherwise None.

Return type:  [EthernetProtocolBase](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase") | None

timestamp[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.timestamp "Link to this definition")  
Receive timestamp in sec., None if not available

Type:  Optional[float]

vlanCfi[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.vlanCfi "Link to this definition")  
802.1a canonical format indicator

Type:  int

vlanCfiOuter[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.vlanCfiOuter "Link to this definition")  
802.1ad canonical format indicator

Type:  int

vlanPcp[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.vlanPcp "Link to this definition")  
802.1a priority code point

Type:  int

vlanPcpOuter[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.vlanPcpOuter "Link to this definition")  
802.1ad priority code point

Type:  int

vlanVid[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.vlanVid "Link to this definition")  
802.1a VLAN id

Type:  int

vlanVidOuter[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.vlanVidOuter "Link to this definition")  
802.1ad VLAN id

Type:  int

icmpPayload[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.icmpPayload "Link to this definition")  
ICMP payload

Type:  bytes

### PacketMka[¶](#packetmka "Link to this heading")

*class* PacketMka[¶](#tts.lib.ethernet.PacketMka.PacketMka "Link to this definition")  
In the test case, use `api.Ethernet.PacketMka`; in UserPyModules, use `from tts.lib.ethernet.PacketMka import PacketMka`.

\<protocol\>  
Equivalent to method [`FindParent(protocol)`](#tts.lib.ethernet.PacketMka.PacketMka.FindParent "tts.lib.ethernet.PacketMka.PacketMka.FindParent"). Direct access to parent protocols. *protocol* is one of [`OsiProtocol`](#tts.lib.ethernet.PacketEthernet.OsiProtocol "tts.lib.ethernet.PacketEthernet.OsiProtocol").

Example: Signal.eth.src provides the source MAC address of the Ethernet protocol layer.

Type:  [`EthernetProtocolBase`](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase")

UseCak(*cak*)[¶](#tts.lib.ethernet.PacketMka.PacketMka.UseCak "Link to this definition")  
Use a specific Connectivity Association Key. Needed for example to unwrap the Security Association Key or to validate the MKPDU’s Integrity Check Value.

GetEthDstMac()[¶](#tts.lib.ethernet.PacketMka.PacketMka.GetEthDstMac "Link to this definition")  
Returns:  destination MAC address e.g. DE:AD:BE:EF:42:05

Return type:  str

SetEthDstMac(*mac*)[¶](#tts.lib.ethernet.PacketMka.PacketMka.SetEthDstMac "Link to this definition")  
Parameters:  **mac** (*str*) – target MAC address e.g. DE:AD:BE:EF:FF:00

ethDstMac[¶](#tts.lib.ethernet.PacketMka.PacketMka.ethDstMac "Link to this definition")  
destination MAC address e.g. DE:AD:BE:EF:42:05

Type:  str

GetEthSrcMac()[¶](#tts.lib.ethernet.PacketMka.PacketMka.GetEthSrcMac "Link to this definition")  
Returns:  source MAC address e.g. DE:AD:BE:EF:42:05

Return type:  str

SetEthSrcMac(*mac*)[¶](#tts.lib.ethernet.PacketMka.PacketMka.SetEthSrcMac "Link to this definition")  
Parameters:  **mac** (*str*) – source MAC addres e.g. DE:AD:BE:EF:FF:00

ethSrcMac[¶](#tts.lib.ethernet.PacketMka.PacketMka.ethSrcMac "Link to this definition")  
source MAC address e.g. DE:AD:BE:EF:42:05

Type:  str

GetEthType()[¶](#tts.lib.ethernet.PacketMka.PacketMka.GetEthType "Link to this definition")  
Returns:  ethernet protocol type

Return type:  int

SetEthType(*ethType*)[¶](#tts.lib.ethernet.PacketMka.PacketMka.SetEthType "Link to this definition")  
Parameters:  **ethType** (*int*) – ethernet protocol type

GetEthPayload()[¶](#tts.lib.ethernet.PacketMka.PacketMka.GetEthPayload "Link to this definition")  
Returns:  Ethernet payload

Return type:  bytes

SetEthPayload(*payload*)[¶](#tts.lib.ethernet.PacketMka.PacketMka.SetEthPayload "Link to this definition")  
Parameters:  **payload** (*bytes*) – Ethernet payload

GetMkaIcv()[¶](#tts.lib.ethernet.PacketMka.PacketMka.GetMkaIcv "Link to this definition")  
Returns:  Integrity Check Value of this MKPDU. See IEEE 802.1X-2020, section 9.4.1.

Return type:  [*ByteStream*](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream")

mkaIcv[¶](#tts.lib.ethernet.PacketMka.PacketMka.mkaIcv "Link to this definition")  
Integrity Check Value of this MKPDU. See IEEE 802.1X-2020, section 9.4.1.

Type:  [ByteStream](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream")

IsMkaIcvValid()[¶](#tts.lib.ethernet.PacketMka.PacketMka.IsMkaIcvValid "Link to this definition")  
Returns:  True if the Integrity Check Value of this PacketMka is valid, False otherwise.

Return type:  bool

GetKeyServerPriority()[¶](#tts.lib.ethernet.PacketMka.PacketMka.GetKeyServerPriority "Link to this definition")  
Returns:  Key Server Priority (0..255) from Basic Parameter Set. See IEEE 802.1X-2020, section 9.5 and table 11-7.

Return type:  int

keyServerPriority[¶](#tts.lib.ethernet.PacketMka.PacketMka.keyServerPriority "Link to this definition")  
Key Server Priority (0..255) from Basic Parameter Set. See IEEE 802.1X-2020, section 9.5 and table 11-7.

Type:  int

GetKeyServerFlag()[¶](#tts.lib.ethernet.PacketMka.PacketMka.GetKeyServerFlag "Link to this definition")  
Returns:  Key Server Flag from Basic Parameter Set. See IEEE 802.1X-2020, section 9.5.1 and table 11-7.

Return type:  bool

keyServerFlag[¶](#tts.lib.ethernet.PacketMka.PacketMka.keyServerFlag "Link to this definition")  
Key Server Flag from Basic Parameter Set. See IEEE 802.1X-2020, section 9.5.1 and table 11-7.

Type:  bool

GetMacSecDesired()[¶](#tts.lib.ethernet.PacketMka.PacketMka.GetMacSecDesired "Link to this definition")  
Returns:  MACsec Desired from Basic Parameter Set. See IEEE 802.1X-2020, section 9.6.1 and table 11-7.

Return type:  bool

macSecDesired[¶](#tts.lib.ethernet.PacketMka.PacketMka.macSecDesired "Link to this definition")  
MACsec Desired from Basic Parameter Set. See IEEE 802.1X-2020, section 9.6.1 and table 11-7.

Type:  bool

GetMacSecCapability()[¶](#tts.lib.ethernet.PacketMka.PacketMka.GetMacSecCapability "Link to this definition")  
Returns:  MACsec Capability from Basic Parameter Set. See IEEE 802.1X-2020, section 9.6.1 and table 11-7.

Return type:  *MacSecCapability*

macSecCapability[¶](#tts.lib.ethernet.PacketMka.PacketMka.macSecCapability "Link to this definition")  
MACsec Capability from Basic Parameter Set. See IEEE 802.1X-2020, section 9.6.1 and table 11-7.

Type:  MacSecCapability

GetMacSecSci()[¶](#tts.lib.ethernet.PacketMka.PacketMka.GetMacSecSci "Link to this definition")  
Returns:  Secure Channel Identifier from Basic Parameter Set. See IEEE 802.1X-2020, table 11-7 and IEEE 802.1AE.

Return type:  [*ByteStream*](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream")

macSecSci[¶](#tts.lib.ethernet.PacketMka.PacketMka.macSecSci "Link to this definition")  
Secure Channel Identifier from Basic Parameter Set. See IEEE 802.1X-2020, table 11-7 and IEEE 802.1AE.

Type:  [ByteStream](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream")

GetMemberIdentifier()[¶](#tts.lib.ethernet.PacketMka.PacketMka.GetMemberIdentifier "Link to this definition")  
Returns:  Member Identifier from Basic Parameter Set. See IEEE 802.1X-2020, table 11-7.

Return type:  [*ByteStream*](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream")

memberIdentifier[¶](#tts.lib.ethernet.PacketMka.PacketMka.memberIdentifier "Link to this definition")  
Member Identifier from Basic Parameter Set. See IEEE 802.1X-2020, table 11-7.

Type:  [ByteStream](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream")

GetMessageNumber()[¶](#tts.lib.ethernet.PacketMka.PacketMka.GetMessageNumber "Link to this definition")  
Returns:  Message Number from Basic Parameter Set. See IEEE 802.1X-2020, table 11-7.

Return type:  int

messageNumber[¶](#tts.lib.ethernet.PacketMka.PacketMka.messageNumber "Link to this definition")  
Message Number from Basic Parameter Set. See IEEE 802.1X-2020, table 11-7.

Type:  int

GetCakName()[¶](#tts.lib.ethernet.PacketMka.PacketMka.GetCakName "Link to this definition")  
Returns:  Connectivity Association Key Name from Basic Parameter Set. See IEEE 802.1X-2020, section 9.3.1 and table 11-7.

Return type:  [*ByteStream*](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream")

cakName[¶](#tts.lib.ethernet.PacketMka.PacketMka.cakName "Link to this definition")  
Connectivity Association Key Name from Basic Parameter Set. See IEEE 802.1X-2020, section 9.3.1 and table 11-7.

Type:  [ByteStream](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream")

GetLivePeerListMemberIdentifiers()[¶](#tts.lib.ethernet.PacketMka.PacketMka.GetLivePeerListMemberIdentifiers "Link to this definition")  
Returns:  List of Member Identifiers from Live Peer List Parameter Set. See IEEE 802.1X-2020, section 9.4.3 and table 11-7.

Return type:  list[[*ByteStream*](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream")] | None

livePeerListMemberIdentifiers[¶](#tts.lib.ethernet.PacketMka.PacketMka.livePeerListMemberIdentifiers "Link to this definition")  
List of Member Identifiers from Live Peer List Parameter Set. See IEEE 802.1X-2020, section 9.4.3 and table 11-7.

Type:  Optional[list[[ByteStream](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream")]]

GetLivePeerListMessageNumbers()[¶](#tts.lib.ethernet.PacketMka.PacketMka.GetLivePeerListMessageNumbers "Link to this definition")  
Returns:  List of Message Numbers (one for each Member Identifier) from Live Peer List Parameter Set. See IEEE 802.1X-2020, section 9.4.3 and table 11-7.

Return type:  list[int] | None

livePeerListMessageNumbers[¶](#tts.lib.ethernet.PacketMka.PacketMka.livePeerListMessageNumbers "Link to this definition")  
List of Message Numbers (one for each Member Identifier) from Live Peer List Parameter Set. See IEEE 802.1X-2020, section 9.4.3 and table 11-7.

Type:  Optional[list[int]]

GetLivePeerListKeyServerSsci()[¶](#tts.lib.ethernet.PacketMka.PacketMka.GetLivePeerListKeyServerSsci "Link to this definition")  
Returns:  Elected Key Server’s Short Secure Channel Identifier from Live Peer List Parameter Set. See IEEE 802.1X-2020, section 9.10 and table 11-7.

Return type:  int | None

livePeerListKeyServerSsci[¶](#tts.lib.ethernet.PacketMka.PacketMka.livePeerListKeyServerSsci "Link to this definition")  
Elected Key Server’s Short Secure Channel Identifier from Live Peer List Parameter Set. See IEEE 802.1X-2020, section 9.10 and table 11-7.

Type:  Optional[int]

RemoveLivePeerList()[¶](#tts.lib.ethernet.PacketMka.PacketMka.RemoveLivePeerList "Link to this definition")  
If the MKPDU has a Live Peer List Parameter Set, remove it.

GetPotentialPeerListMemberIdentifiers()[¶](#tts.lib.ethernet.PacketMka.PacketMka.GetPotentialPeerListMemberIdentifiers "Link to this definition")  
Returns:  List of Member Identifiers from Potential Peer List Parameter Set. See IEEE 802.1X-2020, section 9.4.3 and table 11-7.

Return type:  list[[*ByteStream*](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream")] | None

potentialPeerListMemberIdentifiers[¶](#tts.lib.ethernet.PacketMka.PacketMka.potentialPeerListMemberIdentifiers "Link to this definition")  
List of Member Identifiers from Potential Peer List Parameter Set. See IEEE 802.1X-2020, section 9.4.3 and table 11-7.

Type:  Optional[list[[ByteStream](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream")]]

GetPotentialPeerListMessageNumbers()[¶](#tts.lib.ethernet.PacketMka.PacketMka.GetPotentialPeerListMessageNumbers "Link to this definition")  
Returns:  List of Message Numbers (one for each Member Identifier) from Potential Peer List Parameter Set. See IEEE 802.1X-2020, section 9.4.3 and table 11-7.

Return type:  list[int] | None

potentialPeerListMessageNumbers[¶](#tts.lib.ethernet.PacketMka.PacketMka.potentialPeerListMessageNumbers "Link to this definition")  
List of Message Numbers (one for each Member Identifier) from Potential Peer List Parameter Set. See IEEE 802.1X-2020, section 9.4.3 and table 11-7.

Type:  Optional[list[int]]

RemovePotentialPeerList()[¶](#tts.lib.ethernet.PacketMka.PacketMka.RemovePotentialPeerList "Link to this definition")  
If the MKPDU has a Potential Peer List Parameter Set, remove it.

GetSakUseLatestAn()[¶](#tts.lib.ethernet.PacketMka.PacketMka.GetSakUseLatestAn "Link to this definition")  
Returns:  Latest Key Association Number from MACsec SAK Use Parameter Set. See IEEE 802.1X-2020, section 9.10 and table 11-7.

Return type:  int | None

sakUseLatestAn[¶](#tts.lib.ethernet.PacketMka.PacketMka.sakUseLatestAn "Link to this definition")  
Latest Key Association Number from MACsec SAK Use Parameter Set. See IEEE 802.1X-2020, section 9.10 and table 11-7.

Type:  Optional[int]

GetSakUseLatestTx()[¶](#tts.lib.ethernet.PacketMka.PacketMka.GetSakUseLatestTx "Link to this definition")  
Returns:  Latest Key Tx Flag from MACsec SAK Use Parameter Set. See IEEE 802.1X-2020, section 9.10 and table 11-7.

Return type:  bool | None

sakUseLatestTx[¶](#tts.lib.ethernet.PacketMka.PacketMka.sakUseLatestTx "Link to this definition")  
Latest Key Tx Flag from MACsec SAK Use Parameter Set. See IEEE 802.1X-2020, section 9.10 and table 11-7.

Type:  Optional[bool]

GetSakUseLatestRx()[¶](#tts.lib.ethernet.PacketMka.PacketMka.GetSakUseLatestRx "Link to this definition")  
Returns:  Latest Key Rx Flag from MACsec SAK Use Parameter Set. See IEEE 802.1X-2020, section 9.10 and table 11-7.

Return type:  bool | None

sakUseLatestRx[¶](#tts.lib.ethernet.PacketMka.PacketMka.sakUseLatestRx "Link to this definition")  
Latest Key Rx Flag from MACsec SAK Use Parameter Set. See IEEE 802.1X-2020, section 9.10 and table 11-7.

Type:  Optional[bool]

GetSakUsePlainTx()[¶](#tts.lib.ethernet.PacketMka.PacketMka.GetSakUsePlainTx "Link to this definition")  
Returns:  Plain Tx Flag from MACsec SAK Use Parameter Set. See IEEE 802.1X-2020, table 11-7 and figure 11-10.

Return type:  bool | None

sakUsePlainTx[¶](#tts.lib.ethernet.PacketMka.PacketMka.sakUsePlainTx "Link to this definition")  
Plain Tx Flag from MACsec SAK Use Parameter Set. See IEEE 802.1X-2020, table 11-7 and figure 11-10.

Type:  Optional[bool]

GetSakUsePlainRx()[¶](#tts.lib.ethernet.PacketMka.PacketMka.GetSakUsePlainRx "Link to this definition")  
Returns:  Plain Rx Flag from MACsec SAK Use Parameter Set. See IEEE 802.1X-2020, table 11-7 and figure 11-10.

Return type:  bool | None

sakUsePlainRx[¶](#tts.lib.ethernet.PacketMka.PacketMka.sakUsePlainRx "Link to this definition")  
Plain Rx Flag from MACsec SAK Use Parameter Set. See IEEE 802.1X-2020, table 11-7 and figure 11-10.

Type:  Optional[bool]

GetSakUseDelayProtect()[¶](#tts.lib.ethernet.PacketMka.PacketMka.GetSakUseDelayProtect "Link to this definition")  
Returns:  Delay Protect Flag from MACsec SAK Use Parameter Set. See IEEE 802.1X-2020, section 9.10.1 and table 11-7.

Return type:  bool | None

sakUseDelayProtect[¶](#tts.lib.ethernet.PacketMka.PacketMka.sakUseDelayProtect "Link to this definition")  
Delay Protect Flag from MACsec SAK Use Parameter Set. See IEEE 802.1X-2020, section 9.10.1 and table 11-7.

Type:  Optional[bool]

GetSakUseLatestKeyServerMemberIdentifier()[¶](#tts.lib.ethernet.PacketMka.PacketMka.GetSakUseLatestKeyServerMemberIdentifier "Link to this definition")  
Returns:  Latest Key Server Member Identifier from MACsec SAK Use Parameter Set. See IEEE 802.1X-2020, section 9.10.1 and table 11-7.

Return type:  [*ByteStream*](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream") | None

sakUseLatestKeyServerMemberIdentifier[¶](#tts.lib.ethernet.PacketMka.PacketMka.sakUseLatestKeyServerMemberIdentifier "Link to this definition")  
Latest Key Server Member Identifier from MACsec SAK Use Parameter Set. See IEEE 802.1X-2020, section 9.10.1 and table 11-7.

Type:  Optional[[ByteStream](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream")]

GetSakUseLatestKeyNumber()[¶](#tts.lib.ethernet.PacketMka.PacketMka.GetSakUseLatestKeyNumber "Link to this definition")  
Returns:  Latest Key Number from MACsec SAK Use Parameter Set. See IEEE 802.1X-2020, section 9.10.1 and table 11-7.

Return type:  int | None

sakUseLatestKeyNumber[¶](#tts.lib.ethernet.PacketMka.PacketMka.sakUseLatestKeyNumber "Link to this definition")  
Latest Key Number from MACsec SAK Use Parameter Set. See IEEE 802.1X-2020, section 9.10.1 and table 11-7.

Type:  Optional[int]

GetSakUseLatestLpn()[¶](#tts.lib.ethernet.PacketMka.PacketMka.GetSakUseLatestLpn "Link to this definition")  
Returns:  Latest Key Lowest Acceptable Packet Number from MACsec SAK Use Parameter Set. See IEEE 802.1X-2020, section 9.10.1 and table 11-7.

Return type:  int | None

sakUseLatestLpn[¶](#tts.lib.ethernet.PacketMka.PacketMka.sakUseLatestLpn "Link to this definition")  
Latest Key Lowest Acceptable Packet Number from MACsec SAK Use Parameter Set. See IEEE 802.1X-2020, section 9.10.1 and table 11-7.

Type:  Optional[int]

RemoveSakUse()[¶](#tts.lib.ethernet.PacketMka.PacketMka.RemoveSakUse "Link to this definition")  
If the MKPDU has a MACsec SAK Use Parameter Set, remove it.

GetDistributedSakWrappedKey()[¶](#tts.lib.ethernet.PacketMka.PacketMka.GetDistributedSakWrappedKey "Link to this definition")  
Returns:  AES Key Wrap of Security Association Key from Distributed SAK Parameter Set. See IEEE 802.1X-2020, section 9.8 and table 11-7.

Return type:  [*ByteStream*](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream") | None

distributedSakWrappedKey[¶](#tts.lib.ethernet.PacketMka.PacketMka.distributedSakWrappedKey "Link to this definition")  
AES Key Wrap of Security Association Key from Distributed SAK Parameter Set. See IEEE 802.1X-2020, section 9.8 and table 11-7.

Type:  Optional[[ByteStream](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream")]

GetDistributedSakUnwrappedKey()[¶](#tts.lib.ethernet.PacketMka.PacketMka.GetDistributedSakUnwrappedKey "Link to this definition")  
Returns:  Security Association Key, unwrapped using the Connectivity Association Key which was set by PacketMka.UseCak().

Return type:  [*ByteStream*](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream") | None

distributedSakUnwrappedKey[¶](#tts.lib.ethernet.PacketMka.PacketMka.distributedSakUnwrappedKey "Link to this definition")  
Security Association Key, unwrapped using the Connectivity Association Key which was set by PacketMka.UseCak().

Type:  Optional[[ByteStream](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream")]

GetDistributedSakAn()[¶](#tts.lib.ethernet.PacketMka.PacketMka.GetDistributedSakAn "Link to this definition")  
Returns:  Association Number from Distributed SAK Parameter Set. See IEEE 802.1X-2020, section 9.9 and table 11-7.

Return type:  int | None

distributedSakAn[¶](#tts.lib.ethernet.PacketMka.PacketMka.distributedSakAn "Link to this definition")  
Association Number from Distributed SAK Parameter Set. See IEEE 802.1X-2020, section 9.9 and table 11-7.

Type:  Optional[int]

GetDistributedSakConfidentialityOffset()[¶](#tts.lib.ethernet.PacketMka.PacketMka.GetDistributedSakConfidentialityOffset "Link to this definition")  
Returns:  Confidentiality Offset from Distributed SAK Parameter Set. 0 = no confidentiality, 1 = no offset, 2 = offset 30 bytes, 3 = offset 50 bytes. See IEEE 802.1X-2020, section 9.6.1, table 11-6 and table 11-7.

Return type:  int | None

distributedSakConfidentialityOffset[¶](#tts.lib.ethernet.PacketMka.PacketMka.distributedSakConfidentialityOffset "Link to this definition")  
Confidentiality Offset from Distributed SAK Parameter Set. 0 = no confidentiality, 1 = no offset, 2 = offset 30 bytes, 3 = offset 50 bytes. See IEEE 802.1X-2020, section 9.6.1, table 11-6 and table 11-7.

Type:  Optional[int]

GetDistributedSakKeyNumber()[¶](#tts.lib.ethernet.PacketMka.PacketMka.GetDistributedSakKeyNumber "Link to this definition")  
Returns:  Key Number from Distributed SAK Parameter Set. See IEEE 802.1X-2020, section 9.8 and table 11-7.

Return type:  int | None

distributedSakKeyNumber[¶](#tts.lib.ethernet.PacketMka.PacketMka.distributedSakKeyNumber "Link to this definition")  
Key Number from Distributed SAK Parameter Set. See IEEE 802.1X-2020, section 9.8 and table 11-7.

Type:  Optional[int]

GetDistributedSakCipherSuite()[¶](#tts.lib.ethernet.PacketMka.PacketMka.GetDistributedSakCipherSuite "Link to this definition")  
Returns:  MACsec Cipher Suite from Distributed SAK Parameter Set. Values from IEEE 802.1AE-2018, table 14-1. See IEEE 802.1X-2020, section 9.7 and table 11-7.

Return type:  [*ByteStream*](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream") | None

distributedSakCipherSuite[¶](#tts.lib.ethernet.PacketMka.PacketMka.distributedSakCipherSuite "Link to this definition")  
MACsec Cipher Suite from Distributed SAK Parameter Set. Values from IEEE 802.1AE-2018, table 14-1. See IEEE 802.1X-2020, section 9.7 and table 11-7.

Type:  Optional[[ByteStream](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream")]

SetDistributedSakToNoMacSec()[¶](#tts.lib.ethernet.PacketMka.PacketMka.SetDistributedSakToNoMacSec "Link to this definition")  
Change the values of the Distributed SAK Parameter Set so MACsec will not be used. See IEEE 802.1X-2020, figure 11-11, footnotes a and b.

RemoveDistributedSak()[¶](#tts.lib.ethernet.PacketMka.PacketMka.RemoveDistributedSak "Link to this definition")  
If the MKPDU has a Distributed SAK Parameter Set, remove it.

GetXpnLatestLpn()[¶](#tts.lib.ethernet.PacketMka.PacketMka.GetXpnLatestLpn "Link to this definition")  
Returns:  Latest Key Lowest Acceptable Packet Number (most significant 32 bits) from XPN Parameter Set. See IEEE 802.1X-2020, section 9.18 and table 11-7.

Return type:  int | None

xpnLatestLpn[¶](#tts.lib.ethernet.PacketMka.PacketMka.xpnLatestLpn "Link to this definition")  
Latest Key Lowest Acceptable Packet Number (most significant 32 bits) from XPN Parameter Set. See IEEE 802.1X-2020, section 9.18 and table 11-7.

Type:  Optional[int]

RemoveXpn()[¶](#tts.lib.ethernet.PacketMka.PacketMka.RemoveXpn "Link to this definition")  
If the MKPDU has an XPN Parameter Set, remove it.

GetAnnouncementTypes()[¶](#tts.lib.ethernet.PacketMka.PacketMka.GetAnnouncementTypes "Link to this definition")  
Returns:  TLV types from Announcement Parameter Set. See IEEE 802.1X-2020, section 9.7 and table 11-8.

Return type:  list[int] | None

announcementTypes[¶](#tts.lib.ethernet.PacketMka.PacketMka.announcementTypes "Link to this definition")  
TLV types from Announcement Parameter Set. See IEEE 802.1X-2020, section 9.7 and table 11-8.

Type:  Optional[list[int]]

GetAnnouncementInfos()[¶](#tts.lib.ethernet.PacketMka.PacketMka.GetAnnouncementInfos "Link to this definition")  
Returns:  TLV infos (without length bits) from Announcement Parameter Set. See IEEE 802.1X-2020, section 9.7 and figure 11-19.

Return type:  list[[*ByteStream*](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream")] | None

announcementInfos[¶](#tts.lib.ethernet.PacketMka.PacketMka.announcementInfos "Link to this definition")  
TLV infos (without length bits) from Announcement Parameter Set. See IEEE 802.1X-2020, section 9.7 and figure 11-19.

Type:  Optional[list[[ByteStream](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream")]]

GetAnnouncementCipherSuiteCapabilities()[¶](#tts.lib.ethernet.PacketMka.PacketMka.GetAnnouncementCipherSuiteCapabilities "Link to this definition")  
Returns:  Implementation capabilities for the MACsec Cipher Suites from Announcement Parameter Set. See IEEE 802.1X-2020, sections 9.7 and 11.12.3 and figure 11-22.

Return type:  list[*MacSecCapability*] | None

announcementCipherSuiteCapabilities[¶](#tts.lib.ethernet.PacketMka.PacketMka.announcementCipherSuiteCapabilities "Link to this definition")  
Implementation capabilities for the MACsec Cipher Suites from Announcement Parameter Set. See IEEE 802.1X-2020, sections 9.7 and 11.12.3 and figure 11-22.

Type:  Optional[list[MacSecCapability]]

GetAnnouncementCipherSuiteNames()[¶](#tts.lib.ethernet.PacketMka.PacketMka.GetAnnouncementCipherSuiteNames "Link to this definition")  
Returns:  Names of the supported Cipher Suites from Announcement Parameter Set, e.g. [‘GCM-AES-XPN-256’]. See IEEE 802.1X-2020, sections 9.7 and 11.12.3 and figure

Return type:  list[str] | None

announcementCipherSuiteNames[¶](#tts.lib.ethernet.PacketMka.PacketMka.announcementCipherSuiteNames "Link to this definition")  
Names of the supported Cipher Suites from Announcement Parameter Set, e.g. [‘GCM-AES-XPN-256’]. See IEEE 802.1X-2020, sections 9.7 and 11.12.3 and figure

Type:  Optional[list[str]]

FindParent(*protocol*)[¶](#tts.lib.ethernet.PacketMka.PacketMka.FindParent "Link to this definition")  
*Only for pseudo signals in trace analysis!* Returns the requested protocol object if present, otherwise a [`NoProtocol`](#tts.lib.ethernet.PacketEthernet.NoProtocol "tts.lib.ethernet.PacketEthernet.NoProtocol") object.

Parameters:  **protocol** ([*OsiProtocol*](#tts.lib.ethernet.PacketEthernet.OsiProtocol "tts.lib.ethernet.PacketEthernet.OsiProtocol")) – The required protocol name.

Returns:  The required parent protocol object.

Return type:  [EthernetProtocolBase](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase")

GetMacSecAn()[¶](#tts.lib.ethernet.PacketMka.PacketMka.GetMacSecAn "Link to this definition")  
Returns:  Association Number of MACsec header (see IEEE 802.1AE)

Return type:  int

GetMacSecIcv()[¶](#tts.lib.ethernet.PacketMka.PacketMka.GetMacSecIcv "Link to this definition")  
Returns:  Integrity check value of MACsec header (see IEEE 802.1AE)

Return type:  bytes

GetMacSecPn()[¶](#tts.lib.ethernet.PacketMka.PacketMka.GetMacSecPn "Link to this definition")  
Returns:  Packet Number of MACsec header (see IEEE 802.1AE)

Return type:  int

GetMacSecSl()[¶](#tts.lib.ethernet.PacketMka.PacketMka.GetMacSecSl "Link to this definition")  
Returns:  Short Length of MACsec header (see IEEE 802.1AE)

Return type:  int

GetMacSecTci()[¶](#tts.lib.ethernet.PacketMka.PacketMka.GetMacSecTci "Link to this definition")  
Returns:  TAG Control Information of MACsec header (see IEEE 802.1AE)

Return type:  int

GetMacSecTciAn()[¶](#tts.lib.ethernet.PacketMka.PacketMka.GetMacSecTciAn "Link to this definition")  
Returns:  TCI_AN byte of MACsec header (see IEEE 802.1AE)

Return type:  int

GetMacSecTciC()[¶](#tts.lib.ethernet.PacketMka.PacketMka.GetMacSecTciC "Link to this definition")  
Returns:  Changed text bit in TCI of MACsec header (see IEEE 802.1AE)

Return type:  bool

GetMacSecTciE()[¶](#tts.lib.ethernet.PacketMka.PacketMka.GetMacSecTciE "Link to this definition")  
Returns:  Encryption bit in TCI of MACsec header (see IEEE 802.1AE)

Return type:  bool

GetMacSecTciEs()[¶](#tts.lib.ethernet.PacketMka.PacketMka.GetMacSecTciEs "Link to this definition")  
Returns:  End station bit in TCI of MACsec header (see IEEE 802.1AE)

Return type:  bool

GetMacSecTciSc()[¶](#tts.lib.ethernet.PacketMka.PacketMka.GetMacSecTciSc "Link to this definition")  
Returns:  SCI indication bit in TCI of MACsec header (see IEEE 802.1AE)

Return type:  bool

GetMacSecTciScb()[¶](#tts.lib.ethernet.PacketMka.PacketMka.GetMacSecTciScb "Link to this definition")  
Returns:  Single copy broadcast capability bit in TCI of MACsec header (see IEEE 802.1AE)

Return type:  bool

GetMacSecTciV()[¶](#tts.lib.ethernet.PacketMka.PacketMka.GetMacSecTciV "Link to this definition")  
Returns:  Version bit in TCI of MACsec header (see IEEE 802.1AE)

Return type:  bool

GetTimestamp()[¶](#tts.lib.ethernet.PacketMka.PacketMka.GetTimestamp "Link to this definition")  
Returns:  Receive timestamp in sec., None if not available

Return type:  float | None

GetVlanCfi(*ixVlanTags*)[¶](#tts.lib.ethernet.PacketMka.PacketMka.GetVlanCfi "Link to this definition")  
Returns:  802.1a canonical format indicator

Return type:  int

GetVlanCfiOuter(*ixVlanTags*)[¶](#tts.lib.ethernet.PacketMka.PacketMka.GetVlanCfiOuter "Link to this definition")  
Returns:  802.1ad canonical format indicator

Return type:  int

GetVlanPcp(*ixVlanTags*)[¶](#tts.lib.ethernet.PacketMka.PacketMka.GetVlanPcp "Link to this definition")  
Returns:  802.1a priority code point

Return type:  int

GetVlanPcpOuter(*ixVlanTags*)[¶](#tts.lib.ethernet.PacketMka.PacketMka.GetVlanPcpOuter "Link to this definition")  
Returns:  802.1ad priority code point

Return type:  int

GetVlanVid(*ixVlanTags*)[¶](#tts.lib.ethernet.PacketMka.PacketMka.GetVlanVid "Link to this definition")  
Returns:  802.1a VLAN id

Return type:  int

GetVlanVidOuter(*ixVlanTags*)[¶](#tts.lib.ethernet.PacketMka.PacketMka.GetVlanVidOuter "Link to this definition")  
Returns:  802.1ad VLAN id

Return type:  int

RemoveAnnouncement()[¶](#tts.lib.ethernet.PacketMka.PacketMka.RemoveAnnouncement "Link to this definition")  
If the MKPDU has an Announcement Parameter Set, remove it.

SetTimestamp(*timestamp*)[¶](#tts.lib.ethernet.PacketMka.PacketMka.SetTimestamp "Link to this definition")  
Parameters:  **timestamp** (*float* *|* *None*) – Receive timestamp in sec., None if not available

SetVlanCfi(*cfi*)[¶](#tts.lib.ethernet.PacketMka.PacketMka.SetVlanCfi "Link to this definition")  
Parameters:  **cfi** (*int*) – 802.1a canonical format indicator

SetVlanCfiOuter(*cfi*)[¶](#tts.lib.ethernet.PacketMka.PacketMka.SetVlanCfiOuter "Link to this definition")  
Parameters:  **cfi** (*int*) – 802.1ad canonical format indicator

SetVlanPcp(*pcp*)[¶](#tts.lib.ethernet.PacketMka.PacketMka.SetVlanPcp "Link to this definition")  
Parameters:  **pcp** (*int*) – 802.1a priority code point

SetVlanPcpOuter(*pcp*)[¶](#tts.lib.ethernet.PacketMka.PacketMka.SetVlanPcpOuter "Link to this definition")  
Parameters:  **pcp** (*int*) – 802.1ad priority code point

SetVlanVid(*vid*)[¶](#tts.lib.ethernet.PacketMka.PacketMka.SetVlanVid "Link to this definition")  
Parameters:  **vid** (*int*) – 802.1a VLAN id

SetVlanVidOuter(*vid*)[¶](#tts.lib.ethernet.PacketMka.PacketMka.SetVlanVidOuter "Link to this definition")  
Parameters:  **vid** (*int*) – 802.1ad VLAN id

ethPayload[¶](#tts.lib.ethernet.PacketMka.PacketMka.ethPayload "Link to this definition")  
Ethernet payload

Type:  bytes

ethType[¶](#tts.lib.ethernet.PacketMka.PacketMka.ethType "Link to this definition")  
ethernet protocol type

Type:  int

macSecAn[¶](#tts.lib.ethernet.PacketMka.PacketMka.macSecAn "Link to this definition")  
Association Number of MACsec header (see IEEE 802.1AE)

Type:  int

macSecIcv[¶](#tts.lib.ethernet.PacketMka.PacketMka.macSecIcv "Link to this definition")  
Integrity check value of MACsec header (see IEEE 802.1AE)

Type:  bytes

macSecPn[¶](#tts.lib.ethernet.PacketMka.PacketMka.macSecPn "Link to this definition")  
Packet Number of MACsec header (see IEEE 802.1AE)

Type:  int

macSecSl[¶](#tts.lib.ethernet.PacketMka.PacketMka.macSecSl "Link to this definition")  
Short Length of MACsec header (see IEEE 802.1AE)

Type:  int

macSecTci[¶](#tts.lib.ethernet.PacketMka.PacketMka.macSecTci "Link to this definition")  
TAG Control Information of MACsec header (see IEEE 802.1AE)

Type:  int

macSecTciAn[¶](#tts.lib.ethernet.PacketMka.PacketMka.macSecTciAn "Link to this definition")  
TCI_AN byte of MACsec header (see IEEE 802.1AE)

Type:  int

macSecTciC[¶](#tts.lib.ethernet.PacketMka.PacketMka.macSecTciC "Link to this definition")  
Changed text bit in TCI of MACsec header (see IEEE 802.1AE)

Type:  bool

macSecTciE[¶](#tts.lib.ethernet.PacketMka.PacketMka.macSecTciE "Link to this definition")  
Encryption bit in TCI of MACsec header (see IEEE 802.1AE)

Type:  bool

macSecTciEs[¶](#tts.lib.ethernet.PacketMka.PacketMka.macSecTciEs "Link to this definition")  
End station bit in TCI of MACsec header (see IEEE 802.1AE)

Type:  bool

macSecTciSc[¶](#tts.lib.ethernet.PacketMka.PacketMka.macSecTciSc "Link to this definition")  
SCI indication bit in TCI of MACsec header (see IEEE 802.1AE)

Type:  bool

macSecTciScb[¶](#tts.lib.ethernet.PacketMka.PacketMka.macSecTciScb "Link to this definition")  
Single copy broadcast capability bit in TCI of MACsec header (see IEEE 802.1AE)

Type:  bool

macSecTciV[¶](#tts.lib.ethernet.PacketMka.PacketMka.macSecTciV "Link to this definition")  
Version bit in TCI of MACsec header (see IEEE 802.1AE)

Type:  bool

parent[¶](#tts.lib.ethernet.PacketMka.PacketMka.parent "Link to this definition")  
*Only for pseudo signals in trace analysis!* Returns the parent protocol object if there is one present, otherwise None.

Return type:  [EthernetProtocolBase](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase") | None

timestamp[¶](#tts.lib.ethernet.PacketMka.PacketMka.timestamp "Link to this definition")  
Receive timestamp in sec., None if not available

Type:  Optional[float]

vlanCfi[¶](#tts.lib.ethernet.PacketMka.PacketMka.vlanCfi "Link to this definition")  
802.1a canonical format indicator

Type:  int

vlanCfiOuter[¶](#tts.lib.ethernet.PacketMka.PacketMka.vlanCfiOuter "Link to this definition")  
802.1ad canonical format indicator

Type:  int

vlanPcp[¶](#tts.lib.ethernet.PacketMka.PacketMka.vlanPcp "Link to this definition")  
802.1a priority code point

Type:  int

vlanPcpOuter[¶](#tts.lib.ethernet.PacketMka.PacketMka.vlanPcpOuter "Link to this definition")  
802.1ad priority code point

Type:  int

vlanVid[¶](#tts.lib.ethernet.PacketMka.PacketMka.vlanVid "Link to this definition")  
802.1a VLAN id

Type:  int

vlanVidOuter[¶](#tts.lib.ethernet.PacketMka.PacketMka.vlanVidOuter "Link to this definition")  
802.1ad VLAN id

Type:  int

### PacketIke[¶](#packetike "Link to this heading")

*class* PacketIke[¶](#tts.lib.ethernet.PacketIke.PacketIke "Link to this definition")  
In the test case, use `api.Ethernet.PacketIke`; in UserPyModules, use `from tts.lib.ethernet.PacketIke import PacketIke`.

\<protocol\>  
Equivalent to method [`FindParent(protocol)`](#tts.lib.ethernet.PacketIke.PacketIke.FindParent "tts.lib.ethernet.PacketIke.PacketIke.FindParent"). Direct access to parent protocols. *protocol* is one of [`OsiProtocol`](#tts.lib.ethernet.PacketEthernet.OsiProtocol "tts.lib.ethernet.PacketEthernet.OsiProtocol").

Example: Signal.eth.src provides the source MAC address of the Ethernet protocol layer.

Type:  [`EthernetProtocolBase`](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase")

GetInitiatorSpi()[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetInitiatorSpi "Link to this definition")  
Returns:  Security Parameter Index chosen by the initiator

Return type:  [*ByteStream*](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream")

initiatorSpi[¶](#tts.lib.ethernet.PacketIke.PacketIke.initiatorSpi "Link to this definition")  
Security Parameter Index chosen by the initiator

Type:  [ByteStream](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream")

GetResponderSpi()[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetResponderSpi "Link to this definition")  
Returns:  Security Parameter Index chosen by the responder

Return type:  [*ByteStream*](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream")

responderSpi[¶](#tts.lib.ethernet.PacketIke.PacketIke.responderSpi "Link to this definition")  
Security Parameter Index chosen by the responder

Type:  [ByteStream](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream")

GetNextPayload()[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetNextPayload "Link to this definition")  
Returns:  type of next payload from IKE header

Return type:  int

nextPayload[¶](#tts.lib.ethernet.PacketIke.PacketIke.nextPayload "Link to this definition")  
type of next payload from IKE header

Type:  int

GetMajorVersion()[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetMajorVersion "Link to this definition")  
Returns:  major protocol version of IKE header

Return type:  int

majorVersion[¶](#tts.lib.ethernet.PacketIke.PacketIke.majorVersion "Link to this definition")  
major protocol version of IKE header

Type:  int

GetMinorVersion()[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetMinorVersion "Link to this definition")  
Returns:  minor protocol version of IKE header

Return type:  int

minorVersion[¶](#tts.lib.ethernet.PacketIke.PacketIke.minorVersion "Link to this definition")  
minor protocol version of IKE header

Type:  int

GetExchangeType()[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetExchangeType "Link to this definition")  
Returns:  exchange type of IKE header

Return type:  int

exchangeType[¶](#tts.lib.ethernet.PacketIke.PacketIke.exchangeType "Link to this definition")  
exchange type of IKE header

Type:  int

GetFlags()[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetFlags "Link to this definition")  
Returns:  flags of IKE header

Return type:  int

flags[¶](#tts.lib.ethernet.PacketIke.PacketIke.flags "Link to this definition")  
flags of IKE header

Type:  int

IsInitiator()[¶](#tts.lib.ethernet.PacketIke.PacketIke.IsInitiator "Link to this definition")  
Returns:  whether the initiator bit of IKE header flags is set

Return type:  bool

IsResponder()[¶](#tts.lib.ethernet.PacketIke.PacketIke.IsResponder "Link to this definition")  
Returns:  whether the initiator bit of IKE header flags is cleared

Return type:  bool

SetToInitiator()[¶](#tts.lib.ethernet.PacketIke.PacketIke.SetToInitiator "Link to this definition")  
Sets the initiator bit of IKE header flags

SetToResponder()[¶](#tts.lib.ethernet.PacketIke.PacketIke.SetToResponder "Link to this definition")  
Clears the initiator bit of IKE header flags

IsRequest()[¶](#tts.lib.ethernet.PacketIke.PacketIke.IsRequest "Link to this definition")  
Returns:  whether the response bit of IKE header flags is cleared

Return type:  bool

IsResponse()[¶](#tts.lib.ethernet.PacketIke.PacketIke.IsResponse "Link to this definition")  
Returns:  whether the response bit of IKE header flags is set

Return type:  bool

SetToRequest()[¶](#tts.lib.ethernet.PacketIke.PacketIke.SetToRequest "Link to this definition")  
Clears the response bit of IKE header flags

SetToReponse()[¶](#tts.lib.ethernet.PacketIke.PacketIke.SetToReponse "Link to this definition")  
Sets the response bit of IKE header flags

GetMessageId()[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetMessageId "Link to this definition")  
Returns:  message id of IKE header

Return type:  int

messageId[¶](#tts.lib.ethernet.PacketIke.PacketIke.messageId "Link to this definition")  
message id of IKE header

Type:  int

GetLength()[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetLength "Link to this definition")  
Returns:  length from IKE header, i.e. total message length including header and payloads)

Return type:  int

length[¶](#tts.lib.ethernet.PacketIke.PacketIke.length "Link to this definition")  
length from IKE header, i.e. total message length including header and payloads)

Type:  int

GetKeyExchangeNextPayload()[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetKeyExchangeNextPayload "Link to this definition")  
Returns:  type of next payload from KE payload, or None if there is no KE payload

Return type:  int | None

keyExchangeNextPayload[¶](#tts.lib.ethernet.PacketIke.PacketIke.keyExchangeNextPayload "Link to this definition")  
type of next payload from KE payload, or None if there is no KE payload

Type:  Optional[int]

IsKeyExchangeCritical()[¶](#tts.lib.ethernet.PacketIke.PacketIke.IsKeyExchangeCritical "Link to this definition")  
Returns:  critical flag of KE payload, or None if there is no KE payload

Return type:  bool | None

keyExchangeCritical[¶](#tts.lib.ethernet.PacketIke.PacketIke.keyExchangeCritical "Link to this definition")  
critical flag of KE payload, or None if there is no KE payload

Type:  Optional[bool]

GetKeyExchangeLength()[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetKeyExchangeLength "Link to this definition")  
Returns:  length of KE payload, or None if there is no KE payload

Return type:  int | None

keyExchangeLength[¶](#tts.lib.ethernet.PacketIke.PacketIke.keyExchangeLength "Link to this definition")  
length of KE payload, or None if there is no KE payload

Type:  Optional[int]

GetKeyExchangeDhGroupNumber()[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetKeyExchangeDhGroupNumber "Link to this definition")  
Returns:  Diffie-Hellman group number of KE payload, or None if there is no KE payload

Return type:  int | None

keyExchangeDhGroupNumber[¶](#tts.lib.ethernet.PacketIke.PacketIke.keyExchangeDhGroupNumber "Link to this definition")  
Diffie-Hellman group number of KE payload, or None if there is no KE payload

Type:  Optional[int]

GetKeyExchangeData()[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetKeyExchangeData "Link to this definition")  
Returns:  key exchange data from KE payload, or None if there is no KE payload

Return type:  [*ByteStream*](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream") | None

keyExchangeData[¶](#tts.lib.ethernet.PacketIke.PacketIke.keyExchangeData "Link to this definition")  
key exchange data from KE payload, or None if there is no KE payload

Type:  Optional[[ByteStream](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream")]

GetNonceNextPayload()[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetNonceNextPayload "Link to this definition")  
Returns:  type of next payload from nonce payload, or None if there is no nonce payload

Return type:  int | None

nonceNextPayload[¶](#tts.lib.ethernet.PacketIke.PacketIke.nonceNextPayload "Link to this definition")  
type of next payload from nonce payload, or None if there is no nonce payload

Type:  Optional[int]

IsNonceCritical()[¶](#tts.lib.ethernet.PacketIke.PacketIke.IsNonceCritical "Link to this definition")  
Returns:  critical flag of nonce payload, or None if there is no nonce payload

Return type:  bool | None

nonceCritical[¶](#tts.lib.ethernet.PacketIke.PacketIke.nonceCritical "Link to this definition")  
critical flag of nonce payload, or None if there is no nonce payload

Type:  Optional[bool]

GetNonceLength()[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetNonceLength "Link to this definition")  
Returns:  length of nonce payload, or None if there is no nonce payload

Return type:  int | None

nonceLength[¶](#tts.lib.ethernet.PacketIke.PacketIke.nonceLength "Link to this definition")  
length of nonce payload, or None if there is no nonce payload

Type:  Optional[int]

GetNonceData()[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetNonceData "Link to this definition")  
Returns:  nonce data, or None if there is no nonce payload

Return type:  [*ByteStream*](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream") | None

nonceData[¶](#tts.lib.ethernet.PacketIke.PacketIke.nonceData "Link to this definition")  
nonce data, or None if there is no nonce payload

Type:  Optional[[ByteStream](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream")]

GetCertificateNextPayload()[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetCertificateNextPayload "Link to this definition")  
Returns:  type of next payload from CERT payload, or None if there is no CERT payload

Return type:  int | None

certificateNextPayload[¶](#tts.lib.ethernet.PacketIke.PacketIke.certificateNextPayload "Link to this definition")  
type of next payload from CERT payload, or None if there is no CERT payload

Type:  Optional[int]

IsCertificateCritical()[¶](#tts.lib.ethernet.PacketIke.PacketIke.IsCertificateCritical "Link to this definition")  
Returns:  critical flag of CERT payload, or None if there is no CERT payload

Return type:  bool | None

certificateCritical[¶](#tts.lib.ethernet.PacketIke.PacketIke.certificateCritical "Link to this definition")  
critical flag of CERT payload, or None if there is no CERT payload

Type:  Optional[bool]

GetCertificateLength()[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetCertificateLength "Link to this definition")  
Returns:  length of CERT payload, or None if there is no CERT payload

Return type:  int | None

certificateLength[¶](#tts.lib.ethernet.PacketIke.PacketIke.certificateLength "Link to this definition")  
length of CERT payload, or None if there is no CERT payload

Type:  Optional[int]

GetCertificateEncoding()[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetCertificateEncoding "Link to this definition")  
Returns:  certificate encoding of CERT payload, or None if there is no CERT payload

Return type:  int | None

certificateEncoding[¶](#tts.lib.ethernet.PacketIke.PacketIke.certificateEncoding "Link to this definition")  
certificate encoding of CERT payload, or None if there is no CERT payload

Type:  Optional[int]

GetCertificateData()[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetCertificateData "Link to this definition")  
Returns:  certificate data of CERT payload, or None if there is no CERT payload

Return type:  [*ByteStream*](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream") | None

certificateData[¶](#tts.lib.ethernet.PacketIke.PacketIke.certificateData "Link to this definition")  
certificate data of CERT payload, or None if there is no CERT payload

Type:  Optional[[ByteStream](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream")]

GetCertificateRequestNextPayload()[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetCertificateRequestNextPayload "Link to this definition")  
Returns:  type of next payload from CERTREQ payload, or None if there is no CERTREQ payload

Return type:  int | None

certificateRequestNextPayload[¶](#tts.lib.ethernet.PacketIke.PacketIke.certificateRequestNextPayload "Link to this definition")  
type of next payload from CERTREQ payload, or None if there is no CERTREQ payload

Type:  Optional[int]

GetCertificateRequestCritical()[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetCertificateRequestCritical "Link to this definition")  
Returns:  critical flag of CERTREQ payload, or None if there is no CERTREQ payload

Return type:  bool | None

certificateRequestCritical[¶](#tts.lib.ethernet.PacketIke.PacketIke.certificateRequestCritical "Link to this definition")  
critical flag of CERTREQ payload, or None if there is no CERTREQ payload

Type:  Optional[bool]

GetCertificateRequestLength()[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetCertificateRequestLength "Link to this definition")  
Returns:  length of CERTREQ payload, or None if there is no CERTREQ payload

Return type:  int | None

certificateRequestLength[¶](#tts.lib.ethernet.PacketIke.PacketIke.certificateRequestLength "Link to this definition")  
length of CERTREQ payload, or None if there is no CERTREQ payload

Type:  Optional[int]

GetCertificateRequestData()[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetCertificateRequestData "Link to this definition")  
Returns:  concatenated certificate authorities’ public key SHA-1 hashes of CERTREQ payload, or None if there is no CERTREQ payload

Return type:  [*ByteStream*](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream") | None

certificateRequestData[¶](#tts.lib.ethernet.PacketIke.PacketIke.certificateRequestData "Link to this definition")  
concatenated certificate authorities’ public key SHA-1 hashes of CERTREQ payload, or None if there is no CERTREQ payload

Type:  Optional[[ByteStream](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream")]

GetCertificateRequestEncoding()[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetCertificateRequestEncoding "Link to this definition")  
Returns:  certificate encoding of CERTREQ payload, or None if there is no CERTREQ payload

Return type:  int | None

certificateRequestEncoding[¶](#tts.lib.ethernet.PacketIke.PacketIke.certificateRequestEncoding "Link to this definition")  
certificate encoding of CERTREQ payload, or None if there is no CERTREQ payload

Type:  Optional[int]

GetIdentInitiatorNextPayload()[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetIdentInitiatorNextPayload "Link to this definition")  
Returns:  type of next payload from IDi payload, or None if there is no IDi payload

Return type:  int | None

identInitiatorNextPayload[¶](#tts.lib.ethernet.PacketIke.PacketIke.identInitiatorNextPayload "Link to this definition")  
type of next payload from IDi payload, or None if there is no IDi payload

Type:  Optional[int]

GetIdentInitiatorCritical()[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetIdentInitiatorCritical "Link to this definition")  
Returns:  critical flag of IDi payload, or None if there is no IDi payload

Return type:  bool | None

identInitiatorCritical[¶](#tts.lib.ethernet.PacketIke.PacketIke.identInitiatorCritical "Link to this definition")  
critical flag of IDi payload, or None if there is no IDi payload

Type:  Optional[bool]

GetIdentInitiatorLength()[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetIdentInitiatorLength "Link to this definition")  
Returns:  length of IDi payload, or None if there is no IDi payload

Return type:  int | None

identInitiatorLength[¶](#tts.lib.ethernet.PacketIke.PacketIke.identInitiatorLength "Link to this definition")  
length of IDi payload, or None if there is no IDi payload

Type:  Optional[int]

GetIdentInitiatorIdType()[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetIdentInitiatorIdType "Link to this definition")  
Returns:  identification type of IDi payload, or None if there is no IDi payload

Return type:  int | None

identInitiatorIdType[¶](#tts.lib.ethernet.PacketIke.PacketIke.identInitiatorIdType "Link to this definition")  
identification type of IDi payload, or None if there is no IDi payload

Type:  Optional[int]

GetIdentInitiatorData()[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetIdentInitiatorData "Link to this definition")  
Returns:  identification data of IDi payload, or None if there is no IDi payload

Return type:  [*ByteStream*](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream") | None

identInitiatorData[¶](#tts.lib.ethernet.PacketIke.PacketIke.identInitiatorData "Link to this definition")  
identification data of IDi payload, or None if there is no IDi payload

Type:  Optional[[ByteStream](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream")]

GetIdentResponderNextPayload()[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetIdentResponderNextPayload "Link to this definition")  
Returns:  type of next payload from IDr payload, or None if there is no IDr payload

Return type:  int | None

identResponderNextPayload[¶](#tts.lib.ethernet.PacketIke.PacketIke.identResponderNextPayload "Link to this definition")  
type of next payload from IDr payload, or None if there is no IDr payload

Type:  Optional[int]

GetIdentResponderCritical()[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetIdentResponderCritical "Link to this definition")  
Returns:  critical flag of IDr payload, or None if there is no IDr payload

Return type:  bool | None

identResponderCritical[¶](#tts.lib.ethernet.PacketIke.PacketIke.identResponderCritical "Link to this definition")  
critical flag of IDr payload, or None if there is no IDr payload

Type:  Optional[bool]

GetIdentResponderLength()[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetIdentResponderLength "Link to this definition")  
Returns:  length of IDr payload, or None if there is no IDr payload

Return type:  int | None

identResponderLength[¶](#tts.lib.ethernet.PacketIke.PacketIke.identResponderLength "Link to this definition")  
length of IDr payload, or None if there is no IDr payload

Type:  Optional[int]

GetIdentResponderIdType()[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetIdentResponderIdType "Link to this definition")  
Returns:  identification type of IDr payload, or None if there is no IDr payload

Return type:  int | None

identResponderIdType[¶](#tts.lib.ethernet.PacketIke.PacketIke.identResponderIdType "Link to this definition")  
identification type of IDr payload, or None if there is no IDr payload

Type:  Optional[int]

GetIdentResponderData()[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetIdentResponderData "Link to this definition")  
Returns:  identification data of IDr payload, or None if there is no IDr payload

Return type:  [*ByteStream*](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream") | None

identResponderData[¶](#tts.lib.ethernet.PacketIke.PacketIke.identResponderData "Link to this definition")  
identification data of IDr payload, or None if there is no IDr payload

Type:  Optional[[ByteStream](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream")]

GetAuthNextPayload()[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetAuthNextPayload "Link to this definition")  
Returns:  type of next payload from AUTH payload, or None if there is no AUTH payload

Return type:  int | None

authNextPayload[¶](#tts.lib.ethernet.PacketIke.PacketIke.authNextPayload "Link to this definition")  
type of next payload from AUTH payload, or None if there is no AUTH payload

Type:  Optional[int]

GetAuthCritical()[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetAuthCritical "Link to this definition")  
Returns:  critical flag of AUTH payload, or None if there is no AUTH payload

Return type:  bool | None

authCritical[¶](#tts.lib.ethernet.PacketIke.PacketIke.authCritical "Link to this definition")  
critical flag of AUTH payload, or None if there is no AUTH payload

Type:  Optional[bool]

GetAuthLength()[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetAuthLength "Link to this definition")  
Returns:  length of AUTH payload, or None if there is no AUTH payload

Return type:  int | None

authLength[¶](#tts.lib.ethernet.PacketIke.PacketIke.authLength "Link to this definition")  
length of AUTH payload, or None if there is no AUTH payload

Type:  Optional[int]

GetAuthMethod()[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetAuthMethod "Link to this definition")  
Returns:  authentication method of AUTH payload, or None if there is no AUTH payload

Return type:  int | None

authMethod[¶](#tts.lib.ethernet.PacketIke.PacketIke.authMethod "Link to this definition")  
authentication method of AUTH payload, or None if there is no AUTH payload

Type:  Optional[int]

GetAuthData()[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetAuthData "Link to this definition")  
Returns:  authentication data of AUTH payload, or None if there is no AUTH payload

Return type:  [*ByteStream*](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream") | None

authData[¶](#tts.lib.ethernet.PacketIke.PacketIke.authData "Link to this definition")  
authentication data of AUTH payload, or None if there is no AUTH payload

Type:  Optional[[ByteStream](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream")]

GetTsInitiatorNextPayload()[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetTsInitiatorNextPayload "Link to this definition")  
Returns:  type of next payload from TSi payload, or None if there is no TSi payload

Return type:  int | None

tsInitiatorNextPayload[¶](#tts.lib.ethernet.PacketIke.PacketIke.tsInitiatorNextPayload "Link to this definition")  
type of next payload from TSi payload, or None if there is no TSi payload

Type:  Optional[int]

GetTsInitiatorCritical()[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetTsInitiatorCritical "Link to this definition")  
Returns:  critical flag of TSi payload, or None if there is no TSi payload

Return type:  bool | None

tsInitiatorCritical[¶](#tts.lib.ethernet.PacketIke.PacketIke.tsInitiatorCritical "Link to this definition")  
critical flag of TSi payload, or None if there is no TSi payload

Type:  Optional[bool]

GetTsInitiatorLength()[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetTsInitiatorLength "Link to this definition")  
Returns:  length of TSi payload, or None if there is no TSi payload

Return type:  int | None

tsInitiatorLength[¶](#tts.lib.ethernet.PacketIke.PacketIke.tsInitiatorLength "Link to this definition")  
length of TSi payload, or None if there is no TSi payload

Type:  Optional[int]

GetTsInitiatorNumOfTss()[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetTsInitiatorNumOfTss "Link to this definition")  
Returns:  number of traffic selectors of TSi payload, or None if there is no TSi payload

Return type:  int | None

tsInitiatorNumOfTss[¶](#tts.lib.ethernet.PacketIke.PacketIke.tsInitiatorNumOfTss "Link to this definition")  
number of traffic selectors of TSi payload, or None if there is no TSi payload

Type:  Optional[int]

GetTsInitiatorTrafficSelectors()[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetTsInitiatorTrafficSelectors "Link to this definition")  
Returns:  traffic selector data of TSi payload, or None if there is no TSi payload

Return type:  [*ByteStream*](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream")

tsInitiatorTrafficSelectors[¶](#tts.lib.ethernet.PacketIke.PacketIke.tsInitiatorTrafficSelectors "Link to this definition")  
traffic selector data of TSi payload, or None if there is no TSi payload

Type:  [ByteStream](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream")

GetTsResponderNextPayload()[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetTsResponderNextPayload "Link to this definition")  
Returns:  type of next payload from TSr payload, or None if there is no TSr payload

Return type:  int | None

tsResponderNextPayload[¶](#tts.lib.ethernet.PacketIke.PacketIke.tsResponderNextPayload "Link to this definition")  
type of next payload from TSr payload, or None if there is no TSr payload

Type:  Optional[int]

GetTsResponderCritical()[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetTsResponderCritical "Link to this definition")  
Returns:  critical flag of TSr payload, or None if there is no TSr payload

Return type:  bool | None

tsResponderCritical[¶](#tts.lib.ethernet.PacketIke.PacketIke.tsResponderCritical "Link to this definition")  
critical flag of TSr payload, or None if there is no TSr payload

Type:  Optional[bool]

GetTsResponderLength()[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetTsResponderLength "Link to this definition")  
Returns:  length of TSr payload, or None if there is no TSr payload

Return type:  int | None

tsResponderLength[¶](#tts.lib.ethernet.PacketIke.PacketIke.tsResponderLength "Link to this definition")  
length of TSr payload, or None if there is no TSr payload

Type:  Optional[int]

GetTsResponderNumOfTss()[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetTsResponderNumOfTss "Link to this definition")  
Returns:  number of traffic selectors of TSr payload, or None if there is no TSr payload

Return type:  int | None

tsResponderNumOfTss[¶](#tts.lib.ethernet.PacketIke.PacketIke.tsResponderNumOfTss "Link to this definition")  
number of traffic selectors of TSr payload, or None if there is no TSr payload

Type:  Optional[int]

GetTsResponderTrafficSelectors()[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetTsResponderTrafficSelectors "Link to this definition")  
Returns:  traffic selector data of TSr payload, or None if there is no TSr payload

Return type:  [*ByteStream*](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream")

tsResponderTrafficSelectors[¶](#tts.lib.ethernet.PacketIke.PacketIke.tsResponderTrafficSelectors "Link to this definition")  
traffic selector data of TSr payload, or None if there is no TSr payload

Type:  [ByteStream](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream")

GetSaNextPayload()[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetSaNextPayload "Link to this definition")  
Returns:  type of next payload from SA payload, or None if there is no SA payload

Return type:  int | None

saNextPayload[¶](#tts.lib.ethernet.PacketIke.PacketIke.saNextPayload "Link to this definition")  
type of next payload from SA payload, or None if there is no SA payload

Type:  Optional[int]

GetSaCritical()[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetSaCritical "Link to this definition")  
Returns:  critical flag of SA payload, or None if there is no SA payload

Return type:  bool | None

saCritical[¶](#tts.lib.ethernet.PacketIke.PacketIke.saCritical "Link to this definition")  
critical flag of SA payload, or None if there is no SA payload

Type:  Optional[bool]

GetSaLength()[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetSaLength "Link to this definition")  
Returns:  length of SA payload, or None if there is no SA payload

Return type:  int | None

saLength[¶](#tts.lib.ethernet.PacketIke.PacketIke.saLength "Link to this definition")  
length of SA payload, or None if there is no SA payload

Type:  Optional[int]

GetSaProposals()[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetSaProposals "Link to this definition")  
Returns:  proposal data SA payload, or None if there is no SA payload

Return type:  [*ByteStream*](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream") | None

saProposals[¶](#tts.lib.ethernet.PacketIke.PacketIke.saProposals "Link to this definition")  
proposal data SA payload, or None if there is no SA payload

Type:  Optional[[ByteStream](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream")]

GetNotifyNumOfPayloads()[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetNotifyNumOfPayloads "Link to this definition")  
Returns:  number of Notify payloads in this IKEv2 packet

Return type:  int

notifyNumOfPayloads[¶](#tts.lib.ethernet.PacketIke.PacketIke.notifyNumOfPayloads "Link to this definition")  
number of Notify payloads in this IKEv2 packet

Type:  int

GetNotifyNextPayload(*notifyIdx=-1*)[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetNotifyNextPayload "Link to this definition")  
Returns:  type of next payload from Notify payload, or None if there is no Notify payload

Return type:  int | None

notifyNextPayload[¶](#tts.lib.ethernet.PacketIke.PacketIke.notifyNextPayload "Link to this definition")  
type of next payload from Notify payload, or None if there is no Notify payload

Type:  Optional[int]

GetNotifyCritical(*notifyIdx=-1*)[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetNotifyCritical "Link to this definition")  
Returns:  critical flag of Notify payload, or None if there is no Notify payload

Return type:  bool | None

notifyCritical[¶](#tts.lib.ethernet.PacketIke.PacketIke.notifyCritical "Link to this definition")  
critical flag of Notify payload, or None if there is no Notify payload

Type:  Optional[bool]

GetNotifyLength(*notifyIdx=-1*)[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetNotifyLength "Link to this definition")  
Returns:  length of Notify payload, or None if there is no Notify payload

Return type:  int | None

notifyLength[¶](#tts.lib.ethernet.PacketIke.PacketIke.notifyLength "Link to this definition")  
length of Notify payload, or None if there is no Notify payload

Type:  Optional[int]

GetNotifyProtocolId(*notifyIdx=-1*)[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetNotifyProtocolId "Link to this definition")  
Returns:  protocol id of Notify payload, or None if there is no Notify payload

Return type:  int | None

notifyProtocolId[¶](#tts.lib.ethernet.PacketIke.PacketIke.notifyProtocolId "Link to this definition")  
protocol id of Notify payload, or None if there is no Notify payload

Type:  Optional[int]

GetNotifySpiSize(*notifyIdx=-1*)[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetNotifySpiSize "Link to this definition")  
Returns:  SPI size of Notify payload, or None if there is no Notify payload

Return type:  int | None

notifySpiSize[¶](#tts.lib.ethernet.PacketIke.PacketIke.notifySpiSize "Link to this definition")  
SPI size of Notify payload, or None if there is no Notify payload

Type:  Optional[int]

GetNotifyMessageType(*notifyIdx=-1*)[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetNotifyMessageType "Link to this definition")  
Returns:  notify message type of Notify payload, or None if there is no Notify payload

Return type:  int | None

notifyMessageType[¶](#tts.lib.ethernet.PacketIke.PacketIke.notifyMessageType "Link to this definition")  
notify message type of Notify payload, or None if there is no Notify payload

Type:  Optional[int]

GetNotifySpi(*notifyIdx=-1*)[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetNotifySpi "Link to this definition")  
Returns:  SPI of Notify payload, or None if there is no Notify payload

Return type:  [*ByteStream*](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream") | None

notifySpi[¶](#tts.lib.ethernet.PacketIke.PacketIke.notifySpi "Link to this definition")  
SPI of Notify payload, or None if there is no Notify payload

Type:  Optional[[ByteStream](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream")]

GetNotifyData(*notifyIdx=-1*)[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetNotifyData "Link to this definition")  
Returns:  notification data of Notify payload, or None if there is no Notify payload

Return type:  [*ByteStream*](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream") | None

notifyData[¶](#tts.lib.ethernet.PacketIke.PacketIke.notifyData "Link to this definition")  
notification data of Notify payload, or None if there is no Notify payload

Type:  Optional[[ByteStream](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream")]

GetDeleteNextPayload()[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetDeleteNextPayload "Link to this definition")  
Returns:  type of next payload from Delete payload, or None if there is no Delete payload

Return type:  int | None

deleteNextPayload[¶](#tts.lib.ethernet.PacketIke.PacketIke.deleteNextPayload "Link to this definition")  
type of next payload from Delete payload, or None if there is no Delete payload

Type:  Optional[int]

GetDeleteCritical()[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetDeleteCritical "Link to this definition")  
Returns:  critical flag of Delete payload, or None if there is no Delete payload

Return type:  bool | None

deleteCritical[¶](#tts.lib.ethernet.PacketIke.PacketIke.deleteCritical "Link to this definition")  
critical flag of Delete payload, or None if there is no Delete payload

Type:  Optional[bool]

GetDeleteLength()[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetDeleteLength "Link to this definition")  
Returns:  length of Delete payload, or None if there is no Delete payload

Return type:  int | None

deleteLength[¶](#tts.lib.ethernet.PacketIke.PacketIke.deleteLength "Link to this definition")  
length of Delete payload, or None if there is no Delete payload

Type:  Optional[int]

GetDeleteProtocolId()[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetDeleteProtocolId "Link to this definition")  
Returns:  protocol id of Delete payload, or None if there is no Delete payload

Return type:  int | None

deleteProtocolId[¶](#tts.lib.ethernet.PacketIke.PacketIke.deleteProtocolId "Link to this definition")  
protocol id of Delete payload, or None if there is no Delete payload

Type:  Optional[int]

GetDeleteSpiSize()[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetDeleteSpiSize "Link to this definition")  
Returns:  SPI size of Delete payload, or None if there is no Delete payload

Return type:  int | None

deleteSpiSize[¶](#tts.lib.ethernet.PacketIke.PacketIke.deleteSpiSize "Link to this definition")  
SPI size of Delete payload, or None if there is no Delete payload

Type:  Optional[int]

GetDeleteSpis()[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetDeleteSpis "Link to this definition")  
Returns:  SPI list of Delete payload, or None if there is no Delete payload

Return type:  list[int] | None

CalcIpLen()[¶](#tts.lib.ethernet.PacketIke.PacketIke.CalcIpLen "Link to this definition")  
Calculate and set the current length of this IP packet

CalcUdpLen()[¶](#tts.lib.ethernet.PacketIke.PacketIke.CalcUdpLen "Link to this definition")  
Calculate and set the current length of this segment

FindParent(*protocol*)[¶](#tts.lib.ethernet.PacketIke.PacketIke.FindParent "Link to this definition")  
*Only for pseudo signals in trace analysis!* Returns the requested protocol object if present, otherwise a [`NoProtocol`](#tts.lib.ethernet.PacketEthernet.NoProtocol "tts.lib.ethernet.PacketEthernet.NoProtocol") object.

Parameters:  **protocol** ([*OsiProtocol*](#tts.lib.ethernet.PacketEthernet.OsiProtocol "tts.lib.ethernet.PacketEthernet.OsiProtocol")) – The required protocol name.

Returns:  The required parent protocol object.

Return type:  [EthernetProtocolBase](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase")

GetEthDstMac()[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetEthDstMac "Link to this definition")  
Returns:  target MAC address e.g. DE:AD:BE:EF:FF:00

Return type:  str

GetEthPayload()[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetEthPayload "Link to this definition")  
Returns:  Ethernet payload

Return type:  bytes

GetEthSrcMac()[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetEthSrcMac "Link to this definition")  
Returns:  source MAC address e.g. DE:AD:BE:EF:FF:00

Return type:  str

GetEthType()[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetEthType "Link to this definition")  
Returns:  ethernet protocol type

Return type:  int

GetIpAhIcv()[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetIpAhIcv "Link to this definition")  
Returns:  Integrity check value of IP authentication header (see RFC 4302)

Return type:  bytes

GetIpAhLen()[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetIpAhLen "Link to this definition")  
Returns:  Length value of IP authentication header (see RFC 4302) =\> len(ICV)/4+1

Return type:  int

GetIpAhNxt()[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetIpAhNxt "Link to this definition")  
Returns:  Next header value of IP authentication header (see RFC 4302)

Return type:  int

GetIpAhRsvd()[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetIpAhRsvd "Link to this definition")  
Returns:  Reserved value of IP authentication header (see RFC 4302)

Return type:  int

GetIpAhSeq()[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetIpAhSeq "Link to this definition")  
Returns:  Sequence number field of IP authentication header (see RFC 4302)

Return type:  int

GetIpAhSpi()[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetIpAhSpi "Link to this definition")  
Returns:  Security parameters index of IP authentication header (see RFC 4302)

Return type:  int

GetIpChecksum()[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetIpChecksum "Link to this definition")  
Returns:  checksum

Return type:  int

GetIpDst()[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetIpDst "Link to this definition")  
Returns:  target IP address e.g. 127.0.0.1

Return type:  str

GetIpIdent()[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetIpIdent "Link to this definition")  
Returns:  identifier

Return type:  int

GetIpLen()[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetIpLen "Link to this definition")  
Returns:  packet length

Return type:  int

GetIpOffset()[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetIpOffset "Link to this definition")  
Returns:  flags and offset combined

Return type:  int

GetIpPayload()[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetIpPayload "Link to this definition")  
Returns:  IP payload

Return type:  bytes

GetIpProt()[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetIpProt "Link to this definition")  
Returns:  protocol type / next header field

Return type:  int

GetIpSrc()[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetIpSrc "Link to this definition")  
Returns:  source IP address e.g. 127.0.0.1

Return type:  str

GetIpTos()[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetIpTos "Link to this definition")  
Returns:  type of service

Return type:  int

GetIpTtl()[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetIpTtl "Link to this definition")  
Returns:  TTL

Return type:  int

GetIpVersionAndHeaderLength()[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetIpVersionAndHeaderLength "Link to this definition")  
Returns:  protocol version and header length

Return type:  int

GetMacSecAn()[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetMacSecAn "Link to this definition")  
Returns:  Association Number of MACsec header (see IEEE 802.1AE)

Return type:  int

GetMacSecIcv()[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetMacSecIcv "Link to this definition")  
Returns:  Integrity check value of MACsec header (see IEEE 802.1AE)

Return type:  bytes

GetMacSecPn()[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetMacSecPn "Link to this definition")  
Returns:  Packet Number of MACsec header (see IEEE 802.1AE)

Return type:  int

GetMacSecSci()[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetMacSecSci "Link to this definition")  
Returns:  Secure Channel Identifier of MACsec header (see IEEE 802.1AE)

Return type:  bytes

GetMacSecSl()[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetMacSecSl "Link to this definition")  
Returns:  Short Length of MACsec header (see IEEE 802.1AE)

Return type:  int

GetMacSecTci()[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetMacSecTci "Link to this definition")  
Returns:  TAG Control Information of MACsec header (see IEEE 802.1AE)

Return type:  int

GetMacSecTciAn()[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetMacSecTciAn "Link to this definition")  
Returns:  TCI_AN byte of MACsec header (see IEEE 802.1AE)

Return type:  int

GetMacSecTciC()[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetMacSecTciC "Link to this definition")  
Returns:  Changed text bit in TCI of MACsec header (see IEEE 802.1AE)

Return type:  bool

GetMacSecTciE()[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetMacSecTciE "Link to this definition")  
Returns:  Encryption bit in TCI of MACsec header (see IEEE 802.1AE)

Return type:  bool

GetMacSecTciEs()[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetMacSecTciEs "Link to this definition")  
Returns:  End station bit in TCI of MACsec header (see IEEE 802.1AE)

Return type:  bool

GetMacSecTciSc()[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetMacSecTciSc "Link to this definition")  
Returns:  SCI indication bit in TCI of MACsec header (see IEEE 802.1AE)

Return type:  bool

GetMacSecTciScb()[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetMacSecTciScb "Link to this definition")  
Returns:  Single copy broadcast capability bit in TCI of MACsec header (see IEEE 802.1AE)

Return type:  bool

GetMacSecTciV()[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetMacSecTciV "Link to this definition")  
Returns:  Version bit in TCI of MACsec header (see IEEE 802.1AE)

Return type:  bool

GetTimestamp()[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetTimestamp "Link to this definition")  
Returns:  Receive timestamp in sec., None if not available

Return type:  float | None

GetUdpChecksum()[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetUdpChecksum "Link to this definition")  
Returns:  checksum

Return type:  int

GetUdpDst()[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetUdpDst "Link to this definition")  
Returns:  destination port

Return type:  int

GetUdpLen()[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetUdpLen "Link to this definition")  
Returns:  length of the UDP segment

Return type:  int

GetUdpPayload()[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetUdpPayload "Link to this definition")  
Returns:  UDP payload

Return type:  bytes

GetUdpSrc()[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetUdpSrc "Link to this definition")  
Returns:  source port

Return type:  int

GetVlanCfi(*ixVlanTags*)[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetVlanCfi "Link to this definition")  
Returns:  802.1a canonical format indicator

Return type:  int

GetVlanCfiOuter(*ixVlanTags*)[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetVlanCfiOuter "Link to this definition")  
Returns:  802.1ad canonical format indicator

Return type:  int

GetVlanPcp(*ixVlanTags*)[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetVlanPcp "Link to this definition")  
Returns:  802.1a priority code point

Return type:  int

GetVlanPcpOuter(*ixVlanTags*)[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetVlanPcpOuter "Link to this definition")  
Returns:  802.1ad priority code point

Return type:  int

GetVlanVid(*ixVlanTags*)[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetVlanVid "Link to this definition")  
Returns:  802.1a VLAN id

Return type:  int

GetVlanVidOuter(*ixVlanTags*)[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetVlanVidOuter "Link to this definition")  
Returns:  802.1ad VLAN id

Return type:  int

PK_CLASS[¶](#tts.lib.ethernet.PacketIke.PacketIke.PK_CLASS "Link to this definition")  
alias of `IP`

SetEthDstMac(*mac*)[¶](#tts.lib.ethernet.PacketIke.PacketIke.SetEthDstMac "Link to this definition")  
Parameters:  **mac** (*str*) – target MAC address e.g. DE:AD:BE:EF:FF:00

SetEthPayload(*payload*)[¶](#tts.lib.ethernet.PacketIke.PacketIke.SetEthPayload "Link to this definition")  
Parameters:  **payload** (*bytes*) – Ethernet payload

SetEthSrcMac(*mac*)[¶](#tts.lib.ethernet.PacketIke.PacketIke.SetEthSrcMac "Link to this definition")  
Parameters:  **mac** (*str*) – source MAC addres e.g. DE:AD:BE:EF:FF:00

SetEthType(*ethType*)[¶](#tts.lib.ethernet.PacketIke.PacketIke.SetEthType "Link to this definition")  
Parameters:  **ethType** (*int*) – ethernet protocol type

SetIpChecksum(*checksum*)[¶](#tts.lib.ethernet.PacketIke.PacketIke.SetIpChecksum "Link to this definition")  
Parameters:  **checksum** (*int*) – checksum

SetIpDst(*addr*)[¶](#tts.lib.ethernet.PacketIke.PacketIke.SetIpDst "Link to this definition")  
Parameters:  **addr** (*str*) – target IP address e.g. 127.0.0.1

SetIpIdent(*ident*)[¶](#tts.lib.ethernet.PacketIke.PacketIke.SetIpIdent "Link to this definition")  
Parameters:  **ident** (*int*) – identifier

SetIpLen(*length*)[¶](#tts.lib.ethernet.PacketIke.PacketIke.SetIpLen "Link to this definition")  
Parameters:  **length** (*int*) – packet length

SetIpOffset(*offset*)[¶](#tts.lib.ethernet.PacketIke.PacketIke.SetIpOffset "Link to this definition")  
Parameters:  **offset** (*int*) – flags and offset combined

SetIpPayload(*payload*)[¶](#tts.lib.ethernet.PacketIke.PacketIke.SetIpPayload "Link to this definition")  
Parameters:  **payload** (*bytes*) – IP payload

SetIpProt(*prot*)[¶](#tts.lib.ethernet.PacketIke.PacketIke.SetIpProt "Link to this definition")  
Parameters:  **prot** (*int*) – protocol type

SetIpSrc(*addr*)[¶](#tts.lib.ethernet.PacketIke.PacketIke.SetIpSrc "Link to this definition")  
Parameters:  **addr** (*str*) – source IP address e.g. 127.0.0.1

SetIpTos(*tos*)[¶](#tts.lib.ethernet.PacketIke.PacketIke.SetIpTos "Link to this definition")  
Parameters:  **tos** (*int*) – type of service

SetIpTtl(*ttl*)[¶](#tts.lib.ethernet.PacketIke.PacketIke.SetIpTtl "Link to this definition")  
Parameters:  **ttl** (*int*) – TTL

SetIpVersionAndHeaderLength(*versionHeader*)[¶](#tts.lib.ethernet.PacketIke.PacketIke.SetIpVersionAndHeaderLength "Link to this definition")  
Parameters:  **versionHeader** (*int*) – protocol version and header length

SetTimestamp(*timestamp*)[¶](#tts.lib.ethernet.PacketIke.PacketIke.SetTimestamp "Link to this definition")  
Parameters:  **timestamp** (*float* *|* *None*) – Receive timestamp in sec., None if not available

SetUdpChecksum(*checksum*)[¶](#tts.lib.ethernet.PacketIke.PacketIke.SetUdpChecksum "Link to this definition")  
Parameters:  **checksum** (*int*) – checksum

SetUdpDst(*port*)[¶](#tts.lib.ethernet.PacketIke.PacketIke.SetUdpDst "Link to this definition")  
Parameters:  **port** (*int*) – destination port

SetUdpLen(*length*)[¶](#tts.lib.ethernet.PacketIke.PacketIke.SetUdpLen "Link to this definition")  
Parameters:  **length** (*int*) – length of the UDP segment

SetUdpPayload(*payload*)[¶](#tts.lib.ethernet.PacketIke.PacketIke.SetUdpPayload "Link to this definition")  
Parameters:  **payload** (*bytes*) – UDP payload

SetUdpSrc(*port*)[¶](#tts.lib.ethernet.PacketIke.PacketIke.SetUdpSrc "Link to this definition")  
Parameters:  **port** (*int*) – source port

SetVlanCfi(*cfi*)[¶](#tts.lib.ethernet.PacketIke.PacketIke.SetVlanCfi "Link to this definition")  
Parameters:  **cfi** (*int*) – 802.1a canonical format indicator

SetVlanCfiOuter(*cfi*)[¶](#tts.lib.ethernet.PacketIke.PacketIke.SetVlanCfiOuter "Link to this definition")  
Parameters:  **cfi** (*int*) – 802.1ad canonical format indicator

SetVlanPcp(*pcp*)[¶](#tts.lib.ethernet.PacketIke.PacketIke.SetVlanPcp "Link to this definition")  
Parameters:  **pcp** (*int*) – 802.1a priority code point

SetVlanPcpOuter(*pcp*)[¶](#tts.lib.ethernet.PacketIke.PacketIke.SetVlanPcpOuter "Link to this definition")  
Parameters:  **pcp** (*int*) – 802.1ad priority code point

SetVlanVid(*vid*)[¶](#tts.lib.ethernet.PacketIke.PacketIke.SetVlanVid "Link to this definition")  
Parameters:  **vid** (*int*) – 802.1a VLAN id

SetVlanVidOuter(*vid*)[¶](#tts.lib.ethernet.PacketIke.PacketIke.SetVlanVidOuter "Link to this definition")  
Parameters:  **vid** (*int*) – 802.1ad VLAN id

ethDstMac[¶](#tts.lib.ethernet.PacketIke.PacketIke.ethDstMac "Link to this definition")  
target MAC address e.g. DE:AD:BE:EF:FF:00

Type:  str

ethPayload[¶](#tts.lib.ethernet.PacketIke.PacketIke.ethPayload "Link to this definition")  
Ethernet payload

Type:  bytes

ethSrcMac[¶](#tts.lib.ethernet.PacketIke.PacketIke.ethSrcMac "Link to this definition")  
source MAC address e.g. DE:AD:BE:EF:FF:00

Type:  str

ethType[¶](#tts.lib.ethernet.PacketIke.PacketIke.ethType "Link to this definition")  
ethernet protocol type

Type:  int

ipAhIcv[¶](#tts.lib.ethernet.PacketIke.PacketIke.ipAhIcv "Link to this definition")  
Integrity check value of IP authentication header (see RFC 4302)

Type:  bytes

ipAhLen[¶](#tts.lib.ethernet.PacketIke.PacketIke.ipAhLen "Link to this definition")  
Length value of IP authentication header (see RFC 4302) =\> len(ICV)/4+1

Type:  int

ipAhNxt[¶](#tts.lib.ethernet.PacketIke.PacketIke.ipAhNxt "Link to this definition")  
Next header value of IP authentication header (see RFC 4302)

Type:  int

ipAhRsvd[¶](#tts.lib.ethernet.PacketIke.PacketIke.ipAhRsvd "Link to this definition")  
Reserved value of IP authentication header (see RFC 4302)

Type:  int

ipAhSeq[¶](#tts.lib.ethernet.PacketIke.PacketIke.ipAhSeq "Link to this definition")  
Sequence number field of IP authentication header (see RFC 4302)

Type:  int

ipAhSpi[¶](#tts.lib.ethernet.PacketIke.PacketIke.ipAhSpi "Link to this definition")  
Security parameters index of IP authentication header (see RFC 4302)

Type:  int

ipChecksum[¶](#tts.lib.ethernet.PacketIke.PacketIke.ipChecksum "Link to this definition")  
checksum

Type:  int

ipDst[¶](#tts.lib.ethernet.PacketIke.PacketIke.ipDst "Link to this definition")  
target IP address e.g. 127.0.0.1

Type:  str

ipIdent[¶](#tts.lib.ethernet.PacketIke.PacketIke.ipIdent "Link to this definition")  
identifier

Type:  int

ipLen[¶](#tts.lib.ethernet.PacketIke.PacketIke.ipLen "Link to this definition")  
packet length

Type:  int

ipOffset[¶](#tts.lib.ethernet.PacketIke.PacketIke.ipOffset "Link to this definition")  
flags and offset combined

Type:  int

ipPayload[¶](#tts.lib.ethernet.PacketIke.PacketIke.ipPayload "Link to this definition")  
IP payload

Type:  bytes

ipProt[¶](#tts.lib.ethernet.PacketIke.PacketIke.ipProt "Link to this definition")  
protocol type / next header field

Type:  int

ipSrc[¶](#tts.lib.ethernet.PacketIke.PacketIke.ipSrc "Link to this definition")  
source IP address e.g. 127.0.0.1

Type:  str

ipTos[¶](#tts.lib.ethernet.PacketIke.PacketIke.ipTos "Link to this definition")  
type of service

Type:  int

ipTtl[¶](#tts.lib.ethernet.PacketIke.PacketIke.ipTtl "Link to this definition")  
TTL

Type:  int

ipVersionHeader[¶](#tts.lib.ethernet.PacketIke.PacketIke.ipVersionHeader "Link to this definition")  
protocol version and header length

Type:  int

macSecAn[¶](#tts.lib.ethernet.PacketIke.PacketIke.macSecAn "Link to this definition")  
Association Number of MACsec header (see IEEE 802.1AE)

Type:  int

macSecIcv[¶](#tts.lib.ethernet.PacketIke.PacketIke.macSecIcv "Link to this definition")  
Integrity check value of MACsec header (see IEEE 802.1AE)

Type:  bytes

macSecPn[¶](#tts.lib.ethernet.PacketIke.PacketIke.macSecPn "Link to this definition")  
Packet Number of MACsec header (see IEEE 802.1AE)

Type:  int

macSecSci[¶](#tts.lib.ethernet.PacketIke.PacketIke.macSecSci "Link to this definition")  
Secure Channel Identifier of MACsec header (see IEEE 802.1AE)

Type:  bytes

macSecSl[¶](#tts.lib.ethernet.PacketIke.PacketIke.macSecSl "Link to this definition")  
Short Length of MACsec header (see IEEE 802.1AE)

Type:  int

macSecTci[¶](#tts.lib.ethernet.PacketIke.PacketIke.macSecTci "Link to this definition")  
TAG Control Information of MACsec header (see IEEE 802.1AE)

Type:  int

macSecTciAn[¶](#tts.lib.ethernet.PacketIke.PacketIke.macSecTciAn "Link to this definition")  
TCI_AN byte of MACsec header (see IEEE 802.1AE)

Type:  int

macSecTciC[¶](#tts.lib.ethernet.PacketIke.PacketIke.macSecTciC "Link to this definition")  
Changed text bit in TCI of MACsec header (see IEEE 802.1AE)

Type:  bool

macSecTciE[¶](#tts.lib.ethernet.PacketIke.PacketIke.macSecTciE "Link to this definition")  
Encryption bit in TCI of MACsec header (see IEEE 802.1AE)

Type:  bool

macSecTciEs[¶](#tts.lib.ethernet.PacketIke.PacketIke.macSecTciEs "Link to this definition")  
End station bit in TCI of MACsec header (see IEEE 802.1AE)

Type:  bool

macSecTciSc[¶](#tts.lib.ethernet.PacketIke.PacketIke.macSecTciSc "Link to this definition")  
SCI indication bit in TCI of MACsec header (see IEEE 802.1AE)

Type:  bool

macSecTciScb[¶](#tts.lib.ethernet.PacketIke.PacketIke.macSecTciScb "Link to this definition")  
Single copy broadcast capability bit in TCI of MACsec header (see IEEE 802.1AE)

Type:  bool

macSecTciV[¶](#tts.lib.ethernet.PacketIke.PacketIke.macSecTciV "Link to this definition")  
Version bit in TCI of MACsec header (see IEEE 802.1AE)

Type:  bool

parent[¶](#tts.lib.ethernet.PacketIke.PacketIke.parent "Link to this definition")  
*Only for pseudo signals in trace analysis!* Returns the parent protocol object if there is one present, otherwise None.

Return type:  [EthernetProtocolBase](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase") | None

timestamp[¶](#tts.lib.ethernet.PacketIke.PacketIke.timestamp "Link to this definition")  
Receive timestamp in sec., None if not available

Type:  Optional[float]

udpChecksum[¶](#tts.lib.ethernet.PacketIke.PacketIke.udpChecksum "Link to this definition")  
checksum

Type:  int

udpDst[¶](#tts.lib.ethernet.PacketIke.PacketIke.udpDst "Link to this definition")  
destination port

Type:  int

udpLen[¶](#tts.lib.ethernet.PacketIke.PacketIke.udpLen "Link to this definition")  
length of the UDP segment

Type:  int

udpPayload[¶](#tts.lib.ethernet.PacketIke.PacketIke.udpPayload "Link to this definition")  
UDP payload

Type:  bytes

udpSrc[¶](#tts.lib.ethernet.PacketIke.PacketIke.udpSrc "Link to this definition")  
source port

Type:  int

vlanCfi[¶](#tts.lib.ethernet.PacketIke.PacketIke.vlanCfi "Link to this definition")  
802.1a canonical format indicator

Type:  int

vlanCfiOuter[¶](#tts.lib.ethernet.PacketIke.PacketIke.vlanCfiOuter "Link to this definition")  
802.1ad canonical format indicator

Type:  int

vlanPcp[¶](#tts.lib.ethernet.PacketIke.PacketIke.vlanPcp "Link to this definition")  
802.1a priority code point

Type:  int

vlanPcpOuter[¶](#tts.lib.ethernet.PacketIke.PacketIke.vlanPcpOuter "Link to this definition")  
802.1ad priority code point

Type:  int

vlanVid[¶](#tts.lib.ethernet.PacketIke.PacketIke.vlanVid "Link to this definition")  
802.1a VLAN id

Type:  int

vlanVidOuter[¶](#tts.lib.ethernet.PacketIke.PacketIke.vlanVidOuter "Link to this definition")  
802.1ad VLAN id

Type:  int

deleteSpis[¶](#tts.lib.ethernet.PacketIke.PacketIke.deleteSpis "Link to this definition")  
SPI list of Delete payload, or None if there is no Delete payload

Type:  Optional[list[int]]

GetDeleteNumOfSpis()[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetDeleteNumOfSpis "Link to this definition")  
Returns:  Number of SPIs in the Delete payload, or None if there is no Delete payload

Return type:  int | None

deleteNumOfSpis[¶](#tts.lib.ethernet.PacketIke.PacketIke.deleteNumOfSpis "Link to this definition")  
Number of SPIs in the Delete payload, or None if there is no Delete payload

Type:  Optional[int]

### PacketTcp[¶](#packettcp "Link to this heading")

*class* PacketTcp[¶](#tts.lib.ethernet.PacketTcp.PacketTcp "Link to this definition")  
In the test case, use `api.Ethernet.PacketTcp`; in UserPyModules, use `from tts.lib.ethernet.PacketTcp import PacketTcp`.

\<protocol\>  
Equivalent to method [`FindParent(protocol)`](#tts.lib.ethernet.PacketTcp.PacketTcp.FindParent "tts.lib.ethernet.PacketTcp.PacketTcp.FindParent"). Direct access to parent protocols. *protocol* is one of [`OsiProtocol`](#tts.lib.ethernet.PacketEthernet.OsiProtocol "tts.lib.ethernet.PacketEthernet.OsiProtocol").

Example: Signal.eth.src provides the source MAC address of the Ethernet protocol layer.

Type:  [`EthernetProtocolBase`](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase")

GetTcpLen()[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.GetTcpLen "Link to this definition")  
Returns:  length of the whole TCP segment including header length

Return type:  int

GetTcpSrc()[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.GetTcpSrc "Link to this definition")  
Returns:  source port

Return type:  int

SetTcpSrc(*port*)[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.SetTcpSrc "Link to this definition")  
Parameters:  **port** (*int*) – source port

tcpSrc[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.tcpSrc "Link to this definition")  
source port

Type:  int

GetTcpDst()[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.GetTcpDst "Link to this definition")  
Returns:  destination port

Return type:  int

SetTcpDst(*port*)[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.SetTcpDst "Link to this definition")  
Parameters:  **port** (*int*) – destination port

tcpDst[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.tcpDst "Link to this definition")  
destination port

Type:  int

GetTcpSeq()[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.GetTcpSeq "Link to this definition")  
Returns:  sequence number

Return type:  int

SetTcpSeq(*seq*)[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.SetTcpSeq "Link to this definition")  
Parameters:  **seq** – sequence number

Type:  int

tcpSeq[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.tcpSeq "Link to this definition")  
sequence number

Type:  int

GetTcpAck()[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.GetTcpAck "Link to this definition")  
Returns:  Ack number

Return type:  int

SetTcpAck(*ack*)[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.SetTcpAck "Link to this definition")  
Parameters:  **ack** – Ack number

Type:  int

tcpAck[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.tcpAck "Link to this definition")  
Ack number

Type:  int

GetTcpOffset()[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.GetTcpOffset "Link to this definition")  
Returns:  TCP offset

Return type:  int

SetTcpOffset(*offset*)[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.SetTcpOffset "Link to this definition")  
Param:  
TCP offset

Type:  int

tcpOffset[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.tcpOffset "Link to this definition")  
TCP offset

Type:  int

GetTcpFlags()[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.GetTcpFlags "Link to this definition")  
Returns:  flags

Return type:  int

SetTcpFlags(*flags*)[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.SetTcpFlags "Link to this definition")  
Parameters:  **flags** – flags

Type:  int

tcpFlags[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.tcpFlags "Link to this definition")  
flags

Type:  int

GetTcpWindow()[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.GetTcpWindow "Link to this definition")  
Returns:  window

Return type:  int

SetTcpWindow(*win*)[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.SetTcpWindow "Link to this definition")  
Param:  
window

Type:  int

tcpWindow[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.tcpWindow "Link to this definition")  
window

Type:  int

GetTcpChecksum()[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.GetTcpChecksum "Link to this definition")  
Returns:  checksum

Return type:  int

SetTcpChecksum(*checksum*)[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.SetTcpChecksum "Link to this definition")  
Parameters:  **checksum** (*int*) – checksum

tcpChecksum[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.tcpChecksum "Link to this definition")  
checksum

Type:  int

GetTcpUrgent()[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.GetTcpUrgent "Link to this definition")  
Returns:  urgent pointer

Return type:  int

SetTcpUrgent(*urgent*)[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.SetTcpUrgent "Link to this definition")  
Parameters:  **urgent** (*int*) – urgent pointer

tcpUrgent[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.tcpUrgent "Link to this definition")  
urgent pointer

Type:  int

GetTcpPayload()[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.GetTcpPayload "Link to this definition")  
Returns:  TCP payload

Return type:  bytes

SetTcpPayload(*payload*)[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.SetTcpPayload "Link to this definition")  
Parameters:  **payload** (*bytes*) – TCP payload

tcpPayload[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.tcpPayload "Link to this definition")  
TCP payload

Type:  bytes

GetTcpOptions()[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.GetTcpOptions "Link to this definition")  
Returns:  the option list - a list with tuples (option, data)

Return type:  list[tuple]

tcpOptions[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.tcpOptions "Link to this definition")  
the option list - a list with tuples (option, data)

Type:  list[tuple]

CalcIpLen()[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.CalcIpLen "Link to this definition")  
Calculate and set the current length of this IP packet

FindParent(*protocol*)[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.FindParent "Link to this definition")  
*Only for pseudo signals in trace analysis!* Returns the requested protocol object if present, otherwise a [`NoProtocol`](#tts.lib.ethernet.PacketEthernet.NoProtocol "tts.lib.ethernet.PacketEthernet.NoProtocol") object.

Parameters:  **protocol** ([*OsiProtocol*](#tts.lib.ethernet.PacketEthernet.OsiProtocol "tts.lib.ethernet.PacketEthernet.OsiProtocol")) – The required protocol name.

Returns:  The required parent protocol object.

Return type:  [EthernetProtocolBase](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase")

GetEthDstMac()[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.GetEthDstMac "Link to this definition")  
Returns:  target MAC address e.g. DE:AD:BE:EF:FF:00

Return type:  str

GetEthPayload()[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.GetEthPayload "Link to this definition")  
Returns:  Ethernet payload

Return type:  bytes

GetEthSrcMac()[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.GetEthSrcMac "Link to this definition")  
Returns:  source MAC address e.g. DE:AD:BE:EF:FF:00

Return type:  str

GetEthType()[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.GetEthType "Link to this definition")  
Returns:  ethernet protocol type

Return type:  int

GetIpAhIcv()[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.GetIpAhIcv "Link to this definition")  
Returns:  Integrity check value of IP authentication header (see RFC 4302)

Return type:  bytes

GetIpAhLen()[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.GetIpAhLen "Link to this definition")  
Returns:  Length value of IP authentication header (see RFC 4302) =\> len(ICV)/4+1

Return type:  int

GetIpAhNxt()[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.GetIpAhNxt "Link to this definition")  
Returns:  Next header value of IP authentication header (see RFC 4302)

Return type:  int

GetIpAhRsvd()[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.GetIpAhRsvd "Link to this definition")  
Returns:  Reserved value of IP authentication header (see RFC 4302)

Return type:  int

GetIpAhSeq()[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.GetIpAhSeq "Link to this definition")  
Returns:  Sequence number field of IP authentication header (see RFC 4302)

Return type:  int

GetIpAhSpi()[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.GetIpAhSpi "Link to this definition")  
Returns:  Security parameters index of IP authentication header (see RFC 4302)

Return type:  int

GetIpChecksum()[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.GetIpChecksum "Link to this definition")  
Returns:  checksum

Return type:  int

GetIpDst()[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.GetIpDst "Link to this definition")  
Returns:  target IP address e.g. 127.0.0.1

Return type:  str

GetIpIdent()[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.GetIpIdent "Link to this definition")  
Returns:  identifier

Return type:  int

GetIpLen()[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.GetIpLen "Link to this definition")  
Returns:  packet length

Return type:  int

GetIpOffset()[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.GetIpOffset "Link to this definition")  
Returns:  flags and offset combined

Return type:  int

GetIpPayload()[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.GetIpPayload "Link to this definition")  
Returns:  IP payload

Return type:  bytes

GetIpProt()[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.GetIpProt "Link to this definition")  
Returns:  protocol type / next header field

Return type:  int

GetIpSrc()[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.GetIpSrc "Link to this definition")  
Returns:  source IP address e.g. 127.0.0.1

Return type:  str

GetIpTos()[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.GetIpTos "Link to this definition")  
Returns:  type of service

Return type:  int

GetIpTtl()[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.GetIpTtl "Link to this definition")  
Returns:  TTL

Return type:  int

GetIpVersionAndHeaderLength()[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.GetIpVersionAndHeaderLength "Link to this definition")  
Returns:  protocol version and header length

Return type:  int

GetMacSecAn()[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.GetMacSecAn "Link to this definition")  
Returns:  Association Number of MACsec header (see IEEE 802.1AE)

Return type:  int

GetMacSecIcv()[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.GetMacSecIcv "Link to this definition")  
Returns:  Integrity check value of MACsec header (see IEEE 802.1AE)

Return type:  bytes

GetMacSecPn()[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.GetMacSecPn "Link to this definition")  
Returns:  Packet Number of MACsec header (see IEEE 802.1AE)

Return type:  int

GetMacSecSci()[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.GetMacSecSci "Link to this definition")  
Returns:  Secure Channel Identifier of MACsec header (see IEEE 802.1AE)

Return type:  bytes

GetMacSecSl()[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.GetMacSecSl "Link to this definition")  
Returns:  Short Length of MACsec header (see IEEE 802.1AE)

Return type:  int

GetMacSecTci()[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.GetMacSecTci "Link to this definition")  
Returns:  TAG Control Information of MACsec header (see IEEE 802.1AE)

Return type:  int

GetMacSecTciAn()[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.GetMacSecTciAn "Link to this definition")  
Returns:  TCI_AN byte of MACsec header (see IEEE 802.1AE)

Return type:  int

GetMacSecTciC()[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.GetMacSecTciC "Link to this definition")  
Returns:  Changed text bit in TCI of MACsec header (see IEEE 802.1AE)

Return type:  bool

GetMacSecTciE()[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.GetMacSecTciE "Link to this definition")  
Returns:  Encryption bit in TCI of MACsec header (see IEEE 802.1AE)

Return type:  bool

GetMacSecTciEs()[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.GetMacSecTciEs "Link to this definition")  
Returns:  End station bit in TCI of MACsec header (see IEEE 802.1AE)

Return type:  bool

GetMacSecTciSc()[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.GetMacSecTciSc "Link to this definition")  
Returns:  SCI indication bit in TCI of MACsec header (see IEEE 802.1AE)

Return type:  bool

GetMacSecTciScb()[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.GetMacSecTciScb "Link to this definition")  
Returns:  Single copy broadcast capability bit in TCI of MACsec header (see IEEE 802.1AE)

Return type:  bool

GetMacSecTciV()[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.GetMacSecTciV "Link to this definition")  
Returns:  Version bit in TCI of MACsec header (see IEEE 802.1AE)

Return type:  bool

GetTimestamp()[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.GetTimestamp "Link to this definition")  
Returns:  Receive timestamp in sec., None if not available

Return type:  float | None

GetVlanCfi(*ixVlanTags*)[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.GetVlanCfi "Link to this definition")  
Returns:  802.1a canonical format indicator

Return type:  int

GetVlanCfiOuter(*ixVlanTags*)[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.GetVlanCfiOuter "Link to this definition")  
Returns:  802.1ad canonical format indicator

Return type:  int

GetVlanPcp(*ixVlanTags*)[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.GetVlanPcp "Link to this definition")  
Returns:  802.1a priority code point

Return type:  int

GetVlanPcpOuter(*ixVlanTags*)[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.GetVlanPcpOuter "Link to this definition")  
Returns:  802.1ad priority code point

Return type:  int

GetVlanVid(*ixVlanTags*)[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.GetVlanVid "Link to this definition")  
Returns:  802.1a VLAN id

Return type:  int

GetVlanVidOuter(*ixVlanTags*)[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.GetVlanVidOuter "Link to this definition")  
Returns:  802.1ad VLAN id

Return type:  int

PK_CLASS[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.PK_CLASS "Link to this definition")  
alias of `IP`

SetEthDstMac(*mac*)[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.SetEthDstMac "Link to this definition")  
Parameters:  **mac** (*str*) – target MAC address e.g. DE:AD:BE:EF:FF:00

SetEthPayload(*payload*)[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.SetEthPayload "Link to this definition")  
Parameters:  **payload** (*bytes*) – Ethernet payload

SetEthSrcMac(*mac*)[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.SetEthSrcMac "Link to this definition")  
Parameters:  **mac** (*str*) – source MAC addres e.g. DE:AD:BE:EF:FF:00

SetEthType(*ethType*)[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.SetEthType "Link to this definition")  
Parameters:  **ethType** (*int*) – ethernet protocol type

SetIpChecksum(*checksum*)[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.SetIpChecksum "Link to this definition")  
Parameters:  **checksum** (*int*) – checksum

SetIpDst(*addr*)[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.SetIpDst "Link to this definition")  
Parameters:  **addr** (*str*) – target IP address e.g. 127.0.0.1

SetIpIdent(*ident*)[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.SetIpIdent "Link to this definition")  
Parameters:  **ident** (*int*) – identifier

SetIpLen(*length*)[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.SetIpLen "Link to this definition")  
Parameters:  **length** (*int*) – packet length

SetIpOffset(*offset*)[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.SetIpOffset "Link to this definition")  
Parameters:  **offset** (*int*) – flags and offset combined

SetIpPayload(*payload*)[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.SetIpPayload "Link to this definition")  
Parameters:  **payload** (*bytes*) – IP payload

SetIpProt(*prot*)[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.SetIpProt "Link to this definition")  
Parameters:  **prot** (*int*) – protocol type

SetIpSrc(*addr*)[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.SetIpSrc "Link to this definition")  
Parameters:  **addr** (*str*) – source IP address e.g. 127.0.0.1

SetIpTos(*tos*)[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.SetIpTos "Link to this definition")  
Parameters:  **tos** (*int*) – type of service

SetIpTtl(*ttl*)[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.SetIpTtl "Link to this definition")  
Parameters:  **ttl** (*int*) – TTL

SetIpVersionAndHeaderLength(*versionHeader*)[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.SetIpVersionAndHeaderLength "Link to this definition")  
Parameters:  **versionHeader** (*int*) – protocol version and header length

SetTimestamp(*timestamp*)[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.SetTimestamp "Link to this definition")  
Parameters:  **timestamp** (*float* *|* *None*) – Receive timestamp in sec., None if not available

SetVlanCfi(*cfi*)[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.SetVlanCfi "Link to this definition")  
Parameters:  **cfi** (*int*) – 802.1a canonical format indicator

SetVlanCfiOuter(*cfi*)[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.SetVlanCfiOuter "Link to this definition")  
Parameters:  **cfi** (*int*) – 802.1ad canonical format indicator

SetVlanPcp(*pcp*)[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.SetVlanPcp "Link to this definition")  
Parameters:  **pcp** (*int*) – 802.1a priority code point

SetVlanPcpOuter(*pcp*)[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.SetVlanPcpOuter "Link to this definition")  
Parameters:  **pcp** (*int*) – 802.1ad priority code point

SetVlanVid(*vid*)[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.SetVlanVid "Link to this definition")  
Parameters:  **vid** (*int*) – 802.1a VLAN id

SetVlanVidOuter(*vid*)[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.SetVlanVidOuter "Link to this definition")  
Parameters:  **vid** (*int*) – 802.1ad VLAN id

ethDstMac[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.ethDstMac "Link to this definition")  
target MAC address e.g. DE:AD:BE:EF:FF:00

Type:  str

ethPayload[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.ethPayload "Link to this definition")  
Ethernet payload

Type:  bytes

ethSrcMac[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.ethSrcMac "Link to this definition")  
source MAC address e.g. DE:AD:BE:EF:FF:00

Type:  str

ethType[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.ethType "Link to this definition")  
ethernet protocol type

Type:  int

ipAhIcv[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.ipAhIcv "Link to this definition")  
Integrity check value of IP authentication header (see RFC 4302)

Type:  bytes

ipAhLen[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.ipAhLen "Link to this definition")  
Length value of IP authentication header (see RFC 4302) =\> len(ICV)/4+1

Type:  int

ipAhNxt[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.ipAhNxt "Link to this definition")  
Next header value of IP authentication header (see RFC 4302)

Type:  int

ipAhRsvd[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.ipAhRsvd "Link to this definition")  
Reserved value of IP authentication header (see RFC 4302)

Type:  int

ipAhSeq[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.ipAhSeq "Link to this definition")  
Sequence number field of IP authentication header (see RFC 4302)

Type:  int

ipAhSpi[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.ipAhSpi "Link to this definition")  
Security parameters index of IP authentication header (see RFC 4302)

Type:  int

ipChecksum[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.ipChecksum "Link to this definition")  
checksum

Type:  int

ipDst[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.ipDst "Link to this definition")  
target IP address e.g. 127.0.0.1

Type:  str

ipIdent[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.ipIdent "Link to this definition")  
identifier

Type:  int

ipLen[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.ipLen "Link to this definition")  
packet length

Type:  int

ipOffset[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.ipOffset "Link to this definition")  
flags and offset combined

Type:  int

ipPayload[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.ipPayload "Link to this definition")  
IP payload

Type:  bytes

ipProt[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.ipProt "Link to this definition")  
protocol type / next header field

Type:  int

ipSrc[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.ipSrc "Link to this definition")  
source IP address e.g. 127.0.0.1

Type:  str

ipTos[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.ipTos "Link to this definition")  
type of service

Type:  int

ipTtl[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.ipTtl "Link to this definition")  
TTL

Type:  int

ipVersionHeader[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.ipVersionHeader "Link to this definition")  
protocol version and header length

Type:  int

macSecAn[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.macSecAn "Link to this definition")  
Association Number of MACsec header (see IEEE 802.1AE)

Type:  int

macSecIcv[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.macSecIcv "Link to this definition")  
Integrity check value of MACsec header (see IEEE 802.1AE)

Type:  bytes

macSecPn[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.macSecPn "Link to this definition")  
Packet Number of MACsec header (see IEEE 802.1AE)

Type:  int

macSecSci[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.macSecSci "Link to this definition")  
Secure Channel Identifier of MACsec header (see IEEE 802.1AE)

Type:  bytes

macSecSl[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.macSecSl "Link to this definition")  
Short Length of MACsec header (see IEEE 802.1AE)

Type:  int

macSecTci[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.macSecTci "Link to this definition")  
TAG Control Information of MACsec header (see IEEE 802.1AE)

Type:  int

macSecTciAn[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.macSecTciAn "Link to this definition")  
TCI_AN byte of MACsec header (see IEEE 802.1AE)

Type:  int

macSecTciC[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.macSecTciC "Link to this definition")  
Changed text bit in TCI of MACsec header (see IEEE 802.1AE)

Type:  bool

macSecTciE[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.macSecTciE "Link to this definition")  
Encryption bit in TCI of MACsec header (see IEEE 802.1AE)

Type:  bool

macSecTciEs[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.macSecTciEs "Link to this definition")  
End station bit in TCI of MACsec header (see IEEE 802.1AE)

Type:  bool

macSecTciSc[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.macSecTciSc "Link to this definition")  
SCI indication bit in TCI of MACsec header (see IEEE 802.1AE)

Type:  bool

macSecTciScb[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.macSecTciScb "Link to this definition")  
Single copy broadcast capability bit in TCI of MACsec header (see IEEE 802.1AE)

Type:  bool

macSecTciV[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.macSecTciV "Link to this definition")  
Version bit in TCI of MACsec header (see IEEE 802.1AE)

Type:  bool

parent[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.parent "Link to this definition")  
*Only for pseudo signals in trace analysis!* Returns the parent protocol object if there is one present, otherwise None.

Return type:  [EthernetProtocolBase](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase") | None

timestamp[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.timestamp "Link to this definition")  
Receive timestamp in sec., None if not available

Type:  Optional[float]

vlanCfi[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.vlanCfi "Link to this definition")  
802.1a canonical format indicator

Type:  int

vlanCfiOuter[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.vlanCfiOuter "Link to this definition")  
802.1ad canonical format indicator

Type:  int

vlanPcp[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.vlanPcp "Link to this definition")  
802.1a priority code point

Type:  int

vlanPcpOuter[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.vlanPcpOuter "Link to this definition")  
802.1ad priority code point

Type:  int

vlanVid[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.vlanVid "Link to this definition")  
802.1a VLAN id

Type:  int

vlanVidOuter[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.vlanVidOuter "Link to this definition")  
802.1ad VLAN id

Type:  int

### PacketUdp[¶](#packetudp "Link to this heading")

*class* PacketUdp[¶](#tts.lib.ethernet.PacketUdp.PacketUdp "Link to this definition")  
In the test case, use `api.Ethernet.PacketUdp`; in UserPyModules, use `from tts.lib.ethernet.PacketUdp import PacketUdp`.

\<protocol\>  
Equivalent to method [`FindParent(protocol)`](#tts.lib.ethernet.PacketUdp.PacketUdp.FindParent "tts.lib.ethernet.PacketUdp.PacketUdp.FindParent"). Direct access to parent protocols. *protocol* is one of [`OsiProtocol`](#tts.lib.ethernet.PacketEthernet.OsiProtocol "tts.lib.ethernet.PacketEthernet.OsiProtocol").

Example: Signal.eth.src provides the source MAC address of the Ethernet protocol layer.

Type:  [`EthernetProtocolBase`](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase")

CalcUdpLen()[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.CalcUdpLen "Link to this definition")  
Calculate and set the current length of this segment

GetUdpSrc()[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.GetUdpSrc "Link to this definition")  
Returns:  source port

Return type:  int

SetUdpSrc(*port*)[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.SetUdpSrc "Link to this definition")  
Parameters:  **port** (*int*) – source port

udpSrc[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.udpSrc "Link to this definition")  
source port

Type:  int

GetUdpDst()[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.GetUdpDst "Link to this definition")  
Returns:  destination port

Return type:  int

SetUdpDst(*port*)[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.SetUdpDst "Link to this definition")  
Parameters:  **port** (*int*) – destination port

udpDst[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.udpDst "Link to this definition")  
destination port

Type:  int

GetUdpLen()[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.GetUdpLen "Link to this definition")  
Returns:  length of the UDP segment

Return type:  int

SetUdpLen(*length*)[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.SetUdpLen "Link to this definition")  
Parameters:  **length** (*int*) – length of the UDP segment

udpLen[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.udpLen "Link to this definition")  
length of the UDP segment

Type:  int

GetUdpChecksum()[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.GetUdpChecksum "Link to this definition")  
Returns:  checksum

Return type:  int

SetUdpChecksum(*checksum*)[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.SetUdpChecksum "Link to this definition")  
Parameters:  **checksum** (*int*) – checksum

udpChecksum[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.udpChecksum "Link to this definition")  
checksum

Type:  int

GetUdpPayload()[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.GetUdpPayload "Link to this definition")  
Returns:  UDP payload

Return type:  bytes

SetUdpPayload(*payload*)[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.SetUdpPayload "Link to this definition")  
Parameters:  **payload** (*bytes*) – UDP payload

udpPayload[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.udpPayload "Link to this definition")  
UDP payload

Type:  bytes

CalcIpLen()[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.CalcIpLen "Link to this definition")  
Calculate and set the current length of this IP packet

FindParent(*protocol*)[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.FindParent "Link to this definition")  
*Only for pseudo signals in trace analysis!* Returns the requested protocol object if present, otherwise a [`NoProtocol`](#tts.lib.ethernet.PacketEthernet.NoProtocol "tts.lib.ethernet.PacketEthernet.NoProtocol") object.

Parameters:  **protocol** ([*OsiProtocol*](#tts.lib.ethernet.PacketEthernet.OsiProtocol "tts.lib.ethernet.PacketEthernet.OsiProtocol")) – The required protocol name.

Returns:  The required parent protocol object.

Return type:  [EthernetProtocolBase](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase")

GetEthDstMac()[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.GetEthDstMac "Link to this definition")  
Returns:  target MAC address e.g. DE:AD:BE:EF:FF:00

Return type:  str

GetEthPayload()[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.GetEthPayload "Link to this definition")  
Returns:  Ethernet payload

Return type:  bytes

GetEthSrcMac()[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.GetEthSrcMac "Link to this definition")  
Returns:  source MAC address e.g. DE:AD:BE:EF:FF:00

Return type:  str

GetEthType()[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.GetEthType "Link to this definition")  
Returns:  ethernet protocol type

Return type:  int

GetIpAhIcv()[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.GetIpAhIcv "Link to this definition")  
Returns:  Integrity check value of IP authentication header (see RFC 4302)

Return type:  bytes

GetIpAhLen()[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.GetIpAhLen "Link to this definition")  
Returns:  Length value of IP authentication header (see RFC 4302) =\> len(ICV)/4+1

Return type:  int

GetIpAhNxt()[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.GetIpAhNxt "Link to this definition")  
Returns:  Next header value of IP authentication header (see RFC 4302)

Return type:  int

GetIpAhRsvd()[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.GetIpAhRsvd "Link to this definition")  
Returns:  Reserved value of IP authentication header (see RFC 4302)

Return type:  int

GetIpAhSeq()[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.GetIpAhSeq "Link to this definition")  
Returns:  Sequence number field of IP authentication header (see RFC 4302)

Return type:  int

GetIpAhSpi()[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.GetIpAhSpi "Link to this definition")  
Returns:  Security parameters index of IP authentication header (see RFC 4302)

Return type:  int

GetIpChecksum()[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.GetIpChecksum "Link to this definition")  
Returns:  checksum

Return type:  int

GetIpDst()[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.GetIpDst "Link to this definition")  
Returns:  target IP address e.g. 127.0.0.1

Return type:  str

GetIpIdent()[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.GetIpIdent "Link to this definition")  
Returns:  identifier

Return type:  int

GetIpLen()[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.GetIpLen "Link to this definition")  
Returns:  packet length

Return type:  int

GetIpOffset()[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.GetIpOffset "Link to this definition")  
Returns:  flags and offset combined

Return type:  int

GetIpPayload()[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.GetIpPayload "Link to this definition")  
Returns:  IP payload

Return type:  bytes

GetIpProt()[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.GetIpProt "Link to this definition")  
Returns:  protocol type / next header field

Return type:  int

GetIpSrc()[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.GetIpSrc "Link to this definition")  
Returns:  source IP address e.g. 127.0.0.1

Return type:  str

GetIpTos()[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.GetIpTos "Link to this definition")  
Returns:  type of service

Return type:  int

GetIpTtl()[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.GetIpTtl "Link to this definition")  
Returns:  TTL

Return type:  int

GetIpVersionAndHeaderLength()[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.GetIpVersionAndHeaderLength "Link to this definition")  
Returns:  protocol version and header length

Return type:  int

GetMacSecAn()[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.GetMacSecAn "Link to this definition")  
Returns:  Association Number of MACsec header (see IEEE 802.1AE)

Return type:  int

GetMacSecIcv()[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.GetMacSecIcv "Link to this definition")  
Returns:  Integrity check value of MACsec header (see IEEE 802.1AE)

Return type:  bytes

GetMacSecPn()[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.GetMacSecPn "Link to this definition")  
Returns:  Packet Number of MACsec header (see IEEE 802.1AE)

Return type:  int

GetMacSecSci()[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.GetMacSecSci "Link to this definition")  
Returns:  Secure Channel Identifier of MACsec header (see IEEE 802.1AE)

Return type:  bytes

GetMacSecSl()[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.GetMacSecSl "Link to this definition")  
Returns:  Short Length of MACsec header (see IEEE 802.1AE)

Return type:  int

GetMacSecTci()[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.GetMacSecTci "Link to this definition")  
Returns:  TAG Control Information of MACsec header (see IEEE 802.1AE)

Return type:  int

GetMacSecTciAn()[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.GetMacSecTciAn "Link to this definition")  
Returns:  TCI_AN byte of MACsec header (see IEEE 802.1AE)

Return type:  int

GetMacSecTciC()[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.GetMacSecTciC "Link to this definition")  
Returns:  Changed text bit in TCI of MACsec header (see IEEE 802.1AE)

Return type:  bool

GetMacSecTciE()[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.GetMacSecTciE "Link to this definition")  
Returns:  Encryption bit in TCI of MACsec header (see IEEE 802.1AE)

Return type:  bool

GetMacSecTciEs()[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.GetMacSecTciEs "Link to this definition")  
Returns:  End station bit in TCI of MACsec header (see IEEE 802.1AE)

Return type:  bool

GetMacSecTciSc()[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.GetMacSecTciSc "Link to this definition")  
Returns:  SCI indication bit in TCI of MACsec header (see IEEE 802.1AE)

Return type:  bool

GetMacSecTciScb()[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.GetMacSecTciScb "Link to this definition")  
Returns:  Single copy broadcast capability bit in TCI of MACsec header (see IEEE 802.1AE)

Return type:  bool

GetMacSecTciV()[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.GetMacSecTciV "Link to this definition")  
Returns:  Version bit in TCI of MACsec header (see IEEE 802.1AE)

Return type:  bool

GetTimestamp()[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.GetTimestamp "Link to this definition")  
Returns:  Receive timestamp in sec., None if not available

Return type:  float | None

GetVlanCfi(*ixVlanTags*)[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.GetVlanCfi "Link to this definition")  
Returns:  802.1a canonical format indicator

Return type:  int

GetVlanCfiOuter(*ixVlanTags*)[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.GetVlanCfiOuter "Link to this definition")  
Returns:  802.1ad canonical format indicator

Return type:  int

GetVlanPcp(*ixVlanTags*)[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.GetVlanPcp "Link to this definition")  
Returns:  802.1a priority code point

Return type:  int

GetVlanPcpOuter(*ixVlanTags*)[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.GetVlanPcpOuter "Link to this definition")  
Returns:  802.1ad priority code point

Return type:  int

GetVlanVid(*ixVlanTags*)[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.GetVlanVid "Link to this definition")  
Returns:  802.1a VLAN id

Return type:  int

GetVlanVidOuter(*ixVlanTags*)[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.GetVlanVidOuter "Link to this definition")  
Returns:  802.1ad VLAN id

Return type:  int

PK_CLASS[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.PK_CLASS "Link to this definition")  
alias of `IP`

SetEthDstMac(*mac*)[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.SetEthDstMac "Link to this definition")  
Parameters:  **mac** (*str*) – target MAC address e.g. DE:AD:BE:EF:FF:00

SetEthPayload(*payload*)[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.SetEthPayload "Link to this definition")  
Parameters:  **payload** (*bytes*) – Ethernet payload

SetEthSrcMac(*mac*)[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.SetEthSrcMac "Link to this definition")  
Parameters:  **mac** (*str*) – source MAC addres e.g. DE:AD:BE:EF:FF:00

SetEthType(*ethType*)[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.SetEthType "Link to this definition")  
Parameters:  **ethType** (*int*) – ethernet protocol type

SetIpChecksum(*checksum*)[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.SetIpChecksum "Link to this definition")  
Parameters:  **checksum** (*int*) – checksum

SetIpDst(*addr*)[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.SetIpDst "Link to this definition")  
Parameters:  **addr** (*str*) – target IP address e.g. 127.0.0.1

SetIpIdent(*ident*)[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.SetIpIdent "Link to this definition")  
Parameters:  **ident** (*int*) – identifier

SetIpLen(*length*)[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.SetIpLen "Link to this definition")  
Parameters:  **length** (*int*) – packet length

SetIpOffset(*offset*)[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.SetIpOffset "Link to this definition")  
Parameters:  **offset** (*int*) – flags and offset combined

SetIpPayload(*payload*)[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.SetIpPayload "Link to this definition")  
Parameters:  **payload** (*bytes*) – IP payload

SetIpProt(*prot*)[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.SetIpProt "Link to this definition")  
Parameters:  **prot** (*int*) – protocol type

SetIpSrc(*addr*)[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.SetIpSrc "Link to this definition")  
Parameters:  **addr** (*str*) – source IP address e.g. 127.0.0.1

SetIpTos(*tos*)[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.SetIpTos "Link to this definition")  
Parameters:  **tos** (*int*) – type of service

SetIpTtl(*ttl*)[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.SetIpTtl "Link to this definition")  
Parameters:  **ttl** (*int*) – TTL

SetIpVersionAndHeaderLength(*versionHeader*)[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.SetIpVersionAndHeaderLength "Link to this definition")  
Parameters:  **versionHeader** (*int*) – protocol version and header length

SetTimestamp(*timestamp*)[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.SetTimestamp "Link to this definition")  
Parameters:  **timestamp** (*float* *|* *None*) – Receive timestamp in sec., None if not available

SetVlanCfi(*cfi*)[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.SetVlanCfi "Link to this definition")  
Parameters:  **cfi** (*int*) – 802.1a canonical format indicator

SetVlanCfiOuter(*cfi*)[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.SetVlanCfiOuter "Link to this definition")  
Parameters:  **cfi** (*int*) – 802.1ad canonical format indicator

SetVlanPcp(*pcp*)[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.SetVlanPcp "Link to this definition")  
Parameters:  **pcp** (*int*) – 802.1a priority code point

SetVlanPcpOuter(*pcp*)[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.SetVlanPcpOuter "Link to this definition")  
Parameters:  **pcp** (*int*) – 802.1ad priority code point

SetVlanVid(*vid*)[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.SetVlanVid "Link to this definition")  
Parameters:  **vid** (*int*) – 802.1a VLAN id

SetVlanVidOuter(*vid*)[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.SetVlanVidOuter "Link to this definition")  
Parameters:  **vid** (*int*) – 802.1ad VLAN id

ethDstMac[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.ethDstMac "Link to this definition")  
target MAC address e.g. DE:AD:BE:EF:FF:00

Type:  str

ethPayload[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.ethPayload "Link to this definition")  
Ethernet payload

Type:  bytes

ethSrcMac[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.ethSrcMac "Link to this definition")  
source MAC address e.g. DE:AD:BE:EF:FF:00

Type:  str

ethType[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.ethType "Link to this definition")  
ethernet protocol type

Type:  int

ipAhIcv[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.ipAhIcv "Link to this definition")  
Integrity check value of IP authentication header (see RFC 4302)

Type:  bytes

ipAhLen[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.ipAhLen "Link to this definition")  
Length value of IP authentication header (see RFC 4302) =\> len(ICV)/4+1

Type:  int

ipAhNxt[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.ipAhNxt "Link to this definition")  
Next header value of IP authentication header (see RFC 4302)

Type:  int

ipAhRsvd[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.ipAhRsvd "Link to this definition")  
Reserved value of IP authentication header (see RFC 4302)

Type:  int

ipAhSeq[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.ipAhSeq "Link to this definition")  
Sequence number field of IP authentication header (see RFC 4302)

Type:  int

ipAhSpi[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.ipAhSpi "Link to this definition")  
Security parameters index of IP authentication header (see RFC 4302)

Type:  int

ipChecksum[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.ipChecksum "Link to this definition")  
checksum

Type:  int

ipDst[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.ipDst "Link to this definition")  
target IP address e.g. 127.0.0.1

Type:  str

ipIdent[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.ipIdent "Link to this definition")  
identifier

Type:  int

ipLen[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.ipLen "Link to this definition")  
packet length

Type:  int

ipOffset[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.ipOffset "Link to this definition")  
flags and offset combined

Type:  int

ipPayload[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.ipPayload "Link to this definition")  
IP payload

Type:  bytes

ipProt[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.ipProt "Link to this definition")  
protocol type / next header field

Type:  int

ipSrc[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.ipSrc "Link to this definition")  
source IP address e.g. 127.0.0.1

Type:  str

ipTos[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.ipTos "Link to this definition")  
type of service

Type:  int

ipTtl[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.ipTtl "Link to this definition")  
TTL

Type:  int

ipVersionHeader[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.ipVersionHeader "Link to this definition")  
protocol version and header length

Type:  int

macSecAn[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.macSecAn "Link to this definition")  
Association Number of MACsec header (see IEEE 802.1AE)

Type:  int

macSecIcv[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.macSecIcv "Link to this definition")  
Integrity check value of MACsec header (see IEEE 802.1AE)

Type:  bytes

macSecPn[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.macSecPn "Link to this definition")  
Packet Number of MACsec header (see IEEE 802.1AE)

Type:  int

macSecSci[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.macSecSci "Link to this definition")  
Secure Channel Identifier of MACsec header (see IEEE 802.1AE)

Type:  bytes

macSecSl[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.macSecSl "Link to this definition")  
Short Length of MACsec header (see IEEE 802.1AE)

Type:  int

macSecTci[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.macSecTci "Link to this definition")  
TAG Control Information of MACsec header (see IEEE 802.1AE)

Type:  int

macSecTciAn[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.macSecTciAn "Link to this definition")  
TCI_AN byte of MACsec header (see IEEE 802.1AE)

Type:  int

macSecTciC[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.macSecTciC "Link to this definition")  
Changed text bit in TCI of MACsec header (see IEEE 802.1AE)

Type:  bool

macSecTciE[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.macSecTciE "Link to this definition")  
Encryption bit in TCI of MACsec header (see IEEE 802.1AE)

Type:  bool

macSecTciEs[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.macSecTciEs "Link to this definition")  
End station bit in TCI of MACsec header (see IEEE 802.1AE)

Type:  bool

macSecTciSc[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.macSecTciSc "Link to this definition")  
SCI indication bit in TCI of MACsec header (see IEEE 802.1AE)

Type:  bool

macSecTciScb[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.macSecTciScb "Link to this definition")  
Single copy broadcast capability bit in TCI of MACsec header (see IEEE 802.1AE)

Type:  bool

macSecTciV[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.macSecTciV "Link to this definition")  
Version bit in TCI of MACsec header (see IEEE 802.1AE)

Type:  bool

parent[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.parent "Link to this definition")  
*Only for pseudo signals in trace analysis!* Returns the parent protocol object if there is one present, otherwise None.

Return type:  [EthernetProtocolBase](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase") | None

timestamp[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.timestamp "Link to this definition")  
Receive timestamp in sec., None if not available

Type:  Optional[float]

vlanCfi[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.vlanCfi "Link to this definition")  
802.1a canonical format indicator

Type:  int

vlanCfiOuter[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.vlanCfiOuter "Link to this definition")  
802.1ad canonical format indicator

Type:  int

vlanPcp[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.vlanPcp "Link to this definition")  
802.1a priority code point

Type:  int

vlanPcpOuter[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.vlanPcpOuter "Link to this definition")  
802.1ad priority code point

Type:  int

vlanVid[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.vlanVid "Link to this definition")  
802.1a VLAN id

Type:  int

vlanVidOuter[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.vlanVidOuter "Link to this definition")  
802.1ad VLAN id

Type:  int

### PTP[¶](#ptp "Link to this heading")

#### PacketPtpSync[¶](#packetptpsync "Link to this heading")

*class* PacketPtpSync[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync "Link to this definition")  
In the test case, use `api.Ethernet.PacketPtpSync`; in UserPyModules, use `from tts.lib.ethernet.PacketPtp import PacketPtpSync`.

\<protocol\>  
Equivalent to method [`FindParent(protocol)`](#tts.lib.ethernet.PacketPtp.PacketPtpSync.FindParent "tts.lib.ethernet.PacketPtp.PacketPtpSync.FindParent"). Direct access to parent protocols. *protocol* is one of [`OsiProtocol`](#tts.lib.ethernet.PacketEthernet.OsiProtocol "tts.lib.ethernet.PacketEthernet.OsiProtocol").

Example: Signal.eth.src provides the source MAC address of the Ethernet protocol layer.

Type:  [`EthernetProtocolBase`](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase")

FindParent(*protocol*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.FindParent "Link to this definition")  
*Only for pseudo signals in trace analysis!* Returns the requested protocol object if present, otherwise a [`NoProtocol`](#tts.lib.ethernet.PacketEthernet.NoProtocol "tts.lib.ethernet.PacketEthernet.NoProtocol") object.

Parameters:  **protocol** ([*OsiProtocol*](#tts.lib.ethernet.PacketEthernet.OsiProtocol "tts.lib.ethernet.PacketEthernet.OsiProtocol")) – The required protocol name.

Returns:  The required parent protocol object.

Return type:  [EthernetProtocolBase](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase")

GetEthDstMac()[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetEthDstMac "Link to this definition")  
Returns:  target MAC address e.g. DE:AD:BE:EF:FF:00

Return type:  str

GetEthPayload()[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetEthPayload "Link to this definition")  
Returns:  Ethernet payload

Return type:  bytes

GetEthSrcMac()[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetEthSrcMac "Link to this definition")  
Returns:  source MAC address e.g. DE:AD:BE:EF:FF:00

Return type:  str

GetEthType()[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetEthType "Link to this definition")  
Returns:  ethernet protocol type

Return type:  int

GetMacSecAn()[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetMacSecAn "Link to this definition")  
Returns:  Association Number of MACsec header (see IEEE 802.1AE)

Return type:  int

GetMacSecIcv()[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetMacSecIcv "Link to this definition")  
Returns:  Integrity check value of MACsec header (see IEEE 802.1AE)

Return type:  bytes

GetMacSecPn()[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetMacSecPn "Link to this definition")  
Returns:  Packet Number of MACsec header (see IEEE 802.1AE)

Return type:  int

GetMacSecSci()[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetMacSecSci "Link to this definition")  
Returns:  Secure Channel Identifier of MACsec header (see IEEE 802.1AE)

Return type:  bytes

GetMacSecSl()[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetMacSecSl "Link to this definition")  
Returns:  Short Length of MACsec header (see IEEE 802.1AE)

Return type:  int

GetMacSecTci()[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetMacSecTci "Link to this definition")  
Returns:  TAG Control Information of MACsec header (see IEEE 802.1AE)

Return type:  int

GetMacSecTciAn()[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetMacSecTciAn "Link to this definition")  
Returns:  TCI_AN byte of MACsec header (see IEEE 802.1AE)

Return type:  int

GetMacSecTciC()[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetMacSecTciC "Link to this definition")  
Returns:  Changed text bit in TCI of MACsec header (see IEEE 802.1AE)

Return type:  bool

GetMacSecTciE()[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetMacSecTciE "Link to this definition")  
Returns:  Encryption bit in TCI of MACsec header (see IEEE 802.1AE)

Return type:  bool

GetMacSecTciEs()[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetMacSecTciEs "Link to this definition")  
Returns:  End station bit in TCI of MACsec header (see IEEE 802.1AE)

Return type:  bool

GetMacSecTciSc()[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetMacSecTciSc "Link to this definition")  
Returns:  SCI indication bit in TCI of MACsec header (see IEEE 802.1AE)

Return type:  bool

GetMacSecTciScb()[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetMacSecTciScb "Link to this definition")  
Returns:  Single copy broadcast capability bit in TCI of MACsec header (see IEEE 802.1AE)

Return type:  bool

GetMacSecTciV()[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetMacSecTciV "Link to this definition")  
Returns:  Version bit in TCI of MACsec header (see IEEE 802.1AE)

Return type:  bool

GetPtpControl()[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetPtpControl "Link to this definition")  
Returns:  PTP control field

Return type:  int

GetPtpCorrectionField()[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetPtpCorrectionField "Link to this definition")  
Returns:  PTP correction field

Return type:  int

GetPtpDomainNumber()[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetPtpDomainNumber "Link to this definition")  
Returns:  PTP domain number

Return type:  int

GetPtpFlags()[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetPtpFlags "Link to this definition")  
Returns:  PTP flags

Return type:  int

GetPtpLogMsgInterval()[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetPtpLogMsgInterval "Link to this definition")  
Returns:  PTP log message interval

Return type:  int

GetPtpMsgLen()[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetPtpMsgLen "Link to this definition")  
Returns:  PTP message length

Return type:  int

GetPtpMsgType()[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetPtpMsgType "Link to this definition")  
Returns:  PTP message type

Return type:  int

GetPtpSequenceId()[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetPtpSequenceId "Link to this definition")  
Returns:  PTP sequence ID

Return type:  int

GetPtpSourcePortIdentity()[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetPtpSourcePortIdentity "Link to this definition")  
Returns:  PTP source port identity

Return type:  bytes

GetPtpVersion()[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetPtpVersion "Link to this definition")  
Returns:  PTP version

Return type:  int

GetTimestamp()[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetTimestamp "Link to this definition")  
Returns:  Receive timestamp in sec., None if not available

Return type:  float | None

GetVlanCfi(*ixVlanTags*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetVlanCfi "Link to this definition")  
Returns:  802.1a canonical format indicator

Return type:  int

GetVlanCfiOuter(*ixVlanTags*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetVlanCfiOuter "Link to this definition")  
Returns:  802.1ad canonical format indicator

Return type:  int

GetVlanPcp(*ixVlanTags*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetVlanPcp "Link to this definition")  
Returns:  802.1a priority code point

Return type:  int

GetVlanPcpOuter(*ixVlanTags*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetVlanPcpOuter "Link to this definition")  
Returns:  802.1ad priority code point

Return type:  int

GetVlanVid(*ixVlanTags*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetVlanVid "Link to this definition")  
Returns:  802.1a VLAN id

Return type:  int

GetVlanVidOuter(*ixVlanTags*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetVlanVidOuter "Link to this definition")  
Returns:  802.1ad VLAN id

Return type:  int

SetEthDstMac(*mac*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetEthDstMac "Link to this definition")  
Parameters:  **mac** (*str*) – target MAC address e.g. DE:AD:BE:EF:FF:00

SetEthPayload(*payload*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetEthPayload "Link to this definition")  
Parameters:  **payload** (*bytes*) – Ethernet payload

SetEthSrcMac(*mac*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetEthSrcMac "Link to this definition")  
Parameters:  **mac** (*str*) – source MAC addres e.g. DE:AD:BE:EF:FF:00

SetEthType(*ethType*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetEthType "Link to this definition")  
Parameters:  **ethType** (*int*) – ethernet protocol type

SetPtpControl(*control*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetPtpControl "Link to this definition")  
Parameters:  **control** (*int*) – PTP control field

SetPtpCorrectionField(*correctionField*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetPtpCorrectionField "Link to this definition")  
Parameters:  **correctionField** (*int*) – PTP correction field

SetPtpDomainNumber(*domainNumber*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetPtpDomainNumber "Link to this definition")  
Parameters:  **domainNumber** (*int*) – PTP domain number

SetPtpFlags(*flags*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetPtpFlags "Link to this definition")  
Parameters:  **flags** (*int*) – PTP flags

SetPtpLogMsgInterval(*logMsgInterval*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetPtpLogMsgInterval "Link to this definition")  
Parameters:  **logMsgInterval** (*int*) – log message interval

SetPtpMsgLen(*msgLen*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetPtpMsgLen "Link to this definition")  
Parameters:  **msgLen** (*int*) – PTP message length

SetPtpMsgType(*msgType*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetPtpMsgType "Link to this definition")  
Parameters:  **msgType** (*int*) – PTP message type

SetPtpSequenceId(*sequenceId*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetPtpSequenceId "Link to this definition")  
Parameters:  **sequenceId** (*int*) – PTP sequence ID

SetPtpSourcePortIdentity(*sourcePortIdentity*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetPtpSourcePortIdentity "Link to this definition")  
Parameters:  **sourcePortIdentity** (*bytes*) – PTP source port identity

SetPtpVersion(*version*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetPtpVersion "Link to this definition")  
Parameters:  **version** (*int*) – PTP version

SetTimestamp(*timestamp*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetTimestamp "Link to this definition")  
Parameters:  **timestamp** (*float* *|* *None*) – Receive timestamp in sec., None if not available

SetVlanCfi(*cfi*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetVlanCfi "Link to this definition")  
Parameters:  **cfi** (*int*) – 802.1a canonical format indicator

SetVlanCfiOuter(*cfi*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetVlanCfiOuter "Link to this definition")  
Parameters:  **cfi** (*int*) – 802.1ad canonical format indicator

SetVlanPcp(*pcp*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetVlanPcp "Link to this definition")  
Parameters:  **pcp** (*int*) – 802.1a priority code point

SetVlanPcpOuter(*pcp*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetVlanPcpOuter "Link to this definition")  
Parameters:  **pcp** (*int*) – 802.1ad priority code point

SetVlanVid(*vid*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetVlanVid "Link to this definition")  
Parameters:  **vid** (*int*) – 802.1a VLAN id

SetVlanVidOuter(*vid*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetVlanVidOuter "Link to this definition")  
Parameters:  **vid** (*int*) – 802.1ad VLAN id

ethDstMac[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.ethDstMac "Link to this definition")  
target MAC address e.g. DE:AD:BE:EF:FF:00

Type:  str

ethPayload[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.ethPayload "Link to this definition")  
Ethernet payload

Type:  bytes

ethSrcMac[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.ethSrcMac "Link to this definition")  
source MAC address e.g. DE:AD:BE:EF:FF:00

Type:  str

ethType[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.ethType "Link to this definition")  
ethernet protocol type

Type:  int

macSecAn[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.macSecAn "Link to this definition")  
Association Number of MACsec header (see IEEE 802.1AE)

Type:  int

macSecIcv[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.macSecIcv "Link to this definition")  
Integrity check value of MACsec header (see IEEE 802.1AE)

Type:  bytes

macSecPn[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.macSecPn "Link to this definition")  
Packet Number of MACsec header (see IEEE 802.1AE)

Type:  int

macSecSci[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.macSecSci "Link to this definition")  
Secure Channel Identifier of MACsec header (see IEEE 802.1AE)

Type:  bytes

macSecSl[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.macSecSl "Link to this definition")  
Short Length of MACsec header (see IEEE 802.1AE)

Type:  int

macSecTci[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.macSecTci "Link to this definition")  
TAG Control Information of MACsec header (see IEEE 802.1AE)

Type:  int

macSecTciAn[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.macSecTciAn "Link to this definition")  
TCI_AN byte of MACsec header (see IEEE 802.1AE)

Type:  int

macSecTciC[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.macSecTciC "Link to this definition")  
Changed text bit in TCI of MACsec header (see IEEE 802.1AE)

Type:  bool

macSecTciE[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.macSecTciE "Link to this definition")  
Encryption bit in TCI of MACsec header (see IEEE 802.1AE)

Type:  bool

macSecTciEs[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.macSecTciEs "Link to this definition")  
End station bit in TCI of MACsec header (see IEEE 802.1AE)

Type:  bool

macSecTciSc[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.macSecTciSc "Link to this definition")  
SCI indication bit in TCI of MACsec header (see IEEE 802.1AE)

Type:  bool

macSecTciScb[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.macSecTciScb "Link to this definition")  
Single copy broadcast capability bit in TCI of MACsec header (see IEEE 802.1AE)

Type:  bool

macSecTciV[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.macSecTciV "Link to this definition")  
Version bit in TCI of MACsec header (see IEEE 802.1AE)

Type:  bool

parent[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.parent "Link to this definition")  
*Only for pseudo signals in trace analysis!* Returns the parent protocol object if there is one present, otherwise None.

Return type:  [EthernetProtocolBase](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase") | None

ptpControl[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.ptpControl "Link to this definition")  
PTP control field

Type:  int

ptpCorrectionField[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.ptpCorrectionField "Link to this definition")  
PTP correction field

Type:  int

ptpDomainNumber[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.ptpDomainNumber "Link to this definition")  
PTP domain number

Type:  int

ptpFlags[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.ptpFlags "Link to this definition")  
PTP flags

Type:  int

ptpLogMsgInterval[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.ptpLogMsgInterval "Link to this definition")  
PTP log message interval

Type:  int

ptpMsgLen[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.ptpMsgLen "Link to this definition")  
PTP message length

Type:  int

ptpMsgType[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.ptpMsgType "Link to this definition")  
PTP message type

Type:  int

ptpSequenceId[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.ptpSequenceId "Link to this definition")  
PTP sequence ID

Type:  int

ptpSourcePortIdentity[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.ptpSourcePortIdentity "Link to this definition")  
PTP source port identity

Type:  bytes

ptpVersion[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.ptpVersion "Link to this definition")  
PTP version

Type:  int

timestamp[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.timestamp "Link to this definition")  
Receive timestamp in sec., None if not available

Type:  Optional[float]

vlanCfi[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.vlanCfi "Link to this definition")  
802.1a canonical format indicator

Type:  int

vlanCfiOuter[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.vlanCfiOuter "Link to this definition")  
802.1ad canonical format indicator

Type:  int

vlanPcp[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.vlanPcp "Link to this definition")  
802.1a priority code point

Type:  int

vlanPcpOuter[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.vlanPcpOuter "Link to this definition")  
802.1ad priority code point

Type:  int

vlanVid[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.vlanVid "Link to this definition")  
802.1a VLAN id

Type:  int

vlanVidOuter[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.vlanVidOuter "Link to this definition")  
802.1ad VLAN id

Type:  int

#### PacketPtpFollowUp[¶](#packetptpfollowup "Link to this heading")

*class* PacketPtpFollowUp[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp "Link to this definition")  
In the test case, use `api.Ethernet.PacketPtpFollowUp`; in UserPyModules, use `from tts.lib.ethernet.PacketPtp import PacketPtpFollowUp`.

\<protocol\>  
Equivalent to method [`FindParent(protocol)`](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.FindParent "tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.FindParent"). Direct access to parent protocols. *protocol* is one of [`OsiProtocol`](#tts.lib.ethernet.PacketEthernet.OsiProtocol "tts.lib.ethernet.PacketEthernet.OsiProtocol").

Example: Signal.eth.src provides the source MAC address of the Ethernet protocol layer.

Type:  [`EthernetProtocolBase`](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase")

GetPtpPreciseOriginTimestampSec()[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetPtpPreciseOriginTimestampSec "Link to this definition")  
Returns:  second portion of the PTP precise origin timestamp

Return type:  int

SetPtpPreciseOriginTimestampSec(*preciseOriginTimestampSec*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetPtpPreciseOriginTimestampSec "Link to this definition")  
Parameters:  **preciseOriginTimestampSec** (*int*) – second portion of the PTP precise origin timestamp

ptpPreciseOriginTimestampSec[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.ptpPreciseOriginTimestampSec "Link to this definition")  
second portion of the PTP precise origin timestamp

Type:  int

GetPtpPreciseOriginTimestampNSec()[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetPtpPreciseOriginTimestampNSec "Link to this definition")  
Returns:  nanosecond portion of the PTP precise origin timestamp

Return type:  int

SetPtpPreciseOriginTimestampNSec(*preciseOriginTimestampNSec*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetPtpPreciseOriginTimestampNSec "Link to this definition")  
Parameters:  **preciseOriginTimestampNSec** (*int*) – nanosecond portion of the PTP precise origin timestamp

ptpPreciseOriginTimestampNSec[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.ptpPreciseOriginTimestampNSec "Link to this definition")  
nanosecond portion of the PTP precise origin timestamp

Type:  int

FindParent(*protocol*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.FindParent "Link to this definition")  
*Only for pseudo signals in trace analysis!* Returns the requested protocol object if present, otherwise a [`NoProtocol`](#tts.lib.ethernet.PacketEthernet.NoProtocol "tts.lib.ethernet.PacketEthernet.NoProtocol") object.

Parameters:  **protocol** ([*OsiProtocol*](#tts.lib.ethernet.PacketEthernet.OsiProtocol "tts.lib.ethernet.PacketEthernet.OsiProtocol")) – The required protocol name.

Returns:  The required parent protocol object.

Return type:  [EthernetProtocolBase](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase")

GetEthDstMac()[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetEthDstMac "Link to this definition")  
Returns:  target MAC address e.g. DE:AD:BE:EF:FF:00

Return type:  str

GetEthPayload()[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetEthPayload "Link to this definition")  
Returns:  Ethernet payload

Return type:  bytes

GetEthSrcMac()[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetEthSrcMac "Link to this definition")  
Returns:  source MAC address e.g. DE:AD:BE:EF:FF:00

Return type:  str

GetEthType()[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetEthType "Link to this definition")  
Returns:  ethernet protocol type

Return type:  int

GetMacSecAn()[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetMacSecAn "Link to this definition")  
Returns:  Association Number of MACsec header (see IEEE 802.1AE)

Return type:  int

GetMacSecIcv()[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetMacSecIcv "Link to this definition")  
Returns:  Integrity check value of MACsec header (see IEEE 802.1AE)

Return type:  bytes

GetMacSecPn()[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetMacSecPn "Link to this definition")  
Returns:  Packet Number of MACsec header (see IEEE 802.1AE)

Return type:  int

GetMacSecSci()[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetMacSecSci "Link to this definition")  
Returns:  Secure Channel Identifier of MACsec header (see IEEE 802.1AE)

Return type:  bytes

GetMacSecSl()[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetMacSecSl "Link to this definition")  
Returns:  Short Length of MACsec header (see IEEE 802.1AE)

Return type:  int

GetMacSecTci()[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetMacSecTci "Link to this definition")  
Returns:  TAG Control Information of MACsec header (see IEEE 802.1AE)

Return type:  int

GetMacSecTciAn()[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetMacSecTciAn "Link to this definition")  
Returns:  TCI_AN byte of MACsec header (see IEEE 802.1AE)

Return type:  int

GetMacSecTciC()[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetMacSecTciC "Link to this definition")  
Returns:  Changed text bit in TCI of MACsec header (see IEEE 802.1AE)

Return type:  bool

GetMacSecTciE()[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetMacSecTciE "Link to this definition")  
Returns:  Encryption bit in TCI of MACsec header (see IEEE 802.1AE)

Return type:  bool

GetMacSecTciEs()[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetMacSecTciEs "Link to this definition")  
Returns:  End station bit in TCI of MACsec header (see IEEE 802.1AE)

Return type:  bool

GetMacSecTciSc()[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetMacSecTciSc "Link to this definition")  
Returns:  SCI indication bit in TCI of MACsec header (see IEEE 802.1AE)

Return type:  bool

GetMacSecTciScb()[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetMacSecTciScb "Link to this definition")  
Returns:  Single copy broadcast capability bit in TCI of MACsec header (see IEEE 802.1AE)

Return type:  bool

GetMacSecTciV()[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetMacSecTciV "Link to this definition")  
Returns:  Version bit in TCI of MACsec header (see IEEE 802.1AE)

Return type:  bool

GetPtpControl()[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetPtpControl "Link to this definition")  
Returns:  PTP control field

Return type:  int

GetPtpCorrectionField()[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetPtpCorrectionField "Link to this definition")  
Returns:  PTP correction field

Return type:  int

GetPtpDomainNumber()[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetPtpDomainNumber "Link to this definition")  
Returns:  PTP domain number

Return type:  int

GetPtpFlags()[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetPtpFlags "Link to this definition")  
Returns:  PTP flags

Return type:  int

GetPtpLogMsgInterval()[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetPtpLogMsgInterval "Link to this definition")  
Returns:  PTP log message interval

Return type:  int

GetPtpMsgLen()[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetPtpMsgLen "Link to this definition")  
Returns:  PTP message length

Return type:  int

GetPtpMsgType()[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetPtpMsgType "Link to this definition")  
Returns:  PTP message type

Return type:  int

GetPtpSequenceId()[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetPtpSequenceId "Link to this definition")  
Returns:  PTP sequence ID

Return type:  int

GetPtpSourcePortIdentity()[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetPtpSourcePortIdentity "Link to this definition")  
Returns:  PTP source port identity

Return type:  bytes

GetPtpVersion()[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetPtpVersion "Link to this definition")  
Returns:  PTP version

Return type:  int

GetTimestamp()[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetTimestamp "Link to this definition")  
Returns:  Receive timestamp in sec., None if not available

Return type:  float | None

GetVlanCfi(*ixVlanTags*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetVlanCfi "Link to this definition")  
Returns:  802.1a canonical format indicator

Return type:  int

GetVlanCfiOuter(*ixVlanTags*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetVlanCfiOuter "Link to this definition")  
Returns:  802.1ad canonical format indicator

Return type:  int

GetVlanPcp(*ixVlanTags*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetVlanPcp "Link to this definition")  
Returns:  802.1a priority code point

Return type:  int

GetVlanPcpOuter(*ixVlanTags*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetVlanPcpOuter "Link to this definition")  
Returns:  802.1ad priority code point

Return type:  int

GetVlanVid(*ixVlanTags*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetVlanVid "Link to this definition")  
Returns:  802.1a VLAN id

Return type:  int

GetVlanVidOuter(*ixVlanTags*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetVlanVidOuter "Link to this definition")  
Returns:  802.1ad VLAN id

Return type:  int

SetEthDstMac(*mac*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetEthDstMac "Link to this definition")  
Parameters:  **mac** (*str*) – target MAC address e.g. DE:AD:BE:EF:FF:00

SetEthPayload(*payload*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetEthPayload "Link to this definition")  
Parameters:  **payload** (*bytes*) – Ethernet payload

SetEthSrcMac(*mac*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetEthSrcMac "Link to this definition")  
Parameters:  **mac** (*str*) – source MAC addres e.g. DE:AD:BE:EF:FF:00

SetEthType(*ethType*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetEthType "Link to this definition")  
Parameters:  **ethType** (*int*) – ethernet protocol type

SetPtpControl(*control*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetPtpControl "Link to this definition")  
Parameters:  **control** (*int*) – PTP control field

SetPtpCorrectionField(*correctionField*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetPtpCorrectionField "Link to this definition")  
Parameters:  **correctionField** (*int*) – PTP correction field

SetPtpDomainNumber(*domainNumber*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetPtpDomainNumber "Link to this definition")  
Parameters:  **domainNumber** (*int*) – PTP domain number

SetPtpFlags(*flags*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetPtpFlags "Link to this definition")  
Parameters:  **flags** (*int*) – PTP flags

SetPtpLogMsgInterval(*logMsgInterval*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetPtpLogMsgInterval "Link to this definition")  
Parameters:  **logMsgInterval** (*int*) – log message interval

SetPtpMsgLen(*msgLen*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetPtpMsgLen "Link to this definition")  
Parameters:  **msgLen** (*int*) – PTP message length

SetPtpMsgType(*msgType*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetPtpMsgType "Link to this definition")  
Parameters:  **msgType** (*int*) – PTP message type

SetPtpSequenceId(*sequenceId*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetPtpSequenceId "Link to this definition")  
Parameters:  **sequenceId** (*int*) – PTP sequence ID

SetPtpSourcePortIdentity(*sourcePortIdentity*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetPtpSourcePortIdentity "Link to this definition")  
Parameters:  **sourcePortIdentity** (*bytes*) – PTP source port identity

SetPtpVersion(*version*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetPtpVersion "Link to this definition")  
Parameters:  **version** (*int*) – PTP version

SetTimestamp(*timestamp*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetTimestamp "Link to this definition")  
Parameters:  **timestamp** (*float* *|* *None*) – Receive timestamp in sec., None if not available

SetVlanCfi(*cfi*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetVlanCfi "Link to this definition")  
Parameters:  **cfi** (*int*) – 802.1a canonical format indicator

SetVlanCfiOuter(*cfi*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetVlanCfiOuter "Link to this definition")  
Parameters:  **cfi** (*int*) – 802.1ad canonical format indicator

SetVlanPcp(*pcp*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetVlanPcp "Link to this definition")  
Parameters:  **pcp** (*int*) – 802.1a priority code point

SetVlanPcpOuter(*pcp*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetVlanPcpOuter "Link to this definition")  
Parameters:  **pcp** (*int*) – 802.1ad priority code point

SetVlanVid(*vid*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetVlanVid "Link to this definition")  
Parameters:  **vid** (*int*) – 802.1a VLAN id

SetVlanVidOuter(*vid*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetVlanVidOuter "Link to this definition")  
Parameters:  **vid** (*int*) – 802.1ad VLAN id

ethDstMac[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.ethDstMac "Link to this definition")  
target MAC address e.g. DE:AD:BE:EF:FF:00

Type:  str

ethPayload[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.ethPayload "Link to this definition")  
Ethernet payload

Type:  bytes

ethSrcMac[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.ethSrcMac "Link to this definition")  
source MAC address e.g. DE:AD:BE:EF:FF:00

Type:  str

ethType[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.ethType "Link to this definition")  
ethernet protocol type

Type:  int

macSecAn[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.macSecAn "Link to this definition")  
Association Number of MACsec header (see IEEE 802.1AE)

Type:  int

macSecIcv[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.macSecIcv "Link to this definition")  
Integrity check value of MACsec header (see IEEE 802.1AE)

Type:  bytes

macSecPn[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.macSecPn "Link to this definition")  
Packet Number of MACsec header (see IEEE 802.1AE)

Type:  int

macSecSci[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.macSecSci "Link to this definition")  
Secure Channel Identifier of MACsec header (see IEEE 802.1AE)

Type:  bytes

macSecSl[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.macSecSl "Link to this definition")  
Short Length of MACsec header (see IEEE 802.1AE)

Type:  int

macSecTci[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.macSecTci "Link to this definition")  
TAG Control Information of MACsec header (see IEEE 802.1AE)

Type:  int

macSecTciAn[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.macSecTciAn "Link to this definition")  
TCI_AN byte of MACsec header (see IEEE 802.1AE)

Type:  int

macSecTciC[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.macSecTciC "Link to this definition")  
Changed text bit in TCI of MACsec header (see IEEE 802.1AE)

Type:  bool

macSecTciE[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.macSecTciE "Link to this definition")  
Encryption bit in TCI of MACsec header (see IEEE 802.1AE)

Type:  bool

macSecTciEs[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.macSecTciEs "Link to this definition")  
End station bit in TCI of MACsec header (see IEEE 802.1AE)

Type:  bool

macSecTciSc[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.macSecTciSc "Link to this definition")  
SCI indication bit in TCI of MACsec header (see IEEE 802.1AE)

Type:  bool

macSecTciScb[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.macSecTciScb "Link to this definition")  
Single copy broadcast capability bit in TCI of MACsec header (see IEEE 802.1AE)

Type:  bool

macSecTciV[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.macSecTciV "Link to this definition")  
Version bit in TCI of MACsec header (see IEEE 802.1AE)

Type:  bool

parent[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.parent "Link to this definition")  
*Only for pseudo signals in trace analysis!* Returns the parent protocol object if there is one present, otherwise None.

Return type:  [EthernetProtocolBase](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase") | None

ptpControl[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.ptpControl "Link to this definition")  
PTP control field

Type:  int

ptpCorrectionField[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.ptpCorrectionField "Link to this definition")  
PTP correction field

Type:  int

ptpDomainNumber[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.ptpDomainNumber "Link to this definition")  
PTP domain number

Type:  int

ptpFlags[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.ptpFlags "Link to this definition")  
PTP flags

Type:  int

ptpLogMsgInterval[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.ptpLogMsgInterval "Link to this definition")  
PTP log message interval

Type:  int

ptpMsgLen[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.ptpMsgLen "Link to this definition")  
PTP message length

Type:  int

ptpMsgType[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.ptpMsgType "Link to this definition")  
PTP message type

Type:  int

ptpSequenceId[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.ptpSequenceId "Link to this definition")  
PTP sequence ID

Type:  int

ptpSourcePortIdentity[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.ptpSourcePortIdentity "Link to this definition")  
PTP source port identity

Type:  bytes

ptpVersion[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.ptpVersion "Link to this definition")  
PTP version

Type:  int

timestamp[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.timestamp "Link to this definition")  
Receive timestamp in sec., None if not available

Type:  Optional[float]

vlanCfi[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.vlanCfi "Link to this definition")  
802.1a canonical format indicator

Type:  int

vlanCfiOuter[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.vlanCfiOuter "Link to this definition")  
802.1ad canonical format indicator

Type:  int

vlanPcp[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.vlanPcp "Link to this definition")  
802.1a priority code point

Type:  int

vlanPcpOuter[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.vlanPcpOuter "Link to this definition")  
802.1ad priority code point

Type:  int

vlanVid[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.vlanVid "Link to this definition")  
802.1a VLAN id

Type:  int

vlanVidOuter[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.vlanVidOuter "Link to this definition")  
802.1ad VLAN id

Type:  int

#### PacketPdelayReq[¶](#packetpdelayreq "Link to this heading")

*class* PacketPdelayReq[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq "Link to this definition")  
In the test case, use `api.Ethernet.PacketPdelayReq`; in UserPyModules, use `from tts.lib.ethernet.PacketPtp import PacketPdelayReq`.

\<protocol\>  
Equivalent to method [`FindParent(protocol)`](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.FindParent "tts.lib.ethernet.PacketPtp.PacketPdelayReq.FindParent"). Direct access to parent protocols. *protocol* is one of [`OsiProtocol`](#tts.lib.ethernet.PacketEthernet.OsiProtocol "tts.lib.ethernet.PacketEthernet.OsiProtocol").

Example: Signal.eth.src provides the source MAC address of the Ethernet protocol layer.

Type:  [`EthernetProtocolBase`](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase")

FindParent(*protocol*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.FindParent "Link to this definition")  
*Only for pseudo signals in trace analysis!* Returns the requested protocol object if present, otherwise a [`NoProtocol`](#tts.lib.ethernet.PacketEthernet.NoProtocol "tts.lib.ethernet.PacketEthernet.NoProtocol") object.

Parameters:  **protocol** ([*OsiProtocol*](#tts.lib.ethernet.PacketEthernet.OsiProtocol "tts.lib.ethernet.PacketEthernet.OsiProtocol")) – The required protocol name.

Returns:  The required parent protocol object.

Return type:  [EthernetProtocolBase](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase")

GetEthDstMac()[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetEthDstMac "Link to this definition")  
Returns:  target MAC address e.g. DE:AD:BE:EF:FF:00

Return type:  str

GetEthPayload()[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetEthPayload "Link to this definition")  
Returns:  Ethernet payload

Return type:  bytes

GetEthSrcMac()[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetEthSrcMac "Link to this definition")  
Returns:  source MAC address e.g. DE:AD:BE:EF:FF:00

Return type:  str

GetEthType()[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetEthType "Link to this definition")  
Returns:  ethernet protocol type

Return type:  int

GetMacSecAn()[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetMacSecAn "Link to this definition")  
Returns:  Association Number of MACsec header (see IEEE 802.1AE)

Return type:  int

GetMacSecIcv()[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetMacSecIcv "Link to this definition")  
Returns:  Integrity check value of MACsec header (see IEEE 802.1AE)

Return type:  bytes

GetMacSecPn()[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetMacSecPn "Link to this definition")  
Returns:  Packet Number of MACsec header (see IEEE 802.1AE)

Return type:  int

GetMacSecSci()[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetMacSecSci "Link to this definition")  
Returns:  Secure Channel Identifier of MACsec header (see IEEE 802.1AE)

Return type:  bytes

GetMacSecSl()[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetMacSecSl "Link to this definition")  
Returns:  Short Length of MACsec header (see IEEE 802.1AE)

Return type:  int

GetMacSecTci()[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetMacSecTci "Link to this definition")  
Returns:  TAG Control Information of MACsec header (see IEEE 802.1AE)

Return type:  int

GetMacSecTciAn()[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetMacSecTciAn "Link to this definition")  
Returns:  TCI_AN byte of MACsec header (see IEEE 802.1AE)

Return type:  int

GetMacSecTciC()[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetMacSecTciC "Link to this definition")  
Returns:  Changed text bit in TCI of MACsec header (see IEEE 802.1AE)

Return type:  bool

GetMacSecTciE()[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetMacSecTciE "Link to this definition")  
Returns:  Encryption bit in TCI of MACsec header (see IEEE 802.1AE)

Return type:  bool

GetMacSecTciEs()[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetMacSecTciEs "Link to this definition")  
Returns:  End station bit in TCI of MACsec header (see IEEE 802.1AE)

Return type:  bool

GetMacSecTciSc()[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetMacSecTciSc "Link to this definition")  
Returns:  SCI indication bit in TCI of MACsec header (see IEEE 802.1AE)

Return type:  bool

GetMacSecTciScb()[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetMacSecTciScb "Link to this definition")  
Returns:  Single copy broadcast capability bit in TCI of MACsec header (see IEEE 802.1AE)

Return type:  bool

GetMacSecTciV()[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetMacSecTciV "Link to this definition")  
Returns:  Version bit in TCI of MACsec header (see IEEE 802.1AE)

Return type:  bool

GetPtpControl()[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetPtpControl "Link to this definition")  
Returns:  PTP control field

Return type:  int

GetPtpCorrectionField()[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetPtpCorrectionField "Link to this definition")  
Returns:  PTP correction field

Return type:  int

GetPtpDomainNumber()[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetPtpDomainNumber "Link to this definition")  
Returns:  PTP domain number

Return type:  int

GetPtpFlags()[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetPtpFlags "Link to this definition")  
Returns:  PTP flags

Return type:  int

GetPtpLogMsgInterval()[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetPtpLogMsgInterval "Link to this definition")  
Returns:  PTP log message interval

Return type:  int

GetPtpMsgLen()[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetPtpMsgLen "Link to this definition")  
Returns:  PTP message length

Return type:  int

GetPtpMsgType()[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetPtpMsgType "Link to this definition")  
Returns:  PTP message type

Return type:  int

GetPtpSequenceId()[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetPtpSequenceId "Link to this definition")  
Returns:  PTP sequence ID

Return type:  int

GetPtpSourcePortIdentity()[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetPtpSourcePortIdentity "Link to this definition")  
Returns:  PTP source port identity

Return type:  bytes

GetPtpVersion()[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetPtpVersion "Link to this definition")  
Returns:  PTP version

Return type:  int

GetTimestamp()[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetTimestamp "Link to this definition")  
Returns:  Receive timestamp in sec., None if not available

Return type:  float | None

GetVlanCfi(*ixVlanTags*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetVlanCfi "Link to this definition")  
Returns:  802.1a canonical format indicator

Return type:  int

GetVlanCfiOuter(*ixVlanTags*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetVlanCfiOuter "Link to this definition")  
Returns:  802.1ad canonical format indicator

Return type:  int

GetVlanPcp(*ixVlanTags*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetVlanPcp "Link to this definition")  
Returns:  802.1a priority code point

Return type:  int

GetVlanPcpOuter(*ixVlanTags*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetVlanPcpOuter "Link to this definition")  
Returns:  802.1ad priority code point

Return type:  int

GetVlanVid(*ixVlanTags*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetVlanVid "Link to this definition")  
Returns:  802.1a VLAN id

Return type:  int

GetVlanVidOuter(*ixVlanTags*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetVlanVidOuter "Link to this definition")  
Returns:  802.1ad VLAN id

Return type:  int

SetEthDstMac(*mac*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetEthDstMac "Link to this definition")  
Parameters:  **mac** (*str*) – target MAC address e.g. DE:AD:BE:EF:FF:00

SetEthPayload(*payload*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetEthPayload "Link to this definition")  
Parameters:  **payload** (*bytes*) – Ethernet payload

SetEthSrcMac(*mac*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetEthSrcMac "Link to this definition")  
Parameters:  **mac** (*str*) – source MAC addres e.g. DE:AD:BE:EF:FF:00

SetEthType(*ethType*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetEthType "Link to this definition")  
Parameters:  **ethType** (*int*) – ethernet protocol type

SetPtpControl(*control*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetPtpControl "Link to this definition")  
Parameters:  **control** (*int*) – PTP control field

SetPtpCorrectionField(*correctionField*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetPtpCorrectionField "Link to this definition")  
Parameters:  **correctionField** (*int*) – PTP correction field

SetPtpDomainNumber(*domainNumber*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetPtpDomainNumber "Link to this definition")  
Parameters:  **domainNumber** (*int*) – PTP domain number

SetPtpFlags(*flags*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetPtpFlags "Link to this definition")  
Parameters:  **flags** (*int*) – PTP flags

SetPtpLogMsgInterval(*logMsgInterval*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetPtpLogMsgInterval "Link to this definition")  
Parameters:  **logMsgInterval** (*int*) – log message interval

SetPtpMsgLen(*msgLen*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetPtpMsgLen "Link to this definition")  
Parameters:  **msgLen** (*int*) – PTP message length

SetPtpMsgType(*msgType*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetPtpMsgType "Link to this definition")  
Parameters:  **msgType** (*int*) – PTP message type

SetPtpSequenceId(*sequenceId*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetPtpSequenceId "Link to this definition")  
Parameters:  **sequenceId** (*int*) – PTP sequence ID

SetPtpSourcePortIdentity(*sourcePortIdentity*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetPtpSourcePortIdentity "Link to this definition")  
Parameters:  **sourcePortIdentity** (*bytes*) – PTP source port identity

SetPtpVersion(*version*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetPtpVersion "Link to this definition")  
Parameters:  **version** (*int*) – PTP version

SetTimestamp(*timestamp*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetTimestamp "Link to this definition")  
Parameters:  **timestamp** (*float* *|* *None*) – Receive timestamp in sec., None if not available

SetVlanCfi(*cfi*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetVlanCfi "Link to this definition")  
Parameters:  **cfi** (*int*) – 802.1a canonical format indicator

SetVlanCfiOuter(*cfi*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetVlanCfiOuter "Link to this definition")  
Parameters:  **cfi** (*int*) – 802.1ad canonical format indicator

SetVlanPcp(*pcp*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetVlanPcp "Link to this definition")  
Parameters:  **pcp** (*int*) – 802.1a priority code point

SetVlanPcpOuter(*pcp*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetVlanPcpOuter "Link to this definition")  
Parameters:  **pcp** (*int*) – 802.1ad priority code point

SetVlanVid(*vid*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetVlanVid "Link to this definition")  
Parameters:  **vid** (*int*) – 802.1a VLAN id

SetVlanVidOuter(*vid*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetVlanVidOuter "Link to this definition")  
Parameters:  **vid** (*int*) – 802.1ad VLAN id

ethDstMac[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.ethDstMac "Link to this definition")  
target MAC address e.g. DE:AD:BE:EF:FF:00

Type:  str

ethPayload[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.ethPayload "Link to this definition")  
Ethernet payload

Type:  bytes

ethSrcMac[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.ethSrcMac "Link to this definition")  
source MAC address e.g. DE:AD:BE:EF:FF:00

Type:  str

ethType[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.ethType "Link to this definition")  
ethernet protocol type

Type:  int

macSecAn[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.macSecAn "Link to this definition")  
Association Number of MACsec header (see IEEE 802.1AE)

Type:  int

macSecIcv[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.macSecIcv "Link to this definition")  
Integrity check value of MACsec header (see IEEE 802.1AE)

Type:  bytes

macSecPn[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.macSecPn "Link to this definition")  
Packet Number of MACsec header (see IEEE 802.1AE)

Type:  int

macSecSci[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.macSecSci "Link to this definition")  
Secure Channel Identifier of MACsec header (see IEEE 802.1AE)

Type:  bytes

macSecSl[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.macSecSl "Link to this definition")  
Short Length of MACsec header (see IEEE 802.1AE)

Type:  int

macSecTci[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.macSecTci "Link to this definition")  
TAG Control Information of MACsec header (see IEEE 802.1AE)

Type:  int

macSecTciAn[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.macSecTciAn "Link to this definition")  
TCI_AN byte of MACsec header (see IEEE 802.1AE)

Type:  int

macSecTciC[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.macSecTciC "Link to this definition")  
Changed text bit in TCI of MACsec header (see IEEE 802.1AE)

Type:  bool

macSecTciE[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.macSecTciE "Link to this definition")  
Encryption bit in TCI of MACsec header (see IEEE 802.1AE)

Type:  bool

macSecTciEs[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.macSecTciEs "Link to this definition")  
End station bit in TCI of MACsec header (see IEEE 802.1AE)

Type:  bool

macSecTciSc[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.macSecTciSc "Link to this definition")  
SCI indication bit in TCI of MACsec header (see IEEE 802.1AE)

Type:  bool

macSecTciScb[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.macSecTciScb "Link to this definition")  
Single copy broadcast capability bit in TCI of MACsec header (see IEEE 802.1AE)

Type:  bool

macSecTciV[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.macSecTciV "Link to this definition")  
Version bit in TCI of MACsec header (see IEEE 802.1AE)

Type:  bool

parent[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.parent "Link to this definition")  
*Only for pseudo signals in trace analysis!* Returns the parent protocol object if there is one present, otherwise None.

Return type:  [EthernetProtocolBase](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase") | None

ptpControl[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.ptpControl "Link to this definition")  
PTP control field

Type:  int

ptpCorrectionField[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.ptpCorrectionField "Link to this definition")  
PTP correction field

Type:  int

ptpDomainNumber[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.ptpDomainNumber "Link to this definition")  
PTP domain number

Type:  int

ptpFlags[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.ptpFlags "Link to this definition")  
PTP flags

Type:  int

ptpLogMsgInterval[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.ptpLogMsgInterval "Link to this definition")  
PTP log message interval

Type:  int

ptpMsgLen[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.ptpMsgLen "Link to this definition")  
PTP message length

Type:  int

ptpMsgType[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.ptpMsgType "Link to this definition")  
PTP message type

Type:  int

ptpSequenceId[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.ptpSequenceId "Link to this definition")  
PTP sequence ID

Type:  int

ptpSourcePortIdentity[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.ptpSourcePortIdentity "Link to this definition")  
PTP source port identity

Type:  bytes

ptpVersion[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.ptpVersion "Link to this definition")  
PTP version

Type:  int

timestamp[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.timestamp "Link to this definition")  
Receive timestamp in sec., None if not available

Type:  Optional[float]

vlanCfi[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.vlanCfi "Link to this definition")  
802.1a canonical format indicator

Type:  int

vlanCfiOuter[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.vlanCfiOuter "Link to this definition")  
802.1ad canonical format indicator

Type:  int

vlanPcp[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.vlanPcp "Link to this definition")  
802.1a priority code point

Type:  int

vlanPcpOuter[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.vlanPcpOuter "Link to this definition")  
802.1ad priority code point

Type:  int

vlanVid[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.vlanVid "Link to this definition")  
802.1a VLAN id

Type:  int

vlanVidOuter[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.vlanVidOuter "Link to this definition")  
802.1ad VLAN id

Type:  int

#### PacketPdelayResp[¶](#packetpdelayresp "Link to this heading")

*class* PacketPdelayResp[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp "Link to this definition")  
In the test case, use `api.Ethernet.PacketPdelayResp`; in UserPyModules, use `from tts.lib.ethernet.PacketPtp import PacketPdelayResp`.

\<protocol\>  
Equivalent to method [`FindParent(protocol)`](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.FindParent "tts.lib.ethernet.PacketPtp.PacketPdelayResp.FindParent"). Direct access to parent protocols. *protocol* is one of [`OsiProtocol`](#tts.lib.ethernet.PacketEthernet.OsiProtocol "tts.lib.ethernet.PacketEthernet.OsiProtocol").

Example: Signal.eth.src provides the source MAC address of the Ethernet protocol layer.

Type:  [`EthernetProtocolBase`](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase")

GetPtpRequestReceiptTimestampSec()[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetPtpRequestReceiptTimestampSec "Link to this definition")  
Returns:  second portion of the PTP request receipt timestamp

Return type:  int

SetPtpRequestReceiptTimestampSec(*requestReceiptTimestampSec*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetPtpRequestReceiptTimestampSec "Link to this definition")  
Parameters:  **requestReceiptTimestampSec** (*int*) – second portion of the PTP request receipt timestamp

ptpRequestReceiptTimestampSec[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.ptpRequestReceiptTimestampSec "Link to this definition")  
second portion of the PTP request receipt timestamp

Type:  int

GetPtpRequestReceiptTimestampNSec()[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetPtpRequestReceiptTimestampNSec "Link to this definition")  
Returns:  nanosecond portion of the PTP precise origin timestamp

Return type:  int

SetPtpRequestReceiptTimestampNSec(*requestReceiptTimestampNSec*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetPtpRequestReceiptTimestampNSec "Link to this definition")  
Parameters:  **requestReceiptTimestampNSec** (*int*) – nanosecond portion of the PTP precise origin timestamp

ptpRequestReceiptTimestampNSec[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.ptpRequestReceiptTimestampNSec "Link to this definition")  
nanosecond portion of the PTP precise origin timestamp

Type:  int

GetPtpRequestingPortIdentity()[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetPtpRequestingPortIdentity "Link to this definition")  
Returns:  PTP requesting port identity

Return type:  bytes

SetPtpRequestingPortIdentity(*requestingPortIdentity*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetPtpRequestingPortIdentity "Link to this definition")  
Parameters:  **requestingPortIdentity** (*bytes*) – PTP requesting port identity

ptpRequestingPortIdentity[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.ptpRequestingPortIdentity "Link to this definition")  
PTP requesting port identity

Type:  bytes

FindParent(*protocol*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.FindParent "Link to this definition")  
*Only for pseudo signals in trace analysis!* Returns the requested protocol object if present, otherwise a [`NoProtocol`](#tts.lib.ethernet.PacketEthernet.NoProtocol "tts.lib.ethernet.PacketEthernet.NoProtocol") object.

Parameters:  **protocol** ([*OsiProtocol*](#tts.lib.ethernet.PacketEthernet.OsiProtocol "tts.lib.ethernet.PacketEthernet.OsiProtocol")) – The required protocol name.

Returns:  The required parent protocol object.

Return type:  [EthernetProtocolBase](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase")

GetEthDstMac()[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetEthDstMac "Link to this definition")  
Returns:  target MAC address e.g. DE:AD:BE:EF:FF:00

Return type:  str

GetEthPayload()[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetEthPayload "Link to this definition")  
Returns:  Ethernet payload

Return type:  bytes

GetEthSrcMac()[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetEthSrcMac "Link to this definition")  
Returns:  source MAC address e.g. DE:AD:BE:EF:FF:00

Return type:  str

GetEthType()[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetEthType "Link to this definition")  
Returns:  ethernet protocol type

Return type:  int

GetMacSecAn()[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetMacSecAn "Link to this definition")  
Returns:  Association Number of MACsec header (see IEEE 802.1AE)

Return type:  int

GetMacSecIcv()[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetMacSecIcv "Link to this definition")  
Returns:  Integrity check value of MACsec header (see IEEE 802.1AE)

Return type:  bytes

GetMacSecPn()[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetMacSecPn "Link to this definition")  
Returns:  Packet Number of MACsec header (see IEEE 802.1AE)

Return type:  int

GetMacSecSci()[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetMacSecSci "Link to this definition")  
Returns:  Secure Channel Identifier of MACsec header (see IEEE 802.1AE)

Return type:  bytes

GetMacSecSl()[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetMacSecSl "Link to this definition")  
Returns:  Short Length of MACsec header (see IEEE 802.1AE)

Return type:  int

GetMacSecTci()[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetMacSecTci "Link to this definition")  
Returns:  TAG Control Information of MACsec header (see IEEE 802.1AE)

Return type:  int

GetMacSecTciAn()[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetMacSecTciAn "Link to this definition")  
Returns:  TCI_AN byte of MACsec header (see IEEE 802.1AE)

Return type:  int

GetMacSecTciC()[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetMacSecTciC "Link to this definition")  
Returns:  Changed text bit in TCI of MACsec header (see IEEE 802.1AE)

Return type:  bool

GetMacSecTciE()[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetMacSecTciE "Link to this definition")  
Returns:  Encryption bit in TCI of MACsec header (see IEEE 802.1AE)

Return type:  bool

GetMacSecTciEs()[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetMacSecTciEs "Link to this definition")  
Returns:  End station bit in TCI of MACsec header (see IEEE 802.1AE)

Return type:  bool

GetMacSecTciSc()[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetMacSecTciSc "Link to this definition")  
Returns:  SCI indication bit in TCI of MACsec header (see IEEE 802.1AE)

Return type:  bool

GetMacSecTciScb()[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetMacSecTciScb "Link to this definition")  
Returns:  Single copy broadcast capability bit in TCI of MACsec header (see IEEE 802.1AE)

Return type:  bool

GetMacSecTciV()[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetMacSecTciV "Link to this definition")  
Returns:  Version bit in TCI of MACsec header (see IEEE 802.1AE)

Return type:  bool

GetPtpControl()[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetPtpControl "Link to this definition")  
Returns:  PTP control field

Return type:  int

GetPtpCorrectionField()[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetPtpCorrectionField "Link to this definition")  
Returns:  PTP correction field

Return type:  int

GetPtpDomainNumber()[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetPtpDomainNumber "Link to this definition")  
Returns:  PTP domain number

Return type:  int

GetPtpFlags()[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetPtpFlags "Link to this definition")  
Returns:  PTP flags

Return type:  int

GetPtpLogMsgInterval()[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetPtpLogMsgInterval "Link to this definition")  
Returns:  PTP log message interval

Return type:  int

GetPtpMsgLen()[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetPtpMsgLen "Link to this definition")  
Returns:  PTP message length

Return type:  int

GetPtpMsgType()[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetPtpMsgType "Link to this definition")  
Returns:  PTP message type

Return type:  int

GetPtpSequenceId()[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetPtpSequenceId "Link to this definition")  
Returns:  PTP sequence ID

Return type:  int

GetPtpSourcePortIdentity()[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetPtpSourcePortIdentity "Link to this definition")  
Returns:  PTP source port identity

Return type:  bytes

GetPtpVersion()[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetPtpVersion "Link to this definition")  
Returns:  PTP version

Return type:  int

GetTimestamp()[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetTimestamp "Link to this definition")  
Returns:  Receive timestamp in sec., None if not available

Return type:  float | None

GetVlanCfi(*ixVlanTags*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetVlanCfi "Link to this definition")  
Returns:  802.1a canonical format indicator

Return type:  int

GetVlanCfiOuter(*ixVlanTags*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetVlanCfiOuter "Link to this definition")  
Returns:  802.1ad canonical format indicator

Return type:  int

GetVlanPcp(*ixVlanTags*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetVlanPcp "Link to this definition")  
Returns:  802.1a priority code point

Return type:  int

GetVlanPcpOuter(*ixVlanTags*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetVlanPcpOuter "Link to this definition")  
Returns:  802.1ad priority code point

Return type:  int

GetVlanVid(*ixVlanTags*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetVlanVid "Link to this definition")  
Returns:  802.1a VLAN id

Return type:  int

GetVlanVidOuter(*ixVlanTags*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetVlanVidOuter "Link to this definition")  
Returns:  802.1ad VLAN id

Return type:  int

SetEthDstMac(*mac*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetEthDstMac "Link to this definition")  
Parameters:  **mac** (*str*) – target MAC address e.g. DE:AD:BE:EF:FF:00

SetEthPayload(*payload*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetEthPayload "Link to this definition")  
Parameters:  **payload** (*bytes*) – Ethernet payload

SetEthSrcMac(*mac*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetEthSrcMac "Link to this definition")  
Parameters:  **mac** (*str*) – source MAC addres e.g. DE:AD:BE:EF:FF:00

SetEthType(*ethType*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetEthType "Link to this definition")  
Parameters:  **ethType** (*int*) – ethernet protocol type

SetPtpControl(*control*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetPtpControl "Link to this definition")  
Parameters:  **control** (*int*) – PTP control field

SetPtpCorrectionField(*correctionField*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetPtpCorrectionField "Link to this definition")  
Parameters:  **correctionField** (*int*) – PTP correction field

SetPtpDomainNumber(*domainNumber*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetPtpDomainNumber "Link to this definition")  
Parameters:  **domainNumber** (*int*) – PTP domain number

SetPtpFlags(*flags*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetPtpFlags "Link to this definition")  
Parameters:  **flags** (*int*) – PTP flags

SetPtpLogMsgInterval(*logMsgInterval*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetPtpLogMsgInterval "Link to this definition")  
Parameters:  **logMsgInterval** (*int*) – log message interval

SetPtpMsgLen(*msgLen*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetPtpMsgLen "Link to this definition")  
Parameters:  **msgLen** (*int*) – PTP message length

SetPtpMsgType(*msgType*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetPtpMsgType "Link to this definition")  
Parameters:  **msgType** (*int*) – PTP message type

SetPtpSequenceId(*sequenceId*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetPtpSequenceId "Link to this definition")  
Parameters:  **sequenceId** (*int*) – PTP sequence ID

SetPtpSourcePortIdentity(*sourcePortIdentity*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetPtpSourcePortIdentity "Link to this definition")  
Parameters:  **sourcePortIdentity** (*bytes*) – PTP source port identity

SetPtpVersion(*version*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetPtpVersion "Link to this definition")  
Parameters:  **version** (*int*) – PTP version

SetTimestamp(*timestamp*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetTimestamp "Link to this definition")  
Parameters:  **timestamp** (*float* *|* *None*) – Receive timestamp in sec., None if not available

SetVlanCfi(*cfi*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetVlanCfi "Link to this definition")  
Parameters:  **cfi** (*int*) – 802.1a canonical format indicator

SetVlanCfiOuter(*cfi*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetVlanCfiOuter "Link to this definition")  
Parameters:  **cfi** (*int*) – 802.1ad canonical format indicator

SetVlanPcp(*pcp*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetVlanPcp "Link to this definition")  
Parameters:  **pcp** (*int*) – 802.1a priority code point

SetVlanPcpOuter(*pcp*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetVlanPcpOuter "Link to this definition")  
Parameters:  **pcp** (*int*) – 802.1ad priority code point

SetVlanVid(*vid*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetVlanVid "Link to this definition")  
Parameters:  **vid** (*int*) – 802.1a VLAN id

SetVlanVidOuter(*vid*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetVlanVidOuter "Link to this definition")  
Parameters:  **vid** (*int*) – 802.1ad VLAN id

ethDstMac[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.ethDstMac "Link to this definition")  
target MAC address e.g. DE:AD:BE:EF:FF:00

Type:  str

ethPayload[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.ethPayload "Link to this definition")  
Ethernet payload

Type:  bytes

ethSrcMac[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.ethSrcMac "Link to this definition")  
source MAC address e.g. DE:AD:BE:EF:FF:00

Type:  str

ethType[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.ethType "Link to this definition")  
ethernet protocol type

Type:  int

macSecAn[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.macSecAn "Link to this definition")  
Association Number of MACsec header (see IEEE 802.1AE)

Type:  int

macSecIcv[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.macSecIcv "Link to this definition")  
Integrity check value of MACsec header (see IEEE 802.1AE)

Type:  bytes

macSecPn[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.macSecPn "Link to this definition")  
Packet Number of MACsec header (see IEEE 802.1AE)

Type:  int

macSecSci[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.macSecSci "Link to this definition")  
Secure Channel Identifier of MACsec header (see IEEE 802.1AE)

Type:  bytes

macSecSl[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.macSecSl "Link to this definition")  
Short Length of MACsec header (see IEEE 802.1AE)

Type:  int

macSecTci[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.macSecTci "Link to this definition")  
TAG Control Information of MACsec header (see IEEE 802.1AE)

Type:  int

macSecTciAn[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.macSecTciAn "Link to this definition")  
TCI_AN byte of MACsec header (see IEEE 802.1AE)

Type:  int

macSecTciC[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.macSecTciC "Link to this definition")  
Changed text bit in TCI of MACsec header (see IEEE 802.1AE)

Type:  bool

macSecTciE[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.macSecTciE "Link to this definition")  
Encryption bit in TCI of MACsec header (see IEEE 802.1AE)

Type:  bool

macSecTciEs[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.macSecTciEs "Link to this definition")  
End station bit in TCI of MACsec header (see IEEE 802.1AE)

Type:  bool

macSecTciSc[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.macSecTciSc "Link to this definition")  
SCI indication bit in TCI of MACsec header (see IEEE 802.1AE)

Type:  bool

macSecTciScb[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.macSecTciScb "Link to this definition")  
Single copy broadcast capability bit in TCI of MACsec header (see IEEE 802.1AE)

Type:  bool

macSecTciV[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.macSecTciV "Link to this definition")  
Version bit in TCI of MACsec header (see IEEE 802.1AE)

Type:  bool

parent[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.parent "Link to this definition")  
*Only for pseudo signals in trace analysis!* Returns the parent protocol object if there is one present, otherwise None.

Return type:  [EthernetProtocolBase](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase") | None

ptpControl[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.ptpControl "Link to this definition")  
PTP control field

Type:  int

ptpCorrectionField[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.ptpCorrectionField "Link to this definition")  
PTP correction field

Type:  int

ptpDomainNumber[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.ptpDomainNumber "Link to this definition")  
PTP domain number

Type:  int

ptpFlags[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.ptpFlags "Link to this definition")  
PTP flags

Type:  int

ptpLogMsgInterval[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.ptpLogMsgInterval "Link to this definition")  
PTP log message interval

Type:  int

ptpMsgLen[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.ptpMsgLen "Link to this definition")  
PTP message length

Type:  int

ptpMsgType[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.ptpMsgType "Link to this definition")  
PTP message type

Type:  int

ptpSequenceId[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.ptpSequenceId "Link to this definition")  
PTP sequence ID

Type:  int

ptpSourcePortIdentity[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.ptpSourcePortIdentity "Link to this definition")  
PTP source port identity

Type:  bytes

ptpVersion[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.ptpVersion "Link to this definition")  
PTP version

Type:  int

timestamp[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.timestamp "Link to this definition")  
Receive timestamp in sec., None if not available

Type:  Optional[float]

vlanCfi[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.vlanCfi "Link to this definition")  
802.1a canonical format indicator

Type:  int

vlanCfiOuter[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.vlanCfiOuter "Link to this definition")  
802.1ad canonical format indicator

Type:  int

vlanPcp[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.vlanPcp "Link to this definition")  
802.1a priority code point

Type:  int

vlanPcpOuter[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.vlanPcpOuter "Link to this definition")  
802.1ad priority code point

Type:  int

vlanVid[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.vlanVid "Link to this definition")  
802.1a VLAN id

Type:  int

vlanVidOuter[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.vlanVidOuter "Link to this definition")  
802.1ad VLAN id

Type:  int

#### PacketPdelayRespFollowUp[¶](#packetpdelayrespfollowup "Link to this heading")

*class* PacketPdelayRespFollowUp[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp "Link to this definition")  
In the test case, use `api.Ethernet.PacketPdelayRespFollowUp`; in UserPyModules, use `from tts.lib.ethernet.PacketPtp import PacketPdelayRespFollowUp`.

\<protocol\>  
Equivalent to method [`FindParent(protocol)`](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.FindParent "tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.FindParent"). Direct access to parent protocols. *protocol* is one of [`OsiProtocol`](#tts.lib.ethernet.PacketEthernet.OsiProtocol "tts.lib.ethernet.PacketEthernet.OsiProtocol").

Example: Signal.eth.src provides the source MAC address of the Ethernet protocol layer.

Type:  [`EthernetProtocolBase`](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase")

GetPtpResponseOriginTimestampSec()[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetPtpResponseOriginTimestampSec "Link to this definition")  
Returns:  second portion of the PTP response origin timestamp

Return type:  int

SetPtpResponseOriginTimestampSec(*responseOriginTimestampSec*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetPtpResponseOriginTimestampSec "Link to this definition")  
Parameters:  **responseOriginTimestampSec** (*int*) – second portion of the PTP response origin timestamp

ptpResponseOriginTimestampSec[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.ptpResponseOriginTimestampSec "Link to this definition")  
second portion of the PTP response origin timestamp

Type:  int

GetPtpResponseOriginTimestampNSec()[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetPtpResponseOriginTimestampNSec "Link to this definition")  
Returns:  nanosecond portion of the PTP response origin timestamp

Return type:  int

SetPtpResponseOriginTimestampNSec(*responseOriginTimestampNSec*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetPtpResponseOriginTimestampNSec "Link to this definition")  
Parameters:  **responseOriginTimestampNSec** (*int*) – nanosecond portion of the PTP response origin timestamp

ptpResponseOriginTimestampNSec[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.ptpResponseOriginTimestampNSec "Link to this definition")  
nanosecond portion of the PTP response origin timestamp

Type:  int

GetPtpRequestingPortIdentity()[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetPtpRequestingPortIdentity "Link to this definition")  
Returns:  PTP requesting port identity

Return type:  bytes

SetPtpRequestingPortIdentity(*requestingPortIdentity*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetPtpRequestingPortIdentity "Link to this definition")  
Parameters:  **requestingPortIdentity** (*bytes*) – PTP requesting port identity

ptpRequestingPortIdentity[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.ptpRequestingPortIdentity "Link to this definition")  
PTP requesting port identity

Type:  bytes

FindParent(*protocol*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.FindParent "Link to this definition")  
*Only for pseudo signals in trace analysis!* Returns the requested protocol object if present, otherwise a [`NoProtocol`](#tts.lib.ethernet.PacketEthernet.NoProtocol "tts.lib.ethernet.PacketEthernet.NoProtocol") object.

Parameters:  **protocol** ([*OsiProtocol*](#tts.lib.ethernet.PacketEthernet.OsiProtocol "tts.lib.ethernet.PacketEthernet.OsiProtocol")) – The required protocol name.

Returns:  The required parent protocol object.

Return type:  [EthernetProtocolBase](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase")

GetEthDstMac()[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetEthDstMac "Link to this definition")  
Returns:  target MAC address e.g. DE:AD:BE:EF:FF:00

Return type:  str

GetEthPayload()[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetEthPayload "Link to this definition")  
Returns:  Ethernet payload

Return type:  bytes

GetEthSrcMac()[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetEthSrcMac "Link to this definition")  
Returns:  source MAC address e.g. DE:AD:BE:EF:FF:00

Return type:  str

GetEthType()[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetEthType "Link to this definition")  
Returns:  ethernet protocol type

Return type:  int

GetMacSecAn()[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetMacSecAn "Link to this definition")  
Returns:  Association Number of MACsec header (see IEEE 802.1AE)

Return type:  int

GetMacSecIcv()[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetMacSecIcv "Link to this definition")  
Returns:  Integrity check value of MACsec header (see IEEE 802.1AE)

Return type:  bytes

GetMacSecPn()[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetMacSecPn "Link to this definition")  
Returns:  Packet Number of MACsec header (see IEEE 802.1AE)

Return type:  int

GetMacSecSci()[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetMacSecSci "Link to this definition")  
Returns:  Secure Channel Identifier of MACsec header (see IEEE 802.1AE)

Return type:  bytes

GetMacSecSl()[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetMacSecSl "Link to this definition")  
Returns:  Short Length of MACsec header (see IEEE 802.1AE)

Return type:  int

GetMacSecTci()[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetMacSecTci "Link to this definition")  
Returns:  TAG Control Information of MACsec header (see IEEE 802.1AE)

Return type:  int

GetMacSecTciAn()[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetMacSecTciAn "Link to this definition")  
Returns:  TCI_AN byte of MACsec header (see IEEE 802.1AE)

Return type:  int

GetMacSecTciC()[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetMacSecTciC "Link to this definition")  
Returns:  Changed text bit in TCI of MACsec header (see IEEE 802.1AE)

Return type:  bool

GetMacSecTciE()[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetMacSecTciE "Link to this definition")  
Returns:  Encryption bit in TCI of MACsec header (see IEEE 802.1AE)

Return type:  bool

GetMacSecTciEs()[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetMacSecTciEs "Link to this definition")  
Returns:  End station bit in TCI of MACsec header (see IEEE 802.1AE)

Return type:  bool

GetMacSecTciSc()[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetMacSecTciSc "Link to this definition")  
Returns:  SCI indication bit in TCI of MACsec header (see IEEE 802.1AE)

Return type:  bool

GetMacSecTciScb()[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetMacSecTciScb "Link to this definition")  
Returns:  Single copy broadcast capability bit in TCI of MACsec header (see IEEE 802.1AE)

Return type:  bool

GetMacSecTciV()[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetMacSecTciV "Link to this definition")  
Returns:  Version bit in TCI of MACsec header (see IEEE 802.1AE)

Return type:  bool

GetPtpControl()[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetPtpControl "Link to this definition")  
Returns:  PTP control field

Return type:  int

GetPtpCorrectionField()[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetPtpCorrectionField "Link to this definition")  
Returns:  PTP correction field

Return type:  int

GetPtpDomainNumber()[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetPtpDomainNumber "Link to this definition")  
Returns:  PTP domain number

Return type:  int

GetPtpFlags()[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetPtpFlags "Link to this definition")  
Returns:  PTP flags

Return type:  int

GetPtpLogMsgInterval()[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetPtpLogMsgInterval "Link to this definition")  
Returns:  PTP log message interval

Return type:  int

GetPtpMsgLen()[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetPtpMsgLen "Link to this definition")  
Returns:  PTP message length

Return type:  int

GetPtpMsgType()[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetPtpMsgType "Link to this definition")  
Returns:  PTP message type

Return type:  int

GetPtpSequenceId()[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetPtpSequenceId "Link to this definition")  
Returns:  PTP sequence ID

Return type:  int

GetPtpSourcePortIdentity()[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetPtpSourcePortIdentity "Link to this definition")  
Returns:  PTP source port identity

Return type:  bytes

GetPtpVersion()[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetPtpVersion "Link to this definition")  
Returns:  PTP version

Return type:  int

GetTimestamp()[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetTimestamp "Link to this definition")  
Returns:  Receive timestamp in sec., None if not available

Return type:  float | None

GetVlanCfi(*ixVlanTags*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetVlanCfi "Link to this definition")  
Returns:  802.1a canonical format indicator

Return type:  int

GetVlanCfiOuter(*ixVlanTags*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetVlanCfiOuter "Link to this definition")  
Returns:  802.1ad canonical format indicator

Return type:  int

GetVlanPcp(*ixVlanTags*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetVlanPcp "Link to this definition")  
Returns:  802.1a priority code point

Return type:  int

GetVlanPcpOuter(*ixVlanTags*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetVlanPcpOuter "Link to this definition")  
Returns:  802.1ad priority code point

Return type:  int

GetVlanVid(*ixVlanTags*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetVlanVid "Link to this definition")  
Returns:  802.1a VLAN id

Return type:  int

GetVlanVidOuter(*ixVlanTags*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetVlanVidOuter "Link to this definition")  
Returns:  802.1ad VLAN id

Return type:  int

SetEthDstMac(*mac*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetEthDstMac "Link to this definition")  
Parameters:  **mac** (*str*) – target MAC address e.g. DE:AD:BE:EF:FF:00

SetEthPayload(*payload*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetEthPayload "Link to this definition")  
Parameters:  **payload** (*bytes*) – Ethernet payload

SetEthSrcMac(*mac*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetEthSrcMac "Link to this definition")  
Parameters:  **mac** (*str*) – source MAC addres e.g. DE:AD:BE:EF:FF:00

SetEthType(*ethType*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetEthType "Link to this definition")  
Parameters:  **ethType** (*int*) – ethernet protocol type

SetPtpControl(*control*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetPtpControl "Link to this definition")  
Parameters:  **control** (*int*) – PTP control field

SetPtpCorrectionField(*correctionField*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetPtpCorrectionField "Link to this definition")  
Parameters:  **correctionField** (*int*) – PTP correction field

SetPtpDomainNumber(*domainNumber*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetPtpDomainNumber "Link to this definition")  
Parameters:  **domainNumber** (*int*) – PTP domain number

SetPtpFlags(*flags*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetPtpFlags "Link to this definition")  
Parameters:  **flags** (*int*) – PTP flags

SetPtpLogMsgInterval(*logMsgInterval*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetPtpLogMsgInterval "Link to this definition")  
Parameters:  **logMsgInterval** (*int*) – log message interval

SetPtpMsgLen(*msgLen*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetPtpMsgLen "Link to this definition")  
Parameters:  **msgLen** (*int*) – PTP message length

SetPtpMsgType(*msgType*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetPtpMsgType "Link to this definition")  
Parameters:  **msgType** (*int*) – PTP message type

SetPtpSequenceId(*sequenceId*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetPtpSequenceId "Link to this definition")  
Parameters:  **sequenceId** (*int*) – PTP sequence ID

SetPtpSourcePortIdentity(*sourcePortIdentity*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetPtpSourcePortIdentity "Link to this definition")  
Parameters:  **sourcePortIdentity** (*bytes*) – PTP source port identity

SetPtpVersion(*version*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetPtpVersion "Link to this definition")  
Parameters:  **version** (*int*) – PTP version

SetTimestamp(*timestamp*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetTimestamp "Link to this definition")  
Parameters:  **timestamp** (*float* *|* *None*) – Receive timestamp in sec., None if not available

SetVlanCfi(*cfi*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetVlanCfi "Link to this definition")  
Parameters:  **cfi** (*int*) – 802.1a canonical format indicator

SetVlanCfiOuter(*cfi*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetVlanCfiOuter "Link to this definition")  
Parameters:  **cfi** (*int*) – 802.1ad canonical format indicator

SetVlanPcp(*pcp*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetVlanPcp "Link to this definition")  
Parameters:  **pcp** (*int*) – 802.1a priority code point

SetVlanPcpOuter(*pcp*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetVlanPcpOuter "Link to this definition")  
Parameters:  **pcp** (*int*) – 802.1ad priority code point

SetVlanVid(*vid*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetVlanVid "Link to this definition")  
Parameters:  **vid** (*int*) – 802.1a VLAN id

SetVlanVidOuter(*vid*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetVlanVidOuter "Link to this definition")  
Parameters:  **vid** (*int*) – 802.1ad VLAN id

ethDstMac[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.ethDstMac "Link to this definition")  
target MAC address e.g. DE:AD:BE:EF:FF:00

Type:  str

ethPayload[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.ethPayload "Link to this definition")  
Ethernet payload

Type:  bytes

ethSrcMac[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.ethSrcMac "Link to this definition")  
source MAC address e.g. DE:AD:BE:EF:FF:00

Type:  str

ethType[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.ethType "Link to this definition")  
ethernet protocol type

Type:  int

macSecAn[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.macSecAn "Link to this definition")  
Association Number of MACsec header (see IEEE 802.1AE)

Type:  int

macSecIcv[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.macSecIcv "Link to this definition")  
Integrity check value of MACsec header (see IEEE 802.1AE)

Type:  bytes

macSecPn[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.macSecPn "Link to this definition")  
Packet Number of MACsec header (see IEEE 802.1AE)

Type:  int

macSecSci[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.macSecSci "Link to this definition")  
Secure Channel Identifier of MACsec header (see IEEE 802.1AE)

Type:  bytes

macSecSl[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.macSecSl "Link to this definition")  
Short Length of MACsec header (see IEEE 802.1AE)

Type:  int

macSecTci[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.macSecTci "Link to this definition")  
TAG Control Information of MACsec header (see IEEE 802.1AE)

Type:  int

macSecTciAn[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.macSecTciAn "Link to this definition")  
TCI_AN byte of MACsec header (see IEEE 802.1AE)

Type:  int

macSecTciC[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.macSecTciC "Link to this definition")  
Changed text bit in TCI of MACsec header (see IEEE 802.1AE)

Type:  bool

macSecTciE[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.macSecTciE "Link to this definition")  
Encryption bit in TCI of MACsec header (see IEEE 802.1AE)

Type:  bool

macSecTciEs[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.macSecTciEs "Link to this definition")  
End station bit in TCI of MACsec header (see IEEE 802.1AE)

Type:  bool

macSecTciSc[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.macSecTciSc "Link to this definition")  
SCI indication bit in TCI of MACsec header (see IEEE 802.1AE)

Type:  bool

macSecTciScb[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.macSecTciScb "Link to this definition")  
Single copy broadcast capability bit in TCI of MACsec header (see IEEE 802.1AE)

Type:  bool

macSecTciV[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.macSecTciV "Link to this definition")  
Version bit in TCI of MACsec header (see IEEE 802.1AE)

Type:  bool

parent[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.parent "Link to this definition")  
*Only for pseudo signals in trace analysis!* Returns the parent protocol object if there is one present, otherwise None.

Return type:  [EthernetProtocolBase](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase") | None

ptpControl[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.ptpControl "Link to this definition")  
PTP control field

Type:  int

ptpCorrectionField[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.ptpCorrectionField "Link to this definition")  
PTP correction field

Type:  int

ptpDomainNumber[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.ptpDomainNumber "Link to this definition")  
PTP domain number

Type:  int

ptpFlags[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.ptpFlags "Link to this definition")  
PTP flags

Type:  int

ptpLogMsgInterval[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.ptpLogMsgInterval "Link to this definition")  
PTP log message interval

Type:  int

ptpMsgLen[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.ptpMsgLen "Link to this definition")  
PTP message length

Type:  int

ptpMsgType[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.ptpMsgType "Link to this definition")  
PTP message type

Type:  int

ptpSequenceId[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.ptpSequenceId "Link to this definition")  
PTP sequence ID

Type:  int

ptpSourcePortIdentity[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.ptpSourcePortIdentity "Link to this definition")  
PTP source port identity

Type:  bytes

ptpVersion[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.ptpVersion "Link to this definition")  
PTP version

Type:  int

timestamp[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.timestamp "Link to this definition")  
Receive timestamp in sec., None if not available

Type:  Optional[float]

vlanCfi[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.vlanCfi "Link to this definition")  
802.1a canonical format indicator

Type:  int

vlanCfiOuter[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.vlanCfiOuter "Link to this definition")  
802.1ad canonical format indicator

Type:  int

vlanPcp[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.vlanPcp "Link to this definition")  
802.1a priority code point

Type:  int

vlanPcpOuter[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.vlanPcpOuter "Link to this definition")  
802.1ad priority code point

Type:  int

vlanVid[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.vlanVid "Link to this definition")  
802.1a VLAN id

Type:  int

vlanVidOuter[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.vlanVidOuter "Link to this definition")  
802.1ad VLAN id

Type:  int

### SOME/IP[¶](#some-ip "Link to this heading")

Note

If your code uses getters and/or setter methods, you should probably convert it to use the properties as documented below, but for the time being it will continue to work.

#### PacketSomeIp[¶](#packetsomeip "Link to this heading")

*class* PacketSomeIp[¶](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp "Link to this definition")  
In the test case, use `api.Ethernet.PacketSomeIp`; in UserPyModules, use `from tts.lib.ethernet.PacketSomeIp import PacketSomeIp`.

SOMEIP_MSG_REQUEST *= 0*[¶](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.SOMEIP_MSG_REQUEST "Link to this definition")  

SOMEIP_MSG_REQUEST_NO_RETURN *= 1*[¶](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.SOMEIP_MSG_REQUEST_NO_RETURN "Link to this definition")  

SOMEIP_MSG_NOTIFICATION *= 2*[¶](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.SOMEIP_MSG_NOTIFICATION "Link to this definition")  

SOMEIP_MSG_TP *= 32*[¶](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.SOMEIP_MSG_TP "Link to this definition")  

SOMEIP_MSG_RESPONSE *= 128*[¶](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.SOMEIP_MSG_RESPONSE "Link to this definition")  

SOMEIP_MSG_ERROR *= 129*[¶](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.SOMEIP_MSG_ERROR "Link to this definition")  

SOMEIP_RETURN_OK *= 0*[¶](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.SOMEIP_RETURN_OK "Link to this definition")  

SOMEIP_RETURN_NOT_OK *= 1*[¶](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.SOMEIP_RETURN_NOT_OK "Link to this definition")  

SOMEIP_RETURN_UNKNOWN_SERVICE *= 2*[¶](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.SOMEIP_RETURN_UNKNOWN_SERVICE "Link to this definition")  

SOMEIP_RETURN_UNKNOWN_METHOD *= 3*[¶](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.SOMEIP_RETURN_UNKNOWN_METHOD "Link to this definition")  

SOMEIP_RETURN_NOT_READY *= 4*[¶](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.SOMEIP_RETURN_NOT_READY "Link to this definition")  

SOMEIP_RETURN_NOT_REACHABLE *= 5*[¶](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.SOMEIP_RETURN_NOT_REACHABLE "Link to this definition")  

SOMEIP_RETURN_TIMEOUT *= 6*[¶](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.SOMEIP_RETURN_TIMEOUT "Link to this definition")  

SOMEIP_RETURN_WRONG_PROTOCOL_VERSION *= 7*[¶](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.SOMEIP_RETURN_WRONG_PROTOCOL_VERSION "Link to this definition")  

SOMEIP_RETURN_WRONG_INTERFACE_VERSION *= 8*[¶](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.SOMEIP_RETURN_WRONG_INTERFACE_VERSION "Link to this definition")  

SOMEIP_RETURN_MALFORMED *= 9*[¶](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.SOMEIP_RETURN_MALFORMED "Link to this definition")  

SOMEIP_RETURN_TCP_ERROR *= 10*[¶](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.SOMEIP_RETURN_TCP_ERROR "Link to this definition")  

*classmethod* GetSomeIpMessagesFromPayload(*data: bytes*) → list[[PacketSomeIp](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp "tts.lib.ethernet.PacketSomeIp.PacketSomeIp")][¶](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.GetSomeIpMessagesFromPayload "Link to this definition")  
Creates one or multiple SOME/IP packets from data.

\<protocol\>  
Equivalent to method [`FindParent(protocol)`](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.FindParent "tts.lib.ethernet.PacketSomeIp.PacketSomeIp.FindParent"). Direct access to parent protocols. *protocol* is one of [`OsiProtocol`](#tts.lib.ethernet.PacketEthernet.OsiProtocol "tts.lib.ethernet.PacketEthernet.OsiProtocol").

Example: Signal.eth.src provides the source MAC address of the Ethernet protocol layer.

Type:  [`EthernetProtocolBase`](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase")

*classmethod* Create(*serviceId=0*, *methodId=0*, *clientId=0*, *sessionId=0*, *protocolVersion=1*, *interfaceVersion=1*, *messageType=0*, *returnCode=0*, *payload=None*, *length='Auto'*, *messageId=None*, *requestId=None*)[¶](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.Create "Link to this definition")  
Returns a PacketSomeIp object as specified. If a messageId is given, any given serviceId and methodId will be overwritten. If a requestId is given, any given clientId and sessionId will be overwritten.

Parameters:  - **serviceId** (*int,* *optional*) – defaults to 0x00

- **methodId** (*int,* *optional*) – defaults to 0x00

- **clientId** (*int,* *optional*) – defaults to 0x00

- **sessionId** (*int,* *optional*) – defaults to 0x00

- **protocolVersion** (*int,* *optional*) – defaults to 0x01

- **interfaceVersion** (*int,* *optional*) – defaults to 0x01

- **messageType** (*int* *|* *str,* *optional*) – defaults to [`api.Ethernet.PacketSomeIp.SOMEIP_MSG_REQUEST`](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.SOMEIP_MSG_REQUEST "tts.lib.ethernet.PacketSomeIp.PacketSomeIp.SOMEIP_MSG_REQUEST")

- **returnCode** (*int* *|* *str,* *optional*) – defaults to [`api.Ethernet.PacketSomeIp.SOMEIP_RETURN_OK`](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.SOMEIP_RETURN_OK "tts.lib.ethernet.PacketSomeIp.PacketSomeIp.SOMEIP_RETURN_OK")

- **payload** (*bytes* *|* [*ByteStream*](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream") *|* *None,* *optional*) – defaults to None

- **length** (*int,* *optional*) – defaults to ‘Auto’

- **messageId** (*int* *|* *None,* *optional*) – defaults to None

- **requestId** (*int* *|* *None,* *optional*) – defaults to None

Returns:  PacketSomeIp object

Return type:  [`PacketSomeIp`](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp "tts.lib.ethernet.PacketSomeIp.PacketSomeIp")

CalcLen()[¶](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.CalcLen "Link to this definition")  
Calculate and set the current length of this SOME/IP packet

messageId[¶](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.messageId "Link to this definition")  
message id

Type:  int

serviceId[¶](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.serviceId "Link to this definition")  
service id (highest 16 bit from message id)

Type:  int

methodId[¶](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.methodId "Link to this definition")  
method id (lowest 16 bit from message id)

Type:  int

length[¶](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.length "Link to this definition")  
length from this header position

Type:  int

requestId[¶](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.requestId "Link to this definition")  
request id

Type:  int

clientId[¶](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.clientId "Link to this definition")  
client id (highest 16 bit from request id)

Type:  int

sessionId[¶](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.sessionId "Link to this definition")  
session id (lowest 16 bit from request id)

Type:  int

protocolVersion[¶](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.protocolVersion "Link to this definition")  
protocol version

Type:  int

interfaceVersion[¶](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.interfaceVersion "Link to this definition")  
interface version

Type:  int

messageType[¶](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.messageType "Link to this definition")  
message type

Type:  int

returnCode[¶](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.returnCode "Link to this definition")  
return code

Type:  int

payload[¶](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.payload "Link to this definition")  
payload for this packet

Type:  bytes

GetHeaderBytes()[¶](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.GetHeaderBytes "Link to this definition")  
Returns:  the header (cached)

Return type:  bytes

instanceIds[¶](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.instanceIds "Link to this definition")  
Return type:  set

FindParent(*protocol*)[¶](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.FindParent "Link to this definition")  
*Only for pseudo signals in trace analysis!* Returns the requested protocol object if present, otherwise a [`NoProtocol`](#tts.lib.ethernet.PacketEthernet.NoProtocol "tts.lib.ethernet.PacketEthernet.NoProtocol") object.

Parameters:  **protocol** ([*OsiProtocol*](#tts.lib.ethernet.PacketEthernet.OsiProtocol "tts.lib.ethernet.PacketEthernet.OsiProtocol")) – The required protocol name.

Returns:  The required parent protocol object.

Return type:  [EthernetProtocolBase](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase")

parent[¶](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.parent "Link to this definition")  
*Only for pseudo signals in trace analysis!* Returns the parent protocol object if there is one present, otherwise None.

Return type:  [EthernetProtocolBase](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase") | None

timestamp[¶](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.timestamp "Link to this definition")  
Receive timestamp in sec., None if not available

Type:  Optional[float]

#### PacketSomeIpSd[¶](#packetsomeipsd "Link to this heading")

*class* PacketSomeIpSd[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSd "Link to this definition")  
In the test case, use `api.Ethernet.PacketSomeIpSd`; in UserPyModules, use `from tts.lib.ethernet.PacketSomeIpSd import PacketSomeIpSd`.

`\_\_init\_\_`(*self*, *data: bytes | None = None*) → [PacketSomeIpSd](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSd "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSd")[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSd.__init__ "Link to this definition")  
Create a [`PacketSomeIpSd`](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSd "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSd") instance. Either from an existing payload, or empty.

\<protocol\>  
Equivalent to method [`FindParent(protocol)`](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSd.FindParent "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSd.FindParent"). Direct access to parent protocols. *protocol* is one of [`OsiProtocol`](#tts.lib.ethernet.PacketEthernet.OsiProtocol "tts.lib.ethernet.PacketEthernet.OsiProtocol").

Example: Signal.eth.src provides the source MAC address of the Ethernet protocol layer.

Type:  [`EthernetProtocolBase`](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase")

CalcEntryArrayLen()[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSd.CalcEntryArrayLen "Link to this definition")  
Calculate and set the current length of all entries

CalcOptionArrayLen()[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSd.CalcOptionArrayLen "Link to this definition")  
Calculate and set the current length of all options

*classmethod* Create(*rebootFlag=True*, *unicastFlag=True*, *entryList=None*, *optionList=None*, *entryArrayLength='Auto'*, *optionArrayLength='Auto'*)[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSd.Create "Link to this definition")  
Returns a PacketSomeIpSd object as specified.

Parameters:  - **rebootFlag** (*bool* *|* *int,* *optional*) – defaults to True

- **unicastFlag** (*bool* *|* *int,* *optional*) – defaults to True

- **entryList** (list[[`PacketSomeIpSdEntry`](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntry "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntry")] | None, optional) – defaults to None

- **optionList** (list[[`PacketSomeIpSdOption`](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOption "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOption")] | None, optional) – defaults to None

- **entryArrayLength** (*int,* *optional*) – defaults to “Auto”

- **optionArrayLength** (*int,* *optional*) – defaults to “Auto”

Returns:  PacketSomeIpSd object

Return type:  [`PacketSomeIpSd`](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSd "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSd")

FindParent(*protocol*)[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSd.FindParent "Link to this definition")  
*Only for pseudo signals in trace analysis!* Returns the requested protocol object if present, otherwise a [`NoProtocol`](#tts.lib.ethernet.PacketEthernet.NoProtocol "tts.lib.ethernet.PacketEthernet.NoProtocol") object.

Parameters:  **protocol** ([*OsiProtocol*](#tts.lib.ethernet.PacketEthernet.OsiProtocol "tts.lib.ethernet.PacketEthernet.OsiProtocol")) – The required protocol name.

Returns:  The required parent protocol object.

Return type:  [EthernetProtocolBase](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase")

entryLen[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSd.entryLen "Link to this definition")  
length of all entries in bytes

Type:  int

entryList[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSd.entryList "Link to this definition")  
list of all SOME/IP-SD entries

Type:  list[[PacketSomeIpSdEntry](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntry "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntry")]

optionLen[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSd.optionLen "Link to this definition")  
length of all options in bytes

Type:  int

optionList[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSd.optionList "Link to this definition")  
list of all SOME/IP-SD options

Type:  list

parent[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSd.parent "Link to this definition")  
*Only for pseudo signals in trace analysis!* Returns the parent protocol object if there is one present, otherwise None.

Return type:  [EthernetProtocolBase](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase") | None

rebootFlag[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSd.rebootFlag "Link to this definition")  
reboot flag

Type:  bool

timestamp[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSd.timestamp "Link to this definition")  
Receive timestamp in sec., None if not available

Type:  Optional[float]

unicastFlag[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSd.unicastFlag "Link to this definition")  
unicast flag

Type:  bool

#### PacketSomeIpSdEntry[¶](#packetsomeipsdentry "Link to this heading")

*class* PacketSomeIpSdEntry[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntry "Link to this definition")  
In the test case, use `api.Ethernet.PacketSomeIpSdEntry`; in UserPyModules, use `from tts.lib.ethernet.PacketSomeIpSd import PacketSomeIpSdEntry`.

index1[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntry.index1 "Link to this definition")  
first option index

Type:  int

index2[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntry.index2 "Link to this definition")  
second option index

Type:  int

instanceId[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntry.instanceId "Link to this definition")  
instance id

Type:  int

majorVersion[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntry.majorVersion "Link to this definition")  
major version

Type:  int

optionCount1[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntry.optionCount1 "Link to this definition")  
first option count

Type:  int

optionCount2[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntry.optionCount2 "Link to this definition")  
second option count

Type:  int

serviceId[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntry.serviceId "Link to this definition")  
service id

Type:  int

ttl[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntry.ttl "Link to this definition")  
Time to live (TTL)

Type:  int

type[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntry.type "Link to this definition")  
entry type

Type:  int

#### PacketSomeIpSdEntryService[¶](#packetsomeipsdentryservice "Link to this heading")

*class* PacketSomeIpSdEntryService[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryService "Link to this definition")  
Bases: [`PacketSomeIpSdEntry`](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntry "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntry")

In the test case, use `api.Ethernet.PacketSomeIpSdEntryService`; in UserPyModules, use `from tts.lib.ethernet.PacketSomeIpSd import PacketSomeIpSdEntryService`.

SERVICE_FIND *= 0*[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryService.SERVICE_FIND "Link to this definition")  

SERVICE_OFFER *= 1*[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryService.SERVICE_OFFER "Link to this definition")  

SERVICE_STOP_OFFER *= 1*[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryService.SERVICE_STOP_OFFER "Link to this definition")  

*classmethod* Create(*index1=0*, *index2=0*, *instanceId=1*, *majorVersion=1*, *minorVersion=0*, *optionCount1=0*, *optionCount2=0*, *serviceId=0*, *ttl=0*, *type=1*)[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryService.Create "Link to this definition")  
Returns a PacketSomeIpSdEntryService object as specified.

Parameters:  - **index1** (*int,* *optional*) – defaults to 0

- **index2** (*int,* *optional*) – defaults to 0

- **instanceId** (*int,* *optional*) – defaults to 1

- **majorVersion** (*int,* *optional*) – defaults to 1

- **minorVersion** (*int,* *optional*) – defaults to 0

- **optionCount1** (*int,* *optional*) – defaults to 0

- **optionCount2** (*int,* *optional*) – defaults to 0

- **serviceId** (*int,* *optional*) – defaults to 0

- **ttl** (*int,* *optional*) – defaults to 0

- **type** (*int,* *optional*) – defaults to [`api.Ethernet.PacketSomeIpSdEntryService.SERVICE_OFFER`](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryService.SERVICE_OFFER "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryService.SERVICE_OFFER")

Returns:  PacketSomeIpSdEntryService object

Return type:  [`PacketSomeIpSdEntryService`](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryService "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryService")

minorVersion[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryService.minorVersion "Link to this definition")  
minor version

Type:  int

#### PacketSomeIpSdEntryEventgroup[¶](#packetsomeipsdentryeventgroup "Link to this heading")

*class* PacketSomeIpSdEntryEventgroup[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryEventgroup "Link to this definition")  
Bases: [`PacketSomeIpSdEntry`](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntry "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntry")

In the test case, use `api.Ethernet.PacketSomeIpSdEntryEventgroup`; in UserPyModules, use `from tts.lib.ethernet.PacketSomeIpSd import PacketSomeIpSdEntryEventgroup`.

EVENTGROUP_SUBSCRIBE *= 6*[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryEventgroup.EVENTGROUP_SUBSCRIBE "Link to this definition")  

EVENTGROUP_SUBSCRIBE_ACK *= 7*[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryEventgroup.EVENTGROUP_SUBSCRIBE_ACK "Link to this definition")  

EVENTGROUP_STOP_SUBSCRIBE *= 6*[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryEventgroup.EVENTGROUP_STOP_SUBSCRIBE "Link to this definition")  

EVENTGROUP_SUBSCRIBE_NACK *= 7*[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryEventgroup.EVENTGROUP_SUBSCRIBE_NACK "Link to this definition")  

*classmethod* Create(*eventgroupId=0*, *index1=0*, *index2=0*, *instanceId=1*, *majorVersion=1*, *optionCount1=0*, *optionCount2=0*, *serviceId=0*, *ttl=0*, *type=6*)[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryEventgroup.Create "Link to this definition")  
Returns a PacketSomeIpSdEntryEventgroup object as specified.

Parameters:  - **eventgroupId** (*int,* *optional*) – defaults to 0

- **index1** (*int,* *optional*) – defaults to 0

- **index2** (*int,* *optional*) – defaults to 0

- **instanceId** (*int,* *optional*) – defaults to 1

- **majorVersion** (*int,* *optional*) – defaults to 1

- **optionCount1** (*int,* *optional*) – defaults to 0

- **optionCount2** (*int,* *optional*) – defaults to 0

- **serviceId** (*int,* *optional*) – defaults to 0

- **ttl** (*int,* *optional*) – defaults to 0

- **type** (*int,* *optional*) – defaults to [`api.Ethernet.PacketSomeIpSdEntryEventgroup.EVENTGROUP_SUBSCRIBE`](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryEventgroup.EVENTGROUP_SUBSCRIBE "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryEventgroup.EVENTGROUP_SUBSCRIBE")

- **validityCheck** (*bool,* *optional*) – defaults to False

Returns:  PacketSomeIpSdEntryEventgroup object

Return type:  [`PacketSomeIpSdEntryEventgroup`](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryEventgroup "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryEventgroup")

eventgroupId[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryEventgroup.eventgroupId "Link to this definition")  
eventgroup id

Type:  int

#### PacketSomeIpSdOption[¶](#packetsomeipsdoption "Link to this heading")

*class* PacketSomeIpSdOption[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOption "Link to this definition")  
In the test case, use `api.Ethernet.PacketSomeIpSdOption`; in UserPyModules, use `from tts.lib.ethernet.PacketSomeIpSd import PacketSomeIpSdOption`.

TRANSPORT_TCP *= 6*[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOption.TRANSPORT_TCP "Link to this definition")  

TRANSPORT_UDP *= 17*[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOption.TRANSPORT_UDP "Link to this definition")  

PACKET_SOME_IP_SD_OPTION_CONFIG *= 1*[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOption.PACKET_SOME_IP_SD_OPTION_CONFIG "Link to this definition")  

PACKET_SOME_IP_SD_OPTION_IPV4 *= 4*[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOption.PACKET_SOME_IP_SD_OPTION_IPV4 "Link to this definition")  

PACKET_SOME_IP_SD_OPTION_IPV6 *= 6*[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOption.PACKET_SOME_IP_SD_OPTION_IPV6 "Link to this definition")  

PACKET_SOME_IP_SD_OPTION_IPV4_MULTICAST *= 20*[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOption.PACKET_SOME_IP_SD_OPTION_IPV4_MULTICAST "Link to this definition")  

PACKET_SOME_IP_SD_OPTION_IPV4_SD *= 36*[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOption.PACKET_SOME_IP_SD_OPTION_IPV4_SD "Link to this definition")  

PACKET_SOME_IP_SD_OPTION_IPV6_MULTICAST *= 22*[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOption.PACKET_SOME_IP_SD_OPTION_IPV6_MULTICAST "Link to this definition")  

PACKET_SOME_IP_SD_OPTION_IPV6_SD *= 38*[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOption.PACKET_SOME_IP_SD_OPTION_IPV6_SD "Link to this definition")  

optionLen[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOption.optionLen "Link to this definition")  
length of this option from reserved field

Type:  int

type[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOption.type "Link to this definition")  
option type

Type:  int

#### PacketSomeIpSdOptionIpv4[¶](#packetsomeipsdoptionipv4 "Link to this heading")

*class* PacketSomeIpSdOptionIpv4[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4 "Link to this definition")  
Bases: [`PacketSomeIpSdOption`](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOption "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOption")

In the test case, use `api.Ethernet.PacketSomeIpSdOptionIpv4`; in UserPyModules, use `from tts.lib.ethernet.PacketSomeIpSd import PacketSomeIpSdOptionIpv4`.

*classmethod* Create(*ip='127.0.0.1'*, *port=1234*, *protocol=17*, *optionLength='Auto'*)[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4.Create "Link to this definition")  
Returns a PacketSomeIpSdOptionIpv4 object as specified.

Parameters:  - **ip** (*str,* *optional*) – defaults to ‘127.0.0.1’

- **port** (*int,* *optional*) – defaults to 1234

- **protocol** (*int,* *optional*) – defaults to [`api.Ethernet.UDP`](#tts.core.api.internalApi.Ethernet.Ethernet.UDP "tts.core.api.internalApi.Ethernet.Ethernet.UDP")

- **optionLength** (*int,* *optional*) – defaults to “Auto”

Returns:  PacketSomeIpSdOptionIpv4 object

Return type:  [`PacketSomeIpSdOptionIpv4`](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4 "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4")

ip[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4.ip "Link to this definition")  
IPv4 address, format 127.0.0.1

Type:  str

optionLen[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4.optionLen "Link to this definition")  
length of this option from reserved field

Type:  int

port[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4.port "Link to this definition")  
transport layer port

Type:  int

protocol[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4.protocol "Link to this definition")  
> transport layer protocol - [`api.Ethernet.UDP`](#tts.core.api.internalApi.Ethernet.Ethernet.UDP "tts.core.api.internalApi.Ethernet.Ethernet.UDP"), [`api.Ethernet.TCP`](#tts.core.api.internalApi.Ethernet.Ethernet.TCP "tts.core.api.internalApi.Ethernet.Ethernet.TCP")

Type:  int

#### PacketSomeIpSdOptionIpv6[¶](#packetsomeipsdoptionipv6 "Link to this heading")

*class* PacketSomeIpSdOptionIpv6[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6 "Link to this definition")  
Bases: [`PacketSomeIpSdOption`](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOption "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOption")

In the test case, use `api.Ethernet.PacketSomeIpSdOptionIpv6`; in UserPyModules, use `from tts.lib.ethernet.PacketSomeIpSd import PacketSomeIpSdOptionIpv6`.

*classmethod* Create(*ip='::1'*, *port=1234*, *protocol=17*, *optionLength='Auto'*)[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6.Create "Link to this definition")  
Returns a PacketSomeIpSdEntryService object as specified

Parameters:  - **ip** (*str,* *optional*) – defaults to ‘::1’

- **port** (*int,* *optional*) – defaults to 1234

- **protocol** (*int,* *optional*) – defaults to [`api.Ethernet.UDP`](#tts.core.api.internalApi.Ethernet.Ethernet.UDP "tts.core.api.internalApi.Ethernet.Ethernet.UDP")

- **optionLength** (*int,* *optional*) – defaults to “Auto”

Returns:  PacketSomeIpSdOptionIpv6 object

Return type:  [`PacketSomeIpSdOptionIpv6`](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6 "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6")

ip[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6.ip "Link to this definition")  
IPv6 address, format 2001:0db8:85a3:08d3:1319:8a2e:0370:7344

Type:  str

optionLen[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6.optionLen "Link to this definition")  
length of this option from reserved field

Type:  int

port[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6.port "Link to this definition")  
transport layer port

Type:  int

protocol[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6.protocol "Link to this definition")  
> transport layer protocol - [`api.Ethernet.UDP`](#tts.core.api.internalApi.Ethernet.Ethernet.UDP "tts.core.api.internalApi.Ethernet.Ethernet.UDP"), [`api.Ethernet.TCP`](#tts.core.api.internalApi.Ethernet.Ethernet.TCP "tts.core.api.internalApi.Ethernet.Ethernet.TCP")

Type:  int

#### PacketSomeIpSdOptionIpv4Multicast[¶](#packetsomeipsdoptionipv4multicast "Link to this heading")

*class* PacketSomeIpSdOptionIpv4Multicast[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4Multicast "Link to this definition")  
Bases: [`PacketSomeIpSdOptionIpv4`](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4 "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4")

In the test case, use `api.Ethernet.PacketSomeIpSdOptionIpv4Multicast`; in UserPyModules, use `from tts.lib.ethernet.PacketSomeIpSd import PacketSomeIpSdOptionIpv4Multicast`.

*classmethod* Create(*ip='127.0.0.1'*, *port=1234*, *protocol=17*, *optionLength='Auto'*)[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4Multicast.Create "Link to this definition")  
Returns a PacketSomeIpSdOptionIpv4Multicast object as specified.

Parameters:  - **ip** (*str,* *optional*) – defaults to ‘127.0.0.1’

- **port** (*int,* *optional*) – defaults to 1234

- **protocol** (*int,* *optional*) – defaults to [`api.Ethernet.UDP`](#tts.core.api.internalApi.Ethernet.Ethernet.UDP "tts.core.api.internalApi.Ethernet.Ethernet.UDP")

- **optionLength** (*int,* *optional*) – defaults to “Auto”

Returns:  PacketSomeIpSdOptionIpv4Multicast object

Return type:  [`PacketSomeIpSdOptionIpv4Multicast`](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4Multicast "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4Multicast")

ip[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4Multicast.ip "Link to this definition")  
IPv4 address, format 127.0.0.1

Type:  str

optionLen[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4Multicast.optionLen "Link to this definition")  
length of this option from reserved field

Type:  int

port[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4Multicast.port "Link to this definition")  
transport layer port

Type:  int

protocol[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4Multicast.protocol "Link to this definition")  
> transport layer protocol - [`api.Ethernet.UDP`](#tts.core.api.internalApi.Ethernet.Ethernet.UDP "tts.core.api.internalApi.Ethernet.Ethernet.UDP"), [`api.Ethernet.TCP`](#tts.core.api.internalApi.Ethernet.Ethernet.TCP "tts.core.api.internalApi.Ethernet.Ethernet.TCP")

Type:  int

#### PacketSomeIpSdOptionIpv6Multicast[¶](#packetsomeipsdoptionipv6multicast "Link to this heading")

*class* PacketSomeIpSdOptionIpv6Multicast[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6Multicast "Link to this definition")  
Bases: [`PacketSomeIpSdOptionIpv6`](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6 "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6")

In the test case, use `api.Ethernet.PacketSomeIpSdOptionIpv6Multicast`; in UserPyModules, use `from tts.lib.ethernet.PacketSomeIpSd import PacketSomeIpSdOptionIpv6Multicast`.

*classmethod* Create(*ip='::1'*, *port=1234*, *protocol=17*, *optionLength='Auto'*)[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6Multicast.Create "Link to this definition")  
Returns a PacketSomeIpSdOptionIpv6Multicast object as specified.

Parameters:  - **ip** (*str,* *optional*) – defaults to ‘::1’

- **port** (*int,* *optional*) – defaults to 1234

- **protocol** (*int,* *optional*) – defaults to [`api.Ethernet.UDP`](#tts.core.api.internalApi.Ethernet.Ethernet.UDP "tts.core.api.internalApi.Ethernet.Ethernet.UDP")

- **optionLength** (*int,* *optional*) – defaults to “Auto”

Returns:  PacketSomeIpSdOptionIpv6Multicast object

Return type:  [`PacketSomeIpSdOptionIpv6Multicast`](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6Multicast "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6Multicast")

ip[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6Multicast.ip "Link to this definition")  
IPv6 address, format 2001:0db8:85a3:08d3:1319:8a2e:0370:7344

Type:  str

optionLen[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6Multicast.optionLen "Link to this definition")  
length of this option from reserved field

Type:  int

port[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6Multicast.port "Link to this definition")  
transport layer port

Type:  int

protocol[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6Multicast.protocol "Link to this definition")  
> transport layer protocol - [`api.Ethernet.UDP`](#tts.core.api.internalApi.Ethernet.Ethernet.UDP "tts.core.api.internalApi.Ethernet.Ethernet.UDP"), [`api.Ethernet.TCP`](#tts.core.api.internalApi.Ethernet.Ethernet.TCP "tts.core.api.internalApi.Ethernet.Ethernet.TCP")

Type:  int

#### PacketSomeIpSdOptionIpv4SD[¶](#packetsomeipsdoptionipv4sd "Link to this heading")

*class* PacketSomeIpSdOptionIpv4SD[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4SD "Link to this definition")  
Bases: [`PacketSomeIpSdOptionIpv4`](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4 "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4")

In the test case, use `api.Ethernet.PacketSomeIpSdOptionIpv4SD`; in UserPyModules, use `from tts.lib.ethernet.PacketSomeIpSd import PacketSomeIpSdOptionIpv4SD`.

*classmethod* Create(*ip='127.0.0.1'*, *port=1234*, *protocol=17*, *optionLength='Auto'*)[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4SD.Create "Link to this definition")  
Returns a PacketSomeIpSdOptionIpv4 object as specified.

Parameters:  - **ip** (*str,* *optional*) – defaults to ‘127.0.0.1’

- **port** (*int,* *optional*) – defaults to 1234

- **protocol** (*int,* *optional*) – defaults to [`api.Ethernet.UDP`](#tts.core.api.internalApi.Ethernet.Ethernet.UDP "tts.core.api.internalApi.Ethernet.Ethernet.UDP")

- **optionLength** (*int,* *optional*) – defaults to “Auto”

Returns:  PacketSomeIpSdOptionIpv4 object

Return type:  [`PacketSomeIpSdOptionIpv4`](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4 "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4")

ip[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4SD.ip "Link to this definition")  
IPv4 address, format 127.0.0.1

Type:  str

optionLen[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4SD.optionLen "Link to this definition")  
length of this option from reserved field

Type:  int

port[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4SD.port "Link to this definition")  
transport layer port

Type:  int

protocol[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4SD.protocol "Link to this definition")  
> transport layer protocol - [`api.Ethernet.UDP`](#tts.core.api.internalApi.Ethernet.Ethernet.UDP "tts.core.api.internalApi.Ethernet.Ethernet.UDP"), [`api.Ethernet.TCP`](#tts.core.api.internalApi.Ethernet.Ethernet.TCP "tts.core.api.internalApi.Ethernet.Ethernet.TCP")

Type:  int

#### PacketSomeIpSdOptionIpv6SD[¶](#packetsomeipsdoptionipv6sd "Link to this heading")

*class* PacketSomeIpSdOptionIpv6SD[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6SD "Link to this definition")  
Bases: [`PacketSomeIpSdOptionIpv6`](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6 "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6")

In the test case, use `api.Ethernet.PacketSomeIpSdOptionIpv6SD`; in UserPyModules, use `from tts.lib.ethernet.PacketSomeIpSd import PacketSomeIpSdOptionIpv6SD`.

*classmethod* Create(*ip='::1'*, *port=1234*, *protocol=17*, *optionLength='Auto'*)[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6SD.Create "Link to this definition")  
Returns a PacketSomeIpSdEntryService object as specified

Parameters:  - **ip** (*str,* *optional*) – defaults to ‘::1’

- **port** (*int,* *optional*) – defaults to 1234

- **protocol** (*int,* *optional*) – defaults to [`api.Ethernet.UDP`](#tts.core.api.internalApi.Ethernet.Ethernet.UDP "tts.core.api.internalApi.Ethernet.Ethernet.UDP")

- **optionLength** (*int,* *optional*) – defaults to “Auto”

Returns:  PacketSomeIpSdOptionIpv6 object

Return type:  [`PacketSomeIpSdOptionIpv6`](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6 "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6")

ip[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6SD.ip "Link to this definition")  
IPv6 address, format 2001:0db8:85a3:08d3:1319:8a2e:0370:7344

Type:  str

optionLen[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6SD.optionLen "Link to this definition")  
length of this option from reserved field

Type:  int

port[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6SD.port "Link to this definition")  
transport layer port

Type:  int

protocol[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6SD.protocol "Link to this definition")  
> transport layer protocol - [`api.Ethernet.UDP`](#tts.core.api.internalApi.Ethernet.Ethernet.UDP "tts.core.api.internalApi.Ethernet.Ethernet.UDP"), [`api.Ethernet.TCP`](#tts.core.api.internalApi.Ethernet.Ethernet.TCP "tts.core.api.internalApi.Ethernet.Ethernet.TCP")

Type:  int

#### PacketSomeIpSdOptionConfig[¶](#packetsomeipsdoptionconfig "Link to this heading")

*class* PacketSomeIpSdOptionConfig[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionConfig "Link to this definition")  
Bases: [`PacketSomeIpSdOption`](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOption "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOption")

In the test case, use `api.Ethernet.PacketSomeIpSdOptionConfig`; in UserPyModules, use `from tts.lib.ethernet.PacketSomeIpSd import PacketSomeIpSdOptionConfig`.

*classmethod* Create(*config*, *optionLength='Auto'*)[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionConfig.Create "Link to this definition")  
Returns a PacketSomeIpSdOptionConfig object as specified.

Parameters:  - **config** (*dict,* *(format: {id1: value1,* *id2: value2,* *...})*) – configuration parameters as dictionary

- **optionLength** (*int,* *optional*) – defaults to “Auto”

Returns:  PacketSomeIpSdOptionConfig object

Return type:  [`PacketSomeIpSdOptionConfig`](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionConfig "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionConfig")

config[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionConfig.config "Link to this definition")  
configuration parameter as dictionary (format: {id1: value1, id: value2, …})

Type:  dict

optionLen[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionConfig.optionLen "Link to this definition")  
length of this option from reserved field

Type:  int

# Bus related objects of trace analysis[¶](#bus-related-objects-of-trace-analysis "Link to this heading")

The following bus objects are supported for ASC recordings.

## CAN[¶](#busapitacan "Link to this heading")

*class* CanMessageEvent[¶](#tts.testModule.bus.busObjects.LIN.CanMessageEvent "Link to this definition")  
Class for multiple types of bus events:

- CAN Message Event

- CAN Extended Message Event

- CAN Error Frame

- CAN Remote Frame Event

- CAN FD Message Event

- CAN FD Extended Message Event

- CAN FD Error Frame

id[¶](#tts.testModule.bus.busObjects.LIN.CanMessageEvent.id "Link to this definition")  
Alias for [`canID`](#tts.testModule.bus.busObjects.LIN.CanMessageEvent.canID "tts.testModule.bus.busObjects.LIN.CanMessageEvent.canID"). The slot ID of the frame.

Type:  int

payload[¶](#tts.testModule.bus.busObjects.LIN.CanMessageEvent.payload "Link to this definition")  
The frame’s payload.

Type:  ByteStream

payloadArray[¶](#tts.testModule.bus.busObjects.LIN.CanMessageEvent.payloadArray "Link to this definition")  
The frame’s payload as numpy array (especially useful in trace step templates).

Type:  numpy.ndarray

length[¶](#tts.testModule.bus.busObjects.LIN.CanMessageEvent.length "Link to this definition")  
The frame’s length in bytes.

Type:  int

timestamp[¶](#tts.testModule.bus.busObjects.LIN.CanMessageEvent.timestamp "Link to this definition")  
The frame’s timestamp in ms.

Type:  float

flags[¶](#tts.testModule.bus.busObjects.LIN.CanMessageEvent.flags "Link to this definition")  
Any of the frame’s flags defined in the corresponding flags class can be accessed directly on the frame object, i.e. theFrame.aFlag instead of theFrame.flags.aFlag.

Some of the flags can take the value False if the driver does not support the respective attribute.

Type:  [`CanFlags`](#tts.testModule.bus.busObjects.CAN.CanFlags "tts.testModule.bus.busObjects.CAN.CanFlags")

canID[¶](#tts.testModule.bus.busObjects.LIN.CanMessageEvent.canID "Link to this definition")  
The CAN ID of the frame.

Type:  int

channelID[¶](#tts.testModule.bus.busObjects.LIN.CanMessageEvent.channelID "Link to this definition")  
The ID of the bus channel on which this frame was received.

Type:  int

ecc[¶](#tts.testModule.bus.busObjects.LIN.CanMessageEvent.ecc "Link to this definition")  
The ECC of the frame.

Type:  int

dlc[¶](#tts.testModule.bus.busObjects.LIN.CanMessageEvent.dlc "Link to this definition")  
The DLC of the frame.

Type:  int

*class* CanBusStatisticsEvent[¶](#tts.testModule.bus.busObjects.LIN.CanBusStatisticsEvent "Link to this definition")  
dataFrames[¶](#tts.testModule.bus.busObjects.LIN.CanBusStatisticsEvent.dataFrames "Link to this definition")  
The number of data frames.

Type:  int

remoteFrames[¶](#tts.testModule.bus.busObjects.LIN.CanBusStatisticsEvent.remoteFrames "Link to this definition")  
The number of remote frames.

Type:  int

extendedDataFrames[¶](#tts.testModule.bus.busObjects.LIN.CanBusStatisticsEvent.extendedDataFrames "Link to this definition")  
The number of extended data frames.

Type:  int

extendedRemoteFrames[¶](#tts.testModule.bus.busObjects.LIN.CanBusStatisticsEvent.extendedRemoteFrames "Link to this definition")  
The number of extended remote frames.

Type:  int

errorFrames[¶](#tts.testModule.bus.busObjects.LIN.CanBusStatisticsEvent.errorFrames "Link to this definition")  
The number of error frames.

Type:  int

overloadFrames[¶](#tts.testModule.bus.busObjects.LIN.CanBusStatisticsEvent.overloadFrames "Link to this definition")  
The number of overload frames.

Type:  int

busload[¶](#tts.testModule.bus.busObjects.LIN.CanBusStatisticsEvent.busload "Link to this definition")  
The busload.

Type:  float

timestamp[¶](#tts.testModule.bus.busObjects.LIN.CanBusStatisticsEvent.timestamp "Link to this definition")  
The frame’s raw timestamp. The determined offset of trace synchronization is not considered.

Type:  float

channelID[¶](#tts.testModule.bus.busObjects.LIN.CanBusStatisticsEvent.channelID "Link to this definition")  
The ID of the bus channel on which this frame was received.

Type:  int

*class* CanErrorEvent[¶](#tts.testModule.bus.busObjects.LIN.CanErrorEvent "Link to this definition")  
error[¶](#tts.testModule.bus.busObjects.LIN.CanErrorEvent.error "Link to this definition")  
The error.

Type:  str

timestamp[¶](#tts.testModule.bus.busObjects.LIN.CanErrorEvent.timestamp "Link to this definition")  
The frame’s raw timestamp. The determined offset of trace synchronization is not considered.

Type:  float

channelID[¶](#tts.testModule.bus.busObjects.LIN.CanErrorEvent.channelID "Link to this definition")  
The ID of the bus channel on which this frame was received.

Type:  int

*class* CanOverloadFrameEvent[¶](#tts.testModule.bus.busObjects.LIN.CanOverloadFrameEvent "Link to this definition")  
timestamp[¶](#tts.testModule.bus.busObjects.LIN.CanOverloadFrameEvent.timestamp "Link to this definition")  
The frame’s raw timestamp. The determined offset of trace synchronization is not considered.

Type:  float

channelID[¶](#tts.testModule.bus.busObjects.LIN.CanOverloadFrameEvent.channelID "Link to this definition")  
The ID of the bus channel on which this frame was received.

Type:  int

## FlexRay[¶](#busapitaflexray "Link to this heading")

*class* FlexRayMessageEvent[¶](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayMessageEvent "Link to this definition")  
timestamp[¶](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayMessageEvent.timestamp "Link to this definition")  
The frame’s raw timestamp. The determined offset of trace synchronization is not considered.

Type:  float

id[¶](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayMessageEvent.id "Link to this definition")  
Alias for [`slotID()`](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayMessageEvent.slotID "tts.traceRecording.parser.formats.BusParserObjects.FlexRayMessageEvent.slotID"). The FlexRay Slot-ID of the frame.

Type:  int

payload[¶](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayMessageEvent.payload "Link to this definition")  
The frame’s payload.

Type:  ByteStream

payloadArray[¶](#tts.traceRecording.parser.formats.BusParserObjects.FlexRayMessageEvent.payloadArray "Link to this definition")  
The frame’s payload as numpy array (especially useful in trace step templates).

Type:  numpy.ndarray

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

Type:  [`FlexRayFlags`](#tts.testModule.bus.busObjects.FlexRay.FlexRayFlags "tts.testModule.bus.busObjects.FlexRay.FlexRayFlags")

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

## LIN[¶](#busapitalin "Link to this heading")

*class* LinMessageEvent[¶](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageEvent "Link to this definition")  
timestamp[¶](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageEvent.timestamp "Link to this definition")  
The frame’s raw timestamp. The determined offset of trace synchronization is not considered.

Type:  float

id[¶](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageEvent.id "Link to this definition")  
Alias for [`linID()`](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageEvent.linID "tts.traceRecording.parser.formats.BusParserObjects.LinMessageEvent.linID"). The slot ID of the frame.

Type:  int

payload[¶](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageEvent.payload "Link to this definition")  
The frame’s payload.

Type:  ByteStream

payloadArray[¶](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageEvent.payloadArray "Link to this definition")  
The frame’s payload as numpy array (especially useful in trace step templates).

Type:  numpy.ndarray

messageInfo[¶](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageEvent.messageInfo "Link to this definition")  
Additional message information, for instance related to timings.

Type:  [`LinMessageInfo`](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageInfo "tts.traceRecording.parser.formats.BusParserObjects.LinMessageInfo")

length[¶](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageEvent.length "Link to this definition")  
The frame’s length in bytes.

Type:  int

flags[¶](#tts.traceRecording.parser.formats.BusParserObjects.LinMessageEvent.flags "Link to this definition")  
Any of the frame’s flags defined in the corresponding flags class can be accessed directly on the frame object, i.e. theFrame.aFlag instead of theFrame.flags.aFlag.

Some of the flags can take the value False if the driver does not support the respective attribute.

Type:  [`LinFlags`](#tts.testModule.bus.busObjects.LIN.LinFlags "tts.testModule.bus.busObjects.LIN.LinFlags")

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

> - 0: Start state

Transition to sleep mode

> - 1: Go-to-Sleep frame
>
> - 2: Bus Idle Timeout
>
> - 3: Silent SleepMode command (for shortening the BusIdle Timeout)

Leaving sleep mode

> - 9: External Wakeup signal
>
> - 10: Internal Wakeup signal
>
> - 11: Bus traffic (can only occur if the LIN hardware does not have a Master function)

LIN hardware does not go into sleep mode inspite of request to do so

> - 18: Bus traffic (can only occur if the LIN hardware does not have a Master function)

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

Type:  [`LinSleepModeFlags`](#tts.traceRecording.parser.formats.BusParserObjects.LinSleepModeFlags "tts.traceRecording.parser.formats.BusParserObjects.LinSleepModeFlags")

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

Type:  [`LinWakeupFrameInfo`](#tts.traceRecording.parser.formats.BusParserObjects.LinWakeupFrameInfo "tts.traceRecording.parser.formats.BusParserObjects.LinWakeupFrameInfo")

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

Type:  [`LinWakeupFrameInfo`](#tts.traceRecording.parser.formats.BusParserObjects.LinWakeupFrameInfo "tts.traceRecording.parser.formats.BusParserObjects.LinWakeupFrameInfo")

*class* LinWakeupFrameInfo[¶](#tts.traceRecording.parser.formats.BusParserObjects.LinWakeupFrameInfo "Link to this definition")  
startOfFrame[¶](#tts.traceRecording.parser.formats.BusParserObjects.LinWakeupFrameInfo.startOfFrame "Link to this definition")  
Absolute timestamp indicating start of event (in seconds).

Type:  float or np.ma.masked if not present

baudrate[¶](#tts.traceRecording.parser.formats.BusParserObjects.LinWakeupFrameInfo.baudrate "Link to this definition")  
Event’s baudrate (in bits/sec).

Type:  int or np.ma.masked if not present

lengthcode[¶](#tts.traceRecording.parser.formats.BusParserObjects.LinWakeupFrameInfo.lengthcode "Link to this definition")  
> This value is only valid for instances of [`LinWakeupFrame`](#tts.traceRecording.parser.formats.BusParserObjects.LinWakeupFrame "tts.traceRecording.parser.formats.BusParserObjects.LinWakeupFrame").
>
> Wake-up length validity indicator:
>
> - 0: Wake-up length is OK
>
> - 1: Wake-up is too short
>
> - 2: Wake-up is too long

Type:  int or np.ma.masked if not present

width[¶](#tts.traceRecording.parser.formats.BusParserObjects.LinWakeupFrameInfo.width "Link to this definition")  
The width of a wakeup signal in us. This value is only valid for instances of [`LinUnexpectedWakeup`](#tts.traceRecording.parser.formats.BusParserObjects.LinUnexpectedWakeup "tts.traceRecording.parser.formats.BusParserObjects.LinUnexpectedWakeup") with LIN 2.0.

Type:  int or np.ma.masked if not present

## Ethernet[¶](#ethernettraceanalysis "Link to this heading")

The following classes are created through calls of .parent, .FindParent(protocolName) or direct attribute access on a pseudo signal during trace analysis. protocolName is a string enum value from [OsiProtocol](#osiprotocolenum).

Examples:

- PacketSomeIp.udp.srcPort

- PacketUdp.FindParent(“eth”)

- PacketIp.parent

Note

Access to `EthernetProtocolBase.parent` can return None, while the other variants to protocols will return a `NoProtocol` instance if the given protocol is not present.

*class* OsiProtocol[¶](#tts.lib.ethernet.PacketEthernet.OsiProtocol "Link to this definition")  
String Enumeration class representing the supported protocol layers.

ETH *= 'eth'*[¶](#tts.lib.ethernet.PacketEthernet.OsiProtocol.ETH "Link to this definition")  

IP4 *= 'ip4'*[¶](#tts.lib.ethernet.PacketEthernet.OsiProtocol.IP4 "Link to this definition")  

IP6 *= 'ip6'*[¶](#tts.lib.ethernet.PacketEthernet.OsiProtocol.IP6 "Link to this definition")  

TCP *= 'tcp'*[¶](#tts.lib.ethernet.PacketEthernet.OsiProtocol.TCP "Link to this definition")  

UDP *= 'udp'*[¶](#tts.lib.ethernet.PacketEthernet.OsiProtocol.UDP "Link to this definition")  

PTP *= 'ptp'*[¶](#tts.lib.ethernet.PacketEthernet.OsiProtocol.PTP "Link to this definition")  

SOMEIP *= 'someip'*[¶](#tts.lib.ethernet.PacketEthernet.OsiProtocol.SOMEIP "Link to this definition")  

### EthernetProtocolBase[¶](#ethernetprotocolbase "Link to this heading")

*class* EthernetProtocolBase[¶](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "Link to this definition")  
Base class for all protocol classes.

\<protocol\>  
Equivalent to method [`FindParent(protocol)`](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase.FindParent "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase.FindParent"). Direct access to parent protocols. *protocol* is one of [`OsiProtocol`](#tts.lib.ethernet.PacketEthernet.OsiProtocol "tts.lib.ethernet.PacketEthernet.OsiProtocol").

Example: Signal.eth.src provides the source MAC address of the Ethernet protocol layer.

Type:  [`EthernetProtocolBase`](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase")

timestamp*: float*[¶](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase.timestamp "Link to this definition")  
current timestamp

parent[¶](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase.parent "Link to this definition")  
Returns the parent protocol object if there is one present, otherwise None.

Return type:  [EthernetProtocolBase](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase") | None

AssertExists()[¶](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase.AssertExists "Link to this definition")  
Raises an AssertionError if the accessed protocol does not exist at some time stamp. Example: Signal.tcp.AssertExists()

Returns:  The protocol itself, to support attribut chaining.

Raises:  
AssertionError

Return type:  *Self*

FindParent(*protocol*)[¶](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase.FindParent "Link to this definition")  
Returns a specific given protocol object if present, otherwise a [`NoProtocol`](#tts.lib.ethernet.PacketEthernet.NoProtocol "tts.lib.ethernet.PacketEthernet.NoProtocol") object.

Parameters:  **protocol** ([*OsiProtocol*](#tts.lib.ethernet.PacketEthernet.OsiProtocol "tts.lib.ethernet.PacketEthernet.OsiProtocol")) – The required protocol name.

Returns:  The required parent protocol object.

Return type:  [EthernetProtocolBase](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase")

### NoProtocol[¶](#noprotocol "Link to this heading")

*class* NoProtocol[¶](#tts.lib.ethernet.PacketEthernet.NoProtocol "Link to this definition")  
Represents a non-present protocol. Accessing any other parent of a non-present protocol will also yield a NoProtocol object. Accessing any protocol specific attributes will lead to an AttributeError since the specific protocol is not available. The boolean value of a NoProtocol object is always False, such that it can be used to check for the precense/absence of a protocol layer.

Examples:

- SigPacketSomeIp.tcp yields True for packets that were transmitted via TCP and False otherwise. This can be used in trigger blocks that trigger only when the TCP protcol layer is present.

- SigPacketSomeIp.tcp.srcPort will raise an AttributeError for packets that were not transmitted via TCP.

- SigPacketSomeIp.tcp.AssertExists() can be used to provoke an AssertionError for packets that were not transmitted via TCP.

\<protocol\>  
Equivalent to method [`FindParent(protocol)`](#tts.lib.ethernet.PacketEthernet.NoProtocol.FindParent "tts.lib.ethernet.PacketEthernet.NoProtocol.FindParent"). Direct access to parent protocols. *protocol* is one of [`OsiProtocol`](#tts.lib.ethernet.PacketEthernet.OsiProtocol "tts.lib.ethernet.PacketEthernet.OsiProtocol").

Example: Signal.eth.src provides the source MAC address of the Ethernet protocol layer.

Type:  [`EthernetProtocolBase`](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase")

AssertExists()[¶](#tts.lib.ethernet.PacketEthernet.NoProtocol.AssertExists "Link to this definition")  
Raises an AssertionError if the accessed protocol does not exist at some time stamp. Example: Signal.tcp.AssertExists()

Returns:  The protocol itself, to support attribut chaining.

Raises:  
AssertionError

Return type:  *Self*

FindParent(*protocol*)[¶](#tts.lib.ethernet.PacketEthernet.NoProtocol.FindParent "Link to this definition")  
Returns another NoProtocol instance.

Return type:  [NoProtocol](#tts.lib.ethernet.PacketEthernet.NoProtocol "tts.lib.ethernet.PacketEthernet.NoProtocol")

parent[¶](#tts.lib.ethernet.PacketEthernet.NoProtocol.parent "Link to this definition")  
Returns another NoProtocol instance.

Return type:  [NoProtocol](#tts.lib.ethernet.PacketEthernet.NoProtocol "tts.lib.ethernet.PacketEthernet.NoProtocol")

timestamp*: float*[¶](#tts.lib.ethernet.PacketEthernet.NoProtocol.timestamp "Link to this definition")  
current timestamp

### EthernetProtocol[¶](#ethernetprotocol "Link to this heading")

*class* EthernetProtocol[¶](#tts.lib.ethernet.PacketEthernet.EthernetProtocol "Link to this definition")  

\<protocol\>  
Equivalent to method [`FindParent(protocol)`](#tts.lib.ethernet.PacketEthernet.EthernetProtocol.FindParent "tts.lib.ethernet.PacketEthernet.EthernetProtocol.FindParent"). Direct access to parent protocols. *protocol* is one of [`OsiProtocol`](#tts.lib.ethernet.PacketEthernet.OsiProtocol "tts.lib.ethernet.PacketEthernet.OsiProtocol").

Example: Signal.eth.src provides the source MAC address of the Ethernet protocol layer.

Type:  [`EthernetProtocolBase`](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase")

dst*: str*[¶](#tts.lib.ethernet.PacketEthernet.EthernetProtocol.dst "Link to this definition")  
target MAC address e.g. DE:AD:BE:EF:FF:00

AssertExists()[¶](#tts.lib.ethernet.PacketEthernet.EthernetProtocol.AssertExists "Link to this definition")  
Raises an AssertionError if the accessed protocol does not exist at some time stamp. Example: Signal.tcp.AssertExists()

Returns:  The protocol itself, to support attribut chaining.

Raises:  
AssertionError

Return type:  *Self*

FindParent(*protocol*)[¶](#tts.lib.ethernet.PacketEthernet.EthernetProtocol.FindParent "Link to this definition")  
Returns a specific given protocol object if present, otherwise a [`NoProtocol`](#tts.lib.ethernet.PacketEthernet.NoProtocol "tts.lib.ethernet.PacketEthernet.NoProtocol") object.

Parameters:  **protocol** ([*OsiProtocol*](#tts.lib.ethernet.PacketEthernet.OsiProtocol "tts.lib.ethernet.PacketEthernet.OsiProtocol")) – The required protocol name.

Returns:  The required parent protocol object.

Return type:  [EthernetProtocolBase](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase")

parent[¶](#tts.lib.ethernet.PacketEthernet.EthernetProtocol.parent "Link to this definition")  
Returns the parent protocol object if there is one present, otherwise None.

Return type:  [EthernetProtocolBase](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase") | None

src*: str*[¶](#tts.lib.ethernet.PacketEthernet.EthernetProtocol.src "Link to this definition")  
source MAC address e.g. DE:AD:BE:EF:FF:00

timestamp*: float*[¶](#tts.lib.ethernet.PacketEthernet.EthernetProtocol.timestamp "Link to this definition")  
current timestamp

type*: int*[¶](#tts.lib.ethernet.PacketEthernet.EthernetProtocol.type "Link to this definition")  
ethernet protocol type

### Ipv4Protocol[¶](#ipv4protocol "Link to this heading")

*class* Ipv4Protocol[¶](#tts.lib.ethernet.PacketIp4.Ipv4Protocol "Link to this definition")  

\<protocol\>  
Equivalent to method [`FindParent(protocol)`](#tts.lib.ethernet.PacketIp4.Ipv4Protocol.FindParent "tts.lib.ethernet.PacketIp4.Ipv4Protocol.FindParent"). Direct access to parent protocols. *protocol* is one of [`OsiProtocol`](#tts.lib.ethernet.PacketEthernet.OsiProtocol "tts.lib.ethernet.PacketEthernet.OsiProtocol").

Example: Signal.eth.src provides the source MAC address of the Ethernet protocol layer.

Type:  [`EthernetProtocolBase`](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase")

version*: int*[¶](#tts.lib.ethernet.PacketIp4.Ipv4Protocol.version "Link to this definition")  
protocol version

headerLength*: int*[¶](#tts.lib.ethernet.PacketIp4.Ipv4Protocol.headerLength "Link to this definition")  
header length

tos*: int*[¶](#tts.lib.ethernet.PacketIp4.Ipv4Protocol.tos "Link to this definition")  
type of service

packetLength*: int*[¶](#tts.lib.ethernet.PacketIp4.Ipv4Protocol.packetLength "Link to this definition")  
packet length

id*: int*[¶](#tts.lib.ethernet.PacketIp4.Ipv4Protocol.id "Link to this definition")  
identifier

ttl*: int*[¶](#tts.lib.ethernet.PacketIp4.Ipv4Protocol.ttl "Link to this definition")  
TTL

protocol*: int*[¶](#tts.lib.ethernet.PacketIp4.Ipv4Protocol.protocol "Link to this definition")  
protocol type / next header field

checksum*: int*[¶](#tts.lib.ethernet.PacketIp4.Ipv4Protocol.checksum "Link to this definition")  
checksum

src*: str*[¶](#tts.lib.ethernet.PacketIp4.Ipv4Protocol.src "Link to this definition")  
source IP address e.g. 127.0.0.1

dst*: str*[¶](#tts.lib.ethernet.PacketIp4.Ipv4Protocol.dst "Link to this definition")  
destination IP address e.g. 127.0.0.1

ahSpi*: int | None = None*[¶](#tts.lib.ethernet.PacketIp4.Ipv4Protocol.ahSpi "Link to this definition")  
Security parameters index of IP authentication header (see RFC 4302)

ahSeq*: int | None = None*[¶](#tts.lib.ethernet.PacketIp4.Ipv4Protocol.ahSeq "Link to this definition")  
Sequence number field of IP authentication header (see RFC 4302)

ahIcv*: bytes | None = None*[¶](#tts.lib.ethernet.PacketIp4.Ipv4Protocol.ahIcv "Link to this definition")  
Integrity check value of IP authentication header (see RFC 4302)

ahNxt*: int | None = None*[¶](#tts.lib.ethernet.PacketIp4.Ipv4Protocol.ahNxt "Link to this definition")  
Next header value of IP authentication header (see RFC 4302)

ahLen*: int | None = None*[¶](#tts.lib.ethernet.PacketIp4.Ipv4Protocol.ahLen "Link to this definition")  
Length value of IP authentication header (see RFC 4302) =\> len(ICV)/4+1’

ahRsvd*: int | None = None*[¶](#tts.lib.ethernet.PacketIp4.Ipv4Protocol.ahRsvd "Link to this definition")  
Reserved value of IP authentication header (see RFC 4302

AssertExists()[¶](#tts.lib.ethernet.PacketIp4.Ipv4Protocol.AssertExists "Link to this definition")  
Raises an AssertionError if the accessed protocol does not exist at some time stamp. Example: Signal.tcp.AssertExists()

Returns:  The protocol itself, to support attribut chaining.

Raises:  
AssertionError

Return type:  *Self*

FindParent(*protocol*)[¶](#tts.lib.ethernet.PacketIp4.Ipv4Protocol.FindParent "Link to this definition")  
Returns a specific given protocol object if present, otherwise a [`NoProtocol`](#tts.lib.ethernet.PacketEthernet.NoProtocol "tts.lib.ethernet.PacketEthernet.NoProtocol") object.

Parameters:  **protocol** ([*OsiProtocol*](#tts.lib.ethernet.PacketEthernet.OsiProtocol "tts.lib.ethernet.PacketEthernet.OsiProtocol")) – The required protocol name.

Returns:  The required parent protocol object.

Return type:  [EthernetProtocolBase](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase")

parent[¶](#tts.lib.ethernet.PacketIp4.Ipv4Protocol.parent "Link to this definition")  
Returns the parent protocol object if there is one present, otherwise None.

Return type:  [EthernetProtocolBase](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase") | None

timestamp*: float*[¶](#tts.lib.ethernet.PacketIp4.Ipv4Protocol.timestamp "Link to this definition")  
current timestamp

### Ipv6Protocol[¶](#ipv6protocol "Link to this heading")

*class* Ipv6Protocol[¶](#tts.lib.ethernet.PacketIp6.Ipv6Protocol "Link to this definition")  

\<protocol\>  
Equivalent to method [`FindParent(protocol)`](#tts.lib.ethernet.PacketIp6.Ipv6Protocol.FindParent "tts.lib.ethernet.PacketIp6.Ipv6Protocol.FindParent"). Direct access to parent protocols. *protocol* is one of [`OsiProtocol`](#tts.lib.ethernet.PacketEthernet.OsiProtocol "tts.lib.ethernet.PacketEthernet.OsiProtocol").

Example: Signal.eth.src provides the source MAC address of the Ethernet protocol layer.

Type:  [`EthernetProtocolBase`](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase")

src*: str*[¶](#tts.lib.ethernet.PacketIp6.Ipv6Protocol.src "Link to this definition")  
source IP address e.g. 2001:db8::1428:57ab

dst*: str*[¶](#tts.lib.ethernet.PacketIp6.Ipv6Protocol.dst "Link to this definition")  
destination IP address e.g. 2001:db8::1428:57ab

protocol*: int*[¶](#tts.lib.ethernet.PacketIp6.Ipv6Protocol.protocol "Link to this definition")  
protocol type / next header field

hopLimit*: int*[¶](#tts.lib.ethernet.PacketIp6.Ipv6Protocol.hopLimit "Link to this definition")  
hop limit field

payloadLength*: int*[¶](#tts.lib.ethernet.PacketIp6.Ipv6Protocol.payloadLength "Link to this definition")  
payload length from IPv6 header

trafficClass*: int*[¶](#tts.lib.ethernet.PacketIp6.Ipv6Protocol.trafficClass "Link to this definition")  
traffic class from IPv6 header

flowLabel*: int*[¶](#tts.lib.ethernet.PacketIp6.Ipv6Protocol.flowLabel "Link to this definition")  
flow label from IPv6 header

AssertExists()[¶](#tts.lib.ethernet.PacketIp6.Ipv6Protocol.AssertExists "Link to this definition")  
Raises an AssertionError if the accessed protocol does not exist at some time stamp. Example: Signal.tcp.AssertExists()

Returns:  The protocol itself, to support attribut chaining.

Raises:  
AssertionError

Return type:  *Self*

FindParent(*protocol*)[¶](#tts.lib.ethernet.PacketIp6.Ipv6Protocol.FindParent "Link to this definition")  
Returns a specific given protocol object if present, otherwise a [`NoProtocol`](#tts.lib.ethernet.PacketEthernet.NoProtocol "tts.lib.ethernet.PacketEthernet.NoProtocol") object.

Parameters:  **protocol** ([*OsiProtocol*](#tts.lib.ethernet.PacketEthernet.OsiProtocol "tts.lib.ethernet.PacketEthernet.OsiProtocol")) – The required protocol name.

Returns:  The required parent protocol object.

Return type:  [EthernetProtocolBase](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase")

parent[¶](#tts.lib.ethernet.PacketIp6.Ipv6Protocol.parent "Link to this definition")  
Returns the parent protocol object if there is one present, otherwise None.

Return type:  [EthernetProtocolBase](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase") | None

timestamp*: float*[¶](#tts.lib.ethernet.PacketIp6.Ipv6Protocol.timestamp "Link to this definition")  
current timestamp

### UdpProtocol[¶](#udpprotocol "Link to this heading")

*class* UdpProtocol[¶](#tts.lib.ethernet.PacketUdp.UdpProtocol "Link to this definition")  

\<protocol\>  
Equivalent to method [`FindParent(protocol)`](#tts.lib.ethernet.PacketUdp.UdpProtocol.FindParent "tts.lib.ethernet.PacketUdp.UdpProtocol.FindParent"). Direct access to parent protocols. *protocol* is one of [`OsiProtocol`](#tts.lib.ethernet.PacketEthernet.OsiProtocol "tts.lib.ethernet.PacketEthernet.OsiProtocol").

Example: Signal.eth.src provides the source MAC address of the Ethernet protocol layer.

Type:  [`EthernetProtocolBase`](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase")

srcPort*: int*[¶](#tts.lib.ethernet.PacketUdp.UdpProtocol.srcPort "Link to this definition")  
source port

dstPort*: int*[¶](#tts.lib.ethernet.PacketUdp.UdpProtocol.dstPort "Link to this definition")  
destination port

AssertExists()[¶](#tts.lib.ethernet.PacketUdp.UdpProtocol.AssertExists "Link to this definition")  
Raises an AssertionError if the accessed protocol does not exist at some time stamp. Example: Signal.tcp.AssertExists()

Returns:  The protocol itself, to support attribut chaining.

Raises:  
AssertionError

Return type:  *Self*

FindParent(*protocol*)[¶](#tts.lib.ethernet.PacketUdp.UdpProtocol.FindParent "Link to this definition")  
Returns a specific given protocol object if present, otherwise a [`NoProtocol`](#tts.lib.ethernet.PacketEthernet.NoProtocol "tts.lib.ethernet.PacketEthernet.NoProtocol") object.

Parameters:  **protocol** ([*OsiProtocol*](#tts.lib.ethernet.PacketEthernet.OsiProtocol "tts.lib.ethernet.PacketEthernet.OsiProtocol")) – The required protocol name.

Returns:  The required parent protocol object.

Return type:  [EthernetProtocolBase](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase")

parent[¶](#tts.lib.ethernet.PacketUdp.UdpProtocol.parent "Link to this definition")  
Returns the parent protocol object if there is one present, otherwise None.

Return type:  [EthernetProtocolBase](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase") | None

packetLength*: int*[¶](#tts.lib.ethernet.PacketUdp.UdpProtocol.packetLength "Link to this definition")  
length of the UDP segment including the header length (8 Byte)

timestamp*: float*[¶](#tts.lib.ethernet.PacketUdp.UdpProtocol.timestamp "Link to this definition")  
current timestamp

checksum*: int*[¶](#tts.lib.ethernet.PacketUdp.UdpProtocol.checksum "Link to this definition")  
checksum

### TcpProtocol[¶](#tcpprotocol "Link to this heading")

*class* TcpProtocol[¶](#tts.lib.ethernet.PacketTcp.TcpProtocol "Link to this definition")  

\<protocol\>  
Equivalent to method [`FindParent(protocol)`](#tts.lib.ethernet.PacketTcp.TcpProtocol.FindParent "tts.lib.ethernet.PacketTcp.TcpProtocol.FindParent"). Direct access to parent protocols. *protocol* is one of [`OsiProtocol`](#tts.lib.ethernet.PacketEthernet.OsiProtocol "tts.lib.ethernet.PacketEthernet.OsiProtocol").

Example: Signal.eth.src provides the source MAC address of the Ethernet protocol layer.

Type:  [`EthernetProtocolBase`](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase")

srcPort*: int*[¶](#tts.lib.ethernet.PacketTcp.TcpProtocol.srcPort "Link to this definition")  
source port

dstPort*: int*[¶](#tts.lib.ethernet.PacketTcp.TcpProtocol.dstPort "Link to this definition")  
destination port

seq*: int*[¶](#tts.lib.ethernet.PacketTcp.TcpProtocol.seq "Link to this definition")  
sequence number

packetLength*: int*[¶](#tts.lib.ethernet.PacketTcp.TcpProtocol.packetLength "Link to this definition")  
length of the whole TCP segment including header length

ack*: int*[¶](#tts.lib.ethernet.PacketTcp.TcpProtocol.ack "Link to this definition")  
Ack number

headerLength*: int*[¶](#tts.lib.ethernet.PacketTcp.TcpProtocol.headerLength "Link to this definition")  
TCP header length (data offset)

flags*: int*[¶](#tts.lib.ethernet.PacketTcp.TcpProtocol.flags "Link to this definition")  
flags

AssertExists()[¶](#tts.lib.ethernet.PacketTcp.TcpProtocol.AssertExists "Link to this definition")  
Raises an AssertionError if the accessed protocol does not exist at some time stamp. Example: Signal.tcp.AssertExists()

Returns:  The protocol itself, to support attribut chaining.

Raises:  
AssertionError

Return type:  *Self*

FindParent(*protocol*)[¶](#tts.lib.ethernet.PacketTcp.TcpProtocol.FindParent "Link to this definition")  
Returns a specific given protocol object if present, otherwise a [`NoProtocol`](#tts.lib.ethernet.PacketEthernet.NoProtocol "tts.lib.ethernet.PacketEthernet.NoProtocol") object.

Parameters:  **protocol** ([*OsiProtocol*](#tts.lib.ethernet.PacketEthernet.OsiProtocol "tts.lib.ethernet.PacketEthernet.OsiProtocol")) – The required protocol name.

Returns:  The required parent protocol object.

Return type:  [EthernetProtocolBase](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase")

parent[¶](#tts.lib.ethernet.PacketTcp.TcpProtocol.parent "Link to this definition")  
Returns the parent protocol object if there is one present, otherwise None.

Return type:  [EthernetProtocolBase](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase") | None

window*: int*[¶](#tts.lib.ethernet.PacketTcp.TcpProtocol.window "Link to this definition")  
window

timestamp*: float*[¶](#tts.lib.ethernet.PacketTcp.TcpProtocol.timestamp "Link to this definition")  
current timestamp

checksum*: int*[¶](#tts.lib.ethernet.PacketTcp.TcpProtocol.checksum "Link to this definition")  
checksum

urgentPointer*: int*[¶](#tts.lib.ethernet.PacketTcp.TcpProtocol.urgentPointer "Link to this definition")  
urgent pointer

### PtpProtocol[¶](#ptpprotocol "Link to this heading")

*class* PtpProtocol[¶](#tts.lib.ethernet.PacketPtp.PtpProtocol "Link to this definition")  

\<protocol\>  
Equivalent to method [`FindParent(protocol)`](#tts.lib.ethernet.PacketPtp.PtpProtocol.FindParent "tts.lib.ethernet.PacketPtp.PtpProtocol.FindParent"). Direct access to parent protocols. *protocol* is one of [`OsiProtocol`](#tts.lib.ethernet.PacketEthernet.OsiProtocol "tts.lib.ethernet.PacketEthernet.OsiProtocol").

Example: Signal.eth.src provides the source MAC address of the Ethernet protocol layer.

Type:  [`EthernetProtocolBase`](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase")

messageType*: int*[¶](#tts.lib.ethernet.PacketPtp.PtpProtocol.messageType "Link to this definition")  
PTP message type

version*: int*[¶](#tts.lib.ethernet.PacketPtp.PtpProtocol.version "Link to this definition")  
PTP version

messageLength*: int*[¶](#tts.lib.ethernet.PacketPtp.PtpProtocol.messageLength "Link to this definition")  
PTP message length

domainNumber*: int*[¶](#tts.lib.ethernet.PacketPtp.PtpProtocol.domainNumber "Link to this definition")  
PTP domain number

flags*: int*[¶](#tts.lib.ethernet.PacketPtp.PtpProtocol.flags "Link to this definition")  
PTP flags

correctionField*: int*[¶](#tts.lib.ethernet.PacketPtp.PtpProtocol.correctionField "Link to this definition")  
PTP correctionField

sourcePortIdentity*: bytes*[¶](#tts.lib.ethernet.PacketPtp.PtpProtocol.sourcePortIdentity "Link to this definition")  
PTP source port identity

sequenceId*: int*[¶](#tts.lib.ethernet.PacketPtp.PtpProtocol.sequenceId "Link to this definition")  
PTP sequence ID

controlField*: int*[¶](#tts.lib.ethernet.PacketPtp.PtpProtocol.controlField "Link to this definition")  
PTP control field

logMessagePeriod*: int*[¶](#tts.lib.ethernet.PacketPtp.PtpProtocol.logMessagePeriod "Link to this definition")  
PTP log message interval

AssertExists()[¶](#tts.lib.ethernet.PacketPtp.PtpProtocol.AssertExists "Link to this definition")  
Raises an AssertionError if the accessed protocol does not exist at some time stamp. Example: Signal.tcp.AssertExists()

Returns:  The protocol itself, to support attribut chaining.

Raises:  
AssertionError

Return type:  *Self*

FindParent(*protocol*)[¶](#tts.lib.ethernet.PacketPtp.PtpProtocol.FindParent "Link to this definition")  
Returns a specific given protocol object if present, otherwise a [`NoProtocol`](#tts.lib.ethernet.PacketEthernet.NoProtocol "tts.lib.ethernet.PacketEthernet.NoProtocol") object.

Parameters:  **protocol** ([*OsiProtocol*](#tts.lib.ethernet.PacketEthernet.OsiProtocol "tts.lib.ethernet.PacketEthernet.OsiProtocol")) – The required protocol name.

Returns:  The required parent protocol object.

Return type:  [EthernetProtocolBase](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase")

parent[¶](#tts.lib.ethernet.PacketPtp.PtpProtocol.parent "Link to this definition")  
Returns the parent protocol object if there is one present, otherwise None.

Return type:  [EthernetProtocolBase](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase") | None

timestamp*: float*[¶](#tts.lib.ethernet.PacketPtp.PtpProtocol.timestamp "Link to this definition")  
current timestamp

### SomeIpProtocol[¶](#someipprotocol "Link to this heading")

*class* SomeIpProtocol[¶](#tts.lib.ethernet.PacketSomeIp.SomeIpProtocol "Link to this definition")  

\<protocol\>  
Equivalent to method [`FindParent(protocol)`](#tts.lib.ethernet.PacketSomeIp.SomeIpProtocol.FindParent "tts.lib.ethernet.PacketSomeIp.SomeIpProtocol.FindParent"). Direct access to parent protocols. *protocol* is one of [`OsiProtocol`](#tts.lib.ethernet.PacketEthernet.OsiProtocol "tts.lib.ethernet.PacketEthernet.OsiProtocol").

Example: Signal.eth.src provides the source MAC address of the Ethernet protocol layer.

Type:  [`EthernetProtocolBase`](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase")

messageId*: int*[¶](#tts.lib.ethernet.PacketSomeIp.SomeIpProtocol.messageId "Link to this definition")  
message ID

serviceId*: int*[¶](#tts.lib.ethernet.PacketSomeIp.SomeIpProtocol.serviceId "Link to this definition")  
service ID (highest 16 bit from message id)

AssertExists()[¶](#tts.lib.ethernet.PacketSomeIp.SomeIpProtocol.AssertExists "Link to this definition")  
Raises an AssertionError if the accessed protocol does not exist at some time stamp. Example: Signal.tcp.AssertExists()

Returns:  The protocol itself, to support attribut chaining.

Raises:  
AssertionError

Return type:  *Self*

FindParent(*protocol*)[¶](#tts.lib.ethernet.PacketSomeIp.SomeIpProtocol.FindParent "Link to this definition")  
Returns a specific given protocol object if present, otherwise a [`NoProtocol`](#tts.lib.ethernet.PacketEthernet.NoProtocol "tts.lib.ethernet.PacketEthernet.NoProtocol") object.

Parameters:  **protocol** ([*OsiProtocol*](#tts.lib.ethernet.PacketEthernet.OsiProtocol "tts.lib.ethernet.PacketEthernet.OsiProtocol")) – The required protocol name.

Returns:  The required parent protocol object.

Return type:  [EthernetProtocolBase](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase")

parent[¶](#tts.lib.ethernet.PacketSomeIp.SomeIpProtocol.parent "Link to this definition")  
Returns the parent protocol object if there is one present, otherwise None.

Return type:  [EthernetProtocolBase](#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase") | None

methodId*: int*[¶](#tts.lib.ethernet.PacketSomeIp.SomeIpProtocol.methodId "Link to this definition")  
method ID (lowest 16 bit from message id)

timestamp*: float*[¶](#tts.lib.ethernet.PacketSomeIp.SomeIpProtocol.timestamp "Link to this definition")  
current timestamp

length*: int*[¶](#tts.lib.ethernet.PacketSomeIp.SomeIpProtocol.length "Link to this definition")  
length from this header position

requestId*: int*[¶](#tts.lib.ethernet.PacketSomeIp.SomeIpProtocol.requestId "Link to this definition")  
request ID

clientId*: int*[¶](#tts.lib.ethernet.PacketSomeIp.SomeIpProtocol.clientId "Link to this definition")  
client id (highest 16 bit from request id)

sessionId*: int*[¶](#tts.lib.ethernet.PacketSomeIp.SomeIpProtocol.sessionId "Link to this definition")  
session id (lowest 16 bit from request id)

protocolVersion*: int*[¶](#tts.lib.ethernet.PacketSomeIp.SomeIpProtocol.protocolVersion "Link to this definition")  
SOME/IP Protocol version

interfaceVersion*: int*[¶](#tts.lib.ethernet.PacketSomeIp.SomeIpProtocol.interfaceVersion "Link to this definition")  
SOME/IP interface version

messageType*: int*[¶](#tts.lib.ethernet.PacketSomeIp.SomeIpProtocol.messageType "Link to this definition")  
message Type

returnCode*: int*[¶](#tts.lib.ethernet.PacketSomeIp.SomeIpProtocol.returnCode "Link to this definition")  
return code
