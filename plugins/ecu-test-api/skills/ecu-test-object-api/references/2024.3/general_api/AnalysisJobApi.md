# API for Analysis Jobs[¶](#api-for-analysis-jobs "Link to this heading")

Part of the [Object based program API](objectApi.md#objectapi)

## AnalysisJobApi[¶](#analysisjobapi "Link to this heading")

*class* AnalysisJobApi[¶](#ApiClient.AnalysisJobApi "Link to this definition")  
Returned by

- [`ApiClient.AnalysisJobApi`](objectApi.md#ApiClient.ApiClient.AnalysisJobApi "ApiClient.ApiClient.AnalysisJobApi")

CreateAnalysisJob()[¶](#ApiClient.AnalysisJobApi.CreateAnalysisJob "Link to this definition")  
Creates a new analysis job

Returns:  A newly created analysis job

Return type:  [`AnalysisJob`](#ApiClient.AnalysisJob "ApiClient.AnalysisJob")

CreateGenericSignal(*signalName*)[¶](#ApiClient.AnalysisJobApi.CreateGenericSignal "Link to this definition")  
Create a generic signal with a given name for a analysis job.

Parameters:  **signalName** (*str*) – signal name

Returns:  newly created generic analysis job signal

Return type:  [`AnalysisJobGenericSignal`](#ApiClient.AnalysisJobGenericSignal "ApiClient.AnalysisJobGenericSignal")

CreateRecording(*recordingName*)[¶](#ApiClient.AnalysisJobApi.CreateRecording "Link to this definition")  
Create a recording for a analysis job.

Parameters:  **recordingName** (*str*) – recording name

Returns:  newly created analysis job recording

Return type:  [`AnalysisJobRecording`](#ApiClient.AnalysisJobRecording "ApiClient.AnalysisJobRecording")

OpenAnalysisJob(*filename*)[¶](#ApiClient.AnalysisJobApi.OpenAnalysisJob "Link to this definition")  
Opens an existing analysis job

Parameters:  **filename** (*str*) – Absolute path to the analysis job file (.ajob) or relative path in regard to the workspace directory

Returns:  Existing analysis job

Return type:  [`AnalysisJob`](#ApiClient.AnalysisJob "ApiClient.AnalysisJob")

## AnalysisJob[¶](#analysisjob "Link to this heading")

*class* AnalysisJob[¶](#ApiClient.AnalysisJob "Link to this definition")  
Returned by

- [`AnalysisJobApi.CreateAnalysisJob`](#ApiClient.AnalysisJobApi.CreateAnalysisJob "ApiClient.AnalysisJobApi.CreateAnalysisJob")

- [`AnalysisJobApi.OpenAnalysisJob`](#ApiClient.AnalysisJobApi.OpenAnalysisJob "ApiClient.AnalysisJobApi.OpenAnalysisJob")

AddGenericSignal(*genericSignal*)[¶](#ApiClient.AnalysisJob.AddGenericSignal "Link to this definition")  
Adds a new generic signal.

Note:  
The name of the generic signal should be unique.

Parameters:  **genericSignal** ([`AnalysisJobGenericSignal`](#ApiClient.AnalysisJobGenericSignal "ApiClient.AnalysisJobGenericSignal")) – Generic signal to add

AddRecording(*recording*)[¶](#ApiClient.AnalysisJob.AddRecording "Link to this definition")  
Adds a new recording.

Note:  
The name of the recordings should be unique.

Parameters:  **recording** ([`AnalysisJobRecording`](#ApiClient.AnalysisJobRecording "ApiClient.AnalysisJobRecording")) – Recording to add

Clone()[¶](#ApiClient.AnalysisJob.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`AnalysisJob`](#ApiClient.AnalysisJob "ApiClient.AnalysisJob")

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

Return type:  list[[`AnalysisJobGenericSignal`](#ApiClient.AnalysisJobGenericSignal "ApiClient.AnalysisJobGenericSignal")]

GetGlobalConstants()[¶](#ApiClient.AnalysisJob.GetGlobalConstants "Link to this definition")  
Returns the container of defined global constants.

Returns:  Container for global constants

Return type:  [`GlobalConstantsDefinition`](ParameterApi.md#ApiClient.GlobalConstantsDefinition "ApiClient.GlobalConstantsDefinition")

GetMapping()[¶](#ApiClient.AnalysisJob.GetMapping "Link to this definition")  
Returns the mapping of the analysis job.

Returns:  Mapping of the analysis job

Return type:  [`Mapping`](MappingApi.md#ApiClient.Mapping "ApiClient.Mapping")

GetPackageReference()[¶](#ApiClient.AnalysisJob.GetPackageReference "Link to this definition")  
Returns the absolute Package file path in which the corresponding trace analysis exists.

Returns:  Package file path or None, if not set.

Return type:  str

GetParameter(*name*)[¶](#ApiClient.AnalysisJob.GetParameter "Link to this definition")  
Retrieves the value assigned to a parameter.

Parameters:  **name** (*string*) – Name of the parameter

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

Return type:  list[[`AnalysisJobRecording`](#ApiClient.AnalysisJobRecording "ApiClient.AnalysisJobRecording")]

GetTestConfigurationPath()[¶](#ApiClient.AnalysisJob.GetTestConfigurationPath "Link to this definition")  
Returns the path to the test configuration file, absolute or relative to the ‘Configuration’ directory.

Returns:  Path to the test configuration or None

Return type:  str

RemoveGenericSignal(*genericSignal*)[¶](#ApiClient.AnalysisJob.RemoveGenericSignal "Link to this definition")  
Removes a generic signal.

Parameters:  **genericSignal** ([`AnalysisJobGenericSignal`](#ApiClient.AnalysisJobGenericSignal "ApiClient.AnalysisJobGenericSignal")) – Existing generic signal

RemoveParameter(*name*)[¶](#ApiClient.AnalysisJob.RemoveParameter "Link to this definition")  
Removes the parameter specified by the given name.

Parameters:  **name** (*str*) – Name of the parameter to remove

Raises:  
ApiError: When parameter does not exist

RemoveRecording(*recording*)[¶](#ApiClient.AnalysisJob.RemoveRecording "Link to this definition")  
Removes a recording.

Parameters:  **recording** ([`AnalysisJobRecording`](#ApiClient.AnalysisJobRecording "ApiClient.AnalysisJobRecording")) – Existing recording.

Save(*filename=None*)[¶](#ApiClient.AnalysisJob.Save "Link to this definition")  
Saves the analysis job.

Appends file ending (.ajob) if needed.

Parameters:  **filename** (*str*) – Absolute or relative workspace file name of the analysis job. Leave out to save the package to its origin file (previously set with [`Save()`](#ApiClient.AnalysisJob.Save "ApiClient.AnalysisJob.Save") or from `TraceAnalysisApi.OpenAnalysisJob()`)

SetAnalysisReference(*analysisName*)[¶](#ApiClient.AnalysisJob.SetAnalysisReference "Link to this definition")  
Sets the trace analysis to be used by the given name.

Parameters:  **analysisName** (*str*) – name of the trace analysis within Package (`GetPackageReference()`)

SetGlobalConstants(*value*)[¶](#ApiClient.AnalysisJob.SetGlobalConstants "Link to this definition")  
Sets the complete set of global constants.

Parameters:  **value** ([`GlobalConstantsDefinition`](ParameterApi.md#ApiClient.GlobalConstantsDefinition "ApiClient.GlobalConstantsDefinition")) – new global constants

SetPackageReference(*packageReference*)[¶](#ApiClient.AnalysisJob.SetPackageReference "Link to this definition")  
Sets the Package file path in which the corresponding trace analysis exists.

Parameters:  **packageReference** (*str*) – Package file path absolute or relative to workspace Packages directory

SetParameter(*name*, *valueExpression*)[¶](#ApiClient.AnalysisJob.SetParameter "Link to this definition")  
Assigns a value to a parameter.

Parameters:  - **name** (*string*) – Name of the parameter

- **valueExpression** (*str*) – Value to assign to the parameter (must be a Python literal expression, for example “‘string’”, “5”, “[1, 2]”, “None”, “True”)

Raises:  
ApiError: When valueExpression is not a Python literal expression

SetParameters(*parameters*)[¶](#ApiClient.AnalysisJob.SetParameters "Link to this definition")  
Assigns values to parameters.

Parameters:  **parameters** (*dict[str,* *str]*) – Dictionary of parameter name -> parameter value (Python literal expression, for example “‘string’”, “5”, “[1, 2]”, “None”, “True”) mappings

Raises:  
ApiError: When parameter value is not a Python literal expression

SetTestConfigurationPath(*testConfiguration*)[¶](#ApiClient.AnalysisJob.SetTestConfigurationPath "Link to this definition")  
Sets the path to the test configuration file, absolute or relative to the ‘Configuration’ directory.

Parameters:  **testConfiguration** (*str*) – Path to the test configuration file or None

## AnalysisJobGenericSignal[¶](#analysisjobgenericsignal "Link to this heading")

*class* AnalysisJobGenericSignal[¶](#ApiClient.AnalysisJobGenericSignal "Link to this definition")  
Returned by

- [`AnalysisJob.GetGenericSignals`](#ApiClient.AnalysisJob.GetGenericSignals "ApiClient.AnalysisJob.GetGenericSignals")

- [`AnalysisJobApi.CreateGenericSignal`](#ApiClient.AnalysisJobApi.CreateGenericSignal "ApiClient.AnalysisJobApi.CreateGenericSignal")

Clone()[¶](#ApiClient.AnalysisJobGenericSignal.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`AnalysisJobGenericSignal`](#ApiClient.AnalysisJobGenericSignal "ApiClient.AnalysisJobGenericSignal")

GetMappingName()[¶](#ApiClient.AnalysisJobGenericSignal.GetMappingName "Link to this definition")  
Returns the name of the mapping item of the recoding assigned to the generic signal.

Returns:  mapping name assigned to this signal, which is used to resolve the real signal.

Return type:  str

GetName()[¶](#ApiClient.AnalysisJobGenericSignal.GetName "Link to this definition")  
Returns the name of the generic signal.

Returns:  name of generic signal

Return type:  str

GetRecording(*analysisJob*)[¶](#ApiClient.AnalysisJobGenericSignal.GetRecording "Link to this definition")  
Get assigned recording from analysis job.

Note:  
Do not use in the context of a analysis package (\*.ta)

Parameters:  **analysisJob** ([`AnalysisJob`](#ApiClient.AnalysisJob "ApiClient.AnalysisJob")) – analysis job from which the assigned recording should be extracted.

Returns:  recording from analysis job which is assigned to the signal

Return type:  [`AnalysisJobRecording`](#ApiClient.AnalysisJobRecording "ApiClient.AnalysisJobRecording")

SetMappingName(*mappingName*)[¶](#ApiClient.AnalysisJobGenericSignal.SetMappingName "Link to this definition")  
Sets mapping name, which should be used to resolve the signal.

Parameters:  **mappingName** (*str*) – name of an existing mapping.

SetRecording(*recording*)[¶](#ApiClient.AnalysisJobGenericSignal.SetRecording "Link to this definition")  
Set reference to recording which the signal will use.

Note:  
Do not use in the context of a analysis package (\*.ta)

Parameters:  **recording** ([`AnalysisJobRecording`](#ApiClient.AnalysisJobRecording "ApiClient.AnalysisJobRecording")) – recording or None, when signal should be resolved only from the mapping item name. In the last case the mapping name must be unique in the analysis job.

## AnalysisJobRecording[¶](#analysisjobrecording "Link to this heading")

*class* AnalysisJobRecording[¶](#ApiClient.AnalysisJobRecording "Link to this definition")  
Returned by

- [`AnalysisJob.GetRecordings`](#ApiClient.AnalysisJob.GetRecordings "ApiClient.AnalysisJob.GetRecordings")

- [`AnalysisJobApi.CreateRecording`](#ApiClient.AnalysisJobApi.CreateRecording "ApiClient.AnalysisJobApi.CreateRecording")

- [`AnalysisJobGenericSignal.GetRecording`](#ApiClient.AnalysisJobGenericSignal.GetRecording "ApiClient.AnalysisJobGenericSignal.GetRecording")

AddMappingName(*mappingName*)[¶](#ApiClient.AnalysisJobRecording.AddMappingName "Link to this definition")  
Adds mapping name to this recording.

Note:  
Only use in the context of a analysis package (\*.ta)

Parameters:  **mappingName** (*str*) – Mapping name to add

Clone()[¶](#ApiClient.AnalysisJobRecording.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`AnalysisJobRecording`](#ApiClient.AnalysisJobRecording "ApiClient.AnalysisJobRecording")

GetDescription()[¶](#ApiClient.AnalysisJobRecording.GetDescription "Link to this definition")  
Returns description of recording (corresponds to recording group description in trace analysis)

Returns:  Description of this recording

Return type:  str

GetMappingNames()[¶](#ApiClient.AnalysisJobRecording.GetMappingNames "Link to this definition")  
Returns all mapping names of this recording.

Note:  
Only use in the context of a analysis package (\*.ta)

Returns:  Mapping names

Return type:  list[str]

GetName()[¶](#ApiClient.AnalysisJobRecording.GetName "Link to this definition")  
Returns name of recording (corresponds to recording group name in trace analysis)

Returns:  Name of this recording

Return type:  str

GetRecordingInfo()[¶](#ApiClient.AnalysisJobRecording.GetRecordingInfo "Link to this definition")  
Returns recording info object of the recording

Returns:  Recording info object of the recording

Return type:  [`RecordingInfo`](SignalRecordingApi.md#ApiClient.RecordingInfo "ApiClient.RecordingInfo")

RemoveMappingName(*mappingName*)[¶](#ApiClient.AnalysisJobRecording.RemoveMappingName "Link to this definition")  
Removes mapping name from this recording.

Note:  
Only use in the context of a analysis package (\*.ta)

Parameters:  **mappingName** (*str*) – Mapping name to remove

SetDescription(*value*)[¶](#ApiClient.AnalysisJobRecording.SetDescription "Link to this definition")  
Sets description of recording.

Parameters:  **value** (*str*) – New description

SetMappingNames(*mappingNames*)[¶](#ApiClient.AnalysisJobRecording.SetMappingNames "Link to this definition")  
Sets mapping names of this recording.

Note:  
Only use in the context of a analysis package (\*.ta)

Parameters:  **mappingNames** (*list[str]*) – New mapping names

SetRecordingInfo(*value*)[¶](#ApiClient.AnalysisJobRecording.SetRecordingInfo "Link to this definition")  
Sets recording info object of the recording

Parameters:  **value** ([`RecordingInfo`](SignalRecordingApi.md#ApiClient.RecordingInfo "ApiClient.RecordingInfo")) – New recording info object
