[ Internal APIs ](../general_api/api.md)

[ Advanced operations of package variable types ](../general_api/variabledatastructures.md)

[ Advanced properties of bus-related objects ](../general_api/busdatastructures.md)

[ Bus related objects of trace analysis ](../general_api/busdatastructuresTraceanalysis.md)

[ Advanced properties of diagnostics-related objects ](../general_api/diagdatastructures.md)

[ Diagnostics related objects of trace analysis ](../general_api/diagdatastructuresTraceanalysis.md)

[ Advanced properties of media-related objects ](../general_api/mediadatastructures.md)

[ Advanced properties of DLT logging-related objects ](../general_api/dltdatastructures.md)

[ COM API ](../general_api/com-api.md)

[ REST API ](../general_api/rest-api.md)

[ Report API ](../general_api/apireport.md)

[ Object API ](../general_api/objectApi.md)

[ Trace Analysis API ](../TraceAnalysisAPI/index.md)

[ Generator APIs ](../generators/index.md)

[ Tools ](../tools/index.md)

[ User test management ](index.md)

User test management

Tm User API [ Tm User API ](#)

Tm User API

- [ TmUserAdapter ](#module-tts.extension.testManagementService.TmUserAdapter)
  - [C TmUserAdapter ](#tts.extension.testManagementService.TmUserAdapter.TmUserAdapter)
    - [M `\_\_init\_\_` ](#tts.extension.testManagementService.TmUserAdapter.TmUserAdapter.__init__)
    - [M GetName ](#tts.extension.testManagementService.TmUserAdapter.TmUserAdapter.GetName)
    - [M GetAvailableProperties ](#tts.extension.testManagementService.TmUserAdapter.TmUserAdapter.GetAvailableProperties)
    - [M Login ](#tts.extension.testManagementService.TmUserAdapter.TmUserAdapter.Login)
    - [M Logout ](#tts.extension.testManagementService.TmUserAdapter.TmUserAdapter.Logout)
    - [M IsLoggedIn ](#tts.extension.testManagementService.TmUserAdapter.TmUserAdapter.IsLoggedIn)
    - [M ExportProject ](#tts.extension.testManagementService.TmUserAdapter.TmUserAdapter.ExportProject)
    - [M ImportProject ](#tts.extension.testManagementService.TmUserAdapter.TmUserAdapter.ImportProject)
    - [M ExportPackage ](#tts.extension.testManagementService.TmUserAdapter.TmUserAdapter.ExportPackage)
    - [M ExportPackageChanges ](#tts.extension.testManagementService.TmUserAdapter.TmUserAdapter.ExportPackageChanges)
    - [M ImportPackage ](#tts.extension.testManagementService.TmUserAdapter.TmUserAdapter.ImportPackage)
    - [M GetCustomPackageActions ](#tts.extension.testManagementService.TmUserAdapter.TmUserAdapter.GetCustomPackageActions)
    - [M GetCustomProjectActions ](#tts.extension.testManagementService.TmUserAdapter.TmUserAdapter.GetCustomProjectActions)
    - [M GetCustomDirectoryActions ](#tts.extension.testManagementService.TmUserAdapter.TmUserAdapter.GetCustomDirectoryActions)
    - [M GetProjectsFromTms ](#tts.extension.testManagementService.TmUserAdapter.TmUserAdapter.GetProjectsFromTms)
    - [M GetPackagesFromTms ](#tts.extension.testManagementService.TmUserAdapter.TmUserAdapter.GetPackagesFromTms)
    - [M UpdateAttributeDefinitions ](#tts.extension.testManagementService.TmUserAdapter.TmUserAdapter.UpdateAttributeDefinitions)
    - [M FetchChildrenForPackageImport ](#tts.extension.testManagementService.TmUserAdapter.TmUserAdapter.FetchChildrenForPackageImport)
    - [M FetchChildrenForProjectImport ](#tts.extension.testManagementService.TmUserAdapter.TmUserAdapter.FetchChildrenForProjectImport)
- [ TmObjectInfo ](#module-tts.extension.testManagementService.userTestmanagement.api.data.TmObjectInfo)
  - [C TmObjectInfo ](#tts.extension.testManagementService.userTestmanagement.api.data.TmObjectInfo.TmObjectInfo)
    - [M `\_\_init\_\_` ](#tts.extension.testManagementService.userTestmanagement.api.data.TmObjectInfo.TmObjectInfo.__init__)
    - [A name ](#tts.extension.testManagementService.userTestmanagement.api.data.TmObjectInfo.TmObjectInfo.name)
    - [A tmsId ](#tts.extension.testManagementService.userTestmanagement.api.data.TmObjectInfo.TmObjectInfo.tmsId)
    - [A attributes ](#tts.extension.testManagementService.userTestmanagement.api.data.TmObjectInfo.TmObjectInfo.attributes)

[ UserUtility API ](../user-utility/user-utility.md)

[ Utility Examples ](../user-utility/example-utilities.md)

Tm User API

- [ TmUserAdapter ](#module-tts.extension.testManagementService.TmUserAdapter)
  - [C TmUserAdapter ](#tts.extension.testManagementService.TmUserAdapter.TmUserAdapter)
    - [M `\_\_init\_\_` ](#tts.extension.testManagementService.TmUserAdapter.TmUserAdapter.__init__)
    - [M GetName ](#tts.extension.testManagementService.TmUserAdapter.TmUserAdapter.GetName)
    - [M GetAvailableProperties ](#tts.extension.testManagementService.TmUserAdapter.TmUserAdapter.GetAvailableProperties)
    - [M Login ](#tts.extension.testManagementService.TmUserAdapter.TmUserAdapter.Login)
    - [M Logout ](#tts.extension.testManagementService.TmUserAdapter.TmUserAdapter.Logout)
    - [M IsLoggedIn ](#tts.extension.testManagementService.TmUserAdapter.TmUserAdapter.IsLoggedIn)
    - [M ExportProject ](#tts.extension.testManagementService.TmUserAdapter.TmUserAdapter.ExportProject)
    - [M ImportProject ](#tts.extension.testManagementService.TmUserAdapter.TmUserAdapter.ImportProject)
    - [M ExportPackage ](#tts.extension.testManagementService.TmUserAdapter.TmUserAdapter.ExportPackage)
    - [M ExportPackageChanges ](#tts.extension.testManagementService.TmUserAdapter.TmUserAdapter.ExportPackageChanges)
    - [M ImportPackage ](#tts.extension.testManagementService.TmUserAdapter.TmUserAdapter.ImportPackage)
    - [M GetCustomPackageActions ](#tts.extension.testManagementService.TmUserAdapter.TmUserAdapter.GetCustomPackageActions)
    - [M GetCustomProjectActions ](#tts.extension.testManagementService.TmUserAdapter.TmUserAdapter.GetCustomProjectActions)
    - [M GetCustomDirectoryActions ](#tts.extension.testManagementService.TmUserAdapter.TmUserAdapter.GetCustomDirectoryActions)
    - [M GetProjectsFromTms ](#tts.extension.testManagementService.TmUserAdapter.TmUserAdapter.GetProjectsFromTms)
    - [M GetPackagesFromTms ](#tts.extension.testManagementService.TmUserAdapter.TmUserAdapter.GetPackagesFromTms)
    - [M UpdateAttributeDefinitions ](#tts.extension.testManagementService.TmUserAdapter.TmUserAdapter.UpdateAttributeDefinitions)
    - [M FetchChildrenForPackageImport ](#tts.extension.testManagementService.TmUserAdapter.TmUserAdapter.FetchChildrenForPackageImport)
    - [M FetchChildrenForProjectImport ](#tts.extension.testManagementService.TmUserAdapter.TmUserAdapter.FetchChildrenForProjectImport)
- [ TmObjectInfo ](#module-tts.extension.testManagementService.userTestmanagement.api.data.TmObjectInfo)
  - [C TmObjectInfo ](#tts.extension.testManagementService.userTestmanagement.api.data.TmObjectInfo.TmObjectInfo)
    - [M `\_\_init\_\_` ](#tts.extension.testManagementService.userTestmanagement.api.data.TmObjectInfo.TmObjectInfo.__init__)
    - [A name ](#tts.extension.testManagementService.userTestmanagement.api.data.TmObjectInfo.TmObjectInfo.name)
    - [A tmsId ](#tts.extension.testManagementService.userTestmanagement.api.data.TmObjectInfo.TmObjectInfo.tmsId)
    - [A attributes ](#tts.extension.testManagementService.userTestmanagement.api.data.TmObjectInfo.TmObjectInfo.attributes)

# Tm User API[¶](#tm-user-api "Link to this heading")

## TmUserAdapter[¶](#module-tts.extension.testManagementService.TmUserAdapter "Link to this heading")

*class* TmUserAdapter[¶](#tts.extension.testManagementService.TmUserAdapter.TmUserAdapter "Link to this definition")  
This class describes the interface of a user test management adapter. This interface offers the possibility to implement your own adapter as a connection to a test management system.

In order for ecu.test to recognize a class as a user test management adapter, the class must meet the requirements of this interface. In addition, the `MODULE_TYPE` must be set to `USER_TMS`.

    import ...

    MODULE_TYPE = 'USER_TMS'

    class TmUserAdapter:
        def __init__(self, properties: dict[str, int | str | float | bool | None]) -> None:
            ...

`\_\_init\_\_`(*[properties](#tts.extension.testManagementService.TmUserAdapter.TmUserAdapter.__init__.properties "tts.extension.testManagementService.TmUserAdapter.TmUserAdapter.__init__.properties (Python parameter) — Contains the configured properties for the concrete adapter as a dictionary. Key: The name of the property. Value: The value for the property.")*)[¶](#tts.extension.testManagementService.TmUserAdapter.TmUserAdapter.__init__ "Link to this definition")  
Parameters:  properties : dict[str, int | str | float | bool | None][¶](#tts.extension.testManagementService.TmUserAdapter.TmUserAdapter.__init__.properties "Permalink to this definition")  
Contains the configured properties for the concrete adapter as a dictionary. Key: The name of the property. Value: The value for the property.

*classmethod* GetName()[¶](#tts.extension.testManagementService.TmUserAdapter.TmUserAdapter.GetName "Link to this definition")  
Returns:  The name of the user test management adapter. This name is displayed in the test management configuration.

Return type:  str

*classmethod* GetAvailableProperties()[¶](#tts.extension.testManagementService.TmUserAdapter.TmUserAdapter.GetAvailableProperties "Link to this definition")  
*Optional (does not have to be implemented)*

Defines the properties available for the user test management adapter as dictionary. Each property is identified by its name and described within its own dict containing information on ‘Description’, ‘Type’ and ‘Default’. Note that this method defines the properties that are generally available within ecu.test’s settings. The values that have been set by the user for each property will be available at runtime through the properties dictionary passed to the `\_\_init\_\_`() method.

Example:

    @classmethod
    def GetAvailableProperties(cls) -> dict[str, dict]:
        return {
            'Option 1': {
                'Description': 'This is Option 1',
                'Type': 'STRING',
                'Default': 'default value',
            },
            'Option 2 (bool)': {
                'Description': 'This is Option 2 (bool)',
                'Type': 'BOOL',
                'Default': False,
            },
            'Option 3': {
                'Description': 'This is int Option 3',
                'Type': 'INTEGER',
                'Default': 42,
            },
            'Option 4': {
                'Description': 'This is float Option 4',
                'Type': 'FLOAT',
                'Default': 9.99999,
            },
        }

Returns:  Dictionary with properties of the user test management adapter.

Return type:  dict[str, dict]

Login()[¶](#tts.extension.testManagementService.TmUserAdapter.TmUserAdapter.Login "Link to this definition")  
Log in to the test management system.

Returns:  True if login was successful, False otherwise.

Return type:  bool

Logout()[¶](#tts.extension.testManagementService.TmUserAdapter.TmUserAdapter.Logout "Link to this definition")  
Log out of the test management system.

Returns:  True if logout was successful, False otherwise.

Return type:  bool

IsLoggedIn()[¶](#tts.extension.testManagementService.TmUserAdapter.TmUserAdapter.IsLoggedIn "Link to this definition")  
Returns if there is currently an active user logged in. Depending on that information, Login() may be called for the current user action.

Returns:  True if the active user is logged in, False otherwise.

Return type:  bool

ExportProject(*[filePaths](#tts.extension.testManagementService.TmUserAdapter.TmUserAdapter.ExportProject.filePaths "tts.extension.testManagementService.TmUserAdapter.TmUserAdapter.ExportProject.filePaths (Python parameter) — The file paths (.prj) of the projects that should be exported.")*)[¶](#tts.extension.testManagementService.TmUserAdapter.TmUserAdapter.ExportProject "Link to this definition")  
*Optional (does not have to be implemented)*

Exports PRJ files to the test management system.

Info

To ensure the test runs of the project can be linked to the exported test suite within the test management system, it is usually necessary to set the matching test suite ID within the original PRJ file, see also ObjectApi.ProjectApi.Project.SetTestSuiteId().

Parameters:  filePaths : list[str][¶](#tts.extension.testManagementService.TmUserAdapter.TmUserAdapter.ExportProject.filePaths "Permalink to this definition")  
The file paths (.prj) of the projects that should be exported.

ImportProject(*[targetDirectory](#tts.extension.testManagementService.TmUserAdapter.TmUserAdapter.ImportProject.targetDirectory "tts.extension.testManagementService.TmUserAdapter.TmUserAdapter.ImportProject.targetDirectory (Python parameter) — Directory for export as selected by the user. The generated project file should be saved within that directory.")*, *[tmsIds](#tts.extension.testManagementService.TmUserAdapter.TmUserAdapter.ImportProject.tmsIds "tts.extension.testManagementService.TmUserAdapter.TmUserAdapter.ImportProject.tmsIds (Python parameter) — List of identifiers of the projects to be imported from the test management system.")*)[¶](#tts.extension.testManagementService.TmUserAdapter.TmUserAdapter.ImportProject "Link to this definition")  
*Optional (does not have to be implemented)*

Imports projects from test management system and saves it as PRJ files. This method needs to contain: - the selection of the project within the test management system - the generation of the PRJ file using the ObjectApi.ProjectApi.

Info

To ensure the test runs of the specific project can be linked to the original test suite within the test management system, it is usually necessary to set a test suite ID for the PRJ file, see also ObjectApi.ProjectApi.Project.SetTestSuiteId().

Parameters:  targetDirectory : str[¶](#tts.extension.testManagementService.TmUserAdapter.TmUserAdapter.ImportProject.targetDirectory "Permalink to this definition")  
Directory for export as selected by the user. The generated project file should be saved within that directory.

tmsIds : list[str][¶](#tts.extension.testManagementService.TmUserAdapter.TmUserAdapter.ImportProject.tmsIds "Permalink to this definition")  
List of identifiers of the projects to be imported from the test management system.

ExportPackage(*[filePaths](#tts.extension.testManagementService.TmUserAdapter.TmUserAdapter.ExportPackage.filePaths "tts.extension.testManagementService.TmUserAdapter.TmUserAdapter.ExportPackage.filePaths (Python parameter) — Paths of the package files (.pkg) to be exported.")*)[¶](#tts.extension.testManagementService.TmUserAdapter.TmUserAdapter.ExportPackage "Link to this definition")  
*Optional (does not have to be implemented)*

Exports PKG files to the test management system.

Info

To ensure the test runs of the package can be linked to the original test script within the test management system, it is usually necessary to set the correct test management ID for the PKG file after export to the test management system, see ObjectApi.PackageApi.Package.SetTestScriptId().

Parameters:  filePaths : list[str][¶](#tts.extension.testManagementService.TmUserAdapter.TmUserAdapter.ExportPackage.filePaths "Permalink to this definition")  
Paths of the package files (.pkg) to be exported.

ExportPackageChanges(*[filePaths](#tts.extension.testManagementService.TmUserAdapter.TmUserAdapter.ExportPackageChanges.filePaths "tts.extension.testManagementService.TmUserAdapter.TmUserAdapter.ExportPackageChanges.filePaths (Python parameter) — Paths of the package files (.pkg) to be exported.")*)[¶](#tts.extension.testManagementService.TmUserAdapter.TmUserAdapter.ExportPackageChanges "Link to this definition")  
*Optional (does not have to be implemented)*

Exports PKG file changes to the test management system.

Parameters:  filePaths : list[str][¶](#tts.extension.testManagementService.TmUserAdapter.TmUserAdapter.ExportPackageChanges.filePaths "Permalink to this definition")  
Paths of the package files (.pkg) to be exported.

ImportPackage(*[targetDirectory](#tts.extension.testManagementService.TmUserAdapter.TmUserAdapter.ImportPackage.targetDirectory "tts.extension.testManagementService.TmUserAdapter.TmUserAdapter.ImportPackage.targetDirectory (Python parameter) — Directory for export as selected by the user. The generated package file should be saved within that directory.")*, *[tmsIds](#tts.extension.testManagementService.TmUserAdapter.TmUserAdapter.ImportPackage.tmsIds "tts.extension.testManagementService.TmUserAdapter.TmUserAdapter.ImportPackage.tmsIds (Python parameter) — List of identifiers of the packages to be imported from the test management system.")*)[¶](#tts.extension.testManagementService.TmUserAdapter.TmUserAdapter.ImportPackage "Link to this definition")  
*Optional (does not have to be implemented)*

Imports packages from the test management system and saves it as PKG files. This method needs to contain: - the selection of the package within the test management system - the generation of the PKG file using the ObjectApi.PackageApi.

Info

To ensure the test runs of the package can be linked to the original test script within the test management system, it is usually necessary to set a test management ID for the PKG file, see also ObjectApi.PackageApi.Package.SetTestScriptId().

Parameters:  targetDirectory : str[¶](#tts.extension.testManagementService.TmUserAdapter.TmUserAdapter.ImportPackage.targetDirectory "Permalink to this definition")  
Directory for export as selected by the user. The generated package file should be saved within that directory.

tmsIds : list[str][¶](#tts.extension.testManagementService.TmUserAdapter.TmUserAdapter.ImportPackage.tmsIds "Permalink to this definition")  
List of identifiers of the packages to be imported from the test management system.

*classmethod* GetCustomPackageActions()[¶](#tts.extension.testManagementService.TmUserAdapter.TmUserAdapter.GetCustomPackageActions "Link to this definition")  
*Optional (does not have to be implemented)*

Allows to define custom actions for Packages. These will be added to the “Test management” context menu if one or more Packages are selected. Please note that every action’s callback method must be able to handle a list of file paths, in case multiple Packages were selected.

Example:

    @classmethod
    def GetCustomPackageActions(cls) -> dict[str, Callable[[list[str]], None]]:
        return {
            "My custom package action": cls.MyPackageAction
        }

    def MyPackageAction(self, packagePaths: list[str]) -> None:
        for pkgPath in packagePaths:
            print(f"Processing package {pkgPath}")

Returns:  A dictionary that maps action labels to their callback.

Return type:  dict[str, Callable[[list[str]], None]]

*classmethod* GetCustomProjectActions()[¶](#tts.extension.testManagementService.TmUserAdapter.TmUserAdapter.GetCustomProjectActions "Link to this definition")  
*Optional (does not have to be implemented)*

Allows to define custom actions for Projects. These will be added to the “Test management” context menu if one or more Projects are selected. Please note that every action’s callback method must be able to handle a list of file paths, in case multiple Projects were selected.

Example:

    @classmethod
    def GetCustomProjectActions(cls) -> dict[str, Callable[[list[str]], None]]:
        return {
            "My custom project action": cls.MyProjectAction
        }

    def MyProjectAction(self, projectPaths: list[str]) -> None:
        for prjPath in projectPaths:
            print(f"Processing project {prjPath}")

Returns:  A dictionary that maps action labels to their callback.

Return type:  dict[str, Callable[[list[str]], None]]

*classmethod* GetCustomDirectoryActions()[¶](#tts.extension.testManagementService.TmUserAdapter.TmUserAdapter.GetCustomDirectoryActions "Link to this definition")  
*Optional (does not have to be implemented)*

Allows to define custom actions for directories. These will be added to the “Test management” context menu if one or more directories are selected. Please note that every action’s callback method must be able to handle a list of file paths, in case multiple directories were selected.

Example:

    @classmethod
    def GetCustomDirectoryActions(cls) -> dict[str, Callable[[list[str]], None]]:
        return {
            "My custom directory action": cls.MyDirectoryAction
        }

    def MyDirectoryAction(self, directoryPaths: list[str]) -> None:
        for dirPath in directoryPaths:
            print(f"Processing directory {dirPath}")

Returns:  A dictionary that maps action labels to their callback.

Return type:  dict[str, Callable[[list[str]], None]]

GetProjectsFromTms()[¶](#tts.extension.testManagementService.TmUserAdapter.TmUserAdapter.GetProjectsFromTms "Link to this definition")  
*Optional (does not have to be implemented)*

Deprecated since version 2025.4: Please use FetchChildrenForProjectImport instead.

Returns the projects available from the test management system. The result will be displayed in the dialog to import projects. For the chosen projects ImportProject() will be called.

Returns:  List with available projects.

Return type:  list[[TmObjectInfo](#tts.extension.testManagementService.userTestmanagement.api.data.TmObjectInfo.TmObjectInfo "tts.extension.testManagementService.userTestmanagement.api.data.TmObjectInfo.TmObjectInfo (Python class) — Contains information about an object from the test management system.")]

GetPackagesFromTms()[¶](#tts.extension.testManagementService.TmUserAdapter.TmUserAdapter.GetPackagesFromTms "Link to this definition")  
*Optional (does not have to be implemented)*

Deprecated since version 2025.4: Please use FetchChildrenForPackageImport instead.

Returns the packages available from the test management system. The result will be displayed in the dialog to import packages. For the chosen packages ImportPackage() will be called.

Returns:  List with available packages.

Return type:  list[[TmObjectInfo](#tts.extension.testManagementService.userTestmanagement.api.data.TmObjectInfo.TmObjectInfo "tts.extension.testManagementService.userTestmanagement.api.data.TmObjectInfo.TmObjectInfo (Python class) — Contains information about an object from the test management system.")]

UpdateAttributeDefinitions()[¶](#tts.extension.testManagementService.TmUserAdapter.TmUserAdapter.UpdateAttributeDefinitions "Link to this definition")  
*Optional (does not have to be implemented)*

Queries all available attributes from the test management system for use in packages and projects.

FetchChildrenForPackageImport(*[tmsId](#tts.extension.testManagementService.TmUserAdapter.TmUserAdapter.FetchChildrenForPackageImport.tmsId "tts.extension.testManagementService.TmUserAdapter.TmUserAdapter.FetchChildrenForPackageImport.tmsId (Python parameter) — Tms id of the parent object.")*)[¶](#tts.extension.testManagementService.TmUserAdapter.TmUserAdapter.FetchChildrenForPackageImport "Link to this definition")  
*Optional (does not have to be implemented)*

Returns the direct children (only first level) for the test management object with the specified tms id. If the tms id is empty the top-level objects are returned. The result will be displayed in the dialog to import packages. For the chosen packages ImportPackage() will be called.

Parameters:  tmsId : str[¶](#tts.extension.testManagementService.TmUserAdapter.TmUserAdapter.FetchChildrenForPackageImport.tmsId "Permalink to this definition")  
Tms id of the parent object.

Returns:  List with available children.

Return type:  list[[TmObjectInfo](#tts.extension.testManagementService.userTestmanagement.api.data.TmObjectInfo.TmObjectInfo "tts.extension.testManagementService.userTestmanagement.api.data.TmObjectInfo.TmObjectInfo (Python class) — Contains information about an object from the test management system.")]

FetchChildrenForProjectImport(*[tmsId](#tts.extension.testManagementService.TmUserAdapter.TmUserAdapter.FetchChildrenForProjectImport.tmsId "tts.extension.testManagementService.TmUserAdapter.TmUserAdapter.FetchChildrenForProjectImport.tmsId (Python parameter) — Tms id of the parent object.")*)[¶](#tts.extension.testManagementService.TmUserAdapter.TmUserAdapter.FetchChildrenForProjectImport "Link to this definition")  
*Optional (does not have to be implemented)*

Returns the direct children (only first level) for the test management object with the specified tms id. If the tms id is empty the top-level objects are returned. The result will be displayed in the dialog to import projects. For the chosen projects ImportProject() will be called.

Parameters:  tmsId : str[¶](#tts.extension.testManagementService.TmUserAdapter.TmUserAdapter.FetchChildrenForProjectImport.tmsId "Permalink to this definition")  
Tms id of the parent object.

Returns:  List with available children.

Return type:  list[[TmObjectInfo](#tts.extension.testManagementService.userTestmanagement.api.data.TmObjectInfo.TmObjectInfo "tts.extension.testManagementService.userTestmanagement.api.data.TmObjectInfo.TmObjectInfo (Python class) — Contains information about an object from the test management system.")]

## TmObjectInfo[¶](#module-tts.extension.testManagementService.userTestmanagement.api.data.TmObjectInfo "Link to this heading")

*class* TmObjectInfo[¶](#tts.extension.testManagementService.userTestmanagement.api.data.TmObjectInfo.TmObjectInfo "Link to this definition")  
Contains information about an object from the test management system.

`\_\_init\_\_`(*[name](#tts.extension.testManagementService.userTestmanagement.api.data.TmObjectInfo.TmObjectInfo.__init__.name "tts.extension.testManagementService.userTestmanagement.api.data.TmObjectInfo.TmObjectInfo.__init__.name (Python parameter) — Name of the object inside the test management system.")*, *[tmsId](#tts.extension.testManagementService.userTestmanagement.api.data.TmObjectInfo.TmObjectInfo.__init__.tmsId "tts.extension.testManagementService.userTestmanagement.api.data.TmObjectInfo.TmObjectInfo.__init__.tmsId (Python parameter) — Identifier inside the test management system.")*, *[attributes](#tts.extension.testManagementService.userTestmanagement.api.data.TmObjectInfo.TmObjectInfo.__init__.attributes "tts.extension.testManagementService.userTestmanagement.api.data.TmObjectInfo.TmObjectInfo.__init__.attributes (Python parameter) — Additional information about the object.")=`None`*)[¶](#tts.extension.testManagementService.userTestmanagement.api.data.TmObjectInfo.TmObjectInfo.__init__ "Link to this definition")  
Parameters:  name : str[¶](#tts.extension.testManagementService.userTestmanagement.api.data.TmObjectInfo.TmObjectInfo.__init__.name "Permalink to this definition")  
Name of the object inside the test management system.

tmsId : str[¶](#tts.extension.testManagementService.userTestmanagement.api.data.TmObjectInfo.TmObjectInfo.__init__.tmsId "Permalink to this definition")  
Identifier inside the test management system.

attributes : dict[str, str] | None[¶](#tts.extension.testManagementService.userTestmanagement.api.data.TmObjectInfo.TmObjectInfo.__init__.attributes "Permalink to this definition")  
Additional information about the object. E.g. author, date etc.

name[¶](#tts.extension.testManagementService.userTestmanagement.api.data.TmObjectInfo.TmObjectInfo.name "Link to this definition")  
Returns:  Returns the name of the object.

tmsId[¶](#tts.extension.testManagementService.userTestmanagement.api.data.TmObjectInfo.TmObjectInfo.tmsId "Link to this definition")  
Returns:  Returns the identifier of the object.

attributes[¶](#tts.extension.testManagementService.userTestmanagement.api.data.TmObjectInfo.TmObjectInfo.attributes "Link to this definition")  
Returns:  Returns the attributes of the object.

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
