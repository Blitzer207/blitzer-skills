# Object based program API[¶](#object-based-program-api "Link to this heading")

The object based program API is designed to read, create or modify ecu.test relevant files. With it you can create your own scripts in a Python development environment of your choice. The design follows an object oriented approach. To execute your script, a started ecu.test is needed.

To use it from an external Python, please extend your `PYTHONPATH` to include *`<path to program>`*`\Templates\ApiClient` in order to be able to import it as shown in the example below. The ApiClient is Python 2 and Python 3 compatible. To use the Object API from within ecu.test use `api.ObjectApi`

Note

The Object API is for dealing with ecu.test relevant files only, e.g. Packages, Projects, TBC or TCF. If you want to execute test cases, you need to use the [REST-API](rest-api.md#rest-api) or the [COM-API](com-api.md#com-api).

Examples for coding with the Object API can be found here: [Code Examples Object API](objectApiExamples.md#objectapiexamples)

## Java-Client[¶](#java-client "Link to this heading")

It is also possible to use the API in Java the same way as in Python. Please use the `ApiClient-X.Y-SNAPSHOT.jar` from the same directory for that. (where X and Y are the major and minor version of your ecu.test installation) Please note, default arguments are not supported. Instead of the Python value `None`, the Java value `null` must be used / will be returned.

The following snippet is the same example translated in Java. On a command line one can use `javac -cp ApiClient-X.Y-SNAPSHOT.jar ApiClientExample.java`to compile and `java -cp .;ApiClient-X.Y-SNAPSHOT.jar ApiClientExample`to run the example.

    import de.tracetronic.tts.apiClient.stubs.*;

    public final class ApiClientTest {
        public void testTcf() {
            String tcfFile = "C:\\Data\\ECU-TEST\\Configurations\\Testconfiguration.tcf";
            ApiClient api = new ApiClient();
            TestConfiguration tcf = api.ConfigurationApi.OpenTestConfiguration(tcfFile);
            Model model = tcf.Platform.ModelAccess.Get("Plant model");
            model.SetFile("NewModelFile.mdl");
            tcf.Save(tcfFile);
        }

        public void testPackage() {
            String packageFile = "C:\\Data\\ECU-TEST\\Packages\\Testpackage.pkg";
            ApiClient api = new ApiClient();
            Package testPackage = api.PackageApi.OpenPackage(packageFile);

            for (TestStep ts : testPackage.GetTestSteps()) {
                if (ts instanceof TsRead) {
                    TsRead tsCasted = (TsRead) ts;
                    if (tsCasted.GetExpectationExpression() == "abs(3 - value) <= 0.5") {
                        tsCasted.SetExpectationExpression("abs(3 - value) <= 1");
                    }
                }
            }
            testPackage.Save(packageFile);
        }

        public static void main(String[] args) {
            ApiClientTest client = new ApiClientTest();
            client.testTcf();
            client.testPackage();
        }
    }

## DotNet-Client[¶](#dotnet-client "Link to this heading")

It is also possible to use the API in C# and Visual Basic .Net the same way as in Python. Please add a reference to the `ApiClient.dll` for that. It can be found in the same directory as the Python and Java client. Instead of the Python value `None`, the C# value `null` or the Visual Basic value `Nothing` must be used / will be returned.

The following snippet is the example translated to C#.

    using TraceTronic.ObjectApi.stubs;

    namespace ApiTest
    {
        class Program
        {
            public static void TestTcf()
            {
                string tcfFile = "C:\\Data\\ECU-TEST\\Configurations\\Testconfiguration.tcf";
                var q = System.IO.File.Exists(tcfFile);
                ApiClient api = new ApiClient();
                TestConfiguration tcf = api.ConfigurationApi.OpenTestConfiguration(tcfFile);
                Model model = tcf.Platform.ModelAccess.Get("Plant model");
                model.SetFile("NewModelFile.mdl");
                tcf.Save(tcfFile);
            }

            public static void TestPackage()
            {
                string packageFile = "C:\\Data\\ECU-TEST\\Packages\\Testpackage.pkg";
                ApiClient api = new ApiClient();
                Package testPackage = api.PackageApi.OpenPackage(packageFile);

                foreach (TestStep ts in testPackage.GetTestSteps())
                {
                    if (ts is TsRead tsCasted)
                    {
                        if (tsCasted.GetExpectationExpression() == "abs(3 - value) <= 0.5")
                        {
                            tsCasted.SetExpectationExpression("abs(3 - value) <= 1");
                        }
                    }
                }
                testPackage.Save(packageFile);
            }

            static void Main(string[] args)
            {
                TestTcf();
                TestPackage();
            }
        }
    }

The following snippet is the example translated to Visual Basic .Net.

    Imports TraceTronic.ObjectApi.stubs

    Module Module1
        Sub TestTcf()
            Dim tcfFile As String = "C:\\Data\\ECU-TEST\\Configurations\\Testconfiguration.tcf"
            Dim api As New ApiClient()
            Dim tcf As TestConfiguration = api.ConfigurationApi.OpenTestConfiguration(tcfFile)
            Dim model As Model = tcf.Platform.ModelAccess.Get("Plant model")
            model.SetFile("NewModelFile.mdl")
            tcf.Save(tcfFile)
        End Sub

        Sub TestPackage()
            Dim packageFile As String = "C:\\Data\\ECU-TEST\\Packages\\Testpackage.pkg"
            Dim api As ApiClient = New ApiClient()
            Dim testPackage As Package = api.PackageApi.OpenPackage(packageFile)

            For Each ts As TestStep In testPackage.GetTestSteps()
                If TypeOf ts Is TsRead Then
                    Dim tsCasted As TsRead = CType(ts, TsRead)
                    If tsCasted.GetExpectationExpression() Is "abs(3 - value) <= 0.5" Then
                        tsCasted.SetExpectationExpression("abs(3 - value) <= 1")
                    End If
                End If
            Next

            testPackage.Save(packageFile)

        End Sub

        Sub Main()
            TestTcf()
            TestPackage()
        End Sub

    End Module

## API entry point[¶](#api-entry-point "Link to this heading")

Part of the [Object based program API](#objectapi)

### ApiClient[¶](#apiclient "Link to this heading")

*class* ApiClient[¶](#ApiClient.ApiClient "Link to this definition")  
Entry point for object based api.

AnalysisJobApi[¶](#ApiClient.ApiClient.AnalysisJobApi "Link to this definition")  
Returns the AnalysisJobApi namespace

Returns:  AnalysisJobApi namespace

Return type:  [`AnalysisJobApi`](AnalysisJobApi.md#ApiClient.AnalysisJobApi "ApiClient.AnalysisJobApi")

ArtifactApi[¶](#ApiClient.ApiClient.ArtifactApi "Link to this definition")  
Returns the ArtifactApi namespace.

Returns:  ArtifactApi namespace

Return type:  [`ArtifactApi`](ArtifactApi.md#ApiClient.ArtifactApi "ApiClient.ArtifactApi")

ConfigurationApi[¶](#ApiClient.ApiClient.ConfigurationApi "Link to this definition")  
Returns the ConfigurationApi namespace.

Returns:  ConfigurationApi namespace

Return type:  [`ConfigurationApi`](ConfigurationApi.md#ApiClient.ConfigurationApi "ApiClient.ConfigurationApi")

GlobalMappingApi[¶](#ApiClient.ApiClient.GlobalMappingApi "Link to this definition")  
Returns the GlobalMappingApi namespace.

Returns:  GlobalMappingApi namespace

Return type:  [`GlobalMappingApi`](GlobalMappingApi.md#ApiClient.GlobalMappingApi "ApiClient.GlobalMappingApi")

MigrationApi[¶](#ApiClient.ApiClient.MigrationApi "Link to this definition")  
Returns the MigrationApi namespace.

Returns:  MigrationApi namespace

Return type:  [`MigrationApi`](MigrationApi.md#ApiClient.MigrationApi "ApiClient.MigrationApi")

MultimediaApi[¶](#ApiClient.ApiClient.MultimediaApi "Link to this definition")  
Returns the MultimediaApi namespace.

Returns:  MultimediaApi namespace

Return type:  [`MultimediaApi`](MultimediaApi.md#ApiClient.MultimediaApi "ApiClient.MultimediaApi")

PackageApi[¶](#ApiClient.ApiClient.PackageApi "Link to this definition")  
Returns the PackageApi namespace.

Returns:  PackageApi namespace

Return type:  [`PackageApi`](PackageApi.md#ApiClient.PackageApi "ApiClient.PackageApi")

ParameterApi[¶](#ApiClient.ApiClient.ParameterApi "Link to this definition")  
Returns the ParameterApi namespace.

Returns:  ParameterApi namespace

Return type:  [`ParameterApi`](ParameterApi.md#ApiClient.ParameterApi "ApiClient.ParameterApi")

ProjectApi[¶](#ApiClient.ApiClient.ProjectApi "Link to this definition")  
Returns the ProjectApi namespace.

Returns:  ProjectApi namespace

Return type:  [`ProjectApi`](ProjectApi.md#ApiClient.ProjectApi "ApiClient.ProjectApi")

RelationApi[¶](#ApiClient.ApiClient.RelationApi "Link to this definition")  
Returns the RelationApi namespace.

Returns:  RelationApi namespace

Return type:  [`RelationApi`](RelationApi.md#ApiClient.RelationApi "ApiClient.RelationApi")

ReportApi[¶](#ApiClient.ApiClient.ReportApi "Link to this definition")  
Returns the ReportApi namespace.

Returns:  ReportApi namespace

Return type:  [`ReportApi`](ReportApi.md#ApiClient.ReportApi "ApiClient.ReportApi")

SignalDescriptionApi[¶](#ApiClient.ApiClient.SignalDescriptionApi "Link to this definition")  
Returns the SignalDescriptionApi namespace.

Returns:  SignalDescriptionApi namespace

Return type:  [`SignalDescriptionApi`](SignalDescriptionApi.md#ApiClient.SignalDescriptionApi "ApiClient.SignalDescriptionApi")

TraceFileApi[¶](#ApiClient.ApiClient.TraceFileApi "Link to this definition")  
Returns the TraceFileApi namespace.

Returns:  TraceFileApi namespace

Return type:  [`TraceFileApi`](TraceFileApi.md#ApiClient.TraceFileApi "ApiClient.TraceFileApi")

TraceStepTemplateApi[¶](#ApiClient.ApiClient.TraceStepTemplateApi "Link to this definition")  
Returns the TraceStepTemplateApi namespace.

Returns:  TraceStepTemplateApi namespace

Return type:  [`TraceStepTemplateApi`](TraceStepTemplateApi.md#ApiClient.TraceStepTemplateApi "ApiClient.TraceStepTemplateApi")

WorkspaceApi[¶](#ApiClient.ApiClient.WorkspaceApi "Link to this definition")  
Returns the WorkspaceApi namespace.

Returns:  WorkspaceApi namespace

Return type:  [`WorkspaceApi`](WorkspaceApi.md#ApiClient.WorkspaceApi "ApiClient.WorkspaceApi")

GetApplicationVersion()[¶](#ApiClient.ApiClient.GetApplicationVersion "Link to this definition")  
Returns the version of ecu.test.

Returns:  ecu.test version

Return type:  str

GetClientVersion()[¶](#ApiClient.ApiClient.GetClientVersion "Link to this definition")  
Returns the version of the object based api client.

Returns:  client version

Return type:  str

## Table Of Contents[¶](#table-of-contents "Link to this heading")

- [API for Analysis Jobs](AnalysisJobApi.md)
  - [AnalysisJobApi](AnalysisJobApi.md#analysisjobapi)
  - [AnalysisJob](AnalysisJobApi.md#analysisjob)
  - [AnalysisJobGenericSignal](AnalysisJobApi.md#analysisjobgenericsignal)
  - [AnalysisJobRecording](AnalysisJobApi.md#analysisjobrecording)
- [API for Artifacts](ArtifactApi.md)
  - [ArtifactApi](ArtifactApi.md#artifactapi)
  - [LocalArtifactReference](ArtifactApi.md#localartifactreference)
  - [TestGuideArtifactReference](ArtifactApi.md#testguideartifactreference)
- [API for Project Components](ComponentApi.md)
  - [ComponentApi](ComponentApi.md#componentapi)
  - [AnalysisPackageCall](ComponentApi.md#analysispackagecall)
  - [ParameterGenerator](ComponentApi.md#parametergenerator)
  - [ProjectComponent](ComponentApi.md#projectcomponent)
  - [ParameterSetAnalysisPackage](ComponentApi.md#parametersetanalysispackage)
  - [GlobalConstants](ComponentApi.md#globalconstants)
  - [ParameterSetMapping](ComponentApi.md#parametersetmapping)
  - [MappingFiles](ComponentApi.md#mappingfiles)
  - [ArtifactReference](ComponentApi.md#artifactreference)
  - [PackageParameters](ComponentApi.md#packageparameters)
  - [ParameterSetBase](ComponentApi.md#parametersetbase)
  - [StimulationPackageCall](ComponentApi.md#stimulationpackagecall)
  - [ParameterVariationGeneratorComponent](ComponentApi.md#parametervariationgeneratorcomponent)
  - [AnalysisPackageMappingCall](ComponentApi.md#analysispackagemappingcall)
  - [AnalysisBindings](ComponentApi.md#analysisbindings)
  - [SignalGroupReference](ComponentApi.md#signalgroupreference)
  - [AssignedSignal](ComponentApi.md#assignedsignal)
  - [ConfigChange](ComponentApi.md#configchange)
  - [PackageCall](ComponentApi.md#packagecall)
  - [ProjectCall](ComponentApi.md#projectcall)
  - [ProjectFolder](ComponentApi.md#projectfolder)
  - [PackageGenerator](ComponentApi.md#packagegenerator)
  - [ProjectGenerator](ComponentApi.md#projectgenerator)
- [API for Configurations](ConfigurationApi.md)
  - [ConfigurationApi](ConfigurationApi.md#configurationapi)
  - [TestBenchConfiguration](ConfigurationApi.md#testbenchconfiguration)
  - [ToolHost](ConfigurationApi.md#toolhost)
  - [Tool](ConfigurationApi.md#tool)
  - [Port](ConfigurationApi.md#port)
  - [PropertySet](ConfigurationApi.md#propertyset)
  - [Property](ConfigurationApi.md#property)
  - [TestConfiguration](ConfigurationApi.md#testconfiguration)
  - [BusAccess](ConfigurationApi.md#busaccess)
  - [Bus](ConfigurationApi.md#bus)
  - [Common](ConfigurationApi.md#common)
  - [ControlUnits](ConfigurationApi.md#controlunits)
  - [ControlUnit](ConfigurationApi.md#controlunit)
  - [DiagSettings](ConfigurationApi.md#diagsettings)
  - [CanIsoTpSettings](ConfigurationApi.md#canisotpsettings)
  - [DoIpSettings](ConfigurationApi.md#doipsettings)
  - [FrTpSettings](ConfigurationApi.md#frtpsettings)
  - [UdsSettings](ConfigurationApi.md#udssettings)
  - [Environment](ConfigurationApi.md#environment)
  - [EnvComAccess](ConfigurationApi.md#envcomaccess)
  - [EnvComData](ConfigurationApi.md#envcomdata)
  - [EnvSimAccess](ConfigurationApi.md#envsimaccess)
  - [EnvSimData](ConfigurationApi.md#envsimdata)
  - [Execution](ConfigurationApi.md#execution)
  - [MediaAccess](ConfigurationApi.md#mediaaccess)
  - [Media](ConfigurationApi.md#media)
  - [Platform](ConfigurationApi.md#platform)
  - [FailureSimulationAccess](ConfigurationApi.md#failuresimulationaccess)
  - [FailureSimulation](ConfigurationApi.md#failuresimulation)
  - [FunctionAccess](ConfigurationApi.md#functionaccess)
  - [Function](ConfigurationApi.md#function)
  - [ModelAccess](ConfigurationApi.md#modelaccess)
  - [Model](ConfigurationApi.md#model)
  - [ReportData](ConfigurationApi.md#reportdata)
  - [ReportFormat](ConfigurationApi.md#reportformat)
  - [UserReportData](ConfigurationApi.md#userreportdata)
  - [Change](ConfigurationApi.md#change)
  - [ValueDifference](ConfigurationApi.md#valuedifference)
- [API for Expectations](ExpectationApi.md)
  - [ExpectationApi](ExpectationApi.md#expectationapi)
  - [AudioExpectation](ExpectationApi.md#audioexpectation)
  - [BinaryExpressionExpectation](ExpectationApi.md#binaryexpressionexpectation)
  - [BitStreamExpectation](ExpectationApi.md#bitstreamexpectation)
  - [NumericExpectation](ExpectationApi.md#numericexpectation)
  - [BitStreamExpressionExpectation](ExpectationApi.md#bitstreamexpressionexpectation)
  - [BooleanExpectation](ExpectationApi.md#booleanexpectation)
  - [ByteStreamExpectation](ExpectationApi.md#bytestreamexpectation)
  - [ByteStreamExpressionExpectation](ExpectationApi.md#bytestreamexpressionexpectation)
  - [CurveAllExpectation](ExpectationApi.md#curveallexpectation)
  - [Expectation](ExpectationApi.md#expectation)
  - [DTCListExpectation](ExpectationApi.md#dtclistexpectation)
  - [ExpressionExpectationBase](ExpectationApi.md#expressionexpectationbase)
  - [ExpressionExpectation](ExpectationApi.md#expressionexpectation)
  - [ManualExpression](ExpectationApi.md#manualexpression)
  - [NumericExpressionExpectation](ExpectationApi.md#numericexpressionexpectation)
  - [StringExpressionExpectation](ExpectationApi.md#stringexpressionexpectation)
  - [PresentExpectation](ExpectationApi.md#presentexpectation)
  - [NotPresentExpectation](ExpectationApi.md#notpresentexpectation)
  - [StringExpectation](ExpectationApi.md#stringexpectation)
  - [StringListExpectation](ExpectationApi.md#stringlistexpectation)
  - [VectorSingleExpectation](ExpectationApi.md#vectorsingleexpectation)
  - [CurveSingleExpectation](ExpectationApi.md#curvesingleexpectation)
  - [MatrixSingleExpectation](ExpectationApi.md#matrixsingleexpectation)
  - [MapSingleExpectation](ExpectationApi.md#mapsingleexpectation)
  - [AllExpectation](ExpectationApi.md#allexpectation)
  - [VectorAllExpectation](ExpectationApi.md#vectorallexpectation)
  - [MatrixAllExpectation](ExpectationApi.md#matrixallexpectation)
  - [MapAllExpectation](ExpectationApi.md#mapallexpectation)
  - [ImageExpectation](ExpectationApi.md#imageexpectation)
- [API for Expressions](ExpressionApi.md)
  - [ExpressionApi](ExpressionApi.md#expressionapi)
  - [CurveExpression](ExpressionApi.md#curveexpression)
  - [Expression](ExpressionApi.md#expression)
  - [KeywordValueExpression](ExpressionApi.md#keywordvalueexpression)
  - [ExpressionValue](ExpressionApi.md#expressionvalue)
  - [MatrixExpression](ExpressionApi.md#matrixexpression)
  - [MapExpression](ExpressionApi.md#mapexpression)
  - [VectorExpression](ExpressionApi.md#vectorexpression)
- [API for Global Mappings](GlobalMappingApi.md)
  - [GlobalMappingApi](GlobalMappingApi.md#globalmappingapi)
  - [GlobalMapping](GlobalMappingApi.md#globalmapping)
- [API for Mappings](MappingApi.md)
  - [MappingApi](MappingApi.md#mappingapi)
  - [AnalysisPackageMappingItem](MappingApi.md#analysispackagemappingitem)
  - [Mapping](MappingApi.md#mapping)
  - [MappingItem](MappingApi.md#mappingitem)
  - [GenericMappingItem](MappingApi.md#genericmappingitem)
  - [PackageMappingItem](MappingApi.md#packagemappingitem)
  - [GenericPackageMappingItem](MappingApi.md#genericpackagemappingitem)
  - [BusMonitoringMappingItem](MappingApi.md#busmonitoringmappingitem)
  - [BusSignalGroupMappingItem](MappingApi.md#bussignalgroupmappingitem)
  - [BusSignalMappingItem](MappingApi.md#bussignalmappingitem)
  - [PortMappingItem](MappingApi.md#portmappingitem)
  - [DebugMappingItem](MappingApi.md#debugmappingitem)
  - [DebugRegisterMappingItem](MappingApi.md#debugregistermappingitem)
  - [DiagDidMappingItem](MappingApi.md#diagdidmappingitem)
  - [CallableMappingItem](MappingApi.md#callablemappingitem)
  - [DiagRoutineMappingItem](MappingApi.md#diagroutinemappingitem)
  - [DiagServiceMappingItem](MappingApi.md#diagservicemappingitem)
  - [ServiceMappingItem](MappingApi.md#servicemappingitem)
  - [DiagFaultMemoryMappingItem](MappingApi.md#diagfaultmemorymappingitem)
  - [EdiabasVariableMappingItem](MappingApi.md#ediabasvariablemappingitem)
  - [EnvSimMappingItem](MappingApi.md#envsimmappingitem)
  - [EesPinVariableMappingItem](MappingApi.md#eespinvariablemappingitem)
  - [LogFilterMessageMappingItem](MappingApi.md#logfiltermessagemappingitem)
  - [LoggingArgumentMappingItem](MappingApi.md#loggingargumentmappingitem)
  - [CalibrationMappingItem](MappingApi.md#calibrationmappingitem)
  - [MeasureMappingItem](MappingApi.md#measuremappingitem)
  - [RunningValueMappingItem](MappingApi.md#runningvaluemappingitem)
  - [ModelMappingItem](MappingApi.md#modelmappingitem)
  - [AudioChannelMappingItem](MappingApi.md#audiochannelmappingitem)
  - [AudioDeviceMappingItem](MappingApi.md#audiodevicemappingitem)
  - [GenericAudioMappingItem](MappingApi.md#genericaudiomappingitem)
  - [GenericImageMappingItem](MappingApi.md#genericimagemappingitem)
  - [ImageMappingItem](MappingApi.md#imagemappingitem)
  - [ServiceEventLeafMappingItem](MappingApi.md#serviceeventleafmappingitem)
  - [ServiceMethodReturnMappingItem](MappingApi.md#servicemethodreturnmappingitem)
  - [ServiceMethodParameterMappingItem](MappingApi.md#servicemethodparametermappingitem)
- [API for Migrations](MigrationApi.md)
  - [MigrationApi](MigrationApi.md#migrationapi)
- [API for Multimedia Objects](MultimediaApi.md)
  - [MultimediaApi](MultimediaApi.md#multimediaapi)
  - [Mask](MultimediaApi.md#mask)
- [API for Packages](PackageApi.md)
  - [PackageApi](PackageApi.md#packageapi)
  - [AnalysisPackage](PackageApi.md#analysispackage)
  - [LocalMapping](PackageApi.md#localmapping)
  - [VariableRecordingGroup](PackageApi.md#variablerecordinggroup)
  - [AutoAssignSignalGroup](PackageApi.md#autoassignsignalgroup)
  - [AutoAssignRecordingGroup](PackageApi.md#autoassignrecordinggroup)
  - [Package](PackageApi.md#package)
  - [RecordingConfig](PackageApi.md#recordingconfig)
- [API for Parameters](ParameterApi.md)
  - [ParameterApi](ParameterApi.md#parameterapi)
  - [GlobalConstantsDefinition](ParameterApi.md#globalconstantsdefinition)
  - [PackageParametersDefinition](ParameterApi.md#packageparametersdefinition)
- [API for Projects](ProjectApi.md)
  - [ProjectApi](ProjectApi.md#projectapi)
  - [Project](ProjectApi.md#project)
  - [Attributes](ProjectApi.md#attributes)
  - [ParameterSet](ProjectApi.md#parameterset)
  - [ParameterSetRecordings](ProjectApi.md#parametersetrecordings)
- [API for Relations](RelationApi.md)
  - [RelationApi](RelationApi.md#relationapi)
  - [Relation](RelationApi.md#relation)
- [API for Reports](ReportApi.md)
  - [ReportApi](ReportApi.md#reportapi)
  - [Report](ReportApi.md#report)
  - [Artifact](ReportApi.md#artifact)
  - [ReportProject](ReportApi.md#reportproject)
  - [ReportProjectElement](ReportApi.md#reportprojectelement)
  - [ReportPackage](ReportApi.md#reportpackage)
  - [GlobalConstant](ReportApi.md#globalconstant)
  - [ReportRecording](ReportApi.md#reportrecording)
  - [RevaluationComment](ReportApi.md#revaluationcomment)
  - [ReportTestCase](ReportApi.md#reporttestcase)
  - [ReportTestStep](ReportApi.md#reportteststep)
  - [Entity](ReportApi.md#entity)
  - [ImageEntity](ReportApi.md#imageentity)
  - [ReportImage](ReportApi.md#reportimage)
  - [ImageExpectationEntity](ReportApi.md#imageexpectationentity)
  - [TableEntity](ReportApi.md#tableentity)
  - [TextEntity](ReportApi.md#textentity)
  - [ReportAnalysisJob](ReportApi.md#reportanalysisjob)
  - [ReportAnalysisEpisode](ReportApi.md#reportanalysisepisode)
  - [ReportAnalysisStep](ReportApi.md#reportanalysisstep)
  - [ReportRecordingInfo](ReportApi.md#reportrecordinginfo)
  - [ReportParameterSet](ReportApi.md#reportparameterset)
  - [ReportParameterizedPackage](ReportApi.md#reportparameterizedpackage)
  - [ReportConfigurationChange](ReportApi.md#reportconfigurationchange)
  - [ReportFolderElement](ReportApi.md#reportfolderelement)
- [API for Report Filters](ReportFilterApi.md)
  - [ReportFilterApi](ReportFilterApi.md#reportfilterapi)
  - [FilterElement](ReportFilterApi.md#filterelement)
  - [FilterGroupConjunction](ReportFilterApi.md#filtergroupconjunction)
  - [FilterGroupDisjunction](ReportFilterApi.md#filtergroupdisjunction)
  - [FilterGroupElement](ReportFilterApi.md#filtergroupelement)
- [API for Settings](SettingsApi.md)
  - [SettingsApi](SettingsApi.md#settingsapi)
- [API for Signals](SignalApi.md)
  - [SignalApi](SignalApi.md#signalapi)
  - [ConstantSegment](SignalApi.md#constantsegment)
  - [SymbolType](SignalApi.md#symboltype)
  - [DataFileSegment](SignalApi.md#datafilesegment)
  - [ExponentialSegment](SignalApi.md#exponentialsegment)
  - [IdleSegment](SignalApi.md#signalapi-idlesegment)
  - [LoopSegment](SignalApi.md#loopsegment)
  - [SignalSegment](SignalApi.md#signalsegment)
  - [RampSegment](SignalApi.md#rampsegment)
  - [RampSlopeSegment](SignalApi.md#rampslopesegment)
  - [NoiseSegment](SignalApi.md#noisesegment)
  - [SineSegment](SignalApi.md#sinesegment)
  - [SawSegment](SignalApi.md#sawsegment)
  - [PulseSegment](SignalApi.md#pulsesegment)
  - [OperationSegment](SignalApi.md#operationsegment)
  - [SignalValueSegment](SignalApi.md#signalvaluesegment)
  - [OperationSignalDescription](SignalApi.md#operationsignaldescription)
  - [SignalDescription](SignalApi.md#signaldescription)
  - [SegmentSignalDescription](SignalApi.md#segmentsignaldescription)
- [API for Signal Descriptions](SignalDescriptionApi.md)
  - [SignalDescriptionApi](SignalDescriptionApi.md#signaldescriptionapi)
  - [SignalDescriptionFile](SignalDescriptionApi.md#signaldescriptionfile)
- [API for Signal Recordings](SignalRecordingApi.md)
  - [SignalRecordingApi](SignalRecordingApi.md#signalrecordingapi)
  - [RecordingGroup](SignalRecordingApi.md#recordinggroup)
  - [RecordingInfo](SignalRecordingApi.md#recordinginfo)
  - [SignalGroupBase](SignalRecordingApi.md#signalgroupbase)
  - [SignalGroup](SignalRecordingApi.md#signalgroup)
- [API for Symbols](SymbolApi.md)
  - [SymbolApi](SymbolApi.md#symbolapi)
  - [ConstSymbol](SymbolApi.md#constsymbol)
  - [SignalSymbol](SymbolApi.md#signalsymbol)
  - [StringSymbol](SymbolApi.md#stringsymbol)
- [API for Test Steps](TestStepApi.md)
  - [TestStepApi](TestStepApi.md#teststepapi)
  - [TsAddTrace](TestStepApi.md#tsaddtrace)
  - [TestStep](TestStepApi.md#teststep)
  - [TsJob](TestStepApi.md#tsjob)
  - [TsRead](TestStepApi.md#tsread)
  - [TsBusFirstSignalCheck](TestStepApi.md#tsbusfirstsignalcheck)
  - [TestStepRWBase](TestStepApi.md#teststeprwbase)
  - [TsWrite](TestStepApi.md#tswrite)
  - [TsReadAudio](TestStepApi.md#tsreadaudio)
  - [TsWriteAudio](TestStepApi.md#tswriteaudio)
  - [TsReadImage](TestStepApi.md#tsreadimage)
  - [ImageFilter](TestStepApi.md#imagefilter)
  - [TsStimulate](TestStepApi.md#tsstimulate)
  - [MappingTestStep](TestStepApi.md#mappingteststep)
  - [MappingTestStepContainer](TestStepApi.md#mappingteststepcontainer)
  - [TsReadBusSignalGroup](TestStepApi.md#tsreadbussignalgroup)
  - [TsSignalGroupOperation](TestStepApi.md#tssignalgroupoperation)
  - [TsWriteBusSignalGroup](TestStepApi.md#tswritebussignalgroup)
  - [TsWriteBusSignalGroupCyclic](TestStepApi.md#tswritebussignalgroupcyclic)
  - [TsRestore](TestStepApi.md#tsrestore)
  - [TsBusFirstSignalReset](TestStepApi.md#tsbusfirstsignalreset)
  - [TsResetPDUTiming](TestStepApi.md#tsresetpdutiming)
  - [TsBusMonitoringAliveCounter](TestStepApi.md#tsbusmonitoringalivecounter)
  - [TsBusMonitoring](TestStepApi.md#tsbusmonitoring)
  - [TsBusMonitoringChecksum](TestStepApi.md#tsbusmonitoringchecksum)
  - [TsBusMonitoringDlc](TestStepApi.md#tsbusmonitoringdlc)
  - [TsBusMonitoringFrameTiming](TestStepApi.md#tsbusmonitoringframetiming)
  - [TsAlterPDUTiming](TestStepApi.md#tsalterpdutiming)
  - [TsClearFrameAndSignalBuffers](TestStepApi.md#tsclearframeandsignalbuffers)
  - [TsEdiabas](TestStepApi.md#tsediabas)
  - [EdiabasResult](TestStepApi.md#ediabasresult)
  - [EdiabasArgument](TestStepApi.md#ediabasargument)
  - [TsReadFaultMemory](TestStepApi.md#tsreadfaultmemory)
  - [TsTouchInput](TestStepApi.md#tstouchinput)
  - [TouchInputAction](TestStepApi.md#touchinputaction)
  - [TestStepContainer](TestStepApi.md#teststepcontainer)
  - [TsIfDef](TestStepApi.md#tsifdef)
  - [TsIfThenElse](TestStepApi.md#tsifthenelse)
  - [Node](TestStepApi.md#node)
  - [TsLoop](TestStepApi.md#tsloop)
  - [TsReactOn](TestStepApi.md#tsreacton)
  - [TsReactOnNode](TestStepApi.md#tsreactonnode)
  - [TsSwitchCase](TestStepApi.md#tsswitchcase)
  - [TsCaseNode](TestStepApi.md#tscasenode)
  - [TsSwitchBase](TestStepApi.md#tsswitchbase)
  - [TsSwitchDefCase](TestStepApi.md#tsswitchdefcase)
  - [TsCaseDefNode](TestStepApi.md#tscasedefnode)
  - [TsCaseNodeBase](TestStepApi.md#tscasenodebase)
  - [TsEesErrorSet](TestStepApi.md#tseeserrorset)
  - [TsEdiabasLockBlock](TestStepApi.md#tsediabaslockblock)
  - [TsAssertion](TestStepApi.md#tsassertion)
  - [TsMultiCheck](TestStepApi.md#tsmulticheck)
  - [TsBlock](TestStepApi.md#tsblock)
  - [TsBlockBase](TestStepApi.md#tsblockbase)
  - [TsPostconditionBlock](TestStepApi.md#tspostconditionblock)
  - [TsPreconditionBlock](TestStepApi.md#tspreconditionblock)
  - [TsInfoBlock](TestStepApi.md#tsinfoblock)
  - [Testcase](TestStepApi.md#testcase)
  - [TsPackageCall](TestStepApi.md#tspackagecall)
  - [TsParallelPackageCall](TestStepApi.md#tsparallelpackagecall)
  - [TsParallelRttPackageCall](TestStepApi.md#tsparallelrttpackagecall)
  - [TsRttPackageCall](TestStepApi.md#tsrttpackagecall)
  - [TsPackage](TestStepApi.md#tspackage)
  - [TsParallelPackage](TestStepApi.md#tsparallelpackage)
  - [TsParallelRttPackage](TestStepApi.md#tsparallelrttpackage)
  - [TsRttPackage](TestStepApi.md#tsrttpackage)
  - [TsCheckSimulationStatus](TestStepApi.md#tschecksimulationstatus)
  - [TsBreak](TestStepApi.md#tsbreak)
  - [TsContinue](TestStepApi.md#tscontinue)
  - [TsExit](TestStepApi.md#tsexit)
  - [TsReturn](TestStepApi.md#tsreturn)
  - [TsWait](TestStepApi.md#tswait)
  - [TsWaitForUser](TestStepApi.md#tswaitforuser)
  - [TsBitExtract](TestStepApi.md#tsbitextract)
  - [TsCalculation](TestStepApi.md#tscalculation)
  - [TsInboxFetch](TestStepApi.md#tsinboxfetch)
  - [TsOutboxPost](TestStepApi.md#tsoutboxpost)
  - [TsEesError](TestStepApi.md#tseeserror)
  - [TsSimulate](TestStepApi.md#tssimulate)
  - [TsLogFile](TestStepApi.md#tslogfile)
  - [TsReport](TestStepApi.md#tsreport)
  - [TsComment](TestStepApi.md#tscomment)
  - [TsTodo](TestStepApi.md#tstodo)
  - [TsStartTrace](TestStepApi.md#tsstarttrace)
  - [TsStopTrace](TestStepApi.md#tsstoptrace)
  - [TsSetTraceComment](TestStepApi.md#tssettracecomment)
  - [TsRequestAnalysis](TestStepApi.md#tsrequestanalysis)
  - [TsAnalysisJob](TestStepApi.md#tsanalysisjob)
  - [TsTraceStepResult](TestStepApi.md#tstracestepresult)
  - [TsSelectList](TestStepApi.md#tsselectlist)
  - [TsUserInterface](TestStepApi.md#tsuserinterface)
  - [TsImageDialog](TestStepApi.md#tsimagedialog)
  - [TsMessageDialog](TestStepApi.md#tsmessagedialog)
  - [TsInputDialog](TestStepApi.md#tsinputdialog)
  - [TsLoadEnvironment](TestStepApi.md#tsloadenvironment)
  - [TsStartSimulation](TestStepApi.md#tsstartsimulation)
  - [TsStopSimulation](TestStepApi.md#tsstopsimulation)
  - [TsStartStimulus](TestStepApi.md#tsstartstimulus)
  - [TsStopStimulus](TestStepApi.md#tsstopstimulus)
  - [TsKeyword](TestStepApi.md#tskeyword)
  - [TsKeywordArgument](TestStepApi.md#tskeywordargument)
  - [TsKeywordReturn](TestStepApi.md#tskeywordreturn)
  - [TsAXSCall](TestStepApi.md#tsaxscall)
  - [Argument](TestStepApi.md#argument)
  - [Return](TestStepApi.md#return)
  - [TsCANoeTestModuleRunner](TestStepApi.md#tscanoetestmodulerunner)
  - [TsCall](TestStepApi.md#tscall)
  - [TsCallDiagService](TestStepApi.md#tscalldiagservice)
  - [TsCallRead](TestStepApi.md#tscallread)
  - [TsCallWrite](TestStepApi.md#tscallwrite)
  - [TsCallIOControl](TestStepApi.md#tscalliocontrol)
  - [TsCallIOControlReturnControlToEcu](TestStepApi.md#tscalliocontrolreturncontroltoecu)
  - [TsCallIOControlResetToDefault](TestStepApi.md#tscalliocontrolresettodefault)
  - [TsCallIOControlFreezeCurrentState](TestStepApi.md#tscalliocontrolfreezecurrentstate)
  - [TsCallIOControlShortTermAdjustment](TestStepApi.md#tscalliocontrolshorttermadjustment)
  - [TsCallIOControlISOSAEReserved](TestStepApi.md#tscalliocontrolisosaereserved)
  - [TsCallKwpIOControlReturnControlToEcu](TestStepApi.md#tscallkwpiocontrolreturncontroltoecu)
  - [TsCallKwpIOControlReportCurrentState](TestStepApi.md#tscallkwpiocontrolreportcurrentstate)
  - [TsCallKwpIOControlResetToDefault](TestStepApi.md#tscallkwpiocontrolresettodefault)
  - [TsCallKwpIOControlFreeze](TestStepApi.md#tscallkwpiocontrolfreeze)
  - [TsCallKwpIOControlShortTermAdjustment](TestStepApi.md#tscallkwpiocontrolshorttermadjustment)
  - [TsCallKwpIOControlLongTermAdjustment](TestStepApi.md#tscallkwpiocontrollongtermadjustment)
- [API for Touch Inputs](TouchInputApi.md)
  - [TouchInputApi](TouchInputApi.md#touchinputapi)
  - [Hold](TouchInputApi.md#hold)
  - [HoldAndSwipe](TouchInputApi.md#holdandswipe)
  - [MultiSwipe](TouchInputApi.md#multiswipe)
  - [MultiTap](TouchInputApi.md#multitap)
  - [Pinch](TouchInputApi.md#pinch)
  - [Rotate](TouchInputApi.md#rotate)
  - [Swipe](TouchInputApi.md#swipe)
  - [Tap](TouchInputApi.md#tap)
- [API for Trace Analyses](TraceAnalysisApi.md)
  - [TraceAnalysisApi](TraceAnalysisApi.md#traceanalysisapi)
  - [Assertion](TraceAnalysisApi.md#assertion)
  - [TraceStep](TraceAnalysisApi.md#tracestep)
  - [AnalysisBlock](TraceAnalysisApi.md#analysisblock)
  - [TraceStepContainer](TraceAnalysisApi.md#tracestepcontainer)
  - [Calculation](TraceAnalysisApi.md#calculation)
  - [ExpectationModeOptions](TraceAnalysisApi.md#expectationmodeoptions)
  - [ReportConfig](TraceAnalysisApi.md#reportconfig)
  - [TemplateBasedTraceStep](TraceAnalysisApi.md#templatebasedtracestep)
  - [SignalBinding](TraceAnalysisApi.md#signalbinding)
  - [GenericSignal](TraceAnalysisApi.md#genericsignal)
  - [RecordingGroupBase](TraceAnalysisApi.md#recordinggroupbase)
  - [Episode](TraceAnalysisApi.md#episode)
  - [SignalRecording](TraceAnalysisApi.md#signalrecording)
  - [IfDef](TraceAnalysisApi.md#ifdef)
  - [IfThenElse](TraceAnalysisApi.md#ifthenelse)
  - [ElseNode](TraceAnalysisApi.md#elsenode)
  - [ThenNode](TraceAnalysisApi.md#thennode)
  - [TraceAnalysis](TraceAnalysisApi.md#traceanalysis)
  - [SyncConfig](TraceAnalysisApi.md#syncconfig)
  - [AutosarTimeSynchronization](TraceAnalysisApi.md#autosartimesynchronization)
  - [AutosarTimeSyncRecordingGroupInfo](TraceAnalysisApi.md#autosartimesyncrecordinggroupinfo)
  - [CrossCorrelationSynchronization](TraceAnalysisApi.md#crosscorrelationsynchronization)
  - [EqualnessMatchingSynchronization](TraceAnalysisApi.md#equalnessmatchingsynchronization)
  - [EqualEntry](TraceAnalysisApi.md#equalentry)
  - [ExpectationSynchronization](TraceAnalysisApi.md#expectationsynchronization)
  - [SyncExpectation](TraceAnalysisApi.md#syncexpectation)
  - [LeastSquaresSynchronization](TraceAnalysisApi.md#leastsquaressynchronization)
  - [OffsetSynchronization](TraceAnalysisApi.md#offsetsynchronization)
  - [UtcTimestampSynchronization](TraceAnalysisApi.md#utctimestampsynchronization)
  - [Synchronization](TraceAnalysisApi.md#synchronization)
  - [SwitchDefCase](TraceAnalysisApi.md#switchdefcase)
  - [CaseDefNode](TraceAnalysisApi.md#casedefnode)
  - [TriggerBlock](TraceAnalysisApi.md#triggerblock)
  - [Plot](TraceAnalysisApi.md#plot)
  - [PlotSubConfig](TraceAnalysisApi.md#plotsubconfig)
  - [PlotSignalBase](TraceAnalysisApi.md#plotsignalbase)
  - [PlotCalculatedSignal](TraceAnalysisApi.md#plotcalculatedsignal)
  - [PlotSignal](TraceAnalysisApi.md#plotsignal)
  - [PlotSubPlot](TraceAnalysisApi.md#plotsubplot)
  - [PlotAxis](TraceAnalysisApi.md#plotaxis)
  - [TraceAnalysisReferenceDeprecated](TraceAnalysisApi.md#traceanalysisreferencedeprecated)
  - [TraceAnalysisReference](TraceAnalysisApi.md#traceanalysisreference)
  - [PackageBase](TraceAnalysisApi.md#packagebase)
- [API for Trace Files](TraceFileApi.md)
  - [TraceFileApi](TraceFileApi.md#tracefileapi)
  - [TraceFile](TraceFileApi.md#tracefile)
  - [Device](TraceFileApi.md#device)
- [API for Trace Step Templates](TraceStepTemplateApi.md)
  - [TraceStepTemplateApi](TraceStepTemplateApi.md#tracesteptemplateapi)
  - [TraceStepTemplate](TraceStepTemplateApi.md#tracesteptemplate)
  - [TraceStepTemplatePythonEvent](TraceStepTemplateApi.md#tracesteptemplatepythonevent)
  - [PythonEventFunction](TraceStepTemplateApi.md#pythoneventfunction)
- [API for Variables](VariableApi.md)
  - [VariableApi](VariableApi.md#variableapi)
  - [BooleanVariable](VariableApi.md#booleanvariable)
  - [DynamicEnumVariable](VariableApi.md#dynamicenumvariable)
  - [DynamicTextTableVariable](VariableApi.md#dynamictexttablevariable)
  - [EnumVariable](VariableApi.md#enumvariable)
  - [EnumVariableElement](VariableApi.md#enumvariableelement)
  - [FunctionVariable](VariableApi.md#functionvariable)
  - [NumericVariable](VariableApi.md#numericvariable)
  - [PyObjectVariable](VariableApi.md#pyobjectvariable)
  - [StaticTextTableVariable](VariableApi.md#statictexttablevariable)
  - [StringVariable](VariableApi.md#stringvariable)
  - [StructureVariable](VariableApi.md#structurevariable)
  - [Variable](VariableApi.md#variable)
  - [VectorVariable](VariableApi.md#vectorvariable)
- [API for Workspaces](WorkspaceApi.md)
  - [WorkspaceApi](WorkspaceApi.md#workspaceapi)
