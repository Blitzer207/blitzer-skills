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

ControlUnit [ ControlUnit ](#)

ControlUnit

- [C ControlUnit ](#ApiClient.ControlUnit)
  - [A DiagSettings ](#ApiClient.ControlUnit.DiagSettings)
  - [M Clone ](#ApiClient.ControlUnit.Clone)
  - [M GetApplicationA2lArtifactReference ](#ApiClient.ControlUnit.GetApplicationA2lArtifactReference)
  - [M GetApplicationA2lFile ](#ApiClient.ControlUnit.GetApplicationA2lFile)
  - [M GetApplicationA2lTransportLayer ](#ApiClient.ControlUnit.GetApplicationA2lTransportLayer)
  - [M GetApplicationHexArtifactReference ](#ApiClient.ControlUnit.GetApplicationHexArtifactReference)
  - [M GetApplicationHexFile ](#ApiClient.ControlUnit.GetApplicationHexFile)
  - [M GetApplicationPort ](#ApiClient.ControlUnit.GetApplicationPort)
  - [M GetAvailableApplicationA2lTransportLayers ](#ApiClient.ControlUnit.GetAvailableApplicationA2lTransportLayers)
  - [M GetConnectionSettings ](#ApiClient.ControlUnit.GetConnectionSettings)
  - [M GetDebuggingElfFile ](#ApiClient.ControlUnit.GetDebuggingElfFile)
  - [M GetDebuggingElfFiles ](#ApiClient.ControlUnit.GetDebuggingElfFiles)
  - [M GetDebuggingHexArtifactReference ](#ApiClient.ControlUnit.GetDebuggingHexArtifactReference)
  - [M GetDebuggingHexFile ](#ApiClient.ControlUnit.GetDebuggingHexFile)
  - [M GetDebuggingPort ](#ApiClient.ControlUnit.GetDebuggingPort)
  - [M GetDiagnosticDb ](#ApiClient.ControlUnit.GetDiagnosticDb)
  - [M GetDiagnosticPort ](#ApiClient.ControlUnit.GetDiagnosticPort)
  - [M GetDiagnosticsLogicalLink ](#ApiClient.ControlUnit.GetDiagnosticsLogicalLink)
  - [M GetDiagnosticsPortDts ](#ApiClient.ControlUnit.GetDiagnosticsPortDts)
  - [M GetDiagnosticsPortEdiabas ](#ApiClient.ControlUnit.GetDiagnosticsPortEdiabas)
  - [M GetDiagnosticsSgbdFile ](#ApiClient.ControlUnit.GetDiagnosticsSgbdFile)
  - [M GetEcuVariant ](#ApiClient.ControlUnit.GetEcuVariant)
  - [M GetEcuVariants ](#ApiClient.ControlUnit.GetEcuVariants)
  - [M GetEdiabasCertificateFile ](#ApiClient.ControlUnit.GetEdiabasCertificateFile)
  - [M GetEdiabasNetworkProtocol ](#ApiClient.ControlUnit.GetEdiabasNetworkProtocol)
  - [M GetLoggingDatabase ](#ApiClient.ControlUnit.GetLoggingDatabase)
  - [M GetLoggingDltFilterFile ](#ApiClient.ControlUnit.GetLoggingDltFilterFile)
  - [M GetLoggingEcu ](#ApiClient.ControlUnit.GetLoggingEcu)
  - [M GetLoggingEthernetIp ](#ApiClient.ControlUnit.GetLoggingEthernetIp)
  - [M GetLoggingEthernetPort ](#ApiClient.ControlUnit.GetLoggingEthernetPort)
  - [M GetLoggingEthernetProtocol ](#ApiClient.ControlUnit.GetLoggingEthernetProtocol)
  - [M GetLoggingPort ](#ApiClient.ControlUnit.GetLoggingPort)
  - [M GetLoggingProtocol ](#ApiClient.ControlUnit.GetLoggingProtocol)
  - [M GetName ](#ApiClient.ControlUnit.GetName)
  - [M GetRemotePartys ](#ApiClient.ControlUnit.GetRemotePartys)
  - [M IsDebuggingUseHexFileFromApplication ](#ApiClient.ControlUnit.IsDebuggingUseHexFileFromApplication)
  - [M RemoveApplicationA2lArtifactReference ](#ApiClient.ControlUnit.RemoveApplicationA2lArtifactReference)
  - [M RemoveApplicationHexArtifactReference ](#ApiClient.ControlUnit.RemoveApplicationHexArtifactReference)
  - [M RemoveDebuggingHexArtifactReference ](#ApiClient.ControlUnit.RemoveDebuggingHexArtifactReference)
  - [M Rename ](#ApiClient.ControlUnit.Rename)
  - [M SetApplicationA2lArtifactReference ](#ApiClient.ControlUnit.SetApplicationA2lArtifactReference)
  - [M SetApplicationA2lFile ](#ApiClient.ControlUnit.SetApplicationA2lFile)
  - [M SetApplicationA2lTransportLayer ](#ApiClient.ControlUnit.SetApplicationA2lTransportLayer)
  - [M SetApplicationHexArtifactReference ](#ApiClient.ControlUnit.SetApplicationHexArtifactReference)
  - [M SetApplicationHexFile ](#ApiClient.ControlUnit.SetApplicationHexFile)
  - [M SetApplicationPort ](#ApiClient.ControlUnit.SetApplicationPort)
  - [M SetConnectionSettings ](#ApiClient.ControlUnit.SetConnectionSettings)
  - [M SetDebuggingElfFile ](#ApiClient.ControlUnit.SetDebuggingElfFile)
  - [M SetDebuggingElfFiles ](#ApiClient.ControlUnit.SetDebuggingElfFiles)
  - [M SetDebuggingHexArtifactReference ](#ApiClient.ControlUnit.SetDebuggingHexArtifactReference)
  - [M SetDebuggingHexFile ](#ApiClient.ControlUnit.SetDebuggingHexFile)
  - [M SetDebuggingPort ](#ApiClient.ControlUnit.SetDebuggingPort)
  - [M SetDebuggingUseHexFileFromApplication ](#ApiClient.ControlUnit.SetDebuggingUseHexFileFromApplication)
  - [M SetDiagnosticDb ](#ApiClient.ControlUnit.SetDiagnosticDb)
  - [M SetDiagnosticPort ](#ApiClient.ControlUnit.SetDiagnosticPort)
  - [M SetDiagnosticsLogicalLink ](#ApiClient.ControlUnit.SetDiagnosticsLogicalLink)
  - [M SetDiagnosticsPortDts ](#ApiClient.ControlUnit.SetDiagnosticsPortDts)
  - [M SetDiagnosticsPortEdiabas ](#ApiClient.ControlUnit.SetDiagnosticsPortEdiabas)
  - [M SetDiagnosticsSgbdFile ](#ApiClient.ControlUnit.SetDiagnosticsSgbdFile)
  - [M SetEcuVariant ](#ApiClient.ControlUnit.SetEcuVariant)
  - [M SetEdiabasCertificateFile ](#ApiClient.ControlUnit.SetEdiabasCertificateFile)
  - [M SetEdiabasNetworkProtocol ](#ApiClient.ControlUnit.SetEdiabasNetworkProtocol)
  - [M SetLoggingDatabase ](#ApiClient.ControlUnit.SetLoggingDatabase)
  - [M SetLoggingDltFilterFile ](#ApiClient.ControlUnit.SetLoggingDltFilterFile)
  - [M SetLoggingEcu ](#ApiClient.ControlUnit.SetLoggingEcu)
  - [M SetLoggingEthernetIp ](#ApiClient.ControlUnit.SetLoggingEthernetIp)
  - [M SetLoggingEthernetPort ](#ApiClient.ControlUnit.SetLoggingEthernetPort)
  - [M SetLoggingEthernetProtocol ](#ApiClient.ControlUnit.SetLoggingEthernetProtocol)
  - [M SetLoggingPort ](#ApiClient.ControlUnit.SetLoggingPort)
  - [M SetLoggingProtocol ](#ApiClient.ControlUnit.SetLoggingProtocol)

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

ControlUnit

- [C ControlUnit ](#ApiClient.ControlUnit)
  - [A DiagSettings ](#ApiClient.ControlUnit.DiagSettings)
  - [M Clone ](#ApiClient.ControlUnit.Clone)
  - [M GetApplicationA2lArtifactReference ](#ApiClient.ControlUnit.GetApplicationA2lArtifactReference)
  - [M GetApplicationA2lFile ](#ApiClient.ControlUnit.GetApplicationA2lFile)
  - [M GetApplicationA2lTransportLayer ](#ApiClient.ControlUnit.GetApplicationA2lTransportLayer)
  - [M GetApplicationHexArtifactReference ](#ApiClient.ControlUnit.GetApplicationHexArtifactReference)
  - [M GetApplicationHexFile ](#ApiClient.ControlUnit.GetApplicationHexFile)
  - [M GetApplicationPort ](#ApiClient.ControlUnit.GetApplicationPort)
  - [M GetAvailableApplicationA2lTransportLayers ](#ApiClient.ControlUnit.GetAvailableApplicationA2lTransportLayers)
  - [M GetConnectionSettings ](#ApiClient.ControlUnit.GetConnectionSettings)
  - [M GetDebuggingElfFile ](#ApiClient.ControlUnit.GetDebuggingElfFile)
  - [M GetDebuggingElfFiles ](#ApiClient.ControlUnit.GetDebuggingElfFiles)
  - [M GetDebuggingHexArtifactReference ](#ApiClient.ControlUnit.GetDebuggingHexArtifactReference)
  - [M GetDebuggingHexFile ](#ApiClient.ControlUnit.GetDebuggingHexFile)
  - [M GetDebuggingPort ](#ApiClient.ControlUnit.GetDebuggingPort)
  - [M GetDiagnosticDb ](#ApiClient.ControlUnit.GetDiagnosticDb)
  - [M GetDiagnosticPort ](#ApiClient.ControlUnit.GetDiagnosticPort)
  - [M GetDiagnosticsLogicalLink ](#ApiClient.ControlUnit.GetDiagnosticsLogicalLink)
  - [M GetDiagnosticsPortDts ](#ApiClient.ControlUnit.GetDiagnosticsPortDts)
  - [M GetDiagnosticsPortEdiabas ](#ApiClient.ControlUnit.GetDiagnosticsPortEdiabas)
  - [M GetDiagnosticsSgbdFile ](#ApiClient.ControlUnit.GetDiagnosticsSgbdFile)
  - [M GetEcuVariant ](#ApiClient.ControlUnit.GetEcuVariant)
  - [M GetEcuVariants ](#ApiClient.ControlUnit.GetEcuVariants)
  - [M GetEdiabasCertificateFile ](#ApiClient.ControlUnit.GetEdiabasCertificateFile)
  - [M GetEdiabasNetworkProtocol ](#ApiClient.ControlUnit.GetEdiabasNetworkProtocol)
  - [M GetLoggingDatabase ](#ApiClient.ControlUnit.GetLoggingDatabase)
  - [M GetLoggingDltFilterFile ](#ApiClient.ControlUnit.GetLoggingDltFilterFile)
  - [M GetLoggingEcu ](#ApiClient.ControlUnit.GetLoggingEcu)
  - [M GetLoggingEthernetIp ](#ApiClient.ControlUnit.GetLoggingEthernetIp)
  - [M GetLoggingEthernetPort ](#ApiClient.ControlUnit.GetLoggingEthernetPort)
  - [M GetLoggingEthernetProtocol ](#ApiClient.ControlUnit.GetLoggingEthernetProtocol)
  - [M GetLoggingPort ](#ApiClient.ControlUnit.GetLoggingPort)
  - [M GetLoggingProtocol ](#ApiClient.ControlUnit.GetLoggingProtocol)
  - [M GetName ](#ApiClient.ControlUnit.GetName)
  - [M GetRemotePartys ](#ApiClient.ControlUnit.GetRemotePartys)
  - [M IsDebuggingUseHexFileFromApplication ](#ApiClient.ControlUnit.IsDebuggingUseHexFileFromApplication)
  - [M RemoveApplicationA2lArtifactReference ](#ApiClient.ControlUnit.RemoveApplicationA2lArtifactReference)
  - [M RemoveApplicationHexArtifactReference ](#ApiClient.ControlUnit.RemoveApplicationHexArtifactReference)
  - [M RemoveDebuggingHexArtifactReference ](#ApiClient.ControlUnit.RemoveDebuggingHexArtifactReference)
  - [M Rename ](#ApiClient.ControlUnit.Rename)
  - [M SetApplicationA2lArtifactReference ](#ApiClient.ControlUnit.SetApplicationA2lArtifactReference)
  - [M SetApplicationA2lFile ](#ApiClient.ControlUnit.SetApplicationA2lFile)
  - [M SetApplicationA2lTransportLayer ](#ApiClient.ControlUnit.SetApplicationA2lTransportLayer)
  - [M SetApplicationHexArtifactReference ](#ApiClient.ControlUnit.SetApplicationHexArtifactReference)
  - [M SetApplicationHexFile ](#ApiClient.ControlUnit.SetApplicationHexFile)
  - [M SetApplicationPort ](#ApiClient.ControlUnit.SetApplicationPort)
  - [M SetConnectionSettings ](#ApiClient.ControlUnit.SetConnectionSettings)
  - [M SetDebuggingElfFile ](#ApiClient.ControlUnit.SetDebuggingElfFile)
  - [M SetDebuggingElfFiles ](#ApiClient.ControlUnit.SetDebuggingElfFiles)
  - [M SetDebuggingHexArtifactReference ](#ApiClient.ControlUnit.SetDebuggingHexArtifactReference)
  - [M SetDebuggingHexFile ](#ApiClient.ControlUnit.SetDebuggingHexFile)
  - [M SetDebuggingPort ](#ApiClient.ControlUnit.SetDebuggingPort)
  - [M SetDebuggingUseHexFileFromApplication ](#ApiClient.ControlUnit.SetDebuggingUseHexFileFromApplication)
  - [M SetDiagnosticDb ](#ApiClient.ControlUnit.SetDiagnosticDb)
  - [M SetDiagnosticPort ](#ApiClient.ControlUnit.SetDiagnosticPort)
  - [M SetDiagnosticsLogicalLink ](#ApiClient.ControlUnit.SetDiagnosticsLogicalLink)
  - [M SetDiagnosticsPortDts ](#ApiClient.ControlUnit.SetDiagnosticsPortDts)
  - [M SetDiagnosticsPortEdiabas ](#ApiClient.ControlUnit.SetDiagnosticsPortEdiabas)
  - [M SetDiagnosticsSgbdFile ](#ApiClient.ControlUnit.SetDiagnosticsSgbdFile)
  - [M SetEcuVariant ](#ApiClient.ControlUnit.SetEcuVariant)
  - [M SetEdiabasCertificateFile ](#ApiClient.ControlUnit.SetEdiabasCertificateFile)
  - [M SetEdiabasNetworkProtocol ](#ApiClient.ControlUnit.SetEdiabasNetworkProtocol)
  - [M SetLoggingDatabase ](#ApiClient.ControlUnit.SetLoggingDatabase)
  - [M SetLoggingDltFilterFile ](#ApiClient.ControlUnit.SetLoggingDltFilterFile)
  - [M SetLoggingEcu ](#ApiClient.ControlUnit.SetLoggingEcu)
  - [M SetLoggingEthernetIp ](#ApiClient.ControlUnit.SetLoggingEthernetIp)
  - [M SetLoggingEthernetPort ](#ApiClient.ControlUnit.SetLoggingEthernetPort)
  - [M SetLoggingEthernetProtocol ](#ApiClient.ControlUnit.SetLoggingEthernetProtocol)
  - [M SetLoggingPort ](#ApiClient.ControlUnit.SetLoggingPort)
  - [M SetLoggingProtocol ](#ApiClient.ControlUnit.SetLoggingProtocol)

# ControlUnit[¶](#controlunit "Link to this heading")

*class* ControlUnit[¶](#ApiClient.ControlUnit "Link to this definition")  
DiagSettings[¶](#ApiClient.ControlUnit.DiagSettings "Link to this definition")  
Access to the diagnostics settings

Returns:  diagnostics settings

Return type:  [`DiagSettings`](DiagSettings.md#ApiClient.DiagSettings "ApiClient.DiagSettings (Python class) — Access to the CAN ISO-TP settings")

Clone()[¶](#ApiClient.ControlUnit.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`ControlUnit`](#ApiClient.ControlUnit "ApiClient.ControlUnit (Python class) — Access to the diagnostics settings")

GetApplicationA2lArtifactReference()[¶](#ApiClient.ControlUnit.GetApplicationA2lArtifactReference "Link to this definition")  
Gets the application port \*.a2l artifact reference.

Returns:  A2L file reference

Return type:  [`ArtifactReference`](../ComponentApi/ArtifactReference.md#ApiClient.ArtifactReference "ApiClient.ArtifactReference (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")

GetApplicationA2lFile()[¶](#ApiClient.ControlUnit.GetApplicationA2lFile "Link to this definition")  
Returns the application port \*.a2l file path if a local file is referenced. Convenience method for GetApplicationA2lArtifactReference().GetPath() for local artifact references.

Returns:  A2L file

Return type:  str

GetApplicationA2lTransportLayer()[¶](#ApiClient.ControlUnit.GetApplicationA2lTransportLayer "Link to this definition")  
Returns the A2L Transport-Layer reference for the application port as string or None if the reference is not set.

Returns:  layer-reference string or None

Return type:  str

GetApplicationHexArtifactReference()[¶](#ApiClient.ControlUnit.GetApplicationHexArtifactReference "Link to this definition")  
Gets the application port artifact reference to the hex file.

Returns:  Hex file reference

Return type:  [`ArtifactReference`](../ComponentApi/ArtifactReference.md#ApiClient.ArtifactReference "ApiClient.ArtifactReference (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")

GetApplicationHexFile()[¶](#ApiClient.ControlUnit.GetApplicationHexFile "Link to this definition")  
Returns the application port hex file path if a local file is referenced. Convenience method for GetApplicationHexArtifactReference().GetPath() for local artifact references.

Returns:  hex file

Return type:  str

GetApplicationPort()[¶](#ApiClient.ControlUnit.GetApplicationPort "Link to this definition")  
Returns the application port.

Returns:  Application port

Return type:  str

GetAvailableApplicationA2lTransportLayers()[¶](#ApiClient.ControlUnit.GetAvailableApplicationA2lTransportLayers "Link to this definition")  
Returns a list of available A2l Transport Layers in the selected A2l File. Returns None, if no A2l File was set beforehand using [`SetApplicationA2lFile()`](#ApiClient.ControlUnit.SetApplicationA2lFile "ApiClient.ControlUnit.SetApplicationA2lFile (Python method) — Sets the application port *.a2l file to the specified local file path. Convenience method for SetApplicationA2lArtifactReference() for local artifact references.") or [`SetApplicationA2lArtifactReference()`](#ApiClient.ControlUnit.SetApplicationA2lArtifactReference "ApiClient.ControlUnit.SetApplicationA2lArtifactReference (Python method) — Sets the application port *.a2l file reference.")

Returns:  Available A2l Transport Layers

Return type:  list[str]

GetConnectionSettings()[¶](#ApiClient.ControlUnit.GetConnectionSettings "Link to this definition")  
Get the connection settings that is currently listed in the TCF.

Returns:  remotePartyShortName

Return type:  str

GetDebuggingElfFile()[¶](#ApiClient.ControlUnit.GetDebuggingElfFile "Link to this definition")  
Returns the debugger \*.elf file. Raises an error if a file list with more than one element is set. Use GetDebuggingElfFiles in this case.

Returns:  Debugger \*.elf file

Return type:  str

Raises:  
**ApiError** – If a file list with more than one element is set

GetDebuggingElfFiles()[¶](#ApiClient.ControlUnit.GetDebuggingElfFiles "Link to this definition")  
Returns the debugger \*.elf files.

Returns:  Identifier and path of configured debugger \*.elf files

Return type:  dict[str, str]

GetDebuggingHexArtifactReference()[¶](#ApiClient.ControlUnit.GetDebuggingHexArtifactReference "Link to this definition")  
Gets the artifact reference to the debugger hex file.

Returns:  Debugger hex file reference

Return type:  [`ArtifactReference`](../ComponentApi/ArtifactReference.md#ApiClient.ArtifactReference "ApiClient.ArtifactReference (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")

GetDebuggingHexFile()[¶](#ApiClient.ControlUnit.GetDebuggingHexFile "Link to this definition")  
Returns the debugger hex file path if a local file is referenced. Convenience method for GetDebuggingHexArtifactReference().GetPath() for local artifact references.

Returns:  Debugger hex file

Return type:  str

GetDebuggingPort()[¶](#ApiClient.ControlUnit.GetDebuggingPort "Link to this definition")  
Returns the debugger port.

Returns:  Debugger port

Return type:  str

GetDiagnosticDb()[¶](#ApiClient.ControlUnit.GetDiagnosticDb "Link to this definition")  
Returns the diagnostic database.

Returns:  Diagnostic database

Return type:  str

GetDiagnosticPort()[¶](#ApiClient.ControlUnit.GetDiagnosticPort "Link to this definition")  
Returns the diagnostic port.

Returns:  Diagnostic port

Return type:  str

GetDiagnosticsLogicalLink()[¶](#ApiClient.ControlUnit.GetDiagnosticsLogicalLink "Link to this definition")  
Returns the logical link file.

Returns:  Logical link file

Return type:  str

GetDiagnosticsPortDts()[¶](#ApiClient.ControlUnit.GetDiagnosticsPortDts "Link to this definition")  
Returns the DTS port.

Returns:  DTS port

Return type:  str

GetDiagnosticsPortEdiabas()[¶](#ApiClient.ControlUnit.GetDiagnosticsPortEdiabas "Link to this definition")  
Returns the EDIABAS diagnostics port.

Returns:  EDIABAS port

Return type:  str

GetDiagnosticsSgbdFile()[¶](#ApiClient.ControlUnit.GetDiagnosticsSgbdFile "Link to this definition")  
Returns the SGBD file.

Returns:  SGBD file

Return type:  str

GetEcuVariant()[¶](#ApiClient.ControlUnit.GetEcuVariant "Link to this definition")  
Get the ecu variant that is currently listed in the TCF.

Returns:  short name of the ecu variant

Return type:  str

GetEcuVariants()[¶](#ApiClient.ControlUnit.GetEcuVariants "Link to this definition")  
Returns list of all ecu variants from the given Diagnostics DB. Returns an empty list if the file is invalid or if there are no ecu variants.

Returns:  List of Variants (short name)

Return type:  list[str]

GetEdiabasCertificateFile()[¶](#ApiClient.ControlUnit.GetEdiabasCertificateFile "Link to this definition")  
Returns the certificate file for Ediabas.

Returns:  Certificate file

Return type:  str

GetEdiabasNetworkProtocol()[¶](#ApiClient.ControlUnit.GetEdiabasNetworkProtocol "Link to this definition")  
Returns the “NetworkProtocol” configuration (SSL/TCP) for EDIABAS.

Returns:  “NetworkProtocol” configuration string

Return type:  str

GetLoggingDatabase()[¶](#ApiClient.ControlUnit.GetLoggingDatabase "Link to this definition")  
Returns the logging database.

The logging database is only used for the logging protocol ‘DLT (non-verbose)’.

Returns:  logging database

Return type:  str

GetLoggingDltFilterFile()[¶](#ApiClient.ControlUnit.GetLoggingDltFilterFile "Link to this definition")  
Returns the DLT filter file.

The DLT filter file is only used for the logging protocol ‘DLT (verbose)’.

Returns:  DLT filter file

Return type:  str

GetLoggingEcu()[¶](#ApiClient.ControlUnit.GetLoggingEcu "Link to this definition")  
Returns the logging ECU.

The logging ECU is only used for the logging protocol ‘DLT (non-verbose)’.

Returns:  logging ECU

Return type:  str

GetLoggingEthernetIp()[¶](#ApiClient.ControlUnit.GetLoggingEthernetIp "Link to this definition")  
Returns the Ethernet IP of the logging ECU.

Returns:  Ethernet-IP of the logging ECU

Return type:  str

GetLoggingEthernetPort()[¶](#ApiClient.ControlUnit.GetLoggingEthernetPort "Link to this definition")  
Returns the Ethernet port(s) of the logging ECU.

Returns:  Comma seperated Ethernet port(s) of the logging ECU

Return type:  str

GetLoggingEthernetProtocol()[¶](#ApiClient.ControlUnit.GetLoggingEthernetProtocol "Link to this definition")  
Returns the Ethernet protocol of the logging ECU.

Returns:  Ethernet protocol of the logging ECU

Return type:  str

GetLoggingPort()[¶](#ApiClient.ControlUnit.GetLoggingPort "Link to this definition")  
Returns the logging port.

Returns:  logging port

Return type:  str

GetLoggingProtocol()[¶](#ApiClient.ControlUnit.GetLoggingProtocol "Link to this definition")  
Returns the logging protocol.

Returns:  logging protocol: ‘DLT (non-verbose)’ or ‘DLT (verbose)’

Return type:  str

GetName()[¶](#ApiClient.ControlUnit.GetName "Link to this definition")  
Returns the name of the control unit.

Returns:  Name of the control unit

Return type:  str

GetRemotePartys()[¶](#ApiClient.ControlUnit.GetRemotePartys "Link to this definition")  
Returns list of remote partys from the given Diagnostics DB. Returns an empty list if the file is invalid or if there are no remote partys.

Returns:  List of Remote Partys (short name)

Return type:  list[str]

IsDebuggingUseHexFileFromApplication()[¶](#ApiClient.ControlUnit.IsDebuggingUseHexFileFromApplication "Link to this definition")  
Returns the option if the hex file is used from the application.

Returns:  Option to use hex file from application

Return type:  boolean

RemoveApplicationA2lArtifactReference()[¶](#ApiClient.ControlUnit.RemoveApplicationA2lArtifactReference "Link to this definition")  
Removes the application port \*.a2l file reference.

RemoveApplicationHexArtifactReference()[¶](#ApiClient.ControlUnit.RemoveApplicationHexArtifactReference "Link to this definition")  
Removes the application port hex file reference.

RemoveDebuggingHexArtifactReference()[¶](#ApiClient.ControlUnit.RemoveDebuggingHexArtifactReference "Link to this definition")  
Removes the debugger hex file reference.

Rename(*[newControlUnitKey](#ApiClient.ControlUnit.Rename.newControlUnitKey "ApiClient.ControlUnit.Rename.newControlUnitKey (Python parameter) — New name of the control unit")*)[¶](#ApiClient.ControlUnit.Rename "Link to this definition")  
Renames the control unit.

Parameters:  newControlUnitKey : str[¶](#ApiClient.ControlUnit.Rename.newControlUnitKey "Permalink to this definition")  
New name of the control unit

SetApplicationA2lArtifactReference(*[a2lReference](#ApiClient.ControlUnit.SetApplicationA2lArtifactReference.a2lReference "ApiClient.ControlUnit.SetApplicationA2lArtifactReference.a2lReference (Python parameter) — A2L file reference to be set")*)[¶](#ApiClient.ControlUnit.SetApplicationA2lArtifactReference "Link to this definition")  
Sets the application port \*.a2l file reference.

Parameters:  a2lReference[¶](#ApiClient.ControlUnit.SetApplicationA2lArtifactReference.a2lReference "Permalink to this definition")  
A2L file reference to be set

SetApplicationA2lFile(*[a2lFile](#ApiClient.ControlUnit.SetApplicationA2lFile.a2lFile "ApiClient.ControlUnit.SetApplicationA2lFile.a2lFile (Python parameter) — A2L file to be set")*)[¶](#ApiClient.ControlUnit.SetApplicationA2lFile "Link to this definition")  
Sets the application port \*.a2l file to the specified local file path. Convenience method for SetApplicationA2lArtifactReference() for local artifact references.

Parameters:  a2lFile : str[¶](#ApiClient.ControlUnit.SetApplicationA2lFile.a2lFile "Permalink to this definition")  
A2L file to be set

SetApplicationA2lTransportLayer(*[value](#ApiClient.ControlUnit.SetApplicationA2lTransportLayer.value "ApiClient.ControlUnit.SetApplicationA2lTransportLayer.value (Python parameter) — layer-reference string or None")*)[¶](#ApiClient.ControlUnit.SetApplicationA2lTransportLayer "Link to this definition")  
Sets the A2L Transport-Layer reference for the application port if given a string as argument or unsets it if given None as argument.

Parameters:  value : str[¶](#ApiClient.ControlUnit.SetApplicationA2lTransportLayer.value "Permalink to this definition")  
layer-reference string or None

SetApplicationHexArtifactReference(*[hexReference](#ApiClient.ControlUnit.SetApplicationHexArtifactReference.hexReference "ApiClient.ControlUnit.SetApplicationHexArtifactReference.hexReference (Python parameter) — Hex file reference to be set")*)[¶](#ApiClient.ControlUnit.SetApplicationHexArtifactReference "Link to this definition")  
Sets the application port hex file reference.

Parameters:  hexReference[¶](#ApiClient.ControlUnit.SetApplicationHexArtifactReference.hexReference "Permalink to this definition")  
Hex file reference to be set

SetApplicationHexFile(*[hexFile](#ApiClient.ControlUnit.SetApplicationHexFile.hexFile "ApiClient.ControlUnit.SetApplicationHexFile.hexFile (Python parameter) — Hex file to be set")*)[¶](#ApiClient.ControlUnit.SetApplicationHexFile "Link to this definition")  
Sets the application port hex file to the specified local file path. Convenience method for SetApplicationHexArtifactReference() for local artifact references.

Parameters:  hexFile : str[¶](#ApiClient.ControlUnit.SetApplicationHexFile.hexFile "Permalink to this definition")  
Hex file to be set

SetApplicationPort(*[applicationPort](#ApiClient.ControlUnit.SetApplicationPort.applicationPort "ApiClient.ControlUnit.SetApplicationPort.applicationPort (Python parameter) — Application port to be set")*)[¶](#ApiClient.ControlUnit.SetApplicationPort "Link to this definition")  
Sets the application port.

Parameters:  applicationPort : str[¶](#ApiClient.ControlUnit.SetApplicationPort.applicationPort "Permalink to this definition")  
Application port to be set

SetConnectionSettings(*[remotePartyShortName](#ApiClient.ControlUnit.SetConnectionSettings.remotePartyShortName "ApiClient.ControlUnit.SetConnectionSettings.remotePartyShortName (Python parameter) — short name of the remote party")*)[¶](#ApiClient.ControlUnit.SetConnectionSettings "Link to this definition")  
Set the connection settings by using the short name of a specific remote party. Use the GetRemotePartys() method to get a list of all remote partys from the diagnostics DB.

Parameters:  remotePartyShortName : str[¶](#ApiClient.ControlUnit.SetConnectionSettings.remotePartyShortName "Permalink to this definition")  
short name of the remote party

Returns:  True if success, else False

Return type:  bool

SetDebuggingElfFile(*[debuggerElfFile](#ApiClient.ControlUnit.SetDebuggingElfFile.debuggerElfFile "ApiClient.ControlUnit.SetDebuggingElfFile.debuggerElfFile (Python parameter) — Debugger *.elf file to be set")*)[¶](#ApiClient.ControlUnit.SetDebuggingElfFile "Link to this definition")  
Sets the debugger \*.elf file. Overwrites an existing file or file list. The \*.elf file will be assigned to identifier “ELF-1”

Parameters:  debuggerElfFile : str[¶](#ApiClient.ControlUnit.SetDebuggingElfFile.debuggerElfFile "Permalink to this definition")  
Debugger \*.elf file to be set

SetDebuggingElfFiles(*[debuggerElfFiles](#ApiClient.ControlUnit.SetDebuggingElfFiles.debuggerElfFiles "ApiClient.ControlUnit.SetDebuggingElfFiles.debuggerElfFiles (Python parameter) — Identifiers and pathes to debugger *.elf files")*)[¶](#ApiClient.ControlUnit.SetDebuggingElfFiles "Link to this definition")  
Sets the debugger \*.elf files. Overwrites an existing file or file list.

Parameters:  debuggerElfFiles : dict[str, str][¶](#ApiClient.ControlUnit.SetDebuggingElfFiles.debuggerElfFiles "Permalink to this definition")  
Identifiers and pathes to debugger \*.elf files

SetDebuggingHexArtifactReference(*[hexReference](#ApiClient.ControlUnit.SetDebuggingHexArtifactReference.hexReference "ApiClient.ControlUnit.SetDebuggingHexArtifactReference.hexReference (Python parameter) — Hex file reference to be set")*)[¶](#ApiClient.ControlUnit.SetDebuggingHexArtifactReference "Link to this definition")  
Sets the debugger hex file reference.

Parameters:  hexReference[¶](#ApiClient.ControlUnit.SetDebuggingHexArtifactReference.hexReference "Permalink to this definition")  
Hex file reference to be set

SetDebuggingHexFile(*[debuggerHexFile](#ApiClient.ControlUnit.SetDebuggingHexFile.debuggerHexFile "ApiClient.ControlUnit.SetDebuggingHexFile.debuggerHexFile (Python parameter) — Debugger hex file to be set")*)[¶](#ApiClient.ControlUnit.SetDebuggingHexFile "Link to this definition")  
Sets the debugger hex file to the specified local file path. Convenience method for SetDebuggingHexArtifactReference() for local artifact references.

Parameters:  debuggerHexFile : str[¶](#ApiClient.ControlUnit.SetDebuggingHexFile.debuggerHexFile "Permalink to this definition")  
Debugger hex file to be set

SetDebuggingPort(*[debuggerPort](#ApiClient.ControlUnit.SetDebuggingPort.debuggerPort "ApiClient.ControlUnit.SetDebuggingPort.debuggerPort (Python parameter) — Debugger port to be set")*)[¶](#ApiClient.ControlUnit.SetDebuggingPort "Link to this definition")  
Sets the debugger port.

Parameters:  debuggerPort : str[¶](#ApiClient.ControlUnit.SetDebuggingPort.debuggerPort "Permalink to this definition")  
Debugger port to be set

SetDebuggingUseHexFileFromApplication(*[value](#ApiClient.ControlUnit.SetDebuggingUseHexFileFromApplication.value "ApiClient.ControlUnit.SetDebuggingUseHexFileFromApplication.value (Python parameter) — Option to use hex file from application")*)[¶](#ApiClient.ControlUnit.SetDebuggingUseHexFileFromApplication "Link to this definition")  
Sets the option to use the hex file from the application.

Parameters:  value : boolean[¶](#ApiClient.ControlUnit.SetDebuggingUseHexFileFromApplication.value "Permalink to this definition")  
Option to use hex file from application

SetDiagnosticDb(*[diagnosticDb](#ApiClient.ControlUnit.SetDiagnosticDb.diagnosticDb "ApiClient.ControlUnit.SetDiagnosticDb.diagnosticDb (Python parameter) — Diagnostic database to be set")*)[¶](#ApiClient.ControlUnit.SetDiagnosticDb "Link to this definition")  
Sets the diagnostic database.

Parameters:  diagnosticDb : str[¶](#ApiClient.ControlUnit.SetDiagnosticDb.diagnosticDb "Permalink to this definition")  
Diagnostic database to be set

SetDiagnosticPort(*[diagnosticPort](#ApiClient.ControlUnit.SetDiagnosticPort.diagnosticPort "ApiClient.ControlUnit.SetDiagnosticPort.diagnosticPort (Python parameter) — Diagnostic port to be set")*)[¶](#ApiClient.ControlUnit.SetDiagnosticPort "Link to this definition")  
Sets the diagnostic port.

Parameters:  diagnosticPort : str[¶](#ApiClient.ControlUnit.SetDiagnosticPort.diagnosticPort "Permalink to this definition")  
Diagnostic port to be set

SetDiagnosticsLogicalLink(*[logicalLinkFile](#ApiClient.ControlUnit.SetDiagnosticsLogicalLink.logicalLinkFile "ApiClient.ControlUnit.SetDiagnosticsLogicalLink.logicalLinkFile (Python parameter) — Logical link file to be set")*)[¶](#ApiClient.ControlUnit.SetDiagnosticsLogicalLink "Link to this definition")  
Sets the logical link file.

Parameters:  logicalLinkFile : str[¶](#ApiClient.ControlUnit.SetDiagnosticsLogicalLink.logicalLinkFile "Permalink to this definition")  
Logical link file to be set

SetDiagnosticsPortDts(*[diagnosticsPortDts](#ApiClient.ControlUnit.SetDiagnosticsPortDts.diagnosticsPortDts "ApiClient.ControlUnit.SetDiagnosticsPortDts.diagnosticsPortDts (Python parameter) — DTS port to be set")*)[¶](#ApiClient.ControlUnit.SetDiagnosticsPortDts "Link to this definition")  
Sets the DTS port.

Parameters:  diagnosticsPortDts : str[¶](#ApiClient.ControlUnit.SetDiagnosticsPortDts.diagnosticsPortDts "Permalink to this definition")  
DTS port to be set

SetDiagnosticsPortEdiabas(*[diagnosticsPort](#ApiClient.ControlUnit.SetDiagnosticsPortEdiabas.diagnosticsPort "ApiClient.ControlUnit.SetDiagnosticsPortEdiabas.diagnosticsPort (Python parameter) — Diagnostics port to be set")*)[¶](#ApiClient.ControlUnit.SetDiagnosticsPortEdiabas "Link to this definition")  
Sets the EDIABAS diagnostics port.

Parameters:  diagnosticsPort : str[¶](#ApiClient.ControlUnit.SetDiagnosticsPortEdiabas.diagnosticsPort "Permalink to this definition")  
Diagnostics port to be set

SetDiagnosticsSgbdFile(*[sgbdFile](#ApiClient.ControlUnit.SetDiagnosticsSgbdFile.sgbdFile "ApiClient.ControlUnit.SetDiagnosticsSgbdFile.sgbdFile (Python parameter) — SGBD file to be set")*)[¶](#ApiClient.ControlUnit.SetDiagnosticsSgbdFile "Link to this definition")  
Sets the SGBD file.

Parameters:  sgbdFile : str[¶](#ApiClient.ControlUnit.SetDiagnosticsSgbdFile.sgbdFile "Permalink to this definition")  
SGBD file to be set

SetEcuVariant(*[ecuVariant](#ApiClient.ControlUnit.SetEcuVariant.ecuVariant "ApiClient.ControlUnit.SetEcuVariant.ecuVariant (Python parameter) — short name of the ecu variant")*)[¶](#ApiClient.ControlUnit.SetEcuVariant "Link to this definition")  
Set the ecu variant by using the short name of a specific ecu variant. Use the GetEcuVariants() method to get a list of all ecu variants from the diagnostics DB.

Parameters:  ecuVariant : str[¶](#ApiClient.ControlUnit.SetEcuVariant.ecuVariant "Permalink to this definition")  
short name of the ecu variant

Returns:  True if success, else False

Return type:  bool

SetEdiabasCertificateFile(*[certificate](#ApiClient.ControlUnit.SetEdiabasCertificateFile.certificate "ApiClient.ControlUnit.SetEdiabasCertificateFile.certificate (Python parameter) — Certificate file to be set.")*)[¶](#ApiClient.ControlUnit.SetEdiabasCertificateFile "Link to this definition")  
Sets the certificate file for Ediabs.

Parameters:  certificate : str[¶](#ApiClient.ControlUnit.SetEdiabasCertificateFile.certificate "Permalink to this definition")  
Certificate file to be set. This must be the file name without the suffix.

SetEdiabasNetworkProtocol(*[ediabasNetworkProtocol](#ApiClient.ControlUnit.SetEdiabasNetworkProtocol.ediabasNetworkProtocol "ApiClient.ControlUnit.SetEdiabasNetworkProtocol.ediabasNetworkProtocol (Python parameter) — The configured value for "NetworkProtocol" selection")*)[¶](#ApiClient.ControlUnit.SetEdiabasNetworkProtocol "Link to this definition")  
Sets the “NetworkProtocol” configuration (SSL/TCP) for EDIABAS.

Parameters:  ediabasNetworkProtocol : str[¶](#ApiClient.ControlUnit.SetEdiabasNetworkProtocol.ediabasNetworkProtocol "Permalink to this definition")  
The configured value for “NetworkProtocol” selection

SetLoggingDatabase(*[loggingDatabase](#ApiClient.ControlUnit.SetLoggingDatabase.loggingDatabase "ApiClient.ControlUnit.SetLoggingDatabase.loggingDatabase (Python parameter) — logging database")*)[¶](#ApiClient.ControlUnit.SetLoggingDatabase "Link to this definition")  
Sets the logging database.

The logging database is only used for the logging protocol ‘DLT (non-verbose)’.

Parameters:  loggingDatabase : str[¶](#ApiClient.ControlUnit.SetLoggingDatabase.loggingDatabase "Permalink to this definition")  
logging database

SetLoggingDltFilterFile(*[loggingDltFilterFile](#ApiClient.ControlUnit.SetLoggingDltFilterFile.loggingDltFilterFile "ApiClient.ControlUnit.SetLoggingDltFilterFile.loggingDltFilterFile (Python parameter) — DLT filter file")*)[¶](#ApiClient.ControlUnit.SetLoggingDltFilterFile "Link to this definition")  
Sets the DLT filter file.

The DLT filter file is only used for the logging protocol ‘DLT (verbose)’.

Parameters:  loggingDltFilterFile : str[¶](#ApiClient.ControlUnit.SetLoggingDltFilterFile.loggingDltFilterFile "Permalink to this definition")  
DLT filter file

SetLoggingEcu(*[loggingEcu](#ApiClient.ControlUnit.SetLoggingEcu.loggingEcu "ApiClient.ControlUnit.SetLoggingEcu.loggingEcu (Python parameter) — logging ECU")*)[¶](#ApiClient.ControlUnit.SetLoggingEcu "Link to this definition")  
Sets the logging ECU.

The logging ECU is only used for the logging protocol ‘DLT (non-verbose)’.

Parameters:  loggingEcu : str[¶](#ApiClient.ControlUnit.SetLoggingEcu.loggingEcu "Permalink to this definition")  
logging ECU

SetLoggingEthernetIp(*[loggingEthernetIp](#ApiClient.ControlUnit.SetLoggingEthernetIp.loggingEthernetIp "ApiClient.ControlUnit.SetLoggingEthernetIp.loggingEthernetIp (Python parameter) — Ethernet-IP of the logging ECU")*)[¶](#ApiClient.ControlUnit.SetLoggingEthernetIp "Link to this definition")  
Sets the Ethernet IP of the logging ECU.

Parameters:  loggingEthernetIp : str[¶](#ApiClient.ControlUnit.SetLoggingEthernetIp.loggingEthernetIp "Permalink to this definition")  
Ethernet-IP of the logging ECU

SetLoggingEthernetPort(*[loggingEthernetPort](#ApiClient.ControlUnit.SetLoggingEthernetPort.loggingEthernetPort "ApiClient.ControlUnit.SetLoggingEthernetPort.loggingEthernetPort (Python parameter) — Ethernet port(s) of the logging ECU.")*)[¶](#ApiClient.ControlUnit.SetLoggingEthernetPort "Link to this definition")  
Sets the Ethernet port(s) of the logging ECU.

Parameters:  loggingEthernetPort : str[¶](#ApiClient.ControlUnit.SetLoggingEthernetPort.loggingEthernetPort "Permalink to this definition")  
Ethernet port(s) of the logging ECU. Multiple ports have to to be comma seperated.

SetLoggingEthernetProtocol(*[loggingEthernetProtocol](#ApiClient.ControlUnit.SetLoggingEthernetProtocol.loggingEthernetProtocol "ApiClient.ControlUnit.SetLoggingEthernetProtocol.loggingEthernetProtocol (Python parameter) — Ethernet protocol of the logging ECU")*)[¶](#ApiClient.ControlUnit.SetLoggingEthernetProtocol "Link to this definition")  
Sets the Ethernet protocol of the logging ECU.

Parameters:  loggingEthernetProtocol : str[¶](#ApiClient.ControlUnit.SetLoggingEthernetProtocol.loggingEthernetProtocol "Permalink to this definition")  
Ethernet protocol of the logging ECU

SetLoggingPort(*[loggingPort](#ApiClient.ControlUnit.SetLoggingPort.loggingPort "ApiClient.ControlUnit.SetLoggingPort.loggingPort (Python parameter) — logging port")*)[¶](#ApiClient.ControlUnit.SetLoggingPort "Link to this definition")  
Sets the logging port.

Parameters:  loggingPort : str[¶](#ApiClient.ControlUnit.SetLoggingPort.loggingPort "Permalink to this definition")  
logging port

SetLoggingProtocol(*[loggingProtocol](#ApiClient.ControlUnit.SetLoggingProtocol.loggingProtocol "ApiClient.ControlUnit.SetLoggingProtocol.loggingProtocol (Python parameter) — logging protocol: 'DLT (non-verbose)' or 'DLT (verbose)'")*)[¶](#ApiClient.ControlUnit.SetLoggingProtocol "Link to this definition")  
Sets the logging protocol.

Note: A change of the logging protocol will automatically set the logging database, logging ecu and dlt filter file to its default values.

Parameters:  loggingProtocol : str[¶](#ApiClient.ControlUnit.SetLoggingProtocol.loggingProtocol "Permalink to this definition")  
logging protocol: ‘DLT (non-verbose)’ or ‘DLT (verbose)’

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
