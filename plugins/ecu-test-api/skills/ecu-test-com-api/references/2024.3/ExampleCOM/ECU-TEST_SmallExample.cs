using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Reflection;

namespace ConsoleApplication1
{
    class Program
    {
        static void Main(string[] args)
        {
            // Die Programm-ID muss entsprechend der installierten Applikation angepasst werden
            // Siehe Api-Dokumentation unter <Programm.-Verz>\Help\APIDoc\COM-API
            Type ecuTestType = Type.GetTypeFromProgID("ECU-TEST.Application");  // COM-Applikation starten
            if (ecuTestType == null)
            {
                return;
            }
            Object ecuTest = Activator.CreateInstance(ecuTestType);
            Object[] parameters = new Object[1];
            parameters[0] = "E:\\Daten\\Packages\\5wait.pkg";
            ecuTest.GetType().InvokeMember("OpenPackage", BindingFlags.InvokeMethod,
                null, ecuTest, parameters);
        }
    }
}
