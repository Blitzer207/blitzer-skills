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

PackageParameters [ PackageParameters ](#)

PackageParameters

- [C PackageParameters ](#ApiClient.PackageParameters)
  - [M AppendReferencedFile ](#ApiClient.PackageParameters.AppendReferencedFile)
  - [M ClearReferencedFiles ](#ApiClient.PackageParameters.ClearReferencedFiles)
  - [M Clone ](#ApiClient.PackageParameters.Clone)
  - [M GetPackageParametersDefinition ](#ApiClient.PackageParameters.GetPackageParametersDefinition)
  - [M GetReferencedFiles ](#ApiClient.PackageParameters.GetReferencedFiles)
  - [M GetStaticParametersPriority ](#ApiClient.PackageParameters.GetStaticParametersPriority)
  - [M RemoveReferencedFile ](#ApiClient.PackageParameters.RemoveReferencedFile)
  - [M SetStaticParametersPriority ](#ApiClient.PackageParameters.SetStaticParametersPriority)

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

PackageParameters

- [C PackageParameters ](#ApiClient.PackageParameters)
  - [M AppendReferencedFile ](#ApiClient.PackageParameters.AppendReferencedFile)
  - [M ClearReferencedFiles ](#ApiClient.PackageParameters.ClearReferencedFiles)
  - [M Clone ](#ApiClient.PackageParameters.Clone)
  - [M GetPackageParametersDefinition ](#ApiClient.PackageParameters.GetPackageParametersDefinition)
  - [M GetReferencedFiles ](#ApiClient.PackageParameters.GetReferencedFiles)
  - [M GetStaticParametersPriority ](#ApiClient.PackageParameters.GetStaticParametersPriority)
  - [M RemoveReferencedFile ](#ApiClient.PackageParameters.RemoveReferencedFile)
  - [M SetStaticParametersPriority ](#ApiClient.PackageParameters.SetStaticParametersPriority)

# PackageParameters[¶](#packageparameters "Link to this heading")

*class* PackageParameters[¶](#ApiClient.PackageParameters "Link to this definition")  
AppendReferencedFile(*[filename](#ApiClient.PackageParameters.AppendReferencedFile.filename "ApiClient.PackageParameters.AppendReferencedFile.filename (Python parameter) — Path to the package parameters definition file.")*)[¶](#ApiClient.PackageParameters.AppendReferencedFile "Link to this definition")  
Appends a package parameters definition file at the end of the list of referenced package parameters definition files.

Parameters:  filename : str[¶](#ApiClient.PackageParameters.AppendReferencedFile.filename "Permalink to this definition")  
Path to the package parameters definition file. Absolute or relative to the current workspace directory.

ClearReferencedFiles()[¶](#ApiClient.PackageParameters.ClearReferencedFiles "Link to this definition")  
Removes all referenced package parameters definition files from the list.

Clone()[¶](#ApiClient.PackageParameters.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`PackageParameters`](#ApiClient.PackageParameters "ApiClient.PackageParameters (Python class) — Appends a package parameters definition file at the end of the list of referenced package parameters definition files.")

GetPackageParametersDefinition()[¶](#ApiClient.PackageParameters.GetPackageParametersDefinition "Link to this definition")  
Returns the container for defining package parameters statically.

Returns:  Container for package parameters

Return type:  [`PackageParametersDefinition`](../ParameterApi/PackageParametersDefinition.md#ApiClient.PackageParametersDefinition "ApiClient.PackageParametersDefinition (Python class) — ParameterApi.CreatePackageParametersDefinition")

GetReferencedFiles()[¶](#ApiClient.PackageParameters.GetReferencedFiles "Link to this definition")  
Returns a list of all referenced package parameters definition files. The list is ordered by priority, i.e. package parameters from files in the beginning of the list overwrite parameters from later files.

Returns:  List of all referenced package parameters definition files (\*.ppd)

Return type:  list[str]

GetStaticParametersPriority()[¶](#ApiClient.PackageParameters.GetStaticParametersPriority "Link to this definition")  
Returns the priority of statically defined parameters with regard to the parameters from referenced files.

Returns:  Priority value

Return type:  int

RemoveReferencedFile(*[filename](#ApiClient.PackageParameters.RemoveReferencedFile.filename "ApiClient.PackageParameters.RemoveReferencedFile.filename (Python parameter) — Path to the package parameters definition file to be removed.")*)[¶](#ApiClient.PackageParameters.RemoveReferencedFile "Link to this definition")  
Removes a package parameters definition file from the list of referenced package parameters definition files.

Parameters:  filename : str[¶](#ApiClient.PackageParameters.RemoveReferencedFile.filename "Permalink to this definition")  
Path to the package parameters definition file to be removed. Absolute or relative to the current workspace directory.

Raises:  
**ApiError** – When the given file is not referenced in this parameter set

SetStaticParametersPriority(*[priority](#ApiClient.PackageParameters.SetStaticParametersPriority.priority "ApiClient.PackageParameters.SetStaticParametersPriority.priority (Python parameter) — Priority of the statically defined parameters.")*)[¶](#ApiClient.PackageParameters.SetStaticParametersPriority "Link to this definition")  
Specifies the priority of the statically defined parameters with regard to the parameters from referenced files.

Note:  
If the given value is out of the valid range, it will be coerced to the closest reasonable value.

Parameters:  priority : int[¶](#ApiClient.PackageParameters.SetStaticParametersPriority.priority "Permalink to this definition")  
Priority of the statically defined parameters. Should be between

- 0: highest priority and

- length of referenced files list: lowest priority

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
