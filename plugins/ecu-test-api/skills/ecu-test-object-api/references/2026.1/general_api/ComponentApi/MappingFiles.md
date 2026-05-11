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

MappingFiles [ MappingFiles ](#)

MappingFiles

- [C MappingFiles ](#ApiClient.MappingFiles)
  - [M AddMappingArtifactReference ](#ApiClient.MappingFiles.AddMappingArtifactReference)
  - [M AddMappingFile ](#ApiClient.MappingFiles.AddMappingFile)
  - [M ClearMappingFiles ](#ApiClient.MappingFiles.ClearMappingFiles)
  - [M Clone ](#ApiClient.MappingFiles.Clone)
  - [M GetMappingArtifactReferences ](#ApiClient.MappingFiles.GetMappingArtifactReferences)
  - [M RemoveMappingArtifactReference ](#ApiClient.MappingFiles.RemoveMappingArtifactReference)
  - [M RemoveMappingFile ](#ApiClient.MappingFiles.RemoveMappingFile)
  - [M GetMappingFiles ](#ApiClient.MappingFiles.GetMappingFiles)

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

MappingFiles

- [C MappingFiles ](#ApiClient.MappingFiles)
  - [M AddMappingArtifactReference ](#ApiClient.MappingFiles.AddMappingArtifactReference)
  - [M AddMappingFile ](#ApiClient.MappingFiles.AddMappingFile)
  - [M ClearMappingFiles ](#ApiClient.MappingFiles.ClearMappingFiles)
  - [M Clone ](#ApiClient.MappingFiles.Clone)
  - [M GetMappingArtifactReferences ](#ApiClient.MappingFiles.GetMappingArtifactReferences)
  - [M RemoveMappingArtifactReference ](#ApiClient.MappingFiles.RemoveMappingArtifactReference)
  - [M RemoveMappingFile ](#ApiClient.MappingFiles.RemoveMappingFile)
  - [M GetMappingFiles ](#ApiClient.MappingFiles.GetMappingFiles)

# MappingFiles[¶](#mappingfiles "Link to this heading")

*class* MappingFiles[¶](#ApiClient.MappingFiles "Link to this definition")  
AddMappingArtifactReference(*[mappingReference](#ApiClient.MappingFiles.AddMappingArtifactReference.mappingReference "ApiClient.MappingFiles.AddMappingArtifactReference.mappingReference (Python parameter) — Artifact reference to a mapping file")*)[¶](#ApiClient.MappingFiles.AddMappingArtifactReference "Link to this definition")  
Adds an artifact reference to a mapping file to the list.

Parameters:  mappingReference[¶](#ApiClient.MappingFiles.AddMappingArtifactReference.mappingReference "Permalink to this definition")  
Artifact reference to a mapping file

AddMappingFile(*[filePath](#ApiClient.MappingFiles.AddMappingFile.filePath "ApiClient.MappingFiles.AddMappingFile.filePath (Python parameter) — Path to the mapping file (absolute or relative to parameter directory)")*, *[namespace](#ApiClient.MappingFiles.AddMappingFile.namespace "ApiClient.MappingFiles.AddMappingFile.namespace (Python parameter) — Identifier of the workspace to which a relative filePath is resolved.")=`None`*)[¶](#ApiClient.MappingFiles.AddMappingFile "Link to this definition")  
Adds a mapping file to the list.

Parameters:  filePath : str[¶](#ApiClient.MappingFiles.AddMappingFile.filePath "Permalink to this definition")  
Path to the mapping file (absolute or relative to parameter directory)

namespace : str[¶](#ApiClient.MappingFiles.AddMappingFile.namespace "Permalink to this definition")  
Identifier of the workspace to which a relative filePath is resolved. If not present or None, the namespace is determined automatically. It is also possible to reference a library workspace using its namespace. A relative filePath is resolved relative to the parameters directory of the given namespace. For example, the namespace parameter ‘myLibrary’ results in ‘\<libraries.myLibrary.parameters\>/MyMapping.xam’.

ClearMappingFiles()[¶](#ApiClient.MappingFiles.ClearMappingFiles "Link to this definition")  
Clears all entries from the mapping file list.

Clone()[¶](#ApiClient.MappingFiles.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`MappingFiles`](#ApiClient.MappingFiles "ApiClient.MappingFiles (Python class) — Adds an artifact reference to a mapping file to the list.")

GetMappingArtifactReferences()[¶](#ApiClient.MappingFiles.GetMappingArtifactReferences "Link to this definition")  
Returns artifact references to mapping files.

Returns:  A list of all artifact references

Return type:  list[[`ArtifactReference`](ArtifactReference.md#ApiClient.ArtifactReference "ApiClient.ArtifactReference (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")]

RemoveMappingArtifactReference(*[mappingReference](#ApiClient.MappingFiles.RemoveMappingArtifactReference.mappingReference "ApiClient.MappingFiles.RemoveMappingArtifactReference.mappingReference (Python parameter) — Artifact reference to a mapping file")*)[¶](#ApiClient.MappingFiles.RemoveMappingArtifactReference "Link to this definition")  
Removes an artifact reference to a mapping file from the list.

Parameters:  mappingReference[¶](#ApiClient.MappingFiles.RemoveMappingArtifactReference.mappingReference "Permalink to this definition")  
Artifact reference to a mapping file

RemoveMappingFile(*[index](#ApiClient.MappingFiles.RemoveMappingFile.index "ApiClient.MappingFiles.RemoveMappingFile.index (Python parameter) — The index of the mapping file to remove")*)[¶](#ApiClient.MappingFiles.RemoveMappingFile "Link to this definition")  
Removes a mapping file from the list.

Parameters:  index : int[¶](#ApiClient.MappingFiles.RemoveMappingFile.index "Permalink to this definition")  
The index of the mapping file to remove

GetMappingFiles()[¶](#ApiClient.MappingFiles.GetMappingFiles "Link to this definition")  
Returns the mapping file paths, relative to the workspace directory.

Returns:  A list of all mapping files

Return type:  list[str]

Deprecated since version 2024.2: Use [`GetMappingArtifactReferences()`](#ApiClient.MappingFiles.GetMappingArtifactReferences "ApiClient.MappingFiles.GetMappingArtifactReferences (Python method) — Returns artifact references to mapping files.") instead

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
