# API for Signal Descriptions[¶](#api-for-signal-descriptions "Link to this heading")

Part of the [Object based program API](objectApi.md#objectapi)

## SignalDescriptionApi[¶](#signaldescriptionapi "Link to this heading")

*class* SignalDescriptionApi[¶](#ApiClient.SignalDescriptionApi "Link to this definition")  
API to access signal description files

Returned by

- [`ApiClient.SignalDescriptionApi`](objectApi.md#ApiClient.ApiClient.SignalDescriptionApi "ApiClient.ApiClient.SignalDescriptionApi")

SignalApi[¶](#ApiClient.SignalDescriptionApi.SignalApi "Link to this definition")  
Returns the SignalApi namespace.

Returns:  SignalApi namespace

Return type:  [`SignalApi`](SignalApi.md#ApiClient.SignalApi "ApiClient.SignalApi")

CreateSignalDescriptionFile()[¶](#ApiClient.SignalDescriptionApi.CreateSignalDescriptionFile "Link to this definition")  
Creates a new sti or stz file.

Returns:  Signal description

Return type:  [`SignalDescriptionFile`](#ApiClient.SignalDescriptionFile "ApiClient.SignalDescriptionFile")

OpenSignalDescriptionFile(*filename*, *upgradeLegacyFile=True*)[¶](#ApiClient.SignalDescriptionApi.OpenSignalDescriptionFile "Link to this definition")  
Opens an existing sti or stz file.

Parameters:  - **filename** (*str*) – Name of the signal description file to open

- **upgradeLegacyFile** (*bool*) – Selects whether a sti in version 1.0 should be upgraded or if loading should be aborted. A backup copy of the original file is saved at the same location with the suffix “.bak”.

Returns:  Signal description

Return type:  [`SignalDescriptionFile`](#ApiClient.SignalDescriptionFile "ApiClient.SignalDescriptionFile")

## SignalDescriptionFile[¶](#signaldescriptionfile "Link to this heading")

*class* SignalDescriptionFile[¶](#ApiClient.SignalDescriptionFile "Link to this definition")  
Returned by

- [`SignalDescriptionApi.CreateSignalDescriptionFile`](#ApiClient.SignalDescriptionApi.CreateSignalDescriptionFile "ApiClient.SignalDescriptionApi.CreateSignalDescriptionFile")

- [`SignalDescriptionApi.OpenSignalDescriptionFile`](#ApiClient.SignalDescriptionApi.OpenSignalDescriptionFile "ApiClient.SignalDescriptionApi.OpenSignalDescriptionFile")

AppendInputSignal(*signalName*)[¶](#ApiClient.SignalDescriptionFile.AppendInputSignal "Link to this definition")  
Append an input signal.

Parameters:  **signalName** (*str*) – The input signal name

AppendSignal(*signal*)[¶](#ApiClient.SignalDescriptionFile.AppendSignal "Link to this definition")  
Append a signal description as last element.

Parameters:  **signal** ([`SignalDescription`](SignalApi.md#ApiClient.SignalDescription "ApiClient.SignalDescription")) – Signal description

ClearInputSignals()[¶](#ApiClient.SignalDescriptionFile.ClearInputSignals "Link to this definition")  
Clear the input signals defined in the description file.

Clone()[¶](#ApiClient.SignalDescriptionFile.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`SignalDescriptionFile`](#ApiClient.SignalDescriptionFile "ApiClient.SignalDescriptionFile")

Close()[¶](#ApiClient.SignalDescriptionFile.Close "Link to this definition")  
Closes the signal description. After closing the file it can not be modified/accessed anymore.

ConvertToMat(*destinationPath*, *sampleRate=100*, *signalList=None*)[¶](#ApiClient.SignalDescriptionFile.ConvertToMat "Link to this definition")  
Converts the signals in the description file to a new MAT file

Parameters:  - **destinationPath** (*str*) – Absolute path to store MAT file

- **sampleRate** (*integer*) – Number of samples per second

- **signalList** (*list[str]*) – Signal names to be exported or None to export all signals

GetAllSignalNames()[¶](#ApiClient.SignalDescriptionFile.GetAllSignalNames "Link to this definition")  
Returns a list of names of all signals defined in the description file

Returns:  Signal names

Return type:  list[str]

GetAllSignals()[¶](#ApiClient.SignalDescriptionFile.GetAllSignals "Link to this definition")  
Returns a list of all signals defined in the description file

Returns:  Signals

Return type:  list[[`SignalDescription`](SignalApi.md#ApiClient.SignalDescription "ApiClient.SignalDescription")]

GetInputSignals()[¶](#ApiClient.SignalDescriptionFile.GetInputSignals "Link to this definition")  
Returns a list of all input signals defined in the description file.

Returns:  The input signal names

Return type:  list[str]

GetParameterComment(*parameterName*)[¶](#ApiClient.SignalDescriptionFile.GetParameterComment "Link to this definition")  
Returns the description of a parameter.

Parameters:  **parameterName** (*str*) – The name of the parameter

Returns:  The description of the parameter

Return type:  str

GetParameterNames()[¶](#ApiClient.SignalDescriptionFile.GetParameterNames "Link to this definition")  
Returns an alphabetically sorted list of parameter names that are specified in this file.

Returns:  List of parameter names

Return type:  list[str]

GetParameterValue(*parameterName*)[¶](#ApiClient.SignalDescriptionFile.GetParameterValue "Link to this definition")  
Returns the default value of a parameter.

Parameters:  **parameterName** (*str*) – The name of the parameter

Returns:  The default value of the parameter

Return type:  float

RemoveInputSignal(*signalName*)[¶](#ApiClient.SignalDescriptionFile.RemoveInputSignal "Link to this definition")  
Remove an input signal.

Parameters:  **signalName** (*str*) – The input signal name

RemoveParameter(*parameterName*)[¶](#ApiClient.SignalDescriptionFile.RemoveParameter "Link to this definition")  
Removes a parameter from the signal description file.

Parameters:  **parameterName** (*str*) – The name of the parameter that shall be removed

RemoveSignal(*signal*)[¶](#ApiClient.SignalDescriptionFile.RemoveSignal "Link to this definition")  
Remove a signal description.

Parameters:  **signal** ([`SignalDescription`](SignalApi.md#ApiClient.SignalDescription "ApiClient.SignalDescription")) – Signal description

SaveSti(*destinationPath*, *version='2.1'*, *absFileReference=False*)[¶](#ApiClient.SignalDescriptionFile.SaveSti "Link to this definition")  
Stores the current signal description to a sti file.

Parameters:  - **destinationPath** (*str*) – Absolute path to store STI file

- **version** (*str*) – STI Version with which the stimulation file should be saved

- **absFileReference** (*bool*) – STI file is created with absolute file references

SaveStz(*destinationPath*, *version='2.1'*)[¶](#ApiClient.SignalDescriptionFile.SaveStz "Link to this definition")  
Stores the current signal description to a stz file. The stz will also contain all referenced signal descriptions

Parameters:  - **destinationPath** (*str*) – Absolute path to store STZ file

- **version** (*str*) – STZ Version with which the stimulation file should be saved

SetParameter(*parameterName*, *defaultValue*, *comment=''*)[¶](#ApiClient.SignalDescriptionFile.SetParameter "Link to this definition")  
Adds a new parameter to the signal description file. If a parameter with this name already exists, the defaultValue and comment will be overwritten.

Parameters:  - **parameterName** (*str*) – The name of the parameter

- **defaultValue** (*float*) – The default value of the parameter

- **comment** (*str*) – Description of the parameter
