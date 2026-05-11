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

ExpectationModeOptions [ ExpectationModeOptions ](#)

ExpectationModeOptions

- [C ExpectationModeOptions ](#ApiClient.ExpectationModeOptions)
  - [M Clone ](#ApiClient.ExpectationModeOptions.Clone)
  - [M GetMinDuration ](#ApiClient.ExpectationModeOptions.GetMinDuration)
  - [M IsCumulated ](#ApiClient.ExpectationModeOptions.IsCumulated)
  - [M IsRelative ](#ApiClient.ExpectationModeOptions.IsRelative)
  - [M SetCumulated ](#ApiClient.ExpectationModeOptions.SetCumulated)
  - [M SetMinDuration ](#ApiClient.ExpectationModeOptions.SetMinDuration)
  - [M SetRelative ](#ApiClient.ExpectationModeOptions.SetRelative)

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

ExpectationModeOptions

- [C ExpectationModeOptions ](#ApiClient.ExpectationModeOptions)
  - [M Clone ](#ApiClient.ExpectationModeOptions.Clone)
  - [M GetMinDuration ](#ApiClient.ExpectationModeOptions.GetMinDuration)
  - [M IsCumulated ](#ApiClient.ExpectationModeOptions.IsCumulated)
  - [M IsRelative ](#ApiClient.ExpectationModeOptions.IsRelative)
  - [M SetCumulated ](#ApiClient.ExpectationModeOptions.SetCumulated)
  - [M SetMinDuration ](#ApiClient.ExpectationModeOptions.SetMinDuration)
  - [M SetRelative ](#ApiClient.ExpectationModeOptions.SetRelative)

# ExpectationModeOptions[¶](#expectationmodeoptions "Link to this heading")

*class* ExpectationModeOptions[¶](#ApiClient.ExpectationModeOptions "Link to this definition")  
Clone()[¶](#ApiClient.ExpectationModeOptions.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`ExpectationModeOptions`](#ApiClient.ExpectationModeOptions "ApiClient.ExpectationModeOptions (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")

GetMinDuration()[¶](#ApiClient.ExpectationModeOptions.GetMinDuration "Link to this definition")  
Returns the minimal duration.

Returns:  The minimal duration

Return type:  str

IsCumulated()[¶](#ApiClient.ExpectationModeOptions.IsCumulated "Link to this definition")  
Returns True if all successful range should be cumulated and evaluated against the expected minimum duration.

Returns:  True if all successful ranges should be cumulated, else False

Return type:  bool

IsRelative()[¶](#ApiClient.ExpectationModeOptions.IsRelative "Link to this definition")  
Returns True if the value for minimum duration is specified as a relative value given in percent.

Returns:  True if mimimum duration is a relative value, else False

Return type:  bool

SetCumulated(*[value](#ApiClient.ExpectationModeOptions.SetCumulated.value "ApiClient.ExpectationModeOptions.SetCumulated.value (Python parameter) — True if all the successful range should be cumulated, else False")*)[¶](#ApiClient.ExpectationModeOptions.SetCumulated "Link to this definition")  
Decides whether all the successful ranges should be cumulated.

Parameters:  value : boolean[¶](#ApiClient.ExpectationModeOptions.SetCumulated.value "Permalink to this definition")  
True if all the successful range should be cumulated, else False

SetMinDuration(*[minDuration](#ApiClient.ExpectationModeOptions.SetMinDuration.minDuration "ApiClient.ExpectationModeOptions.SetMinDuration.minDuration (Python parameter) — The expression for minimal duration.")*)[¶](#ApiClient.ExpectationModeOptions.SetMinDuration "Link to this definition")  
Sets the minimal duration.

Parameters:  minDuration : str[¶](#ApiClient.ExpectationModeOptions.SetMinDuration.minDuration "Permalink to this definition")  
The expression for minimal duration.

SetRelative(*[value](#ApiClient.ExpectationModeOptions.SetRelative.value "ApiClient.ExpectationModeOptions.SetRelative.value (Python parameter) — True if the value for mimimum duration is a relative value, else False")*)[¶](#ApiClient.ExpectationModeOptions.SetRelative "Link to this definition")  
Decides whether the value for minimum duration is given as a relative value given in percent.

Parameters:  value : boolean[¶](#ApiClient.ExpectationModeOptions.SetRelative.value "Permalink to this definition")  
True if the value for mimimum duration is a relative value, else False

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
