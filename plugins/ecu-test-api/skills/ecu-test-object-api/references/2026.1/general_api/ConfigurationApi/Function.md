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

Function [ Function ](#)

Function

- [C Function ](#ApiClient.Function)
  - [M Clone ](#ApiClient.Function.Clone)
  - [M GetFile ](#ApiClient.Function.GetFile)
  - [M GetName ](#ApiClient.Function.GetName)
  - [M GetPort ](#ApiClient.Function.GetPort)
  - [M Rename ](#ApiClient.Function.Rename)
  - [M SetFile ](#ApiClient.Function.SetFile)
  - [M SetPort ](#ApiClient.Function.SetPort)

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

Function

- [C Function ](#ApiClient.Function)
  - [M Clone ](#ApiClient.Function.Clone)
  - [M GetFile ](#ApiClient.Function.GetFile)
  - [M GetName ](#ApiClient.Function.GetName)
  - [M GetPort ](#ApiClient.Function.GetPort)
  - [M Rename ](#ApiClient.Function.Rename)
  - [M SetFile ](#ApiClient.Function.SetFile)
  - [M SetPort ](#ApiClient.Function.SetPort)

# Function[¶](#function "Link to this heading")

*class* Function[¶](#ApiClient.Function "Link to this definition")  
Clone()[¶](#ApiClient.Function.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`Function`](#ApiClient.Function "ApiClient.Function (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")

GetFile()[¶](#ApiClient.Function.GetFile "Link to this definition")  
Returns the function access file.

Returns:  Function access file

Return type:  str

GetName()[¶](#ApiClient.Function.GetName "Link to this definition")  
Returns the name of the function access.

Returns:  Name of the function

Return type:  str

GetPort()[¶](#ApiClient.Function.GetPort "Link to this definition")  
Returns the function access port.

Returns:  Function access port

Return type:  str

Rename(*[newFunctionKey](#ApiClient.Function.Rename.newFunctionKey "ApiClient.Function.Rename.newFunctionKey (Python parameter) — New name of the function")*)[¶](#ApiClient.Function.Rename "Link to this definition")  
Renames the function access.

Parameters:  newFunctionKey : str[¶](#ApiClient.Function.Rename.newFunctionKey "Permalink to this definition")  
New name of the function

SetFile(*[functionFile](#ApiClient.Function.SetFile.functionFile "ApiClient.Function.SetFile.functionFile (Python parameter) — Function access file to be set")*)[¶](#ApiClient.Function.SetFile "Link to this definition")  
Sets the function access file.

Parameters:  functionFile : str[¶](#ApiClient.Function.SetFile.functionFile "Permalink to this definition")  
Function access file to be set

SetPort(*[functionPort](#ApiClient.Function.SetPort.functionPort "ApiClient.Function.SetPort.functionPort (Python parameter) — Function access port to be set")*)[¶](#ApiClient.Function.SetPort "Link to this definition")  
Sets the function access port.

Parameters:  functionPort : str[¶](#ApiClient.Function.SetPort.functionPort "Permalink to this definition")  
Function access port to be set

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
