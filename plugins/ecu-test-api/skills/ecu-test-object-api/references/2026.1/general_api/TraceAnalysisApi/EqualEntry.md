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

EqualEntry [ EqualEntry ](#)

EqualEntry

- [C EqualEntry ](#ApiClient.EqualEntry)
  - [M Clone ](#ApiClient.EqualEntry.Clone)
  - [M GetEventType ](#ApiClient.EqualEntry.GetEventType)
  - [M GetMasterName ](#ApiClient.EqualEntry.GetMasterName)
  - [M GetName ](#ApiClient.EqualEntry.GetName)
  - [M SetEventType ](#ApiClient.EqualEntry.SetEventType)
  - [M SetMasterName ](#ApiClient.EqualEntry.SetMasterName)
  - [M SetName ](#ApiClient.EqualEntry.SetName)

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

EqualEntry

- [C EqualEntry ](#ApiClient.EqualEntry)
  - [M Clone ](#ApiClient.EqualEntry.Clone)
  - [M GetEventType ](#ApiClient.EqualEntry.GetEventType)
  - [M GetMasterName ](#ApiClient.EqualEntry.GetMasterName)
  - [M GetName ](#ApiClient.EqualEntry.GetName)
  - [M SetEventType ](#ApiClient.EqualEntry.SetEventType)
  - [M SetMasterName ](#ApiClient.EqualEntry.SetMasterName)
  - [M SetName ](#ApiClient.EqualEntry.SetName)

# EqualEntry[¶](#equalentry "Link to this heading")

*class* EqualEntry[¶](#ApiClient.EqualEntry "Link to this definition")  
Clone()[¶](#ApiClient.EqualEntry.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`EqualEntry`](#ApiClient.EqualEntry "ApiClient.EqualEntry (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")

GetEventType()[¶](#ApiClient.EqualEntry.GetEventType "Link to this definition")  
Return the event type for this equalness matching. Possible values are ‘RAW’, ‘PHY’, and ‘STR’.

Returns:  The event type

Return type:  str

GetMasterName()[¶](#ApiClient.EqualEntry.GetMasterName "Link to this definition")  
Returns the signal name of the selected master recording group that is used for the equalness synchronization.

Returns:  The signal name

Return type:  str

GetName()[¶](#ApiClient.EqualEntry.GetName "Link to this definition")  
Returns the signal name of the associated recording group that is used for the equalness synchronization.

Returns:  The signal name

Return type:  str

SetEventType(*[eventType](#ApiClient.EqualEntry.SetEventType.eventType "ApiClient.EqualEntry.SetEventType.eventType (Python parameter) — Type of event: 'RAW', 'PHY', or 'STR'")*)[¶](#ApiClient.EqualEntry.SetEventType "Link to this definition")  
Sets the event type to use for this equalness matching.

Parameters:  eventType : str[¶](#ApiClient.EqualEntry.SetEventType.eventType "Permalink to this definition")  
Type of event: ‘RAW’, ‘PHY’, or ‘STR’

SetMasterName(*[masterName](#ApiClient.EqualEntry.SetMasterName.masterName "ApiClient.EqualEntry.SetMasterName.masterName (Python parameter) — The name of the signal")*)[¶](#ApiClient.EqualEntry.SetMasterName "Link to this definition")  
Sets the signal (by name) of the selected master recording group to use for the equalness synchronization.

Parameters:  masterName : str[¶](#ApiClient.EqualEntry.SetMasterName.masterName "Permalink to this definition")  
The name of the signal

SetName(*[name](#ApiClient.EqualEntry.SetName.name "ApiClient.EqualEntry.SetName.name (Python parameter) — The name of the signal")*)[¶](#ApiClient.EqualEntry.SetName "Link to this definition")  
Sets the signal (by name) of the associated recording group to use for the equalness synchronization.

Parameters:  name : str[¶](#ApiClient.EqualEntry.SetName.name "Permalink to this definition")  
The name of the signal

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
