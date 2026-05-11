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

Argument [ Argument ](#)

Argument

- [C Argument ](#ApiClient.Argument)
  - [M Clone ](#ApiClient.Argument.Clone)
  - [M GetIdentifier ](#ApiClient.Argument.GetIdentifier)
  - [M GetUnit ](#ApiClient.Argument.GetUnit)
  - [M GetValueExpression ](#ApiClient.Argument.GetValueExpression)
  - [M SetUnit ](#ApiClient.Argument.SetUnit)
  - [M SetValueExpression ](#ApiClient.Argument.SetValueExpression)
  - [M SetValueRangeExpression ](#ApiClient.Argument.SetValueRangeExpression)

[ Attributes ](Attributes.md)

[ AutoAssignRecordingGroup ](AutoAssignRecordingGroup.md)

[ AutoAssignSignalGroup ](AutoAssignSignalGroup.md)

[ LocalMapping ](LocalMapping.md)

[ MappingTestStep ](MappingTestStep.md)

[ MappingTestStepContainer ](MappingTestStepContainer.md)

[ Package ](Package.md)

[ RecordingConfig ](RecordingConfig.md)

[ Return ](Return.md)

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

Argument

- [C Argument ](#ApiClient.Argument)
  - [M Clone ](#ApiClient.Argument.Clone)
  - [M GetIdentifier ](#ApiClient.Argument.GetIdentifier)
  - [M GetUnit ](#ApiClient.Argument.GetUnit)
  - [M GetValueExpression ](#ApiClient.Argument.GetValueExpression)
  - [M SetUnit ](#ApiClient.Argument.SetUnit)
  - [M SetValueExpression ](#ApiClient.Argument.SetValueExpression)
  - [M SetValueRangeExpression ](#ApiClient.Argument.SetValueRangeExpression)

# Argument[¶](#argument "Link to this heading")

*class* Argument[¶](#ApiClient.Argument "Link to this definition")  
Clone()[¶](#ApiClient.Argument.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`Argument`](#ApiClient.Argument "ApiClient.Argument (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")

GetIdentifier()[¶](#ApiClient.Argument.GetIdentifier "Link to this definition")  
Returns the identifier of the argument.

Returns:  Identifier of argument.

Return type:  str

GetUnit()[¶](#ApiClient.Argument.GetUnit "Link to this definition")  
Returns the unit of the argument.

Returns:  Unit string of argument or None if no unit information is attached.

Return type:  str

GetValueExpression()[¶](#ApiClient.Argument.GetValueExpression "Link to this definition")  
Returns the value expression of the argument.

Returns:  Expression of argument.

Return type:  str

SetUnit(*[unit](#ApiClient.Argument.SetUnit.unit "ApiClient.Argument.SetUnit.unit (Python parameter) — Unit string of argument.")*)[¶](#ApiClient.Argument.SetUnit "Link to this definition")  
Sets the unit of the argument.

Parameters:  unit : str[¶](#ApiClient.Argument.SetUnit.unit "Permalink to this definition")  
Unit string of argument. Use None to remove unit information.

SetValueExpression(*[value](#ApiClient.Argument.SetValueExpression.value "ApiClient.Argument.SetValueExpression.value (Python parameter) — Expression of argument.")*)[¶](#ApiClient.Argument.SetValueExpression "Link to this definition")  
Sets the value expression of the argument.

Parameters:  value : str[¶](#ApiClient.Argument.SetValueExpression.value "Permalink to this definition")  
Expression of argument.

SetValueRangeExpression(*[minValue](#ApiClient.Argument.SetValueRangeExpression.minValue "ApiClient.Argument.SetValueRangeExpression.minValue (Python parameter) — Expression of the lower limit")*, *[maxValue](#ApiClient.Argument.SetValueRangeExpression.maxValue "ApiClient.Argument.SetValueRangeExpression.maxValue (Python parameter) — Expression of the upper limit")*, *[stepSize](#ApiClient.Argument.SetValueRangeExpression.stepSize "ApiClient.Argument.SetValueRangeExpression.stepSize (Python parameter) — Expression of the step size")*, *[includeMinValue](#ApiClient.Argument.SetValueRangeExpression.includeMinValue "ApiClient.Argument.SetValueRangeExpression.includeMinValue (Python parameter) — If True (default) the minimum value is a candidate for the random value at runtime.")=`True`*, *[includeMaxValue](#ApiClient.Argument.SetValueRangeExpression.includeMaxValue "ApiClient.Argument.SetValueRangeExpression.includeMaxValue (Python parameter) — If True the maximum value is a candidate for the random value at runtime; if False (default) it is not.")=`False`*)[¶](#ApiClient.Argument.SetValueRangeExpression "Link to this definition")  
Special method to define a range as value expression for the argument.

Parameters:  minValue : str[¶](#ApiClient.Argument.SetValueRangeExpression.minValue "Permalink to this definition")  
Expression of the lower limit

maxValue : str[¶](#ApiClient.Argument.SetValueRangeExpression.maxValue "Permalink to this definition")  
Expression of the upper limit

stepSize : str[¶](#ApiClient.Argument.SetValueRangeExpression.stepSize "Permalink to this definition")  
Expression of the step size

includeMinValue : boolean[¶](#ApiClient.Argument.SetValueRangeExpression.includeMinValue "Permalink to this definition")  
If True (default) the minimum value is a candidate for the random value at runtime. If False it is not a possible candidate to pick from.

includeMaxValue : boolean[¶](#ApiClient.Argument.SetValueRangeExpression.includeMaxValue "Permalink to this definition")  
If True the maximum value is a candidate for the random value at runtime; if False (default) it is not.

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
