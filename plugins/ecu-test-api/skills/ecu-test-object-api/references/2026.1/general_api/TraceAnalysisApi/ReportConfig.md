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

ReportConfig [ ReportConfig ](#)

ReportConfig

- [C ReportConfig ](#ApiClient.ReportConfig)
  - [M Clone ](#ApiClient.ReportConfig.Clone)
  - [M GetMaxSpots ](#ApiClient.ReportConfig.GetMaxSpots)
  - [M GetMinDelta ](#ApiClient.ReportConfig.GetMinDelta)
  - [M GetResultDetailsVariable ](#ApiClient.ReportConfig.GetResultDetailsVariable)
  - [M SetMaxSpots ](#ApiClient.ReportConfig.SetMaxSpots)
  - [M SetMinDelta ](#ApiClient.ReportConfig.SetMinDelta)
  - [M SetResultDetailsVariable ](#ApiClient.ReportConfig.SetResultDetailsVariable)

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

ReportConfig

- [C ReportConfig ](#ApiClient.ReportConfig)
  - [M Clone ](#ApiClient.ReportConfig.Clone)
  - [M GetMaxSpots ](#ApiClient.ReportConfig.GetMaxSpots)
  - [M GetMinDelta ](#ApiClient.ReportConfig.GetMinDelta)
  - [M GetResultDetailsVariable ](#ApiClient.ReportConfig.GetResultDetailsVariable)
  - [M SetMaxSpots ](#ApiClient.ReportConfig.SetMaxSpots)
  - [M SetMinDelta ](#ApiClient.ReportConfig.SetMinDelta)
  - [M SetResultDetailsVariable ](#ApiClient.ReportConfig.SetResultDetailsVariable)

# ReportConfig[¶](#reportconfig "Link to this heading")

*class* ReportConfig[¶](#ApiClient.ReportConfig "Link to this definition")  
Clone()[¶](#ApiClient.ReportConfig.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`ReportConfig`](#ApiClient.ReportConfig "ApiClient.ReportConfig (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")

GetMaxSpots()[¶](#ApiClient.ReportConfig.GetMaxSpots "Link to this definition")  
Get how many spots or ranges will be reported.

Returns:  Number of spots or ranges to be reported

Return type:  int

GetMinDelta()[¶](#ApiClient.ReportConfig.GetMinDelta "Link to this definition")  
Get the minimum duration between reported spots or ranges.

Returns:  Minimum duration between reported spots or ranges

Return type:  float

GetResultDetailsVariable()[¶](#ApiClient.ReportConfig.GetResultDetailsVariable "Link to this definition")  
Get the name of the package variable result details will be written to.

Returns:  Name of the result details variable. None if not set.

Return type:  str

SetMaxSpots(*[maxSpots](#ApiClient.ReportConfig.SetMaxSpots.maxSpots "ApiClient.ReportConfig.SetMaxSpots.maxSpots (Python parameter) — Number of spots or ranges to be reported (defaults to 100)")*)[¶](#ApiClient.ReportConfig.SetMaxSpots "Link to this definition")  
Sets how many spots or ranges will be reported.

Parameters:  maxSpots : int[¶](#ApiClient.ReportConfig.SetMaxSpots.maxSpots "Permalink to this definition")  
Number of spots or ranges to be reported (defaults to 100)

SetMinDelta(*[minDelta](#ApiClient.ReportConfig.SetMinDelta.minDelta "ApiClient.ReportConfig.SetMinDelta.minDelta (Python parameter) — Minimum duration between reported spots or ranges (defaults to 0.0)")*)[¶](#ApiClient.ReportConfig.SetMinDelta "Link to this definition")  
Sets the minimum duration between reported spots or ranges.

Parameters:  minDelta : float[¶](#ApiClient.ReportConfig.SetMinDelta.minDelta "Permalink to this definition")  
Minimum duration between reported spots or ranges (defaults to 0.0)

SetResultDetailsVariable(*[varName](#ApiClient.ReportConfig.SetResultDetailsVariable.varName "ApiClient.ReportConfig.SetResultDetailsVariable.varName (Python parameter) — Name of the result details variable.")*)[¶](#ApiClient.ReportConfig.SetResultDetailsVariable "Link to this definition")  
Sets the name of the package variable result details will be written to.

Parameters:  varName : str[¶](#ApiClient.ReportConfig.SetResultDetailsVariable.varName "Permalink to this definition")  
Name of the result details variable. None to set no variable.

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
