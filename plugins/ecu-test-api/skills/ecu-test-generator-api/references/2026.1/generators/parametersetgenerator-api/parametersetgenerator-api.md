[![logo](../../_static/ecu.test.svg)](../../index.html "API  documentation") API documentation

[ Internal APIs ](../../general_api/api.md)

[ Advanced operations of package variable types ](../../general_api/variabledatastructures.md)

[ Advanced properties of bus-related objects ](../../general_api/busdatastructures.md)

[ Bus related objects of trace analysis ](../../general_api/busdatastructuresTraceanalysis.md)

[ Advanced properties of diagnostics-related objects ](../../general_api/diagdatastructures.md)

[ Diagnostics related objects of trace analysis ](../../general_api/diagdatastructuresTraceanalysis.md)

[ Advanced properties of media-related objects ](../../general_api/mediadatastructures.md)

[ Advanced properties of DLT logging-related objects ](../../general_api/dltdatastructures.md)

[ COM API ](../../general_api/com-api.md)

[ REST API ](../../general_api/rest-api.md)

[ Report API ](../../general_api/apireport.md)

[ Object API ](../../general_api/objectApi.md)

[ Trace Analysis API ](../../TraceAnalysisAPI/index.md)

[ Generator APIs ](../index.md)

Generator APIs

[ Project Generator API ](../projectgenerator-api/projectgenerator-api.md)

[ Package Generator API ](../packagegenerator-api/packagegenerator-api.md)

Parameter Set Generator API [ Parameter Set Generator API ](#)

Parameter Set Generator API

- [ ParamGenerator ](#module-tts.core.project.generator.paramGenerator.ParamGenerator)
  - [C ParamGenerator ](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator)
    - [A DESCRIPTION ](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.DESCRIPTION)
    - [A ID ](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.ID)
    - [A NAME ](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.NAME)
    - [A SERIALIZE ](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.SERIALIZE)
    - [A api ](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.api)
    - [A projectPath ](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.projectPath)
    - [M GetDescription ](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.GetDescription)
    - [M GetId ](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.GetId)
    - [M GetName ](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.GetName)
    - [M Check ](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.Check)
    - [M CreateCycleData ](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.CreateCycleData)
    - [M DryGenerationEnabled ](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.DryGenerationEnabled)
    - [M GenerationIterator ](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.GenerationIterator)
    - [M GetDialog ](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.GetDialog)
    - [M GetLastReturnSet ](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.GetLastReturnSet)
    - [M GetParameterText ](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.GetParameterText)
    - [M GetReportData ](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.GetReportData)
    - [M GetTargetItemCount ](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.GetTargetItemCount)
    - [M GetUsedMappingItems ](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.GetUsedMappingItems)
    - [M IsValidForAnalysisPackages ](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.IsValidForAnalysisPackages)
    - [M OnInit ](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.OnInit)
    - [M PostGeneration ](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.PostGeneration)
    - [M PreGeneration ](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.PreGeneration)
- [ AbortError ](#aborterror)
  - [C AbortError ](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.AbortError)
- [ CallbackParamGenerator ](#module-tts.core.project.generator.paramGenerator.CallbackParamGenerator)
  - [C CallbackParamGenerator ](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator)
    - [A DESCRIPTION ](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.DESCRIPTION)
    - [A ID ](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.ID)
    - [A NAME ](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.NAME)
    - [A SERIALIZE ](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.SERIALIZE)
    - [A api ](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.api)
    - [A projectPath ](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.projectPath)
    - [M GetDescription ](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.GetDescription)
    - [M GetId ](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.GetId)
    - [M GetName ](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.GetName)
    - [M Check ](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.Check)
    - [M CreateCycleData ](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.CreateCycleData)
    - [M DryGenerationEnabled ](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.DryGenerationEnabled)
    - [M Generate ](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.Generate)
    - [M GetDialog ](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.GetDialog)
    - [M GetLastReturnSets ](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.GetLastReturnSets)
    - [M GetParameterText ](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.GetParameterText)
    - [M GetReportData ](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.GetReportData)
    - [M GetTargetItemCount ](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.GetTargetItemCount)
    - [M GetUsedMappingItems ](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.GetUsedMappingItems)
    - [M IsValidForAnalysisPackages ](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.IsValidForAnalysisPackages)
    - [M OnInit ](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.OnInit)
    - [M PostGeneration ](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.PostGeneration)
    - [M PreGeneration ](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.PreGeneration)
- [ CycleData ](#cycledata)
  - [C CycleData ](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData)
    - [A RECORDING_INFO_CLASS ](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.RECORDING_INFO_CLASS)
    - [A Attributes ](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.Attributes)
    - [A ConstSet ](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.ConstSet)
    - [A Name ](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.Name)
    - [A ParamSet ](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.ParamSet)
    - [A RecordingInfos ](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.RecordingInfos)
    - [M AddAttribute ](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.AddAttribute)
    - [M AddConst ](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.AddConst)
    - [M AddMappingItem ](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.AddMappingItem)
    - [M AddParameter ](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.AddParameter)
    - [M AddRecordingInfo ](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.AddRecordingInfo)
    - [M GetAttributes ](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.GetAttributes)
    - [M GetConstSet ](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.GetConstSet)
    - [M GetName ](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.GetName)
    - [M GetParamSet ](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.GetParamSet)
    - [M GetRecordingInfos ](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.GetRecordingInfos)
    - [M SetName ](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.SetName)
    - [M UpdateAttribute ](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.UpdateAttribute)
- [ OptimizerBase ](#module-tts.core.project.generator.paramGenerator.OptimizerBase)
  - [C OptimizerBase ](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase)
    - [A DESCRIPTION ](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.DESCRIPTION)
    - [A ENABLE_PARAMETER_VARIATION ](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.ENABLE_PARAMETER_VARIATION)
    - [A ID ](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.ID)
    - [A NAME ](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.NAME)
    - [A SERIALIZE ](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.SERIALIZE)
    - [A api ](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.api)
    - [A projectPath ](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.projectPath)
    - [M GetDescription ](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.GetDescription)
    - [M GetId ](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.GetId)
    - [M GetName ](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.GetName)
    - [M Check ](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.Check)
    - [M CreateCycleData ](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.CreateCycleData)
    - [M DryGenerationEnabled ](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.DryGenerationEnabled)
    - [M Generate ](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.Generate)
    - [M GetDialog ](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.GetDialog)
    - [M GetLastReturnSets ](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.GetLastReturnSets)
    - [M GetMinMaxValues ](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.GetMinMaxValues)
    - [M GetParameterText ](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.GetParameterText)
    - [M GetReportData ](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.GetReportData)
    - [M GetTargetItemCount ](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.GetTargetItemCount)
    - [M GetUsedMappingItems ](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.GetUsedMappingItems)
    - [M GetVariationResults ](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.GetVariationResults)
    - [M IsValidForAnalysisPackages ](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.IsValidForAnalysisPackages)
    - [M OnInit ](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.OnInit)
    - [M PostGeneration ](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.PostGeneration)
    - [M PreGeneration ](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.PreGeneration)
  - [C VariationResult ](#tts.core.project.generator.paramGenerator.OptimizerBase.VariationResult)
    - [A CycleData ](#tts.core.project.generator.paramGenerator.OptimizerBase.VariationResult.CycleData)
    - [A ReturnSet ](#tts.core.project.generator.paramGenerator.OptimizerBase.VariationResult.ReturnSet)
- [ PackageInfo ](#module-tts.core.project.projectStep.PackageInfo)
  - [C PackageInfo ](#tts.core.project.projectStep.PackageInfo.PackageInfo)
    - [M GetName ](#tts.core.project.projectStep.PackageInfo.PackageInfo.GetName)
    - [M GetParameterVariables ](#tts.core.project.projectStep.PackageInfo.PackageInfo.GetParameterVariables)
    - [M GetPath ](#tts.core.project.projectStep.PackageInfo.PackageInfo.GetPath)
    - [M GetReturnVariables ](#tts.core.project.projectStep.PackageInfo.PackageInfo.GetReturnVariables)
    - [M GetVariables ](#tts.core.project.projectStep.PackageInfo.PackageInfo.GetVariables)
- [ RecordingInfo ](#recordinginfo)
  - [C RecordingInfo ](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.RecordingInfo)
    - [A FormatDetails ](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.RecordingInfo.FormatDetails)
    - [A Path ](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.RecordingInfo.Path)
    - [A RecordingName ](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.RecordingInfo.RecordingName)
    - [A RecordingNumber ](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.RecordingInfo.RecordingNumber)
    - [A RecordingType ](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.RecordingInfo.RecordingType)
    - [M GetFormatDetails ](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.RecordingInfo.GetFormatDetails)
    - [M GetPath ](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.RecordingInfo.GetPath)
    - [M GetRecordingName ](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.RecordingInfo.GetRecordingName)
    - [M GetRecordingNumber ](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.RecordingInfo.GetRecordingNumber)
    - [M GetRecordingType ](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.RecordingInfo.GetRecordingType)
    - [M SetFormatDetails ](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.RecordingInfo.SetFormatDetails)
    - [M SetRecordingName ](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.RecordingInfo.SetRecordingName)
    - [M SetRecordingNumber ](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.RecordingInfo.SetRecordingNumber)
    - [M SetRecordingType ](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.RecordingInfo.SetRecordingType)
    - [M `\_\_init\_\_` ](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.RecordingInfo.__init__)
- [ ReportData ](#reportdata)
  - [C ReportData ](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.ReportData)
    - [A Comment ](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.ReportData.Comment)
    - [A Value ](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.ReportData.Value)
    - [M GetComment ](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.ReportData.GetComment)
    - [M GetValue ](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.ReportData.GetValue)
    - [M SetComment ](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.ReportData.SetComment)
    - [M SetValue ](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.ReportData.SetValue)
- [ Variable ](#variable)
- [ VariationResult ](#variationresult)

[ Tools ](../../tools/index.md)

[ User test management ](../../userTestmanagement/index.md)

[ UserUtility API ](../../user-utility/user-utility.md)

[ Utility Examples ](../../user-utility/example-utilities.md)

Parameter Set Generator API

- [ ParamGenerator ](#module-tts.core.project.generator.paramGenerator.ParamGenerator)
  - [C ParamGenerator ](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator)
    - [A DESCRIPTION ](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.DESCRIPTION)
    - [A ID ](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.ID)
    - [A NAME ](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.NAME)
    - [A SERIALIZE ](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.SERIALIZE)
    - [A api ](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.api)
    - [A projectPath ](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.projectPath)
    - [M GetDescription ](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.GetDescription)
    - [M GetId ](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.GetId)
    - [M GetName ](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.GetName)
    - [M Check ](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.Check)
    - [M CreateCycleData ](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.CreateCycleData)
    - [M DryGenerationEnabled ](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.DryGenerationEnabled)
    - [M GenerationIterator ](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.GenerationIterator)
    - [M GetDialog ](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.GetDialog)
    - [M GetLastReturnSet ](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.GetLastReturnSet)
    - [M GetParameterText ](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.GetParameterText)
    - [M GetReportData ](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.GetReportData)
    - [M GetTargetItemCount ](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.GetTargetItemCount)
    - [M GetUsedMappingItems ](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.GetUsedMappingItems)
    - [M IsValidForAnalysisPackages ](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.IsValidForAnalysisPackages)
    - [M OnInit ](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.OnInit)
    - [M PostGeneration ](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.PostGeneration)
    - [M PreGeneration ](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.PreGeneration)
- [ AbortError ](#aborterror)
  - [C AbortError ](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.AbortError)
- [ CallbackParamGenerator ](#module-tts.core.project.generator.paramGenerator.CallbackParamGenerator)
  - [C CallbackParamGenerator ](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator)
    - [A DESCRIPTION ](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.DESCRIPTION)
    - [A ID ](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.ID)
    - [A NAME ](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.NAME)
    - [A SERIALIZE ](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.SERIALIZE)
    - [A api ](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.api)
    - [A projectPath ](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.projectPath)
    - [M GetDescription ](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.GetDescription)
    - [M GetId ](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.GetId)
    - [M GetName ](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.GetName)
    - [M Check ](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.Check)
    - [M CreateCycleData ](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.CreateCycleData)
    - [M DryGenerationEnabled ](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.DryGenerationEnabled)
    - [M Generate ](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.Generate)
    - [M GetDialog ](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.GetDialog)
    - [M GetLastReturnSets ](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.GetLastReturnSets)
    - [M GetParameterText ](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.GetParameterText)
    - [M GetReportData ](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.GetReportData)
    - [M GetTargetItemCount ](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.GetTargetItemCount)
    - [M GetUsedMappingItems ](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.GetUsedMappingItems)
    - [M IsValidForAnalysisPackages ](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.IsValidForAnalysisPackages)
    - [M OnInit ](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.OnInit)
    - [M PostGeneration ](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.PostGeneration)
    - [M PreGeneration ](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.PreGeneration)
- [ CycleData ](#cycledata)
  - [C CycleData ](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData)
    - [A RECORDING_INFO_CLASS ](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.RECORDING_INFO_CLASS)
    - [A Attributes ](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.Attributes)
    - [A ConstSet ](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.ConstSet)
    - [A Name ](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.Name)
    - [A ParamSet ](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.ParamSet)
    - [A RecordingInfos ](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.RecordingInfos)
    - [M AddAttribute ](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.AddAttribute)
    - [M AddConst ](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.AddConst)
    - [M AddMappingItem ](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.AddMappingItem)
    - [M AddParameter ](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.AddParameter)
    - [M AddRecordingInfo ](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.AddRecordingInfo)
    - [M GetAttributes ](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.GetAttributes)
    - [M GetConstSet ](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.GetConstSet)
    - [M GetName ](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.GetName)
    - [M GetParamSet ](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.GetParamSet)
    - [M GetRecordingInfos ](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.GetRecordingInfos)
    - [M SetName ](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.SetName)
    - [M UpdateAttribute ](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.UpdateAttribute)
- [ OptimizerBase ](#module-tts.core.project.generator.paramGenerator.OptimizerBase)
  - [C OptimizerBase ](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase)
    - [A DESCRIPTION ](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.DESCRIPTION)
    - [A ENABLE_PARAMETER_VARIATION ](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.ENABLE_PARAMETER_VARIATION)
    - [A ID ](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.ID)
    - [A NAME ](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.NAME)
    - [A SERIALIZE ](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.SERIALIZE)
    - [A api ](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.api)
    - [A projectPath ](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.projectPath)
    - [M GetDescription ](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.GetDescription)
    - [M GetId ](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.GetId)
    - [M GetName ](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.GetName)
    - [M Check ](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.Check)
    - [M CreateCycleData ](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.CreateCycleData)
    - [M DryGenerationEnabled ](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.DryGenerationEnabled)
    - [M Generate ](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.Generate)
    - [M GetDialog ](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.GetDialog)
    - [M GetLastReturnSets ](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.GetLastReturnSets)
    - [M GetMinMaxValues ](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.GetMinMaxValues)
    - [M GetParameterText ](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.GetParameterText)
    - [M GetReportData ](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.GetReportData)
    - [M GetTargetItemCount ](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.GetTargetItemCount)
    - [M GetUsedMappingItems ](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.GetUsedMappingItems)
    - [M GetVariationResults ](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.GetVariationResults)
    - [M IsValidForAnalysisPackages ](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.IsValidForAnalysisPackages)
    - [M OnInit ](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.OnInit)
    - [M PostGeneration ](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.PostGeneration)
    - [M PreGeneration ](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.PreGeneration)
  - [C VariationResult ](#tts.core.project.generator.paramGenerator.OptimizerBase.VariationResult)
    - [A CycleData ](#tts.core.project.generator.paramGenerator.OptimizerBase.VariationResult.CycleData)
    - [A ReturnSet ](#tts.core.project.generator.paramGenerator.OptimizerBase.VariationResult.ReturnSet)
- [ PackageInfo ](#module-tts.core.project.projectStep.PackageInfo)
  - [C PackageInfo ](#tts.core.project.projectStep.PackageInfo.PackageInfo)
    - [M GetName ](#tts.core.project.projectStep.PackageInfo.PackageInfo.GetName)
    - [M GetParameterVariables ](#tts.core.project.projectStep.PackageInfo.PackageInfo.GetParameterVariables)
    - [M GetPath ](#tts.core.project.projectStep.PackageInfo.PackageInfo.GetPath)
    - [M GetReturnVariables ](#tts.core.project.projectStep.PackageInfo.PackageInfo.GetReturnVariables)
    - [M GetVariables ](#tts.core.project.projectStep.PackageInfo.PackageInfo.GetVariables)
- [ RecordingInfo ](#recordinginfo)
  - [C RecordingInfo ](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.RecordingInfo)
    - [A FormatDetails ](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.RecordingInfo.FormatDetails)
    - [A Path ](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.RecordingInfo.Path)
    - [A RecordingName ](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.RecordingInfo.RecordingName)
    - [A RecordingNumber ](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.RecordingInfo.RecordingNumber)
    - [A RecordingType ](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.RecordingInfo.RecordingType)
    - [M GetFormatDetails ](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.RecordingInfo.GetFormatDetails)
    - [M GetPath ](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.RecordingInfo.GetPath)
    - [M GetRecordingName ](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.RecordingInfo.GetRecordingName)
    - [M GetRecordingNumber ](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.RecordingInfo.GetRecordingNumber)
    - [M GetRecordingType ](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.RecordingInfo.GetRecordingType)
    - [M SetFormatDetails ](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.RecordingInfo.SetFormatDetails)
    - [M SetRecordingName ](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.RecordingInfo.SetRecordingName)
    - [M SetRecordingNumber ](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.RecordingInfo.SetRecordingNumber)
    - [M SetRecordingType ](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.RecordingInfo.SetRecordingType)
    - [M `\_\_init\_\_` ](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.RecordingInfo.__init__)
- [ ReportData ](#reportdata)
  - [C ReportData ](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.ReportData)
    - [A Comment ](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.ReportData.Comment)
    - [A Value ](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.ReportData.Value)
    - [M GetComment ](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.ReportData.GetComment)
    - [M GetValue ](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.ReportData.GetValue)
    - [M SetComment ](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.ReportData.SetComment)
    - [M SetValue ](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.ReportData.SetValue)
- [ Variable ](#variable)
- [ VariationResult ](#variationresult)

# Parameter Set Generator API[¶](#parameter-set-generator-api "Link to this heading")

An overview of commands for [Parameter generator for projects](../../../en/Extensions/Param-generator.html).

## ParamGenerator[¶](#module-tts.core.project.generator.paramGenerator.ParamGenerator "Link to this heading")

*class* ParamGenerator[¶](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator "Link to this definition")  
This is the base class for user-defined parameter generators and all implementations should be derived from this class. It defines specific methods that are called during generation of parameter sets. The desired behavior of a parameter generator is achieved by overwriting the methods provided for this purpose.

Some fields and methods *must* be overridden (**mandatory**), others *may* be overridden (**optional**). There are also methods that are only to be called by the user implementation and should not be overridden (those without a note).

DESCRIPTION = `''`[¶](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.DESCRIPTION "Link to this definition")  
A short description of the parameter generator.

Type:  str

Info: Setting this field is **optional**
ID = `''`[¶](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.ID "Link to this definition")  
A universally unique identifier to make the parameter generator unique. The ID should be generated using a UUID generator to be unique.

Type:  str

Info: Setting this field is **mandatory**
NAME = `''`[¶](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.NAME "Link to this definition")  
The display name of the parameter generator.

Type:  str

Info: Setting this field is **mandatory**
SERIALIZE : dict[str, tuple[str, str] | tuple[str, str, object]] = `{}`[¶](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.SERIALIZE "Link to this definition")  
Declaration of instance variables of the parameter generator, that are to be exported/imported to/from xml format (e.g. during saving/loading a project). The declaration contains an item for each instance variable in form of an dictionary. Example:

    SERIALIZE = {
                    "foo": ("FOO-VAR", "integer", 23),
                    "bar": ("BAR", "string"),
                    "params: ("PARAMETERS", "list")
                }

The declaration items key must match the name of the corresponding instance variable (e.g. for an instance variable self.foo the item’s key must be “foo”). The item’s value must be a tuple containing at least 2 elements. So the general syntax for a declaration item is:

    ``<variable name>: (<variable alias>, <type alias>, [default value])``

Syntax and meaning of the tuple’s elements are:

- **\<variable alias\>** declares the name of the xml element that is used for the variable’s xml representation.

- **\<type alias\>** keyword specifing the python variable’s type. The following table gives all keywords and their corresponding python type respectively:

  - `boolean`: bool

  - `integer`: int

  - `long`: int

  - `float`: float

  - `string`: str

  - `unicode`: str

  - `list`: list

  - `dict`: dict

PLEASE NOTE: Keys of dictionaries being (de-)serialized must be strings. Furthermore values of dictionaries and lists are required to be of type `bool`, `int`, `float`, `str`, `list` or `dict`. The same restrictions apply to embedded lists and dictionaries. The types `long` and `unicode` are only kept for compatibility. Do not use these in new code.

- **\<default value\>** is an optional element. It specifies the variable’s default value. If the variable’s value equals its default value during export the variable is not exported at all. Conversely, the variable is assigned its default value during import if the xml data does not provide an value for the variable.

Type:  dict

Info: Setting this field is **optional**
api = `None`[¶](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.api "Link to this definition")  
Access to the internal ecu.test API. The API will be assigned at runtime, in order to be independent from ecu.test for testing purposes.

See also

[Internal APIs](../../general_api/api.md#internalapi)

projectPath : str | None = `None`[¶](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.projectPath "Link to this definition")  
Absolute path to the project file containing the generator. In case of direct execution, this is the source project. In case of static generation it is the destination project.

*classmethod* GetDescription()[¶](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.GetDescription "Link to this definition")  
Returns the description of the parameter generator. The description can be specified by setting the class variable [`DESCRIPTION`](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.DESCRIPTION "tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.DESCRIPTION (Python attribute) — A short description of the parameter generator.").

Return type:  str

*classmethod* GetId()[¶](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.GetId "Link to this definition")  
Returns the universally unique identifier of the parameter generator. The identifier should be specified by setting the class variable [`ID`](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.ID "tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.ID (Python attribute) — A universally unique identifier to make the parameter generator unique. The ID should be generated using a UUID generator to be unique.").

Return type:  str

*classmethod* GetName()[¶](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.GetName "Link to this definition")  
Returns the name of the parameter generator. The name should be specified by setting the class variable [`NAME`](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.NAME "tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.NAME (Python attribute) — The display name of the parameter generator.").

Return type:  str

Check()[¶](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.Check "Link to this definition")  
Implement this method to allow the user-implemented generator to be checked.

Returns:  A list of error messages or an empty list if everything is fine.

Return type:  list\<str\>

Info

Overriding this method is **optional**.

CreateCycleData(*[paramSet](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.CreateCycleData.paramSet "tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.CreateCycleData.paramSet (Python parameter) — A set of parameters to parameterize a package.")=`None`*, *[constSet](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.CreateCycleData.constSet "tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.CreateCycleData.constSet (Python parameter) — A set of constants that will be set before running a package.")=`None`*, *[name](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.CreateCycleData.name "tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.CreateCycleData.name (Python parameter) — A name for this cycle that will be displayed in the report.")=`None`*)[¶](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.CreateCycleData "Link to this definition")  
Method, to create an instance of class CycleData.

Parameters:  paramSet : dict[¶](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.CreateCycleData.paramSet "Permalink to this definition")  
A set of parameters to parameterize a package.

constSet : dict[¶](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.CreateCycleData.constSet "Permalink to this definition")  
A set of constants that will be set before running a package. (optional)

name : str[¶](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.CreateCycleData.name "Permalink to this definition")  
A name for this cycle that will be displayed in the report. (optional)

Returns:  The cycle data object

Return type:  [`CycleData`](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData "tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData (Python class) — This class is a container for all data, that can be generated during one cycle.")

DryGenerationEnabled()[¶](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.DryGenerationEnabled "Link to this definition")  
Returns True, if the generator runs in dry generation mode. In this mode, the generator is used to generate a project with static parameter records.

Return type:  bool

GenerationIterator()[¶](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.GenerationIterator "Link to this definition")  
Implement this method for generating parameter sets. Each parameter set must be an object of [`CycleData`](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData "tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData (Python class) — This class is a container for all data, that can be generated during one cycle.") and can be created with the method [`CreateCycleData()`](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.CreateCycleData "tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.CreateCycleData (Python method) — Method, to create an instance of class CycleData."). Since this is a python iterator, the parameter sets must be returned with the keyword ‘yield’. Either a single parameter set or a list of parameter sets can be yielded.

Example:

    def GenerationIterator(self):
        for line in file:
            yield CreateCycleData({'lineData': line})

Info

Overriding this method is **mandatory**

GetDialog()[¶](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.GetDialog "Link to this definition")  
Implement this method to return the configuration dialog of your parameter generator. The dialog should set the generator data.

Return type:  wx.Dialog or None

Info

Overriding this method is **optional**.

GetLastReturnSet()[¶](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.GetLastReturnSet "Link to this definition")  
Returns the return set of the last package execution.

This method only returns a result if the generator is not running in dry generation mode and it is called within the [`GenerationIterator()`](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.GenerationIterator "tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.GenerationIterator (Python method) — Implement this method for generating parameter sets. Each parameter set must be an object of CycleData and can be created with the method CreateCycleData(). Since this is a python iterator, the parameter sets must be returned with the keyword 'yield'. Either a single parameter set or a list of parameter sets can be yielded.") method after at least one parameter set has been executed (by a yield in the [`GenerationIterator()`](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.GenerationIterator "tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.GenerationIterator (Python method) — Implement this method for generating parameter sets. Each parameter set must be an object of CycleData and can be created with the method CreateCycleData(). Since this is a python iterator, the parameter sets must be returned with the keyword 'yield'. Either a single parameter set or a list of parameter sets can be yielded.") method). In all other circumstances, the method always returns None.

Return type:  dict, None

GetParameterText()[¶](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.GetParameterText "Link to this definition")  
Implement this method to show the parameters of your param generator in properties column.

Returns:  parameter text

Return type:  str

Info

Overriding this method is **optional**.

GetReportData()[¶](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.GetReportData "Link to this definition")  
Implement this method to set the information for the generator test step in the report. An object of type [`ReportData`](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.ReportData "tts.core.project.generator.paramGenerator.ParamGeneratorBase.ReportData (Python class) — This class is a container for the information of the generator test step shown in the report") must be returned.

Return type:  [`ReportData`](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.ReportData "tts.core.project.generator.paramGenerator.ParamGeneratorBase.ReportData (Python class) — This class is a container for the information of the generator test step shown in the report") or None

Info

Overriding this method is **optional**.

GetTargetItemCount()[¶](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.GetTargetItemCount "Link to this definition")  
Implement this method to define the expected number of cycle sets to be generated as information for progress indicators. Will be called for updates throughout the generation. Therefore, you can dynamically return the size of the current task.

Returns:  expected count of cycle sets to be generated

Return type:  int

GetUsedMappingItems()[¶](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.GetUsedMappingItems "Link to this definition")  
Returns the mapping items that will be used during generation.

If mapping items are to be added to the generated parameter sets of an analysis package, they have to be defined here in order to be registered for the stimulation package. Mapping items can be defined here directly, parsed from a file or whatever source, but the complete set of mapping items used during generation has to be returned by this method.

Info

Overriding this method is **optional** and only necessary for parameter set generators used with analysis packages and overwriting mapping items.

Caution

This method is called before any other method (e.g., PreGeneration)! If you read in required data for the mapping during PreGeneration, you have to redesign your code to be called at least once during GetUsedMappingItems.

Returns:  list of mapping items

Return type:  list[[ApiClient.MappingItem](../../general_api/MappingApi/MappingItem.md#ApiClient.MappingItem "ApiClient.MappingItem (Python class) — MappingApi.CreateGenericMappingItem")]

IsValidForAnalysisPackages()[¶](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.IsValidForAnalysisPackages "Link to this definition")  
Returns if usage of parameter set generator is feasible for analysis packages.

If set to ‘True’ and parameter set generator is not feasible for analysis packages, errors will be raised during runtime. If set to ‘False’, the GUI will give direct feedback if the parameter set generator is used for an analysis package.

Returns:  True, if valid for analysis package usage, else False

Return type:  bool

Info

Overriding this method is **optional**.

OnInit(*[packageInfo](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.OnInit.packageInfo "tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.OnInit.packageInfo (Python parameter) — The package info object.")*)[¶](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.OnInit "Link to this definition")  
Implement this method to process information about the package to which the generator belongs. It will be called before [`PreGeneration()`](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.PreGeneration "tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.PreGeneration (Python method) — Implement this method to specify pre generation behavior. This method is called before the generation.") or [`GetDialog()`](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.GetDialog "tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.GetDialog (Python method) — Implement this method to return the configuration dialog of your parameter generator. The dialog should set the generator data.") is called.

Parameters:  packageInfo[¶](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.OnInit.packageInfo "Permalink to this definition")  
The package info object.

Info

Overriding this method is **optional**

PostGeneration()[¶](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.PostGeneration "Link to this definition")  
Implement this method to specify post generation behavior. This method is called after the generation. This method will be called even if an exception occurs during generation (incl. PreGeneration), but not if the project execution is aborted (by the user or because of an “abort on error” setting).

Info

Overriding this method is **optional**.

PreGeneration()[¶](#tts.core.project.generator.paramGenerator.ParamGenerator.ParamGenerator.PreGeneration "Link to this definition")  
Implement this method to specify pre generation behavior. This method is called before the generation.

Info

Overriding this method is **optional**.

## AbortError[¶](#aborterror "Link to this heading")

*class* AbortError[¶](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.AbortError "Link to this definition")  

## CallbackParamGenerator[¶](#module-tts.core.project.generator.paramGenerator.CallbackParamGenerator "Link to this heading")

*class* CallbackParamGenerator[¶](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator "Link to this definition")  
This is an alternative base class for user-defined parameter generators. The interface corresponds to that of the ParamGenerator class with the only difference that the Generate method must be implemented instead of the GenerationIterator method.

DESCRIPTION = `''`[¶](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.DESCRIPTION "Link to this definition")  
A short description of the parameter generator.

Type:  str

Info: Setting this field is **optional**
ID = `''`[¶](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.ID "Link to this definition")  
A universally unique identifier to make the parameter generator unique. The ID should be generated using a UUID generator to be unique.

Type:  str

Info: Setting this field is **mandatory**
NAME = `''`[¶](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.NAME "Link to this definition")  
The display name of the parameter generator.

Type:  str

Info: Setting this field is **mandatory**
SERIALIZE : dict[str, tuple[str, str] | tuple[str, str, object]] = `{}`[¶](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.SERIALIZE "Link to this definition")  
Declaration of instance variables of the parameter generator, that are to be exported/imported to/from xml format (e.g. during saving/loading a project). The declaration contains an item for each instance variable in form of an dictionary. Example:

    SERIALIZE = {
                    "foo": ("FOO-VAR", "integer", 23),
                    "bar": ("BAR", "string"),
                    "params: ("PARAMETERS", "list")
                }

The declaration items key must match the name of the corresponding instance variable (e.g. for an instance variable self.foo the item’s key must be “foo”). The item’s value must be a tuple containing at least 2 elements. So the general syntax for a declaration item is:

    ``<variable name>: (<variable alias>, <type alias>, [default value])``

Syntax and meaning of the tuple’s elements are:

- **\<variable alias\>** declares the name of the xml element that is used for the variable’s xml representation.

- **\<type alias\>** keyword specifing the python variable’s type. The following table gives all keywords and their corresponding python type respectively:

  - `boolean`: bool

  - `integer`: int

  - `long`: long

  - `float`: float

  - `string`: str

  - `unicode`: str

  - `list`: list

  - `dict`: dict

PLEASE NOTE: Keys of dictionaries being (de-)serialized must be strings. Furthermore values of dictionaries and lists are required to be of type `bool`, `int`, `float`, `str`, `list` or `dict`. The same restrictions apply to embedded lists and dictionaries. The types `long` and `unicode` are only kept for compatibility. Do not use these in new code.

- **\<default value\>** is an optional element. It specifies the variable’s default value. If the variable’s value equals its default value during export the variable is not exported at all. Conversely, the variable is assigned its default value during import if the xml data does not provide an value for the variable.

Type:  dict

Info: Setting this field is **optional**
api = `None`[¶](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.api "Link to this definition")  
Access to the internal ecu.test API. The API will be assigned at runtime, in order to be independent from ecu.test for testing purposes.

See also

[Internal APIs](../../general_api/api.md#internalapi)

projectPath : str | None = `None`[¶](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.projectPath "Link to this definition")  
Absolute path to the project file containing the generator. In case of direct execution, this is the source project. In case of static generation it is the destination project.

*classmethod* GetDescription()[¶](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.GetDescription "Link to this definition")  
Returns the description of the parameter generator. The description can be specified by setting the class variable [`DESCRIPTION`](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.DESCRIPTION "tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.DESCRIPTION (Python attribute) — A short description of the parameter generator.").

Return type:  str

*classmethod* GetId()[¶](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.GetId "Link to this definition")  
Returns the universally unique identifier of the parameter generator. The identifier should be specified by setting the class variable [`ID`](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.ID "tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.ID (Python attribute) — A universally unique identifier to make the parameter generator unique. The ID should be generated using a UUID generator to be unique.").

Return type:  str

*classmethod* GetName()[¶](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.GetName "Link to this definition")  
Returns the name of the parameter generator. The name should be specified by setting the class variable [`NAME`](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.NAME "tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.NAME (Python attribute) — The display name of the parameter generator.").

Return type:  str

Check()[¶](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.Check "Link to this definition")  
Implement this method to allow the user-implemented generator to be checked.

Returns:  A list of error messages or an empty list if everything is fine.

Return type:  list\<str\>

Info

Overriding this method is **optional**.

CreateCycleData(*[paramSet](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.CreateCycleData.paramSet "tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.CreateCycleData.paramSet (Python parameter) — A set of parameters to parameterize a package.")=`None`*, *[constSet](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.CreateCycleData.constSet "tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.CreateCycleData.constSet (Python parameter) — A set of constants that will be set before running a package.")=`None`*, *[name](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.CreateCycleData.name "tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.CreateCycleData.name (Python parameter) — A name for this cycle that will be displayed in the report.")=`None`*)[¶](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.CreateCycleData "Link to this definition")  
Method, to create an instance of class CycleData.

Parameters:  paramSet : dict[¶](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.CreateCycleData.paramSet "Permalink to this definition")  
A set of parameters to parameterize a package.

constSet : dict[¶](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.CreateCycleData.constSet "Permalink to this definition")  
A set of constants that will be set before running a package. (optional)

name : str[¶](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.CreateCycleData.name "Permalink to this definition")  
A name for this cycle that will be displayed in the report. (optional)

Returns:  The cycle data object

Return type:  [`CycleData`](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData "tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData (Python class) — This class is a container for all data, that can be generated during one cycle.")

DryGenerationEnabled()[¶](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.DryGenerationEnabled "Link to this definition")  
Returns True, if the generator runs in dry generation mode. In this mode, the generator is used to generate a project with static parameter records.

Return type:  bool

Generate(*[testRunFunction](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.Generate.testRunFunction "tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.Generate.testRunFunction (Python parameter) — If this function is called, an ecu.test test run is started.")*)[¶](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.Generate "Link to this definition")  
Implement this method for generating parameter sets. Each parameter set must be an object of [`CycleData`](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData "tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData (Python class) — This class is a container for all data, that can be generated during one cycle.") and can be created with the method [`CreateCycleData()`](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.CreateCycleData "tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.CreateCycleData (Python method) — Method, to create an instance of class CycleData."). A test run is executed by calling the testRunFunction.

Parameters:  testRunFunction[¶](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.Generate.testRunFunction "Permalink to this definition")  
If this function is called, an ecu.test test run is started. The function expects one or more parameter sets and returns a list of dictionaries containing the return variables of the package with their result values. A parameter set must be an instance of [`CycleData`](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData "tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData (Python class) — This class is a container for all data, that can be generated during one cycle.") which can be created with the method [`CreateCycleData()`](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.CreateCycleData "tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.CreateCycleData (Python method) — Method, to create an instance of class CycleData."). If the test run is aborted by ecu.test, an abort error occurs. This error should only be caught for the purpose of cleaning up.

Info

Overriding this method is **mandatory**

GetDialog()[¶](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.GetDialog "Link to this definition")  
Implement this method to return the configuration dialog of your parameter generator. The dialog should set the generator data.

Return type:  wx.Dialog or None

Info

Overriding this method is **optional**.

GetLastReturnSets()[¶](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.GetLastReturnSets "Link to this definition")  
Returns a list of all return sets from the last ecu.test test run.

This method only returns a result if the generator is not running in dry generation mode and it is called within the L{Generate()} method after at least one parameter set has been executed (by calling the testRunFunction in the L{Generate()} method). In all other circumstances, the method always returns an empty list.

Return type:  list of dicts

GetParameterText()[¶](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.GetParameterText "Link to this definition")  
Implement this method to show the parameters of your param generator in properties column.

Returns:  parameter text

Return type:  str

Info

Overriding this method is **optional**.

GetReportData()[¶](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.GetReportData "Link to this definition")  
Implement this method to set the information for the generator test step in the report. An object of type [`ReportData`](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.ReportData "tts.core.project.generator.paramGenerator.ParamGeneratorBase.ReportData (Python class) — This class is a container for the information of the generator test step shown in the report") must be returned.

Return type:  [`ReportData`](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.ReportData "tts.core.project.generator.paramGenerator.ParamGeneratorBase.ReportData (Python class) — This class is a container for the information of the generator test step shown in the report") or None

Info

Overriding this method is **optional**.

GetTargetItemCount()[¶](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.GetTargetItemCount "Link to this definition")  
Implement this method to define the expected number of cycle sets to be generated as information for progress indicators. Will be called for updates throughout the generation. Therefore, you can dynamically return the size of the current task.

Returns:  expected count of cycle sets to be generated

Return type:  int

GetUsedMappingItems()[¶](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.GetUsedMappingItems "Link to this definition")  
Returns the mapping items that will be used during generation.

If mapping items are to be added to the generated parameter sets of an analysis package, they have to be defined here in order to be registered for the stimulation package. Mapping items can be defined here directly, parsed from a file or whatever source, but the complete set of mapping items used during generation has to be returned by this method.

Info

Overriding this method is **optional** and only necessary for parameter set generators used with analysis packages and overwriting mapping items.

Caution

This method is called before any other method (e.g., PreGeneration)! If you read in required data for the mapping during PreGeneration, you have to redesign your code to be called at least once during GetUsedMappingItems.

Returns:  list of mapping items

Return type:  list[[ApiClient.MappingItem](../../general_api/MappingApi/MappingItem.md#ApiClient.MappingItem "ApiClient.MappingItem (Python class) — MappingApi.CreateGenericMappingItem")]

IsValidForAnalysisPackages()[¶](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.IsValidForAnalysisPackages "Link to this definition")  
Returns if usage of parameter set generator is feasible for analysis packages.

If set to ‘True’ and parameter set generator is not feasible for analysis packages, errors will be raised during runtime. If set to ‘False’, the GUI will give direct feedback if the parameter set generator is used for an analysis package.

Returns:  True, if valid for analysis package usage, else False

Return type:  bool

Info

Overriding this method is **optional**.

OnInit(*[packageInfo](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.OnInit.packageInfo "tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.OnInit.packageInfo (Python parameter) — The package info object.")*)[¶](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.OnInit "Link to this definition")  
Implement this method to process information about the package to which the generator belongs. It will be called before [`PreGeneration()`](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.PreGeneration "tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.PreGeneration (Python method) — Implement this method to specify pre generation behavior. This method is called before the generation.") or [`GetDialog()`](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.GetDialog "tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.GetDialog (Python method) — Implement this method to return the configuration dialog of your parameter generator. The dialog should set the generator data.") is called.

Parameters:  packageInfo[¶](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.OnInit.packageInfo "Permalink to this definition")  
The package info object.

Info

Overriding this method is **optional**

PostGeneration()[¶](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.PostGeneration "Link to this definition")  
Implement this method to specify post generation behavior. This method is called after the generation. This method will be called even if an exception occurs during generation (incl. PreGeneration), but not if the project execution is aborted (by the user or because of an “abort on error” setting).

Info

Overriding this method is **optional**.

PreGeneration()[¶](#tts.core.project.generator.paramGenerator.CallbackParamGenerator.CallbackParamGenerator.PreGeneration "Link to this definition")  
Implement this method to specify pre generation behavior. This method is called before the generation.

Info

Overriding this method is **optional**.

## CycleData[¶](#cycledata "Link to this heading")

*class* CycleData[¶](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData "Link to this definition")  
This class is a container for all data, that can be generated during one cycle.

RECORDING_INFO_CLASS[¶](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.RECORDING_INFO_CLASS "Link to this definition")  
alias of [`RecordingInfo`](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.RecordingInfo "tts.core.project.generator.paramGenerator.ParamGeneratorBase.RecordingInfo (Python class) — This class is a container for the information of a recording.")

Attributes[¶](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.Attributes "Link to this definition")  
Returns the dict of attributes.

Returns:  The dict of attributes

Return type:  dict

ConstSet[¶](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.ConstSet "Link to this definition")  
Returns the set of constants.

Returns:  The set of constants.

Return type:  dict

Name[¶](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.Name "Link to this definition")  
Returns the name of this cycle

Returns:  The name of this cycle

Return type:  str

ParamSet[¶](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.ParamSet "Link to this definition")  
Returns the set of parameters.

Returns:  The set of parameters.

Return type:  dict

RecordingInfos[¶](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.RecordingInfos "Link to this definition")  
Returns the dict of recording infos.

Returns:  The dict of recording infos.

Return type:  dict

AddAttribute(*[name](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.AddAttribute.name "tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.AddAttribute.name (Python parameter) — Name of the attribute")*, *[value](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.AddAttribute.value "tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.AddAttribute.value (Python parameter) — Value of the attribute")*)[¶](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.AddAttribute "Link to this definition")  
Adds an attribute to this cycle.

Parameters:  name : str[¶](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.AddAttribute.name "Permalink to this definition")  
Name of the attribute

value : str[¶](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.AddAttribute.value "Permalink to this definition")  
Value of the attribute

AddConst(*[name](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.AddConst.name "tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.AddConst.name (Python parameter) — Name for the constant.")*, *[value](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.AddConst.value "tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.AddConst.value (Python parameter) — Value to assign to this constant.")*)[¶](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.AddConst "Link to this definition")  
Adds a constant to this cycle.

Parameters:  name : str[¶](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.AddConst.name "Permalink to this definition")  
Name for the constant.

value : str | float | int | bool[¶](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.AddConst.value "Permalink to this definition")  
Value to assign to this constant.

AddMappingItem(*[mappingItem](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.AddMappingItem.mappingItem "tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.AddMappingItem.mappingItem (Python parameter) — MappingItem originating from e.g api.GetObjectApi().PackageApi.MappingApi")*)[¶](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.AddMappingItem "Link to this definition")  
Adds mapping item to the mapping space for this cycle.

See also

[Object API](../../general_api/objectApi.md#objectapi)

Parameters:  mappingItem : [ApiClient.MappingItem](../../general_api/MappingApi/MappingItem.md#ApiClient.MappingItem "ApiClient.MappingItem (Python class) — MappingApi.CreateGenericMappingItem")[¶](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.AddMappingItem.mappingItem "Permalink to this definition")  
MappingItem originating from e.g api.GetObjectApi().PackageApi.MappingApi

AddParameter(*[name](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.AddParameter.name "tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.AddParameter.name (Python parameter) — Name for the parameter.")*, *[value](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.AddParameter.value "tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.AddParameter.value (Python parameter) — Value to assign to this parameter.")*)[¶](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.AddParameter "Link to this definition")  
Adds a parameter to this cycle.

Parameters:  name : str[¶](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.AddParameter.name "Permalink to this definition")  
Name for the parameter.

value : str | float | int | bool[¶](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.AddParameter.value "Permalink to this definition")  
Value to assign to this parameter.

AddRecordingInfo(*[recordingGroupName](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.AddRecordingInfo.recordingGroupName "tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.AddRecordingInfo.recordingGroupName (Python parameter) — Name of the recording group.")*, *[path](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.AddRecordingInfo.path "tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.AddRecordingInfo.path (Python parameter) — Path to the recording.")*)[¶](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.AddRecordingInfo "Link to this definition")  
Adds a recording info into a recording group for this cycle. A recording info consists of a recording (path) and some additional information depending on the recording type. The method returns a recording info object, so the additional information can be specified in this object.

Parameters:  recordingGroupName : str[¶](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.AddRecordingInfo.recordingGroupName "Permalink to this definition")  
Name of the recording group.

path : str[¶](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.AddRecordingInfo.path "Permalink to this definition")  
Path to the recording.

Returns:  The recording info object.

Return type:  [*RecordingInfo*](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.RecordingInfo "tts.core.project.generator.paramGenerator.ParamGeneratorBase.RecordingInfo (Python class) — This class is a container for the information of a recording.")

GetAttributes()[¶](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.GetAttributes "Link to this definition")  
Returns the dict of attributes.

Returns:  The dict of attributes

Return type:  dict

GetConstSet()[¶](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.GetConstSet "Link to this definition")  
Returns the set of constants.

Returns:  The set of constants.

Return type:  dict

GetName()[¶](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.GetName "Link to this definition")  
Returns the name of this cycle

Returns:  The name of this cycle

Return type:  str

GetParamSet()[¶](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.GetParamSet "Link to this definition")  
Returns the set of parameters.

Returns:  The set of parameters.

Return type:  dict

GetRecordingInfos()[¶](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.GetRecordingInfos "Link to this definition")  
Returns the dict of recording infos.

Returns:  The dict of recording infos.

Return type:  dict

SetName(*[value](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.SetName.value "tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.SetName.value (Python parameter) — Name for this cycle.")*)[¶](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.SetName "Link to this definition")  
Sets the name of this cycle.

Parameters:  value : str[¶](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.SetName.value "Permalink to this definition")  
Name for this cycle.

UpdateAttribute(*[name](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.UpdateAttribute.name "tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.UpdateAttribute.name (Python parameter) — Name of the attribute")*, *[value](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.UpdateAttribute.value "tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.UpdateAttribute.value (Python parameter) — Value of the attribute")*)[¶](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.UpdateAttribute "Link to this definition")  
Update an attribute

Parameters:  name : str[¶](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.UpdateAttribute.name "Permalink to this definition")  
Name of the attribute

value : str[¶](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData.UpdateAttribute.value "Permalink to this definition")  
Value of the attribute

## OptimizerBase[¶](#module-tts.core.project.generator.paramGenerator.OptimizerBase "Link to this heading")

*class* OptimizerBase[¶](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase "Link to this definition")  
This is the base class for user-defined optimizers. The class is based on the CallbackParamGenerator and extends its functionality with new features:

- Management of minimum and maximum values for the package parameters

- Optional parameter variation before the actual optimization

- A dialog for managing minimum and maximum values, parameter variation and optimizer-specific settings

If a parameter variation is activated, it is executed after calling PreGeneration and before calling Generate. With GetVariationResults the results of the variation can be accessed in the Generate method.

DESCRIPTION = `''`[¶](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.DESCRIPTION "Link to this definition")  
A short description of the parameter generator.

Type:  str

Info: Setting this field is **optional**
ENABLE_PARAMETER_VARIATION = `True`[¶](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.ENABLE_PARAMETER_VARIATION "Link to this definition")  
Enables or disables the support of a parameter variation before the optimization starts.

Type:  boolean

ID = `''`[¶](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.ID "Link to this definition")  
A universally unique identifier to make the parameter generator unique. The ID should be generated using a UUID generator to be unique.

Type:  str

Info: Setting this field is **mandatory**
NAME = `''`[¶](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.NAME "Link to this definition")  
The display name of the parameter generator.

Type:  str

Info: Setting this field is **mandatory**
SERIALIZE : dict[str, tuple[str, str] | tuple[str, str, object]] = `{}`[¶](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.SERIALIZE "Link to this definition")  
Declaration of instance variables of the parameter generator, that are to be exported/imported to/from xml format (e.g. during saving/loading a project). The declaration contains an item for each instance variable in form of an dictionary. Example:

    SERIALIZE = {
                    "foo": ("FOO-VAR", "integer", 23),
                    "bar": ("BAR", "string"),
                    "params: ("PARAMETERS", "list")
                }

The declaration items key must match the name of the corresponding instance variable (e.g. for an instance variable self.foo the item’s key must be “foo”). The item’s value must be a tuple containing at least 2 elements. So the general syntax for a declaration item is:

    ``<variable name>: (<variable alias>, <type alias>, [default value])``

Syntax and meaning of the tuple’s elements are:

- **\<variable alias\>** declares the name of the xml element that is used for the variable’s xml representation.

- **\<type alias\>** keyword specifing the python variable’s type. The following table gives all keywords and their corresponding python type respectively:

  - `boolean`: bool

  - `integer`: int

  - `long`: long

  - `float`: float

  - `string`: str

  - `unicode`: str

PLEASE NOTE: The types `long` and `unicode` are only kept for compatibility. Do not use these in new code.

- **\<default value\>** is an optional element. It specifies the variable’s default value. If the variable’s value equals its default value during export the variable is not exported at all. Conversely, the variable is assigned its default value during import if the xml data does not provide an value for the variable.

Type:  dict

Info: Setting this field is **optional**
api = `None`[¶](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.api "Link to this definition")  
Access to the internal ecu.test API. The API will be assigned at runtime, in order to be independent from ecu.test for testing purposes.

See also

[Internal APIs](../../general_api/api.md#internalapi)

projectPath : str | None = `None`[¶](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.projectPath "Link to this definition")  
Absolute path to the project file containing the generator. In case of direct execution, this is the source project. In case of static generation it is the destination project.

*classmethod* GetDescription()[¶](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.GetDescription "Link to this definition")  
Returns the description of the parameter generator. The description can be specified by setting the class variable [`DESCRIPTION`](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.DESCRIPTION "tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.DESCRIPTION (Python attribute) — A short description of the parameter generator.").

Return type:  str

*classmethod* GetId()[¶](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.GetId "Link to this definition")  
Returns the universally unique identifier of the parameter generator. The identifier should be specified by setting the class variable [`ID`](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.ID "tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.ID (Python attribute) — A universally unique identifier to make the parameter generator unique. The ID should be generated using a UUID generator to be unique.").

Return type:  str

*classmethod* GetName()[¶](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.GetName "Link to this definition")  
Returns the name of the parameter generator. The name should be specified by setting the class variable [`NAME`](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.NAME "tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.NAME (Python attribute) — The display name of the parameter generator.").

Return type:  str

Check()[¶](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.Check "Link to this definition")  
Implement this method to allow the user-implemented generator to be checked.

Returns:  A list of error messages or an empty list if everything is fine.

Return type:  list\<str\>

Info

Overriding this method is **optional**.

CreateCycleData(*[paramSet](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.CreateCycleData.paramSet "tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.CreateCycleData.paramSet (Python parameter) — A set of parameters to parameterize a package.")=`None`*, *[constSet](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.CreateCycleData.constSet "tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.CreateCycleData.constSet (Python parameter) — A set of constants that will be set before running a package.")=`None`*, *[name](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.CreateCycleData.name "tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.CreateCycleData.name (Python parameter) — A name for this cycle that will be displayed in the report.")=`None`*)[¶](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.CreateCycleData "Link to this definition")  
Method, to create an instance of class CycleData.

Parameters:  paramSet : dict[¶](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.CreateCycleData.paramSet "Permalink to this definition")  
A set of parameters to parameterize a package.

constSet : dict[¶](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.CreateCycleData.constSet "Permalink to this definition")  
A set of constants that will be set before running a package. (optional)

name : str[¶](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.CreateCycleData.name "Permalink to this definition")  
A name for this cycle that will be displayed in the report. (optional)

Returns:  The cycle data object

Return type:  [`CycleData`](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData "tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData (Python class) — This class is a container for all data, that can be generated during one cycle.")

DryGenerationEnabled()[¶](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.DryGenerationEnabled "Link to this definition")  
Returns True, if the generator runs in dry generation mode. In this mode, the generator is used to generate a project with static parameter records.

Return type:  bool

Generate(*[testRunFunction](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.Generate.testRunFunction "tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.Generate.testRunFunction (Python parameter) — If this function is called, an ecu.test test run is started.")*)[¶](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.Generate "Link to this definition")  
Implement this method for generating parameter sets. Each parameter set must be an object of [`CycleData`](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData "tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData (Python class) — This class is a container for all data, that can be generated during one cycle.") and can be created with the method [`CreateCycleData()`](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.CreateCycleData "tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.CreateCycleData (Python method) — Method, to create an instance of class CycleData."). A test run is executed by calling the testRunFunction.

Parameters:  testRunFunction[¶](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.Generate.testRunFunction "Permalink to this definition")  
If this function is called, an ecu.test test run is started. The function expects one or more parameter sets and returns a list of dictionaries containing the return variables of the package with their result values. A parameter set must be an instance of [`CycleData`](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData "tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData (Python class) — This class is a container for all data, that can be generated during one cycle.") which can be created with the method [`CreateCycleData()`](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.CreateCycleData "tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.CreateCycleData (Python method) — Method, to create an instance of class CycleData."). If the test run is aborted by ecu.test, an abort error occurs. This error should only be caught for the purpose of cleaning up.

Info

Overriding this method is **mandatory**

GetDialog()[¶](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.GetDialog "Link to this definition")  
Implement this method to return the configuration dialog of your parameter generator. The dialog should set the generator data.

Return type:  wx.Dialog or None

Info

Overriding this method is **optional**.

GetLastReturnSets()[¶](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.GetLastReturnSets "Link to this definition")  
Returns a list of all return sets from the last ecu.test test run.

This method only returns a result if the generator is not running in dry generation mode and it is called within the L{Generate()} method after at least one parameter set has been executed (by calling the testRunFunction in the L{Generate()} method). In all other circumstances, the method always returns an empty list.

Return type:  list of dicts

GetMinMaxValues()[¶](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.GetMinMaxValues "Link to this definition")  
Returns the specified minimum and maximum values for the package parameters. A dictionary is returned with the parameter names as keys and lists with minimum and maximum as values. Example:

    {'speed': [100, 120],
     'distance': [1000, 1500]
    }

Return type:  dict

GetParameterText()[¶](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.GetParameterText "Link to this definition")  
Implement this method to show the parameters of your param generator in properties column.

Returns:  parameter text

Return type:  str

Info

Overriding this method is **optional**.

GetReportData()[¶](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.GetReportData "Link to this definition")  
Implement this method to set the information for the generator test step in the report. An object of type [`ReportData`](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.ReportData "tts.core.project.generator.paramGenerator.ParamGeneratorBase.ReportData (Python class) — This class is a container for the information of the generator test step shown in the report") must be returned.

Return type:  [`ReportData`](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.ReportData "tts.core.project.generator.paramGenerator.ParamGeneratorBase.ReportData (Python class) — This class is a container for the information of the generator test step shown in the report") or None

Info

Overriding this method is **optional**.

GetTargetItemCount()[¶](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.GetTargetItemCount "Link to this definition")  
Implement this method to define the expected number of cycle sets to be generated as information for progress indicators. Will be called for updates throughout the generation. Therefore, you can dynamically return the size of the current task.

Returns:  expected count of cycle sets to be generated

Return type:  int

GetUsedMappingItems()[¶](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.GetUsedMappingItems "Link to this definition")  
Returns the mapping items that will be used during generation.

If mapping items are to be added to the generated parameter sets of an analysis package, they have to be defined here in order to be registered for the stimulation package. Mapping items can be defined here directly, parsed from a file or whatever source, but the complete set of mapping items used during generation has to be returned by this method.

Info

Overriding this method is **optional** and only necessary for parameter set generators used with analysis packages and overwriting mapping items.

Caution

This method is called before any other method (e.g., PreGeneration)! If you read in required data for the mapping during PreGeneration, you have to redesign your code to be called at least once during GetUsedMappingItems.

Returns:  list of mapping items

Return type:  list[[ApiClient.MappingItem](../../general_api/MappingApi/MappingItem.md#ApiClient.MappingItem "ApiClient.MappingItem (Python class) — MappingApi.CreateGenericMappingItem")]

GetVariationResults()[¶](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.GetVariationResults "Link to this definition")  
Returns the results of the parameter variation as a list of [`VariationResult`](#tts.core.project.generator.paramGenerator.OptimizerBase.VariationResult "tts.core.project.generator.paramGenerator.OptimizerBase.VariationResult (Python class) — This class is a container for the input and result data of one variation.") objects. The method only returns results if it is called in the generator method and the parameter variation is activated. In all other circumstances, an empty list is returned.

Return type:  list\<[`VariationResult`](#tts.core.project.generator.paramGenerator.OptimizerBase.VariationResult "tts.core.project.generator.paramGenerator.OptimizerBase.VariationResult (Python class) — This class is a container for the input and result data of one variation.")\>

IsValidForAnalysisPackages()[¶](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.IsValidForAnalysisPackages "Link to this definition")  
Returns if usage of parameter set generator is feasible for analysis packages.

If set to ‘True’ and parameter set generator is not feasible for analysis packages, errors will be raised during runtime. If set to ‘False’, the GUI will give direct feedback if the parameter set generator is used for an analysis package.

Returns:  True, if valid for analysis package usage, else False

Return type:  bool

Info

Overriding this method is **optional**.

OnInit(*[packageInfo](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.OnInit.packageInfo "tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.OnInit.packageInfo (Python parameter) — The package info object.")*)[¶](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.OnInit "Link to this definition")  
Implement this method to process information about the package to which the generator belongs. It will be called before [`PreGeneration()`](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.PreGeneration "tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.PreGeneration (Python method) — Implement this method to specify pre generation behavior. This method is called before the generation.") or [`GetDialog()`](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.GetDialog "tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.GetDialog (Python method) — Implement this method to return the configuration dialog of your parameter generator. The dialog should set the generator data.") is called.

Parameters:  packageInfo[¶](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.OnInit.packageInfo "Permalink to this definition")  
The package info object.

Info

Overriding this method is **optional**

PostGeneration()[¶](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.PostGeneration "Link to this definition")  
Implement this method to specify post generation behavior. This method is called after the generation. This method will be called even if an exception occurs during generation (incl. PreGeneration), but not if the project execution is aborted (by the user or because of an “abort on error” setting).

Info

Overriding this method is **optional**.

PreGeneration()[¶](#tts.core.project.generator.paramGenerator.OptimizerBase.OptimizerBase.PreGeneration "Link to this definition")  
Implement this method to specify pre generation behavior. This method is called before the generation.

Info

Overriding this method is **optional**.

*class* VariationResult[¶](#tts.core.project.generator.paramGenerator.OptimizerBase.VariationResult "Link to this definition")  
This class is a container for the input and result data of one variation.

CycleData[¶](#tts.core.project.generator.paramGenerator.OptimizerBase.VariationResult.CycleData "Link to this definition")  
Returns the cycle data object that contains the input data for the variation.

Returns:  The cycle data object

Return type:  [`CycleData`](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData "tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData (Python class) — This class is a container for all data, that can be generated during one cycle.")

ReturnSet[¶](#tts.core.project.generator.paramGenerator.OptimizerBase.VariationResult.ReturnSet "Link to this definition")  
Returns the return set of the package execution for the variation.

Returns:  The return set as a dictionary

Return type:  dict, None

## PackageInfo[¶](#module-tts.core.project.projectStep.PackageInfo "Link to this heading")

*class* PackageInfo[¶](#tts.core.project.projectStep.PackageInfo.PackageInfo "Link to this definition")  
Provides information about a package, like name, variables, etc.

GetName()[¶](#tts.core.project.projectStep.PackageInfo.PackageInfo.GetName "Link to this definition")  
Returns the package name.

Returns:  package name without extension

Return type:  str

GetParameterVariables()[¶](#tts.core.project.projectStep.PackageInfo.PackageInfo.GetParameterVariables "Link to this definition")  
Returns a list of all variables defined in the package and set as a parameter.

Returns:  List of all defined parameters

Return type:  list \<`Variable`\>

GetPath()[¶](#tts.core.project.projectStep.PackageInfo.PackageInfo.GetPath "Link to this definition")  
Returns the path of the package file as absolute path.

Returns:  absolute package path

Return type:  str

GetReturnVariables()[¶](#tts.core.project.projectStep.PackageInfo.PackageInfo.GetReturnVariables "Link to this definition")  
Returns a list of all variables defined in the package and set as a return variable.

Returns:  List of all defined return variables

Return type:  list \<`Variable`\>

GetVariables()[¶](#tts.core.project.projectStep.PackageInfo.PackageInfo.GetVariables "Link to this definition")  
Returns a list of all variables defined in the package.

Returns:  List of all defined variables

Return type:  list \<`Variable`\>

## RecordingInfo[¶](#recordinginfo "Link to this heading")

*class* RecordingInfo[¶](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.RecordingInfo "Link to this definition")  
This class is a container for the information of a recording.

FormatDetails[¶](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.RecordingInfo.FormatDetails "Link to this definition")  
Returns the format details of the recording.

Returns:  Format details of the recording.

Return type:  str

Path[¶](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.RecordingInfo.Path "Link to this definition")  
Returns the path to the recording.

Returns:  Path to the recording.

Return type:  str

RecordingName[¶](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.RecordingInfo.RecordingName "Link to this definition")  
Returns the name of the recording.

Returns:  Name of the recording.

Return type:  str

RecordingNumber[¶](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.RecordingInfo.RecordingNumber "Link to this definition")  
Returns the number of the recording.

Returns:  Number of the recording.

Return type:  int

RecordingType[¶](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.RecordingInfo.RecordingType "Link to this definition")  
Returns the type of the recording.

Returns:  Type of the recording.

Return type:  str

GetFormatDetails()[¶](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.RecordingInfo.GetFormatDetails "Link to this definition")  
Returns the format details of the recording.

Returns:  Format details of the recording.

Return type:  str

GetPath()[¶](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.RecordingInfo.GetPath "Link to this definition")  
Returns the path to the recording.

Returns:  Path to the recording.

Return type:  str

GetRecordingName()[¶](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.RecordingInfo.GetRecordingName "Link to this definition")  
Returns the name of the recording.

Returns:  Name of the recording.

Return type:  str

GetRecordingNumber()[¶](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.RecordingInfo.GetRecordingNumber "Link to this definition")  
Returns the number of the recording.

Returns:  Number of the recording.

Return type:  int

GetRecordingType()[¶](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.RecordingInfo.GetRecordingType "Link to this definition")  
Returns the type of the recording.

Returns:  Type of the recording.

Return type:  str

SetFormatDetails(*[formatDetails](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.RecordingInfo.SetFormatDetails.formatDetails "tts.core.project.generator.paramGenerator.ParamGeneratorBase.RecordingInfo.SetFormatDetails.formatDetails (Python parameter) — Format details of the recording.")*)[¶](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.RecordingInfo.SetFormatDetails "Link to this definition")  
Sets the format details of the recording.

Parameters:  formatDetails : str[¶](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.RecordingInfo.SetFormatDetails.formatDetails "Permalink to this definition")  
Format details of the recording.

SetRecordingName(*[recordingName](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.RecordingInfo.SetRecordingName.recordingName "tts.core.project.generator.paramGenerator.ParamGeneratorBase.RecordingInfo.SetRecordingName.recordingName (Python parameter) — Name of the recording.")*)[¶](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.RecordingInfo.SetRecordingName "Link to this definition")  
Sets the name of the recording.

Parameters:  recordingName : str[¶](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.RecordingInfo.SetRecordingName.recordingName "Permalink to this definition")  
Name of the recording.

SetRecordingNumber(*[recordingNumber](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.RecordingInfo.SetRecordingNumber.recordingNumber "tts.core.project.generator.paramGenerator.ParamGeneratorBase.RecordingInfo.SetRecordingNumber.recordingNumber (Python parameter) — Number of the recording.")*)[¶](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.RecordingInfo.SetRecordingNumber "Link to this definition")  
Sets the number of the recording.

Parameters:  recordingNumber : str[¶](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.RecordingInfo.SetRecordingNumber.recordingNumber "Permalink to this definition")  
Number of the recording.

SetRecordingType(*[recordingType](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.RecordingInfo.SetRecordingType.recordingType "tts.core.project.generator.paramGenerator.ParamGeneratorBase.RecordingInfo.SetRecordingType.recordingType (Python parameter) — Type of the recording.")*)[¶](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.RecordingInfo.SetRecordingType "Link to this definition")  
Sets the type of the recording.

Parameters:  recordingType : str[¶](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.RecordingInfo.SetRecordingType.recordingType "Permalink to this definition")  
Type of the recording.

`\_\_init\_\_`(*[path](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.RecordingInfo.__init__.path "tts.core.project.generator.paramGenerator.ParamGeneratorBase.RecordingInfo.__init__.path (Python parameter) — Path to the recording.")*)[¶](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.RecordingInfo.__init__ "Link to this definition")  
Method, to initialize an instance of this class.

Parameters:  path : str[¶](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.RecordingInfo.__init__.path "Permalink to this definition")  
Path to the recording.

## ReportData[¶](#reportdata "Link to this heading")

*class* ReportData[¶](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.ReportData "Link to this definition")  
This class is a container for the information of the generator test step shown in the report

Comment[¶](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.ReportData.Comment "Link to this definition")  
Returns the string for the comment column

Returns:  String for the comment column

Return type:  str

Value[¶](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.ReportData.Value "Link to this definition")  
Returns the string for the value column

Returns:  String for the value column

Return type:  str

GetComment()[¶](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.ReportData.GetComment "Link to this definition")  
Returns the string for the comment column

Returns:  String for the comment column

Return type:  str

GetValue()[¶](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.ReportData.GetValue "Link to this definition")  
Returns the string for the value column

Returns:  String for the value column

Return type:  str

SetComment(*[comment](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.ReportData.SetComment.comment "tts.core.project.generator.paramGenerator.ParamGeneratorBase.ReportData.SetComment.comment (Python parameter) — String for the comment column")*)[¶](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.ReportData.SetComment "Link to this definition")  
Sets the string for the comment column

Parameters:  comment : str[¶](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.ReportData.SetComment.comment "Permalink to this definition")  
String for the comment column

SetValue(*[value](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.ReportData.SetValue.value "tts.core.project.generator.paramGenerator.ParamGeneratorBase.ReportData.SetValue.value (Python parameter) — String for the value column")*)[¶](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.ReportData.SetValue "Link to this definition")  
Sets the string for the value column

Parameters:  value : str[¶](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.ReportData.SetValue.value "Permalink to this definition")  
String for the value column

## Variable[¶](#variable "Link to this heading")

*class* Variable  
Description  
returns the description of this variable.

Returns:  the description of this variable

Return type:  str

InitValue  
returns the initial value of this variable.

Returns:  the initial value of this variable

Return type:  str

Name  
returns the name of this variable.

Returns:  the name of this variable

Return type:  str

VariableType  
Returns:  type of this variable

Return type:  str

GetDescription()  
returns the description of this variable.

Returns:  the description of this variable

Return type:  str

GetInitValue()  
returns the initial value of this variable.

Returns:  the initial value of this variable

Return type:  str

GetName()  
returns the name of this variable.

Returns:  the name of this variable

Return type:  str

GetVariableType()  
Returns:  type of this variable

Return type:  str

IsInput()  
Returns True if this variable is an input parameter, otherwise False

IsOutput()  
Returns True if this variable is an output parameter, otherwise False

*class* VariableType  
Defines type of the variable.

Class var UNDEFINED:  
‘Undefined’

Class var NUMERIC:  
‘Numeric’

Class var STRING:  
‘String’

Class var ENUM:  
‘Enum’

Class var TEXTTABLE:  
‘Texttable’

Class var BOOL:  
‘Boolean’

## VariationResult[¶](#variationresult "Link to this heading")

*class* VariationResult  
This class is a container for the input and result data of one variation.

CycleData  
Returns the cycle data object that contains the input data for the variation.

Returns:  The cycle data object

Return type:  [`CycleData`](#tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData "tts.core.project.generator.paramGenerator.ParamGeneratorBase.CycleData (Python class) — This class is a container for all data, that can be generated during one cycle.")

ReturnSet  
Returns the return set of the package execution for the variation.

Returns:  The return set as a dictionary

Return type:  dict, None

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
