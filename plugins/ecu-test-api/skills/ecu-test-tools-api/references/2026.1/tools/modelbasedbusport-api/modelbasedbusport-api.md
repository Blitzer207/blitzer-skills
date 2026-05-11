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

[ User Tool API ](../usertool-api/usertool-api.md)

Model-based Bus Port API [ Model-based Bus Port API ](#)

Model-based Bus Port API

- [ BusToModelPathResolver ](#module-tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver)
  - [C BusToModelPathResolver ](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.BusToModelPathResolver)
    - [M `\_\_init\_\_` ](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.BusToModelPathResolver.__init__)
    - [M GetName ](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.BusToModelPathResolver.GetName)
    - [M GetProperties ](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.BusToModelPathResolver.GetProperties)
    - [M GetSettings ](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.BusToModelPathResolver.GetSettings)
    - [M GetConstants ](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.BusToModelPathResolver.GetConstants)
    - [M IsCrcSignal ](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.BusToModelPathResolver.IsCrcSignal)
    - [M IsAliveSignal ](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.BusToModelPathResolver.IsAliveSignal)
    - [M GetTxPath ](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.BusToModelPathResolver.GetTxPath)
    - [M GetRxPath ](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.BusToModelPathResolver.GetRxPath)
    - [M GetTxSwitchPath ](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.BusToModelPathResolver.GetTxSwitchPath)
    - [M GetPduEnablePath ](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.BusToModelPathResolver.GetPduEnablePath)
    - [M GetPduEnableSwitchPath ](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.BusToModelPathResolver.GetPduEnableSwitchPath)
    - [M GetFeatureSwitchPath ](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.BusToModelPathResolver.GetFeatureSwitchPath)
    - [M GetFeatureSwitchSwitchPath ](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.BusToModelPathResolver.GetFeatureSwitchSwitchPath)
    - [M GetPduTimingPath ](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.BusToModelPathResolver.GetPduTimingPath)
    - [M GetPduTimingSwitchPath ](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.BusToModelPathResolver.GetPduTimingSwitchPath)
- [ Settings ](#settings)
  - [C Settings ](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.Settings)
    - [A TxSwitchBehavior ](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.Settings.TxSwitchBehavior)
    - [A RestoreBehaviour ](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.Settings.RestoreBehaviour)
    - [A AlterPduTimingSupport ](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.Settings.AlterPduTimingSupport)
    - [A PduCycleTimeFactor ](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.Settings.PduCycleTimeFactor)
    - [A FeatureSwitchSupport ](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.Settings.FeatureSwitchSupport)
- [ Constants ](#constants)
  - [C Constants ](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.Constants)
    - [A DeactivateCrcSignalManipulation ](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.Constants.DeactivateCrcSignalManipulation)
    - [A ActivateCrcSignalManipulation ](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.Constants.ActivateCrcSignalManipulation)
    - [A DeactivateAliveSignalManipulation ](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.Constants.DeactivateAliveSignalManipulation)
    - [A ActivateAliveSignalManipulation ](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.Constants.ActivateAliveSignalManipulation)
    - [A DeactivateSignalManipulation ](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.Constants.DeactivateSignalManipulation)
    - [A ActivateSignalManipulation ](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.Constants.ActivateSignalManipulation)
    - [A NoneFeatureSwitchValue ](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.Constants.NoneFeatureSwitchValue)
    - [A OverwritePermanentlyFeatureSwitchValue ](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.Constants.OverwritePermanentlyFeatureSwitchValue)
    - [A DisablePdu ](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.Constants.DisablePdu)
    - [A EnablePdu ](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.Constants.EnablePdu)

[ User test management ](../../userTestmanagement/index.md)

[ UserUtility API ](../../user-utility/user-utility.md)

[ Utility Examples ](../../user-utility/example-utilities.md)

Model-based Bus Port API

- [ BusToModelPathResolver ](#module-tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver)
  - [C BusToModelPathResolver ](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.BusToModelPathResolver)
    - [M `\_\_init\_\_` ](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.BusToModelPathResolver.__init__)
    - [M GetName ](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.BusToModelPathResolver.GetName)
    - [M GetProperties ](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.BusToModelPathResolver.GetProperties)
    - [M GetSettings ](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.BusToModelPathResolver.GetSettings)
    - [M GetConstants ](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.BusToModelPathResolver.GetConstants)
    - [M IsCrcSignal ](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.BusToModelPathResolver.IsCrcSignal)
    - [M IsAliveSignal ](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.BusToModelPathResolver.IsAliveSignal)
    - [M GetTxPath ](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.BusToModelPathResolver.GetTxPath)
    - [M GetRxPath ](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.BusToModelPathResolver.GetRxPath)
    - [M GetTxSwitchPath ](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.BusToModelPathResolver.GetTxSwitchPath)
    - [M GetPduEnablePath ](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.BusToModelPathResolver.GetPduEnablePath)
    - [M GetPduEnableSwitchPath ](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.BusToModelPathResolver.GetPduEnableSwitchPath)
    - [M GetFeatureSwitchPath ](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.BusToModelPathResolver.GetFeatureSwitchPath)
    - [M GetFeatureSwitchSwitchPath ](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.BusToModelPathResolver.GetFeatureSwitchSwitchPath)
    - [M GetPduTimingPath ](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.BusToModelPathResolver.GetPduTimingPath)
    - [M GetPduTimingSwitchPath ](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.BusToModelPathResolver.GetPduTimingSwitchPath)
- [ Settings ](#settings)
  - [C Settings ](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.Settings)
    - [A TxSwitchBehavior ](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.Settings.TxSwitchBehavior)
    - [A RestoreBehaviour ](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.Settings.RestoreBehaviour)
    - [A AlterPduTimingSupport ](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.Settings.AlterPduTimingSupport)
    - [A PduCycleTimeFactor ](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.Settings.PduCycleTimeFactor)
    - [A FeatureSwitchSupport ](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.Settings.FeatureSwitchSupport)
- [ Constants ](#constants)
  - [C Constants ](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.Constants)
    - [A DeactivateCrcSignalManipulation ](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.Constants.DeactivateCrcSignalManipulation)
    - [A ActivateCrcSignalManipulation ](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.Constants.ActivateCrcSignalManipulation)
    - [A DeactivateAliveSignalManipulation ](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.Constants.DeactivateAliveSignalManipulation)
    - [A ActivateAliveSignalManipulation ](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.Constants.ActivateAliveSignalManipulation)
    - [A DeactivateSignalManipulation ](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.Constants.DeactivateSignalManipulation)
    - [A ActivateSignalManipulation ](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.Constants.ActivateSignalManipulation)
    - [A NoneFeatureSwitchValue ](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.Constants.NoneFeatureSwitchValue)
    - [A OverwritePermanentlyFeatureSwitchValue ](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.Constants.OverwritePermanentlyFeatureSwitchValue)
    - [A DisablePdu ](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.Constants.DisablePdu)
    - [A EnablePdu ](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.Constants.EnablePdu)

# Model-based Bus Port API[¶](#model-based-bus-port-api "Link to this heading")

## BusToModelPathResolver[¶](#module-tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver "Link to this heading")

*class* BusToModelPathResolver[¶](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.BusToModelPathResolver "Link to this definition")  
This class describes the interface of a BusToModelPathResolver.

In order for ecu.test to recognize a class as a `BusToModelPathResolver`, the class must meet the requirements of this interface. In addition, the `MODULE_TYPE` must be set to `BUS_TO_MODEL_PATH_RESOLVER`.

    import ...

    MODULE_TYPE = 'BUS_TO_MODEL_PATH_RESOLVER'

    class MyBusToModelPathResolver:
        def __init__(self, properties: dict[str, str | bool]) -> None:
            ...

`\_\_init\_\_`(*[properties](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.BusToModelPathResolver.__init__.properties "tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.BusToModelPathResolver.__init__.properties (Python parameter) — Dictionary with the properties from the test bench configuration for this BusToModelPathResolver and the configured values.")*)[¶](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.BusToModelPathResolver.__init__ "Link to this definition")  
Parameters:  properties : dict[str, str | bool][¶](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.BusToModelPathResolver.__init__.properties "Permalink to this definition")  
Dictionary with the properties from the test bench configuration for this BusToModelPathResolver and the configured values. The possible properties are defined by the return value of the [`GetProperties()`](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.BusToModelPathResolver.GetProperties "tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.BusToModelPathResolver.GetProperties (Python method) — Optional (does not have to be implemented)") method.

*classmethod* GetName()[¶](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.BusToModelPathResolver.GetName "Link to this definition")  
Provides the name of the BusToModelPathResolver. This name is displayed as the implementation type of a bus port for tools that support this type of port.

Returns:  Name of the port

Return type:  str

*classmethod* GetProperties()[¶](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.BusToModelPathResolver.GetProperties "Link to this definition")  
*Optional (does not have to be implemented)*

Properties of the custom BusToModelPathResolver. These properties can be configured in the test bench configuration. The configured properties are passed to the custom BusToModelPathResolver constructor when the configuration is started. Available property types are STRING, BOOL and CHOICE. Properties may be sorted into groups to improve visual separation in the test bench configuration.

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
                    'Type': 'BOOL',
                    'Default': True,
                },
                'Option 3': {
                    'Description': 'This is Option 3',
                    'Type': 'CHOICE',
                    'Choices': ['c1', 'c2', 'c3'],
                    'Default': 'c2',
                },
            }
        }

The above example will generate the following properties:

![](../../_images/UserTool_GetProperties.png)

\

Returns:  Dictionary with properties of the custom BusToModelPathResolver.

Return type:  dict[str, dict]

GetSettings()[¶](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.BusToModelPathResolver.GetSettings "Link to this definition")  
*Optional (does not have to be implemented)*

Can be used to overwrite the default values of certain settings. If a setting is not overwritten, its default value is used.

Returns:  Dictionary with new settings

Return type:  [*Settings*](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.Settings "tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.Settings (Python class) — Bases: TypedDict")

GetConstants()[¶](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.BusToModelPathResolver.GetConstants "Link to this definition")  
*Optional (does not have to be implemented)*

Can be used to overwrite the default values of certain constants. If a constant is not overwritten, its default value is used.

Returns:  Dictionary with new constant values

Return type:  [*Constants*](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.Constants "tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.Constants (Python class) — Bases: TypedDict")

IsCrcSignal(*[busEntity](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.BusToModelPathResolver.IsCrcSignal.busEntity "tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.BusToModelPathResolver.IsCrcSignal.busEntity (Python parameter) — bus entity to be checked")*)[¶](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.BusToModelPathResolver.IsCrcSignal "Link to this definition")  
True if the bus entity object is a CRC signal.

Parameters:  busEntity : [BusEntity](../../general_api/api.md#tts.core.api.dataBrowserApi.DataBrowser.BusEntity "tts.core.api.dataBrowserApi.DataBrowser.BusEntity (Python class) — The BusEntity type represents one entry in a bus database")[¶](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.BusToModelPathResolver.IsCrcSignal.busEntity "Permalink to this definition")  
bus entity to be checked

Returns:  True if the bus entity belongs to a CRC signal

Return type:  bool

IsAliveSignal(*[busEntity](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.BusToModelPathResolver.IsAliveSignal.busEntity "tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.BusToModelPathResolver.IsAliveSignal.busEntity (Python parameter) — bus entity to be checked")*)[¶](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.BusToModelPathResolver.IsAliveSignal "Link to this definition")  
True if the bus entity object is an alive signal.

Parameters:  busEntity : [BusEntity](../../general_api/api.md#tts.core.api.dataBrowserApi.DataBrowser.BusEntity "tts.core.api.dataBrowserApi.DataBrowser.BusEntity (Python class) — The BusEntity type represents one entry in a bus database")[¶](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.BusToModelPathResolver.IsAliveSignal.busEntity "Permalink to this definition")  
bus entity to be checked

Returns:  True if the bus entity belongs to an alive signal

Return type:  bool

GetTxPath(*[busEntity](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.BusToModelPathResolver.GetTxPath.busEntity "tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.BusToModelPathResolver.GetTxPath.busEntity (Python parameter) — bus entity describing a bus signal")*)[¶](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.BusToModelPathResolver.GetTxPath "Link to this definition")  
Returns the model path for manipulation when a Write, Stimulate or Reset test step is executed on a bus signal. The setpoint value will be written to that model path. Such a model path is called Tx or transmission path in this context because it typically denotes a variable that is transmitted by the model as part of a restbus simulation.

For some models it is necessary to activate the manipulation by changing another model value. The path for that can be specified within the implemetation of [`GetTxSwitchPath()`](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.BusToModelPathResolver.GetTxSwitchPath "tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.BusToModelPathResolver.GetTxSwitchPath (Python method) — Optional (does not have to be implemented)").

Parameters:  busEntity : [BusEntity](../../general_api/api.md#tts.core.api.dataBrowserApi.DataBrowser.BusEntity "tts.core.api.dataBrowserApi.DataBrowser.BusEntity (Python class) — The BusEntity type represents one entry in a bus database")[¶](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.BusToModelPathResolver.GetTxPath.busEntity "Permalink to this definition")  
bus entity describing a bus signal

Returns:  The write path for the given bus entity

Return type:  str

GetRxPath(*[busEntity](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.BusToModelPathResolver.GetRxPath.busEntity "tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.BusToModelPathResolver.GetRxPath.busEntity (Python parameter) — bus entity describing a bus signal")*)[¶](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.BusToModelPathResolver.GetRxPath "Link to this definition")  
Returns the model path with the current value when a Read test step is executed on a bus signal. Such a model path is called Rx or receive path because it typically denotes a variable that is received by the model.

Parameters:  busEntity : [BusEntity](../../general_api/api.md#tts.core.api.dataBrowserApi.DataBrowser.BusEntity "tts.core.api.dataBrowserApi.DataBrowser.BusEntity (Python class) — The BusEntity type represents one entry in a bus database")[¶](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.BusToModelPathResolver.GetRxPath.busEntity "Permalink to this definition")  
bus entity describing a bus signal

Returns:  The read path for the given bus entity

Return type:  str

GetTxSwitchPath(*[busEntity](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.BusToModelPathResolver.GetTxSwitchPath.busEntity "tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.BusToModelPathResolver.GetTxSwitchPath.busEntity (Python parameter) — bus entity describing a bus signal")*)[¶](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.BusToModelPathResolver.GetTxSwitchPath "Link to this definition")  
*Optional (does not have to be implemented)*

Returns the model path for manipulation activation when a Write, Stimulate or Reset test step is executed on a bus signal.

Such model paths are called switch or control, as they switch the source for the associated bus signal from the model to a constant or vice versa.

The value that will be written to that model path depends on the test step. Depending on the signal being an alive, CRC or standard signal the value is one of the following:

- physical input, set for Write/Stimulate

  - `Constants.ActivateSignalManipulation`

  - `Constants.ActivateCrcSignalManipulation`

  - `Constants.ActivateAliveSignalManipulation`

- simulation or calculation by the model, set for Reset:

  - `Constants.DeactivateSignalManipulation`

  - `Constants.DeactivateCrcSignalManipulation`

  - `Constants.DeactivateAliveSignalManipulation`

Illustration of a switch:

[![](../../_images/ModelBasedBusPort_TxSwitch.png)](../../_images/ModelBasedBusPort_TxSwitch.png)

\

Parameters:  busEntity : [BusEntity](../../general_api/api.md#tts.core.api.dataBrowserApi.DataBrowser.BusEntity "tts.core.api.dataBrowserApi.DataBrowser.BusEntity (Python class) — The BusEntity type represents one entry in a bus database")[¶](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.BusToModelPathResolver.GetTxSwitchPath.busEntity "Permalink to this definition")  
bus entity describing a bus signal

Returns:  Control write path for the given bus entity

Return type:  str | None

GetPduEnablePath(*[busEntity](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.BusToModelPathResolver.GetPduEnablePath.busEntity "tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.BusToModelPathResolver.GetPduEnablePath.busEntity (Python parameter) — bus entity object describing a bus signal")*)[¶](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.BusToModelPathResolver.GetPduEnablePath "Link to this definition")  
Returns the model path for enabling or disabling a PDU.

The value that will be written to that model path depends on the action:

- `Constants.EnablePdu`: PDU is being enabled

- `Constants.DisablePdu`: PDU is being disabled

Parameters:  busEntity : [BusEntity](../../general_api/api.md#tts.core.api.dataBrowserApi.DataBrowser.BusEntity "tts.core.api.dataBrowserApi.DataBrowser.BusEntity (Python class) — The BusEntity type represents one entry in a bus database")[¶](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.BusToModelPathResolver.GetPduEnablePath.busEntity "Permalink to this definition")  
bus entity object describing a bus signal

Returns:  PDU enable write path for the given bus entity

Return type:  str

GetPduEnableSwitchPath(*[busEntity](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.BusToModelPathResolver.GetPduEnableSwitchPath.busEntity "tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.BusToModelPathResolver.GetPduEnableSwitchPath.busEntity (Python parameter) — bus entity object describing a bus signal")*)[¶](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.BusToModelPathResolver.GetPduEnableSwitchPath "Link to this definition")  
Returns the model path for the activation of the corresponding signal that enables or disables a PDU, see GetPduEnablePath.

The value that will be written to that model path depends on the action:

- `Constants.ActivateSignalManipulation`: activates the corresponding signal

- `Constants.DeactivateSignalManipulation`: deactivates the corresponding signal

Parameters:  busEntity : [BusEntity](../../general_api/api.md#tts.core.api.dataBrowserApi.DataBrowser.BusEntity "tts.core.api.dataBrowserApi.DataBrowser.BusEntity (Python class) — The BusEntity type represents one entry in a bus database")[¶](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.BusToModelPathResolver.GetPduEnableSwitchPath.busEntity "Permalink to this definition")  
bus entity object describing a bus signal

Returns:  PDU enable switch write path for the given bus entity

Return type:  str | None

GetFeatureSwitchPath(*[busEntity](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.BusToModelPathResolver.GetFeatureSwitchPath.busEntity "tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.BusToModelPathResolver.GetFeatureSwitchPath.busEntity (Python parameter) — bus entity object describing a bus signal")*)[¶](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.BusToModelPathResolver.GetFeatureSwitchPath "Link to this definition")  
*Optional (does not have to be implemented)*

Returns the model path for enabling or disabling a feature switch.

The value that will be written to that model path depends on the action:

- `Constants.OverwritePermanentlyFeatureSwitchValue`: feature switch is being enabled

- `Constants.NoneFeatureSwitchValue`: feature switch is being disabled

Parameters:  busEntity : [BusEntity](../../general_api/api.md#tts.core.api.dataBrowserApi.DataBrowser.BusEntity "tts.core.api.dataBrowserApi.DataBrowser.BusEntity (Python class) — The BusEntity type represents one entry in a bus database")[¶](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.BusToModelPathResolver.GetFeatureSwitchPath.busEntity "Permalink to this definition")  
bus entity object describing a bus signal

Returns:  Feature switch write path for the given bus entity

Return type:  str

GetFeatureSwitchSwitchPath(*[busEntity](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.BusToModelPathResolver.GetFeatureSwitchSwitchPath.busEntity "tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.BusToModelPathResolver.GetFeatureSwitchSwitchPath.busEntity (Python parameter) — bus entity object describing a bus signal")*)[¶](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.BusToModelPathResolver.GetFeatureSwitchSwitchPath "Link to this definition")  
*Optional (does not have to be implemented)*

Returns the model path for the activation of the corresponding signal that enables or disables a feature switch, see GetFeatureSwitchPath.

The value that will be written to that model path depends on the action:

- `Constants.ActivateSignalManipulation`: activates the corresponding signal

- `Constants.DeactivateSignalManipulation`: deactivates the corresponding signal

Parameters:  busEntity : [BusEntity](../../general_api/api.md#tts.core.api.dataBrowserApi.DataBrowser.BusEntity "tts.core.api.dataBrowserApi.DataBrowser.BusEntity (Python class) — The BusEntity type represents one entry in a bus database")[¶](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.BusToModelPathResolver.GetFeatureSwitchSwitchPath.busEntity "Permalink to this definition")  
bus entity object describing a bus signal

Returns:  Feature switch switch write path for the given bus entity

Return type:  str | None

GetPduTimingPath(*[busEntity](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.BusToModelPathResolver.GetPduTimingPath.busEntity "tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.BusToModelPathResolver.GetPduTimingPath.busEntity (Python parameter) — bus entity object describing a bus signal")*)[¶](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.BusToModelPathResolver.GetPduTimingPath "Link to this definition")  
*Optional (does not have to be implemented)*

Returns the model path used to control the PDU timing in a Change Timing test step.

Parameters:  busEntity : [BusEntity](../../general_api/api.md#tts.core.api.dataBrowserApi.DataBrowser.BusEntity "tts.core.api.dataBrowserApi.DataBrowser.BusEntity (Python class) — The BusEntity type represents one entry in a bus database")[¶](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.BusToModelPathResolver.GetPduTimingPath.busEntity "Permalink to this definition")  
bus entity object describing a bus signal

Returns:  PDU timing write path for the given bus entity

Return type:  str

GetPduTimingSwitchPath(*[busEntity](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.BusToModelPathResolver.GetPduTimingSwitchPath.busEntity "tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.BusToModelPathResolver.GetPduTimingSwitchPath.busEntity (Python parameter) — bus entity object describing a bus signal")*)[¶](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.BusToModelPathResolver.GetPduTimingSwitchPath "Link to this definition")  
*Optional (does not have to be implemented)*

Returns the model path for the activation of the corresponding signal that controls the PDU timing, see GetPduTimingPath.

The value that will be written to that model path depends on the action:

- `Constants.ActivateSignalManipulation`: activates the corresponding signal

- `Constants.DeactivateSignalManipulation`: deactivates the corresponding signal

Parameters:  busEntity : [BusEntity](../../general_api/api.md#tts.core.api.dataBrowserApi.DataBrowser.BusEntity "tts.core.api.dataBrowserApi.DataBrowser.BusEntity (Python class) — The BusEntity type represents one entry in a bus database")[¶](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.BusToModelPathResolver.GetPduTimingSwitchPath.busEntity "Permalink to this definition")  
bus entity object describing a bus signal

Returns:  PDU timing switch write path for the given bus entity

Return type:  str | None

## Settings[¶](#settings "Link to this heading")

*class* Settings[¶](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.Settings "Link to this definition")  
Bases: `TypedDict`

Possible settings.

All settings are optional. This means that they do not have to be set explicitly. Each setting has a default value. If the setting is not set, the default value is used.

TxSwitchBehavior : NotRequired[Literal['BeforeConst', 'AfterConst']][¶](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.Settings.TxSwitchBehavior "Link to this definition")  
Determines the behavior, whether the switch is written before or after the constant.

Default: `AfterConst`

RestoreBehaviour : NotRequired[Literal['Default', 'SwitchModel']][¶](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.Settings.RestoreBehaviour "Link to this definition")  
Determines the behavior when performing a reset.

- `Default` Both switch and const value are reset to their initial values.

- `SwitchModel` The switch will always be reset to “use the calculated value”. The const value is not changed.

Default: `Default`

AlterPduTimingSupport : NotRequired[bool][¶](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.Settings.AlterPduTimingSupport "Link to this definition")  
Indicates whether the BusToModelPathResolver implementation and the associated model port supports setting the PDU timing.

Activating this setting means that the [`BusToModelPathResolver.GetPduTimingPath()`](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.BusToModelPathResolver.GetPduTimingPath "tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.BusToModelPathResolver.GetPduTimingPath (Python method) — Optional (does not have to be implemented)") method must be implemented.

Default: `False`

PduCycleTimeFactor : NotRequired[float][¶](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.Settings.PduCycleTimeFactor "Link to this definition")  
Factor by which the cycle time is multiplied. ecu.test writes the cycle time in milliseconds. This factor can be used to change the unit of the cycle time.

If, for example, the value should be written in seconds instead of milliseconds, the factor 0.001 can be used:

1000ms \* 0.001 = 1.0s

Default: `1.0`

FeatureSwitchSupport : NotRequired[bool][¶](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.Settings.FeatureSwitchSupport "Link to this definition")  
Indicates whether the BusToModelPathResolver implementation and the associated model port supports FeatureSwitches. FeatureSwitches are a feature of *dSPACE BusManager*.

Activating this setting means that the [`BusToModelPathResolver.GetFeatureSwitchPath()`](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.BusToModelPathResolver.GetFeatureSwitchPath "tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.BusToModelPathResolver.GetFeatureSwitchPath (Python method) — Optional (does not have to be implemented)") method must be implemented.

Default: `False`

## Constants[¶](#constants "Link to this heading")

*class* Constants[¶](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.Constants "Link to this definition")  
Bases: `TypedDict`

Possible constants.

All constants are optional. This means that they do not have to be set explicitly. Each constant has a default value. If the constant is not set, the default value is used.

DeactivateCrcSignalManipulation : NotRequired[int][¶](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.Constants.DeactivateCrcSignalManipulation "Link to this definition")  
This value is written to the switch in order to set the switch back to simulation as the source for the CRC signal.

Default: `0`

ActivateCrcSignalManipulation : NotRequired[int][¶](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.Constants.ActivateCrcSignalManipulation "Link to this definition")  
This value is written to the switch in order to set the switch to a constant value as the source for the CRC signal.

Default: `1`

DeactivateAliveSignalManipulation : NotRequired[int][¶](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.Constants.DeactivateAliveSignalManipulation "Link to this definition")  
This value is written to the switch in order to set the switch back to simulation as the source for the alive signal.

Default: `0`

ActivateAliveSignalManipulation : NotRequired[int][¶](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.Constants.ActivateAliveSignalManipulation "Link to this definition")  
This value is written to the switch in order to set the switch to a constant value as the source for the alive signal.

Default: `1`

DeactivateSignalManipulation : NotRequired[int][¶](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.Constants.DeactivateSignalManipulation "Link to this definition")  
This value is written to the switch in order to set the switch back to simulation as the source for the signal.

Default: `0`

ActivateSignalManipulation : NotRequired[int][¶](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.Constants.ActivateSignalManipulation "Link to this definition")  
This value is written to the switch in order to set the switch to a constant value as the source for the signal.

Default: `1`

NoneFeatureSwitchValue : NotRequired[int][¶](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.Constants.NoneFeatureSwitchValue "Link to this definition")  
This value is written to the FeatureSwitch in order to set it to None.

Default: `0`

OverwritePermanentlyFeatureSwitchValue : NotRequired[int][¶](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.Constants.OverwritePermanentlyFeatureSwitchValue "Link to this definition")  
This value is written to the FeatureSwitch in order to permanently enable it.

Default: `1`

DisablePdu : NotRequired[int][¶](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.Constants.DisablePdu "Link to this definition")  
This value is written to the PDU enable path in order to deactivate PDUs.

Default: `0`

EnablePdu : NotRequired[int][¶](#tts.tooling.common.modelBasedBusAccess.BusToModelPathResolver.Constants.EnablePdu "Link to this definition")  
This value is written to the PDU enable path in order to enable PDUs.

Default: `1`

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
