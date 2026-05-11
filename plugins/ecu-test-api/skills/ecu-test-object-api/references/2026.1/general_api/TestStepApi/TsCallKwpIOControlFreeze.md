[![logo](../../_static/ecu.test.svg)](../../index.html "API  documentation") API documentation

[ Internal APIs ](../api.md)

[ Advanced operations of package variable types ](../variabledatastructures.md)

[ Advanced properties of bus-related objects ](../busdatastructures.md)

[ Bus related objects of trace analysis ](../busdatastructuresTraceanalysis.md)

[ Advanced properties of diagnostics-related objects ](../diagdatastructures.md)

[ Diagnostics related objects of trace analysis ](../diagdatastructuresTraceanalysis.md)

[ Advanced properties of media-related objects ](../mediadatastructures.md)

[ Advanced properties of DLT logging-related objects ](../dltdatastructures.md)

[ COM API ](../com-api.md)

[ REST API ](../rest-api.md)

[ Report API ](../apireport.md)

[ Object API ](../objectApi.md)

Object API

[ API entry points ](../objectApi.md#api-entry-points)

API entry points

[ API for Analysis Jobs ](../AnalysisJobApi.md)

[ API for Artifacts ](../ArtifactApi.md)

[ API for Project Components ](../ComponentApi.md)

[ API for Configurations ](../ConfigurationApi.md)

[ API for Expectations ](../ExpectationApi.md)

[ API for Expressions ](../ExpressionApi.md)

[ API for Global Mappings ](../GlobalMappingApi.md)

[ API for Mappings ](../MappingApi.md)

[ API for Multimedia Objects ](../MultimediaApi.md)

[ API for Packages ](../PackageApi.md)

[ API for Parameters ](../ParameterApi.md)

[ API for Projects ](../ProjectApi.md)

[ API for Relations ](../RelationApi.md)

[ API for Reports ](../ReportApi.md)

[ API for Report Filters ](../ReportFilterApi.md)

[ API for Settings ](../SettingsApi.md)

[ API for Signals ](../SignalApi.md)

[ API for Signal Descriptions ](../SignalDescriptionApi.md)

[ API for Signal Recordings ](../SignalRecordingApi.md)

[ API for Symbols ](../SymbolApi.md)

[ API for Test Steps ](../TestStepApi.md)

API for Test Steps

[ EdiabasArgument ](EdiabasArgument.md)

[ EdiabasResult ](EdiabasResult.md)

[ ImageFilter ](ImageFilter.md)

[ Node ](Node.md)

[ TouchInputAction ](TouchInputAction.md)

[ TsAddTrace ](TsAddTrace.md)

[ TsAlterPDUTiming ](TsAlterPDUTiming.md)

[ TsAnalysisJob ](TsAnalysisJob.md)

[ TsAssertion ](TsAssertion.md)

[ TsBitExtract ](TsBitExtract.md)

[ TsBlock ](TsBlock.md)

[ TsBreak ](TsBreak.md)

[ TsBusFirstSignalCheck ](TsBusFirstSignalCheck.md)

[ TsBusFirstSignalReset ](TsBusFirstSignalReset.md)

[ TsBusMonitoringAliveCounter ](TsBusMonitoringAliveCounter.md)

[ TsBusMonitoringChecksum ](TsBusMonitoringChecksum.md)

[ TsBusMonitoringDlc ](TsBusMonitoringDlc.md)

[ TsBusMonitoringFrameTiming ](TsBusMonitoringFrameTiming.md)

[ TsCANoeTestModuleRunner ](TsCANoeTestModuleRunner.md)

[ TsCalculation ](TsCalculation.md)

[ TsCall ](TsCall.md)

[ TsCallDiagObdOnUdsService ](TsCallDiagObdOnUdsService.md)

[ TsCallDiagService ](TsCallDiagService.md)

[ TsCallIOControl ](TsCallIOControl.md)

[ TsCallIOControlFreezeCurrentState ](TsCallIOControlFreezeCurrentState.md)

[ TsCallIOControlISOSAEReserved ](TsCallIOControlISOSAEReserved.md)

[ TsCallIOControlResetToDefault ](TsCallIOControlResetToDefault.md)

[ TsCallIOControlReturnControlToEcu ](TsCallIOControlReturnControlToEcu.md)

[ TsCallIOControlShortTermAdjustment ](TsCallIOControlShortTermAdjustment.md)

TsCallKwpIOControlFreeze [ TsCallKwpIOControlFreeze ](#)

TsCallKwpIOControlFreeze

- [C TsCallKwpIOControlFreeze ](#ApiClient.TsCallKwpIOControlFreeze)
  - [M AddParameter ](#ApiClient.TsCallKwpIOControlFreeze.AddParameter)
  - [M AddReturnValue ](#ApiClient.TsCallKwpIOControlFreeze.AddReturnValue)
  - [M AddTag ](#ApiClient.TsCallKwpIOControlFreeze.AddTag)
  - [M Clone ](#ApiClient.TsCallKwpIOControlFreeze.Clone)
  - [M DeactivateReturnValueExpectation ](#ApiClient.TsCallKwpIOControlFreeze.DeactivateReturnValueExpectation)
  - [M DeactivateReturnValueSaveIn ](#ApiClient.TsCallKwpIOControlFreeze.DeactivateReturnValueSaveIn)
  - [M DeactivateTimeOption ](#ApiClient.TsCallKwpIOControlFreeze.DeactivateTimeOption)
  - [M DeleteParameter ](#ApiClient.TsCallKwpIOControlFreeze.DeleteParameter)
  - [M DeleteReturnValue ](#ApiClient.TsCallKwpIOControlFreeze.DeleteReturnValue)
  - [M DeleteTranslatedCommentText ](#ApiClient.TsCallKwpIOControlFreeze.DeleteTranslatedCommentText)
  - [M GetActionColumnText ](#ApiClient.TsCallKwpIOControlFreeze.GetActionColumnText)
  - [M GetActiveTimeOptionType ](#ApiClient.TsCallKwpIOControlFreeze.GetActiveTimeOptionType)
  - [M GetComment ](#ApiClient.TsCallKwpIOControlFreeze.GetComment)
  - [M GetCommentColumnText ](#ApiClient.TsCallKwpIOControlFreeze.GetCommentColumnText)
  - [M GetCycleTimeExpression ](#ApiClient.TsCallKwpIOControlFreeze.GetCycleTimeExpression)
  - [M GetCyclicState ](#ApiClient.TsCallKwpIOControlFreeze.GetCyclicState)
  - [M GetError ](#ApiClient.TsCallKwpIOControlFreeze.GetError)
  - [M GetIgnoreResponse ](#ApiClient.TsCallKwpIOControlFreeze.GetIgnoreResponse)
  - [M GetIndex ](#ApiClient.TsCallKwpIOControlFreeze.GetIndex)
  - [M GetLineNo ](#ApiClient.TsCallKwpIOControlFreeze.GetLineNo)
  - [M GetMappingItemReferenceName ](#ApiClient.TsCallKwpIOControlFreeze.GetMappingItemReferenceName)
  - [M GetMinimumDuration ](#ApiClient.TsCallKwpIOControlFreeze.GetMinimumDuration)
  - [M GetMinimumDurationUnit ](#ApiClient.TsCallKwpIOControlFreeze.GetMinimumDurationUnit)
  - [M GetPacketExpectation ](#ApiClient.TsCallKwpIOControlFreeze.GetPacketExpectation)
  - [M GetParameterColumnText ](#ApiClient.TsCallKwpIOControlFreeze.GetParameterColumnText)
  - [M GetParameterNames ](#ApiClient.TsCallKwpIOControlFreeze.GetParameterNames)
  - [M GetParameterRepresentation ](#ApiClient.TsCallKwpIOControlFreeze.GetParameterRepresentation)
  - [M GetParameterUnit ](#ApiClient.TsCallKwpIOControlFreeze.GetParameterUnit)
  - [M GetParameterValue ](#ApiClient.TsCallKwpIOControlFreeze.GetParameterValue)
  - [M GetParent ](#ApiClient.TsCallKwpIOControlFreeze.GetParent)
  - [M GetPollingCycle ](#ApiClient.TsCallKwpIOControlFreeze.GetPollingCycle)
  - [M GetPollingCycleUnit ](#ApiClient.TsCallKwpIOControlFreeze.GetPollingCycleUnit)
  - [M GetReturnNames ](#ApiClient.TsCallKwpIOControlFreeze.GetReturnNames)
  - [M GetReturnValueExpectation ](#ApiClient.TsCallKwpIOControlFreeze.GetReturnValueExpectation)
  - [M GetReturnValueRepresentation ](#ApiClient.TsCallKwpIOControlFreeze.GetReturnValueRepresentation)
  - [M GetReturnValueSaveIn ](#ApiClient.TsCallKwpIOControlFreeze.GetReturnValueSaveIn)
  - [M GetReturnValueUnit ](#ApiClient.TsCallKwpIOControlFreeze.GetReturnValueUnit)
  - [M GetTags ](#ApiClient.TsCallKwpIOControlFreeze.GetTags)
  - [M GetTestManagementId ](#ApiClient.TsCallKwpIOControlFreeze.GetTestManagementId)
  - [M GetTestStepId ](#ApiClient.TsCallKwpIOControlFreeze.GetTestStepId)
  - [M GetTimeout ](#ApiClient.TsCallKwpIOControlFreeze.GetTimeout)
  - [M GetTimeoutUnit ](#ApiClient.TsCallKwpIOControlFreeze.GetTimeoutUnit)
  - [M GetTranslatedCommentText ](#ApiClient.TsCallKwpIOControlFreeze.GetTranslatedCommentText)
  - [M GetType ](#ApiClient.TsCallKwpIOControlFreeze.GetType)
  - [M GetValueColumnText ](#ApiClient.TsCallKwpIOControlFreeze.GetValueColumnText)
  - [M IsBreakpoint ](#ApiClient.TsCallKwpIOControlFreeze.IsBreakpoint)
  - [M IsContainer ](#ApiClient.TsCallKwpIOControlFreeze.IsContainer)
  - [M IsEnabled ](#ApiClient.TsCallKwpIOControlFreeze.IsEnabled)
  - [M IsInPostcondition ](#ApiClient.TsCallKwpIOControlFreeze.IsInPostcondition)
  - [M IsInPrecondition ](#ApiClient.TsCallKwpIOControlFreeze.IsInPrecondition)
  - [M IsOk ](#ApiClient.TsCallKwpIOControlFreeze.IsOk)
  - [M IsVisible ](#ApiClient.TsCallKwpIOControlFreeze.IsVisible)
  - [M RemovePacketExpectation ](#ApiClient.TsCallKwpIOControlFreeze.RemovePacketExpectation)
  - [M RemoveTag ](#ApiClient.TsCallKwpIOControlFreeze.RemoveTag)
  - [M SetBreakpoint ](#ApiClient.TsCallKwpIOControlFreeze.SetBreakpoint)
  - [M SetComment ](#ApiClient.TsCallKwpIOControlFreeze.SetComment)
  - [M SetCyclic ](#ApiClient.TsCallKwpIOControlFreeze.SetCyclic)
  - [M SetEnabled ](#ApiClient.TsCallKwpIOControlFreeze.SetEnabled)
  - [M SetIgnoreResponse ](#ApiClient.TsCallKwpIOControlFreeze.SetIgnoreResponse)
  - [M SetPacketExpectation ](#ApiClient.TsCallKwpIOControlFreeze.SetPacketExpectation)
  - [M SetParameterRepresentation ](#ApiClient.TsCallKwpIOControlFreeze.SetParameterRepresentation)
  - [M SetParameterUnit ](#ApiClient.TsCallKwpIOControlFreeze.SetParameterUnit)
  - [M SetParameterValue ](#ApiClient.TsCallKwpIOControlFreeze.SetParameterValue)
  - [M SetReturnValueExpectation ](#ApiClient.TsCallKwpIOControlFreeze.SetReturnValueExpectation)
  - [M SetReturnValueRepresentation ](#ApiClient.TsCallKwpIOControlFreeze.SetReturnValueRepresentation)
  - [M SetReturnValueSaveIn ](#ApiClient.TsCallKwpIOControlFreeze.SetReturnValueSaveIn)
  - [M SetReturnValueUnit ](#ApiClient.TsCallKwpIOControlFreeze.SetReturnValueUnit)
  - [M SetTags ](#ApiClient.TsCallKwpIOControlFreeze.SetTags)
  - [M SetTestManagementId ](#ApiClient.TsCallKwpIOControlFreeze.SetTestManagementId)
  - [M SetTimeOptionOnlySynchronization ](#ApiClient.TsCallKwpIOControlFreeze.SetTimeOptionOnlySynchronization)
  - [M SetTimeOptionPollingCycleMultiplier ](#ApiClient.TsCallKwpIOControlFreeze.SetTimeOptionPollingCycleMultiplier)
  - [M SetTimeOptionTrueForAtLeast ](#ApiClient.TsCallKwpIOControlFreeze.SetTimeOptionTrueForAtLeast)
  - [M SetTimeOptionTrueForAtLeastWithin ](#ApiClient.TsCallKwpIOControlFreeze.SetTimeOptionTrueForAtLeastWithin)
  - [M SetTimeOptionWaitUntilTrue ](#ApiClient.TsCallKwpIOControlFreeze.SetTimeOptionWaitUntilTrue)
  - [M SetTranslatedCommentText ](#ApiClient.TsCallKwpIOControlFreeze.SetTranslatedCommentText)
  - [M UpdateInterface ](#ApiClient.TsCallKwpIOControlFreeze.UpdateInterface)

[ TsCallKwpIOControlLongTermAdjustment ](TsCallKwpIOControlLongTermAdjustment.md)

[ TsCallKwpIOControlReportCurrentState ](TsCallKwpIOControlReportCurrentState.md)

[ TsCallKwpIOControlResetToDefault ](TsCallKwpIOControlResetToDefault.md)

[ TsCallKwpIOControlReturnControlToEcu ](TsCallKwpIOControlReturnControlToEcu.md)

[ TsCallKwpIOControlShortTermAdjustment ](TsCallKwpIOControlShortTermAdjustment.md)

[ TsCallProvideMethod ](TsCallProvideMethod.md)

[ TsCallRead ](TsCallRead.md)

[ TsCallWrite ](TsCallWrite.md)

[ TsCaseDefNode ](TsCaseDefNode.md)

[ TsCaseNode ](TsCaseNode.md)

[ TsCheckSimulationStatus ](TsCheckSimulationStatus.md)

[ TsClearFrameAndSignalBuffers ](TsClearFrameAndSignalBuffers.md)

[ TsComment ](TsComment.md)

[ TsContinue ](TsContinue.md)

[ TsEdiabas ](TsEdiabas.md)

[ TsEdiabasLockBlock ](TsEdiabasLockBlock.md)

[ TsEesError ](TsEesError.md)

[ TsEesErrorSet ](TsEesErrorSet.md)

[ TsExit ](TsExit.md)

[ TsIfDef ](TsIfDef.md)

[ TsIfThenElse ](TsIfThenElse.md)

[ TsImageDialog ](TsImageDialog.md)

[ TsInboxFetch ](TsInboxFetch.md)

[ TsInfoBlock ](TsInfoBlock.md)

[ TsInputDialog ](TsInputDialog.md)

[ TsJob ](TsJob.md)

[ TsKeyword ](TsKeyword.md)

[ TsKeywordArgument ](TsKeywordArgument.md)

[ TsKeywordReturn ](TsKeywordReturn.md)

[ TsLoadEnvironment ](TsLoadEnvironment.md)

[ TsLogFile ](TsLogFile.md)

[ TsLoop ](TsLoop.md)

[ TsMessageDialog ](TsMessageDialog.md)

[ TsMultiCheck ](TsMultiCheck.md)

[ TsOutboxPost ](TsOutboxPost.md)

[ TsPackage ](TsPackage.md)

[ TsPackageCall ](TsPackageCall.md)

[ TsParallelPackageCall ](TsParallelPackageCall.md)

[ TsParallelRttPackageCall ](TsParallelRttPackageCall.md)

[ TsPostconditionBlock ](TsPostconditionBlock.md)

[ TsPreconditionBlock ](TsPreconditionBlock.md)

[ TsReactOn ](TsReactOn.md)

[ TsReactOnNode ](TsReactOnNode.md)

[ TsRead ](TsRead.md)

[ TsReadAudio ](TsReadAudio.md)

[ TsReadBusSignalGroup ](TsReadBusSignalGroup.md)

[ TsReadFaultMemory ](TsReadFaultMemory.md)

[ TsReadImage ](TsReadImage.md)

[ TsReport ](TsReport.md)

[ TsRequestAnalysis ](TsRequestAnalysis.md)

[ TsResetPDUTiming ](TsResetPDUTiming.md)

[ TsRestore ](TsRestore.md)

[ TsReturn ](TsReturn.md)

[ TsRttPackageCall ](TsRttPackageCall.md)

[ TsSelectList ](TsSelectList.md)

[ TsSetTraceComment ](TsSetTraceComment.md)

[ TsSimulate ](TsSimulate.md)

[ TsStartSimulation ](TsStartSimulation.md)

[ TsStartStimulus ](TsStartStimulus.md)

[ TsStartTrace ](TsStartTrace.md)

[ TsStimulate ](TsStimulate.md)

[ TsStopOfferService ](TsStopOfferService.md)

[ TsStopSimulation ](TsStopSimulation.md)

[ TsStopStimulus ](TsStopStimulus.md)

[ TsStopTrace ](TsStopTrace.md)

[ TsSwitchCase ](TsSwitchCase.md)

[ TsSwitchDefCase ](TsSwitchDefCase.md)

[ TsTodo ](TsTodo.md)

[ TsTouchInput ](TsTouchInput.md)

[ TsTraceStepResult ](TsTraceStepResult.md)

[ TsWait ](TsWait.md)

[ TsWaitForUser ](TsWaitForUser.md)

[ TsWrite ](TsWrite.md)

[ TsWriteAudio ](TsWriteAudio.md)

[ TsWriteBusSignalGroup ](TsWriteBusSignalGroup.md)

[ TsWriteBusSignalGroupCyclic ](TsWriteBusSignalGroupCyclic.md)

[ API for Touch Inputs ](../TouchInputApi.md)

[ API for Trace Analyses ](../TraceAnalysisApi.md)

[ API for Trace Files ](../TraceFileApi.md)

[ API for Trace Step Templates ](../TraceStepTemplateApi.md)

[ API for Variables ](../VariableApi.md)

[ API for Workspaces ](../WorkspaceApi.md)

[ Trace Analysis API ](../../TraceAnalysisAPI/index.md)

[ Generator APIs ](../../generators/index.md)

[ Tools ](../../tools/index.md)

[ User test management ](../../userTestmanagement/index.md)

[ UserUtility API ](../../user-utility/user-utility.md)

[ Utility Examples ](../../user-utility/example-utilities.md)

TsCallKwpIOControlFreeze

- [C TsCallKwpIOControlFreeze ](#ApiClient.TsCallKwpIOControlFreeze)
  - [M AddParameter ](#ApiClient.TsCallKwpIOControlFreeze.AddParameter)
  - [M AddReturnValue ](#ApiClient.TsCallKwpIOControlFreeze.AddReturnValue)
  - [M AddTag ](#ApiClient.TsCallKwpIOControlFreeze.AddTag)
  - [M Clone ](#ApiClient.TsCallKwpIOControlFreeze.Clone)
  - [M DeactivateReturnValueExpectation ](#ApiClient.TsCallKwpIOControlFreeze.DeactivateReturnValueExpectation)
  - [M DeactivateReturnValueSaveIn ](#ApiClient.TsCallKwpIOControlFreeze.DeactivateReturnValueSaveIn)
  - [M DeactivateTimeOption ](#ApiClient.TsCallKwpIOControlFreeze.DeactivateTimeOption)
  - [M DeleteParameter ](#ApiClient.TsCallKwpIOControlFreeze.DeleteParameter)
  - [M DeleteReturnValue ](#ApiClient.TsCallKwpIOControlFreeze.DeleteReturnValue)
  - [M DeleteTranslatedCommentText ](#ApiClient.TsCallKwpIOControlFreeze.DeleteTranslatedCommentText)
  - [M GetActionColumnText ](#ApiClient.TsCallKwpIOControlFreeze.GetActionColumnText)
  - [M GetActiveTimeOptionType ](#ApiClient.TsCallKwpIOControlFreeze.GetActiveTimeOptionType)
  - [M GetComment ](#ApiClient.TsCallKwpIOControlFreeze.GetComment)
  - [M GetCommentColumnText ](#ApiClient.TsCallKwpIOControlFreeze.GetCommentColumnText)
  - [M GetCycleTimeExpression ](#ApiClient.TsCallKwpIOControlFreeze.GetCycleTimeExpression)
  - [M GetCyclicState ](#ApiClient.TsCallKwpIOControlFreeze.GetCyclicState)
  - [M GetError ](#ApiClient.TsCallKwpIOControlFreeze.GetError)
  - [M GetIgnoreResponse ](#ApiClient.TsCallKwpIOControlFreeze.GetIgnoreResponse)
  - [M GetIndex ](#ApiClient.TsCallKwpIOControlFreeze.GetIndex)
  - [M GetLineNo ](#ApiClient.TsCallKwpIOControlFreeze.GetLineNo)
  - [M GetMappingItemReferenceName ](#ApiClient.TsCallKwpIOControlFreeze.GetMappingItemReferenceName)
  - [M GetMinimumDuration ](#ApiClient.TsCallKwpIOControlFreeze.GetMinimumDuration)
  - [M GetMinimumDurationUnit ](#ApiClient.TsCallKwpIOControlFreeze.GetMinimumDurationUnit)
  - [M GetPacketExpectation ](#ApiClient.TsCallKwpIOControlFreeze.GetPacketExpectation)
  - [M GetParameterColumnText ](#ApiClient.TsCallKwpIOControlFreeze.GetParameterColumnText)
  - [M GetParameterNames ](#ApiClient.TsCallKwpIOControlFreeze.GetParameterNames)
  - [M GetParameterRepresentation ](#ApiClient.TsCallKwpIOControlFreeze.GetParameterRepresentation)
  - [M GetParameterUnit ](#ApiClient.TsCallKwpIOControlFreeze.GetParameterUnit)
  - [M GetParameterValue ](#ApiClient.TsCallKwpIOControlFreeze.GetParameterValue)
  - [M GetParent ](#ApiClient.TsCallKwpIOControlFreeze.GetParent)
  - [M GetPollingCycle ](#ApiClient.TsCallKwpIOControlFreeze.GetPollingCycle)
  - [M GetPollingCycleUnit ](#ApiClient.TsCallKwpIOControlFreeze.GetPollingCycleUnit)
  - [M GetReturnNames ](#ApiClient.TsCallKwpIOControlFreeze.GetReturnNames)
  - [M GetReturnValueExpectation ](#ApiClient.TsCallKwpIOControlFreeze.GetReturnValueExpectation)
  - [M GetReturnValueRepresentation ](#ApiClient.TsCallKwpIOControlFreeze.GetReturnValueRepresentation)
  - [M GetReturnValueSaveIn ](#ApiClient.TsCallKwpIOControlFreeze.GetReturnValueSaveIn)
  - [M GetReturnValueUnit ](#ApiClient.TsCallKwpIOControlFreeze.GetReturnValueUnit)
  - [M GetTags ](#ApiClient.TsCallKwpIOControlFreeze.GetTags)
  - [M GetTestManagementId ](#ApiClient.TsCallKwpIOControlFreeze.GetTestManagementId)
  - [M GetTestStepId ](#ApiClient.TsCallKwpIOControlFreeze.GetTestStepId)
  - [M GetTimeout ](#ApiClient.TsCallKwpIOControlFreeze.GetTimeout)
  - [M GetTimeoutUnit ](#ApiClient.TsCallKwpIOControlFreeze.GetTimeoutUnit)
  - [M GetTranslatedCommentText ](#ApiClient.TsCallKwpIOControlFreeze.GetTranslatedCommentText)
  - [M GetType ](#ApiClient.TsCallKwpIOControlFreeze.GetType)
  - [M GetValueColumnText ](#ApiClient.TsCallKwpIOControlFreeze.GetValueColumnText)
  - [M IsBreakpoint ](#ApiClient.TsCallKwpIOControlFreeze.IsBreakpoint)
  - [M IsContainer ](#ApiClient.TsCallKwpIOControlFreeze.IsContainer)
  - [M IsEnabled ](#ApiClient.TsCallKwpIOControlFreeze.IsEnabled)
  - [M IsInPostcondition ](#ApiClient.TsCallKwpIOControlFreeze.IsInPostcondition)
  - [M IsInPrecondition ](#ApiClient.TsCallKwpIOControlFreeze.IsInPrecondition)
  - [M IsOk ](#ApiClient.TsCallKwpIOControlFreeze.IsOk)
  - [M IsVisible ](#ApiClient.TsCallKwpIOControlFreeze.IsVisible)
  - [M RemovePacketExpectation ](#ApiClient.TsCallKwpIOControlFreeze.RemovePacketExpectation)
  - [M RemoveTag ](#ApiClient.TsCallKwpIOControlFreeze.RemoveTag)
  - [M SetBreakpoint ](#ApiClient.TsCallKwpIOControlFreeze.SetBreakpoint)
  - [M SetComment ](#ApiClient.TsCallKwpIOControlFreeze.SetComment)
  - [M SetCyclic ](#ApiClient.TsCallKwpIOControlFreeze.SetCyclic)
  - [M SetEnabled ](#ApiClient.TsCallKwpIOControlFreeze.SetEnabled)
  - [M SetIgnoreResponse ](#ApiClient.TsCallKwpIOControlFreeze.SetIgnoreResponse)
  - [M SetPacketExpectation ](#ApiClient.TsCallKwpIOControlFreeze.SetPacketExpectation)
  - [M SetParameterRepresentation ](#ApiClient.TsCallKwpIOControlFreeze.SetParameterRepresentation)
  - [M SetParameterUnit ](#ApiClient.TsCallKwpIOControlFreeze.SetParameterUnit)
  - [M SetParameterValue ](#ApiClient.TsCallKwpIOControlFreeze.SetParameterValue)
  - [M SetReturnValueExpectation ](#ApiClient.TsCallKwpIOControlFreeze.SetReturnValueExpectation)
  - [M SetReturnValueRepresentation ](#ApiClient.TsCallKwpIOControlFreeze.SetReturnValueRepresentation)
  - [M SetReturnValueSaveIn ](#ApiClient.TsCallKwpIOControlFreeze.SetReturnValueSaveIn)
  - [M SetReturnValueUnit ](#ApiClient.TsCallKwpIOControlFreeze.SetReturnValueUnit)
  - [M SetTags ](#ApiClient.TsCallKwpIOControlFreeze.SetTags)
  - [M SetTestManagementId ](#ApiClient.TsCallKwpIOControlFreeze.SetTestManagementId)
  - [M SetTimeOptionOnlySynchronization ](#ApiClient.TsCallKwpIOControlFreeze.SetTimeOptionOnlySynchronization)
  - [M SetTimeOptionPollingCycleMultiplier ](#ApiClient.TsCallKwpIOControlFreeze.SetTimeOptionPollingCycleMultiplier)
  - [M SetTimeOptionTrueForAtLeast ](#ApiClient.TsCallKwpIOControlFreeze.SetTimeOptionTrueForAtLeast)
  - [M SetTimeOptionTrueForAtLeastWithin ](#ApiClient.TsCallKwpIOControlFreeze.SetTimeOptionTrueForAtLeastWithin)
  - [M SetTimeOptionWaitUntilTrue ](#ApiClient.TsCallKwpIOControlFreeze.SetTimeOptionWaitUntilTrue)
  - [M SetTranslatedCommentText ](#ApiClient.TsCallKwpIOControlFreeze.SetTranslatedCommentText)
  - [M UpdateInterface ](#ApiClient.TsCallKwpIOControlFreeze.UpdateInterface)

# TsCallKwpIOControlFreeze[¶](#tscallkwpiocontrolfreeze "Link to this heading")

*class* TsCallKwpIOControlFreeze[¶](#ApiClient.TsCallKwpIOControlFreeze "Link to this definition")  
AddParameter(*[parameterName](#ApiClient.TsCallKwpIOControlFreeze.AddParameter.parameterName "ApiClient.TsCallKwpIOControlFreeze.AddParameter.parameterName (Python parameter) — name of the parameter")*, *[valueExpression](#ApiClient.TsCallKwpIOControlFreeze.AddParameter.valueExpression "ApiClient.TsCallKwpIOControlFreeze.AddParameter.valueExpression (Python parameter) — expression to use for the parameter's value")=`None`*, *[repr](#ApiClient.TsCallKwpIOControlFreeze.AddParameter.repr "ApiClient.TsCallKwpIOControlFreeze.AddParameter.repr (Python parameter) — Representation.")=`'PHYS'`*, *[unit](#ApiClient.TsCallKwpIOControlFreeze.AddParameter.unit "ApiClient.TsCallKwpIOControlFreeze.AddParameter.unit (Python parameter) — Unit of the parameter")=`"don't care"`*)[¶](#ApiClient.TsCallKwpIOControlFreeze.AddParameter "Link to this definition")  
Adds a parameter to the test step.

See also [`UpdateInterface()`](#ApiClient.TsCallKwpIOControlFreeze.UpdateInterface "ApiClient.TsCallKwpIOControlFreeze.UpdateInterface (Python method) — Updates the list of parameters and return values according to the assigned mapping target:") and the various `SetParameter...` methods.

Parameters:  parameterName : str[¶](#ApiClient.TsCallKwpIOControlFreeze.AddParameter.parameterName "Permalink to this definition")  
name of the parameter

valueExpression : str[¶](#ApiClient.TsCallKwpIOControlFreeze.AddParameter.valueExpression "Permalink to this definition")  
expression to use for the parameter’s value

repr : str[¶](#ApiClient.TsCallKwpIOControlFreeze.AddParameter.repr "Permalink to this definition")  
Representation. One of `~ApiClient.PHYS`, `~ApiClient.RAW`, `~ApiClient.TEXT` or `~ApiClient.BITS`

unit : str[¶](#ApiClient.TsCallKwpIOControlFreeze.AddParameter.unit "Permalink to this definition")  
Unit of the parameter

AddReturnValue(*[returnName](#ApiClient.TsCallKwpIOControlFreeze.AddReturnValue.returnName "ApiClient.TsCallKwpIOControlFreeze.AddReturnValue.returnName (Python parameter) — name of the return value")*, *[saveIn](#ApiClient.TsCallKwpIOControlFreeze.AddReturnValue.saveIn "ApiClient.TsCallKwpIOControlFreeze.AddReturnValue.saveIn (Python parameter) — name of the variable to save the return value into")=`None`*, *[expectation](#ApiClient.TsCallKwpIOControlFreeze.AddReturnValue.expectation "ApiClient.TsCallKwpIOControlFreeze.AddReturnValue.expectation (Python parameter) — Expectation for the return value")=`None`*, *[repr](#ApiClient.TsCallKwpIOControlFreeze.AddReturnValue.repr "ApiClient.TsCallKwpIOControlFreeze.AddReturnValue.repr (Python parameter) — Representation.")=`'PHYS'`*, *[unit](#ApiClient.TsCallKwpIOControlFreeze.AddReturnValue.unit "ApiClient.TsCallKwpIOControlFreeze.AddReturnValue.unit (Python parameter) — Unit of the return value")=`"don't care"`*)[¶](#ApiClient.TsCallKwpIOControlFreeze.AddReturnValue "Link to this definition")  
Adds a return value to the test step.

See also [`UpdateInterface()`](#ApiClient.TsCallKwpIOControlFreeze.UpdateInterface "ApiClient.TsCallKwpIOControlFreeze.UpdateInterface (Python method) — Updates the list of parameters and return values according to the assigned mapping target:") and the various `SetReturnValue...` methods.

Parameters:  returnName : str[¶](#ApiClient.TsCallKwpIOControlFreeze.AddReturnValue.returnName "Permalink to this definition")  
name of the return value

saveIn : str[¶](#ApiClient.TsCallKwpIOControlFreeze.AddReturnValue.saveIn "Permalink to this definition")  
name of the variable to save the return value into

expectation=`None`[¶](#ApiClient.TsCallKwpIOControlFreeze.AddReturnValue.expectation "Permalink to this definition")  
Expectation for the return value

repr : str[¶](#ApiClient.TsCallKwpIOControlFreeze.AddReturnValue.repr "Permalink to this definition")  
Representation. One of `~ApiClient.PHYS`, `~ApiClient.RAW`, `~ApiClient.TEXT` or `~ApiClient.BITS`

unit : str[¶](#ApiClient.TsCallKwpIOControlFreeze.AddReturnValue.unit "Permalink to this definition")  
Unit of the return value

AddTag(*[tag](#ApiClient.TsCallKwpIOControlFreeze.AddTag.tag "ApiClient.TsCallKwpIOControlFreeze.AddTag.tag (Python parameter) — The tag to be set")*)[¶](#ApiClient.TsCallKwpIOControlFreeze.AddTag "Link to this definition")  
Add a specific tag to this step.

Parameters:  tag : str[¶](#ApiClient.TsCallKwpIOControlFreeze.AddTag.tag "Permalink to this definition")  
The tag to be set

Clone()[¶](#ApiClient.TsCallKwpIOControlFreeze.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`TsCallKwpIOControlFreeze`](#ApiClient.TsCallKwpIOControlFreeze "ApiClient.TsCallKwpIOControlFreeze (Python class) — Adds a parameter to the test step.")

DeactivateReturnValueExpectation(*[returnName](#ApiClient.TsCallKwpIOControlFreeze.DeactivateReturnValueExpectation.returnName "ApiClient.TsCallKwpIOControlFreeze.DeactivateReturnValueExpectation.returnName (Python parameter) — name of the return value")*)[¶](#ApiClient.TsCallKwpIOControlFreeze.DeactivateReturnValueExpectation "Link to this definition")  
Deactivates the expectation for the specified return value.

If no return value with an expectation remains, also deactivates any time option that may be configured.

Parameters:  returnName : str[¶](#ApiClient.TsCallKwpIOControlFreeze.DeactivateReturnValueExpectation.returnName "Permalink to this definition")  
name of the return value

DeactivateReturnValueSaveIn(*[returnName](#ApiClient.TsCallKwpIOControlFreeze.DeactivateReturnValueSaveIn.returnName "ApiClient.TsCallKwpIOControlFreeze.DeactivateReturnValueSaveIn.returnName (Python parameter) — name of the return value")*)[¶](#ApiClient.TsCallKwpIOControlFreeze.DeactivateReturnValueSaveIn "Link to this definition")  
Deactivates the save into a variable mechanism for the specified return value

Parameters:  returnName : str[¶](#ApiClient.TsCallKwpIOControlFreeze.DeactivateReturnValueSaveIn.returnName "Permalink to this definition")  
name of the return value

DeactivateTimeOption()[¶](#ApiClient.TsCallKwpIOControlFreeze.DeactivateTimeOption "Link to this definition")  
Deactivates any time option set on the test step. This is equivalent to selecting the option “none” in the test step’s time options menu.

DeleteParameter(*[parameterName](#ApiClient.TsCallKwpIOControlFreeze.DeleteParameter.parameterName "ApiClient.TsCallKwpIOControlFreeze.DeleteParameter.parameterName (Python parameter) — name of the parameter")*)[¶](#ApiClient.TsCallKwpIOControlFreeze.DeleteParameter "Link to this definition")  
Removes a parameter from the test step.

See also [`UpdateInterface()`](#ApiClient.TsCallKwpIOControlFreeze.UpdateInterface "ApiClient.TsCallKwpIOControlFreeze.UpdateInterface (Python method) — Updates the list of parameters and return values according to the assigned mapping target:").

Parameters:  parameterName : str[¶](#ApiClient.TsCallKwpIOControlFreeze.DeleteParameter.parameterName "Permalink to this definition")  
name of the parameter

DeleteReturnValue(*[returnName](#ApiClient.TsCallKwpIOControlFreeze.DeleteReturnValue.returnName "ApiClient.TsCallKwpIOControlFreeze.DeleteReturnValue.returnName (Python parameter) — name of the return value")*)[¶](#ApiClient.TsCallKwpIOControlFreeze.DeleteReturnValue "Link to this definition")  
Removes a return value from the test step. If no return values are left after the deletion, also deactivates any time option that may be configured.

See also [`UpdateInterface()`](#ApiClient.TsCallKwpIOControlFreeze.UpdateInterface "ApiClient.TsCallKwpIOControlFreeze.UpdateInterface (Python method) — Updates the list of parameters and return values according to the assigned mapping target:").

Parameters:  returnName : str[¶](#ApiClient.TsCallKwpIOControlFreeze.DeleteReturnValue.returnName "Permalink to this definition")  
name of the return value

DeleteTranslatedCommentText(*[language](#ApiClient.TsCallKwpIOControlFreeze.DeleteTranslatedCommentText.language "ApiClient.TsCallKwpIOControlFreeze.DeleteTranslatedCommentText.language (Python parameter) — Language of the text ('en_US', 'de_DE', 'zh_CN')")*)[¶](#ApiClient.TsCallKwpIOControlFreeze.DeleteTranslatedCommentText "Link to this definition")  
Deletes a comment for the test step in the given language.

Parameters:  language : str[¶](#ApiClient.TsCallKwpIOControlFreeze.DeleteTranslatedCommentText.language "Permalink to this definition")  
Language of the text (‘en_US’, ‘de_DE’, ‘zh_CN’)

GetActionColumnText()[¶](#ApiClient.TsCallKwpIOControlFreeze.GetActionColumnText "Link to this definition")  
Returns the text value of the “action” column.

Returns:  Action column text

Return type:  str

GetActiveTimeOptionType()[¶](#ApiClient.TsCallKwpIOControlFreeze.GetActiveTimeOptionType "Link to this definition")  
Returns the type of the currently active time option.

Returns:  Type of active time option (“Timeless”, “Finally”, “TrueForWithin”, “Generally”, “SyncOnly”, “PollingCycleMultiplier”)

Return type:  string

GetComment()[¶](#ApiClient.TsCallKwpIOControlFreeze.GetComment "Link to this definition")  
Returns the comment of the test step in the current test case language.

Returns:  Comment text as shown in the comment tab

Return type:  str

GetCommentColumnText()[¶](#ApiClient.TsCallKwpIOControlFreeze.GetCommentColumnText "Link to this definition")  
Returns the text value of the “comment” column.

Returns:  Comment column text

Return type:  str

GetCycleTimeExpression()[¶](#ApiClient.TsCallKwpIOControlFreeze.GetCycleTimeExpression "Link to this definition")  
Gets the cycle time expression for this test step.

Returns:  cycle time expression in milliseconds

Return type:  str

GetCyclicState()[¶](#ApiClient.TsCallKwpIOControlFreeze.GetCyclicState "Link to this definition")  
Gets the cyclic sending state for this test step.

Returns:  ‘on’, ‘off’, ‘unchanged’ or None

Return type:  str

GetError()[¶](#ApiClient.TsCallKwpIOControlFreeze.GetError "Link to this definition")  
Returns a list of errors. Note that the error messages depend on the program language ecu.test is set to. Because of that we do not recommend to check against exact error messages, unless you are certain about the respective program language.

Returns:  List of errors

Return type:  list[str]

GetIgnoreResponse()[¶](#ApiClient.TsCallKwpIOControlFreeze.GetIgnoreResponse "Link to this definition")  
Returns test step’s option for ignoring its response.

Raises:  
**ApiError** – If not return values or ignoring the response is not supported the option does not make sense.

Returns:  Returns the value of the option.

Return type:  bool

GetIndex()[¶](#ApiClient.TsCallKwpIOControlFreeze.GetIndex "Link to this definition")  
Returns the zero based index in the parent.

Returns:  Zero based index

Return type:  integer

GetLineNo()[¶](#ApiClient.TsCallKwpIOControlFreeze.GetLineNo "Link to this definition")  
Returns the test steps line number within its test case.

Returns:  Line number

Return type:  int

GetMappingItemReferenceName()[¶](#ApiClient.TsCallKwpIOControlFreeze.GetMappingItemReferenceName "Link to this definition")  
Returns the unique reference name of the mapping item used by this test step.

Returns:  Reference name of used mapping item

Return type:  str

GetMinimumDuration()[¶](#ApiClient.TsCallKwpIOControlFreeze.GetMinimumDuration "Link to this definition")  
Returns the minimum duration of the test step’s time option, if a corresponding option has been set.

Returns:  The minimum duration, else None

Return type:  string

GetMinimumDurationUnit()[¶](#ApiClient.TsCallKwpIOControlFreeze.GetMinimumDurationUnit "Link to this definition")  
Returns the unit of the minimum duration of the test step’s time option, if a corresponding option has been set.

Returns:  The unit of the minimum duration, else None

Return type:  string

GetPacketExpectation()[¶](#ApiClient.TsCallKwpIOControlFreeze.GetPacketExpectation "Link to this definition")  
Returns the expectation for the packet

Returns:  expectation

Return type:  [`Expectation`](../ExpectationApi/Expectation.md#ApiClient.Expectation "ApiClient.Expectation (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")

GetParameterColumnText()[¶](#ApiClient.TsCallKwpIOControlFreeze.GetParameterColumnText "Link to this definition")  
Returns the text value of the “parameter” column.

Returns:  Parameter column text

Return type:  str

GetParameterNames()[¶](#ApiClient.TsCallKwpIOControlFreeze.GetParameterNames "Link to this definition")  
Returns the names of the parameters defined in the test step.

Info

If the test step was created without a mapping item, or if the data base describing the target of the mapping item was not loaded, this list is initially empty. You can use [`AddParameter()`](#ApiClient.TsCallKwpIOControlFreeze.AddParameter "ApiClient.TsCallKwpIOControlFreeze.AddParameter (Python method) — Adds a parameter to the test step.") or [`UpdateInterface()`](#ApiClient.TsCallKwpIOControlFreeze.UpdateInterface "ApiClient.TsCallKwpIOControlFreeze.UpdateInterface (Python method) — Updates the list of parameters and return values according to the assigned mapping target:") to populate it.

Returns:  Parameter names

Return type:  list[str]

GetParameterRepresentation(*[parameterName](#ApiClient.TsCallKwpIOControlFreeze.GetParameterRepresentation.parameterName "ApiClient.TsCallKwpIOControlFreeze.GetParameterRepresentation.parameterName (Python parameter) — name of the parameter")*)[¶](#ApiClient.TsCallKwpIOControlFreeze.GetParameterRepresentation "Link to this definition")  
Returns the representation used for the specified parameter

Parameters:  parameterName : str[¶](#ApiClient.TsCallKwpIOControlFreeze.GetParameterRepresentation.parameterName "Permalink to this definition")  
name of the parameter

Returns:  representation used for the parameter

Return type:  str

GetParameterUnit(*[parameterName](#ApiClient.TsCallKwpIOControlFreeze.GetParameterUnit.parameterName "ApiClient.TsCallKwpIOControlFreeze.GetParameterUnit.parameterName (Python parameter) — name of the parameter")*)[¶](#ApiClient.TsCallKwpIOControlFreeze.GetParameterUnit "Link to this definition")  
Returns the unit for the specified parameter

Parameters:  parameterName : str[¶](#ApiClient.TsCallKwpIOControlFreeze.GetParameterUnit.parameterName "Permalink to this definition")  
name of the parameter

Returns:  Unit used by the `~ApiClient.PHYS` representation for this parameter

Return type:  str

GetParameterValue(*[parameterName](#ApiClient.TsCallKwpIOControlFreeze.GetParameterValue.parameterName "ApiClient.TsCallKwpIOControlFreeze.GetParameterValue.parameterName (Python parameter) — name of the parameter")*)[¶](#ApiClient.TsCallKwpIOControlFreeze.GetParameterValue "Link to this definition")  
Returns the value expression assigned to the specified parameter

Parameters:  parameterName : str[¶](#ApiClient.TsCallKwpIOControlFreeze.GetParameterValue.parameterName "Permalink to this definition")  
name of the parameter

Returns:  value expression assigned to the parameter

Return type:  str

GetParent()[¶](#ApiClient.TsCallKwpIOControlFreeze.GetParent "Link to this definition")  
Returns the parent test step.

Returns:  The parent test step or None if it is a top level test step.

Return type:  [`TestStep`](../PackageApi/TestStep.md#ApiClient.TestStep "ApiClient.TestStep (Python class) — Add a specific tag to this step.")

GetPollingCycle()[¶](#ApiClient.TsCallKwpIOControlFreeze.GetPollingCycle "Link to this definition")  
Returns the polling cycle of the test step’s time option, if a corresponding option has been set.

Returns:  The polling cycle, else None

Return type:  string

GetPollingCycleUnit()[¶](#ApiClient.TsCallKwpIOControlFreeze.GetPollingCycleUnit "Link to this definition")  
Returns the unit of the polling cycle of the test step’s time option, if a corresponding option has been set.

Returns:  The unit of the polling cycle, else None

Return type:  string

GetReturnNames()[¶](#ApiClient.TsCallKwpIOControlFreeze.GetReturnNames "Link to this definition")  
Returns the names of the return values defined in the test step.

Info

If the test step was created without a mapping item, or if the data base describing the target of the mapping item was not loaded, this list is initially empty. You can use [`AddReturnValue()`](#ApiClient.TsCallKwpIOControlFreeze.AddReturnValue "ApiClient.TsCallKwpIOControlFreeze.AddReturnValue (Python method) — Adds a return value to the test step.") or [`UpdateInterface()`](#ApiClient.TsCallKwpIOControlFreeze.UpdateInterface "ApiClient.TsCallKwpIOControlFreeze.UpdateInterface (Python method) — Updates the list of parameters and return values according to the assigned mapping target:") to populate it.

Returns:  Return value names

Return type:  list[str]

GetReturnValueExpectation(*[returnName](#ApiClient.TsCallKwpIOControlFreeze.GetReturnValueExpectation.returnName "ApiClient.TsCallKwpIOControlFreeze.GetReturnValueExpectation.returnName (Python parameter) — name of the return value")*)[¶](#ApiClient.TsCallKwpIOControlFreeze.GetReturnValueExpectation "Link to this definition")  
Returns the expectation for the specified return value

Parameters:  returnName : str[¶](#ApiClient.TsCallKwpIOControlFreeze.GetReturnValueExpectation.returnName "Permalink to this definition")  
name of the return value

Returns:  expectation

Return type:  [`Expectation`](../ExpectationApi/Expectation.md#ApiClient.Expectation "ApiClient.Expectation (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")

GetReturnValueRepresentation(*[returnName](#ApiClient.TsCallKwpIOControlFreeze.GetReturnValueRepresentation.returnName "ApiClient.TsCallKwpIOControlFreeze.GetReturnValueRepresentation.returnName (Python parameter) — name of the return value")*)[¶](#ApiClient.TsCallKwpIOControlFreeze.GetReturnValueRepresentation "Link to this definition")  
Returns the representation used for the specified return value

Parameters:  returnName : str[¶](#ApiClient.TsCallKwpIOControlFreeze.GetReturnValueRepresentation.returnName "Permalink to this definition")  
name of the return value

Returns:  representation used for the return value

Return type:  str

GetReturnValueSaveIn(*[returnName](#ApiClient.TsCallKwpIOControlFreeze.GetReturnValueSaveIn.returnName "ApiClient.TsCallKwpIOControlFreeze.GetReturnValueSaveIn.returnName (Python parameter) — name of the return value")*)[¶](#ApiClient.TsCallKwpIOControlFreeze.GetReturnValueSaveIn "Link to this definition")  
Returns the variable name to save the specified return value in

Parameters:  returnName : str[¶](#ApiClient.TsCallKwpIOControlFreeze.GetReturnValueSaveIn.returnName "Permalink to this definition")  
name of the return value

Returns:  variable name

Return type:  str

GetReturnValueUnit(*[returnName](#ApiClient.TsCallKwpIOControlFreeze.GetReturnValueUnit.returnName "ApiClient.TsCallKwpIOControlFreeze.GetReturnValueUnit.returnName (Python parameter) — name of the return value")*)[¶](#ApiClient.TsCallKwpIOControlFreeze.GetReturnValueUnit "Link to this definition")  
Returns the unit for the specified return value

Parameters:  returnName : str[¶](#ApiClient.TsCallKwpIOControlFreeze.GetReturnValueUnit.returnName "Permalink to this definition")  
name of the return value

Returns:  Unit used by the `~ApiClient.PHYS` representation for this return value

Return type:  str

GetTags()[¶](#ApiClient.TsCallKwpIOControlFreeze.GetTags "Link to this definition")  
Returns the tags set for this step.

Returns:  A (sorted) list of tags

Return type:  list[str]

GetTestManagementId()[¶](#ApiClient.TsCallKwpIOControlFreeze.GetTestManagementId "Link to this definition")  
Returns the test management id of the test step.

Returns:  Test step id.

Return type:  str

GetTestStepId()[¶](#ApiClient.TsCallKwpIOControlFreeze.GetTestStepId "Link to this definition")  
Returns the test step id.

Returns:  test step id

Return type:  str

GetTimeout()[¶](#ApiClient.TsCallKwpIOControlFreeze.GetTimeout "Link to this definition")  
Returns the timeout of the test step’s time option, if a corresponding option has been set.

Returns:  The timeout else None

Return type:  string

GetTimeoutUnit()[¶](#ApiClient.TsCallKwpIOControlFreeze.GetTimeoutUnit "Link to this definition")  
Returns the unit of the timeout of the test step’s time option, if a corresponding option has been set.

Returns:  The unit of the timeout else None

Return type:  string

GetTranslatedCommentText(*[language](#ApiClient.TsCallKwpIOControlFreeze.GetTranslatedCommentText.language "ApiClient.TsCallKwpIOControlFreeze.GetTranslatedCommentText.language (Python parameter) — Language of the requested text ('en_US', 'de_DE', 'zh_CN')")*)[¶](#ApiClient.TsCallKwpIOControlFreeze.GetTranslatedCommentText "Link to this definition")  
Returns the text value of the “comment” column in the given language.

Parameters:  language : str[¶](#ApiClient.TsCallKwpIOControlFreeze.GetTranslatedCommentText.language "Permalink to this definition")  
Language of the requested text (‘en_US’, ‘de_DE’, ‘zh_CN’)

Returns:  Comment column text

Return type:  str

GetType()[¶](#ApiClient.TsCallKwpIOControlFreeze.GetType "Link to this definition")  
Returns the type (class name) of the test step, e.g.

- “TsPreconditionBlock”

- “TsWait”

- “TsIfThenElse”

- “TsSwitchCase”

- “TsCaseNode”

Returns:  Type (class name) of the test step

Return type:  str

GetValueColumnText()[¶](#ApiClient.TsCallKwpIOControlFreeze.GetValueColumnText "Link to this definition")  
Returns the text value of the “value” column in your current test case language.

Returns:  Value column text

Return type:  str

IsBreakpoint()[¶](#ApiClient.TsCallKwpIOControlFreeze.IsBreakpoint "Link to this definition")  
Checks whether the test step is a break point.

Returns:  True if test step is a break point, else False

Return type:  boolean

IsContainer()[¶](#ApiClient.TsCallKwpIOControlFreeze.IsContainer "Link to this definition")  
Checks whether this test step can contain test steps

Returns:  True if it can contain test steps, else False

Return type:  boolean

IsEnabled()[¶](#ApiClient.TsCallKwpIOControlFreeze.IsEnabled "Link to this definition")  
Returns the state of the test step.

Returns:  True if test step is enabled, otherwise False

Return type:  bool

IsInPostcondition()[¶](#ApiClient.TsCallKwpIOControlFreeze.IsInPostcondition "Link to this definition")  
Returns True if the test step is located in a postcondition

Returns:  True if the test step is located in a postcondition, else Flase

Return type:  bool

IsInPrecondition()[¶](#ApiClient.TsCallKwpIOControlFreeze.IsInPrecondition "Link to this definition")  
Returns True if the test step is located in a precondition

Returns:  True if the test step is located in a precondition, else False

Return type:  bool

IsOk()[¶](#ApiClient.TsCallKwpIOControlFreeze.IsOk "Link to this definition")  
Returns the internal state of correctness of the test step.

Returns:  True if no problems were found, else False

Return type:  boolean

IsVisible()[¶](#ApiClient.TsCallKwpIOControlFreeze.IsVisible "Link to this definition")  
Checks whether the test step is visible. This depends on the test step itself or a parent test step being disabled.

Returns:  True if test step is visible, else False

Return type:  boolean

RemovePacketExpectation()[¶](#ApiClient.TsCallKwpIOControlFreeze.RemovePacketExpectation "Link to this definition")  
Removes the expectation for the packet. Only applicable if this test step is mapped to a service method/event.

RemoveTag(*[tag](#ApiClient.TsCallKwpIOControlFreeze.RemoveTag.tag "ApiClient.TsCallKwpIOControlFreeze.RemoveTag.tag (Python parameter) — The tag to be removed")*)[¶](#ApiClient.TsCallKwpIOControlFreeze.RemoveTag "Link to this definition")  
Remove a specific tag from this step.

Parameters:  tag : str[¶](#ApiClient.TsCallKwpIOControlFreeze.RemoveTag.tag "Permalink to this definition")  
The tag to be removed

SetBreakpoint(*[enable](#ApiClient.TsCallKwpIOControlFreeze.SetBreakpoint.enable "ApiClient.TsCallKwpIOControlFreeze.SetBreakpoint.enable (Python parameter) — True if test step is a break point, else False")*)[¶](#ApiClient.TsCallKwpIOControlFreeze.SetBreakpoint "Link to this definition")  
Sets or unsets the test step to act as a break point.

Parameters:  enable : boolean[¶](#ApiClient.TsCallKwpIOControlFreeze.SetBreakpoint.enable "Permalink to this definition")  
True if test step is a break point, else False

SetComment(*[comment](#ApiClient.TsCallKwpIOControlFreeze.SetComment.comment "ApiClient.TsCallKwpIOControlFreeze.SetComment.comment (Python parameter) — Text to be displayed in the comment tab")*)[¶](#ApiClient.TsCallKwpIOControlFreeze.SetComment "Link to this definition")  
Sets a comment for the test step in the current test case language.

Parameters:  comment : str[¶](#ApiClient.TsCallKwpIOControlFreeze.SetComment.comment "Permalink to this definition")  
Text to be displayed in the comment tab

SetCyclic(*[cyclicState](#ApiClient.TsCallKwpIOControlFreeze.SetCyclic.cyclicState "ApiClient.TsCallKwpIOControlFreeze.SetCyclic.cyclicState (Python parameter) — possible values are:")*, *[cycleTimeExpression](#ApiClient.TsCallKwpIOControlFreeze.SetCyclic.cycleTimeExpression "ApiClient.TsCallKwpIOControlFreeze.SetCyclic.cycleTimeExpression (Python parameter) — in milliseconds, necessary for cyclicState 'on'")=`None`*)[¶](#ApiClient.TsCallKwpIOControlFreeze.SetCyclic "Link to this definition")  
Changes the send cyclic settings for a test step that has call mode ‘SEND_EVENT’

Raises:  
**ApiError** – if the test step doesn’t support cyclic sending

Parameters:  cyclicState : str[¶](#ApiClient.TsCallKwpIOControlFreeze.SetCyclic.cyclicState "Permalink to this definition")  
possible values are:

- ’on’ enables cyclic sending using the specified cycleTimeExpression

- ’off’ disables cyclic sending

- ’unchanged’ keeps cyclic sending (e.g. if just the event’s values should be changed)

- None removes cyclic settings so the test step will send the event just once

cycleTimeExpression : str[¶](#ApiClient.TsCallKwpIOControlFreeze.SetCyclic.cycleTimeExpression "Permalink to this definition")  
in milliseconds, necessary for cyclicState ‘on’

SetEnabled(*[state](#ApiClient.TsCallKwpIOControlFreeze.SetEnabled.state "ApiClient.TsCallKwpIOControlFreeze.SetEnabled.state (Python parameter) — True (Default) to enable, False to disable the test step.")=`True`*)[¶](#ApiClient.TsCallKwpIOControlFreeze.SetEnabled "Link to this definition")  
Enable or disable the test step.

Parameters:  state : bool[¶](#ApiClient.TsCallKwpIOControlFreeze.SetEnabled.state "Permalink to this definition")  
True (Default) to enable, False to disable the test step.

SetIgnoreResponse(*[ignoreResponse](#ApiClient.TsCallKwpIOControlFreeze.SetIgnoreResponse.ignoreResponse "ApiClient.TsCallKwpIOControlFreeze.SetIgnoreResponse.ignoreResponse (Python parameter) — Sets the value of the option.")*)[¶](#ApiClient.TsCallKwpIOControlFreeze.SetIgnoreResponse "Link to this definition")  
Sets test step’s option for ignoring its response.

Raises:  
**ApiError** – If not return values or ignoring the response is not supported the option does not make sense.

Parameters:  ignoreResponse : bool[¶](#ApiClient.TsCallKwpIOControlFreeze.SetIgnoreResponse.ignoreResponse "Permalink to this definition")  
Sets the value of the option.

SetPacketExpectation(*[expectationExpression](#ApiClient.TsCallKwpIOControlFreeze.SetPacketExpectation.expectationExpression "ApiClient.TsCallKwpIOControlFreeze.SetPacketExpectation.expectationExpression (Python parameter) — expectation for the return value")*)[¶](#ApiClient.TsCallKwpIOControlFreeze.SetPacketExpectation "Link to this definition")  
Sets the expectation for the packet. Only applicable if this test step is mapped to a service method/event.

This should be a [`ExpressionExpectation`](../ExpectationApi/ExpressionExpectation.md#ApiClient.ExpressionExpectation "ApiClient.ExpressionExpectation (Python class) — ExpectationApi.CreateExpressionExpectation") referencing the packet as `value`, a [`PresentExpectation`](../ExpectationApi/PresentExpectation.md#ApiClient.PresentExpectation "ApiClient.PresentExpectation (Python class) — ExpectationApi.CreatePresentExpectation"), or a [`NotPresentExpectation`](../ExpectationApi/NotPresentExpectation.md#ApiClient.NotPresentExpectation "ApiClient.NotPresentExpectation (Python class) — ExpectationApi.CreateNotPresentExpectation").

Keep in mind that the `value` object can not only be a `PacketSomeIp` but also NotPresent.

Parameters:  expectationExpression[¶](#ApiClient.TsCallKwpIOControlFreeze.SetPacketExpectation.expectationExpression "Permalink to this definition")  
expectation for the return value

SetParameterRepresentation(*[parameterName](#ApiClient.TsCallKwpIOControlFreeze.SetParameterRepresentation.parameterName "ApiClient.TsCallKwpIOControlFreeze.SetParameterRepresentation.parameterName (Python parameter) — name of the parameter")*, *[repr](#ApiClient.TsCallKwpIOControlFreeze.SetParameterRepresentation.repr "ApiClient.TsCallKwpIOControlFreeze.SetParameterRepresentation.repr (Python parameter) — representation to use for the parameter. One of ~ApiClient.PHYS, ~ApiClient.RAW, ~ApiClient.TEXT or ~ApiClient.BITS")*)[¶](#ApiClient.TsCallKwpIOControlFreeze.SetParameterRepresentation "Link to this definition")  
Sets the representation for the specified parameter

This method only works with existing parameters. To add a parameter please use [`AddParameter()`](#ApiClient.TsCallKwpIOControlFreeze.AddParameter "ApiClient.TsCallKwpIOControlFreeze.AddParameter (Python method) — Adds a parameter to the test step.")

Parameters:  parameterName : str[¶](#ApiClient.TsCallKwpIOControlFreeze.SetParameterRepresentation.parameterName "Permalink to this definition")  
name of the parameter

repr : str[¶](#ApiClient.TsCallKwpIOControlFreeze.SetParameterRepresentation.repr "Permalink to this definition")  
representation to use for the parameter. One of `~ApiClient.PHYS`, `~ApiClient.RAW`, `~ApiClient.TEXT` or `~ApiClient.BITS`

SetParameterUnit(*[parameterName](#ApiClient.TsCallKwpIOControlFreeze.SetParameterUnit.parameterName "ApiClient.TsCallKwpIOControlFreeze.SetParameterUnit.parameterName (Python parameter) — name of the parameter")*, *[unit](#ApiClient.TsCallKwpIOControlFreeze.SetParameterUnit.unit "ApiClient.TsCallKwpIOControlFreeze.SetParameterUnit.unit (Python parameter) — Unit to use for the ~ApiClient.PHYS representation for this parameter")*)[¶](#ApiClient.TsCallKwpIOControlFreeze.SetParameterUnit "Link to this definition")  
Sets the unit for the specified parameter

This method only works with existing parameters. To add a parameter please use [`AddParameter()`](#ApiClient.TsCallKwpIOControlFreeze.AddParameter "ApiClient.TsCallKwpIOControlFreeze.AddParameter (Python method) — Adds a parameter to the test step.")

Parameters:  parameterName : str[¶](#ApiClient.TsCallKwpIOControlFreeze.SetParameterUnit.parameterName "Permalink to this definition")  
name of the parameter

unit : str[¶](#ApiClient.TsCallKwpIOControlFreeze.SetParameterUnit.unit "Permalink to this definition")  
Unit to use for the `~ApiClient.PHYS` representation for this parameter

SetParameterValue(*[parameterName](#ApiClient.TsCallKwpIOControlFreeze.SetParameterValue.parameterName "ApiClient.TsCallKwpIOControlFreeze.SetParameterValue.parameterName (Python parameter) — name of the parameter")*, *[valueExpression](#ApiClient.TsCallKwpIOControlFreeze.SetParameterValue.valueExpression "ApiClient.TsCallKwpIOControlFreeze.SetParameterValue.valueExpression (Python parameter) — expression to use for the parameter's value")*)[¶](#ApiClient.TsCallKwpIOControlFreeze.SetParameterValue "Link to this definition")  
Assigns a new expression to use the specified parameter’s value

This method only works with existing parameters. To add a parameter please use [`AddParameter()`](#ApiClient.TsCallKwpIOControlFreeze.AddParameter "ApiClient.TsCallKwpIOControlFreeze.AddParameter (Python method) — Adds a parameter to the test step.")

Parameters:  parameterName : str[¶](#ApiClient.TsCallKwpIOControlFreeze.SetParameterValue.parameterName "Permalink to this definition")  
name of the parameter

valueExpression : str[¶](#ApiClient.TsCallKwpIOControlFreeze.SetParameterValue.valueExpression "Permalink to this definition")  
expression to use for the parameter’s value

SetReturnValueExpectation(*[returnName](#ApiClient.TsCallKwpIOControlFreeze.SetReturnValueExpectation.returnName "ApiClient.TsCallKwpIOControlFreeze.SetReturnValueExpectation.returnName (Python parameter) — name of the return value")*, *[expectationExpression](#ApiClient.TsCallKwpIOControlFreeze.SetReturnValueExpectation.expectationExpression "ApiClient.TsCallKwpIOControlFreeze.SetReturnValueExpectation.expectationExpression (Python parameter) — expectation for the return value")*)[¶](#ApiClient.TsCallKwpIOControlFreeze.SetReturnValueExpectation "Link to this definition")  
Sets the expectation for the specified return value.

This method only works with existing return values. To add a return value please use [`AddReturnValue()`](#ApiClient.TsCallKwpIOControlFreeze.AddReturnValue "ApiClient.TsCallKwpIOControlFreeze.AddReturnValue (Python method) — Adds a return value to the test step.")

Parameters:  returnName : str[¶](#ApiClient.TsCallKwpIOControlFreeze.SetReturnValueExpectation.returnName "Permalink to this definition")  
name of the return value

expectationExpression[¶](#ApiClient.TsCallKwpIOControlFreeze.SetReturnValueExpectation.expectationExpression "Permalink to this definition")  
expectation for the return value

SetReturnValueRepresentation(*[returnName](#ApiClient.TsCallKwpIOControlFreeze.SetReturnValueRepresentation.returnName "ApiClient.TsCallKwpIOControlFreeze.SetReturnValueRepresentation.returnName (Python parameter) — name of the return value")*, *[repr](#ApiClient.TsCallKwpIOControlFreeze.SetReturnValueRepresentation.repr "ApiClient.TsCallKwpIOControlFreeze.SetReturnValueRepresentation.repr (Python parameter) — representation to use for the return value. One of ~ApiClient.PHYS, ~ApiClient.RAW, ~ApiClient.TEXT or ~ApiClient.BITS")*)[¶](#ApiClient.TsCallKwpIOControlFreeze.SetReturnValueRepresentation "Link to this definition")  
Sets the representation for the specified return value

This method only works with existing return values. To add a return value please use [`AddReturnValue()`](#ApiClient.TsCallKwpIOControlFreeze.AddReturnValue "ApiClient.TsCallKwpIOControlFreeze.AddReturnValue (Python method) — Adds a return value to the test step.")

Parameters:  returnName : str[¶](#ApiClient.TsCallKwpIOControlFreeze.SetReturnValueRepresentation.returnName "Permalink to this definition")  
name of the return value

repr : str[¶](#ApiClient.TsCallKwpIOControlFreeze.SetReturnValueRepresentation.repr "Permalink to this definition")  
representation to use for the return value. One of `~ApiClient.PHYS`, `~ApiClient.RAW`, `~ApiClient.TEXT` or `~ApiClient.BITS`

SetReturnValueSaveIn(*[returnName](#ApiClient.TsCallKwpIOControlFreeze.SetReturnValueSaveIn.returnName "ApiClient.TsCallKwpIOControlFreeze.SetReturnValueSaveIn.returnName (Python parameter) — name of the return value")*, *[saveInVariableName](#ApiClient.TsCallKwpIOControlFreeze.SetReturnValueSaveIn.saveInVariableName "ApiClient.TsCallKwpIOControlFreeze.SetReturnValueSaveIn.saveInVariableName (Python parameter) — variable name")*)[¶](#ApiClient.TsCallKwpIOControlFreeze.SetReturnValueSaveIn "Link to this definition")  
Sets the variable name to save the specified return value in

This method only works with existing return values. To add a return value please use [`AddReturnValue()`](#ApiClient.TsCallKwpIOControlFreeze.AddReturnValue "ApiClient.TsCallKwpIOControlFreeze.AddReturnValue (Python method) — Adds a return value to the test step.")

Parameters:  returnName : str[¶](#ApiClient.TsCallKwpIOControlFreeze.SetReturnValueSaveIn.returnName "Permalink to this definition")  
name of the return value

saveInVariableName : str[¶](#ApiClient.TsCallKwpIOControlFreeze.SetReturnValueSaveIn.saveInVariableName "Permalink to this definition")  
variable name

SetReturnValueUnit(*[returnName](#ApiClient.TsCallKwpIOControlFreeze.SetReturnValueUnit.returnName "ApiClient.TsCallKwpIOControlFreeze.SetReturnValueUnit.returnName (Python parameter) — name of the return value")*, *[unit](#ApiClient.TsCallKwpIOControlFreeze.SetReturnValueUnit.unit "ApiClient.TsCallKwpIOControlFreeze.SetReturnValueUnit.unit (Python parameter) — Unit to use for the ~ApiClient.PHYS representation for this return value")*)[¶](#ApiClient.TsCallKwpIOControlFreeze.SetReturnValueUnit "Link to this definition")  
Sets the unit for the specified return value

This method only works with existing return values. To add a return value please use [`AddReturnValue()`](#ApiClient.TsCallKwpIOControlFreeze.AddReturnValue "ApiClient.TsCallKwpIOControlFreeze.AddReturnValue (Python method) — Adds a return value to the test step.")

Parameters:  returnName : str[¶](#ApiClient.TsCallKwpIOControlFreeze.SetReturnValueUnit.returnName "Permalink to this definition")  
name of the return value

unit : str[¶](#ApiClient.TsCallKwpIOControlFreeze.SetReturnValueUnit.unit "Permalink to this definition")  
Unit to use for the `~ApiClient.PHYS` representation for this return value

SetTags(*[tags](#ApiClient.TsCallKwpIOControlFreeze.SetTags.tags "ApiClient.TsCallKwpIOControlFreeze.SetTags.tags (Python parameter) — The list of tags")*)[¶](#ApiClient.TsCallKwpIOControlFreeze.SetTags "Link to this definition")  
Set the list of tags for this step. The list of tags will be sorted and stored.

Parameters:  tags : list[str][¶](#ApiClient.TsCallKwpIOControlFreeze.SetTags.tags "Permalink to this definition")  
The list of tags

SetTestManagementId(*[testManagementId](#ApiClient.TsCallKwpIOControlFreeze.SetTestManagementId.testManagementId "ApiClient.TsCallKwpIOControlFreeze.SetTestManagementId.testManagementId (Python parameter) — Test management id of the test step")*)[¶](#ApiClient.TsCallKwpIOControlFreeze.SetTestManagementId "Link to this definition")  
Sets the test management id of the test step.

Parameters:  testManagementId : str[¶](#ApiClient.TsCallKwpIOControlFreeze.SetTestManagementId.testManagementId "Permalink to this definition")  
Test management id of the test step

SetTimeOptionOnlySynchronization(*[timeout](#ApiClient.TsCallKwpIOControlFreeze.SetTimeOptionOnlySynchronization.timeout "ApiClient.TsCallKwpIOControlFreeze.SetTimeOptionOnlySynchronization.timeout (Python parameter) — The timeout to be used")*, *[pollingCycle](#ApiClient.TsCallKwpIOControlFreeze.SetTimeOptionOnlySynchronization.pollingCycle "ApiClient.TsCallKwpIOControlFreeze.SetTimeOptionOnlySynchronization.pollingCycle (Python parameter) — Optional polling cycle to be used")=`None`*, *[timeoutUnit](#ApiClient.TsCallKwpIOControlFreeze.SetTimeOptionOnlySynchronization.timeoutUnit "ApiClient.TsCallKwpIOControlFreeze.SetTimeOptionOnlySynchronization.timeoutUnit (Python parameter) — Optional unit for the timeout (ms, s, min, h or d)")=`'ms'`*, *[pollingCycleUnit](#ApiClient.TsCallKwpIOControlFreeze.SetTimeOptionOnlySynchronization.pollingCycleUnit "ApiClient.TsCallKwpIOControlFreeze.SetTimeOptionOnlySynchronization.pollingCycleUnit (Python parameter) — Optional unit for the polling cycle (ms, s, min, h or d)")=`'ms'`*)[¶](#ApiClient.TsCallKwpIOControlFreeze.SetTimeOptionOnlySynchronization "Link to this definition")  
Sets the test step’s time option to “only synchronization”.

Raises:  
**ApiError** – If no return value has an expectation, no time option can be set.

Parameters:  timeout : string[¶](#ApiClient.TsCallKwpIOControlFreeze.SetTimeOptionOnlySynchronization.timeout "Permalink to this definition")  
The timeout to be used

pollingCycle : string[¶](#ApiClient.TsCallKwpIOControlFreeze.SetTimeOptionOnlySynchronization.pollingCycle "Permalink to this definition")  
Optional polling cycle to be used

timeoutUnit : string[¶](#ApiClient.TsCallKwpIOControlFreeze.SetTimeOptionOnlySynchronization.timeoutUnit "Permalink to this definition")  
Optional unit for the timeout (ms, s, min, h or d)

pollingCycleUnit : string[¶](#ApiClient.TsCallKwpIOControlFreeze.SetTimeOptionOnlySynchronization.pollingCycleUnit "Permalink to this definition")  
Optional unit for the polling cycle (ms, s, min, h or d)

SetTimeOptionPollingCycleMultiplier(*[pollingCycleMultiplier](#ApiClient.TsCallKwpIOControlFreeze.SetTimeOptionPollingCycleMultiplier.pollingCycleMultiplier "ApiClient.TsCallKwpIOControlFreeze.SetTimeOptionPollingCycleMultiplier.pollingCycleMultiplier (Python parameter) — The polling cycle multiplier to be used.")*)[¶](#ApiClient.TsCallKwpIOControlFreeze.SetTimeOptionPollingCycleMultiplier "Link to this definition")  
Sets the test step’s time option to “polling cycle multiplier”. This option must only be used when inserting the test step into a Multi-Check!

Parameters:  pollingCycleMultiplier : string[¶](#ApiClient.TsCallKwpIOControlFreeze.SetTimeOptionPollingCycleMultiplier.pollingCycleMultiplier "Permalink to this definition")  
The polling cycle multiplier to be used.

SetTimeOptionTrueForAtLeast(*[minimumDuration](#ApiClient.TsCallKwpIOControlFreeze.SetTimeOptionTrueForAtLeast.minimumDuration "ApiClient.TsCallKwpIOControlFreeze.SetTimeOptionTrueForAtLeast.minimumDuration (Python parameter) — The minimum duration to be used")*, *[pollingCycle](#ApiClient.TsCallKwpIOControlFreeze.SetTimeOptionTrueForAtLeast.pollingCycle "ApiClient.TsCallKwpIOControlFreeze.SetTimeOptionTrueForAtLeast.pollingCycle (Python parameter) — Optional polling cycle to be used")=`None`*, *[timeoutUnit](#ApiClient.TsCallKwpIOControlFreeze.SetTimeOptionTrueForAtLeast.timeoutUnit "ApiClient.TsCallKwpIOControlFreeze.SetTimeOptionTrueForAtLeast.timeoutUnit (Python parameter) — Optional unit for the timeout (ms, s, min, h or d)")=`'ms'`*, *[pollingCycleUnit](#ApiClient.TsCallKwpIOControlFreeze.SetTimeOptionTrueForAtLeast.pollingCycleUnit "ApiClient.TsCallKwpIOControlFreeze.SetTimeOptionTrueForAtLeast.pollingCycleUnit (Python parameter) — Optional unit for the polling cycle (ms, s, min, h or d)")=`'ms'`*)[¶](#ApiClient.TsCallKwpIOControlFreeze.SetTimeOptionTrueForAtLeast "Link to this definition")  
Sets the test step’s time option to “true for at least”.

Raises:  
**ApiError** – If no return value has an expectation, no time option can be set.

Parameters:  minimumDuration : string[¶](#ApiClient.TsCallKwpIOControlFreeze.SetTimeOptionTrueForAtLeast.minimumDuration "Permalink to this definition")  
The minimum duration to be used

pollingCycle : string[¶](#ApiClient.TsCallKwpIOControlFreeze.SetTimeOptionTrueForAtLeast.pollingCycle "Permalink to this definition")  
Optional polling cycle to be used

timeoutUnit : string[¶](#ApiClient.TsCallKwpIOControlFreeze.SetTimeOptionTrueForAtLeast.timeoutUnit "Permalink to this definition")  
Optional unit for the timeout (ms, s, min, h or d)

pollingCycleUnit : string[¶](#ApiClient.TsCallKwpIOControlFreeze.SetTimeOptionTrueForAtLeast.pollingCycleUnit "Permalink to this definition")  
Optional unit for the polling cycle (ms, s, min, h or d)

SetTimeOptionTrueForAtLeastWithin(*[minimumDuration](#ApiClient.TsCallKwpIOControlFreeze.SetTimeOptionTrueForAtLeastWithin.minimumDuration "ApiClient.TsCallKwpIOControlFreeze.SetTimeOptionTrueForAtLeastWithin.minimumDuration (Python parameter) — The minimum duration to be used")*, *[timeout](#ApiClient.TsCallKwpIOControlFreeze.SetTimeOptionTrueForAtLeastWithin.timeout "ApiClient.TsCallKwpIOControlFreeze.SetTimeOptionTrueForAtLeastWithin.timeout (Python parameter) — The timeout to be used")*, *[pollingCycle](#ApiClient.TsCallKwpIOControlFreeze.SetTimeOptionTrueForAtLeastWithin.pollingCycle "ApiClient.TsCallKwpIOControlFreeze.SetTimeOptionTrueForAtLeastWithin.pollingCycle (Python parameter) — Optional polling cycle to be used")=`None`*, *[timeoutUnit](#ApiClient.TsCallKwpIOControlFreeze.SetTimeOptionTrueForAtLeastWithin.timeoutUnit "ApiClient.TsCallKwpIOControlFreeze.SetTimeOptionTrueForAtLeastWithin.timeoutUnit (Python parameter) — Optional unit for the timeout (ms, s, min, h or d)")=`'ms'`*, *[pollingCycleUnit](#ApiClient.TsCallKwpIOControlFreeze.SetTimeOptionTrueForAtLeastWithin.pollingCycleUnit "ApiClient.TsCallKwpIOControlFreeze.SetTimeOptionTrueForAtLeastWithin.pollingCycleUnit (Python parameter) — Optional unit for the polling cycle (ms, s, min, h or d)")=`'ms'`*)[¶](#ApiClient.TsCallKwpIOControlFreeze.SetTimeOptionTrueForAtLeastWithin "Link to this definition")  
Sets the test step’s time option to “true for at least … within …”.

Raises:  
**ApiError** – If no return value has an expectation, no time option can be set.

Parameters:  minimumDuration : string[¶](#ApiClient.TsCallKwpIOControlFreeze.SetTimeOptionTrueForAtLeastWithin.minimumDuration "Permalink to this definition")  
The minimum duration to be used

timeout : string[¶](#ApiClient.TsCallKwpIOControlFreeze.SetTimeOptionTrueForAtLeastWithin.timeout "Permalink to this definition")  
The timeout to be used

pollingCycle : string[¶](#ApiClient.TsCallKwpIOControlFreeze.SetTimeOptionTrueForAtLeastWithin.pollingCycle "Permalink to this definition")  
Optional polling cycle to be used

timeoutUnit : string[¶](#ApiClient.TsCallKwpIOControlFreeze.SetTimeOptionTrueForAtLeastWithin.timeoutUnit "Permalink to this definition")  
Optional unit for the timeout (ms, s, min, h or d)

pollingCycleUnit : string[¶](#ApiClient.TsCallKwpIOControlFreeze.SetTimeOptionTrueForAtLeastWithin.pollingCycleUnit "Permalink to this definition")  
Optional unit for the polling cycle (ms, s, min, h or d)

SetTimeOptionWaitUntilTrue(*[timeout](#ApiClient.TsCallKwpIOControlFreeze.SetTimeOptionWaitUntilTrue.timeout "ApiClient.TsCallKwpIOControlFreeze.SetTimeOptionWaitUntilTrue.timeout (Python parameter) — The timeout to be used")*, *[pollingCycle](#ApiClient.TsCallKwpIOControlFreeze.SetTimeOptionWaitUntilTrue.pollingCycle "ApiClient.TsCallKwpIOControlFreeze.SetTimeOptionWaitUntilTrue.pollingCycle (Python parameter) — Optional polling cycle to be used")=`None`*, *[timeoutUnit](#ApiClient.TsCallKwpIOControlFreeze.SetTimeOptionWaitUntilTrue.timeoutUnit "ApiClient.TsCallKwpIOControlFreeze.SetTimeOptionWaitUntilTrue.timeoutUnit (Python parameter) — Optional unit for the timeout (ms, s, min, h or d)")=`'ms'`*, *[pollingCycleUnit](#ApiClient.TsCallKwpIOControlFreeze.SetTimeOptionWaitUntilTrue.pollingCycleUnit "ApiClient.TsCallKwpIOControlFreeze.SetTimeOptionWaitUntilTrue.pollingCycleUnit (Python parameter) — Optional unit for the polling cycle (ms, s, min, h or d)")=`'ms'`*)[¶](#ApiClient.TsCallKwpIOControlFreeze.SetTimeOptionWaitUntilTrue "Link to this definition")  
Sets the test step’s time option to “wait until true”.

Raises:  
**ApiError** – If no return value has an expectation, no time option can be set.

Parameters:  timeout : string[¶](#ApiClient.TsCallKwpIOControlFreeze.SetTimeOptionWaitUntilTrue.timeout "Permalink to this definition")  
The timeout to be used

pollingCycle : string[¶](#ApiClient.TsCallKwpIOControlFreeze.SetTimeOptionWaitUntilTrue.pollingCycle "Permalink to this definition")  
Optional polling cycle to be used

timeoutUnit : string[¶](#ApiClient.TsCallKwpIOControlFreeze.SetTimeOptionWaitUntilTrue.timeoutUnit "Permalink to this definition")  
Optional unit for the timeout (ms, s, min, h or d)

pollingCycleUnit : string[¶](#ApiClient.TsCallKwpIOControlFreeze.SetTimeOptionWaitUntilTrue.pollingCycleUnit "Permalink to this definition")  
Optional unit for the polling cycle (ms, s, min, h or d)

SetTranslatedCommentText(*[comment](#ApiClient.TsCallKwpIOControlFreeze.SetTranslatedCommentText.comment "ApiClient.TsCallKwpIOControlFreeze.SetTranslatedCommentText.comment (Python parameter) — Text to be displayed")*, *[language](#ApiClient.TsCallKwpIOControlFreeze.SetTranslatedCommentText.language "ApiClient.TsCallKwpIOControlFreeze.SetTranslatedCommentText.language (Python parameter) — Language of the text ('en_US', 'de_DE', 'zh_CN')")*)[¶](#ApiClient.TsCallKwpIOControlFreeze.SetTranslatedCommentText "Link to this definition")  
Sets a comment for the test step in the given language.

Parameters:  comment : str[¶](#ApiClient.TsCallKwpIOControlFreeze.SetTranslatedCommentText.comment "Permalink to this definition")  
Text to be displayed

language : str[¶](#ApiClient.TsCallKwpIOControlFreeze.SetTranslatedCommentText.language "Permalink to this definition")  
Language of the text (‘en_US’, ‘de_DE’, ‘zh_CN’)

UpdateInterface()[¶](#ApiClient.TsCallKwpIOControlFreeze.UpdateInterface "Link to this definition")  
Updates the list of parameters and return values according to the assigned mapping target:

- Removes any parameters and return values not available in the assigned mapping target

- Adds any missing parameters and return values defined in the assigned mapping target. Parameters are assigned a default value. Return values are not assigned any expectation.

Parameters and return values existing in both the test step and the mapping target are left as they are, which might in some cases result in an incompatible representation or unit.

Info

This only works if the test step is associated with an appropriate mappingItem (via a package, via a global mapping, or via the `~ApiClient.mappingItem` parameter of the [`CreateTsCall()`](../TestStepApi.md#ApiClient.TestStepApi.CreateTsCall "ApiClient.TestStepApi.CreateTsCall (Python method) — Creates a call test step.") method) and the database describing the target of the mapping item is loaded.

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
