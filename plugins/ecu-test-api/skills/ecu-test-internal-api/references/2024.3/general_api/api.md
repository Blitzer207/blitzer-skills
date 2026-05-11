# Internal APIs[¶](#internal-apis "Link to this heading")

## API entry point[¶](#api-entry-point "Link to this heading")

Entry point for the ecu.test Internal API. The Internal API can be used in many expression controls inside test steps and utilities by using `api.`

For using it inside function variables and other user code, the Internal API can be instantiated the following way:

    from tts.core.api.internalApi.Api import Api
    api = Api()

### API[¶](#module-tts.core.api.internalApi.Api "Link to this heading")

*class* Api[¶](#tts.core.api.internalApi.Api.Api "Link to this definition")  
Entry point for the Internal API.

AnalysisEnvironment[¶](#tts.core.api.internalApi.Api.Api.AnalysisEnvironment "Link to this definition")  
Object for the [`AnalysisEnvironment`](#tts.core.api.internalApi.AnalysisEnvironment.AnalysisEnvironment "tts.core.api.internalApi.AnalysisEnvironment.AnalysisEnvironment")

Credentials[¶](#tts.core.api.internalApi.Api.Api.Credentials "Link to this definition")  
Access to [`Credentials`](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials "tts.core.api.internalApi.credentialsApi.Credentials.Credentials") for handling Credentials such as certificates and private keys.

CurrentTestConfiguration[¶](#tts.core.api.internalApi.Api.Api.CurrentTestConfiguration "Link to this definition")  
Object for the [`TestConfiguration`](#tts.core.api.internalApi.TestConfiguration.TestConfiguration "tts.core.api.internalApi.TestConfiguration.TestConfiguration")

CurrentTestbenchConfiguration[¶](#tts.core.api.internalApi.Api.Api.CurrentTestbenchConfiguration "Link to this definition")  
Object for the [`TestbenchConfiguration`](#tts.core.api.internalApi.TestbenchConfiguration.TestbenchConfiguration "tts.core.api.internalApi.TestbenchConfiguration.TestbenchConfiguration")

DataBrowser[¶](#tts.core.api.internalApi.Api.Api.DataBrowser "Link to this definition")  
Object for the [`DataBrowser`](#tts.core.api.dataBrowserApi.DataBrowser.DataBrowser "tts.core.api.dataBrowserApi.DataBrowser.DataBrowser")

Ethernet[¶](#tts.core.api.internalApi.Api.Api.Ethernet "Link to this definition")  
Access to various [`Ethernet`](busdatastructures.md#tts.core.api.internalApi.Ethernet.Ethernet "tts.core.api.internalApi.Ethernet.Ethernet") related packet types

GlobalConstants[¶](#tts.core.api.internalApi.Api.Api.GlobalConstants "Link to this definition")  
Object for the [`GlobalConstants`](#tts.core.api.internalApi.GlobalConstants.GlobalConstants "tts.core.api.internalApi.GlobalConstants.GlobalConstants")

KeywordCatalog[¶](#tts.core.api.internalApi.Api.Api.KeywordCatalog "Link to this definition")  
Offers key word catalog access methods

Math[¶](#tts.core.api.internalApi.Api.Api.Math "Link to this definition")  
Object for [`Math`](#tts.core.api.internalApi.Math.Math "tts.core.api.internalApi.Math.Math")

Multimedia[¶](#tts.core.api.internalApi.Api.Api.Multimedia "Link to this definition")  
Object for [`MultimediaApi`](#tts.testModule.multimedia.api.MultimediaApi.MultimediaApi "tts.testModule.multimedia.api.MultimediaApi.MultimediaApi")

ObjectApi[¶](#tts.core.api.internalApi.Api.Api.ObjectApi "Link to this definition")  
Use this to access the [Object API](objectApi.md#objectapi) internally

Scm[¶](#tts.core.api.internalApi.Api.Api.Scm "Link to this definition")  
Object for [`Scm`](#tts.core.api.internalApi.Scm.Scm "tts.core.api.internalApi.Scm.Scm")

Service[¶](#tts.core.api.internalApi.Api.Api.Service "Link to this definition")  
Object for [`Service`](#tts.core.api.internalApi.Service.Service "tts.core.api.internalApi.Service.Service")

TestBench[¶](#tts.core.api.internalApi.Api.Api.TestBench "Link to this definition")  
Provides access to the [`TestBench`](#tts.core.api.internalApi.TestBench.TestBench "tts.core.api.internalApi.TestBench.TestBench")

TestEnvironment[¶](#tts.core.api.internalApi.Api.Api.TestEnvironment "Link to this definition")  
Object for the [`TestEnvironment`](#tts.core.api.internalApi.TestEnvironment.TestEnvironment "tts.core.api.internalApi.TestEnvironment.TestEnvironment")

TestGuideApiClient[¶](#tts.core.api.internalApi.Api.Api.TestGuideApiClient "Link to this definition")  
Object for [`TestGuideApiClient`](#tts.core.api.internalApi.TestGuideApiClient.TestGuideApiClient "tts.core.api.internalApi.TestGuideApiClient.TestGuideApiClient")

TestManagement[¶](#tts.core.api.internalApi.Api.Api.TestManagement "Link to this definition")  
Object for the [`TestManagementApi`](#tts.core.api.internalApi.TestManagement.TestManagementApi "tts.core.api.internalApi.TestManagement.TestManagementApi")

UnitInfo[¶](#tts.core.api.internalApi.Api.Api.UnitInfo "Link to this definition")  
Object for the [`UnitInfo`](#tts.core.api.dataBrowserApi.UnitInfo.UnitInfo "tts.core.api.dataBrowserApi.UnitInfo.UnitInfo")

GeneratePackageDocumentation(*pkgPath*, *docPath*, *doasync=True*)[¶](#tts.core.api.internalApi.Api.Api.GeneratePackageDocumentation "Link to this definition")  
Creates documentation file(s) for a package or all packages in a folder depending on the given path

Parameters:  - **pkgPath** (*str*) – Path of either a package or a folder containing packages

- **docPath** (*str*) – Path where the documentation files will be created

- **doasync** (*bool*) – Mode of execution: asynchronous if True otherwise synchronous

Returns:  Path of the generated (index) document if synchronous mode, otherwise None

Return type:  str or None

GetSetting(*value*)[¶](#tts.core.api.internalApi.Api.Api.GetSetting "Link to this definition")  
Returns a value from the settings file. Possible values are:

- configPath

- errorLogFile

- generatorPath

- imagePath

- language

- logFile

- offlineFiuPath

- offlineModelPath

- offlineSgbdPath

- packagePath

- parameterPath

- reportPath

- settingsPath

- templatePath

- traceFileDir

- traceStepPath

- userPyModulesPath

- utilityPath

- workspacePath

Parameters:  **value** (*str*) – The setting to return

Returns:  The current value

Return type:  str or None

GetVersion()[¶](#tts.core.api.internalApi.Api.Api.GetVersion "Link to this definition")  
Returns the ecu.test version.

Return type:  str

## API classes[¶](#api-classes "Link to this heading")

### AnalysisEnvironment[¶](#analysisenvironment "Link to this heading")

*class* AnalysisEnvironment[¶](#tts.core.api.internalApi.AnalysisEnvironment.AnalysisEnvironment "Link to this definition")  
Object of analysis job procedure engine.

ExecutionInfo[¶](#tts.core.api.internalApi.AnalysisEnvironment.AnalysisEnvironment.ExecutionInfo "Link to this definition")  
The current [`AnalysisExecutionInfo`](#tts.core.api.internalApi.AnalysisExecutionInfo.AnalysisExecutionInfo "tts.core.api.internalApi.AnalysisExecutionInfo.AnalysisExecutionInfo") object.

Type:  list

ClearSignalCache()[¶](#tts.core.api.internalApi.AnalysisEnvironment.AnalysisEnvironment.ClearSignalCache "Link to this definition")  
Removes all signals from the signal cache.

Note

Calling this method can be useful in large projects analyzing many object signals (signals that are not of a primitive data type). Object signals are cached in memory. Thus, if the analyses of the project access different object signals, the memory consumption is continuously increasing. Calling this method frees all the memory consumed by the signal cache.

This method should be called at some point in the project, when it is known that most of the previously used signals are not required anymore for the following analyses or if the memory consumption has to be reduced. Calling this method too often, has a negative effect on the execution time.

In order to ensure that the signal cache is cleared completely, this method should be called in a separate episode or the test case part of a package.

### AnalysisExecutionInfo[¶](#analysisexecutioninfo "Link to this heading")

*class* AnalysisExecutionInfo[¶](#tts.core.api.internalApi.AnalysisExecutionInfo.AnalysisExecutionInfo "Link to this definition")  
Provides information for current analysis job execution

JobResult[¶](#tts.core.api.internalApi.AnalysisExecutionInfo.AnalysisExecutionInfo.JobResult "Link to this definition")  
The result of the current analysis job

Note

During job execution only completed episodes (and child trace steps) are considered. This means, the results of assertions and other steps above an episode are not considered.

Type:  str

LogFolder[¶](#tts.core.api.internalApi.AnalysisExecutionInfo.AnalysisExecutionInfo.LogFolder "Link to this definition")  
Folder where trace and logging files of the current analysis job are saved during execution

Note

This may be a temporary location, in case a network drive is used. [`TargetReportDbFolder`](#tts.core.api.internalApi.AnalysisExecutionInfo.AnalysisExecutionInfo.TargetReportDbFolder "tts.core.api.internalApi.AnalysisExecutionInfo.AnalysisExecutionInfo.TargetReportDbFolder") may be used to deduce the final location from the final report location.

Type:  str

ReportDb[¶](#tts.core.api.internalApi.AnalysisExecutionInfo.AnalysisExecutionInfo.ReportDb "Link to this definition")  
Path to report database of current (or most recent) analysis job execution

Type:  str

ReportDbFolder[¶](#tts.core.api.internalApi.AnalysisExecutionInfo.AnalysisExecutionInfo.ReportDbFolder "Link to this definition")  
Folder of the report database of the current analysis job during execution

Note

This may be a temporary location, in case a network drive is used. [`TargetReportDbFolder`](#tts.core.api.internalApi.AnalysisExecutionInfo.AnalysisExecutionInfo.TargetReportDbFolder "tts.core.api.internalApi.AnalysisExecutionInfo.AnalysisExecutionInfo.TargetReportDbFolder") returns the final location instead.

Type:  str

StartTime[¶](#tts.core.api.internalApi.AnalysisExecutionInfo.AnalysisExecutionInfo.StartTime "Link to this definition")  
Time where the current analysis job execution began

Type:  str

TargetReportDbFolder[¶](#tts.core.api.internalApi.AnalysisExecutionInfo.AnalysisExecutionInfo.TargetReportDbFolder "Link to this definition")  
Folder of the report database of the current analysis job execution after job completion.

Note

Trace and logging files may be located in the respective subfolders. In case a network drive is used, a temporary location is used during execution that is returned by [`ReportDbFolder`](#tts.core.api.internalApi.AnalysisExecutionInfo.AnalysisExecutionInfo.ReportDbFolder "tts.core.api.internalApi.AnalysisExecutionInfo.AnalysisExecutionInfo.ReportDbFolder").

Type:  str

GetCurrentPackageFilename()[¶](#tts.core.api.internalApi.AnalysisExecutionInfo.AnalysisExecutionInfo.GetCurrentPackageFilename "Link to this definition")  
Returns the path to the package containing the episode that is currently running

Returns:  Path to the package

Return type:  str

GetMainPackageFilename()[¶](#tts.core.api.internalApi.AnalysisExecutionInfo.AnalysisExecutionInfo.GetMainPackageFilename "Link to this definition")  
Returns the path to the main package

Returns:  Path to the main package

Return type:  str

GetWatchTime(*key='DefaultWatch'*)[¶](#tts.core.api.internalApi.AnalysisExecutionInfo.AnalysisExecutionInfo.GetWatchTime "Link to this definition")  
Returns the difference between the current time and the start of a watch

Parameters:  **key** – The identifier of the watch

Returns:  The time difference [ms]

Return type:  int

StartWatch(*key='DefaultWatch'*)[¶](#tts.core.api.internalApi.AnalysisExecutionInfo.AnalysisExecutionInfo.StartWatch "Link to this definition")  
Starts a watch or resets an existing watch

Parameters:  **key** (*str*) – The identifier of the watch

### BusSystem[¶](#bussystem "Link to this heading")

*class* BusSystem[¶](#tts.core.api.internalApi.BusSystem.BusSystem "Link to this definition")  
A Bus system

Channel[¶](#tts.core.api.internalApi.BusSystem.BusSystem.Channel "Link to this definition")  
The channel

Type:  str

Database[¶](#tts.core.api.internalApi.BusSystem.BusSystem.Database "Link to this definition")  
The filename

Type:  str

Name[¶](#tts.core.api.internalApi.BusSystem.BusSystem.Name "Link to this definition")  
The name

Type:  str

### BusSystems[¶](#bussystems "Link to this heading")

*class* BusSystems[¶](#tts.core.api.internalApi.BusSystems.BusSystems "Link to this definition")  
Container for BusSystems. Item Type: [`BusSystem`](#module-tts.core.api.internalApi.BusSystem "tts.core.api.internalApi.BusSystem")

Count[¶](#tts.core.api.internalApi.BusSystems.BusSystems.Count "Link to this definition")  
The number of items in the collection

Type:  int

Item(*idx*)[¶](#tts.core.api.internalApi.BusSystems.BusSystems.Item "Link to this definition")  
Returns the item at the specified index

Parameters:  **idx** (*int*) – The index

Returns:  The item at index *idx*

Return type:  object

### Constant[¶](#constant "Link to this heading")

*class* Constant[¶](#tts.core.api.internalApi.Constant.Constant "Link to this definition")  
A global constant

Description[¶](#tts.core.api.internalApi.Constant.Constant.Description "Link to this definition")  
Returns the description of this constant

Type:  str

Name[¶](#tts.core.api.internalApi.Constant.Constant.Name "Link to this definition")  
Returns the name of this constant

Type:  str

Value[¶](#tts.core.api.internalApi.Constant.Constant.Value "Link to this definition")  
Returns the defined value of this constant

Type:  str

### Constants[¶](#constants "Link to this heading")

*class* Constants[¶](#tts.core.api.internalApi.Constants.Constants "Link to this definition")  
Container for Constants. Item Type: [`Constant`](#module-tts.core.api.internalApi.Constant "tts.core.api.internalApi.Constant")

Count[¶](#tts.core.api.internalApi.Constants.Constants.Count "Link to this definition")  
The number of items in the collection

Type:  int

Item(*idx*)[¶](#tts.core.api.internalApi.Constants.Constants.Item "Link to this definition")  
Returns the item at the specified index

Parameters:  **idx** (*int*) – The index

Returns:  The item at index *idx*

Return type:  object

### Ecu[¶](#ecu "Link to this heading")

*class* Ecu[¶](#tts.core.api.internalApi.Ecu.Ecu "Link to this definition")  
An ECU

A2l[¶](#tts.core.api.internalApi.Ecu.Ecu.A2l "Link to this definition")  
The filename of the A2L file

Type:  str

DebugHex[¶](#tts.core.api.internalApi.Ecu.Ecu.DebugHex "Link to this definition")  
The filename of the debugger HEX file

Type:  str

Elf[¶](#tts.core.api.internalApi.Ecu.Ecu.Elf "Link to this definition")  
The filename of the ELF file

Type:  str

Elfs[¶](#tts.core.api.internalApi.Ecu.Ecu.Elfs "Link to this definition")  
The filenames of the ELF files

Type:  str

Hex[¶](#tts.core.api.internalApi.Ecu.Ecu.Hex "Link to this definition")  
The filename of the HEX file

Type:  str

Name[¶](#tts.core.api.internalApi.Ecu.Ecu.Name "Link to this definition")  
The name

Type:  str

Sgbd[¶](#tts.core.api.internalApi.Ecu.Ecu.Sgbd "Link to this definition")  
The filename of the SGBD file

Type:  str

### Ecus[¶](#ecus "Link to this heading")

*class* Ecus[¶](#tts.core.api.internalApi.Ecus.Ecus "Link to this definition")  
Container for Ecus. Item Type: [`Ecu`](#module-tts.core.api.internalApi.Ecu "tts.core.api.internalApi.Ecu")

Count[¶](#tts.core.api.internalApi.Ecus.Ecus.Count "Link to this definition")  
The number of items in the collection

Type:  int

Item(*idx*)[¶](#tts.core.api.internalApi.Ecus.Ecus.Item "Link to this definition")  
Returns the item at the specified index

Parameters:  **idx** (*int*) – The index

Returns:  The item at index *idx*

Return type:  object

### EnvironmentCommunication[¶](#environmentcommunication "Link to this heading")

*class* EnvironmentCommunication[¶](#tts.testModule.envCom.internalApi.EnvironmentCommunication.EnvironmentCommunication "Link to this definition")  
An environment communication system

Name[¶](#tts.testModule.envCom.internalApi.EnvironmentCommunication.EnvironmentCommunication.Name "Link to this definition")  
The name

Type:  str

### EnvironmentCommunications[¶](#environmentcommunications "Link to this heading")

*class* EnvironmentCommunications[¶](#tts.testModule.envCom.internalApi.EnvironmentCommunications.EnvironmentCommunications "Link to this definition")  
Container for environment communication systems. Item Type: [`EnvironmentCommunication`](#module-tts.testModule.envCom.internalApi.EnvironmentCommunication "tts.testModule.envCom.internalApi.EnvironmentCommunication")

Count[¶](#tts.testModule.envCom.internalApi.EnvironmentCommunications.EnvironmentCommunications.Count "Link to this definition")  
The number of items in the collection

Type:  int

Item(*idx*)[¶](#tts.testModule.envCom.internalApi.EnvironmentCommunications.EnvironmentCommunications.Item "Link to this definition")  
Returns the item at the specified index

Parameters:  **idx** (*int*) – The index

Returns:  The item at index *idx*

Return type:  object

### EnvironmentSimulation[¶](#environmentsimulation "Link to this heading")

*class* EnvironmentSimulation[¶](#tts.testModule.envSim.internalApi.EnvironmentSimulation.EnvironmentSimulation "Link to this definition")  
An environment simulation system

Name[¶](#tts.testModule.envSim.internalApi.EnvironmentSimulation.EnvironmentSimulation.Name "Link to this definition")  
The name

Type:  str

OfflineFile[¶](#tts.testModule.envSim.internalApi.EnvironmentSimulation.EnvironmentSimulation.OfflineFile "Link to this definition")  
The offline file

Type:  str

### EnvironmentSimulations[¶](#environmentsimulations "Link to this heading")

*class* EnvironmentSimulations[¶](#tts.testModule.envSim.internalApi.EnvironmentSimulations.EnvironmentSimulations "Link to this definition")  
Container for environment simulation systems. Item Type: [`EnvironmentSimulation`](#module-tts.testModule.envSim.internalApi.EnvironmentSimulation "tts.testModule.envSim.internalApi.EnvironmentSimulation")

Count[¶](#tts.testModule.envSim.internalApi.EnvironmentSimulations.EnvironmentSimulations.Count "Link to this definition")  
The number of items in the collection

Type:  int

Item(*idx*)[¶](#tts.testModule.envSim.internalApi.EnvironmentSimulations.EnvironmentSimulations.Item "Link to this definition")  
Returns the item at the specified index

Parameters:  **idx** (*int*) – The index

Returns:  The item at index *idx*

Return type:  object

### GlobalConstants[¶](#globalconstants "Link to this heading")

*class* GlobalConstants[¶](#tts.core.api.internalApi.GlobalConstants.GlobalConstants "Link to this definition")  
This class represents a container for holding global constants. Use:

    GlobalConstants.YourConstantName

to get the value of any self defined constant.

GetConstant(*name*, *default=NOT_SET*)[¶](#tts.core.api.internalApi.GlobalConstants.GlobalConstants.GetConstant "Link to this definition")  
Returns the value of the given constant

Parameters:  - **default** – The default value to return if the constant does not exists. If this is not set, an exception is raised in this case.

- **name** (*str*) – The name of the constants to retrieve the value

Returns:  The value of the constant

Return type:  *Any*

GetConstants()[¶](#tts.core.api.internalApi.GlobalConstants.GlobalConstants.GetConstants "Link to this definition")  
Returns a list of names containing all constants defined in this container

Returns:  A list of names

Return type:  list[str]

ORIGIN_DEFINED_AT_RUNTIME *= 'defined at runtime'*[¶](#tts.core.api.internalApi.GlobalConstants.ORIGIN_DEFINED_AT_RUNTIME "Link to this definition")  

ORIGIN_MANIPULATED_AT_RUNTIME *= 'manipulated at runtime'*[¶](#tts.core.api.internalApi.GlobalConstants.ORIGIN_MANIPULATED_AT_RUNTIME "Link to this definition")  

### KeywordCatalog[¶](#keywordcatalog "Link to this heading")

*class* KeywordCatalogApi[¶](#tts.core.api.internalApi.KeywordCatalogApi.KeywordCatalogApi "Link to this definition")  
Internal API for keyword catalog accesses

Connect()[¶](#tts.core.api.internalApi.KeywordCatalogApi.KeywordCatalogApi.Connect "Link to this definition")  
Tries to establish a connection to the keyword catalog server defined in the workspace settings

Returns:  The connection state: True if the connection has been established, else False

Return type:  bool

GetAvailableCatalogs()[¶](#tts.core.api.internalApi.KeywordCatalogApi.KeywordCatalogApi.GetAvailableCatalogs "Link to this definition")  
Returns the available catalogs of the current project

Returns:  List of available catalog names

Return type:  list\<str\>

GetAvailableProjects()[¶](#tts.core.api.internalApi.KeywordCatalogApi.KeywordCatalogApi.GetAvailableProjects "Link to this definition")  
Returns the available projects

Returns:  List of available project names

Return type:  list\<str\>

GetAvailableVariants()[¶](#tts.core.api.internalApi.KeywordCatalogApi.KeywordCatalogApi.GetAvailableVariants "Link to this definition")  
Returns the available variants

Returns:  List of available variant names

Return type:  list\<str\>

GetCurrentCatalogName()[¶](#tts.core.api.internalApi.KeywordCatalogApi.KeywordCatalogApi.GetCurrentCatalogName "Link to this definition")  
Returns the name of the loaded keyword catalog or None, if no catalog has been loaded

Returns:  Name of current catalog or None

Return type:  str or None

GetCurrentProject()[¶](#tts.core.api.internalApi.KeywordCatalogApi.KeywordCatalogApi.GetCurrentProject "Link to this definition")  
Returns the name of the current project or None, if no project has been configured

Returns:  Current project name or None

Return type:  str or None

GetCurrentVariant()[¶](#tts.core.api.internalApi.KeywordCatalogApi.KeywordCatalogApi.GetCurrentVariant "Link to this definition")  
Returns the name of the current variant or None, if no variant has been configured

Returns:  Current variant name or None

Return type:  str or None

IsConnected()[¶](#tts.core.api.internalApi.KeywordCatalogApi.KeywordCatalogApi.IsConnected "Link to this definition")  
Returns the connection state to the keyword catalog server

Returns:  True, if the connection has already been established, else False

Return type:  bool

LoadCatalog(*catalogName*)[¶](#tts.core.api.internalApi.KeywordCatalogApi.KeywordCatalogApi.LoadCatalog "Link to this definition")  
Loads the referenced catalog

Parameters:  **catalogName** (*str*) – Name of the catalog

Raises:  
**exception** – If an invalid catalog name has been referenced

SetProject(*projectName*)[¶](#tts.core.api.internalApi.KeywordCatalogApi.KeywordCatalogApi.SetProject "Link to this definition")  
Sets the referenced project

Parameters:  **projectName** (*str*) – Project name

Raises:  
**exception** – If an invalid project name has been referenced

SetVariant(*variantName*)[¶](#tts.core.api.internalApi.KeywordCatalogApi.KeywordCatalogApi.SetVariant "Link to this definition")  
Sets the referenced variant

Parameters:  **variantName** (*str*) – Variant name

Raises:  
**exception** – If an invalid variant name has been referenced

### Math[¶](#id16 "Link to this heading")

*class* Math[¶](#tts.core.api.internalApi.Math.Math "Link to this definition")  
Functions for Math

*static* RandomValue(*value*, *absTolerance*, *stepSize=0*)[¶](#tts.core.api.internalApi.Math.Math.RandomValue "Link to this definition")  
Evaluates a random value around a center

Parameters:  - **value** (*float*) – Center for the range of possible values

- **absTolerance** (*float*) – Tolerance for the used value range (must be \>= 0)

- **stepSize** (*float*) – Step size which is used to partition the value range (0 for continous distribution (must be \>= 0))

Returns:  Random value (value - absTolerance \<= returnValue \<= value + absTolerance)

Return type:  float

*static* RandomValueMinMax(*minValue*, *maxValue*, *stepSize=0*, *includeMinValue=True*, *includeMaxValue=False*)[¶](#tts.core.api.internalApi.Math.Math.RandomValueMinMax "Link to this definition")  
Evaluates a random value in the from minValue to maxValue. It can be parameterized whether the interval includes minValue (default True) and maxValue (default False).

Parameters:  - **minValue** (*float*) – Center for the range of possible values

- **maxValue** (*float*) – Tolerance for the used value range (must be \>= 0)

- **stepSize** (*float*) – Step size which is used to partition the value range (0 for continous distribution (must be \>= 0))

- **includeMinValue** (*bool*) – True if the minValue should be part of the distribution values (closed interval), else False.

- **includeMaxValue** – True if the maxValue should be part of the distribution values (closed interval), else False.

- **includeMaxValue** – bool

Returns:  Random value (minValue \<= returnValue \<= maxValue)

Return type:  float

### Model[¶](#model "Link to this heading")

*class* Model[¶](#tts.core.api.internalApi.Model.Model "Link to this definition")  
A Model

Name[¶](#tts.core.api.internalApi.Model.Model.Name "Link to this definition")  
The name

Type:  str

### Models[¶](#models "Link to this heading")

*class* Models[¶](#tts.core.api.internalApi.Models.Models "Link to this definition")  
Container for Models. Item Type: [`Model`](#module-tts.core.api.internalApi.Model "tts.core.api.internalApi.Model")

Count[¶](#tts.core.api.internalApi.Models.Models.Count "Link to this definition")  
The number of items in the collection

Type:  int

Item(*idx*)[¶](#tts.core.api.internalApi.Models.Models.Item "Link to this definition")  
Returns the item at the specified index

Parameters:  **idx** (*int*) – The index

Returns:  The item at index *idx*

Return type:  object

### Multimedia[¶](#multimedia "Link to this heading")

Entry point in the internal api for multimedia content

*class* ImageFiltersApi[¶](#tts.testModule.multimedia.api.MultimediaApi.ImageFiltersApi "Link to this definition")  
Provides access to image filters. Filters are grouped into the two namespaces `default` and `user`. The following filters are provided by ecu.test out of the box:

- `default.BlurFilter(image, Type='GAUSS', Kernelsize=15)`- `default.BWFilter(image, Threshold=-1)`- `default.ColorFilter(image, Colors=["#ff0000"], Tolerance=5)`- `default.ContrastFilter(image, Contrast=1, Brightness=0)`- `default.HSVFilter(image, Hue=0, Saturation=1, Value=1)`- `default.InvertFilter(image)`

- `default.RotationFilter(image, Angle=90)`To call a filter you can pass an image object as first argument, followed by any parameter the filter expects. Note that the filter parameters must be passed as keyword arguments. They cannot be passed as positional arguments. If a parameter is omitted it will be filled with its default value. For example to increase the brightness of an image:

    >>> filteredImage = api.Multimedia.ImageFilters.default.ContrastFilter(image, Brightness=100)

Any user-defined image filter will appear under the namespace `user`. Suppose you implemented a custom filter and placed it in the UserPyModules directory. The filter could then be accessed via `api.Multimedia.ImageFilters.user.MyCustomFilter`.

Note that all filters will show up in a flat list without accounting for any file system hierarchies. For example a filter located at “UserPyModules/My Image Filters/MyCustomFilter.py” will still show up as `user.MyCustomFilter`. Therefore please make sure that your filters use unique module names in order to avoid name clashes.

*class* MultimediaApi[¶](#tts.testModule.multimedia.api.MultimediaApi.MultimediaApi "Link to this definition")  
Provides access to multimedia content at runtime

ImageFilters[¶](#tts.testModule.multimedia.api.MultimediaApi.MultimediaApi.ImageFilters "Link to this definition")  
Object for [`ImageFiltersApi`](#tts.testModule.multimedia.api.MultimediaApi.ImageFiltersApi "tts.testModule.multimedia.api.MultimediaApi.ImageFiltersApi")

Type:  list

GetAvailableOCRServices()[¶](#tts.testModule.multimedia.api.MultimediaApi.MultimediaApi.GetAvailableOCRServices "Link to this definition")  
Returns a list of available OCR services. These identifiers can be used with GetOCRService.

Returns:  A list of OCR service identifiers

Return type:  list\<str\>

GetAvailableSTTProfiles()[¶](#tts.testModule.multimedia.api.MultimediaApi.MultimediaApi.GetAvailableSTTProfiles "Link to this definition")  
Returns the currently available profiles for speech-to-text.

Returns:  A list of profile dictionaries containing the configured serviceId, profileName, language for each profile.

Return type:  list\<dict\<str:str\>\>

GetAvailableTTSVoices()[¶](#tts.testModule.multimedia.api.MultimediaApi.MultimediaApi.GetAvailableTTSVoices "Link to this definition")  
Gets the currently available voices for text-to-speech output.

Returns:  Returns a list of voice dictionaries containing the configured serviceId, voiceName, voiceLanguage, voiceGender for each voice.

Return type:  list\<dict\<str:str\>\>

GetDefaultOCRService(*sut=None*)[¶](#tts.testModule.multimedia.api.MultimediaApi.MultimediaApi.GetDefaultOCRService "Link to this definition")  
Returns the OCR service that is configured in the active test configuration.

Parameters:  **sut** (*str* *|* *None*) – The system under test whose OCR service should be created. Can be omitted if only one system for media access exists.

Returns:  A new OCR service instance configured according to the test configuration

Return type:  [OCRService](mediadatastructures.md#tts.lib.ocr.OCRService.OCRService "tts.lib.ocr.OCRService.OCRService")

GetOCRService(*serviceId*)[¶](#tts.testModule.multimedia.api.MultimediaApi.MultimediaApi.GetOCRService "Link to this definition")  
Creates a new OCR service instance from a given sevice ID.

Parameters:  **serviceId** (*str*) – Identifier of the OCR service to be created

Returns:  A new OCR service instance

Return type:  [OCRService](mediadatastructures.md#tts.lib.ocr.OCRService.OCRService "tts.lib.ocr.OCRService.OCRService")

SpeechToText(*audioBlock*, *profile=None*)[¶](#tts.testModule.multimedia.api.MultimediaApi.MultimediaApi.SpeechToText "Link to this definition")  
Converts voice to text. Returns the recognized text as a string.

Parameters:  - **audioBlock** ([*AudioBlock*](mediadatastructures.md#tts.testModule.multimedia.dataElements.AudioBlock.AudioBlock "tts.testModule.multimedia.dataElements.AudioBlock.AudioBlock")) – The audio recording that should be converted to text.

- **profile** (*dict*) – The profile to be used for speech recognition, identified by a dictionary containing `serviceId`, `profileName` and `language`. See [`GetAvailableSTTProfiles()`](#tts.testModule.multimedia.api.MultimediaApi.MultimediaApi.GetAvailableSTTProfiles "tts.testModule.multimedia.api.MultimediaApi.MultimediaApi.GetAvailableSTTProfiles") for a list of valid values. If no profile is provided, the default profile that is configured in the test configuration will be used.

Returns:  The recognized text

Return type:  str

TextToSpeech(*text*, *voice=None*, *parameters=None*)[¶](#tts.testModule.multimedia.api.MultimediaApi.MultimediaApi.TextToSpeech "Link to this definition")  
Converts text to speech. Returns the spoken text as an AudioBlock.

Parameters:  - **text** (*str*) – The text that should be converted to speech

- **voice** (*dict*) – The voice to use for speech generation, identified by a dictionary containing `serviceId`, `voiceName`, `voiceLanguage` and `voiceGender`. See [`GetAvailableTTSVoices()`](#tts.testModule.multimedia.api.MultimediaApi.MultimediaApi.GetAvailableTTSVoices "tts.testModule.multimedia.api.MultimediaApi.MultimediaApi.GetAvailableTTSVoices") for a list of valid values. If no voice is provided, the default voice from the current test configuration will be used.

- **parameters** (*dict*) – Optional dictionary with parameters for speech generation. For example the default parameters are `{'pitch': 0, 'speed': 1}`Returns:  
An AudioBlock containing the spoken text

Return type:  [AudioBlock](mediadatastructures.md#tts.testModule.multimedia.dataElements.AudioBlock.AudioBlock "tts.testModule.multimedia.dataElements.AudioBlock.AudioBlock")

### Scm[¶](#scm "Link to this heading")

*class* Scm[¶](#tts.core.api.internalApi.Scm.Scm "Link to this definition")  
Functions for SCM

GetCheckoutRevision()[¶](#tts.core.api.internalApi.Scm.Scm.GetCheckoutRevision "Link to this definition")  
Returns the revision number of the actual workspace repository

Returns:  - The revision of the actual workspace repository

- An empty string if the workspace is not versioned

- None if SCM is not available or not enabled in the user settings

Return type:  str or None

GetFileRevision(*filename*)[¶](#tts.core.api.internalApi.Scm.Scm.GetFileRevision "Link to this definition")  
Returns the revision number of a given file

Parameters:  **filename** (*str*) – Path to the file. Relative paths will be evaluated as relative to the workspace directory.

Returns:  - The revision of the file, e.g. u”8524” or u”8524m” for a locally modified file

- An empty string if the file does not exist or is not versioned

- None if SCM is not available or not enabled in the user settings

Return type:  str or None

GetFileStatus(*filename*)[¶](#tts.core.api.internalApi.Scm.Scm.GetFileStatus "Link to this definition")  
Returns the status of a given file

Parameters:  **filename** (*str*) – Path to the file. Relative paths will be evaluated as relative to the workspace directory

Returns:  - The SCM status of the file for a locally modified file

- An empty string if the file does not exist or is not versioned

- None if SCM is not available or not enabled in the user settings

Return type:  str or None

GetUrl()[¶](#tts.core.api.internalApi.Scm.Scm.GetUrl "Link to this definition")  
Returns the SCM-URL of the workspace directory

Returns:  - The URL of the workspace

- None if SCM is not available or not enabled in the user settings

Return type:  str or None

### Service[¶](#service "Link to this heading")

Entry point in the internal api for the Ethernet RBS

*class* Service[¶](#tts.core.api.internalApi.Service.Service "Link to this definition")  
Provides access to simulated Ethernet Services at runtime

GenerateService(*systemIdentifier*, *ecuName*, *serviceName*, *projectName=''*)[¶](#tts.core.api.internalApi.Service.Service.GenerateService "Link to this definition")  
Generates a service module for `systemIdentifier`, `ecuName` and `serviceName`

Parameters:  - **systemIdentifier** (*str*) – System identifier

- **ecuName** (*str*) – Ecu name

- **serviceName** (*str*) – Service name

- **projectName** (*str*) – Optional project name

GetPort(*portName*)[¶](#tts.core.api.internalApi.Service.Service.GetPort "Link to this definition")  
Returns a service port for the given port name

Parameters:  **portName** (*str*) – Port identifier according to TBC

Returns:  Service Port

Return type:  [ServicePort](#tts.core.api.internalApi.Service.ServicePort "tts.core.api.internalApi.Service.ServicePort")

*static* GetUsedServices(*systemIdentifier=None*, *excludeRecordingOnlyMappings=True*)[¶](#tts.core.api.internalApi.Service.Service.GetUsedServices "Link to this definition")  
Returns all SystemIdentifiers, EcuNames and ServiceNames used in the current test execution

Parameters:  - **systemIdentifier** (*str* *or* *None*) – Filter Mappings for given SystemIdentifier (default=None)

- **excludeRecordingOnlyMappings** (*boolean*) – Ignore Mappings which are exclusively used for recording (default=True)

Returns:  A set of tuples containing SystemIdentifier, EcuName and ServiceName

Return type:  set[tuple[str, str, str]]

*class* ServicePort[¶](#tts.core.api.internalApi.Service.ServicePort "Link to this definition")  
Functions for Ports in the context of simulated Ethernet Services

GetService(*serviceName*)[¶](#tts.core.api.internalApi.Service.ServicePort.GetService "Link to this definition")  
Returns a proxy to the service identified by `serviceName`

Parameters:  **serviceName** (*str*) – Service identifier is a composition of optional projectName and ecuName and serviceName in the format [projectName.]\<ecuName\>\_\<serviceName\>

Returns:  Service Proxy

Return type:  [ServiceProxy](#tts.core.api.internalApi.Service.ServiceProxy "tts.core.api.internalApi.Service.ServiceProxy")

StartService(*serviceName*)[¶](#tts.core.api.internalApi.Service.ServicePort.StartService "Link to this definition")  
Starts the service identified by `serviceName` on this port

Parameters:  **serviceName** (*str*) – Service identifier is a composition of optional projectName and ecuName and serviceName in the format [projectName.]\<ecuName\>\_\<serviceName\>

StopService(*serviceName*)[¶](#tts.core.api.internalApi.Service.ServicePort.StopService "Link to this definition")  
Stops the service identified by `serviceName` on this port

Parameters:  **serviceName** (*str*) – service identifier is a composition of optional projectName and ecuName and serviceName in the format [projectName.]\<ecuName\>\_\<serviceName\>

*class* ServiceProxy[¶](#tts.core.api.internalApi.Service.ServiceProxy "Link to this definition")  
Service proxy for a running simulated Ethernet Service. Service methods can be called on this object, and will be executed on the service instance.

*static* GetFunctionsHelp(*name*, *serviceName*)[¶](#tts.core.api.internalApi.Service.ServiceProxy.GetFunctionsHelp "Link to this definition")  
Provides the docstring of a function of the service simulation

Parameters:  - **name** (*str*) – Name of function

- **serviceName** (*str*) – Service identifier is a composition of optional projectName and ecuName and serviceName in the format [projectName.]\<ecuName\>\_\<serviceName\>

Return type:  str

*static* GetServiceFunctions(*serviceName*)[¶](#tts.core.api.internalApi.Service.ServiceProxy.GetServiceFunctions "Link to this definition")  
Provides available functions of a service simulation

Parameters:  **serviceName** (*str*) – Service identifier is a composition of optional projectName and ecuName and serviceName in the format [projectName.]\<ecuName\>\_\<serviceName\>

Return type:  list[str]

### TestBench[¶](#testbench "Link to this heading")

*class* TestBench[¶](#tts.core.api.internalApi.TestBench.TestBench "Link to this definition")  
Entry point for starting/stopping tools

GetPortStatus(*portName*)[¶](#tts.core.api.internalApi.TestBench.TestBench.GetPortStatus "Link to this definition")  
Retrieves the status of the port.

Parameters:  **portName** (*str*) – Name of the port as shown in the “Host / Tool / Port” column in the test bench configuration editor (e.g. “MDL-DEFAULT01”)

Returns:  Status of the port

- 0 (Stopped, shown gray in the tool status monitor)

- 1 (Started, shown green in the tool status monitor)

- 2 (Broken, shown red in the tool status monitor)

Return type:  int

GetToolStatus(*toolId*)[¶](#tts.core.api.internalApi.TestBench.TestBench.GetToolStatus "Link to this definition")  
Retrieves the status of the tool.

Parameters:  **toolId** (*str*) – ID of the tool as shown in the tooltip in the test bench configuration editor (e.g. “CONTROLDESKNG01”)

Returns:  Status of the tool

- 0 (Stopped, shown gray in the tool status monitor)

- 1 (Started, shown green in the tool status monitor)

- 2 (Broken, shown red in the tool status monitor)

Return type:  int

StartTool(*toolId*)[¶](#tts.core.api.internalApi.TestBench.TestBench.StartTool "Link to this definition")  
Starts the specified tool

Note

This is not the recommended way of changing the status of connected tools. Instead, a configuration change step in a project should be used.

Warning

Updates variable descriptions. Because signals are registered during test case initialization, accessing signals provided by a tool started via this method is in most cases not possible within the same test case.

Parameters:  **toolId** (*str*) – ID of the tool as shown in the ToolTip in the testbench configuration editor (e.g. CONTROLDESKNG01)

Returns:  True if the tool was started successfully or had been started already, else False

Return type:  bool

StopTool(*toolId*)[¶](#tts.core.api.internalApi.TestBench.TestBench.StopTool "Link to this definition")  
Stops the specified tool.

Note

This is not the recommended way of changing the status of connected tools. Instead, a configuration change step in a project should be used.

Warning

Unloads the model description assigned to the ports of the stopped tool. Can break mapping and timestamp streaming within the same test case.

Any subsequent access to the tool, both explicitly by a test step and implicitly by cleanup for previous test steps, can lead to completely unpredictable behavior after this call.

Parameters:  **toolId** (*str*) – ID of the tool as shown in the ToolTip in the testbench configuration editor (e.g. CONTROLDESKNG01)

Returns:  True if the tool was stopped successfully, had been stopped already or had never been started in the first place, else False

Return type:  bool

### TestbenchConfiguration[¶](#testbenchconfiguration "Link to this heading")

*class* TestbenchConfiguration[¶](#tts.core.api.internalApi.TestbenchConfiguration.TestbenchConfiguration "Link to this definition")  
Object for accessing information about test bench configuration

Filename[¶](#tts.core.api.internalApi.TestbenchConfiguration.TestbenchConfiguration.Filename "Link to this definition")  
The filename of the test bench configuration

Type:  str

ToolList[¶](#tts.core.api.internalApi.TestbenchConfiguration.TestbenchConfiguration.ToolList "Link to this definition")  
List containing objects of type [`TestbenchTool`](#tts.core.api.internalApi.TestbenchTool.TestbenchTool "tts.core.api.internalApi.TestbenchTool.TestbenchTool")

Type:  list([`TestbenchTool`](#tts.core.api.internalApi.TestbenchTool.TestbenchTool "tts.core.api.internalApi.TestbenchTool.TestbenchTool"))

GetToolhostInfo()[¶](#tts.core.api.internalApi.TestbenchConfiguration.TestbenchConfiguration.GetToolhostInfo "Link to this definition")  
Returns a list of lists containing url, version, revision and loaded patches of all connected toolhosts

Returns:  List of lists containing toolhost information

Return type:  list\<list\>

### TestbenchTool[¶](#testbenchtool "Link to this heading")

*class* TestbenchTool[¶](#tts.core.api.internalApi.TestbenchTool.TestbenchTool "Link to this definition")  
Provides information about the respective tool in the test bench configuration

Location[¶](#tts.core.api.internalApi.TestbenchTool.TestbenchTool.Location "Link to this definition")  
Location (host) of the tool

Type:  str

Name[¶](#tts.core.api.internalApi.TestbenchTool.TestbenchTool.Name "Link to this definition")  
Name of the tool

Type:  str

Ports[¶](#tts.core.api.internalApi.TestbenchTool.TestbenchTool.Ports "Link to this definition")  
Ports of the tool

Type:  list\<str\>

ToolId[¶](#tts.core.api.internalApi.TestbenchTool.TestbenchTool.ToolId "Link to this definition")  
ID of the tool

Type:  str

Version[¶](#tts.core.api.internalApi.TestbenchTool.TestbenchTool.Version "Link to this definition")  
Version of an activated tool (if known)

Type:  str/None

### TestConfiguration[¶](#id25 "Link to this heading")

*class* TestConfiguration[¶](#tts.core.api.internalApi.TestConfiguration.TestConfiguration "Link to this definition")  
Object for accessing information about test configuration

Note

For most properties it is enough to have the test configuration selected and not loaded.

BusSystems[¶](#tts.core.api.internalApi.TestConfiguration.TestConfiguration.BusSystems "Link to this definition")  
Collection for [`BusSystems`](#tts.core.api.internalApi.BusSystems.BusSystems "tts.core.api.internalApi.BusSystems.BusSystems")

Type:  list

Ecus[¶](#tts.core.api.internalApi.TestConfiguration.TestConfiguration.Ecus "Link to this definition")  
Collection for [`Ecus`](#tts.core.api.internalApi.Ecus.Ecus "tts.core.api.internalApi.Ecus.Ecus")

Type:  list

EnvironmentCommunications[¶](#tts.core.api.internalApi.TestConfiguration.TestConfiguration.EnvironmentCommunications "Link to this definition")  
Collection for [`EnvironmentCommunications`](#module-tts.testModule.envCom.internalApi.EnvironmentCommunications "tts.testModule.envCom.internalApi.EnvironmentCommunications")

Type:  list

EnvironmentSimulations[¶](#tts.core.api.internalApi.TestConfiguration.TestConfiguration.EnvironmentSimulations "Link to this definition")  
Collection for [`EnvironmentSimulations`](#module-tts.testModule.envSim.internalApi.EnvironmentSimulations "tts.testModule.envSim.internalApi.EnvironmentSimulations")

Type:  list

Filename[¶](#tts.core.api.internalApi.TestConfiguration.TestConfiguration.Filename "Link to this definition")  
Absolute path of the test configuration

Type:  str

GlobalConstants[¶](#tts.core.api.internalApi.TestConfiguration.TestConfiguration.GlobalConstants "Link to this definition")  
Collection for [`Constants`](#tts.core.api.internalApi.Constants.Constants "tts.core.api.internalApi.Constants.Constants")

Note

Test configuration has to be loaded.

Type:  list

Models[¶](#tts.core.api.internalApi.TestConfiguration.TestConfiguration.Models "Link to this definition")  
Collection for [`Models`](#tts.core.api.internalApi.Models.Models "tts.core.api.internalApi.Models.Models")

Type:  list

NameTester[¶](#tts.core.api.internalApi.TestConfiguration.TestConfiguration.NameTester "Link to this definition")  
Name of the tester

Type:  str

ReloadGlobalMapping()[¶](#tts.core.api.internalApi.TestConfiguration.TestConfiguration.ReloadGlobalMapping "Link to this definition")  
Reloads the global mapping from the test configuration without reloading the whole configuration

Note

Closed files are loaded, changed files are reloaded, additional files are unloaded.

Note

Calling this method has no effect on the package from which it is called but only on subsequent packages.

Warning

Changes in unsaved loaded mapping files are discarded when calling this method!

### TestEnvironment[¶](#testenvironment "Link to this heading")

*class* TestEnvironment[¶](#tts.core.api.internalApi.TestEnvironment.TestEnvironment "Link to this definition")  
Object of test procedure engine

ExecutionInfo[¶](#tts.core.api.internalApi.TestEnvironment.TestEnvironment.ExecutionInfo "Link to this definition")  
The current [`TestExecutionInfo`](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo "tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo") object

GenerateTestReportDocumentFromDB(*dbFile*, *outDir*, *fmtName=None*, *waitUntilFinished=False*, *fmtConfig=None*)[¶](#tts.core.api.internalApi.TestEnvironment.TestEnvironment.GenerateTestReportDocumentFromDB "Link to this definition")  
Generates a handler-based test report on the filesystem

Parameters:  - **dbFile** (*str*) – Path to the report database file (.trf)

- **outDir** (*str*) – The output directory. Absolute or relative to the program’s report directory

- **fmtName** (*str*) – Name of the report format or handler which should be used (optional) (default is HTML)

- **waitUntilFinished** (*boolean*) – Defines whether the API call should block until generation is finished

- **fmtConfig** (*dict\<str,* *str\>*) – Optional dictionary {name: value} of additional configuration parameters for the report format

GetPackageReferences(*filePath*, *skipDisabled=True*)[¶](#tts.core.api.internalApi.TestEnvironment.TestEnvironment.GetPackageReferences "Link to this definition")  
Gives a set of all referenced sub packages of this package or project depending on the actual configuration

Parameters:  - **filePath** (*str*) – Path of package or project (relative to the package directory or absolute)

- **skipDisabled** (*boolean*) – Flag to include disabled test steps or not

Returns:  List of package references with absolute file path

Return type:  list\<str\>

TimeElapsing()[¶](#tts.core.api.internalApi.TestEnvironment.TestEnvironment.TimeElapsing "Link to this definition")  
Resumes a stepwise simulation time when entering the context manager. Pauses the simulation time on context manager exit. This requires that a test execution is running. Does have no effect in real time or continuous simulation time.

Returns:  The context manager.

Return type:  Iterator[None]

Wait(*seconds*)[¶](#tts.core.api.internalApi.TestEnvironment.TestEnvironment.Wait "Link to this definition")  
Waits the given number of seconds in the currently selected time mode. This requires that a test execution is running.

Returns:  True if wait completed. False if test execution is not active or wait has been aborted.

Return type:  bool

### TestExecutionInfo[¶](#testexecutioninfo "Link to this heading")

*class* ExecutionExceptionInfo[¶](#tts.core.api.internalApi.TestExecutionInfo.ExecutionExceptionInfo "Link to this definition")  
Provides information about an exception that has happened during test execution

GetMessage()[¶](#tts.core.api.internalApi.TestExecutionInfo.ExecutionExceptionInfo.GetMessage "Link to this definition")  
Returns the message of the exception

Returns:  The message of the exception

Return type:  str

GetTestStepPortId()[¶](#tts.core.api.internalApi.TestExecutionInfo.ExecutionExceptionInfo.GetTestStepPortId "Link to this definition")  
Returns the ID (alias) of the port that was used by the test step that caused the exception

Returns:  - The port alias

- None, if the test step did not refer to any port

Return type:  str or None

GetTestStepToolId()[¶](#tts.core.api.internalApi.TestExecutionInfo.ExecutionExceptionInfo.GetTestStepToolId "Link to this definition")  
Returns the ID (alias) of the tool that was used by the test step that caused the exception

Returns:  - The tool alias

- None, if the test step did not refer to any tool

Return type:  str or None

GetTestStepType()[¶](#tts.core.api.internalApi.TestExecutionInfo.ExecutionExceptionInfo.GetTestStepType "Link to this definition")  
Returns the name of the test step type

Returns:  The name of the test step type

Return type:  str

GetType()[¶](#tts.core.api.internalApi.TestExecutionInfo.ExecutionExceptionInfo.GetType "Link to this definition")  
Returns the name of the exception type

Returns:  The name of the exception type

Return type:  str

*class* KeywordInfo[¶](#tts.core.api.internalApi.TestExecutionInfo.KeywordInfo "Link to this definition")  
KeywordInfo provides an interface to query properties of the currently executed keyword teststep

GetArgumentUnit(*argName*)[¶](#tts.core.api.internalApi.TestExecutionInfo.KeywordInfo.GetArgumentUnit "Link to this definition")  
Returns the unit of the given argument configured in the test step

Parameters:  **argName** (*str*) – The name of the desired argument

Returns:  Unit of the return parameter

Return type:  str

GetArguments()[¶](#tts.core.api.internalApi.TestExecutionInfo.KeywordInfo.GetArguments "Link to this definition")  
Returns a list of all arguments

Returns:  All arguments

Return type:  list\<str\>

GetComponentType()[¶](#tts.core.api.internalApi.TestExecutionInfo.KeywordInfo.GetComponentType "Link to this definition")  
Returns the component type

Returns:  The component type

Return type:  str

GetCurrentTimeOptionIteration()[¶](#tts.core.api.internalApi.TestExecutionInfo.KeywordInfo.GetCurrentTimeOptionIteration "Link to this definition")  
Returns the repetition count of the execution implementation

Returns:  The repetition count

Return type:  int

GetId()[¶](#tts.core.api.internalApi.TestExecutionInfo.KeywordInfo.GetId "Link to this definition")  
Returns the keyword ID

Returns:  The keyword ID or None

Return type:  int or None

GetReturnUnit(*retName=None*)[¶](#tts.core.api.internalApi.TestExecutionInfo.KeywordInfo.GetReturnUnit "Link to this definition")  
Returns the unit of the given return parameter configured in the test step

Parameters:  **retName** (*str* *or* *None*) – The name of the desired return parameter or None if only one exists

Returns:  Unit of the return parameter or None

Return type:  str or None

GetReturns()[¶](#tts.core.api.internalApi.TestExecutionInfo.KeywordInfo.GetReturns "Link to this definition")  
Returns a list all return parameters

Returns:  All return parameters

Return type:  list\<str\>

GetTimeOptionDuration(*asUnit=None*)[¶](#tts.core.api.internalApi.TestExecutionInfo.KeywordInfo.GetTimeOptionDuration "Link to this definition")  
Returns the minimum duration of the configured time option or None if not set

Parameters:  **asUnit** (*str* *('ms',* *'s',* *'min',* *'h',* *'d')*) – Return the value in the desired unit. Default is None, the value as it is.

Returns:  The minimum duration value

Return type:  int or float

GetTimeOptionMode()[¶](#tts.core.api.internalApi.TestExecutionInfo.KeywordInfo.GetTimeOptionMode "Link to this definition")  
Returns the mode of the configured time option or None if time option is not set

Returns:  Mode of the time option

- Finally

- TrueForWithin

- Generally

- SyncOnly

Return type:  str or None

GetTimeOptionPollingCycle(*asUnit=None*)[¶](#tts.core.api.internalApi.TestExecutionInfo.KeywordInfo.GetTimeOptionPollingCycle "Link to this definition")  
Returns the polling cycle of the configured time option or None if not set

Parameters:  **asUnit** (*str* *('ms',* *'s',* *'min',* *'h',* *'d')*) – Return the value in the desired unit. Default is None, the value as it is.

Returns:  The polling cycle value

Return type:  int or float

GetTimeOptionTimeout(*asUnit=None*)[¶](#tts.core.api.internalApi.TestExecutionInfo.KeywordInfo.GetTimeOptionTimeout "Link to this definition")  
Returns the timeout of the configured time option or None if not set

Parameters:  **asUnit** (*str* *('ms',* *'s',* *'min',* *'h',* *'d')*) – Return the value in the desired unit. Default is None, the value as it is.

Returns:  The timeout value

Return type:  int or float

IsControlTestStep()[¶](#tts.core.api.internalApi.TestExecutionInfo.KeywordInfo.IsControlTestStep "Link to this definition")  
Returns True, if the keyword test step is of type control

Returns:  True, if the test step is of type control else False

Return type:  bool

IsEstablishTestStep()[¶](#tts.core.api.internalApi.TestExecutionInfo.KeywordInfo.IsEstablishTestStep "Link to this definition")  
Returns True, if the keyword test step is of type establish

Returns:  True, if the test step is of type establish else False

Return type:  bool

IsStateTestStep()[¶](#tts.core.api.internalApi.TestExecutionInfo.KeywordInfo.IsStateTestStep "Link to this definition")  
Returns True, if the keyword test step is of type state

Returns:  True, if the test step is of type state else False

Return type:  bool

*class* TestExecutionInfo[¶](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo "Link to this definition")  
Provides information for current test execution

AllProjectsStepCount[¶](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.AllProjectsStepCount "Link to this definition")  
Total number of project execution steps, including separately executed sub-projects

Type:  int

AllProjectsStepsExecuted[¶](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.AllProjectsStepsExecuted "Link to this definition")  
Number of completed project execution steps, including separately executed sub-projects

Type:  int

CurrentLineNumber[¶](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.CurrentLineNumber "Link to this definition")  
Line number of the current teststep

Type:  int

CurrentTestStepHierarchy[¶](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.CurrentTestStepHierarchy "Link to this definition")  
Current test step’s hierarchy including all parents’ line numbers (e.g. ‘3/4/17’)

Type:  str

KeywordInfo[¶](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.KeywordInfo "Link to this definition")  
The information object of the current keyword call

Type:  [`KeywordInfo`](#tts.core.api.internalApi.TestExecutionInfo.KeywordInfo "tts.core.api.internalApi.TestExecutionInfo.KeywordInfo")

LastTestStepResult[¶](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.LastTestStepResult "Link to this definition")  
Testresult of the last executed teststep in the same teststep hierarchy

Type:  str

LogFolder[¶](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.LogFolder "Link to this definition")  
Folder where trace and logging files of the current main package are saved during execution

Note

This may be a temporary location, in case a network drive is used. [`TargetReportDbFolder`](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.TargetReportDbFolder "tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.TargetReportDbFolder") may be used to deduce the final location from the final report location.

Type:  str

MainProjectStepCount[¶](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.MainProjectStepCount "Link to this definition")  
Total number of project execution steps, excluding separately executed sub-projects

Type:  int

MainProjectStepsExecuted[¶](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.MainProjectStepsExecuted "Link to this definition")  
Number of completed project execution steps, excluding separately executed sub-projects

Type:  int

PackageResult[¶](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.PackageResult "Link to this definition")  
The result of the current package

Type:  str

ProjectResult[¶](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.ProjectResult "Link to this definition")  
The result of the current project

Type:  str

ProjectStartTime[¶](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.ProjectStartTime "Link to this definition")  
Time where the current project execution began

Type:  float

ReportDb[¶](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.ReportDb "Link to this definition")  
Path to report database of current (or most recent) test run

Type:  str

ReportDbFolder[¶](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.ReportDbFolder "Link to this definition")  
Folder of the report database of the current test run during execution

Note

This may be a temporary location, in case a network drive is used. [`TargetReportDbFolder`](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.TargetReportDbFolder "tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.TargetReportDbFolder") returns the final report location instead.

Type:  str

RunningTime[¶](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.RunningTime "Link to this definition")  
Difference between the current time and the start of the testexecution

Type:  int

StartTime[¶](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.StartTime "Link to this definition")  
Time where the current testexecution began

Type:  float

TargetReportDbFolder[¶](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.TargetReportDbFolder "Link to this definition")  
Folder of the report database of the current main package after completion of the package run

Note

Trace and logging files may be located in the respective subfolders. In case a network drive is used, a temporary location is used during execution that is returned by [`ReportDbFolder`](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.ReportDbFolder "tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.ReportDbFolder").

Type:  str

AddArtifact(*fileName=None*, *filePath=''*, *context=None*)[¶](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.AddArtifact "Link to this definition")  
Adds an artifact reference to the test report.

Parameters:  - **fileName** (*str* *or* *None*) – File name of the artifact

- **filePath** (*str*) – Path or URI to the artifact. If the file is accessible on the local file system, a md5 hashsum will be calculated. The prefix ‘report://’ denotes a relative path within the current report directory. To copy a file to this location use the [`TargetReportDbFolder`](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.TargetReportDbFolder "tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.TargetReportDbFolder") property.

- **context** (*str* *or* *None*) – Additional context / comment for the artifact.

AddTestStepReportDetail(*text*)[¶](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.AddTestStepReportDetail "Link to this definition")  
Adds a text to the “custom data” section of the currently running teststep’s report details

Note

The entry will be added with a leading time stamp of the test execution. This feature is only available within a package execution. When used within a project step (e.g. a project generator) an error will be raised.

Parameters:  **text** (*str*) – The text to be added in the report details

GetCurrentPackageFilename()[¶](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.GetCurrentPackageFilename "Link to this definition")  
Returns the file name of the current subpackage

Note

Infos of Packages executed in parallel are not returned.

Returns:  File name of current subpackage file or an empty string if the Package is not saved

Return type:  str

GetCurrentPackagePath()[¶](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.GetCurrentPackagePath "Link to this definition")  
Returns the absolute file system path of the current subpackage

Note

Infos of Packages executed in parallel are not returned.

Returns:  - Absolute path of current subpackage file

- An empty string if the Package is not saved

Return type:  str

GetCurrentProjectFilename()[¶](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.GetCurrentProjectFilename "Link to this definition")  
Returns the file name of the current project

Returns:  - File name of current project

- An empty string, if the project has not been saved yet

- None, if no project is running

Return type:  str or None

GetCurrentProjectPath()[¶](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.GetCurrentProjectPath "Link to this definition")  
Returns the absolute file system path of the current project

Returns:  - Absolute path of the current project

- An empty string, if the project has not been saved yet

- None, if no project is running

Return type:  str or None

GetExecutionExceptionInfo()[¶](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.GetExecutionExceptionInfo "Link to this definition")  
Returns a list of exceptions that have occured during the execution of this package. This information is also available in error recovery packages.

Returns:  A list of exception info objects

Return type:  list\<[`ExecutionExceptionInfo`](#tts.core.api.internalApi.TestExecutionInfo.ExecutionExceptionInfo "tts.core.api.internalApi.TestExecutionInfo.ExecutionExceptionInfo")\>

GetKeywordInfo()[¶](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.GetKeywordInfo "Link to this definition")  
Returns an information object of the current executed keyword call

Returns:  The information object of the current keyword call

Return type:  [`KeywordInfo`](#tts.core.api.internalApi.TestExecutionInfo.KeywordInfo "tts.core.api.internalApi.TestExecutionInfo.KeywordInfo")

GetMainPackageFilename()[¶](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.GetMainPackageFilename "Link to this definition")  
Returns the file name of the running main package

Returns:  - File name of current main package file

- An empty string if the package is not saved

Return type:  str

GetMainPackagePath()[¶](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.GetMainPackagePath "Link to this definition")  
Returns the absolute file system path of the running main package

Returns:  - Absolute path of current main package file

- An empty string if package is not saved

Return type:  str

GetMappingNames()[¶](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.GetMappingNames "Link to this definition")  
Returns a list of all available mappings in the current package.

Note

This function is not supported in parallel packages.

Returns:  Mapping names in the running package

Return type:  list[str]

GetMappingTargetPath(*mappingName*)[¶](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.GetMappingTargetPath "Link to this definition")  
Returns the target path of the mapping with the given name

Note

This function is not supported in parallel packages.

Parameters:  **mappingName** (*str*) – Name of the mapping

Returns:  - The target path of the mapping

- None, if it is a generic mapping

Return type:  str or None

GetWatchTime(*key='DefaultWatch'*)[¶](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.GetWatchTime "Link to this definition")  
Returns the difference between the current time and the start of a watch

Returns:  The time difference [ms]

Return type:  int

IsAbortRequested()[¶](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.IsAbortRequested "Link to this definition")  
Returns True if the user has requested an abort.

Note

This method should be used to check if an abort is requested in long-running implementations (e.g. in UserPyModules, generators, package inline code or utility implementations) in order to abort this routine. Returns False if the abort of an execution has already been completed.

Returns:  True if the user has requested an abort else False.

Return type:  bool

IsAborted()[¶](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.IsAborted "Link to this definition")  
Returns True if a package or project is aborted.

Returns:  True if abort is sent by a package or project.

Return type:  bool

IsInMain()[¶](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.IsInMain "Link to this definition")  
Checks if execution is currently neither in a pre- nor a postcondition block

Returns:  True, if the currently executed test step is not in a pre- or postcondition block else False

Return type:  bool

IsInPostcondition()[¶](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.IsInPostcondition "Link to this definition")  
Checks if execution is currently in postcondition block

Returns:  True, if a postcondition block is currently executed else False

Return type:  bool

IsInPrecondition()[¶](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.IsInPrecondition "Link to this definition")  
Checks if execution is currently in precondition block

Returns:  True, if a precondition block is currently executed else False

Return type:  bool

IsInteractiveExecution()[¶](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.IsInteractiveExecution "Link to this definition")  
Checks if test is executed interactively

Returns:  - True, if test is executed interactively

- False, if test is not executed interactively

- None, if no execution is running

Return type:  bool or None

StartWatch(*key='DefaultWatch'*)[¶](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.StartWatch "Link to this definition")  
Start a watch or reset an existing watch

Parameters:  **key** (*str*) – The indentifier of the watch

### TestGuideApiClient[¶](#testguideapiclient "Link to this heading")

*class* TestGuideApiClient[¶](#tts.core.api.internalApi.TestGuideApiClient.TestGuideApiClient "Link to this definition")  
API Client for test.guide Functions

ExecutionApi[¶](#tts.core.api.internalApi.TestGuideApiClient.TestGuideApiClient.ExecutionApi "Link to this definition")  
Object for [`ExecutionApi`](#tts.core.api.internalApi.testGuideApi.ExecutionApi.ExecutionApi "tts.core.api.internalApi.testGuideApi.ExecutionApi.ExecutionApi")

### TestGuideExecutionApi[¶](#module-tts.core.api.internalApi.testGuideApi.ExecutionApi "Link to this heading")

*class* ExecutionApi[¶](#tts.core.api.internalApi.testGuideApi.ExecutionApi.ExecutionApi "Link to this definition")  
API Client for test.guide Execution API Functions

UploadPlaybook(*playbookJsonDict*)[¶](#tts.core.api.internalApi.testGuideApi.ExecutionApi.ExecutionApi.UploadPlaybook "Link to this definition")  
Upload a new playbook

Parameters:  **playbookJsonDict** (*Dict*) – JSON dictionary representing the playbook

### TestManagement[¶](#module-tts.core.api.internalApi.TestManagement "Link to this heading")

*class* TestManagementApi[¶](#tts.core.api.internalApi.TestManagement.TestManagementApi "Link to this definition")  
API to interact with the configured test management system.

Note

Test management must be configured and already successfully authenticated.

GetTestScriptByID(*testScriptId*)[¶](#tts.core.api.internalApi.TestManagement.TestManagementApi.GetTestScriptByID "Link to this definition")  
Queries a test script by its ID. The returned data object corresponds to the interface of almhooks.

Parameters:  **testScriptId** (*str*) – String value of the identifer, e.g.: “42” or “TT-1234”

Returns:  Data object of the Almhook Interface representing a test script.

Return type:  TestScript

## Credentials API[¶](#credentials-api "Link to this heading")

### Introduction[¶](#module-tts.core.api.internalApi.credentialsApi.Credentials "Link to this heading")

The credentials API can be used to manage and access credentials such as certificates and private keys.

#### Keystores[¶](#keystores "Link to this heading")

Certificates and private keys are stored in keystores, e.g. PKCS12 files. These keystores are meant to prevent direct access to especially private keys. For example, PKCS12 files can be encrypted by a password to protect the private key from simple plaintext access via the file system.

#### Managing Keystores[¶](#managing-keystores "Link to this heading")

Keystores can be created or loaded in the central vault of ecu.test to access them later within a test case, e.g. via path and the password of a PKCS12 file via CreatePkcs12KeyStore and LoadPkcs12KeyStore. The vault is encrypted and secured by a central password that must be provided by the user to decrypt and gain access to the saved keystores - similar to the concept of a password manager.

#### Accessing Keystores[¶](#accessing-keystores "Link to this heading")

Previously created or loaded keystores can be simply accessed as attribute or by GetVaultEntry:

    >>> api.Credentials.OpenCryptFileVault(...)
    >>> api.Credentials.CreatePkcs12KeyStore("myKeyStore", ...)
    >>> ...
    >>> api.Credentials.myKeyStore.GetPrivateKey()
    >>> api.Credentials.GetVaultEntry("myKeyStore").GetCertificates()

#### Secrets[¶](#secrets "Link to this heading")

Simple secrets such as strings or byte streams can be stored directly in the vault. Analogously to keystores, they can be accessed as attribute or by GetVaultEntry:

    >>> api.Credentials.OpenCryptFileVault(...)
    >>> api.Credentials.CreateSecret("secret", "e25f790f00e553b82592626a2a948a64", "accessToken")
    >>> ...
    >>> api.Credentials.secret.Reveal()
    'e25f790f00e553b82592626a2a948a64'
    >>> api.Credentials.GetVaultEntry("secret").AssociatedData()
    'accessToken'

#### Managing the Vault[¶](#managing-the-vault "Link to this heading")

Currently, the central vault is a password encrypted file containing the access data to the different keystores. One can simply create a vault by CreateCryptFileVault or load an existing one by OpenCryptFileVault. The central password for opening the vault can be provided directly or by password prompt.

#### Security[¶](#security "Link to this heading")

See security notes

Warning

Providing the password directly via API can currently reveal the central password by reporting. To circumvent reporting, it is advised to use the credentials API within function variables or UserPyModules.

#### Examples[¶](#examples "Link to this heading")

Creating a vault:

    >>> api.Credentials.CreateCryptFileVault("C:/<path>/vault")
    >>> api.Credentials.Close()

Creating a PKCS12 keystore:

    >>> api.Credentials.OpenCryptFileVault("C:/<path>/vault")
    >>> pkcs = "C:/<path>/service29.pkcs"
    >>> privateKey = "C:/<path>/private.key"
    >>> certs = ["C:/<path>/Service29.crt"]
    >>> api.Credentials.CreatePkcs12KeyStore("service29", pkcs, privateKey, certs)
    >>> api.Credentials.Save()
    >>> api.Credentials.Close()

Accessing keystores:

    >>> # Assuming the vault has been opened beforehand
    >>> privateKey = api.Credentials.service29.GetPrivateKey()
    >>> cert = api.Credentials.service29.GetCertificate("SERVICE-29")  # common name SERVICE-29
    >>> signature = privateKey.Sign(ByteStream(b"message"))
    >>> cert.Verify(signature, ByteStream(b"message"))
    True
    >>> cert.Verify(signature, ByteStream(b"nonsense"))
    False

### Credentials[¶](#credentials "Link to this heading")

*class* Credentials[¶](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials "Link to this definition")  
Access to the Credentials API

Certificate[¶](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials.Certificate "Link to this definition")  
Returns Certificate API for utility methods.

Return type:  [`Certificate`](#tts.core.api.internalApi.credentialsApi.Certificate.Certificate "tts.core.api.internalApi.credentialsApi.Certificate.Certificate")

ChangeLoginCredentials(*old=None*, *new=None*)[¶](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials.ChangeLoginCredentials "Link to this definition")  
Changes the login credentials (vault password). If a credential is not given, it will be actively prompted.

Parameters:  - **old** (*str* *|* *None*) – Old vault password.

- **new** (*str* *|* *None*) – New vault password.

Close()[¶](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials.Close "Link to this definition")  
Closes the vault. Unsaved modifications will be discarded!

CreateCryptFileVault(*path*, *vaultPassword=None*)[¶](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials.CreateCryptFileVault "Link to this definition")  
Creates a new crypt file vault. After that the new vault will be open.

Parameters:  - **path** (*str*) – The path of the vault. This path can be relative to the workspace or absolute.

- **vaultPassword** (*str* *|* *None*) – The password of the vault. If no password is given, it will be actively prompted.

CreatePkcs12KeyStore(*identifier*, *filePath*, *privateKey=None*, *certs=None*, *password=''*)[¶](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials.CreatePkcs12KeyStore "Link to this definition")  
Creates the PKCS12 file with its given path, private key, certificates and password. The created PKC12 file is stored afterward.

Parameters:  - **identifier** (*str*) – This identifier will be used to reference the created keystore. The identifier has to be a valid python variable name without leading underscores.

- **filePath** (*str*) – The path of the PKCS12 file to be created.

- **privateKey** (*str* *|* *None*) – Path to the private key that will be stored in the PKCS12 file. If not given, the PKCS12 file will be created without a private key.

- **certs** (*list[str]* *|* *None*) – Certificates that will be stored in the PKCS12 file. The certificates can be given as files paths or standard base64 encoded strings. Additionally, they have to be ordered as certificate chain. If not given, the PKCS12 file will be created without certificates.

- **password** (*str*) – Password for accessing the PKCS12 file. If the PKCS12 file shall not be password protected, just choose an empty password.

Return type:  [`KeyStore`](#tts.core.api.internalApi.credentialsApi.KeyStore.KeyStore "tts.core.api.internalApi.credentialsApi.KeyStore.KeyStore")

CreateSecret(*identifier*, *secret*, *associatedData=None*)[¶](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials.CreateSecret "Link to this definition")  
Creates and saves the secret with its associated data.

Parameters:  - **identifier** (*str*) – This identifier will be used to reference the created keystore. The identifier has to be a valid python variable name without leading underscores.

- **secret** (*str*) – The secret to be stored, e.g. passwords, tokens.

- **associatedData** (*Any*) – Additional data associated with the secret. Data has to be JSON serializable.

Return type:  [`Secret`](#tts.core.api.internalApi.credentialsApi.Secret.Secret "tts.core.api.internalApi.credentialsApi.Secret.Secret")

DeleteVaultEntry(*identifier*)[¶](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials.DeleteVaultEntry "Link to this definition")  
Deletes the vault entry with the given identifier.

GetAvailableVaultEntries()[¶](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials.GetAvailableVaultEntries "Link to this definition")  
Returns all available vault entry identifiers.

Return type:  list[str]

GetVaultEntry(*identifier*)[¶](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials.GetVaultEntry "Link to this definition")  
Returns the vault entry with the given identifier.

Returns:  Returns vault entry if existent, otherwise None

Return type:  [*KeyStore*](#tts.core.api.internalApi.credentialsApi.KeyStore.KeyStore "tts.core.api.internalApi.credentialsApi.KeyStore.KeyStore") | [*Secret*](#tts.core.api.internalApi.credentialsApi.Secret.Secret "tts.core.api.internalApi.credentialsApi.Secret.Secret") | None

LoadPkcs12KeyStore(*identifier*, *filePath*, *password=''*)[¶](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials.LoadPkcs12KeyStore "Link to this definition")  
Loads and stores an existing PKCS12 file given by its path and password.

Parameters:  - **identifier** (*str*) – This identifier will be used to reference the created keystore. The identifier has to be a valid python variable name without leading underscores.

- **filePath** (*str*) – The path of the PKCS12 file.

- **password** (*str*) – Password for accessing the PKCS12 file. If the PKCS12 file is not password protected, just choose an empty password.

Return type:  [`KeyStore`](#tts.core.api.internalApi.credentialsApi.KeyStore.KeyStore "tts.core.api.internalApi.credentialsApi.KeyStore.KeyStore")

OpenCryptFileVault(*path*, *vaultPassword=None*)[¶](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials.OpenCryptFileVault "Link to this definition")  
Opens the crypt file vault. The vault can only be modified if it has been opened.

Parameters:  - **path** (*str*) – The path of the vault. This path can be relative to the workspace or absolute.

- **vaultPassword** (*str* *|* *None*) – The password of the vault. If no password is given, it will be actively prompted.

OpenVault(*vaultPassword=None*)[¶](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials.OpenVault "Link to this definition")  
Opens the vault that is configured in credential settings. The vault can only be modified if it has been opened.

Parameters:  **vaultPassword** (*str* *|* *None*) – The password of the vault. If no password is given, it will be actively prompted.

PublicKey[¶](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials.PublicKey "Link to this definition")  
Returns PublicKey API for utility methods.

Return type:  [`PublicKey`](#tts.core.api.internalApi.credentialsApi.PublicKey.PublicKey "tts.core.api.internalApi.credentialsApi.PublicKey.PublicKey")

Save()[¶](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials.Save "Link to this definition")  
Saves all modifications.

### KeyStore[¶](#keystore "Link to this heading")

*class* KeyStore[¶](#tts.core.api.internalApi.credentialsApi.KeyStore.KeyStore "Link to this definition")  
Keystore for saving credentials.

Delete()[¶](#tts.core.api.internalApi.credentialsApi.KeyStore.KeyStore.Delete "Link to this definition")  
Deletes the vault entry.

GetCertificate(*name*)[¶](#tts.core.api.internalApi.credentialsApi.KeyStore.KeyStore.GetCertificate "Link to this definition")  
Returns the certificate with the given name. For PKCS12 files the common name of the certificate is used as identifier.

Parameters:  **name** (*str*) – The name of the certificate that will be used to identify it.

Return type:  [`Certificate`](#tts.core.api.internalApi.credentialsApi.Certificate.Certificate "tts.core.api.internalApi.credentialsApi.Certificate.Certificate")

GetCertificateChain(*name*)[¶](#tts.core.api.internalApi.credentialsApi.KeyStore.KeyStore.GetCertificateChain "Link to this definition")  
Returns the certificate chain for the certificate with the given name. For PKCS12 files the common name of the certificate is used as identifier.

Parameters:  **name** (*str*) – The name of the certificate that will be used to identify it.

Return type:  list[[`Certificate`](#tts.core.api.internalApi.credentialsApi.Certificate.Certificate "tts.core.api.internalApi.credentialsApi.Certificate.Certificate")]

GetCertificates()[¶](#tts.core.api.internalApi.credentialsApi.KeyStore.KeyStore.GetCertificates "Link to this definition")  
Returns all stored certificates.

Return type:  list[[`Certificate`](#tts.core.api.internalApi.credentialsApi.Certificate.Certificate "tts.core.api.internalApi.credentialsApi.Certificate.Certificate")]

GetPrivateKey()[¶](#tts.core.api.internalApi.credentialsApi.KeyStore.KeyStore.GetPrivateKey "Link to this definition")  
Returns the private key.

Return type:  [`PrivateKey`](#tts.core.api.internalApi.credentialsApi.PrivateKey.PrivateKey "tts.core.api.internalApi.credentialsApi.PrivateKey.PrivateKey") | None

### Secret[¶](#secret "Link to this heading")

*class* Secret[¶](#tts.core.api.internalApi.credentialsApi.Secret.Secret "Link to this definition")  

AssociatedData()[¶](#tts.core.api.internalApi.credentialsApi.Secret.Secret.AssociatedData "Link to this definition")  
Additional data associated with the secret.

Delete()[¶](#tts.core.api.internalApi.credentialsApi.Secret.Secret.Delete "Link to this definition")  
Deletes the vault entry.

Reveal()[¶](#tts.core.api.internalApi.credentialsApi.Secret.Secret.Reveal "Link to this definition")  
Returns the stored secret.

Return type:  str

### Certificate[¶](#certificate "Link to this heading")

*class* Certificate[¶](#tts.core.api.internalApi.credentialsApi.Certificate.Certificate "Link to this definition")  

CommonName()[¶](#tts.core.api.internalApi.credentialsApi.Certificate.Certificate.CommonName "Link to this definition")  
Return the common name of this certificate.

Return type:  str

DER()[¶](#tts.core.api.internalApi.credentialsApi.Certificate.Certificate.DER "Link to this definition")  
Return the certificate as bytes in DER format.

Return type:  [`ByteStream`](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream")

*classmethod* FromBase64(*data*)[¶](#tts.core.api.internalApi.credentialsApi.Certificate.Certificate.FromBase64 "Link to this definition")  
Create certificate object from base64 encoded data.

Parameters:  **data** (*str*) – Base64 encoded content

Return type:  [`Certificate`](#tts.core.api.internalApi.credentialsApi.Certificate.Certificate "tts.core.api.internalApi.credentialsApi.Certificate.Certificate")

*classmethod* FromFile(*filePath*)[¶](#tts.core.api.internalApi.credentialsApi.Certificate.Certificate.FromFile "Link to this definition")  
Creates a Certificate instance from a PEM or DER formatted file.

Parameters:  **filePath** (*str*) – Path of certificate file.

Return type:  [`Certificate`](#tts.core.api.internalApi.credentialsApi.Certificate.Certificate "tts.core.api.internalApi.credentialsApi.Certificate.Certificate")

IsValid(*hours=0*)[¶](#tts.core.api.internalApi.credentialsApi.Certificate.Certificate.IsValid "Link to this definition")  
Checks if the certificate is still valid for at least the given amount of time.

Parameters:  **hours** (*int*) – The minimum number of hours for which the certificate must still be valid.

Return type:  bool

Issuer()[¶](#tts.core.api.internalApi.credentialsApi.Certificate.Certificate.Issuer "Link to this definition")  
Return the issuer of this certificate.

Return type:  str

PEM()[¶](#tts.core.api.internalApi.credentialsApi.Certificate.Certificate.PEM "Link to this definition")  
Returns the certificate as PEM encoded string.

Return type:  str

PublicKey()[¶](#tts.core.api.internalApi.credentialsApi.Certificate.Certificate.PublicKey "Link to this definition")  
Return the certificate’s public key.

Return type:  [`PublicKey`](#tts.core.api.internalApi.credentialsApi.PublicKey.PublicKey "tts.core.api.internalApi.credentialsApi.PublicKey.PublicKey")

Subject()[¶](#tts.core.api.internalApi.credentialsApi.Certificate.Certificate.Subject "Link to this definition")  
Return subject of this certificate.

Return type:  str

Verify(*signature*, *message*)[¶](#tts.core.api.internalApi.credentialsApi.Certificate.Certificate.Verify "Link to this definition")  
Verifies a signature of the given message.

Parameters:  - **signature** ([*ByteStream*](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream")) – The supposed signature of the message created by the corresponding private key.

- **message** ([*ByteStream*](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream")) – The message that has been signed.

Returns:  True, if the verification is successful, otherwise False.

Return type:  bool

### PrivateKey[¶](#privatekey "Link to this heading")

*class* PrivateKey[¶](#tts.core.api.internalApi.credentialsApi.PrivateKey.PrivateKey "Link to this definition")  

*classmethod* FromFile(*filePath*)[¶](#tts.core.api.internalApi.credentialsApi.PrivateKey.PrivateKey.FromFile "Link to this definition")  
Creates a PrivateKey instance from a PEM or DER formatted file.

Parameters:  **filePath** (*str*) – Path of private key file.

Return type:  [`PrivateKey`](#tts.core.api.internalApi.credentialsApi.PrivateKey.PrivateKey "tts.core.api.internalApi.credentialsApi.PrivateKey.PrivateKey")

PublicKey()[¶](#tts.core.api.internalApi.credentialsApi.PrivateKey.PrivateKey.PublicKey "Link to this definition")  
Return the corresponding public key.

Return type:  [`PublicKey`](#tts.core.api.internalApi.credentialsApi.PublicKey.PublicKey "tts.core.api.internalApi.credentialsApi.PublicKey.PublicKey")

Sign(*message*)[¶](#tts.core.api.internalApi.credentialsApi.PrivateKey.PrivateKey.Sign "Link to this definition")  
Signs the given message.

Return type:  [`ByteStream`](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream")

### PublicKey[¶](#publickey "Link to this heading")

*class* PublicKey[¶](#tts.core.api.internalApi.credentialsApi.PublicKey.PublicKey "Link to this definition")  

Base64()[¶](#tts.core.api.internalApi.credentialsApi.PublicKey.PublicKey.Base64 "Link to this definition")  
Returns the public key as base64 string.

Return type:  str

*classmethod* FromFile(*filePath*)[¶](#tts.core.api.internalApi.credentialsApi.PublicKey.PublicKey.FromFile "Link to this definition")  
Creates a PublicKey instance from a PEM or DER formatted file.

Parameters:  **filePath** (*str*) – Path of the public key file.

Return type:  [`PublicKey`](#tts.core.api.internalApi.credentialsApi.PublicKey.PublicKey "tts.core.api.internalApi.credentialsApi.PublicKey.PublicKey")

Verify(*signature*, *message*)[¶](#tts.core.api.internalApi.credentialsApi.PublicKey.PublicKey.Verify "Link to this definition")  
Verifies a signature of the given message.

Parameters:  - **signature** ([*ByteStream*](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream")) – The supposed signature of the message created by the corresponding private key.

- **message** ([*ByteStream*](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream")) – The message that has been signed.

Returns:  True, if the verification is successful, otherwise False.

Return type:  bool

## DataBrowser[¶](#module-tts.core.api.dataBrowserApi.DataBrowser "Link to this heading")

### A2lBrowser[¶](#a2lbrowser "Link to this heading")

*class* A2lBrowser[¶](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser "Link to this definition")  
The A2lBrowser type provides an interface to a A2L database. It is possible to retrieve information for a single entry or to use a full text search to get a list of filtered entries. Every entity is represented by an instance of the type [`A2lEntity`](#tts.core.api.dataBrowserApi.DataBrowser.A2lEntity "tts.core.api.dataBrowserApi.DataBrowser.A2lEntity").

CalcPhysToRaw(*label*, *physValue*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.CalcPhysToRaw "Link to this definition")  
Returns the raw value of the provided physical value computed using the computation method defined for the provided label

Parameters:  - **label** (*str*) – The A2L label to select the computation method from

- **physValue** (*float*) – The numeric value to be converted to its raw representation

Returns:  raw value

Return type:  float

CalcRawToPhys(*label*, *rawValue*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.CalcRawToPhys "Link to this definition")  
Returns the physical converted value of the provided raw value computed using the computation method defined for the provided label

Parameters:  - **label** (*str*) – The A2L label to select the computation method from

- **rawValue** (*float*) – The numeric value to be converted to its physical representation

Returns:  physical converted value

Return type:  float

GetA2lEntity(*label*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.GetA2lEntity "Link to this definition")  
Returns an instance of A2lEntity representing the entity with the specified label

Parameters:  **label** (*str*) – The A2L label to retrieve an A2lEntity instance

Returns:  An A2lEntity instance if the A2L database contains an entry with the given name, otherwise None

Return type:  [`A2lEntity`](#tts.core.api.dataBrowserApi.DataBrowser.A2lEntity "tts.core.api.dataBrowserApi.DataBrowser.A2lEntity") or None

GetAcquisitionRateNames()[¶](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.GetAcquisitionRateNames "Link to this definition")  
Returns a list containing all acquisition rate names defined in the A2L database.

Returns:  A list of all acquisition rate names

Return type:  list \<str\>

GetFunctionCharacteristics(*name*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.GetFunctionCharacteristics "Link to this definition")  
Returns the characteristics of the function with the given name

Parameters:  **name** (*str*) – The name of the function to return the characteristics of

Returns:  The characteristics of the function

Return type:  list \<str\>

GetFunctionInMeasurements(*name*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.GetFunctionInMeasurements "Link to this definition")  
Returns the in measurements of the function with the given name

Parameters:  **name** (*str*) – The name of the function to return the in measurementes of

Returns:  The in measurements of the function

Return type:  list \<str\>

GetFunctionLocMeasurements(*name*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.GetFunctionLocMeasurements "Link to this definition")  
Returns the local measurements of the function with the given name

Parameters:  **name** (*str*) – The name of the function to return the local measurementes of

Returns:  The local measurements of the function

Return type:  list \<str\>

GetFunctionNames()[¶](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.GetFunctionNames "Link to this definition")  
Returns the names of all functions within the A2L

Returns:  The names of all functions

Return type:  list \<str\>

GetFunctionOutMeasurements(*name*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.GetFunctionOutMeasurements "Link to this definition")  
Returns the out measurements of the function with the given name

Parameters:  **name** (*str*) – The name of the function to return the out measurements of

Returns:  The out measurements of the function

Return type:  list \<str\>

GetFunctionVersion(*name*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.GetFunctionVersion "Link to this definition")  
Returns the version of the function with the given name

Parameters:  **name** (*str*) – The name of the function to return the version of

Returns:  The version of the function

Return type:  str

GetLabelNameList(*filter=''*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.GetLabelNameList "Link to this definition")  
Returns a list which contains names of labels whose matches the specified label search string

Parameters:  **filter** (*str*) – The search string which is part of an A2L label

Returns:  A list of names if the A2L database containsentries with the given search string, otherwise an empty list

Return type:  list\<str\>

GetSubFunctionNames(*name*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.GetSubFunctionNames "Link to this definition")  
Returns the names of all sub functions within the function with the given name

Parameters:  **name** (*str*) – The name of the function to get the sub functions of

Returns:  The names of all sub functions

Return type:  list \<str\>

GetSystemConstantNameList()[¶](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.GetSystemConstantNameList "Link to this definition")  
Returns a list which contains names of system constants defined in the A2L

Returns:  A list of names

Return type:  list\<str\>

GetSystemConstantValue(*constName*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.GetSystemConstantValue "Link to this definition")  
Returns the value of the given system constant

Parameters:  **constName** (*str*) – Name of system constant defined in A2L

Returns:  Value of system constant or None if name was not found

Return type:  str or None

HasFunction(*name*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.HasFunction "Link to this definition")  
Checks if a function of the given name exists within the A2L file

Parameters:  **name** (*str*) – The name to check if it is an existing function

Returns:  True if a function with the given name exist, otherwise False

Return type:  bool

HasSubFunctions(*name*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.HasSubFunctions "Link to this definition")  
Checks if a function of the given name within the A2L file has sub functions

Parameters:  **name** (*str*) – The name of the function to check for sub functions

Returns:  True if the function of the given name has subfunctions, otherwise False

Return type:  bool

IsCharacteristic(*label*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.IsCharacteristic "Link to this definition")  
Checks if the given label name is a calibration variable

Parameters:  **label** (*str*) – The A2L label to check for a calibration variable

Returns:  True if the given label is a calibration variable, otherwise False

Return type:  bool

IsMeasurement(*label*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.IsMeasurement "Link to this definition")  
Checks if the given label name is a measurement variable

Parameters:  **label** (*str*) – The A2L label to check for a measurement variable

Returns:  True if the given label is a measurement variable, otherwise False.

Return type:  bool

### A2lEntity[¶](#a2lentity "Link to this heading")

*class* A2lEntity[¶](#tts.core.api.dataBrowserApi.DataBrowser.A2lEntity "Link to this definition")  
The A2lEntity type represents one entry in an A2L database

GetAddress()[¶](#tts.core.api.dataBrowserApi.DataBrowser.A2lEntity.GetAddress "Link to this definition")  
Returns the address of this A2L entity

Returns:  Address as hex number

Return type:  str

GetByteOrder()[¶](#tts.core.api.dataBrowserApi.DataBrowser.A2lEntity.GetByteOrder "Link to this definition")  
Returns the signals byte order

Returns:  ‘MSB_LAST’ or ‘MSB_FIRST’

Return type:  str

GetCoeffsDict()[¶](#tts.core.api.dataBrowserApi.DataBrowser.A2lEntity.GetCoeffsDict "Link to this definition")  
Returns the coefficients of this A2L entity

Returns:  - The coefficients stored in a dictionary where the key is the index and value is the value at this index

- None if the coefficients are invalid

Return type:  dict\<int: float\> or None

GetCompuMethodName()[¶](#tts.core.api.dataBrowserApi.DataBrowser.A2lEntity.GetCompuMethodName "Link to this definition")  
Returns the name of the compu method of this A2L entity like defined in the A2L database

Returns:  The compu methods name

Return type:  str

GetDataType()[¶](#tts.core.api.dataBrowserApi.DataBrowser.A2lEntity.GetDataType "Link to this definition")  
Returns the dataype of this A2L entity

Returns:  The datatype

Return type:  str

GetDescription()[¶](#tts.core.api.dataBrowserApi.DataBrowser.A2lEntity.GetDescription "Link to this definition")  
Returns the description of this A2L entity

Returns:  The description

Return type:  str

GetDisplayIdentifier()[¶](#tts.core.api.dataBrowserApi.DataBrowser.A2lEntity.GetDisplayIdentifier "Link to this definition")  
Returns the display identifier of this A2L entity

Returns:  The display identifier

Return type:  str

GetLowerLimit()[¶](#tts.core.api.dataBrowserApi.DataBrowser.A2lEntity.GetLowerLimit "Link to this definition")  
Returns the lower limit of this A2L entity

Returns:  The lower limit

Return type:  str

GetMatrixDim()[¶](#tts.core.api.dataBrowserApi.DataBrowser.A2lEntity.GetMatrixDim "Link to this definition")  
Returns the matrix dimensions for calibration or measurement entities

Returns:  - Dimensions tuple

- None if no MATRIX_DIM is given in the A2L file

Return type:  tuple or None

GetName()[¶](#tts.core.api.dataBrowserApi.DataBrowser.A2lEntity.GetName "Link to this definition")  
Returns the name of this A2L entity

Returns:  The name

Return type:  str

GetSize()[¶](#tts.core.api.dataBrowserApi.DataBrowser.A2lEntity.GetSize "Link to this definition")  
Returns the size of this A2L entity

Returns:  - The size

- None if it is a scalar

Return type:  int or None

GetUnit()[¶](#tts.core.api.dataBrowserApi.DataBrowser.A2lEntity.GetUnit "Link to this definition")  
Returns the name of the unit of this A2L entity like defined in the A2L database

Returns:  The units name

Return type:  str

GetUpperLimit()[¶](#tts.core.api.dataBrowserApi.DataBrowser.A2lEntity.GetUpperLimit "Link to this definition")  
Returns the upper limit of this A2L entity

Returns:  The upper limit

Return type:  str

GetValueType()[¶](#tts.core.api.dataBrowserApi.DataBrowser.A2lEntity.GetValueType "Link to this definition")  
Returns the internal data type representation of the current A2L entity

Returns:  - Internal data type representation

- None if the entity is of an unsupported type

Return type:  str or None

GetVtabDict()[¶](#tts.core.api.dataBrowserApi.DataBrowser.A2lEntity.GetVtabDict "Link to this definition")  
Returns the V-TAB Dictionary

Returns:  V-TAB Dictionary

Return type:  dict

### BusBrowser[¶](#busbrowser "Link to this heading")

*class* BusBrowser[¶](#tts.core.api.dataBrowserApi.DataBrowser.BusBrowser "Link to this definition")  
The BusBrowser type provides an interface to a BUS database. It is possible to retrieve information for a single entry or to use a full text search to get a list of filtered entries. Every entity is represented by an instance of the type [`BusEntity`](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity "tts.core.api.dataBrowserApi.DataBrowser.BusEntity").

Note

This part of the DataBrowser API was specifically created to support certain use cases. Don’t expect your use case to easily map onto this API!

GetFrameNamesByPDUName(*pduName*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.BusBrowser.GetFrameNamesByPDUName "Link to this definition")  
Returns a set of frame names the given PDU is bound to

Parameters:  **pduName** (*str*) – The name of the PDU

Returns:  The frame names

Return type:  set\<str\>

GetLinScheduleTables()[¶](#tts.core.api.dataBrowserApi.DataBrowser.BusBrowser.GetLinScheduleTables "Link to this definition")  
Returns the LIN schedule tables as a dictionary, mapping the schedule table name to a sequence of triples (isFrameName, command, frameTime)

Returns:  LIN schedule tables

Return type:  dict\<string, tuple\<bool, string, float\>\>

ListFrames(*filter=''*, *useLongNames=False*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.BusBrowser.ListFrames "Link to this definition")  
Returns a list of BusEntity instances corresponding to frames whose name matches the specified search string

Parameters:  - **filter** (*str*) – The search string which is part of a bus frame

- **useLongNames** (*bool*) – If True search in LongNames else (default) in ShortNames

Returns:  A list of BusEntity instances if the bus database contains entries with the given search string, otherwise an empty list

Return type:  list \<[`BusEntities`](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity "tts.core.api.dataBrowserApi.DataBrowser.BusEntity")\>

ListPDUs(*frameName=None*, *filter=''*, *useLongNames=False*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.BusBrowser.ListPDUs "Link to this definition")  
Returns a list of BusEntity instances corresponding to PDUs whose name matches the specified search string

Parameters:  - **frameName** (*str*) – The exact short name of the frame in which to search for PDUs (optional)

- **filter** (*str*) – The search string which is part of a bus frame

- **useLongNames** (*bool*) – If True search in LongNames else (default) in ShortNames

Returns:  A list of BusEntity instances if the bus database contains entries with the given search string, otherwise an empty list

Return type:  list \<[`BusEntities`](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity "tts.core.api.dataBrowserApi.DataBrowser.BusEntity")\>

ListSignals(*frameName*, *filter=''*, *useLongNames=False*, *includePseudoSignals=False*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.BusBrowser.ListSignals "Link to this definition")  
Returns a list of BusEntity instances corresponding to signals whose name matches the specified search string

Parameters:  - **frameName** (*str*) – The exact name of the frame in which to search for signals

- **filter** (*str*) – The search string which is part of a bus signal

- **useLongNames** (*bool*) – If True search in LongNames else (default) in ShortNames

- **includePseudoSignals** (*bool*) – If True additionally list pseudo signals like \_pduUpdateBit (default=False)

Returns:  A list of BusEntity instances if the bus database contains entries with the given search string, otherwise an empty list

Return type:  list \<[`BusEntities`](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity "tts.core.api.dataBrowserApi.DataBrowser.BusEntity")\>

ListSignalsByPDU(*pduName*, *filter=''*, *useLongNames=False*, *includePseudoSignals=False*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.BusBrowser.ListSignalsByPDU "Link to this definition")  
Returns a list of BusEntity instances corresponding to signals whose name matches the specified search string

Parameters:  - **pduName** (*str*) – The exact name of the PDU in which to search for signals

- **filter** (*str*) – The search string which is part of a bus signal

- **useLongNames** (*bool*) – If True search in LongNames else (default) in ShortNames

- **includePseudoSignals** (*bool*) – If True additionally list pseudo signals like \_pduUpdateBit (default=False)

Returns:  A list of BusEntity instances if the bus database contains entries with the given search string, otherwise an empty list

Return type:  list \<[`BusEntities`](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity "tts.core.api.dataBrowserApi.DataBrowser.BusEntity")\>

### BusEntity[¶](#busentity "Link to this heading")

*class* BusEntity[¶](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity "Link to this definition")  
The BusEntity type represents one entry in a bus database

GetActivations()[¶](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetActivations "Link to this definition")  
Returns a list consisting of tuples with activation state, activation time and signal quality of the signal

Return type:  list \<tuple \<str, float, str\>\>

GetByteOrder()[¶](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetByteOrder "Link to this definition")  
Returns the signals byte order

Returns:  - “Intel”

- ”Motorola”

- ”Default”

- None

Return type:  str or None

GetCycleRepetition()[¶](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetCycleRepetition "Link to this definition")  
Returns the frames cycle repetition if this bus entity is a bus frame else None

Note

Only applies to FlexRay frames.

Returns:  Frame cycle repetition

Return type:  int or None

GetDebounceTime()[¶](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetDebounceTime "Link to this definition")  
Returns the debounce time of a PDU or a frame else None

Returns:  Debounce time

Return type:  float or None

GetDescription()[¶](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetDescription "Link to this definition")  
Returns the description of this bus entity

Returns:  The description

Return type:  str

GetE2EProfile()[¶](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetE2EProfile "Link to this definition")  
Returns the E2E profile of a PDU

Returns:  E2E profile

Return type:  dict

GetFrameLength()[¶](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetFrameLength "Link to this definition")  
Returns the length of the frame in bytes if this bus entity is a bus frame else None

Returns:  Length of frame in bytes

Return type:  int or None

GetId()[¶](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetId "Link to this definition")  
Returns the identifier of this bus entity

Note

This works only for BusEntities representing a bus frame.

Returns:  The identifier

Return type:  str

GetLongName()[¶](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetLongName "Link to this definition")  
Returns the long name of this bus entity

Returns:  The long name

Return type:  str

GetMaxRawValue()[¶](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetMaxRawValue "Link to this definition")  
Returns the maximum raw value of the signal. Note that this value is not necessarily equal (but always greater or equal) to GetRawValue(GetMaxValue()) as the set of physical values usually not maps to all valid raw values.

Returns:  Maximum raw value

Return type:  float

GetMaxValue()[¶](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetMaxValue "Link to this definition")  
Returns the maximum physical value of the signal

Returns:  Maximum physical value

Return type:  float

GetMinRawValue()[¶](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetMinRawValue "Link to this definition")  
Returns the minimum raw value of the signal. Note that this value is not necessarily equal (but always less or equal) to GetRawValue(GetMinValue()) as the set of physical values usually not maps to all valid raw values.

Returns:  Minimum raw value

Return type:  float

GetMinValue()[¶](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetMinValue "Link to this definition")  
Returns the minimum physical value of the signal

Returns:  Minimum physical value

Return type:  float

GetMultiplexerSwitchCode()[¶](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetMultiplexerSwitchCode "Link to this definition")  
Returns the switch code of this bus entity else None

Note

This works only for BusEntities representing a bus PDU or bus signal.

Returns:  The switch code if available

Return type:  str or None

GetName()[¶](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetName "Link to this definition")  
Returns the name of this bus entity

Returns:  The name

Return type:  str

GetPDULength()[¶](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetPDULength "Link to this definition")  
Returns the byte length if this bus entity is a bus PDU

Returns:  The byte length

Return type:  int or None

GetPDUPosition()[¶](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetPDUPosition "Link to this definition")  
Returns the absolute bit position if this bus entity is a bus PDU

Returns:  The absolute bit position

Return type:  int or None

GetPDUUpdateBit()[¶](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetPDUUpdateBit "Link to this definition")  
Returns the absolute bit position of the update bit if this bus entity is a bus PDU

Returns:  The absolute bit position

Return type:  int or None

GetPath()[¶](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetPath "Link to this definition")  
Returns the variablepath of this bus entity

Returns:  The variablepath (e.g.: \<busName\>/\<ecuName\>/\<frameName\>/\<pduName\>/\<signalName\>)

Return type:  str

GetPhysResolution()[¶](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetPhysResolution "Link to this definition")  
Returns the physical resolution (slope)

Returns:  The physical resolution

Return type:  float

GetPhysValue(*rawValue*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetPhysValue "Link to this definition")  
Returns the physical value of given raw value

Returns:  Physical value of given raw value

Return type:  float

GetRawValue(*value*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetRawValue "Link to this definition")  
Returns the raw value of given value

Note

Value can be text or physical value.

Returns:  The raw value

Return type:  int

GetRxEcuNames()[¶](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetRxEcuNames "Link to this definition")  
Returns the names of the ECUs which listen for this Frame/PDU

Returns:  The names of the ECUs

Return type:  list\<str\>

GetSignalDataPositionInFrame()[¶](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetSignalDataPositionInFrame "Link to this definition")  
Returns the signals data bit position relative to the frame

Returns:  The signals data bit position

Return type:  int or None

Raise:  
ValueError if the Signal has no fixed position in the frame (e.g. container PDUs)

GetSignalDataPositionInPDU()[¶](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetSignalDataPositionInPDU "Link to this definition")  
Returns the signals data bit position relative to the PDU

Returns:  The signals data bit position

Return type:  int or None

GetSignalLength()[¶](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetSignalLength "Link to this definition")  
Returns the length of the signal in bits if this bus entity is a bus signal else None

Returns:  The length of the signal in bits

Return type:  int or None

GetStartCycle()[¶](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetStartCycle "Link to this definition")  
Returns the frames start cycle if this bus entity is a bus frame else None

Note

Only applies to FlexRay frames.

Returns:  The frames start cycle

Return type:  int or None

GetSystemSignalName()[¶](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetSystemSignalName "Link to this definition")  
Returns the name of the system signal of this bus entity

Returns:  The name

Return type:  str

GetTextTable(*numbersAsStrings=False*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetTextTable "Link to this definition")  
Returns the text table as a dictionary

Note

Set numbersAsStrings to True when using this method via ApiProxy.

Returns:  The text table

Return type:  dict

GetTimeOffset(*transmissionMode=None*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetTimeOffset "Link to this definition")  
Returns the time offset of a PDU or a frame

Parameters:  **transmissionMode** – If None maximal time offset is returned. If True cyclic time offset and if False cyclic-controlled time offset is returned. (optional)

Return type:  float or None

GetTimings(*transmissionMode=None*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetTimings "Link to this definition")  
Returns dtMin and dtMax for this Frame/PDU

Parameters:  **transmissionMode** – If None global Timings are returned. If True cyclic timings and if False event-controlled Timings are returned. (optional)

Returns:  Minimum and maximum timings (in seconds)

Return type:  (float, float) or (None, None)

GetTxEcuNames()[¶](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetTxEcuNames "Link to this definition")  
Returns the names of the ECUs which are capable of transmitting this Frame/PDU/Signal corresponding to the Bus access tab

Returns:  The names of the ECUs

Return type:  list\<str\>

GetUnit()[¶](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetUnit "Link to this definition")  
Returns the unit of a bus signal

Returns:  The unit

Returns:  str

IsFrame()[¶](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.IsFrame "Link to this definition")  
Checks if this bus entity is a bus frame

Returns:  True if this entity is a bus frame else False

Return type:  bool

IsMultiplexer()[¶](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.IsMultiplexer "Link to this definition")  
Checks if this bus entity is multiplexed

Note

This works only for BusEntities representing a bus PDU or frame.

Returns:  True if this Item is a multiplexed PDU (DynamicPart) or a Frame containing multiplexed PDUs else False

Return type:  bool

IsNode()[¶](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.IsNode "Link to this definition")  
Checks if this bus entity is a bus node

Returns:  True if this entity is a bus node else False

Return type:  bool

IsPDU()[¶](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.IsPDU "Link to this definition")  
Checks if this bus entity is a bus PDU

Returns:  True if this entity is a bus PDU else False

Return type:  bool

IsSend()[¶](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.IsSend "Link to this definition")  
Returns true if the current signal is sent from its associated ECU

Return type:  bool

IsSignal()[¶](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.IsSignal "Link to this definition")  
Checks if this bus entity is a bus signal

Returns:  True if this entity is a bus signal else False

Return type:  bool

### DataBrowser[¶](#id30 "Link to this heading")

*class* DataBrowser[¶](#tts.core.api.dataBrowserApi.DataBrowser.DataBrowser "Link to this definition")  
The DataBrowser provides functions to retrieve a specific object to a database of a configured device in the test configuration. Currently, there are interfaces to browse inside A2L, BUS , debugging (ELF), diagnostic, logging, multimedia, service and SGBD data of an electronic control unit (ECU). The interface to browse SGBD data is currently in a prototype state.

BrowseA2l(*ecuKey*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.DataBrowser.BrowseA2l "Link to this definition")  
BrowseA2l gives access to an A2L database. The database is specified by the same name of the ECU which is given in the test configuration.

> - E.g.: a2lBrowser = DataBrowser().BrowseA2l(“DME1_DDE1”)

Parameters:  **ecuKey** (*str*) – The name of the ECU to which an A2L browser is requested

Returns:  A2lBrowser object

Return type:  [`A2lBrowser`](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser "tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser")

BrowseBus(*busKey*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.DataBrowser.BrowseBus "Link to this definition")  
BrowseBus gives access to a bus database. The database is specified by the same bus name which is given in the test configuration.

> - E.g.: busBrowser = DataBrowser().BrowseBus(“PT_CAN”)

Parameters:  **busKey** (*str*) – The name of the BUS to which a BUS browser is requested.

Returns:  BusBrowser object

Return type:  [`BusBrowser`](#tts.core.api.dataBrowserApi.DataBrowser.BusBrowser "tts.core.api.dataBrowserApi.DataBrowser.BusBrowser")

Note

This part of the DataBrowser API was specifically created to support certain use cases. Don’t expect your use case to easily map onto this API!

BrowseDebug(*ecuKey*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.DataBrowser.BrowseDebug "Link to this definition")  
BrowseDebug gives access to the debug database with information provided by ELF files. The database is specified by the name of the ECU (ecuKey) which is defined in the test configuration.

Parameters:  **ecuKey** (*str*) – The name of the ECU to which a DebugBrowser is requested.

Returns:  DebugBrowser object

Return type:  [`DebugBrowser`](#tts.core.api.dataBrowserApi.DataBrowser.DebugBrowser "tts.core.api.dataBrowserApi.DataBrowser.DebugBrowser")

BrowseDebugElf(*elfFile*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.DataBrowser.BrowseDebugElf "Link to this definition")  
BrowseDebugElf gives access to an ELF-database. Contrary to BrowseDebug the database is specified by an ELF-File on the filesystem. Please Note: To query a register a connection to a debugger as well as a API call via BrowseDebug (not BrowseDebugElf) is required.

Parameters:  **elfFile** (*str*) – The full path to an ELF-File.

Returns:  DebugBrowser object

Return type:  [`DebugBrowser`](#tts.core.api.dataBrowserApi.DataBrowser.DebugBrowser "tts.core.api.dataBrowserApi.DataBrowser.DebugBrowser")

BrowseDiag(*ecuKey*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.DataBrowser.BrowseDiag "Link to this definition")  
BrowseDiag gives access to entities from the diagnostic database which was assigned to the ECU in the test configuration.

> - E.g.: diagBrowser = DataBrowser().BrowseDiag(‘Engine’)

Parameters:  **ecuKey** (*str*) – The name of the ECU a DiagBrowser is requested for

Returns:  DiagBrowser object

Return type:  [`DiagBrowser`](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagBrowser "tts.testModule.diag.dataBrowser.DiagBrowser.DiagBrowser")

BrowseLogging(*ecuKey*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.DataBrowser.BrowseLogging "Link to this definition")  
BrowseLogging gives access to a logging database. The database is specified by the same name of the ECU which is given in the test configuration.

> - E.g.: loggingBrowser = DataBrowser().BrowseLogging(“DME1_DDE1”)

Parameters:  **ecuKey** (*str*) – The name of the ECU to which a logging browser is requested.

Returns:  LoggingBrowser object

Return type:  [`LoggingBrowser`](#tts.core.api.dataBrowserApi.DataBrowser.LoggingBrowser "tts.core.api.dataBrowserApi.DataBrowser.LoggingBrowser")

BrowseModel(*modelKey*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.DataBrowser.BrowseModel "Link to this definition")  
BrowseModel gives access to the model database associated with the given modelKey in the test configuration.

Parameters:  **modelKey** (*str*) – Key of the model as specified in the test configuration’s Platform tab.

Returns:  ModelBrowser object

Return type:  [`ModelBrowser`](#tts.core.api.dataBrowserApi.DataBrowser.ModelBrowser "tts.core.api.dataBrowserApi.DataBrowser.ModelBrowser")

BrowseMultimedia(*deviceKey*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.DataBrowser.BrowseMultimedia "Link to this definition")  
BrowseMultimedia gives access to [`Image`](mediadatastructures.md#tts.testModule.multimedia.dataElements.Image.Image "tts.testModule.multimedia.dataElements.Image.Image") or [`Mask`](mediadatastructures.md#tts.testModule.multimedia.dataElements.Mask.Mask "tts.testModule.multimedia.dataElements.Mask.Mask") ojects. The target folder is specified by the same deviceKey which is given as a name in the test configuration.

> - E.g.: multimediaBrowser = DataBrowser().BrowseMultimedia(“CAM”)

Parameters:  **deviceKey** (*str*) – The name of the multimedia device to which a browser is requested.

Returns:  MediaBrowser object

Return type:  [`MediaBrowser`](#tts.testModule.multimedia.dataBrowser.MediaBrowser.MediaBrowser "tts.testModule.multimedia.dataBrowser.MediaBrowser.MediaBrowser")

BrowseService(*serviceKey*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.DataBrowser.BrowseService "Link to this definition")  
BrowseService gives access to a service database. The database is specified by the same name of the service name which is given in the test configuration.

> - E.g.: serviceBrowser = DataBrowser().BrowseService(“ETHERNET”)

Parameters:  **serviceKey** (*str*) – The name of the BUS to which a BUS browser is requested.

Returns:  ServiceBrowser object

Return type:  [`ServiceBrowser`](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser "tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser")

Note

prototype

BrowseSgbd(*ecuKey*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.DataBrowser.BrowseSgbd "Link to this definition")  
BrowseSgbd gives access to a SGBD file. The SGBD is specified by the same name of the ECU which is given in the test configuration.

> - E.g.: sgbdBrowser = DataBrowser().BrowseSgbd(“DME1_DDE1”)

Parameters:  **ecuKey** (*str*) – The name of the ECU to which a SGBD browser is requested.

Returns:  SgbdBrowser object

Return type:  [`SgbdBrowser`](#tts.core.api.dataBrowserApi.DataBrowser.SgbdBrowser "tts.core.api.dataBrowserApi.DataBrowser.SgbdBrowser")

Note

prototype

### DebugBrowser[¶](#debugbrowser "Link to this heading")

*class* DebugBrowser[¶](#tts.core.api.dataBrowserApi.DataBrowser.DebugBrowser "Link to this definition")  
The DebugBrowser type prodvides an interface to a Debugger database. It is possible to query for debug variables or register entries.

GetCores()[¶](#tts.core.api.dataBrowserApi.DataBrowser.DebugBrowser.GetCores "Link to this definition")  
Returns names of all cores

Note

Cores are not supported by all debugger tool adapters

Returns:  A list of strings containing the core names found in the database.

Return type:  list\<str\>

GetElfFiles()[¶](#tts.core.api.dataBrowserApi.DataBrowser.DebugBrowser.GetElfFiles "Link to this definition")  
Returns dictionary with mapping from elfFileKey to ELF file path

Returns:  Dictionary with elfFileKey and corresponding ELF file path

Return type:  dict\<str:str\>

GetModules(*elfFileKey*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.DebugBrowser.GetModules "Link to this definition")  
Returns all modules of the ELF file referenced by the given elfFileKey

Parameters:  **elfFileKey** (*str*) – elfFileKey with or without wildcard for filtering

Returns:  List of modules

Return type:  list\<str\>

GetRegisters(*registerName=None*, *coreName=None*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.DebugBrowser.GetRegisters "Link to this definition")  
Returns all registers by default

Note

- Use optional parameters to filter registers. You can use \* as wildcard.

- Delivered registerName returns the full name, consisting of register Group and register name separated by underscore.

- Registers are not supported by all debugger tool adapters.

Parameters:  - **registerName** (*str*) – Full register name (group_name) with or without wildcard for filtering

- **coreName** (*str*) – Core name with or without wildcard for filtering

Returns:  A list of dictionaries, each filled the registers full name, its cores name and the mapping path is retured for every entry

Return type:  list\<dict\>

GetVariables(*variableName=None*, *visibility=None*, *moduleName=None*, *functionName=None*, *elfFileKey=None*, *includeExterns=False*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.DebugBrowser.GetVariables "Link to this definition")  
Returns all variables except extern variables by default

Note

Use optional parameters to filter variables. You can use \* as wildcard.

Parameters:  - **variableName** (*str*) – Variable name with or without wildcard for filtering

- **visibility** (*int*) – Type 0 for local, 1 for global or 2 for extern variables to be returned

- **moduleName** (*str*) – Module name with or without wildcard for filtering

- **functionName** (*str*) – Function name with or without wildcard for filtering

- **elfFileKey** (*str*) – elfFileKey with or without wildcard for filtering

- **includeExterns** (*bool*) – Use True to include extern variables in the search

Returns:  A list of dictionaries with the following keys: name, moduleName, visibility, type, elfFileKey, mappingPath, functionName and arraySize

Return type:  list\<dict\>

### DiagBrowser[¶](#diagbrowser "Link to this heading")

*class* DiagBrowser[¶](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagBrowser "Link to this definition")  
The DiagBrowser type provides an interface to a diagnostics data base.

GetDiagDtcs()[¶](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagBrowser.GetDiagDtcs "Link to this definition")  
Returns a list of DTC entities representing all diagnostics DTCs defined in the database

Returns:  A list of DiagDtcEntity

Return type:  list\<[`DiagDtcEntity`](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagDtcEntity "tts.testModule.diag.dataBrowser.DiagBrowser.DiagDtcEntity")\>

GetDiagServices()[¶](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagBrowser.GetDiagServices "Link to this definition")  
Returns a list of service entities representing all diagnostics services defined in the database

Returns:  A list of DiagServiceEntity

Return type:  list\<[`DiagServiceEntity`](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagServiceEntity "tts.testModule.diag.dataBrowser.DiagBrowser.DiagServiceEntity")\>

GetDiagStateCharts()[¶](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagBrowser.GetDiagStateCharts "Link to this definition")  
Returns a list of state chart entities representing all state charts defined in the database

Returns:  A list of DiagStateChartEntity

Return type:  list\<[`DiagStateChartEntity`](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateChartEntity "tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateChartEntity")\>

### DiagDtcEntity[¶](#diagdtcentity "Link to this heading")

*class* DiagDtcEntity[¶](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagDtcEntity "Link to this definition")  
The DiagDtcEntity represents one diagnostics dtc in the database.

GetSdgs()[¶](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagDtcEntity.GetSdgs "Link to this definition")  
Returns the special data of the diagnostics DTC from the data base. The special data is a set of key/value pairs, and can be subdivided into groups (SDGs).

GetShortName()[¶](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagDtcEntity.GetShortName "Link to this definition")  
Returns the name of this DTC

Returns:  The name of DTC

Return type:  str | None

GetTroubleCode()[¶](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagDtcEntity.GetTroubleCode "Link to this definition")  
Returns trouble code as integer

### DiagServiceEntity[¶](#diagserviceentity "Link to this heading")

*class* DiagServiceEntity[¶](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagServiceEntity "Link to this definition")  
The DiagServiceEntity represents one diagnostics service in the database.

GetLongName()[¶](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagServiceEntity.GetLongName "Link to this definition")  
Returns the long name of this service

Returns:  The long name of service

Return type:  str | None

GetPreconditions()[¶](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagServiceEntity.GetPreconditions "Link to this definition")  
Returns a list of the states which are defined as preconditions for this service in the diagnostics database

Returns:  A list of precondition states

Return type:  list[[*DiagStateEntity*](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateEntity "tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateEntity")]

GetSdgs()[¶](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagServiceEntity.GetSdgs "Link to this definition")  
Returns the special data of the diagnostics service from the database. The special data is a set of key/value pairs and can be subdivided into groups.

Returns:  A dictionary containing the special data group SI attribute or caption short name as key. The value will be the SD key/value pairs as further dictionaries

Return type:  dict\<str, dict\<str, str\>\>

GetServiceId()[¶](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagServiceEntity.GetServiceId "Link to this definition")  
Returns the service ID of this service

Note

e.g. 34 for ReadDataByIdentifier

Returns:  The service ID

Return type:  int

GetServiceName()[¶](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagServiceEntity.GetServiceName "Link to this definition")  
Returns the name of the service. This Methode distinguishes between different application layers (e.g. UDS, KWP 2000)

Note

e.g. “Read Data By Identifier”

Returns:  service name or “Unknown Service”

Return type:  str

GetShortName()[¶](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagServiceEntity.GetShortName "Link to this definition")  
Returns the short name of this service

Returns:  The short name of service

Return type:  str

GetTransitions()[¶](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagServiceEntity.GetTransitions "Link to this definition")  
Returns a list of state transitions which will be performed if the service was successfully called

Returns:  A list of state transitions

Return type:  list\<DiagStateTransitionEntity\>

### DiagStateChartEntity[¶](#diagstatechartentity "Link to this heading")

*class* DiagStateChartEntity[¶](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateChartEntity "Link to this definition")  
The DiagStateChartEntity represents a state chart from the diagnostics database.

GetLongName()[¶](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateChartEntity.GetLongName "Link to this definition")  
Returns the long name of this state chart

Returns:  The long name

Return type:  str

GetSemantic()[¶](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateChartEntity.GetSemantic "Link to this definition")  
Returns the semantic of this state chart

Returns:  The semantic

Return type:  str

GetShortName()[¶](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateChartEntity.GetShortName "Link to this definition")  
Returns the short name of this state chart

Returns:  The short name

Return type:  str

GetStartState()[¶](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateChartEntity.GetStartState "Link to this definition")  
Returns the start state of this state chart

Returns:  The start state

Return type:  [DiagStateEntity](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateEntity "tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateEntity")

GetStateChartId()[¶](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateChartEntity.GetStateChartId "Link to this definition")  
Returns the ID of this state chart if it was defined in the diagnostics database

Returns:  The state chart ID

Return type:  str

GetStates()[¶](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateChartEntity.GetStates "Link to this definition")  
Returns a list of all states inside this state chart

Returns:  A list of states

Return type:  list\<DiagStateEntity\>

GetTransitions()[¶](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateChartEntity.GetTransitions "Link to this definition")  
Returns a list of all transitions inside this state chart

Returns:  A list of state transitions

Return type:  list\<DiagStateTransitionEntity\>

### DiagStateEntity[¶](#diagstateentity "Link to this heading")

*class* DiagStateEntity[¶](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateEntity "Link to this definition")  
The DiagStateEntity represents a state from the diagnostics database.

GetEndingTransitions()[¶](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateEntity.GetEndingTransitions "Link to this definition")  
Returns a list of state transitions which have this state as their target state

Returns:  A list of state transitions

Return type:  list[[*DiagStateTransitionEntity*](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateTransitionEntity "tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateTransitionEntity")]

GetLongName()[¶](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateEntity.GetLongName "Link to this definition")  
Returns the long name of the state

Returns:  The long name of the state

Return type:  str | None

GetShortName()[¶](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateEntity.GetShortName "Link to this definition")  
Returns the short name of the state

Returns:  The short name of the state

Return type:  str

GetStartingTransitions()[¶](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateEntity.GetStartingTransitions "Link to this definition")  
Returns a list of state transitions which have this state as their source state

Returns:  A list of state transitions

Return type:  list[[*DiagStateTransitionEntity*](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateTransitionEntity "tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateTransitionEntity")]

GetStateChart()[¶](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateEntity.GetStateChart "Link to this definition")  
Returns the state chart this state belongs to

Returns:  The state chart

Return type:  [*DiagStateChartEntity*](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateChartEntity "tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateChartEntity")

GetStateId()[¶](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateEntity.GetStateId "Link to this definition")  
Returns the ID of this state if it was specified in the diagnostics database

Returns:  The state ID

Return type:  str

### DiagStateTransitionEntity[¶](#diagstatetransitionentity "Link to this heading")

*class* DiagStateTransitionEntity[¶](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateTransitionEntity "Link to this definition")  
The DiagStateTransitionEntity represents a transition from one state to another as defined in the diagnostics data base.

GetLongName()[¶](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateTransitionEntity.GetLongName "Link to this definition")  
Returns the long name of this transition

Returns:  The long name

Return type:  str | None

GetServices()[¶](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateTransitionEntity.GetServices "Link to this definition")  
Returns a list of all services which may trigger this transition

Returns:  A list of services

Return type:  list[[*DiagServiceEntity*](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagServiceEntity "tts.testModule.diag.dataBrowser.DiagBrowser.DiagServiceEntity")]

GetShortName()[¶](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateTransitionEntity.GetShortName "Link to this definition")  
Returns the short name of this transition

Returns:  The short name

Return type:  str | None

GetSourceState()[¶](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateTransitionEntity.GetSourceState "Link to this definition")  
Returns the source state of this transition

Returns:  The state

Return type:  [*DiagStateEntity*](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateEntity "tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateEntity")

GetStateChart()[¶](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateTransitionEntity.GetStateChart "Link to this definition")  
Returns the state chart this transition belongs to

Returns:  The state chart

Return type:  [*DiagStateChartEntity*](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateChartEntity "tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateChartEntity")

GetTargetState()[¶](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateTransitionEntity.GetTargetState "Link to this definition")  
Returns the target state of this transition

Returns:  The state

Return type:  [*DiagStateEntity*](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateEntity "tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateEntity")

GetTransitionId()[¶](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateTransitionEntity.GetTransitionId "Link to this definition")  
Returns the ID of this transition if it was specified in the diagnostics database

Returns:  The transition ID

Return type:  str

### LoggingBrowser[¶](#loggingbrowser "Link to this heading")

*class* LoggingBrowser[¶](#tts.core.api.dataBrowserApi.DataBrowser.LoggingBrowser "Link to this definition")  
The LoggingBrowser type provides an interface to a logging database. It is possible to retrieve information for a single entry or to use a full text search to get a list of filtered entries. Every entity is represented by an instance of the type [`LoggingEntity`](#tts.core.api.dataBrowserApi.DataBrowser.LoggingEntity "tts.core.api.dataBrowserApi.DataBrowser.LoggingEntity").

GetProtocol()[¶](#tts.core.api.dataBrowserApi.DataBrowser.LoggingBrowser.GetProtocol "Link to this definition")  
Returns the logging protocol configured for the ECU

Returns:  “DLT (non-verbose)” or “DLT (verbose)”

Return type:  str

ListArguments(*messageName*, *filter=''*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.LoggingBrowser.ListArguments "Link to this definition")  
Returns a list of LoggingEntity instances corresponding to message arguments whose name matches the specified search string

Returns an empty list if the logging protocol is not “DLT (non-verbose)”.

Parameters:  - **messageName** (*str*) – The exact name of the message in which to search for arguments

- **filter** (*str*) – The search string which is part of a logging argument’s nam

Returns:  A list of LoggingEntity instances if the logging database contains entries with the given search string, otherwise an empty list

Return type:  list \<[`LoggingEntity`](#tts.core.api.dataBrowserApi.DataBrowser.LoggingEntity "tts.core.api.dataBrowserApi.DataBrowser.LoggingEntity")\>

ListMessages(*filter=''*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.LoggingBrowser.ListMessages "Link to this definition")  
Returns a list of LoggingEntity instances corresponding to messages whose name matches the specified search string

Parameters:  **filter** (*str*) – The search string which is part of a logging message’s name

Returns:  A list of LoggingEntity instances if the logging database contains entries with the given search string, otherwise an empty list

Return type:  list \<[`LoggingEntity`](#tts.core.api.dataBrowserApi.DataBrowser.LoggingEntity "tts.core.api.dataBrowserApi.DataBrowser.LoggingEntity")\>

### LoggingEntity[¶](#loggingentity "Link to this heading")

*class* LoggingEntity[¶](#tts.core.api.dataBrowserApi.DataBrowser.LoggingEntity "Link to this definition")  
The LoggingEntity type represents one entry in a logging database.

GetArgumentLength()[¶](#tts.core.api.dataBrowserApi.DataBrowser.LoggingEntity.GetArgumentLength "Link to this definition")  
Returns the length of the argument in bits if this logging entity is a logging argument of protocol “DLT (non-verbose)” else None

Returns:  The length of the argument

Return type:  int or None

GetArgumentPositionInMessage()[¶](#tts.core.api.dataBrowserApi.DataBrowser.LoggingEntity.GetArgumentPositionInMessage "Link to this definition")  
Returns the argument’s bit position relative to the message if this logging entity is a logging argument of protocol “DLT (non-verbose)” else None

Returns:  The argument’s bit position

Return type:  int or None

GetDescription()[¶](#tts.core.api.dataBrowserApi.DataBrowser.LoggingEntity.GetDescription "Link to this definition")  
Returns the description of this logging entity

Returns:  The description

Return type:  str

GetFilterDescription()[¶](#tts.core.api.dataBrowserApi.DataBrowser.LoggingEntity.GetFilterDescription "Link to this definition")  
Returns the filter description if this logging message of protocol “DLT (verbose)”, otherwise None

Returns:  Dict with filter attribute name as key and filter value as value. The filter values are of type bool for flags, and type str for text values, IDs and regular expressions. Regular expressions are introduced with “RegEx: “. If an attribute is not filtered, its value is None.

Return type:  dict\<str, str|bool\> or None

GetId()[¶](#tts.core.api.dataBrowserApi.DataBrowser.LoggingEntity.GetId "Link to this definition")  
Returns the message identifier if this logging entity is a logging message else None

Returns:  The identifier

Return type:  str or None

GetMessageLength()[¶](#tts.core.api.dataBrowserApi.DataBrowser.LoggingEntity.GetMessageLength "Link to this definition")  
Returns the length of the message in bytes if this logging entity is a logging message of protocol “DLT (non-verbose)” else None

Returns:  The length of the message

Return type:  int or None

GetName()[¶](#tts.core.api.dataBrowserApi.DataBrowser.LoggingEntity.GetName "Link to this definition")  
Returns the name of this logging entity

Returns:  The name

Return type:  str

GetPath()[¶](#tts.core.api.dataBrowserApi.DataBrowser.LoggingEntity.GetPath "Link to this definition")  
Returns the variablepath of this logging entity

Returns:  The variablepath (/\<messageName\>/\<argumentName\>/)

Return type:  str

GetPhysValue(*rawValue*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.LoggingEntity.GetPhysValue "Link to this definition")  
Returns the physical value of given raw value

Note

Only valid for logging arguments of protocol “DLT (non-verbose)”

Returns:  The physical value of given raw value

Return type:  float

GetRawValue(*value*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.LoggingEntity.GetRawValue "Link to this definition")  
Returns the raw value of given value

Note

Value can be text or physical value. Only valid for logging arguments of protocol “DLT (non-verbose)”

Returns:  The raw value of given value

Return type:  int

GetTxEcuNames()[¶](#tts.core.api.dataBrowserApi.DataBrowser.LoggingEntity.GetTxEcuNames "Link to this definition")  
Returns the names of the ECUs which transmit this message/signal

Note

Only valid for protocol “DLT (non-verbose)”

Returns:  The names of the ECUs

Return type:  list\<str\>

IsArgument()[¶](#tts.core.api.dataBrowserApi.DataBrowser.LoggingEntity.IsArgument "Link to this definition")  
Checks if this logging entity is a logging argument

Returns:  True if this entity is a logging argument else False

Return type:  bool

IsMessage()[¶](#tts.core.api.dataBrowserApi.DataBrowser.LoggingEntity.IsMessage "Link to this definition")  
Checks if this logging entity is a logging message

Returns:  True if this entity is a logging message else False

Return type:  bool

### MediaBrowser[¶](#mediabrowser "Link to this heading")

*class* MediaBrowser[¶](#tts.testModule.multimedia.dataBrowser.MediaBrowser.MediaBrowser "Link to this definition")  
The MediaBrowser provides access to images and masks from the file system.

Images can be accessed via the Images property. E.g. mediaBrowser.Images.myImage. This will return an object of type [`Image`](mediadatastructures.md#tts.testModule.multimedia.dataElements.Image.Image "tts.testModule.multimedia.dataElements.Image.Image").

Masks can be accessed via the Masks property. E.g. mediaBrowser.Masks.myMask. This will return an object of type [`Mask`](mediadatastructures.md#tts.testModule.multimedia.dataElements.Mask.Mask "tts.testModule.multimedia.dataElements.Mask.Mask").

Example:  
Suppose there is a file called “myImage.png” in the image directory that is associated with the media node “CAM”. Then you could access it with:

    >>> api.DataBrowser.BrowseMultimedia("CAM").Images.myImage

### ModelBrowser[¶](#modelbrowser "Link to this heading")

*class* ModelBrowser[¶](#tts.core.api.dataBrowserApi.DataBrowser.ModelBrowser "Link to this definition")  
The ModelBrowser provides an interface to a model database. It is possible to search the available variable paths.

FindVariables(*searchString*, *maxResults=None*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.ModelBrowser.FindVariables "Link to this definition")  
Find all variables in the model tree whose full model path matches the given search string. The search may include the wildcards ‘\*’ and ‘?’. Only leaf elements of the model tree are returned. These are either parameters, signals or virtual signals of the model.

Parameters:  - **searchString** (*str*) – string for search

- **maxResults** (*int* *|* *None*) – maximal number of returned found items

Returns:  list of found model paths

Return type:  list \<str\>

### ServiceBrowser[¶](#servicebrowser "Link to this heading")

*class* ServiceBrowser[¶](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser "Link to this definition")  
The ServiceBrowser type provides an interface to a service database which allows to access information regarding ECUs, services, methods, events etc.

GetE2EProfile(*ecuName*, *serviceName*, *methodOrEventName*, *eventgroupName=None*, *fieldName=None*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetE2EProfile "Link to this definition")  
Returns the E2E profile configuration of an event or a field or a method

Note

A method may have different profiles for input and output parameters. Profiles 4 and 7 are currently supported.

Parameters:  - **ecuName** (*str*) – The name of the ECU

- **serviceName** (*str*) – The name of the service

- **methodOrEventName** (*str*) – The event or method name

- **eventgroupName** (*str* *or* *None*) – The name of the event group or None

- **fieldName** (*str* *or* *None*) – The name of the field or None

Return type:  dict

Note

The key is the extended name of the E2E input “in” or return “out” parameter. The values are E2E configuration parameters. The validity of each of the configuration parameters depends on the E2E profile. See the item “category”.

GetEcuConsumerInfos(*providerEcuName*, *serviceName*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetEcuConsumerInfos "Link to this definition")  
Returns network infos of the consumer ECUs of the service, that is specified by a given serviceName and a providerEcuName. Use only for ARXMLs of version AUTOSAR_00048 or higher. If the port is assigned dynamically at runtime, the key ‘Port’ will return ‘dynamic’.

Parameters:  - **providerEcuName** (*str*) – The name of the providing ECU

- **serviceName** (*str*) – The name of the service

Returns:  Network infos ecuName, IP, TP=UDP|TCP, Port of consuming ECUs as list of dicts with the keys: ecuName, IP, TP (transport protocol = UDP|TCP), Port (\<int\>|’dynamic’)

Return type:  list \<dict\>

GetEcuConsumerNamesByServiceName(*serviceName*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetEcuConsumerNamesByServiceName "Link to this definition")  
Returns the ECUs the given service is consumed by

Parameters:  **serviceName** (*str*) – The name of the service

Returns:  The names of the events

Return type:  list \<str\>

GetEcuNamesByServiceName(*serviceName*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetEcuNamesByServiceName "Link to this definition")  
Returns the ECUs the given service is provided by

Parameters:  **serviceName** (*str*) – The name of the service

Returns:  The names of the ECUs

Return type:  list \<str\>

GetEcus()[¶](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetEcus "Link to this definition")  
Returns all ECU names

Returns:  The names of the ECUs

Return type:  list \<str\>

GetEventGroupInfos(*ecuName*, *serviceName*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetEventGroupInfos "Link to this definition")  
Returns name and ID of all event groups of a given service

Parameters:  - **ecuName** (*str*) – The Name of the ECU

- **serviceName** (*str*) – The name of the service

Returns:  List of tuples with name and ID of all event groups

Return type:  list \<tuple \<str, int\> \>

GetEventInfos(*ecuName*, *serviceName*, *eventgroupName*, *fieldName=None*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetEventInfos "Link to this definition")  
Returns name and ID of all events of a given event group

Parameters:  - **ecuName** (*str*) – The name of the ECU

- **serviceName** (*str*) – The name of the service

- **eventgroupName** (*str*) – The name of the event group

- **fieldName** (*str* *or* *None*) – (Optional) The name of the field

Returns:  List of tuples with name and ID of all events

Return type:  list \<tuple \<str, int\> \>

GetFieldNamesByServiceName(*ecuName*, *serviceName*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetFieldNamesByServiceName "Link to this definition")  
Returns field names of a given service

Parameters:  - **ecuName** (*str*) – The name of the ECU

- **serviceName** (*str*) – The name of the service

Returns:  The names of the fields

Return type:  list \<str\>

GetInputParameterRepresentation(*ecuName*, *serviceName*, *methodOrEventName*, *eventgroupName=None*, *fieldName=None*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetInputParameterRepresentation "Link to this definition")  
Returns a nested dict which contains the type definitions of all input values of an event, a field or a method.

Parameters:  - **ecuName** (*str*) – name of the ECU

- **serviceName** (*str*) – name of the service

- **methodOrEventName** (*str*) – event or method name

- **eventgroupName** (*str / None*) – name of the event group or None

- **fieldName** (*str / None*) – name of the field or None

Return type:  dict

GetInstanceID(*ecuName*, *serviceName*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetInstanceID "Link to this definition")  
Returns the instance ID of a given service

Parameters:  - **ecuName** (*str*) – The name of the ECU

- **serviceName** (*str*) – The name of the service

Returns:  The instance ID

Return type:  str or None

GetMethodInfos(*ecuName*, *serviceName*, *fieldName=None*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetMethodInfos "Link to this definition")  
Returns name and ID of all methods of a given service

Parameters:  - **ecuName** (*str*) – The name of the ECU

- **serviceName** (*str*) – The name of the service

- **fieldName** (*str* *or* *None*) – (Optional) The name of the field

Returns:  List of tuples with name and ID of all methods

Return type:  list \<tuple \<str, int\> \>

GetOfferCyclicDelay(*ecuName*, *serviceName*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetOfferCyclicDelay "Link to this definition")  
Returns the delay between cyclic offers in seconds of a given service

Parameters:  - **ecuName** (*str*) – The name of the ECU

- **serviceName** (*str*) – The name of the service

Returns:  Cyclic offers in seconds

Return type:  float or None

GetReturnParameterRepresentation(*ecuName*, *serviceName*, *methodOrEventName*, *eventgroupName=None*, *fieldName=None*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetReturnParameterRepresentation "Link to this definition")  
Returns a nested dict which contains the type definitions of all return values of an event, a field or a method.

Parameters:  - **ecuName** (*str*) – name of the ECU

- **serviceName** (*str*) – name of the service

- **methodOrEventName** (*str*) – event or method name

- **eventgroupName** (*str / None*) – name of the event group or None

- **fieldName** (*str / None*) – name of the field or None

Return type:  dict

GetServiceAdressInfos(*ecuName*, *serviceName*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetServiceAdressInfos "Link to this definition")  
Returns all provider adress infos of a given service

Parameters:  - **ecuName** (*str*) – The name of the ECU

- **serviceName** (*str*) – The name of the service

Returns:  Dict with provider adress ‘IP’ and ‘TCP’ or ‘UDP’ source port

Return type:  \<dict\>

GetServiceID(*ecuName*, *serviceName*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetServiceID "Link to this definition")  
Returns the service ID of a given service

Parameters:  - **ecuName** (*str*) – The name of the ECU

- **serviceName** (*str*) – The name of the service

Returns:  The service ID

Return type:  str or None

GetServiceInfos(*ecuName=None*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetServiceInfos "Link to this definition")  
Returns name and ID of all provided services (of a given ECU)

Parameters:  **ecuName** (*str* *or* *None*) – (Optional) Name of the ECU

Returns:  List of tuples with name and ID of services

Return type:  dict \<tuple \<str, int\> \>

GetTimings(*ecuName*, *serviceName*, *methodName*, *eventgroupName=None*, *fieldName=None*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetTimings "Link to this definition")  
Returns timing information of a given event or method

Parameters:  - **ecuName** (*str*) – The name of the ECU

- **serviceName** (*str*) – The name of the service

- **methodName** (*str*) – The name of the method

- **eventgroupName** (*str* *or* *None*) – (Optional) The name of the event group

- **fieldName** (*str* *or* *None*) – (Optional) The name of the field

Returns:  Dict with keys ‘ApplicationCycleTime’, ‘DebounceTimeRange’, ‘RequestDebounceTimeRange’, ‘TpSeparationTime’ and their values

Return type:  dict

GetVersion(*ecuName*, *serviceName*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetVersion "Link to this definition")  
Returns the minor and major version of a given service

Parameters:  - **ecuName** (*str*) – The name of the ECU

- **serviceName** (*str*) – The name of the service

Returns:  Tuple with the minor and major version

Return type:  tuple \<int, int\>

GetVlanInfo(*ecuName*, *serviceName*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetVlanInfo "Link to this definition")  
Returns the VLAN ID and the default priority of a given service

Parameters:  - **ecuName** (*str*) – The name of the ECU

- **serviceName** (*str*) – nThe name of the service

Returns:  VLAN ID and the default priority

Return type:  tuple(int, int)

### SgbdBrowser[¶](#sgbdbrowser "Link to this heading")

*class* SgbdBrowser[¶](#tts.core.api.dataBrowserApi.DataBrowser.SgbdBrowser "Link to this definition")  
The SgbdBrowser type provides an interface to a SGBD file. It is possible to retrieve information for a single entry or to use a full text search to get a list of filtered entries. Every entity is represented by an instance of the type [`SgbdEntity`](#tts.core.api.dataBrowserApi.DataBrowser.SgbdEntity "tts.core.api.dataBrowserApi.DataBrowser.SgbdEntity").

Note

prototype

GetJob(*jobName*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.SgbdBrowser.GetJob "Link to this definition")  
Returns the SgbdEntity of a Job if it exists in selected SGBD or None if does not

Parameters:  **jobName** (*str*) – Name of job to get

Returns:  [`SgbdEntity`](#tts.core.api.dataBrowserApi.DataBrowser.SgbdEntity "tts.core.api.dataBrowserApi.DataBrowser.SgbdEntity") for the first matching job or None

Return type:  [`SgbdEntity`](#tts.core.api.dataBrowserApi.DataBrowser.SgbdEntity "tts.core.api.dataBrowserApi.DataBrowser.SgbdEntity") or None

GetListTableNames()[¶](#tts.core.api.dataBrowserApi.DataBrowser.SgbdBrowser.GetListTableNames "Link to this definition")  
Returns a list which contains all SGBD table names

Returns:  A list with all SGBD table names

Return type:  list \<str\>

IsJob(*jobName*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.SgbdBrowser.IsJob "Link to this definition")  
Returns True if Job exists in selected SGBD or False if not

Parameters:  **jobName** (*str*) – The name of job to be checked

Returns:  True if Job exists or False if not

Return type:  bool

ListJobs(*filter=''*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.SgbdBrowser.ListJobs "Link to this definition")  
Returns a list which contains instances of SgbdEntity whose matches the specified job search string

Parameters:  **filter** (*str*) – The search string which is part of a job

Returns:  A list of SgbdEntity instances if the SGBD file contains entries with the given search string, otherwise an empty list

Return type:  list \<[`SgbdEntity`](#tts.core.api.dataBrowserApi.DataBrowser.SgbdEntity "tts.core.api.dataBrowserApi.DataBrowser.SgbdEntity")\>

Note

prototype

QueryTableByArgument(*job=None*, *argument=None*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.SgbdBrowser.QueryTableByArgument "Link to this definition")  
Returns a dictionary representing a specific argument table of the given job

Parameters:  - **job** (*str*) – The name of the job

- **argument** (*str*) – The name of the argument

Returns:  A dictionary representing the columns of the argument table

Return type:  dict

QueryTableByName(*tableName=None*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.SgbdBrowser.QueryTableByName "Link to this definition")  
Returns the SGBD table indicated by the given name

Parameters:  **tableName** (*str*) – The name of a SGBD table

Returns:  A dictionary representing the columns of the SGBD table

Return type:  dict

QueryTableByResult(*job=None*, *result=None*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.SgbdBrowser.QueryTableByResult "Link to this definition")  
Returns a dictionary representing a specific result table of the given job

Parameters:  - **job** (*str*) – The name of the job

- **result** (*str*) – The name of the result

Returns:  A dictionary representing the columns of the result table

Return type:  dict

### SgbdEntity[¶](#sgbdentity "Link to this heading")

*class* SgbdEntity[¶](#tts.core.api.dataBrowserApi.DataBrowser.SgbdEntity "Link to this definition")  
The SgbdEntity type represents one entry in a SGBD file.

Note

prototype

GetArgumentType(*argumentName*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.SgbdEntity.GetArgumentType "Link to this definition")  
Returns the argument type of this SGBD entity argument name

Parameters:  **argumentName** (*str*) – The argument name

Returns:  The argument type

Return type:  str

GetArguments()[¶](#tts.core.api.dataBrowserApi.DataBrowser.SgbdEntity.GetArguments "Link to this definition")  
Returns the arguments of this SGBD entity

Returns:  The arguments

Return type:  list \<str\>

Note

prototype

GetDescription()[¶](#tts.core.api.dataBrowserApi.DataBrowser.SgbdEntity.GetDescription "Link to this definition")  
Returns the description of this SGBD entity

Returns:  The description

Return type:  str

Note

prototype

GetName()[¶](#tts.core.api.dataBrowserApi.DataBrowser.SgbdEntity.GetName "Link to this definition")  
Returns the name of this SGBD entity

Returns:  The name

Return type:  str

Note

prototype

GetResultType(*resultName*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.SgbdEntity.GetResultType "Link to this definition")  
Returns the result type of this SGBD entity result name

Parameters:  **resultName** (*str*) – The result name

Returns:  The result type

Return type:  str

GetResults()[¶](#tts.core.api.dataBrowserApi.DataBrowser.SgbdEntity.GetResults "Link to this definition")  
Returns the results of this SGBD entity

Returns:  The results

Return type:  list \<str\>

Note

prototype

## UnitInfo[¶](#unitinfo "Link to this heading")

### UnitInfo[¶](#module-tts.core.api.dataBrowserApi.UnitInfo "Link to this heading")

*class* UnitInfo[¶](#tts.core.api.dataBrowserApi.UnitInfo.UnitInfo "Link to this definition")  
UnitInfo provides functions to retrieve information concerning unit definitions

Convert(*value*, *srcUnit*, *dstUnit*)[¶](#tts.core.api.dataBrowserApi.UnitInfo.UnitInfo.Convert "Link to this definition")  
Converts the given value from a source unit into the destination unit

Note

A unitless size (noUnit) cannot be converted.

Parameters:  - **value** (*float*) – Numeric value in source unit to be converted

- **srcUnit** (*str*) – Name of source unit

- **dstUnit** (*str*) – Name of destination unit

Returns:  Converted numeric value in destination unit, or None, if not convertable

Return type:  float or None

GetDimension(*unitString*)[¶](#tts.core.api.dataBrowserApi.UnitInfo.UnitInfo.GetDimension "Link to this definition")  
Provides the dimension of a unit

Parameters:  **unitString** (*str*) – Name of unit

Returns:  Dimension or None if unit unknown

Return type:  str or None

HasUnit(*unitString*)[¶](#tts.core.api.dataBrowserApi.UnitInfo.UnitInfo.HasUnit "Link to this definition")  
Checks whether the unit is defined in the units definition file

Parameters:  **unitString** (*str*) – Name of unit

Returns:  True or False

Return type:  bool
