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

Model [ Model ](#)

Model

- [C Model ](#ApiClient.Model)
  - [M Clone ](#ApiClient.Model.Clone)
  - [M GetAdditionalFiles ](#ApiClient.Model.GetAdditionalFiles)
  - [M GetFile ](#ApiClient.Model.GetFile)
  - [M GetImportSource ](#ApiClient.Model.GetImportSource)
  - [M GetName ](#ApiClient.Model.GetName)
  - [M GetPort ](#ApiClient.Model.GetPort)
  - [M InsertAdditionalFile ](#ApiClient.Model.InsertAdditionalFile)
  - [M RemoveAdditionalFile ](#ApiClient.Model.RemoveAdditionalFile)
  - [M Rename ](#ApiClient.Model.Rename)
  - [M SetFile ](#ApiClient.Model.SetFile)
  - [M SetImportSource ](#ApiClient.Model.SetImportSource)
  - [M SetPort ](#ApiClient.Model.SetPort)

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

Model

- [C Model ](#ApiClient.Model)
  - [M Clone ](#ApiClient.Model.Clone)
  - [M GetAdditionalFiles ](#ApiClient.Model.GetAdditionalFiles)
  - [M GetFile ](#ApiClient.Model.GetFile)
  - [M GetImportSource ](#ApiClient.Model.GetImportSource)
  - [M GetName ](#ApiClient.Model.GetName)
  - [M GetPort ](#ApiClient.Model.GetPort)
  - [M InsertAdditionalFile ](#ApiClient.Model.InsertAdditionalFile)
  - [M RemoveAdditionalFile ](#ApiClient.Model.RemoveAdditionalFile)
  - [M Rename ](#ApiClient.Model.Rename)
  - [M SetFile ](#ApiClient.Model.SetFile)
  - [M SetImportSource ](#ApiClient.Model.SetImportSource)
  - [M SetPort ](#ApiClient.Model.SetPort)

# Model[¶](#model "Link to this heading")

*class* Model[¶](#ApiClient.Model "Link to this definition")  
Clone()[¶](#ApiClient.Model.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`Model`](#ApiClient.Model "ApiClient.Model (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")

GetAdditionalFiles()[¶](#ApiClient.Model.GetAdditionalFiles "Link to this definition")  
Gets additional files configured for this model.

Returns:  The list of additional files

Return type:  list[str]

GetFile()[¶](#ApiClient.Model.GetFile "Link to this definition")  
Returns the model file.

Returns:  Model file

Return type:  str

GetImportSource()[¶](#ApiClient.Model.GetImportSource "Link to this definition")  
Returns the model import source.

Returns:  Model import source: 0 Automatically, 1 From Cache, 2 Disabled

Return type:  int

GetName()[¶](#ApiClient.Model.GetName "Link to this definition")  
Returns the name of the model.

Returns:  Name of the model

Return type:  str

GetPort()[¶](#ApiClient.Model.GetPort "Link to this definition")  
Returns the model port.

Returns:  Model port

Return type:  str

InsertAdditionalFile(*[filename](#ApiClient.Model.InsertAdditionalFile.filename "ApiClient.Model.InsertAdditionalFile.filename (Python parameter) — The name of the file to be added")*, *[index](#ApiClient.Model.InsertAdditionalFile.index "ApiClient.Model.InsertAdditionalFile.index (Python parameter) — The index the new entry should be placed at.")=`None`*)[¶](#ApiClient.Model.InsertAdditionalFile "Link to this definition")  
Adds an entry on the given index into the additional files list.

Some model tools allow e.g. \*.par or \*.smf files to be specified here.

Parameters:  filename : str[¶](#ApiClient.Model.InsertAdditionalFile.filename "Permalink to this definition")  
The name of the file to be added

index : int[¶](#ApiClient.Model.InsertAdditionalFile.index "Permalink to this definition")  
The index the new entry should be placed at. If left out, the filename will be appended at the end of the list.

RemoveAdditionalFile(*[index](#ApiClient.Model.RemoveAdditionalFile.index "ApiClient.Model.RemoveAdditionalFile.index (Python parameter) — The index to be removed.")*)[¶](#ApiClient.Model.RemoveAdditionalFile "Link to this definition")  
Removes the entry on the given index from additional files list.

Parameters:  index : int[¶](#ApiClient.Model.RemoveAdditionalFile.index "Permalink to this definition")  
The index to be removed.

Rename(*[newModelKey](#ApiClient.Model.Rename.newModelKey "ApiClient.Model.Rename.newModelKey (Python parameter) — New name of the model")*)[¶](#ApiClient.Model.Rename "Link to this definition")  
Renames the model.

Parameters:  newModelKey : str[¶](#ApiClient.Model.Rename.newModelKey "Permalink to this definition")  
New name of the model

SetFile(*[modelFile](#ApiClient.Model.SetFile.modelFile "ApiClient.Model.SetFile.modelFile (Python parameter) — Model file to be set")*)[¶](#ApiClient.Model.SetFile "Link to this definition")  
Sets the model file.

Parameters:  modelFile : str[¶](#ApiClient.Model.SetFile.modelFile "Permalink to this definition")  
Model file to be set

SetImportSource(*[importSource](#ApiClient.Model.SetImportSource.importSource "ApiClient.Model.SetImportSource.importSource (Python parameter) — Model import source: 0 Automatically, 1 From Cache, 2 Disabled")*)[¶](#ApiClient.Model.SetImportSource "Link to this definition")  
Sets the model import source.

Parameters:  importSource : int[¶](#ApiClient.Model.SetImportSource.importSource "Permalink to this definition")  
Model import source: 0 Automatically, 1 From Cache, 2 Disabled

SetPort(*[modelPort](#ApiClient.Model.SetPort.modelPort "ApiClient.Model.SetPort.modelPort (Python parameter) — Model port to be set")*)[¶](#ApiClient.Model.SetPort "Link to this definition")  
Sets the model port.

Parameters:  modelPort : str[¶](#ApiClient.Model.SetPort.modelPort "Permalink to this definition")  
Model port to be set

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
