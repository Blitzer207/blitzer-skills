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

SignalBinding [ SignalBinding ](#)

SignalBinding

- [C SignalBinding ](#ApiClient.SignalBinding)
  - [M Clone ](#ApiClient.SignalBinding.Clone)
  - [M GetGenericSignal ](#ApiClient.SignalBinding.GetGenericSignal)
  - [M GetUnit ](#ApiClient.SignalBinding.GetUnit)
  - [M IsOptional ](#ApiClient.SignalBinding.IsOptional)
  - [M SetGenericSignal ](#ApiClient.SignalBinding.SetGenericSignal)
  - [M SetOptional ](#ApiClient.SignalBinding.SetOptional)
  - [M SetUnit ](#ApiClient.SignalBinding.SetUnit)

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

[ TriggerBlock ](TriggerBlock.md)

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

SignalBinding

- [C SignalBinding ](#ApiClient.SignalBinding)
  - [M Clone ](#ApiClient.SignalBinding.Clone)
  - [M GetGenericSignal ](#ApiClient.SignalBinding.GetGenericSignal)
  - [M GetUnit ](#ApiClient.SignalBinding.GetUnit)
  - [M IsOptional ](#ApiClient.SignalBinding.IsOptional)
  - [M SetGenericSignal ](#ApiClient.SignalBinding.SetGenericSignal)
  - [M SetOptional ](#ApiClient.SignalBinding.SetOptional)
  - [M SetUnit ](#ApiClient.SignalBinding.SetUnit)

# SignalBinding[¶](#signalbinding "Link to this heading")

*class* SignalBinding[¶](#ApiClient.SignalBinding "Link to this definition")  
Clone()[¶](#ApiClient.SignalBinding.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`SignalBinding`](#ApiClient.SignalBinding "ApiClient.SignalBinding (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")

GetGenericSignal()[¶](#ApiClient.SignalBinding.GetGenericSignal "Link to this definition")  
Get the bound generic signal.

Returns:  The generic signal. Can be None.

Return type:  [`GenericSignal`](GenericSignal.md#ApiClient.GenericSignal "ApiClient.GenericSignal (Python class) — TraceAnalysisApi.CreateGenericSignal")

GetUnit()[¶](#ApiClient.SignalBinding.GetUnit "Link to this definition")  
Returns the default unit that will be used if a trace step (e.g. a plot) uses this signal.

Returns:  The default unit (default: “don’t care”)

Return type:  str

IsOptional()[¶](#ApiClient.SignalBinding.IsOptional "Link to this definition")  
Checks whether the bound generic signal is optionally bound to a recording signal.

Note:  
The value True for this flag is only valid if the trace step template signal is marked as optional.

Returns:  True if it is optional, else False

Return type:  boolean

SetGenericSignal(*[genericSignal](#ApiClient.SignalBinding.SetGenericSignal.genericSignal "ApiClient.SignalBinding.SetGenericSignal.genericSignal (Python parameter) — The generic signal")*)[¶](#ApiClient.SignalBinding.SetGenericSignal "Link to this definition")  
Set a new generic signal to be bound.

Parameters:  genericSignal[¶](#ApiClient.SignalBinding.SetGenericSignal.genericSignal "Permalink to this definition")  
The generic signal

SetOptional(*[optional](#ApiClient.SignalBinding.SetOptional.optional "ApiClient.SignalBinding.SetOptional.optional (Python parameter) — The new value")*)[¶](#ApiClient.SignalBinding.SetOptional "Link to this definition")  
Set whether the bound generic signal is optionally bound to a recording signal.

Note:  
The value True for this flag is only valid if the trace step template signal is marked as optional.

Parameters:  optional : boolean[¶](#ApiClient.SignalBinding.SetOptional.optional "Permalink to this definition")  
The new value

SetUnit(*[unit](#ApiClient.SignalBinding.SetUnit.unit "ApiClient.SignalBinding.SetUnit.unit (Python parameter) — The default unit (default: "don't care").")*)[¶](#ApiClient.SignalBinding.SetUnit "Link to this definition")  
Set the default unit that will be used if a trace step (e.g. a plot) uses this signal.

Parameters:  unit : str[¶](#ApiClient.SignalBinding.SetUnit.unit "Permalink to this definition")  
The default unit (default: “don’t care”). Use None or ‘don’t care’ to set it to its default value.

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
