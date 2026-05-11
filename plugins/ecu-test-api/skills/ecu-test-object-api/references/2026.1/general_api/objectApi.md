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

[ Report API ](apireport.md)

[ Object API ](#)

Object API

[ API entry points ](#api-entry-points)

API entry points

- [ API for Analysis Jobs ](AnalysisJobApi.md)
- [ API for Artifacts ](ArtifactApi.md)
- [ API for Project Components ](ComponentApi.md)
- [ API for Configurations ](ConfigurationApi.md)
- [ API for Expectations ](ExpectationApi.md)
- [ API for Expressions ](ExpressionApi.md)
- [ API for Global Mappings ](GlobalMappingApi.md)
- [ API for Mappings ](MappingApi.md)
- [ API for Multimedia Objects ](MultimediaApi.md)
- [ API for Packages ](PackageApi.md)
- [ API for Parameters ](ParameterApi.md)
- [ API for Projects ](ProjectApi.md)
- [ API for Relations ](RelationApi.md)
- [ API for Reports ](ReportApi.md)
- [ API for Report Filters ](ReportFilterApi.md)
- [ API for Settings ](SettingsApi.md)
- [ API for Signals ](SignalApi.md)
- [ API for Signal Descriptions ](SignalDescriptionApi.md)
- [ API for Signal Recordings ](SignalRecordingApi.md)
- [ API for Symbols ](SymbolApi.md)
- [ API for Test Steps ](TestStepApi.md)
- [ API for Touch Inputs ](TouchInputApi.md)
- [ API for Trace Analyses ](TraceAnalysisApi.md)
- [ API for Trace Files ](TraceFileApi.md)
- [ API for Trace Step Templates ](TraceStepTemplateApi.md)
- [ API for Variables ](VariableApi.md)
- [ API for Workspaces ](WorkspaceApi.md)

Object API [ Object API ](#)

Object API

- [ Java-Client ](#java-client)
- [ DotNet-Client ](#dotnet-client)
- [ API entry points ](#api-entry-points)
  - [C ApiClient ](#ApiClient.ApiClient)
    - [A AnalysisJobApi ](#ApiClient.ApiClient.AnalysisJobApi)
    - [A ArtifactApi ](#ApiClient.ApiClient.ArtifactApi)
    - [A ConfigurationApi ](#ApiClient.ApiClient.ConfigurationApi)
    - [A GlobalMappingApi ](#ApiClient.ApiClient.GlobalMappingApi)
    - [A MultimediaApi ](#ApiClient.ApiClient.MultimediaApi)
    - [A PackageApi ](#ApiClient.ApiClient.PackageApi)
    - [A ParameterApi ](#ApiClient.ApiClient.ParameterApi)
    - [A ProjectApi ](#ApiClient.ApiClient.ProjectApi)
    - [A RelationApi ](#ApiClient.ApiClient.RelationApi)
    - [A ReportApi ](#ApiClient.ApiClient.ReportApi)
    - [A SignalDescriptionApi ](#ApiClient.ApiClient.SignalDescriptionApi)
    - [A TraceFileApi ](#ApiClient.ApiClient.TraceFileApi)
    - [A TraceStepTemplateApi ](#ApiClient.ApiClient.TraceStepTemplateApi)
    - [A WorkspaceApi ](#ApiClient.ApiClient.WorkspaceApi)
    - [M GetApplicationVersion ](#ApiClient.ApiClient.GetApplicationVersion)
    - [M GetClientVersion ](#ApiClient.ApiClient.GetClientVersion)
  - [ API for Analysis Jobs ](AnalysisJobApi.md)
  - [ API for Artifacts ](ArtifactApi.md)
  - [ API for Project Components ](ComponentApi.md)
  - [ API for Configurations ](ConfigurationApi.md)
  - [ API for Expectations ](ExpectationApi.md)
  - [ API for Expressions ](ExpressionApi.md)
  - [ API for Global Mappings ](GlobalMappingApi.md)
  - [ API for Mappings ](MappingApi.md)
  - [ API for Multimedia Objects ](MultimediaApi.md)
  - [ API for Packages ](PackageApi.md)
  - [ API for Parameters ](ParameterApi.md)
  - [ API for Projects ](ProjectApi.md)
  - [ API for Relations ](RelationApi.md)
  - [ API for Reports ](ReportApi.md)
  - [ API for Report Filters ](ReportFilterApi.md)
  - [ API for Settings ](SettingsApi.md)
  - [ API for Signals ](SignalApi.md)
  - [ API for Signal Descriptions ](SignalDescriptionApi.md)
  - [ API for Signal Recordings ](SignalRecordingApi.md)
  - [ API for Symbols ](SymbolApi.md)
  - [ API for Test Steps ](TestStepApi.md)
  - [ API for Touch Inputs ](TouchInputApi.md)
  - [ API for Trace Analyses ](TraceAnalysisApi.md)
  - [ API for Trace Files ](TraceFileApi.md)
  - [ API for Trace Step Templates ](TraceStepTemplateApi.md)
  - [ API for Variables ](VariableApi.md)
  - [ API for Workspaces ](WorkspaceApi.md)

[ Trace Analysis API ](../TraceAnalysisAPI/index.md)

[ Generator APIs ](../generators/index.md)

[ Tools ](../tools/index.md)

[ User test management ](../userTestmanagement/index.md)

[ UserUtility API ](../user-utility/user-utility.md)

[ Utility Examples ](../user-utility/example-utilities.md)

Object API

- [ Java-Client ](#java-client)
- [ DotNet-Client ](#dotnet-client)
- [ API entry points ](#api-entry-points)
  - [C ApiClient ](#ApiClient.ApiClient)
    - [A AnalysisJobApi ](#ApiClient.ApiClient.AnalysisJobApi)
    - [A ArtifactApi ](#ApiClient.ApiClient.ArtifactApi)
    - [A ConfigurationApi ](#ApiClient.ApiClient.ConfigurationApi)
    - [A GlobalMappingApi ](#ApiClient.ApiClient.GlobalMappingApi)
    - [A MultimediaApi ](#ApiClient.ApiClient.MultimediaApi)
    - [A PackageApi ](#ApiClient.ApiClient.PackageApi)
    - [A ParameterApi ](#ApiClient.ApiClient.ParameterApi)
    - [A ProjectApi ](#ApiClient.ApiClient.ProjectApi)
    - [A RelationApi ](#ApiClient.ApiClient.RelationApi)
    - [A ReportApi ](#ApiClient.ApiClient.ReportApi)
    - [A SignalDescriptionApi ](#ApiClient.ApiClient.SignalDescriptionApi)
    - [A TraceFileApi ](#ApiClient.ApiClient.TraceFileApi)
    - [A TraceStepTemplateApi ](#ApiClient.ApiClient.TraceStepTemplateApi)
    - [A WorkspaceApi ](#ApiClient.ApiClient.WorkspaceApi)
    - [M GetApplicationVersion ](#ApiClient.ApiClient.GetApplicationVersion)
    - [M GetClientVersion ](#ApiClient.ApiClient.GetClientVersion)

# Object based program API[¶](#object-based-program-api "Link to this heading")

The object based program API is designed to read, create or modify ecu.test relevant files. With it you can create your own scripts in a Python development environment of your choice. The design follows an object oriented approach. To execute your script, a started ecu.test is needed.

To use it from an external Python, please extend your `PYTHONPATH` to include *`<path to program>`*`\Templates\ApiClient` in order to be able to import it as shown in the example below. The ApiClient is Python 2 and Python 3 compatible. To use the Object API from within ecu.test use `api.ObjectApi`

Info

The Object API is for dealing with ecu.test relevant files only, e.g. Packages, Projects, TBC or TCF. If you want to execute test cases, you need to use the [REST API](rest-api.md#rest-api) or the [COM API](com-api.md#com-api).

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
                if (!System.IO.File.Exists(tcfFile))
                {
                    Console.WriteLine($"File path '{tcfFile}' does not exists! Abort.");
                    return;
                }

                ApiClient api = new ApiClient();
                TestConfiguration tcf = api.ConfigurationApi.OpenTestConfiguration(tcfFile);
                Model model = tcf.Platform.ModelAccess.Get("Plant model");
                model.SetFile("NewModelFile.mdl");
                tcf.Save(tcfFile);
            }

            public static void TestPackage()
            {
                string packageFile = "C:\\Data\\ECU-TEST\\Packages\\Testpackage.pkg";

                if (!System.IO.File.Exists(packageFile))
                {
                    Console.WriteLine($"File path '{packageFile}' does not exists! Abort.");
                    return;
                }

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

## API entry points[¶](#api-entry-points "Link to this heading")

Part of the [Object based program API](#objectapi).

*class* ApiClient[¶](#ApiClient.ApiClient "Link to this definition")  
Entry point for object based api.

AnalysisJobApi[¶](#ApiClient.ApiClient.AnalysisJobApi "Link to this definition")  
Returns the AnalysisJobApi namespace

Returns:  AnalysisJobApi namespace

Return type:  [`AnalysisJobApi`](AnalysisJobApi.md#ApiClient.AnalysisJobApi "ApiClient.AnalysisJobApi (Python class) — ApiClient.AnalysisJobApi")

ArtifactApi[¶](#ApiClient.ApiClient.ArtifactApi "Link to this definition")  
Returns the ArtifactApi namespace.

Returns:  ArtifactApi namespace

Return type:  [`ArtifactApi`](ArtifactApi.md#ApiClient.ArtifactApi "ApiClient.ArtifactApi (Python class) — ApiClient.ArtifactApi")

ConfigurationApi[¶](#ApiClient.ApiClient.ConfigurationApi "Link to this definition")  
Returns the ConfigurationApi namespace.

Returns:  ConfigurationApi namespace

Return type:  [`ConfigurationApi`](ConfigurationApi.md#ApiClient.ConfigurationApi "ApiClient.ConfigurationApi (Python class) — API to access configuration files")

GlobalMappingApi[¶](#ApiClient.ApiClient.GlobalMappingApi "Link to this definition")  
Returns the GlobalMappingApi namespace.

Returns:  GlobalMappingApi namespace

Return type:  [`GlobalMappingApi`](GlobalMappingApi.md#ApiClient.GlobalMappingApi "ApiClient.GlobalMappingApi (Python class) — API to access global mapping files")

MultimediaApi[¶](#ApiClient.ApiClient.MultimediaApi "Link to this definition")  
Returns the MultimediaApi namespace.

Returns:  MultimediaApi namespace

Return type:  [`MultimediaApi`](MultimediaApi.md#ApiClient.MultimediaApi "ApiClient.MultimediaApi (Python class) — ApiClient.MultimediaApi")

PackageApi[¶](#ApiClient.ApiClient.PackageApi "Link to this definition")  
Returns the PackageApi namespace.

Returns:  PackageApi namespace

Return type:  [`PackageApi`](PackageApi.md#ApiClient.PackageApi "ApiClient.PackageApi (Python class) — API to access Packages")

ParameterApi[¶](#ApiClient.ApiClient.ParameterApi "Link to this definition")  
Returns the ParameterApi namespace.

Returns:  ParameterApi namespace

Return type:  [`ParameterApi`](ParameterApi.md#ApiClient.ParameterApi "ApiClient.ParameterApi (Python class) — API to access parameter files")

ProjectApi[¶](#ApiClient.ApiClient.ProjectApi "Link to this definition")  
Returns the ProjectApi namespace.

Returns:  ProjectApi namespace

Return type:  [`ProjectApi`](ProjectApi.md#ApiClient.ProjectApi "ApiClient.ProjectApi (Python class) — API to access projects")

RelationApi[¶](#ApiClient.ApiClient.RelationApi "Link to this definition")  
Returns the RelationApi namespace.

Returns:  RelationApi namespace

Return type:  [`RelationApi`](RelationApi.md#ApiClient.RelationApi "ApiClient.RelationApi (Python class) — API to access relations")

ReportApi[¶](#ApiClient.ApiClient.ReportApi "Link to this definition")  
Returns the ReportApi namespace.

Returns:  ReportApi namespace

Return type:  [`ReportApi`](ReportApi.md#ApiClient.ReportApi "ApiClient.ReportApi (Python class) — API to access test reports")

SignalDescriptionApi[¶](#ApiClient.ApiClient.SignalDescriptionApi "Link to this definition")  
Returns the SignalDescriptionApi namespace.

Returns:  SignalDescriptionApi namespace

Return type:  [`SignalDescriptionApi`](SignalDescriptionApi.md#ApiClient.SignalDescriptionApi "ApiClient.SignalDescriptionApi (Python class) — API to access signal description files")

TraceFileApi[¶](#ApiClient.ApiClient.TraceFileApi "Link to this definition")  
Returns the TraceFileApi namespace.

Returns:  TraceFileApi namespace

Return type:  [`TraceFileApi`](TraceFileApi.md#ApiClient.TraceFileApi "ApiClient.TraceFileApi (Python class) — API to access trace files")

TraceStepTemplateApi[¶](#ApiClient.ApiClient.TraceStepTemplateApi "Link to this definition")  
Returns the TraceStepTemplateApi namespace.

Returns:  TraceStepTemplateApi namespace

Return type:  [`TraceStepTemplateApi`](TraceStepTemplateApi.md#ApiClient.TraceStepTemplateApi "ApiClient.TraceStepTemplateApi (Python class) — API to access trace step template files")

WorkspaceApi[¶](#ApiClient.ApiClient.WorkspaceApi "Link to this definition")  
Returns the WorkspaceApi namespace.

Returns:  WorkspaceApi namespace

Return type:  [`WorkspaceApi`](WorkspaceApi.md#ApiClient.WorkspaceApi "ApiClient.WorkspaceApi (Python class) — API to access the workspace")

GetApplicationVersion()[¶](#ApiClient.ApiClient.GetApplicationVersion "Link to this definition")  
Returns the version of ecu.test in format ‘year.release.servicepack’.

Returns:  ecu.test version

Return type:  str

GetClientVersion()[¶](#ApiClient.ApiClient.GetClientVersion "Link to this definition")  
Returns the version of the object based api client.

Returns:  client version

Return type:  str

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
