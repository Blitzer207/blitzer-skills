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

API for Packages

[ AnalysisPackage ](AnalysisPackage.md)

[ Argument ](Argument.md)

[ Attributes ](Attributes.md)

[ AutoAssignRecordingGroup ](AutoAssignRecordingGroup.md)

[ AutoAssignSignalGroup ](AutoAssignSignalGroup.md)

[ LocalMapping ](LocalMapping.md)

[ MappingTestStep ](MappingTestStep.md)

[ MappingTestStepContainer ](MappingTestStepContainer.md)

[ Package ](Package.md)

[ RecordingConfig ](RecordingConfig.md)

[ Return ](Return.md)

[ TestStep ](TestStep.md)

[ TestStepContainer ](TestStepContainer.md)

[ TestStepRWBase ](TestStepRWBase.md)

[ Testcase ](Testcase.md)

TsAXSCall [ TsAXSCall ](#)

TsAXSCall

- [C TsAXSCall ](#ApiClient.TsAXSCall)
  - [M AddTag ](#ApiClient.TsAXSCall.AddTag)
  - [M Clone ](#ApiClient.TsAXSCall.Clone)
  - [M DeactivateFailedComment ](#ApiClient.TsAXSCall.DeactivateFailedComment)
  - [M DeactivateSuccessComment ](#ApiClient.TsAXSCall.DeactivateSuccessComment)
  - [M DeactivateTimeOption ](#ApiClient.TsAXSCall.DeactivateTimeOption)
  - [M DeleteTranslatedCommentText ](#ApiClient.TsAXSCall.DeleteTranslatedCommentText)
  - [M GetActionColumnText ](#ApiClient.TsAXSCall.GetActionColumnText)
  - [M GetActiveTimeOptionType ](#ApiClient.TsAXSCall.GetActiveTimeOptionType)
  - [M GetArgument ](#ApiClient.TsAXSCall.GetArgument)
  - [M GetComment ](#ApiClient.TsAXSCall.GetComment)
  - [M GetCommentColumnText ](#ApiClient.TsAXSCall.GetCommentColumnText)
  - [M GetError ](#ApiClient.TsAXSCall.GetError)
  - [M GetFailedComment ](#ApiClient.TsAXSCall.GetFailedComment)
  - [M GetIndex ](#ApiClient.TsAXSCall.GetIndex)
  - [M GetLineNo ](#ApiClient.TsAXSCall.GetLineNo)
  - [M GetMinimumDuration ](#ApiClient.TsAXSCall.GetMinimumDuration)
  - [M GetMinimumDurationUnit ](#ApiClient.TsAXSCall.GetMinimumDurationUnit)
  - [M GetParameterColumnText ](#ApiClient.TsAXSCall.GetParameterColumnText)
  - [M GetParent ](#ApiClient.TsAXSCall.GetParent)
  - [M GetPollingCycle ](#ApiClient.TsAXSCall.GetPollingCycle)
  - [M GetPollingCycleUnit ](#ApiClient.TsAXSCall.GetPollingCycleUnit)
  - [M GetReturn ](#ApiClient.TsAXSCall.GetReturn)
  - [M GetSuccessComment ](#ApiClient.TsAXSCall.GetSuccessComment)
  - [M GetTags ](#ApiClient.TsAXSCall.GetTags)
  - [M GetTestManagementId ](#ApiClient.TsAXSCall.GetTestManagementId)
  - [M GetTestStepId ](#ApiClient.TsAXSCall.GetTestStepId)
  - [M GetTimeout ](#ApiClient.TsAXSCall.GetTimeout)
  - [M GetTimeoutUnit ](#ApiClient.TsAXSCall.GetTimeoutUnit)
  - [M GetTranslatedCommentText ](#ApiClient.TsAXSCall.GetTranslatedCommentText)
  - [M GetType ](#ApiClient.TsAXSCall.GetType)
  - [M GetValueColumnText ](#ApiClient.TsAXSCall.GetValueColumnText)
  - [M IsBreakpoint ](#ApiClient.TsAXSCall.IsBreakpoint)
  - [M IsContainer ](#ApiClient.TsAXSCall.IsContainer)
  - [M IsEnabled ](#ApiClient.TsAXSCall.IsEnabled)
  - [M IsInPostcondition ](#ApiClient.TsAXSCall.IsInPostcondition)
  - [M IsInPrecondition ](#ApiClient.TsAXSCall.IsInPrecondition)
  - [M IsOk ](#ApiClient.TsAXSCall.IsOk)
  - [M IsVisible ](#ApiClient.TsAXSCall.IsVisible)
  - [M RemoveArgument ](#ApiClient.TsAXSCall.RemoveArgument)
  - [M RemoveReturn ](#ApiClient.TsAXSCall.RemoveReturn)
  - [M RemoveTag ](#ApiClient.TsAXSCall.RemoveTag)
  - [M SetBreakpoint ](#ApiClient.TsAXSCall.SetBreakpoint)
  - [M SetComment ](#ApiClient.TsAXSCall.SetComment)
  - [M SetEnabled ](#ApiClient.TsAXSCall.SetEnabled)
  - [M SetFailedComment ](#ApiClient.TsAXSCall.SetFailedComment)
  - [M SetSuccessComment ](#ApiClient.TsAXSCall.SetSuccessComment)
  - [M SetTags ](#ApiClient.TsAXSCall.SetTags)
  - [M SetTestManagementId ](#ApiClient.TsAXSCall.SetTestManagementId)
  - [M SetTimeOptionOnlySynchronization ](#ApiClient.TsAXSCall.SetTimeOptionOnlySynchronization)
  - [M SetTimeOptionPollingCycleMultiplier ](#ApiClient.TsAXSCall.SetTimeOptionPollingCycleMultiplier)
  - [M SetTimeOptionTrueForAtLeast ](#ApiClient.TsAXSCall.SetTimeOptionTrueForAtLeast)
  - [M SetTimeOptionTrueForAtLeastWithin ](#ApiClient.TsAXSCall.SetTimeOptionTrueForAtLeastWithin)
  - [M SetTimeOptionWaitUntilTrue ](#ApiClient.TsAXSCall.SetTimeOptionWaitUntilTrue)
  - [M SetTranslatedCommentText ](#ApiClient.TsAXSCall.SetTranslatedCommentText)

[ TsBlockBase ](TsBlockBase.md)

[ TsBusMonitoring ](TsBusMonitoring.md)

[ TsCaseNodeBase ](TsCaseNodeBase.md)

[ TsSignalGroupOperation ](TsSignalGroupOperation.md)

[ TsSwitchBase ](TsSwitchBase.md)

[ TsUserInterface ](TsUserInterface.md)

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

TsAXSCall

- [C TsAXSCall ](#ApiClient.TsAXSCall)
  - [M AddTag ](#ApiClient.TsAXSCall.AddTag)
  - [M Clone ](#ApiClient.TsAXSCall.Clone)
  - [M DeactivateFailedComment ](#ApiClient.TsAXSCall.DeactivateFailedComment)
  - [M DeactivateSuccessComment ](#ApiClient.TsAXSCall.DeactivateSuccessComment)
  - [M DeactivateTimeOption ](#ApiClient.TsAXSCall.DeactivateTimeOption)
  - [M DeleteTranslatedCommentText ](#ApiClient.TsAXSCall.DeleteTranslatedCommentText)
  - [M GetActionColumnText ](#ApiClient.TsAXSCall.GetActionColumnText)
  - [M GetActiveTimeOptionType ](#ApiClient.TsAXSCall.GetActiveTimeOptionType)
  - [M GetArgument ](#ApiClient.TsAXSCall.GetArgument)
  - [M GetComment ](#ApiClient.TsAXSCall.GetComment)
  - [M GetCommentColumnText ](#ApiClient.TsAXSCall.GetCommentColumnText)
  - [M GetError ](#ApiClient.TsAXSCall.GetError)
  - [M GetFailedComment ](#ApiClient.TsAXSCall.GetFailedComment)
  - [M GetIndex ](#ApiClient.TsAXSCall.GetIndex)
  - [M GetLineNo ](#ApiClient.TsAXSCall.GetLineNo)
  - [M GetMinimumDuration ](#ApiClient.TsAXSCall.GetMinimumDuration)
  - [M GetMinimumDurationUnit ](#ApiClient.TsAXSCall.GetMinimumDurationUnit)
  - [M GetParameterColumnText ](#ApiClient.TsAXSCall.GetParameterColumnText)
  - [M GetParent ](#ApiClient.TsAXSCall.GetParent)
  - [M GetPollingCycle ](#ApiClient.TsAXSCall.GetPollingCycle)
  - [M GetPollingCycleUnit ](#ApiClient.TsAXSCall.GetPollingCycleUnit)
  - [M GetReturn ](#ApiClient.TsAXSCall.GetReturn)
  - [M GetSuccessComment ](#ApiClient.TsAXSCall.GetSuccessComment)
  - [M GetTags ](#ApiClient.TsAXSCall.GetTags)
  - [M GetTestManagementId ](#ApiClient.TsAXSCall.GetTestManagementId)
  - [M GetTestStepId ](#ApiClient.TsAXSCall.GetTestStepId)
  - [M GetTimeout ](#ApiClient.TsAXSCall.GetTimeout)
  - [M GetTimeoutUnit ](#ApiClient.TsAXSCall.GetTimeoutUnit)
  - [M GetTranslatedCommentText ](#ApiClient.TsAXSCall.GetTranslatedCommentText)
  - [M GetType ](#ApiClient.TsAXSCall.GetType)
  - [M GetValueColumnText ](#ApiClient.TsAXSCall.GetValueColumnText)
  - [M IsBreakpoint ](#ApiClient.TsAXSCall.IsBreakpoint)
  - [M IsContainer ](#ApiClient.TsAXSCall.IsContainer)
  - [M IsEnabled ](#ApiClient.TsAXSCall.IsEnabled)
  - [M IsInPostcondition ](#ApiClient.TsAXSCall.IsInPostcondition)
  - [M IsInPrecondition ](#ApiClient.TsAXSCall.IsInPrecondition)
  - [M IsOk ](#ApiClient.TsAXSCall.IsOk)
  - [M IsVisible ](#ApiClient.TsAXSCall.IsVisible)
  - [M RemoveArgument ](#ApiClient.TsAXSCall.RemoveArgument)
  - [M RemoveReturn ](#ApiClient.TsAXSCall.RemoveReturn)
  - [M RemoveTag ](#ApiClient.TsAXSCall.RemoveTag)
  - [M SetBreakpoint ](#ApiClient.TsAXSCall.SetBreakpoint)
  - [M SetComment ](#ApiClient.TsAXSCall.SetComment)
  - [M SetEnabled ](#ApiClient.TsAXSCall.SetEnabled)
  - [M SetFailedComment ](#ApiClient.TsAXSCall.SetFailedComment)
  - [M SetSuccessComment ](#ApiClient.TsAXSCall.SetSuccessComment)
  - [M SetTags ](#ApiClient.TsAXSCall.SetTags)
  - [M SetTestManagementId ](#ApiClient.TsAXSCall.SetTestManagementId)
  - [M SetTimeOptionOnlySynchronization ](#ApiClient.TsAXSCall.SetTimeOptionOnlySynchronization)
  - [M SetTimeOptionPollingCycleMultiplier ](#ApiClient.TsAXSCall.SetTimeOptionPollingCycleMultiplier)
  - [M SetTimeOptionTrueForAtLeast ](#ApiClient.TsAXSCall.SetTimeOptionTrueForAtLeast)
  - [M SetTimeOptionTrueForAtLeastWithin ](#ApiClient.TsAXSCall.SetTimeOptionTrueForAtLeastWithin)
  - [M SetTimeOptionWaitUntilTrue ](#ApiClient.TsAXSCall.SetTimeOptionWaitUntilTrue)
  - [M SetTranslatedCommentText ](#ApiClient.TsAXSCall.SetTranslatedCommentText)

# TsAXSCall[¶](#tsaxscall "Link to this heading")

*class* TsAXSCall[¶](#ApiClient.TsAXSCall "Link to this definition")  
AddTag(*[tag](#ApiClient.TsAXSCall.AddTag.tag "ApiClient.TsAXSCall.AddTag.tag (Python parameter) — The tag to be set")*)[¶](#ApiClient.TsAXSCall.AddTag "Link to this definition")  
Add a specific tag to this step.

Parameters:  tag : str[¶](#ApiClient.TsAXSCall.AddTag.tag "Permalink to this definition")  
The tag to be set

Clone()[¶](#ApiClient.TsAXSCall.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`TsAXSCall`](#ApiClient.TsAXSCall "ApiClient.TsAXSCall (Python class) — Add a specific tag to this step.")

DeactivateFailedComment()[¶](#ApiClient.TsAXSCall.DeactivateFailedComment "Link to this definition")  
Deactivates the expectation for the failed comment so that the result will not be evaluated.

DeactivateSuccessComment()[¶](#ApiClient.TsAXSCall.DeactivateSuccessComment "Link to this definition")  
Deactivates the expectation for the success comment so that the result will not be evaluated.

DeactivateTimeOption()[¶](#ApiClient.TsAXSCall.DeactivateTimeOption "Link to this definition")  
Deactivates any time option set on the test step. This is equivalent to selecting the option “none” in the test step’s time options menu.

DeleteTranslatedCommentText(*[language](#ApiClient.TsAXSCall.DeleteTranslatedCommentText.language "ApiClient.TsAXSCall.DeleteTranslatedCommentText.language (Python parameter) — Language of the text ('en_US', 'de_DE', 'zh_CN')")*)[¶](#ApiClient.TsAXSCall.DeleteTranslatedCommentText "Link to this definition")  
Deletes a comment for the test step in the given language.

Parameters:  language : str[¶](#ApiClient.TsAXSCall.DeleteTranslatedCommentText.language "Permalink to this definition")  
Language of the text (‘en_US’, ‘de_DE’, ‘zh_CN’)

GetActionColumnText()[¶](#ApiClient.TsAXSCall.GetActionColumnText "Link to this definition")  
Returns the text value of the “action” column.

Returns:  Action column text

Return type:  str

GetActiveTimeOptionType()[¶](#ApiClient.TsAXSCall.GetActiveTimeOptionType "Link to this definition")  
Returns the type of the currently active time option.

Returns:  Type of active time option (“Timeless”, “Finally”, “TrueForWithin”, “Generally”, “SyncOnly”, “PollingCycleMultiplier”)

Return type:  string

GetArgument(*[identifier](#ApiClient.TsAXSCall.GetArgument.identifier "ApiClient.TsAXSCall.GetArgument.identifier (Python parameter) — Identifier of argument.")*)[¶](#ApiClient.TsAXSCall.GetArgument "Link to this definition")  
Gets the argument with the given identifier of the keyword test step.

Parameters:  identifier : str[¶](#ApiClient.TsAXSCall.GetArgument.identifier "Permalink to this definition")  
Identifier of argument. Has to match the identifier of an existing argument of the keyword.

Returns:  Argument of this test step whose identifier matches ‘identifier’ or None if there is no argument with this identifier.

Return type:  [`Argument`](Argument.md#ApiClient.Argument "ApiClient.Argument (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")

Raises:  
**ApiError** – If identifier is None or an empty string

GetComment()[¶](#ApiClient.TsAXSCall.GetComment "Link to this definition")  
Returns the comment of the test step in the current test case language.

Returns:  Comment text as shown in the comment tab

Return type:  str

GetCommentColumnText()[¶](#ApiClient.TsAXSCall.GetCommentColumnText "Link to this definition")  
Returns the text value of the “comment” column.

Returns:  Comment column text

Return type:  str

GetError()[¶](#ApiClient.TsAXSCall.GetError "Link to this definition")  
Returns a list of errors. Note that the error messages depend on the program language ecu.test is set to. Because of that we do not recommend to check against exact error messages, unless you are certain about the respective program language.

Returns:  List of errors

Return type:  list[str]

GetFailedComment()[¶](#ApiClient.TsAXSCall.GetFailedComment "Link to this definition")  
Returns the failed comment of the step.

Returns:  The failed comment

Return type:  string

GetIndex()[¶](#ApiClient.TsAXSCall.GetIndex "Link to this definition")  
Returns the zero based index in the parent.

Returns:  Zero based index

Return type:  integer

GetLineNo()[¶](#ApiClient.TsAXSCall.GetLineNo "Link to this definition")  
Returns the test steps line number within its test case.

Returns:  Line number

Return type:  int

GetMinimumDuration()[¶](#ApiClient.TsAXSCall.GetMinimumDuration "Link to this definition")  
Returns the minimum duration of the test step’s time option, if a corresponding option has been set.

Returns:  The minimum duration, else None

Return type:  string

GetMinimumDurationUnit()[¶](#ApiClient.TsAXSCall.GetMinimumDurationUnit "Link to this definition")  
Returns the unit of the minimum duration of the test step’s time option, if a corresponding option has been set.

Returns:  The unit of the minimum duration, else None

Return type:  string

GetParameterColumnText()[¶](#ApiClient.TsAXSCall.GetParameterColumnText "Link to this definition")  
Returns the text value of the “parameter” column.

Returns:  Parameter column text

Return type:  str

GetParent()[¶](#ApiClient.TsAXSCall.GetParent "Link to this definition")  
Returns the parent test step.

Returns:  The parent test step or None if it is a top level test step.

Return type:  [`TestStep`](TestStep.md#ApiClient.TestStep "ApiClient.TestStep (Python class) — Add a specific tag to this step.")

GetPollingCycle()[¶](#ApiClient.TsAXSCall.GetPollingCycle "Link to this definition")  
Returns the polling cycle of the test step’s time option, if a corresponding option has been set.

Returns:  The polling cycle, else None

Return type:  string

GetPollingCycleUnit()[¶](#ApiClient.TsAXSCall.GetPollingCycleUnit "Link to this definition")  
Returns the unit of the polling cycle of the test step’s time option, if a corresponding option has been set.

Returns:  The unit of the polling cycle, else None

Return type:  string

GetReturn(*[identifier](#ApiClient.TsAXSCall.GetReturn.identifier "ApiClient.TsAXSCall.GetReturn.identifier (Python parameter) — Identifier of the return.")*)[¶](#ApiClient.TsAXSCall.GetReturn "Link to this definition")  
Gets the return with the given identifier of the keyword test step.

Parameters:  identifier : str[¶](#ApiClient.TsAXSCall.GetReturn.identifier "Permalink to this definition")  
Identifier of the return. Has to match the identifier of an existing return of the keyword.

Returns:  Return of this test step whose identifier matches ‘identifier’ or None if there is no return with this identifier.

Return type:  [`Return`](Return.md#ApiClient.Return "ApiClient.Return (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")

Raises:  
**ApiError** – If identifier is None or an empty string

GetSuccessComment()[¶](#ApiClient.TsAXSCall.GetSuccessComment "Link to this definition")  
Returns the success comment of the step.

Returns:  The success comment

Return type:  string

GetTags()[¶](#ApiClient.TsAXSCall.GetTags "Link to this definition")  
Returns the tags set for this step.

Returns:  A (sorted) list of tags

Return type:  list[str]

GetTestManagementId()[¶](#ApiClient.TsAXSCall.GetTestManagementId "Link to this definition")  
Returns the test management id of the test step.

Returns:  Test step id.

Return type:  str

GetTestStepId()[¶](#ApiClient.TsAXSCall.GetTestStepId "Link to this definition")  
Returns the test step id.

Returns:  test step id

Return type:  str

GetTimeout()[¶](#ApiClient.TsAXSCall.GetTimeout "Link to this definition")  
Returns the timeout of the test step’s time option, if a corresponding option has been set.

Returns:  The timeout else None

Return type:  string

GetTimeoutUnit()[¶](#ApiClient.TsAXSCall.GetTimeoutUnit "Link to this definition")  
Returns the unit of the timeout of the test step’s time option, if a corresponding option has been set.

Returns:  The unit of the timeout else None

Return type:  string

GetTranslatedCommentText(*[language](#ApiClient.TsAXSCall.GetTranslatedCommentText.language "ApiClient.TsAXSCall.GetTranslatedCommentText.language (Python parameter) — Language of the requested text ('en_US', 'de_DE', 'zh_CN')")*)[¶](#ApiClient.TsAXSCall.GetTranslatedCommentText "Link to this definition")  
Returns the text value of the “comment” column in the given language.

Parameters:  language : str[¶](#ApiClient.TsAXSCall.GetTranslatedCommentText.language "Permalink to this definition")  
Language of the requested text (‘en_US’, ‘de_DE’, ‘zh_CN’)

Returns:  Comment column text

Return type:  str

GetType()[¶](#ApiClient.TsAXSCall.GetType "Link to this definition")  
Returns the type (class name) of the test step, e.g.

- “TsPreconditionBlock”

- “TsWait”

- “TsIfThenElse”

- “TsSwitchCase”

- “TsCaseNode”

Returns:  Type (class name) of the test step

Return type:  str

GetValueColumnText()[¶](#ApiClient.TsAXSCall.GetValueColumnText "Link to this definition")  
Returns the text value of the “value” column in your current test case language.

Returns:  Value column text

Return type:  str

IsBreakpoint()[¶](#ApiClient.TsAXSCall.IsBreakpoint "Link to this definition")  
Checks whether the test step is a break point.

Returns:  True if test step is a break point, else False

Return type:  boolean

IsContainer()[¶](#ApiClient.TsAXSCall.IsContainer "Link to this definition")  
Returns True, if the test step supports calling GetChildren as well as manipulating the structure of its children. (e. g. via inserting or deleting sub test steps).

Returns:  True if it can contain test steps, else False

Return type:  boolean

IsEnabled()[¶](#ApiClient.TsAXSCall.IsEnabled "Link to this definition")  
Returns the state of the test step.

Returns:  True if test step is enabled, otherwise False

Return type:  bool

IsInPostcondition()[¶](#ApiClient.TsAXSCall.IsInPostcondition "Link to this definition")  
Returns True if the test step is located in a postcondition

Returns:  True if the test step is located in a postcondition, else Flase

Return type:  bool

IsInPrecondition()[¶](#ApiClient.TsAXSCall.IsInPrecondition "Link to this definition")  
Returns True if the test step is located in a precondition

Returns:  True if the test step is located in a precondition, else False

Return type:  bool

IsOk()[¶](#ApiClient.TsAXSCall.IsOk "Link to this definition")  
Returns the internal state of correctness of the test step.

Returns:  True if no problems were found, else False

Return type:  boolean

IsVisible()[¶](#ApiClient.TsAXSCall.IsVisible "Link to this definition")  
Checks whether the test step is visible. This depends on the test step itself or a parent test step being disabled.

Returns:  True if test step is visible, else False

Return type:  boolean

RemoveArgument(*[identifier](#ApiClient.TsAXSCall.RemoveArgument.identifier "ApiClient.TsAXSCall.RemoveArgument.identifier (Python parameter) — Identifier of argument.")*)[¶](#ApiClient.TsAXSCall.RemoveArgument "Link to this definition")  
Removes the argument with the given identifier from the keyword test step.

Parameters:  identifier : str[¶](#ApiClient.TsAXSCall.RemoveArgument.identifier "Permalink to this definition")  
Identifier of argument. Has to match the identifier of an existing argument of the keyword.

Raises:  
**ApiError** – If there is no argument that matches identifier

RemoveReturn(*[identifier](#ApiClient.TsAXSCall.RemoveReturn.identifier "ApiClient.TsAXSCall.RemoveReturn.identifier (Python parameter) — Identifier of the return.")*)[¶](#ApiClient.TsAXSCall.RemoveReturn "Link to this definition")  
Removes the return with the given identifier from the keyword test step.

Parameters:  identifier : str[¶](#ApiClient.TsAXSCall.RemoveReturn.identifier "Permalink to this definition")  
Identifier of the return. Has to match the identifier of an existing return of the keyword.

Raises:  
**ApiError** – If there is no return that matches identifier

RemoveTag(*[tag](#ApiClient.TsAXSCall.RemoveTag.tag "ApiClient.TsAXSCall.RemoveTag.tag (Python parameter) — The tag to be removed")*)[¶](#ApiClient.TsAXSCall.RemoveTag "Link to this definition")  
Remove a specific tag from this step.

Parameters:  tag : str[¶](#ApiClient.TsAXSCall.RemoveTag.tag "Permalink to this definition")  
The tag to be removed

SetBreakpoint(*[enable](#ApiClient.TsAXSCall.SetBreakpoint.enable "ApiClient.TsAXSCall.SetBreakpoint.enable (Python parameter) — True if test step is a break point, else False")*)[¶](#ApiClient.TsAXSCall.SetBreakpoint "Link to this definition")  
Sets or unsets the test step to act as a break point.

Parameters:  enable : boolean[¶](#ApiClient.TsAXSCall.SetBreakpoint.enable "Permalink to this definition")  
True if test step is a break point, else False

SetComment(*[comment](#ApiClient.TsAXSCall.SetComment.comment "ApiClient.TsAXSCall.SetComment.comment (Python parameter) — Text to be displayed in the comment tab")*)[¶](#ApiClient.TsAXSCall.SetComment "Link to this definition")  
Sets a comment for the test step in the current test case language.

Parameters:  comment : str[¶](#ApiClient.TsAXSCall.SetComment.comment "Permalink to this definition")  
Text to be displayed in the comment tab

SetEnabled(*[state](#ApiClient.TsAXSCall.SetEnabled.state "ApiClient.TsAXSCall.SetEnabled.state (Python parameter) — True (Default) to enable, False to disable the test step.")=`True`*)[¶](#ApiClient.TsAXSCall.SetEnabled "Link to this definition")  
Enable or disable the test step.

Parameters:  state : bool[¶](#ApiClient.TsAXSCall.SetEnabled.state "Permalink to this definition")  
True (Default) to enable, False to disable the test step.

SetFailedComment(*[failedComment](#ApiClient.TsAXSCall.SetFailedComment.failedComment "ApiClient.TsAXSCall.SetFailedComment.failedComment (Python parameter) — The expression for the failed comment")*)[¶](#ApiClient.TsAXSCall.SetFailedComment "Link to this definition")  
Sets the expression for the failed comment of the step. The expression will be activated if it was not enabled previously.

Parameters:  failedComment : string[¶](#ApiClient.TsAXSCall.SetFailedComment.failedComment "Permalink to this definition")  
The expression for the failed comment

SetSuccessComment(*[successComment](#ApiClient.TsAXSCall.SetSuccessComment.successComment "ApiClient.TsAXSCall.SetSuccessComment.successComment (Python parameter) — The expression for the success comment")*)[¶](#ApiClient.TsAXSCall.SetSuccessComment "Link to this definition")  
Sets the expression for the success comment of the step. The expression will be activated if it was not enabled previously.

Parameters:  successComment : string[¶](#ApiClient.TsAXSCall.SetSuccessComment.successComment "Permalink to this definition")  
The expression for the success comment

SetTags(*[tags](#ApiClient.TsAXSCall.SetTags.tags "ApiClient.TsAXSCall.SetTags.tags (Python parameter) — The list of tags")*)[¶](#ApiClient.TsAXSCall.SetTags "Link to this definition")  
Set the list of tags for this step. The list of tags will be sorted and stored.

Parameters:  tags : list[str][¶](#ApiClient.TsAXSCall.SetTags.tags "Permalink to this definition")  
The list of tags

SetTestManagementId(*[testManagementId](#ApiClient.TsAXSCall.SetTestManagementId.testManagementId "ApiClient.TsAXSCall.SetTestManagementId.testManagementId (Python parameter) — Test management id of the test step")*)[¶](#ApiClient.TsAXSCall.SetTestManagementId "Link to this definition")  
Sets the test management id of the test step.

Parameters:  testManagementId : str[¶](#ApiClient.TsAXSCall.SetTestManagementId.testManagementId "Permalink to this definition")  
Test management id of the test step

SetTimeOptionOnlySynchronization(*[timeout](#ApiClient.TsAXSCall.SetTimeOptionOnlySynchronization.timeout "ApiClient.TsAXSCall.SetTimeOptionOnlySynchronization.timeout (Python parameter) — The timeout in ms to be used")*, *[pollingCycle](#ApiClient.TsAXSCall.SetTimeOptionOnlySynchronization.pollingCycle "ApiClient.TsAXSCall.SetTimeOptionOnlySynchronization.pollingCycle (Python parameter) — The polling cycle in ms or s or min or h or d.")=`None`*, *[timeoutUnit](#ApiClient.TsAXSCall.SetTimeOptionOnlySynchronization.timeoutUnit "ApiClient.TsAXSCall.SetTimeOptionOnlySynchronization.timeoutUnit (Python parameter) — Optional unit of the timeout (ms, s, min, h or d)")=`'ms'`*, *[pollingCycleUnit](#ApiClient.TsAXSCall.SetTimeOptionOnlySynchronization.pollingCycleUnit "ApiClient.TsAXSCall.SetTimeOptionOnlySynchronization.pollingCycleUnit (Python parameter) — Optional unit of the polling cycle (ms, s, min, h, or d)")=`'ms'`*)[¶](#ApiClient.TsAXSCall.SetTimeOptionOnlySynchronization "Link to this definition")  
Sets the test step’s time option to “only synchronization”.

Parameters:  timeout : string[¶](#ApiClient.TsAXSCall.SetTimeOptionOnlySynchronization.timeout "Permalink to this definition")  
The timeout in ms to be used

pollingCycle : string[¶](#ApiClient.TsAXSCall.SetTimeOptionOnlySynchronization.pollingCycle "Permalink to this definition")  
The polling cycle in ms or s or min or h or d. Might be left out.

timeoutUnit : string[¶](#ApiClient.TsAXSCall.SetTimeOptionOnlySynchronization.timeoutUnit "Permalink to this definition")  
Optional unit of the timeout (ms, s, min, h or d)

pollingCycleUnit : string[¶](#ApiClient.TsAXSCall.SetTimeOptionOnlySynchronization.pollingCycleUnit "Permalink to this definition")  
Optional unit of the polling cycle (ms, s, min, h, or d)

SetTimeOptionPollingCycleMultiplier(*[pollingCycleMultiplier](#ApiClient.TsAXSCall.SetTimeOptionPollingCycleMultiplier.pollingCycleMultiplier "ApiClient.TsAXSCall.SetTimeOptionPollingCycleMultiplier.pollingCycleMultiplier (Python parameter) — The polling cycle multiplier to be used.")*)[¶](#ApiClient.TsAXSCall.SetTimeOptionPollingCycleMultiplier "Link to this definition")  
Sets the test step’s time option to “polling cycle multiplier”. This option must only be used when inserting the test step into a Multi-Check!

Parameters:  pollingCycleMultiplier : string[¶](#ApiClient.TsAXSCall.SetTimeOptionPollingCycleMultiplier.pollingCycleMultiplier "Permalink to this definition")  
The polling cycle multiplier to be used.

SetTimeOptionTrueForAtLeast(*[minimumDuration](#ApiClient.TsAXSCall.SetTimeOptionTrueForAtLeast.minimumDuration "ApiClient.TsAXSCall.SetTimeOptionTrueForAtLeast.minimumDuration (Python parameter) — The minimum duration to be used")*, *[pollingCycle](#ApiClient.TsAXSCall.SetTimeOptionTrueForAtLeast.pollingCycle "ApiClient.TsAXSCall.SetTimeOptionTrueForAtLeast.pollingCycle (Python parameter) — Optional polling cycle to be used")=`None`*, *[timeoutUnit](#ApiClient.TsAXSCall.SetTimeOptionTrueForAtLeast.timeoutUnit "ApiClient.TsAXSCall.SetTimeOptionTrueForAtLeast.timeoutUnit (Python parameter) — Optional unit of the timeout (ms, s, min, h or d)")=`'ms'`*, *[pollingCycleUnit](#ApiClient.TsAXSCall.SetTimeOptionTrueForAtLeast.pollingCycleUnit "ApiClient.TsAXSCall.SetTimeOptionTrueForAtLeast.pollingCycleUnit (Python parameter) — Optional unit of the polling cycle (ms, s, min, h, or d)")=`'ms'`*)[¶](#ApiClient.TsAXSCall.SetTimeOptionTrueForAtLeast "Link to this definition")  
Sets the test step’s time option to “true for at least”.

Parameters:  minimumDuration : string[¶](#ApiClient.TsAXSCall.SetTimeOptionTrueForAtLeast.minimumDuration "Permalink to this definition")  
The minimum duration to be used

pollingCycle : string[¶](#ApiClient.TsAXSCall.SetTimeOptionTrueForAtLeast.pollingCycle "Permalink to this definition")  
Optional polling cycle to be used

timeoutUnit : string[¶](#ApiClient.TsAXSCall.SetTimeOptionTrueForAtLeast.timeoutUnit "Permalink to this definition")  
Optional unit of the timeout (ms, s, min, h or d)

pollingCycleUnit : string[¶](#ApiClient.TsAXSCall.SetTimeOptionTrueForAtLeast.pollingCycleUnit "Permalink to this definition")  
Optional unit of the polling cycle (ms, s, min, h, or d)

SetTimeOptionTrueForAtLeastWithin(*[minimumDuration](#ApiClient.TsAXSCall.SetTimeOptionTrueForAtLeastWithin.minimumDuration "ApiClient.TsAXSCall.SetTimeOptionTrueForAtLeastWithin.minimumDuration (Python parameter) — The minimum duration in ms to be used")*, *[timeout](#ApiClient.TsAXSCall.SetTimeOptionTrueForAtLeastWithin.timeout "ApiClient.TsAXSCall.SetTimeOptionTrueForAtLeastWithin.timeout (Python parameter) — The timeout to be used")*, *[pollingCycle](#ApiClient.TsAXSCall.SetTimeOptionTrueForAtLeastWithin.pollingCycle "ApiClient.TsAXSCall.SetTimeOptionTrueForAtLeastWithin.pollingCycle (Python parameter) — Optional polling cycle to be used")=`None`*, *[timeoutUnit](#ApiClient.TsAXSCall.SetTimeOptionTrueForAtLeastWithin.timeoutUnit "ApiClient.TsAXSCall.SetTimeOptionTrueForAtLeastWithin.timeoutUnit (Python parameter) — Optional unit of the timeout (ms, s, min, h or d)")=`'ms'`*, *[pollingCycleUnit](#ApiClient.TsAXSCall.SetTimeOptionTrueForAtLeastWithin.pollingCycleUnit "ApiClient.TsAXSCall.SetTimeOptionTrueForAtLeastWithin.pollingCycleUnit (Python parameter) — Optional unit of the polling cycle (ms, s, min, h, or d)")=`'ms'`*)[¶](#ApiClient.TsAXSCall.SetTimeOptionTrueForAtLeastWithin "Link to this definition")  
Sets the test step’s time option to “true for at least … within …”.

Parameters:  minimumDuration : string[¶](#ApiClient.TsAXSCall.SetTimeOptionTrueForAtLeastWithin.minimumDuration "Permalink to this definition")  
The minimum duration in ms to be used

timeout : string[¶](#ApiClient.TsAXSCall.SetTimeOptionTrueForAtLeastWithin.timeout "Permalink to this definition")  
The timeout to be used

pollingCycle : string[¶](#ApiClient.TsAXSCall.SetTimeOptionTrueForAtLeastWithin.pollingCycle "Permalink to this definition")  
Optional polling cycle to be used

timeoutUnit : string[¶](#ApiClient.TsAXSCall.SetTimeOptionTrueForAtLeastWithin.timeoutUnit "Permalink to this definition")  
Optional unit of the timeout (ms, s, min, h or d)

pollingCycleUnit : string[¶](#ApiClient.TsAXSCall.SetTimeOptionTrueForAtLeastWithin.pollingCycleUnit "Permalink to this definition")  
Optional unit of the polling cycle (ms, s, min, h, or d)

SetTimeOptionWaitUntilTrue(*[timeout](#ApiClient.TsAXSCall.SetTimeOptionWaitUntilTrue.timeout "ApiClient.TsAXSCall.SetTimeOptionWaitUntilTrue.timeout (Python parameter) — The timeout to be used")*, *[pollingCycle](#ApiClient.TsAXSCall.SetTimeOptionWaitUntilTrue.pollingCycle "ApiClient.TsAXSCall.SetTimeOptionWaitUntilTrue.pollingCycle (Python parameter) — Optional polling cycle to be used.")=`None`*, *[timeoutUnit](#ApiClient.TsAXSCall.SetTimeOptionWaitUntilTrue.timeoutUnit "ApiClient.TsAXSCall.SetTimeOptionWaitUntilTrue.timeoutUnit (Python parameter) — Optional unit of the timeout (ms, s, min, h or d)")=`'ms'`*, *[pollingCycleUnit](#ApiClient.TsAXSCall.SetTimeOptionWaitUntilTrue.pollingCycleUnit "ApiClient.TsAXSCall.SetTimeOptionWaitUntilTrue.pollingCycleUnit (Python parameter) — Optional unit of the polling cycle (ms, s, min, h, or d).")=`'ms'`*)[¶](#ApiClient.TsAXSCall.SetTimeOptionWaitUntilTrue "Link to this definition")  
Sets the test step’s time option to “wait until true”.

Parameters:  timeout : string[¶](#ApiClient.TsAXSCall.SetTimeOptionWaitUntilTrue.timeout "Permalink to this definition")  
The timeout to be used

pollingCycle : string[¶](#ApiClient.TsAXSCall.SetTimeOptionWaitUntilTrue.pollingCycle "Permalink to this definition")  
Optional polling cycle to be used.

timeoutUnit : string[¶](#ApiClient.TsAXSCall.SetTimeOptionWaitUntilTrue.timeoutUnit "Permalink to this definition")  
Optional unit of the timeout (ms, s, min, h or d)

pollingCycleUnit : string[¶](#ApiClient.TsAXSCall.SetTimeOptionWaitUntilTrue.pollingCycleUnit "Permalink to this definition")  
Optional unit of the polling cycle (ms, s, min, h, or d).

SetTranslatedCommentText(*[comment](#ApiClient.TsAXSCall.SetTranslatedCommentText.comment "ApiClient.TsAXSCall.SetTranslatedCommentText.comment (Python parameter) — Text to be displayed")*, *[language](#ApiClient.TsAXSCall.SetTranslatedCommentText.language "ApiClient.TsAXSCall.SetTranslatedCommentText.language (Python parameter) — Language of the text ('en_US', 'de_DE', 'zh_CN')")*)[¶](#ApiClient.TsAXSCall.SetTranslatedCommentText "Link to this definition")  
Sets a comment for the test step in the given language.

Parameters:  comment : str[¶](#ApiClient.TsAXSCall.SetTranslatedCommentText.comment "Permalink to this definition")  
Text to be displayed

language : str[¶](#ApiClient.TsAXSCall.SetTranslatedCommentText.language "Permalink to this definition")  
Language of the text (‘en_US’, ‘de_DE’, ‘zh_CN’)

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
