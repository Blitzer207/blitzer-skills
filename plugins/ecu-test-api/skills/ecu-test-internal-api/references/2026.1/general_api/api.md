Internal APIs [ Internal APIs ](#)

Internal APIs

- [ API entry point ](#api-entry-point)
  - [ API ](#module-tts.core.api.internalApi.Api)
    - [C Api ](#tts.core.api.internalApi.Api.Api)
      - [A AnalysisEnvironment ](#tts.core.api.internalApi.Api.Api.AnalysisEnvironment)
      - [A Credentials ](#tts.core.api.internalApi.Api.Api.Credentials)
      - [A CurrentTestConfiguration ](#tts.core.api.internalApi.Api.Api.CurrentTestConfiguration)
      - [A CurrentTestbenchConfiguration ](#tts.core.api.internalApi.Api.Api.CurrentTestbenchConfiguration)
      - [A DataBrowser ](#tts.core.api.internalApi.Api.Api.DataBrowser)
      - [A Ethernet ](#tts.core.api.internalApi.Api.Api.Ethernet)
      - [A GlobalConstants ](#tts.core.api.internalApi.Api.Api.GlobalConstants)
      - [A KeywordCatalog ](#tts.core.api.internalApi.Api.Api.KeywordCatalog)
      - [A Math ](#tts.core.api.internalApi.Api.Api.Math)
      - [A Multimedia ](#tts.core.api.internalApi.Api.Api.Multimedia)
      - [A ObjectApi ](#tts.core.api.internalApi.Api.Api.ObjectApi)
      - [A Scm ](#tts.core.api.internalApi.Api.Api.Scm)
      - [A Service ](#tts.core.api.internalApi.Api.Api.Service)
      - [A TestBench ](#tts.core.api.internalApi.Api.Api.TestBench)
      - [A TestEnvironment ](#tts.core.api.internalApi.Api.Api.TestEnvironment)
      - [A TestManagement ](#tts.core.api.internalApi.Api.Api.TestManagement)
      - [A ToolAccess ](#tts.core.api.internalApi.Api.Api.ToolAccess)
      - [A UnitInfo ](#tts.core.api.internalApi.Api.Api.UnitInfo)
      - [A Workspace ](#tts.core.api.internalApi.Api.Api.Workspace)
      - [M GeneratePackageDocumentation ](#tts.core.api.internalApi.Api.Api.GeneratePackageDocumentation)
      - [M GetAppName ](#tts.core.api.internalApi.Api.Api.GetAppName)
      - [M GetSetting ](#tts.core.api.internalApi.Api.Api.GetSetting)
      - [M GetVersion ](#tts.core.api.internalApi.Api.Api.GetVersion)
      - [M IsRunner ](#tts.core.api.internalApi.Api.Api.IsRunner)
- [ API classes ](#api-classes)
  - [ AnalysisEnvironment ](#analysisenvironment)
    - [C AnalysisEnvironment ](#tts.core.api.internalApi.AnalysisEnvironment.AnalysisEnvironment)
      - [A ExecutionInfo ](#tts.core.api.internalApi.AnalysisEnvironment.AnalysisEnvironment.ExecutionInfo)
      - [M ClearSignalCache ](#tts.core.api.internalApi.AnalysisEnvironment.AnalysisEnvironment.ClearSignalCache)
  - [ AnalysisExecutionInfo ](#analysisexecutioninfo)
    - [C AnalysisExecutionInfo ](#tts.core.api.internalApi.AnalysisExecutionInfo.AnalysisExecutionInfo)
      - [A JobResult ](#tts.core.api.internalApi.AnalysisExecutionInfo.AnalysisExecutionInfo.JobResult)
      - [A LogFolder ](#tts.core.api.internalApi.AnalysisExecutionInfo.AnalysisExecutionInfo.LogFolder)
      - [A ReportDb ](#tts.core.api.internalApi.AnalysisExecutionInfo.AnalysisExecutionInfo.ReportDb)
      - [A ReportDbFolder ](#tts.core.api.internalApi.AnalysisExecutionInfo.AnalysisExecutionInfo.ReportDbFolder)
      - [A StartTime ](#tts.core.api.internalApi.AnalysisExecutionInfo.AnalysisExecutionInfo.StartTime)
      - [A TargetReportDbFolder ](#tts.core.api.internalApi.AnalysisExecutionInfo.AnalysisExecutionInfo.TargetReportDbFolder)
      - [M GetCurrentPackageFilename ](#tts.core.api.internalApi.AnalysisExecutionInfo.AnalysisExecutionInfo.GetCurrentPackageFilename)
      - [M GetMainPackageFilename ](#tts.core.api.internalApi.AnalysisExecutionInfo.AnalysisExecutionInfo.GetMainPackageFilename)
      - [M GetWatchTime ](#tts.core.api.internalApi.AnalysisExecutionInfo.AnalysisExecutionInfo.GetWatchTime)
      - [M StartWatch ](#tts.core.api.internalApi.AnalysisExecutionInfo.AnalysisExecutionInfo.StartWatch)
  - [ BusSystem ](#bussystem)
    - [C BusSystem ](#tts.core.api.internalApi.BusSystem.BusSystem)
      - [A Channel ](#tts.core.api.internalApi.BusSystem.BusSystem.Channel)
      - [A Database ](#tts.core.api.internalApi.BusSystem.BusSystem.Database)
      - [A Name ](#tts.core.api.internalApi.BusSystem.BusSystem.Name)
  - [ BusSystems ](#bussystems)
    - [C BusSystems ](#tts.core.api.internalApi.BusSystems.BusSystems)
      - [A Count ](#tts.core.api.internalApi.BusSystems.BusSystems.Count)
      - [M Item ](#tts.core.api.internalApi.BusSystems.BusSystems.Item)
  - [ Constant ](#constant)
    - [C Constant ](#tts.core.api.internalApi.Constant.Constant)
      - [A Description ](#tts.core.api.internalApi.Constant.Constant.Description)
      - [A Name ](#tts.core.api.internalApi.Constant.Constant.Name)
      - [A Value ](#tts.core.api.internalApi.Constant.Constant.Value)
  - [ Constants ](#constants)
    - [C Constants ](#tts.core.api.internalApi.Constants.Constants)
      - [A Count ](#tts.core.api.internalApi.Constants.Constants.Count)
      - [M Item ](#tts.core.api.internalApi.Constants.Constants.Item)
  - [ Ecu ](#ecu)
    - [C Ecu ](#tts.core.api.internalApi.Ecu.Ecu)
      - [A A2l ](#tts.core.api.internalApi.Ecu.Ecu.A2l)
      - [A DebugHex ](#tts.core.api.internalApi.Ecu.Ecu.DebugHex)
      - [A Elf ](#tts.core.api.internalApi.Ecu.Ecu.Elf)
      - [A Elfs ](#tts.core.api.internalApi.Ecu.Ecu.Elfs)
      - [A Hex ](#tts.core.api.internalApi.Ecu.Ecu.Hex)
      - [A Name ](#tts.core.api.internalApi.Ecu.Ecu.Name)
      - [A Sgbd ](#tts.core.api.internalApi.Ecu.Ecu.Sgbd)
  - [ Ecus ](#ecus)
    - [C Ecus ](#tts.core.api.internalApi.Ecus.Ecus)
      - [A Count ](#tts.core.api.internalApi.Ecus.Ecus.Count)
      - [M Item ](#tts.core.api.internalApi.Ecus.Ecus.Item)
  - [ EnvironmentCommunication ](#environmentcommunication)
    - [C EnvironmentCommunication ](#tts.testModule.envCom.internalApi.EnvironmentCommunication.EnvironmentCommunication)
      - [A Name ](#tts.testModule.envCom.internalApi.EnvironmentCommunication.EnvironmentCommunication.Name)
  - [ EnvironmentCommunications ](#environmentcommunications)
    - [C EnvironmentCommunications ](#tts.testModule.envCom.internalApi.EnvironmentCommunications.EnvironmentCommunications)
      - [A Count ](#tts.testModule.envCom.internalApi.EnvironmentCommunications.EnvironmentCommunications.Count)
      - [M Item ](#tts.testModule.envCom.internalApi.EnvironmentCommunications.EnvironmentCommunications.Item)
  - [ EnvironmentSimulation ](#environmentsimulation)
    - [C EnvironmentSimulation ](#tts.testModule.envSim.internalApi.EnvironmentSimulation.EnvironmentSimulation)
      - [A Name ](#tts.testModule.envSim.internalApi.EnvironmentSimulation.EnvironmentSimulation.Name)
      - [A OfflineFile ](#tts.testModule.envSim.internalApi.EnvironmentSimulation.EnvironmentSimulation.OfflineFile)
  - [ EnvironmentSimulations ](#environmentsimulations)
    - [C EnvironmentSimulations ](#tts.testModule.envSim.internalApi.EnvironmentSimulations.EnvironmentSimulations)
      - [A Count ](#tts.testModule.envSim.internalApi.EnvironmentSimulations.EnvironmentSimulations.Count)
      - [M Item ](#tts.testModule.envSim.internalApi.EnvironmentSimulations.EnvironmentSimulations.Item)
  - [ GlobalConstants ](#globalconstants)
    - [C GlobalConstants ](#tts.core.api.internalApi.GlobalConstants.GlobalConstants)
      - [M GetConstant ](#tts.core.api.internalApi.GlobalConstants.GlobalConstants.GetConstant)
      - [M GetConstants ](#tts.core.api.internalApi.GlobalConstants.GlobalConstants.GetConstants)
    - [V ORIGIN_DEFINED_AT_RUNTIME ](#tts.core.api.internalApi.GlobalConstants.ORIGIN_DEFINED_AT_RUNTIME)
    - [V ORIGIN_MANIPULATED_AT_RUNTIME ](#tts.core.api.internalApi.GlobalConstants.ORIGIN_MANIPULATED_AT_RUNTIME)
  - [ KeywordCatalog ](#keywordcatalog)
    - [C KeywordCatalogApi ](#tts.core.api.internalApi.KeywordCatalogApi.KeywordCatalogApi)
      - [M Connect ](#tts.core.api.internalApi.KeywordCatalogApi.KeywordCatalogApi.Connect)
      - [M GetAvailableCatalogs ](#tts.core.api.internalApi.KeywordCatalogApi.KeywordCatalogApi.GetAvailableCatalogs)
      - [M GetAvailableProjects ](#tts.core.api.internalApi.KeywordCatalogApi.KeywordCatalogApi.GetAvailableProjects)
      - [M GetAvailableVariants ](#tts.core.api.internalApi.KeywordCatalogApi.KeywordCatalogApi.GetAvailableVariants)
      - [M GetCurrentCatalogName ](#tts.core.api.internalApi.KeywordCatalogApi.KeywordCatalogApi.GetCurrentCatalogName)
      - [M GetCurrentProject ](#tts.core.api.internalApi.KeywordCatalogApi.KeywordCatalogApi.GetCurrentProject)
      - [M GetCurrentVariant ](#tts.core.api.internalApi.KeywordCatalogApi.KeywordCatalogApi.GetCurrentVariant)
      - [M IsConnected ](#tts.core.api.internalApi.KeywordCatalogApi.KeywordCatalogApi.IsConnected)
      - [M LoadCatalog ](#tts.core.api.internalApi.KeywordCatalogApi.KeywordCatalogApi.LoadCatalog)
      - [M SetProject ](#tts.core.api.internalApi.KeywordCatalogApi.KeywordCatalogApi.SetProject)
      - [M SetVariant ](#tts.core.api.internalApi.KeywordCatalogApi.KeywordCatalogApi.SetVariant)
  - [ Math ](#id16)
  - [ Model ](#model)
    - [C Model ](#tts.core.api.internalApi.Model.Model)
      - [A Name ](#tts.core.api.internalApi.Model.Model.Name)
  - [ Models ](#models)
    - [C Models ](#tts.core.api.internalApi.Models.Models)
      - [A Count ](#tts.core.api.internalApi.Models.Models.Count)
      - [M Item ](#tts.core.api.internalApi.Models.Models.Item)
  - [ Multimedia ](#multimedia)
    - [C ImageFiltersApi ](#tts.testModule.multimedia.api.MultimediaApi.ImageFiltersApi)
    - [C MultimediaApi ](#tts.testModule.multimedia.api.MultimediaApi.MultimediaApi)
      - [A ImageFilters ](#tts.testModule.multimedia.api.MultimediaApi.MultimediaApi.ImageFilters)
      - [M GetAvailableOCRServices ](#tts.testModule.multimedia.api.MultimediaApi.MultimediaApi.GetAvailableOCRServices)
      - [M GetAvailableObjectDetectors ](#tts.testModule.multimedia.api.MultimediaApi.MultimediaApi.GetAvailableObjectDetectors)
      - [M GetAvailableSTTProfiles ](#tts.testModule.multimedia.api.MultimediaApi.MultimediaApi.GetAvailableSTTProfiles)
      - [M GetAvailableTTSVoices ](#tts.testModule.multimedia.api.MultimediaApi.MultimediaApi.GetAvailableTTSVoices)
      - [M GetDefaultOCRService ](#tts.testModule.multimedia.api.MultimediaApi.MultimediaApi.GetDefaultOCRService)
      - [M GetOCRService ](#tts.testModule.multimedia.api.MultimediaApi.MultimediaApi.GetOCRService)
      - [M GetObjectDetector ](#tts.testModule.multimedia.api.MultimediaApi.MultimediaApi.GetObjectDetector)
      - [M SpeechToText ](#tts.testModule.multimedia.api.MultimediaApi.MultimediaApi.SpeechToText)
      - [M TextToSpeech ](#tts.testModule.multimedia.api.MultimediaApi.MultimediaApi.TextToSpeech)
  - [ Scm ](#scm)
    - [C Scm ](#tts.core.api.internalApi.Scm.Scm)
      - [M GetCheckoutRevision ](#tts.core.api.internalApi.Scm.Scm.GetCheckoutRevision)
      - [M GetFileRevision ](#tts.core.api.internalApi.Scm.Scm.GetFileRevision)
      - [M GetFileStatus ](#tts.core.api.internalApi.Scm.Scm.GetFileStatus)
      - [M GetUrl ](#tts.core.api.internalApi.Scm.Scm.GetUrl)
  - [ Service ](#service)
    - [C Service ](#tts.core.api.internalApi.Service.Service)
      - [M GetUsedServices ](#tts.core.api.internalApi.Service.Service.GetUsedServices)
      - [M GenerateService ](#tts.core.api.internalApi.Service.Service.GenerateService)
      - [M GetPort ](#tts.core.api.internalApi.Service.Service.GetPort)
    - [C ServicePort ](#tts.core.api.internalApi.Service.ServicePort)
      - [M GetService ](#tts.core.api.internalApi.Service.ServicePort.GetService)
      - [M StartService ](#tts.core.api.internalApi.Service.ServicePort.StartService)
      - [M StopService ](#tts.core.api.internalApi.Service.ServicePort.StopService)
    - [C ServiceProxy ](#tts.core.api.internalApi.Service.ServiceProxy)
      - [M GetFunctionsHelp ](#tts.core.api.internalApi.Service.ServiceProxy.GetFunctionsHelp)
      - [M GetServiceFunctions ](#tts.core.api.internalApi.Service.ServiceProxy.GetServiceFunctions)
  - [ TestBench ](#testbench)
    - [C TestBench ](#tts.core.api.internalApi.TestBench.TestBench)
      - [M GetPortStatus ](#tts.core.api.internalApi.TestBench.TestBench.GetPortStatus)
      - [M GetToolStatus ](#tts.core.api.internalApi.TestBench.TestBench.GetToolStatus)
      - [M StartTool ](#tts.core.api.internalApi.TestBench.TestBench.StartTool)
      - [M StopTool ](#tts.core.api.internalApi.TestBench.TestBench.StopTool)
  - [ TestbenchConfiguration ](#testbenchconfiguration)
    - [C TestbenchConfiguration ](#tts.core.api.internalApi.TestbenchConfiguration.TestbenchConfiguration)
      - [A Filename ](#tts.core.api.internalApi.TestbenchConfiguration.TestbenchConfiguration.Filename)
      - [A ToolList ](#tts.core.api.internalApi.TestbenchConfiguration.TestbenchConfiguration.ToolList)
      - [M GetToolhostInfo ](#tts.core.api.internalApi.TestbenchConfiguration.TestbenchConfiguration.GetToolhostInfo)
  - [ TestbenchTool ](#testbenchtool)
    - [C TestbenchTool ](#tts.core.api.internalApi.TestbenchTool.TestbenchTool)
      - [A Jobs ](#tts.core.api.internalApi.TestbenchTool.TestbenchTool.Jobs)
      - [A Location ](#tts.core.api.internalApi.TestbenchTool.TestbenchTool.Location)
      - [A Name ](#tts.core.api.internalApi.TestbenchTool.TestbenchTool.Name)
      - [A PortList ](#tts.core.api.internalApi.TestbenchTool.TestbenchTool.PortList)
      - [A Ports ](#tts.core.api.internalApi.TestbenchTool.TestbenchTool.Ports)
      - [A ToolId ](#tts.core.api.internalApi.TestbenchTool.TestbenchTool.ToolId)
      - [A Version ](#tts.core.api.internalApi.TestbenchTool.TestbenchTool.Version)
  - [ TestConfiguration ](#id25)
    - [C TestConfiguration ](#tts.core.api.internalApi.TestConfiguration.TestConfiguration)
      - [A BusSystems ](#tts.core.api.internalApi.TestConfiguration.TestConfiguration.BusSystems)
      - [A Ecus ](#tts.core.api.internalApi.TestConfiguration.TestConfiguration.Ecus)
      - [A EnvironmentCommunications ](#tts.core.api.internalApi.TestConfiguration.TestConfiguration.EnvironmentCommunications)
      - [A EnvironmentSimulations ](#tts.core.api.internalApi.TestConfiguration.TestConfiguration.EnvironmentSimulations)
      - [A Filename ](#tts.core.api.internalApi.TestConfiguration.TestConfiguration.Filename)
      - [A GlobalConstants ](#tts.core.api.internalApi.TestConfiguration.TestConfiguration.GlobalConstants)
      - [A Models ](#tts.core.api.internalApi.TestConfiguration.TestConfiguration.Models)
      - [A NameTester ](#tts.core.api.internalApi.TestConfiguration.TestConfiguration.NameTester)
      - [M ReloadGlobalMapping ](#tts.core.api.internalApi.TestConfiguration.TestConfiguration.ReloadGlobalMapping)
  - [ TestEnvironment ](#testenvironment)
    - [C TestEnvironment ](#tts.core.api.internalApi.TestEnvironment.TestEnvironment)
      - [A ExecutionInfo ](#tts.core.api.internalApi.TestEnvironment.TestEnvironment.ExecutionInfo)
      - [M GenerateTestReportDocumentFromDB ](#tts.core.api.internalApi.TestEnvironment.TestEnvironment.GenerateTestReportDocumentFromDB)
      - [M GetPackageReferences ](#tts.core.api.internalApi.TestEnvironment.TestEnvironment.GetPackageReferences)
      - [M TimeElapsing ](#tts.core.api.internalApi.TestEnvironment.TestEnvironment.TimeElapsing)
      - [M Wait ](#tts.core.api.internalApi.TestEnvironment.TestEnvironment.Wait)
  - [ TestExecutionInfo ](#testexecutioninfo)
    - [C ExecutionExceptionInfo ](#tts.core.api.internalApi.TestExecutionInfo.ExecutionExceptionInfo)
      - [M GetMessage ](#tts.core.api.internalApi.TestExecutionInfo.ExecutionExceptionInfo.GetMessage)
      - [M GetTestStepPortId ](#tts.core.api.internalApi.TestExecutionInfo.ExecutionExceptionInfo.GetTestStepPortId)
      - [M GetTestStepToolId ](#tts.core.api.internalApi.TestExecutionInfo.ExecutionExceptionInfo.GetTestStepToolId)
      - [M GetTestStepType ](#tts.core.api.internalApi.TestExecutionInfo.ExecutionExceptionInfo.GetTestStepType)
      - [M GetType ](#tts.core.api.internalApi.TestExecutionInfo.ExecutionExceptionInfo.GetType)
    - [C KeywordInfo ](#tts.core.api.internalApi.TestExecutionInfo.KeywordInfo)
      - [M GetArgumentUnit ](#tts.core.api.internalApi.TestExecutionInfo.KeywordInfo.GetArgumentUnit)
      - [M GetArguments ](#tts.core.api.internalApi.TestExecutionInfo.KeywordInfo.GetArguments)
      - [M GetComponentType ](#tts.core.api.internalApi.TestExecutionInfo.KeywordInfo.GetComponentType)
      - [M GetCurrentTimeOptionIteration ](#tts.core.api.internalApi.TestExecutionInfo.KeywordInfo.GetCurrentTimeOptionIteration)
      - [M GetId ](#tts.core.api.internalApi.TestExecutionInfo.KeywordInfo.GetId)
      - [M GetReturnUnit ](#tts.core.api.internalApi.TestExecutionInfo.KeywordInfo.GetReturnUnit)
      - [M GetReturns ](#tts.core.api.internalApi.TestExecutionInfo.KeywordInfo.GetReturns)
      - [M GetTimeOptionDuration ](#tts.core.api.internalApi.TestExecutionInfo.KeywordInfo.GetTimeOptionDuration)
      - [M GetTimeOptionMode ](#tts.core.api.internalApi.TestExecutionInfo.KeywordInfo.GetTimeOptionMode)
      - [M GetTimeOptionPollingCycle ](#tts.core.api.internalApi.TestExecutionInfo.KeywordInfo.GetTimeOptionPollingCycle)
      - [M GetTimeOptionTimeout ](#tts.core.api.internalApi.TestExecutionInfo.KeywordInfo.GetTimeOptionTimeout)
      - [M IsControlTestStep ](#tts.core.api.internalApi.TestExecutionInfo.KeywordInfo.IsControlTestStep)
      - [M IsEstablishTestStep ](#tts.core.api.internalApi.TestExecutionInfo.KeywordInfo.IsEstablishTestStep)
      - [M IsStateTestStep ](#tts.core.api.internalApi.TestExecutionInfo.KeywordInfo.IsStateTestStep)
    - [C TestExecutionInfo ](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo)
      - [A AllProjectsStepCount ](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.AllProjectsStepCount)
      - [A AllProjectsStepsExecuted ](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.AllProjectsStepsExecuted)
      - [A CurrentLineNumber ](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.CurrentLineNumber)
      - [A CurrentTestStepHierarchy ](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.CurrentTestStepHierarchy)
      - [A KeywordInfo ](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.KeywordInfo)
      - [A LastTestStepResult ](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.LastTestStepResult)
      - [A LogFolder ](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.LogFolder)
      - [A MainProjectStepCount ](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.MainProjectStepCount)
      - [A MainProjectStepsExecuted ](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.MainProjectStepsExecuted)
      - [A PackageResult ](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.PackageResult)
      - [A ProjectResult ](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.ProjectResult)
      - [A ProjectStartTime ](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.ProjectStartTime)
      - [A ReportDb ](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.ReportDb)
      - [A ReportDbFolder ](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.ReportDbFolder)
      - [A RunningTime ](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.RunningTime)
      - [A StartTime ](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.StartTime)
      - [A TargetReportDbFolder ](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.TargetReportDbFolder)
      - [M AddArtifact ](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.AddArtifact)
      - [M AddTestStepReportDetail ](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.AddTestStepReportDetail)
      - [M GetCurrentPackageFilename ](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.GetCurrentPackageFilename)
      - [M GetCurrentPackagePath ](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.GetCurrentPackagePath)
      - [M GetCurrentProjectFilename ](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.GetCurrentProjectFilename)
      - [M GetCurrentProjectPath ](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.GetCurrentProjectPath)
      - [M GetExecutionExceptionInfo ](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.GetExecutionExceptionInfo)
      - [M GetExecutionMode ](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.GetExecutionMode)
      - [M GetKeywordInfo ](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.GetKeywordInfo)
      - [M GetMainPackageFilename ](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.GetMainPackageFilename)
      - [M GetMainPackagePath ](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.GetMainPackagePath)
      - [M GetMappingNames ](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.GetMappingNames)
      - [M GetMappingTargetPath ](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.GetMappingTargetPath)
      - [M GetWatchTime ](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.GetWatchTime)
      - [M IsAbortRequested ](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.IsAbortRequested)
      - [M IsAborted ](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.IsAborted)
      - [M IsInMain ](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.IsInMain)
      - [M IsInPostcondition ](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.IsInPostcondition)
      - [M IsInPrecondition ](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.IsInPrecondition)
      - [M IsInteractiveExecution ](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.IsInteractiveExecution)
      - [M StartWatch ](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.StartWatch)
  - [ TestManagement ](#module-tts.core.api.internalApi.TestManagement)
    - [C TestManagementApi ](#tts.core.api.internalApi.TestManagement.TestManagementApi)
      - [M GetTestScriptByID ](#tts.core.api.internalApi.TestManagement.TestManagementApi.GetTestScriptByID)
  - [ ToolAccess ](#toolaccess)
    - [C JobExecutor ](#tts.core.api.internalApi.ToolAccess.JobExecutor)
      - [M Execute ](#tts.core.api.internalApi.ToolAccess.JobExecutor.Execute)
    - [C ToolAccess ](#tts.core.api.internalApi.ToolAccess.ToolAccess)
      - [M GetPortJobExecutor ](#tts.core.api.internalApi.ToolAccess.ToolAccess.GetPortJobExecutor)
      - [M GetToolJobExecutor ](#tts.core.api.internalApi.ToolAccess.ToolAccess.GetToolJobExecutor)
  - [ Workspace ](#workspace)
    - [C Finding ](#tts.core.api.internalApi.Workspace.Finding)
    - [C Workspace ](#tts.core.api.internalApi.Workspace.Workspace)
      - [M Check ](#tts.core.api.internalApi.Workspace.Workspace.Check)
- [ Credentials API ](#credentials-api)
  - [ Introduction ](#module-tts.core.api.internalApi.credentialsApi.Credentials)
    - [ Keystores ](#keystores)
    - [ Managing Keystores ](#managing-keystores)
    - [ Accessing Keystores ](#accessing-keystores)
    - [ Secrets ](#secrets)
    - [ Managing the Vault ](#managing-the-vault)
    - [ Security ](#security)
    - [ Examples ](#examples)
  - [ Credentials ](#credentials)
    - [C Credentials ](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials)
      - [A Certificate ](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials.Certificate)
      - [M ChangeLoginCredentials ](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials.ChangeLoginCredentials)
      - [M Close ](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials.Close)
      - [M CreateCryptFileVault ](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials.CreateCryptFileVault)
      - [M CreatePkcs12KeyStore ](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials.CreatePkcs12KeyStore)
      - [M CreateSecret ](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials.CreateSecret)
      - [M DeleteVaultEntry ](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials.DeleteVaultEntry)
      - [M GetAvailableVaultEntries ](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials.GetAvailableVaultEntries)
      - [M GetTesterKey ](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials.GetTesterKey)
      - [M GetVaultEntry ](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials.GetVaultEntry)
      - [M LoadPkcs12KeyStore ](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials.LoadPkcs12KeyStore)
      - [M OpenCryptFileVault ](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials.OpenCryptFileVault)
      - [M OpenVault ](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials.OpenVault)
      - [A PrivateKey ](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials.PrivateKey)
      - [A PublicKey ](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials.PublicKey)
      - [M Save ](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials.Save)
      - [A SeedAndKey ](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials.SeedAndKey)
  - [ KeyStore ](#keystore)
    - [C KeyStore ](#tts.core.api.internalApi.credentialsApi.KeyStore.KeyStore)
      - [M Delete ](#tts.core.api.internalApi.credentialsApi.KeyStore.KeyStore.Delete)
      - [M GetCertificate ](#tts.core.api.internalApi.credentialsApi.KeyStore.KeyStore.GetCertificate)
      - [M GetCertificateChain ](#tts.core.api.internalApi.credentialsApi.KeyStore.KeyStore.GetCertificateChain)
      - [M GetCertificates ](#tts.core.api.internalApi.credentialsApi.KeyStore.KeyStore.GetCertificates)
      - [M GetPrivateKey ](#tts.core.api.internalApi.credentialsApi.KeyStore.KeyStore.GetPrivateKey)
  - [ Secret ](#secret)
    - [C Secret ](#tts.core.api.internalApi.credentialsApi.Secret.Secret)
      - [M AssociatedData ](#tts.core.api.internalApi.credentialsApi.Secret.Secret.AssociatedData)
      - [M Delete ](#tts.core.api.internalApi.credentialsApi.Secret.Secret.Delete)
      - [M Reveal ](#tts.core.api.internalApi.credentialsApi.Secret.Secret.Reveal)
  - [ Certificate ](#certificate)
    - [C Certificate ](#tts.core.api.internalApi.credentialsApi.Certificate.Certificate)
      - [M Base64 ](#tts.core.api.internalApi.credentialsApi.Certificate.Certificate.Base64)
      - [M CommonName ](#tts.core.api.internalApi.credentialsApi.Certificate.Certificate.CommonName)
      - [M DER ](#tts.core.api.internalApi.credentialsApi.Certificate.Certificate.DER)
      - [M FromBase64 ](#tts.core.api.internalApi.credentialsApi.Certificate.Certificate.FromBase64)
      - [M FromDER ](#tts.core.api.internalApi.credentialsApi.Certificate.Certificate.FromDER)
      - [M FromFile ](#tts.core.api.internalApi.credentialsApi.Certificate.Certificate.FromFile)
      - [M FromPEM ](#tts.core.api.internalApi.credentialsApi.Certificate.Certificate.FromPEM)
      - [M IsValid ](#tts.core.api.internalApi.credentialsApi.Certificate.Certificate.IsValid)
      - [M Issuer ](#tts.core.api.internalApi.credentialsApi.Certificate.Certificate.Issuer)
      - [M PEM ](#tts.core.api.internalApi.credentialsApi.Certificate.Certificate.PEM)
      - [M PublicKey ](#tts.core.api.internalApi.credentialsApi.Certificate.Certificate.PublicKey)
      - [M Subject ](#tts.core.api.internalApi.credentialsApi.Certificate.Certificate.Subject)
      - [M Verify ](#tts.core.api.internalApi.credentialsApi.Certificate.Certificate.Verify)
  - [ PrivateKey ](#privatekey)
    - [C PrivateKey ](#tts.core.api.internalApi.credentialsApi.PrivateKey.PrivateKey)
      - [M FromBase64 ](#tts.core.api.internalApi.credentialsApi.PrivateKey.PrivateKey.FromBase64)
      - [M FromDER ](#tts.core.api.internalApi.credentialsApi.PrivateKey.PrivateKey.FromDER)
      - [M FromFile ](#tts.core.api.internalApi.credentialsApi.PrivateKey.PrivateKey.FromFile)
      - [M FromPEM ](#tts.core.api.internalApi.credentialsApi.PrivateKey.PrivateKey.FromPEM)
      - [M PublicKey ](#tts.core.api.internalApi.credentialsApi.PrivateKey.PrivateKey.PublicKey)
      - [M Sign ](#tts.core.api.internalApi.credentialsApi.PrivateKey.PrivateKey.Sign)
  - [ PublicKey ](#publickey)
    - [C PublicKey ](#tts.core.api.internalApi.credentialsApi.PublicKey.PublicKey)
      - [M Base64 ](#tts.core.api.internalApi.credentialsApi.PublicKey.PublicKey.Base64)
      - [M DER ](#tts.core.api.internalApi.credentialsApi.PublicKey.PublicKey.DER)
      - [M FromBase64 ](#tts.core.api.internalApi.credentialsApi.PublicKey.PublicKey.FromBase64)
      - [M FromDER ](#tts.core.api.internalApi.credentialsApi.PublicKey.PublicKey.FromDER)
      - [M FromFile ](#tts.core.api.internalApi.credentialsApi.PublicKey.PublicKey.FromFile)
      - [M FromPEM ](#tts.core.api.internalApi.credentialsApi.PublicKey.PublicKey.FromPEM)
      - [M PEM ](#tts.core.api.internalApi.credentialsApi.PublicKey.PublicKey.PEM)
      - [M Verify ](#tts.core.api.internalApi.credentialsApi.PublicKey.PublicKey.Verify)
  - [ SeedAndKey ](#seedandkey)
    - [C SeedAndKey ](#tts.core.api.internalApi.credentialsApi.SeedAndKey.SeedAndKey)
      - [A Diag ](#tts.core.api.internalApi.credentialsApi.SeedAndKey.SeedAndKey.Diag)
      - [A Xcp ](#tts.core.api.internalApi.credentialsApi.SeedAndKey.SeedAndKey.Xcp)
  - [ DiagSeedAndKey ](#diagseedandkey)
    - [C DiagSeedAndKey ](#tts.core.api.internalApi.credentialsApi.SeedAndKey.DiagSeedAndKey)
      - [M FromLib ](#tts.core.api.internalApi.credentialsApi.SeedAndKey.DiagSeedAndKey.FromLib)
      - [M GenerateKeyEx ](#tts.core.api.internalApi.credentialsApi.SeedAndKey.DiagSeedAndKey.GenerateKeyEx)
      - [M GenerateKeyExOpt ](#tts.core.api.internalApi.credentialsApi.SeedAndKey.DiagSeedAndKey.GenerateKeyExOpt)
  - [ XcpSeedAndKey ](#xcpseedandkey)
    - [C XcpSeedAndKey ](#tts.core.api.internalApi.credentialsApi.SeedAndKey.XcpSeedAndKey)
      - [M ComputeKeyFromSeed ](#tts.core.api.internalApi.credentialsApi.SeedAndKey.XcpSeedAndKey.ComputeKeyFromSeed)
      - [M FromLib ](#tts.core.api.internalApi.credentialsApi.SeedAndKey.XcpSeedAndKey.FromLib)
      - [M GetAvailablePrivileges ](#tts.core.api.internalApi.credentialsApi.SeedAndKey.XcpSeedAndKey.GetAvailablePrivileges)
- [ DataBrowser ](#module-tts.core.api.dataBrowserApi.DataBrowser)
  - [ A2lBrowser ](#a2lbrowser)
    - [C A2lBrowser ](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser)
      - [M CalcPhysToRaw ](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.CalcPhysToRaw)
      - [M CalcRawToPhys ](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.CalcRawToPhys)
      - [M GetA2lEntity ](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.GetA2lEntity)
      - [M GetAcquisitionRateNames ](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.GetAcquisitionRateNames)
      - [M GetCodeCheckInformation ](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.GetCodeCheckInformation)
      - [M GetEpkInformation ](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.GetEpkInformation)
      - [M GetFunctionCharacteristics ](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.GetFunctionCharacteristics)
      - [M GetFunctionInMeasurements ](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.GetFunctionInMeasurements)
      - [M GetFunctionLocMeasurements ](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.GetFunctionLocMeasurements)
      - [M GetFunctionNames ](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.GetFunctionNames)
      - [M GetFunctionOutMeasurements ](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.GetFunctionOutMeasurements)
      - [M GetFunctionVersion ](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.GetFunctionVersion)
      - [M GetLabelNameList ](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.GetLabelNameList)
      - [M GetSubFunctionNames ](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.GetSubFunctionNames)
      - [M GetSystemConstantNameList ](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.GetSystemConstantNameList)
      - [M GetSystemConstantValue ](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.GetSystemConstantValue)
      - [M HasFunction ](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.HasFunction)
      - [M HasSubFunctions ](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.HasSubFunctions)
      - [M IsCharacteristic ](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.IsCharacteristic)
      - [M IsMeasurement ](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.IsMeasurement)
      - [M ReadDataFromHex ](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.ReadDataFromHex)
  - [ A2lEntity ](#a2lentity)
    - [C A2lEntity ](#tts.core.api.dataBrowserApi.DataBrowser.A2lEntity)
      - [M GetAddress ](#tts.core.api.dataBrowserApi.DataBrowser.A2lEntity.GetAddress)
      - [M GetByteOrder ](#tts.core.api.dataBrowserApi.DataBrowser.A2lEntity.GetByteOrder)
      - [M GetCoeffsDict ](#tts.core.api.dataBrowserApi.DataBrowser.A2lEntity.GetCoeffsDict)
      - [M GetCompuMethodName ](#tts.core.api.dataBrowserApi.DataBrowser.A2lEntity.GetCompuMethodName)
      - [M GetDataType ](#tts.core.api.dataBrowserApi.DataBrowser.A2lEntity.GetDataType)
      - [M GetDescription ](#tts.core.api.dataBrowserApi.DataBrowser.A2lEntity.GetDescription)
      - [M GetDisplayIdentifier ](#tts.core.api.dataBrowserApi.DataBrowser.A2lEntity.GetDisplayIdentifier)
      - [M GetLowerLimit ](#tts.core.api.dataBrowserApi.DataBrowser.A2lEntity.GetLowerLimit)
      - [M GetMatrixDim ](#tts.core.api.dataBrowserApi.DataBrowser.A2lEntity.GetMatrixDim)
      - [M GetName ](#tts.core.api.dataBrowserApi.DataBrowser.A2lEntity.GetName)
      - [M GetSize ](#tts.core.api.dataBrowserApi.DataBrowser.A2lEntity.GetSize)
      - [M GetUnit ](#tts.core.api.dataBrowserApi.DataBrowser.A2lEntity.GetUnit)
      - [M GetUpperLimit ](#tts.core.api.dataBrowserApi.DataBrowser.A2lEntity.GetUpperLimit)
      - [M GetValueType ](#tts.core.api.dataBrowserApi.DataBrowser.A2lEntity.GetValueType)
      - [M GetVtabDict ](#tts.core.api.dataBrowserApi.DataBrowser.A2lEntity.GetVtabDict)
  - [ BusBrowser ](#busbrowser)
    - [C BusBrowser ](#tts.core.api.dataBrowserApi.DataBrowser.BusBrowser)
      - [M GetFrameNamesByPDUName ](#tts.core.api.dataBrowserApi.DataBrowser.BusBrowser.GetFrameNamesByPDUName)
      - [M GetLinScheduleTables ](#tts.core.api.dataBrowserApi.DataBrowser.BusBrowser.GetLinScheduleTables)
      - [M GetSDGsAndSDs ](#tts.core.api.dataBrowserApi.DataBrowser.BusBrowser.GetSDGsAndSDs)
      - [M ListFrames ](#tts.core.api.dataBrowserApi.DataBrowser.BusBrowser.ListFrames)
      - [M ListPDUs ](#tts.core.api.dataBrowserApi.DataBrowser.BusBrowser.ListPDUs)
      - [M ListSignals ](#tts.core.api.dataBrowserApi.DataBrowser.BusBrowser.ListSignals)
      - [M ListSignalsByPDU ](#tts.core.api.dataBrowserApi.DataBrowser.BusBrowser.ListSignalsByPDU)
  - [ BusEntity ](#busentity)
    - [C BusEntity ](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity)
      - [M GetActivations ](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetActivations)
      - [M GetByteOrder ](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetByteOrder)
      - [M GetCycleRepetition ](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetCycleRepetition)
      - [M GetDebounceTime ](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetDebounceTime)
      - [M GetDescription ](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetDescription)
      - [M GetE2EProfile ](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetE2EProfile)
      - [M GetFrameLength ](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetFrameLength)
      - [M GetFrameType ](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetFrameType)
      - [M GetId ](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetId)
      - [M GetLinearCoeffs ](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetLinearCoeffs)
      - [M GetLongName ](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetLongName)
      - [M GetMaxRawValue ](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetMaxRawValue)
      - [M GetMaxValue ](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetMaxValue)
      - [M GetMinRawValue ](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetMinRawValue)
      - [M GetMinValue ](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetMinValue)
      - [M GetMultiplexerSwitchCode ](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetMultiplexerSwitchCode)
      - [M GetName ](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetName)
      - [M GetOriginalName ](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetOriginalName)
      - [M GetPDULength ](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetPDULength)
      - [M GetPDUPosition ](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetPDUPosition)
      - [M GetPDUUpdateBit ](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetPDUUpdateBit)
      - [M GetPath ](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetPath)
      - [M GetPhysValue ](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetPhysValue)
      - [M GetRawValue ](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetRawValue)
      - [M GetRxEcuNames ](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetRxEcuNames)
      - [M GetSecOcDataId ](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetSecOcDataId)
      - [M GetSignalDataPositionInFrame ](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetSignalDataPositionInFrame)
      - [M GetSignalDataPositionInPDU ](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetSignalDataPositionInPDU)
      - [M GetSignalLength ](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetSignalLength)
      - [M GetStartCycle ](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetStartCycle)
      - [M GetSystemSignalName ](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetSystemSignalName)
      - [M GetTextTable ](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetTextTable)
      - [M GetTimeOffset ](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetTimeOffset)
      - [M GetTimings ](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetTimings)
      - [M GetTxEcuNames ](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetTxEcuNames)
      - [M GetUnit ](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetUnit)
      - [M IsFrame ](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.IsFrame)
      - [M IsMultiplexer ](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.IsMultiplexer)
      - [M IsNode ](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.IsNode)
      - [M IsPDU ](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.IsPDU)
      - [M IsSend ](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.IsSend)
      - [M IsSignal ](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.IsSignal)
  - [ DataBrowser ](#id31)
    - [C DataBrowser ](#tts.core.api.dataBrowserApi.DataBrowser.DataBrowser)
      - [M BrowseA2l ](#tts.core.api.dataBrowserApi.DataBrowser.DataBrowser.BrowseA2l)
      - [M BrowseBus ](#tts.core.api.dataBrowserApi.DataBrowser.DataBrowser.BrowseBus)
      - [M BrowseDebug ](#tts.core.api.dataBrowserApi.DataBrowser.DataBrowser.BrowseDebug)
      - [M BrowseDebugElf ](#tts.core.api.dataBrowserApi.DataBrowser.DataBrowser.BrowseDebugElf)
      - [M BrowseDiag ](#tts.core.api.dataBrowserApi.DataBrowser.DataBrowser.BrowseDiag)
      - [M BrowseLogging ](#tts.core.api.dataBrowserApi.DataBrowser.DataBrowser.BrowseLogging)
      - [M BrowseModel ](#tts.core.api.dataBrowserApi.DataBrowser.DataBrowser.BrowseModel)
      - [M BrowseMultimedia ](#tts.core.api.dataBrowserApi.DataBrowser.DataBrowser.BrowseMultimedia)
      - [M BrowseService ](#tts.core.api.dataBrowserApi.DataBrowser.DataBrowser.BrowseService)
      - [M BrowseSgbd ](#tts.core.api.dataBrowserApi.DataBrowser.DataBrowser.BrowseSgbd)
  - [ DebugBrowser ](#debugbrowser)
    - [C DebugBrowser ](#tts.core.api.dataBrowserApi.DataBrowser.DebugBrowser)
      - [M GetCores ](#tts.core.api.dataBrowserApi.DataBrowser.DebugBrowser.GetCores)
      - [M GetElfFiles ](#tts.core.api.dataBrowserApi.DataBrowser.DebugBrowser.GetElfFiles)
      - [M GetModules ](#tts.core.api.dataBrowserApi.DataBrowser.DebugBrowser.GetModules)
      - [M GetRegisters ](#tts.core.api.dataBrowserApi.DataBrowser.DebugBrowser.GetRegisters)
      - [M GetVariables ](#tts.core.api.dataBrowserApi.DataBrowser.DebugBrowser.GetVariables)
  - [ DiagBrowser ](#diagbrowser)
    - [C DiagBrowser ](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagBrowser)
      - [M GetDiagDtcs ](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagBrowser.GetDiagDtcs)
      - [M GetDiagServices ](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagBrowser.GetDiagServices)
      - [M GetDiagStateCharts ](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagBrowser.GetDiagStateCharts)
  - [ DiagDtcEntity ](#diagdtcentity)
    - [C DiagDtcEntity ](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagDtcEntity)
      - [M GetSdgs ](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagDtcEntity.GetSdgs)
      - [M GetShortName ](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagDtcEntity.GetShortName)
      - [M GetTroubleCode ](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagDtcEntity.GetTroubleCode)
  - [ DiagServiceEntity ](#diagserviceentity)
    - [C DiagServiceEntity ](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagServiceEntity)
      - [M GetLongName ](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagServiceEntity.GetLongName)
      - [M GetPreconditions ](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagServiceEntity.GetPreconditions)
      - [M GetSdgs ](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagServiceEntity.GetSdgs)
      - [M GetServiceId ](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagServiceEntity.GetServiceId)
      - [M GetServiceName ](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagServiceEntity.GetServiceName)
      - [M GetShortName ](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagServiceEntity.GetShortName)
      - [M GetTransitions ](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagServiceEntity.GetTransitions)
  - [ DiagStateChartEntity ](#diagstatechartentity)
    - [C DiagStateChartEntity ](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateChartEntity)
      - [M GetLongName ](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateChartEntity.GetLongName)
      - [M GetSemantic ](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateChartEntity.GetSemantic)
      - [M GetShortName ](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateChartEntity.GetShortName)
      - [M GetStartState ](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateChartEntity.GetStartState)
      - [M GetStateChartId ](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateChartEntity.GetStateChartId)
      - [M GetStates ](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateChartEntity.GetStates)
      - [M GetTransitions ](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateChartEntity.GetTransitions)
  - [ DiagStateEntity ](#diagstateentity)
    - [C DiagStateEntity ](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateEntity)
      - [M GetEndingTransitions ](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateEntity.GetEndingTransitions)
      - [M GetLongName ](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateEntity.GetLongName)
      - [M GetShortName ](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateEntity.GetShortName)
      - [M GetStartingTransitions ](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateEntity.GetStartingTransitions)
      - [M GetStateChart ](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateEntity.GetStateChart)
      - [M GetStateId ](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateEntity.GetStateId)
  - [ DiagStateTransitionEntity ](#diagstatetransitionentity)
    - [C DiagStateTransitionEntity ](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateTransitionEntity)
      - [M GetLongName ](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateTransitionEntity.GetLongName)
      - [M GetServices ](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateTransitionEntity.GetServices)
      - [M GetShortName ](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateTransitionEntity.GetShortName)
      - [M GetSourceState ](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateTransitionEntity.GetSourceState)
      - [M GetStateChart ](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateTransitionEntity.GetStateChart)
      - [M GetTargetState ](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateTransitionEntity.GetTargetState)
      - [M GetTransitionId ](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateTransitionEntity.GetTransitionId)
  - [ LoggingBrowser ](#loggingbrowser)
    - [C LoggingBrowser ](#tts.core.api.dataBrowserApi.DataBrowser.LoggingBrowser)
      - [M GetProtocol ](#tts.core.api.dataBrowserApi.DataBrowser.LoggingBrowser.GetProtocol)
      - [M ListArguments ](#tts.core.api.dataBrowserApi.DataBrowser.LoggingBrowser.ListArguments)
      - [M ListMessages ](#tts.core.api.dataBrowserApi.DataBrowser.LoggingBrowser.ListMessages)
  - [ LoggingEntity ](#loggingentity)
    - [C LoggingEntity ](#tts.core.api.dataBrowserApi.DataBrowser.LoggingEntity)
      - [M GetArgumentLength ](#tts.core.api.dataBrowserApi.DataBrowser.LoggingEntity.GetArgumentLength)
      - [M GetArgumentPositionInMessage ](#tts.core.api.dataBrowserApi.DataBrowser.LoggingEntity.GetArgumentPositionInMessage)
      - [M GetDescription ](#tts.core.api.dataBrowserApi.DataBrowser.LoggingEntity.GetDescription)
      - [M GetFilterDescription ](#tts.core.api.dataBrowserApi.DataBrowser.LoggingEntity.GetFilterDescription)
      - [M GetId ](#tts.core.api.dataBrowserApi.DataBrowser.LoggingEntity.GetId)
      - [M GetMessageLength ](#tts.core.api.dataBrowserApi.DataBrowser.LoggingEntity.GetMessageLength)
      - [M GetName ](#tts.core.api.dataBrowserApi.DataBrowser.LoggingEntity.GetName)
      - [M GetPath ](#tts.core.api.dataBrowserApi.DataBrowser.LoggingEntity.GetPath)
      - [M GetPhysValue ](#tts.core.api.dataBrowserApi.DataBrowser.LoggingEntity.GetPhysValue)
      - [M GetRawValue ](#tts.core.api.dataBrowserApi.DataBrowser.LoggingEntity.GetRawValue)
      - [M GetTxEcuNames ](#tts.core.api.dataBrowserApi.DataBrowser.LoggingEntity.GetTxEcuNames)
      - [M IsArgument ](#tts.core.api.dataBrowserApi.DataBrowser.LoggingEntity.IsArgument)
      - [M IsMessage ](#tts.core.api.dataBrowserApi.DataBrowser.LoggingEntity.IsMessage)
  - [ MediaBrowser ](#mediabrowser)
    - [C MediaBrowser ](#tts.testModule.multimedia.dataBrowser.MediaBrowser.MediaBrowser)
  - [ ModelBrowser ](#modelbrowser)
    - [C ModelBrowser ](#tts.core.api.dataBrowserApi.DataBrowser.ModelBrowser)
      - [M FindVariables ](#tts.core.api.dataBrowserApi.DataBrowser.ModelBrowser.FindVariables)
  - [ ServiceBrowser ](#servicebrowser)
    - [C ServiceBrowser ](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser)
      - [M GetE2EProfile ](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetE2EProfile)
      - [M GetEcuConsumerInfos ](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetEcuConsumerInfos)
      - [M GetEcuConsumerNamesByServiceName ](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetEcuConsumerNamesByServiceName)
      - [M GetEcuNamesByServiceName ](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetEcuNamesByServiceName)
      - [M GetEcus ](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetEcus)
      - [M GetEventGroupInfos ](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetEventGroupInfos)
      - [M GetEventInfos ](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetEventInfos)
      - [M GetFieldNamesByServiceName ](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetFieldNamesByServiceName)
      - [M GetInputParameterRepresentation ](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetInputParameterRepresentation)
      - [M GetInstanceID ](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetInstanceID)
      - [M GetMethodInfos ](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetMethodInfos)
      - [M GetOfferCyclicDelay ](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetOfferCyclicDelay)
      - [M GetReturnParameterRepresentation ](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetReturnParameterRepresentation)
      - [M GetSDGsAndSDs ](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetSDGsAndSDs)
      - [M GetServiceAdressInfos ](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetServiceAdressInfos)
      - [M GetServiceID ](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetServiceID)
      - [M GetServiceInfos ](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetServiceInfos)
      - [M GetTimings ](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetTimings)
      - [M GetVersion ](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetVersion)
      - [M GetVlanInfo ](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetVlanInfo)
  - [ SgbdBrowser ](#sgbdbrowser)
    - [C SgbdBrowser ](#tts.core.api.dataBrowserApi.DataBrowser.SgbdBrowser)
      - [M GetJob ](#tts.core.api.dataBrowserApi.DataBrowser.SgbdBrowser.GetJob)
      - [M GetListTableNames ](#tts.core.api.dataBrowserApi.DataBrowser.SgbdBrowser.GetListTableNames)
      - [M IsJob ](#tts.core.api.dataBrowserApi.DataBrowser.SgbdBrowser.IsJob)
      - [M ListJobs ](#tts.core.api.dataBrowserApi.DataBrowser.SgbdBrowser.ListJobs)
      - [M QueryTableByArgument ](#tts.core.api.dataBrowserApi.DataBrowser.SgbdBrowser.QueryTableByArgument)
      - [M QueryTableByName ](#tts.core.api.dataBrowserApi.DataBrowser.SgbdBrowser.QueryTableByName)
      - [M QueryTableByResult ](#tts.core.api.dataBrowserApi.DataBrowser.SgbdBrowser.QueryTableByResult)
  - [ SgbdEntity ](#sgbdentity)
    - [C SgbdEntity ](#tts.core.api.dataBrowserApi.DataBrowser.SgbdEntity)
      - [M GetArgumentType ](#tts.core.api.dataBrowserApi.DataBrowser.SgbdEntity.GetArgumentType)
      - [M GetArguments ](#tts.core.api.dataBrowserApi.DataBrowser.SgbdEntity.GetArguments)
      - [M GetDescription ](#tts.core.api.dataBrowserApi.DataBrowser.SgbdEntity.GetDescription)
      - [M GetName ](#tts.core.api.dataBrowserApi.DataBrowser.SgbdEntity.GetName)
      - [M GetResultType ](#tts.core.api.dataBrowserApi.DataBrowser.SgbdEntity.GetResultType)
      - [M GetResults ](#tts.core.api.dataBrowserApi.DataBrowser.SgbdEntity.GetResults)
- [ UnitInfo ](#unitinfo)
  - [ UnitInfo ](#module-tts.core.api.dataBrowserApi.UnitInfo)
    - [C UnitInfo ](#tts.core.api.dataBrowserApi.UnitInfo.UnitInfo)
      - [M Convert ](#tts.core.api.dataBrowserApi.UnitInfo.UnitInfo.Convert)
      - [M GetDimension ](#tts.core.api.dataBrowserApi.UnitInfo.UnitInfo.GetDimension)
      - [M HasUnit ](#tts.core.api.dataBrowserApi.UnitInfo.UnitInfo.HasUnit)

[ Advanced operations of package variable types ](variabledatastructures.md)

[ Advanced properties of bus-related objects ](busdatastructures.md)

[ Bus related objects of trace analysis ](busdatastructuresTraceanalysis.md)

[ Advanced properties of diagnostics-related objects ](diagdatastructures.md)

[ Diagnostics related objects of trace analysis ](diagdatastructuresTraceanalysis.md)

[ Advanced properties of media-related objects ](mediadatastructures.md)

[ Advanced properties of DLT logging-related objects ](dltdatastructures.md)

[ COM API ](com-api.md)

[ REST API ](rest-api.md)

[ Report API ](apireport.md)

[ Object API ](objectApi.md)

[ Trace Analysis API ](../TraceAnalysisAPI/index.md)

[ Generator APIs ](../generators/index.md)

[ Tools ](../tools/index.md)

[ User test management ](../userTestmanagement/index.md)

[ UserUtility API ](../user-utility/user-utility.md)

[ Utility Examples ](../user-utility/example-utilities.md)

Internal APIs

- [ API entry point ](#api-entry-point)
  - [ API ](#module-tts.core.api.internalApi.Api)
    - [C Api ](#tts.core.api.internalApi.Api.Api)
      - [A AnalysisEnvironment ](#tts.core.api.internalApi.Api.Api.AnalysisEnvironment)
      - [A Credentials ](#tts.core.api.internalApi.Api.Api.Credentials)
      - [A CurrentTestConfiguration ](#tts.core.api.internalApi.Api.Api.CurrentTestConfiguration)
      - [A CurrentTestbenchConfiguration ](#tts.core.api.internalApi.Api.Api.CurrentTestbenchConfiguration)
      - [A DataBrowser ](#tts.core.api.internalApi.Api.Api.DataBrowser)
      - [A Ethernet ](#tts.core.api.internalApi.Api.Api.Ethernet)
      - [A GlobalConstants ](#tts.core.api.internalApi.Api.Api.GlobalConstants)
      - [A KeywordCatalog ](#tts.core.api.internalApi.Api.Api.KeywordCatalog)
      - [A Math ](#tts.core.api.internalApi.Api.Api.Math)
      - [A Multimedia ](#tts.core.api.internalApi.Api.Api.Multimedia)
      - [A ObjectApi ](#tts.core.api.internalApi.Api.Api.ObjectApi)
      - [A Scm ](#tts.core.api.internalApi.Api.Api.Scm)
      - [A Service ](#tts.core.api.internalApi.Api.Api.Service)
      - [A TestBench ](#tts.core.api.internalApi.Api.Api.TestBench)
      - [A TestEnvironment ](#tts.core.api.internalApi.Api.Api.TestEnvironment)
      - [A TestManagement ](#tts.core.api.internalApi.Api.Api.TestManagement)
      - [A ToolAccess ](#tts.core.api.internalApi.Api.Api.ToolAccess)
      - [A UnitInfo ](#tts.core.api.internalApi.Api.Api.UnitInfo)
      - [A Workspace ](#tts.core.api.internalApi.Api.Api.Workspace)
      - [M GeneratePackageDocumentation ](#tts.core.api.internalApi.Api.Api.GeneratePackageDocumentation)
      - [M GetAppName ](#tts.core.api.internalApi.Api.Api.GetAppName)
      - [M GetSetting ](#tts.core.api.internalApi.Api.Api.GetSetting)
      - [M GetVersion ](#tts.core.api.internalApi.Api.Api.GetVersion)
      - [M IsRunner ](#tts.core.api.internalApi.Api.Api.IsRunner)
- [ API classes ](#api-classes)
  - [ AnalysisEnvironment ](#analysisenvironment)
    - [C AnalysisEnvironment ](#tts.core.api.internalApi.AnalysisEnvironment.AnalysisEnvironment)
      - [A ExecutionInfo ](#tts.core.api.internalApi.AnalysisEnvironment.AnalysisEnvironment.ExecutionInfo)
      - [M ClearSignalCache ](#tts.core.api.internalApi.AnalysisEnvironment.AnalysisEnvironment.ClearSignalCache)
  - [ AnalysisExecutionInfo ](#analysisexecutioninfo)
    - [C AnalysisExecutionInfo ](#tts.core.api.internalApi.AnalysisExecutionInfo.AnalysisExecutionInfo)
      - [A JobResult ](#tts.core.api.internalApi.AnalysisExecutionInfo.AnalysisExecutionInfo.JobResult)
      - [A LogFolder ](#tts.core.api.internalApi.AnalysisExecutionInfo.AnalysisExecutionInfo.LogFolder)
      - [A ReportDb ](#tts.core.api.internalApi.AnalysisExecutionInfo.AnalysisExecutionInfo.ReportDb)
      - [A ReportDbFolder ](#tts.core.api.internalApi.AnalysisExecutionInfo.AnalysisExecutionInfo.ReportDbFolder)
      - [A StartTime ](#tts.core.api.internalApi.AnalysisExecutionInfo.AnalysisExecutionInfo.StartTime)
      - [A TargetReportDbFolder ](#tts.core.api.internalApi.AnalysisExecutionInfo.AnalysisExecutionInfo.TargetReportDbFolder)
      - [M GetCurrentPackageFilename ](#tts.core.api.internalApi.AnalysisExecutionInfo.AnalysisExecutionInfo.GetCurrentPackageFilename)
      - [M GetMainPackageFilename ](#tts.core.api.internalApi.AnalysisExecutionInfo.AnalysisExecutionInfo.GetMainPackageFilename)
      - [M GetWatchTime ](#tts.core.api.internalApi.AnalysisExecutionInfo.AnalysisExecutionInfo.GetWatchTime)
      - [M StartWatch ](#tts.core.api.internalApi.AnalysisExecutionInfo.AnalysisExecutionInfo.StartWatch)
  - [ BusSystem ](#bussystem)
    - [C BusSystem ](#tts.core.api.internalApi.BusSystem.BusSystem)
      - [A Channel ](#tts.core.api.internalApi.BusSystem.BusSystem.Channel)
      - [A Database ](#tts.core.api.internalApi.BusSystem.BusSystem.Database)
      - [A Name ](#tts.core.api.internalApi.BusSystem.BusSystem.Name)
  - [ BusSystems ](#bussystems)
    - [C BusSystems ](#tts.core.api.internalApi.BusSystems.BusSystems)
      - [A Count ](#tts.core.api.internalApi.BusSystems.BusSystems.Count)
      - [M Item ](#tts.core.api.internalApi.BusSystems.BusSystems.Item)
  - [ Constant ](#constant)
    - [C Constant ](#tts.core.api.internalApi.Constant.Constant)
      - [A Description ](#tts.core.api.internalApi.Constant.Constant.Description)
      - [A Name ](#tts.core.api.internalApi.Constant.Constant.Name)
      - [A Value ](#tts.core.api.internalApi.Constant.Constant.Value)
  - [ Constants ](#constants)
    - [C Constants ](#tts.core.api.internalApi.Constants.Constants)
      - [A Count ](#tts.core.api.internalApi.Constants.Constants.Count)
      - [M Item ](#tts.core.api.internalApi.Constants.Constants.Item)
  - [ Ecu ](#ecu)
    - [C Ecu ](#tts.core.api.internalApi.Ecu.Ecu)
      - [A A2l ](#tts.core.api.internalApi.Ecu.Ecu.A2l)
      - [A DebugHex ](#tts.core.api.internalApi.Ecu.Ecu.DebugHex)
      - [A Elf ](#tts.core.api.internalApi.Ecu.Ecu.Elf)
      - [A Elfs ](#tts.core.api.internalApi.Ecu.Ecu.Elfs)
      - [A Hex ](#tts.core.api.internalApi.Ecu.Ecu.Hex)
      - [A Name ](#tts.core.api.internalApi.Ecu.Ecu.Name)
      - [A Sgbd ](#tts.core.api.internalApi.Ecu.Ecu.Sgbd)
  - [ Ecus ](#ecus)
    - [C Ecus ](#tts.core.api.internalApi.Ecus.Ecus)
      - [A Count ](#tts.core.api.internalApi.Ecus.Ecus.Count)
      - [M Item ](#tts.core.api.internalApi.Ecus.Ecus.Item)
  - [ EnvironmentCommunication ](#environmentcommunication)
    - [C EnvironmentCommunication ](#tts.testModule.envCom.internalApi.EnvironmentCommunication.EnvironmentCommunication)
      - [A Name ](#tts.testModule.envCom.internalApi.EnvironmentCommunication.EnvironmentCommunication.Name)
  - [ EnvironmentCommunications ](#environmentcommunications)
    - [C EnvironmentCommunications ](#tts.testModule.envCom.internalApi.EnvironmentCommunications.EnvironmentCommunications)
      - [A Count ](#tts.testModule.envCom.internalApi.EnvironmentCommunications.EnvironmentCommunications.Count)
      - [M Item ](#tts.testModule.envCom.internalApi.EnvironmentCommunications.EnvironmentCommunications.Item)
  - [ EnvironmentSimulation ](#environmentsimulation)
    - [C EnvironmentSimulation ](#tts.testModule.envSim.internalApi.EnvironmentSimulation.EnvironmentSimulation)
      - [A Name ](#tts.testModule.envSim.internalApi.EnvironmentSimulation.EnvironmentSimulation.Name)
      - [A OfflineFile ](#tts.testModule.envSim.internalApi.EnvironmentSimulation.EnvironmentSimulation.OfflineFile)
  - [ EnvironmentSimulations ](#environmentsimulations)
    - [C EnvironmentSimulations ](#tts.testModule.envSim.internalApi.EnvironmentSimulations.EnvironmentSimulations)
      - [A Count ](#tts.testModule.envSim.internalApi.EnvironmentSimulations.EnvironmentSimulations.Count)
      - [M Item ](#tts.testModule.envSim.internalApi.EnvironmentSimulations.EnvironmentSimulations.Item)
  - [ GlobalConstants ](#globalconstants)
    - [C GlobalConstants ](#tts.core.api.internalApi.GlobalConstants.GlobalConstants)
      - [M GetConstant ](#tts.core.api.internalApi.GlobalConstants.GlobalConstants.GetConstant)
      - [M GetConstants ](#tts.core.api.internalApi.GlobalConstants.GlobalConstants.GetConstants)
    - [V ORIGIN_DEFINED_AT_RUNTIME ](#tts.core.api.internalApi.GlobalConstants.ORIGIN_DEFINED_AT_RUNTIME)
    - [V ORIGIN_MANIPULATED_AT_RUNTIME ](#tts.core.api.internalApi.GlobalConstants.ORIGIN_MANIPULATED_AT_RUNTIME)
  - [ KeywordCatalog ](#keywordcatalog)
    - [C KeywordCatalogApi ](#tts.core.api.internalApi.KeywordCatalogApi.KeywordCatalogApi)
      - [M Connect ](#tts.core.api.internalApi.KeywordCatalogApi.KeywordCatalogApi.Connect)
      - [M GetAvailableCatalogs ](#tts.core.api.internalApi.KeywordCatalogApi.KeywordCatalogApi.GetAvailableCatalogs)
      - [M GetAvailableProjects ](#tts.core.api.internalApi.KeywordCatalogApi.KeywordCatalogApi.GetAvailableProjects)
      - [M GetAvailableVariants ](#tts.core.api.internalApi.KeywordCatalogApi.KeywordCatalogApi.GetAvailableVariants)
      - [M GetCurrentCatalogName ](#tts.core.api.internalApi.KeywordCatalogApi.KeywordCatalogApi.GetCurrentCatalogName)
      - [M GetCurrentProject ](#tts.core.api.internalApi.KeywordCatalogApi.KeywordCatalogApi.GetCurrentProject)
      - [M GetCurrentVariant ](#tts.core.api.internalApi.KeywordCatalogApi.KeywordCatalogApi.GetCurrentVariant)
      - [M IsConnected ](#tts.core.api.internalApi.KeywordCatalogApi.KeywordCatalogApi.IsConnected)
      - [M LoadCatalog ](#tts.core.api.internalApi.KeywordCatalogApi.KeywordCatalogApi.LoadCatalog)
      - [M SetProject ](#tts.core.api.internalApi.KeywordCatalogApi.KeywordCatalogApi.SetProject)
      - [M SetVariant ](#tts.core.api.internalApi.KeywordCatalogApi.KeywordCatalogApi.SetVariant)
  - [ Math ](#id16)
  - [ Model ](#model)
    - [C Model ](#tts.core.api.internalApi.Model.Model)
      - [A Name ](#tts.core.api.internalApi.Model.Model.Name)
  - [ Models ](#models)
    - [C Models ](#tts.core.api.internalApi.Models.Models)
      - [A Count ](#tts.core.api.internalApi.Models.Models.Count)
      - [M Item ](#tts.core.api.internalApi.Models.Models.Item)
  - [ Multimedia ](#multimedia)
    - [C ImageFiltersApi ](#tts.testModule.multimedia.api.MultimediaApi.ImageFiltersApi)
    - [C MultimediaApi ](#tts.testModule.multimedia.api.MultimediaApi.MultimediaApi)
      - [A ImageFilters ](#tts.testModule.multimedia.api.MultimediaApi.MultimediaApi.ImageFilters)
      - [M GetAvailableOCRServices ](#tts.testModule.multimedia.api.MultimediaApi.MultimediaApi.GetAvailableOCRServices)
      - [M GetAvailableObjectDetectors ](#tts.testModule.multimedia.api.MultimediaApi.MultimediaApi.GetAvailableObjectDetectors)
      - [M GetAvailableSTTProfiles ](#tts.testModule.multimedia.api.MultimediaApi.MultimediaApi.GetAvailableSTTProfiles)
      - [M GetAvailableTTSVoices ](#tts.testModule.multimedia.api.MultimediaApi.MultimediaApi.GetAvailableTTSVoices)
      - [M GetDefaultOCRService ](#tts.testModule.multimedia.api.MultimediaApi.MultimediaApi.GetDefaultOCRService)
      - [M GetOCRService ](#tts.testModule.multimedia.api.MultimediaApi.MultimediaApi.GetOCRService)
      - [M GetObjectDetector ](#tts.testModule.multimedia.api.MultimediaApi.MultimediaApi.GetObjectDetector)
      - [M SpeechToText ](#tts.testModule.multimedia.api.MultimediaApi.MultimediaApi.SpeechToText)
      - [M TextToSpeech ](#tts.testModule.multimedia.api.MultimediaApi.MultimediaApi.TextToSpeech)
  - [ Scm ](#scm)
    - [C Scm ](#tts.core.api.internalApi.Scm.Scm)
      - [M GetCheckoutRevision ](#tts.core.api.internalApi.Scm.Scm.GetCheckoutRevision)
      - [M GetFileRevision ](#tts.core.api.internalApi.Scm.Scm.GetFileRevision)
      - [M GetFileStatus ](#tts.core.api.internalApi.Scm.Scm.GetFileStatus)
      - [M GetUrl ](#tts.core.api.internalApi.Scm.Scm.GetUrl)
  - [ Service ](#service)
    - [C Service ](#tts.core.api.internalApi.Service.Service)
      - [M GetUsedServices ](#tts.core.api.internalApi.Service.Service.GetUsedServices)
      - [M GenerateService ](#tts.core.api.internalApi.Service.Service.GenerateService)
      - [M GetPort ](#tts.core.api.internalApi.Service.Service.GetPort)
    - [C ServicePort ](#tts.core.api.internalApi.Service.ServicePort)
      - [M GetService ](#tts.core.api.internalApi.Service.ServicePort.GetService)
      - [M StartService ](#tts.core.api.internalApi.Service.ServicePort.StartService)
      - [M StopService ](#tts.core.api.internalApi.Service.ServicePort.StopService)
    - [C ServiceProxy ](#tts.core.api.internalApi.Service.ServiceProxy)
      - [M GetFunctionsHelp ](#tts.core.api.internalApi.Service.ServiceProxy.GetFunctionsHelp)
      - [M GetServiceFunctions ](#tts.core.api.internalApi.Service.ServiceProxy.GetServiceFunctions)
  - [ TestBench ](#testbench)
    - [C TestBench ](#tts.core.api.internalApi.TestBench.TestBench)
      - [M GetPortStatus ](#tts.core.api.internalApi.TestBench.TestBench.GetPortStatus)
      - [M GetToolStatus ](#tts.core.api.internalApi.TestBench.TestBench.GetToolStatus)
      - [M StartTool ](#tts.core.api.internalApi.TestBench.TestBench.StartTool)
      - [M StopTool ](#tts.core.api.internalApi.TestBench.TestBench.StopTool)
  - [ TestbenchConfiguration ](#testbenchconfiguration)
    - [C TestbenchConfiguration ](#tts.core.api.internalApi.TestbenchConfiguration.TestbenchConfiguration)
      - [A Filename ](#tts.core.api.internalApi.TestbenchConfiguration.TestbenchConfiguration.Filename)
      - [A ToolList ](#tts.core.api.internalApi.TestbenchConfiguration.TestbenchConfiguration.ToolList)
      - [M GetToolhostInfo ](#tts.core.api.internalApi.TestbenchConfiguration.TestbenchConfiguration.GetToolhostInfo)
  - [ TestbenchTool ](#testbenchtool)
    - [C TestbenchTool ](#tts.core.api.internalApi.TestbenchTool.TestbenchTool)
      - [A Jobs ](#tts.core.api.internalApi.TestbenchTool.TestbenchTool.Jobs)
      - [A Location ](#tts.core.api.internalApi.TestbenchTool.TestbenchTool.Location)
      - [A Name ](#tts.core.api.internalApi.TestbenchTool.TestbenchTool.Name)
      - [A PortList ](#tts.core.api.internalApi.TestbenchTool.TestbenchTool.PortList)
      - [A Ports ](#tts.core.api.internalApi.TestbenchTool.TestbenchTool.Ports)
      - [A ToolId ](#tts.core.api.internalApi.TestbenchTool.TestbenchTool.ToolId)
      - [A Version ](#tts.core.api.internalApi.TestbenchTool.TestbenchTool.Version)
  - [ TestConfiguration ](#id25)
    - [C TestConfiguration ](#tts.core.api.internalApi.TestConfiguration.TestConfiguration)
      - [A BusSystems ](#tts.core.api.internalApi.TestConfiguration.TestConfiguration.BusSystems)
      - [A Ecus ](#tts.core.api.internalApi.TestConfiguration.TestConfiguration.Ecus)
      - [A EnvironmentCommunications ](#tts.core.api.internalApi.TestConfiguration.TestConfiguration.EnvironmentCommunications)
      - [A EnvironmentSimulations ](#tts.core.api.internalApi.TestConfiguration.TestConfiguration.EnvironmentSimulations)
      - [A Filename ](#tts.core.api.internalApi.TestConfiguration.TestConfiguration.Filename)
      - [A GlobalConstants ](#tts.core.api.internalApi.TestConfiguration.TestConfiguration.GlobalConstants)
      - [A Models ](#tts.core.api.internalApi.TestConfiguration.TestConfiguration.Models)
      - [A NameTester ](#tts.core.api.internalApi.TestConfiguration.TestConfiguration.NameTester)
      - [M ReloadGlobalMapping ](#tts.core.api.internalApi.TestConfiguration.TestConfiguration.ReloadGlobalMapping)
  - [ TestEnvironment ](#testenvironment)
    - [C TestEnvironment ](#tts.core.api.internalApi.TestEnvironment.TestEnvironment)
      - [A ExecutionInfo ](#tts.core.api.internalApi.TestEnvironment.TestEnvironment.ExecutionInfo)
      - [M GenerateTestReportDocumentFromDB ](#tts.core.api.internalApi.TestEnvironment.TestEnvironment.GenerateTestReportDocumentFromDB)
      - [M GetPackageReferences ](#tts.core.api.internalApi.TestEnvironment.TestEnvironment.GetPackageReferences)
      - [M TimeElapsing ](#tts.core.api.internalApi.TestEnvironment.TestEnvironment.TimeElapsing)
      - [M Wait ](#tts.core.api.internalApi.TestEnvironment.TestEnvironment.Wait)
  - [ TestExecutionInfo ](#testexecutioninfo)
    - [C ExecutionExceptionInfo ](#tts.core.api.internalApi.TestExecutionInfo.ExecutionExceptionInfo)
      - [M GetMessage ](#tts.core.api.internalApi.TestExecutionInfo.ExecutionExceptionInfo.GetMessage)
      - [M GetTestStepPortId ](#tts.core.api.internalApi.TestExecutionInfo.ExecutionExceptionInfo.GetTestStepPortId)
      - [M GetTestStepToolId ](#tts.core.api.internalApi.TestExecutionInfo.ExecutionExceptionInfo.GetTestStepToolId)
      - [M GetTestStepType ](#tts.core.api.internalApi.TestExecutionInfo.ExecutionExceptionInfo.GetTestStepType)
      - [M GetType ](#tts.core.api.internalApi.TestExecutionInfo.ExecutionExceptionInfo.GetType)
    - [C KeywordInfo ](#tts.core.api.internalApi.TestExecutionInfo.KeywordInfo)
      - [M GetArgumentUnit ](#tts.core.api.internalApi.TestExecutionInfo.KeywordInfo.GetArgumentUnit)
      - [M GetArguments ](#tts.core.api.internalApi.TestExecutionInfo.KeywordInfo.GetArguments)
      - [M GetComponentType ](#tts.core.api.internalApi.TestExecutionInfo.KeywordInfo.GetComponentType)
      - [M GetCurrentTimeOptionIteration ](#tts.core.api.internalApi.TestExecutionInfo.KeywordInfo.GetCurrentTimeOptionIteration)
      - [M GetId ](#tts.core.api.internalApi.TestExecutionInfo.KeywordInfo.GetId)
      - [M GetReturnUnit ](#tts.core.api.internalApi.TestExecutionInfo.KeywordInfo.GetReturnUnit)
      - [M GetReturns ](#tts.core.api.internalApi.TestExecutionInfo.KeywordInfo.GetReturns)
      - [M GetTimeOptionDuration ](#tts.core.api.internalApi.TestExecutionInfo.KeywordInfo.GetTimeOptionDuration)
      - [M GetTimeOptionMode ](#tts.core.api.internalApi.TestExecutionInfo.KeywordInfo.GetTimeOptionMode)
      - [M GetTimeOptionPollingCycle ](#tts.core.api.internalApi.TestExecutionInfo.KeywordInfo.GetTimeOptionPollingCycle)
      - [M GetTimeOptionTimeout ](#tts.core.api.internalApi.TestExecutionInfo.KeywordInfo.GetTimeOptionTimeout)
      - [M IsControlTestStep ](#tts.core.api.internalApi.TestExecutionInfo.KeywordInfo.IsControlTestStep)
      - [M IsEstablishTestStep ](#tts.core.api.internalApi.TestExecutionInfo.KeywordInfo.IsEstablishTestStep)
      - [M IsStateTestStep ](#tts.core.api.internalApi.TestExecutionInfo.KeywordInfo.IsStateTestStep)
    - [C TestExecutionInfo ](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo)
      - [A AllProjectsStepCount ](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.AllProjectsStepCount)
      - [A AllProjectsStepsExecuted ](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.AllProjectsStepsExecuted)
      - [A CurrentLineNumber ](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.CurrentLineNumber)
      - [A CurrentTestStepHierarchy ](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.CurrentTestStepHierarchy)
      - [A KeywordInfo ](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.KeywordInfo)
      - [A LastTestStepResult ](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.LastTestStepResult)
      - [A LogFolder ](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.LogFolder)
      - [A MainProjectStepCount ](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.MainProjectStepCount)
      - [A MainProjectStepsExecuted ](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.MainProjectStepsExecuted)
      - [A PackageResult ](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.PackageResult)
      - [A ProjectResult ](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.ProjectResult)
      - [A ProjectStartTime ](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.ProjectStartTime)
      - [A ReportDb ](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.ReportDb)
      - [A ReportDbFolder ](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.ReportDbFolder)
      - [A RunningTime ](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.RunningTime)
      - [A StartTime ](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.StartTime)
      - [A TargetReportDbFolder ](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.TargetReportDbFolder)
      - [M AddArtifact ](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.AddArtifact)
      - [M AddTestStepReportDetail ](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.AddTestStepReportDetail)
      - [M GetCurrentPackageFilename ](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.GetCurrentPackageFilename)
      - [M GetCurrentPackagePath ](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.GetCurrentPackagePath)
      - [M GetCurrentProjectFilename ](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.GetCurrentProjectFilename)
      - [M GetCurrentProjectPath ](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.GetCurrentProjectPath)
      - [M GetExecutionExceptionInfo ](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.GetExecutionExceptionInfo)
      - [M GetExecutionMode ](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.GetExecutionMode)
      - [M GetKeywordInfo ](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.GetKeywordInfo)
      - [M GetMainPackageFilename ](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.GetMainPackageFilename)
      - [M GetMainPackagePath ](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.GetMainPackagePath)
      - [M GetMappingNames ](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.GetMappingNames)
      - [M GetMappingTargetPath ](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.GetMappingTargetPath)
      - [M GetWatchTime ](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.GetWatchTime)
      - [M IsAbortRequested ](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.IsAbortRequested)
      - [M IsAborted ](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.IsAborted)
      - [M IsInMain ](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.IsInMain)
      - [M IsInPostcondition ](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.IsInPostcondition)
      - [M IsInPrecondition ](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.IsInPrecondition)
      - [M IsInteractiveExecution ](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.IsInteractiveExecution)
      - [M StartWatch ](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.StartWatch)
  - [ TestManagement ](#module-tts.core.api.internalApi.TestManagement)
    - [C TestManagementApi ](#tts.core.api.internalApi.TestManagement.TestManagementApi)
      - [M GetTestScriptByID ](#tts.core.api.internalApi.TestManagement.TestManagementApi.GetTestScriptByID)
  - [ ToolAccess ](#toolaccess)
    - [C JobExecutor ](#tts.core.api.internalApi.ToolAccess.JobExecutor)
      - [M Execute ](#tts.core.api.internalApi.ToolAccess.JobExecutor.Execute)
    - [C ToolAccess ](#tts.core.api.internalApi.ToolAccess.ToolAccess)
      - [M GetPortJobExecutor ](#tts.core.api.internalApi.ToolAccess.ToolAccess.GetPortJobExecutor)
      - [M GetToolJobExecutor ](#tts.core.api.internalApi.ToolAccess.ToolAccess.GetToolJobExecutor)
  - [ Workspace ](#workspace)
    - [C Finding ](#tts.core.api.internalApi.Workspace.Finding)
    - [C Workspace ](#tts.core.api.internalApi.Workspace.Workspace)
      - [M Check ](#tts.core.api.internalApi.Workspace.Workspace.Check)
- [ Credentials API ](#credentials-api)
  - [ Introduction ](#module-tts.core.api.internalApi.credentialsApi.Credentials)
    - [ Keystores ](#keystores)
    - [ Managing Keystores ](#managing-keystores)
    - [ Accessing Keystores ](#accessing-keystores)
    - [ Secrets ](#secrets)
    - [ Managing the Vault ](#managing-the-vault)
    - [ Security ](#security)
    - [ Examples ](#examples)
  - [ Credentials ](#credentials)
    - [C Credentials ](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials)
      - [A Certificate ](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials.Certificate)
      - [M ChangeLoginCredentials ](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials.ChangeLoginCredentials)
      - [M Close ](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials.Close)
      - [M CreateCryptFileVault ](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials.CreateCryptFileVault)
      - [M CreatePkcs12KeyStore ](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials.CreatePkcs12KeyStore)
      - [M CreateSecret ](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials.CreateSecret)
      - [M DeleteVaultEntry ](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials.DeleteVaultEntry)
      - [M GetAvailableVaultEntries ](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials.GetAvailableVaultEntries)
      - [M GetTesterKey ](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials.GetTesterKey)
      - [M GetVaultEntry ](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials.GetVaultEntry)
      - [M LoadPkcs12KeyStore ](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials.LoadPkcs12KeyStore)
      - [M OpenCryptFileVault ](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials.OpenCryptFileVault)
      - [M OpenVault ](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials.OpenVault)
      - [A PrivateKey ](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials.PrivateKey)
      - [A PublicKey ](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials.PublicKey)
      - [M Save ](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials.Save)
      - [A SeedAndKey ](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials.SeedAndKey)
  - [ KeyStore ](#keystore)
    - [C KeyStore ](#tts.core.api.internalApi.credentialsApi.KeyStore.KeyStore)
      - [M Delete ](#tts.core.api.internalApi.credentialsApi.KeyStore.KeyStore.Delete)
      - [M GetCertificate ](#tts.core.api.internalApi.credentialsApi.KeyStore.KeyStore.GetCertificate)
      - [M GetCertificateChain ](#tts.core.api.internalApi.credentialsApi.KeyStore.KeyStore.GetCertificateChain)
      - [M GetCertificates ](#tts.core.api.internalApi.credentialsApi.KeyStore.KeyStore.GetCertificates)
      - [M GetPrivateKey ](#tts.core.api.internalApi.credentialsApi.KeyStore.KeyStore.GetPrivateKey)
  - [ Secret ](#secret)
    - [C Secret ](#tts.core.api.internalApi.credentialsApi.Secret.Secret)
      - [M AssociatedData ](#tts.core.api.internalApi.credentialsApi.Secret.Secret.AssociatedData)
      - [M Delete ](#tts.core.api.internalApi.credentialsApi.Secret.Secret.Delete)
      - [M Reveal ](#tts.core.api.internalApi.credentialsApi.Secret.Secret.Reveal)
  - [ Certificate ](#certificate)
    - [C Certificate ](#tts.core.api.internalApi.credentialsApi.Certificate.Certificate)
      - [M Base64 ](#tts.core.api.internalApi.credentialsApi.Certificate.Certificate.Base64)
      - [M CommonName ](#tts.core.api.internalApi.credentialsApi.Certificate.Certificate.CommonName)
      - [M DER ](#tts.core.api.internalApi.credentialsApi.Certificate.Certificate.DER)
      - [M FromBase64 ](#tts.core.api.internalApi.credentialsApi.Certificate.Certificate.FromBase64)
      - [M FromDER ](#tts.core.api.internalApi.credentialsApi.Certificate.Certificate.FromDER)
      - [M FromFile ](#tts.core.api.internalApi.credentialsApi.Certificate.Certificate.FromFile)
      - [M FromPEM ](#tts.core.api.internalApi.credentialsApi.Certificate.Certificate.FromPEM)
      - [M IsValid ](#tts.core.api.internalApi.credentialsApi.Certificate.Certificate.IsValid)
      - [M Issuer ](#tts.core.api.internalApi.credentialsApi.Certificate.Certificate.Issuer)
      - [M PEM ](#tts.core.api.internalApi.credentialsApi.Certificate.Certificate.PEM)
      - [M PublicKey ](#tts.core.api.internalApi.credentialsApi.Certificate.Certificate.PublicKey)
      - [M Subject ](#tts.core.api.internalApi.credentialsApi.Certificate.Certificate.Subject)
      - [M Verify ](#tts.core.api.internalApi.credentialsApi.Certificate.Certificate.Verify)
  - [ PrivateKey ](#privatekey)
    - [C PrivateKey ](#tts.core.api.internalApi.credentialsApi.PrivateKey.PrivateKey)
      - [M FromBase64 ](#tts.core.api.internalApi.credentialsApi.PrivateKey.PrivateKey.FromBase64)
      - [M FromDER ](#tts.core.api.internalApi.credentialsApi.PrivateKey.PrivateKey.FromDER)
      - [M FromFile ](#tts.core.api.internalApi.credentialsApi.PrivateKey.PrivateKey.FromFile)
      - [M FromPEM ](#tts.core.api.internalApi.credentialsApi.PrivateKey.PrivateKey.FromPEM)
      - [M PublicKey ](#tts.core.api.internalApi.credentialsApi.PrivateKey.PrivateKey.PublicKey)
      - [M Sign ](#tts.core.api.internalApi.credentialsApi.PrivateKey.PrivateKey.Sign)
  - [ PublicKey ](#publickey)
    - [C PublicKey ](#tts.core.api.internalApi.credentialsApi.PublicKey.PublicKey)
      - [M Base64 ](#tts.core.api.internalApi.credentialsApi.PublicKey.PublicKey.Base64)
      - [M DER ](#tts.core.api.internalApi.credentialsApi.PublicKey.PublicKey.DER)
      - [M FromBase64 ](#tts.core.api.internalApi.credentialsApi.PublicKey.PublicKey.FromBase64)
      - [M FromDER ](#tts.core.api.internalApi.credentialsApi.PublicKey.PublicKey.FromDER)
      - [M FromFile ](#tts.core.api.internalApi.credentialsApi.PublicKey.PublicKey.FromFile)
      - [M FromPEM ](#tts.core.api.internalApi.credentialsApi.PublicKey.PublicKey.FromPEM)
      - [M PEM ](#tts.core.api.internalApi.credentialsApi.PublicKey.PublicKey.PEM)
      - [M Verify ](#tts.core.api.internalApi.credentialsApi.PublicKey.PublicKey.Verify)
  - [ SeedAndKey ](#seedandkey)
    - [C SeedAndKey ](#tts.core.api.internalApi.credentialsApi.SeedAndKey.SeedAndKey)
      - [A Diag ](#tts.core.api.internalApi.credentialsApi.SeedAndKey.SeedAndKey.Diag)
      - [A Xcp ](#tts.core.api.internalApi.credentialsApi.SeedAndKey.SeedAndKey.Xcp)
  - [ DiagSeedAndKey ](#diagseedandkey)
    - [C DiagSeedAndKey ](#tts.core.api.internalApi.credentialsApi.SeedAndKey.DiagSeedAndKey)
      - [M FromLib ](#tts.core.api.internalApi.credentialsApi.SeedAndKey.DiagSeedAndKey.FromLib)
      - [M GenerateKeyEx ](#tts.core.api.internalApi.credentialsApi.SeedAndKey.DiagSeedAndKey.GenerateKeyEx)
      - [M GenerateKeyExOpt ](#tts.core.api.internalApi.credentialsApi.SeedAndKey.DiagSeedAndKey.GenerateKeyExOpt)
  - [ XcpSeedAndKey ](#xcpseedandkey)
    - [C XcpSeedAndKey ](#tts.core.api.internalApi.credentialsApi.SeedAndKey.XcpSeedAndKey)
      - [M ComputeKeyFromSeed ](#tts.core.api.internalApi.credentialsApi.SeedAndKey.XcpSeedAndKey.ComputeKeyFromSeed)
      - [M FromLib ](#tts.core.api.internalApi.credentialsApi.SeedAndKey.XcpSeedAndKey.FromLib)
      - [M GetAvailablePrivileges ](#tts.core.api.internalApi.credentialsApi.SeedAndKey.XcpSeedAndKey.GetAvailablePrivileges)
- [ DataBrowser ](#module-tts.core.api.dataBrowserApi.DataBrowser)
  - [ A2lBrowser ](#a2lbrowser)
    - [C A2lBrowser ](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser)
      - [M CalcPhysToRaw ](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.CalcPhysToRaw)
      - [M CalcRawToPhys ](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.CalcRawToPhys)
      - [M GetA2lEntity ](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.GetA2lEntity)
      - [M GetAcquisitionRateNames ](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.GetAcquisitionRateNames)
      - [M GetCodeCheckInformation ](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.GetCodeCheckInformation)
      - [M GetEpkInformation ](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.GetEpkInformation)
      - [M GetFunctionCharacteristics ](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.GetFunctionCharacteristics)
      - [M GetFunctionInMeasurements ](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.GetFunctionInMeasurements)
      - [M GetFunctionLocMeasurements ](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.GetFunctionLocMeasurements)
      - [M GetFunctionNames ](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.GetFunctionNames)
      - [M GetFunctionOutMeasurements ](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.GetFunctionOutMeasurements)
      - [M GetFunctionVersion ](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.GetFunctionVersion)
      - [M GetLabelNameList ](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.GetLabelNameList)
      - [M GetSubFunctionNames ](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.GetSubFunctionNames)
      - [M GetSystemConstantNameList ](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.GetSystemConstantNameList)
      - [M GetSystemConstantValue ](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.GetSystemConstantValue)
      - [M HasFunction ](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.HasFunction)
      - [M HasSubFunctions ](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.HasSubFunctions)
      - [M IsCharacteristic ](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.IsCharacteristic)
      - [M IsMeasurement ](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.IsMeasurement)
      - [M ReadDataFromHex ](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.ReadDataFromHex)
  - [ A2lEntity ](#a2lentity)
    - [C A2lEntity ](#tts.core.api.dataBrowserApi.DataBrowser.A2lEntity)
      - [M GetAddress ](#tts.core.api.dataBrowserApi.DataBrowser.A2lEntity.GetAddress)
      - [M GetByteOrder ](#tts.core.api.dataBrowserApi.DataBrowser.A2lEntity.GetByteOrder)
      - [M GetCoeffsDict ](#tts.core.api.dataBrowserApi.DataBrowser.A2lEntity.GetCoeffsDict)
      - [M GetCompuMethodName ](#tts.core.api.dataBrowserApi.DataBrowser.A2lEntity.GetCompuMethodName)
      - [M GetDataType ](#tts.core.api.dataBrowserApi.DataBrowser.A2lEntity.GetDataType)
      - [M GetDescription ](#tts.core.api.dataBrowserApi.DataBrowser.A2lEntity.GetDescription)
      - [M GetDisplayIdentifier ](#tts.core.api.dataBrowserApi.DataBrowser.A2lEntity.GetDisplayIdentifier)
      - [M GetLowerLimit ](#tts.core.api.dataBrowserApi.DataBrowser.A2lEntity.GetLowerLimit)
      - [M GetMatrixDim ](#tts.core.api.dataBrowserApi.DataBrowser.A2lEntity.GetMatrixDim)
      - [M GetName ](#tts.core.api.dataBrowserApi.DataBrowser.A2lEntity.GetName)
      - [M GetSize ](#tts.core.api.dataBrowserApi.DataBrowser.A2lEntity.GetSize)
      - [M GetUnit ](#tts.core.api.dataBrowserApi.DataBrowser.A2lEntity.GetUnit)
      - [M GetUpperLimit ](#tts.core.api.dataBrowserApi.DataBrowser.A2lEntity.GetUpperLimit)
      - [M GetValueType ](#tts.core.api.dataBrowserApi.DataBrowser.A2lEntity.GetValueType)
      - [M GetVtabDict ](#tts.core.api.dataBrowserApi.DataBrowser.A2lEntity.GetVtabDict)
  - [ BusBrowser ](#busbrowser)
    - [C BusBrowser ](#tts.core.api.dataBrowserApi.DataBrowser.BusBrowser)
      - [M GetFrameNamesByPDUName ](#tts.core.api.dataBrowserApi.DataBrowser.BusBrowser.GetFrameNamesByPDUName)
      - [M GetLinScheduleTables ](#tts.core.api.dataBrowserApi.DataBrowser.BusBrowser.GetLinScheduleTables)
      - [M GetSDGsAndSDs ](#tts.core.api.dataBrowserApi.DataBrowser.BusBrowser.GetSDGsAndSDs)
      - [M ListFrames ](#tts.core.api.dataBrowserApi.DataBrowser.BusBrowser.ListFrames)
      - [M ListPDUs ](#tts.core.api.dataBrowserApi.DataBrowser.BusBrowser.ListPDUs)
      - [M ListSignals ](#tts.core.api.dataBrowserApi.DataBrowser.BusBrowser.ListSignals)
      - [M ListSignalsByPDU ](#tts.core.api.dataBrowserApi.DataBrowser.BusBrowser.ListSignalsByPDU)
  - [ BusEntity ](#busentity)
    - [C BusEntity ](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity)
      - [M GetActivations ](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetActivations)
      - [M GetByteOrder ](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetByteOrder)
      - [M GetCycleRepetition ](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetCycleRepetition)
      - [M GetDebounceTime ](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetDebounceTime)
      - [M GetDescription ](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetDescription)
      - [M GetE2EProfile ](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetE2EProfile)
      - [M GetFrameLength ](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetFrameLength)
      - [M GetFrameType ](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetFrameType)
      - [M GetId ](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetId)
      - [M GetLinearCoeffs ](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetLinearCoeffs)
      - [M GetLongName ](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetLongName)
      - [M GetMaxRawValue ](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetMaxRawValue)
      - [M GetMaxValue ](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetMaxValue)
      - [M GetMinRawValue ](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetMinRawValue)
      - [M GetMinValue ](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetMinValue)
      - [M GetMultiplexerSwitchCode ](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetMultiplexerSwitchCode)
      - [M GetName ](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetName)
      - [M GetOriginalName ](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetOriginalName)
      - [M GetPDULength ](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetPDULength)
      - [M GetPDUPosition ](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetPDUPosition)
      - [M GetPDUUpdateBit ](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetPDUUpdateBit)
      - [M GetPath ](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetPath)
      - [M GetPhysValue ](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetPhysValue)
      - [M GetRawValue ](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetRawValue)
      - [M GetRxEcuNames ](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetRxEcuNames)
      - [M GetSecOcDataId ](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetSecOcDataId)
      - [M GetSignalDataPositionInFrame ](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetSignalDataPositionInFrame)
      - [M GetSignalDataPositionInPDU ](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetSignalDataPositionInPDU)
      - [M GetSignalLength ](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetSignalLength)
      - [M GetStartCycle ](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetStartCycle)
      - [M GetSystemSignalName ](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetSystemSignalName)
      - [M GetTextTable ](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetTextTable)
      - [M GetTimeOffset ](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetTimeOffset)
      - [M GetTimings ](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetTimings)
      - [M GetTxEcuNames ](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetTxEcuNames)
      - [M GetUnit ](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetUnit)
      - [M IsFrame ](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.IsFrame)
      - [M IsMultiplexer ](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.IsMultiplexer)
      - [M IsNode ](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.IsNode)
      - [M IsPDU ](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.IsPDU)
      - [M IsSend ](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.IsSend)
      - [M IsSignal ](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.IsSignal)
  - [ DataBrowser ](#id31)
    - [C DataBrowser ](#tts.core.api.dataBrowserApi.DataBrowser.DataBrowser)
      - [M BrowseA2l ](#tts.core.api.dataBrowserApi.DataBrowser.DataBrowser.BrowseA2l)
      - [M BrowseBus ](#tts.core.api.dataBrowserApi.DataBrowser.DataBrowser.BrowseBus)
      - [M BrowseDebug ](#tts.core.api.dataBrowserApi.DataBrowser.DataBrowser.BrowseDebug)
      - [M BrowseDebugElf ](#tts.core.api.dataBrowserApi.DataBrowser.DataBrowser.BrowseDebugElf)
      - [M BrowseDiag ](#tts.core.api.dataBrowserApi.DataBrowser.DataBrowser.BrowseDiag)
      - [M BrowseLogging ](#tts.core.api.dataBrowserApi.DataBrowser.DataBrowser.BrowseLogging)
      - [M BrowseModel ](#tts.core.api.dataBrowserApi.DataBrowser.DataBrowser.BrowseModel)
      - [M BrowseMultimedia ](#tts.core.api.dataBrowserApi.DataBrowser.DataBrowser.BrowseMultimedia)
      - [M BrowseService ](#tts.core.api.dataBrowserApi.DataBrowser.DataBrowser.BrowseService)
      - [M BrowseSgbd ](#tts.core.api.dataBrowserApi.DataBrowser.DataBrowser.BrowseSgbd)
  - [ DebugBrowser ](#debugbrowser)
    - [C DebugBrowser ](#tts.core.api.dataBrowserApi.DataBrowser.DebugBrowser)
      - [M GetCores ](#tts.core.api.dataBrowserApi.DataBrowser.DebugBrowser.GetCores)
      - [M GetElfFiles ](#tts.core.api.dataBrowserApi.DataBrowser.DebugBrowser.GetElfFiles)
      - [M GetModules ](#tts.core.api.dataBrowserApi.DataBrowser.DebugBrowser.GetModules)
      - [M GetRegisters ](#tts.core.api.dataBrowserApi.DataBrowser.DebugBrowser.GetRegisters)
      - [M GetVariables ](#tts.core.api.dataBrowserApi.DataBrowser.DebugBrowser.GetVariables)
  - [ DiagBrowser ](#diagbrowser)
    - [C DiagBrowser ](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagBrowser)
      - [M GetDiagDtcs ](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagBrowser.GetDiagDtcs)
      - [M GetDiagServices ](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagBrowser.GetDiagServices)
      - [M GetDiagStateCharts ](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagBrowser.GetDiagStateCharts)
  - [ DiagDtcEntity ](#diagdtcentity)
    - [C DiagDtcEntity ](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagDtcEntity)
      - [M GetSdgs ](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagDtcEntity.GetSdgs)
      - [M GetShortName ](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagDtcEntity.GetShortName)
      - [M GetTroubleCode ](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagDtcEntity.GetTroubleCode)
  - [ DiagServiceEntity ](#diagserviceentity)
    - [C DiagServiceEntity ](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagServiceEntity)
      - [M GetLongName ](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagServiceEntity.GetLongName)
      - [M GetPreconditions ](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagServiceEntity.GetPreconditions)
      - [M GetSdgs ](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagServiceEntity.GetSdgs)
      - [M GetServiceId ](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagServiceEntity.GetServiceId)
      - [M GetServiceName ](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagServiceEntity.GetServiceName)
      - [M GetShortName ](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagServiceEntity.GetShortName)
      - [M GetTransitions ](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagServiceEntity.GetTransitions)
  - [ DiagStateChartEntity ](#diagstatechartentity)
    - [C DiagStateChartEntity ](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateChartEntity)
      - [M GetLongName ](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateChartEntity.GetLongName)
      - [M GetSemantic ](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateChartEntity.GetSemantic)
      - [M GetShortName ](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateChartEntity.GetShortName)
      - [M GetStartState ](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateChartEntity.GetStartState)
      - [M GetStateChartId ](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateChartEntity.GetStateChartId)
      - [M GetStates ](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateChartEntity.GetStates)
      - [M GetTransitions ](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateChartEntity.GetTransitions)
  - [ DiagStateEntity ](#diagstateentity)
    - [C DiagStateEntity ](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateEntity)
      - [M GetEndingTransitions ](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateEntity.GetEndingTransitions)
      - [M GetLongName ](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateEntity.GetLongName)
      - [M GetShortName ](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateEntity.GetShortName)
      - [M GetStartingTransitions ](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateEntity.GetStartingTransitions)
      - [M GetStateChart ](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateEntity.GetStateChart)
      - [M GetStateId ](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateEntity.GetStateId)
  - [ DiagStateTransitionEntity ](#diagstatetransitionentity)
    - [C DiagStateTransitionEntity ](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateTransitionEntity)
      - [M GetLongName ](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateTransitionEntity.GetLongName)
      - [M GetServices ](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateTransitionEntity.GetServices)
      - [M GetShortName ](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateTransitionEntity.GetShortName)
      - [M GetSourceState ](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateTransitionEntity.GetSourceState)
      - [M GetStateChart ](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateTransitionEntity.GetStateChart)
      - [M GetTargetState ](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateTransitionEntity.GetTargetState)
      - [M GetTransitionId ](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateTransitionEntity.GetTransitionId)
  - [ LoggingBrowser ](#loggingbrowser)
    - [C LoggingBrowser ](#tts.core.api.dataBrowserApi.DataBrowser.LoggingBrowser)
      - [M GetProtocol ](#tts.core.api.dataBrowserApi.DataBrowser.LoggingBrowser.GetProtocol)
      - [M ListArguments ](#tts.core.api.dataBrowserApi.DataBrowser.LoggingBrowser.ListArguments)
      - [M ListMessages ](#tts.core.api.dataBrowserApi.DataBrowser.LoggingBrowser.ListMessages)
  - [ LoggingEntity ](#loggingentity)
    - [C LoggingEntity ](#tts.core.api.dataBrowserApi.DataBrowser.LoggingEntity)
      - [M GetArgumentLength ](#tts.core.api.dataBrowserApi.DataBrowser.LoggingEntity.GetArgumentLength)
      - [M GetArgumentPositionInMessage ](#tts.core.api.dataBrowserApi.DataBrowser.LoggingEntity.GetArgumentPositionInMessage)
      - [M GetDescription ](#tts.core.api.dataBrowserApi.DataBrowser.LoggingEntity.GetDescription)
      - [M GetFilterDescription ](#tts.core.api.dataBrowserApi.DataBrowser.LoggingEntity.GetFilterDescription)
      - [M GetId ](#tts.core.api.dataBrowserApi.DataBrowser.LoggingEntity.GetId)
      - [M GetMessageLength ](#tts.core.api.dataBrowserApi.DataBrowser.LoggingEntity.GetMessageLength)
      - [M GetName ](#tts.core.api.dataBrowserApi.DataBrowser.LoggingEntity.GetName)
      - [M GetPath ](#tts.core.api.dataBrowserApi.DataBrowser.LoggingEntity.GetPath)
      - [M GetPhysValue ](#tts.core.api.dataBrowserApi.DataBrowser.LoggingEntity.GetPhysValue)
      - [M GetRawValue ](#tts.core.api.dataBrowserApi.DataBrowser.LoggingEntity.GetRawValue)
      - [M GetTxEcuNames ](#tts.core.api.dataBrowserApi.DataBrowser.LoggingEntity.GetTxEcuNames)
      - [M IsArgument ](#tts.core.api.dataBrowserApi.DataBrowser.LoggingEntity.IsArgument)
      - [M IsMessage ](#tts.core.api.dataBrowserApi.DataBrowser.LoggingEntity.IsMessage)
  - [ MediaBrowser ](#mediabrowser)
    - [C MediaBrowser ](#tts.testModule.multimedia.dataBrowser.MediaBrowser.MediaBrowser)
  - [ ModelBrowser ](#modelbrowser)
    - [C ModelBrowser ](#tts.core.api.dataBrowserApi.DataBrowser.ModelBrowser)
      - [M FindVariables ](#tts.core.api.dataBrowserApi.DataBrowser.ModelBrowser.FindVariables)
  - [ ServiceBrowser ](#servicebrowser)
    - [C ServiceBrowser ](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser)
      - [M GetE2EProfile ](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetE2EProfile)
      - [M GetEcuConsumerInfos ](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetEcuConsumerInfos)
      - [M GetEcuConsumerNamesByServiceName ](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetEcuConsumerNamesByServiceName)
      - [M GetEcuNamesByServiceName ](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetEcuNamesByServiceName)
      - [M GetEcus ](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetEcus)
      - [M GetEventGroupInfos ](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetEventGroupInfos)
      - [M GetEventInfos ](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetEventInfos)
      - [M GetFieldNamesByServiceName ](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetFieldNamesByServiceName)
      - [M GetInputParameterRepresentation ](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetInputParameterRepresentation)
      - [M GetInstanceID ](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetInstanceID)
      - [M GetMethodInfos ](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetMethodInfos)
      - [M GetOfferCyclicDelay ](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetOfferCyclicDelay)
      - [M GetReturnParameterRepresentation ](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetReturnParameterRepresentation)
      - [M GetSDGsAndSDs ](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetSDGsAndSDs)
      - [M GetServiceAdressInfos ](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetServiceAdressInfos)
      - [M GetServiceID ](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetServiceID)
      - [M GetServiceInfos ](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetServiceInfos)
      - [M GetTimings ](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetTimings)
      - [M GetVersion ](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetVersion)
      - [M GetVlanInfo ](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetVlanInfo)
  - [ SgbdBrowser ](#sgbdbrowser)
    - [C SgbdBrowser ](#tts.core.api.dataBrowserApi.DataBrowser.SgbdBrowser)
      - [M GetJob ](#tts.core.api.dataBrowserApi.DataBrowser.SgbdBrowser.GetJob)
      - [M GetListTableNames ](#tts.core.api.dataBrowserApi.DataBrowser.SgbdBrowser.GetListTableNames)
      - [M IsJob ](#tts.core.api.dataBrowserApi.DataBrowser.SgbdBrowser.IsJob)
      - [M ListJobs ](#tts.core.api.dataBrowserApi.DataBrowser.SgbdBrowser.ListJobs)
      - [M QueryTableByArgument ](#tts.core.api.dataBrowserApi.DataBrowser.SgbdBrowser.QueryTableByArgument)
      - [M QueryTableByName ](#tts.core.api.dataBrowserApi.DataBrowser.SgbdBrowser.QueryTableByName)
      - [M QueryTableByResult ](#tts.core.api.dataBrowserApi.DataBrowser.SgbdBrowser.QueryTableByResult)
  - [ SgbdEntity ](#sgbdentity)
    - [C SgbdEntity ](#tts.core.api.dataBrowserApi.DataBrowser.SgbdEntity)
      - [M GetArgumentType ](#tts.core.api.dataBrowserApi.DataBrowser.SgbdEntity.GetArgumentType)
      - [M GetArguments ](#tts.core.api.dataBrowserApi.DataBrowser.SgbdEntity.GetArguments)
      - [M GetDescription ](#tts.core.api.dataBrowserApi.DataBrowser.SgbdEntity.GetDescription)
      - [M GetName ](#tts.core.api.dataBrowserApi.DataBrowser.SgbdEntity.GetName)
      - [M GetResultType ](#tts.core.api.dataBrowserApi.DataBrowser.SgbdEntity.GetResultType)
      - [M GetResults ](#tts.core.api.dataBrowserApi.DataBrowser.SgbdEntity.GetResults)
- [ UnitInfo ](#unitinfo)
  - [ UnitInfo ](#module-tts.core.api.dataBrowserApi.UnitInfo)
    - [C UnitInfo ](#tts.core.api.dataBrowserApi.UnitInfo.UnitInfo)
      - [M Convert ](#tts.core.api.dataBrowserApi.UnitInfo.UnitInfo.Convert)
      - [M GetDimension ](#tts.core.api.dataBrowserApi.UnitInfo.UnitInfo.GetDimension)
      - [M HasUnit ](#tts.core.api.dataBrowserApi.UnitInfo.UnitInfo.HasUnit)

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
Object for the [`AnalysisEnvironment`](#tts.core.api.internalApi.AnalysisEnvironment.AnalysisEnvironment "tts.core.api.internalApi.AnalysisEnvironment.AnalysisEnvironment (Python class) — Object of analysis job procedure engine.")

Credentials[¶](#tts.core.api.internalApi.Api.Api.Credentials "Link to this definition")  
Access to [`Credentials`](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials "tts.core.api.internalApi.credentialsApi.Credentials.Credentials (Python class) — Access to the Credentials API") for handling Credentials such as certificates and private keys.

CurrentTestConfiguration[¶](#tts.core.api.internalApi.Api.Api.CurrentTestConfiguration "Link to this definition")  
Object for the [`TestConfiguration`](#tts.core.api.internalApi.TestConfiguration.TestConfiguration "tts.core.api.internalApi.TestConfiguration.TestConfiguration (Python class) — Object for accessing information about test configuration")

CurrentTestbenchConfiguration[¶](#tts.core.api.internalApi.Api.Api.CurrentTestbenchConfiguration "Link to this definition")  
Object for the [`TestbenchConfiguration`](#tts.core.api.internalApi.TestbenchConfiguration.TestbenchConfiguration "tts.core.api.internalApi.TestbenchConfiguration.TestbenchConfiguration (Python class) — Object for accessing information about test bench configuration")

DataBrowser[¶](#tts.core.api.internalApi.Api.Api.DataBrowser "Link to this definition")  
Object for the [`DataBrowser`](#tts.core.api.dataBrowserApi.DataBrowser.DataBrowser "tts.core.api.dataBrowserApi.DataBrowser.DataBrowser (Python class) — The DataBrowser provides functions to retrieve a specific object to a database of a configured device in the test configuration. Currently, there are interfaces to browse inside A2L, BUS , debugging (ELF), diagnostic, logging, multimedia, service and SGBD data of an electronic control unit (ECU). The interface to browse SGBD data is currently in a prototype state.")

Ethernet[¶](#tts.core.api.internalApi.Api.Api.Ethernet "Link to this definition")  
Access to various [`Ethernet`](busdatastructures.md#tts.core.api.internalApi.Ethernet.Ethernet "tts.core.api.internalApi.Ethernet.Ethernet (Python class) — Access to various Ethernet related packet types and constants") related packet types

GlobalConstants[¶](#tts.core.api.internalApi.Api.Api.GlobalConstants "Link to this definition")  
Object for the [`GlobalConstants`](#tts.core.api.internalApi.GlobalConstants.GlobalConstants "tts.core.api.internalApi.GlobalConstants.GlobalConstants (Python class) — This class represents a container for holding global constants. Use:")

KeywordCatalog[¶](#tts.core.api.internalApi.Api.Api.KeywordCatalog "Link to this definition")  
Offers key word catalog access methods

Math[¶](#tts.core.api.internalApi.Api.Api.Math "Link to this definition")  
Object for `Math`

Multimedia[¶](#tts.core.api.internalApi.Api.Api.Multimedia "Link to this definition")  
Object for [`MultimediaApi`](#tts.testModule.multimedia.api.MultimediaApi.MultimediaApi "tts.testModule.multimedia.api.MultimediaApi.MultimediaApi (Python class) — Provides access to multimedia content at runtime")

ObjectApi[¶](#tts.core.api.internalApi.Api.Api.ObjectApi "Link to this definition")  
Use this to access the [Object API](objectApi.md#objectapi) internally

Scm[¶](#tts.core.api.internalApi.Api.Api.Scm "Link to this definition")  
Object for [`Scm`](#tts.core.api.internalApi.Scm.Scm "tts.core.api.internalApi.Scm.Scm (Python class) — Functions for SCM")

Service[¶](#tts.core.api.internalApi.Api.Api.Service "Link to this definition")  
Object for [`Service`](#tts.core.api.internalApi.Service.Service "tts.core.api.internalApi.Service.Service (Python class) — Provides access to simulated Ethernet Services at runtime")

TestBench[¶](#tts.core.api.internalApi.Api.Api.TestBench "Link to this definition")  
Provides access to the [`TestBench`](#tts.core.api.internalApi.TestBench.TestBench "tts.core.api.internalApi.TestBench.TestBench (Python class) — Entry point for starting/stopping tools")

TestEnvironment[¶](#tts.core.api.internalApi.Api.Api.TestEnvironment "Link to this definition")  
Object for the [`TestEnvironment`](#tts.core.api.internalApi.TestEnvironment.TestEnvironment "tts.core.api.internalApi.TestEnvironment.TestEnvironment (Python class) — Object of test procedure engine")

TestManagement[¶](#tts.core.api.internalApi.Api.Api.TestManagement "Link to this definition")  
Object for the [`TestManagementApi`](#tts.core.api.internalApi.TestManagement.TestManagementApi "tts.core.api.internalApi.TestManagement.TestManagementApi (Python class) — API to interact with the configured test management system.")

ToolAccess[¶](#tts.core.api.internalApi.Api.Api.ToolAccess "Link to this definition")  
Access to [`ToolAccess`](#tts.core.api.internalApi.ToolAccess.ToolAccess "tts.core.api.internalApi.ToolAccess.ToolAccess (Python class) — Entry point for executing jobs on tools or ports.") for handling job execution.

UnitInfo[¶](#tts.core.api.internalApi.Api.Api.UnitInfo "Link to this definition")  
Object for the [`UnitInfo`](#tts.core.api.dataBrowserApi.UnitInfo.UnitInfo "tts.core.api.dataBrowserApi.UnitInfo.UnitInfo (Python class) — UnitInfo provides functions to retrieve information concerning unit definitions")

Workspace[¶](#tts.core.api.internalApi.Api.Api.Workspace "Link to this definition")  
Access to [`Workspace`](#tts.core.api.internalApi.Workspace.Workspace "tts.core.api.internalApi.Workspace.Workspace (Python class) — Access to workspace related information.").

GeneratePackageDocumentation(*[pkgPath](#tts.core.api.internalApi.Api.Api.GeneratePackageDocumentation.pkgPath "tts.core.api.internalApi.Api.Api.GeneratePackageDocumentation.pkgPath (Python parameter) — Path of either a package or a folder containing packages")*, *[docPath](#tts.core.api.internalApi.Api.Api.GeneratePackageDocumentation.docPath "tts.core.api.internalApi.Api.Api.GeneratePackageDocumentation.docPath (Python parameter) — Path where the documentation files will be created")*, *[doasync](#tts.core.api.internalApi.Api.Api.GeneratePackageDocumentation.doasync "tts.core.api.internalApi.Api.Api.GeneratePackageDocumentation.doasync (Python parameter) — Mode of execution: asynchronous if True otherwise synchronous")=`True`*)[¶](#tts.core.api.internalApi.Api.Api.GeneratePackageDocumentation "Link to this definition")  
Creates documentation file(s) for a package or all packages in a folder depending on the given path

Parameters:  pkgPath : str[¶](#tts.core.api.internalApi.Api.Api.GeneratePackageDocumentation.pkgPath "Permalink to this definition")  
Path of either a package or a folder containing packages

docPath : str[¶](#tts.core.api.internalApi.Api.Api.GeneratePackageDocumentation.docPath "Permalink to this definition")  
Path where the documentation files will be created

doasync : bool[¶](#tts.core.api.internalApi.Api.Api.GeneratePackageDocumentation.doasync "Permalink to this definition")  
Mode of execution: asynchronous if True otherwise synchronous

Returns:  Path of the generated (index) document if synchronous mode, otherwise None

Return type:  str or None

GetAppName()[¶](#tts.core.api.internalApi.Api.Api.GetAppName "Link to this definition")  
Returns the application name.

Return type:  str

GetSetting(*[value](#tts.core.api.internalApi.Api.Api.GetSetting.value "tts.core.api.internalApi.Api.Api.GetSetting.value (Python parameter) — The setting to return")*)[¶](#tts.core.api.internalApi.Api.Api.GetSetting "Link to this definition")  
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

Parameters:  value : str[¶](#tts.core.api.internalApi.Api.Api.GetSetting.value "Permalink to this definition")  
The setting to return

Returns:  The current value

Return type:  str or None

GetVersion()[¶](#tts.core.api.internalApi.Api.Api.GetVersion "Link to this definition")  
Returns the ecu.test version.

Return type:  str

IsRunner()[¶](#tts.core.api.internalApi.Api.Api.IsRunner "Link to this definition")  

## API classes[¶](#api-classes "Link to this heading")

### AnalysisEnvironment[¶](#analysisenvironment "Link to this heading")

*class* AnalysisEnvironment[¶](#tts.core.api.internalApi.AnalysisEnvironment.AnalysisEnvironment "Link to this definition")  
Object of analysis job procedure engine.

ExecutionInfo[¶](#tts.core.api.internalApi.AnalysisEnvironment.AnalysisEnvironment.ExecutionInfo "Link to this definition")  
The current [`AnalysisExecutionInfo`](#tts.core.api.internalApi.AnalysisExecutionInfo.AnalysisExecutionInfo "tts.core.api.internalApi.AnalysisExecutionInfo.AnalysisExecutionInfo (Python class) — Provides information for current analysis job execution") object.

Type:  list

ClearSignalCache()[¶](#tts.core.api.internalApi.AnalysisEnvironment.AnalysisEnvironment.ClearSignalCache "Link to this definition")  
Removes all signals from the signal cache.

Info

Calling this method can be useful in large projects analyzing many object signals (signals that are not of a primitive data type). Object signals are cached in memory. Thus, if the analyses of the project access different object signals, the memory consumption is continuously increasing. Calling this method frees all the memory consumed by the signal cache.

This method should be called at some point in the project, when it is known that most of the previously used signals are not required anymore for the following analyses or if the memory consumption has to be reduced. Calling this method too often, has a negative effect on the execution time.

In order to ensure that the signal cache is cleared completely, this method should be called in a separate episode or the test case part of a package.

### AnalysisExecutionInfo[¶](#analysisexecutioninfo "Link to this heading")

*class* AnalysisExecutionInfo[¶](#tts.core.api.internalApi.AnalysisExecutionInfo.AnalysisExecutionInfo "Link to this definition")  
Provides information for current analysis job execution

JobResult[¶](#tts.core.api.internalApi.AnalysisExecutionInfo.AnalysisExecutionInfo.JobResult "Link to this definition")  
The result of the current analysis job

Info

During job execution only completed episodes (and child trace steps) are considered. This means, the results of assertions and other steps above an episode are not considered.

Type:  str

LogFolder[¶](#tts.core.api.internalApi.AnalysisExecutionInfo.AnalysisExecutionInfo.LogFolder "Link to this definition")  
Folder where trace and logging files of the current analysis job are saved during execution

Info

This may be a temporary location, in case a network drive is used. [`TargetReportDbFolder`](#tts.core.api.internalApi.AnalysisExecutionInfo.AnalysisExecutionInfo.TargetReportDbFolder "tts.core.api.internalApi.AnalysisExecutionInfo.AnalysisExecutionInfo.TargetReportDbFolder (Python attribute) — Folder of the report database of the current analysis job execution after job completion.") may be used to deduce the final location from the final report location.

Type:  str

ReportDb[¶](#tts.core.api.internalApi.AnalysisExecutionInfo.AnalysisExecutionInfo.ReportDb "Link to this definition")  
Path to report database of current (or most recent) analysis job execution

Type:  str

ReportDbFolder[¶](#tts.core.api.internalApi.AnalysisExecutionInfo.AnalysisExecutionInfo.ReportDbFolder "Link to this definition")  
Folder of the report database of the current analysis job during execution

Info

This may be a temporary location, in case a network drive is used. [`TargetReportDbFolder`](#tts.core.api.internalApi.AnalysisExecutionInfo.AnalysisExecutionInfo.TargetReportDbFolder "tts.core.api.internalApi.AnalysisExecutionInfo.AnalysisExecutionInfo.TargetReportDbFolder (Python attribute) — Folder of the report database of the current analysis job execution after job completion.") returns the final location instead.

Type:  str

StartTime[¶](#tts.core.api.internalApi.AnalysisExecutionInfo.AnalysisExecutionInfo.StartTime "Link to this definition")  
Time where the current analysis job execution began

Type:  str

TargetReportDbFolder[¶](#tts.core.api.internalApi.AnalysisExecutionInfo.AnalysisExecutionInfo.TargetReportDbFolder "Link to this definition")  
Folder of the report database of the current analysis job execution after job completion.

Info

Trace and logging files may be located in the respective subfolders. In case a network drive is used, a temporary location is used during execution that is returned by [`ReportDbFolder`](#tts.core.api.internalApi.AnalysisExecutionInfo.AnalysisExecutionInfo.ReportDbFolder "tts.core.api.internalApi.AnalysisExecutionInfo.AnalysisExecutionInfo.ReportDbFolder (Python attribute) — Folder of the report database of the current analysis job during execution").

Type:  str

GetCurrentPackageFilename()[¶](#tts.core.api.internalApi.AnalysisExecutionInfo.AnalysisExecutionInfo.GetCurrentPackageFilename "Link to this definition")  
Returns the path to the package containing the episode that is currently running

Returns:  Path to the package

Return type:  str

GetMainPackageFilename()[¶](#tts.core.api.internalApi.AnalysisExecutionInfo.AnalysisExecutionInfo.GetMainPackageFilename "Link to this definition")  
Returns the path to the main package

Returns:  Path to the main package

Return type:  str

GetWatchTime(*[key](#tts.core.api.internalApi.AnalysisExecutionInfo.AnalysisExecutionInfo.GetWatchTime.key "tts.core.api.internalApi.AnalysisExecutionInfo.AnalysisExecutionInfo.GetWatchTime.key (Python parameter) — The identifier of the watch")=`'DefaultWatch'`*)[¶](#tts.core.api.internalApi.AnalysisExecutionInfo.AnalysisExecutionInfo.GetWatchTime "Link to this definition")  
Returns the difference between the current time and the start of a watch

Parameters:  key=`'DefaultWatch'`[¶](#tts.core.api.internalApi.AnalysisExecutionInfo.AnalysisExecutionInfo.GetWatchTime.key "Permalink to this definition")  
The identifier of the watch

Returns:  The time difference [ms]

Return type:  int

StartWatch(*[key](#tts.core.api.internalApi.AnalysisExecutionInfo.AnalysisExecutionInfo.StartWatch.key "tts.core.api.internalApi.AnalysisExecutionInfo.AnalysisExecutionInfo.StartWatch.key (Python parameter) — The identifier of the watch")=`'DefaultWatch'`*)[¶](#tts.core.api.internalApi.AnalysisExecutionInfo.AnalysisExecutionInfo.StartWatch "Link to this definition")  
Starts a watch or resets an existing watch

Parameters:  key : str[¶](#tts.core.api.internalApi.AnalysisExecutionInfo.AnalysisExecutionInfo.StartWatch.key "Permalink to this definition")  
The identifier of the watch

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
Container for BusSystems. Item Type: [`BusSystem`](#module-tts.core.api.internalApi.BusSystem "tts.core.api.internalApi.BusSystem (Python module)")

Count[¶](#tts.core.api.internalApi.BusSystems.BusSystems.Count "Link to this definition")  
The number of items in the collection

Type:  int

Item(*[idx](#tts.core.api.internalApi.BusSystems.BusSystems.Item.idx "tts.core.api.internalApi.BusSystems.BusSystems.Item.idx (Python parameter) — The index")*)[¶](#tts.core.api.internalApi.BusSystems.BusSystems.Item "Link to this definition")  
Returns the item at the specified index

Parameters:  idx : int[¶](#tts.core.api.internalApi.BusSystems.BusSystems.Item.idx "Permalink to this definition")  
The index

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
Container for Constants. Item Type: [`Constant`](#module-tts.core.api.internalApi.Constant "tts.core.api.internalApi.Constant (Python module)")

Count[¶](#tts.core.api.internalApi.Constants.Constants.Count "Link to this definition")  
The number of items in the collection

Type:  int

Item(*[idx](#tts.core.api.internalApi.Constants.Constants.Item.idx "tts.core.api.internalApi.Constants.Constants.Item.idx (Python parameter) — The index")*)[¶](#tts.core.api.internalApi.Constants.Constants.Item "Link to this definition")  
Returns the item at the specified index

Parameters:  idx : int[¶](#tts.core.api.internalApi.Constants.Constants.Item.idx "Permalink to this definition")  
The index

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
Container for Ecus. Item Type: [`Ecu`](#module-tts.core.api.internalApi.Ecu "tts.core.api.internalApi.Ecu (Python module)")

Count[¶](#tts.core.api.internalApi.Ecus.Ecus.Count "Link to this definition")  
The number of items in the collection

Type:  int

Item(*[idx](#tts.core.api.internalApi.Ecus.Ecus.Item.idx "tts.core.api.internalApi.Ecus.Ecus.Item.idx (Python parameter) — The index")*)[¶](#tts.core.api.internalApi.Ecus.Ecus.Item "Link to this definition")  
Returns the item at the specified index

Parameters:  idx : int[¶](#tts.core.api.internalApi.Ecus.Ecus.Item.idx "Permalink to this definition")  
The index

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
Container for environment communication systems. Item Type: [`EnvironmentCommunication`](#module-tts.testModule.envCom.internalApi.EnvironmentCommunication "tts.testModule.envCom.internalApi.EnvironmentCommunication (Python module)")

Count[¶](#tts.testModule.envCom.internalApi.EnvironmentCommunications.EnvironmentCommunications.Count "Link to this definition")  
The number of items in the collection

Type:  int

Item(*[idx](#tts.testModule.envCom.internalApi.EnvironmentCommunications.EnvironmentCommunications.Item.idx "tts.testModule.envCom.internalApi.EnvironmentCommunications.EnvironmentCommunications.Item.idx (Python parameter) — The index")*)[¶](#tts.testModule.envCom.internalApi.EnvironmentCommunications.EnvironmentCommunications.Item "Link to this definition")  
Returns the item at the specified index

Parameters:  idx : int[¶](#tts.testModule.envCom.internalApi.EnvironmentCommunications.EnvironmentCommunications.Item.idx "Permalink to this definition")  
The index

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
Container for environment simulation systems. Item Type: [`EnvironmentSimulation`](#module-tts.testModule.envSim.internalApi.EnvironmentSimulation "tts.testModule.envSim.internalApi.EnvironmentSimulation (Python module)")

Count[¶](#tts.testModule.envSim.internalApi.EnvironmentSimulations.EnvironmentSimulations.Count "Link to this definition")  
The number of items in the collection

Type:  int

Item(*[idx](#tts.testModule.envSim.internalApi.EnvironmentSimulations.EnvironmentSimulations.Item.idx "tts.testModule.envSim.internalApi.EnvironmentSimulations.EnvironmentSimulations.Item.idx (Python parameter) — The index")*)[¶](#tts.testModule.envSim.internalApi.EnvironmentSimulations.EnvironmentSimulations.Item "Link to this definition")  
Returns the item at the specified index

Parameters:  idx : int[¶](#tts.testModule.envSim.internalApi.EnvironmentSimulations.EnvironmentSimulations.Item.idx "Permalink to this definition")  
The index

Returns:  The item at index *idx*

Return type:  object

### GlobalConstants[¶](#globalconstants "Link to this heading")

*class* GlobalConstants[¶](#tts.core.api.internalApi.GlobalConstants.GlobalConstants "Link to this definition")  
This class represents a container for holding global constants. Use:

    GlobalConstants.YourConstantName

to get the value of any self defined constant.

GetConstant(*[name](#tts.core.api.internalApi.GlobalConstants.GlobalConstants.GetConstant.name "tts.core.api.internalApi.GlobalConstants.GlobalConstants.GetConstant.name (Python parameter) — The name of the constants to retrieve the value")*, *[default](#tts.core.api.internalApi.GlobalConstants.GlobalConstants.GetConstant.default "tts.core.api.internalApi.GlobalConstants.GlobalConstants.GetConstant.default (Python parameter) — The default value to return if the constant does not exists.")=`NOT_SET`*)[¶](#tts.core.api.internalApi.GlobalConstants.GlobalConstants.GetConstant "Link to this definition")  
Returns the value of the given constant

Parameters:  default=`NOT_SET`[¶](#tts.core.api.internalApi.GlobalConstants.GlobalConstants.GetConstant.default "Permalink to this definition")  
The default value to return if the constant does not exists. If this is not set, an exception is raised in this case.

name : str[¶](#tts.core.api.internalApi.GlobalConstants.GlobalConstants.GetConstant.name "Permalink to this definition")  
The name of the constants to retrieve the value

Returns:  The value of the constant

Return type:  *Any*

GetConstants()[¶](#tts.core.api.internalApi.GlobalConstants.GlobalConstants.GetConstants "Link to this definition")  
Returns a list of names containing all constants defined in this container

Returns:  A list of names

Return type:  list[str]

ORIGIN_DEFINED_AT_RUNTIME = `'defined at runtime'`[¶](#tts.core.api.internalApi.GlobalConstants.ORIGIN_DEFINED_AT_RUNTIME "Link to this definition")  

ORIGIN_MANIPULATED_AT_RUNTIME = `'manipulated at runtime'`[¶](#tts.core.api.internalApi.GlobalConstants.ORIGIN_MANIPULATED_AT_RUNTIME "Link to this definition")  

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

LoadCatalog(*[catalogName](#tts.core.api.internalApi.KeywordCatalogApi.KeywordCatalogApi.LoadCatalog.catalogName "tts.core.api.internalApi.KeywordCatalogApi.KeywordCatalogApi.LoadCatalog.catalogName (Python parameter) — Name of the catalog")*)[¶](#tts.core.api.internalApi.KeywordCatalogApi.KeywordCatalogApi.LoadCatalog "Link to this definition")  
Loads the referenced catalog

Parameters:  catalogName : str[¶](#tts.core.api.internalApi.KeywordCatalogApi.KeywordCatalogApi.LoadCatalog.catalogName "Permalink to this definition")  
Name of the catalog

Raises:  
**exception** – If an invalid catalog name has been referenced

SetProject(*[projectName](#tts.core.api.internalApi.KeywordCatalogApi.KeywordCatalogApi.SetProject.projectName "tts.core.api.internalApi.KeywordCatalogApi.KeywordCatalogApi.SetProject.projectName (Python parameter) — Project name")*)[¶](#tts.core.api.internalApi.KeywordCatalogApi.KeywordCatalogApi.SetProject "Link to this definition")  
Sets the referenced project

Parameters:  projectName : str[¶](#tts.core.api.internalApi.KeywordCatalogApi.KeywordCatalogApi.SetProject.projectName "Permalink to this definition")  
Project name

Raises:  
**exception** – If an invalid project name has been referenced

SetVariant(*[variantName](#tts.core.api.internalApi.KeywordCatalogApi.KeywordCatalogApi.SetVariant.variantName "tts.core.api.internalApi.KeywordCatalogApi.KeywordCatalogApi.SetVariant.variantName (Python parameter) — Variant name")*)[¶](#tts.core.api.internalApi.KeywordCatalogApi.KeywordCatalogApi.SetVariant "Link to this definition")  
Sets the referenced variant

Parameters:  variantName : str[¶](#tts.core.api.internalApi.KeywordCatalogApi.KeywordCatalogApi.SetVariant.variantName "Permalink to this definition")  
Variant name

Raises:  
**exception** – If an invalid variant name has been referenced

### Math[¶](#id16 "Link to this heading")

*class* Math  
Functions for Math

*static* RandomValue(*[value](#tts.core.api.internalApi.Math.Math.RandomValue.value "tts.core.api.internalApi.Math.Math.RandomValue.value (Python parameter) — Center for the range of possible values")*, *[absTolerance](#tts.core.api.internalApi.Math.Math.RandomValue.absTolerance "tts.core.api.internalApi.Math.Math.RandomValue.absTolerance (Python parameter) — Tolerance for the used value range (must be >= 0)")*, *[stepSize](#tts.core.api.internalApi.Math.Math.RandomValue.stepSize "tts.core.api.internalApi.Math.Math.RandomValue.stepSize (Python parameter) — Step size which is used to partition the value range (0 for continous distribution (must be >= 0))")=`0`*)  
Evaluates a random value around a center

Parameters:  value : float[¶](#tts.core.api.internalApi.Math.Math.RandomValue.value "Permalink to this definition")  
Center for the range of possible values

absTolerance : float[¶](#tts.core.api.internalApi.Math.Math.RandomValue.absTolerance "Permalink to this definition")  
Tolerance for the used value range (must be \>= 0)

stepSize : float[¶](#tts.core.api.internalApi.Math.Math.RandomValue.stepSize "Permalink to this definition")  
Step size which is used to partition the value range (0 for continous distribution (must be \>= 0))

Returns:  Random value (value - absTolerance \<= returnValue \<= value + absTolerance)

Return type:  float

*static* RandomValueMinMax(*[minValue](#tts.core.api.internalApi.Math.Math.RandomValueMinMax.minValue "tts.core.api.internalApi.Math.Math.RandomValueMinMax.minValue (Python parameter) — Center for the range of possible values")*, *[maxValue](#tts.core.api.internalApi.Math.Math.RandomValueMinMax.maxValue "tts.core.api.internalApi.Math.Math.RandomValueMinMax.maxValue (Python parameter) — Tolerance for the used value range (must be >= 0)")*, *[stepSize](#tts.core.api.internalApi.Math.Math.RandomValueMinMax.stepSize "tts.core.api.internalApi.Math.Math.RandomValueMinMax.stepSize (Python parameter) — Step size which is used to partition the value range (0 for continous distribution (must be >= 0))")=`0`*, *[includeMinValue](#tts.core.api.internalApi.Math.Math.RandomValueMinMax.includeMinValue "tts.core.api.internalApi.Math.Math.RandomValueMinMax.includeMinValue (Python parameter) — True if the minValue should be part of the distribution values (closed interval), else False.")=`True`*, *[includeMaxValue](#tts.core.api.internalApi.Math.Math.RandomValueMinMax.includeMaxValue "tts.core.api.internalApi.Math.Math.RandomValueMinMax.includeMaxValue (Python parameter) — True if the maxValue should be part of the distribution values (closed interval), else False.")=`False`*)  
Evaluates a random value in the from minValue to maxValue. It can be parameterized whether the interval includes minValue (default True) and maxValue (default False).

Parameters:  minValue : float[¶](#tts.core.api.internalApi.Math.Math.RandomValueMinMax.minValue "Permalink to this definition")  
Center for the range of possible values

maxValue : float[¶](#tts.core.api.internalApi.Math.Math.RandomValueMinMax.maxValue "Permalink to this definition")  
Tolerance for the used value range (must be \>= 0)

stepSize : float[¶](#tts.core.api.internalApi.Math.Math.RandomValueMinMax.stepSize "Permalink to this definition")  
Step size which is used to partition the value range (0 for continous distribution (must be \>= 0))

includeMinValue : bool[¶](#tts.core.api.internalApi.Math.Math.RandomValueMinMax.includeMinValue "Permalink to this definition")  
True if the minValue should be part of the distribution values (closed interval), else False.

includeMaxValue : bool[¶](#tts.core.api.internalApi.Math.Math.RandomValueMinMax.includeMaxValue "Permalink to this definition")  
True if the maxValue should be part of the distribution values (closed interval), else False.

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
Container for Models. Item Type: [`Model`](#module-tts.core.api.internalApi.Model "tts.core.api.internalApi.Model (Python module)")

Count[¶](#tts.core.api.internalApi.Models.Models.Count "Link to this definition")  
The number of items in the collection

Type:  int

Item(*[idx](#tts.core.api.internalApi.Models.Models.Item.idx "tts.core.api.internalApi.Models.Models.Item.idx (Python parameter) — The index")*)[¶](#tts.core.api.internalApi.Models.Models.Item "Link to this definition")  
Returns the item at the specified index

Parameters:  idx : int[¶](#tts.core.api.internalApi.Models.Models.Item.idx "Permalink to this definition")  
The index

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
Object for [`ImageFiltersApi`](#tts.testModule.multimedia.api.MultimediaApi.ImageFiltersApi "tts.testModule.multimedia.api.MultimediaApi.ImageFiltersApi (Python class) — Provides access to image filters. Filters are grouped into the two namespaces default and user. The following filters are provided by ecu.test out of the box:")

Type:  list

GetAvailableOCRServices()[¶](#tts.testModule.multimedia.api.MultimediaApi.MultimediaApi.GetAvailableOCRServices "Link to this definition")  
Returns a list of available OCR services. These identifiers can be used with GetOCRService.

Returns:  A list of OCR service identifiers

Return type:  list\<str\>

GetAvailableObjectDetectors()[¶](#tts.testModule.multimedia.api.MultimediaApi.MultimediaApi.GetAvailableObjectDetectors "Link to this definition")  
Returns the currently available object detectors.

Returns:  A list of configured object detectors.

Return type:  list\<str\>

GetAvailableSTTProfiles()[¶](#tts.testModule.multimedia.api.MultimediaApi.MultimediaApi.GetAvailableSTTProfiles "Link to this definition")  
Returns the currently available profiles for speech-to-text.

Returns:  A list of profile dictionaries containing the configured serviceId, profileName, language for each profile.

Return type:  list\<dict\<str:str\>\>

GetAvailableTTSVoices()[¶](#tts.testModule.multimedia.api.MultimediaApi.MultimediaApi.GetAvailableTTSVoices "Link to this definition")  
Gets the currently available voices for text-to-speech output.

Returns:  Returns a list of voice dictionaries containing the configured serviceId, voiceName, voiceLanguage, voiceGender for each voice.

Return type:  list\<dict\<str:str\>\>

GetDefaultOCRService(*[sut](#tts.testModule.multimedia.api.MultimediaApi.MultimediaApi.GetDefaultOCRService.sut "tts.testModule.multimedia.api.MultimediaApi.MultimediaApi.GetDefaultOCRService.sut (Python parameter) — The system under test whose OCR service should be created.")=`None`*)[¶](#tts.testModule.multimedia.api.MultimediaApi.MultimediaApi.GetDefaultOCRService "Link to this definition")  
Returns the OCR service that is configured in the active test configuration.

Parameters:  sut : str | None[¶](#tts.testModule.multimedia.api.MultimediaApi.MultimediaApi.GetDefaultOCRService.sut "Permalink to this definition")  
The system under test whose OCR service should be created. Can be omitted if only one system for media access exists.

Returns:  A new OCR service instance configured according to the test configuration

Return type:  [OCRService](mediadatastructures.md#tts.lib.ocr.OCRService.OCRService "tts.lib.ocr.OCRService.OCRService (Python class) — Returns the name of the service as a unique ID.")

GetOCRService(*[serviceId](#tts.testModule.multimedia.api.MultimediaApi.MultimediaApi.GetOCRService.serviceId "tts.testModule.multimedia.api.MultimediaApi.MultimediaApi.GetOCRService.serviceId (Python parameter) — Identifier of the OCR service to be created")*)[¶](#tts.testModule.multimedia.api.MultimediaApi.MultimediaApi.GetOCRService "Link to this definition")  
Creates a new OCR service instance from a given sevice ID.

Parameters:  serviceId : str[¶](#tts.testModule.multimedia.api.MultimediaApi.MultimediaApi.GetOCRService.serviceId "Permalink to this definition")  
Identifier of the OCR service to be created

Returns:  A new OCR service instance

Return type:  [OCRService](mediadatastructures.md#tts.lib.ocr.OCRService.OCRService "tts.lib.ocr.OCRService.OCRService (Python class) — Returns the name of the service as a unique ID.")

GetObjectDetector(*[detectorId](#tts.testModule.multimedia.api.MultimediaApi.MultimediaApi.GetObjectDetector.detectorId "tts.testModule.multimedia.api.MultimediaApi.MultimediaApi.GetObjectDetector.detectorId (Python parameter) — ID of the object detector to be created")*)[¶](#tts.testModule.multimedia.api.MultimediaApi.MultimediaApi.GetObjectDetector "Link to this definition")  
Creates a new object detector for a given ID.

Parameters:  detectorId : str[¶](#tts.testModule.multimedia.api.MultimediaApi.MultimediaApi.GetObjectDetector.detectorId "Permalink to this definition")  
ID of the object detector to be created

Returns:  A new object detector instance

Return type:  ObjectDetector

SpeechToText(*[audioBlock](#tts.testModule.multimedia.api.MultimediaApi.MultimediaApi.SpeechToText.audioBlock "tts.testModule.multimedia.api.MultimediaApi.MultimediaApi.SpeechToText.audioBlock (Python parameter) — The audio recording that should be converted to text.")*, *[profile](#tts.testModule.multimedia.api.MultimediaApi.MultimediaApi.SpeechToText.profile "tts.testModule.multimedia.api.MultimediaApi.MultimediaApi.SpeechToText.profile (Python parameter) — The profile to be used for speech recognition, identified by a dictionary containing serviceId, profileName, language and description.")=`None`*)[¶](#tts.testModule.multimedia.api.MultimediaApi.MultimediaApi.SpeechToText "Link to this definition")  
Converts voice to text. Returns the recognized text as a string.

Parameters:  audioBlock : [AudioBlock](mediadatastructures.md#tts.testModule.multimedia.dataElements.AudioBlock.AudioBlock "tts.testModule.multimedia.dataElements.AudioBlock.AudioBlock (Python class) — The source from which to load audio data (a file path or a NumPy array). In case of a file path it has to be an absolute path or a path relative to the workspace. In case of a NumPy array, the audio channels must either be a 1D NumPy array of shape (<frames>) for a one channel stream or a 2D NumPy array of shape (<frames>, <channels>) for a multiple channel stream. Array members must be of type np.int16 or float. The former will be internally normalized to float between -1.0 and 1.0.")[¶](#tts.testModule.multimedia.api.MultimediaApi.MultimediaApi.SpeechToText.audioBlock "Permalink to this definition")  
The audio recording that should be converted to text.

profile : dict[¶](#tts.testModule.multimedia.api.MultimediaApi.MultimediaApi.SpeechToText.profile "Permalink to this definition")  
The profile to be used for speech recognition, identified by a dictionary containing `serviceId`, `profileName`, `language` and `description`. See [`GetAvailableSTTProfiles()`](#tts.testModule.multimedia.api.MultimediaApi.MultimediaApi.GetAvailableSTTProfiles "tts.testModule.multimedia.api.MultimediaApi.MultimediaApi.GetAvailableSTTProfiles (Python method) — Returns the currently available profiles for speech-to-text.") for a list of valid values. If no profile is provided, the default profile that is configured in the test configuration will be used.

Returns:  The recognized text

Return type:  str

TextToSpeech(*[text](#tts.testModule.multimedia.api.MultimediaApi.MultimediaApi.TextToSpeech.text "tts.testModule.multimedia.api.MultimediaApi.MultimediaApi.TextToSpeech.text (Python parameter) — The text that should be converted to speech")*, *[voice](#tts.testModule.multimedia.api.MultimediaApi.MultimediaApi.TextToSpeech.voice "tts.testModule.multimedia.api.MultimediaApi.MultimediaApi.TextToSpeech.voice (Python parameter) — The voice to use for speech generation, identified by a dictionary containing serviceId, voiceName, voiceLanguage and voiceGender.")=`None`*, *[parameters](#tts.testModule.multimedia.api.MultimediaApi.MultimediaApi.TextToSpeech.parameters "tts.testModule.multimedia.api.MultimediaApi.MultimediaApi.TextToSpeech.parameters (Python parameter) — Optional dictionary with parameters for speech generation.")=`None`*)[¶](#tts.testModule.multimedia.api.MultimediaApi.MultimediaApi.TextToSpeech "Link to this definition")  
Converts text to speech. Returns the spoken text as an AudioBlock.

Parameters:  text : str[¶](#tts.testModule.multimedia.api.MultimediaApi.MultimediaApi.TextToSpeech.text "Permalink to this definition")  
The text that should be converted to speech

voice : dict[¶](#tts.testModule.multimedia.api.MultimediaApi.MultimediaApi.TextToSpeech.voice "Permalink to this definition")  
The voice to use for speech generation, identified by a dictionary containing `serviceId`, `voiceName`, `voiceLanguage` and `voiceGender`. See [`GetAvailableTTSVoices()`](#tts.testModule.multimedia.api.MultimediaApi.MultimediaApi.GetAvailableTTSVoices "tts.testModule.multimedia.api.MultimediaApi.MultimediaApi.GetAvailableTTSVoices (Python method) — Gets the currently available voices for text-to-speech output.") for a list of valid values. If no voice is provided, the default voice from the current test configuration will be used.

parameters : dict[¶](#tts.testModule.multimedia.api.MultimediaApi.MultimediaApi.TextToSpeech.parameters "Permalink to this definition")  
Optional dictionary with parameters for speech generation. For example the default parameters are `{'pitch': 0, 'speed': 1}`Returns:  
An AudioBlock containing the spoken text

Return type:  [AudioBlock](mediadatastructures.md#tts.testModule.multimedia.dataElements.AudioBlock.AudioBlock "tts.testModule.multimedia.dataElements.AudioBlock.AudioBlock (Python class) — The source from which to load audio data (a file path or a NumPy array). In case of a file path it has to be an absolute path or a path relative to the workspace. In case of a NumPy array, the audio channels must either be a 1D NumPy array of shape (<frames>) for a one channel stream or a 2D NumPy array of shape (<frames>, <channels>) for a multiple channel stream. Array members must be of type np.int16 or float. The former will be internally normalized to float between -1.0 and 1.0.")

### Scm[¶](#scm "Link to this heading")

*class* Scm[¶](#tts.core.api.internalApi.Scm.Scm "Link to this definition")  
Functions for SCM

GetCheckoutRevision()[¶](#tts.core.api.internalApi.Scm.Scm.GetCheckoutRevision "Link to this definition")  
Returns the revision number of the actual workspace repository

Returns:  - The revision of the actual workspace repository

- An empty string if the workspace is not versioned

- None if SCM is not available or not enabled in the user settings

Return type:  str or None

GetFileRevision(*[filename](#tts.core.api.internalApi.Scm.Scm.GetFileRevision.filename "tts.core.api.internalApi.Scm.Scm.GetFileRevision.filename (Python parameter) — Path to the file.")*)[¶](#tts.core.api.internalApi.Scm.Scm.GetFileRevision "Link to this definition")  
Returns the revision number of a given file

Parameters:  filename : str[¶](#tts.core.api.internalApi.Scm.Scm.GetFileRevision.filename "Permalink to this definition")  
Path to the file. Relative paths will be evaluated as relative to the workspace directory.

Returns:  - The revision of the file, e.g. u”8524” or u”8524m” for a locally modified file

- An empty string if the file does not exist or is not versioned

- None if SCM is not available or not enabled in the user settings

Return type:  str or None

GetFileStatus(*[filename](#tts.core.api.internalApi.Scm.Scm.GetFileStatus.filename "tts.core.api.internalApi.Scm.Scm.GetFileStatus.filename (Python parameter) — Path to the file.")*)[¶](#tts.core.api.internalApi.Scm.Scm.GetFileStatus "Link to this definition")  
Returns the status of a given file

Parameters:  filename : str[¶](#tts.core.api.internalApi.Scm.Scm.GetFileStatus.filename "Permalink to this definition")  
Path to the file. Relative paths will be evaluated as relative to the workspace directory

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

*static* GetUsedServices(*[systemIdentifier](#tts.core.api.internalApi.Service.Service.GetUsedServices.systemIdentifier "tts.core.api.internalApi.Service.Service.GetUsedServices.systemIdentifier (Python parameter) — Filter Mappings for given SystemIdentifier (default=None)")=`None`*, *[excludeRecordingOnlyMappings](#tts.core.api.internalApi.Service.Service.GetUsedServices.excludeRecordingOnlyMappings "tts.core.api.internalApi.Service.Service.GetUsedServices.excludeRecordingOnlyMappings (Python parameter) — Ignore Mappings which are exclusively used for recording (default=True)")=`True`*)[¶](#tts.core.api.internalApi.Service.Service.GetUsedServices "Link to this definition")  
Returns all SystemIdentifiers, EcuNames and ServiceNames used in the current test execution

Parameters:  systemIdentifier : str or None[¶](#tts.core.api.internalApi.Service.Service.GetUsedServices.systemIdentifier "Permalink to this definition")  
Filter Mappings for given SystemIdentifier (default=None)

excludeRecordingOnlyMappings : boolean[¶](#tts.core.api.internalApi.Service.Service.GetUsedServices.excludeRecordingOnlyMappings "Permalink to this definition")  
Ignore Mappings which are exclusively used for recording (default=True)

Returns:  A set of tuples containing SystemIdentifier, EcuName and ServiceName

Return type:  set[tuple[str, str, str]]

GenerateService(*[systemIdentifier](#tts.core.api.internalApi.Service.Service.GenerateService.systemIdentifier "tts.core.api.internalApi.Service.Service.GenerateService.systemIdentifier (Python parameter) — System identifier")*, *[ecuName](#tts.core.api.internalApi.Service.Service.GenerateService.ecuName "tts.core.api.internalApi.Service.Service.GenerateService.ecuName (Python parameter) — Ecu name")*, *[serviceName](#tts.core.api.internalApi.Service.Service.GenerateService.serviceName "tts.core.api.internalApi.Service.Service.GenerateService.serviceName (Python parameter) — Service name")*, *[projectName](#tts.core.api.internalApi.Service.Service.GenerateService.projectName "tts.core.api.internalApi.Service.Service.GenerateService.projectName (Python parameter) — Optional project name")=`''`*)[¶](#tts.core.api.internalApi.Service.Service.GenerateService "Link to this definition")  
Generates a service module for `systemIdentifier`, `ecuName` and `serviceName`

Parameters:  systemIdentifier : str[¶](#tts.core.api.internalApi.Service.Service.GenerateService.systemIdentifier "Permalink to this definition")  
System identifier

ecuName : str[¶](#tts.core.api.internalApi.Service.Service.GenerateService.ecuName "Permalink to this definition")  
Ecu name

serviceName : str[¶](#tts.core.api.internalApi.Service.Service.GenerateService.serviceName "Permalink to this definition")  
Service name

projectName : str[¶](#tts.core.api.internalApi.Service.Service.GenerateService.projectName "Permalink to this definition")  
Optional project name

GetPort(*[portName](#tts.core.api.internalApi.Service.Service.GetPort.portName "tts.core.api.internalApi.Service.Service.GetPort.portName (Python parameter) — Port identifier according to TBC")*)[¶](#tts.core.api.internalApi.Service.Service.GetPort "Link to this definition")  
Returns a service port for the given port name

Parameters:  portName : str[¶](#tts.core.api.internalApi.Service.Service.GetPort.portName "Permalink to this definition")  
Port identifier according to TBC

Returns:  Service Port

Return type:  [ServicePort](#tts.core.api.internalApi.Service.ServicePort "tts.core.api.internalApi.Service.ServicePort (Python class) — Functions for Ports in the context of simulated Ethernet Services")

*class* ServicePort[¶](#tts.core.api.internalApi.Service.ServicePort "Link to this definition")  
Functions for Ports in the context of simulated Ethernet Services

GetService(*[serviceName](#tts.core.api.internalApi.Service.ServicePort.GetService.serviceName "tts.core.api.internalApi.Service.ServicePort.GetService.serviceName (Python parameter) — Service identifier is a composition of optional projectName and ecuName and serviceName in the format [projectName.]<ecuName>_<serviceName>")*)[¶](#tts.core.api.internalApi.Service.ServicePort.GetService "Link to this definition")  
Returns a proxy to the service identified by `serviceName`

Parameters:  serviceName : str[¶](#tts.core.api.internalApi.Service.ServicePort.GetService.serviceName "Permalink to this definition")  
Service identifier is a composition of optional projectName and ecuName and serviceName in the format [projectName.]\<ecuName\>\_\<serviceName\>

Returns:  Service Proxy

Return type:  [ServiceProxy](#tts.core.api.internalApi.Service.ServiceProxy "tts.core.api.internalApi.Service.ServiceProxy (Python class) — Service proxy for a running simulated Ethernet Service. Service methods can be called on this object, and will be executed on the service instance.")

StartService(*[serviceName](#tts.core.api.internalApi.Service.ServicePort.StartService.serviceName "tts.core.api.internalApi.Service.ServicePort.StartService.serviceName (Python parameter) — Service identifier is a composition of optional projectName and ecuName and serviceName in the format [projectName.]<ecuName>_<serviceName>")*)[¶](#tts.core.api.internalApi.Service.ServicePort.StartService "Link to this definition")  
Starts the service identified by `serviceName` on this port

Parameters:  serviceName : str[¶](#tts.core.api.internalApi.Service.ServicePort.StartService.serviceName "Permalink to this definition")  
Service identifier is a composition of optional projectName and ecuName and serviceName in the format [projectName.]\<ecuName\>\_\<serviceName\>

StopService(*[serviceName](#tts.core.api.internalApi.Service.ServicePort.StopService.serviceName "tts.core.api.internalApi.Service.ServicePort.StopService.serviceName (Python parameter) — service identifier is a composition of optional projectName and ecuName and serviceName in the format [projectName.]<ecuName>_<serviceName>")*)[¶](#tts.core.api.internalApi.Service.ServicePort.StopService "Link to this definition")  
Stops the service identified by `serviceName` on this port

Parameters:  serviceName : str[¶](#tts.core.api.internalApi.Service.ServicePort.StopService.serviceName "Permalink to this definition")  
service identifier is a composition of optional projectName and ecuName and serviceName in the format [projectName.]\<ecuName\>\_\<serviceName\>

*class* ServiceProxy[¶](#tts.core.api.internalApi.Service.ServiceProxy "Link to this definition")  
Service proxy for a running simulated Ethernet Service. Service methods can be called on this object, and will be executed on the service instance.

*static* GetFunctionsHelp(*[name](#tts.core.api.internalApi.Service.ServiceProxy.GetFunctionsHelp.name "tts.core.api.internalApi.Service.ServiceProxy.GetFunctionsHelp.name (Python parameter) — Name of function")*, *[serviceName](#tts.core.api.internalApi.Service.ServiceProxy.GetFunctionsHelp.serviceName "tts.core.api.internalApi.Service.ServiceProxy.GetFunctionsHelp.serviceName (Python parameter) — Service identifier is a composition of optional projectName and ecuName and serviceName in the format [projectName.]<ecuName>_<serviceName>")*)[¶](#tts.core.api.internalApi.Service.ServiceProxy.GetFunctionsHelp "Link to this definition")  
Provides the docstring of a function of the service simulation

Parameters:  name : str[¶](#tts.core.api.internalApi.Service.ServiceProxy.GetFunctionsHelp.name "Permalink to this definition")  
Name of function

serviceName : str[¶](#tts.core.api.internalApi.Service.ServiceProxy.GetFunctionsHelp.serviceName "Permalink to this definition")  
Service identifier is a composition of optional projectName and ecuName and serviceName in the format [projectName.]\<ecuName\>\_\<serviceName\>

Return type:  str

*static* GetServiceFunctions(*[serviceName](#tts.core.api.internalApi.Service.ServiceProxy.GetServiceFunctions.serviceName "tts.core.api.internalApi.Service.ServiceProxy.GetServiceFunctions.serviceName (Python parameter) — Service identifier is a composition of optional projectName and ecuName and serviceName in the format [projectName.]<ecuName>_<serviceName>")*)[¶](#tts.core.api.internalApi.Service.ServiceProxy.GetServiceFunctions "Link to this definition")  
Provides available functions of a service simulation

Parameters:  serviceName : str[¶](#tts.core.api.internalApi.Service.ServiceProxy.GetServiceFunctions.serviceName "Permalink to this definition")  
Service identifier is a composition of optional projectName and ecuName and serviceName in the format [projectName.]\<ecuName\>\_\<serviceName\>

Return type:  list[str]

### TestBench[¶](#testbench "Link to this heading")

*class* TestBench[¶](#tts.core.api.internalApi.TestBench.TestBench "Link to this definition")  
Entry point for starting/stopping tools

GetPortStatus(*[portName](#tts.core.api.internalApi.TestBench.TestBench.GetPortStatus.portName "tts.core.api.internalApi.TestBench.TestBench.GetPortStatus.portName (Python parameter) — Name of the port as shown in the "Host / Tool / Port" column in the test bench configuration editor (e.g.")*)[¶](#tts.core.api.internalApi.TestBench.TestBench.GetPortStatus "Link to this definition")  
Retrieves the status of the port.

Parameters:  portName : str[¶](#tts.core.api.internalApi.TestBench.TestBench.GetPortStatus.portName "Permalink to this definition")  
Name of the port as shown in the “Host / Tool / Port” column in the test bench configuration editor (e.g. “MDL-DEFAULT01”)

Returns:  Status of the port

- 0 (Stopped, shown gray in the tool status monitor)

- 1 (Started, shown green in the tool status monitor)

- 2 (Broken, shown red in the tool status monitor)

Return type:  int

GetToolStatus(*[toolId](#tts.core.api.internalApi.TestBench.TestBench.GetToolStatus.toolId "tts.core.api.internalApi.TestBench.TestBench.GetToolStatus.toolId (Python parameter) — ID of the tool as shown in the tooltip in the test bench configuration editor (e.g.")*)[¶](#tts.core.api.internalApi.TestBench.TestBench.GetToolStatus "Link to this definition")  
Retrieves the status of the tool.

Parameters:  toolId : str[¶](#tts.core.api.internalApi.TestBench.TestBench.GetToolStatus.toolId "Permalink to this definition")  
ID of the tool as shown in the tooltip in the test bench configuration editor (e.g. “CONTROLDESKNG01”)

Returns:  Status of the tool

- 0 (Stopped, shown gray in the tool status monitor)

- 1 (Started, shown green in the tool status monitor)

- 2 (Broken, shown red in the tool status monitor)

Return type:  int

StartTool(*[toolId](#tts.core.api.internalApi.TestBench.TestBench.StartTool.toolId "tts.core.api.internalApi.TestBench.TestBench.StartTool.toolId (Python parameter) — ID of the tool as shown in the ToolTip in the testbench configuration editor (e.g.")*)[¶](#tts.core.api.internalApi.TestBench.TestBench.StartTool "Link to this definition")  
Starts the specified tool

Info

This is not the recommended way of changing the status of connected tools. Instead, a configuration change step in a project should be used.

Warning

Updates variable descriptions. Because signals are registered during test case initialization, accessing signals provided by a tool started via this method is in most cases not possible within the same test case.

Parameters:  toolId : str[¶](#tts.core.api.internalApi.TestBench.TestBench.StartTool.toolId "Permalink to this definition")  
ID of the tool as shown in the ToolTip in the testbench configuration editor (e.g. CONTROLDESKNG01)

Returns:  True if the tool was started successfully or had been started already, else False

Return type:  bool

StopTool(*[toolId](#tts.core.api.internalApi.TestBench.TestBench.StopTool.toolId "tts.core.api.internalApi.TestBench.TestBench.StopTool.toolId (Python parameter) — ID of the tool as shown in the ToolTip in the testbench configuration editor (e.g.")*)[¶](#tts.core.api.internalApi.TestBench.TestBench.StopTool "Link to this definition")  
Stops the specified tool.

Info

This is not the recommended way of changing the status of connected tools. Instead, a configuration change step in a project should be used.

Warning

Unloads the model description assigned to the ports of the stopped tool. Can break mapping and timestamp streaming within the same test case.

Any subsequent access to the tool, both explicitly by a test step and implicitly by cleanup for previous test steps, can lead to completely unpredictable behavior after this call.

Parameters:  toolId : str[¶](#tts.core.api.internalApi.TestBench.TestBench.StopTool.toolId "Permalink to this definition")  
ID of the tool as shown in the ToolTip in the testbench configuration editor (e.g. CONTROLDESKNG01)

Returns:  True if the tool was stopped successfully, had been stopped already or had never been started in the first place, else False

Return type:  bool

### TestbenchConfiguration[¶](#testbenchconfiguration "Link to this heading")

*class* TestbenchConfiguration[¶](#tts.core.api.internalApi.TestbenchConfiguration.TestbenchConfiguration "Link to this definition")  
Object for accessing information about test bench configuration

Filename[¶](#tts.core.api.internalApi.TestbenchConfiguration.TestbenchConfiguration.Filename "Link to this definition")  
The filename of the test bench configuration

Type:  str

ToolList[¶](#tts.core.api.internalApi.TestbenchConfiguration.TestbenchConfiguration.ToolList "Link to this definition")  
List containing objects of type [`TestbenchTool`](#tts.core.api.internalApi.TestbenchTool.TestbenchTool "tts.core.api.internalApi.TestbenchTool.TestbenchTool (Python class) — Provides information about the respective tool in the test bench configuration")

Type:  list([`TestbenchTool`](#tts.core.api.internalApi.TestbenchTool.TestbenchTool "tts.core.api.internalApi.TestbenchTool.TestbenchTool (Python class) — Provides information about the respective tool in the test bench configuration"))

GetToolhostInfo()[¶](#tts.core.api.internalApi.TestbenchConfiguration.TestbenchConfiguration.GetToolhostInfo "Link to this definition")  
Returns a list of lists containing url, version, revision and loaded patches of all connected toolhosts

Returns:  List of lists containing toolhost information

Return type:  list\<list\>

### TestbenchTool[¶](#testbenchtool "Link to this heading")

*class* TestbenchTool[¶](#tts.core.api.internalApi.TestbenchTool.TestbenchTool "Link to this definition")  
Provides information about the respective tool in the test bench configuration

Jobs[¶](#tts.core.api.internalApi.TestbenchTool.TestbenchTool.Jobs "Link to this definition")  
List containing the names of the tool jobs

Type:  list\<str\>

Location[¶](#tts.core.api.internalApi.TestbenchTool.TestbenchTool.Location "Link to this definition")  
Location (host) of the tool

Type:  str

Name[¶](#tts.core.api.internalApi.TestbenchTool.TestbenchTool.Name "Link to this definition")  
Name of the tool

Type:  str

PortList[¶](#tts.core.api.internalApi.TestbenchTool.TestbenchTool.PortList "Link to this definition")  
List containing objects of type `ToolPort`

Type:  list(`ToolPort`)

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

Info

For most properties it is enough to have the test configuration selected and not loaded.

BusSystems[¶](#tts.core.api.internalApi.TestConfiguration.TestConfiguration.BusSystems "Link to this definition")  
Collection for [`BusSystems`](#tts.core.api.internalApi.BusSystems.BusSystems "tts.core.api.internalApi.BusSystems.BusSystems (Python class) — Container for BusSystems. Item Type: BusSystem")

Type:  list

Ecus[¶](#tts.core.api.internalApi.TestConfiguration.TestConfiguration.Ecus "Link to this definition")  
Collection for [`Ecus`](#tts.core.api.internalApi.Ecus.Ecus "tts.core.api.internalApi.Ecus.Ecus (Python class) — Container for Ecus. Item Type: Ecu")

Type:  list

EnvironmentCommunications[¶](#tts.core.api.internalApi.TestConfiguration.TestConfiguration.EnvironmentCommunications "Link to this definition")  
Collection for [`EnvironmentCommunications`](#module-tts.testModule.envCom.internalApi.EnvironmentCommunications "tts.testModule.envCom.internalApi.EnvironmentCommunications (Python module)")

Type:  list

EnvironmentSimulations[¶](#tts.core.api.internalApi.TestConfiguration.TestConfiguration.EnvironmentSimulations "Link to this definition")  
Collection for [`EnvironmentSimulations`](#module-tts.testModule.envSim.internalApi.EnvironmentSimulations "tts.testModule.envSim.internalApi.EnvironmentSimulations (Python module)")

Type:  list

Filename[¶](#tts.core.api.internalApi.TestConfiguration.TestConfiguration.Filename "Link to this definition")  
Absolute path of the test configuration

Type:  str

GlobalConstants[¶](#tts.core.api.internalApi.TestConfiguration.TestConfiguration.GlobalConstants "Link to this definition")  
Collection for [`Constants`](#tts.core.api.internalApi.Constants.Constants "tts.core.api.internalApi.Constants.Constants (Python class) — Container for Constants. Item Type: Constant")

Info

Test configuration has to be loaded.

Type:  list

Models[¶](#tts.core.api.internalApi.TestConfiguration.TestConfiguration.Models "Link to this definition")  
Collection for [`Models`](#tts.core.api.internalApi.Models.Models "tts.core.api.internalApi.Models.Models (Python class) — Container for Models. Item Type: Model")

Type:  list

NameTester[¶](#tts.core.api.internalApi.TestConfiguration.TestConfiguration.NameTester "Link to this definition")  
Name of the tester

Type:  str

ReloadGlobalMapping()[¶](#tts.core.api.internalApi.TestConfiguration.TestConfiguration.ReloadGlobalMapping "Link to this definition")  
Reloads the global mapping from the test configuration without reloading the whole configuration

Info

Closed files are loaded, changed files are reloaded, additional files are unloaded.

Info

Calling this method has no effect on the package from which it is called but only on subsequent packages.

Warning

Changes in unsaved loaded mapping files are discarded when calling this method!

### TestEnvironment[¶](#testenvironment "Link to this heading")

*class* TestEnvironment[¶](#tts.core.api.internalApi.TestEnvironment.TestEnvironment "Link to this definition")  
Object of test procedure engine

ExecutionInfo[¶](#tts.core.api.internalApi.TestEnvironment.TestEnvironment.ExecutionInfo "Link to this definition")  
The current [`TestExecutionInfo`](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo "tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo (Python class) — Provides information for current test execution.") object

GenerateTestReportDocumentFromDB(*[dbFile](#tts.core.api.internalApi.TestEnvironment.TestEnvironment.GenerateTestReportDocumentFromDB.dbFile "tts.core.api.internalApi.TestEnvironment.TestEnvironment.GenerateTestReportDocumentFromDB.dbFile (Python parameter) — Path to the report database file (.trf or .prf)")*, *[outDir](#tts.core.api.internalApi.TestEnvironment.TestEnvironment.GenerateTestReportDocumentFromDB.outDir "tts.core.api.internalApi.TestEnvironment.TestEnvironment.GenerateTestReportDocumentFromDB.outDir (Python parameter) — The output directory.")*, *[fmtName](#tts.core.api.internalApi.TestEnvironment.TestEnvironment.GenerateTestReportDocumentFromDB.fmtName "tts.core.api.internalApi.TestEnvironment.TestEnvironment.GenerateTestReportDocumentFromDB.fmtName (Python parameter) — Name of the report format or handler which should be used (optional) (default is HTML)")=`None`*, *[waitUntilFinished](#tts.core.api.internalApi.TestEnvironment.TestEnvironment.GenerateTestReportDocumentFromDB.waitUntilFinished "tts.core.api.internalApi.TestEnvironment.TestEnvironment.GenerateTestReportDocumentFromDB.waitUntilFinished (Python parameter) — Defines whether the API call should block until generation is finished")=`False`*, *[fmtConfig](#tts.core.api.internalApi.TestEnvironment.TestEnvironment.GenerateTestReportDocumentFromDB.fmtConfig "tts.core.api.internalApi.TestEnvironment.TestEnvironment.GenerateTestReportDocumentFromDB.fmtConfig (Python parameter) — Optional dictionary {name: value} of additional configuration parameters for the report format")=`None`*)[¶](#tts.core.api.internalApi.TestEnvironment.TestEnvironment.GenerateTestReportDocumentFromDB "Link to this definition")  
Generates a handler-based test report on the filesystem

Parameters:  dbFile : str[¶](#tts.core.api.internalApi.TestEnvironment.TestEnvironment.GenerateTestReportDocumentFromDB.dbFile "Permalink to this definition")  
Path to the report database file (.trf or .prf)

outDir : str[¶](#tts.core.api.internalApi.TestEnvironment.TestEnvironment.GenerateTestReportDocumentFromDB.outDir "Permalink to this definition")  
The output directory. Absolute or relative to the program’s report directory

fmtName : str[¶](#tts.core.api.internalApi.TestEnvironment.TestEnvironment.GenerateTestReportDocumentFromDB.fmtName "Permalink to this definition")  
Name of the report format or handler which should be used (optional) (default is HTML)

waitUntilFinished : boolean[¶](#tts.core.api.internalApi.TestEnvironment.TestEnvironment.GenerateTestReportDocumentFromDB.waitUntilFinished "Permalink to this definition")  
Defines whether the API call should block until generation is finished

fmtConfig : dict\<str, str\>[¶](#tts.core.api.internalApi.TestEnvironment.TestEnvironment.GenerateTestReportDocumentFromDB.fmtConfig "Permalink to this definition")  
Optional dictionary {name: value} of additional configuration parameters for the report format

GetPackageReferences(*[filePath](#tts.core.api.internalApi.TestEnvironment.TestEnvironment.GetPackageReferences.filePath "tts.core.api.internalApi.TestEnvironment.TestEnvironment.GetPackageReferences.filePath (Python parameter) — Path of package or project (relative to the package directory or absolute)")*, *[skipDisabled](#tts.core.api.internalApi.TestEnvironment.TestEnvironment.GetPackageReferences.skipDisabled "tts.core.api.internalApi.TestEnvironment.TestEnvironment.GetPackageReferences.skipDisabled (Python parameter) — Flag to include disabled test steps or not")=`True`*)[¶](#tts.core.api.internalApi.TestEnvironment.TestEnvironment.GetPackageReferences "Link to this definition")  
Gives a set of all referenced sub packages of this package or project depending on the actual configuration

Parameters:  filePath : str[¶](#tts.core.api.internalApi.TestEnvironment.TestEnvironment.GetPackageReferences.filePath "Permalink to this definition")  
Path of package or project (relative to the package directory or absolute)

skipDisabled : boolean[¶](#tts.core.api.internalApi.TestEnvironment.TestEnvironment.GetPackageReferences.skipDisabled "Permalink to this definition")  
Flag to include disabled test steps or not

Returns:  List of package references with absolute file path

Return type:  list\<str\>

TimeElapsing()[¶](#tts.core.api.internalApi.TestEnvironment.TestEnvironment.TimeElapsing "Link to this definition")  
Resumes a stepwise simulation time when entering the context manager. Pauses the simulation time on context manager exit. This requires that a test execution is running. Does have no effect in real time or continuous simulation time.

Returns:  The context manager.

Return type:  Iterator[None]

Wait(*[seconds](#tts.core.api.internalApi.TestEnvironment.TestEnvironment.Wait "tts.core.api.internalApi.TestEnvironment.TestEnvironment.Wait.seconds (Python parameter)")*)[¶](#tts.core.api.internalApi.TestEnvironment.TestEnvironment.Wait "Link to this definition")  
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

GetArgumentUnit(*[argName](#tts.core.api.internalApi.TestExecutionInfo.KeywordInfo.GetArgumentUnit.argName "tts.core.api.internalApi.TestExecutionInfo.KeywordInfo.GetArgumentUnit.argName (Python parameter) — The name of the desired argument")*)[¶](#tts.core.api.internalApi.TestExecutionInfo.KeywordInfo.GetArgumentUnit "Link to this definition")  
Returns the unit of the given argument configured in the test step

Parameters:  argName : str[¶](#tts.core.api.internalApi.TestExecutionInfo.KeywordInfo.GetArgumentUnit.argName "Permalink to this definition")  
The name of the desired argument

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

GetReturnUnit(*[retName](#tts.core.api.internalApi.TestExecutionInfo.KeywordInfo.GetReturnUnit.retName "tts.core.api.internalApi.TestExecutionInfo.KeywordInfo.GetReturnUnit.retName (Python parameter) — The name of the desired return parameter or None if only one exists")=`None`*)[¶](#tts.core.api.internalApi.TestExecutionInfo.KeywordInfo.GetReturnUnit "Link to this definition")  
Returns the unit of the given return parameter configured in the test step

Parameters:  retName : str or None[¶](#tts.core.api.internalApi.TestExecutionInfo.KeywordInfo.GetReturnUnit.retName "Permalink to this definition")  
The name of the desired return parameter or None if only one exists

Returns:  Unit of the return parameter or None

Return type:  str or None

GetReturns()[¶](#tts.core.api.internalApi.TestExecutionInfo.KeywordInfo.GetReturns "Link to this definition")  
Returns a list all return parameters

Returns:  All return parameters

Return type:  list\<str\>

GetTimeOptionDuration(*[asUnit](#tts.core.api.internalApi.TestExecutionInfo.KeywordInfo.GetTimeOptionDuration.asUnit "tts.core.api.internalApi.TestExecutionInfo.KeywordInfo.GetTimeOptionDuration.asUnit (Python parameter) — Return the value in the desired unit.")=`None`*)[¶](#tts.core.api.internalApi.TestExecutionInfo.KeywordInfo.GetTimeOptionDuration "Link to this definition")  
Returns the minimum duration of the configured time option or None if not set

Parameters:  asUnit : str ('ms', 's', 'min', 'h', 'd')[¶](#tts.core.api.internalApi.TestExecutionInfo.KeywordInfo.GetTimeOptionDuration.asUnit "Permalink to this definition")  
Return the value in the desired unit. Default is None, the value as it is.

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

GetTimeOptionPollingCycle(*[asUnit](#tts.core.api.internalApi.TestExecutionInfo.KeywordInfo.GetTimeOptionPollingCycle.asUnit "tts.core.api.internalApi.TestExecutionInfo.KeywordInfo.GetTimeOptionPollingCycle.asUnit (Python parameter) — Return the value in the desired unit.")=`None`*)[¶](#tts.core.api.internalApi.TestExecutionInfo.KeywordInfo.GetTimeOptionPollingCycle "Link to this definition")  
Returns the polling cycle of the configured time option or None if not set

Parameters:  asUnit : str ('ms', 's', 'min', 'h', 'd')[¶](#tts.core.api.internalApi.TestExecutionInfo.KeywordInfo.GetTimeOptionPollingCycle.asUnit "Permalink to this definition")  
Return the value in the desired unit. Default is None, the value as it is.

Returns:  The polling cycle value

Return type:  int or float

GetTimeOptionTimeout(*[asUnit](#tts.core.api.internalApi.TestExecutionInfo.KeywordInfo.GetTimeOptionTimeout.asUnit "tts.core.api.internalApi.TestExecutionInfo.KeywordInfo.GetTimeOptionTimeout.asUnit (Python parameter) — Return the value in the desired unit.")=`None`*)[¶](#tts.core.api.internalApi.TestExecutionInfo.KeywordInfo.GetTimeOptionTimeout "Link to this definition")  
Returns the timeout of the configured time option or None if not set

Parameters:  asUnit : str ('ms', 's', 'min', 'h', 'd')[¶](#tts.core.api.internalApi.TestExecutionInfo.KeywordInfo.GetTimeOptionTimeout.asUnit "Permalink to this definition")  
Return the value in the desired unit. Default is None, the value as it is.

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
Provides information for current test execution.

All API functions refer to the context of the currently synchronously called package. Information within asynchronous/parallel package executions cannot be provided.

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

Type:  [`KeywordInfo`](#tts.core.api.internalApi.TestExecutionInfo.KeywordInfo "tts.core.api.internalApi.TestExecutionInfo.KeywordInfo (Python class) — KeywordInfo provides an interface to query properties of the currently executed keyword teststep")

LastTestStepResult[¶](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.LastTestStepResult "Link to this definition")  
Test result of the last executed teststep in the same test step hierarchy in main package execution. Not intended for parallel package calls.

Type:  str

LogFolder[¶](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.LogFolder "Link to this definition")  
Folder where trace and logging files of the current main package are saved during execution

Info

This may be a temporary location, in case a network drive is used. [`TargetReportDbFolder`](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.TargetReportDbFolder "tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.TargetReportDbFolder (Python attribute) — Folder of the report database of the current main package after completion of the package run") may be used to deduce the final location from the final report location.

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

Info

This may be a temporary location, in case a network drive is used. [`TargetReportDbFolder`](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.TargetReportDbFolder "tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.TargetReportDbFolder (Python attribute) — Folder of the report database of the current main package after completion of the package run") returns the final report location instead.

Type:  str

RunningTime[¶](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.RunningTime "Link to this definition")  
Difference between the current time and the start of the testexecution

Type:  int

StartTime[¶](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.StartTime "Link to this definition")  
Time where the current testexecution began

Type:  float

TargetReportDbFolder[¶](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.TargetReportDbFolder "Link to this definition")  
Folder of the report database of the current main package after completion of the package run

Info

Trace and logging files may be located in the respective subfolders. In case a network drive is used, a temporary location is used during execution that is returned by [`ReportDbFolder`](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.ReportDbFolder "tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.ReportDbFolder (Python attribute) — Folder of the report database of the current test run during execution").

Type:  str

AddArtifact(*[fileName](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.AddArtifact.fileName "tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.AddArtifact.fileName (Python parameter) — File name of the artifact")=`None`*, *[filePath](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.AddArtifact.filePath "tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.AddArtifact.filePath (Python parameter) — Path or URI to the artifact.")=`''`*, *[context](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.AddArtifact.context "tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.AddArtifact.context (Python parameter) — Additional context / comment for the artifact.")=`None`*)[¶](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.AddArtifact "Link to this definition")  
Adds an artifact reference to the test report.

Parameters:  fileName : str or None[¶](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.AddArtifact.fileName "Permalink to this definition")  
File name of the artifact

filePath : str[¶](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.AddArtifact.filePath "Permalink to this definition")  
Path or URI to the artifact. If the file is accessible on the local file system, a md5 hashsum will be calculated. The prefix ‘report://’ denotes a relative path within the current report directory. To copy a file to this location use the [`TargetReportDbFolder`](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.TargetReportDbFolder "tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.TargetReportDbFolder (Python attribute) — Folder of the report database of the current main package after completion of the package run") property.

context : str or None[¶](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.AddArtifact.context "Permalink to this definition")  
Additional context / comment for the artifact.

AddTestStepReportDetail(*[text](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.AddTestStepReportDetail.text "tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.AddTestStepReportDetail.text (Python parameter) — The text to be added in the report details")*)[¶](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.AddTestStepReportDetail "Link to this definition")  
Adds a text to the “custom data” section of the currently running teststep’s report details

Info

The entry will be added with a leading time stamp of the test execution. This feature is only available within a package execution. When used within a project step (e.g. a project generator) an error will be raised.

Parameters:  text : str[¶](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.AddTestStepReportDetail.text "Permalink to this definition")  
The text to be added in the report details

GetCurrentPackageFilename()[¶](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.GetCurrentPackageFilename "Link to this definition")  
Returns the file name of the current subpackage

Info

Infos of Packages executed in parallel are not returned.

Returns:  File name of current subpackage file or an empty string if the Package is not saved

Return type:  str

GetCurrentPackagePath()[¶](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.GetCurrentPackagePath "Link to this definition")  
Returns the absolute file system path of the current subpackage

Info

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

Return type:  list\<[`ExecutionExceptionInfo`](#tts.core.api.internalApi.TestExecutionInfo.ExecutionExceptionInfo "tts.core.api.internalApi.TestExecutionInfo.ExecutionExceptionInfo (Python class) — Provides information about an exception that has happened during test execution")\>

GetExecutionMode()[¶](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.GetExecutionMode "Link to this definition")  
Returns the bit field coding the execution mode of the package or project:

- NO_JOB_EXECUTION = 0

- SEQUENTIAL_JOB_EXECUTION = 1

- PARALLEL_JOB_EXECUTION = 2 (project execution only)

- DISABLE_JOBREPORT_MERGE = 4 (project execution only)

- SKIP_TESTCASE = 8

- DOWNSTREAM_JOB_EXECUTION = 16 (project execution only)

Returns:  bit field coding the execution mode of the package or project.

Return type:  int

Info

May return None if called within the trace analysis during PARALLEL_JOB_EXECUTION. SEQUENTIAL_JOB_EXECUTION, PARALLEL_JOB_EXECUTION and DOWNSTREAM_JOB_EXECUTION can not be set at the same time.

GetKeywordInfo()[¶](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.GetKeywordInfo "Link to this definition")  
Returns an information object of the current executed keyword call

Returns:  The information object of the current keyword call

Return type:  [`KeywordInfo`](#tts.core.api.internalApi.TestExecutionInfo.KeywordInfo "tts.core.api.internalApi.TestExecutionInfo.KeywordInfo (Python class) — KeywordInfo provides an interface to query properties of the currently executed keyword teststep")

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

GetMappingNames(*[scope](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.GetMappingNames.scope "tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.GetMappingNames.scope (Python parameter) — The scope of the mapping space to look in.")=`'exec'`*)[¶](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.GetMappingNames "Link to this definition")  
Returns a list of all available mappings for the chosen scope of the current package.

Info

This function is not supported in parallel packages.

Parameters:  scope : str[¶](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.GetMappingNames.scope "Permalink to this definition")  
The scope of the mapping space to look in. Possible values are

- **exec**: The execution mapping space of the current package.

- **project**: The project mapping space, i.e., mappings defined in parameter sets or project folders.

- **global**: The global mapping space, i.e., mappings defined via a test configuration or a currently loaded .xam file.

- **all**: All combined mapping spaces.

Returns:  Mapping names of the chosen scope.

Return type:  list[str]

Raise:  
TTError if the scope is ‘project’ but there is no project running.

GetMappingTargetPath(*[mappingName](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.GetMappingTargetPath.mappingName "tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.GetMappingTargetPath.mappingName (Python parameter) — Name of the mapping.")*, *[scope](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.GetMappingTargetPath.scope "tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.GetMappingTargetPath.scope (Python parameter) — The scope of the mapping space to look in.")=`'exec'`*)[¶](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.GetMappingTargetPath "Link to this definition")  
Returns the target path of the mapping with the given name depending on the chosen scope.

Info

This function is not supported in parallel packages.

Parameters:  mappingName : str[¶](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.GetMappingTargetPath.mappingName "Permalink to this definition")  
Name of the mapping.

scope : str[¶](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.GetMappingTargetPath.scope "Permalink to this definition")  
The scope of the mapping space to look in. Possible values are

- **exec**: The execution mapping space of the current package.

- **project**: The project mapping space, i.e., mappings defined in parameter sets or project folders.

- **global**: The global mapping space, i.e., mappings defined via a test configuration or a currently loaded .xam file.

- **all**: All combined mapping spaces. Returns always the target path of that mapping that has the highest priority throughout all scopes.

Returns:  - The target path for the given mapping name of the chosen scope.

- None if it is a generic mapping.

Raise:  
TTError if

- the scope is ‘project’ but there is no project running.

- there is no mapping of the given name in the scope.

Return type:  str | None

GetWatchTime(*[key](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.GetWatchTime "tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.GetWatchTime.key (Python parameter)")=`'DefaultWatch'`*)[¶](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.GetWatchTime "Link to this definition")  
Returns the difference between the current time and the start of a watch

Returns:  The time difference [ms]

Return type:  int

IsAbortRequested()[¶](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.IsAbortRequested "Link to this definition")  
Returns True if the user has requested an abort.

Info

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

StartWatch(*[key](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.StartWatch.key "tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.StartWatch.key (Python parameter) — The indentifier of the watch")=`'DefaultWatch'`*)[¶](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.StartWatch "Link to this definition")  
Start a watch or reset an existing watch

Parameters:  key : str[¶](#tts.core.api.internalApi.TestExecutionInfo.TestExecutionInfo.StartWatch.key "Permalink to this definition")  
The indentifier of the watch

### TestManagement[¶](#module-tts.core.api.internalApi.TestManagement "Link to this heading")

*class* TestManagementApi[¶](#tts.core.api.internalApi.TestManagement.TestManagementApi "Link to this definition")  
API to interact with the configured test management system.

Info

Test management must be configured and already successfully authenticated.

GetTestScriptByID(*[testScriptId](#tts.core.api.internalApi.TestManagement.TestManagementApi.GetTestScriptByID.testScriptId "tts.core.api.internalApi.TestManagement.TestManagementApi.GetTestScriptByID.testScriptId (Python parameter) — String value of the identifer, e.g.: "42" or "TT-1234"")*)[¶](#tts.core.api.internalApi.TestManagement.TestManagementApi.GetTestScriptByID "Link to this definition")  
Queries a test script by its ID. The returned data object corresponds to the interface of almhooks.

Parameters:  testScriptId : str[¶](#tts.core.api.internalApi.TestManagement.TestManagementApi.GetTestScriptByID.testScriptId "Permalink to this definition")  
String value of the identifer, e.g.: “42” or “TT-1234”

Returns:  Data object of the Almhook Interface representing a test script.

Raises:  
**exception** – if a user adapter is currently active. Or the test management system is not configured. Or the user is not authenticated.

Return type:  TestScript

### ToolAccess[¶](#toolaccess "Link to this heading")

*class* JobExecutor[¶](#tts.core.api.internalApi.ToolAccess.JobExecutor "Link to this definition")  
Object for executing jobs on tools or ports.

Execute(*\*\*[params](#tts.core.api.internalApi.ToolAccess.JobExecutor.Execute.params "tts.core.api.internalApi.ToolAccess.JobExecutor.Execute.params (Python parameter) — The parameters as keyword arguments.")*)[¶](#tts.core.api.internalApi.ToolAccess.JobExecutor.Execute "Link to this definition")  
Executes the job with the provided parameters.

Parameters:  \*\*params[¶](#tts.core.api.internalApi.ToolAccess.JobExecutor.Execute.params "Permalink to this definition")  
The parameters as keyword arguments.

*class* ToolAccess[¶](#tts.core.api.internalApi.ToolAccess.ToolAccess "Link to this definition")  
Entry point for executing jobs on tools or ports.

GetPortJobExecutor(*[portId](#tts.core.api.internalApi.ToolAccess.ToolAccess.GetPortJobExecutor.portId "tts.core.api.internalApi.ToolAccess.ToolAccess.GetPortJobExecutor.portId (Python parameter) — The ID of the port.")*, *[jobName](#tts.core.api.internalApi.ToolAccess.ToolAccess.GetPortJobExecutor.jobName "tts.core.api.internalApi.ToolAccess.ToolAccess.GetPortJobExecutor.jobName (Python parameter) — The name of the job to run.")*)[¶](#tts.core.api.internalApi.ToolAccess.ToolAccess.GetPortJobExecutor "Link to this definition")  
Get a JobExecutor for a specific port and job name.

Parameters:  portId : str[¶](#tts.core.api.internalApi.ToolAccess.ToolAccess.GetPortJobExecutor.portId "Permalink to this definition")  
The ID of the port.

jobName : str[¶](#tts.core.api.internalApi.ToolAccess.ToolAccess.GetPortJobExecutor.jobName "Permalink to this definition")  
The name of the job to run.

Returns:  A JobExecutor instance for the specified port and job.

Return type:  [`JobExecutor`](#tts.core.api.internalApi.ToolAccess.JobExecutor "tts.core.api.internalApi.ToolAccess.JobExecutor (Python class) — Object for executing jobs on tools or ports.")

GetToolJobExecutor(*[toolId](#tts.core.api.internalApi.ToolAccess.ToolAccess.GetToolJobExecutor.toolId "tts.core.api.internalApi.ToolAccess.ToolAccess.GetToolJobExecutor.toolId (Python parameter) — The ID of the tool.")*, *[jobName](#tts.core.api.internalApi.ToolAccess.ToolAccess.GetToolJobExecutor.jobName "tts.core.api.internalApi.ToolAccess.ToolAccess.GetToolJobExecutor.jobName (Python parameter) — The name of the job to run.")*)[¶](#tts.core.api.internalApi.ToolAccess.ToolAccess.GetToolJobExecutor "Link to this definition")  
Get a JobExecutor for a specific tool and job name.

Parameters:  toolId : str[¶](#tts.core.api.internalApi.ToolAccess.ToolAccess.GetToolJobExecutor.toolId "Permalink to this definition")  
The ID of the tool.

jobName : str[¶](#tts.core.api.internalApi.ToolAccess.ToolAccess.GetToolJobExecutor.jobName "Permalink to this definition")  
The name of the job to run.

Returns:  A JobExecutor instance for the specified tool and job.

Return type:  [`JobExecutor`](#tts.core.api.internalApi.ToolAccess.JobExecutor "tts.core.api.internalApi.ToolAccess.JobExecutor (Python class) — Object for executing jobs on tools or ports.")

### Workspace[¶](#workspace "Link to this heading")

*class* Finding[¶](#tts.core.api.internalApi.Workspace.Finding "Link to this definition")  
Represents a finding returned by method [`Workspace.Check()`](#tts.core.api.internalApi.Workspace.Workspace.Check "tts.core.api.internalApi.Workspace.Workspace.Check (Python method) — Checks an item and returns a list of findings.").

Variables:  
message  
a message describing the finding

severity  
a severity (note, warning, error, exception)

filepath  
optionally, a file path if the finding occurred in an artifact

lineno  
optionally, a line number in the artifact where the finding occurred

id  
optionally, an ID to identify the exact source of the finding

*class* Workspace[¶](#tts.core.api.internalApi.Workspace.Workspace "Link to this definition")  
Access to workspace related information.

Check(*[item](#tts.core.api.internalApi.Workspace.Workspace.Check.item "tts.core.api.internalApi.Workspace.Workspace.Check.item (Python parameter) — The item to check. Supported are file paths to packages and analysis packages. The paths have to be absolute or relative to the "packages" directory.")*, *[recursive](#tts.core.api.internalApi.Workspace.Workspace.Check.recursive "tts.core.api.internalApi.Workspace.Workspace.Check.recursive (Python parameter) — If True, referenced items (that are supported) are also checked. If False, only the item itself is checked. If None, the default behavior as set in the workspace settings is used.")=`None`*)[¶](#tts.core.api.internalApi.Workspace.Workspace.Check "Link to this definition")  
Checks an item and returns a list of findings.

Parameters:  item : str | Path[¶](#tts.core.api.internalApi.Workspace.Workspace.Check.item "Permalink to this definition")  
The item to check. Supported are file paths to packages and analysis packages. The paths have to be absolute or relative to the “packages” directory.

recursive : bool | None[¶](#tts.core.api.internalApi.Workspace.Workspace.Check.recursive "Permalink to this definition")  
If True, referenced items (that are supported) are also checked. If False, only the item itself is checked. If None, the default behavior as set in the workspace settings is used.

Returns:  a list of findings

Return type:  list[[*Finding*](#tts.core.api.internalApi.Workspace.Finding "tts.core.api.internalApi.Workspace.Finding (Python class) — Represents a finding returned by method Workspace.Check().")]

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

Currently, the central vault is a password encrypted file containing the access data to the different keystores. One can simply create a vault by CreateCryptFileVault or load an existing one by OpenCryptFileVault.

#### Security[¶](#security "Link to this heading")

See security notes for the vault in the workspace settings documentation.

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

Return type:  [`Certificate`](#tts.core.api.internalApi.credentialsApi.Certificate.Certificate "tts.core.api.internalApi.credentialsApi.Certificate.Certificate (Python class) — Returns the certificate as base64 encoded string.")

ChangeLoginCredentials(*[old](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials.ChangeLoginCredentials.old "tts.core.api.internalApi.credentialsApi.Credentials.Credentials.ChangeLoginCredentials.old (Python parameter) — Old vault password.")*, *[new](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials.ChangeLoginCredentials.new "tts.core.api.internalApi.credentialsApi.Credentials.Credentials.ChangeLoginCredentials.new (Python parameter) — New vault password.")*)[¶](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials.ChangeLoginCredentials "Link to this definition")  
Changes the login credentials (vault password).

Parameters:  old : str[¶](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials.ChangeLoginCredentials.old "Permalink to this definition")  
Old vault password.

new : str[¶](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials.ChangeLoginCredentials.new "Permalink to this definition")  
New vault password.

Close()[¶](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials.Close "Link to this definition")  
Closes the vault. Unsaved modifications will be discarded!

CreateCryptFileVault(*[path](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials.CreateCryptFileVault.path "tts.core.api.internalApi.credentialsApi.Credentials.Credentials.CreateCryptFileVault.path (Python parameter) — The path of the vault.")*, *[vaultPassword](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials.CreateCryptFileVault.vaultPassword "tts.core.api.internalApi.credentialsApi.Credentials.Credentials.CreateCryptFileVault.vaultPassword (Python parameter) — The password of the vault.")*)[¶](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials.CreateCryptFileVault "Link to this definition")  
Creates a new crypt file vault. After that the new vault will be open.

Parameters:  path : str[¶](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials.CreateCryptFileVault.path "Permalink to this definition")  
The path of the vault. This path can be relative to the workspace or absolute.

vaultPassword : str[¶](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials.CreateCryptFileVault.vaultPassword "Permalink to this definition")  
The password of the vault.

CreatePkcs12KeyStore(*[identifier](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials.CreatePkcs12KeyStore.identifier "tts.core.api.internalApi.credentialsApi.Credentials.Credentials.CreatePkcs12KeyStore.identifier (Python parameter) — This identifier will be used to reference the created keystore. The identifier has to be a valid python variable name without leading underscores.")*, *[filePath](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials.CreatePkcs12KeyStore.filePath "tts.core.api.internalApi.credentialsApi.Credentials.Credentials.CreatePkcs12KeyStore.filePath (Python parameter) — The path of the PKCS12 file to be created.")*, *[privateKey](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials.CreatePkcs12KeyStore.privateKey "tts.core.api.internalApi.credentialsApi.Credentials.Credentials.CreatePkcs12KeyStore.privateKey (Python parameter) — Path to the private key that will be stored in the PKCS12 file.")=`None`*, *[certs](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials.CreatePkcs12KeyStore.certs "tts.core.api.internalApi.credentialsApi.Credentials.Credentials.CreatePkcs12KeyStore.certs (Python parameter) — Certificates that will be stored in the PKCS12 file.")=`None`*, *[password](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials.CreatePkcs12KeyStore.password "tts.core.api.internalApi.credentialsApi.Credentials.Credentials.CreatePkcs12KeyStore.password (Python parameter) — Password for accessing the PKCS12 file.")=`''`*)[¶](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials.CreatePkcs12KeyStore "Link to this definition")  
Creates the PKCS12 file with its given path, private key, certificates and password. The created PKC12 file is stored afterward.

Parameters:  identifier : str[¶](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials.CreatePkcs12KeyStore.identifier "Permalink to this definition")  
This identifier will be used to reference the created keystore. The identifier has to be a valid python variable name without leading underscores.

filePath : str[¶](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials.CreatePkcs12KeyStore.filePath "Permalink to this definition")  
The path of the PKCS12 file to be created.

privateKey : str | None[¶](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials.CreatePkcs12KeyStore.privateKey "Permalink to this definition")  
Path to the private key that will be stored in the PKCS12 file. If not given, the PKCS12 file will be created without a private key.

certs : list[str] | None[¶](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials.CreatePkcs12KeyStore.certs "Permalink to this definition")  
Certificates that will be stored in the PKCS12 file. The certificates can be given as files paths or standard base64 encoded strings. Additionally, they have to be ordered as certificate chain. If not given, the PKCS12 file will be created without certificates.

password : str[¶](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials.CreatePkcs12KeyStore.password "Permalink to this definition")  
Password for accessing the PKCS12 file. If the PKCS12 file shall not be password protected, just choose an empty password.

Return type:  [`KeyStore`](#tts.core.api.internalApi.credentialsApi.KeyStore.KeyStore "tts.core.api.internalApi.credentialsApi.KeyStore.KeyStore (Python class) — Keystore for saving credentials.")

CreateSecret(*[identifier](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials.CreateSecret.identifier "tts.core.api.internalApi.credentialsApi.Credentials.Credentials.CreateSecret.identifier (Python parameter) — This identifier will be used to reference the created keystore. The identifier has to be a valid python variable name without leading underscores.")*, *[secret](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials.CreateSecret.secret "tts.core.api.internalApi.credentialsApi.Credentials.Credentials.CreateSecret.secret (Python parameter) — The secret to be stored, e.g.")*, *[associatedData](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials.CreateSecret.associatedData "tts.core.api.internalApi.credentialsApi.Credentials.Credentials.CreateSecret.associatedData (Python parameter) — Additional data associated with the secret.")=`None`*)[¶](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials.CreateSecret "Link to this definition")  
Creates and saves the secret with its associated data.

Parameters:  identifier : str[¶](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials.CreateSecret.identifier "Permalink to this definition")  
This identifier will be used to reference the created keystore. The identifier has to be a valid python variable name without leading underscores.

secret : str[¶](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials.CreateSecret.secret "Permalink to this definition")  
The secret to be stored, e.g. passwords, tokens.

associatedData : Any[¶](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials.CreateSecret.associatedData "Permalink to this definition")  
Additional data associated with the secret. Data has to be JSON serializable.

Return type:  [`Secret`](#tts.core.api.internalApi.credentialsApi.Secret.Secret "tts.core.api.internalApi.credentialsApi.Secret.Secret (Python class) — Additional data associated with the secret.")

DeleteVaultEntry(*[identifier](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials.DeleteVaultEntry "tts.core.api.internalApi.credentialsApi.Credentials.Credentials.DeleteVaultEntry.identifier (Python parameter)")*)[¶](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials.DeleteVaultEntry "Link to this definition")  
Deletes the vault entry with the given identifier.

GetAvailableVaultEntries()[¶](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials.GetAvailableVaultEntries "Link to this definition")  
Returns all available vault entry identifiers.

Return type:  list[str]

GetTesterKey(*[vaultPassword](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials.GetTesterKey.vaultPassword "tts.core.api.internalApi.credentialsApi.Credentials.Credentials.GetTesterKey.vaultPassword (Python parameter) — The password of the vault.")*)[¶](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials.GetTesterKey "Link to this definition")  
Returns the tester key.

Parameters:  vaultPassword : str[¶](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials.GetTesterKey.vaultPassword "Permalink to this definition")  
The password of the vault.

GetVaultEntry(*[identifier](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials.GetVaultEntry "tts.core.api.internalApi.credentialsApi.Credentials.Credentials.GetVaultEntry.identifier (Python parameter)")*)[¶](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials.GetVaultEntry "Link to this definition")  
Returns the vault entry with the given identifier.

Returns:  Returns vault entry if existent, otherwise None

Return type:  [*KeyStore*](#tts.core.api.internalApi.credentialsApi.KeyStore.KeyStore "tts.core.api.internalApi.credentialsApi.KeyStore.KeyStore (Python class) — Keystore for saving credentials.") | [*Secret*](#tts.core.api.internalApi.credentialsApi.Secret.Secret "tts.core.api.internalApi.credentialsApi.Secret.Secret (Python class) — Additional data associated with the secret.") | None

LoadPkcs12KeyStore(*[identifier](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials.LoadPkcs12KeyStore.identifier "tts.core.api.internalApi.credentialsApi.Credentials.Credentials.LoadPkcs12KeyStore.identifier (Python parameter) — This identifier will be used to reference the created keystore. The identifier has to be a valid python variable name without leading underscores.")*, *[filePath](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials.LoadPkcs12KeyStore.filePath "tts.core.api.internalApi.credentialsApi.Credentials.Credentials.LoadPkcs12KeyStore.filePath (Python parameter) — The path of the PKCS12 file.")*, *[password](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials.LoadPkcs12KeyStore.password "tts.core.api.internalApi.credentialsApi.Credentials.Credentials.LoadPkcs12KeyStore.password (Python parameter) — Password for accessing the PKCS12 file.")=`''`*)[¶](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials.LoadPkcs12KeyStore "Link to this definition")  
Loads and stores an existing PKCS12 file given by its path and password.

Parameters:  identifier : str[¶](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials.LoadPkcs12KeyStore.identifier "Permalink to this definition")  
This identifier will be used to reference the created keystore. The identifier has to be a valid python variable name without leading underscores.

filePath : str[¶](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials.LoadPkcs12KeyStore.filePath "Permalink to this definition")  
The path of the PKCS12 file.

password : str[¶](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials.LoadPkcs12KeyStore.password "Permalink to this definition")  
Password for accessing the PKCS12 file. If the PKCS12 file is not password protected, just choose an empty password.

Return type:  [`KeyStore`](#tts.core.api.internalApi.credentialsApi.KeyStore.KeyStore "tts.core.api.internalApi.credentialsApi.KeyStore.KeyStore (Python class) — Keystore for saving credentials.")

OpenCryptFileVault(*[path](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials.OpenCryptFileVault.path "tts.core.api.internalApi.credentialsApi.Credentials.Credentials.OpenCryptFileVault.path (Python parameter) — The path of the vault.")*, *[vaultPassword](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials.OpenCryptFileVault.vaultPassword "tts.core.api.internalApi.credentialsApi.Credentials.Credentials.OpenCryptFileVault.vaultPassword (Python parameter) — The password or tester key of the vault.")*)[¶](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials.OpenCryptFileVault "Link to this definition")  
Opens the crypt file vault. The vault can only be modified if it has been opened.

Access via password allocates for a short time ca. 2 GB RAM.

Parameters:  path : str[¶](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials.OpenCryptFileVault.path "Permalink to this definition")  
The path of the vault. This path can be relative to the workspace or absolute.

vaultPassword : str[¶](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials.OpenCryptFileVault.vaultPassword "Permalink to this definition")  
The password or tester key of the vault.

OpenVault(*[vaultPassword](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials.OpenVault.vaultPassword "tts.core.api.internalApi.credentialsApi.Credentials.Credentials.OpenVault.vaultPassword (Python parameter) — The password or tester key of the vault.")*)[¶](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials.OpenVault "Link to this definition")  
Opens the vault that is configured in credential settings. The vault can only be modified if it has been opened.

Access via password allocates for a short time ca. 2 GB RAM.

Parameters:  vaultPassword : str[¶](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials.OpenVault.vaultPassword "Permalink to this definition")  
The password or tester key of the vault.

PrivateKey[¶](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials.PrivateKey "Link to this definition")  
Returns PrivateKey API for utility methods.

Return type:  [`PrivateKey`](#tts.core.api.internalApi.credentialsApi.PrivateKey.PrivateKey "tts.core.api.internalApi.credentialsApi.PrivateKey.PrivateKey (Python class) — Create a PrivateKey instance from base64 encoded data.")

PublicKey[¶](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials.PublicKey "Link to this definition")  
Returns PublicKey API for utility methods.

Return type:  [`PublicKey`](#tts.core.api.internalApi.credentialsApi.PublicKey.PublicKey "tts.core.api.internalApi.credentialsApi.PublicKey.PublicKey (Python class) — Returns the public key as base64 encoded string.")

Save()[¶](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials.Save "Link to this definition")  
Saves all modifications.

SeedAndKey[¶](#tts.core.api.internalApi.credentialsApi.Credentials.Credentials.SeedAndKey "Link to this definition")  
Returns SeedAndKey API for generating keys from seeds.

Return type:  [`SeedAndKey`](#tts.core.api.internalApi.credentialsApi.SeedAndKey.SeedAndKey "tts.core.api.internalApi.credentialsApi.SeedAndKey.SeedAndKey (Python class) — Diagnostics related seed and key API")

### KeyStore[¶](#keystore "Link to this heading")

*class* KeyStore[¶](#tts.core.api.internalApi.credentialsApi.KeyStore.KeyStore "Link to this definition")  
Keystore for saving credentials.

Delete()[¶](#tts.core.api.internalApi.credentialsApi.KeyStore.KeyStore.Delete "Link to this definition")  
Deletes the vault entry.

GetCertificate(*[name](#tts.core.api.internalApi.credentialsApi.KeyStore.KeyStore.GetCertificate.name "tts.core.api.internalApi.credentialsApi.KeyStore.KeyStore.GetCertificate.name (Python parameter) — The name of the certificate that will be used to identify it.")*)[¶](#tts.core.api.internalApi.credentialsApi.KeyStore.KeyStore.GetCertificate "Link to this definition")  
Returns the certificate with the given name. For PKCS12 files the common name of the certificate is used as identifier.

Parameters:  name : str[¶](#tts.core.api.internalApi.credentialsApi.KeyStore.KeyStore.GetCertificate.name "Permalink to this definition")  
The name of the certificate that will be used to identify it.

Return type:  [`Certificate`](#tts.core.api.internalApi.credentialsApi.Certificate.Certificate "tts.core.api.internalApi.credentialsApi.Certificate.Certificate (Python class) — Returns the certificate as base64 encoded string.")

GetCertificateChain(*[name](#tts.core.api.internalApi.credentialsApi.KeyStore.KeyStore.GetCertificateChain.name "tts.core.api.internalApi.credentialsApi.KeyStore.KeyStore.GetCertificateChain.name (Python parameter) — The name of the certificate that will be used to identify it.")*)[¶](#tts.core.api.internalApi.credentialsApi.KeyStore.KeyStore.GetCertificateChain "Link to this definition")  
Returns the certificate chain for the certificate with the given name. For PKCS12 files the common name of the certificate is used as identifier.

Parameters:  name : str[¶](#tts.core.api.internalApi.credentialsApi.KeyStore.KeyStore.GetCertificateChain.name "Permalink to this definition")  
The name of the certificate that will be used to identify it.

Return type:  list[[`Certificate`](#tts.core.api.internalApi.credentialsApi.Certificate.Certificate "tts.core.api.internalApi.credentialsApi.Certificate.Certificate (Python class) — Returns the certificate as base64 encoded string.")]

GetCertificates()[¶](#tts.core.api.internalApi.credentialsApi.KeyStore.KeyStore.GetCertificates "Link to this definition")  
Returns all stored certificates.

Return type:  list[[`Certificate`](#tts.core.api.internalApi.credentialsApi.Certificate.Certificate "tts.core.api.internalApi.credentialsApi.Certificate.Certificate (Python class) — Returns the certificate as base64 encoded string.")]

GetPrivateKey()[¶](#tts.core.api.internalApi.credentialsApi.KeyStore.KeyStore.GetPrivateKey "Link to this definition")  
Returns the private key.

Return type:  [`PrivateKey`](#tts.core.api.internalApi.credentialsApi.PrivateKey.PrivateKey "tts.core.api.internalApi.credentialsApi.PrivateKey.PrivateKey (Python class) — Create a PrivateKey instance from base64 encoded data.") | None

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

Base64()[¶](#tts.core.api.internalApi.credentialsApi.Certificate.Certificate.Base64 "Link to this definition")  
Returns the certificate as base64 encoded string.

Return type:  str

CommonName()[¶](#tts.core.api.internalApi.credentialsApi.Certificate.Certificate.CommonName "Link to this definition")  
Return the common name of this certificate.

Return type:  str

DER()[¶](#tts.core.api.internalApi.credentialsApi.Certificate.Certificate.DER "Link to this definition")  
Return the certificate as bytes in DER format.

Return type:  [`ByteStream`](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream (Python class) — The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.")

*classmethod* FromBase64(*[data](#tts.core.api.internalApi.credentialsApi.Certificate.Certificate.FromBase64.data "tts.core.api.internalApi.credentialsApi.Certificate.Certificate.FromBase64.data (Python parameter) — Base64 encoded data")*)[¶](#tts.core.api.internalApi.credentialsApi.Certificate.Certificate.FromBase64 "Link to this definition")  
Create a Certificate instance from base64 encoded data.

Parameters:  data : str[¶](#tts.core.api.internalApi.credentialsApi.Certificate.Certificate.FromBase64.data "Permalink to this definition")  
Base64 encoded data

Return type:  [`Certificate`](#tts.core.api.internalApi.credentialsApi.Certificate.Certificate "tts.core.api.internalApi.credentialsApi.Certificate.Certificate (Python class) — Returns the certificate as base64 encoded string.")

*classmethod* FromDER(*[data](#tts.core.api.internalApi.credentialsApi.Certificate.Certificate.FromDER.data "tts.core.api.internalApi.credentialsApi.Certificate.Certificate.FromDER.data (Python parameter) — DER encoded data")*)[¶](#tts.core.api.internalApi.credentialsApi.Certificate.Certificate.FromDER "Link to this definition")  
Create a Certificate instance from DER encoded data.

Parameters:  data : [ByteStream](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream (Python class) — The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.")[¶](#tts.core.api.internalApi.credentialsApi.Certificate.Certificate.FromDER.data "Permalink to this definition")  
DER encoded data

Return type:  [`Certificate`](#tts.core.api.internalApi.credentialsApi.Certificate.Certificate "tts.core.api.internalApi.credentialsApi.Certificate.Certificate (Python class) — Returns the certificate as base64 encoded string.")

*classmethod* FromFile(*[filePath](#tts.core.api.internalApi.credentialsApi.Certificate.Certificate.FromFile.filePath "tts.core.api.internalApi.credentialsApi.Certificate.Certificate.FromFile.filePath (Python parameter) — Path of certificate file.")*)[¶](#tts.core.api.internalApi.credentialsApi.Certificate.Certificate.FromFile "Link to this definition")  
Creates a Certificate instance from a PEM or DER formatted file.

Parameters:  filePath : str[¶](#tts.core.api.internalApi.credentialsApi.Certificate.Certificate.FromFile.filePath "Permalink to this definition")  
Path of certificate file.

Return type:  [`Certificate`](#tts.core.api.internalApi.credentialsApi.Certificate.Certificate "tts.core.api.internalApi.credentialsApi.Certificate.Certificate (Python class) — Returns the certificate as base64 encoded string.")

*classmethod* FromPEM(*[data](#tts.core.api.internalApi.credentialsApi.Certificate.Certificate.FromPEM.data "tts.core.api.internalApi.credentialsApi.Certificate.Certificate.FromPEM.data (Python parameter) — PEM encoded data")*)[¶](#tts.core.api.internalApi.credentialsApi.Certificate.Certificate.FromPEM "Link to this definition")  
Create a Certificate instance from PEM encoded data.

Parameters:  data : str[¶](#tts.core.api.internalApi.credentialsApi.Certificate.Certificate.FromPEM.data "Permalink to this definition")  
PEM encoded data

Return type:  [`Certificate`](#tts.core.api.internalApi.credentialsApi.Certificate.Certificate "tts.core.api.internalApi.credentialsApi.Certificate.Certificate (Python class) — Returns the certificate as base64 encoded string.")

IsValid(*[hours](#tts.core.api.internalApi.credentialsApi.Certificate.Certificate.IsValid.hours "tts.core.api.internalApi.credentialsApi.Certificate.Certificate.IsValid.hours (Python parameter) — The minimum number of hours for which the certificate must still be valid.")=`0`*)[¶](#tts.core.api.internalApi.credentialsApi.Certificate.Certificate.IsValid "Link to this definition")  
Checks if the certificate is still valid for at least the given amount of time.

Parameters:  hours : int[¶](#tts.core.api.internalApi.credentialsApi.Certificate.Certificate.IsValid.hours "Permalink to this definition")  
The minimum number of hours for which the certificate must still be valid.

Return type:  bool

Issuer()[¶](#tts.core.api.internalApi.credentialsApi.Certificate.Certificate.Issuer "Link to this definition")  
Return the issuer of this certificate.

Return type:  str

PEM()[¶](#tts.core.api.internalApi.credentialsApi.Certificate.Certificate.PEM "Link to this definition")  
Returns the certificate as PEM encoded string.

Return type:  str

PublicKey()[¶](#tts.core.api.internalApi.credentialsApi.Certificate.Certificate.PublicKey "Link to this definition")  
Return the certificate’s public key.

Return type:  [`PublicKey`](#tts.core.api.internalApi.credentialsApi.PublicKey.PublicKey "tts.core.api.internalApi.credentialsApi.PublicKey.PublicKey (Python class) — Returns the public key as base64 encoded string.")

Subject()[¶](#tts.core.api.internalApi.credentialsApi.Certificate.Certificate.Subject "Link to this definition")  
Return subject of this certificate.

Return type:  str

Verify(*[signature](#tts.core.api.internalApi.credentialsApi.Certificate.Certificate.Verify.signature "tts.core.api.internalApi.credentialsApi.Certificate.Certificate.Verify.signature (Python parameter) — The supposed signature of the message created by the corresponding private key.")*, *[message](#tts.core.api.internalApi.credentialsApi.Certificate.Certificate.Verify.message "tts.core.api.internalApi.credentialsApi.Certificate.Certificate.Verify.message (Python parameter) — The message that has been signed.")*)[¶](#tts.core.api.internalApi.credentialsApi.Certificate.Certificate.Verify "Link to this definition")  
Verifies a signature of the given message.

Parameters:  signature : [ByteStream](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream (Python class) — The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.")[¶](#tts.core.api.internalApi.credentialsApi.Certificate.Certificate.Verify.signature "Permalink to this definition")  
The supposed signature of the message created by the corresponding private key.

message : [ByteStream](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream (Python class) — The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.")[¶](#tts.core.api.internalApi.credentialsApi.Certificate.Certificate.Verify.message "Permalink to this definition")  
The message that has been signed.

Returns:  True, if the verification is successful, otherwise False.

Return type:  bool

### PrivateKey[¶](#privatekey "Link to this heading")

*class* PrivateKey[¶](#tts.core.api.internalApi.credentialsApi.PrivateKey.PrivateKey "Link to this definition")  

*classmethod* FromBase64(*[data](#tts.core.api.internalApi.credentialsApi.PrivateKey.PrivateKey.FromBase64.data "tts.core.api.internalApi.credentialsApi.PrivateKey.PrivateKey.FromBase64.data (Python parameter) — Base64 encoded data")*)[¶](#tts.core.api.internalApi.credentialsApi.PrivateKey.PrivateKey.FromBase64 "Link to this definition")  
Create a PrivateKey instance from base64 encoded data.

Parameters:  data : str[¶](#tts.core.api.internalApi.credentialsApi.PrivateKey.PrivateKey.FromBase64.data "Permalink to this definition")  
Base64 encoded data

Return type:  [`PrivateKey`](#tts.core.api.internalApi.credentialsApi.PrivateKey.PrivateKey "tts.core.api.internalApi.credentialsApi.PrivateKey.PrivateKey (Python class) — Create a PrivateKey instance from base64 encoded data.")

*classmethod* FromDER(*[data](#tts.core.api.internalApi.credentialsApi.PrivateKey.PrivateKey.FromDER.data "tts.core.api.internalApi.credentialsApi.PrivateKey.PrivateKey.FromDER.data (Python parameter) — DER encoded data")*)[¶](#tts.core.api.internalApi.credentialsApi.PrivateKey.PrivateKey.FromDER "Link to this definition")  
Create a PrivateKey instance from DER encoded data.

Parameters:  data : [ByteStream](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream (Python class) — The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.")[¶](#tts.core.api.internalApi.credentialsApi.PrivateKey.PrivateKey.FromDER.data "Permalink to this definition")  
DER encoded data

Return type:  [`PrivateKey`](#tts.core.api.internalApi.credentialsApi.PrivateKey.PrivateKey "tts.core.api.internalApi.credentialsApi.PrivateKey.PrivateKey (Python class) — Create a PrivateKey instance from base64 encoded data.")

*classmethod* FromFile(*[filePath](#tts.core.api.internalApi.credentialsApi.PrivateKey.PrivateKey.FromFile.filePath "tts.core.api.internalApi.credentialsApi.PrivateKey.PrivateKey.FromFile.filePath (Python parameter) — Path of private key file.")*)[¶](#tts.core.api.internalApi.credentialsApi.PrivateKey.PrivateKey.FromFile "Link to this definition")  
Creates a PrivateKey instance from a PEM or DER formatted file.

Parameters:  filePath : str[¶](#tts.core.api.internalApi.credentialsApi.PrivateKey.PrivateKey.FromFile.filePath "Permalink to this definition")  
Path of private key file.

Return type:  [`PrivateKey`](#tts.core.api.internalApi.credentialsApi.PrivateKey.PrivateKey "tts.core.api.internalApi.credentialsApi.PrivateKey.PrivateKey (Python class) — Create a PrivateKey instance from base64 encoded data.")

*classmethod* FromPEM(*[data](#tts.core.api.internalApi.credentialsApi.PrivateKey.PrivateKey.FromPEM.data "tts.core.api.internalApi.credentialsApi.PrivateKey.PrivateKey.FromPEM.data (Python parameter) — PEM encoded data")*)[¶](#tts.core.api.internalApi.credentialsApi.PrivateKey.PrivateKey.FromPEM "Link to this definition")  
Create a PrivateKey instance from PEM encoded data.

Parameters:  data : str[¶](#tts.core.api.internalApi.credentialsApi.PrivateKey.PrivateKey.FromPEM.data "Permalink to this definition")  
PEM encoded data

Return type:  [`PrivateKey`](#tts.core.api.internalApi.credentialsApi.PrivateKey.PrivateKey "tts.core.api.internalApi.credentialsApi.PrivateKey.PrivateKey (Python class) — Create a PrivateKey instance from base64 encoded data.")

PublicKey()[¶](#tts.core.api.internalApi.credentialsApi.PrivateKey.PrivateKey.PublicKey "Link to this definition")  
Return the corresponding public key.

Return type:  [`PublicKey`](#tts.core.api.internalApi.credentialsApi.PublicKey.PublicKey "tts.core.api.internalApi.credentialsApi.PublicKey.PublicKey (Python class) — Returns the public key as base64 encoded string.")

Sign(*[message](#tts.core.api.internalApi.credentialsApi.PrivateKey.PrivateKey.Sign "tts.core.api.internalApi.credentialsApi.PrivateKey.PrivateKey.Sign.message (Python parameter)")*)[¶](#tts.core.api.internalApi.credentialsApi.PrivateKey.PrivateKey.Sign "Link to this definition")  
Signs the given message.

Return type:  [`ByteStream`](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream (Python class) — The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.")

### PublicKey[¶](#publickey "Link to this heading")

*class* PublicKey[¶](#tts.core.api.internalApi.credentialsApi.PublicKey.PublicKey "Link to this definition")  

Base64()[¶](#tts.core.api.internalApi.credentialsApi.PublicKey.PublicKey.Base64 "Link to this definition")  
Returns the public key as base64 encoded string.

Return type:  str

DER()[¶](#tts.core.api.internalApi.credentialsApi.PublicKey.PublicKey.DER "Link to this definition")  
Return the public key as bytes in DER format.

Return type:  [`ByteStream`](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream (Python class) — The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.")

*classmethod* FromBase64(*[data](#tts.core.api.internalApi.credentialsApi.PublicKey.PublicKey.FromBase64.data "tts.core.api.internalApi.credentialsApi.PublicKey.PublicKey.FromBase64.data (Python parameter) — Base64 encoded data")*)[¶](#tts.core.api.internalApi.credentialsApi.PublicKey.PublicKey.FromBase64 "Link to this definition")  
Create a PublicKey instance from base64 encoded data.

Parameters:  data : str[¶](#tts.core.api.internalApi.credentialsApi.PublicKey.PublicKey.FromBase64.data "Permalink to this definition")  
Base64 encoded data

Return type:  [`PublicKey`](#tts.core.api.internalApi.credentialsApi.PublicKey.PublicKey "tts.core.api.internalApi.credentialsApi.PublicKey.PublicKey (Python class) — Returns the public key as base64 encoded string.")

*classmethod* FromDER(*[data](#tts.core.api.internalApi.credentialsApi.PublicKey.PublicKey.FromDER.data "tts.core.api.internalApi.credentialsApi.PublicKey.PublicKey.FromDER.data (Python parameter) — DER encoded data")*)[¶](#tts.core.api.internalApi.credentialsApi.PublicKey.PublicKey.FromDER "Link to this definition")  
Create a PublicKey instance from DER encoded data.

Parameters:  data : [ByteStream](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream (Python class) — The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.")[¶](#tts.core.api.internalApi.credentialsApi.PublicKey.PublicKey.FromDER.data "Permalink to this definition")  
DER encoded data

Return type:  [`PublicKey`](#tts.core.api.internalApi.credentialsApi.PublicKey.PublicKey "tts.core.api.internalApi.credentialsApi.PublicKey.PublicKey (Python class) — Returns the public key as base64 encoded string.")

*classmethod* FromFile(*[filePath](#tts.core.api.internalApi.credentialsApi.PublicKey.PublicKey.FromFile.filePath "tts.core.api.internalApi.credentialsApi.PublicKey.PublicKey.FromFile.filePath (Python parameter) — Path of the public key file.")*)[¶](#tts.core.api.internalApi.credentialsApi.PublicKey.PublicKey.FromFile "Link to this definition")  
Creates a PublicKey instance from a PEM or DER formatted file.

Parameters:  filePath : str[¶](#tts.core.api.internalApi.credentialsApi.PublicKey.PublicKey.FromFile.filePath "Permalink to this definition")  
Path of the public key file.

Return type:  [`PublicKey`](#tts.core.api.internalApi.credentialsApi.PublicKey.PublicKey "tts.core.api.internalApi.credentialsApi.PublicKey.PublicKey (Python class) — Returns the public key as base64 encoded string.")

*classmethod* FromPEM(*[data](#tts.core.api.internalApi.credentialsApi.PublicKey.PublicKey.FromPEM.data "tts.core.api.internalApi.credentialsApi.PublicKey.PublicKey.FromPEM.data (Python parameter) — PEM encoded data")*)[¶](#tts.core.api.internalApi.credentialsApi.PublicKey.PublicKey.FromPEM "Link to this definition")  
Create a PublicKey instance from PEM encoded data.

Parameters:  data : str[¶](#tts.core.api.internalApi.credentialsApi.PublicKey.PublicKey.FromPEM.data "Permalink to this definition")  
PEM encoded data

Return type:  [`PublicKey`](#tts.core.api.internalApi.credentialsApi.PublicKey.PublicKey "tts.core.api.internalApi.credentialsApi.PublicKey.PublicKey (Python class) — Returns the public key as base64 encoded string.")

PEM()[¶](#tts.core.api.internalApi.credentialsApi.PublicKey.PublicKey.PEM "Link to this definition")  
Returns the public key as PEM encoded string.

Return type:  str

Verify(*[signature](#tts.core.api.internalApi.credentialsApi.PublicKey.PublicKey.Verify.signature "tts.core.api.internalApi.credentialsApi.PublicKey.PublicKey.Verify.signature (Python parameter) — The supposed signature of the message created by the corresponding private key.")*, *[message](#tts.core.api.internalApi.credentialsApi.PublicKey.PublicKey.Verify.message "tts.core.api.internalApi.credentialsApi.PublicKey.PublicKey.Verify.message (Python parameter) — The message that has been signed.")*)[¶](#tts.core.api.internalApi.credentialsApi.PublicKey.PublicKey.Verify "Link to this definition")  
Verifies a signature of the given message.

Parameters:  signature : [ByteStream](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream (Python class) — The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.")[¶](#tts.core.api.internalApi.credentialsApi.PublicKey.PublicKey.Verify.signature "Permalink to this definition")  
The supposed signature of the message created by the corresponding private key.

message : [ByteStream](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream (Python class) — The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.")[¶](#tts.core.api.internalApi.credentialsApi.PublicKey.PublicKey.Verify.message "Permalink to this definition")  
The message that has been signed.

Returns:  True, if the verification is successful, otherwise False.

Return type:  bool

### SeedAndKey[¶](#seedandkey "Link to this heading")

*class* SeedAndKey[¶](#tts.core.api.internalApi.credentialsApi.SeedAndKey.SeedAndKey "Link to this definition")  
Diag[¶](#tts.core.api.internalApi.credentialsApi.SeedAndKey.SeedAndKey.Diag "Link to this definition")  
Diagnostics related seed and key API

Return type:  [`DiagSeedAndKey`](#tts.core.api.internalApi.credentialsApi.SeedAndKey.DiagSeedAndKey "tts.core.api.internalApi.credentialsApi.SeedAndKey.DiagSeedAndKey (Python class) — Returns DiagSeedAndKey instance for accessing libPath seed and key API.")

Xcp[¶](#tts.core.api.internalApi.credentialsApi.SeedAndKey.SeedAndKey.Xcp "Link to this definition")  
XCP related seed and key API

Return type:  [`XcpSeedAndKey`](#tts.core.api.internalApi.credentialsApi.SeedAndKey.XcpSeedAndKey "tts.core.api.internalApi.credentialsApi.SeedAndKey.XcpSeedAndKey (Python class) — Compute key from seed by using the previously passed library.")

### DiagSeedAndKey[¶](#diagseedandkey "Link to this heading")

*class* DiagSeedAndKey[¶](#tts.core.api.internalApi.credentialsApi.SeedAndKey.DiagSeedAndKey "Link to this definition")  

*classmethod* FromLib(*[libPath](#tts.core.api.internalApi.credentialsApi.SeedAndKey.DiagSeedAndKey.FromLib.libPath "tts.core.api.internalApi.credentialsApi.SeedAndKey.DiagSeedAndKey.FromLib.libPath (Python parameter) — The path of the dll.")*)[¶](#tts.core.api.internalApi.credentialsApi.SeedAndKey.DiagSeedAndKey.FromLib "Link to this definition")  
Returns DiagSeedAndKey instance for accessing libPath seed and key API.

Parameters:  libPath : str[¶](#tts.core.api.internalApi.credentialsApi.SeedAndKey.DiagSeedAndKey.FromLib.libPath "Permalink to this definition")  
The path of the dll. This path can be relative to the workspace or absolute.

Return type:  [`DiagSeedAndKey`](#tts.core.api.internalApi.credentialsApi.SeedAndKey.DiagSeedAndKey "tts.core.api.internalApi.credentialsApi.SeedAndKey.DiagSeedAndKey (Python class) — Returns DiagSeedAndKey instance for accessing libPath seed and key API.")

GenerateKeyEx(*[seed](#tts.core.api.internalApi.credentialsApi.SeedAndKey.DiagSeedAndKey.GenerateKeyEx.seed "tts.core.api.internalApi.credentialsApi.SeedAndKey.DiagSeedAndKey.GenerateKeyEx.seed (Python parameter) — The seed queried by the ECU (as byte raw data)")*, *[securityLevel](#tts.core.api.internalApi.credentialsApi.SeedAndKey.DiagSeedAndKey.GenerateKeyEx.securityLevel "tts.core.api.internalApi.credentialsApi.SeedAndKey.DiagSeedAndKey.GenerateKeyEx.securityLevel (Python parameter) — The security level to be change to")*, *[ecuVariant](#tts.core.api.internalApi.credentialsApi.SeedAndKey.DiagSeedAndKey.GenerateKeyEx.ecuVariant "tts.core.api.internalApi.credentialsApi.SeedAndKey.DiagSeedAndKey.GenerateKeyEx.ecuVariant (Python parameter) — The ECU variant's qualifier")*)[¶](#tts.core.api.internalApi.credentialsApi.SeedAndKey.DiagSeedAndKey.GenerateKeyEx "Link to this definition")  
Generates the key from the seed by using the previously passed library. Internally the user defined functiuon GenerateKeyEx() is called.

Parameters:  seed : [ByteStream](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream (Python class) — The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.")[¶](#tts.core.api.internalApi.credentialsApi.SeedAndKey.DiagSeedAndKey.GenerateKeyEx.seed "Permalink to this definition")  
The seed queried by the ECU (as byte raw data)

securityLevel : int[¶](#tts.core.api.internalApi.credentialsApi.SeedAndKey.DiagSeedAndKey.GenerateKeyEx.securityLevel "Permalink to this definition")  
The security level to be change to

ecuVariant : str[¶](#tts.core.api.internalApi.credentialsApi.SeedAndKey.DiagSeedAndKey.GenerateKeyEx.ecuVariant "Permalink to this definition")  
The ECU variant’s qualifier

Return type:  [`ByteStream`](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream (Python class) — The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.")

GenerateKeyExOpt(*[seed](#tts.core.api.internalApi.credentialsApi.SeedAndKey.DiagSeedAndKey.GenerateKeyExOpt.seed "tts.core.api.internalApi.credentialsApi.SeedAndKey.DiagSeedAndKey.GenerateKeyExOpt.seed (Python parameter) — The seed queried by the ECU (as byte raw data)")*, *[securityLevel](#tts.core.api.internalApi.credentialsApi.SeedAndKey.DiagSeedAndKey.GenerateKeyExOpt.securityLevel "tts.core.api.internalApi.credentialsApi.SeedAndKey.DiagSeedAndKey.GenerateKeyExOpt.securityLevel (Python parameter) — The security level to be change to")*, *[ecuVariant](#tts.core.api.internalApi.credentialsApi.SeedAndKey.DiagSeedAndKey.GenerateKeyExOpt.ecuVariant "tts.core.api.internalApi.credentialsApi.SeedAndKey.DiagSeedAndKey.GenerateKeyExOpt.ecuVariant (Python parameter) — The ECU variant's qualifier")*, *[options](#tts.core.api.internalApi.credentialsApi.SeedAndKey.DiagSeedAndKey.GenerateKeyExOpt.options "tts.core.api.internalApi.credentialsApi.SeedAndKey.DiagSeedAndKey.GenerateKeyExOpt.options (Python parameter) — The option string (free text)")*)[¶](#tts.core.api.internalApi.credentialsApi.SeedAndKey.DiagSeedAndKey.GenerateKeyExOpt "Link to this definition")  
Generates the key from the seed by using the previously passed library. Internally the user defined functiuon GenerateKeyExOpt() is called.

Parameters:  seed : [ByteStream](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream (Python class) — The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.")[¶](#tts.core.api.internalApi.credentialsApi.SeedAndKey.DiagSeedAndKey.GenerateKeyExOpt.seed "Permalink to this definition")  
The seed queried by the ECU (as byte raw data)

securityLevel : int[¶](#tts.core.api.internalApi.credentialsApi.SeedAndKey.DiagSeedAndKey.GenerateKeyExOpt.securityLevel "Permalink to this definition")  
The security level to be change to

ecuVariant : str[¶](#tts.core.api.internalApi.credentialsApi.SeedAndKey.DiagSeedAndKey.GenerateKeyExOpt.ecuVariant "Permalink to this definition")  
The ECU variant’s qualifier

options : str[¶](#tts.core.api.internalApi.credentialsApi.SeedAndKey.DiagSeedAndKey.GenerateKeyExOpt.options "Permalink to this definition")  
The option string (free text)

Return type:  [`ByteStream`](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream (Python class) — The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.")

### XcpSeedAndKey[¶](#xcpseedandkey "Link to this heading")

*class* XcpSeedAndKey[¶](#tts.core.api.internalApi.credentialsApi.SeedAndKey.XcpSeedAndKey "Link to this definition")  

ComputeKeyFromSeed(*[seed](#tts.core.api.internalApi.credentialsApi.SeedAndKey.XcpSeedAndKey.ComputeKeyFromSeed.seed "tts.core.api.internalApi.credentialsApi.SeedAndKey.XcpSeedAndKey.ComputeKeyFromSeed.seed (Python parameter) — Given seed that will be used to compute the key")*, *[privilege](#tts.core.api.internalApi.credentialsApi.SeedAndKey.XcpSeedAndKey.ComputeKeyFromSeed.privilege "tts.core.api.internalApi.credentialsApi.SeedAndKey.XcpSeedAndKey.ComputeKeyFromSeed.privilege (Python parameter) — Given privilege")*)[¶](#tts.core.api.internalApi.credentialsApi.SeedAndKey.XcpSeedAndKey.ComputeKeyFromSeed "Link to this definition")  
Compute key from seed by using the previously passed library.

Parameters:  seed : [ByteStream](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream (Python class) — The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.")[¶](#tts.core.api.internalApi.credentialsApi.SeedAndKey.XcpSeedAndKey.ComputeKeyFromSeed.seed "Permalink to this definition")  
Given seed that will be used to compute the key

privilege : int[¶](#tts.core.api.internalApi.credentialsApi.SeedAndKey.XcpSeedAndKey.ComputeKeyFromSeed.privilege "Permalink to this definition")  
Given privilege

Return type:  [`ByteStream`](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream (Python class) — The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.")

*classmethod* FromLib(*[libPath](#tts.core.api.internalApi.credentialsApi.SeedAndKey.XcpSeedAndKey.FromLib.libPath "tts.core.api.internalApi.credentialsApi.SeedAndKey.XcpSeedAndKey.FromLib.libPath (Python parameter) — The path of the dll.")*)[¶](#tts.core.api.internalApi.credentialsApi.SeedAndKey.XcpSeedAndKey.FromLib "Link to this definition")  
Returns XcpSeedAndKey instance for accessing libPath seed and key API.

Parameters:  libPath : str[¶](#tts.core.api.internalApi.credentialsApi.SeedAndKey.XcpSeedAndKey.FromLib.libPath "Permalink to this definition")  
The path of the dll. This path can be relative to the workspace or absolute.

Return type:  [`XcpSeedAndKey`](#tts.core.api.internalApi.credentialsApi.SeedAndKey.XcpSeedAndKey "tts.core.api.internalApi.credentialsApi.SeedAndKey.XcpSeedAndKey (Python class) — Compute key from seed by using the previously passed library.")

GetAvailablePrivileges()[¶](#tts.core.api.internalApi.credentialsApi.SeedAndKey.XcpSeedAndKey.GetAvailablePrivileges "Link to this definition")  
Get privileges given by the seed and key dll.

Return type:  int

## DataBrowser[¶](#module-tts.core.api.dataBrowserApi.DataBrowser "Link to this heading")

### A2lBrowser[¶](#a2lbrowser "Link to this heading")

*class* A2lBrowser[¶](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser "Link to this definition")  
The A2lBrowser type provides an interface to a A2L database. It is possible to retrieve information for a single entry or to use a full text search to get a list of filtered entries. Every entity is represented by an instance of the type [`A2lEntity`](#tts.core.api.dataBrowserApi.DataBrowser.A2lEntity "tts.core.api.dataBrowserApi.DataBrowser.A2lEntity (Python class) — The A2lEntity type represents one entry in an A2L database").

CalcPhysToRaw(*[label](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.CalcPhysToRaw.label "tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.CalcPhysToRaw.label (Python parameter) — The A2L label to select the computation method from")*, *[physValue](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.CalcPhysToRaw.physValue "tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.CalcPhysToRaw.physValue (Python parameter) — The numeric value to be converted to its raw representation")*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.CalcPhysToRaw "Link to this definition")  
Returns the raw value of the provided physical value computed using the computation method defined for the provided label

Parameters:  label : str[¶](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.CalcPhysToRaw.label "Permalink to this definition")  
The A2L label to select the computation method from

physValue : float[¶](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.CalcPhysToRaw.physValue "Permalink to this definition")  
The numeric value to be converted to its raw representation

Returns:  raw value

Return type:  float

CalcRawToPhys(*[label](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.CalcRawToPhys.label "tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.CalcRawToPhys.label (Python parameter) — The A2L label to select the computation method from")*, *[rawValue](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.CalcRawToPhys.rawValue "tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.CalcRawToPhys.rawValue (Python parameter) — The numeric value to be converted to its physical representation")*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.CalcRawToPhys "Link to this definition")  
Returns the physical converted value of the provided raw value computed using the computation method defined for the provided label

Parameters:  label : str[¶](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.CalcRawToPhys.label "Permalink to this definition")  
The A2L label to select the computation method from

rawValue : float[¶](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.CalcRawToPhys.rawValue "Permalink to this definition")  
The numeric value to be converted to its physical representation

Returns:  physical converted value

Return type:  float

GetA2lEntity(*[label](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.GetA2lEntity.label "tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.GetA2lEntity.label (Python parameter) — The A2L label to retrieve an A2lEntity instance")*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.GetA2lEntity "Link to this definition")  
Returns an instance of A2lEntity representing the entity with the specified label

Parameters:  label : str[¶](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.GetA2lEntity.label "Permalink to this definition")  
The A2L label to retrieve an A2lEntity instance

Returns:  An A2lEntity instance if the A2L database contains an entry with the given name, otherwise None

Return type:  [`A2lEntity`](#tts.core.api.dataBrowserApi.DataBrowser.A2lEntity "tts.core.api.dataBrowserApi.DataBrowser.A2lEntity (Python class) — The A2lEntity type represents one entry in an A2L database") or None

GetAcquisitionRateNames()[¶](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.GetAcquisitionRateNames "Link to this definition")  
Returns a list containing all acquisition rate names defined in the A2L database.

Returns:  A list of all acquisition rate names

Return type:  list \<str\>

GetCodeCheckInformation()[¶](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.GetCodeCheckInformation "Link to this definition")  
Query Code Check information from the A2L file.

Returns:  Code Check information as a dict, having the keys “software_revision_address” (int), “software_revision” (str), “code_check_internal_address” (int), “code_check_external_address” (int), “code_check_length” (int) and “code_check_pattern_wp” (int). The values of the dict will be None if the Code Check information could not be parsed from the A2L file.

Return type:  dict

GetEpkInformation()[¶](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.GetEpkInformation "Link to this definition")  
Query information about the EPROM identifier (EPK) from the A2L file.

Returns:  EPK information as a dict, having the keys “address” (int) and “value” (str). The values of the dict will be None if the EPK information could not be parsed from the A2L file.

Return type:  dict

GetFunctionCharacteristics(*[name](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.GetFunctionCharacteristics.name "tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.GetFunctionCharacteristics.name (Python parameter) — The name of the function to return the characteristics of")*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.GetFunctionCharacteristics "Link to this definition")  
Returns the characteristics of the function with the given name

Parameters:  name : str[¶](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.GetFunctionCharacteristics.name "Permalink to this definition")  
The name of the function to return the characteristics of

Returns:  The characteristics of the function

Return type:  list \<str\>

GetFunctionInMeasurements(*[name](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.GetFunctionInMeasurements.name "tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.GetFunctionInMeasurements.name (Python parameter) — The name of the function to return the in measurementes of")*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.GetFunctionInMeasurements "Link to this definition")  
Returns the in measurements of the function with the given name

Parameters:  name : str[¶](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.GetFunctionInMeasurements.name "Permalink to this definition")  
The name of the function to return the in measurementes of

Returns:  The in measurements of the function

Return type:  list \<str\>

GetFunctionLocMeasurements(*[name](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.GetFunctionLocMeasurements.name "tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.GetFunctionLocMeasurements.name (Python parameter) — The name of the function to return the local measurementes of")*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.GetFunctionLocMeasurements "Link to this definition")  
Returns the local measurements of the function with the given name

Parameters:  name : str[¶](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.GetFunctionLocMeasurements.name "Permalink to this definition")  
The name of the function to return the local measurementes of

Returns:  The local measurements of the function

Return type:  list \<str\>

GetFunctionNames()[¶](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.GetFunctionNames "Link to this definition")  
Returns the names of all functions within the A2L

Returns:  The names of all functions

Return type:  list \<str\>

GetFunctionOutMeasurements(*[name](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.GetFunctionOutMeasurements.name "tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.GetFunctionOutMeasurements.name (Python parameter) — The name of the function to return the out measurements of")*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.GetFunctionOutMeasurements "Link to this definition")  
Returns the out measurements of the function with the given name

Parameters:  name : str[¶](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.GetFunctionOutMeasurements.name "Permalink to this definition")  
The name of the function to return the out measurements of

Returns:  The out measurements of the function

Return type:  list \<str\>

GetFunctionVersion(*[name](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.GetFunctionVersion.name "tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.GetFunctionVersion.name (Python parameter) — The name of the function to return the version of")*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.GetFunctionVersion "Link to this definition")  
Returns the version of the function with the given name

Parameters:  name : str[¶](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.GetFunctionVersion.name "Permalink to this definition")  
The name of the function to return the version of

Returns:  The version of the function

Return type:  str

GetLabelNameList(*[filter](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.GetLabelNameList.filter "tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.GetLabelNameList.filter (Python parameter) — The search string which is part of an A2L label")=`''`*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.GetLabelNameList "Link to this definition")  
Returns a list which contains names of labels whose matches the specified label search string

Parameters:  filter : str[¶](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.GetLabelNameList.filter "Permalink to this definition")  
The search string which is part of an A2L label

Returns:  A list of names if the A2L database containsentries with the given search string, otherwise an empty list

Return type:  list\<str\>

GetSubFunctionNames(*[name](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.GetSubFunctionNames.name "tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.GetSubFunctionNames.name (Python parameter) — The name of the function to get the sub functions of")*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.GetSubFunctionNames "Link to this definition")  
Returns the names of all sub functions within the function with the given name

Parameters:  name : str[¶](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.GetSubFunctionNames.name "Permalink to this definition")  
The name of the function to get the sub functions of

Returns:  The names of all sub functions

Return type:  list \<str\>

GetSystemConstantNameList()[¶](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.GetSystemConstantNameList "Link to this definition")  
Returns a list which contains names of system constants defined in the A2L

Returns:  A list of names

Return type:  list\<str\>

GetSystemConstantValue(*[constName](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.GetSystemConstantValue.constName "tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.GetSystemConstantValue.constName (Python parameter) — Name of system constant defined in A2L")*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.GetSystemConstantValue "Link to this definition")  
Returns the value of the given system constant

Parameters:  constName : str[¶](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.GetSystemConstantValue.constName "Permalink to this definition")  
Name of system constant defined in A2L

Returns:  Value of system constant or None if name was not found

Return type:  str or None

HasFunction(*[name](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.HasFunction.name "tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.HasFunction.name (Python parameter) — The name to check if it is an existing function")*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.HasFunction "Link to this definition")  
Checks if a function of the given name exists within the A2L file

Parameters:  name : str[¶](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.HasFunction.name "Permalink to this definition")  
The name to check if it is an existing function

Returns:  True if a function with the given name exist, otherwise False

Return type:  bool

HasSubFunctions(*[name](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.HasSubFunctions.name "tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.HasSubFunctions.name (Python parameter) — The name of the function to check for sub functions")*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.HasSubFunctions "Link to this definition")  
Checks if a function of the given name within the A2L file has sub functions

Parameters:  name : str[¶](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.HasSubFunctions.name "Permalink to this definition")  
The name of the function to check for sub functions

Returns:  True if the function of the given name has subfunctions, otherwise False

Return type:  bool

IsCharacteristic(*[label](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.IsCharacteristic.label "tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.IsCharacteristic.label (Python parameter) — The A2L label to check for a calibration variable")*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.IsCharacteristic "Link to this definition")  
Checks if the given label name is a calibration variable

Parameters:  label : str[¶](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.IsCharacteristic.label "Permalink to this definition")  
The A2L label to check for a calibration variable

Returns:  True if the given label is a calibration variable, otherwise False

Return type:  bool

IsMeasurement(*[label](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.IsMeasurement.label "tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.IsMeasurement.label (Python parameter) — The A2L label to check for a measurement variable")*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.IsMeasurement "Link to this definition")  
Checks if the given label name is a measurement variable

Parameters:  label : str[¶](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.IsMeasurement.label "Permalink to this definition")  
The A2L label to check for a measurement variable

Returns:  True if the given label is a measurement variable, otherwise False.

Return type:  bool

ReadDataFromHex(*[address](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.ReadDataFromHex.address "tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.ReadDataFromHex.address (Python parameter) — start address of the bytes to read")*, *[length](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.ReadDataFromHex.length "tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.ReadDataFromHex.length (Python parameter) — number of bytes to read")*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.ReadDataFromHex "Link to this definition")  
Reads the given number of bytes from the Hex file at the given address.

Parameters:  address : int[¶](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.ReadDataFromHex.address "Permalink to this definition")  
start address of the bytes to read

length : int[¶](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser.ReadDataFromHex.length "Permalink to this definition")  
number of bytes to read

Returns:  bytes at the given address - or a ByteStream filled with zeroes if the Hex file does not contain the specified range.

Return type:  [ByteStream](variabledatastructures.md#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream (Python class) — The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.")

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
The BusBrowser type provides an interface to a BUS database. It is possible to retrieve information for a single entry or to use a full text search to get a list of filtered entries. Every entity is represented by an instance of the type [`BusEntity`](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity "tts.core.api.dataBrowserApi.DataBrowser.BusEntity (Python class) — The BusEntity type represents one entry in a bus database").

Info

This part of the DataBrowser API was specifically created to support certain use cases. Don’t expect your use case to easily map onto this API!

GetFrameNamesByPDUName(*[pduName](#tts.core.api.dataBrowserApi.DataBrowser.BusBrowser.GetFrameNamesByPDUName.pduName "tts.core.api.dataBrowserApi.DataBrowser.BusBrowser.GetFrameNamesByPDUName.pduName (Python parameter) — The name of the PDU")*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.BusBrowser.GetFrameNamesByPDUName "Link to this definition")  
Returns a set of frame names the given PDU is bound to

Parameters:  pduName : str[¶](#tts.core.api.dataBrowserApi.DataBrowser.BusBrowser.GetFrameNamesByPDUName.pduName "Permalink to this definition")  
The name of the PDU

Returns:  The frame names

Return type:  set\<str\>

GetLinScheduleTables()[¶](#tts.core.api.dataBrowserApi.DataBrowser.BusBrowser.GetLinScheduleTables "Link to this definition")  
Returns the LIN schedule tables as a dictionary, mapping the schedule table name to a sequence of triples (isFrameName, command, frameTime)

Returns:  LIN schedule tables

Return type:  dict\<string, tuple\<bool, string, float\>\>

GetSDGsAndSDs()[¶](#tts.core.api.dataBrowserApi.DataBrowser.BusBrowser.GetSDGsAndSDs "Link to this definition")  
Returns a dictionary with all top level SDGs and their associated SDs.

Returns:  Dictionary with SDG names as keys and a list of their corresponding SDs as values (JSON).

Return type:  dict \<str, dict\<str, list\<str\>\>\>

ListFrames(*[filter](#tts.core.api.dataBrowserApi.DataBrowser.BusBrowser.ListFrames.filter "tts.core.api.dataBrowserApi.DataBrowser.BusBrowser.ListFrames.filter (Python parameter) — The search string which is part of a bus frame")=`''`*, *[useLongNames](#tts.core.api.dataBrowserApi.DataBrowser.BusBrowser.ListFrames.useLongNames "tts.core.api.dataBrowserApi.DataBrowser.BusBrowser.ListFrames.useLongNames (Python parameter) — If True search in LongNames else (default) in ShortNames")=`False`*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.BusBrowser.ListFrames "Link to this definition")  
Returns a list of BusEntity instances corresponding to frames whose name matches the specified search string

Parameters:  filter : str[¶](#tts.core.api.dataBrowserApi.DataBrowser.BusBrowser.ListFrames.filter "Permalink to this definition")  
The search string which is part of a bus frame

useLongNames : bool[¶](#tts.core.api.dataBrowserApi.DataBrowser.BusBrowser.ListFrames.useLongNames "Permalink to this definition")  
If True search in LongNames else (default) in ShortNames

Returns:  A list of BusEntity instances if the bus database contains entries with the given search string, otherwise an empty list

Return type:  list \<[`BusEntities`](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity "tts.core.api.dataBrowserApi.DataBrowser.BusEntity (Python class) — The BusEntity type represents one entry in a bus database")\>

ListPDUs(*[frameName](#tts.core.api.dataBrowserApi.DataBrowser.BusBrowser.ListPDUs.frameName "tts.core.api.dataBrowserApi.DataBrowser.BusBrowser.ListPDUs.frameName (Python parameter) — The exact short name of the frame in which to search for PDUs (optional)")=`None`*, *[filter](#tts.core.api.dataBrowserApi.DataBrowser.BusBrowser.ListPDUs.filter "tts.core.api.dataBrowserApi.DataBrowser.BusBrowser.ListPDUs.filter (Python parameter) — The search string which is part of a bus frame")=`''`*, *[useLongNames](#tts.core.api.dataBrowserApi.DataBrowser.BusBrowser.ListPDUs.useLongNames "tts.core.api.dataBrowserApi.DataBrowser.BusBrowser.ListPDUs.useLongNames (Python parameter) — If True search in LongNames else (default) in ShortNames")=`False`*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.BusBrowser.ListPDUs "Link to this definition")  
Returns a list of BusEntity instances corresponding to PDUs whose name matches the specified search string

Parameters:  frameName : str[¶](#tts.core.api.dataBrowserApi.DataBrowser.BusBrowser.ListPDUs.frameName "Permalink to this definition")  
The exact short name of the frame in which to search for PDUs (optional)

filter : str[¶](#tts.core.api.dataBrowserApi.DataBrowser.BusBrowser.ListPDUs.filter "Permalink to this definition")  
The search string which is part of a bus frame

useLongNames : bool[¶](#tts.core.api.dataBrowserApi.DataBrowser.BusBrowser.ListPDUs.useLongNames "Permalink to this definition")  
If True search in LongNames else (default) in ShortNames

Returns:  A list of BusEntity instances if the bus database contains entries with the given search string, otherwise an empty list

Return type:  list \<[`BusEntities`](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity "tts.core.api.dataBrowserApi.DataBrowser.BusEntity (Python class) — The BusEntity type represents one entry in a bus database")\>

ListSignals(*[frameName](#tts.core.api.dataBrowserApi.DataBrowser.BusBrowser.ListSignals.frameName "tts.core.api.dataBrowserApi.DataBrowser.BusBrowser.ListSignals.frameName (Python parameter) — The exact name of the frame in which to search for signals")*, *[filter](#tts.core.api.dataBrowserApi.DataBrowser.BusBrowser.ListSignals.filter "tts.core.api.dataBrowserApi.DataBrowser.BusBrowser.ListSignals.filter (Python parameter) — The search string which is part of a bus signal")=`''`*, *[useLongNames](#tts.core.api.dataBrowserApi.DataBrowser.BusBrowser.ListSignals.useLongNames "tts.core.api.dataBrowserApi.DataBrowser.BusBrowser.ListSignals.useLongNames (Python parameter) — If True search in LongNames else (default) in ShortNames")=`False`*, *[includePseudoSignals](#tts.core.api.dataBrowserApi.DataBrowser.BusBrowser.ListSignals.includePseudoSignals "tts.core.api.dataBrowserApi.DataBrowser.BusBrowser.ListSignals.includePseudoSignals (Python parameter) — If True additionally list pseudo signals like _pduUpdateBit (default=False)")=`False`*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.BusBrowser.ListSignals "Link to this definition")  
Returns a list of BusEntity instances corresponding to signals whose name matches the specified search string

Parameters:  frameName : str[¶](#tts.core.api.dataBrowserApi.DataBrowser.BusBrowser.ListSignals.frameName "Permalink to this definition")  
The exact name of the frame in which to search for signals

filter : str[¶](#tts.core.api.dataBrowserApi.DataBrowser.BusBrowser.ListSignals.filter "Permalink to this definition")  
The search string which is part of a bus signal

useLongNames : bool[¶](#tts.core.api.dataBrowserApi.DataBrowser.BusBrowser.ListSignals.useLongNames "Permalink to this definition")  
If True search in LongNames else (default) in ShortNames

includePseudoSignals : bool[¶](#tts.core.api.dataBrowserApi.DataBrowser.BusBrowser.ListSignals.includePseudoSignals "Permalink to this definition")  
If True additionally list pseudo signals like \_pduUpdateBit (default=False)

Returns:  A list of BusEntity instances if the bus database contains entries with the given search string, otherwise an empty list

Return type:  list \<[`BusEntities`](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity "tts.core.api.dataBrowserApi.DataBrowser.BusEntity (Python class) — The BusEntity type represents one entry in a bus database")\>

ListSignalsByPDU(*[pduName](#tts.core.api.dataBrowserApi.DataBrowser.BusBrowser.ListSignalsByPDU.pduName "tts.core.api.dataBrowserApi.DataBrowser.BusBrowser.ListSignalsByPDU.pduName (Python parameter) — The exact name of the PDU in which to search for signals")*, *[filter](#tts.core.api.dataBrowserApi.DataBrowser.BusBrowser.ListSignalsByPDU.filter "tts.core.api.dataBrowserApi.DataBrowser.BusBrowser.ListSignalsByPDU.filter (Python parameter) — The search string which is part of a bus signal")=`''`*, *[useLongNames](#tts.core.api.dataBrowserApi.DataBrowser.BusBrowser.ListSignalsByPDU.useLongNames "tts.core.api.dataBrowserApi.DataBrowser.BusBrowser.ListSignalsByPDU.useLongNames (Python parameter) — If True search in LongNames else (default) in ShortNames")=`False`*, *[includePseudoSignals](#tts.core.api.dataBrowserApi.DataBrowser.BusBrowser.ListSignalsByPDU.includePseudoSignals "tts.core.api.dataBrowserApi.DataBrowser.BusBrowser.ListSignalsByPDU.includePseudoSignals (Python parameter) — If True additionally list pseudo signals like _pduUpdateBit (default=False)")=`False`*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.BusBrowser.ListSignalsByPDU "Link to this definition")  
Returns a list of BusEntity instances corresponding to signals whose name matches the specified search string

Parameters:  pduName : str[¶](#tts.core.api.dataBrowserApi.DataBrowser.BusBrowser.ListSignalsByPDU.pduName "Permalink to this definition")  
The exact name of the PDU in which to search for signals

filter : str[¶](#tts.core.api.dataBrowserApi.DataBrowser.BusBrowser.ListSignalsByPDU.filter "Permalink to this definition")  
The search string which is part of a bus signal

useLongNames : bool[¶](#tts.core.api.dataBrowserApi.DataBrowser.BusBrowser.ListSignalsByPDU.useLongNames "Permalink to this definition")  
If True search in LongNames else (default) in ShortNames

includePseudoSignals : bool[¶](#tts.core.api.dataBrowserApi.DataBrowser.BusBrowser.ListSignalsByPDU.includePseudoSignals "Permalink to this definition")  
If True additionally list pseudo signals like \_pduUpdateBit (default=False)

Returns:  A list of BusEntity instances if the bus database contains entries with the given search string, otherwise an empty list

Return type:  list \<[`BusEntities`](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity "tts.core.api.dataBrowserApi.DataBrowser.BusEntity (Python class) — The BusEntity type represents one entry in a bus database")\>

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

Info

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

GetFrameType()[¶](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetFrameType "Link to this definition")  
Returns the frame type (DBC MsgType or ARXML CATEGORY) or None if this is not a frame.

Returns:  frame type

Return type:  str or None

GetId()[¶](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetId "Link to this definition")  
Returns the identifier of this bus entity

Info

This works only for BusEntities representing a bus frame.

Returns:  The identifier

Return type:  str

GetLinearCoeffs()[¶](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetLinearCoeffs "Link to this definition")  
Returns the coefficients of the linear function y = slope \* x + offset where the slope is also called physical resoution.

Returns:  (slope, offset)

Return type:  tuple(float / None, float / None) / None

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

Info

This works only for BusEntities representing a bus PDU or bus signal.

Returns:  The switch code if available

Return type:  str or None

GetName()[¶](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetName "Link to this definition")  
Returns the name (as used within ecu.test) of this bus entity

Returns:  The name

Return type:  str

GetOriginalName()[¶](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetOriginalName "Link to this definition")  
Returns the original name of this bus entity as specified in the bus database.

Info

This is different from [`GetName()`](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetName "tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetName (Python method) — Returns the name (as used within ecu.test) of this bus entity") in case ecu.test needs to add information to the name in order to make it unique.

Returns:  The original name

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

GetPhysValue(*[rawValue](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetPhysValue "tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetPhysValue.rawValue (Python parameter)")*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetPhysValue "Link to this definition")  
Returns the physical value of given raw value

Returns:  Physical value of given raw value

Return type:  float

GetRawValue(*[value](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetRawValue "tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetRawValue.value (Python parameter)")*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetRawValue "Link to this definition")  
Returns the raw value of given value

Info

Value can be text or physical value.

Returns:  The raw value

Return type:  int

GetRxEcuNames()[¶](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetRxEcuNames "Link to this definition")  
Returns the names of the ECUs which listen for this Frame/PDU

Returns:  The names of the ECUs

Return type:  list\<str\>

GetSecOcDataId()[¶](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetSecOcDataId "Link to this definition")  
Returns the SecOC Data ID of a PDU, if it is a secured PDU or inside a secured PDU, or None otherwise.

Returns:  SecOC Data ID

Return type:  int or None

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

Info

Only applies to FlexRay frames.

Returns:  The frames start cycle

Return type:  int or None

GetSystemSignalName()[¶](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetSystemSignalName "Link to this definition")  
Returns the name of the system signal of this bus entity

Returns:  The name

Return type:  str

GetTextTable(*[numbersAsStrings](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetTextTable "tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetTextTable.numbersAsStrings (Python parameter)")=`False`*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetTextTable "Link to this definition")  
Returns the text table as a dictionary

Info

Set numbersAsStrings to True when using this method via ApiProxy.

Returns:  The text table

Return type:  dict

GetTimeOffset(*[transmissionMode](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetTimeOffset.transmissionMode "tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetTimeOffset.transmissionMode (Python parameter) — If None maximal time offset is returned. True/False refers to TRANSMISSION-MODE-TRUE/FALSE-TIMING (optional)")=`None`*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetTimeOffset "Link to this definition")  
Returns the time offset of a PDU or a frame

Parameters:  transmissionMode=`None`[¶](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetTimeOffset.transmissionMode "Permalink to this definition")  
If None maximal time offset is returned. True/False refers to TRANSMISSION-MODE-TRUE/FALSE-TIMING (optional)

Return type:  float or None

GetTimings(*[transmissionMode](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetTimings.transmissionMode "tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetTimings.transmissionMode (Python parameter) — If None global Timings are returned. True/False refers to TRANSMISSION-MODE-TRUE/FALSE-TIMING (optional)")=`None`*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetTimings "Link to this definition")  
Returns dtMin and dtMax for this Frame/PDU

Parameters:  transmissionMode=`None`[¶](#tts.core.api.dataBrowserApi.DataBrowser.BusEntity.GetTimings.transmissionMode "Permalink to this definition")  
If None global Timings are returned. True/False refers to TRANSMISSION-MODE-TRUE/FALSE-TIMING (optional)

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

Info

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

### DataBrowser[¶](#id31 "Link to this heading")

*class* DataBrowser[¶](#tts.core.api.dataBrowserApi.DataBrowser.DataBrowser "Link to this definition")  
The DataBrowser provides functions to retrieve a specific object to a database of a configured device in the test configuration. Currently, there are interfaces to browse inside A2L, BUS , debugging (ELF), diagnostic, logging, multimedia, service and SGBD data of an electronic control unit (ECU). The interface to browse SGBD data is currently in a prototype state.

BrowseA2l(*[ecuKey](#tts.core.api.dataBrowserApi.DataBrowser.DataBrowser.BrowseA2l.ecuKey "tts.core.api.dataBrowserApi.DataBrowser.DataBrowser.BrowseA2l.ecuKey (Python parameter) — The name of the ECU to which an A2L browser is requested")*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.DataBrowser.BrowseA2l "Link to this definition")  
BrowseA2l gives access to an A2L database. The database is specified by the same name of the ECU which is given in the test configuration.

E.g.: `a2lBrowser = DataBrowser().BrowseA2l("DME1_DDE1")`Parameters:  
ecuKey : str[¶](#tts.core.api.dataBrowserApi.DataBrowser.DataBrowser.BrowseA2l.ecuKey "Permalink to this definition")  
The name of the ECU to which an A2L browser is requested

Returns:  A2lBrowser object

Return type:  [`A2lBrowser`](#tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser "tts.core.api.dataBrowserApi.DataBrowser.A2lBrowser (Python class) — The A2lBrowser type provides an interface to a A2L database. It is possible to retrieve information for a single entry or to use a full text search to get a list of filtered entries. Every entity is represented by an instance of the type A2lEntity.")

BrowseBus(*[busKey](#tts.core.api.dataBrowserApi.DataBrowser.DataBrowser.BrowseBus.busKey "tts.core.api.dataBrowserApi.DataBrowser.DataBrowser.BrowseBus.busKey (Python parameter) — The name of the BUS to which a BUS browser is requested.")*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.DataBrowser.BrowseBus "Link to this definition")  
BrowseBus gives access to a bus database. The database is specified by the same bus name which is given in the test configuration.

E.g.: `busBrowser = DataBrowser().BrowseBus("PT_CAN")`Parameters:  
busKey : str[¶](#tts.core.api.dataBrowserApi.DataBrowser.DataBrowser.BrowseBus.busKey "Permalink to this definition")  
The name of the BUS to which a BUS browser is requested.

Returns:  BusBrowser object

Return type:  [`BusBrowser`](#tts.core.api.dataBrowserApi.DataBrowser.BusBrowser "tts.core.api.dataBrowserApi.DataBrowser.BusBrowser (Python class) — The BusBrowser type provides an interface to a BUS database. It is possible to retrieve information for a single entry or to use a full text search to get a list of filtered entries. Every entity is represented by an instance of the type BusEntity.")

Info

This part of the DataBrowser API was specifically created to support certain use cases. Don’t expect your use case to easily map onto this API!

BrowseDebug(*[ecuKey](#tts.core.api.dataBrowserApi.DataBrowser.DataBrowser.BrowseDebug.ecuKey "tts.core.api.dataBrowserApi.DataBrowser.DataBrowser.BrowseDebug.ecuKey (Python parameter) — The name of the ECU to which a DebugBrowser is requested.")*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.DataBrowser.BrowseDebug "Link to this definition")  
BrowseDebug gives access to the debug database with information provided by ELF files. The database is specified by the name of the ECU (ecuKey) which is defined in the test configuration.

Parameters:  ecuKey : str[¶](#tts.core.api.dataBrowserApi.DataBrowser.DataBrowser.BrowseDebug.ecuKey "Permalink to this definition")  
The name of the ECU to which a DebugBrowser is requested.

Returns:  DebugBrowser object

Return type:  [`DebugBrowser`](#tts.core.api.dataBrowserApi.DataBrowser.DebugBrowser "tts.core.api.dataBrowserApi.DataBrowser.DebugBrowser (Python class) — The DebugBrowser type prodvides an interface to a Debugger database. It is possible to query for debug variables or register entries.")

BrowseDebugElf(*[elfFile](#tts.core.api.dataBrowserApi.DataBrowser.DataBrowser.BrowseDebugElf.elfFile "tts.core.api.dataBrowserApi.DataBrowser.DataBrowser.BrowseDebugElf.elfFile (Python parameter) — The full path to an ELF-File.")*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.DataBrowser.BrowseDebugElf "Link to this definition")  
BrowseDebugElf gives access to an ELF-database. Contrary to BrowseDebug the database is specified by an ELF-File on the filesystem. Please Note: To query a register a connection to a debugger as well as a API call via BrowseDebug (not BrowseDebugElf) is required.

Parameters:  elfFile : str[¶](#tts.core.api.dataBrowserApi.DataBrowser.DataBrowser.BrowseDebugElf.elfFile "Permalink to this definition")  
The full path to an ELF-File.

Returns:  DebugBrowser object

Return type:  [`DebugBrowser`](#tts.core.api.dataBrowserApi.DataBrowser.DebugBrowser "tts.core.api.dataBrowserApi.DataBrowser.DebugBrowser (Python class) — The DebugBrowser type prodvides an interface to a Debugger database. It is possible to query for debug variables or register entries.")

BrowseDiag(*[ecuKey](#tts.core.api.dataBrowserApi.DataBrowser.DataBrowser.BrowseDiag.ecuKey "tts.core.api.dataBrowserApi.DataBrowser.DataBrowser.BrowseDiag.ecuKey (Python parameter) — The name of the ECU a DiagBrowser is requested for")*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.DataBrowser.BrowseDiag "Link to this definition")  
BrowseDiag gives access to entities from the diagnostic database which was assigned to the ECU in the test configuration.

E.g.: `diagBrowser = DataBrowser().BrowseDiag('Engine')`Parameters:  
ecuKey : str[¶](#tts.core.api.dataBrowserApi.DataBrowser.DataBrowser.BrowseDiag.ecuKey "Permalink to this definition")  
The name of the ECU a DiagBrowser is requested for

Returns:  DiagBrowser object

Return type:  [`DiagBrowser`](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagBrowser "tts.testModule.diag.dataBrowser.DiagBrowser.DiagBrowser (Python class) — The DiagBrowser type provides an interface to a diagnostics data base. DiagBrowser functions are available for ODX-based diagnostics only and are not supported when using CDD or GDX, for example.")

BrowseLogging(*[ecuKey](#tts.core.api.dataBrowserApi.DataBrowser.DataBrowser.BrowseLogging.ecuKey "tts.core.api.dataBrowserApi.DataBrowser.DataBrowser.BrowseLogging.ecuKey (Python parameter) — The name of the ECU to which a logging browser is requested.")*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.DataBrowser.BrowseLogging "Link to this definition")  
BrowseLogging gives access to a logging database. The database is specified by the same name of the ECU which is given in the test configuration.

E.g.: `loggingBrowser = DataBrowser().BrowseLogging("DME1_DDE1")`Parameters:  
ecuKey : str[¶](#tts.core.api.dataBrowserApi.DataBrowser.DataBrowser.BrowseLogging.ecuKey "Permalink to this definition")  
The name of the ECU to which a logging browser is requested.

Returns:  LoggingBrowser object

Return type:  [`LoggingBrowser`](#tts.core.api.dataBrowserApi.DataBrowser.LoggingBrowser "tts.core.api.dataBrowserApi.DataBrowser.LoggingBrowser (Python class) — The LoggingBrowser type provides an interface to a logging database. It is possible to retrieve information for a single entry or to use a full text search to get a list of filtered entries. Every entity is represented by an instance of the type LoggingEntity.")

BrowseModel(*[modelKey](#tts.core.api.dataBrowserApi.DataBrowser.DataBrowser.BrowseModel.modelKey "tts.core.api.dataBrowserApi.DataBrowser.DataBrowser.BrowseModel.modelKey (Python parameter) — Key of the model as specified in the test configuration's Platform tab.")*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.DataBrowser.BrowseModel "Link to this definition")  
BrowseModel gives access to the model database associated with the given modelKey in the test configuration.

Parameters:  modelKey : str[¶](#tts.core.api.dataBrowserApi.DataBrowser.DataBrowser.BrowseModel.modelKey "Permalink to this definition")  
Key of the model as specified in the test configuration’s Platform tab.

Returns:  ModelBrowser object

Return type:  [`ModelBrowser`](#tts.core.api.dataBrowserApi.DataBrowser.ModelBrowser "tts.core.api.dataBrowserApi.DataBrowser.ModelBrowser (Python class) — The ModelBrowser provides an interface to a model database. It is possible to search the available variable paths.")

BrowseMultimedia(*[deviceKey](#tts.core.api.dataBrowserApi.DataBrowser.DataBrowser.BrowseMultimedia.deviceKey "tts.core.api.dataBrowserApi.DataBrowser.DataBrowser.BrowseMultimedia.deviceKey (Python parameter) — The name of the multimedia device to which a browser is requested.")*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.DataBrowser.BrowseMultimedia "Link to this definition")  
BrowseMultimedia gives access to [`Image`](mediadatastructures.md#tts.testModule.multimedia.dataElements.Image.Image "tts.testModule.multimedia.dataElements.Image.Image (Python class) — Represents an image.") or [`Mask`](mediadatastructures.md#tts.testModule.multimedia.dataElements.Mask.Mask "tts.testModule.multimedia.dataElements.Mask.Mask (Python class) — The mask file to load") ojects. The target folder is specified by the same deviceKey which is given as a name in the test configuration.

E.g.: `multimediaBrowser = DataBrowser().BrowseMultimedia("CAM")`Parameters:  
deviceKey : str[¶](#tts.core.api.dataBrowserApi.DataBrowser.DataBrowser.BrowseMultimedia.deviceKey "Permalink to this definition")  
The name of the multimedia device to which a browser is requested.

Returns:  MediaBrowser object

Return type:  [`MediaBrowser`](#tts.testModule.multimedia.dataBrowser.MediaBrowser.MediaBrowser "tts.testModule.multimedia.dataBrowser.MediaBrowser.MediaBrowser (Python class) — The MediaBrowser provides access to images and masks from the file system.")

BrowseService(*[serviceKey](#tts.core.api.dataBrowserApi.DataBrowser.DataBrowser.BrowseService.serviceKey "tts.core.api.dataBrowserApi.DataBrowser.DataBrowser.BrowseService.serviceKey (Python parameter) — The name of the BUS to which a BUS browser is requested.")*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.DataBrowser.BrowseService "Link to this definition")  
BrowseService gives access to a service database. The database is specified by the same name of the service name which is given in the test configuration.

E.g.: `serviceBrowser = DataBrowser().BrowseService("ETHERNET")`Parameters:  
serviceKey : str[¶](#tts.core.api.dataBrowserApi.DataBrowser.DataBrowser.BrowseService.serviceKey "Permalink to this definition")  
The name of the BUS to which a BUS browser is requested.

Returns:  ServiceBrowser object

Return type:  [`ServiceBrowser`](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser "tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser (Python class) — The ServiceBrowser type provides an interface to a service database which allows to access information regarding ECUs, services, methods, events etc.")

Info

prototype

BrowseSgbd(*[ecuKey](#tts.core.api.dataBrowserApi.DataBrowser.DataBrowser.BrowseSgbd.ecuKey "tts.core.api.dataBrowserApi.DataBrowser.DataBrowser.BrowseSgbd.ecuKey (Python parameter) — The name of the ECU to which a SGBD browser is requested.")*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.DataBrowser.BrowseSgbd "Link to this definition")  
BrowseSgbd gives access to a SGBD file. The SGBD is specified by the same name of the ECU which is given in the test configuration.

E.g.: `sgbdBrowser = DataBrowser().BrowseSgbd("DME1_DDE1")`Parameters:  
ecuKey : str[¶](#tts.core.api.dataBrowserApi.DataBrowser.DataBrowser.BrowseSgbd.ecuKey "Permalink to this definition")  
The name of the ECU to which a SGBD browser is requested.

Returns:  SgbdBrowser object

Return type:  [`SgbdBrowser`](#tts.core.api.dataBrowserApi.DataBrowser.SgbdBrowser "tts.core.api.dataBrowserApi.DataBrowser.SgbdBrowser (Python class) — The SgbdBrowser type provides an interface to a SGBD file. It is possible to retrieve information for a single entry or to use a full text search to get a list of filtered entries. Every entity is represented by an instance of the type SgbdEntity.")

Info

prototype

### DebugBrowser[¶](#debugbrowser "Link to this heading")

*class* DebugBrowser[¶](#tts.core.api.dataBrowserApi.DataBrowser.DebugBrowser "Link to this definition")  
The DebugBrowser type prodvides an interface to a Debugger database. It is possible to query for debug variables or register entries.

GetCores()[¶](#tts.core.api.dataBrowserApi.DataBrowser.DebugBrowser.GetCores "Link to this definition")  
Returns names of all cores

Info

Cores are not supported by all debugger tool adapters

Returns:  A list of strings containing the core names found in the database.

Return type:  list\<str\>

GetElfFiles()[¶](#tts.core.api.dataBrowserApi.DataBrowser.DebugBrowser.GetElfFiles "Link to this definition")  
Returns dictionary with mapping from elfFileKey to ELF file path

Returns:  Dictionary with elfFileKey and corresponding ELF file path

Return type:  dict\<str:str\>

GetModules(*[elfFileKey](#tts.core.api.dataBrowserApi.DataBrowser.DebugBrowser.GetModules.elfFileKey "tts.core.api.dataBrowserApi.DataBrowser.DebugBrowser.GetModules.elfFileKey (Python parameter) — elfFileKey with or without wildcard for filtering")*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.DebugBrowser.GetModules "Link to this definition")  
Returns all modules of the ELF file referenced by the given elfFileKey

Parameters:  elfFileKey : str[¶](#tts.core.api.dataBrowserApi.DataBrowser.DebugBrowser.GetModules.elfFileKey "Permalink to this definition")  
elfFileKey with or without wildcard for filtering

Returns:  List of modules

Return type:  list\<str\>

GetRegisters(*[registerName](#tts.core.api.dataBrowserApi.DataBrowser.DebugBrowser.GetRegisters.registerName "tts.core.api.dataBrowserApi.DataBrowser.DebugBrowser.GetRegisters.registerName (Python parameter) — Full register name (group_name) with or without wildcard for filtering")=`None`*, *[coreName](#tts.core.api.dataBrowserApi.DataBrowser.DebugBrowser.GetRegisters.coreName "tts.core.api.dataBrowserApi.DataBrowser.DebugBrowser.GetRegisters.coreName (Python parameter) — Core name with or without wildcard for filtering")=`None`*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.DebugBrowser.GetRegisters "Link to this definition")  
Returns all registers by default

Info

- Use optional parameters to filter registers. You can use \* as wildcard.

- Delivered registerName returns the full name, consisting of register Group and register name separated by underscore.

- Registers are not supported by all debugger tool adapters.

Parameters:  registerName : str[¶](#tts.core.api.dataBrowserApi.DataBrowser.DebugBrowser.GetRegisters.registerName "Permalink to this definition")  
Full register name (group_name) with or without wildcard for filtering

coreName : str[¶](#tts.core.api.dataBrowserApi.DataBrowser.DebugBrowser.GetRegisters.coreName "Permalink to this definition")  
Core name with or without wildcard for filtering

Returns:  A list of dictionaries, each filled the registers full name, its cores name and the mapping path is retured for every entry

Return type:  list\<dict\>

GetVariables(*[variableName](#tts.core.api.dataBrowserApi.DataBrowser.DebugBrowser.GetVariables.variableName "tts.core.api.dataBrowserApi.DataBrowser.DebugBrowser.GetVariables.variableName (Python parameter) — Variable name with or without wildcard for filtering")=`None`*, *[visibility](#tts.core.api.dataBrowserApi.DataBrowser.DebugBrowser.GetVariables.visibility "tts.core.api.dataBrowserApi.DataBrowser.DebugBrowser.GetVariables.visibility (Python parameter) — Type 0 for local, 1 for global or 2 for extern variables to be returned")=`None`*, *[moduleName](#tts.core.api.dataBrowserApi.DataBrowser.DebugBrowser.GetVariables.moduleName "tts.core.api.dataBrowserApi.DataBrowser.DebugBrowser.GetVariables.moduleName (Python parameter) — Module name with or without wildcard for filtering")=`None`*, *[functionName](#tts.core.api.dataBrowserApi.DataBrowser.DebugBrowser.GetVariables.functionName "tts.core.api.dataBrowserApi.DataBrowser.DebugBrowser.GetVariables.functionName (Python parameter) — Function name with or without wildcard for filtering")=`None`*, *[elfFileKey](#tts.core.api.dataBrowserApi.DataBrowser.DebugBrowser.GetVariables.elfFileKey "tts.core.api.dataBrowserApi.DataBrowser.DebugBrowser.GetVariables.elfFileKey (Python parameter) — elfFileKey with or without wildcard for filtering")=`None`*, *[includeExterns](#tts.core.api.dataBrowserApi.DataBrowser.DebugBrowser.GetVariables.includeExterns "tts.core.api.dataBrowserApi.DataBrowser.DebugBrowser.GetVariables.includeExterns (Python parameter) — Use True to include extern variables in the search")=`False`*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.DebugBrowser.GetVariables "Link to this definition")  
Returns all variables except extern variables by default

Info

Use optional parameters to filter variables. You can use \* as wildcard.

Parameters:  variableName : str[¶](#tts.core.api.dataBrowserApi.DataBrowser.DebugBrowser.GetVariables.variableName "Permalink to this definition")  
Variable name with or without wildcard for filtering

visibility : int[¶](#tts.core.api.dataBrowserApi.DataBrowser.DebugBrowser.GetVariables.visibility "Permalink to this definition")  
Type 0 for local, 1 for global or 2 for extern variables to be returned

moduleName : str[¶](#tts.core.api.dataBrowserApi.DataBrowser.DebugBrowser.GetVariables.moduleName "Permalink to this definition")  
Module name with or without wildcard for filtering

functionName : str[¶](#tts.core.api.dataBrowserApi.DataBrowser.DebugBrowser.GetVariables.functionName "Permalink to this definition")  
Function name with or without wildcard for filtering

elfFileKey : str[¶](#tts.core.api.dataBrowserApi.DataBrowser.DebugBrowser.GetVariables.elfFileKey "Permalink to this definition")  
elfFileKey with or without wildcard for filtering

includeExterns : bool[¶](#tts.core.api.dataBrowserApi.DataBrowser.DebugBrowser.GetVariables.includeExterns "Permalink to this definition")  
Use True to include extern variables in the search

Returns:  A list of dictionaries with the following keys: name, moduleName, visibility, type, elfFileKey, mappingPath, functionName and arraySize

Return type:  list\<dict\>

### DiagBrowser[¶](#diagbrowser "Link to this heading")

*class* DiagBrowser[¶](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagBrowser "Link to this definition")  
The DiagBrowser type provides an interface to a diagnostics data base. DiagBrowser functions are available for ODX-based diagnostics only and are not supported when using CDD or GDX, for example.

GetDiagDtcs()[¶](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagBrowser.GetDiagDtcs "Link to this definition")  
Returns a list of DTC entities representing all diagnostics DTCs defined in the database

Returns:  A list of DiagDtcEntity

Return type:  list\<[`DiagDtcEntity`](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagDtcEntity "tts.testModule.diag.dataBrowser.DiagBrowser.DiagDtcEntity (Python class) — The DiagDtcEntity represents one diagnostics dtc in the database.")\>

GetDiagServices()[¶](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagBrowser.GetDiagServices "Link to this definition")  
Returns a list of service entities representing all diagnostics services defined in the database

Returns:  A list of DiagServiceEntity

Return type:  list\<[`DiagServiceEntity`](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagServiceEntity "tts.testModule.diag.dataBrowser.DiagBrowser.DiagServiceEntity (Python class) — The DiagServiceEntity represents one diagnostics service in the database.")\>

GetDiagStateCharts()[¶](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagBrowser.GetDiagStateCharts "Link to this definition")  
Returns a list of state chart entities representing all state charts defined in the database

Returns:  A list of DiagStateChartEntity

Return type:  list\<[`DiagStateChartEntity`](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateChartEntity "tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateChartEntity (Python class) — The DiagStateChartEntity represents a state chart from the diagnostics database.")\>

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

Return type:  list[[*DiagStateEntity*](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateEntity "tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateEntity (Python class) — The DiagStateEntity represents a state from the diagnostics database.")]

GetSdgs()[¶](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagServiceEntity.GetSdgs "Link to this definition")  
Returns the special data of the diagnostics service from the database. The special data is a set of key/value pairs and can be subdivided into groups.

Returns:  A dictionary containing the special data group SI attribute or caption short name as key. The value will be the SD key/value pairs as further dictionaries

Return type:  dict\<str, dict\<str, str\>\>

GetServiceId()[¶](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagServiceEntity.GetServiceId "Link to this definition")  
Returns the service ID of this service

Info

e.g. 34 for ReadDataByIdentifier

Returns:  The service ID

Return type:  int

GetServiceName()[¶](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagServiceEntity.GetServiceName "Link to this definition")  
Returns the name of the service. This Methode distinguishes between different application layers (e.g. UDS, KWP 2000)

Info

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

Return type:  [DiagStateEntity](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateEntity "tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateEntity (Python class) — The DiagStateEntity represents a state from the diagnostics database.")

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

Return type:  list[[*DiagStateTransitionEntity*](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateTransitionEntity "tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateTransitionEntity (Python class) — The DiagStateTransitionEntity represents a transition from one state to another as defined in the diagnostics data base.")]

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

Return type:  list[[*DiagStateTransitionEntity*](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateTransitionEntity "tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateTransitionEntity (Python class) — The DiagStateTransitionEntity represents a transition from one state to another as defined in the diagnostics data base.")]

GetStateChart()[¶](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateEntity.GetStateChart "Link to this definition")  
Returns the state chart this state belongs to

Returns:  The state chart

Return type:  [*DiagStateChartEntity*](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateChartEntity "tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateChartEntity (Python class) — The DiagStateChartEntity represents a state chart from the diagnostics database.")

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

Return type:  list[[*DiagServiceEntity*](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagServiceEntity "tts.testModule.diag.dataBrowser.DiagBrowser.DiagServiceEntity (Python class) — The DiagServiceEntity represents one diagnostics service in the database.")]

GetShortName()[¶](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateTransitionEntity.GetShortName "Link to this definition")  
Returns the short name of this transition

Returns:  The short name

Return type:  str | None

GetSourceState()[¶](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateTransitionEntity.GetSourceState "Link to this definition")  
Returns the source state of this transition

Returns:  The state

Return type:  [*DiagStateEntity*](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateEntity "tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateEntity (Python class) — The DiagStateEntity represents a state from the diagnostics database.")

GetStateChart()[¶](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateTransitionEntity.GetStateChart "Link to this definition")  
Returns the state chart this transition belongs to

Returns:  The state chart

Return type:  [*DiagStateChartEntity*](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateChartEntity "tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateChartEntity (Python class) — The DiagStateChartEntity represents a state chart from the diagnostics database.")

GetTargetState()[¶](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateTransitionEntity.GetTargetState "Link to this definition")  
Returns the target state of this transition

Returns:  The state

Return type:  [*DiagStateEntity*](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateEntity "tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateEntity (Python class) — The DiagStateEntity represents a state from the diagnostics database.")

GetTransitionId()[¶](#tts.testModule.diag.dataBrowser.DiagBrowser.DiagStateTransitionEntity.GetTransitionId "Link to this definition")  
Returns the ID of this transition if it was specified in the diagnostics database

Returns:  The transition ID

Return type:  str

### LoggingBrowser[¶](#loggingbrowser "Link to this heading")

*class* LoggingBrowser[¶](#tts.core.api.dataBrowserApi.DataBrowser.LoggingBrowser "Link to this definition")  
The LoggingBrowser type provides an interface to a logging database. It is possible to retrieve information for a single entry or to use a full text search to get a list of filtered entries. Every entity is represented by an instance of the type [`LoggingEntity`](#tts.core.api.dataBrowserApi.DataBrowser.LoggingEntity "tts.core.api.dataBrowserApi.DataBrowser.LoggingEntity (Python class) — The LoggingEntity type represents one entry in a logging database.").

GetProtocol()[¶](#tts.core.api.dataBrowserApi.DataBrowser.LoggingBrowser.GetProtocol "Link to this definition")  
Returns the logging protocol configured for the ECU

Returns:  “DLT (non-verbose)” or “DLT (verbose)”

Return type:  str

ListArguments(*[messageName](#tts.core.api.dataBrowserApi.DataBrowser.LoggingBrowser.ListArguments.messageName "tts.core.api.dataBrowserApi.DataBrowser.LoggingBrowser.ListArguments.messageName (Python parameter) — The exact name of the message in which to search for arguments")*, *[filter](#tts.core.api.dataBrowserApi.DataBrowser.LoggingBrowser.ListArguments.filter "tts.core.api.dataBrowserApi.DataBrowser.LoggingBrowser.ListArguments.filter (Python parameter) — The search string which is part of a logging argument's nam")=`''`*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.LoggingBrowser.ListArguments "Link to this definition")  
Returns a list of LoggingEntity instances corresponding to message arguments whose name matches the specified search string

Returns an empty list if the logging protocol is not “DLT (non-verbose)”.

Parameters:  messageName : str[¶](#tts.core.api.dataBrowserApi.DataBrowser.LoggingBrowser.ListArguments.messageName "Permalink to this definition")  
The exact name of the message in which to search for arguments

filter : str[¶](#tts.core.api.dataBrowserApi.DataBrowser.LoggingBrowser.ListArguments.filter "Permalink to this definition")  
The search string which is part of a logging argument’s nam

Returns:  A list of LoggingEntity instances if the logging database contains entries with the given search string, otherwise an empty list

Return type:  list \<[`LoggingEntity`](#tts.core.api.dataBrowserApi.DataBrowser.LoggingEntity "tts.core.api.dataBrowserApi.DataBrowser.LoggingEntity (Python class) — The LoggingEntity type represents one entry in a logging database.")\>

ListMessages(*[filter](#tts.core.api.dataBrowserApi.DataBrowser.LoggingBrowser.ListMessages.filter "tts.core.api.dataBrowserApi.DataBrowser.LoggingBrowser.ListMessages.filter (Python parameter) — The search string which is part of a logging message's name")=`''`*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.LoggingBrowser.ListMessages "Link to this definition")  
Returns a list of LoggingEntity instances corresponding to messages whose name matches the specified search string

Parameters:  filter : str[¶](#tts.core.api.dataBrowserApi.DataBrowser.LoggingBrowser.ListMessages.filter "Permalink to this definition")  
The search string which is part of a logging message’s name

Returns:  A list of LoggingEntity instances if the logging database contains entries with the given search string, otherwise an empty list

Return type:  list \<[`LoggingEntity`](#tts.core.api.dataBrowserApi.DataBrowser.LoggingEntity "tts.core.api.dataBrowserApi.DataBrowser.LoggingEntity (Python class) — The LoggingEntity type represents one entry in a logging database.")\>

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

GetPhysValue(*[rawValue](#tts.core.api.dataBrowserApi.DataBrowser.LoggingEntity.GetPhysValue "tts.core.api.dataBrowserApi.DataBrowser.LoggingEntity.GetPhysValue.rawValue (Python parameter)")*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.LoggingEntity.GetPhysValue "Link to this definition")  
Returns the physical value of given raw value

Info

Only valid for logging arguments of protocol “DLT (non-verbose)”

Returns:  The physical value of given raw value

Return type:  float

GetRawValue(*[value](#tts.core.api.dataBrowserApi.DataBrowser.LoggingEntity.GetRawValue "tts.core.api.dataBrowserApi.DataBrowser.LoggingEntity.GetRawValue.value (Python parameter)")*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.LoggingEntity.GetRawValue "Link to this definition")  
Returns the raw value of given value

Info

Value can be text or physical value. Only valid for logging arguments of protocol “DLT (non-verbose)”

Returns:  The raw value of given value

Return type:  int

GetTxEcuNames()[¶](#tts.core.api.dataBrowserApi.DataBrowser.LoggingEntity.GetTxEcuNames "Link to this definition")  
Returns the names of the ECUs which transmit this message/signal

Info

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

Images can be accessed via the Images property. E.g. mediaBrowser.Images.myImage. This will return an object of type [`Image`](mediadatastructures.md#tts.testModule.multimedia.dataElements.Image.Image "tts.testModule.multimedia.dataElements.Image.Image (Python class) — Represents an image.").

Masks can be accessed via the Masks property. E.g. mediaBrowser.Masks.myMask. This will return an object of type [`Mask`](mediadatastructures.md#tts.testModule.multimedia.dataElements.Mask.Mask "tts.testModule.multimedia.dataElements.Mask.Mask (Python class) — The mask file to load").

Example:  
Suppose there is a file called “myImage.png” in the image directory that is associated with the media node “CAM”. Then you could access it with:

    >>> api.DataBrowser.BrowseMultimedia("CAM").Images.myImage

### ModelBrowser[¶](#modelbrowser "Link to this heading")

*class* ModelBrowser[¶](#tts.core.api.dataBrowserApi.DataBrowser.ModelBrowser "Link to this definition")  
The ModelBrowser provides an interface to a model database. It is possible to search the available variable paths.

FindVariables(*[searchString](#tts.core.api.dataBrowserApi.DataBrowser.ModelBrowser.FindVariables.searchString "tts.core.api.dataBrowserApi.DataBrowser.ModelBrowser.FindVariables.searchString (Python parameter) — string for search")*, *[maxResults](#tts.core.api.dataBrowserApi.DataBrowser.ModelBrowser.FindVariables.maxResults "tts.core.api.dataBrowserApi.DataBrowser.ModelBrowser.FindVariables.maxResults (Python parameter) — maximal number of returned found items")=`None`*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.ModelBrowser.FindVariables "Link to this definition")  
Find all variables in the model tree whose full model path matches the given search string. The search may include the wildcards ‘\*’ and ‘?’. Only leaf elements of the model tree are returned. These are either parameters, signals or virtual signals of the model.

Parameters:  searchString : str[¶](#tts.core.api.dataBrowserApi.DataBrowser.ModelBrowser.FindVariables.searchString "Permalink to this definition")  
string for search

maxResults : int | None[¶](#tts.core.api.dataBrowserApi.DataBrowser.ModelBrowser.FindVariables.maxResults "Permalink to this definition")  
maximal number of returned found items

Returns:  list of found model paths

Return type:  list \<str\>

### ServiceBrowser[¶](#servicebrowser "Link to this heading")

*class* ServiceBrowser[¶](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser "Link to this definition")  
The ServiceBrowser type provides an interface to a service database which allows to access information regarding ECUs, services, methods, events etc.

GetE2EProfile(*[ecuName](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetE2EProfile.ecuName "tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetE2EProfile.ecuName (Python parameter) — The name of the ECU")*, *[serviceName](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetE2EProfile.serviceName "tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetE2EProfile.serviceName (Python parameter) — The name of the service")*, *[methodOrEventName](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetE2EProfile.methodOrEventName "tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetE2EProfile.methodOrEventName (Python parameter) — The event or method name")*, *[eventgroupName](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetE2EProfile.eventgroupName "tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetE2EProfile.eventgroupName (Python parameter) — The name of the event group or None")=`None`*, *[fieldName](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetE2EProfile.fieldName "tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetE2EProfile.fieldName (Python parameter) — The name of the field or None")=`None`*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetE2EProfile "Link to this definition")  
Returns the E2E profile configuration of an event or a field or a method

Info

A method may have different profiles for input and output parameters. Profiles 4 and 7 are currently supported.

Parameters:  ecuName : str[¶](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetE2EProfile.ecuName "Permalink to this definition")  
The name of the ECU

serviceName : str[¶](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetE2EProfile.serviceName "Permalink to this definition")  
The name of the service

methodOrEventName : str[¶](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetE2EProfile.methodOrEventName "Permalink to this definition")  
The event or method name

eventgroupName : str or None[¶](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetE2EProfile.eventgroupName "Permalink to this definition")  
The name of the event group or None

fieldName : str or None[¶](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetE2EProfile.fieldName "Permalink to this definition")  
The name of the field or None

Return type:  dict

Info

The key is the extended name of the E2E input “in” or return “out” parameter. The values are E2E configuration parameters. The validity of each of the configuration parameters depends on the E2E profile. See the item “category”.

GetEcuConsumerInfos(*[providerEcuName](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetEcuConsumerInfos.providerEcuName "tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetEcuConsumerInfos.providerEcuName (Python parameter) — The name of the providing ECU")*, *[serviceName](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetEcuConsumerInfos.serviceName "tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetEcuConsumerInfos.serviceName (Python parameter) — The name of the service")*, *[eventGroupName](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetEcuConsumerInfos.eventGroupName "tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetEcuConsumerInfos.eventGroupName (Python parameter) — If set, the name of the provided event group")=`None`*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetEcuConsumerInfos "Link to this definition")  
Returns network infos of the consumer ECUs of the service (or event group), that is specified by a given providerEcuName, serviceName (and eventGroupName). Use only for ARXMLs of version AUTOSAR_00048 or higher. If the port is assigned dynamically at runtime, the key ‘Port’ will return ‘dynamic’.

Parameters:  providerEcuName : str[¶](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetEcuConsumerInfos.providerEcuName "Permalink to this definition")  
The name of the providing ECU

serviceName : str[¶](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetEcuConsumerInfos.serviceName "Permalink to this definition")  
The name of the service

eventGroupName : str | None[¶](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetEcuConsumerInfos.eventGroupName "Permalink to this definition")  
If set, the name of the provided event group

Returns:  Network infos ecuName, IP, TP=UDP|TCP, Port of consuming ECUs as list of dicts with the keys: ecuName, IP, TP (transport protocol = UDP|TCP), Port (\<int\>|’dynamic’)

Return type:  list \<dict\>

GetEcuConsumerNamesByServiceName(*[serviceName](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetEcuConsumerNamesByServiceName.serviceName "tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetEcuConsumerNamesByServiceName.serviceName (Python parameter) — The name of the service")*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetEcuConsumerNamesByServiceName "Link to this definition")  
Returns the ECUs the given service is consumed by

Parameters:  serviceName : str[¶](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetEcuConsumerNamesByServiceName.serviceName "Permalink to this definition")  
The name of the service

Returns:  The names of the events

Return type:  list \<str\>

GetEcuNamesByServiceName(*[serviceName](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetEcuNamesByServiceName.serviceName "tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetEcuNamesByServiceName.serviceName (Python parameter) — The name of the service")*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetEcuNamesByServiceName "Link to this definition")  
Returns the ECUs the given service is provided by

Parameters:  serviceName : str[¶](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetEcuNamesByServiceName.serviceName "Permalink to this definition")  
The name of the service

Returns:  The names of the ECUs

Return type:  list \<str\>

GetEcus()[¶](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetEcus "Link to this definition")  
Returns all ECU names

Returns:  The names of the ECUs

Return type:  list \<str\>

GetEventGroupInfos(*[ecuName](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetEventGroupInfos.ecuName "tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetEventGroupInfos.ecuName (Python parameter) — The Name of the ECU")*, *[serviceName](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetEventGroupInfos.serviceName "tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetEventGroupInfos.serviceName (Python parameter) — The name of the service")*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetEventGroupInfos "Link to this definition")  
Returns name and ID of all event groups of a given service

Parameters:  ecuName : str[¶](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetEventGroupInfos.ecuName "Permalink to this definition")  
The Name of the ECU

serviceName : str[¶](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetEventGroupInfos.serviceName "Permalink to this definition")  
The name of the service

Returns:  List of tuples with name and ID of all event groups

Return type:  list \<tuple \<str, int\> \>

GetEventInfos(*[ecuName](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetEventInfos.ecuName "tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetEventInfos.ecuName (Python parameter) — The name of the ECU")*, *[serviceName](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetEventInfos.serviceName "tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetEventInfos.serviceName (Python parameter) — The name of the service")*, *[eventgroupName](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetEventInfos.eventgroupName "tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetEventInfos.eventgroupName (Python parameter) — The name of the event group")*, *[fieldName](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetEventInfos.fieldName "tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetEventInfos.fieldName (Python parameter) — (Optional) The name of the field")=`None`*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetEventInfos "Link to this definition")  
Returns name and ID of all events of a given event group

Parameters:  ecuName : str[¶](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetEventInfos.ecuName "Permalink to this definition")  
The name of the ECU

serviceName : str[¶](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetEventInfos.serviceName "Permalink to this definition")  
The name of the service

eventgroupName : str[¶](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetEventInfos.eventgroupName "Permalink to this definition")  
The name of the event group

fieldName : str or None[¶](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetEventInfos.fieldName "Permalink to this definition")  
(Optional) The name of the field

Returns:  List of tuples with name and ID of all events

Return type:  list \<tuple \<str, int\> \>

GetFieldNamesByServiceName(*[ecuName](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetFieldNamesByServiceName.ecuName "tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetFieldNamesByServiceName.ecuName (Python parameter) — The name of the ECU")*, *[serviceName](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetFieldNamesByServiceName.serviceName "tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetFieldNamesByServiceName.serviceName (Python parameter) — The name of the service")*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetFieldNamesByServiceName "Link to this definition")  
Returns field names of a given service

Parameters:  ecuName : str[¶](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetFieldNamesByServiceName.ecuName "Permalink to this definition")  
The name of the ECU

serviceName : str[¶](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetFieldNamesByServiceName.serviceName "Permalink to this definition")  
The name of the service

Returns:  The names of the fields

Return type:  list \<str\>

GetInputParameterRepresentation(*[ecuName](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetInputParameterRepresentation.ecuName "tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetInputParameterRepresentation.ecuName (Python parameter) — name of the ECU")*, *[serviceName](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetInputParameterRepresentation.serviceName "tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetInputParameterRepresentation.serviceName (Python parameter) — name of the service")*, *[methodOrEventName](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetInputParameterRepresentation.methodOrEventName "tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetInputParameterRepresentation.methodOrEventName (Python parameter) — event or method name")*, *[eventgroupName](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetInputParameterRepresentation.eventgroupName "tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetInputParameterRepresentation.eventgroupName (Python parameter) — name of the event group or None")=`None`*, *[fieldName](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetInputParameterRepresentation.fieldName "tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetInputParameterRepresentation.fieldName (Python parameter) — name of the field or None")=`None`*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetInputParameterRepresentation "Link to this definition")  
Returns a nested dict which contains the type definitions of all input values of an event, a field or a method.

Parameters:  ecuName : str[¶](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetInputParameterRepresentation.ecuName "Permalink to this definition")  
name of the ECU

serviceName : str[¶](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetInputParameterRepresentation.serviceName "Permalink to this definition")  
name of the service

methodOrEventName : str[¶](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetInputParameterRepresentation.methodOrEventName "Permalink to this definition")  
event or method name

eventgroupName : str / None[¶](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetInputParameterRepresentation.eventgroupName "Permalink to this definition")  
name of the event group or None

fieldName : str / None[¶](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetInputParameterRepresentation.fieldName "Permalink to this definition")  
name of the field or None

Return type:  dict

GetInstanceID(*[ecuName](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetInstanceID.ecuName "tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetInstanceID.ecuName (Python parameter) — The name of the ECU")*, *[serviceName](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetInstanceID.serviceName "tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetInstanceID.serviceName (Python parameter) — The name of the service")*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetInstanceID "Link to this definition")  
Returns the instance ID of a given service

Parameters:  ecuName : str[¶](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetInstanceID.ecuName "Permalink to this definition")  
The name of the ECU

serviceName : str[¶](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetInstanceID.serviceName "Permalink to this definition")  
The name of the service

Returns:  The instance ID

Return type:  str or None

GetMethodInfos(*[ecuName](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetMethodInfos.ecuName "tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetMethodInfos.ecuName (Python parameter) — The name of the ECU")*, *[serviceName](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetMethodInfos.serviceName "tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetMethodInfos.serviceName (Python parameter) — The name of the service")*, *[fieldName](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetMethodInfos.fieldName "tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetMethodInfos.fieldName (Python parameter) — (Optional) The name of the field")=`None`*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetMethodInfos "Link to this definition")  
Returns name and ID of all methods of a given service

Parameters:  ecuName : str[¶](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetMethodInfos.ecuName "Permalink to this definition")  
The name of the ECU

serviceName : str[¶](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetMethodInfos.serviceName "Permalink to this definition")  
The name of the service

fieldName : str or None[¶](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetMethodInfos.fieldName "Permalink to this definition")  
(Optional) The name of the field

Returns:  List of tuples with name and ID of all methods

Return type:  list \<tuple \<str, int\> \>

GetOfferCyclicDelay(*[ecuName](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetOfferCyclicDelay.ecuName "tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetOfferCyclicDelay.ecuName (Python parameter) — The name of the ECU")*, *[serviceName](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetOfferCyclicDelay.serviceName "tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetOfferCyclicDelay.serviceName (Python parameter) — The name of the service")*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetOfferCyclicDelay "Link to this definition")  
Returns the delay between cyclic offers in seconds of a given service

Parameters:  ecuName : str[¶](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetOfferCyclicDelay.ecuName "Permalink to this definition")  
The name of the ECU

serviceName : str[¶](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetOfferCyclicDelay.serviceName "Permalink to this definition")  
The name of the service

Returns:  Cyclic offers in seconds

Return type:  float or None

GetReturnParameterRepresentation(*[ecuName](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetReturnParameterRepresentation.ecuName "tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetReturnParameterRepresentation.ecuName (Python parameter) — name of the ECU")*, *[serviceName](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetReturnParameterRepresentation.serviceName "tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetReturnParameterRepresentation.serviceName (Python parameter) — name of the service")*, *[methodOrEventName](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetReturnParameterRepresentation.methodOrEventName "tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetReturnParameterRepresentation.methodOrEventName (Python parameter) — event or method name")*, *[eventgroupName](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetReturnParameterRepresentation.eventgroupName "tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetReturnParameterRepresentation.eventgroupName (Python parameter) — name of the event group or None")=`None`*, *[fieldName](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetReturnParameterRepresentation.fieldName "tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetReturnParameterRepresentation.fieldName (Python parameter) — name of the field or None")=`None`*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetReturnParameterRepresentation "Link to this definition")  
Returns a nested dict which contains the type definitions of all return values of an event, a field or a method.

Parameters:  ecuName : str[¶](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetReturnParameterRepresentation.ecuName "Permalink to this definition")  
name of the ECU

serviceName : str[¶](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetReturnParameterRepresentation.serviceName "Permalink to this definition")  
name of the service

methodOrEventName : str[¶](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetReturnParameterRepresentation.methodOrEventName "Permalink to this definition")  
event or method name

eventgroupName : str / None[¶](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetReturnParameterRepresentation.eventgroupName "Permalink to this definition")  
name of the event group or None

fieldName : str / None[¶](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetReturnParameterRepresentation.fieldName "Permalink to this definition")  
name of the field or None

Return type:  dict

GetSDGsAndSDs()[¶](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetSDGsAndSDs "Link to this definition")  
Returns a dictionary with all top level SDGs and their associated SDs.

Returns:  Dictionary with SDG names as keys and a list of their corresponding SDs as values (JSON).

Return type:  dict \<str, list\<str\>\>

GetServiceAdressInfos(*[ecuName](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetServiceAdressInfos.ecuName "tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetServiceAdressInfos.ecuName (Python parameter) — The name of the ECU")*, *[serviceName](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetServiceAdressInfos.serviceName "tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetServiceAdressInfos.serviceName (Python parameter) — The name of the service")*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetServiceAdressInfos "Link to this definition")  
Returns all provider adress infos of a given service

Parameters:  ecuName : str[¶](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetServiceAdressInfos.ecuName "Permalink to this definition")  
The name of the ECU

serviceName : str[¶](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetServiceAdressInfos.serviceName "Permalink to this definition")  
The name of the service

Returns:  Dict with provider adress ‘IP’ and ‘TCP’ or ‘UDP’ source port

Return type:  \<dict\>

GetServiceID(*[ecuName](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetServiceID.ecuName "tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetServiceID.ecuName (Python parameter) — The name of the ECU")*, *[serviceName](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetServiceID.serviceName "tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetServiceID.serviceName (Python parameter) — The name of the service")*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetServiceID "Link to this definition")  
Returns the service ID of a given service

Parameters:  ecuName : str[¶](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetServiceID.ecuName "Permalink to this definition")  
The name of the ECU

serviceName : str[¶](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetServiceID.serviceName "Permalink to this definition")  
The name of the service

Returns:  The service ID

Return type:  str or None

GetServiceInfos(*[ecuName](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetServiceInfos.ecuName "tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetServiceInfos.ecuName (Python parameter) — (Optional) Name of the ECU")=`None`*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetServiceInfos "Link to this definition")  
Returns name and ID of all provided services (of a given ECU)

Parameters:  ecuName : str or None[¶](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetServiceInfos.ecuName "Permalink to this definition")  
(Optional) Name of the ECU

Returns:  List of tuples with name and ID of services

Return type:  dict \<tuple \<str, int\> \>

GetTimings(*[ecuName](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetTimings.ecuName "tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetTimings.ecuName (Python parameter) — The name of the ECU")*, *[serviceName](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetTimings.serviceName "tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetTimings.serviceName (Python parameter) — The name of the service")*, *[methodName](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetTimings.methodName "tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetTimings.methodName (Python parameter) — The name of the method")*, *[eventgroupName](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetTimings.eventgroupName "tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetTimings.eventgroupName (Python parameter) — (Optional) The name of the event group")=`None`*, *[fieldName](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetTimings.fieldName "tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetTimings.fieldName (Python parameter) — (Optional) The name of the field")=`None`*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetTimings "Link to this definition")  
Returns timing information of a given event or method

Parameters:  ecuName : str[¶](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetTimings.ecuName "Permalink to this definition")  
The name of the ECU

serviceName : str[¶](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetTimings.serviceName "Permalink to this definition")  
The name of the service

methodName : str[¶](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetTimings.methodName "Permalink to this definition")  
The name of the method

eventgroupName : str or None[¶](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetTimings.eventgroupName "Permalink to this definition")  
(Optional) The name of the event group

fieldName : str or None[¶](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetTimings.fieldName "Permalink to this definition")  
(Optional) The name of the field

Returns:  Dict with keys ‘ApplicationCycleTime’, ‘DebounceTimeRange’, ‘RequestDebounceTimeRange’, ‘TpSeparationTime’ and their values

Return type:  dict

GetVersion(*[ecuName](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetVersion.ecuName "tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetVersion.ecuName (Python parameter) — The name of the ECU")*, *[serviceName](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetVersion.serviceName "tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetVersion.serviceName (Python parameter) — The name of the service")*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetVersion "Link to this definition")  
Returns the minor and major version of a given service

Parameters:  ecuName : str[¶](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetVersion.ecuName "Permalink to this definition")  
The name of the ECU

serviceName : str[¶](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetVersion.serviceName "Permalink to this definition")  
The name of the service

Returns:  Tuple with the minor and major version

Return type:  tuple \<int, int\>

GetVlanInfo(*[ecuName](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetVlanInfo.ecuName "tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetVlanInfo.ecuName (Python parameter) — The name of the ECU")*, *[serviceName](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetVlanInfo.serviceName "tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetVlanInfo.serviceName (Python parameter) — nThe name of the service")*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetVlanInfo "Link to this definition")  
Returns the VLAN ID and the default priority of a given service

Parameters:  ecuName : str[¶](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetVlanInfo.ecuName "Permalink to this definition")  
The name of the ECU

serviceName : str[¶](#tts.core.api.dataBrowserApi.DataBrowser.ServiceBrowser.GetVlanInfo.serviceName "Permalink to this definition")  
nThe name of the service

Returns:  VLAN ID and the default priority

Return type:  tuple(int, int)

### SgbdBrowser[¶](#sgbdbrowser "Link to this heading")

*class* SgbdBrowser[¶](#tts.core.api.dataBrowserApi.DataBrowser.SgbdBrowser "Link to this definition")  
The SgbdBrowser type provides an interface to a SGBD file. It is possible to retrieve information for a single entry or to use a full text search to get a list of filtered entries. Every entity is represented by an instance of the type [`SgbdEntity`](#tts.core.api.dataBrowserApi.DataBrowser.SgbdEntity "tts.core.api.dataBrowserApi.DataBrowser.SgbdEntity (Python class) — The SgbdEntity type represents one entry in a SGBD file.").

Info

prototype

GetJob(*[jobName](#tts.core.api.dataBrowserApi.DataBrowser.SgbdBrowser.GetJob.jobName "tts.core.api.dataBrowserApi.DataBrowser.SgbdBrowser.GetJob.jobName (Python parameter) — Name of job to get")*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.SgbdBrowser.GetJob "Link to this definition")  
Returns the SgbdEntity of a Job if it exists in selected SGBD or None if does not

Parameters:  jobName : str[¶](#tts.core.api.dataBrowserApi.DataBrowser.SgbdBrowser.GetJob.jobName "Permalink to this definition")  
Name of job to get

Returns:  [`SgbdEntity`](#tts.core.api.dataBrowserApi.DataBrowser.SgbdEntity "tts.core.api.dataBrowserApi.DataBrowser.SgbdEntity (Python class) — The SgbdEntity type represents one entry in a SGBD file.") for the first matching job or None

Return type:  [`SgbdEntity`](#tts.core.api.dataBrowserApi.DataBrowser.SgbdEntity "tts.core.api.dataBrowserApi.DataBrowser.SgbdEntity (Python class) — The SgbdEntity type represents one entry in a SGBD file.") or None

GetListTableNames()[¶](#tts.core.api.dataBrowserApi.DataBrowser.SgbdBrowser.GetListTableNames "Link to this definition")  
Returns a list which contains all SGBD table names

Returns:  A list with all SGBD table names

Return type:  list \<str\>

IsJob(*[jobName](#tts.core.api.dataBrowserApi.DataBrowser.SgbdBrowser.IsJob.jobName "tts.core.api.dataBrowserApi.DataBrowser.SgbdBrowser.IsJob.jobName (Python parameter) — The name of job to be checked")*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.SgbdBrowser.IsJob "Link to this definition")  
Returns True if Job exists in selected SGBD or False if not

Parameters:  jobName : str[¶](#tts.core.api.dataBrowserApi.DataBrowser.SgbdBrowser.IsJob.jobName "Permalink to this definition")  
The name of job to be checked

Returns:  True if Job exists or False if not

Return type:  bool

ListJobs(*[filter](#tts.core.api.dataBrowserApi.DataBrowser.SgbdBrowser.ListJobs.filter "tts.core.api.dataBrowserApi.DataBrowser.SgbdBrowser.ListJobs.filter (Python parameter) — The search string which is part of a job")=`''`*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.SgbdBrowser.ListJobs "Link to this definition")  
Returns a list which contains instances of SgbdEntity whose matches the specified job search string

Parameters:  filter : str[¶](#tts.core.api.dataBrowserApi.DataBrowser.SgbdBrowser.ListJobs.filter "Permalink to this definition")  
The search string which is part of a job

Returns:  A list of SgbdEntity instances if the SGBD file contains entries with the given search string, otherwise an empty list

Return type:  list \<[`SgbdEntity`](#tts.core.api.dataBrowserApi.DataBrowser.SgbdEntity "tts.core.api.dataBrowserApi.DataBrowser.SgbdEntity (Python class) — The SgbdEntity type represents one entry in a SGBD file.")\>

Info

prototype

QueryTableByArgument(*[job](#tts.core.api.dataBrowserApi.DataBrowser.SgbdBrowser.QueryTableByArgument.job "tts.core.api.dataBrowserApi.DataBrowser.SgbdBrowser.QueryTableByArgument.job (Python parameter) — The name of the job")=`None`*, *[argument](#tts.core.api.dataBrowserApi.DataBrowser.SgbdBrowser.QueryTableByArgument.argument "tts.core.api.dataBrowserApi.DataBrowser.SgbdBrowser.QueryTableByArgument.argument (Python parameter) — The name of the argument")=`None`*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.SgbdBrowser.QueryTableByArgument "Link to this definition")  
Returns a dictionary representing a specific argument table of the given job

Parameters:  job : str[¶](#tts.core.api.dataBrowserApi.DataBrowser.SgbdBrowser.QueryTableByArgument.job "Permalink to this definition")  
The name of the job

argument : str[¶](#tts.core.api.dataBrowserApi.DataBrowser.SgbdBrowser.QueryTableByArgument.argument "Permalink to this definition")  
The name of the argument

Returns:  A dictionary representing the columns of the argument table

Return type:  dict

QueryTableByName(*[tableName](#tts.core.api.dataBrowserApi.DataBrowser.SgbdBrowser.QueryTableByName.tableName "tts.core.api.dataBrowserApi.DataBrowser.SgbdBrowser.QueryTableByName.tableName (Python parameter) — The name of a SGBD table")=`None`*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.SgbdBrowser.QueryTableByName "Link to this definition")  
Returns the SGBD table indicated by the given name

Parameters:  tableName : str[¶](#tts.core.api.dataBrowserApi.DataBrowser.SgbdBrowser.QueryTableByName.tableName "Permalink to this definition")  
The name of a SGBD table

Returns:  A dictionary representing the columns of the SGBD table

Return type:  dict

QueryTableByResult(*[job](#tts.core.api.dataBrowserApi.DataBrowser.SgbdBrowser.QueryTableByResult.job "tts.core.api.dataBrowserApi.DataBrowser.SgbdBrowser.QueryTableByResult.job (Python parameter) — The name of the job")=`None`*, *[result](#tts.core.api.dataBrowserApi.DataBrowser.SgbdBrowser.QueryTableByResult.result "tts.core.api.dataBrowserApi.DataBrowser.SgbdBrowser.QueryTableByResult.result (Python parameter) — The name of the result")=`None`*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.SgbdBrowser.QueryTableByResult "Link to this definition")  
Returns a dictionary representing a specific result table of the given job

Parameters:  job : str[¶](#tts.core.api.dataBrowserApi.DataBrowser.SgbdBrowser.QueryTableByResult.job "Permalink to this definition")  
The name of the job

result : str[¶](#tts.core.api.dataBrowserApi.DataBrowser.SgbdBrowser.QueryTableByResult.result "Permalink to this definition")  
The name of the result

Returns:  A dictionary representing the columns of the result table

Return type:  dict

### SgbdEntity[¶](#sgbdentity "Link to this heading")

*class* SgbdEntity[¶](#tts.core.api.dataBrowserApi.DataBrowser.SgbdEntity "Link to this definition")  
The SgbdEntity type represents one entry in a SGBD file.

Info

prototype

GetArgumentType(*[argumentName](#tts.core.api.dataBrowserApi.DataBrowser.SgbdEntity.GetArgumentType.argumentName "tts.core.api.dataBrowserApi.DataBrowser.SgbdEntity.GetArgumentType.argumentName (Python parameter) — The argument name")*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.SgbdEntity.GetArgumentType "Link to this definition")  
Returns the argument type of this SGBD entity argument name

Parameters:  argumentName : str[¶](#tts.core.api.dataBrowserApi.DataBrowser.SgbdEntity.GetArgumentType.argumentName "Permalink to this definition")  
The argument name

Returns:  The argument type

Return type:  str

GetArguments()[¶](#tts.core.api.dataBrowserApi.DataBrowser.SgbdEntity.GetArguments "Link to this definition")  
Returns the arguments of this SGBD entity

Returns:  The arguments

Return type:  list \<str\>

Info

prototype

GetDescription()[¶](#tts.core.api.dataBrowserApi.DataBrowser.SgbdEntity.GetDescription "Link to this definition")  
Returns the description of this SGBD entity

Returns:  The description

Return type:  str

Info

prototype

GetName()[¶](#tts.core.api.dataBrowserApi.DataBrowser.SgbdEntity.GetName "Link to this definition")  
Returns the name of this SGBD entity

Returns:  The name

Return type:  str

Info

prototype

GetResultType(*[resultName](#tts.core.api.dataBrowserApi.DataBrowser.SgbdEntity.GetResultType.resultName "tts.core.api.dataBrowserApi.DataBrowser.SgbdEntity.GetResultType.resultName (Python parameter) — The result name")*)[¶](#tts.core.api.dataBrowserApi.DataBrowser.SgbdEntity.GetResultType "Link to this definition")  
Returns the result type of this SGBD entity result name

Parameters:  resultName : str[¶](#tts.core.api.dataBrowserApi.DataBrowser.SgbdEntity.GetResultType.resultName "Permalink to this definition")  
The result name

Returns:  The result type

Return type:  str

GetResults()[¶](#tts.core.api.dataBrowserApi.DataBrowser.SgbdEntity.GetResults "Link to this definition")  
Returns the results of this SGBD entity

Returns:  The results

Return type:  list \<str\>

Info

prototype

## UnitInfo[¶](#unitinfo "Link to this heading")

### UnitInfo[¶](#module-tts.core.api.dataBrowserApi.UnitInfo "Link to this heading")

*class* UnitInfo[¶](#tts.core.api.dataBrowserApi.UnitInfo.UnitInfo "Link to this definition")  
UnitInfo provides functions to retrieve information concerning unit definitions

Convert(*[value](#tts.core.api.dataBrowserApi.UnitInfo.UnitInfo.Convert.value "tts.core.api.dataBrowserApi.UnitInfo.UnitInfo.Convert.value (Python parameter) — Numeric value in source unit to be converted")*, *[srcUnit](#tts.core.api.dataBrowserApi.UnitInfo.UnitInfo.Convert.srcUnit "tts.core.api.dataBrowserApi.UnitInfo.UnitInfo.Convert.srcUnit (Python parameter) — Name of source unit")*, *[dstUnit](#tts.core.api.dataBrowserApi.UnitInfo.UnitInfo.Convert.dstUnit "tts.core.api.dataBrowserApi.UnitInfo.UnitInfo.Convert.dstUnit (Python parameter) — Name of destination unit")*)[¶](#tts.core.api.dataBrowserApi.UnitInfo.UnitInfo.Convert "Link to this definition")  
Converts the given value from a source unit into the destination unit

Info

A unitless size (noUnit) cannot be converted.

Parameters:  value : float[¶](#tts.core.api.dataBrowserApi.UnitInfo.UnitInfo.Convert.value "Permalink to this definition")  
Numeric value in source unit to be converted

srcUnit : str[¶](#tts.core.api.dataBrowserApi.UnitInfo.UnitInfo.Convert.srcUnit "Permalink to this definition")  
Name of source unit

dstUnit : str[¶](#tts.core.api.dataBrowserApi.UnitInfo.UnitInfo.Convert.dstUnit "Permalink to this definition")  
Name of destination unit

Returns:  Converted numeric value in destination unit, or None, if not convertable

Return type:  float or None

GetDimension(*[unitString](#tts.core.api.dataBrowserApi.UnitInfo.UnitInfo.GetDimension.unitString "tts.core.api.dataBrowserApi.UnitInfo.UnitInfo.GetDimension.unitString (Python parameter) — Name of unit")*)[¶](#tts.core.api.dataBrowserApi.UnitInfo.UnitInfo.GetDimension "Link to this definition")  
Provides the dimension of a unit

Parameters:  unitString : str[¶](#tts.core.api.dataBrowserApi.UnitInfo.UnitInfo.GetDimension.unitString "Permalink to this definition")  
Name of unit

Returns:  Dimension or None if unit unknown

Return type:  str or None

HasUnit(*[unitString](#tts.core.api.dataBrowserApi.UnitInfo.UnitInfo.HasUnit.unitString "tts.core.api.dataBrowserApi.UnitInfo.UnitInfo.HasUnit.unitString (Python parameter) — Name of unit")*)[¶](#tts.core.api.dataBrowserApi.UnitInfo.UnitInfo.HasUnit "Link to this definition")  
Checks whether the unit is defined in the units definition file

Parameters:  unitString : str[¶](#tts.core.api.dataBrowserApi.UnitInfo.UnitInfo.HasUnit.unitString "Permalink to this definition")  
Name of unit

Returns:  True or False

Return type:  bool

