# Available python libraries and APIs[¶](#available-python-libraries-and-apis "Link to this heading")

## NumPy[¶](#numpy "Link to this heading")

The Python package for scientific computing can be used by entering the command:

    import numpy

Currently included version: 1.26.4

For more information about NumPy see the official website of NumPy: [http://www.numpy.org/](http://www.numpy.org/).

## matplotlib[¶](#matplotlib "Link to this heading")

matplotlib is a python library for 2D plotting. It can be used by entering the command:

    import matplotlib

Currently included version: 3.9.2

For more information about matplotlib see the official website: [http://matplotlib.org/](http://matplotlib.org/).

Note

Please note that deprecation warnings of matplotlib are disabled by default. To enable them, please add the following lines to your user code:

    import warnings
    import matplotlib

    warnings.filterwarnings("default", category=matplotlib.MatplotlibDeprecationWarning)

## Methods for signal filtering[¶](#methods-for-signal-filtering "Link to this heading")

### Downsampling[¶](#downsampling "Link to this heading")

*class* tts.traceAnalysis.signalProcessing.DownSampling.DownSampler(*xValuesIn*, *yValuesIn*, *samplingStyle=3*, *minSamples=5000*)[¶](#tts.traceAnalysis.signalProcessing.DownSampling.DownSampler "Link to this definition")  
Class which calculates for a given pane of a plot an optimized selection of signal data points.

`\_\_init\_\_`(*xValuesIn*, *yValuesIn*, *samplingStyle=3*, *minSamples=5000*)[¶](#tts.traceAnalysis.signalProcessing.DownSampling.DownSampler.__init__ "Link to this definition")  
Parameters:  - **xValuesIn** (*numpy.array*) – Values of the time axis of the original signal

- **yValuesIn** (*numpy.array*) – Values of the original signal

- **samplingStyle** (*int*) – Sets the option in which shape the downsampled signal will be returned. This parameter influences whether a single array or a tuple with two arrays for the description of the signal will be returned. The default value is SAMPLE_BOUNDING_VALUES.

Possible values for samplingStyle are:

- SAMPLE_BOUNDING_VALUES: Presentation of the signal by means of an upper and a lower signal  
  where the region between the signals has to be filled.

- SAMPLE_UPPER_VALUES: Presentation of the signal by means of the upper signal.

- SAMPLE_LOWER_VALUES: Presentation of the signal by means of the lower signal.

Parameters:  **minSamples** (*int*) – Minimum number of samples (i.e. signal values) of the original signal to perform downsampling. (If the original signal contains less signal values than this number, no downsampling is performed.)

SampleDown(*xRange*, *pxWidth*, *panFactor=0.0*)[¶](#tts.traceAnalysis.signalProcessing.DownSampling.DownSampler.SampleDown "Link to this definition")  
Parameters:  - **xRange** (*tuple* *(xmin,* *xmax)*) – Range of the time axis for the given signal.

- **pxWidth** (*int*) – Width of region to be displayed in pixels.

- **panFactor** (*float*) – Factor \>= 0, which indicates whether and how much points out of the displayed region should be calculated. The default value is 0.0.

Returns:  Tuple (xValues, yValues) with optimized data points. If samplingStyle SAMPLE_BOUNDING_VALUES is used, the return type changes to (xValues, (yValuesMin, yValuesMax)).

Note:  

- panFactor = 0 means that only pixels in the displayed region will be calculated.

- panFactor = 1 means that left and right of the displayed region an additional range (given by xrange) will be calculated for each direction.

Calculates for the given pane of a plot an optimized selection of signal data points.

SetInput(*xValuesIn*, *yValuesIn*)[¶](#tts.traceAnalysis.signalProcessing.DownSampling.DownSampler.SetInput "Link to this definition")  
Parameters:  - **xValuesIn** (*numpy.array*) – Values of the time axis of the original signal.

- **yValuesIn** (*numpy.array*) – Values of the originals signal.

Set new input values for the downsampling.

SetSamplingStyle(*samplingStyle*)[¶](#tts.traceAnalysis.signalProcessing.DownSampling.DownSampler.SetSamplingStyle "Link to this definition")  
Parameters:  **samplingStyle** (*int*) – Sets the option in which shape the downsampled signal will be returned. This parameter influences whether a single array or a tuple with two arrays for the description of the signal will be returned.

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
