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

ParameterSetMapping [ ParameterSetMapping ](#)

ParameterSetMapping

- [C ParameterSetMapping ](#ApiClient.ParameterSetMapping)
  - [M Clone ](#ApiClient.ParameterSetMapping.Clone)
  - [M CreateAlternativeMapping ](#ApiClient.ParameterSetMapping.CreateAlternativeMapping)
  - [M GetAlternativeMapping ](#ApiClient.ParameterSetMapping.GetAlternativeMapping)
  - [M GetMappingFromPackage ](#ApiClient.ParameterSetMapping.GetMappingFromPackage)
  - [M HasAlternativeMapping ](#ApiClient.ParameterSetMapping.HasAlternativeMapping)
  - [M RemoveAlternativeMapping ](#ApiClient.ParameterSetMapping.RemoveAlternativeMapping)
  - [M SetAlternativeMapping ](#ApiClient.ParameterSetMapping.SetAlternativeMapping)

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

ParameterSetMapping

- [C ParameterSetMapping ](#ApiClient.ParameterSetMapping)
  - [M Clone ](#ApiClient.ParameterSetMapping.Clone)
  - [M CreateAlternativeMapping ](#ApiClient.ParameterSetMapping.CreateAlternativeMapping)
  - [M GetAlternativeMapping ](#ApiClient.ParameterSetMapping.GetAlternativeMapping)
  - [M GetMappingFromPackage ](#ApiClient.ParameterSetMapping.GetMappingFromPackage)
  - [M HasAlternativeMapping ](#ApiClient.ParameterSetMapping.HasAlternativeMapping)
  - [M RemoveAlternativeMapping ](#ApiClient.ParameterSetMapping.RemoveAlternativeMapping)
  - [M SetAlternativeMapping ](#ApiClient.ParameterSetMapping.SetAlternativeMapping)

# ParameterSetMapping[¶](#parametersetmapping "Link to this heading")

*class* ParameterSetMapping[¶](#ApiClient.ParameterSetMapping "Link to this definition")  
Clone()[¶](#ApiClient.ParameterSetMapping.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`ParameterSetMapping`](#ApiClient.ParameterSetMapping "ApiClient.ParameterSetMapping (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")

CreateAlternativeMapping()[¶](#ApiClient.ParameterSetMapping.CreateAlternativeMapping "Link to this definition")  
Creates an empty mapping within the parameter set. If the parameter set already has an alternative mapping, it will be replaced.

Returns:  The mapping

Return type:  [`Mapping`](../AnalysisJobApi/Mapping.md#ApiClient.Mapping "ApiClient.Mapping (Python class) — Adds a mapping item to the mapping.")

GetAlternativeMapping()[¶](#ApiClient.ParameterSetMapping.GetAlternativeMapping "Link to this definition")  
Returns the alternative mapping of the parameter set or None if no the parameter set does not have an alternative mapping.

Returns:  The mapping

Return type:  [`Mapping`](../AnalysisJobApi/Mapping.md#ApiClient.Mapping "ApiClient.Mapping (Python class) — Adds a mapping item to the mapping.")

GetMappingFromPackage()[¶](#ApiClient.ParameterSetMapping.GetMappingFromPackage "Link to this definition")  
Returns the mapping of the package.

Returns:  Mapping to be set

Return type:  [`Mapping`](../AnalysisJobApi/Mapping.md#ApiClient.Mapping "ApiClient.Mapping (Python class) — Adds a mapping item to the mapping.")

HasAlternativeMapping()[¶](#ApiClient.ParameterSetMapping.HasAlternativeMapping "Link to this definition")  
Checks whether the parameter set has an alternative mapping.

Returns:  True if the parameter set has an alternative mapping.

Return type:  boolean

RemoveAlternativeMapping()[¶](#ApiClient.ParameterSetMapping.RemoveAlternativeMapping "Link to this definition")  
Removes the alternative mapping from the parameter set.

SetAlternativeMapping(*[mapping](#ApiClient.ParameterSetMapping.SetAlternativeMapping.mapping "ApiClient.ParameterSetMapping.SetAlternativeMapping.mapping (Python parameter) — Mapping to be set")*)[¶](#ApiClient.ParameterSetMapping.SetAlternativeMapping "Link to this definition")  
Sets the alternative mapping of the parameter set.

Parameters:  mapping[¶](#ApiClient.ParameterSetMapping.SetAlternativeMapping.mapping "Permalink to this definition")  
Mapping to be set

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
