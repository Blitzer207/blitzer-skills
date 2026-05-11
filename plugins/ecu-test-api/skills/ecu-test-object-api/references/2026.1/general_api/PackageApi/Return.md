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

[ API for Configurations ](../ConfigurationApi.md)

[ API for Expectations ](../ExpectationApi.md)

[ API for Expressions ](../ExpressionApi.md)

[ API for Global Mappings ](../GlobalMappingApi.md)

[ API for Mappings ](../MappingApi.md)

[ API for Multimedia Objects ](../MultimediaApi.md)

[ API for Packages ](../PackageApi.md)

API for Packages

[ AnalysisPackage ](AnalysisPackage.md)

[ Argument ](Argument.md)

[ Attributes ](Attributes.md)

[ AutoAssignRecordingGroup ](AutoAssignRecordingGroup.md)

[ AutoAssignSignalGroup ](AutoAssignSignalGroup.md)

[ LocalMapping ](LocalMapping.md)

[ MappingTestStep ](MappingTestStep.md)

[ MappingTestStepContainer ](MappingTestStepContainer.md)

[ Package ](Package.md)

[ RecordingConfig ](RecordingConfig.md)

Return [ Return ](#)

Return

- [C Return ](#ApiClient.Return)
  - [M Clone ](#ApiClient.Return.Clone)
  - [M DeactivateExpectation ](#ApiClient.Return.DeactivateExpectation)
  - [M DeactivateSaveIn ](#ApiClient.Return.DeactivateSaveIn)
  - [M GetExpectation ](#ApiClient.Return.GetExpectation)
  - [M GetIdentifier ](#ApiClient.Return.GetIdentifier)
  - [M GetSaveInVariableName ](#ApiClient.Return.GetSaveInVariableName)
  - [M GetUnit ](#ApiClient.Return.GetUnit)
  - [M SetExpectation ](#ApiClient.Return.SetExpectation)
  - [M SetSaveInVariableName ](#ApiClient.Return.SetSaveInVariableName)
  - [M SetUnit ](#ApiClient.Return.SetUnit)

[ TestStep ](TestStep.md)

[ TestStepContainer ](TestStepContainer.md)

[ TestStepRWBase ](TestStepRWBase.md)

[ Testcase ](Testcase.md)

[ TsAXSCall ](TsAXSCall.md)

[ TsBlockBase ](TsBlockBase.md)

[ TsBusMonitoring ](TsBusMonitoring.md)

[ TsCaseNodeBase ](TsCaseNodeBase.md)

[ TsSignalGroupOperation ](TsSignalGroupOperation.md)

[ TsSwitchBase ](TsSwitchBase.md)

[ TsUserInterface ](TsUserInterface.md)

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

Return

- [C Return ](#ApiClient.Return)
  - [M Clone ](#ApiClient.Return.Clone)
  - [M DeactivateExpectation ](#ApiClient.Return.DeactivateExpectation)
  - [M DeactivateSaveIn ](#ApiClient.Return.DeactivateSaveIn)
  - [M GetExpectation ](#ApiClient.Return.GetExpectation)
  - [M GetIdentifier ](#ApiClient.Return.GetIdentifier)
  - [M GetSaveInVariableName ](#ApiClient.Return.GetSaveInVariableName)
  - [M GetUnit ](#ApiClient.Return.GetUnit)
  - [M SetExpectation ](#ApiClient.Return.SetExpectation)
  - [M SetSaveInVariableName ](#ApiClient.Return.SetSaveInVariableName)
  - [M SetUnit ](#ApiClient.Return.SetUnit)

# Return[¶](#return "Link to this heading")

*class* Return[¶](#ApiClient.Return "Link to this definition")  
Clone()[¶](#ApiClient.Return.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`Return`](#ApiClient.Return "ApiClient.Return (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")

DeactivateExpectation()[¶](#ApiClient.Return.DeactivateExpectation "Link to this definition")  
Deactivates the expectation so that the result will not be evaluated.

DeactivateSaveIn()[¶](#ApiClient.Return.DeactivateSaveIn "Link to this definition")  
Deactivates the return’s save in property, so the value will not be stored in a package variable.

GetExpectation()[¶](#ApiClient.Return.GetExpectation "Link to this definition")  
Returns the expectation expression from the evaluation of the test step, or None, if no expectation was defined.

Returns:  The expectation

Return type:  [`Expectation`](../ExpectationApi/Expectation.md#ApiClient.Expectation "ApiClient.Expectation (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")

GetIdentifier()[¶](#ApiClient.Return.GetIdentifier "Link to this definition")  
Returns the identifier of the argument.

Returns:  Identifier of return.

Return type:  str

GetSaveInVariableName()[¶](#ApiClient.Return.GetSaveInVariableName "Link to this definition")  
Returns the currently selected variable to save the return value.

Returns:  The variable’s name or None if return value is not saved to a variable by the keyword test step.

Return type:  str

GetUnit()[¶](#ApiClient.Return.GetUnit "Link to this definition")  
Returns the unit of the return.

Returns:  Unit string of return or None if no unit information is attached.

Return type:  str

SetExpectation(*[expectation](#ApiClient.Return.SetExpectation.expectation "ApiClient.Return.SetExpectation.expectation (Python parameter) — The expectation")*)[¶](#ApiClient.Return.SetExpectation "Link to this definition")  
Sets the expectation in the evaluation of the test step. The expectation will be activated if it was not enabled previously.

Parameters:  expectation[¶](#ApiClient.Return.SetExpectation.expectation "Permalink to this definition")  
The expectation

Raises:  
**ValueError** – If the expectation is not of type NumericExpectation or StringExpectation

SetSaveInVariableName(*[variableName](#ApiClient.Return.SetSaveInVariableName.variableName "ApiClient.Return.SetSaveInVariableName.variableName (Python parameter) — The variable's name.")*)[¶](#ApiClient.Return.SetSaveInVariableName "Link to this definition")  
Sets the name of the variable used for storing data by the return. The variable will be created automatically if it does not already exist in the package where the return is placed in.

Parameters:  variableName : str[¶](#ApiClient.Return.SetSaveInVariableName.variableName "Permalink to this definition")  
The variable’s name. Must not be None or an empty string.

Raises:  
**ApiError** – If variableName is None or an empty string

SetUnit(*[unit](#ApiClient.Return.SetUnit.unit "ApiClient.Return.SetUnit.unit (Python parameter) — Unit string of return.")*)[¶](#ApiClient.Return.SetUnit "Link to this definition")  
Sets the unit of the return.

Parameters:  unit : str[¶](#ApiClient.Return.SetUnit.unit "Permalink to this definition")  
Unit string of return. Use None to remove unit information.

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
