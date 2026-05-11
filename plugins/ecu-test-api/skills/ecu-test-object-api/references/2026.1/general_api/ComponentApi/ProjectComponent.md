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

[ ConfigChange ](ConfigChange.md)

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

ProjectComponent [ ProjectComponent ](#)

ProjectComponent

- [C ProjectComponent ](#ApiClient.ProjectComponent)
  - [M Clone ](#ApiClient.ProjectComponent.Clone)
  - [M GetIndex ](#ApiClient.ProjectComponent.GetIndex)
  - [M GetLineNo ](#ApiClient.ProjectComponent.GetLineNo)
  - [M GetName ](#ApiClient.ProjectComponent.GetName)
  - [M GetParent ](#ApiClient.ProjectComponent.GetParent)
  - [M GetType ](#ApiClient.ProjectComponent.GetType)
  - [M IsEnabled ](#ApiClient.ProjectComponent.IsEnabled)
  - [M IsReported ](#ApiClient.ProjectComponent.IsReported)
  - [M RemoveFromProject ](#ApiClient.ProjectComponent.RemoveFromProject)
  - [M SetEnabled ](#ApiClient.ProjectComponent.SetEnabled)
  - [M SetName ](#ApiClient.ProjectComponent.SetName)
  - [M SetReported ](#ApiClient.ProjectComponent.SetReported)
  - [M GetPosition ](#ApiClient.ProjectComponent.GetPosition)

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

ProjectComponent

- [C ProjectComponent ](#ApiClient.ProjectComponent)
  - [M Clone ](#ApiClient.ProjectComponent.Clone)
  - [M GetIndex ](#ApiClient.ProjectComponent.GetIndex)
  - [M GetLineNo ](#ApiClient.ProjectComponent.GetLineNo)
  - [M GetName ](#ApiClient.ProjectComponent.GetName)
  - [M GetParent ](#ApiClient.ProjectComponent.GetParent)
  - [M GetType ](#ApiClient.ProjectComponent.GetType)
  - [M IsEnabled ](#ApiClient.ProjectComponent.IsEnabled)
  - [M IsReported ](#ApiClient.ProjectComponent.IsReported)
  - [M RemoveFromProject ](#ApiClient.ProjectComponent.RemoveFromProject)
  - [M SetEnabled ](#ApiClient.ProjectComponent.SetEnabled)
  - [M SetName ](#ApiClient.ProjectComponent.SetName)
  - [M SetReported ](#ApiClient.ProjectComponent.SetReported)
  - [M GetPosition ](#ApiClient.ProjectComponent.GetPosition)

# ProjectComponent[¶](#projectcomponent "Link to this heading")

*class* ProjectComponent[¶](#ApiClient.ProjectComponent "Link to this definition")  
Clone()[¶](#ApiClient.ProjectComponent.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`ProjectComponent`](#ApiClient.ProjectComponent "ApiClient.ProjectComponent (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")

GetIndex()[¶](#ApiClient.ProjectComponent.GetIndex "Link to this definition")  
Returns the zero based index in the parent.

Returns:  Zero based index

Return type:  int

GetLineNo()[¶](#ApiClient.ProjectComponent.GetLineNo "Link to this definition")  
Returns the line number within its project.

Returns:  Line number

Return type:  int

GetName()[¶](#ApiClient.ProjectComponent.GetName "Link to this definition")  
Returns the name of the project component.

Returns:  Name of the component

Return type:  str

GetParent()[¶](#ApiClient.ProjectComponent.GetParent "Link to this definition")  
Returns the parent project component.

Returns:  Parent component

Return type:  [`ProjectComponent`](#ApiClient.ProjectComponent "ApiClient.ProjectComponent (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")

GetType()[¶](#ApiClient.ProjectComponent.GetType "Link to this definition")  
Returns the type (class name) of the project component, e.g.  
- “ConfigChange”

- “ParameterSet”

- “PackageCall”

- “Project”

- “PackageGenerator”

Returns:  Type (class name) of the project component

Return type:  str

IsEnabled()[¶](#ApiClient.ProjectComponent.IsEnabled "Link to this definition")  
Returns the state of the test step.

Returns:  True if test step is enabled, otherwise False

Return type:  bool

IsReported()[¶](#ApiClient.ProjectComponent.IsReported "Link to this definition")  
Returns whether the test step will be reported. If it has a parent test step, this function will only return true if both this test step and the parent test step should be reported.

Returns:  True if test step will be reported, otherwise False

Return type:  bool

RemoveFromProject()[¶](#ApiClient.ProjectComponent.RemoveFromProject "Link to this definition")  
Removes this component from the project.

Raises:  
**ApiError** – if the component is not part of any project

SetEnabled(*[state](#ApiClient.ProjectComponent.SetEnabled.state "ApiClient.ProjectComponent.SetEnabled.state (Python parameter) — True (=Default) to enable, False to disable the test step.")=`True`*)[¶](#ApiClient.ProjectComponent.SetEnabled "Link to this definition")  
Enable or disable the test step.

Parameters:  state : bool[¶](#ApiClient.ProjectComponent.SetEnabled.state "Permalink to this definition")  
True (=Default) to enable, False to disable the test step.

SetName(*[name](#ApiClient.ProjectComponent.SetName.name "ApiClient.ProjectComponent.SetName.name (Python parameter) — Name of the component")*)[¶](#ApiClient.ProjectComponent.SetName "Link to this definition")  
Sets the name of the project component.

Parameters:  name : str[¶](#ApiClient.ProjectComponent.SetName.name "Permalink to this definition")  
Name of the component

SetReported(*[state](#ApiClient.ProjectComponent.SetReported.state "ApiClient.ProjectComponent.SetReported.state (Python parameter) — True (=Default) to enable, False to disable the reporting of the test step.")=`True`*)[¶](#ApiClient.ProjectComponent.SetReported "Link to this definition")  
Enable or disable the reporting of the test step. If it has a parent test step, its reporting must also be enabled in order to have this test step appear in the report.

Parameters:  state : bool[¶](#ApiClient.ProjectComponent.SetReported.state "Permalink to this definition")  
True (=Default) to enable, False to disable the reporting of the test step.

GetPosition()[¶](#ApiClient.ProjectComponent.GetPosition "Link to this definition")  
Returns the position in the parent project.

Returns:  parent position

Return type:  int

Deprecated since version 2024.4: Please use method [`GetLineNo`](#ApiClient.ProjectComponent.GetLineNo "ApiClient.ProjectComponent.GetLineNo (Python method) — Returns the line number within its project.") instead.

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
