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

API for Configurations

[ Bus ](Bus.md)

[ BusAccess ](BusAccess.md)

[ CanIsoTpSettings ](CanIsoTpSettings.md)

[ Change ](Change.md)

[ Common ](Common.md)

[ ControlUnit ](ControlUnit.md)

[ ControlUnits ](ControlUnits.md)

[ DiagSettings ](DiagSettings.md)

[ DoIpSettings ](DoIpSettings.md)

[ DoSoAdSettings ](DoSoAdSettings.md)

[ EnvComAccess ](EnvComAccess.md)

[ EnvComData ](EnvComData.md)

[ EnvSimAccess ](EnvSimAccess.md)

[ EnvSimData ](EnvSimData.md)

[ Environment ](Environment.md)

[ Execution ](Execution.md)

[ FailureSimulation ](FailureSimulation.md)

[ FailureSimulationAccess ](FailureSimulationAccess.md)

[ FrTpSettings ](FrTpSettings.md)

[ Function ](Function.md)

[ FunctionAccess ](FunctionAccess.md)

[ HSFZSettings ](HSFZSettings.md)

[ Media ](Media.md)

[ MediaAccess ](MediaAccess.md)

[ Model ](Model.md)

[ ModelAccess ](ModelAccess.md)

[ Platform ](Platform.md)

[ Port ](Port.md)

[ Property ](Property.md)

[ PropertySet ](PropertySet.md)

[ ReportData ](ReportData.md)

[ ReportFormat ](ReportFormat.md)

[ TestBenchConfiguration ](TestBenchConfiguration.md)

[ TestConfiguration ](TestConfiguration.md)

[ TestConfigurationGlobalConstants ](TestConfigurationGlobalConstants.md)

[ Tool ](Tool.md)

[ ToolHost ](ToolHost.md)

[ UdsSettings ](UdsSettings.md)

UserReportData [ UserReportData ](#)

UserReportData

- [C UserReportData ](#ApiClient.UserReportData)
  - [M AppendEntry ](#ApiClient.UserReportData.AppendEntry)
  - [M Clone ](#ApiClient.UserReportData.Clone)
  - [M GetAllEntryNames ](#ApiClient.UserReportData.GetAllEntryNames)
  - [M GetDescription ](#ApiClient.UserReportData.GetDescription)
  - [M GetValue ](#ApiClient.UserReportData.GetValue)
  - [M RemoveEntry ](#ApiClient.UserReportData.RemoveEntry)
  - [M SetDescription ](#ApiClient.UserReportData.SetDescription)
  - [M SetValue ](#ApiClient.UserReportData.SetValue)

[ ValueDifference ](ValueDifference.md)

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

UserReportData

- [C UserReportData ](#ApiClient.UserReportData)
  - [M AppendEntry ](#ApiClient.UserReportData.AppendEntry)
  - [M Clone ](#ApiClient.UserReportData.Clone)
  - [M GetAllEntryNames ](#ApiClient.UserReportData.GetAllEntryNames)
  - [M GetDescription ](#ApiClient.UserReportData.GetDescription)
  - [M GetValue ](#ApiClient.UserReportData.GetValue)
  - [M RemoveEntry ](#ApiClient.UserReportData.RemoveEntry)
  - [M SetDescription ](#ApiClient.UserReportData.SetDescription)
  - [M SetValue ](#ApiClient.UserReportData.SetValue)

# UserReportData[¶](#userreportdata "Link to this heading")

*class* UserReportData[¶](#ApiClient.UserReportData "Link to this definition")  
AppendEntry(*[name](#ApiClient.UserReportData.AppendEntry.name "ApiClient.UserReportData.AppendEntry.name (Python parameter) — Name of the entry")*, *[value](#ApiClient.UserReportData.AppendEntry.value "ApiClient.UserReportData.AppendEntry.value (Python parameter) — Value of the entry")=`None`*, *[description](#ApiClient.UserReportData.AppendEntry.description "ApiClient.UserReportData.AppendEntry.description (Python parameter) — Description of the entry")=`None`*)[¶](#ApiClient.UserReportData.AppendEntry "Link to this definition")  
Appends a new entry. If a entry with the same name already exists, it will be overwritten.

Parameters:  name : str[¶](#ApiClient.UserReportData.AppendEntry.name "Permalink to this definition")  
Name of the entry

value : str[¶](#ApiClient.UserReportData.AppendEntry.value "Permalink to this definition")  
Value of the entry

description : str[¶](#ApiClient.UserReportData.AppendEntry.description "Permalink to this definition")  
Description of the entry

Clone()[¶](#ApiClient.UserReportData.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`UserReportData`](#ApiClient.UserReportData "ApiClient.UserReportData (Python class) — Appends a new entry. If a entry with the same name already exists, it will be overwritten.")

GetAllEntryNames()[¶](#ApiClient.UserReportData.GetAllEntryNames "Link to this definition")  
Returns a list of all entry names.

Returns:  List of all entry names

Return type:  list[str]

GetDescription(*[name](#ApiClient.UserReportData.GetDescription.name "ApiClient.UserReportData.GetDescription.name (Python parameter) — Name of the entry")*)[¶](#ApiClient.UserReportData.GetDescription "Link to this definition")  
Returns the description of the entry specified by the given name.

Parameters:  name : str[¶](#ApiClient.UserReportData.GetDescription.name "Permalink to this definition")  
Name of the entry

Returns:  Description text

Return type:  str

GetValue(*[name](#ApiClient.UserReportData.GetValue.name "ApiClient.UserReportData.GetValue.name (Python parameter) — Name of the entry")*)[¶](#ApiClient.UserReportData.GetValue "Link to this definition")  
Returns the value of the entry specified by the given name.

Parameters:  name : str[¶](#ApiClient.UserReportData.GetValue.name "Permalink to this definition")  
Name of the entry

Returns:  Value of the entry

Return type:  str

Raises:  
**ApiError** – If the entry with the given name does not exist

RemoveEntry(*[name](#ApiClient.UserReportData.RemoveEntry.name "ApiClient.UserReportData.RemoveEntry.name (Python parameter) — Name of the entry")*)[¶](#ApiClient.UserReportData.RemoveEntry "Link to this definition")  
Removes the entry specified by the given name.

Parameters:  name : str[¶](#ApiClient.UserReportData.RemoveEntry.name "Permalink to this definition")  
Name of the entry

Returns:  True if successful. False if no entry with such name exists.

Return type:  boolean

SetDescription(*[name](#ApiClient.UserReportData.SetDescription.name "ApiClient.UserReportData.SetDescription.name (Python parameter) — Name of the entry")*, *[description](#ApiClient.UserReportData.SetDescription.description "ApiClient.UserReportData.SetDescription.description (Python parameter) — Description text")*)[¶](#ApiClient.UserReportData.SetDescription "Link to this definition")  
Sets the description of the entry specified by the given name.

Parameters:  name : str[¶](#ApiClient.UserReportData.SetDescription.name "Permalink to this definition")  
Name of the entry

description : str[¶](#ApiClient.UserReportData.SetDescription.description "Permalink to this definition")  
Description text

Raises:  
- **ApiError** – If the entry with the given name does not exist

- **ApiError** – If description is no str

SetValue(*[name](#ApiClient.UserReportData.SetValue.name "ApiClient.UserReportData.SetValue.name (Python parameter) — Name of the entry")*, *[value](#ApiClient.UserReportData.SetValue.value "ApiClient.UserReportData.SetValue.value (Python parameter) — Value of the entry")*)[¶](#ApiClient.UserReportData.SetValue "Link to this definition")  
Sets the value of the entry specified by the given name.

Parameters:  name : str[¶](#ApiClient.UserReportData.SetValue.name "Permalink to this definition")  
Name of the entry

value : str[¶](#ApiClient.UserReportData.SetValue.value "Permalink to this definition")  
Value of the entry

Raises:  
**ApiError** – If the entry with the given name does not exist

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
