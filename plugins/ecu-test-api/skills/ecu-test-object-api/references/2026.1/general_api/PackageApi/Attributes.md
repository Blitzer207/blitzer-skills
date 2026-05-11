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

Attributes [ Attributes ](#)

Attributes

- [C Attributes ](#ApiClient.Attributes)
  - [M Clone ](#ApiClient.Attributes.Clone)
  - [M GetNames ](#ApiClient.Attributes.GetNames)
  - [M GetNamesAndValues ](#ApiClient.Attributes.GetNamesAndValues)
  - [M GetValue ](#ApiClient.Attributes.GetValue)
  - [M SetValue ](#ApiClient.Attributes.SetValue)

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

Attributes

- [C Attributes ](#ApiClient.Attributes)
  - [M Clone ](#ApiClient.Attributes.Clone)
  - [M GetNames ](#ApiClient.Attributes.GetNames)
  - [M GetNamesAndValues ](#ApiClient.Attributes.GetNamesAndValues)
  - [M GetValue ](#ApiClient.Attributes.GetValue)
  - [M SetValue ](#ApiClient.Attributes.SetValue)

# Attributes[¶](#attributes "Link to this heading")

*class* Attributes[¶](#ApiClient.Attributes "Link to this definition")  
API to access attributes

Clone()[¶](#ApiClient.Attributes.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`Attributes`](#ApiClient.Attributes "ApiClient.Attributes (Python class) — API to access attributes")

GetNames()[¶](#ApiClient.Attributes.GetNames "Link to this definition")  
Returns the names of all attributes available

Returns:  List of attribute names

Return type:  list[str]

GetNamesAndValues()[¶](#ApiClient.Attributes.GetNamesAndValues "Link to this definition")  
Returns all attributes with their values.

Returns:  Dictionary of attributes with values

Return type:  dict[str, str]

GetValue(*[name](#ApiClient.Attributes.GetValue.name "ApiClient.Attributes.GetValue.name (Python parameter) — Name of attribute")*)[¶](#ApiClient.Attributes.GetValue "Link to this definition")  
Returns the value of the attribute of the provided name

Parameters:  name : str[¶](#ApiClient.Attributes.GetValue.name "Permalink to this definition")  
Name of attribute

Returns:  Value of attribute

Return type:  str

SetValue(*[name](#ApiClient.Attributes.SetValue.name "ApiClient.Attributes.SetValue.name (Python parameter) — Name of attribute")*, *[value](#ApiClient.Attributes.SetValue.value "ApiClient.Attributes.SetValue.value (Python parameter) — Value of attribute")*)[¶](#ApiClient.Attributes.SetValue "Link to this definition")  
Sets the value of an attribute with the provided name.

Parameters:  name : str[¶](#ApiClient.Attributes.SetValue.name "Permalink to this definition")  
Name of attribute

value : str[¶](#ApiClient.Attributes.SetValue.value "Permalink to this definition")  
Value of attribute

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
