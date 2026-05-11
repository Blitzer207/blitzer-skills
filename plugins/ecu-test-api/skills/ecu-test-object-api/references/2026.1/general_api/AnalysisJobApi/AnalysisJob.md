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

API for Analysis Jobs

AnalysisJob [ AnalysisJob ](#)

AnalysisJob

- [C AnalysisJob ](#ApiClient.AnalysisJob)
  - [M AddGenericSignal ](#ApiClient.AnalysisJob.AddGenericSignal)
  - [M AddRecording ](#ApiClient.AnalysisJob.AddRecording)
  - [M Clone ](#ApiClient.AnalysisJob.Clone)
  - [M GetAnalysisReference ](#ApiClient.AnalysisJob.GetAnalysisReference)
  - [M GetFilename ](#ApiClient.AnalysisJob.GetFilename)
  - [M GetGenericSignals ](#ApiClient.AnalysisJob.GetGenericSignals)
  - [M GetGlobalConstants ](#ApiClient.AnalysisJob.GetGlobalConstants)
  - [M GetMapping ](#ApiClient.AnalysisJob.GetMapping)
  - [M GetPackageReference ](#ApiClient.AnalysisJob.GetPackageReference)
  - [M GetParameter ](#ApiClient.AnalysisJob.GetParameter)
  - [M GetParameters ](#ApiClient.AnalysisJob.GetParameters)
  - [M GetRecordings ](#ApiClient.AnalysisJob.GetRecordings)
  - [M GetTestConfigurationPath ](#ApiClient.AnalysisJob.GetTestConfigurationPath)
  - [M RemoveGenericSignal ](#ApiClient.AnalysisJob.RemoveGenericSignal)
  - [M RemoveParameter ](#ApiClient.AnalysisJob.RemoveParameter)
  - [M RemoveRecording ](#ApiClient.AnalysisJob.RemoveRecording)
  - [M Save ](#ApiClient.AnalysisJob.Save)
  - [M SetAnalysisReference ](#ApiClient.AnalysisJob.SetAnalysisReference)
  - [M SetGlobalConstants ](#ApiClient.AnalysisJob.SetGlobalConstants)
  - [M SetPackageReference ](#ApiClient.AnalysisJob.SetPackageReference)
  - [M SetParameter ](#ApiClient.AnalysisJob.SetParameter)
  - [M SetParameters ](#ApiClient.AnalysisJob.SetParameters)
  - [M SetTestConfigurationPath ](#ApiClient.AnalysisJob.SetTestConfigurationPath)

[ AnalysisJobGenericSignal ](AnalysisJobGenericSignal.md)

[ AnalysisJobRecording ](AnalysisJobRecording.md)

[ Mapping ](Mapping.md)

[ API for Artifacts ](../ArtifactApi.md)

[ API for Project Components ](../ComponentApi.md)

[ API for Configurations ](../ConfigurationApi.md)

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

AnalysisJob

- [C AnalysisJob ](#ApiClient.AnalysisJob)
  - [M AddGenericSignal ](#ApiClient.AnalysisJob.AddGenericSignal)
  - [M AddRecording ](#ApiClient.AnalysisJob.AddRecording)
  - [M Clone ](#ApiClient.AnalysisJob.Clone)
  - [M GetAnalysisReference ](#ApiClient.AnalysisJob.GetAnalysisReference)
  - [M GetFilename ](#ApiClient.AnalysisJob.GetFilename)
  - [M GetGenericSignals ](#ApiClient.AnalysisJob.GetGenericSignals)
  - [M GetGlobalConstants ](#ApiClient.AnalysisJob.GetGlobalConstants)
  - [M GetMapping ](#ApiClient.AnalysisJob.GetMapping)
  - [M GetPackageReference ](#ApiClient.AnalysisJob.GetPackageReference)
  - [M GetParameter ](#ApiClient.AnalysisJob.GetParameter)
  - [M GetParameters ](#ApiClient.AnalysisJob.GetParameters)
  - [M GetRecordings ](#ApiClient.AnalysisJob.GetRecordings)
  - [M GetTestConfigurationPath ](#ApiClient.AnalysisJob.GetTestConfigurationPath)
  - [M RemoveGenericSignal ](#ApiClient.AnalysisJob.RemoveGenericSignal)
  - [M RemoveParameter ](#ApiClient.AnalysisJob.RemoveParameter)
  - [M RemoveRecording ](#ApiClient.AnalysisJob.RemoveRecording)
  - [M Save ](#ApiClient.AnalysisJob.Save)
  - [M SetAnalysisReference ](#ApiClient.AnalysisJob.SetAnalysisReference)
  - [M SetGlobalConstants ](#ApiClient.AnalysisJob.SetGlobalConstants)
  - [M SetPackageReference ](#ApiClient.AnalysisJob.SetPackageReference)
  - [M SetParameter ](#ApiClient.AnalysisJob.SetParameter)
  - [M SetParameters ](#ApiClient.AnalysisJob.SetParameters)
  - [M SetTestConfigurationPath ](#ApiClient.AnalysisJob.SetTestConfigurationPath)

# AnalysisJob[¶](#analysisjob "Link to this heading")

*class* AnalysisJob[¶](#ApiClient.AnalysisJob "Link to this definition")  
Returned by

- [`AnalysisJobApi.CreateAnalysisJob`](../AnalysisJobApi.md#ApiClient.AnalysisJobApi.CreateAnalysisJob "ApiClient.AnalysisJobApi.CreateAnalysisJob (Python method) — Creates a new analysis job")

- [`AnalysisJobApi.OpenAnalysisJob`](../AnalysisJobApi.md#ApiClient.AnalysisJobApi.OpenAnalysisJob "ApiClient.AnalysisJobApi.OpenAnalysisJob (Python method) — Opens an existing analysis job")

AddGenericSignal(*[genericSignal](#ApiClient.AnalysisJob.AddGenericSignal.genericSignal "ApiClient.AnalysisJob.AddGenericSignal.genericSignal (Python parameter) — Generic signal to add")*)[¶](#ApiClient.AnalysisJob.AddGenericSignal "Link to this definition")  
Adds a new generic signal.

Note:  
The name of the generic signal should be unique.

Parameters:  genericSignal[¶](#ApiClient.AnalysisJob.AddGenericSignal.genericSignal "Permalink to this definition")  
Generic signal to add

AddRecording(*[recording](#ApiClient.AnalysisJob.AddRecording.recording "ApiClient.AnalysisJob.AddRecording.recording (Python parameter) — Recording to add")*)[¶](#ApiClient.AnalysisJob.AddRecording "Link to this definition")  
Adds a new recording.

Note:  
The name of the recordings should be unique.

Parameters:  recording[¶](#ApiClient.AnalysisJob.AddRecording.recording "Permalink to this definition")  
Recording to add

Clone()[¶](#ApiClient.AnalysisJob.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`AnalysisJob`](#ApiClient.AnalysisJob "ApiClient.AnalysisJob (Python class) — AnalysisJobApi.CreateAnalysisJob")

GetAnalysisReference()[¶](#ApiClient.AnalysisJob.GetAnalysisReference "Link to this definition")  
Returns the name of the trace analysis which is used.

Returns:  name of trace analysis within package (`GetPackageReference()`)

Return type:  str

GetFilename()[¶](#ApiClient.AnalysisJob.GetFilename "Link to this definition")  
Returns the file name of the analysis job file as absolute path, if this file was loaded or saved.

Returns:  The file name of the origin file or None

Return type:  str

GetGenericSignals()[¶](#ApiClient.AnalysisJob.GetGenericSignals "Link to this definition")  
Returns all generic signals with their assignments.

Returns:  Generic signals

Return type:  list[[`AnalysisJobGenericSignal`](AnalysisJobGenericSignal.md#ApiClient.AnalysisJobGenericSignal "ApiClient.AnalysisJobGenericSignal (Python class) — AnalysisJobApi.CreateGenericSignal")]

GetGlobalConstants()[¶](#ApiClient.AnalysisJob.GetGlobalConstants "Link to this definition")  
Returns the container of defined global constants.

Returns:  Container for global constants

Return type:  [`GlobalConstantsDefinition`](../ParameterApi/GlobalConstantsDefinition.md#ApiClient.GlobalConstantsDefinition "ApiClient.GlobalConstantsDefinition (Python class) — ParameterApi.CreateGlobalConstantsDefinition")

GetMapping()[¶](#ApiClient.AnalysisJob.GetMapping "Link to this definition")  
Returns the mapping of the analysis job.

Returns:  Mapping of the analysis job

Return type:  [`Mapping`](Mapping.md#ApiClient.Mapping "ApiClient.Mapping (Python class) — Adds a mapping item to the mapping.")

GetPackageReference()[¶](#ApiClient.AnalysisJob.GetPackageReference "Link to this definition")  
Returns the absolute Package file path in which the corresponding trace analysis exists.

Returns:  Package file path or None, if not set.

Return type:  str

GetParameter(*[name](#ApiClient.AnalysisJob.GetParameter.name "ApiClient.AnalysisJob.GetParameter.name (Python parameter) — Name of the parameter")*)[¶](#ApiClient.AnalysisJob.GetParameter "Link to this definition")  
Retrieves the value assigned to a parameter.

Parameters:  name : string[¶](#ApiClient.AnalysisJob.GetParameter.name "Permalink to this definition")  
Name of the parameter

Returns:  Parameter value as Python literal expression

Return type:  str

Raises:  
ApiError: When parameter does not exist

GetParameters()[¶](#ApiClient.AnalysisJob.GetParameters "Link to this definition")  
Retrieves the values assigned to template parameters.

Returns:  A dictionary of parameter name -> parameter value (Python literal expression) mappings

Return type:  dict[str, str]

GetRecordings()[¶](#ApiClient.AnalysisJob.GetRecordings "Link to this definition")  
Returns all recordings.

Returns:  Recordings

Return type:  list[[`AnalysisJobRecording`](AnalysisJobRecording.md#ApiClient.AnalysisJobRecording "ApiClient.AnalysisJobRecording (Python class) — AnalysisJobApi.CreateRecording")]

GetTestConfigurationPath()[¶](#ApiClient.AnalysisJob.GetTestConfigurationPath "Link to this definition")  
Returns the path to the test configuration file, absolute or relative to the ‘Configuration’ directory.

Returns:  Path to the test configuration or None

Return type:  str

RemoveGenericSignal(*[genericSignal](#ApiClient.AnalysisJob.RemoveGenericSignal.genericSignal "ApiClient.AnalysisJob.RemoveGenericSignal.genericSignal (Python parameter) — Existing generic signal")*)[¶](#ApiClient.AnalysisJob.RemoveGenericSignal "Link to this definition")  
Removes a generic signal.

Parameters:  genericSignal[¶](#ApiClient.AnalysisJob.RemoveGenericSignal.genericSignal "Permalink to this definition")  
Existing generic signal

RemoveParameter(*[name](#ApiClient.AnalysisJob.RemoveParameter.name "ApiClient.AnalysisJob.RemoveParameter.name (Python parameter) — Name of the parameter to remove")*)[¶](#ApiClient.AnalysisJob.RemoveParameter "Link to this definition")  
Removes the parameter specified by the given name.

Parameters:  name : str[¶](#ApiClient.AnalysisJob.RemoveParameter.name "Permalink to this definition")  
Name of the parameter to remove

Raises:  
ApiError: When parameter does not exist

RemoveRecording(*[recording](#ApiClient.AnalysisJob.RemoveRecording.recording "ApiClient.AnalysisJob.RemoveRecording.recording (Python parameter) — Existing recording.")*)[¶](#ApiClient.AnalysisJob.RemoveRecording "Link to this definition")  
Removes a recording.

Parameters:  recording[¶](#ApiClient.AnalysisJob.RemoveRecording.recording "Permalink to this definition")  
Existing recording.

Save(*[filename](#ApiClient.AnalysisJob.Save.filename "ApiClient.AnalysisJob.Save.filename (Python parameter) — Absolute or relative workspace file name of the analysis job. Leave out to save the package to its origin file (previously set with Save() or from TraceAnalysisApi.OpenAnalysisJob())")=`None`*)[¶](#ApiClient.AnalysisJob.Save "Link to this definition")  
Saves the analysis job.

Appends file ending (.ajob) if needed.

Parameters:  filename : str[¶](#ApiClient.AnalysisJob.Save.filename "Permalink to this definition")  
Absolute or relative workspace file name of the analysis job. Leave out to save the package to its origin file (previously set with [`Save()`](#ApiClient.AnalysisJob.Save "ApiClient.AnalysisJob.Save (Python method) — Saves the analysis job.") or from `TraceAnalysisApi.OpenAnalysisJob()`)

SetAnalysisReference(*[analysisName](#ApiClient.AnalysisJob.SetAnalysisReference.analysisName "ApiClient.AnalysisJob.SetAnalysisReference.analysisName (Python parameter) — name of the trace analysis within Package (GetPackageReference())")*)[¶](#ApiClient.AnalysisJob.SetAnalysisReference "Link to this definition")  
Sets the trace analysis to be used by the given name.

Parameters:  analysisName : str[¶](#ApiClient.AnalysisJob.SetAnalysisReference.analysisName "Permalink to this definition")  
name of the trace analysis within Package (`GetPackageReference()`)

SetGlobalConstants(*[value](#ApiClient.AnalysisJob.SetGlobalConstants.value "ApiClient.AnalysisJob.SetGlobalConstants.value (Python parameter) — new global constants")*)[¶](#ApiClient.AnalysisJob.SetGlobalConstants "Link to this definition")  
Sets the complete set of global constants.

Parameters:  value[¶](#ApiClient.AnalysisJob.SetGlobalConstants.value "Permalink to this definition")  
new global constants

SetPackageReference(*[packageReference](#ApiClient.AnalysisJob.SetPackageReference.packageReference "ApiClient.AnalysisJob.SetPackageReference.packageReference (Python parameter) — Package file path absolute or relative to workspace Packages directory")*)[¶](#ApiClient.AnalysisJob.SetPackageReference "Link to this definition")  
Sets the Package file path in which the corresponding trace analysis exists.

Parameters:  packageReference : str[¶](#ApiClient.AnalysisJob.SetPackageReference.packageReference "Permalink to this definition")  
Package file path absolute or relative to workspace Packages directory

SetParameter(*[name](#ApiClient.AnalysisJob.SetParameter.name "ApiClient.AnalysisJob.SetParameter.name (Python parameter) — Name of the parameter")*, *[valueExpression](#ApiClient.AnalysisJob.SetParameter.valueExpression "ApiClient.AnalysisJob.SetParameter.valueExpression (Python parameter) — Value to assign to the parameter (must be a Python literal expression, for example "'string'", "5", "[1, 2]", "None", "True")")*)[¶](#ApiClient.AnalysisJob.SetParameter "Link to this definition")  
Assigns a value to a parameter.

Parameters:  name : string[¶](#ApiClient.AnalysisJob.SetParameter.name "Permalink to this definition")  
Name of the parameter

valueExpression : str[¶](#ApiClient.AnalysisJob.SetParameter.valueExpression "Permalink to this definition")  
Value to assign to the parameter (must be a Python literal expression, for example “‘string’”, “5”, “[1, 2]”, “None”, “True”)

Raises:  
ApiError: When valueExpression is not a Python literal expression

SetParameters(*[parameters](#ApiClient.AnalysisJob.SetParameters.parameters "ApiClient.AnalysisJob.SetParameters.parameters (Python parameter) — Dictionary of parameter name -> parameter value (Python literal expression, for example "'string'", "5", "[1, 2]", "None", "True") mappings")*)[¶](#ApiClient.AnalysisJob.SetParameters "Link to this definition")  
Assigns values to parameters.

Parameters:  parameters : dict[str, str][¶](#ApiClient.AnalysisJob.SetParameters.parameters "Permalink to this definition")  
Dictionary of parameter name -> parameter value (Python literal expression, for example “‘string’”, “5”, “[1, 2]”, “None”, “True”) mappings

Raises:  
ApiError: When parameter value is not a Python literal expression

SetTestConfigurationPath(*[testConfiguration](#ApiClient.AnalysisJob.SetTestConfigurationPath.testConfiguration "ApiClient.AnalysisJob.SetTestConfigurationPath.testConfiguration (Python parameter) — Path to the test configuration file or None")*)[¶](#ApiClient.AnalysisJob.SetTestConfigurationPath "Link to this definition")  
Sets the path to the test configuration file, absolute or relative to the ‘Configuration’ directory.

Parameters:  testConfiguration : str[¶](#ApiClient.AnalysisJob.SetTestConfigurationPath.testConfiguration "Permalink to this definition")  
Path to the test configuration file or None

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
