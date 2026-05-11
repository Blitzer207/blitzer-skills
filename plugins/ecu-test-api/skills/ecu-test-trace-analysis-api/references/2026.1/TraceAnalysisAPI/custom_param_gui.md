[ Array-based NumPy trace step templates ](array_based_templates.md)

[ Event based tracestep templates ](event_based_templates.md)

[ Stream based tracestep templates ](stream_based_templates.md)

Custom GUI for parameters [ Custom GUI for parameters ](#)

Custom GUI for parameters

- [ ParameterPanel ](#parameterpanel)
  - [C traceAnalysisAPI.ParameterPanel ](#traceAnalysisAPI.ParameterPanel)
    - [M `\_\_init\_\_` ](#traceAnalysisAPI.ParameterPanel.__init__)
    - [M SetupParams ](#traceAnalysisAPI.ParameterPanel.SetupParams)
    - [M OnOk ](#traceAnalysisAPI.ParameterPanel.OnOk)
    - [M StoreParams ](#traceAnalysisAPI.ParameterPanel.StoreParams)
- [ TraceStepDataAPI ](#tracestepdataapi)
  - [C traceAnalysisAPI.TraceStepDataAPI ](#traceAnalysisAPI.TraceStepDataAPI)
    - [M GetSignalNames ](#traceAnalysisAPI.TraceStepDataAPI.GetSignalNames)
    - [M GetSignalDescription ](#traceAnalysisAPI.TraceStepDataAPI.GetSignalDescription)
    - [M GetSignalDirection ](#traceAnalysisAPI.TraceStepDataAPI.GetSignalDirection)
    - [M GetParameterNames ](#traceAnalysisAPI.TraceStepDataAPI.GetParameterNames)
    - [M GetParameterDescription ](#traceAnalysisAPI.TraceStepDataAPI.GetParameterDescription)
    - [M GetParameterType ](#traceAnalysisAPI.TraceStepDataAPI.GetParameterType)
    - [M GetParameterValue ](#traceAnalysisAPI.TraceStepDataAPI.GetParameterValue)
    - [M SetParameterValue ](#traceAnalysisAPI.TraceStepDataAPI.SetParameterValue)

[ Custom trace synchronization ](custom_trace_synchronization.md)

[ Available python libraries and APIs ](python_libraries.md)

Custom GUI for parameters

- [ ParameterPanel ](#parameterpanel)
  - [C traceAnalysisAPI.ParameterPanel ](#traceAnalysisAPI.ParameterPanel)
    - [M `\_\_init\_\_` ](#traceAnalysisAPI.ParameterPanel.__init__)
    - [M SetupParams ](#traceAnalysisAPI.ParameterPanel.SetupParams)
    - [M OnOk ](#traceAnalysisAPI.ParameterPanel.OnOk)
    - [M StoreParams ](#traceAnalysisAPI.ParameterPanel.StoreParams)
- [ TraceStepDataAPI ](#tracestepdataapi)
  - [C traceAnalysisAPI.TraceStepDataAPI ](#traceAnalysisAPI.TraceStepDataAPI)
    - [M GetSignalNames ](#traceAnalysisAPI.TraceStepDataAPI.GetSignalNames)
    - [M GetSignalDescription ](#traceAnalysisAPI.TraceStepDataAPI.GetSignalDescription)
    - [M GetSignalDirection ](#traceAnalysisAPI.TraceStepDataAPI.GetSignalDirection)
    - [M GetParameterNames ](#traceAnalysisAPI.TraceStepDataAPI.GetParameterNames)
    - [M GetParameterDescription ](#traceAnalysisAPI.TraceStepDataAPI.GetParameterDescription)
    - [M GetParameterType ](#traceAnalysisAPI.TraceStepDataAPI.GetParameterType)
    - [M GetParameterValue ](#traceAnalysisAPI.TraceStepDataAPI.GetParameterValue)
    - [M SetParameterValue ](#traceAnalysisAPI.TraceStepDataAPI.SetParameterValue)

# Custom GUI for parameters[¶](#custom-gui-for-parameters "Link to this heading")

Info

**Deprecated:** The TraceStepDataAPI will be adjusted to the Object API in product version 8.0! Affected trace step templates must then be updated.

## ParameterPanel[¶](#parameterpanel "Link to this heading")

*class* traceAnalysisAPI.ParameterPanel[¶](#traceAnalysisAPI.ParameterPanel "Link to this definition")  
Interface to be implemented by a custom parameterization GUI panel. The panel must inherit from wx.Panel or any sub class.

`\_\_init\_\_`(*[parent](#traceAnalysisAPI.ParameterPanel.__init__.parent "traceAnalysisAPI.ParameterPanel.__init__.parent (Python parameter) — The parent window")*)[¶](#traceAnalysisAPI.ParameterPanel.__init__ "Link to this definition")  
Parameters:  parent : wx.Window[¶](#traceAnalysisAPI.ParameterPanel.__init__.parent "Permalink to this definition")  
The parent window

SetupParams(*[traceStepData](#traceAnalysisAPI.ParameterPanel.SetupParams.traceStepData "traceAnalysisAPI.ParameterPanel.SetupParams.traceStepData (Python parameter) — Interface to the trace step data like parameters and signals.")*)[¶](#traceAnalysisAPI.ParameterPanel.SetupParams "Link to this definition")  
Fill your custom GUI with information of the trace step.

Parameters:  traceStepData[¶](#traceAnalysisAPI.ParameterPanel.SetupParams.traceStepData "Permalink to this definition")  
Interface to the trace step data like parameters and signals.

OnOk()[¶](#traceAnalysisAPI.ParameterPanel.OnOk "Link to this definition")  
This method is called if the user clicks the OK button of the trace step dialog. Check the user input here.

Returns:  Returns True if user input is OK and the dialog can be closed, else False.

Return type:  bool

StoreParams(*[traceStepData](#traceAnalysisAPI.ParameterPanel.StoreParams.traceStepData "traceAnalysisAPI.ParameterPanel.StoreParams.traceStepData (Python parameter) — Interface to the trace step data like parameters and signals.")*)[¶](#traceAnalysisAPI.ParameterPanel.StoreParams "Link to this definition")  
Collect the information of your custom GUI and update the parameterization accordingly via [`TraceStepDataAPI.SetParameterValue()`](#traceAnalysisAPI.TraceStepDataAPI.SetParameterValue "traceAnalysisAPI.TraceStepDataAPI.SetParameterValue (Python method) — Sets a new value for a given parameter. Values can only be assigned to parameters with direction IN.")

Parameters:  traceStepData[¶](#traceAnalysisAPI.ParameterPanel.StoreParams.traceStepData "Permalink to this definition")  
Interface to the trace step data like parameters and signals.

## TraceStepDataAPI[¶](#tracestepdataapi "Link to this heading")

*class* traceAnalysisAPI.TraceStepDataAPI[¶](#traceAnalysisAPI.TraceStepDataAPI "Link to this definition")  
The TraceStepDataAPI provides functions to access information about parameters and signals of a trace step and it’s underlying trace step prototype. The API allows changing values of parameters as well. It is used to develop a custom user interface for trace steps.

GetSignalNames()[¶](#traceAnalysisAPI.TraceStepDataAPI.GetSignalNames "Link to this definition")  
Returns a list of signal names used in the trace step.

Return type:  list[str]

GetSignalDescription(*[sigName](#traceAnalysisAPI.TraceStepDataAPI.GetSignalDescription.sigName "traceAnalysisAPI.TraceStepDataAPI.GetSignalDescription.sigName (Python parameter) — The name of the desired signal.")*)[¶](#traceAnalysisAPI.TraceStepDataAPI.GetSignalDescription "Link to this definition")  
Returns the description for a given signal.

Parameters:  sigName : str[¶](#traceAnalysisAPI.TraceStepDataAPI.GetSignalDescription.sigName "Permalink to this definition")  
The name of the desired signal.

Return type:  str

GetSignalDirection(*[sigName](#traceAnalysisAPI.TraceStepDataAPI.GetSignalDirection.sigName "traceAnalysisAPI.TraceStepDataAPI.GetSignalDirection.sigName (Python parameter) — The name of the desired signal.")*)[¶](#traceAnalysisAPI.TraceStepDataAPI.GetSignalDirection "Link to this definition")  
Returns the direction for a given signal.

Parameters:  sigName : str[¶](#traceAnalysisAPI.TraceStepDataAPI.GetSignalDirection.sigName "Permalink to this definition")  
The name of the desired signal.

Returns:  IN or OUT

Return type:  str

GetParameterNames()[¶](#traceAnalysisAPI.TraceStepDataAPI.GetParameterNames "Link to this definition")  
Returns a list of parameter names used in the trace step.

Return type:  list[str]

GetParameterDescription(*[paramName](#traceAnalysisAPI.TraceStepDataAPI.GetParameterDescription.paramName "traceAnalysisAPI.TraceStepDataAPI.GetParameterDescription.paramName (Python parameter) — the name of the desired parameter")*)[¶](#traceAnalysisAPI.TraceStepDataAPI.GetParameterDescription "Link to this definition")  
Returns the description for a given parameter.

Parameters:  paramName : str[¶](#traceAnalysisAPI.TraceStepDataAPI.GetParameterDescription.paramName "Permalink to this definition")  
the name of the desired parameter

Return type:  str

GetParameterType(*[paramName](#traceAnalysisAPI.TraceStepDataAPI.GetParameterType.paramName "traceAnalysisAPI.TraceStepDataAPI.GetParameterType.paramName (Python parameter) — The name of the desired parameter.")*)[¶](#traceAnalysisAPI.TraceStepDataAPI.GetParameterType "Link to this definition")  
Returns the type for a given parameter.

Parameters:  paramName : str[¶](#traceAnalysisAPI.TraceStepDataAPI.GetParameterType.paramName "Permalink to this definition")  
The name of the desired parameter.

Returns:  INTEGER, FLOAT, STRING, BOOLEAN, PYOBJECT

Return type:  str

GetParameterValue(*[paramName](#traceAnalysisAPI.TraceStepDataAPI.GetParameterValue.paramName "traceAnalysisAPI.TraceStepDataAPI.GetParameterValue.paramName (Python parameter) — The name of the desired parameter.")*)[¶](#traceAnalysisAPI.TraceStepDataAPI.GetParameterValue "Link to this definition")  
Returns the current value for a given parameter.

Parameters:  paramName : str[¶](#traceAnalysisAPI.TraceStepDataAPI.GetParameterValue.paramName "Permalink to this definition")  
The name of the desired parameter.

Return type:  Value or None

SetParameterValue(*[paramName](#traceAnalysisAPI.TraceStepDataAPI.SetParameterValue.paramName "traceAnalysisAPI.TraceStepDataAPI.SetParameterValue.paramName (Python parameter) — The name of the desired parameter.")*, *[value](#traceAnalysisAPI.TraceStepDataAPI.SetParameterValue.value "traceAnalysisAPI.TraceStepDataAPI.SetParameterValue.value (Python parameter) — The new parameter value.")*)[¶](#traceAnalysisAPI.TraceStepDataAPI.SetParameterValue "Link to this definition")  
Sets a new value for a given parameter. Values can only be assigned to parameters with direction IN.

Parameters:  paramName : str[¶](#traceAnalysisAPI.TraceStepDataAPI.SetParameterValue.paramName "Permalink to this definition")  
The name of the desired parameter.

value : str|int|float|bool[¶](#traceAnalysisAPI.TraceStepDataAPI.SetParameterValue.value "Permalink to this definition")  
The new parameter value.

Returns:  True on success, otherwise False

Return type:  bool

Raises:  
- **TypeError** – Invalid type for parameter value.

- **ValueError** – Invalid assignment to OUT parameter.

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
