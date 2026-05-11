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

Bus [ Bus ](#)

Bus

- [C Bus ](#ApiClient.Bus)
  - [M Clone ](#ApiClient.Bus.Clone)
  - [M GetAccessPort ](#ApiClient.Bus.GetAccessPort)
  - [M GetAvailableChannelsAndProtocols ](#ApiClient.Bus.GetAvailableChannelsAndProtocols)
  - [M GetChannel ](#ApiClient.Bus.GetChannel)
  - [M GetDatabaseArtifactReference ](#ApiClient.Bus.GetDatabaseArtifactReference)
  - [M GetDatabaseFile ](#ApiClient.Bus.GetDatabaseFile)
  - [M GetName ](#ApiClient.Bus.GetName)
  - [M GetProtocol ](#ApiClient.Bus.GetProtocol)
  - [M Rename ](#ApiClient.Bus.Rename)
  - [M SetAccessPort ](#ApiClient.Bus.SetAccessPort)
  - [M SetChannel ](#ApiClient.Bus.SetChannel)
  - [M SetDatabaseArtifactReference ](#ApiClient.Bus.SetDatabaseArtifactReference)
  - [M SetDatabaseFile ](#ApiClient.Bus.SetDatabaseFile)
  - [M SetProtocol ](#ApiClient.Bus.SetProtocol)

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

Bus

- [C Bus ](#ApiClient.Bus)
  - [M Clone ](#ApiClient.Bus.Clone)
  - [M GetAccessPort ](#ApiClient.Bus.GetAccessPort)
  - [M GetAvailableChannelsAndProtocols ](#ApiClient.Bus.GetAvailableChannelsAndProtocols)
  - [M GetChannel ](#ApiClient.Bus.GetChannel)
  - [M GetDatabaseArtifactReference ](#ApiClient.Bus.GetDatabaseArtifactReference)
  - [M GetDatabaseFile ](#ApiClient.Bus.GetDatabaseFile)
  - [M GetName ](#ApiClient.Bus.GetName)
  - [M GetProtocol ](#ApiClient.Bus.GetProtocol)
  - [M Rename ](#ApiClient.Bus.Rename)
  - [M SetAccessPort ](#ApiClient.Bus.SetAccessPort)
  - [M SetChannel ](#ApiClient.Bus.SetChannel)
  - [M SetDatabaseArtifactReference ](#ApiClient.Bus.SetDatabaseArtifactReference)
  - [M SetDatabaseFile ](#ApiClient.Bus.SetDatabaseFile)
  - [M SetProtocol ](#ApiClient.Bus.SetProtocol)

# Bus[¶](#bus "Link to this heading")

*class* Bus[¶](#ApiClient.Bus "Link to this definition")  
Clone()[¶](#ApiClient.Bus.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`Bus`](#ApiClient.Bus "ApiClient.Bus (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")

GetAccessPort(*[accessType](#ApiClient.Bus.GetAccessPort.accessType "ApiClient.Bus.GetAccessPort.accessType (Python parameter) — 'AccessActiveNode', 'AccessManipulation', 'ServiceApplicationLayer'")*)[¶](#ApiClient.Bus.GetAccessPort "Link to this definition")  
Returns the bus port dependent on accessType.

Parameters:  accessType : str[¶](#ApiClient.Bus.GetAccessPort.accessType "Permalink to this definition")  
‘AccessActiveNode’, ‘AccessManipulation’, ‘ServiceApplicationLayer’

Returns:  Bus port

Return type:  str

GetAvailableChannelsAndProtocols()[¶](#ApiClient.Bus.GetAvailableChannelsAndProtocols "Link to this definition")  
Returns a list of all available channels and protocols of the bus.

Returns:  List of tuples (channel name, protocol)

Return type:  list[list[str]]

GetChannel()[¶](#ApiClient.Bus.GetChannel "Link to this definition")  
Returns the channel of the bus.

Returns:  Channel of the bus

Return type:  str

GetDatabaseArtifactReference()[¶](#ApiClient.Bus.GetDatabaseArtifactReference "Link to this definition")  
Returns the bus database artifact reference.

Returns:  The bus database artifact reference

Return type:  [`ArtifactReference`](../ComponentApi/ArtifactReference.md#ApiClient.ArtifactReference "ApiClient.ArtifactReference (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")

GetDatabaseFile()[¶](#ApiClient.Bus.GetDatabaseFile "Link to this definition")  
Returns the bus database file.

Returns:  The bus database file

Return type:  str

GetName()[¶](#ApiClient.Bus.GetName "Link to this definition")  
Returns the name of the bus.

Returns:  Name of the bus

Return type:  str

GetProtocol()[¶](#ApiClient.Bus.GetProtocol "Link to this definition")  
Returns the protocol of the bus.

Returns:  Protocol

Return type:  str

Rename(*[newBusKey](#ApiClient.Bus.Rename.newBusKey "ApiClient.Bus.Rename.newBusKey (Python parameter) — New name of the bus object")*)[¶](#ApiClient.Bus.Rename "Link to this definition")  
Renames the bus.

Parameters:  newBusKey : str[¶](#ApiClient.Bus.Rename.newBusKey "Permalink to this definition")  
New name of the bus object

SetAccessPort(*[accessType](#ApiClient.Bus.SetAccessPort.accessType "ApiClient.Bus.SetAccessPort.accessType (Python parameter) — 'AccessActiveNode', 'AccessManipulation', 'ServiceApplicationLayer'")*, *[accessPort](#ApiClient.Bus.SetAccessPort.accessPort "ApiClient.Bus.SetAccessPort.accessPort (Python parameter) — Port to be set")*)[¶](#ApiClient.Bus.SetAccessPort "Link to this definition")  
Sets the bus port dependent on accessType.

Parameters:  accessType : str[¶](#ApiClient.Bus.SetAccessPort.accessType "Permalink to this definition")  
‘AccessActiveNode’, ‘AccessManipulation’, ‘ServiceApplicationLayer’

accessPort : str[¶](#ApiClient.Bus.SetAccessPort.accessPort "Permalink to this definition")  
Port to be set

SetChannel(*[channel](#ApiClient.Bus.SetChannel.channel "ApiClient.Bus.SetChannel.channel (Python parameter) — Channel of the bus")*)[¶](#ApiClient.Bus.SetChannel "Link to this definition")  
Sets the channel of the bus.

Parameters:  channel : str[¶](#ApiClient.Bus.SetChannel.channel "Permalink to this definition")  
Channel of the bus

SetDatabaseArtifactReference(*[busDbReference](#ApiClient.Bus.SetDatabaseArtifactReference.busDbReference "ApiClient.Bus.SetDatabaseArtifactReference.busDbReference (Python parameter) — bus database artifact reference to be set")*)[¶](#ApiClient.Bus.SetDatabaseArtifactReference "Link to this definition")  
Sets the bus database artifact reference.

Parameters:  busDbReference[¶](#ApiClient.Bus.SetDatabaseArtifactReference.busDbReference "Permalink to this definition")  
bus database artifact reference to be set

SetDatabaseFile(*[database](#ApiClient.Bus.SetDatabaseFile.database "ApiClient.Bus.SetDatabaseFile.database (Python parameter) — The bus database file")*)[¶](#ApiClient.Bus.SetDatabaseFile "Link to this definition")  
Sets the bus database file.

Parameters:  database : str[¶](#ApiClient.Bus.SetDatabaseFile.database "Permalink to this definition")  
The bus database file

SetProtocol(*[protocol](#ApiClient.Bus.SetProtocol.protocol "ApiClient.Bus.SetProtocol.protocol (Python parameter) — Protocol to be set")*)[¶](#ApiClient.Bus.SetProtocol "Link to this definition")  
Sets the protocol of the bus.

Parameters:  protocol : str[¶](#ApiClient.Bus.SetProtocol.protocol "Permalink to this definition")  
Protocol to be set

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
