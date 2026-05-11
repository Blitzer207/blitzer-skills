# Advanced properties of diagnostics related objects[¶](#advanced-properties-of-diagnostics-related-objects "Link to this heading")

## UDS result objects[¶](#uds-result-objects "Link to this heading")

*class* DiagResult(*responseObj*, *errCode*, *responseTime*, *pendingCount*, *busyCount*)[¶](#ttRawDiag.diag.DiagResult.DiagResult "Link to this definition")  
GetResponse()[¶](#ttRawDiag.diag.DiagResult.DiagResult.GetResponse "Link to this definition")  
Returns the diagnostics response.

Returns:  Diagnostics response or None if no reponse was received.

Return type:  [`ByteStream`](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream")

Response[¶](#ttRawDiag.diag.DiagResult.DiagResult.Response "Link to this definition")  
Diagnostics response

GetErrCode()[¶](#ttRawDiag.diag.DiagResult.DiagResult.GetErrCode "Link to this definition")  
Returns the error code.

Returns:  Error code: 0: “Ok”, 1: “Timeout in transport layer”, 2: “Received negative response”, 3: “No active diagnostics session”, 4: “Timeout waiting for diagnostics response”, 5: “Transmission error”, 6: “Unexpected response”, 7: “Still waiting for response”

Return type:  int

ErrCode[¶](#ttRawDiag.diag.DiagResult.DiagResult.ErrCode "Link to this definition")  
Error code

GetErrMsg()[¶](#ttRawDiag.diag.DiagResult.DiagResult.GetErrMsg "Link to this definition")  
Returns the error message.

Returns:  Error message: 0: “Ok”, 1: “Timeout in transport layer”, 2: “Received negative response”, 3: “No active diagnostics session”, 4: “Timeout waiting for diagnostics response”, 5: “Transmission error”, 6: “Unexpected response”, 7: “Still waiting for response”

Return type:  str

ErrMsg[¶](#ttRawDiag.diag.DiagResult.DiagResult.ErrMsg "Link to this definition")  
Error message

GetResponseTime()[¶](#ttRawDiag.diag.DiagResult.DiagResult.GetResponseTime "Link to this definition")  
Returns the time between sending the request and receiving the response in ms.

Returns:  Time until response was received in ms

Return type:  int

ResponseTime[¶](#ttRawDiag.diag.DiagResult.DiagResult.ResponseTime "Link to this definition")  
Time until response was received in ms.

GetPendingCount()[¶](#ttRawDiag.diag.DiagResult.DiagResult.GetPendingCount "Link to this definition")  
Returns the number of received RCRRP messages (Request correctly received, but response is pending).

Returns:  Number of received RCRRP messages

Return type:  int

PendingCount[¶](#ttRawDiag.diag.DiagResult.DiagResult.PendingCount "Link to this definition")  
Number of received RCRRP messages

GetBusyCount()[¶](#ttRawDiag.diag.DiagResult.DiagResult.GetBusyCount "Link to this definition")  
Returns the number of received BRR messages (Busy, repeat request).

Returns:  Number of received BRR messages

Return type:  int

BusyCount[¶](#ttRawDiag.diag.DiagResult.DiagResult.BusyCount "Link to this definition")  
Number of received BRR messages.

GetTpInfo()[¶](#ttRawDiag.diag.DiagResult.DiagResult.GetTpInfo "Link to this definition")  
Returns specific information of the underlying transport protocol, e.g. CAN, DoIP, FlexRay.

Returns:  Transport protocol specific information.

Return type:  dict

TpInfo[¶](#ttRawDiag.diag.DiagResult.DiagResult.TpInfo "Link to this definition")  
Transport protocol specific information

GetServiceId()[¶](#ttRawDiag.diag.DiagResult.DiagResult.GetServiceId "Link to this definition")  
Returns the service ID of the diagnostic response.

Returns:  Service ID of the diagnostic response

Return type:  int

ServiceId[¶](#ttRawDiag.diag.DiagResult.DiagResult.ServiceId "Link to this definition")  
Service ID of the diagnostic response

### Authentication[¶](#module-tts.tooling.common.genericBusAccess.busHw.diag.AuthenticationResult "Link to this heading")

*class* AuthenticationConfigurationResult[¶](#tts.tooling.common.genericBusAccess.busHw.diag.AuthenticationResult.AuthenticationConfigurationResult "Link to this definition")  
Bases: [`AuthenticationResult`](#tts.tooling.common.genericBusAccess.busHw.diag.AuthenticationResult.AuthenticationResult "tts.tooling.common.genericBusAccess.busHw.diag.AuthenticationResult.AuthenticationResult")

*class* AuthenticationDeauthenticateResult[¶](#tts.tooling.common.genericBusAccess.busHw.diag.AuthenticationResult.AuthenticationDeauthenticateResult "Link to this definition")  
Bases: [`AuthenticationResult`](#tts.tooling.common.genericBusAccess.busHw.diag.AuthenticationResult.AuthenticationResult "tts.tooling.common.genericBusAccess.busHw.diag.AuthenticationResult.AuthenticationResult")

*class* AuthenticationProofOfOwnershipResult[¶](#tts.tooling.common.genericBusAccess.busHw.diag.AuthenticationResult.AuthenticationProofOfOwnershipResult "Link to this definition")  
Bases: [`AuthenticationResult`](#tts.tooling.common.genericBusAccess.busHw.diag.AuthenticationResult.AuthenticationResult "tts.tooling.common.genericBusAccess.busHw.diag.AuthenticationResult.AuthenticationResult")

GetSessionKeyInfo()[¶](#tts.tooling.common.genericBusAccess.busHw.diag.AuthenticationResult.AuthenticationProofOfOwnershipResult.GetSessionKeyInfo "Link to this definition")  
If present, this value shall contain session key information, e.g. the encrypted session key(s) for securing further communication in the actual session and/or proof value(s) (e.g. a hash value) for the validation of the session key(s) on the client side.

NOTE 1 This information is linked to the contents of the request message data-parameter communicationConfiguration. The format of this parameter as well as the creation of the session key(s) and the computation of the proof value(s) are up to the vehicle manufacturer choice.

Return type:  [`ByteStream`](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream")

SessionKeyInfo[¶](#tts.tooling.common.genericBusAccess.busHw.diag.AuthenticationResult.AuthenticationProofOfOwnershipResult.SessionKeyInfo "Link to this definition")  
If present, this value shall contain session key information.

*class* AuthenticationResult[¶](#tts.tooling.common.genericBusAccess.busHw.diag.AuthenticationResult.AuthenticationResult "Link to this definition")  
Bases: [`DiagResult`](#ttRawDiag.diag.DiagResult.DiagResult "ttRawDiag.diag.DiagResult.DiagResult")

GetReturnValue()[¶](#tts.tooling.common.genericBusAccess.busHw.diag.AuthenticationResult.AuthenticationResult.GetReturnValue "Link to this definition")  
This parameter returns the result of the procedure on the server.

Return type:  int

ReturnValue[¶](#tts.tooling.common.genericBusAccess.busHw.diag.AuthenticationResult.AuthenticationResult.ReturnValue "Link to this definition")  
This parameter returns the result of the procedure on the server.

*class* AuthenticationVerifyCertificateUnidirectionalResult[¶](#tts.tooling.common.genericBusAccess.busHw.diag.AuthenticationResult.AuthenticationVerifyCertificateUnidirectionalResult "Link to this definition")  
Bases: [`AuthenticationResult`](#tts.tooling.common.genericBusAccess.busHw.diag.AuthenticationResult.AuthenticationResult "tts.tooling.common.genericBusAccess.busHw.diag.AuthenticationResult.AuthenticationResult")

ChallengeServer[¶](#tts.tooling.common.genericBusAccess.busHw.diag.AuthenticationResult.AuthenticationVerifyCertificateUnidirectionalResult.ChallengeServer "Link to this definition")  
The challenge contains vehicle manufacturer specific formatted server data.

EphemeralPublicKeyServer[¶](#tts.tooling.common.genericBusAccess.busHw.diag.AuthenticationResult.AuthenticationVerifyCertificateUnidirectionalResult.EphemeralPublicKeyServer "Link to this definition")  
Ephemeral public key generated by the server for Diffie-Hellman key agreement.

GetChallengeServer()[¶](#tts.tooling.common.genericBusAccess.busHw.diag.AuthenticationResult.AuthenticationVerifyCertificateUnidirectionalResult.GetChallengeServer "Link to this definition")  
The challenge contains vehicle manufacturer specific formatted server data (eventually containing randomized information) or is a random number. This parameter record is to transmit the challenge to the client.

Return type:  [`ByteStream`](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream")

GetEphemeralPublicKeyServer()[¶](#tts.tooling.common.genericBusAccess.busHw.diag.AuthenticationResult.AuthenticationVerifyCertificateUnidirectionalResult.GetEphemeralPublicKeyServer "Link to this definition")  
Ephemeral public key generated by the server for Diffie-Hellman key agreement.

Return type:  [`ByteStream`](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream")

### ECUReset[¶](#module-tts.tooling.common.genericBusAccess.busHw.diag.ECUResetResult "Link to this heading")

*class* ECUResetResult[¶](#tts.tooling.common.genericBusAccess.busHw.diag.ECUResetResult.ECUResetResult "Link to this definition")  
Bases: [`DiagResult`](#ttRawDiag.diag.DiagResult.DiagResult "ttRawDiag.diag.DiagResult.DiagResult")

This class represents the result of a successful ECUReset (0x11) call, consisting of the data record.

GetPowerDownTime()[¶](#tts.tooling.common.genericBusAccess.busHw.diag.ECUResetResult.ECUResetResult.GetPowerDownTime "Link to this definition")  
Returns the minimum time the server will remain in the power down sequence in seconds. 0xFF indicates a failure or time not available.

Returns:  Power down time

Return type:  int

PowerDownTime[¶](#tts.tooling.common.genericBusAccess.busHw.diag.ECUResetResult.ECUResetResult.PowerDownTime "Link to this definition")  
Returns the minimum time the server will remain in the power down sequence in seconds. 0xFF indicates a failure or time not available.

Returns:  Power down time

Return type:  int

### InputOutputControlByIdentifier[¶](#module-tts.tooling.common.genericBusAccess.busHw.diag.InputOutputControlByIdentifierResult "Link to this heading")

*class* InputOutputControlByIdentifierResult[¶](#tts.tooling.common.genericBusAccess.busHw.diag.InputOutputControlByIdentifierResult.InputOutputControlByIdentifierResult "Link to this definition")  
Bases: [`DiagResult`](#ttRawDiag.diag.DiagResult.DiagResult "ttRawDiag.diag.DiagResult.DiagResult")

Result of a successful InputOutputControlByIdentifier (0x2F) call, consisting of ID and data. Only one set of (ID, data) is supported.

GetDataIdentifier()[¶](#tts.tooling.common.genericBusAccess.busHw.diag.InputOutputControlByIdentifierResult.InputOutputControlByIdentifierResult.GetDataIdentifier "Link to this definition")  
Returns the data identifier.

Returns:  Data identifier

Return type:  int

DataIdentifier[¶](#tts.tooling.common.genericBusAccess.busHw.diag.InputOutputControlByIdentifierResult.InputOutputControlByIdentifierResult.DataIdentifier "Link to this definition")  
Returns the data identifier.

Returns:  Data identifier

Return type:  int

GetIoCtrlParam()[¶](#tts.tooling.common.genericBusAccess.busHw.diag.InputOutputControlByIdentifierResult.InputOutputControlByIdentifierResult.GetIoCtrlParam "Link to this definition")  
Returns the inputOutputControlParameter.

Returns:  inputOutputControlParameter

Return type:  int

IoCtrlParam[¶](#tts.tooling.common.genericBusAccess.busHw.diag.InputOutputControlByIdentifierResult.InputOutputControlByIdentifierResult.IoCtrlParam "Link to this definition")  
Returns the inputOutputControlParameter.

Returns:  inputOutputControlParameter

Return type:  int

GetData()[¶](#tts.tooling.common.genericBusAccess.busHw.diag.InputOutputControlByIdentifierResult.InputOutputControlByIdentifierResult.GetData "Link to this definition")  
Returns the data record.

Returns:  Data record

Return type:  [`ByteStream`](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream")

Data[¶](#tts.tooling.common.genericBusAccess.busHw.diag.InputOutputControlByIdentifierResult.InputOutputControlByIdentifierResult.Data "Link to this definition")  
Returns the data record.

Returns:  Data record

Return type:  [`ByteStream`](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream")

### ReadDataByIdentifier[¶](#module-tts.tooling.common.genericBusAccess.busHw.diag.ReadDataByIdentifierResult "Link to this heading")

*class* DataRecordDiagResult[¶](#tts.tooling.common.genericBusAccess.busHw.diag.ReadDataByIdentifierResult.DataRecordDiagResult "Link to this definition")  
Bases: [`DiagResult`](#ttRawDiag.diag.DiagResult.DiagResult "ttRawDiag.diag.DiagResult.DiagResult")

Result of a successful ReadDataByIdentifier (0x22) call, consisting of ID and data. Only one set of (ID, data) is supported.

GetDataIdentifier()[¶](#tts.tooling.common.genericBusAccess.busHw.diag.ReadDataByIdentifierResult.DataRecordDiagResult.GetDataIdentifier "Link to this definition")  
Returns the data identifier.

Returns:  Data identifier

Return type:  int

DataIdentifier[¶](#tts.tooling.common.genericBusAccess.busHw.diag.ReadDataByIdentifierResult.DataRecordDiagResult.DataIdentifier "Link to this definition")  
Returns the data identifier.

Returns:  Data identifier

Return type:  int

GetData()[¶](#tts.tooling.common.genericBusAccess.busHw.diag.ReadDataByIdentifierResult.DataRecordDiagResult.GetData "Link to this definition")  
Returns the data record.

Returns:  Data record

Return type:  [`ByteStream`](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream")

Data[¶](#tts.tooling.common.genericBusAccess.busHw.diag.ReadDataByIdentifierResult.DataRecordDiagResult.Data "Link to this definition")  
Returns the data record.

Returns:  Data record

Return type:  [`ByteStream`](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream")

### ReadDTCInformation[¶](#module-tts.testModule.diag.diagObjects.DTCResult "Link to this heading")

*class* DTCListDiagResult[¶](#tts.testModule.diag.diagObjects.DTCResult.DTCListDiagResult "Link to this definition")  
Bases: `list`, [`DiagResult`](#ttRawDiag.diag.DiagResult.DiagResult "ttRawDiag.diag.DiagResult.DiagResult")

This class represents the result of calling a diagnostic service whose response is expected to contain a DTC status availability mask and a list of DTCs and status codes, e.g. ReadDTCInformation.reportDTCByStatusMask.

Beside the methods and properties documented below, you can also use it just like a list. The list elements are of type [`DTCAndStatusRecord`](#tts.testModule.diag.diagObjects.DTCResult.DTCAndStatusRecord "tts.testModule.diag.diagObjects.DTCResult.DTCAndStatusRecord").

GetDTCStatusAvailabilityMask()[¶](#tts.testModule.diag.diagObjects.DTCResult.DTCListDiagResult.GetDTCStatusAvailabilityMask "Link to this definition")  
Returns the status availability mask as stated in the ECU’s response

Returns:  Status availability mask

Return type:  int

DTCStatusAvailabilityMask[¶](#tts.testModule.diag.diagObjects.DTCResult.DTCListDiagResult.DTCStatusAvailabilityMask "Link to this definition")  
Returns the status availability mask as stated in the ECU’s response

Returns:  Status availability mask

Return type:  int

*class* DTCNumber[¶](#tts.testModule.diag.diagObjects.DTCResult.DTCNumber "Link to this definition")  
Bases: `object`

This object represents a DTC.

GetNumber()[¶](#tts.testModule.diag.diagObjects.DTCResult.DTCNumber.GetNumber "Link to this definition")  
Returns the 3 byte DTC number

Returns:  DTC number

Return type:  int

Number[¶](#tts.testModule.diag.diagObjects.DTCResult.DTCNumber.Number "Link to this definition")  
Returns the 3 byte DTC number

Returns:  DTC number

Return type:  int

GetShortName()[¶](#tts.testModule.diag.diagObjects.DTCResult.DTCNumber.GetShortName "Link to this definition")  
Returns the short name

Returns:  DTC name

Return type:  str

SetShortName(*name*)[¶](#tts.testModule.diag.diagObjects.DTCResult.DTCNumber.SetShortName "Link to this definition")  
Set the short name

Parameters:  **name** (*str*) – DTC name

ShortName[¶](#tts.testModule.diag.diagObjects.DTCResult.DTCNumber.ShortName "Link to this definition")  
Returns the short name

Returns:  DTC name

Return type:  str

GetShortNumber()[¶](#tts.testModule.diag.diagObjects.DTCResult.DTCNumber.GetShortNumber "Link to this definition")  
Returns the 2 byte DTC number

Returns:  DTC number

Return type:  int

ShortNumber[¶](#tts.testModule.diag.diagObjects.DTCResult.DTCNumber.ShortNumber "Link to this definition")  
Returns the 2 byte DTC number

Returns:  DTC number

Return type:  int

GetDefinition()[¶](#tts.testModule.diag.diagObjects.DTCResult.DTCNumber.GetDefinition "Link to this definition")  
Returns the J2012 Representation (also known as P code) including the Failure Type Byte

Returns:  J2012 representation

Return type:  str

Definition[¶](#tts.testModule.diag.diagObjects.DTCResult.DTCNumber.Definition "Link to this definition")  
Returns the J2012 Representation (also known as P code) including the Failure Type Byte

Returns:  J2012 representation

Return type:  str

GetShortDefinition()[¶](#tts.testModule.diag.diagObjects.DTCResult.DTCNumber.GetShortDefinition "Link to this definition")  
Returns the J2012 Representation (also known as P code) without Failure Type Byte

Returns:  J2012 representation

Return type:  str

ShortDefinition[¶](#tts.testModule.diag.diagObjects.DTCResult.DTCNumber.ShortDefinition "Link to this definition")  
Returns the J2012 Representation (also known as P code) without Failure Type Byte

Returns:  J2012 representation

Return type:  str

GetFTB()[¶](#tts.testModule.diag.diagObjects.DTCResult.DTCNumber.GetFTB "Link to this definition")  
Returns the Failure Type Byte

Returns:  Failure type byte

Return type:  int

FTB[¶](#tts.testModule.diag.diagObjects.DTCResult.DTCNumber.FTB "Link to this definition")  
Returns the Failure Type Byte

Returns:  Failure type byte

Return type:  int

GetDescription()[¶](#tts.testModule.diag.diagObjects.DTCResult.DTCNumber.GetDescription "Link to this definition")  
Returns the description of the DTC, if known; else None

Returns:  DTC description

Return type:  str

SetDescription(*description*)[¶](#tts.testModule.diag.diagObjects.DTCResult.DTCNumber.SetDescription "Link to this definition")  
Set the description

Parameters:  **description** (*str*) – DTC description

Description[¶](#tts.testModule.diag.diagObjects.DTCResult.DTCNumber.Description "Link to this definition")  
Returns the description of the DTC, if known; else None

Returns:  DTC description

Return type:  str

*class* DTCAndStatusRecord[¶](#tts.testModule.diag.diagObjects.DTCResult.DTCAndStatusRecord "Link to this definition")  
Bases: [`DTCNumber`](#tts.testModule.diag.diagObjects.DTCResult.DTCNumber "tts.testModule.diag.diagObjects.DTCResult.DTCNumber")

This object represents a single DTC list entry, consisting of the DTC number itself and the status code.

GetStatus()[¶](#tts.testModule.diag.diagObjects.DTCResult.DTCAndStatusRecord.GetStatus "Link to this definition")  
Returns the DTC status code

Returns:  DTC status code

Return type:  int

Status[¶](#tts.testModule.diag.diagObjects.DTCResult.DTCAndStatusRecord.Status "Link to this definition")  
Returns the DTC status code

Returns:  DTC status code

Return type:  int

*class* DTCNumberDiagResult[¶](#tts.tooling.common.genericBusAccess.busHw.diag.ReadDTCInformationResult.DTCNumberDiagResult "Link to this definition")  
Bases: [`DiagResult`](#ttRawDiag.diag.DiagResult.DiagResult "ttRawDiag.diag.DiagResult.DiagResult")

This class represents the result of calling a diagnostic service whose response is expected to contain a DTC status availability mask, a DTC format identifier and the DTC count, e.g. ReadDTCInformation.reportNumberOfDTCByStatusMask.

GetDTCStatusAvailabilityMask()[¶](#tts.tooling.common.genericBusAccess.busHw.diag.ReadDTCInformationResult.DTCNumberDiagResult.GetDTCStatusAvailabilityMask "Link to this definition")  
Returns the status availability mask as stated in the ECU’s response

Returns:  Status availability mask

Return type:  int

DTCStatusAvailabilityMask[¶](#tts.tooling.common.genericBusAccess.busHw.diag.ReadDTCInformationResult.DTCNumberDiagResult.DTCStatusAvailabilityMask "Link to this definition")  
Returns the status availability mask as stated in the ECU’s response

Returns:  Status availability mask

Return type:  int

GetDTCFormatIdentifier()[¶](#tts.tooling.common.genericBusAccess.busHw.diag.ReadDTCInformationResult.DTCNumberDiagResult.GetDTCFormatIdentifier "Link to this definition")  
Returns the DTC format identifier

Returns:  DTC format identifier

Return type:  int

DTCFormatIdentifier[¶](#tts.tooling.common.genericBusAccess.busHw.diag.ReadDTCInformationResult.DTCNumberDiagResult.DTCFormatIdentifier "Link to this definition")  
Returns the DTC format identifier

Returns:  DTC format identifier

Return type:  int

GetDTCCount()[¶](#tts.tooling.common.genericBusAccess.busHw.diag.ReadDTCInformationResult.DTCNumberDiagResult.GetDTCCount "Link to this definition")  
Returns the DTC count

Returns:  DTC count

Return type:  int

DTCCount[¶](#tts.tooling.common.genericBusAccess.busHw.diag.ReadDTCInformationResult.DTCNumberDiagResult.DTCCount "Link to this definition")  
Returns the DTC count

Returns:  DTC count

Return type:  int

*class* DTCSnapshotIdentification[¶](#tts.tooling.common.genericBusAccess.busHw.diag.ReadDTCInformationResult.DTCSnapshotIdentification "Link to this definition")  
Bases: `object`

This object represents a single DTC snapshot identification list entry consisting of the DTC number and the according snapshot number.

GetDTC()[¶](#tts.tooling.common.genericBusAccess.busHw.diag.ReadDTCInformationResult.DTCSnapshotIdentification.GetDTC "Link to this definition")  
Returns the DTC number

Returns:  DTC number

Return type:  int

DTC[¶](#tts.tooling.common.genericBusAccess.busHw.diag.ReadDTCInformationResult.DTCSnapshotIdentification.DTC "Link to this definition")  
Returns the DTC number

Returns:  DTC number

Return type:  int

GetSnapshotNumber()[¶](#tts.tooling.common.genericBusAccess.busHw.diag.ReadDTCInformationResult.DTCSnapshotIdentification.GetSnapshotNumber "Link to this definition")  
Returns the snapshot number

Returns:  Snapshot number of the DTC

Return type:  int

SnapshotNumber[¶](#tts.tooling.common.genericBusAccess.busHw.diag.ReadDTCInformationResult.DTCSnapshotIdentification.SnapshotNumber "Link to this definition")  
Returns the snapshot number

Returns:  Snapshot number of the DTC

Return type:  int

*class* DTCSnapshotIdentificationDiagResult[¶](#tts.tooling.common.genericBusAccess.busHw.diag.ReadDTCInformationResult.DTCSnapshotIdentificationDiagResult "Link to this definition")  
Bases: [`DiagResult`](#ttRawDiag.diag.DiagResult.DiagResult "ttRawDiag.diag.DiagResult.DiagResult")

This class represents the result of calling a diagnostic service whose response is expected to contain a list of DTC numbers and according snapshot numbers, e.g. ReadDTCInformation.reportDTCSnapshotIdentification.

GetDTCSnapshotList()[¶](#tts.tooling.common.genericBusAccess.busHw.diag.ReadDTCInformationResult.DTCSnapshotIdentificationDiagResult.GetDTCSnapshotList "Link to this definition")  
Returns the snapshot list.

Returns:  List of DTCs and corresponding snapshot numbers

Return type:  list\<[`DTCSnapshotIdentification`](#tts.tooling.common.genericBusAccess.busHw.diag.ReadDTCInformationResult.DTCSnapshotIdentification "tts.tooling.common.genericBusAccess.busHw.diag.ReadDTCInformationResult.DTCSnapshotIdentification")\>

DTCSnapshotList[¶](#tts.tooling.common.genericBusAccess.busHw.diag.ReadDTCInformationResult.DTCSnapshotIdentificationDiagResult.DTCSnapshotList "Link to this definition")  
Returns the snapshot list.

Returns:  List of DTCs and corresponding snapshot numbers

Return type:  list\<[`DTCSnapshotIdentification`](#tts.tooling.common.genericBusAccess.busHw.diag.ReadDTCInformationResult.DTCSnapshotIdentification "tts.tooling.common.genericBusAccess.busHw.diag.ReadDTCInformationResult.DTCSnapshotIdentification")\>

*class* DTCFaultCounter[¶](#tts.tooling.common.genericBusAccess.busHw.diag.ReadDTCInformationResult.DTCFaultCounter "Link to this definition")  
Bases: `object`

This object represents a single DTC fault counter list entry consisting of the DTC number and the according fault counter.

GetDTC()[¶](#tts.tooling.common.genericBusAccess.busHw.diag.ReadDTCInformationResult.DTCFaultCounter.GetDTC "Link to this definition")  
Returns the DTC number

Returns:  DTC number

Return type:  int

DTC[¶](#tts.tooling.common.genericBusAccess.busHw.diag.ReadDTCInformationResult.DTCFaultCounter.DTC "Link to this definition")  
Returns the DTC number

Returns:  DTC number

Return type:  int

GetFaultCounter()[¶](#tts.tooling.common.genericBusAccess.busHw.diag.ReadDTCInformationResult.DTCFaultCounter.GetFaultCounter "Link to this definition")  
Returns the fault counter

Returns:  Fault counter of the DTC

Return type:  int

FaultCounter[¶](#tts.tooling.common.genericBusAccess.busHw.diag.ReadDTCInformationResult.DTCFaultCounter.FaultCounter "Link to this definition")  
Returns the fault counter

Returns:  Fault counter of the DTC

Return type:  int

*class* DTCFaultCounterDiagResult[¶](#tts.tooling.common.genericBusAccess.busHw.diag.ReadDTCInformationResult.DTCFaultCounterDiagResult "Link to this definition")  
Bases: [`DiagResult`](#ttRawDiag.diag.DiagResult.DiagResult "ttRawDiag.diag.DiagResult.DiagResult")

This class represents the result of calling a diagnostic service whose response is expected to contain a list of DTCs and fault counters, e.g. ReadDTCInformation.reportDTCFaultDetectionCounter.

GetDTCFaultList()[¶](#tts.tooling.common.genericBusAccess.busHw.diag.ReadDTCInformationResult.DTCFaultCounterDiagResult.GetDTCFaultList "Link to this definition")  
Returns the list of DTC faults

Returns:  List of DTCs and corresponding fault counter

Return type:  list\<[`DTCFaultCounter`](#tts.tooling.common.genericBusAccess.busHw.diag.ReadDTCInformationResult.DTCFaultCounter "tts.tooling.common.genericBusAccess.busHw.diag.ReadDTCInformationResult.DTCFaultCounter")\>

DTCFaultList[¶](#tts.tooling.common.genericBusAccess.busHw.diag.ReadDTCInformationResult.DTCFaultCounterDiagResult.DTCFaultList "Link to this definition")  
Returns the list of DTC faults

Returns:  List of DTCs and corresponding fault counter

Return type:  list\<[`DTCFaultCounter`](#tts.tooling.common.genericBusAccess.busHw.diag.ReadDTCInformationResult.DTCFaultCounter "tts.tooling.common.genericBusAccess.busHw.diag.ReadDTCInformationResult.DTCFaultCounter")\>

*class* UserDTCListDiagResult[¶](#tts.tooling.common.genericBusAccess.busHw.diag.ReadDTCInformationResult.UserDTCListDiagResult "Link to this definition")  
Bases: [`DTCListDiagResult`](#tts.testModule.diag.diagObjects.DTCResult.DTCListDiagResult "tts.testModule.diag.diagObjects.DTCResult.DTCListDiagResult")

This class represents the result of calling a diagnostic service whose response is expected to contain a memory selection, DTC status availability mask and a list of DTCs and status codes, e.g. ReadDTCInformation.reportUserDefMemoryDTCByStatusMask.

GetDTCMemorySelection()[¶](#tts.tooling.common.genericBusAccess.busHw.diag.ReadDTCInformationResult.UserDTCListDiagResult.GetDTCMemorySelection "Link to this definition")  
Returns the user DTC memory selection as stated in the ECU’s response

Returns:  Memory selection

Return type:  int

DTCMemorySelection[¶](#tts.tooling.common.genericBusAccess.busHw.diag.ReadDTCInformationResult.UserDTCListDiagResult.DTCMemorySelection "Link to this definition")  
Returns the user DTC memory selection as stated in the ECU’s response

Returns:  Memory selection

Return type:  int

### ReadMemoryByAddress[¶](#module-tts.tooling.common.genericBusAccess.busHw.diag.ReadMemoryByAddressResult "Link to this heading")

*class* MemoryDiagResult[¶](#tts.tooling.common.genericBusAccess.busHw.diag.ReadMemoryByAddressResult.MemoryDiagResult "Link to this definition")  
Bases: [`DiagResult`](#ttRawDiag.diag.DiagResult.DiagResult "ttRawDiag.diag.DiagResult.DiagResult")

This class represents the result of a successful ReadMemoryByAddress (0x23) call, consisting of the data record.

GetDataRecord()[¶](#tts.tooling.common.genericBusAccess.busHw.diag.ReadMemoryByAddressResult.MemoryDiagResult.GetDataRecord "Link to this definition")  
Returns the data record

Returns:  Data record

Return type:  [`BitStream`](variabledatastructures.md#tts.lib.dataStructures.BitStream.BitStream "tts.lib.dataStructures.BitStream.BitStream")

DataRecord[¶](#tts.tooling.common.genericBusAccess.busHw.diag.ReadMemoryByAddressResult.MemoryDiagResult.DataRecord "Link to this definition")  
Returns the data record

Returns:  Data record

Return type:  [`BitStream`](variabledatastructures.md#tts.lib.dataStructures.BitStream.BitStream "tts.lib.dataStructures.BitStream.BitStream")

### RoutineControl[¶](#module-tts.tooling.common.genericBusAccess.busHw.diag.RoutineControlResult "Link to this heading")

*class* RoutineDiagResult[¶](#tts.tooling.common.genericBusAccess.busHw.diag.RoutineControlResult.RoutineDiagResult "Link to this definition")  
Bases: [`DiagResult`](#ttRawDiag.diag.DiagResult.DiagResult "ttRawDiag.diag.DiagResult.DiagResult")

This class represents the result of a successful RoutineControl (0x31) call, consisting of the routine info and the routine status record.

GetRoutineControlType()[¶](#tts.tooling.common.genericBusAccess.busHw.diag.RoutineControlResult.RoutineDiagResult.GetRoutineControlType "Link to this definition")  
Returns the routine control type

Returns:  Routine Control Type

Return type:  int

GetRoutineId()[¶](#tts.tooling.common.genericBusAccess.busHw.diag.RoutineControlResult.RoutineDiagResult.GetRoutineId "Link to this definition")  
Returns the routine id

Returns:  Routine Id

Return type:  int

RoutineId[¶](#tts.tooling.common.genericBusAccess.busHw.diag.RoutineControlResult.RoutineDiagResult.RoutineId "Link to this definition")  
Returns the routine id

Returns:  Routine Id

Return type:  int

GetRoutineInfo()[¶](#tts.tooling.common.genericBusAccess.busHw.diag.RoutineControlResult.RoutineDiagResult.GetRoutineInfo "Link to this definition")  
Returns the routine info

Returns:  Routine Info

Return type:  [`BitStream`](variabledatastructures.md#tts.lib.dataStructures.BitStream.BitStream "tts.lib.dataStructures.BitStream.BitStream")

RoutineInfo[¶](#tts.tooling.common.genericBusAccess.busHw.diag.RoutineControlResult.RoutineDiagResult.RoutineInfo "Link to this definition")  
Returns the routine info

Returns:  Routine Info

Return type:  [`BitStream`](variabledatastructures.md#tts.lib.dataStructures.BitStream.BitStream "tts.lib.dataStructures.BitStream.BitStream")

GetStatusRecord()[¶](#tts.tooling.common.genericBusAccess.busHw.diag.RoutineControlResult.RoutineDiagResult.GetStatusRecord "Link to this definition")  
Returns the status record

Returns:  Status record

Return type:  [`ByteStream`](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream")

StatusRecord[¶](#tts.tooling.common.genericBusAccess.busHw.diag.RoutineControlResult.RoutineDiagResult.StatusRecord "Link to this definition")  
Returns the status record

Returns:  Status record

Return type:  [`ByteStream`](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream")

### SecurityAccess[¶](#module-tts.tooling.common.genericBusAccess.busHw.diag.SecurityAccessResult "Link to this heading")

*class* SecuritySeedDiagResult[¶](#tts.tooling.common.genericBusAccess.busHw.diag.SecurityAccessResult.SecuritySeedDiagResult "Link to this definition")  
Bases: [`DiagResult`](#ttRawDiag.diag.DiagResult.DiagResult "ttRawDiag.diag.DiagResult.DiagResult")

This class represents the result of calling the security access requestKey subfunction whose response is expected to contain a security seed.

GetSecuritySeed()[¶](#tts.tooling.common.genericBusAccess.busHw.diag.SecurityAccessResult.SecuritySeedDiagResult.GetSecuritySeed "Link to this definition")  
Returns the security seed of the ECU’s response

Returns:  Security seed

Return type:  int

SecuritySeed[¶](#tts.tooling.common.genericBusAccess.busHw.diag.SecurityAccessResult.SecuritySeedDiagResult.SecuritySeed "Link to this definition")  
Returns the security seed of the ECU’s response

Returns:  Security seed

Return type:  int

*class* SecurityAccessSuccessDiagResult[¶](#tts.tooling.common.genericBusAccess.busHw.diag.SecurityAccessResult.SecurityAccessSuccessDiagResult "Link to this definition")  
Bases: [`DiagResult`](#ttRawDiag.diag.DiagResult.DiagResult "ttRawDiag.diag.DiagResult.DiagResult")

This class represents the result of calling the security access sendKey subfunction.

IsAccessGranted()[¶](#tts.tooling.common.genericBusAccess.busHw.diag.SecurityAccessResult.SecurityAccessSuccessDiagResult.IsAccessGranted "Link to this definition")  
Returns whether the access is granted or not.

Returns:  Whether the access is granted

Return type:  int

AccessGranted[¶](#tts.tooling.common.genericBusAccess.busHw.diag.SecurityAccessResult.SecurityAccessSuccessDiagResult.AccessGranted "Link to this definition")  
Returns whether the access is granted or not.

Returns:  Whether the access is granted

Return type:  int

### WriteDataByIdentifier[¶](#module-tts.tooling.common.genericBusAccess.busHw.diag.WriteDataByIdentifierResult "Link to this heading")

*class* WriteDataByIdentifierResult[¶](#tts.tooling.common.genericBusAccess.busHw.diag.WriteDataByIdentifierResult.WriteDataByIdentifierResult "Link to this definition")  
Bases: [`DiagResult`](#ttRawDiag.diag.DiagResult.DiagResult "ttRawDiag.diag.DiagResult.DiagResult")

Result of a successful WriteDataByIdentifier (0x2E) call, consisting of ID.

GetDataIdentifier()[¶](#tts.tooling.common.genericBusAccess.busHw.diag.WriteDataByIdentifierResult.WriteDataByIdentifierResult.GetDataIdentifier "Link to this definition")  
Returns the data identifier.

Returns:  Data identifier

Return type:  int

DataIdentifier[¶](#tts.tooling.common.genericBusAccess.busHw.diag.WriteDataByIdentifierResult.WriteDataByIdentifierResult.DataIdentifier "Link to this definition")  
Returns the data identifier.

Returns:  Data identifier

Return type:  int

### WriteMemoryByAddress[¶](#module-tts.tooling.common.genericBusAccess.busHw.diag.WriteMemoryByAddressResult "Link to this heading")

*class* WriteMemoryByAddressResult[¶](#tts.tooling.common.genericBusAccess.busHw.diag.WriteMemoryByAddressResult.WriteMemoryByAddressResult "Link to this definition")  
Bases: [`DiagResult`](#ttRawDiag.diag.DiagResult.DiagResult "ttRawDiag.diag.DiagResult.DiagResult")

Result of a successful WriteMemoryByAddress (0x3D) call, consisting of MemoryAddress and MemorySize.

GetMemoryAddress()[¶](#tts.tooling.common.genericBusAccess.busHw.diag.WriteMemoryByAddressResult.WriteMemoryByAddressResult.GetMemoryAddress "Link to this definition")  
Returns the echo of the memory address.

Returns:  Memory address

Return type:  int

MemoryAddress[¶](#tts.tooling.common.genericBusAccess.busHw.diag.WriteMemoryByAddressResult.WriteMemoryByAddressResult.MemoryAddress "Link to this definition")  
Returns the echo of the memory address.

Returns:  Memory address

Return type:  int

GetMemorySize()[¶](#tts.tooling.common.genericBusAccess.busHw.diag.WriteMemoryByAddressResult.WriteMemoryByAddressResult.GetMemorySize "Link to this definition")  
Returns the echo of the memory size.

Returns:  Memory size

Return type:  int

MemorySize[¶](#tts.tooling.common.genericBusAccess.busHw.diag.WriteMemoryByAddressResult.WriteMemoryByAddressResult.MemorySize "Link to this definition")  
Returns the echo of the memory size.

Returns:  Memory size

Return type:  int

### NegativeResponse[¶](#module-tts.tooling.common.genericBusAccess.busHw.diag.NegativeResponse "Link to this heading")

*class* NegativeResponse[¶](#tts.tooling.common.genericBusAccess.busHw.diag.NegativeResponse.NegativeResponse "Link to this definition")  
Bases: [`DiagResult`](#ttRawDiag.diag.DiagResult.DiagResult "ttRawDiag.diag.DiagResult.DiagResult")

Representation of a negative UDS response.

GetUDSErrMsg()[¶](#tts.tooling.common.genericBusAccess.busHw.diag.NegativeResponse.NegativeResponse.GetUDSErrMsg "Link to this definition")  
Returns the UDS error message.

Returns:  UDS error message

Return type:  str

*class* UndefinedResponse[¶](#tts.tooling.common.genericBusAccess.busHw.diag.NegativeResponse.UndefinedResponse "Link to this definition")  
Bases: `object`

Im Fall, dass als Ergebniss eines Diagnoserequests ‘Undefined’ vorliegt (z.b. manueller Testabbruch) kann dies für eine schönere Meldung im Testreport in UndefinedReponse umgewandelt werden.

## KWP2000 result objects[¶](#kwp2000-result-objects "Link to this heading")

### ClearDTC[¶](#module-tts.tooling.common.genericBusAccess.busHw.diag.kwp2000.ClearDTCResult "Link to this heading")

*class* ClearDTCResult[¶](#tts.tooling.common.genericBusAccess.busHw.diag.kwp2000.ClearDTCResult.ClearDTCResult "Link to this definition")  
Bases: [`DiagResult`](#ttRawDiag.diag.DiagResult.DiagResult "ttRawDiag.diag.DiagResult.DiagResult")

Result of a successful ClearDTC (0x14) call, consisting of the optional DTC group.

GetGroupOfDTCs()[¶](#tts.tooling.common.genericBusAccess.busHw.diag.kwp2000.ClearDTCResult.ClearDTCResult.GetGroupOfDTCs "Link to this definition")  
Returns the DTC group.

Returns:  DTC group

Return type:  [`ByteStream`](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream")

GroupOfDTCs[¶](#tts.tooling.common.genericBusAccess.busHw.diag.kwp2000.ClearDTCResult.ClearDTCResult.GroupOfDTCs "Link to this definition")  
Returns the DTC group.

Returns:  DTC group

Return type:  [`ByteStream`](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream")

### ECUReset[¶](#diagapikwp2000ecureset "Link to this heading")

*class* ECUResetResult[¶](#tts.tooling.common.genericBusAccess.busHw.diag.kwp2000.ECUResetResult.ECUResetResult "Link to this definition")  
Bases: [`DiagResult`](#ttRawDiag.diag.DiagResult.DiagResult "ttRawDiag.diag.DiagResult.DiagResult")

This class represents the result of a successful ECUReset (0x11) call, consisting of the reset status.

GetResetStatus()[¶](#tts.tooling.common.genericBusAccess.busHw.diag.kwp2000.ECUResetResult.ECUResetResult.GetResetStatus "Link to this definition")  
Returns the optional Reset Status returned by the ECU.

Returns:  Reset status

Return type:  [`ByteStream`](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream")

ResetStatus[¶](#tts.tooling.common.genericBusAccess.busHw.diag.kwp2000.ECUResetResult.ECUResetResult.ResetStatus "Link to this definition")  
Returns the optional Reset Status returned by the ECU.

Returns:  Reset status

Return type:  [`ByteStream`](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream")

### InputOutputControlByCommonIdentifier[¶](#module-tts.tooling.common.genericBusAccess.busHw.diag.kwp2000.InputOutputControlByCommonIdentifierResult "Link to this heading")

*class* InputOutputControlByCommonIdentifierResult[¶](#tts.tooling.common.genericBusAccess.busHw.diag.kwp2000.InputOutputControlByCommonIdentifierResult.InputOutputControlByCommonIdentifierResult "Link to this definition")  
Bases: [`DiagResult`](#ttRawDiag.diag.DiagResult.DiagResult "ttRawDiag.diag.DiagResult.DiagResult")

Result of a successful InputOutputControlByCommonIdentifier (0x2F) call, consisting of ID and data. Only one set of (ID, data) is supported.

GetDataIdentifierHighByte()[¶](#tts.tooling.common.genericBusAccess.busHw.diag.kwp2000.InputOutputControlByCommonIdentifierResult.InputOutputControlByCommonIdentifierResult.GetDataIdentifierHighByte "Link to this definition")  
Returns the InputOutputCommonIdentifier (High Byte).

Returns:  InputOutputCommonIdentifier (High Byte)

Return type:  int

DataIdentifierHighByte[¶](#tts.tooling.common.genericBusAccess.busHw.diag.kwp2000.InputOutputControlByCommonIdentifierResult.InputOutputControlByCommonIdentifierResult.DataIdentifierHighByte "Link to this definition")  
Returns the InputOutputCommonIdentifier (High Byte).

Returns:  InputOutputCommonIdentifier (High Byte)

Return type:  int

GetDataIdentifierLowByte()[¶](#tts.tooling.common.genericBusAccess.busHw.diag.kwp2000.InputOutputControlByCommonIdentifierResult.InputOutputControlByCommonIdentifierResult.GetDataIdentifierLowByte "Link to this definition")  
Returns the InputOutputCommonIdentifier (Low Byte).

Returns:  InputOutputCommonIdentifier (Low Byte)

Return type:  int

DataIdentifierLowByte[¶](#tts.tooling.common.genericBusAccess.busHw.diag.kwp2000.InputOutputControlByCommonIdentifierResult.InputOutputControlByCommonIdentifierResult.DataIdentifierLowByte "Link to this definition")  
Returns the InputOutputCommonIdentifier (Low Byte).

Returns:  InputOutputCommonIdentifier (Low Byte)

Return type:  int

GetControlStatus()[¶](#tts.tooling.common.genericBusAccess.busHw.diag.kwp2000.InputOutputControlByCommonIdentifierResult.InputOutputControlByCommonIdentifierResult.GetControlStatus "Link to this definition")  
Returns the ControlStatus.

Returns:  ControlStatus

Return type:  [`ByteStream`](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream")

ControlStatus[¶](#tts.tooling.common.genericBusAccess.busHw.diag.kwp2000.InputOutputControlByCommonIdentifierResult.InputOutputControlByCommonIdentifierResult.ControlStatus "Link to this definition")  
Returns the ControlStatus.

Returns:  ControlStatus

Return type:  [`ByteStream`](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream")

### InputOutputControlByLocalIdentifier[¶](#module-tts.tooling.common.genericBusAccess.busHw.diag.kwp2000.InputOutputControlByLocalIdentifierResult "Link to this heading")

*class* InputOutputControlByLocalIdentifierResult[¶](#tts.tooling.common.genericBusAccess.busHw.diag.kwp2000.InputOutputControlByLocalIdentifierResult.InputOutputControlByLocalIdentifierResult "Link to this definition")  
Bases: [`DiagResult`](#ttRawDiag.diag.DiagResult.DiagResult "ttRawDiag.diag.DiagResult.DiagResult")

Result of a successful InputOutputControlByLocalIdentifier (0x30) call, consisting of ID and data. Only one set of (ID, data) is supported.

GetDataIdentifier()[¶](#tts.tooling.common.genericBusAccess.busHw.diag.kwp2000.InputOutputControlByLocalIdentifierResult.InputOutputControlByLocalIdentifierResult.GetDataIdentifier "Link to this definition")  
Returns the data identifier.

Returns:  Data identifier

Return type:  int

DataIdentifier[¶](#tts.tooling.common.genericBusAccess.busHw.diag.kwp2000.InputOutputControlByLocalIdentifierResult.InputOutputControlByLocalIdentifierResult.DataIdentifier "Link to this definition")  
Returns the data identifier.

Returns:  Data identifier

Return type:  int

GetControlStatus()[¶](#tts.tooling.common.genericBusAccess.busHw.diag.kwp2000.InputOutputControlByLocalIdentifierResult.InputOutputControlByLocalIdentifierResult.GetControlStatus "Link to this definition")  
Returns the ControlStatus.

Returns:  ControlStatus

Return type:  [ByteStream](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream")

ControlStatus[¶](#tts.tooling.common.genericBusAccess.busHw.diag.kwp2000.InputOutputControlByLocalIdentifierResult.InputOutputControlByLocalIdentifierResult.ControlStatus "Link to this definition")  
Returns the ControlStatus.

Returns:  ControlStatus

Return type:  [ByteStream](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream")

### ReadDataByCommonIdentifier[¶](#module-tts.tooling.common.genericBusAccess.busHw.diag.kwp2000.ReadDataByCommonIdentifierResult "Link to this heading")

*class* ReadDataByCommonIdentifierResult[¶](#tts.tooling.common.genericBusAccess.busHw.diag.kwp2000.ReadDataByCommonIdentifierResult.ReadDataByCommonIdentifierResult "Link to this definition")  
Bases: [`DiagResult`](#ttRawDiag.diag.DiagResult.DiagResult "ttRawDiag.diag.DiagResult.DiagResult")

Result of a successful ReadDataByLocalIdentifier (0x22) call, consisting of ID and data. Only one set of (ID, data) is supported.

GetDataIdentifierHighByte()[¶](#tts.tooling.common.genericBusAccess.busHw.diag.kwp2000.ReadDataByCommonIdentifierResult.ReadDataByCommonIdentifierResult.GetDataIdentifierHighByte "Link to this definition")  
Returns the RecordCommonIdentifier (High Byte).

Returns:  RecordCommonIdentifier (High Byte)

Return type:  int

DataIdentifierHighByte[¶](#tts.tooling.common.genericBusAccess.busHw.diag.kwp2000.ReadDataByCommonIdentifierResult.ReadDataByCommonIdentifierResult.DataIdentifierHighByte "Link to this definition")  
Returns the RecordCommonIdentifier (High Byte).

Returns:  RecordCommonIdentifier (High Byte)

Return type:  int

GetDataIdentifierLowByte()[¶](#tts.tooling.common.genericBusAccess.busHw.diag.kwp2000.ReadDataByCommonIdentifierResult.ReadDataByCommonIdentifierResult.GetDataIdentifierLowByte "Link to this definition")  
Returns the RecordCommonIdentifier (Low Byte).

Returns:  RecordCommonIdentifier (Low Byte)

Return type:  int

DataIdentifierLowByte[¶](#tts.tooling.common.genericBusAccess.busHw.diag.kwp2000.ReadDataByCommonIdentifierResult.ReadDataByCommonIdentifierResult.DataIdentifierLowByte "Link to this definition")  
Returns the RecordCommonIdentifier (Low Byte).

Returns:  RecordCommonIdentifier (Low Byte)

Return type:  int

GetData()[¶](#tts.tooling.common.genericBusAccess.busHw.diag.kwp2000.ReadDataByCommonIdentifierResult.ReadDataByCommonIdentifierResult.GetData "Link to this definition")  
Returns the record value.

Returns:  record value

Return type:  [`ByteStream`](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream")

Data[¶](#tts.tooling.common.genericBusAccess.busHw.diag.kwp2000.ReadDataByCommonIdentifierResult.ReadDataByCommonIdentifierResult.Data "Link to this definition")  
Returns the record value.

Returns:  record value

Return type:  [`ByteStream`](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream")

### ReadDataByLocalIdentifier[¶](#module-tts.tooling.common.genericBusAccess.busHw.diag.kwp2000.ReadDataByLocalIdentifierResult "Link to this heading")

*class* ReadDataByLocalIdentifierResult[¶](#tts.tooling.common.genericBusAccess.busHw.diag.kwp2000.ReadDataByLocalIdentifierResult.ReadDataByLocalIdentifierResult "Link to this definition")  
Bases: [`DiagResult`](#ttRawDiag.diag.DiagResult.DiagResult "ttRawDiag.diag.DiagResult.DiagResult")

Result of a successful ReadDataByLocalIdentifier (0x21) call, consisting of ID and data. Only one set of (ID, data) is supported.

GetDataIdentifier()[¶](#tts.tooling.common.genericBusAccess.busHw.diag.kwp2000.ReadDataByLocalIdentifierResult.ReadDataByLocalIdentifierResult.GetDataIdentifier "Link to this definition")  
Returns the RecordLocalIdentifier.

Returns:  RecordLocalIdentifier

Return type:  int

DataIdentifier[¶](#tts.tooling.common.genericBusAccess.busHw.diag.kwp2000.ReadDataByLocalIdentifierResult.ReadDataByLocalIdentifierResult.DataIdentifier "Link to this definition")  
Returns the RecordLocalIdentifier.

Returns:  RecordLocalIdentifier

Return type:  int

GetData()[¶](#tts.tooling.common.genericBusAccess.busHw.diag.kwp2000.ReadDataByLocalIdentifierResult.ReadDataByLocalIdentifierResult.GetData "Link to this definition")  
Returns the record value.

Returns:  record value

Return type:  [`ByteStream`](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream")

Data[¶](#tts.tooling.common.genericBusAccess.busHw.diag.kwp2000.ReadDataByLocalIdentifierResult.ReadDataByLocalIdentifierResult.Data "Link to this definition")  
Returns the record value.

Returns:  record value

Return type:  [`ByteStream`](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream")

### ReadDTCInformation[¶](#diagapikwp2000readdtcinformation "Link to this heading")

*class* ReadDiagnosticTroubleCodesDiagResult[¶](#tts.tooling.common.genericBusAccess.busHw.diag.kwp2000.ReadDTCInformationResult.ReadDiagnosticTroubleCodesDiagResult "Link to this definition")  
Bases: [`DiagResult`](#ttRawDiag.diag.DiagResult.DiagResult "ttRawDiag.diag.DiagResult.DiagResult")

This class represents the result of a successful ReadDiagnosticTroubleCodes (0x13) call, consisting of the number and list of DTCs.

GetDTCCount()[¶](#tts.tooling.common.genericBusAccess.busHw.diag.kwp2000.ReadDTCInformationResult.ReadDiagnosticTroubleCodesDiagResult.GetDTCCount "Link to this definition")  
Returns the DTC count

Returns:  DTC count

Return type:  int

DTCCount[¶](#tts.tooling.common.genericBusAccess.busHw.diag.kwp2000.ReadDTCInformationResult.ReadDiagnosticTroubleCodesDiagResult.DTCCount "Link to this definition")  
Returns the DTC count

Returns:  DTC count

Return type:  int

GetDTCFaultList()[¶](#tts.tooling.common.genericBusAccess.busHw.diag.kwp2000.ReadDTCInformationResult.ReadDiagnosticTroubleCodesDiagResult.GetDTCFaultList "Link to this definition")  
Returns the list of DTC faults

Returns:  List of DTCs

Return type:  list\<[`DTCNumber`](#tts.testModule.diag.diagObjects.DTCResult.DTCNumber "tts.testModule.diag.diagObjects.DTCResult.DTCNumber")\>

DTCFaultList[¶](#tts.tooling.common.genericBusAccess.busHw.diag.kwp2000.ReadDTCInformationResult.ReadDiagnosticTroubleCodesDiagResult.DTCFaultList "Link to this definition")  
Returns the list of DTC faults

Returns:  List of DTCs

Return type:  list\<[`DTCNumber`](#tts.testModule.diag.diagObjects.DTCResult.DTCNumber "tts.testModule.diag.diagObjects.DTCResult.DTCNumber")\>

*class* ReadDiagnosticTroubleCodesAndStatusDiagResult[¶](#tts.tooling.common.genericBusAccess.busHw.diag.kwp2000.ReadDTCInformationResult.ReadDiagnosticTroubleCodesAndStatusDiagResult "Link to this definition")  
Bases: [`DiagResult`](#ttRawDiag.diag.DiagResult.DiagResult "ttRawDiag.diag.DiagResult.DiagResult")

This class represents the result of a successful ReadDiagnosticTroubleCodesByStatus (0x18) or ReadStatusOfDiagnosticTroubleCodes (0x17) call, consisting of the number and list of DTCs and status.

GetDTCCount()[¶](#tts.tooling.common.genericBusAccess.busHw.diag.kwp2000.ReadDTCInformationResult.ReadDiagnosticTroubleCodesAndStatusDiagResult.GetDTCCount "Link to this definition")  
Returns the DTC count

Returns:  DTC count

Return type:  int

DTCCount[¶](#tts.tooling.common.genericBusAccess.busHw.diag.kwp2000.ReadDTCInformationResult.ReadDiagnosticTroubleCodesAndStatusDiagResult.DTCCount "Link to this definition")  
Returns the DTC count

Returns:  DTC count

Return type:  int

GetDTCFaultList()[¶](#tts.tooling.common.genericBusAccess.busHw.diag.kwp2000.ReadDTCInformationResult.ReadDiagnosticTroubleCodesAndStatusDiagResult.GetDTCFaultList "Link to this definition")  
Returns the list of DTC faults

Returns:  List of DTCs and corresponding status

Return type:  list\<[`DTCAndStatusRecord`](#tts.testModule.diag.diagObjects.DTCResult.DTCAndStatusRecord "tts.testModule.diag.diagObjects.DTCResult.DTCAndStatusRecord")\>

DTCFaultList[¶](#tts.tooling.common.genericBusAccess.busHw.diag.kwp2000.ReadDTCInformationResult.ReadDiagnosticTroubleCodesAndStatusDiagResult.DTCFaultList "Link to this definition")  
Returns the list of DTC faults

Returns:  List of DTCs and corresponding status

Return type:  list\<[`DTCAndStatusRecord`](#tts.testModule.diag.diagObjects.DTCResult.DTCAndStatusRecord "tts.testModule.diag.diagObjects.DTCResult.DTCAndStatusRecord")\>

### ReadECUIdentification[¶](#module-tts.tooling.common.genericBusAccess.busHw.diag.kwp2000.ReadECUIdentificationResult "Link to this heading")

*class* ReadECUIdentificationResult[¶](#tts.tooling.common.genericBusAccess.busHw.diag.kwp2000.ReadECUIdentificationResult.ReadECUIdentificationResult "Link to this definition")  
Bases: [`DiagResult`](#ttRawDiag.diag.DiagResult.DiagResult "ttRawDiag.diag.DiagResult.DiagResult")

Result of a successful ReadECUIdentification (0x1A) call, consisting of ID and data. Only one set of (ID, data) is supported.

GetDataIdentifier()[¶](#tts.tooling.common.genericBusAccess.busHw.diag.kwp2000.ReadECUIdentificationResult.ReadECUIdentificationResult.GetDataIdentifier "Link to this definition")  
Returns the data identifier.

Returns:  Data identifier

Return type:  int

DataIdentifier[¶](#tts.tooling.common.genericBusAccess.busHw.diag.kwp2000.ReadECUIdentificationResult.ReadECUIdentificationResult.DataIdentifier "Link to this definition")  
Returns the data identifier.

Returns:  Data identifier

Return type:  int

GetData()[¶](#tts.tooling.common.genericBusAccess.busHw.diag.kwp2000.ReadECUIdentificationResult.ReadECUIdentificationResult.GetData "Link to this definition")  
Returns the ECU identification parameters.

Returns:  ECU identification parameters

Return type:  [`ByteStream`](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream")

Data[¶](#tts.tooling.common.genericBusAccess.busHw.diag.kwp2000.ReadECUIdentificationResult.ReadECUIdentificationResult.Data "Link to this definition")  
Returns the ECU identification parameters.

Returns:  ECU identification parameters

Return type:  [`ByteStream`](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream")

### RoutineControl[¶](#diagapikwp2000routinecontrol "Link to this heading")

*class* RoutineByLocalIdentifierDiagResult[¶](#tts.tooling.common.genericBusAccess.busHw.diag.kwp2000.RoutineControlResult.RoutineByLocalIdentifierDiagResult "Link to this definition")  
Bases: [`DiagResult`](#ttRawDiag.diag.DiagResult.DiagResult "ttRawDiag.diag.DiagResult.DiagResult")

This class represents the result of a successful RoutineByLocalIdentifier call

GetRoutineId()[¶](#tts.tooling.common.genericBusAccess.busHw.diag.kwp2000.RoutineControlResult.RoutineByLocalIdentifierDiagResult.GetRoutineId "Link to this definition")  
Returns the routine id

Returns:  Routine Id

Return type:  int

RoutineId[¶](#tts.tooling.common.genericBusAccess.busHw.diag.kwp2000.RoutineControlResult.RoutineByLocalIdentifierDiagResult.RoutineId "Link to this definition")  
Returns the routine id

Returns:  Routine Id

Return type:  int

GetStatusRecord()[¶](#tts.tooling.common.genericBusAccess.busHw.diag.kwp2000.RoutineControlResult.RoutineByLocalIdentifierDiagResult.GetStatusRecord "Link to this definition")  
Returns the status record

Returns:  Status record

Return type:  [`ByteStream`](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream")

StatusRecord[¶](#tts.tooling.common.genericBusAccess.busHw.diag.kwp2000.RoutineControlResult.RoutineByLocalIdentifierDiagResult.StatusRecord "Link to this definition")  
Returns the status record

Returns:  Status record

Return type:  [`ByteStream`](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream")

*class* StartRoutineByLocalIdentifierDiagResult[¶](#tts.tooling.common.genericBusAccess.busHw.diag.kwp2000.RoutineControlResult.StartRoutineByLocalIdentifierDiagResult "Link to this definition")  
Bases: [`RoutineByLocalIdentifierDiagResult`](#tts.tooling.common.genericBusAccess.busHw.diag.kwp2000.RoutineControlResult.RoutineByLocalIdentifierDiagResult "tts.tooling.common.genericBusAccess.busHw.diag.kwp2000.RoutineControlResult.RoutineByLocalIdentifierDiagResult")

This class represents the result of a successful StartRoutineByLocalIdentifier (0x31) call, consisting of the routine entry status.

GetEntryStatus()[¶](#tts.tooling.common.genericBusAccess.busHw.diag.kwp2000.RoutineControlResult.StartRoutineByLocalIdentifierDiagResult.GetEntryStatus "Link to this definition")  
Returns the entry status

Returns:  Entry status

Return type:  [`ByteStream`](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream")

EntryStatus[¶](#tts.tooling.common.genericBusAccess.busHw.diag.kwp2000.RoutineControlResult.StartRoutineByLocalIdentifierDiagResult.EntryStatus "Link to this definition")  
Returns the entry status

Returns:  Entry status

Return type:  [`ByteStream`](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream")

*class* StopRoutineByLocalIdentifierDiagResult[¶](#tts.tooling.common.genericBusAccess.busHw.diag.kwp2000.RoutineControlResult.StopRoutineByLocalIdentifierDiagResult "Link to this definition")  
Bases: [`RoutineByLocalIdentifierDiagResult`](#tts.tooling.common.genericBusAccess.busHw.diag.kwp2000.RoutineControlResult.RoutineByLocalIdentifierDiagResult "tts.tooling.common.genericBusAccess.busHw.diag.kwp2000.RoutineControlResult.RoutineByLocalIdentifierDiagResult")

This class represents the result of a successful StopRoutineByLocalIdentifier (0x32) call, consisting of the routine exit status.

GetExitStatus()[¶](#tts.tooling.common.genericBusAccess.busHw.diag.kwp2000.RoutineControlResult.StopRoutineByLocalIdentifierDiagResult.GetExitStatus "Link to this definition")  
Returns the exit status

Returns:  exit status

Return type:  [`ByteStream`](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream")

ExitStatus[¶](#tts.tooling.common.genericBusAccess.busHw.diag.kwp2000.RoutineControlResult.StopRoutineByLocalIdentifierDiagResult.ExitStatus "Link to this definition")  
Returns the exit status

Returns:  exit status

Return type:  [`ByteStream`](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream")

*class* RequestRoutineByLocalIdentifierDiagResult[¶](#tts.tooling.common.genericBusAccess.busHw.diag.kwp2000.RoutineControlResult.RequestRoutineByLocalIdentifierDiagResult "Link to this definition")  
Bases: [`RoutineByLocalIdentifierDiagResult`](#tts.tooling.common.genericBusAccess.busHw.diag.kwp2000.RoutineControlResult.RoutineByLocalIdentifierDiagResult "tts.tooling.common.genericBusAccess.busHw.diag.kwp2000.RoutineControlResult.RoutineByLocalIdentifierDiagResult")

This class represents the result of a successful RequestRoutineByLocalIdentifier (0x33) call, consisting of the routine results.

GetRoutineResults()[¶](#tts.tooling.common.genericBusAccess.busHw.diag.kwp2000.RoutineControlResult.RequestRoutineByLocalIdentifierDiagResult.GetRoutineResults "Link to this definition")  
Returns the routine results

Returns:  Routine results

Return type:  [`ByteStream`](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream")

RoutineResults[¶](#tts.tooling.common.genericBusAccess.busHw.diag.kwp2000.RoutineControlResult.RequestRoutineByLocalIdentifierDiagResult.RoutineResults "Link to this definition")  
Returns the routine results

Returns:  Routine results

Return type:  [`ByteStream`](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream")

### WriteDataByCommonIdentifier[¶](#module-tts.tooling.common.genericBusAccess.busHw.diag.kwp2000.WriteDataByCommonIdentifierResult "Link to this heading")

*class* WriteDataByCommonIdentifierResult[¶](#tts.tooling.common.genericBusAccess.busHw.diag.kwp2000.WriteDataByCommonIdentifierResult.WriteDataByCommonIdentifierResult "Link to this definition")  
Bases: [`DiagResult`](#ttRawDiag.diag.DiagResult.DiagResult "ttRawDiag.diag.DiagResult.DiagResult")

Result of a successful WriteDataByCommonIdentifier (0x3B) call, consisting of ID.

GetDataIdentifierHighByte()[¶](#tts.tooling.common.genericBusAccess.busHw.diag.kwp2000.WriteDataByCommonIdentifierResult.WriteDataByCommonIdentifierResult.GetDataIdentifierHighByte "Link to this definition")  
Returns the RecordCommonIdentifier (High Byte).

Returns:  RecordCommonIdentifier (High Byte)

Return type:  int

DataIdentifierHighByte[¶](#tts.tooling.common.genericBusAccess.busHw.diag.kwp2000.WriteDataByCommonIdentifierResult.WriteDataByCommonIdentifierResult.DataIdentifierHighByte "Link to this definition")  
Returns the RecordCommonIdentifier (High Byte).

Returns:  RecordCommonIdentifier (High Byte)

Return type:  int

GetDataIdentifierLowByte()[¶](#tts.tooling.common.genericBusAccess.busHw.diag.kwp2000.WriteDataByCommonIdentifierResult.WriteDataByCommonIdentifierResult.GetDataIdentifierLowByte "Link to this definition")  
Returns the RecordCommonIdentifier (Low Byte).

Returns:  RecordCommonIdentifier (Low Byte)

Return type:  int

DataIdentifierLowByte[¶](#tts.tooling.common.genericBusAccess.busHw.diag.kwp2000.WriteDataByCommonIdentifierResult.WriteDataByCommonIdentifierResult.DataIdentifierLowByte "Link to this definition")  
Returns the RecordCommonIdentifier (Low Byte).

Returns:  RecordCommonIdentifier (Low Byte)

Return type:  int

### WriteDataByLocalIdentifier[¶](#module-tts.tooling.common.genericBusAccess.busHw.diag.kwp2000.WriteDataByLocalIdentifierResult "Link to this heading")

*class* WriteDataByLocalIdentifierResult[¶](#tts.tooling.common.genericBusAccess.busHw.diag.kwp2000.WriteDataByLocalIdentifierResult.WriteDataByLocalIdentifierResult "Link to this definition")  
Bases: [`DiagResult`](#ttRawDiag.diag.DiagResult.DiagResult "ttRawDiag.diag.DiagResult.DiagResult")

Result of a successful WriteDataByLocalIdentifier (0x3B) call, consisting of ID.

GetDataIdentifier()[¶](#tts.tooling.common.genericBusAccess.busHw.diag.kwp2000.WriteDataByLocalIdentifierResult.WriteDataByLocalIdentifierResult.GetDataIdentifier "Link to this definition")  
Returns the data identifier.

Returns:  Data identifier

Return type:  int

DataIdentifier[¶](#tts.tooling.common.genericBusAccess.busHw.diag.kwp2000.WriteDataByLocalIdentifierResult.WriteDataByLocalIdentifierResult.DataIdentifier "Link to this definition")  
Returns the data identifier.

Returns:  Data identifier

Return type:  int

## J1939[¶](#j1939 "Link to this heading")

*class* J1939Message[¶](#tts.testModule.bus.busObjects.J1939.J1939Message "Link to this definition")  
A J1939 message.

priority[¶](#tts.testModule.bus.busObjects.J1939.J1939Message.priority "Link to this definition")  
The priority of the message

Type:  int

pduFormat[¶](#tts.testModule.bus.busObjects.J1939.J1939Message.pduFormat "Link to this definition")  
The PDU format of the message

Type:  int

pduSpecific[¶](#tts.testModule.bus.busObjects.J1939.J1939Message.pduSpecific "Link to this definition")  
The PDU specific part of the message. This could be either the destination address (PDU format \< 0xf0) or the group extension.

Type:  int

sourceAddress[¶](#tts.testModule.bus.busObjects.J1939.J1939Message.sourceAddress "Link to this definition")  
The source address of the message

Type:  int

tla[¶](#tts.testModule.bus.busObjects.J1939.J1939Message.tla "Link to this definition")  
The three letter acronym of the DTC

Type:  str

payload[¶](#tts.testModule.bus.busObjects.J1939.J1939Message.payload "Link to this definition")  
The payload of the message

Type:  ByteStream

timestamp[¶](#tts.testModule.bus.busObjects.J1939.J1939Message.timestamp "Link to this definition")  
Timestamp of the message (only available in the trace analysis). If the message consists of multiple frames, the timestamp of the first incoming message is used.

Type:  float / None

*class* J1939DTCList[¶](#tts.testModule.bus.busObjects.J1939.J1939DTCList "Link to this definition")  
Container for J1939DTCs.

Variables:  
- **TYPE_DM1** – active DTC

- **TYPE_DM2** – previously active DTC

Check(*sourceAddress*, *dtcSet=None*, *conjunction='AND'*, *dtcNotSet=None*, *dtcType=None*)[¶](#tts.testModule.bus.busObjects.J1939.J1939DTCList.Check "Link to this definition")  
Check if a set of DTCs from a specific sender is included.

Examples:

> 1.  Check that there is no DTC on ECU “ABC”
>
> dtcList.Check(“ABC”, conjunction=”ONLY”)
>
> 2.  Check that active DTCs 203.04 and 123.03 are set on ECU “ABC”
>
> dtcList.Check(“ABC”, [“203.04”, “123.03”], “AND”, dtcType=”Active”)

Parameters:  - **sourceAddress** (str / int) – SourceAddress (int), TLA (string) or “ALL” (the source isn’t checked)

- **dtcSet** (list) – List of DTCs which should be included, e.g. [“2001.11”, “2003.14”]

- **conjunction** (str) –

  Possibilities for checking the dtcSet:

  ”AND”: all DTCs from dtcSet must be included, others are allowed

  ”ONLY”: all DTCs from dtcSet must be included, others are forbidden

  ”OR”: at least one DTC from dtcSet must be included, others are allowed

- **dtcNotSet** (list) – List of DTCs which may not be included, e.g. [“2001.11”, “2003.14”]

- **dtcType** (str / None) – DTC-Type (“Active”, “Previously Active”) or None (type is ignored)

Returns:  Expectation fulfilled

Return type:  bool

*class* J1939DTC[¶](#tts.testModule.bus.busObjects.J1939.J1939DTC "Link to this definition")  
A J1939 Diagnostic response.

Variables:  
- **TYPE_DM1** – active DTC

- **TYPE_DM2** – previously active DTC

sourceAddress[¶](#tts.testModule.bus.busObjects.J1939.J1939DTC.sourceAddress "Link to this definition")  
The source address of the DTC

Type:  int

tla[¶](#tts.testModule.bus.busObjects.J1939.J1939DTC.tla "Link to this definition")  
The three letter acronym of the DTC

Type:  str

spn[¶](#tts.testModule.bus.busObjects.J1939.J1939DTC.spn "Link to this definition")  
The suspect parameter number of the DTC

Type:  int

fmi[¶](#tts.testModule.bus.busObjects.J1939.J1939DTC.fmi "Link to this definition")  
The failure mode identifier of the DTC

Type:  int

dtc[¶](#tts.testModule.bus.busObjects.J1939.J1939DTC.dtc "Link to this definition")  
Combination of SPN and FMI (format: \<spn\>.\<fmi\>)

Type:  str

count[¶](#tts.testModule.bus.busObjects.J1939.J1939DTC.count "Link to this definition")  
The occurrence count of the DTC

Type:  int

type[¶](#tts.testModule.bus.busObjects.J1939.J1939DTC.type "Link to this definition")  
The DTC type (TYPE_DM1 “Active” / TYPE_DM2 “Previously Active”)

Type:  str

timestamp[¶](#tts.testModule.bus.busObjects.J1939.J1939DTC.timestamp "Link to this definition")  
Timestamp of the DTC (only available in the trace analysis) If the message consists of multiple frames, the timestamp of the first incoming message is used.

Type:  float / None
