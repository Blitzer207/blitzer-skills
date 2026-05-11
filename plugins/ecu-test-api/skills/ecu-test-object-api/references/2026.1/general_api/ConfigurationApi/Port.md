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

Port [ Port ](#)

Port

- [C Port ](#ApiClient.Port)
  - [A AUTOSTART_ALWAYS ](#ApiClient.Port.AUTOSTART_ALWAYS)
  - [A AUTOSTART_CONDITIONAL ](#ApiClient.Port.AUTOSTART_CONDITIONAL)
  - [A AUTOSTART_NEVER ](#ApiClient.Port.AUTOSTART_NEVER)
  - [A PropertySet ](#ApiClient.Port.PropertySet)
  - [M Clone ](#ApiClient.Port.Clone)
  - [M GetAutostart ](#ApiClient.Port.GetAutostart)
  - [M GetId ](#ApiClient.Port.GetId)
  - [M GetImplType ](#ApiClient.Port.GetImplType)
  - [M GetPortType ](#ApiClient.Port.GetPortType)
  - [M Refresh ](#ApiClient.Port.Refresh)
  - [M Rename ](#ApiClient.Port.Rename)
  - [M SetAutostart ](#ApiClient.Port.SetAutostart)

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

[ UserReportData ](UserReportData.md)

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

Port

- [C Port ](#ApiClient.Port)
  - [A AUTOSTART_ALWAYS ](#ApiClient.Port.AUTOSTART_ALWAYS)
  - [A AUTOSTART_CONDITIONAL ](#ApiClient.Port.AUTOSTART_CONDITIONAL)
  - [A AUTOSTART_NEVER ](#ApiClient.Port.AUTOSTART_NEVER)
  - [A PropertySet ](#ApiClient.Port.PropertySet)
  - [M Clone ](#ApiClient.Port.Clone)
  - [M GetAutostart ](#ApiClient.Port.GetAutostart)
  - [M GetId ](#ApiClient.Port.GetId)
  - [M GetImplType ](#ApiClient.Port.GetImplType)
  - [M GetPortType ](#ApiClient.Port.GetPortType)
  - [M Refresh ](#ApiClient.Port.Refresh)
  - [M Rename ](#ApiClient.Port.Rename)
  - [M SetAutostart ](#ApiClient.Port.SetAutostart)

# Port[¶](#port "Link to this heading")

*class* Port[¶](#ApiClient.Port "Link to this definition")  
AUTOSTART_ALWAYS[¶](#ApiClient.Port.AUTOSTART_ALWAYS "Link to this definition")  
Returns the constant used to specify the autostart option ‘always’: The port will always be started.

Returns:  The constant

Return type:  int

AUTOSTART_CONDITIONAL[¶](#ApiClient.Port.AUTOSTART_CONDITIONAL "Link to this definition")  
Returns the constant used to specify the autostart option ‘conditional’: The port will be started when needed.

Returns:  The constant

Return type:  int

AUTOSTART_NEVER[¶](#ApiClient.Port.AUTOSTART_NEVER "Link to this definition")  
Returns the constant used to specify the autostart option ‘never’: The port will never be started automatically.

Returns:  The constant

Return type:  int

PropertySet[¶](#ApiClient.Port.PropertySet "Link to this definition")  
The properties of this port.

Returns:  properties of this port

Return type:  [`PropertySet`](PropertySet.md#ApiClient.PropertySet "ApiClient.PropertySet (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")

Clone()[¶](#ApiClient.Port.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`Port`](#ApiClient.Port "ApiClient.Port (Python class) — Returns the constant used to specify the autostart option 'always': The port will always be started.")

GetAutostart()[¶](#ApiClient.Port.GetAutostart "Link to this definition")  
Returns the autostart mode for this port.

Returns:  Autostart option of the port.

- [`Port.AUTOSTART_CONDITIONAL`](#ApiClient.Port.AUTOSTART_CONDITIONAL "ApiClient.Port.AUTOSTART_CONDITIONAL (Python attribute) — Returns the constant used to specify the autostart option 'conditional': The port will be started when needed.")

- [`Port.AUTOSTART_ALWAYS`](#ApiClient.Port.AUTOSTART_ALWAYS "ApiClient.Port.AUTOSTART_ALWAYS (Python attribute) — Returns the constant used to specify the autostart option 'always': The port will always be started.")

- [`Port.AUTOSTART_NEVER`](#ApiClient.Port.AUTOSTART_NEVER "ApiClient.Port.AUTOSTART_NEVER (Python attribute) — Returns the constant used to specify the autostart option 'never': The port will never be started automatically.")

Return type:  int

GetId()[¶](#ApiClient.Port.GetId "Link to this definition")  
Returns the id of the port.

Returns:  The id of the port.

Return type:  str

GetImplType()[¶](#ApiClient.Port.GetImplType "Link to this definition")  
Returns the port’s implementation type :return: the implementation type :rtype: str

GetPortType()[¶](#ApiClient.Port.GetPortType "Link to this definition")  
Returns the type of the port.

Returns:  The type of the port.

Return type:  str

Refresh()[¶](#ApiClient.Port.Refresh "Link to this definition")  
Refreshes the properties of the port

Rename(*[newPortId](#ApiClient.Port.Rename.newPortId "ApiClient.Port.Rename.newPortId (Python parameter) — The new id to be used.")*)[¶](#ApiClient.Port.Rename "Link to this definition")  
Changes the id of the port to the given one.

Parameters:  newPortId : str[¶](#ApiClient.Port.Rename.newPortId "Permalink to this definition")  
The new id to be used.

Raises:  
**ApiError** – If newPortId could not be set

SetAutostart(*[option](#ApiClient.Port.SetAutostart.option "ApiClient.Port.SetAutostart.option (Python parameter) — New autostart option for the port.")*)[¶](#ApiClient.Port.SetAutostart "Link to this definition")  
Sets the autostart option of the port.

Parameters:  option : int[¶](#ApiClient.Port.SetAutostart.option "Permalink to this definition")  
New autostart option for the port. Possible values are:

- [`Port.AUTOSTART_CONDITIONAL`](#ApiClient.Port.AUTOSTART_CONDITIONAL "ApiClient.Port.AUTOSTART_CONDITIONAL (Python attribute) — Returns the constant used to specify the autostart option 'conditional': The port will be started when needed.")

- [`Port.AUTOSTART_ALWAYS`](#ApiClient.Port.AUTOSTART_ALWAYS "ApiClient.Port.AUTOSTART_ALWAYS (Python attribute) — Returns the constant used to specify the autostart option 'always': The port will always be started.")

- [`Port.AUTOSTART_NEVER`](#ApiClient.Port.AUTOSTART_NEVER "ApiClient.Port.AUTOSTART_NEVER (Python attribute) — Returns the constant used to specify the autostart option 'never': The port will never be started automatically.")

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
