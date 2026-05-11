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

ParameterGenerator [ ParameterGenerator ](#)

ParameterGenerator

- [C ParameterGenerator ](#ApiClient.ParameterGenerator)
  - [M Clone ](#ApiClient.ParameterGenerator.Clone)
  - [M GenerateProject ](#ApiClient.ParameterGenerator.GenerateProject)
  - [M GetAttribute ](#ApiClient.ParameterGenerator.GetAttribute)
  - [M GetGeneratorAttributes ](#ApiClient.ParameterGenerator.GetGeneratorAttributes)
  - [M GetGeneratorId ](#ApiClient.ParameterGenerator.GetGeneratorId)
  - [M GetIndex ](#ApiClient.ParameterGenerator.GetIndex)
  - [M GetLineNo ](#ApiClient.ParameterGenerator.GetLineNo)
  - [M GetName ](#ApiClient.ParameterGenerator.GetName)
  - [M GetParent ](#ApiClient.ParameterGenerator.GetParent)
  - [M GetType ](#ApiClient.ParameterGenerator.GetType)
  - [M IsEnabled ](#ApiClient.ParameterGenerator.IsEnabled)
  - [M IsReported ](#ApiClient.ParameterGenerator.IsReported)
  - [M RemoveFromProject ](#ApiClient.ParameterGenerator.RemoveFromProject)
  - [M SetAttribute ](#ApiClient.ParameterGenerator.SetAttribute)
  - [M SetEnabled ](#ApiClient.ParameterGenerator.SetEnabled)
  - [M SetGeneratorAttributes ](#ApiClient.ParameterGenerator.SetGeneratorAttributes)
  - [M SetName ](#ApiClient.ParameterGenerator.SetName)
  - [M SetReported ](#ApiClient.ParameterGenerator.SetReported)
  - [M GetPosition ](#ApiClient.ParameterGenerator.GetPosition)

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

ParameterGenerator

- [C ParameterGenerator ](#ApiClient.ParameterGenerator)
  - [M Clone ](#ApiClient.ParameterGenerator.Clone)
  - [M GenerateProject ](#ApiClient.ParameterGenerator.GenerateProject)
  - [M GetAttribute ](#ApiClient.ParameterGenerator.GetAttribute)
  - [M GetGeneratorAttributes ](#ApiClient.ParameterGenerator.GetGeneratorAttributes)
  - [M GetGeneratorId ](#ApiClient.ParameterGenerator.GetGeneratorId)
  - [M GetIndex ](#ApiClient.ParameterGenerator.GetIndex)
  - [M GetLineNo ](#ApiClient.ParameterGenerator.GetLineNo)
  - [M GetName ](#ApiClient.ParameterGenerator.GetName)
  - [M GetParent ](#ApiClient.ParameterGenerator.GetParent)
  - [M GetType ](#ApiClient.ParameterGenerator.GetType)
  - [M IsEnabled ](#ApiClient.ParameterGenerator.IsEnabled)
  - [M IsReported ](#ApiClient.ParameterGenerator.IsReported)
  - [M RemoveFromProject ](#ApiClient.ParameterGenerator.RemoveFromProject)
  - [M SetAttribute ](#ApiClient.ParameterGenerator.SetAttribute)
  - [M SetEnabled ](#ApiClient.ParameterGenerator.SetEnabled)
  - [M SetGeneratorAttributes ](#ApiClient.ParameterGenerator.SetGeneratorAttributes)
  - [M SetName ](#ApiClient.ParameterGenerator.SetName)
  - [M SetReported ](#ApiClient.ParameterGenerator.SetReported)
  - [M GetPosition ](#ApiClient.ParameterGenerator.GetPosition)

# ParameterGenerator[¶](#parametergenerator "Link to this heading")

*class* ParameterGenerator[¶](#ApiClient.ParameterGenerator "Link to this definition")  
Clone()[¶](#ApiClient.ParameterGenerator.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`ParameterGenerator`](#ApiClient.ParameterGenerator "ApiClient.ParameterGenerator (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")

GenerateProject(*[destinationPath](#ApiClient.ParameterGenerator.GenerateProject.destinationPath "ApiClient.ParameterGenerator.GenerateProject.destinationPath (Python parameter) — Absolute destination path to store the project file")*)[¶](#ApiClient.ParameterGenerator.GenerateProject "Link to this definition")  
Initiates the execution of the generator and stores the result as a new project file.

Parameters:  destinationPath : str[¶](#ApiClient.ParameterGenerator.GenerateProject.destinationPath "Permalink to this definition")  
Absolute destination path to store the project file

GetAttribute(*[attributeName](#ApiClient.ParameterGenerator.GetAttribute.attributeName "ApiClient.ParameterGenerator.GetAttribute.attributeName (Python parameter) — Name of attribute to be returned")*)[¶](#ApiClient.ParameterGenerator.GetAttribute "Link to this definition")  
Returns the value of the attribute of the given name. Value is returned as str. Examples: int 5 –\> u”5” string “5” –\> u“‘5’” list [1,2,3] –\> u”[1,2,3]”

Parameters:  attributeName : str[¶](#ApiClient.ParameterGenerator.GetAttribute.attributeName "Permalink to this definition")  
Name of attribute to be returned

Returns:  attribute value

Return type:  str

GetGeneratorAttributes()[¶](#ApiClient.ParameterGenerator.GetGeneratorAttributes "Link to this definition")  
Returns all the stored attributes of the generator. Values are returned as str. Examples: int 5 –\> u”5” string “5” –\> u“‘5’” list [1,2,3] –\> u”[1,2,3]”

Returns:  Dictionary mapping attributes names to values

Return type:  dict[str, str]

GetGeneratorId()[¶](#ApiClient.ParameterGenerator.GetGeneratorId "Link to this definition")  
Returns the unique generator id of the referenced parameter generator.

Returns:  generator id

Return type:  str

GetIndex()[¶](#ApiClient.ParameterGenerator.GetIndex "Link to this definition")  
Returns the zero based index in the parent.

Returns:  Zero based index

Return type:  int

GetLineNo()[¶](#ApiClient.ParameterGenerator.GetLineNo "Link to this definition")  
Returns the line number within its project.

Returns:  Line number

Return type:  int

GetName()[¶](#ApiClient.ParameterGenerator.GetName "Link to this definition")  
Returns the name of the project component.

Returns:  Name of the component

Return type:  str

GetParent()[¶](#ApiClient.ParameterGenerator.GetParent "Link to this definition")  
Returns the parent project component.

Returns:  Parent component

Return type:  [`ProjectComponent`](ProjectComponent.md#ApiClient.ProjectComponent "ApiClient.ProjectComponent (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")

GetType()[¶](#ApiClient.ParameterGenerator.GetType "Link to this definition")  
Returns the type (class name) of the project component, e.g.  
- “ConfigChange”

- “ParameterSet”

- “PackageCall”

- “Project”

- “PackageGenerator”

Returns:  Type (class name) of the project component

Return type:  str

IsEnabled()[¶](#ApiClient.ParameterGenerator.IsEnabled "Link to this definition")  
Returns the state of the test step.

Returns:  True if test step is enabled, otherwise False

Return type:  bool

IsReported()[¶](#ApiClient.ParameterGenerator.IsReported "Link to this definition")  
Returns whether the test step will be reported. If it has a parent test step, this function will only return true if both this test step and the parent test step should be reported.

Returns:  True if test step will be reported, otherwise False

Return type:  bool

RemoveFromProject()[¶](#ApiClient.ParameterGenerator.RemoveFromProject "Link to this definition")  
Removes this component from the project.

Raises:  
**ApiError** – if the component is not part of any project

SetAttribute(*[attributeName](#ApiClient.ParameterGenerator.SetAttribute.attributeName "ApiClient.ParameterGenerator.SetAttribute.attributeName (Python parameter) — Name of attribute to be returned")*, *[value](#ApiClient.ParameterGenerator.SetAttribute.value "ApiClient.ParameterGenerator.SetAttribute.value (Python parameter) — attribute value")*)[¶](#ApiClient.ParameterGenerator.SetAttribute "Link to this definition")  
Sets the value of the attribute of the given name. Value has to be provided as str. Examples: int 5 –\> u”5” string “5” –\> u“‘5’” list [1,2,3] –\> u”[1,2,3]”

Parameters:  attributeName : str[¶](#ApiClient.ParameterGenerator.SetAttribute.attributeName "Permalink to this definition")  
Name of attribute to be returned

value : str[¶](#ApiClient.ParameterGenerator.SetAttribute.value "Permalink to this definition")  
attribute value

SetEnabled(*[state](#ApiClient.ParameterGenerator.SetEnabled.state "ApiClient.ParameterGenerator.SetEnabled.state (Python parameter) — True (=Default) to enable, False to disable the test step.")=`True`*)[¶](#ApiClient.ParameterGenerator.SetEnabled "Link to this definition")  
Enable or disable the test step.

Parameters:  state : bool[¶](#ApiClient.ParameterGenerator.SetEnabled.state "Permalink to this definition")  
True (=Default) to enable, False to disable the test step.

SetGeneratorAttributes(*[attributesDict](#ApiClient.ParameterGenerator.SetGeneratorAttributes.attributesDict "ApiClient.ParameterGenerator.SetGeneratorAttributes.attributesDict (Python parameter) — Dictionary mapping attribute names to values")*)[¶](#ApiClient.ParameterGenerator.SetGeneratorAttributes "Link to this definition")  
Overwrites the existing attributes of the generator with the provided ones. Values have to be provided as str. Examples: int 5 –\> u”5” string “5” –\> u“‘5’” list [1,2,3] –\> u”[1,2,3]”

Parameters:  attributesDict : dict[str, str][¶](#ApiClient.ParameterGenerator.SetGeneratorAttributes.attributesDict "Permalink to this definition")  
Dictionary mapping attribute names to values

SetName(*[name](#ApiClient.ParameterGenerator.SetName.name "ApiClient.ParameterGenerator.SetName.name (Python parameter) — Name of the component")*)[¶](#ApiClient.ParameterGenerator.SetName "Link to this definition")  
Sets the name of the project component.

Parameters:  name : str[¶](#ApiClient.ParameterGenerator.SetName.name "Permalink to this definition")  
Name of the component

SetReported(*[state](#ApiClient.ParameterGenerator.SetReported.state "ApiClient.ParameterGenerator.SetReported.state (Python parameter) — True (=Default) to enable, False to disable the reporting of the test step.")=`True`*)[¶](#ApiClient.ParameterGenerator.SetReported "Link to this definition")  
Enable or disable the reporting of the test step. If it has a parent test step, its reporting must also be enabled in order to have this test step appear in the report.

Parameters:  state : bool[¶](#ApiClient.ParameterGenerator.SetReported.state "Permalink to this definition")  
True (=Default) to enable, False to disable the reporting of the test step.

GetPosition()[¶](#ApiClient.ParameterGenerator.GetPosition "Link to this definition")  
Returns the position in the parent project.

Returns:  parent position

Return type:  int

Deprecated since version 2024.4: Please use method [`GetLineNo`](#ApiClient.ParameterGenerator.GetLineNo "ApiClient.ParameterGenerator.GetLineNo (Python method) — Returns the line number within its project.") instead.

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
