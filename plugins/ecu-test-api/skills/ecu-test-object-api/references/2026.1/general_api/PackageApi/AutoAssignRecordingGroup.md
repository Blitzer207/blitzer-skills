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

AutoAssignRecordingGroup [ AutoAssignRecordingGroup ](#)

AutoAssignRecordingGroup

- [C AutoAssignRecordingGroup ](#ApiClient.AutoAssignRecordingGroup)
  - [M GetConditionalSignalNamesForTraceAnalyses ](#ApiClient.AutoAssignRecordingGroup.GetConditionalSignalNamesForTraceAnalyses)
  - [M GetMandatorySignalNamesForTraceAnalyses ](#ApiClient.AutoAssignRecordingGroup.GetMandatorySignalNamesForTraceAnalyses)
  - [M GetName ](#ApiClient.AutoAssignRecordingGroup.GetName)
  - [M GetOptionalSignalNamesForTraceAnalyses ](#ApiClient.AutoAssignRecordingGroup.GetOptionalSignalNamesForTraceAnalyses)
  - [M GetSignalGroup ](#ApiClient.AutoAssignRecordingGroup.GetSignalGroup)

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

AutoAssignRecordingGroup

- [C AutoAssignRecordingGroup ](#ApiClient.AutoAssignRecordingGroup)
  - [M GetConditionalSignalNamesForTraceAnalyses ](#ApiClient.AutoAssignRecordingGroup.GetConditionalSignalNamesForTraceAnalyses)
  - [M GetMandatorySignalNamesForTraceAnalyses ](#ApiClient.AutoAssignRecordingGroup.GetMandatorySignalNamesForTraceAnalyses)
  - [M GetName ](#ApiClient.AutoAssignRecordingGroup.GetName)
  - [M GetOptionalSignalNamesForTraceAnalyses ](#ApiClient.AutoAssignRecordingGroup.GetOptionalSignalNamesForTraceAnalyses)
  - [M GetSignalGroup ](#ApiClient.AutoAssignRecordingGroup.GetSignalGroup)

# AutoAssignRecordingGroup[¶](#autoassignrecordinggroup "Link to this heading")

*class* AutoAssignRecordingGroup[¶](#ApiClient.AutoAssignRecordingGroup "Link to this definition")  
GetConditionalSignalNamesForTraceAnalyses()[¶](#ApiClient.AutoAssignRecordingGroup.GetConditionalSignalNamesForTraceAnalyses "Link to this definition")  
Returns the list of signal names that can be optional or mandatory for running the trace analyses depending on the values of global constants.

Returns:  The list of undetermined signal names.

Return type:  list[str]

GetMandatorySignalNamesForTraceAnalyses()[¶](#ApiClient.AutoAssignRecordingGroup.GetMandatorySignalNamesForTraceAnalyses "Link to this definition")  
Returns the list of signal names that are mandatory for running the trace analyses.

Returns:  The list of mandatory signal names.

Return type:  list[str]

GetName()[¶](#ApiClient.AutoAssignRecordingGroup.GetName "Link to this definition")  
Returns the name of a recording group.

Returns:  the name

Return type:  str

GetOptionalSignalNamesForTraceAnalyses()[¶](#ApiClient.AutoAssignRecordingGroup.GetOptionalSignalNamesForTraceAnalyses "Link to this definition")  
Returns the list of signal names that are optional for running the trace analyses.

Returns:  The list of optional signal names.

Return type:  list[str]

GetSignalGroup()[¶](#ApiClient.AutoAssignRecordingGroup.GetSignalGroup "Link to this definition")  
Returns the parent signal group.

Returns:  The parent signal group

Return type:  [`SignalGroupBase`](../SignalRecordingApi/SignalGroupBase.md#ApiClient.SignalGroupBase "ApiClient.SignalGroupBase (Python class) — API to access signal groups. Signals of a signal group are represented by references to mapping items.")

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
