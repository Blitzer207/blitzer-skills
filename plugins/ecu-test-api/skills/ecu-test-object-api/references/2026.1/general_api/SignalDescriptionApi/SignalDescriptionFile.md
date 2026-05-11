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

[ API for Parameters ](../ParameterApi.md)

[ API for Projects ](../ProjectApi.md)

[ API for Relations ](../RelationApi.md)

[ API for Reports ](../ReportApi.md)

[ API for Report Filters ](../ReportFilterApi.md)

[ API for Settings ](../SettingsApi.md)

[ API for Signals ](../SignalApi.md)

[ API for Signal Descriptions ](../SignalDescriptionApi.md)

API for Signal Descriptions

SignalDescriptionFile [ SignalDescriptionFile ](#)

SignalDescriptionFile

- [C SignalDescriptionFile ](#ApiClient.SignalDescriptionFile)
  - [M AppendInputSignal ](#ApiClient.SignalDescriptionFile.AppendInputSignal)
  - [M AppendSignal ](#ApiClient.SignalDescriptionFile.AppendSignal)
  - [M ClearInputSignals ](#ApiClient.SignalDescriptionFile.ClearInputSignals)
  - [M Clone ](#ApiClient.SignalDescriptionFile.Clone)
  - [M Close ](#ApiClient.SignalDescriptionFile.Close)
  - [M ConvertToMat ](#ApiClient.SignalDescriptionFile.ConvertToMat)
  - [M GetAllSignalNames ](#ApiClient.SignalDescriptionFile.GetAllSignalNames)
  - [M GetAllSignals ](#ApiClient.SignalDescriptionFile.GetAllSignals)
  - [M GetInputSignals ](#ApiClient.SignalDescriptionFile.GetInputSignals)
  - [M GetParameterComment ](#ApiClient.SignalDescriptionFile.GetParameterComment)
  - [M GetParameterNames ](#ApiClient.SignalDescriptionFile.GetParameterNames)
  - [M GetParameterValue ](#ApiClient.SignalDescriptionFile.GetParameterValue)
  - [M RemoveInputSignal ](#ApiClient.SignalDescriptionFile.RemoveInputSignal)
  - [M RemoveParameter ](#ApiClient.SignalDescriptionFile.RemoveParameter)
  - [M RemoveSignal ](#ApiClient.SignalDescriptionFile.RemoveSignal)
  - [M SaveSti ](#ApiClient.SignalDescriptionFile.SaveSti)
  - [M SaveStz ](#ApiClient.SignalDescriptionFile.SaveStz)
  - [M SetParameter ](#ApiClient.SignalDescriptionFile.SetParameter)

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

SignalDescriptionFile

- [C SignalDescriptionFile ](#ApiClient.SignalDescriptionFile)
  - [M AppendInputSignal ](#ApiClient.SignalDescriptionFile.AppendInputSignal)
  - [M AppendSignal ](#ApiClient.SignalDescriptionFile.AppendSignal)
  - [M ClearInputSignals ](#ApiClient.SignalDescriptionFile.ClearInputSignals)
  - [M Clone ](#ApiClient.SignalDescriptionFile.Clone)
  - [M Close ](#ApiClient.SignalDescriptionFile.Close)
  - [M ConvertToMat ](#ApiClient.SignalDescriptionFile.ConvertToMat)
  - [M GetAllSignalNames ](#ApiClient.SignalDescriptionFile.GetAllSignalNames)
  - [M GetAllSignals ](#ApiClient.SignalDescriptionFile.GetAllSignals)
  - [M GetInputSignals ](#ApiClient.SignalDescriptionFile.GetInputSignals)
  - [M GetParameterComment ](#ApiClient.SignalDescriptionFile.GetParameterComment)
  - [M GetParameterNames ](#ApiClient.SignalDescriptionFile.GetParameterNames)
  - [M GetParameterValue ](#ApiClient.SignalDescriptionFile.GetParameterValue)
  - [M RemoveInputSignal ](#ApiClient.SignalDescriptionFile.RemoveInputSignal)
  - [M RemoveParameter ](#ApiClient.SignalDescriptionFile.RemoveParameter)
  - [M RemoveSignal ](#ApiClient.SignalDescriptionFile.RemoveSignal)
  - [M SaveSti ](#ApiClient.SignalDescriptionFile.SaveSti)
  - [M SaveStz ](#ApiClient.SignalDescriptionFile.SaveStz)
  - [M SetParameter ](#ApiClient.SignalDescriptionFile.SetParameter)

# SignalDescriptionFile[¶](#signaldescriptionfile "Link to this heading")

*class* SignalDescriptionFile[¶](#ApiClient.SignalDescriptionFile "Link to this definition")  
Returned by

- [`SignalDescriptionApi.CreateSignalDescriptionFile`](../SignalDescriptionApi.md#ApiClient.SignalDescriptionApi.CreateSignalDescriptionFile "ApiClient.SignalDescriptionApi.CreateSignalDescriptionFile (Python method) — Creates a new sti or stz file.")

- [`SignalDescriptionApi.OpenSignalDescriptionFile`](../SignalDescriptionApi.md#ApiClient.SignalDescriptionApi.OpenSignalDescriptionFile "ApiClient.SignalDescriptionApi.OpenSignalDescriptionFile (Python method) — Opens an existing sti or stz file.")

AppendInputSignal(*[signalName](#ApiClient.SignalDescriptionFile.AppendInputSignal.signalName "ApiClient.SignalDescriptionFile.AppendInputSignal.signalName (Python parameter) — The input signal name")*)[¶](#ApiClient.SignalDescriptionFile.AppendInputSignal "Link to this definition")  
Append an input signal.

Parameters:  signalName : str[¶](#ApiClient.SignalDescriptionFile.AppendInputSignal.signalName "Permalink to this definition")  
The input signal name

AppendSignal(*[signal](#ApiClient.SignalDescriptionFile.AppendSignal.signal "ApiClient.SignalDescriptionFile.AppendSignal.signal (Python parameter) — Signal description")*)[¶](#ApiClient.SignalDescriptionFile.AppendSignal "Link to this definition")  
Append a signal description as last element.

Parameters:  signal[¶](#ApiClient.SignalDescriptionFile.AppendSignal.signal "Permalink to this definition")  
Signal description

ClearInputSignals()[¶](#ApiClient.SignalDescriptionFile.ClearInputSignals "Link to this definition")  
Clear the input signals defined in the description file.

Clone()[¶](#ApiClient.SignalDescriptionFile.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`SignalDescriptionFile`](#ApiClient.SignalDescriptionFile "ApiClient.SignalDescriptionFile (Python class) — SignalDescriptionApi.CreateSignalDescriptionFile")

Close()[¶](#ApiClient.SignalDescriptionFile.Close "Link to this definition")  
Closes the signal description. After closing the file it can not be modified/accessed anymore.

ConvertToMat(*[destinationPath](#ApiClient.SignalDescriptionFile.ConvertToMat.destinationPath "ApiClient.SignalDescriptionFile.ConvertToMat.destinationPath (Python parameter) — Absolute path to store MAT file")*, *[sampleRate](#ApiClient.SignalDescriptionFile.ConvertToMat.sampleRate "ApiClient.SignalDescriptionFile.ConvertToMat.sampleRate (Python parameter) — Number of samples per second")=`100`*, *[signalList](#ApiClient.SignalDescriptionFile.ConvertToMat.signalList "ApiClient.SignalDescriptionFile.ConvertToMat.signalList (Python parameter) — Signal names to be exported or None to export all signals")=`None`*)[¶](#ApiClient.SignalDescriptionFile.ConvertToMat "Link to this definition")  
Converts the signals in the description file to a new MAT file

Parameters:  destinationPath : str[¶](#ApiClient.SignalDescriptionFile.ConvertToMat.destinationPath "Permalink to this definition")  
Absolute path to store MAT file

sampleRate : integer[¶](#ApiClient.SignalDescriptionFile.ConvertToMat.sampleRate "Permalink to this definition")  
Number of samples per second

signalList : list[str][¶](#ApiClient.SignalDescriptionFile.ConvertToMat.signalList "Permalink to this definition")  
Signal names to be exported or None to export all signals

GetAllSignalNames()[¶](#ApiClient.SignalDescriptionFile.GetAllSignalNames "Link to this definition")  
Returns a list of names of all signals defined in the description file

Returns:  Signal names

Return type:  list[str]

GetAllSignals()[¶](#ApiClient.SignalDescriptionFile.GetAllSignals "Link to this definition")  
Returns a list of all signals defined in the description file

Returns:  Signals

Return type:  list[[`SignalDescription`](../SignalApi/SignalDescription.md#ApiClient.SignalDescription "ApiClient.SignalDescription (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")]

GetInputSignals()[¶](#ApiClient.SignalDescriptionFile.GetInputSignals "Link to this definition")  
Returns a list of all input signals defined in the description file.

Returns:  The input signal names

Return type:  list[str]

GetParameterComment(*[parameterName](#ApiClient.SignalDescriptionFile.GetParameterComment.parameterName "ApiClient.SignalDescriptionFile.GetParameterComment.parameterName (Python parameter) — The name of the parameter")*)[¶](#ApiClient.SignalDescriptionFile.GetParameterComment "Link to this definition")  
Returns the description of a parameter.

Parameters:  parameterName : str[¶](#ApiClient.SignalDescriptionFile.GetParameterComment.parameterName "Permalink to this definition")  
The name of the parameter

Returns:  The description of the parameter

Return type:  str

GetParameterNames()[¶](#ApiClient.SignalDescriptionFile.GetParameterNames "Link to this definition")  
Returns an alphabetically sorted list of parameter names that are specified in this file.

Returns:  List of parameter names

Return type:  list[str]

GetParameterValue(*[parameterName](#ApiClient.SignalDescriptionFile.GetParameterValue.parameterName "ApiClient.SignalDescriptionFile.GetParameterValue.parameterName (Python parameter) — The name of the parameter")*)[¶](#ApiClient.SignalDescriptionFile.GetParameterValue "Link to this definition")  
Returns the default value of a parameter.

Parameters:  parameterName : str[¶](#ApiClient.SignalDescriptionFile.GetParameterValue.parameterName "Permalink to this definition")  
The name of the parameter

Returns:  The default value of the parameter

Return type:  float

RemoveInputSignal(*[signalName](#ApiClient.SignalDescriptionFile.RemoveInputSignal.signalName "ApiClient.SignalDescriptionFile.RemoveInputSignal.signalName (Python parameter) — The input signal name")*)[¶](#ApiClient.SignalDescriptionFile.RemoveInputSignal "Link to this definition")  
Remove an input signal.

Parameters:  signalName : str[¶](#ApiClient.SignalDescriptionFile.RemoveInputSignal.signalName "Permalink to this definition")  
The input signal name

RemoveParameter(*[parameterName](#ApiClient.SignalDescriptionFile.RemoveParameter.parameterName "ApiClient.SignalDescriptionFile.RemoveParameter.parameterName (Python parameter) — The name of the parameter that shall be removed")*)[¶](#ApiClient.SignalDescriptionFile.RemoveParameter "Link to this definition")  
Removes a parameter from the signal description file.

Parameters:  parameterName : str[¶](#ApiClient.SignalDescriptionFile.RemoveParameter.parameterName "Permalink to this definition")  
The name of the parameter that shall be removed

RemoveSignal(*[signal](#ApiClient.SignalDescriptionFile.RemoveSignal.signal "ApiClient.SignalDescriptionFile.RemoveSignal.signal (Python parameter) — Signal description")*)[¶](#ApiClient.SignalDescriptionFile.RemoveSignal "Link to this definition")  
Remove a signal description.

Parameters:  signal[¶](#ApiClient.SignalDescriptionFile.RemoveSignal.signal "Permalink to this definition")  
Signal description

SaveSti(*[destinationPath](#ApiClient.SignalDescriptionFile.SaveSti.destinationPath "ApiClient.SignalDescriptionFile.SaveSti.destinationPath (Python parameter) — Absolute path to store STI file")*, *[version](#ApiClient.SignalDescriptionFile.SaveSti.version "ApiClient.SignalDescriptionFile.SaveSti.version (Python parameter) — STI Version with which the stimulation file should be saved")=`'2.1'`*, *[absFileReference](#ApiClient.SignalDescriptionFile.SaveSti.absFileReference "ApiClient.SignalDescriptionFile.SaveSti.absFileReference (Python parameter) — STI file is created with absolute file references")=`False`*)[¶](#ApiClient.SignalDescriptionFile.SaveSti "Link to this definition")  
Stores the current signal description to a sti file.

Parameters:  destinationPath : str[¶](#ApiClient.SignalDescriptionFile.SaveSti.destinationPath "Permalink to this definition")  
Absolute path to store STI file

version : str[¶](#ApiClient.SignalDescriptionFile.SaveSti.version "Permalink to this definition")  
STI Version with which the stimulation file should be saved

absFileReference : bool[¶](#ApiClient.SignalDescriptionFile.SaveSti.absFileReference "Permalink to this definition")  
STI file is created with absolute file references

SaveStz(*[destinationPath](#ApiClient.SignalDescriptionFile.SaveStz.destinationPath "ApiClient.SignalDescriptionFile.SaveStz.destinationPath (Python parameter) — Absolute path to store STZ file")*, *[version](#ApiClient.SignalDescriptionFile.SaveStz.version "ApiClient.SignalDescriptionFile.SaveStz.version (Python parameter) — STZ Version with which the stimulation file should be saved")=`'2.1'`*)[¶](#ApiClient.SignalDescriptionFile.SaveStz "Link to this definition")  
Stores the current signal description to a stz file. The stz will also contain all referenced signal descriptions

Parameters:  destinationPath : str[¶](#ApiClient.SignalDescriptionFile.SaveStz.destinationPath "Permalink to this definition")  
Absolute path to store STZ file

version : str[¶](#ApiClient.SignalDescriptionFile.SaveStz.version "Permalink to this definition")  
STZ Version with which the stimulation file should be saved

SetParameter(*[parameterName](#ApiClient.SignalDescriptionFile.SetParameter.parameterName "ApiClient.SignalDescriptionFile.SetParameter.parameterName (Python parameter) — The name of the parameter")*, *[defaultValue](#ApiClient.SignalDescriptionFile.SetParameter.defaultValue "ApiClient.SignalDescriptionFile.SetParameter.defaultValue (Python parameter) — The default value of the parameter")*, *[comment](#ApiClient.SignalDescriptionFile.SetParameter.comment "ApiClient.SignalDescriptionFile.SetParameter.comment (Python parameter) — Description of the parameter")=`''`*)[¶](#ApiClient.SignalDescriptionFile.SetParameter "Link to this definition")  
Adds a new parameter to the signal description file. If a parameter with this name already exists, the defaultValue and comment will be overwritten.

Parameters:  parameterName : str[¶](#ApiClient.SignalDescriptionFile.SetParameter.parameterName "Permalink to this definition")  
The name of the parameter

defaultValue : float[¶](#ApiClient.SignalDescriptionFile.SetParameter.defaultValue "Permalink to this definition")  
The default value of the parameter

comment : str[¶](#ApiClient.SignalDescriptionFile.SetParameter.comment "Permalink to this definition")  
Description of the parameter

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
