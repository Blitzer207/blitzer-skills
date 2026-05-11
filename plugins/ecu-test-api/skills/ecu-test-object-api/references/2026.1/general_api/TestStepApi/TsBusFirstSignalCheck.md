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

TsBusFirstSignalCheck [ TsBusFirstSignalCheck ](#)

TsBusFirstSignalCheck

- [C TsBusFirstSignalCheck ](#ApiClient.TsBusFirstSignalCheck)
  - [M AddTag ](#ApiClient.TsBusFirstSignalCheck.AddTag)
  - [M Clone ](#ApiClient.TsBusFirstSignalCheck.Clone)
  - [M DeactivateExpectation ](#ApiClient.TsBusFirstSignalCheck.DeactivateExpectation)
  - [M DeactivateFailedComment ](#ApiClient.TsBusFirstSignalCheck.DeactivateFailedComment)
  - [M DeactivateSaveIn ](#ApiClient.TsBusFirstSignalCheck.DeactivateSaveIn)
  - [M DeactivateSuccessComment ](#ApiClient.TsBusFirstSignalCheck.DeactivateSuccessComment)
  - [M DeactivateTimeOption ](#ApiClient.TsBusFirstSignalCheck.DeactivateTimeOption)
  - [M DeleteTranslatedCommentText ](#ApiClient.TsBusFirstSignalCheck.DeleteTranslatedCommentText)
  - [M GetActionColumnText ](#ApiClient.TsBusFirstSignalCheck.GetActionColumnText)
  - [M GetActiveTimeOptionType ](#ApiClient.TsBusFirstSignalCheck.GetActiveTimeOptionType)
  - [M GetComment ](#ApiClient.TsBusFirstSignalCheck.GetComment)
  - [M GetCommentColumnText ](#ApiClient.TsBusFirstSignalCheck.GetCommentColumnText)
  - [M GetError ](#ApiClient.TsBusFirstSignalCheck.GetError)
  - [M GetExpectation ](#ApiClient.TsBusFirstSignalCheck.GetExpectation)
  - [M GetExpectationExpression ](#ApiClient.TsBusFirstSignalCheck.GetExpectationExpression)
  - [M GetFailedComment ](#ApiClient.TsBusFirstSignalCheck.GetFailedComment)
  - [M GetIndex ](#ApiClient.TsBusFirstSignalCheck.GetIndex)
  - [M GetLineNo ](#ApiClient.TsBusFirstSignalCheck.GetLineNo)
  - [M GetMappingItemReferenceName ](#ApiClient.TsBusFirstSignalCheck.GetMappingItemReferenceName)
  - [M GetMinimumDuration ](#ApiClient.TsBusFirstSignalCheck.GetMinimumDuration)
  - [M GetMinimumDurationUnit ](#ApiClient.TsBusFirstSignalCheck.GetMinimumDurationUnit)
  - [M GetParameterColumnText ](#ApiClient.TsBusFirstSignalCheck.GetParameterColumnText)
  - [M GetParent ](#ApiClient.TsBusFirstSignalCheck.GetParent)
  - [M GetPollingCycle ](#ApiClient.TsBusFirstSignalCheck.GetPollingCycle)
  - [M GetPollingCycleUnit ](#ApiClient.TsBusFirstSignalCheck.GetPollingCycleUnit)
  - [M GetRepresentation ](#ApiClient.TsBusFirstSignalCheck.GetRepresentation)
  - [M GetSaveInVariableName ](#ApiClient.TsBusFirstSignalCheck.GetSaveInVariableName)
  - [M GetSuccessComment ](#ApiClient.TsBusFirstSignalCheck.GetSuccessComment)
  - [M GetTags ](#ApiClient.TsBusFirstSignalCheck.GetTags)
  - [M GetTestManagementId ](#ApiClient.TsBusFirstSignalCheck.GetTestManagementId)
  - [M GetTestStepId ](#ApiClient.TsBusFirstSignalCheck.GetTestStepId)
  - [M GetTimeout ](#ApiClient.TsBusFirstSignalCheck.GetTimeout)
  - [M GetTimeoutUnit ](#ApiClient.TsBusFirstSignalCheck.GetTimeoutUnit)
  - [M GetTranslatedCommentText ](#ApiClient.TsBusFirstSignalCheck.GetTranslatedCommentText)
  - [M GetType ](#ApiClient.TsBusFirstSignalCheck.GetType)
  - [M GetUnit ](#ApiClient.TsBusFirstSignalCheck.GetUnit)
  - [M GetValueColumnText ](#ApiClient.TsBusFirstSignalCheck.GetValueColumnText)
  - [M IsBreakpoint ](#ApiClient.TsBusFirstSignalCheck.IsBreakpoint)
  - [M IsContainer ](#ApiClient.TsBusFirstSignalCheck.IsContainer)
  - [M IsEnabled ](#ApiClient.TsBusFirstSignalCheck.IsEnabled)
  - [M IsInPostcondition ](#ApiClient.TsBusFirstSignalCheck.IsInPostcondition)
  - [M IsInPrecondition ](#ApiClient.TsBusFirstSignalCheck.IsInPrecondition)
  - [M IsOk ](#ApiClient.TsBusFirstSignalCheck.IsOk)
  - [M IsVisible ](#ApiClient.TsBusFirstSignalCheck.IsVisible)
  - [M RemoveTag ](#ApiClient.TsBusFirstSignalCheck.RemoveTag)
  - [M SetBreakpoint ](#ApiClient.TsBusFirstSignalCheck.SetBreakpoint)
  - [M SetComment ](#ApiClient.TsBusFirstSignalCheck.SetComment)
  - [M SetEnabled ](#ApiClient.TsBusFirstSignalCheck.SetEnabled)
  - [M SetExpectation ](#ApiClient.TsBusFirstSignalCheck.SetExpectation)
  - [M SetExpectationExpression ](#ApiClient.TsBusFirstSignalCheck.SetExpectationExpression)
  - [M SetFailedComment ](#ApiClient.TsBusFirstSignalCheck.SetFailedComment)
  - [M SetRepresentation ](#ApiClient.TsBusFirstSignalCheck.SetRepresentation)
  - [M SetSaveInVariableName ](#ApiClient.TsBusFirstSignalCheck.SetSaveInVariableName)
  - [M SetSuccessComment ](#ApiClient.TsBusFirstSignalCheck.SetSuccessComment)
  - [M SetTags ](#ApiClient.TsBusFirstSignalCheck.SetTags)
  - [M SetTestManagementId ](#ApiClient.TsBusFirstSignalCheck.SetTestManagementId)
  - [M SetTimeOptionOnlySynchronization ](#ApiClient.TsBusFirstSignalCheck.SetTimeOptionOnlySynchronization)
  - [M SetTimeOptionPollingCycleMultiplier ](#ApiClient.TsBusFirstSignalCheck.SetTimeOptionPollingCycleMultiplier)
  - [M SetTimeOptionTrueForAtLeast ](#ApiClient.TsBusFirstSignalCheck.SetTimeOptionTrueForAtLeast)
  - [M SetTimeOptionTrueForAtLeastWithin ](#ApiClient.TsBusFirstSignalCheck.SetTimeOptionTrueForAtLeastWithin)
  - [M SetTimeOptionWaitUntilTrue ](#ApiClient.TsBusFirstSignalCheck.SetTimeOptionWaitUntilTrue)
  - [M SetTranslatedCommentText ](#ApiClient.TsBusFirstSignalCheck.SetTranslatedCommentText)
  - [M SetUnit ](#ApiClient.TsBusFirstSignalCheck.SetUnit)

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

TsBusFirstSignalCheck

- [C TsBusFirstSignalCheck ](#ApiClient.TsBusFirstSignalCheck)
  - [M AddTag ](#ApiClient.TsBusFirstSignalCheck.AddTag)
  - [M Clone ](#ApiClient.TsBusFirstSignalCheck.Clone)
  - [M DeactivateExpectation ](#ApiClient.TsBusFirstSignalCheck.DeactivateExpectation)
  - [M DeactivateFailedComment ](#ApiClient.TsBusFirstSignalCheck.DeactivateFailedComment)
  - [M DeactivateSaveIn ](#ApiClient.TsBusFirstSignalCheck.DeactivateSaveIn)
  - [M DeactivateSuccessComment ](#ApiClient.TsBusFirstSignalCheck.DeactivateSuccessComment)
  - [M DeactivateTimeOption ](#ApiClient.TsBusFirstSignalCheck.DeactivateTimeOption)
  - [M DeleteTranslatedCommentText ](#ApiClient.TsBusFirstSignalCheck.DeleteTranslatedCommentText)
  - [M GetActionColumnText ](#ApiClient.TsBusFirstSignalCheck.GetActionColumnText)
  - [M GetActiveTimeOptionType ](#ApiClient.TsBusFirstSignalCheck.GetActiveTimeOptionType)
  - [M GetComment ](#ApiClient.TsBusFirstSignalCheck.GetComment)
  - [M GetCommentColumnText ](#ApiClient.TsBusFirstSignalCheck.GetCommentColumnText)
  - [M GetError ](#ApiClient.TsBusFirstSignalCheck.GetError)
  - [M GetExpectation ](#ApiClient.TsBusFirstSignalCheck.GetExpectation)
  - [M GetExpectationExpression ](#ApiClient.TsBusFirstSignalCheck.GetExpectationExpression)
  - [M GetFailedComment ](#ApiClient.TsBusFirstSignalCheck.GetFailedComment)
  - [M GetIndex ](#ApiClient.TsBusFirstSignalCheck.GetIndex)
  - [M GetLineNo ](#ApiClient.TsBusFirstSignalCheck.GetLineNo)
  - [M GetMappingItemReferenceName ](#ApiClient.TsBusFirstSignalCheck.GetMappingItemReferenceName)
  - [M GetMinimumDuration ](#ApiClient.TsBusFirstSignalCheck.GetMinimumDuration)
  - [M GetMinimumDurationUnit ](#ApiClient.TsBusFirstSignalCheck.GetMinimumDurationUnit)
  - [M GetParameterColumnText ](#ApiClient.TsBusFirstSignalCheck.GetParameterColumnText)
  - [M GetParent ](#ApiClient.TsBusFirstSignalCheck.GetParent)
  - [M GetPollingCycle ](#ApiClient.TsBusFirstSignalCheck.GetPollingCycle)
  - [M GetPollingCycleUnit ](#ApiClient.TsBusFirstSignalCheck.GetPollingCycleUnit)
  - [M GetRepresentation ](#ApiClient.TsBusFirstSignalCheck.GetRepresentation)
  - [M GetSaveInVariableName ](#ApiClient.TsBusFirstSignalCheck.GetSaveInVariableName)
  - [M GetSuccessComment ](#ApiClient.TsBusFirstSignalCheck.GetSuccessComment)
  - [M GetTags ](#ApiClient.TsBusFirstSignalCheck.GetTags)
  - [M GetTestManagementId ](#ApiClient.TsBusFirstSignalCheck.GetTestManagementId)
  - [M GetTestStepId ](#ApiClient.TsBusFirstSignalCheck.GetTestStepId)
  - [M GetTimeout ](#ApiClient.TsBusFirstSignalCheck.GetTimeout)
  - [M GetTimeoutUnit ](#ApiClient.TsBusFirstSignalCheck.GetTimeoutUnit)
  - [M GetTranslatedCommentText ](#ApiClient.TsBusFirstSignalCheck.GetTranslatedCommentText)
  - [M GetType ](#ApiClient.TsBusFirstSignalCheck.GetType)
  - [M GetUnit ](#ApiClient.TsBusFirstSignalCheck.GetUnit)
  - [M GetValueColumnText ](#ApiClient.TsBusFirstSignalCheck.GetValueColumnText)
  - [M IsBreakpoint ](#ApiClient.TsBusFirstSignalCheck.IsBreakpoint)
  - [M IsContainer ](#ApiClient.TsBusFirstSignalCheck.IsContainer)
  - [M IsEnabled ](#ApiClient.TsBusFirstSignalCheck.IsEnabled)
  - [M IsInPostcondition ](#ApiClient.TsBusFirstSignalCheck.IsInPostcondition)
  - [M IsInPrecondition ](#ApiClient.TsBusFirstSignalCheck.IsInPrecondition)
  - [M IsOk ](#ApiClient.TsBusFirstSignalCheck.IsOk)
  - [M IsVisible ](#ApiClient.TsBusFirstSignalCheck.IsVisible)
  - [M RemoveTag ](#ApiClient.TsBusFirstSignalCheck.RemoveTag)
  - [M SetBreakpoint ](#ApiClient.TsBusFirstSignalCheck.SetBreakpoint)
  - [M SetComment ](#ApiClient.TsBusFirstSignalCheck.SetComment)
  - [M SetEnabled ](#ApiClient.TsBusFirstSignalCheck.SetEnabled)
  - [M SetExpectation ](#ApiClient.TsBusFirstSignalCheck.SetExpectation)
  - [M SetExpectationExpression ](#ApiClient.TsBusFirstSignalCheck.SetExpectationExpression)
  - [M SetFailedComment ](#ApiClient.TsBusFirstSignalCheck.SetFailedComment)
  - [M SetRepresentation ](#ApiClient.TsBusFirstSignalCheck.SetRepresentation)
  - [M SetSaveInVariableName ](#ApiClient.TsBusFirstSignalCheck.SetSaveInVariableName)
  - [M SetSuccessComment ](#ApiClient.TsBusFirstSignalCheck.SetSuccessComment)
  - [M SetTags ](#ApiClient.TsBusFirstSignalCheck.SetTags)
  - [M SetTestManagementId ](#ApiClient.TsBusFirstSignalCheck.SetTestManagementId)
  - [M SetTimeOptionOnlySynchronization ](#ApiClient.TsBusFirstSignalCheck.SetTimeOptionOnlySynchronization)
  - [M SetTimeOptionPollingCycleMultiplier ](#ApiClient.TsBusFirstSignalCheck.SetTimeOptionPollingCycleMultiplier)
  - [M SetTimeOptionTrueForAtLeast ](#ApiClient.TsBusFirstSignalCheck.SetTimeOptionTrueForAtLeast)
  - [M SetTimeOptionTrueForAtLeastWithin ](#ApiClient.TsBusFirstSignalCheck.SetTimeOptionTrueForAtLeastWithin)
  - [M SetTimeOptionWaitUntilTrue ](#ApiClient.TsBusFirstSignalCheck.SetTimeOptionWaitUntilTrue)
  - [M SetTranslatedCommentText ](#ApiClient.TsBusFirstSignalCheck.SetTranslatedCommentText)
  - [M SetUnit ](#ApiClient.TsBusFirstSignalCheck.SetUnit)

# TsBusFirstSignalCheck[¶](#tsbusfirstsignalcheck "Link to this heading")

*class* TsBusFirstSignalCheck[¶](#ApiClient.TsBusFirstSignalCheck "Link to this definition")  
Returned by

- [`TestStepApi.CreateTsBusFirstSignalCheck`](../TestStepApi.md#ApiClient.TestStepApi.CreateTsBusFirstSignalCheck "ApiClient.TestStepApi.CreateTsBusFirstSignalCheck (Python method) — Creates a new check initial value test step")

AddTag(*[tag](#ApiClient.TsBusFirstSignalCheck.AddTag.tag "ApiClient.TsBusFirstSignalCheck.AddTag.tag (Python parameter) — The tag to be set")*)[¶](#ApiClient.TsBusFirstSignalCheck.AddTag "Link to this definition")  
Add a specific tag to this step.

Parameters:  tag : str[¶](#ApiClient.TsBusFirstSignalCheck.AddTag.tag "Permalink to this definition")  
The tag to be set

Clone()[¶](#ApiClient.TsBusFirstSignalCheck.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`TsBusFirstSignalCheck`](#ApiClient.TsBusFirstSignalCheck "ApiClient.TsBusFirstSignalCheck (Python class) — TestStepApi.CreateTsBusFirstSignalCheck")

DeactivateExpectation()[¶](#ApiClient.TsBusFirstSignalCheck.DeactivateExpectation "Link to this definition")  
Deactivates the expectation so that the result will not be evaluated.

DeactivateFailedComment()[¶](#ApiClient.TsBusFirstSignalCheck.DeactivateFailedComment "Link to this definition")  
Deactivates the expectation for the failed comment so that the result will not be evaluated.

DeactivateSaveIn()[¶](#ApiClient.TsBusFirstSignalCheck.DeactivateSaveIn "Link to this definition")  
Deactivates the test step’s save in property, so the value will not be stored in a package variable.

DeactivateSuccessComment()[¶](#ApiClient.TsBusFirstSignalCheck.DeactivateSuccessComment "Link to this definition")  
Deactivates the expectation for the success comment so that the result will not be evaluated.

DeactivateTimeOption()[¶](#ApiClient.TsBusFirstSignalCheck.DeactivateTimeOption "Link to this definition")  
Deactivates any time option set on the test step. This is equivalent to selecting the option “none” in the test step’s time options menu.

DeleteTranslatedCommentText(*[language](#ApiClient.TsBusFirstSignalCheck.DeleteTranslatedCommentText.language "ApiClient.TsBusFirstSignalCheck.DeleteTranslatedCommentText.language (Python parameter) — Language of the text ('en_US', 'de_DE', 'zh_CN')")*)[¶](#ApiClient.TsBusFirstSignalCheck.DeleteTranslatedCommentText "Link to this definition")  
Deletes a comment for the test step in the given language.

Parameters:  language : str[¶](#ApiClient.TsBusFirstSignalCheck.DeleteTranslatedCommentText.language "Permalink to this definition")  
Language of the text (‘en_US’, ‘de_DE’, ‘zh_CN’)

GetActionColumnText()[¶](#ApiClient.TsBusFirstSignalCheck.GetActionColumnText "Link to this definition")  
Returns the text value of the “action” column.

Returns:  Action column text

Return type:  str

GetActiveTimeOptionType()[¶](#ApiClient.TsBusFirstSignalCheck.GetActiveTimeOptionType "Link to this definition")  
Returns the type of the currently active time option.

Returns:  Type of active time option (“Timeless”, “Finally”, “TrueForWithin”, “Generally”, “SyncOnly”, “PollingCycleMultiplier”)

Return type:  string

GetComment()[¶](#ApiClient.TsBusFirstSignalCheck.GetComment "Link to this definition")  
Returns the comment of the test step in the current test case language.

Returns:  Comment text as shown in the comment tab

Return type:  str

GetCommentColumnText()[¶](#ApiClient.TsBusFirstSignalCheck.GetCommentColumnText "Link to this definition")  
Returns the text value of the “comment” column.

Returns:  Comment column text

Return type:  str

GetError()[¶](#ApiClient.TsBusFirstSignalCheck.GetError "Link to this definition")  
Returns a list of errors. Note that the error messages depend on the program language ecu.test is set to. Because of that we do not recommend to check against exact error messages, unless you are certain about the respective program language.

Returns:  List of errors

Return type:  list[str]

GetExpectation()[¶](#ApiClient.TsBusFirstSignalCheck.GetExpectation "Link to this definition")  
Returns the expectation expression from the evaluation of the test step, or None, if no expectation was defined.

Returns:  The expectation

Return type:  [`Expectation`](../ExpectationApi/Expectation.md#ApiClient.Expectation "ApiClient.Expectation (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")

GetExpectationExpression()[¶](#ApiClient.TsBusFirstSignalCheck.GetExpectationExpression "Link to this definition")  
Returns the expectation expression from the evaluation of the test step, or None, if no expectation was defined.

Returns:  The expectation

Return type:  string

GetFailedComment()[¶](#ApiClient.TsBusFirstSignalCheck.GetFailedComment "Link to this definition")  
Returns the failed comment of the step.

Returns:  The failed comment

Return type:  string

GetIndex()[¶](#ApiClient.TsBusFirstSignalCheck.GetIndex "Link to this definition")  
Returns the zero based index in the parent.

Returns:  Zero based index

Return type:  integer

GetLineNo()[¶](#ApiClient.TsBusFirstSignalCheck.GetLineNo "Link to this definition")  
Returns the test steps line number within its test case.

Returns:  Line number

Return type:  int

GetMappingItemReferenceName()[¶](#ApiClient.TsBusFirstSignalCheck.GetMappingItemReferenceName "Link to this definition")  
Returns the unique reference name of the mapping item used by this test step.

Returns:  Reference name of used mapping item

Return type:  str

GetMinimumDuration()[¶](#ApiClient.TsBusFirstSignalCheck.GetMinimumDuration "Link to this definition")  
Returns the minimum duration of the test step’s time option, if a corresponding option has been set.

Returns:  The minimum duration, else None

Return type:  string

GetMinimumDurationUnit()[¶](#ApiClient.TsBusFirstSignalCheck.GetMinimumDurationUnit "Link to this definition")  
Returns the unit of the minimum duration of the test step’s time option, if a corresponding option has been set.

Returns:  The unit of the minimum duration, else None

Return type:  string

GetParameterColumnText()[¶](#ApiClient.TsBusFirstSignalCheck.GetParameterColumnText "Link to this definition")  
Returns the text value of the “parameter” column.

Returns:  Parameter column text

Return type:  str

GetParent()[¶](#ApiClient.TsBusFirstSignalCheck.GetParent "Link to this definition")  
Returns the parent test step.

Returns:  The parent test step or None if it is a top level test step.

Return type:  [`TestStep`](../PackageApi/TestStep.md#ApiClient.TestStep "ApiClient.TestStep (Python class) — Add a specific tag to this step.")

GetPollingCycle()[¶](#ApiClient.TsBusFirstSignalCheck.GetPollingCycle "Link to this definition")  
Returns the polling cycle of the test step’s time option, if a corresponding option has been set.

Returns:  The polling cycle, else None

Return type:  string

GetPollingCycleUnit()[¶](#ApiClient.TsBusFirstSignalCheck.GetPollingCycleUnit "Link to this definition")  
Returns the unit of the polling cycle of the test step’s time option, if a corresponding option has been set.

Returns:  The unit of the polling cycle, else None

Return type:  string

GetRepresentation(*[axis](#ApiClient.TsBusFirstSignalCheck.GetRepresentation.axis "ApiClient.TsBusFirstSignalCheck.GetRepresentation.axis (Python parameter) — Axis to set representation for (x, y, z)")=`'z'`*)[¶](#ApiClient.TsBusFirstSignalCheck.GetRepresentation "Link to this definition")  
Returns the representation of a certain axis of the accessed test quantity.

Parameters:  axis : str[¶](#ApiClient.TsBusFirstSignalCheck.GetRepresentation.axis "Permalink to this definition")  
Axis to set representation for (x, y, z)

Returns:  Representation for axis (PHYS, TEXT, RAW, BITS)

Return type:  str

GetSaveInVariableName()[¶](#ApiClient.TsBusFirstSignalCheck.GetSaveInVariableName "Link to this definition")  
Returns the currently selected variable to save the data.

Returns:  The variable’s name

Return type:  string

GetSuccessComment()[¶](#ApiClient.TsBusFirstSignalCheck.GetSuccessComment "Link to this definition")  
Returns the success comment of the step.

Returns:  The success comment

Return type:  string

GetTags()[¶](#ApiClient.TsBusFirstSignalCheck.GetTags "Link to this definition")  
Returns the tags set for this step.

Returns:  A (sorted) list of tags

Return type:  list[str]

GetTestManagementId()[¶](#ApiClient.TsBusFirstSignalCheck.GetTestManagementId "Link to this definition")  
Returns the test management id of the test step.

Returns:  Test step id.

Return type:  str

GetTestStepId()[¶](#ApiClient.TsBusFirstSignalCheck.GetTestStepId "Link to this definition")  
Returns the test step id.

Returns:  test step id

Return type:  str

GetTimeout()[¶](#ApiClient.TsBusFirstSignalCheck.GetTimeout "Link to this definition")  
Returns the timeout of the test step’s time option, if a corresponding option has been set.

Returns:  The timeout else None

Return type:  string

GetTimeoutUnit()[¶](#ApiClient.TsBusFirstSignalCheck.GetTimeoutUnit "Link to this definition")  
Returns the unit of the timeout of the test step’s time option, if a corresponding option has been set.

Returns:  The unit of the timeout else None

Return type:  string

GetTranslatedCommentText(*[language](#ApiClient.TsBusFirstSignalCheck.GetTranslatedCommentText.language "ApiClient.TsBusFirstSignalCheck.GetTranslatedCommentText.language (Python parameter) — Language of the requested text ('en_US', 'de_DE', 'zh_CN')")*)[¶](#ApiClient.TsBusFirstSignalCheck.GetTranslatedCommentText "Link to this definition")  
Returns the text value of the “comment” column in the given language.

Parameters:  language : str[¶](#ApiClient.TsBusFirstSignalCheck.GetTranslatedCommentText.language "Permalink to this definition")  
Language of the requested text (‘en_US’, ‘de_DE’, ‘zh_CN’)

Returns:  Comment column text

Return type:  str

GetType()[¶](#ApiClient.TsBusFirstSignalCheck.GetType "Link to this definition")  
Returns the type (class name) of the test step, e.g.

- “TsPreconditionBlock”

- “TsWait”

- “TsIfThenElse”

- “TsSwitchCase”

- “TsCaseNode”

Returns:  Type (class name) of the test step

Return type:  str

GetUnit(*[axis](#ApiClient.TsBusFirstSignalCheck.GetUnit.axis "ApiClient.TsBusFirstSignalCheck.GetUnit.axis (Python parameter) — Axis to set unit for (x, y, z)")=`'z'`*)[¶](#ApiClient.TsBusFirstSignalCheck.GetUnit "Link to this definition")  
Returns the unit of a certain axis of the accessed test quantity.

Parameters:  axis : str[¶](#ApiClient.TsBusFirstSignalCheck.GetUnit.axis "Permalink to this definition")  
Axis to set unit for (x, y, z)

Returns:  Unit for axis

Return type:  str

GetValueColumnText()[¶](#ApiClient.TsBusFirstSignalCheck.GetValueColumnText "Link to this definition")  
Returns the text value of the “value” column in your current test case language.

Returns:  Value column text

Return type:  str

IsBreakpoint()[¶](#ApiClient.TsBusFirstSignalCheck.IsBreakpoint "Link to this definition")  
Checks whether the test step is a break point.

Returns:  True if test step is a break point, else False

Return type:  boolean

IsContainer()[¶](#ApiClient.TsBusFirstSignalCheck.IsContainer "Link to this definition")  
Returns True, if the test step supports calling GetChildren as well as manipulating the structure of its children. (e. g. via inserting or deleting sub test steps).

Returns:  True if it can contain test steps, else False

Return type:  boolean

IsEnabled()[¶](#ApiClient.TsBusFirstSignalCheck.IsEnabled "Link to this definition")  
Returns the state of the test step.

Returns:  True if test step is enabled, otherwise False

Return type:  bool

IsInPostcondition()[¶](#ApiClient.TsBusFirstSignalCheck.IsInPostcondition "Link to this definition")  
Returns True if the test step is located in a postcondition

Returns:  True if the test step is located in a postcondition, else Flase

Return type:  bool

IsInPrecondition()[¶](#ApiClient.TsBusFirstSignalCheck.IsInPrecondition "Link to this definition")  
Returns True if the test step is located in a precondition

Returns:  True if the test step is located in a precondition, else False

Return type:  bool

IsOk()[¶](#ApiClient.TsBusFirstSignalCheck.IsOk "Link to this definition")  
Returns the internal state of correctness of the test step.

Returns:  True if no problems were found, else False

Return type:  boolean

IsVisible()[¶](#ApiClient.TsBusFirstSignalCheck.IsVisible "Link to this definition")  
Checks whether the test step is visible. This depends on the test step itself or a parent test step being disabled.

Returns:  True if test step is visible, else False

Return type:  boolean

RemoveTag(*[tag](#ApiClient.TsBusFirstSignalCheck.RemoveTag.tag "ApiClient.TsBusFirstSignalCheck.RemoveTag.tag (Python parameter) — The tag to be removed")*)[¶](#ApiClient.TsBusFirstSignalCheck.RemoveTag "Link to this definition")  
Remove a specific tag from this step.

Parameters:  tag : str[¶](#ApiClient.TsBusFirstSignalCheck.RemoveTag.tag "Permalink to this definition")  
The tag to be removed

SetBreakpoint(*[enable](#ApiClient.TsBusFirstSignalCheck.SetBreakpoint.enable "ApiClient.TsBusFirstSignalCheck.SetBreakpoint.enable (Python parameter) — True if test step is a break point, else False")*)[¶](#ApiClient.TsBusFirstSignalCheck.SetBreakpoint "Link to this definition")  
Sets or unsets the test step to act as a break point.

Parameters:  enable : boolean[¶](#ApiClient.TsBusFirstSignalCheck.SetBreakpoint.enable "Permalink to this definition")  
True if test step is a break point, else False

SetComment(*[comment](#ApiClient.TsBusFirstSignalCheck.SetComment.comment "ApiClient.TsBusFirstSignalCheck.SetComment.comment (Python parameter) — Text to be displayed in the comment tab")*)[¶](#ApiClient.TsBusFirstSignalCheck.SetComment "Link to this definition")  
Sets a comment for the test step in the current test case language.

Parameters:  comment : str[¶](#ApiClient.TsBusFirstSignalCheck.SetComment.comment "Permalink to this definition")  
Text to be displayed in the comment tab

SetEnabled(*[state](#ApiClient.TsBusFirstSignalCheck.SetEnabled.state "ApiClient.TsBusFirstSignalCheck.SetEnabled.state (Python parameter) — True (Default) to enable, False to disable the test step.")=`True`*)[¶](#ApiClient.TsBusFirstSignalCheck.SetEnabled "Link to this definition")  
Enable or disable the test step.

Parameters:  state : bool[¶](#ApiClient.TsBusFirstSignalCheck.SetEnabled.state "Permalink to this definition")  
True (Default) to enable, False to disable the test step.

SetExpectation(*[expectation](#ApiClient.TsBusFirstSignalCheck.SetExpectation.expectation "ApiClient.TsBusFirstSignalCheck.SetExpectation.expectation (Python parameter) — The expectation")*)[¶](#ApiClient.TsBusFirstSignalCheck.SetExpectation "Link to this definition")  
Sets the expectation in the evaluation of the test step. The expectation will be activated if it was not enabled previously.

Parameters:  expectation[¶](#ApiClient.TsBusFirstSignalCheck.SetExpectation.expectation "Permalink to this definition")  
The expectation

SetExpectationExpression(*[expectation](#ApiClient.TsBusFirstSignalCheck.SetExpectationExpression.expectation "ApiClient.TsBusFirstSignalCheck.SetExpectationExpression.expectation (Python parameter) — The expectation")*)[¶](#ApiClient.TsBusFirstSignalCheck.SetExpectationExpression "Link to this definition")  
Shortcut to set an expectation for an unspecific type in the evaluation of the test step. The expectation will be activated if it was not enabled previously.

Parameters:  expectation : string[¶](#ApiClient.TsBusFirstSignalCheck.SetExpectationExpression.expectation "Permalink to this definition")  
The expectation

SetFailedComment(*[failedComment](#ApiClient.TsBusFirstSignalCheck.SetFailedComment.failedComment "ApiClient.TsBusFirstSignalCheck.SetFailedComment.failedComment (Python parameter) — The expression for the failed comment")*)[¶](#ApiClient.TsBusFirstSignalCheck.SetFailedComment "Link to this definition")  
Sets the expression for the failed comment of the step. The expression will be activated if it was not enabled previously.

Parameters:  failedComment : string[¶](#ApiClient.TsBusFirstSignalCheck.SetFailedComment.failedComment "Permalink to this definition")  
The expression for the failed comment

SetRepresentation(*[representation](#ApiClient.TsBusFirstSignalCheck.SetRepresentation.representation "ApiClient.TsBusFirstSignalCheck.SetRepresentation.representation (Python parameter) — Representation for axis (PHYS, TEXT, RAW, BITS)")=`'PHYS'`*, *[axis](#ApiClient.TsBusFirstSignalCheck.SetRepresentation.axis "ApiClient.TsBusFirstSignalCheck.SetRepresentation.axis (Python parameter) — Axis to set representation for (x, y, z)")=`'z'`*)[¶](#ApiClient.TsBusFirstSignalCheck.SetRepresentation "Link to this definition")  
Sets the representation of a certain axis of the accessed test quantity.

Parameters:  representation : str[¶](#ApiClient.TsBusFirstSignalCheck.SetRepresentation.representation "Permalink to this definition")  
Representation for axis (PHYS, TEXT, RAW, BITS)

axis : str[¶](#ApiClient.TsBusFirstSignalCheck.SetRepresentation.axis "Permalink to this definition")  
Axis to set representation for (x, y, z)

SetSaveInVariableName(*[variableName](#ApiClient.TsBusFirstSignalCheck.SetSaveInVariableName.variableName "ApiClient.TsBusFirstSignalCheck.SetSaveInVariableName.variableName (Python parameter) — The variable's name.")*)[¶](#ApiClient.TsBusFirstSignalCheck.SetSaveInVariableName "Link to this definition")  
Sets the name of the variable used for storing data by the test step. The variable will be created automatically if it does not already exist in the package where the test step is placed in. This method must not be called, if the test step has not been added to a package previously.

Parameters:  variableName : string[¶](#ApiClient.TsBusFirstSignalCheck.SetSaveInVariableName.variableName "Permalink to this definition")  
The variable’s name. Must not be None or an empty string.

Raises:  
**ApiError** –

- If SaveIn was called before the test step was added to a package.

- If variableName is None or an empty string

SetSuccessComment(*[successComment](#ApiClient.TsBusFirstSignalCheck.SetSuccessComment.successComment "ApiClient.TsBusFirstSignalCheck.SetSuccessComment.successComment (Python parameter) — The expression for the success comment")*)[¶](#ApiClient.TsBusFirstSignalCheck.SetSuccessComment "Link to this definition")  
Sets the expression for the success comment of the step. The expression will be activated if it was not enabled previously.

Parameters:  successComment : string[¶](#ApiClient.TsBusFirstSignalCheck.SetSuccessComment.successComment "Permalink to this definition")  
The expression for the success comment

SetTags(*[tags](#ApiClient.TsBusFirstSignalCheck.SetTags.tags "ApiClient.TsBusFirstSignalCheck.SetTags.tags (Python parameter) — The list of tags")*)[¶](#ApiClient.TsBusFirstSignalCheck.SetTags "Link to this definition")  
Set the list of tags for this step. The list of tags will be sorted and stored.

Parameters:  tags : list[str][¶](#ApiClient.TsBusFirstSignalCheck.SetTags.tags "Permalink to this definition")  
The list of tags

SetTestManagementId(*[testManagementId](#ApiClient.TsBusFirstSignalCheck.SetTestManagementId.testManagementId "ApiClient.TsBusFirstSignalCheck.SetTestManagementId.testManagementId (Python parameter) — Test management id of the test step")*)[¶](#ApiClient.TsBusFirstSignalCheck.SetTestManagementId "Link to this definition")  
Sets the test management id of the test step.

Parameters:  testManagementId : str[¶](#ApiClient.TsBusFirstSignalCheck.SetTestManagementId.testManagementId "Permalink to this definition")  
Test management id of the test step

SetTimeOptionOnlySynchronization(*[timeout](#ApiClient.TsBusFirstSignalCheck.SetTimeOptionOnlySynchronization.timeout "ApiClient.TsBusFirstSignalCheck.SetTimeOptionOnlySynchronization.timeout (Python parameter) — The timeout in ms to be used")*, *[pollingCycle](#ApiClient.TsBusFirstSignalCheck.SetTimeOptionOnlySynchronization.pollingCycle "ApiClient.TsBusFirstSignalCheck.SetTimeOptionOnlySynchronization.pollingCycle (Python parameter) — The polling cycle in ms or s or min or h or d.")=`None`*, *[timeoutUnit](#ApiClient.TsBusFirstSignalCheck.SetTimeOptionOnlySynchronization.timeoutUnit "ApiClient.TsBusFirstSignalCheck.SetTimeOptionOnlySynchronization.timeoutUnit (Python parameter) — Optional unit of the timeout (ms, s, min, h or d)")=`'ms'`*, *[pollingCycleUnit](#ApiClient.TsBusFirstSignalCheck.SetTimeOptionOnlySynchronization.pollingCycleUnit "ApiClient.TsBusFirstSignalCheck.SetTimeOptionOnlySynchronization.pollingCycleUnit (Python parameter) — Optional unit of the polling cycle (ms, s, min, h, or d)")=`'ms'`*)[¶](#ApiClient.TsBusFirstSignalCheck.SetTimeOptionOnlySynchronization "Link to this definition")  
Sets the test step’s time option to “only synchronization”.

Parameters:  timeout : string[¶](#ApiClient.TsBusFirstSignalCheck.SetTimeOptionOnlySynchronization.timeout "Permalink to this definition")  
The timeout in ms to be used

pollingCycle : string[¶](#ApiClient.TsBusFirstSignalCheck.SetTimeOptionOnlySynchronization.pollingCycle "Permalink to this definition")  
The polling cycle in ms or s or min or h or d. Might be left out.

timeoutUnit : string[¶](#ApiClient.TsBusFirstSignalCheck.SetTimeOptionOnlySynchronization.timeoutUnit "Permalink to this definition")  
Optional unit of the timeout (ms, s, min, h or d)

pollingCycleUnit : string[¶](#ApiClient.TsBusFirstSignalCheck.SetTimeOptionOnlySynchronization.pollingCycleUnit "Permalink to this definition")  
Optional unit of the polling cycle (ms, s, min, h, or d)

SetTimeOptionPollingCycleMultiplier(*[pollingCycleMultiplier](#ApiClient.TsBusFirstSignalCheck.SetTimeOptionPollingCycleMultiplier.pollingCycleMultiplier "ApiClient.TsBusFirstSignalCheck.SetTimeOptionPollingCycleMultiplier.pollingCycleMultiplier (Python parameter) — The polling cycle multiplier to be used.")*)[¶](#ApiClient.TsBusFirstSignalCheck.SetTimeOptionPollingCycleMultiplier "Link to this definition")  
Sets the test step’s time option to “polling cycle multiplier”. This option must only be used when inserting the test step into a Multi-Check!

Parameters:  pollingCycleMultiplier : string[¶](#ApiClient.TsBusFirstSignalCheck.SetTimeOptionPollingCycleMultiplier.pollingCycleMultiplier "Permalink to this definition")  
The polling cycle multiplier to be used.

SetTimeOptionTrueForAtLeast(*[minimumDuration](#ApiClient.TsBusFirstSignalCheck.SetTimeOptionTrueForAtLeast.minimumDuration "ApiClient.TsBusFirstSignalCheck.SetTimeOptionTrueForAtLeast.minimumDuration (Python parameter) — The minimum duration to be used")*, *[pollingCycle](#ApiClient.TsBusFirstSignalCheck.SetTimeOptionTrueForAtLeast.pollingCycle "ApiClient.TsBusFirstSignalCheck.SetTimeOptionTrueForAtLeast.pollingCycle (Python parameter) — Optional polling cycle to be used")=`None`*, *[timeoutUnit](#ApiClient.TsBusFirstSignalCheck.SetTimeOptionTrueForAtLeast.timeoutUnit "ApiClient.TsBusFirstSignalCheck.SetTimeOptionTrueForAtLeast.timeoutUnit (Python parameter) — Optional unit of the timeout (ms, s, min, h or d)")=`'ms'`*, *[pollingCycleUnit](#ApiClient.TsBusFirstSignalCheck.SetTimeOptionTrueForAtLeast.pollingCycleUnit "ApiClient.TsBusFirstSignalCheck.SetTimeOptionTrueForAtLeast.pollingCycleUnit (Python parameter) — Optional unit of the polling cycle (ms, s, min, h, or d)")=`'ms'`*)[¶](#ApiClient.TsBusFirstSignalCheck.SetTimeOptionTrueForAtLeast "Link to this definition")  
Sets the test step’s time option to “true for at least”.

Parameters:  minimumDuration : string[¶](#ApiClient.TsBusFirstSignalCheck.SetTimeOptionTrueForAtLeast.minimumDuration "Permalink to this definition")  
The minimum duration to be used

pollingCycle : string[¶](#ApiClient.TsBusFirstSignalCheck.SetTimeOptionTrueForAtLeast.pollingCycle "Permalink to this definition")  
Optional polling cycle to be used

timeoutUnit : string[¶](#ApiClient.TsBusFirstSignalCheck.SetTimeOptionTrueForAtLeast.timeoutUnit "Permalink to this definition")  
Optional unit of the timeout (ms, s, min, h or d)

pollingCycleUnit : string[¶](#ApiClient.TsBusFirstSignalCheck.SetTimeOptionTrueForAtLeast.pollingCycleUnit "Permalink to this definition")  
Optional unit of the polling cycle (ms, s, min, h, or d)

SetTimeOptionTrueForAtLeastWithin(*[minimumDuration](#ApiClient.TsBusFirstSignalCheck.SetTimeOptionTrueForAtLeastWithin.minimumDuration "ApiClient.TsBusFirstSignalCheck.SetTimeOptionTrueForAtLeastWithin.minimumDuration (Python parameter) — The minimum duration in ms to be used")*, *[timeout](#ApiClient.TsBusFirstSignalCheck.SetTimeOptionTrueForAtLeastWithin.timeout "ApiClient.TsBusFirstSignalCheck.SetTimeOptionTrueForAtLeastWithin.timeout (Python parameter) — The timeout to be used")*, *[pollingCycle](#ApiClient.TsBusFirstSignalCheck.SetTimeOptionTrueForAtLeastWithin.pollingCycle "ApiClient.TsBusFirstSignalCheck.SetTimeOptionTrueForAtLeastWithin.pollingCycle (Python parameter) — Optional polling cycle to be used")=`None`*, *[timeoutUnit](#ApiClient.TsBusFirstSignalCheck.SetTimeOptionTrueForAtLeastWithin.timeoutUnit "ApiClient.TsBusFirstSignalCheck.SetTimeOptionTrueForAtLeastWithin.timeoutUnit (Python parameter) — Optional unit of the timeout (ms, s, min, h or d)")=`'ms'`*, *[pollingCycleUnit](#ApiClient.TsBusFirstSignalCheck.SetTimeOptionTrueForAtLeastWithin.pollingCycleUnit "ApiClient.TsBusFirstSignalCheck.SetTimeOptionTrueForAtLeastWithin.pollingCycleUnit (Python parameter) — Optional unit of the polling cycle (ms, s, min, h, or d)")=`'ms'`*)[¶](#ApiClient.TsBusFirstSignalCheck.SetTimeOptionTrueForAtLeastWithin "Link to this definition")  
Sets the test step’s time option to “true for at least … within …”.

Parameters:  minimumDuration : string[¶](#ApiClient.TsBusFirstSignalCheck.SetTimeOptionTrueForAtLeastWithin.minimumDuration "Permalink to this definition")  
The minimum duration in ms to be used

timeout : string[¶](#ApiClient.TsBusFirstSignalCheck.SetTimeOptionTrueForAtLeastWithin.timeout "Permalink to this definition")  
The timeout to be used

pollingCycle : string[¶](#ApiClient.TsBusFirstSignalCheck.SetTimeOptionTrueForAtLeastWithin.pollingCycle "Permalink to this definition")  
Optional polling cycle to be used

timeoutUnit : string[¶](#ApiClient.TsBusFirstSignalCheck.SetTimeOptionTrueForAtLeastWithin.timeoutUnit "Permalink to this definition")  
Optional unit of the timeout (ms, s, min, h or d)

pollingCycleUnit : string[¶](#ApiClient.TsBusFirstSignalCheck.SetTimeOptionTrueForAtLeastWithin.pollingCycleUnit "Permalink to this definition")  
Optional unit of the polling cycle (ms, s, min, h, or d)

SetTimeOptionWaitUntilTrue(*[timeout](#ApiClient.TsBusFirstSignalCheck.SetTimeOptionWaitUntilTrue.timeout "ApiClient.TsBusFirstSignalCheck.SetTimeOptionWaitUntilTrue.timeout (Python parameter) — The timeout to be used")*, *[pollingCycle](#ApiClient.TsBusFirstSignalCheck.SetTimeOptionWaitUntilTrue.pollingCycle "ApiClient.TsBusFirstSignalCheck.SetTimeOptionWaitUntilTrue.pollingCycle (Python parameter) — Optional polling cycle to be used.")=`None`*, *[timeoutUnit](#ApiClient.TsBusFirstSignalCheck.SetTimeOptionWaitUntilTrue.timeoutUnit "ApiClient.TsBusFirstSignalCheck.SetTimeOptionWaitUntilTrue.timeoutUnit (Python parameter) — Optional unit of the timeout (ms, s, min, h or d)")=`'ms'`*, *[pollingCycleUnit](#ApiClient.TsBusFirstSignalCheck.SetTimeOptionWaitUntilTrue.pollingCycleUnit "ApiClient.TsBusFirstSignalCheck.SetTimeOptionWaitUntilTrue.pollingCycleUnit (Python parameter) — Optional unit of the polling cycle (ms, s, min, h, or d).")=`'ms'`*)[¶](#ApiClient.TsBusFirstSignalCheck.SetTimeOptionWaitUntilTrue "Link to this definition")  
Sets the test step’s time option to “wait until true”.

Parameters:  timeout : string[¶](#ApiClient.TsBusFirstSignalCheck.SetTimeOptionWaitUntilTrue.timeout "Permalink to this definition")  
The timeout to be used

pollingCycle : string[¶](#ApiClient.TsBusFirstSignalCheck.SetTimeOptionWaitUntilTrue.pollingCycle "Permalink to this definition")  
Optional polling cycle to be used.

timeoutUnit : string[¶](#ApiClient.TsBusFirstSignalCheck.SetTimeOptionWaitUntilTrue.timeoutUnit "Permalink to this definition")  
Optional unit of the timeout (ms, s, min, h or d)

pollingCycleUnit : string[¶](#ApiClient.TsBusFirstSignalCheck.SetTimeOptionWaitUntilTrue.pollingCycleUnit "Permalink to this definition")  
Optional unit of the polling cycle (ms, s, min, h, or d).

SetTranslatedCommentText(*[comment](#ApiClient.TsBusFirstSignalCheck.SetTranslatedCommentText.comment "ApiClient.TsBusFirstSignalCheck.SetTranslatedCommentText.comment (Python parameter) — Text to be displayed")*, *[language](#ApiClient.TsBusFirstSignalCheck.SetTranslatedCommentText.language "ApiClient.TsBusFirstSignalCheck.SetTranslatedCommentText.language (Python parameter) — Language of the text ('en_US', 'de_DE', 'zh_CN')")*)[¶](#ApiClient.TsBusFirstSignalCheck.SetTranslatedCommentText "Link to this definition")  
Sets a comment for the test step in the given language.

Parameters:  comment : str[¶](#ApiClient.TsBusFirstSignalCheck.SetTranslatedCommentText.comment "Permalink to this definition")  
Text to be displayed

language : str[¶](#ApiClient.TsBusFirstSignalCheck.SetTranslatedCommentText.language "Permalink to this definition")  
Language of the text (‘en_US’, ‘de_DE’, ‘zh_CN’)

SetUnit(*[unit](#ApiClient.TsBusFirstSignalCheck.SetUnit.unit "ApiClient.TsBusFirstSignalCheck.SetUnit.unit (Python parameter) — Unit for axis")*, *[axis](#ApiClient.TsBusFirstSignalCheck.SetUnit.axis "ApiClient.TsBusFirstSignalCheck.SetUnit.axis (Python parameter) — Axis to set unit for (x, y, z)")=`'z'`*)[¶](#ApiClient.TsBusFirstSignalCheck.SetUnit "Link to this definition")  
Sets the unit of a certain axis of the accessed test quantity.

Parameters:  unit : str[¶](#ApiClient.TsBusFirstSignalCheck.SetUnit.unit "Permalink to this definition")  
Unit for axis

axis : str[¶](#ApiClient.TsBusFirstSignalCheck.SetUnit.axis "Permalink to this definition")  
Axis to set unit for (x, y, z)

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
