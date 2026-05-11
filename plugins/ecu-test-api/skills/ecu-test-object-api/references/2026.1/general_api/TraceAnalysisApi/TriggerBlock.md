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

[ API for Touch Inputs ](../TouchInputApi.md)

[ API for Trace Analyses ](../TraceAnalysisApi.md)

API for Trace Analyses

[ AnalysisBlock ](AnalysisBlock.md)

[ Assertion ](Assertion.md)

[ AutosarTimeSyncRecordingGroupInfo ](AutosarTimeSyncRecordingGroupInfo.md)

[ AutosarTimeSynchronization ](AutosarTimeSynchronization.md)

[ Calculation ](Calculation.md)

[ CaseDefNode ](CaseDefNode.md)

[ CrossCorrelationSynchronization ](CrossCorrelationSynchronization.md)

[ ElseNode ](ElseNode.md)

[ Episode ](Episode.md)

[ EqualEntry ](EqualEntry.md)

[ EqualnessMatchingSynchronization ](EqualnessMatchingSynchronization.md)

[ ExpectationModeOptions ](ExpectationModeOptions.md)

[ ExpectationSynchronization ](ExpectationSynchronization.md)

[ GenericSignal ](GenericSignal.md)

[ IfDef ](IfDef.md)

[ IfThenElse ](IfThenElse.md)

[ LeastSquaresSynchronization ](LeastSquaresSynchronization.md)

[ OffsetSynchronization ](OffsetSynchronization.md)

[ PackageBase ](PackageBase.md)

[ Plot ](Plot.md)

[ PlotAxis ](PlotAxis.md)

[ PlotCalculatedSignal ](PlotCalculatedSignal.md)

[ PlotSignal ](PlotSignal.md)

[ PlotSignalBase ](PlotSignalBase.md)

[ PlotSubConfig ](PlotSubConfig.md)

[ PlotSubPlot ](PlotSubPlot.md)

[ RecordingGroupBase ](RecordingGroupBase.md)

[ ReportConfig ](ReportConfig.md)

[ SignalBinding ](SignalBinding.md)

[ SignalRecording ](SignalRecording.md)

[ SwitchDefCase ](SwitchDefCase.md)

[ SyncConfig ](SyncConfig.md)

[ SyncExpectation ](SyncExpectation.md)

[ Synchronization ](Synchronization.md)

[ TemplateBasedTraceStep ](TemplateBasedTraceStep.md)

[ ThenNode ](ThenNode.md)

[ TraceAnalysis ](TraceAnalysis.md)

[ TraceAnalysisReference ](TraceAnalysisReference.md)

[ TraceAnalysisReferenceDeprecated ](TraceAnalysisReferenceDeprecated.md)

[ TraceStep ](TraceStep.md)

[ TraceStepContainer ](TraceStepContainer.md)

TriggerBlock [ TriggerBlock ](#)

TriggerBlock

- [C TriggerBlock ](#ApiClient.TriggerBlock)
  - [A MODE_STARTTRIGGER_TO_NEXT_STOPTRIGGER ](#ApiClient.TriggerBlock.MODE_STARTTRIGGER_TO_NEXT_STOPTRIGGER)
  - [A MODE_STARTTRIGGER_WHILE_NOT_STOPTRIGGER ](#ApiClient.TriggerBlock.MODE_STARTTRIGGER_WHILE_NOT_STOPTRIGGER)
  - [A MODE_STARTTRIGGER_WITH_TIME_OFFSETS ](#ApiClient.TriggerBlock.MODE_STARTTRIGGER_WITH_TIME_OFFSETS)
  - [A MODE_WHILE_STARTTRIGGER ](#ApiClient.TriggerBlock.MODE_WHILE_STARTTRIGGER)
  - [M AddTag ](#ApiClient.TriggerBlock.AddTag)
  - [M AppendTraceStep ](#ApiClient.TriggerBlock.AppendTraceStep)
  - [M Clone ](#ApiClient.TriggerBlock.Clone)
  - [M GetDescription ](#ApiClient.TriggerBlock.GetDescription)
  - [M GetEndOfTraceAsStopTrigger ](#ApiClient.TriggerBlock.GetEndOfTraceAsStopTrigger)
  - [M GetIgnoreFirstMode ](#ApiClient.TriggerBlock.GetIgnoreFirstMode)
  - [M GetIgnoreFirstTime ](#ApiClient.TriggerBlock.GetIgnoreFirstTime)
  - [M GetIgnoreLastMode ](#ApiClient.TriggerBlock.GetIgnoreLastMode)
  - [M GetIgnoreLastTime ](#ApiClient.TriggerBlock.GetIgnoreLastTime)
  - [M GetIndex ](#ApiClient.TriggerBlock.GetIndex)
  - [M GetLineNo ](#ApiClient.TriggerBlock.GetLineNo)
  - [M GetName ](#ApiClient.TriggerBlock.GetName)
  - [M GetReportEntryLimit ](#ApiClient.TriggerBlock.GetReportEntryLimit)
  - [M GetReportFilterCondition ](#ApiClient.TriggerBlock.GetReportFilterCondition)
  - [M GetReportIgnoredRanges ](#ApiClient.TriggerBlock.GetReportIgnoredRanges)
  - [M GetReportOmittedStartTrigger ](#ApiClient.TriggerBlock.GetReportOmittedStartTrigger)
  - [M GetResultNoMatch ](#ApiClient.TriggerBlock.GetResultNoMatch)
  - [M GetResultTruncatedRange ](#ApiClient.TriggerBlock.GetResultTruncatedRange)
  - [M GetStartOffset ](#ApiClient.TriggerBlock.GetStartOffset)
  - [M GetStartTrigger ](#ApiClient.TriggerBlock.GetStartTrigger)
  - [M GetStopOffset ](#ApiClient.TriggerBlock.GetStopOffset)
  - [M GetStopTrigger ](#ApiClient.TriggerBlock.GetStopTrigger)
  - [M GetTags ](#ApiClient.TriggerBlock.GetTags)
  - [M GetTraceSteps ](#ApiClient.TriggerBlock.GetTraceSteps)
  - [M GetTriggerMode ](#ApiClient.TriggerBlock.GetTriggerMode)
  - [M GetTriggerOnce ](#ApiClient.TriggerBlock.GetTriggerOnce)
  - [M GetType ](#ApiClient.TriggerBlock.GetType)
  - [M GetUuid ](#ApiClient.TriggerBlock.GetUuid)
  - [M InsertTraceStep ](#ApiClient.TriggerBlock.InsertTraceStep)
  - [M IsContainer ](#ApiClient.TriggerBlock.IsContainer)
  - [M IsEnabled ](#ApiClient.TriggerBlock.IsEnabled)
  - [M IsOk ](#ApiClient.TriggerBlock.IsOk)
  - [M IsVisible ](#ApiClient.TriggerBlock.IsVisible)
  - [M RemoveTag ](#ApiClient.TriggerBlock.RemoveTag)
  - [M RemoveTraceStep ](#ApiClient.TriggerBlock.RemoveTraceStep)
  - [M SetDescription ](#ApiClient.TriggerBlock.SetDescription)
  - [M SetEnabled ](#ApiClient.TriggerBlock.SetEnabled)
  - [M SetEndOfTraceAsStopTrigger ](#ApiClient.TriggerBlock.SetEndOfTraceAsStopTrigger)
  - [M SetIgnoreFirst ](#ApiClient.TriggerBlock.SetIgnoreFirst)
  - [M SetIgnoreLast ](#ApiClient.TriggerBlock.SetIgnoreLast)
  - [M SetName ](#ApiClient.TriggerBlock.SetName)
  - [M SetReportEntryLimit ](#ApiClient.TriggerBlock.SetReportEntryLimit)
  - [M SetReportFilterCondition ](#ApiClient.TriggerBlock.SetReportFilterCondition)
  - [M SetReportIgnoredRanges ](#ApiClient.TriggerBlock.SetReportIgnoredRanges)
  - [M SetReportOmittedStartTrigger ](#ApiClient.TriggerBlock.SetReportOmittedStartTrigger)
  - [M SetResultNoMatch ](#ApiClient.TriggerBlock.SetResultNoMatch)
  - [M SetResultTruncatedRange ](#ApiClient.TriggerBlock.SetResultTruncatedRange)
  - [M SetStartOffset ](#ApiClient.TriggerBlock.SetStartOffset)
  - [M SetStartTrigger ](#ApiClient.TriggerBlock.SetStartTrigger)
  - [M SetStopOffset ](#ApiClient.TriggerBlock.SetStopOffset)
  - [M SetStopTrigger ](#ApiClient.TriggerBlock.SetStopTrigger)
  - [M SetTags ](#ApiClient.TriggerBlock.SetTags)
  - [M SetTriggerMode ](#ApiClient.TriggerBlock.SetTriggerMode)
  - [M SetTriggerOnce ](#ApiClient.TriggerBlock.SetTriggerOnce)

[ UtcTimestampSynchronization ](UtcTimestampSynchronization.md)

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

TriggerBlock

- [C TriggerBlock ](#ApiClient.TriggerBlock)
  - [A MODE_STARTTRIGGER_TO_NEXT_STOPTRIGGER ](#ApiClient.TriggerBlock.MODE_STARTTRIGGER_TO_NEXT_STOPTRIGGER)
  - [A MODE_STARTTRIGGER_WHILE_NOT_STOPTRIGGER ](#ApiClient.TriggerBlock.MODE_STARTTRIGGER_WHILE_NOT_STOPTRIGGER)
  - [A MODE_STARTTRIGGER_WITH_TIME_OFFSETS ](#ApiClient.TriggerBlock.MODE_STARTTRIGGER_WITH_TIME_OFFSETS)
  - [A MODE_WHILE_STARTTRIGGER ](#ApiClient.TriggerBlock.MODE_WHILE_STARTTRIGGER)
  - [M AddTag ](#ApiClient.TriggerBlock.AddTag)
  - [M AppendTraceStep ](#ApiClient.TriggerBlock.AppendTraceStep)
  - [M Clone ](#ApiClient.TriggerBlock.Clone)
  - [M GetDescription ](#ApiClient.TriggerBlock.GetDescription)
  - [M GetEndOfTraceAsStopTrigger ](#ApiClient.TriggerBlock.GetEndOfTraceAsStopTrigger)
  - [M GetIgnoreFirstMode ](#ApiClient.TriggerBlock.GetIgnoreFirstMode)
  - [M GetIgnoreFirstTime ](#ApiClient.TriggerBlock.GetIgnoreFirstTime)
  - [M GetIgnoreLastMode ](#ApiClient.TriggerBlock.GetIgnoreLastMode)
  - [M GetIgnoreLastTime ](#ApiClient.TriggerBlock.GetIgnoreLastTime)
  - [M GetIndex ](#ApiClient.TriggerBlock.GetIndex)
  - [M GetLineNo ](#ApiClient.TriggerBlock.GetLineNo)
  - [M GetName ](#ApiClient.TriggerBlock.GetName)
  - [M GetReportEntryLimit ](#ApiClient.TriggerBlock.GetReportEntryLimit)
  - [M GetReportFilterCondition ](#ApiClient.TriggerBlock.GetReportFilterCondition)
  - [M GetReportIgnoredRanges ](#ApiClient.TriggerBlock.GetReportIgnoredRanges)
  - [M GetReportOmittedStartTrigger ](#ApiClient.TriggerBlock.GetReportOmittedStartTrigger)
  - [M GetResultNoMatch ](#ApiClient.TriggerBlock.GetResultNoMatch)
  - [M GetResultTruncatedRange ](#ApiClient.TriggerBlock.GetResultTruncatedRange)
  - [M GetStartOffset ](#ApiClient.TriggerBlock.GetStartOffset)
  - [M GetStartTrigger ](#ApiClient.TriggerBlock.GetStartTrigger)
  - [M GetStopOffset ](#ApiClient.TriggerBlock.GetStopOffset)
  - [M GetStopTrigger ](#ApiClient.TriggerBlock.GetStopTrigger)
  - [M GetTags ](#ApiClient.TriggerBlock.GetTags)
  - [M GetTraceSteps ](#ApiClient.TriggerBlock.GetTraceSteps)
  - [M GetTriggerMode ](#ApiClient.TriggerBlock.GetTriggerMode)
  - [M GetTriggerOnce ](#ApiClient.TriggerBlock.GetTriggerOnce)
  - [M GetType ](#ApiClient.TriggerBlock.GetType)
  - [M GetUuid ](#ApiClient.TriggerBlock.GetUuid)
  - [M InsertTraceStep ](#ApiClient.TriggerBlock.InsertTraceStep)
  - [M IsContainer ](#ApiClient.TriggerBlock.IsContainer)
  - [M IsEnabled ](#ApiClient.TriggerBlock.IsEnabled)
  - [M IsOk ](#ApiClient.TriggerBlock.IsOk)
  - [M IsVisible ](#ApiClient.TriggerBlock.IsVisible)
  - [M RemoveTag ](#ApiClient.TriggerBlock.RemoveTag)
  - [M RemoveTraceStep ](#ApiClient.TriggerBlock.RemoveTraceStep)
  - [M SetDescription ](#ApiClient.TriggerBlock.SetDescription)
  - [M SetEnabled ](#ApiClient.TriggerBlock.SetEnabled)
  - [M SetEndOfTraceAsStopTrigger ](#ApiClient.TriggerBlock.SetEndOfTraceAsStopTrigger)
  - [M SetIgnoreFirst ](#ApiClient.TriggerBlock.SetIgnoreFirst)
  - [M SetIgnoreLast ](#ApiClient.TriggerBlock.SetIgnoreLast)
  - [M SetName ](#ApiClient.TriggerBlock.SetName)
  - [M SetReportEntryLimit ](#ApiClient.TriggerBlock.SetReportEntryLimit)
  - [M SetReportFilterCondition ](#ApiClient.TriggerBlock.SetReportFilterCondition)
  - [M SetReportIgnoredRanges ](#ApiClient.TriggerBlock.SetReportIgnoredRanges)
  - [M SetReportOmittedStartTrigger ](#ApiClient.TriggerBlock.SetReportOmittedStartTrigger)
  - [M SetResultNoMatch ](#ApiClient.TriggerBlock.SetResultNoMatch)
  - [M SetResultTruncatedRange ](#ApiClient.TriggerBlock.SetResultTruncatedRange)
  - [M SetStartOffset ](#ApiClient.TriggerBlock.SetStartOffset)
  - [M SetStartTrigger ](#ApiClient.TriggerBlock.SetStartTrigger)
  - [M SetStopOffset ](#ApiClient.TriggerBlock.SetStopOffset)
  - [M SetStopTrigger ](#ApiClient.TriggerBlock.SetStopTrigger)
  - [M SetTags ](#ApiClient.TriggerBlock.SetTags)
  - [M SetTriggerMode ](#ApiClient.TriggerBlock.SetTriggerMode)
  - [M SetTriggerOnce ](#ApiClient.TriggerBlock.SetTriggerOnce)

# TriggerBlock[¶](#triggerblock "Link to this heading")

*class* TriggerBlock[¶](#ApiClient.TriggerBlock "Link to this definition")  
Returned by

- [`TraceAnalysisApi.CreateTriggerBlock`](../TraceAnalysisApi.md#ApiClient.TraceAnalysisApi.CreateTriggerBlock "ApiClient.TraceAnalysisApi.CreateTriggerBlock (Python method) — Creates a trigger block.")

MODE_STARTTRIGGER_TO_NEXT_STOPTRIGGER[¶](#ApiClient.TriggerBlock.MODE_STARTTRIGGER_TO_NEXT_STOPTRIGGER "Link to this definition")  
Returns the constant used to specify the expectation mode ‘from start trigger until next time stop trigger is fulfilled’.

Returns:  The constant

Return type:  str

MODE_STARTTRIGGER_WHILE_NOT_STOPTRIGGER[¶](#ApiClient.TriggerBlock.MODE_STARTTRIGGER_WHILE_NOT_STOPTRIGGER "Link to this definition")  
Returns the constant used to specify the expectation mode ‘from start trigger as long as stop trigger is not fulfilled’.

Returns:  The constant

Return type:  str

MODE_STARTTRIGGER_WITH_TIME_OFFSETS[¶](#ApiClient.TriggerBlock.MODE_STARTTRIGGER_WITH_TIME_OFFSETS "Link to this definition")  
Returns the constant used to specify the expectation mode ‘with time offset if start trigger is fulfilled’.

Returns:  The constant

Return type:  str

MODE_WHILE_STARTTRIGGER[¶](#ApiClient.TriggerBlock.MODE_WHILE_STARTTRIGGER "Link to this definition")  
Returns the constant used to specify the expectation mode ‘as long as start trigger is fulfilled’.

Returns:  The constant

Return type:  str

AddTag(*[tag](#ApiClient.TriggerBlock.AddTag.tag "ApiClient.TriggerBlock.AddTag.tag (Python parameter) — The tag to be set")*)[¶](#ApiClient.TriggerBlock.AddTag "Link to this definition")  
Add a specific tag to this step.

Parameters:  tag : str[¶](#ApiClient.TriggerBlock.AddTag.tag "Permalink to this definition")  
The tag to be set

AppendTraceStep(*[traceStep](#ApiClient.TriggerBlock.AppendTraceStep.traceStep "ApiClient.TriggerBlock.AppendTraceStep.traceStep (Python parameter) — Trace step to be added")*)[¶](#ApiClient.TriggerBlock.AppendTraceStep "Link to this definition")  
Adds a trace step at the end of its children.

Parameters:  traceStep[¶](#ApiClient.TriggerBlock.AppendTraceStep.traceStep "Permalink to this definition")  
Trace step to be added

Clone()[¶](#ApiClient.TriggerBlock.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`TriggerBlock`](#ApiClient.TriggerBlock "ApiClient.TriggerBlock (Python class) — TraceAnalysisApi.CreateTriggerBlock")

GetDescription()[¶](#ApiClient.TriggerBlock.GetDescription "Link to this definition")  
Returns the description of the trace analysis element.

Returns:  The description

Return type:  str

GetEndOfTraceAsStopTrigger()[¶](#ApiClient.TriggerBlock.GetEndOfTraceAsStopTrigger "Link to this definition")  
Returns whether the end of trace shall be handled as a stop trigger.

Returns:  The setting for the treatment of unfinished ranges at the end of trace

Return type:  bool

GetIgnoreFirstMode()[¶](#ApiClient.TriggerBlock.GetIgnoreFirstMode "Link to this definition")  
Returns the ignore first mode.

Returns:  The mode: ‘manual’, ‘firstsample’ or ‘disabled’

Return type:  str

GetIgnoreFirstTime()[¶](#ApiClient.TriggerBlock.GetIgnoreFirstTime "Link to this definition")  
Returns the ignore first time if set. Otherwise None is returned.

Returns:  The expression value (only for manual mode)

Return type:  str

GetIgnoreLastMode()[¶](#ApiClient.TriggerBlock.GetIgnoreLastMode "Link to this definition")  
Returns the ignore last mode.

Returns:  The mode: ‘manual’ or ‘disabled’

Return type:  str

GetIgnoreLastTime()[¶](#ApiClient.TriggerBlock.GetIgnoreLastTime "Link to this definition")  
Returns the ignore last time if set. Otherwise None is returned.

Returns:  The expression value (only for manual mode)

Return type:  str

GetIndex()[¶](#ApiClient.TriggerBlock.GetIndex "Link to this definition")  
Returns the zero based index in the parent.

Returns:  Zero based index

Return type:  int

GetLineNo()[¶](#ApiClient.TriggerBlock.GetLineNo "Link to this definition")  
Returns the trace steps line number within its trace analysis.

Returns:  Line number

Return type:  int

GetName()[¶](#ApiClient.TriggerBlock.GetName "Link to this definition")  
Returns the name of the trace analysis element.

Returns:  The name

Return type:  str

GetReportEntryLimit()[¶](#ApiClient.TriggerBlock.GetReportEntryLimit "Link to this definition")  
Returns the maximal number of entries per verdict and child the reporting shall be limited to. A return value of None indicates that no limitation is in place.

Returns:  The maximal number of entries per verdict and child as expression string or None

Return type:  str

GetReportFilterCondition()[¶](#ApiClient.TriggerBlock.GetReportFilterCondition "Link to this definition")  
Returns the condition that must be matched for the trigger range to be reported. Possible values are: - ‘NONE’ (meaning no filtering for verdict types) - ‘SUCCESS’ (meaning SUCCESS or worse) - ‘INCONCLUSIVE’ (meaning INCONCLUSIVE or worse) - ‘FAILED’ (meaning FAILED or worse) - ‘ERROR’ (meaning ERROR)

Returns:  The report condition

Return type:  str

GetReportIgnoredRanges()[¶](#ApiClient.TriggerBlock.GetReportIgnoredRanges "Link to this definition")  
Returns whether ranges without a sample after consideration of the ignore times should be reported.

Returns:  The setting whether ignored ranges will be reported

Return type:  bool

GetReportOmittedStartTrigger()[¶](#ApiClient.TriggerBlock.GetReportOmittedStartTrigger "Link to this definition")  
Returns whether omitted start triggers will be reported.

Returns:  The setting whether omitted start triggers will be reported

Return type:  bool

GetResultNoMatch()[¶](#ApiClient.TriggerBlock.GetResultNoMatch "Link to this definition")  
Returns the verdict of a trigger block that does not open any trigger range.

Returns:  The verdict of a trigger block without a trigger range

Return type:  str

GetResultTruncatedRange()[¶](#ApiClient.TriggerBlock.GetResultTruncatedRange "Link to this definition")  
Returns the blanket verdict of a truncated trigger range or None if truncated trigger ranges are evaluated normally.

Returns:  The verdict of a truncated trigger range

Return type:  str

GetStartOffset()[¶](#ApiClient.TriggerBlock.GetStartOffset "Link to this definition")  
Returns the start offset expression.

Returns:  The start offset

Return type:  str

GetStartTrigger()[¶](#ApiClient.TriggerBlock.GetStartTrigger "Link to this definition")  
Returns the start trigger expression.

Returns:  The start trigger expression

Return type:  str

GetStopOffset()[¶](#ApiClient.TriggerBlock.GetStopOffset "Link to this definition")  
Returns the stop offset expression.

Returns:  The stop offset

Return type:  str

GetStopTrigger()[¶](#ApiClient.TriggerBlock.GetStopTrigger "Link to this definition")  
Returns the stop trigger expression or None if no stop trigger is defined.

Returns:  The stop trigger expression

Return type:  str

GetTags()[¶](#ApiClient.TriggerBlock.GetTags "Link to this definition")  
Returns the tags set for this step.

Returns:  A (sorted) list of tags

Return type:  list[str]

GetTraceSteps(*[skipDisabledSteps](#ApiClient.TriggerBlock.GetTraceSteps.skipDisabledSteps "ApiClient.TriggerBlock.GetTraceSteps.skipDisabledSteps (Python parameter) — Defines whether disabled trace steps should be excluded, defaults to False.")=`False`*, *[recursive](#ApiClient.TriggerBlock.GetTraceSteps.recursive "ApiClient.TriggerBlock.GetTraceSteps.recursive (Python parameter) — Defines whether children of children are included, defaults to False.")=`False`*)[¶](#ApiClient.TriggerBlock.GetTraceSteps "Link to this definition")  
Returns either direct or all children of the trace step.

Parameters:  skipDisabledSteps : boolean[¶](#ApiClient.TriggerBlock.GetTraceSteps.skipDisabledSteps "Permalink to this definition")  
Defines whether disabled trace steps should be excluded, defaults to False.

recursive : boolean[¶](#ApiClient.TriggerBlock.GetTraceSteps.recursive "Permalink to this definition")  
Defines whether children of children are included, defaults to False.

Returns:  The trace steps as flat list.

Return type:  list[[`TraceStep`](TraceStep.md#ApiClient.TraceStep "ApiClient.TraceStep (Python class) — Base class for all elements of a trace analysis and the trace analysis itself.")]

GetTriggerMode()[¶](#ApiClient.TriggerBlock.GetTriggerMode "Link to this definition")  
Returns the trigger mode.

Returns:  The trigger mode

Return type:  str

GetTriggerOnce()[¶](#ApiClient.TriggerBlock.GetTriggerOnce "Link to this definition")  
Returns whether the trigger block should trigger only once.

Returns:  The setting for restricting the number of trigger ranges to one

Return type:  bool

GetType()[¶](#ApiClient.TriggerBlock.GetType "Link to this definition")  
Returns the type (class name) of the trace step, e.g.

- ‘Episode’

- ‘AnalysisBlock’

- ‘TriggerBlock’

- ‘Calculation’

- ‘TemplateBasedTraceStep’

- ‘TraceAnalysisReference’

- ‘TraceAnalysisReferenceDeprecated’

Returns:  Type (class name) of the trace step

Return type:  str

GetUuid()[¶](#ApiClient.TriggerBlock.GetUuid "Link to this definition")  
Returns the UUID of the trace step.

Returns:  UUID of the trace step

Return type:  str

InsertTraceStep(*[traceStep](#ApiClient.TriggerBlock.InsertTraceStep.traceStep "ApiClient.TriggerBlock.InsertTraceStep.traceStep (Python parameter) — Trace step to be added")*, *[position](#ApiClient.TriggerBlock.InsertTraceStep.position "ApiClient.TriggerBlock.InsertTraceStep.position (Python parameter) — Target index of child beginning with 0")*)[¶](#ApiClient.TriggerBlock.InsertTraceStep "Link to this definition")  
Adds a trace step at a certain line of the trace analysis.

Parameters:  traceStep[¶](#ApiClient.TriggerBlock.InsertTraceStep.traceStep "Permalink to this definition")  
Trace step to be added

position : integer[¶](#ApiClient.TriggerBlock.InsertTraceStep.position "Permalink to this definition")  
Target index of child beginning with 0

IsContainer()[¶](#ApiClient.TriggerBlock.IsContainer "Link to this definition")  
Checks whether this trace step can contain trace steps.

Returns:  True if it can contain trace steps, else False

Return type:  boolean

IsEnabled()[¶](#ApiClient.TriggerBlock.IsEnabled "Link to this definition")  
Checks whether the trace step is enabled.

Returns:  True if trace step is enabled, else False

Return type:  boolean

IsOk()[¶](#ApiClient.TriggerBlock.IsOk "Link to this definition")  
Returns the internal state of correctness of the trace step.

Returns:  True if no problems were found, else False

Return type:  boolean

IsVisible()[¶](#ApiClient.TriggerBlock.IsVisible "Link to this definition")  
Checks whether the trace step is visible. This depends on the trace step itself or a parent trace step being disabled.

Returns:  True if trace step is visible, else False

Return type:  boolean

RemoveTag(*[tag](#ApiClient.TriggerBlock.RemoveTag.tag "ApiClient.TriggerBlock.RemoveTag.tag (Python parameter) — The tag to be removed")*)[¶](#ApiClient.TriggerBlock.RemoveTag "Link to this definition")  
Remove a specific tag from this step.

Parameters:  tag : str[¶](#ApiClient.TriggerBlock.RemoveTag.tag "Permalink to this definition")  
The tag to be removed

RemoveTraceStep(*[traceStep](#ApiClient.TriggerBlock.RemoveTraceStep.traceStep "ApiClient.TriggerBlock.RemoveTraceStep.traceStep (Python parameter) — Trace step to be removed")*)[¶](#ApiClient.TriggerBlock.RemoveTraceStep "Link to this definition")  
Removes the given trace step from the trace analysis.

Parameters:  traceStep[¶](#ApiClient.TriggerBlock.RemoveTraceStep.traceStep "Permalink to this definition")  
Trace step to be removed

SetDescription(*[value](#ApiClient.TriggerBlock.SetDescription.value "ApiClient.TriggerBlock.SetDescription.value (Python parameter) — The new description")*)[¶](#ApiClient.TriggerBlock.SetDescription "Link to this definition")  
Sets the description of the trace analysis element.

Parameters:  value : str[¶](#ApiClient.TriggerBlock.SetDescription.value "Permalink to this definition")  
The new description

SetEnabled(*[enable](#ApiClient.TriggerBlock.SetEnabled.enable "ApiClient.TriggerBlock.SetEnabled.enable (Python parameter) — If True, enables the trace step, if False, disables the trace step")*)[¶](#ApiClient.TriggerBlock.SetEnabled "Link to this definition")  
Enables or disables the trace step (this also affects child trace steps).

Parameters:  enable : boolean[¶](#ApiClient.TriggerBlock.SetEnabled.enable "Permalink to this definition")  
If True, enables the trace step, if False, disables the trace step

SetEndOfTraceAsStopTrigger(*[mode](#ApiClient.TriggerBlock.SetEndOfTraceAsStopTrigger.mode "ApiClient.TriggerBlock.SetEndOfTraceAsStopTrigger.mode (Python parameter) — If True, unfinished ranges will be completed as if an ordinary stop trigger occurred.")*)[¶](#ApiClient.TriggerBlock.SetEndOfTraceAsStopTrigger "Link to this definition")  
Sets whether the end of trace shall be handled as a stop trigger.

Parameters:  mode : bool[¶](#ApiClient.TriggerBlock.SetEndOfTraceAsStopTrigger.mode "Permalink to this definition")  
If True, unfinished ranges will be completed as if an ordinary stop trigger occurred. Otherwise such ranges will be rated INCONCLUSIVE.

SetIgnoreFirst(*[mode](#ApiClient.TriggerBlock.SetIgnoreFirst.mode "ApiClient.TriggerBlock.SetIgnoreFirst.mode (Python parameter) — The mode for ignore first")*, *[ignoreTime](#ApiClient.TriggerBlock.SetIgnoreFirst.ignoreTime "ApiClient.TriggerBlock.SetIgnoreFirst.ignoreTime (Python parameter) — The expression value for the ignored time (only for manual mode)")=`None`*)[¶](#ApiClient.TriggerBlock.SetIgnoreFirst "Link to this definition")  
Sets whether at the start of each trigger range a quantity of samples should be excluded. Possible values for mode are: ‘disabled’, ‘manual’ or ‘firstsample’. In the latter mode the parameter ignoreTime will have no impact.

Parameters:  mode : str[¶](#ApiClient.TriggerBlock.SetIgnoreFirst.mode "Permalink to this definition")  
The mode for ignore first

ignoreTime : str[¶](#ApiClient.TriggerBlock.SetIgnoreFirst.ignoreTime "Permalink to this definition")  
The expression value for the ignored time (only for manual mode)

SetIgnoreLast(*[mode](#ApiClient.TriggerBlock.SetIgnoreLast.mode "ApiClient.TriggerBlock.SetIgnoreLast.mode (Python parameter) — The mode for ignore last")*, *[ignoreTime](#ApiClient.TriggerBlock.SetIgnoreLast.ignoreTime "ApiClient.TriggerBlock.SetIgnoreLast.ignoreTime (Python parameter) — The expression value for the ignored time (only for manual mode)")=`None`*)[¶](#ApiClient.TriggerBlock.SetIgnoreLast "Link to this definition")  
Sets whether at the end of each trigger range a certain time span parameterized by ignoreTime should be excluded. Possible values for mode are: ‘disabled’ or ‘manual’.

Parameters:  mode : str[¶](#ApiClient.TriggerBlock.SetIgnoreLast.mode "Permalink to this definition")  
The mode for ignore last

ignoreTime : str[¶](#ApiClient.TriggerBlock.SetIgnoreLast.ignoreTime "Permalink to this definition")  
The expression value for the ignored time (only for manual mode)

SetName(*[value](#ApiClient.TriggerBlock.SetName.value "ApiClient.TriggerBlock.SetName.value (Python parameter) — The new name")*)[¶](#ApiClient.TriggerBlock.SetName "Link to this definition")  
Sets the name of the trace analysis element.

Parameters:  value : str[¶](#ApiClient.TriggerBlock.SetName.value "Permalink to this definition")  
The new name

SetReportEntryLimit(*[maxEntryCount](#ApiClient.TriggerBlock.SetReportEntryLimit.maxEntryCount "ApiClient.TriggerBlock.SetReportEntryLimit.maxEntryCount (Python parameter) — The maximal number of entries per verdict as expression or None")*)[¶](#ApiClient.TriggerBlock.SetReportEntryLimit "Link to this definition")  
Sets the maximal number of entries per verdict and child the reporting shall be limited to. A value of None specifies that no limit shall be applied.

Parameters:  maxEntryCount : str[¶](#ApiClient.TriggerBlock.SetReportEntryLimit.maxEntryCount "Permalink to this definition")  
The maximal number of entries per verdict as expression or None

SetReportFilterCondition(*[condition](#ApiClient.TriggerBlock.SetReportFilterCondition.condition "ApiClient.TriggerBlock.SetReportFilterCondition.condition (Python parameter) — The report condition")*)[¶](#ApiClient.TriggerBlock.SetReportFilterCondition "Link to this definition")  
Sets the condition that must be matched for the trigger range to be reported. Possible values are: - ‘NONE’ (meaning no filtering for verdict types) - ‘SUCCESS’ (meaning SUCCESS or worse) - ‘INCONCLUSIVE’ (meaning INCONCLUSIVE or worse) - ‘FAILED’ (meaning FAILED or worse) - ‘ERROR’ (meaning ERROR)

Parameters:  condition : str[¶](#ApiClient.TriggerBlock.SetReportFilterCondition.condition "Permalink to this definition")  
The report condition

SetReportIgnoredRanges(*[reportRanges](#ApiClient.TriggerBlock.SetReportIgnoredRanges.reportRanges "ApiClient.TriggerBlock.SetReportIgnoredRanges.reportRanges (Python parameter) — If true, a range whose samples are completely left out due to the ignore times will be reported as NONE range. Otherwise it will not be reported.")*)[¶](#ApiClient.TriggerBlock.SetReportIgnoredRanges "Link to this definition")  
Sets whether ranges without a sample after consideration of the ignore times should be reported.

Parameters:  reportRanges : bool[¶](#ApiClient.TriggerBlock.SetReportIgnoredRanges.reportRanges "Permalink to this definition")  
If true, a range whose samples are completely left out due to the ignore times will be reported as NONE range. Otherwise it will not be reported.

SetReportOmittedStartTrigger(*[reportTrigger](#ApiClient.TriggerBlock.SetReportOmittedStartTrigger.reportTrigger "ApiClient.TriggerBlock.SetReportOmittedStartTrigger.reportTrigger (Python parameter) — If true, for every omitted start trigger of the mode 'start trigger while not stop trigger' a spot will be generated.")*)[¶](#ApiClient.TriggerBlock.SetReportOmittedStartTrigger "Link to this definition")  
Sets whether omitted start triggers will be reported.

Parameters:  reportTrigger : bool[¶](#ApiClient.TriggerBlock.SetReportOmittedStartTrigger.reportTrigger "Permalink to this definition")  
If true, for every omitted start trigger of the mode ‘start trigger while not stop trigger’ a spot will be generated.

SetResultNoMatch(*[result](#ApiClient.TriggerBlock.SetResultNoMatch.result "ApiClient.TriggerBlock.SetResultNoMatch.result (Python parameter) — The verdict of a trigger block without a trigger range")*)[¶](#ApiClient.TriggerBlock.SetResultNoMatch "Link to this definition")  
Sets the verdict of a trigger block that does not open any trigger range. Possible values: ‘NONE’, ‘SUCCESS’, ‘INCONCLUSIVE’, ‘FAILED’ or ‘ERROR’.

Parameters:  result : str[¶](#ApiClient.TriggerBlock.SetResultNoMatch.result "Permalink to this definition")  
The verdict of a trigger block without a trigger range

SetResultTruncatedRange(*[result](#ApiClient.TriggerBlock.SetResultTruncatedRange.result "ApiClient.TriggerBlock.SetResultTruncatedRange.result (Python parameter) — The verdict of a truncated trigger range")*)[¶](#ApiClient.TriggerBlock.SetResultTruncatedRange "Link to this definition")  
Sets the blanket verdict of a truncated trigger range. Possible values of verdicts: ‘NONE’, ‘SUCCESS’, ‘INCONCLUSIVE’, ‘FAILED’ or ‘ERROR’.

Set to None if truncated trigger ranges shall be evaluated normally

Parameters:  result : str[¶](#ApiClient.TriggerBlock.SetResultTruncatedRange.result "Permalink to this definition")  
The verdict of a truncated trigger range

SetStartOffset(*[startOffset](#ApiClient.TriggerBlock.SetStartOffset.startOffset "ApiClient.TriggerBlock.SetStartOffset.startOffset (Python parameter) — The start offset")*)[¶](#ApiClient.TriggerBlock.SetStartOffset "Link to this definition")  
Sets the start offset expression.

Parameters:  startOffset : str[¶](#ApiClient.TriggerBlock.SetStartOffset.startOffset "Permalink to this definition")  
The start offset

SetStartTrigger(*[startTrigger](#ApiClient.TriggerBlock.SetStartTrigger.startTrigger "ApiClient.TriggerBlock.SetStartTrigger.startTrigger (Python parameter) — The start trigger expression")*)[¶](#ApiClient.TriggerBlock.SetStartTrigger "Link to this definition")  
Sets the start trigger expression.

Parameters:  startTrigger : str[¶](#ApiClient.TriggerBlock.SetStartTrigger.startTrigger "Permalink to this definition")  
The start trigger expression

SetStopOffset(*[stopOffset](#ApiClient.TriggerBlock.SetStopOffset.stopOffset "ApiClient.TriggerBlock.SetStopOffset.stopOffset (Python parameter) — The start offset")*)[¶](#ApiClient.TriggerBlock.SetStopOffset "Link to this definition")  
Sets the stop offset expression.

Parameters:  stopOffset : str[¶](#ApiClient.TriggerBlock.SetStopOffset.stopOffset "Permalink to this definition")  
The start offset

SetStopTrigger(*[stopTrigger](#ApiClient.TriggerBlock.SetStopTrigger.stopTrigger "ApiClient.TriggerBlock.SetStopTrigger.stopTrigger (Python parameter) — The stop trigger expression")*)[¶](#ApiClient.TriggerBlock.SetStopTrigger "Link to this definition")  
Sets the stop trigger expression.

Parameters:  stopTrigger : str[¶](#ApiClient.TriggerBlock.SetStopTrigger.stopTrigger "Permalink to this definition")  
The stop trigger expression

SetTags(*[tags](#ApiClient.TriggerBlock.SetTags.tags "ApiClient.TriggerBlock.SetTags.tags (Python parameter) — The list of tags")*)[¶](#ApiClient.TriggerBlock.SetTags "Link to this definition")  
Set the list of tags for this step. The list of tags will be sorted and stored.

Parameters:  tags : list[str][¶](#ApiClient.TriggerBlock.SetTags.tags "Permalink to this definition")  
The list of tags

SetTriggerMode(*[triggerMode](#ApiClient.TriggerBlock.SetTriggerMode.triggerMode "ApiClient.TriggerBlock.SetTriggerMode.triggerMode (Python parameter) — The stop trigger expression")*)[¶](#ApiClient.TriggerBlock.SetTriggerMode "Link to this definition")  
Sets the trigger mode. Possible values for mode can be obtained by either of the constants:

- [`TriggerBlock.MODE_WHILE_STARTTRIGGER`](#ApiClient.TriggerBlock.MODE_WHILE_STARTTRIGGER "ApiClient.TriggerBlock.MODE_WHILE_STARTTRIGGER (Python attribute) — Returns the constant used to specify the expectation mode 'as long as start trigger is fulfilled'.")

- [`TriggerBlock.MODE_STARTTRIGGER_WHILE_NOT_STOPTRIGGER`](#ApiClient.TriggerBlock.MODE_STARTTRIGGER_WHILE_NOT_STOPTRIGGER "ApiClient.TriggerBlock.MODE_STARTTRIGGER_WHILE_NOT_STOPTRIGGER (Python attribute) — Returns the constant used to specify the expectation mode 'from start trigger as long as stop trigger is not fulfilled'.")

- [`TriggerBlock.MODE_STARTTRIGGER_TO_NEXT_STOPTRIGGER`](#ApiClient.TriggerBlock.MODE_STARTTRIGGER_TO_NEXT_STOPTRIGGER "ApiClient.TriggerBlock.MODE_STARTTRIGGER_TO_NEXT_STOPTRIGGER (Python attribute) — Returns the constant used to specify the expectation mode 'from start trigger until next time stop trigger is fulfilled'.")

- [`TriggerBlock.MODE_STARTTRIGGER_WITH_TIME_OFFSETS`](#ApiClient.TriggerBlock.MODE_STARTTRIGGER_WITH_TIME_OFFSETS "ApiClient.TriggerBlock.MODE_STARTTRIGGER_WITH_TIME_OFFSETS (Python attribute) — Returns the constant used to specify the expectation mode 'with time offset if start trigger is fulfilled'.")

Parameters:  triggerMode : str[¶](#ApiClient.TriggerBlock.SetTriggerMode.triggerMode "Permalink to this definition")  
The stop trigger expression

SetTriggerOnce(*[triggerOnce](#ApiClient.TriggerBlock.SetTriggerOnce.triggerOnce "ApiClient.TriggerBlock.SetTriggerOnce.triggerOnce (Python parameter) — If true, only the very first trigger range that is found will be analyzed.")*)[¶](#ApiClient.TriggerBlock.SetTriggerOnce "Link to this definition")  
Sets whether the trigger block should trigger once or repeatedly.

Parameters:  triggerOnce : bool[¶](#ApiClient.TriggerBlock.SetTriggerOnce.triggerOnce "Permalink to this definition")  
If true, only the very first trigger range that is found will be analyzed. Further ranges will be ignored.

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
