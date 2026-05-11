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

API for Project Components

[ AnalysisBindings ](AnalysisBindings.md)

[ AnalysisPackageCall ](AnalysisPackageCall.md)

[ AnalysisPackageMappingCall ](AnalysisPackageMappingCall.md)

[ ArtifactReference ](ArtifactReference.md)

[ AssignedSignal ](AssignedSignal.md)

[ ConfigChange ](ConfigChange.md)

[ GlobalConstants ](GlobalConstants.md)

[ MappingFiles ](MappingFiles.md)

[ PackageCall ](PackageCall.md)

[ PackageGenerator ](PackageGenerator.md)

[ PackageParameters ](PackageParameters.md)

[ ParameterGenerator ](ParameterGenerator.md)

[ ParameterSet ](ParameterSet.md)

[ ParameterSetAnalysisPackage ](ParameterSetAnalysisPackage.md)

[ ParameterSetBase ](ParameterSetBase.md)

[ ParameterSetMapping ](ParameterSetMapping.md)

[ ParameterSetRecordings ](ParameterSetRecordings.md)

[ ParameterVariationGeneratorComponent ](ParameterVariationGeneratorComponent.md)

[ ProjectCall ](ProjectCall.md)

[ ProjectComponent ](ProjectComponent.md)

[ ProjectFolder ](ProjectFolder.md)

[ ProjectGenerator ](ProjectGenerator.md)

SignalGroupReference [ SignalGroupReference ](#)

SignalGroupReference

- [C SignalGroupReference ](#ApiClient.SignalGroupReference)
  - [M AppendSignal ](#ApiClient.SignalGroupReference.AppendSignal)
  - [M AppendTraceFileSignal ](#ApiClient.SignalGroupReference.AppendTraceFileSignal)
  - [M Clear ](#ApiClient.SignalGroupReference.Clear)
  - [M Clone ](#ApiClient.SignalGroupReference.Clone)
  - [M GetName ](#ApiClient.SignalGroupReference.GetName)
  - [M GetSignals ](#ApiClient.SignalGroupReference.GetSignals)

[ StimulationPackageCall ](StimulationPackageCall.md)

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

SignalGroupReference

- [C SignalGroupReference ](#ApiClient.SignalGroupReference)
  - [M AppendSignal ](#ApiClient.SignalGroupReference.AppendSignal)
  - [M AppendTraceFileSignal ](#ApiClient.SignalGroupReference.AppendTraceFileSignal)
  - [M Clear ](#ApiClient.SignalGroupReference.Clear)
  - [M Clone ](#ApiClient.SignalGroupReference.Clone)
  - [M GetName ](#ApiClient.SignalGroupReference.GetName)
  - [M GetSignals ](#ApiClient.SignalGroupReference.GetSignals)

# SignalGroupReference[¶](#signalgroupreference "Link to this heading")

*class* SignalGroupReference[¶](#ApiClient.SignalGroupReference "Link to this definition")  
A signal group reference of the [`AnalysisBindings`](AnalysisBindings.md#ApiClient.AnalysisBindings "ApiClient.AnalysisBindings (Python class) — The configured bindings between a stimulation package and its attached analysis packages.") between a stimulation package and its attached analysis packages containing manually assigned signals.

AppendSignal(*[mappingItem](#ApiClient.SignalGroupReference.AppendSignal.mappingItem "ApiClient.SignalGroupReference.AppendSignal.mappingItem (Python parameter) — The mapping item whose information is used to create and append the manually assigned signal.")*)[¶](#ApiClient.SignalGroupReference.AppendSignal "Link to this definition")  
Assigns a signal to the signal group. The signal is defined by the given mapping item. Its name and target variable are adopted.

Mapping items can be created using the [`MappingApi`](../MappingApi.md#ApiClient.MappingApi "ApiClient.MappingApi (Python class) — PackageApi.MappingApi").

Parameters:  mappingItem[¶](#ApiClient.SignalGroupReference.AppendSignal.mappingItem "Permalink to this definition")  
The mapping item whose information is used to create and append the manually assigned signal.

AppendTraceFileSignal(*[referenceName](#ApiClient.SignalGroupReference.AppendTraceFileSignal.referenceName "ApiClient.SignalGroupReference.AppendTraceFileSignal.referenceName (Python parameter) — Name of the mapping item")*, *[targetPath](#ApiClient.SignalGroupReference.AppendTraceFileSignal.targetPath "ApiClient.SignalGroupReference.AppendTraceFileSignal.targetPath (Python parameter) — Path to the trace file signal to be accessed")*)[¶](#ApiClient.SignalGroupReference.AppendTraceFileSignal "Link to this definition")  
Convenience method that works like [`AppendSignal()`](#ApiClient.SignalGroupReference.AppendSignal "ApiClient.SignalGroupReference.AppendSignal (Python method) — Assigns a signal to the signal group. The signal is defined by the given mapping item. Its name and target variable are adopted.") without the necessity to create a mapping item first. Instead, referenceName and targetPath are passed directly to address a trace file signal.

Parameters:  referenceName : str[¶](#ApiClient.SignalGroupReference.AppendTraceFileSignal.referenceName "Permalink to this definition")  
Name of the mapping item

targetPath : str[¶](#ApiClient.SignalGroupReference.AppendTraceFileSignal.targetPath "Permalink to this definition")  
Path to the trace file signal to be accessed

Clear()[¶](#ApiClient.SignalGroupReference.Clear "Link to this definition")  
Removes all manually assigned signals from this signal group reference.

Clone()[¶](#ApiClient.SignalGroupReference.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`SignalGroupReference`](#ApiClient.SignalGroupReference "ApiClient.SignalGroupReference (Python class) — A signal group reference of the AnalysisBindings between a stimulation package and its attached analysis packages containing manually assigned signals.")

GetName()[¶](#ApiClient.SignalGroupReference.GetName "Link to this definition")  
Returns the name of the given signal group.

Returns:  Signal group name.

Return type:  str

GetSignals()[¶](#ApiClient.SignalGroupReference.GetSignals "Link to this definition")  
Returns all signals manually assigned to the given signal group reference.

Returns:  List of signals manually assigned to signal group reference.

Return type:  list[[`AssignedSignal`](AssignedSignal.md#ApiClient.AssignedSignal "ApiClient.AssignedSignal (Python class) — A signal assigned to a signal group reference.")]

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
