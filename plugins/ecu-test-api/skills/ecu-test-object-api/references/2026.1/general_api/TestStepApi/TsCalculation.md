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

TsCalculation [ TsCalculation ](#)

TsCalculation

- [C TsCalculation ](#ApiClient.TsCalculation)
  - [M AddTag ](#ApiClient.TsCalculation.AddTag)
  - [M Clone ](#ApiClient.TsCalculation.Clone)
  - [M DeactivateExpectation ](#ApiClient.TsCalculation.DeactivateExpectation)
  - [M DeactivateFailedComment ](#ApiClient.TsCalculation.DeactivateFailedComment)
  - [M DeactivateSaveIn ](#ApiClient.TsCalculation.DeactivateSaveIn)
  - [M DeactivateSuccessComment ](#ApiClient.TsCalculation.DeactivateSuccessComment)
  - [M DeactivateTimeOption ](#ApiClient.TsCalculation.DeactivateTimeOption)
  - [M DeleteTranslatedCommentText ](#ApiClient.TsCalculation.DeleteTranslatedCommentText)
  - [M GetActionColumnText ](#ApiClient.TsCalculation.GetActionColumnText)
  - [M GetActiveTimeOptionType ](#ApiClient.TsCalculation.GetActiveTimeOptionType)
  - [M GetComment ](#ApiClient.TsCalculation.GetComment)
  - [M GetCommentColumnText ](#ApiClient.TsCalculation.GetCommentColumnText)
  - [M GetError ](#ApiClient.TsCalculation.GetError)
  - [M GetExpectation ](#ApiClient.TsCalculation.GetExpectation)
  - [M GetExpectationExpression ](#ApiClient.TsCalculation.GetExpectationExpression)
  - [M GetExpression ](#ApiClient.TsCalculation.GetExpression)
  - [M GetFailedComment ](#ApiClient.TsCalculation.GetFailedComment)
  - [M GetIndex ](#ApiClient.TsCalculation.GetIndex)
  - [M GetInstanceName ](#ApiClient.TsCalculation.GetInstanceName)
  - [M GetLineNo ](#ApiClient.TsCalculation.GetLineNo)
  - [M GetMinimumDuration ](#ApiClient.TsCalculation.GetMinimumDuration)
  - [M GetMinimumDurationUnit ](#ApiClient.TsCalculation.GetMinimumDurationUnit)
  - [M GetParameterColumnText ](#ApiClient.TsCalculation.GetParameterColumnText)
  - [M GetParent ](#ApiClient.TsCalculation.GetParent)
  - [M GetPollingCycle ](#ApiClient.TsCalculation.GetPollingCycle)
  - [M GetPollingCycleUnit ](#ApiClient.TsCalculation.GetPollingCycleUnit)
  - [M GetSaveInVariableName ](#ApiClient.TsCalculation.GetSaveInVariableName)
  - [M GetSuccessComment ](#ApiClient.TsCalculation.GetSuccessComment)
  - [M GetTags ](#ApiClient.TsCalculation.GetTags)
  - [M GetTestManagementId ](#ApiClient.TsCalculation.GetTestManagementId)
  - [M GetTestStepId ](#ApiClient.TsCalculation.GetTestStepId)
  - [M GetTimeout ](#ApiClient.TsCalculation.GetTimeout)
  - [M GetTimeoutUnit ](#ApiClient.TsCalculation.GetTimeoutUnit)
  - [M GetTranslatedCommentText ](#ApiClient.TsCalculation.GetTranslatedCommentText)
  - [M GetType ](#ApiClient.TsCalculation.GetType)
  - [M GetValueColumnText ](#ApiClient.TsCalculation.GetValueColumnText)
  - [M IsBreakpoint ](#ApiClient.TsCalculation.IsBreakpoint)
  - [M IsContainer ](#ApiClient.TsCalculation.IsContainer)
  - [M IsEnabled ](#ApiClient.TsCalculation.IsEnabled)
  - [M IsInPostcondition ](#ApiClient.TsCalculation.IsInPostcondition)
  - [M IsInPrecondition ](#ApiClient.TsCalculation.IsInPrecondition)
  - [M IsOk ](#ApiClient.TsCalculation.IsOk)
  - [M IsVisible ](#ApiClient.TsCalculation.IsVisible)
  - [M RemoveTag ](#ApiClient.TsCalculation.RemoveTag)
  - [M SetBreakpoint ](#ApiClient.TsCalculation.SetBreakpoint)
  - [M SetComment ](#ApiClient.TsCalculation.SetComment)
  - [M SetEnabled ](#ApiClient.TsCalculation.SetEnabled)
  - [M SetExpectation ](#ApiClient.TsCalculation.SetExpectation)
  - [M SetExpectationExpression ](#ApiClient.TsCalculation.SetExpectationExpression)
  - [M SetExpression ](#ApiClient.TsCalculation.SetExpression)
  - [M SetFailedComment ](#ApiClient.TsCalculation.SetFailedComment)
  - [M SetInstanceName ](#ApiClient.TsCalculation.SetInstanceName)
  - [M SetSaveInVariableName ](#ApiClient.TsCalculation.SetSaveInVariableName)
  - [M SetSuccessComment ](#ApiClient.TsCalculation.SetSuccessComment)
  - [M SetTags ](#ApiClient.TsCalculation.SetTags)
  - [M SetTestManagementId ](#ApiClient.TsCalculation.SetTestManagementId)
  - [M SetTimeOptionOnlySynchronization ](#ApiClient.TsCalculation.SetTimeOptionOnlySynchronization)
  - [M SetTimeOptionPollingCycleMultiplier ](#ApiClient.TsCalculation.SetTimeOptionPollingCycleMultiplier)
  - [M SetTimeOptionTrueForAtLeast ](#ApiClient.TsCalculation.SetTimeOptionTrueForAtLeast)
  - [M SetTimeOptionTrueForAtLeastWithin ](#ApiClient.TsCalculation.SetTimeOptionTrueForAtLeastWithin)
  - [M SetTimeOptionWaitUntilTrue ](#ApiClient.TsCalculation.SetTimeOptionWaitUntilTrue)
  - [M SetTranslatedCommentText ](#ApiClient.TsCalculation.SetTranslatedCommentText)

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

TsCalculation

- [C TsCalculation ](#ApiClient.TsCalculation)
  - [M AddTag ](#ApiClient.TsCalculation.AddTag)
  - [M Clone ](#ApiClient.TsCalculation.Clone)
  - [M DeactivateExpectation ](#ApiClient.TsCalculation.DeactivateExpectation)
  - [M DeactivateFailedComment ](#ApiClient.TsCalculation.DeactivateFailedComment)
  - [M DeactivateSaveIn ](#ApiClient.TsCalculation.DeactivateSaveIn)
  - [M DeactivateSuccessComment ](#ApiClient.TsCalculation.DeactivateSuccessComment)
  - [M DeactivateTimeOption ](#ApiClient.TsCalculation.DeactivateTimeOption)
  - [M DeleteTranslatedCommentText ](#ApiClient.TsCalculation.DeleteTranslatedCommentText)
  - [M GetActionColumnText ](#ApiClient.TsCalculation.GetActionColumnText)
  - [M GetActiveTimeOptionType ](#ApiClient.TsCalculation.GetActiveTimeOptionType)
  - [M GetComment ](#ApiClient.TsCalculation.GetComment)
  - [M GetCommentColumnText ](#ApiClient.TsCalculation.GetCommentColumnText)
  - [M GetError ](#ApiClient.TsCalculation.GetError)
  - [M GetExpectation ](#ApiClient.TsCalculation.GetExpectation)
  - [M GetExpectationExpression ](#ApiClient.TsCalculation.GetExpectationExpression)
  - [M GetExpression ](#ApiClient.TsCalculation.GetExpression)
  - [M GetFailedComment ](#ApiClient.TsCalculation.GetFailedComment)
  - [M GetIndex ](#ApiClient.TsCalculation.GetIndex)
  - [M GetInstanceName ](#ApiClient.TsCalculation.GetInstanceName)
  - [M GetLineNo ](#ApiClient.TsCalculation.GetLineNo)
  - [M GetMinimumDuration ](#ApiClient.TsCalculation.GetMinimumDuration)
  - [M GetMinimumDurationUnit ](#ApiClient.TsCalculation.GetMinimumDurationUnit)
  - [M GetParameterColumnText ](#ApiClient.TsCalculation.GetParameterColumnText)
  - [M GetParent ](#ApiClient.TsCalculation.GetParent)
  - [M GetPollingCycle ](#ApiClient.TsCalculation.GetPollingCycle)
  - [M GetPollingCycleUnit ](#ApiClient.TsCalculation.GetPollingCycleUnit)
  - [M GetSaveInVariableName ](#ApiClient.TsCalculation.GetSaveInVariableName)
  - [M GetSuccessComment ](#ApiClient.TsCalculation.GetSuccessComment)
  - [M GetTags ](#ApiClient.TsCalculation.GetTags)
  - [M GetTestManagementId ](#ApiClient.TsCalculation.GetTestManagementId)
  - [M GetTestStepId ](#ApiClient.TsCalculation.GetTestStepId)
  - [M GetTimeout ](#ApiClient.TsCalculation.GetTimeout)
  - [M GetTimeoutUnit ](#ApiClient.TsCalculation.GetTimeoutUnit)
  - [M GetTranslatedCommentText ](#ApiClient.TsCalculation.GetTranslatedCommentText)
  - [M GetType ](#ApiClient.TsCalculation.GetType)
  - [M GetValueColumnText ](#ApiClient.TsCalculation.GetValueColumnText)
  - [M IsBreakpoint ](#ApiClient.TsCalculation.IsBreakpoint)
  - [M IsContainer ](#ApiClient.TsCalculation.IsContainer)
  - [M IsEnabled ](#ApiClient.TsCalculation.IsEnabled)
  - [M IsInPostcondition ](#ApiClient.TsCalculation.IsInPostcondition)
  - [M IsInPrecondition ](#ApiClient.TsCalculation.IsInPrecondition)
  - [M IsOk ](#ApiClient.TsCalculation.IsOk)
  - [M IsVisible ](#ApiClient.TsCalculation.IsVisible)
  - [M RemoveTag ](#ApiClient.TsCalculation.RemoveTag)
  - [M SetBreakpoint ](#ApiClient.TsCalculation.SetBreakpoint)
  - [M SetComment ](#ApiClient.TsCalculation.SetComment)
  - [M SetEnabled ](#ApiClient.TsCalculation.SetEnabled)
  - [M SetExpectation ](#ApiClient.TsCalculation.SetExpectation)
  - [M SetExpectationExpression ](#ApiClient.TsCalculation.SetExpectationExpression)
  - [M SetExpression ](#ApiClient.TsCalculation.SetExpression)
  - [M SetFailedComment ](#ApiClient.TsCalculation.SetFailedComment)
  - [M SetInstanceName ](#ApiClient.TsCalculation.SetInstanceName)
  - [M SetSaveInVariableName ](#ApiClient.TsCalculation.SetSaveInVariableName)
  - [M SetSuccessComment ](#ApiClient.TsCalculation.SetSuccessComment)
  - [M SetTags ](#ApiClient.TsCalculation.SetTags)
  - [M SetTestManagementId ](#ApiClient.TsCalculation.SetTestManagementId)
  - [M SetTimeOptionOnlySynchronization ](#ApiClient.TsCalculation.SetTimeOptionOnlySynchronization)
  - [M SetTimeOptionPollingCycleMultiplier ](#ApiClient.TsCalculation.SetTimeOptionPollingCycleMultiplier)
  - [M SetTimeOptionTrueForAtLeast ](#ApiClient.TsCalculation.SetTimeOptionTrueForAtLeast)
  - [M SetTimeOptionTrueForAtLeastWithin ](#ApiClient.TsCalculation.SetTimeOptionTrueForAtLeastWithin)
  - [M SetTimeOptionWaitUntilTrue ](#ApiClient.TsCalculation.SetTimeOptionWaitUntilTrue)
  - [M SetTranslatedCommentText ](#ApiClient.TsCalculation.SetTranslatedCommentText)

# TsCalculation[¶](#tscalculation "Link to this heading")

*class* TsCalculation[¶](#ApiClient.TsCalculation "Link to this definition")  
Returned by

- [`TestStepApi.CreateTsCalculation`](../TestStepApi.md#ApiClient.TestStepApi.CreateTsCalculation "ApiClient.TestStepApi.CreateTsCalculation (Python method) — Creates a calculation test step.")

AddTag(*[tag](#ApiClient.TsCalculation.AddTag.tag "ApiClient.TsCalculation.AddTag.tag (Python parameter) — The tag to be set")*)[¶](#ApiClient.TsCalculation.AddTag "Link to this definition")  
Add a specific tag to this step.

Parameters:  tag : str[¶](#ApiClient.TsCalculation.AddTag.tag "Permalink to this definition")  
The tag to be set

Clone()[¶](#ApiClient.TsCalculation.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`TsCalculation`](#ApiClient.TsCalculation "ApiClient.TsCalculation (Python class) — TestStepApi.CreateTsCalculation")

DeactivateExpectation()[¶](#ApiClient.TsCalculation.DeactivateExpectation "Link to this definition")  
Deactivates the expectation so that the result will not be evaluated.

DeactivateFailedComment()[¶](#ApiClient.TsCalculation.DeactivateFailedComment "Link to this definition")  
Deactivates the expectation for the failed comment so that the result will not be evaluated.

DeactivateSaveIn()[¶](#ApiClient.TsCalculation.DeactivateSaveIn "Link to this definition")  
Deactivates the test step’s save in property, so the value will not be stored in a package variable.

DeactivateSuccessComment()[¶](#ApiClient.TsCalculation.DeactivateSuccessComment "Link to this definition")  
Deactivates the expectation for the success comment so that the result will not be evaluated.

DeactivateTimeOption()[¶](#ApiClient.TsCalculation.DeactivateTimeOption "Link to this definition")  
Deactivates any time option set on the test step. This is equivalent to selecting the option “none” in the test step’s time options menu.

DeleteTranslatedCommentText(*[language](#ApiClient.TsCalculation.DeleteTranslatedCommentText.language "ApiClient.TsCalculation.DeleteTranslatedCommentText.language (Python parameter) — Language of the text ('en_US', 'de_DE', 'zh_CN')")*)[¶](#ApiClient.TsCalculation.DeleteTranslatedCommentText "Link to this definition")  
Deletes a comment for the test step in the given language.

Parameters:  language : str[¶](#ApiClient.TsCalculation.DeleteTranslatedCommentText.language "Permalink to this definition")  
Language of the text (‘en_US’, ‘de_DE’, ‘zh_CN’)

GetActionColumnText()[¶](#ApiClient.TsCalculation.GetActionColumnText "Link to this definition")  
Returns the text value of the “action” column.

Returns:  Action column text

Return type:  str

GetActiveTimeOptionType()[¶](#ApiClient.TsCalculation.GetActiveTimeOptionType "Link to this definition")  
Returns the type of the currently active time option.

Returns:  Type of active time option (“Timeless”, “Finally”, “TrueForWithin”, “Generally”, “SyncOnly”, “PollingCycleMultiplier”)

Return type:  string

GetComment()[¶](#ApiClient.TsCalculation.GetComment "Link to this definition")  
Returns the comment of the test step in the current test case language.

Returns:  Comment text as shown in the comment tab

Return type:  str

GetCommentColumnText()[¶](#ApiClient.TsCalculation.GetCommentColumnText "Link to this definition")  
Returns the text value of the “comment” column.

Returns:  Comment column text

Return type:  str

GetError()[¶](#ApiClient.TsCalculation.GetError "Link to this definition")  
Returns a list of errors. Note that the error messages depend on the program language ecu.test is set to. Because of that we do not recommend to check against exact error messages, unless you are certain about the respective program language.

Returns:  List of errors

Return type:  list[str]

GetExpectation()[¶](#ApiClient.TsCalculation.GetExpectation "Link to this definition")  
Returns the expectation expression from the evaluation of the test step, or None, if no expectation was defined.

Returns:  The expectation

Return type:  [`Expectation`](../ExpectationApi/Expectation.md#ApiClient.Expectation "ApiClient.Expectation (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")

GetExpectationExpression()[¶](#ApiClient.TsCalculation.GetExpectationExpression "Link to this definition")  
Returns the expectation expression from the evaluation of the test step, or None, if no expectation was defined.

Returns:  The expectation

Return type:  string

GetExpression()[¶](#ApiClient.TsCalculation.GetExpression "Link to this definition")  
Returns the expression of the calculation test step.

Returns:  Expression of the calculation test step

Return type:  str

GetFailedComment()[¶](#ApiClient.TsCalculation.GetFailedComment "Link to this definition")  
Returns the failed comment of the step.

Returns:  The failed comment

Return type:  string

GetIndex()[¶](#ApiClient.TsCalculation.GetIndex "Link to this definition")  
Returns the zero based index in the parent.

Returns:  Zero based index

Return type:  integer

GetInstanceName()[¶](#ApiClient.TsCalculation.GetInstanceName "Link to this definition")  
Returns the instance name of the test step. If no name has been set, this method returns the same as GetName().

Returns:  The instance name

Return type:  string

GetLineNo()[¶](#ApiClient.TsCalculation.GetLineNo "Link to this definition")  
Returns the test steps line number within its test case.

Returns:  Line number

Return type:  int

GetMinimumDuration()[¶](#ApiClient.TsCalculation.GetMinimumDuration "Link to this definition")  
Returns the minimum duration of the test step’s time option, if a corresponding option has been set.

Returns:  The minimum duration, else None

Return type:  string

GetMinimumDurationUnit()[¶](#ApiClient.TsCalculation.GetMinimumDurationUnit "Link to this definition")  
Returns the unit of the minimum duration of the test step’s time option, if a corresponding option has been set.

Returns:  The unit of the minimum duration, else None

Return type:  string

GetParameterColumnText()[¶](#ApiClient.TsCalculation.GetParameterColumnText "Link to this definition")  
Returns the text value of the “parameter” column.

Returns:  Parameter column text

Return type:  str

GetParent()[¶](#ApiClient.TsCalculation.GetParent "Link to this definition")  
Returns the parent test step.

Returns:  The parent test step or None if it is a top level test step.

Return type:  [`TestStep`](../PackageApi/TestStep.md#ApiClient.TestStep "ApiClient.TestStep (Python class) — Add a specific tag to this step.")

GetPollingCycle()[¶](#ApiClient.TsCalculation.GetPollingCycle "Link to this definition")  
Returns the polling cycle of the test step’s time option, if a corresponding option has been set.

Returns:  The polling cycle, else None

Return type:  string

GetPollingCycleUnit()[¶](#ApiClient.TsCalculation.GetPollingCycleUnit "Link to this definition")  
Returns the unit of the polling cycle of the test step’s time option, if a corresponding option has been set.

Returns:  The unit of the polling cycle, else None

Return type:  string

GetSaveInVariableName()[¶](#ApiClient.TsCalculation.GetSaveInVariableName "Link to this definition")  
Returns the currently selected variable to save the data.

Returns:  The variable’s name

Return type:  string

GetSuccessComment()[¶](#ApiClient.TsCalculation.GetSuccessComment "Link to this definition")  
Returns the success comment of the step.

Returns:  The success comment

Return type:  string

GetTags()[¶](#ApiClient.TsCalculation.GetTags "Link to this definition")  
Returns the tags set for this step.

Returns:  A (sorted) list of tags

Return type:  list[str]

GetTestManagementId()[¶](#ApiClient.TsCalculation.GetTestManagementId "Link to this definition")  
Returns the test management id of the test step.

Returns:  Test step id.

Return type:  str

GetTestStepId()[¶](#ApiClient.TsCalculation.GetTestStepId "Link to this definition")  
Returns the test step id.

Returns:  test step id

Return type:  str

GetTimeout()[¶](#ApiClient.TsCalculation.GetTimeout "Link to this definition")  
Returns the timeout of the test step’s time option, if a corresponding option has been set.

Returns:  The timeout else None

Return type:  string

GetTimeoutUnit()[¶](#ApiClient.TsCalculation.GetTimeoutUnit "Link to this definition")  
Returns the unit of the timeout of the test step’s time option, if a corresponding option has been set.

Returns:  The unit of the timeout else None

Return type:  string

GetTranslatedCommentText(*[language](#ApiClient.TsCalculation.GetTranslatedCommentText.language "ApiClient.TsCalculation.GetTranslatedCommentText.language (Python parameter) — Language of the requested text ('en_US', 'de_DE', 'zh_CN')")*)[¶](#ApiClient.TsCalculation.GetTranslatedCommentText "Link to this definition")  
Returns the text value of the “comment” column in the given language.

Parameters:  language : str[¶](#ApiClient.TsCalculation.GetTranslatedCommentText.language "Permalink to this definition")  
Language of the requested text (‘en_US’, ‘de_DE’, ‘zh_CN’)

Returns:  Comment column text

Return type:  str

GetType()[¶](#ApiClient.TsCalculation.GetType "Link to this definition")  
Returns the type (class name) of the test step, e.g.

- “TsPreconditionBlock”

- “TsWait”

- “TsIfThenElse”

- “TsSwitchCase”

- “TsCaseNode”

Returns:  Type (class name) of the test step

Return type:  str

GetValueColumnText()[¶](#ApiClient.TsCalculation.GetValueColumnText "Link to this definition")  
Returns the text value of the “value” column in your current test case language.

Returns:  Value column text

Return type:  str

IsBreakpoint()[¶](#ApiClient.TsCalculation.IsBreakpoint "Link to this definition")  
Checks whether the test step is a break point.

Returns:  True if test step is a break point, else False

Return type:  boolean

IsContainer()[¶](#ApiClient.TsCalculation.IsContainer "Link to this definition")  
Returns True, if the test step supports calling GetChildren as well as manipulating the structure of its children. (e. g. via inserting or deleting sub test steps).

Returns:  True if it can contain test steps, else False

Return type:  boolean

IsEnabled()[¶](#ApiClient.TsCalculation.IsEnabled "Link to this definition")  
Returns the state of the test step.

Returns:  True if test step is enabled, otherwise False

Return type:  bool

IsInPostcondition()[¶](#ApiClient.TsCalculation.IsInPostcondition "Link to this definition")  
Returns True if the test step is located in a postcondition

Returns:  True if the test step is located in a postcondition, else Flase

Return type:  bool

IsInPrecondition()[¶](#ApiClient.TsCalculation.IsInPrecondition "Link to this definition")  
Returns True if the test step is located in a precondition

Returns:  True if the test step is located in a precondition, else False

Return type:  bool

IsOk()[¶](#ApiClient.TsCalculation.IsOk "Link to this definition")  
Returns the internal state of correctness of the test step.

Returns:  True if no problems were found, else False

Return type:  boolean

IsVisible()[¶](#ApiClient.TsCalculation.IsVisible "Link to this definition")  
Checks whether the test step is visible. This depends on the test step itself or a parent test step being disabled.

Returns:  True if test step is visible, else False

Return type:  boolean

RemoveTag(*[tag](#ApiClient.TsCalculation.RemoveTag.tag "ApiClient.TsCalculation.RemoveTag.tag (Python parameter) — The tag to be removed")*)[¶](#ApiClient.TsCalculation.RemoveTag "Link to this definition")  
Remove a specific tag from this step.

Parameters:  tag : str[¶](#ApiClient.TsCalculation.RemoveTag.tag "Permalink to this definition")  
The tag to be removed

SetBreakpoint(*[enable](#ApiClient.TsCalculation.SetBreakpoint.enable "ApiClient.TsCalculation.SetBreakpoint.enable (Python parameter) — True if test step is a break point, else False")*)[¶](#ApiClient.TsCalculation.SetBreakpoint "Link to this definition")  
Sets or unsets the test step to act as a break point.

Parameters:  enable : boolean[¶](#ApiClient.TsCalculation.SetBreakpoint.enable "Permalink to this definition")  
True if test step is a break point, else False

SetComment(*[comment](#ApiClient.TsCalculation.SetComment.comment "ApiClient.TsCalculation.SetComment.comment (Python parameter) — Text to be displayed in the comment tab")*)[¶](#ApiClient.TsCalculation.SetComment "Link to this definition")  
Sets a comment for the test step in the current test case language.

Parameters:  comment : str[¶](#ApiClient.TsCalculation.SetComment.comment "Permalink to this definition")  
Text to be displayed in the comment tab

SetEnabled(*[state](#ApiClient.TsCalculation.SetEnabled.state "ApiClient.TsCalculation.SetEnabled.state (Python parameter) — True (Default) to enable, False to disable the test step.")=`True`*)[¶](#ApiClient.TsCalculation.SetEnabled "Link to this definition")  
Enable or disable the test step.

Parameters:  state : bool[¶](#ApiClient.TsCalculation.SetEnabled.state "Permalink to this definition")  
True (Default) to enable, False to disable the test step.

SetExpectation(*[expectation](#ApiClient.TsCalculation.SetExpectation.expectation "ApiClient.TsCalculation.SetExpectation.expectation (Python parameter) — The expectation")*)[¶](#ApiClient.TsCalculation.SetExpectation "Link to this definition")  
Sets the expectation in the evaluation of the test step. The expectation will be activated if it was not enabled previously.

Parameters:  expectation[¶](#ApiClient.TsCalculation.SetExpectation.expectation "Permalink to this definition")  
The expectation

SetExpectationExpression(*[expectation](#ApiClient.TsCalculation.SetExpectationExpression.expectation "ApiClient.TsCalculation.SetExpectationExpression.expectation (Python parameter) — The expectation")*)[¶](#ApiClient.TsCalculation.SetExpectationExpression "Link to this definition")  
Shortcut to set an expectation for an unspecific type in the evaluation of the test step. The expectation will be activated if it was not enabled previously.

Parameters:  expectation : string[¶](#ApiClient.TsCalculation.SetExpectationExpression.expectation "Permalink to this definition")  
The expectation

SetExpression(*[expression](#ApiClient.TsCalculation.SetExpression.expression "ApiClient.TsCalculation.SetExpression.expression (Python parameter) — Expression of the calculation test step")=`'0'`*)[¶](#ApiClient.TsCalculation.SetExpression "Link to this definition")  
Sets the expression of the calculation test step.

Parameters:  expression : str[¶](#ApiClient.TsCalculation.SetExpression.expression "Permalink to this definition")  
Expression of the calculation test step

SetFailedComment(*[failedComment](#ApiClient.TsCalculation.SetFailedComment.failedComment "ApiClient.TsCalculation.SetFailedComment.failedComment (Python parameter) — The expression for the failed comment")*)[¶](#ApiClient.TsCalculation.SetFailedComment "Link to this definition")  
Sets the expression for the failed comment of the step. The expression will be activated if it was not enabled previously.

Parameters:  failedComment : string[¶](#ApiClient.TsCalculation.SetFailedComment.failedComment "Permalink to this definition")  
The expression for the failed comment

SetInstanceName(*[name](#ApiClient.TsCalculation.SetInstanceName.name "ApiClient.TsCalculation.SetInstanceName.name (Python parameter) — The instance name to be set")*)[¶](#ApiClient.TsCalculation.SetInstanceName "Link to this definition")  
Sets the instance name of the test step. By default (if no instance name has been set explicitely) the instance name is equal to GetName().

Parameters:  name : string[¶](#ApiClient.TsCalculation.SetInstanceName.name "Permalink to this definition")  
The instance name to be set

SetSaveInVariableName(*[variableName](#ApiClient.TsCalculation.SetSaveInVariableName.variableName "ApiClient.TsCalculation.SetSaveInVariableName.variableName (Python parameter) — The variable's name.")*)[¶](#ApiClient.TsCalculation.SetSaveInVariableName "Link to this definition")  
Sets the name of the variable used for storing data by the test step. The variable will be created automatically if it does not already exist in the package where the test step is placed in. This method must not be called, if the test step has not been added to a package previously.

Parameters:  variableName : string[¶](#ApiClient.TsCalculation.SetSaveInVariableName.variableName "Permalink to this definition")  
The variable’s name. Must not be None or an empty string.

Raises:  
**ApiError** –

- If SaveIn was called before the test step was added to a package.

- If variableName is None or an empty string

SetSuccessComment(*[successComment](#ApiClient.TsCalculation.SetSuccessComment.successComment "ApiClient.TsCalculation.SetSuccessComment.successComment (Python parameter) — The expression for the success comment")*)[¶](#ApiClient.TsCalculation.SetSuccessComment "Link to this definition")  
Sets the expression for the success comment of the step. The expression will be activated if it was not enabled previously.

Parameters:  successComment : string[¶](#ApiClient.TsCalculation.SetSuccessComment.successComment "Permalink to this definition")  
The expression for the success comment

SetTags(*[tags](#ApiClient.TsCalculation.SetTags.tags "ApiClient.TsCalculation.SetTags.tags (Python parameter) — The list of tags")*)[¶](#ApiClient.TsCalculation.SetTags "Link to this definition")  
Set the list of tags for this step. The list of tags will be sorted and stored.

Parameters:  tags : list[str][¶](#ApiClient.TsCalculation.SetTags.tags "Permalink to this definition")  
The list of tags

SetTestManagementId(*[testManagementId](#ApiClient.TsCalculation.SetTestManagementId.testManagementId "ApiClient.TsCalculation.SetTestManagementId.testManagementId (Python parameter) — Test management id of the test step")*)[¶](#ApiClient.TsCalculation.SetTestManagementId "Link to this definition")  
Sets the test management id of the test step.

Parameters:  testManagementId : str[¶](#ApiClient.TsCalculation.SetTestManagementId.testManagementId "Permalink to this definition")  
Test management id of the test step

SetTimeOptionOnlySynchronization(*[timeout](#ApiClient.TsCalculation.SetTimeOptionOnlySynchronization.timeout "ApiClient.TsCalculation.SetTimeOptionOnlySynchronization.timeout (Python parameter) — The timeout in ms to be used")*, *[pollingCycle](#ApiClient.TsCalculation.SetTimeOptionOnlySynchronization.pollingCycle "ApiClient.TsCalculation.SetTimeOptionOnlySynchronization.pollingCycle (Python parameter) — The polling cycle in ms or s or min or h or d.")=`None`*, *[timeoutUnit](#ApiClient.TsCalculation.SetTimeOptionOnlySynchronization.timeoutUnit "ApiClient.TsCalculation.SetTimeOptionOnlySynchronization.timeoutUnit (Python parameter) — Optional unit of the timeout (ms, s, min, h or d)")=`'ms'`*, *[pollingCycleUnit](#ApiClient.TsCalculation.SetTimeOptionOnlySynchronization.pollingCycleUnit "ApiClient.TsCalculation.SetTimeOptionOnlySynchronization.pollingCycleUnit (Python parameter) — Optional unit of the polling cycle (ms, s, min, h, or d)")=`'ms'`*)[¶](#ApiClient.TsCalculation.SetTimeOptionOnlySynchronization "Link to this definition")  
Sets the test step’s time option to “only synchronization”.

Parameters:  timeout : string[¶](#ApiClient.TsCalculation.SetTimeOptionOnlySynchronization.timeout "Permalink to this definition")  
The timeout in ms to be used

pollingCycle : string[¶](#ApiClient.TsCalculation.SetTimeOptionOnlySynchronization.pollingCycle "Permalink to this definition")  
The polling cycle in ms or s or min or h or d. Might be left out.

timeoutUnit : string[¶](#ApiClient.TsCalculation.SetTimeOptionOnlySynchronization.timeoutUnit "Permalink to this definition")  
Optional unit of the timeout (ms, s, min, h or d)

pollingCycleUnit : string[¶](#ApiClient.TsCalculation.SetTimeOptionOnlySynchronization.pollingCycleUnit "Permalink to this definition")  
Optional unit of the polling cycle (ms, s, min, h, or d)

SetTimeOptionPollingCycleMultiplier(*[pollingCycleMultiplier](#ApiClient.TsCalculation.SetTimeOptionPollingCycleMultiplier.pollingCycleMultiplier "ApiClient.TsCalculation.SetTimeOptionPollingCycleMultiplier.pollingCycleMultiplier (Python parameter) — The polling cycle multiplier to be used.")*)[¶](#ApiClient.TsCalculation.SetTimeOptionPollingCycleMultiplier "Link to this definition")  
Sets the test step’s time option to “polling cycle multiplier”. This option must only be used when inserting the test step into a Multi-Check!

Parameters:  pollingCycleMultiplier : string[¶](#ApiClient.TsCalculation.SetTimeOptionPollingCycleMultiplier.pollingCycleMultiplier "Permalink to this definition")  
The polling cycle multiplier to be used.

SetTimeOptionTrueForAtLeast(*[minimumDuration](#ApiClient.TsCalculation.SetTimeOptionTrueForAtLeast.minimumDuration "ApiClient.TsCalculation.SetTimeOptionTrueForAtLeast.minimumDuration (Python parameter) — The minimum duration to be used")*, *[pollingCycle](#ApiClient.TsCalculation.SetTimeOptionTrueForAtLeast.pollingCycle "ApiClient.TsCalculation.SetTimeOptionTrueForAtLeast.pollingCycle (Python parameter) — Optional polling cycle to be used")=`None`*, *[timeoutUnit](#ApiClient.TsCalculation.SetTimeOptionTrueForAtLeast.timeoutUnit "ApiClient.TsCalculation.SetTimeOptionTrueForAtLeast.timeoutUnit (Python parameter) — Optional unit of the timeout (ms, s, min, h or d)")=`'ms'`*, *[pollingCycleUnit](#ApiClient.TsCalculation.SetTimeOptionTrueForAtLeast.pollingCycleUnit "ApiClient.TsCalculation.SetTimeOptionTrueForAtLeast.pollingCycleUnit (Python parameter) — Optional unit of the polling cycle (ms, s, min, h, or d)")=`'ms'`*)[¶](#ApiClient.TsCalculation.SetTimeOptionTrueForAtLeast "Link to this definition")  
Sets the test step’s time option to “true for at least”.

Parameters:  minimumDuration : string[¶](#ApiClient.TsCalculation.SetTimeOptionTrueForAtLeast.minimumDuration "Permalink to this definition")  
The minimum duration to be used

pollingCycle : string[¶](#ApiClient.TsCalculation.SetTimeOptionTrueForAtLeast.pollingCycle "Permalink to this definition")  
Optional polling cycle to be used

timeoutUnit : string[¶](#ApiClient.TsCalculation.SetTimeOptionTrueForAtLeast.timeoutUnit "Permalink to this definition")  
Optional unit of the timeout (ms, s, min, h or d)

pollingCycleUnit : string[¶](#ApiClient.TsCalculation.SetTimeOptionTrueForAtLeast.pollingCycleUnit "Permalink to this definition")  
Optional unit of the polling cycle (ms, s, min, h, or d)

SetTimeOptionTrueForAtLeastWithin(*[minimumDuration](#ApiClient.TsCalculation.SetTimeOptionTrueForAtLeastWithin.minimumDuration "ApiClient.TsCalculation.SetTimeOptionTrueForAtLeastWithin.minimumDuration (Python parameter) — The minimum duration in ms to be used")*, *[timeout](#ApiClient.TsCalculation.SetTimeOptionTrueForAtLeastWithin.timeout "ApiClient.TsCalculation.SetTimeOptionTrueForAtLeastWithin.timeout (Python parameter) — The timeout to be used")*, *[pollingCycle](#ApiClient.TsCalculation.SetTimeOptionTrueForAtLeastWithin.pollingCycle "ApiClient.TsCalculation.SetTimeOptionTrueForAtLeastWithin.pollingCycle (Python parameter) — Optional polling cycle to be used")=`None`*, *[timeoutUnit](#ApiClient.TsCalculation.SetTimeOptionTrueForAtLeastWithin.timeoutUnit "ApiClient.TsCalculation.SetTimeOptionTrueForAtLeastWithin.timeoutUnit (Python parameter) — Optional unit of the timeout (ms, s, min, h or d)")=`'ms'`*, *[pollingCycleUnit](#ApiClient.TsCalculation.SetTimeOptionTrueForAtLeastWithin.pollingCycleUnit "ApiClient.TsCalculation.SetTimeOptionTrueForAtLeastWithin.pollingCycleUnit (Python parameter) — Optional unit of the polling cycle (ms, s, min, h, or d)")=`'ms'`*)[¶](#ApiClient.TsCalculation.SetTimeOptionTrueForAtLeastWithin "Link to this definition")  
Sets the test step’s time option to “true for at least … within …”.

Parameters:  minimumDuration : string[¶](#ApiClient.TsCalculation.SetTimeOptionTrueForAtLeastWithin.minimumDuration "Permalink to this definition")  
The minimum duration in ms to be used

timeout : string[¶](#ApiClient.TsCalculation.SetTimeOptionTrueForAtLeastWithin.timeout "Permalink to this definition")  
The timeout to be used

pollingCycle : string[¶](#ApiClient.TsCalculation.SetTimeOptionTrueForAtLeastWithin.pollingCycle "Permalink to this definition")  
Optional polling cycle to be used

timeoutUnit : string[¶](#ApiClient.TsCalculation.SetTimeOptionTrueForAtLeastWithin.timeoutUnit "Permalink to this definition")  
Optional unit of the timeout (ms, s, min, h or d)

pollingCycleUnit : string[¶](#ApiClient.TsCalculation.SetTimeOptionTrueForAtLeastWithin.pollingCycleUnit "Permalink to this definition")  
Optional unit of the polling cycle (ms, s, min, h, or d)

SetTimeOptionWaitUntilTrue(*[timeout](#ApiClient.TsCalculation.SetTimeOptionWaitUntilTrue.timeout "ApiClient.TsCalculation.SetTimeOptionWaitUntilTrue.timeout (Python parameter) — The timeout to be used")*, *[pollingCycle](#ApiClient.TsCalculation.SetTimeOptionWaitUntilTrue.pollingCycle "ApiClient.TsCalculation.SetTimeOptionWaitUntilTrue.pollingCycle (Python parameter) — Optional polling cycle to be used.")=`None`*, *[timeoutUnit](#ApiClient.TsCalculation.SetTimeOptionWaitUntilTrue.timeoutUnit "ApiClient.TsCalculation.SetTimeOptionWaitUntilTrue.timeoutUnit (Python parameter) — Optional unit of the timeout (ms, s, min, h or d)")=`'ms'`*, *[pollingCycleUnit](#ApiClient.TsCalculation.SetTimeOptionWaitUntilTrue.pollingCycleUnit "ApiClient.TsCalculation.SetTimeOptionWaitUntilTrue.pollingCycleUnit (Python parameter) — Optional unit of the polling cycle (ms, s, min, h, or d).")=`'ms'`*)[¶](#ApiClient.TsCalculation.SetTimeOptionWaitUntilTrue "Link to this definition")  
Sets the test step’s time option to “wait until true”.

Parameters:  timeout : string[¶](#ApiClient.TsCalculation.SetTimeOptionWaitUntilTrue.timeout "Permalink to this definition")  
The timeout to be used

pollingCycle : string[¶](#ApiClient.TsCalculation.SetTimeOptionWaitUntilTrue.pollingCycle "Permalink to this definition")  
Optional polling cycle to be used.

timeoutUnit : string[¶](#ApiClient.TsCalculation.SetTimeOptionWaitUntilTrue.timeoutUnit "Permalink to this definition")  
Optional unit of the timeout (ms, s, min, h or d)

pollingCycleUnit : string[¶](#ApiClient.TsCalculation.SetTimeOptionWaitUntilTrue.pollingCycleUnit "Permalink to this definition")  
Optional unit of the polling cycle (ms, s, min, h, or d).

SetTranslatedCommentText(*[comment](#ApiClient.TsCalculation.SetTranslatedCommentText.comment "ApiClient.TsCalculation.SetTranslatedCommentText.comment (Python parameter) — Text to be displayed")*, *[language](#ApiClient.TsCalculation.SetTranslatedCommentText.language "ApiClient.TsCalculation.SetTranslatedCommentText.language (Python parameter) — Language of the text ('en_US', 'de_DE', 'zh_CN')")*)[¶](#ApiClient.TsCalculation.SetTranslatedCommentText "Link to this definition")  
Sets a comment for the test step in the given language.

Parameters:  comment : str[¶](#ApiClient.TsCalculation.SetTranslatedCommentText.comment "Permalink to this definition")  
Text to be displayed

language : str[¶](#ApiClient.TsCalculation.SetTranslatedCommentText.language "Permalink to this definition")  
Language of the text (‘en_US’, ‘de_DE’, ‘zh_CN’)

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
