[ Internal APIs ](api.md)

[ Advanced operations of package variable types ](variabledatastructures.md)

[ Advanced properties of bus-related objects ](busdatastructures.md)

[ Bus related objects of trace analysis ](busdatastructuresTraceanalysis.md)

Advanced properties of diagnostics-related objects [ Advanced properties of diagnostics-related objects ](#)

Advanced properties of diagnostics-related objects

- [ UDS result objects ](#uds-result-objects)
  - [C DiagResult ](#ttRawDiag.diag.DiagResult.DiagResult)
    - [M GetResponse ](#ttRawDiag.diag.DiagResult.DiagResult.GetResponse)
    - [M GetErrCode ](#ttRawDiag.diag.DiagResult.DiagResult.GetErrCode)
    - [M GetErrMsg ](#ttRawDiag.diag.DiagResult.DiagResult.GetErrMsg)
    - [M GetResponseTime ](#ttRawDiag.diag.DiagResult.DiagResult.GetResponseTime)
    - [M GetPendingCount ](#ttRawDiag.diag.DiagResult.DiagResult.GetPendingCount)
    - [M GetBusyCount ](#ttRawDiag.diag.DiagResult.DiagResult.GetBusyCount)
    - [M GetTpInfo ](#ttRawDiag.diag.DiagResult.DiagResult.GetTpInfo)
    - [M GetServiceId ](#ttRawDiag.diag.DiagResult.DiagResult.GetServiceId)
  - [ DiagService ](#diagservice)
    - [C DiagServiceResult ](#tts.tooling.common.diagnostic.DiagServiceResult.DiagServiceResult)
      - [M GetDecodedResponse ](#tts.tooling.common.diagnostic.DiagServiceResult.DiagServiceResult.GetDecodedResponse)
  - [ ObdOnUdsService ](#obdonudsservice)
    - [C ObdOnUdsServiceResult ](#tts.tooling.common.diagnostic.DiagServiceResult.ObdOnUdsServiceResult)
      - [M GetDecodedResponse ](#tts.tooling.common.diagnostic.DiagServiceResult.ObdOnUdsServiceResult.GetDecodedResponse)
  - [ Authentication ](#module-tts.tooling.common.diagnostic.uds.authentication.AuthenticationResult)
    - [C AuthenticationConfigurationResult ](#tts.tooling.common.diagnostic.uds.authentication.AuthenticationResult.AuthenticationConfigurationResult)
    - [C AuthenticationDeauthenticateResult ](#tts.tooling.common.diagnostic.uds.authentication.AuthenticationResult.AuthenticationDeauthenticateResult)
    - [C AuthenticationProofOfOwnershipResult ](#tts.tooling.common.diagnostic.uds.authentication.AuthenticationResult.AuthenticationProofOfOwnershipResult)
      - [M GetSessionKeyInfo ](#tts.tooling.common.diagnostic.uds.authentication.AuthenticationResult.AuthenticationProofOfOwnershipResult.GetSessionKeyInfo)
    - [C AuthenticationResult ](#tts.tooling.common.diagnostic.uds.authentication.AuthenticationResult.AuthenticationResult)
      - [A ReturnValue ](#tts.tooling.common.diagnostic.uds.authentication.AuthenticationResult.AuthenticationResult.ReturnValue)
    - [C AuthenticationVerifyCertificateUnidirectionalResult ](#tts.tooling.common.diagnostic.uds.authentication.AuthenticationResult.AuthenticationVerifyCertificateUnidirectionalResult)
      - [M GetChallengeServer ](#tts.tooling.common.diagnostic.uds.authentication.AuthenticationResult.AuthenticationVerifyCertificateUnidirectionalResult.GetChallengeServer)
      - [M GetEphemeralPublicKeyServer ](#tts.tooling.common.diagnostic.uds.authentication.AuthenticationResult.AuthenticationVerifyCertificateUnidirectionalResult.GetEphemeralPublicKeyServer)
  - [ UploadDownloadFunctionalUnit ](#module-tts.tooling.common.diagnostic.uds.uploadDownloadFunctionalUnit.UploadDownloadFunctionalUnitResult)
    - [C RequestDownloadResult ](#tts.tooling.common.diagnostic.uds.uploadDownloadFunctionalUnit.UploadDownloadFunctionalUnitResult.RequestDownloadResult)
      - [M GetLengthFormatIdentifier ](#tts.tooling.common.diagnostic.uds.uploadDownloadFunctionalUnit.UploadDownloadFunctionalUnitResult.RequestDownloadResult.GetLengthFormatIdentifier)
      - [M GetMaxNumberOfBlockLength ](#tts.tooling.common.diagnostic.uds.uploadDownloadFunctionalUnit.UploadDownloadFunctionalUnitResult.RequestDownloadResult.GetMaxNumberOfBlockLength)
      - [M GetMaxNumberOfBlockLengthAsInt ](#tts.tooling.common.diagnostic.uds.uploadDownloadFunctionalUnit.UploadDownloadFunctionalUnitResult.RequestDownloadResult.GetMaxNumberOfBlockLengthAsInt)
      - [M GetNumberOfBlockLengthParameterLength ](#tts.tooling.common.diagnostic.uds.uploadDownloadFunctionalUnit.UploadDownloadFunctionalUnitResult.RequestDownloadResult.GetNumberOfBlockLengthParameterLength)
    - [C TransferDataBlockResult ](#tts.tooling.common.diagnostic.uds.uploadDownloadFunctionalUnit.UploadDownloadFunctionalUnitResult.TransferDataBlockResult)
      - [M GetBlockSequenceCounter ](#tts.tooling.common.diagnostic.uds.uploadDownloadFunctionalUnit.UploadDownloadFunctionalUnitResult.TransferDataBlockResult.GetBlockSequenceCounter)
    - [C TransferDataResult ](#tts.tooling.common.diagnostic.uds.uploadDownloadFunctionalUnit.UploadDownloadFunctionalUnitResult.TransferDataResult)
      - [M GetAllBlockResults ](#tts.tooling.common.diagnostic.uds.uploadDownloadFunctionalUnit.UploadDownloadFunctionalUnitResult.TransferDataResult.GetAllBlockResults)
      - [M GetErrCode ](#tts.tooling.common.diagnostic.uds.uploadDownloadFunctionalUnit.UploadDownloadFunctionalUnitResult.TransferDataResult.GetErrCode)
      - [M GetErrMsg ](#tts.tooling.common.diagnostic.uds.uploadDownloadFunctionalUnit.UploadDownloadFunctionalUnitResult.TransferDataResult.GetErrMsg)
      - [M GetResponse ](#tts.tooling.common.diagnostic.uds.uploadDownloadFunctionalUnit.UploadDownloadFunctionalUnitResult.TransferDataResult.GetResponse)
  - [ DiagnosticSessionControl ](#module-tts.tooling.common.diagnostic.uds.diagnosticSessionControl.DiagnosticSessionControlResult)
    - [C DiagnosticSessionControlResult ](#tts.tooling.common.diagnostic.uds.diagnosticSessionControl.DiagnosticSessionControlResult.DiagnosticSessionControlResult)
      - [M GetP2ServerMax1 ](#tts.tooling.common.diagnostic.uds.diagnosticSessionControl.DiagnosticSessionControlResult.DiagnosticSessionControlResult.GetP2ServerMax1)
      - [M GetP2ServerMax2 ](#tts.tooling.common.diagnostic.uds.diagnosticSessionControl.DiagnosticSessionControlResult.DiagnosticSessionControlResult.GetP2ServerMax2)
      - [M GetSubfunction ](#tts.tooling.common.diagnostic.uds.diagnosticSessionControl.DiagnosticSessionControlResult.DiagnosticSessionControlResult.GetSubfunction)
  - [ ECUReset ](#module-tts.tooling.common.diagnostic.uds.ecuReset.ECUResetResult)
    - [C ECUResetResult ](#tts.tooling.common.diagnostic.uds.ecuReset.ECUResetResult.ECUResetResult)
      - [M GetPowerDownTime ](#tts.tooling.common.diagnostic.uds.ecuReset.ECUResetResult.ECUResetResult.GetPowerDownTime)
  - [ InputOutputControlByIdentifier ](#module-tts.tooling.common.diagnostic.uds.inputOutputControlByIdentifier.InputOutputControlByIdentifierResult)
    - [C InputOutputControlByIdentifierResult ](#tts.tooling.common.diagnostic.uds.inputOutputControlByIdentifier.InputOutputControlByIdentifierResult.InputOutputControlByIdentifierResult)
      - [M GetDataIdentifier ](#tts.tooling.common.diagnostic.uds.inputOutputControlByIdentifier.InputOutputControlByIdentifierResult.InputOutputControlByIdentifierResult.GetDataIdentifier)
      - [M GetIoCtrlParam ](#tts.tooling.common.diagnostic.uds.inputOutputControlByIdentifier.InputOutputControlByIdentifierResult.InputOutputControlByIdentifierResult.GetIoCtrlParam)
      - [M GetData ](#tts.tooling.common.diagnostic.uds.inputOutputControlByIdentifier.InputOutputControlByIdentifierResult.InputOutputControlByIdentifierResult.GetData)
  - [ ReadDataByIdentifier ](#module-tts.tooling.common.diagnostic.uds.readDataByIdentifier.ReadDataByIdentifierResult)
    - [C DataRecordDiagResult ](#tts.tooling.common.diagnostic.uds.readDataByIdentifier.ReadDataByIdentifierResult.DataRecordDiagResult)
      - [M GetDataIdentifier ](#tts.tooling.common.diagnostic.uds.readDataByIdentifier.ReadDataByIdentifierResult.DataRecordDiagResult.GetDataIdentifier)
      - [M GetData ](#tts.tooling.common.diagnostic.uds.readDataByIdentifier.ReadDataByIdentifierResult.DataRecordDiagResult.GetData)
  - [ ReadDTCInformation ](#module-tts.testModule.diag.diagObjects.DTCResult)
    - [C DTCListDiagResult ](#tts.testModule.diag.diagObjects.DTCResult.DTCListDiagResult)
      - [M GetDTCStatusAvailabilityMask ](#tts.testModule.diag.diagObjects.DTCResult.DTCListDiagResult.GetDTCStatusAvailabilityMask)
      - [A DTCStatusAvailabilityMask ](#tts.testModule.diag.diagObjects.DTCResult.DTCListDiagResult.DTCStatusAvailabilityMask)
    - [C DTCNumber ](#tts.testModule.diag.diagObjects.DTCResult.DTCNumber)
      - [M GetNumber ](#tts.testModule.diag.diagObjects.DTCResult.DTCNumber.GetNumber)
      - [M GetShortName ](#tts.testModule.diag.diagObjects.DTCResult.DTCNumber.GetShortName)
      - [M SetShortName ](#tts.testModule.diag.diagObjects.DTCResult.DTCNumber.SetShortName)
      - [M GetShortNumber ](#tts.testModule.diag.diagObjects.DTCResult.DTCNumber.GetShortNumber)
      - [M GetDefinition ](#tts.testModule.diag.diagObjects.DTCResult.DTCNumber.GetDefinition)
      - [M GetShortDefinition ](#tts.testModule.diag.diagObjects.DTCResult.DTCNumber.GetShortDefinition)
      - [M GetFTB ](#tts.testModule.diag.diagObjects.DTCResult.DTCNumber.GetFTB)
      - [M GetDescription ](#tts.testModule.diag.diagObjects.DTCResult.DTCNumber.GetDescription)
      - [M SetDescription ](#tts.testModule.diag.diagObjects.DTCResult.DTCNumber.SetDescription)
    - [C DTCAndStatusRecord ](#tts.testModule.diag.diagObjects.DTCResult.DTCAndStatusRecord)
      - [M GetStatus ](#tts.testModule.diag.diagObjects.DTCResult.DTCAndStatusRecord.GetStatus)
    - [C DTCNumberDiagResult ](#tts.tooling.common.diagnostic.uds.readDtcInformation.ReadDTCInformationResult.DTCNumberDiagResult)
      - [M GetDTCStatusAvailabilityMask ](#tts.tooling.common.diagnostic.uds.readDtcInformation.ReadDTCInformationResult.DTCNumberDiagResult.GetDTCStatusAvailabilityMask)
      - [M GetDTCFormatIdentifier ](#tts.tooling.common.diagnostic.uds.readDtcInformation.ReadDTCInformationResult.DTCNumberDiagResult.GetDTCFormatIdentifier)
      - [M GetDTCCount ](#tts.tooling.common.diagnostic.uds.readDtcInformation.ReadDTCInformationResult.DTCNumberDiagResult.GetDTCCount)
    - [C DTCSnapshotIdentification ](#tts.tooling.common.diagnostic.uds.readDtcInformation.ReadDTCInformationResult.DTCSnapshotIdentification)
      - [M GetDTC ](#tts.tooling.common.diagnostic.uds.readDtcInformation.ReadDTCInformationResult.DTCSnapshotIdentification.GetDTC)
      - [M GetSnapshotNumber ](#tts.tooling.common.diagnostic.uds.readDtcInformation.ReadDTCInformationResult.DTCSnapshotIdentification.GetSnapshotNumber)
    - [C DTCSnapshotIdentificationDiagResult ](#tts.tooling.common.diagnostic.uds.readDtcInformation.ReadDTCInformationResult.DTCSnapshotIdentificationDiagResult)
      - [M GetDTCSnapshotList ](#tts.tooling.common.diagnostic.uds.readDtcInformation.ReadDTCInformationResult.DTCSnapshotIdentificationDiagResult.GetDTCSnapshotList)
    - [C DTCSnapshotRecordDiagResult ](#tts.tooling.common.diagnostic.uds.readDtcInformation.ReadDTCInformationResult.DTCSnapshotRecordDiagResult)
      - [M GetDTCAndStatusRecord ](#tts.tooling.common.diagnostic.uds.readDtcInformation.ReadDTCInformationResult.DTCSnapshotRecordDiagResult.GetDTCAndStatusRecord)
      - [M GetDTCSnapshotData ](#tts.tooling.common.diagnostic.uds.readDtcInformation.ReadDTCInformationResult.DTCSnapshotRecordDiagResult.GetDTCSnapshotData)
      - [M GetDTCSnapshotDataRaw ](#tts.tooling.common.diagnostic.uds.readDtcInformation.ReadDTCInformationResult.DTCSnapshotRecordDiagResult.GetDTCSnapshotDataRaw)
    - [C DTCSnapshotDataEntry ](#tts.tooling.common.diagnostic.uds.readDtcInformation.ReadDTCInformationResult.DTCSnapshotDataEntry)
      - [M GetDTCSnapshotRecordNumber ](#tts.tooling.common.diagnostic.uds.readDtcInformation.ReadDTCInformationResult.DTCSnapshotDataEntry.GetDTCSnapshotRecordNumber)
      - [M GetDTCSnapshotRecordNumberOfIdentifiers ](#tts.tooling.common.diagnostic.uds.readDtcInformation.ReadDTCInformationResult.DTCSnapshotDataEntry.GetDTCSnapshotRecordNumberOfIdentifiers)
      - [M GetDTCSnapshotRecord ](#tts.tooling.common.diagnostic.uds.readDtcInformation.ReadDTCInformationResult.DTCSnapshotDataEntry.GetDTCSnapshotRecord)
    - [C DTCSnapshotRecordEntry ](#tts.tooling.common.diagnostic.uds.readDtcInformation.ReadDTCInformationResult.DTCSnapshotRecordEntry)
      - [M GetDID ](#tts.tooling.common.diagnostic.uds.readDtcInformation.ReadDTCInformationResult.DTCSnapshotRecordEntry.GetDID)
      - [M GetValue ](#tts.tooling.common.diagnostic.uds.readDtcInformation.ReadDTCInformationResult.DTCSnapshotRecordEntry.GetValue)
    - [C DTCFaultCounter ](#tts.tooling.common.diagnostic.uds.readDtcInformation.ReadDTCInformationResult.DTCFaultCounter)
      - [M GetDTC ](#tts.tooling.common.diagnostic.uds.readDtcInformation.ReadDTCInformationResult.DTCFaultCounter.GetDTC)
      - [M GetFaultCounter ](#tts.tooling.common.diagnostic.uds.readDtcInformation.ReadDTCInformationResult.DTCFaultCounter.GetFaultCounter)
    - [C DTCFaultCounterDiagResult ](#tts.tooling.common.diagnostic.uds.readDtcInformation.ReadDTCInformationResult.DTCFaultCounterDiagResult)
      - [M GetDTCFaultList ](#tts.tooling.common.diagnostic.uds.readDtcInformation.ReadDTCInformationResult.DTCFaultCounterDiagResult.GetDTCFaultList)
    - [C UserDTCListDiagResult ](#tts.tooling.common.diagnostic.uds.readDtcInformation.ReadDTCInformationResult.UserDTCListDiagResult)
      - [M GetDTCMemorySelection ](#tts.tooling.common.diagnostic.uds.readDtcInformation.ReadDTCInformationResult.UserDTCListDiagResult.GetDTCMemorySelection)
      - [A DTCMemorySelection ](#tts.tooling.common.diagnostic.uds.readDtcInformation.ReadDTCInformationResult.UserDTCListDiagResult.DTCMemorySelection)
  - [ ReadMemoryByAddress ](#module-tts.tooling.common.diagnostic.uds.readMemoryByAddress.ReadMemoryByAddressResult)
    - [C MemoryDiagResult ](#tts.tooling.common.diagnostic.uds.readMemoryByAddress.ReadMemoryByAddressResult.MemoryDiagResult)
      - [M GetDataRecord ](#tts.tooling.common.diagnostic.uds.readMemoryByAddress.ReadMemoryByAddressResult.MemoryDiagResult.GetDataRecord)
  - [ RoutineControl ](#module-tts.tooling.common.diagnostic.uds.routineControl.RoutineControlResult)
    - [C RoutineDiagResult ](#tts.tooling.common.diagnostic.uds.routineControl.RoutineControlResult.RoutineDiagResult)
      - [M GetRoutineControlType ](#tts.tooling.common.diagnostic.uds.routineControl.RoutineControlResult.RoutineDiagResult.GetRoutineControlType)
      - [M GetRoutineId ](#tts.tooling.common.diagnostic.uds.routineControl.RoutineControlResult.RoutineDiagResult.GetRoutineId)
      - [M GetRoutineInfo ](#tts.tooling.common.diagnostic.uds.routineControl.RoutineControlResult.RoutineDiagResult.GetRoutineInfo)
      - [M GetStatusRecord ](#tts.tooling.common.diagnostic.uds.routineControl.RoutineControlResult.RoutineDiagResult.GetStatusRecord)
  - [ SecurityAccess ](#module-tts.tooling.common.diagnostic.commonJobs.securityAccess.SecurityAccessResult)
    - [C SecurityAccessDiagResult ](#tts.tooling.common.diagnostic.commonJobs.securityAccess.SecurityAccessResult.SecurityAccessDiagResult)
      - [M GetSecuritySeed ](#tts.tooling.common.diagnostic.commonJobs.securityAccess.SecurityAccessResult.SecurityAccessDiagResult.GetSecuritySeed)
      - [M GetGeneratedKey ](#tts.tooling.common.diagnostic.commonJobs.securityAccess.SecurityAccessResult.SecurityAccessDiagResult.GetGeneratedKey)
    - [C SecuritySeedDiagResult ](#tts.tooling.common.diagnostic.commonJobs.securityAccess.SecurityAccessResult.SecuritySeedDiagResult)
      - [M GetSecuritySeed ](#tts.tooling.common.diagnostic.commonJobs.securityAccess.SecurityAccessResult.SecuritySeedDiagResult.GetSecuritySeed)
    - [C SecurityAccessSuccessDiagResult ](#tts.tooling.common.diagnostic.commonJobs.securityAccess.SecurityAccessResult.SecurityAccessSuccessDiagResult)
      - [M IsAccessGranted ](#tts.tooling.common.diagnostic.commonJobs.securityAccess.SecurityAccessResult.SecurityAccessSuccessDiagResult.IsAccessGranted)
  - [ WriteDataByIdentifier ](#module-tts.tooling.common.diagnostic.uds.writeDataByIdentifier.WriteDataByIdentifierResult)
    - [C WriteDataByIdentifierResult ](#tts.tooling.common.diagnostic.uds.writeDataByIdentifier.WriteDataByIdentifierResult.WriteDataByIdentifierResult)
      - [M GetDataIdentifier ](#tts.tooling.common.diagnostic.uds.writeDataByIdentifier.WriteDataByIdentifierResult.WriteDataByIdentifierResult.GetDataIdentifier)
  - [ WriteMemoryByAddress ](#module-tts.tooling.common.diagnostic.uds.writeMemoryByAddress.WriteMemoryByAddressResult)
    - [C WriteMemoryByAddressResult ](#tts.tooling.common.diagnostic.uds.writeMemoryByAddress.WriteMemoryByAddressResult.WriteMemoryByAddressResult)
      - [M GetMemoryAddress ](#tts.tooling.common.diagnostic.uds.writeMemoryByAddress.WriteMemoryByAddressResult.WriteMemoryByAddressResult.GetMemoryAddress)
      - [M GetMemorySize ](#tts.tooling.common.diagnostic.uds.writeMemoryByAddress.WriteMemoryByAddressResult.WriteMemoryByAddressResult.GetMemorySize)
  - [ NegativeResponse ](#module-tts.tooling.common.diagnostic.NegativeResponse)
    - [C NegativeResponse ](#tts.tooling.common.diagnostic.NegativeResponse.NegativeResponse)
      - [M GetUDSErrMsg ](#tts.tooling.common.diagnostic.NegativeResponse.NegativeResponse.GetUDSErrMsg)
    - [C UndefinedResponse ](#tts.tooling.common.diagnostic.NegativeResponse.UndefinedResponse)
- [ KWP2000 result objects ](#kwp2000-result-objects)
  - [ ClearDTC ](#module-tts.tooling.common.diagnostic.kwp2000.clearDtc.ClearDTCResult)
    - [C ClearDTCResult ](#tts.tooling.common.diagnostic.kwp2000.clearDtc.ClearDTCResult.ClearDTCResult)
      - [M GetGroupOfDTCs ](#tts.tooling.common.diagnostic.kwp2000.clearDtc.ClearDTCResult.ClearDTCResult.GetGroupOfDTCs)
  - [ ECUReset ](#diagapikwp2000ecureset)
    - [C ECUResetResult ](#tts.tooling.common.diagnostic.kwp2000.ecuReset.ECUResetResult.ECUResetResult)
      - [M GetResetStatus ](#tts.tooling.common.diagnostic.kwp2000.ecuReset.ECUResetResult.ECUResetResult.GetResetStatus)
  - [ InputOutputControlByCommonIdentifier ](#module-tts.tooling.common.diagnostic.kwp2000.inputOutputControlByCommonIdentifier.InputOutputControlByCommonIdentifierResult)
    - [C InputOutputControlByCommonIdentifierResult ](#tts.tooling.common.diagnostic.kwp2000.inputOutputControlByCommonIdentifier.InputOutputControlByCommonIdentifierResult.InputOutputControlByCommonIdentifierResult)
      - [M GetDataIdentifierHighByte ](#tts.tooling.common.diagnostic.kwp2000.inputOutputControlByCommonIdentifier.InputOutputControlByCommonIdentifierResult.InputOutputControlByCommonIdentifierResult.GetDataIdentifierHighByte)
      - [M GetDataIdentifierLowByte ](#tts.tooling.common.diagnostic.kwp2000.inputOutputControlByCommonIdentifier.InputOutputControlByCommonIdentifierResult.InputOutputControlByCommonIdentifierResult.GetDataIdentifierLowByte)
      - [M GetControlStatus ](#tts.tooling.common.diagnostic.kwp2000.inputOutputControlByCommonIdentifier.InputOutputControlByCommonIdentifierResult.InputOutputControlByCommonIdentifierResult.GetControlStatus)
  - [ InputOutputControlByLocalIdentifier ](#module-tts.tooling.common.diagnostic.kwp2000.inputOutputControlByLocalIdentifier.InputOutputControlByLocalIdentifierResult)
    - [C InputOutputControlByLocalIdentifierResult ](#tts.tooling.common.diagnostic.kwp2000.inputOutputControlByLocalIdentifier.InputOutputControlByLocalIdentifierResult.InputOutputControlByLocalIdentifierResult)
      - [M GetDataIdentifier ](#tts.tooling.common.diagnostic.kwp2000.inputOutputControlByLocalIdentifier.InputOutputControlByLocalIdentifierResult.InputOutputControlByLocalIdentifierResult.GetDataIdentifier)
      - [M GetControlStatus ](#tts.tooling.common.diagnostic.kwp2000.inputOutputControlByLocalIdentifier.InputOutputControlByLocalIdentifierResult.InputOutputControlByLocalIdentifierResult.GetControlStatus)
  - [ ReadDataByCommonIdentifier ](#module-tts.tooling.common.diagnostic.kwp2000.readDataByCommonIdentifier.ReadDataByCommonIdentifierResult)
    - [C ReadDataByCommonIdentifierResult ](#tts.tooling.common.diagnostic.kwp2000.readDataByCommonIdentifier.ReadDataByCommonIdentifierResult.ReadDataByCommonIdentifierResult)
      - [M GetDataIdentifierHighByte ](#tts.tooling.common.diagnostic.kwp2000.readDataByCommonIdentifier.ReadDataByCommonIdentifierResult.ReadDataByCommonIdentifierResult.GetDataIdentifierHighByte)
      - [M GetDataIdentifierLowByte ](#tts.tooling.common.diagnostic.kwp2000.readDataByCommonIdentifier.ReadDataByCommonIdentifierResult.ReadDataByCommonIdentifierResult.GetDataIdentifierLowByte)
      - [M GetData ](#tts.tooling.common.diagnostic.kwp2000.readDataByCommonIdentifier.ReadDataByCommonIdentifierResult.ReadDataByCommonIdentifierResult.GetData)
  - [ ReadDataByLocalIdentifier ](#module-tts.tooling.common.diagnostic.kwp2000.readDataByLocalIdentifier.ReadDataByLocalIdentifierResult)
    - [C ReadDataByLocalIdentifierResult ](#tts.tooling.common.diagnostic.kwp2000.readDataByLocalIdentifier.ReadDataByLocalIdentifierResult.ReadDataByLocalIdentifierResult)
      - [M GetDataIdentifier ](#tts.tooling.common.diagnostic.kwp2000.readDataByLocalIdentifier.ReadDataByLocalIdentifierResult.ReadDataByLocalIdentifierResult.GetDataIdentifier)
      - [M GetData ](#tts.tooling.common.diagnostic.kwp2000.readDataByLocalIdentifier.ReadDataByLocalIdentifierResult.ReadDataByLocalIdentifierResult.GetData)
  - [ ReadDTCInformation ](#diagapikwp2000readdtcinformation)
    - [C ReadDiagnosticTroubleCodesDiagResult ](#tts.tooling.common.diagnostic.kwp2000.readDtcInformation.ReadDTCInformationResult.ReadDiagnosticTroubleCodesDiagResult)
      - [M GetDTCCount ](#tts.tooling.common.diagnostic.kwp2000.readDtcInformation.ReadDTCInformationResult.ReadDiagnosticTroubleCodesDiagResult.GetDTCCount)
      - [M GetDTCFaultList ](#tts.tooling.common.diagnostic.kwp2000.readDtcInformation.ReadDTCInformationResult.ReadDiagnosticTroubleCodesDiagResult.GetDTCFaultList)
    - [C ReadDiagnosticTroubleCodesAndStatusDiagResult ](#tts.tooling.common.diagnostic.kwp2000.readDtcInformation.ReadDTCInformationResult.ReadDiagnosticTroubleCodesAndStatusDiagResult)
      - [M GetDTCCount ](#tts.tooling.common.diagnostic.kwp2000.readDtcInformation.ReadDTCInformationResult.ReadDiagnosticTroubleCodesAndStatusDiagResult.GetDTCCount)
      - [M GetDTCFaultList ](#tts.tooling.common.diagnostic.kwp2000.readDtcInformation.ReadDTCInformationResult.ReadDiagnosticTroubleCodesAndStatusDiagResult.GetDTCFaultList)
  - [ ReadECUIdentification ](#module-tts.tooling.common.diagnostic.kwp2000.readEcuIdentification.ReadECUIdentificationResult)
    - [C ReadECUIdentificationResult ](#tts.tooling.common.diagnostic.kwp2000.readEcuIdentification.ReadECUIdentificationResult.ReadECUIdentificationResult)
      - [M GetDataIdentifier ](#tts.tooling.common.diagnostic.kwp2000.readEcuIdentification.ReadECUIdentificationResult.ReadECUIdentificationResult.GetDataIdentifier)
      - [M GetData ](#tts.tooling.common.diagnostic.kwp2000.readEcuIdentification.ReadECUIdentificationResult.ReadECUIdentificationResult.GetData)
  - [ RoutineControl ](#diagapikwp2000routinecontrol)
    - [C RoutineByLocalIdentifierDiagResult ](#tts.tooling.common.diagnostic.kwp2000.routineControl.RoutineControlResult.RoutineByLocalIdentifierDiagResult)
      - [M GetRoutineId ](#tts.tooling.common.diagnostic.kwp2000.routineControl.RoutineControlResult.RoutineByLocalIdentifierDiagResult.GetRoutineId)
      - [M GetStatusRecord ](#tts.tooling.common.diagnostic.kwp2000.routineControl.RoutineControlResult.RoutineByLocalIdentifierDiagResult.GetStatusRecord)
    - [C StartRoutineByLocalIdentifierDiagResult ](#tts.tooling.common.diagnostic.kwp2000.routineControl.RoutineControlResult.StartRoutineByLocalIdentifierDiagResult)
      - [M GetEntryStatus ](#tts.tooling.common.diagnostic.kwp2000.routineControl.RoutineControlResult.StartRoutineByLocalIdentifierDiagResult.GetEntryStatus)
    - [C StopRoutineByLocalIdentifierDiagResult ](#tts.tooling.common.diagnostic.kwp2000.routineControl.RoutineControlResult.StopRoutineByLocalIdentifierDiagResult)
      - [M GetExitStatus ](#tts.tooling.common.diagnostic.kwp2000.routineControl.RoutineControlResult.StopRoutineByLocalIdentifierDiagResult.GetExitStatus)
    - [C RequestRoutineByLocalIdentifierDiagResult ](#tts.tooling.common.diagnostic.kwp2000.routineControl.RoutineControlResult.RequestRoutineByLocalIdentifierDiagResult)
      - [M GetRoutineResults ](#tts.tooling.common.diagnostic.kwp2000.routineControl.RoutineControlResult.RequestRoutineByLocalIdentifierDiagResult.GetRoutineResults)
  - [ WriteDataByCommonIdentifier ](#module-tts.tooling.common.diagnostic.kwp2000.writeDataByCommonIdentifier.WriteDataByCommonIdentifierResult)
    - [C WriteDataByCommonIdentifierResult ](#tts.tooling.common.diagnostic.kwp2000.writeDataByCommonIdentifier.WriteDataByCommonIdentifierResult.WriteDataByCommonIdentifierResult)
      - [M GetDataIdentifierHighByte ](#tts.tooling.common.diagnostic.kwp2000.writeDataByCommonIdentifier.WriteDataByCommonIdentifierResult.WriteDataByCommonIdentifierResult.GetDataIdentifierHighByte)
      - [M GetDataIdentifierLowByte ](#tts.tooling.common.diagnostic.kwp2000.writeDataByCommonIdentifier.WriteDataByCommonIdentifierResult.WriteDataByCommonIdentifierResult.GetDataIdentifierLowByte)
  - [ WriteDataByLocalIdentifier ](#module-tts.tooling.common.diagnostic.kwp2000.writeDataByLocalIdentifier.WriteDataByLocalIdentifierResult)
    - [C WriteDataByLocalIdentifierResult ](#tts.tooling.common.diagnostic.kwp2000.writeDataByLocalIdentifier.WriteDataByLocalIdentifierResult.WriteDataByLocalIdentifierResult)
      - [M GetDataIdentifier ](#tts.tooling.common.diagnostic.kwp2000.writeDataByLocalIdentifier.WriteDataByLocalIdentifierResult.WriteDataByLocalIdentifierResult.GetDataIdentifier)
- [ J1939 ](#j1939)
  - [C J1939Message ](#tts.testModule.bus.busObjects.J1939.J1939Message)
    - [A priority ](#tts.testModule.bus.busObjects.J1939.J1939Message.priority)
    - [A pduFormat ](#tts.testModule.bus.busObjects.J1939.J1939Message.pduFormat)
    - [A pduSpecific ](#tts.testModule.bus.busObjects.J1939.J1939Message.pduSpecific)
    - [A sourceAddress ](#tts.testModule.bus.busObjects.J1939.J1939Message.sourceAddress)
    - [A tla ](#tts.testModule.bus.busObjects.J1939.J1939Message.tla)
    - [A payload ](#tts.testModule.bus.busObjects.J1939.J1939Message.payload)
    - [A timestamp ](#tts.testModule.bus.busObjects.J1939.J1939Message.timestamp)
  - [C J1939DTCList ](#tts.testModule.bus.busObjects.J1939.J1939DTCList)
    - [M Check ](#tts.testModule.bus.busObjects.J1939.J1939DTCList.Check)
  - [C J1939DTC ](#tts.testModule.bus.busObjects.J1939.J1939DTC)
    - [A sourceAddress ](#tts.testModule.bus.busObjects.J1939.J1939DTC.sourceAddress)
    - [A tla ](#tts.testModule.bus.busObjects.J1939.J1939DTC.tla)
    - [A spn ](#tts.testModule.bus.busObjects.J1939.J1939DTC.spn)
    - [A fmi ](#tts.testModule.bus.busObjects.J1939.J1939DTC.fmi)
    - [A dtc ](#tts.testModule.bus.busObjects.J1939.J1939DTC.dtc)
    - [A count ](#tts.testModule.bus.busObjects.J1939.J1939DTC.count)
    - [A type ](#tts.testModule.bus.busObjects.J1939.J1939DTC.type)
    - [A timestamp ](#tts.testModule.bus.busObjects.J1939.J1939DTC.timestamp)

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

Advanced properties of diagnostics-related objects

- [ UDS result objects ](#uds-result-objects)
  - [C DiagResult ](#ttRawDiag.diag.DiagResult.DiagResult)
    - [M GetResponse ](#ttRawDiag.diag.DiagResult.DiagResult.GetResponse)
    - [M GetErrCode ](#ttRawDiag.diag.DiagResult.DiagResult.GetErrCode)
    - [M GetErrMsg ](#ttRawDiag.diag.DiagResult.DiagResult.GetErrMsg)
    - [M GetResponseTime ](#ttRawDiag.diag.DiagResult.DiagResult.GetResponseTime)
    - [M GetPendingCount ](#ttRawDiag.diag.DiagResult.DiagResult.GetPendingCount)
    - [M GetBusyCount ](#ttRawDiag.diag.DiagResult.DiagResult.GetBusyCount)
    - [M GetTpInfo ](#ttRawDiag.diag.DiagResult.DiagResult.GetTpInfo)
    - [M GetServiceId ](#ttRawDiag.diag.DiagResult.DiagResult.GetServiceId)
  - [ DiagService ](#diagservice)
    - [C DiagServiceResult ](#tts.tooling.common.diagnostic.DiagServiceResult.DiagServiceResult)
      - [M GetDecodedResponse ](#tts.tooling.common.diagnostic.DiagServiceResult.DiagServiceResult.GetDecodedResponse)
  - [ ObdOnUdsService ](#obdonudsservice)
    - [C ObdOnUdsServiceResult ](#tts.tooling.common.diagnostic.DiagServiceResult.ObdOnUdsServiceResult)
      - [M GetDecodedResponse ](#tts.tooling.common.diagnostic.DiagServiceResult.ObdOnUdsServiceResult.GetDecodedResponse)
  - [ Authentication ](#module-tts.tooling.common.diagnostic.uds.authentication.AuthenticationResult)
    - [C AuthenticationConfigurationResult ](#tts.tooling.common.diagnostic.uds.authentication.AuthenticationResult.AuthenticationConfigurationResult)
    - [C AuthenticationDeauthenticateResult ](#tts.tooling.common.diagnostic.uds.authentication.AuthenticationResult.AuthenticationDeauthenticateResult)
    - [C AuthenticationProofOfOwnershipResult ](#tts.tooling.common.diagnostic.uds.authentication.AuthenticationResult.AuthenticationProofOfOwnershipResult)
      - [M GetSessionKeyInfo ](#tts.tooling.common.diagnostic.uds.authentication.AuthenticationResult.AuthenticationProofOfOwnershipResult.GetSessionKeyInfo)
    - [C AuthenticationResult ](#tts.tooling.common.diagnostic.uds.authentication.AuthenticationResult.AuthenticationResult)
      - [A ReturnValue ](#tts.tooling.common.diagnostic.uds.authentication.AuthenticationResult.AuthenticationResult.ReturnValue)
    - [C AuthenticationVerifyCertificateUnidirectionalResult ](#tts.tooling.common.diagnostic.uds.authentication.AuthenticationResult.AuthenticationVerifyCertificateUnidirectionalResult)
      - [M GetChallengeServer ](#tts.tooling.common.diagnostic.uds.authentication.AuthenticationResult.AuthenticationVerifyCertificateUnidirectionalResult.GetChallengeServer)
      - [M GetEphemeralPublicKeyServer ](#tts.tooling.common.diagnostic.uds.authentication.AuthenticationResult.AuthenticationVerifyCertificateUnidirectionalResult.GetEphemeralPublicKeyServer)
  - [ UploadDownloadFunctionalUnit ](#module-tts.tooling.common.diagnostic.uds.uploadDownloadFunctionalUnit.UploadDownloadFunctionalUnitResult)
    - [C RequestDownloadResult ](#tts.tooling.common.diagnostic.uds.uploadDownloadFunctionalUnit.UploadDownloadFunctionalUnitResult.RequestDownloadResult)
      - [M GetLengthFormatIdentifier ](#tts.tooling.common.diagnostic.uds.uploadDownloadFunctionalUnit.UploadDownloadFunctionalUnitResult.RequestDownloadResult.GetLengthFormatIdentifier)
      - [M GetMaxNumberOfBlockLength ](#tts.tooling.common.diagnostic.uds.uploadDownloadFunctionalUnit.UploadDownloadFunctionalUnitResult.RequestDownloadResult.GetMaxNumberOfBlockLength)
      - [M GetMaxNumberOfBlockLengthAsInt ](#tts.tooling.common.diagnostic.uds.uploadDownloadFunctionalUnit.UploadDownloadFunctionalUnitResult.RequestDownloadResult.GetMaxNumberOfBlockLengthAsInt)
      - [M GetNumberOfBlockLengthParameterLength ](#tts.tooling.common.diagnostic.uds.uploadDownloadFunctionalUnit.UploadDownloadFunctionalUnitResult.RequestDownloadResult.GetNumberOfBlockLengthParameterLength)
    - [C TransferDataBlockResult ](#tts.tooling.common.diagnostic.uds.uploadDownloadFunctionalUnit.UploadDownloadFunctionalUnitResult.TransferDataBlockResult)
      - [M GetBlockSequenceCounter ](#tts.tooling.common.diagnostic.uds.uploadDownloadFunctionalUnit.UploadDownloadFunctionalUnitResult.TransferDataBlockResult.GetBlockSequenceCounter)
    - [C TransferDataResult ](#tts.tooling.common.diagnostic.uds.uploadDownloadFunctionalUnit.UploadDownloadFunctionalUnitResult.TransferDataResult)
      - [M GetAllBlockResults ](#tts.tooling.common.diagnostic.uds.uploadDownloadFunctionalUnit.UploadDownloadFunctionalUnitResult.TransferDataResult.GetAllBlockResults)
      - [M GetErrCode ](#tts.tooling.common.diagnostic.uds.uploadDownloadFunctionalUnit.UploadDownloadFunctionalUnitResult.TransferDataResult.GetErrCode)
      - [M GetErrMsg ](#tts.tooling.common.diagnostic.uds.uploadDownloadFunctionalUnit.UploadDownloadFunctionalUnitResult.TransferDataResult.GetErrMsg)
      - [M GetResponse ](#tts.tooling.common.diagnostic.uds.uploadDownloadFunctionalUnit.UploadDownloadFunctionalUnitResult.TransferDataResult.GetResponse)
  - [ DiagnosticSessionControl ](#module-tts.tooling.common.diagnostic.uds.diagnosticSessionControl.DiagnosticSessionControlResult)
    - [C DiagnosticSessionControlResult ](#tts.tooling.common.diagnostic.uds.diagnosticSessionControl.DiagnosticSessionControlResult.DiagnosticSessionControlResult)
      - [M GetP2ServerMax1 ](#tts.tooling.common.diagnostic.uds.diagnosticSessionControl.DiagnosticSessionControlResult.DiagnosticSessionControlResult.GetP2ServerMax1)
      - [M GetP2ServerMax2 ](#tts.tooling.common.diagnostic.uds.diagnosticSessionControl.DiagnosticSessionControlResult.DiagnosticSessionControlResult.GetP2ServerMax2)
      - [M GetSubfunction ](#tts.tooling.common.diagnostic.uds.diagnosticSessionControl.DiagnosticSessionControlResult.DiagnosticSessionControlResult.GetSubfunction)
  - [ ECUReset ](#module-tts.tooling.common.diagnostic.uds.ecuReset.ECUResetResult)
    - [C ECUResetResult ](#tts.tooling.common.diagnostic.uds.ecuReset.ECUResetResult.ECUResetResult)
      - [M GetPowerDownTime ](#tts.tooling.common.diagnostic.uds.ecuReset.ECUResetResult.ECUResetResult.GetPowerDownTime)
  - [ InputOutputControlByIdentifier ](#module-tts.tooling.common.diagnostic.uds.inputOutputControlByIdentifier.InputOutputControlByIdentifierResult)
    - [C InputOutputControlByIdentifierResult ](#tts.tooling.common.diagnostic.uds.inputOutputControlByIdentifier.InputOutputControlByIdentifierResult.InputOutputControlByIdentifierResult)
      - [M GetDataIdentifier ](#tts.tooling.common.diagnostic.uds.inputOutputControlByIdentifier.InputOutputControlByIdentifierResult.InputOutputControlByIdentifierResult.GetDataIdentifier)
      - [M GetIoCtrlParam ](#tts.tooling.common.diagnostic.uds.inputOutputControlByIdentifier.InputOutputControlByIdentifierResult.InputOutputControlByIdentifierResult.GetIoCtrlParam)
      - [M GetData ](#tts.tooling.common.diagnostic.uds.inputOutputControlByIdentifier.InputOutputControlByIdentifierResult.InputOutputControlByIdentifierResult.GetData)
  - [ ReadDataByIdentifier ](#module-tts.tooling.common.diagnostic.uds.readDataByIdentifier.ReadDataByIdentifierResult)
    - [C DataRecordDiagResult ](#tts.tooling.common.diagnostic.uds.readDataByIdentifier.ReadDataByIdentifierResult.DataRecordDiagResult)
      - [M GetDataIdentifier ](#tts.tooling.common.diagnostic.uds.readDataByIdentifier.ReadDataByIdentifierResult.DataRecordDiagResult.GetDataIdentifier)
      - [M GetData ](#tts.tooling.common.diagnostic.uds.readDataByIdentifier.ReadDataByIdentifierResult.DataRecordDiagResult.GetData)
  - [ ReadDTCInformation ](#module-tts.testModule.diag.diagObjects.DTCResult)
    - [C DTCListDiagResult ](#tts.testModule.diag.diagObjects.DTCResult.DTCListDiagResult)
      - [M GetDTCStatusAvailabilityMask ](#tts.testModule.diag.diagObjects.DTCResult.DTCListDiagResult.GetDTCStatusAvailabilityMask)
      - [A DTCStatusAvailabilityMask ](#tts.testModule.diag.diagObjects.DTCResult.DTCListDiagResult.DTCStatusAvailabilityMask)
    - [C DTCNumber ](#tts.testModule.diag.diagObjects.DTCResult.DTCNumber)
      - [M GetNumber ](#tts.testModule.diag.diagObjects.DTCResult.DTCNumber.GetNumber)
      - [M GetShortName ](#tts.testModule.diag.diagObjects.DTCResult.DTCNumber.GetShortName)
      - [M SetShortName ](#tts.testModule.diag.diagObjects.DTCResult.DTCNumber.SetShortName)
      - [M GetShortNumber ](#tts.testModule.diag.diagObjects.DTCResult.DTCNumber.GetShortNumber)
      - [M GetDefinition ](#tts.testModule.diag.diagObjects.DTCResult.DTCNumber.GetDefinition)
      - [M GetShortDefinition ](#tts.testModule.diag.diagObjects.DTCResult.DTCNumber.GetShortDefinition)
      - [M GetFTB ](#tts.testModule.diag.diagObjects.DTCResult.DTCNumber.GetFTB)
      - [M GetDescription ](#tts.testModule.diag.diagObjects.DTCResult.DTCNumber.GetDescription)
      - [M SetDescription ](#tts.testModule.diag.diagObjects.DTCResult.DTCNumber.SetDescription)
    - [C DTCAndStatusRecord ](#tts.testModule.diag.diagObjects.DTCResult.DTCAndStatusRecord)
      - [M GetStatus ](#tts.testModule.diag.diagObjects.DTCResult.DTCAndStatusRecord.GetStatus)
    - [C DTCNumberDiagResult ](#tts.tooling.common.diagnostic.uds.readDtcInformation.ReadDTCInformationResult.DTCNumberDiagResult)
      - [M GetDTCStatusAvailabilityMask ](#tts.tooling.common.diagnostic.uds.readDtcInformation.ReadDTCInformationResult.DTCNumberDiagResult.GetDTCStatusAvailabilityMask)
      - [M GetDTCFormatIdentifier ](#tts.tooling.common.diagnostic.uds.readDtcInformation.ReadDTCInformationResult.DTCNumberDiagResult.GetDTCFormatIdentifier)
      - [M GetDTCCount ](#tts.tooling.common.diagnostic.uds.readDtcInformation.ReadDTCInformationResult.DTCNumberDiagResult.GetDTCCount)
    - [C DTCSnapshotIdentification ](#tts.tooling.common.diagnostic.uds.readDtcInformation.ReadDTCInformationResult.DTCSnapshotIdentification)
      - [M GetDTC ](#tts.tooling.common.diagnostic.uds.readDtcInformation.ReadDTCInformationResult.DTCSnapshotIdentification.GetDTC)
      - [M GetSnapshotNumber ](#tts.tooling.common.diagnostic.uds.readDtcInformation.ReadDTCInformationResult.DTCSnapshotIdentification.GetSnapshotNumber)
    - [C DTCSnapshotIdentificationDiagResult ](#tts.tooling.common.diagnostic.uds.readDtcInformation.ReadDTCInformationResult.DTCSnapshotIdentificationDiagResult)
      - [M GetDTCSnapshotList ](#tts.tooling.common.diagnostic.uds.readDtcInformation.ReadDTCInformationResult.DTCSnapshotIdentificationDiagResult.GetDTCSnapshotList)
    - [C DTCSnapshotRecordDiagResult ](#tts.tooling.common.diagnostic.uds.readDtcInformation.ReadDTCInformationResult.DTCSnapshotRecordDiagResult)
      - [M GetDTCAndStatusRecord ](#tts.tooling.common.diagnostic.uds.readDtcInformation.ReadDTCInformationResult.DTCSnapshotRecordDiagResult.GetDTCAndStatusRecord)
      - [M GetDTCSnapshotData ](#tts.tooling.common.diagnostic.uds.readDtcInformation.ReadDTCInformationResult.DTCSnapshotRecordDiagResult.GetDTCSnapshotData)
      - [M GetDTCSnapshotDataRaw ](#tts.tooling.common.diagnostic.uds.readDtcInformation.ReadDTCInformationResult.DTCSnapshotRecordDiagResult.GetDTCSnapshotDataRaw)
    - [C DTCSnapshotDataEntry ](#tts.tooling.common.diagnostic.uds.readDtcInformation.ReadDTCInformationResult.DTCSnapshotDataEntry)
      - [M GetDTCSnapshotRecordNumber ](#tts.tooling.common.diagnostic.uds.readDtcInformation.ReadDTCInformationResult.DTCSnapshotDataEntry.GetDTCSnapshotRecordNumber)
      - [M GetDTCSnapshotRecordNumberOfIdentifiers ](#tts.tooling.common.diagnostic.uds.readDtcInformation.ReadDTCInformationResult.DTCSnapshotDataEntry.GetDTCSnapshotRecordNumberOfIdentifiers)
      - [M GetDTCSnapshotRecord ](#tts.tooling.common.diagnostic.uds.readDtcInformation.ReadDTCInformationResult.DTCSnapshotDataEntry.GetDTCSnapshotRecord)
    - [C DTCSnapshotRecordEntry ](#tts.tooling.common.diagnostic.uds.readDtcInformation.ReadDTCInformationResult.DTCSnapshotRecordEntry)
      - [M GetDID ](#tts.tooling.common.diagnostic.uds.readDtcInformation.ReadDTCInformationResult.DTCSnapshotRecordEntry.GetDID)
      - [M GetValue ](#tts.tooling.common.diagnostic.uds.readDtcInformation.ReadDTCInformationResult.DTCSnapshotRecordEntry.GetValue)
    - [C DTCFaultCounter ](#tts.tooling.common.diagnostic.uds.readDtcInformation.ReadDTCInformationResult.DTCFaultCounter)
      - [M GetDTC ](#tts.tooling.common.diagnostic.uds.readDtcInformation.ReadDTCInformationResult.DTCFaultCounter.GetDTC)
      - [M GetFaultCounter ](#tts.tooling.common.diagnostic.uds.readDtcInformation.ReadDTCInformationResult.DTCFaultCounter.GetFaultCounter)
    - [C DTCFaultCounterDiagResult ](#tts.tooling.common.diagnostic.uds.readDtcInformation.ReadDTCInformationResult.DTCFaultCounterDiagResult)
      - [M GetDTCFaultList ](#tts.tooling.common.diagnostic.uds.readDtcInformation.ReadDTCInformationResult.DTCFaultCounterDiagResult.GetDTCFaultList)
    - [C UserDTCListDiagResult ](#tts.tooling.common.diagnostic.uds.readDtcInformation.ReadDTCInformationResult.UserDTCListDiagResult)
      - [M GetDTCMemorySelection ](#tts.tooling.common.diagnostic.uds.readDtcInformation.ReadDTCInformationResult.UserDTCListDiagResult.GetDTCMemorySelection)
      - [A DTCMemorySelection ](#tts.tooling.common.diagnostic.uds.readDtcInformation.ReadDTCInformationResult.UserDTCListDiagResult.DTCMemorySelection)
  - [ ReadMemoryByAddress ](#module-tts.tooling.common.diagnostic.uds.readMemoryByAddress.ReadMemoryByAddressResult)
    - [C MemoryDiagResult ](#tts.tooling.common.diagnostic.uds.readMemoryByAddress.ReadMemoryByAddressResult.MemoryDiagResult)
      - [M GetDataRecord ](#tts.tooling.common.diagnostic.uds.readMemoryByAddress.ReadMemoryByAddressResult.MemoryDiagResult.GetDataRecord)
  - [ RoutineControl ](#module-tts.tooling.common.diagnostic.uds.routineControl.RoutineControlResult)
    - [C RoutineDiagResult ](#tts.tooling.common.diagnostic.uds.routineControl.RoutineControlResult.RoutineDiagResult)
      - [M GetRoutineControlType ](#tts.tooling.common.diagnostic.uds.routineControl.RoutineControlResult.RoutineDiagResult.GetRoutineControlType)
      - [M GetRoutineId ](#tts.tooling.common.diagnostic.uds.routineControl.RoutineControlResult.RoutineDiagResult.GetRoutineId)
      - [M GetRoutineInfo ](#tts.tooling.common.diagnostic.uds.routineControl.RoutineControlResult.RoutineDiagResult.GetRoutineInfo)
      - [M GetStatusRecord ](#tts.tooling.common.diagnostic.uds.routineControl.RoutineControlResult.RoutineDiagResult.GetStatusRecord)
  - [ SecurityAccess ](#module-tts.tooling.common.diagnostic.commonJobs.securityAccess.SecurityAccessResult)
    - [C SecurityAccessDiagResult ](#tts.tooling.common.diagnostic.commonJobs.securityAccess.SecurityAccessResult.SecurityAccessDiagResult)
      - [M GetSecuritySeed ](#tts.tooling.common.diagnostic.commonJobs.securityAccess.SecurityAccessResult.SecurityAccessDiagResult.GetSecuritySeed)
      - [M GetGeneratedKey ](#tts.tooling.common.diagnostic.commonJobs.securityAccess.SecurityAccessResult.SecurityAccessDiagResult.GetGeneratedKey)
    - [C SecuritySeedDiagResult ](#tts.tooling.common.diagnostic.commonJobs.securityAccess.SecurityAccessResult.SecuritySeedDiagResult)
      - [M GetSecuritySeed ](#tts.tooling.common.diagnostic.commonJobs.securityAccess.SecurityAccessResult.SecuritySeedDiagResult.GetSecuritySeed)
    - [C SecurityAccessSuccessDiagResult ](#tts.tooling.common.diagnostic.commonJobs.securityAccess.SecurityAccessResult.SecurityAccessSuccessDiagResult)
      - [M IsAccessGranted ](#tts.tooling.common.diagnostic.commonJobs.securityAccess.SecurityAccessResult.SecurityAccessSuccessDiagResult.IsAccessGranted)
  - [ WriteDataByIdentifier ](#module-tts.tooling.common.diagnostic.uds.writeDataByIdentifier.WriteDataByIdentifierResult)
    - [C WriteDataByIdentifierResult ](#tts.tooling.common.diagnostic.uds.writeDataByIdentifier.WriteDataByIdentifierResult.WriteDataByIdentifierResult)
      - [M GetDataIdentifier ](#tts.tooling.common.diagnostic.uds.writeDataByIdentifier.WriteDataByIdentifierResult.WriteDataByIdentifierResult.GetDataIdentifier)
  - [ WriteMemoryByAddress ](#module-tts.tooling.common.diagnostic.uds.writeMemoryByAddress.WriteMemoryByAddressResult)
    - [C WriteMemoryByAddressResult ](#tts.tooling.common.diagnostic.uds.writeMemoryByAddress.WriteMemoryByAddressResult.WriteMemoryByAddressResult)
      - [M GetMemoryAddress ](#tts.tooling.common.diagnostic.uds.writeMemoryByAddress.WriteMemoryByAddressResult.WriteMemoryByAddressResult.GetMemoryAddress)
      - [M GetMemorySize ](#tts.tooling.common.diagnostic.uds.writeMemoryByAddress.WriteMemoryByAddressResult.WriteMemoryByAddressResult.GetMemorySize)
  - [ NegativeResponse ](#module-tts.tooling.common.diagnostic.NegativeResponse)
    - [C NegativeResponse ](#tts.tooling.common.diagnostic.NegativeResponse.NegativeResponse)
      - [M GetUDSErrMsg ](#tts.tooling.common.diagnostic.NegativeResponse.NegativeResponse.GetUDSErrMsg)
    - [C UndefinedResponse ](#tts.tooling.common.diagnostic.NegativeResponse.UndefinedResponse)
- [ KWP2000 result objects ](#kwp2000-result-objects)
  - [ ClearDTC ](#module-tts.tooling.common.diagnostic.kwp2000.clearDtc.ClearDTCResult)
    - [C ClearDTCResult ](#tts.tooling.common.diagnostic.kwp2000.clearDtc.ClearDTCResult.ClearDTCResult)
      - [M GetGroupOfDTCs ](#tts.tooling.common.diagnostic.kwp2000.clearDtc.ClearDTCResult.ClearDTCResult.GetGroupOfDTCs)
  - [ ECUReset ](#diagapikwp2000ecureset)
    - [C ECUResetResult ](#tts.tooling.common.diagnostic.kwp2000.ecuReset.ECUResetResult.ECUResetResult)
      - [M GetResetStatus ](#tts.tooling.common.diagnostic.kwp2000.ecuReset.ECUResetResult.ECUResetResult.GetResetStatus)
  - [ InputOutputControlByCommonIdentifier ](#module-tts.tooling.common.diagnostic.kwp2000.inputOutputControlByCommonIdentifier.InputOutputControlByCommonIdentifierResult)
    - [C InputOutputControlByCommonIdentifierResult ](#tts.tooling.common.diagnostic.kwp2000.inputOutputControlByCommonIdentifier.InputOutputControlByCommonIdentifierResult.InputOutputControlByCommonIdentifierResult)
      - [M GetDataIdentifierHighByte ](#tts.tooling.common.diagnostic.kwp2000.inputOutputControlByCommonIdentifier.InputOutputControlByCommonIdentifierResult.InputOutputControlByCommonIdentifierResult.GetDataIdentifierHighByte)
      - [M GetDataIdentifierLowByte ](#tts.tooling.common.diagnostic.kwp2000.inputOutputControlByCommonIdentifier.InputOutputControlByCommonIdentifierResult.InputOutputControlByCommonIdentifierResult.GetDataIdentifierLowByte)
      - [M GetControlStatus ](#tts.tooling.common.diagnostic.kwp2000.inputOutputControlByCommonIdentifier.InputOutputControlByCommonIdentifierResult.InputOutputControlByCommonIdentifierResult.GetControlStatus)
  - [ InputOutputControlByLocalIdentifier ](#module-tts.tooling.common.diagnostic.kwp2000.inputOutputControlByLocalIdentifier.InputOutputControlByLocalIdentifierResult)
    - [C InputOutputControlByLocalIdentifierResult ](#tts.tooling.common.diagnostic.kwp2000.inputOutputControlByLocalIdentifier.InputOutputControlByLocalIdentifierResult.InputOutputControlByLocalIdentifierResult)
      - [M GetDataIdentifier ](#tts.tooling.common.diagnostic.kwp2000.inputOutputControlByLocalIdentifier.InputOutputControlByLocalIdentifierResult.InputOutputControlByLocalIdentifierResult.GetDataIdentifier)
      - [M GetControlStatus ](#tts.tooling.common.diagnostic.kwp2000.inputOutputControlByLocalIdentifier.InputOutputControlByLocalIdentifierResult.InputOutputControlByLocalIdentifierResult.GetControlStatus)
  - [ ReadDataByCommonIdentifier ](#module-tts.tooling.common.diagnostic.kwp2000.readDataByCommonIdentifier.ReadDataByCommonIdentifierResult)
    - [C ReadDataByCommonIdentifierResult ](#tts.tooling.common.diagnostic.kwp2000.readDataByCommonIdentifier.ReadDataByCommonIdentifierResult.ReadDataByCommonIdentifierResult)
      - [M GetDataIdentifierHighByte ](#tts.tooling.common.diagnostic.kwp2000.readDataByCommonIdentifier.ReadDataByCommonIdentifierResult.ReadDataByCommonIdentifierResult.GetDataIdentifierHighByte)
      - [M GetDataIdentifierLowByte ](#tts.tooling.common.diagnostic.kwp2000.readDataByCommonIdentifier.ReadDataByCommonIdentifierResult.ReadDataByCommonIdentifierResult.GetDataIdentifierLowByte)
      - [M GetData ](#tts.tooling.common.diagnostic.kwp2000.readDataByCommonIdentifier.ReadDataByCommonIdentifierResult.ReadDataByCommonIdentifierResult.GetData)
  - [ ReadDataByLocalIdentifier ](#module-tts.tooling.common.diagnostic.kwp2000.readDataByLocalIdentifier.ReadDataByLocalIdentifierResult)
    - [C ReadDataByLocalIdentifierResult ](#tts.tooling.common.diagnostic.kwp2000.readDataByLocalIdentifier.ReadDataByLocalIdentifierResult.ReadDataByLocalIdentifierResult)
      - [M GetDataIdentifier ](#tts.tooling.common.diagnostic.kwp2000.readDataByLocalIdentifier.ReadDataByLocalIdentifierResult.ReadDataByLocalIdentifierResult.GetDataIdentifier)
      - [M GetData ](#tts.tooling.common.diagnostic.kwp2000.readDataByLocalIdentifier.ReadDataByLocalIdentifierResult.ReadDataByLocalIdentifierResult.GetData)
  - [ ReadDTCInformation ](#diagapikwp2000readdtcinformation)
    - [C ReadDiagnosticTroubleCodesDiagResult ](#tts.tooling.common.diagnostic.kwp2000.readDtcInformation.ReadDTCInformationResult.ReadDiagnosticTroubleCodesDiagResult)
      - [M GetDTCCount ](#tts.tooling.common.diagnostic.kwp2000.readDtcInformation.ReadDTCInformationResult.ReadDiagnosticTroubleCodesDiagResult.GetDTCCount)
      - [M GetDTCFaultList ](#tts.tooling.common.diagnostic.kwp2000.readDtcInformation.ReadDTCInformationResult.ReadDiagnosticTroubleCodesDiagResult.GetDTCFaultList)
    - [C ReadDiagnosticTroubleCodesAndStatusDiagResult ](#tts.tooling.common.diagnostic.kwp2000.readDtcInformation.ReadDTCInformationResult.ReadDiagnosticTroubleCodesAndStatusDiagResult)
      - [M GetDTCCount ](#tts.tooling.common.diagnostic.kwp2000.readDtcInformation.ReadDTCInformationResult.ReadDiagnosticTroubleCodesAndStatusDiagResult.GetDTCCount)
      - [M GetDTCFaultList ](#tts.tooling.common.diagnostic.kwp2000.readDtcInformation.ReadDTCInformationResult.ReadDiagnosticTroubleCodesAndStatusDiagResult.GetDTCFaultList)
  - [ ReadECUIdentification ](#module-tts.tooling.common.diagnostic.kwp2000.readEcuIdentification.ReadECUIdentificationResult)
    - [C ReadECUIdentificationResult ](#tts.tooling.common.diagnostic.kwp2000.readEcuIdentification.ReadECUIdentificationResult.ReadECUIdentificationResult)
      - [M GetDataIdentifier ](#tts.tooling.common.diagnostic.kwp2000.readEcuIdentification.ReadECUIdentificationResult.ReadECUIdentificationResult.GetDataIdentifier)
      - [M GetData ](#tts.tooling.common.diagnostic.kwp2000.readEcuIdentification.ReadECUIdentificationResult.ReadECUIdentificationResult.GetData)
  - [ RoutineControl ](#diagapikwp2000routinecontrol)
    - [C RoutineByLocalIdentifierDiagResult ](#tts.tooling.common.diagnostic.kwp2000.routineControl.RoutineControlResult.RoutineByLocalIdentifierDiagResult)
      - [M GetRoutineId ](#tts.tooling.common.diagnostic.kwp2000.routineControl.RoutineControlResult.RoutineByLocalIdentifierDiagResult.GetRoutineId)
      - [M GetStatusRecord ](#tts.tooling.common.diagnostic.kwp2000.routineControl.RoutineControlResult.RoutineByLocalIdentifierDiagResult.GetStatusRecord)
    - [C StartRoutineByLocalIdentifierDiagResult ](#tts.tooling.common.diagnostic.kwp2000.routineControl.RoutineControlResult.StartRoutineByLocalIdentifierDiagResult)
      - [M GetEntryStatus ](#tts.tooling.common.diagnostic.kwp2000.routineControl.RoutineControlResult.StartRoutineByLocalIdentifierDiagResult.GetEntryStatus)
    - [C StopRoutineByLocalIdentifierDiagResult ](#tts.tooling.common.diagnostic.kwp2000.routineControl.RoutineControlResult.StopRoutineByLocalIdentifierDiagResult)
      - [M GetExitStatus ](#tts.tooling.common.diagnostic.kwp2000.routineControl.RoutineControlResult.StopRoutineByLocalIdentifierDiagResult.GetExitStatus)
    - [C RequestRoutineByLocalIdentifierDiagResult ](#tts.tooling.common.diagnostic.kwp2000.routineControl.RoutineControlResult.RequestRoutineByLocalIdentifierDiagResult)
      - [M GetRoutineResults ](#tts.tooling.common.diagnostic.kwp2000.routineControl.RoutineControlResult.RequestRoutineByLocalIdentifierDiagResult.GetRoutineResults)
  - [ WriteDataByCommonIdentifier ](#module-tts.tooling.common.diagnostic.kwp2000.writeDataByCommonIdentifier.WriteDataByCommonIdentifierResult)
    - [C WriteDataByCommonIdentifierResult ](#tts.tooling.common.diagnostic.kwp2000.writeDataByCommonIdentifier.WriteDataByCommonIdentifierResult.WriteDataByCommonIdentifierResult)
      - [M GetDataIdentifierHighByte ](#tts.tooling.common.diagnostic.kwp2000.writeDataByCommonIdentifier.WriteDataByCommonIdentifierResult.WriteDataByCommonIdentifierResult.GetDataIdentifierHighByte)
      - [M GetDataIdentifierLowByte ](#tts.tooling.common.diagnostic.kwp2000.writeDataByCommonIdentifier.WriteDataByCommonIdentifierResult.WriteDataByCommonIdentifierResult.GetDataIdentifierLowByte)
  - [ WriteDataByLocalIdentifier ](#module-tts.tooling.common.diagnostic.kwp2000.writeDataByLocalIdentifier.WriteDataByLocalIdentifierResult)
    - [C WriteDataByLocalIdentifierResult ](#tts.tooling.common.diagnostic.kwp2000.writeDataByLocalIdentifier.WriteDataByLocalIdentifierResult.WriteDataByLocalIdentifierResult)
      - [M GetDataIdentifier ](#tts.tooling.common.diagnostic.kwp2000.writeDataByLocalIdentifier.WriteDataByLocalIdentifierResult.WriteDataByLocalIdentifierResult.GetDataIdentifier)
- [ J1939 ](#j1939)
  - [C J1939Message ](#tts.testModule.bus.busObjects.J1939.J1939Message)
    - [A priority ](#tts.testModule.bus.busObjects.J1939.J1939Message.priority)
    - [A pduFormat ](#tts.testModule.bus.busObjects.J1939.J1939Message.pduFormat)
    - [A pduSpecific ](#tts.testModule.bus.busObjects.J1939.J1939Message.pduSpecific)
    - [A sourceAddress ](#tts.testModule.bus.busObjects.J1939.J1939Message.sourceAddress)
    - [A tla ](#tts.testModule.bus.busObjects.J1939.J1939Message.tla)
    - [A payload ](#tts.testModule.bus.busObjects.J1939.J1939Message.payload)
    - [A timestamp ](#tts.testModule.bus.busObjects.J1939.J1939Message.timestamp)
  - [C J1939DTCList ](#tts.testModule.bus.busObjects.J1939.J1939DTCList)
    - [M Check ](#tts.testModule.bus.busObjects.J1939.J1939DTCList.Check)
  - [C J1939DTC ](#tts.testModule.bus.busObjects.J1939.J1939DTC)
    - [A sourceAddress ](#tts.testModule.bus.busObjects.J1939.J1939DTC.sourceAddress)
    - [A tla ](#tts.testModule.bus.busObjects.J1939.J1939DTC.tla)
    - [A spn ](#tts.testModule.bus.busObjects.J1939.J1939DTC.spn)
    - [A fmi ](#tts.testModule.bus.busObjects.J1939.J1939DTC.fmi)
    - [A dtc ](#tts.testModule.bus.busObjects.J1939.J1939DTC.dtc)
    - [A count ](#tts.testModule.bus.busObjects.J1939.J1939DTC.count)
    - [A type ](#tts.testModule.bus.busObjects.J1939.J1939DTC.type)
    - [A timestamp ](#tts.testModule.bus.busObjects.J1939.J1939DTC.timestamp)

# Advanced properties of diagnostics-related objects[¶](#advanced-properties-of-diagnostics-related-objects "Link to this heading")

## UDS result objects[¶](#uds-result-objects "Link to this heading")

*class* DiagResult(*[responseObj](#ttRawDiag.diag.DiagResult.DiagResult "ttRawDiag.diag.DiagResult.DiagResult.__init__.responseObj (Python parameter)")*, *[errCode](#ttRawDiag.diag.DiagResult.DiagResult "ttRawDiag.diag.DiagResult.DiagResult.__init__.errCode (Python parameter)")*, *[responseTime](#ttRawDiag.diag.DiagResult.DiagResult "ttRawDiag.diag.DiagResult.DiagResult.__init__.responseTime (Python parameter)")*, *[pendingCount](#ttRawDiag.diag.DiagResult.DiagResult "ttRawDiag.diag.DiagResult.DiagResult.__init__.pendingCount (Python parameter)")*, *[busyCount](#ttRawDiag.diag.DiagResult.DiagResult "ttRawDiag.diag.DiagResult.DiagResult.__init__.busyCount (Python parameter)")*)[¶](#ttRawDiag.diag.DiagResult.DiagResult "Link to this definition")  
GetResponse()[¶](#ttRawDiag.diag.DiagResult.DiagResult.GetResponse "Link to this definition")  
Returns the diagnostics response.

Returns:  Diagnostics response or None if no response was received.

Return type:  [`ByteStream`](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream (Python class) — The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.")

GetErrCode()[¶](#ttRawDiag.diag.DiagResult.DiagResult.GetErrCode "Link to this definition")  
Returns the error code. The error codes and their meaning can be found in the table below.

Returns:  Error code

Return type:  int

| Error code | Error message                              |
|------------|--------------------------------------------|
| 0          | ”Ok”                                       |
| 1          | ”Timeout in transport layer”               |
| 2          | ”Received negative response”               |
| 3          | ”No active diagnostics session”            |
| 4          | ”Timeout waiting for diagnostics response” |
| 5          | ”Transmission error”                       |
| 6          | ”Unexpected response”                      |
| 7          | ”Still waiting for response”               |
| 8          | ”Transport error”                          |
| 9          | ”Application error”                        |

GetErrMsg()[¶](#ttRawDiag.diag.DiagResult.DiagResult.GetErrMsg "Link to this definition")  
Returns a textual representation of the error code.

Returns:  Error message

Return type:  str

GetResponseTime()[¶](#ttRawDiag.diag.DiagResult.DiagResult.GetResponseTime "Link to this definition")  
Returns the time between sending the request and receiving the response in ms.

Returns:  Time until response was received in ms

Return type:  int

GetPendingCount()[¶](#ttRawDiag.diag.DiagResult.DiagResult.GetPendingCount "Link to this definition")  
Returns the number of received RCRRP messages (Request correctly received, but response is pending).

Returns:  Number of received RCRRP messages

Return type:  int

GetBusyCount()[¶](#ttRawDiag.diag.DiagResult.DiagResult.GetBusyCount "Link to this definition")  
Returns the number of received BRR messages (Busy, repeat request).

Returns:  Number of received BRR messages

Return type:  int

GetTpInfo()[¶](#ttRawDiag.diag.DiagResult.DiagResult.GetTpInfo "Link to this definition")  
Provides the following protocol-specific information:

- CAN: CanId of the response

- FlexRay, DoIP, DoSoAd: source address of the response

DoIP example: {‘sourceAddress’: ByteStream(‘01:00’)}

Returns:  Transport protocol specific information.

Return type:  dict

GetServiceId()[¶](#ttRawDiag.diag.DiagResult.DiagResult.GetServiceId "Link to this definition")  
Returns the service ID of the diagnostic response.

Returns:  Service ID of the diagnostic response

Return type:  int

### DiagService[¶](#diagservice "Link to this heading")

*class* DiagServiceResult[¶](#tts.tooling.common.diagnostic.DiagServiceResult.DiagServiceResult "Link to this definition")  

GetDecodedResponse()[¶](#tts.tooling.common.diagnostic.DiagServiceResult.DiagServiceResult.GetDecodedResponse "Link to this definition")  
Returns the decoded response of the original raw response.

Returns:  Decoded response

Return type:  dict | NotPresent

### ObdOnUdsService[¶](#obdonudsservice "Link to this heading")

*class* ObdOnUdsServiceResult[¶](#tts.tooling.common.diagnostic.DiagServiceResult.ObdOnUdsServiceResult "Link to this definition")  

GetDecodedResponse()[¶](#tts.tooling.common.diagnostic.DiagServiceResult.ObdOnUdsServiceResult.GetDecodedResponse "Link to this definition")  
Returns the decoded response of the original raw response.

Returns:  Decoded response

Return type:  dict | NotPresent

### Authentication[¶](#module-tts.tooling.common.diagnostic.uds.authentication.AuthenticationResult "Link to this heading")

*class* AuthenticationConfigurationResult[¶](#tts.tooling.common.diagnostic.uds.authentication.AuthenticationResult.AuthenticationConfigurationResult "Link to this definition")  
Bases: [`AuthenticationResult`](#tts.tooling.common.diagnostic.uds.authentication.AuthenticationResult.AuthenticationResult "tts.tooling.common.diagnostic.uds.authentication.AuthenticationResult.AuthenticationResult (Python class) — Bases: DiagResult")

*class* AuthenticationDeauthenticateResult[¶](#tts.tooling.common.diagnostic.uds.authentication.AuthenticationResult.AuthenticationDeauthenticateResult "Link to this definition")  
Bases: [`AuthenticationResult`](#tts.tooling.common.diagnostic.uds.authentication.AuthenticationResult.AuthenticationResult "tts.tooling.common.diagnostic.uds.authentication.AuthenticationResult.AuthenticationResult (Python class) — Bases: DiagResult")

*class* AuthenticationProofOfOwnershipResult[¶](#tts.tooling.common.diagnostic.uds.authentication.AuthenticationResult.AuthenticationProofOfOwnershipResult "Link to this definition")  
Bases: [`AuthenticationResult`](#tts.tooling.common.diagnostic.uds.authentication.AuthenticationResult.AuthenticationResult "tts.tooling.common.diagnostic.uds.authentication.AuthenticationResult.AuthenticationResult (Python class) — Bases: DiagResult")

GetSessionKeyInfo()[¶](#tts.tooling.common.diagnostic.uds.authentication.AuthenticationResult.AuthenticationProofOfOwnershipResult.GetSessionKeyInfo "Link to this definition")  
If present, this value shall contain session key information, e.g. the encrypted session key(s) for securing further communication in the actual session and/or proof value(s) (e.g. a hash value) for the validation of the session key(s) on the client side.

NOTE 1 This information is linked to the contents of the request message data-parameter communicationConfiguration. The format of this parameter as well as the creation of the session key(s) and the computation of the proof value(s) are up to the vehicle manufacturer choice.

Return type:  [`ByteStream`](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream (Python class) — The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.")

*class* AuthenticationResult[¶](#tts.tooling.common.diagnostic.uds.authentication.AuthenticationResult.AuthenticationResult "Link to this definition")  
Bases: [`DiagResult`](#ttRawDiag.diag.DiagResult.DiagResult "ttRawDiag.diag.DiagResult.DiagResult (Python class) — Returns the diagnostics response.")

ReturnValue[¶](#tts.tooling.common.diagnostic.uds.authentication.AuthenticationResult.AuthenticationResult.ReturnValue "Link to this definition")  
This parameter returns the result of the procedure on the server.

*class* AuthenticationVerifyCertificateUnidirectionalResult[¶](#tts.tooling.common.diagnostic.uds.authentication.AuthenticationResult.AuthenticationVerifyCertificateUnidirectionalResult "Link to this definition")  
Bases: [`AuthenticationResult`](#tts.tooling.common.diagnostic.uds.authentication.AuthenticationResult.AuthenticationResult "tts.tooling.common.diagnostic.uds.authentication.AuthenticationResult.AuthenticationResult (Python class) — Bases: DiagResult")

GetChallengeServer()[¶](#tts.tooling.common.diagnostic.uds.authentication.AuthenticationResult.AuthenticationVerifyCertificateUnidirectionalResult.GetChallengeServer "Link to this definition")  
The challenge contains vehicle manufacturer specific formatted server data (eventually containing randomized information) or is a random number. This parameter record is to transmit the challenge to the client.

Return type:  [`ByteStream`](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream (Python class) — The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.")

GetEphemeralPublicKeyServer()[¶](#tts.tooling.common.diagnostic.uds.authentication.AuthenticationResult.AuthenticationVerifyCertificateUnidirectionalResult.GetEphemeralPublicKeyServer "Link to this definition")  
Ephemeral public key generated by the server for Diffie-Hellman key agreement.

Return type:  [`ByteStream`](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream (Python class) — The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.")

### UploadDownloadFunctionalUnit[¶](#module-tts.tooling.common.diagnostic.uds.uploadDownloadFunctionalUnit.UploadDownloadFunctionalUnitResult "Link to this heading")

*class* RequestDownloadResult[¶](#tts.tooling.common.diagnostic.uds.uploadDownloadFunctionalUnit.UploadDownloadFunctionalUnitResult.RequestDownloadResult "Link to this definition")  
Bases: [`DiagResult`](#ttRawDiag.diag.DiagResult.DiagResult "ttRawDiag.diag.DiagResult.DiagResult (Python class) — Returns the diagnostics response.")

GetLengthFormatIdentifier()[¶](#tts.tooling.common.diagnostic.uds.uploadDownloadFunctionalUnit.UploadDownloadFunctionalUnitResult.RequestDownloadResult.GetLengthFormatIdentifier "Link to this definition")  
This parameter returns the length of the following maxNumberOfBlockLength in bytes.

Return type:  int

GetMaxNumberOfBlockLength()[¶](#tts.tooling.common.diagnostic.uds.uploadDownloadFunctionalUnit.UploadDownloadFunctionalUnitResult.RequestDownloadResult.GetMaxNumberOfBlockLength "Link to this definition")  
This parameter returns the maxNumberOfBlockLength field of the UDS response. It specifies the maximal length of bytes the client is allowed to send in each TransferData message. This length reflects the complete message length, including the service identifier and the data-parameters present in the TransferData request message.

Return type:  [ByteStream](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream (Python class) — The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.")

GetMaxNumberOfBlockLengthAsInt()[¶](#tts.tooling.common.diagnostic.uds.uploadDownloadFunctionalUnit.UploadDownloadFunctionalUnitResult.RequestDownloadResult.GetMaxNumberOfBlockLengthAsInt "Link to this definition")  
This parameter returns the maxNumberOfBlockLength field of the UDS response, interpreted as an integer value.

Return type:  int

GetNumberOfBlockLengthParameterLength()[¶](#tts.tooling.common.diagnostic.uds.uploadDownloadFunctionalUnit.UploadDownloadFunctionalUnitResult.RequestDownloadResult.GetNumberOfBlockLengthParameterLength "Link to this definition")  
This parameter returns the length of the maxNumberOfBlockLength field within the UDS response.

Return type:  int

*class* TransferDataBlockResult[¶](#tts.tooling.common.diagnostic.uds.uploadDownloadFunctionalUnit.UploadDownloadFunctionalUnitResult.TransferDataBlockResult "Link to this definition")  
Bases: [`DiagResult`](#ttRawDiag.diag.DiagResult.DiagResult "ttRawDiag.diag.DiagResult.DiagResult (Python class) — Returns the diagnostics response.")

GetBlockSequenceCounter()[¶](#tts.tooling.common.diagnostic.uds.uploadDownloadFunctionalUnit.UploadDownloadFunctionalUnitResult.TransferDataBlockResult.GetBlockSequenceCounter "Link to this definition")  
This parameter returns the block sequence counter of the UDS response as a decimal integer value.

Return type:  int

*class* TransferDataResult[¶](#tts.tooling.common.diagnostic.uds.uploadDownloadFunctionalUnit.UploadDownloadFunctionalUnitResult.TransferDataResult "Link to this definition")  

GetAllBlockResults()[¶](#tts.tooling.common.diagnostic.uds.uploadDownloadFunctionalUnit.UploadDownloadFunctionalUnitResult.TransferDataResult.GetAllBlockResults "Link to this definition")  
Returns all responses from each transfer data block as list.

Return type:  list\<[`TransferDataBlockResult`](#tts.tooling.common.diagnostic.uds.uploadDownloadFunctionalUnit.UploadDownloadFunctionalUnitResult.TransferDataBlockResult "tts.tooling.common.diagnostic.uds.uploadDownloadFunctionalUnit.UploadDownloadFunctionalUnitResult.TransferDataBlockResult (Python class) — Bases: DiagResult")\>

GetErrCode()[¶](#tts.tooling.common.diagnostic.uds.uploadDownloadFunctionalUnit.UploadDownloadFunctionalUnitResult.TransferDataResult.GetErrCode "Link to this definition")  
Returns the error code of the last received response.

Return type:  int

GetErrMsg()[¶](#tts.tooling.common.diagnostic.uds.uploadDownloadFunctionalUnit.UploadDownloadFunctionalUnitResult.TransferDataResult.GetErrMsg "Link to this definition")  
Returns the error message of the last received response

Return type:  str

GetResponse()[¶](#tts.tooling.common.diagnostic.uds.uploadDownloadFunctionalUnit.UploadDownloadFunctionalUnitResult.TransferDataResult.GetResponse "Link to this definition")  
Returns the last received response of the transfer data blocks

Return type:  [`ByteStream`](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream (Python class) — The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.")

### DiagnosticSessionControl[¶](#module-tts.tooling.common.diagnostic.uds.diagnosticSessionControl.DiagnosticSessionControlResult "Link to this heading")

*class* DiagnosticSessionControlResult[¶](#tts.tooling.common.diagnostic.uds.diagnosticSessionControl.DiagnosticSessionControlResult.DiagnosticSessionControlResult "Link to this definition")  
Bases: [`DiagResult`](#ttRawDiag.diag.DiagResult.DiagResult "ttRawDiag.diag.DiagResult.DiagResult (Python class) — Returns the diagnostics response.")

GetP2ServerMax1()[¶](#tts.tooling.common.diagnostic.uds.diagnosticSessionControl.DiagnosticSessionControlResult.DiagnosticSessionControlResult.GetP2ServerMax1 "Link to this definition")  
Returns the default P2Server_max timing supported by the server for the activated diagnostic session.

Return type:  int

GetP2ServerMax2()[¶](#tts.tooling.common.diagnostic.uds.diagnosticSessionControl.DiagnosticSessionControlResult.DiagnosticSessionControlResult.GetP2ServerMax2 "Link to this definition")  
Returns the enhanced (NRC 0x78) P2 Server_max supported by the server for the activated diagnostic session.

Return type:  int

GetSubfunction()[¶](#tts.tooling.common.diagnostic.uds.diagnosticSessionControl.DiagnosticSessionControlResult.DiagnosticSessionControlResult.GetSubfunction "Link to this definition")  
Returns the subfunction the service has been called with.

Return type:  int

### ECUReset[¶](#module-tts.tooling.common.diagnostic.uds.ecuReset.ECUResetResult "Link to this heading")

*class* ECUResetResult[¶](#tts.tooling.common.diagnostic.uds.ecuReset.ECUResetResult.ECUResetResult "Link to this definition")  
Bases: [`DiagResult`](#ttRawDiag.diag.DiagResult.DiagResult "ttRawDiag.diag.DiagResult.DiagResult (Python class) — Returns the diagnostics response.")

This class represents the result of a successful ECUReset (0x11) call, consisting of the data record.

GetPowerDownTime()[¶](#tts.tooling.common.diagnostic.uds.ecuReset.ECUResetResult.ECUResetResult.GetPowerDownTime "Link to this definition")  
Returns the minimum time the server will remain in the power down sequence in seconds. 0xFF indicates a failure or time not available.

Returns:  Power down time

Return type:  int

### InputOutputControlByIdentifier[¶](#module-tts.tooling.common.diagnostic.uds.inputOutputControlByIdentifier.InputOutputControlByIdentifierResult "Link to this heading")

*class* InputOutputControlByIdentifierResult[¶](#tts.tooling.common.diagnostic.uds.inputOutputControlByIdentifier.InputOutputControlByIdentifierResult.InputOutputControlByIdentifierResult "Link to this definition")  
Bases: [`DiagResult`](#ttRawDiag.diag.DiagResult.DiagResult "ttRawDiag.diag.DiagResult.DiagResult (Python class) — Returns the diagnostics response.")

Result of a successful InputOutputControlByIdentifier (0x2F) call, consisting of ID and data. Only one set of (ID, data) is supported.

GetDataIdentifier()[¶](#tts.tooling.common.diagnostic.uds.inputOutputControlByIdentifier.InputOutputControlByIdentifierResult.InputOutputControlByIdentifierResult.GetDataIdentifier "Link to this definition")  
Returns the data identifier.

Returns:  Data identifier

Return type:  int

GetIoCtrlParam()[¶](#tts.tooling.common.diagnostic.uds.inputOutputControlByIdentifier.InputOutputControlByIdentifierResult.InputOutputControlByIdentifierResult.GetIoCtrlParam "Link to this definition")  
Returns the inputOutputControlParameter.

Returns:  inputOutputControlParameter

Return type:  int

GetData()[¶](#tts.tooling.common.diagnostic.uds.inputOutputControlByIdentifier.InputOutputControlByIdentifierResult.InputOutputControlByIdentifierResult.GetData "Link to this definition")  
Returns the data record.

Returns:  Data record

Return type:  [`ByteStream`](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream (Python class) — The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.")

### ReadDataByIdentifier[¶](#module-tts.tooling.common.diagnostic.uds.readDataByIdentifier.ReadDataByIdentifierResult "Link to this heading")

*class* DataRecordDiagResult[¶](#tts.tooling.common.diagnostic.uds.readDataByIdentifier.ReadDataByIdentifierResult.DataRecordDiagResult "Link to this definition")  
Bases: [`DiagResult`](#ttRawDiag.diag.DiagResult.DiagResult "ttRawDiag.diag.DiagResult.DiagResult (Python class) — Returns the diagnostics response.")

Result of a successful ReadDataByIdentifier (0x22) call, consisting of ID and data. Only one set of (ID, data) is supported.

GetDataIdentifier()[¶](#tts.tooling.common.diagnostic.uds.readDataByIdentifier.ReadDataByIdentifierResult.DataRecordDiagResult.GetDataIdentifier "Link to this definition")  
Returns the data identifier.

Returns:  Data identifier

Return type:  int

GetData()[¶](#tts.tooling.common.diagnostic.uds.readDataByIdentifier.ReadDataByIdentifierResult.DataRecordDiagResult.GetData "Link to this definition")  
Returns the data record.

Returns:  Data record

Return type:  [`ByteStream`](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream (Python class) — The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.")

### ReadDTCInformation[¶](#module-tts.testModule.diag.diagObjects.DTCResult "Link to this heading")

*class* DTCListDiagResult[¶](#tts.testModule.diag.diagObjects.DTCResult.DTCListDiagResult "Link to this definition")  
Bases: `list`, [`DiagResult`](#ttRawDiag.diag.DiagResult.DiagResult "ttRawDiag.diag.DiagResult.DiagResult (Python class) — Returns the diagnostics response.")

This class represents the result of calling a diagnostic service whose response is expected to contain a DTC status availability mask and a list of DTCs and status codes, e.g. ReadDTCInformation.reportDTCByStatusMask.

Beside the methods and properties documented below, you can also use it just like a list. The list elements are of type [`DTCAndStatusRecord`](#tts.testModule.diag.diagObjects.DTCResult.DTCAndStatusRecord "tts.testModule.diag.diagObjects.DTCResult.DTCAndStatusRecord (Python class) — Bases: DTCNumber").

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

GetShortName()[¶](#tts.testModule.diag.diagObjects.DTCResult.DTCNumber.GetShortName "Link to this definition")  
Returns the short name

Returns:  DTC name

Return type:  str

SetShortName(*[name](#tts.testModule.diag.diagObjects.DTCResult.DTCNumber.SetShortName.name "tts.testModule.diag.diagObjects.DTCResult.DTCNumber.SetShortName.name (Python parameter) — DTC name")*)[¶](#tts.testModule.diag.diagObjects.DTCResult.DTCNumber.SetShortName "Link to this definition")  
Set the short name

Parameters:  name : str[¶](#tts.testModule.diag.diagObjects.DTCResult.DTCNumber.SetShortName.name "Permalink to this definition")  
DTC name

GetShortNumber()[¶](#tts.testModule.diag.diagObjects.DTCResult.DTCNumber.GetShortNumber "Link to this definition")  
Returns the 2 byte DTC number

Returns:  DTC number

Return type:  int

GetDefinition()[¶](#tts.testModule.diag.diagObjects.DTCResult.DTCNumber.GetDefinition "Link to this definition")  
Returns the J2012 Representation (also known as P code) including the Failure Type Byte

Returns:  J2012 representation

Return type:  str

GetShortDefinition()[¶](#tts.testModule.diag.diagObjects.DTCResult.DTCNumber.GetShortDefinition "Link to this definition")  
Returns the J2012 Representation (also known as P code) without Failure Type Byte

Returns:  J2012 representation

Return type:  str

GetFTB()[¶](#tts.testModule.diag.diagObjects.DTCResult.DTCNumber.GetFTB "Link to this definition")  
Returns the Failure Type Byte

Returns:  Failure type byte

Return type:  int

GetDescription()[¶](#tts.testModule.diag.diagObjects.DTCResult.DTCNumber.GetDescription "Link to this definition")  
Returns the description of the DTC, if known; else None

Returns:  DTC description

Return type:  str

SetDescription(*[description](#tts.testModule.diag.diagObjects.DTCResult.DTCNumber.SetDescription.description "tts.testModule.diag.diagObjects.DTCResult.DTCNumber.SetDescription.description (Python parameter) — DTC description")*)[¶](#tts.testModule.diag.diagObjects.DTCResult.DTCNumber.SetDescription "Link to this definition")  
Set the description

Parameters:  description : str[¶](#tts.testModule.diag.diagObjects.DTCResult.DTCNumber.SetDescription.description "Permalink to this definition")  
DTC description

*class* DTCAndStatusRecord[¶](#tts.testModule.diag.diagObjects.DTCResult.DTCAndStatusRecord "Link to this definition")  
Bases: [`DTCNumber`](#tts.testModule.diag.diagObjects.DTCResult.DTCNumber "tts.testModule.diag.diagObjects.DTCResult.DTCNumber (Python class) — Bases: object")

This object represents the DTC number itself and the status code of the DTC.

GetStatus()[¶](#tts.testModule.diag.diagObjects.DTCResult.DTCAndStatusRecord.GetStatus "Link to this definition")  
Returns the DTC status code

Returns:  DTC status code

Return type:  int

*class* DTCNumberDiagResult[¶](#tts.tooling.common.diagnostic.uds.readDtcInformation.ReadDTCInformationResult.DTCNumberDiagResult "Link to this definition")  
Bases: [`DiagResult`](#ttRawDiag.diag.DiagResult.DiagResult "ttRawDiag.diag.DiagResult.DiagResult (Python class) — Returns the diagnostics response.")

This class represents the result of calling a diagnostic service whose response is expected to contain a DTC status availability mask, a DTC format identifier and the DTC count, e.g. ReadDTCInformation.reportNumberOfDTCByStatusMask.

GetDTCStatusAvailabilityMask()[¶](#tts.tooling.common.diagnostic.uds.readDtcInformation.ReadDTCInformationResult.DTCNumberDiagResult.GetDTCStatusAvailabilityMask "Link to this definition")  
Returns the status availability mask as stated in the ECU’s response

Returns:  Status availability mask

Return type:  int

GetDTCFormatIdentifier()[¶](#tts.tooling.common.diagnostic.uds.readDtcInformation.ReadDTCInformationResult.DTCNumberDiagResult.GetDTCFormatIdentifier "Link to this definition")  
Returns the DTC format identifier

Returns:  DTC format identifier

Return type:  int

GetDTCCount()[¶](#tts.tooling.common.diagnostic.uds.readDtcInformation.ReadDTCInformationResult.DTCNumberDiagResult.GetDTCCount "Link to this definition")  
Returns the DTC count

Returns:  DTC count

Return type:  int

*class* DTCSnapshotIdentification[¶](#tts.tooling.common.diagnostic.uds.readDtcInformation.ReadDTCInformationResult.DTCSnapshotIdentification "Link to this definition")  
Bases: `object`

This object represents a single DTC snapshot identification list entry consisting of the DTC number and the according snapshot number.

GetDTC()[¶](#tts.tooling.common.diagnostic.uds.readDtcInformation.ReadDTCInformationResult.DTCSnapshotIdentification.GetDTC "Link to this definition")  
Returns the DTC number

Returns:  DTC number

Return type:  int

GetSnapshotNumber()[¶](#tts.tooling.common.diagnostic.uds.readDtcInformation.ReadDTCInformationResult.DTCSnapshotIdentification.GetSnapshotNumber "Link to this definition")  
Returns the snapshot number

Returns:  Snapshot number of the DTC

Return type:  int

*class* DTCSnapshotIdentificationDiagResult[¶](#tts.tooling.common.diagnostic.uds.readDtcInformation.ReadDTCInformationResult.DTCSnapshotIdentificationDiagResult "Link to this definition")  
Bases: [`DiagResult`](#ttRawDiag.diag.DiagResult.DiagResult "ttRawDiag.diag.DiagResult.DiagResult (Python class) — Returns the diagnostics response.")

This class represents the result of calling a diagnostic service whose response is expected to contain a list of DTC numbers and according snapshot numbers, e.g. ReadDTCInformation.reportDTCSnapshotIdentification.

GetDTCSnapshotList()[¶](#tts.tooling.common.diagnostic.uds.readDtcInformation.ReadDTCInformationResult.DTCSnapshotIdentificationDiagResult.GetDTCSnapshotList "Link to this definition")  
Returns the snapshot list.

Returns:  List of DTCs and corresponding snapshot numbers

Return type:  list\<[`DTCSnapshotIdentification`](#tts.tooling.common.diagnostic.uds.readDtcInformation.ReadDTCInformationResult.DTCSnapshotIdentification "tts.tooling.common.diagnostic.uds.readDtcInformation.ReadDTCInformationResult.DTCSnapshotIdentification (Python class) — Bases: object")\>

*class* DTCSnapshotRecordDiagResult[¶](#tts.tooling.common.diagnostic.uds.readDtcInformation.ReadDTCInformationResult.DTCSnapshotRecordDiagResult "Link to this definition")  
Bases: [`DiagResult`](#ttRawDiag.diag.DiagResult.DiagResult "ttRawDiag.diag.DiagResult.DiagResult (Python class) — Returns the diagnostics response.")

This class represents the result of a successful ReportDTCSnapshotRecordByDTCNumber (0x1904) call, consisting of the DTC number, the DTC status, the DTC snapshot records as raw data and, if the according option was chosen when the job ReportDTCSnapshotRecordByDTCNumber called, the snapshot data in an interpreted form. The latter is only possible if the values of the DIDs containing within the snapshot have a fixed length.

GetDTCAndStatusRecord()[¶](#tts.tooling.common.diagnostic.uds.readDtcInformation.ReadDTCInformationResult.DTCSnapshotRecordDiagResult.GetDTCAndStatusRecord "Link to this definition")  
Returns the DTCAndStatusRecord contained in the response.

Returns:  Object containig DTC number (3 bytes) and status information

Return type:  [`DTCAndStatusRecord`](#tts.testModule.diag.diagObjects.DTCResult.DTCAndStatusRecord "tts.testModule.diag.diagObjects.DTCResult.DTCAndStatusRecord (Python class) — Bases: DTCNumber")

GetDTCSnapshotData()[¶](#tts.tooling.common.diagnostic.uds.readDtcInformation.ReadDTCInformationResult.DTCSnapshotRecordDiagResult.GetDTCSnapshotData "Link to this definition")  
Returns a list containing the DTC snapshot data.

Returns:  List containing the DTC snapshot data

Return type:  list\<[`DTCSnapshotDataEntry`](#tts.tooling.common.diagnostic.uds.readDtcInformation.ReadDTCInformationResult.DTCSnapshotDataEntry "tts.tooling.common.diagnostic.uds.readDtcInformation.ReadDTCInformationResult.DTCSnapshotDataEntry (Python class) — Bases: object")\>

GetDTCSnapshotDataRaw()[¶](#tts.tooling.common.diagnostic.uds.readDtcInformation.ReadDTCInformationResult.DTCSnapshotRecordDiagResult.GetDTCSnapshotDataRaw "Link to this definition")  
Returns the DTC snapshot data as ByteStream.

Returns:  DTC snapshot data

Return type:  [ByteStream](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream (Python class) — The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.")

*class* DTCSnapshotDataEntry[¶](#tts.tooling.common.diagnostic.uds.readDtcInformation.ReadDTCInformationResult.DTCSnapshotDataEntry "Link to this definition")  
Bases: `object`

This class represents a DTC snapshot data entry consisting of the occurrence number of the snapshot, the number of DataIdentifiers it contains and the associated recorded snapshot data.

GetDTCSnapshotRecordNumber()[¶](#tts.tooling.common.diagnostic.uds.readDtcInformation.ReadDTCInformationResult.DTCSnapshotDataEntry.GetDTCSnapshotRecordNumber "Link to this definition")  
Returns the DTC snapshot record number.

Returns:  DTC snapshot record number

Return type:  int

GetDTCSnapshotRecordNumberOfIdentifiers()[¶](#tts.tooling.common.diagnostic.uds.readDtcInformation.ReadDTCInformationResult.DTCSnapshotDataEntry.GetDTCSnapshotRecordNumberOfIdentifiers "Link to this definition")  
Returns the number of data identifiers contained in the snapshot data.

Returns:  Number of identifiers

Return type:  int

GetDTCSnapshotRecord()[¶](#tts.tooling.common.diagnostic.uds.readDtcInformation.ReadDTCInformationResult.DTCSnapshotDataEntry.GetDTCSnapshotRecord "Link to this definition")  
Returns a list representing the snapshot data record. Each snapshot data record entry consists of the data identifier and its value.

Returns:  List containing the DTC snapshot record entries.

Return type:  list\<[`DTCSnapshotRecordEntry`](#tts.tooling.common.diagnostic.uds.readDtcInformation.ReadDTCInformationResult.DTCSnapshotRecordEntry "tts.tooling.common.diagnostic.uds.readDtcInformation.ReadDTCInformationResult.DTCSnapshotRecordEntry (Python class) — Bases: object")\>

*class* DTCSnapshotRecordEntry[¶](#tts.tooling.common.diagnostic.uds.readDtcInformation.ReadDTCInformationResult.DTCSnapshotRecordEntry "Link to this definition")  
Bases: `object`

This class represents a DTC snapshot record entry consisting of the data identifier and its value.

GetDID()[¶](#tts.tooling.common.diagnostic.uds.readDtcInformation.ReadDTCInformationResult.DTCSnapshotRecordEntry.GetDID "Link to this definition")  
Returns the data identifier.

Returns:  Data identifier

Return type:  int

GetValue()[¶](#tts.tooling.common.diagnostic.uds.readDtcInformation.ReadDTCInformationResult.DTCSnapshotRecordEntry.GetValue "Link to this definition")  
Returns the value of the data identifier.

Returns:  Value of the data identifier

Return type:  [ByteStream](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream (Python class) — The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.")

*class* DTCFaultCounter[¶](#tts.tooling.common.diagnostic.uds.readDtcInformation.ReadDTCInformationResult.DTCFaultCounter "Link to this definition")  
Bases: `object`

This object represents a single DTC fault counter list entry consisting of the DTC number and the according fault counter.

GetDTC()[¶](#tts.tooling.common.diagnostic.uds.readDtcInformation.ReadDTCInformationResult.DTCFaultCounter.GetDTC "Link to this definition")  
Returns the DTC number

Returns:  DTC number

Return type:  int

GetFaultCounter()[¶](#tts.tooling.common.diagnostic.uds.readDtcInformation.ReadDTCInformationResult.DTCFaultCounter.GetFaultCounter "Link to this definition")  
Returns the fault counter

Returns:  Fault counter of the DTC

Return type:  int

*class* DTCFaultCounterDiagResult[¶](#tts.tooling.common.diagnostic.uds.readDtcInformation.ReadDTCInformationResult.DTCFaultCounterDiagResult "Link to this definition")  
Bases: [`DiagResult`](#ttRawDiag.diag.DiagResult.DiagResult "ttRawDiag.diag.DiagResult.DiagResult (Python class) — Returns the diagnostics response.")

This class represents the result of calling a diagnostic service whose response is expected to contain a list of DTCs and fault counters, e.g. ReadDTCInformation.reportDTCFaultDetectionCounter.

GetDTCFaultList()[¶](#tts.tooling.common.diagnostic.uds.readDtcInformation.ReadDTCInformationResult.DTCFaultCounterDiagResult.GetDTCFaultList "Link to this definition")  
Returns the list of DTC faults

Returns:  List of DTCs and corresponding fault counter

Return type:  list\<[`DTCFaultCounter`](#tts.tooling.common.diagnostic.uds.readDtcInformation.ReadDTCInformationResult.DTCFaultCounter "tts.tooling.common.diagnostic.uds.readDtcInformation.ReadDTCInformationResult.DTCFaultCounter (Python class) — Bases: object")\>

*class* UserDTCListDiagResult[¶](#tts.tooling.common.diagnostic.uds.readDtcInformation.ReadDTCInformationResult.UserDTCListDiagResult "Link to this definition")  
Bases: [`DTCListDiagResult`](#tts.testModule.diag.diagObjects.DTCResult.DTCListDiagResult "tts.testModule.diag.diagObjects.DTCResult.DTCListDiagResult (Python class) — Bases: list, DiagResult")

This class represents the result of calling a diagnostic service whose response is expected to contain a memory selection, DTC status availability mask and a list of DTCs and status codes, e.g. ReadDTCInformation.reportUserDefMemoryDTCByStatusMask.

GetDTCMemorySelection()[¶](#tts.tooling.common.diagnostic.uds.readDtcInformation.ReadDTCInformationResult.UserDTCListDiagResult.GetDTCMemorySelection "Link to this definition")  
Returns the user DTC memory selection as stated in the ECU’s response

Returns:  Memory selection

Return type:  int

DTCMemorySelection[¶](#tts.tooling.common.diagnostic.uds.readDtcInformation.ReadDTCInformationResult.UserDTCListDiagResult.DTCMemorySelection "Link to this definition")  
Returns the user DTC memory selection as stated in the ECU’s response

Returns:  Memory selection

Return type:  int

### ReadMemoryByAddress[¶](#module-tts.tooling.common.diagnostic.uds.readMemoryByAddress.ReadMemoryByAddressResult "Link to this heading")

*class* MemoryDiagResult[¶](#tts.tooling.common.diagnostic.uds.readMemoryByAddress.ReadMemoryByAddressResult.MemoryDiagResult "Link to this definition")  
Bases: [`DiagResult`](#ttRawDiag.diag.DiagResult.DiagResult "ttRawDiag.diag.DiagResult.DiagResult (Python class) — Returns the diagnostics response.")

This class represents the result of a successful readMemoryByAddress (0x23) call, consisting of the data record.

GetDataRecord()[¶](#tts.tooling.common.diagnostic.uds.readMemoryByAddress.ReadMemoryByAddressResult.MemoryDiagResult.GetDataRecord "Link to this definition")  
Returns the data record

Returns:  Data record

Return type:  [`BitStream`](variabledatastructures.html#tts.lib.dataStructures.BitStream.BitStream "tts.lib.dataStructures.BitStream.BitStream (Python class) — The BitStream type is used to represent binary data. It is possible to represent leading zeros (in contrast to plain integers), as BitStream objects have a defined length. The BitStream type supports binary operations (in contrast to plain strings), sequence operations and checking for equality. When a binary operator has operands with different size, it pads the "shorter" BitStream with zeros until its size matches the size of the "larger" BitStream.")

### RoutineControl[¶](#module-tts.tooling.common.diagnostic.uds.routineControl.RoutineControlResult "Link to this heading")

*class* RoutineDiagResult[¶](#tts.tooling.common.diagnostic.uds.routineControl.RoutineControlResult.RoutineDiagResult "Link to this definition")  
Bases: [`DiagResult`](#ttRawDiag.diag.DiagResult.DiagResult "ttRawDiag.diag.DiagResult.DiagResult (Python class) — Returns the diagnostics response.")

This class represents the result of a successful RoutineControl (0x31) call, consisting of the routine info and the routine status record.

GetRoutineControlType()[¶](#tts.tooling.common.diagnostic.uds.routineControl.RoutineControlResult.RoutineDiagResult.GetRoutineControlType "Link to this definition")  
Returns the routine control type

Returns:  Routine Control Type

Return type:  int

GetRoutineId()[¶](#tts.tooling.common.diagnostic.uds.routineControl.RoutineControlResult.RoutineDiagResult.GetRoutineId "Link to this definition")  
Returns the routine id

Returns:  Routine Id

Return type:  int

GetRoutineInfo()[¶](#tts.tooling.common.diagnostic.uds.routineControl.RoutineControlResult.RoutineDiagResult.GetRoutineInfo "Link to this definition")  
Returns the routine info

Returns:  Routine Info

Return type:  [`BitStream`](variabledatastructures.html#tts.lib.dataStructures.BitStream.BitStream "tts.lib.dataStructures.BitStream.BitStream (Python class) — The BitStream type is used to represent binary data. It is possible to represent leading zeros (in contrast to plain integers), as BitStream objects have a defined length. The BitStream type supports binary operations (in contrast to plain strings), sequence operations and checking for equality. When a binary operator has operands with different size, it pads the "shorter" BitStream with zeros until its size matches the size of the "larger" BitStream.")

GetStatusRecord()[¶](#tts.tooling.common.diagnostic.uds.routineControl.RoutineControlResult.RoutineDiagResult.GetStatusRecord "Link to this definition")  
Returns the status record

Returns:  Status record

Return type:  [`ByteStream`](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream (Python class) — The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.")

### SecurityAccess[¶](#module-tts.tooling.common.diagnostic.commonJobs.securityAccess.SecurityAccessResult "Link to this heading")

*class* SecurityAccessDiagResult[¶](#tts.tooling.common.diagnostic.commonJobs.securityAccess.SecurityAccessResult.SecurityAccessDiagResult "Link to this definition")  
Bases: [`DiagResult`](#ttRawDiag.diag.DiagResult.DiagResult "ttRawDiag.diag.DiagResult.DiagResult (Python class) — Returns the diagnostics response.")

This class represents the result of a successful SecurityAccess (0x27) call with the subfunction requestKey. The result contains at least the seed received from the ECU. If a Seed&Key library was specified when the SecurityAccessRequestSeed job was called, the result also contains the key calculated by the Seed&Key library.

GetSecuritySeed()[¶](#tts.tooling.common.diagnostic.commonJobs.securityAccess.SecurityAccessResult.SecurityAccessDiagResult.GetSecuritySeed "Link to this definition")  
Returns the security seed of the ECU’s response

Returns:  Security seed

Return type:  [ByteStream](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream (Python class) — The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.")

GetGeneratedKey()[¶](#tts.tooling.common.diagnostic.commonJobs.securityAccess.SecurityAccessResult.SecurityAccessDiagResult.GetGeneratedKey "Link to this definition")  
Returns the security key that was generated by the Seed&Key library, if the path to the Seed&Key library was set in the parameter SeedAndKeyLibraryPath of job SecurityAccessRequestSeed. The value can be used as parameter SecurityKey of the job SecurityAccessSendKey to unlock the ECU. If no Seed&Key library was specified, None is returned.

Returns:  Generated security key

Return type:  [ByteStream](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream (Python class) — The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.")

*class* SecuritySeedDiagResult[¶](#tts.tooling.common.diagnostic.commonJobs.securityAccess.SecurityAccessResult.SecuritySeedDiagResult "Link to this definition")  
Bases: [`DiagResult`](#ttRawDiag.diag.DiagResult.DiagResult "ttRawDiag.diag.DiagResult.DiagResult (Python class) — Returns the diagnostics response.")

This class represents the result of calling the security access requestKey subfunction whose response is expected to contain a security seed.

GetSecuritySeed()[¶](#tts.tooling.common.diagnostic.commonJobs.securityAccess.SecurityAccessResult.SecuritySeedDiagResult.GetSecuritySeed "Link to this definition")  
Returns the security seed of the ECU’s response

Returns:  Security seed

Return type:  int

*class* SecurityAccessSuccessDiagResult[¶](#tts.tooling.common.diagnostic.commonJobs.securityAccess.SecurityAccessResult.SecurityAccessSuccessDiagResult "Link to this definition")  
Bases: [`DiagResult`](#ttRawDiag.diag.DiagResult.DiagResult "ttRawDiag.diag.DiagResult.DiagResult (Python class) — Returns the diagnostics response.")

This class represents the result of calling the security access sendKey subfunction.

IsAccessGranted()[¶](#tts.tooling.common.diagnostic.commonJobs.securityAccess.SecurityAccessResult.SecurityAccessSuccessDiagResult.IsAccessGranted "Link to this definition")  
Returns whether the access is granted or not.

Returns:  Whether the access is granted

Return type:  int

### WriteDataByIdentifier[¶](#module-tts.tooling.common.diagnostic.uds.writeDataByIdentifier.WriteDataByIdentifierResult "Link to this heading")

*class* WriteDataByIdentifierResult[¶](#tts.tooling.common.diagnostic.uds.writeDataByIdentifier.WriteDataByIdentifierResult.WriteDataByIdentifierResult "Link to this definition")  
Bases: [`DiagResult`](#ttRawDiag.diag.DiagResult.DiagResult "ttRawDiag.diag.DiagResult.DiagResult (Python class) — Returns the diagnostics response.")

Result of a successful WriteDataByIdentifier (0x2E) call, consisting of ID.

GetDataIdentifier()[¶](#tts.tooling.common.diagnostic.uds.writeDataByIdentifier.WriteDataByIdentifierResult.WriteDataByIdentifierResult.GetDataIdentifier "Link to this definition")  
Returns the data identifier.

Returns:  Data identifier

Return type:  int

### WriteMemoryByAddress[¶](#module-tts.tooling.common.diagnostic.uds.writeMemoryByAddress.WriteMemoryByAddressResult "Link to this heading")

*class* WriteMemoryByAddressResult[¶](#tts.tooling.common.diagnostic.uds.writeMemoryByAddress.WriteMemoryByAddressResult.WriteMemoryByAddressResult "Link to this definition")  
Bases: [`DiagResult`](#ttRawDiag.diag.DiagResult.DiagResult "ttRawDiag.diag.DiagResult.DiagResult (Python class) — Returns the diagnostics response.")

Result of a successful writeMemoryByAddress (0x3D) call, consisting of MemoryAddress and MemorySize.

GetMemoryAddress()[¶](#tts.tooling.common.diagnostic.uds.writeMemoryByAddress.WriteMemoryByAddressResult.WriteMemoryByAddressResult.GetMemoryAddress "Link to this definition")  
Returns the echo of the memory address.

Returns:  Memory address

Return type:  int

GetMemorySize()[¶](#tts.tooling.common.diagnostic.uds.writeMemoryByAddress.WriteMemoryByAddressResult.WriteMemoryByAddressResult.GetMemorySize "Link to this definition")  
Returns the echo of the memory size.

Returns:  Memory size

Return type:  int

### NegativeResponse[¶](#module-tts.tooling.common.diagnostic.NegativeResponse "Link to this heading")

*class* NegativeResponse[¶](#tts.tooling.common.diagnostic.NegativeResponse.NegativeResponse "Link to this definition")  
Bases: [`DiagResult`](#ttRawDiag.diag.DiagResult.DiagResult "ttRawDiag.diag.DiagResult.DiagResult (Python class) — Returns the diagnostics response.")

Representation of a negative UDS response.

GetUDSErrMsg()[¶](#tts.tooling.common.diagnostic.NegativeResponse.NegativeResponse.GetUDSErrMsg "Link to this definition")  
Returns the UDS error message.

Returns:  UDS error message

Return type:  str

*class* UndefinedResponse[¶](#tts.tooling.common.diagnostic.NegativeResponse.UndefinedResponse "Link to this definition")  
Bases: `object`

Im Fall, dass als Ergebniss eines Diagnoserequests ‘Undefined’ vorliegt (z.b. manueller Testabbruch) kann dies für eine schönere Meldung im Testreport in UndefinedReponse umgewandelt werden.

## KWP2000 result objects[¶](#kwp2000-result-objects "Link to this heading")

### ClearDTC[¶](#module-tts.tooling.common.diagnostic.kwp2000.clearDtc.ClearDTCResult "Link to this heading")

*class* ClearDTCResult[¶](#tts.tooling.common.diagnostic.kwp2000.clearDtc.ClearDTCResult.ClearDTCResult "Link to this definition")  
Bases: [`DiagResult`](#ttRawDiag.diag.DiagResult.DiagResult "ttRawDiag.diag.DiagResult.DiagResult (Python class) — Returns the diagnostics response.")

Result of a successful ClearDTC (0x14) call, consisting of the optional DTC group.

GetGroupOfDTCs()[¶](#tts.tooling.common.diagnostic.kwp2000.clearDtc.ClearDTCResult.ClearDTCResult.GetGroupOfDTCs "Link to this definition")  
Returns the DTC group.

Returns:  DTC group

Return type:  [`ByteStream`](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream (Python class) — The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.")

### ECUReset[¶](#diagapikwp2000ecureset "Link to this heading")

*class* ECUResetResult[¶](#tts.tooling.common.diagnostic.kwp2000.ecuReset.ECUResetResult.ECUResetResult "Link to this definition")  
Bases: [`DiagResult`](#ttRawDiag.diag.DiagResult.DiagResult "ttRawDiag.diag.DiagResult.DiagResult (Python class) — Returns the diagnostics response.")

This class represents the result of a successful ECUReset (0x11) call, consisting of the reset status.

GetResetStatus()[¶](#tts.tooling.common.diagnostic.kwp2000.ecuReset.ECUResetResult.ECUResetResult.GetResetStatus "Link to this definition")  
Returns the optional Reset Status returned by the ECU.

Returns:  Reset status

Return type:  [`ByteStream`](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream (Python class) — The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.")

### InputOutputControlByCommonIdentifier[¶](#module-tts.tooling.common.diagnostic.kwp2000.inputOutputControlByCommonIdentifier.InputOutputControlByCommonIdentifierResult "Link to this heading")

*class* InputOutputControlByCommonIdentifierResult[¶](#tts.tooling.common.diagnostic.kwp2000.inputOutputControlByCommonIdentifier.InputOutputControlByCommonIdentifierResult.InputOutputControlByCommonIdentifierResult "Link to this definition")  
Bases: [`DiagResult`](#ttRawDiag.diag.DiagResult.DiagResult "ttRawDiag.diag.DiagResult.DiagResult (Python class) — Returns the diagnostics response.")

Result of a successful InputOutputControlByCommonIdentifier (0x2F) call, consisting of ID and data. Only one set of (ID, data) is supported.

GetDataIdentifierHighByte()[¶](#tts.tooling.common.diagnostic.kwp2000.inputOutputControlByCommonIdentifier.InputOutputControlByCommonIdentifierResult.InputOutputControlByCommonIdentifierResult.GetDataIdentifierHighByte "Link to this definition")  
Returns the InputOutputCommonIdentifier (High Byte).

Returns:  InputOutputCommonIdentifier (High Byte)

Return type:  int

GetDataIdentifierLowByte()[¶](#tts.tooling.common.diagnostic.kwp2000.inputOutputControlByCommonIdentifier.InputOutputControlByCommonIdentifierResult.InputOutputControlByCommonIdentifierResult.GetDataIdentifierLowByte "Link to this definition")  
Returns the InputOutputCommonIdentifier (Low Byte).

Returns:  InputOutputCommonIdentifier (Low Byte)

Return type:  int

GetControlStatus()[¶](#tts.tooling.common.diagnostic.kwp2000.inputOutputControlByCommonIdentifier.InputOutputControlByCommonIdentifierResult.InputOutputControlByCommonIdentifierResult.GetControlStatus "Link to this definition")  
Returns the ControlStatus.

Returns:  ControlStatus

Return type:  [`ByteStream`](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream (Python class) — The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.")

### InputOutputControlByLocalIdentifier[¶](#module-tts.tooling.common.diagnostic.kwp2000.inputOutputControlByLocalIdentifier.InputOutputControlByLocalIdentifierResult "Link to this heading")

*class* InputOutputControlByLocalIdentifierResult[¶](#tts.tooling.common.diagnostic.kwp2000.inputOutputControlByLocalIdentifier.InputOutputControlByLocalIdentifierResult.InputOutputControlByLocalIdentifierResult "Link to this definition")  
Bases: [`DiagResult`](#ttRawDiag.diag.DiagResult.DiagResult "ttRawDiag.diag.DiagResult.DiagResult (Python class) — Returns the diagnostics response.")

Result of a successful InputOutputControlByLocalIdentifier (0x30) call, consisting of ID and data. Only one set of (ID, data) is supported.

GetDataIdentifier()[¶](#tts.tooling.common.diagnostic.kwp2000.inputOutputControlByLocalIdentifier.InputOutputControlByLocalIdentifierResult.InputOutputControlByLocalIdentifierResult.GetDataIdentifier "Link to this definition")  
Returns the data identifier.

Returns:  Data identifier

Return type:  int

GetControlStatus()[¶](#tts.tooling.common.diagnostic.kwp2000.inputOutputControlByLocalIdentifier.InputOutputControlByLocalIdentifierResult.InputOutputControlByLocalIdentifierResult.GetControlStatus "Link to this definition")  
Returns the ControlStatus.

Returns:  ControlStatus

Return type:  [ByteStream](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream (Python class) — The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.")

### ReadDataByCommonIdentifier[¶](#module-tts.tooling.common.diagnostic.kwp2000.readDataByCommonIdentifier.ReadDataByCommonIdentifierResult "Link to this heading")

*class* ReadDataByCommonIdentifierResult[¶](#tts.tooling.common.diagnostic.kwp2000.readDataByCommonIdentifier.ReadDataByCommonIdentifierResult.ReadDataByCommonIdentifierResult "Link to this definition")  
Bases: [`DiagResult`](#ttRawDiag.diag.DiagResult.DiagResult "ttRawDiag.diag.DiagResult.DiagResult (Python class) — Returns the diagnostics response.")

Result of a successful ReadDataByLocalIdentifier (0x22) call, consisting of ID and data. Only one set of (ID, data) is supported.

GetDataIdentifierHighByte()[¶](#tts.tooling.common.diagnostic.kwp2000.readDataByCommonIdentifier.ReadDataByCommonIdentifierResult.ReadDataByCommonIdentifierResult.GetDataIdentifierHighByte "Link to this definition")  
Returns the RecordCommonIdentifier (High Byte).

Returns:  RecordCommonIdentifier (High Byte)

Return type:  int

GetDataIdentifierLowByte()[¶](#tts.tooling.common.diagnostic.kwp2000.readDataByCommonIdentifier.ReadDataByCommonIdentifierResult.ReadDataByCommonIdentifierResult.GetDataIdentifierLowByte "Link to this definition")  
Returns the RecordCommonIdentifier (Low Byte).

Returns:  RecordCommonIdentifier (Low Byte)

Return type:  int

GetData()[¶](#tts.tooling.common.diagnostic.kwp2000.readDataByCommonIdentifier.ReadDataByCommonIdentifierResult.ReadDataByCommonIdentifierResult.GetData "Link to this definition")  
Returns the record value.

Returns:  record value

Return type:  [`ByteStream`](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream (Python class) — The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.")

### ReadDataByLocalIdentifier[¶](#module-tts.tooling.common.diagnostic.kwp2000.readDataByLocalIdentifier.ReadDataByLocalIdentifierResult "Link to this heading")

*class* ReadDataByLocalIdentifierResult[¶](#tts.tooling.common.diagnostic.kwp2000.readDataByLocalIdentifier.ReadDataByLocalIdentifierResult.ReadDataByLocalIdentifierResult "Link to this definition")  
Bases: [`DiagResult`](#ttRawDiag.diag.DiagResult.DiagResult "ttRawDiag.diag.DiagResult.DiagResult (Python class) — Returns the diagnostics response.")

Result of a successful ReadDataByLocalIdentifier (0x21) call, consisting of ID and data. Only one set of (ID, data) is supported.

GetDataIdentifier()[¶](#tts.tooling.common.diagnostic.kwp2000.readDataByLocalIdentifier.ReadDataByLocalIdentifierResult.ReadDataByLocalIdentifierResult.GetDataIdentifier "Link to this definition")  
Returns the RecordLocalIdentifier.

Returns:  RecordLocalIdentifier

Return type:  int

GetData()[¶](#tts.tooling.common.diagnostic.kwp2000.readDataByLocalIdentifier.ReadDataByLocalIdentifierResult.ReadDataByLocalIdentifierResult.GetData "Link to this definition")  
Returns the record value.

Returns:  record value

Return type:  [`ByteStream`](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream (Python class) — The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.")

### ReadDTCInformation[¶](#diagapikwp2000readdtcinformation "Link to this heading")

*class* ReadDiagnosticTroubleCodesDiagResult[¶](#tts.tooling.common.diagnostic.kwp2000.readDtcInformation.ReadDTCInformationResult.ReadDiagnosticTroubleCodesDiagResult "Link to this definition")  
Bases: [`DiagResult`](#ttRawDiag.diag.DiagResult.DiagResult "ttRawDiag.diag.DiagResult.DiagResult (Python class) — Returns the diagnostics response.")

This class represents the result of a successful ReadDiagnosticTroubleCodes (0x13) call, consisting of the number and list of DTCs.

GetDTCCount()[¶](#tts.tooling.common.diagnostic.kwp2000.readDtcInformation.ReadDTCInformationResult.ReadDiagnosticTroubleCodesDiagResult.GetDTCCount "Link to this definition")  
Returns the DTC count

Returns:  DTC count

Return type:  int

GetDTCFaultList()[¶](#tts.tooling.common.diagnostic.kwp2000.readDtcInformation.ReadDTCInformationResult.ReadDiagnosticTroubleCodesDiagResult.GetDTCFaultList "Link to this definition")  
Returns the list of DTC faults

Returns:  List of DTCs

Return type:  list\<[`DTCNumber`](#tts.testModule.diag.diagObjects.DTCResult.DTCNumber "tts.testModule.diag.diagObjects.DTCResult.DTCNumber (Python class) — Bases: object")\>

*class* ReadDiagnosticTroubleCodesAndStatusDiagResult[¶](#tts.tooling.common.diagnostic.kwp2000.readDtcInformation.ReadDTCInformationResult.ReadDiagnosticTroubleCodesAndStatusDiagResult "Link to this definition")  
Bases: [`DiagResult`](#ttRawDiag.diag.DiagResult.DiagResult "ttRawDiag.diag.DiagResult.DiagResult (Python class) — Returns the diagnostics response.")

This class represents the result of a successful ReadDiagnosticTroubleCodesByStatus (0x18) or ReadStatusOfDiagnosticTroubleCodes (0x17) call, consisting of the number and list of DTCs and status.

GetDTCCount()[¶](#tts.tooling.common.diagnostic.kwp2000.readDtcInformation.ReadDTCInformationResult.ReadDiagnosticTroubleCodesAndStatusDiagResult.GetDTCCount "Link to this definition")  
Returns the DTC count

Returns:  DTC count

Return type:  int

GetDTCFaultList()[¶](#tts.tooling.common.diagnostic.kwp2000.readDtcInformation.ReadDTCInformationResult.ReadDiagnosticTroubleCodesAndStatusDiagResult.GetDTCFaultList "Link to this definition")  
Returns the list of DTC faults

Returns:  List of DTCs and corresponding status

Return type:  list\<[`DTCAndStatusRecord`](#tts.testModule.diag.diagObjects.DTCResult.DTCAndStatusRecord "tts.testModule.diag.diagObjects.DTCResult.DTCAndStatusRecord (Python class) — Bases: DTCNumber")\>

### ReadECUIdentification[¶](#module-tts.tooling.common.diagnostic.kwp2000.readEcuIdentification.ReadECUIdentificationResult "Link to this heading")

*class* ReadECUIdentificationResult[¶](#tts.tooling.common.diagnostic.kwp2000.readEcuIdentification.ReadECUIdentificationResult.ReadECUIdentificationResult "Link to this definition")  
Bases: [`DiagResult`](#ttRawDiag.diag.DiagResult.DiagResult "ttRawDiag.diag.DiagResult.DiagResult (Python class) — Returns the diagnostics response.")

Result of a successful ReadECUIdentification (0x1A) call, consisting of ID and data. Only one set of (ID, data) is supported.

GetDataIdentifier()[¶](#tts.tooling.common.diagnostic.kwp2000.readEcuIdentification.ReadECUIdentificationResult.ReadECUIdentificationResult.GetDataIdentifier "Link to this definition")  
Returns the data identifier.

Returns:  Data identifier

Return type:  int

GetData()[¶](#tts.tooling.common.diagnostic.kwp2000.readEcuIdentification.ReadECUIdentificationResult.ReadECUIdentificationResult.GetData "Link to this definition")  
Returns the ECU identification parameters.

Returns:  ECU identification parameters

Return type:  [`ByteStream`](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream (Python class) — The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.")

### RoutineControl[¶](#diagapikwp2000routinecontrol "Link to this heading")

*class* RoutineByLocalIdentifierDiagResult[¶](#tts.tooling.common.diagnostic.kwp2000.routineControl.RoutineControlResult.RoutineByLocalIdentifierDiagResult "Link to this definition")  
Bases: [`DiagResult`](#ttRawDiag.diag.DiagResult.DiagResult "ttRawDiag.diag.DiagResult.DiagResult (Python class) — Returns the diagnostics response.")

This class represents the result of a successful RoutineByLocalIdentifier call

GetRoutineId()[¶](#tts.tooling.common.diagnostic.kwp2000.routineControl.RoutineControlResult.RoutineByLocalIdentifierDiagResult.GetRoutineId "Link to this definition")  
Returns the routine id

Returns:  Routine Id

Return type:  int

GetStatusRecord()[¶](#tts.tooling.common.diagnostic.kwp2000.routineControl.RoutineControlResult.RoutineByLocalIdentifierDiagResult.GetStatusRecord "Link to this definition")  
Returns the status record

Returns:  Status record

Return type:  [`ByteStream`](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream (Python class) — The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.")

*class* StartRoutineByLocalIdentifierDiagResult[¶](#tts.tooling.common.diagnostic.kwp2000.routineControl.RoutineControlResult.StartRoutineByLocalIdentifierDiagResult "Link to this definition")  
Bases: [`RoutineByLocalIdentifierDiagResult`](#tts.tooling.common.diagnostic.kwp2000.routineControl.RoutineControlResult.RoutineByLocalIdentifierDiagResult "tts.tooling.common.diagnostic.kwp2000.routineControl.RoutineControlResult.RoutineByLocalIdentifierDiagResult (Python class) — Bases: DiagResult")

This class represents the result of a successful StartRoutineByLocalIdentifier (0x31) call, consisting of the routine entry status.

GetEntryStatus()[¶](#tts.tooling.common.diagnostic.kwp2000.routineControl.RoutineControlResult.StartRoutineByLocalIdentifierDiagResult.GetEntryStatus "Link to this definition")  
Returns the entry status

Returns:  Entry status

Return type:  [`ByteStream`](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream (Python class) — The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.")

*class* StopRoutineByLocalIdentifierDiagResult[¶](#tts.tooling.common.diagnostic.kwp2000.routineControl.RoutineControlResult.StopRoutineByLocalIdentifierDiagResult "Link to this definition")  
Bases: [`RoutineByLocalIdentifierDiagResult`](#tts.tooling.common.diagnostic.kwp2000.routineControl.RoutineControlResult.RoutineByLocalIdentifierDiagResult "tts.tooling.common.diagnostic.kwp2000.routineControl.RoutineControlResult.RoutineByLocalIdentifierDiagResult (Python class) — Bases: DiagResult")

This class represents the result of a successful StopRoutineByLocalIdentifier (0x32) call, consisting of the routine exit status.

GetExitStatus()[¶](#tts.tooling.common.diagnostic.kwp2000.routineControl.RoutineControlResult.StopRoutineByLocalIdentifierDiagResult.GetExitStatus "Link to this definition")  
Returns the exit status

Returns:  exit status

Return type:  [`ByteStream`](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream (Python class) — The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.")

*class* RequestRoutineByLocalIdentifierDiagResult[¶](#tts.tooling.common.diagnostic.kwp2000.routineControl.RoutineControlResult.RequestRoutineByLocalIdentifierDiagResult "Link to this definition")  
Bases: [`RoutineByLocalIdentifierDiagResult`](#tts.tooling.common.diagnostic.kwp2000.routineControl.RoutineControlResult.RoutineByLocalIdentifierDiagResult "tts.tooling.common.diagnostic.kwp2000.routineControl.RoutineControlResult.RoutineByLocalIdentifierDiagResult (Python class) — Bases: DiagResult")

This class represents the result of a successful RequestRoutineByLocalIdentifier (0x33) call, consisting of the routine results.

GetRoutineResults()[¶](#tts.tooling.common.diagnostic.kwp2000.routineControl.RoutineControlResult.RequestRoutineByLocalIdentifierDiagResult.GetRoutineResults "Link to this definition")  
Returns the routine results

Returns:  Routine results

Return type:  [`ByteStream`](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream (Python class) — The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.")

### WriteDataByCommonIdentifier[¶](#module-tts.tooling.common.diagnostic.kwp2000.writeDataByCommonIdentifier.WriteDataByCommonIdentifierResult "Link to this heading")

*class* WriteDataByCommonIdentifierResult[¶](#tts.tooling.common.diagnostic.kwp2000.writeDataByCommonIdentifier.WriteDataByCommonIdentifierResult.WriteDataByCommonIdentifierResult "Link to this definition")  
Bases: [`DiagResult`](#ttRawDiag.diag.DiagResult.DiagResult "ttRawDiag.diag.DiagResult.DiagResult (Python class) — Returns the diagnostics response.")

Result of a successful WriteDataByCommonIdentifier (0x3B) call, consisting of ID.

GetDataIdentifierHighByte()[¶](#tts.tooling.common.diagnostic.kwp2000.writeDataByCommonIdentifier.WriteDataByCommonIdentifierResult.WriteDataByCommonIdentifierResult.GetDataIdentifierHighByte "Link to this definition")  
Returns the RecordCommonIdentifier (High Byte).

Returns:  RecordCommonIdentifier (High Byte)

Return type:  int

GetDataIdentifierLowByte()[¶](#tts.tooling.common.diagnostic.kwp2000.writeDataByCommonIdentifier.WriteDataByCommonIdentifierResult.WriteDataByCommonIdentifierResult.GetDataIdentifierLowByte "Link to this definition")  
Returns the RecordCommonIdentifier (Low Byte).

Returns:  RecordCommonIdentifier (Low Byte)

Return type:  int

### WriteDataByLocalIdentifier[¶](#module-tts.tooling.common.diagnostic.kwp2000.writeDataByLocalIdentifier.WriteDataByLocalIdentifierResult "Link to this heading")

*class* WriteDataByLocalIdentifierResult[¶](#tts.tooling.common.diagnostic.kwp2000.writeDataByLocalIdentifier.WriteDataByLocalIdentifierResult.WriteDataByLocalIdentifierResult "Link to this definition")  
Bases: [`DiagResult`](#ttRawDiag.diag.DiagResult.DiagResult "ttRawDiag.diag.DiagResult.DiagResult (Python class) — Returns the diagnostics response.")

Result of a successful WriteDataByLocalIdentifier (0x3B) call, consisting of ID.

GetDataIdentifier()[¶](#tts.tooling.common.diagnostic.kwp2000.writeDataByLocalIdentifier.WriteDataByLocalIdentifierResult.WriteDataByLocalIdentifierResult.GetDataIdentifier "Link to this definition")  
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

Class var TYPE_DM1:  
active DTC

Class var TYPE_DM2:  
previously active DTC

Check(*[sourceAddress](#tts.testModule.bus.busObjects.J1939.J1939DTCList.Check.sourceAddress "tts.testModule.bus.busObjects.J1939.J1939DTCList.Check.sourceAddress (Python parameter) — SourceAddress (int), TLA (string) or "ALL" (the source isn't checked)")*, *[dtcSet](#tts.testModule.bus.busObjects.J1939.J1939DTCList.Check.dtcSet "tts.testModule.bus.busObjects.J1939.J1939DTCList.Check.dtcSet (Python parameter) — List of DTCs which should be included, e.g.")=`None`*, *[conjunction](#tts.testModule.bus.busObjects.J1939.J1939DTCList.Check.conjunction "tts.testModule.bus.busObjects.J1939.J1939DTCList.Check.conjunction (Python parameter) — Possibilities for checking the dtcSet:")=`'AND'`*, *[dtcNotSet](#tts.testModule.bus.busObjects.J1939.J1939DTCList.Check.dtcNotSet "tts.testModule.bus.busObjects.J1939.J1939DTCList.Check.dtcNotSet (Python parameter) — List of DTCs which may not be included, e.g.")=`None`*, *[dtcType](#tts.testModule.bus.busObjects.J1939.J1939DTCList.Check.dtcType "tts.testModule.bus.busObjects.J1939.J1939DTCList.Check.dtcType (Python parameter) — DTC-Type ("Active", "Previously Active") or None (type is ignored)")=`None`*)[¶](#tts.testModule.bus.busObjects.J1939.J1939DTCList.Check "Link to this definition")  
Check if a set of DTCs from a specific sender is included.

Examples:

- Check that there is no DTC on ECU “ABC”

  `dtcList.Check("ABC", conjunction="ONLY")`- Check that active DTCs 203.04 and 123.03 are set on ECU “ABC”

  `dtcList.Check("ABC", ["203.04", "123.03"], "AND", dtcType="Active")`Parameters:  
sourceAddress[¶](#tts.testModule.bus.busObjects.J1939.J1939DTCList.Check.sourceAddress "Permalink to this definition")  
SourceAddress (int), TLA (string) or “ALL” (the source isn’t checked)

dtcSet=`None`[¶](#tts.testModule.bus.busObjects.J1939.J1939DTCList.Check.dtcSet "Permalink to this definition")  
List of DTCs which should be included, e.g. [“2001.11”, “2003.14”]

conjunction=`'AND'`[¶](#tts.testModule.bus.busObjects.J1939.J1939DTCList.Check.conjunction "Permalink to this definition")  
Possibilities for checking the dtcSet:

”AND”: all DTCs from dtcSet must be included, others are allowed

”ONLY”: all DTCs from dtcSet must be included, others are forbidden

”OR”: at least one DTC from dtcSet must be included, others are allowed

dtcNotSet=`None`[¶](#tts.testModule.bus.busObjects.J1939.J1939DTCList.Check.dtcNotSet "Permalink to this definition")  
List of DTCs which may not be included, e.g. [“2001.11”, “2003.14”]

dtcType=`None`[¶](#tts.testModule.bus.busObjects.J1939.J1939DTCList.Check.dtcType "Permalink to this definition")  
DTC-Type (“Active”, “Previously Active”) or None (type is ignored)

Returns:  Expectation fulfilled

Return type:  bool

*class* J1939DTC[¶](#tts.testModule.bus.busObjects.J1939.J1939DTC "Link to this definition")  
A J1939 Diagnostic response.

Class var TYPE_DM1:  
active DTC

Class var TYPE_DM2:  
previously active DTC

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

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
