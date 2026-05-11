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

TsBlock [ TsBlock ](#)

TsBlock

- [C TsBlock ](#ApiClient.TsBlock)
  - [M AddTag ](#ApiClient.TsBlock.AddTag)
  - [M AppendTestStep ](#ApiClient.TsBlock.AppendTestStep)
  - [M Clone ](#ApiClient.TsBlock.Clone)
  - [M DeleteTranslatedActionColumnText ](#ApiClient.TsBlock.DeleteTranslatedActionColumnText)
  - [M DeleteTranslatedCommentText ](#ApiClient.TsBlock.DeleteTranslatedCommentText)
  - [M DeleteTranslatedParameterColumnText ](#ApiClient.TsBlock.DeleteTranslatedParameterColumnText)
  - [M DeleteTranslatedValueColumnText ](#ApiClient.TsBlock.DeleteTranslatedValueColumnText)
  - [M DisableReporting ](#ApiClient.TsBlock.DisableReporting)
  - [M DisableReportingFor ](#ApiClient.TsBlock.DisableReportingFor)
  - [M GetAbortCode ](#ApiClient.TsBlock.GetAbortCode)
  - [M GetAbortComment ](#ApiClient.TsBlock.GetAbortComment)
  - [M GetAbortCondition ](#ApiClient.TsBlock.GetAbortCondition)
  - [M GetActionColumnText ](#ApiClient.TsBlock.GetActionColumnText)
  - [M GetComment ](#ApiClient.TsBlock.GetComment)
  - [M GetCommentColumnText ](#ApiClient.TsBlock.GetCommentColumnText)
  - [M GetError ](#ApiClient.TsBlock.GetError)
  - [M GetIndex ](#ApiClient.TsBlock.GetIndex)
  - [M GetLineNo ](#ApiClient.TsBlock.GetLineNo)
  - [M GetParameterColumnText ](#ApiClient.TsBlock.GetParameterColumnText)
  - [M GetParent ](#ApiClient.TsBlock.GetParent)
  - [M GetReportDisablingResults ](#ApiClient.TsBlock.GetReportDisablingResults)
  - [M GetTags ](#ApiClient.TsBlock.GetTags)
  - [M GetTestManagementId ](#ApiClient.TsBlock.GetTestManagementId)
  - [M GetTestStepId ](#ApiClient.TsBlock.GetTestStepId)
  - [M GetTestSteps ](#ApiClient.TsBlock.GetTestSteps)
  - [M GetTranslatedActionColumnText ](#ApiClient.TsBlock.GetTranslatedActionColumnText)
  - [M GetTranslatedCommentText ](#ApiClient.TsBlock.GetTranslatedCommentText)
  - [M GetTranslatedParameterColumnText ](#ApiClient.TsBlock.GetTranslatedParameterColumnText)
  - [M GetTranslatedValueColumnText ](#ApiClient.TsBlock.GetTranslatedValueColumnText)
  - [M GetType ](#ApiClient.TsBlock.GetType)
  - [M GetValueColumnText ](#ApiClient.TsBlock.GetValueColumnText)
  - [M InsertTestStep ](#ApiClient.TsBlock.InsertTestStep)
  - [M IsBreakpoint ](#ApiClient.TsBlock.IsBreakpoint)
  - [M IsConditionalAbortEnabled ](#ApiClient.TsBlock.IsConditionalAbortEnabled)
  - [M IsConditionalEndEnabled ](#ApiClient.TsBlock.IsConditionalEndEnabled)
  - [M IsContainer ](#ApiClient.TsBlock.IsContainer)
  - [M IsEnabled ](#ApiClient.TsBlock.IsEnabled)
  - [M IsGeneratedByAgent ](#ApiClient.TsBlock.IsGeneratedByAgent)
  - [M IsInPostcondition ](#ApiClient.TsBlock.IsInPostcondition)
  - [M IsInPrecondition ](#ApiClient.TsBlock.IsInPrecondition)
  - [M IsOk ](#ApiClient.TsBlock.IsOk)
  - [M IsOverrideAbortInfoEnabled ](#ApiClient.TsBlock.IsOverrideAbortInfoEnabled)
  - [M IsReportingDisabled ](#ApiClient.TsBlock.IsReportingDisabled)
  - [M IsUserInteractionEnabled ](#ApiClient.TsBlock.IsUserInteractionEnabled)
  - [M IsVisible ](#ApiClient.TsBlock.IsVisible)
  - [M RemoveTag ](#ApiClient.TsBlock.RemoveTag)
  - [M RemoveTestStep ](#ApiClient.TsBlock.RemoveTestStep)
  - [M SetAbortCode ](#ApiClient.TsBlock.SetAbortCode)
  - [M SetAbortComment ](#ApiClient.TsBlock.SetAbortComment)
  - [M SetAbortCondition ](#ApiClient.TsBlock.SetAbortCondition)
  - [M SetActionColumnText ](#ApiClient.TsBlock.SetActionColumnText)
  - [M SetBreakpoint ](#ApiClient.TsBlock.SetBreakpoint)
  - [M SetComment ](#ApiClient.TsBlock.SetComment)
  - [M SetConditionalAbort ](#ApiClient.TsBlock.SetConditionalAbort)
  - [M SetConditionalEnd ](#ApiClient.TsBlock.SetConditionalEnd)
  - [M SetEnabled ](#ApiClient.TsBlock.SetEnabled)
  - [M SetOverrideAbortInfo ](#ApiClient.TsBlock.SetOverrideAbortInfo)
  - [M SetParameterColumnText ](#ApiClient.TsBlock.SetParameterColumnText)
  - [M SetTags ](#ApiClient.TsBlock.SetTags)
  - [M SetTestManagementId ](#ApiClient.TsBlock.SetTestManagementId)
  - [M SetTranslatedActionColumnText ](#ApiClient.TsBlock.SetTranslatedActionColumnText)
  - [M SetTranslatedCommentText ](#ApiClient.TsBlock.SetTranslatedCommentText)
  - [M SetTranslatedParameterColumnText ](#ApiClient.TsBlock.SetTranslatedParameterColumnText)
  - [M SetTranslatedValueColumnText ](#ApiClient.TsBlock.SetTranslatedValueColumnText)
  - [M SetUserInteraction ](#ApiClient.TsBlock.SetUserInteraction)
  - [M SetValueColumnText ](#ApiClient.TsBlock.SetValueColumnText)

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

TsBlock

- [C TsBlock ](#ApiClient.TsBlock)
  - [M AddTag ](#ApiClient.TsBlock.AddTag)
  - [M AppendTestStep ](#ApiClient.TsBlock.AppendTestStep)
  - [M Clone ](#ApiClient.TsBlock.Clone)
  - [M DeleteTranslatedActionColumnText ](#ApiClient.TsBlock.DeleteTranslatedActionColumnText)
  - [M DeleteTranslatedCommentText ](#ApiClient.TsBlock.DeleteTranslatedCommentText)
  - [M DeleteTranslatedParameterColumnText ](#ApiClient.TsBlock.DeleteTranslatedParameterColumnText)
  - [M DeleteTranslatedValueColumnText ](#ApiClient.TsBlock.DeleteTranslatedValueColumnText)
  - [M DisableReporting ](#ApiClient.TsBlock.DisableReporting)
  - [M DisableReportingFor ](#ApiClient.TsBlock.DisableReportingFor)
  - [M GetAbortCode ](#ApiClient.TsBlock.GetAbortCode)
  - [M GetAbortComment ](#ApiClient.TsBlock.GetAbortComment)
  - [M GetAbortCondition ](#ApiClient.TsBlock.GetAbortCondition)
  - [M GetActionColumnText ](#ApiClient.TsBlock.GetActionColumnText)
  - [M GetComment ](#ApiClient.TsBlock.GetComment)
  - [M GetCommentColumnText ](#ApiClient.TsBlock.GetCommentColumnText)
  - [M GetError ](#ApiClient.TsBlock.GetError)
  - [M GetIndex ](#ApiClient.TsBlock.GetIndex)
  - [M GetLineNo ](#ApiClient.TsBlock.GetLineNo)
  - [M GetParameterColumnText ](#ApiClient.TsBlock.GetParameterColumnText)
  - [M GetParent ](#ApiClient.TsBlock.GetParent)
  - [M GetReportDisablingResults ](#ApiClient.TsBlock.GetReportDisablingResults)
  - [M GetTags ](#ApiClient.TsBlock.GetTags)
  - [M GetTestManagementId ](#ApiClient.TsBlock.GetTestManagementId)
  - [M GetTestStepId ](#ApiClient.TsBlock.GetTestStepId)
  - [M GetTestSteps ](#ApiClient.TsBlock.GetTestSteps)
  - [M GetTranslatedActionColumnText ](#ApiClient.TsBlock.GetTranslatedActionColumnText)
  - [M GetTranslatedCommentText ](#ApiClient.TsBlock.GetTranslatedCommentText)
  - [M GetTranslatedParameterColumnText ](#ApiClient.TsBlock.GetTranslatedParameterColumnText)
  - [M GetTranslatedValueColumnText ](#ApiClient.TsBlock.GetTranslatedValueColumnText)
  - [M GetType ](#ApiClient.TsBlock.GetType)
  - [M GetValueColumnText ](#ApiClient.TsBlock.GetValueColumnText)
  - [M InsertTestStep ](#ApiClient.TsBlock.InsertTestStep)
  - [M IsBreakpoint ](#ApiClient.TsBlock.IsBreakpoint)
  - [M IsConditionalAbortEnabled ](#ApiClient.TsBlock.IsConditionalAbortEnabled)
  - [M IsConditionalEndEnabled ](#ApiClient.TsBlock.IsConditionalEndEnabled)
  - [M IsContainer ](#ApiClient.TsBlock.IsContainer)
  - [M IsEnabled ](#ApiClient.TsBlock.IsEnabled)
  - [M IsGeneratedByAgent ](#ApiClient.TsBlock.IsGeneratedByAgent)
  - [M IsInPostcondition ](#ApiClient.TsBlock.IsInPostcondition)
  - [M IsInPrecondition ](#ApiClient.TsBlock.IsInPrecondition)
  - [M IsOk ](#ApiClient.TsBlock.IsOk)
  - [M IsOverrideAbortInfoEnabled ](#ApiClient.TsBlock.IsOverrideAbortInfoEnabled)
  - [M IsReportingDisabled ](#ApiClient.TsBlock.IsReportingDisabled)
  - [M IsUserInteractionEnabled ](#ApiClient.TsBlock.IsUserInteractionEnabled)
  - [M IsVisible ](#ApiClient.TsBlock.IsVisible)
  - [M RemoveTag ](#ApiClient.TsBlock.RemoveTag)
  - [M RemoveTestStep ](#ApiClient.TsBlock.RemoveTestStep)
  - [M SetAbortCode ](#ApiClient.TsBlock.SetAbortCode)
  - [M SetAbortComment ](#ApiClient.TsBlock.SetAbortComment)
  - [M SetAbortCondition ](#ApiClient.TsBlock.SetAbortCondition)
  - [M SetActionColumnText ](#ApiClient.TsBlock.SetActionColumnText)
  - [M SetBreakpoint ](#ApiClient.TsBlock.SetBreakpoint)
  - [M SetComment ](#ApiClient.TsBlock.SetComment)
  - [M SetConditionalAbort ](#ApiClient.TsBlock.SetConditionalAbort)
  - [M SetConditionalEnd ](#ApiClient.TsBlock.SetConditionalEnd)
  - [M SetEnabled ](#ApiClient.TsBlock.SetEnabled)
  - [M SetOverrideAbortInfo ](#ApiClient.TsBlock.SetOverrideAbortInfo)
  - [M SetParameterColumnText ](#ApiClient.TsBlock.SetParameterColumnText)
  - [M SetTags ](#ApiClient.TsBlock.SetTags)
  - [M SetTestManagementId ](#ApiClient.TsBlock.SetTestManagementId)
  - [M SetTranslatedActionColumnText ](#ApiClient.TsBlock.SetTranslatedActionColumnText)
  - [M SetTranslatedCommentText ](#ApiClient.TsBlock.SetTranslatedCommentText)
  - [M SetTranslatedParameterColumnText ](#ApiClient.TsBlock.SetTranslatedParameterColumnText)
  - [M SetTranslatedValueColumnText ](#ApiClient.TsBlock.SetTranslatedValueColumnText)
  - [M SetUserInteraction ](#ApiClient.TsBlock.SetUserInteraction)
  - [M SetValueColumnText ](#ApiClient.TsBlock.SetValueColumnText)

# TsBlock[¶](#tsblock "Link to this heading")

*class* TsBlock[¶](#ApiClient.TsBlock "Link to this definition")  
Api- of the block structure test step.

Returned by

- [`TestStepApi.CreateTsBlock`](../TestStepApi.md#ApiClient.TestStepApi.CreateTsBlock "ApiClient.TestStepApi.CreateTsBlock (Python method) — Creates a block test step. Other test steps can be added to the block.")

AddTag(*[tag](#ApiClient.TsBlock.AddTag.tag "ApiClient.TsBlock.AddTag.tag (Python parameter) — The tag to be set")*)[¶](#ApiClient.TsBlock.AddTag "Link to this definition")  
Add a specific tag to this step.

Parameters:  tag : str[¶](#ApiClient.TsBlock.AddTag.tag "Permalink to this definition")  
The tag to be set

AppendTestStep(*[testStep](#ApiClient.TsBlock.AppendTestStep.testStep "ApiClient.TsBlock.AppendTestStep.testStep (Python parameter) — Test step to be added")*)[¶](#ApiClient.TsBlock.AppendTestStep "Link to this definition")  
Adds a test step at the end of the container.

Parameters:  testStep[¶](#ApiClient.TsBlock.AppendTestStep.testStep "Permalink to this definition")  
Test step to be added

Clone()[¶](#ApiClient.TsBlock.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`TsBlock`](#ApiClient.TsBlock "ApiClient.TsBlock (Python class) — Api- of the block structure test step.")

DeleteTranslatedActionColumnText(*[language](#ApiClient.TsBlock.DeleteTranslatedActionColumnText.language "ApiClient.TsBlock.DeleteTranslatedActionColumnText.language (Python parameter) — Language of the text ('en_US', 'de_DE', 'zh_CN')")*)[¶](#ApiClient.TsBlock.DeleteTranslatedActionColumnText "Link to this definition")  
Deletes the text value to be displayed in the action column of the test case editor in the given language.

Parameters:  language : str[¶](#ApiClient.TsBlock.DeleteTranslatedActionColumnText.language "Permalink to this definition")  
Language of the text (‘en_US’, ‘de_DE’, ‘zh_CN’)

DeleteTranslatedCommentText(*[language](#ApiClient.TsBlock.DeleteTranslatedCommentText.language "ApiClient.TsBlock.DeleteTranslatedCommentText.language (Python parameter) — Language of the text ('en_US', 'de_DE', 'zh_CN')")*)[¶](#ApiClient.TsBlock.DeleteTranslatedCommentText "Link to this definition")  
Deletes a comment for the test step in the given language.

Parameters:  language : str[¶](#ApiClient.TsBlock.DeleteTranslatedCommentText.language "Permalink to this definition")  
Language of the text (‘en_US’, ‘de_DE’, ‘zh_CN’)

DeleteTranslatedParameterColumnText(*[language](#ApiClient.TsBlock.DeleteTranslatedParameterColumnText.language "ApiClient.TsBlock.DeleteTranslatedParameterColumnText.language (Python parameter) — Language of the text ('en_US', 'de_DE', 'zh_CN')")*)[¶](#ApiClient.TsBlock.DeleteTranslatedParameterColumnText "Link to this definition")  
Deletes the text value to be displayed in the parameter column of the test case editor in the given language.

Parameters:  language : str[¶](#ApiClient.TsBlock.DeleteTranslatedParameterColumnText.language "Permalink to this definition")  
Language of the text (‘en_US’, ‘de_DE’, ‘zh_CN’)

DeleteTranslatedValueColumnText(*[language](#ApiClient.TsBlock.DeleteTranslatedValueColumnText.language "ApiClient.TsBlock.DeleteTranslatedValueColumnText.language (Python parameter) — Language of the text ('en_US', 'de_DE', 'zh_CN')")*)[¶](#ApiClient.TsBlock.DeleteTranslatedValueColumnText "Link to this definition")  
Deletes the text value to be displayed in the value column of the test case editor in the given language.

Parameters:  language : str[¶](#ApiClient.TsBlock.DeleteTranslatedValueColumnText.language "Permalink to this definition")  
Language of the text (‘en_US’, ‘de_DE’, ‘zh_CN’)

DisableReporting(*[disable](#ApiClient.TsBlock.DisableReporting.disable "ApiClient.TsBlock.DisableReporting.disable (Python parameter) — If True the result of this test step will not be reported (optional)")=`True`*)[¶](#ApiClient.TsBlock.DisableReporting "Link to this definition")  
Disables or enables the reporting this test step.

Parameters:  disable : boolean[¶](#ApiClient.TsBlock.DisableReporting.disable "Permalink to this definition")  
If True the result of this test step will not be reported (optional)

DisableReportingFor(*[results](#ApiClient.TsBlock.DisableReportingFor.results "ApiClient.TsBlock.DisableReportingFor.results (Python parameter) — List of results for which the test step will not be reported.")*)[¶](#ApiClient.TsBlock.DisableReportingFor "Link to this definition")  
Sets for which results reporting of the test step is disabled.

Parameters:  results : list[str][¶](#ApiClient.TsBlock.DisableReportingFor.results "Permalink to this definition")  
List of results for which the test step will not be reported. Valid results are: u’NONE’, u’SUCCESS’, u’INCONCLUSIVE’, u’FAILED’, u’ERROR’

GetAbortCode()[¶](#ApiClient.TsBlock.GetAbortCode "Link to this definition")  
Returns the abort code of the block.

Returns:  Abort code

Return type:  str

GetAbortComment()[¶](#ApiClient.TsBlock.GetAbortComment "Link to this definition")  
Returns the abort comment of the block.

Returns:  Abort comment

Return type:  str

GetAbortCondition()[¶](#ApiClient.TsBlock.GetAbortCondition "Link to this definition")  
Returns the condition under which the test case will be terminated or aborted.

Returns:  one of [‘ERROR’, ‘ERROR_OR_FAILED’, ‘ERROR_OR_FAILED_OR_INCONCLUSIVE’]

Return type:  str

GetActionColumnText()[¶](#ApiClient.TsBlock.GetActionColumnText "Link to this definition")  
Returns the text value of the “action” column in your current test case language.

Returns:  Action column text

Return type:  str

GetComment()[¶](#ApiClient.TsBlock.GetComment "Link to this definition")  
Returns the comment of the test step in the current test case language.

Returns:  Comment text as shown in the comment tab

Return type:  str

GetCommentColumnText()[¶](#ApiClient.TsBlock.GetCommentColumnText "Link to this definition")  
Returns the text value of the “comment” column.

Returns:  Comment column text

Return type:  str

GetError()[¶](#ApiClient.TsBlock.GetError "Link to this definition")  
Returns a list of errors. Note that the error messages depend on the program language ecu.test is set to. Because of that we do not recommend to check against exact error messages, unless you are certain about the respective program language.

Returns:  List of errors

Return type:  list[str]

GetIndex()[¶](#ApiClient.TsBlock.GetIndex "Link to this definition")  
Returns the zero based index in the parent.

Returns:  Zero based index

Return type:  integer

GetLineNo()[¶](#ApiClient.TsBlock.GetLineNo "Link to this definition")  
Returns the test steps line number within its test case.

Returns:  Line number

Return type:  int

GetParameterColumnText()[¶](#ApiClient.TsBlock.GetParameterColumnText "Link to this definition")  
Returns the text value of the “parameter” column.

Returns:  Parameter column text

Return type:  str

GetParent()[¶](#ApiClient.TsBlock.GetParent "Link to this definition")  
Returns the parent test step.

Returns:  The parent test step or None if it is a top level test step.

Return type:  [`TestStep`](../PackageApi/TestStep.md#ApiClient.TestStep "ApiClient.TestStep (Python class) — Add a specific tag to this step.")

GetReportDisablingResults()[¶](#ApiClient.TsBlock.GetReportDisablingResults "Link to this definition")  
Returns for which results reporting of the test step is disabled.

Returns:  List of results for which the test step will not be reported

Return type:  list[str]

GetTags()[¶](#ApiClient.TsBlock.GetTags "Link to this definition")  
Returns the tags set for this step.

Returns:  A (sorted) list of tags

Return type:  list[str]

GetTestManagementId()[¶](#ApiClient.TsBlock.GetTestManagementId "Link to this definition")  
Returns the test management id of the test step.

Returns:  Test step id.

Return type:  str

GetTestStepId()[¶](#ApiClient.TsBlock.GetTestStepId "Link to this definition")  
Returns the test step id.

Returns:  test step id

Return type:  str

GetTestSteps(*[skipDisabledSteps](#ApiClient.TsBlock.GetTestSteps.skipDisabledSteps "ApiClient.TsBlock.GetTestSteps.skipDisabledSteps (Python parameter) — Defines whether disabled test steps should be excluded.")=`True`*, *[recursive](#ApiClient.TsBlock.GetTestSteps.recursive "ApiClient.TsBlock.GetTestSteps.recursive (Python parameter) — Specifies whether only the direct children of the test step or recursively all test steps from the complete test step tree should be returned.")=`False`*, *[whiteList](#ApiClient.TsBlock.GetTestSteps.whiteList "ApiClient.TsBlock.GetTestSteps.whiteList (Python parameter) — If specified, only those test steps whose class name is on this list are returned.")=`None`*, *[blackList](#ApiClient.TsBlock.GetTestSteps.blackList "ApiClient.TsBlock.GetTestSteps.blackList (Python parameter) — If specified, only those test steps whose class name is not on this list are returned.")=`None`*)[¶](#ApiClient.TsBlock.GetTestSteps "Link to this definition")  
Returns the children of the test step.

Parameters:  skipDisabledSteps : boolean[¶](#ApiClient.TsBlock.GetTestSteps.skipDisabledSteps "Permalink to this definition")  
Defines whether disabled test steps should be excluded.

recursive : boolean[¶](#ApiClient.TsBlock.GetTestSteps.recursive "Permalink to this definition")  
Specifies whether only the direct children of the test step or recursively all test steps from the complete test step tree should be returned.

whiteList : list[str][¶](#ApiClient.TsBlock.GetTestSteps.whiteList "Permalink to this definition")  
If specified, only those test steps whose class name is on this list are returned.

blackList : list[str][¶](#ApiClient.TsBlock.GetTestSteps.blackList "Permalink to this definition")  
If specified, only those test steps whose class name is not on this list are returned.

Returns:  List with all children test steps

Return type:  list[[`TestStep`](../PackageApi/TestStep.md#ApiClient.TestStep "ApiClient.TestStep (Python class) — Add a specific tag to this step.")]

GetTranslatedActionColumnText(*[language](#ApiClient.TsBlock.GetTranslatedActionColumnText.language "ApiClient.TsBlock.GetTranslatedActionColumnText.language (Python parameter) — Language of the requested text ('en_US', 'de_DE', 'zh_CN')")*)[¶](#ApiClient.TsBlock.GetTranslatedActionColumnText "Link to this definition")  
Returns the text value of the “action” column in the given language.

Parameters:  language : str[¶](#ApiClient.TsBlock.GetTranslatedActionColumnText.language "Permalink to this definition")  
Language of the requested text (‘en_US’, ‘de_DE’, ‘zh_CN’)

Returns:  Action column text

Return type:  str

GetTranslatedCommentText(*[language](#ApiClient.TsBlock.GetTranslatedCommentText.language "ApiClient.TsBlock.GetTranslatedCommentText.language (Python parameter) — Language of the requested text ('en_US', 'de_DE', 'zh_CN')")*)[¶](#ApiClient.TsBlock.GetTranslatedCommentText "Link to this definition")  
Returns the text value of the “comment” column in the given language.

Parameters:  language : str[¶](#ApiClient.TsBlock.GetTranslatedCommentText.language "Permalink to this definition")  
Language of the requested text (‘en_US’, ‘de_DE’, ‘zh_CN’)

Returns:  Comment column text

Return type:  str

GetTranslatedParameterColumnText(*[language](#ApiClient.TsBlock.GetTranslatedParameterColumnText.language "ApiClient.TsBlock.GetTranslatedParameterColumnText.language (Python parameter) — Language of the requested text ('en_US', 'de_DE', 'zh_CN')")*)[¶](#ApiClient.TsBlock.GetTranslatedParameterColumnText "Link to this definition")  
Returns the text value of the “parameter” column in the given language.

Parameters:  language : str[¶](#ApiClient.TsBlock.GetTranslatedParameterColumnText.language "Permalink to this definition")  
Language of the requested text (‘en_US’, ‘de_DE’, ‘zh_CN’)

Returns:  Value column text

Return type:  str

GetTranslatedValueColumnText(*[language](#ApiClient.TsBlock.GetTranslatedValueColumnText.language "ApiClient.TsBlock.GetTranslatedValueColumnText.language (Python parameter) — Language of the requested text ('en_US', 'de_DE', 'zh_CN')")*)[¶](#ApiClient.TsBlock.GetTranslatedValueColumnText "Link to this definition")  
Returns the text value of the “value” column in the given language.

Parameters:  language : str[¶](#ApiClient.TsBlock.GetTranslatedValueColumnText.language "Permalink to this definition")  
Language of the requested text (‘en_US’, ‘de_DE’, ‘zh_CN’)

Returns:  Value column text

Return type:  str

GetType()[¶](#ApiClient.TsBlock.GetType "Link to this definition")  
Returns the type (class name) of the test step, e.g.

- “TsPreconditionBlock”

- “TsWait”

- “TsIfThenElse”

- “TsSwitchCase”

- “TsCaseNode”

Returns:  Type (class name) of the test step

Return type:  str

GetValueColumnText()[¶](#ApiClient.TsBlock.GetValueColumnText "Link to this definition")  
Returns the text value of the “value” column in your current test case language.

Returns:  Value column text

Return type:  str

InsertTestStep(*[testStep](#ApiClient.TsBlock.InsertTestStep.testStep "ApiClient.TsBlock.InsertTestStep.testStep (Python parameter) — Test step to be added")*, *[position](#ApiClient.TsBlock.InsertTestStep.position "ApiClient.TsBlock.InsertTestStep.position (Python parameter) — Target index of child beginning with 0")*)[¶](#ApiClient.TsBlock.InsertTestStep "Link to this definition")  
Adds a test step at a certain position of the container.

Parameters:  testStep[¶](#ApiClient.TsBlock.InsertTestStep.testStep "Permalink to this definition")  
Test step to be added

position : integer[¶](#ApiClient.TsBlock.InsertTestStep.position "Permalink to this definition")  
Target index of child beginning with 0

IsBreakpoint()[¶](#ApiClient.TsBlock.IsBreakpoint "Link to this definition")  
Checks whether the test step is a break point.

Returns:  True if test step is a break point, else False

Return type:  boolean

IsConditionalAbortEnabled()[¶](#ApiClient.TsBlock.IsConditionalAbortEnabled "Link to this definition")  
Returns whether the block will abort the test case if the condition is met.

Returns:  Conditional abort enabled

Return type:  boolean

IsConditionalEndEnabled()[¶](#ApiClient.TsBlock.IsConditionalEndEnabled "Link to this definition")  
Returns whether the block will terminate the test case if the condition is met.

Returns:  Conditional end enabled

Return type:  boolean

IsContainer()[¶](#ApiClient.TsBlock.IsContainer "Link to this definition")  
Returns True, if the test step supports calling GetChildren as well as manipulating the structure of its children. (e. g. via inserting or deleting sub test steps).

Returns:  True if it can contain test steps, else False

Return type:  boolean

IsEnabled()[¶](#ApiClient.TsBlock.IsEnabled "Link to this definition")  
Returns the state of the test step.

Returns:  True if test step is enabled, otherwise False

Return type:  bool

IsGeneratedByAgent()[¶](#ApiClient.TsBlock.IsGeneratedByAgent "Link to this definition")  
Returns whether the test steps in this block were generated by the ecu.test agent.

Returns:  True if generated by ecu.test agent, False otherwise

Return type:  bool

IsInPostcondition()[¶](#ApiClient.TsBlock.IsInPostcondition "Link to this definition")  
Returns True if the test step is located in a postcondition

Returns:  True if the test step is located in a postcondition, else Flase

Return type:  bool

IsInPrecondition()[¶](#ApiClient.TsBlock.IsInPrecondition "Link to this definition")  
Returns True if the test step is located in a precondition

Returns:  True if the test step is located in a precondition, else False

Return type:  bool

IsOk()[¶](#ApiClient.TsBlock.IsOk "Link to this definition")  
Returns the internal state of correctness of the test step.

Returns:  True if no problems were found, else False

Return type:  boolean

IsOverrideAbortInfoEnabled()[¶](#ApiClient.TsBlock.IsOverrideAbortInfoEnabled "Link to this definition")  
Returns if the block override abort information of underlying test steps.

Returns:  Conditional abort enabled

Return type:  boolean

IsReportingDisabled()[¶](#ApiClient.TsBlock.IsReportingDisabled "Link to this definition")  
Returns whether reporting of this test step is disabled.

Returns:  True if reporting is disabled

Return type:  boolean

IsUserInteractionEnabled()[¶](#ApiClient.TsBlock.IsUserInteractionEnabled "Link to this definition")  
Returns if the block is set to be a user interaction.

Returns:  User interaction status

Return type:  boolean

IsVisible()[¶](#ApiClient.TsBlock.IsVisible "Link to this definition")  
Checks whether the test step is visible. This depends on the test step itself or a parent test step being disabled.

Returns:  True if test step is visible, else False

Return type:  boolean

RemoveTag(*[tag](#ApiClient.TsBlock.RemoveTag.tag "ApiClient.TsBlock.RemoveTag.tag (Python parameter) — The tag to be removed")*)[¶](#ApiClient.TsBlock.RemoveTag "Link to this definition")  
Remove a specific tag from this step.

Parameters:  tag : str[¶](#ApiClient.TsBlock.RemoveTag.tag "Permalink to this definition")  
The tag to be removed

RemoveTestStep(*[testStep](#ApiClient.TsBlock.RemoveTestStep.testStep "ApiClient.TsBlock.RemoveTestStep.testStep (Python parameter) — Test step to be removed")*)[¶](#ApiClient.TsBlock.RemoveTestStep "Link to this definition")  
Removes a test step from the container.

Parameters:  testStep[¶](#ApiClient.TsBlock.RemoveTestStep.testStep "Permalink to this definition")  
Test step to be removed

Raises:  
ApiError:

- When the test step is not a direct child of the container

- When the test step is not editable

SetAbortCode(*[code](#ApiClient.TsBlock.SetAbortCode.code "ApiClient.TsBlock.SetAbortCode.code (Python parameter) — Abort code")*)[¶](#ApiClient.TsBlock.SetAbortCode "Link to this definition")  
Sets the abort code of the block.

Parameters:  code : str[¶](#ApiClient.TsBlock.SetAbortCode.code "Permalink to this definition")  
Abort code

SetAbortComment(*[comment](#ApiClient.TsBlock.SetAbortComment.comment "ApiClient.TsBlock.SetAbortComment.comment (Python parameter) — Abort comment")*)[¶](#ApiClient.TsBlock.SetAbortComment "Link to this definition")  
Sets the abort comment of the block.

Parameters:  comment : str[¶](#ApiClient.TsBlock.SetAbortComment.comment "Permalink to this definition")  
Abort comment

SetAbortCondition(*[condition](#ApiClient.TsBlock.SetAbortCondition.condition "ApiClient.TsBlock.SetAbortCondition.condition (Python parameter) — Abort condition")*)[¶](#ApiClient.TsBlock.SetAbortCondition "Link to this definition")  
Sets the condition under which the test case will be terminated or aborted. Must be one of [‘ERROR’, ‘ERROR_OR_FAILED’, ‘ERROR_OR_FAILED_OR_INCONCLUSIVE’], otherwise the command raises an error.

Parameters:  condition : str[¶](#ApiClient.TsBlock.SetAbortCondition.condition "Permalink to this definition")  
Abort condition

SetActionColumnText(*[text](#ApiClient.TsBlock.SetActionColumnText.text "ApiClient.TsBlock.SetActionColumnText.text (Python parameter) — Text to be displayed")*)[¶](#ApiClient.TsBlock.SetActionColumnText "Link to this definition")  
Sets the text value to be displayed in the action column of the test case editor in your current test case language.

Parameters:  text : str[¶](#ApiClient.TsBlock.SetActionColumnText.text "Permalink to this definition")  
Text to be displayed

SetBreakpoint(*[enable](#ApiClient.TsBlock.SetBreakpoint.enable "ApiClient.TsBlock.SetBreakpoint.enable (Python parameter) — True if test step is a break point, else False")*)[¶](#ApiClient.TsBlock.SetBreakpoint "Link to this definition")  
Sets or unsets the test step to act as a break point.

Parameters:  enable : boolean[¶](#ApiClient.TsBlock.SetBreakpoint.enable "Permalink to this definition")  
True if test step is a break point, else False

SetComment(*[comment](#ApiClient.TsBlock.SetComment.comment "ApiClient.TsBlock.SetComment.comment (Python parameter) — Text to be displayed in the comment tab")*)[¶](#ApiClient.TsBlock.SetComment "Link to this definition")  
Sets a comment for the test step in the current test case language.

Parameters:  comment : str[¶](#ApiClient.TsBlock.SetComment.comment "Permalink to this definition")  
Text to be displayed in the comment tab

SetConditionalAbort(*[abort](#ApiClient.TsBlock.SetConditionalAbort.abort "ApiClient.TsBlock.SetConditionalAbort.abort (Python parameter) — Conditional abort status")=`True`*)[¶](#ApiClient.TsBlock.SetConditionalAbort "Link to this definition")  
Sets whether the block will abort the test case if the condition is met.

Parameters:  abort : boolean[¶](#ApiClient.TsBlock.SetConditionalAbort.abort "Permalink to this definition")  
Conditional abort status

SetConditionalEnd(*[end](#ApiClient.TsBlock.SetConditionalEnd.end "ApiClient.TsBlock.SetConditionalEnd.end (Python parameter) — Conditional end status")=`True`*)[¶](#ApiClient.TsBlock.SetConditionalEnd "Link to this definition")  
Sets whether the block will terminate the test case if the condition is met.

Parameters:  end : boolean[¶](#ApiClient.TsBlock.SetConditionalEnd.end "Permalink to this definition")  
Conditional end status

SetEnabled(*[state](#ApiClient.TsBlock.SetEnabled.state "ApiClient.TsBlock.SetEnabled.state (Python parameter) — True (Default) to enable, False to disable the test step.")=`True`*)[¶](#ApiClient.TsBlock.SetEnabled "Link to this definition")  
Enable or disable the test step.

Parameters:  state : bool[¶](#ApiClient.TsBlock.SetEnabled.state "Permalink to this definition")  
True (Default) to enable, False to disable the test step.

SetOverrideAbortInfo(*[override](#ApiClient.TsBlock.SetOverrideAbortInfo.override "ApiClient.TsBlock.SetOverrideAbortInfo.override (Python parameter) — Override abort information status")*)[¶](#ApiClient.TsBlock.SetOverrideAbortInfo "Link to this definition")  
Sets the override abort information status.

Parameters:  override : boolean[¶](#ApiClient.TsBlock.SetOverrideAbortInfo.override "Permalink to this definition")  
Override abort information status

SetParameterColumnText(*[text](#ApiClient.TsBlock.SetParameterColumnText.text "ApiClient.TsBlock.SetParameterColumnText.text (Python parameter) — Text to be displayed")*)[¶](#ApiClient.TsBlock.SetParameterColumnText "Link to this definition")  
Sets the text value to be displayed in the parameter column of the test case editor.

Parameters:  text : str[¶](#ApiClient.TsBlock.SetParameterColumnText.text "Permalink to this definition")  
Text to be displayed

SetTags(*[tags](#ApiClient.TsBlock.SetTags.tags "ApiClient.TsBlock.SetTags.tags (Python parameter) — The list of tags")*)[¶](#ApiClient.TsBlock.SetTags "Link to this definition")  
Set the list of tags for this step. The list of tags will be sorted and stored.

Parameters:  tags : list[str][¶](#ApiClient.TsBlock.SetTags.tags "Permalink to this definition")  
The list of tags

SetTestManagementId(*[testManagementId](#ApiClient.TsBlock.SetTestManagementId.testManagementId "ApiClient.TsBlock.SetTestManagementId.testManagementId (Python parameter) — Test management id of the test step")*)[¶](#ApiClient.TsBlock.SetTestManagementId "Link to this definition")  
Sets the test management id of the test step.

Parameters:  testManagementId : str[¶](#ApiClient.TsBlock.SetTestManagementId.testManagementId "Permalink to this definition")  
Test management id of the test step

SetTranslatedActionColumnText(*[text](#ApiClient.TsBlock.SetTranslatedActionColumnText.text "ApiClient.TsBlock.SetTranslatedActionColumnText.text (Python parameter) — Text to be displayed")*, *[language](#ApiClient.TsBlock.SetTranslatedActionColumnText.language "ApiClient.TsBlock.SetTranslatedActionColumnText.language (Python parameter) — Language of the text ('en_US', 'de_DE', 'zh_CN')")*)[¶](#ApiClient.TsBlock.SetTranslatedActionColumnText "Link to this definition")  
Sets the text value for the action column of the test case editor in the given language.

Parameters:  text : str[¶](#ApiClient.TsBlock.SetTranslatedActionColumnText.text "Permalink to this definition")  
Text to be displayed

language : str[¶](#ApiClient.TsBlock.SetTranslatedActionColumnText.language "Permalink to this definition")  
Language of the text (‘en_US’, ‘de_DE’, ‘zh_CN’)

SetTranslatedCommentText(*[comment](#ApiClient.TsBlock.SetTranslatedCommentText.comment "ApiClient.TsBlock.SetTranslatedCommentText.comment (Python parameter) — Text to be displayed")*, *[language](#ApiClient.TsBlock.SetTranslatedCommentText.language "ApiClient.TsBlock.SetTranslatedCommentText.language (Python parameter) — Language of the text ('en_US', 'de_DE', 'zh_CN')")*)[¶](#ApiClient.TsBlock.SetTranslatedCommentText "Link to this definition")  
Sets a comment for the test step in the given language.

Parameters:  comment : str[¶](#ApiClient.TsBlock.SetTranslatedCommentText.comment "Permalink to this definition")  
Text to be displayed

language : str[¶](#ApiClient.TsBlock.SetTranslatedCommentText.language "Permalink to this definition")  
Language of the text (‘en_US’, ‘de_DE’, ‘zh_CN’)

SetTranslatedParameterColumnText(*[text](#ApiClient.TsBlock.SetTranslatedParameterColumnText.text "ApiClient.TsBlock.SetTranslatedParameterColumnText.text (Python parameter) — Text to be displayed")*, *[language](#ApiClient.TsBlock.SetTranslatedParameterColumnText.language "ApiClient.TsBlock.SetTranslatedParameterColumnText.language (Python parameter) — Language of the text ('en_US', 'de_DE', 'zh_CN')")*)[¶](#ApiClient.TsBlock.SetTranslatedParameterColumnText "Link to this definition")  
Sets the text value to be displayed in the parameter column of the test case editor in the given language.

Parameters:  text : str[¶](#ApiClient.TsBlock.SetTranslatedParameterColumnText.text "Permalink to this definition")  
Text to be displayed

language : str[¶](#ApiClient.TsBlock.SetTranslatedParameterColumnText.language "Permalink to this definition")  
Language of the text (‘en_US’, ‘de_DE’, ‘zh_CN’)

SetTranslatedValueColumnText(*[text](#ApiClient.TsBlock.SetTranslatedValueColumnText.text "ApiClient.TsBlock.SetTranslatedValueColumnText.text (Python parameter) — Text to be displayed")*, *[language](#ApiClient.TsBlock.SetTranslatedValueColumnText.language "ApiClient.TsBlock.SetTranslatedValueColumnText.language (Python parameter) — Language of the text ('en_US', 'de_DE', 'zh_CN')")*)[¶](#ApiClient.TsBlock.SetTranslatedValueColumnText "Link to this definition")  
Sets the text value to be displayed in the value column of the test case editor in the given language.

Parameters:  text : str[¶](#ApiClient.TsBlock.SetTranslatedValueColumnText.text "Permalink to this definition")  
Text to be displayed

language : str[¶](#ApiClient.TsBlock.SetTranslatedValueColumnText.language "Permalink to this definition")  
Language of the text (‘en_US’, ‘de_DE’, ‘zh_CN’)

SetUserInteraction(*[interactive](#ApiClient.TsBlock.SetUserInteraction.interactive "ApiClient.TsBlock.SetUserInteraction.interactive (Python parameter) — User interaction status")=`True`*)[¶](#ApiClient.TsBlock.SetUserInteraction "Link to this definition")  
Sets if the block is user interactive.

Parameters:  interactive : boolean[¶](#ApiClient.TsBlock.SetUserInteraction.interactive "Permalink to this definition")  
User interaction status

SetValueColumnText(*[text](#ApiClient.TsBlock.SetValueColumnText.text "ApiClient.TsBlock.SetValueColumnText.text (Python parameter) — Text to be displayed")*)[¶](#ApiClient.TsBlock.SetValueColumnText "Link to this definition")  
Sets the text value to be displayed in the value column of the test case editor in your current test case language.

Parameters:  text : str[¶](#ApiClient.TsBlock.SetValueColumnText.text "Permalink to this definition")  
Text to be displayed

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
