# API for Mappings[¶](#api-for-mappings "Link to this heading")

Part of the [Object based program API](objectApi.md#objectapi)

## MappingApi[¶](#mappingapi "Link to this heading")

*class* MappingApi[¶](#ApiClient.MappingApi "Link to this definition")  
Returned by

- [`PackageApi.MappingApi`](PackageApi.md#ApiClient.PackageApi.MappingApi "ApiClient.PackageApi.MappingApi")

CreateAnalysisPackageMappingItem(*pkgPath*, *referenceName=None*, *namespace=None*, *checkTarget=True*)[¶](#ApiClient.MappingApi.CreateAnalysisPackageMappingItem "Link to this definition")  
Creates an analysis package mapping item that references an analysis package (e.g. MyAnalysisPackage.ta). This mapping item can be used for analysis package mapping steps in a project, an analysis package reference in a test case or a referenced trace analysis. These steps do not reference a concrete analysis package. Instead, the implemented analysis label is resolved in the global mapping to get this reference.

Parameters:  - **pkgPath** (*str*) – Path to the referenced package, either absolute or relative to the packages directory of the current workspace or given namespace, e.g. ‘MyPackage.pkg’. An absolute path located in the current workspace will also be resolved to a relative workspace reference.

- **referenceName** (*str*) – Name of the mapping item

- **namespace** (*str*) – Identifier of the workspace to which a relative pkgPath is resolved. If not present or None, the namespace is determined automatically. It is also possible to reference a library workspace using its namespace. A relative pkgPath is resolved relative to the packages directory of the given namespace. For example, the namespace parameter ‘myLibrary’ results in ‘\<libraries.myLibrary.packages\>/MyPackage.pkg’.

- **checkTarget** (*boolean*) – Selects if path should be checked

Returns:  The just created mapping item.

Return type:  [`AnalysisPackageMappingItem`](#ApiClient.AnalysisPackageMappingItem "ApiClient.AnalysisPackageMappingItem")

CreateAudioChannelMappingItem(*systemIdentifier*, *channel=1*, *referenceName=None*, *checkTarget=None*)[¶](#ApiClient.MappingApi.CreateAudioChannelMappingItem "Link to this definition")  
Creates a mapping item pointing at a certain audio channel.

Parameters:  - **systemIdentifier** (*str*) – Name of the system according to the test configuration.

- **channel** (*int*) – Number of channel (optional). Uses channel 1 if ommitted.

- **referenceName** (*str*) – Name of the mapping item (optional).

- **checkTarget** (*boolean*) – Determines if the target path should be checked (optional).

Returns:  The new mapping item

Return type:  [`AudioChannelMappingItem`](#ApiClient.AudioChannelMappingItem "ApiClient.AudioChannelMappingItem")

CreateAudioDeviceMappingItem(*systemIdentifier*, *referenceName=None*, *checkTarget=True*)[¶](#ApiClient.MappingApi.CreateAudioDeviceMappingItem "Link to this definition")  
Creates a mapping item pointing at a certain audio device.

Parameters:  - **systemIdentifier** (*str*) – Name of the system according to the test configuration.

- **referenceName** (*str*) – Name of the mapping item (optional).

- **checkTarget** (*boolean*) – Determines if the target path should be checked (optional).

Returns:  The new mapping item

Return type:  [`AudioDeviceMappingItem`](#ApiClient.AudioDeviceMappingItem "ApiClient.AudioDeviceMappingItem")

CreateBusMonitoringMappingItem(*systemIdentifier*, *nodeName*, *frameName*, *referenceName=None*, *checkTarget=True*)[¶](#ApiClient.MappingApi.CreateBusMonitoringMappingItem "Link to this definition")  
Creates a bus monitoring mapping item of the desired variable type.

Parameters:  - **systemIdentifier** (*str*) – Name of Bus system according to the test configuration

- **nodeName** (*str*) – Name of sending ECU

- **frameName** (*str*) – Name of the frame containing the signal

- **referenceName** (*str*) – Name of the mapping item (optional)

- **checkTarget** (*boolean*) – Selects if target path should be checked (optional)

Returns:  The just created mapping item

Return type:  [`BusMonitoringMappingItem`](#ApiClient.BusMonitoringMappingItem "ApiClient.BusMonitoringMappingItem")

CreateBusSignalGroupMappingItem(*systemIdentifier*, *nodeName=''*, *frameName=''*, *pduName=''*, *referenceName=None*, *checkTarget=True*, *switchCode=None*)[¶](#ApiClient.MappingApi.CreateBusSignalGroupMappingItem "Link to this definition")  
Creates a bus signal group mapping item of the desired variable type.

Parameters:  - **systemIdentifier** (*str*) – Name of Bus system according to the test configuration

- **nodeName** (*str*) – Name of sending ECU (optional)

- **frameName** (*str*) – Name of the frame containing the signal (optional)

- **pduName** (*str*) – Name of the PDU containing the signal (optional)

- **referenceName** (*str*) – Name of the mapping item (optional)

- **checkTarget** (*boolean*) – Selects if target path should be checked (optional)

- **switchCode** (*int*) – In case the underlying bus database does not support PDU names, switch code can be specified to disambiguate between multiplexed PDUs

Returns:  The just created mapping item

Return type:  [`BusSignalGroupMappingItem`](#ApiClient.BusSignalGroupMappingItem "ApiClient.BusSignalGroupMappingItem")

CreateBusSignalWithPduMappingItem(*systemIdentifier*, *signalName*, *nodeName=''*, *frameName=''*, *pduName=''*, *referenceName=None*, *checkTarget=True*)[¶](#ApiClient.MappingApi.CreateBusSignalWithPduMappingItem "Link to this definition")  
Creates a bus signal mapping item of the desired variable type.

Parameters:  - **systemIdentifier** (*str*) – Name of Bus system according to the test configuration

- **signalName** (*str*) – Name of the signal

- **nodeName** (*str*) – Name of sending ECU (optional)

- **frameName** (*str*) – Name of the frame containing the signal (optional)

- **pduName** (*str*) – Name of the PDU containing the signal (optional)

- **referenceName** (*str*) – Name of the mapping item

- **checkTarget** (*boolean*) – Selects if target path should be checked

Returns:  The just created mapping item

Return type:  [`BusSignalMappingItem`](#ApiClient.BusSignalMappingItem "ApiClient.BusSignalMappingItem")

CreateCalibrationMappingItem(*systemIdentifier*, *targetPath*, *variableType=None*, *referenceName=None*, *xElement=None*, *yElement=None*, *checkTarget=True*)[¶](#ApiClient.MappingApi.CreateCalibrationMappingItem "Link to this definition")  
Creates a calibration mapping item of the desired variable type.

Parameters:  - **systemIdentifier** (*str*) – Name of ECU according to the test configuration

- **targetPath** (*str*) – Name of calibration variable to be accessed

- **variableType** (*str*) – Type of variable to be mapped (VALUE, VECTOR, MATRIX, CURVE, MAP, VECTOR-ELEMENT, MATRIX-ELEMENT)

- **referenceName** (*str*) – Name of the mapping item

- **xElement** (*integer*) – Index on x axis if single element of VECTOR or MATRIX should be accessed

- **yElement** (*integer*) – Index on y axis if single item of MATRIX should be accessed

- **checkTarget** (*boolean*) – Selects if target path should be checked

Returns:  The just created mapping item

Return type:  [`CalibrationMappingItem`](#ApiClient.CalibrationMappingItem "ApiClient.CalibrationMappingItem")

CreateDebugMappingItem(*ecuKey*, *targetPath*, *variableType=None*, *referenceName=None*, *checkTarget=True*)[¶](#ApiClient.MappingApi.CreateDebugMappingItem "Link to this definition")  
Creates a debug mapping item.

Parameters:  - **ecuKey** (*str*) – Name of the ECU

- **targetPath** (*str*) – Path to the debug variable to be accessed

- **variableType** (*str*) – Type of variable to be mapped (VALUE, VECTOR, MATRIX)

- **referenceName** (*str*) – Name of the mapping item (optional)

- **checkTarget** (*boolean*) – Selects if target path should be checked

Returns:  The just created mapping item

Return type:  [`DebugMappingItem`](#ApiClient.DebugMappingItem "ApiClient.DebugMappingItem")

CreateDebugRegisterMappingItem(*ecuKey*, *targetPath*, *referenceName=None*, *checkTarget=True*)[¶](#ApiClient.MappingApi.CreateDebugRegisterMappingItem "Link to this definition")  
Creates a debug register mapping item.

Parameters:  - **ecuKey** (*str*) – Name of the ECU

- **targetPath** (*str*) – Path to the register variable to be accessed

- **referenceName** (*str*) – Name of the mapping item (optional)

- **checkTarget** (*boolean*) – Selects if target path should be checked

Returns:  The just created mapping item

Return type:  [`DebugRegisterMappingItem`](#ApiClient.DebugRegisterMappingItem "ApiClient.DebugRegisterMappingItem")

CreateDiagDidMappingItem(*systemIdentifier*, *name*, *referenceName=None*, *checkTarget=True*)[¶](#ApiClient.MappingApi.CreateDiagDidMappingItem "Link to this definition")  
Creates DIAG DID mapping item.

Parameters:  - **systemIdentifier** (*str*) – Name of the ECU according to the test configuration

- **name** (*str*) – Name of the DIAG DID signal

- **referenceName** (*str*) – Name of the mapping item

- **checkTarget** (*boolean*) – Selects if target path should be checked

Returns:  The just created mapping item

Return type:  [`DiagDidMappingItem`](#ApiClient.DiagDidMappingItem "ApiClient.DiagDidMappingItem")

CreateDiagFaultMemoryMappingItem(*ecuKey*, *referenceName=None*)[¶](#ApiClient.MappingApi.CreateDiagFaultMemoryMappingItem "Link to this definition")  
Creates a fault memory mapping item.

Parameters:  - **ecuKey** (*str*) – Name of the ECU

- **referenceName** (*str*) – Name of the mapping item (optional)

Returns:  The just created mapping item

Return type:  [`DiagFaultMemoryMappingItem`](#ApiClient.DiagFaultMemoryMappingItem "ApiClient.DiagFaultMemoryMappingItem")

CreateDiagRoutineMappingItem(*systemIdentifier*, *name*, *referenceName=None*, *checkTarget=True*)[¶](#ApiClient.MappingApi.CreateDiagRoutineMappingItem "Link to this definition")  
Creates DIAG RoutineControl mapping item.

Parameters:  - **systemIdentifier** (*str*) – Name of the ECU according to the test configuration

- **name** (*str*) – Name of the DIAG RoutineControl

- **referenceName** (*str*) – Name of the mapping item

- **checkTarget** (*boolean*) – Selects if target path should be checked

Returns:  The just created mapping item

Return type:  [`DiagRoutineMappingItem`](#ApiClient.DiagRoutineMappingItem "ApiClient.DiagRoutineMappingItem")

CreateDiagServiceMappingItem(*systemIdentifier*, *name*, *protocol=0*, *referenceName=None*, *checkTarget=True*)[¶](#ApiClient.MappingApi.CreateDiagServiceMappingItem "Link to this definition")  
Creates a DIAG Service mapping item.

Parameters:  - **systemIdentifier** (*str*) – Name of the ECU according to the test configuration

- **name** (*str*) – Name of the DIAG DID signal

- **protocol** (*int*) – Protocol (0 - UDS, 1 - KWP_2000)

- **referenceName** (*str*) – Name of the mapping item

- **checkTarget** (*bool*) – Selects if target path should be checked

Returns:  The just created mapping item

Return type:  [`DiagServiceMappingItem`](#ApiClient.DiagServiceMappingItem "ApiClient.DiagServiceMappingItem")

CreateEdiabasVariableMappingItem(*ecuKey*, *job*, *referenceName=None*, *checkTarget=True*)[¶](#ApiClient.MappingApi.CreateEdiabasVariableMappingItem "Link to this definition")  
Creates an ediabas variable mapping item.

Parameters:  - **ecuKey** (*str*) – Name of the ECU

- **job** (*str*) – Name of the job

- **referenceName** (*str*) – Name of the mapping item (optional)

- **checkTarget** (*boolean*) – Selects if the target path and the job should be checked (optional)

Returns:  The just created mapping item

Return type:  [`EdiabasVariableMappingItem`](#ApiClient.EdiabasVariableMappingItem "ApiClient.EdiabasVariableMappingItem")

CreateEesPinVariableMappingItem(*systemIdentifier*, *name*, *referenceName=None*, *checkTarget=True*)[¶](#ApiClient.MappingApi.CreateEesPinVariableMappingItem "Link to this definition")  
Creates an ees pin variable mapping item.

Parameters:  - **systemIdentifier** (*str*) – SUT key

- **name** (*str*) – Name of the signal

- **referenceName** (*str*) – Name of the mapping item (optional)

- **checkTarget** (*boolean*) – Selects if target path should be checked (optional)

Returns:  The just created mapping item

Return type:  [`EesPinVariableMappingItem`](#ApiClient.EesPinVariableMappingItem "ApiClient.EesPinVariableMappingItem")

CreateEnvSimMappingItem(*systemIdentifier*, *targetPath*, *variableType=None*, *isSignal=False*, *referenceName=None*, *checkTarget=True*)[¶](#ApiClient.MappingApi.CreateEnvSimMappingItem "Link to this definition")  
Creates a mapping item of the desired variable type pointing at a certain envsim variable. The envsim has to be loaded in order to create a envsim mapping item.

Parameters:  - **systemIdentifier** (*str*) – Name of system according to the test configuration, e.g. “Plant model”

- **targetPath** (*str*) – Path to the model variable to be accessed, e.g. “Model Root/varName”.

- **variableType** (*str*) – Type of variable to be mapped (VALUE, VECTOR, MATRIX)

- **isSignal** (*boolean*) – Selects if the mapping item should point to a model signal instead of variable

- **referenceName** (*str*) – Name of the mapping item

- **checkTarget** (*boolean*) – Selects if target path should be checked

Returns:  The just created mapping item

Return type:  [`EnvSimMappingItem`](#ApiClient.EnvSimMappingItem "ApiClient.EnvSimMappingItem")

CreateGenericMappingItem(*variableType=None*, *referenceName=None*)[¶](#ApiClient.MappingApi.CreateGenericMappingItem "Link to this definition")  
Creates a generic mapping item of the desired variable type.

Parameters:  - **variableType** (*str*) – Type of variable to be mapped (VALUE, VECTOR, CURVE, MATRIX, MAP, IMAGE, AUDIO, JOB, PACKAGE)

- **referenceName** (*str*) – Name of the mapping item

Returns:  The just created mapping item

Return type:  [`MappingItem`](#ApiClient.MappingItem "ApiClient.MappingItem")

CreateImageMappingItem(*systemIdentifier*, *targetPath*, *maskPath=''*, *referenceName=None*, *checkTarget=True*)[¶](#ApiClient.MappingApi.CreateImageMappingItem "Link to this definition")  
Creates a mapping item pointing at a certain image variable.

Parameters:  - **systemIdentifier** (*str*) – Name of system according to the test configuration, e.g. “CAM”

- **targetPath** (*str*) – Path to the image variable to be accessed, e.g. “Image” to read the whole image. To access a mask in a subfolder, the path to that folder must also be specified here, e.g. “Image/mymasks/moremasks/”. The actual name of the mask (and submask) however is specified in the parameter `maskPath`.

- **maskPath** (*str*) – The name of the mask, submask and index to use, e.g. “MyMask[1, 1]/icon” would refer to the submask “icon” of index [1, 1] of the mask “MyMask”.

- **referenceName** (*str*) – Name of the mapping item

- **checkTarget** (*boolean*) – Selects if target path should be checked

Returns:  The just created mapping item

Return type:  [`ImageMappingItem`](#ApiClient.ImageMappingItem "ApiClient.ImageMappingItem")

CreateJobMappingItem(*toolId*, *jobName*, *portId=None*, *checkTarget=True*)[¶](#ApiClient.MappingApi.CreateJobMappingItem "Link to this definition")  
Creates a tool job or port job mapping item.

Parameters:  - **toolId** (*str*) – Name of the used tool

- **jobName** (*str*) – Name of the job

- **portId** (*str*) – Name of the port

- **checkTarget** (*boolean*) – Selects if target path should be checked

Returns:  The just created mapping item

Return type:  [`MappingItem`](#ApiClient.MappingItem "ApiClient.MappingItem")

CreateLogFilterMessageMappingItem(*ecuKey*, *messageName*, *referenceName=None*, *checkTarget=True*)[¶](#ApiClient.MappingApi.CreateLogFilterMessageMappingItem "Link to this definition")  
Creates a DLT log filter mapping item.

Parameters:  - **ecuKey** (*str*) – name of the ECU for which the filter has been loaded

- **messageName** (*str*) – name of the message filter

- **referenceName** (*str*) – Name of the mapping item

- **checkTarget** (*boolean*) – Selects if target path should be checked

Returns:  The just created mapping item

Return type:  [`LogFilterMessageMappingItem`](#ApiClient.LogFilterMessageMappingItem "ApiClient.LogFilterMessageMappingItem")

CreateLoggingArgumentMappingItem(*systemIdentifier*, *messageName*, *argumentName*, *referenceName=None*, *checkTarget=True*)[¶](#ApiClient.MappingApi.CreateLoggingArgumentMappingItem "Link to this definition")  
Creates a logging argument mapping item.

Parameters:  - **systemIdentifier** (*str*) – Name of logging system according to the test configuration

- **messageName** (*str*) – Name of the message containing the argument

- **argumentName** (*str*) – Name of the message argument

- **referenceName** (*str*) – Name of the mapping item

- **checkTarget** (*boolean*) – Selects if target path should be checked

Returns:  The just created mapping item

Return type:  [`LoggingArgumentMappingItem`](#ApiClient.LoggingArgumentMappingItem "ApiClient.LoggingArgumentMappingItem")

CreateMappingItem(*systemIdentifier*, *targetPath*, *referenceName=None*)[¶](#ApiClient.MappingApi.CreateMappingItem "Link to this definition")  
Creates a mapping item with automatically determined type.

The desired mapping target needs to exist in the currently loaded/activated configuration!

Parameters:  - **systemIdentifier** (*str*) – Name of system according to the test configuration

- **targetPath** (*str*) –

  Name of bus, model, calibration or measure variable to be accessed (Needs indices if datatype is VECTOR-ELEMENT label[idx_X] or if datatype is MATRIX-ELEMENT label[idx_X][idx_Y])

  Bus signals need a target path of the following form: “\<nodeName\>/\<frameName\>/\<pduName\>/\<signalName\>” Note: \<nodeName\>, \<frameName\> and \<pduName\> are optional, that means ///\<signalName\> is also valid. Logging arguments need a target path of the form: “/\<messageName\>/\<argumentName\>/”

- **referenceName** (*str*) – Name of the mapping item

Returns:  The just created mapping item

Return type:  [`MappingItem`](#ApiClient.MappingItem "ApiClient.MappingItem")

CreateMeasurementMappingItem(*systemIdentifier*, *targetPath*, *variableType=None*, *referenceName=None*, *xElement=None*, *yElement=None*, *zElement=None*, *checkTarget=True*)[¶](#ApiClient.MappingApi.CreateMeasurementMappingItem "Link to this definition")  
Creates a measurement mapping item of the desired variable type.

Parameters:  - **systemIdentifier** (*str*) – Name of ECU according to the test configuration

- **targetPath** (*str*) – Name of measurement variable to be accessed

- **variableType** (*str*) – Type of variable to be mapped (VALUE, VECTOR, MATRIX, VECTOR-ELEMENT, MATRIX-ELEMENT)

- **referenceName** (*str*) – Name of the mapping item

- **xElement** (*integer*) – Index on x axis if single element of VECTOR or MATRIX should be accessed

- **yElement** (*integer*) – Index on y axis if single element of MATRIX should be accessed

- **zElement** (*integer*) – Index on z axis if single element of MATRIX should be accessed

- **checkTarget** (*boolean*) – Selects if target path should be checked

Returns:  The just created mapping item

Return type:  [`MeasureMappingItem`](#ApiClient.MeasureMappingItem "ApiClient.MeasureMappingItem")

CreateModelMappingItem(*systemIdentifier*, *targetPath*, *variableType=None*, *isSignal=False*, *referenceName=None*, *checkTarget=True*)[¶](#ApiClient.MappingApi.CreateModelMappingItem "Link to this definition")  
Creates a mapping item of the desired variable type pointing at a certain model variable. The model has to be loaded in order to create a model mapping item.

Parameters:  - **systemIdentifier** (*str*) – Name of system according to the test configuration, e.g. “Plant model”

- **targetPath** (*str*) – Path to the model variable to be accessed, e.g. “Model Root/varName”.

- **variableType** (*str*) – Type of variable to be mapped (VALUE, VECTOR, MATRIX)

- **isSignal** (*boolean*) – Selects if the mapping item should point to a model signal instead of variable

- **referenceName** (*str*) – Name of the mapping item

- **checkTarget** (*boolean*) – Selects if target path should be checked

Returns:  The just created mapping item

Return type:  [`ModelMappingItem`](#ApiClient.ModelMappingItem "ApiClient.ModelMappingItem")

CreatePackageMappingItem(*pkgPath*, *referenceName=None*, *namespace=None*, *checkTarget=True*)[¶](#ApiClient.MappingApi.CreatePackageMappingItem "Link to this definition")  
Creates a package mapping item referencing the given package path. For example, CreatePackageMappingItem(‘MyPackage.pkg’) results in a reference to ‘\<workspace.packages\>/MyPackage.pkg’.

Parameters:  - **pkgPath** (*str*) – Path to the referenced package, either absolute or relative to the packages directory of the current workspace or given namespace, e.g. ‘MyPackage.pkg’. An absolute path located in the current workspace will also be resolved to a relative workspace reference.

- **referenceName** (*str*) – Name of the mapping item

- **namespace** (*str*) – Identifier of the workspace to which a relative pkgPath is resolved. If not present or None, the namespace is determined automatically. It is also possible to reference a library workspace using its namespace. A relative pkgPath is resolved relative to the packages directory of the given namespace. For example, the namespace parameter ‘myLibrary’ results in ‘\<libraries.myLibrary.packages\>/MyPackage.pkg’.

- **checkTarget** (*boolean*) – Selects if target path should be checked

Returns:  The just created mapping item

Return type:  [`PackageMappingItem`](#ApiClient.PackageMappingItem "ApiClient.PackageMappingItem")

CreatePortMappingItem(*systemIdentifier*, *portType*, *referenceName=None*, *checkTarget=True*)[¶](#ApiClient.MappingApi.CreatePortMappingItem "Link to this definition")  
Creates a port mapping item.

Parameters:  - **systemIdentifier** (*str*) – SUT key

- **portType** (*str*) – type of the port - one of Bus, Service, or Logging

- **referenceName** (*str*) – Name of the mapping item (optional)

- **checkTarget** (*boolean*) – Selects if target path should be checked (optional)

Returns:  The just created mapping item

Return type:  [`PortMappingItem`](#ApiClient.PortMappingItem "ApiClient.PortMappingItem")

CreateRunningValueMappingItem(*systemIdentifier*, *targetPath*, *referenceName=None*, *checkTarget=True*)[¶](#ApiClient.MappingApi.CreateRunningValueMappingItem "Link to this definition")  
Creates a running value mapping item of the desired variable type.

Parameters:  - **systemIdentifier** (*str*) – Name of ECU according to the test configuration

- **targetPath** (*str*) – Name of running value variable to be accessed

- **referenceName** (*str*) – Name of the mapping item

- **checkTarget** (*boolean*) – Selects if target path should be checked

Returns:  The just created mapping item

Return type:  [`RunningValueMappingItem`](#ApiClient.RunningValueMappingItem "ApiClient.RunningValueMappingItem")

CreateServiceEventLeafMappingItem(*systemIdentifier*, *ecuName*, *serviceName*, *eventName*, *variablePath*, *eventgroupName=''*, *fieldName=''*, *referenceName=None*, *checkTarget=True*)[¶](#ApiClient.MappingApi.CreateServiceEventLeafMappingItem "Link to this definition")  
Creates a service event leaf mapping item.

Parameters:  - **systemIdentifier** (*str*) – SUT key

- **ecuName** (*str*) – Name of the ECU that provides the service

- **serviceName** (*str*) – Name of the service that provides the event

- **eventName** (*str*) – Name of the event

- **variablePath** (*str*) – Path to the return leaf node

- **eventgroupName** (*str*) – Name of the event group that contains the event (optional)

- **fieldName** (*str*) – Name of the field to which the event belongs (optional)

- **referenceName** (*str*) – Name of the mapping item (optional)

- **checkTarget** (*boolean*) – Selects if target path should be checked (optional)

Returns:  The just created mapping item

Return type:  [`ServiceEventLeafMappingItem`](#ApiClient.ServiceEventLeafMappingItem "ApiClient.ServiceEventLeafMappingItem")

CreateServiceMappingItem(*systemIdentifier*, *ecuName*, *serviceName*, *eventOrMethodName*, *fieldName=''*, *eventGroupName=''*, *referenceName=None*, *checkTarget=True*)[¶](#ApiClient.MappingApi.CreateServiceMappingItem "Link to this definition")  
Creates a service field event mapping item.

Parameters:  - **systemIdentifier** (*str*) – SUT key

- **ecuName** (*str*) – Name of the ECU that provides the service

- **serviceName** (*str*) – Name of the service that provides the event

- **eventOrMethodName** (*str*) – Name of the event or the method

- **fieldName** (*str*) – Name of the field (optional)

- **eventGroupName** (*str*) – Name of the event group that contains the event (optional)

- **referenceName** (*str*) – Name of the mapping item (optional)

- **checkTarget** (*boolean*) – Selects if target path should be checked (optional)

Returns:  The just created mapping item

Return type:  [`ServiceMappingItem`](#ApiClient.ServiceMappingItem "ApiClient.ServiceMappingItem")

CreateServiceMethodParameterMappingItem(*systemIdentifier*, *ecuName*, *serviceName*, *methodName*, *variablePath*, *eventgroupName=''*, *fieldName=''*, *referenceName=None*, *checkTarget=True*)[¶](#ApiClient.MappingApi.CreateServiceMethodParameterMappingItem "Link to this definition")  
Creates a service method parameter mapping item.

Parameters:  - **systemIdentifier** (*str*) – SUT key

- **ecuName** (*str*) – Name of the ECU that provides the service

- **serviceName** (*str*) – Name of the service that provides the method

- **methodName** (*str*) – Name of the method

- **variablePath** (*str*) – Path to the parameter leaf node

- **eventgroupName** (*str*) – Name of the event group that contains the method (optional)

- **fieldName** (*str*) – Name of the field to which the method belongs (optional)

- **referenceName** (*str*) – Name of the mapping item (optional)

- **checkTarget** (*boolean*) – Selects if target path should be checked (optional)

Returns:  The just created mapping item

Return type:  [`ServiceMethodParameterMappingItem`](#ApiClient.ServiceMethodParameterMappingItem "ApiClient.ServiceMethodParameterMappingItem")

CreateServiceMethodReturnMappingItem(*systemIdentifier*, *ecuName*, *serviceName*, *methodName*, *variablePath*, *eventgroupName=''*, *fieldName=''*, *referenceName=None*, *checkTarget=True*)[¶](#ApiClient.MappingApi.CreateServiceMethodReturnMappingItem "Link to this definition")  
Creates a service method return mapping item.

Parameters:  - **systemIdentifier** (*str*) – SUT key

- **ecuName** (*str*) – Name of the ECU that provides the service

- **serviceName** (*str*) – Name of the service that provides the method

- **methodName** (*str*) – Name of the method

- **variablePath** (*str*) – Path to the return leaf node

- **eventgroupName** (*str*) – Name of the event group that contains the method (optional)

- **fieldName** (*str*) – Name of the field to which the method belongs (optional)

- **referenceName** (*str*) – Name of the mapping item (optional)

- **checkTarget** (*boolean*) – Selects if target path should be checked (optional)

Returns:  The just created mapping item

Return type:  [`ServiceMethodReturnMappingItem`](#ApiClient.ServiceMethodReturnMappingItem "ApiClient.ServiceMethodReturnMappingItem")

CreateTraceFileMappingItem(*targetPath*, *referenceName=None*, *systemIdentifier=None*)[¶](#ApiClient.MappingApi.CreateTraceFileMappingItem "Link to this definition")  
Creates a trace file mapping item pointing at a certain trace file signal.

Parameters:  - **targetPath** (*str*) – Path to the trace file signal to be accessed

- **referenceName** (*str*) – Name of the mapping item

- **systemIdentifier** (*str*) – Name of system (relevant for automatically assignment to a signal group)

Returns:  The just created mapping item

Return type:  [`MappingItem`](#ApiClient.MappingItem "ApiClient.MappingItem")

## AnalysisPackageMappingItem[¶](#analysispackagemappingitem "Link to this heading")

*class* AnalysisPackageMappingItem[¶](#ApiClient.AnalysisPackageMappingItem "Link to this definition")  
Base class

[`MappingItem`](#ApiClient.MappingItem "ApiClient.MappingItem")

Returned by

- [`MappingApi.CreateAnalysisPackageMappingItem`](#ApiClient.MappingApi.CreateAnalysisPackageMappingItem "ApiClient.MappingApi.CreateAnalysisPackageMappingItem")

Clone()[¶](#ApiClient.AnalysisPackageMappingItem.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`AnalysisPackageMappingItem`](#ApiClient.AnalysisPackageMappingItem "ApiClient.AnalysisPackageMappingItem")

GetAccessType()[¶](#ApiClient.AnalysisPackageMappingItem.GetAccessType "Link to this definition")  
Returns a string identifying the mapping item’s type. (such as MODEL, BUS, MEASUREMENT, …)

Returns:  access type

Return type:  str

GetCategory()[¶](#ApiClient.AnalysisPackageMappingItem.GetCategory "Link to this definition")  
Returns the category

Returns:  Category

Return type:  str

GetDescription()[¶](#ApiClient.AnalysisPackageMappingItem.GetDescription "Link to this definition")  
Returns the description

Returns:  Description

Return type:  str

GetDisplayedType()[¶](#ApiClient.AnalysisPackageMappingItem.GetDisplayedType "Link to this definition")  
Returns a “nice” representation of the type as displayed in the “type” column of the mapping panel

Returns:  the displayed mapping type

Return type:  str

GetReferenceName()[¶](#ApiClient.AnalysisPackageMappingItem.GetReferenceName "Link to this definition")  
Returns the reference name of the mapping.

Returns:  The reference name of the mapping

Return type:  str

GetSubMapping()[¶](#ApiClient.AnalysisPackageMappingItem.GetSubMapping "Link to this definition")  
Returns contained Mapping or None if item does not support sub-mappings.

Returns:  Mapping with all submappings of the mapping item

Return type:  [`Mapping`](#ApiClient.Mapping "ApiClient.Mapping")

GetSystemIdentifier()[¶](#ApiClient.AnalysisPackageMappingItem.GetSystemIdentifier "Link to this definition")  
Returns the system identifier providing the currently mapped test quantity

Returns:  system identifier

Return type:  str

GetTargetPath()[¶](#ApiClient.AnalysisPackageMappingItem.GetTargetPath "Link to this definition")  
Returns the path this mapping item is currently pointing at

Returns:  complete path to the destination test quantity

Return type:  str

GetVariableType()[¶](#ApiClient.AnalysisPackageMappingItem.GetVariableType "Link to this definition")  
Returns the type of the target variable or None if target has no type.

Returns:  The type of the target variable. (e.g. VALUE, MATRIX, CURVE, …)

Return type:  str

IsAutogenerated()[¶](#ApiClient.AnalysisPackageMappingItem.IsAutogenerated "Link to this definition")  
Returns whether the mapping item is autogenerated.

Returns:  True, if autogenerated flag is set, else False

Return type:  boolean

SetCategory(*category*)[¶](#ApiClient.AnalysisPackageMappingItem.SetCategory "Link to this definition")  
Sets the category

Parameters:  **category** (*str*) – The new category to be used

SetDescription(*description*)[¶](#ApiClient.AnalysisPackageMappingItem.SetDescription "Link to this definition")  
Sets the description

Parameters:  **description** (*str*) – The new description to be used

SetReferenceName(*name*)[¶](#ApiClient.AnalysisPackageMappingItem.SetReferenceName "Link to this definition")  
Sets the reference name of the mapping.

Parameters:  **name** (*str*) – The reference name of the mapping

## Mapping[¶](#mapping "Link to this heading")

*class* Mapping[¶](#ApiClient.Mapping "Link to this definition")  
Returned by

- [`AnalysisJob.GetMapping`](AnalysisJobApi.md#ApiClient.AnalysisJob.GetMapping "ApiClient.AnalysisJob.GetMapping")

- [`AnalysisPackageMappingItem.GetSubMapping`](#ApiClient.AnalysisPackageMappingItem.GetSubMapping "ApiClient.AnalysisPackageMappingItem.GetSubMapping")

- [`AudioChannelMappingItem.GetSubMapping`](#ApiClient.AudioChannelMappingItem.GetSubMapping "ApiClient.AudioChannelMappingItem.GetSubMapping")

- [`AudioDeviceMappingItem.GetSubMapping`](#ApiClient.AudioDeviceMappingItem.GetSubMapping "ApiClient.AudioDeviceMappingItem.GetSubMapping")

- [`BusMonitoringMappingItem.GetSubMapping`](#ApiClient.BusMonitoringMappingItem.GetSubMapping "ApiClient.BusMonitoringMappingItem.GetSubMapping")

- [`BusSignalGroupMappingItem.GetSubMapping`](#ApiClient.BusSignalGroupMappingItem.GetSubMapping "ApiClient.BusSignalGroupMappingItem.GetSubMapping")

- [`BusSignalMappingItem.GetSubMapping`](#ApiClient.BusSignalMappingItem.GetSubMapping "ApiClient.BusSignalMappingItem.GetSubMapping")

- [`CalibrationMappingItem.GetSubMapping`](#ApiClient.CalibrationMappingItem.GetSubMapping "ApiClient.CalibrationMappingItem.GetSubMapping")

- [`CallableMappingItem.GetSubMapping`](#ApiClient.CallableMappingItem.GetSubMapping "ApiClient.CallableMappingItem.GetSubMapping")

- [`DebugMappingItem.GetSubMapping`](#ApiClient.DebugMappingItem.GetSubMapping "ApiClient.DebugMappingItem.GetSubMapping")

- [`DebugRegisterMappingItem.GetSubMapping`](#ApiClient.DebugRegisterMappingItem.GetSubMapping "ApiClient.DebugRegisterMappingItem.GetSubMapping")

- [`DiagDidMappingItem.GetSubMapping`](#ApiClient.DiagDidMappingItem.GetSubMapping "ApiClient.DiagDidMappingItem.GetSubMapping")

- [`DiagFaultMemoryMappingItem.GetSubMapping`](#ApiClient.DiagFaultMemoryMappingItem.GetSubMapping "ApiClient.DiagFaultMemoryMappingItem.GetSubMapping")

- [`DiagRoutineMappingItem.GetSubMapping`](#ApiClient.DiagRoutineMappingItem.GetSubMapping "ApiClient.DiagRoutineMappingItem.GetSubMapping")

- [`DiagServiceMappingItem.GetSubMapping`](#ApiClient.DiagServiceMappingItem.GetSubMapping "ApiClient.DiagServiceMappingItem.GetSubMapping")

- [`EdiabasVariableMappingItem.GetSubMapping`](#ApiClient.EdiabasVariableMappingItem.GetSubMapping "ApiClient.EdiabasVariableMappingItem.GetSubMapping")

- [`EesPinVariableMappingItem.GetSubMapping`](#ApiClient.EesPinVariableMappingItem.GetSubMapping "ApiClient.EesPinVariableMappingItem.GetSubMapping")

- [`EnvSimMappingItem.GetSubMapping`](#ApiClient.EnvSimMappingItem.GetSubMapping "ApiClient.EnvSimMappingItem.GetSubMapping")

- [`GenericAudioMappingItem.GetSubMapping`](#ApiClient.GenericAudioMappingItem.GetSubMapping "ApiClient.GenericAudioMappingItem.GetSubMapping")

- [`GenericImageMappingItem.GetSubMapping`](#ApiClient.GenericImageMappingItem.GetSubMapping "ApiClient.GenericImageMappingItem.GetSubMapping")

- [`GenericMappingItem.GetSubMapping`](#ApiClient.GenericMappingItem.GetSubMapping "ApiClient.GenericMappingItem.GetSubMapping")

- [`GenericPackageMappingItem.GetSubMapping`](#ApiClient.GenericPackageMappingItem.GetSubMapping "ApiClient.GenericPackageMappingItem.GetSubMapping")

- [`ImageMappingItem.GetSubMapping`](#ApiClient.ImageMappingItem.GetSubMapping "ApiClient.ImageMappingItem.GetSubMapping")

- [`LogFilterMessageMappingItem.GetSubMapping`](#ApiClient.LogFilterMessageMappingItem.GetSubMapping "ApiClient.LogFilterMessageMappingItem.GetSubMapping")

- [`LoggingArgumentMappingItem.GetSubMapping`](#ApiClient.LoggingArgumentMappingItem.GetSubMapping "ApiClient.LoggingArgumentMappingItem.GetSubMapping")

- [`MappingItem.GetSubMapping`](#ApiClient.MappingItem.GetSubMapping "ApiClient.MappingItem.GetSubMapping")

- [`MeasureMappingItem.GetSubMapping`](#ApiClient.MeasureMappingItem.GetSubMapping "ApiClient.MeasureMappingItem.GetSubMapping")

- [`ModelMappingItem.GetSubMapping`](#ApiClient.ModelMappingItem.GetSubMapping "ApiClient.ModelMappingItem.GetSubMapping")

- [`PackageMappingItem.GetSubMapping`](#ApiClient.PackageMappingItem.GetSubMapping "ApiClient.PackageMappingItem.GetSubMapping")

- [`ParameterSetMapping.CreateAlternativeMapping`](ComponentApi.md#ApiClient.ParameterSetMapping.CreateAlternativeMapping "ApiClient.ParameterSetMapping.CreateAlternativeMapping")

- [`ParameterSetMapping.GetAlternativeMapping`](ComponentApi.md#ApiClient.ParameterSetMapping.GetAlternativeMapping "ApiClient.ParameterSetMapping.GetAlternativeMapping")

- [`ParameterSetMapping.GetMappingFromPackage`](ComponentApi.md#ApiClient.ParameterSetMapping.GetMappingFromPackage "ApiClient.ParameterSetMapping.GetMappingFromPackage")

- [`PortMappingItem.GetSubMapping`](#ApiClient.PortMappingItem.GetSubMapping "ApiClient.PortMappingItem.GetSubMapping")

- [`RunningValueMappingItem.GetSubMapping`](#ApiClient.RunningValueMappingItem.GetSubMapping "ApiClient.RunningValueMappingItem.GetSubMapping")

- [`ServiceEventLeafMappingItem.GetSubMapping`](#ApiClient.ServiceEventLeafMappingItem.GetSubMapping "ApiClient.ServiceEventLeafMappingItem.GetSubMapping")

- [`ServiceMappingItem.GetSubMapping`](#ApiClient.ServiceMappingItem.GetSubMapping "ApiClient.ServiceMappingItem.GetSubMapping")

- [`ServiceMethodParameterMappingItem.GetSubMapping`](#ApiClient.ServiceMethodParameterMappingItem.GetSubMapping "ApiClient.ServiceMethodParameterMappingItem.GetSubMapping")

- [`ServiceMethodReturnMappingItem.GetSubMapping`](#ApiClient.ServiceMethodReturnMappingItem.GetSubMapping "ApiClient.ServiceMethodReturnMappingItem.GetSubMapping")

Subclasses

- [`GlobalMapping`](GlobalMappingApi.md#ApiClient.GlobalMapping "ApiClient.GlobalMapping")

- [`LocalMapping`](PackageApi.md#ApiClient.LocalMapping "ApiClient.LocalMapping")

AddItem(*mappingItem*)[¶](#ApiClient.Mapping.AddItem "Link to this definition")  
Adds a mapping item to the mapping.

Parameters:  **mappingItem** ([`MappingItem`](#ApiClient.MappingItem "ApiClient.MappingItem")) – The mapping item to be added

Clone()[¶](#ApiClient.Mapping.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`Mapping`](#ApiClient.Mapping "ApiClient.Mapping")

GetItemByName(*name*)[¶](#ApiClient.Mapping.GetItemByName "Link to this definition")  
Searches the mapping for the mapping item by its name and returns it if existing.

Parameters:  **name** (*str*) – The name of the mapping item to be searched for

Returns:  mapping item with the given name or None if no such mapping item exists

Return type:  [`MappingItem`](#ApiClient.MappingItem "ApiClient.MappingItem")

GetItems()[¶](#ApiClient.Mapping.GetItems "Link to this definition")  
Returns a list of all the mapping items of the mapping.

Returns:  List of all the mapping items of the mapping.

Return type:  list[[`MappingItem`](#ApiClient.MappingItem "ApiClient.MappingItem")]

GetItemsByTargetPath(*targetPath*)[¶](#ApiClient.Mapping.GetItemsByTargetPath "Link to this definition")  
Searches the mapping for all mapping items that have the target path and returns them if existing.

Parameters:  **targetPath** (*str*) – The target path of the mapping items to be searched for

Returns:  List of mapping items that have the target path.

Return type:  list[[`MappingItem`](#ApiClient.MappingItem "ApiClient.MappingItem")]

HasItem(*mappingItem*)[¶](#ApiClient.Mapping.HasItem "Link to this definition")  
Checks whether the given mapping item belongs to the mapping.

Parameters:  **mappingItem** ([`MappingItem`](#ApiClient.MappingItem "ApiClient.MappingItem")) – The mapping item to be checked

Returns:  True if the given mapping item belongs to the mapping.

Return type:  boolean

RemoveItemByName(*name*)[¶](#ApiClient.Mapping.RemoveItemByName "Link to this definition")  
Removes a mapping item from the mapping.

Parameters:  **name** (*str*) – The name of the mapping item to be removed

ReplaceItem(*mappingItem*)[¶](#ApiClient.Mapping.ReplaceItem "Link to this definition")  
Replaces a mapping item from the mapping

Parameters:  **mappingItem** ([`MappingItem`](#ApiClient.MappingItem "ApiClient.MappingItem")) – The new mapping item to replace an existing one of the same name

## MappingItem[¶](#mappingitem "Link to this heading")

*class* MappingItem[¶](#ApiClient.MappingItem "Link to this definition")  
Returned by

- [`AutoAssignSignalGroup.GetMappingItems`](PackageApi.md#ApiClient.AutoAssignSignalGroup.GetMappingItems "ApiClient.AutoAssignSignalGroup.GetMappingItems")

- [`GlobalMapping.GetItemByName`](GlobalMappingApi.md#ApiClient.GlobalMapping.GetItemByName "ApiClient.GlobalMapping.GetItemByName")

- [`GlobalMapping.GetItems`](GlobalMappingApi.md#ApiClient.GlobalMapping.GetItems "ApiClient.GlobalMapping.GetItems")

- [`GlobalMapping.GetItemsByTargetPath`](GlobalMappingApi.md#ApiClient.GlobalMapping.GetItemsByTargetPath "ApiClient.GlobalMapping.GetItemsByTargetPath")

- [`LocalMapping.GetItemByName`](PackageApi.md#ApiClient.LocalMapping.GetItemByName "ApiClient.LocalMapping.GetItemByName")

- [`LocalMapping.GetItems`](PackageApi.md#ApiClient.LocalMapping.GetItems "ApiClient.LocalMapping.GetItems")

- [`LocalMapping.GetItemsByTargetPath`](PackageApi.md#ApiClient.LocalMapping.GetItemsByTargetPath "ApiClient.LocalMapping.GetItemsByTargetPath")

- [`Mapping.GetItemByName`](#ApiClient.Mapping.GetItemByName "ApiClient.Mapping.GetItemByName")

- [`Mapping.GetItems`](#ApiClient.Mapping.GetItems "ApiClient.Mapping.GetItems")

- [`Mapping.GetItemsByTargetPath`](#ApiClient.Mapping.GetItemsByTargetPath "ApiClient.Mapping.GetItemsByTargetPath")

- [`MappingApi.CreateGenericMappingItem`](#ApiClient.MappingApi.CreateGenericMappingItem "ApiClient.MappingApi.CreateGenericMappingItem")

- [`MappingApi.CreateJobMappingItem`](#ApiClient.MappingApi.CreateJobMappingItem "ApiClient.MappingApi.CreateJobMappingItem")

- [`MappingApi.CreateMappingItem`](#ApiClient.MappingApi.CreateMappingItem "ApiClient.MappingApi.CreateMappingItem")

- [`MappingApi.CreateTraceFileMappingItem`](#ApiClient.MappingApi.CreateTraceFileMappingItem "ApiClient.MappingApi.CreateTraceFileMappingItem")

- [`SignalGroup.GetMappingItems`](SignalRecordingApi.md#ApiClient.SignalGroup.GetMappingItems "ApiClient.SignalGroup.GetMappingItems")

- [`SignalGroupBase.GetMappingItems`](SignalRecordingApi.md#ApiClient.SignalGroupBase.GetMappingItems "ApiClient.SignalGroupBase.GetMappingItems")

Subclasses

- [`AnalysisPackageMappingItem`](#ApiClient.AnalysisPackageMappingItem "ApiClient.AnalysisPackageMappingItem")

- [`AudioChannelMappingItem`](#ApiClient.AudioChannelMappingItem "ApiClient.AudioChannelMappingItem")

- [`AudioDeviceMappingItem`](#ApiClient.AudioDeviceMappingItem "ApiClient.AudioDeviceMappingItem")

- [`BusMonitoringMappingItem`](#ApiClient.BusMonitoringMappingItem "ApiClient.BusMonitoringMappingItem")

- [`BusSignalGroupMappingItem`](#ApiClient.BusSignalGroupMappingItem "ApiClient.BusSignalGroupMappingItem")

- [`BusSignalMappingItem`](#ApiClient.BusSignalMappingItem "ApiClient.BusSignalMappingItem")

- [`CalibrationMappingItem`](#ApiClient.CalibrationMappingItem "ApiClient.CalibrationMappingItem")

- [`CallableMappingItem`](#ApiClient.CallableMappingItem "ApiClient.CallableMappingItem")

- [`DebugMappingItem`](#ApiClient.DebugMappingItem "ApiClient.DebugMappingItem")

- [`DebugRegisterMappingItem`](#ApiClient.DebugRegisterMappingItem "ApiClient.DebugRegisterMappingItem")

- [`DiagDidMappingItem`](#ApiClient.DiagDidMappingItem "ApiClient.DiagDidMappingItem")

- [`DiagFaultMemoryMappingItem`](#ApiClient.DiagFaultMemoryMappingItem "ApiClient.DiagFaultMemoryMappingItem")

- [`DiagRoutineMappingItem`](#ApiClient.DiagRoutineMappingItem "ApiClient.DiagRoutineMappingItem")

- [`DiagServiceMappingItem`](#ApiClient.DiagServiceMappingItem "ApiClient.DiagServiceMappingItem")

- [`EdiabasVariableMappingItem`](#ApiClient.EdiabasVariableMappingItem "ApiClient.EdiabasVariableMappingItem")

- [`EesPinVariableMappingItem`](#ApiClient.EesPinVariableMappingItem "ApiClient.EesPinVariableMappingItem")

- [`EnvSimMappingItem`](#ApiClient.EnvSimMappingItem "ApiClient.EnvSimMappingItem")

- [`GenericAudioMappingItem`](#ApiClient.GenericAudioMappingItem "ApiClient.GenericAudioMappingItem")

- [`GenericImageMappingItem`](#ApiClient.GenericImageMappingItem "ApiClient.GenericImageMappingItem")

- [`GenericMappingItem`](#ApiClient.GenericMappingItem "ApiClient.GenericMappingItem")

- [`GenericPackageMappingItem`](#ApiClient.GenericPackageMappingItem "ApiClient.GenericPackageMappingItem")

- [`ImageMappingItem`](#ApiClient.ImageMappingItem "ApiClient.ImageMappingItem")

- [`LogFilterMessageMappingItem`](#ApiClient.LogFilterMessageMappingItem "ApiClient.LogFilterMessageMappingItem")

- [`LoggingArgumentMappingItem`](#ApiClient.LoggingArgumentMappingItem "ApiClient.LoggingArgumentMappingItem")

- [`MeasureMappingItem`](#ApiClient.MeasureMappingItem "ApiClient.MeasureMappingItem")

- [`ModelMappingItem`](#ApiClient.ModelMappingItem "ApiClient.ModelMappingItem")

- [`PackageMappingItem`](#ApiClient.PackageMappingItem "ApiClient.PackageMappingItem")

- [`PortMappingItem`](#ApiClient.PortMappingItem "ApiClient.PortMappingItem")

- [`RunningValueMappingItem`](#ApiClient.RunningValueMappingItem "ApiClient.RunningValueMappingItem")

- [`ServiceEventLeafMappingItem`](#ApiClient.ServiceEventLeafMappingItem "ApiClient.ServiceEventLeafMappingItem")

- [`ServiceMappingItem`](#ApiClient.ServiceMappingItem "ApiClient.ServiceMappingItem")

- [`ServiceMethodParameterMappingItem`](#ApiClient.ServiceMethodParameterMappingItem "ApiClient.ServiceMethodParameterMappingItem")

- [`ServiceMethodReturnMappingItem`](#ApiClient.ServiceMethodReturnMappingItem "ApiClient.ServiceMethodReturnMappingItem")

Clone()[¶](#ApiClient.MappingItem.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`MappingItem`](#ApiClient.MappingItem "ApiClient.MappingItem")

GetAccessType()[¶](#ApiClient.MappingItem.GetAccessType "Link to this definition")  
Returns a string identifying the mapping item’s type. (such as MODEL, BUS, MEASUREMENT, …)

Returns:  access type

Return type:  str

GetCategory()[¶](#ApiClient.MappingItem.GetCategory "Link to this definition")  
Returns the category

Returns:  Category

Return type:  str

GetDescription()[¶](#ApiClient.MappingItem.GetDescription "Link to this definition")  
Returns the description

Returns:  Description

Return type:  str

GetDisplayedType()[¶](#ApiClient.MappingItem.GetDisplayedType "Link to this definition")  
Returns a “nice” representation of the type as displayed in the “type” column of the mapping panel

Returns:  the displayed mapping type

Return type:  str

GetReferenceName()[¶](#ApiClient.MappingItem.GetReferenceName "Link to this definition")  
Returns the reference name of the mapping.

Returns:  The reference name of the mapping

Return type:  str

GetSubMapping()[¶](#ApiClient.MappingItem.GetSubMapping "Link to this definition")  
Returns contained Mapping or None if item does not support sub-mappings.

Returns:  Mapping with all submappings of the mapping item

Return type:  [`Mapping`](#ApiClient.Mapping "ApiClient.Mapping")

GetSystemIdentifier()[¶](#ApiClient.MappingItem.GetSystemIdentifier "Link to this definition")  
Returns the system identifier providing the currently mapped test quantity

Returns:  system identifier

Return type:  str

GetTargetPath()[¶](#ApiClient.MappingItem.GetTargetPath "Link to this definition")  
Returns the path this mapping item is currently pointing at

Returns:  complete path to the destination test quantity

Return type:  str

GetVariableType()[¶](#ApiClient.MappingItem.GetVariableType "Link to this definition")  
Returns the type of the target variable or None if target has no type.

Returns:  The type of the target variable. (e.g. VALUE, MATRIX, CURVE, …)

Return type:  str

IsAutogenerated()[¶](#ApiClient.MappingItem.IsAutogenerated "Link to this definition")  
Returns whether the mapping item is autogenerated.

Returns:  True, if autogenerated flag is set, else False

Return type:  boolean

SetCategory(*category*)[¶](#ApiClient.MappingItem.SetCategory "Link to this definition")  
Sets the category

Parameters:  **category** (*str*) – The new category to be used

SetDescription(*description*)[¶](#ApiClient.MappingItem.SetDescription "Link to this definition")  
Sets the description

Parameters:  **description** (*str*) – The new description to be used

SetReferenceName(*name*)[¶](#ApiClient.MappingItem.SetReferenceName "Link to this definition")  
Sets the reference name of the mapping.

Parameters:  **name** (*str*) – The reference name of the mapping

## GenericMappingItem[¶](#genericmappingitem "Link to this heading")

*class* GenericMappingItem[¶](#ApiClient.GenericMappingItem "Link to this definition")  
Base class

[`MappingItem`](#ApiClient.MappingItem "ApiClient.MappingItem")

AddEnumeration(*text*, *value*)[¶](#ApiClient.GenericMappingItem.AddEnumeration "Link to this definition")  
Adds a (text: value) pair to an existing enumeration. Creates a new enumeration if none exists.

Parameters:  - **text** (*str*) – Text to show instead of the value

- **value** (*int*) – Value that should be mapped

Clone()[¶](#ApiClient.GenericMappingItem.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`GenericMappingItem`](#ApiClient.GenericMappingItem "ApiClient.GenericMappingItem")

GetAccessType()[¶](#ApiClient.GenericMappingItem.GetAccessType "Link to this definition")  
Returns a string identifying the mapping item’s type. (such as MODEL, BUS, MEASUREMENT, …)

Returns:  access type

Return type:  str

GetCategory()[¶](#ApiClient.GenericMappingItem.GetCategory "Link to this definition")  
Returns the category

Returns:  Category

Return type:  str

GetDescription()[¶](#ApiClient.GenericMappingItem.GetDescription "Link to this definition")  
Returns the description

Returns:  Description

Return type:  str

GetDisplayedType()[¶](#ApiClient.GenericMappingItem.GetDisplayedType "Link to this definition")  
Returns a “nice” representation of the type as displayed in the “type” column of the mapping panel

Returns:  the displayed mapping type

Return type:  str

GetEnumeration()[¶](#ApiClient.GenericMappingItem.GetEnumeration "Link to this definition")  
Returns the enumeration of the mapping item.

Returns:  Dictionary with the (text: value) pairs.

Return type:  dict[str, int]

GetReferenceName()[¶](#ApiClient.GenericMappingItem.GetReferenceName "Link to this definition")  
Returns the reference name of the mapping.

Returns:  The reference name of the mapping

Return type:  str

GetSubMapping()[¶](#ApiClient.GenericMappingItem.GetSubMapping "Link to this definition")  
Returns contained Mapping or None if item does not support sub-mappings.

Returns:  Mapping with all submappings of the mapping item

Return type:  [`Mapping`](#ApiClient.Mapping "ApiClient.Mapping")

GetSystemIdentifier()[¶](#ApiClient.GenericMappingItem.GetSystemIdentifier "Link to this definition")  
Returns the system identifier providing the currently mapped test quantity

Returns:  system identifier

Return type:  str

GetTargetPath()[¶](#ApiClient.GenericMappingItem.GetTargetPath "Link to this definition")  
Returns the path this mapping item is currently pointing at

Returns:  complete path to the destination test quantity

Return type:  str

GetVariableType()[¶](#ApiClient.GenericMappingItem.GetVariableType "Link to this definition")  
Returns the type of the target variable or None if target has no type.

Returns:  The type of the target variable. (e.g. VALUE, MATRIX, CURVE, …)

Return type:  str

IsAutogenerated()[¶](#ApiClient.GenericMappingItem.IsAutogenerated "Link to this definition")  
Returns whether the mapping item is autogenerated.

Returns:  True, if autogenerated flag is set, else False

Return type:  boolean

RemoveEnumeration()[¶](#ApiClient.GenericMappingItem.RemoveEnumeration "Link to this definition")  
Removes the enumeration of the mapping item.

Returns:  True on success

Return type:  bool

SetCategory(*category*)[¶](#ApiClient.GenericMappingItem.SetCategory "Link to this definition")  
Sets the category

Parameters:  **category** (*str*) – The new category to be used

SetDescription(*description*)[¶](#ApiClient.GenericMappingItem.SetDescription "Link to this definition")  
Sets the description

Parameters:  **description** (*str*) – The new description to be used

SetEnumeration(*vtabDict*)[¶](#ApiClient.GenericMappingItem.SetEnumeration "Link to this definition")  
Sets the enumeration of the mapping item.

Parameters:  **vtabDict** (*dict[str,* *int]*) – Dictionary with the (text: value) pairs.

SetReferenceName(*name*)[¶](#ApiClient.GenericMappingItem.SetReferenceName "Link to this definition")  
Sets the reference name of the mapping.

Parameters:  **name** (*str*) – The reference name of the mapping

## PackageMappingItem[¶](#packagemappingitem "Link to this heading")

*class* PackageMappingItem[¶](#ApiClient.PackageMappingItem "Link to this definition")  
Base class

[`MappingItem`](#ApiClient.MappingItem "ApiClient.MappingItem")

Returned by

- [`MappingApi.CreatePackageMappingItem`](#ApiClient.MappingApi.CreatePackageMappingItem "ApiClient.MappingApi.CreatePackageMappingItem")

Clone()[¶](#ApiClient.PackageMappingItem.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`PackageMappingItem`](#ApiClient.PackageMappingItem "ApiClient.PackageMappingItem")

GetAccessType()[¶](#ApiClient.PackageMappingItem.GetAccessType "Link to this definition")  
Returns a string identifying the mapping item’s type. (such as MODEL, BUS, MEASUREMENT, …)

Returns:  access type

Return type:  str

GetCategory()[¶](#ApiClient.PackageMappingItem.GetCategory "Link to this definition")  
Returns the category

Returns:  Category

Return type:  str

GetDescription()[¶](#ApiClient.PackageMappingItem.GetDescription "Link to this definition")  
Returns the description

Returns:  Description

Return type:  str

GetDisplayedType()[¶](#ApiClient.PackageMappingItem.GetDisplayedType "Link to this definition")  
Returns a “nice” representation of the type as displayed in the “type” column of the mapping panel

Returns:  the displayed mapping type

Return type:  str

GetReferenceName()[¶](#ApiClient.PackageMappingItem.GetReferenceName "Link to this definition")  
Returns the reference name of the mapping.

Returns:  The reference name of the mapping

Return type:  str

GetSubMapping()[¶](#ApiClient.PackageMappingItem.GetSubMapping "Link to this definition")  
Returns contained Mapping or None if item does not support sub-mappings.

Returns:  Mapping with all submappings of the mapping item

Return type:  [`Mapping`](#ApiClient.Mapping "ApiClient.Mapping")

GetSystemIdentifier()[¶](#ApiClient.PackageMappingItem.GetSystemIdentifier "Link to this definition")  
Returns the system identifier providing the currently mapped test quantity

Returns:  system identifier

Return type:  str

GetTargetPath()[¶](#ApiClient.PackageMappingItem.GetTargetPath "Link to this definition")  
Returns the path this mapping item is currently pointing at

Returns:  complete path to the destination test quantity

Return type:  str

GetVariableType()[¶](#ApiClient.PackageMappingItem.GetVariableType "Link to this definition")  
Returns the type of the target variable or None if target has no type.

Returns:  The type of the target variable. (e.g. VALUE, MATRIX, CURVE, …)

Return type:  str

IsAutogenerated()[¶](#ApiClient.PackageMappingItem.IsAutogenerated "Link to this definition")  
Returns whether the mapping item is autogenerated.

Returns:  True, if autogenerated flag is set, else False

Return type:  boolean

SetCategory(*category*)[¶](#ApiClient.PackageMappingItem.SetCategory "Link to this definition")  
Sets the category

Parameters:  **category** (*str*) – The new category to be used

SetDescription(*description*)[¶](#ApiClient.PackageMappingItem.SetDescription "Link to this definition")  
Sets the description

Parameters:  **description** (*str*) – The new description to be used

SetReferenceName(*name*)[¶](#ApiClient.PackageMappingItem.SetReferenceName "Link to this definition")  
Sets the reference name of the mapping.

Parameters:  **name** (*str*) – The reference name of the mapping

## GenericPackageMappingItem[¶](#genericpackagemappingitem "Link to this heading")

*class* GenericPackageMappingItem[¶](#ApiClient.GenericPackageMappingItem "Link to this definition")  
Base class

[`MappingItem`](#ApiClient.MappingItem "ApiClient.MappingItem")

Clone()[¶](#ApiClient.GenericPackageMappingItem.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`GenericPackageMappingItem`](#ApiClient.GenericPackageMappingItem "ApiClient.GenericPackageMappingItem")

GetAccessType()[¶](#ApiClient.GenericPackageMappingItem.GetAccessType "Link to this definition")  
Returns a string identifying the mapping item’s type. (such as MODEL, BUS, MEASUREMENT, …)

Returns:  access type

Return type:  str

GetCategory()[¶](#ApiClient.GenericPackageMappingItem.GetCategory "Link to this definition")  
Returns the category

Returns:  Category

Return type:  str

GetDescription()[¶](#ApiClient.GenericPackageMappingItem.GetDescription "Link to this definition")  
Returns the description

Returns:  Description

Return type:  str

GetDisplayedType()[¶](#ApiClient.GenericPackageMappingItem.GetDisplayedType "Link to this definition")  
Returns a “nice” representation of the type as displayed in the “type” column of the mapping panel

Returns:  the displayed mapping type

Return type:  str

GetReferenceName()[¶](#ApiClient.GenericPackageMappingItem.GetReferenceName "Link to this definition")  
Returns the reference name of the mapping.

Returns:  The reference name of the mapping

Return type:  str

GetSubMapping()[¶](#ApiClient.GenericPackageMappingItem.GetSubMapping "Link to this definition")  
Returns contained Mapping or None if item does not support sub-mappings.

Returns:  Mapping with all submappings of the mapping item

Return type:  [`Mapping`](#ApiClient.Mapping "ApiClient.Mapping")

GetSystemIdentifier()[¶](#ApiClient.GenericPackageMappingItem.GetSystemIdentifier "Link to this definition")  
Returns the system identifier providing the currently mapped test quantity

Returns:  system identifier

Return type:  str

GetTargetPath()[¶](#ApiClient.GenericPackageMappingItem.GetTargetPath "Link to this definition")  
Returns the path this mapping item is currently pointing at

Returns:  complete path to the destination test quantity

Return type:  str

GetVariableType()[¶](#ApiClient.GenericPackageMappingItem.GetVariableType "Link to this definition")  
Returns the type of the target variable or None if target has no type.

Returns:  The type of the target variable. (e.g. VALUE, MATRIX, CURVE, …)

Return type:  str

IsAutogenerated()[¶](#ApiClient.GenericPackageMappingItem.IsAutogenerated "Link to this definition")  
Returns whether the mapping item is autogenerated.

Returns:  True, if autogenerated flag is set, else False

Return type:  boolean

SetCategory(*category*)[¶](#ApiClient.GenericPackageMappingItem.SetCategory "Link to this definition")  
Sets the category

Parameters:  **category** (*str*) – The new category to be used

SetDescription(*description*)[¶](#ApiClient.GenericPackageMappingItem.SetDescription "Link to this definition")  
Sets the description

Parameters:  **description** (*str*) – The new description to be used

SetReferenceName(*name*)[¶](#ApiClient.GenericPackageMappingItem.SetReferenceName "Link to this definition")  
Sets the reference name of the mapping.

Parameters:  **name** (*str*) – The reference name of the mapping

## BusMonitoringMappingItem[¶](#busmonitoringmappingitem "Link to this heading")

*class* BusMonitoringMappingItem[¶](#ApiClient.BusMonitoringMappingItem "Link to this definition")  
Base class

[`MappingItem`](#ApiClient.MappingItem "ApiClient.MappingItem")

Returned by

- [`MappingApi.CreateBusMonitoringMappingItem`](#ApiClient.MappingApi.CreateBusMonitoringMappingItem "ApiClient.MappingApi.CreateBusMonitoringMappingItem")

Clone()[¶](#ApiClient.BusMonitoringMappingItem.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`BusMonitoringMappingItem`](#ApiClient.BusMonitoringMappingItem "ApiClient.BusMonitoringMappingItem")

DeactivateCycleTime()[¶](#ApiClient.BusMonitoringMappingItem.DeactivateCycleTime "Link to this definition")  
Deactivates the cycle option.

DeactivateDebounce()[¶](#ApiClient.BusMonitoringMappingItem.DeactivateDebounce "Link to this definition")  
Deactivates the debounce option.

GetAccessType()[¶](#ApiClient.BusMonitoringMappingItem.GetAccessType "Link to this definition")  
Returns a string identifying the mapping item’s type. (such as MODEL, BUS, MEASUREMENT, …)

Returns:  access type

Return type:  str

GetCategory()[¶](#ApiClient.BusMonitoringMappingItem.GetCategory "Link to this definition")  
Returns the category

Returns:  Category

Return type:  str

GetCycleTimeMax()[¶](#ApiClient.BusMonitoringMappingItem.GetCycleTimeMax "Link to this definition")  
Returns the maximum cycle time in milliseconds.

Returns:  Maximum cycle time in milliseconds

Return type:  integer

GetCycleTimeMin()[¶](#ApiClient.BusMonitoringMappingItem.GetCycleTimeMin "Link to this definition")  
Returns the minimum cycle time in milliseconds.

Returns:  Minimum cycle time in milliseconds

Return type:  integer

GetDebounceTime()[¶](#ApiClient.BusMonitoringMappingItem.GetDebounceTime "Link to this definition")  
Returns the debounce time in milliseconds.

Returns:  Debounce time in milliseconds

Return type:  integer

GetDescription()[¶](#ApiClient.BusMonitoringMappingItem.GetDescription "Link to this definition")  
Returns the description

Returns:  Description

Return type:  str

GetDisplayedType()[¶](#ApiClient.BusMonitoringMappingItem.GetDisplayedType "Link to this definition")  
Returns a “nice” representation of the type as displayed in the “type” column of the mapping panel

Returns:  the displayed mapping type

Return type:  str

GetFrameName()[¶](#ApiClient.BusMonitoringMappingItem.GetFrameName "Link to this definition")  
Returns the name of the frame containing the signal.

Returns:  Name of the frame containing the signal or empty string if no frame name is set

Return type:  str

GetNodeName()[¶](#ApiClient.BusMonitoringMappingItem.GetNodeName "Link to this definition")  
Returns the name of the sending ECU.

Returns:  Name of the sending ECU or empty string if no name node name is set

Return type:  str

GetReferenceName()[¶](#ApiClient.BusMonitoringMappingItem.GetReferenceName "Link to this definition")  
Returns the reference name of the mapping.

Returns:  The reference name of the mapping

Return type:  str

GetSubMapping()[¶](#ApiClient.BusMonitoringMappingItem.GetSubMapping "Link to this definition")  
Returns contained Mapping or None if item does not support sub-mappings.

Returns:  Mapping with all submappings of the mapping item

Return type:  [`Mapping`](#ApiClient.Mapping "ApiClient.Mapping")

GetSystemIdentifier()[¶](#ApiClient.BusMonitoringMappingItem.GetSystemIdentifier "Link to this definition")  
Returns the system identifier providing the currently mapped test quantity

Returns:  system identifier

Return type:  str

GetTargetPath()[¶](#ApiClient.BusMonitoringMappingItem.GetTargetPath "Link to this definition")  
Returns the path this mapping item is currently pointing at

Returns:  complete path to the destination test quantity

Return type:  str

GetVariableType()[¶](#ApiClient.BusMonitoringMappingItem.GetVariableType "Link to this definition")  
Returns the type of the target variable or None if target has no type.

Returns:  The type of the target variable. (e.g. VALUE, MATRIX, CURVE, …)

Return type:  str

IsAutogenerated()[¶](#ApiClient.BusMonitoringMappingItem.IsAutogenerated "Link to this definition")  
Returns whether the mapping item is autogenerated.

Returns:  True, if autogenerated flag is set, else False

Return type:  boolean

SetCategory(*category*)[¶](#ApiClient.BusMonitoringMappingItem.SetCategory "Link to this definition")  
Sets the category

Parameters:  **category** (*str*) – The new category to be used

SetCycleTimeMax(*cycleTimeMax*)[¶](#ApiClient.BusMonitoringMappingItem.SetCycleTimeMax "Link to this definition")  
Sets the maximum cycle time in milliseconds.

Parameters:  **cycleTimeMax** (*integer*) – Maximum cycle time in milliseconds

SetCycleTimeMin(*cycleTimeMin*)[¶](#ApiClient.BusMonitoringMappingItem.SetCycleTimeMin "Link to this definition")  
Sets the minimum cycle time in milliseconds.

Parameters:  **cycleTimeMin** (*integer*) – Minimum cycle time in milliseconds

SetDebounceTime(*debounceTime*)[¶](#ApiClient.BusMonitoringMappingItem.SetDebounceTime "Link to this definition")  
Sets the debounce time in milliseconds.

Parameters:  **debounceTime** (*integer*) – Debounce time in milliseconds

SetDescription(*description*)[¶](#ApiClient.BusMonitoringMappingItem.SetDescription "Link to this definition")  
Sets the description

Parameters:  **description** (*str*) – The new description to be used

SetFrameName(*frameName*)[¶](#ApiClient.BusMonitoringMappingItem.SetFrameName "Link to this definition")  
Sets the name of the frame containing the signal.

Parameters:  **frameName** (*str*) – Name of the frame containing the signal

SetNodeName(*nodeName*)[¶](#ApiClient.BusMonitoringMappingItem.SetNodeName "Link to this definition")  
Sets the name of the sending ECU.

Parameters:  **nodeName** (*str*) – Name of the sending ECU

SetReferenceName(*name*)[¶](#ApiClient.BusMonitoringMappingItem.SetReferenceName "Link to this definition")  
Sets the reference name of the mapping.

Parameters:  **name** (*str*) – The reference name of the mapping

## BusSignalGroupMappingItem[¶](#bussignalgroupmappingitem "Link to this heading")

*class* BusSignalGroupMappingItem[¶](#ApiClient.BusSignalGroupMappingItem "Link to this definition")  
Base class

[`MappingItem`](#ApiClient.MappingItem "ApiClient.MappingItem")

Returned by

- [`MappingApi.CreateBusSignalGroupMappingItem`](#ApiClient.MappingApi.CreateBusSignalGroupMappingItem "ApiClient.MappingApi.CreateBusSignalGroupMappingItem")

Clone()[¶](#ApiClient.BusSignalGroupMappingItem.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`BusSignalGroupMappingItem`](#ApiClient.BusSignalGroupMappingItem "ApiClient.BusSignalGroupMappingItem")

GetAccessType()[¶](#ApiClient.BusSignalGroupMappingItem.GetAccessType "Link to this definition")  
Returns a string identifying the mapping item’s type. (such as MODEL, BUS, MEASUREMENT, …)

Returns:  access type

Return type:  str

GetCategory()[¶](#ApiClient.BusSignalGroupMappingItem.GetCategory "Link to this definition")  
Returns the category

Returns:  Category

Return type:  str

GetDescription()[¶](#ApiClient.BusSignalGroupMappingItem.GetDescription "Link to this definition")  
Returns the description

Returns:  Description

Return type:  str

GetDisplayedType()[¶](#ApiClient.BusSignalGroupMappingItem.GetDisplayedType "Link to this definition")  
Returns a “nice” representation of the type as displayed in the “type” column of the mapping panel

Returns:  the displayed mapping type

Return type:  str

GetFrameName()[¶](#ApiClient.BusSignalGroupMappingItem.GetFrameName "Link to this definition")  
Returns the name of the frame containing the signal.

Returns:  Name of the frame containing the signal

Return type:  str

GetNodeName()[¶](#ApiClient.BusSignalGroupMappingItem.GetNodeName "Link to this definition")  
Returns the name of the sending ECU.

Returns:  Name of the sending ECU

Return type:  str

GetPduName()[¶](#ApiClient.BusSignalGroupMappingItem.GetPduName "Link to this definition")  
Returns the name of the PDU containing the signal.

Returns:  Name of the PDU containing the signal or empty string if no PDU name is set

Return type:  str

GetReferenceName()[¶](#ApiClient.BusSignalGroupMappingItem.GetReferenceName "Link to this definition")  
Returns the reference name of the mapping.

Returns:  The reference name of the mapping

Return type:  str

GetSubMapping()[¶](#ApiClient.BusSignalGroupMappingItem.GetSubMapping "Link to this definition")  
Returns contained Mapping or None if item does not support sub-mappings.

Returns:  Mapping with all submappings of the mapping item

Return type:  [`Mapping`](#ApiClient.Mapping "ApiClient.Mapping")

GetSystemIdentifier()[¶](#ApiClient.BusSignalGroupMappingItem.GetSystemIdentifier "Link to this definition")  
Returns the system identifier providing the currently mapped test quantity

Returns:  system identifier

Return type:  str

GetTargetPath()[¶](#ApiClient.BusSignalGroupMappingItem.GetTargetPath "Link to this definition")  
Returns the path this mapping item is currently pointing at

Returns:  complete path to the destination test quantity

Return type:  str

GetVariableType()[¶](#ApiClient.BusSignalGroupMappingItem.GetVariableType "Link to this definition")  
Returns the type of the target variable or None if target has no type.

Returns:  The type of the target variable. (e.g. VALUE, MATRIX, CURVE, …)

Return type:  str

IsAutogenerated()[¶](#ApiClient.BusSignalGroupMappingItem.IsAutogenerated "Link to this definition")  
Returns whether the mapping item is autogenerated.

Returns:  True, if autogenerated flag is set, else False

Return type:  boolean

SetCategory(*category*)[¶](#ApiClient.BusSignalGroupMappingItem.SetCategory "Link to this definition")  
Sets the category

Parameters:  **category** (*str*) – The new category to be used

SetDescription(*description*)[¶](#ApiClient.BusSignalGroupMappingItem.SetDescription "Link to this definition")  
Sets the description

Parameters:  **description** (*str*) – The new description to be used

SetFrameName(*frameName*)[¶](#ApiClient.BusSignalGroupMappingItem.SetFrameName "Link to this definition")  
Sets the name of the frame containing the signal.

Parameters:  **frameName** (*str*) – Name of the frame containing the signal

SetNodeName(*nodeName*)[¶](#ApiClient.BusSignalGroupMappingItem.SetNodeName "Link to this definition")  
Sets the name of the sending ECU.

Parameters:  **nodeName** (*str*) – Name of the sending ECU

SetPduName(*pduName*)[¶](#ApiClient.BusSignalGroupMappingItem.SetPduName "Link to this definition")  
Sets the name of the PDU containing the signal.

Parameters:  **pduName** (*str*) – Name of the PDU containing the signal

SetReferenceName(*name*)[¶](#ApiClient.BusSignalGroupMappingItem.SetReferenceName "Link to this definition")  
Sets the reference name of the mapping.

Parameters:  **name** (*str*) – The reference name of the mapping

## BusSignalMappingItem[¶](#bussignalmappingitem "Link to this heading")

*class* BusSignalMappingItem[¶](#ApiClient.BusSignalMappingItem "Link to this definition")  
Base class

[`MappingItem`](#ApiClient.MappingItem "ApiClient.MappingItem")

Returned by

- [`MappingApi.CreateBusSignalWithPduMappingItem`](#ApiClient.MappingApi.CreateBusSignalWithPduMappingItem "ApiClient.MappingApi.CreateBusSignalWithPduMappingItem")

Clone()[¶](#ApiClient.BusSignalMappingItem.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`BusSignalMappingItem`](#ApiClient.BusSignalMappingItem "ApiClient.BusSignalMappingItem")

GetAccessType()[¶](#ApiClient.BusSignalMappingItem.GetAccessType "Link to this definition")  
Returns a string identifying the mapping item’s type. (such as MODEL, BUS, MEASUREMENT, …)

Returns:  access type

Return type:  str

GetCategory()[¶](#ApiClient.BusSignalMappingItem.GetCategory "Link to this definition")  
Returns the category

Returns:  Category

Return type:  str

GetDescription()[¶](#ApiClient.BusSignalMappingItem.GetDescription "Link to this definition")  
Returns the description

Returns:  Description

Return type:  str

GetDisplayedType()[¶](#ApiClient.BusSignalMappingItem.GetDisplayedType "Link to this definition")  
Returns a “nice” representation of the type as displayed in the “type” column of the mapping panel

Returns:  the displayed mapping type

Return type:  str

GetFrameName()[¶](#ApiClient.BusSignalMappingItem.GetFrameName "Link to this definition")  
Returns the name of the frame containing the signal.

Returns:  Name of the frame containing the signal or empty string if no frame name is set

Return type:  str

GetNodeName()[¶](#ApiClient.BusSignalMappingItem.GetNodeName "Link to this definition")  
Returns the name of the sending ECU.

Returns:  Name of the sending ECU or empty string if no node name is set

Return type:  str

GetPduName()[¶](#ApiClient.BusSignalMappingItem.GetPduName "Link to this definition")  
Returns the name of the PDU containing the signal.

Returns:  Name of the PDU containing the signal or empty string if no PDU name is set

Return type:  str

GetReferenceName()[¶](#ApiClient.BusSignalMappingItem.GetReferenceName "Link to this definition")  
Returns the reference name of the mapping.

Returns:  The reference name of the mapping

Return type:  str

GetSignalManipulation()[¶](#ApiClient.BusSignalMappingItem.GetSignalManipulation "Link to this definition")  
Returns the manipulation parameters. Can only be used for bus signals!

Returns:  SignalManipulation. Possible values:

- None: signal manipulation is disabled

- 0: signal manipulation is permanent

- n\>0: signal is manipulated for n frames

Return type:  int

GetSignalName()[¶](#ApiClient.BusSignalMappingItem.GetSignalName "Link to this definition")  
Returns the name of the signal. :return: Name of the signal :rtype: str

GetSubMapping()[¶](#ApiClient.BusSignalMappingItem.GetSubMapping "Link to this definition")  
Returns contained Mapping or None if item does not support sub-mappings.

Returns:  Mapping with all submappings of the mapping item

Return type:  [`Mapping`](#ApiClient.Mapping "ApiClient.Mapping")

GetSystemIdentifier()[¶](#ApiClient.BusSignalMappingItem.GetSystemIdentifier "Link to this definition")  
Returns the system identifier providing the currently mapped test quantity

Returns:  system identifier

Return type:  str

GetTargetPath()[¶](#ApiClient.BusSignalMappingItem.GetTargetPath "Link to this definition")  
Returns the path this mapping item is currently pointing at

Returns:  complete path to the destination test quantity

Return type:  str

GetVariableType()[¶](#ApiClient.BusSignalMappingItem.GetVariableType "Link to this definition")  
Returns the type of the target variable or None if target has no type.

Returns:  The type of the target variable. (e.g. VALUE, MATRIX, CURVE, …)

Return type:  str

IsAutogenerated()[¶](#ApiClient.BusSignalMappingItem.IsAutogenerated "Link to this definition")  
Returns whether the mapping item is autogenerated.

Returns:  True, if autogenerated flag is set, else False

Return type:  boolean

SetCategory(*category*)[¶](#ApiClient.BusSignalMappingItem.SetCategory "Link to this definition")  
Sets the category

Parameters:  **category** (*str*) – The new category to be used

SetDescription(*description*)[¶](#ApiClient.BusSignalMappingItem.SetDescription "Link to this definition")  
Sets the description

Parameters:  **description** (*str*) – The new description to be used

SetFrameName(*frameName*)[¶](#ApiClient.BusSignalMappingItem.SetFrameName "Link to this definition")  
Sets the name of the frame containing the signal.

Parameters:  **frameName** (*str*) – Name of the frame containing the signal

SetNodeName(*nodeName*)[¶](#ApiClient.BusSignalMappingItem.SetNodeName "Link to this definition")  
Sets the name of the sending ECU.

Parameters:  **nodeName** (*str*) – Name of the sending ECU

SetPduName(*pduName*)[¶](#ApiClient.BusSignalMappingItem.SetPduName "Link to this definition")  
Sets the name of the PDU containing the signal.

Parameters:  **pduName** (*str*) – Name of the PDU containing the signal

SetReferenceName(*name*)[¶](#ApiClient.BusSignalMappingItem.SetReferenceName "Link to this definition")  
Sets the reference name of the mapping.

Parameters:  **name** (*str*) – The reference name of the mapping

SetSignalManipulation(*value=None*)[¶](#ApiClient.BusSignalMappingItem.SetSignalManipulation "Link to this definition")  
Sets the manipulation parameters. Can only be used for bus signals!

Parameters:  **value** (*int*) –

The value to be used. Possible values:

- None: signal manipulation parameters will be disabled

- 0: permanent

- n\>0: signal is manipulated for n frames

SetSignalName(*signalName*)[¶](#ApiClient.BusSignalMappingItem.SetSignalName "Link to this definition")  
Sets the name of the signal. :param signalName: Name of the signal :type signalName: str

## PortMappingItem[¶](#portmappingitem "Link to this heading")

*class* PortMappingItem[¶](#ApiClient.PortMappingItem "Link to this definition")  
Base class

[`MappingItem`](#ApiClient.MappingItem "ApiClient.MappingItem")

Returned by

- [`MappingApi.CreatePortMappingItem`](#ApiClient.MappingApi.CreatePortMappingItem "ApiClient.MappingApi.CreatePortMappingItem")

Clone()[¶](#ApiClient.PortMappingItem.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`PortMappingItem`](#ApiClient.PortMappingItem "ApiClient.PortMappingItem")

GetAccessType()[¶](#ApiClient.PortMappingItem.GetAccessType "Link to this definition")  
Returns a string identifying the mapping item’s type. (such as MODEL, BUS, MEASUREMENT, …)

Returns:  access type

Return type:  str

GetCategory()[¶](#ApiClient.PortMappingItem.GetCategory "Link to this definition")  
Returns the category

Returns:  Category

Return type:  str

GetDescription()[¶](#ApiClient.PortMappingItem.GetDescription "Link to this definition")  
Returns the description

Returns:  Description

Return type:  str

GetDisplayedType()[¶](#ApiClient.PortMappingItem.GetDisplayedType "Link to this definition")  
Returns a “nice” representation of the type as displayed in the “type” column of the mapping panel

Returns:  the displayed mapping type

Return type:  str

GetReferenceName()[¶](#ApiClient.PortMappingItem.GetReferenceName "Link to this definition")  
Returns the reference name of the mapping.

Returns:  The reference name of the mapping

Return type:  str

GetSubMapping()[¶](#ApiClient.PortMappingItem.GetSubMapping "Link to this definition")  
Returns contained Mapping or None if item does not support sub-mappings.

Returns:  Mapping with all submappings of the mapping item

Return type:  [`Mapping`](#ApiClient.Mapping "ApiClient.Mapping")

GetSystemIdentifier()[¶](#ApiClient.PortMappingItem.GetSystemIdentifier "Link to this definition")  
Returns the system identifier providing the currently mapped test quantity

Returns:  system identifier

Return type:  str

GetTargetPath()[¶](#ApiClient.PortMappingItem.GetTargetPath "Link to this definition")  
Returns the path this mapping item is currently pointing at

Returns:  complete path to the destination test quantity

Return type:  str

GetVariableType()[¶](#ApiClient.PortMappingItem.GetVariableType "Link to this definition")  
Returns the type of the target variable or None if target has no type.

Returns:  The type of the target variable. (e.g. VALUE, MATRIX, CURVE, …)

Return type:  str

IsAutogenerated()[¶](#ApiClient.PortMappingItem.IsAutogenerated "Link to this definition")  
Returns whether the mapping item is autogenerated.

Returns:  True, if autogenerated flag is set, else False

Return type:  boolean

SetCategory(*category*)[¶](#ApiClient.PortMappingItem.SetCategory "Link to this definition")  
Sets the category

Parameters:  **category** (*str*) – The new category to be used

SetDescription(*description*)[¶](#ApiClient.PortMappingItem.SetDescription "Link to this definition")  
Sets the description

Parameters:  **description** (*str*) – The new description to be used

SetReferenceName(*name*)[¶](#ApiClient.PortMappingItem.SetReferenceName "Link to this definition")  
Sets the reference name of the mapping.

Parameters:  **name** (*str*) – The reference name of the mapping

## DebugMappingItem[¶](#debugmappingitem "Link to this heading")

*class* DebugMappingItem[¶](#ApiClient.DebugMappingItem "Link to this definition")  
Interface of MappingItems for debugging variables. Debugging registers have their own interface.

Base class

[`MappingItem`](#ApiClient.MappingItem "ApiClient.MappingItem")

Returned by

- [`MappingApi.CreateDebugMappingItem`](#ApiClient.MappingApi.CreateDebugMappingItem "ApiClient.MappingApi.CreateDebugMappingItem")

Clone()[¶](#ApiClient.DebugMappingItem.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`DebugMappingItem`](#ApiClient.DebugMappingItem "ApiClient.DebugMappingItem")

GetAccessType()[¶](#ApiClient.DebugMappingItem.GetAccessType "Link to this definition")  
Returns a string identifying the mapping item’s type. (such as MODEL, BUS, MEASUREMENT, …)

Returns:  access type

Return type:  str

GetCategory()[¶](#ApiClient.DebugMappingItem.GetCategory "Link to this definition")  
Returns the category

Returns:  Category

Return type:  str

GetDescription()[¶](#ApiClient.DebugMappingItem.GetDescription "Link to this definition")  
Returns the description

Returns:  Description

Return type:  str

GetDisplayedType()[¶](#ApiClient.DebugMappingItem.GetDisplayedType "Link to this definition")  
Returns a “nice” representation of the type as displayed in the “type” column of the mapping panel

Returns:  the displayed mapping type

Return type:  str

GetReferenceName()[¶](#ApiClient.DebugMappingItem.GetReferenceName "Link to this definition")  
Returns the reference name of the mapping.

Returns:  The reference name of the mapping

Return type:  str

GetSubMapping()[¶](#ApiClient.DebugMappingItem.GetSubMapping "Link to this definition")  
Returns contained Mapping or None if item does not support sub-mappings.

Returns:  Mapping with all submappings of the mapping item

Return type:  [`Mapping`](#ApiClient.Mapping "ApiClient.Mapping")

GetSystemIdentifier()[¶](#ApiClient.DebugMappingItem.GetSystemIdentifier "Link to this definition")  
Returns the system identifier providing the currently mapped test quantity

Returns:  system identifier

Return type:  str

GetTargetPath()[¶](#ApiClient.DebugMappingItem.GetTargetPath "Link to this definition")  
Returns the path this mapping item is currently pointing at

Returns:  complete path to the destination test quantity

Return type:  str

GetVariableType()[¶](#ApiClient.DebugMappingItem.GetVariableType "Link to this definition")  
Returns the type of the target variable or None if target has no type.

Returns:  The type of the target variable. (e.g. VALUE, MATRIX, CURVE, …)

Return type:  str

IsAutogenerated()[¶](#ApiClient.DebugMappingItem.IsAutogenerated "Link to this definition")  
Returns whether the mapping item is autogenerated.

Returns:  True, if autogenerated flag is set, else False

Return type:  boolean

SetCategory(*category*)[¶](#ApiClient.DebugMappingItem.SetCategory "Link to this definition")  
Sets the category

Parameters:  **category** (*str*) – The new category to be used

SetDescription(*description*)[¶](#ApiClient.DebugMappingItem.SetDescription "Link to this definition")  
Sets the description

Parameters:  **description** (*str*) – The new description to be used

SetReferenceName(*name*)[¶](#ApiClient.DebugMappingItem.SetReferenceName "Link to this definition")  
Sets the reference name of the mapping.

Parameters:  **name** (*str*) – The reference name of the mapping

## DebugRegisterMappingItem[¶](#debugregistermappingitem "Link to this heading")

*class* DebugRegisterMappingItem[¶](#ApiClient.DebugRegisterMappingItem "Link to this definition")  
Interface of MappingItems for debugging registers.

Base class

[`MappingItem`](#ApiClient.MappingItem "ApiClient.MappingItem")

Returned by

- [`MappingApi.CreateDebugRegisterMappingItem`](#ApiClient.MappingApi.CreateDebugRegisterMappingItem "ApiClient.MappingApi.CreateDebugRegisterMappingItem")

Clone()[¶](#ApiClient.DebugRegisterMappingItem.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`DebugRegisterMappingItem`](#ApiClient.DebugRegisterMappingItem "ApiClient.DebugRegisterMappingItem")

GetAccessType()[¶](#ApiClient.DebugRegisterMappingItem.GetAccessType "Link to this definition")  
Returns a string identifying the mapping item’s type. (such as MODEL, BUS, MEASUREMENT, …)

Returns:  access type

Return type:  str

GetCategory()[¶](#ApiClient.DebugRegisterMappingItem.GetCategory "Link to this definition")  
Returns the category

Returns:  Category

Return type:  str

GetDescription()[¶](#ApiClient.DebugRegisterMappingItem.GetDescription "Link to this definition")  
Returns the description

Returns:  Description

Return type:  str

GetDisplayedType()[¶](#ApiClient.DebugRegisterMappingItem.GetDisplayedType "Link to this definition")  
Returns a “nice” representation of the type as displayed in the “type” column of the mapping panel

Returns:  the displayed mapping type

Return type:  str

GetReferenceName()[¶](#ApiClient.DebugRegisterMappingItem.GetReferenceName "Link to this definition")  
Returns the reference name of the mapping.

Returns:  The reference name of the mapping

Return type:  str

GetSubMapping()[¶](#ApiClient.DebugRegisterMappingItem.GetSubMapping "Link to this definition")  
Returns contained Mapping or None if item does not support sub-mappings.

Returns:  Mapping with all submappings of the mapping item

Return type:  [`Mapping`](#ApiClient.Mapping "ApiClient.Mapping")

GetSystemIdentifier()[¶](#ApiClient.DebugRegisterMappingItem.GetSystemIdentifier "Link to this definition")  
Returns the system identifier providing the currently mapped test quantity

Returns:  system identifier

Return type:  str

GetTargetPath()[¶](#ApiClient.DebugRegisterMappingItem.GetTargetPath "Link to this definition")  
Returns the path this mapping item is currently pointing at

Returns:  complete path to the destination test quantity

Return type:  str

GetVariableType()[¶](#ApiClient.DebugRegisterMappingItem.GetVariableType "Link to this definition")  
Returns the type of the target variable or None if target has no type.

Returns:  The type of the target variable. (e.g. VALUE, MATRIX, CURVE, …)

Return type:  str

IsAutogenerated()[¶](#ApiClient.DebugRegisterMappingItem.IsAutogenerated "Link to this definition")  
Returns whether the mapping item is autogenerated.

Returns:  True, if autogenerated flag is set, else False

Return type:  boolean

SetCategory(*category*)[¶](#ApiClient.DebugRegisterMappingItem.SetCategory "Link to this definition")  
Sets the category

Parameters:  **category** (*str*) – The new category to be used

SetDescription(*description*)[¶](#ApiClient.DebugRegisterMappingItem.SetDescription "Link to this definition")  
Sets the description

Parameters:  **description** (*str*) – The new description to be used

SetReferenceName(*name*)[¶](#ApiClient.DebugRegisterMappingItem.SetReferenceName "Link to this definition")  
Sets the reference name of the mapping.

Parameters:  **name** (*str*) – The reference name of the mapping

## DiagDidMappingItem[¶](#diagdidmappingitem "Link to this heading")

*class* DiagDidMappingItem[¶](#ApiClient.DiagDidMappingItem "Link to this definition")  
Base classes

- [`MappingItem`](#ApiClient.MappingItem "ApiClient.MappingItem")

- [`CallableMappingItem`](#ApiClient.CallableMappingItem "ApiClient.CallableMappingItem")

Returned by

- [`MappingApi.CreateDiagDidMappingItem`](#ApiClient.MappingApi.CreateDiagDidMappingItem "ApiClient.MappingApi.CreateDiagDidMappingItem")

Clone()[¶](#ApiClient.DiagDidMappingItem.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`DiagDidMappingItem`](#ApiClient.DiagDidMappingItem "ApiClient.DiagDidMappingItem")

GetAccessType()[¶](#ApiClient.DiagDidMappingItem.GetAccessType "Link to this definition")  
Returns a string identifying the mapping item’s type. (such as MODEL, BUS, MEASUREMENT, …)

Returns:  access type

Return type:  str

GetCategory()[¶](#ApiClient.DiagDidMappingItem.GetCategory "Link to this definition")  
Returns the category

Returns:  Category

Return type:  str

GetDescription()[¶](#ApiClient.DiagDidMappingItem.GetDescription "Link to this definition")  
Returns the description

Returns:  Description

Return type:  str

GetDisplayedType()[¶](#ApiClient.DiagDidMappingItem.GetDisplayedType "Link to this definition")  
Returns a “nice” representation of the type as displayed in the “type” column of the mapping panel

Returns:  the displayed mapping type

Return type:  str

GetEcuKey()[¶](#ApiClient.DiagDidMappingItem.GetEcuKey "Link to this definition")  
Returns the ECU key.

Returns:  ECU key

Return type:  str

GetName()[¶](#ApiClient.DiagDidMappingItem.GetName "Link to this definition")  
Returns the DID name.

Returns:  DID name

Return type:  str

GetReferenceName()[¶](#ApiClient.DiagDidMappingItem.GetReferenceName "Link to this definition")  
Returns the reference name of the mapping.

Returns:  The reference name of the mapping

Return type:  str

GetSubMapping()[¶](#ApiClient.DiagDidMappingItem.GetSubMapping "Link to this definition")  
Returns contained Mapping or None if item does not support sub-mappings.

Returns:  Mapping with all submappings of the mapping item

Return type:  [`Mapping`](#ApiClient.Mapping "ApiClient.Mapping")

GetSystemIdentifier()[¶](#ApiClient.DiagDidMappingItem.GetSystemIdentifier "Link to this definition")  
Returns the system identifier providing the currently mapped test quantity

Returns:  system identifier

Return type:  str

GetTargetPath()[¶](#ApiClient.DiagDidMappingItem.GetTargetPath "Link to this definition")  
Returns the path this mapping item is currently pointing at

Returns:  complete path to the destination test quantity

Return type:  str

GetVariableType()[¶](#ApiClient.DiagDidMappingItem.GetVariableType "Link to this definition")  
Returns the type of the target variable or None if target has no type.

Returns:  The type of the target variable. (e.g. VALUE, MATRIX, CURVE, …)

Return type:  str

IsAutogenerated()[¶](#ApiClient.DiagDidMappingItem.IsAutogenerated "Link to this definition")  
Returns whether the mapping item is autogenerated.

Returns:  True, if autogenerated flag is set, else False

Return type:  boolean

SetCategory(*category*)[¶](#ApiClient.DiagDidMappingItem.SetCategory "Link to this definition")  
Sets the category

Parameters:  **category** (*str*) – The new category to be used

SetDescription(*description*)[¶](#ApiClient.DiagDidMappingItem.SetDescription "Link to this definition")  
Sets the description

Parameters:  **description** (*str*) – The new description to be used

SetReferenceName(*name*)[¶](#ApiClient.DiagDidMappingItem.SetReferenceName "Link to this definition")  
Sets the reference name of the mapping.

Parameters:  **name** (*str*) – The reference name of the mapping

## CallableMappingItem[¶](#callablemappingitem "Link to this heading")

*class* CallableMappingItem[¶](#ApiClient.CallableMappingItem "Link to this definition")  
Base class

[`MappingItem`](#ApiClient.MappingItem "ApiClient.MappingItem")

Subclasses

- [`DiagDidMappingItem`](#ApiClient.DiagDidMappingItem "ApiClient.DiagDidMappingItem")

- [`DiagRoutineMappingItem`](#ApiClient.DiagRoutineMappingItem "ApiClient.DiagRoutineMappingItem")

- [`DiagServiceMappingItem`](#ApiClient.DiagServiceMappingItem "ApiClient.DiagServiceMappingItem")

- [`ServiceMappingItem`](#ApiClient.ServiceMappingItem "ApiClient.ServiceMappingItem")

Clone()[¶](#ApiClient.CallableMappingItem.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`CallableMappingItem`](#ApiClient.CallableMappingItem "ApiClient.CallableMappingItem")

GetAccessType()[¶](#ApiClient.CallableMappingItem.GetAccessType "Link to this definition")  
Returns a string identifying the mapping item’s type. (such as MODEL, BUS, MEASUREMENT, …)

Returns:  access type

Return type:  str

GetCategory()[¶](#ApiClient.CallableMappingItem.GetCategory "Link to this definition")  
Returns the category

Returns:  Category

Return type:  str

GetDescription()[¶](#ApiClient.CallableMappingItem.GetDescription "Link to this definition")  
Returns the description

Returns:  Description

Return type:  str

GetDisplayedType()[¶](#ApiClient.CallableMappingItem.GetDisplayedType "Link to this definition")  
Returns a “nice” representation of the type as displayed in the “type” column of the mapping panel

Returns:  the displayed mapping type

Return type:  str

GetReferenceName()[¶](#ApiClient.CallableMappingItem.GetReferenceName "Link to this definition")  
Returns the reference name of the mapping.

Returns:  The reference name of the mapping

Return type:  str

GetSubMapping()[¶](#ApiClient.CallableMappingItem.GetSubMapping "Link to this definition")  
Returns contained Mapping or None if item does not support sub-mappings.

Returns:  Mapping with all submappings of the mapping item

Return type:  [`Mapping`](#ApiClient.Mapping "ApiClient.Mapping")

GetSystemIdentifier()[¶](#ApiClient.CallableMappingItem.GetSystemIdentifier "Link to this definition")  
Returns the system identifier providing the currently mapped test quantity

Returns:  system identifier

Return type:  str

GetTargetPath()[¶](#ApiClient.CallableMappingItem.GetTargetPath "Link to this definition")  
Returns the path this mapping item is currently pointing at

Returns:  complete path to the destination test quantity

Return type:  str

GetVariableType()[¶](#ApiClient.CallableMappingItem.GetVariableType "Link to this definition")  
Returns the type of the target variable or None if target has no type.

Returns:  The type of the target variable. (e.g. VALUE, MATRIX, CURVE, …)

Return type:  str

IsAutogenerated()[¶](#ApiClient.CallableMappingItem.IsAutogenerated "Link to this definition")  
Returns whether the mapping item is autogenerated.

Returns:  True, if autogenerated flag is set, else False

Return type:  boolean

SetCategory(*category*)[¶](#ApiClient.CallableMappingItem.SetCategory "Link to this definition")  
Sets the category

Parameters:  **category** (*str*) – The new category to be used

SetDescription(*description*)[¶](#ApiClient.CallableMappingItem.SetDescription "Link to this definition")  
Sets the description

Parameters:  **description** (*str*) – The new description to be used

SetReferenceName(*name*)[¶](#ApiClient.CallableMappingItem.SetReferenceName "Link to this definition")  
Sets the reference name of the mapping.

Parameters:  **name** (*str*) – The reference name of the mapping

## DiagRoutineMappingItem[¶](#diagroutinemappingitem "Link to this heading")

*class* DiagRoutineMappingItem[¶](#ApiClient.DiagRoutineMappingItem "Link to this definition")  
Base classes

- [`MappingItem`](#ApiClient.MappingItem "ApiClient.MappingItem")

- [`CallableMappingItem`](#ApiClient.CallableMappingItem "ApiClient.CallableMappingItem")

Returned by

- [`MappingApi.CreateDiagRoutineMappingItem`](#ApiClient.MappingApi.CreateDiagRoutineMappingItem "ApiClient.MappingApi.CreateDiagRoutineMappingItem")

Clone()[¶](#ApiClient.DiagRoutineMappingItem.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`DiagRoutineMappingItem`](#ApiClient.DiagRoutineMappingItem "ApiClient.DiagRoutineMappingItem")

GetAccessType()[¶](#ApiClient.DiagRoutineMappingItem.GetAccessType "Link to this definition")  
Returns a string identifying the mapping item’s type. (such as MODEL, BUS, MEASUREMENT, …)

Returns:  access type

Return type:  str

GetCategory()[¶](#ApiClient.DiagRoutineMappingItem.GetCategory "Link to this definition")  
Returns the category

Returns:  Category

Return type:  str

GetDescription()[¶](#ApiClient.DiagRoutineMappingItem.GetDescription "Link to this definition")  
Returns the description

Returns:  Description

Return type:  str

GetDisplayedType()[¶](#ApiClient.DiagRoutineMappingItem.GetDisplayedType "Link to this definition")  
Returns a “nice” representation of the type as displayed in the “type” column of the mapping panel

Returns:  the displayed mapping type

Return type:  str

GetEcuKey()[¶](#ApiClient.DiagRoutineMappingItem.GetEcuKey "Link to this definition")  
Returns the ECU key.

Returns:  ECU key

Return type:  str

GetInputParameterEnumeration(*parameterName*)[¶](#ApiClient.DiagRoutineMappingItem.GetInputParameterEnumeration "Link to this definition")  
Returns the enumeration of the input parameter.

Parameters:  **parameterName** (*str*) – name of the parameter

Returns:  Dictionary with the (text: value) pairs

Return type:  dict[str, int]

GetInputParameterNames()[¶](#ApiClient.DiagRoutineMappingItem.GetInputParameterNames "Link to this definition")  
Returns the names of the input parameters.

Returns:  names of the input parameters

Return type:  list[str]

GetInputParameterUnit(*parameterName*)[¶](#ApiClient.DiagRoutineMappingItem.GetInputParameterUnit "Link to this definition")  
Returns the unit of the input parameter.

Parameters:  **parameterName** (*str*) – name of the parameter

Returns:  unit of the parameter

Return type:  str

GetName()[¶](#ApiClient.DiagRoutineMappingItem.GetName "Link to this definition")  
Returns the RoutineControl name.

Returns:  RoutineControl name

Return type:  str

GetOutputParameterEnumeration(*parameterName*)[¶](#ApiClient.DiagRoutineMappingItem.GetOutputParameterEnumeration "Link to this definition")  
Returns the enumeration of the output parameter.

Parameters:  **parameterName** (*str*) – name of the parameter

Returns:  Dictionary with the (text: value) pairs

Return type:  dict[str, int]

GetOutputParameterNames()[¶](#ApiClient.DiagRoutineMappingItem.GetOutputParameterNames "Link to this definition")  
Returns the names of the output parameters.

Returns:  names of the output parameters

Return type:  list[str]

GetOutputParameterUnit(*parameterName*)[¶](#ApiClient.DiagRoutineMappingItem.GetOutputParameterUnit "Link to this definition")  
Returns the unit of the output parameter.

Parameters:  **parameterName** (*str*) – name of the parameter

Returns:  unit of the parameter

Return type:  str

GetReferenceName()[¶](#ApiClient.DiagRoutineMappingItem.GetReferenceName "Link to this definition")  
Returns the reference name of the mapping.

Returns:  The reference name of the mapping

Return type:  str

GetSubMapping()[¶](#ApiClient.DiagRoutineMappingItem.GetSubMapping "Link to this definition")  
Returns contained Mapping or None if item does not support sub-mappings.

Returns:  Mapping with all submappings of the mapping item

Return type:  [`Mapping`](#ApiClient.Mapping "ApiClient.Mapping")

GetSystemIdentifier()[¶](#ApiClient.DiagRoutineMappingItem.GetSystemIdentifier "Link to this definition")  
Returns the system identifier providing the currently mapped test quantity

Returns:  system identifier

Return type:  str

GetTargetPath()[¶](#ApiClient.DiagRoutineMappingItem.GetTargetPath "Link to this definition")  
Returns the path this mapping item is currently pointing at

Returns:  complete path to the destination test quantity

Return type:  str

GetVariableType()[¶](#ApiClient.DiagRoutineMappingItem.GetVariableType "Link to this definition")  
Returns the type of the target variable or None if target has no type.

Returns:  The type of the target variable. (e.g. VALUE, MATRIX, CURVE, …)

Return type:  str

IsAutogenerated()[¶](#ApiClient.DiagRoutineMappingItem.IsAutogenerated "Link to this definition")  
Returns whether the mapping item is autogenerated.

Returns:  True, if autogenerated flag is set, else False

Return type:  boolean

SetCategory(*category*)[¶](#ApiClient.DiagRoutineMappingItem.SetCategory "Link to this definition")  
Sets the category

Parameters:  **category** (*str*) – The new category to be used

SetDescription(*description*)[¶](#ApiClient.DiagRoutineMappingItem.SetDescription "Link to this definition")  
Sets the description

Parameters:  **description** (*str*) – The new description to be used

SetReferenceName(*name*)[¶](#ApiClient.DiagRoutineMappingItem.SetReferenceName "Link to this definition")  
Sets the reference name of the mapping.

Parameters:  **name** (*str*) – The reference name of the mapping

## DiagServiceMappingItem[¶](#diagservicemappingitem "Link to this heading")

*class* DiagServiceMappingItem[¶](#ApiClient.DiagServiceMappingItem "Link to this definition")  
Base classes

- [`MappingItem`](#ApiClient.MappingItem "ApiClient.MappingItem")

- [`CallableMappingItem`](#ApiClient.CallableMappingItem "ApiClient.CallableMappingItem")

Returned by

- [`MappingApi.CreateDiagServiceMappingItem`](#ApiClient.MappingApi.CreateDiagServiceMappingItem "ApiClient.MappingApi.CreateDiagServiceMappingItem")

Clone()[¶](#ApiClient.DiagServiceMappingItem.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`DiagServiceMappingItem`](#ApiClient.DiagServiceMappingItem "ApiClient.DiagServiceMappingItem")

GetAccessType()[¶](#ApiClient.DiagServiceMappingItem.GetAccessType "Link to this definition")  
Returns a string identifying the mapping item’s type. (such as MODEL, BUS, MEASUREMENT, …)

Returns:  access type

Return type:  str

GetCategory()[¶](#ApiClient.DiagServiceMappingItem.GetCategory "Link to this definition")  
Returns the category

Returns:  Category

Return type:  str

GetDescription()[¶](#ApiClient.DiagServiceMappingItem.GetDescription "Link to this definition")  
Returns the description

Returns:  Description

Return type:  str

GetDisplayedType()[¶](#ApiClient.DiagServiceMappingItem.GetDisplayedType "Link to this definition")  
Returns a “nice” representation of the type as displayed in the “type” column of the mapping panel

Returns:  the displayed mapping type

Return type:  str

GetEcuKey()[¶](#ApiClient.DiagServiceMappingItem.GetEcuKey "Link to this definition")  
Returns the ECU key.

Returns:  ECU key

Return type:  str

GetName()[¶](#ApiClient.DiagServiceMappingItem.GetName "Link to this definition")  
Returns the Service name.

Returns:  Service name

Return type:  str

GetProtocol()[¶](#ApiClient.DiagServiceMappingItem.GetProtocol "Link to this definition")  
Returns the Protocol.

Returns:  Protocol (0 - UDS, 1 - KWP_2000)

Return type:  int

GetReferenceName()[¶](#ApiClient.DiagServiceMappingItem.GetReferenceName "Link to this definition")  
Returns the reference name of the mapping.

Returns:  The reference name of the mapping

Return type:  str

GetSubMapping()[¶](#ApiClient.DiagServiceMappingItem.GetSubMapping "Link to this definition")  
Returns contained Mapping or None if item does not support sub-mappings.

Returns:  Mapping with all submappings of the mapping item

Return type:  [`Mapping`](#ApiClient.Mapping "ApiClient.Mapping")

GetSystemIdentifier()[¶](#ApiClient.DiagServiceMappingItem.GetSystemIdentifier "Link to this definition")  
Returns the system identifier providing the currently mapped test quantity

Returns:  system identifier

Return type:  str

GetTargetPath()[¶](#ApiClient.DiagServiceMappingItem.GetTargetPath "Link to this definition")  
Returns the path this mapping item is currently pointing at

Returns:  complete path to the destination test quantity

Return type:  str

GetVariableType()[¶](#ApiClient.DiagServiceMappingItem.GetVariableType "Link to this definition")  
Returns the type of the target variable or None if target has no type.

Returns:  The type of the target variable. (e.g. VALUE, MATRIX, CURVE, …)

Return type:  str

IsAutogenerated()[¶](#ApiClient.DiagServiceMappingItem.IsAutogenerated "Link to this definition")  
Returns whether the mapping item is autogenerated.

Returns:  True, if autogenerated flag is set, else False

Return type:  boolean

SetCategory(*category*)[¶](#ApiClient.DiagServiceMappingItem.SetCategory "Link to this definition")  
Sets the category

Parameters:  **category** (*str*) – The new category to be used

SetDescription(*description*)[¶](#ApiClient.DiagServiceMappingItem.SetDescription "Link to this definition")  
Sets the description

Parameters:  **description** (*str*) – The new description to be used

SetReferenceName(*name*)[¶](#ApiClient.DiagServiceMappingItem.SetReferenceName "Link to this definition")  
Sets the reference name of the mapping.

Parameters:  **name** (*str*) – The reference name of the mapping

## ServiceMappingItem[¶](#servicemappingitem "Link to this heading")

*class* ServiceMappingItem[¶](#ApiClient.ServiceMappingItem "Link to this definition")  
Base classes

- [`MappingItem`](#ApiClient.MappingItem "ApiClient.MappingItem")

- [`CallableMappingItem`](#ApiClient.CallableMappingItem "ApiClient.CallableMappingItem")

Returned by

- [`MappingApi.CreateServiceMappingItem`](#ApiClient.MappingApi.CreateServiceMappingItem "ApiClient.MappingApi.CreateServiceMappingItem")

Clone()[¶](#ApiClient.ServiceMappingItem.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`ServiceMappingItem`](#ApiClient.ServiceMappingItem "ApiClient.ServiceMappingItem")

GetAccessType()[¶](#ApiClient.ServiceMappingItem.GetAccessType "Link to this definition")  
Returns a string identifying the mapping item’s type. (such as MODEL, BUS, MEASUREMENT, …)

Returns:  access type

Return type:  str

GetCategory()[¶](#ApiClient.ServiceMappingItem.GetCategory "Link to this definition")  
Returns the category

Returns:  Category

Return type:  str

GetDescription()[¶](#ApiClient.ServiceMappingItem.GetDescription "Link to this definition")  
Returns the description

Returns:  Description

Return type:  str

GetDisplayedType()[¶](#ApiClient.ServiceMappingItem.GetDisplayedType "Link to this definition")  
Returns a “nice” representation of the type as displayed in the “type” column of the mapping panel

Returns:  the displayed mapping type

Return type:  str

GetReferenceName()[¶](#ApiClient.ServiceMappingItem.GetReferenceName "Link to this definition")  
Returns the reference name of the mapping.

Returns:  The reference name of the mapping

Return type:  str

GetSubMapping()[¶](#ApiClient.ServiceMappingItem.GetSubMapping "Link to this definition")  
Returns contained Mapping or None if item does not support sub-mappings.

Returns:  Mapping with all submappings of the mapping item

Return type:  [`Mapping`](#ApiClient.Mapping "ApiClient.Mapping")

GetSystemIdentifier()[¶](#ApiClient.ServiceMappingItem.GetSystemIdentifier "Link to this definition")  
Returns the system identifier providing the currently mapped test quantity

Returns:  system identifier

Return type:  str

GetTargetPath()[¶](#ApiClient.ServiceMappingItem.GetTargetPath "Link to this definition")  
Returns the path this mapping item is currently pointing at

Returns:  complete path to the destination test quantity

Return type:  str

GetVariableType()[¶](#ApiClient.ServiceMappingItem.GetVariableType "Link to this definition")  
Returns the type of the target variable or None if target has no type.

Returns:  The type of the target variable. (e.g. VALUE, MATRIX, CURVE, …)

Return type:  str

IsAutogenerated()[¶](#ApiClient.ServiceMappingItem.IsAutogenerated "Link to this definition")  
Returns whether the mapping item is autogenerated.

Returns:  True, if autogenerated flag is set, else False

Return type:  boolean

SetCategory(*category*)[¶](#ApiClient.ServiceMappingItem.SetCategory "Link to this definition")  
Sets the category

Parameters:  **category** (*str*) – The new category to be used

SetDescription(*description*)[¶](#ApiClient.ServiceMappingItem.SetDescription "Link to this definition")  
Sets the description

Parameters:  **description** (*str*) – The new description to be used

SetReferenceName(*name*)[¶](#ApiClient.ServiceMappingItem.SetReferenceName "Link to this definition")  
Sets the reference name of the mapping.

Parameters:  **name** (*str*) – The reference name of the mapping

## DiagFaultMemoryMappingItem[¶](#diagfaultmemorymappingitem "Link to this heading")

*class* DiagFaultMemoryMappingItem[¶](#ApiClient.DiagFaultMemoryMappingItem "Link to this definition")  
Base class

[`MappingItem`](#ApiClient.MappingItem "ApiClient.MappingItem")

Returned by

- [`MappingApi.CreateDiagFaultMemoryMappingItem`](#ApiClient.MappingApi.CreateDiagFaultMemoryMappingItem "ApiClient.MappingApi.CreateDiagFaultMemoryMappingItem")

Clone()[¶](#ApiClient.DiagFaultMemoryMappingItem.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`DiagFaultMemoryMappingItem`](#ApiClient.DiagFaultMemoryMappingItem "ApiClient.DiagFaultMemoryMappingItem")

GetAccessType()[¶](#ApiClient.DiagFaultMemoryMappingItem.GetAccessType "Link to this definition")  
Returns a string identifying the mapping item’s type. (such as MODEL, BUS, MEASUREMENT, …)

Returns:  access type

Return type:  str

GetCategory()[¶](#ApiClient.DiagFaultMemoryMappingItem.GetCategory "Link to this definition")  
Returns the category

Returns:  Category

Return type:  str

GetDescription()[¶](#ApiClient.DiagFaultMemoryMappingItem.GetDescription "Link to this definition")  
Returns the description

Returns:  Description

Return type:  str

GetDisplayedType()[¶](#ApiClient.DiagFaultMemoryMappingItem.GetDisplayedType "Link to this definition")  
Returns a “nice” representation of the type as displayed in the “type” column of the mapping panel

Returns:  the displayed mapping type

Return type:  str

GetEcuKey()[¶](#ApiClient.DiagFaultMemoryMappingItem.GetEcuKey "Link to this definition")  
Returns the ECU key.

Returns:  ECU key

Return type:  str

GetReferenceName()[¶](#ApiClient.DiagFaultMemoryMappingItem.GetReferenceName "Link to this definition")  
Returns the reference name of the mapping.

Returns:  The reference name of the mapping

Return type:  str

GetSubMapping()[¶](#ApiClient.DiagFaultMemoryMappingItem.GetSubMapping "Link to this definition")  
Returns contained Mapping or None if item does not support sub-mappings.

Returns:  Mapping with all submappings of the mapping item

Return type:  [`Mapping`](#ApiClient.Mapping "ApiClient.Mapping")

GetSystemIdentifier()[¶](#ApiClient.DiagFaultMemoryMappingItem.GetSystemIdentifier "Link to this definition")  
Returns the system identifier providing the currently mapped test quantity

Returns:  system identifier

Return type:  str

GetTargetPath()[¶](#ApiClient.DiagFaultMemoryMappingItem.GetTargetPath "Link to this definition")  
Returns the path this mapping item is currently pointing at

Returns:  complete path to the destination test quantity

Return type:  str

GetVariableType()[¶](#ApiClient.DiagFaultMemoryMappingItem.GetVariableType "Link to this definition")  
Returns the type of the target variable or None if target has no type.

Returns:  The type of the target variable. (e.g. VALUE, MATRIX, CURVE, …)

Return type:  str

IsAutogenerated()[¶](#ApiClient.DiagFaultMemoryMappingItem.IsAutogenerated "Link to this definition")  
Returns whether the mapping item is autogenerated.

Returns:  True, if autogenerated flag is set, else False

Return type:  boolean

SetCategory(*category*)[¶](#ApiClient.DiagFaultMemoryMappingItem.SetCategory "Link to this definition")  
Sets the category

Parameters:  **category** (*str*) – The new category to be used

SetDescription(*description*)[¶](#ApiClient.DiagFaultMemoryMappingItem.SetDescription "Link to this definition")  
Sets the description

Parameters:  **description** (*str*) – The new description to be used

SetReferenceName(*name*)[¶](#ApiClient.DiagFaultMemoryMappingItem.SetReferenceName "Link to this definition")  
Sets the reference name of the mapping.

Parameters:  **name** (*str*) – The reference name of the mapping

## EdiabasVariableMappingItem[¶](#ediabasvariablemappingitem "Link to this heading")

*class* EdiabasVariableMappingItem[¶](#ApiClient.EdiabasVariableMappingItem "Link to this definition")  
Base class

[`MappingItem`](#ApiClient.MappingItem "ApiClient.MappingItem")

Returned by

- [`MappingApi.CreateEdiabasVariableMappingItem`](#ApiClient.MappingApi.CreateEdiabasVariableMappingItem "ApiClient.MappingApi.CreateEdiabasVariableMappingItem")

Clone()[¶](#ApiClient.EdiabasVariableMappingItem.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`EdiabasVariableMappingItem`](#ApiClient.EdiabasVariableMappingItem "ApiClient.EdiabasVariableMappingItem")

GetAccessType()[¶](#ApiClient.EdiabasVariableMappingItem.GetAccessType "Link to this definition")  
Returns a string identifying the mapping item’s type. (such as MODEL, BUS, MEASUREMENT, …)

Returns:  access type

Return type:  str

GetCategory()[¶](#ApiClient.EdiabasVariableMappingItem.GetCategory "Link to this definition")  
Returns the category

Returns:  Category

Return type:  str

GetDescription()[¶](#ApiClient.EdiabasVariableMappingItem.GetDescription "Link to this definition")  
Returns the description

Returns:  Description

Return type:  str

GetDisplayedType()[¶](#ApiClient.EdiabasVariableMappingItem.GetDisplayedType "Link to this definition")  
Returns a “nice” representation of the type as displayed in the “type” column of the mapping panel

Returns:  the displayed mapping type

Return type:  str

GetEcuKey()[¶](#ApiClient.EdiabasVariableMappingItem.GetEcuKey "Link to this definition")  
Returns the ECU key.

Returns:  ECU key

Return type:  str

GetJobComment()[¶](#ApiClient.EdiabasVariableMappingItem.GetJobComment "Link to this definition")  
Returns the job comment.

Returns:  Job comment

Return type:  str

GetJobName()[¶](#ApiClient.EdiabasVariableMappingItem.GetJobName "Link to this definition")  
Returns the job name.

Returns:  Job name

Return type:  str

GetReferenceName()[¶](#ApiClient.EdiabasVariableMappingItem.GetReferenceName "Link to this definition")  
Returns the reference name of the mapping.

Returns:  The reference name of the mapping

Return type:  str

GetSgbdName()[¶](#ApiClient.EdiabasVariableMappingItem.GetSgbdName "Link to this definition")  
Returns the SGBD name.

Returns:  SGBD name

Return type:  str

GetSubMapping()[¶](#ApiClient.EdiabasVariableMappingItem.GetSubMapping "Link to this definition")  
Returns contained Mapping or None if item does not support sub-mappings.

Returns:  Mapping with all submappings of the mapping item

Return type:  [`Mapping`](#ApiClient.Mapping "ApiClient.Mapping")

GetSystemIdentifier()[¶](#ApiClient.EdiabasVariableMappingItem.GetSystemIdentifier "Link to this definition")  
Returns the system identifier providing the currently mapped test quantity

Returns:  system identifier

Return type:  str

GetTargetPath()[¶](#ApiClient.EdiabasVariableMappingItem.GetTargetPath "Link to this definition")  
Returns the path this mapping item is currently pointing at

Returns:  complete path to the destination test quantity

Return type:  str

GetVariableType()[¶](#ApiClient.EdiabasVariableMappingItem.GetVariableType "Link to this definition")  
Returns the type of the target variable or None if target has no type.

Returns:  The type of the target variable. (e.g. VALUE, MATRIX, CURVE, …)

Return type:  str

IsAutogenerated()[¶](#ApiClient.EdiabasVariableMappingItem.IsAutogenerated "Link to this definition")  
Returns whether the mapping item is autogenerated.

Returns:  True, if autogenerated flag is set, else False

Return type:  boolean

SetCategory(*category*)[¶](#ApiClient.EdiabasVariableMappingItem.SetCategory "Link to this definition")  
Sets the category

Parameters:  **category** (*str*) – The new category to be used

SetDescription(*description*)[¶](#ApiClient.EdiabasVariableMappingItem.SetDescription "Link to this definition")  
Sets the description

Parameters:  **description** (*str*) – The new description to be used

SetReferenceName(*name*)[¶](#ApiClient.EdiabasVariableMappingItem.SetReferenceName "Link to this definition")  
Sets the reference name of the mapping.

Parameters:  **name** (*str*) – The reference name of the mapping

## EnvSimMappingItem[¶](#envsimmappingitem "Link to this heading")

*class* EnvSimMappingItem[¶](#ApiClient.EnvSimMappingItem "Link to this definition")  
Base class

[`MappingItem`](#ApiClient.MappingItem "ApiClient.MappingItem")

Returned by

- [`MappingApi.CreateEnvSimMappingItem`](#ApiClient.MappingApi.CreateEnvSimMappingItem "ApiClient.MappingApi.CreateEnvSimMappingItem")

Clone()[¶](#ApiClient.EnvSimMappingItem.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`EnvSimMappingItem`](#ApiClient.EnvSimMappingItem "ApiClient.EnvSimMappingItem")

GetAccessType()[¶](#ApiClient.EnvSimMappingItem.GetAccessType "Link to this definition")  
Returns a string identifying the mapping item’s type. (such as MODEL, BUS, MEASUREMENT, …)

Returns:  access type

Return type:  str

GetCategory()[¶](#ApiClient.EnvSimMappingItem.GetCategory "Link to this definition")  
Returns the category

Returns:  Category

Return type:  str

GetDescription()[¶](#ApiClient.EnvSimMappingItem.GetDescription "Link to this definition")  
Returns the description

Returns:  Description

Return type:  str

GetDisplayedType()[¶](#ApiClient.EnvSimMappingItem.GetDisplayedType "Link to this definition")  
Returns a “nice” representation of the type as displayed in the “type” column of the mapping panel

Returns:  the displayed mapping type

Return type:  str

GetReferenceName()[¶](#ApiClient.EnvSimMappingItem.GetReferenceName "Link to this definition")  
Returns the reference name of the mapping.

Returns:  The reference name of the mapping

Return type:  str

GetSubMapping()[¶](#ApiClient.EnvSimMappingItem.GetSubMapping "Link to this definition")  
Returns contained Mapping or None if item does not support sub-mappings.

Returns:  Mapping with all submappings of the mapping item

Return type:  [`Mapping`](#ApiClient.Mapping "ApiClient.Mapping")

GetSystemIdentifier()[¶](#ApiClient.EnvSimMappingItem.GetSystemIdentifier "Link to this definition")  
Returns the system identifier providing the currently mapped test quantity

Returns:  system identifier

Return type:  str

GetTargetPath()[¶](#ApiClient.EnvSimMappingItem.GetTargetPath "Link to this definition")  
Returns the path this mapping item is currently pointing at

Returns:  complete path to the destination test quantity

Return type:  str

GetVariableType()[¶](#ApiClient.EnvSimMappingItem.GetVariableType "Link to this definition")  
Returns the type of the target variable or None if target has no type.

Returns:  The type of the target variable. (e.g. VALUE, MATRIX, CURVE, …)

Return type:  str

IsAutogenerated()[¶](#ApiClient.EnvSimMappingItem.IsAutogenerated "Link to this definition")  
Returns whether the mapping item is autogenerated.

Returns:  True, if autogenerated flag is set, else False

Return type:  boolean

SetCategory(*category*)[¶](#ApiClient.EnvSimMappingItem.SetCategory "Link to this definition")  
Sets the category

Parameters:  **category** (*str*) – The new category to be used

SetDescription(*description*)[¶](#ApiClient.EnvSimMappingItem.SetDescription "Link to this definition")  
Sets the description

Parameters:  **description** (*str*) – The new description to be used

SetReferenceName(*name*)[¶](#ApiClient.EnvSimMappingItem.SetReferenceName "Link to this definition")  
Sets the reference name of the mapping.

Parameters:  **name** (*str*) – The reference name of the mapping

## EesPinVariableMappingItem[¶](#eespinvariablemappingitem "Link to this heading")

*class* EesPinVariableMappingItem[¶](#ApiClient.EesPinVariableMappingItem "Link to this definition")  
Base class

[`MappingItem`](#ApiClient.MappingItem "ApiClient.MappingItem")

Returned by

- [`MappingApi.CreateEesPinVariableMappingItem`](#ApiClient.MappingApi.CreateEesPinVariableMappingItem "ApiClient.MappingApi.CreateEesPinVariableMappingItem")

- [`TsEesError.GetEesPinVariableMappingItems`](TestStepApi.md#ApiClient.TsEesError.GetEesPinVariableMappingItems "ApiClient.TsEesError.GetEesPinVariableMappingItems")

Clone()[¶](#ApiClient.EesPinVariableMappingItem.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`EesPinVariableMappingItem`](#ApiClient.EesPinVariableMappingItem "ApiClient.EesPinVariableMappingItem")

GetAccessType()[¶](#ApiClient.EesPinVariableMappingItem.GetAccessType "Link to this definition")  
Returns a string identifying the mapping item’s type. (such as MODEL, BUS, MEASUREMENT, …)

Returns:  access type

Return type:  str

GetCategory()[¶](#ApiClient.EesPinVariableMappingItem.GetCategory "Link to this definition")  
Returns the category

Returns:  Category

Return type:  str

GetDescription()[¶](#ApiClient.EesPinVariableMappingItem.GetDescription "Link to this definition")  
Returns the description

Returns:  Description

Return type:  str

GetDisplayedType()[¶](#ApiClient.EesPinVariableMappingItem.GetDisplayedType "Link to this definition")  
Returns a “nice” representation of the type as displayed in the “type” column of the mapping panel

Returns:  the displayed mapping type

Return type:  str

GetReferenceName()[¶](#ApiClient.EesPinVariableMappingItem.GetReferenceName "Link to this definition")  
Returns the reference name of the mapping.

Returns:  The reference name of the mapping

Return type:  str

GetSubMapping()[¶](#ApiClient.EesPinVariableMappingItem.GetSubMapping "Link to this definition")  
Returns contained Mapping or None if item does not support sub-mappings.

Returns:  Mapping with all submappings of the mapping item

Return type:  [`Mapping`](#ApiClient.Mapping "ApiClient.Mapping")

GetSystemIdentifier()[¶](#ApiClient.EesPinVariableMappingItem.GetSystemIdentifier "Link to this definition")  
Returns the system identifier providing the currently mapped test quantity

Returns:  system identifier

Return type:  str

GetTargetPath()[¶](#ApiClient.EesPinVariableMappingItem.GetTargetPath "Link to this definition")  
Returns the path this mapping item is currently pointing at

Returns:  complete path to the destination test quantity

Return type:  str

GetVariableType()[¶](#ApiClient.EesPinVariableMappingItem.GetVariableType "Link to this definition")  
Returns the type of the target variable or None if target has no type.

Returns:  The type of the target variable. (e.g. VALUE, MATRIX, CURVE, …)

Return type:  str

IsAutogenerated()[¶](#ApiClient.EesPinVariableMappingItem.IsAutogenerated "Link to this definition")  
Returns whether the mapping item is autogenerated.

Returns:  True, if autogenerated flag is set, else False

Return type:  boolean

SetCategory(*category*)[¶](#ApiClient.EesPinVariableMappingItem.SetCategory "Link to this definition")  
Sets the category

Parameters:  **category** (*str*) – The new category to be used

SetDescription(*description*)[¶](#ApiClient.EesPinVariableMappingItem.SetDescription "Link to this definition")  
Sets the description

Parameters:  **description** (*str*) – The new description to be used

SetReferenceName(*name*)[¶](#ApiClient.EesPinVariableMappingItem.SetReferenceName "Link to this definition")  
Sets the reference name of the mapping.

Parameters:  **name** (*str*) – The reference name of the mapping

## LogFilterMessageMappingItem[¶](#logfiltermessagemappingitem "Link to this heading")

*class* LogFilterMessageMappingItem[¶](#ApiClient.LogFilterMessageMappingItem "Link to this definition")  
Base class

[`MappingItem`](#ApiClient.MappingItem "ApiClient.MappingItem")

Returned by

- [`MappingApi.CreateLogFilterMessageMappingItem`](#ApiClient.MappingApi.CreateLogFilterMessageMappingItem "ApiClient.MappingApi.CreateLogFilterMessageMappingItem")

Clone()[¶](#ApiClient.LogFilterMessageMappingItem.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`LogFilterMessageMappingItem`](#ApiClient.LogFilterMessageMappingItem "ApiClient.LogFilterMessageMappingItem")

GetAccessType()[¶](#ApiClient.LogFilterMessageMappingItem.GetAccessType "Link to this definition")  
Returns a string identifying the mapping item’s type. (such as MODEL, BUS, MEASUREMENT, …)

Returns:  access type

Return type:  str

GetCategory()[¶](#ApiClient.LogFilterMessageMappingItem.GetCategory "Link to this definition")  
Returns the category

Returns:  Category

Return type:  str

GetDescription()[¶](#ApiClient.LogFilterMessageMappingItem.GetDescription "Link to this definition")  
Returns the description

Returns:  Description

Return type:  str

GetDisplayedType()[¶](#ApiClient.LogFilterMessageMappingItem.GetDisplayedType "Link to this definition")  
Returns a “nice” representation of the type as displayed in the “type” column of the mapping panel

Returns:  the displayed mapping type

Return type:  str

GetEcuKey()[¶](#ApiClient.LogFilterMessageMappingItem.GetEcuKey "Link to this definition")  
Returns the ECU key.

Returns:  ECU key

Return type:  str

GetMessageName()[¶](#ApiClient.LogFilterMessageMappingItem.GetMessageName "Link to this definition")  
Returns the name of the message filter.

Returns:  message filter name

Return type:  str

GetReferenceName()[¶](#ApiClient.LogFilterMessageMappingItem.GetReferenceName "Link to this definition")  
Returns the reference name of the mapping.

Returns:  The reference name of the mapping

Return type:  str

GetSubMapping()[¶](#ApiClient.LogFilterMessageMappingItem.GetSubMapping "Link to this definition")  
Returns contained Mapping or None if item does not support sub-mappings.

Returns:  Mapping with all submappings of the mapping item

Return type:  [`Mapping`](#ApiClient.Mapping "ApiClient.Mapping")

GetSystemIdentifier()[¶](#ApiClient.LogFilterMessageMappingItem.GetSystemIdentifier "Link to this definition")  
Returns the system identifier providing the currently mapped test quantity

Returns:  system identifier

Return type:  str

GetTargetPath()[¶](#ApiClient.LogFilterMessageMappingItem.GetTargetPath "Link to this definition")  
Returns the path this mapping item is currently pointing at

Returns:  complete path to the destination test quantity

Return type:  str

GetVariableType()[¶](#ApiClient.LogFilterMessageMappingItem.GetVariableType "Link to this definition")  
Returns the type of the target variable or None if target has no type.

Returns:  The type of the target variable. (e.g. VALUE, MATRIX, CURVE, …)

Return type:  str

IsAutogenerated()[¶](#ApiClient.LogFilterMessageMappingItem.IsAutogenerated "Link to this definition")  
Returns whether the mapping item is autogenerated.

Returns:  True, if autogenerated flag is set, else False

Return type:  boolean

SetCategory(*category*)[¶](#ApiClient.LogFilterMessageMappingItem.SetCategory "Link to this definition")  
Sets the category

Parameters:  **category** (*str*) – The new category to be used

SetDescription(*description*)[¶](#ApiClient.LogFilterMessageMappingItem.SetDescription "Link to this definition")  
Sets the description

Parameters:  **description** (*str*) – The new description to be used

SetReferenceName(*name*)[¶](#ApiClient.LogFilterMessageMappingItem.SetReferenceName "Link to this definition")  
Sets the reference name of the mapping.

Parameters:  **name** (*str*) – The reference name of the mapping

## LoggingArgumentMappingItem[¶](#loggingargumentmappingitem "Link to this heading")

*class* LoggingArgumentMappingItem[¶](#ApiClient.LoggingArgumentMappingItem "Link to this definition")  
Base class

[`MappingItem`](#ApiClient.MappingItem "ApiClient.MappingItem")

Returned by

- [`MappingApi.CreateLoggingArgumentMappingItem`](#ApiClient.MappingApi.CreateLoggingArgumentMappingItem "ApiClient.MappingApi.CreateLoggingArgumentMappingItem")

Clone()[¶](#ApiClient.LoggingArgumentMappingItem.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`LoggingArgumentMappingItem`](#ApiClient.LoggingArgumentMappingItem "ApiClient.LoggingArgumentMappingItem")

GetAccessType()[¶](#ApiClient.LoggingArgumentMappingItem.GetAccessType "Link to this definition")  
Returns a string identifying the mapping item’s type. (such as MODEL, BUS, MEASUREMENT, …)

Returns:  access type

Return type:  str

GetArgumentName()[¶](#ApiClient.LoggingArgumentMappingItem.GetArgumentName "Link to this definition")  
Returns the name of the message argument.

Returns:  Name of the message argument or empty string if no name is set

Return type:  str

GetCategory()[¶](#ApiClient.LoggingArgumentMappingItem.GetCategory "Link to this definition")  
Returns the category

Returns:  Category

Return type:  str

GetDescription()[¶](#ApiClient.LoggingArgumentMappingItem.GetDescription "Link to this definition")  
Returns the description

Returns:  Description

Return type:  str

GetDisplayedType()[¶](#ApiClient.LoggingArgumentMappingItem.GetDisplayedType "Link to this definition")  
Returns a “nice” representation of the type as displayed in the “type” column of the mapping panel

Returns:  the displayed mapping type

Return type:  str

GetMessageName()[¶](#ApiClient.LoggingArgumentMappingItem.GetMessageName "Link to this definition")  
Returns the name of the message containing the argument.

Returns:  Name of the message containing the argument or empty string if no name is set

Return type:  str

GetReferenceName()[¶](#ApiClient.LoggingArgumentMappingItem.GetReferenceName "Link to this definition")  
Returns the reference name of the mapping.

Returns:  The reference name of the mapping

Return type:  str

GetSubMapping()[¶](#ApiClient.LoggingArgumentMappingItem.GetSubMapping "Link to this definition")  
Returns contained Mapping or None if item does not support sub-mappings.

Returns:  Mapping with all submappings of the mapping item

Return type:  [`Mapping`](#ApiClient.Mapping "ApiClient.Mapping")

GetSystemIdentifier()[¶](#ApiClient.LoggingArgumentMappingItem.GetSystemIdentifier "Link to this definition")  
Returns the system identifier providing the currently mapped test quantity

Returns:  system identifier

Return type:  str

GetSystemName()[¶](#ApiClient.LoggingArgumentMappingItem.GetSystemName "Link to this definition")  
Returns the name of the sending ECU system.

Returns:  Name of the sending ECU system or empty string if no system name is set

Return type:  str

GetTargetPath()[¶](#ApiClient.LoggingArgumentMappingItem.GetTargetPath "Link to this definition")  
Returns the path this mapping item is currently pointing at

Returns:  complete path to the destination test quantity

Return type:  str

GetVariableType()[¶](#ApiClient.LoggingArgumentMappingItem.GetVariableType "Link to this definition")  
Returns the type of the target variable or None if target has no type.

Returns:  The type of the target variable. (e.g. VALUE, MATRIX, CURVE, …)

Return type:  str

IsAutogenerated()[¶](#ApiClient.LoggingArgumentMappingItem.IsAutogenerated "Link to this definition")  
Returns whether the mapping item is autogenerated.

Returns:  True, if autogenerated flag is set, else False

Return type:  boolean

SetArgumentName(*argumentName*)[¶](#ApiClient.LoggingArgumentMappingItem.SetArgumentName "Link to this definition")  
Sets the name of the message argument.

Parameters:  **argumentName** (*str*) – Name of the message argument

SetCategory(*category*)[¶](#ApiClient.LoggingArgumentMappingItem.SetCategory "Link to this definition")  
Sets the category

Parameters:  **category** (*str*) – The new category to be used

SetDescription(*description*)[¶](#ApiClient.LoggingArgumentMappingItem.SetDescription "Link to this definition")  
Sets the description

Parameters:  **description** (*str*) – The new description to be used

SetMessageName(*messageName*)[¶](#ApiClient.LoggingArgumentMappingItem.SetMessageName "Link to this definition")  
Sets the name of the message containing the signal.

Parameters:  **messageName** (*str*) – Name of the frame containing the signal

SetReferenceName(*name*)[¶](#ApiClient.LoggingArgumentMappingItem.SetReferenceName "Link to this definition")  
Sets the reference name of the mapping.

Parameters:  **name** (*str*) – The reference name of the mapping

SetSystemName(*systemName*)[¶](#ApiClient.LoggingArgumentMappingItem.SetSystemName "Link to this definition")  
Sets the name of the sending ECU system.

Parameters:  **systemName** (*str*) – Name of the sending ECU system

## CalibrationMappingItem[¶](#calibrationmappingitem "Link to this heading")

*class* CalibrationMappingItem[¶](#ApiClient.CalibrationMappingItem "Link to this definition")  
Base class

[`MappingItem`](#ApiClient.MappingItem "ApiClient.MappingItem")

Returned by

- [`MappingApi.CreateCalibrationMappingItem`](#ApiClient.MappingApi.CreateCalibrationMappingItem "ApiClient.MappingApi.CreateCalibrationMappingItem")

Clone()[¶](#ApiClient.CalibrationMappingItem.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`CalibrationMappingItem`](#ApiClient.CalibrationMappingItem "ApiClient.CalibrationMappingItem")

GetAccessType()[¶](#ApiClient.CalibrationMappingItem.GetAccessType "Link to this definition")  
Returns a string identifying the mapping item’s type. (such as MODEL, BUS, MEASUREMENT, …)

Returns:  access type

Return type:  str

GetCategory()[¶](#ApiClient.CalibrationMappingItem.GetCategory "Link to this definition")  
Returns the category

Returns:  Category

Return type:  str

GetDescription()[¶](#ApiClient.CalibrationMappingItem.GetDescription "Link to this definition")  
Returns the description

Returns:  Description

Return type:  str

GetDisplayedType()[¶](#ApiClient.CalibrationMappingItem.GetDisplayedType "Link to this definition")  
Returns a “nice” representation of the type as displayed in the “type” column of the mapping panel

Returns:  the displayed mapping type

Return type:  str

GetReferenceName()[¶](#ApiClient.CalibrationMappingItem.GetReferenceName "Link to this definition")  
Returns the reference name of the mapping.

Returns:  The reference name of the mapping

Return type:  str

GetSubMapping()[¶](#ApiClient.CalibrationMappingItem.GetSubMapping "Link to this definition")  
Returns contained Mapping or None if item does not support sub-mappings.

Returns:  Mapping with all submappings of the mapping item

Return type:  [`Mapping`](#ApiClient.Mapping "ApiClient.Mapping")

GetSystemIdentifier()[¶](#ApiClient.CalibrationMappingItem.GetSystemIdentifier "Link to this definition")  
Returns the system identifier providing the currently mapped test quantity

Returns:  system identifier

Return type:  str

GetTargetPath()[¶](#ApiClient.CalibrationMappingItem.GetTargetPath "Link to this definition")  
Returns the path this mapping item is currently pointing at

Returns:  complete path to the destination test quantity

Return type:  str

GetVariableType()[¶](#ApiClient.CalibrationMappingItem.GetVariableType "Link to this definition")  
Returns the type of the target variable or None if target has no type.

Returns:  The type of the target variable. (e.g. VALUE, MATRIX, CURVE, …)

Return type:  str

IsAutogenerated()[¶](#ApiClient.CalibrationMappingItem.IsAutogenerated "Link to this definition")  
Returns whether the mapping item is autogenerated.

Returns:  True, if autogenerated flag is set, else False

Return type:  boolean

SetCategory(*category*)[¶](#ApiClient.CalibrationMappingItem.SetCategory "Link to this definition")  
Sets the category

Parameters:  **category** (*str*) – The new category to be used

SetDescription(*description*)[¶](#ApiClient.CalibrationMappingItem.SetDescription "Link to this definition")  
Sets the description

Parameters:  **description** (*str*) – The new description to be used

SetReferenceName(*name*)[¶](#ApiClient.CalibrationMappingItem.SetReferenceName "Link to this definition")  
Sets the reference name of the mapping.

Parameters:  **name** (*str*) – The reference name of the mapping

## MeasureMappingItem[¶](#measuremappingitem "Link to this heading")

*class* MeasureMappingItem[¶](#ApiClient.MeasureMappingItem "Link to this definition")  
Base class

[`MappingItem`](#ApiClient.MappingItem "ApiClient.MappingItem")

Returned by

- [`MappingApi.CreateMeasurementMappingItem`](#ApiClient.MappingApi.CreateMeasurementMappingItem "ApiClient.MappingApi.CreateMeasurementMappingItem")

Subclasses

- [`RunningValueMappingItem`](#ApiClient.RunningValueMappingItem "ApiClient.RunningValueMappingItem")

AllowOtherRaster(*forceRaster*)[¶](#ApiClient.MeasureMappingItem.AllowOtherRaster "Link to this definition")  
Set that the registration of the raster should be enforced

Parameters:  **forceRaster** (*bool*) – Set if the specified raster should be enforced or not

Clone()[¶](#ApiClient.MeasureMappingItem.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`MeasureMappingItem`](#ApiClient.MeasureMappingItem "ApiClient.MeasureMappingItem")

GetAccessType()[¶](#ApiClient.MeasureMappingItem.GetAccessType "Link to this definition")  
Returns a string identifying the mapping item’s type. (such as MODEL, BUS, MEASUREMENT, …)

Returns:  access type

Return type:  str

GetCategory()[¶](#ApiClient.MeasureMappingItem.GetCategory "Link to this definition")  
Returns the category

Returns:  Category

Return type:  str

GetDescription()[¶](#ApiClient.MeasureMappingItem.GetDescription "Link to this definition")  
Returns the description

Returns:  Description

Return type:  str

GetDisplayedType()[¶](#ApiClient.MeasureMappingItem.GetDisplayedType "Link to this definition")  
Returns a “nice” representation of the type as displayed in the “type” column of the mapping panel

Returns:  the displayed mapping type

Return type:  str

GetRaster()[¶](#ApiClient.MeasureMappingItem.GetRaster "Link to this definition")  
Returns the raster of the mapping item.

Returns:  Raster

Return type:  str

GetReferenceName()[¶](#ApiClient.MeasureMappingItem.GetReferenceName "Link to this definition")  
Returns the reference name of the mapping.

Returns:  The reference name of the mapping

Return type:  str

GetSubMapping()[¶](#ApiClient.MeasureMappingItem.GetSubMapping "Link to this definition")  
Returns contained Mapping or None if item does not support sub-mappings.

Returns:  Mapping with all submappings of the mapping item

Return type:  [`Mapping`](#ApiClient.Mapping "ApiClient.Mapping")

GetSystemIdentifier()[¶](#ApiClient.MeasureMappingItem.GetSystemIdentifier "Link to this definition")  
Returns the system identifier providing the currently mapped test quantity

Returns:  system identifier

Return type:  str

GetTargetPath()[¶](#ApiClient.MeasureMappingItem.GetTargetPath "Link to this definition")  
Returns the path this mapping item is currently pointing at

Returns:  complete path to the destination test quantity

Return type:  str

GetVariableType()[¶](#ApiClient.MeasureMappingItem.GetVariableType "Link to this definition")  
Returns the type of the target variable or None if target has no type.

Returns:  The type of the target variable. (e.g. VALUE, MATRIX, CURVE, …)

Return type:  str

IsAutogenerated()[¶](#ApiClient.MeasureMappingItem.IsAutogenerated "Link to this definition")  
Returns whether the mapping item is autogenerated.

Returns:  True, if autogenerated flag is set, else False

Return type:  boolean

IsOtherRasterAllowed()[¶](#ApiClient.MeasureMappingItem.IsOtherRasterAllowed "Link to this definition")  
Returns if the registration of the raster should be enforced

Returns:  Name of selected raster

Return type:  bool

SetCategory(*category*)[¶](#ApiClient.MeasureMappingItem.SetCategory "Link to this definition")  
Sets the category

Parameters:  **category** (*str*) – The new category to be used

SetDescription(*description*)[¶](#ApiClient.MeasureMappingItem.SetDescription "Link to this definition")  
Sets the description

Parameters:  **description** (*str*) – The new description to be used

SetRaster(*rasterName*)[¶](#ApiClient.MeasureMappingItem.SetRaster "Link to this definition")  
Sets the enumeration of the mapping item.

Parameters:  **rasterName** (*str*) – Raster to be set

Returns:  True if the raster has changed, else False

Return type:  bool

SetReferenceName(*name*)[¶](#ApiClient.MeasureMappingItem.SetReferenceName "Link to this definition")  
Sets the reference name of the mapping.

Parameters:  **name** (*str*) – The reference name of the mapping

## RunningValueMappingItem[¶](#runningvaluemappingitem "Link to this heading")

*class* RunningValueMappingItem[¶](#ApiClient.RunningValueMappingItem "Link to this definition")  
Base classes

- [`MappingItem`](#ApiClient.MappingItem "ApiClient.MappingItem")

- [`MeasureMappingItem`](#ApiClient.MeasureMappingItem "ApiClient.MeasureMappingItem")

Returned by

- [`MappingApi.CreateRunningValueMappingItem`](#ApiClient.MappingApi.CreateRunningValueMappingItem "ApiClient.MappingApi.CreateRunningValueMappingItem")

AllowOtherRaster(*forceRaster*)[¶](#ApiClient.RunningValueMappingItem.AllowOtherRaster "Link to this definition")  
Set that the registration of the raster should be enforced

Parameters:  **forceRaster** (*bool*) – Set if the specified raster should be enforced or not

Clone()[¶](#ApiClient.RunningValueMappingItem.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`RunningValueMappingItem`](#ApiClient.RunningValueMappingItem "ApiClient.RunningValueMappingItem")

GetAccessType()[¶](#ApiClient.RunningValueMappingItem.GetAccessType "Link to this definition")  
Returns a string identifying the mapping item’s type. (such as MODEL, BUS, MEASUREMENT, …)

Returns:  access type

Return type:  str

GetCategory()[¶](#ApiClient.RunningValueMappingItem.GetCategory "Link to this definition")  
Returns the category

Returns:  Category

Return type:  str

GetDescription()[¶](#ApiClient.RunningValueMappingItem.GetDescription "Link to this definition")  
Returns the description

Returns:  Description

Return type:  str

GetDisplayedType()[¶](#ApiClient.RunningValueMappingItem.GetDisplayedType "Link to this definition")  
Returns a “nice” representation of the type as displayed in the “type” column of the mapping panel

Returns:  the displayed mapping type

Return type:  str

GetRaster()[¶](#ApiClient.RunningValueMappingItem.GetRaster "Link to this definition")  
Returns the raster of the mapping item.

Returns:  Raster

Return type:  str

GetReferenceName()[¶](#ApiClient.RunningValueMappingItem.GetReferenceName "Link to this definition")  
Returns the reference name of the mapping.

Returns:  The reference name of the mapping

Return type:  str

GetSubMapping()[¶](#ApiClient.RunningValueMappingItem.GetSubMapping "Link to this definition")  
Returns contained Mapping or None if item does not support sub-mappings.

Returns:  Mapping with all submappings of the mapping item

Return type:  [`Mapping`](#ApiClient.Mapping "ApiClient.Mapping")

GetSystemIdentifier()[¶](#ApiClient.RunningValueMappingItem.GetSystemIdentifier "Link to this definition")  
Returns the system identifier providing the currently mapped test quantity

Returns:  system identifier

Return type:  str

GetTargetPath()[¶](#ApiClient.RunningValueMappingItem.GetTargetPath "Link to this definition")  
Returns the path this mapping item is currently pointing at

Returns:  complete path to the destination test quantity

Return type:  str

GetVariableType()[¶](#ApiClient.RunningValueMappingItem.GetVariableType "Link to this definition")  
Returns the type of the target variable or None if target has no type.

Returns:  The type of the target variable. (e.g. VALUE, MATRIX, CURVE, …)

Return type:  str

IsAutogenerated()[¶](#ApiClient.RunningValueMappingItem.IsAutogenerated "Link to this definition")  
Returns whether the mapping item is autogenerated.

Returns:  True, if autogenerated flag is set, else False

Return type:  boolean

IsOtherRasterAllowed()[¶](#ApiClient.RunningValueMappingItem.IsOtherRasterAllowed "Link to this definition")  
Returns if the registration of the raster should be enforced

Returns:  Name of selected raster

Return type:  bool

SetCategory(*category*)[¶](#ApiClient.RunningValueMappingItem.SetCategory "Link to this definition")  
Sets the category

Parameters:  **category** (*str*) – The new category to be used

SetDescription(*description*)[¶](#ApiClient.RunningValueMappingItem.SetDescription "Link to this definition")  
Sets the description

Parameters:  **description** (*str*) – The new description to be used

SetRaster(*rasterName*)[¶](#ApiClient.RunningValueMappingItem.SetRaster "Link to this definition")  
Sets the enumeration of the mapping item.

Parameters:  **rasterName** (*str*) – Raster to be set

Returns:  True if the raster has changed, else False

Return type:  bool

SetReferenceName(*name*)[¶](#ApiClient.RunningValueMappingItem.SetReferenceName "Link to this definition")  
Sets the reference name of the mapping.

Parameters:  **name** (*str*) – The reference name of the mapping

## ModelMappingItem[¶](#modelmappingitem "Link to this heading")

*class* ModelMappingItem[¶](#ApiClient.ModelMappingItem "Link to this definition")  
Base class

[`MappingItem`](#ApiClient.MappingItem "ApiClient.MappingItem")

Returned by

- [`MappingApi.CreateModelMappingItem`](#ApiClient.MappingApi.CreateModelMappingItem "ApiClient.MappingApi.CreateModelMappingItem")

AddEnumeration(*text*, *value*)[¶](#ApiClient.ModelMappingItem.AddEnumeration "Link to this definition")  
Adds a (text: value) pair to an existing enumeration. Creates a new enumeration if none exists.

Parameters:  - **text** (*str*) – Text to show instead of the value

- **value** (*int*) – Value that should be mapped

AllowOtherRaster(*forceRaster*)[¶](#ApiClient.ModelMappingItem.AllowOtherRaster "Link to this definition")  
Set that the registration of the raster should be enforced

Parameters:  **forceRaster** (*bool*) – Set if the specified raster should be enforced or not

Clone()[¶](#ApiClient.ModelMappingItem.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`ModelMappingItem`](#ApiClient.ModelMappingItem "ApiClient.ModelMappingItem")

GetAccessType()[¶](#ApiClient.ModelMappingItem.GetAccessType "Link to this definition")  
Returns a string identifying the mapping item’s type. (such as MODEL, BUS, MEASUREMENT, …)

Returns:  access type

Return type:  str

GetCategory()[¶](#ApiClient.ModelMappingItem.GetCategory "Link to this definition")  
Returns the category

Returns:  Category

Return type:  str

GetDataType()[¶](#ApiClient.ModelMappingItem.GetDataType "Link to this definition")  
Returns the data type.

Returns:  The data type or an empty string if the mapping item does not support enforcing a data type.

Return type:  str

GetDescription()[¶](#ApiClient.ModelMappingItem.GetDescription "Link to this definition")  
Returns the description

Returns:  Description

Return type:  str

GetDisplayedType()[¶](#ApiClient.ModelMappingItem.GetDisplayedType "Link to this definition")  
Returns a “nice” representation of the type as displayed in the “type” column of the mapping panel

Returns:  the displayed mapping type

Return type:  str

GetEnumeration()[¶](#ApiClient.ModelMappingItem.GetEnumeration "Link to this definition")  
Returns the enumeration of the mapping item.

Returns:  Dictionary with the (text: value) pairs.

Return type:  dict[str, int]

GetFallbackUnit()[¶](#ApiClient.ModelMappingItem.GetFallbackUnit "Link to this definition")  
Returns name of the fallback unit of the mapping item.

Returns:  The fallback unit name

Return type:  str

GetRaster()[¶](#ApiClient.ModelMappingItem.GetRaster "Link to this definition")  
Returns the raster of the mapping item.

Returns:  Raster

Return type:  str

GetReferenceName()[¶](#ApiClient.ModelMappingItem.GetReferenceName "Link to this definition")  
Returns the reference name of the mapping.

Returns:  The reference name of the mapping

Return type:  str

GetSubMapping()[¶](#ApiClient.ModelMappingItem.GetSubMapping "Link to this definition")  
Returns contained Mapping or None if item does not support sub-mappings.

Returns:  Mapping with all submappings of the mapping item

Return type:  [`Mapping`](#ApiClient.Mapping "ApiClient.Mapping")

GetSystemIdentifier()[¶](#ApiClient.ModelMappingItem.GetSystemIdentifier "Link to this definition")  
Returns the system identifier providing the currently mapped test quantity

Returns:  system identifier

Return type:  str

GetTargetPath()[¶](#ApiClient.ModelMappingItem.GetTargetPath "Link to this definition")  
Returns the path this mapping item is currently pointing at

Returns:  complete path to the destination test quantity

Return type:  str

GetUnit()[¶](#ApiClient.ModelMappingItem.GetUnit "Link to this definition")  
Returns the unit of the mapping item. The returned unit depends on the current state of ecu.test. If the mapping item points to an invalid path (e.g. if no configuration has been started) this method will always return ‘dont care’. If the mapping is valid this method returns the unit provided by the corresponding model tool. If the tool does not provide a unit, the fallback unit will be returned.

Returns:  The unit of the mapping item. May be None if the unit is not set.

Return type:  str

GetVariableType()[¶](#ApiClient.ModelMappingItem.GetVariableType "Link to this definition")  
Returns the type of the target variable or None if target has no type.

Returns:  The type of the target variable. (e.g. VALUE, MATRIX, CURVE, …)

Return type:  str

IsAutogenerated()[¶](#ApiClient.ModelMappingItem.IsAutogenerated "Link to this definition")  
Returns whether the mapping item is autogenerated.

Returns:  True, if autogenerated flag is set, else False

Return type:  boolean

IsOtherRasterAllowed()[¶](#ApiClient.ModelMappingItem.IsOtherRasterAllowed "Link to this definition")  
Returns if the registration of the raster should be enforced

Returns:  Name of selected raster

Return type:  bool

RemoveEnumeration()[¶](#ApiClient.ModelMappingItem.RemoveEnumeration "Link to this definition")  
Removes the enumeration of the mapping item.

SetCategory(*category*)[¶](#ApiClient.ModelMappingItem.SetCategory "Link to this definition")  
Sets the category

Parameters:  **category** (*str*) – The new category to be used

SetDescription(*description*)[¶](#ApiClient.ModelMappingItem.SetDescription "Link to this definition")  
Sets the description

Parameters:  **description** (*str*) – The new description to be used

SetEnumeration(*vtabDict*)[¶](#ApiClient.ModelMappingItem.SetEnumeration "Link to this definition")  
Sets the enumeration of the mapping item.

Parameters:  **vtabDict** (*dict[str,* *int]*) – Dictionary with the (text: value) pairs.

SetFallbackUnit(*reference*)[¶](#ApiClient.ModelMappingItem.SetFallbackUnit "Link to this definition")  
Sets the fallback unit that will be used if the model does not provide a unit for this variable. An empty string deletes the currently set fallback unit. You can find a full list of units in the .workspace folder in “units.spec” in the ecu.test workspace. Please specify the short name of the corresponding unit.

Parameters:  **reference** (*str*) – The unit reference (short name)

SetRaster(*rasterName*)[¶](#ApiClient.ModelMappingItem.SetRaster "Link to this definition")  
Sets the enumeration of the mapping item.

Parameters:  **rasterName** (*str*) – Raster to be set

Returns:  True if the raster has changed, else False

Return type:  bool

SetReferenceName(*name*)[¶](#ApiClient.ModelMappingItem.SetReferenceName "Link to this definition")  
Sets the reference name of the mapping.

Parameters:  **name** (*str*) – The reference name of the mapping

## AudioChannelMappingItem[¶](#audiochannelmappingitem "Link to this heading")

*class* AudioChannelMappingItem[¶](#ApiClient.AudioChannelMappingItem "Link to this definition")  
Base class

[`MappingItem`](#ApiClient.MappingItem "ApiClient.MappingItem")

Returned by

- [`MappingApi.CreateAudioChannelMappingItem`](#ApiClient.MappingApi.CreateAudioChannelMappingItem "ApiClient.MappingApi.CreateAudioChannelMappingItem")

Clone()[¶](#ApiClient.AudioChannelMappingItem.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`AudioChannelMappingItem`](#ApiClient.AudioChannelMappingItem "ApiClient.AudioChannelMappingItem")

GetAccessType()[¶](#ApiClient.AudioChannelMappingItem.GetAccessType "Link to this definition")  
Returns a string identifying the mapping item’s type. (such as MODEL, BUS, MEASUREMENT, …)

Returns:  access type

Return type:  str

GetCategory()[¶](#ApiClient.AudioChannelMappingItem.GetCategory "Link to this definition")  
Returns the category

Returns:  Category

Return type:  str

GetDescription()[¶](#ApiClient.AudioChannelMappingItem.GetDescription "Link to this definition")  
Returns the description

Returns:  Description

Return type:  str

GetDisplayedType()[¶](#ApiClient.AudioChannelMappingItem.GetDisplayedType "Link to this definition")  
Returns a “nice” representation of the type as displayed in the “type” column of the mapping panel

Returns:  the displayed mapping type

Return type:  str

GetReferenceName()[¶](#ApiClient.AudioChannelMappingItem.GetReferenceName "Link to this definition")  
Returns the reference name of the mapping.

Returns:  The reference name of the mapping

Return type:  str

GetSubMapping()[¶](#ApiClient.AudioChannelMappingItem.GetSubMapping "Link to this definition")  
Returns contained Mapping or None if item does not support sub-mappings.

Returns:  Mapping with all submappings of the mapping item

Return type:  [`Mapping`](#ApiClient.Mapping "ApiClient.Mapping")

GetSystemIdentifier()[¶](#ApiClient.AudioChannelMappingItem.GetSystemIdentifier "Link to this definition")  
Returns the system identifier providing the currently mapped test quantity

Returns:  system identifier

Return type:  str

GetTargetPath()[¶](#ApiClient.AudioChannelMappingItem.GetTargetPath "Link to this definition")  
Returns the path this mapping item is currently pointing at

Returns:  complete path to the destination test quantity

Return type:  str

GetVariableType()[¶](#ApiClient.AudioChannelMappingItem.GetVariableType "Link to this definition")  
Returns the type of the target variable or None if target has no type.

Returns:  The type of the target variable. (e.g. VALUE, MATRIX, CURVE, …)

Return type:  str

IsAutogenerated()[¶](#ApiClient.AudioChannelMappingItem.IsAutogenerated "Link to this definition")  
Returns whether the mapping item is autogenerated.

Returns:  True, if autogenerated flag is set, else False

Return type:  boolean

SetCategory(*category*)[¶](#ApiClient.AudioChannelMappingItem.SetCategory "Link to this definition")  
Sets the category

Parameters:  **category** (*str*) – The new category to be used

SetDescription(*description*)[¶](#ApiClient.AudioChannelMappingItem.SetDescription "Link to this definition")  
Sets the description

Parameters:  **description** (*str*) – The new description to be used

SetReferenceName(*name*)[¶](#ApiClient.AudioChannelMappingItem.SetReferenceName "Link to this definition")  
Sets the reference name of the mapping.

Parameters:  **name** (*str*) – The reference name of the mapping

## AudioDeviceMappingItem[¶](#audiodevicemappingitem "Link to this heading")

*class* AudioDeviceMappingItem[¶](#ApiClient.AudioDeviceMappingItem "Link to this definition")  
Base class

[`MappingItem`](#ApiClient.MappingItem "ApiClient.MappingItem")

Returned by

- [`MappingApi.CreateAudioDeviceMappingItem`](#ApiClient.MappingApi.CreateAudioDeviceMappingItem "ApiClient.MappingApi.CreateAudioDeviceMappingItem")

Clone()[¶](#ApiClient.AudioDeviceMappingItem.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`AudioDeviceMappingItem`](#ApiClient.AudioDeviceMappingItem "ApiClient.AudioDeviceMappingItem")

GetAccessType()[¶](#ApiClient.AudioDeviceMappingItem.GetAccessType "Link to this definition")  
Returns a string identifying the mapping item’s type. (such as MODEL, BUS, MEASUREMENT, …)

Returns:  access type

Return type:  str

GetCategory()[¶](#ApiClient.AudioDeviceMappingItem.GetCategory "Link to this definition")  
Returns the category

Returns:  Category

Return type:  str

GetDescription()[¶](#ApiClient.AudioDeviceMappingItem.GetDescription "Link to this definition")  
Returns the description

Returns:  Description

Return type:  str

GetDisplayedType()[¶](#ApiClient.AudioDeviceMappingItem.GetDisplayedType "Link to this definition")  
Returns a “nice” representation of the type as displayed in the “type” column of the mapping panel

Returns:  the displayed mapping type

Return type:  str

GetReferenceName()[¶](#ApiClient.AudioDeviceMappingItem.GetReferenceName "Link to this definition")  
Returns the reference name of the mapping.

Returns:  The reference name of the mapping

Return type:  str

GetSubMapping()[¶](#ApiClient.AudioDeviceMappingItem.GetSubMapping "Link to this definition")  
Returns contained Mapping or None if item does not support sub-mappings.

Returns:  Mapping with all submappings of the mapping item

Return type:  [`Mapping`](#ApiClient.Mapping "ApiClient.Mapping")

GetSystemIdentifier()[¶](#ApiClient.AudioDeviceMappingItem.GetSystemIdentifier "Link to this definition")  
Returns the system identifier providing the currently mapped test quantity

Returns:  system identifier

Return type:  str

GetTargetPath()[¶](#ApiClient.AudioDeviceMappingItem.GetTargetPath "Link to this definition")  
Returns the path this mapping item is currently pointing at

Returns:  complete path to the destination test quantity

Return type:  str

GetVariableType()[¶](#ApiClient.AudioDeviceMappingItem.GetVariableType "Link to this definition")  
Returns the type of the target variable or None if target has no type.

Returns:  The type of the target variable. (e.g. VALUE, MATRIX, CURVE, …)

Return type:  str

IsAutogenerated()[¶](#ApiClient.AudioDeviceMappingItem.IsAutogenerated "Link to this definition")  
Returns whether the mapping item is autogenerated.

Returns:  True, if autogenerated flag is set, else False

Return type:  boolean

SetCategory(*category*)[¶](#ApiClient.AudioDeviceMappingItem.SetCategory "Link to this definition")  
Sets the category

Parameters:  **category** (*str*) – The new category to be used

SetDescription(*description*)[¶](#ApiClient.AudioDeviceMappingItem.SetDescription "Link to this definition")  
Sets the description

Parameters:  **description** (*str*) – The new description to be used

SetReferenceName(*name*)[¶](#ApiClient.AudioDeviceMappingItem.SetReferenceName "Link to this definition")  
Sets the reference name of the mapping.

Parameters:  **name** (*str*) – The reference name of the mapping

## GenericAudioMappingItem[¶](#genericaudiomappingitem "Link to this heading")

*class* GenericAudioMappingItem[¶](#ApiClient.GenericAudioMappingItem "Link to this definition")  
Base class

[`MappingItem`](#ApiClient.MappingItem "ApiClient.MappingItem")

Clone()[¶](#ApiClient.GenericAudioMappingItem.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`GenericAudioMappingItem`](#ApiClient.GenericAudioMappingItem "ApiClient.GenericAudioMappingItem")

GetAccessType()[¶](#ApiClient.GenericAudioMappingItem.GetAccessType "Link to this definition")  
Returns a string identifying the mapping item’s type. (such as MODEL, BUS, MEASUREMENT, …)

Returns:  access type

Return type:  str

GetCategory()[¶](#ApiClient.GenericAudioMappingItem.GetCategory "Link to this definition")  
Returns the category

Returns:  Category

Return type:  str

GetDescription()[¶](#ApiClient.GenericAudioMappingItem.GetDescription "Link to this definition")  
Returns the description

Returns:  Description

Return type:  str

GetDisplayedType()[¶](#ApiClient.GenericAudioMappingItem.GetDisplayedType "Link to this definition")  
Returns a “nice” representation of the type as displayed in the “type” column of the mapping panel

Returns:  the displayed mapping type

Return type:  str

GetReferenceName()[¶](#ApiClient.GenericAudioMappingItem.GetReferenceName "Link to this definition")  
Returns the reference name of the mapping.

Returns:  The reference name of the mapping

Return type:  str

GetSubMapping()[¶](#ApiClient.GenericAudioMappingItem.GetSubMapping "Link to this definition")  
Returns contained Mapping or None if item does not support sub-mappings.

Returns:  Mapping with all submappings of the mapping item

Return type:  [`Mapping`](#ApiClient.Mapping "ApiClient.Mapping")

GetSystemIdentifier()[¶](#ApiClient.GenericAudioMappingItem.GetSystemIdentifier "Link to this definition")  
Returns the system identifier providing the currently mapped test quantity

Returns:  system identifier

Return type:  str

GetTargetPath()[¶](#ApiClient.GenericAudioMappingItem.GetTargetPath "Link to this definition")  
Returns the path this mapping item is currently pointing at

Returns:  complete path to the destination test quantity

Return type:  str

GetVariableType()[¶](#ApiClient.GenericAudioMappingItem.GetVariableType "Link to this definition")  
Returns the type of the target variable or None if target has no type.

Returns:  The type of the target variable. (e.g. VALUE, MATRIX, CURVE, …)

Return type:  str

IsAutogenerated()[¶](#ApiClient.GenericAudioMappingItem.IsAutogenerated "Link to this definition")  
Returns whether the mapping item is autogenerated.

Returns:  True, if autogenerated flag is set, else False

Return type:  boolean

SetCategory(*category*)[¶](#ApiClient.GenericAudioMappingItem.SetCategory "Link to this definition")  
Sets the category

Parameters:  **category** (*str*) – The new category to be used

SetDescription(*description*)[¶](#ApiClient.GenericAudioMappingItem.SetDescription "Link to this definition")  
Sets the description

Parameters:  **description** (*str*) – The new description to be used

SetReferenceName(*name*)[¶](#ApiClient.GenericAudioMappingItem.SetReferenceName "Link to this definition")  
Sets the reference name of the mapping.

Parameters:  **name** (*str*) – The reference name of the mapping

## GenericImageMappingItem[¶](#genericimagemappingitem "Link to this heading")

*class* GenericImageMappingItem[¶](#ApiClient.GenericImageMappingItem "Link to this definition")  
Base class

[`MappingItem`](#ApiClient.MappingItem "ApiClient.MappingItem")

Clone()[¶](#ApiClient.GenericImageMappingItem.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`GenericImageMappingItem`](#ApiClient.GenericImageMappingItem "ApiClient.GenericImageMappingItem")

GetAccessType()[¶](#ApiClient.GenericImageMappingItem.GetAccessType "Link to this definition")  
Returns a string identifying the mapping item’s type. (such as MODEL, BUS, MEASUREMENT, …)

Returns:  access type

Return type:  str

GetCategory()[¶](#ApiClient.GenericImageMappingItem.GetCategory "Link to this definition")  
Returns the category

Returns:  Category

Return type:  str

GetDescription()[¶](#ApiClient.GenericImageMappingItem.GetDescription "Link to this definition")  
Returns the description

Returns:  Description

Return type:  str

GetDisplayedType()[¶](#ApiClient.GenericImageMappingItem.GetDisplayedType "Link to this definition")  
Returns a “nice” representation of the type as displayed in the “type” column of the mapping panel

Returns:  the displayed mapping type

Return type:  str

GetReferenceName()[¶](#ApiClient.GenericImageMappingItem.GetReferenceName "Link to this definition")  
Returns the reference name of the mapping.

Returns:  The reference name of the mapping

Return type:  str

GetSubMapping()[¶](#ApiClient.GenericImageMappingItem.GetSubMapping "Link to this definition")  
Returns contained Mapping or None if item does not support sub-mappings.

Returns:  Mapping with all submappings of the mapping item

Return type:  [`Mapping`](#ApiClient.Mapping "ApiClient.Mapping")

GetSystemIdentifier()[¶](#ApiClient.GenericImageMappingItem.GetSystemIdentifier "Link to this definition")  
Returns the system identifier providing the currently mapped test quantity

Returns:  system identifier

Return type:  str

GetTargetPath()[¶](#ApiClient.GenericImageMappingItem.GetTargetPath "Link to this definition")  
Returns the path this mapping item is currently pointing at

Returns:  complete path to the destination test quantity

Return type:  str

GetVariableType()[¶](#ApiClient.GenericImageMappingItem.GetVariableType "Link to this definition")  
Returns the type of the target variable or None if target has no type.

Returns:  The type of the target variable. (e.g. VALUE, MATRIX, CURVE, …)

Return type:  str

IsAutogenerated()[¶](#ApiClient.GenericImageMappingItem.IsAutogenerated "Link to this definition")  
Returns whether the mapping item is autogenerated.

Returns:  True, if autogenerated flag is set, else False

Return type:  boolean

SetCategory(*category*)[¶](#ApiClient.GenericImageMappingItem.SetCategory "Link to this definition")  
Sets the category

Parameters:  **category** (*str*) – The new category to be used

SetDescription(*description*)[¶](#ApiClient.GenericImageMappingItem.SetDescription "Link to this definition")  
Sets the description

Parameters:  **description** (*str*) – The new description to be used

SetReferenceName(*name*)[¶](#ApiClient.GenericImageMappingItem.SetReferenceName "Link to this definition")  
Sets the reference name of the mapping.

Parameters:  **name** (*str*) – The reference name of the mapping

## ImageMappingItem[¶](#imagemappingitem "Link to this heading")

*class* ImageMappingItem[¶](#ApiClient.ImageMappingItem "Link to this definition")  
Base class

[`MappingItem`](#ApiClient.MappingItem "ApiClient.MappingItem")

Returned by

- [`MappingApi.CreateImageMappingItem`](#ApiClient.MappingApi.CreateImageMappingItem "ApiClient.MappingApi.CreateImageMappingItem")

Clone()[¶](#ApiClient.ImageMappingItem.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`ImageMappingItem`](#ApiClient.ImageMappingItem "ApiClient.ImageMappingItem")

GetAccessType()[¶](#ApiClient.ImageMappingItem.GetAccessType "Link to this definition")  
Returns a string identifying the mapping item’s type. (such as MODEL, BUS, MEASUREMENT, …)

Returns:  access type

Return type:  str

GetCategory()[¶](#ApiClient.ImageMappingItem.GetCategory "Link to this definition")  
Returns the category

Returns:  Category

Return type:  str

GetDescription()[¶](#ApiClient.ImageMappingItem.GetDescription "Link to this definition")  
Returns the description

Returns:  Description

Return type:  str

GetDisplayedType()[¶](#ApiClient.ImageMappingItem.GetDisplayedType "Link to this definition")  
Returns a “nice” representation of the type as displayed in the “type” column of the mapping panel

Returns:  the displayed mapping type

Return type:  str

GetReferenceName()[¶](#ApiClient.ImageMappingItem.GetReferenceName "Link to this definition")  
Returns the reference name of the mapping.

Returns:  The reference name of the mapping

Return type:  str

GetSubMapping()[¶](#ApiClient.ImageMappingItem.GetSubMapping "Link to this definition")  
Returns contained Mapping or None if item does not support sub-mappings.

Returns:  Mapping with all submappings of the mapping item

Return type:  [`Mapping`](#ApiClient.Mapping "ApiClient.Mapping")

GetSystemIdentifier()[¶](#ApiClient.ImageMappingItem.GetSystemIdentifier "Link to this definition")  
Returns the system identifier providing the currently mapped test quantity

Returns:  system identifier

Return type:  str

GetTargetPath()[¶](#ApiClient.ImageMappingItem.GetTargetPath "Link to this definition")  
Returns the path this mapping item is currently pointing at

Returns:  complete path to the destination test quantity

Return type:  str

GetVariableType()[¶](#ApiClient.ImageMappingItem.GetVariableType "Link to this definition")  
Returns the type of the target variable or None if target has no type.

Returns:  The type of the target variable. (e.g. VALUE, MATRIX, CURVE, …)

Return type:  str

IsAutogenerated()[¶](#ApiClient.ImageMappingItem.IsAutogenerated "Link to this definition")  
Returns whether the mapping item is autogenerated.

Returns:  True, if autogenerated flag is set, else False

Return type:  boolean

SetCategory(*category*)[¶](#ApiClient.ImageMappingItem.SetCategory "Link to this definition")  
Sets the category

Parameters:  **category** (*str*) – The new category to be used

SetDescription(*description*)[¶](#ApiClient.ImageMappingItem.SetDescription "Link to this definition")  
Sets the description

Parameters:  **description** (*str*) – The new description to be used

SetReferenceName(*name*)[¶](#ApiClient.ImageMappingItem.SetReferenceName "Link to this definition")  
Sets the reference name of the mapping.

Parameters:  **name** (*str*) – The reference name of the mapping

## ServiceEventLeafMappingItem[¶](#serviceeventleafmappingitem "Link to this heading")

*class* ServiceEventLeafMappingItem[¶](#ApiClient.ServiceEventLeafMappingItem "Link to this definition")  
Base class

[`MappingItem`](#ApiClient.MappingItem "ApiClient.MappingItem")

Returned by

- [`MappingApi.CreateServiceEventLeafMappingItem`](#ApiClient.MappingApi.CreateServiceEventLeafMappingItem "ApiClient.MappingApi.CreateServiceEventLeafMappingItem")

Clone()[¶](#ApiClient.ServiceEventLeafMappingItem.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`ServiceEventLeafMappingItem`](#ApiClient.ServiceEventLeafMappingItem "ApiClient.ServiceEventLeafMappingItem")

GetAccessType()[¶](#ApiClient.ServiceEventLeafMappingItem.GetAccessType "Link to this definition")  
Returns a string identifying the mapping item’s type. (such as MODEL, BUS, MEASUREMENT, …)

Returns:  access type

Return type:  str

GetCategory()[¶](#ApiClient.ServiceEventLeafMappingItem.GetCategory "Link to this definition")  
Returns the category

Returns:  Category

Return type:  str

GetDescription()[¶](#ApiClient.ServiceEventLeafMappingItem.GetDescription "Link to this definition")  
Returns the description

Returns:  Description

Return type:  str

GetDisplayedType()[¶](#ApiClient.ServiceEventLeafMappingItem.GetDisplayedType "Link to this definition")  
Returns a “nice” representation of the type as displayed in the “type” column of the mapping panel

Returns:  the displayed mapping type

Return type:  str

GetReferenceName()[¶](#ApiClient.ServiceEventLeafMappingItem.GetReferenceName "Link to this definition")  
Returns the reference name of the mapping.

Returns:  The reference name of the mapping

Return type:  str

GetSubMapping()[¶](#ApiClient.ServiceEventLeafMappingItem.GetSubMapping "Link to this definition")  
Returns contained Mapping or None if item does not support sub-mappings.

Returns:  Mapping with all submappings of the mapping item

Return type:  [`Mapping`](#ApiClient.Mapping "ApiClient.Mapping")

GetSystemIdentifier()[¶](#ApiClient.ServiceEventLeafMappingItem.GetSystemIdentifier "Link to this definition")  
Returns the system identifier providing the currently mapped test quantity

Returns:  system identifier

Return type:  str

GetTargetPath()[¶](#ApiClient.ServiceEventLeafMappingItem.GetTargetPath "Link to this definition")  
Returns the path this mapping item is currently pointing at

Returns:  complete path to the destination test quantity

Return type:  str

GetVariableType()[¶](#ApiClient.ServiceEventLeafMappingItem.GetVariableType "Link to this definition")  
Returns the type of the target variable or None if target has no type.

Returns:  The type of the target variable. (e.g. VALUE, MATRIX, CURVE, …)

Return type:  str

IsAutogenerated()[¶](#ApiClient.ServiceEventLeafMappingItem.IsAutogenerated "Link to this definition")  
Returns whether the mapping item is autogenerated.

Returns:  True, if autogenerated flag is set, else False

Return type:  boolean

SetCategory(*category*)[¶](#ApiClient.ServiceEventLeafMappingItem.SetCategory "Link to this definition")  
Sets the category

Parameters:  **category** (*str*) – The new category to be used

SetDescription(*description*)[¶](#ApiClient.ServiceEventLeafMappingItem.SetDescription "Link to this definition")  
Sets the description

Parameters:  **description** (*str*) – The new description to be used

SetReferenceName(*name*)[¶](#ApiClient.ServiceEventLeafMappingItem.SetReferenceName "Link to this definition")  
Sets the reference name of the mapping.

Parameters:  **name** (*str*) – The reference name of the mapping

## ServiceMethodReturnMappingItem[¶](#servicemethodreturnmappingitem "Link to this heading")

*class* ServiceMethodReturnMappingItem[¶](#ApiClient.ServiceMethodReturnMappingItem "Link to this definition")  
Base class

[`MappingItem`](#ApiClient.MappingItem "ApiClient.MappingItem")

Returned by

- [`MappingApi.CreateServiceMethodReturnMappingItem`](#ApiClient.MappingApi.CreateServiceMethodReturnMappingItem "ApiClient.MappingApi.CreateServiceMethodReturnMappingItem")

Clone()[¶](#ApiClient.ServiceMethodReturnMappingItem.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`ServiceMethodReturnMappingItem`](#ApiClient.ServiceMethodReturnMappingItem "ApiClient.ServiceMethodReturnMappingItem")

GetAccessType()[¶](#ApiClient.ServiceMethodReturnMappingItem.GetAccessType "Link to this definition")  
Returns a string identifying the mapping item’s type. (such as MODEL, BUS, MEASUREMENT, …)

Returns:  access type

Return type:  str

GetCategory()[¶](#ApiClient.ServiceMethodReturnMappingItem.GetCategory "Link to this definition")  
Returns the category

Returns:  Category

Return type:  str

GetDescription()[¶](#ApiClient.ServiceMethodReturnMappingItem.GetDescription "Link to this definition")  
Returns the description

Returns:  Description

Return type:  str

GetDisplayedType()[¶](#ApiClient.ServiceMethodReturnMappingItem.GetDisplayedType "Link to this definition")  
Returns a “nice” representation of the type as displayed in the “type” column of the mapping panel

Returns:  the displayed mapping type

Return type:  str

GetReferenceName()[¶](#ApiClient.ServiceMethodReturnMappingItem.GetReferenceName "Link to this definition")  
Returns the reference name of the mapping.

Returns:  The reference name of the mapping

Return type:  str

GetSubMapping()[¶](#ApiClient.ServiceMethodReturnMappingItem.GetSubMapping "Link to this definition")  
Returns contained Mapping or None if item does not support sub-mappings.

Returns:  Mapping with all submappings of the mapping item

Return type:  [`Mapping`](#ApiClient.Mapping "ApiClient.Mapping")

GetSystemIdentifier()[¶](#ApiClient.ServiceMethodReturnMappingItem.GetSystemIdentifier "Link to this definition")  
Returns the system identifier providing the currently mapped test quantity

Returns:  system identifier

Return type:  str

GetTargetPath()[¶](#ApiClient.ServiceMethodReturnMappingItem.GetTargetPath "Link to this definition")  
Returns the path this mapping item is currently pointing at

Returns:  complete path to the destination test quantity

Return type:  str

GetVariableType()[¶](#ApiClient.ServiceMethodReturnMappingItem.GetVariableType "Link to this definition")  
Returns the type of the target variable or None if target has no type.

Returns:  The type of the target variable. (e.g. VALUE, MATRIX, CURVE, …)

Return type:  str

IsAutogenerated()[¶](#ApiClient.ServiceMethodReturnMappingItem.IsAutogenerated "Link to this definition")  
Returns whether the mapping item is autogenerated.

Returns:  True, if autogenerated flag is set, else False

Return type:  boolean

SetCategory(*category*)[¶](#ApiClient.ServiceMethodReturnMappingItem.SetCategory "Link to this definition")  
Sets the category

Parameters:  **category** (*str*) – The new category to be used

SetDescription(*description*)[¶](#ApiClient.ServiceMethodReturnMappingItem.SetDescription "Link to this definition")  
Sets the description

Parameters:  **description** (*str*) – The new description to be used

SetReferenceName(*name*)[¶](#ApiClient.ServiceMethodReturnMappingItem.SetReferenceName "Link to this definition")  
Sets the reference name of the mapping.

Parameters:  **name** (*str*) – The reference name of the mapping

## ServiceMethodParameterMappingItem[¶](#servicemethodparametermappingitem "Link to this heading")

*class* ServiceMethodParameterMappingItem[¶](#ApiClient.ServiceMethodParameterMappingItem "Link to this definition")  
Base class

[`MappingItem`](#ApiClient.MappingItem "ApiClient.MappingItem")

Returned by

- [`MappingApi.CreateServiceMethodParameterMappingItem`](#ApiClient.MappingApi.CreateServiceMethodParameterMappingItem "ApiClient.MappingApi.CreateServiceMethodParameterMappingItem")

Clone()[¶](#ApiClient.ServiceMethodParameterMappingItem.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`ServiceMethodParameterMappingItem`](#ApiClient.ServiceMethodParameterMappingItem "ApiClient.ServiceMethodParameterMappingItem")

GetAccessType()[¶](#ApiClient.ServiceMethodParameterMappingItem.GetAccessType "Link to this definition")  
Returns a string identifying the mapping item’s type. (such as MODEL, BUS, MEASUREMENT, …)

Returns:  access type

Return type:  str

GetCategory()[¶](#ApiClient.ServiceMethodParameterMappingItem.GetCategory "Link to this definition")  
Returns the category

Returns:  Category

Return type:  str

GetDescription()[¶](#ApiClient.ServiceMethodParameterMappingItem.GetDescription "Link to this definition")  
Returns the description

Returns:  Description

Return type:  str

GetDisplayedType()[¶](#ApiClient.ServiceMethodParameterMappingItem.GetDisplayedType "Link to this definition")  
Returns a “nice” representation of the type as displayed in the “type” column of the mapping panel

Returns:  the displayed mapping type

Return type:  str

GetReferenceName()[¶](#ApiClient.ServiceMethodParameterMappingItem.GetReferenceName "Link to this definition")  
Returns the reference name of the mapping.

Returns:  The reference name of the mapping

Return type:  str

GetSubMapping()[¶](#ApiClient.ServiceMethodParameterMappingItem.GetSubMapping "Link to this definition")  
Returns contained Mapping or None if item does not support sub-mappings.

Returns:  Mapping with all submappings of the mapping item

Return type:  [`Mapping`](#ApiClient.Mapping "ApiClient.Mapping")

GetSystemIdentifier()[¶](#ApiClient.ServiceMethodParameterMappingItem.GetSystemIdentifier "Link to this definition")  
Returns the system identifier providing the currently mapped test quantity

Returns:  system identifier

Return type:  str

GetTargetPath()[¶](#ApiClient.ServiceMethodParameterMappingItem.GetTargetPath "Link to this definition")  
Returns the path this mapping item is currently pointing at

Returns:  complete path to the destination test quantity

Return type:  str

GetVariableType()[¶](#ApiClient.ServiceMethodParameterMappingItem.GetVariableType "Link to this definition")  
Returns the type of the target variable or None if target has no type.

Returns:  The type of the target variable. (e.g. VALUE, MATRIX, CURVE, …)

Return type:  str

IsAutogenerated()[¶](#ApiClient.ServiceMethodParameterMappingItem.IsAutogenerated "Link to this definition")  
Returns whether the mapping item is autogenerated.

Returns:  True, if autogenerated flag is set, else False

Return type:  boolean

SetCategory(*category*)[¶](#ApiClient.ServiceMethodParameterMappingItem.SetCategory "Link to this definition")  
Sets the category

Parameters:  **category** (*str*) – The new category to be used

SetDescription(*description*)[¶](#ApiClient.ServiceMethodParameterMappingItem.SetDescription "Link to this definition")  
Sets the description

Parameters:  **description** (*str*) – The new description to be used

SetReferenceName(*name*)[¶](#ApiClient.ServiceMethodParameterMappingItem.SetReferenceName "Link to this definition")  
Sets the reference name of the mapping.

Parameters:  **name** (*str*) – The reference name of the mapping
