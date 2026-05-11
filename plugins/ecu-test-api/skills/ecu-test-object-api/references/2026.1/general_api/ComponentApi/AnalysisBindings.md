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

AnalysisBindings [ AnalysisBindings ](#)

AnalysisBindings

- [C AnalysisBindings ](#ApiClient.AnalysisBindings)
  - [M AddSignalGroupReference ](#ApiClient.AnalysisBindings.AddSignalGroupReference)
  - [M Clone ](#ApiClient.AnalysisBindings.Clone)
  - [M GetAvailableSignalGroupNames ](#ApiClient.AnalysisBindings.GetAvailableSignalGroupNames)
  - [M GetSignalGroupReference ](#ApiClient.AnalysisBindings.GetSignalGroupReference)
  - [M GetSignalGroupReferences ](#ApiClient.AnalysisBindings.GetSignalGroupReferences)

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

[ SignalGroupReference ](SignalGroupReference.md)

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

AnalysisBindings

- [C AnalysisBindings ](#ApiClient.AnalysisBindings)
  - [M AddSignalGroupReference ](#ApiClient.AnalysisBindings.AddSignalGroupReference)
  - [M Clone ](#ApiClient.AnalysisBindings.Clone)
  - [M GetAvailableSignalGroupNames ](#ApiClient.AnalysisBindings.GetAvailableSignalGroupNames)
  - [M GetSignalGroupReference ](#ApiClient.AnalysisBindings.GetSignalGroupReference)
  - [M GetSignalGroupReferences ](#ApiClient.AnalysisBindings.GetSignalGroupReferences)

# AnalysisBindings[¶](#analysisbindings "Link to this heading")

*class* AnalysisBindings[¶](#ApiClient.AnalysisBindings "Link to this definition")  
The configured bindings between a stimulation package and its attached analysis packages.

AddSignalGroupReference(*[signalGroupName](#ApiClient.AnalysisBindings.AddSignalGroupReference.signalGroupName "ApiClient.AnalysisBindings.AddSignalGroupReference.signalGroupName (Python parameter) — Name of the signal group to be referenced.")*)[¶](#ApiClient.AnalysisBindings.AddSignalGroupReference "Link to this definition")  
Adds a signal group reference.

Note: It is only necessary to add signal group references and manually assign a signal if the signal cannot be assigned automatically (e.g. signals of type trace file).

Parameters:  signalGroupName : str[¶](#ApiClient.AnalysisBindings.AddSignalGroupReference.signalGroupName "Permalink to this definition")  
Name of the signal group to be referenced.

Clone()[¶](#ApiClient.AnalysisBindings.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`AnalysisBindings`](#ApiClient.AnalysisBindings "ApiClient.AnalysisBindings (Python class) — The configured bindings between a stimulation package and its attached analysis packages.")

GetAvailableSignalGroupNames()[¶](#ApiClient.AnalysisBindings.GetAvailableSignalGroupNames "Link to this definition")  
Returns all available signal group names of the stimulation package step that can be referenced. The returned list includes the names of regular signal groups, the test case variable group (if active) and generated signal groups from event stores in trace analyses.

Returns:  The list of available signal group names that can be referenced.

Return type:  list[str]

GetSignalGroupReference(*[signalGroupName](#ApiClient.AnalysisBindings.GetSignalGroupReference.signalGroupName "ApiClient.AnalysisBindings.GetSignalGroupReference.signalGroupName (Python parameter) — Name of the desired signal group reference.")*)[¶](#ApiClient.AnalysisBindings.GetSignalGroupReference "Link to this definition")  
Returns the reference to the given signal group.

Parameters:  signalGroupName : str[¶](#ApiClient.AnalysisBindings.GetSignalGroupReference.signalGroupName "Permalink to this definition")  
Name of the desired signal group reference.

Returns:  Desired signal group reference.

Return type:  [`SignalGroupReference`](SignalGroupReference.md#ApiClient.SignalGroupReference "ApiClient.SignalGroupReference (Python class) — A signal group reference of the AnalysisBindings between a stimulation package and its attached analysis packages containing manually assigned signals.")

GetSignalGroupReferences()[¶](#ApiClient.AnalysisBindings.GetSignalGroupReferences "Link to this definition")  
Returns all signal group references of the analysis binding.

Returns:  Signal group references

Return type:  list[[`SignalGroupReference`](SignalGroupReference.md#ApiClient.SignalGroupReference "ApiClient.SignalGroupReference (Python class) — A signal group reference of the AnalysisBindings between a stimulation package and its attached analysis packages containing manually assigned signals.")]

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
