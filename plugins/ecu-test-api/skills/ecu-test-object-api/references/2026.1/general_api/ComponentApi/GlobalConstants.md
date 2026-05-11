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

GlobalConstants [ GlobalConstants ](#)

GlobalConstants

- [C GlobalConstants ](#ApiClient.GlobalConstants)
  - [M AddArtifactReference ](#ApiClient.GlobalConstants.AddArtifactReference)
  - [M AppendReferencedFile ](#ApiClient.GlobalConstants.AppendReferencedFile)
  - [M ClearReferencedFiles ](#ApiClient.GlobalConstants.ClearReferencedFiles)
  - [M Clone ](#ApiClient.GlobalConstants.Clone)
  - [M GetArtifactReferences ](#ApiClient.GlobalConstants.GetArtifactReferences)
  - [M GetGlobalConstantsDefinition ](#ApiClient.GlobalConstants.GetGlobalConstantsDefinition)
  - [M GetReferencedFiles ](#ApiClient.GlobalConstants.GetReferencedFiles)
  - [M GetStaticConstantsPriority ](#ApiClient.GlobalConstants.GetStaticConstantsPriority)
  - [M RemoveArtifactReference ](#ApiClient.GlobalConstants.RemoveArtifactReference)
  - [M RemoveReferencedFile ](#ApiClient.GlobalConstants.RemoveReferencedFile)
  - [M SetStaticConstantsPriority ](#ApiClient.GlobalConstants.SetStaticConstantsPriority)

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

GlobalConstants

- [C GlobalConstants ](#ApiClient.GlobalConstants)
  - [M AddArtifactReference ](#ApiClient.GlobalConstants.AddArtifactReference)
  - [M AppendReferencedFile ](#ApiClient.GlobalConstants.AppendReferencedFile)
  - [M ClearReferencedFiles ](#ApiClient.GlobalConstants.ClearReferencedFiles)
  - [M Clone ](#ApiClient.GlobalConstants.Clone)
  - [M GetArtifactReferences ](#ApiClient.GlobalConstants.GetArtifactReferences)
  - [M GetGlobalConstantsDefinition ](#ApiClient.GlobalConstants.GetGlobalConstantsDefinition)
  - [M GetReferencedFiles ](#ApiClient.GlobalConstants.GetReferencedFiles)
  - [M GetStaticConstantsPriority ](#ApiClient.GlobalConstants.GetStaticConstantsPriority)
  - [M RemoveArtifactReference ](#ApiClient.GlobalConstants.RemoveArtifactReference)
  - [M RemoveReferencedFile ](#ApiClient.GlobalConstants.RemoveReferencedFile)
  - [M SetStaticConstantsPriority ](#ApiClient.GlobalConstants.SetStaticConstantsPriority)

# GlobalConstants[¶](#globalconstants "Link to this heading")

*class* GlobalConstants[¶](#ApiClient.GlobalConstants "Link to this definition")  
Contains the global constants definition and references to global constants definition files.

Specifically for use in project components. See [`TestConfigurationGlobalConstants`](../ConfigurationApi/TestConfigurationGlobalConstants.md#ApiClient.TestConfigurationGlobalConstants "ApiClient.TestConfigurationGlobalConstants (Python class) — Contains the global constants definition and references to global constants definition files.") for a container to be used in test configurations.

AddArtifactReference(*[constantsReference](#ApiClient.GlobalConstants.AddArtifactReference.constantsReference "ApiClient.GlobalConstants.AddArtifactReference.constantsReference (Python parameter) — Artifact reference to a global constants definition file")*)[¶](#ApiClient.GlobalConstants.AddArtifactReference "Link to this definition")  
Adds an artifact reference to a global constants definition file to the list.

Parameters:  constantsReference[¶](#ApiClient.GlobalConstants.AddArtifactReference.constantsReference "Permalink to this definition")  
Artifact reference to a global constants definition file

AppendReferencedFile(*[filename](#ApiClient.GlobalConstants.AppendReferencedFile.filename "ApiClient.GlobalConstants.AppendReferencedFile.filename (Python parameter) — Path to the global constants definition file.")*, *[namespace](#ApiClient.GlobalConstants.AppendReferencedFile.namespace "ApiClient.GlobalConstants.AppendReferencedFile.namespace (Python parameter) — Identifier of the workspace to which a file path is resolved. If specified, the file reference is always created relative to the parameters directory of the workspace with the given 'namespace'. For example, the namespace 'myLibrary' results in '<libraries.myLibrary.parameters>/MyConstants.gcd'. If None, ecu.test tries to find a matching library workspace based on the absolute or relative file path.")=`None`*)[¶](#ApiClient.GlobalConstants.AppendReferencedFile "Link to this definition")  
Appends a global constants definition file at the end of the list of referenced global constants definition files.

Parameters:  filename : str[¶](#ApiClient.GlobalConstants.AppendReferencedFile.filename "Permalink to this definition")  
Path to the global constants definition file. Either absolute or relative. For non-library workspaces, a relative path is interpreted relative to the *workspace* directory. For library workspaces, a relative path is interpreted relative to the *parameters* directory.

namespace : str[¶](#ApiClient.GlobalConstants.AppendReferencedFile.namespace "Permalink to this definition")  
Identifier of the workspace to which a file path is resolved. If specified, the file reference is always created relative to the *parameters* directory of the workspace with the given ‘namespace’. For example, the namespace ‘myLibrary’ results in ‘\<libraries.myLibrary.parameters\>/MyConstants.gcd’. If None, ecu.test tries to find a matching library workspace based on the absolute or relative file path. If no matching library workspace was found, the file path is treated as relative to the current *workspace* directory.

Raises:  
**ApiError** – When the given file is already referenced in this test configuration

ClearReferencedFiles()[¶](#ApiClient.GlobalConstants.ClearReferencedFiles "Link to this definition")  
Removes all referenced global constants definition files from the list.

Clone()[¶](#ApiClient.GlobalConstants.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`GlobalConstants`](#ApiClient.GlobalConstants "ApiClient.GlobalConstants (Python class) — Contains the global constants definition and references to global constants definition files.")

GetArtifactReferences()[¶](#ApiClient.GlobalConstants.GetArtifactReferences "Link to this definition")  
Returns artifact references to global constants definition files.

Returns:  A list of all artifact references

Return type:  list[[`ArtifactReference`](ArtifactReference.md#ApiClient.ArtifactReference "ApiClient.ArtifactReference (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")]

GetGlobalConstantsDefinition()[¶](#ApiClient.GlobalConstants.GetGlobalConstantsDefinition "Link to this definition")  
Returns the container for defining global constants statically.

Returns:  Container for global constants

Return type:  [`GlobalConstantsDefinition`](../ParameterApi/GlobalConstantsDefinition.md#ApiClient.GlobalConstantsDefinition "ApiClient.GlobalConstantsDefinition (Python class) — ParameterApi.CreateGlobalConstantsDefinition")

GetReferencedFiles()[¶](#ApiClient.GlobalConstants.GetReferencedFiles "Link to this definition")  
Returns a list of all referenced global constants definition files. The list is ordered by priority, i.e. global constants from files in the beginning of the list overwrite constants from later files. File references to a library workspace are always returned as an absolute path. Non-library workspace references are always returned relative to the *workspace* directory.

Returns:  List of all referenced global constants definition files (\*.gcd)

Return type:  list[str]

GetStaticConstantsPriority()[¶](#ApiClient.GlobalConstants.GetStaticConstantsPriority "Link to this definition")  
Returns the priority of statically defined constants with regard to the constants from referenced files and constants that are defined via REST API during configuration start.

Returns:  Priority value

Return type:  int

RemoveArtifactReference(*[constantsReference](#ApiClient.GlobalConstants.RemoveArtifactReference.constantsReference "ApiClient.GlobalConstants.RemoveArtifactReference.constantsReference (Python parameter) — Artifact reference to a global constants definition file")*)[¶](#ApiClient.GlobalConstants.RemoveArtifactReference "Link to this definition")  
Removes an artifact reference to a global constants definition file from the list.

Parameters:  constantsReference[¶](#ApiClient.GlobalConstants.RemoveArtifactReference.constantsReference "Permalink to this definition")  
Artifact reference to a global constants definition file

RemoveReferencedFile(*[filename](#ApiClient.GlobalConstants.RemoveReferencedFile.filename "ApiClient.GlobalConstants.RemoveReferencedFile.filename (Python parameter) — Path to the global constants definition file to be removed. Either absolute or relative. For non-library workspaces, a relative path is interpreted relative to the workspace directory. For library workspaces, a relative path is interpreted relative to the parameters directory.")*, *[namespace](#ApiClient.GlobalConstants.RemoveReferencedFile.namespace "ApiClient.GlobalConstants.RemoveReferencedFile.namespace (Python parameter) — Identifier of the workspace to which a file path is resolved. If specified, the file reference is always created relative to the parameters directory of the workspace with the given 'namespace'. For example, the namespace 'myLibrary' results in '<libraries.myLibrary.parameters>/MyConstants.gcd'. If None, ecu.test tries to find a matching library workspace based on the absolute or relative file path.")=`None`*)[¶](#ApiClient.GlobalConstants.RemoveReferencedFile "Link to this definition")  
Removes a global constants definition file from the list of referenced global constants definition files.

Parameters:  filename : str[¶](#ApiClient.GlobalConstants.RemoveReferencedFile.filename "Permalink to this definition")  
Path to the global constants definition file to be removed. Either absolute or relative. For non-library workspaces, a relative path is interpreted relative to the *workspace* directory. For library workspaces, a relative path is interpreted relative to the *parameters* directory.

namespace : str[¶](#ApiClient.GlobalConstants.RemoveReferencedFile.namespace "Permalink to this definition")  
Identifier of the workspace to which a file path is resolved. If specified, the file reference is always created relative to the *parameters* directory of the workspace with the given ‘namespace’. For example, the namespace ‘myLibrary’ results in ‘\<libraries.myLibrary.parameters\>/MyConstants.gcd’. If None, ecu.test tries to find a matching library workspace based on the absolute or relative file path. If no matching library workspace was found, the file path is treated as relative to the current *workspace* directory.

Raises:  
**ApiError** – When the given file is not referenced in this test configuration

SetStaticConstantsPriority(*[priority](#ApiClient.GlobalConstants.SetStaticConstantsPriority.priority "ApiClient.GlobalConstants.SetStaticConstantsPriority.priority (Python parameter) — Priority of the statically defined constants.")*)[¶](#ApiClient.GlobalConstants.SetStaticConstantsPriority "Link to this definition")  
Specifies the priority of the statically defined constants with regard to the constants from referenced files and constants that are defined via REST API during configuration start.

Note:  
If the given value is out of the valid range, it will be coerced to the closest reasonable value.

Parameters:  priority : int[¶](#ApiClient.GlobalConstants.SetStaticConstantsPriority.priority "Permalink to this definition")  
Priority of the statically defined constants. Should be between

- 0: highest priority and

- length of referenced files list + 1: lowest priority

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
