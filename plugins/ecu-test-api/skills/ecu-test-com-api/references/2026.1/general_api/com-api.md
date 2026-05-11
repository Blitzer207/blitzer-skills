[ Internal APIs ](api.md)

[ Advanced operations of package variable types ](variabledatastructures.md)

[ Advanced properties of bus-related objects ](busdatastructures.md)

[ Bus related objects of trace analysis ](busdatastructuresTraceanalysis.md)

[ Advanced properties of diagnostics-related objects ](diagdatastructures.md)

[ Diagnostics related objects of trace analysis ](diagdatastructuresTraceanalysis.md)

[ Advanced properties of media-related objects ](mediadatastructures.md)

[ Advanced properties of DLT logging-related objects ](dltdatastructures.md)

COM API [ COM API ](#)

COM API

- [ COMApplication_ET ](#comapplication-et)
  - [C COMApplication_ET ](#tts.core.api.comApi.Comserver_ET.COMApplication_ET)
    - [A Caches ](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.Caches)
    - [A Packages ](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.Packages)
    - [A Projects ](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.Projects)
    - [A StartTimeout ](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.StartTimeout)
    - [M ClosePackage ](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.ClosePackage)
    - [M CloseProject ](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.CloseProject)
    - [M Exit ](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.Exit)
    - [M GeneratePackageDocumentation ](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.GeneratePackageDocumentation)
    - [M GetAnalysisEnvironment ](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.GetAnalysisEnvironment)
    - [M GetCaches ](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.GetCaches)
    - [M GetCurrentTestConfiguration ](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.GetCurrentTestConfiguration)
    - [M GetCurrentTestbenchConfiguration ](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.GetCurrentTestbenchConfiguration)
    - [M GetInstallDir ](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.GetInstallDir)
    - [M GetKeywordCatalogModule ](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.GetKeywordCatalogModule)
    - [M GetLoadedPatches ](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.GetLoadedPatches)
    - [M GetObjectApiPythonPath ](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.GetObjectApiPythonPath)
    - [M GetPackages ](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.GetPackages)
    - [M GetProjects ](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.GetProjects)
    - [M GetSetting ](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.GetSetting)
    - [M GetTestEnvironment ](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.GetTestEnvironment)
    - [M GetTestManagementModule ](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.GetTestManagementModule)
    - [M GetVersion ](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.GetVersion)
    - [M HasActiveTasks ](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.HasActiveTasks)
    - [M IconizeMainFrame ](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.IconizeMainFrame)
    - [M IsApplicationRunning ](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.IsApplicationRunning)
    - [M IsStarted ](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.IsStarted)
    - [M IsXmlRpcApiBusy ](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.IsXmlRpcApiBusy)
    - [M LoadGlobalMapping ](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.LoadGlobalMapping)
    - [M MaximizeMainFrame ](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.MaximizeMainFrame)
    - [M OpenPackage ](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.OpenPackage)
    - [M OpenProject ](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.OpenProject)
    - [M OpenTestConfiguration ](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.OpenTestConfiguration)
    - [M OpenTestbenchConfiguration ](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.OpenTestbenchConfiguration)
    - [M Quit ](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.Quit)
    - [M RunApplication ](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.RunApplication)
    - [M Start ](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.Start)
    - [M Stop ](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.Stop)
    - [M UnloadGlobalMapping ](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.UnloadGlobalMapping)
    - [M UpdateUserLibraries ](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.UpdateUserLibraries)
    - [M WaitForIdle ](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.WaitForIdle)
- [ COMAnalysisEnvironment ](#comanalysisenvironment)
  - [C COMAnalysisEnvironment ](#tts.core.api.comApi.Comserver.COMAnalysisEnvironment)
    - [M ExecuteJob ](#tts.core.api.comApi.Comserver.COMAnalysisEnvironment.ExecuteJob)
    - [M GetAnalysisExecutionInfo ](#tts.core.api.comApi.Comserver.COMAnalysisEnvironment.GetAnalysisExecutionInfo)
    - [M MergeJobReports ](#tts.core.api.comApi.Comserver.COMAnalysisEnvironment.MergeJobReports)
- [ COMAnalysisExecutionInfo ](#comanalysisexecutioninfo)
  - [C COMAnalysisExecutionInfo ](#tts.core.api.comApi.Comserver.COMAnalysisExecutionInfo)
    - [M Abort ](#tts.core.api.comApi.Comserver.COMAnalysisExecutionInfo.Abort)
    - [M GetLogFolder ](#tts.core.api.comApi.Comserver.COMAnalysisExecutionInfo.GetLogFolder)
    - [M GetReportDb ](#tts.core.api.comApi.Comserver.COMAnalysisExecutionInfo.GetReportDb)
    - [M GetResult ](#tts.core.api.comApi.Comserver.COMAnalysisExecutionInfo.GetResult)
    - [M GetStartTime ](#tts.core.api.comApi.Comserver.COMAnalysisExecutionInfo.GetStartTime)
    - [M GetState ](#tts.core.api.comApi.Comserver.COMAnalysisExecutionInfo.GetState)
    - [M WaitForTestexecutionCompletion ](#tts.core.api.comApi.Comserver.COMAnalysisExecutionInfo.WaitForTestexecutionCompletion)
- [ COMCache ](#comcache)
  - [C COMCache ](#tts.core.api.comApi.Comserver.COMCache)
    - [M Clear ](#tts.core.api.comApi.Comserver.COMCache.Clear)
    - [M GetFiles ](#tts.core.api.comApi.Comserver.COMCache.GetFiles)
    - [M Insert ](#tts.core.api.comApi.Comserver.COMCache.Insert)
- [ COMCaches ](#comcaches)
  - [C COMCaches ](#tts.core.api.comApi.Comserver.COMCaches)
    - [M GetA2lCache ](#tts.core.api.comApi.Comserver.COMCaches.GetA2lCache)
    - [M GetBusCache ](#tts.core.api.comApi.Comserver.COMCaches.GetBusCache)
    - [M GetElfCache ](#tts.core.api.comApi.Comserver.COMCaches.GetElfCache)
    - [M GetModelCache ](#tts.core.api.comApi.Comserver.COMCaches.GetModelCache)
    - [M GetServiceCache ](#tts.core.api.comApi.Comserver.COMCaches.GetServiceCache)
- [ COMConstant ](#comconstant)
  - [C COMConstant ](#tts.core.api.comApi.Comserver.COMConstant)
    - [A Description ](#tts.core.api.comApi.Comserver.COMConstant.Description)
    - [A Name ](#tts.core.api.comApi.Comserver.COMConstant.Name)
    - [A Value ](#tts.core.api.comApi.Comserver.COMConstant.Value)
    - [M GetDescription ](#tts.core.api.comApi.Comserver.COMConstant.GetDescription)
    - [M GetName ](#tts.core.api.comApi.Comserver.COMConstant.GetName)
    - [M GetValue ](#tts.core.api.comApi.Comserver.COMConstant.GetValue)
- [ COMConstants ](#comconstants)
  - [C COMConstants ](#tts.core.api.comApi.Comserver.COMConstants)
    - [A Count ](#tts.core.api.comApi.Comserver.COMConstants.Count)
    - [M GetCount ](#tts.core.api.comApi.Comserver.COMConstants.GetCount)
    - [M Item ](#tts.core.api.comApi.Comserver.COMConstants.Item)
- [ COMKeywordCatalog ](#comkeywordcatalog)
  - [C COMKeywordCatalog ](#tts.core.api.comApi.Comserver.COMKeywordCatalog)
    - [M Connect ](#tts.core.api.comApi.Comserver.COMKeywordCatalog.Connect)
    - [M GetAvailableCatalogs ](#tts.core.api.comApi.Comserver.COMKeywordCatalog.GetAvailableCatalogs)
    - [M GetAvailableProjects ](#tts.core.api.comApi.Comserver.COMKeywordCatalog.GetAvailableProjects)
    - [M GetAvailableVariants ](#tts.core.api.comApi.Comserver.COMKeywordCatalog.GetAvailableVariants)
    - [M GetCurrentCatalogName ](#tts.core.api.comApi.Comserver.COMKeywordCatalog.GetCurrentCatalogName)
    - [M GetCurrentProject ](#tts.core.api.comApi.Comserver.COMKeywordCatalog.GetCurrentProject)
    - [M GetCurrentVariant ](#tts.core.api.comApi.Comserver.COMKeywordCatalog.GetCurrentVariant)
    - [M IsConnected ](#tts.core.api.comApi.Comserver.COMKeywordCatalog.IsConnected)
    - [M LoadCatalog ](#tts.core.api.comApi.Comserver.COMKeywordCatalog.LoadCatalog)
    - [M SetProject ](#tts.core.api.comApi.Comserver.COMKeywordCatalog.SetProject)
    - [M SetVariant ](#tts.core.api.comApi.Comserver.COMKeywordCatalog.SetVariant)
- [ COMPackage ](#compackage)
  - [C COMPackage ](#tts.core.api.comApi.Comserver.COMPackage)
    - [A Description ](#tts.core.api.comApi.Comserver.COMPackage.Description)
    - [A Filename ](#tts.core.api.comApi.Comserver.COMPackage.Filename)
    - [A Name ](#tts.core.api.comApi.Comserver.COMPackage.Name)
    - [A Variables ](#tts.core.api.comApi.Comserver.COMPackage.Variables)
    - [M Check ](#tts.core.api.comApi.Comserver.COMPackage.Check)
    - [M CheckNG ](#tts.core.api.comApi.Comserver.COMPackage.CheckNG)
    - [M GetDescription ](#tts.core.api.comApi.Comserver.COMPackage.GetDescription)
    - [M GetFilename ](#tts.core.api.comApi.Comserver.COMPackage.GetFilename)
    - [M GetName ](#tts.core.api.comApi.Comserver.COMPackage.GetName)
    - [M GetVariables ](#tts.core.api.comApi.Comserver.COMPackage.GetVariables)
- [ COMPackages ](#compackages)
  - [C COMPackages ](#tts.core.api.comApi.Comserver.COMPackages)
    - [A Count ](#tts.core.api.comApi.Comserver.COMPackages.Count)
    - [M GetCount ](#tts.core.api.comApi.Comserver.COMPackages.GetCount)
    - [M Item ](#tts.core.api.comApi.Comserver.COMPackages.Item)
- [ COMProject ](#comproject)
  - [C COMProject ](#tts.core.api.comApi.Comserver.COMProject)
    - [A Filename ](#tts.core.api.comApi.Comserver.COMProject.Filename)
    - [A Packages ](#tts.core.api.comApi.Comserver.COMProject.Packages)
    - [M Check ](#tts.core.api.comApi.Comserver.COMProject.Check)
    - [M CheckNG ](#tts.core.api.comApi.Comserver.COMProject.CheckNG)
    - [M GetFilename ](#tts.core.api.comApi.Comserver.COMProject.GetFilename)
    - [M GetPackages ](#tts.core.api.comApi.Comserver.COMProject.GetPackages)
- [ COMProjects ](#comprojects)
  - [C COMProjects ](#tts.core.api.comApi.Comserver.COMProjects)
    - [A Count ](#tts.core.api.comApi.Comserver.COMProjects.Count)
    - [M GetCount ](#tts.core.api.comApi.Comserver.COMProjects.GetCount)
    - [M Item ](#tts.core.api.comApi.Comserver.COMProjects.Item)
- [ COMTestbenchConfiguration ](#comtestbenchconfiguration)
  - [C COMTestbenchConfiguration ](#tts.core.api.comApi.Comserver_ET.COMTestbenchConfiguration)
    - [M GetFilename ](#tts.core.api.comApi.Comserver_ET.COMTestbenchConfiguration.GetFilename)
    - [M GetToolhostInfo ](#tts.core.api.comApi.Comserver_ET.COMTestbenchConfiguration.GetToolhostInfo)
- [ COMTestConfiguration ](#comtestconfiguration)
  - [C COMTestConfiguration ](#tts.core.api.comApi.Comserver.COMTestConfiguration)
    - [A Filename ](#tts.core.api.comApi.Comserver.COMTestConfiguration.Filename)
    - [A GlobalConstants ](#tts.core.api.comApi.Comserver.COMTestConfiguration.GlobalConstants)
    - [M GetFilename ](#tts.core.api.comApi.Comserver.COMTestConfiguration.GetFilename)
    - [M GetGlobalConstants ](#tts.core.api.comApi.Comserver.COMTestConfiguration.GetGlobalConstants)
    - [M SetGlobalConstant ](#tts.core.api.comApi.Comserver.COMTestConfiguration.SetGlobalConstant)
    - [M SetReportBaseFolder ](#tts.core.api.comApi.Comserver.COMTestConfiguration.SetReportBaseFolder)
- [ COMTestEnvironment ](#comtestenvironment)
  - [C COMTestEnvironment ](#tts.core.api.comApi.Comserver.COMTestEnvironment)
    - [M ExecutePackage ](#tts.core.api.comApi.Comserver.COMTestEnvironment.ExecutePackage)
    - [M ExecuteProject ](#tts.core.api.comApi.Comserver.COMTestEnvironment.ExecuteProject)
    - [M ExecuteProjectArchive ](#tts.core.api.comApi.Comserver.COMTestEnvironment.ExecuteProjectArchive)
    - [M GenerateTestReportDocument ](#tts.core.api.comApi.Comserver.COMTestEnvironment.GenerateTestReportDocument)
    - [M GenerateTestReportDocumentFromDB ](#tts.core.api.comApi.Comserver.COMTestEnvironment.GenerateTestReportDocumentFromDB)
    - [M GetTestExecutionInfo ](#tts.core.api.comApi.Comserver.COMTestEnvironment.GetTestExecutionInfo)
- [ COMTestExecutionInfo ](#comtestexecutioninfo)
  - [C COMTestExecutionInfo ](#tts.core.api.comApi.Comserver.COMTestExecutionInfo)
    - [A TestReport ](#tts.core.api.comApi.Comserver.COMTestExecutionInfo.TestReport)
    - [M Abort ](#tts.core.api.comApi.Comserver.COMTestExecutionInfo.Abort)
    - [M AbortAfterCurrentProjectStep ](#tts.core.api.comApi.Comserver.COMTestExecutionInfo.AbortAfterCurrentProjectStep)
    - [M GenerateTestReportDocument ](#tts.core.api.comApi.Comserver.COMTestExecutionInfo.GenerateTestReportDocument)
    - [M GetLogFolder ](#tts.core.api.comApi.Comserver.COMTestExecutionInfo.GetLogFolder)
    - [M GetPackageAbortCode ](#tts.core.api.comApi.Comserver.COMTestExecutionInfo.GetPackageAbortCode)
    - [M GetPackageAbortComment ](#tts.core.api.comApi.Comserver.COMTestExecutionInfo.GetPackageAbortComment)
    - [M GetReportDb ](#tts.core.api.comApi.Comserver.COMTestExecutionInfo.GetReportDb)
    - [M GetResult ](#tts.core.api.comApi.Comserver.COMTestExecutionInfo.GetResult)
    - [M GetReturnValue ](#tts.core.api.comApi.Comserver.COMTestExecutionInfo.GetReturnValue)
    - [M GetStartTime ](#tts.core.api.comApi.Comserver.COMTestExecutionInfo.GetStartTime)
    - [M GetState ](#tts.core.api.comApi.Comserver.COMTestExecutionInfo.GetState)
    - [M GetTestReport ](#tts.core.api.comApi.Comserver.COMTestExecutionInfo.GetTestReport)
    - [M WaitForTestexecutionCompletion ](#tts.core.api.comApi.Comserver.COMTestExecutionInfo.WaitForTestexecutionCompletion)
- [ COMTestManagement ](#comtestmanagement)
  - [C COMTestManagement ](#tts.core.api.comApi.Comserver.COMTestManagement)
    - [M ExportPackage ](#tts.core.api.comApi.Comserver.COMTestManagement.ExportPackage)
    - [M ExportPackageAttributes ](#tts.core.api.comApi.Comserver.COMTestManagement.ExportPackageAttributes)
    - [M ExportPackageChanges ](#tts.core.api.comApi.Comserver.COMTestManagement.ExportPackageChanges)
    - [M ExportProject ](#tts.core.api.comApi.Comserver.COMTestManagement.ExportProject)
    - [M ExportProjectAttributes ](#tts.core.api.comApi.Comserver.COMTestManagement.ExportProjectAttributes)
    - [M ExportReport ](#tts.core.api.comApi.Comserver.COMTestManagement.ExportReport)
    - [M GetActiveConfigurationName ](#tts.core.api.comApi.Comserver.COMTestManagement.GetActiveConfigurationName)
    - [M GetConfigurationNames ](#tts.core.api.comApi.Comserver.COMTestManagement.GetConfigurationNames)
    - [M ImportPackage ](#tts.core.api.comApi.Comserver.COMTestManagement.ImportPackage)
    - [M ImportPackageAttributes ](#tts.core.api.comApi.Comserver.COMTestManagement.ImportPackageAttributes)
    - [M ImportPackageById ](#tts.core.api.comApi.Comserver.COMTestManagement.ImportPackageById)
    - [M ImportPackageDirectory ](#tts.core.api.comApi.Comserver.COMTestManagement.ImportPackageDirectory)
    - [M ImportProject ](#tts.core.api.comApi.Comserver.COMTestManagement.ImportProject)
    - [M ImportProjectAttributes ](#tts.core.api.comApi.Comserver.COMTestManagement.ImportProjectAttributes)
    - [M ImportProjectById ](#tts.core.api.comApi.Comserver.COMTestManagement.ImportProjectById)
    - [M ImportProjectDirectory ](#tts.core.api.comApi.Comserver.COMTestManagement.ImportProjectDirectory)
    - [M IsLoggedIn ](#tts.core.api.comApi.Comserver.COMTestManagement.IsLoggedIn)
    - [M IsTmsAvailable ](#tts.core.api.comApi.Comserver.COMTestManagement.IsTmsAvailable)
    - [M LinkAndSyncProject ](#tts.core.api.comApi.Comserver.COMTestManagement.LinkAndSyncProject)
    - [M Login ](#tts.core.api.comApi.Comserver.COMTestManagement.Login)
    - [M Logout ](#tts.core.api.comApi.Comserver.COMTestManagement.Logout)
    - [M SetActiveConfiguration ](#tts.core.api.comApi.Comserver.COMTestManagement.SetActiveConfiguration)
    - [M UpdateAttributeDefinitions ](#tts.core.api.comApi.Comserver.COMTestManagement.UpdateAttributeDefinitions)
- [ COMTestReport ](#comtestreport)
  - [C COMTestReport ](#tts.core.api.comApi.Comserver.COMTestReport)
    - [A Count ](#tts.core.api.comApi.Comserver.COMTestReport.Count)
    - [M Activity ](#tts.core.api.comApi.Comserver.COMTestReport.Activity)
    - [M Comment ](#tts.core.api.comApi.Comserver.COMTestReport.Comment)
    - [M GetAnalysisJobFiles ](#tts.core.api.comApi.Comserver.COMTestReport.GetAnalysisJobFiles)
    - [M GetCount ](#tts.core.api.comApi.Comserver.COMTestReport.GetCount)
    - [M Index ](#tts.core.api.comApi.Comserver.COMTestReport.Index)
    - [M Info ](#tts.core.api.comApi.Comserver.COMTestReport.Info)
    - [M IsOk ](#tts.core.api.comApi.Comserver.COMTestReport.IsOk)
    - [M Item ](#tts.core.api.comApi.Comserver.COMTestReport.Item)
    - [M Name ](#tts.core.api.comApi.Comserver.COMTestReport.Name)
    - [M Result ](#tts.core.api.comApi.Comserver.COMTestReport.Result)
    - [M TimeStamp ](#tts.core.api.comApi.Comserver.COMTestReport.TimeStamp)
- [ COMVariable ](#comvariable)
  - [C COMVariable ](#tts.core.api.comApi.Comserver.COMVariable)
    - [A Description ](#tts.core.api.comApi.Comserver.COMVariable.Description)
    - [A InitValue ](#tts.core.api.comApi.Comserver.COMVariable.InitValue)
    - [A Name ](#tts.core.api.comApi.Comserver.COMVariable.Name)
    - [M GetDescription ](#tts.core.api.comApi.Comserver.COMVariable.GetDescription)
    - [M GetInitValue ](#tts.core.api.comApi.Comserver.COMVariable.GetInitValue)
    - [M GetName ](#tts.core.api.comApi.Comserver.COMVariable.GetName)
    - [M IsInput ](#tts.core.api.comApi.Comserver.COMVariable.IsInput)
    - [M IsOutput ](#tts.core.api.comApi.Comserver.COMVariable.IsOutput)
- [ COMVariables ](#comvariables)
  - [C COMVariables ](#tts.core.api.comApi.Comserver.COMVariables)
    - [A Count ](#tts.core.api.comApi.Comserver.COMVariables.Count)
    - [M GetCount ](#tts.core.api.comApi.Comserver.COMVariables.GetCount)
    - [M Item ](#tts.core.api.comApi.Comserver.COMVariables.Item)

[ REST API ](rest-api.md)

[ Report API ](apireport.md)

[ Object API ](objectApi.md)

[ Trace Analysis API ](../TraceAnalysisAPI/index.md)

[ Generator APIs ](../generators/index.md)

[ Tools ](../tools/index.md)

[ User test management ](../userTestmanagement/index.md)

[ UserUtility API ](../user-utility/user-utility.md)

[ Utility Examples ](../user-utility/example-utilities.md)

COM API

- [ COMApplication_ET ](#comapplication-et)
  - [C COMApplication_ET ](#tts.core.api.comApi.Comserver_ET.COMApplication_ET)
    - [A Caches ](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.Caches)
    - [A Packages ](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.Packages)
    - [A Projects ](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.Projects)
    - [A StartTimeout ](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.StartTimeout)
    - [M ClosePackage ](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.ClosePackage)
    - [M CloseProject ](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.CloseProject)
    - [M Exit ](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.Exit)
    - [M GeneratePackageDocumentation ](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.GeneratePackageDocumentation)
    - [M GetAnalysisEnvironment ](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.GetAnalysisEnvironment)
    - [M GetCaches ](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.GetCaches)
    - [M GetCurrentTestConfiguration ](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.GetCurrentTestConfiguration)
    - [M GetCurrentTestbenchConfiguration ](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.GetCurrentTestbenchConfiguration)
    - [M GetInstallDir ](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.GetInstallDir)
    - [M GetKeywordCatalogModule ](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.GetKeywordCatalogModule)
    - [M GetLoadedPatches ](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.GetLoadedPatches)
    - [M GetObjectApiPythonPath ](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.GetObjectApiPythonPath)
    - [M GetPackages ](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.GetPackages)
    - [M GetProjects ](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.GetProjects)
    - [M GetSetting ](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.GetSetting)
    - [M GetTestEnvironment ](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.GetTestEnvironment)
    - [M GetTestManagementModule ](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.GetTestManagementModule)
    - [M GetVersion ](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.GetVersion)
    - [M HasActiveTasks ](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.HasActiveTasks)
    - [M IconizeMainFrame ](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.IconizeMainFrame)
    - [M IsApplicationRunning ](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.IsApplicationRunning)
    - [M IsStarted ](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.IsStarted)
    - [M IsXmlRpcApiBusy ](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.IsXmlRpcApiBusy)
    - [M LoadGlobalMapping ](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.LoadGlobalMapping)
    - [M MaximizeMainFrame ](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.MaximizeMainFrame)
    - [M OpenPackage ](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.OpenPackage)
    - [M OpenProject ](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.OpenProject)
    - [M OpenTestConfiguration ](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.OpenTestConfiguration)
    - [M OpenTestbenchConfiguration ](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.OpenTestbenchConfiguration)
    - [M Quit ](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.Quit)
    - [M RunApplication ](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.RunApplication)
    - [M Start ](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.Start)
    - [M Stop ](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.Stop)
    - [M UnloadGlobalMapping ](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.UnloadGlobalMapping)
    - [M UpdateUserLibraries ](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.UpdateUserLibraries)
    - [M WaitForIdle ](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.WaitForIdle)
- [ COMAnalysisEnvironment ](#comanalysisenvironment)
  - [C COMAnalysisEnvironment ](#tts.core.api.comApi.Comserver.COMAnalysisEnvironment)
    - [M ExecuteJob ](#tts.core.api.comApi.Comserver.COMAnalysisEnvironment.ExecuteJob)
    - [M GetAnalysisExecutionInfo ](#tts.core.api.comApi.Comserver.COMAnalysisEnvironment.GetAnalysisExecutionInfo)
    - [M MergeJobReports ](#tts.core.api.comApi.Comserver.COMAnalysisEnvironment.MergeJobReports)
- [ COMAnalysisExecutionInfo ](#comanalysisexecutioninfo)
  - [C COMAnalysisExecutionInfo ](#tts.core.api.comApi.Comserver.COMAnalysisExecutionInfo)
    - [M Abort ](#tts.core.api.comApi.Comserver.COMAnalysisExecutionInfo.Abort)
    - [M GetLogFolder ](#tts.core.api.comApi.Comserver.COMAnalysisExecutionInfo.GetLogFolder)
    - [M GetReportDb ](#tts.core.api.comApi.Comserver.COMAnalysisExecutionInfo.GetReportDb)
    - [M GetResult ](#tts.core.api.comApi.Comserver.COMAnalysisExecutionInfo.GetResult)
    - [M GetStartTime ](#tts.core.api.comApi.Comserver.COMAnalysisExecutionInfo.GetStartTime)
    - [M GetState ](#tts.core.api.comApi.Comserver.COMAnalysisExecutionInfo.GetState)
    - [M WaitForTestexecutionCompletion ](#tts.core.api.comApi.Comserver.COMAnalysisExecutionInfo.WaitForTestexecutionCompletion)
- [ COMCache ](#comcache)
  - [C COMCache ](#tts.core.api.comApi.Comserver.COMCache)
    - [M Clear ](#tts.core.api.comApi.Comserver.COMCache.Clear)
    - [M GetFiles ](#tts.core.api.comApi.Comserver.COMCache.GetFiles)
    - [M Insert ](#tts.core.api.comApi.Comserver.COMCache.Insert)
- [ COMCaches ](#comcaches)
  - [C COMCaches ](#tts.core.api.comApi.Comserver.COMCaches)
    - [M GetA2lCache ](#tts.core.api.comApi.Comserver.COMCaches.GetA2lCache)
    - [M GetBusCache ](#tts.core.api.comApi.Comserver.COMCaches.GetBusCache)
    - [M GetElfCache ](#tts.core.api.comApi.Comserver.COMCaches.GetElfCache)
    - [M GetModelCache ](#tts.core.api.comApi.Comserver.COMCaches.GetModelCache)
    - [M GetServiceCache ](#tts.core.api.comApi.Comserver.COMCaches.GetServiceCache)
- [ COMConstant ](#comconstant)
  - [C COMConstant ](#tts.core.api.comApi.Comserver.COMConstant)
    - [A Description ](#tts.core.api.comApi.Comserver.COMConstant.Description)
    - [A Name ](#tts.core.api.comApi.Comserver.COMConstant.Name)
    - [A Value ](#tts.core.api.comApi.Comserver.COMConstant.Value)
    - [M GetDescription ](#tts.core.api.comApi.Comserver.COMConstant.GetDescription)
    - [M GetName ](#tts.core.api.comApi.Comserver.COMConstant.GetName)
    - [M GetValue ](#tts.core.api.comApi.Comserver.COMConstant.GetValue)
- [ COMConstants ](#comconstants)
  - [C COMConstants ](#tts.core.api.comApi.Comserver.COMConstants)
    - [A Count ](#tts.core.api.comApi.Comserver.COMConstants.Count)
    - [M GetCount ](#tts.core.api.comApi.Comserver.COMConstants.GetCount)
    - [M Item ](#tts.core.api.comApi.Comserver.COMConstants.Item)
- [ COMKeywordCatalog ](#comkeywordcatalog)
  - [C COMKeywordCatalog ](#tts.core.api.comApi.Comserver.COMKeywordCatalog)
    - [M Connect ](#tts.core.api.comApi.Comserver.COMKeywordCatalog.Connect)
    - [M GetAvailableCatalogs ](#tts.core.api.comApi.Comserver.COMKeywordCatalog.GetAvailableCatalogs)
    - [M GetAvailableProjects ](#tts.core.api.comApi.Comserver.COMKeywordCatalog.GetAvailableProjects)
    - [M GetAvailableVariants ](#tts.core.api.comApi.Comserver.COMKeywordCatalog.GetAvailableVariants)
    - [M GetCurrentCatalogName ](#tts.core.api.comApi.Comserver.COMKeywordCatalog.GetCurrentCatalogName)
    - [M GetCurrentProject ](#tts.core.api.comApi.Comserver.COMKeywordCatalog.GetCurrentProject)
    - [M GetCurrentVariant ](#tts.core.api.comApi.Comserver.COMKeywordCatalog.GetCurrentVariant)
    - [M IsConnected ](#tts.core.api.comApi.Comserver.COMKeywordCatalog.IsConnected)
    - [M LoadCatalog ](#tts.core.api.comApi.Comserver.COMKeywordCatalog.LoadCatalog)
    - [M SetProject ](#tts.core.api.comApi.Comserver.COMKeywordCatalog.SetProject)
    - [M SetVariant ](#tts.core.api.comApi.Comserver.COMKeywordCatalog.SetVariant)
- [ COMPackage ](#compackage)
  - [C COMPackage ](#tts.core.api.comApi.Comserver.COMPackage)
    - [A Description ](#tts.core.api.comApi.Comserver.COMPackage.Description)
    - [A Filename ](#tts.core.api.comApi.Comserver.COMPackage.Filename)
    - [A Name ](#tts.core.api.comApi.Comserver.COMPackage.Name)
    - [A Variables ](#tts.core.api.comApi.Comserver.COMPackage.Variables)
    - [M Check ](#tts.core.api.comApi.Comserver.COMPackage.Check)
    - [M CheckNG ](#tts.core.api.comApi.Comserver.COMPackage.CheckNG)
    - [M GetDescription ](#tts.core.api.comApi.Comserver.COMPackage.GetDescription)
    - [M GetFilename ](#tts.core.api.comApi.Comserver.COMPackage.GetFilename)
    - [M GetName ](#tts.core.api.comApi.Comserver.COMPackage.GetName)
    - [M GetVariables ](#tts.core.api.comApi.Comserver.COMPackage.GetVariables)
- [ COMPackages ](#compackages)
  - [C COMPackages ](#tts.core.api.comApi.Comserver.COMPackages)
    - [A Count ](#tts.core.api.comApi.Comserver.COMPackages.Count)
    - [M GetCount ](#tts.core.api.comApi.Comserver.COMPackages.GetCount)
    - [M Item ](#tts.core.api.comApi.Comserver.COMPackages.Item)
- [ COMProject ](#comproject)
  - [C COMProject ](#tts.core.api.comApi.Comserver.COMProject)
    - [A Filename ](#tts.core.api.comApi.Comserver.COMProject.Filename)
    - [A Packages ](#tts.core.api.comApi.Comserver.COMProject.Packages)
    - [M Check ](#tts.core.api.comApi.Comserver.COMProject.Check)
    - [M CheckNG ](#tts.core.api.comApi.Comserver.COMProject.CheckNG)
    - [M GetFilename ](#tts.core.api.comApi.Comserver.COMProject.GetFilename)
    - [M GetPackages ](#tts.core.api.comApi.Comserver.COMProject.GetPackages)
- [ COMProjects ](#comprojects)
  - [C COMProjects ](#tts.core.api.comApi.Comserver.COMProjects)
    - [A Count ](#tts.core.api.comApi.Comserver.COMProjects.Count)
    - [M GetCount ](#tts.core.api.comApi.Comserver.COMProjects.GetCount)
    - [M Item ](#tts.core.api.comApi.Comserver.COMProjects.Item)
- [ COMTestbenchConfiguration ](#comtestbenchconfiguration)
  - [C COMTestbenchConfiguration ](#tts.core.api.comApi.Comserver_ET.COMTestbenchConfiguration)
    - [M GetFilename ](#tts.core.api.comApi.Comserver_ET.COMTestbenchConfiguration.GetFilename)
    - [M GetToolhostInfo ](#tts.core.api.comApi.Comserver_ET.COMTestbenchConfiguration.GetToolhostInfo)
- [ COMTestConfiguration ](#comtestconfiguration)
  - [C COMTestConfiguration ](#tts.core.api.comApi.Comserver.COMTestConfiguration)
    - [A Filename ](#tts.core.api.comApi.Comserver.COMTestConfiguration.Filename)
    - [A GlobalConstants ](#tts.core.api.comApi.Comserver.COMTestConfiguration.GlobalConstants)
    - [M GetFilename ](#tts.core.api.comApi.Comserver.COMTestConfiguration.GetFilename)
    - [M GetGlobalConstants ](#tts.core.api.comApi.Comserver.COMTestConfiguration.GetGlobalConstants)
    - [M SetGlobalConstant ](#tts.core.api.comApi.Comserver.COMTestConfiguration.SetGlobalConstant)
    - [M SetReportBaseFolder ](#tts.core.api.comApi.Comserver.COMTestConfiguration.SetReportBaseFolder)
- [ COMTestEnvironment ](#comtestenvironment)
  - [C COMTestEnvironment ](#tts.core.api.comApi.Comserver.COMTestEnvironment)
    - [M ExecutePackage ](#tts.core.api.comApi.Comserver.COMTestEnvironment.ExecutePackage)
    - [M ExecuteProject ](#tts.core.api.comApi.Comserver.COMTestEnvironment.ExecuteProject)
    - [M ExecuteProjectArchive ](#tts.core.api.comApi.Comserver.COMTestEnvironment.ExecuteProjectArchive)
    - [M GenerateTestReportDocument ](#tts.core.api.comApi.Comserver.COMTestEnvironment.GenerateTestReportDocument)
    - [M GenerateTestReportDocumentFromDB ](#tts.core.api.comApi.Comserver.COMTestEnvironment.GenerateTestReportDocumentFromDB)
    - [M GetTestExecutionInfo ](#tts.core.api.comApi.Comserver.COMTestEnvironment.GetTestExecutionInfo)
- [ COMTestExecutionInfo ](#comtestexecutioninfo)
  - [C COMTestExecutionInfo ](#tts.core.api.comApi.Comserver.COMTestExecutionInfo)
    - [A TestReport ](#tts.core.api.comApi.Comserver.COMTestExecutionInfo.TestReport)
    - [M Abort ](#tts.core.api.comApi.Comserver.COMTestExecutionInfo.Abort)
    - [M AbortAfterCurrentProjectStep ](#tts.core.api.comApi.Comserver.COMTestExecutionInfo.AbortAfterCurrentProjectStep)
    - [M GenerateTestReportDocument ](#tts.core.api.comApi.Comserver.COMTestExecutionInfo.GenerateTestReportDocument)
    - [M GetLogFolder ](#tts.core.api.comApi.Comserver.COMTestExecutionInfo.GetLogFolder)
    - [M GetPackageAbortCode ](#tts.core.api.comApi.Comserver.COMTestExecutionInfo.GetPackageAbortCode)
    - [M GetPackageAbortComment ](#tts.core.api.comApi.Comserver.COMTestExecutionInfo.GetPackageAbortComment)
    - [M GetReportDb ](#tts.core.api.comApi.Comserver.COMTestExecutionInfo.GetReportDb)
    - [M GetResult ](#tts.core.api.comApi.Comserver.COMTestExecutionInfo.GetResult)
    - [M GetReturnValue ](#tts.core.api.comApi.Comserver.COMTestExecutionInfo.GetReturnValue)
    - [M GetStartTime ](#tts.core.api.comApi.Comserver.COMTestExecutionInfo.GetStartTime)
    - [M GetState ](#tts.core.api.comApi.Comserver.COMTestExecutionInfo.GetState)
    - [M GetTestReport ](#tts.core.api.comApi.Comserver.COMTestExecutionInfo.GetTestReport)
    - [M WaitForTestexecutionCompletion ](#tts.core.api.comApi.Comserver.COMTestExecutionInfo.WaitForTestexecutionCompletion)
- [ COMTestManagement ](#comtestmanagement)
  - [C COMTestManagement ](#tts.core.api.comApi.Comserver.COMTestManagement)
    - [M ExportPackage ](#tts.core.api.comApi.Comserver.COMTestManagement.ExportPackage)
    - [M ExportPackageAttributes ](#tts.core.api.comApi.Comserver.COMTestManagement.ExportPackageAttributes)
    - [M ExportPackageChanges ](#tts.core.api.comApi.Comserver.COMTestManagement.ExportPackageChanges)
    - [M ExportProject ](#tts.core.api.comApi.Comserver.COMTestManagement.ExportProject)
    - [M ExportProjectAttributes ](#tts.core.api.comApi.Comserver.COMTestManagement.ExportProjectAttributes)
    - [M ExportReport ](#tts.core.api.comApi.Comserver.COMTestManagement.ExportReport)
    - [M GetActiveConfigurationName ](#tts.core.api.comApi.Comserver.COMTestManagement.GetActiveConfigurationName)
    - [M GetConfigurationNames ](#tts.core.api.comApi.Comserver.COMTestManagement.GetConfigurationNames)
    - [M ImportPackage ](#tts.core.api.comApi.Comserver.COMTestManagement.ImportPackage)
    - [M ImportPackageAttributes ](#tts.core.api.comApi.Comserver.COMTestManagement.ImportPackageAttributes)
    - [M ImportPackageById ](#tts.core.api.comApi.Comserver.COMTestManagement.ImportPackageById)
    - [M ImportPackageDirectory ](#tts.core.api.comApi.Comserver.COMTestManagement.ImportPackageDirectory)
    - [M ImportProject ](#tts.core.api.comApi.Comserver.COMTestManagement.ImportProject)
    - [M ImportProjectAttributes ](#tts.core.api.comApi.Comserver.COMTestManagement.ImportProjectAttributes)
    - [M ImportProjectById ](#tts.core.api.comApi.Comserver.COMTestManagement.ImportProjectById)
    - [M ImportProjectDirectory ](#tts.core.api.comApi.Comserver.COMTestManagement.ImportProjectDirectory)
    - [M IsLoggedIn ](#tts.core.api.comApi.Comserver.COMTestManagement.IsLoggedIn)
    - [M IsTmsAvailable ](#tts.core.api.comApi.Comserver.COMTestManagement.IsTmsAvailable)
    - [M LinkAndSyncProject ](#tts.core.api.comApi.Comserver.COMTestManagement.LinkAndSyncProject)
    - [M Login ](#tts.core.api.comApi.Comserver.COMTestManagement.Login)
    - [M Logout ](#tts.core.api.comApi.Comserver.COMTestManagement.Logout)
    - [M SetActiveConfiguration ](#tts.core.api.comApi.Comserver.COMTestManagement.SetActiveConfiguration)
    - [M UpdateAttributeDefinitions ](#tts.core.api.comApi.Comserver.COMTestManagement.UpdateAttributeDefinitions)
- [ COMTestReport ](#comtestreport)
  - [C COMTestReport ](#tts.core.api.comApi.Comserver.COMTestReport)
    - [A Count ](#tts.core.api.comApi.Comserver.COMTestReport.Count)
    - [M Activity ](#tts.core.api.comApi.Comserver.COMTestReport.Activity)
    - [M Comment ](#tts.core.api.comApi.Comserver.COMTestReport.Comment)
    - [M GetAnalysisJobFiles ](#tts.core.api.comApi.Comserver.COMTestReport.GetAnalysisJobFiles)
    - [M GetCount ](#tts.core.api.comApi.Comserver.COMTestReport.GetCount)
    - [M Index ](#tts.core.api.comApi.Comserver.COMTestReport.Index)
    - [M Info ](#tts.core.api.comApi.Comserver.COMTestReport.Info)
    - [M IsOk ](#tts.core.api.comApi.Comserver.COMTestReport.IsOk)
    - [M Item ](#tts.core.api.comApi.Comserver.COMTestReport.Item)
    - [M Name ](#tts.core.api.comApi.Comserver.COMTestReport.Name)
    - [M Result ](#tts.core.api.comApi.Comserver.COMTestReport.Result)
    - [M TimeStamp ](#tts.core.api.comApi.Comserver.COMTestReport.TimeStamp)
- [ COMVariable ](#comvariable)
  - [C COMVariable ](#tts.core.api.comApi.Comserver.COMVariable)
    - [A Description ](#tts.core.api.comApi.Comserver.COMVariable.Description)
    - [A InitValue ](#tts.core.api.comApi.Comserver.COMVariable.InitValue)
    - [A Name ](#tts.core.api.comApi.Comserver.COMVariable.Name)
    - [M GetDescription ](#tts.core.api.comApi.Comserver.COMVariable.GetDescription)
    - [M GetInitValue ](#tts.core.api.comApi.Comserver.COMVariable.GetInitValue)
    - [M GetName ](#tts.core.api.comApi.Comserver.COMVariable.GetName)
    - [M IsInput ](#tts.core.api.comApi.Comserver.COMVariable.IsInput)
    - [M IsOutput ](#tts.core.api.comApi.Comserver.COMVariable.IsOutput)
- [ COMVariables ](#comvariables)
  - [C COMVariables ](#tts.core.api.comApi.Comserver.COMVariables)
    - [A Count ](#tts.core.api.comApi.Comserver.COMVariables.Count)
    - [M GetCount ](#tts.core.api.comApi.Comserver.COMVariables.GetCount)
    - [M Item ](#tts.core.api.comApi.Comserver.COMVariables.Item)

# COM API[¶](#com-api "Link to this heading")

This module contains the types for the COM-Application-Server. The main class is [`COMApplication`](#tts.core.api.comApi.Comserver_ET.COMApplication_ET "tts.core.api.comApi.Comserver_ET.COMApplication_ET (Python class) — This is the main object returned by the Dispatch() call.") which is instantiated with Prog-ID **‘ecu.test.Application’**.

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

Returns:  A [`COMCaches`](#tts.core.api.comApi.Comserver.COMCaches "tts.core.api.comApi.Comserver.COMCaches (Python class) — This class offers access to the different files caches.") object.

Return type:  [`COMCaches`](#tts.core.api.comApi.Comserver.COMCaches "tts.core.api.comApi.Comserver.COMCaches (Python class) — This class offers access to the different files caches.")

Packages[¶](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.Packages "Link to this definition")  
Returns a container object which gives access to all opened packages in COM-Application.

Returns:  The container object to access all opened packages.

Return type:  [`COMPackages`](#tts.core.api.comApi.Comserver.COMPackages "tts.core.api.comApi.Comserver.COMPackages (Python class) — This object gives access to all opened packages in COM-Application.")

Projects[¶](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.Projects "Link to this definition")  
Returns a container object which gives access to all opened projects in COM-Application.

Returns:  The container object to access all opened packages.

Return type:  [`COMProjects`](#tts.core.api.comApi.Comserver.COMProjects "tts.core.api.comApi.Comserver.COMProjects (Python class) — This object gives access to all opened projects in COM-Application.")

StartTimeout[¶](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.StartTimeout "Link to this definition")  
Property to get or set the timeout for the application start in seconds. Defaults to 90s.

Type:  int|float

ClosePackage(*[filename](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.ClosePackage.filename "tts.core.api.comApi.Comserver_ET.COMApplication_ET.ClosePackage.filename (Python parameter) — The full path name of the Package to close (for example "C:WorkspacePackagesSubfolderPackage.pkg") or a path name relative to the Packages directory of the current workspace (for example "SubfolderPackage.pkg")")*)[¶](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.ClosePackage "Link to this definition")  
Closes a Package (test case).

Parameters:  filename : str[¶](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.ClosePackage.filename "Permalink to this definition")  
The full path name of the Package to close (for example “C:WorkspacePackagesSubfolderPackage.pkg”) or a path name relative to the Packages directory of the current workspace (for example “SubfolderPackage.pkg”)

Returns:  True, if the package was closed, otherwise False.

Return type:  bool

CloseProject(*[filename](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.CloseProject.filename "tts.core.api.comApi.Comserver_ET.COMApplication_ET.CloseProject.filename (Python parameter) — The full path name of the project to close or a path name relative to the Packages directory of the current workspace")*)[¶](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.CloseProject "Link to this definition")  
Closes a project.

Parameters:  filename : str[¶](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.CloseProject.filename "Permalink to this definition")  
The full path name of the project to close or a path name relative to the Packages directory of the current workspace

Returns:  True, if the project was closed, otherwise False.

Return type:  bool

Exit(*[timeout](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.Exit.timeout "tts.core.api.comApi.Comserver_ET.COMApplication_ET.Exit.timeout (Python parameter) — Timeout in seconds before giving up to wait for application shutdown and raising an exception.")=`60`*)[¶](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.Exit "Link to this definition")  
Exits the currently running instance of the application (Hard Exit). Prefer the method Quit instead.

Parameters:  timeout : int[¶](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.Exit.timeout "Permalink to this definition")  
Timeout in seconds before giving up to wait for application shutdown and raising an exception.

Returns:  True, if operation successful.

Return type:  bool

Raises:  
**COMException** – if shutdown failed

GeneratePackageDocumentation(*[pkgPath](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.GeneratePackageDocumentation.pkgPath "tts.core.api.comApi.Comserver_ET.COMApplication_ET.GeneratePackageDocumentation.pkgPath (Python parameter) — Path of either a package or a folder containing packages.")*, *[docPath](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.GeneratePackageDocumentation.docPath "tts.core.api.comApi.Comserver_ET.COMApplication_ET.GeneratePackageDocumentation.docPath (Python parameter) — Path where the documentation files will be created.")*, *[doasync](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.GeneratePackageDocumentation.doasync "tts.core.api.comApi.Comserver_ET.COMApplication_ET.GeneratePackageDocumentation.doasync (Python parameter) — Mode of execution: asynchronous if True otherwise synchronous.")=`True`*)[¶](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.GeneratePackageDocumentation "Link to this definition")  
Creates documentation file(s) for a package or all packages in a folder depending on the given path.

Parameters:  pkgPath : str[¶](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.GeneratePackageDocumentation.pkgPath "Permalink to this definition")  
Path of either a package or a folder containing packages.

docPath : str[¶](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.GeneratePackageDocumentation.docPath "Permalink to this definition")  
Path where the documentation files will be created.

doasync : bool[¶](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.GeneratePackageDocumentation.doasync "Permalink to this definition")  
Mode of execution: asynchronous if True otherwise synchronous.

Returns:  Path of the generated (index) document if synchronous mode otherwise None.

Return type:  str

GetAnalysisEnvironment()[¶](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.GetAnalysisEnvironment "Link to this definition")  
Returns the analysis environment.

Returns:  A [`COMAnalysisEnvironment`](#tts.core.api.comApi.Comserver.COMAnalysisEnvironment "tts.core.api.comApi.Comserver.COMAnalysisEnvironment (Python class) — This class represents the currently started analysis environment. This environment supports operations to run analysis jobs.") object.

Return type:  [`COMAnalysisEnvironment`](#tts.core.api.comApi.Comserver.COMAnalysisEnvironment "tts.core.api.comApi.Comserver.COMAnalysisEnvironment (Python class) — This class represents the currently started analysis environment. This environment supports operations to run analysis jobs.")

GetCaches()[¶](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.GetCaches "Link to this definition")  
Returns the cache module.

Returns:  A [`COMCaches`](#tts.core.api.comApi.Comserver.COMCaches "tts.core.api.comApi.Comserver.COMCaches (Python class) — This class offers access to the different files caches.") object.

Return type:  [`COMCaches`](#tts.core.api.comApi.Comserver.COMCaches "tts.core.api.comApi.Comserver.COMCaches (Python class) — This class offers access to the different files caches.")

GetCurrentTestConfiguration()[¶](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.GetCurrentTestConfiguration "Link to this definition")  
Returns a TestConfiguration object providing access to settings of the currently active test configuration file.

Returns:  TestConfiguration object

Return type:  [`COMTestConfiguration`](#tts.core.api.comApi.Comserver.COMTestConfiguration "tts.core.api.comApi.Comserver.COMTestConfiguration (Python class) — Represent the currently loaded test configuration file and provides methods for accessing the contained settings.")

GetCurrentTestbenchConfiguration()[¶](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.GetCurrentTestbenchConfiguration "Link to this definition")  
Returns a TestbenchConfiguration object providing access to settings of the currently active testbench configuration file.

Returns:  TestConfiguration object

Return type:  [`COMTestbenchConfiguration`](#tts.core.api.comApi.Comserver_ET.COMTestbenchConfiguration "tts.core.api.comApi.Comserver_ET.COMTestbenchConfiguration (Python class) — Represent the currently loaded testbench configuration file and provides methods for accessing the contained settings.")

GetInstallDir()[¶](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.GetInstallDir "Link to this definition")  
Returns the installation directory.

Returns:  the installation directory.

Return type:  str

GetKeywordCatalogModule()[¶](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.GetKeywordCatalogModule "Link to this definition")  
Returns the keyword catalog module.

Returns:  A [`COMKeywordCatalog`](#tts.core.api.comApi.Comserver.COMKeywordCatalog "tts.core.api.comApi.Comserver.COMKeywordCatalog (Python class) — This class offers access to the keyword catalog interface.") object.

Return type:  [`COMKeywordCatalog`](#tts.core.api.comApi.Comserver.COMKeywordCatalog "tts.core.api.comApi.Comserver.COMKeywordCatalog (Python class) — This class offers access to the keyword catalog interface.")

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

Return type:  [`COMPackages`](#tts.core.api.comApi.Comserver.COMPackages "tts.core.api.comApi.Comserver.COMPackages (Python class) — This object gives access to all opened packages in COM-Application.")

GetProjects()[¶](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.GetProjects "Link to this definition")  
Returns a container object which gives access to all opened projects in COM-Application.

Returns:  The container object to access all opened packages.

Return type:  [`COMProjects`](#tts.core.api.comApi.Comserver.COMProjects "tts.core.api.comApi.Comserver.COMProjects (Python class) — This object gives access to all opened projects in COM-Application.")

GetSetting(*[settingName](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.GetSetting.settingName "tts.core.api.comApi.Comserver_ET.COMApplication_ET.GetSetting.settingName (Python parameter) — the setting name")*)[¶](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.GetSetting "Link to this definition")  
Queries the COM-Application setting value by name. Possible setting names are: - configPath - errorLogFile - generatorPath - language - logFile - packagePath - reportPath - templatePath - parameterPath - traceStepPath - userPyModulesPath - utilityPath - workspacePath - offlineModelPath - offlineSgbdPath - offlineFiuPath - settingsPath

Parameters:  settingName : str[¶](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.GetSetting.settingName "Permalink to this definition")  
the setting name

Returns:  setting value or None if not defined

Return type:  str or None

GetTestEnvironment()[¶](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.GetTestEnvironment "Link to this definition")  
Returns the test environment.

Returns:  A [`COMTestEnvironment`](#tts.core.api.comApi.Comserver.COMTestEnvironment "tts.core.api.comApi.Comserver.COMTestEnvironment (Python class) — This class represents the currently started test environment. The test environment supports operations to run packages (testcases) and projects.") object.

Return type:  [`COMTestEnvironment`](#tts.core.api.comApi.Comserver.COMTestEnvironment "tts.core.api.comApi.Comserver.COMTestEnvironment (Python class) — This class represents the currently started test environment. The test environment supports operations to run packages (testcases) and projects.")

GetTestManagementModule()[¶](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.GetTestManagementModule "Link to this definition")  
Returns the testmanagement module.

Returns:  A [`COMTestManagement`](#tts.core.api.comApi.Comserver.COMTestManagement "tts.core.api.comApi.Comserver.COMTestManagement (Python class) — This class offers access to the testmanagement interface.") object.

Return type:  [`COMTestManagement`](#tts.core.api.comApi.Comserver.COMTestManagement "tts.core.api.comApi.Comserver.COMTestManagement (Python class) — This class offers access to the testmanagement interface.")

GetVersion()[¶](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.GetVersion "Link to this definition")  
Queries the COM-Application version.

Returns:  Version string.

Return type:  str

HasActiveTasks()[¶](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.HasActiveTasks "Link to this definition")  
Returns if any tasks are running or are queued.

Returns:  True, if any active task exists.

Return type:  bool

IconizeMainFrame(*[iconize](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.IconizeMainFrame.iconize "tts.core.api.comApi.Comserver_ET.COMApplication_ET.IconizeMainFrame.iconize (Python parameter) — True - minimize window, False - restore window")*)[¶](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.IconizeMainFrame "Link to this definition")  
Iconize/Restore the MainFrame Window

Parameters:  iconize : bool[¶](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.IconizeMainFrame.iconize "Permalink to this definition")  
True - minimize window, False - restore window

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

LoadGlobalMapping(*[filename](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.LoadGlobalMapping.filename "tts.core.api.comApi.Comserver_ET.COMApplication_ET.LoadGlobalMapping.filename (Python parameter) — The full path name of the mapping file to load or a path name relative to the current workspace.")*, *[index](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.LoadGlobalMapping.index "tts.core.api.comApi.Comserver_ET.COMApplication_ET.LoadGlobalMapping.index (Python parameter) — The priority-index of the mapping file.")=`-``1`*, *[reloadIfNecessary](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.LoadGlobalMapping.reloadIfNecessary "tts.core.api.comApi.Comserver_ET.COMApplication_ET.LoadGlobalMapping.reloadIfNecessary (Python parameter) — Reload the mapping file when it is already open.")=`False`*)[¶](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.LoadGlobalMapping "Link to this definition")  
Loads a mapping file (\*.xam) into the global mapping space.

Parameters:  filename : str[¶](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.LoadGlobalMapping.filename "Permalink to this definition")  
The full path name of the mapping file to load or a path name relative to the current workspace.

index : int[¶](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.LoadGlobalMapping.index "Permalink to this definition")  
The priority-index of the mapping file. Index 0 is highest priority. (default is ‘-1’ for lowest priority)

reloadIfNecessary : bool[¶](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.LoadGlobalMapping.reloadIfNecessary "Permalink to this definition")  
Reload the mapping file when it is already open. (default: False)

Returns:  True, if the mapping file was successfully loaded, otherwise False.

Return type:  bool

MaximizeMainFrame(*[maximize](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.MaximizeMainFrame.maximize "tts.core.api.comApi.Comserver_ET.COMApplication_ET.MaximizeMainFrame.maximize (Python parameter) — True - maximize window, False - restore window")*)[¶](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.MaximizeMainFrame "Link to this definition")  
Maximize/Restore the MainFrame Window

Parameters:  maximize : bool[¶](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.MaximizeMainFrame.maximize "Permalink to this definition")  
True - maximize window, False - restore window

Returns:  True if success, otherwise False

Return type:  bool

OpenPackage(*[filename](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.OpenPackage.filename "tts.core.api.comApi.Comserver_ET.COMApplication_ET.OpenPackage.filename (Python parameter) — The full path name of the Package to open (for example "C:WorkspacePackagesSubfolderPackage.pkg") or a path name relative to the Packages directory of the current workspace (for example "SubfolderPackage.pkg")")*)[¶](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.OpenPackage "Link to this definition")  
Opens an existing Package (test case) in COM-Application. If the package to be opened is password protected an exception is raised.

Parameters:  filename : str[¶](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.OpenPackage.filename "Permalink to this definition")  
The full path name of the Package to open (for example “C:WorkspacePackagesSubfolderPackage.pkg”) or a path name relative to the Packages directory of the current workspace (for example “SubfolderPackage.pkg”)

Returns:  COMPackage, if the package is successfully opened, otherwise None.

Return type:  [`COMPackage`](#tts.core.api.comApi.Comserver.COMPackage "tts.core.api.comApi.Comserver.COMPackage (Python class) — This object gives access to the properties of an opened package.")

Raises:  
**COMException** – if the package is password protected

OpenProject(*[filename](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.OpenProject.filename "tts.core.api.comApi.Comserver_ET.COMApplication_ET.OpenProject.filename (Python parameter) — The full path name of the project to open or a path name relative to the Packages directory of the current workspace")*, *[execInCurrentPkgDir](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.OpenProject.execInCurrentPkgDir "tts.core.api.comApi.Comserver_ET.COMApplication_ET.OpenProject.execInCurrentPkgDir (Python parameter) — defines whether relative references in the project are resolved starting from the current workspaces package directory or from the project file location")=`False`*, *[filterExpression](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.OpenProject.filterExpression "tts.core.api.comApi.Comserver_ET.COMApplication_ET.OpenProject.filterExpression (Python parameter) — a valid filter expression (see the main help document, section 'Projects')")=`''`*)[¶](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.OpenProject "Link to this definition")  
Opens an existing project in COM-Application.

Parameters:  filename : str[¶](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.OpenProject.filename "Permalink to this definition")  
The full path name of the project to open or a path name relative to the Packages directory of the current workspace

execInCurrentPkgDir : bool[¶](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.OpenProject.execInCurrentPkgDir "Permalink to this definition")  
defines whether relative references in the project are resolved starting from the current workspaces package directory or from the project file location

filterExpression : str[¶](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.OpenProject.filterExpression "Permalink to this definition")  
a valid filter expression (see the main help document, section ‘Projects’)

Returns:  COMProject, if the project is successfully opened, otherwise None.

Return type:  [`COMProject`](#tts.core.api.comApi.Comserver.COMProject "tts.core.api.comApi.Comserver.COMProject (Python class) — This object gives access to the properties of an opened project.")

OpenTestConfiguration(*[filename](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.OpenTestConfiguration.filename "tts.core.api.comApi.Comserver_ET.COMApplication_ET.OpenTestConfiguration.filename (Python parameter) — The full path name of the test-configuration file to open or a path name relative to the Configurations directory of the current workspace")*)[¶](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.OpenTestConfiguration "Link to this definition")  
Opens a test-configuration file (\*.tcf).

Parameters:  filename : str[¶](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.OpenTestConfiguration.filename "Permalink to this definition")  
The full path name of the test-configuration file to open or a path name relative to the Configurations directory of the current workspace

Returns:  True, if the configuration was successfully opened, otherwise False.

Return type:  bool

OpenTestbenchConfiguration(*[filename](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.OpenTestbenchConfiguration.filename "tts.core.api.comApi.Comserver_ET.COMApplication_ET.OpenTestbenchConfiguration.filename (Python parameter) — The full path name of the testbench-configuration file to open.")*)[¶](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.OpenTestbenchConfiguration "Link to this definition")  
Opens a testbench configuration file (\*.tbc).

Parameters:  filename : str[¶](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.OpenTestbenchConfiguration.filename "Permalink to this definition")  
The full path name of the testbench-configuration file to open.

Returns:  True, if the configuration was successfully opened, otherwise False.

Return type:  bool

Quit(*[timeout](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.Quit.timeout "tts.core.api.comApi.Comserver_ET.COMApplication_ET.Quit.timeout (Python parameter) — Timeout in seconds before giving up to wait for application shutdown and raising an exception.")=`60`*)[¶](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.Quit "Link to this definition")  
Exits the currently running instance of the application (Soft Exit).

Parameters:  timeout : int[¶](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.Quit.timeout "Permalink to this definition")  
Timeout in seconds before giving up to wait for application shutdown and raising an exception.

Returns:  True, if success.

Return type:  bool

Raises:  
**COMException** – if shutdown failed

RunApplication(*[workspaceDir](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.RunApplication.workspaceDir "tts.core.api.comApi.Comserver_ET.COMApplication_ET.RunApplication.workspaceDir (Python parameter) — The full path name of the workspace directory.")=`None`*, *[localSettingsDir](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.RunApplication.localSettingsDir "tts.core.api.comApi.Comserver_ET.COMApplication_ET.RunApplication.localSettingsDir (Python parameter) — Absolute path specification to the directory in which the local user settings should be read from and stored in.")=`None`*)[¶](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.RunApplication "Link to this definition")  
Runs the application process and allows to specify a workspace directory. All other COM-Application methods require a running application process.

Parameters:  workspaceDir : str or None[¶](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.RunApplication.workspaceDir "Permalink to this definition")  
The full path name of the workspace directory. This directory must exist. If no sub directory .workspace with the corresponding settings files exists in this directory it will be created as well as the needed sub directories under the workspace directory. If the settings files exist the default directories are used like specified there. If in this case a needed directory doesn’t exist it will be created. If omitted (None) the default settings are used. In this case all default directories must exist in order to run the application process.

localSettingsDir : str or None[¶](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.RunApplication.localSettingsDir "Permalink to this definition")  
Absolute path specification to the directory in which the local user settings should be read from and stored in. If a directory is specified, it must exist. No new directory is created. In addition, no workspace selection dialog is displayed when ecu.test starts if this option is set.

Raises:  
**COMException** – if the application is already running or the process startup failed

Start()[¶](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.Start "Link to this definition")  
Starts up the currently loaded test configuration and testbench configuration files and returns a [`COMTestEnvironment`](#tts.core.api.comApi.Comserver.COMTestEnvironment "tts.core.api.comApi.Comserver.COMTestEnvironment (Python class) — This class represents the currently started test environment. The test environment supports operations to run packages (testcases) and projects.") object.

> The test- and testbench configuration can be changed by calling `OpenTestConfiguration()` and/or `OpenTestbenchConfiguration()` otherwise the last ran configurations are used.

Returns:  A [`COMTestEnvironment`](#tts.core.api.comApi.Comserver.COMTestEnvironment "tts.core.api.comApi.Comserver.COMTestEnvironment (Python class) — This class represents the currently started test environment. The test environment supports operations to run packages (testcases) and projects.") object.

Return type:  [`COMTestEnvironment`](#tts.core.api.comApi.Comserver.COMTestEnvironment "tts.core.api.comApi.Comserver.COMTestEnvironment (Python class) — This class represents the currently started test environment. The test environment supports operations to run packages (testcases) and projects.")

Raises:  
**COMException** – if the configuration start was prohibited by error in user script.

Stop()[¶](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.Stop "Link to this definition")  
Stops up the currently loaded test configuration and testbench configuration files and returns a [`COMTestEnvironment`](#tts.core.api.comApi.Comserver.COMTestEnvironment "tts.core.api.comApi.Comserver.COMTestEnvironment (Python class) — This class represents the currently started test environment. The test environment supports operations to run packages (testcases) and projects.") object.

Returns:  A [`COMTestEnvironment`](#tts.core.api.comApi.Comserver.COMTestEnvironment "tts.core.api.comApi.Comserver.COMTestEnvironment (Python class) — This class represents the currently started test environment. The test environment supports operations to run packages (testcases) and projects.") object.

Return type:  [`COMTestEnvironment`](#tts.core.api.comApi.Comserver.COMTestEnvironment "tts.core.api.comApi.Comserver.COMTestEnvironment (Python class) — This class represents the currently started test environment. The test environment supports operations to run packages (testcases) and projects.")

UnloadGlobalMapping(*[filename](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.UnloadGlobalMapping.filename "tts.core.api.comApi.Comserver_ET.COMApplication_ET.UnloadGlobalMapping.filename (Python parameter) — The full path name of the mapping file to unload or a path name relative to the current workspace.")*, *[force](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.UnloadGlobalMapping.force "tts.core.api.comApi.Comserver_ET.COMApplication_ET.UnloadGlobalMapping.force (Python parameter) — Ignore unsaved changes.")=`False`*)[¶](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.UnloadGlobalMapping "Link to this definition")  
Unloads a mapping file (\*.xam) from the global mapping space.

Parameters:  filename : str[¶](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.UnloadGlobalMapping.filename "Permalink to this definition")  
The full path name of the mapping file to unload or a path name relative to the current workspace.

force : bool[¶](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.UnloadGlobalMapping.force "Permalink to this definition")  
Ignore unsaved changes. (default: False)

Returns:  True, if the mapping file was successfully unloaded, otherwise False.

Return type:  bool

UpdateUserLibraries()[¶](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.UpdateUserLibraries "Link to this definition")  
Update all user libraries. Only possible if neither a test nor the analysis is running.

Returns:  True if success, otherwise False

Return type:  bool

WaitForIdle(*[timeout](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.WaitForIdle.timeout "tts.core.api.comApi.Comserver_ET.COMApplication_ET.WaitForIdle.timeout (Python parameter) — Timeout in seconds")=`None`*)[¶](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.WaitForIdle "Link to this definition")  
Waits until the job count in the task manager reaches zero. With the timeout parameter you can specify the maximum waiting time in seconds.

Parameters:  timeout : float[¶](#tts.core.api.comApi.Comserver_ET.COMApplication_ET.WaitForIdle.timeout "Permalink to this definition")  
Timeout in seconds

Returns:  True, if a job count of zero was reached within the timeout

Return type:  bool

## COMAnalysisEnvironment[¶](#comanalysisenvironment "Link to this heading")

*class* COMAnalysisEnvironment[¶](#tts.core.api.comApi.Comserver.COMAnalysisEnvironment "Link to this definition")  
This class represents the currently started analysis environment. This environment supports operations to run analysis jobs.

ExecuteJob(*[jobFile](#tts.core.api.comApi.Comserver.COMAnalysisEnvironment.ExecuteJob.jobFile "tts.core.api.comApi.Comserver.COMAnalysisEnvironment.ExecuteJob.jobFile (Python parameter) — The full path name of the analysis job file.")*, *[createReportDir](#tts.core.api.comApi.Comserver.COMAnalysisEnvironment.ExecuteJob.createReportDir "tts.core.api.comApi.Comserver.COMAnalysisEnvironment.ExecuteJob.createReportDir (Python parameter) — Flag that indicates whether a new report directory is created, or whether the report should be stored next to the job.")=`True`*)[¶](#tts.core.api.comApi.Comserver.COMAnalysisEnvironment.ExecuteJob "Link to this definition")  
Starts the execution of an analysis job.

Parameters:  jobFile : str[¶](#tts.core.api.comApi.Comserver.COMAnalysisEnvironment.ExecuteJob.jobFile "Permalink to this definition")  
The full path name of the analysis job file.

createReportDir : bool[¶](#tts.core.api.comApi.Comserver.COMAnalysisEnvironment.ExecuteJob.createReportDir "Permalink to this definition")  
Flag that indicates whether a new report directory is created, or whether the report should be stored next to the job.

Returns:  A [`COMAnalysisExecutionInfo`](#tts.core.api.comApi.Comserver.COMAnalysisExecutionInfo "tts.core.api.comApi.Comserver.COMAnalysisExecutionInfo (Python class) — This class offers operations to obtain information of the currently running analysis job.") object.

Return type:  [`COMAnalysisExecutionInfo`](#tts.core.api.comApi.Comserver.COMAnalysisExecutionInfo "tts.core.api.comApi.Comserver.COMAnalysisExecutionInfo (Python class) — This class offers operations to obtain information of the currently running analysis job.")

GetAnalysisExecutionInfo()[¶](#tts.core.api.comApi.Comserver.COMAnalysisEnvironment.GetAnalysisExecutionInfo "Link to this definition")  
Returns:  A [`COMAnalysisExecutionInfo`](#tts.core.api.comApi.Comserver.COMAnalysisExecutionInfo "tts.core.api.comApi.Comserver.COMAnalysisExecutionInfo (Python class) — This class offers operations to obtain information of the currently running analysis job.") object.

Return type:  [`COMAnalysisExecutionInfo`](#tts.core.api.comApi.Comserver.COMAnalysisExecutionInfo "tts.core.api.comApi.Comserver.COMAnalysisExecutionInfo (Python class) — This class offers operations to obtain information of the currently running analysis job.")

MergeJobReports(*[mainReportFilename](#tts.core.api.comApi.Comserver.COMAnalysisEnvironment.MergeJobReports.mainReportFilename "tts.core.api.comApi.Comserver.COMAnalysisEnvironment.MergeJobReports.mainReportFilename (Python parameter) — filename of main report")*, *[jobReports](#tts.core.api.comApi.Comserver.COMAnalysisEnvironment.MergeJobReports.jobReports "tts.core.api.comApi.Comserver.COMAnalysisEnvironment.MergeJobReports.jobReports (Python parameter) — list of filenames to reports of analysis job executions")*)[¶](#tts.core.api.comApi.Comserver.COMAnalysisEnvironment.MergeJobReports "Link to this definition")  
Merge reports of analysis job executions into a main report.

Parameters:  mainReportFilename : str[¶](#tts.core.api.comApi.Comserver.COMAnalysisEnvironment.MergeJobReports.mainReportFilename "Permalink to this definition")  
filename of main report

jobReports : list\<str\>[¶](#tts.core.api.comApi.Comserver.COMAnalysisEnvironment.MergeJobReports.jobReports "Permalink to this definition")  
list of filenames to reports of analysis job executions

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

WaitForTestexecutionCompletion(*[timeout](#tts.core.api.comApi.Comserver.COMAnalysisExecutionInfo.WaitForTestexecutionCompletion "tts.core.api.comApi.Comserver.COMAnalysisExecutionInfo.WaitForTestexecutionCompletion.timeout (Python parameter)")=`None`*)[¶](#tts.core.api.comApi.Comserver.COMAnalysisExecutionInfo.WaitForTestexecutionCompletion "Link to this definition")  
Waits until the current analysis job execution state will change to ABORTED or FINISHED. The timeout parameter specifies the maximum waiting time.

Returns:  The state of the current analysis job execution. One of - IDLE - RUNNING - ABORTED - FINISHED

Return type:  str

## COMCache[¶](#comcache "Link to this heading")

*class* COMCache[¶](#tts.core.api.comApi.Comserver.COMCache "Link to this definition")  
This class offers access to a specific file cache.

Clear(*[force](#tts.core.api.comApi.Comserver.COMCache.Clear.force "tts.core.api.comApi.Comserver.COMCache.Clear.force (Python parameter) — Close already opend cache files. ATTENTION: Data objects that are used in ecu.test will be destroyed.")=`False`*)[¶](#tts.core.api.comApi.Comserver.COMCache.Clear "Link to this definition")  
Remove all cache files of this category.

Parameters:  force : bool[¶](#tts.core.api.comApi.Comserver.COMCache.Clear.force "Permalink to this definition")  
Close already opend cache files. ATTENTION: Data objects that are used in ecu.test will be destroyed.

GetFiles()[¶](#tts.core.api.comApi.Comserver.COMCache.GetFiles "Link to this definition")  
Returns all cache files of this category.

Returns:  List of available cache files

Return type:  list\<str\>

Insert(*[filePath](#tts.core.api.comApi.Comserver.COMCache.Insert.filePath "tts.core.api.comApi.Comserver.COMCache.Insert.filePath (Python parameter) — The file path of the database to be added to the cache")*, *[dbChannel](#tts.core.api.comApi.Comserver.COMCache.Insert.dbChannel "tts.core.api.comApi.Comserver.COMCache.Insert.dbChannel (Python parameter) — The optional database channel.")=`''`*)[¶](#tts.core.api.comApi.Comserver.COMCache.Insert "Link to this definition")  
Insert a database to the cache.

Parameters:  filePath : str[¶](#tts.core.api.comApi.Comserver.COMCache.Insert.filePath "Permalink to this definition")  
The file path of the database to be added to the cache

dbChannel : str[¶](#tts.core.api.comApi.Comserver.COMCache.Insert.dbChannel "Permalink to this definition")  
The optional database channel. Only needed by bus and service databases.

## COMCaches[¶](#comcaches "Link to this heading")

*class* COMCaches[¶](#tts.core.api.comApi.Comserver.COMCaches "Link to this definition")  
This class offers access to the different files caches.

GetA2lCache()[¶](#tts.core.api.comApi.Comserver.COMCaches.GetA2lCache "Link to this definition")  
Provides access to A2L cache files.

Returns:  Cache object

Return type:  [`COMCache`](#tts.core.api.comApi.Comserver.COMCache "tts.core.api.comApi.Comserver.COMCache (Python class) — This class offers access to a specific file cache.")

GetBusCache()[¶](#tts.core.api.comApi.Comserver.COMCaches.GetBusCache "Link to this definition")  
Provides access to bus cache files.

Returns:  Cache object

Return type:  [`COMCache`](#tts.core.api.comApi.Comserver.COMCache "tts.core.api.comApi.Comserver.COMCache (Python class) — This class offers access to a specific file cache.")

GetElfCache()[¶](#tts.core.api.comApi.Comserver.COMCaches.GetElfCache "Link to this definition")  
Provides access to ELF cache files.

Returns:  Cache object

Return type:  [`COMCache`](#tts.core.api.comApi.Comserver.COMCache "tts.core.api.comApi.Comserver.COMCache (Python class) — This class offers access to a specific file cache.")

GetModelCache()[¶](#tts.core.api.comApi.Comserver.COMCaches.GetModelCache "Link to this definition")  
Provides access to model cache files.

Returns:  Cache object

Return type:  [`COMCache`](#tts.core.api.comApi.Comserver.COMCache "tts.core.api.comApi.Comserver.COMCache (Python class) — This class offers access to a specific file cache.")

GetServiceCache()[¶](#tts.core.api.comApi.Comserver.COMCaches.GetServiceCache "Link to this definition")  
Provides access to service cache files.

Returns:  Cache object

Return type:  [`COMCache`](#tts.core.api.comApi.Comserver.COMCache "tts.core.api.comApi.Comserver.COMCache (Python class) — This class offers access to a specific file cache.")

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

Item(*[idxOrName](#tts.core.api.comApi.Comserver.COMConstants.Item.idxOrName "tts.core.api.comApi.Comserver.COMConstants.Item.idxOrName (Python parameter) — The name of the constant or an index")*)[¶](#tts.core.api.comApi.Comserver.COMConstants.Item "Link to this definition")  
returns a specified constant. idxOrName can be either the name or an index. If an index is given then it should be between 0 and `GetCount()` - 1

Parameters:  idxOrName[¶](#tts.core.api.comApi.Comserver.COMConstants.Item.idxOrName "Permalink to this definition")  
The name of the constant or an index

Returns:  the constant.

Return type:  [`COMConstant`](#tts.core.api.comApi.Comserver.COMConstant "tts.core.api.comApi.Comserver.COMConstant (Python class) — This object gives access to the properties of a constant.")

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

LoadCatalog(*[catalogName](#tts.core.api.comApi.Comserver.COMKeywordCatalog.LoadCatalog.catalogName "tts.core.api.comApi.Comserver.COMKeywordCatalog.LoadCatalog.catalogName (Python parameter) — Name of the catalog.")*)[¶](#tts.core.api.comApi.Comserver.COMKeywordCatalog.LoadCatalog "Link to this definition")  
Loads the referenced catalog.

Parameters:  catalogName : str[¶](#tts.core.api.comApi.Comserver.COMKeywordCatalog.LoadCatalog.catalogName "Permalink to this definition")  
Name of the catalog.

Raises:  
**exception** – If an invalid catalog name has been referenced.

SetProject(*[projectName](#tts.core.api.comApi.Comserver.COMKeywordCatalog.SetProject.projectName "tts.core.api.comApi.Comserver.COMKeywordCatalog.SetProject.projectName (Python parameter) — Project name")*)[¶](#tts.core.api.comApi.Comserver.COMKeywordCatalog.SetProject "Link to this definition")  
Sets the referenced project.

Parameters:  projectName : str[¶](#tts.core.api.comApi.Comserver.COMKeywordCatalog.SetProject.projectName "Permalink to this definition")  
Project name

Raises:  
**exception** – If an invalid project name has been referenced.

SetVariant(*[variantName](#tts.core.api.comApi.Comserver.COMKeywordCatalog.SetVariant.variantName "tts.core.api.comApi.Comserver.COMKeywordCatalog.SetVariant.variantName (Python parameter) — Variant name")*)[¶](#tts.core.api.comApi.Comserver.COMKeywordCatalog.SetVariant "Link to this definition")  
Sets the referenced variant.

Parameters:  variantName : str[¶](#tts.core.api.comApi.Comserver.COMKeywordCatalog.SetVariant.variantName "Permalink to this definition")  
Variant name

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

Return type:  [`COMVariables`](#tts.core.api.comApi.Comserver.COMVariables "tts.core.api.comApi.Comserver.COMVariables (Python class) — This object gives access to all variable of a package in COM-Application.")

Check(*[recursive](#tts.core.api.comApi.Comserver.COMPackage.Check.recursive "tts.core.api.comApi.Comserver.COMPackage.Check.recursive (Python parameter) — Specifies if the package should be checked recursively.")=`None`*)[¶](#tts.core.api.comApi.Comserver.COMPackage.Check "Link to this definition")  
Returns a list of the errors of the package (including all subpackages).

Every list element is a tuple containing:

- file path

- seriousness (‘Error’, ‘Warning’ or ‘Note’)

- error message

- line number

- step UUID

Parameters:  recursive : bool[¶](#tts.core.api.comApi.Comserver.COMPackage.Check.recursive "Permalink to this definition")  
Specifies if the package should be checked recursively.

Returns:  Error List

Return type:  list\<tuple\>

CheckNG(*[recursive](#tts.core.api.comApi.Comserver.COMPackage.CheckNG.recursive "tts.core.api.comApi.Comserver.COMPackage.CheckNG.recursive (Python parameter) — Specifies if the package should be checked recursively.")=`None`*)[¶](#tts.core.api.comApi.Comserver.COMPackage.CheckNG "Link to this definition")  
Returns converted error descriptions into specific WarningsNG plugin JSON format.

- issues

  - description (link to package)

  - directory (package parent directory)

  - fileName (package name)

  - message (error message)

  - packageName (workspace subdirectory path of package)

  - severity (Error -> ‘ERROR’, Warning -> ‘HIGH’ or Note -> ‘NORMAL’)

- size (count of issues)

- \_class

Parameters:  recursive : bool[¶](#tts.core.api.comApi.Comserver.COMPackage.CheckNG.recursive "Permalink to this definition")  
Specifies if the package should be checked recursively.

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

Return type:  [`COMVariables`](#tts.core.api.comApi.Comserver.COMVariables "tts.core.api.comApi.Comserver.COMVariables (Python class) — This object gives access to all variable of a package in COM-Application.")

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

Item(*[pkg](#tts.core.api.comApi.Comserver.COMPackages.Item.pkg "tts.core.api.comApi.Comserver.COMPackages.Item.pkg (Python parameter) — The full path or an index")*)[¶](#tts.core.api.comApi.Comserver.COMPackages.Item "Link to this definition")  
returns a specified package. pkg can be either the full path or an index. If an index is given then it should be larger than 0 and lesser the number of packages opened. How many packages are currently open can be determined with `GetCount`

Parameters:  pkg[¶](#tts.core.api.comApi.Comserver.COMPackages.Item.pkg "Permalink to this definition")  
The full path or an index

Returns:  the package.

Return type:  [`COMPackage`](#tts.core.api.comApi.Comserver.COMPackage "tts.core.api.comApi.Comserver.COMPackage (Python class) — This object gives access to the properties of an opened package.")

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

Check(*[recursive](#tts.core.api.comApi.Comserver.COMProject.Check.recursive "tts.core.api.comApi.Comserver.COMProject.Check.recursive (Python parameter) — Specifies if the project should be checked recursively.")=`None`*)[¶](#tts.core.api.comApi.Comserver.COMProject.Check "Link to this definition")  
Returns a list of the errors of the project.

Every list element is a tuple containing:

- file path

- seriousness (‘Error’, ‘Warning’ or ‘Note’)

- error message

- line number

- step UUID

Parameters:  recursive : bool[¶](#tts.core.api.comApi.Comserver.COMProject.Check.recursive "Permalink to this definition")  
Specifies if the project should be checked recursively.

Returns:  Error List

Return type:  list\<tuple\>

CheckNG(*[recursive](#tts.core.api.comApi.Comserver.COMProject.CheckNG.recursive "tts.core.api.comApi.Comserver.COMProject.CheckNG.recursive (Python parameter) — Specifies if the project should be checked recursively.")=`None`*)[¶](#tts.core.api.comApi.Comserver.COMProject.CheckNG "Link to this definition")  
Returns converted error descriptions into specific WarningsNG plugin JSON format.

- issues

  - description (link to project)

  - directory (project parent directory)

  - fileName (project name)

  - message (error message)

  - packageName (workspace subdirectory path of project)

  - severity (Error -> ‘ERROR’, Warning -> ‘HIGH’ or Note -> ‘NORMAL’)

- size (count of issues)

- \_class

Parameters:  recursive : bool[¶](#tts.core.api.comApi.Comserver.COMProject.CheckNG.recursive "Permalink to this definition")  
Specifies if the project should be checked recursively.

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

Item(*[prj](#tts.core.api.comApi.Comserver.COMProjects.Item.prj "tts.core.api.comApi.Comserver.COMProjects.Item.prj (Python parameter) — The full path or an index")*)[¶](#tts.core.api.comApi.Comserver.COMProjects.Item "Link to this definition")  
returns a specified project. prj can be either the full path or an index. If an index is given then it should be larger than 0 and lesser than the number of projects opened. How many projects are currently open can be determined with `GetCount`

Parameters:  prj[¶](#tts.core.api.comApi.Comserver.COMProjects.Item.prj "Permalink to this definition")  
The full path or an index

Returns:  the project.

Return type:  [`COMProject`](#tts.core.api.comApi.Comserver.COMProject "tts.core.api.comApi.Comserver.COMProject (Python class) — This object gives access to the properties of an opened project.")

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

Return type:  [`COMConstants`](#tts.core.api.comApi.Comserver.COMConstants "tts.core.api.comApi.Comserver.COMConstants (Python class) — This object gives access to all global constants of the currently loaded test configuration.")

GetFilename()[¶](#tts.core.api.comApi.Comserver.COMTestConfiguration.GetFilename "Link to this definition")  
returns the full path of this test configuration.

Returns:  the full path of this configuration

Return type:  str

GetGlobalConstants()[¶](#tts.core.api.comApi.Comserver.COMTestConfiguration.GetGlobalConstants "Link to this definition")  
Returns a container object which gives access to all global constants of the currently loaded test configuration.

Returns:  The container object to access all global constants.

Return type:  [`COMConstants`](#tts.core.api.comApi.Comserver.COMConstants "tts.core.api.comApi.Comserver.COMConstants (Python class) — This object gives access to all global constants of the currently loaded test configuration.")

SetGlobalConstant(*[name](#tts.core.api.comApi.Comserver.COMTestConfiguration.SetGlobalConstant.name "tts.core.api.comApi.Comserver.COMTestConfiguration.SetGlobalConstant.name (Python parameter) — Name of the constant to be modified.")*, *[value](#tts.core.api.comApi.Comserver.COMTestConfiguration.SetGlobalConstant.value "tts.core.api.comApi.Comserver.COMTestConfiguration.SetGlobalConstant.value (Python parameter) — Value to be assigned.")*)[¶](#tts.core.api.comApi.Comserver.COMTestConfiguration.SetGlobalConstant "Link to this definition")  
Assign a value to a global constant. If the global constant does not exist it is created. This method requires a test configuration file to be loaded, otherwise an exception is thrown. The changed test configuration is saved instantly.

Parameters:  name : str[¶](#tts.core.api.comApi.Comserver.COMTestConfiguration.SetGlobalConstant.name "Permalink to this definition")  
Name of the constant to be modified.

value : str[¶](#tts.core.api.comApi.Comserver.COMTestConfiguration.SetGlobalConstant.value "Permalink to this definition")  
Value to be assigned. This must be a literal of a python data type, e.g. “1” (int literal) or “‘foo’” (string literal) or “[1, 2, 3]” (literal for a list with integer elements).

SetReportBaseFolder(*[path](#tts.core.api.comApi.Comserver.COMTestConfiguration.SetReportBaseFolder.path "tts.core.api.comApi.Comserver.COMTestConfiguration.SetReportBaseFolder.path (Python parameter) — Absolute or relative path to the new report base folder. If a relative path is passed the data directory is used as reference directory.")*)[¶](#tts.core.api.comApi.Comserver.COMTestConfiguration.SetReportBaseFolder "Link to this definition")  
Change base folder for test reports. If the new base folder does not exist it is created. The changed test configuration is saved instantly.

Parameters:  path : str[¶](#tts.core.api.comApi.Comserver.COMTestConfiguration.SetReportBaseFolder.path "Permalink to this definition")  
Absolute or relative path to the new report base folder. If a relative path is passed the data directory is used as reference directory.

## COMTestEnvironment[¶](#comtestenvironment "Link to this heading")

*class* COMTestEnvironment[¶](#tts.core.api.comApi.Comserver.COMTestEnvironment "Link to this definition")  
This class represents the currently started test environment. The test environment supports operations to run packages (testcases) and projects.

ExecutePackage(*[pkgFile](#tts.core.api.comApi.Comserver.COMTestEnvironment.ExecutePackage.pkgFile "tts.core.api.comApi.Comserver.COMTestEnvironment.ExecutePackage.pkgFile (Python parameter) — The full path name of the Package to execute (for example "C:\Workspace\Packages\Subfolder\Package.pkg") or a path name relative to the Packages directory of the current workspace (for example "Subfolder\Package.pkg")")*, *[runTraceAnalysis](#tts.core.api.comApi.Comserver.COMTestEnvironment.ExecutePackage.runTraceAnalysis "tts.core.api.comApi.Comserver.COMTestEnvironment.ExecutePackage.runTraceAnalysis (Python parameter) — specifies whether the trace analysis should be executed")=`True`*, *[runTest](#tts.core.api.comApi.Comserver.COMTestEnvironment.ExecutePackage.runTest "tts.core.api.comApi.Comserver.COMTestEnvironment.ExecutePackage.runTest (Python parameter) — specifies whether the test should be executed")=`True`*, *[paramValueDictAsList](#tts.core.api.comApi.Comserver.COMTestEnvironment.ExecutePackage.paramValueDictAsList "tts.core.api.comApi.Comserver.COMTestEnvironment.ExecutePackage.paramValueDictAsList (Python parameter) — A list with tuples (name, value) of length two for each parameter for the test and the trace analysis. Due to technical restrictions of the COM interface the parameter values must not contain dictionaries.")=`None`*, *[recInfoDictAsList](#tts.core.api.comApi.Comserver.COMTestEnvironment.ExecutePackage.recInfoDictAsList "tts.core.api.comApi.Comserver.COMTestEnvironment.ExecutePackage.recInfoDictAsList (Python parameter) — This list with tuples (recording group name, recording info list) assigns traces to recording groups.")=`None`*, *[parameterFiles](#tts.core.api.comApi.Comserver.COMTestEnvironment.ExecutePackage.parameterFiles "tts.core.api.comApi.Comserver.COMTestEnvironment.ExecutePackage.parameterFiles (Python parameter) — List of pathes to *.ppd files containing parameters to be applied to the package.")=`None`*, *[interactive](#tts.core.api.comApi.Comserver.COMTestEnvironment.ExecutePackage.interactive "tts.core.api.comApi.Comserver.COMTestEnvironment.ExecutePackage.interactive (Python parameter) — Specify if the package should be executed in the interactive mode")=`False`*, *[traceAnalysisMode](#tts.core.api.comApi.Comserver.COMTestEnvironment.ExecutePackage.traceAnalysisMode "tts.core.api.comApi.Comserver.COMTestEnvironment.ExecutePackage.traceAnalysisMode (Python parameter) — For internal use only")=`1`*)[¶](#tts.core.api.comApi.Comserver.COMTestEnvironment.ExecutePackage "Link to this definition")  
Starts the execution of the specified package file. The package must be already opened with `OpenPackage`. If it is not opened a call of this function will raise an error.

Parameters:  pkgFile : str[¶](#tts.core.api.comApi.Comserver.COMTestEnvironment.ExecutePackage.pkgFile "Permalink to this definition")  
The full path name of the Package to execute (for example “C:\Workspace\Packages\Subfolder\Package.pkg”) or a path name relative to the Packages directory of the current workspace (for example “Subfolder\Package.pkg”)

runTraceAnalysis : bool[¶](#tts.core.api.comApi.Comserver.COMTestEnvironment.ExecutePackage.runTraceAnalysis "Permalink to this definition")  
specifies whether the trace analysis should be executed

runTest : bool[¶](#tts.core.api.comApi.Comserver.COMTestEnvironment.ExecutePackage.runTest "Permalink to this definition")  
specifies whether the test should be executed

paramValueDictAsList : list\<tuple\>[¶](#tts.core.api.comApi.Comserver.COMTestEnvironment.ExecutePackage.paramValueDictAsList "Permalink to this definition")  
A list with tuples (name, value) of length two for each parameter for the test and the trace analysis. Due to technical restrictions of the COM interface the parameter values must not contain dictionaries.

recInfoDictAsList : list\<tuple\>[¶](#tts.core.api.comApi.Comserver.COMTestEnvironment.ExecutePackage.recInfoDictAsList "Permalink to this definition")  
This list with tuples (recording group name, recording info list) assigns traces to recording groups.

The entry ‘recording group name’ is a name of an existing recording group.

The entry ‘recording info list’ is a list of recording infos. A recording info is a list of tuples (key, value) which defines a dictionary with the following structure:

path: Either a trace file or a list of trace files. This must be given.

recordingName: The name of the recording, if it is necessary. For instance in a container file format for the unique identification.

recordingNumber: The number of the recording, if it is necessary. For instance in a container file format for the unique identification.

recordingType: The file type of the recording. If not given, an auto type detection is performed.

formatDetails: Format specific details. See the ‘Supported file formats’ section in the documentation.

parameterFiles : list\<str\>[¶](#tts.core.api.comApi.Comserver.COMTestEnvironment.ExecutePackage.parameterFiles "Permalink to this definition")  
List of pathes to \*.ppd files containing parameters to be applied to the package.

interactive : bool[¶](#tts.core.api.comApi.Comserver.COMTestEnvironment.ExecutePackage.interactive "Permalink to this definition")  
Specify if the package should be executed in the interactive mode

traceAnalysisMode : int[¶](#tts.core.api.comApi.Comserver.COMTestEnvironment.ExecutePackage.traceAnalysisMode "Permalink to this definition")  
For internal use only

Returns:  A [`COMTestExecutionInfo`](#tts.core.api.comApi.Comserver.COMTestExecutionInfo "tts.core.api.comApi.Comserver.COMTestExecutionInfo (Python class) — This class offers operations to obtain information of the currently running test.") object.

Return type:  [`COMTestExecutionInfo`](#tts.core.api.comApi.Comserver.COMTestExecutionInfo "tts.core.api.comApi.Comserver.COMTestExecutionInfo (Python class) — This class offers operations to obtain information of the currently running test.")

Raises:  
**COMException** – This exception is raised if the packages was not opened before. Or the format of the parameter values is wrong.

ExecuteProject(*[prjFile](#tts.core.api.comApi.Comserver.COMTestEnvironment.ExecuteProject.prjFile "tts.core.api.comApi.Comserver.COMTestEnvironment.ExecuteProject.prjFile (Python parameter) — The full path name of the project file")*, *[autocloseProjectProgressPnl](#tts.core.api.comApi.Comserver.COMTestEnvironment.ExecuteProject.autocloseProjectProgressPnl "tts.core.api.comApi.Comserver.COMTestEnvironment.ExecuteProject.autocloseProjectProgressPnl (Python parameter) — Determines whether the progress dialog will be closed when finished (default False).")=`False`*, *[executionMode](#tts.core.api.comApi.Comserver.COMTestEnvironment.ExecuteProject.executionMode "tts.core.api.comApi.Comserver.COMTestEnvironment.ExecuteProject.executionMode (Python parameter) — Specifies whether and how the analysis jobs should be executed.")=`1`*, *[interactive](#tts.core.api.comApi.Comserver.COMTestEnvironment.ExecuteProject.interactive "tts.core.api.comApi.Comserver.COMTestEnvironment.ExecuteProject.interactive (Python parameter) — Specify if the project should be executed in the interactive mode")=`False`*)[¶](#tts.core.api.comApi.Comserver.COMTestEnvironment.ExecuteProject "Link to this definition")  
Starts the execution of the specified project file. The project must be already opened with `OpenProject`. If it is not opened a call of this function will raise an error.

Parameters:  prjFile : str[¶](#tts.core.api.comApi.Comserver.COMTestEnvironment.ExecuteProject.prjFile "Permalink to this definition")  
The full path name of the project file

autocloseProjectProgressPnl : bool[¶](#tts.core.api.comApi.Comserver.COMTestEnvironment.ExecuteProject.autocloseProjectProgressPnl "Permalink to this definition")  
Determines whether the progress dialog will be closed when finished (default False).

executionMode : int[¶](#tts.core.api.comApi.Comserver.COMTestEnvironment.ExecuteProject.executionMode "Permalink to this definition")  
Specifies whether and how the analysis jobs should be executed.

0.  no job execution

1.  sequential job execution (default)

2.  parallel job execution

5.  sequential job execution without report merge of analysis job sub reports into the main test report

6.  parallel job execution without report merge of analysis job sub reports into the main test report

9.  job execution without running the test case part

interactive : bool[¶](#tts.core.api.comApi.Comserver.COMTestEnvironment.ExecuteProject.interactive "Permalink to this definition")  
Specify if the project should be executed in the interactive mode

Returns:  A [`COMTestExecutionInfo`](#tts.core.api.comApi.Comserver.COMTestExecutionInfo "tts.core.api.comApi.Comserver.COMTestExecutionInfo (Python class) — This class offers operations to obtain information of the currently running test.") object.

Return type:  [`COMTestExecutionInfo`](#tts.core.api.comApi.Comserver.COMTestExecutionInfo "tts.core.api.comApi.Comserver.COMTestExecutionInfo (Python class) — This class offers operations to obtain information of the currently running test.")

Raises:  
**COMException** – Will be raised if the project has not been opened.

ExecuteProjectArchive(*[przFile](#tts.core.api.comApi.Comserver.COMTestEnvironment.ExecuteProjectArchive.przFile "tts.core.api.comApi.Comserver.COMTestEnvironment.ExecuteProjectArchive.przFile (Python parameter) — The full path name of the project archive file")*, *[autocloseProjectProgressPnl](#tts.core.api.comApi.Comserver.COMTestEnvironment.ExecuteProjectArchive.autocloseProjectProgressPnl "tts.core.api.comApi.Comserver.COMTestEnvironment.ExecuteProjectArchive.autocloseProjectProgressPnl (Python parameter) — Determines whether the progress dialog will be closed when finished (default False).")=`True`*, *[executionMode](#tts.core.api.comApi.Comserver.COMTestEnvironment.ExecuteProjectArchive.executionMode "tts.core.api.comApi.Comserver.COMTestEnvironment.ExecuteProjectArchive.executionMode (Python parameter) — Specifies whether and how the analysis jobs should be executed.")=`1`*, *[interactive](#tts.core.api.comApi.Comserver.COMTestEnvironment.ExecuteProjectArchive.interactive "tts.core.api.comApi.Comserver.COMTestEnvironment.ExecuteProjectArchive.interactive (Python parameter) — Specify if the project should be executed in the interactive mode")=`False`*)[¶](#tts.core.api.comApi.Comserver.COMTestEnvironment.ExecuteProjectArchive "Link to this definition")  
Extracts a project archive and starts the execution of the archived project.

Parameters:  przFile : str[¶](#tts.core.api.comApi.Comserver.COMTestEnvironment.ExecuteProjectArchive.przFile "Permalink to this definition")  
The full path name of the project archive file

autocloseProjectProgressPnl : boolean[¶](#tts.core.api.comApi.Comserver.COMTestEnvironment.ExecuteProjectArchive.autocloseProjectProgressPnl "Permalink to this definition")  
Determines whether the progress dialog will be closed when finished (default False).

executionMode : int[¶](#tts.core.api.comApi.Comserver.COMTestEnvironment.ExecuteProjectArchive.executionMode "Permalink to this definition")  
Specifies whether and how the analysis jobs should be executed.

0.  no job execution

1.  sequential job execution (default)

2.  parallel job execution

5.  sequential job execution without report merge of analysis job sub reports into the main test report

6.  parallel job execution without report merge of analysis job sub reports into the main test report

9.  job execution without running the test case part

interactive : bool[¶](#tts.core.api.comApi.Comserver.COMTestEnvironment.ExecuteProjectArchive.interactive "Permalink to this definition")  
Specify if the project should be executed in the interactive mode

Returns:  A [`COMTestExecutionInfo`](#tts.core.api.comApi.Comserver.COMTestExecutionInfo "tts.core.api.comApi.Comserver.COMTestExecutionInfo (Python class) — This class offers operations to obtain information of the currently running test.") object.

Return type:  [`COMTestExecutionInfo`](#tts.core.api.comApi.Comserver.COMTestExecutionInfo "tts.core.api.comApi.Comserver.COMTestExecutionInfo (Python class) — This class offers operations to obtain information of the currently running test.")

Raises:  
**COMException** – Will be raised if the project archive could not be extracted or started.

GenerateTestReportDocument(*[reportFile](#tts.core.api.comApi.Comserver.COMTestEnvironment.GenerateTestReportDocument.reportFile "tts.core.api.comApi.Comserver.COMTestEnvironment.GenerateTestReportDocument.reportFile (Python parameter) — path to the TRF or PRF")*, *[outDir](#tts.core.api.comApi.Comserver.COMTestEnvironment.GenerateTestReportDocument.outDir "tts.core.api.comApi.Comserver.COMTestEnvironment.GenerateTestReportDocument.outDir (Python parameter) — output directory")*, *[fmtConfigFile](#tts.core.api.comApi.Comserver.COMTestEnvironment.GenerateTestReportDocument.fmtConfigFile "tts.core.api.comApi.Comserver.COMTestEnvironment.GenerateTestReportDocument.fmtConfigFile (Python parameter) — Path to the reportFormatFile(XML) specifying the generator settings which should be used.")*, *[waitUntilFinished](#tts.core.api.comApi.Comserver.COMTestEnvironment.GenerateTestReportDocument.waitUntilFinished "tts.core.api.comApi.Comserver.COMTestEnvironment.GenerateTestReportDocument.waitUntilFinished (Python parameter) — defines whether the API call should block until generation is finished.")=`False`*)[¶](#tts.core.api.comApi.Comserver.COMTestEnvironment.GenerateTestReportDocument "Link to this definition")  
Generates a handler based testreport on the filesystem. It uses the settings previously stored next to the trf. This is performed when the “Save settings for later generation next to the TRF” option of the report generator configuration is ticked.

Parameters:  reportFile : str[¶](#tts.core.api.comApi.Comserver.COMTestEnvironment.GenerateTestReportDocument.reportFile "Permalink to this definition")  
path to the TRF or PRF

outDir : str[¶](#tts.core.api.comApi.Comserver.COMTestEnvironment.GenerateTestReportDocument.outDir "Permalink to this definition")  
output directory

fmtConfigFile : str[¶](#tts.core.api.comApi.Comserver.COMTestEnvironment.GenerateTestReportDocument.fmtConfigFile "Permalink to this definition")  
Path to the reportFormatFile(XML) specifying the generator settings which should be used.

waitUntilFinished : bool[¶](#tts.core.api.comApi.Comserver.COMTestEnvironment.GenerateTestReportDocument.waitUntilFinished "Permalink to this definition")  
defines whether the API call should block until generation is finished.

Returns:  always True

Return type:  bool

GenerateTestReportDocumentFromDB(*[dbFile](#tts.core.api.comApi.Comserver.COMTestEnvironment.GenerateTestReportDocumentFromDB.dbFile "tts.core.api.comApi.Comserver.COMTestEnvironment.GenerateTestReportDocumentFromDB.dbFile (Python parameter) — path to the databasefile")*, *[outDir](#tts.core.api.comApi.Comserver.COMTestEnvironment.GenerateTestReportDocumentFromDB.outDir "tts.core.api.comApi.Comserver.COMTestEnvironment.GenerateTestReportDocumentFromDB.outDir (Python parameter) — output directory")*, *[fmtName](#tts.core.api.comApi.Comserver.COMTestEnvironment.GenerateTestReportDocumentFromDB.fmtName "tts.core.api.comApi.Comserver.COMTestEnvironment.GenerateTestReportDocumentFromDB.fmtName (Python parameter) — Name of the reportformat or handler which should be used.")=`None`*, *[waitUntilFinished](#tts.core.api.comApi.Comserver.COMTestEnvironment.GenerateTestReportDocumentFromDB.waitUntilFinished "tts.core.api.comApi.Comserver.COMTestEnvironment.GenerateTestReportDocumentFromDB.waitUntilFinished (Python parameter) — defines whether the API call should block until generation is finished.")=`False`*, *[fmtConfig](#tts.core.api.comApi.Comserver.COMTestEnvironment.GenerateTestReportDocumentFromDB.fmtConfig "tts.core.api.comApi.Comserver.COMTestEnvironment.GenerateTestReportDocumentFromDB.fmtConfig (Python parameter) — A list with tuples (name, value) of length two for each configuration parameter for the report format.")=`None`*)[¶](#tts.core.api.comApi.Comserver.COMTestEnvironment.GenerateTestReportDocumentFromDB "Link to this definition")  
Generates a handler based testreport on the filesystem.

Parameters:  dbFile : str[¶](#tts.core.api.comApi.Comserver.COMTestEnvironment.GenerateTestReportDocumentFromDB.dbFile "Permalink to this definition")  
path to the databasefile

outDir : str[¶](#tts.core.api.comApi.Comserver.COMTestEnvironment.GenerateTestReportDocumentFromDB.outDir "Permalink to this definition")  
output directory

fmtName : str[¶](#tts.core.api.comApi.Comserver.COMTestEnvironment.GenerateTestReportDocumentFromDB.fmtName "Permalink to this definition")  
Name of the reportformat or handler which should be used. (Optional) The default is the standardhandler.

fmtConfig : list\<tuples\>[¶](#tts.core.api.comApi.Comserver.COMTestEnvironment.GenerateTestReportDocumentFromDB.fmtConfig "Permalink to this definition")  
A list with tuples (name, value) of length two for each configuration parameter for the report format. Due to technical restrictions of the COM interface the parameter values must not contain dictionaries.

waitUntilFinished : bool[¶](#tts.core.api.comApi.Comserver.COMTestEnvironment.GenerateTestReportDocumentFromDB.waitUntilFinished "Permalink to this definition")  
defines whether the API call should block until generation is finished.

Returns:  always True

Return type:  bool

GetTestExecutionInfo()[¶](#tts.core.api.comApi.Comserver.COMTestEnvironment.GetTestExecutionInfo "Link to this definition")  
Returns:  A [`COMTestExecutionInfo`](#tts.core.api.comApi.Comserver.COMTestExecutionInfo "tts.core.api.comApi.Comserver.COMTestExecutionInfo (Python class) — This class offers operations to obtain information of the currently running test.") object.

Return type:  [`COMTestExecutionInfo`](#tts.core.api.comApi.Comserver.COMTestExecutionInfo "tts.core.api.comApi.Comserver.COMTestExecutionInfo (Python class) — This class offers operations to obtain information of the currently running test.")

## COMTestExecutionInfo[¶](#comtestexecutioninfo "Link to this heading")

*class* COMTestExecutionInfo[¶](#tts.core.api.comApi.Comserver.COMTestExecutionInfo "Link to this definition")  
This class offers operations to obtain information of the currently running test.

TestReport[¶](#tts.core.api.comApi.Comserver.COMTestExecutionInfo.TestReport "Link to this definition")  
Get a new testreport object.

Abort()[¶](#tts.core.api.comApi.Comserver.COMTestExecutionInfo.Abort "Link to this definition")  
Aborts the current testexecution.

Returns:  True, if the abort succeeded. False, if the testexecution has already finished or aborted.

Return type:  bool

AbortAfterCurrentProjectStep(*[timeout](#tts.core.api.comApi.Comserver.COMTestExecutionInfo.AbortAfterCurrentProjectStep "tts.core.api.comApi.Comserver.COMTestExecutionInfo.AbortAfterCurrentProjectStep.timeout (Python parameter)")=`None`*)[¶](#tts.core.api.comApi.Comserver.COMTestExecutionInfo.AbortAfterCurrentProjectStep "Link to this definition")  
Aborts the current testexecution.

Returns:  True, if the abort succeded. False, if the testexecution has already finished or aborted.

Return type:  bool

GenerateTestReportDocument(*[outDir](#tts.core.api.comApi.Comserver.COMTestExecutionInfo.GenerateTestReportDocument.outDir "tts.core.api.comApi.Comserver.COMTestExecutionInfo.GenerateTestReportDocument.outDir (Python parameter) — output directory")*, *[fmtName](#tts.core.api.comApi.Comserver.COMTestExecutionInfo.GenerateTestReportDocument.fmtName "tts.core.api.comApi.Comserver.COMTestExecutionInfo.GenerateTestReportDocument.fmtName (Python parameter) — Name of the reportformat or handler which should be used (Optional). The default is the standardhandler.")=`None`*, *[waitUntilFinished](#tts.core.api.comApi.Comserver.COMTestExecutionInfo.GenerateTestReportDocument.waitUntilFinished "tts.core.api.comApi.Comserver.COMTestExecutionInfo.GenerateTestReportDocument.waitUntilFinished (Python parameter) — defines whether the API call should block until generation is finished")=`False`*, *[fmtConfig](#tts.core.api.comApi.Comserver.COMTestExecutionInfo.GenerateTestReportDocument.fmtConfig "tts.core.api.comApi.Comserver.COMTestExecutionInfo.GenerateTestReportDocument.fmtConfig (Python parameter) — A list with tuples (name, value) of length two for each configuration parameter for the reportformat, where name and value are of data type string (e.g., "True" instead of True for value). Due to technical restrictions of the COM interface the parameter values must not contain dictionaries.")=`None`*)[¶](#tts.core.api.comApi.Comserver.COMTestExecutionInfo.GenerateTestReportDocument "Link to this definition")  
Generates a handler based testreport on the filesystem.

Returns:  True - all o.k., otherwise False

Return type:  bool

Parameters:  outDir : str[¶](#tts.core.api.comApi.Comserver.COMTestExecutionInfo.GenerateTestReportDocument.outDir "Permalink to this definition")  
output directory

fmtName : str[¶](#tts.core.api.comApi.Comserver.COMTestExecutionInfo.GenerateTestReportDocument.fmtName "Permalink to this definition")  
Name of the reportformat or handler which should be used (Optional). The default is the standardhandler.

waitUntilFinished : bool[¶](#tts.core.api.comApi.Comserver.COMTestExecutionInfo.GenerateTestReportDocument.waitUntilFinished "Permalink to this definition")  
defines whether the API call should block until generation is finished

fmtConfig : list(tuple(string, string))[¶](#tts.core.api.comApi.Comserver.COMTestExecutionInfo.GenerateTestReportDocument.fmtConfig "Permalink to this definition")  
A list with tuples (name, value) of length two for each configuration parameter for the reportformat, where name and value are of data type string (e.g., “True” instead of True for value). Due to technical restrictions of the COM interface the parameter values must not contain dictionaries.

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

GetReturnValue(*[varName](#tts.core.api.comApi.Comserver.COMTestExecutionInfo.GetReturnValue.varName "tts.core.api.comApi.Comserver.COMTestExecutionInfo.GetReturnValue.varName (Python parameter) — the variable name")*)[¶](#tts.core.api.comApi.Comserver.COMTestExecutionInfo.GetReturnValue "Link to this definition")  
If a test execution has finished GetReturnValue returns the final value of a package variable.

Parameters:  varName : str[¶](#tts.core.api.comApi.Comserver.COMTestExecutionInfo.GetReturnValue.varName "Permalink to this definition")  
the variable name

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

Return type:  [`COMTestReport`](#tts.core.api.comApi.Comserver.COMTestReport "tts.core.api.comApi.Comserver.COMTestReport (Python class) — This object gives access to the test report of the current or most recent testrun")

WaitForTestexecutionCompletion(*[timeout](#tts.core.api.comApi.Comserver.COMTestExecutionInfo.WaitForTestexecutionCompletion "tts.core.api.comApi.Comserver.COMTestExecutionInfo.WaitForTestexecutionCompletion.timeout (Python parameter)")=`None`*)[¶](#tts.core.api.comApi.Comserver.COMTestExecutionInfo.WaitForTestexecutionCompletion "Link to this definition")  
Waits until the current testexecution state will change to ABORTED or FINISHED. With the timeout parameter you can specify the maximum waiting time.

Returns:  The state of the current testexecution. One of - IDLE - RUNNING - ABORTED - FINISHED

Return type:  str

## COMTestManagement[¶](#comtestmanagement "Link to this heading")

*class* COMTestManagement[¶](#tts.core.api.comApi.Comserver.COMTestManagement "Link to this definition")  
This class offers access to the testmanagement interface.

These methods can only be used if access to a test management system has previously been configured (once) manually for the current workspace.

ExportPackage(*[filePath](#tts.core.api.comApi.Comserver.COMTestManagement.ExportPackage.filePath "tts.core.api.comApi.Comserver.COMTestManagement.ExportPackage.filePath (Python parameter) — The file path of the package to be exported (relative to package directory or absolute).")*, *[exportPath](#tts.core.api.comApi.Comserver.COMTestManagement.ExportPackage.exportPath "tts.core.api.comApi.Comserver.COMTestManagement.ExportPackage.exportPath (Python parameter) — Path specifying where the project should be placed at.")*, *[createNewPath](#tts.core.api.comApi.Comserver.COMTestManagement.ExportPackage.createNewPath "tts.core.api.comApi.Comserver.COMTestManagement.ExportPackage.createNewPath (Python parameter) — If the exportPath does not exist, it will be created. (Optional) The default is False.")=`False`*, *[overrideExisting](#tts.core.api.comApi.Comserver.COMTestManagement.ExportPackage.overrideExisting "tts.core.api.comApi.Comserver.COMTestManagement.ExportPackage.overrideExisting (Python parameter) — Defines, if an existing package with the same name (in the referenced folder) should be overridden.")=`True`*, *[timeout](#tts.core.api.comApi.Comserver.COMTestManagement.ExportPackage.timeout "tts.core.api.comApi.Comserver.COMTestManagement.ExportPackage.timeout (Python parameter) — timeout in seconds to wait for export to be finished (optional).")=`None`*)[¶](#tts.core.api.comApi.Comserver.COMTestManagement.ExportPackage "Link to this definition")  
Exports the given package into the test management system. The exportPath is needed to specify where the package should be placed at.

Parameters:  filePath : str[¶](#tts.core.api.comApi.Comserver.COMTestManagement.ExportPackage.filePath "Permalink to this definition")  
The file path of the package to be exported (relative to package directory or absolute).

exportPath : str[¶](#tts.core.api.comApi.Comserver.COMTestManagement.ExportPackage.exportPath "Permalink to this definition")  
Path specifying where the project should be placed at. Specify the path as it would be displayed in the export dialog. Only Unix styled paths (separated by forward slashes, “/”) are allowed.

createNewPath : bool[¶](#tts.core.api.comApi.Comserver.COMTestManagement.ExportPackage.createNewPath "Permalink to this definition")  
If the exportPath does not exist, it will be created. (Optional) The default is False.

overrideExisting : bool[¶](#tts.core.api.comApi.Comserver.COMTestManagement.ExportPackage.overrideExisting "Permalink to this definition")  
Defines, if an existing package with the same name (in the referenced folder) should be overridden.

timeout : int[¶](#tts.core.api.comApi.Comserver.COMTestManagement.ExportPackage.timeout "Permalink to this definition")  
timeout in seconds to wait for export to be finished (optional).

Raises:  
**exception** – If a user adapter is currently active. Or the test management system is not configured. Or the user is not authenticated.

ExportPackageAttributes(*[filePath](#tts.core.api.comApi.Comserver.COMTestManagement.ExportPackageAttributes.filePath "tts.core.api.comApi.Comserver.COMTestManagement.ExportPackageAttributes.filePath (Python parameter) — The file path of the package whose attributes have to be exported (relative to package directory or absolute).")*, *[timeout](#tts.core.api.comApi.Comserver.COMTestManagement.ExportPackageAttributes.timeout "tts.core.api.comApi.Comserver.COMTestManagement.ExportPackageAttributes.timeout (Python parameter) — timeout in seconds to wait for import to be finished (optional).")=`None`*)[¶](#tts.core.api.comApi.Comserver.COMTestManagement.ExportPackageAttributes "Link to this definition")  
Exports the attributes of the given package to test management system.

Parameters:  filePath : str[¶](#tts.core.api.comApi.Comserver.COMTestManagement.ExportPackageAttributes.filePath "Permalink to this definition")  
The file path of the package whose attributes have to be exported (relative to package directory or absolute).

timeout : int[¶](#tts.core.api.comApi.Comserver.COMTestManagement.ExportPackageAttributes.timeout "Permalink to this definition")  
timeout in seconds to wait for import to be finished (optional).

Raises:  
**exception** – If a user adapter is currently active. Or the test management system is not configured. Or the user is not authenticated.

ExportPackageChanges(*[filePath](#tts.core.api.comApi.Comserver.COMTestManagement.ExportPackageChanges.filePath "tts.core.api.comApi.Comserver.COMTestManagement.ExportPackageChanges.filePath (Python parameter) — The file path of the package to be exported (relative to package directory or absolute).")*, *[timeout](#tts.core.api.comApi.Comserver.COMTestManagement.ExportPackageChanges.timeout "tts.core.api.comApi.Comserver.COMTestManagement.ExportPackageChanges.timeout (Python parameter) — timeout in seconds to wait for export to be finished (optional).")=`None`*)[¶](#tts.core.api.comApi.Comserver.COMTestManagement.ExportPackageChanges "Link to this definition")  
Exports the changes of the given package into the test management system. The package needs to be already link with the test management system.

Parameters:  filePath : str[¶](#tts.core.api.comApi.Comserver.COMTestManagement.ExportPackageChanges.filePath "Permalink to this definition")  
The file path of the package to be exported (relative to package directory or absolute).

timeout : int[¶](#tts.core.api.comApi.Comserver.COMTestManagement.ExportPackageChanges.timeout "Permalink to this definition")  
timeout in seconds to wait for export to be finished (optional).

Raises:  
**exception** – If a user adapter is currently active. Or the test management system is not configured. Or the user is not authenticated.

ExportProject(*[filePath](#tts.core.api.comApi.Comserver.COMTestManagement.ExportProject.filePath "tts.core.api.comApi.Comserver.COMTestManagement.ExportProject.filePath (Python parameter) — The filepath of the project to be exported (relative to package directory or absolute).")*, *[exportPath](#tts.core.api.comApi.Comserver.COMTestManagement.ExportProject.exportPath "tts.core.api.comApi.Comserver.COMTestManagement.ExportProject.exportPath (Python parameter) — Path specifying where the project should be placed at.")*, *[createNewPath](#tts.core.api.comApi.Comserver.COMTestManagement.ExportProject.createNewPath "tts.core.api.comApi.Comserver.COMTestManagement.ExportProject.createNewPath (Python parameter) — If the exportPath does not exist, it will be created. (Optional) The default is False.")=`False`*, *[overrideExisting](#tts.core.api.comApi.Comserver.COMTestManagement.ExportProject.overrideExisting "tts.core.api.comApi.Comserver.COMTestManagement.ExportProject.overrideExisting (Python parameter) — Defines, if an existing project with the same name (in the referenced folder) should be overridden.")=`True`*, *[timeout](#tts.core.api.comApi.Comserver.COMTestManagement.ExportProject.timeout "tts.core.api.comApi.Comserver.COMTestManagement.ExportProject.timeout (Python parameter) — timeout in seconds to wait for the export to be finished (optional).")=`None`*)[¶](#tts.core.api.comApi.Comserver.COMTestManagement.ExportProject "Link to this definition")  
Exports the given project into the test management system. The exportPath is needed to specify where the project should be placed at.

Parameters:  filePath : str[¶](#tts.core.api.comApi.Comserver.COMTestManagement.ExportProject.filePath "Permalink to this definition")  
The filepath of the project to be exported (relative to package directory or absolute).

exportPath : str[¶](#tts.core.api.comApi.Comserver.COMTestManagement.ExportProject.exportPath "Permalink to this definition")  
Path specifying where the project should be placed at. Specify the path as it would be displayed in the export dialog. Only Unix styled paths (separated by forward slashes, “/”) are allowed.

createNewPath : bool[¶](#tts.core.api.comApi.Comserver.COMTestManagement.ExportProject.createNewPath "Permalink to this definition")  
If the exportPath does not exist, it will be created. (Optional) The default is False.

overrideExisting : bool[¶](#tts.core.api.comApi.Comserver.COMTestManagement.ExportProject.overrideExisting "Permalink to this definition")  
Defines, if an existing project with the same name (in the referenced folder) should be overridden.

timeout : int[¶](#tts.core.api.comApi.Comserver.COMTestManagement.ExportProject.timeout "Permalink to this definition")  
timeout in seconds to wait for the export to be finished (optional).

Raises:  
**exception** – If a user adapter is currently active. Or the test management system is not configured. Or the user is not authenticated.

ExportProjectAttributes(*[filePath](#tts.core.api.comApi.Comserver.COMTestManagement.ExportProjectAttributes.filePath "tts.core.api.comApi.Comserver.COMTestManagement.ExportProjectAttributes.filePath (Python parameter) — The file path of the project whose attributes have to be exported (relative to package directory or absolute).")*, *[timeout](#tts.core.api.comApi.Comserver.COMTestManagement.ExportProjectAttributes.timeout "tts.core.api.comApi.Comserver.COMTestManagement.ExportProjectAttributes.timeout (Python parameter) — timeout in seconds to wait for import to be finished (optional).")=`None`*)[¶](#tts.core.api.comApi.Comserver.COMTestManagement.ExportProjectAttributes "Link to this definition")  
Exports the attributes of the given project to test management system.

Parameters:  filePath : str[¶](#tts.core.api.comApi.Comserver.COMTestManagement.ExportProjectAttributes.filePath "Permalink to this definition")  
The file path of the project whose attributes have to be exported (relative to package directory or absolute).

timeout : int[¶](#tts.core.api.comApi.Comserver.COMTestManagement.ExportProjectAttributes.timeout "Permalink to this definition")  
timeout in seconds to wait for import to be finished (optional).

Raises:  
**exception** – If a user adapter is currently active. Or the test management system is not configured. Or the user is not authenticated.

ExportReport(*[filePath](#tts.core.api.comApi.Comserver.COMTestManagement.ExportReport.filePath "tts.core.api.comApi.Comserver.COMTestManagement.ExportReport.filePath (Python parameter) — The filepath of the project report file to be exported")*, *[archivePath](#tts.core.api.comApi.Comserver.COMTestManagement.ExportReport.archivePath "tts.core.api.comApi.Comserver.COMTestManagement.ExportReport.archivePath (Python parameter) — Path to directory or filename to copy the report to and to reference in test management (optional).")=`None`*, *[timeout](#tts.core.api.comApi.Comserver.COMTestManagement.ExportReport.timeout "tts.core.api.comApi.Comserver.COMTestManagement.ExportReport.timeout (Python parameter) — timeout in seconds to wait for the export to be finished (optional).")=`None`*)[¶](#tts.core.api.comApi.Comserver.COMTestManagement.ExportReport "Link to this definition")  
Exports the given project report file into the test management system. The archive path may be used to copy the report to another directory and to reference it from the test management entry.

Parameters:  filePath : str[¶](#tts.core.api.comApi.Comserver.COMTestManagement.ExportReport.filePath "Permalink to this definition")  
The filepath of the project report file to be exported

archivePath : str[¶](#tts.core.api.comApi.Comserver.COMTestManagement.ExportReport.archivePath "Permalink to this definition")  
Path to directory or filename to copy the report to and to reference in test management (optional).

timeout : int[¶](#tts.core.api.comApi.Comserver.COMTestManagement.ExportReport.timeout "Permalink to this definition")  
timeout in seconds to wait for the export to be finished (optional).

Raises:  
**exception** – If a user adapter is currently active. Or the test management system is not configured. Or the user is not authenticated.

GetActiveConfigurationName()[¶](#tts.core.api.comApi.Comserver.COMTestManagement.GetActiveConfigurationName "Link to this definition")  
Returns the name of the currently loaded test management configuration.

Returns:  name of test managemnt configuration

Return type:  str

GetConfigurationNames()[¶](#tts.core.api.comApi.Comserver.COMTestManagement.GetConfigurationNames "Link to this definition")  
Returns a list of all configuration names defined in the settings.

Returns:  list of configuration names

Return type:  list\<str\>

ImportPackage(*[tmPackagePath](#tts.core.api.comApi.Comserver.COMTestManagement.ImportPackage.tmPackagePath "tts.core.api.comApi.Comserver.COMTestManagement.ImportPackage.tmPackagePath (Python parameter) — Path specifying the package in the test management system, as it would be displayed in the import dialog. Only Unix styled paths (separated by forward slashes, "/") are allowed.")*, *[importPath](#tts.core.api.comApi.Comserver.COMTestManagement.ImportPackage.importPath "tts.core.api.comApi.Comserver.COMTestManagement.ImportPackage.importPath (Python parameter) — Directory, where the package should be placed (relative to package directory or absolute).")*, *[timeout](#tts.core.api.comApi.Comserver.COMTestManagement.ImportPackage.timeout "tts.core.api.comApi.Comserver.COMTestManagement.ImportPackage.timeout (Python parameter) — timeout in seconds to wait for the import to be finished (optional).")=`None`*)[¶](#tts.core.api.comApi.Comserver.COMTestManagement.ImportPackage "Link to this definition")  
Imports a package from a test management system. The tmPackagePath specifies the package in the test management system. The package will be imported into the directory given by importPath.

Parameters:  tmPackagePath : str[¶](#tts.core.api.comApi.Comserver.COMTestManagement.ImportPackage.tmPackagePath "Permalink to this definition")  
Path specifying the package in the test management system, as it would be displayed in the import dialog. Only Unix styled paths (separated by forward slashes, “/”) are allowed.

importPath : str[¶](#tts.core.api.comApi.Comserver.COMTestManagement.ImportPackage.importPath "Permalink to this definition")  
Directory, where the package should be placed (relative to package directory or absolute).

timeout : int[¶](#tts.core.api.comApi.Comserver.COMTestManagement.ImportPackage.timeout "Permalink to this definition")  
timeout in seconds to wait for the import to be finished (optional).

Raises:  
**exception** – If a user adapter is currently active. Or the test management system is not configured. Or the user is not authenticated.

ImportPackageAttributes(*[filePath](#tts.core.api.comApi.Comserver.COMTestManagement.ImportPackageAttributes.filePath "tts.core.api.comApi.Comserver.COMTestManagement.ImportPackageAttributes.filePath (Python parameter) — The file path of the package whose attributes have to be imported")*, *[timeout](#tts.core.api.comApi.Comserver.COMTestManagement.ImportPackageAttributes.timeout "tts.core.api.comApi.Comserver.COMTestManagement.ImportPackageAttributes.timeout (Python parameter) — timeout in seconds to wait for import to be finished (optional).")=`None`*)[¶](#tts.core.api.comApi.Comserver.COMTestManagement.ImportPackageAttributes "Link to this definition")  
Imports the attributes of a package from the test management system. The package must exist within the local workspace or an exception will be raised.

Parameters:  filePath : str[¶](#tts.core.api.comApi.Comserver.COMTestManagement.ImportPackageAttributes.filePath "Permalink to this definition")  
The file path of the package whose attributes have to be imported

timeout : int[¶](#tts.core.api.comApi.Comserver.COMTestManagement.ImportPackageAttributes.timeout "Permalink to this definition")  
timeout in seconds to wait for import to be finished (optional).

Raises:  
**exception** – If a user adapter is currently active. Or the test management system is not configured. Or the user is not authenticated.

ImportPackageById(*[tmPackageId](#tts.core.api.comApi.Comserver.COMTestManagement.ImportPackageById.tmPackageId "tts.core.api.comApi.Comserver.COMTestManagement.ImportPackageById.tmPackageId (Python parameter) — Id specifying the package in the test management system, as it would be displayed in the import dialog.")*, *[importPath](#tts.core.api.comApi.Comserver.COMTestManagement.ImportPackageById.importPath "tts.core.api.comApi.Comserver.COMTestManagement.ImportPackageById.importPath (Python parameter) — Directory, where the package should be placed (relative to package directory or absolute).")*, *[timeout](#tts.core.api.comApi.Comserver.COMTestManagement.ImportPackageById.timeout "tts.core.api.comApi.Comserver.COMTestManagement.ImportPackageById.timeout (Python parameter) — timeout in seconds to wait for the import to be finished (optional).")=`None`*)[¶](#tts.core.api.comApi.Comserver.COMTestManagement.ImportPackageById "Link to this definition")  
Imports a package from a test management system. The tmPackageId specifies the package in the test management system. The package will be imported into the directory given by importPath.

Parameters:  tmPackageId : str[¶](#tts.core.api.comApi.Comserver.COMTestManagement.ImportPackageById.tmPackageId "Permalink to this definition")  
Id specifying the package in the test management system, as it would be displayed in the import dialog.

importPath : str[¶](#tts.core.api.comApi.Comserver.COMTestManagement.ImportPackageById.importPath "Permalink to this definition")  
Directory, where the package should be placed (relative to package directory or absolute).

timeout : int[¶](#tts.core.api.comApi.Comserver.COMTestManagement.ImportPackageById.timeout "Permalink to this definition")  
timeout in seconds to wait for the import to be finished (optional).

Raises:  
**exception** – If a user adapter is currently active. Or the test management system is not configured. Or the user is not authenticated.

ImportPackageDirectory(*[tmDirectoryPath](#tts.core.api.comApi.Comserver.COMTestManagement.ImportPackageDirectory.tmDirectoryPath "tts.core.api.comApi.Comserver.COMTestManagement.ImportPackageDirectory.tmDirectoryPath (Python parameter) — Path specifying the directory in the test management system, as it would be displayed in the import dialog. Only Unix styled paths (separated by forward slashes, "/") are allowed.")*, *[importPath](#tts.core.api.comApi.Comserver.COMTestManagement.ImportPackageDirectory.importPath "tts.core.api.comApi.Comserver.COMTestManagement.ImportPackageDirectory.importPath (Python parameter) — Directory, where the imported directory should be placed (relative to package directory or absolute).")*, *[timeout](#tts.core.api.comApi.Comserver.COMTestManagement.ImportPackageDirectory.timeout "tts.core.api.comApi.Comserver.COMTestManagement.ImportPackageDirectory.timeout (Python parameter) — timeout in seconds to wait for import to be finished (optional).")=`None`*)[¶](#tts.core.api.comApi.Comserver.COMTestManagement.ImportPackageDirectory "Link to this definition")  
Imports a directory from a test management system with all subdirectories and packages. The tmDirectoryPath specifies the directory in the test management system. The directory will be imported into the directory given by importPath.

Parameters:  tmDirectoryPath : str[¶](#tts.core.api.comApi.Comserver.COMTestManagement.ImportPackageDirectory.tmDirectoryPath "Permalink to this definition")  
Path specifying the directory in the test management system, as it would be displayed in the import dialog. Only Unix styled paths (separated by forward slashes, “/”) are allowed.

importPath : str[¶](#tts.core.api.comApi.Comserver.COMTestManagement.ImportPackageDirectory.importPath "Permalink to this definition")  
Directory, where the imported directory should be placed (relative to package directory or absolute).

timeout : int[¶](#tts.core.api.comApi.Comserver.COMTestManagement.ImportPackageDirectory.timeout "Permalink to this definition")  
timeout in seconds to wait for import to be finished (optional).

Raises:  
**exception** – If a user adapter is currently active. Or the test management system is not configured. Or the user is not authenticated.

ImportProject(*[tmProjectPath](#tts.core.api.comApi.Comserver.COMTestManagement.ImportProject.tmProjectPath "tts.core.api.comApi.Comserver.COMTestManagement.ImportProject.tmProjectPath (Python parameter) — Path specifying the project in the test management system, as it would be displayed in the import dialog. Only Unix styled paths (separated by forward slashes, "/") are allowed.")*, *[importPath](#tts.core.api.comApi.Comserver.COMTestManagement.ImportProject.importPath "tts.core.api.comApi.Comserver.COMTestManagement.ImportProject.importPath (Python parameter) — Directory, where the project should be placed (relative to package directory or absolute).")*, *[importMissingPackages](#tts.core.api.comApi.Comserver.COMTestManagement.ImportProject.importMissingPackages "tts.core.api.comApi.Comserver.COMTestManagement.ImportProject.importMissingPackages (Python parameter) — If set, missing packages will be automatically imported.")=`False`*, *[timeout](#tts.core.api.comApi.Comserver.COMTestManagement.ImportProject.timeout "tts.core.api.comApi.Comserver.COMTestManagement.ImportProject.timeout (Python parameter) — timeout in seconds to wait for the import to be finished (optional).")=`None`*, *[parameters](#tts.core.api.comApi.Comserver.COMTestManagement.ImportProject.parameters "tts.core.api.comApi.Comserver.COMTestManagement.ImportProject.parameters (Python parameter) — A list of tuples (name, value) of length two for each adapter parameter to be temporarily changed for the duration of the project import.")=`None`*)[¶](#tts.core.api.comApi.Comserver.COMTestManagement.ImportProject "Link to this definition")  
Imports a project from a test management system. The tmProjectPath specifies the project in the test management system. The project will be imported into the directory given by importPath.

Parameters:  tmProjectPath : str[¶](#tts.core.api.comApi.Comserver.COMTestManagement.ImportProject.tmProjectPath "Permalink to this definition")  
Path specifying the project in the test management system, as it would be displayed in the import dialog. Only Unix styled paths (separated by forward slashes, “/”) are allowed.

importPath : str[¶](#tts.core.api.comApi.Comserver.COMTestManagement.ImportProject.importPath "Permalink to this definition")  
Directory, where the project should be placed (relative to package directory or absolute).

importMissingPackages : bool[¶](#tts.core.api.comApi.Comserver.COMTestManagement.ImportProject.importMissingPackages "Permalink to this definition")  
If set, missing packages will be automatically imported.

timeout : int[¶](#tts.core.api.comApi.Comserver.COMTestManagement.ImportProject.timeout "Permalink to this definition")  
timeout in seconds to wait for the import to be finished (optional).

parameters : list\<tuple\>[¶](#tts.core.api.comApi.Comserver.COMTestManagement.ImportProject.parameters "Permalink to this definition")  
A list of tuples (name, value) of length two for each adapter parameter to be temporarily changed for the duration of the project import. Due to technical restrictions of the COM interface the parameter values must not contain dictionaries.Following adapter parameters can be set: Suite Run Query (only ALM Octane), Test Suite Query (only ALM Octane)

Raises:  
**exception** – If a user adapter is currently active. Or the test management system is not configured. Or the user is not authenticated.

ImportProjectAttributes(*[filePath](#tts.core.api.comApi.Comserver.COMTestManagement.ImportProjectAttributes.filePath "tts.core.api.comApi.Comserver.COMTestManagement.ImportProjectAttributes.filePath (Python parameter) — The file path of the project whose attributes have to be imported")*, *[timeout](#tts.core.api.comApi.Comserver.COMTestManagement.ImportProjectAttributes.timeout "tts.core.api.comApi.Comserver.COMTestManagement.ImportProjectAttributes.timeout (Python parameter) — timeout in seconds to wait for import to be finished (optional).")=`None`*)[¶](#tts.core.api.comApi.Comserver.COMTestManagement.ImportProjectAttributes "Link to this definition")  
Imports the attributes of a project from the test management system. The project must exist within the local workspace or an exception will be raised.

Parameters:  filePath : str[¶](#tts.core.api.comApi.Comserver.COMTestManagement.ImportProjectAttributes.filePath "Permalink to this definition")  
The file path of the project whose attributes have to be imported

timeout : int[¶](#tts.core.api.comApi.Comserver.COMTestManagement.ImportProjectAttributes.timeout "Permalink to this definition")  
timeout in seconds to wait for import to be finished (optional).

Raises:  
**exception** – If a user adapter is currently active. Or the test management system is not configured. Or the user is not authenticated.

ImportProjectById(*[tmProjectId](#tts.core.api.comApi.Comserver.COMTestManagement.ImportProjectById.tmProjectId "tts.core.api.comApi.Comserver.COMTestManagement.ImportProjectById.tmProjectId (Python parameter) — Id specifying the project in the test management system, as it would be displayed in the import dialog.")*, *[importPath](#tts.core.api.comApi.Comserver.COMTestManagement.ImportProjectById.importPath "tts.core.api.comApi.Comserver.COMTestManagement.ImportProjectById.importPath (Python parameter) — Directory, where the project should be placed (relative to package directory or absolute).")*, *[importMissingPackages](#tts.core.api.comApi.Comserver.COMTestManagement.ImportProjectById.importMissingPackages "tts.core.api.comApi.Comserver.COMTestManagement.ImportProjectById.importMissingPackages (Python parameter) — If set, missing packages will be automatically imported.")=`False`*, *[timeout](#tts.core.api.comApi.Comserver.COMTestManagement.ImportProjectById.timeout "tts.core.api.comApi.Comserver.COMTestManagement.ImportProjectById.timeout (Python parameter) — timeout in seconds to wait for the import to be finished (optional).")=`None`*)[¶](#tts.core.api.comApi.Comserver.COMTestManagement.ImportProjectById "Link to this definition")  
Imports a project from a test management system. The tmProjectId specifies the project in the test management system. The project will be imported into the directory given by importPath.

Parameters:  tmProjectId : str[¶](#tts.core.api.comApi.Comserver.COMTestManagement.ImportProjectById.tmProjectId "Permalink to this definition")  
Id specifying the project in the test management system, as it would be displayed in the import dialog.

importPath : str[¶](#tts.core.api.comApi.Comserver.COMTestManagement.ImportProjectById.importPath "Permalink to this definition")  
Directory, where the project should be placed (relative to package directory or absolute).

importMissingPackages : bool[¶](#tts.core.api.comApi.Comserver.COMTestManagement.ImportProjectById.importMissingPackages "Permalink to this definition")  
If set, missing packages will be automatically imported.

timeout : int[¶](#tts.core.api.comApi.Comserver.COMTestManagement.ImportProjectById.timeout "Permalink to this definition")  
timeout in seconds to wait for the import to be finished (optional).

Raises:  
**exception** – If a user adapter is currently active. Or the test management system is not configured. Or the user is not authenticated.

ImportProjectDirectory(*[tmDirectoryPath](#tts.core.api.comApi.Comserver.COMTestManagement.ImportProjectDirectory.tmDirectoryPath "tts.core.api.comApi.Comserver.COMTestManagement.ImportProjectDirectory.tmDirectoryPath (Python parameter) — Path specifying the directory in the test management system, as it would be displayed in the import dialog. Only Unix styled paths (separated by forward slashes, "/") are allowed.")*, *[importPath](#tts.core.api.comApi.Comserver.COMTestManagement.ImportProjectDirectory.importPath "tts.core.api.comApi.Comserver.COMTestManagement.ImportProjectDirectory.importPath (Python parameter) — Directory, where the imported directory should be placed (relative to package directory or absolute).")*, *[timeout](#tts.core.api.comApi.Comserver.COMTestManagement.ImportProjectDirectory.timeout "tts.core.api.comApi.Comserver.COMTestManagement.ImportProjectDirectory.timeout (Python parameter) — timeout in seconds to wait for import to be finished (optional).")=`None`*, *[parameters](#tts.core.api.comApi.Comserver.COMTestManagement.ImportProjectDirectory.parameters "tts.core.api.comApi.Comserver.COMTestManagement.ImportProjectDirectory.parameters (Python parameter) — A list of tuples (name, value) of length two for each adapter parameter to be temporarily changed for the duration of the project import.")=`None`*)[¶](#tts.core.api.comApi.Comserver.COMTestManagement.ImportProjectDirectory "Link to this definition")  
Imports a directory from a test management system with all subdirectories and projects. The tmDirectoryPath specifies the directory in the test management system. The directory will be imported into the directory given by importPath.

Parameters:  tmDirectoryPath : str[¶](#tts.core.api.comApi.Comserver.COMTestManagement.ImportProjectDirectory.tmDirectoryPath "Permalink to this definition")  
Path specifying the directory in the test management system, as it would be displayed in the import dialog. Only Unix styled paths (separated by forward slashes, “/”) are allowed.

importPath : str[¶](#tts.core.api.comApi.Comserver.COMTestManagement.ImportProjectDirectory.importPath "Permalink to this definition")  
Directory, where the imported directory should be placed (relative to package directory or absolute).

timeout : int[¶](#tts.core.api.comApi.Comserver.COMTestManagement.ImportProjectDirectory.timeout "Permalink to this definition")  
timeout in seconds to wait for import to be finished (optional).

parameters : list\<tuple\>[¶](#tts.core.api.comApi.Comserver.COMTestManagement.ImportProjectDirectory.parameters "Permalink to this definition")  
A list of tuples (name, value) of length two for each adapter parameter to be temporarily changed for the duration of the project import. Due to technical restrictions of the COM interface the parameter values must not contain dictionaries. Following adapter parameters can be set: Suite Run Query (only ALM Octane), Test Suite Query (only ALM Octane)

Raises:  
**exception** – If a user adapter is currently active. Or the test management system is not configured. Or the user is not authenticated.

IsLoggedIn()[¶](#tts.core.api.comApi.Comserver.COMTestManagement.IsLoggedIn "Link to this definition")  
Returns True if ecu.test is currently logged in the Testmanagement system, else False

Returns:  True if ecu.test is currently logged in the Testmanagement system, else False

Return type:  bool

Raises:  
**exception** – If a user adapter is currently active.

IsTmsAvailable()[¶](#tts.core.api.comApi.Comserver.COMTestManagement.IsTmsAvailable "Link to this definition")  
Checks if the test management service is available.

Returns:  True if the service is available, otherwise False.

Return type:  bool

LinkAndSyncProject(*[filePath](#tts.core.api.comApi.Comserver.COMTestManagement.LinkAndSyncProject.filePath "tts.core.api.comApi.Comserver.COMTestManagement.LinkAndSyncProject.filePath (Python parameter) — The file path of the project to be linked and synced (relative to package directory or absolute).")*, *[tmProjectPath](#tts.core.api.comApi.Comserver.COMTestManagement.LinkAndSyncProject.tmProjectPath "tts.core.api.comApi.Comserver.COMTestManagement.LinkAndSyncProject.tmProjectPath (Python parameter) — Path specifying the project in the test management system, as it would be displayed in the import dialog. Only Unix styled paths (separated by forward slashes, "/") are allowed.")*)[¶](#tts.core.api.comApi.Comserver.COMTestManagement.LinkAndSyncProject "Link to this definition")  
Links a project from ecu.test with a test suite in the test management system and synchronizes the contained test cases.

Parameters:  filePath : str[¶](#tts.core.api.comApi.Comserver.COMTestManagement.LinkAndSyncProject.filePath "Permalink to this definition")  
The file path of the project to be linked and synced (relative to package directory or absolute).

tmProjectPath : str[¶](#tts.core.api.comApi.Comserver.COMTestManagement.LinkAndSyncProject.tmProjectPath "Permalink to this definition")  
Path specifying the project in the test management system, as it would be displayed in the import dialog. Only Unix styled paths (separated by forward slashes, “/”) are allowed.

Returns:  Empty list on success, otherwise a list of messages from unsynced test cases.

Return type:  list\<string\>

Raises:  
**exception** – If a user adapter is currently active. Or the test management system is not configured. Or the user is not authenticated.

Login(*[user](#tts.core.api.comApi.Comserver.COMTestManagement.Login.user "tts.core.api.comApi.Comserver.COMTestManagement.Login.user (Python parameter) — User to be logged in")*, *[password](#tts.core.api.comApi.Comserver.COMTestManagement.Login.password "tts.core.api.comApi.Comserver.COMTestManagement.Login.password (Python parameter) — Password of the user")*)[¶](#tts.core.api.comApi.Comserver.COMTestManagement.Login "Link to this definition")  
Performs a login to the preconfigured testmanagement service.

Info

Will try a “Basic” Authentication regardless of the configuration.

Parameters:  user : str[¶](#tts.core.api.comApi.Comserver.COMTestManagement.Login.user "Permalink to this definition")  
User to be logged in

password : str[¶](#tts.core.api.comApi.Comserver.COMTestManagement.Login.password "Permalink to this definition")  
Password of the user

Returns:  True if login succeeded, else False

Return type:  bool

Raises:  
**exception** – If a user adapter is currently active.

Logout()[¶](#tts.core.api.comApi.Comserver.COMTestManagement.Logout "Link to this definition")  
Performs a logout from the preconfigured testmanagement service.

Returns:  True if logout succeeded, else False

Return type:  bool

Raises:  
**exception** – If a user adapter is currently active.

SetActiveConfiguration(*[configName](#tts.core.api.comApi.Comserver.COMTestManagement.SetActiveConfiguration.configName "tts.core.api.comApi.Comserver.COMTestManagement.SetActiveConfiguration.configName (Python parameter) — Name of the test management configuration")*)[¶](#tts.core.api.comApi.Comserver.COMTestManagement.SetActiveConfiguration "Link to this definition")  
Activate the specified test management configuration.

Parameters:  configName : str[¶](#tts.core.api.comApi.Comserver.COMTestManagement.SetActiveConfiguration.configName "Permalink to this definition")  
Name of the test management configuration

UpdateAttributeDefinitions(*[timeout](#tts.core.api.comApi.Comserver.COMTestManagement.UpdateAttributeDefinitions.timeout "tts.core.api.comApi.Comserver.COMTestManagement.UpdateAttributeDefinitions.timeout (Python parameter) — timeout in seconds to wait for import to be finished (optional).")=`None`*)[¶](#tts.core.api.comApi.Comserver.COMTestManagement.UpdateAttributeDefinitions "Link to this definition")  
Updates the attribute definitions with attributes of the currently configured test management system.

Parameters:  timeout : int[¶](#tts.core.api.comApi.Comserver.COMTestManagement.UpdateAttributeDefinitions.timeout "Permalink to this definition")  
timeout in seconds to wait for import to be finished (optional).

Raises:  
**exception** – If a user adapter is currently active. Or the test management system is not configured. Or the user is not authenticated.

## COMTestReport[¶](#comtestreport "Link to this heading")

*class* COMTestReport[¶](#tts.core.api.comApi.Comserver.COMTestReport "Link to this definition")  
This object gives access to the test report of the current or most recent testrun

Count[¶](#tts.core.api.comApi.Comserver.COMTestReport.Count "Link to this definition")  
returns the number of items in this test report. If the package was not executed yet GetCount will return 0. See: `IsOk`

Returns:  the number of items.

Return type:  int

Activity(*[idx](#tts.core.api.comApi.Comserver.COMTestReport.Activity.idx "tts.core.api.comApi.Comserver.COMTestReport.Activity.idx (Python parameter) — the index of the item to obtain the test step's activity.")*)[¶](#tts.core.api.comApi.Comserver.COMTestReport.Activity "Link to this definition")  
returns the test step’s activity of the item with the specified index.

Parameters:  idx : int[¶](#tts.core.api.comApi.Comserver.COMTestReport.Activity.idx "Permalink to this definition")  
the index of the item to obtain the test step’s activity.

Returns:  the test step’s activity of the specified item

Return type:  str

Comment(*[idx](#tts.core.api.comApi.Comserver.COMTestReport.Comment.idx "tts.core.api.comApi.Comserver.COMTestReport.Comment.idx (Python parameter) — the index of the item to obtain the comment.")*)[¶](#tts.core.api.comApi.Comserver.COMTestReport.Comment "Link to this definition")  
returns the test step’s comment of the item with the specified index.

Parameters:  idx : int[¶](#tts.core.api.comApi.Comserver.COMTestReport.Comment.idx "Permalink to this definition")  
the index of the item to obtain the comment.

Returns:  the comment of the specified item

Return type:  str

GetAnalysisJobFiles(*[extract](#tts.core.api.comApi.Comserver.COMTestReport.GetAnalysisJobFiles.extract "tts.core.api.comApi.Comserver.COMTestReport.GetAnalysisJobFiles.extract (Python parameter) — If true, extract the analysis job files into the report folder")=`True`*)[¶](#tts.core.api.comApi.Comserver.COMTestReport.GetAnalysisJobFiles "Link to this definition")  
Get absolute file paths to all analysis jobs within the report.

Info

The files may not be present anymore on the filesystem.

Parameters:  extract : bool[¶](#tts.core.api.comApi.Comserver.COMTestReport.GetAnalysisJobFiles.extract "Permalink to this definition")  
If true, extract the analysis job files into the report folder

Returns:  list of file paths

Return type:  list\<str\>

GetCount()[¶](#tts.core.api.comApi.Comserver.COMTestReport.GetCount "Link to this definition")  
returns the number of items in this test report. If the package was not executed yet GetCount will return 0. See: `IsOk`

Returns:  the number of items.

Return type:  int

Index(*[idx](#tts.core.api.comApi.Comserver.COMTestReport.Index.idx "tts.core.api.comApi.Comserver.COMTestReport.Index.idx (Python parameter) — the index of the item to obtain the name.")*)[¶](#tts.core.api.comApi.Comserver.COMTestReport.Index "Link to this definition")  
returns the index of the item with the specified index.

Parameters:  idx : int[¶](#tts.core.api.comApi.Comserver.COMTestReport.Index.idx "Permalink to this definition")  
the index of the item to obtain the name.

Returns:  the name of the specified item

Return type:  str

Info(*[idx](#tts.core.api.comApi.Comserver.COMTestReport.Info.idx "tts.core.api.comApi.Comserver.COMTestReport.Info.idx (Python parameter) — the index of the item to obtain the info field.")*)[¶](#tts.core.api.comApi.Comserver.COMTestReport.Info "Link to this definition")  
returns the info field’s value of the item with the specified index.

Parameters:  idx : int[¶](#tts.core.api.comApi.Comserver.COMTestReport.Info.idx "Permalink to this definition")  
the index of the item to obtain the info field.

Returns:  the info field’s value of the specified item

Return type:  str

IsOk()[¶](#tts.core.api.comApi.Comserver.COMTestReport.IsOk "Link to this definition")  
This method can be used to check if this test report is valid or more precisely the package was already executed and a test report is available.

Returns:  True, if this test report is valid, otherwise False. It is a convenience function for:

    GetCount() > 0

Return type:  bool

Item(*[idx](#tts.core.api.comApi.Comserver.COMTestReport.Item "tts.core.api.comApi.Comserver.COMTestReport.Item.idx (Python parameter)")*)[¶](#tts.core.api.comApi.Comserver.COMTestReport.Item "Link to this definition")  
See: `Result`

Name(*[idx](#tts.core.api.comApi.Comserver.COMTestReport.Name.idx "tts.core.api.comApi.Comserver.COMTestReport.Name.idx (Python parameter) — the index of the item to obtain the name.")*)[¶](#tts.core.api.comApi.Comserver.COMTestReport.Name "Link to this definition")  
returns the name of the item with the specified index.

Parameters:  idx : int[¶](#tts.core.api.comApi.Comserver.COMTestReport.Name.idx "Permalink to this definition")  
the index of the item to obtain the name.

Returns:  the name of the specified item

Return type:  str

Result(*[idx](#tts.core.api.comApi.Comserver.COMTestReport.Result.idx "tts.core.api.comApi.Comserver.COMTestReport.Result.idx (Python parameter) — the index of the item to obtain the result.")*)[¶](#tts.core.api.comApi.Comserver.COMTestReport.Result "Link to this definition")  
returns the result of the item with the specified index.

Parameters:  idx : int[¶](#tts.core.api.comApi.Comserver.COMTestReport.Result.idx "Permalink to this definition")  
the index of the item to obtain the result.

Returns:  the result of the specified item

Return type:  str

TimeStamp(*[idx](#tts.core.api.comApi.Comserver.COMTestReport.TimeStamp.idx "tts.core.api.comApi.Comserver.COMTestReport.TimeStamp.idx (Python parameter) — the index of the item to obtain the time stamp.")*)[¶](#tts.core.api.comApi.Comserver.COMTestReport.TimeStamp "Link to this definition")  
returns the time stamp of the item with the specified index.

Parameters:  idx : int[¶](#tts.core.api.comApi.Comserver.COMTestReport.TimeStamp.idx "Permalink to this definition")  
the index of the item to obtain the time stamp.

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

Item(*[idxOrName](#tts.core.api.comApi.Comserver.COMVariables.Item.idxOrName "tts.core.api.comApi.Comserver.COMVariables.Item.idxOrName (Python parameter) — The name of the variable or an index")*)[¶](#tts.core.api.comApi.Comserver.COMVariables.Item "Link to this definition")  
returns a specified variable. idxOrName can be either the name or an index. If an index is given then it should be larger than 0 and lesser the number of variables. The count of variables can be determined with `GetCount`

Parameters:  idxOrName[¶](#tts.core.api.comApi.Comserver.COMVariables.Item.idxOrName "Permalink to this definition")  
The name of the variable or an index

Returns:  the variable.

Return type:  [`COMVariable`](#tts.core.api.comApi.Comserver.COMVariable "tts.core.api.comApi.Comserver.COMVariable (Python class) — This object gives access to the properties of a variable.")

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
