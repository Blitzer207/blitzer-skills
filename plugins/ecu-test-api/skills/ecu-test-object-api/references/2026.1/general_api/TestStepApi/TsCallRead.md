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

[ TsCallKwpIOControlFreeze ](TsCallKwpIOControlFreeze.md)

[ TsCallKwpIOControlLongTermAdjustment ](TsCallKwpIOControlLongTermAdjustment.md)

[ TsCallKwpIOControlReportCurrentState ](TsCallKwpIOControlReportCurrentState.md)

[ TsCallKwpIOControlResetToDefault ](TsCallKwpIOControlResetToDefault.md)

[ TsCallKwpIOControlReturnControlToEcu ](TsCallKwpIOControlReturnControlToEcu.md)

[ TsCallKwpIOControlShortTermAdjustment ](TsCallKwpIOControlShortTermAdjustment.md)

[ TsCallProvideMethod ](TsCallProvideMethod.md)

TsCallRead [ TsCallRead ](#)

TsCallRead

- [C TsCallRead ](#ApiClient.TsCallRead)
  - [M AddParameter ](#ApiClient.TsCallRead.AddParameter)
  - [M AddReturnValue ](#ApiClient.TsCallRead.AddReturnValue)
  - [M AddTag ](#ApiClient.TsCallRead.AddTag)
  - [M Clone ](#ApiClient.TsCallRead.Clone)
  - [M DeactivateReturnValueExpectation ](#ApiClient.TsCallRead.DeactivateReturnValueExpectation)
  - [M DeactivateReturnValueSaveIn ](#ApiClient.TsCallRead.DeactivateReturnValueSaveIn)
  - [M DeactivateTimeOption ](#ApiClient.TsCallRead.DeactivateTimeOption)
  - [M DeleteParameter ](#ApiClient.TsCallRead.DeleteParameter)
  - [M DeleteReturnValue ](#ApiClient.TsCallRead.DeleteReturnValue)
  - [M DeleteTranslatedCommentText ](#ApiClient.TsCallRead.DeleteTranslatedCommentText)
  - [M GetActionColumnText ](#ApiClient.TsCallRead.GetActionColumnText)
  - [M GetActiveTimeOptionType ](#ApiClient.TsCallRead.GetActiveTimeOptionType)
  - [M GetComment ](#ApiClient.TsCallRead.GetComment)
  - [M GetCommentColumnText ](#ApiClient.TsCallRead.GetCommentColumnText)
  - [M GetCycleTimeExpression ](#ApiClient.TsCallRead.GetCycleTimeExpression)
  - [M GetCyclicState ](#ApiClient.TsCallRead.GetCyclicState)
  - [M GetError ](#ApiClient.TsCallRead.GetError)
  - [M GetIgnoreResponse ](#ApiClient.TsCallRead.GetIgnoreResponse)
  - [M GetIndex ](#ApiClient.TsCallRead.GetIndex)
  - [M GetLineNo ](#ApiClient.TsCallRead.GetLineNo)
  - [M GetMappingItemReferenceName ](#ApiClient.TsCallRead.GetMappingItemReferenceName)
  - [M GetMinimumDuration ](#ApiClient.TsCallRead.GetMinimumDuration)
  - [M GetMinimumDurationUnit ](#ApiClient.TsCallRead.GetMinimumDurationUnit)
  - [M GetPacketExpectation ](#ApiClient.TsCallRead.GetPacketExpectation)
  - [M GetParameterColumnText ](#ApiClient.TsCallRead.GetParameterColumnText)
  - [M GetParameterNames ](#ApiClient.TsCallRead.GetParameterNames)
  - [M GetParameterRepresentation ](#ApiClient.TsCallRead.GetParameterRepresentation)
  - [M GetParameterUnit ](#ApiClient.TsCallRead.GetParameterUnit)
  - [M GetParameterValue ](#ApiClient.TsCallRead.GetParameterValue)
  - [M GetParent ](#ApiClient.TsCallRead.GetParent)
  - [M GetPollingCycle ](#ApiClient.TsCallRead.GetPollingCycle)
  - [M GetPollingCycleUnit ](#ApiClient.TsCallRead.GetPollingCycleUnit)
  - [M GetReturnNames ](#ApiClient.TsCallRead.GetReturnNames)
  - [M GetReturnValueExpectation ](#ApiClient.TsCallRead.GetReturnValueExpectation)
  - [M GetReturnValueRepresentation ](#ApiClient.TsCallRead.GetReturnValueRepresentation)
  - [M GetReturnValueSaveIn ](#ApiClient.TsCallRead.GetReturnValueSaveIn)
  - [M GetReturnValueUnit ](#ApiClient.TsCallRead.GetReturnValueUnit)
  - [M GetTags ](#ApiClient.TsCallRead.GetTags)
  - [M GetTestManagementId ](#ApiClient.TsCallRead.GetTestManagementId)
  - [M GetTestStepId ](#ApiClient.TsCallRead.GetTestStepId)
  - [M GetTimeout ](#ApiClient.TsCallRead.GetTimeout)
  - [M GetTimeoutUnit ](#ApiClient.TsCallRead.GetTimeoutUnit)
  - [M GetTranslatedCommentText ](#ApiClient.TsCallRead.GetTranslatedCommentText)
  - [M GetType ](#ApiClient.TsCallRead.GetType)
  - [M GetValueColumnText ](#ApiClient.TsCallRead.GetValueColumnText)
  - [M IsBreakpoint ](#ApiClient.TsCallRead.IsBreakpoint)
  - [M IsContainer ](#ApiClient.TsCallRead.IsContainer)
  - [M IsEnabled ](#ApiClient.TsCallRead.IsEnabled)
  - [M IsInPostcondition ](#ApiClient.TsCallRead.IsInPostcondition)
  - [M IsInPrecondition ](#ApiClient.TsCallRead.IsInPrecondition)
  - [M IsOk ](#ApiClient.TsCallRead.IsOk)
  - [M IsVisible ](#ApiClient.TsCallRead.IsVisible)
  - [M RemovePacketExpectation ](#ApiClient.TsCallRead.RemovePacketExpectation)
  - [M RemoveTag ](#ApiClient.TsCallRead.RemoveTag)
  - [M SetBreakpoint ](#ApiClient.TsCallRead.SetBreakpoint)
  - [M SetComment ](#ApiClient.TsCallRead.SetComment)
  - [M SetCyclic ](#ApiClient.TsCallRead.SetCyclic)
  - [M SetEnabled ](#ApiClient.TsCallRead.SetEnabled)
  - [M SetIgnoreResponse ](#ApiClient.TsCallRead.SetIgnoreResponse)
  - [M SetPacketExpectation ](#ApiClient.TsCallRead.SetPacketExpectation)
  - [M SetParameterRepresentation ](#ApiClient.TsCallRead.SetParameterRepresentation)
  - [M SetParameterUnit ](#ApiClient.TsCallRead.SetParameterUnit)
  - [M SetParameterValue ](#ApiClient.TsCallRead.SetParameterValue)
  - [M SetReturnValueExpectation ](#ApiClient.TsCallRead.SetReturnValueExpectation)
  - [M SetReturnValueRepresentation ](#ApiClient.TsCallRead.SetReturnValueRepresentation)
  - [M SetReturnValueSaveIn ](#ApiClient.TsCallRead.SetReturnValueSaveIn)
  - [M SetReturnValueUnit ](#ApiClient.TsCallRead.SetReturnValueUnit)
  - [M SetTags ](#ApiClient.TsCallRead.SetTags)
  - [M SetTestManagementId ](#ApiClient.TsCallRead.SetTestManagementId)
  - [M SetTimeOptionOnlySynchronization ](#ApiClient.TsCallRead.SetTimeOptionOnlySynchronization)
  - [M SetTimeOptionPollingCycleMultiplier ](#ApiClient.TsCallRead.SetTimeOptionPollingCycleMultiplier)
  - [M SetTimeOptionTrueForAtLeast ](#ApiClient.TsCallRead.SetTimeOptionTrueForAtLeast)
  - [M SetTimeOptionTrueForAtLeastWithin ](#ApiClient.TsCallRead.SetTimeOptionTrueForAtLeastWithin)
  - [M SetTimeOptionWaitUntilTrue ](#ApiClient.TsCallRead.SetTimeOptionWaitUntilTrue)
  - [M SetTranslatedCommentText ](#ApiClient.TsCallRead.SetTranslatedCommentText)
  - [M UpdateInterface ](#ApiClient.TsCallRead.UpdateInterface)

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

TsCallRead

- [C TsCallRead ](#ApiClient.TsCallRead)
  - [M AddParameter ](#ApiClient.TsCallRead.AddParameter)
  - [M AddReturnValue ](#ApiClient.TsCallRead.AddReturnValue)
  - [M AddTag ](#ApiClient.TsCallRead.AddTag)
  - [M Clone ](#ApiClient.TsCallRead.Clone)
  - [M DeactivateReturnValueExpectation ](#ApiClient.TsCallRead.DeactivateReturnValueExpectation)
  - [M DeactivateReturnValueSaveIn ](#ApiClient.TsCallRead.DeactivateReturnValueSaveIn)
  - [M DeactivateTimeOption ](#ApiClient.TsCallRead.DeactivateTimeOption)
  - [M DeleteParameter ](#ApiClient.TsCallRead.DeleteParameter)
  - [M DeleteReturnValue ](#ApiClient.TsCallRead.DeleteReturnValue)
  - [M DeleteTranslatedCommentText ](#ApiClient.TsCallRead.DeleteTranslatedCommentText)
  - [M GetActionColumnText ](#ApiClient.TsCallRead.GetActionColumnText)
  - [M GetActiveTimeOptionType ](#ApiClient.TsCallRead.GetActiveTimeOptionType)
  - [M GetComment ](#ApiClient.TsCallRead.GetComment)
  - [M GetCommentColumnText ](#ApiClient.TsCallRead.GetCommentColumnText)
  - [M GetCycleTimeExpression ](#ApiClient.TsCallRead.GetCycleTimeExpression)
  - [M GetCyclicState ](#ApiClient.TsCallRead.GetCyclicState)
  - [M GetError ](#ApiClient.TsCallRead.GetError)
  - [M GetIgnoreResponse ](#ApiClient.TsCallRead.GetIgnoreResponse)
  - [M GetIndex ](#ApiClient.TsCallRead.GetIndex)
  - [M GetLineNo ](#ApiClient.TsCallRead.GetLineNo)
  - [M GetMappingItemReferenceName ](#ApiClient.TsCallRead.GetMappingItemReferenceName)
  - [M GetMinimumDuration ](#ApiClient.TsCallRead.GetMinimumDuration)
  - [M GetMinimumDurationUnit ](#ApiClient.TsCallRead.GetMinimumDurationUnit)
  - [M GetPacketExpectation ](#ApiClient.TsCallRead.GetPacketExpectation)
  - [M GetParameterColumnText ](#ApiClient.TsCallRead.GetParameterColumnText)
  - [M GetParameterNames ](#ApiClient.TsCallRead.GetParameterNames)
  - [M GetParameterRepresentation ](#ApiClient.TsCallRead.GetParameterRepresentation)
  - [M GetParameterUnit ](#ApiClient.TsCallRead.GetParameterUnit)
  - [M GetParameterValue ](#ApiClient.TsCallRead.GetParameterValue)
  - [M GetParent ](#ApiClient.TsCallRead.GetParent)
  - [M GetPollingCycle ](#ApiClient.TsCallRead.GetPollingCycle)
  - [M GetPollingCycleUnit ](#ApiClient.TsCallRead.GetPollingCycleUnit)
  - [M GetReturnNames ](#ApiClient.TsCallRead.GetReturnNames)
  - [M GetReturnValueExpectation ](#ApiClient.TsCallRead.GetReturnValueExpectation)
  - [M GetReturnValueRepresentation ](#ApiClient.TsCallRead.GetReturnValueRepresentation)
  - [M GetReturnValueSaveIn ](#ApiClient.TsCallRead.GetReturnValueSaveIn)
  - [M GetReturnValueUnit ](#ApiClient.TsCallRead.GetReturnValueUnit)
  - [M GetTags ](#ApiClient.TsCallRead.GetTags)
  - [M GetTestManagementId ](#ApiClient.TsCallRead.GetTestManagementId)
  - [M GetTestStepId ](#ApiClient.TsCallRead.GetTestStepId)
  - [M GetTimeout ](#ApiClient.TsCallRead.GetTimeout)
  - [M GetTimeoutUnit ](#ApiClient.TsCallRead.GetTimeoutUnit)
  - [M GetTranslatedCommentText ](#ApiClient.TsCallRead.GetTranslatedCommentText)
  - [M GetType ](#ApiClient.TsCallRead.GetType)
  - [M GetValueColumnText ](#ApiClient.TsCallRead.GetValueColumnText)
  - [M IsBreakpoint ](#ApiClient.TsCallRead.IsBreakpoint)
  - [M IsContainer ](#ApiClient.TsCallRead.IsContainer)
  - [M IsEnabled ](#ApiClient.TsCallRead.IsEnabled)
  - [M IsInPostcondition ](#ApiClient.TsCallRead.IsInPostcondition)
  - [M IsInPrecondition ](#ApiClient.TsCallRead.IsInPrecondition)
  - [M IsOk ](#ApiClient.TsCallRead.IsOk)
  - [M IsVisible ](#ApiClient.TsCallRead.IsVisible)
  - [M RemovePacketExpectation ](#ApiClient.TsCallRead.RemovePacketExpectation)
  - [M RemoveTag ](#ApiClient.TsCallRead.RemoveTag)
  - [M SetBreakpoint ](#ApiClient.TsCallRead.SetBreakpoint)
  - [M SetComment ](#ApiClient.TsCallRead.SetComment)
  - [M SetCyclic ](#ApiClient.TsCallRead.SetCyclic)
  - [M SetEnabled ](#ApiClient.TsCallRead.SetEnabled)
  - [M SetIgnoreResponse ](#ApiClient.TsCallRead.SetIgnoreResponse)
  - [M SetPacketExpectation ](#ApiClient.TsCallRead.SetPacketExpectation)
  - [M SetParameterRepresentation ](#ApiClient.TsCallRead.SetParameterRepresentation)
  - [M SetParameterUnit ](#ApiClient.TsCallRead.SetParameterUnit)
  - [M SetParameterValue ](#ApiClient.TsCallRead.SetParameterValue)
  - [M SetReturnValueExpectation ](#ApiClient.TsCallRead.SetReturnValueExpectation)
  - [M SetReturnValueRepresentation ](#ApiClient.TsCallRead.SetReturnValueRepresentation)
  - [M SetReturnValueSaveIn ](#ApiClient.TsCallRead.SetReturnValueSaveIn)
  - [M SetReturnValueUnit ](#ApiClient.TsCallRead.SetReturnValueUnit)
  - [M SetTags ](#ApiClient.TsCallRead.SetTags)
  - [M SetTestManagementId ](#ApiClient.TsCallRead.SetTestManagementId)
  - [M SetTimeOptionOnlySynchronization ](#ApiClient.TsCallRead.SetTimeOptionOnlySynchronization)
  - [M SetTimeOptionPollingCycleMultiplier ](#ApiClient.TsCallRead.SetTimeOptionPollingCycleMultiplier)
  - [M SetTimeOptionTrueForAtLeast ](#ApiClient.TsCallRead.SetTimeOptionTrueForAtLeast)
  - [M SetTimeOptionTrueForAtLeastWithin ](#ApiClient.TsCallRead.SetTimeOptionTrueForAtLeastWithin)
  - [M SetTimeOptionWaitUntilTrue ](#ApiClient.TsCallRead.SetTimeOptionWaitUntilTrue)
  - [M SetTranslatedCommentText ](#ApiClient.TsCallRead.SetTranslatedCommentText)
  - [M UpdateInterface ](#ApiClient.TsCallRead.UpdateInterface)

# TsCallRead[¶](#tscallread "Link to this heading")

*class* TsCallRead[¶](#ApiClient.TsCallRead "Link to this definition")  
AddParameter(*[parameterName](#ApiClient.TsCallRead.AddParameter.parameterName "ApiClient.TsCallRead.AddParameter.parameterName (Python parameter) — name of the parameter")*, *[valueExpression](#ApiClient.TsCallRead.AddParameter.valueExpression "ApiClient.TsCallRead.AddParameter.valueExpression (Python parameter) — expression to use for the parameter's value")=`None`*, *[repr](#ApiClient.TsCallRead.AddParameter.repr "ApiClient.TsCallRead.AddParameter.repr (Python parameter) — Representation.")=`'PHYS'`*, *[unit](#ApiClient.TsCallRead.AddParameter.unit "ApiClient.TsCallRead.AddParameter.unit (Python parameter) — Unit of the parameter")=`"don't care"`*)[¶](#ApiClient.TsCallRead.AddParameter "Link to this definition")  
Adds a parameter to the test step.

See also [`UpdateInterface()`](#ApiClient.TsCallRead.UpdateInterface "ApiClient.TsCallRead.UpdateInterface (Python method) — Updates the list of parameters and return values according to the assigned mapping target:") and the various `SetParameter...` methods.

Parameters:  parameterName : str[¶](#ApiClient.TsCallRead.AddParameter.parameterName "Permalink to this definition")  
name of the parameter

valueExpression : str[¶](#ApiClient.TsCallRead.AddParameter.valueExpression "Permalink to this definition")  
expression to use for the parameter’s value

repr : str[¶](#ApiClient.TsCallRead.AddParameter.repr "Permalink to this definition")  
Representation. One of `~ApiClient.PHYS`, `~ApiClient.RAW`, `~ApiClient.TEXT` or `~ApiClient.BITS`

unit : str[¶](#ApiClient.TsCallRead.AddParameter.unit "Permalink to this definition")  
Unit of the parameter

AddReturnValue(*[returnName](#ApiClient.TsCallRead.AddReturnValue.returnName "ApiClient.TsCallRead.AddReturnValue.returnName (Python parameter) — name of the return value")*, *[saveIn](#ApiClient.TsCallRead.AddReturnValue.saveIn "ApiClient.TsCallRead.AddReturnValue.saveIn (Python parameter) — name of the variable to save the return value into")=`None`*, *[expectation](#ApiClient.TsCallRead.AddReturnValue.expectation "ApiClient.TsCallRead.AddReturnValue.expectation (Python parameter) — Expectation for the return value")=`None`*, *[repr](#ApiClient.TsCallRead.AddReturnValue.repr "ApiClient.TsCallRead.AddReturnValue.repr (Python parameter) — Representation.")=`'PHYS'`*, *[unit](#ApiClient.TsCallRead.AddReturnValue.unit "ApiClient.TsCallRead.AddReturnValue.unit (Python parameter) — Unit of the return value")=`"don't care"`*)[¶](#ApiClient.TsCallRead.AddReturnValue "Link to this definition")  
Adds a return value to the test step.

See also [`UpdateInterface()`](#ApiClient.TsCallRead.UpdateInterface "ApiClient.TsCallRead.UpdateInterface (Python method) — Updates the list of parameters and return values according to the assigned mapping target:") and the various `SetReturnValue...` methods.

Parameters:  returnName : str[¶](#ApiClient.TsCallRead.AddReturnValue.returnName "Permalink to this definition")  
name of the return value

saveIn : str[¶](#ApiClient.TsCallRead.AddReturnValue.saveIn "Permalink to this definition")  
name of the variable to save the return value into

expectation=`None`[¶](#ApiClient.TsCallRead.AddReturnValue.expectation "Permalink to this definition")  
Expectation for the return value

repr : str[¶](#ApiClient.TsCallRead.AddReturnValue.repr "Permalink to this definition")  
Representation. One of `~ApiClient.PHYS`, `~ApiClient.RAW`, `~ApiClient.TEXT` or `~ApiClient.BITS`

unit : str[¶](#ApiClient.TsCallRead.AddReturnValue.unit "Permalink to this definition")  
Unit of the return value

AddTag(*[tag](#ApiClient.TsCallRead.AddTag.tag "ApiClient.TsCallRead.AddTag.tag (Python parameter) — The tag to be set")*)[¶](#ApiClient.TsCallRead.AddTag "Link to this definition")  
Add a specific tag to this step.

Parameters:  tag : str[¶](#ApiClient.TsCallRead.AddTag.tag "Permalink to this definition")  
The tag to be set

Clone()[¶](#ApiClient.TsCallRead.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`TsCallRead`](#ApiClient.TsCallRead "ApiClient.TsCallRead (Python class) — Adds a parameter to the test step.")

DeactivateReturnValueExpectation(*[returnName](#ApiClient.TsCallRead.DeactivateReturnValueExpectation.returnName "ApiClient.TsCallRead.DeactivateReturnValueExpectation.returnName (Python parameter) — name of the return value")*)[¶](#ApiClient.TsCallRead.DeactivateReturnValueExpectation "Link to this definition")  
Deactivates the expectation for the specified return value.

If no return value with an expectation remains, also deactivates any time option that may be configured.

Parameters:  returnName : str[¶](#ApiClient.TsCallRead.DeactivateReturnValueExpectation.returnName "Permalink to this definition")  
name of the return value

DeactivateReturnValueSaveIn(*[returnName](#ApiClient.TsCallRead.DeactivateReturnValueSaveIn.returnName "ApiClient.TsCallRead.DeactivateReturnValueSaveIn.returnName (Python parameter) — name of the return value")*)[¶](#ApiClient.TsCallRead.DeactivateReturnValueSaveIn "Link to this definition")  
Deactivates the save into a variable mechanism for the specified return value

Parameters:  returnName : str[¶](#ApiClient.TsCallRead.DeactivateReturnValueSaveIn.returnName "Permalink to this definition")  
name of the return value

DeactivateTimeOption()[¶](#ApiClient.TsCallRead.DeactivateTimeOption "Link to this definition")  
Deactivates any time option set on the test step. This is equivalent to selecting the option “none” in the test step’s time options menu.

DeleteParameter(*[parameterName](#ApiClient.TsCallRead.DeleteParameter.parameterName "ApiClient.TsCallRead.DeleteParameter.parameterName (Python parameter) — name of the parameter")*)[¶](#ApiClient.TsCallRead.DeleteParameter "Link to this definition")  
Removes a parameter from the test step.

See also [`UpdateInterface()`](#ApiClient.TsCallRead.UpdateInterface "ApiClient.TsCallRead.UpdateInterface (Python method) — Updates the list of parameters and return values according to the assigned mapping target:").

Parameters:  parameterName : str[¶](#ApiClient.TsCallRead.DeleteParameter.parameterName "Permalink to this definition")  
name of the parameter

DeleteReturnValue(*[returnName](#ApiClient.TsCallRead.DeleteReturnValue.returnName "ApiClient.TsCallRead.DeleteReturnValue.returnName (Python parameter) — name of the return value")*)[¶](#ApiClient.TsCallRead.DeleteReturnValue "Link to this definition")  
Removes a return value from the test step. If no return values are left after the deletion, also deactivates any time option that may be configured.

See also [`UpdateInterface()`](#ApiClient.TsCallRead.UpdateInterface "ApiClient.TsCallRead.UpdateInterface (Python method) — Updates the list of parameters and return values according to the assigned mapping target:").

Parameters:  returnName : str[¶](#ApiClient.TsCallRead.DeleteReturnValue.returnName "Permalink to this definition")  
name of the return value

DeleteTranslatedCommentText(*[language](#ApiClient.TsCallRead.DeleteTranslatedCommentText.language "ApiClient.TsCallRead.DeleteTranslatedCommentText.language (Python parameter) — Language of the text ('en_US', 'de_DE', 'zh_CN')")*)[¶](#ApiClient.TsCallRead.DeleteTranslatedCommentText "Link to this definition")  
Deletes a comment for the test step in the given language.

Parameters:  language : str[¶](#ApiClient.TsCallRead.DeleteTranslatedCommentText.language "Permalink to this definition")  
Language of the text (‘en_US’, ‘de_DE’, ‘zh_CN’)

GetActionColumnText()[¶](#ApiClient.TsCallRead.GetActionColumnText "Link to this definition")  
Returns the text value of the “action” column.

Returns:  Action column text

Return type:  str

GetActiveTimeOptionType()[¶](#ApiClient.TsCallRead.GetActiveTimeOptionType "Link to this definition")  
Returns the type of the currently active time option.

Returns:  Type of active time option (“Timeless”, “Finally”, “TrueForWithin”, “Generally”, “SyncOnly”, “PollingCycleMultiplier”)

Return type:  string

GetComment()[¶](#ApiClient.TsCallRead.GetComment "Link to this definition")  
Returns the comment of the test step in the current test case language.

Returns:  Comment text as shown in the comment tab

Return type:  str

GetCommentColumnText()[¶](#ApiClient.TsCallRead.GetCommentColumnText "Link to this definition")  
Returns the text value of the “comment” column.

Returns:  Comment column text

Return type:  str

GetCycleTimeExpression()[¶](#ApiClient.TsCallRead.GetCycleTimeExpression "Link to this definition")  
Gets the cycle time expression for this test step.

Returns:  cycle time expression in milliseconds

Return type:  str

GetCyclicState()[¶](#ApiClient.TsCallRead.GetCyclicState "Link to this definition")  
Gets the cyclic sending state for this test step.

Returns:  ‘on’, ‘off’, ‘unchanged’ or None

Return type:  str

GetError()[¶](#ApiClient.TsCallRead.GetError "Link to this definition")  
Returns a list of errors. Note that the error messages depend on the program language ecu.test is set to. Because of that we do not recommend to check against exact error messages, unless you are certain about the respective program language.

Returns:  List of errors

Return type:  list[str]

GetIgnoreResponse()[¶](#ApiClient.TsCallRead.GetIgnoreResponse "Link to this definition")  
Returns test step’s option for ignoring its response.

Raises:  
**ApiError** – If not return values or ignoring the response is not supported the option does not make sense.

Returns:  Returns the value of the option.

Return type:  bool

GetIndex()[¶](#ApiClient.TsCallRead.GetIndex "Link to this definition")  
Returns the zero based index in the parent.

Returns:  Zero based index

Return type:  integer

GetLineNo()[¶](#ApiClient.TsCallRead.GetLineNo "Link to this definition")  
Returns the test steps line number within its test case.

Returns:  Line number

Return type:  int

GetMappingItemReferenceName()[¶](#ApiClient.TsCallRead.GetMappingItemReferenceName "Link to this definition")  
Returns the unique reference name of the mapping item used by this test step.

Returns:  Reference name of used mapping item

Return type:  str

GetMinimumDuration()[¶](#ApiClient.TsCallRead.GetMinimumDuration "Link to this definition")  
Returns the minimum duration of the test step’s time option, if a corresponding option has been set.

Returns:  The minimum duration, else None

Return type:  string

GetMinimumDurationUnit()[¶](#ApiClient.TsCallRead.GetMinimumDurationUnit "Link to this definition")  
Returns the unit of the minimum duration of the test step’s time option, if a corresponding option has been set.

Returns:  The unit of the minimum duration, else None

Return type:  string

GetPacketExpectation()[¶](#ApiClient.TsCallRead.GetPacketExpectation "Link to this definition")  
Returns the expectation for the packet

Returns:  expectation

Return type:  [`Expectation`](../ExpectationApi/Expectation.md#ApiClient.Expectation "ApiClient.Expectation (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")

GetParameterColumnText()[¶](#ApiClient.TsCallRead.GetParameterColumnText "Link to this definition")  
Returns the text value of the “parameter” column.

Returns:  Parameter column text

Return type:  str

GetParameterNames()[¶](#ApiClient.TsCallRead.GetParameterNames "Link to this definition")  
Returns the names of the parameters defined in the test step.

Info

If the test step was created without a mapping item, or if the data base describing the target of the mapping item was not loaded, this list is initially empty. You can use [`AddParameter()`](#ApiClient.TsCallRead.AddParameter "ApiClient.TsCallRead.AddParameter (Python method) — Adds a parameter to the test step.") or [`UpdateInterface()`](#ApiClient.TsCallRead.UpdateInterface "ApiClient.TsCallRead.UpdateInterface (Python method) — Updates the list of parameters and return values according to the assigned mapping target:") to populate it.

Returns:  Parameter names

Return type:  list[str]

GetParameterRepresentation(*[parameterName](#ApiClient.TsCallRead.GetParameterRepresentation.parameterName "ApiClient.TsCallRead.GetParameterRepresentation.parameterName (Python parameter) — name of the parameter")*)[¶](#ApiClient.TsCallRead.GetParameterRepresentation "Link to this definition")  
Returns the representation used for the specified parameter

Parameters:  parameterName : str[¶](#ApiClient.TsCallRead.GetParameterRepresentation.parameterName "Permalink to this definition")  
name of the parameter

Returns:  representation used for the parameter

Return type:  str

GetParameterUnit(*[parameterName](#ApiClient.TsCallRead.GetParameterUnit.parameterName "ApiClient.TsCallRead.GetParameterUnit.parameterName (Python parameter) — name of the parameter")*)[¶](#ApiClient.TsCallRead.GetParameterUnit "Link to this definition")  
Returns the unit for the specified parameter

Parameters:  parameterName : str[¶](#ApiClient.TsCallRead.GetParameterUnit.parameterName "Permalink to this definition")  
name of the parameter

Returns:  Unit used by the `~ApiClient.PHYS` representation for this parameter

Return type:  str

GetParameterValue(*[parameterName](#ApiClient.TsCallRead.GetParameterValue.parameterName "ApiClient.TsCallRead.GetParameterValue.parameterName (Python parameter) — name of the parameter")*)[¶](#ApiClient.TsCallRead.GetParameterValue "Link to this definition")  
Returns the value expression assigned to the specified parameter

Parameters:  parameterName : str[¶](#ApiClient.TsCallRead.GetParameterValue.parameterName "Permalink to this definition")  
name of the parameter

Returns:  value expression assigned to the parameter

Return type:  str

GetParent()[¶](#ApiClient.TsCallRead.GetParent "Link to this definition")  
Returns the parent test step.

Returns:  The parent test step or None if it is a top level test step.

Return type:  [`TestStep`](../PackageApi/TestStep.md#ApiClient.TestStep "ApiClient.TestStep (Python class) — Add a specific tag to this step.")

GetPollingCycle()[¶](#ApiClient.TsCallRead.GetPollingCycle "Link to this definition")  
Returns the polling cycle of the test step’s time option, if a corresponding option has been set.

Returns:  The polling cycle, else None

Return type:  string

GetPollingCycleUnit()[¶](#ApiClient.TsCallRead.GetPollingCycleUnit "Link to this definition")  
Returns the unit of the polling cycle of the test step’s time option, if a corresponding option has been set.

Returns:  The unit of the polling cycle, else None

Return type:  string

GetReturnNames()[¶](#ApiClient.TsCallRead.GetReturnNames "Link to this definition")  
Returns the names of the return values defined in the test step.

Info

If the test step was created without a mapping item, or if the data base describing the target of the mapping item was not loaded, this list is initially empty. You can use [`AddReturnValue()`](#ApiClient.TsCallRead.AddReturnValue "ApiClient.TsCallRead.AddReturnValue (Python method) — Adds a return value to the test step.") or [`UpdateInterface()`](#ApiClient.TsCallRead.UpdateInterface "ApiClient.TsCallRead.UpdateInterface (Python method) — Updates the list of parameters and return values according to the assigned mapping target:") to populate it.

Returns:  Return value names

Return type:  list[str]

GetReturnValueExpectation(*[returnName](#ApiClient.TsCallRead.GetReturnValueExpectation.returnName "ApiClient.TsCallRead.GetReturnValueExpectation.returnName (Python parameter) — name of the return value")*)[¶](#ApiClient.TsCallRead.GetReturnValueExpectation "Link to this definition")  
Returns the expectation for the specified return value

Parameters:  returnName : str[¶](#ApiClient.TsCallRead.GetReturnValueExpectation.returnName "Permalink to this definition")  
name of the return value

Returns:  expectation

Return type:  [`Expectation`](../ExpectationApi/Expectation.md#ApiClient.Expectation "ApiClient.Expectation (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")

GetReturnValueRepresentation(*[returnName](#ApiClient.TsCallRead.GetReturnValueRepresentation.returnName "ApiClient.TsCallRead.GetReturnValueRepresentation.returnName (Python parameter) — name of the return value")*)[¶](#ApiClient.TsCallRead.GetReturnValueRepresentation "Link to this definition")  
Returns the representation used for the specified return value

Parameters:  returnName : str[¶](#ApiClient.TsCallRead.GetReturnValueRepresentation.returnName "Permalink to this definition")  
name of the return value

Returns:  representation used for the return value

Return type:  str

GetReturnValueSaveIn(*[returnName](#ApiClient.TsCallRead.GetReturnValueSaveIn.returnName "ApiClient.TsCallRead.GetReturnValueSaveIn.returnName (Python parameter) — name of the return value")*)[¶](#ApiClient.TsCallRead.GetReturnValueSaveIn "Link to this definition")  
Returns the variable name to save the specified return value in

Parameters:  returnName : str[¶](#ApiClient.TsCallRead.GetReturnValueSaveIn.returnName "Permalink to this definition")  
name of the return value

Returns:  variable name

Return type:  str

GetReturnValueUnit(*[returnName](#ApiClient.TsCallRead.GetReturnValueUnit.returnName "ApiClient.TsCallRead.GetReturnValueUnit.returnName (Python parameter) — name of the return value")*)[¶](#ApiClient.TsCallRead.GetReturnValueUnit "Link to this definition")  
Returns the unit for the specified return value

Parameters:  returnName : str[¶](#ApiClient.TsCallRead.GetReturnValueUnit.returnName "Permalink to this definition")  
name of the return value

Returns:  Unit used by the `~ApiClient.PHYS` representation for this return value

Return type:  str

GetTags()[¶](#ApiClient.TsCallRead.GetTags "Link to this definition")  
Returns the tags set for this step.

Returns:  A (sorted) list of tags

Return type:  list[str]

GetTestManagementId()[¶](#ApiClient.TsCallRead.GetTestManagementId "Link to this definition")  
Returns the test management id of the test step.

Returns:  Test step id.

Return type:  str

GetTestStepId()[¶](#ApiClient.TsCallRead.GetTestStepId "Link to this definition")  
Returns the test step id.

Returns:  test step id

Return type:  str

GetTimeout()[¶](#ApiClient.TsCallRead.GetTimeout "Link to this definition")  
Returns the timeout of the test step’s time option, if a corresponding option has been set.

Returns:  The timeout else None

Return type:  string

GetTimeoutUnit()[¶](#ApiClient.TsCallRead.GetTimeoutUnit "Link to this definition")  
Returns the unit of the timeout of the test step’s time option, if a corresponding option has been set.

Returns:  The unit of the timeout else None

Return type:  string

GetTranslatedCommentText(*[language](#ApiClient.TsCallRead.GetTranslatedCommentText.language "ApiClient.TsCallRead.GetTranslatedCommentText.language (Python parameter) — Language of the requested text ('en_US', 'de_DE', 'zh_CN')")*)[¶](#ApiClient.TsCallRead.GetTranslatedCommentText "Link to this definition")  
Returns the text value of the “comment” column in the given language.

Parameters:  language : str[¶](#ApiClient.TsCallRead.GetTranslatedCommentText.language "Permalink to this definition")  
Language of the requested text (‘en_US’, ‘de_DE’, ‘zh_CN’)

Returns:  Comment column text

Return type:  str

GetType()[¶](#ApiClient.TsCallRead.GetType "Link to this definition")  
Returns the type (class name) of the test step, e.g.

- “TsPreconditionBlock”

- “TsWait”

- “TsIfThenElse”

- “TsSwitchCase”

- “TsCaseNode”

Returns:  Type (class name) of the test step

Return type:  str

GetValueColumnText()[¶](#ApiClient.TsCallRead.GetValueColumnText "Link to this definition")  
Returns the text value of the “value” column in your current test case language.

Returns:  Value column text

Return type:  str

IsBreakpoint()[¶](#ApiClient.TsCallRead.IsBreakpoint "Link to this definition")  
Checks whether the test step is a break point.

Returns:  True if test step is a break point, else False

Return type:  boolean

IsContainer()[¶](#ApiClient.TsCallRead.IsContainer "Link to this definition")  
Checks whether this test step can contain test steps

Returns:  True if it can contain test steps, else False

Return type:  boolean

IsEnabled()[¶](#ApiClient.TsCallRead.IsEnabled "Link to this definition")  
Returns the state of the test step.

Returns:  True if test step is enabled, otherwise False

Return type:  bool

IsInPostcondition()[¶](#ApiClient.TsCallRead.IsInPostcondition "Link to this definition")  
Returns True if the test step is located in a postcondition

Returns:  True if the test step is located in a postcondition, else Flase

Return type:  bool

IsInPrecondition()[¶](#ApiClient.TsCallRead.IsInPrecondition "Link to this definition")  
Returns True if the test step is located in a precondition

Returns:  True if the test step is located in a precondition, else False

Return type:  bool

IsOk()[¶](#ApiClient.TsCallRead.IsOk "Link to this definition")  
Returns the internal state of correctness of the test step.

Returns:  True if no problems were found, else False

Return type:  boolean

IsVisible()[¶](#ApiClient.TsCallRead.IsVisible "Link to this definition")  
Checks whether the test step is visible. This depends on the test step itself or a parent test step being disabled.

Returns:  True if test step is visible, else False

Return type:  boolean

RemovePacketExpectation()[¶](#ApiClient.TsCallRead.RemovePacketExpectation "Link to this definition")  
Removes the expectation for the packet. Only applicable if this test step is mapped to a service method/event.

RemoveTag(*[tag](#ApiClient.TsCallRead.RemoveTag.tag "ApiClient.TsCallRead.RemoveTag.tag (Python parameter) — The tag to be removed")*)[¶](#ApiClient.TsCallRead.RemoveTag "Link to this definition")  
Remove a specific tag from this step.

Parameters:  tag : str[¶](#ApiClient.TsCallRead.RemoveTag.tag "Permalink to this definition")  
The tag to be removed

SetBreakpoint(*[enable](#ApiClient.TsCallRead.SetBreakpoint.enable "ApiClient.TsCallRead.SetBreakpoint.enable (Python parameter) — True if test step is a break point, else False")*)[¶](#ApiClient.TsCallRead.SetBreakpoint "Link to this definition")  
Sets or unsets the test step to act as a break point.

Parameters:  enable : boolean[¶](#ApiClient.TsCallRead.SetBreakpoint.enable "Permalink to this definition")  
True if test step is a break point, else False

SetComment(*[comment](#ApiClient.TsCallRead.SetComment.comment "ApiClient.TsCallRead.SetComment.comment (Python parameter) — Text to be displayed in the comment tab")*)[¶](#ApiClient.TsCallRead.SetComment "Link to this definition")  
Sets a comment for the test step in the current test case language.

Parameters:  comment : str[¶](#ApiClient.TsCallRead.SetComment.comment "Permalink to this definition")  
Text to be displayed in the comment tab

SetCyclic(*[cyclicState](#ApiClient.TsCallRead.SetCyclic.cyclicState "ApiClient.TsCallRead.SetCyclic.cyclicState (Python parameter) — possible values are:")*, *[cycleTimeExpression](#ApiClient.TsCallRead.SetCyclic.cycleTimeExpression "ApiClient.TsCallRead.SetCyclic.cycleTimeExpression (Python parameter) — in milliseconds, necessary for cyclicState 'on'")=`None`*)[¶](#ApiClient.TsCallRead.SetCyclic "Link to this definition")  
Changes the send cyclic settings for a test step that has call mode ‘SEND_EVENT’

Raises:  
**ApiError** – if the test step doesn’t support cyclic sending

Parameters:  cyclicState : str[¶](#ApiClient.TsCallRead.SetCyclic.cyclicState "Permalink to this definition")  
possible values are:

- ’on’ enables cyclic sending using the specified cycleTimeExpression

- ’off’ disables cyclic sending

- ’unchanged’ keeps cyclic sending (e.g. if just the event’s values should be changed)

- None removes cyclic settings so the test step will send the event just once

cycleTimeExpression : str[¶](#ApiClient.TsCallRead.SetCyclic.cycleTimeExpression "Permalink to this definition")  
in milliseconds, necessary for cyclicState ‘on’

SetEnabled(*[state](#ApiClient.TsCallRead.SetEnabled.state "ApiClient.TsCallRead.SetEnabled.state (Python parameter) — True (Default) to enable, False to disable the test step.")=`True`*)[¶](#ApiClient.TsCallRead.SetEnabled "Link to this definition")  
Enable or disable the test step.

Parameters:  state : bool[¶](#ApiClient.TsCallRead.SetEnabled.state "Permalink to this definition")  
True (Default) to enable, False to disable the test step.

SetIgnoreResponse(*[ignoreResponse](#ApiClient.TsCallRead.SetIgnoreResponse.ignoreResponse "ApiClient.TsCallRead.SetIgnoreResponse.ignoreResponse (Python parameter) — Sets the value of the option.")*)[¶](#ApiClient.TsCallRead.SetIgnoreResponse "Link to this definition")  
Sets test step’s option for ignoring its response.

Raises:  
**ApiError** – If not return values or ignoring the response is not supported the option does not make sense.

Parameters:  ignoreResponse : bool[¶](#ApiClient.TsCallRead.SetIgnoreResponse.ignoreResponse "Permalink to this definition")  
Sets the value of the option.

SetPacketExpectation(*[expectationExpression](#ApiClient.TsCallRead.SetPacketExpectation.expectationExpression "ApiClient.TsCallRead.SetPacketExpectation.expectationExpression (Python parameter) — expectation for the return value")*)[¶](#ApiClient.TsCallRead.SetPacketExpectation "Link to this definition")  
Sets the expectation for the packet. Only applicable if this test step is mapped to a service method/event.

This should be a [`ExpressionExpectation`](../ExpectationApi/ExpressionExpectation.md#ApiClient.ExpressionExpectation "ApiClient.ExpressionExpectation (Python class) — ExpectationApi.CreateExpressionExpectation") referencing the packet as `value`, a [`PresentExpectation`](../ExpectationApi/PresentExpectation.md#ApiClient.PresentExpectation "ApiClient.PresentExpectation (Python class) — ExpectationApi.CreatePresentExpectation"), or a [`NotPresentExpectation`](../ExpectationApi/NotPresentExpectation.md#ApiClient.NotPresentExpectation "ApiClient.NotPresentExpectation (Python class) — ExpectationApi.CreateNotPresentExpectation").

Keep in mind that the `value` object can not only be a `PacketSomeIp` but also NotPresent.

Parameters:  expectationExpression[¶](#ApiClient.TsCallRead.SetPacketExpectation.expectationExpression "Permalink to this definition")  
expectation for the return value

SetParameterRepresentation(*[parameterName](#ApiClient.TsCallRead.SetParameterRepresentation.parameterName "ApiClient.TsCallRead.SetParameterRepresentation.parameterName (Python parameter) — name of the parameter")*, *[repr](#ApiClient.TsCallRead.SetParameterRepresentation.repr "ApiClient.TsCallRead.SetParameterRepresentation.repr (Python parameter) — representation to use for the parameter. One of ~ApiClient.PHYS, ~ApiClient.RAW, ~ApiClient.TEXT or ~ApiClient.BITS")*)[¶](#ApiClient.TsCallRead.SetParameterRepresentation "Link to this definition")  
Sets the representation for the specified parameter

This method only works with existing parameters. To add a parameter please use [`AddParameter()`](#ApiClient.TsCallRead.AddParameter "ApiClient.TsCallRead.AddParameter (Python method) — Adds a parameter to the test step.")

Parameters:  parameterName : str[¶](#ApiClient.TsCallRead.SetParameterRepresentation.parameterName "Permalink to this definition")  
name of the parameter

repr : str[¶](#ApiClient.TsCallRead.SetParameterRepresentation.repr "Permalink to this definition")  
representation to use for the parameter. One of `~ApiClient.PHYS`, `~ApiClient.RAW`, `~ApiClient.TEXT` or `~ApiClient.BITS`

SetParameterUnit(*[parameterName](#ApiClient.TsCallRead.SetParameterUnit.parameterName "ApiClient.TsCallRead.SetParameterUnit.parameterName (Python parameter) — name of the parameter")*, *[unit](#ApiClient.TsCallRead.SetParameterUnit.unit "ApiClient.TsCallRead.SetParameterUnit.unit (Python parameter) — Unit to use for the ~ApiClient.PHYS representation for this parameter")*)[¶](#ApiClient.TsCallRead.SetParameterUnit "Link to this definition")  
Sets the unit for the specified parameter

This method only works with existing parameters. To add a parameter please use [`AddParameter()`](#ApiClient.TsCallRead.AddParameter "ApiClient.TsCallRead.AddParameter (Python method) — Adds a parameter to the test step.")

Parameters:  parameterName : str[¶](#ApiClient.TsCallRead.SetParameterUnit.parameterName "Permalink to this definition")  
name of the parameter

unit : str[¶](#ApiClient.TsCallRead.SetParameterUnit.unit "Permalink to this definition")  
Unit to use for the `~ApiClient.PHYS` representation for this parameter

SetParameterValue(*[parameterName](#ApiClient.TsCallRead.SetParameterValue.parameterName "ApiClient.TsCallRead.SetParameterValue.parameterName (Python parameter) — name of the parameter")*, *[valueExpression](#ApiClient.TsCallRead.SetParameterValue.valueExpression "ApiClient.TsCallRead.SetParameterValue.valueExpression (Python parameter) — expression to use for the parameter's value")*)[¶](#ApiClient.TsCallRead.SetParameterValue "Link to this definition")  
Assigns a new expression to use the specified parameter’s value

This method only works with existing parameters. To add a parameter please use [`AddParameter()`](#ApiClient.TsCallRead.AddParameter "ApiClient.TsCallRead.AddParameter (Python method) — Adds a parameter to the test step.")

Parameters:  parameterName : str[¶](#ApiClient.TsCallRead.SetParameterValue.parameterName "Permalink to this definition")  
name of the parameter

valueExpression : str[¶](#ApiClient.TsCallRead.SetParameterValue.valueExpression "Permalink to this definition")  
expression to use for the parameter’s value

SetReturnValueExpectation(*[returnName](#ApiClient.TsCallRead.SetReturnValueExpectation.returnName "ApiClient.TsCallRead.SetReturnValueExpectation.returnName (Python parameter) — name of the return value")*, *[expectationExpression](#ApiClient.TsCallRead.SetReturnValueExpectation.expectationExpression "ApiClient.TsCallRead.SetReturnValueExpectation.expectationExpression (Python parameter) — expectation for the return value")*)[¶](#ApiClient.TsCallRead.SetReturnValueExpectation "Link to this definition")  
Sets the expectation for the specified return value.

This method only works with existing return values. To add a return value please use [`AddReturnValue()`](#ApiClient.TsCallRead.AddReturnValue "ApiClient.TsCallRead.AddReturnValue (Python method) — Adds a return value to the test step.")

Parameters:  returnName : str[¶](#ApiClient.TsCallRead.SetReturnValueExpectation.returnName "Permalink to this definition")  
name of the return value

expectationExpression[¶](#ApiClient.TsCallRead.SetReturnValueExpectation.expectationExpression "Permalink to this definition")  
expectation for the return value

SetReturnValueRepresentation(*[returnName](#ApiClient.TsCallRead.SetReturnValueRepresentation.returnName "ApiClient.TsCallRead.SetReturnValueRepresentation.returnName (Python parameter) — name of the return value")*, *[repr](#ApiClient.TsCallRead.SetReturnValueRepresentation.repr "ApiClient.TsCallRead.SetReturnValueRepresentation.repr (Python parameter) — representation to use for the return value. One of ~ApiClient.PHYS, ~ApiClient.RAW, ~ApiClient.TEXT or ~ApiClient.BITS")*)[¶](#ApiClient.TsCallRead.SetReturnValueRepresentation "Link to this definition")  
Sets the representation for the specified return value

This method only works with existing return values. To add a return value please use [`AddReturnValue()`](#ApiClient.TsCallRead.AddReturnValue "ApiClient.TsCallRead.AddReturnValue (Python method) — Adds a return value to the test step.")

Parameters:  returnName : str[¶](#ApiClient.TsCallRead.SetReturnValueRepresentation.returnName "Permalink to this definition")  
name of the return value

repr : str[¶](#ApiClient.TsCallRead.SetReturnValueRepresentation.repr "Permalink to this definition")  
representation to use for the return value. One of `~ApiClient.PHYS`, `~ApiClient.RAW`, `~ApiClient.TEXT` or `~ApiClient.BITS`

SetReturnValueSaveIn(*[returnName](#ApiClient.TsCallRead.SetReturnValueSaveIn.returnName "ApiClient.TsCallRead.SetReturnValueSaveIn.returnName (Python parameter) — name of the return value")*, *[saveInVariableName](#ApiClient.TsCallRead.SetReturnValueSaveIn.saveInVariableName "ApiClient.TsCallRead.SetReturnValueSaveIn.saveInVariableName (Python parameter) — variable name")*)[¶](#ApiClient.TsCallRead.SetReturnValueSaveIn "Link to this definition")  
Sets the variable name to save the specified return value in

This method only works with existing return values. To add a return value please use [`AddReturnValue()`](#ApiClient.TsCallRead.AddReturnValue "ApiClient.TsCallRead.AddReturnValue (Python method) — Adds a return value to the test step.")

Parameters:  returnName : str[¶](#ApiClient.TsCallRead.SetReturnValueSaveIn.returnName "Permalink to this definition")  
name of the return value

saveInVariableName : str[¶](#ApiClient.TsCallRead.SetReturnValueSaveIn.saveInVariableName "Permalink to this definition")  
variable name

SetReturnValueUnit(*[returnName](#ApiClient.TsCallRead.SetReturnValueUnit.returnName "ApiClient.TsCallRead.SetReturnValueUnit.returnName (Python parameter) — name of the return value")*, *[unit](#ApiClient.TsCallRead.SetReturnValueUnit.unit "ApiClient.TsCallRead.SetReturnValueUnit.unit (Python parameter) — Unit to use for the ~ApiClient.PHYS representation for this return value")*)[¶](#ApiClient.TsCallRead.SetReturnValueUnit "Link to this definition")  
Sets the unit for the specified return value

This method only works with existing return values. To add a return value please use [`AddReturnValue()`](#ApiClient.TsCallRead.AddReturnValue "ApiClient.TsCallRead.AddReturnValue (Python method) — Adds a return value to the test step.")

Parameters:  returnName : str[¶](#ApiClient.TsCallRead.SetReturnValueUnit.returnName "Permalink to this definition")  
name of the return value

unit : str[¶](#ApiClient.TsCallRead.SetReturnValueUnit.unit "Permalink to this definition")  
Unit to use for the `~ApiClient.PHYS` representation for this return value

SetTags(*[tags](#ApiClient.TsCallRead.SetTags.tags "ApiClient.TsCallRead.SetTags.tags (Python parameter) — The list of tags")*)[¶](#ApiClient.TsCallRead.SetTags "Link to this definition")  
Set the list of tags for this step. The list of tags will be sorted and stored.

Parameters:  tags : list[str][¶](#ApiClient.TsCallRead.SetTags.tags "Permalink to this definition")  
The list of tags

SetTestManagementId(*[testManagementId](#ApiClient.TsCallRead.SetTestManagementId.testManagementId "ApiClient.TsCallRead.SetTestManagementId.testManagementId (Python parameter) — Test management id of the test step")*)[¶](#ApiClient.TsCallRead.SetTestManagementId "Link to this definition")  
Sets the test management id of the test step.

Parameters:  testManagementId : str[¶](#ApiClient.TsCallRead.SetTestManagementId.testManagementId "Permalink to this definition")  
Test management id of the test step

SetTimeOptionOnlySynchronization(*[timeout](#ApiClient.TsCallRead.SetTimeOptionOnlySynchronization.timeout "ApiClient.TsCallRead.SetTimeOptionOnlySynchronization.timeout (Python parameter) — The timeout to be used")*, *[pollingCycle](#ApiClient.TsCallRead.SetTimeOptionOnlySynchronization.pollingCycle "ApiClient.TsCallRead.SetTimeOptionOnlySynchronization.pollingCycle (Python parameter) — Optional polling cycle to be used")=`None`*, *[timeoutUnit](#ApiClient.TsCallRead.SetTimeOptionOnlySynchronization.timeoutUnit "ApiClient.TsCallRead.SetTimeOptionOnlySynchronization.timeoutUnit (Python parameter) — Optional unit for the timeout (ms, s, min, h or d)")=`'ms'`*, *[pollingCycleUnit](#ApiClient.TsCallRead.SetTimeOptionOnlySynchronization.pollingCycleUnit "ApiClient.TsCallRead.SetTimeOptionOnlySynchronization.pollingCycleUnit (Python parameter) — Optional unit for the polling cycle (ms, s, min, h or d)")=`'ms'`*)[¶](#ApiClient.TsCallRead.SetTimeOptionOnlySynchronization "Link to this definition")  
Sets the test step’s time option to “only synchronization”.

Raises:  
**ApiError** – If no return value has an expectation, no time option can be set.

Parameters:  timeout : string[¶](#ApiClient.TsCallRead.SetTimeOptionOnlySynchronization.timeout "Permalink to this definition")  
The timeout to be used

pollingCycle : string[¶](#ApiClient.TsCallRead.SetTimeOptionOnlySynchronization.pollingCycle "Permalink to this definition")  
Optional polling cycle to be used

timeoutUnit : string[¶](#ApiClient.TsCallRead.SetTimeOptionOnlySynchronization.timeoutUnit "Permalink to this definition")  
Optional unit for the timeout (ms, s, min, h or d)

pollingCycleUnit : string[¶](#ApiClient.TsCallRead.SetTimeOptionOnlySynchronization.pollingCycleUnit "Permalink to this definition")  
Optional unit for the polling cycle (ms, s, min, h or d)

SetTimeOptionPollingCycleMultiplier(*[pollingCycleMultiplier](#ApiClient.TsCallRead.SetTimeOptionPollingCycleMultiplier.pollingCycleMultiplier "ApiClient.TsCallRead.SetTimeOptionPollingCycleMultiplier.pollingCycleMultiplier (Python parameter) — The polling cycle multiplier to be used.")*)[¶](#ApiClient.TsCallRead.SetTimeOptionPollingCycleMultiplier "Link to this definition")  
Sets the test step’s time option to “polling cycle multiplier”. This option must only be used when inserting the test step into a Multi-Check!

Parameters:  pollingCycleMultiplier : string[¶](#ApiClient.TsCallRead.SetTimeOptionPollingCycleMultiplier.pollingCycleMultiplier "Permalink to this definition")  
The polling cycle multiplier to be used.

SetTimeOptionTrueForAtLeast(*[minimumDuration](#ApiClient.TsCallRead.SetTimeOptionTrueForAtLeast.minimumDuration "ApiClient.TsCallRead.SetTimeOptionTrueForAtLeast.minimumDuration (Python parameter) — The minimum duration to be used")*, *[pollingCycle](#ApiClient.TsCallRead.SetTimeOptionTrueForAtLeast.pollingCycle "ApiClient.TsCallRead.SetTimeOptionTrueForAtLeast.pollingCycle (Python parameter) — Optional polling cycle to be used")=`None`*, *[timeoutUnit](#ApiClient.TsCallRead.SetTimeOptionTrueForAtLeast.timeoutUnit "ApiClient.TsCallRead.SetTimeOptionTrueForAtLeast.timeoutUnit (Python parameter) — Optional unit for the timeout (ms, s, min, h or d)")=`'ms'`*, *[pollingCycleUnit](#ApiClient.TsCallRead.SetTimeOptionTrueForAtLeast.pollingCycleUnit "ApiClient.TsCallRead.SetTimeOptionTrueForAtLeast.pollingCycleUnit (Python parameter) — Optional unit for the polling cycle (ms, s, min, h or d)")=`'ms'`*)[¶](#ApiClient.TsCallRead.SetTimeOptionTrueForAtLeast "Link to this definition")  
Sets the test step’s time option to “true for at least”.

Raises:  
**ApiError** – If no return value has an expectation, no time option can be set.

Parameters:  minimumDuration : string[¶](#ApiClient.TsCallRead.SetTimeOptionTrueForAtLeast.minimumDuration "Permalink to this definition")  
The minimum duration to be used

pollingCycle : string[¶](#ApiClient.TsCallRead.SetTimeOptionTrueForAtLeast.pollingCycle "Permalink to this definition")  
Optional polling cycle to be used

timeoutUnit : string[¶](#ApiClient.TsCallRead.SetTimeOptionTrueForAtLeast.timeoutUnit "Permalink to this definition")  
Optional unit for the timeout (ms, s, min, h or d)

pollingCycleUnit : string[¶](#ApiClient.TsCallRead.SetTimeOptionTrueForAtLeast.pollingCycleUnit "Permalink to this definition")  
Optional unit for the polling cycle (ms, s, min, h or d)

SetTimeOptionTrueForAtLeastWithin(*[minimumDuration](#ApiClient.TsCallRead.SetTimeOptionTrueForAtLeastWithin.minimumDuration "ApiClient.TsCallRead.SetTimeOptionTrueForAtLeastWithin.minimumDuration (Python parameter) — The minimum duration to be used")*, *[timeout](#ApiClient.TsCallRead.SetTimeOptionTrueForAtLeastWithin.timeout "ApiClient.TsCallRead.SetTimeOptionTrueForAtLeastWithin.timeout (Python parameter) — The timeout to be used")*, *[pollingCycle](#ApiClient.TsCallRead.SetTimeOptionTrueForAtLeastWithin.pollingCycle "ApiClient.TsCallRead.SetTimeOptionTrueForAtLeastWithin.pollingCycle (Python parameter) — Optional polling cycle to be used")=`None`*, *[timeoutUnit](#ApiClient.TsCallRead.SetTimeOptionTrueForAtLeastWithin.timeoutUnit "ApiClient.TsCallRead.SetTimeOptionTrueForAtLeastWithin.timeoutUnit (Python parameter) — Optional unit for the timeout (ms, s, min, h or d)")=`'ms'`*, *[pollingCycleUnit](#ApiClient.TsCallRead.SetTimeOptionTrueForAtLeastWithin.pollingCycleUnit "ApiClient.TsCallRead.SetTimeOptionTrueForAtLeastWithin.pollingCycleUnit (Python parameter) — Optional unit for the polling cycle (ms, s, min, h or d)")=`'ms'`*)[¶](#ApiClient.TsCallRead.SetTimeOptionTrueForAtLeastWithin "Link to this definition")  
Sets the test step’s time option to “true for at least … within …”.

Raises:  
**ApiError** – If no return value has an expectation, no time option can be set.

Parameters:  minimumDuration : string[¶](#ApiClient.TsCallRead.SetTimeOptionTrueForAtLeastWithin.minimumDuration "Permalink to this definition")  
The minimum duration to be used

timeout : string[¶](#ApiClient.TsCallRead.SetTimeOptionTrueForAtLeastWithin.timeout "Permalink to this definition")  
The timeout to be used

pollingCycle : string[¶](#ApiClient.TsCallRead.SetTimeOptionTrueForAtLeastWithin.pollingCycle "Permalink to this definition")  
Optional polling cycle to be used

timeoutUnit : string[¶](#ApiClient.TsCallRead.SetTimeOptionTrueForAtLeastWithin.timeoutUnit "Permalink to this definition")  
Optional unit for the timeout (ms, s, min, h or d)

pollingCycleUnit : string[¶](#ApiClient.TsCallRead.SetTimeOptionTrueForAtLeastWithin.pollingCycleUnit "Permalink to this definition")  
Optional unit for the polling cycle (ms, s, min, h or d)

SetTimeOptionWaitUntilTrue(*[timeout](#ApiClient.TsCallRead.SetTimeOptionWaitUntilTrue.timeout "ApiClient.TsCallRead.SetTimeOptionWaitUntilTrue.timeout (Python parameter) — The timeout to be used")*, *[pollingCycle](#ApiClient.TsCallRead.SetTimeOptionWaitUntilTrue.pollingCycle "ApiClient.TsCallRead.SetTimeOptionWaitUntilTrue.pollingCycle (Python parameter) — Optional polling cycle to be used")=`None`*, *[timeoutUnit](#ApiClient.TsCallRead.SetTimeOptionWaitUntilTrue.timeoutUnit "ApiClient.TsCallRead.SetTimeOptionWaitUntilTrue.timeoutUnit (Python parameter) — Optional unit for the timeout (ms, s, min, h or d)")=`'ms'`*, *[pollingCycleUnit](#ApiClient.TsCallRead.SetTimeOptionWaitUntilTrue.pollingCycleUnit "ApiClient.TsCallRead.SetTimeOptionWaitUntilTrue.pollingCycleUnit (Python parameter) — Optional unit for the polling cycle (ms, s, min, h or d)")=`'ms'`*)[¶](#ApiClient.TsCallRead.SetTimeOptionWaitUntilTrue "Link to this definition")  
Sets the test step’s time option to “wait until true”.

Raises:  
**ApiError** – If no return value has an expectation, no time option can be set.

Parameters:  timeout : string[¶](#ApiClient.TsCallRead.SetTimeOptionWaitUntilTrue.timeout "Permalink to this definition")  
The timeout to be used

pollingCycle : string[¶](#ApiClient.TsCallRead.SetTimeOptionWaitUntilTrue.pollingCycle "Permalink to this definition")  
Optional polling cycle to be used

timeoutUnit : string[¶](#ApiClient.TsCallRead.SetTimeOptionWaitUntilTrue.timeoutUnit "Permalink to this definition")  
Optional unit for the timeout (ms, s, min, h or d)

pollingCycleUnit : string[¶](#ApiClient.TsCallRead.SetTimeOptionWaitUntilTrue.pollingCycleUnit "Permalink to this definition")  
Optional unit for the polling cycle (ms, s, min, h or d)

SetTranslatedCommentText(*[comment](#ApiClient.TsCallRead.SetTranslatedCommentText.comment "ApiClient.TsCallRead.SetTranslatedCommentText.comment (Python parameter) — Text to be displayed")*, *[language](#ApiClient.TsCallRead.SetTranslatedCommentText.language "ApiClient.TsCallRead.SetTranslatedCommentText.language (Python parameter) — Language of the text ('en_US', 'de_DE', 'zh_CN')")*)[¶](#ApiClient.TsCallRead.SetTranslatedCommentText "Link to this definition")  
Sets a comment for the test step in the given language.

Parameters:  comment : str[¶](#ApiClient.TsCallRead.SetTranslatedCommentText.comment "Permalink to this definition")  
Text to be displayed

language : str[¶](#ApiClient.TsCallRead.SetTranslatedCommentText.language "Permalink to this definition")  
Language of the text (‘en_US’, ‘de_DE’, ‘zh_CN’)

UpdateInterface()[¶](#ApiClient.TsCallRead.UpdateInterface "Link to this definition")  
Updates the list of parameters and return values according to the assigned mapping target:

- Removes any parameters and return values not available in the assigned mapping target

- Adds any missing parameters and return values defined in the assigned mapping target. Parameters are assigned a default value. Return values are not assigned any expectation.

Parameters and return values existing in both the test step and the mapping target are left as they are, which might in some cases result in an incompatible representation or unit.

Info

This only works if the test step is associated with an appropriate mappingItem (via a package, via a global mapping, or via the `~ApiClient.mappingItem` parameter of the [`CreateTsCall()`](../TestStepApi.md#ApiClient.TestStepApi.CreateTsCall "ApiClient.TestStepApi.CreateTsCall (Python method) — Creates a call test step.") method) and the database describing the target of the mapping item is loaded.

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
