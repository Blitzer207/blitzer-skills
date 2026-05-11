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

AssignedSignal [ AssignedSignal ](#)

AssignedSignal

- [C AssignedSignal ](#ApiClient.AssignedSignal)
  - [M Clone ](#ApiClient.AssignedSignal.Clone)
  - [M GetAccessType ](#ApiClient.AssignedSignal.GetAccessType)
  - [M GetDisplayedType ](#ApiClient.AssignedSignal.GetDisplayedType)
  - [M GetReferenceName ](#ApiClient.AssignedSignal.GetReferenceName)
  - [M GetSystemIdentifier ](#ApiClient.AssignedSignal.GetSystemIdentifier)
  - [M GetTargetPath ](#ApiClient.AssignedSignal.GetTargetPath)
  - [M GetVariableType ](#ApiClient.AssignedSignal.GetVariableType)

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

AssignedSignal

- [C AssignedSignal ](#ApiClient.AssignedSignal)
  - [M Clone ](#ApiClient.AssignedSignal.Clone)
  - [M GetAccessType ](#ApiClient.AssignedSignal.GetAccessType)
  - [M GetDisplayedType ](#ApiClient.AssignedSignal.GetDisplayedType)
  - [M GetReferenceName ](#ApiClient.AssignedSignal.GetReferenceName)
  - [M GetSystemIdentifier ](#ApiClient.AssignedSignal.GetSystemIdentifier)
  - [M GetTargetPath ](#ApiClient.AssignedSignal.GetTargetPath)
  - [M GetVariableType ](#ApiClient.AssignedSignal.GetVariableType)

# AssignedSignal[¶](#assignedsignal "Link to this heading")

*class* AssignedSignal[¶](#ApiClient.AssignedSignal "Link to this definition")  
A signal assigned to a signal group reference.

Clone()[¶](#ApiClient.AssignedSignal.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`AssignedSignal`](#ApiClient.AssignedSignal "ApiClient.AssignedSignal (Python class) — A signal assigned to a signal group reference.")

GetAccessType()[¶](#ApiClient.AssignedSignal.GetAccessType "Link to this definition")  
Returns a string identifying the mapping item’s type. (such as MODEL, BUS, MEASUREMENT, …)

Returns:  access type

Return type:  str

GetDisplayedType()[¶](#ApiClient.AssignedSignal.GetDisplayedType "Link to this definition")  
Returns a “nice” representation of the type as displayed in the “type” column of the mapping panel

Returns:  the displayed mapping type

Return type:  str

GetReferenceName()[¶](#ApiClient.AssignedSignal.GetReferenceName "Link to this definition")  
Returns the reference name of mapping corresponding to the assigned signal.

Returns:  The reference name of the mapping

Return type:  str

GetSystemIdentifier()[¶](#ApiClient.AssignedSignal.GetSystemIdentifier "Link to this definition")  
Returns the system identifier providing the currently mapped test quantity

Returns:  system identifier

Return type:  str

GetTargetPath()[¶](#ApiClient.AssignedSignal.GetTargetPath "Link to this definition")  
Returns the path this mapping item is currently pointing at

Returns:  complete path to the destination test quantity

Return type:  str

GetVariableType()[¶](#ApiClient.AssignedSignal.GetVariableType "Link to this definition")  
Returns the type of the target variable or None if target has no type.

Returns:  The type of the target variable. (e.g. VALUE, MATRIX, CURVE, …)

Return type:  str

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
