[ Internal APIs ](api.md)

[ Advanced operations of package variable types ](variabledatastructures.md)

[ Advanced properties of bus-related objects ](busdatastructures.md)

[ Bus related objects of trace analysis ](busdatastructuresTraceanalysis.md)

[ Advanced properties of diagnostics-related objects ](diagdatastructures.md)

[ Diagnostics related objects of trace analysis ](diagdatastructuresTraceanalysis.md)

[ Advanced properties of media-related objects ](mediadatastructures.md)

[ Advanced properties of DLT logging-related objects ](dltdatastructures.md)

[ COM API ](com-api.md)

[ REST API ](rest-api.md)

[ Report API ](apireport.md)

[ Object API ](objectApi.md)

Object API

[ API entry points ](objectApi.md#api-entry-points)

API entry points

[ API for Analysis Jobs ](AnalysisJobApi.md)

[ API for Artifacts ](ArtifactApi.md)

[ API for Project Components ](ComponentApi.md)

[ API for Configurations ](ConfigurationApi.md)

[ API for Expectations ](ExpectationApi.md)

[ API for Expressions ](ExpressionApi.md)

[ API for Global Mappings ](GlobalMappingApi.md)

[ API for Mappings ](MappingApi.md)

[ API for Multimedia Objects ](MultimediaApi.md)

[ API for Packages ](PackageApi.md)

[ API for Parameters ](ParameterApi.md)

[ API for Projects ](ProjectApi.md)

[ API for Relations ](RelationApi.md)

[ API for Reports ](ReportApi.md)

[ API for Report Filters ](ReportFilterApi.md)

[ API for Settings ](SettingsApi.md)

[ API for Signals ](SignalApi.md)

[ API for Signal Descriptions ](SignalDescriptionApi.md)

[ API for Signal Recordings ](SignalRecordingApi.md)

[ API for Symbols ](SymbolApi.md)

[ API for Test Steps ](TestStepApi.md)

[ API for Touch Inputs ](TouchInputApi.md)

[ API for Trace Analyses ](#)

API for Trace Analyses

- [ AnalysisBlock ](TraceAnalysisApi/AnalysisBlock.md)
- [ Assertion ](TraceAnalysisApi/Assertion.md)
- [ AutosarTimeSyncRecordingGroupInfo ](TraceAnalysisApi/AutosarTimeSyncRecordingGroupInfo.md)
- [ AutosarTimeSynchronization ](TraceAnalysisApi/AutosarTimeSynchronization.md)
- [ Calculation ](TraceAnalysisApi/Calculation.md)
- [ CaseDefNode ](TraceAnalysisApi/CaseDefNode.md)
- [ CrossCorrelationSynchronization ](TraceAnalysisApi/CrossCorrelationSynchronization.md)
- [ ElseNode ](TraceAnalysisApi/ElseNode.md)
- [ Episode ](TraceAnalysisApi/Episode.md)
- [ EqualEntry ](TraceAnalysisApi/EqualEntry.md)
- [ EqualnessMatchingSynchronization ](TraceAnalysisApi/EqualnessMatchingSynchronization.md)
- [ ExpectationModeOptions ](TraceAnalysisApi/ExpectationModeOptions.md)
- [ ExpectationSynchronization ](TraceAnalysisApi/ExpectationSynchronization.md)
- [ GenericSignal ](TraceAnalysisApi/GenericSignal.md)
- [ IfDef ](TraceAnalysisApi/IfDef.md)
- [ IfThenElse ](TraceAnalysisApi/IfThenElse.md)
- [ LeastSquaresSynchronization ](TraceAnalysisApi/LeastSquaresSynchronization.md)
- [ OffsetSynchronization ](TraceAnalysisApi/OffsetSynchronization.md)
- [ PackageBase ](TraceAnalysisApi/PackageBase.md)
- [ Plot ](TraceAnalysisApi/Plot.md)
- [ PlotAxis ](TraceAnalysisApi/PlotAxis.md)
- [ PlotCalculatedSignal ](TraceAnalysisApi/PlotCalculatedSignal.md)
- [ PlotSignal ](TraceAnalysisApi/PlotSignal.md)
- [ PlotSignalBase ](TraceAnalysisApi/PlotSignalBase.md)
- [ PlotSubConfig ](TraceAnalysisApi/PlotSubConfig.md)
- [ PlotSubPlot ](TraceAnalysisApi/PlotSubPlot.md)
- [ RecordingGroupBase ](TraceAnalysisApi/RecordingGroupBase.md)
- [ ReportConfig ](TraceAnalysisApi/ReportConfig.md)
- [ SignalBinding ](TraceAnalysisApi/SignalBinding.md)
- [ SignalRecording ](TraceAnalysisApi/SignalRecording.md)
- [ SwitchDefCase ](TraceAnalysisApi/SwitchDefCase.md)
- [ SyncConfig ](TraceAnalysisApi/SyncConfig.md)
- [ SyncExpectation ](TraceAnalysisApi/SyncExpectation.md)
- [ Synchronization ](TraceAnalysisApi/Synchronization.md)
- [ TemplateBasedTraceStep ](TraceAnalysisApi/TemplateBasedTraceStep.md)
- [ ThenNode ](TraceAnalysisApi/ThenNode.md)
- [ TraceAnalysis ](TraceAnalysisApi/TraceAnalysis.md)
- [ TraceAnalysisReference ](TraceAnalysisApi/TraceAnalysisReference.md)
- [ TraceAnalysisReferenceDeprecated ](TraceAnalysisApi/TraceAnalysisReferenceDeprecated.md)
- [ TraceStep ](TraceAnalysisApi/TraceStep.md)
- [ TraceStepContainer ](TraceAnalysisApi/TraceStepContainer.md)
- [ TriggerBlock ](TraceAnalysisApi/TriggerBlock.md)
- [ UtcTimestampSynchronization ](TraceAnalysisApi/UtcTimestampSynchronization.md)

API for Trace Analyses [ API for Trace Analyses ](#)

API for Trace Analyses

- [C TraceAnalysisApi ](#ApiClient.TraceAnalysisApi)
  - [M CreateAssertion ](#ApiClient.TraceAnalysisApi.CreateAssertion)
  - [M CreateBlock ](#ApiClient.TraceAnalysisApi.CreateBlock)
  - [M CreateCalculation ](#ApiClient.TraceAnalysisApi.CreateCalculation)
  - [M CreateEpisode ](#ApiClient.TraceAnalysisApi.CreateEpisode)
  - [M CreateGenericSignal ](#ApiClient.TraceAnalysisApi.CreateGenericSignal)
  - [M CreateIfDef ](#ApiClient.TraceAnalysisApi.CreateIfDef)
  - [M CreateIfThenElse ](#ApiClient.TraceAnalysisApi.CreateIfThenElse)
  - [M CreatePlot ](#ApiClient.TraceAnalysisApi.CreatePlot)
  - [M CreatePlotCalculatedSignal ](#ApiClient.TraceAnalysisApi.CreatePlotCalculatedSignal)
  - [M CreatePlotSignal ](#ApiClient.TraceAnalysisApi.CreatePlotSignal)
  - [M CreateSignalRecording ](#ApiClient.TraceAnalysisApi.CreateSignalRecording)
  - [M CreateSwitchDefCase ](#ApiClient.TraceAnalysisApi.CreateSwitchDefCase)
  - [M CreateTemplateBasedTraceStep ](#ApiClient.TraceAnalysisApi.CreateTemplateBasedTraceStep)
  - [M CreateTraceAnalysis ](#ApiClient.TraceAnalysisApi.CreateTraceAnalysis)
  - [M CreateTraceAnalysisReference ](#ApiClient.TraceAnalysisApi.CreateTraceAnalysisReference)
  - [M CreateTraceAnalysisReferenceFromMappingItem ](#ApiClient.TraceAnalysisApi.CreateTraceAnalysisReferenceFromMappingItem)
  - [M CreateTriggerBlock ](#ApiClient.TraceAnalysisApi.CreateTriggerBlock)
- [ AnalysisBlock ](TraceAnalysisApi/AnalysisBlock.md)
- [ Assertion ](TraceAnalysisApi/Assertion.md)
- [ AutosarTimeSyncRecordingGroupInfo ](TraceAnalysisApi/AutosarTimeSyncRecordingGroupInfo.md)
- [ AutosarTimeSynchronization ](TraceAnalysisApi/AutosarTimeSynchronization.md)
- [ Calculation ](TraceAnalysisApi/Calculation.md)
- [ CaseDefNode ](TraceAnalysisApi/CaseDefNode.md)
- [ CrossCorrelationSynchronization ](TraceAnalysisApi/CrossCorrelationSynchronization.md)
- [ ElseNode ](TraceAnalysisApi/ElseNode.md)
- [ Episode ](TraceAnalysisApi/Episode.md)
- [ EqualEntry ](TraceAnalysisApi/EqualEntry.md)
- [ EqualnessMatchingSynchronization ](TraceAnalysisApi/EqualnessMatchingSynchronization.md)
- [ ExpectationModeOptions ](TraceAnalysisApi/ExpectationModeOptions.md)
- [ ExpectationSynchronization ](TraceAnalysisApi/ExpectationSynchronization.md)
- [ GenericSignal ](TraceAnalysisApi/GenericSignal.md)
- [ IfDef ](TraceAnalysisApi/IfDef.md)
- [ IfThenElse ](TraceAnalysisApi/IfThenElse.md)
- [ LeastSquaresSynchronization ](TraceAnalysisApi/LeastSquaresSynchronization.md)
- [ OffsetSynchronization ](TraceAnalysisApi/OffsetSynchronization.md)
- [ PackageBase ](TraceAnalysisApi/PackageBase.md)
- [ Plot ](TraceAnalysisApi/Plot.md)
- [ PlotAxis ](TraceAnalysisApi/PlotAxis.md)
- [ PlotCalculatedSignal ](TraceAnalysisApi/PlotCalculatedSignal.md)
- [ PlotSignal ](TraceAnalysisApi/PlotSignal.md)
- [ PlotSignalBase ](TraceAnalysisApi/PlotSignalBase.md)
- [ PlotSubConfig ](TraceAnalysisApi/PlotSubConfig.md)
- [ PlotSubPlot ](TraceAnalysisApi/PlotSubPlot.md)
- [ RecordingGroupBase ](TraceAnalysisApi/RecordingGroupBase.md)
- [ ReportConfig ](TraceAnalysisApi/ReportConfig.md)
- [ SignalBinding ](TraceAnalysisApi/SignalBinding.md)
- [ SignalRecording ](TraceAnalysisApi/SignalRecording.md)
- [ SwitchDefCase ](TraceAnalysisApi/SwitchDefCase.md)
- [ SyncConfig ](TraceAnalysisApi/SyncConfig.md)
- [ SyncExpectation ](TraceAnalysisApi/SyncExpectation.md)
- [ Synchronization ](TraceAnalysisApi/Synchronization.md)
- [ TemplateBasedTraceStep ](TraceAnalysisApi/TemplateBasedTraceStep.md)
- [ ThenNode ](TraceAnalysisApi/ThenNode.md)
- [ TraceAnalysis ](TraceAnalysisApi/TraceAnalysis.md)
- [ TraceAnalysisReference ](TraceAnalysisApi/TraceAnalysisReference.md)
- [ TraceAnalysisReferenceDeprecated ](TraceAnalysisApi/TraceAnalysisReferenceDeprecated.md)
- [ TraceStep ](TraceAnalysisApi/TraceStep.md)
- [ TraceStepContainer ](TraceAnalysisApi/TraceStepContainer.md)
- [ TriggerBlock ](TraceAnalysisApi/TriggerBlock.md)
- [ UtcTimestampSynchronization ](TraceAnalysisApi/UtcTimestampSynchronization.md)

[ API for Trace Files ](TraceFileApi.md)

[ API for Trace Step Templates ](TraceStepTemplateApi.md)

[ API for Variables ](VariableApi.md)

[ API for Workspaces ](WorkspaceApi.md)

[ Trace Analysis API ](../TraceAnalysisAPI/index.md)

[ Generator APIs ](../generators/index.md)

[ Tools ](../tools/index.md)

[ User test management ](../userTestmanagement/index.md)

[ UserUtility API ](../user-utility/user-utility.md)

[ Utility Examples ](../user-utility/example-utilities.md)

API for Trace Analyses

- [C TraceAnalysisApi ](#ApiClient.TraceAnalysisApi)
  - [M CreateAssertion ](#ApiClient.TraceAnalysisApi.CreateAssertion)
  - [M CreateBlock ](#ApiClient.TraceAnalysisApi.CreateBlock)
  - [M CreateCalculation ](#ApiClient.TraceAnalysisApi.CreateCalculation)
  - [M CreateEpisode ](#ApiClient.TraceAnalysisApi.CreateEpisode)
  - [M CreateGenericSignal ](#ApiClient.TraceAnalysisApi.CreateGenericSignal)
  - [M CreateIfDef ](#ApiClient.TraceAnalysisApi.CreateIfDef)
  - [M CreateIfThenElse ](#ApiClient.TraceAnalysisApi.CreateIfThenElse)
  - [M CreatePlot ](#ApiClient.TraceAnalysisApi.CreatePlot)
  - [M CreatePlotCalculatedSignal ](#ApiClient.TraceAnalysisApi.CreatePlotCalculatedSignal)
  - [M CreatePlotSignal ](#ApiClient.TraceAnalysisApi.CreatePlotSignal)
  - [M CreateSignalRecording ](#ApiClient.TraceAnalysisApi.CreateSignalRecording)
  - [M CreateSwitchDefCase ](#ApiClient.TraceAnalysisApi.CreateSwitchDefCase)
  - [M CreateTemplateBasedTraceStep ](#ApiClient.TraceAnalysisApi.CreateTemplateBasedTraceStep)
  - [M CreateTraceAnalysis ](#ApiClient.TraceAnalysisApi.CreateTraceAnalysis)
  - [M CreateTraceAnalysisReference ](#ApiClient.TraceAnalysisApi.CreateTraceAnalysisReference)
  - [M CreateTraceAnalysisReferenceFromMappingItem ](#ApiClient.TraceAnalysisApi.CreateTraceAnalysisReferenceFromMappingItem)
  - [M CreateTriggerBlock ](#ApiClient.TraceAnalysisApi.CreateTriggerBlock)

# API for Trace Analyses[¶](#api-for-trace-analyses "Link to this heading")

Part of the [Object based program API](objectApi.md#objectapi).

*class* TraceAnalysisApi[¶](#ApiClient.TraceAnalysisApi "Link to this definition")  
Returned by

- [`PackageApi.TraceAnalysisApi`](PackageApi.md#ApiClient.PackageApi.TraceAnalysisApi "ApiClient.PackageApi.TraceAnalysisApi (Python attribute) — Returns the TraceAnalysisApi namespace.")

CreateAssertion(*[name](#ApiClient.TraceAnalysisApi.CreateAssertion.name "ApiClient.TraceAnalysisApi.CreateAssertion.name (Python parameter) — The name of newly created trace step")*, *[description](#ApiClient.TraceAnalysisApi.CreateAssertion.description "ApiClient.TraceAnalysisApi.CreateAssertion.description (Python parameter) — The description of newly created trace step")=`None`*)[¶](#ApiClient.TraceAnalysisApi.CreateAssertion "Link to this definition")  
Creates an assertion trace step.

Parameters:  name : str[¶](#ApiClient.TraceAnalysisApi.CreateAssertion.name "Permalink to this definition")  
The name of newly created trace step

description : str[¶](#ApiClient.TraceAnalysisApi.CreateAssertion.description "Permalink to this definition")  
The description of newly created trace step

Returns:  New trace analysis assertion step

Return type:  [`Assertion`](TraceAnalysisApi/Assertion.md#ApiClient.Assertion "ApiClient.Assertion (Python class) — TraceAnalysisApi.CreateAssertion")

CreateBlock(*[name](#ApiClient.TraceAnalysisApi.CreateBlock.name "ApiClient.TraceAnalysisApi.CreateBlock.name (Python parameter) — The name of newly created trace analysis")*, *[description](#ApiClient.TraceAnalysisApi.CreateBlock.description "ApiClient.TraceAnalysisApi.CreateBlock.description (Python parameter) — The description of newly created trace step")=`None`*)[¶](#ApiClient.TraceAnalysisApi.CreateBlock "Link to this definition")  
Creates a block.

Parameters:  name : str[¶](#ApiClient.TraceAnalysisApi.CreateBlock.name "Permalink to this definition")  
The name of newly created trace analysis

description : str[¶](#ApiClient.TraceAnalysisApi.CreateBlock.description "Permalink to this definition")  
The description of newly created trace step

Returns:  New block

Return type:  [`AnalysisBlock`](TraceAnalysisApi/AnalysisBlock.md#ApiClient.AnalysisBlock "ApiClient.AnalysisBlock (Python class) — TraceAnalysisApi.CreateBlock")

CreateCalculation(*[name](#ApiClient.TraceAnalysisApi.CreateCalculation.name "ApiClient.TraceAnalysisApi.CreateCalculation.name (Python parameter) — The name of newly created trace step")*, *[description](#ApiClient.TraceAnalysisApi.CreateCalculation.description "ApiClient.TraceAnalysisApi.CreateCalculation.description (Python parameter) — The description of newly created trace step")=`None`*)[¶](#ApiClient.TraceAnalysisApi.CreateCalculation "Link to this definition")  
Creates a calculation trace step.

Parameters:  name : str[¶](#ApiClient.TraceAnalysisApi.CreateCalculation.name "Permalink to this definition")  
The name of newly created trace step

description : str[¶](#ApiClient.TraceAnalysisApi.CreateCalculation.description "Permalink to this definition")  
The description of newly created trace step

Returns:  New trace analysis calculation step

Return type:  [`Calculation`](TraceAnalysisApi/Calculation.md#ApiClient.Calculation "ApiClient.Calculation (Python class) — TraceAnalysisApi.CreateCalculation")

CreateEpisode(*[name](#ApiClient.TraceAnalysisApi.CreateEpisode.name "ApiClient.TraceAnalysisApi.CreateEpisode.name (Python parameter) — The name of newly created episode")*, *[description](#ApiClient.TraceAnalysisApi.CreateEpisode.description "ApiClient.TraceAnalysisApi.CreateEpisode.description (Python parameter) — The description of newly created episode")=`None`*)[¶](#ApiClient.TraceAnalysisApi.CreateEpisode "Link to this definition")  
Creates an episode.

Parameters:  name : str[¶](#ApiClient.TraceAnalysisApi.CreateEpisode.name "Permalink to this definition")  
The name of newly created episode

description : str[¶](#ApiClient.TraceAnalysisApi.CreateEpisode.description "Permalink to this definition")  
The description of newly created episode

Returns:  New trace analysis episode

Return type:  [`Episode`](TraceAnalysisApi/Episode.md#ApiClient.Episode "ApiClient.Episode (Python class) — TraceAnalysisApi.CreateEpisode")

CreateGenericSignal(*[name](#ApiClient.TraceAnalysisApi.CreateGenericSignal.name "ApiClient.TraceAnalysisApi.CreateGenericSignal.name (Python parameter) — The name of the generic signal")*, *[description](#ApiClient.TraceAnalysisApi.CreateGenericSignal.description "ApiClient.TraceAnalysisApi.CreateGenericSignal.description (Python parameter) — The description of newly created generic signal")=`None`*)[¶](#ApiClient.TraceAnalysisApi.CreateGenericSignal "Link to this definition")  
Creates a generic signal to the trace analysis. The name must be python-conform!

Parameters:  name : str[¶](#ApiClient.TraceAnalysisApi.CreateGenericSignal.name "Permalink to this definition")  
The name of the generic signal

description : str[¶](#ApiClient.TraceAnalysisApi.CreateGenericSignal.description "Permalink to this definition")  
The description of newly created generic signal

Returns:  The new generic signal

Return type:  [`GenericSignal`](TraceAnalysisApi/GenericSignal.md#ApiClient.GenericSignal "ApiClient.GenericSignal (Python class) — TraceAnalysisApi.CreateGenericSignal")

CreateIfDef()[¶](#ApiClient.TraceAnalysisApi.CreateIfDef "Link to this definition")  
Creates an IfDef block.

Returns:  New trace analysis IfDef block

Return type:  [`IfDef`](TraceAnalysisApi/IfDef.md#ApiClient.IfDef "ApiClient.IfDef (Python class) — TraceAnalysisApi.CreateIfDef")

CreateIfThenElse()[¶](#ApiClient.TraceAnalysisApi.CreateIfThenElse "Link to this definition")  
Creates an IfThenElse block.

Returns:  New trace analysis IfThenElse block

Return type:  [`IfThenElse`](TraceAnalysisApi/IfThenElse.md#ApiClient.IfThenElse "ApiClient.IfThenElse (Python class) — TraceAnalysisApi.CreateIfThenElse")

CreatePlot(*[name](#ApiClient.TraceAnalysisApi.CreatePlot.name "ApiClient.TraceAnalysisApi.CreatePlot.name (Python parameter) — The name of newly created plot")*, *[description](#ApiClient.TraceAnalysisApi.CreatePlot.description "ApiClient.TraceAnalysisApi.CreatePlot.description (Python parameter) — The description of newly created plot")=`None`*)[¶](#ApiClient.TraceAnalysisApi.CreatePlot "Link to this definition")  
Creates a plot.

Parameters:  name : str[¶](#ApiClient.TraceAnalysisApi.CreatePlot.name "Permalink to this definition")  
The name of newly created plot

description : str[¶](#ApiClient.TraceAnalysisApi.CreatePlot.description "Permalink to this definition")  
The description of newly created plot

Returns:  New trace analysis plot

Return type:  [`Plot`](TraceAnalysisApi/Plot.md#ApiClient.Plot "ApiClient.Plot (Python class) — TraceAnalysisApi.CreatePlot")

CreatePlotCalculatedSignal(*[expression](#ApiClient.TraceAnalysisApi.CreatePlotCalculatedSignal.expression "ApiClient.TraceAnalysisApi.CreatePlotCalculatedSignal.expression (Python parameter) — The expression from which the signal will be calculated.")*, *[name](#ApiClient.TraceAnalysisApi.CreatePlotCalculatedSignal.name "ApiClient.TraceAnalysisApi.CreatePlotCalculatedSignal.name (Python parameter) — Display name in the plot (optional, otherwise expression string will be used).")=`''`*)[¶](#ApiClient.TraceAnalysisApi.CreatePlotCalculatedSignal "Link to this definition")  
Creates a calculated plot signal to be used for a plot ([`PlotCalculatedSignal`](TraceAnalysisApi/PlotCalculatedSignal.md#ApiClient.PlotCalculatedSignal "ApiClient.PlotCalculatedSignal (Python class) — TraceAnalysisApi.CreatePlotCalculatedSignal")).

Parameters:  expression : str[¶](#ApiClient.TraceAnalysisApi.CreatePlotCalculatedSignal.expression "Permalink to this definition")  
The expression from which the signal will be calculated.

name : str[¶](#ApiClient.TraceAnalysisApi.CreatePlotCalculatedSignal.name "Permalink to this definition")  
Display name in the plot (optional, otherwise expression string will be used).

Returns:  A calculated plot signal

Return type:  [`PlotCalculatedSignal`](TraceAnalysisApi/PlotCalculatedSignal.md#ApiClient.PlotCalculatedSignal "ApiClient.PlotCalculatedSignal (Python class) — TraceAnalysisApi.CreatePlotCalculatedSignal")

CreatePlotSignal(*[name](#ApiClient.TraceAnalysisApi.CreatePlotSignal.name "ApiClient.TraceAnalysisApi.CreatePlotSignal.name (Python parameter) — Name of the plot signal")*, *[signalType](#ApiClient.TraceAnalysisApi.CreatePlotSignal.signalType "ApiClient.TraceAnalysisApi.CreatePlotSignal.signalType (Python parameter) — Type of plot signal to be mapped (GENERIC, TRACESTEP)")=`'GENERIC'`*)[¶](#ApiClient.TraceAnalysisApi.CreatePlotSignal "Link to this definition")  
Creates a plot signal to be used for a plot ([`PlotSignal`](TraceAnalysisApi/PlotSignal.md#ApiClient.PlotSignal "ApiClient.PlotSignal (Python class) — TraceAnalysisApi.CreatePlotSignal")).

Parameters:  name : str[¶](#ApiClient.TraceAnalysisApi.CreatePlotSignal.name "Permalink to this definition")  
Name of the plot signal

signalType : str[¶](#ApiClient.TraceAnalysisApi.CreatePlotSignal.signalType "Permalink to this definition")  
Type of plot signal to be mapped (GENERIC, TRACESTEP)

Returns:  A plot signal

Return type:  [`PlotSignal`](TraceAnalysisApi/PlotSignal.md#ApiClient.PlotSignal "ApiClient.PlotSignal (Python class) — TraceAnalysisApi.CreatePlotSignal")

CreateSignalRecording(*[name](#ApiClient.TraceAnalysisApi.CreateSignalRecording.name "ApiClient.TraceAnalysisApi.CreateSignalRecording.name (Python parameter) — The name of newly created signal recording")=`None`*, *[description](#ApiClient.TraceAnalysisApi.CreateSignalRecording.description "ApiClient.TraceAnalysisApi.CreateSignalRecording.description (Python parameter) — The description of newly created signal recording")=`None`*)[¶](#ApiClient.TraceAnalysisApi.CreateSignalRecording "Link to this definition")  
Creates a signal recording step.

Parameters:  name : str[¶](#ApiClient.TraceAnalysisApi.CreateSignalRecording.name "Permalink to this definition")  
The name of newly created signal recording

description : str[¶](#ApiClient.TraceAnalysisApi.CreateSignalRecording.description "Permalink to this definition")  
The description of newly created signal recording

Returns:  New trace analysis signal recording step

Return type:  [`SignalRecording`](TraceAnalysisApi/SignalRecording.md#ApiClient.SignalRecording "ApiClient.SignalRecording (Python class) — TraceAnalysisApi.CreateSignalRecording")

CreateSwitchDefCase()[¶](#ApiClient.TraceAnalysisApi.CreateSwitchDefCase "Link to this definition")  
Creates a SwitchDefCase block.

Returns:  New trace analysis SwitchDefCase block

Return type:  [`SwitchDefCase`](TraceAnalysisApi/SwitchDefCase.md#ApiClient.SwitchDefCase "ApiClient.SwitchDefCase (Python class) — TraceAnalysisApi.CreateSwitchDefCase")

CreateTemplateBasedTraceStep(*[name](#ApiClient.TraceAnalysisApi.CreateTemplateBasedTraceStep.name "ApiClient.TraceAnalysisApi.CreateTemplateBasedTraceStep.name (Python parameter) — The name of the newly created trace step.")=`None`*, *[description](#ApiClient.TraceAnalysisApi.CreateTemplateBasedTraceStep.description "ApiClient.TraceAnalysisApi.CreateTemplateBasedTraceStep.description (Python parameter) — The description of the newly created trace step")=`None`*)[¶](#ApiClient.TraceAnalysisApi.CreateTemplateBasedTraceStep "Link to this definition")  
Creates a trace step that references a trace step template.

Note:  
After creation the template reference has to be set by calling [`TemplateBasedTraceStep.SetTemplate()`](TraceAnalysisApi/TemplateBasedTraceStep.md#ApiClient.TemplateBasedTraceStep.SetTemplate "ApiClient.TemplateBasedTraceStep.SetTemplate (Python method) — Sets the referenced trace step template via object.")!

Parameters:  name : str[¶](#ApiClient.TraceAnalysisApi.CreateTemplateBasedTraceStep.name "Permalink to this definition")  
The name of the newly created trace step. If None, the trace step template name will be used.

description : str[¶](#ApiClient.TraceAnalysisApi.CreateTemplateBasedTraceStep.description "Permalink to this definition")  
The description of the newly created trace step

Returns:  New template based trace step

Return type:  [`TemplateBasedTraceStep`](TraceAnalysisApi/TemplateBasedTraceStep.md#ApiClient.TemplateBasedTraceStep "ApiClient.TemplateBasedTraceStep (Python class) — TraceAnalysisApi.CreateTemplateBasedTraceStep")

CreateTraceAnalysis(*[name](#ApiClient.TraceAnalysisApi.CreateTraceAnalysis.name "ApiClient.TraceAnalysisApi.CreateTraceAnalysis.name (Python parameter) — The name of newly created trace analysis")*, *[description](#ApiClient.TraceAnalysisApi.CreateTraceAnalysis.description "ApiClient.TraceAnalysisApi.CreateTraceAnalysis.description (Python parameter) — The description of newly created trace step")=`None`*)[¶](#ApiClient.TraceAnalysisApi.CreateTraceAnalysis "Link to this definition")  
Creates a trace analysis.

Parameters:  name : str[¶](#ApiClient.TraceAnalysisApi.CreateTraceAnalysis.name "Permalink to this definition")  
The name of newly created trace analysis

description : str[¶](#ApiClient.TraceAnalysisApi.CreateTraceAnalysis.description "Permalink to this definition")  
The description of newly created trace step

Returns:  New trace analysis

Return type:  [`TraceAnalysis`](TraceAnalysisApi/TraceAnalysis.md#ApiClient.TraceAnalysis "ApiClient.TraceAnalysis (Python class) — TraceAnalysisApi.CreateTraceAnalysis")

CreateTraceAnalysisReference(*[name](#ApiClient.TraceAnalysisApi.CreateTraceAnalysisReference.name "ApiClient.TraceAnalysisApi.CreateTraceAnalysisReference.name (Python parameter) — The name of newly created trace analysis reference")*, *[description](#ApiClient.TraceAnalysisApi.CreateTraceAnalysisReference.description "ApiClient.TraceAnalysisApi.CreateTraceAnalysisReference.description (Python parameter) — The description of newly created trace analysis reference")=`None`*)[¶](#ApiClient.TraceAnalysisApi.CreateTraceAnalysisReference "Link to this definition")  
Creates a reference to another trace analysis of a different package that works like an episode.

Parameters:  name : str[¶](#ApiClient.TraceAnalysisApi.CreateTraceAnalysisReference.name "Permalink to this definition")  
The name of newly created trace analysis reference

description : str[¶](#ApiClient.TraceAnalysisApi.CreateTraceAnalysisReference.description "Permalink to this definition")  
The description of newly created trace analysis reference

Returns:  New trace analysis reference

Return type:  [`TraceAnalysisReference`](TraceAnalysisApi/TraceAnalysisReference.md#ApiClient.TraceAnalysisReference "ApiClient.TraceAnalysisReference (Python class) — Most methods of the TraceAnalysisReference can only be used if it is assigned to a package.")

CreateTraceAnalysisReferenceFromMappingItem(*[mappingItem](#ApiClient.TraceAnalysisApi.CreateTraceAnalysisReferenceFromMappingItem.mappingItem "ApiClient.TraceAnalysisApi.CreateTraceAnalysisReferenceFromMappingItem.mappingItem (Python parameter) — The mapping item referencing the analysis package")*)[¶](#ApiClient.TraceAnalysisApi.CreateTraceAnalysisReferenceFromMappingItem "Link to this definition")  
Creates a reference to another trace analysis of a different package that works like an episode, referenced in the given mappingItem.

Parameters:  mappingItem[¶](#ApiClient.TraceAnalysisApi.CreateTraceAnalysisReferenceFromMappingItem.mappingItem "Permalink to this definition")  
The mapping item referencing the analysis package

Returns:  New trace analysis reference

Return type:  [`TraceAnalysisReference`](TraceAnalysisApi/TraceAnalysisReference.md#ApiClient.TraceAnalysisReference "ApiClient.TraceAnalysisReference (Python class) — Most methods of the TraceAnalysisReference can only be used if it is assigned to a package.")

CreateTriggerBlock(*[name](#ApiClient.TraceAnalysisApi.CreateTriggerBlock.name "ApiClient.TraceAnalysisApi.CreateTriggerBlock.name (Python parameter) — The name of newly created trace step")*, *[description](#ApiClient.TraceAnalysisApi.CreateTriggerBlock.description "ApiClient.TraceAnalysisApi.CreateTriggerBlock.description (Python parameter) — The description of newly created trace step")=`None`*)[¶](#ApiClient.TraceAnalysisApi.CreateTriggerBlock "Link to this definition")  
Creates a trigger block.

Parameters:  name : str[¶](#ApiClient.TraceAnalysisApi.CreateTriggerBlock.name "Permalink to this definition")  
The name of newly created trace step

description : str[¶](#ApiClient.TraceAnalysisApi.CreateTriggerBlock.description "Permalink to this definition")  
The description of newly created trace step

Returns:  New trigger block

Return type:  [`TriggerBlock`](TraceAnalysisApi/TriggerBlock.md#ApiClient.TriggerBlock "ApiClient.TriggerBlock (Python class) — TraceAnalysisApi.CreateTriggerBlock")

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
