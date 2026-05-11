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

EnvSimData [ EnvSimData ](#)

EnvSimData

- [C EnvSimData ](#ApiClient.EnvSimData)
  - [M Clone ](#ApiClient.EnvSimData.Clone)
  - [M GetDataSource ](#ApiClient.EnvSimData.GetDataSource)
  - [M GetName ](#ApiClient.EnvSimData.GetName)
  - [M GetOfflineFile ](#ApiClient.EnvSimData.GetOfflineFile)
  - [M GetPort ](#ApiClient.EnvSimData.GetPort)
  - [M Rename ](#ApiClient.EnvSimData.Rename)
  - [M SetDataSource ](#ApiClient.EnvSimData.SetDataSource)
  - [M SetOfflineFile ](#ApiClient.EnvSimData.SetOfflineFile)
  - [M SetPort ](#ApiClient.EnvSimData.SetPort)

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

EnvSimData

- [C EnvSimData ](#ApiClient.EnvSimData)
  - [M Clone ](#ApiClient.EnvSimData.Clone)
  - [M GetDataSource ](#ApiClient.EnvSimData.GetDataSource)
  - [M GetName ](#ApiClient.EnvSimData.GetName)
  - [M GetOfflineFile ](#ApiClient.EnvSimData.GetOfflineFile)
  - [M GetPort ](#ApiClient.EnvSimData.GetPort)
  - [M Rename ](#ApiClient.EnvSimData.Rename)
  - [M SetDataSource ](#ApiClient.EnvSimData.SetDataSource)
  - [M SetOfflineFile ](#ApiClient.EnvSimData.SetOfflineFile)
  - [M SetPort ](#ApiClient.EnvSimData.SetPort)

# EnvSimData[¶](#envsimdata "Link to this heading")

*class* EnvSimData[¶](#ApiClient.EnvSimData "Link to this definition")  
Clone()[¶](#ApiClient.EnvSimData.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`EnvSimData`](#ApiClient.EnvSimData "ApiClient.EnvSimData (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")

GetDataSource()[¶](#ApiClient.EnvSimData.GetDataSource "Link to this definition")  
Returns the data source.

Returns:  data source: 0 online query, 1 offline file

Return type:  int

GetName()[¶](#ApiClient.EnvSimData.GetName "Link to this definition")  
Returns the name of the enviroment simulation.

Returns:  Name of the environment simulation

Return type:  str

GetOfflineFile()[¶](#ApiClient.EnvSimData.GetOfflineFile "Link to this definition")  
Returns the offline file.

Returns:  offline file

Return type:  str

GetPort()[¶](#ApiClient.EnvSimData.GetPort "Link to this definition")  
Returns the enviroment simulation port.

Returns:  environment simulation port

Return type:  str

Rename(*[newEnvironmentSimulationKey](#ApiClient.EnvSimData.Rename.newEnvironmentSimulationKey "ApiClient.EnvSimData.Rename.newEnvironmentSimulationKey (Python parameter) — New name of the environment simulation")*)[¶](#ApiClient.EnvSimData.Rename "Link to this definition")  
Renames the model.

Parameters:  newEnvironmentSimulationKey : str[¶](#ApiClient.EnvSimData.Rename.newEnvironmentSimulationKey "Permalink to this definition")  
New name of the environment simulation

SetDataSource(*[dataSource](#ApiClient.EnvSimData.SetDataSource.dataSource "ApiClient.EnvSimData.SetDataSource.dataSource (Python parameter) — data source: 0 online query, 1 offline file")*)[¶](#ApiClient.EnvSimData.SetDataSource "Link to this definition")  
Set the data source to switch between online query and offline file.

Parameters:  dataSource : int[¶](#ApiClient.EnvSimData.SetDataSource.dataSource "Permalink to this definition")  
data source: 0 online query, 1 offline file

SetOfflineFile(*[offlineFile](#ApiClient.EnvSimData.SetOfflineFile.offlineFile "ApiClient.EnvSimData.SetOfflineFile.offlineFile (Python parameter) — offline file to be set")*)[¶](#ApiClient.EnvSimData.SetOfflineFile "Link to this definition")  
Sets the offline file.

Parameters:  offlineFile : str[¶](#ApiClient.EnvSimData.SetOfflineFile.offlineFile "Permalink to this definition")  
offline file to be set

SetPort(*[port](#ApiClient.EnvSimData.SetPort.port "ApiClient.EnvSimData.SetPort.port (Python parameter) — environment simulation port to be set")*)[¶](#ApiClient.EnvSimData.SetPort "Link to this definition")  
Sets the enviroment simulation port.

Parameters:  port : str[¶](#ApiClient.EnvSimData.SetPort.port "Permalink to this definition")  
environment simulation port to be set

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
