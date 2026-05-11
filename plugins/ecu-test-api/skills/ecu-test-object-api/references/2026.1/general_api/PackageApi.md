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

[ API for Packages ](#)

API for Packages

- [ AnalysisPackage ](PackageApi/AnalysisPackage.md)
- [ Argument ](PackageApi/Argument.md)
- [ Attributes ](PackageApi/Attributes.md)
- [ AutoAssignRecordingGroup ](PackageApi/AutoAssignRecordingGroup.md)
- [ AutoAssignSignalGroup ](PackageApi/AutoAssignSignalGroup.md)
- [ LocalMapping ](PackageApi/LocalMapping.md)
- [ MappingTestStep ](PackageApi/MappingTestStep.md)
- [ MappingTestStepContainer ](PackageApi/MappingTestStepContainer.md)
- [ Package ](PackageApi/Package.md)
- [ RecordingConfig ](PackageApi/RecordingConfig.md)
- [ Return ](PackageApi/Return.md)
- [ TestStep ](PackageApi/TestStep.md)
- [ TestStepContainer ](PackageApi/TestStepContainer.md)
- [ TestStepRWBase ](PackageApi/TestStepRWBase.md)
- [ Testcase ](PackageApi/Testcase.md)
- [ TsAXSCall ](PackageApi/TsAXSCall.md)
- [ TsBlockBase ](PackageApi/TsBlockBase.md)
- [ TsBusMonitoring ](PackageApi/TsBusMonitoring.md)
- [ TsCaseNodeBase ](PackageApi/TsCaseNodeBase.md)
- [ TsSignalGroupOperation ](PackageApi/TsSignalGroupOperation.md)
- [ TsSwitchBase ](PackageApi/TsSwitchBase.md)
- [ TsUserInterface ](PackageApi/TsUserInterface.md)

API for Packages [ API for Packages ](#)

API for Packages

- [C PackageApi ](#ApiClient.PackageApi)
  - [A ExpectationApi ](#ApiClient.PackageApi.ExpectationApi)
  - [A ExpressionApi ](#ApiClient.PackageApi.ExpressionApi)
  - [A MappingApi ](#ApiClient.PackageApi.MappingApi)
  - [A SignalRecordingApi ](#ApiClient.PackageApi.SignalRecordingApi)
  - [A TestStepApi ](#ApiClient.PackageApi.TestStepApi)
  - [A TraceAnalysisApi ](#ApiClient.PackageApi.TraceAnalysisApi)
  - [A VariableApi ](#ApiClient.PackageApi.VariableApi)
  - [M CreateAnalysisPackage ](#ApiClient.PackageApi.CreateAnalysisPackage)
  - [M CreatePackage ](#ApiClient.PackageApi.CreatePackage)
  - [M GetAnalysisPackageByTestManagementId ](#ApiClient.PackageApi.GetAnalysisPackageByTestManagementId)
  - [M GetAnalysisPackageChanges ](#ApiClient.PackageApi.GetAnalysisPackageChanges)
  - [M GetAnalysisPackagePathsByTestscriptId ](#ApiClient.PackageApi.GetAnalysisPackagePathsByTestscriptId)
  - [M GetChanges ](#ApiClient.PackageApi.GetChanges)
  - [M GetPackageByTestManagementId ](#ApiClient.PackageApi.GetPackageByTestManagementId)
  - [M GetPackagePathsByTestscriptId ](#ApiClient.PackageApi.GetPackagePathsByTestscriptId)
  - [M GetTestManagementIdByPath ](#ApiClient.PackageApi.GetTestManagementIdByPath)
  - [M OpenAnalysisPackage ](#ApiClient.PackageApi.OpenAnalysisPackage)
  - [M OpenPackage ](#ApiClient.PackageApi.OpenPackage)
  - [M SearchAnalysisPackages ](#ApiClient.PackageApi.SearchAnalysisPackages)
  - [M SearchPackages ](#ApiClient.PackageApi.SearchPackages)
- [ AnalysisPackage ](PackageApi/AnalysisPackage.md)
- [ Argument ](PackageApi/Argument.md)
- [ Attributes ](PackageApi/Attributes.md)
- [ AutoAssignRecordingGroup ](PackageApi/AutoAssignRecordingGroup.md)
- [ AutoAssignSignalGroup ](PackageApi/AutoAssignSignalGroup.md)
- [ LocalMapping ](PackageApi/LocalMapping.md)
- [ MappingTestStep ](PackageApi/MappingTestStep.md)
- [ MappingTestStepContainer ](PackageApi/MappingTestStepContainer.md)
- [ Package ](PackageApi/Package.md)
- [ RecordingConfig ](PackageApi/RecordingConfig.md)
- [ Return ](PackageApi/Return.md)
- [ TestStep ](PackageApi/TestStep.md)
- [ TestStepContainer ](PackageApi/TestStepContainer.md)
- [ TestStepRWBase ](PackageApi/TestStepRWBase.md)
- [ Testcase ](PackageApi/Testcase.md)
- [ TsAXSCall ](PackageApi/TsAXSCall.md)
- [ TsBlockBase ](PackageApi/TsBlockBase.md)
- [ TsBusMonitoring ](PackageApi/TsBusMonitoring.md)
- [ TsCaseNodeBase ](PackageApi/TsCaseNodeBase.md)
- [ TsSignalGroupOperation ](PackageApi/TsSignalGroupOperation.md)
- [ TsSwitchBase ](PackageApi/TsSwitchBase.md)
- [ TsUserInterface ](PackageApi/TsUserInterface.md)

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

[ API for Trace Analyses ](TraceAnalysisApi.md)

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

API for Packages

- [C PackageApi ](#ApiClient.PackageApi)
  - [A ExpectationApi ](#ApiClient.PackageApi.ExpectationApi)
  - [A ExpressionApi ](#ApiClient.PackageApi.ExpressionApi)
  - [A MappingApi ](#ApiClient.PackageApi.MappingApi)
  - [A SignalRecordingApi ](#ApiClient.PackageApi.SignalRecordingApi)
  - [A TestStepApi ](#ApiClient.PackageApi.TestStepApi)
  - [A TraceAnalysisApi ](#ApiClient.PackageApi.TraceAnalysisApi)
  - [A VariableApi ](#ApiClient.PackageApi.VariableApi)
  - [M CreateAnalysisPackage ](#ApiClient.PackageApi.CreateAnalysisPackage)
  - [M CreatePackage ](#ApiClient.PackageApi.CreatePackage)
  - [M GetAnalysisPackageByTestManagementId ](#ApiClient.PackageApi.GetAnalysisPackageByTestManagementId)
  - [M GetAnalysisPackageChanges ](#ApiClient.PackageApi.GetAnalysisPackageChanges)
  - [M GetAnalysisPackagePathsByTestscriptId ](#ApiClient.PackageApi.GetAnalysisPackagePathsByTestscriptId)
  - [M GetChanges ](#ApiClient.PackageApi.GetChanges)
  - [M GetPackageByTestManagementId ](#ApiClient.PackageApi.GetPackageByTestManagementId)
  - [M GetPackagePathsByTestscriptId ](#ApiClient.PackageApi.GetPackagePathsByTestscriptId)
  - [M GetTestManagementIdByPath ](#ApiClient.PackageApi.GetTestManagementIdByPath)
  - [M OpenAnalysisPackage ](#ApiClient.PackageApi.OpenAnalysisPackage)
  - [M OpenPackage ](#ApiClient.PackageApi.OpenPackage)
  - [M SearchAnalysisPackages ](#ApiClient.PackageApi.SearchAnalysisPackages)
  - [M SearchPackages ](#ApiClient.PackageApi.SearchPackages)

# API for Packages[¶](#api-for-packages "Link to this heading")

Part of the [Object based program API](objectApi.md#objectapi).

*class* PackageApi[¶](#ApiClient.PackageApi "Link to this definition")  
API to access Packages

Returned by

- [`ApiClient.PackageApi`](objectApi.md#ApiClient.ApiClient.PackageApi "ApiClient.ApiClient.PackageApi (Python attribute) — Returns the PackageApi namespace.")

ExpectationApi[¶](#ApiClient.PackageApi.ExpectationApi "Link to this definition")  
Returns the ExpectationApi namespace.

Returns:  ExpectationApi namespace

Return type:  [`ExpectationApi`](ExpectationApi.md#ApiClient.ExpectationApi "ApiClient.ExpectationApi (Python class) — PackageApi.ExpectationApi")

ExpressionApi[¶](#ApiClient.PackageApi.ExpressionApi "Link to this definition")  
Returns the ExpressionApi namespace.

Returns:  ExpressionApi namespace

Return type:  [`ExpressionApi`](ExpressionApi.md#ApiClient.ExpressionApi "ApiClient.ExpressionApi (Python class) — PackageApi.ExpressionApi")

MappingApi[¶](#ApiClient.PackageApi.MappingApi "Link to this definition")  
Returns the MappingApi namespace.

Returns:  MappingApi namespace

Return type:  [`MappingApi`](MappingApi.md#ApiClient.MappingApi "ApiClient.MappingApi (Python class) — PackageApi.MappingApi")

SignalRecordingApi[¶](#ApiClient.PackageApi.SignalRecordingApi "Link to this definition")  
Returns the SignalRecordingApi namespace.

Returns:  SignalRecordingApi namespace

Return type:  [`SignalRecordingApi`](SignalRecordingApi.md#ApiClient.SignalRecordingApi "ApiClient.SignalRecordingApi (Python class) — PackageApi.SignalRecordingApi")

TestStepApi[¶](#ApiClient.PackageApi.TestStepApi "Link to this definition")  
Returns the TestStepApi namespace.

Returns:  TestStepApi namespace

Return type:  [`TestStepApi`](TestStepApi.md#ApiClient.TestStepApi "ApiClient.TestStepApi (Python class) — PackageApi.TestStepApi")

TraceAnalysisApi[¶](#ApiClient.PackageApi.TraceAnalysisApi "Link to this definition")  
Returns the TraceAnalysisApi namespace.

Returns:  TraceAnalysisApi namespace

Return type:  [`TraceAnalysisApi`](TraceAnalysisApi.md#ApiClient.TraceAnalysisApi "ApiClient.TraceAnalysisApi (Python class) — PackageApi.TraceAnalysisApi")

VariableApi[¶](#ApiClient.PackageApi.VariableApi "Link to this definition")  
Returns the VariableApi namespace.

Returns:  VariableApi namespace

Return type:  [`VariableApi`](VariableApi.md#ApiClient.VariableApi "ApiClient.VariableApi (Python class) — PackageApi.VariableApi")

CreateAnalysisPackage()[¶](#ApiClient.PackageApi.CreateAnalysisPackage "Link to this definition")  
Creates a new analysis package.

Returns:  New empty analysis package

Return type:  [`AnalysisPackage`](PackageApi/AnalysisPackage.md#ApiClient.AnalysisPackage "ApiClient.AnalysisPackage (Python class) — PackageApi.CreateAnalysisPackage")

CreatePackage()[¶](#ApiClient.PackageApi.CreatePackage "Link to this definition")  
Creates a new package.

Returns:  New empty package

Return type:  [`Package`](PackageApi/Package.md#ApiClient.Package "ApiClient.Package (Python class) — PackageApi.CreatePackage")

GetAnalysisPackageByTestManagementId(*[testManagementId](#ApiClient.PackageApi.GetAnalysisPackageByTestManagementId.testManagementId "ApiClient.PackageApi.GetAnalysisPackageByTestManagementId.testManagementId (Python parameter) — The test management id identifying the analysis package")*)[¶](#ApiClient.PackageApi.GetAnalysisPackageByTestManagementId "Link to this definition")  
Returns an existing analysis package holding the given test management id or None, if no matching analysis package exists in the workspace. If found, the analysis package will be opened.

Parameters:  testManagementId : str[¶](#ApiClient.PackageApi.GetAnalysisPackageByTestManagementId.testManagementId "Permalink to this definition")  
The test management id identifying the analysis package

Returns:  the analysis package or None, if no matching item exists within the workspace

Return type:  [`AnalysisPackage`](PackageApi/AnalysisPackage.md#ApiClient.AnalysisPackage "ApiClient.AnalysisPackage (Python class) — PackageApi.CreateAnalysisPackage")

GetAnalysisPackageChanges(*[oldPackage](#ApiClient.PackageApi.GetAnalysisPackageChanges.oldPackage "ApiClient.PackageApi.GetAnalysisPackageChanges.oldPackage (Python parameter) — The old package to compare.")*, *[newPackage](#ApiClient.PackageApi.GetAnalysisPackageChanges.newPackage "ApiClient.PackageApi.GetAnalysisPackageChanges.newPackage (Python parameter) — The new package to compare.")*)[¶](#ApiClient.PackageApi.GetAnalysisPackageChanges "Link to this definition")  
Get the changes that exist between two given analysis packages.

Parameters:  oldPackage[¶](#ApiClient.PackageApi.GetAnalysisPackageChanges.oldPackage "Permalink to this definition")  
The old package to compare.

newPackage[¶](#ApiClient.PackageApi.GetAnalysisPackageChanges.newPackage "Permalink to this definition")  
The new package to compare.

Returns:  The changes that exist between the two analysis packages.

Return type:  list[[`Change`](ConfigurationApi/Change.md#ApiClient.Change "ApiClient.Change (Python class) — Represents a change between an old element and a new element. Both elements have the same type, e.g. a certain test step and stem from two different Objects, e.g. an old Package a new Package.")]

GetAnalysisPackagePathsByTestscriptId(*[testscriptId](#ApiClient.PackageApi.GetAnalysisPackagePathsByTestscriptId.testscriptId "ApiClient.PackageApi.GetAnalysisPackagePathsByTestscriptId.testscriptId (Python parameter) — The test management id identifying the package")*)[¶](#ApiClient.PackageApi.GetAnalysisPackagePathsByTestscriptId "Link to this definition")  
Returns paths of packages which holding the given test script id.

Parameters:  testscriptId : str[¶](#ApiClient.PackageApi.GetAnalysisPackagePathsByTestscriptId.testscriptId "Permalink to this definition")  
The test management id identifying the package

Returns:  list of file paths

Return type:  list[str]

GetChanges(*[oldPackage](#ApiClient.PackageApi.GetChanges.oldPackage "ApiClient.PackageApi.GetChanges.oldPackage (Python parameter) — The old package to compare.")*, *[newPackage](#ApiClient.PackageApi.GetChanges.newPackage "ApiClient.PackageApi.GetChanges.newPackage (Python parameter) — The new package to compare.")*)[¶](#ApiClient.PackageApi.GetChanges "Link to this definition")  
Get the changes that exist between two given packages.

Parameters:  oldPackage[¶](#ApiClient.PackageApi.GetChanges.oldPackage "Permalink to this definition")  
The old package to compare.

newPackage[¶](#ApiClient.PackageApi.GetChanges.newPackage "Permalink to this definition")  
The new package to compare.

Returns:  The changes that exist between the two packages.

Return type:  list[[`Change`](ConfigurationApi/Change.md#ApiClient.Change "ApiClient.Change (Python class) — Represents a change between an old element and a new element. Both elements have the same type, e.g. a certain test step and stem from two different Objects, e.g. an old Package a new Package.")]

GetPackageByTestManagementId(*[testManagementId](#ApiClient.PackageApi.GetPackageByTestManagementId.testManagementId "ApiClient.PackageApi.GetPackageByTestManagementId.testManagementId (Python parameter) — The test management id identifying the package")*)[¶](#ApiClient.PackageApi.GetPackageByTestManagementId "Link to this definition")  
Returns an existing package holding the given test management id or None, if no matching package exists in the workspace. If found, the package will be opened.

Parameters:  testManagementId : str[¶](#ApiClient.PackageApi.GetPackageByTestManagementId.testManagementId "Permalink to this definition")  
The test management id identifying the package

Returns:  the package or None, if no matching package exists within the workspace

Return type:  [`Package`](PackageApi/Package.md#ApiClient.Package "ApiClient.Package (Python class) — PackageApi.CreatePackage")

GetPackagePathsByTestscriptId(*[testscriptId](#ApiClient.PackageApi.GetPackagePathsByTestscriptId.testscriptId "ApiClient.PackageApi.GetPackagePathsByTestscriptId.testscriptId (Python parameter) — The test management id identifying the package")*)[¶](#ApiClient.PackageApi.GetPackagePathsByTestscriptId "Link to this definition")  
Returns paths of packages which holding the given test script id.

Parameters:  testscriptId : str[¶](#ApiClient.PackageApi.GetPackagePathsByTestscriptId.testscriptId "Permalink to this definition")  
The test management id identifying the package

Returns:  list of file paths

Return type:  list[str]

GetTestManagementIdByPath(*[filename](#ApiClient.PackageApi.GetTestManagementIdByPath.filename "ApiClient.PackageApi.GetTestManagementIdByPath.filename (Python parameter) — Absolute path to the package or analysis package file or relative path in regard to the package directory")*)[¶](#ApiClient.PackageApi.GetTestManagementIdByPath "Link to this definition")  
Returns the test script id for a given Package or Analysis Package filename. If the corresponding item has no id or if it does not exist, an empty string is returned.

Parameters:  filename : str[¶](#ApiClient.PackageApi.GetTestManagementIdByPath.filename "Permalink to this definition")  
Absolute path to the package or analysis package file or relative path in regard to the package directory

Returns:  The test script id of an empty string

Return type:  str

OpenAnalysisPackage(*[filename](#ApiClient.PackageApi.OpenAnalysisPackage.filename "ApiClient.PackageApi.OpenAnalysisPackage.filename (Python parameter) — Absolute path to the analysis package file or relative path in regard to the package directory")*)[¶](#ApiClient.PackageApi.OpenAnalysisPackage "Link to this definition")  
Opens an existing analysis package. The analysis package may not be opened in ecu.test.

Parameters:  filename : str[¶](#ApiClient.PackageApi.OpenAnalysisPackage.filename "Permalink to this definition")  
Absolute path to the analysis package file or relative path in regard to the package directory

Returns:  Existing package

Return type:  [`AnalysisPackage`](PackageApi/AnalysisPackage.md#ApiClient.AnalysisPackage "ApiClient.AnalysisPackage (Python class) — PackageApi.CreateAnalysisPackage")

OpenPackage(*[filename](#ApiClient.PackageApi.OpenPackage.filename "ApiClient.PackageApi.OpenPackage.filename (Python parameter) — Absolute path to the package file or relative path in regard to the package directory")*)[¶](#ApiClient.PackageApi.OpenPackage "Link to this definition")  
Opens an existing package. The package may not be opened in ecu.test.

Parameters:  filename : str[¶](#ApiClient.PackageApi.OpenPackage.filename "Permalink to this definition")  
Absolute path to the package file or relative path in regard to the package directory

Returns:  Existing package

Return type:  [`Package`](PackageApi/Package.md#ApiClient.Package "ApiClient.Package (Python class) — PackageApi.CreatePackage")

SearchAnalysisPackages(*[searchCriteria](#ApiClient.PackageApi.SearchAnalysisPackages.searchCriteria "ApiClient.PackageApi.SearchAnalysisPackages.searchCriteria (Python parameter) — The search criteria expressed in the ecu.test filter syntax.")*, *[useExtendedMode](#ApiClient.PackageApi.SearchAnalysisPackages.useExtendedMode "ApiClient.PackageApi.SearchAnalysisPackages.useExtendedMode (Python parameter) — If True, extended search strings are enabled.")=`False`*)[¶](#ApiClient.PackageApi.SearchAnalysisPackages "Link to this definition")  
Searches the current workspace and library workspaces for analysis packages matching  
the given search criteria.

Parameters:  searchCriteria : str[¶](#ApiClient.PackageApi.SearchAnalysisPackages.searchCriteria "Permalink to this definition")  
The search criteria expressed in the ecu.test filter syntax. See section “Handling” =\> “Filter” of the ecu.test User Documentation.

useExtendedMode : boolean[¶](#ApiClient.PackageApi.SearchAnalysisPackages.useExtendedMode "Permalink to this definition")  
If True, extended search strings are enabled. The default is False, meaning each word in the searchCriteria will be enclosed by wildcards and mapped to the filename. (e.g. “hello world” =\> “Name = ‘\*hello\*’ and Name = ‘\*world\*’”)

Returns:  All matching analysis packages. If no item matches, an empty list is returned.

Return type:  list[[`AnalysisPackage`](PackageApi/AnalysisPackage.md#ApiClient.AnalysisPackage "ApiClient.AnalysisPackage (Python class) — PackageApi.CreateAnalysisPackage")]

Raises:  
**ApiError** – If the searchCriteria has an illegal syntax.

SearchPackages(*[searchCriteria](#ApiClient.PackageApi.SearchPackages.searchCriteria "ApiClient.PackageApi.SearchPackages.searchCriteria (Python parameter) — The search criteria expressed in the ecu.test filter syntax.")*, *[useExtendedMode](#ApiClient.PackageApi.SearchPackages.useExtendedMode "ApiClient.PackageApi.SearchPackages.useExtendedMode (Python parameter) — If True, extended search strings are enabled.")=`False`*)[¶](#ApiClient.PackageApi.SearchPackages "Link to this definition")  
Searches the current workspace and library workspaces for packages matching the given search criteria.

Parameters:  searchCriteria : str[¶](#ApiClient.PackageApi.SearchPackages.searchCriteria "Permalink to this definition")  
The search criteria expressed in the ecu.test filter syntax. See section “Handling” =\> “Filter” of the ecu.test User Documentation.

useExtendedMode : boolean[¶](#ApiClient.PackageApi.SearchPackages.useExtendedMode "Permalink to this definition")  
If True, extended search strings are enabled. The default is False, meaning each word in the searchCriteria will be enclosed by wildcards and mapped to the filename. (e.g. “hello world” =\> “Name = ‘\*hello\*’ and Name = ‘\*world\*’”)

Returns:  All matching packages. If no package matches, an empty list is returned.

Return type:  list[[`Package`](PackageApi/Package.md#ApiClient.Package "ApiClient.Package (Python class) — PackageApi.CreatePackage")]

Raises:  
**ApiError** – If the searchCriteria has an illegal syntax.

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
