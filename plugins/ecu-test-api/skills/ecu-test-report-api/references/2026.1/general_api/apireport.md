[ Internal APIs ](api.md)

[ Advanced operations of package variable types ](variabledatastructures.md)

[ Advanced properties of bus-related objects ](busdatastructures.md)

[ Bus related objects of trace analysis ](busdatastructuresTraceanalysis.md)

[ Advanced properties of diagnostics-related objects ](diagdatastructures.md)

[ Diagnostics related objects of trace analysis ](diagdatastructuresTraceanalysis.md)

[ Advanced properties of media-related objects ](mediadatastructures.md)

[ Advanced properties of DLT logging-related objects ](dltdatastructures.md)

[ COM API ](com-api.md)

[ REST API ](rest-api.md)

Report API [ Report API ](#)

Report API

- [ ReportApi ](#id1)
  - [C ReportApi ](#tts.core.report.parser.ReportApi.ReportApi)
    - [M AnalysePath ](#tts.core.report.parser.ReportApi.ReportApi.AnalysePath)
    - [M GetArtifacts ](#tts.core.report.parser.ReportApi.ReportApi.GetArtifacts)
    - [M GetConfiguration ](#tts.core.report.parser.ReportApi.ReportApi.GetConfiguration)
    - [M GetDbDir ](#tts.core.report.parser.ReportApi.ReportApi.GetDbDir)
    - [M GetDbFile ](#tts.core.report.parser.ReportApi.ReportApi.GetDbFile)
    - [M GetInfo ](#tts.core.report.parser.ReportApi.ReportApi.GetInfo)
    - [M GetMainPackage ](#tts.core.report.parser.ReportApi.ReportApi.GetMainPackage)
    - [M GetMainProject ](#tts.core.report.parser.ReportApi.ReportApi.GetMainProject)
    - [M GetPackage ](#tts.core.report.parser.ReportApi.ReportApi.GetPackage)
    - [M GetPatchInfo ](#tts.core.report.parser.ReportApi.ReportApi.GetPatchInfo)
    - [M GetReportDir ](#tts.core.report.parser.ReportApi.ReportApi.GetReportDir)
    - [M GetResultBgColor ](#tts.core.report.parser.ReportApi.ReportApi.GetResultBgColor)
    - [M GetResultColor ](#tts.core.report.parser.ReportApi.ReportApi.GetResultColor)
    - [M GetResultTxtColor ](#tts.core.report.parser.ReportApi.ReportApi.GetResultTxtColor)
    - [M GetRootActivity ](#tts.core.report.parser.ReportApi.ReportApi.GetRootActivity)
    - [M GetSetting ](#tts.core.report.parser.ReportApi.ReportApi.GetSetting)
    - [M GetSrcColor ](#tts.core.report.parser.ReportApi.ReportApi.GetSrcColor)
    - [M GetSrcStyle ](#tts.core.report.parser.ReportApi.ReportApi.GetSrcStyle)
    - [M GetTemplateDir ](#tts.core.report.parser.ReportApi.ReportApi.GetTemplateDir)
    - [M HasConfiguration ](#tts.core.report.parser.ReportApi.ReportApi.HasConfiguration)
    - [M IsFiltered ](#tts.core.report.parser.ReportApi.ReportApi.IsFiltered)
    - [M IsProjectReport ](#tts.core.report.parser.ReportApi.ReportApi.IsProjectReport)
    - [M IsSet ](#tts.core.report.parser.ReportApi.ReportApi.IsSet)
    - [M IterItems ](#tts.core.report.parser.ReportApi.ReportApi.IterItems)
    - [M MakeAbsPath ](#tts.core.report.parser.ReportApi.ReportApi.MakeAbsPath)
    - [M SetSetting ](#tts.core.report.parser.ReportApi.ReportApi.SetSetting)
    - [M GetPackageScmInfo ](#tts.core.report.parser.ReportApi.ReportApi.GetPackageScmInfo)
    - [M IterUserComments ](#tts.core.report.parser.ReportApi.ReportApi.IterUserComments)
- [ Artifact ](#artifact)
  - [C Artifact ](#tts.core.report.db.Artifact.Artifact)
    - [M GetContext ](#tts.core.report.db.Artifact.Artifact.GetContext)
    - [M GetFileHash ](#tts.core.report.db.Artifact.Artifact.GetFileHash)
    - [M GetFileName ](#tts.core.report.db.Artifact.Artifact.GetFileName)
    - [M GetFilePath ](#tts.core.report.db.Artifact.Artifact.GetFilePath)
    - [M GetId ](#tts.core.report.db.Artifact.Artifact.GetId)
    - [M GetMainPackageReportItemId ](#tts.core.report.db.Artifact.Artifact.GetMainPackageReportItemId)
- [ Attribute ](#attribute)
  - [C Attribute ](#tts.core.report.db.Attribute.Attribute)
    - [M GetId ](#tts.core.report.db.Attribute.Attribute.GetId)
    - [M GetName ](#tts.core.report.db.Attribute.Attribute.GetName)
    - [M GetOrigin ](#tts.core.report.db.Attribute.Attribute.GetOrigin)
    - [M GetReportItemId ](#tts.core.report.db.Attribute.Attribute.GetReportItemId)
    - [M GetValue ](#tts.core.report.db.Attribute.Attribute.GetValue)
- [ Configuration ](#module-tts.core.report.parser.Configuration)
  - [C Configuration ](#tts.core.report.parser.Configuration.Configuration)
    - [M GetTestBenchConfiguration ](#tts.core.report.parser.Configuration.Configuration.GetTestBenchConfiguration)
    - [M GetTestConfiguration ](#tts.core.report.parser.Configuration.Configuration.GetTestConfiguration)
    - [M HasTestBenchConfiguration ](#tts.core.report.parser.Configuration.Configuration.HasTestBenchConfiguration)
    - [M HasTestConfiguration ](#tts.core.report.parser.Configuration.Configuration.HasTestConfiguration)
  - [C PrfTestBenchConfiguration ](#tts.core.report.parser.Configuration.PrfTestBenchConfiguration)
    - [A PLibraryId ](#tts.core.report.parser.Configuration.PrfTestBenchConfiguration.PLibraryId)
    - [M GetId ](#tts.core.report.parser.Configuration.PrfTestBenchConfiguration.GetId)
    - [M GetLibraryId ](#tts.core.report.parser.Configuration.PrfTestBenchConfiguration.GetLibraryId)
    - [M GetName ](#tts.core.report.parser.Configuration.PrfTestBenchConfiguration.GetName)
    - [M GetPath ](#tts.core.report.parser.Configuration.PrfTestBenchConfiguration.GetPath)
    - [M GetTbcId ](#tts.core.report.parser.Configuration.PrfTestBenchConfiguration.GetTbcId)
    - [M GetTools ](#tts.core.report.parser.Configuration.PrfTestBenchConfiguration.GetTools)
    - [M HasTools ](#tts.core.report.parser.Configuration.PrfTestBenchConfiguration.HasTools)
    - [M IterTools ](#tts.core.report.parser.Configuration.PrfTestBenchConfiguration.IterTools)
  - [C PrfTestConfiguration ](#tts.core.report.parser.Configuration.PrfTestConfiguration)
    - [A PLibraryId ](#tts.core.report.parser.Configuration.PrfTestConfiguration.PLibraryId)
    - [M GetDataDir ](#tts.core.report.parser.Configuration.PrfTestConfiguration.GetDataDir)
    - [M GetEditor ](#tts.core.report.parser.Configuration.PrfTestConfiguration.GetEditor)
    - [M GetId ](#tts.core.report.parser.Configuration.PrfTestConfiguration.GetId)
    - [M GetLibraryId ](#tts.core.report.parser.Configuration.PrfTestConfiguration.GetLibraryId)
    - [M GetMappingFile ](#tts.core.report.parser.Configuration.PrfTestConfiguration.GetMappingFile)
    - [M GetName ](#tts.core.report.parser.Configuration.PrfTestConfiguration.GetName)
    - [M GetPath ](#tts.core.report.parser.Configuration.PrfTestConfiguration.GetPath)
    - [M GetPkgDir ](#tts.core.report.parser.Configuration.PrfTestConfiguration.GetPkgDir)
    - [M GetTcfId ](#tts.core.report.parser.Configuration.PrfTestConfiguration.GetTcfId)
    - [M GetTeststand ](#tts.core.report.parser.Configuration.PrfTestConfiguration.GetTeststand)
    - [M HasBusConfigurations ](#tts.core.report.parser.Configuration.PrfTestConfiguration.HasBusConfigurations)
    - [M HasConstFiles ](#tts.core.report.parser.Configuration.PrfTestConfiguration.HasConstFiles)
    - [M HasEcuConfigurations ](#tts.core.report.parser.Configuration.PrfTestConfiguration.HasEcuConfigurations)
    - [M HasEfsConfigurations ](#tts.core.report.parser.Configuration.PrfTestConfiguration.HasEfsConfigurations)
    - [M HasFunctionConfigurations ](#tts.core.report.parser.Configuration.PrfTestConfiguration.HasFunctionConfigurations)
    - [M HasModelConfigurations ](#tts.core.report.parser.Configuration.PrfTestConfiguration.HasModelConfigurations)
    - [M IterBusConfigurations ](#tts.core.report.parser.Configuration.PrfTestConfiguration.IterBusConfigurations)
    - [M IterConstFiles ](#tts.core.report.parser.Configuration.PrfTestConfiguration.IterConstFiles)
    - [M IterEcuConfigurations ](#tts.core.report.parser.Configuration.PrfTestConfiguration.IterEcuConfigurations)
    - [M IterEfsConfigurations ](#tts.core.report.parser.Configuration.PrfTestConfiguration.IterEfsConfigurations)
    - [M IterFunctionConfigurations ](#tts.core.report.parser.Configuration.PrfTestConfiguration.IterFunctionConfigurations)
    - [M IterMappingFiles ](#tts.core.report.parser.Configuration.PrfTestConfiguration.IterMappingFiles)
    - [M IterModelConfigurations ](#tts.core.report.parser.Configuration.PrfTestConfiguration.IterModelConfigurations)
  - [C TestBenchConfiguration ](#tts.core.report.parser.Configuration.TestBenchConfiguration)
    - [A PLibraryId ](#tts.core.report.parser.Configuration.TestBenchConfiguration.PLibraryId)
    - [M GetId ](#tts.core.report.parser.Configuration.TestBenchConfiguration.GetId)
    - [M GetLibraryId ](#tts.core.report.parser.Configuration.TestBenchConfiguration.GetLibraryId)
    - [M GetName ](#tts.core.report.parser.Configuration.TestBenchConfiguration.GetName)
    - [M GetPath ](#tts.core.report.parser.Configuration.TestBenchConfiguration.GetPath)
    - [M GetTbcId ](#tts.core.report.parser.Configuration.TestBenchConfiguration.GetTbcId)
    - [M GetTools ](#tts.core.report.parser.Configuration.TestBenchConfiguration.GetTools)
    - [M HasTools ](#tts.core.report.parser.Configuration.TestBenchConfiguration.HasTools)
    - [M IterTools ](#tts.core.report.parser.Configuration.TestBenchConfiguration.IterTools)
  - [C TestConfiguration ](#tts.core.report.parser.Configuration.TestConfiguration)
    - [A PLibraryId ](#tts.core.report.parser.Configuration.TestConfiguration.PLibraryId)
    - [M GetDataDir ](#tts.core.report.parser.Configuration.TestConfiguration.GetDataDir)
    - [M GetEditor ](#tts.core.report.parser.Configuration.TestConfiguration.GetEditor)
    - [M GetId ](#tts.core.report.parser.Configuration.TestConfiguration.GetId)
    - [M GetLibraryId ](#tts.core.report.parser.Configuration.TestConfiguration.GetLibraryId)
    - [M GetName ](#tts.core.report.parser.Configuration.TestConfiguration.GetName)
    - [M GetPath ](#tts.core.report.parser.Configuration.TestConfiguration.GetPath)
    - [M GetPkgDir ](#tts.core.report.parser.Configuration.TestConfiguration.GetPkgDir)
    - [M GetTcfId ](#tts.core.report.parser.Configuration.TestConfiguration.GetTcfId)
    - [M GetTeststand ](#tts.core.report.parser.Configuration.TestConfiguration.GetTeststand)
    - [M HasBusConfigurations ](#tts.core.report.parser.Configuration.TestConfiguration.HasBusConfigurations)
    - [M HasConstFiles ](#tts.core.report.parser.Configuration.TestConfiguration.HasConstFiles)
    - [M HasEcuConfigurations ](#tts.core.report.parser.Configuration.TestConfiguration.HasEcuConfigurations)
    - [M HasEfsConfigurations ](#tts.core.report.parser.Configuration.TestConfiguration.HasEfsConfigurations)
    - [M HasFunctionConfigurations ](#tts.core.report.parser.Configuration.TestConfiguration.HasFunctionConfigurations)
    - [M HasModelConfigurations ](#tts.core.report.parser.Configuration.TestConfiguration.HasModelConfigurations)
    - [M IterBusConfigurations ](#tts.core.report.parser.Configuration.TestConfiguration.IterBusConfigurations)
    - [M IterConstFiles ](#tts.core.report.parser.Configuration.TestConfiguration.IterConstFiles)
    - [M IterEcuConfigurations ](#tts.core.report.parser.Configuration.TestConfiguration.IterEcuConfigurations)
    - [M IterEfsConfigurations ](#tts.core.report.parser.Configuration.TestConfiguration.IterEfsConfigurations)
    - [M IterFunctionConfigurations ](#tts.core.report.parser.Configuration.TestConfiguration.IterFunctionConfigurations)
    - [M IterMappingFiles ](#tts.core.report.parser.Configuration.TestConfiguration.IterMappingFiles)
    - [M IterModelConfigurations ](#tts.core.report.parser.Configuration.TestConfiguration.IterModelConfigurations)
  - [C TrfTestBenchConfiguration ](#tts.core.report.parser.Configuration.TrfTestBenchConfiguration)
    - [A PLibraryId ](#tts.core.report.parser.Configuration.TrfTestBenchConfiguration.PLibraryId)
    - [M GetId ](#tts.core.report.parser.Configuration.TrfTestBenchConfiguration.GetId)
    - [M GetLibraryId ](#tts.core.report.parser.Configuration.TrfTestBenchConfiguration.GetLibraryId)
    - [M GetName ](#tts.core.report.parser.Configuration.TrfTestBenchConfiguration.GetName)
    - [M GetPath ](#tts.core.report.parser.Configuration.TrfTestBenchConfiguration.GetPath)
    - [M GetTbcId ](#tts.core.report.parser.Configuration.TrfTestBenchConfiguration.GetTbcId)
    - [M GetTools ](#tts.core.report.parser.Configuration.TrfTestBenchConfiguration.GetTools)
    - [M HasTools ](#tts.core.report.parser.Configuration.TrfTestBenchConfiguration.HasTools)
    - [M IterTools ](#tts.core.report.parser.Configuration.TrfTestBenchConfiguration.IterTools)
  - [C TrfTestConfiguration ](#tts.core.report.parser.Configuration.TrfTestConfiguration)
    - [A PLibraryId ](#tts.core.report.parser.Configuration.TrfTestConfiguration.PLibraryId)
    - [M GetDataDir ](#tts.core.report.parser.Configuration.TrfTestConfiguration.GetDataDir)
    - [M GetEditor ](#tts.core.report.parser.Configuration.TrfTestConfiguration.GetEditor)
    - [M GetId ](#tts.core.report.parser.Configuration.TrfTestConfiguration.GetId)
    - [M GetLibraryId ](#tts.core.report.parser.Configuration.TrfTestConfiguration.GetLibraryId)
    - [M GetMappingFile ](#tts.core.report.parser.Configuration.TrfTestConfiguration.GetMappingFile)
    - [M GetName ](#tts.core.report.parser.Configuration.TrfTestConfiguration.GetName)
    - [M GetPath ](#tts.core.report.parser.Configuration.TrfTestConfiguration.GetPath)
    - [M GetPkgDir ](#tts.core.report.parser.Configuration.TrfTestConfiguration.GetPkgDir)
    - [M GetTcfId ](#tts.core.report.parser.Configuration.TrfTestConfiguration.GetTcfId)
    - [M GetTeststand ](#tts.core.report.parser.Configuration.TrfTestConfiguration.GetTeststand)
    - [M HasBusConfigurations ](#tts.core.report.parser.Configuration.TrfTestConfiguration.HasBusConfigurations)
    - [M HasConstFiles ](#tts.core.report.parser.Configuration.TrfTestConfiguration.HasConstFiles)
    - [M HasEcuConfigurations ](#tts.core.report.parser.Configuration.TrfTestConfiguration.HasEcuConfigurations)
    - [M HasEfsConfigurations ](#tts.core.report.parser.Configuration.TrfTestConfiguration.HasEfsConfigurations)
    - [M HasFunctionConfigurations ](#tts.core.report.parser.Configuration.TrfTestConfiguration.HasFunctionConfigurations)
    - [M HasModelConfigurations ](#tts.core.report.parser.Configuration.TrfTestConfiguration.HasModelConfigurations)
    - [M IterBusConfigurations ](#tts.core.report.parser.Configuration.TrfTestConfiguration.IterBusConfigurations)
    - [M IterConstFiles ](#tts.core.report.parser.Configuration.TrfTestConfiguration.IterConstFiles)
    - [M IterEcuConfigurations ](#tts.core.report.parser.Configuration.TrfTestConfiguration.IterEcuConfigurations)
    - [M IterEfsConfigurations ](#tts.core.report.parser.Configuration.TrfTestConfiguration.IterEfsConfigurations)
    - [M IterFunctionConfigurations ](#tts.core.report.parser.Configuration.TrfTestConfiguration.IterFunctionConfigurations)
    - [M IterMappingFiles ](#tts.core.report.parser.Configuration.TrfTestConfiguration.IterMappingFiles)
    - [M IterModelConfigurations ](#tts.core.report.parser.Configuration.TrfTestConfiguration.IterModelConfigurations)
  - [C TcfBus ](#tts.core.report.db.TcfBus.TcfBus)
    - [M GetDbPath ](#tts.core.report.db.TcfBus.TcfBus.GetDbPath)
    - [M GetFbxChn ](#tts.core.report.db.TcfBus.TcfBus.GetFbxChn)
    - [M GetId ](#tts.core.report.db.TcfBus.TcfBus.GetId)
    - [M GetTcfBusId ](#tts.core.report.db.TcfBus.TcfBus.GetTcfBusId)
    - [M GetTcfId ](#tts.core.report.db.TcfBus.TcfBus.GetTcfId)
  - [C TcfEcu ](#tts.core.report.db.TcfEcu.TcfEcu)
    - [A PDiagHSFZSettings ](#tts.core.report.db.TcfEcu.TcfEcu.PDiagHSFZSettings)
    - [M GetA2lFile ](#tts.core.report.db.TcfEcu.TcfEcu.GetA2lFile)
    - [M GetDebugHex ](#tts.core.report.db.TcfEcu.TcfEcu.GetDebugHex)
    - [M GetDiagDoIpSettings ](#tts.core.report.db.TcfEcu.TcfEcu.GetDiagDoIpSettings)
    - [M GetDiagDoSoAdSettings ](#tts.core.report.db.TcfEcu.TcfEcu.GetDiagDoSoAdSettings)
    - [M GetDiagFrTpSettings ](#tts.core.report.db.TcfEcu.TcfEcu.GetDiagFrTpSettings)
    - [M GetDiagHSFZSettings ](#tts.core.report.db.TcfEcu.TcfEcu.GetDiagHSFZSettings)
    - [M GetDiagIsoTpSettings ](#tts.core.report.db.TcfEcu.TcfEcu.GetDiagIsoTpSettings)
    - [M GetDiagPort ](#tts.core.report.db.TcfEcu.TcfEcu.GetDiagPort)
    - [M GetDiagUDSSettings ](#tts.core.report.db.TcfEcu.TcfEcu.GetDiagUDSSettings)
    - [M GetDiagnosticDb ](#tts.core.report.db.TcfEcu.TcfEcu.GetDiagnosticDb)
    - [M GetElf ](#tts.core.report.db.TcfEcu.TcfEcu.GetElf)
    - [M GetElfs ](#tts.core.report.db.TcfEcu.TcfEcu.GetElfs)
    - [M GetHexFile ](#tts.core.report.db.TcfEcu.TcfEcu.GetHexFile)
    - [M GetId ](#tts.core.report.db.TcfEcu.TcfEcu.GetId)
    - [M GetLogDatabase ](#tts.core.report.db.TcfEcu.TcfEcu.GetLogDatabase)
    - [M GetLogFilterFile ](#tts.core.report.db.TcfEcu.TcfEcu.GetLogFilterFile)
    - [M GetLogilink ](#tts.core.report.db.TcfEcu.TcfEcu.GetLogilink)
    - [M GetSgbd ](#tts.core.report.db.TcfEcu.TcfEcu.GetSgbd)
    - [M GetSgbdVersion ](#tts.core.report.db.TcfEcu.TcfEcu.GetSgbdVersion)
    - [M GetTcfEcuId ](#tts.core.report.db.TcfEcu.TcfEcu.GetTcfEcuId)
    - [M GetTcfId ](#tts.core.report.db.TcfEcu.TcfEcu.GetTcfId)
  - [C TcfEfs ](#tts.core.report.db.TcfEfs.TcfEfs)
    - [M GetDb ](#tts.core.report.db.TcfEfs.TcfEfs.GetDb)
    - [M GetId ](#tts.core.report.db.TcfEfs.TcfEfs.GetId)
    - [M GetTcfEfsId ](#tts.core.report.db.TcfEfs.TcfEfs.GetTcfEfsId)
    - [M GetTcfId ](#tts.core.report.db.TcfEfs.TcfEfs.GetTcfId)
  - [C TcfExecution ](#tts.core.report.db.TcfExecution.TcfExecution)
    - [M GetSimulationMode ](#tts.core.report.db.TcfExecution.TcfExecution.GetSimulationMode)
    - [M GetTcfId ](#tts.core.report.db.TcfExecution.TcfExecution.GetTcfId)
    - [M GetWaitAfterTeststep ](#tts.core.report.db.TcfExecution.TcfExecution.GetWaitAfterTeststep)
  - [C TcfFct ](#tts.core.report.db.TcfFct.TcfFct)
    - [M GetCatalog ](#tts.core.report.db.TcfFct.TcfFct.GetCatalog)
    - [M GetId ](#tts.core.report.db.TcfFct.TcfFct.GetId)
    - [M GetTcfFctId ](#tts.core.report.db.TcfFct.TcfFct.GetTcfFctId)
    - [M GetTcfId ](#tts.core.report.db.TcfFct.TcfFct.GetTcfId)
  - [C TcfModel ](#tts.core.report.db.TcfModel.TcfModel)
    - [M GetId ](#tts.core.report.db.TcfModel.TcfModel.GetId)
    - [M GetModel ](#tts.core.report.db.TcfModel.TcfModel.GetModel)
    - [M GetTcfId ](#tts.core.report.db.TcfModel.TcfModel.GetTcfId)
    - [M GetTcfModelId ](#tts.core.report.db.TcfModel.TcfModel.GetTcfModelId)
    - [M GetTimebase ](#tts.core.report.db.TcfModel.TcfModel.GetTimebase)
    - [M GetVersion ](#tts.core.report.db.TcfModel.TcfModel.GetVersion)
  - [C TbcTool ](#tts.core.report.db.TbcTool.TbcTool)
    - [M GetLocation ](#tts.core.report.db.TbcTool.TbcTool.GetLocation)
    - [M GetName ](#tts.core.report.db.TbcTool.TbcTool.GetName)
    - [M GetPatches ](#tts.core.report.db.TbcTool.TbcTool.GetPatches)
    - [M GetStatus ](#tts.core.report.db.TbcTool.TbcTool.GetStatus)
    - [M GetTbcId ](#tts.core.report.db.TbcTool.TbcTool.GetTbcId)
    - [M GetTbcToolId ](#tts.core.report.db.TbcTool.TbcTool.GetTbcToolId)
    - [M GetVersion ](#tts.core.report.db.TbcTool.TbcTool.GetVersion)
- [ Constant ](#constant)
  - [C Constant ](#tts.core.report.db.Constant.Constant)
    - [M GetDescription ](#tts.core.report.db.Constant.Constant.GetDescription)
    - [M GetName ](#tts.core.report.db.Constant.Constant.GetName)
    - [M GetOrigin ](#tts.core.report.db.Constant.Constant.GetOrigin)
    - [M GetValue ](#tts.core.report.db.Constant.Constant.GetValue)
- [ Entities ](#entities)
  - [C Entity ](#tts.core.report.db.Entity.Entity)
    - [M GetEntityId ](#tts.core.report.db.Entity.Entity.GetEntityId)
    - [M GetId ](#tts.core.report.db.Entity.Entity.GetId)
    - [M GetName ](#tts.core.report.db.Entity.Entity.GetName)
    - [M GetReportItemId ](#tts.core.report.db.Entity.Entity.GetReportItemId)
    - [M GetType ](#tts.core.report.db.Entity.Entity.GetType)
  - [C ImageEntity ](#tts.core.report.db.ImageEntity.ImageEntity)
    - [M GetData ](#tts.core.report.db.ImageEntity.ImageEntity.GetData)
    - [M GetEntityId ](#tts.core.report.db.ImageEntity.ImageEntity.GetEntityId)
    - [M GetId ](#tts.core.report.db.ImageEntity.ImageEntity.GetId)
    - [M GetImage ](#tts.core.report.db.ImageEntity.ImageEntity.GetImage)
    - [M GetName ](#tts.core.report.db.ImageEntity.ImageEntity.GetName)
    - [M GetReportItemId ](#tts.core.report.db.ImageEntity.ImageEntity.GetReportItemId)
    - [M GetType ](#tts.core.report.db.ImageEntity.ImageEntity.GetType)
    - [M ToFile ](#tts.core.report.db.ImageEntity.ImageEntity.ToFile)
  - [C ImageExpectationEntity ](#tts.core.report.db.ImageExpectationEntity.ImageExpectationEntity)
    - [M GetActualImage ](#tts.core.report.db.ImageExpectationEntity.ImageExpectationEntity.GetActualImage)
    - [M GetEntityId ](#tts.core.report.db.ImageExpectationEntity.ImageExpectationEntity.GetEntityId)
    - [M GetExpectedImage ](#tts.core.report.db.ImageExpectationEntity.ImageExpectationEntity.GetExpectedImage)
    - [M GetId ](#tts.core.report.db.ImageExpectationEntity.ImageExpectationEntity.GetId)
    - [M GetName ](#tts.core.report.db.ImageExpectationEntity.ImageExpectationEntity.GetName)
    - [M GetReportItemId ](#tts.core.report.db.ImageExpectationEntity.ImageExpectationEntity.GetReportItemId)
    - [M GetType ](#tts.core.report.db.ImageExpectationEntity.ImageExpectationEntity.GetType)
  - [C RecordingInfosEntity ](#tts.core.report.parser.Package.RecordingInfosEntity)
    - [M GetCount ](#tts.core.report.parser.Package.RecordingInfosEntity.GetCount)
    - [M GetEntityId ](#tts.core.report.parser.Package.RecordingInfosEntity.GetEntityId)
    - [M GetId ](#tts.core.report.parser.Package.RecordingInfosEntity.GetId)
    - [M GetName ](#tts.core.report.parser.Package.RecordingInfosEntity.GetName)
    - [M GetRecording ](#tts.core.report.parser.Package.RecordingInfosEntity.GetRecording)
    - [M GetRecordingId ](#tts.core.report.parser.Package.RecordingInfosEntity.GetRecordingId)
    - [M GetReportItemId ](#tts.core.report.parser.Package.RecordingInfosEntity.GetReportItemId)
    - [M GetStartTime ](#tts.core.report.parser.Package.RecordingInfosEntity.GetStartTime)
    - [M GetStopTime ](#tts.core.report.parser.Package.RecordingInfosEntity.GetStopTime)
    - [M GetSyncDeltaT ](#tts.core.report.parser.Package.RecordingInfosEntity.GetSyncDeltaT)
    - [M GetType ](#tts.core.report.parser.Package.RecordingInfosEntity.GetType)
  - [C ProjectElementStatistic ](#tts.core.report.parser.ProjectElement.ProjectElementStatistic)
    - [M GetCountAndPercentageOfResultItem ](#tts.core.report.parser.ProjectElement.ProjectElementStatistic.GetCountAndPercentageOfResultItem)
    - [M GetCountOfResultItem ](#tts.core.report.parser.ProjectElement.ProjectElementStatistic.GetCountOfResultItem)
    - [M GetEntityId ](#tts.core.report.parser.ProjectElement.ProjectElementStatistic.GetEntityId)
    - [M GetErrorCount ](#tts.core.report.parser.ProjectElement.ProjectElementStatistic.GetErrorCount)
    - [M GetFailedCount ](#tts.core.report.parser.ProjectElement.ProjectElementStatistic.GetFailedCount)
    - [M GetHeader ](#tts.core.report.parser.ProjectElement.ProjectElementStatistic.GetHeader)
    - [M GetId ](#tts.core.report.parser.ProjectElement.ProjectElementStatistic.GetId)
    - [M GetInconCount ](#tts.core.report.parser.ProjectElement.ProjectElementStatistic.GetInconCount)
    - [M GetName ](#tts.core.report.parser.ProjectElement.ProjectElementStatistic.GetName)
    - [M GetNoneCount ](#tts.core.report.parser.ProjectElement.ProjectElementStatistic.GetNoneCount)
    - [M GetNumberCols ](#tts.core.report.parser.ProjectElement.ProjectElementStatistic.GetNumberCols)
    - [M GetNumberRows ](#tts.core.report.parser.ProjectElement.ProjectElementStatistic.GetNumberRows)
    - [M GetPercentageOfResultItem ](#tts.core.report.parser.ProjectElement.ProjectElementStatistic.GetPercentageOfResultItem)
    - [M GetReportItemId ](#tts.core.report.parser.ProjectElement.ProjectElementStatistic.GetReportItemId)
    - [M GetResult ](#tts.core.report.parser.ProjectElement.ProjectElementStatistic.GetResult)
    - [M GetResultCount ](#tts.core.report.parser.ProjectElement.ProjectElementStatistic.GetResultCount)
    - [M GetSuccessCount ](#tts.core.report.parser.ProjectElement.ProjectElementStatistic.GetSuccessCount)
    - [M GetTotalCount ](#tts.core.report.parser.ProjectElement.ProjectElementStatistic.GetTotalCount)
    - [M GetType ](#tts.core.report.parser.ProjectElement.ProjectElementStatistic.GetType)
    - [M GetValue ](#tts.core.report.parser.ProjectElement.ProjectElementStatistic.GetValue)
    - [M IterRowsWithResult ](#tts.core.report.parser.ProjectElement.ProjectElementStatistic.IterRowsWithResult)
  - [C TableEntity ](#tts.core.report.db.TableEntity.TableEntity)
    - [M GetCountAndPercentageOfResultItem ](#tts.core.report.db.TableEntity.TableEntity.GetCountAndPercentageOfResultItem)
    - [M GetCountOfResultItem ](#tts.core.report.db.TableEntity.TableEntity.GetCountOfResultItem)
    - [M GetEntityId ](#tts.core.report.db.TableEntity.TableEntity.GetEntityId)
    - [M GetHeader ](#tts.core.report.db.TableEntity.TableEntity.GetHeader)
    - [M GetId ](#tts.core.report.db.TableEntity.TableEntity.GetId)
    - [M GetName ](#tts.core.report.db.TableEntity.TableEntity.GetName)
    - [M GetNumberCols ](#tts.core.report.db.TableEntity.TableEntity.GetNumberCols)
    - [M GetNumberRows ](#tts.core.report.db.TableEntity.TableEntity.GetNumberRows)
    - [M GetPercentageOfResultItem ](#tts.core.report.db.TableEntity.TableEntity.GetPercentageOfResultItem)
    - [M GetReportItemId ](#tts.core.report.db.TableEntity.TableEntity.GetReportItemId)
    - [M GetResult ](#tts.core.report.db.TableEntity.TableEntity.GetResult)
    - [M GetType ](#tts.core.report.db.TableEntity.TableEntity.GetType)
    - [M GetValue ](#tts.core.report.db.TableEntity.TableEntity.GetValue)
    - [M IterRowsWithResult ](#tts.core.report.db.TableEntity.TableEntity.IterRowsWithResult)
  - [C TextEntity ](#tts.core.report.db.TextEntity.TextEntity)
    - [M GetEntityId ](#tts.core.report.db.TextEntity.TextEntity.GetEntityId)
    - [M GetId ](#tts.core.report.db.TextEntity.TextEntity.GetId)
    - [M GetName ](#tts.core.report.db.TextEntity.TextEntity.GetName)
    - [M GetReportItemId ](#tts.core.report.db.TextEntity.TextEntity.GetReportItemId)
    - [M GetType ](#tts.core.report.db.TextEntity.TextEntity.GetType)
    - [M GetValue ](#tts.core.report.db.TextEntity.TextEntity.GetValue)
  - [C TraceArtifactEntity ](#tts.core.report.parser.Package.TraceArtifactEntity)
    - [M GetComment ](#tts.core.report.parser.Package.TraceArtifactEntity.GetComment)
    - [M GetCount ](#tts.core.report.parser.Package.TraceArtifactEntity.GetCount)
    - [M GetEntityId ](#tts.core.report.parser.Package.TraceArtifactEntity.GetEntityId)
    - [M GetId ](#tts.core.report.parser.Package.TraceArtifactEntity.GetId)
    - [M GetName ](#tts.core.report.parser.Package.TraceArtifactEntity.GetName)
    - [M GetRecording ](#tts.core.report.parser.Package.TraceArtifactEntity.GetRecording)
    - [M GetRecordingId ](#tts.core.report.parser.Package.TraceArtifactEntity.GetRecordingId)
    - [M GetReportItemId ](#tts.core.report.parser.Package.TraceArtifactEntity.GetReportItemId)
    - [M GetSourceReportItem ](#tts.core.report.parser.Package.TraceArtifactEntity.GetSourceReportItem)
    - [M GetSourceReportItemId ](#tts.core.report.parser.Package.TraceArtifactEntity.GetSourceReportItemId)
    - [M GetType ](#tts.core.report.parser.Package.TraceArtifactEntity.GetType)
    - [M IterItems ](#tts.core.report.parser.Package.TraceArtifactEntity.IterItems)
- [ Image ](#image)
  - [C Image ](#tts.core.report.db.Image.Image)
    - [M GetBitmap ](#tts.core.report.db.Image.Image.GetBitmap)
    - [M GetDepth ](#tts.core.report.db.Image.Image.GetDepth)
    - [M GetHeight ](#tts.core.report.db.Image.Image.GetHeight)
    - [M GetId ](#tts.core.report.db.Image.Image.GetId)
    - [M GetMaskColor ](#tts.core.report.db.Image.Image.GetMaskColor)
    - [M GetName ](#tts.core.report.db.Image.Image.GetName)
    - [M GetSubTitle ](#tts.core.report.db.Image.Image.GetSubTitle)
    - [M GetTitle ](#tts.core.report.db.Image.Image.GetTitle)
    - [M GetWidth ](#tts.core.report.db.Image.Image.GetWidth)
- [ Info ](#info)
  - [C Info ](#tts.core.report.db.Info.Info)
    - [M GetAppName ](#tts.core.report.db.Info.Info.GetAppName)
    - [M GetAppVersion ](#tts.core.report.db.Info.Info.GetAppVersion)
    - [M GetAuthor ](#tts.core.report.db.Info.Info.GetAuthor)
    - [M GetDbVersion ](#tts.core.report.db.Info.Info.GetDbVersion)
    - [M GetDuration ](#tts.core.report.db.Info.Info.GetDuration)
    - [M GetExecutionMode ](#tts.core.report.db.Info.Info.GetExecutionMode)
    - [M GetExecutionTime ](#tts.core.report.db.Info.Info.GetExecutionTime)
    - [M GetId ](#tts.core.report.db.Info.Info.GetId)
    - [M GetInfoId ](#tts.core.report.db.Info.Info.GetInfoId)
    - [M GetKeywordCatalog ](#tts.core.report.db.Info.Info.GetKeywordCatalog)
    - [M GetProjectExecutionPath ](#tts.core.report.db.Info.Info.GetProjectExecutionPath)
    - [M GetResult ](#tts.core.report.db.Info.Info.GetResult)
    - [M GetSignature ](#tts.core.report.db.Info.Info.GetSignature)
    - [M GetTeststand ](#tts.core.report.db.Info.Info.GetTeststand)
    - [M GetTimeZoneUTCOffset ](#tts.core.report.db.Info.Info.GetTimeZoneUTCOffset)
    - [M GetTimeZoneUTCOffsetStr ](#tts.core.report.db.Info.Info.GetTimeZoneUTCOffsetStr)
    - [M GetUUID ](#tts.core.report.db.Info.Info.GetUUID)
- [ MappingItem ](#mappingitem)
  - [C MappingItem ](#tts.core.report.db.MappingItem.MappingItem)
    - [M GetDescription ](#tts.core.report.db.MappingItem.MappingItem.GetDescription)
    - [M GetId ](#tts.core.report.db.MappingItem.MappingItem.GetId)
    - [M GetMappingItemId ](#tts.core.report.db.MappingItem.MappingItem.GetMappingItemId)
    - [M GetName ](#tts.core.report.db.MappingItem.MappingItem.GetName)
    - [M GetOrigin ](#tts.core.report.db.MappingItem.MappingItem.GetOrigin)
    - [M GetParentId ](#tts.core.report.db.MappingItem.MappingItem.GetParentId)
    - [M GetTarget ](#tts.core.report.db.MappingItem.MappingItem.GetTarget)
    - [M GetType ](#tts.core.report.db.MappingItem.MappingItem.GetType)
    - [M GetUsedRaster ](#tts.core.report.db.MappingItem.MappingItem.GetUsedRaster)
    - [M GetWantedRaster ](#tts.core.report.db.MappingItem.MappingItem.GetWantedRaster)
    - [M IsForcedRaster ](#tts.core.report.db.MappingItem.MappingItem.IsForcedRaster)
    - [M IsGlobal ](#tts.core.report.db.MappingItem.MappingItem.IsGlobal)
- [ Package ](#module-tts.core.report.parser.Package)
  - [C AnalysisJobItem ](#tts.core.report.parser.Package.AnalysisJobItem)
    - [M GetMaxExecLevel ](#tts.core.report.parser.Package.AnalysisJobItem.GetMaxExecLevel)
    - [M GetOriginalResult ](#tts.core.report.parser.Package.AnalysisJobItem.GetOriginalResult)
    - [M GetResult ](#tts.core.report.parser.Package.AnalysisJobItem.GetResult)
    - [M GetStimulationPackage ](#tts.core.report.parser.Package.AnalysisJobItem.GetStimulationPackage)
    - [M GetTraceAnalysis ](#tts.core.report.parser.Package.AnalysisJobItem.GetTraceAnalysis)
    - [M HasData ](#tts.core.report.parser.Package.AnalysisJobItem.HasData)
    - [M HasParams ](#tts.core.report.parser.Package.AnalysisJobItem.HasParams)
    - [M HasReturnValues ](#tts.core.report.parser.Package.AnalysisJobItem.HasReturnValues)
    - [M IterParameterVariables ](#tts.core.report.parser.Package.AnalysisJobItem.IterParameterVariables)
    - [M IterReturnVariables ](#tts.core.report.parser.Package.AnalysisJobItem.IterReturnVariables)
    - [M IterTraceItems ](#tts.core.report.parser.Package.AnalysisJobItem.IterTraceItems)
    - [M IterUserComments ](#tts.core.report.parser.Package.AnalysisJobItem.IterUserComments)
  - [C Mapping ](#tts.core.report.parser.Package.Mapping)
    - [M GetDescription ](#tts.core.report.parser.Package.Mapping.GetDescription)
    - [M GetId ](#tts.core.report.parser.Package.Mapping.GetId)
    - [M GetMappingItemId ](#tts.core.report.parser.Package.Mapping.GetMappingItemId)
    - [M GetName ](#tts.core.report.parser.Package.Mapping.GetName)
    - [M GetOrigin ](#tts.core.report.parser.Package.Mapping.GetOrigin)
    - [M GetParentId ](#tts.core.report.parser.Package.Mapping.GetParentId)
    - [M GetTarget ](#tts.core.report.parser.Package.Mapping.GetTarget)
    - [M GetType ](#tts.core.report.parser.Package.Mapping.GetType)
    - [M GetUsedRaster ](#tts.core.report.parser.Package.Mapping.GetUsedRaster)
    - [M GetWantedRaster ](#tts.core.report.parser.Package.Mapping.GetWantedRaster)
    - [M HasSubMappings ](#tts.core.report.parser.Package.Mapping.HasSubMappings)
    - [M IsForcedRaster ](#tts.core.report.parser.Package.Mapping.IsForcedRaster)
    - [M IsGlobal ](#tts.core.report.parser.Package.Mapping.IsGlobal)
    - [M IterSubMappings ](#tts.core.report.parser.Package.Mapping.IterSubMappings)
  - [C Mappings ](#tts.core.report.parser.Package.Mappings)
    - [M IterMappings ](#tts.core.report.parser.Package.Mappings.IterMappings)
  - [C Package ](#tts.core.report.parser.Package.Package)
    - [M GetAbortCode ](#tts.core.report.parser.Package.Package.GetAbortCode)
    - [M GetAbortComment ](#tts.core.report.parser.Package.Package.GetAbortComment)
    - [M GetAdditionalInfo ](#tts.core.report.parser.Package.Package.GetAdditionalInfo)
    - [M GetArtifacts ](#tts.core.report.parser.Package.Package.GetArtifacts)
    - [M GetCallError ](#tts.core.report.parser.Package.Package.GetCallError)
    - [M GetComment ](#tts.core.report.parser.Package.Package.GetComment)
    - [M GetDescription ](#tts.core.report.parser.Package.Package.GetDescription)
    - [M GetDuration ](#tts.core.report.parser.Package.Package.GetDuration)
    - [M GetElementName ](#tts.core.report.parser.Package.Package.GetElementName)
    - [M GetGlobalConstantsDefinedOnStart ](#tts.core.report.parser.Package.Package.GetGlobalConstantsDefinedOnStart)
    - [M GetHash ](#tts.core.report.parser.Package.Package.GetHash)
    - [M GetId ](#tts.core.report.parser.Package.Package.GetId)
    - [M GetIsTestcase ](#tts.core.report.parser.Package.Package.GetIsTestcase)
    - [M GetLibraryId ](#tts.core.report.parser.Package.Package.GetLibraryId)
    - [M GetLinkedTestManagementIds ](#tts.core.report.parser.Package.Package.GetLinkedTestManagementIds)
    - [M GetMappings ](#tts.core.report.parser.Package.Package.GetMappings)
    - [M GetName ](#tts.core.report.parser.Package.Package.GetName)
    - [M GetOriginalResult ](#tts.core.report.parser.Package.Package.GetOriginalResult)
    - [M GetParameterDescription ](#tts.core.report.parser.Package.Package.GetParameterDescription)
    - [M GetParameterInitialValue ](#tts.core.report.parser.Package.Package.GetParameterInitialValue)
    - [M GetParameterNames ](#tts.core.report.parser.Package.Package.GetParameterNames)
    - [M GetParameterOrigin ](#tts.core.report.parser.Package.Package.GetParameterOrigin)
    - [M GetParameterValue ](#tts.core.report.parser.Package.Package.GetParameterValue)
    - [M GetPath ](#tts.core.report.parser.Package.Package.GetPath)
    - [M GetPkgId ](#tts.core.report.parser.Package.Package.GetPkgId)
    - [M GetRecordings ](#tts.core.report.parser.Package.Package.GetRecordings)
    - [M GetReportItemId ](#tts.core.report.parser.Package.Package.GetReportItemId)
    - [M GetResult ](#tts.core.report.parser.Package.Package.GetResult)
    - [M GetReturnDescription ](#tts.core.report.parser.Package.Package.GetReturnDescription)
    - [M GetReturnInitialValue ](#tts.core.report.parser.Package.Package.GetReturnInitialValue)
    - [M GetReturnNames ](#tts.core.report.parser.Package.Package.GetReturnNames)
    - [M GetReturnValue ](#tts.core.report.parser.Package.Package.GetReturnValue)
    - [M GetRevalComments ](#tts.core.report.parser.Package.Package.GetRevalComments)
    - [M GetRevalCommentsString ](#tts.core.report.parser.Package.Package.GetRevalCommentsString)
    - [M GetRevision ](#tts.core.report.parser.Package.Package.GetRevision)
    - [M GetSCMBranch ](#tts.core.report.parser.Package.Package.GetSCMBranch)
    - [M GetSCMStatus ](#tts.core.report.parser.Package.Package.GetSCMStatus)
    - [M GetSCMUrl ](#tts.core.report.parser.Package.Package.GetSCMUrl)
    - [M GetStimulationPackage ](#tts.core.report.parser.Package.Package.GetStimulationPackage)
    - [M GetSubReportPath ](#tts.core.report.parser.Package.Package.GetSubReportPath)
    - [M GetTestCase ](#tts.core.report.parser.Package.Package.GetTestCase)
    - [M GetTestScriptId ](#tts.core.report.parser.Package.Package.GetTestScriptId)
    - [M GetTestmanagementId ](#tts.core.report.parser.Package.Package.GetTestmanagementId)
    - [M GetTime ](#tts.core.report.parser.Package.Package.GetTime)
    - [M GetTraceAnalyses ](#tts.core.report.parser.Package.Package.GetTraceAnalyses)
    - [M GetUserReportData ](#tts.core.report.parser.Package.Package.GetUserReportData)
    - [M GetVersion ](#tts.core.report.parser.Package.Package.GetVersion)
    - [M HasAnalysisJobs ](#tts.core.report.parser.Package.Package.HasAnalysisJobs)
    - [M HasAttributes ](#tts.core.report.parser.Package.Package.HasAttributes)
    - [M HasMappings ](#tts.core.report.parser.Package.Package.HasMappings)
    - [M HasParams ](#tts.core.report.parser.Package.Package.HasParams)
    - [M HasRecordings ](#tts.core.report.parser.Package.Package.HasRecordings)
    - [M HasReturnValues ](#tts.core.report.parser.Package.Package.HasReturnValues)
    - [M HasRevalComments ](#tts.core.report.parser.Package.Package.HasRevalComments)
    - [M HasTestCase ](#tts.core.report.parser.Package.Package.HasTestCase)
    - [M HasTraceAnalyses ](#tts.core.report.parser.Package.Package.HasTraceAnalyses)
    - [M IsAnalysisPackage ](#tts.core.report.parser.Package.Package.IsAnalysisPackage)
    - [M IsSkipped ](#tts.core.report.parser.Package.Package.IsSkipped)
    - [M IsStimulationPackage ](#tts.core.report.parser.Package.Package.IsStimulationPackage)
    - [M IterAnalysisJobs ](#tts.core.report.parser.Package.Package.IterAnalysisJobs)
    - [M IterAttributes ](#tts.core.report.parser.Package.Package.IterAttributes)
    - [M IterParameterVariables ](#tts.core.report.parser.Package.Package.IterParameterVariables)
    - [M IterReturnVariables ](#tts.core.report.parser.Package.Package.IterReturnVariables)
    - [M IterReturnVariablesAfterTest ](#tts.core.report.parser.Package.Package.IterReturnVariablesAfterTest)
    - [M IterUserComments ](#tts.core.report.parser.Package.Package.IterUserComments)
    - [M GetComponentName ](#tts.core.report.parser.Package.Package.GetComponentName)
  - [C ParallelPackage ](#tts.core.report.parser.Package.ParallelPackage)
    - [M GetAbortCode ](#tts.core.report.parser.Package.ParallelPackage.GetAbortCode)
    - [M GetAbortComment ](#tts.core.report.parser.Package.ParallelPackage.GetAbortComment)
    - [M GetAdditionalInfo ](#tts.core.report.parser.Package.ParallelPackage.GetAdditionalInfo)
    - [M GetCallError ](#tts.core.report.parser.Package.ParallelPackage.GetCallError)
    - [M GetComment ](#tts.core.report.parser.Package.ParallelPackage.GetComment)
    - [M GetDescription ](#tts.core.report.parser.Package.ParallelPackage.GetDescription)
    - [M GetDuration ](#tts.core.report.parser.Package.ParallelPackage.GetDuration)
    - [M GetElementName ](#tts.core.report.parser.Package.ParallelPackage.GetElementName)
    - [M GetGlobalConstantsDefinedOnStart ](#tts.core.report.parser.Package.ParallelPackage.GetGlobalConstantsDefinedOnStart)
    - [M GetHash ](#tts.core.report.parser.Package.ParallelPackage.GetHash)
    - [M GetId ](#tts.core.report.parser.Package.ParallelPackage.GetId)
    - [M GetIsTestcase ](#tts.core.report.parser.Package.ParallelPackage.GetIsTestcase)
    - [M GetLibraryId ](#tts.core.report.parser.Package.ParallelPackage.GetLibraryId)
    - [M GetLinkedTestManagementIds ](#tts.core.report.parser.Package.ParallelPackage.GetLinkedTestManagementIds)
    - [M GetMappings ](#tts.core.report.parser.Package.ParallelPackage.GetMappings)
    - [M GetName ](#tts.core.report.parser.Package.ParallelPackage.GetName)
    - [M GetOriginalResult ](#tts.core.report.parser.Package.ParallelPackage.GetOriginalResult)
    - [M GetParameterDescription ](#tts.core.report.parser.Package.ParallelPackage.GetParameterDescription)
    - [M GetParameterInitialValue ](#tts.core.report.parser.Package.ParallelPackage.GetParameterInitialValue)
    - [M GetParameterNames ](#tts.core.report.parser.Package.ParallelPackage.GetParameterNames)
    - [M GetParameterOrigin ](#tts.core.report.parser.Package.ParallelPackage.GetParameterOrigin)
    - [M GetParameterValue ](#tts.core.report.parser.Package.ParallelPackage.GetParameterValue)
    - [M GetPath ](#tts.core.report.parser.Package.ParallelPackage.GetPath)
    - [M GetPkgId ](#tts.core.report.parser.Package.ParallelPackage.GetPkgId)
    - [M GetRecordings ](#tts.core.report.parser.Package.ParallelPackage.GetRecordings)
    - [M GetReportItemId ](#tts.core.report.parser.Package.ParallelPackage.GetReportItemId)
    - [M GetResult ](#tts.core.report.parser.Package.ParallelPackage.GetResult)
    - [M GetReturnDescription ](#tts.core.report.parser.Package.ParallelPackage.GetReturnDescription)
    - [M GetReturnInitialValue ](#tts.core.report.parser.Package.ParallelPackage.GetReturnInitialValue)
    - [M GetReturnNames ](#tts.core.report.parser.Package.ParallelPackage.GetReturnNames)
    - [M GetReturnValue ](#tts.core.report.parser.Package.ParallelPackage.GetReturnValue)
    - [M GetRevalComments ](#tts.core.report.parser.Package.ParallelPackage.GetRevalComments)
    - [M GetRevalCommentsString ](#tts.core.report.parser.Package.ParallelPackage.GetRevalCommentsString)
    - [M GetRevision ](#tts.core.report.parser.Package.ParallelPackage.GetRevision)
    - [M GetSCMBranch ](#tts.core.report.parser.Package.ParallelPackage.GetSCMBranch)
    - [M GetSCMStatus ](#tts.core.report.parser.Package.ParallelPackage.GetSCMStatus)
    - [M GetSCMUrl ](#tts.core.report.parser.Package.ParallelPackage.GetSCMUrl)
    - [M GetStimulationPackage ](#tts.core.report.parser.Package.ParallelPackage.GetStimulationPackage)
    - [M GetTestCase ](#tts.core.report.parser.Package.ParallelPackage.GetTestCase)
    - [M GetTestScriptId ](#tts.core.report.parser.Package.ParallelPackage.GetTestScriptId)
    - [M GetTestmanagementId ](#tts.core.report.parser.Package.ParallelPackage.GetTestmanagementId)
    - [M GetTime ](#tts.core.report.parser.Package.ParallelPackage.GetTime)
    - [M GetTraceAnalyses ](#tts.core.report.parser.Package.ParallelPackage.GetTraceAnalyses)
    - [M GetUserReportData ](#tts.core.report.parser.Package.ParallelPackage.GetUserReportData)
    - [M GetVersion ](#tts.core.report.parser.Package.ParallelPackage.GetVersion)
    - [M HasAnalysisJobs ](#tts.core.report.parser.Package.ParallelPackage.HasAnalysisJobs)
    - [M HasAttributes ](#tts.core.report.parser.Package.ParallelPackage.HasAttributes)
    - [M HasMappings ](#tts.core.report.parser.Package.ParallelPackage.HasMappings)
    - [M HasParams ](#tts.core.report.parser.Package.ParallelPackage.HasParams)
    - [M HasRecordings ](#tts.core.report.parser.Package.ParallelPackage.HasRecordings)
    - [M HasReturnValues ](#tts.core.report.parser.Package.ParallelPackage.HasReturnValues)
    - [M HasRevalComments ](#tts.core.report.parser.Package.ParallelPackage.HasRevalComments)
    - [M HasTestCase ](#tts.core.report.parser.Package.ParallelPackage.HasTestCase)
    - [M HasTraceAnalyses ](#tts.core.report.parser.Package.ParallelPackage.HasTraceAnalyses)
    - [M IsAnalysisPackage ](#tts.core.report.parser.Package.ParallelPackage.IsAnalysisPackage)
    - [M IsSkipped ](#tts.core.report.parser.Package.ParallelPackage.IsSkipped)
    - [M IsStimulationPackage ](#tts.core.report.parser.Package.ParallelPackage.IsStimulationPackage)
    - [M IterAnalysisJobs ](#tts.core.report.parser.Package.ParallelPackage.IterAnalysisJobs)
    - [M IterAttributes ](#tts.core.report.parser.Package.ParallelPackage.IterAttributes)
    - [M IterParameterVariables ](#tts.core.report.parser.Package.ParallelPackage.IterParameterVariables)
    - [M IterReturnVariables ](#tts.core.report.parser.Package.ParallelPackage.IterReturnVariables)
    - [M IterReturnVariablesAfterTest ](#tts.core.report.parser.Package.ParallelPackage.IterReturnVariablesAfterTest)
    - [M IterUserComments ](#tts.core.report.parser.Package.ParallelPackage.IterUserComments)
    - [M GetComponentName ](#tts.core.report.parser.Package.ParallelPackage.GetComponentName)
  - [C Recording ](#tts.core.report.parser.Package.Recording)
    - [M GetMeasurementListFile ](#tts.core.report.parser.Package.Recording.GetMeasurementListFile)
    - [M GetNumberOfMeasurementListFileSignals ](#tts.core.report.parser.Package.Recording.GetNumberOfMeasurementListFileSignals)
    - [M GetOrigin ](#tts.core.report.parser.Package.Recording.GetOrigin)
    - [M GetSignalGroupName ](#tts.core.report.parser.Package.Recording.GetSignalGroupName)
    - [M GetSource ](#tts.core.report.parser.Package.Recording.GetSource)
    - [M GetSyncDeltaT ](#tts.core.report.parser.Package.Recording.GetSyncDeltaT)
    - [M IterMappings ](#tts.core.report.parser.Package.Recording.IterMappings)
    - [M IterSignals ](#tts.core.report.parser.Package.Recording.IterSignals)
  - [C Recordings ](#tts.core.report.parser.Package.Recordings)
    - [M IterRecordings ](#tts.core.report.parser.Package.Recordings.IterRecordings)
  - [C ReportItem ](#tts.core.report.parser.Package.ReportItem)
    - [A PPackageReportName ](#tts.core.report.parser.Package.ReportItem.PPackageReportName)
    - [M GetAbortCode ](#tts.core.report.parser.Package.ReportItem.GetAbortCode)
    - [M GetAbortComment ](#tts.core.report.parser.Package.ReportItem.GetAbortComment)
    - [M GetAbsoluteTimestamp ](#tts.core.report.parser.Package.ReportItem.GetAbsoluteTimestamp)
    - [M GetAdditionalInfo ](#tts.core.report.parser.Package.ReportItem.GetAdditionalInfo)
    - [M GetComment ](#tts.core.report.parser.Package.ReportItem.GetComment)
    - [M GetDuration ](#tts.core.report.parser.Package.ReportItem.GetDuration)
    - [M GetElementaryResult ](#tts.core.report.parser.Package.ReportItem.GetElementaryResult)
    - [M GetExecLevel ](#tts.core.report.parser.Package.ReportItem.GetExecLevel)
    - [M GetId ](#tts.core.report.parser.Package.ReportItem.GetId)
    - [M GetImageKey ](#tts.core.report.parser.Package.ReportItem.GetImageKey)
    - [M GetInfo ](#tts.core.report.parser.Package.ReportItem.GetInfo)
    - [M GetLabel ](#tts.core.report.parser.Package.ReportItem.GetLabel)
    - [M GetLinkedTestManagementIds ](#tts.core.report.parser.Package.ReportItem.GetLinkedTestManagementIds)
    - [M GetLoopCycle ](#tts.core.report.parser.Package.ReportItem.GetLoopCycle)
    - [M GetMappingTargets ](#tts.core.report.parser.Package.ReportItem.GetMappingTargets)
    - [M GetName ](#tts.core.report.parser.Package.ReportItem.GetName)
    - [M GetOriginalResult ](#tts.core.report.parser.Package.ReportItem.GetOriginalResult)
    - [M GetPackageInfo ](#tts.core.report.parser.Package.ReportItem.GetPackageInfo)
    - [M GetPackageReportName ](#tts.core.report.parser.Package.ReportItem.GetPackageReportName)
    - [M GetPackageScmInfo ](#tts.core.report.parser.Package.ReportItem.GetPackageScmInfo)
    - [M GetParentId ](#tts.core.report.parser.Package.ReportItem.GetParentId)
    - [M GetPos ](#tts.core.report.parser.Package.ReportItem.GetPos)
    - [M GetRelativeRealtime ](#tts.core.report.parser.Package.ReportItem.GetRelativeRealtime)
    - [M GetRelativeTimestamp ](#tts.core.report.parser.Package.ReportItem.GetRelativeTimestamp)
    - [M GetReportItemId ](#tts.core.report.parser.Package.ReportItem.GetReportItemId)
    - [M GetResult ](#tts.core.report.parser.Package.ReportItem.GetResult)
    - [M GetRevalComments ](#tts.core.report.parser.Package.ReportItem.GetRevalComments)
    - [M GetRevalCommentsString ](#tts.core.report.parser.Package.ReportItem.GetRevalCommentsString)
    - [M GetSrc ](#tts.core.report.parser.Package.ReportItem.GetSrc)
    - [M GetSrcCategory ](#tts.core.report.parser.Package.ReportItem.GetSrcCategory)
    - [M GetSrcIndex ](#tts.core.report.parser.Package.ReportItem.GetSrcIndex)
    - [M GetSrcSubType ](#tts.core.report.parser.Package.ReportItem.GetSrcSubType)
    - [M GetSrcType ](#tts.core.report.parser.Package.ReportItem.GetSrcType)
    - [M GetTargetValue ](#tts.core.report.parser.Package.ReportItem.GetTargetValue)
    - [M GetUndocumentedChild ](#tts.core.report.parser.Package.ReportItem.GetUndocumentedChild)
    - [M HasEntities ](#tts.core.report.parser.Package.ReportItem.HasEntities)
    - [M HasRevalComments ](#tts.core.report.parser.Package.ReportItem.HasRevalComments)
    - [M HasTag ](#tts.core.report.parser.Package.ReportItem.HasTag)
    - [M InitFromParentId ](#tts.core.report.parser.Package.ReportItem.InitFromParentId)
    - [M InitFromParentItem ](#tts.core.report.parser.Package.ReportItem.InitFromParentItem)
    - [M IsSkipped ](#tts.core.report.parser.Package.ReportItem.IsSkipped)
    - [M IterEntities ](#tts.core.report.parser.Package.ReportItem.IterEntities)
    - [M IterTags ](#tts.core.report.parser.Package.ReportItem.IterTags)
    - [M IterUserComments ](#tts.core.report.parser.Package.ReportItem.IterUserComments)
    - [M SetPackageReportName ](#tts.core.report.parser.Package.ReportItem.SetPackageReportName)
    - [M GetActivity ](#tts.core.report.parser.Package.ReportItem.GetActivity)
  - [C TestCase ](#tts.core.report.parser.Package.TestCase)
    - [M GetMaxExecLevel ](#tts.core.report.parser.Package.TestCase.GetMaxExecLevel)
    - [M GetResult ](#tts.core.report.parser.Package.TestCase.GetResult)
    - [M HasData ](#tts.core.report.parser.Package.TestCase.HasData)
    - [M IterTestSteps ](#tts.core.report.parser.Package.TestCase.IterTestSteps)
  - [C TraceAnalyses ](#tts.core.report.parser.Package.TraceAnalyses)
    - [M GetMaxExecLevel ](#tts.core.report.parser.Package.TraceAnalyses.GetMaxExecLevel)
    - [M HasData ](#tts.core.report.parser.Package.TraceAnalyses.HasData)
    - [M IterTraceItems ](#tts.core.report.parser.Package.TraceAnalyses.IterTraceItems)
- [ ProjectElements ](#module-tts.core.report.parser.ProjectElement)
  - [C ConfigChange ](#tts.core.report.parser.ProjectElement.ConfigChange)
    - [M GetAdditionalInfo ](#tts.core.report.parser.ProjectElement.ConfigChange.GetAdditionalInfo)
    - [M GetComment ](#tts.core.report.parser.ProjectElement.ConfigChange.GetComment)
    - [M GetDuration ](#tts.core.report.parser.ProjectElement.ConfigChange.GetDuration)
    - [M GetElementName ](#tts.core.report.parser.ProjectElement.ConfigChange.GetElementName)
    - [M GetName ](#tts.core.report.parser.ProjectElement.ConfigChange.GetName)
    - [M GetOriginalResult ](#tts.core.report.parser.ProjectElement.ConfigChange.GetOriginalResult)
    - [M GetReportItemId ](#tts.core.report.parser.ProjectElement.ConfigChange.GetReportItemId)
    - [M GetResult ](#tts.core.report.parser.ProjectElement.ConfigChange.GetResult)
    - [M GetSrcType ](#tts.core.report.parser.ProjectElement.ConfigChange.GetSrcType)
    - [M GetStatistic ](#tts.core.report.parser.ProjectElement.ConfigChange.GetStatistic)
    - [M GetTestBenchConfiguration ](#tts.core.report.parser.ProjectElement.ConfigChange.GetTestBenchConfiguration)
    - [M GetTestConfiguration ](#tts.core.report.parser.ProjectElement.ConfigChange.GetTestConfiguration)
    - [M GetTime ](#tts.core.report.parser.ProjectElement.ConfigChange.GetTime)
    - [M HasTestBenchConfiguration ](#tts.core.report.parser.ProjectElement.ConfigChange.HasTestBenchConfiguration)
    - [M HasTestConfiguration ](#tts.core.report.parser.ProjectElement.ConfigChange.HasTestConfiguration)
    - [M IsSkipped ](#tts.core.report.parser.ProjectElement.ConfigChange.IsSkipped)
    - [M IterItems ](#tts.core.report.parser.ProjectElement.ConfigChange.IterItems)
    - [M IterUserComments ](#tts.core.report.parser.ProjectElement.ConfigChange.IterUserComments)
  - [C Project ](#tts.core.report.parser.ProjectElement.Project)
    - [A PLibraryId ](#tts.core.report.parser.ProjectElement.Project.PLibraryId)
    - [M GetAdditionalInfo ](#tts.core.report.parser.ProjectElement.Project.GetAdditionalInfo)
    - [M GetComment ](#tts.core.report.parser.ProjectElement.Project.GetComment)
    - [M GetDuration ](#tts.core.report.parser.ProjectElement.Project.GetDuration)
    - [M GetElementName ](#tts.core.report.parser.ProjectElement.Project.GetElementName)
    - [M GetLibraryId ](#tts.core.report.parser.ProjectElement.Project.GetLibraryId)
    - [M GetName ](#tts.core.report.parser.ProjectElement.Project.GetName)
    - [M GetOriginalResult ](#tts.core.report.parser.ProjectElement.Project.GetOriginalResult)
    - [M GetPrjCompName ](#tts.core.report.parser.ProjectElement.Project.GetPrjCompName)
    - [M GetPrjId ](#tts.core.report.parser.ProjectElement.Project.GetPrjId)
    - [M GetReportItemId ](#tts.core.report.parser.ProjectElement.Project.GetReportItemId)
    - [M GetResult ](#tts.core.report.parser.ProjectElement.Project.GetResult)
    - [M GetSrcType ](#tts.core.report.parser.ProjectElement.Project.GetSrcType)
    - [M GetStatistic ](#tts.core.report.parser.ProjectElement.Project.GetStatistic)
    - [M GetTestManagementId ](#tts.core.report.parser.ProjectElement.Project.GetTestManagementId)
    - [M GetTime ](#tts.core.report.parser.ProjectElement.Project.GetTime)
    - [M HasAttributes ](#tts.core.report.parser.ProjectElement.Project.HasAttributes)
    - [M IsSkipped ](#tts.core.report.parser.ProjectElement.Project.IsSkipped)
    - [M IterAttributes ](#tts.core.report.parser.ProjectElement.Project.IterAttributes)
    - [M IterItems ](#tts.core.report.parser.ProjectElement.Project.IterItems)
    - [M IterUserComments ](#tts.core.report.parser.ProjectElement.Project.IterUserComments)
  - [C ProjectElement ](#tts.core.report.parser.ProjectElement.ProjectElement)
    - [M GetAdditionalInfo ](#tts.core.report.parser.ProjectElement.ProjectElement.GetAdditionalInfo)
    - [M GetComment ](#tts.core.report.parser.ProjectElement.ProjectElement.GetComment)
    - [M GetDuration ](#tts.core.report.parser.ProjectElement.ProjectElement.GetDuration)
    - [M GetElementName ](#tts.core.report.parser.ProjectElement.ProjectElement.GetElementName)
    - [M GetName ](#tts.core.report.parser.ProjectElement.ProjectElement.GetName)
    - [M GetOriginalResult ](#tts.core.report.parser.ProjectElement.ProjectElement.GetOriginalResult)
    - [M GetReportItemId ](#tts.core.report.parser.ProjectElement.ProjectElement.GetReportItemId)
    - [M GetResult ](#tts.core.report.parser.ProjectElement.ProjectElement.GetResult)
    - [M GetSrcType ](#tts.core.report.parser.ProjectElement.ProjectElement.GetSrcType)
    - [M GetStatistic ](#tts.core.report.parser.ProjectElement.ProjectElement.GetStatistic)
    - [M GetTime ](#tts.core.report.parser.ProjectElement.ProjectElement.GetTime)
    - [M IsSkipped ](#tts.core.report.parser.ProjectElement.ProjectElement.IsSkipped)
    - [M IterItems ](#tts.core.report.parser.ProjectElement.ProjectElement.IterItems)
    - [M IterUserComments ](#tts.core.report.parser.ProjectElement.ProjectElement.IterUserComments)
- [ ReportItems ](#reportitems)
  - [C ReportItem ](#tts.core.report.db.ReportItem.ReportItem)
    - [M GetAbortCode ](#tts.core.report.db.ReportItem.ReportItem.GetAbortCode)
    - [M GetAbortComment ](#tts.core.report.db.ReportItem.ReportItem.GetAbortComment)
    - [M GetAbsoluteTimestamp ](#tts.core.report.db.ReportItem.ReportItem.GetAbsoluteTimestamp)
    - [M GetAdditionalInfo ](#tts.core.report.db.ReportItem.ReportItem.GetAdditionalInfo)
    - [M GetComment ](#tts.core.report.db.ReportItem.ReportItem.GetComment)
    - [M GetDuration ](#tts.core.report.db.ReportItem.ReportItem.GetDuration)
    - [M GetElementaryResult ](#tts.core.report.db.ReportItem.ReportItem.GetElementaryResult)
    - [M GetExecLevel ](#tts.core.report.db.ReportItem.ReportItem.GetExecLevel)
    - [M GetId ](#tts.core.report.db.ReportItem.ReportItem.GetId)
    - [M GetImageKey ](#tts.core.report.db.ReportItem.ReportItem.GetImageKey)
    - [M GetInfo ](#tts.core.report.db.ReportItem.ReportItem.GetInfo)
    - [M GetLabel ](#tts.core.report.db.ReportItem.ReportItem.GetLabel)
    - [M GetLinkedTestManagementIds ](#tts.core.report.db.ReportItem.ReportItem.GetLinkedTestManagementIds)
    - [M GetLoopCycle ](#tts.core.report.db.ReportItem.ReportItem.GetLoopCycle)
    - [M GetName ](#tts.core.report.db.ReportItem.ReportItem.GetName)
    - [M GetOriginalResult ](#tts.core.report.db.ReportItem.ReportItem.GetOriginalResult)
    - [M GetParentId ](#tts.core.report.db.ReportItem.ReportItem.GetParentId)
    - [M GetPos ](#tts.core.report.db.ReportItem.ReportItem.GetPos)
    - [M GetRelativeRealtime ](#tts.core.report.db.ReportItem.ReportItem.GetRelativeRealtime)
    - [M GetRelativeTimestamp ](#tts.core.report.db.ReportItem.ReportItem.GetRelativeTimestamp)
    - [M GetReportItemId ](#tts.core.report.db.ReportItem.ReportItem.GetReportItemId)
    - [M GetResult ](#tts.core.report.db.ReportItem.ReportItem.GetResult)
    - [M GetRevalComments ](#tts.core.report.db.ReportItem.ReportItem.GetRevalComments)
    - [M GetRevalCommentsString ](#tts.core.report.db.ReportItem.ReportItem.GetRevalCommentsString)
    - [M GetSrc ](#tts.core.report.db.ReportItem.ReportItem.GetSrc)
    - [M GetSrcCategory ](#tts.core.report.db.ReportItem.ReportItem.GetSrcCategory)
    - [M GetSrcIndex ](#tts.core.report.db.ReportItem.ReportItem.GetSrcIndex)
    - [M GetSrcSubType ](#tts.core.report.db.ReportItem.ReportItem.GetSrcSubType)
    - [M GetSrcType ](#tts.core.report.db.ReportItem.ReportItem.GetSrcType)
    - [M GetTargetValue ](#tts.core.report.db.ReportItem.ReportItem.GetTargetValue)
    - [M GetUndocumentedChild ](#tts.core.report.db.ReportItem.ReportItem.GetUndocumentedChild)
    - [M HasRevalComments ](#tts.core.report.db.ReportItem.ReportItem.HasRevalComments)
    - [M InitFromParentId ](#tts.core.report.db.ReportItem.ReportItem.InitFromParentId)
    - [M InitFromParentItem ](#tts.core.report.db.ReportItem.ReportItem.InitFromParentItem)
    - [M IsSkipped ](#tts.core.report.db.ReportItem.ReportItem.IsSkipped)
    - [M GetActivity ](#tts.core.report.db.ReportItem.ReportItem.GetActivity)
  - [C ReportItemAnalysisInfo ](#tts.core.report.db.ReportItemAnalysisInfo.ReportItemAnalysisInfo)
    - [M GetImplementedAnalysisLabel ](#tts.core.report.db.ReportItemAnalysisInfo.ReportItemAnalysisInfo.GetImplementedAnalysisLabel)
    - [M GetReportItemId ](#tts.core.report.db.ReportItemAnalysisInfo.ReportItemAnalysisInfo.GetReportItemId)
    - [M GetStimParamReportItemId ](#tts.core.report.db.ReportItemAnalysisInfo.ReportItemAnalysisInfo.GetStimParamReportItemId)
    - [M GetStimReportItemId ](#tts.core.report.db.ReportItemAnalysisInfo.ReportItemAnalysisInfo.GetStimReportItemId)
    - [M IsRequested ](#tts.core.report.db.ReportItemAnalysisInfo.ReportItemAnalysisInfo.IsRequested)
  - [C ReportItemComment ](#tts.core.report.db.ReportItemComment.ReportItemComment)
    - [M GetAuthor ](#tts.core.report.db.ReportItemComment.ReportItemComment.GetAuthor)
    - [M GetId ](#tts.core.report.db.ReportItemComment.ReportItemComment.GetId)
    - [M GetOverriddenResult ](#tts.core.report.db.ReportItemComment.ReportItemComment.GetOverriddenResult)
    - [M GetReportItemId ](#tts.core.report.db.ReportItemComment.ReportItemComment.GetReportItemId)
    - [M GetText ](#tts.core.report.db.ReportItemComment.ReportItemComment.GetText)
    - [M GetTimestamp ](#tts.core.report.db.ReportItemComment.ReportItemComment.GetTimestamp)
  - [C RevaluationComment ](#tts.core.report.db.ReportItem.RevaluationComment)
    - [M GetAuthor ](#tts.core.report.db.ReportItem.RevaluationComment.GetAuthor)
    - [M GetResult ](#tts.core.report.db.ReportItem.RevaluationComment.GetResult)
    - [M GetText ](#tts.core.report.db.ReportItem.RevaluationComment.GetText)
    - [M GetTime ](#tts.core.report.db.ReportItem.RevaluationComment.GetTime)
- [ Variables ](#variables)
  - [C PackageParameterVariable ](#tts.core.report.db.Variable.PackageParameterVariable)
    - [M GetDescription ](#tts.core.report.db.Variable.PackageParameterVariable.GetDescription)
    - [M GetName ](#tts.core.report.db.Variable.PackageParameterVariable.GetName)
    - [M GetOrigin ](#tts.core.report.db.Variable.PackageParameterVariable.GetOrigin)
    - [M GetValue ](#tts.core.report.db.Variable.PackageParameterVariable.GetValue)
  - [C PackageReturnVariable ](#tts.core.report.db.Variable.PackageReturnVariable)
    - [M GetDescription ](#tts.core.report.db.Variable.PackageReturnVariable.GetDescription)
    - [M GetName ](#tts.core.report.db.Variable.PackageReturnVariable.GetName)
    - [M GetValue ](#tts.core.report.db.Variable.PackageReturnVariable.GetValue)
  - [C PackageVariable ](#tts.core.report.db.Variable.PackageVariable)
    - [M GetDescription ](#tts.core.report.db.Variable.PackageVariable.GetDescription)
    - [M GetName ](#tts.core.report.db.Variable.PackageVariable.GetName)
    - [M GetValue ](#tts.core.report.db.Variable.PackageVariable.GetValue)

[ Object API ](objectApi.md)

[ Trace Analysis API ](../TraceAnalysisAPI/index.md)

[ Generator APIs ](../generators/index.md)

[ Tools ](../tools/index.md)

[ User test management ](../userTestmanagement/index.md)

[ UserUtility API ](../user-utility/user-utility.md)

[ Utility Examples ](../user-utility/example-utilities.md)

Report API

- [ ReportApi ](#id1)
  - [C ReportApi ](#tts.core.report.parser.ReportApi.ReportApi)
    - [M AnalysePath ](#tts.core.report.parser.ReportApi.ReportApi.AnalysePath)
    - [M GetArtifacts ](#tts.core.report.parser.ReportApi.ReportApi.GetArtifacts)
    - [M GetConfiguration ](#tts.core.report.parser.ReportApi.ReportApi.GetConfiguration)
    - [M GetDbDir ](#tts.core.report.parser.ReportApi.ReportApi.GetDbDir)
    - [M GetDbFile ](#tts.core.report.parser.ReportApi.ReportApi.GetDbFile)
    - [M GetInfo ](#tts.core.report.parser.ReportApi.ReportApi.GetInfo)
    - [M GetMainPackage ](#tts.core.report.parser.ReportApi.ReportApi.GetMainPackage)
    - [M GetMainProject ](#tts.core.report.parser.ReportApi.ReportApi.GetMainProject)
    - [M GetPackage ](#tts.core.report.parser.ReportApi.ReportApi.GetPackage)
    - [M GetPatchInfo ](#tts.core.report.parser.ReportApi.ReportApi.GetPatchInfo)
    - [M GetReportDir ](#tts.core.report.parser.ReportApi.ReportApi.GetReportDir)
    - [M GetResultBgColor ](#tts.core.report.parser.ReportApi.ReportApi.GetResultBgColor)
    - [M GetResultColor ](#tts.core.report.parser.ReportApi.ReportApi.GetResultColor)
    - [M GetResultTxtColor ](#tts.core.report.parser.ReportApi.ReportApi.GetResultTxtColor)
    - [M GetRootActivity ](#tts.core.report.parser.ReportApi.ReportApi.GetRootActivity)
    - [M GetSetting ](#tts.core.report.parser.ReportApi.ReportApi.GetSetting)
    - [M GetSrcColor ](#tts.core.report.parser.ReportApi.ReportApi.GetSrcColor)
    - [M GetSrcStyle ](#tts.core.report.parser.ReportApi.ReportApi.GetSrcStyle)
    - [M GetTemplateDir ](#tts.core.report.parser.ReportApi.ReportApi.GetTemplateDir)
    - [M HasConfiguration ](#tts.core.report.parser.ReportApi.ReportApi.HasConfiguration)
    - [M IsFiltered ](#tts.core.report.parser.ReportApi.ReportApi.IsFiltered)
    - [M IsProjectReport ](#tts.core.report.parser.ReportApi.ReportApi.IsProjectReport)
    - [M IsSet ](#tts.core.report.parser.ReportApi.ReportApi.IsSet)
    - [M IterItems ](#tts.core.report.parser.ReportApi.ReportApi.IterItems)
    - [M MakeAbsPath ](#tts.core.report.parser.ReportApi.ReportApi.MakeAbsPath)
    - [M SetSetting ](#tts.core.report.parser.ReportApi.ReportApi.SetSetting)
    - [M GetPackageScmInfo ](#tts.core.report.parser.ReportApi.ReportApi.GetPackageScmInfo)
    - [M IterUserComments ](#tts.core.report.parser.ReportApi.ReportApi.IterUserComments)
- [ Artifact ](#artifact)
  - [C Artifact ](#tts.core.report.db.Artifact.Artifact)
    - [M GetContext ](#tts.core.report.db.Artifact.Artifact.GetContext)
    - [M GetFileHash ](#tts.core.report.db.Artifact.Artifact.GetFileHash)
    - [M GetFileName ](#tts.core.report.db.Artifact.Artifact.GetFileName)
    - [M GetFilePath ](#tts.core.report.db.Artifact.Artifact.GetFilePath)
    - [M GetId ](#tts.core.report.db.Artifact.Artifact.GetId)
    - [M GetMainPackageReportItemId ](#tts.core.report.db.Artifact.Artifact.GetMainPackageReportItemId)
- [ Attribute ](#attribute)
  - [C Attribute ](#tts.core.report.db.Attribute.Attribute)
    - [M GetId ](#tts.core.report.db.Attribute.Attribute.GetId)
    - [M GetName ](#tts.core.report.db.Attribute.Attribute.GetName)
    - [M GetOrigin ](#tts.core.report.db.Attribute.Attribute.GetOrigin)
    - [M GetReportItemId ](#tts.core.report.db.Attribute.Attribute.GetReportItemId)
    - [M GetValue ](#tts.core.report.db.Attribute.Attribute.GetValue)
- [ Configuration ](#module-tts.core.report.parser.Configuration)
  - [C Configuration ](#tts.core.report.parser.Configuration.Configuration)
    - [M GetTestBenchConfiguration ](#tts.core.report.parser.Configuration.Configuration.GetTestBenchConfiguration)
    - [M GetTestConfiguration ](#tts.core.report.parser.Configuration.Configuration.GetTestConfiguration)
    - [M HasTestBenchConfiguration ](#tts.core.report.parser.Configuration.Configuration.HasTestBenchConfiguration)
    - [M HasTestConfiguration ](#tts.core.report.parser.Configuration.Configuration.HasTestConfiguration)
  - [C PrfTestBenchConfiguration ](#tts.core.report.parser.Configuration.PrfTestBenchConfiguration)
    - [A PLibraryId ](#tts.core.report.parser.Configuration.PrfTestBenchConfiguration.PLibraryId)
    - [M GetId ](#tts.core.report.parser.Configuration.PrfTestBenchConfiguration.GetId)
    - [M GetLibraryId ](#tts.core.report.parser.Configuration.PrfTestBenchConfiguration.GetLibraryId)
    - [M GetName ](#tts.core.report.parser.Configuration.PrfTestBenchConfiguration.GetName)
    - [M GetPath ](#tts.core.report.parser.Configuration.PrfTestBenchConfiguration.GetPath)
    - [M GetTbcId ](#tts.core.report.parser.Configuration.PrfTestBenchConfiguration.GetTbcId)
    - [M GetTools ](#tts.core.report.parser.Configuration.PrfTestBenchConfiguration.GetTools)
    - [M HasTools ](#tts.core.report.parser.Configuration.PrfTestBenchConfiguration.HasTools)
    - [M IterTools ](#tts.core.report.parser.Configuration.PrfTestBenchConfiguration.IterTools)
  - [C PrfTestConfiguration ](#tts.core.report.parser.Configuration.PrfTestConfiguration)
    - [A PLibraryId ](#tts.core.report.parser.Configuration.PrfTestConfiguration.PLibraryId)
    - [M GetDataDir ](#tts.core.report.parser.Configuration.PrfTestConfiguration.GetDataDir)
    - [M GetEditor ](#tts.core.report.parser.Configuration.PrfTestConfiguration.GetEditor)
    - [M GetId ](#tts.core.report.parser.Configuration.PrfTestConfiguration.GetId)
    - [M GetLibraryId ](#tts.core.report.parser.Configuration.PrfTestConfiguration.GetLibraryId)
    - [M GetMappingFile ](#tts.core.report.parser.Configuration.PrfTestConfiguration.GetMappingFile)
    - [M GetName ](#tts.core.report.parser.Configuration.PrfTestConfiguration.GetName)
    - [M GetPath ](#tts.core.report.parser.Configuration.PrfTestConfiguration.GetPath)
    - [M GetPkgDir ](#tts.core.report.parser.Configuration.PrfTestConfiguration.GetPkgDir)
    - [M GetTcfId ](#tts.core.report.parser.Configuration.PrfTestConfiguration.GetTcfId)
    - [M GetTeststand ](#tts.core.report.parser.Configuration.PrfTestConfiguration.GetTeststand)
    - [M HasBusConfigurations ](#tts.core.report.parser.Configuration.PrfTestConfiguration.HasBusConfigurations)
    - [M HasConstFiles ](#tts.core.report.parser.Configuration.PrfTestConfiguration.HasConstFiles)
    - [M HasEcuConfigurations ](#tts.core.report.parser.Configuration.PrfTestConfiguration.HasEcuConfigurations)
    - [M HasEfsConfigurations ](#tts.core.report.parser.Configuration.PrfTestConfiguration.HasEfsConfigurations)
    - [M HasFunctionConfigurations ](#tts.core.report.parser.Configuration.PrfTestConfiguration.HasFunctionConfigurations)
    - [M HasModelConfigurations ](#tts.core.report.parser.Configuration.PrfTestConfiguration.HasModelConfigurations)
    - [M IterBusConfigurations ](#tts.core.report.parser.Configuration.PrfTestConfiguration.IterBusConfigurations)
    - [M IterConstFiles ](#tts.core.report.parser.Configuration.PrfTestConfiguration.IterConstFiles)
    - [M IterEcuConfigurations ](#tts.core.report.parser.Configuration.PrfTestConfiguration.IterEcuConfigurations)
    - [M IterEfsConfigurations ](#tts.core.report.parser.Configuration.PrfTestConfiguration.IterEfsConfigurations)
    - [M IterFunctionConfigurations ](#tts.core.report.parser.Configuration.PrfTestConfiguration.IterFunctionConfigurations)
    - [M IterMappingFiles ](#tts.core.report.parser.Configuration.PrfTestConfiguration.IterMappingFiles)
    - [M IterModelConfigurations ](#tts.core.report.parser.Configuration.PrfTestConfiguration.IterModelConfigurations)
  - [C TestBenchConfiguration ](#tts.core.report.parser.Configuration.TestBenchConfiguration)
    - [A PLibraryId ](#tts.core.report.parser.Configuration.TestBenchConfiguration.PLibraryId)
    - [M GetId ](#tts.core.report.parser.Configuration.TestBenchConfiguration.GetId)
    - [M GetLibraryId ](#tts.core.report.parser.Configuration.TestBenchConfiguration.GetLibraryId)
    - [M GetName ](#tts.core.report.parser.Configuration.TestBenchConfiguration.GetName)
    - [M GetPath ](#tts.core.report.parser.Configuration.TestBenchConfiguration.GetPath)
    - [M GetTbcId ](#tts.core.report.parser.Configuration.TestBenchConfiguration.GetTbcId)
    - [M GetTools ](#tts.core.report.parser.Configuration.TestBenchConfiguration.GetTools)
    - [M HasTools ](#tts.core.report.parser.Configuration.TestBenchConfiguration.HasTools)
    - [M IterTools ](#tts.core.report.parser.Configuration.TestBenchConfiguration.IterTools)
  - [C TestConfiguration ](#tts.core.report.parser.Configuration.TestConfiguration)
    - [A PLibraryId ](#tts.core.report.parser.Configuration.TestConfiguration.PLibraryId)
    - [M GetDataDir ](#tts.core.report.parser.Configuration.TestConfiguration.GetDataDir)
    - [M GetEditor ](#tts.core.report.parser.Configuration.TestConfiguration.GetEditor)
    - [M GetId ](#tts.core.report.parser.Configuration.TestConfiguration.GetId)
    - [M GetLibraryId ](#tts.core.report.parser.Configuration.TestConfiguration.GetLibraryId)
    - [M GetName ](#tts.core.report.parser.Configuration.TestConfiguration.GetName)
    - [M GetPath ](#tts.core.report.parser.Configuration.TestConfiguration.GetPath)
    - [M GetPkgDir ](#tts.core.report.parser.Configuration.TestConfiguration.GetPkgDir)
    - [M GetTcfId ](#tts.core.report.parser.Configuration.TestConfiguration.GetTcfId)
    - [M GetTeststand ](#tts.core.report.parser.Configuration.TestConfiguration.GetTeststand)
    - [M HasBusConfigurations ](#tts.core.report.parser.Configuration.TestConfiguration.HasBusConfigurations)
    - [M HasConstFiles ](#tts.core.report.parser.Configuration.TestConfiguration.HasConstFiles)
    - [M HasEcuConfigurations ](#tts.core.report.parser.Configuration.TestConfiguration.HasEcuConfigurations)
    - [M HasEfsConfigurations ](#tts.core.report.parser.Configuration.TestConfiguration.HasEfsConfigurations)
    - [M HasFunctionConfigurations ](#tts.core.report.parser.Configuration.TestConfiguration.HasFunctionConfigurations)
    - [M HasModelConfigurations ](#tts.core.report.parser.Configuration.TestConfiguration.HasModelConfigurations)
    - [M IterBusConfigurations ](#tts.core.report.parser.Configuration.TestConfiguration.IterBusConfigurations)
    - [M IterConstFiles ](#tts.core.report.parser.Configuration.TestConfiguration.IterConstFiles)
    - [M IterEcuConfigurations ](#tts.core.report.parser.Configuration.TestConfiguration.IterEcuConfigurations)
    - [M IterEfsConfigurations ](#tts.core.report.parser.Configuration.TestConfiguration.IterEfsConfigurations)
    - [M IterFunctionConfigurations ](#tts.core.report.parser.Configuration.TestConfiguration.IterFunctionConfigurations)
    - [M IterMappingFiles ](#tts.core.report.parser.Configuration.TestConfiguration.IterMappingFiles)
    - [M IterModelConfigurations ](#tts.core.report.parser.Configuration.TestConfiguration.IterModelConfigurations)
  - [C TrfTestBenchConfiguration ](#tts.core.report.parser.Configuration.TrfTestBenchConfiguration)
    - [A PLibraryId ](#tts.core.report.parser.Configuration.TrfTestBenchConfiguration.PLibraryId)
    - [M GetId ](#tts.core.report.parser.Configuration.TrfTestBenchConfiguration.GetId)
    - [M GetLibraryId ](#tts.core.report.parser.Configuration.TrfTestBenchConfiguration.GetLibraryId)
    - [M GetName ](#tts.core.report.parser.Configuration.TrfTestBenchConfiguration.GetName)
    - [M GetPath ](#tts.core.report.parser.Configuration.TrfTestBenchConfiguration.GetPath)
    - [M GetTbcId ](#tts.core.report.parser.Configuration.TrfTestBenchConfiguration.GetTbcId)
    - [M GetTools ](#tts.core.report.parser.Configuration.TrfTestBenchConfiguration.GetTools)
    - [M HasTools ](#tts.core.report.parser.Configuration.TrfTestBenchConfiguration.HasTools)
    - [M IterTools ](#tts.core.report.parser.Configuration.TrfTestBenchConfiguration.IterTools)
  - [C TrfTestConfiguration ](#tts.core.report.parser.Configuration.TrfTestConfiguration)
    - [A PLibraryId ](#tts.core.report.parser.Configuration.TrfTestConfiguration.PLibraryId)
    - [M GetDataDir ](#tts.core.report.parser.Configuration.TrfTestConfiguration.GetDataDir)
    - [M GetEditor ](#tts.core.report.parser.Configuration.TrfTestConfiguration.GetEditor)
    - [M GetId ](#tts.core.report.parser.Configuration.TrfTestConfiguration.GetId)
    - [M GetLibraryId ](#tts.core.report.parser.Configuration.TrfTestConfiguration.GetLibraryId)
    - [M GetMappingFile ](#tts.core.report.parser.Configuration.TrfTestConfiguration.GetMappingFile)
    - [M GetName ](#tts.core.report.parser.Configuration.TrfTestConfiguration.GetName)
    - [M GetPath ](#tts.core.report.parser.Configuration.TrfTestConfiguration.GetPath)
    - [M GetPkgDir ](#tts.core.report.parser.Configuration.TrfTestConfiguration.GetPkgDir)
    - [M GetTcfId ](#tts.core.report.parser.Configuration.TrfTestConfiguration.GetTcfId)
    - [M GetTeststand ](#tts.core.report.parser.Configuration.TrfTestConfiguration.GetTeststand)
    - [M HasBusConfigurations ](#tts.core.report.parser.Configuration.TrfTestConfiguration.HasBusConfigurations)
    - [M HasConstFiles ](#tts.core.report.parser.Configuration.TrfTestConfiguration.HasConstFiles)
    - [M HasEcuConfigurations ](#tts.core.report.parser.Configuration.TrfTestConfiguration.HasEcuConfigurations)
    - [M HasEfsConfigurations ](#tts.core.report.parser.Configuration.TrfTestConfiguration.HasEfsConfigurations)
    - [M HasFunctionConfigurations ](#tts.core.report.parser.Configuration.TrfTestConfiguration.HasFunctionConfigurations)
    - [M HasModelConfigurations ](#tts.core.report.parser.Configuration.TrfTestConfiguration.HasModelConfigurations)
    - [M IterBusConfigurations ](#tts.core.report.parser.Configuration.TrfTestConfiguration.IterBusConfigurations)
    - [M IterConstFiles ](#tts.core.report.parser.Configuration.TrfTestConfiguration.IterConstFiles)
    - [M IterEcuConfigurations ](#tts.core.report.parser.Configuration.TrfTestConfiguration.IterEcuConfigurations)
    - [M IterEfsConfigurations ](#tts.core.report.parser.Configuration.TrfTestConfiguration.IterEfsConfigurations)
    - [M IterFunctionConfigurations ](#tts.core.report.parser.Configuration.TrfTestConfiguration.IterFunctionConfigurations)
    - [M IterMappingFiles ](#tts.core.report.parser.Configuration.TrfTestConfiguration.IterMappingFiles)
    - [M IterModelConfigurations ](#tts.core.report.parser.Configuration.TrfTestConfiguration.IterModelConfigurations)
  - [C TcfBus ](#tts.core.report.db.TcfBus.TcfBus)
    - [M GetDbPath ](#tts.core.report.db.TcfBus.TcfBus.GetDbPath)
    - [M GetFbxChn ](#tts.core.report.db.TcfBus.TcfBus.GetFbxChn)
    - [M GetId ](#tts.core.report.db.TcfBus.TcfBus.GetId)
    - [M GetTcfBusId ](#tts.core.report.db.TcfBus.TcfBus.GetTcfBusId)
    - [M GetTcfId ](#tts.core.report.db.TcfBus.TcfBus.GetTcfId)
  - [C TcfEcu ](#tts.core.report.db.TcfEcu.TcfEcu)
    - [A PDiagHSFZSettings ](#tts.core.report.db.TcfEcu.TcfEcu.PDiagHSFZSettings)
    - [M GetA2lFile ](#tts.core.report.db.TcfEcu.TcfEcu.GetA2lFile)
    - [M GetDebugHex ](#tts.core.report.db.TcfEcu.TcfEcu.GetDebugHex)
    - [M GetDiagDoIpSettings ](#tts.core.report.db.TcfEcu.TcfEcu.GetDiagDoIpSettings)
    - [M GetDiagDoSoAdSettings ](#tts.core.report.db.TcfEcu.TcfEcu.GetDiagDoSoAdSettings)
    - [M GetDiagFrTpSettings ](#tts.core.report.db.TcfEcu.TcfEcu.GetDiagFrTpSettings)
    - [M GetDiagHSFZSettings ](#tts.core.report.db.TcfEcu.TcfEcu.GetDiagHSFZSettings)
    - [M GetDiagIsoTpSettings ](#tts.core.report.db.TcfEcu.TcfEcu.GetDiagIsoTpSettings)
    - [M GetDiagPort ](#tts.core.report.db.TcfEcu.TcfEcu.GetDiagPort)
    - [M GetDiagUDSSettings ](#tts.core.report.db.TcfEcu.TcfEcu.GetDiagUDSSettings)
    - [M GetDiagnosticDb ](#tts.core.report.db.TcfEcu.TcfEcu.GetDiagnosticDb)
    - [M GetElf ](#tts.core.report.db.TcfEcu.TcfEcu.GetElf)
    - [M GetElfs ](#tts.core.report.db.TcfEcu.TcfEcu.GetElfs)
    - [M GetHexFile ](#tts.core.report.db.TcfEcu.TcfEcu.GetHexFile)
    - [M GetId ](#tts.core.report.db.TcfEcu.TcfEcu.GetId)
    - [M GetLogDatabase ](#tts.core.report.db.TcfEcu.TcfEcu.GetLogDatabase)
    - [M GetLogFilterFile ](#tts.core.report.db.TcfEcu.TcfEcu.GetLogFilterFile)
    - [M GetLogilink ](#tts.core.report.db.TcfEcu.TcfEcu.GetLogilink)
    - [M GetSgbd ](#tts.core.report.db.TcfEcu.TcfEcu.GetSgbd)
    - [M GetSgbdVersion ](#tts.core.report.db.TcfEcu.TcfEcu.GetSgbdVersion)
    - [M GetTcfEcuId ](#tts.core.report.db.TcfEcu.TcfEcu.GetTcfEcuId)
    - [M GetTcfId ](#tts.core.report.db.TcfEcu.TcfEcu.GetTcfId)
  - [C TcfEfs ](#tts.core.report.db.TcfEfs.TcfEfs)
    - [M GetDb ](#tts.core.report.db.TcfEfs.TcfEfs.GetDb)
    - [M GetId ](#tts.core.report.db.TcfEfs.TcfEfs.GetId)
    - [M GetTcfEfsId ](#tts.core.report.db.TcfEfs.TcfEfs.GetTcfEfsId)
    - [M GetTcfId ](#tts.core.report.db.TcfEfs.TcfEfs.GetTcfId)
  - [C TcfExecution ](#tts.core.report.db.TcfExecution.TcfExecution)
    - [M GetSimulationMode ](#tts.core.report.db.TcfExecution.TcfExecution.GetSimulationMode)
    - [M GetTcfId ](#tts.core.report.db.TcfExecution.TcfExecution.GetTcfId)
    - [M GetWaitAfterTeststep ](#tts.core.report.db.TcfExecution.TcfExecution.GetWaitAfterTeststep)
  - [C TcfFct ](#tts.core.report.db.TcfFct.TcfFct)
    - [M GetCatalog ](#tts.core.report.db.TcfFct.TcfFct.GetCatalog)
    - [M GetId ](#tts.core.report.db.TcfFct.TcfFct.GetId)
    - [M GetTcfFctId ](#tts.core.report.db.TcfFct.TcfFct.GetTcfFctId)
    - [M GetTcfId ](#tts.core.report.db.TcfFct.TcfFct.GetTcfId)
  - [C TcfModel ](#tts.core.report.db.TcfModel.TcfModel)
    - [M GetId ](#tts.core.report.db.TcfModel.TcfModel.GetId)
    - [M GetModel ](#tts.core.report.db.TcfModel.TcfModel.GetModel)
    - [M GetTcfId ](#tts.core.report.db.TcfModel.TcfModel.GetTcfId)
    - [M GetTcfModelId ](#tts.core.report.db.TcfModel.TcfModel.GetTcfModelId)
    - [M GetTimebase ](#tts.core.report.db.TcfModel.TcfModel.GetTimebase)
    - [M GetVersion ](#tts.core.report.db.TcfModel.TcfModel.GetVersion)
  - [C TbcTool ](#tts.core.report.db.TbcTool.TbcTool)
    - [M GetLocation ](#tts.core.report.db.TbcTool.TbcTool.GetLocation)
    - [M GetName ](#tts.core.report.db.TbcTool.TbcTool.GetName)
    - [M GetPatches ](#tts.core.report.db.TbcTool.TbcTool.GetPatches)
    - [M GetStatus ](#tts.core.report.db.TbcTool.TbcTool.GetStatus)
    - [M GetTbcId ](#tts.core.report.db.TbcTool.TbcTool.GetTbcId)
    - [M GetTbcToolId ](#tts.core.report.db.TbcTool.TbcTool.GetTbcToolId)
    - [M GetVersion ](#tts.core.report.db.TbcTool.TbcTool.GetVersion)
- [ Constant ](#constant)
  - [C Constant ](#tts.core.report.db.Constant.Constant)
    - [M GetDescription ](#tts.core.report.db.Constant.Constant.GetDescription)
    - [M GetName ](#tts.core.report.db.Constant.Constant.GetName)
    - [M GetOrigin ](#tts.core.report.db.Constant.Constant.GetOrigin)
    - [M GetValue ](#tts.core.report.db.Constant.Constant.GetValue)
- [ Entities ](#entities)
  - [C Entity ](#tts.core.report.db.Entity.Entity)
    - [M GetEntityId ](#tts.core.report.db.Entity.Entity.GetEntityId)
    - [M GetId ](#tts.core.report.db.Entity.Entity.GetId)
    - [M GetName ](#tts.core.report.db.Entity.Entity.GetName)
    - [M GetReportItemId ](#tts.core.report.db.Entity.Entity.GetReportItemId)
    - [M GetType ](#tts.core.report.db.Entity.Entity.GetType)
  - [C ImageEntity ](#tts.core.report.db.ImageEntity.ImageEntity)
    - [M GetData ](#tts.core.report.db.ImageEntity.ImageEntity.GetData)
    - [M GetEntityId ](#tts.core.report.db.ImageEntity.ImageEntity.GetEntityId)
    - [M GetId ](#tts.core.report.db.ImageEntity.ImageEntity.GetId)
    - [M GetImage ](#tts.core.report.db.ImageEntity.ImageEntity.GetImage)
    - [M GetName ](#tts.core.report.db.ImageEntity.ImageEntity.GetName)
    - [M GetReportItemId ](#tts.core.report.db.ImageEntity.ImageEntity.GetReportItemId)
    - [M GetType ](#tts.core.report.db.ImageEntity.ImageEntity.GetType)
    - [M ToFile ](#tts.core.report.db.ImageEntity.ImageEntity.ToFile)
  - [C ImageExpectationEntity ](#tts.core.report.db.ImageExpectationEntity.ImageExpectationEntity)
    - [M GetActualImage ](#tts.core.report.db.ImageExpectationEntity.ImageExpectationEntity.GetActualImage)
    - [M GetEntityId ](#tts.core.report.db.ImageExpectationEntity.ImageExpectationEntity.GetEntityId)
    - [M GetExpectedImage ](#tts.core.report.db.ImageExpectationEntity.ImageExpectationEntity.GetExpectedImage)
    - [M GetId ](#tts.core.report.db.ImageExpectationEntity.ImageExpectationEntity.GetId)
    - [M GetName ](#tts.core.report.db.ImageExpectationEntity.ImageExpectationEntity.GetName)
    - [M GetReportItemId ](#tts.core.report.db.ImageExpectationEntity.ImageExpectationEntity.GetReportItemId)
    - [M GetType ](#tts.core.report.db.ImageExpectationEntity.ImageExpectationEntity.GetType)
  - [C RecordingInfosEntity ](#tts.core.report.parser.Package.RecordingInfosEntity)
    - [M GetCount ](#tts.core.report.parser.Package.RecordingInfosEntity.GetCount)
    - [M GetEntityId ](#tts.core.report.parser.Package.RecordingInfosEntity.GetEntityId)
    - [M GetId ](#tts.core.report.parser.Package.RecordingInfosEntity.GetId)
    - [M GetName ](#tts.core.report.parser.Package.RecordingInfosEntity.GetName)
    - [M GetRecording ](#tts.core.report.parser.Package.RecordingInfosEntity.GetRecording)
    - [M GetRecordingId ](#tts.core.report.parser.Package.RecordingInfosEntity.GetRecordingId)
    - [M GetReportItemId ](#tts.core.report.parser.Package.RecordingInfosEntity.GetReportItemId)
    - [M GetStartTime ](#tts.core.report.parser.Package.RecordingInfosEntity.GetStartTime)
    - [M GetStopTime ](#tts.core.report.parser.Package.RecordingInfosEntity.GetStopTime)
    - [M GetSyncDeltaT ](#tts.core.report.parser.Package.RecordingInfosEntity.GetSyncDeltaT)
    - [M GetType ](#tts.core.report.parser.Package.RecordingInfosEntity.GetType)
  - [C ProjectElementStatistic ](#tts.core.report.parser.ProjectElement.ProjectElementStatistic)
    - [M GetCountAndPercentageOfResultItem ](#tts.core.report.parser.ProjectElement.ProjectElementStatistic.GetCountAndPercentageOfResultItem)
    - [M GetCountOfResultItem ](#tts.core.report.parser.ProjectElement.ProjectElementStatistic.GetCountOfResultItem)
    - [M GetEntityId ](#tts.core.report.parser.ProjectElement.ProjectElementStatistic.GetEntityId)
    - [M GetErrorCount ](#tts.core.report.parser.ProjectElement.ProjectElementStatistic.GetErrorCount)
    - [M GetFailedCount ](#tts.core.report.parser.ProjectElement.ProjectElementStatistic.GetFailedCount)
    - [M GetHeader ](#tts.core.report.parser.ProjectElement.ProjectElementStatistic.GetHeader)
    - [M GetId ](#tts.core.report.parser.ProjectElement.ProjectElementStatistic.GetId)
    - [M GetInconCount ](#tts.core.report.parser.ProjectElement.ProjectElementStatistic.GetInconCount)
    - [M GetName ](#tts.core.report.parser.ProjectElement.ProjectElementStatistic.GetName)
    - [M GetNoneCount ](#tts.core.report.parser.ProjectElement.ProjectElementStatistic.GetNoneCount)
    - [M GetNumberCols ](#tts.core.report.parser.ProjectElement.ProjectElementStatistic.GetNumberCols)
    - [M GetNumberRows ](#tts.core.report.parser.ProjectElement.ProjectElementStatistic.GetNumberRows)
    - [M GetPercentageOfResultItem ](#tts.core.report.parser.ProjectElement.ProjectElementStatistic.GetPercentageOfResultItem)
    - [M GetReportItemId ](#tts.core.report.parser.ProjectElement.ProjectElementStatistic.GetReportItemId)
    - [M GetResult ](#tts.core.report.parser.ProjectElement.ProjectElementStatistic.GetResult)
    - [M GetResultCount ](#tts.core.report.parser.ProjectElement.ProjectElementStatistic.GetResultCount)
    - [M GetSuccessCount ](#tts.core.report.parser.ProjectElement.ProjectElementStatistic.GetSuccessCount)
    - [M GetTotalCount ](#tts.core.report.parser.ProjectElement.ProjectElementStatistic.GetTotalCount)
    - [M GetType ](#tts.core.report.parser.ProjectElement.ProjectElementStatistic.GetType)
    - [M GetValue ](#tts.core.report.parser.ProjectElement.ProjectElementStatistic.GetValue)
    - [M IterRowsWithResult ](#tts.core.report.parser.ProjectElement.ProjectElementStatistic.IterRowsWithResult)
  - [C TableEntity ](#tts.core.report.db.TableEntity.TableEntity)
    - [M GetCountAndPercentageOfResultItem ](#tts.core.report.db.TableEntity.TableEntity.GetCountAndPercentageOfResultItem)
    - [M GetCountOfResultItem ](#tts.core.report.db.TableEntity.TableEntity.GetCountOfResultItem)
    - [M GetEntityId ](#tts.core.report.db.TableEntity.TableEntity.GetEntityId)
    - [M GetHeader ](#tts.core.report.db.TableEntity.TableEntity.GetHeader)
    - [M GetId ](#tts.core.report.db.TableEntity.TableEntity.GetId)
    - [M GetName ](#tts.core.report.db.TableEntity.TableEntity.GetName)
    - [M GetNumberCols ](#tts.core.report.db.TableEntity.TableEntity.GetNumberCols)
    - [M GetNumberRows ](#tts.core.report.db.TableEntity.TableEntity.GetNumberRows)
    - [M GetPercentageOfResultItem ](#tts.core.report.db.TableEntity.TableEntity.GetPercentageOfResultItem)
    - [M GetReportItemId ](#tts.core.report.db.TableEntity.TableEntity.GetReportItemId)
    - [M GetResult ](#tts.core.report.db.TableEntity.TableEntity.GetResult)
    - [M GetType ](#tts.core.report.db.TableEntity.TableEntity.GetType)
    - [M GetValue ](#tts.core.report.db.TableEntity.TableEntity.GetValue)
    - [M IterRowsWithResult ](#tts.core.report.db.TableEntity.TableEntity.IterRowsWithResult)
  - [C TextEntity ](#tts.core.report.db.TextEntity.TextEntity)
    - [M GetEntityId ](#tts.core.report.db.TextEntity.TextEntity.GetEntityId)
    - [M GetId ](#tts.core.report.db.TextEntity.TextEntity.GetId)
    - [M GetName ](#tts.core.report.db.TextEntity.TextEntity.GetName)
    - [M GetReportItemId ](#tts.core.report.db.TextEntity.TextEntity.GetReportItemId)
    - [M GetType ](#tts.core.report.db.TextEntity.TextEntity.GetType)
    - [M GetValue ](#tts.core.report.db.TextEntity.TextEntity.GetValue)
  - [C TraceArtifactEntity ](#tts.core.report.parser.Package.TraceArtifactEntity)
    - [M GetComment ](#tts.core.report.parser.Package.TraceArtifactEntity.GetComment)
    - [M GetCount ](#tts.core.report.parser.Package.TraceArtifactEntity.GetCount)
    - [M GetEntityId ](#tts.core.report.parser.Package.TraceArtifactEntity.GetEntityId)
    - [M GetId ](#tts.core.report.parser.Package.TraceArtifactEntity.GetId)
    - [M GetName ](#tts.core.report.parser.Package.TraceArtifactEntity.GetName)
    - [M GetRecording ](#tts.core.report.parser.Package.TraceArtifactEntity.GetRecording)
    - [M GetRecordingId ](#tts.core.report.parser.Package.TraceArtifactEntity.GetRecordingId)
    - [M GetReportItemId ](#tts.core.report.parser.Package.TraceArtifactEntity.GetReportItemId)
    - [M GetSourceReportItem ](#tts.core.report.parser.Package.TraceArtifactEntity.GetSourceReportItem)
    - [M GetSourceReportItemId ](#tts.core.report.parser.Package.TraceArtifactEntity.GetSourceReportItemId)
    - [M GetType ](#tts.core.report.parser.Package.TraceArtifactEntity.GetType)
    - [M IterItems ](#tts.core.report.parser.Package.TraceArtifactEntity.IterItems)
- [ Image ](#image)
  - [C Image ](#tts.core.report.db.Image.Image)
    - [M GetBitmap ](#tts.core.report.db.Image.Image.GetBitmap)
    - [M GetDepth ](#tts.core.report.db.Image.Image.GetDepth)
    - [M GetHeight ](#tts.core.report.db.Image.Image.GetHeight)
    - [M GetId ](#tts.core.report.db.Image.Image.GetId)
    - [M GetMaskColor ](#tts.core.report.db.Image.Image.GetMaskColor)
    - [M GetName ](#tts.core.report.db.Image.Image.GetName)
    - [M GetSubTitle ](#tts.core.report.db.Image.Image.GetSubTitle)
    - [M GetTitle ](#tts.core.report.db.Image.Image.GetTitle)
    - [M GetWidth ](#tts.core.report.db.Image.Image.GetWidth)
- [ Info ](#info)
  - [C Info ](#tts.core.report.db.Info.Info)
    - [M GetAppName ](#tts.core.report.db.Info.Info.GetAppName)
    - [M GetAppVersion ](#tts.core.report.db.Info.Info.GetAppVersion)
    - [M GetAuthor ](#tts.core.report.db.Info.Info.GetAuthor)
    - [M GetDbVersion ](#tts.core.report.db.Info.Info.GetDbVersion)
    - [M GetDuration ](#tts.core.report.db.Info.Info.GetDuration)
    - [M GetExecutionMode ](#tts.core.report.db.Info.Info.GetExecutionMode)
    - [M GetExecutionTime ](#tts.core.report.db.Info.Info.GetExecutionTime)
    - [M GetId ](#tts.core.report.db.Info.Info.GetId)
    - [M GetInfoId ](#tts.core.report.db.Info.Info.GetInfoId)
    - [M GetKeywordCatalog ](#tts.core.report.db.Info.Info.GetKeywordCatalog)
    - [M GetProjectExecutionPath ](#tts.core.report.db.Info.Info.GetProjectExecutionPath)
    - [M GetResult ](#tts.core.report.db.Info.Info.GetResult)
    - [M GetSignature ](#tts.core.report.db.Info.Info.GetSignature)
    - [M GetTeststand ](#tts.core.report.db.Info.Info.GetTeststand)
    - [M GetTimeZoneUTCOffset ](#tts.core.report.db.Info.Info.GetTimeZoneUTCOffset)
    - [M GetTimeZoneUTCOffsetStr ](#tts.core.report.db.Info.Info.GetTimeZoneUTCOffsetStr)
    - [M GetUUID ](#tts.core.report.db.Info.Info.GetUUID)
- [ MappingItem ](#mappingitem)
  - [C MappingItem ](#tts.core.report.db.MappingItem.MappingItem)
    - [M GetDescription ](#tts.core.report.db.MappingItem.MappingItem.GetDescription)
    - [M GetId ](#tts.core.report.db.MappingItem.MappingItem.GetId)
    - [M GetMappingItemId ](#tts.core.report.db.MappingItem.MappingItem.GetMappingItemId)
    - [M GetName ](#tts.core.report.db.MappingItem.MappingItem.GetName)
    - [M GetOrigin ](#tts.core.report.db.MappingItem.MappingItem.GetOrigin)
    - [M GetParentId ](#tts.core.report.db.MappingItem.MappingItem.GetParentId)
    - [M GetTarget ](#tts.core.report.db.MappingItem.MappingItem.GetTarget)
    - [M GetType ](#tts.core.report.db.MappingItem.MappingItem.GetType)
    - [M GetUsedRaster ](#tts.core.report.db.MappingItem.MappingItem.GetUsedRaster)
    - [M GetWantedRaster ](#tts.core.report.db.MappingItem.MappingItem.GetWantedRaster)
    - [M IsForcedRaster ](#tts.core.report.db.MappingItem.MappingItem.IsForcedRaster)
    - [M IsGlobal ](#tts.core.report.db.MappingItem.MappingItem.IsGlobal)
- [ Package ](#module-tts.core.report.parser.Package)
  - [C AnalysisJobItem ](#tts.core.report.parser.Package.AnalysisJobItem)
    - [M GetMaxExecLevel ](#tts.core.report.parser.Package.AnalysisJobItem.GetMaxExecLevel)
    - [M GetOriginalResult ](#tts.core.report.parser.Package.AnalysisJobItem.GetOriginalResult)
    - [M GetResult ](#tts.core.report.parser.Package.AnalysisJobItem.GetResult)
    - [M GetStimulationPackage ](#tts.core.report.parser.Package.AnalysisJobItem.GetStimulationPackage)
    - [M GetTraceAnalysis ](#tts.core.report.parser.Package.AnalysisJobItem.GetTraceAnalysis)
    - [M HasData ](#tts.core.report.parser.Package.AnalysisJobItem.HasData)
    - [M HasParams ](#tts.core.report.parser.Package.AnalysisJobItem.HasParams)
    - [M HasReturnValues ](#tts.core.report.parser.Package.AnalysisJobItem.HasReturnValues)
    - [M IterParameterVariables ](#tts.core.report.parser.Package.AnalysisJobItem.IterParameterVariables)
    - [M IterReturnVariables ](#tts.core.report.parser.Package.AnalysisJobItem.IterReturnVariables)
    - [M IterTraceItems ](#tts.core.report.parser.Package.AnalysisJobItem.IterTraceItems)
    - [M IterUserComments ](#tts.core.report.parser.Package.AnalysisJobItem.IterUserComments)
  - [C Mapping ](#tts.core.report.parser.Package.Mapping)
    - [M GetDescription ](#tts.core.report.parser.Package.Mapping.GetDescription)
    - [M GetId ](#tts.core.report.parser.Package.Mapping.GetId)
    - [M GetMappingItemId ](#tts.core.report.parser.Package.Mapping.GetMappingItemId)
    - [M GetName ](#tts.core.report.parser.Package.Mapping.GetName)
    - [M GetOrigin ](#tts.core.report.parser.Package.Mapping.GetOrigin)
    - [M GetParentId ](#tts.core.report.parser.Package.Mapping.GetParentId)
    - [M GetTarget ](#tts.core.report.parser.Package.Mapping.GetTarget)
    - [M GetType ](#tts.core.report.parser.Package.Mapping.GetType)
    - [M GetUsedRaster ](#tts.core.report.parser.Package.Mapping.GetUsedRaster)
    - [M GetWantedRaster ](#tts.core.report.parser.Package.Mapping.GetWantedRaster)
    - [M HasSubMappings ](#tts.core.report.parser.Package.Mapping.HasSubMappings)
    - [M IsForcedRaster ](#tts.core.report.parser.Package.Mapping.IsForcedRaster)
    - [M IsGlobal ](#tts.core.report.parser.Package.Mapping.IsGlobal)
    - [M IterSubMappings ](#tts.core.report.parser.Package.Mapping.IterSubMappings)
  - [C Mappings ](#tts.core.report.parser.Package.Mappings)
    - [M IterMappings ](#tts.core.report.parser.Package.Mappings.IterMappings)
  - [C Package ](#tts.core.report.parser.Package.Package)
    - [M GetAbortCode ](#tts.core.report.parser.Package.Package.GetAbortCode)
    - [M GetAbortComment ](#tts.core.report.parser.Package.Package.GetAbortComment)
    - [M GetAdditionalInfo ](#tts.core.report.parser.Package.Package.GetAdditionalInfo)
    - [M GetArtifacts ](#tts.core.report.parser.Package.Package.GetArtifacts)
    - [M GetCallError ](#tts.core.report.parser.Package.Package.GetCallError)
    - [M GetComment ](#tts.core.report.parser.Package.Package.GetComment)
    - [M GetDescription ](#tts.core.report.parser.Package.Package.GetDescription)
    - [M GetDuration ](#tts.core.report.parser.Package.Package.GetDuration)
    - [M GetElementName ](#tts.core.report.parser.Package.Package.GetElementName)
    - [M GetGlobalConstantsDefinedOnStart ](#tts.core.report.parser.Package.Package.GetGlobalConstantsDefinedOnStart)
    - [M GetHash ](#tts.core.report.parser.Package.Package.GetHash)
    - [M GetId ](#tts.core.report.parser.Package.Package.GetId)
    - [M GetIsTestcase ](#tts.core.report.parser.Package.Package.GetIsTestcase)
    - [M GetLibraryId ](#tts.core.report.parser.Package.Package.GetLibraryId)
    - [M GetLinkedTestManagementIds ](#tts.core.report.parser.Package.Package.GetLinkedTestManagementIds)
    - [M GetMappings ](#tts.core.report.parser.Package.Package.GetMappings)
    - [M GetName ](#tts.core.report.parser.Package.Package.GetName)
    - [M GetOriginalResult ](#tts.core.report.parser.Package.Package.GetOriginalResult)
    - [M GetParameterDescription ](#tts.core.report.parser.Package.Package.GetParameterDescription)
    - [M GetParameterInitialValue ](#tts.core.report.parser.Package.Package.GetParameterInitialValue)
    - [M GetParameterNames ](#tts.core.report.parser.Package.Package.GetParameterNames)
    - [M GetParameterOrigin ](#tts.core.report.parser.Package.Package.GetParameterOrigin)
    - [M GetParameterValue ](#tts.core.report.parser.Package.Package.GetParameterValue)
    - [M GetPath ](#tts.core.report.parser.Package.Package.GetPath)
    - [M GetPkgId ](#tts.core.report.parser.Package.Package.GetPkgId)
    - [M GetRecordings ](#tts.core.report.parser.Package.Package.GetRecordings)
    - [M GetReportItemId ](#tts.core.report.parser.Package.Package.GetReportItemId)
    - [M GetResult ](#tts.core.report.parser.Package.Package.GetResult)
    - [M GetReturnDescription ](#tts.core.report.parser.Package.Package.GetReturnDescription)
    - [M GetReturnInitialValue ](#tts.core.report.parser.Package.Package.GetReturnInitialValue)
    - [M GetReturnNames ](#tts.core.report.parser.Package.Package.GetReturnNames)
    - [M GetReturnValue ](#tts.core.report.parser.Package.Package.GetReturnValue)
    - [M GetRevalComments ](#tts.core.report.parser.Package.Package.GetRevalComments)
    - [M GetRevalCommentsString ](#tts.core.report.parser.Package.Package.GetRevalCommentsString)
    - [M GetRevision ](#tts.core.report.parser.Package.Package.GetRevision)
    - [M GetSCMBranch ](#tts.core.report.parser.Package.Package.GetSCMBranch)
    - [M GetSCMStatus ](#tts.core.report.parser.Package.Package.GetSCMStatus)
    - [M GetSCMUrl ](#tts.core.report.parser.Package.Package.GetSCMUrl)
    - [M GetStimulationPackage ](#tts.core.report.parser.Package.Package.GetStimulationPackage)
    - [M GetSubReportPath ](#tts.core.report.parser.Package.Package.GetSubReportPath)
    - [M GetTestCase ](#tts.core.report.parser.Package.Package.GetTestCase)
    - [M GetTestScriptId ](#tts.core.report.parser.Package.Package.GetTestScriptId)
    - [M GetTestmanagementId ](#tts.core.report.parser.Package.Package.GetTestmanagementId)
    - [M GetTime ](#tts.core.report.parser.Package.Package.GetTime)
    - [M GetTraceAnalyses ](#tts.core.report.parser.Package.Package.GetTraceAnalyses)
    - [M GetUserReportData ](#tts.core.report.parser.Package.Package.GetUserReportData)
    - [M GetVersion ](#tts.core.report.parser.Package.Package.GetVersion)
    - [M HasAnalysisJobs ](#tts.core.report.parser.Package.Package.HasAnalysisJobs)
    - [M HasAttributes ](#tts.core.report.parser.Package.Package.HasAttributes)
    - [M HasMappings ](#tts.core.report.parser.Package.Package.HasMappings)
    - [M HasParams ](#tts.core.report.parser.Package.Package.HasParams)
    - [M HasRecordings ](#tts.core.report.parser.Package.Package.HasRecordings)
    - [M HasReturnValues ](#tts.core.report.parser.Package.Package.HasReturnValues)
    - [M HasRevalComments ](#tts.core.report.parser.Package.Package.HasRevalComments)
    - [M HasTestCase ](#tts.core.report.parser.Package.Package.HasTestCase)
    - [M HasTraceAnalyses ](#tts.core.report.parser.Package.Package.HasTraceAnalyses)
    - [M IsAnalysisPackage ](#tts.core.report.parser.Package.Package.IsAnalysisPackage)
    - [M IsSkipped ](#tts.core.report.parser.Package.Package.IsSkipped)
    - [M IsStimulationPackage ](#tts.core.report.parser.Package.Package.IsStimulationPackage)
    - [M IterAnalysisJobs ](#tts.core.report.parser.Package.Package.IterAnalysisJobs)
    - [M IterAttributes ](#tts.core.report.parser.Package.Package.IterAttributes)
    - [M IterParameterVariables ](#tts.core.report.parser.Package.Package.IterParameterVariables)
    - [M IterReturnVariables ](#tts.core.report.parser.Package.Package.IterReturnVariables)
    - [M IterReturnVariablesAfterTest ](#tts.core.report.parser.Package.Package.IterReturnVariablesAfterTest)
    - [M IterUserComments ](#tts.core.report.parser.Package.Package.IterUserComments)
    - [M GetComponentName ](#tts.core.report.parser.Package.Package.GetComponentName)
  - [C ParallelPackage ](#tts.core.report.parser.Package.ParallelPackage)
    - [M GetAbortCode ](#tts.core.report.parser.Package.ParallelPackage.GetAbortCode)
    - [M GetAbortComment ](#tts.core.report.parser.Package.ParallelPackage.GetAbortComment)
    - [M GetAdditionalInfo ](#tts.core.report.parser.Package.ParallelPackage.GetAdditionalInfo)
    - [M GetCallError ](#tts.core.report.parser.Package.ParallelPackage.GetCallError)
    - [M GetComment ](#tts.core.report.parser.Package.ParallelPackage.GetComment)
    - [M GetDescription ](#tts.core.report.parser.Package.ParallelPackage.GetDescription)
    - [M GetDuration ](#tts.core.report.parser.Package.ParallelPackage.GetDuration)
    - [M GetElementName ](#tts.core.report.parser.Package.ParallelPackage.GetElementName)
    - [M GetGlobalConstantsDefinedOnStart ](#tts.core.report.parser.Package.ParallelPackage.GetGlobalConstantsDefinedOnStart)
    - [M GetHash ](#tts.core.report.parser.Package.ParallelPackage.GetHash)
    - [M GetId ](#tts.core.report.parser.Package.ParallelPackage.GetId)
    - [M GetIsTestcase ](#tts.core.report.parser.Package.ParallelPackage.GetIsTestcase)
    - [M GetLibraryId ](#tts.core.report.parser.Package.ParallelPackage.GetLibraryId)
    - [M GetLinkedTestManagementIds ](#tts.core.report.parser.Package.ParallelPackage.GetLinkedTestManagementIds)
    - [M GetMappings ](#tts.core.report.parser.Package.ParallelPackage.GetMappings)
    - [M GetName ](#tts.core.report.parser.Package.ParallelPackage.GetName)
    - [M GetOriginalResult ](#tts.core.report.parser.Package.ParallelPackage.GetOriginalResult)
    - [M GetParameterDescription ](#tts.core.report.parser.Package.ParallelPackage.GetParameterDescription)
    - [M GetParameterInitialValue ](#tts.core.report.parser.Package.ParallelPackage.GetParameterInitialValue)
    - [M GetParameterNames ](#tts.core.report.parser.Package.ParallelPackage.GetParameterNames)
    - [M GetParameterOrigin ](#tts.core.report.parser.Package.ParallelPackage.GetParameterOrigin)
    - [M GetParameterValue ](#tts.core.report.parser.Package.ParallelPackage.GetParameterValue)
    - [M GetPath ](#tts.core.report.parser.Package.ParallelPackage.GetPath)
    - [M GetPkgId ](#tts.core.report.parser.Package.ParallelPackage.GetPkgId)
    - [M GetRecordings ](#tts.core.report.parser.Package.ParallelPackage.GetRecordings)
    - [M GetReportItemId ](#tts.core.report.parser.Package.ParallelPackage.GetReportItemId)
    - [M GetResult ](#tts.core.report.parser.Package.ParallelPackage.GetResult)
    - [M GetReturnDescription ](#tts.core.report.parser.Package.ParallelPackage.GetReturnDescription)
    - [M GetReturnInitialValue ](#tts.core.report.parser.Package.ParallelPackage.GetReturnInitialValue)
    - [M GetReturnNames ](#tts.core.report.parser.Package.ParallelPackage.GetReturnNames)
    - [M GetReturnValue ](#tts.core.report.parser.Package.ParallelPackage.GetReturnValue)
    - [M GetRevalComments ](#tts.core.report.parser.Package.ParallelPackage.GetRevalComments)
    - [M GetRevalCommentsString ](#tts.core.report.parser.Package.ParallelPackage.GetRevalCommentsString)
    - [M GetRevision ](#tts.core.report.parser.Package.ParallelPackage.GetRevision)
    - [M GetSCMBranch ](#tts.core.report.parser.Package.ParallelPackage.GetSCMBranch)
    - [M GetSCMStatus ](#tts.core.report.parser.Package.ParallelPackage.GetSCMStatus)
    - [M GetSCMUrl ](#tts.core.report.parser.Package.ParallelPackage.GetSCMUrl)
    - [M GetStimulationPackage ](#tts.core.report.parser.Package.ParallelPackage.GetStimulationPackage)
    - [M GetTestCase ](#tts.core.report.parser.Package.ParallelPackage.GetTestCase)
    - [M GetTestScriptId ](#tts.core.report.parser.Package.ParallelPackage.GetTestScriptId)
    - [M GetTestmanagementId ](#tts.core.report.parser.Package.ParallelPackage.GetTestmanagementId)
    - [M GetTime ](#tts.core.report.parser.Package.ParallelPackage.GetTime)
    - [M GetTraceAnalyses ](#tts.core.report.parser.Package.ParallelPackage.GetTraceAnalyses)
    - [M GetUserReportData ](#tts.core.report.parser.Package.ParallelPackage.GetUserReportData)
    - [M GetVersion ](#tts.core.report.parser.Package.ParallelPackage.GetVersion)
    - [M HasAnalysisJobs ](#tts.core.report.parser.Package.ParallelPackage.HasAnalysisJobs)
    - [M HasAttributes ](#tts.core.report.parser.Package.ParallelPackage.HasAttributes)
    - [M HasMappings ](#tts.core.report.parser.Package.ParallelPackage.HasMappings)
    - [M HasParams ](#tts.core.report.parser.Package.ParallelPackage.HasParams)
    - [M HasRecordings ](#tts.core.report.parser.Package.ParallelPackage.HasRecordings)
    - [M HasReturnValues ](#tts.core.report.parser.Package.ParallelPackage.HasReturnValues)
    - [M HasRevalComments ](#tts.core.report.parser.Package.ParallelPackage.HasRevalComments)
    - [M HasTestCase ](#tts.core.report.parser.Package.ParallelPackage.HasTestCase)
    - [M HasTraceAnalyses ](#tts.core.report.parser.Package.ParallelPackage.HasTraceAnalyses)
    - [M IsAnalysisPackage ](#tts.core.report.parser.Package.ParallelPackage.IsAnalysisPackage)
    - [M IsSkipped ](#tts.core.report.parser.Package.ParallelPackage.IsSkipped)
    - [M IsStimulationPackage ](#tts.core.report.parser.Package.ParallelPackage.IsStimulationPackage)
    - [M IterAnalysisJobs ](#tts.core.report.parser.Package.ParallelPackage.IterAnalysisJobs)
    - [M IterAttributes ](#tts.core.report.parser.Package.ParallelPackage.IterAttributes)
    - [M IterParameterVariables ](#tts.core.report.parser.Package.ParallelPackage.IterParameterVariables)
    - [M IterReturnVariables ](#tts.core.report.parser.Package.ParallelPackage.IterReturnVariables)
    - [M IterReturnVariablesAfterTest ](#tts.core.report.parser.Package.ParallelPackage.IterReturnVariablesAfterTest)
    - [M IterUserComments ](#tts.core.report.parser.Package.ParallelPackage.IterUserComments)
    - [M GetComponentName ](#tts.core.report.parser.Package.ParallelPackage.GetComponentName)
  - [C Recording ](#tts.core.report.parser.Package.Recording)
    - [M GetMeasurementListFile ](#tts.core.report.parser.Package.Recording.GetMeasurementListFile)
    - [M GetNumberOfMeasurementListFileSignals ](#tts.core.report.parser.Package.Recording.GetNumberOfMeasurementListFileSignals)
    - [M GetOrigin ](#tts.core.report.parser.Package.Recording.GetOrigin)
    - [M GetSignalGroupName ](#tts.core.report.parser.Package.Recording.GetSignalGroupName)
    - [M GetSource ](#tts.core.report.parser.Package.Recording.GetSource)
    - [M GetSyncDeltaT ](#tts.core.report.parser.Package.Recording.GetSyncDeltaT)
    - [M IterMappings ](#tts.core.report.parser.Package.Recording.IterMappings)
    - [M IterSignals ](#tts.core.report.parser.Package.Recording.IterSignals)
  - [C Recordings ](#tts.core.report.parser.Package.Recordings)
    - [M IterRecordings ](#tts.core.report.parser.Package.Recordings.IterRecordings)
  - [C ReportItem ](#tts.core.report.parser.Package.ReportItem)
    - [A PPackageReportName ](#tts.core.report.parser.Package.ReportItem.PPackageReportName)
    - [M GetAbortCode ](#tts.core.report.parser.Package.ReportItem.GetAbortCode)
    - [M GetAbortComment ](#tts.core.report.parser.Package.ReportItem.GetAbortComment)
    - [M GetAbsoluteTimestamp ](#tts.core.report.parser.Package.ReportItem.GetAbsoluteTimestamp)
    - [M GetAdditionalInfo ](#tts.core.report.parser.Package.ReportItem.GetAdditionalInfo)
    - [M GetComment ](#tts.core.report.parser.Package.ReportItem.GetComment)
    - [M GetDuration ](#tts.core.report.parser.Package.ReportItem.GetDuration)
    - [M GetElementaryResult ](#tts.core.report.parser.Package.ReportItem.GetElementaryResult)
    - [M GetExecLevel ](#tts.core.report.parser.Package.ReportItem.GetExecLevel)
    - [M GetId ](#tts.core.report.parser.Package.ReportItem.GetId)
    - [M GetImageKey ](#tts.core.report.parser.Package.ReportItem.GetImageKey)
    - [M GetInfo ](#tts.core.report.parser.Package.ReportItem.GetInfo)
    - [M GetLabel ](#tts.core.report.parser.Package.ReportItem.GetLabel)
    - [M GetLinkedTestManagementIds ](#tts.core.report.parser.Package.ReportItem.GetLinkedTestManagementIds)
    - [M GetLoopCycle ](#tts.core.report.parser.Package.ReportItem.GetLoopCycle)
    - [M GetMappingTargets ](#tts.core.report.parser.Package.ReportItem.GetMappingTargets)
    - [M GetName ](#tts.core.report.parser.Package.ReportItem.GetName)
    - [M GetOriginalResult ](#tts.core.report.parser.Package.ReportItem.GetOriginalResult)
    - [M GetPackageInfo ](#tts.core.report.parser.Package.ReportItem.GetPackageInfo)
    - [M GetPackageReportName ](#tts.core.report.parser.Package.ReportItem.GetPackageReportName)
    - [M GetPackageScmInfo ](#tts.core.report.parser.Package.ReportItem.GetPackageScmInfo)
    - [M GetParentId ](#tts.core.report.parser.Package.ReportItem.GetParentId)
    - [M GetPos ](#tts.core.report.parser.Package.ReportItem.GetPos)
    - [M GetRelativeRealtime ](#tts.core.report.parser.Package.ReportItem.GetRelativeRealtime)
    - [M GetRelativeTimestamp ](#tts.core.report.parser.Package.ReportItem.GetRelativeTimestamp)
    - [M GetReportItemId ](#tts.core.report.parser.Package.ReportItem.GetReportItemId)
    - [M GetResult ](#tts.core.report.parser.Package.ReportItem.GetResult)
    - [M GetRevalComments ](#tts.core.report.parser.Package.ReportItem.GetRevalComments)
    - [M GetRevalCommentsString ](#tts.core.report.parser.Package.ReportItem.GetRevalCommentsString)
    - [M GetSrc ](#tts.core.report.parser.Package.ReportItem.GetSrc)
    - [M GetSrcCategory ](#tts.core.report.parser.Package.ReportItem.GetSrcCategory)
    - [M GetSrcIndex ](#tts.core.report.parser.Package.ReportItem.GetSrcIndex)
    - [M GetSrcSubType ](#tts.core.report.parser.Package.ReportItem.GetSrcSubType)
    - [M GetSrcType ](#tts.core.report.parser.Package.ReportItem.GetSrcType)
    - [M GetTargetValue ](#tts.core.report.parser.Package.ReportItem.GetTargetValue)
    - [M GetUndocumentedChild ](#tts.core.report.parser.Package.ReportItem.GetUndocumentedChild)
    - [M HasEntities ](#tts.core.report.parser.Package.ReportItem.HasEntities)
    - [M HasRevalComments ](#tts.core.report.parser.Package.ReportItem.HasRevalComments)
    - [M HasTag ](#tts.core.report.parser.Package.ReportItem.HasTag)
    - [M InitFromParentId ](#tts.core.report.parser.Package.ReportItem.InitFromParentId)
    - [M InitFromParentItem ](#tts.core.report.parser.Package.ReportItem.InitFromParentItem)
    - [M IsSkipped ](#tts.core.report.parser.Package.ReportItem.IsSkipped)
    - [M IterEntities ](#tts.core.report.parser.Package.ReportItem.IterEntities)
    - [M IterTags ](#tts.core.report.parser.Package.ReportItem.IterTags)
    - [M IterUserComments ](#tts.core.report.parser.Package.ReportItem.IterUserComments)
    - [M SetPackageReportName ](#tts.core.report.parser.Package.ReportItem.SetPackageReportName)
    - [M GetActivity ](#tts.core.report.parser.Package.ReportItem.GetActivity)
  - [C TestCase ](#tts.core.report.parser.Package.TestCase)
    - [M GetMaxExecLevel ](#tts.core.report.parser.Package.TestCase.GetMaxExecLevel)
    - [M GetResult ](#tts.core.report.parser.Package.TestCase.GetResult)
    - [M HasData ](#tts.core.report.parser.Package.TestCase.HasData)
    - [M IterTestSteps ](#tts.core.report.parser.Package.TestCase.IterTestSteps)
  - [C TraceAnalyses ](#tts.core.report.parser.Package.TraceAnalyses)
    - [M GetMaxExecLevel ](#tts.core.report.parser.Package.TraceAnalyses.GetMaxExecLevel)
    - [M HasData ](#tts.core.report.parser.Package.TraceAnalyses.HasData)
    - [M IterTraceItems ](#tts.core.report.parser.Package.TraceAnalyses.IterTraceItems)
- [ ProjectElements ](#module-tts.core.report.parser.ProjectElement)
  - [C ConfigChange ](#tts.core.report.parser.ProjectElement.ConfigChange)
    - [M GetAdditionalInfo ](#tts.core.report.parser.ProjectElement.ConfigChange.GetAdditionalInfo)
    - [M GetComment ](#tts.core.report.parser.ProjectElement.ConfigChange.GetComment)
    - [M GetDuration ](#tts.core.report.parser.ProjectElement.ConfigChange.GetDuration)
    - [M GetElementName ](#tts.core.report.parser.ProjectElement.ConfigChange.GetElementName)
    - [M GetName ](#tts.core.report.parser.ProjectElement.ConfigChange.GetName)
    - [M GetOriginalResult ](#tts.core.report.parser.ProjectElement.ConfigChange.GetOriginalResult)
    - [M GetReportItemId ](#tts.core.report.parser.ProjectElement.ConfigChange.GetReportItemId)
    - [M GetResult ](#tts.core.report.parser.ProjectElement.ConfigChange.GetResult)
    - [M GetSrcType ](#tts.core.report.parser.ProjectElement.ConfigChange.GetSrcType)
    - [M GetStatistic ](#tts.core.report.parser.ProjectElement.ConfigChange.GetStatistic)
    - [M GetTestBenchConfiguration ](#tts.core.report.parser.ProjectElement.ConfigChange.GetTestBenchConfiguration)
    - [M GetTestConfiguration ](#tts.core.report.parser.ProjectElement.ConfigChange.GetTestConfiguration)
    - [M GetTime ](#tts.core.report.parser.ProjectElement.ConfigChange.GetTime)
    - [M HasTestBenchConfiguration ](#tts.core.report.parser.ProjectElement.ConfigChange.HasTestBenchConfiguration)
    - [M HasTestConfiguration ](#tts.core.report.parser.ProjectElement.ConfigChange.HasTestConfiguration)
    - [M IsSkipped ](#tts.core.report.parser.ProjectElement.ConfigChange.IsSkipped)
    - [M IterItems ](#tts.core.report.parser.ProjectElement.ConfigChange.IterItems)
    - [M IterUserComments ](#tts.core.report.parser.ProjectElement.ConfigChange.IterUserComments)
  - [C Project ](#tts.core.report.parser.ProjectElement.Project)
    - [A PLibraryId ](#tts.core.report.parser.ProjectElement.Project.PLibraryId)
    - [M GetAdditionalInfo ](#tts.core.report.parser.ProjectElement.Project.GetAdditionalInfo)
    - [M GetComment ](#tts.core.report.parser.ProjectElement.Project.GetComment)
    - [M GetDuration ](#tts.core.report.parser.ProjectElement.Project.GetDuration)
    - [M GetElementName ](#tts.core.report.parser.ProjectElement.Project.GetElementName)
    - [M GetLibraryId ](#tts.core.report.parser.ProjectElement.Project.GetLibraryId)
    - [M GetName ](#tts.core.report.parser.ProjectElement.Project.GetName)
    - [M GetOriginalResult ](#tts.core.report.parser.ProjectElement.Project.GetOriginalResult)
    - [M GetPrjCompName ](#tts.core.report.parser.ProjectElement.Project.GetPrjCompName)
    - [M GetPrjId ](#tts.core.report.parser.ProjectElement.Project.GetPrjId)
    - [M GetReportItemId ](#tts.core.report.parser.ProjectElement.Project.GetReportItemId)
    - [M GetResult ](#tts.core.report.parser.ProjectElement.Project.GetResult)
    - [M GetSrcType ](#tts.core.report.parser.ProjectElement.Project.GetSrcType)
    - [M GetStatistic ](#tts.core.report.parser.ProjectElement.Project.GetStatistic)
    - [M GetTestManagementId ](#tts.core.report.parser.ProjectElement.Project.GetTestManagementId)
    - [M GetTime ](#tts.core.report.parser.ProjectElement.Project.GetTime)
    - [M HasAttributes ](#tts.core.report.parser.ProjectElement.Project.HasAttributes)
    - [M IsSkipped ](#tts.core.report.parser.ProjectElement.Project.IsSkipped)
    - [M IterAttributes ](#tts.core.report.parser.ProjectElement.Project.IterAttributes)
    - [M IterItems ](#tts.core.report.parser.ProjectElement.Project.IterItems)
    - [M IterUserComments ](#tts.core.report.parser.ProjectElement.Project.IterUserComments)
  - [C ProjectElement ](#tts.core.report.parser.ProjectElement.ProjectElement)
    - [M GetAdditionalInfo ](#tts.core.report.parser.ProjectElement.ProjectElement.GetAdditionalInfo)
    - [M GetComment ](#tts.core.report.parser.ProjectElement.ProjectElement.GetComment)
    - [M GetDuration ](#tts.core.report.parser.ProjectElement.ProjectElement.GetDuration)
    - [M GetElementName ](#tts.core.report.parser.ProjectElement.ProjectElement.GetElementName)
    - [M GetName ](#tts.core.report.parser.ProjectElement.ProjectElement.GetName)
    - [M GetOriginalResult ](#tts.core.report.parser.ProjectElement.ProjectElement.GetOriginalResult)
    - [M GetReportItemId ](#tts.core.report.parser.ProjectElement.ProjectElement.GetReportItemId)
    - [M GetResult ](#tts.core.report.parser.ProjectElement.ProjectElement.GetResult)
    - [M GetSrcType ](#tts.core.report.parser.ProjectElement.ProjectElement.GetSrcType)
    - [M GetStatistic ](#tts.core.report.parser.ProjectElement.ProjectElement.GetStatistic)
    - [M GetTime ](#tts.core.report.parser.ProjectElement.ProjectElement.GetTime)
    - [M IsSkipped ](#tts.core.report.parser.ProjectElement.ProjectElement.IsSkipped)
    - [M IterItems ](#tts.core.report.parser.ProjectElement.ProjectElement.IterItems)
    - [M IterUserComments ](#tts.core.report.parser.ProjectElement.ProjectElement.IterUserComments)
- [ ReportItems ](#reportitems)
  - [C ReportItem ](#tts.core.report.db.ReportItem.ReportItem)
    - [M GetAbortCode ](#tts.core.report.db.ReportItem.ReportItem.GetAbortCode)
    - [M GetAbortComment ](#tts.core.report.db.ReportItem.ReportItem.GetAbortComment)
    - [M GetAbsoluteTimestamp ](#tts.core.report.db.ReportItem.ReportItem.GetAbsoluteTimestamp)
    - [M GetAdditionalInfo ](#tts.core.report.db.ReportItem.ReportItem.GetAdditionalInfo)
    - [M GetComment ](#tts.core.report.db.ReportItem.ReportItem.GetComment)
    - [M GetDuration ](#tts.core.report.db.ReportItem.ReportItem.GetDuration)
    - [M GetElementaryResult ](#tts.core.report.db.ReportItem.ReportItem.GetElementaryResult)
    - [M GetExecLevel ](#tts.core.report.db.ReportItem.ReportItem.GetExecLevel)
    - [M GetId ](#tts.core.report.db.ReportItem.ReportItem.GetId)
    - [M GetImageKey ](#tts.core.report.db.ReportItem.ReportItem.GetImageKey)
    - [M GetInfo ](#tts.core.report.db.ReportItem.ReportItem.GetInfo)
    - [M GetLabel ](#tts.core.report.db.ReportItem.ReportItem.GetLabel)
    - [M GetLinkedTestManagementIds ](#tts.core.report.db.ReportItem.ReportItem.GetLinkedTestManagementIds)
    - [M GetLoopCycle ](#tts.core.report.db.ReportItem.ReportItem.GetLoopCycle)
    - [M GetName ](#tts.core.report.db.ReportItem.ReportItem.GetName)
    - [M GetOriginalResult ](#tts.core.report.db.ReportItem.ReportItem.GetOriginalResult)
    - [M GetParentId ](#tts.core.report.db.ReportItem.ReportItem.GetParentId)
    - [M GetPos ](#tts.core.report.db.ReportItem.ReportItem.GetPos)
    - [M GetRelativeRealtime ](#tts.core.report.db.ReportItem.ReportItem.GetRelativeRealtime)
    - [M GetRelativeTimestamp ](#tts.core.report.db.ReportItem.ReportItem.GetRelativeTimestamp)
    - [M GetReportItemId ](#tts.core.report.db.ReportItem.ReportItem.GetReportItemId)
    - [M GetResult ](#tts.core.report.db.ReportItem.ReportItem.GetResult)
    - [M GetRevalComments ](#tts.core.report.db.ReportItem.ReportItem.GetRevalComments)
    - [M GetRevalCommentsString ](#tts.core.report.db.ReportItem.ReportItem.GetRevalCommentsString)
    - [M GetSrc ](#tts.core.report.db.ReportItem.ReportItem.GetSrc)
    - [M GetSrcCategory ](#tts.core.report.db.ReportItem.ReportItem.GetSrcCategory)
    - [M GetSrcIndex ](#tts.core.report.db.ReportItem.ReportItem.GetSrcIndex)
    - [M GetSrcSubType ](#tts.core.report.db.ReportItem.ReportItem.GetSrcSubType)
    - [M GetSrcType ](#tts.core.report.db.ReportItem.ReportItem.GetSrcType)
    - [M GetTargetValue ](#tts.core.report.db.ReportItem.ReportItem.GetTargetValue)
    - [M GetUndocumentedChild ](#tts.core.report.db.ReportItem.ReportItem.GetUndocumentedChild)
    - [M HasRevalComments ](#tts.core.report.db.ReportItem.ReportItem.HasRevalComments)
    - [M InitFromParentId ](#tts.core.report.db.ReportItem.ReportItem.InitFromParentId)
    - [M InitFromParentItem ](#tts.core.report.db.ReportItem.ReportItem.InitFromParentItem)
    - [M IsSkipped ](#tts.core.report.db.ReportItem.ReportItem.IsSkipped)
    - [M GetActivity ](#tts.core.report.db.ReportItem.ReportItem.GetActivity)
  - [C ReportItemAnalysisInfo ](#tts.core.report.db.ReportItemAnalysisInfo.ReportItemAnalysisInfo)
    - [M GetImplementedAnalysisLabel ](#tts.core.report.db.ReportItemAnalysisInfo.ReportItemAnalysisInfo.GetImplementedAnalysisLabel)
    - [M GetReportItemId ](#tts.core.report.db.ReportItemAnalysisInfo.ReportItemAnalysisInfo.GetReportItemId)
    - [M GetStimParamReportItemId ](#tts.core.report.db.ReportItemAnalysisInfo.ReportItemAnalysisInfo.GetStimParamReportItemId)
    - [M GetStimReportItemId ](#tts.core.report.db.ReportItemAnalysisInfo.ReportItemAnalysisInfo.GetStimReportItemId)
    - [M IsRequested ](#tts.core.report.db.ReportItemAnalysisInfo.ReportItemAnalysisInfo.IsRequested)
  - [C ReportItemComment ](#tts.core.report.db.ReportItemComment.ReportItemComment)
    - [M GetAuthor ](#tts.core.report.db.ReportItemComment.ReportItemComment.GetAuthor)
    - [M GetId ](#tts.core.report.db.ReportItemComment.ReportItemComment.GetId)
    - [M GetOverriddenResult ](#tts.core.report.db.ReportItemComment.ReportItemComment.GetOverriddenResult)
    - [M GetReportItemId ](#tts.core.report.db.ReportItemComment.ReportItemComment.GetReportItemId)
    - [M GetText ](#tts.core.report.db.ReportItemComment.ReportItemComment.GetText)
    - [M GetTimestamp ](#tts.core.report.db.ReportItemComment.ReportItemComment.GetTimestamp)
  - [C RevaluationComment ](#tts.core.report.db.ReportItem.RevaluationComment)
    - [M GetAuthor ](#tts.core.report.db.ReportItem.RevaluationComment.GetAuthor)
    - [M GetResult ](#tts.core.report.db.ReportItem.RevaluationComment.GetResult)
    - [M GetText ](#tts.core.report.db.ReportItem.RevaluationComment.GetText)
    - [M GetTime ](#tts.core.report.db.ReportItem.RevaluationComment.GetTime)
- [ Variables ](#variables)
  - [C PackageParameterVariable ](#tts.core.report.db.Variable.PackageParameterVariable)
    - [M GetDescription ](#tts.core.report.db.Variable.PackageParameterVariable.GetDescription)
    - [M GetName ](#tts.core.report.db.Variable.PackageParameterVariable.GetName)
    - [M GetOrigin ](#tts.core.report.db.Variable.PackageParameterVariable.GetOrigin)
    - [M GetValue ](#tts.core.report.db.Variable.PackageParameterVariable.GetValue)
  - [C PackageReturnVariable ](#tts.core.report.db.Variable.PackageReturnVariable)
    - [M GetDescription ](#tts.core.report.db.Variable.PackageReturnVariable.GetDescription)
    - [M GetName ](#tts.core.report.db.Variable.PackageReturnVariable.GetName)
    - [M GetValue ](#tts.core.report.db.Variable.PackageReturnVariable.GetValue)
  - [C PackageVariable ](#tts.core.report.db.Variable.PackageVariable)
    - [M GetDescription ](#tts.core.report.db.Variable.PackageVariable.GetDescription)
    - [M GetName ](#tts.core.report.db.Variable.PackageVariable.GetName)
    - [M GetValue ](#tts.core.report.db.Variable.PackageVariable.GetValue)

# Report API[¶](#report-api "Link to this heading")

Custom report generators may use this API to retrieve detailed test report information.

## ReportApi[¶](#id1 "Link to this heading")

*class* ReportApi[¶](#tts.core.report.parser.ReportApi.ReportApi "Link to this definition")  
Instance var CAT_TESTCASE:  
1

Instance var CAT_PROJECT:  
2

Instance var CAT_TRACEANALYSIS:  
8

AnalysePath(*[path](#tts.core.report.parser.ReportApi.ReportApi.AnalysePath.path "tts.core.report.parser.ReportApi.ReportApi.AnalysePath.path (Python parameter) — path to analyse")*)[¶](#tts.core.report.parser.ReportApi.ReportApi.AnalysePath "Link to this definition")  
Analyses whether the given path is a subpath of the report or database directory. If it is then a string and a relative path are returned. Otherwise None and the original path are returned. In both cases the ‘\\ separator is replaced by ‘/’.

Parameters:  path : str[¶](#tts.core.report.parser.ReportApi.ReportApi.AnalysePath.path "Permalink to this definition")  
path to analyse

Returns:  Result of the analysis

Return type:  tuple[str, str]

GetArtifacts()[¶](#tts.core.report.parser.ReportApi.ReportApi.GetArtifacts "Link to this definition")  
Returns all artifacts that are referenced by any package in the report.

Returns:  A list of all artifacts.

Return type:  list[[`Artifact`](#tts.core.report.db.Artifact.Artifact "tts.core.report.db.Artifact.Artifact (Python class) — Represents an artifact that is shown in the package's report summary "Artifacts" tab.")]

GetConfiguration()[¶](#tts.core.report.parser.ReportApi.ReportApi.GetConfiguration "Link to this definition")  
Do not use with project reports.

Returns:  Configuration set during Package execution

Return type:  [`Configuration`](#tts.core.report.parser.Configuration.Configuration "tts.core.report.parser.Configuration.Configuration (Python class) — The Configuration represents information about the used test bench configuration and test configuration.")

GetDbDir()[¶](#tts.core.report.parser.ReportApi.ReportApi.GetDbDir "Link to this definition")  
Returns:  Directory of the database file

Return type:  str

GetDbFile()[¶](#tts.core.report.parser.ReportApi.ReportApi.GetDbFile "Link to this definition")  
Returns:  Path to the database file

Return type:  str

GetInfo()[¶](#tts.core.report.parser.ReportApi.ReportApi.GetInfo "Link to this definition")  
Get an [`Info`](#tts.core.report.db.Info.Info "tts.core.report.db.Info.Info (Python class) — The name of the used application") object that holds some general information about the database.

Returns:  General information

Return type:  [`Info`](#tts.core.report.db.Info.Info "tts.core.report.db.Info.Info (Python class) — The name of the used application")

GetMainPackage()[¶](#tts.core.report.parser.ReportApi.ReportApi.GetMainPackage "Link to this definition")  
Do not use with project reports.

Returns:  The main Package of a report

Return type:  [`Package`](#tts.core.report.parser.Package.Package "tts.core.report.parser.Package.Package (Python class) — This class represents a Package that was executed individually or called directly from a Project.")

GetMainProject()[¶](#tts.core.report.parser.ReportApi.ReportApi.GetMainProject "Link to this definition")  
Returns:  The root project of a report

Return type:  [`Project`](#tts.core.report.parser.ProjectElement.Project "tts.core.report.parser.ProjectElement.Project (Python class) — Represents a Project report item.") | None

GetPackage(*[reportItem](#tts.core.report.parser.ReportApi.ReportApi.GetPackage.reportItem "tts.core.report.parser.ReportApi.ReportApi.GetPackage.reportItem (Python parameter) — A ReportItem that represents a Package")*)[¶](#tts.core.report.parser.ReportApi.ReportApi.GetPackage "Link to this definition")  
Parameters:  reportItem[¶](#tts.core.report.parser.ReportApi.ReportApi.GetPackage.reportItem "Permalink to this definition")  
A [`ReportItem`](#tts.core.report.parser.Package.ReportItem "tts.core.report.parser.Package.ReportItem (Python class) — Represents a report item.") that represents a [`Package`](#tts.core.report.parser.Package.Package "tts.core.report.parser.Package.Package (Python class) — This class represents a Package that was executed individually or called directly from a Project.")

Returns:  A created [`Package`](#tts.core.report.parser.Package.Package "tts.core.report.parser.Package.Package (Python class) — This class represents a Package that was executed individually or called directly from a Project.") object for the given [`ReportItem`](#tts.core.report.parser.Package.ReportItem "tts.core.report.parser.Package.ReportItem (Python class) — Represents a report item.").

Return type:  [`Package`](#tts.core.report.parser.Package.Package "tts.core.report.parser.Package.Package (Python class) — This class represents a Package that was executed individually or called directly from a Project.")

GetPatchInfo()[¶](#tts.core.report.parser.ReportApi.ReportApi.GetPatchInfo "Link to this definition")  
Returns a list of patch IDs, which where applied to the ecu.test that created the report.

Returns:  List of the ID of applied patches

Return type:  list[str]

GetReportDir()[¶](#tts.core.report.parser.ReportApi.ReportApi.GetReportDir "Link to this definition")  
Returns:  Target directory of the generated files

Return type:  str

GetResultBgColor(*[resultName](#tts.core.report.parser.ReportApi.ReportApi.GetResultBgColor.resultName "tts.core.report.parser.ReportApi.ReportApi.GetResultBgColor.resultName (Python parameter) — string name of the result, e.g.")*)[¶](#tts.core.report.parser.ReportApi.ReportApi.GetResultBgColor "Link to this definition")  
Get a string representing the background color used for the given result string in RGB notation.

Parameters:  resultName : str[¶](#tts.core.report.parser.ReportApi.ReportApi.GetResultBgColor.resultName "Permalink to this definition")  
string name of the result, e.g. “SUCCESS” or “FAILED”

Returns:  The background color

Return type:  str

GetResultColor(*[resultName](#tts.core.report.parser.ReportApi.ReportApi.GetResultColor.resultName "tts.core.report.parser.ReportApi.ReportApi.GetResultColor.resultName (Python parameter) — string name of the result, e.g.")*)[¶](#tts.core.report.parser.ReportApi.ReportApi.GetResultColor "Link to this definition")  
Get a string representing the result color of the given result string in RGB notation.

Parameters:  resultName : str[¶](#tts.core.report.parser.ReportApi.ReportApi.GetResultColor.resultName "Permalink to this definition")  
string name of the result, e.g. “SUCCESS” or “FAILED”

Returns:  The result color

Return type:  str

GetResultTxtColor(*[resultName](#tts.core.report.parser.ReportApi.ReportApi.GetResultTxtColor.resultName "tts.core.report.parser.ReportApi.ReportApi.GetResultTxtColor.resultName (Python parameter) — string name of the result, e.g.")*)[¶](#tts.core.report.parser.ReportApi.ReportApi.GetResultTxtColor "Link to this definition")  
Get a string representing the text color used for the given result string in RGB notation.

Parameters:  resultName : str[¶](#tts.core.report.parser.ReportApi.ReportApi.GetResultTxtColor.resultName "Permalink to this definition")  
string name of the result, e.g. “SUCCESS” or “FAILED”

Returns:  The text color

Return type:  str

GetRootActivity()[¶](#tts.core.report.parser.ReportApi.ReportApi.GetRootActivity "Link to this definition")  
Activity of the first element. On a project report it is the project name, otherwise empty.

Returns:  Name of the root project or an empty string

Return type:  str

GetSetting(*[name](#tts.core.report.parser.ReportApi.ReportApi.GetSetting.name "tts.core.report.parser.ReportApi.ReportApi.GetSetting.name (Python parameter) — settings name")*)[¶](#tts.core.report.parser.ReportApi.ReportApi.GetSetting "Link to this definition")  
Returns the value of the specified setting name of the templates config.xml

Parameters:  name : str[¶](#tts.core.report.parser.ReportApi.ReportApi.GetSetting.name "Permalink to this definition")  
settings name

Returns:  The settings value, None if there is no setting for the given name

Return type:  str | None

GetSrcColor(*[srcCategory](#tts.core.report.parser.ReportApi.ReportApi.GetSrcColor.srcCategory "tts.core.report.parser.ReportApi.ReportApi.GetSrcColor.srcCategory (Python parameter) — Category of the source, one of")*, *[srcType](#tts.core.report.parser.ReportApi.ReportApi.GetSrcColor.srcType "tts.core.report.parser.ReportApi.ReportApi.GetSrcColor.srcType (Python parameter) — String representing the type of the source, e.g.")*, *[srcSubType](#tts.core.report.parser.ReportApi.ReportApi.GetSrcColor.srcSubType "tts.core.report.parser.ReportApi.ReportApi.GetSrcColor.srcSubType (Python parameter) — UUID of a specific utility")*)[¶](#tts.core.report.parser.ReportApi.ReportApi.GetSrcColor "Link to this definition")  
Get a string representing the background color used to represent the given type of source in RGB notation.

Parameters:  srcCategory : int[¶](#tts.core.report.parser.ReportApi.ReportApi.GetSrcColor.srcCategory "Permalink to this definition")  
Category of the source, one of

- `CAT_TESTCASE`

- `CAT_PROJECT`

- `CAT_TRACEANALYSIS`

srcType : str[¶](#tts.core.report.parser.ReportApi.ReportApi.GetSrcColor.srcType "Permalink to this definition")  
String representing the type of the source, e.g. “READ” or “WRITE”

srcSubType : str[¶](#tts.core.report.parser.ReportApi.ReportApi.GetSrcColor.srcSubType "Permalink to this definition")  
UUID of a specific utility

Returns:  The background color

Return type:  str

GetSrcStyle(*[srcCategory](#tts.core.report.parser.ReportApi.ReportApi.GetSrcStyle.srcCategory "tts.core.report.parser.ReportApi.ReportApi.GetSrcStyle.srcCategory (Python parameter) — Category of the source, one of")*, *[srcType](#tts.core.report.parser.ReportApi.ReportApi.GetSrcStyle.srcType "tts.core.report.parser.ReportApi.ReportApi.GetSrcStyle.srcType (Python parameter) — String representing the type of the source, e.g.")*, *[srcSubType](#tts.core.report.parser.ReportApi.ReportApi.GetSrcStyle.srcSubType "tts.core.report.parser.ReportApi.ReportApi.GetSrcStyle.srcSubType (Python parameter) — UUID of a specific utility")*)[¶](#tts.core.report.parser.ReportApi.ReportApi.GetSrcStyle "Link to this definition")  
Parameters:  srcCategory : int[¶](#tts.core.report.parser.ReportApi.ReportApi.GetSrcStyle.srcCategory "Permalink to this definition")  
Category of the source, one of

- `CAT_TESTCASE`

- `CAT_PROJECT`

- `CAT_TRACEANALYSIS`

srcType : str[¶](#tts.core.report.parser.ReportApi.ReportApi.GetSrcStyle.srcType "Permalink to this definition")  
String representing the type of the source, e.g. “READ” or “WRITE”

srcSubType : str[¶](#tts.core.report.parser.ReportApi.ReportApi.GetSrcStyle.srcSubType "Permalink to this definition")  
UUID of a specific utility

Returns:  List of strings representing the style of the source

Return type:  list[str]

GetTemplateDir()[¶](#tts.core.report.parser.ReportApi.ReportApi.GetTemplateDir "Link to this definition")  
Returns:  Directory of the template of this report

Return type:  str

HasConfiguration()[¶](#tts.core.report.parser.ReportApi.ReportApi.HasConfiguration "Link to this definition")  
Do not use with project reports.

Returns:  True if a configuration was set during the Package execution, otherwise False

Return type:  bool

IsFiltered(*[component](#tts.core.report.parser.ReportApi.ReportApi.IsFiltered.component "tts.core.report.parser.ReportApi.ReportApi.IsFiltered.component (Python parameter) — component name (Testcase, TraceAnalysis or Project)")*)[¶](#tts.core.report.parser.ReportApi.ReportApi.IsFiltered "Link to this definition")  
Checks whether the component is filtered.

Parameters:  component : str[¶](#tts.core.report.parser.ReportApi.ReportApi.IsFiltered.component "Permalink to this definition")  
component name (Testcase, TraceAnalysis or Project)

Returns:  True if the component is filtered else False

Return type:  bool

IsProjectReport()[¶](#tts.core.report.parser.ReportApi.ReportApi.IsProjectReport "Link to this definition")  
Returns:  True if the report is the result of a project execution, otherwise False

Return type:  bool

IsSet(*[name](#tts.core.report.parser.ReportApi.ReportApi.IsSet.name "tts.core.report.parser.ReportApi.ReportApi.IsSet.name (Python parameter) — settings name")*, *[value](#tts.core.report.parser.ReportApi.ReportApi.IsSet.value "tts.core.report.parser.ReportApi.ReportApi.IsSet.value (Python parameter) — expected value")*)[¶](#tts.core.report.parser.ReportApi.ReportApi.IsSet "Link to this definition")  
Checks whether the setting name from the templates config.xml is set to value.

Parameters:  name : str[¶](#tts.core.report.parser.ReportApi.ReportApi.IsSet.name "Permalink to this definition")  
settings name

value : str[¶](#tts.core.report.parser.ReportApi.ReportApi.IsSet.value "Permalink to this definition")  
expected value

Returns:  True if the value of the given setting is equal to the given value, otherwise False

Return type:  bool

IterItems()[¶](#tts.core.report.parser.ReportApi.ReportApi.IterItems "Link to this definition")  
Returns an iterator with exactly two items. The first item is a [`Configuration`](#tts.core.report.parser.Configuration.Configuration "tts.core.report.parser.Configuration.Configuration (Python class) — The Configuration represents information about the used test bench configuration and test configuration."). The second item is either a [`Project`](#tts.core.report.parser.ProjectElement.Project "tts.core.report.parser.ProjectElement.Project (Python class) — Represents a Project report item.") (for a project report) or a [`Package`](#tts.core.report.parser.Package.Package "tts.core.report.parser.Package.Package (Python class) — This class represents a Package that was executed individually or called directly from a Project.") (for a package report).

Return type:  Iterator[[`Configuration`](#tts.core.report.parser.Configuration.Configuration "tts.core.report.parser.Configuration.Configuration (Python class) — The Configuration represents information about the used test bench configuration and test configuration.") | [`Project`](#tts.core.report.parser.ProjectElement.Project "tts.core.report.parser.ProjectElement.Project (Python class) — Represents a Project report item.") | [`Package`](#tts.core.report.parser.Package.Package "tts.core.report.parser.Package.Package (Python class) — This class represents a Package that was executed individually or called directly from a Project.")]

MakeAbsPath(*[path](#tts.core.report.parser.ReportApi.ReportApi.MakeAbsPath.path "tts.core.report.parser.ReportApi.ReportApi.MakeAbsPath.path (Python parameter) — path to join")*)[¶](#tts.core.report.parser.ReportApi.ReportApi.MakeAbsPath "Link to this definition")  
Joins the database directory with the given path

Parameters:  path : str[¶](#tts.core.report.parser.ReportApi.ReportApi.MakeAbsPath.path "Permalink to this definition")  
path to join

Returns:  An absolute path

Return type:  str

SetSetting(*[name](#tts.core.report.parser.ReportApi.ReportApi.SetSetting.name "tts.core.report.parser.ReportApi.ReportApi.SetSetting.name (Python parameter) — settings name")*, *[value](#tts.core.report.parser.ReportApi.ReportApi.SetSetting.value "tts.core.report.parser.ReportApi.ReportApi.SetSetting.value (Python parameter) — settings value")*)[¶](#tts.core.report.parser.ReportApi.ReportApi.SetSetting "Link to this definition")  
Sets a setting of the templates config.xml

Parameters:  name : str[¶](#tts.core.report.parser.ReportApi.ReportApi.SetSetting.name "Permalink to this definition")  
settings name

value : str[¶](#tts.core.report.parser.ReportApi.ReportApi.SetSetting.value "Permalink to this definition")  
settings value

GetPackageScmInfo(*[reportItem](#tts.core.report.parser.ReportApi.ReportApi.GetPackageScmInfo.reportItem "tts.core.report.parser.ReportApi.ReportApi.GetPackageScmInfo.reportItem (Python parameter) — A ReportItem that represents a Package")*)[¶](#tts.core.report.parser.ReportApi.ReportApi.GetPackageScmInfo "Link to this definition")  
Deprecated since version 2024.1: use [`ReportItem.GetPackageScmInfo()`](#tts.core.report.parser.Package.ReportItem.GetPackageScmInfo "tts.core.report.parser.Package.ReportItem.GetPackageScmInfo (Python method) — Information about the SCM")

Parameters:  reportItem[¶](#tts.core.report.parser.ReportApi.ReportApi.GetPackageScmInfo.reportItem "Permalink to this definition")  
A [`ReportItem`](#tts.core.report.parser.Package.ReportItem "tts.core.report.parser.Package.ReportItem (Python class) — Represents a report item.") that represents a [`Package`](#tts.core.report.parser.Package.Package "tts.core.report.parser.Package.Package (Python class) — This class represents a Package that was executed individually or called directly from a Project.")

Returns:  Information about the SCM

Return type:  tuple[str, str, str] | None

IterUserComments(*[reportItemId](#tts.core.report.parser.ReportApi.ReportApi.IterUserComments.reportItemId "tts.core.report.parser.ReportApi.ReportApi.IterUserComments.reportItemId (Python parameter) — ID of the ReportItem")*, *[recursive](#tts.core.report.parser.ReportApi.ReportApi.IterUserComments.recursive "tts.core.report.parser.ReportApi.ReportApi.IterUserComments.recursive (Python parameter) — If True, also comments of children are included.")=`False`*)[¶](#tts.core.report.parser.ReportApi.ReportApi.IterUserComments "Link to this definition")  
Deprecated since version 2024.1: use [`Package.IterUserComments()`](#tts.core.report.parser.Package.Package.IterUserComments "tts.core.report.parser.Package.Package.IterUserComments (Python method) — Yield all ReportItemComment of the ReportItem. If recursive is True, comments of all children are yielded as well. This can improve performance of reading all report comments significantly.") or [`ReportItem.IterUserComments()`](#tts.core.report.parser.Package.ReportItem.IterUserComments "tts.core.report.parser.Package.ReportItem.IterUserComments (Python method) — Yield all ReportItemComment of the ReportItem. If recursive is True, comments of all children are yielded as well. This can improve performance of reading all report comments significantly.")

Yield all [`ReportItemComment`](#tts.core.report.db.ReportItemComment.ReportItemComment "tts.core.report.db.ReportItemComment.ReportItemComment (Python class) — The author of the comment") of the [`ReportItem`](#tts.core.report.db.ReportItem.ReportItem "tts.core.report.db.ReportItem.ReportItem (Python class) — A report item represents the execution results of one test step. It contains information like test step number, time of execution, type of test step and custom fields. Furthermore additional information on a test step can be stored in so called entity elements being attached to the respective report item (e.g. TableEntity or TextEntity).") with the given reportItemId. If recursive is True, comments of all children are yielded too. This can improve performance of reading all report comments significantly.

Parameters:  reportItemId : int[¶](#tts.core.report.parser.ReportApi.ReportApi.IterUserComments.reportItemId "Permalink to this definition")  
ID of the [`ReportItem`](#tts.core.report.db.ReportItem.ReportItem "tts.core.report.db.ReportItem.ReportItem (Python class) — A report item represents the execution results of one test step. It contains information like test step number, time of execution, type of test step and custom fields. Furthermore additional information on a test step can be stored in so called entity elements being attached to the respective report item (e.g. TableEntity or TextEntity).")

recursive : bool[¶](#tts.core.report.parser.ReportApi.ReportApi.IterUserComments.recursive "Permalink to this definition")  
If True, also comments of children are included.

Type:  recursive: bool

Return type:  Iterator[[`ReportItemComment`](#tts.core.report.db.ReportItemComment.ReportItemComment "tts.core.report.db.ReportItemComment.ReportItemComment (Python class) — The author of the comment")]

## Artifact[¶](#artifact "Link to this heading")

*class* Artifact[¶](#tts.core.report.db.Artifact.Artifact "Link to this definition")  
Represents an artifact that is shown in the package’s report summary “Artifacts” tab.

GetContext()[¶](#tts.core.report.db.Artifact.Artifact.GetContext "Link to this definition")  
Returns the context of the artifact, e.g. test step.

Returns:  context of the artifact

Return type:  str | None

GetFileHash()[¶](#tts.core.report.db.Artifact.Artifact.GetFileHash "Link to this definition")  
Returns the MD5 hashsum of the artifact if available.

Returns:  md5 hashsum

Return type:  str | None

GetFileName()[¶](#tts.core.report.db.Artifact.Artifact.GetFileName "Link to this definition")  
Returns the file name of the artifact.

Returns:  artifact name

Return type:  str | None

GetFilePath()[¶](#tts.core.report.db.Artifact.Artifact.GetFilePath "Link to this definition")  
Returns the path/url of the artifact.

Returns:  artifact path/url

Return type:  str | None

GetId()[¶](#tts.core.report.db.Artifact.Artifact.GetId "Link to this definition")  
Returns Id of the artifact.

Returns:  Id of the artifact

Return type:  int | None

GetMainPackageReportItemId()[¶](#tts.core.report.db.Artifact.Artifact.GetMainPackageReportItemId "Link to this definition")  
Returns the Id of the corresponding main report item (the main package item Id).

Returns:  report item Id

Return type:  int | None

## Attribute[¶](#attribute "Link to this heading")

*class* Attribute[¶](#tts.core.report.db.Attribute.Attribute "Link to this definition")  
Represents attributes of a project, package, or test case

GetId()[¶](#tts.core.report.db.Attribute.Attribute.GetId "Link to this definition")  
Returns:  The ID of the attribute

Return type:  int

GetName()[¶](#tts.core.report.db.Attribute.Attribute.GetName "Link to this definition")  
Returns:  The name of the attribute

Return type:  str

GetOrigin()[¶](#tts.core.report.db.Attribute.Attribute.GetOrigin "Link to this definition")  
Returns:  The origin of the attribute

Return type:  str

GetReportItemId()[¶](#tts.core.report.db.Attribute.Attribute.GetReportItemId "Link to this definition")  
Returns:  The ID of the report item

Return type:  int

GetValue()[¶](#tts.core.report.db.Attribute.Attribute.GetValue "Link to this definition")  
Returns:  The value of the attribute

Return type:  str

## Configuration[¶](#module-tts.core.report.parser.Configuration "Link to this heading")

*class* Configuration[¶](#tts.core.report.parser.Configuration.Configuration "Link to this definition")  
The Configuration represents information about the used test bench configuration and test configuration.

GetTestBenchConfiguration()[¶](#tts.core.report.parser.Configuration.Configuration.GetTestBenchConfiguration "Link to this definition")  
Returns:  The tbc which is used in the configuration

Return type:  [`TestBenchConfiguration`](#tts.core.report.parser.Configuration.TestBenchConfiguration "tts.core.report.parser.Configuration.TestBenchConfiguration (Python class) — The TestBenchConfiguration represents information about a test bench configuration.") | None

GetTestConfiguration()[¶](#tts.core.report.parser.Configuration.Configuration.GetTestConfiguration "Link to this definition")  
Returns:  The tcf which is used in the configuration

Return type:  [`TestConfiguration`](#tts.core.report.parser.Configuration.TestConfiguration "tts.core.report.parser.Configuration.TestConfiguration (Python class) — The Tcf represents information about a test configuration.") | None

HasTestBenchConfiguration()[¶](#tts.core.report.parser.Configuration.Configuration.HasTestBenchConfiguration "Link to this definition")  
Returns:  True if the configuration has a tbc, otherwise False

Return type:  bool

HasTestConfiguration()[¶](#tts.core.report.parser.Configuration.Configuration.HasTestConfiguration "Link to this definition")  
Returns:  True if the configuration has a tcf, otherwise False

Return type:  bool

*class* PrfTestBenchConfiguration[¶](#tts.core.report.parser.Configuration.PrfTestBenchConfiguration "Link to this definition")  

PLibraryId[¶](#tts.core.report.parser.Configuration.PrfTestBenchConfiguration.PLibraryId "Link to this definition")  
Returns:  The library ID of the Package

Return type:  str or None

GetId()[¶](#tts.core.report.parser.Configuration.PrfTestBenchConfiguration.GetId "Link to this definition")  
Returns:  The ID of the tbc

Return type:  int

GetLibraryId()[¶](#tts.core.report.parser.Configuration.PrfTestBenchConfiguration.GetLibraryId "Link to this definition")  
Returns:  The library ID of the Package

Return type:  str or None

GetName()[¶](#tts.core.report.parser.Configuration.PrfTestBenchConfiguration.GetName "Link to this definition")  
Returns:  The name of the tbc

Return type:  str

GetPath()[¶](#tts.core.report.parser.Configuration.PrfTestBenchConfiguration.GetPath "Link to this definition")  
Returns:  The path of the tbc

Return type:  str

GetTbcId()[¶](#tts.core.report.parser.Configuration.PrfTestBenchConfiguration.GetTbcId "Link to this definition")  
Returns:  The ID of the tbc

Return type:  int

GetTools()[¶](#tts.core.report.parser.Configuration.PrfTestBenchConfiguration.GetTools "Link to this definition")  
Returns:  A list of all tools used in the tbc

Return type:  list\<[`TbcTool`](#tts.core.report.db.TbcTool.TbcTool "tts.core.report.db.TbcTool.TbcTool (Python class) — The TbcTool represents information about a tool used within a test bench configuration.")\>

HasTools()[¶](#tts.core.report.parser.Configuration.PrfTestBenchConfiguration.HasTools "Link to this definition")  
Returns:  True if the test bench configuration has any tools, otherwise False

Return type:  bool

IterTools()[¶](#tts.core.report.parser.Configuration.PrfTestBenchConfiguration.IterTools "Link to this definition")  
Returns:  An iterator of all tools in the configuration

Return type:  Iterator[[`TbcTool`](#tts.core.report.db.TbcTool.TbcTool "tts.core.report.db.TbcTool.TbcTool (Python class) — The TbcTool represents information about a tool used within a test bench configuration.")]

*class* PrfTestConfiguration[¶](#tts.core.report.parser.Configuration.PrfTestConfiguration "Link to this definition")  

PLibraryId[¶](#tts.core.report.parser.Configuration.PrfTestConfiguration.PLibraryId "Link to this definition")  
Returns:  The library ID of the Package

Return type:  str or None

GetDataDir()[¶](#tts.core.report.parser.Configuration.PrfTestConfiguration.GetDataDir "Link to this definition")  
Returns:  The data directory stored in the test configuration or the user-specific default data directory if the test configuration does not define a data directory

Return type:  str

GetEditor()[¶](#tts.core.report.parser.Configuration.PrfTestConfiguration.GetEditor "Link to this definition")  
Returns:  The editor of the TCF

Return type:  str

GetId()[¶](#tts.core.report.parser.Configuration.PrfTestConfiguration.GetId "Link to this definition")  
Returns:  The ID of the TCF

Return type:  int

GetLibraryId()[¶](#tts.core.report.parser.Configuration.PrfTestConfiguration.GetLibraryId "Link to this definition")  
Returns:  The library ID of the Package

Return type:  str or None

GetMappingFile()[¶](#tts.core.report.parser.Configuration.PrfTestConfiguration.GetMappingFile "Link to this definition")  
Deprecated since version 6.4: Use [`IterMappingFiles()`](#tts.core.report.parser.Configuration.PrfTestConfiguration.IterMappingFiles "tts.core.report.parser.Configuration.PrfTestConfiguration.IterMappingFiles (Python method) — An iterator of all mapping files in the configuration")

Returns:  The first mapping file

Return type:  str | None

GetName()[¶](#tts.core.report.parser.Configuration.PrfTestConfiguration.GetName "Link to this definition")  
Returns:  The name of the TCF

Return type:  str

GetPath()[¶](#tts.core.report.parser.Configuration.PrfTestConfiguration.GetPath "Link to this definition")  
Returns:  The path of the TCF

Return type:  str

GetPkgDir()[¶](#tts.core.report.parser.Configuration.PrfTestConfiguration.GetPkgDir "Link to this definition")  
Returns:  The Package directory stored in the test configuration or the user-specific default Package directory if the test configuration does not define a Package directory

Return type:  str

GetTcfId()[¶](#tts.core.report.parser.Configuration.PrfTestConfiguration.GetTcfId "Link to this definition")  
Returns:  The ID of the TCF

Return type:  int

GetTeststand()[¶](#tts.core.report.parser.Configuration.PrfTestConfiguration.GetTeststand "Link to this definition")  
Returns:  The name of the computer the TCF was created with

Return type:  str

HasBusConfigurations()[¶](#tts.core.report.parser.Configuration.PrfTestConfiguration.HasBusConfigurations "Link to this definition")  
Returns:  True if the configuration has any bus configuration, otherwise False

Return type:  bool

HasConstFiles()[¶](#tts.core.report.parser.Configuration.PrfTestConfiguration.HasConstFiles "Link to this definition")  
Returns:  True if the configuration has any constant files, otherwise False

Return type:  bool

HasEcuConfigurations()[¶](#tts.core.report.parser.Configuration.PrfTestConfiguration.HasEcuConfigurations "Link to this definition")  
Returns:  True if the configuration has any ECU configuration, otherwise False

Return type:  bool

HasEfsConfigurations()[¶](#tts.core.report.parser.Configuration.PrfTestConfiguration.HasEfsConfigurations "Link to this definition")  
Returns:  True if the configuration has any electrical failure simulation configuration, otherwise False

Return type:  bool

HasFunctionConfigurations()[¶](#tts.core.report.parser.Configuration.PrfTestConfiguration.HasFunctionConfigurations "Link to this definition")  
Returns:  True if the configuration has any function configuration, otherwise False

Return type:  bool

HasModelConfigurations()[¶](#tts.core.report.parser.Configuration.PrfTestConfiguration.HasModelConfigurations "Link to this definition")  
Returns:  True if the configuration has any model configuration, otherwise False

Return type:  bool

IterBusConfigurations()[¶](#tts.core.report.parser.Configuration.PrfTestConfiguration.IterBusConfigurations "Link to this definition")  
Returns:  An iterator of all bus configurations

Return type:  Iterator[[`TcfBus`](#tts.core.report.db.TcfBus.TcfBus "tts.core.report.db.TcfBus.TcfBus (Python class) — The TcfBus represents information about a bus used within a test configuration.")]

IterConstFiles()[¶](#tts.core.report.parser.Configuration.PrfTestConfiguration.IterConstFiles "Link to this definition")  
Returns:  An iterator of all constant files in the configuration

Return type:  Iterator[str]

IterEcuConfigurations()[¶](#tts.core.report.parser.Configuration.PrfTestConfiguration.IterEcuConfigurations "Link to this definition")  
Returns:  An iterator of all ECU configurations

Return type:  Iterator[[`TcfEcu`](#tts.core.report.db.TcfEcu.TcfEcu "tts.core.report.db.TcfEcu.TcfEcu (Python class) — The TcfEcu represents information about an ECU used within a test configuration.")]

IterEfsConfigurations()[¶](#tts.core.report.parser.Configuration.PrfTestConfiguration.IterEfsConfigurations "Link to this definition")  
Returns:  An iterator of all electrical failure simulation configurations

Return type:  Iterator[[`TcfEfs`](#tts.core.report.db.TcfEfs.TcfEfs "tts.core.report.db.TcfEfs.TcfEfs (Python class) — The TcfEfs represents information about an electrical failure simulation used within a test configuration.")]

IterFunctionConfigurations()[¶](#tts.core.report.parser.Configuration.PrfTestConfiguration.IterFunctionConfigurations "Link to this definition")  
Returns:  An iterator of all function configurations

Return type:  Iterator[[`TcfFct`](#tts.core.report.db.TcfFct.TcfFct "tts.core.report.db.TcfFct.TcfFct (Python class) — The TcfFct represents information about a function used by a test configuration.")]

IterMappingFiles()[¶](#tts.core.report.parser.Configuration.PrfTestConfiguration.IterMappingFiles "Link to this definition")  
Returns:  An iterator of all mapping files in the configuration

Return type:  Iterator[str]

IterModelConfigurations()[¶](#tts.core.report.parser.Configuration.PrfTestConfiguration.IterModelConfigurations "Link to this definition")  
Returns:  An iterator of all model configurations

Return type:  Iterator[[`TcfModel`](#tts.core.report.db.TcfModel.TcfModel "tts.core.report.db.TcfModel.TcfModel (Python class) — The TcfModel represents information about a model used within a test configuration.")]

*class* TestBenchConfiguration[¶](#tts.core.report.parser.Configuration.TestBenchConfiguration "Link to this definition")  
The TestBenchConfiguration represents information about a test bench configuration.

PLibraryId[¶](#tts.core.report.parser.Configuration.TestBenchConfiguration.PLibraryId "Link to this definition")  
Returns:  The library ID of the Package

Return type:  str or None

GetId()[¶](#tts.core.report.parser.Configuration.TestBenchConfiguration.GetId "Link to this definition")  
Returns:  The ID of the tbc

Return type:  int

GetLibraryId()[¶](#tts.core.report.parser.Configuration.TestBenchConfiguration.GetLibraryId "Link to this definition")  
Returns:  The library ID of the Package

Return type:  str or None

GetName()[¶](#tts.core.report.parser.Configuration.TestBenchConfiguration.GetName "Link to this definition")  
Returns:  The name of the tbc

Return type:  str

GetPath()[¶](#tts.core.report.parser.Configuration.TestBenchConfiguration.GetPath "Link to this definition")  
Returns:  The path of the tbc

Return type:  str

GetTbcId()[¶](#tts.core.report.parser.Configuration.TestBenchConfiguration.GetTbcId "Link to this definition")  
Returns:  The ID of the tbc

Return type:  int

GetTools()[¶](#tts.core.report.parser.Configuration.TestBenchConfiguration.GetTools "Link to this definition")  
Returns:  A list of all tools used in the tbc

Return type:  list\<[`TbcTool`](#tts.core.report.db.TbcTool.TbcTool "tts.core.report.db.TbcTool.TbcTool (Python class) — The TbcTool represents information about a tool used within a test bench configuration.")\>

HasTools()[¶](#tts.core.report.parser.Configuration.TestBenchConfiguration.HasTools "Link to this definition")  
Returns:  True if the test bench configuration has any tools, otherwise False

Return type:  bool

IterTools()[¶](#tts.core.report.parser.Configuration.TestBenchConfiguration.IterTools "Link to this definition")  
Returns:  An iterator of all tools in the configuration

Return type:  Iterator[[`TbcTool`](#tts.core.report.db.TbcTool.TbcTool "tts.core.report.db.TbcTool.TbcTool (Python class) — The TbcTool represents information about a tool used within a test bench configuration.")]

*class* TestConfiguration[¶](#tts.core.report.parser.Configuration.TestConfiguration "Link to this definition")  
The Tcf represents information about a test configuration.

PLibraryId[¶](#tts.core.report.parser.Configuration.TestConfiguration.PLibraryId "Link to this definition")  
Returns:  The library ID of the Package

Return type:  str or None

GetDataDir()[¶](#tts.core.report.parser.Configuration.TestConfiguration.GetDataDir "Link to this definition")  
Returns:  The data directory stored in the test configuration or the user-specific default data directory if the test configuration does not define a data directory

Return type:  str

GetEditor()[¶](#tts.core.report.parser.Configuration.TestConfiguration.GetEditor "Link to this definition")  
Returns:  The editor of the TCF

Return type:  str

GetId()[¶](#tts.core.report.parser.Configuration.TestConfiguration.GetId "Link to this definition")  
Returns:  The ID of the TCF

Return type:  int

GetLibraryId()[¶](#tts.core.report.parser.Configuration.TestConfiguration.GetLibraryId "Link to this definition")  
Returns:  The library ID of the Package

Return type:  str or None

GetName()[¶](#tts.core.report.parser.Configuration.TestConfiguration.GetName "Link to this definition")  
Returns:  The name of the TCF

Return type:  str

GetPath()[¶](#tts.core.report.parser.Configuration.TestConfiguration.GetPath "Link to this definition")  
Returns:  The path of the TCF

Return type:  str

GetPkgDir()[¶](#tts.core.report.parser.Configuration.TestConfiguration.GetPkgDir "Link to this definition")  
Returns:  The Package directory stored in the test configuration or the user-specific default Package directory if the test configuration does not define a Package directory

Return type:  str

GetTcfId()[¶](#tts.core.report.parser.Configuration.TestConfiguration.GetTcfId "Link to this definition")  
Returns:  The ID of the TCF

Return type:  int

GetTeststand()[¶](#tts.core.report.parser.Configuration.TestConfiguration.GetTeststand "Link to this definition")  
Returns:  The name of the computer the TCF was created with

Return type:  str

*abstractmethod* HasBusConfigurations()[¶](#tts.core.report.parser.Configuration.TestConfiguration.HasBusConfigurations "Link to this definition")  
Returns:  True if the configuration has any bus configuration, otherwise False

Return type:  bool

*abstractmethod* HasConstFiles()[¶](#tts.core.report.parser.Configuration.TestConfiguration.HasConstFiles "Link to this definition")  
Returns:  True if the configuration has any constant files, otherwise False

Return type:  bool

*abstractmethod* HasEcuConfigurations()[¶](#tts.core.report.parser.Configuration.TestConfiguration.HasEcuConfigurations "Link to this definition")  
Returns:  True if the configuration has any ECU configuration, otherwise False

Return type:  bool

*abstractmethod* HasEfsConfigurations()[¶](#tts.core.report.parser.Configuration.TestConfiguration.HasEfsConfigurations "Link to this definition")  
Returns:  True if the configuration has any electrical failure simulation configuration, otherwise False

Return type:  bool

*abstractmethod* HasFunctionConfigurations()[¶](#tts.core.report.parser.Configuration.TestConfiguration.HasFunctionConfigurations "Link to this definition")  
Returns:  True if the configuration has any function configuration, otherwise False

Return type:  bool

*abstractmethod* HasModelConfigurations()[¶](#tts.core.report.parser.Configuration.TestConfiguration.HasModelConfigurations "Link to this definition")  
Returns:  True if the configuration has any model configuration, otherwise False

Return type:  bool

*abstractmethod* IterBusConfigurations()[¶](#tts.core.report.parser.Configuration.TestConfiguration.IterBusConfigurations "Link to this definition")  
Returns:  An iterator of all bus configurations

Return type:  Iterator[[`TcfBus`](#tts.core.report.db.TcfBus.TcfBus "tts.core.report.db.TcfBus.TcfBus (Python class) — The TcfBus represents information about a bus used within a test configuration.")]

*abstractmethod* IterConstFiles()[¶](#tts.core.report.parser.Configuration.TestConfiguration.IterConstFiles "Link to this definition")  
Returns:  An iterator of all constant files in the configuration

Return type:  Iterator[str]

*abstractmethod* IterEcuConfigurations()[¶](#tts.core.report.parser.Configuration.TestConfiguration.IterEcuConfigurations "Link to this definition")  
Returns:  An iterator of all ECU configurations

Return type:  Iterator[[`TcfEcu`](#tts.core.report.db.TcfEcu.TcfEcu "tts.core.report.db.TcfEcu.TcfEcu (Python class) — The TcfEcu represents information about an ECU used within a test configuration.")]

*abstractmethod* IterEfsConfigurations()[¶](#tts.core.report.parser.Configuration.TestConfiguration.IterEfsConfigurations "Link to this definition")  
Returns:  An iterator of all electrical failure simulation configurations

Return type:  Iterator[[`TcfEfs`](#tts.core.report.db.TcfEfs.TcfEfs "tts.core.report.db.TcfEfs.TcfEfs (Python class) — The TcfEfs represents information about an electrical failure simulation used within a test configuration.")]

*abstractmethod* IterFunctionConfigurations()[¶](#tts.core.report.parser.Configuration.TestConfiguration.IterFunctionConfigurations "Link to this definition")  
Returns:  An iterator of all function configurations

Return type:  Iterator[[`TcfFct`](#tts.core.report.db.TcfFct.TcfFct "tts.core.report.db.TcfFct.TcfFct (Python class) — The TcfFct represents information about a function used by a test configuration.")]

*abstractmethod* IterMappingFiles()[¶](#tts.core.report.parser.Configuration.TestConfiguration.IterMappingFiles "Link to this definition")  
Returns:  An iterator of all mapping files in the configuration

Return type:  Iterator[str]

*abstractmethod* IterModelConfigurations()[¶](#tts.core.report.parser.Configuration.TestConfiguration.IterModelConfigurations "Link to this definition")  
Returns:  An iterator of all model configurations

Return type:  Iterator[[`TcfModel`](#tts.core.report.db.TcfModel.TcfModel "tts.core.report.db.TcfModel.TcfModel (Python class) — The TcfModel represents information about a model used within a test configuration.")]

*class* TrfTestBenchConfiguration[¶](#tts.core.report.parser.Configuration.TrfTestBenchConfiguration "Link to this definition")  

PLibraryId[¶](#tts.core.report.parser.Configuration.TrfTestBenchConfiguration.PLibraryId "Link to this definition")  
Returns:  The library ID of the Package

Return type:  str or None

GetId()[¶](#tts.core.report.parser.Configuration.TrfTestBenchConfiguration.GetId "Link to this definition")  
Returns:  The ID of the tbc

Return type:  int

GetLibraryId()[¶](#tts.core.report.parser.Configuration.TrfTestBenchConfiguration.GetLibraryId "Link to this definition")  
Returns:  The library ID of the Package

Return type:  str or None

GetName()[¶](#tts.core.report.parser.Configuration.TrfTestBenchConfiguration.GetName "Link to this definition")  
Returns:  The name of the tbc

Return type:  str

GetPath()[¶](#tts.core.report.parser.Configuration.TrfTestBenchConfiguration.GetPath "Link to this definition")  
Returns:  The path of the tbc

Return type:  str

GetTbcId()[¶](#tts.core.report.parser.Configuration.TrfTestBenchConfiguration.GetTbcId "Link to this definition")  
Returns:  The ID of the tbc

Return type:  int

GetTools()[¶](#tts.core.report.parser.Configuration.TrfTestBenchConfiguration.GetTools "Link to this definition")  
Returns:  A list of all tools used in the tbc

Return type:  list\<[`TbcTool`](#tts.core.report.db.TbcTool.TbcTool "tts.core.report.db.TbcTool.TbcTool (Python class) — The TbcTool represents information about a tool used within a test bench configuration.")\>

HasTools()[¶](#tts.core.report.parser.Configuration.TrfTestBenchConfiguration.HasTools "Link to this definition")  
Returns:  True if the test bench configuration has any tools, otherwise False

Return type:  bool

IterTools()[¶](#tts.core.report.parser.Configuration.TrfTestBenchConfiguration.IterTools "Link to this definition")  
Returns:  An iterator of all tools in the configuration

Return type:  Iterator[[`TbcTool`](#tts.core.report.db.TbcTool.TbcTool "tts.core.report.db.TbcTool.TbcTool (Python class) — The TbcTool represents information about a tool used within a test bench configuration.")]

*class* TrfTestConfiguration[¶](#tts.core.report.parser.Configuration.TrfTestConfiguration "Link to this definition")  

PLibraryId[¶](#tts.core.report.parser.Configuration.TrfTestConfiguration.PLibraryId "Link to this definition")  
Returns:  The library ID of the Package

Return type:  str or None

GetDataDir()[¶](#tts.core.report.parser.Configuration.TrfTestConfiguration.GetDataDir "Link to this definition")  
Returns:  The data directory stored in the test configuration or the user-specific default data directory if the test configuration does not define a data directory

Return type:  str

GetEditor()[¶](#tts.core.report.parser.Configuration.TrfTestConfiguration.GetEditor "Link to this definition")  
Returns:  The editor of the TCF

Return type:  str

GetId()[¶](#tts.core.report.parser.Configuration.TrfTestConfiguration.GetId "Link to this definition")  
Returns:  The ID of the TCF

Return type:  int

GetLibraryId()[¶](#tts.core.report.parser.Configuration.TrfTestConfiguration.GetLibraryId "Link to this definition")  
Returns:  The library ID of the Package

Return type:  str or None

GetMappingFile()[¶](#tts.core.report.parser.Configuration.TrfTestConfiguration.GetMappingFile "Link to this definition")  
Deprecated since version 6.4: Use [`IterMappingFiles()`](#tts.core.report.parser.Configuration.TrfTestConfiguration.IterMappingFiles "tts.core.report.parser.Configuration.TrfTestConfiguration.IterMappingFiles (Python method) — An iterator of all mapping files in the configuration")

Returns:  The first mapping file

Return type:  str | None

GetName()[¶](#tts.core.report.parser.Configuration.TrfTestConfiguration.GetName "Link to this definition")  
Returns:  The name of the TCF

Return type:  str

GetPath()[¶](#tts.core.report.parser.Configuration.TrfTestConfiguration.GetPath "Link to this definition")  
Returns:  The path of the TCF

Return type:  str

GetPkgDir()[¶](#tts.core.report.parser.Configuration.TrfTestConfiguration.GetPkgDir "Link to this definition")  
Returns:  The Package directory stored in the test configuration or the user-specific default Package directory if the test configuration does not define a Package directory

Return type:  str

GetTcfId()[¶](#tts.core.report.parser.Configuration.TrfTestConfiguration.GetTcfId "Link to this definition")  
Returns:  The ID of the TCF

Return type:  int

GetTeststand()[¶](#tts.core.report.parser.Configuration.TrfTestConfiguration.GetTeststand "Link to this definition")  
Returns:  The name of the computer the TCF was created with

Return type:  str

HasBusConfigurations()[¶](#tts.core.report.parser.Configuration.TrfTestConfiguration.HasBusConfigurations "Link to this definition")  
Returns:  True if the configuration has any bus configuration, otherwise False

Return type:  bool

HasConstFiles()[¶](#tts.core.report.parser.Configuration.TrfTestConfiguration.HasConstFiles "Link to this definition")  
Returns:  True if the configuration has any constant files, otherwise False

Return type:  bool

HasEcuConfigurations()[¶](#tts.core.report.parser.Configuration.TrfTestConfiguration.HasEcuConfigurations "Link to this definition")  
Returns:  True if the configuration has any ECU configuration, otherwise False

Return type:  bool

HasEfsConfigurations()[¶](#tts.core.report.parser.Configuration.TrfTestConfiguration.HasEfsConfigurations "Link to this definition")  
Returns:  True if the configuration has any electrical failure simulation configuration, otherwise False

Return type:  bool

HasFunctionConfigurations()[¶](#tts.core.report.parser.Configuration.TrfTestConfiguration.HasFunctionConfigurations "Link to this definition")  
Returns:  True if the configuration has any function configuration, otherwise False

Return type:  bool

HasModelConfigurations()[¶](#tts.core.report.parser.Configuration.TrfTestConfiguration.HasModelConfigurations "Link to this definition")  
Returns:  True if the configuration has any model configuration, otherwise False

Return type:  bool

IterBusConfigurations()[¶](#tts.core.report.parser.Configuration.TrfTestConfiguration.IterBusConfigurations "Link to this definition")  
Returns:  An iterator of all bus configurations

Return type:  Iterator[[`TcfBus`](#tts.core.report.db.TcfBus.TcfBus "tts.core.report.db.TcfBus.TcfBus (Python class) — The TcfBus represents information about a bus used within a test configuration.")]

IterConstFiles()[¶](#tts.core.report.parser.Configuration.TrfTestConfiguration.IterConstFiles "Link to this definition")  
Returns:  An iterator of all constant files in the configuration

Return type:  Iterator[str]

IterEcuConfigurations()[¶](#tts.core.report.parser.Configuration.TrfTestConfiguration.IterEcuConfigurations "Link to this definition")  
Returns:  An iterator of all ECU configurations

Return type:  Iterator[[`TcfEcu`](#tts.core.report.db.TcfEcu.TcfEcu "tts.core.report.db.TcfEcu.TcfEcu (Python class) — The TcfEcu represents information about an ECU used within a test configuration.")]

IterEfsConfigurations()[¶](#tts.core.report.parser.Configuration.TrfTestConfiguration.IterEfsConfigurations "Link to this definition")  
Returns:  An iterator of all electrical failure simulation configurations

Return type:  Iterator[[`TcfEfs`](#tts.core.report.db.TcfEfs.TcfEfs "tts.core.report.db.TcfEfs.TcfEfs (Python class) — The TcfEfs represents information about an electrical failure simulation used within a test configuration.")]

IterFunctionConfigurations()[¶](#tts.core.report.parser.Configuration.TrfTestConfiguration.IterFunctionConfigurations "Link to this definition")  
Returns:  An iterator of all function configurations

Return type:  Iterator[[`TcfFct`](#tts.core.report.db.TcfFct.TcfFct "tts.core.report.db.TcfFct.TcfFct (Python class) — The TcfFct represents information about a function used by a test configuration.")]

IterMappingFiles()[¶](#tts.core.report.parser.Configuration.TrfTestConfiguration.IterMappingFiles "Link to this definition")  
Returns:  An iterator of all mapping files in the configuration

Return type:  Iterator[str]

IterModelConfigurations()[¶](#tts.core.report.parser.Configuration.TrfTestConfiguration.IterModelConfigurations "Link to this definition")  
Returns:  An iterator of all model configurations

Return type:  Iterator[[`TcfModel`](#tts.core.report.db.TcfModel.TcfModel "tts.core.report.db.TcfModel.TcfModel (Python class) — The TcfModel represents information about a model used within a test configuration.")]

*class* TcfBus[¶](#tts.core.report.db.TcfBus.TcfBus "Link to this definition")  
The TcfBus represents information about a bus used within a test configuration.

GetDbPath()[¶](#tts.core.report.db.TcfBus.TcfBus.GetDbPath "Link to this definition")  
Returns:  The path to the bus database

Return type:  str

GetFbxChn()[¶](#tts.core.report.db.TcfBus.TcfBus.GetFbxChn "Link to this definition")  
Returns:  The fibex channel

Return type:  str or None

GetId()[¶](#tts.core.report.db.TcfBus.TcfBus.GetId "Link to this definition")  
Returns:  The ID of the bus

Return type:  str

GetTcfBusId()[¶](#tts.core.report.db.TcfBus.TcfBus.GetTcfBusId "Link to this definition")  
Returns:  The ID of the bus

Return type:  int

GetTcfId()[¶](#tts.core.report.db.TcfBus.TcfBus.GetTcfId "Link to this definition")  
Returns:  The ID of the TCF

Return type:  int

*class* TcfEcu[¶](#tts.core.report.db.TcfEcu.TcfEcu "Link to this definition")  
The TcfEcu represents information about an ECU used within a test configuration.

PDiagHSFZSettings[¶](#tts.core.report.db.TcfEcu.TcfEcu.PDiagHSFZSettings "Link to this definition")  
Returns:  The HSFZ settings as string

Return type:  str or None

GetA2lFile()[¶](#tts.core.report.db.TcfEcu.TcfEcu.GetA2lFile "Link to this definition")  
Returns:  The path to the A2L file

Return type:  str or None

GetDebugHex()[¶](#tts.core.report.db.TcfEcu.TcfEcu.GetDebugHex "Link to this definition")  
Returns:  The path to the HEX file

Return type:  str or None

GetDiagDoIpSettings()[¶](#tts.core.report.db.TcfEcu.TcfEcu.GetDiagDoIpSettings "Link to this definition")  
Returns:  The DoIp settings as string

Return type:  str or None

GetDiagDoSoAdSettings()[¶](#tts.core.report.db.TcfEcu.TcfEcu.GetDiagDoSoAdSettings "Link to this definition")  
Returns:  The DoSoAd settings as string

Return type:  str or None

GetDiagFrTpSettings()[¶](#tts.core.report.db.TcfEcu.TcfEcu.GetDiagFrTpSettings "Link to this definition")  
Returns:  The FrTp settings as string

Return type:  str or None

GetDiagHSFZSettings()[¶](#tts.core.report.db.TcfEcu.TcfEcu.GetDiagHSFZSettings "Link to this definition")  
Returns:  The HSFZ settings as string

Return type:  str or None

GetDiagIsoTpSettings()[¶](#tts.core.report.db.TcfEcu.TcfEcu.GetDiagIsoTpSettings "Link to this definition")  
Returns:  The IsoTp settings as string

Return type:  str or None

GetDiagPort()[¶](#tts.core.report.db.TcfEcu.TcfEcu.GetDiagPort "Link to this definition")  
Returns:  The name of the DiagPort

Return type:  str or None

GetDiagUDSSettings()[¶](#tts.core.report.db.TcfEcu.TcfEcu.GetDiagUDSSettings "Link to this definition")  
Returns:  The UDS settings as string

Return type:  str or None

GetDiagnosticDb()[¶](#tts.core.report.db.TcfEcu.TcfEcu.GetDiagnosticDb "Link to this definition")  
Returns:  The path to the diagnostic db

Return type:  str or None

GetElf()[¶](#tts.core.report.db.TcfEcu.TcfEcu.GetElf "Link to this definition")  
Raises:  
~tt.Error

Returns:  The path to the Elf file

Return type:  str or None

GetElfs()[¶](#tts.core.report.db.TcfEcu.TcfEcu.GetElfs "Link to this definition")  
Returns:  A string of all paths to the Elf files seperated by ‘;’

Return type:  str or None

GetHexFile()[¶](#tts.core.report.db.TcfEcu.TcfEcu.GetHexFile "Link to this definition")  
Returns:  The path to the HEX file

Return type:  str or None

GetId()[¶](#tts.core.report.db.TcfEcu.TcfEcu.GetId "Link to this definition")  
Returns:  The ID of the ECU

Return type:  str

GetLogDatabase()[¶](#tts.core.report.db.TcfEcu.TcfEcu.GetLogDatabase "Link to this definition")  
Returns:  The path to the log database

Return type:  str or None

GetLogFilterFile()[¶](#tts.core.report.db.TcfEcu.TcfEcu.GetLogFilterFile "Link to this definition")  
Returns:  The path to the log filter file

Return type:  str or None

GetLogilink()[¶](#tts.core.report.db.TcfEcu.TcfEcu.GetLogilink "Link to this definition")  
Returns:  The path to the Logilink file

Return type:  str or None

GetSgbd()[¶](#tts.core.report.db.TcfEcu.TcfEcu.GetSgbd "Link to this definition")  
Returns:  The path to the SGBD file

Return type:  str or None

GetSgbdVersion()[¶](#tts.core.report.db.TcfEcu.TcfEcu.GetSgbdVersion "Link to this definition")  
Gets the SGBD version. If the SGBD is unspecified, a string containing “unknown” is returned.

Returns:  A string containing the SGBD version or “unknown”.

Return type:  str

GetTcfEcuId()[¶](#tts.core.report.db.TcfEcu.TcfEcu.GetTcfEcuId "Link to this definition")  
Returns:  The ID of the ECU

Return type:  str

GetTcfId()[¶](#tts.core.report.db.TcfEcu.TcfEcu.GetTcfId "Link to this definition")  
Returns:  The ID of the TCF

Return type:  int

*class* TcfEfs[¶](#tts.core.report.db.TcfEfs.TcfEfs "Link to this definition")  
The TcfEfs represents information about an electrical failure simulation used within a test configuration.

GetDb()[¶](#tts.core.report.db.TcfEfs.TcfEfs.GetDb "Link to this definition")  
Returns:  The path to the database

Return type:  str

GetId()[¶](#tts.core.report.db.TcfEfs.TcfEfs.GetId "Link to this definition")  
Returns:  The ID of the EFS

Return type:  str

GetTcfEfsId()[¶](#tts.core.report.db.TcfEfs.TcfEfs.GetTcfEfsId "Link to this definition")  
Returns:  The ID of the EFS

Return type:  str

GetTcfId()[¶](#tts.core.report.db.TcfEfs.TcfEfs.GetTcfId "Link to this definition")  
Returns:  The ID of the TCF

Return type:  int

*class* TcfExecution[¶](#tts.core.report.db.TcfExecution.TcfExecution "Link to this definition")  
The TcfExecution represents information about the execution configuration of a test configuration.

GetSimulationMode()[¶](#tts.core.report.db.TcfExecution.TcfExecution.GetSimulationMode "Link to this definition")  
Returns:  The simulation mode

Return type:  str

GetTcfId()[¶](#tts.core.report.db.TcfExecution.TcfExecution.GetTcfId "Link to this definition")  
Returns:  The ID of the TCF

Return type:  int

GetWaitAfterTeststep()[¶](#tts.core.report.db.TcfExecution.TcfExecution.GetWaitAfterTeststep "Link to this definition")  
Returns:  The wait time after a test step

Return type:  float

*class* TcfFct[¶](#tts.core.report.db.TcfFct.TcfFct "Link to this definition")  
The TcfFct represents information about a function used by a test configuration.

GetCatalog()[¶](#tts.core.report.db.TcfFct.TcfFct.GetCatalog "Link to this definition")  
Returns:  The catalog

Return type:  str

GetId()[¶](#tts.core.report.db.TcfFct.TcfFct.GetId "Link to this definition")  
Returns:  The ID of the Fct

Return type:  str

GetTcfFctId()[¶](#tts.core.report.db.TcfFct.TcfFct.GetTcfFctId "Link to this definition")  
Returns:  The ID of the Fct

Return type:  str

GetTcfId()[¶](#tts.core.report.db.TcfFct.TcfFct.GetTcfId "Link to this definition")  
Returns:  The ID of the TCF

Return type:  int

*class* TcfModel[¶](#tts.core.report.db.TcfModel.TcfModel "Link to this definition")  
The TcfModel represents information about a model used within a test configuration.

GetId()[¶](#tts.core.report.db.TcfModel.TcfModel.GetId "Link to this definition")  
Returns:  The textual ID of the model

Return type:  str

GetModel()[¶](#tts.core.report.db.TcfModel.TcfModel.GetModel "Link to this definition")  
Returns:  The path to the model

Return type:  str

GetTcfId()[¶](#tts.core.report.db.TcfModel.TcfModel.GetTcfId "Link to this definition")  
Returns:  The numeric ID of the TCF

Return type:  int

GetTcfModelId()[¶](#tts.core.report.db.TcfModel.TcfModel.GetTcfModelId "Link to this definition")  
Returns:  The textual ID of the model

Return type:  str

GetTimebase()[¶](#tts.core.report.db.TcfModel.TcfModel.GetTimebase "Link to this definition")  
Returns:  True if Port is set as timebase, otherwise False

Return type:  bool

GetVersion()[¶](#tts.core.report.db.TcfModel.TcfModel.GetVersion "Link to this definition")  
Returns:  The version of the model

Return type:  str

*class* TbcTool[¶](#tts.core.report.db.TbcTool.TbcTool "Link to this definition")  
The TbcTool represents information about a tool used within a test bench configuration.

GetLocation()[¶](#tts.core.report.db.TbcTool.TbcTool.GetLocation "Link to this definition")  
Returns:  The location of the tool

Return type:  str

GetName()[¶](#tts.core.report.db.TbcTool.TbcTool.GetName "Link to this definition")  
Returns:  The name of the tool

Return type:  str

GetPatches()[¶](#tts.core.report.db.TbcTool.TbcTool.GetPatches "Link to this definition")  
Returns:  The patches of the tool

Return type:  str

GetStatus()[¶](#tts.core.report.db.TbcTool.TbcTool.GetStatus "Link to this definition")  
Returns:  The status of the tool

Return type:  str

GetTbcId()[¶](#tts.core.report.db.TbcTool.TbcTool.GetTbcId "Link to this definition")  
Returns:  The ID of the TBC

Return type:  int

GetTbcToolId()[¶](#tts.core.report.db.TbcTool.TbcTool.GetTbcToolId "Link to this definition")  
Returns:  The ID of the tool

Return type:  str

GetVersion()[¶](#tts.core.report.db.TbcTool.TbcTool.GetVersion "Link to this definition")  
Returns:  The version of the tool

Return type:  str

## Constant[¶](#constant "Link to this heading")

*class* Constant[¶](#tts.core.report.db.Constant.Constant "Link to this definition")  
Represents a global constant.

GetDescription()[¶](#tts.core.report.db.Constant.Constant.GetDescription "Link to this definition")  
Returns:  The description of the global constant

Return type:  str

GetName()[¶](#tts.core.report.db.Constant.Constant.GetName "Link to this definition")  
Returns:  The name of the global constant

Return type:  str

GetOrigin()[¶](#tts.core.report.db.Constant.Constant.GetOrigin "Link to this definition")  
Returns:  The origin of the global constant

Return type:  str

GetValue()[¶](#tts.core.report.db.Constant.Constant.GetValue "Link to this definition")  
Returns:  The string representation of the value of the global constant

Return type:  str

## Entities[¶](#entities "Link to this heading")

*class* Entity[¶](#tts.core.report.db.Entity.Entity "Link to this definition")  
GetEntityId()[¶](#tts.core.report.db.Entity.Entity.GetEntityId "Link to this definition")  
Returns:  The ID of the entity

Return type:  int

GetId()[¶](#tts.core.report.db.Entity.Entity.GetId "Link to this definition")  
Returns:  The ID of the entity

Return type:  int

GetName()[¶](#tts.core.report.db.Entity.Entity.GetName "Link to this definition")  
Returns:  The name of the entity

Return type:  str

GetReportItemId()[¶](#tts.core.report.db.Entity.Entity.GetReportItemId "Link to this definition")  
Returns:  The ID of the associated [`ReportItem`](#tts.core.report.db.ReportItem.ReportItem "tts.core.report.db.ReportItem.ReportItem (Python class) — A report item represents the execution results of one test step. It contains information like test step number, time of execution, type of test step and custom fields. Furthermore additional information on a test step can be stored in so called entity elements being attached to the respective report item (e.g. TableEntity or TextEntity).")

Return type:  int

GetType()[¶](#tts.core.report.db.Entity.Entity.GetType "Link to this definition")  
Returns the type name of the entity.

Returns:  The type name of the entity

Return type:  str

*class* ImageEntity[¶](#tts.core.report.db.ImageEntity.ImageEntity "Link to this definition")  
Represents an image.

GetData()[¶](#tts.core.report.db.ImageEntity.ImageEntity.GetData "Link to this definition")  
Returns:  Data bytes of the image. Can be None if the image is not embedded in the report and was not found!

Return type:  bytes or None

GetEntityId()[¶](#tts.core.report.db.ImageEntity.ImageEntity.GetEntityId "Link to this definition")  
Returns:  The ID of the entity

Return type:  int

GetId()[¶](#tts.core.report.db.ImageEntity.ImageEntity.GetId "Link to this definition")  
Returns:  The ID of the entity

Return type:  int

GetImage()[¶](#tts.core.report.db.ImageEntity.ImageEntity.GetImage "Link to this definition")  
Returns:  The image

Return type:  [`Image`](#tts.core.report.db.Image.Image "tts.core.report.db.Image.Image (Python class) — Represents a ReportItem-Image.")

GetName()[¶](#tts.core.report.db.ImageEntity.ImageEntity.GetName "Link to this definition")  
Returns:  The name of the entity

Return type:  str

GetReportItemId()[¶](#tts.core.report.db.ImageEntity.ImageEntity.GetReportItemId "Link to this definition")  
Returns:  The ID of the associated [`ReportItem`](#tts.core.report.db.ReportItem.ReportItem "tts.core.report.db.ReportItem.ReportItem (Python class) — A report item represents the execution results of one test step. It contains information like test step number, time of execution, type of test step and custom fields. Furthermore additional information on a test step can be stored in so called entity elements being attached to the respective report item (e.g. TableEntity or TextEntity).")

Return type:  int

GetType()[¶](#tts.core.report.db.ImageEntity.ImageEntity.GetType "Link to this definition")  
Returns the type name of the entity.

Returns:  The type name of the entity

Return type:  str

ToFile(*[path](#tts.core.report.db.ImageEntity.ImageEntity.ToFile.path "tts.core.report.db.ImageEntity.ImageEntity.ToFile.path (Python parameter) — path to the directory in which the image should be saved")=`'.'`*)[¶](#tts.core.report.db.ImageEntity.ImageEntity.ToFile "Link to this definition")  
Saves the image to the given directory.

Parameters:  path : str[¶](#tts.core.report.db.ImageEntity.ImageEntity.ToFile.path "Permalink to this definition")  
path to the directory in which the image should be saved

Raises:  
**ValueError** – Image is not embedded in the report and was not found on file system.

Returns:  Path to the saved image

Return type:  str

*class* ImageExpectationEntity[¶](#tts.core.report.db.ImageExpectationEntity.ImageExpectationEntity "Link to this definition")  
Represents an image expectation.

GetActualImage()[¶](#tts.core.report.db.ImageExpectationEntity.ImageExpectationEntity.GetActualImage "Link to this definition")  
Returns:  The actual image

Return type:  [`Image`](#tts.core.report.db.Image.Image "tts.core.report.db.Image.Image (Python class) — Represents a ReportItem-Image.")

GetEntityId()[¶](#tts.core.report.db.ImageExpectationEntity.ImageExpectationEntity.GetEntityId "Link to this definition")  
Returns:  The ID of the entity

Return type:  int

GetExpectedImage()[¶](#tts.core.report.db.ImageExpectationEntity.ImageExpectationEntity.GetExpectedImage "Link to this definition")  
Returns:  The expected image

Return type:  [`Image`](#tts.core.report.db.Image.Image "tts.core.report.db.Image.Image (Python class) — Represents a ReportItem-Image.")

GetId()[¶](#tts.core.report.db.ImageExpectationEntity.ImageExpectationEntity.GetId "Link to this definition")  
Returns:  The ID of the entity

Return type:  int

GetName()[¶](#tts.core.report.db.ImageExpectationEntity.ImageExpectationEntity.GetName "Link to this definition")  
Returns:  The name of the entity

Return type:  str

GetReportItemId()[¶](#tts.core.report.db.ImageExpectationEntity.ImageExpectationEntity.GetReportItemId "Link to this definition")  
Returns:  The ID of the associated [`ReportItem`](#tts.core.report.db.ReportItem.ReportItem "tts.core.report.db.ReportItem.ReportItem (Python class) — A report item represents the execution results of one test step. It contains information like test step number, time of execution, type of test step and custom fields. Furthermore additional information on a test step can be stored in so called entity elements being attached to the respective report item (e.g. TableEntity or TextEntity).")

Return type:  int

GetType()[¶](#tts.core.report.db.ImageExpectationEntity.ImageExpectationEntity.GetType "Link to this definition")  
Returns the type name of the entity.

Returns:  The type name of the entity

Return type:  str

*class* RecordingInfosEntity[¶](#tts.core.report.parser.Package.RecordingInfosEntity "Link to this definition")  
The RecordingInfosEntity represents a table of recording infos (RecordingEntity).

GetCount()[¶](#tts.core.report.parser.Package.RecordingInfosEntity.GetCount "Link to this definition")  
Returns:  The number of entries

Return type:  int

GetEntityId()[¶](#tts.core.report.parser.Package.RecordingInfosEntity.GetEntityId "Link to this definition")  
Returns:  The ID of the entity

Return type:  int

GetId()[¶](#tts.core.report.parser.Package.RecordingInfosEntity.GetId "Link to this definition")  
Returns:  The ID of the entity

Return type:  int

GetName()[¶](#tts.core.report.parser.Package.RecordingInfosEntity.GetName "Link to this definition")  
Returns:  The name of the entity

Return type:  str

GetRecording(*[index](#tts.core.report.parser.Package.RecordingInfosEntity.GetRecording "tts.core.report.parser.Package.RecordingInfosEntity.GetRecording.index (Python parameter)")*)[¶](#tts.core.report.parser.Package.RecordingInfosEntity.GetRecording "Link to this definition")  
Returns:  The referenced recording

Return type:  [`Recording`](#tts.core.report.parser.Package.Recording "tts.core.report.parser.Package.Recording (Python class) — Represents a recording.")

GetRecordingId(*[index](#tts.core.report.parser.Package.RecordingInfosEntity.GetRecordingId.index "tts.core.report.parser.Package.RecordingInfosEntity.GetRecordingId.index (Python parameter)")*)[¶](#tts.core.report.parser.Package.RecordingInfosEntity.GetRecordingId "Link to this definition")  
Parameters:  index : int[¶](#tts.core.report.parser.Package.RecordingInfosEntity.GetRecordingId.index "Permalink to this definition")  

Returns:  The ID of the recording at the given index

Return type:  int

GetReportItemId()[¶](#tts.core.report.parser.Package.RecordingInfosEntity.GetReportItemId "Link to this definition")  
Returns:  The ID of the associated [`ReportItem`](#tts.core.report.db.ReportItem.ReportItem "tts.core.report.db.ReportItem.ReportItem (Python class) — A report item represents the execution results of one test step. It contains information like test step number, time of execution, type of test step and custom fields. Furthermore additional information on a test step can be stored in so called entity elements being attached to the respective report item (e.g. TableEntity or TextEntity).")

Return type:  int

GetStartTime(*[index](#tts.core.report.parser.Package.RecordingInfosEntity.GetStartTime.index "tts.core.report.parser.Package.RecordingInfosEntity.GetStartTime.index (Python parameter)")*)[¶](#tts.core.report.parser.Package.RecordingInfosEntity.GetStartTime "Link to this definition")  
Returns the first timestamp (of the original time axis) from which samples are read. Samples before this point will be skipped.

Parameters:  index : int[¶](#tts.core.report.parser.Package.RecordingInfosEntity.GetStartTime.index "Permalink to this definition")  

Returns:  The start time

Return type:  float

GetStopTime(*[index](#tts.core.report.parser.Package.RecordingInfosEntity.GetStopTime.index "tts.core.report.parser.Package.RecordingInfosEntity.GetStopTime.index (Python parameter)")*)[¶](#tts.core.report.parser.Package.RecordingInfosEntity.GetStopTime "Link to this definition")  
Returns the last timestamp (of the original time axis) up to which samples are read. Samples after this point will be skipped.

Parameters:  index : int[¶](#tts.core.report.parser.Package.RecordingInfosEntity.GetStopTime.index "Permalink to this definition")  

Returns:  The stop time

Return type:  float

GetSyncDeltaT(*[index](#tts.core.report.parser.Package.RecordingInfosEntity.GetSyncDeltaT.index "tts.core.report.parser.Package.RecordingInfosEntity.GetSyncDeltaT.index (Python parameter)")*)[¶](#tts.core.report.parser.Package.RecordingInfosEntity.GetSyncDeltaT "Link to this definition")  
Parameters:  index : int[¶](#tts.core.report.parser.Package.RecordingInfosEntity.GetSyncDeltaT.index "Permalink to this definition")  

Returns:  The time offset deltaT that is applied to the time axis. Defaults to None if no synchronization was executed.

Return type:  float or None

GetType()[¶](#tts.core.report.parser.Package.RecordingInfosEntity.GetType "Link to this definition")  
Returns the type name of the entity.

Returns:  The type name of the entity

Return type:  str

*class* ProjectElementStatistic[¶](#tts.core.report.parser.ProjectElement.ProjectElementStatistic "Link to this definition")  
Represents the project element statistic.

GetCountAndPercentageOfResultItem(*[item](#tts.core.report.parser.ProjectElement.ProjectElementStatistic.GetCountAndPercentageOfResultItem.item "tts.core.report.parser.ProjectElement.ProjectElementStatistic.GetCountAndPercentageOfResultItem.item (Python parameter) — The result for which the count and percentage shall be returned, e.g. tts.core.common.Constants.RESULT_ERROR")*)[¶](#tts.core.report.parser.ProjectElement.ProjectElementStatistic.GetCountAndPercentageOfResultItem "Link to this definition")  
Gets the absolute count and percentage of Packages that have the specified result. If no Package has the given result, a tuple containing (0, 0.0) is returned.

Parameters:  item : str[¶](#tts.core.report.parser.ProjectElement.ProjectElementStatistic.GetCountAndPercentageOfResultItem.item "Permalink to this definition")  
The result for which the count and percentage shall be returned, e.g. tts.core.common.Constants.RESULT_ERROR

Returns:  Tuple consisting of the count and the percentage

Return type:  tuple[int, float]

GetCountOfResultItem(*[item](#tts.core.report.parser.ProjectElement.ProjectElementStatistic.GetCountOfResultItem.item "tts.core.report.parser.ProjectElement.ProjectElementStatistic.GetCountOfResultItem.item (Python parameter) — The result for which the count shall be returned, e.g. tts.core.common.Constants.RESULT_ERROR")*)[¶](#tts.core.report.parser.ProjectElement.ProjectElementStatistic.GetCountOfResultItem "Link to this definition")  
Parameters:  item : str[¶](#tts.core.report.parser.ProjectElement.ProjectElementStatistic.GetCountOfResultItem.item "Permalink to this definition")  
The result for which the count shall be returned, e.g. tts.core.common.Constants.RESULT_ERROR

Returns:  The absolute count of Packages that have the specified result

Return type:  int

GetEntityId()[¶](#tts.core.report.parser.ProjectElement.ProjectElementStatistic.GetEntityId "Link to this definition")  
Returns:  The ID of the entity

Return type:  int

GetErrorCount()[¶](#tts.core.report.parser.ProjectElement.ProjectElementStatistic.GetErrorCount "Link to this definition")  
Returns:  The count of all project elements with the result ‘ERROR’

Return type:  int

GetFailedCount()[¶](#tts.core.report.parser.ProjectElement.ProjectElementStatistic.GetFailedCount "Link to this definition")  
Returns:  The count of all project elements with the result ‘FAILED’

Return type:  int

GetHeader()[¶](#tts.core.report.parser.ProjectElement.ProjectElementStatistic.GetHeader "Link to this definition")  
Returns:  The header (first element of each column)

Return type:  list\<str\>

GetId()[¶](#tts.core.report.parser.ProjectElement.ProjectElementStatistic.GetId "Link to this definition")  
Returns:  The ID of the entity

Return type:  int

GetInconCount()[¶](#tts.core.report.parser.ProjectElement.ProjectElementStatistic.GetInconCount "Link to this definition")  
Returns:  The count of all project elements with the result ‘INCONCLUSIVE’

Return type:  int

GetName()[¶](#tts.core.report.parser.ProjectElement.ProjectElementStatistic.GetName "Link to this definition")  
Returns:  The name of the entity

Return type:  str

GetNoneCount()[¶](#tts.core.report.parser.ProjectElement.ProjectElementStatistic.GetNoneCount "Link to this definition")  
Returns:  The count of all project elements with the result ‘NONE’

Return type:  int

GetNumberCols()[¶](#tts.core.report.parser.ProjectElement.ProjectElementStatistic.GetNumberCols "Link to this definition")  
Returns:  The number of columns

Return type:  int

GetNumberRows()[¶](#tts.core.report.parser.ProjectElement.ProjectElementStatistic.GetNumberRows "Link to this definition")  
Returns:  The number of rows

Return type:  int

GetPercentageOfResultItem(*[item](#tts.core.report.parser.ProjectElement.ProjectElementStatistic.GetPercentageOfResultItem.item "tts.core.report.parser.ProjectElement.ProjectElementStatistic.GetPercentageOfResultItem.item (Python parameter) — The result for which the precentage shall be returned, e.g. tts.core.common.Constants.RESULT_ERROR")*)[¶](#tts.core.report.parser.ProjectElement.ProjectElementStatistic.GetPercentageOfResultItem "Link to this definition")  
Gets the percentage of Packages that have the specified result.

Parameters:  item : str[¶](#tts.core.report.parser.ProjectElement.ProjectElementStatistic.GetPercentageOfResultItem.item "Permalink to this definition")  
The result for which the precentage shall be returned, e.g. tts.core.common.Constants.RESULT_ERROR

Returns:  The percentage of Packages that have the specified result

Return type:  float

GetReportItemId()[¶](#tts.core.report.parser.ProjectElement.ProjectElementStatistic.GetReportItemId "Link to this definition")  
Returns:  The ID of the associated [`ReportItem`](#tts.core.report.db.ReportItem.ReportItem "tts.core.report.db.ReportItem.ReportItem (Python class) — A report item represents the execution results of one test step. It contains information like test step number, time of execution, type of test step and custom fields. Furthermore additional information on a test step can be stored in so called entity elements being attached to the respective report item (e.g. TableEntity or TextEntity).")

Return type:  int

GetResult(*[row](#tts.core.report.parser.ProjectElement.ProjectElementStatistic.GetResult.row "tts.core.report.parser.ProjectElement.ProjectElementStatistic.GetResult.row (Python parameter) — The index of the row")*)[¶](#tts.core.report.parser.ProjectElement.ProjectElementStatistic.GetResult "Link to this definition")  
Parameters:  row : int[¶](#tts.core.report.parser.ProjectElement.ProjectElementStatistic.GetResult.row "Permalink to this definition")  
The index of the row

Returns:  The result of the given row

Return type:  str

GetResultCount(*[result](#tts.core.report.parser.ProjectElement.ProjectElementStatistic.GetResultCount.result "tts.core.report.parser.ProjectElement.ProjectElementStatistic.GetResultCount.result (Python parameter) — The result string.")*)[¶](#tts.core.report.parser.ProjectElement.ProjectElementStatistic.GetResultCount "Link to this definition")  
Parameters:  result : str[¶](#tts.core.report.parser.ProjectElement.ProjectElementStatistic.GetResultCount.result "Permalink to this definition")  
The result string. One of ‘NONE’, ‘SUCCESS’,’INCONCLUSIVE’, ‘FAILED’ or ‘ERROR’, otherwise None.

Returns:  The count of all project elements with the specified result

Return type:  int

GetSuccessCount()[¶](#tts.core.report.parser.ProjectElement.ProjectElementStatistic.GetSuccessCount "Link to this definition")  
Returns:  The count of all project elements with the result ‘SUCCESS’

Return type:  int

GetTotalCount()[¶](#tts.core.report.parser.ProjectElement.ProjectElementStatistic.GetTotalCount "Link to this definition")  
Returns:  The count of all project elements

Return type:  int

GetType()[¶](#tts.core.report.parser.ProjectElement.ProjectElementStatistic.GetType "Link to this definition")  
Returns the type name of the entity.

Returns:  The type name of the entity

Return type:  str

GetValue(*[row](#tts.core.report.parser.ProjectElement.ProjectElementStatistic.GetValue.row "tts.core.report.parser.ProjectElement.ProjectElementStatistic.GetValue.row (Python parameter) — The index of the row")*, *[col](#tts.core.report.parser.ProjectElement.ProjectElementStatistic.GetValue.col "tts.core.report.parser.ProjectElement.ProjectElementStatistic.GetValue.col (Python parameter) — The index of the column")*)[¶](#tts.core.report.parser.ProjectElement.ProjectElementStatistic.GetValue "Link to this definition")  
Parameters:  row : int[¶](#tts.core.report.parser.ProjectElement.ProjectElementStatistic.GetValue.row "Permalink to this definition")  
The index of the row

col : int[¶](#tts.core.report.parser.ProjectElement.ProjectElementStatistic.GetValue.col "Permalink to this definition")  
The index of the column

Returns:  The string for the cell specified by row and column

Return type:  str or None

IterRowsWithResult()[¶](#tts.core.report.parser.ProjectElement.ProjectElementStatistic.IterRowsWithResult "Link to this definition")  
Returns:  An iterator of all rows with a result

Return type:  generator\<tuple\<list\<str\>, str\>\>

*class* TableEntity[¶](#tts.core.report.db.TableEntity.TableEntity "Link to this definition")  
Represents a table.

GetCountAndPercentageOfResultItem(*[item](#tts.core.report.db.TableEntity.TableEntity.GetCountAndPercentageOfResultItem.item "tts.core.report.db.TableEntity.TableEntity.GetCountAndPercentageOfResultItem.item (Python parameter) — The result for which the count and percentage shall be returned, e.g. tts.core.common.Constants.RESULT_ERROR")*)[¶](#tts.core.report.db.TableEntity.TableEntity.GetCountAndPercentageOfResultItem "Link to this definition")  
Gets the absolute count and percentage of Packages that have the specified result. If no Package has the given result, a tuple containing (0, 0.0) is returned.

Parameters:  item : str[¶](#tts.core.report.db.TableEntity.TableEntity.GetCountAndPercentageOfResultItem.item "Permalink to this definition")  
The result for which the count and percentage shall be returned, e.g. tts.core.common.Constants.RESULT_ERROR

Returns:  Tuple consisting of the count and the percentage

Return type:  tuple[int, float]

GetCountOfResultItem(*[item](#tts.core.report.db.TableEntity.TableEntity.GetCountOfResultItem.item "tts.core.report.db.TableEntity.TableEntity.GetCountOfResultItem.item (Python parameter) — The result for which the count shall be returned, e.g. tts.core.common.Constants.RESULT_ERROR")*)[¶](#tts.core.report.db.TableEntity.TableEntity.GetCountOfResultItem "Link to this definition")  
Parameters:  item : str[¶](#tts.core.report.db.TableEntity.TableEntity.GetCountOfResultItem.item "Permalink to this definition")  
The result for which the count shall be returned, e.g. tts.core.common.Constants.RESULT_ERROR

Returns:  The absolute count of Packages that have the specified result

Return type:  int

GetEntityId()[¶](#tts.core.report.db.TableEntity.TableEntity.GetEntityId "Link to this definition")  
Returns:  The ID of the entity

Return type:  int

GetHeader()[¶](#tts.core.report.db.TableEntity.TableEntity.GetHeader "Link to this definition")  
Returns:  The header (first element of each column)

Return type:  list\<str\>

GetId()[¶](#tts.core.report.db.TableEntity.TableEntity.GetId "Link to this definition")  
Returns:  The ID of the entity

Return type:  int

GetName()[¶](#tts.core.report.db.TableEntity.TableEntity.GetName "Link to this definition")  
Returns:  The name of the entity

Return type:  str

GetNumberCols()[¶](#tts.core.report.db.TableEntity.TableEntity.GetNumberCols "Link to this definition")  
Returns:  The number of columns

Return type:  int

GetNumberRows()[¶](#tts.core.report.db.TableEntity.TableEntity.GetNumberRows "Link to this definition")  
Returns:  The number of rows

Return type:  int

GetPercentageOfResultItem(*[item](#tts.core.report.db.TableEntity.TableEntity.GetPercentageOfResultItem.item "tts.core.report.db.TableEntity.TableEntity.GetPercentageOfResultItem.item (Python parameter) — The result for which the precentage shall be returned, e.g. tts.core.common.Constants.RESULT_ERROR")*)[¶](#tts.core.report.db.TableEntity.TableEntity.GetPercentageOfResultItem "Link to this definition")  
Gets the percentage of Packages that have the specified result.

Parameters:  item : str[¶](#tts.core.report.db.TableEntity.TableEntity.GetPercentageOfResultItem.item "Permalink to this definition")  
The result for which the precentage shall be returned, e.g. tts.core.common.Constants.RESULT_ERROR

Returns:  The percentage of Packages that have the specified result

Return type:  float

GetReportItemId()[¶](#tts.core.report.db.TableEntity.TableEntity.GetReportItemId "Link to this definition")  
Returns:  The ID of the associated [`ReportItem`](#tts.core.report.db.ReportItem.ReportItem "tts.core.report.db.ReportItem.ReportItem (Python class) — A report item represents the execution results of one test step. It contains information like test step number, time of execution, type of test step and custom fields. Furthermore additional information on a test step can be stored in so called entity elements being attached to the respective report item (e.g. TableEntity or TextEntity).")

Return type:  int

GetResult(*[row](#tts.core.report.db.TableEntity.TableEntity.GetResult.row "tts.core.report.db.TableEntity.TableEntity.GetResult.row (Python parameter) — The index of the row")*)[¶](#tts.core.report.db.TableEntity.TableEntity.GetResult "Link to this definition")  
Parameters:  row : int[¶](#tts.core.report.db.TableEntity.TableEntity.GetResult.row "Permalink to this definition")  
The index of the row

Returns:  The result of the given row

Return type:  str

GetType()[¶](#tts.core.report.db.TableEntity.TableEntity.GetType "Link to this definition")  
Returns the type name of the entity.

Returns:  The type name of the entity

Return type:  str

GetValue(*[row](#tts.core.report.db.TableEntity.TableEntity.GetValue.row "tts.core.report.db.TableEntity.TableEntity.GetValue.row (Python parameter) — The index of the row")*, *[col](#tts.core.report.db.TableEntity.TableEntity.GetValue.col "tts.core.report.db.TableEntity.TableEntity.GetValue.col (Python parameter) — The index of the column")*)[¶](#tts.core.report.db.TableEntity.TableEntity.GetValue "Link to this definition")  
Parameters:  row : int[¶](#tts.core.report.db.TableEntity.TableEntity.GetValue.row "Permalink to this definition")  
The index of the row

col : int[¶](#tts.core.report.db.TableEntity.TableEntity.GetValue.col "Permalink to this definition")  
The index of the column

Returns:  The string for the cell specified by row and column

Return type:  str or None

IterRowsWithResult()[¶](#tts.core.report.db.TableEntity.TableEntity.IterRowsWithResult "Link to this definition")  
Returns:  An iterator of all rows with a result

Return type:  generator\<tuple\<list\<str\>, str\>\>

*class* TextEntity[¶](#tts.core.report.db.TextEntity.TextEntity "Link to this definition")  
Represents a custom text.

GetEntityId()[¶](#tts.core.report.db.TextEntity.TextEntity.GetEntityId "Link to this definition")  
Returns:  The ID of the entity

Return type:  int

GetId()[¶](#tts.core.report.db.TextEntity.TextEntity.GetId "Link to this definition")  
Returns:  The ID of the entity

Return type:  int

GetName()[¶](#tts.core.report.db.TextEntity.TextEntity.GetName "Link to this definition")  
Returns:  The name of the entity

Return type:  str

GetReportItemId()[¶](#tts.core.report.db.TextEntity.TextEntity.GetReportItemId "Link to this definition")  
Returns:  The ID of the associated [`ReportItem`](#tts.core.report.db.ReportItem.ReportItem "tts.core.report.db.ReportItem.ReportItem (Python class) — A report item represents the execution results of one test step. It contains information like test step number, time of execution, type of test step and custom fields. Furthermore additional information on a test step can be stored in so called entity elements being attached to the respective report item (e.g. TableEntity or TextEntity).")

Return type:  int

GetType()[¶](#tts.core.report.db.TextEntity.TextEntity.GetType "Link to this definition")  
Returns the type name of the entity.

Returns:  The type name of the entity

Return type:  str

GetValue()[¶](#tts.core.report.db.TextEntity.TextEntity.GetValue "Link to this definition")  
Returns the string for the custom text.

Returns:  The string for the custom text

Return type:  str

*class* TraceArtifactEntity[¶](#tts.core.report.parser.Package.TraceArtifactEntity "Link to this definition")  
The TraceArtifactEntity represents a table of recordings created by the trace analysis.

GetComment(*[index](#tts.core.report.parser.Package.TraceArtifactEntity.GetComment.index "tts.core.report.parser.Package.TraceArtifactEntity.GetComment.index (Python parameter)")*)[¶](#tts.core.report.parser.Package.TraceArtifactEntity.GetComment "Link to this definition")  
Parameters:  index : int[¶](#tts.core.report.parser.Package.TraceArtifactEntity.GetComment.index "Permalink to this definition")  

Returns:  Returns the comment of an artifact, if set.

Return type:  str or None

GetCount()[¶](#tts.core.report.parser.Package.TraceArtifactEntity.GetCount "Link to this definition")  
Returns:  The number of entries

Return type:  int

GetEntityId()[¶](#tts.core.report.parser.Package.TraceArtifactEntity.GetEntityId "Link to this definition")  
Returns:  The ID of the entity

Return type:  int

GetId()[¶](#tts.core.report.parser.Package.TraceArtifactEntity.GetId "Link to this definition")  
Returns:  The ID of the entity

Return type:  int

GetName()[¶](#tts.core.report.parser.Package.TraceArtifactEntity.GetName "Link to this definition")  
Returns:  The name of the entity

Return type:  str

GetRecording(*[index](#tts.core.report.parser.Package.TraceArtifactEntity.GetRecording.index "tts.core.report.parser.Package.TraceArtifactEntity.GetRecording.index (Python parameter)")*)[¶](#tts.core.report.parser.Package.TraceArtifactEntity.GetRecording "Link to this definition")  
Parameters:  index : int[¶](#tts.core.report.parser.Package.TraceArtifactEntity.GetRecording.index "Permalink to this definition")  

Returns:  The referenced recording

Return type:  [`Recording`](#tts.core.report.parser.Package.Recording "tts.core.report.parser.Package.Recording (Python class) — Represents a recording.")

GetRecordingId(*[index](#tts.core.report.parser.Package.TraceArtifactEntity.GetRecordingId.index "tts.core.report.parser.Package.TraceArtifactEntity.GetRecordingId.index (Python parameter)")*)[¶](#tts.core.report.parser.Package.TraceArtifactEntity.GetRecordingId "Link to this definition")  
Parameters:  index : int[¶](#tts.core.report.parser.Package.TraceArtifactEntity.GetRecordingId.index "Permalink to this definition")  

Returns:  The ID of the referenced recording

Return type:  int

GetReportItemId()[¶](#tts.core.report.parser.Package.TraceArtifactEntity.GetReportItemId "Link to this definition")  
Returns:  The ID of the associated [`ReportItem`](#tts.core.report.db.ReportItem.ReportItem "tts.core.report.db.ReportItem.ReportItem (Python class) — A report item represents the execution results of one test step. It contains information like test step number, time of execution, type of test step and custom fields. Furthermore additional information on a test step can be stored in so called entity elements being attached to the respective report item (e.g. TableEntity or TextEntity).")

Return type:  int

GetSourceReportItem(*[index](#tts.core.report.parser.Package.TraceArtifactEntity.GetSourceReportItem.index "tts.core.report.parser.Package.TraceArtifactEntity.GetSourceReportItem.index (Python parameter)")*)[¶](#tts.core.report.parser.Package.TraceArtifactEntity.GetSourceReportItem "Link to this definition")  
Parameters:  index : int[¶](#tts.core.report.parser.Package.TraceArtifactEntity.GetSourceReportItem.index "Permalink to this definition")  

Returns:  The report item of the step that created the artifact. Can be None.

Return type:  `AnalysisReportItem` or None

GetSourceReportItemId(*[index](#tts.core.report.parser.Package.TraceArtifactEntity.GetSourceReportItemId.index "tts.core.report.parser.Package.TraceArtifactEntity.GetSourceReportItemId.index (Python parameter)")*)[¶](#tts.core.report.parser.Package.TraceArtifactEntity.GetSourceReportItemId "Link to this definition")  
Returns the report item ID of the trace step that created the artifact. None if no source is set. Better use GetSourceReportItem(index) directly.

Parameters:  index : int[¶](#tts.core.report.parser.Package.TraceArtifactEntity.GetSourceReportItemId.index "Permalink to this definition")  

Returns:  The report item ID of the trace step that created the artifact

Return type:  int or None

GetType()[¶](#tts.core.report.parser.Package.TraceArtifactEntity.GetType "Link to this definition")  
Returns the type name of the entity.

Returns:  The type name of the entity

Return type:  str

IterItems()[¶](#tts.core.report.parser.Package.TraceArtifactEntity.IterItems "Link to this definition")  
Returns:  An iterator of all recordings returning a tuple containing recordingID, sourceReportItemID and comment

Return type:  generator\<tuple\<int, int, str\>\>

## Image[¶](#image "Link to this heading")

*class* Image[¶](#tts.core.report.db.Image.Image "Link to this definition")  
Represents a ReportItem-Image.

GetBitmap()[¶](#tts.core.report.db.Image.Image.GetBitmap "Link to this definition")  
Returns:  The bitmap

Return type:  wx.Bitmap

GetDepth()[¶](#tts.core.report.db.Image.Image.GetDepth "Link to this definition")  
Returns:  The color depth of the bitmap.

Return type:  int

GetHeight()[¶](#tts.core.report.db.Image.Image.GetHeight "Link to this definition")  
Returns:  The height of the image

Return type:  int

GetId()[¶](#tts.core.report.db.Image.Image.GetId "Link to this definition")  
Returns:  The ID of the image

Return type:  int

GetMaskColor()[¶](#tts.core.report.db.Image.Image.GetMaskColor "Link to this definition")  
Returns:  Mask-Color in CSS Hex e.g. \#00FF00

Return type:  str

GetName()[¶](#tts.core.report.db.Image.Image.GetName "Link to this definition")  
Returns:  The name of the image

Return type:  str

GetSubTitle()[¶](#tts.core.report.db.Image.Image.GetSubTitle "Link to this definition")  
Returns:  The sub title of the image

Return type:  str

GetTitle()[¶](#tts.core.report.db.Image.Image.GetTitle "Link to this definition")  
Returns:  The title of the image

Return type:  str

GetWidth()[¶](#tts.core.report.db.Image.Image.GetWidth "Link to this definition")  
Returns:  The width of the mage

Return type:  int

## Info[¶](#info "Link to this heading")

*class* Info[¶](#tts.core.report.db.Info.Info "Link to this definition")  

GetAppName()[¶](#tts.core.report.db.Info.Info.GetAppName "Link to this definition")  
Returns:  The name of the used application

Return type:  str

GetAppVersion()[¶](#tts.core.report.db.Info.Info.GetAppVersion "Link to this definition")  
Returns:  The version of the used application

Return type:  str

GetAuthor()[¶](#tts.core.report.db.Info.Info.GetAuthor "Link to this definition")  
Returns:  The author of the info

Return type:  str

GetDbVersion()[¶](#tts.core.report.db.Info.Info.GetDbVersion "Link to this definition")  
Returns:  The version of the database

Return type:  int

GetDuration()[¶](#tts.core.report.db.Info.Info.GetDuration "Link to this definition")  
Returns:  The Duration of the info

Return type:  float

GetExecutionMode()[¶](#tts.core.report.db.Info.Info.GetExecutionMode "Link to this definition")  
Returns:  The execution mode

Return type:  str

GetExecutionTime()[¶](#tts.core.report.db.Info.Info.GetExecutionTime "Link to this definition")  
Returns:  The execution time

Return type:  datetime

GetId()[¶](#tts.core.report.db.Info.Info.GetId "Link to this definition")  
Returns:  The ID of the info

Return type:  int

GetInfoId()[¶](#tts.core.report.db.Info.Info.GetInfoId "Link to this definition")  
Returns:  The ID of the info

Return type:  int

GetKeywordCatalog()[¶](#tts.core.report.db.Info.Info.GetKeywordCatalog "Link to this definition")  
Returns:  The keyword catalog name or an empty string if no keyword catalog was present at test execution.

Return type:  str

GetProjectExecutionPath()[¶](#tts.core.report.db.Info.Info.GetProjectExecutionPath "Link to this definition")  
Returns the execution path in relation to the calling project if executed as separate subproject or the name of the project, if not executed separately.

Returns:  Path in the project execution stack

Return type:  str

GetResult()[¶](#tts.core.report.db.Info.Info.GetResult "Link to this definition")  
Returns the result of the info

Returns:  The test result. One of - NONE - SUCCESS - INCONCLUSIVE - FAILED - ERROR

Return type:  str

GetSignature()[¶](#tts.core.report.db.Info.Info.GetSignature "Link to this definition")  
Returns:  The Signature of the info

Return type:  str

GetTeststand()[¶](#tts.core.report.db.Info.Info.GetTeststand "Link to this definition")  
Returns:  Name of the computer the test was executed at

Return type:  str

GetTimeZoneUTCOffset()[¶](#tts.core.report.db.Info.Info.GetTimeZoneUTCOffset "Link to this definition")  
Gets the UTC offset in seconds based on the time zone in which the test report was created. If the time zone is not specified in the report, None is returned.

Returns:  UTC offset in seconds or None

Return type:  int or None

GetTimeZoneUTCOffsetStr()[¶](#tts.core.report.db.Info.Info.GetTimeZoneUTCOffsetStr "Link to this definition")  
Gets a string which contains the UTC offset of the time zone in which the test report was created, e.g. “UTC +2:00”. If the time zone is not specified in the report, an empty string is returned.

Returns:  UTC offset as string or an empty string

Return type:  str

GetUUID()[¶](#tts.core.report.db.Info.Info.GetUUID "Link to this definition")  
Returns:  The UUID of the info

Return type:  UUID

## MappingItem[¶](#mappingitem "Link to this heading")

*class* MappingItem[¶](#tts.core.report.db.MappingItem.MappingItem "Link to this definition")  
GetDescription()[¶](#tts.core.report.db.MappingItem.MappingItem.GetDescription "Link to this definition")  
Returns:  The description of the mapping item

Return type:  str

GetId()[¶](#tts.core.report.db.MappingItem.MappingItem.GetId "Link to this definition")  
Returns:  The ID of the mapping item

Return type:  int

GetMappingItemId()[¶](#tts.core.report.db.MappingItem.MappingItem.GetMappingItemId "Link to this definition")  
Returns:  The ID of the mapping item

Return type:  int

GetName()[¶](#tts.core.report.db.MappingItem.MappingItem.GetName "Link to this definition")  
Returns:  The name of the mapping item

Return type:  str

GetOrigin()[¶](#tts.core.report.db.MappingItem.MappingItem.GetOrigin "Link to this definition")  
Returns:  The origin of the mapping item

Return type:  str

GetParentId()[¶](#tts.core.report.db.MappingItem.MappingItem.GetParentId "Link to this definition")  
Returns:  The ID of the parent

Return type:  int

GetTarget()[¶](#tts.core.report.db.MappingItem.MappingItem.GetTarget "Link to this definition")  
Returns the path this mapping item is currently pointing at.

Returns:  Complete path to the destination test quantity

Return type:  str

GetType()[¶](#tts.core.report.db.MappingItem.MappingItem.GetType "Link to this definition")  
Returns:  Type of the mapping item

Return type:  str

GetUsedRaster()[¶](#tts.core.report.db.MappingItem.MappingItem.GetUsedRaster "Link to this definition")  
Returns:  The used raster of the mapping item

Return type:  str

GetWantedRaster()[¶](#tts.core.report.db.MappingItem.MappingItem.GetWantedRaster "Link to this definition")  
Returns:  The wanted raster of the mapping item

Return type:  str

IsForcedRaster()[¶](#tts.core.report.db.MappingItem.MappingItem.IsForcedRaster "Link to this definition")  
Returns:  True if registration of the raster is enforced, otherwise False

Return type:  bool

IsGlobal()[¶](#tts.core.report.db.MappingItem.MappingItem.IsGlobal "Link to this definition")  
Returns:  True if mapping item is global, otherwise False

Return type:  bool

## Package[¶](#module-tts.core.report.parser.Package "Link to this heading")

*class* AnalysisJobItem[¶](#tts.core.report.parser.Package.AnalysisJobItem "Link to this definition")  

GetMaxExecLevel()[¶](#tts.core.report.parser.Package.AnalysisJobItem.GetMaxExecLevel "Link to this definition")  
Returns:  The maximum execution level

Return type:  int

GetOriginalResult()[¶](#tts.core.report.parser.Package.AnalysisJobItem.GetOriginalResult "Link to this definition")  
Returns:  The original result verdict of the analysis job

Return type:  str

GetResult()[¶](#tts.core.report.parser.Package.AnalysisJobItem.GetResult "Link to this definition")  
Returns:  The result verdict of the analysis job

Return type:  str

GetStimulationPackage()[¶](#tts.core.report.parser.Package.AnalysisJobItem.GetStimulationPackage "Link to this definition")  
This call is only valid for analysis jobs derived from analysis packages. For parameterized stimulations, the resulting Package object characterizes a particular parameter set.

Returns:  The invoked stimulation Package

Return type:  [`Package`](#tts.core.report.parser.Package.Package "tts.core.report.parser.Package.Package (Python class) — This class represents a Package that was executed individually or called directly from a Project.")

GetTraceAnalysis()[¶](#tts.core.report.parser.Package.AnalysisJobItem.GetTraceAnalysis "Link to this definition")  
Returns:  The ReportItem instance of the trace analysis. If the trace analysis has not been executed, None is returned.

Return type:  `AnalysisReportItem`

HasData()[¶](#tts.core.report.parser.Package.AnalysisJobItem.HasData "Link to this definition")  
Returns:  True when analysis job item has data, otherwise False

Return type:  bool

HasParams()[¶](#tts.core.report.parser.Package.AnalysisJobItem.HasParams "Link to this definition")  
Returns:  Indicates whether the analysis job has input parameters

Return type:  bool

HasReturnValues()[¶](#tts.core.report.parser.Package.AnalysisJobItem.HasReturnValues "Link to this definition")  
Returns:  Indicates whether the analysis job has return values

Return type:  bool

IterParameterVariables()[¶](#tts.core.report.parser.Package.AnalysisJobItem.IterParameterVariables "Link to this definition")  
Returns:  An iterator for the parameters. Each parameter is represented as a [`PackageParameterVariable`](#tts.core.report.db.Variable.PackageParameterVariable "tts.core.report.db.Variable.PackageParameterVariable (Python class) — The Variable represents a test case parameter variable used in a Package.") instance. Their origin is always None.

Return type:  generator\<[`PackageParameterVariable`](#tts.core.report.db.Variable.PackageParameterVariable "tts.core.report.db.Variable.PackageParameterVariable (Python class) — The Variable represents a test case parameter variable used in a Package.")\>

IterReturnVariables(*[stage](#tts.core.report.parser.Package.AnalysisJobItem.IterReturnVariables "tts.core.report.parser.Package.AnalysisJobItem.IterReturnVariables.stage (Python parameter)")=`'final'`*)[¶](#tts.core.report.parser.Package.AnalysisJobItem.IterReturnVariables "Link to this definition")  
Returns:  An iterator for all return variables. Each variable is represented as a [`PackageReturnVariable`](#tts.core.report.db.Variable.PackageReturnVariable "tts.core.report.db.Variable.PackageReturnVariable (Python class) — The Variable represents a return variable used in a Package.") instance.

Return type:  generator\<[`PackageReturnVariable`](#tts.core.report.db.Variable.PackageReturnVariable "tts.core.report.db.Variable.PackageReturnVariable (Python class) — The Variable represents a return variable used in a Package.")\>

IterTraceItems(*[excludeRefTa](#tts.core.report.parser.Package.AnalysisJobItem.IterTraceItems "tts.core.report.parser.Package.AnalysisJobItem.IterTraceItems.excludeRefTa (Python parameter)")=`False`*)[¶](#tts.core.report.parser.Package.AnalysisJobItem.IterTraceItems "Link to this definition")  
Returns:  An iterator for all trace items

Return type:  generator\<[`ReportItem`](#tts.core.report.db.ReportItem.ReportItem "tts.core.report.db.ReportItem.ReportItem (Python class) — A report item represents the execution results of one test step. It contains information like test step number, time of execution, type of test step and custom fields. Furthermore additional information on a test step can be stored in so called entity elements being attached to the respective report item (e.g. TableEntity or TextEntity).")\>

IterUserComments(*[recursive](#tts.core.report.parser.Package.AnalysisJobItem.IterUserComments.recursive "tts.core.report.parser.Package.AnalysisJobItem.IterUserComments.recursive (Python parameter) — If True, also comments of children are included.")=`False`*)[¶](#tts.core.report.parser.Package.AnalysisJobItem.IterUserComments "Link to this definition")  
Yield all [`ReportItemComment`](#tts.core.report.db.ReportItemComment.ReportItemComment "tts.core.report.db.ReportItemComment.ReportItemComment (Python class) — The author of the comment") of the [`ReportItem`](#tts.core.report.db.ReportItem.ReportItem "tts.core.report.db.ReportItem.ReportItem (Python class) — A report item represents the execution results of one test step. It contains information like test step number, time of execution, type of test step and custom fields. Furthermore additional information on a test step can be stored in so called entity elements being attached to the respective report item (e.g. TableEntity or TextEntity)."). If recursive is True, comments of all children are yielded as well. This can improve performance of reading all report comments significantly.

Parameters:  recursive : bool[¶](#tts.core.report.parser.Package.AnalysisJobItem.IterUserComments.recursive "Permalink to this definition")  
If True, also comments of children are included.

Type:  recursive: bool

Return type:  Iterator[[`ReportItemComment`](#tts.core.report.db.ReportItemComment.ReportItemComment "tts.core.report.db.ReportItemComment.ReportItemComment (Python class) — The author of the comment")]

*class* Mapping[¶](#tts.core.report.parser.Package.Mapping "Link to this definition")  
Represents a mapping item.

GetDescription()[¶](#tts.core.report.parser.Package.Mapping.GetDescription "Link to this definition")  
Returns:  The description of the mapping item

Return type:  str

GetId()[¶](#tts.core.report.parser.Package.Mapping.GetId "Link to this definition")  
Returns:  The ID of the mapping item

Return type:  int

GetMappingItemId()[¶](#tts.core.report.parser.Package.Mapping.GetMappingItemId "Link to this definition")  
Returns:  The ID of the mapping item

Return type:  int

GetName()[¶](#tts.core.report.parser.Package.Mapping.GetName "Link to this definition")  
Returns:  The name of the mapping item

Return type:  str

GetOrigin()[¶](#tts.core.report.parser.Package.Mapping.GetOrigin "Link to this definition")  
Returns:  The origin of the mapping item

Return type:  str

GetParentId()[¶](#tts.core.report.parser.Package.Mapping.GetParentId "Link to this definition")  
Returns:  The ID of the parent

Return type:  int

GetTarget()[¶](#tts.core.report.parser.Package.Mapping.GetTarget "Link to this definition")  
Returns the path this mapping item is currently pointing at.

Returns:  Complete path to the destination test quantity

Return type:  str

GetType()[¶](#tts.core.report.parser.Package.Mapping.GetType "Link to this definition")  
Returns:  Type of the mapping item

Return type:  str

GetUsedRaster()[¶](#tts.core.report.parser.Package.Mapping.GetUsedRaster "Link to this definition")  
Returns:  The used raster of the mapping item

Return type:  str

GetWantedRaster()[¶](#tts.core.report.parser.Package.Mapping.GetWantedRaster "Link to this definition")  
Returns:  The wanted raster of the mapping item

Return type:  str

HasSubMappings()[¶](#tts.core.report.parser.Package.Mapping.HasSubMappings "Link to this definition")  
Returns:  Indicates weather the mapping has sub mappings

Return type:  bool

IsForcedRaster()[¶](#tts.core.report.parser.Package.Mapping.IsForcedRaster "Link to this definition")  
Returns:  True if registration of the raster is enforced, otherwise False

Return type:  bool

IsGlobal()[¶](#tts.core.report.parser.Package.Mapping.IsGlobal "Link to this definition")  
Returns:  True if mapping item is global, otherwise False

Return type:  bool

IterSubMappings()[¶](#tts.core.report.parser.Package.Mapping.IterSubMappings "Link to this definition")  
Returns:  An iterator for all sub mappings

Return type:  generator\<[`Mapping`](#tts.core.report.parser.Package.Mapping "tts.core.report.parser.Package.Mapping (Python class) — Represents a mapping item.")\>

*class* Mappings[¶](#tts.core.report.parser.Package.Mappings "Link to this definition")  
Represents package mappings.

IterMappings()[¶](#tts.core.report.parser.Package.Mappings.IterMappings "Link to this definition")  
Returns:  An iterator for all mappings used by the package

Return type:  generator\<[`Mapping`](#tts.core.report.parser.Package.Mapping "tts.core.report.parser.Package.Mapping (Python class) — Represents a mapping item.")\>

*class* Package[¶](#tts.core.report.parser.Package.Package "Link to this definition")  
This class represents a Package that was executed individually or called directly from a Project.

GetAbortCode()[¶](#tts.core.report.parser.Package.Package.GetAbortCode "Link to this definition")  
Returns:  The abort code of the Package

Return type:  str

GetAbortComment()[¶](#tts.core.report.parser.Package.Package.GetAbortComment "Link to this definition")  
Returns:  The abort comment of the Package

Return type:  str

GetAdditionalInfo()[¶](#tts.core.report.parser.Package.Package.GetAdditionalInfo "Link to this definition")  
Returns:  The additional info of the Package, if set

Return type:  str | None

GetArtifacts()[¶](#tts.core.report.parser.Package.Package.GetArtifacts "Link to this definition")  
Returns all referenced artifacts.

Returns:  A list of all referenced artifacts.

Return type:  list[[`Artifact`](#tts.core.report.db.Artifact.Artifact "tts.core.report.db.Artifact.Artifact (Python class) — Represents an artifact that is shown in the package's report summary "Artifacts" tab.")]

GetCallError()[¶](#tts.core.report.parser.Package.Package.GetCallError "Link to this definition")  
Returns:  The call error of the Package

Return type:  str

GetComment()[¶](#tts.core.report.parser.Package.Package.GetComment "Link to this definition")  
Returns:  Comment of the Package

Return type:  str

GetDescription()[¶](#tts.core.report.parser.Package.Package.GetDescription "Link to this definition")  
Returns:  The description of the Package

Return type:  str

GetDuration()[¶](#tts.core.report.parser.Package.Package.GetDuration "Link to this definition")  
Returns:  The duration of the Package

Return type:  str or None

GetElementName()[¶](#tts.core.report.parser.Package.Package.GetElementName "Link to this definition")  
Returns:  The name of the project component

Return type:  str

GetGlobalConstantsDefinedOnStart()[¶](#tts.core.report.parser.Package.Package.GetGlobalConstantsDefinedOnStart "Link to this definition")  
Returns:  The values that the global constants had at the start of the Package execution

Return type:  list[[`Constant`](#tts.core.report.db.Constant.Constant "tts.core.report.db.Constant.Constant (Python class) — Represents a global constant.")]

GetHash()[¶](#tts.core.report.parser.Package.Package.GetHash "Link to this definition")  
Returns:  The hash of the Package

Return type:  str or None

GetId()[¶](#tts.core.report.parser.Package.Package.GetId "Link to this definition")  
Returns:  The ID of the Package

Return type:  int or None

GetIsTestcase()[¶](#tts.core.report.parser.Package.Package.GetIsTestcase "Link to this definition")  
Returns the state of the test case flag.

Returns:  True if test case flag is enabled, otherwise False

Return type:  bool

GetLibraryId()[¶](#tts.core.report.parser.Package.Package.GetLibraryId "Link to this definition")  
Returns:  The library ID of the Package

Return type:  str or None

GetLinkedTestManagementIds()[¶](#tts.core.report.parser.Package.Package.GetLinkedTestManagementIds "Link to this definition")  
Returns:  The test management IDs which are contained in the revaluation comments

Return type:  list[str]

GetMappings()[¶](#tts.core.report.parser.Package.Package.GetMappings "Link to this definition")  
Returns:  The mappings of the Package

Return type:  [`Mappings`](#tts.core.report.parser.Package.Mappings "tts.core.report.parser.Package.Mappings (Python class) — Represents package mappings.")

GetName()[¶](#tts.core.report.parser.Package.Package.GetName "Link to this definition")  
Returns:  The name of the Package.

Return type:  str

GetOriginalResult()[¶](#tts.core.report.parser.Package.Package.GetOriginalResult "Link to this definition")  
Returns:  The original result verdict of the report item

Return type:  str

GetParameterDescription(*[name](#tts.core.report.parser.Package.Package.GetParameterDescription.name "tts.core.report.parser.Package.Package.GetParameterDescription.name (Python parameter) — Name of the parameter")*)[¶](#tts.core.report.parser.Package.Package.GetParameterDescription "Link to this definition")  
Parameters:  name : str[¶](#tts.core.report.parser.Package.Package.GetParameterDescription.name "Permalink to this definition")  
Name of the parameter

Returns:  The description of the specified parameter

Return type:  str

GetParameterInitialValue(*[name](#tts.core.report.parser.Package.Package.GetParameterInitialValue.name "tts.core.report.parser.Package.Package.GetParameterInitialValue.name (Python parameter) — Name of the parameter")*)[¶](#tts.core.report.parser.Package.Package.GetParameterInitialValue "Link to this definition")  
Parameters:  name : str[¶](#tts.core.report.parser.Package.Package.GetParameterInitialValue.name "Permalink to this definition")  
Name of the parameter

Returns:  The initial value of the specified parameter.

Return type:  str

GetParameterNames()[¶](#tts.core.report.parser.Package.Package.GetParameterNames "Link to this definition")  
Returns:  The names of all parameters

Return type:  list[str]

GetParameterOrigin(*[name](#tts.core.report.parser.Package.Package.GetParameterOrigin.name "tts.core.report.parser.Package.Package.GetParameterOrigin.name (Python parameter) — Name of the parameter")*)[¶](#tts.core.report.parser.Package.Package.GetParameterOrigin "Link to this definition")  
Parameters:  name : str[¶](#tts.core.report.parser.Package.Package.GetParameterOrigin.name "Permalink to this definition")  
Name of the parameter

Returns:  The origin of the parameter

Rytpe:  
str

Return type:  str | None

GetParameterValue(*[name](#tts.core.report.parser.Package.Package.GetParameterValue.name "tts.core.report.parser.Package.Package.GetParameterValue.name (Python parameter) — Name of the parameter")*)[¶](#tts.core.report.parser.Package.Package.GetParameterValue "Link to this definition")  
Parameters:  name : str[¶](#tts.core.report.parser.Package.Package.GetParameterValue.name "Permalink to this definition")  
Name of the parameter

Returns:  The value of the specified parameter as string representation

Return type:  str

GetPath()[¶](#tts.core.report.parser.Package.Package.GetPath "Link to this definition")  
Returns:  The path of the Package

Return type:  str

GetPkgId()[¶](#tts.core.report.parser.Package.Package.GetPkgId "Link to this definition")  
Returns:  The ID of the Package

Return type:  int or None

GetRecordings()[¶](#tts.core.report.parser.Package.Package.GetRecordings "Link to this definition")  
Returns:  The recordings of the Package

Return type:  [`Recordings`](#tts.core.report.parser.Package.Recordings "tts.core.report.parser.Package.Recordings (Python class) — Represents recordings.")

GetReportItemId()[¶](#tts.core.report.parser.Package.Package.GetReportItemId "Link to this definition")  
Returns:  The ID of the report item

Return type:  int

GetResult()[¶](#tts.core.report.parser.Package.Package.GetResult "Link to this definition")  
Returns:  The result of the project component

Return type:  str

GetReturnDescription(*[name](#tts.core.report.parser.Package.Package.GetReturnDescription "tts.core.report.parser.Package.Package.GetReturnDescription.name (Python parameter)")*)[¶](#tts.core.report.parser.Package.Package.GetReturnDescription "Link to this definition")  
Returns:  The description of the specified return

Return type:  str | None

GetReturnInitialValue(*[name](#tts.core.report.parser.Package.Package.GetReturnInitialValue "tts.core.report.parser.Package.Package.GetReturnInitialValue.name (Python parameter)")*)[¶](#tts.core.report.parser.Package.Package.GetReturnInitialValue "Link to this definition")  
Returns:  The initial value of the specified return

Return type:  str

GetReturnNames()[¶](#tts.core.report.parser.Package.Package.GetReturnNames "Link to this definition")  
Returns:  The names of all returns of the current Package

Return type:  list[str]

GetReturnValue(*[name](#tts.core.report.parser.Package.Package.GetReturnValue "tts.core.report.parser.Package.Package.GetReturnValue.name (Python parameter)")*)[¶](#tts.core.report.parser.Package.Package.GetReturnValue "Link to this definition")  
Returns:  The value of the specified return

Return type:  str

GetRevalComments()[¶](#tts.core.report.parser.Package.Package.GetRevalComments "Link to this definition")  
Returns:  The revaluation comments of the current Package

Return type:  list\<[`RevaluationComment`](#tts.core.report.db.ReportItem.RevaluationComment "tts.core.report.db.ReportItem.RevaluationComment (Python class) — The author of the revaluation comment")\>

GetRevalCommentsString()[¶](#tts.core.report.parser.Package.Package.GetRevalCommentsString "Link to this definition")  
Gets the revaluation comments of the current Package. The comments are combined to a single string with the pattern “Creator: Comment -> Revaluated result”. If no revaluation comments exists, an empty string is returned.

Returns:  A string representing the combined revaluation comments

Return type:  str

GetRevision()[¶](#tts.core.report.parser.Package.Package.GetRevision "Link to this definition")  
Returns:  The revision of the Package

Return type:  str

GetSCMBranch()[¶](#tts.core.report.parser.Package.Package.GetSCMBranch "Link to this definition")  
Returns:  The SCM Branch of the Package

Return type:  str or None

GetSCMStatus()[¶](#tts.core.report.parser.Package.Package.GetSCMStatus "Link to this definition")  
Returns:  The SCM status of the Package

Return type:  str or None

GetSCMUrl()[¶](#tts.core.report.parser.Package.Package.GetSCMUrl "Link to this definition")  
Returns:  The SCM URL of the Package

Return type:  str or None

GetStimulationPackage(*[returnParamSets](#tts.core.report.parser.Package.Package.GetStimulationPackage.returnParamSets "tts.core.report.parser.Package.Package.GetStimulationPackage.returnParamSets (Python parameter) — Specifies, how to deal with stimulation parameter sets.")=`True`*)[¶](#tts.core.report.parser.Package.Package.GetStimulationPackage "Link to this definition")  
This call is only valid for analysis packages and returns the stimulation Package.

Note:  
For older reports (before 2022.2) this method may return None if no trace analysis was executed.

Parameters:  returnParamSets : bool[¶](#tts.core.report.parser.Package.Package.GetStimulationPackage.returnParamSets "Permalink to this definition")  
Specifies, how to deal with stimulation parameter sets. If True, the parameter set that has been used to stimulate the execution of the analysis Package is returned.

If False, the stimulation Package itself is returned, which is of type `ParameterizedPackage` for parameterized stimulations.

Returns:  The stimulation Package. The default return value will be of type [`Package`](#tts.core.report.parser.Package.Package "tts.core.report.parser.Package.Package (Python class) — This class represents a Package that was executed individually or called directly from a Project."). If returnParamSets is False, it is possibly also of type `ParameterizedPackage`.

Return type:  [`Package`](#tts.core.report.parser.Package.Package "tts.core.report.parser.Package.Package (Python class) — This class represents a Package that was executed individually or called directly from a Project.") or `ParameterizedPackage`

GetSubReportPath()[¶](#tts.core.report.parser.Package.Package.GetSubReportPath "Link to this definition")  
Returns the path to the trf subreport of the package.

Returns:  The path to the trf sub report or None if there is no sub report

Return type:  str

GetTestCase(*[excludeSubPackages](#tts.core.report.parser.Package.Package.GetTestCase.excludeSubPackages "tts.core.report.parser.Package.Package.GetTestCase.excludeSubPackages (Python parameter)")=`True`*)[¶](#tts.core.report.parser.Package.Package.GetTestCase "Link to this definition")  
Parameters:  excludeSubPackages : bool[¶](#tts.core.report.parser.Package.Package.GetTestCase.excludeSubPackages "Permalink to this definition")  

Returns:  The test case of the Package

Return type:  [`TestCase`](#tts.core.report.parser.Package.TestCase "tts.core.report.parser.Package.TestCase (Python class) — Maximum execution level")

GetTestScriptId()[¶](#tts.core.report.parser.Package.Package.GetTestScriptId "Link to this definition")  
Returns:  The test script ID, if set

Return type:  str | None

GetTestmanagementId()[¶](#tts.core.report.parser.Package.Package.GetTestmanagementId "Link to this definition")  
Returns:  The test management ID of the Package

Return type:  str or None

GetTime()[¶](#tts.core.report.parser.Package.Package.GetTime "Link to this definition")  
Returns:  The time of the Package

Return type:  datetime.datetime | None

GetTraceAnalyses()[¶](#tts.core.report.parser.Package.Package.GetTraceAnalyses "Link to this definition")  
Returns:  The trace analyses

Return type:  [`TraceAnalyses`](#tts.core.report.parser.Package.TraceAnalyses "tts.core.report.parser.Package.TraceAnalyses (Python class) — The maximum execution level")

GetUserReportData()[¶](#tts.core.report.parser.Package.Package.GetUserReportData "Link to this definition")  
Returns:  The user defined report data. The data consists of name and a tuple consisting of value and description.

Return type:  dict[str, tuple[str, str]]

GetVersion()[¶](#tts.core.report.parser.Package.Package.GetVersion "Link to this definition")  
Returns:  The version of the Package

Return type:  str

HasAnalysisJobs(*[excludeSubPackages](#tts.core.report.parser.Package.Package.HasAnalysisJobs "tts.core.report.parser.Package.Package.HasAnalysisJobs.excludeSubPackages (Python parameter)")=`True`*)[¶](#tts.core.report.parser.Package.Package.HasAnalysisJobs "Link to this definition")  
Returns:  Indicates whether the Package has analysis jobs

Return type:  bool

HasAttributes()[¶](#tts.core.report.parser.Package.Package.HasAttributes "Link to this definition")  
Returns:  True if Package has any attributes, otherwise False

Return type:  bool

HasMappings()[¶](#tts.core.report.parser.Package.Package.HasMappings "Link to this definition")  
Returns:  Indicates whether the Package has mappings

Return type:  bool

HasParams()[¶](#tts.core.report.parser.Package.Package.HasParams "Link to this definition")  
Returns:  True if Package has any parameters, otherwise False

Return type:  bool

HasRecordings()[¶](#tts.core.report.parser.Package.Package.HasRecordings "Link to this definition")  
Returns:  Indicates whether the Package has recordings

Return type:  bool

HasReturnValues()[¶](#tts.core.report.parser.Package.Package.HasReturnValues "Link to this definition")  
Returns:  True if Package has any return values, otherwise False

Return type:  bool

HasRevalComments()[¶](#tts.core.report.parser.Package.Package.HasRevalComments "Link to this definition")  
Returns:  Indicates whether the current Package has revaluation comments

Return type:  bool

HasTestCase()[¶](#tts.core.report.parser.Package.Package.HasTestCase "Link to this definition")  
Returns:  Indicates whether the Package has a test case

Return type:  bool

HasTraceAnalyses()[¶](#tts.core.report.parser.Package.Package.HasTraceAnalyses "Link to this definition")  
Returns:  Indicates whether the Package has trace analyses

Return type:  bool

IsAnalysisPackage()[¶](#tts.core.report.parser.Package.Package.IsAnalysisPackage "Link to this definition")  
Returns:  True if Package is an analysis Package, otherwise False

Return type:  bool

IsSkipped()[¶](#tts.core.report.parser.Package.Package.IsSkipped "Link to this definition")  
Returns:  Indicates whether the current Package was skipped by the user, e.g. by filtering or commenting out.

Return type:  bool

IsStimulationPackage()[¶](#tts.core.report.parser.Package.Package.IsStimulationPackage "Link to this definition")  
Returns:  True if Package is a stimulation Package, otherwise False

Return type:  bool

IterAnalysisJobs(*[excludeSubPackages](#tts.core.report.parser.Package.Package.IterAnalysisJobs.excludeSubPackages "tts.core.report.parser.Package.Package.IterAnalysisJobs.excludeSubPackages (Python parameter) — True when subPackages should be excluded, otherwise False")=`True`*)[¶](#tts.core.report.parser.Package.Package.IterAnalysisJobs "Link to this definition")  
Parameters:  excludeSubPackages : bool[¶](#tts.core.report.parser.Package.Package.IterAnalysisJobs.excludeSubPackages "Permalink to this definition")  
True when subPackages should be excluded, otherwise False

Returns:  An Iterator for the analysis jobs

Return type:  Iterator[[`AnalysisJobItem`](#tts.core.report.parser.Package.AnalysisJobItem "tts.core.report.parser.Package.AnalysisJobItem (Python class) — The maximum execution level")]

IterAttributes()[¶](#tts.core.report.parser.Package.Package.IterAttributes "Link to this definition")  
Returns:  An Iterator for the attributes

Return type:  Iterator[[`Attribute`](#tts.core.report.db.Attribute.Attribute "tts.core.report.db.Attribute.Attribute (Python class) — Represents attributes of a project, package, or test case")]

IterParameterVariables()[¶](#tts.core.report.parser.Package.Package.IterParameterVariables "Link to this definition")  
Returns:  An iterator for the parameters

Return type:  Iterator[[`PackageParameterVariable`](#tts.core.report.db.Variable.PackageParameterVariable "tts.core.report.db.Variable.PackageParameterVariable (Python class) — The Variable represents a test case parameter variable used in a Package.")]

IterReturnVariables()[¶](#tts.core.report.parser.Package.Package.IterReturnVariables "Link to this definition")  
Gets an iterator for the return variables. Each variable is represented by a [`PackageReturnVariable`](#tts.core.report.db.Variable.PackageReturnVariable "tts.core.report.db.Variable.PackageReturnVariable (Python class) — The Variable represents a return variable used in a Package.") instance containing the value the variable had after the execution of the test case and all analysis jobs. If the variable is written by multiple analysis jobs with different values, the value is set to ‘Inconsistent’.

Return type:  Iterator[[`PackageReturnVariable`](#tts.core.report.db.Variable.PackageReturnVariable "tts.core.report.db.Variable.PackageReturnVariable (Python class) — The Variable represents a return variable used in a Package.")]

IterReturnVariablesAfterTest()[¶](#tts.core.report.parser.Package.Package.IterReturnVariablesAfterTest "Link to this definition")  
Gets an iterator for the return variables. Each variable is represented by a [`PackageReturnVariable`](#tts.core.report.db.Variable.PackageReturnVariable "tts.core.report.db.Variable.PackageReturnVariable (Python class) — The Variable represents a return variable used in a Package.") instance containing the value the variable had after the execution of the test case but before the execution of the analysis jobs.

Return type:  Iterator[[`PackageReturnVariable`](#tts.core.report.db.Variable.PackageReturnVariable "tts.core.report.db.Variable.PackageReturnVariable (Python class) — The Variable represents a return variable used in a Package.")]

IterUserComments(*[recursive](#tts.core.report.parser.Package.Package.IterUserComments.recursive "tts.core.report.parser.Package.Package.IterUserComments.recursive (Python parameter) — If True, also comments of children are included.")=`False`*)[¶](#tts.core.report.parser.Package.Package.IterUserComments "Link to this definition")  
Yield all [`ReportItemComment`](#tts.core.report.db.ReportItemComment.ReportItemComment "tts.core.report.db.ReportItemComment.ReportItemComment (Python class) — The author of the comment") of the [`ReportItem`](#tts.core.report.db.ReportItem.ReportItem "tts.core.report.db.ReportItem.ReportItem (Python class) — A report item represents the execution results of one test step. It contains information like test step number, time of execution, type of test step and custom fields. Furthermore additional information on a test step can be stored in so called entity elements being attached to the respective report item (e.g. TableEntity or TextEntity)."). If recursive is True, comments of all children are yielded as well. This can improve performance of reading all report comments significantly.

Parameters:  recursive : bool[¶](#tts.core.report.parser.Package.Package.IterUserComments.recursive "Permalink to this definition")  
If True, also comments of children are included.

Type:  recursive: bool

Return type:  Iterator[[`ReportItemComment`](#tts.core.report.db.ReportItemComment.ReportItemComment "tts.core.report.db.ReportItemComment.ReportItemComment (Python class) — The author of the comment")]

GetComponentName()[¶](#tts.core.report.parser.Package.Package.GetComponentName "Link to this definition")  
Deprecated since version 2024.1: Use [`GetElementName()`](#tts.core.report.parser.Package.Package.GetElementName "tts.core.report.parser.Package.Package.GetElementName (Python method) — The name of the project component").

Returns:  The name of the project component

Return type:  str

*class* ParallelPackage[¶](#tts.core.report.parser.Package.ParallelPackage "Link to this definition")  

GetAbortCode()[¶](#tts.core.report.parser.Package.ParallelPackage.GetAbortCode "Link to this definition")  
Returns:  The abort code of the Package

Return type:  str

GetAbortComment()[¶](#tts.core.report.parser.Package.ParallelPackage.GetAbortComment "Link to this definition")  
Returns:  The abort comment of the Package

Return type:  str

GetAdditionalInfo()[¶](#tts.core.report.parser.Package.ParallelPackage.GetAdditionalInfo "Link to this definition")  
Returns:  The additional info of the Package, if set

Return type:  str | None

GetCallError()[¶](#tts.core.report.parser.Package.ParallelPackage.GetCallError "Link to this definition")  
Returns:  The call error of the Package

Return type:  str

GetComment()[¶](#tts.core.report.parser.Package.ParallelPackage.GetComment "Link to this definition")  
Returns:  Comment of the Package

Return type:  str

GetDescription()[¶](#tts.core.report.parser.Package.ParallelPackage.GetDescription "Link to this definition")  
Returns:  The description of the Package

Return type:  str

GetDuration()[¶](#tts.core.report.parser.Package.ParallelPackage.GetDuration "Link to this definition")  
Returns:  The duration of the Package

Return type:  str or None

GetElementName()[¶](#tts.core.report.parser.Package.ParallelPackage.GetElementName "Link to this definition")  
Returns:  The name of the project component

Return type:  str

GetGlobalConstantsDefinedOnStart()[¶](#tts.core.report.parser.Package.ParallelPackage.GetGlobalConstantsDefinedOnStart "Link to this definition")  
Returns:  The values that the global constants had at the start of the Package execution

Return type:  list[[`Constant`](#tts.core.report.db.Constant.Constant "tts.core.report.db.Constant.Constant (Python class) — Represents a global constant.")]

GetHash()[¶](#tts.core.report.parser.Package.ParallelPackage.GetHash "Link to this definition")  
Returns:  The hash of the Package

Return type:  str or None

GetId()[¶](#tts.core.report.parser.Package.ParallelPackage.GetId "Link to this definition")  
Returns:  The ID of the Package

Return type:  int or None

GetIsTestcase()[¶](#tts.core.report.parser.Package.ParallelPackage.GetIsTestcase "Link to this definition")  
Returns the state of the test case flag.

Returns:  True if test case flag is enabled, otherwise False

Return type:  bool

GetLibraryId()[¶](#tts.core.report.parser.Package.ParallelPackage.GetLibraryId "Link to this definition")  
Returns:  The library ID of the Package

Return type:  str or None

GetLinkedTestManagementIds()[¶](#tts.core.report.parser.Package.ParallelPackage.GetLinkedTestManagementIds "Link to this definition")  
Returns:  The test management IDs which are contained in the revaluation comments

Return type:  list[str]

GetMappings()[¶](#tts.core.report.parser.Package.ParallelPackage.GetMappings "Link to this definition")  
Returns:  The mappings of the Package

Return type:  [`Mappings`](#tts.core.report.parser.Package.Mappings "tts.core.report.parser.Package.Mappings (Python class) — Represents package mappings.")

GetName()[¶](#tts.core.report.parser.Package.ParallelPackage.GetName "Link to this definition")  
Returns:  The name of the Package.

Return type:  str

GetOriginalResult()[¶](#tts.core.report.parser.Package.ParallelPackage.GetOriginalResult "Link to this definition")  
Returns:  The original result verdict of the report item

Return type:  str

GetParameterDescription(*[name](#tts.core.report.parser.Package.ParallelPackage.GetParameterDescription.name "tts.core.report.parser.Package.ParallelPackage.GetParameterDescription.name (Python parameter) — Name of the parameter")*)[¶](#tts.core.report.parser.Package.ParallelPackage.GetParameterDescription "Link to this definition")  
Parameters:  name : str[¶](#tts.core.report.parser.Package.ParallelPackage.GetParameterDescription.name "Permalink to this definition")  
Name of the parameter

Returns:  The description of the specified parameter

Return type:  str

GetParameterInitialValue(*[name](#tts.core.report.parser.Package.ParallelPackage.GetParameterInitialValue.name "tts.core.report.parser.Package.ParallelPackage.GetParameterInitialValue.name (Python parameter) — Name of the parameter")*)[¶](#tts.core.report.parser.Package.ParallelPackage.GetParameterInitialValue "Link to this definition")  
Parameters:  name : str[¶](#tts.core.report.parser.Package.ParallelPackage.GetParameterInitialValue.name "Permalink to this definition")  
Name of the parameter

Returns:  The initial value of the specified parameter.

Return type:  str

GetParameterNames()[¶](#tts.core.report.parser.Package.ParallelPackage.GetParameterNames "Link to this definition")  
Returns:  The names of all parameters

Return type:  list[str]

GetParameterOrigin(*[name](#tts.core.report.parser.Package.ParallelPackage.GetParameterOrigin.name "tts.core.report.parser.Package.ParallelPackage.GetParameterOrigin.name (Python parameter) — Name of the parameter")*)[¶](#tts.core.report.parser.Package.ParallelPackage.GetParameterOrigin "Link to this definition")  
Parameters:  name : str[¶](#tts.core.report.parser.Package.ParallelPackage.GetParameterOrigin.name "Permalink to this definition")  
Name of the parameter

Returns:  The origin of the parameter

Rytpe:  
str

Return type:  str | None

GetParameterValue(*[name](#tts.core.report.parser.Package.ParallelPackage.GetParameterValue.name "tts.core.report.parser.Package.ParallelPackage.GetParameterValue.name (Python parameter) — Name of the parameter")*)[¶](#tts.core.report.parser.Package.ParallelPackage.GetParameterValue "Link to this definition")  
Parameters:  name : str[¶](#tts.core.report.parser.Package.ParallelPackage.GetParameterValue.name "Permalink to this definition")  
Name of the parameter

Returns:  The value of the specified parameter as string representation

Return type:  str

GetPath()[¶](#tts.core.report.parser.Package.ParallelPackage.GetPath "Link to this definition")  
Returns:  The path of the Package

Return type:  str

GetPkgId()[¶](#tts.core.report.parser.Package.ParallelPackage.GetPkgId "Link to this definition")  
Returns:  The ID of the Package

Return type:  int or None

GetRecordings()[¶](#tts.core.report.parser.Package.ParallelPackage.GetRecordings "Link to this definition")  
Returns:  The recordings of the Package

Return type:  [`Recordings`](#tts.core.report.parser.Package.Recordings "tts.core.report.parser.Package.Recordings (Python class) — Represents recordings.")

GetReportItemId()[¶](#tts.core.report.parser.Package.ParallelPackage.GetReportItemId "Link to this definition")  
Returns:  The ID of the report item

Return type:  int

GetResult()[¶](#tts.core.report.parser.Package.ParallelPackage.GetResult "Link to this definition")  
Returns:  The result of the project component

Return type:  str

GetReturnDescription(*[name](#tts.core.report.parser.Package.ParallelPackage.GetReturnDescription "tts.core.report.parser.Package.ParallelPackage.GetReturnDescription.name (Python parameter)")*)[¶](#tts.core.report.parser.Package.ParallelPackage.GetReturnDescription "Link to this definition")  
Returns:  The description of the specified return

Return type:  str | None

GetReturnInitialValue(*[name](#tts.core.report.parser.Package.ParallelPackage.GetReturnInitialValue "tts.core.report.parser.Package.ParallelPackage.GetReturnInitialValue.name (Python parameter)")*)[¶](#tts.core.report.parser.Package.ParallelPackage.GetReturnInitialValue "Link to this definition")  
Returns:  The initial value of the specified return

Return type:  str

GetReturnNames()[¶](#tts.core.report.parser.Package.ParallelPackage.GetReturnNames "Link to this definition")  
Returns:  The names of all returns of the current Package

Return type:  list[str]

GetReturnValue(*[name](#tts.core.report.parser.Package.ParallelPackage.GetReturnValue "tts.core.report.parser.Package.ParallelPackage.GetReturnValue.name (Python parameter)")*)[¶](#tts.core.report.parser.Package.ParallelPackage.GetReturnValue "Link to this definition")  
Returns:  The value of the specified return

Return type:  str

GetRevalComments()[¶](#tts.core.report.parser.Package.ParallelPackage.GetRevalComments "Link to this definition")  
Returns:  The revaluation comments of the current Package

Return type:  list\<[`RevaluationComment`](#tts.core.report.db.ReportItem.RevaluationComment "tts.core.report.db.ReportItem.RevaluationComment (Python class) — The author of the revaluation comment")\>

GetRevalCommentsString()[¶](#tts.core.report.parser.Package.ParallelPackage.GetRevalCommentsString "Link to this definition")  
Gets the revaluation comments of the current Package. The comments are combined to a single string with the pattern “Creator: Comment -> Revaluated result”. If no revaluation comments exists, an empty string is returned.

Returns:  A string representing the combined revaluation comments

Return type:  str

GetRevision()[¶](#tts.core.report.parser.Package.ParallelPackage.GetRevision "Link to this definition")  
Returns:  The revision of the Package

Return type:  str

GetSCMBranch()[¶](#tts.core.report.parser.Package.ParallelPackage.GetSCMBranch "Link to this definition")  
Returns:  The SCM Branch of the Package

Return type:  str or None

GetSCMStatus()[¶](#tts.core.report.parser.Package.ParallelPackage.GetSCMStatus "Link to this definition")  
Returns:  The SCM status of the Package

Return type:  str or None

GetSCMUrl()[¶](#tts.core.report.parser.Package.ParallelPackage.GetSCMUrl "Link to this definition")  
Returns:  The SCM URL of the Package

Return type:  str or None

GetStimulationPackage(*[returnParamSets](#tts.core.report.parser.Package.ParallelPackage.GetStimulationPackage.returnParamSets "tts.core.report.parser.Package.ParallelPackage.GetStimulationPackage.returnParamSets (Python parameter) — Specifies, how to deal with stimulation parameter sets.")=`True`*)[¶](#tts.core.report.parser.Package.ParallelPackage.GetStimulationPackage "Link to this definition")  
This call is only valid for analysis packages and returns the stimulation Package.

Note:  
For older reports (before 2022.2) this method may return None if no trace analysis was executed.

Parameters:  returnParamSets : bool[¶](#tts.core.report.parser.Package.ParallelPackage.GetStimulationPackage.returnParamSets "Permalink to this definition")  
Specifies, how to deal with stimulation parameter sets. If True, the parameter set that has been used to stimulate the execution of the analysis Package is returned.

If False, the stimulation Package itself is returned, which is of type `ParameterizedPackage` for parameterized stimulations.

Returns:  The stimulation Package. The default return value will be of type [`Package`](#tts.core.report.parser.Package.Package "tts.core.report.parser.Package.Package (Python class) — This class represents a Package that was executed individually or called directly from a Project."). If returnParamSets is False, it is possibly also of type `ParameterizedPackage`.

Return type:  [`Package`](#tts.core.report.parser.Package.Package "tts.core.report.parser.Package.Package (Python class) — This class represents a Package that was executed individually or called directly from a Project.") or `ParameterizedPackage`

GetTestCase(*[excludeSubPackages](#tts.core.report.parser.Package.ParallelPackage.GetTestCase.excludeSubPackages "tts.core.report.parser.Package.ParallelPackage.GetTestCase.excludeSubPackages (Python parameter)")=`True`*)[¶](#tts.core.report.parser.Package.ParallelPackage.GetTestCase "Link to this definition")  
Parameters:  excludeSubPackages : bool[¶](#tts.core.report.parser.Package.ParallelPackage.GetTestCase.excludeSubPackages "Permalink to this definition")  

Returns:  The test case of the Package

Return type:  [`TestCase`](#tts.core.report.parser.Package.TestCase "tts.core.report.parser.Package.TestCase (Python class) — Maximum execution level")

GetTestScriptId()[¶](#tts.core.report.parser.Package.ParallelPackage.GetTestScriptId "Link to this definition")  
Returns:  The test script ID, if set

Return type:  str | None

GetTestmanagementId()[¶](#tts.core.report.parser.Package.ParallelPackage.GetTestmanagementId "Link to this definition")  
Returns:  The test management ID of the Package

Return type:  str or None

GetTime()[¶](#tts.core.report.parser.Package.ParallelPackage.GetTime "Link to this definition")  
Returns:  The time of the Package

Return type:  datetime.datetime | None

GetTraceAnalyses()[¶](#tts.core.report.parser.Package.ParallelPackage.GetTraceAnalyses "Link to this definition")  
Returns:  The trace analyses

Return type:  [`TraceAnalyses`](#tts.core.report.parser.Package.TraceAnalyses "tts.core.report.parser.Package.TraceAnalyses (Python class) — The maximum execution level")

GetUserReportData()[¶](#tts.core.report.parser.Package.ParallelPackage.GetUserReportData "Link to this definition")  
Returns:  The user defined report data. The data consists of name and a tuple consisting of value and description.

Return type:  dict[str, tuple[str, str]]

GetVersion()[¶](#tts.core.report.parser.Package.ParallelPackage.GetVersion "Link to this definition")  
Returns:  The version of the Package

Return type:  str

HasAnalysisJobs(*[excludeSubPackages](#tts.core.report.parser.Package.ParallelPackage.HasAnalysisJobs "tts.core.report.parser.Package.ParallelPackage.HasAnalysisJobs.excludeSubPackages (Python parameter)")=`True`*)[¶](#tts.core.report.parser.Package.ParallelPackage.HasAnalysisJobs "Link to this definition")  
Returns:  Indicates whether the Package has analysis jobs

Return type:  bool

HasAttributes()[¶](#tts.core.report.parser.Package.ParallelPackage.HasAttributes "Link to this definition")  
Returns:  True if Package has any attributes, otherwise False

Return type:  bool

HasMappings()[¶](#tts.core.report.parser.Package.ParallelPackage.HasMappings "Link to this definition")  
Returns:  Indicates whether the Package has mappings

Return type:  bool

HasParams()[¶](#tts.core.report.parser.Package.ParallelPackage.HasParams "Link to this definition")  
Returns:  True if Package has any parameters, otherwise False

Return type:  bool

HasRecordings()[¶](#tts.core.report.parser.Package.ParallelPackage.HasRecordings "Link to this definition")  
Returns:  Indicates whether the Package has recordings

Return type:  bool

HasReturnValues()[¶](#tts.core.report.parser.Package.ParallelPackage.HasReturnValues "Link to this definition")  
Returns:  True if Package has any return values, otherwise False

Return type:  bool

HasRevalComments()[¶](#tts.core.report.parser.Package.ParallelPackage.HasRevalComments "Link to this definition")  
Returns:  Indicates whether the current Package has revaluation comments

Return type:  bool

HasTestCase()[¶](#tts.core.report.parser.Package.ParallelPackage.HasTestCase "Link to this definition")  
Returns:  Indicates whether the Package has a test case

Return type:  bool

HasTraceAnalyses()[¶](#tts.core.report.parser.Package.ParallelPackage.HasTraceAnalyses "Link to this definition")  
Returns:  Indicates whether the Package has trace analyses

Return type:  bool

IsAnalysisPackage()[¶](#tts.core.report.parser.Package.ParallelPackage.IsAnalysisPackage "Link to this definition")  
Returns:  True if Package is an analysis Package, otherwise False

Return type:  bool

IsSkipped()[¶](#tts.core.report.parser.Package.ParallelPackage.IsSkipped "Link to this definition")  
Returns:  Indicates whether the current Package was skipped by the user, e.g. by filtering or commenting out.

Return type:  bool

IsStimulationPackage()[¶](#tts.core.report.parser.Package.ParallelPackage.IsStimulationPackage "Link to this definition")  
Returns:  True if Package is a stimulation Package, otherwise False

Return type:  bool

IterAnalysisJobs(*[excludeSubPackages](#tts.core.report.parser.Package.ParallelPackage.IterAnalysisJobs.excludeSubPackages "tts.core.report.parser.Package.ParallelPackage.IterAnalysisJobs.excludeSubPackages (Python parameter) — True when subPackages should be excluded, otherwise False")=`True`*)[¶](#tts.core.report.parser.Package.ParallelPackage.IterAnalysisJobs "Link to this definition")  
Parameters:  excludeSubPackages : bool[¶](#tts.core.report.parser.Package.ParallelPackage.IterAnalysisJobs.excludeSubPackages "Permalink to this definition")  
True when subPackages should be excluded, otherwise False

Returns:  An Iterator for the analysis jobs

Return type:  Iterator[[`AnalysisJobItem`](#tts.core.report.parser.Package.AnalysisJobItem "tts.core.report.parser.Package.AnalysisJobItem (Python class) — The maximum execution level")]

IterAttributes()[¶](#tts.core.report.parser.Package.ParallelPackage.IterAttributes "Link to this definition")  
Returns:  An Iterator for the attributes

Return type:  Iterator[[`Attribute`](#tts.core.report.db.Attribute.Attribute "tts.core.report.db.Attribute.Attribute (Python class) — Represents attributes of a project, package, or test case")]

IterParameterVariables()[¶](#tts.core.report.parser.Package.ParallelPackage.IterParameterVariables "Link to this definition")  
Returns:  An iterator for the parameters

Return type:  Iterator[[`PackageParameterVariable`](#tts.core.report.db.Variable.PackageParameterVariable "tts.core.report.db.Variable.PackageParameterVariable (Python class) — The Variable represents a test case parameter variable used in a Package.")]

IterReturnVariables()[¶](#tts.core.report.parser.Package.ParallelPackage.IterReturnVariables "Link to this definition")  
Gets an iterator for the return variables. Each variable is represented by a [`PackageReturnVariable`](#tts.core.report.db.Variable.PackageReturnVariable "tts.core.report.db.Variable.PackageReturnVariable (Python class) — The Variable represents a return variable used in a Package.") instance containing the value the variable had after the execution of the test case and all analysis jobs. If the variable is written by multiple analysis jobs with different values, the value is set to ‘Inconsistent’.

Return type:  Iterator[[`PackageReturnVariable`](#tts.core.report.db.Variable.PackageReturnVariable "tts.core.report.db.Variable.PackageReturnVariable (Python class) — The Variable represents a return variable used in a Package.")]

IterReturnVariablesAfterTest()[¶](#tts.core.report.parser.Package.ParallelPackage.IterReturnVariablesAfterTest "Link to this definition")  
Gets an iterator for the return variables. Each variable is represented by a [`PackageReturnVariable`](#tts.core.report.db.Variable.PackageReturnVariable "tts.core.report.db.Variable.PackageReturnVariable (Python class) — The Variable represents a return variable used in a Package.") instance containing the value the variable had after the execution of the test case but before the execution of the analysis jobs.

Return type:  Iterator[[`PackageReturnVariable`](#tts.core.report.db.Variable.PackageReturnVariable "tts.core.report.db.Variable.PackageReturnVariable (Python class) — The Variable represents a return variable used in a Package.")]

IterUserComments(*[recursive](#tts.core.report.parser.Package.ParallelPackage.IterUserComments.recursive "tts.core.report.parser.Package.ParallelPackage.IterUserComments.recursive (Python parameter) — If True, also comments of children are included.")=`False`*)[¶](#tts.core.report.parser.Package.ParallelPackage.IterUserComments "Link to this definition")  
Yield all [`ReportItemComment`](#tts.core.report.db.ReportItemComment.ReportItemComment "tts.core.report.db.ReportItemComment.ReportItemComment (Python class) — The author of the comment") of the [`ReportItem`](#tts.core.report.db.ReportItem.ReportItem "tts.core.report.db.ReportItem.ReportItem (Python class) — A report item represents the execution results of one test step. It contains information like test step number, time of execution, type of test step and custom fields. Furthermore additional information on a test step can be stored in so called entity elements being attached to the respective report item (e.g. TableEntity or TextEntity)."). If recursive is True, comments of all children are yielded as well. This can improve performance of reading all report comments significantly.

Parameters:  recursive : bool[¶](#tts.core.report.parser.Package.ParallelPackage.IterUserComments.recursive "Permalink to this definition")  
If True, also comments of children are included.

Type:  recursive: bool

Return type:  Iterator[[`ReportItemComment`](#tts.core.report.db.ReportItemComment.ReportItemComment "tts.core.report.db.ReportItemComment.ReportItemComment (Python class) — The author of the comment")]

GetComponentName()[¶](#tts.core.report.parser.Package.ParallelPackage.GetComponentName "Link to this definition")  
Deprecated since version 2024.1: Use [`GetElementName()`](#tts.core.report.parser.Package.ParallelPackage.GetElementName "tts.core.report.parser.Package.ParallelPackage.GetElementName (Python method) — The name of the project component").

Returns:  The name of the project component

Return type:  str

*class* Recording[¶](#tts.core.report.parser.Package.Recording "Link to this definition")  
Represents a recording.

GetMeasurementListFile()[¶](#tts.core.report.parser.Package.Recording.GetMeasurementListFile "Link to this definition")  
Returns:  The measurement list file name

Return type:  str

GetNumberOfMeasurementListFileSignals()[¶](#tts.core.report.parser.Package.Recording.GetNumberOfMeasurementListFileSignals "Link to this definition")  
Returns:  The number of signals in the measurement file that have been recorded

Return type:  int

GetOrigin()[¶](#tts.core.report.parser.Package.Recording.GetOrigin "Link to this definition")  
Returns the origin, a text representation of the source field.

Returns:  The origin

Return type:  str

GetSignalGroupName()[¶](#tts.core.report.parser.Package.Recording.GetSignalGroupName "Link to this definition")  
Returns:  The signal group name

Return type:  str

GetSource()[¶](#tts.core.report.parser.Package.Recording.GetSource "Link to this definition")  
The source bits. One of the constants SOURCE_RECORDING, SOURCE_TRACEANALYSIS, SOURCE_MANUAL, or SOURCE_TRACEMERGE in combination with the flags SOURCE_FLAG_STIMULATION, SOURCE_FLAG_AUTOGENERATED

Return type:  int

GetSyncDeltaT()[¶](#tts.core.report.parser.Package.Recording.GetSyncDeltaT "Link to this definition")  
Returns the deltaT, calculated by the synchronization, that is applied to the time axis.

Return type:  str

IterMappings()[¶](#tts.core.report.parser.Package.Recording.IterMappings "Link to this definition")  
Returns:  Iterator of mappings

Return type:  generator\<[`Mapping`](#tts.core.report.parser.Package.Mapping "tts.core.report.parser.Package.Mapping (Python class) — Represents a mapping item.")\>

IterSignals()[¶](#tts.core.report.parser.Package.Recording.IterSignals "Link to this definition")  
Returns:  Iterator of signal names

Return type:  generator\<str\>

*class* Recordings[¶](#tts.core.report.parser.Package.Recordings "Link to this definition")  
Represents recordings.

IterRecordings()[¶](#tts.core.report.parser.Package.Recordings.IterRecordings "Link to this definition")  
Returns:  An iterator for all recordnings

Return type:  generator\<[`Recording`](#tts.core.report.parser.Package.Recording "tts.core.report.parser.Package.Recording (Python class) — Represents a recording.")\>

*class* ReportItem[¶](#tts.core.report.parser.Package.ReportItem "Link to this definition")  
Represents a report item.

PPackageReportName[¶](#tts.core.report.parser.Package.ReportItem.PPackageReportName "Link to this definition")  
Returns:  The string for the alternative name field

Return type:  str

GetAbortCode()[¶](#tts.core.report.parser.Package.ReportItem.GetAbortCode "Link to this definition")  
Returns:  The abort code of the report item

Return type:  str

GetAbortComment()[¶](#tts.core.report.parser.Package.ReportItem.GetAbortComment "Link to this definition")  
Returns:  The abort comment of the report item

Return type:  str

GetAbsoluteTimestamp()[¶](#tts.core.report.parser.Package.ReportItem.GetAbsoluteTimestamp "Link to this definition")  
Returns:  The value of the timestamp field

Return type:  float or None

GetAdditionalInfo()[¶](#tts.core.report.parser.Package.ReportItem.GetAdditionalInfo "Link to this definition")  
Returns:  The string for the additional info field

Return type:  str

GetComment()[¶](#tts.core.report.parser.Package.ReportItem.GetComment "Link to this definition")  
Returns:  The string for the comment field

Return type:  str

GetDuration()[¶](#tts.core.report.parser.Package.ReportItem.GetDuration "Link to this definition")  
Returns:  The value of the duration field

Return type:  float | None

GetElementaryResult()[¶](#tts.core.report.parser.Package.ReportItem.GetElementaryResult "Link to this definition")  
Returns:  True if the result is elementary, otherwise False

Return type:  bool

GetExecLevel()[¶](#tts.core.report.parser.Package.ReportItem.GetExecLevel "Link to this definition")  
Returns:  The execution level

Return type:  int

GetId()[¶](#tts.core.report.parser.Package.ReportItem.GetId "Link to this definition")  
Returns:  The ID of the report item

Return type:  int

GetImageKey()[¶](#tts.core.report.parser.Package.ReportItem.GetImageKey "Link to this definition")  
Returns:  The image key

Return type:  int

GetInfo()[¶](#tts.core.report.parser.Package.ReportItem.GetInfo "Link to this definition")  
Depending on the category of the report item the info field corresponds to the following columns in the test report:

- `CAT_TESTCASE`: the value of the `Value` column.

- `CAT_PROJECT`: the value of the `Value` column.

- `CAT_TRACEANALYSIS`: the value of the `Parameter` column.

Returns:  The string for the info field

Return type:  str

GetLabel()[¶](#tts.core.report.parser.Package.ReportItem.GetLabel "Link to this definition")  
Corresponds to the Action/Name column in the test report.

Returns:  The string for the label field

Return type:  str

GetLinkedTestManagementIds()[¶](#tts.core.report.parser.Package.ReportItem.GetLinkedTestManagementIds "Link to this definition")  
Returns:  The test management IDs which are contained in the revaluation comments

Return type:  list\<str\>

GetLoopCycle()[¶](#tts.core.report.parser.Package.ReportItem.GetLoopCycle "Link to this definition")  
Returns:  The loop cycle

Return type:  str or None

GetMappingTargets()[¶](#tts.core.report.parser.Package.ReportItem.GetMappingTargets "Link to this definition")  
Returns:  The mapping targets of the current test step

Return type:  list\<str\>

GetName()[¶](#tts.core.report.parser.Package.ReportItem.GetName "Link to this definition")  
ReportItems of category `CAT_TRACEANALYSIS` use the name field to store the signal binding informations. It corresponds to the `Generic signals`column in the test report. For ReportItems of other categories use [`GetLabel()`](#tts.core.report.parser.Package.ReportItem.GetLabel "tts.core.report.parser.Package.ReportItem.GetLabel (Python method) — Corresponds to the Action/Name column in the test report.") for a briefer representation.

Returns:  The string for the name field

Return type:  str

GetOriginalResult()[¶](#tts.core.report.parser.Package.ReportItem.GetOriginalResult "Link to this definition")  
Returns:  String of the original result field

Return type:  str

GetPackageInfo()[¶](#tts.core.report.parser.Package.ReportItem.GetPackageInfo "Link to this definition")  
Returns:  The package info

Return type:  `Pkg` or None

GetPackageReportName()[¶](#tts.core.report.parser.Package.ReportItem.GetPackageReportName "Link to this definition")  
Returns:  The string for the alternative name field

Return type:  str

GetPackageScmInfo()[¶](#tts.core.report.parser.Package.ReportItem.GetPackageScmInfo "Link to this definition")  
Returns:  Information about the SCM

Return type:  tuple[str, str, str] | None

GetParentId()[¶](#tts.core.report.parser.Package.ReportItem.GetParentId "Link to this definition")  
Returns:  The ID of the parent report item

Return type:  int

GetPos()[¶](#tts.core.report.parser.Package.ReportItem.GetPos "Link to this definition")  
Returns:  The position in the report

Return type:  int

GetRelativeRealtime()[¶](#tts.core.report.parser.Package.ReportItem.GetRelativeRealtime "Link to this definition")  
Returns:  The value of the relative_realtime field

Return type:  float or None

GetRelativeTimestamp()[¶](#tts.core.report.parser.Package.ReportItem.GetRelativeTimestamp "Link to this definition")  
Returns:  The value of the timestamp_relative field

Return type:  float or None

GetReportItemId()[¶](#tts.core.report.parser.Package.ReportItem.GetReportItemId "Link to this definition")  
Returns:  The ID of the report item

Return type:  int

GetResult()[¶](#tts.core.report.parser.Package.ReportItem.GetResult "Link to this definition")  
Returns:  The string for the result field

Return type:  str or None

GetRevalComments()[¶](#tts.core.report.parser.Package.ReportItem.GetRevalComments "Link to this definition")  
Returns:  The revaluation comments of the current report item

Return type:  list\< [`RevaluationComment`](#tts.core.report.db.ReportItem.RevaluationComment "tts.core.report.db.ReportItem.RevaluationComment (Python class) — The author of the revaluation comment") \>

GetRevalCommentsString()[¶](#tts.core.report.parser.Package.ReportItem.GetRevalCommentsString "Link to this definition")  
Gets the revaluation comments of the current report item. The comments are combined to a single string with the pattern “Creator: Comment -> Revaluated result”. If no revaluation comments exists, an empty string is returned.

Returns:  A string representing the combined revaluation comments

Return type:  str

GetSrc()[¶](#tts.core.report.parser.Package.ReportItem.GetSrc "Link to this definition")  
Returns:  The name of the source report item

Return type:  str or None

GetSrcCategory()[¶](#tts.core.report.parser.Package.ReportItem.GetSrcCategory "Link to this definition")  
Returns:  The category of the source, one of

- `CAT_TESTCASE`

- `CAT_PROJECT`

- `CAT_TRACEANALYSIS`

Return type:  int or None

GetSrcIndex()[¶](#tts.core.report.parser.Package.ReportItem.GetSrcIndex "Link to this definition")  
Returns:  The string for the index field

Return type:  str

GetSrcSubType()[¶](#tts.core.report.parser.Package.ReportItem.GetSrcSubType "Link to this definition")  
Returns:  UUID of a specific Utility

Return type:  str or None

GetSrcType()[¶](#tts.core.report.parser.Package.ReportItem.GetSrcType "Link to this definition")  
Returns the type of the ReportItem, e.g.

- ‘PACKAGE’

- ‘PROJECT’

- ‘CALCULATION’

- ‘TRACE-ANALYSIS’

- ‘EPISODE’

- ‘TRACESTEP’

- ‘TRIGGERBLOCK’

- ‘PLOTITEM’

Returns:  The type of the ReportItem

Return type:  str or None

GetTargetValue()[¶](#tts.core.report.parser.Package.ReportItem.GetTargetValue "Link to this definition")  
Corresponds to the `Expected value`column in the test report.

Returns:  The string for the target value field

Return type:  str

GetUndocumentedChild()[¶](#tts.core.report.parser.Package.ReportItem.GetUndocumentedChild "Link to this definition")  
Returns:  True if the item has undocumented children, otherwise False

Return type:  bool

HasEntities()[¶](#tts.core.report.parser.Package.ReportItem.HasEntities "Link to this definition")  
Returns:  Indicates weather the report item has report entities

Return type:  bool

HasRevalComments()[¶](#tts.core.report.parser.Package.ReportItem.HasRevalComments "Link to this definition")  
Returns:  True when the current report item has revaluation comments, otherwise False

Return type:  bool

HasTag(*[tagName](#tts.core.report.parser.Package.ReportItem.HasTag.tagName "tts.core.report.parser.Package.ReportItem.HasTag.tagName (Python parameter) — The tag to check for")*)[¶](#tts.core.report.parser.Package.ReportItem.HasTag "Link to this definition")  
Returns whether this report item has set the specified tag.

Parameters:  tagName : str[¶](#tts.core.report.parser.Package.ReportItem.HasTag.tagName "Permalink to this definition")  
The tag to check for

Returns:  True, if the tag is set, otherwise False

Return type:  bool

InitFromParentId(*[dbCur](#tts.core.report.parser.Package.ReportItem.InitFromParentId "tts.core.report.parser.Package.ReportItem.InitFromParentId.dbCur (Python parameter)")*, *[parentId](#tts.core.report.parser.Package.ReportItem.InitFromParentId.parentId "tts.core.report.parser.Package.ReportItem.InitFromParentId.parentId (Python parameter) — ID of the parent item (None for top level items of the main thread).")*, *[parentThreadId](#tts.core.report.parser.Package.ReportItem.InitFromParentId.parentThreadId "tts.core.report.parser.Package.ReportItem.InitFromParentId.parentThreadId (Python parameter) — Thread ID of the parent item if the information is known.")=`None`*)[¶](#tts.core.report.parser.Package.ReportItem.InitFromParentId "Link to this definition")  
See [`InitFromParentItem()`](#tts.core.report.parser.Package.ReportItem.InitFromParentItem "tts.core.report.parser.Package.ReportItem.InitFromParentItem (Python method) — Init new report item as port of the children list of its parent item indicated by parentId/parent. Attribute threadId, pos and blkEnd are automatically determined and assigned. The new item's threadId depends on whether the parent item is marked the creator of a sub thread (see creator_id of thread table) or not. In the first case the new item is assigned the sub thread id. In the other case the new item inherits its parent's thread id. If parentId is None the new item becomes part of the main thread.").

Parameters:  parentId : int | None[¶](#tts.core.report.parser.Package.ReportItem.InitFromParentId.parentId "Permalink to this definition")  
ID of the parent item (None for top level items of the main thread).

parentThreadId : int | None[¶](#tts.core.report.parser.Package.ReportItem.InitFromParentId.parentThreadId "Permalink to this definition")  
Thread ID of the parent item if the information is known. Otherwise, it will be determined using the report DB.

InitFromParentItem(*[dbCur](#tts.core.report.parser.Package.ReportItem.InitFromParentItem "tts.core.report.parser.Package.ReportItem.InitFromParentItem.dbCur (Python parameter)")*, *[parent](#tts.core.report.parser.Package.ReportItem.InitFromParentItem.parent "tts.core.report.parser.Package.ReportItem.InitFromParentItem.parent (Python parameter) — The parent item referenced by parentId. This parameter exists for performance reasons only, avoiding repeatedly reload of the parent item.")*)[¶](#tts.core.report.parser.Package.ReportItem.InitFromParentItem "Link to this definition")  
Init new report item as port of the children list of its parent item indicated by parentId/parent. Attribute threadId, pos and blkEnd are automatically determined and assigned. The new item’s threadId depends on whether the parent item is marked the creator of a sub thread (see creator_id of thread table) or not. In the first case the new item is assigned the sub thread id. In the other case the new item inherits its parent’s thread id. If parentId is None the new item becomes part of the main thread.

Parameters:  parent : [ReportItem](#tts.core.report.parser.Package.ReportItem "tts.core.report.parser.Package.ReportItem (Python class) — Represents a report item.")[¶](#tts.core.report.parser.Package.ReportItem.InitFromParentItem.parent "Permalink to this definition")  
The parent item referenced by parentId. This parameter exists for performance reasons only, avoiding repeatedly reload of the parent item. If cachedParentItem.reportItemId does not match parentId the passed item will be ignored and the proper parent item will be fetched from the database.

IsSkipped()[¶](#tts.core.report.parser.Package.ReportItem.IsSkipped "Link to this definition")  
Returns:  True when the report item was skipped by the user, e.g. by filtering or commenting out, otherwise False

Return type:  bool

IterEntities()[¶](#tts.core.report.parser.Package.ReportItem.IterEntities "Link to this definition")  
Returns:  An iterator for the entities of report item

Return type:  generator\<[`Entity`](#tts.core.report.db.Entity.Entity "tts.core.report.db.Entity.Entity (Python class) — The ID of the entity")\>

IterTags()[¶](#tts.core.report.parser.Package.ReportItem.IterTags "Link to this definition")  
Returns:  An iterator for all tag names used for the report item

Return type:  generator\<str\>

IterUserComments(*[recursive](#tts.core.report.parser.Package.ReportItem.IterUserComments.recursive "tts.core.report.parser.Package.ReportItem.IterUserComments.recursive (Python parameter) — If True, also comments of children are included.")=`False`*)[¶](#tts.core.report.parser.Package.ReportItem.IterUserComments "Link to this definition")  
Yield all [`ReportItemComment`](#tts.core.report.db.ReportItemComment.ReportItemComment "tts.core.report.db.ReportItemComment.ReportItemComment (Python class) — The author of the comment") of the [`ReportItem`](#tts.core.report.db.ReportItem.ReportItem "tts.core.report.db.ReportItem.ReportItem (Python class) — A report item represents the execution results of one test step. It contains information like test step number, time of execution, type of test step and custom fields. Furthermore additional information on a test step can be stored in so called entity elements being attached to the respective report item (e.g. TableEntity or TextEntity)."). If recursive is True, comments of all children are yielded as well. This can improve performance of reading all report comments significantly.

Parameters:  recursive : bool[¶](#tts.core.report.parser.Package.ReportItem.IterUserComments.recursive "Permalink to this definition")  
If True, also comments of children are included.

Type:  recursive: bool

Return type:  Iterator[[`ReportItemComment`](#tts.core.report.db.ReportItemComment.ReportItemComment "tts.core.report.db.ReportItemComment.ReportItemComment (Python class) — The author of the comment")]

SetPackageReportName(*[value](#tts.core.report.parser.Package.ReportItem.SetPackageReportName.value "tts.core.report.parser.Package.ReportItem.SetPackageReportName.value (Python parameter) — The string for the alternative name field")*)[¶](#tts.core.report.parser.Package.ReportItem.SetPackageReportName "Link to this definition")  
Parameters:  value : str[¶](#tts.core.report.parser.Package.ReportItem.SetPackageReportName.value "Permalink to this definition")  
The string for the alternative name field

GetActivity()[¶](#tts.core.report.parser.Package.ReportItem.GetActivity "Link to this definition")  
Deprecated since version 6.4: Name and Activity are to be replaced by Label

Returns:  The string for the activity field

Return type:  str

*class* TestCase[¶](#tts.core.report.parser.Package.TestCase "Link to this definition")  
GetMaxExecLevel()[¶](#tts.core.report.parser.Package.TestCase.GetMaxExecLevel "Link to this definition")  
Returns:  Maximum execution level

Return type:  int

GetResult()[¶](#tts.core.report.parser.Package.TestCase.GetResult "Link to this definition")  
Returns:  The string for the result of the test case.

Return type:  str

HasData()[¶](#tts.core.report.parser.Package.TestCase.HasData "Link to this definition")  
Returns:  True when test case has data, otherwise False

Return type:  bool

IterTestSteps()[¶](#tts.core.report.parser.Package.TestCase.IterTestSteps "Link to this definition")  
Returns:  The report items of the test steps

Return type:  generator\<[`ReportItem`](#tts.core.report.parser.Package.ReportItem "tts.core.report.parser.Package.ReportItem (Python class) — Represents a report item.")\>

*class* TraceAnalyses[¶](#tts.core.report.parser.Package.TraceAnalyses "Link to this definition")  
GetMaxExecLevel()[¶](#tts.core.report.parser.Package.TraceAnalyses.GetMaxExecLevel "Link to this definition")  
Returns:  The maximum execution level

Return type:  int

HasData()[¶](#tts.core.report.parser.Package.TraceAnalyses.HasData "Link to this definition")  
Returns:  True when trace analyses have data, otherwise False

Return type:  bool

IterTraceItems(*[excludeRefTa](#tts.core.report.parser.Package.TraceAnalyses.IterTraceItems "tts.core.report.parser.Package.TraceAnalyses.IterTraceItems.excludeRefTa (Python parameter)")=`False`*)[¶](#tts.core.report.parser.Package.TraceAnalyses.IterTraceItems "Link to this definition")  
Returns:  An iterator for all trace items

Return type:  generator\<[`ReportItem`](#tts.core.report.db.ReportItem.ReportItem "tts.core.report.db.ReportItem.ReportItem (Python class) — A report item represents the execution results of one test step. It contains information like test step number, time of execution, type of test step and custom fields. Furthermore additional information on a test step can be stored in so called entity elements being attached to the respective report item (e.g. TableEntity or TextEntity).")\>

## ProjectElements[¶](#module-tts.core.report.parser.ProjectElement "Link to this heading")

*class* ConfigChange[¶](#tts.core.report.parser.ProjectElement.ConfigChange "Link to this definition")  
Represents a configuration change report item.

GetAdditionalInfo()[¶](#tts.core.report.parser.ProjectElement.ConfigChange.GetAdditionalInfo "Link to this definition")  
Returns:  The additional info of the ReportItem

Return type:  str

GetComment()[¶](#tts.core.report.parser.ProjectElement.ConfigChange.GetComment "Link to this definition")  
Returns:  The comment of the ReportItem

Return type:  str

GetDuration()[¶](#tts.core.report.parser.ProjectElement.ConfigChange.GetDuration "Link to this definition")  
Returns:  The duration of the project component

Return type:  str

GetElementName()[¶](#tts.core.report.parser.ProjectElement.ConfigChange.GetElementName "Link to this definition")  
Returns:  The name of the project component

Return type:  str

GetName()[¶](#tts.core.report.parser.ProjectElement.ConfigChange.GetName "Link to this definition")  
Returns:  The name of the project component

Return type:  str

GetOriginalResult()[¶](#tts.core.report.parser.ProjectElement.ConfigChange.GetOriginalResult "Link to this definition")  
Returns:  The original result of the project component

Return type:  str

GetReportItemId()[¶](#tts.core.report.parser.ProjectElement.ConfigChange.GetReportItemId "Link to this definition")  
Returns:  The ID of the report item

Return type:  int

GetResult()[¶](#tts.core.report.parser.ProjectElement.ConfigChange.GetResult "Link to this definition")  
Returns:  The result of the project component

Return type:  str

GetSrcType()[¶](#tts.core.report.parser.ProjectElement.ConfigChange.GetSrcType "Link to this definition")  
Returns the type of the ReportItem, e.g.

- ‘PACKAGE’

- ‘PROJECT’

- ‘CALCULATION’

- ‘TRACE-ANALYSIS’

- ‘EPISODE’

- ‘TRACESTEP’

- ‘TRIGGERBLOCK’

- ‘PLOTITEM’

Returns:  The type of the ReportItem

Return type:  str

GetStatistic()[¶](#tts.core.report.parser.ProjectElement.ConfigChange.GetStatistic "Link to this definition")  
Returns:  The statistic of the ReportItem

Return type:  [`ProjectElementStatistic`](#tts.core.report.parser.ProjectElement.ProjectElementStatistic "tts.core.report.parser.ProjectElement.ProjectElementStatistic (Python class) — Represents the project element statistic.")

GetTestBenchConfiguration()[¶](#tts.core.report.parser.ProjectElement.ConfigChange.GetTestBenchConfiguration "Link to this definition")  
Returns:  The tbc which is used in the configuration

Return type:  [`TestBenchConfiguration`](#tts.core.report.parser.Configuration.TestBenchConfiguration "tts.core.report.parser.Configuration.TestBenchConfiguration (Python class) — The TestBenchConfiguration represents information about a test bench configuration.") | None

GetTestConfiguration()[¶](#tts.core.report.parser.ProjectElement.ConfigChange.GetTestConfiguration "Link to this definition")  
Returns:  The tcf which is used in the configuration

Return type:  [`TestConfiguration`](#tts.core.report.parser.Configuration.TestConfiguration "tts.core.report.parser.Configuration.TestConfiguration (Python class) — The Tcf represents information about a test configuration.") | None

GetTime()[¶](#tts.core.report.parser.ProjectElement.ConfigChange.GetTime "Link to this definition")  
Returns:  The time of the ReportItem

Return type:  datetime.datetime

HasTestBenchConfiguration()[¶](#tts.core.report.parser.ProjectElement.ConfigChange.HasTestBenchConfiguration "Link to this definition")  
Returns:  True if the configuration has a tbc, otherwise False

Return type:  bool

HasTestConfiguration()[¶](#tts.core.report.parser.ProjectElement.ConfigChange.HasTestConfiguration "Link to this definition")  
Returns:  True if the configuration has a tcf, otherwise False

Return type:  bool

IsSkipped()[¶](#tts.core.report.parser.ProjectElement.ConfigChange.IsSkipped "Link to this definition")  
Returns:  True if the current ReportItem has not been executed by user definition (for example by filtering or commenting out).

Return type:  bool

IterItems(*[ignoreProjectViewFilter](#tts.core.report.parser.ProjectElement.ConfigChange.IterItems "tts.core.report.parser.ProjectElement.ConfigChange.IterItems.ignoreProjectViewFilter (Python parameter)")=`False`*)[¶](#tts.core.report.parser.ProjectElement.ConfigChange.IterItems "Link to this definition")  
Returns:  The [`Project`](#tts.core.report.parser.ProjectElement.Project "tts.core.report.parser.ProjectElement.Project (Python class) — Represents a Project report item.") or its elements of type [`ProjectElement`](#tts.core.report.parser.ProjectElement.ProjectElement "tts.core.report.parser.ProjectElement.ProjectElement (Python class) — The additional info of the ReportItem") or [`Package`](#tts.core.report.parser.Package.Package "tts.core.report.parser.Package.Package (Python class) — This class represents a Package that was executed individually or called directly from a Project.").

Return type:  [`Project`](#tts.core.report.parser.ProjectElement.Project "tts.core.report.parser.ProjectElement.Project (Python class) — Represents a Project report item.") or [`ProjectElement`](#tts.core.report.parser.ProjectElement.ProjectElement "tts.core.report.parser.ProjectElement.ProjectElement (Python class) — The additional info of the ReportItem") or [`Package`](#tts.core.report.parser.Package.Package "tts.core.report.parser.Package.Package (Python class) — This class represents a Package that was executed individually or called directly from a Project.")

IterUserComments(*[recursive](#tts.core.report.parser.ProjectElement.ConfigChange.IterUserComments.recursive "tts.core.report.parser.ProjectElement.ConfigChange.IterUserComments.recursive (Python parameter) — If True, also comments of children are included.")=`False`*)[¶](#tts.core.report.parser.ProjectElement.ConfigChange.IterUserComments "Link to this definition")  
Yield all [`ReportItemComment`](#tts.core.report.db.ReportItemComment.ReportItemComment "tts.core.report.db.ReportItemComment.ReportItemComment (Python class) — The author of the comment") of the [`ReportItem`](#tts.core.report.db.ReportItem.ReportItem "tts.core.report.db.ReportItem.ReportItem (Python class) — A report item represents the execution results of one test step. It contains information like test step number, time of execution, type of test step and custom fields. Furthermore additional information on a test step can be stored in so called entity elements being attached to the respective report item (e.g. TableEntity or TextEntity)."). If recursive is True, comments of all children are yielded as well. This can improve performance of reading all report comments significantly.

Parameters:  recursive : bool[¶](#tts.core.report.parser.ProjectElement.ConfigChange.IterUserComments.recursive "Permalink to this definition")  
If True, also comments of children are included.

Type:  recursive: bool

Return type:  Iterator[[`ReportItemComment`](#tts.core.report.db.ReportItemComment.ReportItemComment "tts.core.report.db.ReportItemComment.ReportItemComment (Python class) — The author of the comment")]

*class* Project[¶](#tts.core.report.parser.ProjectElement.Project "Link to this definition")  
Represents a Project report item.

PLibraryId[¶](#tts.core.report.parser.ProjectElement.Project.PLibraryId "Link to this definition")  
Returns:  The library ID of the Package

Return type:  str or None

GetAdditionalInfo()[¶](#tts.core.report.parser.ProjectElement.Project.GetAdditionalInfo "Link to this definition")  
Returns:  The additional info of the ReportItem

Return type:  str

GetComment()[¶](#tts.core.report.parser.ProjectElement.Project.GetComment "Link to this definition")  
Returns:  The comment of the project element

Return type:  str

GetDuration()[¶](#tts.core.report.parser.ProjectElement.Project.GetDuration "Link to this definition")  
Returns:  The duration of the project component

Return type:  str

GetElementName()[¶](#tts.core.report.parser.ProjectElement.Project.GetElementName "Link to this definition")  
Returns:  The name of the project component

Return type:  str

GetLibraryId()[¶](#tts.core.report.parser.ProjectElement.Project.GetLibraryId "Link to this definition")  
Returns:  The library ID of the Package

Return type:  str or None

GetName()[¶](#tts.core.report.parser.ProjectElement.Project.GetName "Link to this definition")  
Returns:  The name of the project

Return type:  str

GetOriginalResult()[¶](#tts.core.report.parser.ProjectElement.Project.GetOriginalResult "Link to this definition")  
Returns:  The original result of the project component

Return type:  str

GetPrjCompName()[¶](#tts.core.report.parser.ProjectElement.Project.GetPrjCompName "Link to this definition")  
Returns:  The name of the project element

Return type:  str

GetPrjId()[¶](#tts.core.report.parser.ProjectElement.Project.GetPrjId "Link to this definition")  
Returns:  The project ID

Return type:  int or None

GetReportItemId()[¶](#tts.core.report.parser.ProjectElement.Project.GetReportItemId "Link to this definition")  
Returns:  The ID of the report item

Return type:  int

GetResult()[¶](#tts.core.report.parser.ProjectElement.Project.GetResult "Link to this definition")  
Returns:  The result of the project component

Return type:  str

GetSrcType()[¶](#tts.core.report.parser.ProjectElement.Project.GetSrcType "Link to this definition")  
Returns the type of the ReportItem, e.g.

- ‘PACKAGE’

- ‘PROJECT’

- ‘CALCULATION’

- ‘TRACE-ANALYSIS’

- ‘EPISODE’

- ‘TRACESTEP’

- ‘TRIGGERBLOCK’

- ‘PLOTITEM’

Returns:  The type of the ReportItem

Return type:  str

GetStatistic()[¶](#tts.core.report.parser.ProjectElement.Project.GetStatistic "Link to this definition")  
Returns:  The statistic of the ReportItem

Return type:  [`ProjectElementStatistic`](#tts.core.report.parser.ProjectElement.ProjectElementStatistic "tts.core.report.parser.ProjectElement.ProjectElementStatistic (Python class) — Represents the project element statistic.")

GetTestManagementId()[¶](#tts.core.report.parser.ProjectElement.Project.GetTestManagementId "Link to this definition")  
Returns:  The test management ID

Return type:  str

GetTime()[¶](#tts.core.report.parser.ProjectElement.Project.GetTime "Link to this definition")  
Returns:  The time of the ReportItem

Return type:  datetime.datetime

HasAttributes()[¶](#tts.core.report.parser.ProjectElement.Project.HasAttributes "Link to this definition")  
Returns:  True when the project has attributes, otherwise False

Return type:  bool

IsSkipped()[¶](#tts.core.report.parser.ProjectElement.Project.IsSkipped "Link to this definition")  
Returns:  True if the current ReportItem has not been executed by user definition (for example by filtering or commenting out).

Return type:  bool

IterAttributes()[¶](#tts.core.report.parser.ProjectElement.Project.IterAttributes "Link to this definition")  
Returns:  Iterator for the attributes of the project

Return type:  Iterator[[`Attribute`](#tts.core.report.db.Attribute.Attribute "tts.core.report.db.Attribute.Attribute (Python class) — Represents attributes of a project, package, or test case")]

IterItems(*[ignoreProjectViewFilter](#tts.core.report.parser.ProjectElement.Project.IterItems "tts.core.report.parser.ProjectElement.Project.IterItems.ignoreProjectViewFilter (Python parameter)")=`False`*)[¶](#tts.core.report.parser.ProjectElement.Project.IterItems "Link to this definition")  
Returns:  The [`Project`](#tts.core.report.parser.ProjectElement.Project "tts.core.report.parser.ProjectElement.Project (Python class) — Represents a Project report item.") or its elements of type [`ProjectElement`](#tts.core.report.parser.ProjectElement.ProjectElement "tts.core.report.parser.ProjectElement.ProjectElement (Python class) — The additional info of the ReportItem") or [`Package`](#tts.core.report.parser.Package.Package "tts.core.report.parser.Package.Package (Python class) — This class represents a Package that was executed individually or called directly from a Project.").

Return type:  [`Project`](#tts.core.report.parser.ProjectElement.Project "tts.core.report.parser.ProjectElement.Project (Python class) — Represents a Project report item.") or [`ProjectElement`](#tts.core.report.parser.ProjectElement.ProjectElement "tts.core.report.parser.ProjectElement.ProjectElement (Python class) — The additional info of the ReportItem") or [`Package`](#tts.core.report.parser.Package.Package "tts.core.report.parser.Package.Package (Python class) — This class represents a Package that was executed individually or called directly from a Project.")

IterUserComments(*[recursive](#tts.core.report.parser.ProjectElement.Project.IterUserComments.recursive "tts.core.report.parser.ProjectElement.Project.IterUserComments.recursive (Python parameter) — If True, also comments of children are included.")=`False`*)[¶](#tts.core.report.parser.ProjectElement.Project.IterUserComments "Link to this definition")  
Yield all [`ReportItemComment`](#tts.core.report.db.ReportItemComment.ReportItemComment "tts.core.report.db.ReportItemComment.ReportItemComment (Python class) — The author of the comment") of the [`ReportItem`](#tts.core.report.db.ReportItem.ReportItem "tts.core.report.db.ReportItem.ReportItem (Python class) — A report item represents the execution results of one test step. It contains information like test step number, time of execution, type of test step and custom fields. Furthermore additional information on a test step can be stored in so called entity elements being attached to the respective report item (e.g. TableEntity or TextEntity)."). If recursive is True, comments of all children are yielded as well. This can improve performance of reading all report comments significantly.

Parameters:  recursive : bool[¶](#tts.core.report.parser.ProjectElement.Project.IterUserComments.recursive "Permalink to this definition")  
If True, also comments of children are included.

Type:  recursive: bool

Return type:  Iterator[[`ReportItemComment`](#tts.core.report.db.ReportItemComment.ReportItemComment "tts.core.report.db.ReportItemComment.ReportItemComment (Python class) — The author of the comment")]

*class* ProjectElement[¶](#tts.core.report.parser.ProjectElement.ProjectElement "Link to this definition")  

GetAdditionalInfo()[¶](#tts.core.report.parser.ProjectElement.ProjectElement.GetAdditionalInfo "Link to this definition")  
Returns:  The additional info of the ReportItem

Return type:  str

GetComment()[¶](#tts.core.report.parser.ProjectElement.ProjectElement.GetComment "Link to this definition")  
Returns:  The comment of the ReportItem

Return type:  str

GetDuration()[¶](#tts.core.report.parser.ProjectElement.ProjectElement.GetDuration "Link to this definition")  
Returns:  The duration of the project component

Return type:  str

GetElementName()[¶](#tts.core.report.parser.ProjectElement.ProjectElement.GetElementName "Link to this definition")  
Returns:  The name of the project component

Return type:  str

GetName()[¶](#tts.core.report.parser.ProjectElement.ProjectElement.GetName "Link to this definition")  
Returns:  The name of the project component

Return type:  str

GetOriginalResult()[¶](#tts.core.report.parser.ProjectElement.ProjectElement.GetOriginalResult "Link to this definition")  
Returns:  The original result of the project component

Return type:  str

GetReportItemId()[¶](#tts.core.report.parser.ProjectElement.ProjectElement.GetReportItemId "Link to this definition")  
Returns:  The ID of the report item

Return type:  int

GetResult()[¶](#tts.core.report.parser.ProjectElement.ProjectElement.GetResult "Link to this definition")  
Returns:  The result of the project component

Return type:  str

GetSrcType()[¶](#tts.core.report.parser.ProjectElement.ProjectElement.GetSrcType "Link to this definition")  
Returns the type of the ReportItem, e.g.

- ‘PACKAGE’

- ‘PROJECT’

- ‘CALCULATION’

- ‘TRACE-ANALYSIS’

- ‘EPISODE’

- ‘TRACESTEP’

- ‘TRIGGERBLOCK’

- ‘PLOTITEM’

Returns:  The type of the ReportItem

Return type:  str

GetStatistic()[¶](#tts.core.report.parser.ProjectElement.ProjectElement.GetStatistic "Link to this definition")  
Returns:  The statistic of the ReportItem

Return type:  [`ProjectElementStatistic`](#tts.core.report.parser.ProjectElement.ProjectElementStatistic "tts.core.report.parser.ProjectElement.ProjectElementStatistic (Python class) — Represents the project element statistic.")

GetTime()[¶](#tts.core.report.parser.ProjectElement.ProjectElement.GetTime "Link to this definition")  
Returns:  The time of the ReportItem

Return type:  datetime.datetime

IsSkipped()[¶](#tts.core.report.parser.ProjectElement.ProjectElement.IsSkipped "Link to this definition")  
Returns:  True if the current ReportItem has not been executed by user definition (for example by filtering or commenting out).

Return type:  bool

IterItems(*[ignoreProjectViewFilter](#tts.core.report.parser.ProjectElement.ProjectElement.IterItems "tts.core.report.parser.ProjectElement.ProjectElement.IterItems.ignoreProjectViewFilter (Python parameter)")=`False`*)[¶](#tts.core.report.parser.ProjectElement.ProjectElement.IterItems "Link to this definition")  
Returns:  The [`Project`](#tts.core.report.parser.ProjectElement.Project "tts.core.report.parser.ProjectElement.Project (Python class) — Represents a Project report item.") or its elements of type [`ProjectElement`](#tts.core.report.parser.ProjectElement.ProjectElement "tts.core.report.parser.ProjectElement.ProjectElement (Python class) — The additional info of the ReportItem") or [`Package`](#tts.core.report.parser.Package.Package "tts.core.report.parser.Package.Package (Python class) — This class represents a Package that was executed individually or called directly from a Project.").

Return type:  [`Project`](#tts.core.report.parser.ProjectElement.Project "tts.core.report.parser.ProjectElement.Project (Python class) — Represents a Project report item.") or [`ProjectElement`](#tts.core.report.parser.ProjectElement.ProjectElement "tts.core.report.parser.ProjectElement.ProjectElement (Python class) — The additional info of the ReportItem") or [`Package`](#tts.core.report.parser.Package.Package "tts.core.report.parser.Package.Package (Python class) — This class represents a Package that was executed individually or called directly from a Project.")

IterUserComments(*[recursive](#tts.core.report.parser.ProjectElement.ProjectElement.IterUserComments.recursive "tts.core.report.parser.ProjectElement.ProjectElement.IterUserComments.recursive (Python parameter) — If True, also comments of children are included.")=`False`*)[¶](#tts.core.report.parser.ProjectElement.ProjectElement.IterUserComments "Link to this definition")  
Yield all [`ReportItemComment`](#tts.core.report.db.ReportItemComment.ReportItemComment "tts.core.report.db.ReportItemComment.ReportItemComment (Python class) — The author of the comment") of the [`ReportItem`](#tts.core.report.db.ReportItem.ReportItem "tts.core.report.db.ReportItem.ReportItem (Python class) — A report item represents the execution results of one test step. It contains information like test step number, time of execution, type of test step and custom fields. Furthermore additional information on a test step can be stored in so called entity elements being attached to the respective report item (e.g. TableEntity or TextEntity)."). If recursive is True, comments of all children are yielded as well. This can improve performance of reading all report comments significantly.

Parameters:  recursive : bool[¶](#tts.core.report.parser.ProjectElement.ProjectElement.IterUserComments.recursive "Permalink to this definition")  
If True, also comments of children are included.

Type:  recursive: bool

Return type:  Iterator[[`ReportItemComment`](#tts.core.report.db.ReportItemComment.ReportItemComment "tts.core.report.db.ReportItemComment.ReportItemComment (Python class) — The author of the comment")]

## ReportItems[¶](#reportitems "Link to this heading")

*class* ReportItem[¶](#tts.core.report.db.ReportItem.ReportItem "Link to this definition")  
A report item represents the execution results of one test step. It contains information like test step number, time of execution, type of test step and custom fields. Furthermore additional information on a test step can be stored in so called entity elements being attached to the respective report item (e.g. [`TableEntity`](#tts.core.report.db.TableEntity.TableEntity "tts.core.report.db.TableEntity.TableEntity (Python class) — Represents a table.") or [`TextEntity`](#tts.core.report.db.TextEntity.TextEntity "tts.core.report.db.TextEntity.TextEntity (Python class) — Represents a custom text.")).

Class var CAT_TESTCASE:  
1

Class var CAT_PROJECT:  
2

Class var CAT_TRACEANALYSIS:  
3

GetAbortCode()[¶](#tts.core.report.db.ReportItem.ReportItem.GetAbortCode "Link to this definition")  
Returns:  The abort code of the report item

Return type:  str

GetAbortComment()[¶](#tts.core.report.db.ReportItem.ReportItem.GetAbortComment "Link to this definition")  
Returns:  The abort comment of the report item

Return type:  str

GetAbsoluteTimestamp()[¶](#tts.core.report.db.ReportItem.ReportItem.GetAbsoluteTimestamp "Link to this definition")  
Returns:  The value of the timestamp field

Return type:  float or None

GetAdditionalInfo()[¶](#tts.core.report.db.ReportItem.ReportItem.GetAdditionalInfo "Link to this definition")  
Returns:  The string for the additional info field

Return type:  str

GetComment()[¶](#tts.core.report.db.ReportItem.ReportItem.GetComment "Link to this definition")  
Returns:  The string for the comment field

Return type:  str

GetDuration()[¶](#tts.core.report.db.ReportItem.ReportItem.GetDuration "Link to this definition")  
Returns:  The value of the duration field

Return type:  float | None

GetElementaryResult()[¶](#tts.core.report.db.ReportItem.ReportItem.GetElementaryResult "Link to this definition")  
Returns:  True if the result is elementary, otherwise False

Return type:  bool

GetExecLevel()[¶](#tts.core.report.db.ReportItem.ReportItem.GetExecLevel "Link to this definition")  
Returns:  The execution level

Return type:  int

GetId()[¶](#tts.core.report.db.ReportItem.ReportItem.GetId "Link to this definition")  
Returns:  The ID of the report item

Return type:  int

GetImageKey()[¶](#tts.core.report.db.ReportItem.ReportItem.GetImageKey "Link to this definition")  
Returns:  The image key

Return type:  int

GetInfo()[¶](#tts.core.report.db.ReportItem.ReportItem.GetInfo "Link to this definition")  
Depending on the category of the report item the info field corresponds to the following columns in the test report:

- `CAT_TESTCASE`: the value of the `Value` column.

- `CAT_PROJECT`: the value of the `Value` column.

- `CAT_TRACEANALYSIS`: the value of the `Parameter` column.

Returns:  The string for the info field

Return type:  str

GetLabel()[¶](#tts.core.report.db.ReportItem.ReportItem.GetLabel "Link to this definition")  
Corresponds to the Action/Name column in the test report.

Returns:  The string for the label field

Return type:  str

GetLinkedTestManagementIds()[¶](#tts.core.report.db.ReportItem.ReportItem.GetLinkedTestManagementIds "Link to this definition")  
Returns:  The test management IDs which are contained in the revaluation comments

Return type:  list\<str\>

GetLoopCycle()[¶](#tts.core.report.db.ReportItem.ReportItem.GetLoopCycle "Link to this definition")  
Returns:  The loop cycle

Return type:  str or None

GetName()[¶](#tts.core.report.db.ReportItem.ReportItem.GetName "Link to this definition")  
ReportItems of category `CAT_TRACEANALYSIS` use the name field to store the signal binding informations. It corresponds to the `Generic signals`column in the test report. For ReportItems of other categories use [`GetLabel()`](#tts.core.report.db.ReportItem.ReportItem.GetLabel "tts.core.report.db.ReportItem.ReportItem.GetLabel (Python method) — Corresponds to the Action/Name column in the test report.") for a briefer representation.

Returns:  The string for the name field

Return type:  str

GetOriginalResult()[¶](#tts.core.report.db.ReportItem.ReportItem.GetOriginalResult "Link to this definition")  
Returns:  String of the original result field

Return type:  str

GetParentId()[¶](#tts.core.report.db.ReportItem.ReportItem.GetParentId "Link to this definition")  
Returns:  The ID of the parent report item

Return type:  int

GetPos()[¶](#tts.core.report.db.ReportItem.ReportItem.GetPos "Link to this definition")  
Returns:  The position in the report

Return type:  int

GetRelativeRealtime()[¶](#tts.core.report.db.ReportItem.ReportItem.GetRelativeRealtime "Link to this definition")  
Returns:  The value of the relative_realtime field

Return type:  float or None

GetRelativeTimestamp()[¶](#tts.core.report.db.ReportItem.ReportItem.GetRelativeTimestamp "Link to this definition")  
Returns:  The value of the timestamp_relative field

Return type:  float or None

GetReportItemId()[¶](#tts.core.report.db.ReportItem.ReportItem.GetReportItemId "Link to this definition")  
Returns:  The ID of the report item

Return type:  int

GetResult()[¶](#tts.core.report.db.ReportItem.ReportItem.GetResult "Link to this definition")  
Returns:  The string for the result field

Return type:  str or None

GetRevalComments()[¶](#tts.core.report.db.ReportItem.ReportItem.GetRevalComments "Link to this definition")  
Returns:  The revaluation comments of the current report item

Return type:  list\< [`RevaluationComment`](#tts.core.report.db.ReportItem.RevaluationComment "tts.core.report.db.ReportItem.RevaluationComment (Python class) — The author of the revaluation comment") \>

GetRevalCommentsString()[¶](#tts.core.report.db.ReportItem.ReportItem.GetRevalCommentsString "Link to this definition")  
Gets the revaluation comments of the current report item. The comments are combined to a single string with the pattern “Creator: Comment -> Revaluated result”. If no revaluation comments exists, an empty string is returned.

Returns:  A string representing the combined revaluation comments

Return type:  str

GetSrc()[¶](#tts.core.report.db.ReportItem.ReportItem.GetSrc "Link to this definition")  
Returns:  The name of the source report item

Return type:  str or None

GetSrcCategory()[¶](#tts.core.report.db.ReportItem.ReportItem.GetSrcCategory "Link to this definition")  
Returns:  The category of the source, one of

- `CAT_TESTCASE`

- `CAT_PROJECT`

- `CAT_TRACEANALYSIS`

Return type:  int or None

GetSrcIndex()[¶](#tts.core.report.db.ReportItem.ReportItem.GetSrcIndex "Link to this definition")  
Returns:  The string for the index field

Return type:  str

GetSrcSubType()[¶](#tts.core.report.db.ReportItem.ReportItem.GetSrcSubType "Link to this definition")  
Returns:  UUID of a specific Utility

Return type:  str or None

GetSrcType()[¶](#tts.core.report.db.ReportItem.ReportItem.GetSrcType "Link to this definition")  
Returns the type of the ReportItem, e.g.

- ‘PACKAGE’

- ‘PROJECT’

- ‘CALCULATION’

- ‘TRACE-ANALYSIS’

- ‘EPISODE’

- ‘TRACESTEP’

- ‘TRIGGERBLOCK’

- ‘PLOTITEM’

Returns:  The type of the ReportItem

Return type:  str or None

GetTargetValue()[¶](#tts.core.report.db.ReportItem.ReportItem.GetTargetValue "Link to this definition")  
Corresponds to the `Expected value`column in the test report.

Returns:  The string for the target value field

Return type:  str

GetUndocumentedChild()[¶](#tts.core.report.db.ReportItem.ReportItem.GetUndocumentedChild "Link to this definition")  
Returns:  True if the item has undocumented children, otherwise False

Return type:  bool

HasRevalComments()[¶](#tts.core.report.db.ReportItem.ReportItem.HasRevalComments "Link to this definition")  
Returns:  True when the current report item has revaluation comments, otherwise False

Return type:  bool

InitFromParentId(*[dbCur](#tts.core.report.db.ReportItem.ReportItem.InitFromParentId "tts.core.report.db.ReportItem.ReportItem.InitFromParentId.dbCur (Python parameter)")*, *[parentId](#tts.core.report.db.ReportItem.ReportItem.InitFromParentId.parentId "tts.core.report.db.ReportItem.ReportItem.InitFromParentId.parentId (Python parameter) — ID of the parent item (None for top level items of the main thread).")*, *[parentThreadId](#tts.core.report.db.ReportItem.ReportItem.InitFromParentId.parentThreadId "tts.core.report.db.ReportItem.ReportItem.InitFromParentId.parentThreadId (Python parameter) — Thread ID of the parent item if the information is known.")=`None`*)[¶](#tts.core.report.db.ReportItem.ReportItem.InitFromParentId "Link to this definition")  
See [`InitFromParentItem()`](#tts.core.report.db.ReportItem.ReportItem.InitFromParentItem "tts.core.report.db.ReportItem.ReportItem.InitFromParentItem (Python method) — Init new report item as port of the children list of its parent item indicated by parentId/parent. Attribute threadId, pos and blkEnd are automatically determined and assigned. The new item's threadId depends on whether the parent item is marked the creator of a sub thread (see creator_id of thread table) or not. In the first case the new item is assigned the sub thread id. In the other case the new item inherits its parent's thread id. If parentId is None the new item becomes part of the main thread.").

Parameters:  parentId : int | None[¶](#tts.core.report.db.ReportItem.ReportItem.InitFromParentId.parentId "Permalink to this definition")  
ID of the parent item (None for top level items of the main thread).

parentThreadId : int | None[¶](#tts.core.report.db.ReportItem.ReportItem.InitFromParentId.parentThreadId "Permalink to this definition")  
Thread ID of the parent item if the information is known. Otherwise, it will be determined using the report DB.

InitFromParentItem(*[dbCur](#tts.core.report.db.ReportItem.ReportItem.InitFromParentItem "tts.core.report.db.ReportItem.ReportItem.InitFromParentItem.dbCur (Python parameter)")*, *[parent](#tts.core.report.db.ReportItem.ReportItem.InitFromParentItem.parent "tts.core.report.db.ReportItem.ReportItem.InitFromParentItem.parent (Python parameter) — The parent item referenced by parentId. This parameter exists for performance reasons only, avoiding repeatedly reload of the parent item.")*)[¶](#tts.core.report.db.ReportItem.ReportItem.InitFromParentItem "Link to this definition")  
Init new report item as port of the children list of its parent item indicated by parentId/parent. Attribute threadId, pos and blkEnd are automatically determined and assigned. The new item’s threadId depends on whether the parent item is marked the creator of a sub thread (see creator_id of thread table) or not. In the first case the new item is assigned the sub thread id. In the other case the new item inherits its parent’s thread id. If parentId is None the new item becomes part of the main thread.

Parameters:  parent : [ReportItem](#tts.core.report.db.ReportItem.ReportItem "tts.core.report.db.ReportItem.ReportItem (Python class) — A report item represents the execution results of one test step. It contains information like test step number, time of execution, type of test step and custom fields. Furthermore additional information on a test step can be stored in so called entity elements being attached to the respective report item (e.g. TableEntity or TextEntity).")[¶](#tts.core.report.db.ReportItem.ReportItem.InitFromParentItem.parent "Permalink to this definition")  
The parent item referenced by parentId. This parameter exists for performance reasons only, avoiding repeatedly reload of the parent item. If cachedParentItem.reportItemId does not match parentId the passed item will be ignored and the proper parent item will be fetched from the database.

IsSkipped()[¶](#tts.core.report.db.ReportItem.ReportItem.IsSkipped "Link to this definition")  
Returns:  True when the report item was skipped by the user, e.g. by filtering or commenting out, otherwise False

Return type:  bool

GetActivity()[¶](#tts.core.report.db.ReportItem.ReportItem.GetActivity "Link to this definition")  
Deprecated since version 6.4: Name and Activity are to be replaced by Label

Returns:  The string for the activity field

Return type:  str

*class* ReportItemAnalysisInfo[¶](#tts.core.report.db.ReportItemAnalysisInfo.ReportItemAnalysisInfo "Link to this definition")  

GetImplementedAnalysisLabel()[¶](#tts.core.report.db.ReportItemAnalysisInfo.ReportItemAnalysisInfo.GetImplementedAnalysisLabel "Link to this definition")  
Returns:  The analysis label that is implemented by the analysis package

Return type:  str | None

GetReportItemId()[¶](#tts.core.report.db.ReportItemAnalysisInfo.ReportItemAnalysisInfo.GetReportItemId "Link to this definition")  
Returns:  The report item id to which the information belongs to

Return type:  int

GetStimParamReportItemId()[¶](#tts.core.report.db.ReportItemAnalysisInfo.ReportItemAnalysisInfo.GetStimParamReportItemId "Link to this definition")  
Returns:  The report item id of the specific parameter set of the stimulation package if there is one.

Return type:  int | None

GetStimReportItemId()[¶](#tts.core.report.db.ReportItemAnalysisInfo.ReportItemAnalysisInfo.GetStimReportItemId "Link to this definition")  
Returns:  The report item id of the stimulation package

Return type:  int | None

IsRequested()[¶](#tts.core.report.db.ReportItemAnalysisInfo.ReportItemAnalysisInfo.IsRequested "Link to this definition")  
Returns:  Indicates whether the analysis label was requested by the stimulation package

Return type:  bool

*class* ReportItemComment[¶](#tts.core.report.db.ReportItemComment.ReportItemComment "Link to this definition")  

GetAuthor()[¶](#tts.core.report.db.ReportItemComment.ReportItemComment.GetAuthor "Link to this definition")  
Returns:  The author of the comment

Return type:  str

GetId()[¶](#tts.core.report.db.ReportItemComment.ReportItemComment.GetId "Link to this definition")  
Returns:  The ID of the comment

Return type:  int | None

GetOverriddenResult()[¶](#tts.core.report.db.ReportItemComment.ReportItemComment.GetOverriddenResult "Link to this definition")  
Returns:  The overridden result

Return type:  str | None

GetReportItemId()[¶](#tts.core.report.db.ReportItemComment.ReportItemComment.GetReportItemId "Link to this definition")  
Returns:  The ID of the report item

Return type:  int

GetText()[¶](#tts.core.report.db.ReportItemComment.ReportItemComment.GetText "Link to this definition")  
Returns:  The comment text

Return type:  str

GetTimestamp()[¶](#tts.core.report.db.ReportItemComment.ReportItemComment.GetTimestamp "Link to this definition")  
Returns:  The timestamp or the absolute timestamp

Return type:  float

*class* RevaluationComment[¶](#tts.core.report.db.ReportItem.RevaluationComment "Link to this definition")  
GetAuthor()[¶](#tts.core.report.db.ReportItem.RevaluationComment.GetAuthor "Link to this definition")  
Returns:  The author of the revaluation comment

Return type:  str

GetResult()[¶](#tts.core.report.db.ReportItem.RevaluationComment.GetResult "Link to this definition")  
Returns:  The revaluated result or None

Return type:  str or None

GetText()[¶](#tts.core.report.db.ReportItem.RevaluationComment.GetText "Link to this definition")  
Returns:  Text of the revaluation comment

Return type:  str

GetTime()[¶](#tts.core.report.db.ReportItem.RevaluationComment.GetTime "Link to this definition")  
Returns:  Creation date and time of the revaluation comment

Return type:  float

## Variables[¶](#variables "Link to this heading")

*class* PackageParameterVariable[¶](#tts.core.report.db.Variable.PackageParameterVariable "Link to this definition")  
The Variable represents a test case parameter variable used in a Package.

GetDescription()[¶](#tts.core.report.db.Variable.PackageParameterVariable.GetDescription "Link to this definition")  
Returns:  The description of the variable

Return type:  str

GetName()[¶](#tts.core.report.db.Variable.PackageParameterVariable.GetName "Link to this definition")  
Returns:  The name of the variable

Return type:  str

GetOrigin()[¶](#tts.core.report.db.Variable.PackageParameterVariable.GetOrigin "Link to this definition")  
Returns:  A text representing the origin of the parameter

Return type:  str

GetValue()[¶](#tts.core.report.db.Variable.PackageParameterVariable.GetValue "Link to this definition")  
Returns:  The value of the variable as string representation

Return type:  str

*class* PackageReturnVariable[¶](#tts.core.report.db.Variable.PackageReturnVariable "Link to this definition")  
The Variable represents a return variable used in a Package.

GetDescription()[¶](#tts.core.report.db.Variable.PackageReturnVariable.GetDescription "Link to this definition")  
Returns:  The description of the variable

Return type:  str

GetName()[¶](#tts.core.report.db.Variable.PackageReturnVariable.GetName "Link to this definition")  
Returns:  The name of the variable

Return type:  str

GetValue()[¶](#tts.core.report.db.Variable.PackageReturnVariable.GetValue "Link to this definition")  
Returns:  The value of the variable as string representation

Return type:  str

*class* PackageVariable[¶](#tts.core.report.db.Variable.PackageVariable "Link to this definition")  
Represents a test case variable used in a Package.

GetDescription()[¶](#tts.core.report.db.Variable.PackageVariable.GetDescription "Link to this definition")  
Returns:  The description of the variable

Return type:  str

GetName()[¶](#tts.core.report.db.Variable.PackageVariable.GetName "Link to this definition")  
Returns:  The name of the variable

Return type:  str

GetValue()[¶](#tts.core.report.db.Variable.PackageVariable.GetValue "Link to this definition")  
Returns:  The value of the variable as string representation

Return type:  str

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
