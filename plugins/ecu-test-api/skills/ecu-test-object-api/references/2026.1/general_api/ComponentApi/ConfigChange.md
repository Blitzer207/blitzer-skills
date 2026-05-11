[![logo](../../_static/ecu.test.svg)](../../index.html "API  documentation") API documentation

[ Internal APIs ](../api.md)

[ Advanced operations of package variable types ](../variabledatastructures.md)

[ Advanced properties of bus-related objects ](../busdatastructures.md)

[ Bus related objects of trace analysis ](../busdatastructuresTraceanalysis.md)

[ Advanced properties of diagnostics-related objects ](../diagdatastructures.md)

[ Diagnostics related objects of trace analysis ](../diagdatastructuresTraceanalysis.md)

[ Advanced properties of media-related objects ](../mediadatastructures.md)

[ Advanced properties of DLT logging-related objects ](../dltdatastructures.md)

[ COM API ](../com-api.md)

[ REST API ](../rest-api.md)

[ Report API ](../apireport.md)

[ Object API ](../objectApi.md)

Object API

[ API entry points ](../objectApi.md#api-entry-points)

API entry points

[ API for Analysis Jobs ](../AnalysisJobApi.md)

[ API for Artifacts ](../ArtifactApi.md)

[ API for Project Components ](../ComponentApi.md)

API for Project Components

[ AnalysisBindings ](AnalysisBindings.md)

[ AnalysisPackageCall ](AnalysisPackageCall.md)

[ AnalysisPackageMappingCall ](AnalysisPackageMappingCall.md)

[ ArtifactReference ](ArtifactReference.md)

[ AssignedSignal ](AssignedSignal.md)

ConfigChange [ ConfigChange ](#)

ConfigChange

- [C ConfigChange ](#ApiClient.ConfigChange)
  - [A ACTION_TYPE_RESTART ](#ApiClient.ConfigChange.ACTION_TYPE_RESTART)
  - [A ACTION_TYPE_START ](#ApiClient.ConfigChange.ACTION_TYPE_START)
  - [A ACTION_TYPE_STOP ](#ApiClient.ConfigChange.ACTION_TYPE_STOP)
  - [M Clone ](#ApiClient.ConfigChange.Clone)
  - [M GetActionType ](#ApiClient.ConfigChange.GetActionType)
  - [M GetIndex ](#ApiClient.ConfigChange.GetIndex)
  - [M GetKeepTbc ](#ApiClient.ConfigChange.GetKeepTbc)
  - [M GetKeepTcf ](#ApiClient.ConfigChange.GetKeepTcf)
  - [M GetLineNo ](#ApiClient.ConfigChange.GetLineNo)
  - [M GetName ](#ApiClient.ConfigChange.GetName)
  - [M GetParent ](#ApiClient.ConfigChange.GetParent)
  - [M GetTestConfigurationPath ](#ApiClient.ConfigChange.GetTestConfigurationPath)
  - [M GetTestbenchConfigurationPath ](#ApiClient.ConfigChange.GetTestbenchConfigurationPath)
  - [M GetToolAction ](#ApiClient.ConfigChange.GetToolAction)
  - [M GetTools ](#ApiClient.ConfigChange.GetTools)
  - [M GetType ](#ApiClient.ConfigChange.GetType)
  - [M IsEnabled ](#ApiClient.ConfigChange.IsEnabled)
  - [M IsReported ](#ApiClient.ConfigChange.IsReported)
  - [M RemoveFromProject ](#ApiClient.ConfigChange.RemoveFromProject)
  - [M SetActionType ](#ApiClient.ConfigChange.SetActionType)
  - [M SetEnabled ](#ApiClient.ConfigChange.SetEnabled)
  - [M SetKeepTbc ](#ApiClient.ConfigChange.SetKeepTbc)
  - [M SetKeepTcf ](#ApiClient.ConfigChange.SetKeepTcf)
  - [M SetName ](#ApiClient.ConfigChange.SetName)
  - [M SetReported ](#ApiClient.ConfigChange.SetReported)
  - [M SetTestConfigurationPath ](#ApiClient.ConfigChange.SetTestConfigurationPath)
  - [M SetTestbenchConfigurationPath ](#ApiClient.ConfigChange.SetTestbenchConfigurationPath)
  - [M SetToolAction ](#ApiClient.ConfigChange.SetToolAction)
  - [M GetPosition ](#ApiClient.ConfigChange.GetPosition)

[ GlobalConstants ](GlobalConstants.md)

[ MappingFiles ](MappingFiles.md)

[ PackageCall ](PackageCall.md)

[ PackageGenerator ](PackageGenerator.md)

[ PackageParameters ](PackageParameters.md)

[ ParameterGenerator ](ParameterGenerator.md)

[ ParameterSet ](ParameterSet.md)

[ ParameterSetAnalysisPackage ](ParameterSetAnalysisPackage.md)

[ ParameterSetBase ](ParameterSetBase.md)

[ ParameterSetMapping ](ParameterSetMapping.md)

[ ParameterSetRecordings ](ParameterSetRecordings.md)

[ ParameterVariationGeneratorComponent ](ParameterVariationGeneratorComponent.md)

[ ProjectCall ](ProjectCall.md)

[ ProjectComponent ](ProjectComponent.md)

[ ProjectFolder ](ProjectFolder.md)

[ ProjectGenerator ](ProjectGenerator.md)

[ SignalGroupReference ](SignalGroupReference.md)

[ StimulationPackageCall ](StimulationPackageCall.md)

[ API for Configurations ](../ConfigurationApi.md)

[ API for Expectations ](../ExpectationApi.md)

[ API for Expressions ](../ExpressionApi.md)

[ API for Global Mappings ](../GlobalMappingApi.md)

[ API for Mappings ](../MappingApi.md)

[ API for Multimedia Objects ](../MultimediaApi.md)

[ API for Packages ](../PackageApi.md)

[ API for Parameters ](../ParameterApi.md)

[ API for Projects ](../ProjectApi.md)

[ API for Relations ](../RelationApi.md)

[ API for Reports ](../ReportApi.md)

[ API for Report Filters ](../ReportFilterApi.md)

[ API for Settings ](../SettingsApi.md)

[ API for Signals ](../SignalApi.md)

[ API for Signal Descriptions ](../SignalDescriptionApi.md)

[ API for Signal Recordings ](../SignalRecordingApi.md)

[ API for Symbols ](../SymbolApi.md)

[ API for Test Steps ](../TestStepApi.md)

[ API for Touch Inputs ](../TouchInputApi.md)

[ API for Trace Analyses ](../TraceAnalysisApi.md)

[ API for Trace Files ](../TraceFileApi.md)

[ API for Trace Step Templates ](../TraceStepTemplateApi.md)

[ API for Variables ](../VariableApi.md)

[ API for Workspaces ](../WorkspaceApi.md)

[ Trace Analysis API ](../../TraceAnalysisAPI/index.md)

[ Generator APIs ](../../generators/index.md)

[ Tools ](../../tools/index.md)

[ User test management ](../../userTestmanagement/index.md)

[ UserUtility API ](../../user-utility/user-utility.md)

[ Utility Examples ](../../user-utility/example-utilities.md)

ConfigChange

- [C ConfigChange ](#ApiClient.ConfigChange)
  - [A ACTION_TYPE_RESTART ](#ApiClient.ConfigChange.ACTION_TYPE_RESTART)
  - [A ACTION_TYPE_START ](#ApiClient.ConfigChange.ACTION_TYPE_START)
  - [A ACTION_TYPE_STOP ](#ApiClient.ConfigChange.ACTION_TYPE_STOP)
  - [M Clone ](#ApiClient.ConfigChange.Clone)
  - [M GetActionType ](#ApiClient.ConfigChange.GetActionType)
  - [M GetIndex ](#ApiClient.ConfigChange.GetIndex)
  - [M GetKeepTbc ](#ApiClient.ConfigChange.GetKeepTbc)
  - [M GetKeepTcf ](#ApiClient.ConfigChange.GetKeepTcf)
  - [M GetLineNo ](#ApiClient.ConfigChange.GetLineNo)
  - [M GetName ](#ApiClient.ConfigChange.GetName)
  - [M GetParent ](#ApiClient.ConfigChange.GetParent)
  - [M GetTestConfigurationPath ](#ApiClient.ConfigChange.GetTestConfigurationPath)
  - [M GetTestbenchConfigurationPath ](#ApiClient.ConfigChange.GetTestbenchConfigurationPath)
  - [M GetToolAction ](#ApiClient.ConfigChange.GetToolAction)
  - [M GetTools ](#ApiClient.ConfigChange.GetTools)
  - [M GetType ](#ApiClient.ConfigChange.GetType)
  - [M IsEnabled ](#ApiClient.ConfigChange.IsEnabled)
  - [M IsReported ](#ApiClient.ConfigChange.IsReported)
  - [M RemoveFromProject ](#ApiClient.ConfigChange.RemoveFromProject)
  - [M SetActionType ](#ApiClient.ConfigChange.SetActionType)
  - [M SetEnabled ](#ApiClient.ConfigChange.SetEnabled)
  - [M SetKeepTbc ](#ApiClient.ConfigChange.SetKeepTbc)
  - [M SetKeepTcf ](#ApiClient.ConfigChange.SetKeepTcf)
  - [M SetName ](#ApiClient.ConfigChange.SetName)
  - [M SetReported ](#ApiClient.ConfigChange.SetReported)
  - [M SetTestConfigurationPath ](#ApiClient.ConfigChange.SetTestConfigurationPath)
  - [M SetTestbenchConfigurationPath ](#ApiClient.ConfigChange.SetTestbenchConfigurationPath)
  - [M SetToolAction ](#ApiClient.ConfigChange.SetToolAction)
  - [M GetPosition ](#ApiClient.ConfigChange.GetPosition)

# ConfigChange[¶](#configchange "Link to this heading")

*class* ConfigChange[¶](#ApiClient.ConfigChange "Link to this definition")  
Returned by

- [`ComponentApi.CreateConfigChange`](../ComponentApi.md#ApiClient.ComponentApi.CreateConfigChange "ApiClient.ComponentApi.CreateConfigChange (Python method) — Returns the created config change.")

ACTION_TYPE_RESTART[¶](#ApiClient.ConfigChange.ACTION_TYPE_RESTART "Link to this definition")  
Returns the constant used to specify the action type ‘RESTART’.

Returns:  The constant

Return type:  str

ACTION_TYPE_START[¶](#ApiClient.ConfigChange.ACTION_TYPE_START "Link to this definition")  
Returns the constant used to specify the action type ‘START’.

Returns:  The constant

Return type:  str

ACTION_TYPE_STOP[¶](#ApiClient.ConfigChange.ACTION_TYPE_STOP "Link to this definition")  
Returns the constant used to specify the action type ‘STOP’.

Returns:  The constant

Return type:  str

Clone()[¶](#ApiClient.ConfigChange.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`ConfigChange`](#ApiClient.ConfigChange "ApiClient.ConfigChange (Python class) — ComponentApi.CreateConfigChange")

GetActionType()[¶](#ApiClient.ConfigChange.GetActionType "Link to this definition")  
Returns the configuration change action type.

Returns:  The configuration change action type. Possible values are: \* [`ConfigChange.ACTION_TYPE_START`](#ApiClient.ConfigChange.ACTION_TYPE_START "ApiClient.ConfigChange.ACTION_TYPE_START (Python attribute) — Returns the constant used to specify the action type 'START'.") \* [`ConfigChange.ACTION_TYPE_RESTART`](#ApiClient.ConfigChange.ACTION_TYPE_RESTART "ApiClient.ConfigChange.ACTION_TYPE_RESTART (Python attribute) — Returns the constant used to specify the action type 'RESTART'.") \* [`ConfigChange.ACTION_TYPE_STOP`](#ApiClient.ConfigChange.ACTION_TYPE_STOP "ApiClient.ConfigChange.ACTION_TYPE_STOP (Python attribute) — Returns the constant used to specify the action type 'STOP'.")

Return type:  str

GetIndex()[¶](#ApiClient.ConfigChange.GetIndex "Link to this definition")  
Returns the zero based index in the parent.

Returns:  Zero based index

Return type:  int

GetKeepTbc()[¶](#ApiClient.ConfigChange.GetKeepTbc "Link to this definition")  
Returns True if the TBC selection keeps unchanged.

Returns:  True if the TBC selection keeps unchanged, else False.

Return type:  bool

GetKeepTcf()[¶](#ApiClient.ConfigChange.GetKeepTcf "Link to this definition")  
Returns True if the TCF selection keeps unchanged.

Returns:  True if the TCF selection keeps unchanged, else False.

Return type:  bool

GetLineNo()[¶](#ApiClient.ConfigChange.GetLineNo "Link to this definition")  
Returns the line number within its project.

Returns:  Line number

Return type:  int

GetName()[¶](#ApiClient.ConfigChange.GetName "Link to this definition")  
Returns the name of the project component.

Returns:  Name of the component

Return type:  str

GetParent()[¶](#ApiClient.ConfigChange.GetParent "Link to this definition")  
Returns the parent project component.

Returns:  Parent component

Return type:  [`ProjectComponent`](ProjectComponent.md#ApiClient.ProjectComponent "ApiClient.ProjectComponent (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")

GetTestConfigurationPath()[¶](#ApiClient.ConfigChange.GetTestConfigurationPath "Link to this definition")  
Returns the path to the test configuration file, absolute or relative to the ‘Configuration’ directory.

Returns:  Path to the test configuration

Return type:  str

GetTestbenchConfigurationPath()[¶](#ApiClient.ConfigChange.GetTestbenchConfigurationPath "Link to this definition")  
Returns the path to the test bench configuration file, absolute or relative to the ‘Configuration’ directory.

Returns:  Path to the test bench configuration

Return type:  str

GetToolAction(*[toolAlias](#ApiClient.ConfigChange.GetToolAction.toolAlias "ApiClient.ConfigChange.GetToolAction.toolAlias (Python parameter) — Alias of the tool")*)[¶](#ApiClient.ConfigChange.GetToolAction "Link to this definition")  
Returns the action of the specified tool if it is different from ‘AUTO’ else None.

Parameters:  toolAlias : str[¶](#ApiClient.ConfigChange.GetToolAction.toolAlias "Permalink to this definition")  
Alias of the tool

Returns:  Action of the specified tool

Return type:  str

GetTools()[¶](#ApiClient.ConfigChange.GetTools "Link to this definition")  
Returns a list of the configured tools. If the test bench configuration file can not be determined or does not exist, only tools with an action different from ‘AUTO’ will be returned.

Returns:  Configured tools

Return type:  list[str]

GetType()[¶](#ApiClient.ConfigChange.GetType "Link to this definition")  
Returns the type (class name) of the project component, e.g.  
- “ConfigChange”

- “ParameterSet”

- “PackageCall”

- “Project”

- “PackageGenerator”

Returns:  Type (class name) of the project component

Return type:  str

IsEnabled()[¶](#ApiClient.ConfigChange.IsEnabled "Link to this definition")  
Returns the state of the test step.

Returns:  True if test step is enabled, otherwise False

Return type:  bool

IsReported()[¶](#ApiClient.ConfigChange.IsReported "Link to this definition")  
Returns whether the test step will be reported. If it has a parent test step, this function will only return true if both this test step and the parent test step should be reported.

Returns:  True if test step will be reported, otherwise False

Return type:  bool

RemoveFromProject()[¶](#ApiClient.ConfigChange.RemoveFromProject "Link to this definition")  
Removes this component from the project.

Raises:  
**ApiError** – if the component is not part of any project

SetActionType(*[actionType](#ApiClient.ConfigChange.SetActionType.actionType "ApiClient.ConfigChange.SetActionType.actionType (Python parameter) — The configuration change action type.")*)[¶](#ApiClient.ConfigChange.SetActionType "Link to this definition")  
Sets the configuration change action type.

Parameters:  actionType : str[¶](#ApiClient.ConfigChange.SetActionType.actionType "Permalink to this definition")  
The configuration change action type. Valid values are: \* [`ConfigChange.ACTION_TYPE_START`](#ApiClient.ConfigChange.ACTION_TYPE_START "ApiClient.ConfigChange.ACTION_TYPE_START (Python attribute) — Returns the constant used to specify the action type 'START'.") \* [`ConfigChange.ACTION_TYPE_RESTART`](#ApiClient.ConfigChange.ACTION_TYPE_RESTART "ApiClient.ConfigChange.ACTION_TYPE_RESTART (Python attribute) — Returns the constant used to specify the action type 'RESTART'.") \* [`ConfigChange.ACTION_TYPE_STOP`](#ApiClient.ConfigChange.ACTION_TYPE_STOP "ApiClient.ConfigChange.ACTION_TYPE_STOP (Python attribute) — Returns the constant used to specify the action type 'STOP'.")

SetEnabled(*[state](#ApiClient.ConfigChange.SetEnabled.state "ApiClient.ConfigChange.SetEnabled.state (Python parameter) — True (=Default) to enable, False to disable the test step.")=`True`*)[¶](#ApiClient.ConfigChange.SetEnabled "Link to this definition")  
Enable or disable the test step.

Parameters:  state : bool[¶](#ApiClient.ConfigChange.SetEnabled.state "Permalink to this definition")  
True (=Default) to enable, False to disable the test step.

SetKeepTbc(*[keepTbc](#ApiClient.ConfigChange.SetKeepTbc.keepTbc "ApiClient.ConfigChange.SetKeepTbc.keepTbc (Python parameter) — True to keep the TBC unchanged.")*)[¶](#ApiClient.ConfigChange.SetKeepTbc "Link to this definition")  
Defines if the TBC keeps unchanged.

Parameters:  keepTbc : bool[¶](#ApiClient.ConfigChange.SetKeepTbc.keepTbc "Permalink to this definition")  
True to keep the TBC unchanged. False to apply the given TBC path, see [`SetTestbenchConfigurationPath()`](#ApiClient.ConfigChange.SetTestbenchConfigurationPath "ApiClient.ConfigChange.SetTestbenchConfigurationPath (Python method) — Sets the path to the test bench configuration file, absolute or relative to the 'Configurations' directory."). False and no given TBC path will deselect the current TBC.

SetKeepTcf(*[keepTcf](#ApiClient.ConfigChange.SetKeepTcf.keepTcf "ApiClient.ConfigChange.SetKeepTcf.keepTcf (Python parameter) — True to keep the TCF unchanged.")*)[¶](#ApiClient.ConfigChange.SetKeepTcf "Link to this definition")  
Defines if the TCF keeps unchanged.

Parameters:  keepTcf : bool[¶](#ApiClient.ConfigChange.SetKeepTcf.keepTcf "Permalink to this definition")  
True to keep the TCF unchanged. False to apply the given TCF path, see [`SetTestConfigurationPath()`](#ApiClient.ConfigChange.SetTestConfigurationPath "ApiClient.ConfigChange.SetTestConfigurationPath (Python method) — Sets the path to the test configuration file, absolute or relative to the 'Configurations' directory."). False and no given TCF path will deselect the current TCF.

SetName(*[name](#ApiClient.ConfigChange.SetName.name "ApiClient.ConfigChange.SetName.name (Python parameter) — Name of the component")*)[¶](#ApiClient.ConfigChange.SetName "Link to this definition")  
Sets the name of the project component.

Parameters:  name : str[¶](#ApiClient.ConfigChange.SetName.name "Permalink to this definition")  
Name of the component

SetReported(*[state](#ApiClient.ConfigChange.SetReported.state "ApiClient.ConfigChange.SetReported.state (Python parameter) — True (=Default) to enable, False to disable the reporting of the test step.")=`True`*)[¶](#ApiClient.ConfigChange.SetReported "Link to this definition")  
Enable or disable the reporting of the test step. If it has a parent test step, its reporting must also be enabled in order to have this test step appear in the report.

Parameters:  state : bool[¶](#ApiClient.ConfigChange.SetReported.state "Permalink to this definition")  
True (=Default) to enable, False to disable the reporting of the test step.

SetTestConfigurationPath(*[testConfiguration](#ApiClient.ConfigChange.SetTestConfigurationPath.testConfiguration "ApiClient.ConfigChange.SetTestConfigurationPath.testConfiguration (Python parameter) — Path to the test configuration file (absolute or relative to configurations directory)")*, *[namespace](#ApiClient.ConfigChange.SetTestConfigurationPath.namespace "ApiClient.ConfigChange.SetTestConfigurationPath.namespace (Python parameter) — Optional namespace of a configured library workspace.")=`None`*)[¶](#ApiClient.ConfigChange.SetTestConfigurationPath "Link to this definition")  
Sets the path to the test configuration file, absolute or relative to the ‘Configurations’ directory.

Parameters:  testConfiguration : str[¶](#ApiClient.ConfigChange.SetTestConfigurationPath.testConfiguration "Permalink to this definition")  
Path to the test configuration file (absolute or relative to configurations directory)

namespace : str[¶](#ApiClient.ConfigChange.SetTestConfigurationPath.namespace "Permalink to this definition")  
Optional namespace of a configured library workspace. For relative paths, the path is resolved via the configured library workspace with this namespace. If not specified, the namespace is determined automatically via configured library workspaces (for absolute paths) and via the main workspace (for relative paths).

SetTestbenchConfigurationPath(*[testbenchConfiguration](#ApiClient.ConfigChange.SetTestbenchConfigurationPath.testbenchConfiguration "ApiClient.ConfigChange.SetTestbenchConfigurationPath.testbenchConfiguration (Python parameter) — Path to the test bench configuration file (absolute or relative to configurations directory)")*, *[namespace](#ApiClient.ConfigChange.SetTestbenchConfigurationPath.namespace "ApiClient.ConfigChange.SetTestbenchConfigurationPath.namespace (Python parameter) — Optional namespace of a configured library workspace.")=`None`*)[¶](#ApiClient.ConfigChange.SetTestbenchConfigurationPath "Link to this definition")  
Sets the path to the test bench configuration file, absolute or relative to the ‘Configurations’ directory.

Parameters:  testbenchConfiguration : str[¶](#ApiClient.ConfigChange.SetTestbenchConfigurationPath.testbenchConfiguration "Permalink to this definition")  
Path to the test bench configuration file (absolute or relative to configurations directory)

namespace : str[¶](#ApiClient.ConfigChange.SetTestbenchConfigurationPath.namespace "Permalink to this definition")  
Optional namespace of a configured library workspace. For relative paths, the path is resolved via the configured library workspace with this namespace. If not specified, the namespace is determined automatically via configured library workspaces (for absolute paths) and via the main workspace (for relative paths).

SetToolAction(*[toolAlias](#ApiClient.ConfigChange.SetToolAction.toolAlias "ApiClient.ConfigChange.SetToolAction.toolAlias (Python parameter) — Alias of the tool")*, *[action](#ApiClient.ConfigChange.SetToolAction.action "ApiClient.ConfigChange.SetToolAction.action (Python parameter) — The action to set the tool to")*)[¶](#ApiClient.ConfigChange.SetToolAction "Link to this definition")  
Sets the action of the specified tool. Has to be one of the following:

- ‘AUTO’: Automatic (removes tool from component as ‘AUTO’ is the default value)

- ‘RE_START’: Start if stopped, restart if started

- ‘START’: Start if stopped, leave as is if started

- ‘STOP’: Stop if started, leave as is if stopped

- ‘NONE’: Leave as is

Parameters:  toolAlias : str[¶](#ApiClient.ConfigChange.SetToolAction.toolAlias "Permalink to this definition")  
Alias of the tool

action : str[¶](#ApiClient.ConfigChange.SetToolAction.action "Permalink to this definition")  
The action to set the tool to

Raises:  
**ApiError** – When the specified action is not supported.

GetPosition()[¶](#ApiClient.ConfigChange.GetPosition "Link to this definition")  
Returns the position in the parent project.

Returns:  parent position

Return type:  int

Deprecated since version 2024.4: Please use method [`GetLineNo`](#ApiClient.ConfigChange.GetLineNo "ApiClient.ConfigChange.GetLineNo (Python method) — Returns the line number within its project.") instead.

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
