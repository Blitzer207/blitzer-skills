# COM-API[¶](#com-api "Link to this heading")

This module contains the types for the COM-Application-Server. The main class is [`COMApplication`](#tts.core.api.comApi.Comserver_ET.COMApplication_ET "tts.core.api.comApi.Comserver_ET.COMApplication_ET") which is instantiated with Prog-ID **‘ecu.test.Application’**.

Sample usage:  
    >>> import win32com.client
    >>> ecutest = win32com.client.Dispatch('ecu.test.Application')
    >>> ecutest.StartTimeout
    90
    >>> ecutest.StartTimeout = 120  # Change timeout for application start
    >>> testEnv = ecutest.Start()
    >>> pkg = ecutest.OpenPackage("c:\\test.pkg")
    >>> pkg is not None
    True
    >>> execInfo = testEnv.ExecutePackage("c:\\test.pkg")
    >>> while execInfo.GetState() == "RUNNING":
    ...     time.sleep(0.1)
    >>> execInfo.GetPackageResult()
    'SUCCESS'
    >>> execInfo.GetReportDb()
    '<path>\test.trf'
    >>> pkg = ecutest.Packages.Item(0)
    >>> pkg.Name
    'test'
    >>> execInfo.TestReport.Count
    26
    >>> execInfo.TestReport.Result(3)
    'NONE'
    >>> execInfo.TestReport.Name(3)
    'Comment'
    >>> execInfo.TestReport.Activity(3)
    'UTILITY'

Warning

Based on the limitations of the Windows COM interface in contrast to the usual Python notation the usage of keywords is not applicable. Keywords documented here can only be used indirectly to pass default values by not assigning the respective optional parameter.

A direct call of e.g. `Exit(timeout=60)` will raise an error. Instead, the call must either be made without the keyword to use the default value of 60: `Exit()` or the parameter must be overridden on the respective position: `Exit(45)`.

## COMApplication_ET[¶](#comapplication-et "Link to this heading")

*class* COMApplication_ET[¶](#tts.core.api.comApi.Comserver_ET.COMApplication_ET "Link to this definition")  
This is the main object returned by the `Dispatch()` call.

Caches[¶](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.Caches "Link to this definition")  
Returns the cache module.

Returns:  A [`COMCaches`](#tts.core.api.comApi.Comserver.COMCaches "tts.core.api.comApi.Comserver.COMCaches") object.

Return type:  [`COMCaches`](#tts.core.api.comApi.Comserver.COMCaches "tts.core.api.comApi.Comserver.COMCaches")

Packages[¶](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.Packages "Link to this definition")  
Returns a container object which gives access to all opened packages in COM-Application.

Returns:  The container object to access all opened packages.

Return type:  [`COMPackages`](#tts.core.api.comApi.Comserver.COMPackages "tts.core.api.comApi.Comserver.COMPackages")

Projects[¶](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.Projects "Link to this definition")  
Returns a container object which gives access to all opened projects in COM-Application.

Returns:  The container object to access all opened packages.

Return type:  [`COMProjects`](#tts.core.api.comApi.Comserver.COMProjects "tts.core.api.comApi.Comserver.COMProjects")

StartTimeout[¶](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.StartTimeout "Link to this definition")  
Property to get or set the timeout for the application start in seconds. Defaults to 90s.

Type:  int|float

ClosePackage(*filename*)[¶](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.ClosePackage "Link to this definition")  
Closes a Package (testcase).

Parameters:  **filename** (*str*) – The full path name of the Package to close (for example “C:WorkspacePackagesSubfolderPackage.pkg”) or a path name relative to the Packages directory of the current workspace (for example “SubfolderPackage.pkg”)

Returns:  True, if the package was closed, otherwise False.

Return type:  bool

CloseProject(*filename*)[¶](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.CloseProject "Link to this definition")  
Closes a project.

Parameters:  **filename** (*str*) – The full path name of the project to close or a path name relative to the Packages directory of the current workspace

Returns:  True, if the project was closed, otherwise False.

Return type:  bool

Exit(*timeout=60*)[¶](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.Exit "Link to this definition")  
Exits the currently running instance of the application (Hard Exit). Prefer the method Quit instead.

Parameters:  **timeout** (*int*) – Timeout in seconds before giving up to wait for application shutdown and raising an exception.

Returns:  True, if operation successful.

Return type:  bool

Raises:  
**COMException** – if shutdown failed

GeneratePackageDocumentation(*pkgPath*, *docPath*, *doasync=True*)[¶](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.GeneratePackageDocumentation "Link to this definition")  
Creates documentation file(s) for a package or all packages in a folder depending on the given path.

Parameters:  - **pkgPath** (*str*) – Path of either a package or a folder containing packages.

- **docPath** (*str*) – Path where the documentation files will be created.

- **doasync** (*bool*) – Mode of execution: asynchronous if True otherwise synchronous.

Returns:  Path of the generated (index) document if synchronous mode otherwise None.

Return type:  str

GetAnalysisEnvironment()[¶](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.GetAnalysisEnvironment "Link to this definition")  
Returns the analysis environment.

Returns:  A [`COMAnalysisEnvironment`](#tts.core.api.comApi.Comserver.COMAnalysisEnvironment "tts.core.api.comApi.Comserver.COMAnalysisEnvironment") object.

Return type:  [`COMAnalysisEnvironment`](#tts.core.api.comApi.Comserver.COMAnalysisEnvironment "tts.core.api.comApi.Comserver.COMAnalysisEnvironment")

GetCaches()[¶](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.GetCaches "Link to this definition")  
Returns the cache module.

Returns:  A [`COMCaches`](#tts.core.api.comApi.Comserver.COMCaches "tts.core.api.comApi.Comserver.COMCaches") object.

Return type:  [`COMCaches`](#tts.core.api.comApi.Comserver.COMCaches "tts.core.api.comApi.Comserver.COMCaches")

GetCurrentTestConfiguration()[¶](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.GetCurrentTestConfiguration "Link to this definition")  
Returns a TestConfiguration object providing access to settings of the currently active test configuration file.

Returns:  TestConfiguration object

Return type:  [`COMTestConfiguration`](#tts.core.api.comApi.Comserver.COMTestConfiguration "tts.core.api.comApi.Comserver.COMTestConfiguration")

GetCurrentTestbenchConfiguration()[¶](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.GetCurrentTestbenchConfiguration "Link to this definition")  
Returns a TestbenchConfiguration object providing access to settings of the currently active testbench configuration file.

Returns:  TestConfiguration object

Return type:  [`COMTestbenchConfiguration`](#tts.core.api.comApi.Comserver_ET.COMTestbenchConfiguration "tts.core.api.comApi.Comserver_ET.COMTestbenchConfiguration")

GetInstallDir()[¶](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.GetInstallDir "Link to this definition")  
Returns the installation directory.

Returns:  the installation directory.

Return type:  str

GetKeywordCatalogModule()[¶](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.GetKeywordCatalogModule "Link to this definition")  
Returns the keyword catalog module.

Returns:  A [`COMKeywordCatalog`](#tts.core.api.comApi.Comserver.COMKeywordCatalog "tts.core.api.comApi.Comserver.COMKeywordCatalog") object.

Return type:  [`COMKeywordCatalog`](#tts.core.api.comApi.Comserver.COMKeywordCatalog "tts.core.api.comApi.Comserver.COMKeywordCatalog")

GetLoadedPatches()[¶](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.GetLoadedPatches "Link to this definition")  
Queries the list of loaded patches of the COM-Application.

Returns:  list of loaded patches

Return type:  list\<str\>

GetObjectApiPythonPath()[¶](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.GetObjectApiPythonPath "Link to this definition")  
Returns Python path for Object API.

Append it to the `sys.path` variable to import the Object API:

    import sys
    sys.path.append(ecutest.GetObjectApiPythonPath())
    from ApiClient import ApiClient

This directory also contains the JAR of the Java client and the DLL of the .Net client.

Returns:  Directory for Python path of Object API.

Return type:  str

GetPackages()[¶](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.GetPackages "Link to this definition")  
Returns a container object which gives access to all opened packages in COM-Application.

Returns:  The container object to access all opened packages.

Return type:  [`COMPackages`](#tts.core.api.comApi.Comserver.COMPackages "tts.core.api.comApi.Comserver.COMPackages")

GetProjects()[¶](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.GetProjects "Link to this definition")  
Returns a container object which gives access to all opened projects in COM-Application.

Returns:  The container object to access all opened packages.

Return type:  [`COMProjects`](#tts.core.api.comApi.Comserver.COMProjects "tts.core.api.comApi.Comserver.COMProjects")

GetSetting(*settingName*)[¶](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.GetSetting "Link to this definition")  
Queries the COM-Application setting value by name. Possible setting names are: - configPath - errorLogFile - generatorPath - language - logFile - packagePath - reportPath - templatePath - parameterPath - traceStepPath - userPyModulesPath - utilityPath - workspacePath - offlineModelPath - offlineSgbdPath - offlineFiuPath - settingsPath

Parameters:  **settingName** (*str*) – the setting name

Returns:  setting value or None if not defined

Return type:  str or None

GetTestEnvironment()[¶](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.GetTestEnvironment "Link to this definition")  
Returns the test environment.

Returns:  A [`COMTestEnvironment`](#tts.core.api.comApi.Comserver.COMTestEnvironment "tts.core.api.comApi.Comserver.COMTestEnvironment") object.

Return type:  [`COMTestEnvironment`](#tts.core.api.comApi.Comserver.COMTestEnvironment "tts.core.api.comApi.Comserver.COMTestEnvironment")

GetTestManagementModule()[¶](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.GetTestManagementModule "Link to this definition")  
Returns the testmanagement module.

Returns:  A [`COMTestManagement`](#tts.core.api.comApi.Comserver.COMTestManagement "tts.core.api.comApi.Comserver.COMTestManagement") object.

Return type:  [`COMTestManagement`](#tts.core.api.comApi.Comserver.COMTestManagement "tts.core.api.comApi.Comserver.COMTestManagement")

GetVersion()[¶](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.GetVersion "Link to this definition")  
Queries the COM-Application version.

Returns:  Version string.

Return type:  str

HasActiveTasks()[¶](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.HasActiveTasks "Link to this definition")  
Returns if any tasks are running or are queued.

Returns:  True, if any active task exists.

Return type:  bool

IconizeMainFrame(*iconize*)[¶](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.IconizeMainFrame "Link to this definition")  
Iconize/Restore the MainFrame Window

Parameters:  **iconize** (*bool*) – True - minimize window, False - restore window

Returns:  True if success, otherwise False

Return type:  bool

IsApplicationRunning()[¶](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.IsApplicationRunning "Link to this definition")  
Check if the application process is running and ready to use.

Returns:  True if application is already running, otherwise False.

Return type:  bool

IsStarted()[¶](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.IsStarted "Link to this definition")  
Returns whether the currently selected test configuration and testbench configuration are started.

Returns:  True if configurations are started, else False

Return type:  bool

IsXmlRpcApiBusy()[¶](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.IsXmlRpcApiBusy "Link to this definition")  
(undocumented) Returns whether the underlying XMLRPC API is currently blocked by another call

Return type:  boolean

LoadGlobalMapping(*filename*, *index=-1*, *reloadIfNecessary=False*)[¶](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.LoadGlobalMapping "Link to this definition")  
Loads a mapping file (\*.xam) into the global mapping space.

Parameters:  - **filename** (*str*) – The full path name of the mapping file to load or a path name relative to the current workspace.

- **index** (*int*) – The priority-index of the mapping file. Index 0 is highest priority. (default is ‘-1’ for lowest priority)

- **reloadIfNecessary** (*bool*) – Reload the mapping file when it is already open. (default: False)

Returns:  True, if the mapping file was successfully loaded, otherwise False.

Return type:  bool

MaximizeMainFrame(*maximize*)[¶](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.MaximizeMainFrame "Link to this definition")  
Maximize/Restore the MainFrame Window

Parameters:  **maximize** (*bool*) – True - maximize window, False - restore window

Returns:  True if success, otherwise False

Return type:  bool

OpenPackage(*filename*)[¶](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.OpenPackage "Link to this definition")  
Opens an existing Package (testcase) in COM-Application. If the package to be opened is password protected an exception is raised.

Parameters:  **filename** (*str*) – The full path name of the Package to open (for example “C:WorkspacePackagesSubfolderPackage.pkg”) or a path name relative to the Packages directory of the current workspace (for example “SubfolderPackage.pkg”)

Returns:  COMPackage, if the package is successfully opened, otherwise None.

Return type:  [`COMPackage`](#tts.core.api.comApi.Comserver.COMPackage "tts.core.api.comApi.Comserver.COMPackage")

Raises:  
**COMException** – if the package is password protected

OpenProject(*filename*, *execInCurrentPkgDir=False*, *filterExpression=''*)[¶](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.OpenProject "Link to this definition")  
Opens an existing project in COM-Application.

Parameters:  - **filename** (*str*) – The full path name of the project to open or a path name relative to the Packages directory of the current workspace

- **execInCurrentPkgDir** (*bool*) – defines whether relative references in the project are resolved starting from the current workspaces package directory or from the project file location

- **filterExpression** (*str*) – a valid filter expression (see the main help document, section ‘Projects’)

Returns:  COMProject, if the project is successfully opened, otherwise None.

Return type:  [`COMProject`](#tts.core.api.comApi.Comserver.COMProject "tts.core.api.comApi.Comserver.COMProject")

OpenTestConfiguration(*filename*)[¶](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.OpenTestConfiguration "Link to this definition")  
Opens a test-configuration file (\*.tcf).

Parameters:  **filename** (*str*) – The full path name of the test-configuration file to open or a path name relative to the Configurations directory of the current workspace

Returns:  True, if the configuration was successfully opened, otherwise False.

Return type:  bool

OpenTestbenchConfiguration(*filename*)[¶](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.OpenTestbenchConfiguration "Link to this definition")  
Opens a testbench configuration file (\*.tbc).

Parameters:  **filename** (*str*) – The full path name of the testbench-configuration file to open.

Returns:  True, if the configuration was successfully opened, otherwise False.

Return type:  bool

Quit(*timeout=60*)[¶](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.Quit "Link to this definition")  
Exits the currently running instance of the application (Soft Exit).

Parameters:  **timeout** (*int*) – Timeout in seconds before giving up to wait for application shutdown and raising an exception.

Returns:  True, if success.

Return type:  bool

Raises:  
**COMException** – if shutdown failed

RunApplication(*workspaceDir=None*, *localSettingsDir=None*)[¶](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.RunApplication "Link to this definition")  
Runs the application process and allows to specify a workspace directory. All other COM-Application methods require a running application process.

Parameters:  - **workspaceDir** (*str* *or* *None*) – The full path name of the workspace directory. This directory must exist. If no sub directory .workspace with the corresponding settings files exists in this directory it will be created as well as the needed sub directories under the workspace directory. If the settings files exist the default directories are used like specified there. If in this case a needed directory doesn’t exist it will be created. If omitted (None) the default settings are used. In this case all default directories must exist in order to run the application process.

- **localSettingsDir** (*str* *or* *None*) – Absolute path specification to the directory in which the local user settings should be read from and stored in. If a directory is specified, it must exist. No new directory is created. In addition, no workspace selection dialog is displayed when ecu.test starts if this option is set.

Raises:  
**COMException** – if the application is already running or the process startup failed

Start()[¶](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.Start "Link to this definition")  
Starts up the currently loaded test configuration and testbench configuration files and returns a [`COMTestEnvironment`](#tts.core.api.comApi.Comserver.COMTestEnvironment "tts.core.api.comApi.Comserver.COMTestEnvironment") object.

The test- and testbench configuration can be changed by calling `OpenTestConfiguration()` and/or `OpenTestbenchConfiguration()` otherwise the last ran configurations are used.

Returns:  A [`COMTestEnvironment`](#tts.core.api.comApi.Comserver.COMTestEnvironment "tts.core.api.comApi.Comserver.COMTestEnvironment") object.

Return type:  [`COMTestEnvironment`](#tts.core.api.comApi.Comserver.COMTestEnvironment "tts.core.api.comApi.Comserver.COMTestEnvironment")

Raises:  
**COMException** – if the configuration start was prohibited by error in user script.

Stop()[¶](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.Stop "Link to this definition")  
Stops up the currently loaded test configuration and testbench configuration files and returns a [`COMTestEnvironment`](#tts.core.api.comApi.Comserver.COMTestEnvironment "tts.core.api.comApi.Comserver.COMTestEnvironment") object.

Returns:  A [`COMTestEnvironment`](#tts.core.api.comApi.Comserver.COMTestEnvironment "tts.core.api.comApi.Comserver.COMTestEnvironment") object.

Return type:  [`COMTestEnvironment`](#tts.core.api.comApi.Comserver.COMTestEnvironment "tts.core.api.comApi.Comserver.COMTestEnvironment")

UnloadGlobalMapping(*filename*, *force=False*)[¶](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.UnloadGlobalMapping "Link to this definition")  
Unloads a mapping file (\*.xam) from the global mapping space.

Parameters:  - **filename** (*str*) – The full path name of the mapping file to unload or a path name relative to the current workspace.

- **force** (*bool*) – Ignore unsaved changes. (default: False)

Returns:  True, if the mapping file was successfully unloaded, otherwise False.

Return type:  bool

UpdateUserLibraries()[¶](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.UpdateUserLibraries "Link to this definition")  
Update all user libraries. Only possible if neither a test nor the analysis is running.

Returns:  True if success, otherwise False

Return type:  bool

WaitForIdle(*timeout=None*)[¶](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.WaitForIdle "Link to this definition")  
Waits until the job count in the task manager reaches zero. With the timeout parameter you can specify the maximum waiting time in seconds.

Parameters:  **timeout** (*float*) – Timeout in seconds

Returns:  True, if a job count of zero was reached within the timeout

Return type:  bool

## COMAnalysisEnvironment[¶](#comanalysisenvironment "Link to this heading")

*class* COMAnalysisEnvironment[¶](#tts.core.api.comApi.Comserver.COMAnalysisEnvironment "Link to this definition")  
This class represents the currently started analysis environment. This environment supports operations to run analysis jobs.

ExecuteJob(*jobFile*, *createReportDir=True*)[¶](#tts.core.api.comApi.Comserver.COMAnalysisEnvironment.ExecuteJob "Link to this definition")  
Starts the execution of an analysis job.

Parameters:  - **jobFile** (*str*) – The full path name of the analysis job file.

- **createReportDir** (*bool*) – Flag that indicates whether a new report directory is created, or whether the report should be stored next to the job.

Returns:  A [`COMAnalysisExecutionInfo`](#tts.core.api.comApi.Comserver.COMAnalysisExecutionInfo "tts.core.api.comApi.Comserver.COMAnalysisExecutionInfo") object.

Return type:  [`COMAnalysisExecutionInfo`](#tts.core.api.comApi.Comserver.COMAnalysisExecutionInfo "tts.core.api.comApi.Comserver.COMAnalysisExecutionInfo")

GetAnalysisExecutionInfo()[¶](#tts.core.api.comApi.Comserver.COMAnalysisEnvironment.GetAnalysisExecutionInfo "Link to this definition")  
Returns:  A [`COMAnalysisExecutionInfo`](#tts.core.api.comApi.Comserver.COMAnalysisExecutionInfo "tts.core.api.comApi.Comserver.COMAnalysisExecutionInfo") object.

Return type:  [`COMAnalysisExecutionInfo`](#tts.core.api.comApi.Comserver.COMAnalysisExecutionInfo "tts.core.api.comApi.Comserver.COMAnalysisExecutionInfo")

MergeJobReports(*mainReportFilename*, *jobReports*)[¶](#tts.core.api.comApi.Comserver.COMAnalysisEnvironment.MergeJobReports "Link to this definition")  
Merge reports of analysis job executions into a main report.

Parameters:  - **mainReportFilename** (*str*) – filename of main report

- **jobReports** (*list\<str\>*) – list of filenames to reports of analysis job executions

Returns:  True if merge was successful, else False

Return type:  bool

## COMAnalysisExecutionInfo[¶](#comanalysisexecutioninfo "Link to this heading")

*class* COMAnalysisExecutionInfo[¶](#tts.core.api.comApi.Comserver.COMAnalysisExecutionInfo "Link to this definition")  
This class offers operations to obtain information of the currently running analysis job.

Abort()[¶](#tts.core.api.comApi.Comserver.COMAnalysisExecutionInfo.Abort "Link to this definition")  
Aborts the current analysis job execution.

Returns:  True, if the abort succeeded. False, if the analysis job execution has already finished or aborted.

Return type:  bool

GetLogFolder()[¶](#tts.core.api.comApi.Comserver.COMAnalysisExecutionInfo.GetLogFolder "Link to this definition")  
Returns:  Folder where trace and log files of the currently executed analysis job are stored. Please note, each analysis job execution has got a separate log folder.

Return type:  str

GetReportDb()[¶](#tts.core.api.comApi.Comserver.COMAnalysisExecutionInfo.GetReportDb "Link to this definition")  
Returns:  Path to report database of current (or most recent) analysis job execution.

Return type:  str

GetResult()[¶](#tts.core.api.comApi.Comserver.COMAnalysisExecutionInfo.GetResult "Link to this definition")  
Returns the result of the analysis job execution. If the execution has not finished yet, the result equates the result at calling time.

Returns:  The current result. One of - NONE - SUCCESS - INCONCLUSIVE - FAILED - ERROR

Return type:  str

GetStartTime()[¶](#tts.core.api.comApi.Comserver.COMAnalysisExecutionInfo.GetStartTime "Link to this definition")  
Returns the time where the analysis job execution has started.

Returns:  The analysis job starting time.

Return type:  str

GetState()[¶](#tts.core.api.comApi.Comserver.COMAnalysisExecutionInfo.GetState "Link to this definition")  
Returns the state of the current analysis job execution.

Returns:  The state of the current analysis job execution. One of - IDLE - RUNNING - ABORTED - FINISHED

Return type:  str

WaitForTestexecutionCompletion(*timeout=None*)[¶](#tts.core.api.comApi.Comserver.COMAnalysisExecutionInfo.WaitForTestexecutionCompletion "Link to this definition")  
Waits until the current analysis job execution state will change to ABORTED or FINISHED. The timeout parameter specifies the maximum waiting time.

Returns:  The state of the current analysis job execution. One of - IDLE - RUNNING - ABORTED - FINISHED

Return type:  str

## COMCache[¶](#comcache "Link to this heading")

*class* COMCache[¶](#tts.core.api.comApi.Comserver.COMCache "Link to this definition")  
This class offers access to a specific file cache.

Clear(*force=False*)[¶](#tts.core.api.comApi.Comserver.COMCache.Clear "Link to this definition")  
Remove all cache files of this category.

Parameters:  **force** (*bool*) – Close already opend cache files. ATTENTION: Data objects that are used in ecu.test will be destroyed.

GetFiles()[¶](#tts.core.api.comApi.Comserver.COMCache.GetFiles "Link to this definition")  
Returns all cache files of this category.

Returns:  List of available cache files

Return type:  list\<str\>

Insert(*filePath*, *dbChannel=''*)[¶](#tts.core.api.comApi.Comserver.COMCache.Insert "Link to this definition")  
Insert a database to the cache.

Parameters:  - **filePath** (*str*) – The file path of the database to be added to the cache

- **dbChannel** (*str*) – The optional database channel. Only needed by bus and service databases.

## COMCaches[¶](#comcaches "Link to this heading")

*class* COMCaches[¶](#tts.core.api.comApi.Comserver.COMCaches "Link to this definition")  
This class offers access to the different files caches.

GetA2lCache()[¶](#tts.core.api.comApi.Comserver.COMCaches.GetA2lCache "Link to this definition")  
Provides access to A2L cache files.

Returns:  Cache object

Return type:  [`COMCache`](#tts.core.api.comApi.Comserver.COMCache "tts.core.api.comApi.Comserver.COMCache")

GetBusCache()[¶](#tts.core.api.comApi.Comserver.COMCaches.GetBusCache "Link to this definition")  
Provides access to bus cache files.

Returns:  Cache object

Return type:  [`COMCache`](#tts.core.api.comApi.Comserver.COMCache "tts.core.api.comApi.Comserver.COMCache")

GetElfCache()[¶](#tts.core.api.comApi.Comserver.COMCaches.GetElfCache "Link to this definition")  
Provides access to ELF cache files.

Returns:  Cache object

Return type:  [`COMCache`](#tts.core.api.comApi.Comserver.COMCache "tts.core.api.comApi.Comserver.COMCache")

GetModelCache()[¶](#tts.core.api.comApi.Comserver.COMCaches.GetModelCache "Link to this definition")  
Provides access to model cache files.

Returns:  Cache object

Return type:  [`COMCache`](#tts.core.api.comApi.Comserver.COMCache "tts.core.api.comApi.Comserver.COMCache")

GetServiceCache()[¶](#tts.core.api.comApi.Comserver.COMCaches.GetServiceCache "Link to this definition")  
Provides access to service cache files.

Returns:  Cache object

Return type:  [`COMCache`](#tts.core.api.comApi.Comserver.COMCache "tts.core.api.comApi.Comserver.COMCache")

## COMConstant[¶](#comconstant "Link to this heading")

*class* COMConstant[¶](#tts.core.api.comApi.Comserver.COMConstant "Link to this definition")  
This object gives access to the properties of a constant.

Description[¶](#tts.core.api.comApi.Comserver.COMConstant.Description "Link to this definition")  
returns the description of this constant.

Returns:  the description of this constant

Return type:  str

Name[¶](#tts.core.api.comApi.Comserver.COMConstant.Name "Link to this definition")  
returns the name of this constant.

Returns:  the name of this constant

Return type:  str

Value[¶](#tts.core.api.comApi.Comserver.COMConstant.Value "Link to this definition")  
returns the value of this constant as string.

Returns:  the value of this constant

Return type:  str

GetDescription()[¶](#tts.core.api.comApi.Comserver.COMConstant.GetDescription "Link to this definition")  
returns the description of this constant.

Returns:  the description of this constant

Return type:  str

GetName()[¶](#tts.core.api.comApi.Comserver.COMConstant.GetName "Link to this definition")  
returns the name of this constant.

Returns:  the name of this constant

Return type:  str

GetValue()[¶](#tts.core.api.comApi.Comserver.COMConstant.GetValue "Link to this definition")  
returns the value of this constant as string.

Returns:  the value of this constant

Return type:  str

## COMConstants[¶](#comconstants "Link to this heading")

*class* COMConstants[¶](#tts.core.api.comApi.Comserver.COMConstants "Link to this definition")  
This object gives access to all global constants of the currently loaded test configuration.

Count[¶](#tts.core.api.comApi.Comserver.COMConstants.Count "Link to this definition")  
returns the number of constants.

Returns:  the number of constants.

Return type:  int

GetCount()[¶](#tts.core.api.comApi.Comserver.COMConstants.GetCount "Link to this definition")  
returns the number of constants.

Returns:  the number of constants.

Return type:  int

Item(*idxOrName*)[¶](#tts.core.api.comApi.Comserver.COMConstants.Item "Link to this definition")  
returns a specified constant. idxOrName can be either the name or an index. If an index is given then it should be between 0 and `GetCount()` - 1

Parameters:  **idxOrName** – The name of the constant or an index

Returns:  the constant.

Return type:  [`COMConstant`](#tts.core.api.comApi.Comserver.COMConstant "tts.core.api.comApi.Comserver.COMConstant")

## COMKeywordCatalog[¶](#comkeywordcatalog "Link to this heading")

*class* COMKeywordCatalog[¶](#tts.core.api.comApi.Comserver.COMKeywordCatalog "Link to this definition")  
This class offers access to the keyword catalog interface.

Connect()[¶](#tts.core.api.comApi.Comserver.COMKeywordCatalog.Connect "Link to this definition")  
Trys to establish a connection to the keyword catalog server defined in the workspace settings.

Returns:  The connection state: True if the connection has been established, else False.

Return type:  boolean

GetAvailableCatalogs()[¶](#tts.core.api.comApi.Comserver.COMKeywordCatalog.GetAvailableCatalogs "Link to this definition")  
Returns the names of the available catalogs of the current project.

Returns:  List of available catalog names

Return type:  list\<str\>

GetAvailableProjects()[¶](#tts.core.api.comApi.Comserver.COMKeywordCatalog.GetAvailableProjects "Link to this definition")  
Returns the available projects.

Returns:  List of available project names

Return type:  list\<str\>

GetAvailableVariants()[¶](#tts.core.api.comApi.Comserver.COMKeywordCatalog.GetAvailableVariants "Link to this definition")  
Returns the available variants.

Returns:  List of available variant names

Return type:  list\<str\>

GetCurrentCatalogName()[¶](#tts.core.api.comApi.Comserver.COMKeywordCatalog.GetCurrentCatalogName "Link to this definition")  
Returns the name of the loaded catalog or None, if no catalog has been loaded.

Returns:  Name of current catalog or None

Return type:  str

GetCurrentProject()[¶](#tts.core.api.comApi.Comserver.COMKeywordCatalog.GetCurrentProject "Link to this definition")  
Returns the name of the current project or None, if no project has been configured.

Returns:  Current project name or None

Return type:  str

GetCurrentVariant()[¶](#tts.core.api.comApi.Comserver.COMKeywordCatalog.GetCurrentVariant "Link to this definition")  
Returns the name of the current variant or None, if no variant has been configured.

Returns:  Current variant name or None

Return type:  str

IsConnected()[¶](#tts.core.api.comApi.Comserver.COMKeywordCatalog.IsConnected "Link to this definition")  
Returns the connection state to the keyword catalog server.

Returns:  True, if the connection has already been established.

Return type:  boolean

LoadCatalog(*catalogName*)[¶](#tts.core.api.comApi.Comserver.COMKeywordCatalog.LoadCatalog "Link to this definition")  
Loads the referenced catalog.

Parameters:  **catalogName** (*str*) – Name of the catalog.

Raises:  
**exception** – If an invalid catalog name has been referenced.

SetProject(*projectName*)[¶](#tts.core.api.comApi.Comserver.COMKeywordCatalog.SetProject "Link to this definition")  
Sets the referenced project.

Parameters:  **projectName** (*str*) – Project name

Raises:  
**exception** – If an invalid project name has been referenced.

SetVariant(*variantName*)[¶](#tts.core.api.comApi.Comserver.COMKeywordCatalog.SetVariant "Link to this definition")  
Sets the referenced variant.

Parameters:  **variantName** (*str*) – Variant name

Raises:  
**exception** – If an invalid variant name has been referenced.

## COMPackage[¶](#compackage "Link to this heading")

*class* COMPackage[¶](#tts.core.api.comApi.Comserver.COMPackage "Link to this definition")  
This object gives access to the properties of an opened package.

Description[¶](#tts.core.api.comApi.Comserver.COMPackage.Description "Link to this definition")  
returns the description of this package.

Returns:  the name of this package

Return type:  str

Filename[¶](#tts.core.api.comApi.Comserver.COMPackage.Filename "Link to this definition")  
returns the full path of this package.

Returns:  the full path of this package

Return type:  str

Name[¶](#tts.core.api.comApi.Comserver.COMPackage.Name "Link to this definition")  
returns the name of this package.

Returns:  the name of this package

Return type:  str

Variables[¶](#tts.core.api.comApi.Comserver.COMPackage.Variables "Link to this definition")  
Returns a container object which gives access to all variables of this package.

Returns:  The container object to access all variables.

Return type:  [`COMVariables`](#tts.core.api.comApi.Comserver.COMVariables "tts.core.api.comApi.Comserver.COMVariables")

Check()[¶](#tts.core.api.comApi.Comserver.COMPackage.Check "Link to this definition")  
Returns a list of the errors of the package (including all subpackages).

Every list element is a tuple containing:

> - file path
>
> - seriousness (‘Error’, ‘Warning’ or ‘Note’)
>
> - error message
>
> - line number
>
> - step UUID

Returns:  Error List

Return type:  list\<tuple\>

CheckNG()[¶](#tts.core.api.comApi.Comserver.COMPackage.CheckNG "Link to this definition")  
Returns converted error descriptions into specific WarningsNG plugin JSON format.

> - issues
>
>   > - description (link to package)
>   >
>   > - directory (package parent directory)
>   >
>   > - fileName (package name)
>   >
>   > - message (error message)
>   >
>   > - packageName (workspace subdirectory path of package)
>   >
>   > - severity (Error -> ‘ERROR’, Warning -> ‘HIGH’ or Note -> ‘NORMAL’)
>
> - size (count of issues)
>
> - \_class

Returns:  error descriptions as issues in JSON format

Return type:  str

GetDescription()[¶](#tts.core.api.comApi.Comserver.COMPackage.GetDescription "Link to this definition")  
returns the description of this package.

Returns:  the name of this package

Return type:  str

GetFilename()[¶](#tts.core.api.comApi.Comserver.COMPackage.GetFilename "Link to this definition")  
returns the full path of this package.

Returns:  the full path of this package

Return type:  str

GetName()[¶](#tts.core.api.comApi.Comserver.COMPackage.GetName "Link to this definition")  
returns the name of this package.

Returns:  the name of this package

Return type:  str

GetVariables()[¶](#tts.core.api.comApi.Comserver.COMPackage.GetVariables "Link to this definition")  
Returns a container object which gives access to all variables of this package.

Returns:  The container object to access all variables.

Return type:  [`COMVariables`](#tts.core.api.comApi.Comserver.COMVariables "tts.core.api.comApi.Comserver.COMVariables")

## COMPackages[¶](#compackages "Link to this heading")

*class* COMPackages[¶](#tts.core.api.comApi.Comserver.COMPackages "Link to this definition")  
This object gives access to all opened packages in COM-Application.

Count[¶](#tts.core.api.comApi.Comserver.COMPackages.Count "Link to this definition")  
returns the number of opened packages in COM-Application.

Returns:  the number of opened packages.

Return type:  int

GetCount()[¶](#tts.core.api.comApi.Comserver.COMPackages.GetCount "Link to this definition")  
returns the number of opened packages in COM-Application.

Returns:  the number of opened packages.

Return type:  int

Item(*pkg*)[¶](#tts.core.api.comApi.Comserver.COMPackages.Item "Link to this definition")  
returns a specified package. pkg can be either the full path or an index. If an index is given then it should be larger than 0 and lesser the number of packages opened. How many packages are currently open can be determined with `GetCount`

Parameters:  **pkg** – The full path or an index

Returns:  the package.

Return type:  [`COMPackage`](#tts.core.api.comApi.Comserver.COMPackage "tts.core.api.comApi.Comserver.COMPackage")

## COMProject[¶](#comproject "Link to this heading")

*class* COMProject[¶](#tts.core.api.comApi.Comserver.COMProject "Link to this definition")  
This object gives access to the properties of an opened project.

Filename[¶](#tts.core.api.comApi.Comserver.COMProject.Filename "Link to this definition")  
returns the full path of this project.

Returns:  the full path of this project

Return type:  str

Packages[¶](#tts.core.api.comApi.Comserver.COMProject.Packages "Link to this definition")  
returns a list of packages used in this project.

Returns:  list of packages

Return type:  str

Check()[¶](#tts.core.api.comApi.Comserver.COMProject.Check "Link to this definition")  
Returns a list of the errors of the project.

Every list element is a tuple containing:

> - file path
>
> - seriousness (‘Error’, ‘Warning’ or ‘Note’)
>
> - error message
>
> - line number
>
> - step UUID

Returns:  Error List

Return type:  list\<tuple\>

CheckNG()[¶](#tts.core.api.comApi.Comserver.COMProject.CheckNG "Link to this definition")  
Returns converted error descriptions into specific WarningsNG plugin JSON format.

> - issues
>
>   > - description (link to project)
>   >
>   > - directory (project parent directory)
>   >
>   > - fileName (project name)
>   >
>   > - message (error message)
>   >
>   > - packageName (workspace subdirectory path of project)
>   >
>   > - severity (Error -> ‘ERROR’, Warning -> ‘HIGH’ or Note -> ‘NORMAL’)
>
> - size (count of issues)
>
> - \_class

Returns:  error descriptions as issues in JSON format

Return type:  str

GetFilename()[¶](#tts.core.api.comApi.Comserver.COMProject.GetFilename "Link to this definition")  
returns the full path of this project.

Returns:  the full path of this project

Return type:  str

GetPackages()[¶](#tts.core.api.comApi.Comserver.COMProject.GetPackages "Link to this definition")  
returns a list of packages used in this project.

Returns:  list of packages

Return type:  str

## COMProjects[¶](#comprojects "Link to this heading")

*class* COMProjects[¶](#tts.core.api.comApi.Comserver.COMProjects "Link to this definition")  
This object gives access to all opened projects in COM-Application.

Count[¶](#tts.core.api.comApi.Comserver.COMProjects.Count "Link to this definition")  
returns the number of opened projects in COM-Application.

Returns:  the number of opened projects.

Return type:  int

GetCount()[¶](#tts.core.api.comApi.Comserver.COMProjects.GetCount "Link to this definition")  
returns the number of opened projects in COM-Application.

Returns:  the number of opened projects.

Return type:  int

Item(*prj*)[¶](#tts.core.api.comApi.Comserver.COMProjects.Item "Link to this definition")  
returns a specified project. prj can be either the full path or an index. If an index is given then it should be larger than 0 and lesser than the number of projects opened. How many projects are currently open can be determined with `GetCount`

Parameters:  **prj** – The full path or an index

Returns:  the project.

Return type:  [`COMProject`](#tts.core.api.comApi.Comserver.COMProject "tts.core.api.comApi.Comserver.COMProject")

## COMTestbenchConfiguration[¶](#comtestbenchconfiguration "Link to this heading")

*class* COMTestbenchConfiguration[¶](#tts.core.api.comApi.Comserver_ET.COMTestbenchConfiguration "Link to this definition")  
Represent the currently loaded testbench configuration file and provides methods for accessing the contained settings.

GetFilename()[¶](#tts.core.api.comApi.Comserver_ET.COMTestbenchConfiguration.GetFilename "Link to this definition")  
returns the full path of this testbench configuration.

Returns:  the full path of this testbench configuration

Return type:  str

GetToolhostInfo()[¶](#tts.core.api.comApi.Comserver_ET.COMTestbenchConfiguration.GetToolhostInfo "Link to this definition")  
Returns a list of lists containing url, version, revision and loaded patches of all connected toolhosts.

Returns:  List of toolhost information(url, version, revision and loaded patches) as list

Return type:  list\<list\>

## COMTestConfiguration[¶](#comtestconfiguration "Link to this heading")

*class* COMTestConfiguration[¶](#tts.core.api.comApi.Comserver.COMTestConfiguration "Link to this definition")  
Represent the currently loaded test configuration file and provides methods for accessing the contained settings.

Filename[¶](#tts.core.api.comApi.Comserver.COMTestConfiguration.Filename "Link to this definition")  
returns the full path of this test configuration.

Returns:  the full path of this configuration

Return type:  str

GlobalConstants[¶](#tts.core.api.comApi.Comserver.COMTestConfiguration.GlobalConstants "Link to this definition")  
Returns a container object which gives access to all global constants of the currently loaded test configuration.

Returns:  The container object to access all global constants.

Return type:  [`COMConstants`](#tts.core.api.comApi.Comserver.COMConstants "tts.core.api.comApi.Comserver.COMConstants")

GetFilename()[¶](#tts.core.api.comApi.Comserver.COMTestConfiguration.GetFilename "Link to this definition")  
returns the full path of this test configuration.

Returns:  the full path of this configuration

Return type:  str

GetGlobalConstants()[¶](#tts.core.api.comApi.Comserver.COMTestConfiguration.GetGlobalConstants "Link to this definition")  
Returns a container object which gives access to all global constants of the currently loaded test configuration.

Returns:  The container object to access all global constants.

Return type:  [`COMConstants`](#tts.core.api.comApi.Comserver.COMConstants "tts.core.api.comApi.Comserver.COMConstants")

SetGlobalConstant(*name*, *value*)[¶](#tts.core.api.comApi.Comserver.COMTestConfiguration.SetGlobalConstant "Link to this definition")  
Assign a value to a global constant. If the global constant does not exist it is created. This method requires a test configuration file to be loaded, otherwise an exception is thrown. The changed test configuration is saved instantly.

Parameters:  - **name** (*str*) – Name of the constant to be modified.

- **value** (*str*) – Value to be assigned. This must be a literal of a python data type, e.g. “1” (int literal) or “‘foo’” (string literal) or “[1, 2, 3]” (literal for a list with integer elements).

SetReportBaseFolder(*path*)[¶](#tts.core.api.comApi.Comserver.COMTestConfiguration.SetReportBaseFolder "Link to this definition")  
Change base folder for test reports. If the new base folder does not exist it is created. The changed test configuration is saved instantly.

Parameters:  **path** (*str*) – Absolute or relative path to the new report base folder. If a relative path is passed the data directory is used as reference directory.

## COMTestEnvironment[¶](#comtestenvironment "Link to this heading")

*class* COMTestEnvironment[¶](#tts.core.api.comApi.Comserver.COMTestEnvironment "Link to this definition")  
This class represents the currently started test environment. The test environment supports operations to run packages (testcases) and projects.

ExecutePackage(*pkgFile*, *runTraceAnalysis=True*, *runTest=True*, *paramValueDictAsList=None*, *recInfoDictAsList=None*, *parameterFiles=None*, *interactive=False*, *traceAnalysisMode=1*)[¶](#tts.core.api.comApi.Comserver.COMTestEnvironment.ExecutePackage "Link to this definition")  
Starts the execution of the specified package file. The package must be already opened with `OpenPackage`. If it is not opened a call of this function will raise an error.

Parameters:  - **pkgFile** (*str*) – The full path name of the Package to execute (for example “C:\Workspace\Packages\Subfolder\Package.pkg”) or a path name relative to the Packages directory of the current workspace (for example “Subfolder\Package.pkg”)

- **runTraceAnalysis** (*bool*) – specifies whether the trace analysis should be executed

- **runTest** (*bool*) – specifies whether the test should be executed

- **paramValueDictAsList** (*list\<tuple\>*) – A list with tuples (name, value) of length two for each parameter for the test and the trace analysis. Due to technical restrictions of the COM interface the parameter values must not contain dictionaries.

- **recInfoDictAsList** (*list\<tuple\>*) –

  This list with tuples (recording group name, recording info list) assigns traces to recording groups.

  The entry ‘recording group name’ is a name of an existing recording group.

  The entry ‘recording info list’ is a list of recording infos. A recording info is a list of tuples (key, value) which defines a dictionary with the following structure:

  path: Either a trace file or a list of trace files. This must be given.

  recordingName: The name of the recording, if it is necessary. For instance in a container file format for the unique identification.

  recordingNumber: The number of the recording, if it is necessary. For instance in a container file format for the unique identification.

  recordingType: The file type of the recording. If not given, an auto type detection is performed.

  formatDetails: Format specific details. See the ‘Supported file formats’ section in the documentation.

- **parameterFiles** (*list\<str\>*) – List of pathes to \*.ppd files containing parameters to be applied to the package.

- **interactive** (*bool*) – Specify if the package should be executed in the interactive mode

- **traceAnalysisMode** (*int*) – For internal use only

Returns:  A [`COMTestExecutionInfo`](#tts.core.api.comApi.Comserver.COMTestExecutionInfo "tts.core.api.comApi.Comserver.COMTestExecutionInfo") object.

Return type:  [`COMTestExecutionInfo`](#tts.core.api.comApi.Comserver.COMTestExecutionInfo "tts.core.api.comApi.Comserver.COMTestExecutionInfo")

Raises:  
**COMException** – This exception is raised if the packages was not opened before. Or the format of the parameter values is wrong.

ExecuteProject(*prjFile*, *autocloseProjectProgressPnl=False*, *executionMode=1*, *interactive=False*)[¶](#tts.core.api.comApi.Comserver.COMTestEnvironment.ExecuteProject "Link to this definition")  
Starts the execution of the specified project file. The project must be already opened with `OpenProject`. If it is not opened a call of this function will raise an error.

Parameters:  - **prjFile** (*str*) – The full path name of the project file

- **autocloseProjectProgressPnl** (*bool*) – Determines whether the progress dialog will be closed when finished (default False).

- **executionMode** (*int*) –

  Specifies whether and how the analysis jobs should be executed.

  0.  no job execution

  1.  sequential job execution (default)

  2.  parallel job execution

  &nbsp;

  5.  sequential job execution without report merge of analysis job sub reports into the main test report

  6.  parallel job execution without report merge of analysis job sub reports into the main test report

  &nbsp;

  9.  job execution without running the testcase part

- **interactive** (*bool*) – Specify if the project should be executed in the interactive mode

Returns:  A [`COMTestExecutionInfo`](#tts.core.api.comApi.Comserver.COMTestExecutionInfo "tts.core.api.comApi.Comserver.COMTestExecutionInfo") object.

Return type:  [`COMTestExecutionInfo`](#tts.core.api.comApi.Comserver.COMTestExecutionInfo "tts.core.api.comApi.Comserver.COMTestExecutionInfo")

Raises:  
**COMException** – Will be raised if the project has not been opened.

ExecuteProjectArchive(*przFile*, *autocloseProjectProgressPnl=True*, *executionMode=1*, *interactive=False*)[¶](#tts.core.api.comApi.Comserver.COMTestEnvironment.ExecuteProjectArchive "Link to this definition")  
Extracts a project archive and starts the execution of the archived project.

Parameters:  - **przFile** (*str*) – The full path name of the project archive file

- **autocloseProjectProgressPnl** (*boolean*) – Determines whether the progress dialog will be closed when finished (default False).

- **executionMode** (*int*) –

  Specifies whether and how the analysis jobs should be executed.

  0.  no job execution

  1.  sequential job execution (default)

  2.  parallel job execution

  &nbsp;

  5.  sequential job execution without report merge of analysis job sub reports into the main test report

  6.  parallel job execution without report merge of analysis job sub reports into the main test report

  &nbsp;

  9.  job execution without running the testcase part

- **interactive** (*bool*) – Specify if the project should be executed in the interactive mode

Returns:  A [`COMTestExecutionInfo`](#tts.core.api.comApi.Comserver.COMTestExecutionInfo "tts.core.api.comApi.Comserver.COMTestExecutionInfo") object.

Return type:  [`COMTestExecutionInfo`](#tts.core.api.comApi.Comserver.COMTestExecutionInfo "tts.core.api.comApi.Comserver.COMTestExecutionInfo")

Raises:  
**COMException** – Will be raised if the project archive could not be extracted or started.

GenerateTestReportDocument(*trfFile*, *outDir*, *fmtConfigFile*, *waitUntilFinished=False*)[¶](#tts.core.api.comApi.Comserver.COMTestEnvironment.GenerateTestReportDocument "Link to this definition")  
Generates a handler based testreport on the filesystem. It uses the settings previously stored next to the trf. This is performed when the “Save settings for later generation next to the TRF” option of the report generator configuration is ticked.

Parameters:  - **trfFile** (*str*) – path to the TRF

- **outDir** (*str*) – output directory

- **fmtConfigFile** (*str*) – Path to the reportFormatFile(XML) specifying the generator settings which should be used.

- **waitUntilFinished** (*bool*) – defines whether the API call should block until generation is finished.

Returns:  always True

Return type:  bool

GenerateTestReportDocumentFromDB(*dbFile*, *outDir*, *fmtName=None*, *waitUntilFinished=False*, *fmtConfig=None*)[¶](#tts.core.api.comApi.Comserver.COMTestEnvironment.GenerateTestReportDocumentFromDB "Link to this definition")  
Generates a handler based testreport on the filesystem.

Parameters:  - **dbFile** (*str*) – path to the databasefile

- **outDir** (*str*) – output directory

- **fmtName** (*str*) – Name of the reportformat or handler which should be used. (Optional) The default is the standardhandler.

- **fmtConfig** (*list\<tuples\>*) – A list with tuples (name, value) of length two for each configuration parameter for the report format. Due to technical restrictions of the COM interface the parameter values must not contain dictionaries.

- **waitUntilFinished** (*bool*) – defines whether the API call should block until generation is finished.

Returns:  always True

Return type:  bool

GetTestExecutionInfo()[¶](#tts.core.api.comApi.Comserver.COMTestEnvironment.GetTestExecutionInfo "Link to this definition")  
Returns:  A [`COMTestExecutionInfo`](#tts.core.api.comApi.Comserver.COMTestExecutionInfo "tts.core.api.comApi.Comserver.COMTestExecutionInfo") object.

Return type:  [`COMTestExecutionInfo`](#tts.core.api.comApi.Comserver.COMTestExecutionInfo "tts.core.api.comApi.Comserver.COMTestExecutionInfo")

## COMTestExecutionInfo[¶](#comtestexecutioninfo "Link to this heading")

*class* COMTestExecutionInfo[¶](#tts.core.api.comApi.Comserver.COMTestExecutionInfo "Link to this definition")  
This class offers operations to obtain information of the currently running test.

TestReport[¶](#tts.core.api.comApi.Comserver.COMTestExecutionInfo.TestReport "Link to this definition")  
Get a new testreport object.

Abort()[¶](#tts.core.api.comApi.Comserver.COMTestExecutionInfo.Abort "Link to this definition")  
Aborts the current testexecution.

Returns:  True, if the abort succeeded. False, if the testexecution has already finished or aborted.

Return type:  bool

AbortAfterCurrentProjectStep(*timeout=None*)[¶](#tts.core.api.comApi.Comserver.COMTestExecutionInfo.AbortAfterCurrentProjectStep "Link to this definition")  
Aborts the current testexecution.

Returns:  True, if the abort succeded. False, if the testexecution has already finished or aborted.

Return type:  bool

GenerateTestReportDocument(*outDir*, *fmtName=None*, *waitUntilFinished=False*, *fmtConfig=None*)[¶](#tts.core.api.comApi.Comserver.COMTestExecutionInfo.GenerateTestReportDocument "Link to this definition")  
Generates a handler based testreport on the filesystem.

Returns:  True - all o.k., otherwise False

Return type:  bool

Parameters:  - **outDir** (*str*) – output directory

- **fmtName** (*str*) – Name of the reportformat or handler which should be used (Optional). The default is the standardhandler.

- **waitUntilFinished** (*bool*) – defines whether the API call should block until generation is finished

- **fmtConfig** (*list(tuple(string,* *string))*) – A list with tuples (name, value) of length two for each configuration parameter for the reportformat, where name and value are of data type string (e.g., “True” instead of True for value). Due to technical restrictions of the COM interface the parameter values must not contain dictionaries.

Returns:  always True

Return type:  bool

GetLogFolder()[¶](#tts.core.api.comApi.Comserver.COMTestExecutionInfo.GetLogFolder "Link to this definition")  
Returns:  Folder where trace and log files of the currently executed package are stored. If there is no test execution in progress the log folder of the most recent package run is returned. Please note, each package run has got a separate log folder.

Return type:  str

Raises:  
**COMException** – Raises Exception when using this method on project executions.

GetPackageAbortCode()[¶](#tts.core.api.comApi.Comserver.COMTestExecutionInfo.GetPackageAbortCode "Link to this definition")  
Returns the abort code of the most recently executed package.

Return type:  str

GetPackageAbortComment()[¶](#tts.core.api.comApi.Comserver.COMTestExecutionInfo.GetPackageAbortComment "Link to this definition")  
Returns the abort comment of the most recently executed package.

Return type:  str

GetReportDb()[¶](#tts.core.api.comApi.Comserver.COMTestExecutionInfo.GetReportDb "Link to this definition")  
Returns:  Path to report database of current (or most recent) test run.

Return type:  str

GetResult()[¶](#tts.core.api.comApi.Comserver.COMTestExecutionInfo.GetResult "Link to this definition")  
Returns the result of the project execution or package execution, depending on which method (COMTestEnvironment.ExecuteProject() or COMTestEnvironment.ExecutePackage()) has called before. If the testexecution has not finished yet, the result equates the testresult at calling time.

Returns:  The current overall testresult. One of - NONE - SUCCESS - INCONCLUSIVE - FAILED - ERROR

Return type:  str

GetReturnValue(*varName*)[¶](#tts.core.api.comApi.Comserver.COMTestExecutionInfo.GetReturnValue "Link to this definition")  
If a test execution has finished GetReturnValue returns the final value of a package variable.

Parameters:  **varName** (*str*) – the variable name

Returns:  the final variable value

Return type:  dynamic

GetStartTime()[¶](#tts.core.api.comApi.Comserver.COMTestExecutionInfo.GetStartTime "Link to this definition")  
Returns the time where the testexecution starts.

Returns:  The testexecution starting time.

Return type:  str

GetState()[¶](#tts.core.api.comApi.Comserver.COMTestExecutionInfo.GetState "Link to this definition")  
Returns the state of the current testexecution.

Returns:  The state of the current testexecution. One of - IDLE - RUNNING - ABORTED - FINISHED

Return type:  str

GetTestReport()[¶](#tts.core.api.comApi.Comserver.COMTestExecutionInfo.GetTestReport "Link to this definition")  
returns the test report of the current or most recent testrun

Returns:  the test report of the current or most recent testrun

Return type:  [`COMTestReport`](#tts.core.api.comApi.Comserver.COMTestReport "tts.core.api.comApi.Comserver.COMTestReport")

WaitForTestexecutionCompletion(*timeout=None*)[¶](#tts.core.api.comApi.Comserver.COMTestExecutionInfo.WaitForTestexecutionCompletion "Link to this definition")  
Waits until the current testexecution state will change to ABORTED or FINISHED. With the timeout parameter you can specify the maximum waiting time.

Returns:  The state of the current testexecution. One of - IDLE - RUNNING - ABORTED - FINISHED

Return type:  str

## COMTestManagement[¶](#comtestmanagement "Link to this heading")

*class* COMTestManagement[¶](#tts.core.api.comApi.Comserver.COMTestManagement "Link to this definition")  
This class offers access to the testmanagement interface.

These methods can only be used if access to a test management system has previously been configured (once) manually for the current workspace.

ExportPackage(*filePath*, *exportPath*, *createNewPath=False*, *overrideExisting=True*, *timeout=None*)[¶](#tts.core.api.comApi.Comserver.COMTestManagement.ExportPackage "Link to this definition")  
Exports the given package into the test management system. The exportPath is needed to specify where the package should be placed at.

Parameters:  - **filePath** (*str*) – The file path of the package to be exported (relative to package directory or absolute).

- **exportPath** (*str*) – Path specifying where the project should be placed at. Specify the path as it would be displayed in the export dialog. Only Unix styled paths (separated by forward slashes, “/”) are allowed.

- **createNewPath** (*bool*) – If the exportPath does not exist, it will be created. (Optional) The default is False.

- **overrideExisting** (*bool*) – Defines, if an existing package with the same name (in the referenced folder) should be overridden.

- **timeout** (*int*) – timeout in seconds to wait for export to be finished (optional).

ExportPackageAttributes(*filePath*, *timeout=None*)[¶](#tts.core.api.comApi.Comserver.COMTestManagement.ExportPackageAttributes "Link to this definition")  
Exports the attributes of the given package to test management system.

Parameters:  - **filePath** (*str*) – The file path of the package whose attributes have to be exported (relative to package directory or absolute).

- **timeout** (*int*) – timeout in seconds to wait for import to be finished (optional).

ExportPackageChanges(*filePath*, *timeout=None*)[¶](#tts.core.api.comApi.Comserver.COMTestManagement.ExportPackageChanges "Link to this definition")  
Exports the changes of the given package into the test management system. The package needs to be already link with the test management system.

Parameters:  - **filePath** (*str*) – The file path of the package to be exported (relative to package directory or absolute).

- **timeout** (*int*) – timeout in seconds to wait for export to be finished (optional).

ExportProject(*filePath*, *exportPath*, *createNewPath=False*, *overrideExisting=True*, *timeout=None*)[¶](#tts.core.api.comApi.Comserver.COMTestManagement.ExportProject "Link to this definition")  
Exports the given project into the test management system. The exportPath is needed to specify where the project should be placed at.

Parameters:  - **filePath** (*str*) – The filepath of the project to be exported (relative to package directory or absolute).

- **exportPath** (*str*) – Path specifying where the project should be placed at. Specify the path as it would be displayed in the export dialog. Only Unix styled paths (separated by forward slashes, “/”) are allowed.

- **createNewPath** (*bool*) – If the exportPath does not exist, it will be created. (Optional) The default is False.

- **overrideExisting** (*bool*) – Defines, if an existing project with the same name (in the referenced folder) should be overridden.

- **timeout** (*int*) – timeout in seconds to wait for the export to be finished (optional).

ExportProjectAttributes(*filePath*, *timeout=None*)[¶](#tts.core.api.comApi.Comserver.COMTestManagement.ExportProjectAttributes "Link to this definition")  
Exports the attributes of the given project to test management system.

Parameters:  - **filePath** (*str*) – The file path of the project whose attributes have to be exported (relative to package directory or absolute).

- **timeout** (*int*) – timeout in seconds to wait for import to be finished (optional).

ExportReport(*filePath*, *archivePath=None*, *timeout=None*)[¶](#tts.core.api.comApi.Comserver.COMTestManagement.ExportReport "Link to this definition")  
Exports the given project report file into the test management system. The archive path may be used to copy the report to another directory and to reference it from the test management entry.

Parameters:  - **filePath** (*str*) – The filepath of the project report file to be exported

- **archivePath** (*str*) – Path to directory or filename to copy the report to and to reference in test management (optional).

- **timeout** (*int*) – timeout in seconds to wait for the export to be finished (optional).

GetActiveConfigurationName()[¶](#tts.core.api.comApi.Comserver.COMTestManagement.GetActiveConfigurationName "Link to this definition")  
Returns the name of the currently loaded test management configuration.

Returns:  name of test managemnt configuration

Return type:  str

GetConfigurationNames()[¶](#tts.core.api.comApi.Comserver.COMTestManagement.GetConfigurationNames "Link to this definition")  
Returns a list of all configuration names defined in the settings.

Returns:  list of configuration names

Return type:  list\<str\>

ImportPackage(*tmPackagePath*, *importPath*, *timeout=None*)[¶](#tts.core.api.comApi.Comserver.COMTestManagement.ImportPackage "Link to this definition")  
Imports a package from a test management system. The tmPackagePath specifies the package in the test management system. The package will be imported into the directory given by importPath.

Parameters:  - **tmPackagePath** (*str*) – Path specifying the package in the test management system, as it would be displayed in the import dialog. Only Unix styled paths (separated by forward slashes, “/”) are allowed.

- **importPath** (*str*) – Directory, where the package should be placed (relative to package directory or absolute).

- **timeout** (*int*) – timeout in seconds to wait for the import to be finished (optional).

ImportPackageAttributes(*filePath*, *timeout=None*)[¶](#tts.core.api.comApi.Comserver.COMTestManagement.ImportPackageAttributes "Link to this definition")  
Imports the attributes of a package from the test management system. The package must exist within the local workspace or an exception will be raised.

Parameters:  - **filePath** (*str*) – The file path of the package whose attributes have to be imported

- **timeout** (*int*) – timeout in seconds to wait for import to be finished (optional).

ImportPackageById(*tmPackageId*, *importPath*, *timeout=None*)[¶](#tts.core.api.comApi.Comserver.COMTestManagement.ImportPackageById "Link to this definition")  
Imports a package from a test management system. The tmPackageId specifies the package in the test management system. The package will be imported into the directory given by importPath.

Parameters:  - **tmPackageId** (*str*) – Id specifying the package in the test management system, as it would be displayed in the import dialog.

- **importPath** (*str*) – Directory, where the package should be placed (relative to package directory or absolute).

- **timeout** (*int*) – timeout in seconds to wait for the import to be finished (optional).

ImportPackageDirectory(*tmDirectoryPath*, *importPath*, *timeout=None*)[¶](#tts.core.api.comApi.Comserver.COMTestManagement.ImportPackageDirectory "Link to this definition")  
Imports a directory from a test management system with all subdirectories and packages. The tmDirectoryPath specifies the directory in the test management system. The directory will be imported into the directory given by importPath.

Parameters:  - **tmDirectoryPath** (*str*) – Path specifying the directory in the test management system, as it would be displayed in the import dialog. Only Unix styled paths (separated by forward slashes, “/”) are allowed.

- **importPath** (*str*) – Directory, where the imported directory should be placed (relative to package directory or absolute).

- **timeout** (*int*) – timeout in seconds to wait for import to be finished (optional).

ImportProject(*tmProjectPath*, *importPath*, *importMissingPackages=False*, *timeout=None*, *parameters=None*)[¶](#tts.core.api.comApi.Comserver.COMTestManagement.ImportProject "Link to this definition")  
Imports a project from a test management system. The tmProjectPath specifies the project in the test management system. The project will be imported into the directory given by importPath.

Parameters:  - **tmProjectPath** (*str*) – Path specifying the project in the test management system, as it would be displayed in the import dialog. Only Unix styled paths (separated by forward slashes, “/”) are allowed.

- **importPath** (*str*) – Directory, where the project should be placed (relative to package directory or absolute).

- **importMissingPackages** (*bool*) – If set, missing packages will be automatically imported.

- **timeout** (*int*) – timeout in seconds to wait for the import to be finished (optional).

- **parameters** (*list\<tuple\>*) – A list of tuples (name, value) of length two for each adapter parameter to be temporarily changed for the duration of the project import. Due to technical restrictions of the COM interface the parameter values must not contain dictionaries.Following adapter parameters can be set: Suite Run Query (only ALM Octane), Test Suite Query (only ALM Octane)

ImportProjectAttributes(*filePath*, *timeout=None*)[¶](#tts.core.api.comApi.Comserver.COMTestManagement.ImportProjectAttributes "Link to this definition")  
Imports the attributes of a project from the test management system. The project must exist within the local workspace or an exception will be raised.

Parameters:  - **filePath** (*str*) – The file path of the project whose attributes have to be imported

- **timeout** (*int*) – timeout in seconds to wait for import to be finished (optional).

ImportProjectById(*tmProjectId*, *importPath*, *importMissingPackages=False*, *timeout=None*)[¶](#tts.core.api.comApi.Comserver.COMTestManagement.ImportProjectById "Link to this definition")  
Imports a project from a test management system. The tmProjectId specifies the project in the test management system. The project will be imported into the directory given by importPath.

Parameters:  - **tmProjectId** (*str*) – Id specifying the project in the test management system, as it would be displayed in the import dialog.

- **importPath** (*str*) – Directory, where the project should be placed (relative to package directory or absolute).

- **importMissingPackages** (*bool*) – If set, missing packages will be automatically imported.

- **timeout** (*int*) – timeout in seconds to wait for the import to be finished (optional).

ImportProjectDirectory(*tmDirectoryPath*, *importPath*, *timeout=None*, *parameters=None*)[¶](#tts.core.api.comApi.Comserver.COMTestManagement.ImportProjectDirectory "Link to this definition")  
Imports a directory from a test management system with all subdirectories and projects. The tmDirectoryPath specifies the directory in the test management system. The directory will be imported into the directory given by importPath.

Parameters:  - **tmDirectoryPath** (*str*) – Path specifying the directory in the test management system, as it would be displayed in the import dialog. Only Unix styled paths (separated by forward slashes, “/”) are allowed.

- **importPath** (*str*) – Directory, where the imported directory should be placed (relative to package directory or absolute).

- **timeout** (*int*) – timeout in seconds to wait for import to be finished (optional).

- **parameters** (*list\<tuple\>*) – A list of tuples (name, value) of length two for each adapter parameter to be temporarily changed for the duration of the project import. Due to technical restrictions of the COM interface the parameter values must not contain dictionaries. Following adapter parameters can be set: Suite Run Query (only ALM Octane), Test Suite Query (only ALM Octane)

IsLoggedIn()[¶](#tts.core.api.comApi.Comserver.COMTestManagement.IsLoggedIn "Link to this definition")  
Returns True if ecu.test is currently logged in the Testmanagement system, else False

Returns:  True if ecu.test is currently logged in the Testmanagement system, else False

Return type:  bool

IsTmsAvailable()[¶](#tts.core.api.comApi.Comserver.COMTestManagement.IsTmsAvailable "Link to this definition")  
Checks if the test management service can be started

Returns:  True if the service could be started, else False

Return type:  bool

LinkAndSyncProject(*filePath*, *tmProjectPath*)[¶](#tts.core.api.comApi.Comserver.COMTestManagement.LinkAndSyncProject "Link to this definition")  
Links a project from ecu.test with a test suite in the test management system and synchronizes the contained test cases.

Parameters:  - **filePath** (*str*) – The file path of the project to be linked and synced (relative to package directory or absolute).

- **tmProjectPath** (*str*) – Path specifying the project in the test management system, as it would be displayed in the import dialog. Only Unix styled paths (separated by forward slashes, “/”) are allowed.

Returns:  Empty list on success, otherwise a list of messages from unsynced test cases.

Return type:  list\<string\>

Login(*user*, *password*)[¶](#tts.core.api.comApi.Comserver.COMTestManagement.Login "Link to this definition")  
Performs a login to the preconfigured testmanagement service.

Note

Will try a “Basic” Authentication regardless of the configuration.

Parameters:  - **user** (*str*) – User to be logged in

- **password** (*str*) – Password of the user

Returns:  True if login succeeded, else False

Return type:  bool

Logout()[¶](#tts.core.api.comApi.Comserver.COMTestManagement.Logout "Link to this definition")  
Performs a logout from the preconfigured testmanagement service.

Returns:  True if logout succeeded, else False

Return type:  bool

SetActiveConfiguration(*configName*)[¶](#tts.core.api.comApi.Comserver.COMTestManagement.SetActiveConfiguration "Link to this definition")  
Activate the specified test management configuration.

Parameters:  **configName** (*str*) – Name of the test management configuration

UpdateAttributeDefinitions(*timeout=None*)[¶](#tts.core.api.comApi.Comserver.COMTestManagement.UpdateAttributeDefinitions "Link to this definition")  
Updates the attribute definitions with attributes of the currently configured test management system.

Parameters:  **timeout** (*int*) – timeout in seconds to wait for import to be finished (optional).

## COMTestReport[¶](#comtestreport "Link to this heading")

*class* COMTestReport[¶](#tts.core.api.comApi.Comserver.COMTestReport "Link to this definition")  
This object gives access to the test report of the current or most recent testrun

Count[¶](#tts.core.api.comApi.Comserver.COMTestReport.Count "Link to this definition")  
returns the number of items in this test report. If the package was not executed yet GetCount will return 0. See: `IsOk`

Returns:  the number of items.

Return type:  int

Activity(*idx*)[¶](#tts.core.api.comApi.Comserver.COMTestReport.Activity "Link to this definition")  
returns the test step’s activity of the item with the specified index.

Parameters:  **idx** (*int*) – the index of the item to obtain the test step’s activity.

Returns:  the test step’s activity of the specified item

Return type:  str

Comment(*idx*)[¶](#tts.core.api.comApi.Comserver.COMTestReport.Comment "Link to this definition")  
returns the test step’s comment of the item with the specified index.

Parameters:  **idx** (*int*) – the index of the item to obtain the comment.

Returns:  the comment of the specified item

Return type:  str

GetAnalysisJobFiles(*extract=True*)[¶](#tts.core.api.comApi.Comserver.COMTestReport.GetAnalysisJobFiles "Link to this definition")  
Get absolute file paths to all analysis jobs within the report.

Note

The files may not be present anymore on the filesystem.

Parameters:  **extract** (*bool*) – If true, extract the analysis job files into the report folder

Returns:  list of file paths

Return type:  list\<str\>

GetCount()[¶](#tts.core.api.comApi.Comserver.COMTestReport.GetCount "Link to this definition")  
returns the number of items in this test report. If the package was not executed yet GetCount will return 0. See: `IsOk`

Returns:  the number of items.

Return type:  int

Index(*idx*)[¶](#tts.core.api.comApi.Comserver.COMTestReport.Index "Link to this definition")  
returns the index of the item with the specified index.

Parameters:  **idx** (*int*) – the index of the item to obtain the name.

Returns:  the name of the specified item

Return type:  str

Info(*idx*)[¶](#tts.core.api.comApi.Comserver.COMTestReport.Info "Link to this definition")  
returns the info field’s value of the item with the specified index.

Parameters:  **idx** (*int*) – the index of the item to obtain the info field.

Returns:  the info field’s value of the specified item

Return type:  str

IsOk()[¶](#tts.core.api.comApi.Comserver.COMTestReport.IsOk "Link to this definition")  
This method can be used to check if this test report is valid or more precisely the package was already executed and a test report is available.

Returns:  True, if this test report is valid, otherwise False. It is a convenience function for:

    GetCount() > 0

Return type:  bool

Item(*idx*)[¶](#tts.core.api.comApi.Comserver.COMTestReport.Item "Link to this definition")  
See: `Result`

Name(*idx*)[¶](#tts.core.api.comApi.Comserver.COMTestReport.Name "Link to this definition")  
returns the name of the item with the specified index.

Parameters:  **idx** (*int*) – the index of the item to obtain the name.

Returns:  the name of the specified item

Return type:  str

Result(*idx*)[¶](#tts.core.api.comApi.Comserver.COMTestReport.Result "Link to this definition")  
returns the result of the item with the specified index.

Parameters:  **idx** (*int*) – the index of the item to obtain the result.

Returns:  the result of the specified item

Return type:  str

TimeStamp(*idx*)[¶](#tts.core.api.comApi.Comserver.COMTestReport.TimeStamp "Link to this definition")  
returns the time stamp of the item with the specified index.

Parameters:  **idx** (*int*) – the index of the item to obtain the time stamp.

Returns:  the time stamp of the specified item

Return type:  str

## COMVariable[¶](#comvariable "Link to this heading")

*class* COMVariable[¶](#tts.core.api.comApi.Comserver.COMVariable "Link to this definition")  
This object gives access to the properties of a variable.

Description[¶](#tts.core.api.comApi.Comserver.COMVariable.Description "Link to this definition")  
returns the description of this variable.

Returns:  the description of this variable

Return type:  str

InitValue[¶](#tts.core.api.comApi.Comserver.COMVariable.InitValue "Link to this definition")  
returns the initial value of this variable as string.

Returns:  the initial value of this variable

Return type:  str

Name[¶](#tts.core.api.comApi.Comserver.COMVariable.Name "Link to this definition")  
returns the name of this variable.

Returns:  the name of this variable

Return type:  str

GetDescription()[¶](#tts.core.api.comApi.Comserver.COMVariable.GetDescription "Link to this definition")  
returns the description of this variable.

Returns:  the description of this variable

Return type:  str

GetInitValue()[¶](#tts.core.api.comApi.Comserver.COMVariable.GetInitValue "Link to this definition")  
returns the initial value of this variable as string.

Returns:  the initial value of this variable

Return type:  str

GetName()[¶](#tts.core.api.comApi.Comserver.COMVariable.GetName "Link to this definition")  
returns the name of this variable.

Returns:  the name of this variable

Return type:  str

IsInput()[¶](#tts.core.api.comApi.Comserver.COMVariable.IsInput "Link to this definition")  
Returns True if this variable is an input parameter, otherwise False.

Returns:  whether this variable is an input parameter or not

Return type:  bool

IsOutput()[¶](#tts.core.api.comApi.Comserver.COMVariable.IsOutput "Link to this definition")  
Returns True if this variable is an ouput parameter, otherwise False.

Returns:  whether this variable is an output parameter or not

Return type:  bool

## COMVariables[¶](#comvariables "Link to this heading")

*class* COMVariables[¶](#tts.core.api.comApi.Comserver.COMVariables "Link to this definition")  
This object gives access to all variable of a package in COM-Application.

Count[¶](#tts.core.api.comApi.Comserver.COMVariables.Count "Link to this definition")  
returns the number of variables.

Returns:  the number of variables.

Return type:  int

GetCount()[¶](#tts.core.api.comApi.Comserver.COMVariables.GetCount "Link to this definition")  
returns the number of variables.

Returns:  the number of variables.

Return type:  int

Item(*idxOrName*)[¶](#tts.core.api.comApi.Comserver.COMVariables.Item "Link to this definition")  
returns a specified variable. idxOrName can be either the name or an index. If an index is given then it should be larger than 0 and lesser the number of variables. The count of variables can be determined with `GetCount`

Parameters:  **idxOrName** – The name of the variable or an index

Returns:  the variable.

Return type:  [`COMVariable`](#tts.core.api.comApi.Comserver.COMVariable "tts.core.api.comApi.Comserver.COMVariable")
