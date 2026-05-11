[![logo](../../_static/ecu.test.svg)](../../index.html "API  documentation") API documentation

[ Internal APIs ](../../general_api/api.md)

[ Advanced operations of package variable types ](../../general_api/variabledatastructures.md)

[ Advanced properties of bus-related objects ](../../general_api/busdatastructures.md)

[ Bus related objects of trace analysis ](../../general_api/busdatastructuresTraceanalysis.md)

[ Advanced properties of diagnostics-related objects ](../../general_api/diagdatastructures.md)

[ Diagnostics related objects of trace analysis ](../../general_api/diagdatastructuresTraceanalysis.md)

[ Advanced properties of media-related objects ](../../general_api/mediadatastructures.md)

[ Advanced properties of DLT logging-related objects ](../../general_api/dltdatastructures.md)

[ COM API ](../../general_api/com-api.md)

[ REST API ](../../general_api/rest-api.md)

[ Report API ](../../general_api/apireport.md)

[ Object API ](../../general_api/objectApi.md)

[ Trace Analysis API ](../../TraceAnalysisAPI/index.md)

[ Generator APIs ](../../generators/index.md)

[ Tools ](../index.md)

Tools

User Tool API [ User Tool API ](#)

User Tool API

- [ UserTool ](#module-tts.core.toolingFramework.userTool.interfaces.UserTool)
  - [C UserTool ](#tts.core.toolingFramework.userTool.interfaces.UserTool.UserTool)
    - [M `\_\_init\_\_` ](#tts.core.toolingFramework.userTool.interfaces.UserTool.UserTool.__init__)
    - [M GetToolName ](#tts.core.toolingFramework.userTool.interfaces.UserTool.UserTool.GetToolName)
    - [M GetPorts ](#tts.core.toolingFramework.userTool.interfaces.UserTool.UserTool.GetPorts)
    - [M GetProperties ](#tts.core.toolingFramework.userTool.interfaces.UserTool.UserTool.GetProperties)
    - [M GetJobs ](#tts.core.toolingFramework.userTool.interfaces.UserTool.UserTool.GetJobs)
    - [M GetVersion ](#tts.core.toolingFramework.userTool.interfaces.UserTool.UserTool.GetVersion)
    - [M IsBroken ](#tts.core.toolingFramework.userTool.interfaces.UserTool.UserTool.IsBroken)
    - [M Dispose ](#tts.core.toolingFramework.userTool.interfaces.UserTool.UserTool.Dispose)
- [ UserPort ](#module-tts.core.toolingFramework.userTool.interfaces.UserPort)
  - [C UserPort ](#tts.core.toolingFramework.userTool.interfaces.UserPort.UserPort)
    - [M `\_\_init\_\_` ](#tts.core.toolingFramework.userTool.interfaces.UserPort.UserPort.__init__)
    - [M GetPortType ](#tts.core.toolingFramework.userTool.interfaces.UserPort.UserPort.GetPortType)
    - [M GetImplementationType ](#tts.core.toolingFramework.userTool.interfaces.UserPort.UserPort.GetImplementationType)
    - [M GetProperties ](#tts.core.toolingFramework.userTool.interfaces.UserPort.UserPort.GetProperties)
    - [M GetJobs ](#tts.core.toolingFramework.userTool.interfaces.UserPort.UserPort.GetJobs)
    - [M IsBroken ](#tts.core.toolingFramework.userTool.interfaces.UserPort.UserPort.IsBroken)
    - [M OnStart ](#tts.core.toolingFramework.userTool.interfaces.UserPort.UserPort.OnStart)
    - [M OnStop ](#tts.core.toolingFramework.userTool.interfaces.UserPort.UserPort.OnStop)
    - [M Dispose ](#tts.core.toolingFramework.userTool.interfaces.UserPort.UserPort.Dispose)
- [ UserImagePort ](#module-tts.core.toolingFramework.userTool.interfaces.UserImagePort)
  - [C UserImagePort ](#tts.core.toolingFramework.userTool.interfaces.UserImagePort.UserImagePort)
    - [M ReadImage ](#tts.core.toolingFramework.userTool.interfaces.UserImagePort.UserImagePort.ReadImage)
    - [M GetTouchInput ](#tts.core.toolingFramework.userTool.interfaces.UserImagePort.UserImagePort.GetTouchInput)
    - [M StartRecording ](#tts.core.toolingFramework.userTool.interfaces.UserImagePort.UserImagePort.StartRecording)
    - [M StopRecording ](#tts.core.toolingFramework.userTool.interfaces.UserImagePort.UserImagePort.StopRecording)
- [ UserTouchInput ](#module-tts.core.toolingFramework.userTool.interfaces.UserTouchInput)
  - [C UserTouchInput ](#tts.core.toolingFramework.userTool.interfaces.UserTouchInput.UserTouchInput)
    - [M GetScreenResolution ](#tts.core.toolingFramework.userTool.interfaces.UserTouchInput.UserTouchInput.GetScreenResolution)
    - [M PerformTap ](#tts.core.toolingFramework.userTool.interfaces.UserTouchInput.UserTouchInput.PerformTap)
    - [M PerformHold ](#tts.core.toolingFramework.userTool.interfaces.UserTouchInput.UserTouchInput.PerformHold)
    - [M PerformMultiTap ](#tts.core.toolingFramework.userTool.interfaces.UserTouchInput.UserTouchInput.PerformMultiTap)
    - [M PerformSwipe ](#tts.core.toolingFramework.userTool.interfaces.UserTouchInput.UserTouchInput.PerformSwipe)
    - [M PerformMultiSwipe ](#tts.core.toolingFramework.userTool.interfaces.UserTouchInput.UserTouchInput.PerformMultiSwipe)
    - [M PerformHoldAndSwipe ](#tts.core.toolingFramework.userTool.interfaces.UserTouchInput.UserTouchInput.PerformHoldAndSwipe)
    - [M PerformPinch ](#tts.core.toolingFramework.userTool.interfaces.UserTouchInput.UserTouchInput.PerformPinch)
    - [M PerformRotate ](#tts.core.toolingFramework.userTool.interfaces.UserTouchInput.UserTouchInput.PerformRotate)
- [ UserModelPort ](#module-tts.core.toolingFramework.userTool.interfaces.UserModelPort)
  - [C VariableInfo ](#tts.core.toolingFramework.userTool.interfaces.UserModelPort.VariableInfo)
    - [A Type ](#tts.core.toolingFramework.userTool.interfaces.UserModelPort.VariableInfo.Type)
    - [A Representation ](#tts.core.toolingFramework.userTool.interfaces.UserModelPort.VariableInfo.Representation)
    - [A Unit ](#tts.core.toolingFramework.userTool.interfaces.UserModelPort.VariableInfo.Unit)
    - [A Description ](#tts.core.toolingFramework.userTool.interfaces.UserModelPort.VariableInfo.Description)
  - [C UserModelPort ](#tts.core.toolingFramework.userTool.interfaces.UserModelPort.UserModelPort)
    - [M GetAcquisitionRates ](#tts.core.toolingFramework.userTool.interfaces.UserModelPort.UserModelPort.GetAcquisitionRates)
    - [M GetDefaultAcquisitionRate ](#tts.core.toolingFramework.userTool.interfaces.UserModelPort.UserModelPort.GetDefaultAcquisitionRate)
    - [M GetModels ](#tts.core.toolingFramework.userTool.interfaces.UserModelPort.UserModelPort.GetModels)
    - [M GetPathDelimiter ](#tts.core.toolingFramework.userTool.interfaces.UserModelPort.UserModelPort.GetPathDelimiter)
    - [M GetRecorder ](#tts.core.toolingFramework.userTool.interfaces.UserModelPort.UserModelPort.GetRecorder)
    - [M GetSimulationManager ](#tts.core.toolingFramework.userTool.interfaces.UserModelPort.UserModelPort.GetSimulationManager)
    - [M GetVariables ](#tts.core.toolingFramework.userTool.interfaces.UserModelPort.UserModelPort.GetVariables)
    - [M GetVariablesHash ](#tts.core.toolingFramework.userTool.interfaces.UserModelPort.UserModelPort.GetVariablesHash)
    - [M Read ](#tts.core.toolingFramework.userTool.interfaces.UserModelPort.UserModelPort.Read)
    - [M RegisterVariable ](#tts.core.toolingFramework.userTool.interfaces.UserModelPort.UserModelPort.RegisterVariable)
    - [M UnregisterVariable ](#tts.core.toolingFramework.userTool.interfaces.UserModelPort.UserModelPort.UnregisterVariable)
    - [M Write ](#tts.core.toolingFramework.userTool.interfaces.UserModelPort.UserModelPort.Write)
- [ UserRecorder ](#module-tts.core.toolingFramework.userTool.interfaces.UserRecorder)
  - [C RecordingVariable ](#tts.core.toolingFramework.userTool.interfaces.UserRecorder.RecordingVariable)
    - [A Path ](#tts.core.toolingFramework.userTool.interfaces.UserRecorder.RecordingVariable.Path)
    - [A AcquisitionRate ](#tts.core.toolingFramework.userTool.interfaces.UserRecorder.RecordingVariable.AcquisitionRate)
  - [C UserRecorder ](#tts.core.toolingFramework.userTool.interfaces.UserRecorder.UserRecorder)
    - [M `\_\_init\_\_` ](#tts.core.toolingFramework.userTool.interfaces.UserRecorder.UserRecorder.__init__)
    - [M Start ](#tts.core.toolingFramework.userTool.interfaces.UserRecorder.UserRecorder.Start)
    - [M Stop ](#tts.core.toolingFramework.userTool.interfaces.UserRecorder.UserRecorder.Stop)
    - [M Dispose ](#tts.core.toolingFramework.userTool.interfaces.UserRecorder.UserRecorder.Dispose)
- [ UserSimulationManager ](#module-tts.core.toolingFramework.userTool.interfaces.UserSimulationManager)
  - [C UserSimulationManager ](#tts.core.toolingFramework.userTool.interfaces.UserSimulationManager.UserSimulationManager)
    - [M `\_\_init\_\_` ](#tts.core.toolingFramework.userTool.interfaces.UserSimulationManager.UserSimulationManager.__init__)
    - [M GetTime ](#tts.core.toolingFramework.userTool.interfaces.UserSimulationManager.UserSimulationManager.GetTime)
    - [M Step ](#tts.core.toolingFramework.userTool.interfaces.UserSimulationManager.UserSimulationManager.Step)
    - [M SetUpdateTimeCallback ](#tts.core.toolingFramework.userTool.interfaces.UserSimulationManager.UserSimulationManager.SetUpdateTimeCallback)
    - [M Start ](#tts.core.toolingFramework.userTool.interfaces.UserSimulationManager.UserSimulationManager.Start)
    - [M Pause ](#tts.core.toolingFramework.userTool.interfaces.UserSimulationManager.UserSimulationManager.Pause)
    - [M Dispose ](#tts.core.toolingFramework.userTool.interfaces.UserSimulationManager.UserSimulationManager.Dispose)
- [ UserJob ](#module-tts.core.toolingFramework.userTool.interfaces.UserJob)
  - [C UserJob ](#tts.core.toolingFramework.userTool.interfaces.UserJob.UserJob)
    - [M Call ](#tts.core.toolingFramework.userTool.interfaces.UserJob.UserJob.Call)
    - [M `\_\_init\_\_` ](#tts.core.toolingFramework.userTool.interfaces.UserJob.UserJob.__init__)
    - [M GetCategory ](#tts.core.toolingFramework.userTool.interfaces.UserJob.UserJob.GetCategory)
    - [M GetDynamicParameterInformation ](#tts.core.toolingFramework.userTool.interfaces.UserJob.UserJob.GetDynamicParameterInformation)
  - [C DynamicParameterInformation ](#tts.core.toolingFramework.userTool.interfaces.UserJob.DynamicParameterInformation)
    - [A Choices ](#tts.core.toolingFramework.userTool.interfaces.UserJob.DynamicParameterInformation.Choices)
    - [A Default ](#tts.core.toolingFramework.userTool.interfaces.UserJob.DynamicParameterInformation.Default)

[ Model-based Bus Port API ](../modelbasedbusport-api/modelbasedbusport-api.md)

[ User test management ](../../userTestmanagement/index.md)

[ UserUtility API ](../../user-utility/user-utility.md)

[ Utility Examples ](../../user-utility/example-utilities.md)

User Tool API

- [ UserTool ](#module-tts.core.toolingFramework.userTool.interfaces.UserTool)
  - [C UserTool ](#tts.core.toolingFramework.userTool.interfaces.UserTool.UserTool)
    - [M `\_\_init\_\_` ](#tts.core.toolingFramework.userTool.interfaces.UserTool.UserTool.__init__)
    - [M GetToolName ](#tts.core.toolingFramework.userTool.interfaces.UserTool.UserTool.GetToolName)
    - [M GetPorts ](#tts.core.toolingFramework.userTool.interfaces.UserTool.UserTool.GetPorts)
    - [M GetProperties ](#tts.core.toolingFramework.userTool.interfaces.UserTool.UserTool.GetProperties)
    - [M GetJobs ](#tts.core.toolingFramework.userTool.interfaces.UserTool.UserTool.GetJobs)
    - [M GetVersion ](#tts.core.toolingFramework.userTool.interfaces.UserTool.UserTool.GetVersion)
    - [M IsBroken ](#tts.core.toolingFramework.userTool.interfaces.UserTool.UserTool.IsBroken)
    - [M Dispose ](#tts.core.toolingFramework.userTool.interfaces.UserTool.UserTool.Dispose)
- [ UserPort ](#module-tts.core.toolingFramework.userTool.interfaces.UserPort)
  - [C UserPort ](#tts.core.toolingFramework.userTool.interfaces.UserPort.UserPort)
    - [M `\_\_init\_\_` ](#tts.core.toolingFramework.userTool.interfaces.UserPort.UserPort.__init__)
    - [M GetPortType ](#tts.core.toolingFramework.userTool.interfaces.UserPort.UserPort.GetPortType)
    - [M GetImplementationType ](#tts.core.toolingFramework.userTool.interfaces.UserPort.UserPort.GetImplementationType)
    - [M GetProperties ](#tts.core.toolingFramework.userTool.interfaces.UserPort.UserPort.GetProperties)
    - [M GetJobs ](#tts.core.toolingFramework.userTool.interfaces.UserPort.UserPort.GetJobs)
    - [M IsBroken ](#tts.core.toolingFramework.userTool.interfaces.UserPort.UserPort.IsBroken)
    - [M OnStart ](#tts.core.toolingFramework.userTool.interfaces.UserPort.UserPort.OnStart)
    - [M OnStop ](#tts.core.toolingFramework.userTool.interfaces.UserPort.UserPort.OnStop)
    - [M Dispose ](#tts.core.toolingFramework.userTool.interfaces.UserPort.UserPort.Dispose)
- [ UserImagePort ](#module-tts.core.toolingFramework.userTool.interfaces.UserImagePort)
  - [C UserImagePort ](#tts.core.toolingFramework.userTool.interfaces.UserImagePort.UserImagePort)
    - [M ReadImage ](#tts.core.toolingFramework.userTool.interfaces.UserImagePort.UserImagePort.ReadImage)
    - [M GetTouchInput ](#tts.core.toolingFramework.userTool.interfaces.UserImagePort.UserImagePort.GetTouchInput)
    - [M StartRecording ](#tts.core.toolingFramework.userTool.interfaces.UserImagePort.UserImagePort.StartRecording)
    - [M StopRecording ](#tts.core.toolingFramework.userTool.interfaces.UserImagePort.UserImagePort.StopRecording)
- [ UserTouchInput ](#module-tts.core.toolingFramework.userTool.interfaces.UserTouchInput)
  - [C UserTouchInput ](#tts.core.toolingFramework.userTool.interfaces.UserTouchInput.UserTouchInput)
    - [M GetScreenResolution ](#tts.core.toolingFramework.userTool.interfaces.UserTouchInput.UserTouchInput.GetScreenResolution)
    - [M PerformTap ](#tts.core.toolingFramework.userTool.interfaces.UserTouchInput.UserTouchInput.PerformTap)
    - [M PerformHold ](#tts.core.toolingFramework.userTool.interfaces.UserTouchInput.UserTouchInput.PerformHold)
    - [M PerformMultiTap ](#tts.core.toolingFramework.userTool.interfaces.UserTouchInput.UserTouchInput.PerformMultiTap)
    - [M PerformSwipe ](#tts.core.toolingFramework.userTool.interfaces.UserTouchInput.UserTouchInput.PerformSwipe)
    - [M PerformMultiSwipe ](#tts.core.toolingFramework.userTool.interfaces.UserTouchInput.UserTouchInput.PerformMultiSwipe)
    - [M PerformHoldAndSwipe ](#tts.core.toolingFramework.userTool.interfaces.UserTouchInput.UserTouchInput.PerformHoldAndSwipe)
    - [M PerformPinch ](#tts.core.toolingFramework.userTool.interfaces.UserTouchInput.UserTouchInput.PerformPinch)
    - [M PerformRotate ](#tts.core.toolingFramework.userTool.interfaces.UserTouchInput.UserTouchInput.PerformRotate)
- [ UserModelPort ](#module-tts.core.toolingFramework.userTool.interfaces.UserModelPort)
  - [C VariableInfo ](#tts.core.toolingFramework.userTool.interfaces.UserModelPort.VariableInfo)
    - [A Type ](#tts.core.toolingFramework.userTool.interfaces.UserModelPort.VariableInfo.Type)
    - [A Representation ](#tts.core.toolingFramework.userTool.interfaces.UserModelPort.VariableInfo.Representation)
    - [A Unit ](#tts.core.toolingFramework.userTool.interfaces.UserModelPort.VariableInfo.Unit)
    - [A Description ](#tts.core.toolingFramework.userTool.interfaces.UserModelPort.VariableInfo.Description)
  - [C UserModelPort ](#tts.core.toolingFramework.userTool.interfaces.UserModelPort.UserModelPort)
    - [M GetAcquisitionRates ](#tts.core.toolingFramework.userTool.interfaces.UserModelPort.UserModelPort.GetAcquisitionRates)
    - [M GetDefaultAcquisitionRate ](#tts.core.toolingFramework.userTool.interfaces.UserModelPort.UserModelPort.GetDefaultAcquisitionRate)
    - [M GetModels ](#tts.core.toolingFramework.userTool.interfaces.UserModelPort.UserModelPort.GetModels)
    - [M GetPathDelimiter ](#tts.core.toolingFramework.userTool.interfaces.UserModelPort.UserModelPort.GetPathDelimiter)
    - [M GetRecorder ](#tts.core.toolingFramework.userTool.interfaces.UserModelPort.UserModelPort.GetRecorder)
    - [M GetSimulationManager ](#tts.core.toolingFramework.userTool.interfaces.UserModelPort.UserModelPort.GetSimulationManager)
    - [M GetVariables ](#tts.core.toolingFramework.userTool.interfaces.UserModelPort.UserModelPort.GetVariables)
    - [M GetVariablesHash ](#tts.core.toolingFramework.userTool.interfaces.UserModelPort.UserModelPort.GetVariablesHash)
    - [M Read ](#tts.core.toolingFramework.userTool.interfaces.UserModelPort.UserModelPort.Read)
    - [M RegisterVariable ](#tts.core.toolingFramework.userTool.interfaces.UserModelPort.UserModelPort.RegisterVariable)
    - [M UnregisterVariable ](#tts.core.toolingFramework.userTool.interfaces.UserModelPort.UserModelPort.UnregisterVariable)
    - [M Write ](#tts.core.toolingFramework.userTool.interfaces.UserModelPort.UserModelPort.Write)
- [ UserRecorder ](#module-tts.core.toolingFramework.userTool.interfaces.UserRecorder)
  - [C RecordingVariable ](#tts.core.toolingFramework.userTool.interfaces.UserRecorder.RecordingVariable)
    - [A Path ](#tts.core.toolingFramework.userTool.interfaces.UserRecorder.RecordingVariable.Path)
    - [A AcquisitionRate ](#tts.core.toolingFramework.userTool.interfaces.UserRecorder.RecordingVariable.AcquisitionRate)
  - [C UserRecorder ](#tts.core.toolingFramework.userTool.interfaces.UserRecorder.UserRecorder)
    - [M `\_\_init\_\_` ](#tts.core.toolingFramework.userTool.interfaces.UserRecorder.UserRecorder.__init__)
    - [M Start ](#tts.core.toolingFramework.userTool.interfaces.UserRecorder.UserRecorder.Start)
    - [M Stop ](#tts.core.toolingFramework.userTool.interfaces.UserRecorder.UserRecorder.Stop)
    - [M Dispose ](#tts.core.toolingFramework.userTool.interfaces.UserRecorder.UserRecorder.Dispose)
- [ UserSimulationManager ](#module-tts.core.toolingFramework.userTool.interfaces.UserSimulationManager)
  - [C UserSimulationManager ](#tts.core.toolingFramework.userTool.interfaces.UserSimulationManager.UserSimulationManager)
    - [M `\_\_init\_\_` ](#tts.core.toolingFramework.userTool.interfaces.UserSimulationManager.UserSimulationManager.__init__)
    - [M GetTime ](#tts.core.toolingFramework.userTool.interfaces.UserSimulationManager.UserSimulationManager.GetTime)
    - [M Step ](#tts.core.toolingFramework.userTool.interfaces.UserSimulationManager.UserSimulationManager.Step)
    - [M SetUpdateTimeCallback ](#tts.core.toolingFramework.userTool.interfaces.UserSimulationManager.UserSimulationManager.SetUpdateTimeCallback)
    - [M Start ](#tts.core.toolingFramework.userTool.interfaces.UserSimulationManager.UserSimulationManager.Start)
    - [M Pause ](#tts.core.toolingFramework.userTool.interfaces.UserSimulationManager.UserSimulationManager.Pause)
    - [M Dispose ](#tts.core.toolingFramework.userTool.interfaces.UserSimulationManager.UserSimulationManager.Dispose)
- [ UserJob ](#module-tts.core.toolingFramework.userTool.interfaces.UserJob)
  - [C UserJob ](#tts.core.toolingFramework.userTool.interfaces.UserJob.UserJob)
    - [M Call ](#tts.core.toolingFramework.userTool.interfaces.UserJob.UserJob.Call)
    - [M `\_\_init\_\_` ](#tts.core.toolingFramework.userTool.interfaces.UserJob.UserJob.__init__)
    - [M GetCategory ](#tts.core.toolingFramework.userTool.interfaces.UserJob.UserJob.GetCategory)
    - [M GetDynamicParameterInformation ](#tts.core.toolingFramework.userTool.interfaces.UserJob.UserJob.GetDynamicParameterInformation)
  - [C DynamicParameterInformation ](#tts.core.toolingFramework.userTool.interfaces.UserJob.DynamicParameterInformation)
    - [A Choices ](#tts.core.toolingFramework.userTool.interfaces.UserJob.DynamicParameterInformation.Choices)
    - [A Default ](#tts.core.toolingFramework.userTool.interfaces.UserJob.DynamicParameterInformation.Default)

# User Tool API[¶](#user-tool-api "Link to this heading")

## UserTool[¶](#module-tts.core.toolingFramework.userTool.interfaces.UserTool "Link to this heading")

*class* UserTool[¶](#tts.core.toolingFramework.userTool.interfaces.UserTool.UserTool "Link to this definition")  
This class describes the interface of a user tool.

In order for ecu.test to recognize a class as a user tool, the class must meet the requirements of this interface. In addition, the `MODULE_TYPE` must be set to `USER_TOOL`.

    import ...

    MODULE_TYPE = 'USER_TOOL'

    class UserTool:
        def __init__(self, properties: dict[str, str | bool]) -> None:
            ...

`\_\_init\_\_`(*[properties](#tts.core.toolingFramework.userTool.interfaces.UserTool.UserTool.__init__.properties "tts.core.toolingFramework.userTool.interfaces.UserTool.UserTool.__init__.properties (Python parameter) — Dictionary with the properties from the test bench configuration for this tool and the configured values.")*)[¶](#tts.core.toolingFramework.userTool.interfaces.UserTool.UserTool.__init__ "Link to this definition")  
Parameters:  properties : dict[str, str | bool][¶](#tts.core.toolingFramework.userTool.interfaces.UserTool.UserTool.__init__.properties "Permalink to this definition")  
Dictionary with the properties from the test bench configuration for this tool and the configured values. The possible properties are defined by the return value of the [`GetProperties()`](#tts.core.toolingFramework.userTool.interfaces.UserTool.UserTool.GetProperties "tts.core.toolingFramework.userTool.interfaces.UserTool.UserTool.GetProperties (Python method) — Optional (does not have to be implemented)") method.

*classmethod* GetToolName()[¶](#tts.core.toolingFramework.userTool.interfaces.UserTool.UserTool.GetToolName "Link to this definition")  
Returns:  The name of the tool. This name is displayed in the test bench configuration.

Return type:  str

*classmethod* GetPorts()[¶](#tts.core.toolingFramework.userTool.interfaces.UserTool.UserTool.GetPorts "Link to this definition")  
*Optional (does not have to be implemented)*

Provides a list of ports offered by this user tool. These ports can be selected in the test bench configuration when a new port is created for the user tool.

Port classes must fulfill a certain interface in order to be accepted by ecu.test.

Returns:  List of supported port classes.

Return type:  list[type[[UserPort](#tts.core.toolingFramework.userTool.interfaces.UserPort.UserPort "tts.core.toolingFramework.userTool.interfaces.UserPort.UserPort (Python class) — This class describes the interface of a user port. Classes that fulfill this interface can be used as port of a user tool.")]]

*classmethod* GetProperties()[¶](#tts.core.toolingFramework.userTool.interfaces.UserTool.UserTool.GetProperties "Link to this definition")  
*Optional (does not have to be implemented)*

Properties of the tool. These properties can be configured in the test bench configuration. The configured properties are passed to the user port when the configuration is started. Available property types are STRING, TEXT, BOOL and CHOICE. Properties may be sorted into groups to improve visual separation in the test bench configuration. Informational properties can be marked readonly. For BOOL and CHOICE properties, it is possible to define properties that are only available for a given property value. Each property can optionally be given a display name. This is useful, for example, if you want to define properties with the same display name for each option of a CHOICE property. If no display name is set, the property name is used.

Example:

    @classmethod
    def GetProperties(cls) -> dict[str, dict]:
        return {
            'Group 1': {
                'Opt1': {
                    'Description': 'This is Option 1',
                    'DisplayName': 'Option 1',
                    'Type': 'STRING',
                    'Default': 'default value',
                },
                'Opt2': {
                    'Description': 'This is Option 2',
                    'DisplayName': 'Option 2',
                    'Type': 'TEXT',
                    'ReadOnly': True,
                    'Default': 'Information on\nmultiple lines.\n',
                },
                'Option 3': {
                    'Description': 'This is Option 3',
                    'Type': 'BOOL',
                    'Default': True,
                },
                'Option 4': {
                    'Description': 'This is Option 4',
                    'Type': 'CHOICE',
                    'Choices': ['c1', 'c2', 'c3'],
                    'Default': 'c2',
                },
            },
            'Group with sub properties': {
                'Option 5': {
                    'Description': 'This BOOL option has a sub property',
                    'Type': 'BOOL',
                    'Default': True,
                    'Children': {
                        'Sub option 5.1': {
                            'Description': 'This option is visible if Option 5 is checked',
                            'Type': 'STRING',
                            'Default': 'default value',
                        },
                    },
                },
                'Option 6': {
                    'Description': 'This CHOICE option has a sub property',
                    'Type': 'CHOICE',
                    'Choices': {
                        'c1': {
                            'Sub option 6.1': {
                                'Description': 'This option is only visible for choice c1',
                                'Type': 'STRING',
                                'Default': 'default value',
                            },
                        },
                        'c2': {
                        },
                    },
                    'Default': 'c2',
                },
            },
        }

The above example will generate the following properties:

![](../../_images/UserTool_GetProperties.png)

\

Returns:  Dictionary with properties of the user tool.

Return type:  dict[str, dict]

*classmethod* GetJobs()[¶](#tts.core.toolingFramework.userTool.interfaces.UserTool.UserTool.GetJobs "Link to this definition")  
*Optional (does not have to be implemented)*

Provides a list of methods that are offered in ecu.test as a tool job for this user tool.

Info

The properties of the tool job are generated using the docstring and the Python type hints of the method.

..example:

    .. code-block:: python

        @classmethod
        def GetJobs(cls) -> list[Callable]:
            return [cls.MyToolJob]

        def MyToolJob(self, param1: str, param2: int) -> bool:
            '''
            :param param1: description of param 1
            :param param2: description of param 2
            :return: description of the returned value
            '''
            return True

Returns:  List of job methods.

Return type:  list[Callable | type[[UserJob](#tts.core.toolingFramework.userTool.interfaces.UserJob.UserJob "tts.core.toolingFramework.userTool.interfaces.UserJob.UserJob (Python class) — This class describes the interface of a user job. It should be used if the list of possible values or the default value of one or more parameters must be determined dynamically.")]]

GetVersion()[¶](#tts.core.toolingFramework.userTool.interfaces.UserTool.UserTool.GetVersion "Link to this definition")  
Version of the external tool. This version will be documented in the test report.

Returns:  version

Return type:  str

IsBroken()[¶](#tts.core.toolingFramework.userTool.interfaces.UserTool.UserTool.IsBroken "Link to this definition")  
*Optional (does not have to be implemented)*

Indicates a broken tool state. Called before test execution and on configuration window update. Should return True if any of the external tools used by this user tool cannot be used anymore (e.g. connection lost, tool locked up).

Otherwise or if no external tool is used, False should be returned.

Returns:  True if tool is broken (not usable), otherwise False.

Return type:  bool

Dispose()[¶](#tts.core.toolingFramework.userTool.interfaces.UserTool.UserTool.Dispose "Link to this definition")  
*Optional (does not have to be implemented)*

Gracefully terminates the connection to the external tool and/or other shutdown sequences.

Is called when the configuration is stopped in ecu.test.

## UserPort[¶](#module-tts.core.toolingFramework.userTool.interfaces.UserPort "Link to this heading")

*class* UserPort[¶](#tts.core.toolingFramework.userTool.interfaces.UserPort.UserPort "Link to this definition")  
This class describes the interface of a user port. Classes that fulfill this interface can be used as port of a user tool.

`\_\_init\_\_`(*[tool](#tts.core.toolingFramework.userTool.interfaces.UserPort.UserPort.__init__.tool "tts.core.toolingFramework.userTool.interfaces.UserPort.UserPort.__init__.tool (Python parameter) — Tool providing this port.")*, *[properties](#tts.core.toolingFramework.userTool.interfaces.UserPort.UserPort.__init__.properties "tts.core.toolingFramework.userTool.interfaces.UserPort.UserPort.__init__.properties (Python parameter) — Dictionary with the properties from the testbench configuration for this port and the configured values.")*)[¶](#tts.core.toolingFramework.userTool.interfaces.UserPort.UserPort.__init__ "Link to this definition")  
Parameters:  tool : [UserTool](#tts.core.toolingFramework.userTool.interfaces.UserTool.UserTool "tts.core.toolingFramework.userTool.interfaces.UserTool.UserTool (Python class) — This class describes the interface of a user tool.")[¶](#tts.core.toolingFramework.userTool.interfaces.UserPort.UserPort.__init__.tool "Permalink to this definition")  
Tool providing this port. Can be used to query the properties of the tool, for example.

properties : dict[str, str | bool][¶](#tts.core.toolingFramework.userTool.interfaces.UserPort.UserPort.__init__.properties "Permalink to this definition")  
Dictionary with the properties from the testbench configuration for this port and the configured values. The possible properties are defined by the return value of the [`GetProperties()`](#tts.core.toolingFramework.userTool.interfaces.UserPort.UserPort.GetProperties "tts.core.toolingFramework.userTool.interfaces.UserPort.UserPort.GetProperties (Python method) — Optional (does not have to be implemented)") method.

*classmethod* GetPortType()[¶](#tts.core.toolingFramework.userTool.interfaces.UserPort.UserPort.GetPortType "Link to this definition")  
Returns the type of the port. This type defines which interface the port must fulfill and therefore which range of functions it offers. Valid types are

- BASE (must fulfill the [`UserPort`](#tts.core.toolingFramework.userTool.interfaces.UserPort.UserPort "tts.core.toolingFramework.userTool.interfaces.UserPort.UserPort (Python class) — This class describes the interface of a user port. Classes that fulfill this interface can be used as port of a user tool.") interface)

- IMAGE (must fulfill the [`UserImagePort`](#tts.core.toolingFramework.userTool.interfaces.UserImagePort.UserImagePort "tts.core.toolingFramework.userTool.interfaces.UserImagePort.UserImagePort (Python class) — Bases: UserPort") interface)

- MODEL (must fulfill the [`UserModelPort`](#tts.core.toolingFramework.userTool.interfaces.UserModelPort.UserModelPort "tts.core.toolingFramework.userTool.interfaces.UserModelPort.UserModelPort (Python class) — Bases: UserPort") interface)

Returns:  Type of the port.

Return type:  *Literal*[‘BASE’, ‘IMAGE’, ‘MODEL’]

*classmethod* GetImplementationType()[¶](#tts.core.toolingFramework.userTool.interfaces.UserPort.UserPort.GetImplementationType "Link to this definition")  
*Optional (does not have to be implemented)*

Returns the implementation type of the port.

By setting an implementation type, several ports of the same type (see [`GetPortType()`](#tts.core.toolingFramework.userTool.interfaces.UserPort.UserPort.GetPortType "tts.core.toolingFramework.userTool.interfaces.UserPort.UserPort.GetPortType (Python method) — Returns the type of the port. This type defines which interface the port must fulfill and therefore which range of functions it offers. Valid types are")) can be offered with different implementations.

Returns:  implementation type of the port

Return type:  str

*classmethod* GetProperties()[¶](#tts.core.toolingFramework.userTool.interfaces.UserPort.UserPort.GetProperties "Link to this definition")  
*Optional (does not have to be implemented)*

Properties of the port. These properties can be configured in the test bench configuration. The configured properties are passed to the `\_\_init\_\_` method when the configuration is started. Available property types are STRING, TEXT, BOOL and CHOICE. Properties may be sorted into groups to improve visual separation in the test bench configuration. Informational properties can be marked readonly. For BOOL and CHOICE properties, it is possible to define properties that are only available for a given property value.

Example:

    @classmethod
    def GetProperties(cls) -> dict[str, dict]:
        return {
            'Group 1': {
                'Option 1': {
                    'Description': 'This is Option 1',
                    'Type': 'STRING',
                    'Default': 'default value',
                },
                'Option 2': {
                    'Description': 'This is Option 2',
                    'Type': 'TEXT',
                    'ReadOnly': True,
                    'Default': 'Information on\nmultiple lines.\n',
                },
                'Option 3': {
                    'Description': 'This is Option 3',
                    'Type': 'BOOL',
                    'Default': True,
                },
                'Option 4': {
                    'Description': 'This is Option 4',
                    'Type': 'CHOICE',
                    'Choices': ['c1', 'c2', 'c3'],
                    'Default': 'c2',
                },
            },
            'Group with sub properties': {
                'Option 5': {
                    'Description': 'This BOOL option has a sub property',
                    'Type': 'BOOL',
                    'Default': True,
                    'Children': {
                        'Sub option 5.1': {
                            'Description': 'This option is visible if Option 5 is checked',
                            'Type': 'STRING',
                            'Default': 'default value',
                        },
                    },
                },
                'Option 6': {
                    'Description': 'This CHOICE option has a sub property',
                    'Type': 'CHOICE',
                    'Choices': {
                        'c1': {
                            'Sub option 6.1': {
                                'Description': 'This option is only visible for choice c1',
                                'Type': 'STRING',
                                'Default': 'default value',
                            },
                        },
                        'c2': {
                        },
                    },
                    'Default': 'c2',
                },
            },
        }

The above example will generate the following properties:

![](../../_images/UserTool_GetProperties.png)

Returns:  Dictionary with properties of the user port.

Return type:  dict[str, dict]

*classmethod* GetJobs()[¶](#tts.core.toolingFramework.userTool.interfaces.UserPort.UserPort.GetJobs "Link to this definition")  
*Optional (does not have to be implemented)*

Provides a list of methods that are offered in ecu.test as a port job for this user port.

Info

The properties of the tool job are generated using the docstring and the Python type hints of the method.

Example:

    @classmethod
    def GetJobs(cls) -> list[Callable]:
        return [cls.MyPortJob]

    def MyPortJob(self, param1: str, param2: int) -> bool:
        '''
        :param param1: description of param 1
        :param param2: description of param 2
        :return: description of the returned value
        '''
        return True

Returns:  List of job methods.

Return type:  list[Callable | type[[UserJob](#tts.core.toolingFramework.userTool.interfaces.UserJob.UserJob "tts.core.toolingFramework.userTool.interfaces.UserJob.UserJob (Python class) — This class describes the interface of a user job. It should be used if the list of possible values or the default value of one or more parameters must be determined dynamically.")]]

IsBroken()[¶](#tts.core.toolingFramework.userTool.interfaces.UserPort.UserPort.IsBroken "Link to this definition")  
*Optional (does not have to be implemented)*

Method to indicate a broken port state. Called before test execution and on configuration window update. Should return True if any of the external tools used by this port cannot be used anymore (e.g. connection lost, tool locked up).

Otherwise or if no external tool is used, False should be returned.

Returns:  True if tool is broken (not usable), otherwise False.

Return type:  bool

OnStart()[¶](#tts.core.toolingFramework.userTool.interfaces.UserPort.UserPort.OnStart "Link to this definition")  
*Optional (does not have to be implemented)*

Method to handle preparatory steps before test execution,

Is called right after a package has been started.

OnStop()[¶](#tts.core.toolingFramework.userTool.interfaces.UserPort.UserPort.OnStop "Link to this definition")  
*Optional (does not have to be implemented)*

Method to handle finalizing steps after test execution.

Is called after the execution of the package has been completed.

Dispose()[¶](#tts.core.toolingFramework.userTool.interfaces.UserPort.UserPort.Dispose "Link to this definition")  
*Optional (does not have to be implemented)*

Gracefully terminates the connection to the external tool and/or other shutdown sequences.

Is called when the configuration is stopped in ecu.test.

## UserImagePort[¶](#module-tts.core.toolingFramework.userTool.interfaces.UserImagePort "Link to this heading")

*class* UserImagePort[¶](#tts.core.toolingFramework.userTool.interfaces.UserImagePort.UserImagePort "Link to this definition")  
Bases: [`UserPort`](#tts.core.toolingFramework.userTool.interfaces.UserPort.UserPort "tts.core.toolingFramework.userTool.interfaces.UserPort.UserPort (Python class) — This class describes the interface of a user port. Classes that fulfill this interface can be used as port of a user tool.")

ReadImage()[¶](#tts.core.toolingFramework.userTool.interfaces.UserImagePort.UserImagePort.ReadImage "Link to this definition")  
Reads an image from e.g. an external source and makes it available as a numpy array.

Returns:  Tuple of two numpy arrays. The first contains the image data, the second contains alpha values or None. Note that if alpha values are returned, the array must have the same size as the image data array.

Return type:  tuple[NDArray[Any], NDArray[Any] | None]

GetTouchInput()[¶](#tts.core.toolingFramework.userTool.interfaces.UserImagePort.UserImagePort.GetTouchInput "Link to this definition")  
*Optional (does not have to be implemented)*

Returns an object that provides the interface for processing touch inputs. Implementing this method indicates that this port supports touch input test steps. Can be omitted if the port does not support touch input.

Returns:  Object that fulfills the [`UserTouchInput`](#tts.core.toolingFramework.userTool.interfaces.UserTouchInput.UserTouchInput "tts.core.toolingFramework.userTool.interfaces.UserTouchInput.UserTouchInput (Python class) — Describes the interface for touch inputs.") interface.

Return type:  [UserTouchInput](#tts.core.toolingFramework.userTool.interfaces.UserTouchInput.UserTouchInput "tts.core.toolingFramework.userTool.interfaces.UserTouchInput.UserTouchInput (Python class) — Describes the interface for touch inputs.")

StartRecording(*[recordingId](#tts.core.toolingFramework.userTool.interfaces.UserImagePort.UserImagePort.StartRecording.recordingId "tts.core.toolingFramework.userTool.interfaces.UserImagePort.UserImagePort.StartRecording.recordingId (Python parameter) — Identifier for the recording to be started.")*)[¶](#tts.core.toolingFramework.userTool.interfaces.UserImagePort.UserImagePort.StartRecording "Link to this definition")  
*Optional (does not have to be implemented)*

Starts a recording. For recording to work, both [`StartRecording()`](#tts.core.toolingFramework.userTool.interfaces.UserImagePort.UserImagePort.StartRecording "tts.core.toolingFramework.userTool.interfaces.UserImagePort.UserImagePort.StartRecording (Python method) — Optional (does not have to be implemented)") and [`StopRecording()`](#tts.core.toolingFramework.userTool.interfaces.UserImagePort.UserImagePort.StopRecording "tts.core.toolingFramework.userTool.interfaces.UserImagePort.UserImagePort.StopRecording (Python method) — Optional (does not have to be implemented)") must be implemented.

Example:

    def StartRecording(self, recordingId: str) -> None:
        # Start recording within the user tool
        self._myUserToolApi.StartRecording()

Parameters:  recordingId : str[¶](#tts.core.toolingFramework.userTool.interfaces.UserImagePort.UserImagePort.StartRecording.recordingId "Permalink to this definition")  
Identifier for the recording to be started. Correlates with a recording group in ecu.test.

StopRecording(*[recordingId](#tts.core.toolingFramework.userTool.interfaces.UserImagePort.UserImagePort.StopRecording.recordingId "tts.core.toolingFramework.userTool.interfaces.UserImagePort.UserImagePort.StopRecording.recordingId (Python parameter) — Identifier for the recording to be stopped.")*)[¶](#tts.core.toolingFramework.userTool.interfaces.UserImagePort.UserImagePort.StopRecording "Link to this definition")  
*Optional (does not have to be implemented)*

Stops the recording for the given recordingId. Should return the path of the created recording file. For recording to work, both [`StartRecording()`](#tts.core.toolingFramework.userTool.interfaces.UserImagePort.UserImagePort.StartRecording "tts.core.toolingFramework.userTool.interfaces.UserImagePort.UserImagePort.StartRecording (Python method) — Optional (does not have to be implemented)") and [`StopRecording()`](#tts.core.toolingFramework.userTool.interfaces.UserImagePort.UserImagePort.StopRecording "tts.core.toolingFramework.userTool.interfaces.UserImagePort.UserImagePort.StopRecording (Python method) — Optional (does not have to be implemented)") must be implemented.

Example:

    def StopRecording(self, recordingId: str) -> str:
        # Stop the recording on your tool
        recordingFilePath = self._myUserToolApi.StopRecording()
        return recordingFilePath

Parameters:  recordingId : str[¶](#tts.core.toolingFramework.userTool.interfaces.UserImagePort.UserImagePort.StopRecording.recordingId "Permalink to this definition")  
Identifier for the recording to be stopped. Matches with the recordingId the recording was previously started for.

Returns:  Path to a video file

Return type:  str

## UserTouchInput[¶](#module-tts.core.toolingFramework.userTool.interfaces.UserTouchInput "Link to this heading")

*class* UserTouchInput[¶](#tts.core.toolingFramework.userTool.interfaces.UserTouchInput.UserTouchInput "Link to this definition")  
Describes the interface for touch inputs.

A class that fulfills this interface can be used to extend a [`UserImagePort`](#tts.core.toolingFramework.userTool.interfaces.UserImagePort.UserImagePort "tts.core.toolingFramework.userTool.interfaces.UserImagePort.UserImagePort (Python class) — Bases: UserPort") to allow touch inputs.

GetScreenResolution()[¶](#tts.core.toolingFramework.userTool.interfaces.UserTouchInput.UserTouchInput.GetScreenResolution "Link to this definition")  
Returns the resolution of the screen.

Returns:  Width and height of the screen (width, height).

Return type:  tuple[int, int]

PerformTap(*[action](#tts.core.toolingFramework.userTool.interfaces.UserTouchInput.UserTouchInput.PerformTap.action "tts.core.toolingFramework.userTool.interfaces.UserTouchInput.UserTouchInput.PerformTap.action (Python parameter) — Dictionary that contains parameters for the "Tap" action:")*)[¶](#tts.core.toolingFramework.userTool.interfaces.UserTouchInput.UserTouchInput.PerformTap "Link to this definition")  
*Optional (does not have to be implemented)*

Performs the “Tap” action. Implementing this method indicates that the “Tap” action is supported by this port.

Parameters:  action : dict[str, int | float][¶](#tts.core.toolingFramework.userTool.interfaces.UserTouchInput.UserTouchInput.PerformTap.action "Permalink to this definition")  
Dictionary that contains parameters for the “Tap” action:

- `posX`: x coordinate in pixels

- `posY`: y coordinate in pixels

PerformHold(*[action](#tts.core.toolingFramework.userTool.interfaces.UserTouchInput.UserTouchInput.PerformHold.action "tts.core.toolingFramework.userTool.interfaces.UserTouchInput.UserTouchInput.PerformHold.action (Python parameter) — Dictionary that contains parameters for the "Hold" action:")*)[¶](#tts.core.toolingFramework.userTool.interfaces.UserTouchInput.UserTouchInput.PerformHold "Link to this definition")  
*Optional (does not have to be implemented)*

Performs the “Hold” action. Implementing this method indicates that the “Hold” action is supported by this port.

Parameters:  action : dict[str, int | float][¶](#tts.core.toolingFramework.userTool.interfaces.UserTouchInput.UserTouchInput.PerformHold.action "Permalink to this definition")  
Dictionary that contains parameters for the “Hold” action:

- `posX`: x coordinate in pixels

- `posY`: y coordinate in pixels

- `holdDuration`: hold duration in seconds

PerformMultiTap(*[action](#tts.core.toolingFramework.userTool.interfaces.UserTouchInput.UserTouchInput.PerformMultiTap.action "tts.core.toolingFramework.userTool.interfaces.UserTouchInput.UserTouchInput.PerformMultiTap.action (Python parameter) — Dictionary that contains parameters for the "MultiTap" action:")*)[¶](#tts.core.toolingFramework.userTool.interfaces.UserTouchInput.UserTouchInput.PerformMultiTap "Link to this definition")  
*Optional (does not have to be implemented)*

Performs the “MultiTap” action. Implementing this method indicates that the “MultiTap” action is supported by this port.

Parameters:  action : dict[str, int | float][¶](#tts.core.toolingFramework.userTool.interfaces.UserTouchInput.UserTouchInput.PerformMultiTap.action "Permalink to this definition")  
Dictionary that contains parameters for the “MultiTap” action:

- `posX`: x coordinate in pixels

- `posY`: y coordinate in pixels

- `count`: number of consecutive taps

- `interval`: interval of consecutive taps in seconds

PerformSwipe(*[action](#tts.core.toolingFramework.userTool.interfaces.UserTouchInput.UserTouchInput.PerformSwipe.action "tts.core.toolingFramework.userTool.interfaces.UserTouchInput.UserTouchInput.PerformSwipe.action (Python parameter) — Dictionary that contains parameters for the "Swipe" action:")*)[¶](#tts.core.toolingFramework.userTool.interfaces.UserTouchInput.UserTouchInput.PerformSwipe "Link to this definition")  
*Optional (does not have to be implemented)*

Performs the “Swipe” action. Implementing this method indicates that the “Swipe” action is supported by this port.

Parameters:  action : dict[str, int | float][¶](#tts.core.toolingFramework.userTool.interfaces.UserTouchInput.UserTouchInput.PerformSwipe.action "Permalink to this definition")  
Dictionary that contains parameters for the “Swipe” action:

- `posX`: x coordinate of the start position in pixels

- `posY`: y coordinate of the start position in pixels

- `swipedPosX`: x coordinate of the end position in pixels

- `swipedPosY`: y coordinate of the end position in pixels

- `swipeDuration`: duration of the swipe movement in seconds

PerformMultiSwipe(*[action](#tts.core.toolingFramework.userTool.interfaces.UserTouchInput.UserTouchInput.PerformMultiSwipe.action "tts.core.toolingFramework.userTool.interfaces.UserTouchInput.UserTouchInput.PerformMultiSwipe.action (Python parameter) — Dictionary that contains parameters for the "MultiSwipe" action:")*)[¶](#tts.core.toolingFramework.userTool.interfaces.UserTouchInput.UserTouchInput.PerformMultiSwipe "Link to this definition")  
*Optional (does not have to be implemented)*

Performs the “MultiSwipe” action. Implementing this method indicates that the “MultiSwipe” action is supported by this port.

Parameters:  action : dict[str, int | float][¶](#tts.core.toolingFramework.userTool.interfaces.UserTouchInput.UserTouchInput.PerformMultiSwipe.action "Permalink to this definition")  
Dictionary that contains parameters for the “MultiSwipe” action:

- `posX`: x coordinate of the start position in pixels

- `posY`: y coordinate of the start position in pixels

- `swipedPosX`: x coordinate of the end position in pixels

- `swipedPosY`: y coordinate of the end position in pixels

- `swipeDuration`: duration of the swipe movement in seconds

- `fingerCount`: number of parallel fingers that perform the action

- `fingerDistance`: distance between two parallel fingers

PerformHoldAndSwipe(*[action](#tts.core.toolingFramework.userTool.interfaces.UserTouchInput.UserTouchInput.PerformHoldAndSwipe.action "tts.core.toolingFramework.userTool.interfaces.UserTouchInput.UserTouchInput.PerformHoldAndSwipe.action (Python parameter) — Dictionary that contains parameters for the "HoldAndSwipe" action:")*)[¶](#tts.core.toolingFramework.userTool.interfaces.UserTouchInput.UserTouchInput.PerformHoldAndSwipe "Link to this definition")  
*Optional (does not have to be implemented)*

Performs the “HoldAndSwipe” action. Implementing this method indicates that the “HoldAndSwipe” action is supported by this port.

Parameters:  action : dict[str, int | float][¶](#tts.core.toolingFramework.userTool.interfaces.UserTouchInput.UserTouchInput.PerformHoldAndSwipe.action "Permalink to this definition")  
Dictionary that contains parameters for the “HoldAndSwipe” action:

- `posX`: x coordinate of the start position in pixels

- `posY`: y coordinate of the start position in pixels

- `swipedPosX`: x coordinate of the end position in pixels

- `swipedPosY`: y coordinate of the end position in pixels

- `holdDuration`: duration of the initial hold in seconds

- `swipeDuration`: duration of the swipe movement in seconds

PerformPinch(*[action](#tts.core.toolingFramework.userTool.interfaces.UserTouchInput.UserTouchInput.PerformPinch.action "tts.core.toolingFramework.userTool.interfaces.UserTouchInput.UserTouchInput.PerformPinch.action (Python parameter) — Dictionary that contains parameters for the "Pinch" action:")*)[¶](#tts.core.toolingFramework.userTool.interfaces.UserTouchInput.UserTouchInput.PerformPinch "Link to this definition")  
*Optional (does not have to be implemented)*

Performs the “Pinch” action. Implementing this method indicates that the “Pinch” action is supported by this port.

Parameters:  action : dict[str, int | float][¶](#tts.core.toolingFramework.userTool.interfaces.UserTouchInput.UserTouchInput.PerformPinch.action "Permalink to this definition")  
Dictionary that contains parameters for the “Pinch” action:

- `finger1PosX`: x coordinate of the first finger in pixels

- `finger1PosY`: Y coordinate of the first finger in pixels

- `finger2PosX`: X coordinate of the second finger in pixels

- `finger2PosY`: Y coordinate of the second finger in pixels

- `pinchDuration`: duration of the pinch movement in seconds

- `scaleFactor`: a factor \< 1 means that the fingers are moving towards each other (zoom out) and a factor \> 1 means that the fingers are moving away from each other (zoom in).

PerformRotate(*[action](#tts.core.toolingFramework.userTool.interfaces.UserTouchInput.UserTouchInput.PerformRotate.action "tts.core.toolingFramework.userTool.interfaces.UserTouchInput.UserTouchInput.PerformRotate.action (Python parameter) — Dictionary that contains parameters for the "Rotate" action:")*)[¶](#tts.core.toolingFramework.userTool.interfaces.UserTouchInput.UserTouchInput.PerformRotate "Link to this definition")  
*Optional (does not have to be implemented)*

Performs the “Rotate” action. Implementing this method indicates that the “Rotate” action is supported by this port.

Parameters:  action : dict[str, int | float][¶](#tts.core.toolingFramework.userTool.interfaces.UserTouchInput.UserTouchInput.PerformRotate.action "Permalink to this definition")  
Dictionary that contains parameters for the “Rotate” action:

- `finger1PosX`: x coordinate of the first finger in pixels

- `finger1PosY`: Y coordinate of the first finger in pixels

- `finger2PosX`: X coordinate of the second finger in pixels

- `finger2PosY`: Y coordinate of the second finger in pixels

- `rotationDuration`: duration of the rotate movement in seconds

- `rotationAngle`: rotation angle in degrees

## UserModelPort[¶](#module-tts.core.toolingFramework.userTool.interfaces.UserModelPort "Link to this heading")

*class* VariableInfo[¶](#tts.core.toolingFramework.userTool.interfaces.UserModelPort.VariableInfo "Link to this definition")  
Bases: `TypedDict`

Set of variable specific information that must or can be provided.

Type : Literal['Signal', 'Parameter'][¶](#tts.core.toolingFramework.userTool.interfaces.UserModelPort.VariableInfo.Type "Link to this definition")  
Type of the variable.

- Signal: Variable is read-only

- Parameter: Variable can be read and written

Representation : Literal['Physical', 'Text'][¶](#tts.core.toolingFramework.userTool.interfaces.UserModelPort.VariableInfo.Representation "Link to this definition")  
Representation of the variable value.

Unit : NotRequired[str][¶](#tts.core.toolingFramework.userTool.interfaces.UserModelPort.VariableInfo.Unit "Link to this definition")  
Unit of the variable.

Default: `None`

Description : NotRequired[str][¶](#tts.core.toolingFramework.userTool.interfaces.UserModelPort.VariableInfo.Description "Link to this definition")  
Description of the variable.

Default: `None`

*class* UserModelPort[¶](#tts.core.toolingFramework.userTool.interfaces.UserModelPort.UserModelPort "Link to this definition")  
Bases: [`UserPort`](#tts.core.toolingFramework.userTool.interfaces.UserPort.UserPort "tts.core.toolingFramework.userTool.interfaces.UserPort.UserPort (Python class) — This class describes the interface of a user port. Classes that fulfill this interface can be used as port of a user tool.")

This class describes the interface of a user model port. Classes that fulfill this interface can be used as model port of a user tool.

GetAcquisitionRates()[¶](#tts.core.toolingFramework.userTool.interfaces.UserModelPort.UserModelPort.GetAcquisitionRates "Link to this definition")  
*Optional (does not have to be implemented)*

Returns:  List of available acquisition rates

Return type:  list[str]

GetDefaultAcquisitionRate()[¶](#tts.core.toolingFramework.userTool.interfaces.UserModelPort.UserModelPort.GetDefaultAcquisitionRate "Link to this definition")  
*Optional (does not have to be implemented)*

Returns:  Default acquisition rate

Return type:  str

*classmethod* GetModels()[¶](#tts.core.toolingFramework.userTool.interfaces.UserModelPort.UserModelPort.GetModels "Link to this definition")  
*Optional (does not have to be implemented)*

This method is called to get all available models for test configuration. If it’s implemented, a new property “Model” will be added to your port properties which contains a selected model from this list.

Returns:  list of available models.

Return type:  list[str]

*classmethod* GetPathDelimiter()[¶](#tts.core.toolingFramework.userTool.interfaces.UserModelPort.UserModelPort.GetPathDelimiter "Link to this definition")  
*Optional (does not have to be implemented)*

Character or string to be used for splitting the variable path into its components.

Example:

- Delimiter: `#`

- Path: `A#B#C`

- Components: `A`, `B`, `C`

If this method is not implemented, `/` is used as the default delimiter.

Returns:  Delimiting character or string

Return type:  str

*classmethod* GetRecorder()[¶](#tts.core.toolingFramework.userTool.interfaces.UserModelPort.UserModelPort.GetRecorder "Link to this definition")  
*Optional (does not have to be implemented)*

Class which takes care of the recording of one or more variables.

Returns:  Class which fulfills the [`UserRecorder`](#tts.core.toolingFramework.userTool.interfaces.UserRecorder.UserRecorder "tts.core.toolingFramework.userTool.interfaces.UserRecorder.UserRecorder (Python class) — Bases: object") interface

Return type:  type[[UserRecorder](#tts.core.toolingFramework.userTool.interfaces.UserRecorder.UserRecorder "tts.core.toolingFramework.userTool.interfaces.UserRecorder.UserRecorder (Python class) — Bases: object")]

*classmethod* GetSimulationManager()[¶](#tts.core.toolingFramework.userTool.interfaces.UserModelPort.UserModelPort.GetSimulationManager "Link to this definition")  
*Optional (does not have to be implemented)*

Class that manages the simulation.

Returns:  Class which fulfills the [`UserSimulationManager`](#tts.core.toolingFramework.userTool.interfaces.UserSimulationManager.UserSimulationManager "tts.core.toolingFramework.userTool.interfaces.UserSimulationManager.UserSimulationManager (Python class) — Bases: object") interface

Return type:  type[[UserSimulationManager](#tts.core.toolingFramework.userTool.interfaces.UserSimulationManager.UserSimulationManager "tts.core.toolingFramework.userTool.interfaces.UserSimulationManager.UserSimulationManager (Python class) — Bases: object")]

GetVariables()[¶](#tts.core.toolingFramework.userTool.interfaces.UserModelPort.UserModelPort.GetVariables "Link to this definition")  
Returns all available variables of the port.

The key of the dictionary must be the path of the variable.

The value of the dictionary contains information about the variable.

Example:

    {
        'a/b/c/var': {
            'Type': 'Signal',
            'Representation': 'Physical',
            'Unit': 'km/h'
        }
    }

Returns:  All Variables

Return type:  dict[str, [*VariableInfo*](#tts.core.toolingFramework.userTool.interfaces.UserModelPort.VariableInfo "tts.core.toolingFramework.userTool.interfaces.UserModelPort.VariableInfo (Python class) — Bases: TypedDict")]

GetVariablesHash()[¶](#tts.core.toolingFramework.userTool.interfaces.UserModelPort.UserModelPort.GetVariablesHash "Link to this definition")  
*Optional (does not have to be implemented)*

This hash is intended to provide information on whether the list of variables for this port has changed. The hash is used to decide whether the created cache of model variables needs to be recreated.

If this method is not implemented, the available variables are queried each time the configuration is started.

Returns:  Hash that represents all variables

Return type:  str

Read(*[path](#tts.core.toolingFramework.userTool.interfaces.UserModelPort.UserModelPort.Read.path "tts.core.toolingFramework.userTool.interfaces.UserModelPort.UserModelPort.Read.path (Python parameter) — Path of the variable")*)[¶](#tts.core.toolingFramework.userTool.interfaces.UserModelPort.UserModelPort.Read "Link to this definition")  
This method is called to read the value of a variable.

Info

Currently only scalar values are supported.

Parameters:  path : str[¶](#tts.core.toolingFramework.userTool.interfaces.UserModelPort.UserModelPort.Read.path "Permalink to this definition")  
Path of the variable

Returns:  Current value of the variable

Return type:  str | int | float | bool

RegisterVariable(*[path](#tts.core.toolingFramework.userTool.interfaces.UserModelPort.UserModelPort.RegisterVariable.path "tts.core.toolingFramework.userTool.interfaces.UserModelPort.UserModelPort.RegisterVariable.path (Python parameter) — Path of the variable that is used")*)[¶](#tts.core.toolingFramework.userTool.interfaces.UserModelPort.UserModelPort.RegisterVariable "Link to this definition")  
*Optional (does not have to be implemented)*

This method is called for each variable that is used in a test case. It is called before the test case execution.

Parameters:  path : str[¶](#tts.core.toolingFramework.userTool.interfaces.UserModelPort.UserModelPort.RegisterVariable.path "Permalink to this definition")  
Path of the variable that is used

UnregisterVariable(*[path](#tts.core.toolingFramework.userTool.interfaces.UserModelPort.UserModelPort.UnregisterVariable.path "tts.core.toolingFramework.userTool.interfaces.UserModelPort.UserModelPort.UnregisterVariable.path (Python parameter) — Path of the variable that was used")*)[¶](#tts.core.toolingFramework.userTool.interfaces.UserModelPort.UserModelPort.UnregisterVariable "Link to this definition")  
*Optional (does not have to be implemented)*

This method is called for each variable that was used in a test case. It is called after the test case has been executed.

Parameters:  path : str[¶](#tts.core.toolingFramework.userTool.interfaces.UserModelPort.UserModelPort.UnregisterVariable.path "Permalink to this definition")  
Path of the variable that was used

Write(*[path](#tts.core.toolingFramework.userTool.interfaces.UserModelPort.UserModelPort.Write.path "tts.core.toolingFramework.userTool.interfaces.UserModelPort.UserModelPort.Write.path (Python parameter) — Path of the variable")*, *[value](#tts.core.toolingFramework.userTool.interfaces.UserModelPort.UserModelPort.Write.value "tts.core.toolingFramework.userTool.interfaces.UserModelPort.UserModelPort.Write.value (Python parameter) — Value to be written")*)[¶](#tts.core.toolingFramework.userTool.interfaces.UserModelPort.UserModelPort.Write "Link to this definition")  
This method is called to write the value of a variable.

Info

Currently only scalar values are supported.

Parameters:  path : str[¶](#tts.core.toolingFramework.userTool.interfaces.UserModelPort.UserModelPort.Write.path "Permalink to this definition")  
Path of the variable

value : str | int | float | bool[¶](#tts.core.toolingFramework.userTool.interfaces.UserModelPort.UserModelPort.Write.value "Permalink to this definition")  
Value to be written

## UserRecorder[¶](#module-tts.core.toolingFramework.userTool.interfaces.UserRecorder "Link to this heading")

*class* RecordingVariable[¶](#tts.core.toolingFramework.userTool.interfaces.UserRecorder.RecordingVariable "Link to this definition")  
Bases: `TypedDict`

Set of information that is provided for a variable that is to be recorded.

Path : str[¶](#tts.core.toolingFramework.userTool.interfaces.UserRecorder.RecordingVariable.Path "Link to this definition")  
Path of the variable.

AcquisitionRate : str[¶](#tts.core.toolingFramework.userTool.interfaces.UserRecorder.RecordingVariable.AcquisitionRate "Link to this definition")  
Acquisition rate at which the variable is to be recorded.

*class* UserRecorder[¶](#tts.core.toolingFramework.userTool.interfaces.UserRecorder.UserRecorder "Link to this definition")  
Bases: `object`

Describes the interface of a user recorder. Is used to record one or more variables.

`\_\_init\_\_`(*[port](#tts.core.toolingFramework.userTool.interfaces.UserRecorder.UserRecorder.__init__.port "tts.core.toolingFramework.userTool.interfaces.UserRecorder.UserRecorder.__init__.port (Python parameter) — Port providing this user recorder.")*, *[variables](#tts.core.toolingFramework.userTool.interfaces.UserRecorder.UserRecorder.__init__.variables "tts.core.toolingFramework.userTool.interfaces.UserRecorder.UserRecorder.__init__.variables (Python parameter) — Variables to be recorded by this recorder.")*)[¶](#tts.core.toolingFramework.userTool.interfaces.UserRecorder.UserRecorder.__init__ "Link to this definition")  
Parameters:  port : [UserModelPort](#tts.core.toolingFramework.userTool.interfaces.UserModelPort.UserModelPort "tts.core.toolingFramework.userTool.interfaces.UserModelPort.UserModelPort (Python class) — Bases: UserPort")[¶](#tts.core.toolingFramework.userTool.interfaces.UserRecorder.UserRecorder.__init__.port "Permalink to this definition")  
Port providing this user recorder. Can be used to query the properties of the port, for example.

variables : list[[RecordingVariable](#tts.core.toolingFramework.userTool.interfaces.UserRecorder.RecordingVariable "tts.core.toolingFramework.userTool.interfaces.UserRecorder.RecordingVariable (Python class) — Bases: TypedDict")][¶](#tts.core.toolingFramework.userTool.interfaces.UserRecorder.UserRecorder.__init__.variables "Permalink to this definition")  
Variables to be recorded by this recorder.

Start()[¶](#tts.core.toolingFramework.userTool.interfaces.UserRecorder.UserRecorder.Start "Link to this definition")  
Starts the recording of all variables of the recorder. Can be called several times in a test case.

Stop()[¶](#tts.core.toolingFramework.userTool.interfaces.UserRecorder.UserRecorder.Stop "Link to this definition")  
Stops the recording of all variables of the recorder. Can be called several times in a test case.

Returns:  List with paths to the recording files

Return type:  list[str]

Dispose()[¶](#tts.core.toolingFramework.userTool.interfaces.UserRecorder.UserRecorder.Dispose "Link to this definition")  
*Optional (does not have to be implemented)*

Ends the recorder gracefully.

Is called when the recorder is no longer in use.

## UserSimulationManager[¶](#module-tts.core.toolingFramework.userTool.interfaces.UserSimulationManager "Link to this heading")

*class* UserSimulationManager[¶](#tts.core.toolingFramework.userTool.interfaces.UserSimulationManager.UserSimulationManager "Link to this definition")  
Bases: `object`

Describes the interface of a user simulation manager. Is used to manage the simulation.

`\_\_init\_\_`(*[port](#tts.core.toolingFramework.userTool.interfaces.UserSimulationManager.UserSimulationManager.__init__.port "tts.core.toolingFramework.userTool.interfaces.UserSimulationManager.UserSimulationManager.__init__.port (Python parameter) — Port providing this user simulation manager.")*)[¶](#tts.core.toolingFramework.userTool.interfaces.UserSimulationManager.UserSimulationManager.__init__ "Link to this definition")  
Parameters:  port : [UserModelPort](#tts.core.toolingFramework.userTool.interfaces.UserModelPort.UserModelPort "tts.core.toolingFramework.userTool.interfaces.UserModelPort.UserModelPort (Python class) — Bases: UserPort")[¶](#tts.core.toolingFramework.userTool.interfaces.UserSimulationManager.UserSimulationManager.__init__.port "Permalink to this definition")  
Port providing this user simulation manager. Can be used to query the properties of the port, for example.

GetTime()[¶](#tts.core.toolingFramework.userTool.interfaces.UserSimulationManager.UserSimulationManager.GetTime "Link to this definition")  
Returns the current simulation time.

Returns:  Simulation time in **seconds**

Return type:  float

Step(*[timeDelta](#tts.core.toolingFramework.userTool.interfaces.UserSimulationManager.UserSimulationManager.Step.timeDelta "tts.core.toolingFramework.userTool.interfaces.UserSimulationManager.UserSimulationManager.Step.timeDelta (Python parameter) — Time delta in seconds by which the simulation time will be increased.")*)[¶](#tts.core.toolingFramework.userTool.interfaces.UserSimulationManager.UserSimulationManager.Step "Link to this definition")  
*Optional (does not have to be implemented)*

Executes a sufficient number of simulation steps to increase the simulation time by the given time delta.

Info

This method must be implemented to support the stepwise execution in simulation time.

Parameters:  timeDelta : float[¶](#tts.core.toolingFramework.userTool.interfaces.UserSimulationManager.UserSimulationManager.Step.timeDelta "Permalink to this definition")  
Time delta in **seconds** by which the simulation time will be increased.

SetUpdateTimeCallback(*[callback](#tts.core.toolingFramework.userTool.interfaces.UserSimulationManager.UserSimulationManager.SetUpdateTimeCallback.callback "tts.core.toolingFramework.userTool.interfaces.UserSimulationManager.UserSimulationManager.SetUpdateTimeCallback.callback (Python parameter) — Function with an input parameter.")*)[¶](#tts.core.toolingFramework.userTool.interfaces.UserSimulationManager.UserSimulationManager.SetUpdateTimeCallback "Link to this definition")  
*Optional (does not have to be implemented)*

The callback passed to this method can be used to send an update of the simulation time in **seconds** to ecu.test.

Info

This method must be implemented to support the continuous execution in simulation time.

For example, this method can be executed for every simulation step. However, this method can also be executed only every nth simulation step, for example to reduce the load.

It is important to note that ecu.test expects an update every 120 seconds at the latest  
(real time).

Parameters:  callback : Callable[[int | float], None][¶](#tts.core.toolingFramework.userTool.interfaces.UserSimulationManager.UserSimulationManager.SetUpdateTimeCallback.callback "Permalink to this definition")  
Function with an input parameter. The current simulation time in **seconds** must be passed to this function.

Start()[¶](#tts.core.toolingFramework.userTool.interfaces.UserSimulationManager.UserSimulationManager.Start "Link to this definition")  
*Optional (does not have to be implemented)*

Starts the simulation.

Info

This method must be implemented to support the continuous execution in simulation time.

Pause()[¶](#tts.core.toolingFramework.userTool.interfaces.UserSimulationManager.UserSimulationManager.Pause "Link to this definition")  
*Optional (does not have to be implemented)*

Pauses the simulation.

Dispose()[¶](#tts.core.toolingFramework.userTool.interfaces.UserSimulationManager.UserSimulationManager.Dispose "Link to this definition")  
*Optional (does not have to be implemented)*

Gracefully terminates the simulation.

Is called when the configuration is stopped.

## UserJob[¶](#module-tts.core.toolingFramework.userTool.interfaces.UserJob "Link to this heading")

*class* UserJob[¶](#tts.core.toolingFramework.userTool.interfaces.UserJob.UserJob "Link to this definition")  
This class describes the interface of a user job. It should be used if the list of possible values or the default value of one or more parameters must be determined dynamically.

Call(*[...](#tts.core.toolingFramework.userTool.interfaces.UserJob.UserJob.Call "tts.core.toolingFramework.userTool.interfaces.UserJob.UserJob.Call.... (Python parameter)")*)[¶](#tts.core.toolingFramework.userTool.interfaces.UserJob.UserJob.Call "Link to this definition")  
This method is executed when the job is executed in ecu.test.

Info

The tooltip in ecu.test of the tool job is generated using the docstring and the Python type hints of this method.

`\_\_init\_\_`(*[parent](#tts.core.toolingFramework.userTool.interfaces.UserJob.UserJob.__init__.parent "tts.core.toolingFramework.userTool.interfaces.UserJob.UserJob.__init__.parent (Python parameter) — Jobs are always subordinate to a tool or a port which is passed as the parent class to the user job constructor.")*)[¶](#tts.core.toolingFramework.userTool.interfaces.UserJob.UserJob.__init__ "Link to this definition")  
Parameters:  parent : [UserTool](#tts.core.toolingFramework.userTool.interfaces.UserTool.UserTool "tts.core.toolingFramework.userTool.interfaces.UserTool.UserTool (Python class) — This class describes the interface of a user tool.") | [UserPort](#tts.core.toolingFramework.userTool.interfaces.UserPort.UserPort "tts.core.toolingFramework.userTool.interfaces.UserPort.UserPort (Python class) — This class describes the interface of a user port. Classes that fulfill this interface can be used as port of a user tool.")[¶](#tts.core.toolingFramework.userTool.interfaces.UserJob.UserJob.__init__.parent "Permalink to this definition")  
Jobs are always subordinate to a tool or a port which is passed as the parent class to the user job constructor. Thus, within the job it is possible to access relevant tool or port properties.

*classmethod* GetCategory()[¶](#tts.core.toolingFramework.userTool.interfaces.UserJob.UserJob.GetCategory "Link to this definition")  
*Optional (does not have to be implemented)*

Method to return a job category. Jobs of the same category are grouped together in the ecu.test job panel. Categories can be minimized and expaned for better overview.

Returns:  String representing the job category.

Return type:  str

GetDynamicParameterInformation()[¶](#tts.core.toolingFramework.userTool.interfaces.UserJob.UserJob.GetDynamicParameterInformation "Link to this definition")  
Returns the dynamically determined information for parameters of the [`Call()`](#tts.core.toolingFramework.userTool.interfaces.UserJob.UserJob.Call "tts.core.toolingFramework.userTool.interfaces.UserJob.UserJob.Call (Python method) — This method is executed when the job is executed in ecu.test.") method.

Info

Not all parameters of the [`Call()`](#tts.core.toolingFramework.userTool.interfaces.UserJob.UserJob.Call "tts.core.toolingFramework.userTool.interfaces.UserJob.UserJob.Call (Python method) — This method is executed when the job is executed in ecu.test.") method need to be included. It is sufficient if only parameters with dynamic values are included.

    def GetDynamicParameterInformation(self):
        choices = [chr(i) for i in range(ord('a'), ord('z') + 1)]
        return {
            'param': {
                'Choices': choices,
                'Default': choices[0]
            },
        }

Returns:  Dictionary where the key represents the parameter name and the value contains the dynamically determined values.

Return type:  dict[str, [*DynamicParameterInformation*](#tts.core.toolingFramework.userTool.interfaces.UserJob.DynamicParameterInformation "tts.core.toolingFramework.userTool.interfaces.UserJob.DynamicParameterInformation (Python class) — Bases: TypedDict")]

*class* DynamicParameterInformation[¶](#tts.core.toolingFramework.userTool.interfaces.UserJob.DynamicParameterInformation "Link to this definition")  
Bases: `TypedDict`

Properties of a job that can be determined dynamically.

Choices : NotRequired[list[Any]][¶](#tts.core.toolingFramework.userTool.interfaces.UserJob.DynamicParameterInformation.Choices "Link to this definition")  
List of possible values for a parameter.

Default : NotRequired[Any][¶](#tts.core.toolingFramework.userTool.interfaces.UserJob.DynamicParameterInformation.Default "Link to this definition")  
Default value of the parameter.

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
