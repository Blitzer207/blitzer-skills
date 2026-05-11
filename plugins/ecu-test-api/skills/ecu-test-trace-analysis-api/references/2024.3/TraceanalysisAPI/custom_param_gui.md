# Custom GUI for parameters[¶](#custom-gui-for-parameters "Link to this heading")

Note

**Deprecated:** The TraceStepDataAPI will be adjusted to the Object API in product version 8.0! Affected trace step templates must then be updated.

## ParameterPanel[¶](#parameterpanel "Link to this heading")

*class* traceAnalysisAPI.ParameterPanel[¶](#traceAnalysisAPI.ParameterPanel "Link to this definition")  
Interface to be implemented by a custom parameterization GUI panel. The panel must inherit from wx.Panel or any sub class.

`\_\_init\_\_`(*parent*)[¶](#traceAnalysisAPI.ParameterPanel.__init__ "Link to this definition")  
Parameters:  **parent** (*wx.Window*) – The parent window

SetupParams(*traceStepData*)[¶](#traceAnalysisAPI.ParameterPanel.SetupParams "Link to this definition")  
Fill your custom GUI with information of the trace step.

Parameters:  **traceStepData** ([`TraceStepDataAPI`](#traceAnalysisAPI.TraceStepDataAPI "traceAnalysisAPI.TraceStepDataAPI")) – Interface to the trace step data like parameters and signals.

OnOk()[¶](#traceAnalysisAPI.ParameterPanel.OnOk "Link to this definition")  
This method is called if the user clicks the OK button of the trace step dialog. Check the user input here.

Returns:  Returns True if user input is OK and the dialog can be closed, else False.

Return type:  bool

StoreParams(*traceStepData*)[¶](#traceAnalysisAPI.ParameterPanel.StoreParams "Link to this definition")  
Collect the information of your custom GUI and update the parameterization accordingly via [`TraceStepDataAPI.SetParameterValue()`](#traceAnalysisAPI.TraceStepDataAPI.SetParameterValue "traceAnalysisAPI.TraceStepDataAPI.SetParameterValue")

Parameters:  **traceStepData** ([`TraceStepDataAPI`](#traceAnalysisAPI.TraceStepDataAPI "traceAnalysisAPI.TraceStepDataAPI")) – Interface to the trace step data like parameters and signals.

## TraceStepDataAPI[¶](#tracestepdataapi "Link to this heading")

*class* traceAnalysisAPI.TraceStepDataAPI[¶](#traceAnalysisAPI.TraceStepDataAPI "Link to this definition")  
The TraceStepDataAPI provides functions to access information about parameters and signals of a trace step and it’s underlying trace step prototype. The API allows changing values of parameters as well. It is used to develop a custom user interface for trace steps.

GetSignalNames()[¶](#traceAnalysisAPI.TraceStepDataAPI.GetSignalNames "Link to this definition")  
Returns a list of signal names used in the trace step.

Return type:  list[str]

GetSignalDescription(*sigName*)[¶](#traceAnalysisAPI.TraceStepDataAPI.GetSignalDescription "Link to this definition")  
Returns the description for a given signal.

Parameters:  **sigName** (*str*) – The name of the desired signal.

Return type:  str

GetSignalDirection(*sigName*)[¶](#traceAnalysisAPI.TraceStepDataAPI.GetSignalDirection "Link to this definition")  
Returns the direction for a given signal.

Parameters:  **sigName** (*str*) – The name of the desired signal.

Returns:  IN or OUT

Return type:  str

GetParameterNames()[¶](#traceAnalysisAPI.TraceStepDataAPI.GetParameterNames "Link to this definition")  
Returns a list of parameter names used in the trace step.

Return type:  list[str]

GetParameterDescription(*paramName*)[¶](#traceAnalysisAPI.TraceStepDataAPI.GetParameterDescription "Link to this definition")  
Returns the description for a given parameter.

Parameters:  **paramName** (*str*) – the name of the desired parameter

Return type:  str

GetParameterType(*paramName*)[¶](#traceAnalysisAPI.TraceStepDataAPI.GetParameterType "Link to this definition")  
Returns the type for a given parameter.

Parameters:  **paramName** (*str*) – The name of the desired parameter.

Returns:  INTEGER, FLOAT, STRING, BOOLEAN, PYOBJECT

Return type:  str

GetParameterValue(*paramName*)[¶](#traceAnalysisAPI.TraceStepDataAPI.GetParameterValue "Link to this definition")  
Returns the current value for a given parameter.

Parameters:  **paramName** (*str*) – The name of the desired parameter.

Return type:  Value or None

SetParameterValue(*paramName*, *value*)[¶](#traceAnalysisAPI.TraceStepDataAPI.SetParameterValue "Link to this definition")  
Sets a new value for a given parameter. Values can only be assigned to parameters with direction IN.

Parameters:  - **paramName** (*str*) – The name of the desired parameter.

- **value** (*str|int|float|bool*) – The new parameter value.

Returns:  True on success, otherwise False

Return type:  bool

Raises:  
- **TypeError** – Invalid type for parameter value.

- **ValueError** – Invalid assignment to OUT parameter.
