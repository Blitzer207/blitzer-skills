# API for Reports[¶](#api-for-reports "Link to this heading")

Part of the [Object based program API](objectApi.md#objectapi)

## ReportApi[¶](#reportapi "Link to this heading")

*class* ReportApi[¶](#ApiClient.ReportApi "Link to this definition")  
API to access test reports

Returned by

- [`ApiClient.ReportApi`](objectApi.md#ApiClient.ApiClient.ReportApi "ApiClient.ApiClient.ReportApi")

OpenReport(*filename*)[¶](#ApiClient.ReportApi.OpenReport "Link to this definition")  
Opens the referenced report file.

Parameters:  **filename** (*str*) – Filename of the report file as absolute path

Return type:  [`Report`](#ApiClient.Report "ApiClient.Report")

Returns:  The report

## Report[¶](#report "Link to this heading")

*class* Report[¶](#ApiClient.Report "Link to this definition")  
Returned by

- [`ReportApi.OpenReport`](#ApiClient.ReportApi.OpenReport "ApiClient.ReportApi.OpenReport")

Clone()[¶](#ApiClient.Report.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`Report`](#ApiClient.Report "ApiClient.Report")

Close()[¶](#ApiClient.Report.Close "Link to this definition")  
Closes the report. After closing the report it can not be modified/accessed anymore.

GetArtifacts(*mainPackageReportItemId=-1*)[¶](#ApiClient.Report.GetArtifacts "Link to this definition")  
Returns all artifacts that are referenced by the given main package report item Id.

**The parameter mainPackageReportItemId is deprecated.** Please use [`ReportPackage.GetArtifacts()`](#ApiClient.ReportPackage.GetArtifacts "ApiClient.ReportPackage.GetArtifacts") or just omit the parameter.

Parameters:  **mainPackageReportItemId** (*int*) – Deprecated. The report item ID. If None, all artifacts referenced in the report will be returned.

Returns:  A list of artifacts that are referenced by the given main package report item ID.

Return type:  list[[`Artifact`](#ApiClient.Artifact "ApiClient.Artifact")]

GetAuthor()[¶](#ApiClient.Report.GetAuthor "Link to this definition")  
Returns the test author.

Returns:  Test author

Return type:  str

GetDuration()[¶](#ApiClient.Report.GetDuration "Link to this definition")  
Returns the duration of the test execution.

Returns:  Execution duration in seconds

Return type:  float

GetExecutionTime()[¶](#ApiClient.Report.GetExecutionTime "Link to this definition")  
Returns the test execution date and time as string representation.

Returns:  Test execution date and time

Return type:  str

GetKeywordCatalog()[¶](#ApiClient.Report.GetKeywordCatalog "Link to this definition")  
Returns the name of the keyword catalog used during test execution.

Returns:  The catalog name or an empty string if no catalog was present at test execution.

Return type:  str

GetMainProject()[¶](#ApiClient.Report.GetMainProject "Link to this definition")  
Returns the main project. Raises an ApiError if the report is not the result of a project execution.

Returns:  List of direct project sub components

Return type:  [`ReportProject`](#ApiClient.ReportProject "ApiClient.ReportProject")

GetProjectExecutionPath()[¶](#ApiClient.Report.GetProjectExecutionPath "Link to this definition")  
Returns the execution path in relation to the calling project if executed as separate sub-project or the name of the project, if not not executed separately.

Returns:  Path in the project execution stack

Return type:  str

GetProjectName()[¶](#ApiClient.Report.GetProjectName "Link to this definition")  
Returns the name of the root project if it is a project report, otherwise empty string.

Returns:  Name of the project

Return type:  str

GetResult()[¶](#ApiClient.Report.GetResult "Link to this definition")  
Returns the total test result.

Returns:  Total test result

Return type:  str

GetTestManagementId()[¶](#ApiClient.Report.GetTestManagementId "Link to this definition")  
Returns the corresponding testmanagement Id of the root level project.

Returns:  Testmanagement Id or an empty string if no Id defined. If no project was executed None will be returned.

Return type:  str

GetTeststand()[¶](#ApiClient.Report.GetTeststand "Link to this definition")  
Returns the computer name where the test was executed.

Returns:  Name of the computer

Return type:  str

GetTimeZoneUTCOffset()[¶](#ApiClient.Report.GetTimeZoneUTCOffset "Link to this definition")  
Returns the offset from UTC in seconds based on the time zone in which the test report was generated. If no time zone is set in the report, None will be returned.

Returns:  Offset from UTC in seconds, or None

Return type:  int

GetTopLevelPackages()[¶](#ApiClient.Report.GetTopLevelPackages "Link to this definition")  
Convenience method for the testmanagement synchronization.

On a package report one package report will be returned. On a project report all package reports will be returned in a flat list regardless of directories. Packages of sub projects will be ignored.

Returns:  List of package objects

Return type:  list[[`ReportPackage`](#ApiClient.ReportPackage "ApiClient.ReportPackage")]

GetVersion()[¶](#ApiClient.Report.GetVersion "Link to this definition")  
Returns the ecu.test Version which created this report.

Returns:  Version of ecu.test

Return type:  str

IsProjectReport()[¶](#ApiClient.Report.IsProjectReport "Link to this definition")  
Checks if the report is from a project execution or not.

Returns:  True if the report is the result of a project execution, otherwise False

Return type:  bool

## Artifact[¶](#artifact "Link to this heading")

*class* Artifact[¶](#ApiClient.Artifact "Link to this definition")  
Returned by

- [`Report.GetArtifacts`](#ApiClient.Report.GetArtifacts "ApiClient.Report.GetArtifacts")

- [`ReportPackage.GetArtifacts`](#ApiClient.ReportPackage.GetArtifacts "ApiClient.ReportPackage.GetArtifacts")

- [`ReportParameterSet.GetArtifacts`](#ApiClient.ReportParameterSet.GetArtifacts "ApiClient.ReportParameterSet.GetArtifacts")

Clone()[¶](#ApiClient.Artifact.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`Artifact`](#ApiClient.Artifact "ApiClient.Artifact")

GetContext()[¶](#ApiClient.Artifact.GetContext "Link to this definition")  
Returns the artifact’s context.

Returns:  the artifact’s context

Return type:  str

GetFileHash()[¶](#ApiClient.Artifact.GetFileHash "Link to this definition")  
Returns the md5 hashsum if the file was stored on local file system.

Returns:  the md5 hashsum or empty string

Return type:  str

GetFileName()[¶](#ApiClient.Artifact.GetFileName "Link to this definition")  
Returns the name of the artifact.

Returns:  the artifact’s file name

Return type:  str

GetFilePath()[¶](#ApiClient.Artifact.GetFilePath "Link to this definition")  
Returns the path to the artifact. This can be a path on the local file system or an url.

Returns:  the file path

Return type:  str

GetMainPackageReportItemId()[¶](#ApiClient.Artifact.GetMainPackageReportItemId "Link to this definition")  
Returns the report item Id of the main package where the artifact was created.

Returns:  the report item Id of the main package

Return type:  int

## ReportProject[¶](#reportproject "Link to this heading")

*class* ReportProject[¶](#ApiClient.ReportProject "Link to this definition")  
Base class

[`ReportProjectElement`](#ApiClient.ReportProjectElement "ApiClient.ReportProjectElement")

Returned by

- [`Report.GetMainProject`](#ApiClient.Report.GetMainProject "ApiClient.Report.GetMainProject")

Clone()[¶](#ApiClient.ReportProject.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`ReportProject`](#ApiClient.ReportProject "ApiClient.ReportProject")

GetAttributes()[¶](#ApiClient.ReportProject.GetAttributes "Link to this definition")  
Returns all project attributes

Returns:  Dictionary of project attributes

Return type:  dict[str, str]

GetComment()[¶](#ApiClient.ReportProject.GetComment "Link to this definition")  
Returns the comment of the project element.

Returns:  Project element comment

Return type:  str

GetElementName()[¶](#ApiClient.ReportProject.GetElementName "Link to this definition")  
Returns the name of the project element.

Returns:  Element name

Return type:  str

GetProjectElements()[¶](#ApiClient.ReportProject.GetProjectElements "Link to this definition")  
Returns a list of all direct project child elements.

Returns:  List of direct project child elements

Return type:  list[[`ReportProjectElement`](#ApiClient.ReportProjectElement "ApiClient.ReportProjectElement")]

GetReportItemId()[¶](#ApiClient.ReportProject.GetReportItemId "Link to this definition")  
Returns the ReportItem Id of the project element.

Returns:  ReportItem Id

Return type:  int

GetResult()[¶](#ApiClient.ReportProject.GetResult "Link to this definition")  
Returns the result of the project element.

Returns:  Project element result

Return type:  str

GetType()[¶](#ApiClient.ReportProject.GetType "Link to this definition")  
Returns the type (class name) of the project element, e.g.  
- “ReportConfigurationChange”

- “ReportFolderElement”

- “ReportPackage”

- “ReportParameterizedPackage”

- “ReportParameterSet”

- “ReportProjectElement”

- “ReportProject”

Returns:  Type (class name) of the test step

Return type:  str

## ReportProjectElement[¶](#reportprojectelement "Link to this heading")

*class* ReportProjectElement[¶](#ApiClient.ReportProjectElement "Link to this definition")  
Returned by

- [`ReportConfigurationChange.GetProjectElements`](#ApiClient.ReportConfigurationChange.GetProjectElements "ApiClient.ReportConfigurationChange.GetProjectElements")

- [`ReportFolderElement.GetProjectElements`](#ApiClient.ReportFolderElement.GetProjectElements "ApiClient.ReportFolderElement.GetProjectElements")

- [`ReportPackage.GetProjectElements`](#ApiClient.ReportPackage.GetProjectElements "ApiClient.ReportPackage.GetProjectElements")

- [`ReportPackage.GetStimulationPackage`](#ApiClient.ReportPackage.GetStimulationPackage "ApiClient.ReportPackage.GetStimulationPackage")

- [`ReportParameterSet.GetProjectElements`](#ApiClient.ReportParameterSet.GetProjectElements "ApiClient.ReportParameterSet.GetProjectElements")

- [`ReportParameterSet.GetStimulationPackage`](#ApiClient.ReportParameterSet.GetStimulationPackage "ApiClient.ReportParameterSet.GetStimulationPackage")

- [`ReportParameterizedPackage.GetProjectElements`](#ApiClient.ReportParameterizedPackage.GetProjectElements "ApiClient.ReportParameterizedPackage.GetProjectElements")

- [`ReportProject.GetProjectElements`](#ApiClient.ReportProject.GetProjectElements "ApiClient.ReportProject.GetProjectElements")

- [`ReportProjectElement.GetProjectElements`](#ApiClient.ReportProjectElement.GetProjectElements "ApiClient.ReportProjectElement.GetProjectElements")

Subclasses

- [`ReportConfigurationChange`](#ApiClient.ReportConfigurationChange "ApiClient.ReportConfigurationChange")

- [`ReportFolderElement`](#ApiClient.ReportFolderElement "ApiClient.ReportFolderElement")

- [`ReportPackage`](#ApiClient.ReportPackage "ApiClient.ReportPackage")

- [`ReportParameterSet`](#ApiClient.ReportParameterSet "ApiClient.ReportParameterSet")

- [`ReportParameterizedPackage`](#ApiClient.ReportParameterizedPackage "ApiClient.ReportParameterizedPackage")

- [`ReportProject`](#ApiClient.ReportProject "ApiClient.ReportProject")

Clone()[¶](#ApiClient.ReportProjectElement.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`ReportProjectElement`](#ApiClient.ReportProjectElement "ApiClient.ReportProjectElement")

GetComment()[¶](#ApiClient.ReportProjectElement.GetComment "Link to this definition")  
Returns the comment of the project element.

Returns:  Project element comment

Return type:  str

GetElementName()[¶](#ApiClient.ReportProjectElement.GetElementName "Link to this definition")  
Returns the name of the project element.

Returns:  Element name

Return type:  str

GetProjectElements()[¶](#ApiClient.ReportProjectElement.GetProjectElements "Link to this definition")  
Returns a list of all direct project child elements.

Returns:  List of direct project child elements

Return type:  list[[`ReportProjectElement`](#ApiClient.ReportProjectElement "ApiClient.ReportProjectElement")]

GetReportItemId()[¶](#ApiClient.ReportProjectElement.GetReportItemId "Link to this definition")  
Returns the ReportItem Id of the project element.

Returns:  ReportItem Id

Return type:  int

GetResult()[¶](#ApiClient.ReportProjectElement.GetResult "Link to this definition")  
Returns the result of the project element.

Returns:  Project element result

Return type:  str

GetType()[¶](#ApiClient.ReportProjectElement.GetType "Link to this definition")  
Returns the type (class name) of the project element, e.g.  
- “ReportConfigurationChange”

- “ReportFolderElement”

- “ReportPackage”

- “ReportParameterizedPackage”

- “ReportParameterSet”

- “ReportProjectElement”

- “ReportProject”

Returns:  Type (class name) of the test step

Return type:  str

## ReportPackage[¶](#reportpackage "Link to this heading")

*class* ReportPackage[¶](#ApiClient.ReportPackage "Link to this definition")  
Base class

[`ReportProjectElement`](#ApiClient.ReportProjectElement "ApiClient.ReportProjectElement")

Returned by

- [`Report.GetTopLevelPackages`](#ApiClient.Report.GetTopLevelPackages "ApiClient.Report.GetTopLevelPackages")

- [`ReportAnalysisJob.GetStimulationPackage`](#ApiClient.ReportAnalysisJob.GetStimulationPackage "ApiClient.ReportAnalysisJob.GetStimulationPackage")

Subclasses

- [`ReportParameterSet`](#ApiClient.ReportParameterSet "ApiClient.ReportParameterSet")

Clone()[¶](#ApiClient.ReportPackage.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`ReportPackage`](#ApiClient.ReportPackage "ApiClient.ReportPackage")

GetAbortCode()[¶](#ApiClient.ReportPackage.GetAbortCode "Link to this definition")  
Returns the abort code of the package or an empty string if it was not aborted.

Returns:  Abort code of the package

Return type:  str

GetAbortComment()[¶](#ApiClient.ReportPackage.GetAbortComment "Link to this definition")  
Returns the abort comment of the package or an empty string if it was not aborted.

Returns:  Abort comment of the package

Return type:  str

GetArtifacts()[¶](#ApiClient.ReportPackage.GetArtifacts "Link to this definition")  
Returns all referenced artifacts.

Returns:  A list of all referenced artifacts.

Return type:  list[[`Artifact`](#ApiClient.Artifact "ApiClient.Artifact")]

GetAttributes()[¶](#ApiClient.ReportPackage.GetAttributes "Link to this definition")  
Returns all package attributes

Returns:  Dictionary of package attributes

Return type:  dict[str, str]

GetComment()[¶](#ApiClient.ReportPackage.GetComment "Link to this definition")  
Returns the comment of the package.

Returns:  Comment of the package

Return type:  str

GetDuration()[¶](#ApiClient.ReportPackage.GetDuration "Link to this definition")  
Returns the duration of the test execution.

Returns:  Execution duration in seconds

Return type:  float

GetElementName()[¶](#ApiClient.ReportPackage.GetElementName "Link to this definition")  
Returns the project element name.

Returns:  Name of the project element

Return type:  str

GetExecutionTime()[¶](#ApiClient.ReportPackage.GetExecutionTime "Link to this definition")  
Returns the test execution date and time as string representation.

Returns:  Execution time

Return type:  str

GetFilename()[¶](#ApiClient.ReportPackage.GetFilename "Link to this definition")  
Returns the filename of the package which corresponds to the column ‘Activity’ in the project summary (without file extension).

Returns:  Name of the package file

Return type:  str

GetGlobalConstantsDefinedOnStart()[¶](#ApiClient.ReportPackage.GetGlobalConstantsDefinedOnStart "Link to this definition")  
Gets the values that the global constants had at the start of the Package execution.

Returns:  list of global constants

Return type:  list[[`GlobalConstant`](#ApiClient.GlobalConstant "ApiClient.GlobalConstant")]

GetName()[¶](#ApiClient.ReportPackage.GetName "Link to this definition")  
Returns the package name.

Returns:  Package name

Return type:  str

GetOriginalResult()[¶](#ApiClient.ReportPackage.GetOriginalResult "Link to this definition")  
Returns the original total test result.

Returns:  Original total test result

Return type:  str

GetParameterDescription(*name*)[¶](#ApiClient.ReportPackage.GetParameterDescription "Link to this definition")  
Returns the description of the parameter specified by the given name.

Parameters:  **name** (*str*) – Name of the parameter

Returns:  Description of the parameter

Return type:  str

GetParameterInitialValue(*name*)[¶](#ApiClient.ReportPackage.GetParameterInitialValue "Link to this definition")  
Returns the initial value of the parameter specified by the given name.

Parameters:  **name** (*str*) – Name of the parameter

Returns:  Initial value of the parameter

Return type:  str

GetParameterNames()[¶](#ApiClient.ReportPackage.GetParameterNames "Link to this definition")  
Returns a list of parameter names.

Returns:  List of names

Return type:  list[str]

GetParameterOrigin(*name*)[¶](#ApiClient.ReportPackage.GetParameterOrigin "Link to this definition")  
Returns the origin of the parameter specified by the given name.

Parameters:  **name** (*str*) – Name of the parameter

Returns:  Origin of the parameter

Return type:  str

GetParameterValue(*name*)[¶](#ApiClient.ReportPackage.GetParameterValue "Link to this definition")  
Returns the latest value of the parameter specified by the given name.

Parameters:  **name** (*str*) – Name of the parameter

Returns:  Value of the parameter

Return type:  str

GetProjectElements()[¶](#ApiClient.ReportPackage.GetProjectElements "Link to this definition")  
Returns a list of all direct project child elements.

Returns:  List of direct project child elements

Return type:  list[[`ReportProjectElement`](#ApiClient.ReportProjectElement "ApiClient.ReportProjectElement")]

GetRecordings()[¶](#ApiClient.ReportPackage.GetRecordings "Link to this definition")  
Returns the recordings created or used by the package.

Returns:  The recording objects

Return type:  list[[`ReportRecording`](#ApiClient.ReportRecording "ApiClient.ReportRecording")]

GetReportItemId()[¶](#ApiClient.ReportPackage.GetReportItemId "Link to this definition")  
Returns the ReportItem Id of the project element.

Returns:  ReportItem Id

Return type:  int

GetResult()[¶](#ApiClient.ReportPackage.GetResult "Link to this definition")  
Returns the package result.

Returns:  Package result

Return type:  str

GetReturnDescription(*name*)[¶](#ApiClient.ReportPackage.GetReturnDescription "Link to this definition")  
Returns the description of the return specified by the given name.

Parameters:  **name** (*str*) – Name of the return

Returns:  Description of the return

Return type:  str

GetReturnInitialValue(*name*)[¶](#ApiClient.ReportPackage.GetReturnInitialValue "Link to this definition")  
Returns the initial value of the return specified by the given name.

Parameters:  **name** (*str*) – Name of the return

Returns:  Initial value of the return

Return type:  str

GetReturnNames()[¶](#ApiClient.ReportPackage.GetReturnNames "Link to this definition")  
Returns a list of return names.

Returns:  List of names

Return type:  list[str]

GetReturnValue(*name*)[¶](#ApiClient.ReportPackage.GetReturnValue "Link to this definition")  
Returns the latest value of the return specified by the given name.

Parameters:  **name** (*str*) – Name of the return

Returns:  Value of the return

Return type:  str

GetRevalComments()[¶](#ApiClient.ReportPackage.GetRevalComments "Link to this definition")  
Returns all revaluation comments of the package.

Returns:  List of revaluation comments

Return type:  list[[`RevaluationComment`](#ApiClient.RevaluationComment "ApiClient.RevaluationComment")]

GetStimulationPackage(*returnParamSets=True*)[¶](#ApiClient.ReportPackage.GetStimulationPackage "Link to this definition")  
This call is only valid for analysis packages and returns the stimulation package.

Note:  
For older reports (before 2022.2) this method may return None if no trace analysis was executed.

Parameters:  **returnParamSets** (*bool*) –

Specifies, how to deal with stimulation parameter sets. If True, the parameter set that has been used to stimulate the execution of the analysis package is returned.

If False, the stimulation package itself is returned, which is of type [`ReportParameterizedPackage`](#ApiClient.ReportParameterizedPackage "ApiClient.ReportParameterizedPackage") for parameterized stimulations.

Returns:  The stimulation package. The default return value will be of type [`ReportPackage`](#ApiClient.ReportPackage "ApiClient.ReportPackage"). If returnParamSets is False, it is possibly also of type [`ReportParameterizedPackage`](#ApiClient.ReportParameterizedPackage "ApiClient.ReportParameterizedPackage").

Return type:  [`ReportProjectElement`](#ApiClient.ReportProjectElement "ApiClient.ReportProjectElement")

GetTestCase()[¶](#ApiClient.ReportPackage.GetTestCase "Link to this definition")  
Returns the test case of the package.

Returns:  Test case of the package

Return type:  [`ReportTestCase`](#ApiClient.ReportTestCase "ApiClient.ReportTestCase")

GetTestManagementId()[¶](#ApiClient.ReportPackage.GetTestManagementId "Link to this definition")  
Returns the corresponding testmanagement ID.

Returns:  Testmanagement ID or an empty string if no ID defined.

Return type:  str

GetTestScriptId()[¶](#ApiClient.ReportPackage.GetTestScriptId "Link to this definition")  
Returns the corresponding testscript ID.

Returns:  Testscript ID or an empty string if no ID defined.

Return type:  str

GetTraceAnalysisJobs()[¶](#ApiClient.ReportPackage.GetTraceAnalysisJobs "Link to this definition")  
Returns a list of the analysis jobs of the package.

Returns:  List of analysis jobs

Return type:  list[[`ReportAnalysisJob`](#ApiClient.ReportAnalysisJob "ApiClient.ReportAnalysisJob")]

GetType()[¶](#ApiClient.ReportPackage.GetType "Link to this definition")  
Returns the type (class name) of the project element, e.g.  
- “ReportConfigurationChange”

- “ReportFolderElement”

- “ReportPackage”

- “ReportParameterizedPackage”

- “ReportParameterSet”

- “ReportProjectElement”

- “ReportProject”

Returns:  Type (class name) of the test step

Return type:  str

GetUserDefinedData()[¶](#ApiClient.ReportPackage.GetUserDefinedData "Link to this definition")  
Returns the user defined report information.

Returns:  Name and value of the user defined information.

Return type:  dict[str, str]

IsAnalysisPackage()[¶](#ApiClient.ReportPackage.IsAnalysisPackage "Link to this definition")  
Returns, whether this package is an analysis package.

Returns:  True if this package is an analysis package

Return type:  bool

IsSkipped()[¶](#ApiClient.ReportPackage.IsSkipped "Link to this definition")  
Returns True if the package was skipped.

Returns:  True if skipped

Return type:  bool

IsStimulationPackage()[¶](#ApiClient.ReportPackage.IsStimulationPackage "Link to this definition")  
Returns, whether this package is a stimulation package.

Returns:  True if this package is a stimulation package

Return type:  bool

## GlobalConstant[¶](#globalconstant "Link to this heading")

*class* GlobalConstant[¶](#ApiClient.GlobalConstant "Link to this definition")  
Represents a global constant.

Returned by

- [`ReportPackage.GetGlobalConstantsDefinedOnStart`](#ApiClient.ReportPackage.GetGlobalConstantsDefinedOnStart "ApiClient.ReportPackage.GetGlobalConstantsDefinedOnStart")

- [`ReportParameterSet.GetGlobalConstantsDefinedOnStart`](#ApiClient.ReportParameterSet.GetGlobalConstantsDefinedOnStart "ApiClient.ReportParameterSet.GetGlobalConstantsDefinedOnStart")

Clone()[¶](#ApiClient.GlobalConstant.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`GlobalConstant`](#ApiClient.GlobalConstant "ApiClient.GlobalConstant")

GetName()[¶](#ApiClient.GlobalConstant.GetName "Link to this definition")  
Returns the name of the global constant.

Returns:  global constant name

Return type:  str

GetValue()[¶](#ApiClient.GlobalConstant.GetValue "Link to this definition")  
Returns the value of the global constant.

Returns:  global constant value

Return type:  str

## ReportRecording[¶](#reportrecording "Link to this heading")

*class* ReportRecording[¶](#ApiClient.ReportRecording "Link to this definition")  
Returned by

- [`ReportPackage.GetRecordings`](#ApiClient.ReportPackage.GetRecordings "ApiClient.ReportPackage.GetRecordings")

- [`ReportParameterSet.GetRecordings`](#ApiClient.ReportParameterSet.GetRecordings "ApiClient.ReportParameterSet.GetRecordings")

- [`ReportRecordingInfo.GetRecording`](#ApiClient.ReportRecordingInfo.GetRecording "ApiClient.ReportRecordingInfo.GetRecording")

PATH_ABS[¶](#ApiClient.ReportRecording.PATH_ABS "Link to this definition")  
The constant used to specify that the recording path is stored as absolute path.

Returns:  The constant

Return type:  int

PATH_REL_REPORT[¶](#ApiClient.ReportRecording.PATH_REL_REPORT "Link to this definition")  
The constant used to specify that the recording path is stored relative to the report database.

Returns:  The constant

Return type:  int

PATH_REL_WORKSPACE[¶](#ApiClient.ReportRecording.PATH_REL_WORKSPACE "Link to this definition")  
The constant used to specify that the recording path is stored relative to the workspace used for the test.

Returns:  The constant

Return type:  int

SOURCE_FLAG_AUTOGENERATED[¶](#ApiClient.ReportRecording.SOURCE_FLAG_AUTOGENERATED "Link to this definition")  
The bit flag used to indicate that the recording was automatically generated (e.g. by a trace analysis).

Returns:  The constant

Return type:  int

SOURCE_FLAG_STIMULATION[¶](#ApiClient.ReportRecording.SOURCE_FLAG_STIMULATION "Link to this definition")  
The bit flag used to indicate that the recording is originated from a stimulation package.

Returns:  The constant

Return type:  int

SOURCE_MANUAL[¶](#ApiClient.ReportRecording.SOURCE_MANUAL "Link to this definition")  
The constant used to specify that the recording was manually added.

Returns:  The constant

Return type:  int

SOURCE_RECORDING[¶](#ApiClient.ReportRecording.SOURCE_RECORDING "Link to this definition")  
The constant used to specify that the recording was recorded during the test.

Returns:  The constant

Return type:  int

SOURCE_TRACEANALYSIS[¶](#ApiClient.ReportRecording.SOURCE_TRACEANALYSIS "Link to this definition")  
The constant used to specify that the recording was added by a trace analysis.

Returns:  The constant

Return type:  int

SOURCE_TRACEMERGE[¶](#ApiClient.ReportRecording.SOURCE_TRACEMERGE "Link to this definition")  
The constant used to specify that the recording was added by a trace merge.

Returns:  The constant

Return type:  int

Clone()[¶](#ApiClient.ReportRecording.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`ReportRecording`](#ApiClient.ReportRecording "ApiClient.ReportRecording")

GetAbsolutePath()[¶](#ApiClient.ReportRecording.GetAbsolutePath "Link to this definition")  
Convenience method to get the absolute path to the recording file. Depending on the path type a base directory will be determined to make an absolute path:

> - [`ReportRecording.PATH_REL_REPORT`](#ApiClient.ReportRecording.PATH_REL_REPORT "ApiClient.ReportRecording.PATH_REL_REPORT"): The path to the current report will be used to make the path absolute.
>
> - [`ReportRecording.PATH_ABS`](#ApiClient.ReportRecording.PATH_ABS "ApiClient.ReportRecording.PATH_ABS"): The path will be returned as it is.
>
> - [`ReportRecording.PATH_REL_WORKSPACE`](#ApiClient.ReportRecording.PATH_REL_WORKSPACE "ApiClient.ReportRecording.PATH_REL_WORKSPACE"): The current workspace path will be used to make the path absolute.

Returns:  The absolute path

Return type:  str

GetNameAndFormatDetails()[¶](#ApiClient.ReportRecording.GetNameAndFormatDetails "Link to this definition")  
Returns the recording name and the format details (if set).

Returns:  The recording name and the format details as text of the form “\<name\> (\<formatdetails\>)” if format details are set else of the form “\<name\>”.

Return type:  str

GetNumber()[¶](#ApiClient.ReportRecording.GetNumber "Link to this definition")  
Returns the recording number.

Returns:  The recording number

Return type:  int

GetOrigin()[¶](#ApiClient.ReportRecording.GetOrigin "Link to this definition")  
Returns the origin, a text representation of [`ReportRecording.GetSource()`](#ApiClient.ReportRecording.GetSource "ApiClient.ReportRecording.GetSource").

Returns:  The origin

Return type:  str

GetPath()[¶](#ApiClient.ReportRecording.GetPath "Link to this definition")  
Returns the path to the recording file. The path can be absolute or relative. The path type can be read by calling [`GetPathType()`](#ApiClient.ReportRecording.GetPathType "ApiClient.ReportRecording.GetPathType").

Returns:  The path

Return type:  str

GetPathType()[¶](#ApiClient.ReportRecording.GetPathType "Link to this definition")  
Returns how the path is to the recording is stored in the report.

Returns:  Can return the following constants:

- [`ReportRecording.PATH_REL_REPORT`](#ApiClient.ReportRecording.PATH_REL_REPORT "ApiClient.ReportRecording.PATH_REL_REPORT")

- [`ReportRecording.PATH_ABS`](#ApiClient.ReportRecording.PATH_ABS "ApiClient.ReportRecording.PATH_ABS")

- [`ReportRecording.PATH_REL_WORKSPACE`](#ApiClient.ReportRecording.PATH_REL_WORKSPACE "ApiClient.ReportRecording.PATH_REL_WORKSPACE")

Return type:  int

GetRecordingGroupName()[¶](#ApiClient.ReportRecording.GetRecordingGroupName "Link to this definition")  
Returns the name of the recording group.

Returns:  The recording group name

Return type:  str

GetSignalGroupName()[¶](#ApiClient.ReportRecording.GetSignalGroupName "Link to this definition")  
Returns the name of the signal group.

Returns:  The signal group name

Return type:  str

GetSource()[¶](#ApiClient.ReportRecording.GetSource "Link to this definition")  
Returns the source of the recording.

Returns:  Can return the following constants:

> - [`ReportRecording.SOURCE_RECORDING`](#ApiClient.ReportRecording.SOURCE_RECORDING "ApiClient.ReportRecording.SOURCE_RECORDING")
>
> - [`ReportRecording.SOURCE_MANUAL`](#ApiClient.ReportRecording.SOURCE_MANUAL "ApiClient.ReportRecording.SOURCE_MANUAL")
>
> - [`ReportRecording.SOURCE_TRACEANALYSIS`](#ApiClient.ReportRecording.SOURCE_TRACEANALYSIS "ApiClient.ReportRecording.SOURCE_TRACEANALYSIS")

In combination with the flags:

> - [`ReportRecording.SOURCE_FLAG_STIMULATION`](#ApiClient.ReportRecording.SOURCE_FLAG_STIMULATION "ApiClient.ReportRecording.SOURCE_FLAG_STIMULATION")
>
> - [`ReportRecording.SOURCE_FLAG_AUTOGENERATED`](#ApiClient.ReportRecording.SOURCE_FLAG_AUTOGENERATED "ApiClient.ReportRecording.SOURCE_FLAG_AUTOGENERATED")

Return type:  int

GetSyncDeltaT()[¶](#ApiClient.ReportRecording.GetSyncDeltaT "Link to this definition")  
Returns the deltaT, calculated by the synchronization, that is applied to the time axis.

Returns:  The time offset deltaT. Will be None, if no synchronization was executed, but will default to 0.0 if this recording is reported by a trace analysis.

Return type:  float

GetType()[¶](#ApiClient.ReportRecording.GetType "Link to this definition")  
Returns the type of the recording, e.g. “CSV”.

Returns:  The type identifier

Return type:  str

## RevaluationComment[¶](#revaluationcomment "Link to this heading")

*class* RevaluationComment[¶](#ApiClient.RevaluationComment "Link to this definition")  
Returned by

- [`ReportAnalysisEpisode.GetRevalComments`](#ApiClient.ReportAnalysisEpisode.GetRevalComments "ApiClient.ReportAnalysisEpisode.GetRevalComments")

- [`ReportAnalysisStep.GetRevalComments`](#ApiClient.ReportAnalysisStep.GetRevalComments "ApiClient.ReportAnalysisStep.GetRevalComments")

- [`ReportPackage.GetRevalComments`](#ApiClient.ReportPackage.GetRevalComments "ApiClient.ReportPackage.GetRevalComments")

- [`ReportParameterSet.GetRevalComments`](#ApiClient.ReportParameterSet.GetRevalComments "ApiClient.ReportParameterSet.GetRevalComments")

- [`ReportTestStep.GetRevalComments`](#ApiClient.ReportTestStep.GetRevalComments "ApiClient.ReportTestStep.GetRevalComments")

Clone()[¶](#ApiClient.RevaluationComment.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`RevaluationComment`](#ApiClient.RevaluationComment "ApiClient.RevaluationComment")

GetAuthor()[¶](#ApiClient.RevaluationComment.GetAuthor "Link to this definition")  
Returns the author of the revaluation comment.

Returns:  Author of the comment

Return type:  str

GetResult()[¶](#ApiClient.RevaluationComment.GetResult "Link to this definition")  
Returns the revaluated result.

Returns:  The revaluated result or None

Return type:  str

GetText()[¶](#ApiClient.RevaluationComment.GetText "Link to this definition")  
Returns the text of the of revaluation comment.

Returns:  Text of the comment

Return type:  str

GetTime()[¶](#ApiClient.RevaluationComment.GetTime "Link to this definition")  
Returns the creation date and time of the revaluation comment.

Returns:  Creation date and time of the revaluation comment

Return type:  str

## ReportTestCase[¶](#reporttestcase "Link to this heading")

*class* ReportTestCase[¶](#ApiClient.ReportTestCase "Link to this definition")  
Returned by

- [`ReportPackage.GetTestCase`](#ApiClient.ReportPackage.GetTestCase "ApiClient.ReportPackage.GetTestCase")

- [`ReportParameterSet.GetTestCase`](#ApiClient.ReportParameterSet.GetTestCase "ApiClient.ReportParameterSet.GetTestCase")

Clone()[¶](#ApiClient.ReportTestCase.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`ReportTestCase`](#ApiClient.ReportTestCase "ApiClient.ReportTestCase")

GetResult()[¶](#ApiClient.ReportTestCase.GetResult "Link to this definition")  
Returns the result of the test case.

Returns:  result of the test case

Return type:  str

GetTestSteps()[¶](#ApiClient.ReportTestCase.GetTestSteps "Link to this definition")  
Returns all direct child test steps of the test case.

Returns:  List of test step results

Return type:  list[[`ReportTestStep`](#ApiClient.ReportTestStep "ApiClient.ReportTestStep")]

## ReportTestStep[¶](#reportteststep "Link to this heading")

*class* ReportTestStep[¶](#ApiClient.ReportTestStep "Link to this definition")  
Returned by

- [`ReportTestCase.GetTestSteps`](#ApiClient.ReportTestCase.GetTestSteps "ApiClient.ReportTestCase.GetTestSteps")

- [`ReportTestStep.GetTestSteps`](#ApiClient.ReportTestStep.GetTestSteps "ApiClient.ReportTestStep.GetTestSteps")

AddRevalComment(*author*, *comment*, *revaluation=None*)[¶](#ApiClient.ReportTestStep.AddRevalComment "Link to this definition")  
Add a revaluation comment to the test step.

Parameters:  - **author** (*str*) – author of the comment

- **comment** (*str*) – text of the comment. Must be at least 10 characters

- **revaluation** (*str*) – “NONE”, “SUCCESS”, “INCONCLUSIVE”, “FAILED” or “ERROR”; None to just add a comment without changing the result

Clone()[¶](#ApiClient.ReportTestStep.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`ReportTestStep`](#ApiClient.ReportTestStep "ApiClient.ReportTestStep")

GetAbortCode()[¶](#ApiClient.ReportTestStep.GetAbortCode "Link to this definition")  
Returns the abort code of the report item.

Returns:  Abort code

Return type:  str

GetAbortComment()[¶](#ApiClient.ReportTestStep.GetAbortComment "Link to this definition")  
Returns the abort comment of the report item.

Returns:  Abort comment

Return type:  str

GetAbsoluteTime()[¶](#ApiClient.ReportTestStep.GetAbsoluteTime "Link to this definition")  
Returns the content of the ‘Time (absolute)’ column.

Returns:  Content of the ‘Time (absolute)’ column

Return type:  float

GetComment()[¶](#ApiClient.ReportTestStep.GetComment "Link to this definition")  
Returns the content of the ‘Comment’ column.

Returns:  Content of the ‘Comment’ column

Return type:  str

GetEntities()[¶](#ApiClient.ReportTestStep.GetEntities "Link to this definition")  
Returns a list of all entities.

Returns:  a list of all entity objects

Return type:  list[[`Entity`](#ApiClient.Entity "ApiClient.Entity")]

GetExpectedValue()[¶](#ApiClient.ReportTestStep.GetExpectedValue "Link to this definition")  
Returns the content of the ‘Expected value’ column. :return: Content of the ‘Expected value’ column :rtype: str

GetId()[¶](#ApiClient.ReportTestStep.GetId "Link to this definition")  
Returns the Id of the report item.

Returns:  Id of the report item

Return type:  int

GetLabel()[¶](#ApiClient.ReportTestStep.GetLabel "Link to this definition")  
Returns the content of the ‘Activity/Name’ column for test steps. Returns the content of the ‘Name’ column for trace steps.

Returns:  Content of the ‘Activity/Name’ column for test steps and content of the ‘Name’ column for trace steps

Return type:  str

GetMappingTargets()[¶](#ApiClient.ReportTestStep.GetMappingTargets "Link to this definition")  
Returns a list with the contents of the ‘Mapping target’ column.

Returns:  Content of the ‘Mapping target’ column

Return type:  list[str]

GetNestingLevel()[¶](#ApiClient.ReportTestStep.GetNestingLevel "Link to this definition")  
Returns the nesting depth.

Returns:  Nesting depth

Return type:  int

GetOriginalResult()[¶](#ApiClient.ReportTestStep.GetOriginalResult "Link to this definition")  
Returns the content of the ‘Original evaluation’ column.

Returns:  Content of the ‘Original evaluation’ column

Return type:  str

GetParentId()[¶](#ApiClient.ReportTestStep.GetParentId "Link to this definition")  
Returns the Id of the parent report item.

Returns:  Id of the parent report item

Return type:  int

GetPosition()[¶](#ApiClient.ReportTestStep.GetPosition "Link to this definition")  
Returns the position of the step within the test case / trace analysis. Example 1: “3” is returned for the step which is at position 3 in the top level Package. Example 2: “5.13” is returned for the 13th step of the subpackage which is at position 5 in the top level Package.

Returns:  position within the test case / trace analysis

Return type:  str

GetRelativeRealTime()[¶](#ApiClient.ReportTestStep.GetRelativeRealTime "Link to this definition")  
Returns the content of the ‘Time [s] (relative)’ column.

Returns:  Content of the ‘Time [s] (relative)’ column

Return type:  float

GetRelativeTestTime()[¶](#ApiClient.ReportTestStep.GetRelativeTestTime "Link to this definition")  
Returns the content of the ‘Test time [s]’ column.

Returns:  Content of the ‘Test time [s]’ column

Return type:  float

GetResult()[¶](#ApiClient.ReportTestStep.GetResult "Link to this definition")  
Returns the content of the ‘Evaluation’ column.

Returns:  Content of the ‘Evaluation’ column

Return type:  str

GetRevalComments()[¶](#ApiClient.ReportTestStep.GetRevalComments "Link to this definition")  
Returns all revaluation comments of the test step.

Returns:  List of revaluation comments

Return type:  list[[`RevaluationComment`](#ApiClient.RevaluationComment "ApiClient.RevaluationComment")]

GetTags()[¶](#ApiClient.ReportTestStep.GetTags "Link to this definition")  
Returns all tags associated with this report entry.

Returns:  Tags

Return type:  list[str]

GetTestSteps()[¶](#ApiClient.ReportTestStep.GetTestSteps "Link to this definition")  
Returns all direct child test steps of the test step. If the test step is no container an empty list will be returned.

Returns:  List of test step results

Return type:  list[[`ReportTestStep`](#ApiClient.ReportTestStep "ApiClient.ReportTestStep")]

GetTextEntities()[¶](#ApiClient.ReportTestStep.GetTextEntities "Link to this definition")  
Returns all text entities associated with this report entry.

Returns:  text entities

Return type:  list[list[str]]

GetTimeDiffToPreviousTeststep()[¶](#ApiClient.ReportTestStep.GetTimeDiffToPreviousTeststep "Link to this definition")  
Returns the time difference in seconds between the previous test step and this test step. :return: The time difference in seconds :rtype: float

GetUserDefinedReportDetails()[¶](#ApiClient.ReportTestStep.GetUserDefinedReportDetails "Link to this definition")  
Returns a list of all report details defined by the user during test execution. Each item in the list is a tuple, representing a line within the report details. The header line displayed in the report is not included in the returned list.

Returns:  A list of tuples, each inner list representing a line within the report details

Return type:  list[list[str]]

GetValue()[¶](#ApiClient.ReportTestStep.GetValue "Link to this definition")  
Returns the content of the ‘Value’ column.

Returns:  Content of the ‘Value’ column

Return type:  str

HasTag(*tagName*)[¶](#ApiClient.ReportTestStep.HasTag "Link to this definition")  
Parameters:  **tagName** (*str*) – The tag to check for

Returns:  Whether this report item has set the specified tag

Return type:  bool

GetActivity()[¶](#ApiClient.ReportTestStep.GetActivity "Link to this definition")  
Returns the activity part of the content of the ‘Activity/Name’ column for test steps. Returns the content of the ‘Name’ column for trace steps.

Returns:  Activity part of the ‘Activity/Name’ column for test steps and content of ‘Name’ column for trace steps

Return type:  str

Deprecated since version 2020.2: Use [`GetLabel()`](#ApiClient.ReportTestStep.GetLabel "ApiClient.ReportTestStep.GetLabel") instead.

GetName()[¶](#ApiClient.ReportTestStep.GetName "Link to this definition")  
Returns the name part of the content of the ‘Activity/Name’ column for test steps.

Returns:  Name part of the ‘Activity/Name’ column

Return type:  str

Deprecated since version 2020.2: Use [`GetLabel()`](#ApiClient.ReportTestStep.GetLabel "ApiClient.ReportTestStep.GetLabel") instead.

GetRelativeTime()[¶](#ApiClient.ReportTestStep.GetRelativeTime "Link to this definition")  
Returns the content of the ‘Test time [s]’ column.

Returns:  Content of the ‘Test time [s]’ column

Return type:  float

Deprecated since version 2020.4: Use [`GetRelativeTestTime()`](#ApiClient.ReportTestStep.GetRelativeTestTime "ApiClient.ReportTestStep.GetRelativeTestTime") instead.

## Entity[¶](#entity "Link to this heading")

*class* Entity[¶](#ApiClient.Entity "Link to this definition")  
An entity is a set of information visible in the report details of a certain reportitem. Each test step, analysis step or project step has specific report details, that are written to the report one after another.

Returned by

- [`ReportAnalysisEpisode.GetEntities`](#ApiClient.ReportAnalysisEpisode.GetEntities "ApiClient.ReportAnalysisEpisode.GetEntities")

- [`ReportAnalysisStep.GetEntities`](#ApiClient.ReportAnalysisStep.GetEntities "ApiClient.ReportAnalysisStep.GetEntities")

- [`ReportTestStep.GetEntities`](#ApiClient.ReportTestStep.GetEntities "ApiClient.ReportTestStep.GetEntities")

Subclasses

- [`ImageEntity`](#ApiClient.ImageEntity "ApiClient.ImageEntity")

- [`ImageExpectationEntity`](#ApiClient.ImageExpectationEntity "ApiClient.ImageExpectationEntity")

- [`TableEntity`](#ApiClient.TableEntity "ApiClient.TableEntity")

- [`TextEntity`](#ApiClient.TextEntity "ApiClient.TextEntity")

Clone()[¶](#ApiClient.Entity.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`Entity`](#ApiClient.Entity "ApiClient.Entity")

GetType()[¶](#ApiClient.Entity.GetType "Link to this definition")  
Returns:  The type name of the entity

Return type:  str

## ImageEntity[¶](#imageentity "Link to this heading")

*class* ImageEntity[¶](#ApiClient.ImageEntity "Link to this definition")  
Represents a single image enbedded within the report details of a report item.

Base class

[`Entity`](#ApiClient.Entity "ApiClient.Entity")

Clone()[¶](#ApiClient.ImageEntity.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`ImageEntity`](#ApiClient.ImageEntity "ApiClient.ImageEntity")

GetImage()[¶](#ApiClient.ImageEntity.GetImage "Link to this definition")  
Returns the image.

Returns:  the image

Return type:  [`ReportImage`](#ApiClient.ReportImage "ApiClient.ReportImage")

GetType()[¶](#ApiClient.ImageEntity.GetType "Link to this definition")  
Returns the type name of the entity.

Returns:  “Image”

Return type:  str

## ReportImage[¶](#reportimage "Link to this heading")

*class* ReportImage[¶](#ApiClient.ReportImage "Link to this definition")  
Returned by

- [`ImageEntity.GetImage`](#ApiClient.ImageEntity.GetImage "ApiClient.ImageEntity.GetImage")

- [`ImageExpectationEntity.GetActualImage`](#ApiClient.ImageExpectationEntity.GetActualImage "ApiClient.ImageExpectationEntity.GetActualImage")

- [`ImageExpectationEntity.GetExpectedImage`](#ApiClient.ImageExpectationEntity.GetExpectedImage "ApiClient.ImageExpectationEntity.GetExpectedImage")

Clone()[¶](#ApiClient.ReportImage.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`ReportImage`](#ApiClient.ReportImage "ApiClient.ReportImage")

GetRelativePath()[¶](#ApiClient.ReportImage.GetRelativePath "Link to this definition")  
Returns a relative path, pointing to the image file in the report directory. This path is relative to the \*.trf-file. If the image has not been saved relatively to the \*.trf-file but is stored within the \*.trf-file instead, this method returns an empty string.

Returns:  a relative path

Return type:  str

GetTitle()[¶](#ApiClient.ReportImage.GetTitle "Link to this definition")  
Returns the title of the image. (typically shown above the image)

Returns:  the image title

Return type:  str

## ImageExpectationEntity[¶](#imageexpectationentity "Link to this heading")

*class* ImageExpectationEntity[¶](#ApiClient.ImageExpectationEntity "Link to this definition")  
This type semantically clusters two images belonging to the same image expectation. This type is used for example when reporting the expected and resulting image of an read-image test step.

Base class

[`Entity`](#ApiClient.Entity "ApiClient.Entity")

Clone()[¶](#ApiClient.ImageExpectationEntity.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`ImageExpectationEntity`](#ApiClient.ImageExpectationEntity "ApiClient.ImageExpectationEntity")

GetActualImage()[¶](#ApiClient.ImageExpectationEntity.GetActualImage "Link to this definition")  
Returns the actual image (the resulting image)

Returns:  the actual image

Return type:  [`ReportImage`](#ApiClient.ReportImage "ApiClient.ReportImage")

GetExpectedImage()[¶](#ApiClient.ImageExpectationEntity.GetExpectedImage "Link to this definition")  
Returns the expected image

Returns:  the expected image

Return type:  [`ReportImage`](#ApiClient.ReportImage "ApiClient.ReportImage")

GetType()[¶](#ApiClient.ImageExpectationEntity.GetType "Link to this definition")  
Returns the type name of the entity.

Returns:  “ImageExpectation”

Return type:  str

## TableEntity[¶](#tableentity "Link to this heading")

*class* TableEntity[¶](#ApiClient.TableEntity "Link to this definition")  
Base class

[`Entity`](#ApiClient.Entity "ApiClient.Entity")

Clone()[¶](#ApiClient.TableEntity.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`TableEntity`](#ApiClient.TableEntity "ApiClient.TableEntity")

GetColumnCount()[¶](#ApiClient.TableEntity.GetColumnCount "Link to this definition")  
Returns the number of columns.

Returns:  the column count

Return type:  int

GetHeaders()[¶](#ApiClient.TableEntity.GetHeaders "Link to this definition")  
Returns a list representing the header row.

Returns:  the header row

Return type:  list[str]

GetRowCount()[¶](#ApiClient.TableEntity.GetRowCount "Link to this definition")  
Returns the number of rows. (not including the header row)

Returns:  the row count (not including the header row)

Return type:  int

GetType()[¶](#ApiClient.TableEntity.GetType "Link to this definition")  
Returns the type name of the entity.

Returns:  “Table”

Return type:  str

GetValue(*row*, *column*)[¶](#ApiClient.TableEntity.GetValue "Link to this definition")  
Returns the value in the given position. The position has to be specified 0 based. The header row does not effect the index, so GetValue(0, 0) will not return the first header cell, but the first actual cell underneath it.

Parameters:  - **row** (*int*) – the index of the row (0-based)

- **column** (*int*) – the index of the column (0-based)

Returns:  the value of the specified cell

Return type:  str

Raises:  
**ApiError** – If row or column values are invalid

GetValues()[¶](#ApiClient.TableEntity.GetValues "Link to this definition")  
Returns a list of lists, representing the values of the table. The header row will not be included.

Returns:  a list of lists representing the table value

Return type:  list[list[str]]

## TextEntity[¶](#textentity "Link to this heading")

*class* TextEntity[¶](#ApiClient.TextEntity "Link to this definition")  
Represents a single line of text within the report details of a report item.

Base class

[`Entity`](#ApiClient.Entity "ApiClient.Entity")

Clone()[¶](#ApiClient.TextEntity.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`TextEntity`](#ApiClient.TextEntity "ApiClient.TextEntity")

GetType()[¶](#ApiClient.TextEntity.GetType "Link to this definition")  
Returns the type name of the entity.

Returns:  “Text”

Return type:  str

GetValue()[¶](#ApiClient.TextEntity.GetValue "Link to this definition")  
Returns:  The string for the custom text

Return type:  str

## ReportAnalysisJob[¶](#reportanalysisjob "Link to this heading")

*class* ReportAnalysisJob[¶](#ApiClient.ReportAnalysisJob "Link to this definition")  
Returned by

- [`ReportPackage.GetTraceAnalysisJobs`](#ApiClient.ReportPackage.GetTraceAnalysisJobs "ApiClient.ReportPackage.GetTraceAnalysisJobs")

- [`ReportParameterSet.GetTraceAnalysisJobs`](#ApiClient.ReportParameterSet.GetTraceAnalysisJobs "ApiClient.ReportParameterSet.GetTraceAnalysisJobs")

Clone()[¶](#ApiClient.ReportAnalysisJob.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`ReportAnalysisJob`](#ApiClient.ReportAnalysisJob "ApiClient.ReportAnalysisJob")

ExportAnalysisJob(*path*)[¶](#ApiClient.ReportAnalysisJob.ExportAnalysisJob "Link to this definition")  
Writes deposited analysis job as an ajob-file for downstream analysis.

Parameters:  **path** (*str*) – Path where ajob-file is written to. Must include the file extension “.ajob”.

GetAllEpisodes()[¶](#ApiClient.ReportAnalysisJob.GetAllEpisodes "Link to this definition")  
Returns all episodes of the analysis job regardless of the position in the report.

Returns:  List of trace step results

Return type:  list[[`ReportAnalysisEpisode`](#ApiClient.ReportAnalysisEpisode "ApiClient.ReportAnalysisEpisode")]

GetDuration()[¶](#ApiClient.ReportAnalysisJob.GetDuration "Link to this definition")  
Returns the execution duration.

Returns:  Execution duration in seconds

Return type:  float

GetName()[¶](#ApiClient.ReportAnalysisJob.GetName "Link to this definition")  
Returns the name of the analysis job.

Returns:  name of the analysis job

Return type:  str

GetOriginalResult()[¶](#ApiClient.ReportAnalysisJob.GetOriginalResult "Link to this definition")  
Returns the result verdict of the analysis job.

Returns:  the result verdict

Return type:  str

GetRecordingInfos()[¶](#ApiClient.ReportAnalysisJob.GetRecordingInfos "Link to this definition")  
Returns an object encapsulating the recording info of the analysis job.

Returns:  The recording info table

Return type:  list[[`ReportRecordingInfo`](#ApiClient.ReportRecordingInfo "ApiClient.ReportRecordingInfo")]

GetResult()[¶](#ApiClient.ReportAnalysisJob.GetResult "Link to this definition")  
Returns the result verdict of the analysis job.

Returns:  the result verdict

Return type:  str

GetStimulationPackage()[¶](#ApiClient.ReportAnalysisJob.GetStimulationPackage "Link to this definition")  
This call is only valid for analysis jobs derived from analysis packages and returns the invoked stimulation package. For parameterized stimulations, the resulting package object characterizes a particular parameter set.

Returns:  stimulation package

Return type:  [`ReportPackage`](#ApiClient.ReportPackage "ApiClient.ReportPackage")

GetTraceAnalysis()[¶](#ApiClient.ReportAnalysisJob.GetTraceAnalysis "Link to this definition")  
Returns the root element ‘trace analysis’ (report item) of the analysis job.

Returns:  Root element of job or None if trace analysis was not executed.

Return type:  [`ReportAnalysisStep`](#ApiClient.ReportAnalysisStep "ApiClient.ReportAnalysisStep")

GetTraceSteps(*recursive=False*)[¶](#ApiClient.ReportAnalysisJob.GetTraceSteps "Link to this definition")  
Returns direct/all children trace steps of the trace analysis.

Parameters:  **recursive** (*boolean*) – Defines whether children of children are included, defaults to False.

Returns:  List of trace step results. If the analysis has not been executed, an empty list will be returned.

Return type:  list[[`ReportAnalysisStep`](#ApiClient.ReportAnalysisStep "ApiClient.ReportAnalysisStep")]

IsDownstream()[¶](#ApiClient.ReportAnalysisJob.IsDownstream "Link to this definition")  
Returns whether the analysis job was created as a downstream analysis. If so, it was not processed within the project execution. Instead, is has to be executed afterwards.

Note:  
A downstream analysis has the default result NONE instead of INCONCLUSIVE.

Returns:  True, if the analysis job was created as downstream analysis.

Return type:  bool

## ReportAnalysisEpisode[¶](#reportanalysisepisode "Link to this heading")

*class* ReportAnalysisEpisode[¶](#ApiClient.ReportAnalysisEpisode "Link to this definition")  
Base class

[`ReportAnalysisStep`](#ApiClient.ReportAnalysisStep "ApiClient.ReportAnalysisStep")

Returned by

- [`ReportAnalysisJob.GetAllEpisodes`](#ApiClient.ReportAnalysisJob.GetAllEpisodes "ApiClient.ReportAnalysisJob.GetAllEpisodes")

AddRevalComment(*author*, *comment*, *revaluation=None*)[¶](#ApiClient.ReportAnalysisEpisode.AddRevalComment "Link to this definition")  
Add a revaluation comment to the test step.

Parameters:  - **author** (*str*) – author of the comment

- **comment** (*str*) – text of the comment. Must be at least 10 characters

- **revaluation** (*str*) – “NONE”, “SUCCESS”, “INCONCLUSIVE”, “FAILED” or “ERROR”; None to just add a comment without changing the result

Clone()[¶](#ApiClient.ReportAnalysisEpisode.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`ReportAnalysisEpisode`](#ApiClient.ReportAnalysisEpisode "ApiClient.ReportAnalysisEpisode")

GetAbortCode()[¶](#ApiClient.ReportAnalysisEpisode.GetAbortCode "Link to this definition")  
Returns the abort code of the report item.

Returns:  Abort code

Return type:  str

GetAbortComment()[¶](#ApiClient.ReportAnalysisEpisode.GetAbortComment "Link to this definition")  
Returns the abort comment of the report item.

Returns:  Abort comment

Return type:  str

GetDescription()[¶](#ApiClient.ReportAnalysisEpisode.GetDescription "Link to this definition")  
Returns the content of the ‘Description’ column.

Returns:  Content of the ‘Description’ column

Return type:  str

GetDuration()[¶](#ApiClient.ReportAnalysisEpisode.GetDuration "Link to this definition")  
Returns the execution duration.

Returns:  Excecution duration in seconds

Return type:  float

GetEntities()[¶](#ApiClient.ReportAnalysisEpisode.GetEntities "Link to this definition")  
Returns a list of all entities.

Returns:  a list of all entity objects

Return type:  list[[`Entity`](#ApiClient.Entity "ApiClient.Entity")]

GetErrorMessage()[¶](#ApiClient.ReportAnalysisEpisode.GetErrorMessage "Link to this definition")  
Returns the episode’s error message.

Returns:  The error message if existing, else an empty string

Return type:  str

GetId()[¶](#ApiClient.ReportAnalysisEpisode.GetId "Link to this definition")  
Returns the Id of the report item.

Returns:  Id of the report item

Return type:  int

GetLabel()[¶](#ApiClient.ReportAnalysisEpisode.GetLabel "Link to this definition")  
Returns the content of the ‘Activity/Name’ column for test steps. Returns the content of the ‘Name’ column for trace steps.

Returns:  Content of the ‘Activity/Name’ column for test steps and content of the ‘Name’ column for trace steps

Return type:  str

GetNestingLevel()[¶](#ApiClient.ReportAnalysisEpisode.GetNestingLevel "Link to this definition")  
Returns the nesting depth.

Returns:  Nesting depth

Return type:  int

GetOriginalResult()[¶](#ApiClient.ReportAnalysisEpisode.GetOriginalResult "Link to this definition")  
Returns the content of the ‘Original evaluation’ column.

Returns:  Content of the ‘Original evaluation’ column

Return type:  str

GetParameter()[¶](#ApiClient.ReportAnalysisEpisode.GetParameter "Link to this definition")  
Returns the content of the ‘Parameter’ column.

Returns:  Content of the ‘Parameter’ column

Return type:  str

GetParentId()[¶](#ApiClient.ReportAnalysisEpisode.GetParentId "Link to this definition")  
Returns the Id of the parent report item.

Returns:  Id of the parent report item

Return type:  int

GetPosition()[¶](#ApiClient.ReportAnalysisEpisode.GetPosition "Link to this definition")  
Returns the position of the step within the test case / trace analysis. Example 1: “3” is returned for the step which is at position 3 in the top level Package. Example 2: “5.13” is returned for the 13th step of the subpackage which is at position 5 in the top level Package.

Returns:  position within the test case / trace analysis

Return type:  str

GetResult()[¶](#ApiClient.ReportAnalysisEpisode.GetResult "Link to this definition")  
Returns the content of the ‘Evaluation’ column.

Returns:  Content of the ‘Evaluation’ column

Return type:  str

GetResultText()[¶](#ApiClient.ReportAnalysisEpisode.GetResultText "Link to this definition")  
Returns text illustrated in the trace step’s report details below ‘result’.

Returns:  The result text if existing, else an empty string

Return type:  str

GetRevalComments()[¶](#ApiClient.ReportAnalysisEpisode.GetRevalComments "Link to this definition")  
Returns all revaluation comments of the test step.

Returns:  List of revaluation comments

Return type:  list[[`RevaluationComment`](#ApiClient.RevaluationComment "ApiClient.RevaluationComment")]

GetTags()[¶](#ApiClient.ReportAnalysisEpisode.GetTags "Link to this definition")  
Returns all tags associated with this report entry.

Returns:  Tags

Return type:  list[str]

GetTextEntities()[¶](#ApiClient.ReportAnalysisEpisode.GetTextEntities "Link to this definition")  
Returns all text entities associated with this report entry.

Returns:  text entities

Return type:  list[list[str]]

GetTraceSteps(*recursive=False*)[¶](#ApiClient.ReportAnalysisEpisode.GetTraceSteps "Link to this definition")  
Returns direct/all children trace steps of this step. If the trace step is no container an empty list will be returned.

Parameters:  **recursive** (*boolean*) – Defines whether children of children are included, defaults to False.

Returns:  List of trace steps

Return type:  list[[`ReportAnalysisStep`](#ApiClient.ReportAnalysisStep "ApiClient.ReportAnalysisStep")]

HasTag(*tagName*)[¶](#ApiClient.ReportAnalysisEpisode.HasTag "Link to this definition")  
Parameters:  **tagName** (*str*) – The tag to check for

Returns:  Whether this report item has set the specified tag

Return type:  bool

IsTemplateBasedTraceStep()[¶](#ApiClient.ReportAnalysisEpisode.IsTemplateBasedTraceStep "Link to this definition")  
Returns whether the trace step is based on a template.

Returns:  True if trace step is based on a template

Return type:  bool

GetActivity()[¶](#ApiClient.ReportAnalysisEpisode.GetActivity "Link to this definition")  
Returns the activity part of the content of the ‘Activity/Name’ column for test steps. Returns the content of the ‘Name’ column for trace steps.

Returns:  Activity part of the ‘Activity/Name’ column for test steps and content of ‘Name’ column for trace steps

Return type:  str

Deprecated since version 2020.2: Use [`GetLabel()`](#ApiClient.ReportAnalysisEpisode.GetLabel "ApiClient.ReportAnalysisEpisode.GetLabel") instead.

GetName()[¶](#ApiClient.ReportAnalysisEpisode.GetName "Link to this definition")  
Returns the name part of the content of the ‘Activity/Name’ column for test steps.

Returns:  Name part of the ‘Activity/Name’ column

Return type:  str

Deprecated since version 2020.2: Use [`GetLabel()`](#ApiClient.ReportAnalysisEpisode.GetLabel "ApiClient.ReportAnalysisEpisode.GetLabel") instead.

## ReportAnalysisStep[¶](#reportanalysisstep "Link to this heading")

*class* ReportAnalysisStep[¶](#ApiClient.ReportAnalysisStep "Link to this definition")  
Returned by

- [`ReportAnalysisEpisode.GetTraceSteps`](#ApiClient.ReportAnalysisEpisode.GetTraceSteps "ApiClient.ReportAnalysisEpisode.GetTraceSteps")

- [`ReportAnalysisJob.GetTraceAnalysis`](#ApiClient.ReportAnalysisJob.GetTraceAnalysis "ApiClient.ReportAnalysisJob.GetTraceAnalysis")

- [`ReportAnalysisJob.GetTraceSteps`](#ApiClient.ReportAnalysisJob.GetTraceSteps "ApiClient.ReportAnalysisJob.GetTraceSteps")

- [`ReportAnalysisStep.GetTraceSteps`](#ApiClient.ReportAnalysisStep.GetTraceSteps "ApiClient.ReportAnalysisStep.GetTraceSteps")

Subclasses

- [`ReportAnalysisEpisode`](#ApiClient.ReportAnalysisEpisode "ApiClient.ReportAnalysisEpisode")

AddRevalComment(*author*, *comment*, *revaluation=None*)[¶](#ApiClient.ReportAnalysisStep.AddRevalComment "Link to this definition")  
Add a revaluation comment to the test step.

Parameters:  - **author** (*str*) – author of the comment

- **comment** (*str*) – text of the comment. Must be at least 10 characters

- **revaluation** (*str*) – “NONE”, “SUCCESS”, “INCONCLUSIVE”, “FAILED” or “ERROR”; None to just add a comment without changing the result

Clone()[¶](#ApiClient.ReportAnalysisStep.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`ReportAnalysisStep`](#ApiClient.ReportAnalysisStep "ApiClient.ReportAnalysisStep")

GetAbortCode()[¶](#ApiClient.ReportAnalysisStep.GetAbortCode "Link to this definition")  
Returns the abort code of the report item.

Returns:  Abort code

Return type:  str

GetAbortComment()[¶](#ApiClient.ReportAnalysisStep.GetAbortComment "Link to this definition")  
Returns the abort comment of the report item.

Returns:  Abort comment

Return type:  str

GetDescription()[¶](#ApiClient.ReportAnalysisStep.GetDescription "Link to this definition")  
Returns the content of the ‘Description’ column.

Returns:  Content of the ‘Description’ column

Return type:  str

GetEntities()[¶](#ApiClient.ReportAnalysisStep.GetEntities "Link to this definition")  
Returns a list of all entities.

Returns:  a list of all entity objects

Return type:  list[[`Entity`](#ApiClient.Entity "ApiClient.Entity")]

GetId()[¶](#ApiClient.ReportAnalysisStep.GetId "Link to this definition")  
Returns the Id of the report item.

Returns:  Id of the report item

Return type:  int

GetLabel()[¶](#ApiClient.ReportAnalysisStep.GetLabel "Link to this definition")  
Returns the content of the ‘Activity/Name’ column for test steps. Returns the content of the ‘Name’ column for trace steps.

Returns:  Content of the ‘Activity/Name’ column for test steps and content of the ‘Name’ column for trace steps

Return type:  str

GetNestingLevel()[¶](#ApiClient.ReportAnalysisStep.GetNestingLevel "Link to this definition")  
Returns the nesting depth.

Returns:  Nesting depth

Return type:  int

GetOriginalResult()[¶](#ApiClient.ReportAnalysisStep.GetOriginalResult "Link to this definition")  
Returns the content of the ‘Original evaluation’ column.

Returns:  Content of the ‘Original evaluation’ column

Return type:  str

GetParameter()[¶](#ApiClient.ReportAnalysisStep.GetParameter "Link to this definition")  
Returns the content of the ‘Parameter’ column.

Returns:  Content of the ‘Parameter’ column

Return type:  str

GetParentId()[¶](#ApiClient.ReportAnalysisStep.GetParentId "Link to this definition")  
Returns the Id of the parent report item.

Returns:  Id of the parent report item

Return type:  int

GetPosition()[¶](#ApiClient.ReportAnalysisStep.GetPosition "Link to this definition")  
Returns the position of the step within the test case / trace analysis. Example 1: “3” is returned for the step which is at position 3 in the top level Package. Example 2: “5.13” is returned for the 13th step of the subpackage which is at position 5 in the top level Package.

Returns:  position within the test case / trace analysis

Return type:  str

GetResult()[¶](#ApiClient.ReportAnalysisStep.GetResult "Link to this definition")  
Returns the content of the ‘Evaluation’ column.

Returns:  Content of the ‘Evaluation’ column

Return type:  str

GetResultText()[¶](#ApiClient.ReportAnalysisStep.GetResultText "Link to this definition")  
Returns text illustrated in the trace step’s report details below ‘result’.

Returns:  The result text if existing, else an empty string

Return type:  str

GetRevalComments()[¶](#ApiClient.ReportAnalysisStep.GetRevalComments "Link to this definition")  
Returns all revaluation comments of the test step.

Returns:  List of revaluation comments

Return type:  list[[`RevaluationComment`](#ApiClient.RevaluationComment "ApiClient.RevaluationComment")]

GetTags()[¶](#ApiClient.ReportAnalysisStep.GetTags "Link to this definition")  
Returns all tags associated with this report entry.

Returns:  Tags

Return type:  list[str]

GetTextEntities()[¶](#ApiClient.ReportAnalysisStep.GetTextEntities "Link to this definition")  
Returns all text entities associated with this report entry.

Returns:  text entities

Return type:  list[list[str]]

GetTraceSteps(*recursive=False*)[¶](#ApiClient.ReportAnalysisStep.GetTraceSteps "Link to this definition")  
Returns direct/all children trace steps of this step. If the trace step is no container an empty list will be returned.

Parameters:  **recursive** (*boolean*) – Defines whether children of children are included, defaults to False.

Returns:  List of trace steps

Return type:  list[[`ReportAnalysisStep`](#ApiClient.ReportAnalysisStep "ApiClient.ReportAnalysisStep")]

HasTag(*tagName*)[¶](#ApiClient.ReportAnalysisStep.HasTag "Link to this definition")  
Parameters:  **tagName** (*str*) – The tag to check for

Returns:  Whether this report item has set the specified tag

Return type:  bool

IsTemplateBasedTraceStep()[¶](#ApiClient.ReportAnalysisStep.IsTemplateBasedTraceStep "Link to this definition")  
Returns whether the trace step is based on a template.

Returns:  True if trace step is based on a template

Return type:  bool

GetActivity()[¶](#ApiClient.ReportAnalysisStep.GetActivity "Link to this definition")  
Returns the activity part of the content of the ‘Activity/Name’ column for test steps. Returns the content of the ‘Name’ column for trace steps.

Returns:  Activity part of the ‘Activity/Name’ column for test steps and content of ‘Name’ column for trace steps

Return type:  str

Deprecated since version 2020.2: Use [`GetLabel()`](#ApiClient.ReportAnalysisStep.GetLabel "ApiClient.ReportAnalysisStep.GetLabel") instead.

GetName()[¶](#ApiClient.ReportAnalysisStep.GetName "Link to this definition")  
Returns the name part of the content of the ‘Activity/Name’ column for test steps.

Returns:  Name part of the ‘Activity/Name’ column

Return type:  str

Deprecated since version 2020.2: Use [`GetLabel()`](#ApiClient.ReportAnalysisStep.GetLabel "ApiClient.ReportAnalysisStep.GetLabel") instead.

## ReportRecordingInfo[¶](#reportrecordinginfo "Link to this heading")

*class* ReportRecordingInfo[¶](#ApiClient.ReportRecordingInfo "Link to this definition")  
Returned by

- [`ReportAnalysisJob.GetRecordingInfos`](#ApiClient.ReportAnalysisJob.GetRecordingInfos "ApiClient.ReportAnalysisJob.GetRecordingInfos")

Clone()[¶](#ApiClient.ReportRecordingInfo.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`ReportRecordingInfo`](#ApiClient.ReportRecordingInfo "ApiClient.ReportRecordingInfo")

GetRecording()[¶](#ApiClient.ReportRecordingInfo.GetRecording "Link to this definition")  
Returns the recording that is referenced by the recording info.

Returns:  The recording object

Return type:  [`ReportRecording`](#ApiClient.ReportRecording "ApiClient.ReportRecording")

GetStartTime()[¶](#ApiClient.ReportRecordingInfo.GetStartTime "Link to this definition")  
Returns the first time stamp read in from the recording.

Returns:  First time stamp read in from the recording. Returns None if no start time was set.

Return type:  float

GetStopTime()[¶](#ApiClient.ReportRecordingInfo.GetStopTime "Link to this definition")  
Returns the last time stamp read in from the recording.

Returns:  Last time stamp read in from the recording. Returns None if no stop time was set.

Return type:  float

GetSyncDeltaT()[¶](#ApiClient.ReportRecordingInfo.GetSyncDeltaT "Link to this definition")  
Returns the time offset set by the synchronization of traces.

Returns:  The deltaT

Return type:  float

## ReportParameterSet[¶](#reportparameterset "Link to this heading")

*class* ReportParameterSet[¶](#ApiClient.ReportParameterSet "Link to this definition")  
Base classes

- [`ReportProjectElement`](#ApiClient.ReportProjectElement "ApiClient.ReportProjectElement")

- [`ReportPackage`](#ApiClient.ReportPackage "ApiClient.ReportPackage")

Clone()[¶](#ApiClient.ReportParameterSet.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`ReportParameterSet`](#ApiClient.ReportParameterSet "ApiClient.ReportParameterSet")

GetAbortCode()[¶](#ApiClient.ReportParameterSet.GetAbortCode "Link to this definition")  
Returns the abort code of the package or an empty string if it was not aborted.

Returns:  Abort code of the package

Return type:  str

GetAbortComment()[¶](#ApiClient.ReportParameterSet.GetAbortComment "Link to this definition")  
Returns the abort comment of the package or an empty string if it was not aborted.

Returns:  Abort comment of the package

Return type:  str

GetArtifacts()[¶](#ApiClient.ReportParameterSet.GetArtifacts "Link to this definition")  
Returns all referenced artifacts.

Returns:  A list of all referenced artifacts.

Return type:  list[[`Artifact`](#ApiClient.Artifact "ApiClient.Artifact")]

GetAttributes()[¶](#ApiClient.ReportParameterSet.GetAttributes "Link to this definition")  
Returns all package attributes

Returns:  Dictionary of package attributes

Return type:  dict[str, str]

GetComment()[¶](#ApiClient.ReportParameterSet.GetComment "Link to this definition")  
Returns the comment of the package.

Returns:  Comment of the package

Return type:  str

GetDuration()[¶](#ApiClient.ReportParameterSet.GetDuration "Link to this definition")  
Returns the duration of the test execution.

Returns:  Execution duration in seconds

Return type:  float

GetElementName()[¶](#ApiClient.ReportParameterSet.GetElementName "Link to this definition")  
Returns the project element name.

Returns:  Name of the project element

Return type:  str

GetExecutionTime()[¶](#ApiClient.ReportParameterSet.GetExecutionTime "Link to this definition")  
Returns the test execution date and time as string representation.

Returns:  Execution time

Return type:  str

GetFilename()[¶](#ApiClient.ReportParameterSet.GetFilename "Link to this definition")  
Returns the filename of the package which corresponds to the column ‘Activity’ in the project summary (without file extension).

Returns:  Name of the package file

Return type:  str

GetGlobalConstantsDefinedOnStart()[¶](#ApiClient.ReportParameterSet.GetGlobalConstantsDefinedOnStart "Link to this definition")  
Gets the values that the global constants had at the start of the Package execution.

Returns:  list of global constants

Return type:  list[[`GlobalConstant`](#ApiClient.GlobalConstant "ApiClient.GlobalConstant")]

GetName()[¶](#ApiClient.ReportParameterSet.GetName "Link to this definition")  
Returns the package name.

Returns:  Package name

Return type:  str

GetOriginalResult()[¶](#ApiClient.ReportParameterSet.GetOriginalResult "Link to this definition")  
Returns the original total test result.

Returns:  Original total test result

Return type:  str

GetParameterDescription(*name*)[¶](#ApiClient.ReportParameterSet.GetParameterDescription "Link to this definition")  
Returns the description of the parameter specified by the given name.

Parameters:  **name** (*str*) – Name of the parameter

Returns:  Description of the parameter

Return type:  str

GetParameterInitialValue(*name*)[¶](#ApiClient.ReportParameterSet.GetParameterInitialValue "Link to this definition")  
Returns the initial value of the parameter specified by the given name.

Parameters:  **name** (*str*) – Name of the parameter

Returns:  Initial value of the parameter

Return type:  str

GetParameterNames()[¶](#ApiClient.ReportParameterSet.GetParameterNames "Link to this definition")  
Returns a list of parameter names.

Returns:  List of names

Return type:  list[str]

GetParameterOrigin(*name*)[¶](#ApiClient.ReportParameterSet.GetParameterOrigin "Link to this definition")  
Returns the origin of the parameter specified by the given name.

Parameters:  **name** (*str*) – Name of the parameter

Returns:  Origin of the parameter

Return type:  str

GetParameterValue(*name*)[¶](#ApiClient.ReportParameterSet.GetParameterValue "Link to this definition")  
Returns the latest value of the parameter specified by the given name.

Parameters:  **name** (*str*) – Name of the parameter

Returns:  Value of the parameter

Return type:  str

GetProjectElements()[¶](#ApiClient.ReportParameterSet.GetProjectElements "Link to this definition")  
Returns a list of all direct project child elements.

Returns:  List of direct project child elements

Return type:  list[[`ReportProjectElement`](#ApiClient.ReportProjectElement "ApiClient.ReportProjectElement")]

GetRecordings()[¶](#ApiClient.ReportParameterSet.GetRecordings "Link to this definition")  
Returns the recordings created or used by the package.

Returns:  The recording objects

Return type:  list[[`ReportRecording`](#ApiClient.ReportRecording "ApiClient.ReportRecording")]

GetReportItemId()[¶](#ApiClient.ReportParameterSet.GetReportItemId "Link to this definition")  
Returns the ReportItem Id of the project element.

Returns:  ReportItem Id

Return type:  int

GetResult()[¶](#ApiClient.ReportParameterSet.GetResult "Link to this definition")  
Returns the package result.

Returns:  Package result

Return type:  str

GetReturnDescription(*name*)[¶](#ApiClient.ReportParameterSet.GetReturnDescription "Link to this definition")  
Returns the description of the return specified by the given name.

Parameters:  **name** (*str*) – Name of the return

Returns:  Description of the return

Return type:  str

GetReturnInitialValue(*name*)[¶](#ApiClient.ReportParameterSet.GetReturnInitialValue "Link to this definition")  
Returns the initial value of the return specified by the given name.

Parameters:  **name** (*str*) – Name of the return

Returns:  Initial value of the return

Return type:  str

GetReturnNames()[¶](#ApiClient.ReportParameterSet.GetReturnNames "Link to this definition")  
Returns a list of return names.

Returns:  List of names

Return type:  list[str]

GetReturnValue(*name*)[¶](#ApiClient.ReportParameterSet.GetReturnValue "Link to this definition")  
Returns the latest value of the return specified by the given name.

Parameters:  **name** (*str*) – Name of the return

Returns:  Value of the return

Return type:  str

GetRevalComments()[¶](#ApiClient.ReportParameterSet.GetRevalComments "Link to this definition")  
Returns all revaluation comments of the package.

Returns:  List of revaluation comments

Return type:  list[[`RevaluationComment`](#ApiClient.RevaluationComment "ApiClient.RevaluationComment")]

GetStimulationPackage(*returnParamSets=True*)[¶](#ApiClient.ReportParameterSet.GetStimulationPackage "Link to this definition")  
This call is only valid for analysis packages and returns the stimulation package.

Note:  
For older reports (before 2022.2) this method may return None if no trace analysis was executed.

Parameters:  **returnParamSets** (*bool*) –

Specifies, how to deal with stimulation parameter sets. If True, the parameter set that has been used to stimulate the execution of the analysis package is returned.

If False, the stimulation package itself is returned, which is of type [`ReportParameterizedPackage`](#ApiClient.ReportParameterizedPackage "ApiClient.ReportParameterizedPackage") for parameterized stimulations.

Returns:  The stimulation package. The default return value will be of type [`ReportPackage`](#ApiClient.ReportPackage "ApiClient.ReportPackage"). If returnParamSets is False, it is possibly also of type [`ReportParameterizedPackage`](#ApiClient.ReportParameterizedPackage "ApiClient.ReportParameterizedPackage").

Return type:  [`ReportProjectElement`](#ApiClient.ReportProjectElement "ApiClient.ReportProjectElement")

GetTestCase()[¶](#ApiClient.ReportParameterSet.GetTestCase "Link to this definition")  
Returns the test case of the package.

Returns:  Test case of the package

Return type:  [`ReportTestCase`](#ApiClient.ReportTestCase "ApiClient.ReportTestCase")

GetTestManagementId()[¶](#ApiClient.ReportParameterSet.GetTestManagementId "Link to this definition")  
Returns the corresponding testmanagement ID.

Returns:  Testmanagement ID or an empty string if no ID defined.

Return type:  str

GetTestScriptId()[¶](#ApiClient.ReportParameterSet.GetTestScriptId "Link to this definition")  
Returns the corresponding testscript ID.

Returns:  Testscript ID or an empty string if no ID defined.

Return type:  str

GetTraceAnalysisJobs()[¶](#ApiClient.ReportParameterSet.GetTraceAnalysisJobs "Link to this definition")  
Returns a list of the analysis jobs of the package.

Returns:  List of analysis jobs

Return type:  list[[`ReportAnalysisJob`](#ApiClient.ReportAnalysisJob "ApiClient.ReportAnalysisJob")]

GetType()[¶](#ApiClient.ReportParameterSet.GetType "Link to this definition")  
Returns the type (class name) of the project element, e.g.  
- “ReportConfigurationChange”

- “ReportFolderElement”

- “ReportPackage”

- “ReportParameterizedPackage”

- “ReportParameterSet”

- “ReportProjectElement”

- “ReportProject”

Returns:  Type (class name) of the test step

Return type:  str

GetUserDefinedData()[¶](#ApiClient.ReportParameterSet.GetUserDefinedData "Link to this definition")  
Returns the user defined report information.

Returns:  Name and value of the user defined information.

Return type:  dict[str, str]

IsAnalysisPackage()[¶](#ApiClient.ReportParameterSet.IsAnalysisPackage "Link to this definition")  
Returns, whether this package is an analysis package.

Returns:  True if this package is an analysis package

Return type:  bool

IsSkipped()[¶](#ApiClient.ReportParameterSet.IsSkipped "Link to this definition")  
Returns True if the package was skipped.

Returns:  True if skipped

Return type:  bool

IsStimulationPackage()[¶](#ApiClient.ReportParameterSet.IsStimulationPackage "Link to this definition")  
Returns, whether this package is a stimulation package.

Returns:  True if this package is a stimulation package

Return type:  bool

## ReportParameterizedPackage[¶](#reportparameterizedpackage "Link to this heading")

*class* ReportParameterizedPackage[¶](#ApiClient.ReportParameterizedPackage "Link to this definition")  
Base class

[`ReportProjectElement`](#ApiClient.ReportProjectElement "ApiClient.ReportProjectElement")

Clone()[¶](#ApiClient.ReportParameterizedPackage.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`ReportParameterizedPackage`](#ApiClient.ReportParameterizedPackage "ApiClient.ReportParameterizedPackage")

GetComment()[¶](#ApiClient.ReportParameterizedPackage.GetComment "Link to this definition")  
Returns the comment of the project element.

Returns:  Project element comment

Return type:  str

GetElementName()[¶](#ApiClient.ReportParameterizedPackage.GetElementName "Link to this definition")  
Returns the name of the project element.

Returns:  Element name

Return type:  str

GetProjectElements()[¶](#ApiClient.ReportParameterizedPackage.GetProjectElements "Link to this definition")  
Returns a list of all direct project child elements.

Returns:  List of direct project child elements

Return type:  list[[`ReportProjectElement`](#ApiClient.ReportProjectElement "ApiClient.ReportProjectElement")]

GetReportItemId()[¶](#ApiClient.ReportParameterizedPackage.GetReportItemId "Link to this definition")  
Returns the ReportItem Id of the project element.

Returns:  ReportItem Id

Return type:  int

GetResult()[¶](#ApiClient.ReportParameterizedPackage.GetResult "Link to this definition")  
Returns the result of the project element.

Returns:  Project element result

Return type:  str

GetType()[¶](#ApiClient.ReportParameterizedPackage.GetType "Link to this definition")  
Returns the type (class name) of the project element, e.g.  
- “ReportConfigurationChange”

- “ReportFolderElement”

- “ReportPackage”

- “ReportParameterizedPackage”

- “ReportParameterSet”

- “ReportProjectElement”

- “ReportProject”

Returns:  Type (class name) of the test step

Return type:  str

## ReportConfigurationChange[¶](#reportconfigurationchange "Link to this heading")

*class* ReportConfigurationChange[¶](#ApiClient.ReportConfigurationChange "Link to this definition")  
Base class

[`ReportProjectElement`](#ApiClient.ReportProjectElement "ApiClient.ReportProjectElement")

Clone()[¶](#ApiClient.ReportConfigurationChange.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`ReportConfigurationChange`](#ApiClient.ReportConfigurationChange "ApiClient.ReportConfigurationChange")

GetComment()[¶](#ApiClient.ReportConfigurationChange.GetComment "Link to this definition")  
Returns the comment of the project element.

Returns:  Project element comment

Return type:  str

GetElementName()[¶](#ApiClient.ReportConfigurationChange.GetElementName "Link to this definition")  
Returns the name of the project element.

Returns:  Element name

Return type:  str

GetProjectElements()[¶](#ApiClient.ReportConfigurationChange.GetProjectElements "Link to this definition")  
Returns a list of all direct project child elements.

Returns:  List of direct project child elements

Return type:  list[[`ReportProjectElement`](#ApiClient.ReportProjectElement "ApiClient.ReportProjectElement")]

GetReportItemId()[¶](#ApiClient.ReportConfigurationChange.GetReportItemId "Link to this definition")  
Returns the ReportItem Id of the project element.

Returns:  ReportItem Id

Return type:  int

GetResult()[¶](#ApiClient.ReportConfigurationChange.GetResult "Link to this definition")  
Returns the result of the project element.

Returns:  Project element result

Return type:  str

GetType()[¶](#ApiClient.ReportConfigurationChange.GetType "Link to this definition")  
Returns the type (class name) of the project element, e.g.  
- “ReportConfigurationChange”

- “ReportFolderElement”

- “ReportPackage”

- “ReportParameterizedPackage”

- “ReportParameterSet”

- “ReportProjectElement”

- “ReportProject”

Returns:  Type (class name) of the test step

Return type:  str

## ReportFolderElement[¶](#reportfolderelement "Link to this heading")

*class* ReportFolderElement[¶](#ApiClient.ReportFolderElement "Link to this definition")  
Base class

[`ReportProjectElement`](#ApiClient.ReportProjectElement "ApiClient.ReportProjectElement")

Clone()[¶](#ApiClient.ReportFolderElement.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`ReportFolderElement`](#ApiClient.ReportFolderElement "ApiClient.ReportFolderElement")

GetComment()[¶](#ApiClient.ReportFolderElement.GetComment "Link to this definition")  
Returns the comment of the project element.

Returns:  Project element comment

Return type:  str

GetElementName()[¶](#ApiClient.ReportFolderElement.GetElementName "Link to this definition")  
Returns the name of the project element.

Returns:  Element name

Return type:  str

GetProjectElements()[¶](#ApiClient.ReportFolderElement.GetProjectElements "Link to this definition")  
Returns a list of all direct project child elements.

Returns:  List of direct project child elements

Return type:  list[[`ReportProjectElement`](#ApiClient.ReportProjectElement "ApiClient.ReportProjectElement")]

GetReportItemId()[¶](#ApiClient.ReportFolderElement.GetReportItemId "Link to this definition")  
Returns the ReportItem Id of the project element.

Returns:  ReportItem Id

Return type:  int

GetResult()[¶](#ApiClient.ReportFolderElement.GetResult "Link to this definition")  
Returns the result of the project element.

Returns:  Project element result

Return type:  str

GetType()[¶](#ApiClient.ReportFolderElement.GetType "Link to this definition")  
Returns the type (class name) of the project element, e.g.  
- “ReportConfigurationChange”

- “ReportFolderElement”

- “ReportPackage”

- “ReportParameterizedPackage”

- “ReportParameterSet”

- “ReportProjectElement”

- “ReportProject”

Returns:  Type (class name) of the test step

Return type:  str
