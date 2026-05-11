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

TsCallIOControl [ TsCallIOControl ](#)

TsCallIOControl

- [C TsCallIOControl ](#ApiClient.TsCallIOControl)
  - [M AddParameter ](#ApiClient.TsCallIOControl.AddParameter)
  - [M AddReturnValue ](#ApiClient.TsCallIOControl.AddReturnValue)
  - [M AddTag ](#ApiClient.TsCallIOControl.AddTag)
  - [M Clone ](#ApiClient.TsCallIOControl.Clone)
  - [M DeactivateReturnValueExpectation ](#ApiClient.TsCallIOControl.DeactivateReturnValueExpectation)
  - [M DeactivateReturnValueSaveIn ](#ApiClient.TsCallIOControl.DeactivateReturnValueSaveIn)
  - [M DeactivateTimeOption ](#ApiClient.TsCallIOControl.DeactivateTimeOption)
  - [M DeleteParameter ](#ApiClient.TsCallIOControl.DeleteParameter)
  - [M DeleteReturnValue ](#ApiClient.TsCallIOControl.DeleteReturnValue)
  - [M DeleteTranslatedCommentText ](#ApiClient.TsCallIOControl.DeleteTranslatedCommentText)
  - [M GetActionColumnText ](#ApiClient.TsCallIOControl.GetActionColumnText)
  - [M GetActiveTimeOptionType ](#ApiClient.TsCallIOControl.GetActiveTimeOptionType)
  - [M GetComment ](#ApiClient.TsCallIOControl.GetComment)
  - [M GetCommentColumnText ](#ApiClient.TsCallIOControl.GetCommentColumnText)
  - [M GetCycleTimeExpression ](#ApiClient.TsCallIOControl.GetCycleTimeExpression)
  - [M GetCyclicState ](#ApiClient.TsCallIOControl.GetCyclicState)
  - [M GetError ](#ApiClient.TsCallIOControl.GetError)
  - [M GetIgnoreResponse ](#ApiClient.TsCallIOControl.GetIgnoreResponse)
  - [M GetIndex ](#ApiClient.TsCallIOControl.GetIndex)
  - [M GetLineNo ](#ApiClient.TsCallIOControl.GetLineNo)
  - [M GetMappingItemReferenceName ](#ApiClient.TsCallIOControl.GetMappingItemReferenceName)
  - [M GetMinimumDuration ](#ApiClient.TsCallIOControl.GetMinimumDuration)
  - [M GetMinimumDurationUnit ](#ApiClient.TsCallIOControl.GetMinimumDurationUnit)
  - [M GetPacketExpectation ](#ApiClient.TsCallIOControl.GetPacketExpectation)
  - [M GetParameterColumnText ](#ApiClient.TsCallIOControl.GetParameterColumnText)
  - [M GetParameterNames ](#ApiClient.TsCallIOControl.GetParameterNames)
  - [M GetParameterRepresentation ](#ApiClient.TsCallIOControl.GetParameterRepresentation)
  - [M GetParameterUnit ](#ApiClient.TsCallIOControl.GetParameterUnit)
  - [M GetParameterValue ](#ApiClient.TsCallIOControl.GetParameterValue)
  - [M GetParent ](#ApiClient.TsCallIOControl.GetParent)
  - [M GetPollingCycle ](#ApiClient.TsCallIOControl.GetPollingCycle)
  - [M GetPollingCycleUnit ](#ApiClient.TsCallIOControl.GetPollingCycleUnit)
  - [M GetReturnNames ](#ApiClient.TsCallIOControl.GetReturnNames)
  - [M GetReturnValueExpectation ](#ApiClient.TsCallIOControl.GetReturnValueExpectation)
  - [M GetReturnValueRepresentation ](#ApiClient.TsCallIOControl.GetReturnValueRepresentation)
  - [M GetReturnValueSaveIn ](#ApiClient.TsCallIOControl.GetReturnValueSaveIn)
  - [M GetReturnValueUnit ](#ApiClient.TsCallIOControl.GetReturnValueUnit)
  - [M GetTags ](#ApiClient.TsCallIOControl.GetTags)
  - [M GetTestManagementId ](#ApiClient.TsCallIOControl.GetTestManagementId)
  - [M GetTestStepId ](#ApiClient.TsCallIOControl.GetTestStepId)
  - [M GetTimeout ](#ApiClient.TsCallIOControl.GetTimeout)
  - [M GetTimeoutUnit ](#ApiClient.TsCallIOControl.GetTimeoutUnit)
  - [M GetTranslatedCommentText ](#ApiClient.TsCallIOControl.GetTranslatedCommentText)
  - [M GetType ](#ApiClient.TsCallIOControl.GetType)
  - [M GetValueColumnText ](#ApiClient.TsCallIOControl.GetValueColumnText)
  - [M IsBreakpoint ](#ApiClient.TsCallIOControl.IsBreakpoint)
  - [M IsContainer ](#ApiClient.TsCallIOControl.IsContainer)
  - [M IsEnabled ](#ApiClient.TsCallIOControl.IsEnabled)
  - [M IsInPostcondition ](#ApiClient.TsCallIOControl.IsInPostcondition)
  - [M IsInPrecondition ](#ApiClient.TsCallIOControl.IsInPrecondition)
  - [M IsOk ](#ApiClient.TsCallIOControl.IsOk)
  - [M IsVisible ](#ApiClient.TsCallIOControl.IsVisible)
  - [M RemovePacketExpectation ](#ApiClient.TsCallIOControl.RemovePacketExpectation)
  - [M RemoveTag ](#ApiClient.TsCallIOControl.RemoveTag)
  - [M SetBreakpoint ](#ApiClient.TsCallIOControl.SetBreakpoint)
  - [M SetComment ](#ApiClient.TsCallIOControl.SetComment)
  - [M SetCyclic ](#ApiClient.TsCallIOControl.SetCyclic)
  - [M SetEnabled ](#ApiClient.TsCallIOControl.SetEnabled)
  - [M SetIgnoreResponse ](#ApiClient.TsCallIOControl.SetIgnoreResponse)
  - [M SetPacketExpectation ](#ApiClient.TsCallIOControl.SetPacketExpectation)
  - [M SetParameterRepresentation ](#ApiClient.TsCallIOControl.SetParameterRepresentation)
  - [M SetParameterUnit ](#ApiClient.TsCallIOControl.SetParameterUnit)
  - [M SetParameterValue ](#ApiClient.TsCallIOControl.SetParameterValue)
  - [M SetReturnValueExpectation ](#ApiClient.TsCallIOControl.SetReturnValueExpectation)
  - [M SetReturnValueRepresentation ](#ApiClient.TsCallIOControl.SetReturnValueRepresentation)
  - [M SetReturnValueSaveIn ](#ApiClient.TsCallIOControl.SetReturnValueSaveIn)
  - [M SetReturnValueUnit ](#ApiClient.TsCallIOControl.SetReturnValueUnit)
  - [M SetTags ](#ApiClient.TsCallIOControl.SetTags)
  - [M SetTestManagementId ](#ApiClient.TsCallIOControl.SetTestManagementId)
  - [M SetTimeOptionOnlySynchronization ](#ApiClient.TsCallIOControl.SetTimeOptionOnlySynchronization)
  - [M SetTimeOptionPollingCycleMultiplier ](#ApiClient.TsCallIOControl.SetTimeOptionPollingCycleMultiplier)
  - [M SetTimeOptionTrueForAtLeast ](#ApiClient.TsCallIOControl.SetTimeOptionTrueForAtLeast)
  - [M SetTimeOptionTrueForAtLeastWithin ](#ApiClient.TsCallIOControl.SetTimeOptionTrueForAtLeastWithin)
  - [M SetTimeOptionWaitUntilTrue ](#ApiClient.TsCallIOControl.SetTimeOptionWaitUntilTrue)
  - [M SetTranslatedCommentText ](#ApiClient.TsCallIOControl.SetTranslatedCommentText)
  - [M UpdateInterface ](#ApiClient.TsCallIOControl.UpdateInterface)

[ TsCallIOControlFreezeCurrentState ](TsCallIOControlFreezeCurrentState.md)

[ TsCallIOControlISOSAEReserved ](TsCallIOControlISOSAEReserved.md)

[ TsCallIOControlResetToDefault ](TsCallIOControlResetToDefault.md)

[ TsCallIOControlReturnControlToEcu ](TsCallIOControlReturnControlToEcu.md)

[ TsCallIOControlShortTermAdjustment ](TsCallIOControlShortTermAdjustment.md)

[ TsCallKwpIOControlFreeze ](TsCallKwpIOControlFreeze.md)

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

TsCallIOControl

- [C TsCallIOControl ](#ApiClient.TsCallIOControl)
  - [M AddParameter ](#ApiClient.TsCallIOControl.AddParameter)
  - [M AddReturnValue ](#ApiClient.TsCallIOControl.AddReturnValue)
  - [M AddTag ](#ApiClient.TsCallIOControl.AddTag)
  - [M Clone ](#ApiClient.TsCallIOControl.Clone)
  - [M DeactivateReturnValueExpectation ](#ApiClient.TsCallIOControl.DeactivateReturnValueExpectation)
  - [M DeactivateReturnValueSaveIn ](#ApiClient.TsCallIOControl.DeactivateReturnValueSaveIn)
  - [M DeactivateTimeOption ](#ApiClient.TsCallIOControl.DeactivateTimeOption)
  - [M DeleteParameter ](#ApiClient.TsCallIOControl.DeleteParameter)
  - [M DeleteReturnValue ](#ApiClient.TsCallIOControl.DeleteReturnValue)
  - [M DeleteTranslatedCommentText ](#ApiClient.TsCallIOControl.DeleteTranslatedCommentText)
  - [M GetActionColumnText ](#ApiClient.TsCallIOControl.GetActionColumnText)
  - [M GetActiveTimeOptionType ](#ApiClient.TsCallIOControl.GetActiveTimeOptionType)
  - [M GetComment ](#ApiClient.TsCallIOControl.GetComment)
  - [M GetCommentColumnText ](#ApiClient.TsCallIOControl.GetCommentColumnText)
  - [M GetCycleTimeExpression ](#ApiClient.TsCallIOControl.GetCycleTimeExpression)
  - [M GetCyclicState ](#ApiClient.TsCallIOControl.GetCyclicState)
  - [M GetError ](#ApiClient.TsCallIOControl.GetError)
  - [M GetIgnoreResponse ](#ApiClient.TsCallIOControl.GetIgnoreResponse)
  - [M GetIndex ](#ApiClient.TsCallIOControl.GetIndex)
  - [M GetLineNo ](#ApiClient.TsCallIOControl.GetLineNo)
  - [M GetMappingItemReferenceName ](#ApiClient.TsCallIOControl.GetMappingItemReferenceName)
  - [M GetMinimumDuration ](#ApiClient.TsCallIOControl.GetMinimumDuration)
  - [M GetMinimumDurationUnit ](#ApiClient.TsCallIOControl.GetMinimumDurationUnit)
  - [M GetPacketExpectation ](#ApiClient.TsCallIOControl.GetPacketExpectation)
  - [M GetParameterColumnText ](#ApiClient.TsCallIOControl.GetParameterColumnText)
  - [M GetParameterNames ](#ApiClient.TsCallIOControl.GetParameterNames)
  - [M GetParameterRepresentation ](#ApiClient.TsCallIOControl.GetParameterRepresentation)
  - [M GetParameterUnit ](#ApiClient.TsCallIOControl.GetParameterUnit)
  - [M GetParameterValue ](#ApiClient.TsCallIOControl.GetParameterValue)
  - [M GetParent ](#ApiClient.TsCallIOControl.GetParent)
  - [M GetPollingCycle ](#ApiClient.TsCallIOControl.GetPollingCycle)
  - [M GetPollingCycleUnit ](#ApiClient.TsCallIOControl.GetPollingCycleUnit)
  - [M GetReturnNames ](#ApiClient.TsCallIOControl.GetReturnNames)
  - [M GetReturnValueExpectation ](#ApiClient.TsCallIOControl.GetReturnValueExpectation)
  - [M GetReturnValueRepresentation ](#ApiClient.TsCallIOControl.GetReturnValueRepresentation)
  - [M GetReturnValueSaveIn ](#ApiClient.TsCallIOControl.GetReturnValueSaveIn)
  - [M GetReturnValueUnit ](#ApiClient.TsCallIOControl.GetReturnValueUnit)
  - [M GetTags ](#ApiClient.TsCallIOControl.GetTags)
  - [M GetTestManagementId ](#ApiClient.TsCallIOControl.GetTestManagementId)
  - [M GetTestStepId ](#ApiClient.TsCallIOControl.GetTestStepId)
  - [M GetTimeout ](#ApiClient.TsCallIOControl.GetTimeout)
  - [M GetTimeoutUnit ](#ApiClient.TsCallIOControl.GetTimeoutUnit)
  - [M GetTranslatedCommentText ](#ApiClient.TsCallIOControl.GetTranslatedCommentText)
  - [M GetType ](#ApiClient.TsCallIOControl.GetType)
  - [M GetValueColumnText ](#ApiClient.TsCallIOControl.GetValueColumnText)
  - [M IsBreakpoint ](#ApiClient.TsCallIOControl.IsBreakpoint)
  - [M IsContainer ](#ApiClient.TsCallIOControl.IsContainer)
  - [M IsEnabled ](#ApiClient.TsCallIOControl.IsEnabled)
  - [M IsInPostcondition ](#ApiClient.TsCallIOControl.IsInPostcondition)
  - [M IsInPrecondition ](#ApiClient.TsCallIOControl.IsInPrecondition)
  - [M IsOk ](#ApiClient.TsCallIOControl.IsOk)
  - [M IsVisible ](#ApiClient.TsCallIOControl.IsVisible)
  - [M RemovePacketExpectation ](#ApiClient.TsCallIOControl.RemovePacketExpectation)
  - [M RemoveTag ](#ApiClient.TsCallIOControl.RemoveTag)
  - [M SetBreakpoint ](#ApiClient.TsCallIOControl.SetBreakpoint)
  - [M SetComment ](#ApiClient.TsCallIOControl.SetComment)
  - [M SetCyclic ](#ApiClient.TsCallIOControl.SetCyclic)
  - [M SetEnabled ](#ApiClient.TsCallIOControl.SetEnabled)
  - [M SetIgnoreResponse ](#ApiClient.TsCallIOControl.SetIgnoreResponse)
  - [M SetPacketExpectation ](#ApiClient.TsCallIOControl.SetPacketExpectation)
  - [M SetParameterRepresentation ](#ApiClient.TsCallIOControl.SetParameterRepresentation)
  - [M SetParameterUnit ](#ApiClient.TsCallIOControl.SetParameterUnit)
  - [M SetParameterValue ](#ApiClient.TsCallIOControl.SetParameterValue)
  - [M SetReturnValueExpectation ](#ApiClient.TsCallIOControl.SetReturnValueExpectation)
  - [M SetReturnValueRepresentation ](#ApiClient.TsCallIOControl.SetReturnValueRepresentation)
  - [M SetReturnValueSaveIn ](#ApiClient.TsCallIOControl.SetReturnValueSaveIn)
  - [M SetReturnValueUnit ](#ApiClient.TsCallIOControl.SetReturnValueUnit)
  - [M SetTags ](#ApiClient.TsCallIOControl.SetTags)
  - [M SetTestManagementId ](#ApiClient.TsCallIOControl.SetTestManagementId)
  - [M SetTimeOptionOnlySynchronization ](#ApiClient.TsCallIOControl.SetTimeOptionOnlySynchronization)
  - [M SetTimeOptionPollingCycleMultiplier ](#ApiClient.TsCallIOControl.SetTimeOptionPollingCycleMultiplier)
  - [M SetTimeOptionTrueForAtLeast ](#ApiClient.TsCallIOControl.SetTimeOptionTrueForAtLeast)
  - [M SetTimeOptionTrueForAtLeastWithin ](#ApiClient.TsCallIOControl.SetTimeOptionTrueForAtLeastWithin)
  - [M SetTimeOptionWaitUntilTrue ](#ApiClient.TsCallIOControl.SetTimeOptionWaitUntilTrue)
  - [M SetTranslatedCommentText ](#ApiClient.TsCallIOControl.SetTranslatedCommentText)
  - [M UpdateInterface ](#ApiClient.TsCallIOControl.UpdateInterface)

# TsCallIOControl[¶](#tscalliocontrol "Link to this heading")

*class* TsCallIOControl[¶](#ApiClient.TsCallIOControl "Link to this definition")  
AddParameter(*[parameterName](#ApiClient.TsCallIOControl.AddParameter.parameterName "ApiClient.TsCallIOControl.AddParameter.parameterName (Python parameter) — name of the parameter")*, *[valueExpression](#ApiClient.TsCallIOControl.AddParameter.valueExpression "ApiClient.TsCallIOControl.AddParameter.valueExpression (Python parameter) — expression to use for the parameter's value")=`None`*, *[repr](#ApiClient.TsCallIOControl.AddParameter.repr "ApiClient.TsCallIOControl.AddParameter.repr (Python parameter) — Representation.")=`'PHYS'`*, *[unit](#ApiClient.TsCallIOControl.AddParameter.unit "ApiClient.TsCallIOControl.AddParameter.unit (Python parameter) — Unit of the parameter")=`"don't care"`*)[¶](#ApiClient.TsCallIOControl.AddParameter "Link to this definition")  
Adds a parameter to the test step.

See also [`UpdateInterface()`](#ApiClient.TsCallIOControl.UpdateInterface "ApiClient.TsCallIOControl.UpdateInterface (Python method) — Updates the list of parameters and return values according to the assigned mapping target:") and the various `SetParameter...` methods.

Parameters:  parameterName : str[¶](#ApiClient.TsCallIOControl.AddParameter.parameterName "Permalink to this definition")  
name of the parameter

valueExpression : str[¶](#ApiClient.TsCallIOControl.AddParameter.valueExpression "Permalink to this definition")  
expression to use for the parameter’s value

repr : str[¶](#ApiClient.TsCallIOControl.AddParameter.repr "Permalink to this definition")  
Representation. One of `~ApiClient.PHYS`, `~ApiClient.RAW`, `~ApiClient.TEXT` or `~ApiClient.BITS`

unit : str[¶](#ApiClient.TsCallIOControl.AddParameter.unit "Permalink to this definition")  
Unit of the parameter

AddReturnValue(*[returnName](#ApiClient.TsCallIOControl.AddReturnValue.returnName "ApiClient.TsCallIOControl.AddReturnValue.returnName (Python parameter) — name of the return value")*, *[saveIn](#ApiClient.TsCallIOControl.AddReturnValue.saveIn "ApiClient.TsCallIOControl.AddReturnValue.saveIn (Python parameter) — name of the variable to save the return value into")=`None`*, *[expectation](#ApiClient.TsCallIOControl.AddReturnValue.expectation "ApiClient.TsCallIOControl.AddReturnValue.expectation (Python parameter) — Expectation for the return value")=`None`*, *[repr](#ApiClient.TsCallIOControl.AddReturnValue.repr "ApiClient.TsCallIOControl.AddReturnValue.repr (Python parameter) — Representation.")=`'PHYS'`*, *[unit](#ApiClient.TsCallIOControl.AddReturnValue.unit "ApiClient.TsCallIOControl.AddReturnValue.unit (Python parameter) — Unit of the return value")=`"don't care"`*)[¶](#ApiClient.TsCallIOControl.AddReturnValue "Link to this definition")  
Adds a return value to the test step.

See also [`UpdateInterface()`](#ApiClient.TsCallIOControl.UpdateInterface "ApiClient.TsCallIOControl.UpdateInterface (Python method) — Updates the list of parameters and return values according to the assigned mapping target:") and the various `SetReturnValue...` methods.

Parameters:  returnName : str[¶](#ApiClient.TsCallIOControl.AddReturnValue.returnName "Permalink to this definition")  
name of the return value

saveIn : str[¶](#ApiClient.TsCallIOControl.AddReturnValue.saveIn "Permalink to this definition")  
name of the variable to save the return value into

expectation=`None`[¶](#ApiClient.TsCallIOControl.AddReturnValue.expectation "Permalink to this definition")  
Expectation for the return value

repr : str[¶](#ApiClient.TsCallIOControl.AddReturnValue.repr "Permalink to this definition")  
Representation. One of `~ApiClient.PHYS`, `~ApiClient.RAW`, `~ApiClient.TEXT` or `~ApiClient.BITS`

unit : str[¶](#ApiClient.TsCallIOControl.AddReturnValue.unit "Permalink to this definition")  
Unit of the return value

AddTag(*[tag](#ApiClient.TsCallIOControl.AddTag.tag "ApiClient.TsCallIOControl.AddTag.tag (Python parameter) — The tag to be set")*)[¶](#ApiClient.TsCallIOControl.AddTag "Link to this definition")  
Add a specific tag to this step.

Parameters:  tag : str[¶](#ApiClient.TsCallIOControl.AddTag.tag "Permalink to this definition")  
The tag to be set

Clone()[¶](#ApiClient.TsCallIOControl.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`TsCallIOControl`](#ApiClient.TsCallIOControl "ApiClient.TsCallIOControl (Python class) — Adds a parameter to the test step.")

DeactivateReturnValueExpectation(*[returnName](#ApiClient.TsCallIOControl.DeactivateReturnValueExpectation.returnName "ApiClient.TsCallIOControl.DeactivateReturnValueExpectation.returnName (Python parameter) — name of the return value")*)[¶](#ApiClient.TsCallIOControl.DeactivateReturnValueExpectation "Link to this definition")  
Deactivates the expectation for the specified return value.

If no return value with an expectation remains, also deactivates any time option that may be configured.

Parameters:  returnName : str[¶](#ApiClient.TsCallIOControl.DeactivateReturnValueExpectation.returnName "Permalink to this definition")  
name of the return value

DeactivateReturnValueSaveIn(*[returnName](#ApiClient.TsCallIOControl.DeactivateReturnValueSaveIn.returnName "ApiClient.TsCallIOControl.DeactivateReturnValueSaveIn.returnName (Python parameter) — name of the return value")*)[¶](#ApiClient.TsCallIOControl.DeactivateReturnValueSaveIn "Link to this definition")  
Deactivates the save into a variable mechanism for the specified return value

Parameters:  returnName : str[¶](#ApiClient.TsCallIOControl.DeactivateReturnValueSaveIn.returnName "Permalink to this definition")  
name of the return value

DeactivateTimeOption()[¶](#ApiClient.TsCallIOControl.DeactivateTimeOption "Link to this definition")  
Deactivates any time option set on the test step. This is equivalent to selecting the option “none” in the test step’s time options menu.

DeleteParameter(*[parameterName](#ApiClient.TsCallIOControl.DeleteParameter.parameterName "ApiClient.TsCallIOControl.DeleteParameter.parameterName (Python parameter) — name of the parameter")*)[¶](#ApiClient.TsCallIOControl.DeleteParameter "Link to this definition")  
Removes a parameter from the test step.

See also [`UpdateInterface()`](#ApiClient.TsCallIOControl.UpdateInterface "ApiClient.TsCallIOControl.UpdateInterface (Python method) — Updates the list of parameters and return values according to the assigned mapping target:").

Parameters:  parameterName : str[¶](#ApiClient.TsCallIOControl.DeleteParameter.parameterName "Permalink to this definition")  
name of the parameter

DeleteReturnValue(*[returnName](#ApiClient.TsCallIOControl.DeleteReturnValue.returnName "ApiClient.TsCallIOControl.DeleteReturnValue.returnName (Python parameter) — name of the return value")*)[¶](#ApiClient.TsCallIOControl.DeleteReturnValue "Link to this definition")  
Removes a return value from the test step. If no return values are left after the deletion, also deactivates any time option that may be configured.

See also [`UpdateInterface()`](#ApiClient.TsCallIOControl.UpdateInterface "ApiClient.TsCallIOControl.UpdateInterface (Python method) — Updates the list of parameters and return values according to the assigned mapping target:").

Parameters:  returnName : str[¶](#ApiClient.TsCallIOControl.DeleteReturnValue.returnName "Permalink to this definition")  
name of the return value

DeleteTranslatedCommentText(*[language](#ApiClient.TsCallIOControl.DeleteTranslatedCommentText.language "ApiClient.TsCallIOControl.DeleteTranslatedCommentText.language (Python parameter) — Language of the text ('en_US', 'de_DE', 'zh_CN')")*)[¶](#ApiClient.TsCallIOControl.DeleteTranslatedCommentText "Link to this definition")  
Deletes a comment for the test step in the given language.

Parameters:  language : str[¶](#ApiClient.TsCallIOControl.DeleteTranslatedCommentText.language "Permalink to this definition")  
Language of the text (‘en_US’, ‘de_DE’, ‘zh_CN’)

GetActionColumnText()[¶](#ApiClient.TsCallIOControl.GetActionColumnText "Link to this definition")  
Returns the text value of the “action” column.

Returns:  Action column text

Return type:  str

GetActiveTimeOptionType()[¶](#ApiClient.TsCallIOControl.GetActiveTimeOptionType "Link to this definition")  
Returns the type of the currently active time option.

Returns:  Type of active time option (“Timeless”, “Finally”, “TrueForWithin”, “Generally”, “SyncOnly”, “PollingCycleMultiplier”)

Return type:  string

GetComment()[¶](#ApiClient.TsCallIOControl.GetComment "Link to this definition")  
Returns the comment of the test step in the current test case language.

Returns:  Comment text as shown in the comment tab

Return type:  str

GetCommentColumnText()[¶](#ApiClient.TsCallIOControl.GetCommentColumnText "Link to this definition")  
Returns the text value of the “comment” column.

Returns:  Comment column text

Return type:  str

GetCycleTimeExpression()[¶](#ApiClient.TsCallIOControl.GetCycleTimeExpression "Link to this definition")  
Gets the cycle time expression for this test step.

Returns:  cycle time expression in milliseconds

Return type:  str

GetCyclicState()[¶](#ApiClient.TsCallIOControl.GetCyclicState "Link to this definition")  
Gets the cyclic sending state for this test step.

Returns:  ‘on’, ‘off’, ‘unchanged’ or None

Return type:  str

GetError()[¶](#ApiClient.TsCallIOControl.GetError "Link to this definition")  
Returns a list of errors. Note that the error messages depend on the program language ecu.test is set to. Because of that we do not recommend to check against exact error messages, unless you are certain about the respective program language.

Returns:  List of errors

Return type:  list[str]

GetIgnoreResponse()[¶](#ApiClient.TsCallIOControl.GetIgnoreResponse "Link to this definition")  
Returns test step’s option for ignoring its response.

Raises:  
**ApiError** – If not return values or ignoring the response is not supported the option does not make sense.

Returns:  Returns the value of the option.

Return type:  bool

GetIndex()[¶](#ApiClient.TsCallIOControl.GetIndex "Link to this definition")  
Returns the zero based index in the parent.

Returns:  Zero based index

Return type:  integer

GetLineNo()[¶](#ApiClient.TsCallIOControl.GetLineNo "Link to this definition")  
Returns the test steps line number within its test case.

Returns:  Line number

Return type:  int

GetMappingItemReferenceName()[¶](#ApiClient.TsCallIOControl.GetMappingItemReferenceName "Link to this definition")  
Returns the unique reference name of the mapping item used by this test step.

Returns:  Reference name of used mapping item

Return type:  str

GetMinimumDuration()[¶](#ApiClient.TsCallIOControl.GetMinimumDuration "Link to this definition")  
Returns the minimum duration of the test step’s time option, if a corresponding option has been set.

Returns:  The minimum duration, else None

Return type:  string

GetMinimumDurationUnit()[¶](#ApiClient.TsCallIOControl.GetMinimumDurationUnit "Link to this definition")  
Returns the unit of the minimum duration of the test step’s time option, if a corresponding option has been set.

Returns:  The unit of the minimum duration, else None

Return type:  string

GetPacketExpectation()[¶](#ApiClient.TsCallIOControl.GetPacketExpectation "Link to this definition")  
Returns the expectation for the packet

Returns:  expectation

Return type:  [`Expectation`](../ExpectationApi/Expectation.md#ApiClient.Expectation "ApiClient.Expectation (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")

GetParameterColumnText()[¶](#ApiClient.TsCallIOControl.GetParameterColumnText "Link to this definition")  
Returns the text value of the “parameter” column.

Returns:  Parameter column text

Return type:  str

GetParameterNames()[¶](#ApiClient.TsCallIOControl.GetParameterNames "Link to this definition")  
Returns the names of the parameters defined in the test step.

Info

If the test step was created without a mapping item, or if the data base describing the target of the mapping item was not loaded, this list is initially empty. You can use [`AddParameter()`](#ApiClient.TsCallIOControl.AddParameter "ApiClient.TsCallIOControl.AddParameter (Python method) — Adds a parameter to the test step.") or [`UpdateInterface()`](#ApiClient.TsCallIOControl.UpdateInterface "ApiClient.TsCallIOControl.UpdateInterface (Python method) — Updates the list of parameters and return values according to the assigned mapping target:") to populate it.

Returns:  Parameter names

Return type:  list[str]

GetParameterRepresentation(*[parameterName](#ApiClient.TsCallIOControl.GetParameterRepresentation.parameterName "ApiClient.TsCallIOControl.GetParameterRepresentation.parameterName (Python parameter) — name of the parameter")*)[¶](#ApiClient.TsCallIOControl.GetParameterRepresentation "Link to this definition")  
Returns the representation used for the specified parameter

Parameters:  parameterName : str[¶](#ApiClient.TsCallIOControl.GetParameterRepresentation.parameterName "Permalink to this definition")  
name of the parameter

Returns:  representation used for the parameter

Return type:  str

GetParameterUnit(*[parameterName](#ApiClient.TsCallIOControl.GetParameterUnit.parameterName "ApiClient.TsCallIOControl.GetParameterUnit.parameterName (Python parameter) — name of the parameter")*)[¶](#ApiClient.TsCallIOControl.GetParameterUnit "Link to this definition")  
Returns the unit for the specified parameter

Parameters:  parameterName : str[¶](#ApiClient.TsCallIOControl.GetParameterUnit.parameterName "Permalink to this definition")  
name of the parameter

Returns:  Unit used by the `~ApiClient.PHYS` representation for this parameter

Return type:  str

GetParameterValue(*[parameterName](#ApiClient.TsCallIOControl.GetParameterValue.parameterName "ApiClient.TsCallIOControl.GetParameterValue.parameterName (Python parameter) — name of the parameter")*)[¶](#ApiClient.TsCallIOControl.GetParameterValue "Link to this definition")  
Returns the value expression assigned to the specified parameter

Parameters:  parameterName : str[¶](#ApiClient.TsCallIOControl.GetParameterValue.parameterName "Permalink to this definition")  
name of the parameter

Returns:  value expression assigned to the parameter

Return type:  str

GetParent()[¶](#ApiClient.TsCallIOControl.GetParent "Link to this definition")  
Returns the parent test step.

Returns:  The parent test step or None if it is a top level test step.

Return type:  [`TestStep`](../PackageApi/TestStep.md#ApiClient.TestStep "ApiClient.TestStep (Python class) — Add a specific tag to this step.")

GetPollingCycle()[¶](#ApiClient.TsCallIOControl.GetPollingCycle "Link to this definition")  
Returns the polling cycle of the test step’s time option, if a corresponding option has been set.

Returns:  The polling cycle, else None

Return type:  string

GetPollingCycleUnit()[¶](#ApiClient.TsCallIOControl.GetPollingCycleUnit "Link to this definition")  
Returns the unit of the polling cycle of the test step’s time option, if a corresponding option has been set.

Returns:  The unit of the polling cycle, else None

Return type:  string

GetReturnNames()[¶](#ApiClient.TsCallIOControl.GetReturnNames "Link to this definition")  
Returns the names of the return values defined in the test step.

Info

If the test step was created without a mapping item, or if the data base describing the target of the mapping item was not loaded, this list is initially empty. You can use [`AddReturnValue()`](#ApiClient.TsCallIOControl.AddReturnValue "ApiClient.TsCallIOControl.AddReturnValue (Python method) — Adds a return value to the test step.") or [`UpdateInterface()`](#ApiClient.TsCallIOControl.UpdateInterface "ApiClient.TsCallIOControl.UpdateInterface (Python method) — Updates the list of parameters and return values according to the assigned mapping target:") to populate it.

Returns:  Return value names

Return type:  list[str]

GetReturnValueExpectation(*[returnName](#ApiClient.TsCallIOControl.GetReturnValueExpectation.returnName "ApiClient.TsCallIOControl.GetReturnValueExpectation.returnName (Python parameter) — name of the return value")*)[¶](#ApiClient.TsCallIOControl.GetReturnValueExpectation "Link to this definition")  
Returns the expectation for the specified return value

Parameters:  returnName : str[¶](#ApiClient.TsCallIOControl.GetReturnValueExpectation.returnName "Permalink to this definition")  
name of the return value

Returns:  expectation

Return type:  [`Expectation`](../ExpectationApi/Expectation.md#ApiClient.Expectation "ApiClient.Expectation (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")

GetReturnValueRepresentation(*[returnName](#ApiClient.TsCallIOControl.GetReturnValueRepresentation.returnName "ApiClient.TsCallIOControl.GetReturnValueRepresentation.returnName (Python parameter) — name of the return value")*)[¶](#ApiClient.TsCallIOControl.GetReturnValueRepresentation "Link to this definition")  
Returns the representation used for the specified return value

Parameters:  returnName : str[¶](#ApiClient.TsCallIOControl.GetReturnValueRepresentation.returnName "Permalink to this definition")  
name of the return value

Returns:  representation used for the return value

Return type:  str

GetReturnValueSaveIn(*[returnName](#ApiClient.TsCallIOControl.GetReturnValueSaveIn.returnName "ApiClient.TsCallIOControl.GetReturnValueSaveIn.returnName (Python parameter) — name of the return value")*)[¶](#ApiClient.TsCallIOControl.GetReturnValueSaveIn "Link to this definition")  
Returns the variable name to save the specified return value in

Parameters:  returnName : str[¶](#ApiClient.TsCallIOControl.GetReturnValueSaveIn.returnName "Permalink to this definition")  
name of the return value

Returns:  variable name

Return type:  str

GetReturnValueUnit(*[returnName](#ApiClient.TsCallIOControl.GetReturnValueUnit.returnName "ApiClient.TsCallIOControl.GetReturnValueUnit.returnName (Python parameter) — name of the return value")*)[¶](#ApiClient.TsCallIOControl.GetReturnValueUnit "Link to this definition")  
Returns the unit for the specified return value

Parameters:  returnName : str[¶](#ApiClient.TsCallIOControl.GetReturnValueUnit.returnName "Permalink to this definition")  
name of the return value

Returns:  Unit used by the `~ApiClient.PHYS` representation for this return value

Return type:  str

GetTags()[¶](#ApiClient.TsCallIOControl.GetTags "Link to this definition")  
Returns the tags set for this step.

Returns:  A (sorted) list of tags

Return type:  list[str]

GetTestManagementId()[¶](#ApiClient.TsCallIOControl.GetTestManagementId "Link to this definition")  
Returns the test management id of the test step.

Returns:  Test step id.

Return type:  str

GetTestStepId()[¶](#ApiClient.TsCallIOControl.GetTestStepId "Link to this definition")  
Returns the test step id.

Returns:  test step id

Return type:  str

GetTimeout()[¶](#ApiClient.TsCallIOControl.GetTimeout "Link to this definition")  
Returns the timeout of the test step’s time option, if a corresponding option has been set.

Returns:  The timeout else None

Return type:  string

GetTimeoutUnit()[¶](#ApiClient.TsCallIOControl.GetTimeoutUnit "Link to this definition")  
Returns the unit of the timeout of the test step’s time option, if a corresponding option has been set.

Returns:  The unit of the timeout else None

Return type:  string

GetTranslatedCommentText(*[language](#ApiClient.TsCallIOControl.GetTranslatedCommentText.language "ApiClient.TsCallIOControl.GetTranslatedCommentText.language (Python parameter) — Language of the requested text ('en_US', 'de_DE', 'zh_CN')")*)[¶](#ApiClient.TsCallIOControl.GetTranslatedCommentText "Link to this definition")  
Returns the text value of the “comment” column in the given language.

Parameters:  language : str[¶](#ApiClient.TsCallIOControl.GetTranslatedCommentText.language "Permalink to this definition")  
Language of the requested text (‘en_US’, ‘de_DE’, ‘zh_CN’)

Returns:  Comment column text

Return type:  str

GetType()[¶](#ApiClient.TsCallIOControl.GetType "Link to this definition")  
Returns the type (class name) of the test step, e.g.

- “TsPreconditionBlock”

- “TsWait”

- “TsIfThenElse”

- “TsSwitchCase”

- “TsCaseNode”

Returns:  Type (class name) of the test step

Return type:  str

GetValueColumnText()[¶](#ApiClient.TsCallIOControl.GetValueColumnText "Link to this definition")  
Returns the text value of the “value” column in your current test case language.

Returns:  Value column text

Return type:  str

IsBreakpoint()[¶](#ApiClient.TsCallIOControl.IsBreakpoint "Link to this definition")  
Checks whether the test step is a break point.

Returns:  True if test step is a break point, else False

Return type:  boolean

IsContainer()[¶](#ApiClient.TsCallIOControl.IsContainer "Link to this definition")  
Checks whether this test step can contain test steps

Returns:  True if it can contain test steps, else False

Return type:  boolean

IsEnabled()[¶](#ApiClient.TsCallIOControl.IsEnabled "Link to this definition")  
Returns the state of the test step.

Returns:  True if test step is enabled, otherwise False

Return type:  bool

IsInPostcondition()[¶](#ApiClient.TsCallIOControl.IsInPostcondition "Link to this definition")  
Returns True if the test step is located in a postcondition

Returns:  True if the test step is located in a postcondition, else Flase

Return type:  bool

IsInPrecondition()[¶](#ApiClient.TsCallIOControl.IsInPrecondition "Link to this definition")  
Returns True if the test step is located in a precondition

Returns:  True if the test step is located in a precondition, else False

Return type:  bool

IsOk()[¶](#ApiClient.TsCallIOControl.IsOk "Link to this definition")  
Returns the internal state of correctness of the test step.

Returns:  True if no problems were found, else False

Return type:  boolean

IsVisible()[¶](#ApiClient.TsCallIOControl.IsVisible "Link to this definition")  
Checks whether the test step is visible. This depends on the test step itself or a parent test step being disabled.

Returns:  True if test step is visible, else False

Return type:  boolean

RemovePacketExpectation()[¶](#ApiClient.TsCallIOControl.RemovePacketExpectation "Link to this definition")  
Removes the expectation for the packet. Only applicable if this test step is mapped to a service method/event.

RemoveTag(*[tag](#ApiClient.TsCallIOControl.RemoveTag.tag "ApiClient.TsCallIOControl.RemoveTag.tag (Python parameter) — The tag to be removed")*)[¶](#ApiClient.TsCallIOControl.RemoveTag "Link to this definition")  
Remove a specific tag from this step.

Parameters:  tag : str[¶](#ApiClient.TsCallIOControl.RemoveTag.tag "Permalink to this definition")  
The tag to be removed

SetBreakpoint(*[enable](#ApiClient.TsCallIOControl.SetBreakpoint.enable "ApiClient.TsCallIOControl.SetBreakpoint.enable (Python parameter) — True if test step is a break point, else False")*)[¶](#ApiClient.TsCallIOControl.SetBreakpoint "Link to this definition")  
Sets or unsets the test step to act as a break point.

Parameters:  enable : boolean[¶](#ApiClient.TsCallIOControl.SetBreakpoint.enable "Permalink to this definition")  
True if test step is a break point, else False

SetComment(*[comment](#ApiClient.TsCallIOControl.SetComment.comment "ApiClient.TsCallIOControl.SetComment.comment (Python parameter) — Text to be displayed in the comment tab")*)[¶](#ApiClient.TsCallIOControl.SetComment "Link to this definition")  
Sets a comment for the test step in the current test case language.

Parameters:  comment : str[¶](#ApiClient.TsCallIOControl.SetComment.comment "Permalink to this definition")  
Text to be displayed in the comment tab

SetCyclic(*[cyclicState](#ApiClient.TsCallIOControl.SetCyclic.cyclicState "ApiClient.TsCallIOControl.SetCyclic.cyclicState (Python parameter) — possible values are:")*, *[cycleTimeExpression](#ApiClient.TsCallIOControl.SetCyclic.cycleTimeExpression "ApiClient.TsCallIOControl.SetCyclic.cycleTimeExpression (Python parameter) — in milliseconds, necessary for cyclicState 'on'")=`None`*)[¶](#ApiClient.TsCallIOControl.SetCyclic "Link to this definition")  
Changes the send cyclic settings for a test step that has call mode ‘SEND_EVENT’

Raises:  
**ApiError** – if the test step doesn’t support cyclic sending

Parameters:  cyclicState : str[¶](#ApiClient.TsCallIOControl.SetCyclic.cyclicState "Permalink to this definition")  
possible values are:

- ’on’ enables cyclic sending using the specified cycleTimeExpression

- ’off’ disables cyclic sending

- ’unchanged’ keeps cyclic sending (e.g. if just the event’s values should be changed)

- None removes cyclic settings so the test step will send the event just once

cycleTimeExpression : str[¶](#ApiClient.TsCallIOControl.SetCyclic.cycleTimeExpression "Permalink to this definition")  
in milliseconds, necessary for cyclicState ‘on’

SetEnabled(*[state](#ApiClient.TsCallIOControl.SetEnabled.state "ApiClient.TsCallIOControl.SetEnabled.state (Python parameter) — True (Default) to enable, False to disable the test step.")=`True`*)[¶](#ApiClient.TsCallIOControl.SetEnabled "Link to this definition")  
Enable or disable the test step.

Parameters:  state : bool[¶](#ApiClient.TsCallIOControl.SetEnabled.state "Permalink to this definition")  
True (Default) to enable, False to disable the test step.

SetIgnoreResponse(*[ignoreResponse](#ApiClient.TsCallIOControl.SetIgnoreResponse.ignoreResponse "ApiClient.TsCallIOControl.SetIgnoreResponse.ignoreResponse (Python parameter) — Sets the value of the option.")*)[¶](#ApiClient.TsCallIOControl.SetIgnoreResponse "Link to this definition")  
Sets test step’s option for ignoring its response.

Raises:  
**ApiError** – If not return values or ignoring the response is not supported the option does not make sense.

Parameters:  ignoreResponse : bool[¶](#ApiClient.TsCallIOControl.SetIgnoreResponse.ignoreResponse "Permalink to this definition")  
Sets the value of the option.

SetPacketExpectation(*[expectationExpression](#ApiClient.TsCallIOControl.SetPacketExpectation.expectationExpression "ApiClient.TsCallIOControl.SetPacketExpectation.expectationExpression (Python parameter) — expectation for the return value")*)[¶](#ApiClient.TsCallIOControl.SetPacketExpectation "Link to this definition")  
Sets the expectation for the packet. Only applicable if this test step is mapped to a service method/event.

This should be a [`ExpressionExpectation`](../ExpectationApi/ExpressionExpectation.md#ApiClient.ExpressionExpectation "ApiClient.ExpressionExpectation (Python class) — ExpectationApi.CreateExpressionExpectation") referencing the packet as `value`, a [`PresentExpectation`](../ExpectationApi/PresentExpectation.md#ApiClient.PresentExpectation "ApiClient.PresentExpectation (Python class) — ExpectationApi.CreatePresentExpectation"), or a [`NotPresentExpectation`](../ExpectationApi/NotPresentExpectation.md#ApiClient.NotPresentExpectation "ApiClient.NotPresentExpectation (Python class) — ExpectationApi.CreateNotPresentExpectation").

Keep in mind that the `value` object can not only be a `PacketSomeIp` but also NotPresent.

Parameters:  expectationExpression[¶](#ApiClient.TsCallIOControl.SetPacketExpectation.expectationExpression "Permalink to this definition")  
expectation for the return value

SetParameterRepresentation(*[parameterName](#ApiClient.TsCallIOControl.SetParameterRepresentation.parameterName "ApiClient.TsCallIOControl.SetParameterRepresentation.parameterName (Python parameter) — name of the parameter")*, *[repr](#ApiClient.TsCallIOControl.SetParameterRepresentation.repr "ApiClient.TsCallIOControl.SetParameterRepresentation.repr (Python parameter) — representation to use for the parameter. One of ~ApiClient.PHYS, ~ApiClient.RAW, ~ApiClient.TEXT or ~ApiClient.BITS")*)[¶](#ApiClient.TsCallIOControl.SetParameterRepresentation "Link to this definition")  
Sets the representation for the specified parameter

This method only works with existing parameters. To add a parameter please use [`AddParameter()`](#ApiClient.TsCallIOControl.AddParameter "ApiClient.TsCallIOControl.AddParameter (Python method) — Adds a parameter to the test step.")

Parameters:  parameterName : str[¶](#ApiClient.TsCallIOControl.SetParameterRepresentation.parameterName "Permalink to this definition")  
name of the parameter

repr : str[¶](#ApiClient.TsCallIOControl.SetParameterRepresentation.repr "Permalink to this definition")  
representation to use for the parameter. One of `~ApiClient.PHYS`, `~ApiClient.RAW`, `~ApiClient.TEXT` or `~ApiClient.BITS`

SetParameterUnit(*[parameterName](#ApiClient.TsCallIOControl.SetParameterUnit.parameterName "ApiClient.TsCallIOControl.SetParameterUnit.parameterName (Python parameter) — name of the parameter")*, *[unit](#ApiClient.TsCallIOControl.SetParameterUnit.unit "ApiClient.TsCallIOControl.SetParameterUnit.unit (Python parameter) — Unit to use for the ~ApiClient.PHYS representation for this parameter")*)[¶](#ApiClient.TsCallIOControl.SetParameterUnit "Link to this definition")  
Sets the unit for the specified parameter

This method only works with existing parameters. To add a parameter please use [`AddParameter()`](#ApiClient.TsCallIOControl.AddParameter "ApiClient.TsCallIOControl.AddParameter (Python method) — Adds a parameter to the test step.")

Parameters:  parameterName : str[¶](#ApiClient.TsCallIOControl.SetParameterUnit.parameterName "Permalink to this definition")  
name of the parameter

unit : str[¶](#ApiClient.TsCallIOControl.SetParameterUnit.unit "Permalink to this definition")  
Unit to use for the `~ApiClient.PHYS` representation for this parameter

SetParameterValue(*[parameterName](#ApiClient.TsCallIOControl.SetParameterValue.parameterName "ApiClient.TsCallIOControl.SetParameterValue.parameterName (Python parameter) — name of the parameter")*, *[valueExpression](#ApiClient.TsCallIOControl.SetParameterValue.valueExpression "ApiClient.TsCallIOControl.SetParameterValue.valueExpression (Python parameter) — expression to use for the parameter's value")*)[¶](#ApiClient.TsCallIOControl.SetParameterValue "Link to this definition")  
Assigns a new expression to use the specified parameter’s value

This method only works with existing parameters. To add a parameter please use [`AddParameter()`](#ApiClient.TsCallIOControl.AddParameter "ApiClient.TsCallIOControl.AddParameter (Python method) — Adds a parameter to the test step.")

Parameters:  parameterName : str[¶](#ApiClient.TsCallIOControl.SetParameterValue.parameterName "Permalink to this definition")  
name of the parameter

valueExpression : str[¶](#ApiClient.TsCallIOControl.SetParameterValue.valueExpression "Permalink to this definition")  
expression to use for the parameter’s value

SetReturnValueExpectation(*[returnName](#ApiClient.TsCallIOControl.SetReturnValueExpectation.returnName "ApiClient.TsCallIOControl.SetReturnValueExpectation.returnName (Python parameter) — name of the return value")*, *[expectationExpression](#ApiClient.TsCallIOControl.SetReturnValueExpectation.expectationExpression "ApiClient.TsCallIOControl.SetReturnValueExpectation.expectationExpression (Python parameter) — expectation for the return value")*)[¶](#ApiClient.TsCallIOControl.SetReturnValueExpectation "Link to this definition")  
Sets the expectation for the specified return value.

This method only works with existing return values. To add a return value please use [`AddReturnValue()`](#ApiClient.TsCallIOControl.AddReturnValue "ApiClient.TsCallIOControl.AddReturnValue (Python method) — Adds a return value to the test step.")

Parameters:  returnName : str[¶](#ApiClient.TsCallIOControl.SetReturnValueExpectation.returnName "Permalink to this definition")  
name of the return value

expectationExpression[¶](#ApiClient.TsCallIOControl.SetReturnValueExpectation.expectationExpression "Permalink to this definition")  
expectation for the return value

SetReturnValueRepresentation(*[returnName](#ApiClient.TsCallIOControl.SetReturnValueRepresentation.returnName "ApiClient.TsCallIOControl.SetReturnValueRepresentation.returnName (Python parameter) — name of the return value")*, *[repr](#ApiClient.TsCallIOControl.SetReturnValueRepresentation.repr "ApiClient.TsCallIOControl.SetReturnValueRepresentation.repr (Python parameter) — representation to use for the return value. One of ~ApiClient.PHYS, ~ApiClient.RAW, ~ApiClient.TEXT or ~ApiClient.BITS")*)[¶](#ApiClient.TsCallIOControl.SetReturnValueRepresentation "Link to this definition")  
Sets the representation for the specified return value

This method only works with existing return values. To add a return value please use [`AddReturnValue()`](#ApiClient.TsCallIOControl.AddReturnValue "ApiClient.TsCallIOControl.AddReturnValue (Python method) — Adds a return value to the test step.")

Parameters:  returnName : str[¶](#ApiClient.TsCallIOControl.SetReturnValueRepresentation.returnName "Permalink to this definition")  
name of the return value

repr : str[¶](#ApiClient.TsCallIOControl.SetReturnValueRepresentation.repr "Permalink to this definition")  
representation to use for the return value. One of `~ApiClient.PHYS`, `~ApiClient.RAW`, `~ApiClient.TEXT` or `~ApiClient.BITS`

SetReturnValueSaveIn(*[returnName](#ApiClient.TsCallIOControl.SetReturnValueSaveIn.returnName "ApiClient.TsCallIOControl.SetReturnValueSaveIn.returnName (Python parameter) — name of the return value")*, *[saveInVariableName](#ApiClient.TsCallIOControl.SetReturnValueSaveIn.saveInVariableName "ApiClient.TsCallIOControl.SetReturnValueSaveIn.saveInVariableName (Python parameter) — variable name")*)[¶](#ApiClient.TsCallIOControl.SetReturnValueSaveIn "Link to this definition")  
Sets the variable name to save the specified return value in

This method only works with existing return values. To add a return value please use [`AddReturnValue()`](#ApiClient.TsCallIOControl.AddReturnValue "ApiClient.TsCallIOControl.AddReturnValue (Python method) — Adds a return value to the test step.")

Parameters:  returnName : str[¶](#ApiClient.TsCallIOControl.SetReturnValueSaveIn.returnName "Permalink to this definition")  
name of the return value

saveInVariableName : str[¶](#ApiClient.TsCallIOControl.SetReturnValueSaveIn.saveInVariableName "Permalink to this definition")  
variable name

SetReturnValueUnit(*[returnName](#ApiClient.TsCallIOControl.SetReturnValueUnit.returnName "ApiClient.TsCallIOControl.SetReturnValueUnit.returnName (Python parameter) — name of the return value")*, *[unit](#ApiClient.TsCallIOControl.SetReturnValueUnit.unit "ApiClient.TsCallIOControl.SetReturnValueUnit.unit (Python parameter) — Unit to use for the ~ApiClient.PHYS representation for this return value")*)[¶](#ApiClient.TsCallIOControl.SetReturnValueUnit "Link to this definition")  
Sets the unit for the specified return value

This method only works with existing return values. To add a return value please use [`AddReturnValue()`](#ApiClient.TsCallIOControl.AddReturnValue "ApiClient.TsCallIOControl.AddReturnValue (Python method) — Adds a return value to the test step.")

Parameters:  returnName : str[¶](#ApiClient.TsCallIOControl.SetReturnValueUnit.returnName "Permalink to this definition")  
name of the return value

unit : str[¶](#ApiClient.TsCallIOControl.SetReturnValueUnit.unit "Permalink to this definition")  
Unit to use for the `~ApiClient.PHYS` representation for this return value

SetTags(*[tags](#ApiClient.TsCallIOControl.SetTags.tags "ApiClient.TsCallIOControl.SetTags.tags (Python parameter) — The list of tags")*)[¶](#ApiClient.TsCallIOControl.SetTags "Link to this definition")  
Set the list of tags for this step. The list of tags will be sorted and stored.

Parameters:  tags : list[str][¶](#ApiClient.TsCallIOControl.SetTags.tags "Permalink to this definition")  
The list of tags

SetTestManagementId(*[testManagementId](#ApiClient.TsCallIOControl.SetTestManagementId.testManagementId "ApiClient.TsCallIOControl.SetTestManagementId.testManagementId (Python parameter) — Test management id of the test step")*)[¶](#ApiClient.TsCallIOControl.SetTestManagementId "Link to this definition")  
Sets the test management id of the test step.

Parameters:  testManagementId : str[¶](#ApiClient.TsCallIOControl.SetTestManagementId.testManagementId "Permalink to this definition")  
Test management id of the test step

SetTimeOptionOnlySynchronization(*[timeout](#ApiClient.TsCallIOControl.SetTimeOptionOnlySynchronization.timeout "ApiClient.TsCallIOControl.SetTimeOptionOnlySynchronization.timeout (Python parameter) — The timeout to be used")*, *[pollingCycle](#ApiClient.TsCallIOControl.SetTimeOptionOnlySynchronization.pollingCycle "ApiClient.TsCallIOControl.SetTimeOptionOnlySynchronization.pollingCycle (Python parameter) — Optional polling cycle to be used")=`None`*, *[timeoutUnit](#ApiClient.TsCallIOControl.SetTimeOptionOnlySynchronization.timeoutUnit "ApiClient.TsCallIOControl.SetTimeOptionOnlySynchronization.timeoutUnit (Python parameter) — Optional unit for the timeout (ms, s, min, h or d)")=`'ms'`*, *[pollingCycleUnit](#ApiClient.TsCallIOControl.SetTimeOptionOnlySynchronization.pollingCycleUnit "ApiClient.TsCallIOControl.SetTimeOptionOnlySynchronization.pollingCycleUnit (Python parameter) — Optional unit for the polling cycle (ms, s, min, h or d)")=`'ms'`*)[¶](#ApiClient.TsCallIOControl.SetTimeOptionOnlySynchronization "Link to this definition")  
Sets the test step’s time option to “only synchronization”.

Raises:  
**ApiError** – If no return value has an expectation, no time option can be set.

Parameters:  timeout : string[¶](#ApiClient.TsCallIOControl.SetTimeOptionOnlySynchronization.timeout "Permalink to this definition")  
The timeout to be used

pollingCycle : string[¶](#ApiClient.TsCallIOControl.SetTimeOptionOnlySynchronization.pollingCycle "Permalink to this definition")  
Optional polling cycle to be used

timeoutUnit : string[¶](#ApiClient.TsCallIOControl.SetTimeOptionOnlySynchronization.timeoutUnit "Permalink to this definition")  
Optional unit for the timeout (ms, s, min, h or d)

pollingCycleUnit : string[¶](#ApiClient.TsCallIOControl.SetTimeOptionOnlySynchronization.pollingCycleUnit "Permalink to this definition")  
Optional unit for the polling cycle (ms, s, min, h or d)

SetTimeOptionPollingCycleMultiplier(*[pollingCycleMultiplier](#ApiClient.TsCallIOControl.SetTimeOptionPollingCycleMultiplier.pollingCycleMultiplier "ApiClient.TsCallIOControl.SetTimeOptionPollingCycleMultiplier.pollingCycleMultiplier (Python parameter) — The polling cycle multiplier to be used.")*)[¶](#ApiClient.TsCallIOControl.SetTimeOptionPollingCycleMultiplier "Link to this definition")  
Sets the test step’s time option to “polling cycle multiplier”. This option must only be used when inserting the test step into a Multi-Check!

Parameters:  pollingCycleMultiplier : string[¶](#ApiClient.TsCallIOControl.SetTimeOptionPollingCycleMultiplier.pollingCycleMultiplier "Permalink to this definition")  
The polling cycle multiplier to be used.

SetTimeOptionTrueForAtLeast(*[minimumDuration](#ApiClient.TsCallIOControl.SetTimeOptionTrueForAtLeast.minimumDuration "ApiClient.TsCallIOControl.SetTimeOptionTrueForAtLeast.minimumDuration (Python parameter) — The minimum duration to be used")*, *[pollingCycle](#ApiClient.TsCallIOControl.SetTimeOptionTrueForAtLeast.pollingCycle "ApiClient.TsCallIOControl.SetTimeOptionTrueForAtLeast.pollingCycle (Python parameter) — Optional polling cycle to be used")=`None`*, *[timeoutUnit](#ApiClient.TsCallIOControl.SetTimeOptionTrueForAtLeast.timeoutUnit "ApiClient.TsCallIOControl.SetTimeOptionTrueForAtLeast.timeoutUnit (Python parameter) — Optional unit for the timeout (ms, s, min, h or d)")=`'ms'`*, *[pollingCycleUnit](#ApiClient.TsCallIOControl.SetTimeOptionTrueForAtLeast.pollingCycleUnit "ApiClient.TsCallIOControl.SetTimeOptionTrueForAtLeast.pollingCycleUnit (Python parameter) — Optional unit for the polling cycle (ms, s, min, h or d)")=`'ms'`*)[¶](#ApiClient.TsCallIOControl.SetTimeOptionTrueForAtLeast "Link to this definition")  
Sets the test step’s time option to “true for at least”.

Raises:  
**ApiError** – If no return value has an expectation, no time option can be set.

Parameters:  minimumDuration : string[¶](#ApiClient.TsCallIOControl.SetTimeOptionTrueForAtLeast.minimumDuration "Permalink to this definition")  
The minimum duration to be used

pollingCycle : string[¶](#ApiClient.TsCallIOControl.SetTimeOptionTrueForAtLeast.pollingCycle "Permalink to this definition")  
Optional polling cycle to be used

timeoutUnit : string[¶](#ApiClient.TsCallIOControl.SetTimeOptionTrueForAtLeast.timeoutUnit "Permalink to this definition")  
Optional unit for the timeout (ms, s, min, h or d)

pollingCycleUnit : string[¶](#ApiClient.TsCallIOControl.SetTimeOptionTrueForAtLeast.pollingCycleUnit "Permalink to this definition")  
Optional unit for the polling cycle (ms, s, min, h or d)

SetTimeOptionTrueForAtLeastWithin(*[minimumDuration](#ApiClient.TsCallIOControl.SetTimeOptionTrueForAtLeastWithin.minimumDuration "ApiClient.TsCallIOControl.SetTimeOptionTrueForAtLeastWithin.minimumDuration (Python parameter) — The minimum duration to be used")*, *[timeout](#ApiClient.TsCallIOControl.SetTimeOptionTrueForAtLeastWithin.timeout "ApiClient.TsCallIOControl.SetTimeOptionTrueForAtLeastWithin.timeout (Python parameter) — The timeout to be used")*, *[pollingCycle](#ApiClient.TsCallIOControl.SetTimeOptionTrueForAtLeastWithin.pollingCycle "ApiClient.TsCallIOControl.SetTimeOptionTrueForAtLeastWithin.pollingCycle (Python parameter) — Optional polling cycle to be used")=`None`*, *[timeoutUnit](#ApiClient.TsCallIOControl.SetTimeOptionTrueForAtLeastWithin.timeoutUnit "ApiClient.TsCallIOControl.SetTimeOptionTrueForAtLeastWithin.timeoutUnit (Python parameter) — Optional unit for the timeout (ms, s, min, h or d)")=`'ms'`*, *[pollingCycleUnit](#ApiClient.TsCallIOControl.SetTimeOptionTrueForAtLeastWithin.pollingCycleUnit "ApiClient.TsCallIOControl.SetTimeOptionTrueForAtLeastWithin.pollingCycleUnit (Python parameter) — Optional unit for the polling cycle (ms, s, min, h or d)")=`'ms'`*)[¶](#ApiClient.TsCallIOControl.SetTimeOptionTrueForAtLeastWithin "Link to this definition")  
Sets the test step’s time option to “true for at least … within …”.

Raises:  
**ApiError** – If no return value has an expectation, no time option can be set.

Parameters:  minimumDuration : string[¶](#ApiClient.TsCallIOControl.SetTimeOptionTrueForAtLeastWithin.minimumDuration "Permalink to this definition")  
The minimum duration to be used

timeout : string[¶](#ApiClient.TsCallIOControl.SetTimeOptionTrueForAtLeastWithin.timeout "Permalink to this definition")  
The timeout to be used

pollingCycle : string[¶](#ApiClient.TsCallIOControl.SetTimeOptionTrueForAtLeastWithin.pollingCycle "Permalink to this definition")  
Optional polling cycle to be used

timeoutUnit : string[¶](#ApiClient.TsCallIOControl.SetTimeOptionTrueForAtLeastWithin.timeoutUnit "Permalink to this definition")  
Optional unit for the timeout (ms, s, min, h or d)

pollingCycleUnit : string[¶](#ApiClient.TsCallIOControl.SetTimeOptionTrueForAtLeastWithin.pollingCycleUnit "Permalink to this definition")  
Optional unit for the polling cycle (ms, s, min, h or d)

SetTimeOptionWaitUntilTrue(*[timeout](#ApiClient.TsCallIOControl.SetTimeOptionWaitUntilTrue.timeout "ApiClient.TsCallIOControl.SetTimeOptionWaitUntilTrue.timeout (Python parameter) — The timeout to be used")*, *[pollingCycle](#ApiClient.TsCallIOControl.SetTimeOptionWaitUntilTrue.pollingCycle "ApiClient.TsCallIOControl.SetTimeOptionWaitUntilTrue.pollingCycle (Python parameter) — Optional polling cycle to be used")=`None`*, *[timeoutUnit](#ApiClient.TsCallIOControl.SetTimeOptionWaitUntilTrue.timeoutUnit "ApiClient.TsCallIOControl.SetTimeOptionWaitUntilTrue.timeoutUnit (Python parameter) — Optional unit for the timeout (ms, s, min, h or d)")=`'ms'`*, *[pollingCycleUnit](#ApiClient.TsCallIOControl.SetTimeOptionWaitUntilTrue.pollingCycleUnit "ApiClient.TsCallIOControl.SetTimeOptionWaitUntilTrue.pollingCycleUnit (Python parameter) — Optional unit for the polling cycle (ms, s, min, h or d)")=`'ms'`*)[¶](#ApiClient.TsCallIOControl.SetTimeOptionWaitUntilTrue "Link to this definition")  
Sets the test step’s time option to “wait until true”.

Raises:  
**ApiError** – If no return value has an expectation, no time option can be set.

Parameters:  timeout : string[¶](#ApiClient.TsCallIOControl.SetTimeOptionWaitUntilTrue.timeout "Permalink to this definition")  
The timeout to be used

pollingCycle : string[¶](#ApiClient.TsCallIOControl.SetTimeOptionWaitUntilTrue.pollingCycle "Permalink to this definition")  
Optional polling cycle to be used

timeoutUnit : string[¶](#ApiClient.TsCallIOControl.SetTimeOptionWaitUntilTrue.timeoutUnit "Permalink to this definition")  
Optional unit for the timeout (ms, s, min, h or d)

pollingCycleUnit : string[¶](#ApiClient.TsCallIOControl.SetTimeOptionWaitUntilTrue.pollingCycleUnit "Permalink to this definition")  
Optional unit for the polling cycle (ms, s, min, h or d)

SetTranslatedCommentText(*[comment](#ApiClient.TsCallIOControl.SetTranslatedCommentText.comment "ApiClient.TsCallIOControl.SetTranslatedCommentText.comment (Python parameter) — Text to be displayed")*, *[language](#ApiClient.TsCallIOControl.SetTranslatedCommentText.language "ApiClient.TsCallIOControl.SetTranslatedCommentText.language (Python parameter) — Language of the text ('en_US', 'de_DE', 'zh_CN')")*)[¶](#ApiClient.TsCallIOControl.SetTranslatedCommentText "Link to this definition")  
Sets a comment for the test step in the given language.

Parameters:  comment : str[¶](#ApiClient.TsCallIOControl.SetTranslatedCommentText.comment "Permalink to this definition")  
Text to be displayed

language : str[¶](#ApiClient.TsCallIOControl.SetTranslatedCommentText.language "Permalink to this definition")  
Language of the text (‘en_US’, ‘de_DE’, ‘zh_CN’)

UpdateInterface()[¶](#ApiClient.TsCallIOControl.UpdateInterface "Link to this definition")  
Updates the list of parameters and return values according to the assigned mapping target:

- Removes any parameters and return values not available in the assigned mapping target

- Adds any missing parameters and return values defined in the assigned mapping target. Parameters are assigned a default value. Return values are not assigned any expectation.

Parameters and return values existing in both the test step and the mapping target are left as they are, which might in some cases result in an incompatible representation or unit.

Info

This only works if the test step is associated with an appropriate mappingItem (via a package, via a global mapping, or via the `~ApiClient.mappingItem` parameter of the [`CreateTsCall()`](../TestStepApi.md#ApiClient.TestStepApi.CreateTsCall "ApiClient.TestStepApi.CreateTsCall (Python method) — Creates a call test step.") method) and the database describing the target of the mapping item is loaded.

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
