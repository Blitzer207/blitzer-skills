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

DiagSettings [ DiagSettings ](#)

DiagSettings

- [C DiagSettings ](#ApiClient.DiagSettings)
  - [A CanIsoTpSettings ](#ApiClient.DiagSettings.CanIsoTpSettings)
  - [A DoIPSettings ](#ApiClient.DiagSettings.DoIPSettings)
  - [A DoSoAdSettings ](#ApiClient.DiagSettings.DoSoAdSettings)
  - [A FrTpSettings ](#ApiClient.DiagSettings.FrTpSettings)
  - [A HSFZSettings ](#ApiClient.DiagSettings.HSFZSettings)
  - [A UdsSettings ](#ApiClient.DiagSettings.UdsSettings)
  - [M Clone ](#ApiClient.DiagSettings.Clone)

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

DiagSettings

- [C DiagSettings ](#ApiClient.DiagSettings)
  - [A CanIsoTpSettings ](#ApiClient.DiagSettings.CanIsoTpSettings)
  - [A DoIPSettings ](#ApiClient.DiagSettings.DoIPSettings)
  - [A DoSoAdSettings ](#ApiClient.DiagSettings.DoSoAdSettings)
  - [A FrTpSettings ](#ApiClient.DiagSettings.FrTpSettings)
  - [A HSFZSettings ](#ApiClient.DiagSettings.HSFZSettings)
  - [A UdsSettings ](#ApiClient.DiagSettings.UdsSettings)
  - [M Clone ](#ApiClient.DiagSettings.Clone)

# DiagSettings[¶](#diagsettings "Link to this heading")

*class* DiagSettings[¶](#ApiClient.DiagSettings "Link to this definition")  
CanIsoTpSettings[¶](#ApiClient.DiagSettings.CanIsoTpSettings "Link to this definition")  
Access to the CAN ISO-TP settings

Returns:  ISO-TP settings

Return type:  [`CanIsoTpSettings`](CanIsoTpSettings.md#ApiClient.CanIsoTpSettings "ApiClient.CanIsoTpSettings (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")

DoIPSettings[¶](#ApiClient.DiagSettings.DoIPSettings "Link to this definition")  
Access to the DoIP settings

Returns:  DoIP settings

Return type:  [`DoIpSettings`](DoIpSettings.md#ApiClient.DoIpSettings "ApiClient.DoIpSettings (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")

DoSoAdSettings[¶](#ApiClient.DiagSettings.DoSoAdSettings "Link to this definition")  
Access to DoSoAd settings

Returns:  DoSoAd Settings

Return type:  [`DoSoAdSettings`](DoSoAdSettings.md#ApiClient.DoSoAdSettings "ApiClient.DoSoAdSettings (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")

FrTpSettings[¶](#ApiClient.DiagSettings.FrTpSettings "Link to this definition")  
Access to the Flexray ISO-TP settings

Returns:  TP settings

Return type:  [`FrTpSettings`](FrTpSettings.md#ApiClient.FrTpSettings "ApiClient.FrTpSettings (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")

HSFZSettings[¶](#ApiClient.DiagSettings.HSFZSettings "Link to this definition")  
Access to HSFZ settings

Returns:  HSFZ Settings

Return type:  [`HSFZSettings`](HSFZSettings.md#ApiClient.HSFZSettings "ApiClient.HSFZSettings (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")

UdsSettings[¶](#ApiClient.DiagSettings.UdsSettings "Link to this definition")  
Access to the UDS settings

Returns:  UDS/KWP2000 settings

Return type:  [`UdsSettings`](UdsSettings.md#ApiClient.UdsSettings "ApiClient.UdsSettings (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")

Clone()[¶](#ApiClient.DiagSettings.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`DiagSettings`](#ApiClient.DiagSettings "ApiClient.DiagSettings (Python class) — Access to the CAN ISO-TP settings")

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
