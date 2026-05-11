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

[ SignalGroupReference ](SignalGroupReference.md)

StimulationPackageCall [ StimulationPackageCall ](#)

StimulationPackageCall

- [C StimulationPackageCall ](#ApiClient.StimulationPackageCall)
  - [M ActivateAutomaticValueRestore ](#ApiClient.StimulationPackageCall.ActivateAutomaticValueRestore)
  - [M AddParameterGenerator ](#ApiClient.StimulationPackageCall.AddParameterGenerator)
  - [M AddParameterSet ](#ApiClient.StimulationPackageCall.AddParameterSet)
  - [M AddParameterVariationGenerator ](#ApiClient.StimulationPackageCall.AddParameterVariationGenerator)
  - [M Clone ](#ApiClient.StimulationPackageCall.Clone)
  - [M CreateAnalysisPackageMappingCalls ](#ApiClient.StimulationPackageCall.CreateAnalysisPackageMappingCalls)
  - [M DeactivateAutomaticValueRestore ](#ApiClient.StimulationPackageCall.DeactivateAutomaticValueRestore)
  - [M GetAbsolutePath ](#ApiClient.StimulationPackageCall.GetAbsolutePath)
  - [M GetAnalysisBindings ](#ApiClient.StimulationPackageCall.GetAnalysisBindings)
  - [M GetAnalysisPackageCalls ](#ApiClient.StimulationPackageCall.GetAnalysisPackageCalls)
  - [M GetComponents ](#ApiClient.StimulationPackageCall.GetComponents)
  - [M GetCustomRetryCondition ](#ApiClient.StimulationPackageCall.GetCustomRetryCondition)
  - [M GetCustomRetryCount ](#ApiClient.StimulationPackageCall.GetCustomRetryCount)
  - [M GetErrorRecoveryPkgLevel ](#ApiClient.StimulationPackageCall.GetErrorRecoveryPkgLevel)
  - [M GetErrorRecoveryPkgPath ](#ApiClient.StimulationPackageCall.GetErrorRecoveryPkgPath)
  - [M GetIndex ](#ApiClient.StimulationPackageCall.GetIndex)
  - [M GetLineNo ](#ApiClient.StimulationPackageCall.GetLineNo)
  - [M GetName ](#ApiClient.StimulationPackageCall.GetName)
  - [M GetPackage ](#ApiClient.StimulationPackageCall.GetPackage)
  - [M GetParameterGenerators ](#ApiClient.StimulationPackageCall.GetParameterGenerators)
  - [M GetParameterSets ](#ApiClient.StimulationPackageCall.GetParameterSets)
  - [M GetParameterVariationGenerators ](#ApiClient.StimulationPackageCall.GetParameterVariationGenerators)
  - [M GetParent ](#ApiClient.StimulationPackageCall.GetParent)
  - [M GetProjectRelativePath ](#ApiClient.StimulationPackageCall.GetProjectRelativePath)
  - [M GetRequestedAnalysisLabels ](#ApiClient.StimulationPackageCall.GetRequestedAnalysisLabels)
  - [M GetTestCaseId ](#ApiClient.StimulationPackageCall.GetTestCaseId)
  - [M GetTestScriptId ](#ApiClient.StimulationPackageCall.GetTestScriptId)
  - [M GetType ](#ApiClient.StimulationPackageCall.GetType)
  - [M HasComponents ](#ApiClient.StimulationPackageCall.HasComponents)
  - [M HasCustomErrorRecoveryPackageSettings ](#ApiClient.StimulationPackageCall.HasCustomErrorRecoveryPackageSettings)
  - [M HasCustomRestoreSettings ](#ApiClient.StimulationPackageCall.HasCustomRestoreSettings)
  - [M HasCustomRetrySettings ](#ApiClient.StimulationPackageCall.HasCustomRetrySettings)
  - [M InsertParameterSet ](#ApiClient.StimulationPackageCall.InsertParameterSet)
  - [M IsAutomaticValueRestoreActivated ](#ApiClient.StimulationPackageCall.IsAutomaticValueRestoreActivated)
  - [M IsAutomaticValueRestoreDeactivated ](#ApiClient.StimulationPackageCall.IsAutomaticValueRestoreDeactivated)
  - [M IsEnabled ](#ApiClient.StimulationPackageCall.IsEnabled)
  - [M IsReported ](#ApiClient.StimulationPackageCall.IsReported)
  - [M RemoveFromProject ](#ApiClient.StimulationPackageCall.RemoveFromProject)
  - [M RemoveParameterGenerator ](#ApiClient.StimulationPackageCall.RemoveParameterGenerator)
  - [M RemoveParameterSet ](#ApiClient.StimulationPackageCall.RemoveParameterSet)
  - [M RemoveParameterVariationGenerator ](#ApiClient.StimulationPackageCall.RemoveParameterVariationGenerator)
  - [M SetCustomRetryCondition ](#ApiClient.StimulationPackageCall.SetCustomRetryCondition)
  - [M SetCustomRetryCount ](#ApiClient.StimulationPackageCall.SetCustomRetryCount)
  - [M SetEnabled ](#ApiClient.StimulationPackageCall.SetEnabled)
  - [M SetErrorRecoveryPkgLevel ](#ApiClient.StimulationPackageCall.SetErrorRecoveryPkgLevel)
  - [M SetErrorRecoveryPkgPath ](#ApiClient.StimulationPackageCall.SetErrorRecoveryPkgPath)
  - [M SetName ](#ApiClient.StimulationPackageCall.SetName)
  - [M SetReported ](#ApiClient.StimulationPackageCall.SetReported)
  - [M SetTestCaseId ](#ApiClient.StimulationPackageCall.SetTestCaseId)
  - [M UseParentErrorRecoveryPackageSettings ](#ApiClient.StimulationPackageCall.UseParentErrorRecoveryPackageSettings)
  - [M UseParentRetrySettings ](#ApiClient.StimulationPackageCall.UseParentRetrySettings)
  - [M UseParentValueRestoreSettings ](#ApiClient.StimulationPackageCall.UseParentValueRestoreSettings)
  - [M GetPosition ](#ApiClient.StimulationPackageCall.GetPosition)

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

StimulationPackageCall

- [C StimulationPackageCall ](#ApiClient.StimulationPackageCall)
  - [M ActivateAutomaticValueRestore ](#ApiClient.StimulationPackageCall.ActivateAutomaticValueRestore)
  - [M AddParameterGenerator ](#ApiClient.StimulationPackageCall.AddParameterGenerator)
  - [M AddParameterSet ](#ApiClient.StimulationPackageCall.AddParameterSet)
  - [M AddParameterVariationGenerator ](#ApiClient.StimulationPackageCall.AddParameterVariationGenerator)
  - [M Clone ](#ApiClient.StimulationPackageCall.Clone)
  - [M CreateAnalysisPackageMappingCalls ](#ApiClient.StimulationPackageCall.CreateAnalysisPackageMappingCalls)
  - [M DeactivateAutomaticValueRestore ](#ApiClient.StimulationPackageCall.DeactivateAutomaticValueRestore)
  - [M GetAbsolutePath ](#ApiClient.StimulationPackageCall.GetAbsolutePath)
  - [M GetAnalysisBindings ](#ApiClient.StimulationPackageCall.GetAnalysisBindings)
  - [M GetAnalysisPackageCalls ](#ApiClient.StimulationPackageCall.GetAnalysisPackageCalls)
  - [M GetComponents ](#ApiClient.StimulationPackageCall.GetComponents)
  - [M GetCustomRetryCondition ](#ApiClient.StimulationPackageCall.GetCustomRetryCondition)
  - [M GetCustomRetryCount ](#ApiClient.StimulationPackageCall.GetCustomRetryCount)
  - [M GetErrorRecoveryPkgLevel ](#ApiClient.StimulationPackageCall.GetErrorRecoveryPkgLevel)
  - [M GetErrorRecoveryPkgPath ](#ApiClient.StimulationPackageCall.GetErrorRecoveryPkgPath)
  - [M GetIndex ](#ApiClient.StimulationPackageCall.GetIndex)
  - [M GetLineNo ](#ApiClient.StimulationPackageCall.GetLineNo)
  - [M GetName ](#ApiClient.StimulationPackageCall.GetName)
  - [M GetPackage ](#ApiClient.StimulationPackageCall.GetPackage)
  - [M GetParameterGenerators ](#ApiClient.StimulationPackageCall.GetParameterGenerators)
  - [M GetParameterSets ](#ApiClient.StimulationPackageCall.GetParameterSets)
  - [M GetParameterVariationGenerators ](#ApiClient.StimulationPackageCall.GetParameterVariationGenerators)
  - [M GetParent ](#ApiClient.StimulationPackageCall.GetParent)
  - [M GetProjectRelativePath ](#ApiClient.StimulationPackageCall.GetProjectRelativePath)
  - [M GetRequestedAnalysisLabels ](#ApiClient.StimulationPackageCall.GetRequestedAnalysisLabels)
  - [M GetTestCaseId ](#ApiClient.StimulationPackageCall.GetTestCaseId)
  - [M GetTestScriptId ](#ApiClient.StimulationPackageCall.GetTestScriptId)
  - [M GetType ](#ApiClient.StimulationPackageCall.GetType)
  - [M HasComponents ](#ApiClient.StimulationPackageCall.HasComponents)
  - [M HasCustomErrorRecoveryPackageSettings ](#ApiClient.StimulationPackageCall.HasCustomErrorRecoveryPackageSettings)
  - [M HasCustomRestoreSettings ](#ApiClient.StimulationPackageCall.HasCustomRestoreSettings)
  - [M HasCustomRetrySettings ](#ApiClient.StimulationPackageCall.HasCustomRetrySettings)
  - [M InsertParameterSet ](#ApiClient.StimulationPackageCall.InsertParameterSet)
  - [M IsAutomaticValueRestoreActivated ](#ApiClient.StimulationPackageCall.IsAutomaticValueRestoreActivated)
  - [M IsAutomaticValueRestoreDeactivated ](#ApiClient.StimulationPackageCall.IsAutomaticValueRestoreDeactivated)
  - [M IsEnabled ](#ApiClient.StimulationPackageCall.IsEnabled)
  - [M IsReported ](#ApiClient.StimulationPackageCall.IsReported)
  - [M RemoveFromProject ](#ApiClient.StimulationPackageCall.RemoveFromProject)
  - [M RemoveParameterGenerator ](#ApiClient.StimulationPackageCall.RemoveParameterGenerator)
  - [M RemoveParameterSet ](#ApiClient.StimulationPackageCall.RemoveParameterSet)
  - [M RemoveParameterVariationGenerator ](#ApiClient.StimulationPackageCall.RemoveParameterVariationGenerator)
  - [M SetCustomRetryCondition ](#ApiClient.StimulationPackageCall.SetCustomRetryCondition)
  - [M SetCustomRetryCount ](#ApiClient.StimulationPackageCall.SetCustomRetryCount)
  - [M SetEnabled ](#ApiClient.StimulationPackageCall.SetEnabled)
  - [M SetErrorRecoveryPkgLevel ](#ApiClient.StimulationPackageCall.SetErrorRecoveryPkgLevel)
  - [M SetErrorRecoveryPkgPath ](#ApiClient.StimulationPackageCall.SetErrorRecoveryPkgPath)
  - [M SetName ](#ApiClient.StimulationPackageCall.SetName)
  - [M SetReported ](#ApiClient.StimulationPackageCall.SetReported)
  - [M SetTestCaseId ](#ApiClient.StimulationPackageCall.SetTestCaseId)
  - [M UseParentErrorRecoveryPackageSettings ](#ApiClient.StimulationPackageCall.UseParentErrorRecoveryPackageSettings)
  - [M UseParentRetrySettings ](#ApiClient.StimulationPackageCall.UseParentRetrySettings)
  - [M UseParentValueRestoreSettings ](#ApiClient.StimulationPackageCall.UseParentValueRestoreSettings)
  - [M GetPosition ](#ApiClient.StimulationPackageCall.GetPosition)

# StimulationPackageCall[¶](#stimulationpackagecall "Link to this heading")

*class* StimulationPackageCall[¶](#ApiClient.StimulationPackageCall "Link to this definition")  
A stimulation package call (of a package) in a project.

Returned by

- [`ComponentApi.CreateStimulationPackageCall`](../ComponentApi.md#ApiClient.ComponentApi.CreateStimulationPackageCall "ApiClient.ComponentApi.CreateStimulationPackageCall (Python method) — Returns the created stimulation package call.")

ActivateAutomaticValueRestore()[¶](#ApiClient.StimulationPackageCall.ActivateAutomaticValueRestore "Link to this definition")  
Activates value restore of test quantities after the execution of every Package.

AddParameterGenerator(*[name](#ApiClient.StimulationPackageCall.AddParameterGenerator.name "ApiClient.StimulationPackageCall.AddParameterGenerator.name (Python parameter) — Name of the parameter generator")*, *[generatorId](#ApiClient.StimulationPackageCall.AddParameterGenerator.generatorId "ApiClient.StimulationPackageCall.AddParameterGenerator.generatorId (Python parameter) — Unique generator id of generator to be added")*)[¶](#ApiClient.StimulationPackageCall.AddParameterGenerator "Link to this definition")  
Adds a parameter generator to the package call

Parameters:  name : str[¶](#ApiClient.StimulationPackageCall.AddParameterGenerator.name "Permalink to this definition")  
Name of the parameter generator

generatorId : str[¶](#ApiClient.StimulationPackageCall.AddParameterGenerator.generatorId "Permalink to this definition")  
Unique generator id of generator to be added

Returns:  The parameter generator

Return type:  [`ParameterGenerator`](ParameterGenerator.md#ApiClient.ParameterGenerator "ApiClient.ParameterGenerator (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")

AddParameterSet(*[name](#ApiClient.StimulationPackageCall.AddParameterSet.name "ApiClient.StimulationPackageCall.AddParameterSet.name (Python parameter) — Name of the parameter set")*, *[index](#ApiClient.StimulationPackageCall.AddParameterSet.index "ApiClient.StimulationPackageCall.AddParameterSet.index (Python parameter) — Zero base index to insert the parameter set inside the package call")=`None`*)[¶](#ApiClient.StimulationPackageCall.AddParameterSet "Link to this definition")  
Adds a parameter set to the stimulation package call

Parameters:  name : str[¶](#ApiClient.StimulationPackageCall.AddParameterSet.name "Permalink to this definition")  
Name of the parameter set

index : int[¶](#ApiClient.StimulationPackageCall.AddParameterSet.index "Permalink to this definition")  
Zero base index to insert the parameter set inside the package call

Returns:  The parameter set

Return type:  [`ParameterSet`](ParameterSet.md#ApiClient.ParameterSet "ApiClient.ParameterSet (Python class) — Returns access to the package attributes definitions specified within the parameter set and the referenced package attribute definition files.")

AddParameterVariationGenerator(*[name](#ApiClient.StimulationPackageCall.AddParameterVariationGenerator.name "ApiClient.StimulationPackageCall.AddParameterVariationGenerator.name (Python parameter) — Name of the parameter variation generator.")*)[¶](#ApiClient.StimulationPackageCall.AddParameterVariationGenerator "Link to this definition")  
Adds a parameter variation generator to the stimulation package call.

Parameters:  name : str[¶](#ApiClient.StimulationPackageCall.AddParameterVariationGenerator.name "Permalink to this definition")  
Name of the parameter variation generator.

Returns:  The parameter variation generator.

Return type:  [`ParameterVariationGeneratorComponent`](ParameterVariationGeneratorComponent.md#ApiClient.ParameterVariationGeneratorComponent "ApiClient.ParameterVariationGeneratorComponent (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")

Clone()[¶](#ApiClient.StimulationPackageCall.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`StimulationPackageCall`](#ApiClient.StimulationPackageCall "ApiClient.StimulationPackageCall (Python class) — A stimulation package call (of a package) in a project.")

CreateAnalysisPackageMappingCalls(*[onlyMissing](#ApiClient.StimulationPackageCall.CreateAnalysisPackageMappingCalls.onlyMissing "ApiClient.StimulationPackageCall.CreateAnalysisPackageMappingCalls.onlyMissing (Python parameter) — If True, only analysis package mapping calls not yet added to the project are created.")=`False`*)[¶](#ApiClient.StimulationPackageCall.CreateAnalysisPackageMappingCalls "Link to this definition")  
Creates an analysis package mapping call for each analysis requested in the stimulation package.

Parameters:  onlyMissing : bool[¶](#ApiClient.StimulationPackageCall.CreateAnalysisPackageMappingCalls.onlyMissing "Permalink to this definition")  
If True, only analysis package mapping calls not yet added to the project are created.

Returns:  list of analysis package mapping calls

Return type:  list[[`AnalysisPackageMappingCall`](AnalysisPackageMappingCall.md#ApiClient.AnalysisPackageMappingCall "ApiClient.AnalysisPackageMappingCall (Python class) — An analysis package mapping call in a project.")]

Raises:  
**ApiError** – If called with onlyMissing=True, without adding the stimulation call to the project first.

DeactivateAutomaticValueRestore()[¶](#ApiClient.StimulationPackageCall.DeactivateAutomaticValueRestore "Link to this definition")  
Deactivate value restore of test quantities after the execution of every Package.

GetAbsolutePath()[¶](#ApiClient.StimulationPackageCall.GetAbsolutePath "Link to this definition")  
Returns the absolute path to referenced package.

Returns:  Absolute path to referenced package

Return type:  str

GetAnalysisBindings()[¶](#ApiClient.StimulationPackageCall.GetAnalysisBindings "Link to this definition")  
Returns the configured bindings between this stimulation package and the attached analysis packages.

Returns:  All signal group references

Return type:  [`AnalysisBindings`](AnalysisBindings.md#ApiClient.AnalysisBindings "ApiClient.AnalysisBindings (Python class) — The configured bindings between a stimulation package and its attached analysis packages.")

GetAnalysisPackageCalls(*[skipDisabled](#ApiClient.StimulationPackageCall.GetAnalysisPackageCalls.skipDisabled "ApiClient.StimulationPackageCall.GetAnalysisPackageCalls.skipDisabled (Python parameter) — Defines whether disabled package calls should be excluded.")=`True`*, *[noParameterSets](#ApiClient.StimulationPackageCall.GetAnalysisPackageCalls.noParameterSets "ApiClient.StimulationPackageCall.GetAnalysisPackageCalls.noParameterSets (Python parameter) — Defines whether package calls with parameter sets should be excluded.")=`False`*)[¶](#ApiClient.StimulationPackageCall.GetAnalysisPackageCalls "Link to this definition")  
Returns all analysis package calls of the project referencing this stimulation package call. Analysis package calls that reference “all previous stimulations” are included (if they are inserted behind the stimulation package call in the project).

Parameters:  skipDisabled : boolean[¶](#ApiClient.StimulationPackageCall.GetAnalysisPackageCalls.skipDisabled "Permalink to this definition")  
Defines whether disabled package calls should be excluded.

noParameterSets : boolean[¶](#ApiClient.StimulationPackageCall.GetAnalysisPackageCalls.noParameterSets "Permalink to this definition")  
Defines whether package calls with parameter sets should be excluded.

Returns:  Package calls

Return type:  list[[`AnalysisPackageCall`](AnalysisPackageCall.md#ApiClient.AnalysisPackageCall "ApiClient.AnalysisPackageCall (Python class) — An analysis package call in a project.")]

GetComponents()[¶](#ApiClient.StimulationPackageCall.GetComponents "Link to this definition")  
Returns all direct children of the package call.

Returns:  List with all children components

Return type:  list[[`ProjectComponent`](ProjectComponent.md#ApiClient.ProjectComponent "ApiClient.ProjectComponent (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")]

GetCustomRetryCondition()[¶](#ApiClient.StimulationPackageCall.GetCustomRetryCondition "Link to this definition")  
Returns the condition of the custom retries. Returns one of the following:

- ‘ERROR’

- ‘FAILED’

- ‘ERROR/FAILED’

Returns:  The condition of the custom retry

Return type:  str

GetCustomRetryCount()[¶](#ApiClient.StimulationPackageCall.GetCustomRetryCount "Link to this definition")  
Returns the number of the retries defined on the project component.

Returns:  Number of the custom retries

Return type:  integer

GetErrorRecoveryPkgLevel()[¶](#ApiClient.StimulationPackageCall.GetErrorRecoveryPkgLevel "Link to this definition")  
Returns the conditions under which the error recovery package (configured via [`SetErrorRecoveryPkgPath()`](#ApiClient.StimulationPackageCall.SetErrorRecoveryPkgPath "ApiClient.StimulationPackageCall.SetErrorRecoveryPkgPath (Python method) — Sets the path for a Package to be executed upon abort of test execution or ERROR/FAILED.")) will be executed

This overrides settings from the parent element or from the test configuration.

Returns:  - -1 = disabled

- 0 = on abort only

- 1 = on ERROR and on abort

- 2 = on FAILED, ERROR and abort.

- None: use inherited setting from parent element or test configuration

Return type:  int

GetErrorRecoveryPkgPath()[¶](#ApiClient.StimulationPackageCall.GetErrorRecoveryPkgPath "Link to this definition")  
Returns the path of the error recovery Package to be executed upon abort of test execution or ERROR/FAILED, if this element has a custom setting which overrides inherited settings from the parent element or from the test configuration.

see also [`GetErrorRecoveryPkgLevel()`](#ApiClient.StimulationPackageCall.GetErrorRecoveryPkgLevel "ApiClient.StimulationPackageCall.GetErrorRecoveryPkgLevel (Python method) — Returns the conditions under which the error recovery package (configured via SetErrorRecoveryPkgPath()) will be executed")

Returns:  Absolute path to Package file; None if inherited or explicitly disabled

Return type:  str

GetIndex()[¶](#ApiClient.StimulationPackageCall.GetIndex "Link to this definition")  
Returns the zero based index in the parent.

Returns:  Zero based index

Return type:  int

GetLineNo()[¶](#ApiClient.StimulationPackageCall.GetLineNo "Link to this definition")  
Returns the line number within its project.

Returns:  Line number

Return type:  int

GetName()[¶](#ApiClient.StimulationPackageCall.GetName "Link to this definition")  
Returns the name of the project component.

Returns:  Name of the component

Return type:  str

GetPackage()[¶](#ApiClient.StimulationPackageCall.GetPackage "Link to this definition")  
Returns the referenced stimulation package.

Note:  
The returned package object is a reference. If this object is used to manipulate the content all references in this project are affected.

Returns:  referenced package

Return type:  [`Package`](../PackageApi/Package.md#ApiClient.Package "ApiClient.Package (Python class) — PackageApi.CreatePackage")

Raises:  
**ApiError** – If the referenced package file (\*.pkg) does not exist.

GetParameterGenerators(*[skipDisabled](#ApiClient.StimulationPackageCall.GetParameterGenerators.skipDisabled "ApiClient.StimulationPackageCall.GetParameterGenerators.skipDisabled (Python parameter) — Defines whether disabled components should be included.")=`True`*)[¶](#ApiClient.StimulationPackageCall.GetParameterGenerators "Link to this definition")  
Returns all parameter generators of the package call.

Parameters:  skipDisabled : bool[¶](#ApiClient.StimulationPackageCall.GetParameterGenerators.skipDisabled "Permalink to this definition")  
Defines whether disabled components should be included.

Returns:  The parameter generators.

Return type:  list[[`ParameterGenerator`](ParameterGenerator.md#ApiClient.ParameterGenerator "ApiClient.ParameterGenerator (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")]

GetParameterSets(*[skipDisabled](#ApiClient.StimulationPackageCall.GetParameterSets.skipDisabled "ApiClient.StimulationPackageCall.GetParameterSets.skipDisabled (Python parameter) — Defines whether disabled components should be included.")=`True`*)[¶](#ApiClient.StimulationPackageCall.GetParameterSets "Link to this definition")  
Returns all parameter sets of the package call.

Parameters:  skipDisabled : bool[¶](#ApiClient.StimulationPackageCall.GetParameterSets.skipDisabled "Permalink to this definition")  
Defines whether disabled components should be included.

Returns:  Parameter sets

Return type:  list[[`ParameterSet`](ParameterSet.md#ApiClient.ParameterSet "ApiClient.ParameterSet (Python class) — Returns access to the package attributes definitions specified within the parameter set and the referenced package attribute definition files.")]

GetParameterVariationGenerators(*[skipDisabled](#ApiClient.StimulationPackageCall.GetParameterVariationGenerators.skipDisabled "ApiClient.StimulationPackageCall.GetParameterVariationGenerators.skipDisabled (Python parameter) — Defines whether disabled generators should be excluded.")=`True`*)[¶](#ApiClient.StimulationPackageCall.GetParameterVariationGenerators "Link to this definition")  
Returns all parameter variation generators of the stimulation package call.

Parameters:  skipDisabled : bool[¶](#ApiClient.StimulationPackageCall.GetParameterVariationGenerators.skipDisabled "Permalink to this definition")  
Defines whether disabled generators should be excluded.

Returns:  The parameter variation generators.

Return type:  list[[`ParameterVariationGeneratorComponent`](ParameterVariationGeneratorComponent.md#ApiClient.ParameterVariationGeneratorComponent "ApiClient.ParameterVariationGeneratorComponent (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")]

GetParent()[¶](#ApiClient.StimulationPackageCall.GetParent "Link to this definition")  
Returns the parent project component.

Returns:  Parent component

Return type:  [`ProjectComponent`](ProjectComponent.md#ApiClient.ProjectComponent "ApiClient.ProjectComponent (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")

GetProjectRelativePath()[¶](#ApiClient.StimulationPackageCall.GetProjectRelativePath "Link to this definition")  
Returns the file project relative path of the referenced package.

The returned path is a relative path, its base is the folder where the calling project is located, just like the path is shown in the package test step’s dialog.

Returns:  File name with relative path of the package to be called.

Return type:  str

Raises:  
**ProjectNotSavedError** – If this method is called before project is saved.

GetRequestedAnalysisLabels()[¶](#ApiClient.StimulationPackageCall.GetRequestedAnalysisLabels "Link to this definition")  
Returns the trace analysis label that are requested by this package.

Returns:  The list for requested analysis labels.

Return type:  list[str]

GetTestCaseId()[¶](#ApiClient.StimulationPackageCall.GetTestCaseId "Link to this definition")  
Returns the test case id of the package test component.

Returns:  Test case id.

Return type:  str

GetTestScriptId()[¶](#ApiClient.StimulationPackageCall.GetTestScriptId "Link to this definition")  
Returns the test script id of the corresponding package will be returned.

Returns:  Test script id.

Return type:  str

GetType()[¶](#ApiClient.StimulationPackageCall.GetType "Link to this definition")  
Returns the type (class name) of the project component, e.g.  
- “ConfigChange”

- “ParameterSet”

- “PackageCall”

- “Project”

- “PackageGenerator”

Returns:  Type (class name) of the project component

Return type:  str

HasComponents()[¶](#ApiClient.StimulationPackageCall.HasComponents "Link to this definition")  
Returns whether the package call has children.

Returns:  True if there are children, False otherwise.

Return type:  bool

HasCustomErrorRecoveryPackageSettings()[¶](#ApiClient.StimulationPackageCall.HasCustomErrorRecoveryPackageSettings "Link to this definition")  
Returns whether the Package execution settings in case of test abort or ERROR/FAILED of the parent element are overridden

Returns:  True if this element has custom error recovery package settings that override the parent element’s settings or those from the test configuration

Return type:  boolean

HasCustomRestoreSettings()[¶](#ApiClient.StimulationPackageCall.HasCustomRestoreSettings "Link to this definition")  
Returns if the value restore settings of the parent element are used or overridden by custom settings

Returns:  True if custom settings used, False if parent settings used

Return type:  boolean

HasCustomRetrySettings()[¶](#ApiClient.StimulationPackageCall.HasCustomRetrySettings "Link to this definition")  
Returns if the retry settings of the parent element are used

Returns:  True if parent settings used, False if custom settings defined

Return type:  boolean

InsertParameterSet(*[parameterSet](#ApiClient.StimulationPackageCall.InsertParameterSet.parameterSet "ApiClient.StimulationPackageCall.InsertParameterSet.parameterSet (Python parameter) — parameter set")*, *[index](#ApiClient.StimulationPackageCall.InsertParameterSet.index "ApiClient.StimulationPackageCall.InsertParameterSet.index (Python parameter) — Zero based index  to insert the parameter set inside the package call")=`None`*)[¶](#ApiClient.StimulationPackageCall.InsertParameterSet "Link to this definition")  
Adds a parameter set to the package call

Parameters:  parameterSet[¶](#ApiClient.StimulationPackageCall.InsertParameterSet.parameterSet "Permalink to this definition")  
parameter set

index : int[¶](#ApiClient.StimulationPackageCall.InsertParameterSet.index "Permalink to this definition")  
Zero based index to insert the parameter set inside the package call

IsAutomaticValueRestoreActivated()[¶](#ApiClient.StimulationPackageCall.IsAutomaticValueRestoreActivated "Link to this definition")  
Returns if the automatic value restore is activated

Returns:  True if activated, else False

Return type:  boolean

IsAutomaticValueRestoreDeactivated()[¶](#ApiClient.StimulationPackageCall.IsAutomaticValueRestoreDeactivated "Link to this definition")  
Returns if the automatic value restore is deactivated

Returns:  True if deactivated, else False

Return type:  boolean

IsEnabled()[¶](#ApiClient.StimulationPackageCall.IsEnabled "Link to this definition")  
Returns the state of the test step.

Returns:  True if test step is enabled, otherwise False

Return type:  bool

IsReported()[¶](#ApiClient.StimulationPackageCall.IsReported "Link to this definition")  
Returns whether the test step will be reported. If it has a parent test step, this function will only return true if both this test step and the parent test step should be reported.

Returns:  True if test step will be reported, otherwise False

Return type:  bool

RemoveFromProject()[¶](#ApiClient.StimulationPackageCall.RemoveFromProject "Link to this definition")  
Removes this component from the project.

Raises:  
**ApiError** – if the component is not part of any project

RemoveParameterGenerator(*[paramGenerator](#ApiClient.StimulationPackageCall.RemoveParameterGenerator.paramGenerator "ApiClient.StimulationPackageCall.RemoveParameterGenerator.paramGenerator (Python parameter) — The parameter generator to be removed")*)[¶](#ApiClient.StimulationPackageCall.RemoveParameterGenerator "Link to this definition")  
Removes a parameter generator from the package call.

Parameters:  paramGenerator[¶](#ApiClient.StimulationPackageCall.RemoveParameterGenerator.paramGenerator "Permalink to this definition")  
The parameter generator to be removed

Raises:  
**ApiError** –

- If the given parameter generator is not part if the package call

- If paramGenerator ist not of type [`ParameterGenerator`](ParameterGenerator.md#ApiClient.ParameterGenerator "ApiClient.ParameterGenerator (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")

RemoveParameterSet(*[paramSet](#ApiClient.StimulationPackageCall.RemoveParameterSet.paramSet "ApiClient.StimulationPackageCall.RemoveParameterSet.paramSet (Python parameter) — The parameter set to be removed")*)[¶](#ApiClient.StimulationPackageCall.RemoveParameterSet "Link to this definition")  
Removes a parameter set from the stimulation package call.

Parameters:  paramSet[¶](#ApiClient.StimulationPackageCall.RemoveParameterSet.paramSet "Permalink to this definition")  
The parameter set to be removed

Raises:  
**ApiError** –

- If the given parameter set is not part if the package call

- If paramGenerator ist not of type [`ParameterSet`](ParameterSet.md#ApiClient.ParameterSet "ApiClient.ParameterSet (Python class) — Returns access to the package attributes definitions specified within the parameter set and the referenced package attribute definition files.")

RemoveParameterVariationGenerator(*[paramVariationGenerator](#ApiClient.StimulationPackageCall.RemoveParameterVariationGenerator.paramVariationGenerator "ApiClient.StimulationPackageCall.RemoveParameterVariationGenerator.paramVariationGenerator (Python parameter) — The parameter variation generator to be removed.")*)[¶](#ApiClient.StimulationPackageCall.RemoveParameterVariationGenerator "Link to this definition")  
Removes a parameter variation generator from the stimulation package call.

Parameters:  paramVariationGenerator[¶](#ApiClient.StimulationPackageCall.RemoveParameterVariationGenerator.paramVariationGenerator "Permalink to this definition")  
The parameter variation generator to be removed.

Raises:  
**ApiError** –

- If the given parameter variation generator is not part of the package call

- If paramVariationGenerator is not of type [`ParameterVariationGeneratorComponent`](ParameterVariationGeneratorComponent.md#ApiClient.ParameterVariationGeneratorComponent "ApiClient.ParameterVariationGeneratorComponent (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")

SetCustomRetryCondition(*[condition](#ApiClient.StimulationPackageCall.SetCustomRetryCondition.condition "ApiClient.StimulationPackageCall.SetCustomRetryCondition.condition (Python parameter) — The condition of the custom retry")*)[¶](#ApiClient.StimulationPackageCall.SetCustomRetryCondition "Link to this definition")  
Sets the condition of the custom retry. Must be one of the following:

- ‘ERROR’

- ‘FAILED’

- ‘ERROR/FAILED’

Parameters:  condition : str[¶](#ApiClient.StimulationPackageCall.SetCustomRetryCondition.condition "Permalink to this definition")  
The condition of the custom retry

SetCustomRetryCount(*[count](#ApiClient.StimulationPackageCall.SetCustomRetryCount.count "ApiClient.StimulationPackageCall.SetCustomRetryCount.count (Python parameter) — Number of the custom retries")*)[¶](#ApiClient.StimulationPackageCall.SetCustomRetryCount "Link to this definition")  
Sets the number of the retries for all Packages within the project component.

Parameters:  count : integer[¶](#ApiClient.StimulationPackageCall.SetCustomRetryCount.count "Permalink to this definition")  
Number of the custom retries

SetEnabled(*[state](#ApiClient.StimulationPackageCall.SetEnabled.state "ApiClient.StimulationPackageCall.SetEnabled.state (Python parameter) — True (=Default) to enable, False to disable the test step.")=`True`*)[¶](#ApiClient.StimulationPackageCall.SetEnabled "Link to this definition")  
Enable or disable the test step.

Parameters:  state : bool[¶](#ApiClient.StimulationPackageCall.SetEnabled.state "Permalink to this definition")  
True (=Default) to enable, False to disable the test step.

SetErrorRecoveryPkgLevel(*[level](#ApiClient.StimulationPackageCall.SetErrorRecoveryPkgLevel.level "ApiClient.StimulationPackageCall.SetErrorRecoveryPkgLevel.level (Python parameter) — disabled")*)[¶](#ApiClient.StimulationPackageCall.SetErrorRecoveryPkgLevel "Link to this definition")  
Sets the conditions under which the error recovery package (configured via [`SetErrorRecoveryPkgPath()`](#ApiClient.StimulationPackageCall.SetErrorRecoveryPkgPath "ApiClient.StimulationPackageCall.SetErrorRecoveryPkgPath (Python method) — Sets the path for a Package to be executed upon abort of test execution or ERROR/FAILED.")) will be executed

This overrides settings from the parent element or from the test configuration.

Parameters:  level : int[¶](#ApiClient.StimulationPackageCall.SetErrorRecoveryPkgLevel.level "Permalink to this definition")  
- -1  
  disabled

- 0 on abort only

- 1 on ERROR and on abort

- 2 on FAILED, ERROR and abort.

SetErrorRecoveryPkgPath(*[packagePath](#ApiClient.StimulationPackageCall.SetErrorRecoveryPkgPath.packagePath "ApiClient.StimulationPackageCall.SetErrorRecoveryPkgPath.packagePath (Python parameter) — Absolute path to Package file")*)[¶](#ApiClient.StimulationPackageCall.SetErrorRecoveryPkgPath "Link to this definition")  
Sets the path for a Package to be executed upon abort of test execution or ERROR/FAILED.

This overrides settings from the parent element or from the test configuration.

See also [`SetErrorRecoveryPkgLevel()`](#ApiClient.StimulationPackageCall.SetErrorRecoveryPkgLevel "ApiClient.StimulationPackageCall.SetErrorRecoveryPkgLevel (Python method) — Sets the conditions under which the error recovery package (configured via SetErrorRecoveryPkgPath()) will be executed")

Parameters:  packagePath : str[¶](#ApiClient.StimulationPackageCall.SetErrorRecoveryPkgPath.packagePath "Permalink to this definition")  
Absolute path to Package file

SetName(*[name](#ApiClient.StimulationPackageCall.SetName.name "ApiClient.StimulationPackageCall.SetName.name (Python parameter) — Name of the component")*)[¶](#ApiClient.StimulationPackageCall.SetName "Link to this definition")  
Sets the name of the project component.

Parameters:  name : str[¶](#ApiClient.StimulationPackageCall.SetName.name "Permalink to this definition")  
Name of the component

SetReported(*[state](#ApiClient.StimulationPackageCall.SetReported.state "ApiClient.StimulationPackageCall.SetReported.state (Python parameter) — True (=Default) to enable, False to disable the reporting of the test step.")=`True`*)[¶](#ApiClient.StimulationPackageCall.SetReported "Link to this definition")  
Enable or disable the reporting of the test step. If it has a parent test step, its reporting must also be enabled in order to have this test step appear in the report.

Parameters:  state : bool[¶](#ApiClient.StimulationPackageCall.SetReported.state "Permalink to this definition")  
True (=Default) to enable, False to disable the reporting of the test step.

SetTestCaseId(*[testCaseId](#ApiClient.StimulationPackageCall.SetTestCaseId.testCaseId "ApiClient.StimulationPackageCall.SetTestCaseId.testCaseId (Python parameter) — Test case id")*)[¶](#ApiClient.StimulationPackageCall.SetTestCaseId "Link to this definition")  
Sets the test case id of the current package test.

Parameters:  testCaseId : str[¶](#ApiClient.StimulationPackageCall.SetTestCaseId.testCaseId "Permalink to this definition")  
Test case id

UseParentErrorRecoveryPackageSettings()[¶](#ApiClient.StimulationPackageCall.UseParentErrorRecoveryPackageSettings "Link to this definition")  
Sets that the Package execution settings in case of test abort or ERROR/FAILED of the parent element are used. Existing custom settings are deleted.

UseParentRetrySettings()[¶](#ApiClient.StimulationPackageCall.UseParentRetrySettings "Link to this definition")  
Sets that the retry settings of the parent element are used. Existing custom settings are deleted.

UseParentValueRestoreSettings()[¶](#ApiClient.StimulationPackageCall.UseParentValueRestoreSettings "Link to this definition")  
Sets that the settings whether to restore the value of test quantities after the execution of every Package of the parent element are used. Existing custom settings are deleted.

GetPosition()[¶](#ApiClient.StimulationPackageCall.GetPosition "Link to this definition")  
Returns the position in the parent project.

Returns:  parent position

Return type:  int

Deprecated since version 2024.4: Please use method [`GetLineNo`](#ApiClient.StimulationPackageCall.GetLineNo "ApiClient.StimulationPackageCall.GetLineNo (Python method) — Returns the line number within its project.") instead.

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
