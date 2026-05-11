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

TsCall [ TsCall ](#)

TsCall

- [C TsCall ](#ApiClient.TsCall)
  - [M AddParameter ](#ApiClient.TsCall.AddParameter)
  - [M AddReturnValue ](#ApiClient.TsCall.AddReturnValue)
  - [M AddTag ](#ApiClient.TsCall.AddTag)
  - [M Clone ](#ApiClient.TsCall.Clone)
  - [M DeactivateReturnValueExpectation ](#ApiClient.TsCall.DeactivateReturnValueExpectation)
  - [M DeactivateReturnValueSaveIn ](#ApiClient.TsCall.DeactivateReturnValueSaveIn)
  - [M DeactivateTimeOption ](#ApiClient.TsCall.DeactivateTimeOption)
  - [M DeleteParameter ](#ApiClient.TsCall.DeleteParameter)
  - [M DeleteReturnValue ](#ApiClient.TsCall.DeleteReturnValue)
  - [M DeleteTranslatedCommentText ](#ApiClient.TsCall.DeleteTranslatedCommentText)
  - [M GetActionColumnText ](#ApiClient.TsCall.GetActionColumnText)
  - [M GetActiveTimeOptionType ](#ApiClient.TsCall.GetActiveTimeOptionType)
  - [M GetComment ](#ApiClient.TsCall.GetComment)
  - [M GetCommentColumnText ](#ApiClient.TsCall.GetCommentColumnText)
  - [M GetCycleTimeExpression ](#ApiClient.TsCall.GetCycleTimeExpression)
  - [M GetCyclicState ](#ApiClient.TsCall.GetCyclicState)
  - [M GetError ](#ApiClient.TsCall.GetError)
  - [M GetIgnoreResponse ](#ApiClient.TsCall.GetIgnoreResponse)
  - [M GetIndex ](#ApiClient.TsCall.GetIndex)
  - [M GetLineNo ](#ApiClient.TsCall.GetLineNo)
  - [M GetMappingItemReferenceName ](#ApiClient.TsCall.GetMappingItemReferenceName)
  - [M GetMinimumDuration ](#ApiClient.TsCall.GetMinimumDuration)
  - [M GetMinimumDurationUnit ](#ApiClient.TsCall.GetMinimumDurationUnit)
  - [M GetPacketExpectation ](#ApiClient.TsCall.GetPacketExpectation)
  - [M GetParameterColumnText ](#ApiClient.TsCall.GetParameterColumnText)
  - [M GetParameterNames ](#ApiClient.TsCall.GetParameterNames)
  - [M GetParameterRepresentation ](#ApiClient.TsCall.GetParameterRepresentation)
  - [M GetParameterUnit ](#ApiClient.TsCall.GetParameterUnit)
  - [M GetParameterValue ](#ApiClient.TsCall.GetParameterValue)
  - [M GetParent ](#ApiClient.TsCall.GetParent)
  - [M GetPollingCycle ](#ApiClient.TsCall.GetPollingCycle)
  - [M GetPollingCycleUnit ](#ApiClient.TsCall.GetPollingCycleUnit)
  - [M GetReturnNames ](#ApiClient.TsCall.GetReturnNames)
  - [M GetReturnValueExpectation ](#ApiClient.TsCall.GetReturnValueExpectation)
  - [M GetReturnValueRepresentation ](#ApiClient.TsCall.GetReturnValueRepresentation)
  - [M GetReturnValueSaveIn ](#ApiClient.TsCall.GetReturnValueSaveIn)
  - [M GetReturnValueUnit ](#ApiClient.TsCall.GetReturnValueUnit)
  - [M GetTags ](#ApiClient.TsCall.GetTags)
  - [M GetTestManagementId ](#ApiClient.TsCall.GetTestManagementId)
  - [M GetTestStepId ](#ApiClient.TsCall.GetTestStepId)
  - [M GetTimeout ](#ApiClient.TsCall.GetTimeout)
  - [M GetTimeoutUnit ](#ApiClient.TsCall.GetTimeoutUnit)
  - [M GetTranslatedCommentText ](#ApiClient.TsCall.GetTranslatedCommentText)
  - [M GetType ](#ApiClient.TsCall.GetType)
  - [M GetValueColumnText ](#ApiClient.TsCall.GetValueColumnText)
  - [M IsBreakpoint ](#ApiClient.TsCall.IsBreakpoint)
  - [M IsContainer ](#ApiClient.TsCall.IsContainer)
  - [M IsEnabled ](#ApiClient.TsCall.IsEnabled)
  - [M IsInPostcondition ](#ApiClient.TsCall.IsInPostcondition)
  - [M IsInPrecondition ](#ApiClient.TsCall.IsInPrecondition)
  - [M IsOk ](#ApiClient.TsCall.IsOk)
  - [M IsVisible ](#ApiClient.TsCall.IsVisible)
  - [M RemovePacketExpectation ](#ApiClient.TsCall.RemovePacketExpectation)
  - [M RemoveTag ](#ApiClient.TsCall.RemoveTag)
  - [M SetBreakpoint ](#ApiClient.TsCall.SetBreakpoint)
  - [M SetComment ](#ApiClient.TsCall.SetComment)
  - [M SetCyclic ](#ApiClient.TsCall.SetCyclic)
  - [M SetEnabled ](#ApiClient.TsCall.SetEnabled)
  - [M SetIgnoreResponse ](#ApiClient.TsCall.SetIgnoreResponse)
  - [M SetPacketExpectation ](#ApiClient.TsCall.SetPacketExpectation)
  - [M SetParameterRepresentation ](#ApiClient.TsCall.SetParameterRepresentation)
  - [M SetParameterUnit ](#ApiClient.TsCall.SetParameterUnit)
  - [M SetParameterValue ](#ApiClient.TsCall.SetParameterValue)
  - [M SetReturnValueExpectation ](#ApiClient.TsCall.SetReturnValueExpectation)
  - [M SetReturnValueRepresentation ](#ApiClient.TsCall.SetReturnValueRepresentation)
  - [M SetReturnValueSaveIn ](#ApiClient.TsCall.SetReturnValueSaveIn)
  - [M SetReturnValueUnit ](#ApiClient.TsCall.SetReturnValueUnit)
  - [M SetTags ](#ApiClient.TsCall.SetTags)
  - [M SetTestManagementId ](#ApiClient.TsCall.SetTestManagementId)
  - [M SetTimeOptionOnlySynchronization ](#ApiClient.TsCall.SetTimeOptionOnlySynchronization)
  - [M SetTimeOptionPollingCycleMultiplier ](#ApiClient.TsCall.SetTimeOptionPollingCycleMultiplier)
  - [M SetTimeOptionTrueForAtLeast ](#ApiClient.TsCall.SetTimeOptionTrueForAtLeast)
  - [M SetTimeOptionTrueForAtLeastWithin ](#ApiClient.TsCall.SetTimeOptionTrueForAtLeastWithin)
  - [M SetTimeOptionWaitUntilTrue ](#ApiClient.TsCall.SetTimeOptionWaitUntilTrue)
  - [M SetTranslatedCommentText ](#ApiClient.TsCall.SetTranslatedCommentText)
  - [M UpdateInterface ](#ApiClient.TsCall.UpdateInterface)

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

TsCall

- [C TsCall ](#ApiClient.TsCall)
  - [M AddParameter ](#ApiClient.TsCall.AddParameter)
  - [M AddReturnValue ](#ApiClient.TsCall.AddReturnValue)
  - [M AddTag ](#ApiClient.TsCall.AddTag)
  - [M Clone ](#ApiClient.TsCall.Clone)
  - [M DeactivateReturnValueExpectation ](#ApiClient.TsCall.DeactivateReturnValueExpectation)
  - [M DeactivateReturnValueSaveIn ](#ApiClient.TsCall.DeactivateReturnValueSaveIn)
  - [M DeactivateTimeOption ](#ApiClient.TsCall.DeactivateTimeOption)
  - [M DeleteParameter ](#ApiClient.TsCall.DeleteParameter)
  - [M DeleteReturnValue ](#ApiClient.TsCall.DeleteReturnValue)
  - [M DeleteTranslatedCommentText ](#ApiClient.TsCall.DeleteTranslatedCommentText)
  - [M GetActionColumnText ](#ApiClient.TsCall.GetActionColumnText)
  - [M GetActiveTimeOptionType ](#ApiClient.TsCall.GetActiveTimeOptionType)
  - [M GetComment ](#ApiClient.TsCall.GetComment)
  - [M GetCommentColumnText ](#ApiClient.TsCall.GetCommentColumnText)
  - [M GetCycleTimeExpression ](#ApiClient.TsCall.GetCycleTimeExpression)
  - [M GetCyclicState ](#ApiClient.TsCall.GetCyclicState)
  - [M GetError ](#ApiClient.TsCall.GetError)
  - [M GetIgnoreResponse ](#ApiClient.TsCall.GetIgnoreResponse)
  - [M GetIndex ](#ApiClient.TsCall.GetIndex)
  - [M GetLineNo ](#ApiClient.TsCall.GetLineNo)
  - [M GetMappingItemReferenceName ](#ApiClient.TsCall.GetMappingItemReferenceName)
  - [M GetMinimumDuration ](#ApiClient.TsCall.GetMinimumDuration)
  - [M GetMinimumDurationUnit ](#ApiClient.TsCall.GetMinimumDurationUnit)
  - [M GetPacketExpectation ](#ApiClient.TsCall.GetPacketExpectation)
  - [M GetParameterColumnText ](#ApiClient.TsCall.GetParameterColumnText)
  - [M GetParameterNames ](#ApiClient.TsCall.GetParameterNames)
  - [M GetParameterRepresentation ](#ApiClient.TsCall.GetParameterRepresentation)
  - [M GetParameterUnit ](#ApiClient.TsCall.GetParameterUnit)
  - [M GetParameterValue ](#ApiClient.TsCall.GetParameterValue)
  - [M GetParent ](#ApiClient.TsCall.GetParent)
  - [M GetPollingCycle ](#ApiClient.TsCall.GetPollingCycle)
  - [M GetPollingCycleUnit ](#ApiClient.TsCall.GetPollingCycleUnit)
  - [M GetReturnNames ](#ApiClient.TsCall.GetReturnNames)
  - [M GetReturnValueExpectation ](#ApiClient.TsCall.GetReturnValueExpectation)
  - [M GetReturnValueRepresentation ](#ApiClient.TsCall.GetReturnValueRepresentation)
  - [M GetReturnValueSaveIn ](#ApiClient.TsCall.GetReturnValueSaveIn)
  - [M GetReturnValueUnit ](#ApiClient.TsCall.GetReturnValueUnit)
  - [M GetTags ](#ApiClient.TsCall.GetTags)
  - [M GetTestManagementId ](#ApiClient.TsCall.GetTestManagementId)
  - [M GetTestStepId ](#ApiClient.TsCall.GetTestStepId)
  - [M GetTimeout ](#ApiClient.TsCall.GetTimeout)
  - [M GetTimeoutUnit ](#ApiClient.TsCall.GetTimeoutUnit)
  - [M GetTranslatedCommentText ](#ApiClient.TsCall.GetTranslatedCommentText)
  - [M GetType ](#ApiClient.TsCall.GetType)
  - [M GetValueColumnText ](#ApiClient.TsCall.GetValueColumnText)
  - [M IsBreakpoint ](#ApiClient.TsCall.IsBreakpoint)
  - [M IsContainer ](#ApiClient.TsCall.IsContainer)
  - [M IsEnabled ](#ApiClient.TsCall.IsEnabled)
  - [M IsInPostcondition ](#ApiClient.TsCall.IsInPostcondition)
  - [M IsInPrecondition ](#ApiClient.TsCall.IsInPrecondition)
  - [M IsOk ](#ApiClient.TsCall.IsOk)
  - [M IsVisible ](#ApiClient.TsCall.IsVisible)
  - [M RemovePacketExpectation ](#ApiClient.TsCall.RemovePacketExpectation)
  - [M RemoveTag ](#ApiClient.TsCall.RemoveTag)
  - [M SetBreakpoint ](#ApiClient.TsCall.SetBreakpoint)
  - [M SetComment ](#ApiClient.TsCall.SetComment)
  - [M SetCyclic ](#ApiClient.TsCall.SetCyclic)
  - [M SetEnabled ](#ApiClient.TsCall.SetEnabled)
  - [M SetIgnoreResponse ](#ApiClient.TsCall.SetIgnoreResponse)
  - [M SetPacketExpectation ](#ApiClient.TsCall.SetPacketExpectation)
  - [M SetParameterRepresentation ](#ApiClient.TsCall.SetParameterRepresentation)
  - [M SetParameterUnit ](#ApiClient.TsCall.SetParameterUnit)
  - [M SetParameterValue ](#ApiClient.TsCall.SetParameterValue)
  - [M SetReturnValueExpectation ](#ApiClient.TsCall.SetReturnValueExpectation)
  - [M SetReturnValueRepresentation ](#ApiClient.TsCall.SetReturnValueRepresentation)
  - [M SetReturnValueSaveIn ](#ApiClient.TsCall.SetReturnValueSaveIn)
  - [M SetReturnValueUnit ](#ApiClient.TsCall.SetReturnValueUnit)
  - [M SetTags ](#ApiClient.TsCall.SetTags)
  - [M SetTestManagementId ](#ApiClient.TsCall.SetTestManagementId)
  - [M SetTimeOptionOnlySynchronization ](#ApiClient.TsCall.SetTimeOptionOnlySynchronization)
  - [M SetTimeOptionPollingCycleMultiplier ](#ApiClient.TsCall.SetTimeOptionPollingCycleMultiplier)
  - [M SetTimeOptionTrueForAtLeast ](#ApiClient.TsCall.SetTimeOptionTrueForAtLeast)
  - [M SetTimeOptionTrueForAtLeastWithin ](#ApiClient.TsCall.SetTimeOptionTrueForAtLeastWithin)
  - [M SetTimeOptionWaitUntilTrue ](#ApiClient.TsCall.SetTimeOptionWaitUntilTrue)
  - [M SetTranslatedCommentText ](#ApiClient.TsCall.SetTranslatedCommentText)
  - [M UpdateInterface ](#ApiClient.TsCall.UpdateInterface)

# TsCall[¶](#tscall "Link to this heading")

*class* TsCall[¶](#ApiClient.TsCall "Link to this definition")  
Returned by

- [`TestStepApi.CreateTsCall`](../TestStepApi.md#ApiClient.TestStepApi.CreateTsCall "ApiClient.TestStepApi.CreateTsCall (Python method) — Creates a call test step.")

AddParameter(*[parameterName](#ApiClient.TsCall.AddParameter.parameterName "ApiClient.TsCall.AddParameter.parameterName (Python parameter) — name of the parameter")*, *[valueExpression](#ApiClient.TsCall.AddParameter.valueExpression "ApiClient.TsCall.AddParameter.valueExpression (Python parameter) — expression to use for the parameter's value")=`None`*, *[repr](#ApiClient.TsCall.AddParameter.repr "ApiClient.TsCall.AddParameter.repr (Python parameter) — Representation.")=`'PHYS'`*, *[unit](#ApiClient.TsCall.AddParameter.unit "ApiClient.TsCall.AddParameter.unit (Python parameter) — Unit of the parameter")=`"don't care"`*)[¶](#ApiClient.TsCall.AddParameter "Link to this definition")  
Adds a parameter to the test step.

See also [`UpdateInterface()`](#ApiClient.TsCall.UpdateInterface "ApiClient.TsCall.UpdateInterface (Python method) — Updates the list of parameters and return values according to the assigned mapping target:") and the various `SetParameter...` methods.

Parameters:  parameterName : str[¶](#ApiClient.TsCall.AddParameter.parameterName "Permalink to this definition")  
name of the parameter

valueExpression : str[¶](#ApiClient.TsCall.AddParameter.valueExpression "Permalink to this definition")  
expression to use for the parameter’s value

repr : str[¶](#ApiClient.TsCall.AddParameter.repr "Permalink to this definition")  
Representation. One of `~ApiClient.PHYS`, `~ApiClient.RAW`, `~ApiClient.TEXT` or `~ApiClient.BITS`

unit : str[¶](#ApiClient.TsCall.AddParameter.unit "Permalink to this definition")  
Unit of the parameter

AddReturnValue(*[returnName](#ApiClient.TsCall.AddReturnValue.returnName "ApiClient.TsCall.AddReturnValue.returnName (Python parameter) — name of the return value")*, *[saveIn](#ApiClient.TsCall.AddReturnValue.saveIn "ApiClient.TsCall.AddReturnValue.saveIn (Python parameter) — name of the variable to save the return value into")=`None`*, *[expectation](#ApiClient.TsCall.AddReturnValue.expectation "ApiClient.TsCall.AddReturnValue.expectation (Python parameter) — Expectation for the return value")=`None`*, *[repr](#ApiClient.TsCall.AddReturnValue.repr "ApiClient.TsCall.AddReturnValue.repr (Python parameter) — Representation.")=`'PHYS'`*, *[unit](#ApiClient.TsCall.AddReturnValue.unit "ApiClient.TsCall.AddReturnValue.unit (Python parameter) — Unit of the return value")=`"don't care"`*)[¶](#ApiClient.TsCall.AddReturnValue "Link to this definition")  
Adds a return value to the test step.

See also [`UpdateInterface()`](#ApiClient.TsCall.UpdateInterface "ApiClient.TsCall.UpdateInterface (Python method) — Updates the list of parameters and return values according to the assigned mapping target:") and the various `SetReturnValue...` methods.

Parameters:  returnName : str[¶](#ApiClient.TsCall.AddReturnValue.returnName "Permalink to this definition")  
name of the return value

saveIn : str[¶](#ApiClient.TsCall.AddReturnValue.saveIn "Permalink to this definition")  
name of the variable to save the return value into

expectation=`None`[¶](#ApiClient.TsCall.AddReturnValue.expectation "Permalink to this definition")  
Expectation for the return value

repr : str[¶](#ApiClient.TsCall.AddReturnValue.repr "Permalink to this definition")  
Representation. One of `~ApiClient.PHYS`, `~ApiClient.RAW`, `~ApiClient.TEXT` or `~ApiClient.BITS`

unit : str[¶](#ApiClient.TsCall.AddReturnValue.unit "Permalink to this definition")  
Unit of the return value

AddTag(*[tag](#ApiClient.TsCall.AddTag.tag "ApiClient.TsCall.AddTag.tag (Python parameter) — The tag to be set")*)[¶](#ApiClient.TsCall.AddTag "Link to this definition")  
Add a specific tag to this step.

Parameters:  tag : str[¶](#ApiClient.TsCall.AddTag.tag "Permalink to this definition")  
The tag to be set

Clone()[¶](#ApiClient.TsCall.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`TsCall`](#ApiClient.TsCall "ApiClient.TsCall (Python class) — TestStepApi.CreateTsCall")

DeactivateReturnValueExpectation(*[returnName](#ApiClient.TsCall.DeactivateReturnValueExpectation.returnName "ApiClient.TsCall.DeactivateReturnValueExpectation.returnName (Python parameter) — name of the return value")*)[¶](#ApiClient.TsCall.DeactivateReturnValueExpectation "Link to this definition")  
Deactivates the expectation for the specified return value.

If no return value with an expectation remains, also deactivates any time option that may be configured.

Parameters:  returnName : str[¶](#ApiClient.TsCall.DeactivateReturnValueExpectation.returnName "Permalink to this definition")  
name of the return value

DeactivateReturnValueSaveIn(*[returnName](#ApiClient.TsCall.DeactivateReturnValueSaveIn.returnName "ApiClient.TsCall.DeactivateReturnValueSaveIn.returnName (Python parameter) — name of the return value")*)[¶](#ApiClient.TsCall.DeactivateReturnValueSaveIn "Link to this definition")  
Deactivates the save into a variable mechanism for the specified return value

Parameters:  returnName : str[¶](#ApiClient.TsCall.DeactivateReturnValueSaveIn.returnName "Permalink to this definition")  
name of the return value

DeactivateTimeOption()[¶](#ApiClient.TsCall.DeactivateTimeOption "Link to this definition")  
Deactivates any time option set on the test step. This is equivalent to selecting the option “none” in the test step’s time options menu.

DeleteParameter(*[parameterName](#ApiClient.TsCall.DeleteParameter.parameterName "ApiClient.TsCall.DeleteParameter.parameterName (Python parameter) — name of the parameter")*)[¶](#ApiClient.TsCall.DeleteParameter "Link to this definition")  
Removes a parameter from the test step.

See also [`UpdateInterface()`](#ApiClient.TsCall.UpdateInterface "ApiClient.TsCall.UpdateInterface (Python method) — Updates the list of parameters and return values according to the assigned mapping target:").

Parameters:  parameterName : str[¶](#ApiClient.TsCall.DeleteParameter.parameterName "Permalink to this definition")  
name of the parameter

DeleteReturnValue(*[returnName](#ApiClient.TsCall.DeleteReturnValue.returnName "ApiClient.TsCall.DeleteReturnValue.returnName (Python parameter) — name of the return value")*)[¶](#ApiClient.TsCall.DeleteReturnValue "Link to this definition")  
Removes a return value from the test step. If no return values are left after the deletion, also deactivates any time option that may be configured.

See also [`UpdateInterface()`](#ApiClient.TsCall.UpdateInterface "ApiClient.TsCall.UpdateInterface (Python method) — Updates the list of parameters and return values according to the assigned mapping target:").

Parameters:  returnName : str[¶](#ApiClient.TsCall.DeleteReturnValue.returnName "Permalink to this definition")  
name of the return value

DeleteTranslatedCommentText(*[language](#ApiClient.TsCall.DeleteTranslatedCommentText.language "ApiClient.TsCall.DeleteTranslatedCommentText.language (Python parameter) — Language of the text ('en_US', 'de_DE', 'zh_CN')")*)[¶](#ApiClient.TsCall.DeleteTranslatedCommentText "Link to this definition")  
Deletes a comment for the test step in the given language.

Parameters:  language : str[¶](#ApiClient.TsCall.DeleteTranslatedCommentText.language "Permalink to this definition")  
Language of the text (‘en_US’, ‘de_DE’, ‘zh_CN’)

GetActionColumnText()[¶](#ApiClient.TsCall.GetActionColumnText "Link to this definition")  
Returns the text value of the “action” column.

Returns:  Action column text

Return type:  str

GetActiveTimeOptionType()[¶](#ApiClient.TsCall.GetActiveTimeOptionType "Link to this definition")  
Returns the type of the currently active time option.

Returns:  Type of active time option (“Timeless”, “Finally”, “TrueForWithin”, “Generally”, “SyncOnly”, “PollingCycleMultiplier”)

Return type:  string

GetComment()[¶](#ApiClient.TsCall.GetComment "Link to this definition")  
Returns the comment of the test step in the current test case language.

Returns:  Comment text as shown in the comment tab

Return type:  str

GetCommentColumnText()[¶](#ApiClient.TsCall.GetCommentColumnText "Link to this definition")  
Returns the text value of the “comment” column.

Returns:  Comment column text

Return type:  str

GetCycleTimeExpression()[¶](#ApiClient.TsCall.GetCycleTimeExpression "Link to this definition")  
Gets the cycle time expression for this test step.

Returns:  cycle time expression in milliseconds

Return type:  str

GetCyclicState()[¶](#ApiClient.TsCall.GetCyclicState "Link to this definition")  
Gets the cyclic sending state for this test step.

Returns:  ‘on’, ‘off’, ‘unchanged’ or None

Return type:  str

GetError()[¶](#ApiClient.TsCall.GetError "Link to this definition")  
Returns a list of errors. Note that the error messages depend on the program language ecu.test is set to. Because of that we do not recommend to check against exact error messages, unless you are certain about the respective program language.

Returns:  List of errors

Return type:  list[str]

GetIgnoreResponse()[¶](#ApiClient.TsCall.GetIgnoreResponse "Link to this definition")  
Returns test step’s option for ignoring its response.

Raises:  
**ApiError** – If not return values or ignoring the response is not supported the option does not make sense.

Returns:  Returns the value of the option.

Return type:  bool

GetIndex()[¶](#ApiClient.TsCall.GetIndex "Link to this definition")  
Returns the zero based index in the parent.

Returns:  Zero based index

Return type:  integer

GetLineNo()[¶](#ApiClient.TsCall.GetLineNo "Link to this definition")  
Returns the test steps line number within its test case.

Returns:  Line number

Return type:  int

GetMappingItemReferenceName()[¶](#ApiClient.TsCall.GetMappingItemReferenceName "Link to this definition")  
Returns the unique reference name of the mapping item used by this test step.

Returns:  Reference name of used mapping item

Return type:  str

GetMinimumDuration()[¶](#ApiClient.TsCall.GetMinimumDuration "Link to this definition")  
Returns the minimum duration of the test step’s time option, if a corresponding option has been set.

Returns:  The minimum duration, else None

Return type:  string

GetMinimumDurationUnit()[¶](#ApiClient.TsCall.GetMinimumDurationUnit "Link to this definition")  
Returns the unit of the minimum duration of the test step’s time option, if a corresponding option has been set.

Returns:  The unit of the minimum duration, else None

Return type:  string

GetPacketExpectation()[¶](#ApiClient.TsCall.GetPacketExpectation "Link to this definition")  
Returns the expectation for the packet

Returns:  expectation

Return type:  [`Expectation`](../ExpectationApi/Expectation.md#ApiClient.Expectation "ApiClient.Expectation (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")

GetParameterColumnText()[¶](#ApiClient.TsCall.GetParameterColumnText "Link to this definition")  
Returns the text value of the “parameter” column.

Returns:  Parameter column text

Return type:  str

GetParameterNames()[¶](#ApiClient.TsCall.GetParameterNames "Link to this definition")  
Returns the names of the parameters defined in the test step.

Info

If the test step was created without a mapping item, or if the data base describing the target of the mapping item was not loaded, this list is initially empty. You can use [`AddParameter()`](#ApiClient.TsCall.AddParameter "ApiClient.TsCall.AddParameter (Python method) — Adds a parameter to the test step.") or [`UpdateInterface()`](#ApiClient.TsCall.UpdateInterface "ApiClient.TsCall.UpdateInterface (Python method) — Updates the list of parameters and return values according to the assigned mapping target:") to populate it.

Returns:  Parameter names

Return type:  list[str]

GetParameterRepresentation(*[parameterName](#ApiClient.TsCall.GetParameterRepresentation.parameterName "ApiClient.TsCall.GetParameterRepresentation.parameterName (Python parameter) — name of the parameter")*)[¶](#ApiClient.TsCall.GetParameterRepresentation "Link to this definition")  
Returns the representation used for the specified parameter

Parameters:  parameterName : str[¶](#ApiClient.TsCall.GetParameterRepresentation.parameterName "Permalink to this definition")  
name of the parameter

Returns:  representation used for the parameter

Return type:  str

GetParameterUnit(*[parameterName](#ApiClient.TsCall.GetParameterUnit.parameterName "ApiClient.TsCall.GetParameterUnit.parameterName (Python parameter) — name of the parameter")*)[¶](#ApiClient.TsCall.GetParameterUnit "Link to this definition")  
Returns the unit for the specified parameter

Parameters:  parameterName : str[¶](#ApiClient.TsCall.GetParameterUnit.parameterName "Permalink to this definition")  
name of the parameter

Returns:  Unit used by the `~ApiClient.PHYS` representation for this parameter

Return type:  str

GetParameterValue(*[parameterName](#ApiClient.TsCall.GetParameterValue.parameterName "ApiClient.TsCall.GetParameterValue.parameterName (Python parameter) — name of the parameter")*)[¶](#ApiClient.TsCall.GetParameterValue "Link to this definition")  
Returns the value expression assigned to the specified parameter

Parameters:  parameterName : str[¶](#ApiClient.TsCall.GetParameterValue.parameterName "Permalink to this definition")  
name of the parameter

Returns:  value expression assigned to the parameter

Return type:  str

GetParent()[¶](#ApiClient.TsCall.GetParent "Link to this definition")  
Returns the parent test step.

Returns:  The parent test step or None if it is a top level test step.

Return type:  [`TestStep`](../PackageApi/TestStep.md#ApiClient.TestStep "ApiClient.TestStep (Python class) — Add a specific tag to this step.")

GetPollingCycle()[¶](#ApiClient.TsCall.GetPollingCycle "Link to this definition")  
Returns the polling cycle of the test step’s time option, if a corresponding option has been set.

Returns:  The polling cycle, else None

Return type:  string

GetPollingCycleUnit()[¶](#ApiClient.TsCall.GetPollingCycleUnit "Link to this definition")  
Returns the unit of the polling cycle of the test step’s time option, if a corresponding option has been set.

Returns:  The unit of the polling cycle, else None

Return type:  string

GetReturnNames()[¶](#ApiClient.TsCall.GetReturnNames "Link to this definition")  
Returns the names of the return values defined in the test step.

Info

If the test step was created without a mapping item, or if the data base describing the target of the mapping item was not loaded, this list is initially empty. You can use [`AddReturnValue()`](#ApiClient.TsCall.AddReturnValue "ApiClient.TsCall.AddReturnValue (Python method) — Adds a return value to the test step.") or [`UpdateInterface()`](#ApiClient.TsCall.UpdateInterface "ApiClient.TsCall.UpdateInterface (Python method) — Updates the list of parameters and return values according to the assigned mapping target:") to populate it.

Returns:  Return value names

Return type:  list[str]

GetReturnValueExpectation(*[returnName](#ApiClient.TsCall.GetReturnValueExpectation.returnName "ApiClient.TsCall.GetReturnValueExpectation.returnName (Python parameter) — name of the return value")*)[¶](#ApiClient.TsCall.GetReturnValueExpectation "Link to this definition")  
Returns the expectation for the specified return value

Parameters:  returnName : str[¶](#ApiClient.TsCall.GetReturnValueExpectation.returnName "Permalink to this definition")  
name of the return value

Returns:  expectation

Return type:  [`Expectation`](../ExpectationApi/Expectation.md#ApiClient.Expectation "ApiClient.Expectation (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")

GetReturnValueRepresentation(*[returnName](#ApiClient.TsCall.GetReturnValueRepresentation.returnName "ApiClient.TsCall.GetReturnValueRepresentation.returnName (Python parameter) — name of the return value")*)[¶](#ApiClient.TsCall.GetReturnValueRepresentation "Link to this definition")  
Returns the representation used for the specified return value

Parameters:  returnName : str[¶](#ApiClient.TsCall.GetReturnValueRepresentation.returnName "Permalink to this definition")  
name of the return value

Returns:  representation used for the return value

Return type:  str

GetReturnValueSaveIn(*[returnName](#ApiClient.TsCall.GetReturnValueSaveIn.returnName "ApiClient.TsCall.GetReturnValueSaveIn.returnName (Python parameter) — name of the return value")*)[¶](#ApiClient.TsCall.GetReturnValueSaveIn "Link to this definition")  
Returns the variable name to save the specified return value in

Parameters:  returnName : str[¶](#ApiClient.TsCall.GetReturnValueSaveIn.returnName "Permalink to this definition")  
name of the return value

Returns:  variable name

Return type:  str

GetReturnValueUnit(*[returnName](#ApiClient.TsCall.GetReturnValueUnit.returnName "ApiClient.TsCall.GetReturnValueUnit.returnName (Python parameter) — name of the return value")*)[¶](#ApiClient.TsCall.GetReturnValueUnit "Link to this definition")  
Returns the unit for the specified return value

Parameters:  returnName : str[¶](#ApiClient.TsCall.GetReturnValueUnit.returnName "Permalink to this definition")  
name of the return value

Returns:  Unit used by the `~ApiClient.PHYS` representation for this return value

Return type:  str

GetTags()[¶](#ApiClient.TsCall.GetTags "Link to this definition")  
Returns the tags set for this step.

Returns:  A (sorted) list of tags

Return type:  list[str]

GetTestManagementId()[¶](#ApiClient.TsCall.GetTestManagementId "Link to this definition")  
Returns the test management id of the test step.

Returns:  Test step id.

Return type:  str

GetTestStepId()[¶](#ApiClient.TsCall.GetTestStepId "Link to this definition")  
Returns the test step id.

Returns:  test step id

Return type:  str

GetTimeout()[¶](#ApiClient.TsCall.GetTimeout "Link to this definition")  
Returns the timeout of the test step’s time option, if a corresponding option has been set.

Returns:  The timeout else None

Return type:  string

GetTimeoutUnit()[¶](#ApiClient.TsCall.GetTimeoutUnit "Link to this definition")  
Returns the unit of the timeout of the test step’s time option, if a corresponding option has been set.

Returns:  The unit of the timeout else None

Return type:  string

GetTranslatedCommentText(*[language](#ApiClient.TsCall.GetTranslatedCommentText.language "ApiClient.TsCall.GetTranslatedCommentText.language (Python parameter) — Language of the requested text ('en_US', 'de_DE', 'zh_CN')")*)[¶](#ApiClient.TsCall.GetTranslatedCommentText "Link to this definition")  
Returns the text value of the “comment” column in the given language.

Parameters:  language : str[¶](#ApiClient.TsCall.GetTranslatedCommentText.language "Permalink to this definition")  
Language of the requested text (‘en_US’, ‘de_DE’, ‘zh_CN’)

Returns:  Comment column text

Return type:  str

GetType()[¶](#ApiClient.TsCall.GetType "Link to this definition")  
Returns the type (class name) of the test step, e.g.

- “TsPreconditionBlock”

- “TsWait”

- “TsIfThenElse”

- “TsSwitchCase”

- “TsCaseNode”

Returns:  Type (class name) of the test step

Return type:  str

GetValueColumnText()[¶](#ApiClient.TsCall.GetValueColumnText "Link to this definition")  
Returns the text value of the “value” column in your current test case language.

Returns:  Value column text

Return type:  str

IsBreakpoint()[¶](#ApiClient.TsCall.IsBreakpoint "Link to this definition")  
Checks whether the test step is a break point.

Returns:  True if test step is a break point, else False

Return type:  boolean

IsContainer()[¶](#ApiClient.TsCall.IsContainer "Link to this definition")  
Checks whether this test step can contain test steps

Returns:  True if it can contain test steps, else False

Return type:  boolean

IsEnabled()[¶](#ApiClient.TsCall.IsEnabled "Link to this definition")  
Returns the state of the test step.

Returns:  True if test step is enabled, otherwise False

Return type:  bool

IsInPostcondition()[¶](#ApiClient.TsCall.IsInPostcondition "Link to this definition")  
Returns True if the test step is located in a postcondition

Returns:  True if the test step is located in a postcondition, else Flase

Return type:  bool

IsInPrecondition()[¶](#ApiClient.TsCall.IsInPrecondition "Link to this definition")  
Returns True if the test step is located in a precondition

Returns:  True if the test step is located in a precondition, else False

Return type:  bool

IsOk()[¶](#ApiClient.TsCall.IsOk "Link to this definition")  
Returns the internal state of correctness of the test step.

Returns:  True if no problems were found, else False

Return type:  boolean

IsVisible()[¶](#ApiClient.TsCall.IsVisible "Link to this definition")  
Checks whether the test step is visible. This depends on the test step itself or a parent test step being disabled.

Returns:  True if test step is visible, else False

Return type:  boolean

RemovePacketExpectation()[¶](#ApiClient.TsCall.RemovePacketExpectation "Link to this definition")  
Removes the expectation for the packet. Only applicable if this test step is mapped to a service method/event.

RemoveTag(*[tag](#ApiClient.TsCall.RemoveTag.tag "ApiClient.TsCall.RemoveTag.tag (Python parameter) — The tag to be removed")*)[¶](#ApiClient.TsCall.RemoveTag "Link to this definition")  
Remove a specific tag from this step.

Parameters:  tag : str[¶](#ApiClient.TsCall.RemoveTag.tag "Permalink to this definition")  
The tag to be removed

SetBreakpoint(*[enable](#ApiClient.TsCall.SetBreakpoint.enable "ApiClient.TsCall.SetBreakpoint.enable (Python parameter) — True if test step is a break point, else False")*)[¶](#ApiClient.TsCall.SetBreakpoint "Link to this definition")  
Sets or unsets the test step to act as a break point.

Parameters:  enable : boolean[¶](#ApiClient.TsCall.SetBreakpoint.enable "Permalink to this definition")  
True if test step is a break point, else False

SetComment(*[comment](#ApiClient.TsCall.SetComment.comment "ApiClient.TsCall.SetComment.comment (Python parameter) — Text to be displayed in the comment tab")*)[¶](#ApiClient.TsCall.SetComment "Link to this definition")  
Sets a comment for the test step in the current test case language.

Parameters:  comment : str[¶](#ApiClient.TsCall.SetComment.comment "Permalink to this definition")  
Text to be displayed in the comment tab

SetCyclic(*[cyclicState](#ApiClient.TsCall.SetCyclic.cyclicState "ApiClient.TsCall.SetCyclic.cyclicState (Python parameter) — possible values are:")*, *[cycleTimeExpression](#ApiClient.TsCall.SetCyclic.cycleTimeExpression "ApiClient.TsCall.SetCyclic.cycleTimeExpression (Python parameter) — in milliseconds, necessary for cyclicState 'on'")=`None`*)[¶](#ApiClient.TsCall.SetCyclic "Link to this definition")  
Changes the send cyclic settings for a test step that has call mode ‘SEND_EVENT’

Raises:  
**ApiError** – if the test step doesn’t support cyclic sending

Parameters:  cyclicState : str[¶](#ApiClient.TsCall.SetCyclic.cyclicState "Permalink to this definition")  
possible values are:

- ’on’ enables cyclic sending using the specified cycleTimeExpression

- ’off’ disables cyclic sending

- ’unchanged’ keeps cyclic sending (e.g. if just the event’s values should be changed)

- None removes cyclic settings so the test step will send the event just once

cycleTimeExpression : str[¶](#ApiClient.TsCall.SetCyclic.cycleTimeExpression "Permalink to this definition")  
in milliseconds, necessary for cyclicState ‘on’

SetEnabled(*[state](#ApiClient.TsCall.SetEnabled.state "ApiClient.TsCall.SetEnabled.state (Python parameter) — True (Default) to enable, False to disable the test step.")=`True`*)[¶](#ApiClient.TsCall.SetEnabled "Link to this definition")  
Enable or disable the test step.

Parameters:  state : bool[¶](#ApiClient.TsCall.SetEnabled.state "Permalink to this definition")  
True (Default) to enable, False to disable the test step.

SetIgnoreResponse(*[ignoreResponse](#ApiClient.TsCall.SetIgnoreResponse.ignoreResponse "ApiClient.TsCall.SetIgnoreResponse.ignoreResponse (Python parameter) — Sets the value of the option.")*)[¶](#ApiClient.TsCall.SetIgnoreResponse "Link to this definition")  
Sets test step’s option for ignoring its response.

Raises:  
**ApiError** – If not return values or ignoring the response is not supported the option does not make sense.

Parameters:  ignoreResponse : bool[¶](#ApiClient.TsCall.SetIgnoreResponse.ignoreResponse "Permalink to this definition")  
Sets the value of the option.

SetPacketExpectation(*[expectationExpression](#ApiClient.TsCall.SetPacketExpectation.expectationExpression "ApiClient.TsCall.SetPacketExpectation.expectationExpression (Python parameter) — expectation for the return value")*)[¶](#ApiClient.TsCall.SetPacketExpectation "Link to this definition")  
Sets the expectation for the packet. Only applicable if this test step is mapped to a service method/event.

This should be a [`ExpressionExpectation`](../ExpectationApi/ExpressionExpectation.md#ApiClient.ExpressionExpectation "ApiClient.ExpressionExpectation (Python class) — ExpectationApi.CreateExpressionExpectation") referencing the packet as `value`, a [`PresentExpectation`](../ExpectationApi/PresentExpectation.md#ApiClient.PresentExpectation "ApiClient.PresentExpectation (Python class) — ExpectationApi.CreatePresentExpectation"), or a [`NotPresentExpectation`](../ExpectationApi/NotPresentExpectation.md#ApiClient.NotPresentExpectation "ApiClient.NotPresentExpectation (Python class) — ExpectationApi.CreateNotPresentExpectation").

Keep in mind that the `value` object can not only be a `PacketSomeIp` but also NotPresent.

Parameters:  expectationExpression[¶](#ApiClient.TsCall.SetPacketExpectation.expectationExpression "Permalink to this definition")  
expectation for the return value

SetParameterRepresentation(*[parameterName](#ApiClient.TsCall.SetParameterRepresentation.parameterName "ApiClient.TsCall.SetParameterRepresentation.parameterName (Python parameter) — name of the parameter")*, *[repr](#ApiClient.TsCall.SetParameterRepresentation.repr "ApiClient.TsCall.SetParameterRepresentation.repr (Python parameter) — representation to use for the parameter. One of ~ApiClient.PHYS, ~ApiClient.RAW, ~ApiClient.TEXT or ~ApiClient.BITS")*)[¶](#ApiClient.TsCall.SetParameterRepresentation "Link to this definition")  
Sets the representation for the specified parameter

This method only works with existing parameters. To add a parameter please use [`AddParameter()`](#ApiClient.TsCall.AddParameter "ApiClient.TsCall.AddParameter (Python method) — Adds a parameter to the test step.")

Parameters:  parameterName : str[¶](#ApiClient.TsCall.SetParameterRepresentation.parameterName "Permalink to this definition")  
name of the parameter

repr : str[¶](#ApiClient.TsCall.SetParameterRepresentation.repr "Permalink to this definition")  
representation to use for the parameter. One of `~ApiClient.PHYS`, `~ApiClient.RAW`, `~ApiClient.TEXT` or `~ApiClient.BITS`

SetParameterUnit(*[parameterName](#ApiClient.TsCall.SetParameterUnit.parameterName "ApiClient.TsCall.SetParameterUnit.parameterName (Python parameter) — name of the parameter")*, *[unit](#ApiClient.TsCall.SetParameterUnit.unit "ApiClient.TsCall.SetParameterUnit.unit (Python parameter) — Unit to use for the ~ApiClient.PHYS representation for this parameter")*)[¶](#ApiClient.TsCall.SetParameterUnit "Link to this definition")  
Sets the unit for the specified parameter

This method only works with existing parameters. To add a parameter please use [`AddParameter()`](#ApiClient.TsCall.AddParameter "ApiClient.TsCall.AddParameter (Python method) — Adds a parameter to the test step.")

Parameters:  parameterName : str[¶](#ApiClient.TsCall.SetParameterUnit.parameterName "Permalink to this definition")  
name of the parameter

unit : str[¶](#ApiClient.TsCall.SetParameterUnit.unit "Permalink to this definition")  
Unit to use for the `~ApiClient.PHYS` representation for this parameter

SetParameterValue(*[parameterName](#ApiClient.TsCall.SetParameterValue.parameterName "ApiClient.TsCall.SetParameterValue.parameterName (Python parameter) — name of the parameter")*, *[valueExpression](#ApiClient.TsCall.SetParameterValue.valueExpression "ApiClient.TsCall.SetParameterValue.valueExpression (Python parameter) — expression to use for the parameter's value")*)[¶](#ApiClient.TsCall.SetParameterValue "Link to this definition")  
Assigns a new expression to use the specified parameter’s value

This method only works with existing parameters. To add a parameter please use [`AddParameter()`](#ApiClient.TsCall.AddParameter "ApiClient.TsCall.AddParameter (Python method) — Adds a parameter to the test step.")

Parameters:  parameterName : str[¶](#ApiClient.TsCall.SetParameterValue.parameterName "Permalink to this definition")  
name of the parameter

valueExpression : str[¶](#ApiClient.TsCall.SetParameterValue.valueExpression "Permalink to this definition")  
expression to use for the parameter’s value

SetReturnValueExpectation(*[returnName](#ApiClient.TsCall.SetReturnValueExpectation.returnName "ApiClient.TsCall.SetReturnValueExpectation.returnName (Python parameter) — name of the return value")*, *[expectationExpression](#ApiClient.TsCall.SetReturnValueExpectation.expectationExpression "ApiClient.TsCall.SetReturnValueExpectation.expectationExpression (Python parameter) — expectation for the return value")*)[¶](#ApiClient.TsCall.SetReturnValueExpectation "Link to this definition")  
Sets the expectation for the specified return value.

This method only works with existing return values. To add a return value please use [`AddReturnValue()`](#ApiClient.TsCall.AddReturnValue "ApiClient.TsCall.AddReturnValue (Python method) — Adds a return value to the test step.")

Parameters:  returnName : str[¶](#ApiClient.TsCall.SetReturnValueExpectation.returnName "Permalink to this definition")  
name of the return value

expectationExpression[¶](#ApiClient.TsCall.SetReturnValueExpectation.expectationExpression "Permalink to this definition")  
expectation for the return value

SetReturnValueRepresentation(*[returnName](#ApiClient.TsCall.SetReturnValueRepresentation.returnName "ApiClient.TsCall.SetReturnValueRepresentation.returnName (Python parameter) — name of the return value")*, *[repr](#ApiClient.TsCall.SetReturnValueRepresentation.repr "ApiClient.TsCall.SetReturnValueRepresentation.repr (Python parameter) — representation to use for the return value. One of ~ApiClient.PHYS, ~ApiClient.RAW, ~ApiClient.TEXT or ~ApiClient.BITS")*)[¶](#ApiClient.TsCall.SetReturnValueRepresentation "Link to this definition")  
Sets the representation for the specified return value

This method only works with existing return values. To add a return value please use [`AddReturnValue()`](#ApiClient.TsCall.AddReturnValue "ApiClient.TsCall.AddReturnValue (Python method) — Adds a return value to the test step.")

Parameters:  returnName : str[¶](#ApiClient.TsCall.SetReturnValueRepresentation.returnName "Permalink to this definition")  
name of the return value

repr : str[¶](#ApiClient.TsCall.SetReturnValueRepresentation.repr "Permalink to this definition")  
representation to use for the return value. One of `~ApiClient.PHYS`, `~ApiClient.RAW`, `~ApiClient.TEXT` or `~ApiClient.BITS`

SetReturnValueSaveIn(*[returnName](#ApiClient.TsCall.SetReturnValueSaveIn.returnName "ApiClient.TsCall.SetReturnValueSaveIn.returnName (Python parameter) — name of the return value")*, *[saveInVariableName](#ApiClient.TsCall.SetReturnValueSaveIn.saveInVariableName "ApiClient.TsCall.SetReturnValueSaveIn.saveInVariableName (Python parameter) — variable name")*)[¶](#ApiClient.TsCall.SetReturnValueSaveIn "Link to this definition")  
Sets the variable name to save the specified return value in

This method only works with existing return values. To add a return value please use [`AddReturnValue()`](#ApiClient.TsCall.AddReturnValue "ApiClient.TsCall.AddReturnValue (Python method) — Adds a return value to the test step.")

Parameters:  returnName : str[¶](#ApiClient.TsCall.SetReturnValueSaveIn.returnName "Permalink to this definition")  
name of the return value

saveInVariableName : str[¶](#ApiClient.TsCall.SetReturnValueSaveIn.saveInVariableName "Permalink to this definition")  
variable name

SetReturnValueUnit(*[returnName](#ApiClient.TsCall.SetReturnValueUnit.returnName "ApiClient.TsCall.SetReturnValueUnit.returnName (Python parameter) — name of the return value")*, *[unit](#ApiClient.TsCall.SetReturnValueUnit.unit "ApiClient.TsCall.SetReturnValueUnit.unit (Python parameter) — Unit to use for the ~ApiClient.PHYS representation for this return value")*)[¶](#ApiClient.TsCall.SetReturnValueUnit "Link to this definition")  
Sets the unit for the specified return value

This method only works with existing return values. To add a return value please use [`AddReturnValue()`](#ApiClient.TsCall.AddReturnValue "ApiClient.TsCall.AddReturnValue (Python method) — Adds a return value to the test step.")

Parameters:  returnName : str[¶](#ApiClient.TsCall.SetReturnValueUnit.returnName "Permalink to this definition")  
name of the return value

unit : str[¶](#ApiClient.TsCall.SetReturnValueUnit.unit "Permalink to this definition")  
Unit to use for the `~ApiClient.PHYS` representation for this return value

SetTags(*[tags](#ApiClient.TsCall.SetTags.tags "ApiClient.TsCall.SetTags.tags (Python parameter) — The list of tags")*)[¶](#ApiClient.TsCall.SetTags "Link to this definition")  
Set the list of tags for this step. The list of tags will be sorted and stored.

Parameters:  tags : list[str][¶](#ApiClient.TsCall.SetTags.tags "Permalink to this definition")  
The list of tags

SetTestManagementId(*[testManagementId](#ApiClient.TsCall.SetTestManagementId.testManagementId "ApiClient.TsCall.SetTestManagementId.testManagementId (Python parameter) — Test management id of the test step")*)[¶](#ApiClient.TsCall.SetTestManagementId "Link to this definition")  
Sets the test management id of the test step.

Parameters:  testManagementId : str[¶](#ApiClient.TsCall.SetTestManagementId.testManagementId "Permalink to this definition")  
Test management id of the test step

SetTimeOptionOnlySynchronization(*[timeout](#ApiClient.TsCall.SetTimeOptionOnlySynchronization.timeout "ApiClient.TsCall.SetTimeOptionOnlySynchronization.timeout (Python parameter) — The timeout to be used")*, *[pollingCycle](#ApiClient.TsCall.SetTimeOptionOnlySynchronization.pollingCycle "ApiClient.TsCall.SetTimeOptionOnlySynchronization.pollingCycle (Python parameter) — Optional polling cycle to be used")=`None`*, *[timeoutUnit](#ApiClient.TsCall.SetTimeOptionOnlySynchronization.timeoutUnit "ApiClient.TsCall.SetTimeOptionOnlySynchronization.timeoutUnit (Python parameter) — Optional unit for the timeout (ms, s, min, h or d)")=`'ms'`*, *[pollingCycleUnit](#ApiClient.TsCall.SetTimeOptionOnlySynchronization.pollingCycleUnit "ApiClient.TsCall.SetTimeOptionOnlySynchronization.pollingCycleUnit (Python parameter) — Optional unit for the polling cycle (ms, s, min, h or d)")=`'ms'`*)[¶](#ApiClient.TsCall.SetTimeOptionOnlySynchronization "Link to this definition")  
Sets the test step’s time option to “only synchronization”.

Raises:  
**ApiError** – If no return value has an expectation, no time option can be set.

Parameters:  timeout : string[¶](#ApiClient.TsCall.SetTimeOptionOnlySynchronization.timeout "Permalink to this definition")  
The timeout to be used

pollingCycle : string[¶](#ApiClient.TsCall.SetTimeOptionOnlySynchronization.pollingCycle "Permalink to this definition")  
Optional polling cycle to be used

timeoutUnit : string[¶](#ApiClient.TsCall.SetTimeOptionOnlySynchronization.timeoutUnit "Permalink to this definition")  
Optional unit for the timeout (ms, s, min, h or d)

pollingCycleUnit : string[¶](#ApiClient.TsCall.SetTimeOptionOnlySynchronization.pollingCycleUnit "Permalink to this definition")  
Optional unit for the polling cycle (ms, s, min, h or d)

SetTimeOptionPollingCycleMultiplier(*[pollingCycleMultiplier](#ApiClient.TsCall.SetTimeOptionPollingCycleMultiplier.pollingCycleMultiplier "ApiClient.TsCall.SetTimeOptionPollingCycleMultiplier.pollingCycleMultiplier (Python parameter) — The polling cycle multiplier to be used.")*)[¶](#ApiClient.TsCall.SetTimeOptionPollingCycleMultiplier "Link to this definition")  
Sets the test step’s time option to “polling cycle multiplier”. This option must only be used when inserting the test step into a Multi-Check!

Parameters:  pollingCycleMultiplier : string[¶](#ApiClient.TsCall.SetTimeOptionPollingCycleMultiplier.pollingCycleMultiplier "Permalink to this definition")  
The polling cycle multiplier to be used.

SetTimeOptionTrueForAtLeast(*[minimumDuration](#ApiClient.TsCall.SetTimeOptionTrueForAtLeast.minimumDuration "ApiClient.TsCall.SetTimeOptionTrueForAtLeast.minimumDuration (Python parameter) — The minimum duration to be used")*, *[pollingCycle](#ApiClient.TsCall.SetTimeOptionTrueForAtLeast.pollingCycle "ApiClient.TsCall.SetTimeOptionTrueForAtLeast.pollingCycle (Python parameter) — Optional polling cycle to be used")=`None`*, *[timeoutUnit](#ApiClient.TsCall.SetTimeOptionTrueForAtLeast.timeoutUnit "ApiClient.TsCall.SetTimeOptionTrueForAtLeast.timeoutUnit (Python parameter) — Optional unit for the timeout (ms, s, min, h or d)")=`'ms'`*, *[pollingCycleUnit](#ApiClient.TsCall.SetTimeOptionTrueForAtLeast.pollingCycleUnit "ApiClient.TsCall.SetTimeOptionTrueForAtLeast.pollingCycleUnit (Python parameter) — Optional unit for the polling cycle (ms, s, min, h or d)")=`'ms'`*)[¶](#ApiClient.TsCall.SetTimeOptionTrueForAtLeast "Link to this definition")  
Sets the test step’s time option to “true for at least”.

Raises:  
**ApiError** – If no return value has an expectation, no time option can be set.

Parameters:  minimumDuration : string[¶](#ApiClient.TsCall.SetTimeOptionTrueForAtLeast.minimumDuration "Permalink to this definition")  
The minimum duration to be used

pollingCycle : string[¶](#ApiClient.TsCall.SetTimeOptionTrueForAtLeast.pollingCycle "Permalink to this definition")  
Optional polling cycle to be used

timeoutUnit : string[¶](#ApiClient.TsCall.SetTimeOptionTrueForAtLeast.timeoutUnit "Permalink to this definition")  
Optional unit for the timeout (ms, s, min, h or d)

pollingCycleUnit : string[¶](#ApiClient.TsCall.SetTimeOptionTrueForAtLeast.pollingCycleUnit "Permalink to this definition")  
Optional unit for the polling cycle (ms, s, min, h or d)

SetTimeOptionTrueForAtLeastWithin(*[minimumDuration](#ApiClient.TsCall.SetTimeOptionTrueForAtLeastWithin.minimumDuration "ApiClient.TsCall.SetTimeOptionTrueForAtLeastWithin.minimumDuration (Python parameter) — The minimum duration to be used")*, *[timeout](#ApiClient.TsCall.SetTimeOptionTrueForAtLeastWithin.timeout "ApiClient.TsCall.SetTimeOptionTrueForAtLeastWithin.timeout (Python parameter) — The timeout to be used")*, *[pollingCycle](#ApiClient.TsCall.SetTimeOptionTrueForAtLeastWithin.pollingCycle "ApiClient.TsCall.SetTimeOptionTrueForAtLeastWithin.pollingCycle (Python parameter) — Optional polling cycle to be used")=`None`*, *[timeoutUnit](#ApiClient.TsCall.SetTimeOptionTrueForAtLeastWithin.timeoutUnit "ApiClient.TsCall.SetTimeOptionTrueForAtLeastWithin.timeoutUnit (Python parameter) — Optional unit for the timeout (ms, s, min, h or d)")=`'ms'`*, *[pollingCycleUnit](#ApiClient.TsCall.SetTimeOptionTrueForAtLeastWithin.pollingCycleUnit "ApiClient.TsCall.SetTimeOptionTrueForAtLeastWithin.pollingCycleUnit (Python parameter) — Optional unit for the polling cycle (ms, s, min, h or d)")=`'ms'`*)[¶](#ApiClient.TsCall.SetTimeOptionTrueForAtLeastWithin "Link to this definition")  
Sets the test step’s time option to “true for at least … within …”.

Raises:  
**ApiError** – If no return value has an expectation, no time option can be set.

Parameters:  minimumDuration : string[¶](#ApiClient.TsCall.SetTimeOptionTrueForAtLeastWithin.minimumDuration "Permalink to this definition")  
The minimum duration to be used

timeout : string[¶](#ApiClient.TsCall.SetTimeOptionTrueForAtLeastWithin.timeout "Permalink to this definition")  
The timeout to be used

pollingCycle : string[¶](#ApiClient.TsCall.SetTimeOptionTrueForAtLeastWithin.pollingCycle "Permalink to this definition")  
Optional polling cycle to be used

timeoutUnit : string[¶](#ApiClient.TsCall.SetTimeOptionTrueForAtLeastWithin.timeoutUnit "Permalink to this definition")  
Optional unit for the timeout (ms, s, min, h or d)

pollingCycleUnit : string[¶](#ApiClient.TsCall.SetTimeOptionTrueForAtLeastWithin.pollingCycleUnit "Permalink to this definition")  
Optional unit for the polling cycle (ms, s, min, h or d)

SetTimeOptionWaitUntilTrue(*[timeout](#ApiClient.TsCall.SetTimeOptionWaitUntilTrue.timeout "ApiClient.TsCall.SetTimeOptionWaitUntilTrue.timeout (Python parameter) — The timeout to be used")*, *[pollingCycle](#ApiClient.TsCall.SetTimeOptionWaitUntilTrue.pollingCycle "ApiClient.TsCall.SetTimeOptionWaitUntilTrue.pollingCycle (Python parameter) — Optional polling cycle to be used")=`None`*, *[timeoutUnit](#ApiClient.TsCall.SetTimeOptionWaitUntilTrue.timeoutUnit "ApiClient.TsCall.SetTimeOptionWaitUntilTrue.timeoutUnit (Python parameter) — Optional unit for the timeout (ms, s, min, h or d)")=`'ms'`*, *[pollingCycleUnit](#ApiClient.TsCall.SetTimeOptionWaitUntilTrue.pollingCycleUnit "ApiClient.TsCall.SetTimeOptionWaitUntilTrue.pollingCycleUnit (Python parameter) — Optional unit for the polling cycle (ms, s, min, h or d)")=`'ms'`*)[¶](#ApiClient.TsCall.SetTimeOptionWaitUntilTrue "Link to this definition")  
Sets the test step’s time option to “wait until true”.

Raises:  
**ApiError** – If no return value has an expectation, no time option can be set.

Parameters:  timeout : string[¶](#ApiClient.TsCall.SetTimeOptionWaitUntilTrue.timeout "Permalink to this definition")  
The timeout to be used

pollingCycle : string[¶](#ApiClient.TsCall.SetTimeOptionWaitUntilTrue.pollingCycle "Permalink to this definition")  
Optional polling cycle to be used

timeoutUnit : string[¶](#ApiClient.TsCall.SetTimeOptionWaitUntilTrue.timeoutUnit "Permalink to this definition")  
Optional unit for the timeout (ms, s, min, h or d)

pollingCycleUnit : string[¶](#ApiClient.TsCall.SetTimeOptionWaitUntilTrue.pollingCycleUnit "Permalink to this definition")  
Optional unit for the polling cycle (ms, s, min, h or d)

SetTranslatedCommentText(*[comment](#ApiClient.TsCall.SetTranslatedCommentText.comment "ApiClient.TsCall.SetTranslatedCommentText.comment (Python parameter) — Text to be displayed")*, *[language](#ApiClient.TsCall.SetTranslatedCommentText.language "ApiClient.TsCall.SetTranslatedCommentText.language (Python parameter) — Language of the text ('en_US', 'de_DE', 'zh_CN')")*)[¶](#ApiClient.TsCall.SetTranslatedCommentText "Link to this definition")  
Sets a comment for the test step in the given language.

Parameters:  comment : str[¶](#ApiClient.TsCall.SetTranslatedCommentText.comment "Permalink to this definition")  
Text to be displayed

language : str[¶](#ApiClient.TsCall.SetTranslatedCommentText.language "Permalink to this definition")  
Language of the text (‘en_US’, ‘de_DE’, ‘zh_CN’)

UpdateInterface()[¶](#ApiClient.TsCall.UpdateInterface "Link to this definition")  
Updates the list of parameters and return values according to the assigned mapping target:

- Removes any parameters and return values not available in the assigned mapping target

- Adds any missing parameters and return values defined in the assigned mapping target. Parameters are assigned a default value. Return values are not assigned any expectation.

Parameters and return values existing in both the test step and the mapping target are left as they are, which might in some cases result in an incompatible representation or unit.

Info

This only works if the test step is associated with an appropriate mappingItem (via a package, via a global mapping, or via the `~ApiClient.mappingItem` parameter of the [`CreateTsCall()`](../TestStepApi.md#ApiClient.TestStepApi.CreateTsCall "ApiClient.TestStepApi.CreateTsCall (Python method) — Creates a call test step.") method) and the database describing the target of the mapping item is loaded.

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
