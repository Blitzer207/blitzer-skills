[ Array-based NumPy trace step templates ](array_based_templates.md)

[ Event based tracestep templates ](event_based_templates.md)

[ Stream based tracestep templates ](stream_based_templates.md)

[ Custom GUI for parameters ](custom_param_gui.md)

Custom trace synchronization [ Custom trace synchronization ](#)

Custom trace synchronization

- [ AbstractTraceSynchronization ](#abstracttracesynchronization)
  - [C traceAnalysisAPI.customsynchro.AbstractTraceSynchronization ](#traceAnalysisAPI.customsynchro.AbstractTraceSynchronization)
    - [M GetParameters ](#traceAnalysisAPI.customsynchro.AbstractTraceSynchronization.GetParameters)
    - [M GetMasterSignals ](#traceAnalysisAPI.customsynchro.AbstractTraceSynchronization.GetMasterSignals)
    - [M GetRecordingSignals ](#traceAnalysisAPI.customsynchro.AbstractTraceSynchronization.GetRecordingSignals)
    - [M Synchronize ](#traceAnalysisAPI.customsynchro.AbstractTraceSynchronization.Synchronize)
- [ ParameterDefinition ](#parameterdefinition)
  - [C traceAnalysisAPI.customsynchro.ParameterDefinition ](#traceAnalysisAPI.customsynchro.ParameterDefinition)
- [ SignalDefinition ](#signaldefinition)
  - [C traceAnalysisAPI.customsynchro.SignalDefinition ](#traceAnalysisAPI.customsynchro.SignalDefinition)
- [ Signal ](#signal)
  - [C traceAnalysisAPI.customsynchro.Signal ](#traceAnalysisAPI.customsynchro.Signal)
    - [M GetMappingItemName ](#traceAnalysisAPI.customsynchro.Signal.GetMappingItemName)
    - [M GetTimestamps ](#traceAnalysisAPI.customsynchro.Signal.GetTimestamps)
    - [M GetValues ](#traceAnalysisAPI.customsynchro.Signal.GetValues)
- [ Example ](#example)

[ Available python libraries and APIs ](python_libraries.md)

Custom trace synchronization

- [ AbstractTraceSynchronization ](#abstracttracesynchronization)
  - [C traceAnalysisAPI.customsynchro.AbstractTraceSynchronization ](#traceAnalysisAPI.customsynchro.AbstractTraceSynchronization)
    - [M GetParameters ](#traceAnalysisAPI.customsynchro.AbstractTraceSynchronization.GetParameters)
    - [M GetMasterSignals ](#traceAnalysisAPI.customsynchro.AbstractTraceSynchronization.GetMasterSignals)
    - [M GetRecordingSignals ](#traceAnalysisAPI.customsynchro.AbstractTraceSynchronization.GetRecordingSignals)
    - [M Synchronize ](#traceAnalysisAPI.customsynchro.AbstractTraceSynchronization.Synchronize)
- [ ParameterDefinition ](#parameterdefinition)
  - [C traceAnalysisAPI.customsynchro.ParameterDefinition ](#traceAnalysisAPI.customsynchro.ParameterDefinition)
- [ SignalDefinition ](#signaldefinition)
  - [C traceAnalysisAPI.customsynchro.SignalDefinition ](#traceAnalysisAPI.customsynchro.SignalDefinition)
- [ Signal ](#signal)
  - [C traceAnalysisAPI.customsynchro.Signal ](#traceAnalysisAPI.customsynchro.Signal)
    - [M GetMappingItemName ](#traceAnalysisAPI.customsynchro.Signal.GetMappingItemName)
    - [M GetTimestamps ](#traceAnalysisAPI.customsynchro.Signal.GetTimestamps)
    - [M GetValues ](#traceAnalysisAPI.customsynchro.Signal.GetValues)
- [ Example ](#example)

# Custom trace synchronization[¶](#custom-trace-synchronization "Link to this heading")

To integrate a custom trace synchronization, you can implement a Python script that follows the interface defined in the AbstractTraceSynchronization class. This Python script needs to fulfill several requirements to be available as a valid trace synchronization.

- The script needs to be located in the `UserPyModules` folder of the workspace.

- On the top level of the script, you must specify the variable MODULE_TYPE = ‘TRACE_SYNCHRONIZATION’.

- The file needs to contain a class that defines two static class variables:

  - ID: that uniquely identifies the synchronization. Could be a generated uuid or a simple versioning schema like *\<class name\>\_v1*

  - DISPLAY_NAME: that is used to display the synchronization in the user interface.

- The class needs to implement the methods GetParameters, GetMasterSignals, GetRecordingSignals and Synchronize.

- There must not be two synchronizations with the same ID.

Newly added sychnronizations are available after refreshing the user libraries. You can do this in the menu “Extras”.

The package ecu.test-interface (available on pypi.org) can be installed in the develop environment to the auto-completion in your IDE

## AbstractTraceSynchronization[¶](#abstracttracesynchronization "Link to this heading")

*class* traceAnalysisAPI.customsynchro.AbstractTraceSynchronization[¶](#traceAnalysisAPI.customsynchro.AbstractTraceSynchronization "Link to this definition")  
Interface class for custom trace synchronization methods.

This abstract base class defines the contract for implementing synchronization algorithms that align recording signals with master signals in trace data. Subclasses must implement the Synchronize method and can override the class methods to specify required parameters and signals.

Variables:  
ID : str  
Unique ID of the synchronization method.

DISPLAY_NAME : str  
Human-readable name of the synchronization method.

*classmethod* GetParameters() → list[[ParameterDefinition](#traceAnalysisAPI.customsynchro.ParameterDefinition "traceAnalysisAPI.customsynchro.ParameterDefinition (Python class) — Represents a parameter definition for user synchronization.")][¶](#traceAnalysisAPI.customsynchro.AbstractTraceSynchronization.GetParameters "Link to this definition")  
Override this method to specify which parameters are needed for your synchronization implementation. By default, no parameters are required.

Returns:  List of ParameterDefinition objects describing required parameters.

*abstractmethod classmethod* GetMasterSignals() → list[[SignalDefinition](#traceAnalysisAPI.customsynchro.SignalDefinition "traceAnalysisAPI.customsynchro.SignalDefinition (Python class) — Represents a signal definition used for describing a signal in the system.")][¶](#traceAnalysisAPI.customsynchro.AbstractTraceSynchronization.GetMasterSignals "Link to this definition")  
Override this method to specify which master signals are required for synchronization.

Returns:  List of SignalDefinition objects for master signals.

Raises:  
**NotImplementedError** – If not implemented in subclass.

*abstractmethod classmethod* GetRecordingSignals() → list[[SignalDefinition](#traceAnalysisAPI.customsynchro.SignalDefinition "traceAnalysisAPI.customsynchro.SignalDefinition (Python class) — Represents a signal definition used for describing a signal in the system.")][¶](#traceAnalysisAPI.customsynchro.AbstractTraceSynchronization.GetRecordingSignals "Link to this definition")  
Override this method to specify which recording signals are required for synchronization.

Returns:  List of SignalDefinition objects for recording signals.

Raises:  
**NotImplementedError** – If not implemented in subclass.

*abstractmethod* Synchronize(*[masterSignals](#traceAnalysisAPI.customsynchro.AbstractTraceSynchronization.Synchronize.masterSignals "traceAnalysisAPI.customsynchro.AbstractTraceSynchronization.Synchronize.masterSignals (Python parameter) — Dictionary of master signal names to Signal objects."): dict[str, [Signal](#traceAnalysisAPI.customsynchro.Signal "traceAnalysisAPI.customsynchro.Signal (Python class) — Represents a time-based signal for mapping items. Provides access to timestamps and corresponding values.")]*, *[recordingSignals](#traceAnalysisAPI.customsynchro.AbstractTraceSynchronization.Synchronize.recordingSignals "traceAnalysisAPI.customsynchro.AbstractTraceSynchronization.Synchronize.recordingSignals (Python parameter) — Dictionary of recording signal names to Signal objects."): dict[str, [Signal](#traceAnalysisAPI.customsynchro.Signal "traceAnalysisAPI.customsynchro.Signal (Python class) — Represents a time-based signal for mapping items. Provides access to timestamps and corresponding values.")]*, *[parameters](#traceAnalysisAPI.customsynchro.AbstractTraceSynchronization.Synchronize.parameters "traceAnalysisAPI.customsynchro.AbstractTraceSynchronization.Synchronize.parameters (Python parameter) — Dictionary of parameter names to their values."): dict[str, object]*) → float[¶](#traceAnalysisAPI.customsynchro.AbstractTraceSynchronization.Synchronize "Link to this definition")  
Calculates the time offset in trace time (usually seconds) to synchronize the traces with the master signals.

Parameters:  masterSignals: dict[str, [Signal](#traceAnalysisAPI.customsynchro.Signal "traceAnalysisAPI.customsynchro.Signal (Python class) — Represents a time-based signal for mapping items. Provides access to timestamps and corresponding values.")][¶](#traceAnalysisAPI.customsynchro.AbstractTraceSynchronization.Synchronize.masterSignals "Permalink to this definition")  
Dictionary of master signal names to Signal objects.

recordingSignals: dict[str, [Signal](#traceAnalysisAPI.customsynchro.Signal "traceAnalysisAPI.customsynchro.Signal (Python class) — Represents a time-based signal for mapping items. Provides access to timestamps and corresponding values.")][¶](#traceAnalysisAPI.customsynchro.AbstractTraceSynchronization.Synchronize.recordingSignals "Permalink to this definition")  
Dictionary of recording signal names to Signal objects.

parameters: dict[str, object][¶](#traceAnalysisAPI.customsynchro.AbstractTraceSynchronization.Synchronize.parameters "Permalink to this definition")  
Dictionary of parameter names to their values.

Returns:  Calculated time offset for synchronization (in seconds).

Raises:  
**NotImplementedError** – If not implemented in subclass.

## ParameterDefinition[¶](#parameterdefinition "Link to this heading")

*class* traceAnalysisAPI.customsynchro.ParameterDefinition[¶](#traceAnalysisAPI.customsynchro.ParameterDefinition "Link to this definition")  
Represents a parameter definition for user synchronization.

Variables:  
name : str  
Name of the parameter.

description : str  
Description of the parameter.

default : Any  
Default value of the parameter.

## SignalDefinition[¶](#signaldefinition "Link to this heading")

*class* traceAnalysisAPI.customsynchro.SignalDefinition[¶](#traceAnalysisAPI.customsynchro.SignalDefinition "Link to this definition")  
Represents a signal definition used for describing a signal in the system.

Variables:  
name : str  
Name of the signal

description : str  
Description of the signal

optional : bool  
Whether the signal is optional

## Signal[¶](#signal "Link to this heading")

*class* traceAnalysisAPI.customsynchro.Signal[¶](#traceAnalysisAPI.customsynchro.Signal "Link to this definition")  
Represents a time-based signal for mapping items. Provides access to timestamps and corresponding values.

*abstractmethod* GetMappingItemName() → str[¶](#traceAnalysisAPI.customsynchro.Signal.GetMappingItemName "Link to this definition")  
Returns:  The mapping item name as a string.

*abstractmethod* GetTimestamps() → numpy.ndarray[¶](#traceAnalysisAPI.customsynchro.Signal.GetTimestamps "Link to this definition")  
Returns:  A numpy.ndarray of timestamps (float64).

*abstractmethod* GetValues() → numpy.ndarray[¶](#traceAnalysisAPI.customsynchro.Signal.GetValues "Link to this definition")  
Returns:  A numpy.ndarray of tuples (timestamp, value).

## Example[¶](#example "Link to this heading")

    from __future__ import annotations

    from dataclasses import dataclass

    MODULE_TYPE = 'TRACE_SYNCHRONIZATION'
    #from tts.interface.userSynchronization.AbstractTraceSynchronization import AbstractTraceSynchronization
    # The AbstractTraceSynchronization defines the interface for all UserSynchronizations.
    from tts.interface.userSynchronization.Signal import Signal
    from tts.interface.userSynchronization.SignalDefinition import SignalDefinition
    from tts.interface.userSynchronization.SignalParameter import SignalParameter

    class ExpectedValueSync:

        DISPLAY_NAME = 'ExpectedValue'
        ID = 'ExpectedValueSync_v1'

        @classmethod
        def GetParameters(cls) -> list[ParameterDefinition]:
            return [
                ParameterDefinition(
                    'expectedValue',
                    description='the description is shown as help text',
                    default='2.5',
                ),
            ]

        @classmethod
        def GetMasterSignals(cls) -> list[SignalDefinition]:
            return [
                SignalDefinition(
                    'SignalA', description='signal that value should match', optional=False
                )
            ]

        @classmethod
        def GetRecordingSignals(cls) -> list[SignalDefinition]:
            return [
                SignalDefinition(
                    'SignalB', description='signal that value should match', optional=False
                )
            ]

        def Synchronize(
            self,
            masterSignals: dict[str, Signal],
            recordingSignals: dict[str, Signal],
            parameters: dict[str, object],
        ) -> float:
            tsMaster = self._FindValue(
                parameters['expectedValue'],
                masterSignals['SignalA'],
            )
            tsRec = self._FindValue(
                parameters['expectedValue'],
                recordingSignals['SignalB'],
            )
            if tsMaster is None or tsRec is None:
                raise ValueError('Could not find value for one of the signals')
            return tsMaster - tsRec

        def _FindValue(self, expValue: float, signal: Signal):
            for ts, value in zip(signal.GetTimestamps(), signal.GetValues()):
                if value == expValue:
                    return ts

            return None

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
