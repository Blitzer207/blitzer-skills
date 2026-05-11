using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Reflection;

namespace ConsoleApplication1
{
    class Program
    {
        static void Main(string[] args)
        {
            // Zugriff auf ECU-TEST-API
            Type ECUTEST_COM_API = Type.GetTypeFromProgID("ECU-TEST.Application.6.5");  // Explizite Versionsangabe (hier 6.5) ist möglich, aber optional
            object ECUTEST_Application = Activator.CreateInstance(ECUTEST_COM_API);

            object[] methodArgs = new object[1];

            // ECU-TEST starten. Nicht nötig/erlaubt, wenn ECU-TEST schon läuft.
            methodArgs[0] = "C:\\Daten\\ECU-TEST";  // Workspace-Verzeichnis, optional (in der Folgezeile null angeben, dann wird der letzte Workspace verwendet)
            ECUTEST_COM_API.InvokeMember("RunApplication", BindingFlags.InvokeMethod, null, ECUTEST_Application, null);

            // Test- und Testbenchkonfiguration laden. Kann übersprungen werden, dann werden die zuletzt geladenen verwendet
            methodArgs[0] = "C:\\Daten\\ECU-TEST\\Configurations\\Tutorial-FirstPackage.tcf";
            ECUTEST_COM_API.InvokeMember("OpenTestConfiguration", BindingFlags.InvokeMethod, null, ECUTEST_Application, methodArgs);
            methodArgs[0] = "C:\\Daten\\ECU-TEST\\Configurations\\Tutorial-FirstPackage.tbc";
            ECUTEST_COM_API.InvokeMember("OpenTestbenchConfiguration", BindingFlags.InvokeMethod, null, ECUTEST_Application, methodArgs);

            // Auf Button "Start Test Engine" klicken. Erforderlich, da dabei das TestEnvironment-Objekt entsteht
            object ECUTEST_TestEnvironment = ECUTEST_COM_API.InvokeMember("Start", BindingFlags.InvokeMethod, null, ECUTEST_Application, null);

            // Ein Package laden
            String packagePath = "C:\\Daten\\ECU-TEST\\Packages\\ExamplePackages\\Tutorial-FirstPackage\\Package.pkg";
            methodArgs[0] = packagePath;
            object ECUTEST_Package = ECUTEST_COM_API.InvokeMember("OpenPackage", BindingFlags.InvokeMethod, null, ECUTEST_Application, methodArgs);

            methodArgs = new object[2];
            methodArgs[0] = packagePath;
            methodArgs[1] = true;
            object ECUTEST_TestExecutionInfo = ECUTEST_COM_API.InvokeMember("ExecutePackage", BindingFlags.InvokeMethod, null, ECUTEST_TestEnvironment, methodArgs);

            // Status prüfen
            Console.WriteLine("Ausführungsstatus: {0}", ECUTEST_COM_API.InvokeMember("GetState", BindingFlags.InvokeMethod, null, ECUTEST_TestExecutionInfo, null));

            // Auf Ende warten
            methodArgs = new object[1];
            methodArgs[0] = 5; // Timeout in Sekunden, auch null möglich für Unendlich
            ECUTEST_COM_API.InvokeMember("WaitForTestExecutionCompletion", BindingFlags.InvokeMethod, null, ECUTEST_TestExecutionInfo, methodArgs);

            // Status erneut prüfen
            Console.WriteLine("Ausführungsstatus: {0}", ECUTEST_COM_API.InvokeMember("GetState", BindingFlags.InvokeMethod, null, ECUTEST_TestExecutionInfo, null));

            // Testergebnis prüfen
            Console.WriteLine("Ergebnis: {0}", ECUTEST_COM_API.InvokeMember("GetResult", BindingFlags.InvokeMethod, null, ECUTEST_TestExecutionInfo, null));

            // Ab C# 4.0 (Visual Studio 2010, .NET Framework 4.0) ist auch dynamischer Zugriff (ohne InvokeMember) auf alle Methoden möglich:
            // Einfach dynamic statt object als Typ verwenden, dann passiert "automatisch das richtige".
            dynamic ECUTEST_Application_dynamic = Activator.CreateInstance(ECUTEST_COM_API);
            Console.WriteLine("ECU-TEST-Version: {0}", ECUTEST_Application_dynamic.GetVersion());

            // Ende erst nach Tastendruck
            Console.ReadKey();

            // Auch ECU-TEST beenden
            ECUTEST_Application_dynamic.Quit();

        }
    }
}
