[ Internal APIs ](api.md)

[ Advanced operations of package variable types ](variabledatastructures.md)

Advanced properties of bus-related objects [ Advanced properties of bus-related objects ](#)

Advanced properties of bus-related objects

- [ CAN ](#can)
  - [C CanFrame ](#tts.testModule.bus.busObjects.CAN.CanFrame)
    - [A canID ](#tts.testModule.bus.busObjects.CAN.CanFrame.canID)
    - [A flags ](#tts.testModule.bus.busObjects.CAN.CanFrame.flags)
    - [A length ](#tts.testModule.bus.busObjects.CAN.CanFrame.length)
    - [A payload ](#tts.testModule.bus.busObjects.CAN.CanFrame.payload)
    - [A timestamp ](#tts.testModule.bus.busObjects.CAN.CanFrame.timestamp)
  - [C CanFlags ](#tts.testModule.bus.busObjects.CAN.CanFlags)
    - [A isError ](#tts.testModule.bus.busObjects.CAN.CanFlags.isError)
    - [A isRemote ](#tts.testModule.bus.busObjects.CAN.CanFlags.isRemote)
    - [A isExtended ](#tts.testModule.bus.busObjects.CAN.CanFlags.isExtended)
    - [A isSelfReceived ](#tts.testModule.bus.busObjects.CAN.CanFlags.isSelfReceived)
    - [A isTx ](#tts.testModule.bus.busObjects.CAN.CanFlags.isTx)
    - [A isEDL ](#tts.testModule.bus.busObjects.CAN.CanFlags.isEDL)
    - [A isBRS ](#tts.testModule.bus.busObjects.CAN.CanFlags.isBRS)
- [ FlexRay ](#flexray)
  - [C FlexRayFrame ](#tts.testModule.bus.busObjects.FlexRay.FlexRayFrame)
    - [A slotID ](#tts.testModule.bus.busObjects.FlexRay.FlexRayFrame.slotID)
    - [A cycleNumber ](#tts.testModule.bus.busObjects.FlexRay.FlexRayFrame.cycleNumber)
    - [A headerCRC ](#tts.testModule.bus.busObjects.FlexRay.FlexRayFrame.headerCRC)
    - [A channelID ](#tts.testModule.bus.busObjects.FlexRay.FlexRayFrame.channelID)
    - [A flags ](#tts.testModule.bus.busObjects.FlexRay.FlexRayFrame.flags)
    - [A payload ](#tts.testModule.bus.busObjects.FlexRay.FlexRayFrame.payload)
    - [A timestamp ](#tts.testModule.bus.busObjects.FlexRay.FlexRayFrame.timestamp)
  - [C FlexRayFlags ](#tts.testModule.bus.busObjects.FlexRay.FlexRayFlags)
    - [A isSelfReceived ](#tts.testModule.bus.busObjects.FlexRay.FlexRayFlags.isSelfReceived)
    - [A isTx ](#tts.testModule.bus.busObjects.FlexRay.FlexRayFlags.isTx)
    - [A isNull ](#tts.testModule.bus.busObjects.FlexRay.FlexRayFlags.isNull)
    - [A isValid ](#tts.testModule.bus.busObjects.FlexRay.FlexRayFlags.isValid)
    - [A isSync ](#tts.testModule.bus.busObjects.FlexRay.FlexRayFlags.isSync)
    - [A isStartup ](#tts.testModule.bus.busObjects.FlexRay.FlexRayFlags.isStartup)
    - [A hasPayloadPreamble ](#tts.testModule.bus.busObjects.FlexRay.FlexRayFlags.hasPayloadPreamble)
    - [A isError ](#tts.testModule.bus.busObjects.FlexRay.FlexRayFlags.isError)
    - [A isAsync ](#tts.testModule.bus.busObjects.FlexRay.FlexRayFlags.isAsync)
    - [A isDynamic ](#tts.testModule.bus.busObjects.FlexRay.FlexRayFlags.isDynamic)
- [ LIN ](#lin)
  - [C LinFrame ](#tts.testModule.bus.busObjects.LIN.LinFrame)
    - [A linID ](#tts.testModule.bus.busObjects.LIN.LinFrame.linID)
    - [A crc ](#tts.testModule.bus.busObjects.LIN.LinFrame.crc)
    - [A flags ](#tts.testModule.bus.busObjects.LIN.LinFrame.flags)
    - [A payload ](#tts.testModule.bus.busObjects.LIN.LinFrame.payload)
    - [A timestamp ](#tts.testModule.bus.busObjects.LIN.LinFrame.timestamp)
  - [C LinFlags ](#tts.testModule.bus.busObjects.LIN.LinFlags)
    - [A isCrcError ](#tts.testModule.bus.busObjects.LIN.LinFlags.isCrcError)
    - [A isSelfReceived ](#tts.testModule.bus.busObjects.LIN.LinFlags.isSelfReceived)
    - [A isTx ](#tts.testModule.bus.busObjects.LIN.LinFlags.isTx)
- [ Ethernet ](#ethernet)
  - [C Ethernet ](#tts.core.api.internalApi.Ethernet.Ethernet)
    - [A UDP ](#tts.core.api.internalApi.Ethernet.Ethernet.UDP)
    - [A TCP ](#tts.core.api.internalApi.Ethernet.Ethernet.TCP)
    - [A PacketEthernet ](#tts.core.api.internalApi.Ethernet.Ethernet.PacketEthernet)
    - [A PacketIp4 ](#tts.core.api.internalApi.Ethernet.Ethernet.PacketIp4)
    - [A PacketIp6 ](#tts.core.api.internalApi.Ethernet.Ethernet.PacketIp6)
    - [A PacketIcmp ](#tts.core.api.internalApi.Ethernet.Ethernet.PacketIcmp)
    - [A PacketMka ](#tts.core.api.internalApi.Ethernet.Ethernet.PacketMka)
    - [A PacketIke ](#tts.core.api.internalApi.Ethernet.Ethernet.PacketIke)
    - [A PacketTcp ](#tts.core.api.internalApi.Ethernet.Ethernet.PacketTcp)
    - [A PacketUdp ](#tts.core.api.internalApi.Ethernet.Ethernet.PacketUdp)
    - [A PacketPtpSync ](#tts.core.api.internalApi.Ethernet.Ethernet.PacketPtpSync)
    - [A PacketPtpFollowUp ](#tts.core.api.internalApi.Ethernet.Ethernet.PacketPtpFollowUp)
    - [A PacketPdelayReq ](#tts.core.api.internalApi.Ethernet.Ethernet.PacketPdelayReq)
    - [A PacketPdelayResp ](#tts.core.api.internalApi.Ethernet.Ethernet.PacketPdelayResp)
    - [A PacketPdelayRespFollowUp ](#tts.core.api.internalApi.Ethernet.Ethernet.PacketPdelayRespFollowUp)
    - [A PacketSomeIp ](#tts.core.api.internalApi.Ethernet.Ethernet.PacketSomeIp)
    - [A PacketSomeIpSd ](#tts.core.api.internalApi.Ethernet.Ethernet.PacketSomeIpSd)
    - [A PacketSomeIpSdEntry ](#tts.core.api.internalApi.Ethernet.Ethernet.PacketSomeIpSdEntry)
    - [A PacketSomeIpSdEntryService ](#tts.core.api.internalApi.Ethernet.Ethernet.PacketSomeIpSdEntryService)
    - [A PacketSomeIpSdEntryEventgroup ](#tts.core.api.internalApi.Ethernet.Ethernet.PacketSomeIpSdEntryEventgroup)
    - [A PacketSomeIpSdOptionIpv4 ](#tts.core.api.internalApi.Ethernet.Ethernet.PacketSomeIpSdOptionIpv4)
    - [A PacketSomeIpSdOption ](#tts.core.api.internalApi.Ethernet.Ethernet.PacketSomeIpSdOption)
    - [A PacketSomeIpSdOptionIpv6 ](#tts.core.api.internalApi.Ethernet.Ethernet.PacketSomeIpSdOptionIpv6)
    - [A PacketSomeIpSdOptionIpv4Multicast ](#tts.core.api.internalApi.Ethernet.Ethernet.PacketSomeIpSdOptionIpv4Multicast)
    - [A PacketSomeIpSdOptionIpv6Multicast ](#tts.core.api.internalApi.Ethernet.Ethernet.PacketSomeIpSdOptionIpv6Multicast)
    - [A PacketSomeIpSdOptionIpv4SD ](#tts.core.api.internalApi.Ethernet.Ethernet.PacketSomeIpSdOptionIpv4SD)
    - [A PacketSomeIpSdOptionIpv6SD ](#tts.core.api.internalApi.Ethernet.Ethernet.PacketSomeIpSdOptionIpv6SD)
    - [A PacketSomeIpSdOptionConfig ](#tts.core.api.internalApi.Ethernet.Ethernet.PacketSomeIpSdOptionConfig)
  - [ PacketEthernet ](#packetethernet)
    - [C PacketEthernet ](#tts.lib.ethernet.PacketEthernet.PacketEthernet)
      - [M GetEthDstMac ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.GetEthDstMac)
      - [M SetEthDstMac ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.SetEthDstMac)
      - [A ethDstMac ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.ethDstMac)
      - [M GetEthSrcMac ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.GetEthSrcMac)
      - [M SetEthSrcMac ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.SetEthSrcMac)
      - [A ethSrcMac ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.ethSrcMac)
      - [M GetEthType ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.GetEthType)
      - [M SetEthType ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.SetEthType)
      - [A ethType ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.ethType)
      - [M GetVlanPcp ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.GetVlanPcp)
      - [M SetVlanPcp ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.SetVlanPcp)
      - [A vlanPcp ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.vlanPcp)
      - [M GetVlanCfi ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.GetVlanCfi)
      - [M SetVlanCfi ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.SetVlanCfi)
      - [A vlanCfi ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.vlanCfi)
      - [M GetVlanVid ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.GetVlanVid)
      - [M SetVlanVid ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.SetVlanVid)
      - [A vlanVid ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.vlanVid)
      - [M GetVlanPcpOuter ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.GetVlanPcpOuter)
      - [M SetVlanPcpOuter ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.SetVlanPcpOuter)
      - [A vlanPcpOuter ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.vlanPcpOuter)
      - [M GetVlanCfiOuter ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.GetVlanCfiOuter)
      - [M SetVlanCfiOuter ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.SetVlanCfiOuter)
      - [A vlanCfiOuter ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.vlanCfiOuter)
      - [M GetVlanVidOuter ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.GetVlanVidOuter)
      - [M SetVlanVidOuter ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.SetVlanVidOuter)
      - [A vlanVidOuter ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.vlanVidOuter)
      - [M GetEthPayload ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.GetEthPayload)
      - [M SetEthPayload ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.SetEthPayload)
      - [A ethPayload ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.ethPayload)
      - [M GetMacSecTciAn ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.GetMacSecTciAn)
      - [A macSecTciAn ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.macSecTciAn)
      - [M GetMacSecTci ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.GetMacSecTci)
      - [A macSecTci ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.macSecTci)
      - [M GetMacSecTciV ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.GetMacSecTciV)
      - [A macSecTciV ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.macSecTciV)
      - [M GetMacSecTciEs ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.GetMacSecTciEs)
      - [A macSecTciEs ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.macSecTciEs)
      - [M GetMacSecTciSc ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.GetMacSecTciSc)
      - [A macSecTciSc ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.macSecTciSc)
      - [M GetMacSecTciScb ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.GetMacSecTciScb)
      - [A macSecTciScb ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.macSecTciScb)
      - [M GetMacSecTciE ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.GetMacSecTciE)
      - [A macSecTciE ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.macSecTciE)
      - [M GetMacSecTciC ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.GetMacSecTciC)
      - [A macSecTciC ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.macSecTciC)
      - [M GetMacSecAn ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.GetMacSecAn)
      - [A macSecAn ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.macSecAn)
      - [M GetMacSecSl ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.GetMacSecSl)
      - [A macSecSl ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.macSecSl)
      - [M GetMacSecPn ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.GetMacSecPn)
      - [A macSecPn ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.macSecPn)
      - [M GetMacSecSci ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.GetMacSecSci)
      - [A macSecSci ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.macSecSci)
      - [M GetMacSecIcv ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.GetMacSecIcv)
      - [A macSecIcv ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.macSecIcv)
      - [M FindParent ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.FindParent)
      - [M GetTimestamp ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.GetTimestamp)
      - [M SetTimestamp ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.SetTimestamp)
      - [A parent ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.parent)
      - [A timestamp ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.timestamp)
  - [ PacketIp4 ](#packetip4)
    - [C PacketIp4 ](#tts.lib.ethernet.PacketIp4.PacketIp4)
      - [M GetIpVersionAndHeaderLength ](#tts.lib.ethernet.PacketIp4.PacketIp4.GetIpVersionAndHeaderLength)
      - [M SetIpVersionAndHeaderLength ](#tts.lib.ethernet.PacketIp4.PacketIp4.SetIpVersionAndHeaderLength)
      - [A ipVersionHeader ](#tts.lib.ethernet.PacketIp4.PacketIp4.ipVersionHeader)
      - [M GetIpTos ](#tts.lib.ethernet.PacketIp4.PacketIp4.GetIpTos)
      - [M SetIpTos ](#tts.lib.ethernet.PacketIp4.PacketIp4.SetIpTos)
      - [A ipTos ](#tts.lib.ethernet.PacketIp4.PacketIp4.ipTos)
      - [M GetIpLen ](#tts.lib.ethernet.PacketIp4.PacketIp4.GetIpLen)
      - [M SetIpLen ](#tts.lib.ethernet.PacketIp4.PacketIp4.SetIpLen)
      - [A ipLen ](#tts.lib.ethernet.PacketIp4.PacketIp4.ipLen)
      - [M GetIpIdent ](#tts.lib.ethernet.PacketIp4.PacketIp4.GetIpIdent)
      - [M SetIpIdent ](#tts.lib.ethernet.PacketIp4.PacketIp4.SetIpIdent)
      - [A ipIdent ](#tts.lib.ethernet.PacketIp4.PacketIp4.ipIdent)
      - [M GetIpOffset ](#tts.lib.ethernet.PacketIp4.PacketIp4.GetIpOffset)
      - [M SetIpOffset ](#tts.lib.ethernet.PacketIp4.PacketIp4.SetIpOffset)
      - [A ipOffset ](#tts.lib.ethernet.PacketIp4.PacketIp4.ipOffset)
      - [M GetIpTtl ](#tts.lib.ethernet.PacketIp4.PacketIp4.GetIpTtl)
      - [M SetIpTtl ](#tts.lib.ethernet.PacketIp4.PacketIp4.SetIpTtl)
      - [A ipTtl ](#tts.lib.ethernet.PacketIp4.PacketIp4.ipTtl)
      - [M GetIpProt ](#tts.lib.ethernet.PacketIp4.PacketIp4.GetIpProt)
      - [M SetIpProt ](#tts.lib.ethernet.PacketIp4.PacketIp4.SetIpProt)
      - [A ipProt ](#tts.lib.ethernet.PacketIp4.PacketIp4.ipProt)
      - [M GetIpChecksum ](#tts.lib.ethernet.PacketIp4.PacketIp4.GetIpChecksum)
      - [M SetIpChecksum ](#tts.lib.ethernet.PacketIp4.PacketIp4.SetIpChecksum)
      - [A ipChecksum ](#tts.lib.ethernet.PacketIp4.PacketIp4.ipChecksum)
      - [M GetIpSrc ](#tts.lib.ethernet.PacketIp4.PacketIp4.GetIpSrc)
      - [M SetIpSrc ](#tts.lib.ethernet.PacketIp4.PacketIp4.SetIpSrc)
      - [A ipSrc ](#tts.lib.ethernet.PacketIp4.PacketIp4.ipSrc)
      - [M GetIpDst ](#tts.lib.ethernet.PacketIp4.PacketIp4.GetIpDst)
      - [M SetIpDst ](#tts.lib.ethernet.PacketIp4.PacketIp4.SetIpDst)
      - [A ipDst ](#tts.lib.ethernet.PacketIp4.PacketIp4.ipDst)
      - [M GetIpPayload ](#tts.lib.ethernet.PacketIp4.PacketIp4.GetIpPayload)
      - [M SetIpPayload ](#tts.lib.ethernet.PacketIp4.PacketIp4.SetIpPayload)
      - [A ipPayload ](#tts.lib.ethernet.PacketIp4.PacketIp4.ipPayload)
      - [M GetIpAhSpi ](#tts.lib.ethernet.PacketIp4.PacketIp4.GetIpAhSpi)
      - [A ipAhSpi ](#tts.lib.ethernet.PacketIp4.PacketIp4.ipAhSpi)
      - [M GetIpAhSeq ](#tts.lib.ethernet.PacketIp4.PacketIp4.GetIpAhSeq)
      - [A ipAhSeq ](#tts.lib.ethernet.PacketIp4.PacketIp4.ipAhSeq)
      - [M GetIpAhIcv ](#tts.lib.ethernet.PacketIp4.PacketIp4.GetIpAhIcv)
      - [A ipAhIcv ](#tts.lib.ethernet.PacketIp4.PacketIp4.ipAhIcv)
      - [M GetIpAhNxt ](#tts.lib.ethernet.PacketIp4.PacketIp4.GetIpAhNxt)
      - [A ipAhNxt ](#tts.lib.ethernet.PacketIp4.PacketIp4.ipAhNxt)
      - [M GetIpAhLen ](#tts.lib.ethernet.PacketIp4.PacketIp4.GetIpAhLen)
      - [A ipAhLen ](#tts.lib.ethernet.PacketIp4.PacketIp4.ipAhLen)
      - [M GetIpAhRsvd ](#tts.lib.ethernet.PacketIp4.PacketIp4.GetIpAhRsvd)
      - [A ipAhRsvd ](#tts.lib.ethernet.PacketIp4.PacketIp4.ipAhRsvd)
      - [M CalcIpLen ](#tts.lib.ethernet.PacketIp4.PacketIp4.CalcIpLen)
      - [M FindParent ](#tts.lib.ethernet.PacketIp4.PacketIp4.FindParent)
      - [M GetEthDstMac ](#tts.lib.ethernet.PacketIp4.PacketIp4.GetEthDstMac)
      - [M GetEthPayload ](#tts.lib.ethernet.PacketIp4.PacketIp4.GetEthPayload)
      - [M GetEthSrcMac ](#tts.lib.ethernet.PacketIp4.PacketIp4.GetEthSrcMac)
      - [M GetEthType ](#tts.lib.ethernet.PacketIp4.PacketIp4.GetEthType)
      - [M GetMacSecAn ](#tts.lib.ethernet.PacketIp4.PacketIp4.GetMacSecAn)
      - [M GetMacSecIcv ](#tts.lib.ethernet.PacketIp4.PacketIp4.GetMacSecIcv)
      - [M GetMacSecPn ](#tts.lib.ethernet.PacketIp4.PacketIp4.GetMacSecPn)
      - [M GetMacSecSci ](#tts.lib.ethernet.PacketIp4.PacketIp4.GetMacSecSci)
      - [M GetMacSecSl ](#tts.lib.ethernet.PacketIp4.PacketIp4.GetMacSecSl)
      - [M GetMacSecTci ](#tts.lib.ethernet.PacketIp4.PacketIp4.GetMacSecTci)
      - [M GetMacSecTciAn ](#tts.lib.ethernet.PacketIp4.PacketIp4.GetMacSecTciAn)
      - [M GetMacSecTciC ](#tts.lib.ethernet.PacketIp4.PacketIp4.GetMacSecTciC)
      - [M GetMacSecTciE ](#tts.lib.ethernet.PacketIp4.PacketIp4.GetMacSecTciE)
      - [M GetMacSecTciEs ](#tts.lib.ethernet.PacketIp4.PacketIp4.GetMacSecTciEs)
      - [M GetMacSecTciSc ](#tts.lib.ethernet.PacketIp4.PacketIp4.GetMacSecTciSc)
      - [M GetMacSecTciScb ](#tts.lib.ethernet.PacketIp4.PacketIp4.GetMacSecTciScb)
      - [M GetMacSecTciV ](#tts.lib.ethernet.PacketIp4.PacketIp4.GetMacSecTciV)
      - [M GetTimestamp ](#tts.lib.ethernet.PacketIp4.PacketIp4.GetTimestamp)
      - [M GetVlanCfi ](#tts.lib.ethernet.PacketIp4.PacketIp4.GetVlanCfi)
      - [M GetVlanCfiOuter ](#tts.lib.ethernet.PacketIp4.PacketIp4.GetVlanCfiOuter)
      - [M GetVlanPcp ](#tts.lib.ethernet.PacketIp4.PacketIp4.GetVlanPcp)
      - [M GetVlanPcpOuter ](#tts.lib.ethernet.PacketIp4.PacketIp4.GetVlanPcpOuter)
      - [M GetVlanVid ](#tts.lib.ethernet.PacketIp4.PacketIp4.GetVlanVid)
      - [M GetVlanVidOuter ](#tts.lib.ethernet.PacketIp4.PacketIp4.GetVlanVidOuter)
      - [M SetEthDstMac ](#tts.lib.ethernet.PacketIp4.PacketIp4.SetEthDstMac)
      - [M SetEthPayload ](#tts.lib.ethernet.PacketIp4.PacketIp4.SetEthPayload)
      - [M SetEthSrcMac ](#tts.lib.ethernet.PacketIp4.PacketIp4.SetEthSrcMac)
      - [M SetEthType ](#tts.lib.ethernet.PacketIp4.PacketIp4.SetEthType)
      - [M SetTimestamp ](#tts.lib.ethernet.PacketIp4.PacketIp4.SetTimestamp)
      - [M SetVlanCfi ](#tts.lib.ethernet.PacketIp4.PacketIp4.SetVlanCfi)
      - [M SetVlanCfiOuter ](#tts.lib.ethernet.PacketIp4.PacketIp4.SetVlanCfiOuter)
      - [M SetVlanPcp ](#tts.lib.ethernet.PacketIp4.PacketIp4.SetVlanPcp)
      - [M SetVlanPcpOuter ](#tts.lib.ethernet.PacketIp4.PacketIp4.SetVlanPcpOuter)
      - [M SetVlanVid ](#tts.lib.ethernet.PacketIp4.PacketIp4.SetVlanVid)
      - [M SetVlanVidOuter ](#tts.lib.ethernet.PacketIp4.PacketIp4.SetVlanVidOuter)
      - [A ethDstMac ](#tts.lib.ethernet.PacketIp4.PacketIp4.ethDstMac)
      - [A ethPayload ](#tts.lib.ethernet.PacketIp4.PacketIp4.ethPayload)
      - [A ethSrcMac ](#tts.lib.ethernet.PacketIp4.PacketIp4.ethSrcMac)
      - [A ethType ](#tts.lib.ethernet.PacketIp4.PacketIp4.ethType)
      - [A macSecAn ](#tts.lib.ethernet.PacketIp4.PacketIp4.macSecAn)
      - [A macSecIcv ](#tts.lib.ethernet.PacketIp4.PacketIp4.macSecIcv)
      - [A macSecPn ](#tts.lib.ethernet.PacketIp4.PacketIp4.macSecPn)
      - [A macSecSci ](#tts.lib.ethernet.PacketIp4.PacketIp4.macSecSci)
      - [A macSecSl ](#tts.lib.ethernet.PacketIp4.PacketIp4.macSecSl)
      - [A macSecTci ](#tts.lib.ethernet.PacketIp4.PacketIp4.macSecTci)
      - [A macSecTciAn ](#tts.lib.ethernet.PacketIp4.PacketIp4.macSecTciAn)
      - [A macSecTciC ](#tts.lib.ethernet.PacketIp4.PacketIp4.macSecTciC)
      - [A macSecTciE ](#tts.lib.ethernet.PacketIp4.PacketIp4.macSecTciE)
      - [A macSecTciEs ](#tts.lib.ethernet.PacketIp4.PacketIp4.macSecTciEs)
      - [A macSecTciSc ](#tts.lib.ethernet.PacketIp4.PacketIp4.macSecTciSc)
      - [A macSecTciScb ](#tts.lib.ethernet.PacketIp4.PacketIp4.macSecTciScb)
      - [A macSecTciV ](#tts.lib.ethernet.PacketIp4.PacketIp4.macSecTciV)
      - [A parent ](#tts.lib.ethernet.PacketIp4.PacketIp4.parent)
      - [A timestamp ](#tts.lib.ethernet.PacketIp4.PacketIp4.timestamp)
      - [A vlanCfi ](#tts.lib.ethernet.PacketIp4.PacketIp4.vlanCfi)
      - [A vlanCfiOuter ](#tts.lib.ethernet.PacketIp4.PacketIp4.vlanCfiOuter)
      - [A vlanPcp ](#tts.lib.ethernet.PacketIp4.PacketIp4.vlanPcp)
      - [A vlanPcpOuter ](#tts.lib.ethernet.PacketIp4.PacketIp4.vlanPcpOuter)
      - [A vlanVid ](#tts.lib.ethernet.PacketIp4.PacketIp4.vlanVid)
      - [A vlanVidOuter ](#tts.lib.ethernet.PacketIp4.PacketIp4.vlanVidOuter)
  - [ PacketIp6 ](#packetip6)
    - [C PacketIp6 ](#tts.lib.ethernet.PacketIp6.PacketIp6)
      - [M GetIpProt ](#tts.lib.ethernet.PacketIp6.PacketIp6.GetIpProt)
      - [M SetIpProt ](#tts.lib.ethernet.PacketIp6.PacketIp6.SetIpProt)
      - [A ipProt ](#tts.lib.ethernet.PacketIp6.PacketIp6.ipProt)
      - [M GetIpHopLimit ](#tts.lib.ethernet.PacketIp6.PacketIp6.GetIpHopLimit)
      - [M SetIpHopLimit ](#tts.lib.ethernet.PacketIp6.PacketIp6.SetIpHopLimit)
      - [A ipHopLimit ](#tts.lib.ethernet.PacketIp6.PacketIp6.ipHopLimit)
      - [M GetIpSrc ](#tts.lib.ethernet.PacketIp6.PacketIp6.GetIpSrc)
      - [M SetIpSrc ](#tts.lib.ethernet.PacketIp6.PacketIp6.SetIpSrc)
      - [A ipSrc ](#tts.lib.ethernet.PacketIp6.PacketIp6.ipSrc)
      - [M GetIpDst ](#tts.lib.ethernet.PacketIp6.PacketIp6.GetIpDst)
      - [M SetIpDst ](#tts.lib.ethernet.PacketIp6.PacketIp6.SetIpDst)
      - [A ipDst ](#tts.lib.ethernet.PacketIp6.PacketIp6.ipDst)
      - [M GetIpPayload ](#tts.lib.ethernet.PacketIp6.PacketIp6.GetIpPayload)
      - [M SetIpPayload ](#tts.lib.ethernet.PacketIp6.PacketIp6.SetIpPayload)
      - [A ipPayload ](#tts.lib.ethernet.PacketIp6.PacketIp6.ipPayload)
      - [M GetIpLen ](#tts.lib.ethernet.PacketIp6.PacketIp6.GetIpLen)
      - [A ipLen ](#tts.lib.ethernet.PacketIp6.PacketIp6.ipLen)
      - [M GetIpTrafficClass ](#tts.lib.ethernet.PacketIp6.PacketIp6.GetIpTrafficClass)
      - [A ipTrafficClass ](#tts.lib.ethernet.PacketIp6.PacketIp6.ipTrafficClass)
      - [M GetIpFlowLabel ](#tts.lib.ethernet.PacketIp6.PacketIp6.GetIpFlowLabel)
      - [A ipFlowLabel ](#tts.lib.ethernet.PacketIp6.PacketIp6.ipFlowLabel)
      - [M CalcIpLen ](#tts.lib.ethernet.PacketIp6.PacketIp6.CalcIpLen)
      - [M FindParent ](#tts.lib.ethernet.PacketIp6.PacketIp6.FindParent)
      - [M GetEthDstMac ](#tts.lib.ethernet.PacketIp6.PacketIp6.GetEthDstMac)
      - [M GetEthPayload ](#tts.lib.ethernet.PacketIp6.PacketIp6.GetEthPayload)
      - [M GetEthSrcMac ](#tts.lib.ethernet.PacketIp6.PacketIp6.GetEthSrcMac)
      - [M GetEthType ](#tts.lib.ethernet.PacketIp6.PacketIp6.GetEthType)
      - [M GetMacSecAn ](#tts.lib.ethernet.PacketIp6.PacketIp6.GetMacSecAn)
      - [M GetMacSecIcv ](#tts.lib.ethernet.PacketIp6.PacketIp6.GetMacSecIcv)
      - [M GetMacSecPn ](#tts.lib.ethernet.PacketIp6.PacketIp6.GetMacSecPn)
      - [M GetMacSecSci ](#tts.lib.ethernet.PacketIp6.PacketIp6.GetMacSecSci)
      - [M GetMacSecSl ](#tts.lib.ethernet.PacketIp6.PacketIp6.GetMacSecSl)
      - [M GetMacSecTci ](#tts.lib.ethernet.PacketIp6.PacketIp6.GetMacSecTci)
      - [M GetMacSecTciAn ](#tts.lib.ethernet.PacketIp6.PacketIp6.GetMacSecTciAn)
      - [M GetMacSecTciC ](#tts.lib.ethernet.PacketIp6.PacketIp6.GetMacSecTciC)
      - [M GetMacSecTciE ](#tts.lib.ethernet.PacketIp6.PacketIp6.GetMacSecTciE)
      - [M GetMacSecTciEs ](#tts.lib.ethernet.PacketIp6.PacketIp6.GetMacSecTciEs)
      - [M GetMacSecTciSc ](#tts.lib.ethernet.PacketIp6.PacketIp6.GetMacSecTciSc)
      - [M GetMacSecTciScb ](#tts.lib.ethernet.PacketIp6.PacketIp6.GetMacSecTciScb)
      - [M GetMacSecTciV ](#tts.lib.ethernet.PacketIp6.PacketIp6.GetMacSecTciV)
      - [M GetTimestamp ](#tts.lib.ethernet.PacketIp6.PacketIp6.GetTimestamp)
      - [M GetVlanCfi ](#tts.lib.ethernet.PacketIp6.PacketIp6.GetVlanCfi)
      - [M GetVlanCfiOuter ](#tts.lib.ethernet.PacketIp6.PacketIp6.GetVlanCfiOuter)
      - [M GetVlanPcp ](#tts.lib.ethernet.PacketIp6.PacketIp6.GetVlanPcp)
      - [M GetVlanPcpOuter ](#tts.lib.ethernet.PacketIp6.PacketIp6.GetVlanPcpOuter)
      - [M GetVlanVid ](#tts.lib.ethernet.PacketIp6.PacketIp6.GetVlanVid)
      - [M GetVlanVidOuter ](#tts.lib.ethernet.PacketIp6.PacketIp6.GetVlanVidOuter)
      - [M SetEthDstMac ](#tts.lib.ethernet.PacketIp6.PacketIp6.SetEthDstMac)
      - [M SetEthPayload ](#tts.lib.ethernet.PacketIp6.PacketIp6.SetEthPayload)
      - [M SetEthSrcMac ](#tts.lib.ethernet.PacketIp6.PacketIp6.SetEthSrcMac)
      - [M SetEthType ](#tts.lib.ethernet.PacketIp6.PacketIp6.SetEthType)
      - [M SetTimestamp ](#tts.lib.ethernet.PacketIp6.PacketIp6.SetTimestamp)
      - [M SetVlanCfi ](#tts.lib.ethernet.PacketIp6.PacketIp6.SetVlanCfi)
      - [M SetVlanCfiOuter ](#tts.lib.ethernet.PacketIp6.PacketIp6.SetVlanCfiOuter)
      - [M SetVlanPcp ](#tts.lib.ethernet.PacketIp6.PacketIp6.SetVlanPcp)
      - [M SetVlanPcpOuter ](#tts.lib.ethernet.PacketIp6.PacketIp6.SetVlanPcpOuter)
      - [M SetVlanVid ](#tts.lib.ethernet.PacketIp6.PacketIp6.SetVlanVid)
      - [M SetVlanVidOuter ](#tts.lib.ethernet.PacketIp6.PacketIp6.SetVlanVidOuter)
      - [A ethDstMac ](#tts.lib.ethernet.PacketIp6.PacketIp6.ethDstMac)
      - [A ethPayload ](#tts.lib.ethernet.PacketIp6.PacketIp6.ethPayload)
      - [A ethSrcMac ](#tts.lib.ethernet.PacketIp6.PacketIp6.ethSrcMac)
      - [A ethType ](#tts.lib.ethernet.PacketIp6.PacketIp6.ethType)
      - [A macSecAn ](#tts.lib.ethernet.PacketIp6.PacketIp6.macSecAn)
      - [A macSecIcv ](#tts.lib.ethernet.PacketIp6.PacketIp6.macSecIcv)
      - [A macSecPn ](#tts.lib.ethernet.PacketIp6.PacketIp6.macSecPn)
      - [A macSecSci ](#tts.lib.ethernet.PacketIp6.PacketIp6.macSecSci)
      - [A macSecSl ](#tts.lib.ethernet.PacketIp6.PacketIp6.macSecSl)
      - [A macSecTci ](#tts.lib.ethernet.PacketIp6.PacketIp6.macSecTci)
      - [A macSecTciAn ](#tts.lib.ethernet.PacketIp6.PacketIp6.macSecTciAn)
      - [A macSecTciC ](#tts.lib.ethernet.PacketIp6.PacketIp6.macSecTciC)
      - [A macSecTciE ](#tts.lib.ethernet.PacketIp6.PacketIp6.macSecTciE)
      - [A macSecTciEs ](#tts.lib.ethernet.PacketIp6.PacketIp6.macSecTciEs)
      - [A macSecTciSc ](#tts.lib.ethernet.PacketIp6.PacketIp6.macSecTciSc)
      - [A macSecTciScb ](#tts.lib.ethernet.PacketIp6.PacketIp6.macSecTciScb)
      - [A macSecTciV ](#tts.lib.ethernet.PacketIp6.PacketIp6.macSecTciV)
      - [A parent ](#tts.lib.ethernet.PacketIp6.PacketIp6.parent)
      - [A timestamp ](#tts.lib.ethernet.PacketIp6.PacketIp6.timestamp)
      - [A vlanCfi ](#tts.lib.ethernet.PacketIp6.PacketIp6.vlanCfi)
      - [A vlanCfiOuter ](#tts.lib.ethernet.PacketIp6.PacketIp6.vlanCfiOuter)
      - [A vlanPcp ](#tts.lib.ethernet.PacketIp6.PacketIp6.vlanPcp)
      - [A vlanPcpOuter ](#tts.lib.ethernet.PacketIp6.PacketIp6.vlanPcpOuter)
      - [A vlanVid ](#tts.lib.ethernet.PacketIp6.PacketIp6.vlanVid)
      - [A vlanVidOuter ](#tts.lib.ethernet.PacketIp6.PacketIp6.vlanVidOuter)
  - [ PacketIcmp ](#packeticmp)
    - [C PacketIcmp ](#tts.lib.ethernet.PacketIcmp.PacketIcmp)
      - [M GetIcmpType ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetIcmpType)
      - [M SetIcmpType ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetIcmpType)
      - [A icmpType ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.icmpType)
      - [M GetIcmpCode ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetIcmpCode)
      - [M SetIcmpCode ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetIcmpCode)
      - [A icmpCode ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.icmpCode)
      - [M GetIcmpChecksum ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetIcmpChecksum)
      - [M SetIcmpChecksum ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetIcmpChecksum)
      - [A icmpChecksum ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.icmpChecksum)
      - [M GetIcmpPayload ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetIcmpPayload)
      - [M CalcIpLen ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.CalcIpLen)
      - [M FindParent ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.FindParent)
      - [M GetEthDstMac ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetEthDstMac)
      - [M GetEthPayload ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetEthPayload)
      - [M GetEthSrcMac ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetEthSrcMac)
      - [M GetEthType ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetEthType)
      - [M GetIpAhIcv ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetIpAhIcv)
      - [M GetIpAhLen ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetIpAhLen)
      - [M GetIpAhNxt ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetIpAhNxt)
      - [M GetIpAhRsvd ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetIpAhRsvd)
      - [M GetIpAhSeq ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetIpAhSeq)
      - [M GetIpAhSpi ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetIpAhSpi)
      - [M GetIpChecksum ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetIpChecksum)
      - [M GetIpDst ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetIpDst)
      - [M GetIpIdent ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetIpIdent)
      - [M GetIpLen ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetIpLen)
      - [M GetIpOffset ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetIpOffset)
      - [M GetIpPayload ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetIpPayload)
      - [M GetIpProt ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetIpProt)
      - [M GetIpSrc ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetIpSrc)
      - [M GetIpTos ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetIpTos)
      - [M GetIpTtl ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetIpTtl)
      - [M GetIpVersionAndHeaderLength ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetIpVersionAndHeaderLength)
      - [M GetMacSecAn ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetMacSecAn)
      - [M GetMacSecIcv ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetMacSecIcv)
      - [M GetMacSecPn ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetMacSecPn)
      - [M GetMacSecSci ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetMacSecSci)
      - [M GetMacSecSl ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetMacSecSl)
      - [M GetMacSecTci ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetMacSecTci)
      - [M GetMacSecTciAn ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetMacSecTciAn)
      - [M GetMacSecTciC ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetMacSecTciC)
      - [M GetMacSecTciE ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetMacSecTciE)
      - [M GetMacSecTciEs ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetMacSecTciEs)
      - [M GetMacSecTciSc ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetMacSecTciSc)
      - [M GetMacSecTciScb ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetMacSecTciScb)
      - [M GetMacSecTciV ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetMacSecTciV)
      - [M GetTimestamp ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetTimestamp)
      - [M GetVlanCfi ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetVlanCfi)
      - [M GetVlanCfiOuter ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetVlanCfiOuter)
      - [M GetVlanPcp ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetVlanPcp)
      - [M GetVlanPcpOuter ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetVlanPcpOuter)
      - [M GetVlanVid ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetVlanVid)
      - [M GetVlanVidOuter ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetVlanVidOuter)
      - [A PK_CLASS ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.PK_CLASS)
      - [M SetEthDstMac ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetEthDstMac)
      - [M SetEthPayload ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetEthPayload)
      - [M SetEthSrcMac ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetEthSrcMac)
      - [M SetEthType ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetEthType)
      - [M SetIcmpPayload ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetIcmpPayload)
      - [M SetIpChecksum ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetIpChecksum)
      - [M SetIpDst ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetIpDst)
      - [M SetIpIdent ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetIpIdent)
      - [M SetIpLen ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetIpLen)
      - [M SetIpOffset ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetIpOffset)
      - [M SetIpPayload ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetIpPayload)
      - [M SetIpProt ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetIpProt)
      - [M SetIpSrc ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetIpSrc)
      - [M SetIpTos ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetIpTos)
      - [M SetIpTtl ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetIpTtl)
      - [M SetIpVersionAndHeaderLength ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetIpVersionAndHeaderLength)
      - [M SetTimestamp ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetTimestamp)
      - [M SetVlanCfi ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetVlanCfi)
      - [M SetVlanCfiOuter ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetVlanCfiOuter)
      - [M SetVlanPcp ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetVlanPcp)
      - [M SetVlanPcpOuter ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetVlanPcpOuter)
      - [M SetVlanVid ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetVlanVid)
      - [M SetVlanVidOuter ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetVlanVidOuter)
      - [A ethDstMac ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.ethDstMac)
      - [A ethPayload ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.ethPayload)
      - [A ethSrcMac ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.ethSrcMac)
      - [A ethType ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.ethType)
      - [A ipAhIcv ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.ipAhIcv)
      - [A ipAhLen ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.ipAhLen)
      - [A ipAhNxt ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.ipAhNxt)
      - [A ipAhRsvd ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.ipAhRsvd)
      - [A ipAhSeq ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.ipAhSeq)
      - [A ipAhSpi ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.ipAhSpi)
      - [A ipChecksum ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.ipChecksum)
      - [A ipDst ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.ipDst)
      - [A ipIdent ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.ipIdent)
      - [A ipLen ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.ipLen)
      - [A ipOffset ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.ipOffset)
      - [A ipPayload ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.ipPayload)
      - [A ipProt ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.ipProt)
      - [A ipSrc ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.ipSrc)
      - [A ipTos ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.ipTos)
      - [A ipTtl ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.ipTtl)
      - [A ipVersionHeader ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.ipVersionHeader)
      - [A macSecAn ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.macSecAn)
      - [A macSecIcv ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.macSecIcv)
      - [A macSecPn ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.macSecPn)
      - [A macSecSci ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.macSecSci)
      - [A macSecSl ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.macSecSl)
      - [A macSecTci ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.macSecTci)
      - [A macSecTciAn ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.macSecTciAn)
      - [A macSecTciC ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.macSecTciC)
      - [A macSecTciE ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.macSecTciE)
      - [A macSecTciEs ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.macSecTciEs)
      - [A macSecTciSc ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.macSecTciSc)
      - [A macSecTciScb ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.macSecTciScb)
      - [A macSecTciV ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.macSecTciV)
      - [A parent ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.parent)
      - [A timestamp ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.timestamp)
      - [A vlanCfi ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.vlanCfi)
      - [A vlanCfiOuter ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.vlanCfiOuter)
      - [A vlanPcp ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.vlanPcp)
      - [A vlanPcpOuter ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.vlanPcpOuter)
      - [A vlanVid ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.vlanVid)
      - [A vlanVidOuter ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.vlanVidOuter)
      - [A icmpPayload ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.icmpPayload)
  - [ PacketMka ](#packetmka)
    - [C PacketMka ](#tts.lib.ethernet.PacketMka.PacketMka)
      - [M UseCak ](#tts.lib.ethernet.PacketMka.PacketMka.UseCak)
      - [M GetEthDstMac ](#tts.lib.ethernet.PacketMka.PacketMka.GetEthDstMac)
      - [M SetEthDstMac ](#tts.lib.ethernet.PacketMka.PacketMka.SetEthDstMac)
      - [A ethDstMac ](#tts.lib.ethernet.PacketMka.PacketMka.ethDstMac)
      - [M GetEthSrcMac ](#tts.lib.ethernet.PacketMka.PacketMka.GetEthSrcMac)
      - [M SetEthSrcMac ](#tts.lib.ethernet.PacketMka.PacketMka.SetEthSrcMac)
      - [A ethSrcMac ](#tts.lib.ethernet.PacketMka.PacketMka.ethSrcMac)
      - [M GetEthType ](#tts.lib.ethernet.PacketMka.PacketMka.GetEthType)
      - [M SetEthType ](#tts.lib.ethernet.PacketMka.PacketMka.SetEthType)
      - [M GetEthPayload ](#tts.lib.ethernet.PacketMka.PacketMka.GetEthPayload)
      - [M SetEthPayload ](#tts.lib.ethernet.PacketMka.PacketMka.SetEthPayload)
      - [M GetMkaIcv ](#tts.lib.ethernet.PacketMka.PacketMka.GetMkaIcv)
      - [A mkaIcv ](#tts.lib.ethernet.PacketMka.PacketMka.mkaIcv)
      - [M IsMkaIcvValid ](#tts.lib.ethernet.PacketMka.PacketMka.IsMkaIcvValid)
      - [M GetKeyServerPriority ](#tts.lib.ethernet.PacketMka.PacketMka.GetKeyServerPriority)
      - [A keyServerPriority ](#tts.lib.ethernet.PacketMka.PacketMka.keyServerPriority)
      - [M GetKeyServerFlag ](#tts.lib.ethernet.PacketMka.PacketMka.GetKeyServerFlag)
      - [A keyServerFlag ](#tts.lib.ethernet.PacketMka.PacketMka.keyServerFlag)
      - [M GetMacSecDesired ](#tts.lib.ethernet.PacketMka.PacketMka.GetMacSecDesired)
      - [A macSecDesired ](#tts.lib.ethernet.PacketMka.PacketMka.macSecDesired)
      - [M GetMacSecCapability ](#tts.lib.ethernet.PacketMka.PacketMka.GetMacSecCapability)
      - [A macSecCapability ](#tts.lib.ethernet.PacketMka.PacketMka.macSecCapability)
      - [M GetMacSecSci ](#tts.lib.ethernet.PacketMka.PacketMka.GetMacSecSci)
      - [A macSecSci ](#tts.lib.ethernet.PacketMka.PacketMka.macSecSci)
      - [M GetMemberIdentifier ](#tts.lib.ethernet.PacketMka.PacketMka.GetMemberIdentifier)
      - [A memberIdentifier ](#tts.lib.ethernet.PacketMka.PacketMka.memberIdentifier)
      - [M GetMessageNumber ](#tts.lib.ethernet.PacketMka.PacketMka.GetMessageNumber)
      - [A messageNumber ](#tts.lib.ethernet.PacketMka.PacketMka.messageNumber)
      - [M GetCakName ](#tts.lib.ethernet.PacketMka.PacketMka.GetCakName)
      - [A cakName ](#tts.lib.ethernet.PacketMka.PacketMka.cakName)
      - [M GetLivePeerListMemberIdentifiers ](#tts.lib.ethernet.PacketMka.PacketMka.GetLivePeerListMemberIdentifiers)
      - [A livePeerListMemberIdentifiers ](#tts.lib.ethernet.PacketMka.PacketMka.livePeerListMemberIdentifiers)
      - [M GetLivePeerListMessageNumbers ](#tts.lib.ethernet.PacketMka.PacketMka.GetLivePeerListMessageNumbers)
      - [A livePeerListMessageNumbers ](#tts.lib.ethernet.PacketMka.PacketMka.livePeerListMessageNumbers)
      - [M GetLivePeerListKeyServerSsci ](#tts.lib.ethernet.PacketMka.PacketMka.GetLivePeerListKeyServerSsci)
      - [A livePeerListKeyServerSsci ](#tts.lib.ethernet.PacketMka.PacketMka.livePeerListKeyServerSsci)
      - [M RemoveLivePeerList ](#tts.lib.ethernet.PacketMka.PacketMka.RemoveLivePeerList)
      - [M GetPotentialPeerListMemberIdentifiers ](#tts.lib.ethernet.PacketMka.PacketMka.GetPotentialPeerListMemberIdentifiers)
      - [A potentialPeerListMemberIdentifiers ](#tts.lib.ethernet.PacketMka.PacketMka.potentialPeerListMemberIdentifiers)
      - [M GetPotentialPeerListMessageNumbers ](#tts.lib.ethernet.PacketMka.PacketMka.GetPotentialPeerListMessageNumbers)
      - [A potentialPeerListMessageNumbers ](#tts.lib.ethernet.PacketMka.PacketMka.potentialPeerListMessageNumbers)
      - [M RemovePotentialPeerList ](#tts.lib.ethernet.PacketMka.PacketMka.RemovePotentialPeerList)
      - [M GetSakUseLatestAn ](#tts.lib.ethernet.PacketMka.PacketMka.GetSakUseLatestAn)
      - [A sakUseLatestAn ](#tts.lib.ethernet.PacketMka.PacketMka.sakUseLatestAn)
      - [M GetSakUseLatestTx ](#tts.lib.ethernet.PacketMka.PacketMka.GetSakUseLatestTx)
      - [A sakUseLatestTx ](#tts.lib.ethernet.PacketMka.PacketMka.sakUseLatestTx)
      - [M GetSakUseLatestRx ](#tts.lib.ethernet.PacketMka.PacketMka.GetSakUseLatestRx)
      - [A sakUseLatestRx ](#tts.lib.ethernet.PacketMka.PacketMka.sakUseLatestRx)
      - [M GetSakUsePlainTx ](#tts.lib.ethernet.PacketMka.PacketMka.GetSakUsePlainTx)
      - [A sakUsePlainTx ](#tts.lib.ethernet.PacketMka.PacketMka.sakUsePlainTx)
      - [M GetSakUsePlainRx ](#tts.lib.ethernet.PacketMka.PacketMka.GetSakUsePlainRx)
      - [A sakUsePlainRx ](#tts.lib.ethernet.PacketMka.PacketMka.sakUsePlainRx)
      - [M GetSakUseDelayProtect ](#tts.lib.ethernet.PacketMka.PacketMka.GetSakUseDelayProtect)
      - [A sakUseDelayProtect ](#tts.lib.ethernet.PacketMka.PacketMka.sakUseDelayProtect)
      - [M GetSakUseLatestKeyServerMemberIdentifier ](#tts.lib.ethernet.PacketMka.PacketMka.GetSakUseLatestKeyServerMemberIdentifier)
      - [A sakUseLatestKeyServerMemberIdentifier ](#tts.lib.ethernet.PacketMka.PacketMka.sakUseLatestKeyServerMemberIdentifier)
      - [M GetSakUseLatestKeyNumber ](#tts.lib.ethernet.PacketMka.PacketMka.GetSakUseLatestKeyNumber)
      - [A sakUseLatestKeyNumber ](#tts.lib.ethernet.PacketMka.PacketMka.sakUseLatestKeyNumber)
      - [M GetSakUseLatestLpn ](#tts.lib.ethernet.PacketMka.PacketMka.GetSakUseLatestLpn)
      - [A sakUseLatestLpn ](#tts.lib.ethernet.PacketMka.PacketMka.sakUseLatestLpn)
      - [M RemoveSakUse ](#tts.lib.ethernet.PacketMka.PacketMka.RemoveSakUse)
      - [M GetDistributedSakWrappedKey ](#tts.lib.ethernet.PacketMka.PacketMka.GetDistributedSakWrappedKey)
      - [A distributedSakWrappedKey ](#tts.lib.ethernet.PacketMka.PacketMka.distributedSakWrappedKey)
      - [M GetDistributedSakUnwrappedKey ](#tts.lib.ethernet.PacketMka.PacketMka.GetDistributedSakUnwrappedKey)
      - [A distributedSakUnwrappedKey ](#tts.lib.ethernet.PacketMka.PacketMka.distributedSakUnwrappedKey)
      - [M GetDistributedSakAn ](#tts.lib.ethernet.PacketMka.PacketMka.GetDistributedSakAn)
      - [A distributedSakAn ](#tts.lib.ethernet.PacketMka.PacketMka.distributedSakAn)
      - [M GetDistributedSakConfidentialityOffset ](#tts.lib.ethernet.PacketMka.PacketMka.GetDistributedSakConfidentialityOffset)
      - [A distributedSakConfidentialityOffset ](#tts.lib.ethernet.PacketMka.PacketMka.distributedSakConfidentialityOffset)
      - [M GetDistributedSakKeyNumber ](#tts.lib.ethernet.PacketMka.PacketMka.GetDistributedSakKeyNumber)
      - [A distributedSakKeyNumber ](#tts.lib.ethernet.PacketMka.PacketMka.distributedSakKeyNumber)
      - [M GetDistributedSakCipherSuite ](#tts.lib.ethernet.PacketMka.PacketMka.GetDistributedSakCipherSuite)
      - [A distributedSakCipherSuite ](#tts.lib.ethernet.PacketMka.PacketMka.distributedSakCipherSuite)
      - [M SetDistributedSakToNoMacSec ](#tts.lib.ethernet.PacketMka.PacketMka.SetDistributedSakToNoMacSec)
      - [M RemoveDistributedSak ](#tts.lib.ethernet.PacketMka.PacketMka.RemoveDistributedSak)
      - [M GetXpnLatestLpn ](#tts.lib.ethernet.PacketMka.PacketMka.GetXpnLatestLpn)
      - [A xpnLatestLpn ](#tts.lib.ethernet.PacketMka.PacketMka.xpnLatestLpn)
      - [M RemoveXpn ](#tts.lib.ethernet.PacketMka.PacketMka.RemoveXpn)
      - [M GetAnnouncementTypes ](#tts.lib.ethernet.PacketMka.PacketMka.GetAnnouncementTypes)
      - [A announcementTypes ](#tts.lib.ethernet.PacketMka.PacketMka.announcementTypes)
      - [M GetAnnouncementInfos ](#tts.lib.ethernet.PacketMka.PacketMka.GetAnnouncementInfos)
      - [A announcementInfos ](#tts.lib.ethernet.PacketMka.PacketMka.announcementInfos)
      - [M GetAnnouncementCipherSuiteCapabilities ](#tts.lib.ethernet.PacketMka.PacketMka.GetAnnouncementCipherSuiteCapabilities)
      - [A announcementCipherSuiteCapabilities ](#tts.lib.ethernet.PacketMka.PacketMka.announcementCipherSuiteCapabilities)
      - [M GetAnnouncementCipherSuiteNames ](#tts.lib.ethernet.PacketMka.PacketMka.GetAnnouncementCipherSuiteNames)
      - [A announcementCipherSuiteNames ](#tts.lib.ethernet.PacketMka.PacketMka.announcementCipherSuiteNames)
      - [M FindParent ](#tts.lib.ethernet.PacketMka.PacketMka.FindParent)
      - [M GetMacSecAn ](#tts.lib.ethernet.PacketMka.PacketMka.GetMacSecAn)
      - [M GetMacSecIcv ](#tts.lib.ethernet.PacketMka.PacketMka.GetMacSecIcv)
      - [M GetMacSecPn ](#tts.lib.ethernet.PacketMka.PacketMka.GetMacSecPn)
      - [M GetMacSecSl ](#tts.lib.ethernet.PacketMka.PacketMka.GetMacSecSl)
      - [M GetMacSecTci ](#tts.lib.ethernet.PacketMka.PacketMka.GetMacSecTci)
      - [M GetMacSecTciAn ](#tts.lib.ethernet.PacketMka.PacketMka.GetMacSecTciAn)
      - [M GetMacSecTciC ](#tts.lib.ethernet.PacketMka.PacketMka.GetMacSecTciC)
      - [M GetMacSecTciE ](#tts.lib.ethernet.PacketMka.PacketMka.GetMacSecTciE)
      - [M GetMacSecTciEs ](#tts.lib.ethernet.PacketMka.PacketMka.GetMacSecTciEs)
      - [M GetMacSecTciSc ](#tts.lib.ethernet.PacketMka.PacketMka.GetMacSecTciSc)
      - [M GetMacSecTciScb ](#tts.lib.ethernet.PacketMka.PacketMka.GetMacSecTciScb)
      - [M GetMacSecTciV ](#tts.lib.ethernet.PacketMka.PacketMka.GetMacSecTciV)
      - [M GetTimestamp ](#tts.lib.ethernet.PacketMka.PacketMka.GetTimestamp)
      - [M GetVlanCfi ](#tts.lib.ethernet.PacketMka.PacketMka.GetVlanCfi)
      - [M GetVlanCfiOuter ](#tts.lib.ethernet.PacketMka.PacketMka.GetVlanCfiOuter)
      - [M GetVlanPcp ](#tts.lib.ethernet.PacketMka.PacketMka.GetVlanPcp)
      - [M GetVlanPcpOuter ](#tts.lib.ethernet.PacketMka.PacketMka.GetVlanPcpOuter)
      - [M GetVlanVid ](#tts.lib.ethernet.PacketMka.PacketMka.GetVlanVid)
      - [M GetVlanVidOuter ](#tts.lib.ethernet.PacketMka.PacketMka.GetVlanVidOuter)
      - [M RemoveAnnouncement ](#tts.lib.ethernet.PacketMka.PacketMka.RemoveAnnouncement)
      - [M SetTimestamp ](#tts.lib.ethernet.PacketMka.PacketMka.SetTimestamp)
      - [M SetVlanCfi ](#tts.lib.ethernet.PacketMka.PacketMka.SetVlanCfi)
      - [M SetVlanCfiOuter ](#tts.lib.ethernet.PacketMka.PacketMka.SetVlanCfiOuter)
      - [M SetVlanPcp ](#tts.lib.ethernet.PacketMka.PacketMka.SetVlanPcp)
      - [M SetVlanPcpOuter ](#tts.lib.ethernet.PacketMka.PacketMka.SetVlanPcpOuter)
      - [M SetVlanVid ](#tts.lib.ethernet.PacketMka.PacketMka.SetVlanVid)
      - [M SetVlanVidOuter ](#tts.lib.ethernet.PacketMka.PacketMka.SetVlanVidOuter)
      - [A ethPayload ](#tts.lib.ethernet.PacketMka.PacketMka.ethPayload)
      - [A ethType ](#tts.lib.ethernet.PacketMka.PacketMka.ethType)
      - [A macSecAn ](#tts.lib.ethernet.PacketMka.PacketMka.macSecAn)
      - [A macSecIcv ](#tts.lib.ethernet.PacketMka.PacketMka.macSecIcv)
      - [A macSecPn ](#tts.lib.ethernet.PacketMka.PacketMka.macSecPn)
      - [A macSecSl ](#tts.lib.ethernet.PacketMka.PacketMka.macSecSl)
      - [A macSecTci ](#tts.lib.ethernet.PacketMka.PacketMka.macSecTci)
      - [A macSecTciAn ](#tts.lib.ethernet.PacketMka.PacketMka.macSecTciAn)
      - [A macSecTciC ](#tts.lib.ethernet.PacketMka.PacketMka.macSecTciC)
      - [A macSecTciE ](#tts.lib.ethernet.PacketMka.PacketMka.macSecTciE)
      - [A macSecTciEs ](#tts.lib.ethernet.PacketMka.PacketMka.macSecTciEs)
      - [A macSecTciSc ](#tts.lib.ethernet.PacketMka.PacketMka.macSecTciSc)
      - [A macSecTciScb ](#tts.lib.ethernet.PacketMka.PacketMka.macSecTciScb)
      - [A macSecTciV ](#tts.lib.ethernet.PacketMka.PacketMka.macSecTciV)
      - [A parent ](#tts.lib.ethernet.PacketMka.PacketMka.parent)
      - [A timestamp ](#tts.lib.ethernet.PacketMka.PacketMka.timestamp)
      - [A vlanCfi ](#tts.lib.ethernet.PacketMka.PacketMka.vlanCfi)
      - [A vlanCfiOuter ](#tts.lib.ethernet.PacketMka.PacketMka.vlanCfiOuter)
      - [A vlanPcp ](#tts.lib.ethernet.PacketMka.PacketMka.vlanPcp)
      - [A vlanPcpOuter ](#tts.lib.ethernet.PacketMka.PacketMka.vlanPcpOuter)
      - [A vlanVid ](#tts.lib.ethernet.PacketMka.PacketMka.vlanVid)
      - [A vlanVidOuter ](#tts.lib.ethernet.PacketMka.PacketMka.vlanVidOuter)
  - [ PacketIke ](#packetike)
    - [C PacketIke ](#tts.lib.ethernet.PacketIke.PacketIke)
      - [M GetInitiatorSpi ](#tts.lib.ethernet.PacketIke.PacketIke.GetInitiatorSpi)
      - [A initiatorSpi ](#tts.lib.ethernet.PacketIke.PacketIke.initiatorSpi)
      - [M GetResponderSpi ](#tts.lib.ethernet.PacketIke.PacketIke.GetResponderSpi)
      - [A responderSpi ](#tts.lib.ethernet.PacketIke.PacketIke.responderSpi)
      - [M GetNextPayload ](#tts.lib.ethernet.PacketIke.PacketIke.GetNextPayload)
      - [A nextPayload ](#tts.lib.ethernet.PacketIke.PacketIke.nextPayload)
      - [M GetMajorVersion ](#tts.lib.ethernet.PacketIke.PacketIke.GetMajorVersion)
      - [A majorVersion ](#tts.lib.ethernet.PacketIke.PacketIke.majorVersion)
      - [M GetMinorVersion ](#tts.lib.ethernet.PacketIke.PacketIke.GetMinorVersion)
      - [A minorVersion ](#tts.lib.ethernet.PacketIke.PacketIke.minorVersion)
      - [M GetExchangeType ](#tts.lib.ethernet.PacketIke.PacketIke.GetExchangeType)
      - [A exchangeType ](#tts.lib.ethernet.PacketIke.PacketIke.exchangeType)
      - [M GetFlags ](#tts.lib.ethernet.PacketIke.PacketIke.GetFlags)
      - [A flags ](#tts.lib.ethernet.PacketIke.PacketIke.flags)
      - [M IsInitiator ](#tts.lib.ethernet.PacketIke.PacketIke.IsInitiator)
      - [M IsResponder ](#tts.lib.ethernet.PacketIke.PacketIke.IsResponder)
      - [M SetToInitiator ](#tts.lib.ethernet.PacketIke.PacketIke.SetToInitiator)
      - [M SetToResponder ](#tts.lib.ethernet.PacketIke.PacketIke.SetToResponder)
      - [M IsRequest ](#tts.lib.ethernet.PacketIke.PacketIke.IsRequest)
      - [M IsResponse ](#tts.lib.ethernet.PacketIke.PacketIke.IsResponse)
      - [M SetToRequest ](#tts.lib.ethernet.PacketIke.PacketIke.SetToRequest)
      - [M SetToReponse ](#tts.lib.ethernet.PacketIke.PacketIke.SetToReponse)
      - [M GetMessageId ](#tts.lib.ethernet.PacketIke.PacketIke.GetMessageId)
      - [A messageId ](#tts.lib.ethernet.PacketIke.PacketIke.messageId)
      - [M GetLength ](#tts.lib.ethernet.PacketIke.PacketIke.GetLength)
      - [A length ](#tts.lib.ethernet.PacketIke.PacketIke.length)
      - [M GetKeyExchangeNextPayload ](#tts.lib.ethernet.PacketIke.PacketIke.GetKeyExchangeNextPayload)
      - [A keyExchangeNextPayload ](#tts.lib.ethernet.PacketIke.PacketIke.keyExchangeNextPayload)
      - [M IsKeyExchangeCritical ](#tts.lib.ethernet.PacketIke.PacketIke.IsKeyExchangeCritical)
      - [A keyExchangeCritical ](#tts.lib.ethernet.PacketIke.PacketIke.keyExchangeCritical)
      - [M GetKeyExchangeLength ](#tts.lib.ethernet.PacketIke.PacketIke.GetKeyExchangeLength)
      - [A keyExchangeLength ](#tts.lib.ethernet.PacketIke.PacketIke.keyExchangeLength)
      - [M GetKeyExchangeDhGroupNumber ](#tts.lib.ethernet.PacketIke.PacketIke.GetKeyExchangeDhGroupNumber)
      - [A keyExchangeDhGroupNumber ](#tts.lib.ethernet.PacketIke.PacketIke.keyExchangeDhGroupNumber)
      - [M GetKeyExchangeData ](#tts.lib.ethernet.PacketIke.PacketIke.GetKeyExchangeData)
      - [A keyExchangeData ](#tts.lib.ethernet.PacketIke.PacketIke.keyExchangeData)
      - [M GetNonceNextPayload ](#tts.lib.ethernet.PacketIke.PacketIke.GetNonceNextPayload)
      - [A nonceNextPayload ](#tts.lib.ethernet.PacketIke.PacketIke.nonceNextPayload)
      - [M IsNonceCritical ](#tts.lib.ethernet.PacketIke.PacketIke.IsNonceCritical)
      - [A nonceCritical ](#tts.lib.ethernet.PacketIke.PacketIke.nonceCritical)
      - [M GetNonceLength ](#tts.lib.ethernet.PacketIke.PacketIke.GetNonceLength)
      - [A nonceLength ](#tts.lib.ethernet.PacketIke.PacketIke.nonceLength)
      - [M GetNonceData ](#tts.lib.ethernet.PacketIke.PacketIke.GetNonceData)
      - [A nonceData ](#tts.lib.ethernet.PacketIke.PacketIke.nonceData)
      - [M GetCertificateNextPayload ](#tts.lib.ethernet.PacketIke.PacketIke.GetCertificateNextPayload)
      - [A certificateNextPayload ](#tts.lib.ethernet.PacketIke.PacketIke.certificateNextPayload)
      - [M IsCertificateCritical ](#tts.lib.ethernet.PacketIke.PacketIke.IsCertificateCritical)
      - [A certificateCritical ](#tts.lib.ethernet.PacketIke.PacketIke.certificateCritical)
      - [M GetCertificateLength ](#tts.lib.ethernet.PacketIke.PacketIke.GetCertificateLength)
      - [A certificateLength ](#tts.lib.ethernet.PacketIke.PacketIke.certificateLength)
      - [M GetCertificateEncoding ](#tts.lib.ethernet.PacketIke.PacketIke.GetCertificateEncoding)
      - [A certificateEncoding ](#tts.lib.ethernet.PacketIke.PacketIke.certificateEncoding)
      - [M GetCertificateData ](#tts.lib.ethernet.PacketIke.PacketIke.GetCertificateData)
      - [A certificateData ](#tts.lib.ethernet.PacketIke.PacketIke.certificateData)
      - [M GetCertificateRequestNextPayload ](#tts.lib.ethernet.PacketIke.PacketIke.GetCertificateRequestNextPayload)
      - [A certificateRequestNextPayload ](#tts.lib.ethernet.PacketIke.PacketIke.certificateRequestNextPayload)
      - [M GetCertificateRequestCritical ](#tts.lib.ethernet.PacketIke.PacketIke.GetCertificateRequestCritical)
      - [A certificateRequestCritical ](#tts.lib.ethernet.PacketIke.PacketIke.certificateRequestCritical)
      - [M GetCertificateRequestLength ](#tts.lib.ethernet.PacketIke.PacketIke.GetCertificateRequestLength)
      - [A certificateRequestLength ](#tts.lib.ethernet.PacketIke.PacketIke.certificateRequestLength)
      - [M GetCertificateRequestData ](#tts.lib.ethernet.PacketIke.PacketIke.GetCertificateRequestData)
      - [A certificateRequestData ](#tts.lib.ethernet.PacketIke.PacketIke.certificateRequestData)
      - [M GetCertificateRequestEncoding ](#tts.lib.ethernet.PacketIke.PacketIke.GetCertificateRequestEncoding)
      - [A certificateRequestEncoding ](#tts.lib.ethernet.PacketIke.PacketIke.certificateRequestEncoding)
      - [M GetIdentInitiatorNextPayload ](#tts.lib.ethernet.PacketIke.PacketIke.GetIdentInitiatorNextPayload)
      - [A identInitiatorNextPayload ](#tts.lib.ethernet.PacketIke.PacketIke.identInitiatorNextPayload)
      - [M GetIdentInitiatorCritical ](#tts.lib.ethernet.PacketIke.PacketIke.GetIdentInitiatorCritical)
      - [A identInitiatorCritical ](#tts.lib.ethernet.PacketIke.PacketIke.identInitiatorCritical)
      - [M GetIdentInitiatorLength ](#tts.lib.ethernet.PacketIke.PacketIke.GetIdentInitiatorLength)
      - [A identInitiatorLength ](#tts.lib.ethernet.PacketIke.PacketIke.identInitiatorLength)
      - [M GetIdentInitiatorIdType ](#tts.lib.ethernet.PacketIke.PacketIke.GetIdentInitiatorIdType)
      - [A identInitiatorIdType ](#tts.lib.ethernet.PacketIke.PacketIke.identInitiatorIdType)
      - [M GetIdentInitiatorData ](#tts.lib.ethernet.PacketIke.PacketIke.GetIdentInitiatorData)
      - [A identInitiatorData ](#tts.lib.ethernet.PacketIke.PacketIke.identInitiatorData)
      - [M GetIdentResponderNextPayload ](#tts.lib.ethernet.PacketIke.PacketIke.GetIdentResponderNextPayload)
      - [A identResponderNextPayload ](#tts.lib.ethernet.PacketIke.PacketIke.identResponderNextPayload)
      - [M GetIdentResponderCritical ](#tts.lib.ethernet.PacketIke.PacketIke.GetIdentResponderCritical)
      - [A identResponderCritical ](#tts.lib.ethernet.PacketIke.PacketIke.identResponderCritical)
      - [M GetIdentResponderLength ](#tts.lib.ethernet.PacketIke.PacketIke.GetIdentResponderLength)
      - [A identResponderLength ](#tts.lib.ethernet.PacketIke.PacketIke.identResponderLength)
      - [M GetIdentResponderIdType ](#tts.lib.ethernet.PacketIke.PacketIke.GetIdentResponderIdType)
      - [A identResponderIdType ](#tts.lib.ethernet.PacketIke.PacketIke.identResponderIdType)
      - [M GetIdentResponderData ](#tts.lib.ethernet.PacketIke.PacketIke.GetIdentResponderData)
      - [A identResponderData ](#tts.lib.ethernet.PacketIke.PacketIke.identResponderData)
      - [M GetAuthNextPayload ](#tts.lib.ethernet.PacketIke.PacketIke.GetAuthNextPayload)
      - [A authNextPayload ](#tts.lib.ethernet.PacketIke.PacketIke.authNextPayload)
      - [M GetAuthCritical ](#tts.lib.ethernet.PacketIke.PacketIke.GetAuthCritical)
      - [A authCritical ](#tts.lib.ethernet.PacketIke.PacketIke.authCritical)
      - [M GetAuthLength ](#tts.lib.ethernet.PacketIke.PacketIke.GetAuthLength)
      - [A authLength ](#tts.lib.ethernet.PacketIke.PacketIke.authLength)
      - [M GetAuthMethod ](#tts.lib.ethernet.PacketIke.PacketIke.GetAuthMethod)
      - [A authMethod ](#tts.lib.ethernet.PacketIke.PacketIke.authMethod)
      - [M GetAuthData ](#tts.lib.ethernet.PacketIke.PacketIke.GetAuthData)
      - [A authData ](#tts.lib.ethernet.PacketIke.PacketIke.authData)
      - [M GetTsInitiatorNextPayload ](#tts.lib.ethernet.PacketIke.PacketIke.GetTsInitiatorNextPayload)
      - [A tsInitiatorNextPayload ](#tts.lib.ethernet.PacketIke.PacketIke.tsInitiatorNextPayload)
      - [M GetTsInitiatorCritical ](#tts.lib.ethernet.PacketIke.PacketIke.GetTsInitiatorCritical)
      - [A tsInitiatorCritical ](#tts.lib.ethernet.PacketIke.PacketIke.tsInitiatorCritical)
      - [M GetTsInitiatorLength ](#tts.lib.ethernet.PacketIke.PacketIke.GetTsInitiatorLength)
      - [A tsInitiatorLength ](#tts.lib.ethernet.PacketIke.PacketIke.tsInitiatorLength)
      - [M GetTsInitiatorNumOfTss ](#tts.lib.ethernet.PacketIke.PacketIke.GetTsInitiatorNumOfTss)
      - [A tsInitiatorNumOfTss ](#tts.lib.ethernet.PacketIke.PacketIke.tsInitiatorNumOfTss)
      - [M GetTsInitiatorTrafficSelectors ](#tts.lib.ethernet.PacketIke.PacketIke.GetTsInitiatorTrafficSelectors)
      - [A tsInitiatorTrafficSelectors ](#tts.lib.ethernet.PacketIke.PacketIke.tsInitiatorTrafficSelectors)
      - [M GetTsResponderNextPayload ](#tts.lib.ethernet.PacketIke.PacketIke.GetTsResponderNextPayload)
      - [A tsResponderNextPayload ](#tts.lib.ethernet.PacketIke.PacketIke.tsResponderNextPayload)
      - [M GetTsResponderCritical ](#tts.lib.ethernet.PacketIke.PacketIke.GetTsResponderCritical)
      - [A tsResponderCritical ](#tts.lib.ethernet.PacketIke.PacketIke.tsResponderCritical)
      - [M GetTsResponderLength ](#tts.lib.ethernet.PacketIke.PacketIke.GetTsResponderLength)
      - [A tsResponderLength ](#tts.lib.ethernet.PacketIke.PacketIke.tsResponderLength)
      - [M GetTsResponderNumOfTss ](#tts.lib.ethernet.PacketIke.PacketIke.GetTsResponderNumOfTss)
      - [A tsResponderNumOfTss ](#tts.lib.ethernet.PacketIke.PacketIke.tsResponderNumOfTss)
      - [M GetTsResponderTrafficSelectors ](#tts.lib.ethernet.PacketIke.PacketIke.GetTsResponderTrafficSelectors)
      - [A tsResponderTrafficSelectors ](#tts.lib.ethernet.PacketIke.PacketIke.tsResponderTrafficSelectors)
      - [M GetSaNextPayload ](#tts.lib.ethernet.PacketIke.PacketIke.GetSaNextPayload)
      - [A saNextPayload ](#tts.lib.ethernet.PacketIke.PacketIke.saNextPayload)
      - [M GetSaCritical ](#tts.lib.ethernet.PacketIke.PacketIke.GetSaCritical)
      - [A saCritical ](#tts.lib.ethernet.PacketIke.PacketIke.saCritical)
      - [M GetSaLength ](#tts.lib.ethernet.PacketIke.PacketIke.GetSaLength)
      - [A saLength ](#tts.lib.ethernet.PacketIke.PacketIke.saLength)
      - [M GetSaProposals ](#tts.lib.ethernet.PacketIke.PacketIke.GetSaProposals)
      - [A saProposals ](#tts.lib.ethernet.PacketIke.PacketIke.saProposals)
      - [M GetNotifyNumOfPayloads ](#tts.lib.ethernet.PacketIke.PacketIke.GetNotifyNumOfPayloads)
      - [A notifyNumOfPayloads ](#tts.lib.ethernet.PacketIke.PacketIke.notifyNumOfPayloads)
      - [M GetNotifyNextPayload ](#tts.lib.ethernet.PacketIke.PacketIke.GetNotifyNextPayload)
      - [A notifyNextPayload ](#tts.lib.ethernet.PacketIke.PacketIke.notifyNextPayload)
      - [M GetNotifyCritical ](#tts.lib.ethernet.PacketIke.PacketIke.GetNotifyCritical)
      - [A notifyCritical ](#tts.lib.ethernet.PacketIke.PacketIke.notifyCritical)
      - [M GetNotifyLength ](#tts.lib.ethernet.PacketIke.PacketIke.GetNotifyLength)
      - [A notifyLength ](#tts.lib.ethernet.PacketIke.PacketIke.notifyLength)
      - [M GetNotifyProtocolId ](#tts.lib.ethernet.PacketIke.PacketIke.GetNotifyProtocolId)
      - [A notifyProtocolId ](#tts.lib.ethernet.PacketIke.PacketIke.notifyProtocolId)
      - [M GetNotifySpiSize ](#tts.lib.ethernet.PacketIke.PacketIke.GetNotifySpiSize)
      - [A notifySpiSize ](#tts.lib.ethernet.PacketIke.PacketIke.notifySpiSize)
      - [M GetNotifyMessageType ](#tts.lib.ethernet.PacketIke.PacketIke.GetNotifyMessageType)
      - [A notifyMessageType ](#tts.lib.ethernet.PacketIke.PacketIke.notifyMessageType)
      - [M GetNotifySpi ](#tts.lib.ethernet.PacketIke.PacketIke.GetNotifySpi)
      - [A notifySpi ](#tts.lib.ethernet.PacketIke.PacketIke.notifySpi)
      - [M GetNotifyData ](#tts.lib.ethernet.PacketIke.PacketIke.GetNotifyData)
      - [A notifyData ](#tts.lib.ethernet.PacketIke.PacketIke.notifyData)
      - [M GetDeleteNextPayload ](#tts.lib.ethernet.PacketIke.PacketIke.GetDeleteNextPayload)
      - [A deleteNextPayload ](#tts.lib.ethernet.PacketIke.PacketIke.deleteNextPayload)
      - [M GetDeleteCritical ](#tts.lib.ethernet.PacketIke.PacketIke.GetDeleteCritical)
      - [A deleteCritical ](#tts.lib.ethernet.PacketIke.PacketIke.deleteCritical)
      - [M GetDeleteLength ](#tts.lib.ethernet.PacketIke.PacketIke.GetDeleteLength)
      - [A deleteLength ](#tts.lib.ethernet.PacketIke.PacketIke.deleteLength)
      - [M GetDeleteProtocolId ](#tts.lib.ethernet.PacketIke.PacketIke.GetDeleteProtocolId)
      - [A deleteProtocolId ](#tts.lib.ethernet.PacketIke.PacketIke.deleteProtocolId)
      - [M GetDeleteSpiSize ](#tts.lib.ethernet.PacketIke.PacketIke.GetDeleteSpiSize)
      - [A deleteSpiSize ](#tts.lib.ethernet.PacketIke.PacketIke.deleteSpiSize)
      - [M GetDeleteSpis ](#tts.lib.ethernet.PacketIke.PacketIke.GetDeleteSpis)
      - [M CalcIpLen ](#tts.lib.ethernet.PacketIke.PacketIke.CalcIpLen)
      - [M CalcUdpLen ](#tts.lib.ethernet.PacketIke.PacketIke.CalcUdpLen)
      - [M FindParent ](#tts.lib.ethernet.PacketIke.PacketIke.FindParent)
      - [M GetEthDstMac ](#tts.lib.ethernet.PacketIke.PacketIke.GetEthDstMac)
      - [M GetEthPayload ](#tts.lib.ethernet.PacketIke.PacketIke.GetEthPayload)
      - [M GetEthSrcMac ](#tts.lib.ethernet.PacketIke.PacketIke.GetEthSrcMac)
      - [M GetEthType ](#tts.lib.ethernet.PacketIke.PacketIke.GetEthType)
      - [M GetIpAhIcv ](#tts.lib.ethernet.PacketIke.PacketIke.GetIpAhIcv)
      - [M GetIpAhLen ](#tts.lib.ethernet.PacketIke.PacketIke.GetIpAhLen)
      - [M GetIpAhNxt ](#tts.lib.ethernet.PacketIke.PacketIke.GetIpAhNxt)
      - [M GetIpAhRsvd ](#tts.lib.ethernet.PacketIke.PacketIke.GetIpAhRsvd)
      - [M GetIpAhSeq ](#tts.lib.ethernet.PacketIke.PacketIke.GetIpAhSeq)
      - [M GetIpAhSpi ](#tts.lib.ethernet.PacketIke.PacketIke.GetIpAhSpi)
      - [M GetIpChecksum ](#tts.lib.ethernet.PacketIke.PacketIke.GetIpChecksum)
      - [M GetIpDst ](#tts.lib.ethernet.PacketIke.PacketIke.GetIpDst)
      - [M GetIpIdent ](#tts.lib.ethernet.PacketIke.PacketIke.GetIpIdent)
      - [M GetIpLen ](#tts.lib.ethernet.PacketIke.PacketIke.GetIpLen)
      - [M GetIpOffset ](#tts.lib.ethernet.PacketIke.PacketIke.GetIpOffset)
      - [M GetIpPayload ](#tts.lib.ethernet.PacketIke.PacketIke.GetIpPayload)
      - [M GetIpProt ](#tts.lib.ethernet.PacketIke.PacketIke.GetIpProt)
      - [M GetIpSrc ](#tts.lib.ethernet.PacketIke.PacketIke.GetIpSrc)
      - [M GetIpTos ](#tts.lib.ethernet.PacketIke.PacketIke.GetIpTos)
      - [M GetIpTtl ](#tts.lib.ethernet.PacketIke.PacketIke.GetIpTtl)
      - [M GetIpVersionAndHeaderLength ](#tts.lib.ethernet.PacketIke.PacketIke.GetIpVersionAndHeaderLength)
      - [M GetMacSecAn ](#tts.lib.ethernet.PacketIke.PacketIke.GetMacSecAn)
      - [M GetMacSecIcv ](#tts.lib.ethernet.PacketIke.PacketIke.GetMacSecIcv)
      - [M GetMacSecPn ](#tts.lib.ethernet.PacketIke.PacketIke.GetMacSecPn)
      - [M GetMacSecSci ](#tts.lib.ethernet.PacketIke.PacketIke.GetMacSecSci)
      - [M GetMacSecSl ](#tts.lib.ethernet.PacketIke.PacketIke.GetMacSecSl)
      - [M GetMacSecTci ](#tts.lib.ethernet.PacketIke.PacketIke.GetMacSecTci)
      - [M GetMacSecTciAn ](#tts.lib.ethernet.PacketIke.PacketIke.GetMacSecTciAn)
      - [M GetMacSecTciC ](#tts.lib.ethernet.PacketIke.PacketIke.GetMacSecTciC)
      - [M GetMacSecTciE ](#tts.lib.ethernet.PacketIke.PacketIke.GetMacSecTciE)
      - [M GetMacSecTciEs ](#tts.lib.ethernet.PacketIke.PacketIke.GetMacSecTciEs)
      - [M GetMacSecTciSc ](#tts.lib.ethernet.PacketIke.PacketIke.GetMacSecTciSc)
      - [M GetMacSecTciScb ](#tts.lib.ethernet.PacketIke.PacketIke.GetMacSecTciScb)
      - [M GetMacSecTciV ](#tts.lib.ethernet.PacketIke.PacketIke.GetMacSecTciV)
      - [M GetTimestamp ](#tts.lib.ethernet.PacketIke.PacketIke.GetTimestamp)
      - [M GetUdpChecksum ](#tts.lib.ethernet.PacketIke.PacketIke.GetUdpChecksum)
      - [M GetUdpDst ](#tts.lib.ethernet.PacketIke.PacketIke.GetUdpDst)
      - [M GetUdpLen ](#tts.lib.ethernet.PacketIke.PacketIke.GetUdpLen)
      - [M GetUdpPayload ](#tts.lib.ethernet.PacketIke.PacketIke.GetUdpPayload)
      - [M GetUdpSrc ](#tts.lib.ethernet.PacketIke.PacketIke.GetUdpSrc)
      - [M GetVlanCfi ](#tts.lib.ethernet.PacketIke.PacketIke.GetVlanCfi)
      - [M GetVlanCfiOuter ](#tts.lib.ethernet.PacketIke.PacketIke.GetVlanCfiOuter)
      - [M GetVlanPcp ](#tts.lib.ethernet.PacketIke.PacketIke.GetVlanPcp)
      - [M GetVlanPcpOuter ](#tts.lib.ethernet.PacketIke.PacketIke.GetVlanPcpOuter)
      - [M GetVlanVid ](#tts.lib.ethernet.PacketIke.PacketIke.GetVlanVid)
      - [M GetVlanVidOuter ](#tts.lib.ethernet.PacketIke.PacketIke.GetVlanVidOuter)
      - [A PK_CLASS ](#tts.lib.ethernet.PacketIke.PacketIke.PK_CLASS)
      - [M SetEthDstMac ](#tts.lib.ethernet.PacketIke.PacketIke.SetEthDstMac)
      - [M SetEthPayload ](#tts.lib.ethernet.PacketIke.PacketIke.SetEthPayload)
      - [M SetEthSrcMac ](#tts.lib.ethernet.PacketIke.PacketIke.SetEthSrcMac)
      - [M SetEthType ](#tts.lib.ethernet.PacketIke.PacketIke.SetEthType)
      - [M SetIpChecksum ](#tts.lib.ethernet.PacketIke.PacketIke.SetIpChecksum)
      - [M SetIpDst ](#tts.lib.ethernet.PacketIke.PacketIke.SetIpDst)
      - [M SetIpIdent ](#tts.lib.ethernet.PacketIke.PacketIke.SetIpIdent)
      - [M SetIpLen ](#tts.lib.ethernet.PacketIke.PacketIke.SetIpLen)
      - [M SetIpOffset ](#tts.lib.ethernet.PacketIke.PacketIke.SetIpOffset)
      - [M SetIpPayload ](#tts.lib.ethernet.PacketIke.PacketIke.SetIpPayload)
      - [M SetIpProt ](#tts.lib.ethernet.PacketIke.PacketIke.SetIpProt)
      - [M SetIpSrc ](#tts.lib.ethernet.PacketIke.PacketIke.SetIpSrc)
      - [M SetIpTos ](#tts.lib.ethernet.PacketIke.PacketIke.SetIpTos)
      - [M SetIpTtl ](#tts.lib.ethernet.PacketIke.PacketIke.SetIpTtl)
      - [M SetIpVersionAndHeaderLength ](#tts.lib.ethernet.PacketIke.PacketIke.SetIpVersionAndHeaderLength)
      - [M SetTimestamp ](#tts.lib.ethernet.PacketIke.PacketIke.SetTimestamp)
      - [M SetUdpChecksum ](#tts.lib.ethernet.PacketIke.PacketIke.SetUdpChecksum)
      - [M SetUdpDst ](#tts.lib.ethernet.PacketIke.PacketIke.SetUdpDst)
      - [M SetUdpLen ](#tts.lib.ethernet.PacketIke.PacketIke.SetUdpLen)
      - [M SetUdpPayload ](#tts.lib.ethernet.PacketIke.PacketIke.SetUdpPayload)
      - [M SetUdpSrc ](#tts.lib.ethernet.PacketIke.PacketIke.SetUdpSrc)
      - [M SetVlanCfi ](#tts.lib.ethernet.PacketIke.PacketIke.SetVlanCfi)
      - [M SetVlanCfiOuter ](#tts.lib.ethernet.PacketIke.PacketIke.SetVlanCfiOuter)
      - [M SetVlanPcp ](#tts.lib.ethernet.PacketIke.PacketIke.SetVlanPcp)
      - [M SetVlanPcpOuter ](#tts.lib.ethernet.PacketIke.PacketIke.SetVlanPcpOuter)
      - [M SetVlanVid ](#tts.lib.ethernet.PacketIke.PacketIke.SetVlanVid)
      - [M SetVlanVidOuter ](#tts.lib.ethernet.PacketIke.PacketIke.SetVlanVidOuter)
      - [A ethDstMac ](#tts.lib.ethernet.PacketIke.PacketIke.ethDstMac)
      - [A ethPayload ](#tts.lib.ethernet.PacketIke.PacketIke.ethPayload)
      - [A ethSrcMac ](#tts.lib.ethernet.PacketIke.PacketIke.ethSrcMac)
      - [A ethType ](#tts.lib.ethernet.PacketIke.PacketIke.ethType)
      - [A ipAhIcv ](#tts.lib.ethernet.PacketIke.PacketIke.ipAhIcv)
      - [A ipAhLen ](#tts.lib.ethernet.PacketIke.PacketIke.ipAhLen)
      - [A ipAhNxt ](#tts.lib.ethernet.PacketIke.PacketIke.ipAhNxt)
      - [A ipAhRsvd ](#tts.lib.ethernet.PacketIke.PacketIke.ipAhRsvd)
      - [A ipAhSeq ](#tts.lib.ethernet.PacketIke.PacketIke.ipAhSeq)
      - [A ipAhSpi ](#tts.lib.ethernet.PacketIke.PacketIke.ipAhSpi)
      - [A ipChecksum ](#tts.lib.ethernet.PacketIke.PacketIke.ipChecksum)
      - [A ipDst ](#tts.lib.ethernet.PacketIke.PacketIke.ipDst)
      - [A ipIdent ](#tts.lib.ethernet.PacketIke.PacketIke.ipIdent)
      - [A ipLen ](#tts.lib.ethernet.PacketIke.PacketIke.ipLen)
      - [A ipOffset ](#tts.lib.ethernet.PacketIke.PacketIke.ipOffset)
      - [A ipPayload ](#tts.lib.ethernet.PacketIke.PacketIke.ipPayload)
      - [A ipProt ](#tts.lib.ethernet.PacketIke.PacketIke.ipProt)
      - [A ipSrc ](#tts.lib.ethernet.PacketIke.PacketIke.ipSrc)
      - [A ipTos ](#tts.lib.ethernet.PacketIke.PacketIke.ipTos)
      - [A ipTtl ](#tts.lib.ethernet.PacketIke.PacketIke.ipTtl)
      - [A ipVersionHeader ](#tts.lib.ethernet.PacketIke.PacketIke.ipVersionHeader)
      - [A macSecAn ](#tts.lib.ethernet.PacketIke.PacketIke.macSecAn)
      - [A macSecIcv ](#tts.lib.ethernet.PacketIke.PacketIke.macSecIcv)
      - [A macSecPn ](#tts.lib.ethernet.PacketIke.PacketIke.macSecPn)
      - [A macSecSci ](#tts.lib.ethernet.PacketIke.PacketIke.macSecSci)
      - [A macSecSl ](#tts.lib.ethernet.PacketIke.PacketIke.macSecSl)
      - [A macSecTci ](#tts.lib.ethernet.PacketIke.PacketIke.macSecTci)
      - [A macSecTciAn ](#tts.lib.ethernet.PacketIke.PacketIke.macSecTciAn)
      - [A macSecTciC ](#tts.lib.ethernet.PacketIke.PacketIke.macSecTciC)
      - [A macSecTciE ](#tts.lib.ethernet.PacketIke.PacketIke.macSecTciE)
      - [A macSecTciEs ](#tts.lib.ethernet.PacketIke.PacketIke.macSecTciEs)
      - [A macSecTciSc ](#tts.lib.ethernet.PacketIke.PacketIke.macSecTciSc)
      - [A macSecTciScb ](#tts.lib.ethernet.PacketIke.PacketIke.macSecTciScb)
      - [A macSecTciV ](#tts.lib.ethernet.PacketIke.PacketIke.macSecTciV)
      - [A parent ](#tts.lib.ethernet.PacketIke.PacketIke.parent)
      - [A timestamp ](#tts.lib.ethernet.PacketIke.PacketIke.timestamp)
      - [A udpChecksum ](#tts.lib.ethernet.PacketIke.PacketIke.udpChecksum)
      - [A udpDst ](#tts.lib.ethernet.PacketIke.PacketIke.udpDst)
      - [A udpLen ](#tts.lib.ethernet.PacketIke.PacketIke.udpLen)
      - [A udpPayload ](#tts.lib.ethernet.PacketIke.PacketIke.udpPayload)
      - [A udpSrc ](#tts.lib.ethernet.PacketIke.PacketIke.udpSrc)
      - [A vlanCfi ](#tts.lib.ethernet.PacketIke.PacketIke.vlanCfi)
      - [A vlanCfiOuter ](#tts.lib.ethernet.PacketIke.PacketIke.vlanCfiOuter)
      - [A vlanPcp ](#tts.lib.ethernet.PacketIke.PacketIke.vlanPcp)
      - [A vlanPcpOuter ](#tts.lib.ethernet.PacketIke.PacketIke.vlanPcpOuter)
      - [A vlanVid ](#tts.lib.ethernet.PacketIke.PacketIke.vlanVid)
      - [A vlanVidOuter ](#tts.lib.ethernet.PacketIke.PacketIke.vlanVidOuter)
      - [A deleteSpis ](#tts.lib.ethernet.PacketIke.PacketIke.deleteSpis)
      - [M GetDeleteNumOfSpis ](#tts.lib.ethernet.PacketIke.PacketIke.GetDeleteNumOfSpis)
      - [A deleteNumOfSpis ](#tts.lib.ethernet.PacketIke.PacketIke.deleteNumOfSpis)
  - [ PacketTcp ](#packettcp)
    - [C PacketTcp ](#tts.lib.ethernet.PacketTcp.PacketTcp)
      - [M GetTcpLen ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetTcpLen)
      - [M GetTcpSrc ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetTcpSrc)
      - [M SetTcpSrc ](#tts.lib.ethernet.PacketTcp.PacketTcp.SetTcpSrc)
      - [A tcpSrc ](#tts.lib.ethernet.PacketTcp.PacketTcp.tcpSrc)
      - [M GetTcpDst ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetTcpDst)
      - [M SetTcpDst ](#tts.lib.ethernet.PacketTcp.PacketTcp.SetTcpDst)
      - [A tcpDst ](#tts.lib.ethernet.PacketTcp.PacketTcp.tcpDst)
      - [M GetTcpSeq ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetTcpSeq)
      - [M SetTcpSeq ](#tts.lib.ethernet.PacketTcp.PacketTcp.SetTcpSeq)
      - [A tcpSeq ](#tts.lib.ethernet.PacketTcp.PacketTcp.tcpSeq)
      - [M GetTcpAck ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetTcpAck)
      - [M SetTcpAck ](#tts.lib.ethernet.PacketTcp.PacketTcp.SetTcpAck)
      - [A tcpAck ](#tts.lib.ethernet.PacketTcp.PacketTcp.tcpAck)
      - [M GetTcpOffset ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetTcpOffset)
      - [M SetTcpOffset ](#tts.lib.ethernet.PacketTcp.PacketTcp.SetTcpOffset)
      - [A tcpOffset ](#tts.lib.ethernet.PacketTcp.PacketTcp.tcpOffset)
      - [M GetTcpFlags ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetTcpFlags)
      - [M SetTcpFlags ](#tts.lib.ethernet.PacketTcp.PacketTcp.SetTcpFlags)
      - [A tcpFlags ](#tts.lib.ethernet.PacketTcp.PacketTcp.tcpFlags)
      - [M GetTcpWindow ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetTcpWindow)
      - [M SetTcpWindow ](#tts.lib.ethernet.PacketTcp.PacketTcp.SetTcpWindow)
      - [A tcpWindow ](#tts.lib.ethernet.PacketTcp.PacketTcp.tcpWindow)
      - [M GetTcpChecksum ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetTcpChecksum)
      - [M SetTcpChecksum ](#tts.lib.ethernet.PacketTcp.PacketTcp.SetTcpChecksum)
      - [A tcpChecksum ](#tts.lib.ethernet.PacketTcp.PacketTcp.tcpChecksum)
      - [M GetTcpUrgent ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetTcpUrgent)
      - [M SetTcpUrgent ](#tts.lib.ethernet.PacketTcp.PacketTcp.SetTcpUrgent)
      - [A tcpUrgent ](#tts.lib.ethernet.PacketTcp.PacketTcp.tcpUrgent)
      - [M GetTcpPayload ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetTcpPayload)
      - [M SetTcpPayload ](#tts.lib.ethernet.PacketTcp.PacketTcp.SetTcpPayload)
      - [A tcpPayload ](#tts.lib.ethernet.PacketTcp.PacketTcp.tcpPayload)
      - [M GetTcpOptions ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetTcpOptions)
      - [A tcpOptions ](#tts.lib.ethernet.PacketTcp.PacketTcp.tcpOptions)
      - [M CalcIpLen ](#tts.lib.ethernet.PacketTcp.PacketTcp.CalcIpLen)
      - [M FindParent ](#tts.lib.ethernet.PacketTcp.PacketTcp.FindParent)
      - [M GetEthDstMac ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetEthDstMac)
      - [M GetEthPayload ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetEthPayload)
      - [M GetEthSrcMac ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetEthSrcMac)
      - [M GetEthType ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetEthType)
      - [M GetIpAhIcv ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetIpAhIcv)
      - [M GetIpAhLen ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetIpAhLen)
      - [M GetIpAhNxt ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetIpAhNxt)
      - [M GetIpAhRsvd ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetIpAhRsvd)
      - [M GetIpAhSeq ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetIpAhSeq)
      - [M GetIpAhSpi ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetIpAhSpi)
      - [M GetIpChecksum ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetIpChecksum)
      - [M GetIpDst ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetIpDst)
      - [M GetIpIdent ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetIpIdent)
      - [M GetIpLen ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetIpLen)
      - [M GetIpOffset ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetIpOffset)
      - [M GetIpPayload ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetIpPayload)
      - [M GetIpProt ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetIpProt)
      - [M GetIpSrc ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetIpSrc)
      - [M GetIpTos ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetIpTos)
      - [M GetIpTtl ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetIpTtl)
      - [M GetIpVersionAndHeaderLength ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetIpVersionAndHeaderLength)
      - [M GetMacSecAn ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetMacSecAn)
      - [M GetMacSecIcv ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetMacSecIcv)
      - [M GetMacSecPn ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetMacSecPn)
      - [M GetMacSecSci ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetMacSecSci)
      - [M GetMacSecSl ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetMacSecSl)
      - [M GetMacSecTci ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetMacSecTci)
      - [M GetMacSecTciAn ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetMacSecTciAn)
      - [M GetMacSecTciC ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetMacSecTciC)
      - [M GetMacSecTciE ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetMacSecTciE)
      - [M GetMacSecTciEs ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetMacSecTciEs)
      - [M GetMacSecTciSc ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetMacSecTciSc)
      - [M GetMacSecTciScb ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetMacSecTciScb)
      - [M GetMacSecTciV ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetMacSecTciV)
      - [M GetTimestamp ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetTimestamp)
      - [M GetVlanCfi ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetVlanCfi)
      - [M GetVlanCfiOuter ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetVlanCfiOuter)
      - [M GetVlanPcp ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetVlanPcp)
      - [M GetVlanPcpOuter ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetVlanPcpOuter)
      - [M GetVlanVid ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetVlanVid)
      - [M GetVlanVidOuter ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetVlanVidOuter)
      - [A PK_CLASS ](#tts.lib.ethernet.PacketTcp.PacketTcp.PK_CLASS)
      - [M SetEthDstMac ](#tts.lib.ethernet.PacketTcp.PacketTcp.SetEthDstMac)
      - [M SetEthPayload ](#tts.lib.ethernet.PacketTcp.PacketTcp.SetEthPayload)
      - [M SetEthSrcMac ](#tts.lib.ethernet.PacketTcp.PacketTcp.SetEthSrcMac)
      - [M SetEthType ](#tts.lib.ethernet.PacketTcp.PacketTcp.SetEthType)
      - [M SetIpChecksum ](#tts.lib.ethernet.PacketTcp.PacketTcp.SetIpChecksum)
      - [M SetIpDst ](#tts.lib.ethernet.PacketTcp.PacketTcp.SetIpDst)
      - [M SetIpIdent ](#tts.lib.ethernet.PacketTcp.PacketTcp.SetIpIdent)
      - [M SetIpLen ](#tts.lib.ethernet.PacketTcp.PacketTcp.SetIpLen)
      - [M SetIpOffset ](#tts.lib.ethernet.PacketTcp.PacketTcp.SetIpOffset)
      - [M SetIpPayload ](#tts.lib.ethernet.PacketTcp.PacketTcp.SetIpPayload)
      - [M SetIpProt ](#tts.lib.ethernet.PacketTcp.PacketTcp.SetIpProt)
      - [M SetIpSrc ](#tts.lib.ethernet.PacketTcp.PacketTcp.SetIpSrc)
      - [M SetIpTos ](#tts.lib.ethernet.PacketTcp.PacketTcp.SetIpTos)
      - [M SetIpTtl ](#tts.lib.ethernet.PacketTcp.PacketTcp.SetIpTtl)
      - [M SetIpVersionAndHeaderLength ](#tts.lib.ethernet.PacketTcp.PacketTcp.SetIpVersionAndHeaderLength)
      - [M SetTimestamp ](#tts.lib.ethernet.PacketTcp.PacketTcp.SetTimestamp)
      - [M SetVlanCfi ](#tts.lib.ethernet.PacketTcp.PacketTcp.SetVlanCfi)
      - [M SetVlanCfiOuter ](#tts.lib.ethernet.PacketTcp.PacketTcp.SetVlanCfiOuter)
      - [M SetVlanPcp ](#tts.lib.ethernet.PacketTcp.PacketTcp.SetVlanPcp)
      - [M SetVlanPcpOuter ](#tts.lib.ethernet.PacketTcp.PacketTcp.SetVlanPcpOuter)
      - [M SetVlanVid ](#tts.lib.ethernet.PacketTcp.PacketTcp.SetVlanVid)
      - [M SetVlanVidOuter ](#tts.lib.ethernet.PacketTcp.PacketTcp.SetVlanVidOuter)
      - [A ethDstMac ](#tts.lib.ethernet.PacketTcp.PacketTcp.ethDstMac)
      - [A ethPayload ](#tts.lib.ethernet.PacketTcp.PacketTcp.ethPayload)
      - [A ethSrcMac ](#tts.lib.ethernet.PacketTcp.PacketTcp.ethSrcMac)
      - [A ethType ](#tts.lib.ethernet.PacketTcp.PacketTcp.ethType)
      - [A ipAhIcv ](#tts.lib.ethernet.PacketTcp.PacketTcp.ipAhIcv)
      - [A ipAhLen ](#tts.lib.ethernet.PacketTcp.PacketTcp.ipAhLen)
      - [A ipAhNxt ](#tts.lib.ethernet.PacketTcp.PacketTcp.ipAhNxt)
      - [A ipAhRsvd ](#tts.lib.ethernet.PacketTcp.PacketTcp.ipAhRsvd)
      - [A ipAhSeq ](#tts.lib.ethernet.PacketTcp.PacketTcp.ipAhSeq)
      - [A ipAhSpi ](#tts.lib.ethernet.PacketTcp.PacketTcp.ipAhSpi)
      - [A ipChecksum ](#tts.lib.ethernet.PacketTcp.PacketTcp.ipChecksum)
      - [A ipDst ](#tts.lib.ethernet.PacketTcp.PacketTcp.ipDst)
      - [A ipIdent ](#tts.lib.ethernet.PacketTcp.PacketTcp.ipIdent)
      - [A ipLen ](#tts.lib.ethernet.PacketTcp.PacketTcp.ipLen)
      - [A ipOffset ](#tts.lib.ethernet.PacketTcp.PacketTcp.ipOffset)
      - [A ipPayload ](#tts.lib.ethernet.PacketTcp.PacketTcp.ipPayload)
      - [A ipProt ](#tts.lib.ethernet.PacketTcp.PacketTcp.ipProt)
      - [A ipSrc ](#tts.lib.ethernet.PacketTcp.PacketTcp.ipSrc)
      - [A ipTos ](#tts.lib.ethernet.PacketTcp.PacketTcp.ipTos)
      - [A ipTtl ](#tts.lib.ethernet.PacketTcp.PacketTcp.ipTtl)
      - [A ipVersionHeader ](#tts.lib.ethernet.PacketTcp.PacketTcp.ipVersionHeader)
      - [A macSecAn ](#tts.lib.ethernet.PacketTcp.PacketTcp.macSecAn)
      - [A macSecIcv ](#tts.lib.ethernet.PacketTcp.PacketTcp.macSecIcv)
      - [A macSecPn ](#tts.lib.ethernet.PacketTcp.PacketTcp.macSecPn)
      - [A macSecSci ](#tts.lib.ethernet.PacketTcp.PacketTcp.macSecSci)
      - [A macSecSl ](#tts.lib.ethernet.PacketTcp.PacketTcp.macSecSl)
      - [A macSecTci ](#tts.lib.ethernet.PacketTcp.PacketTcp.macSecTci)
      - [A macSecTciAn ](#tts.lib.ethernet.PacketTcp.PacketTcp.macSecTciAn)
      - [A macSecTciC ](#tts.lib.ethernet.PacketTcp.PacketTcp.macSecTciC)
      - [A macSecTciE ](#tts.lib.ethernet.PacketTcp.PacketTcp.macSecTciE)
      - [A macSecTciEs ](#tts.lib.ethernet.PacketTcp.PacketTcp.macSecTciEs)
      - [A macSecTciSc ](#tts.lib.ethernet.PacketTcp.PacketTcp.macSecTciSc)
      - [A macSecTciScb ](#tts.lib.ethernet.PacketTcp.PacketTcp.macSecTciScb)
      - [A macSecTciV ](#tts.lib.ethernet.PacketTcp.PacketTcp.macSecTciV)
      - [A parent ](#tts.lib.ethernet.PacketTcp.PacketTcp.parent)
      - [A timestamp ](#tts.lib.ethernet.PacketTcp.PacketTcp.timestamp)
      - [A vlanCfi ](#tts.lib.ethernet.PacketTcp.PacketTcp.vlanCfi)
      - [A vlanCfiOuter ](#tts.lib.ethernet.PacketTcp.PacketTcp.vlanCfiOuter)
      - [A vlanPcp ](#tts.lib.ethernet.PacketTcp.PacketTcp.vlanPcp)
      - [A vlanPcpOuter ](#tts.lib.ethernet.PacketTcp.PacketTcp.vlanPcpOuter)
      - [A vlanVid ](#tts.lib.ethernet.PacketTcp.PacketTcp.vlanVid)
      - [A vlanVidOuter ](#tts.lib.ethernet.PacketTcp.PacketTcp.vlanVidOuter)
  - [ PacketUdp ](#packetudp)
    - [C PacketUdp ](#tts.lib.ethernet.PacketUdp.PacketUdp)
      - [M CalcUdpLen ](#tts.lib.ethernet.PacketUdp.PacketUdp.CalcUdpLen)
      - [M GetUdpSrc ](#tts.lib.ethernet.PacketUdp.PacketUdp.GetUdpSrc)
      - [M SetUdpSrc ](#tts.lib.ethernet.PacketUdp.PacketUdp.SetUdpSrc)
      - [A udpSrc ](#tts.lib.ethernet.PacketUdp.PacketUdp.udpSrc)
      - [M GetUdpDst ](#tts.lib.ethernet.PacketUdp.PacketUdp.GetUdpDst)
      - [M SetUdpDst ](#tts.lib.ethernet.PacketUdp.PacketUdp.SetUdpDst)
      - [A udpDst ](#tts.lib.ethernet.PacketUdp.PacketUdp.udpDst)
      - [M GetUdpLen ](#tts.lib.ethernet.PacketUdp.PacketUdp.GetUdpLen)
      - [M SetUdpLen ](#tts.lib.ethernet.PacketUdp.PacketUdp.SetUdpLen)
      - [A udpLen ](#tts.lib.ethernet.PacketUdp.PacketUdp.udpLen)
      - [M GetUdpChecksum ](#tts.lib.ethernet.PacketUdp.PacketUdp.GetUdpChecksum)
      - [M SetUdpChecksum ](#tts.lib.ethernet.PacketUdp.PacketUdp.SetUdpChecksum)
      - [A udpChecksum ](#tts.lib.ethernet.PacketUdp.PacketUdp.udpChecksum)
      - [M GetUdpPayload ](#tts.lib.ethernet.PacketUdp.PacketUdp.GetUdpPayload)
      - [M SetUdpPayload ](#tts.lib.ethernet.PacketUdp.PacketUdp.SetUdpPayload)
      - [A udpPayload ](#tts.lib.ethernet.PacketUdp.PacketUdp.udpPayload)
      - [M CalcIpLen ](#tts.lib.ethernet.PacketUdp.PacketUdp.CalcIpLen)
      - [M FindParent ](#tts.lib.ethernet.PacketUdp.PacketUdp.FindParent)
      - [M GetEthDstMac ](#tts.lib.ethernet.PacketUdp.PacketUdp.GetEthDstMac)
      - [M GetEthPayload ](#tts.lib.ethernet.PacketUdp.PacketUdp.GetEthPayload)
      - [M GetEthSrcMac ](#tts.lib.ethernet.PacketUdp.PacketUdp.GetEthSrcMac)
      - [M GetEthType ](#tts.lib.ethernet.PacketUdp.PacketUdp.GetEthType)
      - [M GetIpAhIcv ](#tts.lib.ethernet.PacketUdp.PacketUdp.GetIpAhIcv)
      - [M GetIpAhLen ](#tts.lib.ethernet.PacketUdp.PacketUdp.GetIpAhLen)
      - [M GetIpAhNxt ](#tts.lib.ethernet.PacketUdp.PacketUdp.GetIpAhNxt)
      - [M GetIpAhRsvd ](#tts.lib.ethernet.PacketUdp.PacketUdp.GetIpAhRsvd)
      - [M GetIpAhSeq ](#tts.lib.ethernet.PacketUdp.PacketUdp.GetIpAhSeq)
      - [M GetIpAhSpi ](#tts.lib.ethernet.PacketUdp.PacketUdp.GetIpAhSpi)
      - [M GetIpChecksum ](#tts.lib.ethernet.PacketUdp.PacketUdp.GetIpChecksum)
      - [M GetIpDst ](#tts.lib.ethernet.PacketUdp.PacketUdp.GetIpDst)
      - [M GetIpIdent ](#tts.lib.ethernet.PacketUdp.PacketUdp.GetIpIdent)
      - [M GetIpLen ](#tts.lib.ethernet.PacketUdp.PacketUdp.GetIpLen)
      - [M GetIpOffset ](#tts.lib.ethernet.PacketUdp.PacketUdp.GetIpOffset)
      - [M GetIpPayload ](#tts.lib.ethernet.PacketUdp.PacketUdp.GetIpPayload)
      - [M GetIpProt ](#tts.lib.ethernet.PacketUdp.PacketUdp.GetIpProt)
      - [M GetIpSrc ](#tts.lib.ethernet.PacketUdp.PacketUdp.GetIpSrc)
      - [M GetIpTos ](#tts.lib.ethernet.PacketUdp.PacketUdp.GetIpTos)
      - [M GetIpTtl ](#tts.lib.ethernet.PacketUdp.PacketUdp.GetIpTtl)
      - [M GetIpVersionAndHeaderLength ](#tts.lib.ethernet.PacketUdp.PacketUdp.GetIpVersionAndHeaderLength)
      - [M GetMacSecAn ](#tts.lib.ethernet.PacketUdp.PacketUdp.GetMacSecAn)
      - [M GetMacSecIcv ](#tts.lib.ethernet.PacketUdp.PacketUdp.GetMacSecIcv)
      - [M GetMacSecPn ](#tts.lib.ethernet.PacketUdp.PacketUdp.GetMacSecPn)
      - [M GetMacSecSci ](#tts.lib.ethernet.PacketUdp.PacketUdp.GetMacSecSci)
      - [M GetMacSecSl ](#tts.lib.ethernet.PacketUdp.PacketUdp.GetMacSecSl)
      - [M GetMacSecTci ](#tts.lib.ethernet.PacketUdp.PacketUdp.GetMacSecTci)
      - [M GetMacSecTciAn ](#tts.lib.ethernet.PacketUdp.PacketUdp.GetMacSecTciAn)
      - [M GetMacSecTciC ](#tts.lib.ethernet.PacketUdp.PacketUdp.GetMacSecTciC)
      - [M GetMacSecTciE ](#tts.lib.ethernet.PacketUdp.PacketUdp.GetMacSecTciE)
      - [M GetMacSecTciEs ](#tts.lib.ethernet.PacketUdp.PacketUdp.GetMacSecTciEs)
      - [M GetMacSecTciSc ](#tts.lib.ethernet.PacketUdp.PacketUdp.GetMacSecTciSc)
      - [M GetMacSecTciScb ](#tts.lib.ethernet.PacketUdp.PacketUdp.GetMacSecTciScb)
      - [M GetMacSecTciV ](#tts.lib.ethernet.PacketUdp.PacketUdp.GetMacSecTciV)
      - [M GetTimestamp ](#tts.lib.ethernet.PacketUdp.PacketUdp.GetTimestamp)
      - [M GetVlanCfi ](#tts.lib.ethernet.PacketUdp.PacketUdp.GetVlanCfi)
      - [M GetVlanCfiOuter ](#tts.lib.ethernet.PacketUdp.PacketUdp.GetVlanCfiOuter)
      - [M GetVlanPcp ](#tts.lib.ethernet.PacketUdp.PacketUdp.GetVlanPcp)
      - [M GetVlanPcpOuter ](#tts.lib.ethernet.PacketUdp.PacketUdp.GetVlanPcpOuter)
      - [M GetVlanVid ](#tts.lib.ethernet.PacketUdp.PacketUdp.GetVlanVid)
      - [M GetVlanVidOuter ](#tts.lib.ethernet.PacketUdp.PacketUdp.GetVlanVidOuter)
      - [A PK_CLASS ](#tts.lib.ethernet.PacketUdp.PacketUdp.PK_CLASS)
      - [M SetEthDstMac ](#tts.lib.ethernet.PacketUdp.PacketUdp.SetEthDstMac)
      - [M SetEthPayload ](#tts.lib.ethernet.PacketUdp.PacketUdp.SetEthPayload)
      - [M SetEthSrcMac ](#tts.lib.ethernet.PacketUdp.PacketUdp.SetEthSrcMac)
      - [M SetEthType ](#tts.lib.ethernet.PacketUdp.PacketUdp.SetEthType)
      - [M SetIpChecksum ](#tts.lib.ethernet.PacketUdp.PacketUdp.SetIpChecksum)
      - [M SetIpDst ](#tts.lib.ethernet.PacketUdp.PacketUdp.SetIpDst)
      - [M SetIpIdent ](#tts.lib.ethernet.PacketUdp.PacketUdp.SetIpIdent)
      - [M SetIpLen ](#tts.lib.ethernet.PacketUdp.PacketUdp.SetIpLen)
      - [M SetIpOffset ](#tts.lib.ethernet.PacketUdp.PacketUdp.SetIpOffset)
      - [M SetIpPayload ](#tts.lib.ethernet.PacketUdp.PacketUdp.SetIpPayload)
      - [M SetIpProt ](#tts.lib.ethernet.PacketUdp.PacketUdp.SetIpProt)
      - [M SetIpSrc ](#tts.lib.ethernet.PacketUdp.PacketUdp.SetIpSrc)
      - [M SetIpTos ](#tts.lib.ethernet.PacketUdp.PacketUdp.SetIpTos)
      - [M SetIpTtl ](#tts.lib.ethernet.PacketUdp.PacketUdp.SetIpTtl)
      - [M SetIpVersionAndHeaderLength ](#tts.lib.ethernet.PacketUdp.PacketUdp.SetIpVersionAndHeaderLength)
      - [M SetTimestamp ](#tts.lib.ethernet.PacketUdp.PacketUdp.SetTimestamp)
      - [M SetVlanCfi ](#tts.lib.ethernet.PacketUdp.PacketUdp.SetVlanCfi)
      - [M SetVlanCfiOuter ](#tts.lib.ethernet.PacketUdp.PacketUdp.SetVlanCfiOuter)
      - [M SetVlanPcp ](#tts.lib.ethernet.PacketUdp.PacketUdp.SetVlanPcp)
      - [M SetVlanPcpOuter ](#tts.lib.ethernet.PacketUdp.PacketUdp.SetVlanPcpOuter)
      - [M SetVlanVid ](#tts.lib.ethernet.PacketUdp.PacketUdp.SetVlanVid)
      - [M SetVlanVidOuter ](#tts.lib.ethernet.PacketUdp.PacketUdp.SetVlanVidOuter)
      - [A ethDstMac ](#tts.lib.ethernet.PacketUdp.PacketUdp.ethDstMac)
      - [A ethPayload ](#tts.lib.ethernet.PacketUdp.PacketUdp.ethPayload)
      - [A ethSrcMac ](#tts.lib.ethernet.PacketUdp.PacketUdp.ethSrcMac)
      - [A ethType ](#tts.lib.ethernet.PacketUdp.PacketUdp.ethType)
      - [A ipAhIcv ](#tts.lib.ethernet.PacketUdp.PacketUdp.ipAhIcv)
      - [A ipAhLen ](#tts.lib.ethernet.PacketUdp.PacketUdp.ipAhLen)
      - [A ipAhNxt ](#tts.lib.ethernet.PacketUdp.PacketUdp.ipAhNxt)
      - [A ipAhRsvd ](#tts.lib.ethernet.PacketUdp.PacketUdp.ipAhRsvd)
      - [A ipAhSeq ](#tts.lib.ethernet.PacketUdp.PacketUdp.ipAhSeq)
      - [A ipAhSpi ](#tts.lib.ethernet.PacketUdp.PacketUdp.ipAhSpi)
      - [A ipChecksum ](#tts.lib.ethernet.PacketUdp.PacketUdp.ipChecksum)
      - [A ipDst ](#tts.lib.ethernet.PacketUdp.PacketUdp.ipDst)
      - [A ipIdent ](#tts.lib.ethernet.PacketUdp.PacketUdp.ipIdent)
      - [A ipLen ](#tts.lib.ethernet.PacketUdp.PacketUdp.ipLen)
      - [A ipOffset ](#tts.lib.ethernet.PacketUdp.PacketUdp.ipOffset)
      - [A ipPayload ](#tts.lib.ethernet.PacketUdp.PacketUdp.ipPayload)
      - [A ipProt ](#tts.lib.ethernet.PacketUdp.PacketUdp.ipProt)
      - [A ipSrc ](#tts.lib.ethernet.PacketUdp.PacketUdp.ipSrc)
      - [A ipTos ](#tts.lib.ethernet.PacketUdp.PacketUdp.ipTos)
      - [A ipTtl ](#tts.lib.ethernet.PacketUdp.PacketUdp.ipTtl)
      - [A ipVersionHeader ](#tts.lib.ethernet.PacketUdp.PacketUdp.ipVersionHeader)
      - [A macSecAn ](#tts.lib.ethernet.PacketUdp.PacketUdp.macSecAn)
      - [A macSecIcv ](#tts.lib.ethernet.PacketUdp.PacketUdp.macSecIcv)
      - [A macSecPn ](#tts.lib.ethernet.PacketUdp.PacketUdp.macSecPn)
      - [A macSecSci ](#tts.lib.ethernet.PacketUdp.PacketUdp.macSecSci)
      - [A macSecSl ](#tts.lib.ethernet.PacketUdp.PacketUdp.macSecSl)
      - [A macSecTci ](#tts.lib.ethernet.PacketUdp.PacketUdp.macSecTci)
      - [A macSecTciAn ](#tts.lib.ethernet.PacketUdp.PacketUdp.macSecTciAn)
      - [A macSecTciC ](#tts.lib.ethernet.PacketUdp.PacketUdp.macSecTciC)
      - [A macSecTciE ](#tts.lib.ethernet.PacketUdp.PacketUdp.macSecTciE)
      - [A macSecTciEs ](#tts.lib.ethernet.PacketUdp.PacketUdp.macSecTciEs)
      - [A macSecTciSc ](#tts.lib.ethernet.PacketUdp.PacketUdp.macSecTciSc)
      - [A macSecTciScb ](#tts.lib.ethernet.PacketUdp.PacketUdp.macSecTciScb)
      - [A macSecTciV ](#tts.lib.ethernet.PacketUdp.PacketUdp.macSecTciV)
      - [A parent ](#tts.lib.ethernet.PacketUdp.PacketUdp.parent)
      - [A timestamp ](#tts.lib.ethernet.PacketUdp.PacketUdp.timestamp)
      - [A vlanCfi ](#tts.lib.ethernet.PacketUdp.PacketUdp.vlanCfi)
      - [A vlanCfiOuter ](#tts.lib.ethernet.PacketUdp.PacketUdp.vlanCfiOuter)
      - [A vlanPcp ](#tts.lib.ethernet.PacketUdp.PacketUdp.vlanPcp)
      - [A vlanPcpOuter ](#tts.lib.ethernet.PacketUdp.PacketUdp.vlanPcpOuter)
      - [A vlanVid ](#tts.lib.ethernet.PacketUdp.PacketUdp.vlanVid)
      - [A vlanVidOuter ](#tts.lib.ethernet.PacketUdp.PacketUdp.vlanVidOuter)
  - [ PTP ](#ptp)
    - [ PacketPtpSync ](#packetptpsync)
      - [C PacketPtpSync ](#tts.lib.ethernet.PacketPtp.PacketPtpSync)
        - [M FindParent ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.FindParent)
        - [M GetEthDstMac ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetEthDstMac)
        - [M GetEthPayload ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetEthPayload)
        - [M GetEthSrcMac ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetEthSrcMac)
        - [M GetEthType ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetEthType)
        - [M GetMacSecAn ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetMacSecAn)
        - [M GetMacSecIcv ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetMacSecIcv)
        - [M GetMacSecPn ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetMacSecPn)
        - [M GetMacSecSci ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetMacSecSci)
        - [M GetMacSecSl ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetMacSecSl)
        - [M GetMacSecTci ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetMacSecTci)
        - [M GetMacSecTciAn ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetMacSecTciAn)
        - [M GetMacSecTciC ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetMacSecTciC)
        - [M GetMacSecTciE ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetMacSecTciE)
        - [M GetMacSecTciEs ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetMacSecTciEs)
        - [M GetMacSecTciSc ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetMacSecTciSc)
        - [M GetMacSecTciScb ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetMacSecTciScb)
        - [M GetMacSecTciV ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetMacSecTciV)
        - [M GetPtpControl ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetPtpControl)
        - [M GetPtpCorrectionField ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetPtpCorrectionField)
        - [M GetPtpDomainNumber ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetPtpDomainNumber)
        - [M GetPtpFlags ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetPtpFlags)
        - [M GetPtpLogMsgInterval ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetPtpLogMsgInterval)
        - [M GetPtpMsgLen ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetPtpMsgLen)
        - [M GetPtpMsgType ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetPtpMsgType)
        - [M GetPtpSequenceId ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetPtpSequenceId)
        - [M GetPtpSourcePortIdentity ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetPtpSourcePortIdentity)
        - [M GetPtpVersion ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetPtpVersion)
        - [M GetTimestamp ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetTimestamp)
        - [M GetVlanCfi ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetVlanCfi)
        - [M GetVlanCfiOuter ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetVlanCfiOuter)
        - [M GetVlanPcp ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetVlanPcp)
        - [M GetVlanPcpOuter ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetVlanPcpOuter)
        - [M GetVlanVid ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetVlanVid)
        - [M GetVlanVidOuter ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetVlanVidOuter)
        - [M SetEthDstMac ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetEthDstMac)
        - [M SetEthPayload ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetEthPayload)
        - [M SetEthSrcMac ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetEthSrcMac)
        - [M SetEthType ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetEthType)
        - [M SetPtpControl ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetPtpControl)
        - [M SetPtpCorrectionField ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetPtpCorrectionField)
        - [M SetPtpDomainNumber ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetPtpDomainNumber)
        - [M SetPtpFlags ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetPtpFlags)
        - [M SetPtpLogMsgInterval ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetPtpLogMsgInterval)
        - [M SetPtpMsgLen ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetPtpMsgLen)
        - [M SetPtpMsgType ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetPtpMsgType)
        - [M SetPtpSequenceId ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetPtpSequenceId)
        - [M SetPtpSourcePortIdentity ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetPtpSourcePortIdentity)
        - [M SetPtpVersion ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetPtpVersion)
        - [M SetTimestamp ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetTimestamp)
        - [M SetVlanCfi ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetVlanCfi)
        - [M SetVlanCfiOuter ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetVlanCfiOuter)
        - [M SetVlanPcp ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetVlanPcp)
        - [M SetVlanPcpOuter ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetVlanPcpOuter)
        - [M SetVlanVid ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetVlanVid)
        - [M SetVlanVidOuter ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetVlanVidOuter)
        - [A ethDstMac ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.ethDstMac)
        - [A ethPayload ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.ethPayload)
        - [A ethSrcMac ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.ethSrcMac)
        - [A ethType ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.ethType)
        - [A macSecAn ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.macSecAn)
        - [A macSecIcv ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.macSecIcv)
        - [A macSecPn ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.macSecPn)
        - [A macSecSci ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.macSecSci)
        - [A macSecSl ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.macSecSl)
        - [A macSecTci ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.macSecTci)
        - [A macSecTciAn ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.macSecTciAn)
        - [A macSecTciC ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.macSecTciC)
        - [A macSecTciE ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.macSecTciE)
        - [A macSecTciEs ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.macSecTciEs)
        - [A macSecTciSc ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.macSecTciSc)
        - [A macSecTciScb ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.macSecTciScb)
        - [A macSecTciV ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.macSecTciV)
        - [A parent ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.parent)
        - [A ptpControl ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.ptpControl)
        - [A ptpCorrectionField ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.ptpCorrectionField)
        - [A ptpDomainNumber ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.ptpDomainNumber)
        - [A ptpFlags ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.ptpFlags)
        - [A ptpLogMsgInterval ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.ptpLogMsgInterval)
        - [A ptpMsgLen ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.ptpMsgLen)
        - [A ptpMsgType ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.ptpMsgType)
        - [A ptpSequenceId ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.ptpSequenceId)
        - [A ptpSourcePortIdentity ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.ptpSourcePortIdentity)
        - [A ptpVersion ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.ptpVersion)
        - [A timestamp ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.timestamp)
        - [A vlanCfi ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.vlanCfi)
        - [A vlanCfiOuter ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.vlanCfiOuter)
        - [A vlanPcp ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.vlanPcp)
        - [A vlanPcpOuter ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.vlanPcpOuter)
        - [A vlanVid ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.vlanVid)
        - [A vlanVidOuter ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.vlanVidOuter)
    - [ PacketPtpFollowUp ](#packetptpfollowup)
      - [C PacketPtpFollowUp ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp)
        - [M GetPtpPreciseOriginTimestampSec ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetPtpPreciseOriginTimestampSec)
        - [M SetPtpPreciseOriginTimestampSec ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetPtpPreciseOriginTimestampSec)
        - [A ptpPreciseOriginTimestampSec ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.ptpPreciseOriginTimestampSec)
        - [M GetPtpPreciseOriginTimestampNSec ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetPtpPreciseOriginTimestampNSec)
        - [M SetPtpPreciseOriginTimestampNSec ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetPtpPreciseOriginTimestampNSec)
        - [A ptpPreciseOriginTimestampNSec ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.ptpPreciseOriginTimestampNSec)
        - [M FindParent ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.FindParent)
        - [M GetEthDstMac ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetEthDstMac)
        - [M GetEthPayload ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetEthPayload)
        - [M GetEthSrcMac ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetEthSrcMac)
        - [M GetEthType ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetEthType)
        - [M GetMacSecAn ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetMacSecAn)
        - [M GetMacSecIcv ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetMacSecIcv)
        - [M GetMacSecPn ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetMacSecPn)
        - [M GetMacSecSci ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetMacSecSci)
        - [M GetMacSecSl ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetMacSecSl)
        - [M GetMacSecTci ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetMacSecTci)
        - [M GetMacSecTciAn ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetMacSecTciAn)
        - [M GetMacSecTciC ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetMacSecTciC)
        - [M GetMacSecTciE ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetMacSecTciE)
        - [M GetMacSecTciEs ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetMacSecTciEs)
        - [M GetMacSecTciSc ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetMacSecTciSc)
        - [M GetMacSecTciScb ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetMacSecTciScb)
        - [M GetMacSecTciV ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetMacSecTciV)
        - [M GetPtpControl ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetPtpControl)
        - [M GetPtpCorrectionField ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetPtpCorrectionField)
        - [M GetPtpDomainNumber ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetPtpDomainNumber)
        - [M GetPtpFlags ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetPtpFlags)
        - [M GetPtpLogMsgInterval ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetPtpLogMsgInterval)
        - [M GetPtpMsgLen ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetPtpMsgLen)
        - [M GetPtpMsgType ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetPtpMsgType)
        - [M GetPtpSequenceId ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetPtpSequenceId)
        - [M GetPtpSourcePortIdentity ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetPtpSourcePortIdentity)
        - [M GetPtpVersion ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetPtpVersion)
        - [M GetTimestamp ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetTimestamp)
        - [M GetVlanCfi ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetVlanCfi)
        - [M GetVlanCfiOuter ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetVlanCfiOuter)
        - [M GetVlanPcp ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetVlanPcp)
        - [M GetVlanPcpOuter ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetVlanPcpOuter)
        - [M GetVlanVid ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetVlanVid)
        - [M GetVlanVidOuter ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetVlanVidOuter)
        - [M SetEthDstMac ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetEthDstMac)
        - [M SetEthPayload ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetEthPayload)
        - [M SetEthSrcMac ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetEthSrcMac)
        - [M SetEthType ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetEthType)
        - [M SetPtpControl ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetPtpControl)
        - [M SetPtpCorrectionField ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetPtpCorrectionField)
        - [M SetPtpDomainNumber ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetPtpDomainNumber)
        - [M SetPtpFlags ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetPtpFlags)
        - [M SetPtpLogMsgInterval ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetPtpLogMsgInterval)
        - [M SetPtpMsgLen ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetPtpMsgLen)
        - [M SetPtpMsgType ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetPtpMsgType)
        - [M SetPtpSequenceId ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetPtpSequenceId)
        - [M SetPtpSourcePortIdentity ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetPtpSourcePortIdentity)
        - [M SetPtpVersion ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetPtpVersion)
        - [M SetTimestamp ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetTimestamp)
        - [M SetVlanCfi ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetVlanCfi)
        - [M SetVlanCfiOuter ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetVlanCfiOuter)
        - [M SetVlanPcp ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetVlanPcp)
        - [M SetVlanPcpOuter ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetVlanPcpOuter)
        - [M SetVlanVid ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetVlanVid)
        - [M SetVlanVidOuter ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetVlanVidOuter)
        - [A ethDstMac ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.ethDstMac)
        - [A ethPayload ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.ethPayload)
        - [A ethSrcMac ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.ethSrcMac)
        - [A ethType ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.ethType)
        - [A macSecAn ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.macSecAn)
        - [A macSecIcv ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.macSecIcv)
        - [A macSecPn ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.macSecPn)
        - [A macSecSci ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.macSecSci)
        - [A macSecSl ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.macSecSl)
        - [A macSecTci ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.macSecTci)
        - [A macSecTciAn ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.macSecTciAn)
        - [A macSecTciC ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.macSecTciC)
        - [A macSecTciE ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.macSecTciE)
        - [A macSecTciEs ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.macSecTciEs)
        - [A macSecTciSc ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.macSecTciSc)
        - [A macSecTciScb ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.macSecTciScb)
        - [A macSecTciV ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.macSecTciV)
        - [A parent ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.parent)
        - [A ptpControl ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.ptpControl)
        - [A ptpCorrectionField ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.ptpCorrectionField)
        - [A ptpDomainNumber ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.ptpDomainNumber)
        - [A ptpFlags ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.ptpFlags)
        - [A ptpLogMsgInterval ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.ptpLogMsgInterval)
        - [A ptpMsgLen ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.ptpMsgLen)
        - [A ptpMsgType ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.ptpMsgType)
        - [A ptpSequenceId ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.ptpSequenceId)
        - [A ptpSourcePortIdentity ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.ptpSourcePortIdentity)
        - [A ptpVersion ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.ptpVersion)
        - [A timestamp ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.timestamp)
        - [A vlanCfi ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.vlanCfi)
        - [A vlanCfiOuter ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.vlanCfiOuter)
        - [A vlanPcp ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.vlanPcp)
        - [A vlanPcpOuter ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.vlanPcpOuter)
        - [A vlanVid ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.vlanVid)
        - [A vlanVidOuter ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.vlanVidOuter)
    - [ PacketPdelayReq ](#packetpdelayreq)
      - [C PacketPdelayReq ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq)
        - [M FindParent ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.FindParent)
        - [M GetEthDstMac ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetEthDstMac)
        - [M GetEthPayload ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetEthPayload)
        - [M GetEthSrcMac ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetEthSrcMac)
        - [M GetEthType ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetEthType)
        - [M GetMacSecAn ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetMacSecAn)
        - [M GetMacSecIcv ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetMacSecIcv)
        - [M GetMacSecPn ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetMacSecPn)
        - [M GetMacSecSci ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetMacSecSci)
        - [M GetMacSecSl ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetMacSecSl)
        - [M GetMacSecTci ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetMacSecTci)
        - [M GetMacSecTciAn ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetMacSecTciAn)
        - [M GetMacSecTciC ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetMacSecTciC)
        - [M GetMacSecTciE ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetMacSecTciE)
        - [M GetMacSecTciEs ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetMacSecTciEs)
        - [M GetMacSecTciSc ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetMacSecTciSc)
        - [M GetMacSecTciScb ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetMacSecTciScb)
        - [M GetMacSecTciV ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetMacSecTciV)
        - [M GetPtpControl ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetPtpControl)
        - [M GetPtpCorrectionField ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetPtpCorrectionField)
        - [M GetPtpDomainNumber ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetPtpDomainNumber)
        - [M GetPtpFlags ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetPtpFlags)
        - [M GetPtpLogMsgInterval ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetPtpLogMsgInterval)
        - [M GetPtpMsgLen ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetPtpMsgLen)
        - [M GetPtpMsgType ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetPtpMsgType)
        - [M GetPtpSequenceId ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetPtpSequenceId)
        - [M GetPtpSourcePortIdentity ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetPtpSourcePortIdentity)
        - [M GetPtpVersion ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetPtpVersion)
        - [M GetTimestamp ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetTimestamp)
        - [M GetVlanCfi ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetVlanCfi)
        - [M GetVlanCfiOuter ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetVlanCfiOuter)
        - [M GetVlanPcp ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetVlanPcp)
        - [M GetVlanPcpOuter ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetVlanPcpOuter)
        - [M GetVlanVid ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetVlanVid)
        - [M GetVlanVidOuter ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetVlanVidOuter)
        - [M SetEthDstMac ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetEthDstMac)
        - [M SetEthPayload ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetEthPayload)
        - [M SetEthSrcMac ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetEthSrcMac)
        - [M SetEthType ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetEthType)
        - [M SetPtpControl ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetPtpControl)
        - [M SetPtpCorrectionField ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetPtpCorrectionField)
        - [M SetPtpDomainNumber ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetPtpDomainNumber)
        - [M SetPtpFlags ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetPtpFlags)
        - [M SetPtpLogMsgInterval ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetPtpLogMsgInterval)
        - [M SetPtpMsgLen ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetPtpMsgLen)
        - [M SetPtpMsgType ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetPtpMsgType)
        - [M SetPtpSequenceId ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetPtpSequenceId)
        - [M SetPtpSourcePortIdentity ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetPtpSourcePortIdentity)
        - [M SetPtpVersion ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetPtpVersion)
        - [M SetTimestamp ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetTimestamp)
        - [M SetVlanCfi ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetVlanCfi)
        - [M SetVlanCfiOuter ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetVlanCfiOuter)
        - [M SetVlanPcp ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetVlanPcp)
        - [M SetVlanPcpOuter ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetVlanPcpOuter)
        - [M SetVlanVid ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetVlanVid)
        - [M SetVlanVidOuter ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetVlanVidOuter)
        - [A ethDstMac ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.ethDstMac)
        - [A ethPayload ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.ethPayload)
        - [A ethSrcMac ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.ethSrcMac)
        - [A ethType ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.ethType)
        - [A macSecAn ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.macSecAn)
        - [A macSecIcv ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.macSecIcv)
        - [A macSecPn ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.macSecPn)
        - [A macSecSci ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.macSecSci)
        - [A macSecSl ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.macSecSl)
        - [A macSecTci ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.macSecTci)
        - [A macSecTciAn ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.macSecTciAn)
        - [A macSecTciC ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.macSecTciC)
        - [A macSecTciE ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.macSecTciE)
        - [A macSecTciEs ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.macSecTciEs)
        - [A macSecTciSc ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.macSecTciSc)
        - [A macSecTciScb ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.macSecTciScb)
        - [A macSecTciV ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.macSecTciV)
        - [A parent ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.parent)
        - [A ptpControl ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.ptpControl)
        - [A ptpCorrectionField ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.ptpCorrectionField)
        - [A ptpDomainNumber ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.ptpDomainNumber)
        - [A ptpFlags ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.ptpFlags)
        - [A ptpLogMsgInterval ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.ptpLogMsgInterval)
        - [A ptpMsgLen ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.ptpMsgLen)
        - [A ptpMsgType ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.ptpMsgType)
        - [A ptpSequenceId ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.ptpSequenceId)
        - [A ptpSourcePortIdentity ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.ptpSourcePortIdentity)
        - [A ptpVersion ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.ptpVersion)
        - [A timestamp ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.timestamp)
        - [A vlanCfi ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.vlanCfi)
        - [A vlanCfiOuter ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.vlanCfiOuter)
        - [A vlanPcp ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.vlanPcp)
        - [A vlanPcpOuter ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.vlanPcpOuter)
        - [A vlanVid ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.vlanVid)
        - [A vlanVidOuter ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.vlanVidOuter)
    - [ PacketPdelayResp ](#packetpdelayresp)
      - [C PacketPdelayResp ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp)
        - [M GetPtpRequestReceiptTimestampSec ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetPtpRequestReceiptTimestampSec)
        - [M SetPtpRequestReceiptTimestampSec ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetPtpRequestReceiptTimestampSec)
        - [A ptpRequestReceiptTimestampSec ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.ptpRequestReceiptTimestampSec)
        - [M GetPtpRequestReceiptTimestampNSec ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetPtpRequestReceiptTimestampNSec)
        - [M SetPtpRequestReceiptTimestampNSec ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetPtpRequestReceiptTimestampNSec)
        - [A ptpRequestReceiptTimestampNSec ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.ptpRequestReceiptTimestampNSec)
        - [M GetPtpRequestingPortIdentity ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetPtpRequestingPortIdentity)
        - [M SetPtpRequestingPortIdentity ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetPtpRequestingPortIdentity)
        - [A ptpRequestingPortIdentity ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.ptpRequestingPortIdentity)
        - [M FindParent ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.FindParent)
        - [M GetEthDstMac ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetEthDstMac)
        - [M GetEthPayload ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetEthPayload)
        - [M GetEthSrcMac ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetEthSrcMac)
        - [M GetEthType ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetEthType)
        - [M GetMacSecAn ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetMacSecAn)
        - [M GetMacSecIcv ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetMacSecIcv)
        - [M GetMacSecPn ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetMacSecPn)
        - [M GetMacSecSci ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetMacSecSci)
        - [M GetMacSecSl ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetMacSecSl)
        - [M GetMacSecTci ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetMacSecTci)
        - [M GetMacSecTciAn ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetMacSecTciAn)
        - [M GetMacSecTciC ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetMacSecTciC)
        - [M GetMacSecTciE ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetMacSecTciE)
        - [M GetMacSecTciEs ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetMacSecTciEs)
        - [M GetMacSecTciSc ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetMacSecTciSc)
        - [M GetMacSecTciScb ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetMacSecTciScb)
        - [M GetMacSecTciV ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetMacSecTciV)
        - [M GetPtpControl ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetPtpControl)
        - [M GetPtpCorrectionField ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetPtpCorrectionField)
        - [M GetPtpDomainNumber ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetPtpDomainNumber)
        - [M GetPtpFlags ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetPtpFlags)
        - [M GetPtpLogMsgInterval ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetPtpLogMsgInterval)
        - [M GetPtpMsgLen ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetPtpMsgLen)
        - [M GetPtpMsgType ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetPtpMsgType)
        - [M GetPtpSequenceId ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetPtpSequenceId)
        - [M GetPtpSourcePortIdentity ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetPtpSourcePortIdentity)
        - [M GetPtpVersion ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetPtpVersion)
        - [M GetTimestamp ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetTimestamp)
        - [M GetVlanCfi ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetVlanCfi)
        - [M GetVlanCfiOuter ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetVlanCfiOuter)
        - [M GetVlanPcp ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetVlanPcp)
        - [M GetVlanPcpOuter ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetVlanPcpOuter)
        - [M GetVlanVid ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetVlanVid)
        - [M GetVlanVidOuter ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetVlanVidOuter)
        - [M SetEthDstMac ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetEthDstMac)
        - [M SetEthPayload ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetEthPayload)
        - [M SetEthSrcMac ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetEthSrcMac)
        - [M SetEthType ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetEthType)
        - [M SetPtpControl ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetPtpControl)
        - [M SetPtpCorrectionField ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetPtpCorrectionField)
        - [M SetPtpDomainNumber ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetPtpDomainNumber)
        - [M SetPtpFlags ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetPtpFlags)
        - [M SetPtpLogMsgInterval ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetPtpLogMsgInterval)
        - [M SetPtpMsgLen ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetPtpMsgLen)
        - [M SetPtpMsgType ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetPtpMsgType)
        - [M SetPtpSequenceId ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetPtpSequenceId)
        - [M SetPtpSourcePortIdentity ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetPtpSourcePortIdentity)
        - [M SetPtpVersion ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetPtpVersion)
        - [M SetTimestamp ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetTimestamp)
        - [M SetVlanCfi ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetVlanCfi)
        - [M SetVlanCfiOuter ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetVlanCfiOuter)
        - [M SetVlanPcp ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetVlanPcp)
        - [M SetVlanPcpOuter ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetVlanPcpOuter)
        - [M SetVlanVid ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetVlanVid)
        - [M SetVlanVidOuter ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetVlanVidOuter)
        - [A ethDstMac ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.ethDstMac)
        - [A ethPayload ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.ethPayload)
        - [A ethSrcMac ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.ethSrcMac)
        - [A ethType ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.ethType)
        - [A macSecAn ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.macSecAn)
        - [A macSecIcv ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.macSecIcv)
        - [A macSecPn ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.macSecPn)
        - [A macSecSci ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.macSecSci)
        - [A macSecSl ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.macSecSl)
        - [A macSecTci ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.macSecTci)
        - [A macSecTciAn ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.macSecTciAn)
        - [A macSecTciC ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.macSecTciC)
        - [A macSecTciE ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.macSecTciE)
        - [A macSecTciEs ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.macSecTciEs)
        - [A macSecTciSc ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.macSecTciSc)
        - [A macSecTciScb ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.macSecTciScb)
        - [A macSecTciV ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.macSecTciV)
        - [A parent ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.parent)
        - [A ptpControl ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.ptpControl)
        - [A ptpCorrectionField ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.ptpCorrectionField)
        - [A ptpDomainNumber ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.ptpDomainNumber)
        - [A ptpFlags ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.ptpFlags)
        - [A ptpLogMsgInterval ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.ptpLogMsgInterval)
        - [A ptpMsgLen ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.ptpMsgLen)
        - [A ptpMsgType ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.ptpMsgType)
        - [A ptpSequenceId ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.ptpSequenceId)
        - [A ptpSourcePortIdentity ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.ptpSourcePortIdentity)
        - [A ptpVersion ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.ptpVersion)
        - [A timestamp ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.timestamp)
        - [A vlanCfi ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.vlanCfi)
        - [A vlanCfiOuter ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.vlanCfiOuter)
        - [A vlanPcp ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.vlanPcp)
        - [A vlanPcpOuter ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.vlanPcpOuter)
        - [A vlanVid ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.vlanVid)
        - [A vlanVidOuter ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.vlanVidOuter)
    - [ PacketPdelayRespFollowUp ](#packetpdelayrespfollowup)
      - [C PacketPdelayRespFollowUp ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp)
        - [M GetPtpResponseOriginTimestampSec ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetPtpResponseOriginTimestampSec)
        - [M SetPtpResponseOriginTimestampSec ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetPtpResponseOriginTimestampSec)
        - [A ptpResponseOriginTimestampSec ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.ptpResponseOriginTimestampSec)
        - [M GetPtpResponseOriginTimestampNSec ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetPtpResponseOriginTimestampNSec)
        - [M SetPtpResponseOriginTimestampNSec ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetPtpResponseOriginTimestampNSec)
        - [A ptpResponseOriginTimestampNSec ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.ptpResponseOriginTimestampNSec)
        - [M GetPtpRequestingPortIdentity ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetPtpRequestingPortIdentity)
        - [M SetPtpRequestingPortIdentity ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetPtpRequestingPortIdentity)
        - [A ptpRequestingPortIdentity ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.ptpRequestingPortIdentity)
        - [M FindParent ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.FindParent)
        - [M GetEthDstMac ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetEthDstMac)
        - [M GetEthPayload ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetEthPayload)
        - [M GetEthSrcMac ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetEthSrcMac)
        - [M GetEthType ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetEthType)
        - [M GetMacSecAn ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetMacSecAn)
        - [M GetMacSecIcv ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetMacSecIcv)
        - [M GetMacSecPn ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetMacSecPn)
        - [M GetMacSecSci ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetMacSecSci)
        - [M GetMacSecSl ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetMacSecSl)
        - [M GetMacSecTci ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetMacSecTci)
        - [M GetMacSecTciAn ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetMacSecTciAn)
        - [M GetMacSecTciC ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetMacSecTciC)
        - [M GetMacSecTciE ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetMacSecTciE)
        - [M GetMacSecTciEs ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetMacSecTciEs)
        - [M GetMacSecTciSc ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetMacSecTciSc)
        - [M GetMacSecTciScb ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetMacSecTciScb)
        - [M GetMacSecTciV ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetMacSecTciV)
        - [M GetPtpControl ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetPtpControl)
        - [M GetPtpCorrectionField ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetPtpCorrectionField)
        - [M GetPtpDomainNumber ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetPtpDomainNumber)
        - [M GetPtpFlags ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetPtpFlags)
        - [M GetPtpLogMsgInterval ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetPtpLogMsgInterval)
        - [M GetPtpMsgLen ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetPtpMsgLen)
        - [M GetPtpMsgType ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetPtpMsgType)
        - [M GetPtpSequenceId ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetPtpSequenceId)
        - [M GetPtpSourcePortIdentity ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetPtpSourcePortIdentity)
        - [M GetPtpVersion ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetPtpVersion)
        - [M GetTimestamp ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetTimestamp)
        - [M GetVlanCfi ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetVlanCfi)
        - [M GetVlanCfiOuter ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetVlanCfiOuter)
        - [M GetVlanPcp ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetVlanPcp)
        - [M GetVlanPcpOuter ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetVlanPcpOuter)
        - [M GetVlanVid ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetVlanVid)
        - [M GetVlanVidOuter ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetVlanVidOuter)
        - [M SetEthDstMac ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetEthDstMac)
        - [M SetEthPayload ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetEthPayload)
        - [M SetEthSrcMac ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetEthSrcMac)
        - [M SetEthType ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetEthType)
        - [M SetPtpControl ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetPtpControl)
        - [M SetPtpCorrectionField ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetPtpCorrectionField)
        - [M SetPtpDomainNumber ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetPtpDomainNumber)
        - [M SetPtpFlags ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetPtpFlags)
        - [M SetPtpLogMsgInterval ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetPtpLogMsgInterval)
        - [M SetPtpMsgLen ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetPtpMsgLen)
        - [M SetPtpMsgType ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetPtpMsgType)
        - [M SetPtpSequenceId ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetPtpSequenceId)
        - [M SetPtpSourcePortIdentity ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetPtpSourcePortIdentity)
        - [M SetPtpVersion ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetPtpVersion)
        - [M SetTimestamp ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetTimestamp)
        - [M SetVlanCfi ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetVlanCfi)
        - [M SetVlanCfiOuter ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetVlanCfiOuter)
        - [M SetVlanPcp ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetVlanPcp)
        - [M SetVlanPcpOuter ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetVlanPcpOuter)
        - [M SetVlanVid ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetVlanVid)
        - [M SetVlanVidOuter ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetVlanVidOuter)
        - [A ethDstMac ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.ethDstMac)
        - [A ethPayload ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.ethPayload)
        - [A ethSrcMac ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.ethSrcMac)
        - [A ethType ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.ethType)
        - [A macSecAn ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.macSecAn)
        - [A macSecIcv ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.macSecIcv)
        - [A macSecPn ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.macSecPn)
        - [A macSecSci ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.macSecSci)
        - [A macSecSl ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.macSecSl)
        - [A macSecTci ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.macSecTci)
        - [A macSecTciAn ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.macSecTciAn)
        - [A macSecTciC ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.macSecTciC)
        - [A macSecTciE ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.macSecTciE)
        - [A macSecTciEs ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.macSecTciEs)
        - [A macSecTciSc ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.macSecTciSc)
        - [A macSecTciScb ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.macSecTciScb)
        - [A macSecTciV ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.macSecTciV)
        - [A parent ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.parent)
        - [A ptpControl ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.ptpControl)
        - [A ptpCorrectionField ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.ptpCorrectionField)
        - [A ptpDomainNumber ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.ptpDomainNumber)
        - [A ptpFlags ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.ptpFlags)
        - [A ptpLogMsgInterval ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.ptpLogMsgInterval)
        - [A ptpMsgLen ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.ptpMsgLen)
        - [A ptpMsgType ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.ptpMsgType)
        - [A ptpSequenceId ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.ptpSequenceId)
        - [A ptpSourcePortIdentity ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.ptpSourcePortIdentity)
        - [A ptpVersion ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.ptpVersion)
        - [A timestamp ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.timestamp)
        - [A vlanCfi ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.vlanCfi)
        - [A vlanCfiOuter ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.vlanCfiOuter)
        - [A vlanPcp ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.vlanPcp)
        - [A vlanPcpOuter ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.vlanPcpOuter)
        - [A vlanVid ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.vlanVid)
        - [A vlanVidOuter ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.vlanVidOuter)
  - [ SOME/IP ](#some-ip)
    - [ PacketSomeIp ](#packetsomeip)
      - [C PacketSomeIp ](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp)
        - [A SOMEIP_MSG_REQUEST ](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.SOMEIP_MSG_REQUEST)
        - [A SOMEIP_MSG_REQUEST_NO_RETURN ](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.SOMEIP_MSG_REQUEST_NO_RETURN)
        - [A SOMEIP_MSG_NOTIFICATION ](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.SOMEIP_MSG_NOTIFICATION)
        - [A SOMEIP_MSG_TP ](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.SOMEIP_MSG_TP)
        - [A SOMEIP_MSG_RESPONSE ](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.SOMEIP_MSG_RESPONSE)
        - [A SOMEIP_MSG_ERROR ](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.SOMEIP_MSG_ERROR)
        - [A SOMEIP_RETURN_OK ](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.SOMEIP_RETURN_OK)
        - [A SOMEIP_RETURN_NOT_OK ](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.SOMEIP_RETURN_NOT_OK)
        - [A SOMEIP_RETURN_UNKNOWN_SERVICE ](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.SOMEIP_RETURN_UNKNOWN_SERVICE)
        - [A SOMEIP_RETURN_UNKNOWN_METHOD ](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.SOMEIP_RETURN_UNKNOWN_METHOD)
        - [A SOMEIP_RETURN_NOT_READY ](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.SOMEIP_RETURN_NOT_READY)
        - [A SOMEIP_RETURN_NOT_REACHABLE ](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.SOMEIP_RETURN_NOT_REACHABLE)
        - [A SOMEIP_RETURN_TIMEOUT ](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.SOMEIP_RETURN_TIMEOUT)
        - [A SOMEIP_RETURN_WRONG_PROTOCOL_VERSION ](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.SOMEIP_RETURN_WRONG_PROTOCOL_VERSION)
        - [A SOMEIP_RETURN_WRONG_INTERFACE_VERSION ](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.SOMEIP_RETURN_WRONG_INTERFACE_VERSION)
        - [A SOMEIP_RETURN_MALFORMED ](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.SOMEIP_RETURN_MALFORMED)
        - [A SOMEIP_RETURN_TCP_ERROR ](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.SOMEIP_RETURN_TCP_ERROR)
        - [M GetSomeIpMessagesFromPayload ](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.GetSomeIpMessagesFromPayload)
        - [M Create ](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.Create)
        - [M CalcLen ](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.CalcLen)
        - [A messageId ](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.messageId)
        - [A serviceId ](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.serviceId)
        - [A methodId ](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.methodId)
        - [A length ](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.length)
        - [A requestId ](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.requestId)
        - [A clientId ](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.clientId)
        - [A sessionId ](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.sessionId)
        - [A protocolVersion ](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.protocolVersion)
        - [A interfaceVersion ](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.interfaceVersion)
        - [A messageType ](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.messageType)
        - [A returnCode ](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.returnCode)
        - [A payload ](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.payload)
        - [M GetHeaderBytes ](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.GetHeaderBytes)
        - [A instanceIds ](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.instanceIds)
        - [M FindParent ](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.FindParent)
        - [A parent ](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.parent)
        - [A timestamp ](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.timestamp)
    - [ PacketSomeIpSd ](#packetsomeipsd)
      - [C PacketSomeIpSd ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSd)
        - [M `\_\_init\_\_` ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSd.__init__)
        - [M CalcEntryArrayLen ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSd.CalcEntryArrayLen)
        - [M CalcOptionArrayLen ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSd.CalcOptionArrayLen)
        - [M Create ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSd.Create)
        - [M FindParent ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSd.FindParent)
        - [A entryLen ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSd.entryLen)
        - [A entryList ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSd.entryList)
        - [A optionLen ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSd.optionLen)
        - [A optionList ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSd.optionList)
        - [A parent ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSd.parent)
        - [A rebootFlag ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSd.rebootFlag)
        - [A timestamp ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSd.timestamp)
        - [A unicastFlag ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSd.unicastFlag)
    - [ PacketSomeIpSdEntry ](#packetsomeipsdentry)
      - [C PacketSomeIpSdEntry ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntry)
        - [A index1 ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntry.index1)
        - [A index2 ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntry.index2)
        - [A instanceId ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntry.instanceId)
        - [A majorVersion ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntry.majorVersion)
        - [A optionCount1 ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntry.optionCount1)
        - [A optionCount2 ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntry.optionCount2)
        - [A serviceId ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntry.serviceId)
        - [A ttl ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntry.ttl)
        - [A type ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntry.type)
    - [ PacketSomeIpSdEntryService ](#packetsomeipsdentryservice)
      - [C PacketSomeIpSdEntryService ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryService)
        - [A SERVICE_FIND ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryService.SERVICE_FIND)
        - [A SERVICE_OFFER ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryService.SERVICE_OFFER)
        - [A SERVICE_STOP_OFFER ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryService.SERVICE_STOP_OFFER)
        - [M Create ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryService.Create)
        - [A minorVersion ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryService.minorVersion)
    - [ PacketSomeIpSdEntryEventgroup ](#packetsomeipsdentryeventgroup)
      - [C PacketSomeIpSdEntryEventgroup ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryEventgroup)
        - [A EVENTGROUP_SUBSCRIBE ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryEventgroup.EVENTGROUP_SUBSCRIBE)
        - [A EVENTGROUP_SUBSCRIBE_ACK ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryEventgroup.EVENTGROUP_SUBSCRIBE_ACK)
        - [A EVENTGROUP_STOP_SUBSCRIBE ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryEventgroup.EVENTGROUP_STOP_SUBSCRIBE)
        - [A EVENTGROUP_SUBSCRIBE_NACK ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryEventgroup.EVENTGROUP_SUBSCRIBE_NACK)
        - [M Create ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryEventgroup.Create)
        - [A eventgroupId ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryEventgroup.eventgroupId)
    - [ PacketSomeIpSdOption ](#packetsomeipsdoption)
      - [C PacketSomeIpSdOption ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOption)
        - [A TRANSPORT_TCP ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOption.TRANSPORT_TCP)
        - [A TRANSPORT_UDP ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOption.TRANSPORT_UDP)
        - [A PACKET_SOME_IP_SD_OPTION_CONFIG ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOption.PACKET_SOME_IP_SD_OPTION_CONFIG)
        - [A PACKET_SOME_IP_SD_OPTION_IPV4 ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOption.PACKET_SOME_IP_SD_OPTION_IPV4)
        - [A PACKET_SOME_IP_SD_OPTION_IPV6 ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOption.PACKET_SOME_IP_SD_OPTION_IPV6)
        - [A PACKET_SOME_IP_SD_OPTION_IPV4_MULTICAST ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOption.PACKET_SOME_IP_SD_OPTION_IPV4_MULTICAST)
        - [A PACKET_SOME_IP_SD_OPTION_IPV4_SD ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOption.PACKET_SOME_IP_SD_OPTION_IPV4_SD)
        - [A PACKET_SOME_IP_SD_OPTION_IPV6_MULTICAST ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOption.PACKET_SOME_IP_SD_OPTION_IPV6_MULTICAST)
        - [A PACKET_SOME_IP_SD_OPTION_IPV6_SD ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOption.PACKET_SOME_IP_SD_OPTION_IPV6_SD)
        - [A optionLen ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOption.optionLen)
        - [A type ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOption.type)
    - [ PacketSomeIpSdOptionIpv4 ](#packetsomeipsdoptionipv4)
      - [C PacketSomeIpSdOptionIpv4 ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4)
        - [M Create ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4.Create)
        - [A ip ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4.ip)
        - [A optionLen ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4.optionLen)
        - [A port ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4.port)
        - [A protocol ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4.protocol)
    - [ PacketSomeIpSdOptionIpv6 ](#packetsomeipsdoptionipv6)
      - [C PacketSomeIpSdOptionIpv6 ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6)
        - [M Create ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6.Create)
        - [A ip ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6.ip)
        - [A optionLen ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6.optionLen)
        - [A port ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6.port)
        - [A protocol ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6.protocol)
    - [ PacketSomeIpSdOptionIpv4Multicast ](#packetsomeipsdoptionipv4multicast)
      - [C PacketSomeIpSdOptionIpv4Multicast ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4Multicast)
        - [M Create ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4Multicast.Create)
        - [A ip ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4Multicast.ip)
        - [A optionLen ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4Multicast.optionLen)
        - [A port ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4Multicast.port)
        - [A protocol ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4Multicast.protocol)
    - [ PacketSomeIpSdOptionIpv6Multicast ](#packetsomeipsdoptionipv6multicast)
      - [C PacketSomeIpSdOptionIpv6Multicast ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6Multicast)
        - [M Create ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6Multicast.Create)
        - [A ip ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6Multicast.ip)
        - [A optionLen ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6Multicast.optionLen)
        - [A port ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6Multicast.port)
        - [A protocol ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6Multicast.protocol)
    - [ PacketSomeIpSdOptionIpv4SD ](#packetsomeipsdoptionipv4sd)
      - [C PacketSomeIpSdOptionIpv4SD ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4SD)
        - [M Create ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4SD.Create)
        - [A ip ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4SD.ip)
        - [A optionLen ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4SD.optionLen)
        - [A port ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4SD.port)
        - [A protocol ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4SD.protocol)
    - [ PacketSomeIpSdOptionIpv6SD ](#packetsomeipsdoptionipv6sd)
      - [C PacketSomeIpSdOptionIpv6SD ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6SD)
        - [M Create ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6SD.Create)
        - [A ip ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6SD.ip)
        - [A optionLen ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6SD.optionLen)
        - [A port ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6SD.port)
        - [A protocol ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6SD.protocol)
    - [ PacketSomeIpSdOptionConfig ](#packetsomeipsdoptionconfig)
      - [C PacketSomeIpSdOptionConfig ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionConfig)
        - [M Create ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionConfig.Create)
        - [A config ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionConfig.config)
        - [A optionLen ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionConfig.optionLen)

[ Bus related objects of trace analysis ](busdatastructuresTraceanalysis.md)

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

Advanced properties of bus-related objects

- [ CAN ](#can)
  - [C CanFrame ](#tts.testModule.bus.busObjects.CAN.CanFrame)
    - [A canID ](#tts.testModule.bus.busObjects.CAN.CanFrame.canID)
    - [A flags ](#tts.testModule.bus.busObjects.CAN.CanFrame.flags)
    - [A length ](#tts.testModule.bus.busObjects.CAN.CanFrame.length)
    - [A payload ](#tts.testModule.bus.busObjects.CAN.CanFrame.payload)
    - [A timestamp ](#tts.testModule.bus.busObjects.CAN.CanFrame.timestamp)
  - [C CanFlags ](#tts.testModule.bus.busObjects.CAN.CanFlags)
    - [A isError ](#tts.testModule.bus.busObjects.CAN.CanFlags.isError)
    - [A isRemote ](#tts.testModule.bus.busObjects.CAN.CanFlags.isRemote)
    - [A isExtended ](#tts.testModule.bus.busObjects.CAN.CanFlags.isExtended)
    - [A isSelfReceived ](#tts.testModule.bus.busObjects.CAN.CanFlags.isSelfReceived)
    - [A isTx ](#tts.testModule.bus.busObjects.CAN.CanFlags.isTx)
    - [A isEDL ](#tts.testModule.bus.busObjects.CAN.CanFlags.isEDL)
    - [A isBRS ](#tts.testModule.bus.busObjects.CAN.CanFlags.isBRS)
- [ FlexRay ](#flexray)
  - [C FlexRayFrame ](#tts.testModule.bus.busObjects.FlexRay.FlexRayFrame)
    - [A slotID ](#tts.testModule.bus.busObjects.FlexRay.FlexRayFrame.slotID)
    - [A cycleNumber ](#tts.testModule.bus.busObjects.FlexRay.FlexRayFrame.cycleNumber)
    - [A headerCRC ](#tts.testModule.bus.busObjects.FlexRay.FlexRayFrame.headerCRC)
    - [A channelID ](#tts.testModule.bus.busObjects.FlexRay.FlexRayFrame.channelID)
    - [A flags ](#tts.testModule.bus.busObjects.FlexRay.FlexRayFrame.flags)
    - [A payload ](#tts.testModule.bus.busObjects.FlexRay.FlexRayFrame.payload)
    - [A timestamp ](#tts.testModule.bus.busObjects.FlexRay.FlexRayFrame.timestamp)
  - [C FlexRayFlags ](#tts.testModule.bus.busObjects.FlexRay.FlexRayFlags)
    - [A isSelfReceived ](#tts.testModule.bus.busObjects.FlexRay.FlexRayFlags.isSelfReceived)
    - [A isTx ](#tts.testModule.bus.busObjects.FlexRay.FlexRayFlags.isTx)
    - [A isNull ](#tts.testModule.bus.busObjects.FlexRay.FlexRayFlags.isNull)
    - [A isValid ](#tts.testModule.bus.busObjects.FlexRay.FlexRayFlags.isValid)
    - [A isSync ](#tts.testModule.bus.busObjects.FlexRay.FlexRayFlags.isSync)
    - [A isStartup ](#tts.testModule.bus.busObjects.FlexRay.FlexRayFlags.isStartup)
    - [A hasPayloadPreamble ](#tts.testModule.bus.busObjects.FlexRay.FlexRayFlags.hasPayloadPreamble)
    - [A isError ](#tts.testModule.bus.busObjects.FlexRay.FlexRayFlags.isError)
    - [A isAsync ](#tts.testModule.bus.busObjects.FlexRay.FlexRayFlags.isAsync)
    - [A isDynamic ](#tts.testModule.bus.busObjects.FlexRay.FlexRayFlags.isDynamic)
- [ LIN ](#lin)
  - [C LinFrame ](#tts.testModule.bus.busObjects.LIN.LinFrame)
    - [A linID ](#tts.testModule.bus.busObjects.LIN.LinFrame.linID)
    - [A crc ](#tts.testModule.bus.busObjects.LIN.LinFrame.crc)
    - [A flags ](#tts.testModule.bus.busObjects.LIN.LinFrame.flags)
    - [A payload ](#tts.testModule.bus.busObjects.LIN.LinFrame.payload)
    - [A timestamp ](#tts.testModule.bus.busObjects.LIN.LinFrame.timestamp)
  - [C LinFlags ](#tts.testModule.bus.busObjects.LIN.LinFlags)
    - [A isCrcError ](#tts.testModule.bus.busObjects.LIN.LinFlags.isCrcError)
    - [A isSelfReceived ](#tts.testModule.bus.busObjects.LIN.LinFlags.isSelfReceived)
    - [A isTx ](#tts.testModule.bus.busObjects.LIN.LinFlags.isTx)
- [ Ethernet ](#ethernet)
  - [C Ethernet ](#tts.core.api.internalApi.Ethernet.Ethernet)
    - [A UDP ](#tts.core.api.internalApi.Ethernet.Ethernet.UDP)
    - [A TCP ](#tts.core.api.internalApi.Ethernet.Ethernet.TCP)
    - [A PacketEthernet ](#tts.core.api.internalApi.Ethernet.Ethernet.PacketEthernet)
    - [A PacketIp4 ](#tts.core.api.internalApi.Ethernet.Ethernet.PacketIp4)
    - [A PacketIp6 ](#tts.core.api.internalApi.Ethernet.Ethernet.PacketIp6)
    - [A PacketIcmp ](#tts.core.api.internalApi.Ethernet.Ethernet.PacketIcmp)
    - [A PacketMka ](#tts.core.api.internalApi.Ethernet.Ethernet.PacketMka)
    - [A PacketIke ](#tts.core.api.internalApi.Ethernet.Ethernet.PacketIke)
    - [A PacketTcp ](#tts.core.api.internalApi.Ethernet.Ethernet.PacketTcp)
    - [A PacketUdp ](#tts.core.api.internalApi.Ethernet.Ethernet.PacketUdp)
    - [A PacketPtpSync ](#tts.core.api.internalApi.Ethernet.Ethernet.PacketPtpSync)
    - [A PacketPtpFollowUp ](#tts.core.api.internalApi.Ethernet.Ethernet.PacketPtpFollowUp)
    - [A PacketPdelayReq ](#tts.core.api.internalApi.Ethernet.Ethernet.PacketPdelayReq)
    - [A PacketPdelayResp ](#tts.core.api.internalApi.Ethernet.Ethernet.PacketPdelayResp)
    - [A PacketPdelayRespFollowUp ](#tts.core.api.internalApi.Ethernet.Ethernet.PacketPdelayRespFollowUp)
    - [A PacketSomeIp ](#tts.core.api.internalApi.Ethernet.Ethernet.PacketSomeIp)
    - [A PacketSomeIpSd ](#tts.core.api.internalApi.Ethernet.Ethernet.PacketSomeIpSd)
    - [A PacketSomeIpSdEntry ](#tts.core.api.internalApi.Ethernet.Ethernet.PacketSomeIpSdEntry)
    - [A PacketSomeIpSdEntryService ](#tts.core.api.internalApi.Ethernet.Ethernet.PacketSomeIpSdEntryService)
    - [A PacketSomeIpSdEntryEventgroup ](#tts.core.api.internalApi.Ethernet.Ethernet.PacketSomeIpSdEntryEventgroup)
    - [A PacketSomeIpSdOptionIpv4 ](#tts.core.api.internalApi.Ethernet.Ethernet.PacketSomeIpSdOptionIpv4)
    - [A PacketSomeIpSdOption ](#tts.core.api.internalApi.Ethernet.Ethernet.PacketSomeIpSdOption)
    - [A PacketSomeIpSdOptionIpv6 ](#tts.core.api.internalApi.Ethernet.Ethernet.PacketSomeIpSdOptionIpv6)
    - [A PacketSomeIpSdOptionIpv4Multicast ](#tts.core.api.internalApi.Ethernet.Ethernet.PacketSomeIpSdOptionIpv4Multicast)
    - [A PacketSomeIpSdOptionIpv6Multicast ](#tts.core.api.internalApi.Ethernet.Ethernet.PacketSomeIpSdOptionIpv6Multicast)
    - [A PacketSomeIpSdOptionIpv4SD ](#tts.core.api.internalApi.Ethernet.Ethernet.PacketSomeIpSdOptionIpv4SD)
    - [A PacketSomeIpSdOptionIpv6SD ](#tts.core.api.internalApi.Ethernet.Ethernet.PacketSomeIpSdOptionIpv6SD)
    - [A PacketSomeIpSdOptionConfig ](#tts.core.api.internalApi.Ethernet.Ethernet.PacketSomeIpSdOptionConfig)
  - [ PacketEthernet ](#packetethernet)
    - [C PacketEthernet ](#tts.lib.ethernet.PacketEthernet.PacketEthernet)
      - [M GetEthDstMac ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.GetEthDstMac)
      - [M SetEthDstMac ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.SetEthDstMac)
      - [A ethDstMac ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.ethDstMac)
      - [M GetEthSrcMac ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.GetEthSrcMac)
      - [M SetEthSrcMac ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.SetEthSrcMac)
      - [A ethSrcMac ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.ethSrcMac)
      - [M GetEthType ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.GetEthType)
      - [M SetEthType ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.SetEthType)
      - [A ethType ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.ethType)
      - [M GetVlanPcp ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.GetVlanPcp)
      - [M SetVlanPcp ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.SetVlanPcp)
      - [A vlanPcp ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.vlanPcp)
      - [M GetVlanCfi ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.GetVlanCfi)
      - [M SetVlanCfi ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.SetVlanCfi)
      - [A vlanCfi ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.vlanCfi)
      - [M GetVlanVid ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.GetVlanVid)
      - [M SetVlanVid ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.SetVlanVid)
      - [A vlanVid ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.vlanVid)
      - [M GetVlanPcpOuter ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.GetVlanPcpOuter)
      - [M SetVlanPcpOuter ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.SetVlanPcpOuter)
      - [A vlanPcpOuter ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.vlanPcpOuter)
      - [M GetVlanCfiOuter ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.GetVlanCfiOuter)
      - [M SetVlanCfiOuter ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.SetVlanCfiOuter)
      - [A vlanCfiOuter ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.vlanCfiOuter)
      - [M GetVlanVidOuter ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.GetVlanVidOuter)
      - [M SetVlanVidOuter ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.SetVlanVidOuter)
      - [A vlanVidOuter ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.vlanVidOuter)
      - [M GetEthPayload ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.GetEthPayload)
      - [M SetEthPayload ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.SetEthPayload)
      - [A ethPayload ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.ethPayload)
      - [M GetMacSecTciAn ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.GetMacSecTciAn)
      - [A macSecTciAn ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.macSecTciAn)
      - [M GetMacSecTci ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.GetMacSecTci)
      - [A macSecTci ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.macSecTci)
      - [M GetMacSecTciV ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.GetMacSecTciV)
      - [A macSecTciV ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.macSecTciV)
      - [M GetMacSecTciEs ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.GetMacSecTciEs)
      - [A macSecTciEs ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.macSecTciEs)
      - [M GetMacSecTciSc ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.GetMacSecTciSc)
      - [A macSecTciSc ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.macSecTciSc)
      - [M GetMacSecTciScb ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.GetMacSecTciScb)
      - [A macSecTciScb ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.macSecTciScb)
      - [M GetMacSecTciE ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.GetMacSecTciE)
      - [A macSecTciE ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.macSecTciE)
      - [M GetMacSecTciC ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.GetMacSecTciC)
      - [A macSecTciC ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.macSecTciC)
      - [M GetMacSecAn ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.GetMacSecAn)
      - [A macSecAn ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.macSecAn)
      - [M GetMacSecSl ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.GetMacSecSl)
      - [A macSecSl ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.macSecSl)
      - [M GetMacSecPn ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.GetMacSecPn)
      - [A macSecPn ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.macSecPn)
      - [M GetMacSecSci ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.GetMacSecSci)
      - [A macSecSci ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.macSecSci)
      - [M GetMacSecIcv ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.GetMacSecIcv)
      - [A macSecIcv ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.macSecIcv)
      - [M FindParent ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.FindParent)
      - [M GetTimestamp ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.GetTimestamp)
      - [M SetTimestamp ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.SetTimestamp)
      - [A parent ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.parent)
      - [A timestamp ](#tts.lib.ethernet.PacketEthernet.PacketEthernet.timestamp)
  - [ PacketIp4 ](#packetip4)
    - [C PacketIp4 ](#tts.lib.ethernet.PacketIp4.PacketIp4)
      - [M GetIpVersionAndHeaderLength ](#tts.lib.ethernet.PacketIp4.PacketIp4.GetIpVersionAndHeaderLength)
      - [M SetIpVersionAndHeaderLength ](#tts.lib.ethernet.PacketIp4.PacketIp4.SetIpVersionAndHeaderLength)
      - [A ipVersionHeader ](#tts.lib.ethernet.PacketIp4.PacketIp4.ipVersionHeader)
      - [M GetIpTos ](#tts.lib.ethernet.PacketIp4.PacketIp4.GetIpTos)
      - [M SetIpTos ](#tts.lib.ethernet.PacketIp4.PacketIp4.SetIpTos)
      - [A ipTos ](#tts.lib.ethernet.PacketIp4.PacketIp4.ipTos)
      - [M GetIpLen ](#tts.lib.ethernet.PacketIp4.PacketIp4.GetIpLen)
      - [M SetIpLen ](#tts.lib.ethernet.PacketIp4.PacketIp4.SetIpLen)
      - [A ipLen ](#tts.lib.ethernet.PacketIp4.PacketIp4.ipLen)
      - [M GetIpIdent ](#tts.lib.ethernet.PacketIp4.PacketIp4.GetIpIdent)
      - [M SetIpIdent ](#tts.lib.ethernet.PacketIp4.PacketIp4.SetIpIdent)
      - [A ipIdent ](#tts.lib.ethernet.PacketIp4.PacketIp4.ipIdent)
      - [M GetIpOffset ](#tts.lib.ethernet.PacketIp4.PacketIp4.GetIpOffset)
      - [M SetIpOffset ](#tts.lib.ethernet.PacketIp4.PacketIp4.SetIpOffset)
      - [A ipOffset ](#tts.lib.ethernet.PacketIp4.PacketIp4.ipOffset)
      - [M GetIpTtl ](#tts.lib.ethernet.PacketIp4.PacketIp4.GetIpTtl)
      - [M SetIpTtl ](#tts.lib.ethernet.PacketIp4.PacketIp4.SetIpTtl)
      - [A ipTtl ](#tts.lib.ethernet.PacketIp4.PacketIp4.ipTtl)
      - [M GetIpProt ](#tts.lib.ethernet.PacketIp4.PacketIp4.GetIpProt)
      - [M SetIpProt ](#tts.lib.ethernet.PacketIp4.PacketIp4.SetIpProt)
      - [A ipProt ](#tts.lib.ethernet.PacketIp4.PacketIp4.ipProt)
      - [M GetIpChecksum ](#tts.lib.ethernet.PacketIp4.PacketIp4.GetIpChecksum)
      - [M SetIpChecksum ](#tts.lib.ethernet.PacketIp4.PacketIp4.SetIpChecksum)
      - [A ipChecksum ](#tts.lib.ethernet.PacketIp4.PacketIp4.ipChecksum)
      - [M GetIpSrc ](#tts.lib.ethernet.PacketIp4.PacketIp4.GetIpSrc)
      - [M SetIpSrc ](#tts.lib.ethernet.PacketIp4.PacketIp4.SetIpSrc)
      - [A ipSrc ](#tts.lib.ethernet.PacketIp4.PacketIp4.ipSrc)
      - [M GetIpDst ](#tts.lib.ethernet.PacketIp4.PacketIp4.GetIpDst)
      - [M SetIpDst ](#tts.lib.ethernet.PacketIp4.PacketIp4.SetIpDst)
      - [A ipDst ](#tts.lib.ethernet.PacketIp4.PacketIp4.ipDst)
      - [M GetIpPayload ](#tts.lib.ethernet.PacketIp4.PacketIp4.GetIpPayload)
      - [M SetIpPayload ](#tts.lib.ethernet.PacketIp4.PacketIp4.SetIpPayload)
      - [A ipPayload ](#tts.lib.ethernet.PacketIp4.PacketIp4.ipPayload)
      - [M GetIpAhSpi ](#tts.lib.ethernet.PacketIp4.PacketIp4.GetIpAhSpi)
      - [A ipAhSpi ](#tts.lib.ethernet.PacketIp4.PacketIp4.ipAhSpi)
      - [M GetIpAhSeq ](#tts.lib.ethernet.PacketIp4.PacketIp4.GetIpAhSeq)
      - [A ipAhSeq ](#tts.lib.ethernet.PacketIp4.PacketIp4.ipAhSeq)
      - [M GetIpAhIcv ](#tts.lib.ethernet.PacketIp4.PacketIp4.GetIpAhIcv)
      - [A ipAhIcv ](#tts.lib.ethernet.PacketIp4.PacketIp4.ipAhIcv)
      - [M GetIpAhNxt ](#tts.lib.ethernet.PacketIp4.PacketIp4.GetIpAhNxt)
      - [A ipAhNxt ](#tts.lib.ethernet.PacketIp4.PacketIp4.ipAhNxt)
      - [M GetIpAhLen ](#tts.lib.ethernet.PacketIp4.PacketIp4.GetIpAhLen)
      - [A ipAhLen ](#tts.lib.ethernet.PacketIp4.PacketIp4.ipAhLen)
      - [M GetIpAhRsvd ](#tts.lib.ethernet.PacketIp4.PacketIp4.GetIpAhRsvd)
      - [A ipAhRsvd ](#tts.lib.ethernet.PacketIp4.PacketIp4.ipAhRsvd)
      - [M CalcIpLen ](#tts.lib.ethernet.PacketIp4.PacketIp4.CalcIpLen)
      - [M FindParent ](#tts.lib.ethernet.PacketIp4.PacketIp4.FindParent)
      - [M GetEthDstMac ](#tts.lib.ethernet.PacketIp4.PacketIp4.GetEthDstMac)
      - [M GetEthPayload ](#tts.lib.ethernet.PacketIp4.PacketIp4.GetEthPayload)
      - [M GetEthSrcMac ](#tts.lib.ethernet.PacketIp4.PacketIp4.GetEthSrcMac)
      - [M GetEthType ](#tts.lib.ethernet.PacketIp4.PacketIp4.GetEthType)
      - [M GetMacSecAn ](#tts.lib.ethernet.PacketIp4.PacketIp4.GetMacSecAn)
      - [M GetMacSecIcv ](#tts.lib.ethernet.PacketIp4.PacketIp4.GetMacSecIcv)
      - [M GetMacSecPn ](#tts.lib.ethernet.PacketIp4.PacketIp4.GetMacSecPn)
      - [M GetMacSecSci ](#tts.lib.ethernet.PacketIp4.PacketIp4.GetMacSecSci)
      - [M GetMacSecSl ](#tts.lib.ethernet.PacketIp4.PacketIp4.GetMacSecSl)
      - [M GetMacSecTci ](#tts.lib.ethernet.PacketIp4.PacketIp4.GetMacSecTci)
      - [M GetMacSecTciAn ](#tts.lib.ethernet.PacketIp4.PacketIp4.GetMacSecTciAn)
      - [M GetMacSecTciC ](#tts.lib.ethernet.PacketIp4.PacketIp4.GetMacSecTciC)
      - [M GetMacSecTciE ](#tts.lib.ethernet.PacketIp4.PacketIp4.GetMacSecTciE)
      - [M GetMacSecTciEs ](#tts.lib.ethernet.PacketIp4.PacketIp4.GetMacSecTciEs)
      - [M GetMacSecTciSc ](#tts.lib.ethernet.PacketIp4.PacketIp4.GetMacSecTciSc)
      - [M GetMacSecTciScb ](#tts.lib.ethernet.PacketIp4.PacketIp4.GetMacSecTciScb)
      - [M GetMacSecTciV ](#tts.lib.ethernet.PacketIp4.PacketIp4.GetMacSecTciV)
      - [M GetTimestamp ](#tts.lib.ethernet.PacketIp4.PacketIp4.GetTimestamp)
      - [M GetVlanCfi ](#tts.lib.ethernet.PacketIp4.PacketIp4.GetVlanCfi)
      - [M GetVlanCfiOuter ](#tts.lib.ethernet.PacketIp4.PacketIp4.GetVlanCfiOuter)
      - [M GetVlanPcp ](#tts.lib.ethernet.PacketIp4.PacketIp4.GetVlanPcp)
      - [M GetVlanPcpOuter ](#tts.lib.ethernet.PacketIp4.PacketIp4.GetVlanPcpOuter)
      - [M GetVlanVid ](#tts.lib.ethernet.PacketIp4.PacketIp4.GetVlanVid)
      - [M GetVlanVidOuter ](#tts.lib.ethernet.PacketIp4.PacketIp4.GetVlanVidOuter)
      - [M SetEthDstMac ](#tts.lib.ethernet.PacketIp4.PacketIp4.SetEthDstMac)
      - [M SetEthPayload ](#tts.lib.ethernet.PacketIp4.PacketIp4.SetEthPayload)
      - [M SetEthSrcMac ](#tts.lib.ethernet.PacketIp4.PacketIp4.SetEthSrcMac)
      - [M SetEthType ](#tts.lib.ethernet.PacketIp4.PacketIp4.SetEthType)
      - [M SetTimestamp ](#tts.lib.ethernet.PacketIp4.PacketIp4.SetTimestamp)
      - [M SetVlanCfi ](#tts.lib.ethernet.PacketIp4.PacketIp4.SetVlanCfi)
      - [M SetVlanCfiOuter ](#tts.lib.ethernet.PacketIp4.PacketIp4.SetVlanCfiOuter)
      - [M SetVlanPcp ](#tts.lib.ethernet.PacketIp4.PacketIp4.SetVlanPcp)
      - [M SetVlanPcpOuter ](#tts.lib.ethernet.PacketIp4.PacketIp4.SetVlanPcpOuter)
      - [M SetVlanVid ](#tts.lib.ethernet.PacketIp4.PacketIp4.SetVlanVid)
      - [M SetVlanVidOuter ](#tts.lib.ethernet.PacketIp4.PacketIp4.SetVlanVidOuter)
      - [A ethDstMac ](#tts.lib.ethernet.PacketIp4.PacketIp4.ethDstMac)
      - [A ethPayload ](#tts.lib.ethernet.PacketIp4.PacketIp4.ethPayload)
      - [A ethSrcMac ](#tts.lib.ethernet.PacketIp4.PacketIp4.ethSrcMac)
      - [A ethType ](#tts.lib.ethernet.PacketIp4.PacketIp4.ethType)
      - [A macSecAn ](#tts.lib.ethernet.PacketIp4.PacketIp4.macSecAn)
      - [A macSecIcv ](#tts.lib.ethernet.PacketIp4.PacketIp4.macSecIcv)
      - [A macSecPn ](#tts.lib.ethernet.PacketIp4.PacketIp4.macSecPn)
      - [A macSecSci ](#tts.lib.ethernet.PacketIp4.PacketIp4.macSecSci)
      - [A macSecSl ](#tts.lib.ethernet.PacketIp4.PacketIp4.macSecSl)
      - [A macSecTci ](#tts.lib.ethernet.PacketIp4.PacketIp4.macSecTci)
      - [A macSecTciAn ](#tts.lib.ethernet.PacketIp4.PacketIp4.macSecTciAn)
      - [A macSecTciC ](#tts.lib.ethernet.PacketIp4.PacketIp4.macSecTciC)
      - [A macSecTciE ](#tts.lib.ethernet.PacketIp4.PacketIp4.macSecTciE)
      - [A macSecTciEs ](#tts.lib.ethernet.PacketIp4.PacketIp4.macSecTciEs)
      - [A macSecTciSc ](#tts.lib.ethernet.PacketIp4.PacketIp4.macSecTciSc)
      - [A macSecTciScb ](#tts.lib.ethernet.PacketIp4.PacketIp4.macSecTciScb)
      - [A macSecTciV ](#tts.lib.ethernet.PacketIp4.PacketIp4.macSecTciV)
      - [A parent ](#tts.lib.ethernet.PacketIp4.PacketIp4.parent)
      - [A timestamp ](#tts.lib.ethernet.PacketIp4.PacketIp4.timestamp)
      - [A vlanCfi ](#tts.lib.ethernet.PacketIp4.PacketIp4.vlanCfi)
      - [A vlanCfiOuter ](#tts.lib.ethernet.PacketIp4.PacketIp4.vlanCfiOuter)
      - [A vlanPcp ](#tts.lib.ethernet.PacketIp4.PacketIp4.vlanPcp)
      - [A vlanPcpOuter ](#tts.lib.ethernet.PacketIp4.PacketIp4.vlanPcpOuter)
      - [A vlanVid ](#tts.lib.ethernet.PacketIp4.PacketIp4.vlanVid)
      - [A vlanVidOuter ](#tts.lib.ethernet.PacketIp4.PacketIp4.vlanVidOuter)
  - [ PacketIp6 ](#packetip6)
    - [C PacketIp6 ](#tts.lib.ethernet.PacketIp6.PacketIp6)
      - [M GetIpProt ](#tts.lib.ethernet.PacketIp6.PacketIp6.GetIpProt)
      - [M SetIpProt ](#tts.lib.ethernet.PacketIp6.PacketIp6.SetIpProt)
      - [A ipProt ](#tts.lib.ethernet.PacketIp6.PacketIp6.ipProt)
      - [M GetIpHopLimit ](#tts.lib.ethernet.PacketIp6.PacketIp6.GetIpHopLimit)
      - [M SetIpHopLimit ](#tts.lib.ethernet.PacketIp6.PacketIp6.SetIpHopLimit)
      - [A ipHopLimit ](#tts.lib.ethernet.PacketIp6.PacketIp6.ipHopLimit)
      - [M GetIpSrc ](#tts.lib.ethernet.PacketIp6.PacketIp6.GetIpSrc)
      - [M SetIpSrc ](#tts.lib.ethernet.PacketIp6.PacketIp6.SetIpSrc)
      - [A ipSrc ](#tts.lib.ethernet.PacketIp6.PacketIp6.ipSrc)
      - [M GetIpDst ](#tts.lib.ethernet.PacketIp6.PacketIp6.GetIpDst)
      - [M SetIpDst ](#tts.lib.ethernet.PacketIp6.PacketIp6.SetIpDst)
      - [A ipDst ](#tts.lib.ethernet.PacketIp6.PacketIp6.ipDst)
      - [M GetIpPayload ](#tts.lib.ethernet.PacketIp6.PacketIp6.GetIpPayload)
      - [M SetIpPayload ](#tts.lib.ethernet.PacketIp6.PacketIp6.SetIpPayload)
      - [A ipPayload ](#tts.lib.ethernet.PacketIp6.PacketIp6.ipPayload)
      - [M GetIpLen ](#tts.lib.ethernet.PacketIp6.PacketIp6.GetIpLen)
      - [A ipLen ](#tts.lib.ethernet.PacketIp6.PacketIp6.ipLen)
      - [M GetIpTrafficClass ](#tts.lib.ethernet.PacketIp6.PacketIp6.GetIpTrafficClass)
      - [A ipTrafficClass ](#tts.lib.ethernet.PacketIp6.PacketIp6.ipTrafficClass)
      - [M GetIpFlowLabel ](#tts.lib.ethernet.PacketIp6.PacketIp6.GetIpFlowLabel)
      - [A ipFlowLabel ](#tts.lib.ethernet.PacketIp6.PacketIp6.ipFlowLabel)
      - [M CalcIpLen ](#tts.lib.ethernet.PacketIp6.PacketIp6.CalcIpLen)
      - [M FindParent ](#tts.lib.ethernet.PacketIp6.PacketIp6.FindParent)
      - [M GetEthDstMac ](#tts.lib.ethernet.PacketIp6.PacketIp6.GetEthDstMac)
      - [M GetEthPayload ](#tts.lib.ethernet.PacketIp6.PacketIp6.GetEthPayload)
      - [M GetEthSrcMac ](#tts.lib.ethernet.PacketIp6.PacketIp6.GetEthSrcMac)
      - [M GetEthType ](#tts.lib.ethernet.PacketIp6.PacketIp6.GetEthType)
      - [M GetMacSecAn ](#tts.lib.ethernet.PacketIp6.PacketIp6.GetMacSecAn)
      - [M GetMacSecIcv ](#tts.lib.ethernet.PacketIp6.PacketIp6.GetMacSecIcv)
      - [M GetMacSecPn ](#tts.lib.ethernet.PacketIp6.PacketIp6.GetMacSecPn)
      - [M GetMacSecSci ](#tts.lib.ethernet.PacketIp6.PacketIp6.GetMacSecSci)
      - [M GetMacSecSl ](#tts.lib.ethernet.PacketIp6.PacketIp6.GetMacSecSl)
      - [M GetMacSecTci ](#tts.lib.ethernet.PacketIp6.PacketIp6.GetMacSecTci)
      - [M GetMacSecTciAn ](#tts.lib.ethernet.PacketIp6.PacketIp6.GetMacSecTciAn)
      - [M GetMacSecTciC ](#tts.lib.ethernet.PacketIp6.PacketIp6.GetMacSecTciC)
      - [M GetMacSecTciE ](#tts.lib.ethernet.PacketIp6.PacketIp6.GetMacSecTciE)
      - [M GetMacSecTciEs ](#tts.lib.ethernet.PacketIp6.PacketIp6.GetMacSecTciEs)
      - [M GetMacSecTciSc ](#tts.lib.ethernet.PacketIp6.PacketIp6.GetMacSecTciSc)
      - [M GetMacSecTciScb ](#tts.lib.ethernet.PacketIp6.PacketIp6.GetMacSecTciScb)
      - [M GetMacSecTciV ](#tts.lib.ethernet.PacketIp6.PacketIp6.GetMacSecTciV)
      - [M GetTimestamp ](#tts.lib.ethernet.PacketIp6.PacketIp6.GetTimestamp)
      - [M GetVlanCfi ](#tts.lib.ethernet.PacketIp6.PacketIp6.GetVlanCfi)
      - [M GetVlanCfiOuter ](#tts.lib.ethernet.PacketIp6.PacketIp6.GetVlanCfiOuter)
      - [M GetVlanPcp ](#tts.lib.ethernet.PacketIp6.PacketIp6.GetVlanPcp)
      - [M GetVlanPcpOuter ](#tts.lib.ethernet.PacketIp6.PacketIp6.GetVlanPcpOuter)
      - [M GetVlanVid ](#tts.lib.ethernet.PacketIp6.PacketIp6.GetVlanVid)
      - [M GetVlanVidOuter ](#tts.lib.ethernet.PacketIp6.PacketIp6.GetVlanVidOuter)
      - [M SetEthDstMac ](#tts.lib.ethernet.PacketIp6.PacketIp6.SetEthDstMac)
      - [M SetEthPayload ](#tts.lib.ethernet.PacketIp6.PacketIp6.SetEthPayload)
      - [M SetEthSrcMac ](#tts.lib.ethernet.PacketIp6.PacketIp6.SetEthSrcMac)
      - [M SetEthType ](#tts.lib.ethernet.PacketIp6.PacketIp6.SetEthType)
      - [M SetTimestamp ](#tts.lib.ethernet.PacketIp6.PacketIp6.SetTimestamp)
      - [M SetVlanCfi ](#tts.lib.ethernet.PacketIp6.PacketIp6.SetVlanCfi)
      - [M SetVlanCfiOuter ](#tts.lib.ethernet.PacketIp6.PacketIp6.SetVlanCfiOuter)
      - [M SetVlanPcp ](#tts.lib.ethernet.PacketIp6.PacketIp6.SetVlanPcp)
      - [M SetVlanPcpOuter ](#tts.lib.ethernet.PacketIp6.PacketIp6.SetVlanPcpOuter)
      - [M SetVlanVid ](#tts.lib.ethernet.PacketIp6.PacketIp6.SetVlanVid)
      - [M SetVlanVidOuter ](#tts.lib.ethernet.PacketIp6.PacketIp6.SetVlanVidOuter)
      - [A ethDstMac ](#tts.lib.ethernet.PacketIp6.PacketIp6.ethDstMac)
      - [A ethPayload ](#tts.lib.ethernet.PacketIp6.PacketIp6.ethPayload)
      - [A ethSrcMac ](#tts.lib.ethernet.PacketIp6.PacketIp6.ethSrcMac)
      - [A ethType ](#tts.lib.ethernet.PacketIp6.PacketIp6.ethType)
      - [A macSecAn ](#tts.lib.ethernet.PacketIp6.PacketIp6.macSecAn)
      - [A macSecIcv ](#tts.lib.ethernet.PacketIp6.PacketIp6.macSecIcv)
      - [A macSecPn ](#tts.lib.ethernet.PacketIp6.PacketIp6.macSecPn)
      - [A macSecSci ](#tts.lib.ethernet.PacketIp6.PacketIp6.macSecSci)
      - [A macSecSl ](#tts.lib.ethernet.PacketIp6.PacketIp6.macSecSl)
      - [A macSecTci ](#tts.lib.ethernet.PacketIp6.PacketIp6.macSecTci)
      - [A macSecTciAn ](#tts.lib.ethernet.PacketIp6.PacketIp6.macSecTciAn)
      - [A macSecTciC ](#tts.lib.ethernet.PacketIp6.PacketIp6.macSecTciC)
      - [A macSecTciE ](#tts.lib.ethernet.PacketIp6.PacketIp6.macSecTciE)
      - [A macSecTciEs ](#tts.lib.ethernet.PacketIp6.PacketIp6.macSecTciEs)
      - [A macSecTciSc ](#tts.lib.ethernet.PacketIp6.PacketIp6.macSecTciSc)
      - [A macSecTciScb ](#tts.lib.ethernet.PacketIp6.PacketIp6.macSecTciScb)
      - [A macSecTciV ](#tts.lib.ethernet.PacketIp6.PacketIp6.macSecTciV)
      - [A parent ](#tts.lib.ethernet.PacketIp6.PacketIp6.parent)
      - [A timestamp ](#tts.lib.ethernet.PacketIp6.PacketIp6.timestamp)
      - [A vlanCfi ](#tts.lib.ethernet.PacketIp6.PacketIp6.vlanCfi)
      - [A vlanCfiOuter ](#tts.lib.ethernet.PacketIp6.PacketIp6.vlanCfiOuter)
      - [A vlanPcp ](#tts.lib.ethernet.PacketIp6.PacketIp6.vlanPcp)
      - [A vlanPcpOuter ](#tts.lib.ethernet.PacketIp6.PacketIp6.vlanPcpOuter)
      - [A vlanVid ](#tts.lib.ethernet.PacketIp6.PacketIp6.vlanVid)
      - [A vlanVidOuter ](#tts.lib.ethernet.PacketIp6.PacketIp6.vlanVidOuter)
  - [ PacketIcmp ](#packeticmp)
    - [C PacketIcmp ](#tts.lib.ethernet.PacketIcmp.PacketIcmp)
      - [M GetIcmpType ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetIcmpType)
      - [M SetIcmpType ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetIcmpType)
      - [A icmpType ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.icmpType)
      - [M GetIcmpCode ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetIcmpCode)
      - [M SetIcmpCode ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetIcmpCode)
      - [A icmpCode ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.icmpCode)
      - [M GetIcmpChecksum ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetIcmpChecksum)
      - [M SetIcmpChecksum ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetIcmpChecksum)
      - [A icmpChecksum ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.icmpChecksum)
      - [M GetIcmpPayload ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetIcmpPayload)
      - [M CalcIpLen ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.CalcIpLen)
      - [M FindParent ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.FindParent)
      - [M GetEthDstMac ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetEthDstMac)
      - [M GetEthPayload ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetEthPayload)
      - [M GetEthSrcMac ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetEthSrcMac)
      - [M GetEthType ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetEthType)
      - [M GetIpAhIcv ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetIpAhIcv)
      - [M GetIpAhLen ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetIpAhLen)
      - [M GetIpAhNxt ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetIpAhNxt)
      - [M GetIpAhRsvd ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetIpAhRsvd)
      - [M GetIpAhSeq ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetIpAhSeq)
      - [M GetIpAhSpi ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetIpAhSpi)
      - [M GetIpChecksum ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetIpChecksum)
      - [M GetIpDst ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetIpDst)
      - [M GetIpIdent ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetIpIdent)
      - [M GetIpLen ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetIpLen)
      - [M GetIpOffset ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetIpOffset)
      - [M GetIpPayload ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetIpPayload)
      - [M GetIpProt ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetIpProt)
      - [M GetIpSrc ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetIpSrc)
      - [M GetIpTos ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetIpTos)
      - [M GetIpTtl ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetIpTtl)
      - [M GetIpVersionAndHeaderLength ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetIpVersionAndHeaderLength)
      - [M GetMacSecAn ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetMacSecAn)
      - [M GetMacSecIcv ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetMacSecIcv)
      - [M GetMacSecPn ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetMacSecPn)
      - [M GetMacSecSci ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetMacSecSci)
      - [M GetMacSecSl ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetMacSecSl)
      - [M GetMacSecTci ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetMacSecTci)
      - [M GetMacSecTciAn ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetMacSecTciAn)
      - [M GetMacSecTciC ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetMacSecTciC)
      - [M GetMacSecTciE ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetMacSecTciE)
      - [M GetMacSecTciEs ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetMacSecTciEs)
      - [M GetMacSecTciSc ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetMacSecTciSc)
      - [M GetMacSecTciScb ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetMacSecTciScb)
      - [M GetMacSecTciV ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetMacSecTciV)
      - [M GetTimestamp ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetTimestamp)
      - [M GetVlanCfi ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetVlanCfi)
      - [M GetVlanCfiOuter ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetVlanCfiOuter)
      - [M GetVlanPcp ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetVlanPcp)
      - [M GetVlanPcpOuter ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetVlanPcpOuter)
      - [M GetVlanVid ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetVlanVid)
      - [M GetVlanVidOuter ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetVlanVidOuter)
      - [A PK_CLASS ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.PK_CLASS)
      - [M SetEthDstMac ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetEthDstMac)
      - [M SetEthPayload ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetEthPayload)
      - [M SetEthSrcMac ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetEthSrcMac)
      - [M SetEthType ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetEthType)
      - [M SetIcmpPayload ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetIcmpPayload)
      - [M SetIpChecksum ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetIpChecksum)
      - [M SetIpDst ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetIpDst)
      - [M SetIpIdent ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetIpIdent)
      - [M SetIpLen ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetIpLen)
      - [M SetIpOffset ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetIpOffset)
      - [M SetIpPayload ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetIpPayload)
      - [M SetIpProt ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetIpProt)
      - [M SetIpSrc ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetIpSrc)
      - [M SetIpTos ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetIpTos)
      - [M SetIpTtl ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetIpTtl)
      - [M SetIpVersionAndHeaderLength ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetIpVersionAndHeaderLength)
      - [M SetTimestamp ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetTimestamp)
      - [M SetVlanCfi ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetVlanCfi)
      - [M SetVlanCfiOuter ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetVlanCfiOuter)
      - [M SetVlanPcp ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetVlanPcp)
      - [M SetVlanPcpOuter ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetVlanPcpOuter)
      - [M SetVlanVid ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetVlanVid)
      - [M SetVlanVidOuter ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetVlanVidOuter)
      - [A ethDstMac ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.ethDstMac)
      - [A ethPayload ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.ethPayload)
      - [A ethSrcMac ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.ethSrcMac)
      - [A ethType ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.ethType)
      - [A ipAhIcv ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.ipAhIcv)
      - [A ipAhLen ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.ipAhLen)
      - [A ipAhNxt ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.ipAhNxt)
      - [A ipAhRsvd ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.ipAhRsvd)
      - [A ipAhSeq ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.ipAhSeq)
      - [A ipAhSpi ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.ipAhSpi)
      - [A ipChecksum ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.ipChecksum)
      - [A ipDst ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.ipDst)
      - [A ipIdent ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.ipIdent)
      - [A ipLen ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.ipLen)
      - [A ipOffset ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.ipOffset)
      - [A ipPayload ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.ipPayload)
      - [A ipProt ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.ipProt)
      - [A ipSrc ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.ipSrc)
      - [A ipTos ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.ipTos)
      - [A ipTtl ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.ipTtl)
      - [A ipVersionHeader ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.ipVersionHeader)
      - [A macSecAn ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.macSecAn)
      - [A macSecIcv ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.macSecIcv)
      - [A macSecPn ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.macSecPn)
      - [A macSecSci ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.macSecSci)
      - [A macSecSl ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.macSecSl)
      - [A macSecTci ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.macSecTci)
      - [A macSecTciAn ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.macSecTciAn)
      - [A macSecTciC ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.macSecTciC)
      - [A macSecTciE ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.macSecTciE)
      - [A macSecTciEs ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.macSecTciEs)
      - [A macSecTciSc ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.macSecTciSc)
      - [A macSecTciScb ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.macSecTciScb)
      - [A macSecTciV ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.macSecTciV)
      - [A parent ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.parent)
      - [A timestamp ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.timestamp)
      - [A vlanCfi ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.vlanCfi)
      - [A vlanCfiOuter ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.vlanCfiOuter)
      - [A vlanPcp ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.vlanPcp)
      - [A vlanPcpOuter ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.vlanPcpOuter)
      - [A vlanVid ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.vlanVid)
      - [A vlanVidOuter ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.vlanVidOuter)
      - [A icmpPayload ](#tts.lib.ethernet.PacketIcmp.PacketIcmp.icmpPayload)
  - [ PacketMka ](#packetmka)
    - [C PacketMka ](#tts.lib.ethernet.PacketMka.PacketMka)
      - [M UseCak ](#tts.lib.ethernet.PacketMka.PacketMka.UseCak)
      - [M GetEthDstMac ](#tts.lib.ethernet.PacketMka.PacketMka.GetEthDstMac)
      - [M SetEthDstMac ](#tts.lib.ethernet.PacketMka.PacketMka.SetEthDstMac)
      - [A ethDstMac ](#tts.lib.ethernet.PacketMka.PacketMka.ethDstMac)
      - [M GetEthSrcMac ](#tts.lib.ethernet.PacketMka.PacketMka.GetEthSrcMac)
      - [M SetEthSrcMac ](#tts.lib.ethernet.PacketMka.PacketMka.SetEthSrcMac)
      - [A ethSrcMac ](#tts.lib.ethernet.PacketMka.PacketMka.ethSrcMac)
      - [M GetEthType ](#tts.lib.ethernet.PacketMka.PacketMka.GetEthType)
      - [M SetEthType ](#tts.lib.ethernet.PacketMka.PacketMka.SetEthType)
      - [M GetEthPayload ](#tts.lib.ethernet.PacketMka.PacketMka.GetEthPayload)
      - [M SetEthPayload ](#tts.lib.ethernet.PacketMka.PacketMka.SetEthPayload)
      - [M GetMkaIcv ](#tts.lib.ethernet.PacketMka.PacketMka.GetMkaIcv)
      - [A mkaIcv ](#tts.lib.ethernet.PacketMka.PacketMka.mkaIcv)
      - [M IsMkaIcvValid ](#tts.lib.ethernet.PacketMka.PacketMka.IsMkaIcvValid)
      - [M GetKeyServerPriority ](#tts.lib.ethernet.PacketMka.PacketMka.GetKeyServerPriority)
      - [A keyServerPriority ](#tts.lib.ethernet.PacketMka.PacketMka.keyServerPriority)
      - [M GetKeyServerFlag ](#tts.lib.ethernet.PacketMka.PacketMka.GetKeyServerFlag)
      - [A keyServerFlag ](#tts.lib.ethernet.PacketMka.PacketMka.keyServerFlag)
      - [M GetMacSecDesired ](#tts.lib.ethernet.PacketMka.PacketMka.GetMacSecDesired)
      - [A macSecDesired ](#tts.lib.ethernet.PacketMka.PacketMka.macSecDesired)
      - [M GetMacSecCapability ](#tts.lib.ethernet.PacketMka.PacketMka.GetMacSecCapability)
      - [A macSecCapability ](#tts.lib.ethernet.PacketMka.PacketMka.macSecCapability)
      - [M GetMacSecSci ](#tts.lib.ethernet.PacketMka.PacketMka.GetMacSecSci)
      - [A macSecSci ](#tts.lib.ethernet.PacketMka.PacketMka.macSecSci)
      - [M GetMemberIdentifier ](#tts.lib.ethernet.PacketMka.PacketMka.GetMemberIdentifier)
      - [A memberIdentifier ](#tts.lib.ethernet.PacketMka.PacketMka.memberIdentifier)
      - [M GetMessageNumber ](#tts.lib.ethernet.PacketMka.PacketMka.GetMessageNumber)
      - [A messageNumber ](#tts.lib.ethernet.PacketMka.PacketMka.messageNumber)
      - [M GetCakName ](#tts.lib.ethernet.PacketMka.PacketMka.GetCakName)
      - [A cakName ](#tts.lib.ethernet.PacketMka.PacketMka.cakName)
      - [M GetLivePeerListMemberIdentifiers ](#tts.lib.ethernet.PacketMka.PacketMka.GetLivePeerListMemberIdentifiers)
      - [A livePeerListMemberIdentifiers ](#tts.lib.ethernet.PacketMka.PacketMka.livePeerListMemberIdentifiers)
      - [M GetLivePeerListMessageNumbers ](#tts.lib.ethernet.PacketMka.PacketMka.GetLivePeerListMessageNumbers)
      - [A livePeerListMessageNumbers ](#tts.lib.ethernet.PacketMka.PacketMka.livePeerListMessageNumbers)
      - [M GetLivePeerListKeyServerSsci ](#tts.lib.ethernet.PacketMka.PacketMka.GetLivePeerListKeyServerSsci)
      - [A livePeerListKeyServerSsci ](#tts.lib.ethernet.PacketMka.PacketMka.livePeerListKeyServerSsci)
      - [M RemoveLivePeerList ](#tts.lib.ethernet.PacketMka.PacketMka.RemoveLivePeerList)
      - [M GetPotentialPeerListMemberIdentifiers ](#tts.lib.ethernet.PacketMka.PacketMka.GetPotentialPeerListMemberIdentifiers)
      - [A potentialPeerListMemberIdentifiers ](#tts.lib.ethernet.PacketMka.PacketMka.potentialPeerListMemberIdentifiers)
      - [M GetPotentialPeerListMessageNumbers ](#tts.lib.ethernet.PacketMka.PacketMka.GetPotentialPeerListMessageNumbers)
      - [A potentialPeerListMessageNumbers ](#tts.lib.ethernet.PacketMka.PacketMka.potentialPeerListMessageNumbers)
      - [M RemovePotentialPeerList ](#tts.lib.ethernet.PacketMka.PacketMka.RemovePotentialPeerList)
      - [M GetSakUseLatestAn ](#tts.lib.ethernet.PacketMka.PacketMka.GetSakUseLatestAn)
      - [A sakUseLatestAn ](#tts.lib.ethernet.PacketMka.PacketMka.sakUseLatestAn)
      - [M GetSakUseLatestTx ](#tts.lib.ethernet.PacketMka.PacketMka.GetSakUseLatestTx)
      - [A sakUseLatestTx ](#tts.lib.ethernet.PacketMka.PacketMka.sakUseLatestTx)
      - [M GetSakUseLatestRx ](#tts.lib.ethernet.PacketMka.PacketMka.GetSakUseLatestRx)
      - [A sakUseLatestRx ](#tts.lib.ethernet.PacketMka.PacketMka.sakUseLatestRx)
      - [M GetSakUsePlainTx ](#tts.lib.ethernet.PacketMka.PacketMka.GetSakUsePlainTx)
      - [A sakUsePlainTx ](#tts.lib.ethernet.PacketMka.PacketMka.sakUsePlainTx)
      - [M GetSakUsePlainRx ](#tts.lib.ethernet.PacketMka.PacketMka.GetSakUsePlainRx)
      - [A sakUsePlainRx ](#tts.lib.ethernet.PacketMka.PacketMka.sakUsePlainRx)
      - [M GetSakUseDelayProtect ](#tts.lib.ethernet.PacketMka.PacketMka.GetSakUseDelayProtect)
      - [A sakUseDelayProtect ](#tts.lib.ethernet.PacketMka.PacketMka.sakUseDelayProtect)
      - [M GetSakUseLatestKeyServerMemberIdentifier ](#tts.lib.ethernet.PacketMka.PacketMka.GetSakUseLatestKeyServerMemberIdentifier)
      - [A sakUseLatestKeyServerMemberIdentifier ](#tts.lib.ethernet.PacketMka.PacketMka.sakUseLatestKeyServerMemberIdentifier)
      - [M GetSakUseLatestKeyNumber ](#tts.lib.ethernet.PacketMka.PacketMka.GetSakUseLatestKeyNumber)
      - [A sakUseLatestKeyNumber ](#tts.lib.ethernet.PacketMka.PacketMka.sakUseLatestKeyNumber)
      - [M GetSakUseLatestLpn ](#tts.lib.ethernet.PacketMka.PacketMka.GetSakUseLatestLpn)
      - [A sakUseLatestLpn ](#tts.lib.ethernet.PacketMka.PacketMka.sakUseLatestLpn)
      - [M RemoveSakUse ](#tts.lib.ethernet.PacketMka.PacketMka.RemoveSakUse)
      - [M GetDistributedSakWrappedKey ](#tts.lib.ethernet.PacketMka.PacketMka.GetDistributedSakWrappedKey)
      - [A distributedSakWrappedKey ](#tts.lib.ethernet.PacketMka.PacketMka.distributedSakWrappedKey)
      - [M GetDistributedSakUnwrappedKey ](#tts.lib.ethernet.PacketMka.PacketMka.GetDistributedSakUnwrappedKey)
      - [A distributedSakUnwrappedKey ](#tts.lib.ethernet.PacketMka.PacketMka.distributedSakUnwrappedKey)
      - [M GetDistributedSakAn ](#tts.lib.ethernet.PacketMka.PacketMka.GetDistributedSakAn)
      - [A distributedSakAn ](#tts.lib.ethernet.PacketMka.PacketMka.distributedSakAn)
      - [M GetDistributedSakConfidentialityOffset ](#tts.lib.ethernet.PacketMka.PacketMka.GetDistributedSakConfidentialityOffset)
      - [A distributedSakConfidentialityOffset ](#tts.lib.ethernet.PacketMka.PacketMka.distributedSakConfidentialityOffset)
      - [M GetDistributedSakKeyNumber ](#tts.lib.ethernet.PacketMka.PacketMka.GetDistributedSakKeyNumber)
      - [A distributedSakKeyNumber ](#tts.lib.ethernet.PacketMka.PacketMka.distributedSakKeyNumber)
      - [M GetDistributedSakCipherSuite ](#tts.lib.ethernet.PacketMka.PacketMka.GetDistributedSakCipherSuite)
      - [A distributedSakCipherSuite ](#tts.lib.ethernet.PacketMka.PacketMka.distributedSakCipherSuite)
      - [M SetDistributedSakToNoMacSec ](#tts.lib.ethernet.PacketMka.PacketMka.SetDistributedSakToNoMacSec)
      - [M RemoveDistributedSak ](#tts.lib.ethernet.PacketMka.PacketMka.RemoveDistributedSak)
      - [M GetXpnLatestLpn ](#tts.lib.ethernet.PacketMka.PacketMka.GetXpnLatestLpn)
      - [A xpnLatestLpn ](#tts.lib.ethernet.PacketMka.PacketMka.xpnLatestLpn)
      - [M RemoveXpn ](#tts.lib.ethernet.PacketMka.PacketMka.RemoveXpn)
      - [M GetAnnouncementTypes ](#tts.lib.ethernet.PacketMka.PacketMka.GetAnnouncementTypes)
      - [A announcementTypes ](#tts.lib.ethernet.PacketMka.PacketMka.announcementTypes)
      - [M GetAnnouncementInfos ](#tts.lib.ethernet.PacketMka.PacketMka.GetAnnouncementInfos)
      - [A announcementInfos ](#tts.lib.ethernet.PacketMka.PacketMka.announcementInfos)
      - [M GetAnnouncementCipherSuiteCapabilities ](#tts.lib.ethernet.PacketMka.PacketMka.GetAnnouncementCipherSuiteCapabilities)
      - [A announcementCipherSuiteCapabilities ](#tts.lib.ethernet.PacketMka.PacketMka.announcementCipherSuiteCapabilities)
      - [M GetAnnouncementCipherSuiteNames ](#tts.lib.ethernet.PacketMka.PacketMka.GetAnnouncementCipherSuiteNames)
      - [A announcementCipherSuiteNames ](#tts.lib.ethernet.PacketMka.PacketMka.announcementCipherSuiteNames)
      - [M FindParent ](#tts.lib.ethernet.PacketMka.PacketMka.FindParent)
      - [M GetMacSecAn ](#tts.lib.ethernet.PacketMka.PacketMka.GetMacSecAn)
      - [M GetMacSecIcv ](#tts.lib.ethernet.PacketMka.PacketMka.GetMacSecIcv)
      - [M GetMacSecPn ](#tts.lib.ethernet.PacketMka.PacketMka.GetMacSecPn)
      - [M GetMacSecSl ](#tts.lib.ethernet.PacketMka.PacketMka.GetMacSecSl)
      - [M GetMacSecTci ](#tts.lib.ethernet.PacketMka.PacketMka.GetMacSecTci)
      - [M GetMacSecTciAn ](#tts.lib.ethernet.PacketMka.PacketMka.GetMacSecTciAn)
      - [M GetMacSecTciC ](#tts.lib.ethernet.PacketMka.PacketMka.GetMacSecTciC)
      - [M GetMacSecTciE ](#tts.lib.ethernet.PacketMka.PacketMka.GetMacSecTciE)
      - [M GetMacSecTciEs ](#tts.lib.ethernet.PacketMka.PacketMka.GetMacSecTciEs)
      - [M GetMacSecTciSc ](#tts.lib.ethernet.PacketMka.PacketMka.GetMacSecTciSc)
      - [M GetMacSecTciScb ](#tts.lib.ethernet.PacketMka.PacketMka.GetMacSecTciScb)
      - [M GetMacSecTciV ](#tts.lib.ethernet.PacketMka.PacketMka.GetMacSecTciV)
      - [M GetTimestamp ](#tts.lib.ethernet.PacketMka.PacketMka.GetTimestamp)
      - [M GetVlanCfi ](#tts.lib.ethernet.PacketMka.PacketMka.GetVlanCfi)
      - [M GetVlanCfiOuter ](#tts.lib.ethernet.PacketMka.PacketMka.GetVlanCfiOuter)
      - [M GetVlanPcp ](#tts.lib.ethernet.PacketMka.PacketMka.GetVlanPcp)
      - [M GetVlanPcpOuter ](#tts.lib.ethernet.PacketMka.PacketMka.GetVlanPcpOuter)
      - [M GetVlanVid ](#tts.lib.ethernet.PacketMka.PacketMka.GetVlanVid)
      - [M GetVlanVidOuter ](#tts.lib.ethernet.PacketMka.PacketMka.GetVlanVidOuter)
      - [M RemoveAnnouncement ](#tts.lib.ethernet.PacketMka.PacketMka.RemoveAnnouncement)
      - [M SetTimestamp ](#tts.lib.ethernet.PacketMka.PacketMka.SetTimestamp)
      - [M SetVlanCfi ](#tts.lib.ethernet.PacketMka.PacketMka.SetVlanCfi)
      - [M SetVlanCfiOuter ](#tts.lib.ethernet.PacketMka.PacketMka.SetVlanCfiOuter)
      - [M SetVlanPcp ](#tts.lib.ethernet.PacketMka.PacketMka.SetVlanPcp)
      - [M SetVlanPcpOuter ](#tts.lib.ethernet.PacketMka.PacketMka.SetVlanPcpOuter)
      - [M SetVlanVid ](#tts.lib.ethernet.PacketMka.PacketMka.SetVlanVid)
      - [M SetVlanVidOuter ](#tts.lib.ethernet.PacketMka.PacketMka.SetVlanVidOuter)
      - [A ethPayload ](#tts.lib.ethernet.PacketMka.PacketMka.ethPayload)
      - [A ethType ](#tts.lib.ethernet.PacketMka.PacketMka.ethType)
      - [A macSecAn ](#tts.lib.ethernet.PacketMka.PacketMka.macSecAn)
      - [A macSecIcv ](#tts.lib.ethernet.PacketMka.PacketMka.macSecIcv)
      - [A macSecPn ](#tts.lib.ethernet.PacketMka.PacketMka.macSecPn)
      - [A macSecSl ](#tts.lib.ethernet.PacketMka.PacketMka.macSecSl)
      - [A macSecTci ](#tts.lib.ethernet.PacketMka.PacketMka.macSecTci)
      - [A macSecTciAn ](#tts.lib.ethernet.PacketMka.PacketMka.macSecTciAn)
      - [A macSecTciC ](#tts.lib.ethernet.PacketMka.PacketMka.macSecTciC)
      - [A macSecTciE ](#tts.lib.ethernet.PacketMka.PacketMka.macSecTciE)
      - [A macSecTciEs ](#tts.lib.ethernet.PacketMka.PacketMka.macSecTciEs)
      - [A macSecTciSc ](#tts.lib.ethernet.PacketMka.PacketMka.macSecTciSc)
      - [A macSecTciScb ](#tts.lib.ethernet.PacketMka.PacketMka.macSecTciScb)
      - [A macSecTciV ](#tts.lib.ethernet.PacketMka.PacketMka.macSecTciV)
      - [A parent ](#tts.lib.ethernet.PacketMka.PacketMka.parent)
      - [A timestamp ](#tts.lib.ethernet.PacketMka.PacketMka.timestamp)
      - [A vlanCfi ](#tts.lib.ethernet.PacketMka.PacketMka.vlanCfi)
      - [A vlanCfiOuter ](#tts.lib.ethernet.PacketMka.PacketMka.vlanCfiOuter)
      - [A vlanPcp ](#tts.lib.ethernet.PacketMka.PacketMka.vlanPcp)
      - [A vlanPcpOuter ](#tts.lib.ethernet.PacketMka.PacketMka.vlanPcpOuter)
      - [A vlanVid ](#tts.lib.ethernet.PacketMka.PacketMka.vlanVid)
      - [A vlanVidOuter ](#tts.lib.ethernet.PacketMka.PacketMka.vlanVidOuter)
  - [ PacketIke ](#packetike)
    - [C PacketIke ](#tts.lib.ethernet.PacketIke.PacketIke)
      - [M GetInitiatorSpi ](#tts.lib.ethernet.PacketIke.PacketIke.GetInitiatorSpi)
      - [A initiatorSpi ](#tts.lib.ethernet.PacketIke.PacketIke.initiatorSpi)
      - [M GetResponderSpi ](#tts.lib.ethernet.PacketIke.PacketIke.GetResponderSpi)
      - [A responderSpi ](#tts.lib.ethernet.PacketIke.PacketIke.responderSpi)
      - [M GetNextPayload ](#tts.lib.ethernet.PacketIke.PacketIke.GetNextPayload)
      - [A nextPayload ](#tts.lib.ethernet.PacketIke.PacketIke.nextPayload)
      - [M GetMajorVersion ](#tts.lib.ethernet.PacketIke.PacketIke.GetMajorVersion)
      - [A majorVersion ](#tts.lib.ethernet.PacketIke.PacketIke.majorVersion)
      - [M GetMinorVersion ](#tts.lib.ethernet.PacketIke.PacketIke.GetMinorVersion)
      - [A minorVersion ](#tts.lib.ethernet.PacketIke.PacketIke.minorVersion)
      - [M GetExchangeType ](#tts.lib.ethernet.PacketIke.PacketIke.GetExchangeType)
      - [A exchangeType ](#tts.lib.ethernet.PacketIke.PacketIke.exchangeType)
      - [M GetFlags ](#tts.lib.ethernet.PacketIke.PacketIke.GetFlags)
      - [A flags ](#tts.lib.ethernet.PacketIke.PacketIke.flags)
      - [M IsInitiator ](#tts.lib.ethernet.PacketIke.PacketIke.IsInitiator)
      - [M IsResponder ](#tts.lib.ethernet.PacketIke.PacketIke.IsResponder)
      - [M SetToInitiator ](#tts.lib.ethernet.PacketIke.PacketIke.SetToInitiator)
      - [M SetToResponder ](#tts.lib.ethernet.PacketIke.PacketIke.SetToResponder)
      - [M IsRequest ](#tts.lib.ethernet.PacketIke.PacketIke.IsRequest)
      - [M IsResponse ](#tts.lib.ethernet.PacketIke.PacketIke.IsResponse)
      - [M SetToRequest ](#tts.lib.ethernet.PacketIke.PacketIke.SetToRequest)
      - [M SetToReponse ](#tts.lib.ethernet.PacketIke.PacketIke.SetToReponse)
      - [M GetMessageId ](#tts.lib.ethernet.PacketIke.PacketIke.GetMessageId)
      - [A messageId ](#tts.lib.ethernet.PacketIke.PacketIke.messageId)
      - [M GetLength ](#tts.lib.ethernet.PacketIke.PacketIke.GetLength)
      - [A length ](#tts.lib.ethernet.PacketIke.PacketIke.length)
      - [M GetKeyExchangeNextPayload ](#tts.lib.ethernet.PacketIke.PacketIke.GetKeyExchangeNextPayload)
      - [A keyExchangeNextPayload ](#tts.lib.ethernet.PacketIke.PacketIke.keyExchangeNextPayload)
      - [M IsKeyExchangeCritical ](#tts.lib.ethernet.PacketIke.PacketIke.IsKeyExchangeCritical)
      - [A keyExchangeCritical ](#tts.lib.ethernet.PacketIke.PacketIke.keyExchangeCritical)
      - [M GetKeyExchangeLength ](#tts.lib.ethernet.PacketIke.PacketIke.GetKeyExchangeLength)
      - [A keyExchangeLength ](#tts.lib.ethernet.PacketIke.PacketIke.keyExchangeLength)
      - [M GetKeyExchangeDhGroupNumber ](#tts.lib.ethernet.PacketIke.PacketIke.GetKeyExchangeDhGroupNumber)
      - [A keyExchangeDhGroupNumber ](#tts.lib.ethernet.PacketIke.PacketIke.keyExchangeDhGroupNumber)
      - [M GetKeyExchangeData ](#tts.lib.ethernet.PacketIke.PacketIke.GetKeyExchangeData)
      - [A keyExchangeData ](#tts.lib.ethernet.PacketIke.PacketIke.keyExchangeData)
      - [M GetNonceNextPayload ](#tts.lib.ethernet.PacketIke.PacketIke.GetNonceNextPayload)
      - [A nonceNextPayload ](#tts.lib.ethernet.PacketIke.PacketIke.nonceNextPayload)
      - [M IsNonceCritical ](#tts.lib.ethernet.PacketIke.PacketIke.IsNonceCritical)
      - [A nonceCritical ](#tts.lib.ethernet.PacketIke.PacketIke.nonceCritical)
      - [M GetNonceLength ](#tts.lib.ethernet.PacketIke.PacketIke.GetNonceLength)
      - [A nonceLength ](#tts.lib.ethernet.PacketIke.PacketIke.nonceLength)
      - [M GetNonceData ](#tts.lib.ethernet.PacketIke.PacketIke.GetNonceData)
      - [A nonceData ](#tts.lib.ethernet.PacketIke.PacketIke.nonceData)
      - [M GetCertificateNextPayload ](#tts.lib.ethernet.PacketIke.PacketIke.GetCertificateNextPayload)
      - [A certificateNextPayload ](#tts.lib.ethernet.PacketIke.PacketIke.certificateNextPayload)
      - [M IsCertificateCritical ](#tts.lib.ethernet.PacketIke.PacketIke.IsCertificateCritical)
      - [A certificateCritical ](#tts.lib.ethernet.PacketIke.PacketIke.certificateCritical)
      - [M GetCertificateLength ](#tts.lib.ethernet.PacketIke.PacketIke.GetCertificateLength)
      - [A certificateLength ](#tts.lib.ethernet.PacketIke.PacketIke.certificateLength)
      - [M GetCertificateEncoding ](#tts.lib.ethernet.PacketIke.PacketIke.GetCertificateEncoding)
      - [A certificateEncoding ](#tts.lib.ethernet.PacketIke.PacketIke.certificateEncoding)
      - [M GetCertificateData ](#tts.lib.ethernet.PacketIke.PacketIke.GetCertificateData)
      - [A certificateData ](#tts.lib.ethernet.PacketIke.PacketIke.certificateData)
      - [M GetCertificateRequestNextPayload ](#tts.lib.ethernet.PacketIke.PacketIke.GetCertificateRequestNextPayload)
      - [A certificateRequestNextPayload ](#tts.lib.ethernet.PacketIke.PacketIke.certificateRequestNextPayload)
      - [M GetCertificateRequestCritical ](#tts.lib.ethernet.PacketIke.PacketIke.GetCertificateRequestCritical)
      - [A certificateRequestCritical ](#tts.lib.ethernet.PacketIke.PacketIke.certificateRequestCritical)
      - [M GetCertificateRequestLength ](#tts.lib.ethernet.PacketIke.PacketIke.GetCertificateRequestLength)
      - [A certificateRequestLength ](#tts.lib.ethernet.PacketIke.PacketIke.certificateRequestLength)
      - [M GetCertificateRequestData ](#tts.lib.ethernet.PacketIke.PacketIke.GetCertificateRequestData)
      - [A certificateRequestData ](#tts.lib.ethernet.PacketIke.PacketIke.certificateRequestData)
      - [M GetCertificateRequestEncoding ](#tts.lib.ethernet.PacketIke.PacketIke.GetCertificateRequestEncoding)
      - [A certificateRequestEncoding ](#tts.lib.ethernet.PacketIke.PacketIke.certificateRequestEncoding)
      - [M GetIdentInitiatorNextPayload ](#tts.lib.ethernet.PacketIke.PacketIke.GetIdentInitiatorNextPayload)
      - [A identInitiatorNextPayload ](#tts.lib.ethernet.PacketIke.PacketIke.identInitiatorNextPayload)
      - [M GetIdentInitiatorCritical ](#tts.lib.ethernet.PacketIke.PacketIke.GetIdentInitiatorCritical)
      - [A identInitiatorCritical ](#tts.lib.ethernet.PacketIke.PacketIke.identInitiatorCritical)
      - [M GetIdentInitiatorLength ](#tts.lib.ethernet.PacketIke.PacketIke.GetIdentInitiatorLength)
      - [A identInitiatorLength ](#tts.lib.ethernet.PacketIke.PacketIke.identInitiatorLength)
      - [M GetIdentInitiatorIdType ](#tts.lib.ethernet.PacketIke.PacketIke.GetIdentInitiatorIdType)
      - [A identInitiatorIdType ](#tts.lib.ethernet.PacketIke.PacketIke.identInitiatorIdType)
      - [M GetIdentInitiatorData ](#tts.lib.ethernet.PacketIke.PacketIke.GetIdentInitiatorData)
      - [A identInitiatorData ](#tts.lib.ethernet.PacketIke.PacketIke.identInitiatorData)
      - [M GetIdentResponderNextPayload ](#tts.lib.ethernet.PacketIke.PacketIke.GetIdentResponderNextPayload)
      - [A identResponderNextPayload ](#tts.lib.ethernet.PacketIke.PacketIke.identResponderNextPayload)
      - [M GetIdentResponderCritical ](#tts.lib.ethernet.PacketIke.PacketIke.GetIdentResponderCritical)
      - [A identResponderCritical ](#tts.lib.ethernet.PacketIke.PacketIke.identResponderCritical)
      - [M GetIdentResponderLength ](#tts.lib.ethernet.PacketIke.PacketIke.GetIdentResponderLength)
      - [A identResponderLength ](#tts.lib.ethernet.PacketIke.PacketIke.identResponderLength)
      - [M GetIdentResponderIdType ](#tts.lib.ethernet.PacketIke.PacketIke.GetIdentResponderIdType)
      - [A identResponderIdType ](#tts.lib.ethernet.PacketIke.PacketIke.identResponderIdType)
      - [M GetIdentResponderData ](#tts.lib.ethernet.PacketIke.PacketIke.GetIdentResponderData)
      - [A identResponderData ](#tts.lib.ethernet.PacketIke.PacketIke.identResponderData)
      - [M GetAuthNextPayload ](#tts.lib.ethernet.PacketIke.PacketIke.GetAuthNextPayload)
      - [A authNextPayload ](#tts.lib.ethernet.PacketIke.PacketIke.authNextPayload)
      - [M GetAuthCritical ](#tts.lib.ethernet.PacketIke.PacketIke.GetAuthCritical)
      - [A authCritical ](#tts.lib.ethernet.PacketIke.PacketIke.authCritical)
      - [M GetAuthLength ](#tts.lib.ethernet.PacketIke.PacketIke.GetAuthLength)
      - [A authLength ](#tts.lib.ethernet.PacketIke.PacketIke.authLength)
      - [M GetAuthMethod ](#tts.lib.ethernet.PacketIke.PacketIke.GetAuthMethod)
      - [A authMethod ](#tts.lib.ethernet.PacketIke.PacketIke.authMethod)
      - [M GetAuthData ](#tts.lib.ethernet.PacketIke.PacketIke.GetAuthData)
      - [A authData ](#tts.lib.ethernet.PacketIke.PacketIke.authData)
      - [M GetTsInitiatorNextPayload ](#tts.lib.ethernet.PacketIke.PacketIke.GetTsInitiatorNextPayload)
      - [A tsInitiatorNextPayload ](#tts.lib.ethernet.PacketIke.PacketIke.tsInitiatorNextPayload)
      - [M GetTsInitiatorCritical ](#tts.lib.ethernet.PacketIke.PacketIke.GetTsInitiatorCritical)
      - [A tsInitiatorCritical ](#tts.lib.ethernet.PacketIke.PacketIke.tsInitiatorCritical)
      - [M GetTsInitiatorLength ](#tts.lib.ethernet.PacketIke.PacketIke.GetTsInitiatorLength)
      - [A tsInitiatorLength ](#tts.lib.ethernet.PacketIke.PacketIke.tsInitiatorLength)
      - [M GetTsInitiatorNumOfTss ](#tts.lib.ethernet.PacketIke.PacketIke.GetTsInitiatorNumOfTss)
      - [A tsInitiatorNumOfTss ](#tts.lib.ethernet.PacketIke.PacketIke.tsInitiatorNumOfTss)
      - [M GetTsInitiatorTrafficSelectors ](#tts.lib.ethernet.PacketIke.PacketIke.GetTsInitiatorTrafficSelectors)
      - [A tsInitiatorTrafficSelectors ](#tts.lib.ethernet.PacketIke.PacketIke.tsInitiatorTrafficSelectors)
      - [M GetTsResponderNextPayload ](#tts.lib.ethernet.PacketIke.PacketIke.GetTsResponderNextPayload)
      - [A tsResponderNextPayload ](#tts.lib.ethernet.PacketIke.PacketIke.tsResponderNextPayload)
      - [M GetTsResponderCritical ](#tts.lib.ethernet.PacketIke.PacketIke.GetTsResponderCritical)
      - [A tsResponderCritical ](#tts.lib.ethernet.PacketIke.PacketIke.tsResponderCritical)
      - [M GetTsResponderLength ](#tts.lib.ethernet.PacketIke.PacketIke.GetTsResponderLength)
      - [A tsResponderLength ](#tts.lib.ethernet.PacketIke.PacketIke.tsResponderLength)
      - [M GetTsResponderNumOfTss ](#tts.lib.ethernet.PacketIke.PacketIke.GetTsResponderNumOfTss)
      - [A tsResponderNumOfTss ](#tts.lib.ethernet.PacketIke.PacketIke.tsResponderNumOfTss)
      - [M GetTsResponderTrafficSelectors ](#tts.lib.ethernet.PacketIke.PacketIke.GetTsResponderTrafficSelectors)
      - [A tsResponderTrafficSelectors ](#tts.lib.ethernet.PacketIke.PacketIke.tsResponderTrafficSelectors)
      - [M GetSaNextPayload ](#tts.lib.ethernet.PacketIke.PacketIke.GetSaNextPayload)
      - [A saNextPayload ](#tts.lib.ethernet.PacketIke.PacketIke.saNextPayload)
      - [M GetSaCritical ](#tts.lib.ethernet.PacketIke.PacketIke.GetSaCritical)
      - [A saCritical ](#tts.lib.ethernet.PacketIke.PacketIke.saCritical)
      - [M GetSaLength ](#tts.lib.ethernet.PacketIke.PacketIke.GetSaLength)
      - [A saLength ](#tts.lib.ethernet.PacketIke.PacketIke.saLength)
      - [M GetSaProposals ](#tts.lib.ethernet.PacketIke.PacketIke.GetSaProposals)
      - [A saProposals ](#tts.lib.ethernet.PacketIke.PacketIke.saProposals)
      - [M GetNotifyNumOfPayloads ](#tts.lib.ethernet.PacketIke.PacketIke.GetNotifyNumOfPayloads)
      - [A notifyNumOfPayloads ](#tts.lib.ethernet.PacketIke.PacketIke.notifyNumOfPayloads)
      - [M GetNotifyNextPayload ](#tts.lib.ethernet.PacketIke.PacketIke.GetNotifyNextPayload)
      - [A notifyNextPayload ](#tts.lib.ethernet.PacketIke.PacketIke.notifyNextPayload)
      - [M GetNotifyCritical ](#tts.lib.ethernet.PacketIke.PacketIke.GetNotifyCritical)
      - [A notifyCritical ](#tts.lib.ethernet.PacketIke.PacketIke.notifyCritical)
      - [M GetNotifyLength ](#tts.lib.ethernet.PacketIke.PacketIke.GetNotifyLength)
      - [A notifyLength ](#tts.lib.ethernet.PacketIke.PacketIke.notifyLength)
      - [M GetNotifyProtocolId ](#tts.lib.ethernet.PacketIke.PacketIke.GetNotifyProtocolId)
      - [A notifyProtocolId ](#tts.lib.ethernet.PacketIke.PacketIke.notifyProtocolId)
      - [M GetNotifySpiSize ](#tts.lib.ethernet.PacketIke.PacketIke.GetNotifySpiSize)
      - [A notifySpiSize ](#tts.lib.ethernet.PacketIke.PacketIke.notifySpiSize)
      - [M GetNotifyMessageType ](#tts.lib.ethernet.PacketIke.PacketIke.GetNotifyMessageType)
      - [A notifyMessageType ](#tts.lib.ethernet.PacketIke.PacketIke.notifyMessageType)
      - [M GetNotifySpi ](#tts.lib.ethernet.PacketIke.PacketIke.GetNotifySpi)
      - [A notifySpi ](#tts.lib.ethernet.PacketIke.PacketIke.notifySpi)
      - [M GetNotifyData ](#tts.lib.ethernet.PacketIke.PacketIke.GetNotifyData)
      - [A notifyData ](#tts.lib.ethernet.PacketIke.PacketIke.notifyData)
      - [M GetDeleteNextPayload ](#tts.lib.ethernet.PacketIke.PacketIke.GetDeleteNextPayload)
      - [A deleteNextPayload ](#tts.lib.ethernet.PacketIke.PacketIke.deleteNextPayload)
      - [M GetDeleteCritical ](#tts.lib.ethernet.PacketIke.PacketIke.GetDeleteCritical)
      - [A deleteCritical ](#tts.lib.ethernet.PacketIke.PacketIke.deleteCritical)
      - [M GetDeleteLength ](#tts.lib.ethernet.PacketIke.PacketIke.GetDeleteLength)
      - [A deleteLength ](#tts.lib.ethernet.PacketIke.PacketIke.deleteLength)
      - [M GetDeleteProtocolId ](#tts.lib.ethernet.PacketIke.PacketIke.GetDeleteProtocolId)
      - [A deleteProtocolId ](#tts.lib.ethernet.PacketIke.PacketIke.deleteProtocolId)
      - [M GetDeleteSpiSize ](#tts.lib.ethernet.PacketIke.PacketIke.GetDeleteSpiSize)
      - [A deleteSpiSize ](#tts.lib.ethernet.PacketIke.PacketIke.deleteSpiSize)
      - [M GetDeleteSpis ](#tts.lib.ethernet.PacketIke.PacketIke.GetDeleteSpis)
      - [M CalcIpLen ](#tts.lib.ethernet.PacketIke.PacketIke.CalcIpLen)
      - [M CalcUdpLen ](#tts.lib.ethernet.PacketIke.PacketIke.CalcUdpLen)
      - [M FindParent ](#tts.lib.ethernet.PacketIke.PacketIke.FindParent)
      - [M GetEthDstMac ](#tts.lib.ethernet.PacketIke.PacketIke.GetEthDstMac)
      - [M GetEthPayload ](#tts.lib.ethernet.PacketIke.PacketIke.GetEthPayload)
      - [M GetEthSrcMac ](#tts.lib.ethernet.PacketIke.PacketIke.GetEthSrcMac)
      - [M GetEthType ](#tts.lib.ethernet.PacketIke.PacketIke.GetEthType)
      - [M GetIpAhIcv ](#tts.lib.ethernet.PacketIke.PacketIke.GetIpAhIcv)
      - [M GetIpAhLen ](#tts.lib.ethernet.PacketIke.PacketIke.GetIpAhLen)
      - [M GetIpAhNxt ](#tts.lib.ethernet.PacketIke.PacketIke.GetIpAhNxt)
      - [M GetIpAhRsvd ](#tts.lib.ethernet.PacketIke.PacketIke.GetIpAhRsvd)
      - [M GetIpAhSeq ](#tts.lib.ethernet.PacketIke.PacketIke.GetIpAhSeq)
      - [M GetIpAhSpi ](#tts.lib.ethernet.PacketIke.PacketIke.GetIpAhSpi)
      - [M GetIpChecksum ](#tts.lib.ethernet.PacketIke.PacketIke.GetIpChecksum)
      - [M GetIpDst ](#tts.lib.ethernet.PacketIke.PacketIke.GetIpDst)
      - [M GetIpIdent ](#tts.lib.ethernet.PacketIke.PacketIke.GetIpIdent)
      - [M GetIpLen ](#tts.lib.ethernet.PacketIke.PacketIke.GetIpLen)
      - [M GetIpOffset ](#tts.lib.ethernet.PacketIke.PacketIke.GetIpOffset)
      - [M GetIpPayload ](#tts.lib.ethernet.PacketIke.PacketIke.GetIpPayload)
      - [M GetIpProt ](#tts.lib.ethernet.PacketIke.PacketIke.GetIpProt)
      - [M GetIpSrc ](#tts.lib.ethernet.PacketIke.PacketIke.GetIpSrc)
      - [M GetIpTos ](#tts.lib.ethernet.PacketIke.PacketIke.GetIpTos)
      - [M GetIpTtl ](#tts.lib.ethernet.PacketIke.PacketIke.GetIpTtl)
      - [M GetIpVersionAndHeaderLength ](#tts.lib.ethernet.PacketIke.PacketIke.GetIpVersionAndHeaderLength)
      - [M GetMacSecAn ](#tts.lib.ethernet.PacketIke.PacketIke.GetMacSecAn)
      - [M GetMacSecIcv ](#tts.lib.ethernet.PacketIke.PacketIke.GetMacSecIcv)
      - [M GetMacSecPn ](#tts.lib.ethernet.PacketIke.PacketIke.GetMacSecPn)
      - [M GetMacSecSci ](#tts.lib.ethernet.PacketIke.PacketIke.GetMacSecSci)
      - [M GetMacSecSl ](#tts.lib.ethernet.PacketIke.PacketIke.GetMacSecSl)
      - [M GetMacSecTci ](#tts.lib.ethernet.PacketIke.PacketIke.GetMacSecTci)
      - [M GetMacSecTciAn ](#tts.lib.ethernet.PacketIke.PacketIke.GetMacSecTciAn)
      - [M GetMacSecTciC ](#tts.lib.ethernet.PacketIke.PacketIke.GetMacSecTciC)
      - [M GetMacSecTciE ](#tts.lib.ethernet.PacketIke.PacketIke.GetMacSecTciE)
      - [M GetMacSecTciEs ](#tts.lib.ethernet.PacketIke.PacketIke.GetMacSecTciEs)
      - [M GetMacSecTciSc ](#tts.lib.ethernet.PacketIke.PacketIke.GetMacSecTciSc)
      - [M GetMacSecTciScb ](#tts.lib.ethernet.PacketIke.PacketIke.GetMacSecTciScb)
      - [M GetMacSecTciV ](#tts.lib.ethernet.PacketIke.PacketIke.GetMacSecTciV)
      - [M GetTimestamp ](#tts.lib.ethernet.PacketIke.PacketIke.GetTimestamp)
      - [M GetUdpChecksum ](#tts.lib.ethernet.PacketIke.PacketIke.GetUdpChecksum)
      - [M GetUdpDst ](#tts.lib.ethernet.PacketIke.PacketIke.GetUdpDst)
      - [M GetUdpLen ](#tts.lib.ethernet.PacketIke.PacketIke.GetUdpLen)
      - [M GetUdpPayload ](#tts.lib.ethernet.PacketIke.PacketIke.GetUdpPayload)
      - [M GetUdpSrc ](#tts.lib.ethernet.PacketIke.PacketIke.GetUdpSrc)
      - [M GetVlanCfi ](#tts.lib.ethernet.PacketIke.PacketIke.GetVlanCfi)
      - [M GetVlanCfiOuter ](#tts.lib.ethernet.PacketIke.PacketIke.GetVlanCfiOuter)
      - [M GetVlanPcp ](#tts.lib.ethernet.PacketIke.PacketIke.GetVlanPcp)
      - [M GetVlanPcpOuter ](#tts.lib.ethernet.PacketIke.PacketIke.GetVlanPcpOuter)
      - [M GetVlanVid ](#tts.lib.ethernet.PacketIke.PacketIke.GetVlanVid)
      - [M GetVlanVidOuter ](#tts.lib.ethernet.PacketIke.PacketIke.GetVlanVidOuter)
      - [A PK_CLASS ](#tts.lib.ethernet.PacketIke.PacketIke.PK_CLASS)
      - [M SetEthDstMac ](#tts.lib.ethernet.PacketIke.PacketIke.SetEthDstMac)
      - [M SetEthPayload ](#tts.lib.ethernet.PacketIke.PacketIke.SetEthPayload)
      - [M SetEthSrcMac ](#tts.lib.ethernet.PacketIke.PacketIke.SetEthSrcMac)
      - [M SetEthType ](#tts.lib.ethernet.PacketIke.PacketIke.SetEthType)
      - [M SetIpChecksum ](#tts.lib.ethernet.PacketIke.PacketIke.SetIpChecksum)
      - [M SetIpDst ](#tts.lib.ethernet.PacketIke.PacketIke.SetIpDst)
      - [M SetIpIdent ](#tts.lib.ethernet.PacketIke.PacketIke.SetIpIdent)
      - [M SetIpLen ](#tts.lib.ethernet.PacketIke.PacketIke.SetIpLen)
      - [M SetIpOffset ](#tts.lib.ethernet.PacketIke.PacketIke.SetIpOffset)
      - [M SetIpPayload ](#tts.lib.ethernet.PacketIke.PacketIke.SetIpPayload)
      - [M SetIpProt ](#tts.lib.ethernet.PacketIke.PacketIke.SetIpProt)
      - [M SetIpSrc ](#tts.lib.ethernet.PacketIke.PacketIke.SetIpSrc)
      - [M SetIpTos ](#tts.lib.ethernet.PacketIke.PacketIke.SetIpTos)
      - [M SetIpTtl ](#tts.lib.ethernet.PacketIke.PacketIke.SetIpTtl)
      - [M SetIpVersionAndHeaderLength ](#tts.lib.ethernet.PacketIke.PacketIke.SetIpVersionAndHeaderLength)
      - [M SetTimestamp ](#tts.lib.ethernet.PacketIke.PacketIke.SetTimestamp)
      - [M SetUdpChecksum ](#tts.lib.ethernet.PacketIke.PacketIke.SetUdpChecksum)
      - [M SetUdpDst ](#tts.lib.ethernet.PacketIke.PacketIke.SetUdpDst)
      - [M SetUdpLen ](#tts.lib.ethernet.PacketIke.PacketIke.SetUdpLen)
      - [M SetUdpPayload ](#tts.lib.ethernet.PacketIke.PacketIke.SetUdpPayload)
      - [M SetUdpSrc ](#tts.lib.ethernet.PacketIke.PacketIke.SetUdpSrc)
      - [M SetVlanCfi ](#tts.lib.ethernet.PacketIke.PacketIke.SetVlanCfi)
      - [M SetVlanCfiOuter ](#tts.lib.ethernet.PacketIke.PacketIke.SetVlanCfiOuter)
      - [M SetVlanPcp ](#tts.lib.ethernet.PacketIke.PacketIke.SetVlanPcp)
      - [M SetVlanPcpOuter ](#tts.lib.ethernet.PacketIke.PacketIke.SetVlanPcpOuter)
      - [M SetVlanVid ](#tts.lib.ethernet.PacketIke.PacketIke.SetVlanVid)
      - [M SetVlanVidOuter ](#tts.lib.ethernet.PacketIke.PacketIke.SetVlanVidOuter)
      - [A ethDstMac ](#tts.lib.ethernet.PacketIke.PacketIke.ethDstMac)
      - [A ethPayload ](#tts.lib.ethernet.PacketIke.PacketIke.ethPayload)
      - [A ethSrcMac ](#tts.lib.ethernet.PacketIke.PacketIke.ethSrcMac)
      - [A ethType ](#tts.lib.ethernet.PacketIke.PacketIke.ethType)
      - [A ipAhIcv ](#tts.lib.ethernet.PacketIke.PacketIke.ipAhIcv)
      - [A ipAhLen ](#tts.lib.ethernet.PacketIke.PacketIke.ipAhLen)
      - [A ipAhNxt ](#tts.lib.ethernet.PacketIke.PacketIke.ipAhNxt)
      - [A ipAhRsvd ](#tts.lib.ethernet.PacketIke.PacketIke.ipAhRsvd)
      - [A ipAhSeq ](#tts.lib.ethernet.PacketIke.PacketIke.ipAhSeq)
      - [A ipAhSpi ](#tts.lib.ethernet.PacketIke.PacketIke.ipAhSpi)
      - [A ipChecksum ](#tts.lib.ethernet.PacketIke.PacketIke.ipChecksum)
      - [A ipDst ](#tts.lib.ethernet.PacketIke.PacketIke.ipDst)
      - [A ipIdent ](#tts.lib.ethernet.PacketIke.PacketIke.ipIdent)
      - [A ipLen ](#tts.lib.ethernet.PacketIke.PacketIke.ipLen)
      - [A ipOffset ](#tts.lib.ethernet.PacketIke.PacketIke.ipOffset)
      - [A ipPayload ](#tts.lib.ethernet.PacketIke.PacketIke.ipPayload)
      - [A ipProt ](#tts.lib.ethernet.PacketIke.PacketIke.ipProt)
      - [A ipSrc ](#tts.lib.ethernet.PacketIke.PacketIke.ipSrc)
      - [A ipTos ](#tts.lib.ethernet.PacketIke.PacketIke.ipTos)
      - [A ipTtl ](#tts.lib.ethernet.PacketIke.PacketIke.ipTtl)
      - [A ipVersionHeader ](#tts.lib.ethernet.PacketIke.PacketIke.ipVersionHeader)
      - [A macSecAn ](#tts.lib.ethernet.PacketIke.PacketIke.macSecAn)
      - [A macSecIcv ](#tts.lib.ethernet.PacketIke.PacketIke.macSecIcv)
      - [A macSecPn ](#tts.lib.ethernet.PacketIke.PacketIke.macSecPn)
      - [A macSecSci ](#tts.lib.ethernet.PacketIke.PacketIke.macSecSci)
      - [A macSecSl ](#tts.lib.ethernet.PacketIke.PacketIke.macSecSl)
      - [A macSecTci ](#tts.lib.ethernet.PacketIke.PacketIke.macSecTci)
      - [A macSecTciAn ](#tts.lib.ethernet.PacketIke.PacketIke.macSecTciAn)
      - [A macSecTciC ](#tts.lib.ethernet.PacketIke.PacketIke.macSecTciC)
      - [A macSecTciE ](#tts.lib.ethernet.PacketIke.PacketIke.macSecTciE)
      - [A macSecTciEs ](#tts.lib.ethernet.PacketIke.PacketIke.macSecTciEs)
      - [A macSecTciSc ](#tts.lib.ethernet.PacketIke.PacketIke.macSecTciSc)
      - [A macSecTciScb ](#tts.lib.ethernet.PacketIke.PacketIke.macSecTciScb)
      - [A macSecTciV ](#tts.lib.ethernet.PacketIke.PacketIke.macSecTciV)
      - [A parent ](#tts.lib.ethernet.PacketIke.PacketIke.parent)
      - [A timestamp ](#tts.lib.ethernet.PacketIke.PacketIke.timestamp)
      - [A udpChecksum ](#tts.lib.ethernet.PacketIke.PacketIke.udpChecksum)
      - [A udpDst ](#tts.lib.ethernet.PacketIke.PacketIke.udpDst)
      - [A udpLen ](#tts.lib.ethernet.PacketIke.PacketIke.udpLen)
      - [A udpPayload ](#tts.lib.ethernet.PacketIke.PacketIke.udpPayload)
      - [A udpSrc ](#tts.lib.ethernet.PacketIke.PacketIke.udpSrc)
      - [A vlanCfi ](#tts.lib.ethernet.PacketIke.PacketIke.vlanCfi)
      - [A vlanCfiOuter ](#tts.lib.ethernet.PacketIke.PacketIke.vlanCfiOuter)
      - [A vlanPcp ](#tts.lib.ethernet.PacketIke.PacketIke.vlanPcp)
      - [A vlanPcpOuter ](#tts.lib.ethernet.PacketIke.PacketIke.vlanPcpOuter)
      - [A vlanVid ](#tts.lib.ethernet.PacketIke.PacketIke.vlanVid)
      - [A vlanVidOuter ](#tts.lib.ethernet.PacketIke.PacketIke.vlanVidOuter)
      - [A deleteSpis ](#tts.lib.ethernet.PacketIke.PacketIke.deleteSpis)
      - [M GetDeleteNumOfSpis ](#tts.lib.ethernet.PacketIke.PacketIke.GetDeleteNumOfSpis)
      - [A deleteNumOfSpis ](#tts.lib.ethernet.PacketIke.PacketIke.deleteNumOfSpis)
  - [ PacketTcp ](#packettcp)
    - [C PacketTcp ](#tts.lib.ethernet.PacketTcp.PacketTcp)
      - [M GetTcpLen ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetTcpLen)
      - [M GetTcpSrc ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetTcpSrc)
      - [M SetTcpSrc ](#tts.lib.ethernet.PacketTcp.PacketTcp.SetTcpSrc)
      - [A tcpSrc ](#tts.lib.ethernet.PacketTcp.PacketTcp.tcpSrc)
      - [M GetTcpDst ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetTcpDst)
      - [M SetTcpDst ](#tts.lib.ethernet.PacketTcp.PacketTcp.SetTcpDst)
      - [A tcpDst ](#tts.lib.ethernet.PacketTcp.PacketTcp.tcpDst)
      - [M GetTcpSeq ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetTcpSeq)
      - [M SetTcpSeq ](#tts.lib.ethernet.PacketTcp.PacketTcp.SetTcpSeq)
      - [A tcpSeq ](#tts.lib.ethernet.PacketTcp.PacketTcp.tcpSeq)
      - [M GetTcpAck ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetTcpAck)
      - [M SetTcpAck ](#tts.lib.ethernet.PacketTcp.PacketTcp.SetTcpAck)
      - [A tcpAck ](#tts.lib.ethernet.PacketTcp.PacketTcp.tcpAck)
      - [M GetTcpOffset ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetTcpOffset)
      - [M SetTcpOffset ](#tts.lib.ethernet.PacketTcp.PacketTcp.SetTcpOffset)
      - [A tcpOffset ](#tts.lib.ethernet.PacketTcp.PacketTcp.tcpOffset)
      - [M GetTcpFlags ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetTcpFlags)
      - [M SetTcpFlags ](#tts.lib.ethernet.PacketTcp.PacketTcp.SetTcpFlags)
      - [A tcpFlags ](#tts.lib.ethernet.PacketTcp.PacketTcp.tcpFlags)
      - [M GetTcpWindow ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetTcpWindow)
      - [M SetTcpWindow ](#tts.lib.ethernet.PacketTcp.PacketTcp.SetTcpWindow)
      - [A tcpWindow ](#tts.lib.ethernet.PacketTcp.PacketTcp.tcpWindow)
      - [M GetTcpChecksum ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetTcpChecksum)
      - [M SetTcpChecksum ](#tts.lib.ethernet.PacketTcp.PacketTcp.SetTcpChecksum)
      - [A tcpChecksum ](#tts.lib.ethernet.PacketTcp.PacketTcp.tcpChecksum)
      - [M GetTcpUrgent ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetTcpUrgent)
      - [M SetTcpUrgent ](#tts.lib.ethernet.PacketTcp.PacketTcp.SetTcpUrgent)
      - [A tcpUrgent ](#tts.lib.ethernet.PacketTcp.PacketTcp.tcpUrgent)
      - [M GetTcpPayload ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetTcpPayload)
      - [M SetTcpPayload ](#tts.lib.ethernet.PacketTcp.PacketTcp.SetTcpPayload)
      - [A tcpPayload ](#tts.lib.ethernet.PacketTcp.PacketTcp.tcpPayload)
      - [M GetTcpOptions ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetTcpOptions)
      - [A tcpOptions ](#tts.lib.ethernet.PacketTcp.PacketTcp.tcpOptions)
      - [M CalcIpLen ](#tts.lib.ethernet.PacketTcp.PacketTcp.CalcIpLen)
      - [M FindParent ](#tts.lib.ethernet.PacketTcp.PacketTcp.FindParent)
      - [M GetEthDstMac ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetEthDstMac)
      - [M GetEthPayload ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetEthPayload)
      - [M GetEthSrcMac ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetEthSrcMac)
      - [M GetEthType ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetEthType)
      - [M GetIpAhIcv ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetIpAhIcv)
      - [M GetIpAhLen ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetIpAhLen)
      - [M GetIpAhNxt ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetIpAhNxt)
      - [M GetIpAhRsvd ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetIpAhRsvd)
      - [M GetIpAhSeq ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetIpAhSeq)
      - [M GetIpAhSpi ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetIpAhSpi)
      - [M GetIpChecksum ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetIpChecksum)
      - [M GetIpDst ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetIpDst)
      - [M GetIpIdent ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetIpIdent)
      - [M GetIpLen ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetIpLen)
      - [M GetIpOffset ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetIpOffset)
      - [M GetIpPayload ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetIpPayload)
      - [M GetIpProt ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetIpProt)
      - [M GetIpSrc ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetIpSrc)
      - [M GetIpTos ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetIpTos)
      - [M GetIpTtl ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetIpTtl)
      - [M GetIpVersionAndHeaderLength ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetIpVersionAndHeaderLength)
      - [M GetMacSecAn ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetMacSecAn)
      - [M GetMacSecIcv ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetMacSecIcv)
      - [M GetMacSecPn ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetMacSecPn)
      - [M GetMacSecSci ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetMacSecSci)
      - [M GetMacSecSl ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetMacSecSl)
      - [M GetMacSecTci ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetMacSecTci)
      - [M GetMacSecTciAn ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetMacSecTciAn)
      - [M GetMacSecTciC ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetMacSecTciC)
      - [M GetMacSecTciE ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetMacSecTciE)
      - [M GetMacSecTciEs ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetMacSecTciEs)
      - [M GetMacSecTciSc ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetMacSecTciSc)
      - [M GetMacSecTciScb ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetMacSecTciScb)
      - [M GetMacSecTciV ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetMacSecTciV)
      - [M GetTimestamp ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetTimestamp)
      - [M GetVlanCfi ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetVlanCfi)
      - [M GetVlanCfiOuter ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetVlanCfiOuter)
      - [M GetVlanPcp ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetVlanPcp)
      - [M GetVlanPcpOuter ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetVlanPcpOuter)
      - [M GetVlanVid ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetVlanVid)
      - [M GetVlanVidOuter ](#tts.lib.ethernet.PacketTcp.PacketTcp.GetVlanVidOuter)
      - [A PK_CLASS ](#tts.lib.ethernet.PacketTcp.PacketTcp.PK_CLASS)
      - [M SetEthDstMac ](#tts.lib.ethernet.PacketTcp.PacketTcp.SetEthDstMac)
      - [M SetEthPayload ](#tts.lib.ethernet.PacketTcp.PacketTcp.SetEthPayload)
      - [M SetEthSrcMac ](#tts.lib.ethernet.PacketTcp.PacketTcp.SetEthSrcMac)
      - [M SetEthType ](#tts.lib.ethernet.PacketTcp.PacketTcp.SetEthType)
      - [M SetIpChecksum ](#tts.lib.ethernet.PacketTcp.PacketTcp.SetIpChecksum)
      - [M SetIpDst ](#tts.lib.ethernet.PacketTcp.PacketTcp.SetIpDst)
      - [M SetIpIdent ](#tts.lib.ethernet.PacketTcp.PacketTcp.SetIpIdent)
      - [M SetIpLen ](#tts.lib.ethernet.PacketTcp.PacketTcp.SetIpLen)
      - [M SetIpOffset ](#tts.lib.ethernet.PacketTcp.PacketTcp.SetIpOffset)
      - [M SetIpPayload ](#tts.lib.ethernet.PacketTcp.PacketTcp.SetIpPayload)
      - [M SetIpProt ](#tts.lib.ethernet.PacketTcp.PacketTcp.SetIpProt)
      - [M SetIpSrc ](#tts.lib.ethernet.PacketTcp.PacketTcp.SetIpSrc)
      - [M SetIpTos ](#tts.lib.ethernet.PacketTcp.PacketTcp.SetIpTos)
      - [M SetIpTtl ](#tts.lib.ethernet.PacketTcp.PacketTcp.SetIpTtl)
      - [M SetIpVersionAndHeaderLength ](#tts.lib.ethernet.PacketTcp.PacketTcp.SetIpVersionAndHeaderLength)
      - [M SetTimestamp ](#tts.lib.ethernet.PacketTcp.PacketTcp.SetTimestamp)
      - [M SetVlanCfi ](#tts.lib.ethernet.PacketTcp.PacketTcp.SetVlanCfi)
      - [M SetVlanCfiOuter ](#tts.lib.ethernet.PacketTcp.PacketTcp.SetVlanCfiOuter)
      - [M SetVlanPcp ](#tts.lib.ethernet.PacketTcp.PacketTcp.SetVlanPcp)
      - [M SetVlanPcpOuter ](#tts.lib.ethernet.PacketTcp.PacketTcp.SetVlanPcpOuter)
      - [M SetVlanVid ](#tts.lib.ethernet.PacketTcp.PacketTcp.SetVlanVid)
      - [M SetVlanVidOuter ](#tts.lib.ethernet.PacketTcp.PacketTcp.SetVlanVidOuter)
      - [A ethDstMac ](#tts.lib.ethernet.PacketTcp.PacketTcp.ethDstMac)
      - [A ethPayload ](#tts.lib.ethernet.PacketTcp.PacketTcp.ethPayload)
      - [A ethSrcMac ](#tts.lib.ethernet.PacketTcp.PacketTcp.ethSrcMac)
      - [A ethType ](#tts.lib.ethernet.PacketTcp.PacketTcp.ethType)
      - [A ipAhIcv ](#tts.lib.ethernet.PacketTcp.PacketTcp.ipAhIcv)
      - [A ipAhLen ](#tts.lib.ethernet.PacketTcp.PacketTcp.ipAhLen)
      - [A ipAhNxt ](#tts.lib.ethernet.PacketTcp.PacketTcp.ipAhNxt)
      - [A ipAhRsvd ](#tts.lib.ethernet.PacketTcp.PacketTcp.ipAhRsvd)
      - [A ipAhSeq ](#tts.lib.ethernet.PacketTcp.PacketTcp.ipAhSeq)
      - [A ipAhSpi ](#tts.lib.ethernet.PacketTcp.PacketTcp.ipAhSpi)
      - [A ipChecksum ](#tts.lib.ethernet.PacketTcp.PacketTcp.ipChecksum)
      - [A ipDst ](#tts.lib.ethernet.PacketTcp.PacketTcp.ipDst)
      - [A ipIdent ](#tts.lib.ethernet.PacketTcp.PacketTcp.ipIdent)
      - [A ipLen ](#tts.lib.ethernet.PacketTcp.PacketTcp.ipLen)
      - [A ipOffset ](#tts.lib.ethernet.PacketTcp.PacketTcp.ipOffset)
      - [A ipPayload ](#tts.lib.ethernet.PacketTcp.PacketTcp.ipPayload)
      - [A ipProt ](#tts.lib.ethernet.PacketTcp.PacketTcp.ipProt)
      - [A ipSrc ](#tts.lib.ethernet.PacketTcp.PacketTcp.ipSrc)
      - [A ipTos ](#tts.lib.ethernet.PacketTcp.PacketTcp.ipTos)
      - [A ipTtl ](#tts.lib.ethernet.PacketTcp.PacketTcp.ipTtl)
      - [A ipVersionHeader ](#tts.lib.ethernet.PacketTcp.PacketTcp.ipVersionHeader)
      - [A macSecAn ](#tts.lib.ethernet.PacketTcp.PacketTcp.macSecAn)
      - [A macSecIcv ](#tts.lib.ethernet.PacketTcp.PacketTcp.macSecIcv)
      - [A macSecPn ](#tts.lib.ethernet.PacketTcp.PacketTcp.macSecPn)
      - [A macSecSci ](#tts.lib.ethernet.PacketTcp.PacketTcp.macSecSci)
      - [A macSecSl ](#tts.lib.ethernet.PacketTcp.PacketTcp.macSecSl)
      - [A macSecTci ](#tts.lib.ethernet.PacketTcp.PacketTcp.macSecTci)
      - [A macSecTciAn ](#tts.lib.ethernet.PacketTcp.PacketTcp.macSecTciAn)
      - [A macSecTciC ](#tts.lib.ethernet.PacketTcp.PacketTcp.macSecTciC)
      - [A macSecTciE ](#tts.lib.ethernet.PacketTcp.PacketTcp.macSecTciE)
      - [A macSecTciEs ](#tts.lib.ethernet.PacketTcp.PacketTcp.macSecTciEs)
      - [A macSecTciSc ](#tts.lib.ethernet.PacketTcp.PacketTcp.macSecTciSc)
      - [A macSecTciScb ](#tts.lib.ethernet.PacketTcp.PacketTcp.macSecTciScb)
      - [A macSecTciV ](#tts.lib.ethernet.PacketTcp.PacketTcp.macSecTciV)
      - [A parent ](#tts.lib.ethernet.PacketTcp.PacketTcp.parent)
      - [A timestamp ](#tts.lib.ethernet.PacketTcp.PacketTcp.timestamp)
      - [A vlanCfi ](#tts.lib.ethernet.PacketTcp.PacketTcp.vlanCfi)
      - [A vlanCfiOuter ](#tts.lib.ethernet.PacketTcp.PacketTcp.vlanCfiOuter)
      - [A vlanPcp ](#tts.lib.ethernet.PacketTcp.PacketTcp.vlanPcp)
      - [A vlanPcpOuter ](#tts.lib.ethernet.PacketTcp.PacketTcp.vlanPcpOuter)
      - [A vlanVid ](#tts.lib.ethernet.PacketTcp.PacketTcp.vlanVid)
      - [A vlanVidOuter ](#tts.lib.ethernet.PacketTcp.PacketTcp.vlanVidOuter)
  - [ PacketUdp ](#packetudp)
    - [C PacketUdp ](#tts.lib.ethernet.PacketUdp.PacketUdp)
      - [M CalcUdpLen ](#tts.lib.ethernet.PacketUdp.PacketUdp.CalcUdpLen)
      - [M GetUdpSrc ](#tts.lib.ethernet.PacketUdp.PacketUdp.GetUdpSrc)
      - [M SetUdpSrc ](#tts.lib.ethernet.PacketUdp.PacketUdp.SetUdpSrc)
      - [A udpSrc ](#tts.lib.ethernet.PacketUdp.PacketUdp.udpSrc)
      - [M GetUdpDst ](#tts.lib.ethernet.PacketUdp.PacketUdp.GetUdpDst)
      - [M SetUdpDst ](#tts.lib.ethernet.PacketUdp.PacketUdp.SetUdpDst)
      - [A udpDst ](#tts.lib.ethernet.PacketUdp.PacketUdp.udpDst)
      - [M GetUdpLen ](#tts.lib.ethernet.PacketUdp.PacketUdp.GetUdpLen)
      - [M SetUdpLen ](#tts.lib.ethernet.PacketUdp.PacketUdp.SetUdpLen)
      - [A udpLen ](#tts.lib.ethernet.PacketUdp.PacketUdp.udpLen)
      - [M GetUdpChecksum ](#tts.lib.ethernet.PacketUdp.PacketUdp.GetUdpChecksum)
      - [M SetUdpChecksum ](#tts.lib.ethernet.PacketUdp.PacketUdp.SetUdpChecksum)
      - [A udpChecksum ](#tts.lib.ethernet.PacketUdp.PacketUdp.udpChecksum)
      - [M GetUdpPayload ](#tts.lib.ethernet.PacketUdp.PacketUdp.GetUdpPayload)
      - [M SetUdpPayload ](#tts.lib.ethernet.PacketUdp.PacketUdp.SetUdpPayload)
      - [A udpPayload ](#tts.lib.ethernet.PacketUdp.PacketUdp.udpPayload)
      - [M CalcIpLen ](#tts.lib.ethernet.PacketUdp.PacketUdp.CalcIpLen)
      - [M FindParent ](#tts.lib.ethernet.PacketUdp.PacketUdp.FindParent)
      - [M GetEthDstMac ](#tts.lib.ethernet.PacketUdp.PacketUdp.GetEthDstMac)
      - [M GetEthPayload ](#tts.lib.ethernet.PacketUdp.PacketUdp.GetEthPayload)
      - [M GetEthSrcMac ](#tts.lib.ethernet.PacketUdp.PacketUdp.GetEthSrcMac)
      - [M GetEthType ](#tts.lib.ethernet.PacketUdp.PacketUdp.GetEthType)
      - [M GetIpAhIcv ](#tts.lib.ethernet.PacketUdp.PacketUdp.GetIpAhIcv)
      - [M GetIpAhLen ](#tts.lib.ethernet.PacketUdp.PacketUdp.GetIpAhLen)
      - [M GetIpAhNxt ](#tts.lib.ethernet.PacketUdp.PacketUdp.GetIpAhNxt)
      - [M GetIpAhRsvd ](#tts.lib.ethernet.PacketUdp.PacketUdp.GetIpAhRsvd)
      - [M GetIpAhSeq ](#tts.lib.ethernet.PacketUdp.PacketUdp.GetIpAhSeq)
      - [M GetIpAhSpi ](#tts.lib.ethernet.PacketUdp.PacketUdp.GetIpAhSpi)
      - [M GetIpChecksum ](#tts.lib.ethernet.PacketUdp.PacketUdp.GetIpChecksum)
      - [M GetIpDst ](#tts.lib.ethernet.PacketUdp.PacketUdp.GetIpDst)
      - [M GetIpIdent ](#tts.lib.ethernet.PacketUdp.PacketUdp.GetIpIdent)
      - [M GetIpLen ](#tts.lib.ethernet.PacketUdp.PacketUdp.GetIpLen)
      - [M GetIpOffset ](#tts.lib.ethernet.PacketUdp.PacketUdp.GetIpOffset)
      - [M GetIpPayload ](#tts.lib.ethernet.PacketUdp.PacketUdp.GetIpPayload)
      - [M GetIpProt ](#tts.lib.ethernet.PacketUdp.PacketUdp.GetIpProt)
      - [M GetIpSrc ](#tts.lib.ethernet.PacketUdp.PacketUdp.GetIpSrc)
      - [M GetIpTos ](#tts.lib.ethernet.PacketUdp.PacketUdp.GetIpTos)
      - [M GetIpTtl ](#tts.lib.ethernet.PacketUdp.PacketUdp.GetIpTtl)
      - [M GetIpVersionAndHeaderLength ](#tts.lib.ethernet.PacketUdp.PacketUdp.GetIpVersionAndHeaderLength)
      - [M GetMacSecAn ](#tts.lib.ethernet.PacketUdp.PacketUdp.GetMacSecAn)
      - [M GetMacSecIcv ](#tts.lib.ethernet.PacketUdp.PacketUdp.GetMacSecIcv)
      - [M GetMacSecPn ](#tts.lib.ethernet.PacketUdp.PacketUdp.GetMacSecPn)
      - [M GetMacSecSci ](#tts.lib.ethernet.PacketUdp.PacketUdp.GetMacSecSci)
      - [M GetMacSecSl ](#tts.lib.ethernet.PacketUdp.PacketUdp.GetMacSecSl)
      - [M GetMacSecTci ](#tts.lib.ethernet.PacketUdp.PacketUdp.GetMacSecTci)
      - [M GetMacSecTciAn ](#tts.lib.ethernet.PacketUdp.PacketUdp.GetMacSecTciAn)
      - [M GetMacSecTciC ](#tts.lib.ethernet.PacketUdp.PacketUdp.GetMacSecTciC)
      - [M GetMacSecTciE ](#tts.lib.ethernet.PacketUdp.PacketUdp.GetMacSecTciE)
      - [M GetMacSecTciEs ](#tts.lib.ethernet.PacketUdp.PacketUdp.GetMacSecTciEs)
      - [M GetMacSecTciSc ](#tts.lib.ethernet.PacketUdp.PacketUdp.GetMacSecTciSc)
      - [M GetMacSecTciScb ](#tts.lib.ethernet.PacketUdp.PacketUdp.GetMacSecTciScb)
      - [M GetMacSecTciV ](#tts.lib.ethernet.PacketUdp.PacketUdp.GetMacSecTciV)
      - [M GetTimestamp ](#tts.lib.ethernet.PacketUdp.PacketUdp.GetTimestamp)
      - [M GetVlanCfi ](#tts.lib.ethernet.PacketUdp.PacketUdp.GetVlanCfi)
      - [M GetVlanCfiOuter ](#tts.lib.ethernet.PacketUdp.PacketUdp.GetVlanCfiOuter)
      - [M GetVlanPcp ](#tts.lib.ethernet.PacketUdp.PacketUdp.GetVlanPcp)
      - [M GetVlanPcpOuter ](#tts.lib.ethernet.PacketUdp.PacketUdp.GetVlanPcpOuter)
      - [M GetVlanVid ](#tts.lib.ethernet.PacketUdp.PacketUdp.GetVlanVid)
      - [M GetVlanVidOuter ](#tts.lib.ethernet.PacketUdp.PacketUdp.GetVlanVidOuter)
      - [A PK_CLASS ](#tts.lib.ethernet.PacketUdp.PacketUdp.PK_CLASS)
      - [M SetEthDstMac ](#tts.lib.ethernet.PacketUdp.PacketUdp.SetEthDstMac)
      - [M SetEthPayload ](#tts.lib.ethernet.PacketUdp.PacketUdp.SetEthPayload)
      - [M SetEthSrcMac ](#tts.lib.ethernet.PacketUdp.PacketUdp.SetEthSrcMac)
      - [M SetEthType ](#tts.lib.ethernet.PacketUdp.PacketUdp.SetEthType)
      - [M SetIpChecksum ](#tts.lib.ethernet.PacketUdp.PacketUdp.SetIpChecksum)
      - [M SetIpDst ](#tts.lib.ethernet.PacketUdp.PacketUdp.SetIpDst)
      - [M SetIpIdent ](#tts.lib.ethernet.PacketUdp.PacketUdp.SetIpIdent)
      - [M SetIpLen ](#tts.lib.ethernet.PacketUdp.PacketUdp.SetIpLen)
      - [M SetIpOffset ](#tts.lib.ethernet.PacketUdp.PacketUdp.SetIpOffset)
      - [M SetIpPayload ](#tts.lib.ethernet.PacketUdp.PacketUdp.SetIpPayload)
      - [M SetIpProt ](#tts.lib.ethernet.PacketUdp.PacketUdp.SetIpProt)
      - [M SetIpSrc ](#tts.lib.ethernet.PacketUdp.PacketUdp.SetIpSrc)
      - [M SetIpTos ](#tts.lib.ethernet.PacketUdp.PacketUdp.SetIpTos)
      - [M SetIpTtl ](#tts.lib.ethernet.PacketUdp.PacketUdp.SetIpTtl)
      - [M SetIpVersionAndHeaderLength ](#tts.lib.ethernet.PacketUdp.PacketUdp.SetIpVersionAndHeaderLength)
      - [M SetTimestamp ](#tts.lib.ethernet.PacketUdp.PacketUdp.SetTimestamp)
      - [M SetVlanCfi ](#tts.lib.ethernet.PacketUdp.PacketUdp.SetVlanCfi)
      - [M SetVlanCfiOuter ](#tts.lib.ethernet.PacketUdp.PacketUdp.SetVlanCfiOuter)
      - [M SetVlanPcp ](#tts.lib.ethernet.PacketUdp.PacketUdp.SetVlanPcp)
      - [M SetVlanPcpOuter ](#tts.lib.ethernet.PacketUdp.PacketUdp.SetVlanPcpOuter)
      - [M SetVlanVid ](#tts.lib.ethernet.PacketUdp.PacketUdp.SetVlanVid)
      - [M SetVlanVidOuter ](#tts.lib.ethernet.PacketUdp.PacketUdp.SetVlanVidOuter)
      - [A ethDstMac ](#tts.lib.ethernet.PacketUdp.PacketUdp.ethDstMac)
      - [A ethPayload ](#tts.lib.ethernet.PacketUdp.PacketUdp.ethPayload)
      - [A ethSrcMac ](#tts.lib.ethernet.PacketUdp.PacketUdp.ethSrcMac)
      - [A ethType ](#tts.lib.ethernet.PacketUdp.PacketUdp.ethType)
      - [A ipAhIcv ](#tts.lib.ethernet.PacketUdp.PacketUdp.ipAhIcv)
      - [A ipAhLen ](#tts.lib.ethernet.PacketUdp.PacketUdp.ipAhLen)
      - [A ipAhNxt ](#tts.lib.ethernet.PacketUdp.PacketUdp.ipAhNxt)
      - [A ipAhRsvd ](#tts.lib.ethernet.PacketUdp.PacketUdp.ipAhRsvd)
      - [A ipAhSeq ](#tts.lib.ethernet.PacketUdp.PacketUdp.ipAhSeq)
      - [A ipAhSpi ](#tts.lib.ethernet.PacketUdp.PacketUdp.ipAhSpi)
      - [A ipChecksum ](#tts.lib.ethernet.PacketUdp.PacketUdp.ipChecksum)
      - [A ipDst ](#tts.lib.ethernet.PacketUdp.PacketUdp.ipDst)
      - [A ipIdent ](#tts.lib.ethernet.PacketUdp.PacketUdp.ipIdent)
      - [A ipLen ](#tts.lib.ethernet.PacketUdp.PacketUdp.ipLen)
      - [A ipOffset ](#tts.lib.ethernet.PacketUdp.PacketUdp.ipOffset)
      - [A ipPayload ](#tts.lib.ethernet.PacketUdp.PacketUdp.ipPayload)
      - [A ipProt ](#tts.lib.ethernet.PacketUdp.PacketUdp.ipProt)
      - [A ipSrc ](#tts.lib.ethernet.PacketUdp.PacketUdp.ipSrc)
      - [A ipTos ](#tts.lib.ethernet.PacketUdp.PacketUdp.ipTos)
      - [A ipTtl ](#tts.lib.ethernet.PacketUdp.PacketUdp.ipTtl)
      - [A ipVersionHeader ](#tts.lib.ethernet.PacketUdp.PacketUdp.ipVersionHeader)
      - [A macSecAn ](#tts.lib.ethernet.PacketUdp.PacketUdp.macSecAn)
      - [A macSecIcv ](#tts.lib.ethernet.PacketUdp.PacketUdp.macSecIcv)
      - [A macSecPn ](#tts.lib.ethernet.PacketUdp.PacketUdp.macSecPn)
      - [A macSecSci ](#tts.lib.ethernet.PacketUdp.PacketUdp.macSecSci)
      - [A macSecSl ](#tts.lib.ethernet.PacketUdp.PacketUdp.macSecSl)
      - [A macSecTci ](#tts.lib.ethernet.PacketUdp.PacketUdp.macSecTci)
      - [A macSecTciAn ](#tts.lib.ethernet.PacketUdp.PacketUdp.macSecTciAn)
      - [A macSecTciC ](#tts.lib.ethernet.PacketUdp.PacketUdp.macSecTciC)
      - [A macSecTciE ](#tts.lib.ethernet.PacketUdp.PacketUdp.macSecTciE)
      - [A macSecTciEs ](#tts.lib.ethernet.PacketUdp.PacketUdp.macSecTciEs)
      - [A macSecTciSc ](#tts.lib.ethernet.PacketUdp.PacketUdp.macSecTciSc)
      - [A macSecTciScb ](#tts.lib.ethernet.PacketUdp.PacketUdp.macSecTciScb)
      - [A macSecTciV ](#tts.lib.ethernet.PacketUdp.PacketUdp.macSecTciV)
      - [A parent ](#tts.lib.ethernet.PacketUdp.PacketUdp.parent)
      - [A timestamp ](#tts.lib.ethernet.PacketUdp.PacketUdp.timestamp)
      - [A vlanCfi ](#tts.lib.ethernet.PacketUdp.PacketUdp.vlanCfi)
      - [A vlanCfiOuter ](#tts.lib.ethernet.PacketUdp.PacketUdp.vlanCfiOuter)
      - [A vlanPcp ](#tts.lib.ethernet.PacketUdp.PacketUdp.vlanPcp)
      - [A vlanPcpOuter ](#tts.lib.ethernet.PacketUdp.PacketUdp.vlanPcpOuter)
      - [A vlanVid ](#tts.lib.ethernet.PacketUdp.PacketUdp.vlanVid)
      - [A vlanVidOuter ](#tts.lib.ethernet.PacketUdp.PacketUdp.vlanVidOuter)
  - [ PTP ](#ptp)
    - [ PacketPtpSync ](#packetptpsync)
      - [C PacketPtpSync ](#tts.lib.ethernet.PacketPtp.PacketPtpSync)
        - [M FindParent ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.FindParent)
        - [M GetEthDstMac ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetEthDstMac)
        - [M GetEthPayload ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetEthPayload)
        - [M GetEthSrcMac ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetEthSrcMac)
        - [M GetEthType ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetEthType)
        - [M GetMacSecAn ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetMacSecAn)
        - [M GetMacSecIcv ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetMacSecIcv)
        - [M GetMacSecPn ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetMacSecPn)
        - [M GetMacSecSci ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetMacSecSci)
        - [M GetMacSecSl ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetMacSecSl)
        - [M GetMacSecTci ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetMacSecTci)
        - [M GetMacSecTciAn ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetMacSecTciAn)
        - [M GetMacSecTciC ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetMacSecTciC)
        - [M GetMacSecTciE ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetMacSecTciE)
        - [M GetMacSecTciEs ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetMacSecTciEs)
        - [M GetMacSecTciSc ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetMacSecTciSc)
        - [M GetMacSecTciScb ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetMacSecTciScb)
        - [M GetMacSecTciV ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetMacSecTciV)
        - [M GetPtpControl ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetPtpControl)
        - [M GetPtpCorrectionField ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetPtpCorrectionField)
        - [M GetPtpDomainNumber ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetPtpDomainNumber)
        - [M GetPtpFlags ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetPtpFlags)
        - [M GetPtpLogMsgInterval ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetPtpLogMsgInterval)
        - [M GetPtpMsgLen ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetPtpMsgLen)
        - [M GetPtpMsgType ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetPtpMsgType)
        - [M GetPtpSequenceId ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetPtpSequenceId)
        - [M GetPtpSourcePortIdentity ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetPtpSourcePortIdentity)
        - [M GetPtpVersion ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetPtpVersion)
        - [M GetTimestamp ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetTimestamp)
        - [M GetVlanCfi ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetVlanCfi)
        - [M GetVlanCfiOuter ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetVlanCfiOuter)
        - [M GetVlanPcp ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetVlanPcp)
        - [M GetVlanPcpOuter ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetVlanPcpOuter)
        - [M GetVlanVid ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetVlanVid)
        - [M GetVlanVidOuter ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetVlanVidOuter)
        - [M SetEthDstMac ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetEthDstMac)
        - [M SetEthPayload ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetEthPayload)
        - [M SetEthSrcMac ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetEthSrcMac)
        - [M SetEthType ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetEthType)
        - [M SetPtpControl ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetPtpControl)
        - [M SetPtpCorrectionField ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetPtpCorrectionField)
        - [M SetPtpDomainNumber ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetPtpDomainNumber)
        - [M SetPtpFlags ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetPtpFlags)
        - [M SetPtpLogMsgInterval ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetPtpLogMsgInterval)
        - [M SetPtpMsgLen ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetPtpMsgLen)
        - [M SetPtpMsgType ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetPtpMsgType)
        - [M SetPtpSequenceId ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetPtpSequenceId)
        - [M SetPtpSourcePortIdentity ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetPtpSourcePortIdentity)
        - [M SetPtpVersion ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetPtpVersion)
        - [M SetTimestamp ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetTimestamp)
        - [M SetVlanCfi ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetVlanCfi)
        - [M SetVlanCfiOuter ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetVlanCfiOuter)
        - [M SetVlanPcp ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetVlanPcp)
        - [M SetVlanPcpOuter ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetVlanPcpOuter)
        - [M SetVlanVid ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetVlanVid)
        - [M SetVlanVidOuter ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetVlanVidOuter)
        - [A ethDstMac ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.ethDstMac)
        - [A ethPayload ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.ethPayload)
        - [A ethSrcMac ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.ethSrcMac)
        - [A ethType ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.ethType)
        - [A macSecAn ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.macSecAn)
        - [A macSecIcv ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.macSecIcv)
        - [A macSecPn ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.macSecPn)
        - [A macSecSci ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.macSecSci)
        - [A macSecSl ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.macSecSl)
        - [A macSecTci ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.macSecTci)
        - [A macSecTciAn ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.macSecTciAn)
        - [A macSecTciC ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.macSecTciC)
        - [A macSecTciE ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.macSecTciE)
        - [A macSecTciEs ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.macSecTciEs)
        - [A macSecTciSc ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.macSecTciSc)
        - [A macSecTciScb ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.macSecTciScb)
        - [A macSecTciV ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.macSecTciV)
        - [A parent ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.parent)
        - [A ptpControl ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.ptpControl)
        - [A ptpCorrectionField ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.ptpCorrectionField)
        - [A ptpDomainNumber ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.ptpDomainNumber)
        - [A ptpFlags ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.ptpFlags)
        - [A ptpLogMsgInterval ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.ptpLogMsgInterval)
        - [A ptpMsgLen ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.ptpMsgLen)
        - [A ptpMsgType ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.ptpMsgType)
        - [A ptpSequenceId ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.ptpSequenceId)
        - [A ptpSourcePortIdentity ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.ptpSourcePortIdentity)
        - [A ptpVersion ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.ptpVersion)
        - [A timestamp ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.timestamp)
        - [A vlanCfi ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.vlanCfi)
        - [A vlanCfiOuter ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.vlanCfiOuter)
        - [A vlanPcp ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.vlanPcp)
        - [A vlanPcpOuter ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.vlanPcpOuter)
        - [A vlanVid ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.vlanVid)
        - [A vlanVidOuter ](#tts.lib.ethernet.PacketPtp.PacketPtpSync.vlanVidOuter)
    - [ PacketPtpFollowUp ](#packetptpfollowup)
      - [C PacketPtpFollowUp ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp)
        - [M GetPtpPreciseOriginTimestampSec ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetPtpPreciseOriginTimestampSec)
        - [M SetPtpPreciseOriginTimestampSec ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetPtpPreciseOriginTimestampSec)
        - [A ptpPreciseOriginTimestampSec ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.ptpPreciseOriginTimestampSec)
        - [M GetPtpPreciseOriginTimestampNSec ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetPtpPreciseOriginTimestampNSec)
        - [M SetPtpPreciseOriginTimestampNSec ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetPtpPreciseOriginTimestampNSec)
        - [A ptpPreciseOriginTimestampNSec ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.ptpPreciseOriginTimestampNSec)
        - [M FindParent ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.FindParent)
        - [M GetEthDstMac ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetEthDstMac)
        - [M GetEthPayload ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetEthPayload)
        - [M GetEthSrcMac ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetEthSrcMac)
        - [M GetEthType ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetEthType)
        - [M GetMacSecAn ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetMacSecAn)
        - [M GetMacSecIcv ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetMacSecIcv)
        - [M GetMacSecPn ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetMacSecPn)
        - [M GetMacSecSci ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetMacSecSci)
        - [M GetMacSecSl ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetMacSecSl)
        - [M GetMacSecTci ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetMacSecTci)
        - [M GetMacSecTciAn ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetMacSecTciAn)
        - [M GetMacSecTciC ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetMacSecTciC)
        - [M GetMacSecTciE ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetMacSecTciE)
        - [M GetMacSecTciEs ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetMacSecTciEs)
        - [M GetMacSecTciSc ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetMacSecTciSc)
        - [M GetMacSecTciScb ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetMacSecTciScb)
        - [M GetMacSecTciV ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetMacSecTciV)
        - [M GetPtpControl ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetPtpControl)
        - [M GetPtpCorrectionField ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetPtpCorrectionField)
        - [M GetPtpDomainNumber ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetPtpDomainNumber)
        - [M GetPtpFlags ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetPtpFlags)
        - [M GetPtpLogMsgInterval ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetPtpLogMsgInterval)
        - [M GetPtpMsgLen ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetPtpMsgLen)
        - [M GetPtpMsgType ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetPtpMsgType)
        - [M GetPtpSequenceId ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetPtpSequenceId)
        - [M GetPtpSourcePortIdentity ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetPtpSourcePortIdentity)
        - [M GetPtpVersion ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetPtpVersion)
        - [M GetTimestamp ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetTimestamp)
        - [M GetVlanCfi ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetVlanCfi)
        - [M GetVlanCfiOuter ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetVlanCfiOuter)
        - [M GetVlanPcp ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetVlanPcp)
        - [M GetVlanPcpOuter ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetVlanPcpOuter)
        - [M GetVlanVid ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetVlanVid)
        - [M GetVlanVidOuter ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetVlanVidOuter)
        - [M SetEthDstMac ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetEthDstMac)
        - [M SetEthPayload ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetEthPayload)
        - [M SetEthSrcMac ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetEthSrcMac)
        - [M SetEthType ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetEthType)
        - [M SetPtpControl ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetPtpControl)
        - [M SetPtpCorrectionField ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetPtpCorrectionField)
        - [M SetPtpDomainNumber ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetPtpDomainNumber)
        - [M SetPtpFlags ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetPtpFlags)
        - [M SetPtpLogMsgInterval ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetPtpLogMsgInterval)
        - [M SetPtpMsgLen ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetPtpMsgLen)
        - [M SetPtpMsgType ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetPtpMsgType)
        - [M SetPtpSequenceId ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetPtpSequenceId)
        - [M SetPtpSourcePortIdentity ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetPtpSourcePortIdentity)
        - [M SetPtpVersion ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetPtpVersion)
        - [M SetTimestamp ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetTimestamp)
        - [M SetVlanCfi ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetVlanCfi)
        - [M SetVlanCfiOuter ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetVlanCfiOuter)
        - [M SetVlanPcp ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetVlanPcp)
        - [M SetVlanPcpOuter ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetVlanPcpOuter)
        - [M SetVlanVid ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetVlanVid)
        - [M SetVlanVidOuter ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetVlanVidOuter)
        - [A ethDstMac ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.ethDstMac)
        - [A ethPayload ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.ethPayload)
        - [A ethSrcMac ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.ethSrcMac)
        - [A ethType ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.ethType)
        - [A macSecAn ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.macSecAn)
        - [A macSecIcv ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.macSecIcv)
        - [A macSecPn ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.macSecPn)
        - [A macSecSci ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.macSecSci)
        - [A macSecSl ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.macSecSl)
        - [A macSecTci ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.macSecTci)
        - [A macSecTciAn ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.macSecTciAn)
        - [A macSecTciC ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.macSecTciC)
        - [A macSecTciE ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.macSecTciE)
        - [A macSecTciEs ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.macSecTciEs)
        - [A macSecTciSc ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.macSecTciSc)
        - [A macSecTciScb ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.macSecTciScb)
        - [A macSecTciV ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.macSecTciV)
        - [A parent ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.parent)
        - [A ptpControl ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.ptpControl)
        - [A ptpCorrectionField ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.ptpCorrectionField)
        - [A ptpDomainNumber ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.ptpDomainNumber)
        - [A ptpFlags ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.ptpFlags)
        - [A ptpLogMsgInterval ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.ptpLogMsgInterval)
        - [A ptpMsgLen ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.ptpMsgLen)
        - [A ptpMsgType ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.ptpMsgType)
        - [A ptpSequenceId ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.ptpSequenceId)
        - [A ptpSourcePortIdentity ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.ptpSourcePortIdentity)
        - [A ptpVersion ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.ptpVersion)
        - [A timestamp ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.timestamp)
        - [A vlanCfi ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.vlanCfi)
        - [A vlanCfiOuter ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.vlanCfiOuter)
        - [A vlanPcp ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.vlanPcp)
        - [A vlanPcpOuter ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.vlanPcpOuter)
        - [A vlanVid ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.vlanVid)
        - [A vlanVidOuter ](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.vlanVidOuter)
    - [ PacketPdelayReq ](#packetpdelayreq)
      - [C PacketPdelayReq ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq)
        - [M FindParent ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.FindParent)
        - [M GetEthDstMac ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetEthDstMac)
        - [M GetEthPayload ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetEthPayload)
        - [M GetEthSrcMac ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetEthSrcMac)
        - [M GetEthType ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetEthType)
        - [M GetMacSecAn ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetMacSecAn)
        - [M GetMacSecIcv ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetMacSecIcv)
        - [M GetMacSecPn ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetMacSecPn)
        - [M GetMacSecSci ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetMacSecSci)
        - [M GetMacSecSl ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetMacSecSl)
        - [M GetMacSecTci ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetMacSecTci)
        - [M GetMacSecTciAn ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetMacSecTciAn)
        - [M GetMacSecTciC ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetMacSecTciC)
        - [M GetMacSecTciE ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetMacSecTciE)
        - [M GetMacSecTciEs ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetMacSecTciEs)
        - [M GetMacSecTciSc ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetMacSecTciSc)
        - [M GetMacSecTciScb ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetMacSecTciScb)
        - [M GetMacSecTciV ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetMacSecTciV)
        - [M GetPtpControl ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetPtpControl)
        - [M GetPtpCorrectionField ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetPtpCorrectionField)
        - [M GetPtpDomainNumber ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetPtpDomainNumber)
        - [M GetPtpFlags ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetPtpFlags)
        - [M GetPtpLogMsgInterval ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetPtpLogMsgInterval)
        - [M GetPtpMsgLen ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetPtpMsgLen)
        - [M GetPtpMsgType ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetPtpMsgType)
        - [M GetPtpSequenceId ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetPtpSequenceId)
        - [M GetPtpSourcePortIdentity ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetPtpSourcePortIdentity)
        - [M GetPtpVersion ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetPtpVersion)
        - [M GetTimestamp ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetTimestamp)
        - [M GetVlanCfi ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetVlanCfi)
        - [M GetVlanCfiOuter ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetVlanCfiOuter)
        - [M GetVlanPcp ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetVlanPcp)
        - [M GetVlanPcpOuter ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetVlanPcpOuter)
        - [M GetVlanVid ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetVlanVid)
        - [M GetVlanVidOuter ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetVlanVidOuter)
        - [M SetEthDstMac ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetEthDstMac)
        - [M SetEthPayload ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetEthPayload)
        - [M SetEthSrcMac ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetEthSrcMac)
        - [M SetEthType ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetEthType)
        - [M SetPtpControl ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetPtpControl)
        - [M SetPtpCorrectionField ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetPtpCorrectionField)
        - [M SetPtpDomainNumber ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetPtpDomainNumber)
        - [M SetPtpFlags ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetPtpFlags)
        - [M SetPtpLogMsgInterval ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetPtpLogMsgInterval)
        - [M SetPtpMsgLen ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetPtpMsgLen)
        - [M SetPtpMsgType ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetPtpMsgType)
        - [M SetPtpSequenceId ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetPtpSequenceId)
        - [M SetPtpSourcePortIdentity ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetPtpSourcePortIdentity)
        - [M SetPtpVersion ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetPtpVersion)
        - [M SetTimestamp ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetTimestamp)
        - [M SetVlanCfi ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetVlanCfi)
        - [M SetVlanCfiOuter ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetVlanCfiOuter)
        - [M SetVlanPcp ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetVlanPcp)
        - [M SetVlanPcpOuter ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetVlanPcpOuter)
        - [M SetVlanVid ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetVlanVid)
        - [M SetVlanVidOuter ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetVlanVidOuter)
        - [A ethDstMac ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.ethDstMac)
        - [A ethPayload ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.ethPayload)
        - [A ethSrcMac ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.ethSrcMac)
        - [A ethType ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.ethType)
        - [A macSecAn ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.macSecAn)
        - [A macSecIcv ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.macSecIcv)
        - [A macSecPn ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.macSecPn)
        - [A macSecSci ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.macSecSci)
        - [A macSecSl ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.macSecSl)
        - [A macSecTci ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.macSecTci)
        - [A macSecTciAn ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.macSecTciAn)
        - [A macSecTciC ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.macSecTciC)
        - [A macSecTciE ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.macSecTciE)
        - [A macSecTciEs ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.macSecTciEs)
        - [A macSecTciSc ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.macSecTciSc)
        - [A macSecTciScb ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.macSecTciScb)
        - [A macSecTciV ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.macSecTciV)
        - [A parent ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.parent)
        - [A ptpControl ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.ptpControl)
        - [A ptpCorrectionField ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.ptpCorrectionField)
        - [A ptpDomainNumber ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.ptpDomainNumber)
        - [A ptpFlags ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.ptpFlags)
        - [A ptpLogMsgInterval ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.ptpLogMsgInterval)
        - [A ptpMsgLen ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.ptpMsgLen)
        - [A ptpMsgType ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.ptpMsgType)
        - [A ptpSequenceId ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.ptpSequenceId)
        - [A ptpSourcePortIdentity ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.ptpSourcePortIdentity)
        - [A ptpVersion ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.ptpVersion)
        - [A timestamp ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.timestamp)
        - [A vlanCfi ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.vlanCfi)
        - [A vlanCfiOuter ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.vlanCfiOuter)
        - [A vlanPcp ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.vlanPcp)
        - [A vlanPcpOuter ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.vlanPcpOuter)
        - [A vlanVid ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.vlanVid)
        - [A vlanVidOuter ](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.vlanVidOuter)
    - [ PacketPdelayResp ](#packetpdelayresp)
      - [C PacketPdelayResp ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp)
        - [M GetPtpRequestReceiptTimestampSec ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetPtpRequestReceiptTimestampSec)
        - [M SetPtpRequestReceiptTimestampSec ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetPtpRequestReceiptTimestampSec)
        - [A ptpRequestReceiptTimestampSec ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.ptpRequestReceiptTimestampSec)
        - [M GetPtpRequestReceiptTimestampNSec ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetPtpRequestReceiptTimestampNSec)
        - [M SetPtpRequestReceiptTimestampNSec ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetPtpRequestReceiptTimestampNSec)
        - [A ptpRequestReceiptTimestampNSec ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.ptpRequestReceiptTimestampNSec)
        - [M GetPtpRequestingPortIdentity ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetPtpRequestingPortIdentity)
        - [M SetPtpRequestingPortIdentity ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetPtpRequestingPortIdentity)
        - [A ptpRequestingPortIdentity ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.ptpRequestingPortIdentity)
        - [M FindParent ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.FindParent)
        - [M GetEthDstMac ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetEthDstMac)
        - [M GetEthPayload ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetEthPayload)
        - [M GetEthSrcMac ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetEthSrcMac)
        - [M GetEthType ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetEthType)
        - [M GetMacSecAn ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetMacSecAn)
        - [M GetMacSecIcv ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetMacSecIcv)
        - [M GetMacSecPn ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetMacSecPn)
        - [M GetMacSecSci ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetMacSecSci)
        - [M GetMacSecSl ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetMacSecSl)
        - [M GetMacSecTci ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetMacSecTci)
        - [M GetMacSecTciAn ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetMacSecTciAn)
        - [M GetMacSecTciC ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetMacSecTciC)
        - [M GetMacSecTciE ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetMacSecTciE)
        - [M GetMacSecTciEs ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetMacSecTciEs)
        - [M GetMacSecTciSc ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetMacSecTciSc)
        - [M GetMacSecTciScb ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetMacSecTciScb)
        - [M GetMacSecTciV ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetMacSecTciV)
        - [M GetPtpControl ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetPtpControl)
        - [M GetPtpCorrectionField ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetPtpCorrectionField)
        - [M GetPtpDomainNumber ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetPtpDomainNumber)
        - [M GetPtpFlags ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetPtpFlags)
        - [M GetPtpLogMsgInterval ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetPtpLogMsgInterval)
        - [M GetPtpMsgLen ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetPtpMsgLen)
        - [M GetPtpMsgType ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetPtpMsgType)
        - [M GetPtpSequenceId ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetPtpSequenceId)
        - [M GetPtpSourcePortIdentity ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetPtpSourcePortIdentity)
        - [M GetPtpVersion ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetPtpVersion)
        - [M GetTimestamp ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetTimestamp)
        - [M GetVlanCfi ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetVlanCfi)
        - [M GetVlanCfiOuter ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetVlanCfiOuter)
        - [M GetVlanPcp ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetVlanPcp)
        - [M GetVlanPcpOuter ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetVlanPcpOuter)
        - [M GetVlanVid ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetVlanVid)
        - [M GetVlanVidOuter ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetVlanVidOuter)
        - [M SetEthDstMac ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetEthDstMac)
        - [M SetEthPayload ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetEthPayload)
        - [M SetEthSrcMac ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetEthSrcMac)
        - [M SetEthType ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetEthType)
        - [M SetPtpControl ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetPtpControl)
        - [M SetPtpCorrectionField ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetPtpCorrectionField)
        - [M SetPtpDomainNumber ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetPtpDomainNumber)
        - [M SetPtpFlags ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetPtpFlags)
        - [M SetPtpLogMsgInterval ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetPtpLogMsgInterval)
        - [M SetPtpMsgLen ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetPtpMsgLen)
        - [M SetPtpMsgType ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetPtpMsgType)
        - [M SetPtpSequenceId ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetPtpSequenceId)
        - [M SetPtpSourcePortIdentity ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetPtpSourcePortIdentity)
        - [M SetPtpVersion ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetPtpVersion)
        - [M SetTimestamp ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetTimestamp)
        - [M SetVlanCfi ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetVlanCfi)
        - [M SetVlanCfiOuter ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetVlanCfiOuter)
        - [M SetVlanPcp ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetVlanPcp)
        - [M SetVlanPcpOuter ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetVlanPcpOuter)
        - [M SetVlanVid ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetVlanVid)
        - [M SetVlanVidOuter ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetVlanVidOuter)
        - [A ethDstMac ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.ethDstMac)
        - [A ethPayload ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.ethPayload)
        - [A ethSrcMac ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.ethSrcMac)
        - [A ethType ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.ethType)
        - [A macSecAn ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.macSecAn)
        - [A macSecIcv ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.macSecIcv)
        - [A macSecPn ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.macSecPn)
        - [A macSecSci ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.macSecSci)
        - [A macSecSl ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.macSecSl)
        - [A macSecTci ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.macSecTci)
        - [A macSecTciAn ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.macSecTciAn)
        - [A macSecTciC ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.macSecTciC)
        - [A macSecTciE ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.macSecTciE)
        - [A macSecTciEs ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.macSecTciEs)
        - [A macSecTciSc ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.macSecTciSc)
        - [A macSecTciScb ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.macSecTciScb)
        - [A macSecTciV ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.macSecTciV)
        - [A parent ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.parent)
        - [A ptpControl ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.ptpControl)
        - [A ptpCorrectionField ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.ptpCorrectionField)
        - [A ptpDomainNumber ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.ptpDomainNumber)
        - [A ptpFlags ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.ptpFlags)
        - [A ptpLogMsgInterval ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.ptpLogMsgInterval)
        - [A ptpMsgLen ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.ptpMsgLen)
        - [A ptpMsgType ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.ptpMsgType)
        - [A ptpSequenceId ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.ptpSequenceId)
        - [A ptpSourcePortIdentity ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.ptpSourcePortIdentity)
        - [A ptpVersion ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.ptpVersion)
        - [A timestamp ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.timestamp)
        - [A vlanCfi ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.vlanCfi)
        - [A vlanCfiOuter ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.vlanCfiOuter)
        - [A vlanPcp ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.vlanPcp)
        - [A vlanPcpOuter ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.vlanPcpOuter)
        - [A vlanVid ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.vlanVid)
        - [A vlanVidOuter ](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.vlanVidOuter)
    - [ PacketPdelayRespFollowUp ](#packetpdelayrespfollowup)
      - [C PacketPdelayRespFollowUp ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp)
        - [M GetPtpResponseOriginTimestampSec ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetPtpResponseOriginTimestampSec)
        - [M SetPtpResponseOriginTimestampSec ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetPtpResponseOriginTimestampSec)
        - [A ptpResponseOriginTimestampSec ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.ptpResponseOriginTimestampSec)
        - [M GetPtpResponseOriginTimestampNSec ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetPtpResponseOriginTimestampNSec)
        - [M SetPtpResponseOriginTimestampNSec ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetPtpResponseOriginTimestampNSec)
        - [A ptpResponseOriginTimestampNSec ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.ptpResponseOriginTimestampNSec)
        - [M GetPtpRequestingPortIdentity ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetPtpRequestingPortIdentity)
        - [M SetPtpRequestingPortIdentity ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetPtpRequestingPortIdentity)
        - [A ptpRequestingPortIdentity ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.ptpRequestingPortIdentity)
        - [M FindParent ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.FindParent)
        - [M GetEthDstMac ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetEthDstMac)
        - [M GetEthPayload ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetEthPayload)
        - [M GetEthSrcMac ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetEthSrcMac)
        - [M GetEthType ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetEthType)
        - [M GetMacSecAn ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetMacSecAn)
        - [M GetMacSecIcv ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetMacSecIcv)
        - [M GetMacSecPn ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetMacSecPn)
        - [M GetMacSecSci ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetMacSecSci)
        - [M GetMacSecSl ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetMacSecSl)
        - [M GetMacSecTci ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetMacSecTci)
        - [M GetMacSecTciAn ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetMacSecTciAn)
        - [M GetMacSecTciC ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetMacSecTciC)
        - [M GetMacSecTciE ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetMacSecTciE)
        - [M GetMacSecTciEs ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetMacSecTciEs)
        - [M GetMacSecTciSc ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetMacSecTciSc)
        - [M GetMacSecTciScb ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetMacSecTciScb)
        - [M GetMacSecTciV ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetMacSecTciV)
        - [M GetPtpControl ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetPtpControl)
        - [M GetPtpCorrectionField ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetPtpCorrectionField)
        - [M GetPtpDomainNumber ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetPtpDomainNumber)
        - [M GetPtpFlags ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetPtpFlags)
        - [M GetPtpLogMsgInterval ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetPtpLogMsgInterval)
        - [M GetPtpMsgLen ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetPtpMsgLen)
        - [M GetPtpMsgType ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetPtpMsgType)
        - [M GetPtpSequenceId ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetPtpSequenceId)
        - [M GetPtpSourcePortIdentity ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetPtpSourcePortIdentity)
        - [M GetPtpVersion ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetPtpVersion)
        - [M GetTimestamp ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetTimestamp)
        - [M GetVlanCfi ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetVlanCfi)
        - [M GetVlanCfiOuter ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetVlanCfiOuter)
        - [M GetVlanPcp ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetVlanPcp)
        - [M GetVlanPcpOuter ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetVlanPcpOuter)
        - [M GetVlanVid ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetVlanVid)
        - [M GetVlanVidOuter ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetVlanVidOuter)
        - [M SetEthDstMac ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetEthDstMac)
        - [M SetEthPayload ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetEthPayload)
        - [M SetEthSrcMac ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetEthSrcMac)
        - [M SetEthType ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetEthType)
        - [M SetPtpControl ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetPtpControl)
        - [M SetPtpCorrectionField ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetPtpCorrectionField)
        - [M SetPtpDomainNumber ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetPtpDomainNumber)
        - [M SetPtpFlags ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetPtpFlags)
        - [M SetPtpLogMsgInterval ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetPtpLogMsgInterval)
        - [M SetPtpMsgLen ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetPtpMsgLen)
        - [M SetPtpMsgType ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetPtpMsgType)
        - [M SetPtpSequenceId ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetPtpSequenceId)
        - [M SetPtpSourcePortIdentity ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetPtpSourcePortIdentity)
        - [M SetPtpVersion ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetPtpVersion)
        - [M SetTimestamp ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetTimestamp)
        - [M SetVlanCfi ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetVlanCfi)
        - [M SetVlanCfiOuter ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetVlanCfiOuter)
        - [M SetVlanPcp ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetVlanPcp)
        - [M SetVlanPcpOuter ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetVlanPcpOuter)
        - [M SetVlanVid ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetVlanVid)
        - [M SetVlanVidOuter ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetVlanVidOuter)
        - [A ethDstMac ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.ethDstMac)
        - [A ethPayload ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.ethPayload)
        - [A ethSrcMac ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.ethSrcMac)
        - [A ethType ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.ethType)
        - [A macSecAn ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.macSecAn)
        - [A macSecIcv ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.macSecIcv)
        - [A macSecPn ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.macSecPn)
        - [A macSecSci ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.macSecSci)
        - [A macSecSl ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.macSecSl)
        - [A macSecTci ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.macSecTci)
        - [A macSecTciAn ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.macSecTciAn)
        - [A macSecTciC ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.macSecTciC)
        - [A macSecTciE ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.macSecTciE)
        - [A macSecTciEs ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.macSecTciEs)
        - [A macSecTciSc ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.macSecTciSc)
        - [A macSecTciScb ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.macSecTciScb)
        - [A macSecTciV ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.macSecTciV)
        - [A parent ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.parent)
        - [A ptpControl ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.ptpControl)
        - [A ptpCorrectionField ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.ptpCorrectionField)
        - [A ptpDomainNumber ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.ptpDomainNumber)
        - [A ptpFlags ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.ptpFlags)
        - [A ptpLogMsgInterval ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.ptpLogMsgInterval)
        - [A ptpMsgLen ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.ptpMsgLen)
        - [A ptpMsgType ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.ptpMsgType)
        - [A ptpSequenceId ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.ptpSequenceId)
        - [A ptpSourcePortIdentity ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.ptpSourcePortIdentity)
        - [A ptpVersion ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.ptpVersion)
        - [A timestamp ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.timestamp)
        - [A vlanCfi ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.vlanCfi)
        - [A vlanCfiOuter ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.vlanCfiOuter)
        - [A vlanPcp ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.vlanPcp)
        - [A vlanPcpOuter ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.vlanPcpOuter)
        - [A vlanVid ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.vlanVid)
        - [A vlanVidOuter ](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.vlanVidOuter)
  - [ SOME/IP ](#some-ip)
    - [ PacketSomeIp ](#packetsomeip)
      - [C PacketSomeIp ](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp)
        - [A SOMEIP_MSG_REQUEST ](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.SOMEIP_MSG_REQUEST)
        - [A SOMEIP_MSG_REQUEST_NO_RETURN ](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.SOMEIP_MSG_REQUEST_NO_RETURN)
        - [A SOMEIP_MSG_NOTIFICATION ](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.SOMEIP_MSG_NOTIFICATION)
        - [A SOMEIP_MSG_TP ](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.SOMEIP_MSG_TP)
        - [A SOMEIP_MSG_RESPONSE ](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.SOMEIP_MSG_RESPONSE)
        - [A SOMEIP_MSG_ERROR ](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.SOMEIP_MSG_ERROR)
        - [A SOMEIP_RETURN_OK ](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.SOMEIP_RETURN_OK)
        - [A SOMEIP_RETURN_NOT_OK ](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.SOMEIP_RETURN_NOT_OK)
        - [A SOMEIP_RETURN_UNKNOWN_SERVICE ](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.SOMEIP_RETURN_UNKNOWN_SERVICE)
        - [A SOMEIP_RETURN_UNKNOWN_METHOD ](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.SOMEIP_RETURN_UNKNOWN_METHOD)
        - [A SOMEIP_RETURN_NOT_READY ](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.SOMEIP_RETURN_NOT_READY)
        - [A SOMEIP_RETURN_NOT_REACHABLE ](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.SOMEIP_RETURN_NOT_REACHABLE)
        - [A SOMEIP_RETURN_TIMEOUT ](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.SOMEIP_RETURN_TIMEOUT)
        - [A SOMEIP_RETURN_WRONG_PROTOCOL_VERSION ](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.SOMEIP_RETURN_WRONG_PROTOCOL_VERSION)
        - [A SOMEIP_RETURN_WRONG_INTERFACE_VERSION ](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.SOMEIP_RETURN_WRONG_INTERFACE_VERSION)
        - [A SOMEIP_RETURN_MALFORMED ](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.SOMEIP_RETURN_MALFORMED)
        - [A SOMEIP_RETURN_TCP_ERROR ](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.SOMEIP_RETURN_TCP_ERROR)
        - [M GetSomeIpMessagesFromPayload ](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.GetSomeIpMessagesFromPayload)
        - [M Create ](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.Create)
        - [M CalcLen ](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.CalcLen)
        - [A messageId ](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.messageId)
        - [A serviceId ](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.serviceId)
        - [A methodId ](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.methodId)
        - [A length ](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.length)
        - [A requestId ](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.requestId)
        - [A clientId ](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.clientId)
        - [A sessionId ](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.sessionId)
        - [A protocolVersion ](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.protocolVersion)
        - [A interfaceVersion ](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.interfaceVersion)
        - [A messageType ](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.messageType)
        - [A returnCode ](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.returnCode)
        - [A payload ](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.payload)
        - [M GetHeaderBytes ](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.GetHeaderBytes)
        - [A instanceIds ](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.instanceIds)
        - [M FindParent ](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.FindParent)
        - [A parent ](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.parent)
        - [A timestamp ](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.timestamp)
    - [ PacketSomeIpSd ](#packetsomeipsd)
      - [C PacketSomeIpSd ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSd)
        - [M `\_\_init\_\_` ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSd.__init__)
        - [M CalcEntryArrayLen ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSd.CalcEntryArrayLen)
        - [M CalcOptionArrayLen ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSd.CalcOptionArrayLen)
        - [M Create ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSd.Create)
        - [M FindParent ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSd.FindParent)
        - [A entryLen ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSd.entryLen)
        - [A entryList ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSd.entryList)
        - [A optionLen ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSd.optionLen)
        - [A optionList ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSd.optionList)
        - [A parent ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSd.parent)
        - [A rebootFlag ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSd.rebootFlag)
        - [A timestamp ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSd.timestamp)
        - [A unicastFlag ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSd.unicastFlag)
    - [ PacketSomeIpSdEntry ](#packetsomeipsdentry)
      - [C PacketSomeIpSdEntry ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntry)
        - [A index1 ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntry.index1)
        - [A index2 ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntry.index2)
        - [A instanceId ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntry.instanceId)
        - [A majorVersion ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntry.majorVersion)
        - [A optionCount1 ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntry.optionCount1)
        - [A optionCount2 ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntry.optionCount2)
        - [A serviceId ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntry.serviceId)
        - [A ttl ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntry.ttl)
        - [A type ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntry.type)
    - [ PacketSomeIpSdEntryService ](#packetsomeipsdentryservice)
      - [C PacketSomeIpSdEntryService ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryService)
        - [A SERVICE_FIND ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryService.SERVICE_FIND)
        - [A SERVICE_OFFER ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryService.SERVICE_OFFER)
        - [A SERVICE_STOP_OFFER ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryService.SERVICE_STOP_OFFER)
        - [M Create ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryService.Create)
        - [A minorVersion ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryService.minorVersion)
    - [ PacketSomeIpSdEntryEventgroup ](#packetsomeipsdentryeventgroup)
      - [C PacketSomeIpSdEntryEventgroup ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryEventgroup)
        - [A EVENTGROUP_SUBSCRIBE ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryEventgroup.EVENTGROUP_SUBSCRIBE)
        - [A EVENTGROUP_SUBSCRIBE_ACK ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryEventgroup.EVENTGROUP_SUBSCRIBE_ACK)
        - [A EVENTGROUP_STOP_SUBSCRIBE ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryEventgroup.EVENTGROUP_STOP_SUBSCRIBE)
        - [A EVENTGROUP_SUBSCRIBE_NACK ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryEventgroup.EVENTGROUP_SUBSCRIBE_NACK)
        - [M Create ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryEventgroup.Create)
        - [A eventgroupId ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryEventgroup.eventgroupId)
    - [ PacketSomeIpSdOption ](#packetsomeipsdoption)
      - [C PacketSomeIpSdOption ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOption)
        - [A TRANSPORT_TCP ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOption.TRANSPORT_TCP)
        - [A TRANSPORT_UDP ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOption.TRANSPORT_UDP)
        - [A PACKET_SOME_IP_SD_OPTION_CONFIG ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOption.PACKET_SOME_IP_SD_OPTION_CONFIG)
        - [A PACKET_SOME_IP_SD_OPTION_IPV4 ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOption.PACKET_SOME_IP_SD_OPTION_IPV4)
        - [A PACKET_SOME_IP_SD_OPTION_IPV6 ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOption.PACKET_SOME_IP_SD_OPTION_IPV6)
        - [A PACKET_SOME_IP_SD_OPTION_IPV4_MULTICAST ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOption.PACKET_SOME_IP_SD_OPTION_IPV4_MULTICAST)
        - [A PACKET_SOME_IP_SD_OPTION_IPV4_SD ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOption.PACKET_SOME_IP_SD_OPTION_IPV4_SD)
        - [A PACKET_SOME_IP_SD_OPTION_IPV6_MULTICAST ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOption.PACKET_SOME_IP_SD_OPTION_IPV6_MULTICAST)
        - [A PACKET_SOME_IP_SD_OPTION_IPV6_SD ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOption.PACKET_SOME_IP_SD_OPTION_IPV6_SD)
        - [A optionLen ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOption.optionLen)
        - [A type ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOption.type)
    - [ PacketSomeIpSdOptionIpv4 ](#packetsomeipsdoptionipv4)
      - [C PacketSomeIpSdOptionIpv4 ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4)
        - [M Create ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4.Create)
        - [A ip ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4.ip)
        - [A optionLen ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4.optionLen)
        - [A port ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4.port)
        - [A protocol ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4.protocol)
    - [ PacketSomeIpSdOptionIpv6 ](#packetsomeipsdoptionipv6)
      - [C PacketSomeIpSdOptionIpv6 ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6)
        - [M Create ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6.Create)
        - [A ip ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6.ip)
        - [A optionLen ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6.optionLen)
        - [A port ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6.port)
        - [A protocol ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6.protocol)
    - [ PacketSomeIpSdOptionIpv4Multicast ](#packetsomeipsdoptionipv4multicast)
      - [C PacketSomeIpSdOptionIpv4Multicast ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4Multicast)
        - [M Create ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4Multicast.Create)
        - [A ip ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4Multicast.ip)
        - [A optionLen ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4Multicast.optionLen)
        - [A port ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4Multicast.port)
        - [A protocol ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4Multicast.protocol)
    - [ PacketSomeIpSdOptionIpv6Multicast ](#packetsomeipsdoptionipv6multicast)
      - [C PacketSomeIpSdOptionIpv6Multicast ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6Multicast)
        - [M Create ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6Multicast.Create)
        - [A ip ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6Multicast.ip)
        - [A optionLen ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6Multicast.optionLen)
        - [A port ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6Multicast.port)
        - [A protocol ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6Multicast.protocol)
    - [ PacketSomeIpSdOptionIpv4SD ](#packetsomeipsdoptionipv4sd)
      - [C PacketSomeIpSdOptionIpv4SD ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4SD)
        - [M Create ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4SD.Create)
        - [A ip ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4SD.ip)
        - [A optionLen ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4SD.optionLen)
        - [A port ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4SD.port)
        - [A protocol ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4SD.protocol)
    - [ PacketSomeIpSdOptionIpv6SD ](#packetsomeipsdoptionipv6sd)
      - [C PacketSomeIpSdOptionIpv6SD ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6SD)
        - [M Create ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6SD.Create)
        - [A ip ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6SD.ip)
        - [A optionLen ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6SD.optionLen)
        - [A port ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6SD.port)
        - [A protocol ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6SD.protocol)
    - [ PacketSomeIpSdOptionConfig ](#packetsomeipsdoptionconfig)
      - [C PacketSomeIpSdOptionConfig ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionConfig)
        - [M Create ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionConfig.Create)
        - [A config ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionConfig.config)
        - [A optionLen ](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionConfig.optionLen)

# Advanced properties of bus-related objects[¶](#advanced-properties-of-bus-related-objects "Link to this heading")

## CAN[¶](#can "Link to this heading")

*class* CanFrame[¶](#tts.testModule.bus.busObjects.CAN.CanFrame "Link to this definition")  

canID[¶](#tts.testModule.bus.busObjects.CAN.CanFrame.canID "Link to this definition")  
The CAN ID of the Frame

Type:  int

flags : [CanFlags](#tts.testModule.bus.busObjects.CAN.CanFlags "tts.testModule.bus.busObjects.CAN.CanFlags (Python class) — Is this an error frame?")[¶](#tts.testModule.bus.busObjects.CAN.CanFrame.flags "Link to this definition")  
Any of the frame’s flags defined in the corresponding flags class can be accessed directly on the frame object, i.e. theFrame.aFlag instead of theFrame.flags.aFlag

Some of the flags can take the value False if the driver does not support the respective attribute.

Type:  [`CanFlags`](#tts.testModule.bus.busObjects.CAN.CanFlags "tts.testModule.bus.busObjects.CAN.CanFlags (Python class) — Is this an error frame?")

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

Type:  [`FlexRayFlags`](#tts.testModule.bus.busObjects.FlexRay.FlexRayFlags "tts.testModule.bus.busObjects.FlexRay.FlexRayFlags (Python class) — Was this frame sent by the controller that received it?")

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

Type:  [`LinFlags`](#tts.testModule.bus.busObjects.LIN.LinFlags "tts.testModule.bus.busObjects.LIN.LinFlags (Python class) — Does this frame have a CRC error?")

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

UDP = `17`[¶](#tts.core.api.internalApi.Ethernet.Ethernet.UDP "Link to this definition")  

TCP = `6`[¶](#tts.core.api.internalApi.Ethernet.Ethernet.TCP "Link to this definition")  

PacketEthernet[¶](#tts.core.api.internalApi.Ethernet.Ethernet.PacketEthernet "Link to this definition")  
[`PacketEthernet`](#tts.lib.ethernet.PacketEthernet.PacketEthernet "tts.lib.ethernet.PacketEthernet.PacketEthernet (Python class) — In the test case, use api.Ethernet.PacketEthernet; in UserPyModules, use from tts.lib.ethernet.PacketEthernet import PacketEthernet.")

PacketIp4[¶](#tts.core.api.internalApi.Ethernet.Ethernet.PacketIp4 "Link to this definition")  
[`PacketIp4`](#tts.lib.ethernet.PacketIp4.PacketIp4 "tts.lib.ethernet.PacketIp4.PacketIp4 (Python class) — In the test case, use api.Ethernet.PacPacketIp4; in UserPyModules, use from tts.lib.ethernet.PacketIp4 import PacketIp4.")

PacketIp6[¶](#tts.core.api.internalApi.Ethernet.Ethernet.PacketIp6 "Link to this definition")  
[`PacketIp6`](#tts.lib.ethernet.PacketIp6.PacketIp6 "tts.lib.ethernet.PacketIp6.PacketIp6 (Python class) — In the test case, use api.Ethernet.PacketIp6; in UserPyModules, use from tts.lib.ethernet.PacketIp6 import PacketIp6.")

PacketIcmp[¶](#tts.core.api.internalApi.Ethernet.Ethernet.PacketIcmp "Link to this definition")  
[`PacketIcmp`](#tts.lib.ethernet.PacketIcmp.PacketIcmp "tts.lib.ethernet.PacketIcmp.PacketIcmp (Python class) — In the test case, use api.Ethernet.PacketIcmp; in UserPyModules, use from tts.lib.ethernet.PacketIcmp import PacketIcmp.")

PacketMka[¶](#tts.core.api.internalApi.Ethernet.Ethernet.PacketMka "Link to this definition")  
[`PacketMka`](#tts.lib.ethernet.PacketMka.PacketMka "tts.lib.ethernet.PacketMka.PacketMka (Python class) — In the test case, use api.Ethernet.PacketMka; in UserPyModules, use from tts.lib.ethernet.PacketMka import PacketMka.")

PacketIke[¶](#tts.core.api.internalApi.Ethernet.Ethernet.PacketIke "Link to this definition")  
[`PacketIke`](#tts.lib.ethernet.PacketIke.PacketIke "tts.lib.ethernet.PacketIke.PacketIke (Python class) — In the test case, use api.Ethernet.PacketIke; in UserPyModules, use from tts.lib.ethernet.PacketIke import PacketIke.")

PacketTcp[¶](#tts.core.api.internalApi.Ethernet.Ethernet.PacketTcp "Link to this definition")  
[`PacketTcp`](#tts.lib.ethernet.PacketTcp.PacketTcp "tts.lib.ethernet.PacketTcp.PacketTcp (Python class) — In the test case, use api.Ethernet.PacketTcp; in UserPyModules, use from tts.lib.ethernet.PacketTcp import PacketTcp.")

PacketUdp[¶](#tts.core.api.internalApi.Ethernet.Ethernet.PacketUdp "Link to this definition")  
[`PacketUdp`](#tts.lib.ethernet.PacketUdp.PacketUdp "tts.lib.ethernet.PacketUdp.PacketUdp (Python class) — In the test case, use api.Ethernet.PacketUdp; in UserPyModules, use from tts.lib.ethernet.PacketUdp import PacketUdp.")

PacketPtpSync[¶](#tts.core.api.internalApi.Ethernet.Ethernet.PacketPtpSync "Link to this definition")  
[`PacketPtpSync`](#tts.lib.ethernet.PacketPtp.PacketPtpSync "tts.lib.ethernet.PacketPtp.PacketPtpSync (Python class) — In the test case, use api.Ethernet.PacketPtpSync; in UserPyModules, use from tts.lib.ethernet.PacketPtp import PacketPtpSync.")

PacketPtpFollowUp[¶](#tts.core.api.internalApi.Ethernet.Ethernet.PacketPtpFollowUp "Link to this definition")  
[`PacketPtpFollowUp`](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp "tts.lib.ethernet.PacketPtp.PacketPtpFollowUp (Python class) — In the test case, use api.Ethernet.PacketPtpFollowUp; in UserPyModules, use from tts.lib.ethernet.PacketPtp import PacketPtpFollowUp.")

PacketPdelayReq[¶](#tts.core.api.internalApi.Ethernet.Ethernet.PacketPdelayReq "Link to this definition")  
[`PacketPdelayReq`](#tts.lib.ethernet.PacketPtp.PacketPdelayReq "tts.lib.ethernet.PacketPtp.PacketPdelayReq (Python class) — In the test case, use api.Ethernet.PacketPdelayReq; in UserPyModules, use from tts.lib.ethernet.PacketPtp import PacketPdelayReq.")

PacketPdelayResp[¶](#tts.core.api.internalApi.Ethernet.Ethernet.PacketPdelayResp "Link to this definition")  
[`PacketPdelayResp`](#tts.lib.ethernet.PacketPtp.PacketPdelayResp "tts.lib.ethernet.PacketPtp.PacketPdelayResp (Python class) — In the test case, use api.Ethernet.PacketPdelayResp; in UserPyModules, use from tts.lib.ethernet.PacketPtp import PacketPdelayResp.")

PacketPdelayRespFollowUp[¶](#tts.core.api.internalApi.Ethernet.Ethernet.PacketPdelayRespFollowUp "Link to this definition")  
[`PacketPdelayRespFollowUp`](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp "tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp (Python class) — In the test case, use api.Ethernet.PacketPdelayRespFollowUp; in UserPyModules, use from tts.lib.ethernet.PacketPtp import PacketPdelayRespFollowUp.")

PacketSomeIp[¶](#tts.core.api.internalApi.Ethernet.Ethernet.PacketSomeIp "Link to this definition")  
[`PacketSomeIp`](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp "tts.lib.ethernet.PacketSomeIp.PacketSomeIp (Python class) — In the test case, use api.Ethernet.PacketSomeIp; in UserPyModules, use from tts.lib.ethernet.PacketSomeIp import PacketSomeIp.")

PacketSomeIpSd[¶](#tts.core.api.internalApi.Ethernet.Ethernet.PacketSomeIpSd "Link to this definition")  
[`PacketSomeIpSd`](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSd "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSd (Python class) — In the test case, use api.Ethernet.PacketSomeIpSd; in UserPyModules, use from tts.lib.ethernet.PacketSomeIpSd import PacketSomeIpSd.")

PacketSomeIpSdEntry[¶](#tts.core.api.internalApi.Ethernet.Ethernet.PacketSomeIpSdEntry "Link to this definition")  
[`PacketSomeIpSdEntry`](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntry "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntry (Python class) — In the test case, use api.Ethernet.PacketSomeIpSdEntry; in UserPyModules, use from tts.lib.ethernet.PacketSomeIpSd import PacketSomeIpSdEntry.")

PacketSomeIpSdEntryService[¶](#tts.core.api.internalApi.Ethernet.Ethernet.PacketSomeIpSdEntryService "Link to this definition")  
[`PacketSomeIpSdEntryService`](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryService "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryService (Python class) — Bases: PacketSomeIpSdEntry")

PacketSomeIpSdEntryEventgroup[¶](#tts.core.api.internalApi.Ethernet.Ethernet.PacketSomeIpSdEntryEventgroup "Link to this definition")  
[`PacketSomeIpSdEntryEventgroup`](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryEventgroup "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryEventgroup (Python class) — Bases: PacketSomeIpSdEntry")

PacketSomeIpSdOptionIpv4[¶](#tts.core.api.internalApi.Ethernet.Ethernet.PacketSomeIpSdOptionIpv4 "Link to this definition")  
[`PacketSomeIpSdOptionIpv4`](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4 "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4 (Python class) — Bases: PacketSomeIpSdOption")

PacketSomeIpSdOption[¶](#tts.core.api.internalApi.Ethernet.Ethernet.PacketSomeIpSdOption "Link to this definition")  
[`PacketSomeIpSdOption`](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOption "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOption (Python class) — In the test case, use api.Ethernet.PacketSomeIpSdOption; in UserPyModules, use from tts.lib.ethernet.PacketSomeIpSd import PacketSomeIpSdOption.")

PacketSomeIpSdOptionIpv6[¶](#tts.core.api.internalApi.Ethernet.Ethernet.PacketSomeIpSdOptionIpv6 "Link to this definition")  
[`PacketSomeIpSdOptionIpv6`](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6 "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6 (Python class) — Bases: PacketSomeIpSdOption")

PacketSomeIpSdOptionIpv4Multicast[¶](#tts.core.api.internalApi.Ethernet.Ethernet.PacketSomeIpSdOptionIpv4Multicast "Link to this definition")  
[`PacketSomeIpSdOptionIpv4Multicast`](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4Multicast "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4Multicast (Python class) — Bases: PacketSomeIpSdOptionIpv4")

PacketSomeIpSdOptionIpv6Multicast[¶](#tts.core.api.internalApi.Ethernet.Ethernet.PacketSomeIpSdOptionIpv6Multicast "Link to this definition")  
[`PacketSomeIpSdOptionIpv6Multicast`](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6Multicast "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6Multicast (Python class) — Bases: PacketSomeIpSdOptionIpv6")

PacketSomeIpSdOptionIpv4SD[¶](#tts.core.api.internalApi.Ethernet.Ethernet.PacketSomeIpSdOptionIpv4SD "Link to this definition")  
[`PacketSomeIpSdOptionIpv4SD`](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4SD "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4SD (Python class) — Bases: PacketSomeIpSdOptionIpv4")

PacketSomeIpSdOptionIpv6SD[¶](#tts.core.api.internalApi.Ethernet.Ethernet.PacketSomeIpSdOptionIpv6SD "Link to this definition")  
[`PacketSomeIpSdOptionIpv6SD`](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6SD "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6SD (Python class) — Bases: PacketSomeIpSdOptionIpv6")

PacketSomeIpSdOptionConfig[¶](#tts.core.api.internalApi.Ethernet.Ethernet.PacketSomeIpSdOptionConfig "Link to this definition")  
[`PacketSomeIpSdOptionConfig`](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionConfig "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionConfig (Python class) — Bases: PacketSomeIpSdOption")

### PacketEthernet[¶](#packetethernet "Link to this heading")

*class* PacketEthernet[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet "Link to this definition")  
In the test case, use `api.Ethernet.PacketEthernet`; in UserPyModules, use `from tts.lib.ethernet.PacketEthernet import PacketEthernet`.

\<protocol\>  
Equivalent to method [`FindParent(protocol)`](#tts.lib.ethernet.PacketEthernet.PacketEthernet.FindParent "tts.lib.ethernet.PacketEthernet.PacketEthernet.FindParent (Python method) — Only for pseudo signals in trace analysis! Returns the requested protocol object if present, otherwise a NoProtocol object."). Direct access to parent protocols. *protocol* is one of [`OsiProtocol`](busdatastructuresTraceanalysis.md#tts.lib.ethernet.PacketEthernet.OsiProtocol "tts.lib.ethernet.PacketEthernet.OsiProtocol (Python class) — String Enumeration class representing the supported protocol layers.").

Example: Signal.eth.src provides the source MAC address of the Ethernet protocol layer.

Type:  [`EthernetProtocolBase`](busdatastructuresTraceanalysis.md#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase (Python class) — Base class for all protocol classes.")

GetEthDstMac()[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.GetEthDstMac "Link to this definition")  
Returns:  target MAC address e.g. DE:AD:BE:EF:FF:00

Return type:  str

SetEthDstMac(*[mac](#tts.lib.ethernet.PacketEthernet.PacketEthernet.SetEthDstMac.mac "tts.lib.ethernet.PacketEthernet.PacketEthernet.SetEthDstMac.mac (Python parameter) — target MAC address e.g.")*)[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.SetEthDstMac "Link to this definition")  
Parameters:  mac : str[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.SetEthDstMac.mac "Permalink to this definition")  
target MAC address e.g. DE:AD:BE:EF:FF:00

ethDstMac[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.ethDstMac "Link to this definition")  
target MAC address e.g. DE:AD:BE:EF:FF:00

Type:  str

GetEthSrcMac()[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.GetEthSrcMac "Link to this definition")  
Returns:  source MAC address e.g. DE:AD:BE:EF:FF:00

Return type:  str

SetEthSrcMac(*[mac](#tts.lib.ethernet.PacketEthernet.PacketEthernet.SetEthSrcMac.mac "tts.lib.ethernet.PacketEthernet.PacketEthernet.SetEthSrcMac.mac (Python parameter) — source MAC addres e.g.")*)[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.SetEthSrcMac "Link to this definition")  
Parameters:  mac : str[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.SetEthSrcMac.mac "Permalink to this definition")  
source MAC addres e.g. DE:AD:BE:EF:FF:00

ethSrcMac[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.ethSrcMac "Link to this definition")  
source MAC address e.g. DE:AD:BE:EF:FF:00

Type:  str

GetEthType()[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.GetEthType "Link to this definition")  
Returns:  ethernet protocol type

Return type:  int

SetEthType(*[ethType](#tts.lib.ethernet.PacketEthernet.PacketEthernet.SetEthType.ethType "tts.lib.ethernet.PacketEthernet.PacketEthernet.SetEthType.ethType (Python parameter) — ethernet protocol type")*)[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.SetEthType "Link to this definition")  
Parameters:  ethType : int[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.SetEthType.ethType "Permalink to this definition")  
ethernet protocol type

ethType[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.ethType "Link to this definition")  
ethernet protocol type

Type:  int

GetVlanPcp(*[ixVlanTags](#tts.lib.ethernet.PacketEthernet.PacketEthernet.GetVlanPcp "tts.lib.ethernet.PacketEthernet.PacketEthernet.GetVlanPcp.ixVlanTags (Python parameter)")*)[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.GetVlanPcp "Link to this definition")  
Returns:  802.1a priority code point

Return type:  int

SetVlanPcp(*[pcp](#tts.lib.ethernet.PacketEthernet.PacketEthernet.SetVlanPcp.pcp "tts.lib.ethernet.PacketEthernet.PacketEthernet.SetVlanPcp.pcp (Python parameter) — 802.1a priority code point")*)[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.SetVlanPcp "Link to this definition")  
Parameters:  pcp : int[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.SetVlanPcp.pcp "Permalink to this definition")  
802.1a priority code point

vlanPcp[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.vlanPcp "Link to this definition")  
802.1a priority code point

Type:  int

GetVlanCfi(*[ixVlanTags](#tts.lib.ethernet.PacketEthernet.PacketEthernet.GetVlanCfi "tts.lib.ethernet.PacketEthernet.PacketEthernet.GetVlanCfi.ixVlanTags (Python parameter)")*)[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.GetVlanCfi "Link to this definition")  
Returns:  802.1a canonical format indicator

Return type:  int

SetVlanCfi(*[cfi](#tts.lib.ethernet.PacketEthernet.PacketEthernet.SetVlanCfi.cfi "tts.lib.ethernet.PacketEthernet.PacketEthernet.SetVlanCfi.cfi (Python parameter) — 802.1a canonical format indicator")*)[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.SetVlanCfi "Link to this definition")  
Parameters:  cfi : int[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.SetVlanCfi.cfi "Permalink to this definition")  
802.1a canonical format indicator

vlanCfi[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.vlanCfi "Link to this definition")  
802.1a canonical format indicator

Type:  int

GetVlanVid(*[ixVlanTags](#tts.lib.ethernet.PacketEthernet.PacketEthernet.GetVlanVid "tts.lib.ethernet.PacketEthernet.PacketEthernet.GetVlanVid.ixVlanTags (Python parameter)")*)[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.GetVlanVid "Link to this definition")  
Returns:  802.1a VLAN id

Return type:  int

SetVlanVid(*[vid](#tts.lib.ethernet.PacketEthernet.PacketEthernet.SetVlanVid.vid "tts.lib.ethernet.PacketEthernet.PacketEthernet.SetVlanVid.vid (Python parameter) — 802.1a VLAN id")*)[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.SetVlanVid "Link to this definition")  
Parameters:  vid : int[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.SetVlanVid.vid "Permalink to this definition")  
802.1a VLAN id

vlanVid[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.vlanVid "Link to this definition")  
802.1a VLAN id

Type:  int

GetVlanPcpOuter(*[ixVlanTags](#tts.lib.ethernet.PacketEthernet.PacketEthernet.GetVlanPcpOuter "tts.lib.ethernet.PacketEthernet.PacketEthernet.GetVlanPcpOuter.ixVlanTags (Python parameter)")*)[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.GetVlanPcpOuter "Link to this definition")  
Returns:  802.1ad priority code point

Return type:  int

SetVlanPcpOuter(*[pcp](#tts.lib.ethernet.PacketEthernet.PacketEthernet.SetVlanPcpOuter.pcp "tts.lib.ethernet.PacketEthernet.PacketEthernet.SetVlanPcpOuter.pcp (Python parameter) — 802.1ad priority code point")*)[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.SetVlanPcpOuter "Link to this definition")  
Parameters:  pcp : int[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.SetVlanPcpOuter.pcp "Permalink to this definition")  
802.1ad priority code point

vlanPcpOuter[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.vlanPcpOuter "Link to this definition")  
802.1ad priority code point

Type:  int

GetVlanCfiOuter(*[ixVlanTags](#tts.lib.ethernet.PacketEthernet.PacketEthernet.GetVlanCfiOuter "tts.lib.ethernet.PacketEthernet.PacketEthernet.GetVlanCfiOuter.ixVlanTags (Python parameter)")*)[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.GetVlanCfiOuter "Link to this definition")  
Returns:  802.1ad canonical format indicator

Return type:  int

SetVlanCfiOuter(*[cfi](#tts.lib.ethernet.PacketEthernet.PacketEthernet.SetVlanCfiOuter.cfi "tts.lib.ethernet.PacketEthernet.PacketEthernet.SetVlanCfiOuter.cfi (Python parameter) — 802.1ad canonical format indicator")*)[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.SetVlanCfiOuter "Link to this definition")  
Parameters:  cfi : int[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.SetVlanCfiOuter.cfi "Permalink to this definition")  
802.1ad canonical format indicator

vlanCfiOuter[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.vlanCfiOuter "Link to this definition")  
802.1ad canonical format indicator

Type:  int

GetVlanVidOuter(*[ixVlanTags](#tts.lib.ethernet.PacketEthernet.PacketEthernet.GetVlanVidOuter "tts.lib.ethernet.PacketEthernet.PacketEthernet.GetVlanVidOuter.ixVlanTags (Python parameter)")*)[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.GetVlanVidOuter "Link to this definition")  
Returns:  802.1ad VLAN id

Return type:  int

SetVlanVidOuter(*[vid](#tts.lib.ethernet.PacketEthernet.PacketEthernet.SetVlanVidOuter.vid "tts.lib.ethernet.PacketEthernet.PacketEthernet.SetVlanVidOuter.vid (Python parameter) — 802.1ad VLAN id")*)[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.SetVlanVidOuter "Link to this definition")  
Parameters:  vid : int[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.SetVlanVidOuter.vid "Permalink to this definition")  
802.1ad VLAN id

vlanVidOuter[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.vlanVidOuter "Link to this definition")  
802.1ad VLAN id

Type:  int

GetEthPayload()[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.GetEthPayload "Link to this definition")  
Returns:  Ethernet payload

Return type:  bytes

SetEthPayload(*[payload](#tts.lib.ethernet.PacketEthernet.PacketEthernet.SetEthPayload.payload "tts.lib.ethernet.PacketEthernet.PacketEthernet.SetEthPayload.payload (Python parameter) — Ethernet payload")*)[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.SetEthPayload "Link to this definition")  
Parameters:  payload : bytes[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.SetEthPayload.payload "Permalink to this definition")  
Ethernet payload

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

FindParent(*[protocol](#tts.lib.ethernet.PacketEthernet.PacketEthernet.FindParent.protocol "tts.lib.ethernet.PacketEthernet.PacketEthernet.FindParent.protocol (Python parameter) — The required protocol name.")*)[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.FindParent "Link to this definition")  
*Only for pseudo signals in trace analysis!* Returns the requested protocol object if present, otherwise a [`NoProtocol`](busdatastructuresTraceanalysis.md#tts.lib.ethernet.PacketEthernet.NoProtocol "tts.lib.ethernet.PacketEthernet.NoProtocol (Python class) — Represents a non-present protocol. Accessing any other parent of a non-present protocol will also yield a NoProtocol object. Accessing any protocol specific attributes will lead to an AttributeError since the specific protocol is not available. The boolean value of a NoProtocol object is always False, such that it can be used to check for the precense/absence of a protocol layer.") object.

Parameters:  protocol : [OsiProtocol](busdatastructuresTraceanalysis.md#tts.lib.ethernet.PacketEthernet.OsiProtocol "tts.lib.ethernet.PacketEthernet.OsiProtocol (Python class) — String Enumeration class representing the supported protocol layers.")[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.FindParent.protocol "Permalink to this definition")  
The required protocol name.

Returns:  The required parent protocol object.

Return type:  [EthernetProtocolBase](busdatastructuresTraceanalysis.md#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase (Python class) — Base class for all protocol classes.")

GetTimestamp()[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.GetTimestamp "Link to this definition")  
Returns:  Receive timestamp in sec., None if not available

Return type:  float | None

SetTimestamp(*[timestamp](#tts.lib.ethernet.PacketEthernet.PacketEthernet.SetTimestamp.timestamp "tts.lib.ethernet.PacketEthernet.PacketEthernet.SetTimestamp.timestamp (Python parameter) — Receive timestamp in sec., None if not available")*)[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.SetTimestamp "Link to this definition")  
Parameters:  timestamp : float | None[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.SetTimestamp.timestamp "Permalink to this definition")  
Receive timestamp in sec., None if not available

parent[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.parent "Link to this definition")  
*Only for pseudo signals in trace analysis!* Returns the parent protocol object if there is one present, otherwise None.

Return type:  [EthernetProtocolBase](busdatastructuresTraceanalysis.md#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase (Python class) — Base class for all protocol classes.") | None

timestamp[¶](#tts.lib.ethernet.PacketEthernet.PacketEthernet.timestamp "Link to this definition")  
Receive timestamp in sec., None if not available

Type:  Optional[float]

### PacketIp4[¶](#packetip4 "Link to this heading")

*class* PacketIp4[¶](#tts.lib.ethernet.PacketIp4.PacketIp4 "Link to this definition")  
In the test case, use `api.Ethernet.PacPacketIp4`; in UserPyModules, use `from tts.lib.ethernet.PacketIp4 import PacketIp4`.

\<protocol\>  
Equivalent to method [`FindParent(protocol)`](#tts.lib.ethernet.PacketIp4.PacketIp4.FindParent "tts.lib.ethernet.PacketIp4.PacketIp4.FindParent (Python method) — Only for pseudo signals in trace analysis! Returns the requested protocol object if present, otherwise a NoProtocol object."). Direct access to parent protocols. *protocol* is one of [`OsiProtocol`](busdatastructuresTraceanalysis.md#tts.lib.ethernet.PacketEthernet.OsiProtocol "tts.lib.ethernet.PacketEthernet.OsiProtocol (Python class) — String Enumeration class representing the supported protocol layers.").

Example: Signal.eth.src provides the source MAC address of the Ethernet protocol layer.

Type:  [`EthernetProtocolBase`](busdatastructuresTraceanalysis.md#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase (Python class) — Base class for all protocol classes.")

GetIpVersionAndHeaderLength()[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.GetIpVersionAndHeaderLength "Link to this definition")  
Returns:  protocol version and header length

Return type:  int

SetIpVersionAndHeaderLength(*[versionHeader](#tts.lib.ethernet.PacketIp4.PacketIp4.SetIpVersionAndHeaderLength.versionHeader "tts.lib.ethernet.PacketIp4.PacketIp4.SetIpVersionAndHeaderLength.versionHeader (Python parameter) — protocol version and header length")*)[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.SetIpVersionAndHeaderLength "Link to this definition")  
Parameters:  versionHeader : int[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.SetIpVersionAndHeaderLength.versionHeader "Permalink to this definition")  
protocol version and header length

ipVersionHeader[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.ipVersionHeader "Link to this definition")  
protocol version and header length

Type:  int

GetIpTos()[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.GetIpTos "Link to this definition")  
Returns:  type of service

Return type:  int

SetIpTos(*[tos](#tts.lib.ethernet.PacketIp4.PacketIp4.SetIpTos.tos "tts.lib.ethernet.PacketIp4.PacketIp4.SetIpTos.tos (Python parameter) — type of service")*)[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.SetIpTos "Link to this definition")  
Parameters:  tos : int[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.SetIpTos.tos "Permalink to this definition")  
type of service

ipTos[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.ipTos "Link to this definition")  
type of service

Type:  int

GetIpLen()[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.GetIpLen "Link to this definition")  
Returns:  packet length

Return type:  int

SetIpLen(*[length](#tts.lib.ethernet.PacketIp4.PacketIp4.SetIpLen.length "tts.lib.ethernet.PacketIp4.PacketIp4.SetIpLen.length (Python parameter) — packet length")*)[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.SetIpLen "Link to this definition")  
Parameters:  length : int[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.SetIpLen.length "Permalink to this definition")  
packet length

ipLen[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.ipLen "Link to this definition")  
packet length

Type:  int

GetIpIdent()[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.GetIpIdent "Link to this definition")  
Returns:  identifier

Return type:  int

SetIpIdent(*[ident](#tts.lib.ethernet.PacketIp4.PacketIp4.SetIpIdent.ident "tts.lib.ethernet.PacketIp4.PacketIp4.SetIpIdent.ident (Python parameter) — identifier")*)[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.SetIpIdent "Link to this definition")  
Parameters:  ident : int[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.SetIpIdent.ident "Permalink to this definition")  
identifier

ipIdent[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.ipIdent "Link to this definition")  
identifier

Type:  int

GetIpOffset()[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.GetIpOffset "Link to this definition")  
Returns:  flags and offset combined

Return type:  int

SetIpOffset(*[offset](#tts.lib.ethernet.PacketIp4.PacketIp4.SetIpOffset.offset "tts.lib.ethernet.PacketIp4.PacketIp4.SetIpOffset.offset (Python parameter) — flags and offset combined")*)[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.SetIpOffset "Link to this definition")  
Parameters:  offset : int[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.SetIpOffset.offset "Permalink to this definition")  
flags and offset combined

ipOffset[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.ipOffset "Link to this definition")  
flags and offset combined

Type:  int

GetIpTtl()[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.GetIpTtl "Link to this definition")  
Returns:  TTL

Return type:  int

SetIpTtl(*[ttl](#tts.lib.ethernet.PacketIp4.PacketIp4.SetIpTtl.ttl "tts.lib.ethernet.PacketIp4.PacketIp4.SetIpTtl.ttl (Python parameter) — TTL")*)[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.SetIpTtl "Link to this definition")  
Parameters:  ttl : int[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.SetIpTtl.ttl "Permalink to this definition")  
TTL

ipTtl[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.ipTtl "Link to this definition")  
TTL

Type:  int

GetIpProt()[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.GetIpProt "Link to this definition")  
Returns:  protocol type / next header field

Return type:  int

SetIpProt(*[prot](#tts.lib.ethernet.PacketIp4.PacketIp4.SetIpProt.prot "tts.lib.ethernet.PacketIp4.PacketIp4.SetIpProt.prot (Python parameter) — protocol type")*)[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.SetIpProt "Link to this definition")  
Parameters:  prot : int[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.SetIpProt.prot "Permalink to this definition")  
protocol type

ipProt[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.ipProt "Link to this definition")  
protocol type / next header field

Type:  int

GetIpChecksum()[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.GetIpChecksum "Link to this definition")  
Returns:  checksum

Return type:  int

SetIpChecksum(*[checksum](#tts.lib.ethernet.PacketIp4.PacketIp4.SetIpChecksum.checksum "tts.lib.ethernet.PacketIp4.PacketIp4.SetIpChecksum.checksum (Python parameter) — checksum")*)[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.SetIpChecksum "Link to this definition")  
Parameters:  checksum : int[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.SetIpChecksum.checksum "Permalink to this definition")  
checksum

ipChecksum[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.ipChecksum "Link to this definition")  
checksum

Type:  int

GetIpSrc()[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.GetIpSrc "Link to this definition")  
Returns:  source IP address e.g. 127.0.0.1

Return type:  str

SetIpSrc(*[addr](#tts.lib.ethernet.PacketIp4.PacketIp4.SetIpSrc.addr "tts.lib.ethernet.PacketIp4.PacketIp4.SetIpSrc.addr (Python parameter) — source IP address e.g.")*)[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.SetIpSrc "Link to this definition")  
Parameters:  addr : str[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.SetIpSrc.addr "Permalink to this definition")  
source IP address e.g. 127.0.0.1

ipSrc[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.ipSrc "Link to this definition")  
source IP address e.g. 127.0.0.1

Type:  str

GetIpDst()[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.GetIpDst "Link to this definition")  
Returns:  target IP address e.g. 127.0.0.1

Return type:  str

SetIpDst(*[addr](#tts.lib.ethernet.PacketIp4.PacketIp4.SetIpDst.addr "tts.lib.ethernet.PacketIp4.PacketIp4.SetIpDst.addr (Python parameter) — target IP address e.g.")*)[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.SetIpDst "Link to this definition")  
Parameters:  addr : str[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.SetIpDst.addr "Permalink to this definition")  
target IP address e.g. 127.0.0.1

ipDst[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.ipDst "Link to this definition")  
target IP address e.g. 127.0.0.1

Type:  str

GetIpPayload()[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.GetIpPayload "Link to this definition")  
Returns:  IP payload

Return type:  bytes

SetIpPayload(*[payload](#tts.lib.ethernet.PacketIp4.PacketIp4.SetIpPayload.payload "tts.lib.ethernet.PacketIp4.PacketIp4.SetIpPayload.payload (Python parameter) — IP payload")*)[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.SetIpPayload "Link to this definition")  
Parameters:  payload : bytes[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.SetIpPayload.payload "Permalink to this definition")  
IP payload

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

FindParent(*[protocol](#tts.lib.ethernet.PacketIp4.PacketIp4.FindParent.protocol "tts.lib.ethernet.PacketIp4.PacketIp4.FindParent.protocol (Python parameter) — The required protocol name.")*)[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.FindParent "Link to this definition")  
*Only for pseudo signals in trace analysis!* Returns the requested protocol object if present, otherwise a [`NoProtocol`](busdatastructuresTraceanalysis.md#tts.lib.ethernet.PacketEthernet.NoProtocol "tts.lib.ethernet.PacketEthernet.NoProtocol (Python class) — Represents a non-present protocol. Accessing any other parent of a non-present protocol will also yield a NoProtocol object. Accessing any protocol specific attributes will lead to an AttributeError since the specific protocol is not available. The boolean value of a NoProtocol object is always False, such that it can be used to check for the precense/absence of a protocol layer.") object.

Parameters:  protocol : [OsiProtocol](busdatastructuresTraceanalysis.md#tts.lib.ethernet.PacketEthernet.OsiProtocol "tts.lib.ethernet.PacketEthernet.OsiProtocol (Python class) — String Enumeration class representing the supported protocol layers.")[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.FindParent.protocol "Permalink to this definition")  
The required protocol name.

Returns:  The required parent protocol object.

Return type:  [EthernetProtocolBase](busdatastructuresTraceanalysis.md#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase (Python class) — Base class for all protocol classes.")

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

GetVlanCfi(*[ixVlanTags](#tts.lib.ethernet.PacketIp4.PacketIp4.GetVlanCfi "tts.lib.ethernet.PacketIp4.PacketIp4.GetVlanCfi.ixVlanTags (Python parameter)")*)[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.GetVlanCfi "Link to this definition")  
Returns:  802.1a canonical format indicator

Return type:  int

GetVlanCfiOuter(*[ixVlanTags](#tts.lib.ethernet.PacketIp4.PacketIp4.GetVlanCfiOuter "tts.lib.ethernet.PacketIp4.PacketIp4.GetVlanCfiOuter.ixVlanTags (Python parameter)")*)[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.GetVlanCfiOuter "Link to this definition")  
Returns:  802.1ad canonical format indicator

Return type:  int

GetVlanPcp(*[ixVlanTags](#tts.lib.ethernet.PacketIp4.PacketIp4.GetVlanPcp "tts.lib.ethernet.PacketIp4.PacketIp4.GetVlanPcp.ixVlanTags (Python parameter)")*)[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.GetVlanPcp "Link to this definition")  
Returns:  802.1a priority code point

Return type:  int

GetVlanPcpOuter(*[ixVlanTags](#tts.lib.ethernet.PacketIp4.PacketIp4.GetVlanPcpOuter "tts.lib.ethernet.PacketIp4.PacketIp4.GetVlanPcpOuter.ixVlanTags (Python parameter)")*)[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.GetVlanPcpOuter "Link to this definition")  
Returns:  802.1ad priority code point

Return type:  int

GetVlanVid(*[ixVlanTags](#tts.lib.ethernet.PacketIp4.PacketIp4.GetVlanVid "tts.lib.ethernet.PacketIp4.PacketIp4.GetVlanVid.ixVlanTags (Python parameter)")*)[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.GetVlanVid "Link to this definition")  
Returns:  802.1a VLAN id

Return type:  int

GetVlanVidOuter(*[ixVlanTags](#tts.lib.ethernet.PacketIp4.PacketIp4.GetVlanVidOuter "tts.lib.ethernet.PacketIp4.PacketIp4.GetVlanVidOuter.ixVlanTags (Python parameter)")*)[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.GetVlanVidOuter "Link to this definition")  
Returns:  802.1ad VLAN id

Return type:  int

SetEthDstMac(*[mac](#tts.lib.ethernet.PacketIp4.PacketIp4.SetEthDstMac.mac "tts.lib.ethernet.PacketIp4.PacketIp4.SetEthDstMac.mac (Python parameter) — target MAC address e.g.")*)[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.SetEthDstMac "Link to this definition")  
Parameters:  mac : str[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.SetEthDstMac.mac "Permalink to this definition")  
target MAC address e.g. DE:AD:BE:EF:FF:00

SetEthPayload(*[payload](#tts.lib.ethernet.PacketIp4.PacketIp4.SetEthPayload.payload "tts.lib.ethernet.PacketIp4.PacketIp4.SetEthPayload.payload (Python parameter) — Ethernet payload")*)[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.SetEthPayload "Link to this definition")  
Parameters:  payload : bytes[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.SetEthPayload.payload "Permalink to this definition")  
Ethernet payload

SetEthSrcMac(*[mac](#tts.lib.ethernet.PacketIp4.PacketIp4.SetEthSrcMac.mac "tts.lib.ethernet.PacketIp4.PacketIp4.SetEthSrcMac.mac (Python parameter) — source MAC addres e.g.")*)[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.SetEthSrcMac "Link to this definition")  
Parameters:  mac : str[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.SetEthSrcMac.mac "Permalink to this definition")  
source MAC addres e.g. DE:AD:BE:EF:FF:00

SetEthType(*[ethType](#tts.lib.ethernet.PacketIp4.PacketIp4.SetEthType.ethType "tts.lib.ethernet.PacketIp4.PacketIp4.SetEthType.ethType (Python parameter) — ethernet protocol type")*)[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.SetEthType "Link to this definition")  
Parameters:  ethType : int[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.SetEthType.ethType "Permalink to this definition")  
ethernet protocol type

SetTimestamp(*[timestamp](#tts.lib.ethernet.PacketIp4.PacketIp4.SetTimestamp.timestamp "tts.lib.ethernet.PacketIp4.PacketIp4.SetTimestamp.timestamp (Python parameter) — Receive timestamp in sec., None if not available")*)[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.SetTimestamp "Link to this definition")  
Parameters:  timestamp : float | None[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.SetTimestamp.timestamp "Permalink to this definition")  
Receive timestamp in sec., None if not available

SetVlanCfi(*[cfi](#tts.lib.ethernet.PacketIp4.PacketIp4.SetVlanCfi.cfi "tts.lib.ethernet.PacketIp4.PacketIp4.SetVlanCfi.cfi (Python parameter) — 802.1a canonical format indicator")*)[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.SetVlanCfi "Link to this definition")  
Parameters:  cfi : int[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.SetVlanCfi.cfi "Permalink to this definition")  
802.1a canonical format indicator

SetVlanCfiOuter(*[cfi](#tts.lib.ethernet.PacketIp4.PacketIp4.SetVlanCfiOuter.cfi "tts.lib.ethernet.PacketIp4.PacketIp4.SetVlanCfiOuter.cfi (Python parameter) — 802.1ad canonical format indicator")*)[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.SetVlanCfiOuter "Link to this definition")  
Parameters:  cfi : int[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.SetVlanCfiOuter.cfi "Permalink to this definition")  
802.1ad canonical format indicator

SetVlanPcp(*[pcp](#tts.lib.ethernet.PacketIp4.PacketIp4.SetVlanPcp.pcp "tts.lib.ethernet.PacketIp4.PacketIp4.SetVlanPcp.pcp (Python parameter) — 802.1a priority code point")*)[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.SetVlanPcp "Link to this definition")  
Parameters:  pcp : int[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.SetVlanPcp.pcp "Permalink to this definition")  
802.1a priority code point

SetVlanPcpOuter(*[pcp](#tts.lib.ethernet.PacketIp4.PacketIp4.SetVlanPcpOuter.pcp "tts.lib.ethernet.PacketIp4.PacketIp4.SetVlanPcpOuter.pcp (Python parameter) — 802.1ad priority code point")*)[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.SetVlanPcpOuter "Link to this definition")  
Parameters:  pcp : int[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.SetVlanPcpOuter.pcp "Permalink to this definition")  
802.1ad priority code point

SetVlanVid(*[vid](#tts.lib.ethernet.PacketIp4.PacketIp4.SetVlanVid.vid "tts.lib.ethernet.PacketIp4.PacketIp4.SetVlanVid.vid (Python parameter) — 802.1a VLAN id")*)[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.SetVlanVid "Link to this definition")  
Parameters:  vid : int[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.SetVlanVid.vid "Permalink to this definition")  
802.1a VLAN id

SetVlanVidOuter(*[vid](#tts.lib.ethernet.PacketIp4.PacketIp4.SetVlanVidOuter.vid "tts.lib.ethernet.PacketIp4.PacketIp4.SetVlanVidOuter.vid (Python parameter) — 802.1ad VLAN id")*)[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.SetVlanVidOuter "Link to this definition")  
Parameters:  vid : int[¶](#tts.lib.ethernet.PacketIp4.PacketIp4.SetVlanVidOuter.vid "Permalink to this definition")  
802.1ad VLAN id

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

Return type:  [EthernetProtocolBase](busdatastructuresTraceanalysis.md#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase (Python class) — Base class for all protocol classes.") | None

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
Equivalent to method [`FindParent(protocol)`](#tts.lib.ethernet.PacketIp6.PacketIp6.FindParent "tts.lib.ethernet.PacketIp6.PacketIp6.FindParent (Python method) — Only for pseudo signals in trace analysis! Returns the requested protocol object if present, otherwise a NoProtocol object."). Direct access to parent protocols. *protocol* is one of [`OsiProtocol`](busdatastructuresTraceanalysis.md#tts.lib.ethernet.PacketEthernet.OsiProtocol "tts.lib.ethernet.PacketEthernet.OsiProtocol (Python class) — String Enumeration class representing the supported protocol layers.").

Example: Signal.eth.src provides the source MAC address of the Ethernet protocol layer.

Type:  [`EthernetProtocolBase`](busdatastructuresTraceanalysis.md#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase (Python class) — Base class for all protocol classes.")

GetIpProt()[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.GetIpProt "Link to this definition")  
Returns:  protocol type / next header field

Return type:  int

SetIpProt(*[prot](#tts.lib.ethernet.PacketIp6.PacketIp6.SetIpProt.prot "tts.lib.ethernet.PacketIp6.PacketIp6.SetIpProt.prot (Python parameter) — next header field")*)[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.SetIpProt "Link to this definition")  
Set the next header field

Parameters:  prot : int[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.SetIpProt.prot "Permalink to this definition")  
next header field

ipProt[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.ipProt "Link to this definition")  
protocol type / next header field

Type:  int

GetIpHopLimit()[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.GetIpHopLimit "Link to this definition")  
Returns:  hop limit field

Return type:  int

SetIpHopLimit(*[hopLimit](#tts.lib.ethernet.PacketIp6.PacketIp6.SetIpHopLimit.hopLimit "tts.lib.ethernet.PacketIp6.PacketIp6.SetIpHopLimit.hopLimit (Python parameter) — hop limit field")*)[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.SetIpHopLimit "Link to this definition")  
Set the hop limit field

Parameters:  hopLimit : int[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.SetIpHopLimit.hopLimit "Permalink to this definition")  
hop limit field

ipHopLimit[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.ipHopLimit "Link to this definition")  
hop limit field

Type:  int

GetIpSrc()[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.GetIpSrc "Link to this definition")  
Returns:  source IP address e.g. 2001:db8::1428:57ab

Return type:  str

SetIpSrc(*[addr](#tts.lib.ethernet.PacketIp6.PacketIp6.SetIpSrc.addr "tts.lib.ethernet.PacketIp6.PacketIp6.SetIpSrc.addr (Python parameter) — source IP address e.g.")*)[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.SetIpSrc "Link to this definition")  
Parameters:  addr : str[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.SetIpSrc.addr "Permalink to this definition")  
source IP address e.g. 2001:db8::1428:57ab

ipSrc[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.ipSrc "Link to this definition")  
source IP address e.g. 2001:db8::1428:57ab

Type:  str

GetIpDst()[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.GetIpDst "Link to this definition")  
Returns:  target IP address e.g. 2001:db8::1428:57ab

Return type:  str

SetIpDst(*[addr](#tts.lib.ethernet.PacketIp6.PacketIp6.SetIpDst.addr "tts.lib.ethernet.PacketIp6.PacketIp6.SetIpDst.addr (Python parameter) — target IP address e.g.")*)[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.SetIpDst "Link to this definition")  
Parameters:  addr : str[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.SetIpDst.addr "Permalink to this definition")  
target IP address e.g. 2001:db8::1428:57ab

ipDst[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.ipDst "Link to this definition")  
target IP address e.g. 2001:db8::1428:57ab

Type:  str

GetIpPayload()[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.GetIpPayload "Link to this definition")  
Returns:  IP payload

Return type:  bytes

SetIpPayload(*[payload](#tts.lib.ethernet.PacketIp6.PacketIp6.SetIpPayload.payload "tts.lib.ethernet.PacketIp6.PacketIp6.SetIpPayload.payload (Python parameter) — IP payload")*)[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.SetIpPayload "Link to this definition")  
Parameters:  payload : bytes[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.SetIpPayload.payload "Permalink to this definition")  
IP payload

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

FindParent(*[protocol](#tts.lib.ethernet.PacketIp6.PacketIp6.FindParent.protocol "tts.lib.ethernet.PacketIp6.PacketIp6.FindParent.protocol (Python parameter) — The required protocol name.")*)[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.FindParent "Link to this definition")  
*Only for pseudo signals in trace analysis!* Returns the requested protocol object if present, otherwise a [`NoProtocol`](busdatastructuresTraceanalysis.md#tts.lib.ethernet.PacketEthernet.NoProtocol "tts.lib.ethernet.PacketEthernet.NoProtocol (Python class) — Represents a non-present protocol. Accessing any other parent of a non-present protocol will also yield a NoProtocol object. Accessing any protocol specific attributes will lead to an AttributeError since the specific protocol is not available. The boolean value of a NoProtocol object is always False, such that it can be used to check for the precense/absence of a protocol layer.") object.

Parameters:  protocol : [OsiProtocol](busdatastructuresTraceanalysis.md#tts.lib.ethernet.PacketEthernet.OsiProtocol "tts.lib.ethernet.PacketEthernet.OsiProtocol (Python class) — String Enumeration class representing the supported protocol layers.")[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.FindParent.protocol "Permalink to this definition")  
The required protocol name.

Returns:  The required parent protocol object.

Return type:  [EthernetProtocolBase](busdatastructuresTraceanalysis.md#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase (Python class) — Base class for all protocol classes.")

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

GetVlanCfi(*[ixVlanTags](#tts.lib.ethernet.PacketIp6.PacketIp6.GetVlanCfi "tts.lib.ethernet.PacketIp6.PacketIp6.GetVlanCfi.ixVlanTags (Python parameter)")*)[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.GetVlanCfi "Link to this definition")  
Returns:  802.1a canonical format indicator

Return type:  int

GetVlanCfiOuter(*[ixVlanTags](#tts.lib.ethernet.PacketIp6.PacketIp6.GetVlanCfiOuter "tts.lib.ethernet.PacketIp6.PacketIp6.GetVlanCfiOuter.ixVlanTags (Python parameter)")*)[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.GetVlanCfiOuter "Link to this definition")  
Returns:  802.1ad canonical format indicator

Return type:  int

GetVlanPcp(*[ixVlanTags](#tts.lib.ethernet.PacketIp6.PacketIp6.GetVlanPcp "tts.lib.ethernet.PacketIp6.PacketIp6.GetVlanPcp.ixVlanTags (Python parameter)")*)[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.GetVlanPcp "Link to this definition")  
Returns:  802.1a priority code point

Return type:  int

GetVlanPcpOuter(*[ixVlanTags](#tts.lib.ethernet.PacketIp6.PacketIp6.GetVlanPcpOuter "tts.lib.ethernet.PacketIp6.PacketIp6.GetVlanPcpOuter.ixVlanTags (Python parameter)")*)[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.GetVlanPcpOuter "Link to this definition")  
Returns:  802.1ad priority code point

Return type:  int

GetVlanVid(*[ixVlanTags](#tts.lib.ethernet.PacketIp6.PacketIp6.GetVlanVid "tts.lib.ethernet.PacketIp6.PacketIp6.GetVlanVid.ixVlanTags (Python parameter)")*)[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.GetVlanVid "Link to this definition")  
Returns:  802.1a VLAN id

Return type:  int

GetVlanVidOuter(*[ixVlanTags](#tts.lib.ethernet.PacketIp6.PacketIp6.GetVlanVidOuter "tts.lib.ethernet.PacketIp6.PacketIp6.GetVlanVidOuter.ixVlanTags (Python parameter)")*)[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.GetVlanVidOuter "Link to this definition")  
Returns:  802.1ad VLAN id

Return type:  int

SetEthDstMac(*[mac](#tts.lib.ethernet.PacketIp6.PacketIp6.SetEthDstMac.mac "tts.lib.ethernet.PacketIp6.PacketIp6.SetEthDstMac.mac (Python parameter) — target MAC address e.g.")*)[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.SetEthDstMac "Link to this definition")  
Parameters:  mac : str[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.SetEthDstMac.mac "Permalink to this definition")  
target MAC address e.g. DE:AD:BE:EF:FF:00

SetEthPayload(*[payload](#tts.lib.ethernet.PacketIp6.PacketIp6.SetEthPayload.payload "tts.lib.ethernet.PacketIp6.PacketIp6.SetEthPayload.payload (Python parameter) — Ethernet payload")*)[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.SetEthPayload "Link to this definition")  
Parameters:  payload : bytes[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.SetEthPayload.payload "Permalink to this definition")  
Ethernet payload

SetEthSrcMac(*[mac](#tts.lib.ethernet.PacketIp6.PacketIp6.SetEthSrcMac.mac "tts.lib.ethernet.PacketIp6.PacketIp6.SetEthSrcMac.mac (Python parameter) — source MAC addres e.g.")*)[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.SetEthSrcMac "Link to this definition")  
Parameters:  mac : str[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.SetEthSrcMac.mac "Permalink to this definition")  
source MAC addres e.g. DE:AD:BE:EF:FF:00

SetEthType(*[ethType](#tts.lib.ethernet.PacketIp6.PacketIp6.SetEthType.ethType "tts.lib.ethernet.PacketIp6.PacketIp6.SetEthType.ethType (Python parameter) — ethernet protocol type")*)[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.SetEthType "Link to this definition")  
Parameters:  ethType : int[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.SetEthType.ethType "Permalink to this definition")  
ethernet protocol type

SetTimestamp(*[timestamp](#tts.lib.ethernet.PacketIp6.PacketIp6.SetTimestamp.timestamp "tts.lib.ethernet.PacketIp6.PacketIp6.SetTimestamp.timestamp (Python parameter) — Receive timestamp in sec., None if not available")*)[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.SetTimestamp "Link to this definition")  
Parameters:  timestamp : float | None[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.SetTimestamp.timestamp "Permalink to this definition")  
Receive timestamp in sec., None if not available

SetVlanCfi(*[cfi](#tts.lib.ethernet.PacketIp6.PacketIp6.SetVlanCfi.cfi "tts.lib.ethernet.PacketIp6.PacketIp6.SetVlanCfi.cfi (Python parameter) — 802.1a canonical format indicator")*)[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.SetVlanCfi "Link to this definition")  
Parameters:  cfi : int[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.SetVlanCfi.cfi "Permalink to this definition")  
802.1a canonical format indicator

SetVlanCfiOuter(*[cfi](#tts.lib.ethernet.PacketIp6.PacketIp6.SetVlanCfiOuter.cfi "tts.lib.ethernet.PacketIp6.PacketIp6.SetVlanCfiOuter.cfi (Python parameter) — 802.1ad canonical format indicator")*)[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.SetVlanCfiOuter "Link to this definition")  
Parameters:  cfi : int[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.SetVlanCfiOuter.cfi "Permalink to this definition")  
802.1ad canonical format indicator

SetVlanPcp(*[pcp](#tts.lib.ethernet.PacketIp6.PacketIp6.SetVlanPcp.pcp "tts.lib.ethernet.PacketIp6.PacketIp6.SetVlanPcp.pcp (Python parameter) — 802.1a priority code point")*)[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.SetVlanPcp "Link to this definition")  
Parameters:  pcp : int[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.SetVlanPcp.pcp "Permalink to this definition")  
802.1a priority code point

SetVlanPcpOuter(*[pcp](#tts.lib.ethernet.PacketIp6.PacketIp6.SetVlanPcpOuter.pcp "tts.lib.ethernet.PacketIp6.PacketIp6.SetVlanPcpOuter.pcp (Python parameter) — 802.1ad priority code point")*)[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.SetVlanPcpOuter "Link to this definition")  
Parameters:  pcp : int[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.SetVlanPcpOuter.pcp "Permalink to this definition")  
802.1ad priority code point

SetVlanVid(*[vid](#tts.lib.ethernet.PacketIp6.PacketIp6.SetVlanVid.vid "tts.lib.ethernet.PacketIp6.PacketIp6.SetVlanVid.vid (Python parameter) — 802.1a VLAN id")*)[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.SetVlanVid "Link to this definition")  
Parameters:  vid : int[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.SetVlanVid.vid "Permalink to this definition")  
802.1a VLAN id

SetVlanVidOuter(*[vid](#tts.lib.ethernet.PacketIp6.PacketIp6.SetVlanVidOuter.vid "tts.lib.ethernet.PacketIp6.PacketIp6.SetVlanVidOuter.vid (Python parameter) — 802.1ad VLAN id")*)[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.SetVlanVidOuter "Link to this definition")  
Parameters:  vid : int[¶](#tts.lib.ethernet.PacketIp6.PacketIp6.SetVlanVidOuter.vid "Permalink to this definition")  
802.1ad VLAN id

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

Return type:  [EthernetProtocolBase](busdatastructuresTraceanalysis.md#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase (Python class) — Base class for all protocol classes.") | None

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
Equivalent to method [`FindParent(protocol)`](#tts.lib.ethernet.PacketIcmp.PacketIcmp.FindParent "tts.lib.ethernet.PacketIcmp.PacketIcmp.FindParent (Python method) — Only for pseudo signals in trace analysis! Returns the requested protocol object if present, otherwise a NoProtocol object."). Direct access to parent protocols. *protocol* is one of [`OsiProtocol`](busdatastructuresTraceanalysis.md#tts.lib.ethernet.PacketEthernet.OsiProtocol "tts.lib.ethernet.PacketEthernet.OsiProtocol (Python class) — String Enumeration class representing the supported protocol layers.").

Example: Signal.eth.src provides the source MAC address of the Ethernet protocol layer.

Type:  [`EthernetProtocolBase`](busdatastructuresTraceanalysis.md#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase (Python class) — Base class for all protocol classes.")

GetIcmpType()[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetIcmpType "Link to this definition")  
Returns:  ICMP type

Return type:  int

SetIcmpType(*[icmpType](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetIcmpType.icmpType "tts.lib.ethernet.PacketIcmp.PacketIcmp.SetIcmpType.icmpType (Python parameter) — ICMP type")*)[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetIcmpType "Link to this definition")  
Parameters:  icmpType : int[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetIcmpType.icmpType "Permalink to this definition")  
ICMP type

icmpType[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.icmpType "Link to this definition")  
ICMP type

Type:  int

GetIcmpCode()[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetIcmpCode "Link to this definition")  
Returns:  ICMP code

Return type:  int

SetIcmpCode(*[code](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetIcmpCode.code "tts.lib.ethernet.PacketIcmp.PacketIcmp.SetIcmpCode.code (Python parameter) — ICMP code")*)[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetIcmpCode "Link to this definition")  
Parameters:  code : int[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetIcmpCode.code "Permalink to this definition")  
ICMP code

icmpCode[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.icmpCode "Link to this definition")  
ICMP code

Type:  int

GetIcmpChecksum()[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetIcmpChecksum "Link to this definition")  
Returns:  checksum

Return type:  int

SetIcmpChecksum(*[checksum](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetIcmpChecksum.checksum "tts.lib.ethernet.PacketIcmp.PacketIcmp.SetIcmpChecksum.checksum (Python parameter) — checksum")*)[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetIcmpChecksum "Link to this definition")  
Parameters:  checksum : int[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetIcmpChecksum.checksum "Permalink to this definition")  
checksum

icmpChecksum[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.icmpChecksum "Link to this definition")  
checksum

Type:  int

GetIcmpPayload()[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetIcmpPayload "Link to this definition")  
Returns:  ICMP payload

Return type:  bytes

CalcIpLen()[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.CalcIpLen "Link to this definition")  
Calculate and set the current length of this IP packet

FindParent(*[protocol](#tts.lib.ethernet.PacketIcmp.PacketIcmp.FindParent.protocol "tts.lib.ethernet.PacketIcmp.PacketIcmp.FindParent.protocol (Python parameter) — The required protocol name.")*)[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.FindParent "Link to this definition")  
*Only for pseudo signals in trace analysis!* Returns the requested protocol object if present, otherwise a [`NoProtocol`](busdatastructuresTraceanalysis.md#tts.lib.ethernet.PacketEthernet.NoProtocol "tts.lib.ethernet.PacketEthernet.NoProtocol (Python class) — Represents a non-present protocol. Accessing any other parent of a non-present protocol will also yield a NoProtocol object. Accessing any protocol specific attributes will lead to an AttributeError since the specific protocol is not available. The boolean value of a NoProtocol object is always False, such that it can be used to check for the precense/absence of a protocol layer.") object.

Parameters:  protocol : [OsiProtocol](busdatastructuresTraceanalysis.md#tts.lib.ethernet.PacketEthernet.OsiProtocol "tts.lib.ethernet.PacketEthernet.OsiProtocol (Python class) — String Enumeration class representing the supported protocol layers.")[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.FindParent.protocol "Permalink to this definition")  
The required protocol name.

Returns:  The required parent protocol object.

Return type:  [EthernetProtocolBase](busdatastructuresTraceanalysis.md#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase (Python class) — Base class for all protocol classes.")

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

GetVlanCfi(*[ixVlanTags](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetVlanCfi "tts.lib.ethernet.PacketIcmp.PacketIcmp.GetVlanCfi.ixVlanTags (Python parameter)")*)[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetVlanCfi "Link to this definition")  
Returns:  802.1a canonical format indicator

Return type:  int

GetVlanCfiOuter(*[ixVlanTags](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetVlanCfiOuter "tts.lib.ethernet.PacketIcmp.PacketIcmp.GetVlanCfiOuter.ixVlanTags (Python parameter)")*)[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetVlanCfiOuter "Link to this definition")  
Returns:  802.1ad canonical format indicator

Return type:  int

GetVlanPcp(*[ixVlanTags](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetVlanPcp "tts.lib.ethernet.PacketIcmp.PacketIcmp.GetVlanPcp.ixVlanTags (Python parameter)")*)[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetVlanPcp "Link to this definition")  
Returns:  802.1a priority code point

Return type:  int

GetVlanPcpOuter(*[ixVlanTags](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetVlanPcpOuter "tts.lib.ethernet.PacketIcmp.PacketIcmp.GetVlanPcpOuter.ixVlanTags (Python parameter)")*)[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetVlanPcpOuter "Link to this definition")  
Returns:  802.1ad priority code point

Return type:  int

GetVlanVid(*[ixVlanTags](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetVlanVid "tts.lib.ethernet.PacketIcmp.PacketIcmp.GetVlanVid.ixVlanTags (Python parameter)")*)[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetVlanVid "Link to this definition")  
Returns:  802.1a VLAN id

Return type:  int

GetVlanVidOuter(*[ixVlanTags](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetVlanVidOuter "tts.lib.ethernet.PacketIcmp.PacketIcmp.GetVlanVidOuter.ixVlanTags (Python parameter)")*)[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.GetVlanVidOuter "Link to this definition")  
Returns:  802.1ad VLAN id

Return type:  int

PK_CLASS[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.PK_CLASS "Link to this definition")  
alias of `IP`

SetEthDstMac(*[mac](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetEthDstMac.mac "tts.lib.ethernet.PacketIcmp.PacketIcmp.SetEthDstMac.mac (Python parameter) — target MAC address e.g.")*)[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetEthDstMac "Link to this definition")  
Parameters:  mac : str[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetEthDstMac.mac "Permalink to this definition")  
target MAC address e.g. DE:AD:BE:EF:FF:00

SetEthPayload(*[payload](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetEthPayload.payload "tts.lib.ethernet.PacketIcmp.PacketIcmp.SetEthPayload.payload (Python parameter) — Ethernet payload")*)[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetEthPayload "Link to this definition")  
Parameters:  payload : bytes[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetEthPayload.payload "Permalink to this definition")  
Ethernet payload

SetEthSrcMac(*[mac](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetEthSrcMac.mac "tts.lib.ethernet.PacketIcmp.PacketIcmp.SetEthSrcMac.mac (Python parameter) — source MAC addres e.g.")*)[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetEthSrcMac "Link to this definition")  
Parameters:  mac : str[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetEthSrcMac.mac "Permalink to this definition")  
source MAC addres e.g. DE:AD:BE:EF:FF:00

SetEthType(*[ethType](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetEthType.ethType "tts.lib.ethernet.PacketIcmp.PacketIcmp.SetEthType.ethType (Python parameter) — ethernet protocol type")*)[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetEthType "Link to this definition")  
Parameters:  ethType : int[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetEthType.ethType "Permalink to this definition")  
ethernet protocol type

SetIcmpPayload(*[payload](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetIcmpPayload.payload "tts.lib.ethernet.PacketIcmp.PacketIcmp.SetIcmpPayload.payload (Python parameter) — ICMP payload")*)[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetIcmpPayload "Link to this definition")  
Parameters:  payload : bytes[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetIcmpPayload.payload "Permalink to this definition")  
ICMP payload

SetIpChecksum(*[checksum](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetIpChecksum.checksum "tts.lib.ethernet.PacketIcmp.PacketIcmp.SetIpChecksum.checksum (Python parameter) — checksum")*)[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetIpChecksum "Link to this definition")  
Parameters:  checksum : int[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetIpChecksum.checksum "Permalink to this definition")  
checksum

SetIpDst(*[addr](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetIpDst.addr "tts.lib.ethernet.PacketIcmp.PacketIcmp.SetIpDst.addr (Python parameter) — target IP address e.g.")*)[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetIpDst "Link to this definition")  
Parameters:  addr : str[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetIpDst.addr "Permalink to this definition")  
target IP address e.g. 127.0.0.1

SetIpIdent(*[ident](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetIpIdent.ident "tts.lib.ethernet.PacketIcmp.PacketIcmp.SetIpIdent.ident (Python parameter) — identifier")*)[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetIpIdent "Link to this definition")  
Parameters:  ident : int[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetIpIdent.ident "Permalink to this definition")  
identifier

SetIpLen(*[length](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetIpLen.length "tts.lib.ethernet.PacketIcmp.PacketIcmp.SetIpLen.length (Python parameter) — packet length")*)[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetIpLen "Link to this definition")  
Parameters:  length : int[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetIpLen.length "Permalink to this definition")  
packet length

SetIpOffset(*[offset](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetIpOffset.offset "tts.lib.ethernet.PacketIcmp.PacketIcmp.SetIpOffset.offset (Python parameter) — flags and offset combined")*)[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetIpOffset "Link to this definition")  
Parameters:  offset : int[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetIpOffset.offset "Permalink to this definition")  
flags and offset combined

SetIpPayload(*[payload](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetIpPayload.payload "tts.lib.ethernet.PacketIcmp.PacketIcmp.SetIpPayload.payload (Python parameter) — IP payload")*)[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetIpPayload "Link to this definition")  
Parameters:  payload : bytes[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetIpPayload.payload "Permalink to this definition")  
IP payload

SetIpProt(*[prot](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetIpProt.prot "tts.lib.ethernet.PacketIcmp.PacketIcmp.SetIpProt.prot (Python parameter) — protocol type")*)[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetIpProt "Link to this definition")  
Parameters:  prot : int[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetIpProt.prot "Permalink to this definition")  
protocol type

SetIpSrc(*[addr](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetIpSrc.addr "tts.lib.ethernet.PacketIcmp.PacketIcmp.SetIpSrc.addr (Python parameter) — source IP address e.g.")*)[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetIpSrc "Link to this definition")  
Parameters:  addr : str[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetIpSrc.addr "Permalink to this definition")  
source IP address e.g. 127.0.0.1

SetIpTos(*[tos](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetIpTos.tos "tts.lib.ethernet.PacketIcmp.PacketIcmp.SetIpTos.tos (Python parameter) — type of service")*)[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetIpTos "Link to this definition")  
Parameters:  tos : int[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetIpTos.tos "Permalink to this definition")  
type of service

SetIpTtl(*[ttl](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetIpTtl.ttl "tts.lib.ethernet.PacketIcmp.PacketIcmp.SetIpTtl.ttl (Python parameter) — TTL")*)[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetIpTtl "Link to this definition")  
Parameters:  ttl : int[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetIpTtl.ttl "Permalink to this definition")  
TTL

SetIpVersionAndHeaderLength(*[versionHeader](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetIpVersionAndHeaderLength.versionHeader "tts.lib.ethernet.PacketIcmp.PacketIcmp.SetIpVersionAndHeaderLength.versionHeader (Python parameter) — protocol version and header length")*)[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetIpVersionAndHeaderLength "Link to this definition")  
Parameters:  versionHeader : int[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetIpVersionAndHeaderLength.versionHeader "Permalink to this definition")  
protocol version and header length

SetTimestamp(*[timestamp](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetTimestamp.timestamp "tts.lib.ethernet.PacketIcmp.PacketIcmp.SetTimestamp.timestamp (Python parameter) — Receive timestamp in sec., None if not available")*)[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetTimestamp "Link to this definition")  
Parameters:  timestamp : float | None[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetTimestamp.timestamp "Permalink to this definition")  
Receive timestamp in sec., None if not available

SetVlanCfi(*[cfi](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetVlanCfi.cfi "tts.lib.ethernet.PacketIcmp.PacketIcmp.SetVlanCfi.cfi (Python parameter) — 802.1a canonical format indicator")*)[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetVlanCfi "Link to this definition")  
Parameters:  cfi : int[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetVlanCfi.cfi "Permalink to this definition")  
802.1a canonical format indicator

SetVlanCfiOuter(*[cfi](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetVlanCfiOuter.cfi "tts.lib.ethernet.PacketIcmp.PacketIcmp.SetVlanCfiOuter.cfi (Python parameter) — 802.1ad canonical format indicator")*)[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetVlanCfiOuter "Link to this definition")  
Parameters:  cfi : int[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetVlanCfiOuter.cfi "Permalink to this definition")  
802.1ad canonical format indicator

SetVlanPcp(*[pcp](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetVlanPcp.pcp "tts.lib.ethernet.PacketIcmp.PacketIcmp.SetVlanPcp.pcp (Python parameter) — 802.1a priority code point")*)[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetVlanPcp "Link to this definition")  
Parameters:  pcp : int[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetVlanPcp.pcp "Permalink to this definition")  
802.1a priority code point

SetVlanPcpOuter(*[pcp](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetVlanPcpOuter.pcp "tts.lib.ethernet.PacketIcmp.PacketIcmp.SetVlanPcpOuter.pcp (Python parameter) — 802.1ad priority code point")*)[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetVlanPcpOuter "Link to this definition")  
Parameters:  pcp : int[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetVlanPcpOuter.pcp "Permalink to this definition")  
802.1ad priority code point

SetVlanVid(*[vid](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetVlanVid.vid "tts.lib.ethernet.PacketIcmp.PacketIcmp.SetVlanVid.vid (Python parameter) — 802.1a VLAN id")*)[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetVlanVid "Link to this definition")  
Parameters:  vid : int[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetVlanVid.vid "Permalink to this definition")  
802.1a VLAN id

SetVlanVidOuter(*[vid](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetVlanVidOuter.vid "tts.lib.ethernet.PacketIcmp.PacketIcmp.SetVlanVidOuter.vid (Python parameter) — 802.1ad VLAN id")*)[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetVlanVidOuter "Link to this definition")  
Parameters:  vid : int[¶](#tts.lib.ethernet.PacketIcmp.PacketIcmp.SetVlanVidOuter.vid "Permalink to this definition")  
802.1ad VLAN id

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

Return type:  [EthernetProtocolBase](busdatastructuresTraceanalysis.md#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase (Python class) — Base class for all protocol classes.") | None

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
Equivalent to method [`FindParent(protocol)`](#tts.lib.ethernet.PacketMka.PacketMka.FindParent "tts.lib.ethernet.PacketMka.PacketMka.FindParent (Python method) — Only for pseudo signals in trace analysis! Returns the requested protocol object if present, otherwise a NoProtocol object."). Direct access to parent protocols. *protocol* is one of [`OsiProtocol`](busdatastructuresTraceanalysis.md#tts.lib.ethernet.PacketEthernet.OsiProtocol "tts.lib.ethernet.PacketEthernet.OsiProtocol (Python class) — String Enumeration class representing the supported protocol layers.").

Example: Signal.eth.src provides the source MAC address of the Ethernet protocol layer.

Type:  [`EthernetProtocolBase`](busdatastructuresTraceanalysis.md#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase (Python class) — Base class for all protocol classes.")

UseCak(*[cak](#tts.lib.ethernet.PacketMka.PacketMka.UseCak "tts.lib.ethernet.PacketMka.PacketMka.UseCak.cak (Python parameter)")*)[¶](#tts.lib.ethernet.PacketMka.PacketMka.UseCak "Link to this definition")  
Use a specific Connectivity Association Key. Needed for example to unwrap the Security Association Key or to validate the MKPDU’s Integrity Check Value.

GetEthDstMac()[¶](#tts.lib.ethernet.PacketMka.PacketMka.GetEthDstMac "Link to this definition")  
Returns:  destination MAC address e.g. DE:AD:BE:EF:42:05

Return type:  str

SetEthDstMac(*[mac](#tts.lib.ethernet.PacketMka.PacketMka.SetEthDstMac.mac "tts.lib.ethernet.PacketMka.PacketMka.SetEthDstMac.mac (Python parameter) — target MAC address e.g.")*)[¶](#tts.lib.ethernet.PacketMka.PacketMka.SetEthDstMac "Link to this definition")  
Parameters:  mac : str[¶](#tts.lib.ethernet.PacketMka.PacketMka.SetEthDstMac.mac "Permalink to this definition")  
target MAC address e.g. DE:AD:BE:EF:FF:00

ethDstMac[¶](#tts.lib.ethernet.PacketMka.PacketMka.ethDstMac "Link to this definition")  
destination MAC address e.g. DE:AD:BE:EF:42:05

Type:  str

GetEthSrcMac()[¶](#tts.lib.ethernet.PacketMka.PacketMka.GetEthSrcMac "Link to this definition")  
Returns:  source MAC address e.g. DE:AD:BE:EF:42:05

Return type:  str

SetEthSrcMac(*[mac](#tts.lib.ethernet.PacketMka.PacketMka.SetEthSrcMac.mac "tts.lib.ethernet.PacketMka.PacketMka.SetEthSrcMac.mac (Python parameter) — source MAC addres e.g.")*)[¶](#tts.lib.ethernet.PacketMka.PacketMka.SetEthSrcMac "Link to this definition")  
Parameters:  mac : str[¶](#tts.lib.ethernet.PacketMka.PacketMka.SetEthSrcMac.mac "Permalink to this definition")  
source MAC addres e.g. DE:AD:BE:EF:FF:00

ethSrcMac[¶](#tts.lib.ethernet.PacketMka.PacketMka.ethSrcMac "Link to this definition")  
source MAC address e.g. DE:AD:BE:EF:42:05

Type:  str

GetEthType()[¶](#tts.lib.ethernet.PacketMka.PacketMka.GetEthType "Link to this definition")  
Returns:  ethernet protocol type

Return type:  int

SetEthType(*[ethType](#tts.lib.ethernet.PacketMka.PacketMka.SetEthType.ethType "tts.lib.ethernet.PacketMka.PacketMka.SetEthType.ethType (Python parameter) — ethernet protocol type")*)[¶](#tts.lib.ethernet.PacketMka.PacketMka.SetEthType "Link to this definition")  
Parameters:  ethType : int[¶](#tts.lib.ethernet.PacketMka.PacketMka.SetEthType.ethType "Permalink to this definition")  
ethernet protocol type

GetEthPayload()[¶](#tts.lib.ethernet.PacketMka.PacketMka.GetEthPayload "Link to this definition")  
Returns:  Ethernet payload

Return type:  bytes

SetEthPayload(*[payload](#tts.lib.ethernet.PacketMka.PacketMka.SetEthPayload.payload "tts.lib.ethernet.PacketMka.PacketMka.SetEthPayload.payload (Python parameter) — Ethernet payload")*)[¶](#tts.lib.ethernet.PacketMka.PacketMka.SetEthPayload "Link to this definition")  
Parameters:  payload : bytes[¶](#tts.lib.ethernet.PacketMka.PacketMka.SetEthPayload.payload "Permalink to this definition")  
Ethernet payload

GetMkaIcv()[¶](#tts.lib.ethernet.PacketMka.PacketMka.GetMkaIcv "Link to this definition")  
Returns:  Integrity Check Value of this MKPDU. See IEEE 802.1X-2020, section 9.4.1.

Return type:  [*ByteStream*](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream (Python class) — The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.")

mkaIcv[¶](#tts.lib.ethernet.PacketMka.PacketMka.mkaIcv "Link to this definition")  
Integrity Check Value of this MKPDU. See IEEE 802.1X-2020, section 9.4.1.

Type:  [ByteStream](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream (Python class) — The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.")

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

Return type:  [*ByteStream*](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream (Python class) — The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.")

macSecSci[¶](#tts.lib.ethernet.PacketMka.PacketMka.macSecSci "Link to this definition")  
Secure Channel Identifier from Basic Parameter Set. See IEEE 802.1X-2020, table 11-7 and IEEE 802.1AE.

Type:  [ByteStream](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream (Python class) — The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.")

GetMemberIdentifier()[¶](#tts.lib.ethernet.PacketMka.PacketMka.GetMemberIdentifier "Link to this definition")  
Returns:  Member Identifier from Basic Parameter Set. See IEEE 802.1X-2020, table 11-7.

Return type:  [*ByteStream*](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream (Python class) — The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.")

memberIdentifier[¶](#tts.lib.ethernet.PacketMka.PacketMka.memberIdentifier "Link to this definition")  
Member Identifier from Basic Parameter Set. See IEEE 802.1X-2020, table 11-7.

Type:  [ByteStream](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream (Python class) — The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.")

GetMessageNumber()[¶](#tts.lib.ethernet.PacketMka.PacketMka.GetMessageNumber "Link to this definition")  
Returns:  Message Number from Basic Parameter Set. See IEEE 802.1X-2020, table 11-7.

Return type:  int

messageNumber[¶](#tts.lib.ethernet.PacketMka.PacketMka.messageNumber "Link to this definition")  
Message Number from Basic Parameter Set. See IEEE 802.1X-2020, table 11-7.

Type:  int

GetCakName()[¶](#tts.lib.ethernet.PacketMka.PacketMka.GetCakName "Link to this definition")  
Returns:  Connectivity Association Key Name from Basic Parameter Set. See IEEE 802.1X-2020, section 9.3.1 and table 11-7.

Return type:  [*ByteStream*](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream (Python class) — The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.")

cakName[¶](#tts.lib.ethernet.PacketMka.PacketMka.cakName "Link to this definition")  
Connectivity Association Key Name from Basic Parameter Set. See IEEE 802.1X-2020, section 9.3.1 and table 11-7.

Type:  [ByteStream](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream (Python class) — The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.")

GetLivePeerListMemberIdentifiers()[¶](#tts.lib.ethernet.PacketMka.PacketMka.GetLivePeerListMemberIdentifiers "Link to this definition")  
Returns:  List of Member Identifiers from Live Peer List Parameter Set. See IEEE 802.1X-2020, section 9.4.3 and table 11-7.

Return type:  list[[*ByteStream*](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream (Python class) — The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.")] | None

livePeerListMemberIdentifiers[¶](#tts.lib.ethernet.PacketMka.PacketMka.livePeerListMemberIdentifiers "Link to this definition")  
List of Member Identifiers from Live Peer List Parameter Set. See IEEE 802.1X-2020, section 9.4.3 and table 11-7.

Type:  Optional[list[[ByteStream](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream (Python class) — The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.")]]

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

Return type:  list[[*ByteStream*](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream (Python class) — The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.")] | None

potentialPeerListMemberIdentifiers[¶](#tts.lib.ethernet.PacketMka.PacketMka.potentialPeerListMemberIdentifiers "Link to this definition")  
List of Member Identifiers from Potential Peer List Parameter Set. See IEEE 802.1X-2020, section 9.4.3 and table 11-7.

Type:  Optional[list[[ByteStream](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream (Python class) — The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.")]]

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

Return type:  [*ByteStream*](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream (Python class) — The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.") | None

sakUseLatestKeyServerMemberIdentifier[¶](#tts.lib.ethernet.PacketMka.PacketMka.sakUseLatestKeyServerMemberIdentifier "Link to this definition")  
Latest Key Server Member Identifier from MACsec SAK Use Parameter Set. See IEEE 802.1X-2020, section 9.10.1 and table 11-7.

Type:  Optional[[ByteStream](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream (Python class) — The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.")]

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

Return type:  [*ByteStream*](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream (Python class) — The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.") | None

distributedSakWrappedKey[¶](#tts.lib.ethernet.PacketMka.PacketMka.distributedSakWrappedKey "Link to this definition")  
AES Key Wrap of Security Association Key from Distributed SAK Parameter Set. See IEEE 802.1X-2020, section 9.8 and table 11-7.

Type:  Optional[[ByteStream](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream (Python class) — The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.")]

GetDistributedSakUnwrappedKey()[¶](#tts.lib.ethernet.PacketMka.PacketMka.GetDistributedSakUnwrappedKey "Link to this definition")  
Returns:  Security Association Key, unwrapped using the Connectivity Association Key which was set by PacketMka.UseCak().

Return type:  [*ByteStream*](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream (Python class) — The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.") | None

distributedSakUnwrappedKey[¶](#tts.lib.ethernet.PacketMka.PacketMka.distributedSakUnwrappedKey "Link to this definition")  
Security Association Key, unwrapped using the Connectivity Association Key which was set by PacketMka.UseCak().

Type:  Optional[[ByteStream](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream (Python class) — The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.")]

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

Return type:  [*ByteStream*](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream (Python class) — The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.") | None

distributedSakCipherSuite[¶](#tts.lib.ethernet.PacketMka.PacketMka.distributedSakCipherSuite "Link to this definition")  
MACsec Cipher Suite from Distributed SAK Parameter Set. Values from IEEE 802.1AE-2018, table 14-1. See IEEE 802.1X-2020, section 9.7 and table 11-7.

Type:  Optional[[ByteStream](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream (Python class) — The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.")]

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

Return type:  list[[*ByteStream*](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream (Python class) — The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.")] | None

announcementInfos[¶](#tts.lib.ethernet.PacketMka.PacketMka.announcementInfos "Link to this definition")  
TLV infos (without length bits) from Announcement Parameter Set. See IEEE 802.1X-2020, section 9.7 and figure 11-19.

Type:  Optional[list[[ByteStream](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream (Python class) — The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.")]]

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

FindParent(*[protocol](#tts.lib.ethernet.PacketMka.PacketMka.FindParent.protocol "tts.lib.ethernet.PacketMka.PacketMka.FindParent.protocol (Python parameter) — The required protocol name.")*)[¶](#tts.lib.ethernet.PacketMka.PacketMka.FindParent "Link to this definition")  
*Only for pseudo signals in trace analysis!* Returns the requested protocol object if present, otherwise a [`NoProtocol`](busdatastructuresTraceanalysis.md#tts.lib.ethernet.PacketEthernet.NoProtocol "tts.lib.ethernet.PacketEthernet.NoProtocol (Python class) — Represents a non-present protocol. Accessing any other parent of a non-present protocol will also yield a NoProtocol object. Accessing any protocol specific attributes will lead to an AttributeError since the specific protocol is not available. The boolean value of a NoProtocol object is always False, such that it can be used to check for the precense/absence of a protocol layer.") object.

Parameters:  protocol : [OsiProtocol](busdatastructuresTraceanalysis.md#tts.lib.ethernet.PacketEthernet.OsiProtocol "tts.lib.ethernet.PacketEthernet.OsiProtocol (Python class) — String Enumeration class representing the supported protocol layers.")[¶](#tts.lib.ethernet.PacketMka.PacketMka.FindParent.protocol "Permalink to this definition")  
The required protocol name.

Returns:  The required parent protocol object.

Return type:  [EthernetProtocolBase](busdatastructuresTraceanalysis.md#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase (Python class) — Base class for all protocol classes.")

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

GetVlanCfi(*[ixVlanTags](#tts.lib.ethernet.PacketMka.PacketMka.GetVlanCfi "tts.lib.ethernet.PacketMka.PacketMka.GetVlanCfi.ixVlanTags (Python parameter)")*)[¶](#tts.lib.ethernet.PacketMka.PacketMka.GetVlanCfi "Link to this definition")  
Returns:  802.1a canonical format indicator

Return type:  int

GetVlanCfiOuter(*[ixVlanTags](#tts.lib.ethernet.PacketMka.PacketMka.GetVlanCfiOuter "tts.lib.ethernet.PacketMka.PacketMka.GetVlanCfiOuter.ixVlanTags (Python parameter)")*)[¶](#tts.lib.ethernet.PacketMka.PacketMka.GetVlanCfiOuter "Link to this definition")  
Returns:  802.1ad canonical format indicator

Return type:  int

GetVlanPcp(*[ixVlanTags](#tts.lib.ethernet.PacketMka.PacketMka.GetVlanPcp "tts.lib.ethernet.PacketMka.PacketMka.GetVlanPcp.ixVlanTags (Python parameter)")*)[¶](#tts.lib.ethernet.PacketMka.PacketMka.GetVlanPcp "Link to this definition")  
Returns:  802.1a priority code point

Return type:  int

GetVlanPcpOuter(*[ixVlanTags](#tts.lib.ethernet.PacketMka.PacketMka.GetVlanPcpOuter "tts.lib.ethernet.PacketMka.PacketMka.GetVlanPcpOuter.ixVlanTags (Python parameter)")*)[¶](#tts.lib.ethernet.PacketMka.PacketMka.GetVlanPcpOuter "Link to this definition")  
Returns:  802.1ad priority code point

Return type:  int

GetVlanVid(*[ixVlanTags](#tts.lib.ethernet.PacketMka.PacketMka.GetVlanVid "tts.lib.ethernet.PacketMka.PacketMka.GetVlanVid.ixVlanTags (Python parameter)")*)[¶](#tts.lib.ethernet.PacketMka.PacketMka.GetVlanVid "Link to this definition")  
Returns:  802.1a VLAN id

Return type:  int

GetVlanVidOuter(*[ixVlanTags](#tts.lib.ethernet.PacketMka.PacketMka.GetVlanVidOuter "tts.lib.ethernet.PacketMka.PacketMka.GetVlanVidOuter.ixVlanTags (Python parameter)")*)[¶](#tts.lib.ethernet.PacketMka.PacketMka.GetVlanVidOuter "Link to this definition")  
Returns:  802.1ad VLAN id

Return type:  int

RemoveAnnouncement()[¶](#tts.lib.ethernet.PacketMka.PacketMka.RemoveAnnouncement "Link to this definition")  
If the MKPDU has an Announcement Parameter Set, remove it.

SetTimestamp(*[timestamp](#tts.lib.ethernet.PacketMka.PacketMka.SetTimestamp.timestamp "tts.lib.ethernet.PacketMka.PacketMka.SetTimestamp.timestamp (Python parameter) — Receive timestamp in sec., None if not available")*)[¶](#tts.lib.ethernet.PacketMka.PacketMka.SetTimestamp "Link to this definition")  
Parameters:  timestamp : float | None[¶](#tts.lib.ethernet.PacketMka.PacketMka.SetTimestamp.timestamp "Permalink to this definition")  
Receive timestamp in sec., None if not available

SetVlanCfi(*[cfi](#tts.lib.ethernet.PacketMka.PacketMka.SetVlanCfi.cfi "tts.lib.ethernet.PacketMka.PacketMka.SetVlanCfi.cfi (Python parameter) — 802.1a canonical format indicator")*)[¶](#tts.lib.ethernet.PacketMka.PacketMka.SetVlanCfi "Link to this definition")  
Parameters:  cfi : int[¶](#tts.lib.ethernet.PacketMka.PacketMka.SetVlanCfi.cfi "Permalink to this definition")  
802.1a canonical format indicator

SetVlanCfiOuter(*[cfi](#tts.lib.ethernet.PacketMka.PacketMka.SetVlanCfiOuter.cfi "tts.lib.ethernet.PacketMka.PacketMka.SetVlanCfiOuter.cfi (Python parameter) — 802.1ad canonical format indicator")*)[¶](#tts.lib.ethernet.PacketMka.PacketMka.SetVlanCfiOuter "Link to this definition")  
Parameters:  cfi : int[¶](#tts.lib.ethernet.PacketMka.PacketMka.SetVlanCfiOuter.cfi "Permalink to this definition")  
802.1ad canonical format indicator

SetVlanPcp(*[pcp](#tts.lib.ethernet.PacketMka.PacketMka.SetVlanPcp.pcp "tts.lib.ethernet.PacketMka.PacketMka.SetVlanPcp.pcp (Python parameter) — 802.1a priority code point")*)[¶](#tts.lib.ethernet.PacketMka.PacketMka.SetVlanPcp "Link to this definition")  
Parameters:  pcp : int[¶](#tts.lib.ethernet.PacketMka.PacketMka.SetVlanPcp.pcp "Permalink to this definition")  
802.1a priority code point

SetVlanPcpOuter(*[pcp](#tts.lib.ethernet.PacketMka.PacketMka.SetVlanPcpOuter.pcp "tts.lib.ethernet.PacketMka.PacketMka.SetVlanPcpOuter.pcp (Python parameter) — 802.1ad priority code point")*)[¶](#tts.lib.ethernet.PacketMka.PacketMka.SetVlanPcpOuter "Link to this definition")  
Parameters:  pcp : int[¶](#tts.lib.ethernet.PacketMka.PacketMka.SetVlanPcpOuter.pcp "Permalink to this definition")  
802.1ad priority code point

SetVlanVid(*[vid](#tts.lib.ethernet.PacketMka.PacketMka.SetVlanVid.vid "tts.lib.ethernet.PacketMka.PacketMka.SetVlanVid.vid (Python parameter) — 802.1a VLAN id")*)[¶](#tts.lib.ethernet.PacketMka.PacketMka.SetVlanVid "Link to this definition")  
Parameters:  vid : int[¶](#tts.lib.ethernet.PacketMka.PacketMka.SetVlanVid.vid "Permalink to this definition")  
802.1a VLAN id

SetVlanVidOuter(*[vid](#tts.lib.ethernet.PacketMka.PacketMka.SetVlanVidOuter.vid "tts.lib.ethernet.PacketMka.PacketMka.SetVlanVidOuter.vid (Python parameter) — 802.1ad VLAN id")*)[¶](#tts.lib.ethernet.PacketMka.PacketMka.SetVlanVidOuter "Link to this definition")  
Parameters:  vid : int[¶](#tts.lib.ethernet.PacketMka.PacketMka.SetVlanVidOuter.vid "Permalink to this definition")  
802.1ad VLAN id

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

Return type:  [EthernetProtocolBase](busdatastructuresTraceanalysis.md#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase (Python class) — Base class for all protocol classes.") | None

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
Equivalent to method [`FindParent(protocol)`](#tts.lib.ethernet.PacketIke.PacketIke.FindParent "tts.lib.ethernet.PacketIke.PacketIke.FindParent (Python method) — Only for pseudo signals in trace analysis! Returns the requested protocol object if present, otherwise a NoProtocol object."). Direct access to parent protocols. *protocol* is one of [`OsiProtocol`](busdatastructuresTraceanalysis.md#tts.lib.ethernet.PacketEthernet.OsiProtocol "tts.lib.ethernet.PacketEthernet.OsiProtocol (Python class) — String Enumeration class representing the supported protocol layers.").

Example: Signal.eth.src provides the source MAC address of the Ethernet protocol layer.

Type:  [`EthernetProtocolBase`](busdatastructuresTraceanalysis.md#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase (Python class) — Base class for all protocol classes.")

GetInitiatorSpi()[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetInitiatorSpi "Link to this definition")  
Returns:  Security Parameter Index chosen by the initiator

Return type:  [*ByteStream*](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream (Python class) — The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.")

initiatorSpi[¶](#tts.lib.ethernet.PacketIke.PacketIke.initiatorSpi "Link to this definition")  
Security Parameter Index chosen by the initiator

Type:  [ByteStream](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream (Python class) — The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.")

GetResponderSpi()[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetResponderSpi "Link to this definition")  
Returns:  Security Parameter Index chosen by the responder

Return type:  [*ByteStream*](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream (Python class) — The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.")

responderSpi[¶](#tts.lib.ethernet.PacketIke.PacketIke.responderSpi "Link to this definition")  
Security Parameter Index chosen by the responder

Type:  [ByteStream](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream (Python class) — The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.")

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

Return type:  [*ByteStream*](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream (Python class) — The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.") | None

keyExchangeData[¶](#tts.lib.ethernet.PacketIke.PacketIke.keyExchangeData "Link to this definition")  
key exchange data from KE payload, or None if there is no KE payload

Type:  Optional[[ByteStream](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream (Python class) — The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.")]

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

Return type:  [*ByteStream*](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream (Python class) — The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.") | None

nonceData[¶](#tts.lib.ethernet.PacketIke.PacketIke.nonceData "Link to this definition")  
nonce data, or None if there is no nonce payload

Type:  Optional[[ByteStream](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream (Python class) — The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.")]

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

Return type:  [*ByteStream*](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream (Python class) — The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.") | None

certificateData[¶](#tts.lib.ethernet.PacketIke.PacketIke.certificateData "Link to this definition")  
certificate data of CERT payload, or None if there is no CERT payload

Type:  Optional[[ByteStream](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream (Python class) — The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.")]

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

Return type:  [*ByteStream*](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream (Python class) — The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.") | None

certificateRequestData[¶](#tts.lib.ethernet.PacketIke.PacketIke.certificateRequestData "Link to this definition")  
concatenated certificate authorities’ public key SHA-1 hashes of CERTREQ payload, or None if there is no CERTREQ payload

Type:  Optional[[ByteStream](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream (Python class) — The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.")]

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

Return type:  [*ByteStream*](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream (Python class) — The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.") | None

identInitiatorData[¶](#tts.lib.ethernet.PacketIke.PacketIke.identInitiatorData "Link to this definition")  
identification data of IDi payload, or None if there is no IDi payload

Type:  Optional[[ByteStream](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream (Python class) — The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.")]

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

Return type:  [*ByteStream*](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream (Python class) — The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.") | None

identResponderData[¶](#tts.lib.ethernet.PacketIke.PacketIke.identResponderData "Link to this definition")  
identification data of IDr payload, or None if there is no IDr payload

Type:  Optional[[ByteStream](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream (Python class) — The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.")]

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

Return type:  [*ByteStream*](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream (Python class) — The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.") | None

authData[¶](#tts.lib.ethernet.PacketIke.PacketIke.authData "Link to this definition")  
authentication data of AUTH payload, or None if there is no AUTH payload

Type:  Optional[[ByteStream](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream (Python class) — The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.")]

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

Return type:  [*ByteStream*](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream (Python class) — The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.")

tsInitiatorTrafficSelectors[¶](#tts.lib.ethernet.PacketIke.PacketIke.tsInitiatorTrafficSelectors "Link to this definition")  
traffic selector data of TSi payload, or None if there is no TSi payload

Type:  [ByteStream](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream (Python class) — The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.")

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

Return type:  [*ByteStream*](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream (Python class) — The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.")

tsResponderTrafficSelectors[¶](#tts.lib.ethernet.PacketIke.PacketIke.tsResponderTrafficSelectors "Link to this definition")  
traffic selector data of TSr payload, or None if there is no TSr payload

Type:  [ByteStream](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream (Python class) — The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.")

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

Return type:  [*ByteStream*](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream (Python class) — The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.") | None

saProposals[¶](#tts.lib.ethernet.PacketIke.PacketIke.saProposals "Link to this definition")  
proposal data SA payload, or None if there is no SA payload

Type:  Optional[[ByteStream](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream (Python class) — The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.")]

GetNotifyNumOfPayloads()[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetNotifyNumOfPayloads "Link to this definition")  
Returns:  number of Notify payloads in this IKEv2 packet

Return type:  int

notifyNumOfPayloads[¶](#tts.lib.ethernet.PacketIke.PacketIke.notifyNumOfPayloads "Link to this definition")  
number of Notify payloads in this IKEv2 packet

Type:  int

GetNotifyNextPayload(*[notifyIdx](#tts.lib.ethernet.PacketIke.PacketIke.GetNotifyNextPayload "tts.lib.ethernet.PacketIke.PacketIke.GetNotifyNextPayload.notifyIdx (Python parameter)")=`-``1`*)[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetNotifyNextPayload "Link to this definition")  
Returns:  type of next payload from Notify payload, or None if there is no Notify payload

Return type:  int | None

notifyNextPayload[¶](#tts.lib.ethernet.PacketIke.PacketIke.notifyNextPayload "Link to this definition")  
type of next payload from Notify payload, or None if there is no Notify payload

Type:  Optional[int]

GetNotifyCritical(*[notifyIdx](#tts.lib.ethernet.PacketIke.PacketIke.GetNotifyCritical "tts.lib.ethernet.PacketIke.PacketIke.GetNotifyCritical.notifyIdx (Python parameter)")=`-``1`*)[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetNotifyCritical "Link to this definition")  
Returns:  critical flag of Notify payload, or None if there is no Notify payload

Return type:  bool | None

notifyCritical[¶](#tts.lib.ethernet.PacketIke.PacketIke.notifyCritical "Link to this definition")  
critical flag of Notify payload, or None if there is no Notify payload

Type:  Optional[bool]

GetNotifyLength(*[notifyIdx](#tts.lib.ethernet.PacketIke.PacketIke.GetNotifyLength "tts.lib.ethernet.PacketIke.PacketIke.GetNotifyLength.notifyIdx (Python parameter)")=`-``1`*)[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetNotifyLength "Link to this definition")  
Returns:  length of Notify payload, or None if there is no Notify payload

Return type:  int | None

notifyLength[¶](#tts.lib.ethernet.PacketIke.PacketIke.notifyLength "Link to this definition")  
length of Notify payload, or None if there is no Notify payload

Type:  Optional[int]

GetNotifyProtocolId(*[notifyIdx](#tts.lib.ethernet.PacketIke.PacketIke.GetNotifyProtocolId "tts.lib.ethernet.PacketIke.PacketIke.GetNotifyProtocolId.notifyIdx (Python parameter)")=`-``1`*)[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetNotifyProtocolId "Link to this definition")  
Returns:  protocol id of Notify payload, or None if there is no Notify payload

Return type:  int | None

notifyProtocolId[¶](#tts.lib.ethernet.PacketIke.PacketIke.notifyProtocolId "Link to this definition")  
protocol id of Notify payload, or None if there is no Notify payload

Type:  Optional[int]

GetNotifySpiSize(*[notifyIdx](#tts.lib.ethernet.PacketIke.PacketIke.GetNotifySpiSize "tts.lib.ethernet.PacketIke.PacketIke.GetNotifySpiSize.notifyIdx (Python parameter)")=`-``1`*)[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetNotifySpiSize "Link to this definition")  
Returns:  SPI size of Notify payload, or None if there is no Notify payload

Return type:  int | None

notifySpiSize[¶](#tts.lib.ethernet.PacketIke.PacketIke.notifySpiSize "Link to this definition")  
SPI size of Notify payload, or None if there is no Notify payload

Type:  Optional[int]

GetNotifyMessageType(*[notifyIdx](#tts.lib.ethernet.PacketIke.PacketIke.GetNotifyMessageType "tts.lib.ethernet.PacketIke.PacketIke.GetNotifyMessageType.notifyIdx (Python parameter)")=`-``1`*)[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetNotifyMessageType "Link to this definition")  
Returns:  notify message type of Notify payload, or None if there is no Notify payload

Return type:  int | None

notifyMessageType[¶](#tts.lib.ethernet.PacketIke.PacketIke.notifyMessageType "Link to this definition")  
notify message type of Notify payload, or None if there is no Notify payload

Type:  Optional[int]

GetNotifySpi(*[notifyIdx](#tts.lib.ethernet.PacketIke.PacketIke.GetNotifySpi "tts.lib.ethernet.PacketIke.PacketIke.GetNotifySpi.notifyIdx (Python parameter)")=`-``1`*)[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetNotifySpi "Link to this definition")  
Returns:  SPI of Notify payload, or None if there is no Notify payload

Return type:  [*ByteStream*](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream (Python class) — The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.") | None

notifySpi[¶](#tts.lib.ethernet.PacketIke.PacketIke.notifySpi "Link to this definition")  
SPI of Notify payload, or None if there is no Notify payload

Type:  Optional[[ByteStream](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream (Python class) — The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.")]

GetNotifyData(*[notifyIdx](#tts.lib.ethernet.PacketIke.PacketIke.GetNotifyData "tts.lib.ethernet.PacketIke.PacketIke.GetNotifyData.notifyIdx (Python parameter)")=`-``1`*)[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetNotifyData "Link to this definition")  
Returns:  notification data of Notify payload, or None if there is no Notify payload

Return type:  [*ByteStream*](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream (Python class) — The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.") | None

notifyData[¶](#tts.lib.ethernet.PacketIke.PacketIke.notifyData "Link to this definition")  
notification data of Notify payload, or None if there is no Notify payload

Type:  Optional[[ByteStream](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream (Python class) — The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.")]

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

FindParent(*[protocol](#tts.lib.ethernet.PacketIke.PacketIke.FindParent.protocol "tts.lib.ethernet.PacketIke.PacketIke.FindParent.protocol (Python parameter) — The required protocol name.")*)[¶](#tts.lib.ethernet.PacketIke.PacketIke.FindParent "Link to this definition")  
*Only for pseudo signals in trace analysis!* Returns the requested protocol object if present, otherwise a [`NoProtocol`](busdatastructuresTraceanalysis.md#tts.lib.ethernet.PacketEthernet.NoProtocol "tts.lib.ethernet.PacketEthernet.NoProtocol (Python class) — Represents a non-present protocol. Accessing any other parent of a non-present protocol will also yield a NoProtocol object. Accessing any protocol specific attributes will lead to an AttributeError since the specific protocol is not available. The boolean value of a NoProtocol object is always False, such that it can be used to check for the precense/absence of a protocol layer.") object.

Parameters:  protocol : [OsiProtocol](busdatastructuresTraceanalysis.md#tts.lib.ethernet.PacketEthernet.OsiProtocol "tts.lib.ethernet.PacketEthernet.OsiProtocol (Python class) — String Enumeration class representing the supported protocol layers.")[¶](#tts.lib.ethernet.PacketIke.PacketIke.FindParent.protocol "Permalink to this definition")  
The required protocol name.

Returns:  The required parent protocol object.

Return type:  [EthernetProtocolBase](busdatastructuresTraceanalysis.md#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase (Python class) — Base class for all protocol classes.")

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

GetVlanCfi(*[ixVlanTags](#tts.lib.ethernet.PacketIke.PacketIke.GetVlanCfi "tts.lib.ethernet.PacketIke.PacketIke.GetVlanCfi.ixVlanTags (Python parameter)")*)[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetVlanCfi "Link to this definition")  
Returns:  802.1a canonical format indicator

Return type:  int

GetVlanCfiOuter(*[ixVlanTags](#tts.lib.ethernet.PacketIke.PacketIke.GetVlanCfiOuter "tts.lib.ethernet.PacketIke.PacketIke.GetVlanCfiOuter.ixVlanTags (Python parameter)")*)[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetVlanCfiOuter "Link to this definition")  
Returns:  802.1ad canonical format indicator

Return type:  int

GetVlanPcp(*[ixVlanTags](#tts.lib.ethernet.PacketIke.PacketIke.GetVlanPcp "tts.lib.ethernet.PacketIke.PacketIke.GetVlanPcp.ixVlanTags (Python parameter)")*)[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetVlanPcp "Link to this definition")  
Returns:  802.1a priority code point

Return type:  int

GetVlanPcpOuter(*[ixVlanTags](#tts.lib.ethernet.PacketIke.PacketIke.GetVlanPcpOuter "tts.lib.ethernet.PacketIke.PacketIke.GetVlanPcpOuter.ixVlanTags (Python parameter)")*)[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetVlanPcpOuter "Link to this definition")  
Returns:  802.1ad priority code point

Return type:  int

GetVlanVid(*[ixVlanTags](#tts.lib.ethernet.PacketIke.PacketIke.GetVlanVid "tts.lib.ethernet.PacketIke.PacketIke.GetVlanVid.ixVlanTags (Python parameter)")*)[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetVlanVid "Link to this definition")  
Returns:  802.1a VLAN id

Return type:  int

GetVlanVidOuter(*[ixVlanTags](#tts.lib.ethernet.PacketIke.PacketIke.GetVlanVidOuter "tts.lib.ethernet.PacketIke.PacketIke.GetVlanVidOuter.ixVlanTags (Python parameter)")*)[¶](#tts.lib.ethernet.PacketIke.PacketIke.GetVlanVidOuter "Link to this definition")  
Returns:  802.1ad VLAN id

Return type:  int

PK_CLASS[¶](#tts.lib.ethernet.PacketIke.PacketIke.PK_CLASS "Link to this definition")  
alias of `IP`

SetEthDstMac(*[mac](#tts.lib.ethernet.PacketIke.PacketIke.SetEthDstMac.mac "tts.lib.ethernet.PacketIke.PacketIke.SetEthDstMac.mac (Python parameter) — target MAC address e.g.")*)[¶](#tts.lib.ethernet.PacketIke.PacketIke.SetEthDstMac "Link to this definition")  
Parameters:  mac : str[¶](#tts.lib.ethernet.PacketIke.PacketIke.SetEthDstMac.mac "Permalink to this definition")  
target MAC address e.g. DE:AD:BE:EF:FF:00

SetEthPayload(*[payload](#tts.lib.ethernet.PacketIke.PacketIke.SetEthPayload.payload "tts.lib.ethernet.PacketIke.PacketIke.SetEthPayload.payload (Python parameter) — Ethernet payload")*)[¶](#tts.lib.ethernet.PacketIke.PacketIke.SetEthPayload "Link to this definition")  
Parameters:  payload : bytes[¶](#tts.lib.ethernet.PacketIke.PacketIke.SetEthPayload.payload "Permalink to this definition")  
Ethernet payload

SetEthSrcMac(*[mac](#tts.lib.ethernet.PacketIke.PacketIke.SetEthSrcMac.mac "tts.lib.ethernet.PacketIke.PacketIke.SetEthSrcMac.mac (Python parameter) — source MAC addres e.g.")*)[¶](#tts.lib.ethernet.PacketIke.PacketIke.SetEthSrcMac "Link to this definition")  
Parameters:  mac : str[¶](#tts.lib.ethernet.PacketIke.PacketIke.SetEthSrcMac.mac "Permalink to this definition")  
source MAC addres e.g. DE:AD:BE:EF:FF:00

SetEthType(*[ethType](#tts.lib.ethernet.PacketIke.PacketIke.SetEthType.ethType "tts.lib.ethernet.PacketIke.PacketIke.SetEthType.ethType (Python parameter) — ethernet protocol type")*)[¶](#tts.lib.ethernet.PacketIke.PacketIke.SetEthType "Link to this definition")  
Parameters:  ethType : int[¶](#tts.lib.ethernet.PacketIke.PacketIke.SetEthType.ethType "Permalink to this definition")  
ethernet protocol type

SetIpChecksum(*[checksum](#tts.lib.ethernet.PacketIke.PacketIke.SetIpChecksum.checksum "tts.lib.ethernet.PacketIke.PacketIke.SetIpChecksum.checksum (Python parameter) — checksum")*)[¶](#tts.lib.ethernet.PacketIke.PacketIke.SetIpChecksum "Link to this definition")  
Parameters:  checksum : int[¶](#tts.lib.ethernet.PacketIke.PacketIke.SetIpChecksum.checksum "Permalink to this definition")  
checksum

SetIpDst(*[addr](#tts.lib.ethernet.PacketIke.PacketIke.SetIpDst.addr "tts.lib.ethernet.PacketIke.PacketIke.SetIpDst.addr (Python parameter) — target IP address e.g.")*)[¶](#tts.lib.ethernet.PacketIke.PacketIke.SetIpDst "Link to this definition")  
Parameters:  addr : str[¶](#tts.lib.ethernet.PacketIke.PacketIke.SetIpDst.addr "Permalink to this definition")  
target IP address e.g. 127.0.0.1

SetIpIdent(*[ident](#tts.lib.ethernet.PacketIke.PacketIke.SetIpIdent.ident "tts.lib.ethernet.PacketIke.PacketIke.SetIpIdent.ident (Python parameter) — identifier")*)[¶](#tts.lib.ethernet.PacketIke.PacketIke.SetIpIdent "Link to this definition")  
Parameters:  ident : int[¶](#tts.lib.ethernet.PacketIke.PacketIke.SetIpIdent.ident "Permalink to this definition")  
identifier

SetIpLen(*[length](#tts.lib.ethernet.PacketIke.PacketIke.SetIpLen.length "tts.lib.ethernet.PacketIke.PacketIke.SetIpLen.length (Python parameter) — packet length")*)[¶](#tts.lib.ethernet.PacketIke.PacketIke.SetIpLen "Link to this definition")  
Parameters:  length : int[¶](#tts.lib.ethernet.PacketIke.PacketIke.SetIpLen.length "Permalink to this definition")  
packet length

SetIpOffset(*[offset](#tts.lib.ethernet.PacketIke.PacketIke.SetIpOffset.offset "tts.lib.ethernet.PacketIke.PacketIke.SetIpOffset.offset (Python parameter) — flags and offset combined")*)[¶](#tts.lib.ethernet.PacketIke.PacketIke.SetIpOffset "Link to this definition")  
Parameters:  offset : int[¶](#tts.lib.ethernet.PacketIke.PacketIke.SetIpOffset.offset "Permalink to this definition")  
flags and offset combined

SetIpPayload(*[payload](#tts.lib.ethernet.PacketIke.PacketIke.SetIpPayload.payload "tts.lib.ethernet.PacketIke.PacketIke.SetIpPayload.payload (Python parameter) — IP payload")*)[¶](#tts.lib.ethernet.PacketIke.PacketIke.SetIpPayload "Link to this definition")  
Parameters:  payload : bytes[¶](#tts.lib.ethernet.PacketIke.PacketIke.SetIpPayload.payload "Permalink to this definition")  
IP payload

SetIpProt(*[prot](#tts.lib.ethernet.PacketIke.PacketIke.SetIpProt.prot "tts.lib.ethernet.PacketIke.PacketIke.SetIpProt.prot (Python parameter) — protocol type")*)[¶](#tts.lib.ethernet.PacketIke.PacketIke.SetIpProt "Link to this definition")  
Parameters:  prot : int[¶](#tts.lib.ethernet.PacketIke.PacketIke.SetIpProt.prot "Permalink to this definition")  
protocol type

SetIpSrc(*[addr](#tts.lib.ethernet.PacketIke.PacketIke.SetIpSrc.addr "tts.lib.ethernet.PacketIke.PacketIke.SetIpSrc.addr (Python parameter) — source IP address e.g.")*)[¶](#tts.lib.ethernet.PacketIke.PacketIke.SetIpSrc "Link to this definition")  
Parameters:  addr : str[¶](#tts.lib.ethernet.PacketIke.PacketIke.SetIpSrc.addr "Permalink to this definition")  
source IP address e.g. 127.0.0.1

SetIpTos(*[tos](#tts.lib.ethernet.PacketIke.PacketIke.SetIpTos.tos "tts.lib.ethernet.PacketIke.PacketIke.SetIpTos.tos (Python parameter) — type of service")*)[¶](#tts.lib.ethernet.PacketIke.PacketIke.SetIpTos "Link to this definition")  
Parameters:  tos : int[¶](#tts.lib.ethernet.PacketIke.PacketIke.SetIpTos.tos "Permalink to this definition")  
type of service

SetIpTtl(*[ttl](#tts.lib.ethernet.PacketIke.PacketIke.SetIpTtl.ttl "tts.lib.ethernet.PacketIke.PacketIke.SetIpTtl.ttl (Python parameter) — TTL")*)[¶](#tts.lib.ethernet.PacketIke.PacketIke.SetIpTtl "Link to this definition")  
Parameters:  ttl : int[¶](#tts.lib.ethernet.PacketIke.PacketIke.SetIpTtl.ttl "Permalink to this definition")  
TTL

SetIpVersionAndHeaderLength(*[versionHeader](#tts.lib.ethernet.PacketIke.PacketIke.SetIpVersionAndHeaderLength.versionHeader "tts.lib.ethernet.PacketIke.PacketIke.SetIpVersionAndHeaderLength.versionHeader (Python parameter) — protocol version and header length")*)[¶](#tts.lib.ethernet.PacketIke.PacketIke.SetIpVersionAndHeaderLength "Link to this definition")  
Parameters:  versionHeader : int[¶](#tts.lib.ethernet.PacketIke.PacketIke.SetIpVersionAndHeaderLength.versionHeader "Permalink to this definition")  
protocol version and header length

SetTimestamp(*[timestamp](#tts.lib.ethernet.PacketIke.PacketIke.SetTimestamp.timestamp "tts.lib.ethernet.PacketIke.PacketIke.SetTimestamp.timestamp (Python parameter) — Receive timestamp in sec., None if not available")*)[¶](#tts.lib.ethernet.PacketIke.PacketIke.SetTimestamp "Link to this definition")  
Parameters:  timestamp : float | None[¶](#tts.lib.ethernet.PacketIke.PacketIke.SetTimestamp.timestamp "Permalink to this definition")  
Receive timestamp in sec., None if not available

SetUdpChecksum(*[checksum](#tts.lib.ethernet.PacketIke.PacketIke.SetUdpChecksum.checksum "tts.lib.ethernet.PacketIke.PacketIke.SetUdpChecksum.checksum (Python parameter) — checksum")*)[¶](#tts.lib.ethernet.PacketIke.PacketIke.SetUdpChecksum "Link to this definition")  
Parameters:  checksum : int[¶](#tts.lib.ethernet.PacketIke.PacketIke.SetUdpChecksum.checksum "Permalink to this definition")  
checksum

SetUdpDst(*[port](#tts.lib.ethernet.PacketIke.PacketIke.SetUdpDst.port "tts.lib.ethernet.PacketIke.PacketIke.SetUdpDst.port (Python parameter) — destination port")*)[¶](#tts.lib.ethernet.PacketIke.PacketIke.SetUdpDst "Link to this definition")  
Parameters:  port : int[¶](#tts.lib.ethernet.PacketIke.PacketIke.SetUdpDst.port "Permalink to this definition")  
destination port

SetUdpLen(*[length](#tts.lib.ethernet.PacketIke.PacketIke.SetUdpLen.length "tts.lib.ethernet.PacketIke.PacketIke.SetUdpLen.length (Python parameter) — length of the UDP segment")*)[¶](#tts.lib.ethernet.PacketIke.PacketIke.SetUdpLen "Link to this definition")  
Parameters:  length : int[¶](#tts.lib.ethernet.PacketIke.PacketIke.SetUdpLen.length "Permalink to this definition")  
length of the UDP segment

SetUdpPayload(*[payload](#tts.lib.ethernet.PacketIke.PacketIke.SetUdpPayload.payload "tts.lib.ethernet.PacketIke.PacketIke.SetUdpPayload.payload (Python parameter) — UDP payload")*)[¶](#tts.lib.ethernet.PacketIke.PacketIke.SetUdpPayload "Link to this definition")  
Parameters:  payload : bytes[¶](#tts.lib.ethernet.PacketIke.PacketIke.SetUdpPayload.payload "Permalink to this definition")  
UDP payload

SetUdpSrc(*[port](#tts.lib.ethernet.PacketIke.PacketIke.SetUdpSrc.port "tts.lib.ethernet.PacketIke.PacketIke.SetUdpSrc.port (Python parameter) — source port")*)[¶](#tts.lib.ethernet.PacketIke.PacketIke.SetUdpSrc "Link to this definition")  
Parameters:  port : int[¶](#tts.lib.ethernet.PacketIke.PacketIke.SetUdpSrc.port "Permalink to this definition")  
source port

SetVlanCfi(*[cfi](#tts.lib.ethernet.PacketIke.PacketIke.SetVlanCfi.cfi "tts.lib.ethernet.PacketIke.PacketIke.SetVlanCfi.cfi (Python parameter) — 802.1a canonical format indicator")*)[¶](#tts.lib.ethernet.PacketIke.PacketIke.SetVlanCfi "Link to this definition")  
Parameters:  cfi : int[¶](#tts.lib.ethernet.PacketIke.PacketIke.SetVlanCfi.cfi "Permalink to this definition")  
802.1a canonical format indicator

SetVlanCfiOuter(*[cfi](#tts.lib.ethernet.PacketIke.PacketIke.SetVlanCfiOuter.cfi "tts.lib.ethernet.PacketIke.PacketIke.SetVlanCfiOuter.cfi (Python parameter) — 802.1ad canonical format indicator")*)[¶](#tts.lib.ethernet.PacketIke.PacketIke.SetVlanCfiOuter "Link to this definition")  
Parameters:  cfi : int[¶](#tts.lib.ethernet.PacketIke.PacketIke.SetVlanCfiOuter.cfi "Permalink to this definition")  
802.1ad canonical format indicator

SetVlanPcp(*[pcp](#tts.lib.ethernet.PacketIke.PacketIke.SetVlanPcp.pcp "tts.lib.ethernet.PacketIke.PacketIke.SetVlanPcp.pcp (Python parameter) — 802.1a priority code point")*)[¶](#tts.lib.ethernet.PacketIke.PacketIke.SetVlanPcp "Link to this definition")  
Parameters:  pcp : int[¶](#tts.lib.ethernet.PacketIke.PacketIke.SetVlanPcp.pcp "Permalink to this definition")  
802.1a priority code point

SetVlanPcpOuter(*[pcp](#tts.lib.ethernet.PacketIke.PacketIke.SetVlanPcpOuter.pcp "tts.lib.ethernet.PacketIke.PacketIke.SetVlanPcpOuter.pcp (Python parameter) — 802.1ad priority code point")*)[¶](#tts.lib.ethernet.PacketIke.PacketIke.SetVlanPcpOuter "Link to this definition")  
Parameters:  pcp : int[¶](#tts.lib.ethernet.PacketIke.PacketIke.SetVlanPcpOuter.pcp "Permalink to this definition")  
802.1ad priority code point

SetVlanVid(*[vid](#tts.lib.ethernet.PacketIke.PacketIke.SetVlanVid.vid "tts.lib.ethernet.PacketIke.PacketIke.SetVlanVid.vid (Python parameter) — 802.1a VLAN id")*)[¶](#tts.lib.ethernet.PacketIke.PacketIke.SetVlanVid "Link to this definition")  
Parameters:  vid : int[¶](#tts.lib.ethernet.PacketIke.PacketIke.SetVlanVid.vid "Permalink to this definition")  
802.1a VLAN id

SetVlanVidOuter(*[vid](#tts.lib.ethernet.PacketIke.PacketIke.SetVlanVidOuter.vid "tts.lib.ethernet.PacketIke.PacketIke.SetVlanVidOuter.vid (Python parameter) — 802.1ad VLAN id")*)[¶](#tts.lib.ethernet.PacketIke.PacketIke.SetVlanVidOuter "Link to this definition")  
Parameters:  vid : int[¶](#tts.lib.ethernet.PacketIke.PacketIke.SetVlanVidOuter.vid "Permalink to this definition")  
802.1ad VLAN id

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

Return type:  [EthernetProtocolBase](busdatastructuresTraceanalysis.md#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase (Python class) — Base class for all protocol classes.") | None

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
Equivalent to method [`FindParent(protocol)`](#tts.lib.ethernet.PacketTcp.PacketTcp.FindParent "tts.lib.ethernet.PacketTcp.PacketTcp.FindParent (Python method) — Only for pseudo signals in trace analysis! Returns the requested protocol object if present, otherwise a NoProtocol object."). Direct access to parent protocols. *protocol* is one of [`OsiProtocol`](busdatastructuresTraceanalysis.md#tts.lib.ethernet.PacketEthernet.OsiProtocol "tts.lib.ethernet.PacketEthernet.OsiProtocol (Python class) — String Enumeration class representing the supported protocol layers.").

Example: Signal.eth.src provides the source MAC address of the Ethernet protocol layer.

Type:  [`EthernetProtocolBase`](busdatastructuresTraceanalysis.md#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase (Python class) — Base class for all protocol classes.")

GetTcpLen()[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.GetTcpLen "Link to this definition")  
Returns:  length of the whole TCP segment including header length

Return type:  int

GetTcpSrc()[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.GetTcpSrc "Link to this definition")  
Returns:  source port

Return type:  int

SetTcpSrc(*[port](#tts.lib.ethernet.PacketTcp.PacketTcp.SetTcpSrc.port "tts.lib.ethernet.PacketTcp.PacketTcp.SetTcpSrc.port (Python parameter) — source port")*)[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.SetTcpSrc "Link to this definition")  
Parameters:  port : int[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.SetTcpSrc.port "Permalink to this definition")  
source port

tcpSrc[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.tcpSrc "Link to this definition")  
source port

Type:  int

GetTcpDst()[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.GetTcpDst "Link to this definition")  
Returns:  destination port

Return type:  int

SetTcpDst(*[port](#tts.lib.ethernet.PacketTcp.PacketTcp.SetTcpDst.port "tts.lib.ethernet.PacketTcp.PacketTcp.SetTcpDst.port (Python parameter) — destination port")*)[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.SetTcpDst "Link to this definition")  
Parameters:  port : int[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.SetTcpDst.port "Permalink to this definition")  
destination port

tcpDst[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.tcpDst "Link to this definition")  
destination port

Type:  int

GetTcpSeq()[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.GetTcpSeq "Link to this definition")  
Returns:  sequence number

Return type:  int

SetTcpSeq(*[seq](#tts.lib.ethernet.PacketTcp.PacketTcp.SetTcpSeq.seq "tts.lib.ethernet.PacketTcp.PacketTcp.SetTcpSeq.seq (Python parameter) — sequence number")*)[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.SetTcpSeq "Link to this definition")  
Parameters:  seq[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.SetTcpSeq.seq "Permalink to this definition")  
sequence number

Type:  int

tcpSeq[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.tcpSeq "Link to this definition")  
sequence number

Type:  int

GetTcpAck()[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.GetTcpAck "Link to this definition")  
Returns:  Ack number

Return type:  int

SetTcpAck(*[ack](#tts.lib.ethernet.PacketTcp.PacketTcp.SetTcpAck.ack "tts.lib.ethernet.PacketTcp.PacketTcp.SetTcpAck.ack (Python parameter) — Ack number")*)[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.SetTcpAck "Link to this definition")  
Parameters:  ack[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.SetTcpAck.ack "Permalink to this definition")  
Ack number

Type:  int

tcpAck[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.tcpAck "Link to this definition")  
Ack number

Type:  int

GetTcpOffset()[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.GetTcpOffset "Link to this definition")  
Returns:  TCP offset

Return type:  int

SetTcpOffset(*[offset](#tts.lib.ethernet.PacketTcp.PacketTcp.SetTcpOffset "tts.lib.ethernet.PacketTcp.PacketTcp.SetTcpOffset.offset (Python parameter)")*)[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.SetTcpOffset "Link to this definition")  
Param:  
TCP offset

Type:  int

tcpOffset[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.tcpOffset "Link to this definition")  
TCP offset

Type:  int

GetTcpFlags()[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.GetTcpFlags "Link to this definition")  
Returns:  flags

Return type:  int

SetTcpFlags(*[flags](#tts.lib.ethernet.PacketTcp.PacketTcp.SetTcpFlags.flags "tts.lib.ethernet.PacketTcp.PacketTcp.SetTcpFlags.flags (Python parameter) — flags")*)[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.SetTcpFlags "Link to this definition")  
Parameters:  flags[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.SetTcpFlags.flags "Permalink to this definition")  
flags

Type:  int

tcpFlags[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.tcpFlags "Link to this definition")  
flags

Type:  int

GetTcpWindow()[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.GetTcpWindow "Link to this definition")  
Returns:  window

Return type:  int

SetTcpWindow(*[win](#tts.lib.ethernet.PacketTcp.PacketTcp.SetTcpWindow "tts.lib.ethernet.PacketTcp.PacketTcp.SetTcpWindow.win (Python parameter)")*)[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.SetTcpWindow "Link to this definition")  
Param:  
window

Type:  int

tcpWindow[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.tcpWindow "Link to this definition")  
window

Type:  int

GetTcpChecksum()[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.GetTcpChecksum "Link to this definition")  
Returns:  checksum

Return type:  int

SetTcpChecksum(*[checksum](#tts.lib.ethernet.PacketTcp.PacketTcp.SetTcpChecksum.checksum "tts.lib.ethernet.PacketTcp.PacketTcp.SetTcpChecksum.checksum (Python parameter) — checksum")*)[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.SetTcpChecksum "Link to this definition")  
Parameters:  checksum : int[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.SetTcpChecksum.checksum "Permalink to this definition")  
checksum

tcpChecksum[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.tcpChecksum "Link to this definition")  
checksum

Type:  int

GetTcpUrgent()[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.GetTcpUrgent "Link to this definition")  
Returns:  urgent pointer

Return type:  int

SetTcpUrgent(*[urgent](#tts.lib.ethernet.PacketTcp.PacketTcp.SetTcpUrgent.urgent "tts.lib.ethernet.PacketTcp.PacketTcp.SetTcpUrgent.urgent (Python parameter) — urgent pointer")*)[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.SetTcpUrgent "Link to this definition")  
Parameters:  urgent : int[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.SetTcpUrgent.urgent "Permalink to this definition")  
urgent pointer

tcpUrgent[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.tcpUrgent "Link to this definition")  
urgent pointer

Type:  int

GetTcpPayload()[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.GetTcpPayload "Link to this definition")  
Returns:  TCP payload

Return type:  bytes

SetTcpPayload(*[payload](#tts.lib.ethernet.PacketTcp.PacketTcp.SetTcpPayload.payload "tts.lib.ethernet.PacketTcp.PacketTcp.SetTcpPayload.payload (Python parameter) — TCP payload")*)[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.SetTcpPayload "Link to this definition")  
Parameters:  payload : bytes[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.SetTcpPayload.payload "Permalink to this definition")  
TCP payload

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

FindParent(*[protocol](#tts.lib.ethernet.PacketTcp.PacketTcp.FindParent.protocol "tts.lib.ethernet.PacketTcp.PacketTcp.FindParent.protocol (Python parameter) — The required protocol name.")*)[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.FindParent "Link to this definition")  
*Only for pseudo signals in trace analysis!* Returns the requested protocol object if present, otherwise a [`NoProtocol`](busdatastructuresTraceanalysis.md#tts.lib.ethernet.PacketEthernet.NoProtocol "tts.lib.ethernet.PacketEthernet.NoProtocol (Python class) — Represents a non-present protocol. Accessing any other parent of a non-present protocol will also yield a NoProtocol object. Accessing any protocol specific attributes will lead to an AttributeError since the specific protocol is not available. The boolean value of a NoProtocol object is always False, such that it can be used to check for the precense/absence of a protocol layer.") object.

Parameters:  protocol : [OsiProtocol](busdatastructuresTraceanalysis.md#tts.lib.ethernet.PacketEthernet.OsiProtocol "tts.lib.ethernet.PacketEthernet.OsiProtocol (Python class) — String Enumeration class representing the supported protocol layers.")[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.FindParent.protocol "Permalink to this definition")  
The required protocol name.

Returns:  The required parent protocol object.

Return type:  [EthernetProtocolBase](busdatastructuresTraceanalysis.md#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase (Python class) — Base class for all protocol classes.")

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

GetVlanCfi(*[ixVlanTags](#tts.lib.ethernet.PacketTcp.PacketTcp.GetVlanCfi "tts.lib.ethernet.PacketTcp.PacketTcp.GetVlanCfi.ixVlanTags (Python parameter)")*)[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.GetVlanCfi "Link to this definition")  
Returns:  802.1a canonical format indicator

Return type:  int

GetVlanCfiOuter(*[ixVlanTags](#tts.lib.ethernet.PacketTcp.PacketTcp.GetVlanCfiOuter "tts.lib.ethernet.PacketTcp.PacketTcp.GetVlanCfiOuter.ixVlanTags (Python parameter)")*)[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.GetVlanCfiOuter "Link to this definition")  
Returns:  802.1ad canonical format indicator

Return type:  int

GetVlanPcp(*[ixVlanTags](#tts.lib.ethernet.PacketTcp.PacketTcp.GetVlanPcp "tts.lib.ethernet.PacketTcp.PacketTcp.GetVlanPcp.ixVlanTags (Python parameter)")*)[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.GetVlanPcp "Link to this definition")  
Returns:  802.1a priority code point

Return type:  int

GetVlanPcpOuter(*[ixVlanTags](#tts.lib.ethernet.PacketTcp.PacketTcp.GetVlanPcpOuter "tts.lib.ethernet.PacketTcp.PacketTcp.GetVlanPcpOuter.ixVlanTags (Python parameter)")*)[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.GetVlanPcpOuter "Link to this definition")  
Returns:  802.1ad priority code point

Return type:  int

GetVlanVid(*[ixVlanTags](#tts.lib.ethernet.PacketTcp.PacketTcp.GetVlanVid "tts.lib.ethernet.PacketTcp.PacketTcp.GetVlanVid.ixVlanTags (Python parameter)")*)[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.GetVlanVid "Link to this definition")  
Returns:  802.1a VLAN id

Return type:  int

GetVlanVidOuter(*[ixVlanTags](#tts.lib.ethernet.PacketTcp.PacketTcp.GetVlanVidOuter "tts.lib.ethernet.PacketTcp.PacketTcp.GetVlanVidOuter.ixVlanTags (Python parameter)")*)[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.GetVlanVidOuter "Link to this definition")  
Returns:  802.1ad VLAN id

Return type:  int

PK_CLASS[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.PK_CLASS "Link to this definition")  
alias of `IP`

SetEthDstMac(*[mac](#tts.lib.ethernet.PacketTcp.PacketTcp.SetEthDstMac.mac "tts.lib.ethernet.PacketTcp.PacketTcp.SetEthDstMac.mac (Python parameter) — target MAC address e.g.")*)[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.SetEthDstMac "Link to this definition")  
Parameters:  mac : str[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.SetEthDstMac.mac "Permalink to this definition")  
target MAC address e.g. DE:AD:BE:EF:FF:00

SetEthPayload(*[payload](#tts.lib.ethernet.PacketTcp.PacketTcp.SetEthPayload.payload "tts.lib.ethernet.PacketTcp.PacketTcp.SetEthPayload.payload (Python parameter) — Ethernet payload")*)[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.SetEthPayload "Link to this definition")  
Parameters:  payload : bytes[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.SetEthPayload.payload "Permalink to this definition")  
Ethernet payload

SetEthSrcMac(*[mac](#tts.lib.ethernet.PacketTcp.PacketTcp.SetEthSrcMac.mac "tts.lib.ethernet.PacketTcp.PacketTcp.SetEthSrcMac.mac (Python parameter) — source MAC addres e.g.")*)[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.SetEthSrcMac "Link to this definition")  
Parameters:  mac : str[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.SetEthSrcMac.mac "Permalink to this definition")  
source MAC addres e.g. DE:AD:BE:EF:FF:00

SetEthType(*[ethType](#tts.lib.ethernet.PacketTcp.PacketTcp.SetEthType.ethType "tts.lib.ethernet.PacketTcp.PacketTcp.SetEthType.ethType (Python parameter) — ethernet protocol type")*)[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.SetEthType "Link to this definition")  
Parameters:  ethType : int[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.SetEthType.ethType "Permalink to this definition")  
ethernet protocol type

SetIpChecksum(*[checksum](#tts.lib.ethernet.PacketTcp.PacketTcp.SetIpChecksum.checksum "tts.lib.ethernet.PacketTcp.PacketTcp.SetIpChecksum.checksum (Python parameter) — checksum")*)[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.SetIpChecksum "Link to this definition")  
Parameters:  checksum : int[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.SetIpChecksum.checksum "Permalink to this definition")  
checksum

SetIpDst(*[addr](#tts.lib.ethernet.PacketTcp.PacketTcp.SetIpDst.addr "tts.lib.ethernet.PacketTcp.PacketTcp.SetIpDst.addr (Python parameter) — target IP address e.g.")*)[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.SetIpDst "Link to this definition")  
Parameters:  addr : str[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.SetIpDst.addr "Permalink to this definition")  
target IP address e.g. 127.0.0.1

SetIpIdent(*[ident](#tts.lib.ethernet.PacketTcp.PacketTcp.SetIpIdent.ident "tts.lib.ethernet.PacketTcp.PacketTcp.SetIpIdent.ident (Python parameter) — identifier")*)[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.SetIpIdent "Link to this definition")  
Parameters:  ident : int[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.SetIpIdent.ident "Permalink to this definition")  
identifier

SetIpLen(*[length](#tts.lib.ethernet.PacketTcp.PacketTcp.SetIpLen.length "tts.lib.ethernet.PacketTcp.PacketTcp.SetIpLen.length (Python parameter) — packet length")*)[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.SetIpLen "Link to this definition")  
Parameters:  length : int[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.SetIpLen.length "Permalink to this definition")  
packet length

SetIpOffset(*[offset](#tts.lib.ethernet.PacketTcp.PacketTcp.SetIpOffset.offset "tts.lib.ethernet.PacketTcp.PacketTcp.SetIpOffset.offset (Python parameter) — flags and offset combined")*)[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.SetIpOffset "Link to this definition")  
Parameters:  offset : int[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.SetIpOffset.offset "Permalink to this definition")  
flags and offset combined

SetIpPayload(*[payload](#tts.lib.ethernet.PacketTcp.PacketTcp.SetIpPayload.payload "tts.lib.ethernet.PacketTcp.PacketTcp.SetIpPayload.payload (Python parameter) — IP payload")*)[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.SetIpPayload "Link to this definition")  
Parameters:  payload : bytes[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.SetIpPayload.payload "Permalink to this definition")  
IP payload

SetIpProt(*[prot](#tts.lib.ethernet.PacketTcp.PacketTcp.SetIpProt.prot "tts.lib.ethernet.PacketTcp.PacketTcp.SetIpProt.prot (Python parameter) — protocol type")*)[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.SetIpProt "Link to this definition")  
Parameters:  prot : int[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.SetIpProt.prot "Permalink to this definition")  
protocol type

SetIpSrc(*[addr](#tts.lib.ethernet.PacketTcp.PacketTcp.SetIpSrc.addr "tts.lib.ethernet.PacketTcp.PacketTcp.SetIpSrc.addr (Python parameter) — source IP address e.g.")*)[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.SetIpSrc "Link to this definition")  
Parameters:  addr : str[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.SetIpSrc.addr "Permalink to this definition")  
source IP address e.g. 127.0.0.1

SetIpTos(*[tos](#tts.lib.ethernet.PacketTcp.PacketTcp.SetIpTos.tos "tts.lib.ethernet.PacketTcp.PacketTcp.SetIpTos.tos (Python parameter) — type of service")*)[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.SetIpTos "Link to this definition")  
Parameters:  tos : int[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.SetIpTos.tos "Permalink to this definition")  
type of service

SetIpTtl(*[ttl](#tts.lib.ethernet.PacketTcp.PacketTcp.SetIpTtl.ttl "tts.lib.ethernet.PacketTcp.PacketTcp.SetIpTtl.ttl (Python parameter) — TTL")*)[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.SetIpTtl "Link to this definition")  
Parameters:  ttl : int[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.SetIpTtl.ttl "Permalink to this definition")  
TTL

SetIpVersionAndHeaderLength(*[versionHeader](#tts.lib.ethernet.PacketTcp.PacketTcp.SetIpVersionAndHeaderLength.versionHeader "tts.lib.ethernet.PacketTcp.PacketTcp.SetIpVersionAndHeaderLength.versionHeader (Python parameter) — protocol version and header length")*)[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.SetIpVersionAndHeaderLength "Link to this definition")  
Parameters:  versionHeader : int[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.SetIpVersionAndHeaderLength.versionHeader "Permalink to this definition")  
protocol version and header length

SetTimestamp(*[timestamp](#tts.lib.ethernet.PacketTcp.PacketTcp.SetTimestamp.timestamp "tts.lib.ethernet.PacketTcp.PacketTcp.SetTimestamp.timestamp (Python parameter) — Receive timestamp in sec., None if not available")*)[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.SetTimestamp "Link to this definition")  
Parameters:  timestamp : float | None[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.SetTimestamp.timestamp "Permalink to this definition")  
Receive timestamp in sec., None if not available

SetVlanCfi(*[cfi](#tts.lib.ethernet.PacketTcp.PacketTcp.SetVlanCfi.cfi "tts.lib.ethernet.PacketTcp.PacketTcp.SetVlanCfi.cfi (Python parameter) — 802.1a canonical format indicator")*)[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.SetVlanCfi "Link to this definition")  
Parameters:  cfi : int[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.SetVlanCfi.cfi "Permalink to this definition")  
802.1a canonical format indicator

SetVlanCfiOuter(*[cfi](#tts.lib.ethernet.PacketTcp.PacketTcp.SetVlanCfiOuter.cfi "tts.lib.ethernet.PacketTcp.PacketTcp.SetVlanCfiOuter.cfi (Python parameter) — 802.1ad canonical format indicator")*)[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.SetVlanCfiOuter "Link to this definition")  
Parameters:  cfi : int[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.SetVlanCfiOuter.cfi "Permalink to this definition")  
802.1ad canonical format indicator

SetVlanPcp(*[pcp](#tts.lib.ethernet.PacketTcp.PacketTcp.SetVlanPcp.pcp "tts.lib.ethernet.PacketTcp.PacketTcp.SetVlanPcp.pcp (Python parameter) — 802.1a priority code point")*)[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.SetVlanPcp "Link to this definition")  
Parameters:  pcp : int[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.SetVlanPcp.pcp "Permalink to this definition")  
802.1a priority code point

SetVlanPcpOuter(*[pcp](#tts.lib.ethernet.PacketTcp.PacketTcp.SetVlanPcpOuter.pcp "tts.lib.ethernet.PacketTcp.PacketTcp.SetVlanPcpOuter.pcp (Python parameter) — 802.1ad priority code point")*)[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.SetVlanPcpOuter "Link to this definition")  
Parameters:  pcp : int[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.SetVlanPcpOuter.pcp "Permalink to this definition")  
802.1ad priority code point

SetVlanVid(*[vid](#tts.lib.ethernet.PacketTcp.PacketTcp.SetVlanVid.vid "tts.lib.ethernet.PacketTcp.PacketTcp.SetVlanVid.vid (Python parameter) — 802.1a VLAN id")*)[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.SetVlanVid "Link to this definition")  
Parameters:  vid : int[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.SetVlanVid.vid "Permalink to this definition")  
802.1a VLAN id

SetVlanVidOuter(*[vid](#tts.lib.ethernet.PacketTcp.PacketTcp.SetVlanVidOuter.vid "tts.lib.ethernet.PacketTcp.PacketTcp.SetVlanVidOuter.vid (Python parameter) — 802.1ad VLAN id")*)[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.SetVlanVidOuter "Link to this definition")  
Parameters:  vid : int[¶](#tts.lib.ethernet.PacketTcp.PacketTcp.SetVlanVidOuter.vid "Permalink to this definition")  
802.1ad VLAN id

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

Return type:  [EthernetProtocolBase](busdatastructuresTraceanalysis.md#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase (Python class) — Base class for all protocol classes.") | None

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
Equivalent to method [`FindParent(protocol)`](#tts.lib.ethernet.PacketUdp.PacketUdp.FindParent "tts.lib.ethernet.PacketUdp.PacketUdp.FindParent (Python method) — Only for pseudo signals in trace analysis! Returns the requested protocol object if present, otherwise a NoProtocol object."). Direct access to parent protocols. *protocol* is one of [`OsiProtocol`](busdatastructuresTraceanalysis.md#tts.lib.ethernet.PacketEthernet.OsiProtocol "tts.lib.ethernet.PacketEthernet.OsiProtocol (Python class) — String Enumeration class representing the supported protocol layers.").

Example: Signal.eth.src provides the source MAC address of the Ethernet protocol layer.

Type:  [`EthernetProtocolBase`](busdatastructuresTraceanalysis.md#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase (Python class) — Base class for all protocol classes.")

CalcUdpLen()[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.CalcUdpLen "Link to this definition")  
Calculate and set the current length of this segment

GetUdpSrc()[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.GetUdpSrc "Link to this definition")  
Returns:  source port

Return type:  int

SetUdpSrc(*[port](#tts.lib.ethernet.PacketUdp.PacketUdp.SetUdpSrc.port "tts.lib.ethernet.PacketUdp.PacketUdp.SetUdpSrc.port (Python parameter) — source port")*)[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.SetUdpSrc "Link to this definition")  
Parameters:  port : int[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.SetUdpSrc.port "Permalink to this definition")  
source port

udpSrc[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.udpSrc "Link to this definition")  
source port

Type:  int

GetUdpDst()[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.GetUdpDst "Link to this definition")  
Returns:  destination port

Return type:  int

SetUdpDst(*[port](#tts.lib.ethernet.PacketUdp.PacketUdp.SetUdpDst.port "tts.lib.ethernet.PacketUdp.PacketUdp.SetUdpDst.port (Python parameter) — destination port")*)[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.SetUdpDst "Link to this definition")  
Parameters:  port : int[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.SetUdpDst.port "Permalink to this definition")  
destination port

udpDst[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.udpDst "Link to this definition")  
destination port

Type:  int

GetUdpLen()[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.GetUdpLen "Link to this definition")  
Returns:  length of the UDP segment

Return type:  int

SetUdpLen(*[length](#tts.lib.ethernet.PacketUdp.PacketUdp.SetUdpLen.length "tts.lib.ethernet.PacketUdp.PacketUdp.SetUdpLen.length (Python parameter) — length of the UDP segment")*)[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.SetUdpLen "Link to this definition")  
Parameters:  length : int[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.SetUdpLen.length "Permalink to this definition")  
length of the UDP segment

udpLen[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.udpLen "Link to this definition")  
length of the UDP segment

Type:  int

GetUdpChecksum()[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.GetUdpChecksum "Link to this definition")  
Returns:  checksum

Return type:  int

SetUdpChecksum(*[checksum](#tts.lib.ethernet.PacketUdp.PacketUdp.SetUdpChecksum.checksum "tts.lib.ethernet.PacketUdp.PacketUdp.SetUdpChecksum.checksum (Python parameter) — checksum")*)[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.SetUdpChecksum "Link to this definition")  
Parameters:  checksum : int[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.SetUdpChecksum.checksum "Permalink to this definition")  
checksum

udpChecksum[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.udpChecksum "Link to this definition")  
checksum

Type:  int

GetUdpPayload()[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.GetUdpPayload "Link to this definition")  
Returns:  UDP payload

Return type:  bytes

SetUdpPayload(*[payload](#tts.lib.ethernet.PacketUdp.PacketUdp.SetUdpPayload.payload "tts.lib.ethernet.PacketUdp.PacketUdp.SetUdpPayload.payload (Python parameter) — UDP payload")*)[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.SetUdpPayload "Link to this definition")  
Parameters:  payload : bytes[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.SetUdpPayload.payload "Permalink to this definition")  
UDP payload

udpPayload[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.udpPayload "Link to this definition")  
UDP payload

Type:  bytes

CalcIpLen()[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.CalcIpLen "Link to this definition")  
Calculate and set the current length of this IP packet

FindParent(*[protocol](#tts.lib.ethernet.PacketUdp.PacketUdp.FindParent.protocol "tts.lib.ethernet.PacketUdp.PacketUdp.FindParent.protocol (Python parameter) — The required protocol name.")*)[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.FindParent "Link to this definition")  
*Only for pseudo signals in trace analysis!* Returns the requested protocol object if present, otherwise a [`NoProtocol`](busdatastructuresTraceanalysis.md#tts.lib.ethernet.PacketEthernet.NoProtocol "tts.lib.ethernet.PacketEthernet.NoProtocol (Python class) — Represents a non-present protocol. Accessing any other parent of a non-present protocol will also yield a NoProtocol object. Accessing any protocol specific attributes will lead to an AttributeError since the specific protocol is not available. The boolean value of a NoProtocol object is always False, such that it can be used to check for the precense/absence of a protocol layer.") object.

Parameters:  protocol : [OsiProtocol](busdatastructuresTraceanalysis.md#tts.lib.ethernet.PacketEthernet.OsiProtocol "tts.lib.ethernet.PacketEthernet.OsiProtocol (Python class) — String Enumeration class representing the supported protocol layers.")[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.FindParent.protocol "Permalink to this definition")  
The required protocol name.

Returns:  The required parent protocol object.

Return type:  [EthernetProtocolBase](busdatastructuresTraceanalysis.md#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase (Python class) — Base class for all protocol classes.")

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

GetVlanCfi(*[ixVlanTags](#tts.lib.ethernet.PacketUdp.PacketUdp.GetVlanCfi "tts.lib.ethernet.PacketUdp.PacketUdp.GetVlanCfi.ixVlanTags (Python parameter)")*)[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.GetVlanCfi "Link to this definition")  
Returns:  802.1a canonical format indicator

Return type:  int

GetVlanCfiOuter(*[ixVlanTags](#tts.lib.ethernet.PacketUdp.PacketUdp.GetVlanCfiOuter "tts.lib.ethernet.PacketUdp.PacketUdp.GetVlanCfiOuter.ixVlanTags (Python parameter)")*)[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.GetVlanCfiOuter "Link to this definition")  
Returns:  802.1ad canonical format indicator

Return type:  int

GetVlanPcp(*[ixVlanTags](#tts.lib.ethernet.PacketUdp.PacketUdp.GetVlanPcp "tts.lib.ethernet.PacketUdp.PacketUdp.GetVlanPcp.ixVlanTags (Python parameter)")*)[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.GetVlanPcp "Link to this definition")  
Returns:  802.1a priority code point

Return type:  int

GetVlanPcpOuter(*[ixVlanTags](#tts.lib.ethernet.PacketUdp.PacketUdp.GetVlanPcpOuter "tts.lib.ethernet.PacketUdp.PacketUdp.GetVlanPcpOuter.ixVlanTags (Python parameter)")*)[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.GetVlanPcpOuter "Link to this definition")  
Returns:  802.1ad priority code point

Return type:  int

GetVlanVid(*[ixVlanTags](#tts.lib.ethernet.PacketUdp.PacketUdp.GetVlanVid "tts.lib.ethernet.PacketUdp.PacketUdp.GetVlanVid.ixVlanTags (Python parameter)")*)[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.GetVlanVid "Link to this definition")  
Returns:  802.1a VLAN id

Return type:  int

GetVlanVidOuter(*[ixVlanTags](#tts.lib.ethernet.PacketUdp.PacketUdp.GetVlanVidOuter "tts.lib.ethernet.PacketUdp.PacketUdp.GetVlanVidOuter.ixVlanTags (Python parameter)")*)[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.GetVlanVidOuter "Link to this definition")  
Returns:  802.1ad VLAN id

Return type:  int

PK_CLASS[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.PK_CLASS "Link to this definition")  
alias of `IP`

SetEthDstMac(*[mac](#tts.lib.ethernet.PacketUdp.PacketUdp.SetEthDstMac.mac "tts.lib.ethernet.PacketUdp.PacketUdp.SetEthDstMac.mac (Python parameter) — target MAC address e.g.")*)[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.SetEthDstMac "Link to this definition")  
Parameters:  mac : str[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.SetEthDstMac.mac "Permalink to this definition")  
target MAC address e.g. DE:AD:BE:EF:FF:00

SetEthPayload(*[payload](#tts.lib.ethernet.PacketUdp.PacketUdp.SetEthPayload.payload "tts.lib.ethernet.PacketUdp.PacketUdp.SetEthPayload.payload (Python parameter) — Ethernet payload")*)[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.SetEthPayload "Link to this definition")  
Parameters:  payload : bytes[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.SetEthPayload.payload "Permalink to this definition")  
Ethernet payload

SetEthSrcMac(*[mac](#tts.lib.ethernet.PacketUdp.PacketUdp.SetEthSrcMac.mac "tts.lib.ethernet.PacketUdp.PacketUdp.SetEthSrcMac.mac (Python parameter) — source MAC addres e.g.")*)[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.SetEthSrcMac "Link to this definition")  
Parameters:  mac : str[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.SetEthSrcMac.mac "Permalink to this definition")  
source MAC addres e.g. DE:AD:BE:EF:FF:00

SetEthType(*[ethType](#tts.lib.ethernet.PacketUdp.PacketUdp.SetEthType.ethType "tts.lib.ethernet.PacketUdp.PacketUdp.SetEthType.ethType (Python parameter) — ethernet protocol type")*)[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.SetEthType "Link to this definition")  
Parameters:  ethType : int[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.SetEthType.ethType "Permalink to this definition")  
ethernet protocol type

SetIpChecksum(*[checksum](#tts.lib.ethernet.PacketUdp.PacketUdp.SetIpChecksum.checksum "tts.lib.ethernet.PacketUdp.PacketUdp.SetIpChecksum.checksum (Python parameter) — checksum")*)[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.SetIpChecksum "Link to this definition")  
Parameters:  checksum : int[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.SetIpChecksum.checksum "Permalink to this definition")  
checksum

SetIpDst(*[addr](#tts.lib.ethernet.PacketUdp.PacketUdp.SetIpDst.addr "tts.lib.ethernet.PacketUdp.PacketUdp.SetIpDst.addr (Python parameter) — target IP address e.g.")*)[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.SetIpDst "Link to this definition")  
Parameters:  addr : str[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.SetIpDst.addr "Permalink to this definition")  
target IP address e.g. 127.0.0.1

SetIpIdent(*[ident](#tts.lib.ethernet.PacketUdp.PacketUdp.SetIpIdent.ident "tts.lib.ethernet.PacketUdp.PacketUdp.SetIpIdent.ident (Python parameter) — identifier")*)[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.SetIpIdent "Link to this definition")  
Parameters:  ident : int[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.SetIpIdent.ident "Permalink to this definition")  
identifier

SetIpLen(*[length](#tts.lib.ethernet.PacketUdp.PacketUdp.SetIpLen.length "tts.lib.ethernet.PacketUdp.PacketUdp.SetIpLen.length (Python parameter) — packet length")*)[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.SetIpLen "Link to this definition")  
Parameters:  length : int[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.SetIpLen.length "Permalink to this definition")  
packet length

SetIpOffset(*[offset](#tts.lib.ethernet.PacketUdp.PacketUdp.SetIpOffset.offset "tts.lib.ethernet.PacketUdp.PacketUdp.SetIpOffset.offset (Python parameter) — flags and offset combined")*)[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.SetIpOffset "Link to this definition")  
Parameters:  offset : int[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.SetIpOffset.offset "Permalink to this definition")  
flags and offset combined

SetIpPayload(*[payload](#tts.lib.ethernet.PacketUdp.PacketUdp.SetIpPayload.payload "tts.lib.ethernet.PacketUdp.PacketUdp.SetIpPayload.payload (Python parameter) — IP payload")*)[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.SetIpPayload "Link to this definition")  
Parameters:  payload : bytes[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.SetIpPayload.payload "Permalink to this definition")  
IP payload

SetIpProt(*[prot](#tts.lib.ethernet.PacketUdp.PacketUdp.SetIpProt.prot "tts.lib.ethernet.PacketUdp.PacketUdp.SetIpProt.prot (Python parameter) — protocol type")*)[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.SetIpProt "Link to this definition")  
Parameters:  prot : int[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.SetIpProt.prot "Permalink to this definition")  
protocol type

SetIpSrc(*[addr](#tts.lib.ethernet.PacketUdp.PacketUdp.SetIpSrc.addr "tts.lib.ethernet.PacketUdp.PacketUdp.SetIpSrc.addr (Python parameter) — source IP address e.g.")*)[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.SetIpSrc "Link to this definition")  
Parameters:  addr : str[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.SetIpSrc.addr "Permalink to this definition")  
source IP address e.g. 127.0.0.1

SetIpTos(*[tos](#tts.lib.ethernet.PacketUdp.PacketUdp.SetIpTos.tos "tts.lib.ethernet.PacketUdp.PacketUdp.SetIpTos.tos (Python parameter) — type of service")*)[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.SetIpTos "Link to this definition")  
Parameters:  tos : int[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.SetIpTos.tos "Permalink to this definition")  
type of service

SetIpTtl(*[ttl](#tts.lib.ethernet.PacketUdp.PacketUdp.SetIpTtl.ttl "tts.lib.ethernet.PacketUdp.PacketUdp.SetIpTtl.ttl (Python parameter) — TTL")*)[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.SetIpTtl "Link to this definition")  
Parameters:  ttl : int[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.SetIpTtl.ttl "Permalink to this definition")  
TTL

SetIpVersionAndHeaderLength(*[versionHeader](#tts.lib.ethernet.PacketUdp.PacketUdp.SetIpVersionAndHeaderLength.versionHeader "tts.lib.ethernet.PacketUdp.PacketUdp.SetIpVersionAndHeaderLength.versionHeader (Python parameter) — protocol version and header length")*)[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.SetIpVersionAndHeaderLength "Link to this definition")  
Parameters:  versionHeader : int[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.SetIpVersionAndHeaderLength.versionHeader "Permalink to this definition")  
protocol version and header length

SetTimestamp(*[timestamp](#tts.lib.ethernet.PacketUdp.PacketUdp.SetTimestamp.timestamp "tts.lib.ethernet.PacketUdp.PacketUdp.SetTimestamp.timestamp (Python parameter) — Receive timestamp in sec., None if not available")*)[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.SetTimestamp "Link to this definition")  
Parameters:  timestamp : float | None[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.SetTimestamp.timestamp "Permalink to this definition")  
Receive timestamp in sec., None if not available

SetVlanCfi(*[cfi](#tts.lib.ethernet.PacketUdp.PacketUdp.SetVlanCfi.cfi "tts.lib.ethernet.PacketUdp.PacketUdp.SetVlanCfi.cfi (Python parameter) — 802.1a canonical format indicator")*)[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.SetVlanCfi "Link to this definition")  
Parameters:  cfi : int[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.SetVlanCfi.cfi "Permalink to this definition")  
802.1a canonical format indicator

SetVlanCfiOuter(*[cfi](#tts.lib.ethernet.PacketUdp.PacketUdp.SetVlanCfiOuter.cfi "tts.lib.ethernet.PacketUdp.PacketUdp.SetVlanCfiOuter.cfi (Python parameter) — 802.1ad canonical format indicator")*)[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.SetVlanCfiOuter "Link to this definition")  
Parameters:  cfi : int[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.SetVlanCfiOuter.cfi "Permalink to this definition")  
802.1ad canonical format indicator

SetVlanPcp(*[pcp](#tts.lib.ethernet.PacketUdp.PacketUdp.SetVlanPcp.pcp "tts.lib.ethernet.PacketUdp.PacketUdp.SetVlanPcp.pcp (Python parameter) — 802.1a priority code point")*)[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.SetVlanPcp "Link to this definition")  
Parameters:  pcp : int[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.SetVlanPcp.pcp "Permalink to this definition")  
802.1a priority code point

SetVlanPcpOuter(*[pcp](#tts.lib.ethernet.PacketUdp.PacketUdp.SetVlanPcpOuter.pcp "tts.lib.ethernet.PacketUdp.PacketUdp.SetVlanPcpOuter.pcp (Python parameter) — 802.1ad priority code point")*)[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.SetVlanPcpOuter "Link to this definition")  
Parameters:  pcp : int[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.SetVlanPcpOuter.pcp "Permalink to this definition")  
802.1ad priority code point

SetVlanVid(*[vid](#tts.lib.ethernet.PacketUdp.PacketUdp.SetVlanVid.vid "tts.lib.ethernet.PacketUdp.PacketUdp.SetVlanVid.vid (Python parameter) — 802.1a VLAN id")*)[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.SetVlanVid "Link to this definition")  
Parameters:  vid : int[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.SetVlanVid.vid "Permalink to this definition")  
802.1a VLAN id

SetVlanVidOuter(*[vid](#tts.lib.ethernet.PacketUdp.PacketUdp.SetVlanVidOuter.vid "tts.lib.ethernet.PacketUdp.PacketUdp.SetVlanVidOuter.vid (Python parameter) — 802.1ad VLAN id")*)[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.SetVlanVidOuter "Link to this definition")  
Parameters:  vid : int[¶](#tts.lib.ethernet.PacketUdp.PacketUdp.SetVlanVidOuter.vid "Permalink to this definition")  
802.1ad VLAN id

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

Return type:  [EthernetProtocolBase](busdatastructuresTraceanalysis.md#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase (Python class) — Base class for all protocol classes.") | None

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
Equivalent to method [`FindParent(protocol)`](#tts.lib.ethernet.PacketPtp.PacketPtpSync.FindParent "tts.lib.ethernet.PacketPtp.PacketPtpSync.FindParent (Python method) — Only for pseudo signals in trace analysis! Returns the requested protocol object if present, otherwise a NoProtocol object."). Direct access to parent protocols. *protocol* is one of [`OsiProtocol`](busdatastructuresTraceanalysis.md#tts.lib.ethernet.PacketEthernet.OsiProtocol "tts.lib.ethernet.PacketEthernet.OsiProtocol (Python class) — String Enumeration class representing the supported protocol layers.").

Example: Signal.eth.src provides the source MAC address of the Ethernet protocol layer.

Type:  [`EthernetProtocolBase`](busdatastructuresTraceanalysis.md#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase (Python class) — Base class for all protocol classes.")

FindParent(*[protocol](#tts.lib.ethernet.PacketPtp.PacketPtpSync.FindParent.protocol "tts.lib.ethernet.PacketPtp.PacketPtpSync.FindParent.protocol (Python parameter) — The required protocol name.")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.FindParent "Link to this definition")  
*Only for pseudo signals in trace analysis!* Returns the requested protocol object if present, otherwise a [`NoProtocol`](busdatastructuresTraceanalysis.md#tts.lib.ethernet.PacketEthernet.NoProtocol "tts.lib.ethernet.PacketEthernet.NoProtocol (Python class) — Represents a non-present protocol. Accessing any other parent of a non-present protocol will also yield a NoProtocol object. Accessing any protocol specific attributes will lead to an AttributeError since the specific protocol is not available. The boolean value of a NoProtocol object is always False, such that it can be used to check for the precense/absence of a protocol layer.") object.

Parameters:  protocol : [OsiProtocol](busdatastructuresTraceanalysis.md#tts.lib.ethernet.PacketEthernet.OsiProtocol "tts.lib.ethernet.PacketEthernet.OsiProtocol (Python class) — String Enumeration class representing the supported protocol layers.")[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.FindParent.protocol "Permalink to this definition")  
The required protocol name.

Returns:  The required parent protocol object.

Return type:  [EthernetProtocolBase](busdatastructuresTraceanalysis.md#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase (Python class) — Base class for all protocol classes.")

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

GetVlanCfi(*[ixVlanTags](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetVlanCfi "tts.lib.ethernet.PacketPtp.PacketPtpSync.GetVlanCfi.ixVlanTags (Python parameter)")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetVlanCfi "Link to this definition")  
Returns:  802.1a canonical format indicator

Return type:  int

GetVlanCfiOuter(*[ixVlanTags](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetVlanCfiOuter "tts.lib.ethernet.PacketPtp.PacketPtpSync.GetVlanCfiOuter.ixVlanTags (Python parameter)")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetVlanCfiOuter "Link to this definition")  
Returns:  802.1ad canonical format indicator

Return type:  int

GetVlanPcp(*[ixVlanTags](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetVlanPcp "tts.lib.ethernet.PacketPtp.PacketPtpSync.GetVlanPcp.ixVlanTags (Python parameter)")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetVlanPcp "Link to this definition")  
Returns:  802.1a priority code point

Return type:  int

GetVlanPcpOuter(*[ixVlanTags](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetVlanPcpOuter "tts.lib.ethernet.PacketPtp.PacketPtpSync.GetVlanPcpOuter.ixVlanTags (Python parameter)")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetVlanPcpOuter "Link to this definition")  
Returns:  802.1ad priority code point

Return type:  int

GetVlanVid(*[ixVlanTags](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetVlanVid "tts.lib.ethernet.PacketPtp.PacketPtpSync.GetVlanVid.ixVlanTags (Python parameter)")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetVlanVid "Link to this definition")  
Returns:  802.1a VLAN id

Return type:  int

GetVlanVidOuter(*[ixVlanTags](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetVlanVidOuter "tts.lib.ethernet.PacketPtp.PacketPtpSync.GetVlanVidOuter.ixVlanTags (Python parameter)")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.GetVlanVidOuter "Link to this definition")  
Returns:  802.1ad VLAN id

Return type:  int

SetEthDstMac(*[mac](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetEthDstMac.mac "tts.lib.ethernet.PacketPtp.PacketPtpSync.SetEthDstMac.mac (Python parameter) — target MAC address e.g.")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetEthDstMac "Link to this definition")  
Parameters:  mac : str[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetEthDstMac.mac "Permalink to this definition")  
target MAC address e.g. DE:AD:BE:EF:FF:00

SetEthPayload(*[payload](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetEthPayload.payload "tts.lib.ethernet.PacketPtp.PacketPtpSync.SetEthPayload.payload (Python parameter) — Ethernet payload")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetEthPayload "Link to this definition")  
Parameters:  payload : bytes[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetEthPayload.payload "Permalink to this definition")  
Ethernet payload

SetEthSrcMac(*[mac](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetEthSrcMac.mac "tts.lib.ethernet.PacketPtp.PacketPtpSync.SetEthSrcMac.mac (Python parameter) — source MAC addres e.g.")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetEthSrcMac "Link to this definition")  
Parameters:  mac : str[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetEthSrcMac.mac "Permalink to this definition")  
source MAC addres e.g. DE:AD:BE:EF:FF:00

SetEthType(*[ethType](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetEthType.ethType "tts.lib.ethernet.PacketPtp.PacketPtpSync.SetEthType.ethType (Python parameter) — ethernet protocol type")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetEthType "Link to this definition")  
Parameters:  ethType : int[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetEthType.ethType "Permalink to this definition")  
ethernet protocol type

SetPtpControl(*[control](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetPtpControl.control "tts.lib.ethernet.PacketPtp.PacketPtpSync.SetPtpControl.control (Python parameter) — PTP control field")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetPtpControl "Link to this definition")  
Parameters:  control : int[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetPtpControl.control "Permalink to this definition")  
PTP control field

SetPtpCorrectionField(*[correctionField](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetPtpCorrectionField.correctionField "tts.lib.ethernet.PacketPtp.PacketPtpSync.SetPtpCorrectionField.correctionField (Python parameter) — PTP correction field")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetPtpCorrectionField "Link to this definition")  
Parameters:  correctionField : int[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetPtpCorrectionField.correctionField "Permalink to this definition")  
PTP correction field

SetPtpDomainNumber(*[domainNumber](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetPtpDomainNumber.domainNumber "tts.lib.ethernet.PacketPtp.PacketPtpSync.SetPtpDomainNumber.domainNumber (Python parameter) — PTP domain number")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetPtpDomainNumber "Link to this definition")  
Parameters:  domainNumber : int[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetPtpDomainNumber.domainNumber "Permalink to this definition")  
PTP domain number

SetPtpFlags(*[flags](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetPtpFlags.flags "tts.lib.ethernet.PacketPtp.PacketPtpSync.SetPtpFlags.flags (Python parameter) — PTP flags")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetPtpFlags "Link to this definition")  
Parameters:  flags : int[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetPtpFlags.flags "Permalink to this definition")  
PTP flags

SetPtpLogMsgInterval(*[logMsgInterval](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetPtpLogMsgInterval.logMsgInterval "tts.lib.ethernet.PacketPtp.PacketPtpSync.SetPtpLogMsgInterval.logMsgInterval (Python parameter) — log message interval")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetPtpLogMsgInterval "Link to this definition")  
Parameters:  logMsgInterval : int[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetPtpLogMsgInterval.logMsgInterval "Permalink to this definition")  
log message interval

SetPtpMsgLen(*[msgLen](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetPtpMsgLen.msgLen "tts.lib.ethernet.PacketPtp.PacketPtpSync.SetPtpMsgLen.msgLen (Python parameter) — PTP message length")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetPtpMsgLen "Link to this definition")  
Parameters:  msgLen : int[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetPtpMsgLen.msgLen "Permalink to this definition")  
PTP message length

SetPtpMsgType(*[msgType](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetPtpMsgType.msgType "tts.lib.ethernet.PacketPtp.PacketPtpSync.SetPtpMsgType.msgType (Python parameter) — PTP message type")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetPtpMsgType "Link to this definition")  
Parameters:  msgType : int[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetPtpMsgType.msgType "Permalink to this definition")  
PTP message type

SetPtpSequenceId(*[sequenceId](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetPtpSequenceId.sequenceId "tts.lib.ethernet.PacketPtp.PacketPtpSync.SetPtpSequenceId.sequenceId (Python parameter) — PTP sequence ID")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetPtpSequenceId "Link to this definition")  
Parameters:  sequenceId : int[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetPtpSequenceId.sequenceId "Permalink to this definition")  
PTP sequence ID

SetPtpSourcePortIdentity(*[sourcePortIdentity](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetPtpSourcePortIdentity.sourcePortIdentity "tts.lib.ethernet.PacketPtp.PacketPtpSync.SetPtpSourcePortIdentity.sourcePortIdentity (Python parameter) — PTP source port identity")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetPtpSourcePortIdentity "Link to this definition")  
Parameters:  sourcePortIdentity : bytes[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetPtpSourcePortIdentity.sourcePortIdentity "Permalink to this definition")  
PTP source port identity

SetPtpVersion(*[version](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetPtpVersion.version "tts.lib.ethernet.PacketPtp.PacketPtpSync.SetPtpVersion.version (Python parameter) — PTP version")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetPtpVersion "Link to this definition")  
Parameters:  version : int[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetPtpVersion.version "Permalink to this definition")  
PTP version

SetTimestamp(*[timestamp](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetTimestamp.timestamp "tts.lib.ethernet.PacketPtp.PacketPtpSync.SetTimestamp.timestamp (Python parameter) — Receive timestamp in sec., None if not available")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetTimestamp "Link to this definition")  
Parameters:  timestamp : float | None[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetTimestamp.timestamp "Permalink to this definition")  
Receive timestamp in sec., None if not available

SetVlanCfi(*[cfi](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetVlanCfi.cfi "tts.lib.ethernet.PacketPtp.PacketPtpSync.SetVlanCfi.cfi (Python parameter) — 802.1a canonical format indicator")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetVlanCfi "Link to this definition")  
Parameters:  cfi : int[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetVlanCfi.cfi "Permalink to this definition")  
802.1a canonical format indicator

SetVlanCfiOuter(*[cfi](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetVlanCfiOuter.cfi "tts.lib.ethernet.PacketPtp.PacketPtpSync.SetVlanCfiOuter.cfi (Python parameter) — 802.1ad canonical format indicator")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetVlanCfiOuter "Link to this definition")  
Parameters:  cfi : int[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetVlanCfiOuter.cfi "Permalink to this definition")  
802.1ad canonical format indicator

SetVlanPcp(*[pcp](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetVlanPcp.pcp "tts.lib.ethernet.PacketPtp.PacketPtpSync.SetVlanPcp.pcp (Python parameter) — 802.1a priority code point")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetVlanPcp "Link to this definition")  
Parameters:  pcp : int[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetVlanPcp.pcp "Permalink to this definition")  
802.1a priority code point

SetVlanPcpOuter(*[pcp](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetVlanPcpOuter.pcp "tts.lib.ethernet.PacketPtp.PacketPtpSync.SetVlanPcpOuter.pcp (Python parameter) — 802.1ad priority code point")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetVlanPcpOuter "Link to this definition")  
Parameters:  pcp : int[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetVlanPcpOuter.pcp "Permalink to this definition")  
802.1ad priority code point

SetVlanVid(*[vid](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetVlanVid.vid "tts.lib.ethernet.PacketPtp.PacketPtpSync.SetVlanVid.vid (Python parameter) — 802.1a VLAN id")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetVlanVid "Link to this definition")  
Parameters:  vid : int[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetVlanVid.vid "Permalink to this definition")  
802.1a VLAN id

SetVlanVidOuter(*[vid](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetVlanVidOuter.vid "tts.lib.ethernet.PacketPtp.PacketPtpSync.SetVlanVidOuter.vid (Python parameter) — 802.1ad VLAN id")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetVlanVidOuter "Link to this definition")  
Parameters:  vid : int[¶](#tts.lib.ethernet.PacketPtp.PacketPtpSync.SetVlanVidOuter.vid "Permalink to this definition")  
802.1ad VLAN id

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

Return type:  [EthernetProtocolBase](busdatastructuresTraceanalysis.md#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase (Python class) — Base class for all protocol classes.") | None

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
Equivalent to method [`FindParent(protocol)`](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.FindParent "tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.FindParent (Python method) — Only for pseudo signals in trace analysis! Returns the requested protocol object if present, otherwise a NoProtocol object."). Direct access to parent protocols. *protocol* is one of [`OsiProtocol`](busdatastructuresTraceanalysis.md#tts.lib.ethernet.PacketEthernet.OsiProtocol "tts.lib.ethernet.PacketEthernet.OsiProtocol (Python class) — String Enumeration class representing the supported protocol layers.").

Example: Signal.eth.src provides the source MAC address of the Ethernet protocol layer.

Type:  [`EthernetProtocolBase`](busdatastructuresTraceanalysis.md#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase (Python class) — Base class for all protocol classes.")

GetPtpPreciseOriginTimestampSec()[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetPtpPreciseOriginTimestampSec "Link to this definition")  
Returns:  second portion of the PTP precise origin timestamp

Return type:  int

SetPtpPreciseOriginTimestampSec(*[preciseOriginTimestampSec](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetPtpPreciseOriginTimestampSec.preciseOriginTimestampSec "tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetPtpPreciseOriginTimestampSec.preciseOriginTimestampSec (Python parameter) — second portion of the PTP precise origin timestamp")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetPtpPreciseOriginTimestampSec "Link to this definition")  
Parameters:  preciseOriginTimestampSec : int[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetPtpPreciseOriginTimestampSec.preciseOriginTimestampSec "Permalink to this definition")  
second portion of the PTP precise origin timestamp

ptpPreciseOriginTimestampSec[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.ptpPreciseOriginTimestampSec "Link to this definition")  
second portion of the PTP precise origin timestamp

Type:  int

GetPtpPreciseOriginTimestampNSec()[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetPtpPreciseOriginTimestampNSec "Link to this definition")  
Returns:  nanosecond portion of the PTP precise origin timestamp

Return type:  int

SetPtpPreciseOriginTimestampNSec(*[preciseOriginTimestampNSec](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetPtpPreciseOriginTimestampNSec.preciseOriginTimestampNSec "tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetPtpPreciseOriginTimestampNSec.preciseOriginTimestampNSec (Python parameter) — nanosecond portion of the PTP precise origin timestamp")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetPtpPreciseOriginTimestampNSec "Link to this definition")  
Parameters:  preciseOriginTimestampNSec : int[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetPtpPreciseOriginTimestampNSec.preciseOriginTimestampNSec "Permalink to this definition")  
nanosecond portion of the PTP precise origin timestamp

ptpPreciseOriginTimestampNSec[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.ptpPreciseOriginTimestampNSec "Link to this definition")  
nanosecond portion of the PTP precise origin timestamp

Type:  int

FindParent(*[protocol](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.FindParent.protocol "tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.FindParent.protocol (Python parameter) — The required protocol name.")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.FindParent "Link to this definition")  
*Only for pseudo signals in trace analysis!* Returns the requested protocol object if present, otherwise a [`NoProtocol`](busdatastructuresTraceanalysis.md#tts.lib.ethernet.PacketEthernet.NoProtocol "tts.lib.ethernet.PacketEthernet.NoProtocol (Python class) — Represents a non-present protocol. Accessing any other parent of a non-present protocol will also yield a NoProtocol object. Accessing any protocol specific attributes will lead to an AttributeError since the specific protocol is not available. The boolean value of a NoProtocol object is always False, such that it can be used to check for the precense/absence of a protocol layer.") object.

Parameters:  protocol : [OsiProtocol](busdatastructuresTraceanalysis.md#tts.lib.ethernet.PacketEthernet.OsiProtocol "tts.lib.ethernet.PacketEthernet.OsiProtocol (Python class) — String Enumeration class representing the supported protocol layers.")[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.FindParent.protocol "Permalink to this definition")  
The required protocol name.

Returns:  The required parent protocol object.

Return type:  [EthernetProtocolBase](busdatastructuresTraceanalysis.md#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase (Python class) — Base class for all protocol classes.")

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

GetVlanCfi(*[ixVlanTags](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetVlanCfi "tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetVlanCfi.ixVlanTags (Python parameter)")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetVlanCfi "Link to this definition")  
Returns:  802.1a canonical format indicator

Return type:  int

GetVlanCfiOuter(*[ixVlanTags](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetVlanCfiOuter "tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetVlanCfiOuter.ixVlanTags (Python parameter)")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetVlanCfiOuter "Link to this definition")  
Returns:  802.1ad canonical format indicator

Return type:  int

GetVlanPcp(*[ixVlanTags](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetVlanPcp "tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetVlanPcp.ixVlanTags (Python parameter)")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetVlanPcp "Link to this definition")  
Returns:  802.1a priority code point

Return type:  int

GetVlanPcpOuter(*[ixVlanTags](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetVlanPcpOuter "tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetVlanPcpOuter.ixVlanTags (Python parameter)")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetVlanPcpOuter "Link to this definition")  
Returns:  802.1ad priority code point

Return type:  int

GetVlanVid(*[ixVlanTags](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetVlanVid "tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetVlanVid.ixVlanTags (Python parameter)")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetVlanVid "Link to this definition")  
Returns:  802.1a VLAN id

Return type:  int

GetVlanVidOuter(*[ixVlanTags](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetVlanVidOuter "tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetVlanVidOuter.ixVlanTags (Python parameter)")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.GetVlanVidOuter "Link to this definition")  
Returns:  802.1ad VLAN id

Return type:  int

SetEthDstMac(*[mac](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetEthDstMac.mac "tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetEthDstMac.mac (Python parameter) — target MAC address e.g.")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetEthDstMac "Link to this definition")  
Parameters:  mac : str[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetEthDstMac.mac "Permalink to this definition")  
target MAC address e.g. DE:AD:BE:EF:FF:00

SetEthPayload(*[payload](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetEthPayload.payload "tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetEthPayload.payload (Python parameter) — Ethernet payload")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetEthPayload "Link to this definition")  
Parameters:  payload : bytes[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetEthPayload.payload "Permalink to this definition")  
Ethernet payload

SetEthSrcMac(*[mac](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetEthSrcMac.mac "tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetEthSrcMac.mac (Python parameter) — source MAC addres e.g.")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetEthSrcMac "Link to this definition")  
Parameters:  mac : str[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetEthSrcMac.mac "Permalink to this definition")  
source MAC addres e.g. DE:AD:BE:EF:FF:00

SetEthType(*[ethType](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetEthType.ethType "tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetEthType.ethType (Python parameter) — ethernet protocol type")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetEthType "Link to this definition")  
Parameters:  ethType : int[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetEthType.ethType "Permalink to this definition")  
ethernet protocol type

SetPtpControl(*[control](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetPtpControl.control "tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetPtpControl.control (Python parameter) — PTP control field")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetPtpControl "Link to this definition")  
Parameters:  control : int[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetPtpControl.control "Permalink to this definition")  
PTP control field

SetPtpCorrectionField(*[correctionField](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetPtpCorrectionField.correctionField "tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetPtpCorrectionField.correctionField (Python parameter) — PTP correction field")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetPtpCorrectionField "Link to this definition")  
Parameters:  correctionField : int[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetPtpCorrectionField.correctionField "Permalink to this definition")  
PTP correction field

SetPtpDomainNumber(*[domainNumber](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetPtpDomainNumber.domainNumber "tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetPtpDomainNumber.domainNumber (Python parameter) — PTP domain number")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetPtpDomainNumber "Link to this definition")  
Parameters:  domainNumber : int[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetPtpDomainNumber.domainNumber "Permalink to this definition")  
PTP domain number

SetPtpFlags(*[flags](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetPtpFlags.flags "tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetPtpFlags.flags (Python parameter) — PTP flags")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetPtpFlags "Link to this definition")  
Parameters:  flags : int[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetPtpFlags.flags "Permalink to this definition")  
PTP flags

SetPtpLogMsgInterval(*[logMsgInterval](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetPtpLogMsgInterval.logMsgInterval "tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetPtpLogMsgInterval.logMsgInterval (Python parameter) — log message interval")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetPtpLogMsgInterval "Link to this definition")  
Parameters:  logMsgInterval : int[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetPtpLogMsgInterval.logMsgInterval "Permalink to this definition")  
log message interval

SetPtpMsgLen(*[msgLen](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetPtpMsgLen.msgLen "tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetPtpMsgLen.msgLen (Python parameter) — PTP message length")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetPtpMsgLen "Link to this definition")  
Parameters:  msgLen : int[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetPtpMsgLen.msgLen "Permalink to this definition")  
PTP message length

SetPtpMsgType(*[msgType](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetPtpMsgType.msgType "tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetPtpMsgType.msgType (Python parameter) — PTP message type")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetPtpMsgType "Link to this definition")  
Parameters:  msgType : int[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetPtpMsgType.msgType "Permalink to this definition")  
PTP message type

SetPtpSequenceId(*[sequenceId](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetPtpSequenceId.sequenceId "tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetPtpSequenceId.sequenceId (Python parameter) — PTP sequence ID")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetPtpSequenceId "Link to this definition")  
Parameters:  sequenceId : int[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetPtpSequenceId.sequenceId "Permalink to this definition")  
PTP sequence ID

SetPtpSourcePortIdentity(*[sourcePortIdentity](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetPtpSourcePortIdentity.sourcePortIdentity "tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetPtpSourcePortIdentity.sourcePortIdentity (Python parameter) — PTP source port identity")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetPtpSourcePortIdentity "Link to this definition")  
Parameters:  sourcePortIdentity : bytes[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetPtpSourcePortIdentity.sourcePortIdentity "Permalink to this definition")  
PTP source port identity

SetPtpVersion(*[version](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetPtpVersion.version "tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetPtpVersion.version (Python parameter) — PTP version")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetPtpVersion "Link to this definition")  
Parameters:  version : int[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetPtpVersion.version "Permalink to this definition")  
PTP version

SetTimestamp(*[timestamp](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetTimestamp.timestamp "tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetTimestamp.timestamp (Python parameter) — Receive timestamp in sec., None if not available")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetTimestamp "Link to this definition")  
Parameters:  timestamp : float | None[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetTimestamp.timestamp "Permalink to this definition")  
Receive timestamp in sec., None if not available

SetVlanCfi(*[cfi](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetVlanCfi.cfi "tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetVlanCfi.cfi (Python parameter) — 802.1a canonical format indicator")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetVlanCfi "Link to this definition")  
Parameters:  cfi : int[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetVlanCfi.cfi "Permalink to this definition")  
802.1a canonical format indicator

SetVlanCfiOuter(*[cfi](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetVlanCfiOuter.cfi "tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetVlanCfiOuter.cfi (Python parameter) — 802.1ad canonical format indicator")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetVlanCfiOuter "Link to this definition")  
Parameters:  cfi : int[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetVlanCfiOuter.cfi "Permalink to this definition")  
802.1ad canonical format indicator

SetVlanPcp(*[pcp](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetVlanPcp.pcp "tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetVlanPcp.pcp (Python parameter) — 802.1a priority code point")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetVlanPcp "Link to this definition")  
Parameters:  pcp : int[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetVlanPcp.pcp "Permalink to this definition")  
802.1a priority code point

SetVlanPcpOuter(*[pcp](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetVlanPcpOuter.pcp "tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetVlanPcpOuter.pcp (Python parameter) — 802.1ad priority code point")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetVlanPcpOuter "Link to this definition")  
Parameters:  pcp : int[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetVlanPcpOuter.pcp "Permalink to this definition")  
802.1ad priority code point

SetVlanVid(*[vid](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetVlanVid.vid "tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetVlanVid.vid (Python parameter) — 802.1a VLAN id")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetVlanVid "Link to this definition")  
Parameters:  vid : int[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetVlanVid.vid "Permalink to this definition")  
802.1a VLAN id

SetVlanVidOuter(*[vid](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetVlanVidOuter.vid "tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetVlanVidOuter.vid (Python parameter) — 802.1ad VLAN id")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetVlanVidOuter "Link to this definition")  
Parameters:  vid : int[¶](#tts.lib.ethernet.PacketPtp.PacketPtpFollowUp.SetVlanVidOuter.vid "Permalink to this definition")  
802.1ad VLAN id

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

Return type:  [EthernetProtocolBase](busdatastructuresTraceanalysis.md#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase (Python class) — Base class for all protocol classes.") | None

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
Equivalent to method [`FindParent(protocol)`](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.FindParent "tts.lib.ethernet.PacketPtp.PacketPdelayReq.FindParent (Python method) — Only for pseudo signals in trace analysis! Returns the requested protocol object if present, otherwise a NoProtocol object."). Direct access to parent protocols. *protocol* is one of [`OsiProtocol`](busdatastructuresTraceanalysis.md#tts.lib.ethernet.PacketEthernet.OsiProtocol "tts.lib.ethernet.PacketEthernet.OsiProtocol (Python class) — String Enumeration class representing the supported protocol layers.").

Example: Signal.eth.src provides the source MAC address of the Ethernet protocol layer.

Type:  [`EthernetProtocolBase`](busdatastructuresTraceanalysis.md#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase (Python class) — Base class for all protocol classes.")

FindParent(*[protocol](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.FindParent.protocol "tts.lib.ethernet.PacketPtp.PacketPdelayReq.FindParent.protocol (Python parameter) — The required protocol name.")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.FindParent "Link to this definition")  
*Only for pseudo signals in trace analysis!* Returns the requested protocol object if present, otherwise a [`NoProtocol`](busdatastructuresTraceanalysis.md#tts.lib.ethernet.PacketEthernet.NoProtocol "tts.lib.ethernet.PacketEthernet.NoProtocol (Python class) — Represents a non-present protocol. Accessing any other parent of a non-present protocol will also yield a NoProtocol object. Accessing any protocol specific attributes will lead to an AttributeError since the specific protocol is not available. The boolean value of a NoProtocol object is always False, such that it can be used to check for the precense/absence of a protocol layer.") object.

Parameters:  protocol : [OsiProtocol](busdatastructuresTraceanalysis.md#tts.lib.ethernet.PacketEthernet.OsiProtocol "tts.lib.ethernet.PacketEthernet.OsiProtocol (Python class) — String Enumeration class representing the supported protocol layers.")[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.FindParent.protocol "Permalink to this definition")  
The required protocol name.

Returns:  The required parent protocol object.

Return type:  [EthernetProtocolBase](busdatastructuresTraceanalysis.md#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase (Python class) — Base class for all protocol classes.")

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

GetVlanCfi(*[ixVlanTags](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetVlanCfi "tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetVlanCfi.ixVlanTags (Python parameter)")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetVlanCfi "Link to this definition")  
Returns:  802.1a canonical format indicator

Return type:  int

GetVlanCfiOuter(*[ixVlanTags](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetVlanCfiOuter "tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetVlanCfiOuter.ixVlanTags (Python parameter)")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetVlanCfiOuter "Link to this definition")  
Returns:  802.1ad canonical format indicator

Return type:  int

GetVlanPcp(*[ixVlanTags](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetVlanPcp "tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetVlanPcp.ixVlanTags (Python parameter)")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetVlanPcp "Link to this definition")  
Returns:  802.1a priority code point

Return type:  int

GetVlanPcpOuter(*[ixVlanTags](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetVlanPcpOuter "tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetVlanPcpOuter.ixVlanTags (Python parameter)")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetVlanPcpOuter "Link to this definition")  
Returns:  802.1ad priority code point

Return type:  int

GetVlanVid(*[ixVlanTags](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetVlanVid "tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetVlanVid.ixVlanTags (Python parameter)")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetVlanVid "Link to this definition")  
Returns:  802.1a VLAN id

Return type:  int

GetVlanVidOuter(*[ixVlanTags](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetVlanVidOuter "tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetVlanVidOuter.ixVlanTags (Python parameter)")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.GetVlanVidOuter "Link to this definition")  
Returns:  802.1ad VLAN id

Return type:  int

SetEthDstMac(*[mac](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetEthDstMac.mac "tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetEthDstMac.mac (Python parameter) — target MAC address e.g.")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetEthDstMac "Link to this definition")  
Parameters:  mac : str[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetEthDstMac.mac "Permalink to this definition")  
target MAC address e.g. DE:AD:BE:EF:FF:00

SetEthPayload(*[payload](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetEthPayload.payload "tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetEthPayload.payload (Python parameter) — Ethernet payload")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetEthPayload "Link to this definition")  
Parameters:  payload : bytes[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetEthPayload.payload "Permalink to this definition")  
Ethernet payload

SetEthSrcMac(*[mac](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetEthSrcMac.mac "tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetEthSrcMac.mac (Python parameter) — source MAC addres e.g.")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetEthSrcMac "Link to this definition")  
Parameters:  mac : str[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetEthSrcMac.mac "Permalink to this definition")  
source MAC addres e.g. DE:AD:BE:EF:FF:00

SetEthType(*[ethType](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetEthType.ethType "tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetEthType.ethType (Python parameter) — ethernet protocol type")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetEthType "Link to this definition")  
Parameters:  ethType : int[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetEthType.ethType "Permalink to this definition")  
ethernet protocol type

SetPtpControl(*[control](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetPtpControl.control "tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetPtpControl.control (Python parameter) — PTP control field")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetPtpControl "Link to this definition")  
Parameters:  control : int[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetPtpControl.control "Permalink to this definition")  
PTP control field

SetPtpCorrectionField(*[correctionField](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetPtpCorrectionField.correctionField "tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetPtpCorrectionField.correctionField (Python parameter) — PTP correction field")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetPtpCorrectionField "Link to this definition")  
Parameters:  correctionField : int[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetPtpCorrectionField.correctionField "Permalink to this definition")  
PTP correction field

SetPtpDomainNumber(*[domainNumber](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetPtpDomainNumber.domainNumber "tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetPtpDomainNumber.domainNumber (Python parameter) — PTP domain number")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetPtpDomainNumber "Link to this definition")  
Parameters:  domainNumber : int[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetPtpDomainNumber.domainNumber "Permalink to this definition")  
PTP domain number

SetPtpFlags(*[flags](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetPtpFlags.flags "tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetPtpFlags.flags (Python parameter) — PTP flags")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetPtpFlags "Link to this definition")  
Parameters:  flags : int[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetPtpFlags.flags "Permalink to this definition")  
PTP flags

SetPtpLogMsgInterval(*[logMsgInterval](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetPtpLogMsgInterval.logMsgInterval "tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetPtpLogMsgInterval.logMsgInterval (Python parameter) — log message interval")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetPtpLogMsgInterval "Link to this definition")  
Parameters:  logMsgInterval : int[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetPtpLogMsgInterval.logMsgInterval "Permalink to this definition")  
log message interval

SetPtpMsgLen(*[msgLen](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetPtpMsgLen.msgLen "tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetPtpMsgLen.msgLen (Python parameter) — PTP message length")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetPtpMsgLen "Link to this definition")  
Parameters:  msgLen : int[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetPtpMsgLen.msgLen "Permalink to this definition")  
PTP message length

SetPtpMsgType(*[msgType](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetPtpMsgType.msgType "tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetPtpMsgType.msgType (Python parameter) — PTP message type")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetPtpMsgType "Link to this definition")  
Parameters:  msgType : int[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetPtpMsgType.msgType "Permalink to this definition")  
PTP message type

SetPtpSequenceId(*[sequenceId](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetPtpSequenceId.sequenceId "tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetPtpSequenceId.sequenceId (Python parameter) — PTP sequence ID")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetPtpSequenceId "Link to this definition")  
Parameters:  sequenceId : int[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetPtpSequenceId.sequenceId "Permalink to this definition")  
PTP sequence ID

SetPtpSourcePortIdentity(*[sourcePortIdentity](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetPtpSourcePortIdentity.sourcePortIdentity "tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetPtpSourcePortIdentity.sourcePortIdentity (Python parameter) — PTP source port identity")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetPtpSourcePortIdentity "Link to this definition")  
Parameters:  sourcePortIdentity : bytes[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetPtpSourcePortIdentity.sourcePortIdentity "Permalink to this definition")  
PTP source port identity

SetPtpVersion(*[version](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetPtpVersion.version "tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetPtpVersion.version (Python parameter) — PTP version")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetPtpVersion "Link to this definition")  
Parameters:  version : int[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetPtpVersion.version "Permalink to this definition")  
PTP version

SetTimestamp(*[timestamp](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetTimestamp.timestamp "tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetTimestamp.timestamp (Python parameter) — Receive timestamp in sec., None if not available")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetTimestamp "Link to this definition")  
Parameters:  timestamp : float | None[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetTimestamp.timestamp "Permalink to this definition")  
Receive timestamp in sec., None if not available

SetVlanCfi(*[cfi](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetVlanCfi.cfi "tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetVlanCfi.cfi (Python parameter) — 802.1a canonical format indicator")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetVlanCfi "Link to this definition")  
Parameters:  cfi : int[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetVlanCfi.cfi "Permalink to this definition")  
802.1a canonical format indicator

SetVlanCfiOuter(*[cfi](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetVlanCfiOuter.cfi "tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetVlanCfiOuter.cfi (Python parameter) — 802.1ad canonical format indicator")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetVlanCfiOuter "Link to this definition")  
Parameters:  cfi : int[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetVlanCfiOuter.cfi "Permalink to this definition")  
802.1ad canonical format indicator

SetVlanPcp(*[pcp](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetVlanPcp.pcp "tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetVlanPcp.pcp (Python parameter) — 802.1a priority code point")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetVlanPcp "Link to this definition")  
Parameters:  pcp : int[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetVlanPcp.pcp "Permalink to this definition")  
802.1a priority code point

SetVlanPcpOuter(*[pcp](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetVlanPcpOuter.pcp "tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetVlanPcpOuter.pcp (Python parameter) — 802.1ad priority code point")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetVlanPcpOuter "Link to this definition")  
Parameters:  pcp : int[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetVlanPcpOuter.pcp "Permalink to this definition")  
802.1ad priority code point

SetVlanVid(*[vid](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetVlanVid.vid "tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetVlanVid.vid (Python parameter) — 802.1a VLAN id")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetVlanVid "Link to this definition")  
Parameters:  vid : int[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetVlanVid.vid "Permalink to this definition")  
802.1a VLAN id

SetVlanVidOuter(*[vid](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetVlanVidOuter.vid "tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetVlanVidOuter.vid (Python parameter) — 802.1ad VLAN id")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetVlanVidOuter "Link to this definition")  
Parameters:  vid : int[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayReq.SetVlanVidOuter.vid "Permalink to this definition")  
802.1ad VLAN id

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

Return type:  [EthernetProtocolBase](busdatastructuresTraceanalysis.md#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase (Python class) — Base class for all protocol classes.") | None

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
Equivalent to method [`FindParent(protocol)`](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.FindParent "tts.lib.ethernet.PacketPtp.PacketPdelayResp.FindParent (Python method) — Only for pseudo signals in trace analysis! Returns the requested protocol object if present, otherwise a NoProtocol object."). Direct access to parent protocols. *protocol* is one of [`OsiProtocol`](busdatastructuresTraceanalysis.md#tts.lib.ethernet.PacketEthernet.OsiProtocol "tts.lib.ethernet.PacketEthernet.OsiProtocol (Python class) — String Enumeration class representing the supported protocol layers.").

Example: Signal.eth.src provides the source MAC address of the Ethernet protocol layer.

Type:  [`EthernetProtocolBase`](busdatastructuresTraceanalysis.md#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase (Python class) — Base class for all protocol classes.")

GetPtpRequestReceiptTimestampSec()[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetPtpRequestReceiptTimestampSec "Link to this definition")  
Returns:  second portion of the PTP request receipt timestamp

Return type:  int

SetPtpRequestReceiptTimestampSec(*[requestReceiptTimestampSec](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetPtpRequestReceiptTimestampSec.requestReceiptTimestampSec "tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetPtpRequestReceiptTimestampSec.requestReceiptTimestampSec (Python parameter) — second portion of the PTP request receipt timestamp")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetPtpRequestReceiptTimestampSec "Link to this definition")  
Parameters:  requestReceiptTimestampSec : int[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetPtpRequestReceiptTimestampSec.requestReceiptTimestampSec "Permalink to this definition")  
second portion of the PTP request receipt timestamp

ptpRequestReceiptTimestampSec[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.ptpRequestReceiptTimestampSec "Link to this definition")  
second portion of the PTP request receipt timestamp

Type:  int

GetPtpRequestReceiptTimestampNSec()[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetPtpRequestReceiptTimestampNSec "Link to this definition")  
Returns:  nanosecond portion of the PTP precise origin timestamp

Return type:  int

SetPtpRequestReceiptTimestampNSec(*[requestReceiptTimestampNSec](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetPtpRequestReceiptTimestampNSec.requestReceiptTimestampNSec "tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetPtpRequestReceiptTimestampNSec.requestReceiptTimestampNSec (Python parameter) — nanosecond portion of the PTP precise origin timestamp")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetPtpRequestReceiptTimestampNSec "Link to this definition")  
Parameters:  requestReceiptTimestampNSec : int[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetPtpRequestReceiptTimestampNSec.requestReceiptTimestampNSec "Permalink to this definition")  
nanosecond portion of the PTP precise origin timestamp

ptpRequestReceiptTimestampNSec[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.ptpRequestReceiptTimestampNSec "Link to this definition")  
nanosecond portion of the PTP precise origin timestamp

Type:  int

GetPtpRequestingPortIdentity()[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetPtpRequestingPortIdentity "Link to this definition")  
Returns:  PTP requesting port identity

Return type:  bytes

SetPtpRequestingPortIdentity(*[requestingPortIdentity](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetPtpRequestingPortIdentity.requestingPortIdentity "tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetPtpRequestingPortIdentity.requestingPortIdentity (Python parameter) — PTP requesting port identity")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetPtpRequestingPortIdentity "Link to this definition")  
Parameters:  requestingPortIdentity : bytes[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetPtpRequestingPortIdentity.requestingPortIdentity "Permalink to this definition")  
PTP requesting port identity

ptpRequestingPortIdentity[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.ptpRequestingPortIdentity "Link to this definition")  
PTP requesting port identity

Type:  bytes

FindParent(*[protocol](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.FindParent.protocol "tts.lib.ethernet.PacketPtp.PacketPdelayResp.FindParent.protocol (Python parameter) — The required protocol name.")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.FindParent "Link to this definition")  
*Only for pseudo signals in trace analysis!* Returns the requested protocol object if present, otherwise a [`NoProtocol`](busdatastructuresTraceanalysis.md#tts.lib.ethernet.PacketEthernet.NoProtocol "tts.lib.ethernet.PacketEthernet.NoProtocol (Python class) — Represents a non-present protocol. Accessing any other parent of a non-present protocol will also yield a NoProtocol object. Accessing any protocol specific attributes will lead to an AttributeError since the specific protocol is not available. The boolean value of a NoProtocol object is always False, such that it can be used to check for the precense/absence of a protocol layer.") object.

Parameters:  protocol : [OsiProtocol](busdatastructuresTraceanalysis.md#tts.lib.ethernet.PacketEthernet.OsiProtocol "tts.lib.ethernet.PacketEthernet.OsiProtocol (Python class) — String Enumeration class representing the supported protocol layers.")[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.FindParent.protocol "Permalink to this definition")  
The required protocol name.

Returns:  The required parent protocol object.

Return type:  [EthernetProtocolBase](busdatastructuresTraceanalysis.md#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase (Python class) — Base class for all protocol classes.")

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

GetVlanCfi(*[ixVlanTags](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetVlanCfi "tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetVlanCfi.ixVlanTags (Python parameter)")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetVlanCfi "Link to this definition")  
Returns:  802.1a canonical format indicator

Return type:  int

GetVlanCfiOuter(*[ixVlanTags](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetVlanCfiOuter "tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetVlanCfiOuter.ixVlanTags (Python parameter)")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetVlanCfiOuter "Link to this definition")  
Returns:  802.1ad canonical format indicator

Return type:  int

GetVlanPcp(*[ixVlanTags](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetVlanPcp "tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetVlanPcp.ixVlanTags (Python parameter)")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetVlanPcp "Link to this definition")  
Returns:  802.1a priority code point

Return type:  int

GetVlanPcpOuter(*[ixVlanTags](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetVlanPcpOuter "tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetVlanPcpOuter.ixVlanTags (Python parameter)")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetVlanPcpOuter "Link to this definition")  
Returns:  802.1ad priority code point

Return type:  int

GetVlanVid(*[ixVlanTags](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetVlanVid "tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetVlanVid.ixVlanTags (Python parameter)")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetVlanVid "Link to this definition")  
Returns:  802.1a VLAN id

Return type:  int

GetVlanVidOuter(*[ixVlanTags](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetVlanVidOuter "tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetVlanVidOuter.ixVlanTags (Python parameter)")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.GetVlanVidOuter "Link to this definition")  
Returns:  802.1ad VLAN id

Return type:  int

SetEthDstMac(*[mac](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetEthDstMac.mac "tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetEthDstMac.mac (Python parameter) — target MAC address e.g.")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetEthDstMac "Link to this definition")  
Parameters:  mac : str[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetEthDstMac.mac "Permalink to this definition")  
target MAC address e.g. DE:AD:BE:EF:FF:00

SetEthPayload(*[payload](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetEthPayload.payload "tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetEthPayload.payload (Python parameter) — Ethernet payload")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetEthPayload "Link to this definition")  
Parameters:  payload : bytes[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetEthPayload.payload "Permalink to this definition")  
Ethernet payload

SetEthSrcMac(*[mac](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetEthSrcMac.mac "tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetEthSrcMac.mac (Python parameter) — source MAC addres e.g.")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetEthSrcMac "Link to this definition")  
Parameters:  mac : str[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetEthSrcMac.mac "Permalink to this definition")  
source MAC addres e.g. DE:AD:BE:EF:FF:00

SetEthType(*[ethType](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetEthType.ethType "tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetEthType.ethType (Python parameter) — ethernet protocol type")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetEthType "Link to this definition")  
Parameters:  ethType : int[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetEthType.ethType "Permalink to this definition")  
ethernet protocol type

SetPtpControl(*[control](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetPtpControl.control "tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetPtpControl.control (Python parameter) — PTP control field")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetPtpControl "Link to this definition")  
Parameters:  control : int[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetPtpControl.control "Permalink to this definition")  
PTP control field

SetPtpCorrectionField(*[correctionField](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetPtpCorrectionField.correctionField "tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetPtpCorrectionField.correctionField (Python parameter) — PTP correction field")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetPtpCorrectionField "Link to this definition")  
Parameters:  correctionField : int[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetPtpCorrectionField.correctionField "Permalink to this definition")  
PTP correction field

SetPtpDomainNumber(*[domainNumber](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetPtpDomainNumber.domainNumber "tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetPtpDomainNumber.domainNumber (Python parameter) — PTP domain number")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetPtpDomainNumber "Link to this definition")  
Parameters:  domainNumber : int[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetPtpDomainNumber.domainNumber "Permalink to this definition")  
PTP domain number

SetPtpFlags(*[flags](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetPtpFlags.flags "tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetPtpFlags.flags (Python parameter) — PTP flags")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetPtpFlags "Link to this definition")  
Parameters:  flags : int[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetPtpFlags.flags "Permalink to this definition")  
PTP flags

SetPtpLogMsgInterval(*[logMsgInterval](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetPtpLogMsgInterval.logMsgInterval "tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetPtpLogMsgInterval.logMsgInterval (Python parameter) — log message interval")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetPtpLogMsgInterval "Link to this definition")  
Parameters:  logMsgInterval : int[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetPtpLogMsgInterval.logMsgInterval "Permalink to this definition")  
log message interval

SetPtpMsgLen(*[msgLen](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetPtpMsgLen.msgLen "tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetPtpMsgLen.msgLen (Python parameter) — PTP message length")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetPtpMsgLen "Link to this definition")  
Parameters:  msgLen : int[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetPtpMsgLen.msgLen "Permalink to this definition")  
PTP message length

SetPtpMsgType(*[msgType](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetPtpMsgType.msgType "tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetPtpMsgType.msgType (Python parameter) — PTP message type")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetPtpMsgType "Link to this definition")  
Parameters:  msgType : int[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetPtpMsgType.msgType "Permalink to this definition")  
PTP message type

SetPtpSequenceId(*[sequenceId](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetPtpSequenceId.sequenceId "tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetPtpSequenceId.sequenceId (Python parameter) — PTP sequence ID")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetPtpSequenceId "Link to this definition")  
Parameters:  sequenceId : int[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetPtpSequenceId.sequenceId "Permalink to this definition")  
PTP sequence ID

SetPtpSourcePortIdentity(*[sourcePortIdentity](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetPtpSourcePortIdentity.sourcePortIdentity "tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetPtpSourcePortIdentity.sourcePortIdentity (Python parameter) — PTP source port identity")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetPtpSourcePortIdentity "Link to this definition")  
Parameters:  sourcePortIdentity : bytes[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetPtpSourcePortIdentity.sourcePortIdentity "Permalink to this definition")  
PTP source port identity

SetPtpVersion(*[version](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetPtpVersion.version "tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetPtpVersion.version (Python parameter) — PTP version")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetPtpVersion "Link to this definition")  
Parameters:  version : int[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetPtpVersion.version "Permalink to this definition")  
PTP version

SetTimestamp(*[timestamp](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetTimestamp.timestamp "tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetTimestamp.timestamp (Python parameter) — Receive timestamp in sec., None if not available")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetTimestamp "Link to this definition")  
Parameters:  timestamp : float | None[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetTimestamp.timestamp "Permalink to this definition")  
Receive timestamp in sec., None if not available

SetVlanCfi(*[cfi](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetVlanCfi.cfi "tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetVlanCfi.cfi (Python parameter) — 802.1a canonical format indicator")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetVlanCfi "Link to this definition")  
Parameters:  cfi : int[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetVlanCfi.cfi "Permalink to this definition")  
802.1a canonical format indicator

SetVlanCfiOuter(*[cfi](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetVlanCfiOuter.cfi "tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetVlanCfiOuter.cfi (Python parameter) — 802.1ad canonical format indicator")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetVlanCfiOuter "Link to this definition")  
Parameters:  cfi : int[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetVlanCfiOuter.cfi "Permalink to this definition")  
802.1ad canonical format indicator

SetVlanPcp(*[pcp](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetVlanPcp.pcp "tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetVlanPcp.pcp (Python parameter) — 802.1a priority code point")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetVlanPcp "Link to this definition")  
Parameters:  pcp : int[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetVlanPcp.pcp "Permalink to this definition")  
802.1a priority code point

SetVlanPcpOuter(*[pcp](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetVlanPcpOuter.pcp "tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetVlanPcpOuter.pcp (Python parameter) — 802.1ad priority code point")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetVlanPcpOuter "Link to this definition")  
Parameters:  pcp : int[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetVlanPcpOuter.pcp "Permalink to this definition")  
802.1ad priority code point

SetVlanVid(*[vid](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetVlanVid.vid "tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetVlanVid.vid (Python parameter) — 802.1a VLAN id")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetVlanVid "Link to this definition")  
Parameters:  vid : int[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetVlanVid.vid "Permalink to this definition")  
802.1a VLAN id

SetVlanVidOuter(*[vid](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetVlanVidOuter.vid "tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetVlanVidOuter.vid (Python parameter) — 802.1ad VLAN id")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetVlanVidOuter "Link to this definition")  
Parameters:  vid : int[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayResp.SetVlanVidOuter.vid "Permalink to this definition")  
802.1ad VLAN id

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

Return type:  [EthernetProtocolBase](busdatastructuresTraceanalysis.md#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase (Python class) — Base class for all protocol classes.") | None

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
Equivalent to method [`FindParent(protocol)`](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.FindParent "tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.FindParent (Python method) — Only for pseudo signals in trace analysis! Returns the requested protocol object if present, otherwise a NoProtocol object."). Direct access to parent protocols. *protocol* is one of [`OsiProtocol`](busdatastructuresTraceanalysis.md#tts.lib.ethernet.PacketEthernet.OsiProtocol "tts.lib.ethernet.PacketEthernet.OsiProtocol (Python class) — String Enumeration class representing the supported protocol layers.").

Example: Signal.eth.src provides the source MAC address of the Ethernet protocol layer.

Type:  [`EthernetProtocolBase`](busdatastructuresTraceanalysis.md#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase (Python class) — Base class for all protocol classes.")

GetPtpResponseOriginTimestampSec()[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetPtpResponseOriginTimestampSec "Link to this definition")  
Returns:  second portion of the PTP response origin timestamp

Return type:  int

SetPtpResponseOriginTimestampSec(*[responseOriginTimestampSec](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetPtpResponseOriginTimestampSec.responseOriginTimestampSec "tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetPtpResponseOriginTimestampSec.responseOriginTimestampSec (Python parameter) — second portion of the PTP response origin timestamp")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetPtpResponseOriginTimestampSec "Link to this definition")  
Parameters:  responseOriginTimestampSec : int[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetPtpResponseOriginTimestampSec.responseOriginTimestampSec "Permalink to this definition")  
second portion of the PTP response origin timestamp

ptpResponseOriginTimestampSec[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.ptpResponseOriginTimestampSec "Link to this definition")  
second portion of the PTP response origin timestamp

Type:  int

GetPtpResponseOriginTimestampNSec()[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetPtpResponseOriginTimestampNSec "Link to this definition")  
Returns:  nanosecond portion of the PTP response origin timestamp

Return type:  int

SetPtpResponseOriginTimestampNSec(*[responseOriginTimestampNSec](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetPtpResponseOriginTimestampNSec.responseOriginTimestampNSec "tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetPtpResponseOriginTimestampNSec.responseOriginTimestampNSec (Python parameter) — nanosecond portion of the PTP response origin timestamp")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetPtpResponseOriginTimestampNSec "Link to this definition")  
Parameters:  responseOriginTimestampNSec : int[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetPtpResponseOriginTimestampNSec.responseOriginTimestampNSec "Permalink to this definition")  
nanosecond portion of the PTP response origin timestamp

ptpResponseOriginTimestampNSec[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.ptpResponseOriginTimestampNSec "Link to this definition")  
nanosecond portion of the PTP response origin timestamp

Type:  int

GetPtpRequestingPortIdentity()[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetPtpRequestingPortIdentity "Link to this definition")  
Returns:  PTP requesting port identity

Return type:  bytes

SetPtpRequestingPortIdentity(*[requestingPortIdentity](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetPtpRequestingPortIdentity.requestingPortIdentity "tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetPtpRequestingPortIdentity.requestingPortIdentity (Python parameter) — PTP requesting port identity")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetPtpRequestingPortIdentity "Link to this definition")  
Parameters:  requestingPortIdentity : bytes[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetPtpRequestingPortIdentity.requestingPortIdentity "Permalink to this definition")  
PTP requesting port identity

ptpRequestingPortIdentity[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.ptpRequestingPortIdentity "Link to this definition")  
PTP requesting port identity

Type:  bytes

FindParent(*[protocol](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.FindParent.protocol "tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.FindParent.protocol (Python parameter) — The required protocol name.")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.FindParent "Link to this definition")  
*Only for pseudo signals in trace analysis!* Returns the requested protocol object if present, otherwise a [`NoProtocol`](busdatastructuresTraceanalysis.md#tts.lib.ethernet.PacketEthernet.NoProtocol "tts.lib.ethernet.PacketEthernet.NoProtocol (Python class) — Represents a non-present protocol. Accessing any other parent of a non-present protocol will also yield a NoProtocol object. Accessing any protocol specific attributes will lead to an AttributeError since the specific protocol is not available. The boolean value of a NoProtocol object is always False, such that it can be used to check for the precense/absence of a protocol layer.") object.

Parameters:  protocol : [OsiProtocol](busdatastructuresTraceanalysis.md#tts.lib.ethernet.PacketEthernet.OsiProtocol "tts.lib.ethernet.PacketEthernet.OsiProtocol (Python class) — String Enumeration class representing the supported protocol layers.")[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.FindParent.protocol "Permalink to this definition")  
The required protocol name.

Returns:  The required parent protocol object.

Return type:  [EthernetProtocolBase](busdatastructuresTraceanalysis.md#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase (Python class) — Base class for all protocol classes.")

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

GetVlanCfi(*[ixVlanTags](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetVlanCfi "tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetVlanCfi.ixVlanTags (Python parameter)")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetVlanCfi "Link to this definition")  
Returns:  802.1a canonical format indicator

Return type:  int

GetVlanCfiOuter(*[ixVlanTags](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetVlanCfiOuter "tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetVlanCfiOuter.ixVlanTags (Python parameter)")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetVlanCfiOuter "Link to this definition")  
Returns:  802.1ad canonical format indicator

Return type:  int

GetVlanPcp(*[ixVlanTags](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetVlanPcp "tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetVlanPcp.ixVlanTags (Python parameter)")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetVlanPcp "Link to this definition")  
Returns:  802.1a priority code point

Return type:  int

GetVlanPcpOuter(*[ixVlanTags](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetVlanPcpOuter "tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetVlanPcpOuter.ixVlanTags (Python parameter)")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetVlanPcpOuter "Link to this definition")  
Returns:  802.1ad priority code point

Return type:  int

GetVlanVid(*[ixVlanTags](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetVlanVid "tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetVlanVid.ixVlanTags (Python parameter)")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetVlanVid "Link to this definition")  
Returns:  802.1a VLAN id

Return type:  int

GetVlanVidOuter(*[ixVlanTags](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetVlanVidOuter "tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetVlanVidOuter.ixVlanTags (Python parameter)")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.GetVlanVidOuter "Link to this definition")  
Returns:  802.1ad VLAN id

Return type:  int

SetEthDstMac(*[mac](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetEthDstMac.mac "tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetEthDstMac.mac (Python parameter) — target MAC address e.g.")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetEthDstMac "Link to this definition")  
Parameters:  mac : str[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetEthDstMac.mac "Permalink to this definition")  
target MAC address e.g. DE:AD:BE:EF:FF:00

SetEthPayload(*[payload](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetEthPayload.payload "tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetEthPayload.payload (Python parameter) — Ethernet payload")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetEthPayload "Link to this definition")  
Parameters:  payload : bytes[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetEthPayload.payload "Permalink to this definition")  
Ethernet payload

SetEthSrcMac(*[mac](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetEthSrcMac.mac "tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetEthSrcMac.mac (Python parameter) — source MAC addres e.g.")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetEthSrcMac "Link to this definition")  
Parameters:  mac : str[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetEthSrcMac.mac "Permalink to this definition")  
source MAC addres e.g. DE:AD:BE:EF:FF:00

SetEthType(*[ethType](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetEthType.ethType "tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetEthType.ethType (Python parameter) — ethernet protocol type")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetEthType "Link to this definition")  
Parameters:  ethType : int[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetEthType.ethType "Permalink to this definition")  
ethernet protocol type

SetPtpControl(*[control](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetPtpControl.control "tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetPtpControl.control (Python parameter) — PTP control field")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetPtpControl "Link to this definition")  
Parameters:  control : int[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetPtpControl.control "Permalink to this definition")  
PTP control field

SetPtpCorrectionField(*[correctionField](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetPtpCorrectionField.correctionField "tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetPtpCorrectionField.correctionField (Python parameter) — PTP correction field")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetPtpCorrectionField "Link to this definition")  
Parameters:  correctionField : int[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetPtpCorrectionField.correctionField "Permalink to this definition")  
PTP correction field

SetPtpDomainNumber(*[domainNumber](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetPtpDomainNumber.domainNumber "tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetPtpDomainNumber.domainNumber (Python parameter) — PTP domain number")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetPtpDomainNumber "Link to this definition")  
Parameters:  domainNumber : int[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetPtpDomainNumber.domainNumber "Permalink to this definition")  
PTP domain number

SetPtpFlags(*[flags](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetPtpFlags.flags "tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetPtpFlags.flags (Python parameter) — PTP flags")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetPtpFlags "Link to this definition")  
Parameters:  flags : int[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetPtpFlags.flags "Permalink to this definition")  
PTP flags

SetPtpLogMsgInterval(*[logMsgInterval](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetPtpLogMsgInterval.logMsgInterval "tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetPtpLogMsgInterval.logMsgInterval (Python parameter) — log message interval")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetPtpLogMsgInterval "Link to this definition")  
Parameters:  logMsgInterval : int[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetPtpLogMsgInterval.logMsgInterval "Permalink to this definition")  
log message interval

SetPtpMsgLen(*[msgLen](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetPtpMsgLen.msgLen "tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetPtpMsgLen.msgLen (Python parameter) — PTP message length")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetPtpMsgLen "Link to this definition")  
Parameters:  msgLen : int[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetPtpMsgLen.msgLen "Permalink to this definition")  
PTP message length

SetPtpMsgType(*[msgType](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetPtpMsgType.msgType "tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetPtpMsgType.msgType (Python parameter) — PTP message type")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetPtpMsgType "Link to this definition")  
Parameters:  msgType : int[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetPtpMsgType.msgType "Permalink to this definition")  
PTP message type

SetPtpSequenceId(*[sequenceId](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetPtpSequenceId.sequenceId "tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetPtpSequenceId.sequenceId (Python parameter) — PTP sequence ID")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetPtpSequenceId "Link to this definition")  
Parameters:  sequenceId : int[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetPtpSequenceId.sequenceId "Permalink to this definition")  
PTP sequence ID

SetPtpSourcePortIdentity(*[sourcePortIdentity](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetPtpSourcePortIdentity.sourcePortIdentity "tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetPtpSourcePortIdentity.sourcePortIdentity (Python parameter) — PTP source port identity")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetPtpSourcePortIdentity "Link to this definition")  
Parameters:  sourcePortIdentity : bytes[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetPtpSourcePortIdentity.sourcePortIdentity "Permalink to this definition")  
PTP source port identity

SetPtpVersion(*[version](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetPtpVersion.version "tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetPtpVersion.version (Python parameter) — PTP version")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetPtpVersion "Link to this definition")  
Parameters:  version : int[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetPtpVersion.version "Permalink to this definition")  
PTP version

SetTimestamp(*[timestamp](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetTimestamp.timestamp "tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetTimestamp.timestamp (Python parameter) — Receive timestamp in sec., None if not available")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetTimestamp "Link to this definition")  
Parameters:  timestamp : float | None[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetTimestamp.timestamp "Permalink to this definition")  
Receive timestamp in sec., None if not available

SetVlanCfi(*[cfi](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetVlanCfi.cfi "tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetVlanCfi.cfi (Python parameter) — 802.1a canonical format indicator")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetVlanCfi "Link to this definition")  
Parameters:  cfi : int[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetVlanCfi.cfi "Permalink to this definition")  
802.1a canonical format indicator

SetVlanCfiOuter(*[cfi](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetVlanCfiOuter.cfi "tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetVlanCfiOuter.cfi (Python parameter) — 802.1ad canonical format indicator")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetVlanCfiOuter "Link to this definition")  
Parameters:  cfi : int[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetVlanCfiOuter.cfi "Permalink to this definition")  
802.1ad canonical format indicator

SetVlanPcp(*[pcp](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetVlanPcp.pcp "tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetVlanPcp.pcp (Python parameter) — 802.1a priority code point")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetVlanPcp "Link to this definition")  
Parameters:  pcp : int[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetVlanPcp.pcp "Permalink to this definition")  
802.1a priority code point

SetVlanPcpOuter(*[pcp](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetVlanPcpOuter.pcp "tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetVlanPcpOuter.pcp (Python parameter) — 802.1ad priority code point")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetVlanPcpOuter "Link to this definition")  
Parameters:  pcp : int[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetVlanPcpOuter.pcp "Permalink to this definition")  
802.1ad priority code point

SetVlanVid(*[vid](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetVlanVid.vid "tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetVlanVid.vid (Python parameter) — 802.1a VLAN id")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetVlanVid "Link to this definition")  
Parameters:  vid : int[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetVlanVid.vid "Permalink to this definition")  
802.1a VLAN id

SetVlanVidOuter(*[vid](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetVlanVidOuter.vid "tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetVlanVidOuter.vid (Python parameter) — 802.1ad VLAN id")*)[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetVlanVidOuter "Link to this definition")  
Parameters:  vid : int[¶](#tts.lib.ethernet.PacketPtp.PacketPdelayRespFollowUp.SetVlanVidOuter.vid "Permalink to this definition")  
802.1ad VLAN id

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

Return type:  [EthernetProtocolBase](busdatastructuresTraceanalysis.md#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase (Python class) — Base class for all protocol classes.") | None

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

Info

If your code uses getters and/or setter methods, you should probably convert it to use the properties as documented below, but for the time being it will continue to work.

#### PacketSomeIp[¶](#packetsomeip "Link to this heading")

*class* PacketSomeIp[¶](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp "Link to this definition")  
In the test case, use `api.Ethernet.PacketSomeIp`; in UserPyModules, use `from tts.lib.ethernet.PacketSomeIp import PacketSomeIp`.

SOMEIP_MSG_REQUEST = `0`[¶](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.SOMEIP_MSG_REQUEST "Link to this definition")  

SOMEIP_MSG_REQUEST_NO_RETURN = `1`[¶](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.SOMEIP_MSG_REQUEST_NO_RETURN "Link to this definition")  

SOMEIP_MSG_NOTIFICATION = `2`[¶](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.SOMEIP_MSG_NOTIFICATION "Link to this definition")  

SOMEIP_MSG_TP = `32`[¶](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.SOMEIP_MSG_TP "Link to this definition")  

SOMEIP_MSG_RESPONSE = `128`[¶](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.SOMEIP_MSG_RESPONSE "Link to this definition")  

SOMEIP_MSG_ERROR = `129`[¶](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.SOMEIP_MSG_ERROR "Link to this definition")  

SOMEIP_RETURN_OK = `0`[¶](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.SOMEIP_RETURN_OK "Link to this definition")  

SOMEIP_RETURN_NOT_OK = `1`[¶](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.SOMEIP_RETURN_NOT_OK "Link to this definition")  

SOMEIP_RETURN_UNKNOWN_SERVICE = `2`[¶](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.SOMEIP_RETURN_UNKNOWN_SERVICE "Link to this definition")  

SOMEIP_RETURN_UNKNOWN_METHOD = `3`[¶](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.SOMEIP_RETURN_UNKNOWN_METHOD "Link to this definition")  

SOMEIP_RETURN_NOT_READY = `4`[¶](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.SOMEIP_RETURN_NOT_READY "Link to this definition")  

SOMEIP_RETURN_NOT_REACHABLE = `5`[¶](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.SOMEIP_RETURN_NOT_REACHABLE "Link to this definition")  

SOMEIP_RETURN_TIMEOUT = `6`[¶](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.SOMEIP_RETURN_TIMEOUT "Link to this definition")  

SOMEIP_RETURN_WRONG_PROTOCOL_VERSION = `7`[¶](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.SOMEIP_RETURN_WRONG_PROTOCOL_VERSION "Link to this definition")  

SOMEIP_RETURN_WRONG_INTERFACE_VERSION = `8`[¶](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.SOMEIP_RETURN_WRONG_INTERFACE_VERSION "Link to this definition")  

SOMEIP_RETURN_MALFORMED = `9`[¶](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.SOMEIP_RETURN_MALFORMED "Link to this definition")  

SOMEIP_RETURN_TCP_ERROR = `10`[¶](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.SOMEIP_RETURN_TCP_ERROR "Link to this definition")  

*classmethod* GetSomeIpMessagesFromPayload(*[data](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.GetSomeIpMessagesFromPayload "tts.lib.ethernet.PacketSomeIp.PacketSomeIp.GetSomeIpMessagesFromPayload.data (Python parameter)"): bytes*) → list[[PacketSomeIp](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp "tts.lib.ethernet.PacketSomeIp.PacketSomeIp (Python class) — In the test case, use api.Ethernet.PacketSomeIp; in UserPyModules, use from tts.lib.ethernet.PacketSomeIp import PacketSomeIp.")][¶](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.GetSomeIpMessagesFromPayload "Link to this definition")  
Creates one or multiple SOME/IP packets from data.

\<protocol\>  
Equivalent to method [`FindParent(protocol)`](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.FindParent "tts.lib.ethernet.PacketSomeIp.PacketSomeIp.FindParent (Python method) — Only for pseudo signals in trace analysis! Returns the requested protocol object if present, otherwise a NoProtocol object."). Direct access to parent protocols. *protocol* is one of [`OsiProtocol`](busdatastructuresTraceanalysis.md#tts.lib.ethernet.PacketEthernet.OsiProtocol "tts.lib.ethernet.PacketEthernet.OsiProtocol (Python class) — String Enumeration class representing the supported protocol layers.").

Example: Signal.eth.src provides the source MAC address of the Ethernet protocol layer.

Type:  [`EthernetProtocolBase`](busdatastructuresTraceanalysis.md#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase (Python class) — Base class for all protocol classes.")

*classmethod* Create(*[serviceId](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.Create.serviceId "tts.lib.ethernet.PacketSomeIp.PacketSomeIp.Create.serviceId (Python parameter) — defaults to 0x00")=`0`*, *[methodId](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.Create.methodId "tts.lib.ethernet.PacketSomeIp.PacketSomeIp.Create.methodId (Python parameter) — defaults to 0x00")=`0`*, *[clientId](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.Create.clientId "tts.lib.ethernet.PacketSomeIp.PacketSomeIp.Create.clientId (Python parameter) — defaults to 0x00")=`0`*, *[sessionId](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.Create.sessionId "tts.lib.ethernet.PacketSomeIp.PacketSomeIp.Create.sessionId (Python parameter) — defaults to 0x00")=`0`*, *[protocolVersion](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.Create.protocolVersion "tts.lib.ethernet.PacketSomeIp.PacketSomeIp.Create.protocolVersion (Python parameter) — defaults to 0x01")=`1`*, *[interfaceVersion](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.Create.interfaceVersion "tts.lib.ethernet.PacketSomeIp.PacketSomeIp.Create.interfaceVersion (Python parameter) — defaults to 0x01")=`1`*, *[messageType](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.Create.messageType "tts.lib.ethernet.PacketSomeIp.PacketSomeIp.Create.messageType (Python parameter) — defaults to api.Ethernet.PacketSomeIp.SOMEIP_MSG_REQUEST")=`0`*, *[returnCode](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.Create.returnCode "tts.lib.ethernet.PacketSomeIp.PacketSomeIp.Create.returnCode (Python parameter) — defaults to api.Ethernet.PacketSomeIp.SOMEIP_RETURN_OK")=`0`*, *[payload](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.Create.payload "tts.lib.ethernet.PacketSomeIp.PacketSomeIp.Create.payload (Python parameter) — defaults to None")=`None`*, *[length](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.Create.length "tts.lib.ethernet.PacketSomeIp.PacketSomeIp.Create.length (Python parameter) — defaults to 'Auto'")=`'Auto'`*, *[messageId](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.Create.messageId "tts.lib.ethernet.PacketSomeIp.PacketSomeIp.Create.messageId (Python parameter) — defaults to None")=`None`*, *[requestId](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.Create.requestId "tts.lib.ethernet.PacketSomeIp.PacketSomeIp.Create.requestId (Python parameter) — defaults to None")=`None`*)[¶](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.Create "Link to this definition")  
Returns a PacketSomeIp object as specified. If a messageId is given, any given serviceId and methodId will be overwritten. If a requestId is given, any given clientId and sessionId will be overwritten.

Parameters:  serviceId : int, optional[¶](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.Create.serviceId "Permalink to this definition")  
defaults to 0x00

methodId : int, optional[¶](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.Create.methodId "Permalink to this definition")  
defaults to 0x00

clientId : int, optional[¶](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.Create.clientId "Permalink to this definition")  
defaults to 0x00

sessionId : int, optional[¶](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.Create.sessionId "Permalink to this definition")  
defaults to 0x00

protocolVersion : int, optional[¶](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.Create.protocolVersion "Permalink to this definition")  
defaults to 0x01

interfaceVersion : int, optional[¶](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.Create.interfaceVersion "Permalink to this definition")  
defaults to 0x01

messageType : int | str, optional[¶](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.Create.messageType "Permalink to this definition")  
defaults to [`api.Ethernet.PacketSomeIp.SOMEIP_MSG_REQUEST`](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.SOMEIP_MSG_REQUEST "tts.lib.ethernet.PacketSomeIp.PacketSomeIp.SOMEIP_MSG_REQUEST (Python attribute)")

returnCode : int | str, optional[¶](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.Create.returnCode "Permalink to this definition")  
defaults to [`api.Ethernet.PacketSomeIp.SOMEIP_RETURN_OK`](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.SOMEIP_RETURN_OK "tts.lib.ethernet.PacketSomeIp.PacketSomeIp.SOMEIP_RETURN_OK (Python attribute)")

payload : bytes | [ByteStream](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream (Python class) — The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.") | None, optional[¶](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.Create.payload "Permalink to this definition")  
defaults to None

length : int, optional[¶](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.Create.length "Permalink to this definition")  
defaults to ‘Auto’

messageId : int | None, optional[¶](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.Create.messageId "Permalink to this definition")  
defaults to None

requestId : int | None, optional[¶](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.Create.requestId "Permalink to this definition")  
defaults to None

Returns:  PacketSomeIp object

Return type:  [`PacketSomeIp`](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp "tts.lib.ethernet.PacketSomeIp.PacketSomeIp (Python class) — In the test case, use api.Ethernet.PacketSomeIp; in UserPyModules, use from tts.lib.ethernet.PacketSomeIp import PacketSomeIp.")

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

FindParent(*[protocol](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.FindParent.protocol "tts.lib.ethernet.PacketSomeIp.PacketSomeIp.FindParent.protocol (Python parameter) — The required protocol name.")*)[¶](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.FindParent "Link to this definition")  
*Only for pseudo signals in trace analysis!* Returns the requested protocol object if present, otherwise a [`NoProtocol`](busdatastructuresTraceanalysis.md#tts.lib.ethernet.PacketEthernet.NoProtocol "tts.lib.ethernet.PacketEthernet.NoProtocol (Python class) — Represents a non-present protocol. Accessing any other parent of a non-present protocol will also yield a NoProtocol object. Accessing any protocol specific attributes will lead to an AttributeError since the specific protocol is not available. The boolean value of a NoProtocol object is always False, such that it can be used to check for the precense/absence of a protocol layer.") object.

Parameters:  protocol : [OsiProtocol](busdatastructuresTraceanalysis.md#tts.lib.ethernet.PacketEthernet.OsiProtocol "tts.lib.ethernet.PacketEthernet.OsiProtocol (Python class) — String Enumeration class representing the supported protocol layers.")[¶](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.FindParent.protocol "Permalink to this definition")  
The required protocol name.

Returns:  The required parent protocol object.

Return type:  [EthernetProtocolBase](busdatastructuresTraceanalysis.md#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase (Python class) — Base class for all protocol classes.")

parent[¶](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.parent "Link to this definition")  
*Only for pseudo signals in trace analysis!* Returns the parent protocol object if there is one present, otherwise None.

Return type:  [EthernetProtocolBase](busdatastructuresTraceanalysis.md#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase (Python class) — Base class for all protocol classes.") | None

timestamp[¶](#tts.lib.ethernet.PacketSomeIp.PacketSomeIp.timestamp "Link to this definition")  
Receive timestamp in sec., None if not available

Type:  Optional[float]

#### PacketSomeIpSd[¶](#packetsomeipsd "Link to this heading")

*class* PacketSomeIpSd[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSd "Link to this definition")  
In the test case, use `api.Ethernet.PacketSomeIpSd`; in UserPyModules, use `from tts.lib.ethernet.PacketSomeIpSd import PacketSomeIpSd`.

`\_\_init\_\_`(*[self](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSd.__init__ "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSd.__init__.self (Python parameter)")*, *[data](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSd.__init__ "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSd.__init__.data (Python parameter)"): bytes | None = `None`*)[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSd.__init__ "Link to this definition")  
Create a [`PacketSomeIpSd`](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSd "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSd (Python class) — In the test case, use api.Ethernet.PacketSomeIpSd; in UserPyModules, use from tts.lib.ethernet.PacketSomeIpSd import PacketSomeIpSd.") instance. Either from an existing payload, or empty.

\<protocol\>  
Equivalent to method [`FindParent(protocol)`](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSd.FindParent "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSd.FindParent (Python method) — Only for pseudo signals in trace analysis! Returns the requested protocol object if present, otherwise a NoProtocol object."). Direct access to parent protocols. *protocol* is one of [`OsiProtocol`](busdatastructuresTraceanalysis.md#tts.lib.ethernet.PacketEthernet.OsiProtocol "tts.lib.ethernet.PacketEthernet.OsiProtocol (Python class) — String Enumeration class representing the supported protocol layers.").

Example: Signal.eth.src provides the source MAC address of the Ethernet protocol layer.

Type:  [`EthernetProtocolBase`](busdatastructuresTraceanalysis.md#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase (Python class) — Base class for all protocol classes.")

CalcEntryArrayLen()[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSd.CalcEntryArrayLen "Link to this definition")  
Calculate and set the current length of all entries

CalcOptionArrayLen()[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSd.CalcOptionArrayLen "Link to this definition")  
Calculate and set the current length of all options

*classmethod* Create(*[rebootFlag](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSd.Create.rebootFlag "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSd.Create.rebootFlag (Python parameter) — defaults to True")=`True`*, *[unicastFlag](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSd.Create.unicastFlag "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSd.Create.unicastFlag (Python parameter) — defaults to True")=`True`*, *[entryList](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSd.Create.entryList "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSd.Create.entryList (Python parameter) — defaults to None")=`None`*, *[optionList](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSd.Create.optionList "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSd.Create.optionList (Python parameter) — defaults to None")=`None`*, *[entryArrayLength](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSd.Create.entryArrayLength "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSd.Create.entryArrayLength (Python parameter) — defaults to "Auto"")=`'Auto'`*, *[optionArrayLength](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSd.Create.optionArrayLength "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSd.Create.optionArrayLength (Python parameter) — defaults to "Auto"")=`'Auto'`*)[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSd.Create "Link to this definition")  
Returns a PacketSomeIpSd object as specified.

Parameters:  rebootFlag : bool | int, optional[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSd.Create.rebootFlag "Permalink to this definition")  
defaults to True

unicastFlag : bool | int, optional[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSd.Create.unicastFlag "Permalink to this definition")  
defaults to True

entryList=`None`[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSd.Create.entryList "Permalink to this definition")  
defaults to None

optionList=`None`[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSd.Create.optionList "Permalink to this definition")  
defaults to None

entryArrayLength : int, optional[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSd.Create.entryArrayLength "Permalink to this definition")  
defaults to “Auto”

optionArrayLength : int, optional[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSd.Create.optionArrayLength "Permalink to this definition")  
defaults to “Auto”

Returns:  PacketSomeIpSd object

Return type:  [`PacketSomeIpSd`](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSd "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSd (Python class) — In the test case, use api.Ethernet.PacketSomeIpSd; in UserPyModules, use from tts.lib.ethernet.PacketSomeIpSd import PacketSomeIpSd.")

FindParent(*[protocol](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSd.FindParent.protocol "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSd.FindParent.protocol (Python parameter) — The required protocol name.")*)[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSd.FindParent "Link to this definition")  
*Only for pseudo signals in trace analysis!* Returns the requested protocol object if present, otherwise a [`NoProtocol`](busdatastructuresTraceanalysis.md#tts.lib.ethernet.PacketEthernet.NoProtocol "tts.lib.ethernet.PacketEthernet.NoProtocol (Python class) — Represents a non-present protocol. Accessing any other parent of a non-present protocol will also yield a NoProtocol object. Accessing any protocol specific attributes will lead to an AttributeError since the specific protocol is not available. The boolean value of a NoProtocol object is always False, such that it can be used to check for the precense/absence of a protocol layer.") object.

Parameters:  protocol : [OsiProtocol](busdatastructuresTraceanalysis.md#tts.lib.ethernet.PacketEthernet.OsiProtocol "tts.lib.ethernet.PacketEthernet.OsiProtocol (Python class) — String Enumeration class representing the supported protocol layers.")[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSd.FindParent.protocol "Permalink to this definition")  
The required protocol name.

Returns:  The required parent protocol object.

Return type:  [EthernetProtocolBase](busdatastructuresTraceanalysis.md#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase (Python class) — Base class for all protocol classes.")

entryLen[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSd.entryLen "Link to this definition")  
length of all entries in bytes

Type:  int

entryList[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSd.entryList "Link to this definition")  
list of all SOME/IP-SD entries

Type:  list[[PacketSomeIpSdEntry](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntry "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntry (Python class) — In the test case, use api.Ethernet.PacketSomeIpSdEntry; in UserPyModules, use from tts.lib.ethernet.PacketSomeIpSd import PacketSomeIpSdEntry.")]

optionLen[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSd.optionLen "Link to this definition")  
length of all options in bytes

Type:  int

optionList[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSd.optionList "Link to this definition")  
list of all SOME/IP-SD options

Type:  list[[PacketSomeIpSdOption](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOption "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOption (Python class) — In the test case, use api.Ethernet.PacketSomeIpSdOption; in UserPyModules, use from tts.lib.ethernet.PacketSomeIpSd import PacketSomeIpSdOption.")]

parent[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSd.parent "Link to this definition")  
*Only for pseudo signals in trace analysis!* Returns the parent protocol object if there is one present, otherwise None.

Return type:  [EthernetProtocolBase](busdatastructuresTraceanalysis.md#tts.lib.ethernet.PacketEthernet.EthernetProtocolBase "tts.lib.ethernet.PacketEthernet.EthernetProtocolBase (Python class) — Base class for all protocol classes.") | None

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
Bases: [`PacketSomeIpSdEntry`](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntry "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntry (Python class) — In the test case, use api.Ethernet.PacketSomeIpSdEntry; in UserPyModules, use from tts.lib.ethernet.PacketSomeIpSd import PacketSomeIpSdEntry.")

In the test case, use `api.Ethernet.PacketSomeIpSdEntryService`; in UserPyModules, use `from tts.lib.ethernet.PacketSomeIpSd import PacketSomeIpSdEntryService`.

SERVICE_FIND = `0`[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryService.SERVICE_FIND "Link to this definition")  

SERVICE_OFFER = `1`[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryService.SERVICE_OFFER "Link to this definition")  

SERVICE_STOP_OFFER = `1`[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryService.SERVICE_STOP_OFFER "Link to this definition")  

*classmethod* Create(*[index1](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryService.Create.index1 "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryService.Create.index1 (Python parameter) — defaults to 0")=`0`*, *[index2](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryService.Create.index2 "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryService.Create.index2 (Python parameter) — defaults to 0")=`0`*, *[instanceId](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryService.Create.instanceId "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryService.Create.instanceId (Python parameter) — defaults to 1")=`1`*, *[majorVersion](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryService.Create.majorVersion "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryService.Create.majorVersion (Python parameter) — defaults to 1")=`1`*, *[minorVersion](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryService.Create.minorVersion "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryService.Create.minorVersion (Python parameter) — defaults to 0")=`0`*, *[optionCount1](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryService.Create.optionCount1 "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryService.Create.optionCount1 (Python parameter) — defaults to 0")=`0`*, *[optionCount2](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryService.Create.optionCount2 "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryService.Create.optionCount2 (Python parameter) — defaults to 0")=`0`*, *[serviceId](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryService.Create.serviceId "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryService.Create.serviceId (Python parameter) — defaults to 0")=`0`*, *[ttl](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryService.Create.ttl "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryService.Create.ttl (Python parameter) — defaults to 0")=`0`*, *[type](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryService.Create.type "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryService.Create.type (Python parameter) — defaults to api.Ethernet.PacketSomeIpSdEntryService.SERVICE_OFFER")=`1`*)[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryService.Create "Link to this definition")  
Returns a PacketSomeIpSdEntryService object as specified.

Parameters:  index1 : int, optional[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryService.Create.index1 "Permalink to this definition")  
defaults to 0

index2 : int, optional[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryService.Create.index2 "Permalink to this definition")  
defaults to 0

instanceId : int, optional[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryService.Create.instanceId "Permalink to this definition")  
defaults to 1

majorVersion : int, optional[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryService.Create.majorVersion "Permalink to this definition")  
defaults to 1

minorVersion : int, optional[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryService.Create.minorVersion "Permalink to this definition")  
defaults to 0

optionCount1 : int, optional[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryService.Create.optionCount1 "Permalink to this definition")  
defaults to 0

optionCount2 : int, optional[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryService.Create.optionCount2 "Permalink to this definition")  
defaults to 0

serviceId : int, optional[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryService.Create.serviceId "Permalink to this definition")  
defaults to 0

ttl : int, optional[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryService.Create.ttl "Permalink to this definition")  
defaults to 0

type : int, optional[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryService.Create.type "Permalink to this definition")  
defaults to [`api.Ethernet.PacketSomeIpSdEntryService.SERVICE_OFFER`](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryService.SERVICE_OFFER "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryService.SERVICE_OFFER (Python attribute)")

Returns:  PacketSomeIpSdEntryService object

Return type:  [`PacketSomeIpSdEntryService`](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryService "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryService (Python class) — Bases: PacketSomeIpSdEntry")

minorVersion[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryService.minorVersion "Link to this definition")  
minor version

Type:  int

#### PacketSomeIpSdEntryEventgroup[¶](#packetsomeipsdentryeventgroup "Link to this heading")

*class* PacketSomeIpSdEntryEventgroup[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryEventgroup "Link to this definition")  
Bases: [`PacketSomeIpSdEntry`](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntry "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntry (Python class) — In the test case, use api.Ethernet.PacketSomeIpSdEntry; in UserPyModules, use from tts.lib.ethernet.PacketSomeIpSd import PacketSomeIpSdEntry.")

In the test case, use `api.Ethernet.PacketSomeIpSdEntryEventgroup`; in UserPyModules, use `from tts.lib.ethernet.PacketSomeIpSd import PacketSomeIpSdEntryEventgroup`.

EVENTGROUP_SUBSCRIBE = `6`[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryEventgroup.EVENTGROUP_SUBSCRIBE "Link to this definition")  

EVENTGROUP_SUBSCRIBE_ACK = `7`[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryEventgroup.EVENTGROUP_SUBSCRIBE_ACK "Link to this definition")  

EVENTGROUP_STOP_SUBSCRIBE = `6`[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryEventgroup.EVENTGROUP_STOP_SUBSCRIBE "Link to this definition")  

EVENTGROUP_SUBSCRIBE_NACK = `7`[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryEventgroup.EVENTGROUP_SUBSCRIBE_NACK "Link to this definition")  

*classmethod* Create(*[eventgroupId](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryEventgroup.Create.eventgroupId "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryEventgroup.Create.eventgroupId (Python parameter) — defaults to 0")=`0`*, *[index1](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryEventgroup.Create.index1 "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryEventgroup.Create.index1 (Python parameter) — defaults to 0")=`0`*, *[index2](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryEventgroup.Create.index2 "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryEventgroup.Create.index2 (Python parameter) — defaults to 0")=`0`*, *[instanceId](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryEventgroup.Create.instanceId "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryEventgroup.Create.instanceId (Python parameter) — defaults to 1")=`1`*, *[majorVersion](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryEventgroup.Create.majorVersion "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryEventgroup.Create.majorVersion (Python parameter) — defaults to 1")=`1`*, *[optionCount1](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryEventgroup.Create.optionCount1 "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryEventgroup.Create.optionCount1 (Python parameter) — defaults to 0")=`0`*, *[optionCount2](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryEventgroup.Create.optionCount2 "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryEventgroup.Create.optionCount2 (Python parameter) — defaults to 0")=`0`*, *[serviceId](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryEventgroup.Create.serviceId "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryEventgroup.Create.serviceId (Python parameter) — defaults to 0")=`0`*, *[ttl](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryEventgroup.Create.ttl "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryEventgroup.Create.ttl (Python parameter) — defaults to 0")=`0`*, *[type](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryEventgroup.Create.type "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryEventgroup.Create.type (Python parameter) — defaults to api.Ethernet.PacketSomeIpSdEntryEventgroup.EVENTGROUP_SUBSCRIBE")=`6`*)[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryEventgroup.Create "Link to this definition")  
Returns a PacketSomeIpSdEntryEventgroup object as specified.

Parameters:  eventgroupId : int, optional[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryEventgroup.Create.eventgroupId "Permalink to this definition")  
defaults to 0

index1 : int, optional[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryEventgroup.Create.index1 "Permalink to this definition")  
defaults to 0

index2 : int, optional[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryEventgroup.Create.index2 "Permalink to this definition")  
defaults to 0

instanceId : int, optional[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryEventgroup.Create.instanceId "Permalink to this definition")  
defaults to 1

majorVersion : int, optional[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryEventgroup.Create.majorVersion "Permalink to this definition")  
defaults to 1

optionCount1 : int, optional[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryEventgroup.Create.optionCount1 "Permalink to this definition")  
defaults to 0

optionCount2 : int, optional[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryEventgroup.Create.optionCount2 "Permalink to this definition")  
defaults to 0

serviceId : int, optional[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryEventgroup.Create.serviceId "Permalink to this definition")  
defaults to 0

ttl : int, optional[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryEventgroup.Create.ttl "Permalink to this definition")  
defaults to 0

type : int, optional[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryEventgroup.Create.type "Permalink to this definition")  
defaults to [`api.Ethernet.PacketSomeIpSdEntryEventgroup.EVENTGROUP_SUBSCRIBE`](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryEventgroup.EVENTGROUP_SUBSCRIBE "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryEventgroup.EVENTGROUP_SUBSCRIBE (Python attribute)")

Returns:  PacketSomeIpSdEntryEventgroup object

Return type:  [`PacketSomeIpSdEntryEventgroup`](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryEventgroup "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryEventgroup (Python class) — Bases: PacketSomeIpSdEntry")

eventgroupId[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdEntryEventgroup.eventgroupId "Link to this definition")  
eventgroup id

Type:  int

#### PacketSomeIpSdOption[¶](#packetsomeipsdoption "Link to this heading")

*class* PacketSomeIpSdOption[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOption "Link to this definition")  
In the test case, use `api.Ethernet.PacketSomeIpSdOption`; in UserPyModules, use `from tts.lib.ethernet.PacketSomeIpSd import PacketSomeIpSdOption`.

TRANSPORT_TCP = `6`[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOption.TRANSPORT_TCP "Link to this definition")  

TRANSPORT_UDP = `17`[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOption.TRANSPORT_UDP "Link to this definition")  

PACKET_SOME_IP_SD_OPTION_CONFIG = `1`[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOption.PACKET_SOME_IP_SD_OPTION_CONFIG "Link to this definition")  

PACKET_SOME_IP_SD_OPTION_IPV4 = `4`[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOption.PACKET_SOME_IP_SD_OPTION_IPV4 "Link to this definition")  

PACKET_SOME_IP_SD_OPTION_IPV6 = `6`[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOption.PACKET_SOME_IP_SD_OPTION_IPV6 "Link to this definition")  

PACKET_SOME_IP_SD_OPTION_IPV4_MULTICAST = `20`[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOption.PACKET_SOME_IP_SD_OPTION_IPV4_MULTICAST "Link to this definition")  

PACKET_SOME_IP_SD_OPTION_IPV4_SD = `36`[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOption.PACKET_SOME_IP_SD_OPTION_IPV4_SD "Link to this definition")  

PACKET_SOME_IP_SD_OPTION_IPV6_MULTICAST = `22`[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOption.PACKET_SOME_IP_SD_OPTION_IPV6_MULTICAST "Link to this definition")  

PACKET_SOME_IP_SD_OPTION_IPV6_SD = `38`[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOption.PACKET_SOME_IP_SD_OPTION_IPV6_SD "Link to this definition")  

optionLen[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOption.optionLen "Link to this definition")  
length of this option from reserved field

Type:  int

type[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOption.type "Link to this definition")  
option type

Type:  int

#### PacketSomeIpSdOptionIpv4[¶](#packetsomeipsdoptionipv4 "Link to this heading")

*class* PacketSomeIpSdOptionIpv4[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4 "Link to this definition")  
Bases: [`PacketSomeIpSdOption`](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOption "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOption (Python class) — In the test case, use api.Ethernet.PacketSomeIpSdOption; in UserPyModules, use from tts.lib.ethernet.PacketSomeIpSd import PacketSomeIpSdOption.")

In the test case, use `api.Ethernet.PacketSomeIpSdOptionIpv4`; in UserPyModules, use `from tts.lib.ethernet.PacketSomeIpSd import PacketSomeIpSdOptionIpv4`.

*classmethod* Create(*[ip](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4.Create.ip "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4.Create.ip (Python parameter) — defaults to '127.0.0.1'")=`'127.0.0.1'`*, *[port](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4.Create.port "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4.Create.port (Python parameter) — defaults to 1234")=`1234`*, *[protocol](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4.Create.protocol "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4.Create.protocol (Python parameter) — defaults to api.Ethernet.UDP")=`17`*, *[optionLength](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4.Create.optionLength "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4.Create.optionLength (Python parameter) — defaults to "Auto"")=`'Auto'`*)[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4.Create "Link to this definition")  
Returns a PacketSomeIpSdOptionIpv4 object as specified.

Parameters:  ip : str, optional[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4.Create.ip "Permalink to this definition")  
defaults to ‘127.0.0.1’

port : int, optional[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4.Create.port "Permalink to this definition")  
defaults to 1234

protocol : int, optional[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4.Create.protocol "Permalink to this definition")  
defaults to [`api.Ethernet.UDP`](#tts.core.api.internalApi.Ethernet.Ethernet.UDP "tts.core.api.internalApi.Ethernet.Ethernet.UDP (Python attribute)")

optionLength : int, optional[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4.Create.optionLength "Permalink to this definition")  
defaults to “Auto”

Returns:  PacketSomeIpSdOptionIpv4 object

Return type:  [`PacketSomeIpSdOptionIpv4`](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4 "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4 (Python class) — Bases: PacketSomeIpSdOption")

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
transport layer protocol - [`api.Ethernet.UDP`](#tts.core.api.internalApi.Ethernet.Ethernet.UDP "tts.core.api.internalApi.Ethernet.Ethernet.UDP (Python attribute)"), [`api.Ethernet.TCP`](#tts.core.api.internalApi.Ethernet.Ethernet.TCP "tts.core.api.internalApi.Ethernet.Ethernet.TCP (Python attribute)")

Type:  int

#### PacketSomeIpSdOptionIpv6[¶](#packetsomeipsdoptionipv6 "Link to this heading")

*class* PacketSomeIpSdOptionIpv6[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6 "Link to this definition")  
Bases: [`PacketSomeIpSdOption`](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOption "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOption (Python class) — In the test case, use api.Ethernet.PacketSomeIpSdOption; in UserPyModules, use from tts.lib.ethernet.PacketSomeIpSd import PacketSomeIpSdOption.")

In the test case, use `api.Ethernet.PacketSomeIpSdOptionIpv6`; in UserPyModules, use `from tts.lib.ethernet.PacketSomeIpSd import PacketSomeIpSdOptionIpv6`.

*classmethod* Create(*[ip](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6.Create.ip "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6.Create.ip (Python parameter) — defaults to '::1'")=`'::1'`*, *[port](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6.Create.port "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6.Create.port (Python parameter) — defaults to 1234")=`1234`*, *[protocol](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6.Create.protocol "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6.Create.protocol (Python parameter) — defaults to api.Ethernet.UDP")=`17`*, *[optionLength](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6.Create.optionLength "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6.Create.optionLength (Python parameter) — defaults to "Auto"")=`'Auto'`*)[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6.Create "Link to this definition")  
Returns a PacketSomeIpSdEntryService object as specified

Parameters:  ip : str, optional[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6.Create.ip "Permalink to this definition")  
defaults to ‘::1’

port : int, optional[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6.Create.port "Permalink to this definition")  
defaults to 1234

protocol : int, optional[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6.Create.protocol "Permalink to this definition")  
defaults to [`api.Ethernet.UDP`](#tts.core.api.internalApi.Ethernet.Ethernet.UDP "tts.core.api.internalApi.Ethernet.Ethernet.UDP (Python attribute)")

optionLength : int, optional[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6.Create.optionLength "Permalink to this definition")  
defaults to “Auto”

Returns:  PacketSomeIpSdOptionIpv6 object

Return type:  [`PacketSomeIpSdOptionIpv6`](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6 "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6 (Python class) — Bases: PacketSomeIpSdOption")

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
transport layer protocol - [`api.Ethernet.UDP`](#tts.core.api.internalApi.Ethernet.Ethernet.UDP "tts.core.api.internalApi.Ethernet.Ethernet.UDP (Python attribute)"), [`api.Ethernet.TCP`](#tts.core.api.internalApi.Ethernet.Ethernet.TCP "tts.core.api.internalApi.Ethernet.Ethernet.TCP (Python attribute)")

Type:  int

#### PacketSomeIpSdOptionIpv4Multicast[¶](#packetsomeipsdoptionipv4multicast "Link to this heading")

*class* PacketSomeIpSdOptionIpv4Multicast[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4Multicast "Link to this definition")  
Bases: [`PacketSomeIpSdOptionIpv4`](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4 "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4 (Python class) — Bases: PacketSomeIpSdOption")

In the test case, use `api.Ethernet.PacketSomeIpSdOptionIpv4Multicast`; in UserPyModules, use `from tts.lib.ethernet.PacketSomeIpSd import PacketSomeIpSdOptionIpv4Multicast`.

*classmethod* Create(*[ip](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4Multicast.Create.ip "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4Multicast.Create.ip (Python parameter) — defaults to '127.0.0.1'")=`'127.0.0.1'`*, *[port](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4Multicast.Create.port "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4Multicast.Create.port (Python parameter) — defaults to 1234")=`1234`*, *[protocol](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4Multicast.Create.protocol "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4Multicast.Create.protocol (Python parameter) — defaults to api.Ethernet.UDP")=`17`*, *[optionLength](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4Multicast.Create.optionLength "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4Multicast.Create.optionLength (Python parameter) — defaults to "Auto"")=`'Auto'`*)[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4Multicast.Create "Link to this definition")  
Returns a PacketSomeIpSdOptionIpv4Multicast object as specified.

Parameters:  ip : str, optional[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4Multicast.Create.ip "Permalink to this definition")  
defaults to ‘127.0.0.1’

port : int, optional[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4Multicast.Create.port "Permalink to this definition")  
defaults to 1234

protocol : int, optional[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4Multicast.Create.protocol "Permalink to this definition")  
defaults to [`api.Ethernet.UDP`](#tts.core.api.internalApi.Ethernet.Ethernet.UDP "tts.core.api.internalApi.Ethernet.Ethernet.UDP (Python attribute)")

optionLength : int, optional[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4Multicast.Create.optionLength "Permalink to this definition")  
defaults to “Auto”

Returns:  PacketSomeIpSdOptionIpv4Multicast object

Return type:  [`PacketSomeIpSdOptionIpv4Multicast`](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4Multicast "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4Multicast (Python class) — Bases: PacketSomeIpSdOptionIpv4")

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
transport layer protocol - [`api.Ethernet.UDP`](#tts.core.api.internalApi.Ethernet.Ethernet.UDP "tts.core.api.internalApi.Ethernet.Ethernet.UDP (Python attribute)"), [`api.Ethernet.TCP`](#tts.core.api.internalApi.Ethernet.Ethernet.TCP "tts.core.api.internalApi.Ethernet.Ethernet.TCP (Python attribute)")

Type:  int

#### PacketSomeIpSdOptionIpv6Multicast[¶](#packetsomeipsdoptionipv6multicast "Link to this heading")

*class* PacketSomeIpSdOptionIpv6Multicast[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6Multicast "Link to this definition")  
Bases: [`PacketSomeIpSdOptionIpv6`](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6 "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6 (Python class) — Bases: PacketSomeIpSdOption")

In the test case, use `api.Ethernet.PacketSomeIpSdOptionIpv6Multicast`; in UserPyModules, use `from tts.lib.ethernet.PacketSomeIpSd import PacketSomeIpSdOptionIpv6Multicast`.

*classmethod* Create(*[ip](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6Multicast.Create.ip "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6Multicast.Create.ip (Python parameter) — defaults to '::1'")=`'::1'`*, *[port](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6Multicast.Create.port "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6Multicast.Create.port (Python parameter) — defaults to 1234")=`1234`*, *[protocol](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6Multicast.Create.protocol "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6Multicast.Create.protocol (Python parameter) — defaults to api.Ethernet.UDP")=`17`*, *[optionLength](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6Multicast.Create.optionLength "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6Multicast.Create.optionLength (Python parameter) — defaults to "Auto"")=`'Auto'`*)[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6Multicast.Create "Link to this definition")  
Returns a PacketSomeIpSdOptionIpv6Multicast object as specified.

Parameters:  ip : str, optional[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6Multicast.Create.ip "Permalink to this definition")  
defaults to ‘::1’

port : int, optional[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6Multicast.Create.port "Permalink to this definition")  
defaults to 1234

protocol : int, optional[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6Multicast.Create.protocol "Permalink to this definition")  
defaults to [`api.Ethernet.UDP`](#tts.core.api.internalApi.Ethernet.Ethernet.UDP "tts.core.api.internalApi.Ethernet.Ethernet.UDP (Python attribute)")

optionLength : int, optional[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6Multicast.Create.optionLength "Permalink to this definition")  
defaults to “Auto”

Returns:  PacketSomeIpSdOptionIpv6Multicast object

Return type:  [`PacketSomeIpSdOptionIpv6Multicast`](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6Multicast "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6Multicast (Python class) — Bases: PacketSomeIpSdOptionIpv6")

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
transport layer protocol - [`api.Ethernet.UDP`](#tts.core.api.internalApi.Ethernet.Ethernet.UDP "tts.core.api.internalApi.Ethernet.Ethernet.UDP (Python attribute)"), [`api.Ethernet.TCP`](#tts.core.api.internalApi.Ethernet.Ethernet.TCP "tts.core.api.internalApi.Ethernet.Ethernet.TCP (Python attribute)")

Type:  int

#### PacketSomeIpSdOptionIpv4SD[¶](#packetsomeipsdoptionipv4sd "Link to this heading")

*class* PacketSomeIpSdOptionIpv4SD[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4SD "Link to this definition")  
Bases: [`PacketSomeIpSdOptionIpv4`](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4 "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4 (Python class) — Bases: PacketSomeIpSdOption")

In the test case, use `api.Ethernet.PacketSomeIpSdOptionIpv4SD`; in UserPyModules, use `from tts.lib.ethernet.PacketSomeIpSd import PacketSomeIpSdOptionIpv4SD`.

*classmethod* Create(*[ip](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4SD.Create.ip "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4SD.Create.ip (Python parameter) — defaults to '127.0.0.1'")=`'127.0.0.1'`*, *[port](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4SD.Create.port "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4SD.Create.port (Python parameter) — defaults to 1234")=`1234`*, *[protocol](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4SD.Create.protocol "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4SD.Create.protocol (Python parameter) — defaults to api.Ethernet.UDP")=`17`*, *[optionLength](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4SD.Create.optionLength "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4SD.Create.optionLength (Python parameter) — defaults to "Auto"")=`'Auto'`*)[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4SD.Create "Link to this definition")  
Returns a PacketSomeIpSdOptionIpv4 object as specified.

Parameters:  ip : str, optional[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4SD.Create.ip "Permalink to this definition")  
defaults to ‘127.0.0.1’

port : int, optional[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4SD.Create.port "Permalink to this definition")  
defaults to 1234

protocol : int, optional[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4SD.Create.protocol "Permalink to this definition")  
defaults to [`api.Ethernet.UDP`](#tts.core.api.internalApi.Ethernet.Ethernet.UDP "tts.core.api.internalApi.Ethernet.Ethernet.UDP (Python attribute)")

optionLength : int, optional[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4SD.Create.optionLength "Permalink to this definition")  
defaults to “Auto”

Returns:  PacketSomeIpSdOptionIpv4 object

Return type:  [`PacketSomeIpSdOptionIpv4`](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4 "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv4 (Python class) — Bases: PacketSomeIpSdOption")

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
transport layer protocol - [`api.Ethernet.UDP`](#tts.core.api.internalApi.Ethernet.Ethernet.UDP "tts.core.api.internalApi.Ethernet.Ethernet.UDP (Python attribute)"), [`api.Ethernet.TCP`](#tts.core.api.internalApi.Ethernet.Ethernet.TCP "tts.core.api.internalApi.Ethernet.Ethernet.TCP (Python attribute)")

Type:  int

#### PacketSomeIpSdOptionIpv6SD[¶](#packetsomeipsdoptionipv6sd "Link to this heading")

*class* PacketSomeIpSdOptionIpv6SD[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6SD "Link to this definition")  
Bases: [`PacketSomeIpSdOptionIpv6`](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6 "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6 (Python class) — Bases: PacketSomeIpSdOption")

In the test case, use `api.Ethernet.PacketSomeIpSdOptionIpv6SD`; in UserPyModules, use `from tts.lib.ethernet.PacketSomeIpSd import PacketSomeIpSdOptionIpv6SD`.

*classmethod* Create(*[ip](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6SD.Create.ip "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6SD.Create.ip (Python parameter) — defaults to '::1'")=`'::1'`*, *[port](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6SD.Create.port "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6SD.Create.port (Python parameter) — defaults to 1234")=`1234`*, *[protocol](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6SD.Create.protocol "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6SD.Create.protocol (Python parameter) — defaults to api.Ethernet.UDP")=`17`*, *[optionLength](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6SD.Create.optionLength "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6SD.Create.optionLength (Python parameter) — defaults to "Auto"")=`'Auto'`*)[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6SD.Create "Link to this definition")  
Returns a PacketSomeIpSdEntryService object as specified

Parameters:  ip : str, optional[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6SD.Create.ip "Permalink to this definition")  
defaults to ‘::1’

port : int, optional[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6SD.Create.port "Permalink to this definition")  
defaults to 1234

protocol : int, optional[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6SD.Create.protocol "Permalink to this definition")  
defaults to [`api.Ethernet.UDP`](#tts.core.api.internalApi.Ethernet.Ethernet.UDP "tts.core.api.internalApi.Ethernet.Ethernet.UDP (Python attribute)")

optionLength : int, optional[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6SD.Create.optionLength "Permalink to this definition")  
defaults to “Auto”

Returns:  PacketSomeIpSdOptionIpv6 object

Return type:  [`PacketSomeIpSdOptionIpv6`](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6 "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionIpv6 (Python class) — Bases: PacketSomeIpSdOption")

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
transport layer protocol - [`api.Ethernet.UDP`](#tts.core.api.internalApi.Ethernet.Ethernet.UDP "tts.core.api.internalApi.Ethernet.Ethernet.UDP (Python attribute)"), [`api.Ethernet.TCP`](#tts.core.api.internalApi.Ethernet.Ethernet.TCP "tts.core.api.internalApi.Ethernet.Ethernet.TCP (Python attribute)")

Type:  int

#### PacketSomeIpSdOptionConfig[¶](#packetsomeipsdoptionconfig "Link to this heading")

*class* PacketSomeIpSdOptionConfig[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionConfig "Link to this definition")  
Bases: [`PacketSomeIpSdOption`](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOption "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOption (Python class) — In the test case, use api.Ethernet.PacketSomeIpSdOption; in UserPyModules, use from tts.lib.ethernet.PacketSomeIpSd import PacketSomeIpSdOption.")

In the test case, use `api.Ethernet.PacketSomeIpSdOptionConfig`; in UserPyModules, use `from tts.lib.ethernet.PacketSomeIpSd import PacketSomeIpSdOptionConfig`.

*classmethod* Create(*[config](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionConfig.Create.config "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionConfig.Create.config (Python parameter) — configuration parameters as dictionary")*, *[optionLength](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionConfig.Create.optionLength "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionConfig.Create.optionLength (Python parameter) — defaults to "Auto"")=`'Auto'`*)[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionConfig.Create "Link to this definition")  
Returns a PacketSomeIpSdOptionConfig object as specified.

Parameters:  config : dict, (format: {id1: value1, id2: value2, ...})[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionConfig.Create.config "Permalink to this definition")  
configuration parameters as dictionary

optionLength : int, optional[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionConfig.Create.optionLength "Permalink to this definition")  
defaults to “Auto”

Returns:  PacketSomeIpSdOptionConfig object

Return type:  [`PacketSomeIpSdOptionConfig`](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionConfig "tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionConfig (Python class) — Bases: PacketSomeIpSdOption")

config[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionConfig.config "Link to this definition")  
configuration parameter as dictionary (format: {id1: value1, id: value2, …})

Type:  dict

optionLen[¶](#tts.lib.ethernet.PacketSomeIpSd.PacketSomeIpSdOptionConfig.optionLen "Link to this definition")  
length of this option from reserved field

Type:  int

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
