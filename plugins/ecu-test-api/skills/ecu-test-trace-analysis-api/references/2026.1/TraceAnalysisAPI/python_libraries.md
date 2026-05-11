[ Array-based NumPy trace step templates ](array_based_templates.md)

[ Event based tracestep templates ](event_based_templates.md)

[ Stream based tracestep templates ](stream_based_templates.md)

[ Custom GUI for parameters ](custom_param_gui.md)

[ Custom trace synchronization ](custom_trace_synchronization.md)

Available python libraries and APIs [ Available python libraries and APIs ](#)

Available python libraries and APIs

- [ NumPy ](#numpy)
- [ matplotlib ](#matplotlib)
- [ Methods for signal filtering ](#methods-for-signal-filtering)
  - [ Downsampling ](#downsampling)
    - [C tts.traceAnalysis.signalProcessing.DownSampling.DownSampler ](#tts.traceAnalysis.signalProcessing.DownSampling.DownSampler)
      - [M `\_\_init\_\_` ](#tts.traceAnalysis.signalProcessing.DownSampling.DownSampler.__init__)
      - [M SampleDown ](#tts.traceAnalysis.signalProcessing.DownSampling.DownSampler.SampleDown)
      - [M SetInput ](#tts.traceAnalysis.signalProcessing.DownSampling.DownSampler.SetInput)
      - [M SetSamplingStyle ](#tts.traceAnalysis.signalProcessing.DownSampling.DownSampler.SetSamplingStyle)
- [ Decorators ](#decorators)
  - [F @tts.traceAnalysis.Decorators.numpyfunc ](#tts.traceAnalysis.Decorators.numpyfunc)

Available python libraries and APIs

- [ NumPy ](#numpy)
- [ matplotlib ](#matplotlib)
- [ Methods for signal filtering ](#methods-for-signal-filtering)
  - [ Downsampling ](#downsampling)
    - [C tts.traceAnalysis.signalProcessing.DownSampling.DownSampler ](#tts.traceAnalysis.signalProcessing.DownSampling.DownSampler)
      - [M `\_\_init\_\_` ](#tts.traceAnalysis.signalProcessing.DownSampling.DownSampler.__init__)
      - [M SampleDown ](#tts.traceAnalysis.signalProcessing.DownSampling.DownSampler.SampleDown)
      - [M SetInput ](#tts.traceAnalysis.signalProcessing.DownSampling.DownSampler.SetInput)
      - [M SetSamplingStyle ](#tts.traceAnalysis.signalProcessing.DownSampling.DownSampler.SetSamplingStyle)
- [ Decorators ](#decorators)
  - [F @tts.traceAnalysis.Decorators.numpyfunc ](#tts.traceAnalysis.Decorators.numpyfunc)

# Available python libraries and APIs[¶](#available-python-libraries-and-apis "Link to this heading")

## NumPy[¶](#numpy "Link to this heading")

The Python package for scientific computing can be used by entering the command:

    import numpy

Currently included version: 2.2.6

For more information about NumPy see the official website of NumPy: [http://www.numpy.org/](http://www.numpy.org/).

## matplotlib[¶](#matplotlib "Link to this heading")

matplotlib is a python library for 2D plotting. It can be used by entering the command:

    import matplotlib

Currently included version: 3.10.8

For more information about matplotlib see the official website: [http://matplotlib.org/](http://matplotlib.org/).

Info

Please note that deprecation warnings of matplotlib are disabled by default. To enable them, please add the following lines to your user code:

    import warnings
    import matplotlib

    warnings.filterwarnings("default", category=matplotlib.MatplotlibDeprecationWarning)

## Methods for signal filtering[¶](#methods-for-signal-filtering "Link to this heading")

### Downsampling[¶](#downsampling "Link to this heading")

*class* tts.traceAnalysis.signalProcessing.DownSampling.DownSampler(*[xValuesIn](#tts.traceAnalysis.signalProcessing.DownSampling.DownSampler "tts.traceAnalysis.signalProcessing.DownSampling.DownSampler.__init__.xValuesIn (Python parameter) — Values of the time axis of the original signal")*, *[yValuesIn](#tts.traceAnalysis.signalProcessing.DownSampling.DownSampler "tts.traceAnalysis.signalProcessing.DownSampling.DownSampler.__init__.yValuesIn (Python parameter) — Values of the original signal")*, *[samplingStyle](#tts.traceAnalysis.signalProcessing.DownSampling.DownSampler "tts.traceAnalysis.signalProcessing.DownSampling.DownSampler.__init__.samplingStyle (Python parameter) — Sets the option in which shape the downsampled signal will be returned. This parameter influences whether a single array or a tuple with two arrays for the description of the signal will be returned.")=`3`*, *[minSamples](#tts.traceAnalysis.signalProcessing.DownSampling.DownSampler "tts.traceAnalysis.signalProcessing.DownSampling.DownSampler.__init__.minSamples (Python parameter) — Minimum number of samples (i.e.")=`5000`*)[¶](#tts.traceAnalysis.signalProcessing.DownSampling.DownSampler "Link to this definition")  
Class which calculates for a given pane of a plot an optimized selection of signal data points.

`\_\_init\_\_`(*[xValuesIn](#tts.traceAnalysis.signalProcessing.DownSampling.DownSampler "tts.traceAnalysis.signalProcessing.DownSampling.DownSampler.__init__.xValuesIn (Python parameter) — Values of the time axis of the original signal")*, *[yValuesIn](#tts.traceAnalysis.signalProcessing.DownSampling.DownSampler "tts.traceAnalysis.signalProcessing.DownSampling.DownSampler.__init__.yValuesIn (Python parameter) — Values of the original signal")*, *[samplingStyle](#tts.traceAnalysis.signalProcessing.DownSampling.DownSampler "tts.traceAnalysis.signalProcessing.DownSampling.DownSampler.__init__.samplingStyle (Python parameter) — Sets the option in which shape the downsampled signal will be returned. This parameter influences whether a single array or a tuple with two arrays for the description of the signal will be returned.")=`3`*, *[minSamples](#tts.traceAnalysis.signalProcessing.DownSampling.DownSampler "tts.traceAnalysis.signalProcessing.DownSampling.DownSampler.__init__.minSamples (Python parameter) — Minimum number of samples (i.e.")=`5000`*)[¶](#tts.traceAnalysis.signalProcessing.DownSampling.DownSampler.__init__ "Link to this definition")  
Parameters:  xValuesIn : numpy.array[¶](#tts.traceAnalysis.signalProcessing.DownSampling.DownSampler.__init__.xValuesIn "Permalink to this definition")  
Values of the time axis of the original signal

yValuesIn : numpy.array[¶](#tts.traceAnalysis.signalProcessing.DownSampling.DownSampler.__init__.yValuesIn "Permalink to this definition")  
Values of the original signal

samplingStyle : int[¶](#tts.traceAnalysis.signalProcessing.DownSampling.DownSampler.__init__.samplingStyle "Permalink to this definition")  
Sets the option in which shape the downsampled signal will be returned. This parameter influences whether a single array or a tuple with two arrays for the description of the signal will be returned. The default value is SAMPLE_BOUNDING_VALUES.

Possible values for samplingStyle are:

- SAMPLE_BOUNDING_VALUES: Presentation of the signal by means of an upper and a lower signal  
  where the region between the signals has to be filled.

- SAMPLE_UPPER_VALUES: Presentation of the signal by means of the upper signal.

- SAMPLE_LOWER_VALUES: Presentation of the signal by means of the lower signal.

Parameters:  minSamples : int[¶](#tts.traceAnalysis.signalProcessing.DownSampling.DownSampler.__init__.minSamples "Permalink to this definition")  
Minimum number of samples (i.e. signal values) of the original signal to perform downsampling. (If the original signal contains less signal values than this number, no downsampling is performed.)

SampleDown(*[xRange](#tts.traceAnalysis.signalProcessing.DownSampling.DownSampler.SampleDown.xRange "tts.traceAnalysis.signalProcessing.DownSampling.DownSampler.SampleDown.xRange (Python parameter) — Range of the time axis for the given signal.")*, *[pxWidth](#tts.traceAnalysis.signalProcessing.DownSampling.DownSampler.SampleDown.pxWidth "tts.traceAnalysis.signalProcessing.DownSampling.DownSampler.SampleDown.pxWidth (Python parameter) — Width of region to be displayed in pixels.")*, *[panFactor](#tts.traceAnalysis.signalProcessing.DownSampling.DownSampler.SampleDown.panFactor "tts.traceAnalysis.signalProcessing.DownSampling.DownSampler.SampleDown.panFactor (Python parameter) — Factor >= 0, which indicates whether and how much points out of the displayed region should be calculated. The default value is 0.0.")=`0.0`*)[¶](#tts.traceAnalysis.signalProcessing.DownSampling.DownSampler.SampleDown "Link to this definition")  
Parameters:  xRange : tuple (xmin, xmax)[¶](#tts.traceAnalysis.signalProcessing.DownSampling.DownSampler.SampleDown.xRange "Permalink to this definition")  
Range of the time axis for the given signal.

pxWidth : int[¶](#tts.traceAnalysis.signalProcessing.DownSampling.DownSampler.SampleDown.pxWidth "Permalink to this definition")  
Width of region to be displayed in pixels.

panFactor : float[¶](#tts.traceAnalysis.signalProcessing.DownSampling.DownSampler.SampleDown.panFactor "Permalink to this definition")  
Factor \>= 0, which indicates whether and how much points out of the displayed region should be calculated. The default value is 0.0.

Returns:  Tuple (xValues, yValues) with optimized data points. If samplingStyle SAMPLE_BOUNDING_VALUES is used, the return type changes to (xValues, (yValuesMin, yValuesMax)).

Note:  

- panFactor = 0 means that only pixels in the displayed region will be calculated.

- panFactor = 1 means that left and right of the displayed region an additional range (given by xrange) will be calculated for each direction.

Calculates for the given pane of a plot an optimized selection of signal data points.

SetInput(*[xValuesIn](#tts.traceAnalysis.signalProcessing.DownSampling.DownSampler.SetInput.xValuesIn "tts.traceAnalysis.signalProcessing.DownSampling.DownSampler.SetInput.xValuesIn (Python parameter) — Values of the time axis of the original signal.")*, *[yValuesIn](#tts.traceAnalysis.signalProcessing.DownSampling.DownSampler.SetInput.yValuesIn "tts.traceAnalysis.signalProcessing.DownSampling.DownSampler.SetInput.yValuesIn (Python parameter) — Values of the originals signal.")*)[¶](#tts.traceAnalysis.signalProcessing.DownSampling.DownSampler.SetInput "Link to this definition")  
Parameters:  xValuesIn : numpy.array[¶](#tts.traceAnalysis.signalProcessing.DownSampling.DownSampler.SetInput.xValuesIn "Permalink to this definition")  
Values of the time axis of the original signal.

yValuesIn : numpy.array[¶](#tts.traceAnalysis.signalProcessing.DownSampling.DownSampler.SetInput.yValuesIn "Permalink to this definition")  
Values of the originals signal.

Set new input values for the downsampling.

SetSamplingStyle(*[samplingStyle](#tts.traceAnalysis.signalProcessing.DownSampling.DownSampler.SetSamplingStyle.samplingStyle "tts.traceAnalysis.signalProcessing.DownSampling.DownSampler.SetSamplingStyle.samplingStyle (Python parameter) — Sets the option in which shape the downsampled signal will be returned. This parameter influences whether a single array or a tuple with two arrays for the description of the signal will be returned.")*)[¶](#tts.traceAnalysis.signalProcessing.DownSampling.DownSampler.SetSamplingStyle "Link to this definition")  
Parameters:  samplingStyle : int[¶](#tts.traceAnalysis.signalProcessing.DownSampling.DownSampler.SetSamplingStyle.samplingStyle "Permalink to this definition")  
Sets the option in which shape the downsampled signal will be returned. This parameter influences whether a single array or a tuple with two arrays for the description of the signal will be returned.

See:  
DownSampler.`\_\_init\_\_`

## Decorators[¶](#decorators "Link to this heading")

@tts.traceAnalysis.Decorators.numpyfunc[¶](#tts.traceAnalysis.Decorators.numpyfunc "Link to this definition")  
Decorator to annotate a function that expects parameters values as whole NumPy array. Use this decorator for functions that are called from calculations and trigger blocks of the trace analysis.

This function will be called once with all signal samples instead once for each sample. Even scalar parameters will be of type numpy.ndarray of shape *(1,)*. Please verify the valid parameterization by yourself.

Keep in mind, that internal functions of the trace analysis (e.g. Edge) may return a NumPy array with one value for each sample (e.g. Edge) or only a NumPy array of shape *(1,)* (e.g. StartTriggerValue, Average). The return value will be directly passed into the decorated function.

The function must return a scalar value or a NumPy array of the same shape as its signal parameter.

Note:  
The decorator is available by default in package variables of type Function. To use it in UserPyModules, it has to be imported explicitly as shown in the example below.

Example:  
    # myUserPyModule.py
    from tts.traceAnalysis.Decorators import numpyfunc

    @numpyfunc
    def MyFunc(values, param1, param2):
        print(values, param1, param2)
        return values*param1+param2

Calling this function from a calculation via

    user.myUserPyModule.MyFunc(Signal1, Signal2, 2)

will result to the parameter shapes *(10,)*, *(10,)*, and *(1,)*, for example. The result will be of shape *(10,)*.

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
