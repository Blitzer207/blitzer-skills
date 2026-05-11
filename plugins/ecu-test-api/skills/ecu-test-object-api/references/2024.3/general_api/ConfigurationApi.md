# API for Configurations[¶](#api-for-configurations "Link to this heading")

Part of the [Object based program API](objectApi.md#objectapi)

## ConfigurationApi[¶](#configurationapi "Link to this heading")

*class* ConfigurationApi[¶](#ApiClient.ConfigurationApi "Link to this definition")  
API to access configuration files

Returned by

- [`ApiClient.ConfigurationApi`](objectApi.md#ApiClient.ApiClient.ConfigurationApi "ApiClient.ApiClient.ConfigurationApi")

ReportFilterApi[¶](#ApiClient.ConfigurationApi.ReportFilterApi "Link to this definition")  
Returns the ReportFilterApi namespace.

Returns:  ReportFilterApi namespace

Return type:  [`ReportFilterApi`](ReportFilterApi.md#ApiClient.ReportFilterApi "ApiClient.ReportFilterApi")

CreateTestBenchConfiguration()[¶](#ApiClient.ConfigurationApi.CreateTestBenchConfiguration "Link to this definition")  
Creates new test bench configuration.

Returns:  New empty test bench configuration

Return type:  [`TestBenchConfiguration`](#ApiClient.TestBenchConfiguration "ApiClient.TestBenchConfiguration")

CreateTestConfiguration()[¶](#ApiClient.ConfigurationApi.CreateTestConfiguration "Link to this definition")  
Creates a new test configuration.

Returns:  New empty test configuration

Return type:  [`TestConfiguration`](#ApiClient.TestConfiguration "ApiClient.TestConfiguration")

GetChangesForTestBenchConfigurations(*oldTestBenchConfig*, *newTestBenchConfig*)[¶](#ApiClient.ConfigurationApi.GetChangesForTestBenchConfigurations "Link to this definition")  
Get the changes that exist between two given test bench configurations.

Parameters:  - **oldTestBenchConfig** ([`TestBenchConfiguration`](#ApiClient.TestBenchConfiguration "ApiClient.TestBenchConfiguration")) – The old test bench configuration to compare.

- **newTestBenchConfig** ([`TestBenchConfiguration`](#ApiClient.TestBenchConfiguration "ApiClient.TestBenchConfiguration")) – The new test bench configuration to compare.

Returns:  The changes that exist between the two test bench configurations.

Return type:  list[[`Change`](#ApiClient.Change "ApiClient.Change")]

GetChangesForTestConfigurations(*oldTestConfig*, *newTestConfig*)[¶](#ApiClient.ConfigurationApi.GetChangesForTestConfigurations "Link to this definition")  
Get the changes that exist between two given test configurations.

Parameters:  - **oldTestConfig** ([`TestConfiguration`](#ApiClient.TestConfiguration "ApiClient.TestConfiguration")) – The old test configuration to compare.

- **newTestConfig** ([`TestConfiguration`](#ApiClient.TestConfiguration "ApiClient.TestConfiguration")) – The new test configuration to compare.

Returns:  The changes that exist between the two test configurations.

Return type:  list[[`Change`](#ApiClient.Change "ApiClient.Change")]

OpenTestBenchConfiguration(*filename*)[¶](#ApiClient.ConfigurationApi.OpenTestBenchConfiguration "Link to this definition")  
Opens an existing test bench configuration (\*.tbc).

Parameters:  **filename** (*str*) – File name of the test bench configuration file (\*.tbc); Either absolute or relative to the ‘Configuration’ directory

Returns:  Loaded test bench configuration

Return type:  [`TestBenchConfiguration`](#ApiClient.TestBenchConfiguration "ApiClient.TestBenchConfiguration")

Raises:  
**ApiError** – If the test bench configuration file (\*.tbc) does not exist.

OpenTestConfiguration(*filename*)[¶](#ApiClient.ConfigurationApi.OpenTestConfiguration "Link to this definition")  
Opens an existing test configuration.

Parameters:  **filename** (*str*) – File name of the test configuration file (\*.tcf); Either absolute or relative to the ‘Configuration’ directory

Returns:  Loaded test configuration

Return type:  [`TestConfiguration`](#ApiClient.TestConfiguration "ApiClient.TestConfiguration")

Raises:  
**ApiError** – If the test configuration file (\*.tcf) does not exist.

SearchTestBenchConfigurations(*searchCriteria*, *useExtendedMode=False*)[¶](#ApiClient.ConfigurationApi.SearchTestBenchConfigurations "Link to this definition")  
Searches the current workspace and library workspaces for Testbenchconfigurations matching the given search criteria.

Parameters:  - **searchCriteria** (*str*) – The search criteria expressed in the ecu.test filter syntax. See section “Handling” =\> “Filter” of the ecu.test User Documentation.

- **useExtendedMode** (*boolean*) – If True, extended search strings are enabled. The default is False, meaning each word in the searchCriteria will be enclosed by wildcards and mapped to the filename. (e.g. “hello world” =\> “Name = ‘\*hello\*’ and Name = ‘\*world\*’”)

Returns:  All matching Testbenchconfigurations. If no file matches, an emtpy list is returned.

Return type:  list[[`TestBenchConfiguration`](#ApiClient.TestBenchConfiguration "ApiClient.TestBenchConfiguration")]

Raises:  
**ApiError** – If the searchCriteria has an illegal syntax.

SearchTestConfigurations(*searchCriteria*, *useExtendedMode=False*)[¶](#ApiClient.ConfigurationApi.SearchTestConfigurations "Link to this definition")  
Searches the current workspace and library workspaces for Testconfigurations matching the given search criteria.

Parameters:  - **searchCriteria** (*str*) – The search criteria expressed in the ecu.test filter syntax. See section “Handling” =\> “Filter” of the ecu.test User Documentation.

- **useExtendedMode** (*boolean*) – If True, extended search strings are enabled. The default is False, meaning each word in the searchCriteria will be enclosed by wildcards and mapped to the filename. (e.g. “hello world” =\> “Name = ‘\*hello\*’ and Name = ‘\*world\*’”)

Returns:  All matching Testconfigurations. If no file matches, an emtpy list is returned.

Return type:  list[[`TestConfiguration`](#ApiClient.TestConfiguration "ApiClient.TestConfiguration")]

Raises:  
**ApiError** – If the searchCriteria has an illegal syntax.

## TestBenchConfiguration[¶](#testbenchconfiguration "Link to this heading")

*class* TestBenchConfiguration[¶](#ApiClient.TestBenchConfiguration "Link to this definition")  
Returned by

- [`ConfigurationApi.CreateTestBenchConfiguration`](#ApiClient.ConfigurationApi.CreateTestBenchConfiguration "ApiClient.ConfigurationApi.CreateTestBenchConfiguration")

- [`ConfigurationApi.OpenTestBenchConfiguration`](#ApiClient.ConfigurationApi.OpenTestBenchConfiguration "ApiClient.ConfigurationApi.OpenTestBenchConfiguration")

- [`ConfigurationApi.SearchTestBenchConfigurations`](#ApiClient.ConfigurationApi.SearchTestBenchConfigurations "ApiClient.ConfigurationApi.SearchTestBenchConfigurations")

CreateToolHost(*toolHostUrl*)[¶](#ApiClient.TestBenchConfiguration.CreateToolHost "Link to this definition")  
Creates a new tool host with the given URL. E.g.:

> - ‘local’
>
> - ‘tsp:127.0.0.1:5017’
>
> - ‘tsp:hostname:5017’

Parameters:  **toolHostUrl** (*str*) – The URL of the created tool host

Returns:  The newly created tool host object

Return type:  [`ToolHost`](#ApiClient.ToolHost "ApiClient.ToolHost")

GetFilename()[¶](#ApiClient.TestBenchConfiguration.GetFilename "Link to this definition")  
Returns the absolute path to the test bench configuration file. If empty, the file has not been saved yet.

Returns:  filename with extension

Return type:  str

GetPort(*portId*)[¶](#ApiClient.TestBenchConfiguration.GetPort "Link to this definition")  
Returns the port with the given portId.

Parameters:  **portId** (*str*) – Name of the port

Returns:  The port object.

Return type:  [`Port`](#ApiClient.Port "ApiClient.Port")

Raises:  
**ApiError** – If there is no port with this Id.

GetTool(*toolId*)[¶](#ApiClient.TestBenchConfiguration.GetTool "Link to this definition")  
Returns the tool with the given toolId.

Parameters:  **toolId** (*str*) – ID of the tool

Returns:  The tool object.

Return type:  [`Tool`](#ApiClient.Tool "ApiClient.Tool")

Raises:  
**ApiError** – If there is no tool with this Id.

GetToolHost(*url*)[¶](#ApiClient.TestBenchConfiguration.GetToolHost "Link to this definition")  
Returns the tool host with the given URL.

Parameters:  **url** (*str*) – URL of the tool host

Returns:  The tool host object.

Return type:  [`ToolHost`](#ApiClient.ToolHost "ApiClient.ToolHost")

Raises:  
**ApiError** – If there is no host using this URL.

GetToolHosts()[¶](#ApiClient.TestBenchConfiguration.GetToolHosts "Link to this definition")  
Returns a list of all tool hosts belonging to this testbench configuration.

Returns:  The list of all tool host objects

Return type:  list[[`ToolHost`](#ApiClient.ToolHost "ApiClient.ToolHost")]

Refresh()[¶](#ApiClient.TestBenchConfiguration.Refresh "Link to this definition")  
Refreshes all hosts, tools and ports in the configuration

RemoveToolHost(*toolHost*)[¶](#ApiClient.TestBenchConfiguration.RemoveToolHost "Link to this definition")  
Removes the tool host and all configured tools and ports connected to it.

Parameters:  **toolHost** ([`ToolHost`](#ApiClient.ToolHost "ApiClient.ToolHost")) – The tool host object to be removed

Save(*filename=None*)[¶](#ApiClient.TestBenchConfiguration.Save "Link to this definition")  
Saves the test bench configuration. Appends file ending if needed.

Parameters:  **filename** (*str*) – The file name used for storing the test bench configuration file; Either absolute or relative to the ‘Configuration’ directory. Leave out to save the configuration to its existing file (from a previous call of [`Save()`](#ApiClient.TestBenchConfiguration.Save "ApiClient.TestBenchConfiguration.Save") or from [`ConfigurationApi.OpenTestBenchConfiguration()`](#ApiClient.ConfigurationApi.OpenTestBenchConfiguration "ApiClient.ConfigurationApi.OpenTestBenchConfiguration"))

## ToolHost[¶](#toolhost "Link to this heading")

*class* ToolHost[¶](#ApiClient.ToolHost "Link to this definition")  
Returned by

- [`TestBenchConfiguration.CreateToolHost`](#ApiClient.TestBenchConfiguration.CreateToolHost "ApiClient.TestBenchConfiguration.CreateToolHost")

- [`TestBenchConfiguration.GetToolHost`](#ApiClient.TestBenchConfiguration.GetToolHost "ApiClient.TestBenchConfiguration.GetToolHost")

- [`TestBenchConfiguration.GetToolHosts`](#ApiClient.TestBenchConfiguration.GetToolHosts "ApiClient.TestBenchConfiguration.GetToolHosts")

AddTool(*toolName*, *useLegacyName=True*)[¶](#ApiClient.ToolHost.AddTool "Link to this definition")  
Configures a tool to be used by the corresponding test bench configuration.

Parameters:  - **toolName** (*str*) – The name of the tool to use. Use [`GetAvailableToolNames()`](#ApiClient.ToolHost.GetAvailableToolNames "ApiClient.ToolHost.GetAvailableToolNames") to get a list of all available tool names.

- **useLegacyName** (*bool*) – Prefer short legacy/internal name for the tool instead of combination of vendor and tool name

Returns:  The created tool object

Return type:  [`Tool`](#ApiClient.Tool "ApiClient.Tool")

Clone()[¶](#ApiClient.ToolHost.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`ToolHost`](#ApiClient.ToolHost "ApiClient.ToolHost")

GetAvailableToolNames(*getLegacyNames=False*)[¶](#ApiClient.ToolHost.GetAvailableToolNames "Link to this definition")  
Returns a list of all tools that are available on this tool host.

Parameters:  **getLegacyNames** (*bool*) – Get short legacy/internal names for the tool instead of combination of vendor and tool name

Returns:  The list of available tools

Return type:  list[str]

GetBasePath()[¶](#ApiClient.ToolHost.GetBasePath "Link to this definition")  
Returns the tool host base path that is used for several tool property settings.

Returns:  The tool host base path

Return type:  str

GetTools()[¶](#ApiClient.ToolHost.GetTools "Link to this definition")  
Returns all tools used by this tool host.

Returns:  A list of the used tools.

Return type:  list[[`Tool`](#ApiClient.Tool "ApiClient.Tool")]

GetUrl()[¶](#ApiClient.ToolHost.GetUrl "Link to this definition")  
Returns the tool host URL.

Returns:  The URL

Return type:  str

Refresh()[¶](#ApiClient.ToolHost.Refresh "Link to this definition")  
Refreshes the tool and all its ports

RemoveTool(*tool*)[¶](#ApiClient.ToolHost.RemoveTool "Link to this definition")  
Removes the tool and all configured ports from the tool host.

Parameters:  **tool** ([`Tool`](#ApiClient.Tool "ApiClient.Tool")) – The tool to be removed

Rename(*newUrl*)[¶](#ApiClient.ToolHost.Rename "Link to this definition")  
Sets the URL of a given tool host. E.g.:

> - ‘local’
>
> - ‘tsp:127.0.0.1:5017’
>
> - ‘tsp:hostname:5017’

Parameters:  **newUrl** (*str*) – New URL

SetBasePath(*basePath*)[¶](#ApiClient.ToolHost.SetBasePath "Link to this definition")  
Sets the tool host base path. A value of ‘\<workspace\>’ represents the current workspace path and can be combined with sub-paths (e.g., ‘\<workspace\>/Models’).

Parameters:  **basePath** (*str*) – Base path on the tool host

GetToolAccessTimeout()[¶](#ApiClient.ToolHost.GetToolAccessTimeout "Link to this definition")  
Returns the minimum of timeouts for all tool calls.

Returns:  timeout in seconds

Return type:  int

Deprecated since version 2024.2: Tool access timeout can now be accessed as a property on the tool.

SetToolAccessTimeout(*timeout*)[¶](#ApiClient.ToolHost.SetToolAccessTimeout "Link to this definition")  
Sets the timeout for tool calls. After that time, a tool call will be terminated with an error.

Parameters:  **timeout** (*int*) – timeout in seconds

Deprecated since version 2024.2: Tool access timeout can now be accessed as a property on the tool.

## Tool[¶](#tool "Link to this heading")

*class* Tool[¶](#ApiClient.Tool "Link to this definition")  
Returned by

- [`TestBenchConfiguration.GetTool`](#ApiClient.TestBenchConfiguration.GetTool "ApiClient.TestBenchConfiguration.GetTool")

- [`ToolHost.AddTool`](#ApiClient.ToolHost.AddTool "ApiClient.ToolHost.AddTool")

- [`ToolHost.GetTools`](#ApiClient.ToolHost.GetTools "ApiClient.ToolHost.GetTools")

PropertySet[¶](#ApiClient.Tool.PropertySet "Link to this definition")  
The properties of this tool.

Returns:  the properties of this tool

Return type:  [`PropertySet`](#ApiClient.PropertySet "ApiClient.PropertySet")

START_OPTION_ALWAYS[¶](#ApiClient.Tool.START_OPTION_ALWAYS "Link to this definition")  
Returns the constant used to specify the start option ‘always’: the tool will always be started.

Returns:  The constant

Return type:  int

START_OPTION_CONDITIONAL[¶](#ApiClient.Tool.START_OPTION_CONDITIONAL "Link to this definition")  
Returns the constant used to specify the start option ‘conditional’: the tool will be started when needed.

Returns:  The constant

Return type:  int

START_OPTION_NEVER[¶](#ApiClient.Tool.START_OPTION_NEVER "Link to this definition")  
Returns the constant used to specify the start option ‘never’: the tool will never be started automatically.

Returns:  The constant

Return type:  int

Clone()[¶](#ApiClient.Tool.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`Tool`](#ApiClient.Tool "ApiClient.Tool")

CreatePort(*portType*, *implType=None*)[¶](#ApiClient.Tool.CreatePort "Link to this definition")  
Creates a new port on this tool.

Parameters:  - **portType** (*str*) – The port type to be used. Use [`GetAvailablePortTypes()`](#ApiClient.Tool.GetAvailablePortTypes "ApiClient.Tool.GetAvailablePortTypes") to get a list of all valid values.

- **implType** (*str*) – The implementation type to be used. If the specified portType does not require a specific implementation type, this argument should be None or left out entirely. Use [`GetAvailableImplTypes()`](#ApiClient.Tool.GetAvailableImplTypes "ApiClient.Tool.GetAvailableImplTypes") to get a list of all valid values.

Returns:  The newly created Port object.

Return type:  [`Port`](#ApiClient.Port "ApiClient.Port")

GetAvailableImplTypes(*portType*)[¶](#ApiClient.Tool.GetAvailableImplTypes "Link to this definition")  
Returns a list of all available implementation types for a specified port type.

Parameters:  **portType** (*str*) – The port type to be used. Use [`GetAvailablePortTypes()`](#ApiClient.Tool.GetAvailablePortTypes "ApiClient.Tool.GetAvailablePortTypes") to get a list of all valid values.

Returns:  A list of all available implementation types

Return type:  list[str]

GetAvailablePortTypes()[¶](#ApiClient.Tool.GetAvailablePortTypes "Link to this definition")  
Returns a list of all available port types for this tool.

Returns:  All available port types

Return type:  list[str]

GetId()[¶](#ApiClient.Tool.GetId "Link to this definition")  
Returns the id of the tool.

Returns:  The id of the tool

Return type:  str

GetLegacyName()[¶](#ApiClient.Tool.GetLegacyName "Link to this definition")  
Returns the legacy name of the tool.

Returns:  The name of the tool

Return type:  str

GetName()[¶](#ApiClient.Tool.GetName "Link to this definition")  
Returns the name of the tool.

Returns:  The name of the tool

Return type:  str

GetPorts(*portType=None*)[¶](#ApiClient.Tool.GetPorts "Link to this definition")  
Returns the ports assigned to this tool. If the parameter portType is given, only those ports belonging to this portType will be returned.

Parameters:  **portType** (*str*) – The portType used for filtering the returned ports. Use [`GetAvailablePortTypes()`](#ApiClient.Tool.GetAvailablePortTypes "ApiClient.Tool.GetAvailablePortTypes") to get a list of all valid values. Might be left out.

Returns:  A list of port objects assigned to this tool.

Return type:  list[[`Port`](#ApiClient.Port "ApiClient.Port")]

GetStartOption()[¶](#ApiClient.Tool.GetStartOption "Link to this definition")  
Returns the startoption for this tool.

Returns:  Startoption of the Tool

- [`Tool.START_OPTION_CONDITIONAL`](#ApiClient.Tool.START_OPTION_CONDITIONAL "ApiClient.Tool.START_OPTION_CONDITIONAL")

- [`Tool.START_OPTION_ALWAYS`](#ApiClient.Tool.START_OPTION_ALWAYS "ApiClient.Tool.START_OPTION_ALWAYS")

- [`Tool.START_OPTION_NEVER`](#ApiClient.Tool.START_OPTION_NEVER "ApiClient.Tool.START_OPTION_NEVER")

Return type:  int

GetStartPriority()[¶](#ApiClient.Tool.GetStartPriority "Link to this definition")  
Queries the start priority of the tool.

Returns:  Start priority. The start priority specifies the start order of the tools. A lower numeric value implies a higher priority.

Return type:  int

Refresh()[¶](#ApiClient.Tool.Refresh "Link to this definition")  
Refreshes the properties of the tool and all of its ports

RemovePort(*port*)[¶](#ApiClient.Tool.RemovePort "Link to this definition")  
Removes the port from the tool.

Parameters:  **port** ([`Port`](#ApiClient.Port "ApiClient.Port")) – The port to be removed.

Rename(*newToolId*)[¶](#ApiClient.Tool.Rename "Link to this definition")  
Changes the id of the tool to the given one.

Parameters:  **newToolId** (*str*) – The new id to be used.

Raises:  
**ApiError** – If newtoolId could not be set

SetStartOption(*option*)[¶](#ApiClient.Tool.SetStartOption "Link to this definition")  
Sets the start option of the tool.

Parameters:  **option** (*int*) –

New start option for the tool. Possible values:

- [`Tool.START_OPTION_CONDITIONAL`](#ApiClient.Tool.START_OPTION_CONDITIONAL "ApiClient.Tool.START_OPTION_CONDITIONAL")

- [`Tool.START_OPTION_ALWAYS`](#ApiClient.Tool.START_OPTION_ALWAYS "ApiClient.Tool.START_OPTION_ALWAYS")

- [`Tool.START_OPTION_NEVER`](#ApiClient.Tool.START_OPTION_NEVER "ApiClient.Tool.START_OPTION_NEVER")

SetStartPriority(*value*)[¶](#ApiClient.Tool.SetStartPriority "Link to this definition")  
Sets the start priority of the tool.

Parameters:  **value** (*int*) – Start priority. The start priority specifies the start order of the tools. A lower numeric value implies a higher priority.

## Port[¶](#port "Link to this heading")

*class* Port[¶](#ApiClient.Port "Link to this definition")  
Returned by

- [`TestBenchConfiguration.GetPort`](#ApiClient.TestBenchConfiguration.GetPort "ApiClient.TestBenchConfiguration.GetPort")

- [`Tool.CreatePort`](#ApiClient.Tool.CreatePort "ApiClient.Tool.CreatePort")

- [`Tool.GetPorts`](#ApiClient.Tool.GetPorts "ApiClient.Tool.GetPorts")

AUTOSTART_ALWAYS[¶](#ApiClient.Port.AUTOSTART_ALWAYS "Link to this definition")  
Returns the constant used to specify the autostart option ‘always’: The port will always be started.

Returns:  The constant

Return type:  int

AUTOSTART_CONDITIONAL[¶](#ApiClient.Port.AUTOSTART_CONDITIONAL "Link to this definition")  
Returns the constant used to specify the autostart option ‘conditional’: The port will be started when needed.

Returns:  The constant

Return type:  int

AUTOSTART_NEVER[¶](#ApiClient.Port.AUTOSTART_NEVER "Link to this definition")  
Returns the constant used to specify the autostart option ‘never’: The port will never be started automatically.

Returns:  The constant

Return type:  int

PropertySet[¶](#ApiClient.Port.PropertySet "Link to this definition")  
The properties of this port.

Returns:  properties of this port

Return type:  [`PropertySet`](#ApiClient.PropertySet "ApiClient.PropertySet")

Clone()[¶](#ApiClient.Port.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`Port`](#ApiClient.Port "ApiClient.Port")

GetAutostart()[¶](#ApiClient.Port.GetAutostart "Link to this definition")  
Returns the autostart mode for this port.

Returns:  Autostart option of the port.

- [`Port.AUTOSTART_CONDITIONAL`](#ApiClient.Port.AUTOSTART_CONDITIONAL "ApiClient.Port.AUTOSTART_CONDITIONAL")

- [`Port.AUTOSTART_ALWAYS`](#ApiClient.Port.AUTOSTART_ALWAYS "ApiClient.Port.AUTOSTART_ALWAYS")

- [`Port.AUTOSTART_NEVER`](#ApiClient.Port.AUTOSTART_NEVER "ApiClient.Port.AUTOSTART_NEVER")

Return type:  int

GetId()[¶](#ApiClient.Port.GetId "Link to this definition")  
Returns the id of the port.

Returns:  The id of the port.

Return type:  str

GetImplType()[¶](#ApiClient.Port.GetImplType "Link to this definition")  
Returns the port’s implementation type :return: the implementation type :rtype: str

GetPortType()[¶](#ApiClient.Port.GetPortType "Link to this definition")  
Returns the type of the port.

Returns:  The type of the port.

Return type:  str

Refresh()[¶](#ApiClient.Port.Refresh "Link to this definition")  
Refreshes the properties of the port

Rename(*newPortId*)[¶](#ApiClient.Port.Rename "Link to this definition")  
Changes the id of the port to the given one.

Parameters:  **newPortId** (*str*) – The new id to be used.

Raises:  
**ApiError** – If newPortId could not be set

SetAutostart(*option*)[¶](#ApiClient.Port.SetAutostart "Link to this definition")  
Sets the autostart option of the port.

Parameters:  **option** (*int*) –

New autostart option for the port. Possible values are:

- [`Port.AUTOSTART_CONDITIONAL`](#ApiClient.Port.AUTOSTART_CONDITIONAL "ApiClient.Port.AUTOSTART_CONDITIONAL")

- [`Port.AUTOSTART_ALWAYS`](#ApiClient.Port.AUTOSTART_ALWAYS "ApiClient.Port.AUTOSTART_ALWAYS")

- [`Port.AUTOSTART_NEVER`](#ApiClient.Port.AUTOSTART_NEVER "ApiClient.Port.AUTOSTART_NEVER")

## PropertySet[¶](#propertyset "Link to this heading")

*class* PropertySet[¶](#ApiClient.PropertySet "Link to this definition")  
Returned by

- [`Port.PropertySet`](#ApiClient.Port.PropertySet "ApiClient.Port.PropertySet")

- [`Tool.PropertySet`](#ApiClient.Tool.PropertySet "ApiClient.Tool.PropertySet")

Clone()[¶](#ApiClient.PropertySet.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`PropertySet`](#ApiClient.PropertySet "ApiClient.PropertySet")

GetNames()[¶](#ApiClient.PropertySet.GetNames "Link to this definition")  
Returns a list of the names of all available properties.

Returns:  Names of all available properties

Return type:  list[str]

GetProperties()[¶](#ApiClient.PropertySet.GetProperties "Link to this definition")  
Returns a list of all available properties.

Returns:  all available properties

Return type:  list[[`Property`](#ApiClient.Property "ApiClient.Property")]

GetProperty(*name*)[¶](#ApiClient.PropertySet.GetProperty "Link to this definition")  
Returns the property with the given name. The name is shown in the tooltip of the respective property in the user documentation. Please find it in the properties table of the tool or port.

Parameters:  **name** (*str*) – The name of the desired property

Returns:  The property with the given name

Return type:  [`Property`](#ApiClient.Property "ApiClient.Property")

## Property[¶](#property "Link to this heading")

*class* Property[¶](#ApiClient.Property "Link to this definition")  
Returned by

- [`PropertySet.GetProperties`](#ApiClient.PropertySet.GetProperties "ApiClient.PropertySet.GetProperties")

- [`PropertySet.GetProperty`](#ApiClient.PropertySet.GetProperty "ApiClient.PropertySet.GetProperty")

Clone()[¶](#ApiClient.Property.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`Property`](#ApiClient.Property "ApiClient.Property")

GetDefaultValue()[¶](#ApiClient.Property.GetDefaultValue "Link to this definition")  
Returns the property’s default value.

Returns:  The default value

Return type:  str

See:  
[`Property.GetValueType()`](#ApiClient.Property.GetValueType "ApiClient.Property.GetValueType")

GetDisplayName()[¶](#ApiClient.Property.GetDisplayName "Link to this definition")  
Returns the display name of the property.

Returns:  The display name of the property

Return type:  str

GetDomain()[¶](#ApiClient.Property.GetDomain "Link to this definition")  
Returns the domain of allowed values of this property.

Returns:  List of valid values

Return type:  list[str]

GetName()[¶](#ApiClient.Property.GetName "Link to this definition")  
Returns the internal name of the property.

Returns:  The name of the property

Return type:  str

GetValue()[¶](#ApiClient.Property.GetValue "Link to this definition")  
Returns the used property value, which is either the configured value or the default value, in case the property is not set.

Returns:  The configured value of the property, or the default value if not set

Return type:  str

See:  
[`Property.GetValueType()`](#ApiClient.Property.GetValueType "ApiClient.Property.GetValueType")

GetValueType()[¶](#ApiClient.Property.GetValueType "Link to this definition")  
Returns the value type of this property.

Returns:  Value type of this property

Return type:  str

IsReadOnly()[¶](#ApiClient.Property.IsReadOnly "Link to this definition")  
Returns whether the property is read-only.

Returns:  Property is read-only?

Return type:  boolean

SetValue(*value*)[¶](#ApiClient.Property.SetValue "Link to this definition")  
Overwrites the value of this property.

Parameters:  **value** (*str*) – New value

See:  
[`GetDomain()`](#ApiClient.Property.GetDomain "ApiClient.Property.GetDomain")

Unset()[¶](#ApiClient.Property.Unset "Link to this definition")  
Specifies that the property is set to its default value.

## TestConfiguration[¶](#testconfiguration "Link to this heading")

*class* TestConfiguration[¶](#ApiClient.TestConfiguration "Link to this definition")  
Returned by

- [`ConfigurationApi.CreateTestConfiguration`](#ApiClient.ConfigurationApi.CreateTestConfiguration "ApiClient.ConfigurationApi.CreateTestConfiguration")

- [`ConfigurationApi.OpenTestConfiguration`](#ApiClient.ConfigurationApi.OpenTestConfiguration "ApiClient.ConfigurationApi.OpenTestConfiguration")

- [`ConfigurationApi.SearchTestConfigurations`](#ApiClient.ConfigurationApi.SearchTestConfigurations "ApiClient.ConfigurationApi.SearchTestConfigurations")

BusAccess[¶](#ApiClient.TestConfiguration.BusAccess "Link to this definition")  
Bus access configuration

Returns:  Bus access configuration

Return type:  [`BusAccess`](#ApiClient.BusAccess "ApiClient.BusAccess")

Common[¶](#ApiClient.TestConfiguration.Common "Link to this definition")  
Common configuration

Returns:  Common configuration

Return type:  [`Common`](#ApiClient.Common "ApiClient.Common")

ControlUnits[¶](#ApiClient.TestConfiguration.ControlUnits "Link to this definition")  
Control units configuration

Returns:  Control units configuration

Return type:  [`ControlUnits`](#ApiClient.ControlUnits "ApiClient.ControlUnits")

EnvironmentAccess[¶](#ApiClient.TestConfiguration.EnvironmentAccess "Link to this definition")  
Environment access configuration

Returns:  Environment access configuration

Return type:  [`Environment`](#ApiClient.Environment "ApiClient.Environment")

Execution[¶](#ApiClient.TestConfiguration.Execution "Link to this definition")  
Execution configuration

Returns:  Execution configuration

Return type:  [`Execution`](#ApiClient.Execution "ApiClient.Execution")

GlobalConstants[¶](#ApiClient.TestConfiguration.GlobalConstants "Link to this definition")  
Global constants configuration

Returns:  Global constants configuration

Return type:  [`GlobalConstants`](ComponentApi.md#ApiClient.GlobalConstants "ApiClient.GlobalConstants")

MediaAccess[¶](#ApiClient.TestConfiguration.MediaAccess "Link to this definition")  
Media access configuration

Returns:  Media access configuration

Return type:  [`MediaAccess`](#ApiClient.MediaAccess "ApiClient.MediaAccess")

Platform[¶](#ApiClient.TestConfiguration.Platform "Link to this definition")  
Platform configuration

Returns:  Platform configuration

Return type:  [`Platform`](#ApiClient.Platform "ApiClient.Platform")

Report[¶](#ApiClient.TestConfiguration.Report "Link to this definition")  
Report configuration

Returns:  Report configuration

Return type:  [`ReportData`](#ApiClient.ReportData "ApiClient.ReportData")

Clone()[¶](#ApiClient.TestConfiguration.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`TestConfiguration`](#ApiClient.TestConfiguration "ApiClient.TestConfiguration")

GetFilename()[¶](#ApiClient.TestConfiguration.GetFilename "Link to this definition")  
Returns the absolute path to the test configuration file. If empty, the file has not been saved yet.

Returns:  filename with extension

Return type:  str

Save(*filename=None*)[¶](#ApiClient.TestConfiguration.Save "Link to this definition")  
Saves the test configuration to a file. Appends file ending if needed.

Parameters:  **filename** (*str*) – The file name used for storing the test configuration file; Either absolute or relative to the ‘Configuration’ directory. Leave out to save the configuration to its existing file (previously set with [`Save()`](#ApiClient.TestConfiguration.Save "ApiClient.TestConfiguration.Save") or from [`ConfigurationApi.OpenTestConfiguration()`](#ApiClient.ConfigurationApi.OpenTestConfiguration "ApiClient.ConfigurationApi.OpenTestConfiguration"))

## BusAccess[¶](#busaccess "Link to this heading")

*class* BusAccess[¶](#ApiClient.BusAccess "Link to this definition")  
Returned by

- [`TestConfiguration.BusAccess`](#ApiClient.TestConfiguration.BusAccess "ApiClient.TestConfiguration.BusAccess")

Add(*busKey*)[¶](#ApiClient.BusAccess.Add "Link to this definition")  
Adds a bus to the bus access.

Parameters:  **busKey** (*str*) – Name of the bus

Returns:  The bus which was added

Return type:  [`Bus`](#ApiClient.Bus "ApiClient.Bus")

Clone()[¶](#ApiClient.BusAccess.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`BusAccess`](#ApiClient.BusAccess "ApiClient.BusAccess")

Delete(*busKey*)[¶](#ApiClient.BusAccess.Delete "Link to this definition")  
Deletes a bus from bus access.

Parameters:  **busKey** (*str*) – Name of bus to delete

Get(*busKey*)[¶](#ApiClient.BusAccess.Get "Link to this definition")  
Returns a bus object.

Parameters:  **busKey** (*str*) – Name of the bus

Returns:  The bus object

Return type:  [`Bus`](#ApiClient.Bus "ApiClient.Bus")

GetAll()[¶](#ApiClient.BusAccess.GetAll "Link to this definition")  
Returns a list of the names of all the accessed buses.

Returns:  List of names of all accessed buses

Return type:  list[str]

## Bus[¶](#bus "Link to this heading")

*class* Bus[¶](#ApiClient.Bus "Link to this definition")  
Returned by

- [`BusAccess.Add`](#ApiClient.BusAccess.Add "ApiClient.BusAccess.Add")

- [`BusAccess.Get`](#ApiClient.BusAccess.Get "ApiClient.BusAccess.Get")

Clone()[¶](#ApiClient.Bus.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`Bus`](#ApiClient.Bus "ApiClient.Bus")

GetAccessPort(*accessType*)[¶](#ApiClient.Bus.GetAccessPort "Link to this definition")  
Returns the bus port dependent on accessType.

Parameters:  **accessType** (*str*) – ‘AccessActiveNode’, ‘AccessManipulation’, ‘ServiceApplicationLayer’

Returns:  Bus port

Return type:  str

GetChannel()[¶](#ApiClient.Bus.GetChannel "Link to this definition")  
Returns the channel of the bus.

Returns:  Channel of the bus

Return type:  str

GetDatabaseArtifactReference()[¶](#ApiClient.Bus.GetDatabaseArtifactReference "Link to this definition")  
Returns the bus database artifact reference.

Returns:  The bus database artifact reference

Return type:  [`ArtifactReference`](ComponentApi.md#ApiClient.ArtifactReference "ApiClient.ArtifactReference")

GetDatabaseFile()[¶](#ApiClient.Bus.GetDatabaseFile "Link to this definition")  
Returns the bus database file.

Returns:  The bus database file

Return type:  str

GetName()[¶](#ApiClient.Bus.GetName "Link to this definition")  
Returns the name of the bus.

Returns:  Name of the bus

Return type:  str

GetProtocol()[¶](#ApiClient.Bus.GetProtocol "Link to this definition")  
Returns the protocol of the bus.

Returns:  Protocol

Return type:  str

Rename(*newBusKey*)[¶](#ApiClient.Bus.Rename "Link to this definition")  
Renames the bus.

Parameters:  **newBusKey** (*str*) – New name of the bus object

SetAccessPort(*accessType*, *accessPort*)[¶](#ApiClient.Bus.SetAccessPort "Link to this definition")  
Sets the bus port dependent on accessType.

Parameters:  - **accessType** (*str*) – ‘AccessActiveNode’, ‘AccessManipulation’, ‘ServiceApplicationLayer’

- **accessPort** (*str*) – Port to be set

SetChannel(*channel*)[¶](#ApiClient.Bus.SetChannel "Link to this definition")  
Sets the channel of the bus.

Parameters:  **channel** (*str*) – Channel of the bus

SetDatabaseArtifactReference(*busDbReference*)[¶](#ApiClient.Bus.SetDatabaseArtifactReference "Link to this definition")  
Sets the bus database artifact reference.

Parameters:  **busDbReference** ([`ArtifactReference`](ComponentApi.md#ApiClient.ArtifactReference "ApiClient.ArtifactReference")) – bus database artifact reference to be set

SetDatabaseFile(*database*)[¶](#ApiClient.Bus.SetDatabaseFile "Link to this definition")  
Sets the bus database file.

Parameters:  **database** (*str*) – The bus database file

SetProtocol(*protocol*)[¶](#ApiClient.Bus.SetProtocol "Link to this definition")  
Sets the protocol of the bus.

Parameters:  **protocol** (*str*) – Protocol to be set

## Common[¶](#common "Link to this heading")

*class* Common[¶](#ApiClient.Common "Link to this definition")  
Base class

[`MappingFiles`](ComponentApi.md#ApiClient.MappingFiles "ApiClient.MappingFiles")

Returned by

- [`TestConfiguration.Common`](#ApiClient.TestConfiguration.Common "ApiClient.TestConfiguration.Common")

AddMappingArtifactReference(*mappingReference*)[¶](#ApiClient.Common.AddMappingArtifactReference "Link to this definition")  
Adds an artifact reference to a mapping file to the list.

Parameters:  **mappingReference** ([`ArtifactReference`](ComponentApi.md#ApiClient.ArtifactReference "ApiClient.ArtifactReference")) – Artifact reference to a mapping file

AddMappingFile(*filename*)[¶](#ApiClient.Common.AddMappingFile "Link to this definition")  
Adds a mapping file to the list.

Parameters:  **filename** (*str*) – Name of the mapping file

ClearMappingFiles()[¶](#ApiClient.Common.ClearMappingFiles "Link to this definition")  
Clears all entries from the mapping file list.

Clone()[¶](#ApiClient.Common.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`Common`](#ApiClient.Common "ApiClient.Common")

GetMappingArtifactReferences()[¶](#ApiClient.Common.GetMappingArtifactReferences "Link to this definition")  
Returns artifact references to mapping files.

Returns:  A list of all artifact references

Return type:  list[[`ArtifactReference`](ComponentApi.md#ApiClient.ArtifactReference "ApiClient.ArtifactReference")]

GetTesterName()[¶](#ApiClient.Common.GetTesterName "Link to this definition")  
Returns the name of the tester.

Returns:  Name of tester to show in the test configuration file

Return type:  str

GetTesterNameQueryMode()[¶](#ApiClient.Common.GetTesterNameQueryMode "Link to this definition")  
Returns the query mode of the tester name.

Returns:  The query mode. Will be one of:

- ’direct input’

- ’query on tcf start’

- ’windows name’

- ’query on test run’

Return type:  str

IsAutoLoadMapping()[¶](#ApiClient.Common.IsAutoLoadMapping "Link to this definition")  
Returns whether mapping files are automatically loaded from model directories.

Returns:  True if mapping files are loaded automatically, else False

Return type:  boolean

RemoveMappingArtifactReference(*mappingReference*)[¶](#ApiClient.Common.RemoveMappingArtifactReference "Link to this definition")  
Removes an artifact reference to a mapping file from the list.

Parameters:  **mappingReference** ([`ArtifactReference`](ComponentApi.md#ApiClient.ArtifactReference "ApiClient.ArtifactReference")) – Artifact reference to a mapping file

RemoveMappingFile(*index*)[¶](#ApiClient.Common.RemoveMappingFile "Link to this definition")  
Removes a mapping file from the list.

Parameters:  **index** (*int*) – The index of the mapping file to remove

SetAutoLoadMapping(*value*)[¶](#ApiClient.Common.SetAutoLoadMapping "Link to this definition")  
Decides whether mapping files are automatically loaded from model directories.

Parameters:  **value** (*boolean*) – True if the mapping files have to be loaded automatically, else False

SetTesterName(*testerName*)[¶](#ApiClient.Common.SetTesterName "Link to this definition")  
Sets the name of the tester. Via API only direct input is possible.

Parameters:  **testerName** (*str*) – Name of tester to show in the test configuration file

SetTesterNameQueryMode(*mode*)[¶](#ApiClient.Common.SetTesterNameQueryMode "Link to this definition")  
Sets the query mode of the tester name. The mode must be one of:

> - ‘direct input’
>
> - ‘query on tcf start’
>
> - ‘windows name’
>
> - ‘query on test run’

Parameters:  **mode** (*str*) – The query mode.

Raises:  
**ApiError** – If the query mode is invalid.

GetMappingFiles()[¶](#ApiClient.Common.GetMappingFiles "Link to this definition")  
Returns the mapping file paths, relative to the workspace directory.

Returns:  A list of all mapping files

Return type:  list[str]

Deprecated since version 2024.2: Use [`GetMappingArtifactReferences()`](#ApiClient.Common.GetMappingArtifactReferences "ApiClient.Common.GetMappingArtifactReferences") instead

## ControlUnits[¶](#controlunits "Link to this heading")

*class* ControlUnits[¶](#ApiClient.ControlUnits "Link to this definition")  
Returned by

- [`TestConfiguration.ControlUnits`](#ApiClient.TestConfiguration.ControlUnits "ApiClient.TestConfiguration.ControlUnits")

Add(*controlUnitKey*)[¶](#ApiClient.ControlUnits.Add "Link to this definition")  
Adds a control unit.

Parameters:  **controlUnitKey** (*str*) – Name of the control unit

Returns:  The control unit which was added

Return type:  [`ControlUnit`](#ApiClient.ControlUnit "ApiClient.ControlUnit")

Clone()[¶](#ApiClient.ControlUnits.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`ControlUnits`](#ApiClient.ControlUnits "ApiClient.ControlUnits")

Delete(*controlUnitKey*)[¶](#ApiClient.ControlUnits.Delete "Link to this definition")  
Deletes a control unit.

Parameters:  **controlUnitKey** (*str*) – Name of control unit to delete

Get(*controlUnitKey*)[¶](#ApiClient.ControlUnits.Get "Link to this definition")  
Returns a control unit object.

Parameters:  **controlUnitKey** (*str*) – Name of the control unit

Returns:  The control unit object

Return type:  [`ControlUnit`](#ApiClient.ControlUnit "ApiClient.ControlUnit")

GetAll()[¶](#ApiClient.ControlUnits.GetAll "Link to this definition")  
Returns a list of the names of all the accessed control units.

Returns:  List of names of all accessed control units

Return type:  list[str]

## ControlUnit[¶](#controlunit "Link to this heading")

*class* ControlUnit[¶](#ApiClient.ControlUnit "Link to this definition")  
Returned by

- [`ControlUnits.Add`](#ApiClient.ControlUnits.Add "ApiClient.ControlUnits.Add")

- [`ControlUnits.Get`](#ApiClient.ControlUnits.Get "ApiClient.ControlUnits.Get")

DiagSettings[¶](#ApiClient.ControlUnit.DiagSettings "Link to this definition")  
Access to the diagnostics settings

Returns:  diagnostics settings

Return type:  [`DiagSettings`](#ApiClient.DiagSettings "ApiClient.DiagSettings")

Clone()[¶](#ApiClient.ControlUnit.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`ControlUnit`](#ApiClient.ControlUnit "ApiClient.ControlUnit")

GetApplicationA2lArtifactReference()[¶](#ApiClient.ControlUnit.GetApplicationA2lArtifactReference "Link to this definition")  
Gets the application port \*.a2l artifact reference.

Returns:  A2L file reference

Return type:  [`ArtifactReference`](ComponentApi.md#ApiClient.ArtifactReference "ApiClient.ArtifactReference")

GetApplicationA2lFile()[¶](#ApiClient.ControlUnit.GetApplicationA2lFile "Link to this definition")  
Returns the application port \*.a2l file path if a local file is referenced. Convenience method for GetApplicationA2lArtifactReference().GetPath() for local artifact references.

Returns:  A2L file

Return type:  str

GetApplicationHexArtifactReference()[¶](#ApiClient.ControlUnit.GetApplicationHexArtifactReference "Link to this definition")  
Gets the application port artifact reference to the hex file.

Returns:  Hex file reference

Return type:  [`ArtifactReference`](ComponentApi.md#ApiClient.ArtifactReference "ApiClient.ArtifactReference")

GetApplicationHexFile()[¶](#ApiClient.ControlUnit.GetApplicationHexFile "Link to this definition")  
Returns the application port hex file path if a local file is referenced. Convenience method for GetApplicationHexArtifactReference().GetPath() for local artifact references.

Returns:  hex file

Return type:  str

GetApplicationPort()[¶](#ApiClient.ControlUnit.GetApplicationPort "Link to this definition")  
Returns the application port.

Returns:  Application port

Return type:  str

GetConnectionSettings()[¶](#ApiClient.ControlUnit.GetConnectionSettings "Link to this definition")  
Get the connection settings that is currently listed in the TCF.

Returns:  remotePartyShortName

Return type:  str

GetDebuggingElfFile()[¶](#ApiClient.ControlUnit.GetDebuggingElfFile "Link to this definition")  
Returns the debugger \*.elf file. Raises an error if a file list with more than one element is set. Use GetDebuggingElfFiles in this case.

Returns:  Debugger \*.elf file

Return type:  str

Raises:  
**ApiError** – If a file list with more than one element is set

GetDebuggingElfFiles()[¶](#ApiClient.ControlUnit.GetDebuggingElfFiles "Link to this definition")  
Returns the debugger \*.elf files.

Returns:  Identifier and path of configured debugger \*.elf files

Return type:  dict[str, str]

GetDebuggingHexArtifactReference()[¶](#ApiClient.ControlUnit.GetDebuggingHexArtifactReference "Link to this definition")  
Gets the artifact reference to the debugger hex file.

Returns:  Debugger hex file reference

Return type:  [`ArtifactReference`](ComponentApi.md#ApiClient.ArtifactReference "ApiClient.ArtifactReference")

GetDebuggingHexFile()[¶](#ApiClient.ControlUnit.GetDebuggingHexFile "Link to this definition")  
Returns the debugger hex file path if a local file is referenced. Convenience method for GetDebuggingHexArtifactReference().GetPath() for local artifact references.

Returns:  Debugger hex file

Return type:  str

GetDebuggingPort()[¶](#ApiClient.ControlUnit.GetDebuggingPort "Link to this definition")  
Returns the debugger port.

Returns:  Debugger port

Return type:  str

GetDiagnosticDb()[¶](#ApiClient.ControlUnit.GetDiagnosticDb "Link to this definition")  
Returns the diagnostic database.

Returns:  Diagnostic database

Return type:  str

GetDiagnosticPort()[¶](#ApiClient.ControlUnit.GetDiagnosticPort "Link to this definition")  
Returns the diagnostic port.

Returns:  Diagnostic port

Return type:  str

GetDiagnosticsLogicalLink()[¶](#ApiClient.ControlUnit.GetDiagnosticsLogicalLink "Link to this definition")  
Returns the logical link file.

Returns:  Logical link file

Return type:  str

GetDiagnosticsPortDts()[¶](#ApiClient.ControlUnit.GetDiagnosticsPortDts "Link to this definition")  
Returns the DTS port.

Returns:  DTS port

Return type:  str

GetDiagnosticsPortEdiabas()[¶](#ApiClient.ControlUnit.GetDiagnosticsPortEdiabas "Link to this definition")  
Returns the EDIABAS diagnostics port.

Returns:  EDIABAS port

Return type:  str

GetDiagnosticsSgbdFile()[¶](#ApiClient.ControlUnit.GetDiagnosticsSgbdFile "Link to this definition")  
Returns the SGBD file.

Returns:  SGBD file

Return type:  str

GetEcuVariant()[¶](#ApiClient.ControlUnit.GetEcuVariant "Link to this definition")  
Get the ecu variant that is currently listed in the TCF.

Returns:  short name of the ecu variant

Return type:  str

GetEcuVariants()[¶](#ApiClient.ControlUnit.GetEcuVariants "Link to this definition")  
Returns list of all ecu variants from the given Diagnostics DB. Returns an empty list if the file is invalid or if there are no ecu variants.

Returns:  List of Variants (short name)

Return type:  list[str]

GetEdiabasCertificateFile()[¶](#ApiClient.ControlUnit.GetEdiabasCertificateFile "Link to this definition")  
Returns the certificate file for Ediabas.

Returns:  Certificate file

Return type:  str

GetLoggingDatabase()[¶](#ApiClient.ControlUnit.GetLoggingDatabase "Link to this definition")  
Returns the logging database.

The logging database is only used for the logging protocol ‘DLT (non-verbose)’.

Returns:  logging database

Return type:  str

GetLoggingDltFilterFile()[¶](#ApiClient.ControlUnit.GetLoggingDltFilterFile "Link to this definition")  
Returns the DLT filter file.

The DLT filter file is only used for the logging protocol ‘DLT (verbose)’.

Returns:  DLT filter file

Return type:  str

GetLoggingEcu()[¶](#ApiClient.ControlUnit.GetLoggingEcu "Link to this definition")  
Returns the logging ECU.

The logging ECU is only used for the logging protocol ‘DLT (non-verbose)’.

Returns:  logging ECU

Return type:  str

GetLoggingEthernetIp()[¶](#ApiClient.ControlUnit.GetLoggingEthernetIp "Link to this definition")  
Returns the Ethernet IP of the logging ECU.

Returns:  Ethernet-IP of the logging ECU

Return type:  str

GetLoggingEthernetPort()[¶](#ApiClient.ControlUnit.GetLoggingEthernetPort "Link to this definition")  
Returns the Ethernet port(s) of the logging ECU.

Returns:  Comma seperated Ethernet port(s) of the logging ECU

Return type:  str

GetLoggingEthernetProtocol()[¶](#ApiClient.ControlUnit.GetLoggingEthernetProtocol "Link to this definition")  
Returns the Ethernet protocol of the logging ECU.

Returns:  Ethernet protocol of the logging ECU

Return type:  str

GetLoggingPort()[¶](#ApiClient.ControlUnit.GetLoggingPort "Link to this definition")  
Returns the logging port.

Returns:  logging port

Return type:  str

GetLoggingProtocol()[¶](#ApiClient.ControlUnit.GetLoggingProtocol "Link to this definition")  
Returns the logging protocol.

Returns:  logging protocol: ‘DLT (non-verbose)’ or ‘DLT (verbose)’

Return type:  str

GetName()[¶](#ApiClient.ControlUnit.GetName "Link to this definition")  
Returns the name of the control unit.

Returns:  Name of the control unit

Return type:  str

GetRemotePartys()[¶](#ApiClient.ControlUnit.GetRemotePartys "Link to this definition")  
Returns list of remote partys from the given Diagnostics DB. Returns an empty list if the file is invalid or if there are no remote partys.

Returns:  List of Remote Partys (short name)

Return type:  list[str]

IsDebuggingUseHexFileFromApplication()[¶](#ApiClient.ControlUnit.IsDebuggingUseHexFileFromApplication "Link to this definition")  
Returns the option if the hex file is used from the application.

Returns:  Option to use hex file from application

Return type:  boolean

RemoveApplicationA2lArtifactReference()[¶](#ApiClient.ControlUnit.RemoveApplicationA2lArtifactReference "Link to this definition")  
Removes the application port \*.a2l file reference.

RemoveApplicationHexArtifactReference()[¶](#ApiClient.ControlUnit.RemoveApplicationHexArtifactReference "Link to this definition")  
Removes the application port hex file reference.

RemoveDebuggingHexArtifactReference()[¶](#ApiClient.ControlUnit.RemoveDebuggingHexArtifactReference "Link to this definition")  
Removes the debugger hex file reference.

Rename(*newControlUnitKey*)[¶](#ApiClient.ControlUnit.Rename "Link to this definition")  
Renames the control unit.

Parameters:  **newControlUnitKey** (*str*) – New name of the control unit

SetApplicationA2lArtifactReference(*a2lReference*)[¶](#ApiClient.ControlUnit.SetApplicationA2lArtifactReference "Link to this definition")  
Sets the application port \*.a2l file reference.

Parameters:  **a2lReference** ([`ArtifactReference`](ComponentApi.md#ApiClient.ArtifactReference "ApiClient.ArtifactReference")) – A2L file reference to be set

SetApplicationA2lFile(*a2lFile*)[¶](#ApiClient.ControlUnit.SetApplicationA2lFile "Link to this definition")  
Sets the application port \*.a2l file to the specified local file path. Convenience method for SetApplicationA2lArtifactReference() for local artifact references.

Parameters:  **a2lFile** (*str*) – A2L file to be set

SetApplicationHexArtifactReference(*hexReference*)[¶](#ApiClient.ControlUnit.SetApplicationHexArtifactReference "Link to this definition")  
Sets the application port hex file reference.

Parameters:  **hexReference** ([`ArtifactReference`](ComponentApi.md#ApiClient.ArtifactReference "ApiClient.ArtifactReference")) – Hex file reference to be set

SetApplicationHexFile(*hexFile*)[¶](#ApiClient.ControlUnit.SetApplicationHexFile "Link to this definition")  
Sets the application port hex file to the specified local file path. Convenience method for SetApplicationHexArtifactReference() for local artifact references.

Parameters:  **hexFile** (*str*) – Hex file to be set

SetApplicationPort(*applicationPort*)[¶](#ApiClient.ControlUnit.SetApplicationPort "Link to this definition")  
Sets the application port.

Parameters:  **applicationPort** (*str*) – Application port to be set

SetConnectionSettings(*remotePartyShortName*)[¶](#ApiClient.ControlUnit.SetConnectionSettings "Link to this definition")  
Set the connection settings by using the short name of a specific remote party. Use the GetRemotePartys() method to get a list of all remote partys from the diagnostics DB.

Parameters:  **remotePartyShortName** (*str*) – short name of the remote party

Returns:  True if success, else False

Return type:  bool

SetDebuggingElfFile(*debuggerElfFile*)[¶](#ApiClient.ControlUnit.SetDebuggingElfFile "Link to this definition")  
Sets the debugger \*.elf file. Overwrites an existing file or file list. The \*.elf file will be assigned to identifier “ELF-1”

Parameters:  **debuggerElfFile** (*str*) – Debugger \*.elf file to be set

SetDebuggingElfFiles(*debuggerElfFiles*)[¶](#ApiClient.ControlUnit.SetDebuggingElfFiles "Link to this definition")  
Sets the debugger \*.elf files. Overwrites an existing file or file list.

Parameters:  **debuggerElfFiles** (*dict[str,* *str]*) – Identifiers and pathes to debugger \*.elf files

SetDebuggingHexArtifactReference(*hexReference*)[¶](#ApiClient.ControlUnit.SetDebuggingHexArtifactReference "Link to this definition")  
Sets the debugger hex file reference.

Parameters:  **hexReference** ([`ArtifactReference`](ComponentApi.md#ApiClient.ArtifactReference "ApiClient.ArtifactReference")) – Hex file reference to be set

SetDebuggingHexFile(*debuggerHexFile*)[¶](#ApiClient.ControlUnit.SetDebuggingHexFile "Link to this definition")  
Sets the debugger hex file to the specified local file path. Convenience method for SetDebuggingHexArtifactReference() for local artifact references.

Parameters:  **debuggerHexFile** (*str*) – Debugger hex file to be set

SetDebuggingPort(*debuggerPort*)[¶](#ApiClient.ControlUnit.SetDebuggingPort "Link to this definition")  
Sets the debugger port.

Parameters:  **debuggerPort** (*str*) – Debugger port to be set

SetDebuggingUseHexFileFromApplication(*value*)[¶](#ApiClient.ControlUnit.SetDebuggingUseHexFileFromApplication "Link to this definition")  
Sets the option to use the hex file from the application.

Parameters:  **value** (*boolean*) – Option to use hex file from application

SetDiagnosticDb(*diagnosticDb*)[¶](#ApiClient.ControlUnit.SetDiagnosticDb "Link to this definition")  
Sets the diagnostic database.

Parameters:  **diagnosticDb** (*str*) – Diagnostic database to be set

SetDiagnosticPort(*diagnosticPort*)[¶](#ApiClient.ControlUnit.SetDiagnosticPort "Link to this definition")  
Sets the diagnostic port.

Parameters:  **diagnosticPort** (*str*) – Diagnostic port to be set

SetDiagnosticsLogicalLink(*logicalLinkFile*)[¶](#ApiClient.ControlUnit.SetDiagnosticsLogicalLink "Link to this definition")  
Sets the logical link file.

Parameters:  **logicalLinkFile** (*str*) – Logical link file to be set

SetDiagnosticsPortDts(*diagnosticsPortDts*)[¶](#ApiClient.ControlUnit.SetDiagnosticsPortDts "Link to this definition")  
Sets the DTS port.

Parameters:  **diagnosticsPortDts** (*str*) – DTS port to be set

SetDiagnosticsPortEdiabas(*diagnosticsPort*)[¶](#ApiClient.ControlUnit.SetDiagnosticsPortEdiabas "Link to this definition")  
Sets the EDIABAS diagnostics port.

Parameters:  **diagnosticsPort** (*str*) – Diagnostics port to be set

SetDiagnosticsSgbdFile(*sgbdFile*)[¶](#ApiClient.ControlUnit.SetDiagnosticsSgbdFile "Link to this definition")  
Sets the SGBD file.

Parameters:  **sgbdFile** (*str*) – SGBD file to be set

SetEcuVariant(*ecuVariant*)[¶](#ApiClient.ControlUnit.SetEcuVariant "Link to this definition")  
Set the ecu variant by using the short name of a specific ecu variant. Use the GetEcuVariants() method to get a list of all ecu variants from the diagnostics DB.

Parameters:  **ecuVariant** (*str*) – short name of the ecu variant

Returns:  True if success, else False

Return type:  bool

SetEdiabasCertificateFile(*certificate*)[¶](#ApiClient.ControlUnit.SetEdiabasCertificateFile "Link to this definition")  
Sets the certificate file for Ediabs.

Parameters:  **certificate** – Certificate file to be set. This must be the file name without the

suffix. :type certificate: str

SetLoggingDatabase(*loggingDatabase*)[¶](#ApiClient.ControlUnit.SetLoggingDatabase "Link to this definition")  
Sets the logging database.

The logging database is only used for the logging protocol ‘DLT (non-verbose)’.

Parameters:  **loggingDatabase** (*str*) – logging database

SetLoggingDltFilterFile(*loggingDltFilterFile*)[¶](#ApiClient.ControlUnit.SetLoggingDltFilterFile "Link to this definition")  
Sets the DLT filter file.

The DLT filter file is only used for the logging protocol ‘DLT (verbose)’.

Parameters:  **loggingDltFilterFile** (*str*) – DLT filter file

SetLoggingEcu(*loggingEcu*)[¶](#ApiClient.ControlUnit.SetLoggingEcu "Link to this definition")  
Sets the logging ECU.

The logging ECU is only used for the logging protocol ‘DLT (non-verbose)’.

Parameters:  **loggingEcu** (*str*) – logging ECU

SetLoggingEthernetIp(*loggingEthernetIp*)[¶](#ApiClient.ControlUnit.SetLoggingEthernetIp "Link to this definition")  
Sets the Ethernet IP of the logging ECU.

Parameters:  **loggingEthernetIp** (*str*) – Ethernet-IP of the logging ECU

SetLoggingEthernetPort(*loggingEthernetPort*)[¶](#ApiClient.ControlUnit.SetLoggingEthernetPort "Link to this definition")  
Sets the Ethernet port(s) of the logging ECU.

Parameters:  **loggingEthernetPort** (*str*) – Ethernet port(s) of the logging ECU. Multiple ports have to to be comma seperated.

SetLoggingEthernetProtocol(*loggingEthernetProtocol*)[¶](#ApiClient.ControlUnit.SetLoggingEthernetProtocol "Link to this definition")  
Sets the Ethernet protocol of the logging ECU.

Parameters:  **loggingEthernetProtocol** (*str*) – Ethernet protocol of the logging ECU

SetLoggingPort(*loggingPort*)[¶](#ApiClient.ControlUnit.SetLoggingPort "Link to this definition")  
Sets the logging port.

Parameters:  **loggingPort** (*str*) – logging port

SetLoggingProtocol(*loggingProtocol*)[¶](#ApiClient.ControlUnit.SetLoggingProtocol "Link to this definition")  
Sets the logging protocol.

Note: A change of the logging protocol will automatically set the logging database, logging ecu and dlt filter file to its default values.

Parameters:  **loggingProtocol** (*str*) – logging protocol: ‘DLT (non-verbose)’ or ‘DLT (verbose)’

## DiagSettings[¶](#diagsettings "Link to this heading")

*class* DiagSettings[¶](#ApiClient.DiagSettings "Link to this definition")  
Returned by

- [`ControlUnit.DiagSettings`](#ApiClient.ControlUnit.DiagSettings "ApiClient.ControlUnit.DiagSettings")

CanIsoTpSettings[¶](#ApiClient.DiagSettings.CanIsoTpSettings "Link to this definition")  
Access to the CAN ISO-TP settings

Returns:  ISO-TP settings

Return type:  [`CanIsoTpSettings`](#ApiClient.CanIsoTpSettings "ApiClient.CanIsoTpSettings")

DoIPSettings[¶](#ApiClient.DiagSettings.DoIPSettings "Link to this definition")  
Access to the DoIP settings

Returns:  DoIP settings

Return type:  [`DoIpSettings`](#ApiClient.DoIpSettings "ApiClient.DoIpSettings")

FrTpSettings[¶](#ApiClient.DiagSettings.FrTpSettings "Link to this definition")  
Access to the Flexray ISO-TP settings

Returns:  TP settings

Return type:  [`FrTpSettings`](#ApiClient.FrTpSettings "ApiClient.FrTpSettings")

UdsSettings[¶](#ApiClient.DiagSettings.UdsSettings "Link to this definition")  
Access to the UDS settings

Returns:  UDS/KWP2000 settings

Return type:  [`UdsSettings`](#ApiClient.UdsSettings "ApiClient.UdsSettings")

Clone()[¶](#ApiClient.DiagSettings.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`DiagSettings`](#ApiClient.DiagSettings "ApiClient.DiagSettings")

## CanIsoTpSettings[¶](#canisotpsettings "Link to this heading")

*class* CanIsoTpSettings[¶](#ApiClient.CanIsoTpSettings "Link to this definition")  
Returned by

- [`DiagSettings.CanIsoTpSettings`](#ApiClient.DiagSettings.CanIsoTpSettings "ApiClient.DiagSettings.CanIsoTpSettings")

Clone()[¶](#ApiClient.CanIsoTpSettings.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`CanIsoTpSettings`](#ApiClient.CanIsoTpSettings "ApiClient.CanIsoTpSettings")

GetAddressByte()[¶](#ApiClient.CanIsoTpSettings.GetAddressByte "Link to this definition")  
Returns the AddressByte.

> Here: Only the byte sequence in format “AA:BB:01”.

Network target address or address extension (only relevant for extended or mixed addressing) - ByteStream of length 1

> return:  
> AddressByte
>
> rtype:  
> str

GetAddressMode()[¶](#ApiClient.CanIsoTpSettings.GetAddressMode "Link to this definition")  
Returns the AddressMode.

Code of addressing mode - Integer (0: Standard Addressing | 1: Extended Addressing)

Returns:  AddressMode

Return type:  int

GetBlockSize()[¶](#ApiClient.CanIsoTpSettings.GetBlockSize "Link to this definition")  
Returns the BlockSize.

Number (0 - 255) of consecutive frames that can be received without an intermediate flow control - Integer

Returns:  BlockSize

Return type:  int

GetDiagTimeoutCanIsoTp()[¶](#ApiClient.CanIsoTpSettings.GetDiagTimeoutCanIsoTp "Link to this definition")  
Returns the DiagTimeoutCanIsoTp.

Timeout in milliseconds when waiting for responses on diagnostic requests via the ISO-TP protocol - Integer

Returns:  DiagTimeoutCanIsoTp

Return type:  int

GetFillByte()[¶](#ApiClient.CanIsoTpSettings.GetFillByte "Link to this definition")  
Returns the FillByte.

> Here: Only the byte sequence in format “AA:BB:01”.

Byte to fill messages (optional) - ByteStream of lenght 1

> return:  
> FillByte
>
> rtype:  
> str

GetFlowControlAddressByte()[¶](#ApiClient.CanIsoTpSettings.GetFlowControlAddressByte "Link to this definition")  
Returns the FlowControlAddressByte.

> Here: Only the byte sequence in format “AA:BB:01”.

Different network destination address or address extension for FlowControl (only relevant for extended and mixed addressing) - ByteStream of length 1

> return:  
> FlowControlAddressByte
>
> rtype:  
> str

GetFlowControlId()[¶](#ApiClient.CanIsoTpSettings.GetFlowControlId "Link to this definition")  
Returns the FlowControlId.

Message ID for flow control messages (optional) - Hex (optional Integer)

> return:  
> FlowControlId
>
> rtype:  
> int

GetIsExtended()[¶](#ApiClient.CanIsoTpSettings.GetIsExtended "Link to this definition")  
Returns the IsExtended.

Use Extended CAN-ID format? (1=yes / 29 Bits; 0=no / 11 Bits; -1 = Use setting from TBC)

Returns:  IsExtended

Return type:  int

GetIsExtendedFlowControlId()[¶](#ApiClient.CanIsoTpSettings.GetIsExtendedFlowControlId "Link to this definition")  
Returns the IsExtendedFlowControlId.

Use Extended CAN ID format (for FlowControlId)? (1=yes/29 bit; 0=no/11 bit;-1 = use same setting as IsExtended)

Returns:  IsExtendedFlowControlId

Return type:  int

GetIsExtendedRequestId()[¶](#ApiClient.CanIsoTpSettings.GetIsExtendedRequestId "Link to this definition")  
Returns the IsExtendedRequestId.

Use Extended CAN ID format (for RequestId)? (1=yes/29 bit; 0=no/11 bit;-1 = use same setting as IsExtended)

Returns:  IsExtendedRequestId

Return type:  int

GetIsExtendedResponseId()[¶](#ApiClient.CanIsoTpSettings.GetIsExtendedResponseId "Link to this definition")  
Returns the IsExtendedResponseId.

Use Extended CAN ID format (for ResponseId)? (1=yes/29 bit; 0=no/11 bit;-1 = use same setting as IsExtended)

Returns:  IsExtendedResponseId

Return type:  int

GetRequestId()[¶](#ApiClient.CanIsoTpSettings.GetRequestId "Link to this definition")  
Returns the RequestId.

Message ID for ECU requests - Hex (optional Integer)

> return:  
> RequestId
>
> rtype:  
> int

GetResponseId()[¶](#ApiClient.CanIsoTpSettings.GetResponseId "Link to this definition")  
Returns the ResponseId.

Message ID for ECU responses - Hex (optional Integer)

> return:  
> ResponseId
>
> rtype:  
> int

GetSeparationTime()[¶](#ApiClient.CanIsoTpSettings.GetSeparationTime "Link to this definition")  
Returns the SeparationTime.

Minimal time separation between successive fragments 0x00..0x7F =\> 0..127ms, 0x80..0xf0 =\> reserved, 0xf1..0xf9 =\> 100.900µs, 0xfa..0xff =\> reserved - Integer

Returns:  SeparationTime

Return type:  int

SetAddressByte(*value*)[¶](#ApiClient.CanIsoTpSettings.SetAddressByte "Link to this definition")  
Sets the AddressByte.

> Here: Only the byte sequence in format “AA:BB:01”.

Network target address or address extension (only relevant for extended or mixed addressing) - ByteStream of length 1

> param value:  
> AddressByte
>
> type value:  
> str

SetAddressMode(*value*)[¶](#ApiClient.CanIsoTpSettings.SetAddressMode "Link to this definition")  
Sets the AddressMode.

Code of addressing mode - Integer (0: Standard Addressing | 1: Extended Addressing)

Parameters:  **value** (*int*) – AddressMode

SetBlockSize(*value*)[¶](#ApiClient.CanIsoTpSettings.SetBlockSize "Link to this definition")  
Sets the BlockSize.

Number (0 - 255) of consecutive frames that can be received without an intermediate flow control - Integer

Parameters:  **value** (*int*) – BlockSize

SetDiagTimeoutCanIsoTp(*value*)[¶](#ApiClient.CanIsoTpSettings.SetDiagTimeoutCanIsoTp "Link to this definition")  
Sets the DiagTimeoutCanIsoTp.

Timeout in milliseconds when waiting for responses on diagnostic requests via the ISO-TP protocol - Integer

Parameters:  **value** (*int*) – DiagTimeoutCanIsoTp

SetFillByte(*value*)[¶](#ApiClient.CanIsoTpSettings.SetFillByte "Link to this definition")  
Sets the FillByte.

> Here: Only the byte sequence in format “AA:BB:01”.

Byte to fill messages (optional) - ByteStream of lenght 1

> param value:  
> FillByte
>
> type value:  
> str

SetFlowControlAddressByte(*value*)[¶](#ApiClient.CanIsoTpSettings.SetFlowControlAddressByte "Link to this definition")  
Sets the FlowControlAddressByte.

> Here: Only the byte sequence in format “AA:BB:01”.

Different network destination address or address extension for FlowControl (only relevant for extended and mixed addressing) - ByteStream of length 1

> param value:  
> FlowControlAddressByte
>
> type value:  
> str

SetFlowControlId(*value*)[¶](#ApiClient.CanIsoTpSettings.SetFlowControlId "Link to this definition")  
Sets the FlowControlId.

Message ID for flow control messages (optional) - Hex (optional Integer)

> param value:  
> FlowControlId
>
> type value:  
> int

SetIsExtended(*value*)[¶](#ApiClient.CanIsoTpSettings.SetIsExtended "Link to this definition")  
Sets the IsExtended.

Use Extended CAN-ID format? (1=yes / 29 Bits; 0=no / 11 Bits; -1 = Use setting from TBC)

Parameters:  **value** (*int*) – IsExtended

SetIsExtendedFlowControlId(*value*)[¶](#ApiClient.CanIsoTpSettings.SetIsExtendedFlowControlId "Link to this definition")  
Sets the IsExtendedFlowControlId.

Use Extended CAN ID format (for FlowControlId)? (1=yes/29 bit; 0=no/11 bit;-1 = use same setting as IsExtended)

Parameters:  **value** (*int*) – IsExtendedFlowControlId

SetIsExtendedRequestId(*value*)[¶](#ApiClient.CanIsoTpSettings.SetIsExtendedRequestId "Link to this definition")  
Sets the IsExtendedRequestId.

Use Extended CAN ID format (for RequestId)? (1=yes/29 bit; 0=no/11 bit;-1 = use same setting as IsExtended)

Parameters:  **value** (*int*) – IsExtendedRequestId

SetIsExtendedResponseId(*value*)[¶](#ApiClient.CanIsoTpSettings.SetIsExtendedResponseId "Link to this definition")  
Sets the IsExtendedResponseId.

Use Extended CAN ID format (for ResponseId)? (1=yes/29 bit; 0=no/11 bit;-1 = use same setting as IsExtended)

Parameters:  **value** (*int*) – IsExtendedResponseId

SetRequestId(*value*)[¶](#ApiClient.CanIsoTpSettings.SetRequestId "Link to this definition")  
Sets the RequestId.

Message ID for ECU requests - Hex (optional Integer)

> param value:  
> RequestId
>
> type value:  
> int

SetResponseId(*value*)[¶](#ApiClient.CanIsoTpSettings.SetResponseId "Link to this definition")  
Sets the ResponseId.

Message ID for ECU responses - Hex (optional Integer)

> param value:  
> ResponseId
>
> type value:  
> int

SetSeparationTime(*value*)[¶](#ApiClient.CanIsoTpSettings.SetSeparationTime "Link to this definition")  
Sets the SeparationTime.

Minimal time separation between successive fragments 0x00..0x7F =\> 0..127ms, 0x80..0xf0 =\> reserved, 0xf1..0xf9 =\> 100.900µs, 0xfa..0xff =\> reserved - Integer

Parameters:  **value** (*int*) – SeparationTime

## DoIpSettings[¶](#doipsettings "Link to this heading")

*class* DoIpSettings[¶](#ApiClient.DoIpSettings "Link to this definition")  
Returned by

- [`DiagSettings.DoIPSettings`](#ApiClient.DiagSettings.DoIPSettings "ApiClient.DiagSettings.DoIPSettings")

Clone()[¶](#ApiClient.DoIpSettings.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`DoIpSettings`](#ApiClient.DoIpSettings "ApiClient.DoIpSettings")

GetActivateRouting()[¶](#ApiClient.DoIpSettings.GetActivateRouting "Link to this definition")  
Returns the ActivateRouting.

Specifies whether the DoIP entity should forward diagnostic messages to an internal device.

Returns:  ActivateRouting

Return type:  bool

GetActivationType()[¶](#ApiClient.DoIpSettings.GetActivationType "Link to this definition")  
Returns the ActivationType.

> Here: Only the byte sequence in format “AA:BB:01”.

The type of routing activation if routing is to be activated. - ByteStream (e.g. 00 -> default, 01 -> WWH-OBD, E0 -> Central Security, further values can be taken from the standard)

> return:  
> ActivationType
>
> rtype:  
> str

GetDiagTimeoutDoIp()[¶](#ApiClient.DoIpSettings.GetDiagTimeoutDoIp "Link to this definition")  
Returns the DiagTimeoutDoIp.

Timeout in milliseconds when waiting for responses on diagnostic requests via the DoIP protocol - Integer

Returns:  DiagTimeoutDoIp

Return type:  int

GetDoIpVersion()[¶](#ApiClient.DoIpSettings.GetDoIpVersion "Link to this definition")  
Returns the DoIpVersion.

The version of the DoIP protocol used - Integer

Returns:  DoIpVersion

Return type:  int

GetEID()[¶](#ApiClient.DoIpSettings.GetEID "Link to this definition")  
Returns the EID.

> Here: Only the byte sequence in format “AA:BB:01”.

ID of the DoIP entity to which a connection is to be established. If specified, a vehicle identification request is sent to this ID to establish the connection. If not, a general vehicle identification request is sent and a connection is established to the first responding ECU. - ByteStream

> return:  
> EID
>
> rtype:  
> str

GetListenPort()[¶](#ApiClient.DoIpSettings.GetListenPort "Link to this definition")  
Returns the ListenPort.

The port on which to wait for responses from the DoIp entity. (Only relevant for UDP messages during connection setup, 0 -> the port is selected automatically) - Integer

Returns:  ListenPort

Return type:  int

GetRemotePort()[¶](#ApiClient.DoIpSettings.GetRemotePort "Link to this definition")  
Returns the RemotePort.

The port on which the DoIp Entity shall receive diagnostic messages - Integer

Returns:  RemotePort

Return type:  int

GetSourceAddress()[¶](#ApiClient.DoIpSettings.GetSourceAddress "Link to this definition")  
Returns the SourceAddress.

> Here: Only the byte sequence in format “AA:BB:01”.

The diagnostic address from which diagnostic messages are sent - ByteStream

> return:  
> SourceAddress
>
> rtype:  
> str

GetTargetAddress()[¶](#ApiClient.DoIpSettings.GetTargetAddress "Link to this definition")  
Returns the TargetAddress.

> Here: Only the byte sequence in format “AA:BB:01”.

The diagnostic address of the DoIP entity. If specified, no vehicle identification request is sent and UDS requests are sent directly to this address. - ByteStream

> return:  
> TargetAddress
>
> rtype:  
> str

GetTargetIp()[¶](#ApiClient.DoIpSettings.GetTargetIp "Link to this definition")  
Returns the TargetIp.

IP address of the DoIP entity - String

Returns:  TargetIp

Return type:  str

SetActivateRouting(*value*)[¶](#ApiClient.DoIpSettings.SetActivateRouting "Link to this definition")  
Sets the ActivateRouting.

Specifies whether the DoIP entity should forward diagnostic messages to an internal device.

Parameters:  **value** (*bool*) – ActivateRouting

SetActivationType(*value*)[¶](#ApiClient.DoIpSettings.SetActivationType "Link to this definition")  
Sets the ActivationType.

> Here: Only the byte sequence in format “AA:BB:01”.

The type of routing activation if routing is to be activated. - ByteStream (e.g. 00 -> default, 01 -> WWH-OBD, E0 -> Central Security, further values can be taken from the standard)

> param value:  
> ActivationType
>
> type value:  
> str

SetDiagTimeoutDoIp(*value*)[¶](#ApiClient.DoIpSettings.SetDiagTimeoutDoIp "Link to this definition")  
Sets the DiagTimeoutDoIp.

Timeout in milliseconds when waiting for responses on diagnostic requests via the DoIP protocol - Integer

Parameters:  **value** (*int*) – DiagTimeoutDoIp

SetDoIpVersion(*value*)[¶](#ApiClient.DoIpSettings.SetDoIpVersion "Link to this definition")  
Sets the DoIpVersion.

The version of the DoIP protocol used - Integer

Parameters:  **value** (*int*) – DoIpVersion

SetEID(*value*)[¶](#ApiClient.DoIpSettings.SetEID "Link to this definition")  
Sets the EID.

> Here: Only the byte sequence in format “AA:BB:01”.

ID of the DoIP entity to which a connection is to be established. If specified, a vehicle identification request is sent to this ID to establish the connection. If not, a general vehicle identification request is sent and a connection is established to the first responding ECU. - ByteStream

> param value:  
> EID
>
> type value:  
> str

SetListenPort(*value*)[¶](#ApiClient.DoIpSettings.SetListenPort "Link to this definition")  
Sets the ListenPort.

The port on which to wait for responses from the DoIp entity. (Only relevant for UDP messages during connection setup, 0 -> the port is selected automatically) - Integer

Parameters:  **value** (*int*) – ListenPort

SetRemotePort(*value*)[¶](#ApiClient.DoIpSettings.SetRemotePort "Link to this definition")  
Sets the RemotePort.

The port on which the DoIp Entity shall receive diagnostic messages - Integer

Parameters:  **value** (*int*) – RemotePort

SetSourceAddress(*value*)[¶](#ApiClient.DoIpSettings.SetSourceAddress "Link to this definition")  
Sets the SourceAddress.

> Here: Only the byte sequence in format “AA:BB:01”.

The diagnostic address from which diagnostic messages are sent - ByteStream

> param value:  
> SourceAddress
>
> type value:  
> str

SetTargetAddress(*value*)[¶](#ApiClient.DoIpSettings.SetTargetAddress "Link to this definition")  
Sets the TargetAddress.

> Here: Only the byte sequence in format “AA:BB:01”.

The diagnostic address of the DoIP entity. If specified, no vehicle identification request is sent and UDS requests are sent directly to this address. - ByteStream

> param value:  
> TargetAddress
>
> type value:  
> str

SetTargetIp(*value*)[¶](#ApiClient.DoIpSettings.SetTargetIp "Link to this definition")  
Sets the TargetIp.

IP address of the DoIP entity - String

Parameters:  **value** (*str*) – TargetIp

## FrTpSettings[¶](#frtpsettings "Link to this heading")

*class* FrTpSettings[¶](#ApiClient.FrTpSettings "Link to this definition")  
Returned by

- [`DiagSettings.FrTpSettings`](#ApiClient.DiagSettings.FrTpSettings "ApiClient.DiagSettings.FrTpSettings")

Clone()[¶](#ApiClient.FrTpSettings.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`FrTpSettings`](#ApiClient.FrTpSettings "ApiClient.FrTpSettings")

GetAcknowledged()[¶](#ApiClient.FrTpSettings.GetAcknowledged "Link to this definition")  
Returns the Acknowledged.

The acknowledge bit (C_CT communication type) signals whether the sender requires a confirmation of receipt (acknowledged, STFA) or not (unacknowledged, STFU). - Integer

Returns:  Acknowledged

Return type:  int

GetBlockSize()[¶](#ApiClient.FrTpSettings.GetBlockSize "Link to this definition")  
Returns the BlockSize.

Block size in bytes; maximum number of bytes that may be transmitted in the following consecutive frames before the sender has to wait for another flow control frame. - Integer

Returns:  BlockSize

Return type:  int

GetDiagTimeoutFrTp()[¶](#ApiClient.FrTpSettings.GetDiagTimeoutFrTp "Link to this definition")  
Returns the DiagTimeoutFrTp.

Timeout in milliseconds when waiting for responses on diagnostic requests via the FrTp protocol - Integer

Returns:  DiagTimeoutFrTp

Return type:  int

GetFillByte()[¶](#ApiClient.FrTpSettings.GetFillByte "Link to this definition")  
Returns the FillByte.

> Here: Only the byte sequence in format “AA:BB:01”.

Byte to fill messages (optional) - ByteStream of length 1

> return:  
> FillByte
>
> rtype:  
> str

GetFlowControlAddress()[¶](#ApiClient.FrTpSettings.GetFlowControlAddress "Link to this definition")  
Returns the FlowControlAddress.

Different address of the control unit (ECU) for FlowControl - Hex (optional Integer)

> return:  
> FlowControlAddress
>
> rtype:  
> int

GetMNPC()[¶](#ApiClient.FrTpSettings.GetMNPC "Link to this definition")  
Returns the MNPC.

MNPC specifies how many consecutive frames the receiver can process within one FlexRay cycle. With MNPC set to 0 the sender can utilize the maximum possible band width. - Integer

Returns:  MNPC

Return type:  int

GetRequestBaseCycle()[¶](#ApiClient.FrTpSettings.GetRequestBaseCycle "Link to this definition")  
Returns the RequestBaseCycle.

Cycle offset in the application cycle window - Integer \< RequestCycleRepetition

Returns:  RequestBaseCycle

Return type:  int

GetRequestCycleRepetition()[¶](#ApiClient.FrTpSettings.GetRequestCycleRepetition "Link to this definition")  
Returns the RequestCycleRepetition.

Cycle count after which the frame is sent periodically based on BaseCycle - Integer \>= 1

Returns:  RequestCycleRepetition

Return type:  int

GetRequestSlotId()[¶](#ApiClient.FrTpSettings.GetRequestSlotId "Link to this definition")  
Returns the RequestSlotId.

Frame-ID for requests sent to the ECU - 1 or 2 byte Hex (optional integer)

> return:  
> RequestSlotId
>
> rtype:  
> int

GetResponseBaseCycle()[¶](#ApiClient.FrTpSettings.GetResponseBaseCycle "Link to this definition")  
Returns the ResponseBaseCycle.

Cycle offset in the application cycle window - Integer \< ResponseCycleRepetition

Returns:  ResponseBaseCycle

Return type:  int

GetResponseCycleRepetition()[¶](#ApiClient.FrTpSettings.GetResponseCycleRepetition "Link to this definition")  
Returns the ResponseCycleRepetition.

Cycle count after which the frame is received periodically based on BaseCycle - Integer \>= 1

Returns:  ResponseCycleRepetition

Return type:  int

GetResponseSlotId()[¶](#ApiClient.FrTpSettings.GetResponseSlotId "Link to this definition")  
Returns the ResponseSlotId.

Frame-ID for ECU responses - 1 or 2 byte Hex (optional integer)

> return:  
> ResponseSlotId
>
> rtype:  
> int

GetSCexp()[¶](#ApiClient.FrTpSettings.GetSCexp "Link to this definition")  
Returns the SCexp.

SC defines the minimum distance in cycles until the sender is allowed to send the next consecutive frame. SC = 2^SCexp - 1 - Integer

Returns:  SCexp

Return type:  int

GetSourceAddress()[¶](#ApiClient.FrTpSettings.GetSourceAddress "Link to this definition")  
Returns the SourceAddress.

Address of the tester (ecu.test) - Hex (optional integer)

> return:  
> SourceAddress
>
> rtype:  
> int

GetTargetAddress()[¶](#ApiClient.FrTpSettings.GetTargetAddress "Link to this definition")  
Returns the TargetAddress.

Address of the ECU - Hex (optional integer)

> return:  
> TargetAddress
>
> rtype:  
> int

SetAcknowledged(*value*)[¶](#ApiClient.FrTpSettings.SetAcknowledged "Link to this definition")  
Sets the Acknowledged.

The acknowledge bit (C_CT communication type) signals whether the sender requires a confirmation of receipt (acknowledged, STFA) or not (unacknowledged, STFU). - Integer

Parameters:  **value** (*int*) – Acknowledged

SetBlockSize(*value*)[¶](#ApiClient.FrTpSettings.SetBlockSize "Link to this definition")  
Sets the BlockSize.

Block size in bytes; maximum number of bytes that may be transmitted in the following consecutive frames before the sender has to wait for another flow control frame. - Integer

Parameters:  **value** (*int*) – BlockSize

SetDiagTimeoutFrTp(*value*)[¶](#ApiClient.FrTpSettings.SetDiagTimeoutFrTp "Link to this definition")  
Sets the DiagTimeoutFrTp.

Timeout in milliseconds when waiting for responses on diagnostic requests via the FrTp protocol - Integer

Parameters:  **value** (*int*) – DiagTimeoutFrTp

SetFillByte(*value*)[¶](#ApiClient.FrTpSettings.SetFillByte "Link to this definition")  
Sets the FillByte.

> Here: Only the byte sequence in format “AA:BB:01”.

Byte to fill messages (optional) - ByteStream of length 1

> param value:  
> FillByte
>
> type value:  
> str

SetFlowControlAddress(*value*)[¶](#ApiClient.FrTpSettings.SetFlowControlAddress "Link to this definition")  
Sets the FlowControlAddress.

Different address of the control unit (ECU) for FlowControl - Hex (optional Integer)

> param value:  
> FlowControlAddress
>
> type value:  
> int

SetMNPC(*value*)[¶](#ApiClient.FrTpSettings.SetMNPC "Link to this definition")  
Sets the MNPC.

MNPC specifies how many consecutive frames the receiver can process within one FlexRay cycle. With MNPC set to 0 the sender can utilize the maximum possible band width. - Integer

Parameters:  **value** (*int*) – MNPC

SetRequestBaseCycle(*value*)[¶](#ApiClient.FrTpSettings.SetRequestBaseCycle "Link to this definition")  
Sets the RequestBaseCycle.

Cycle offset in the application cycle window - Integer \< RequestCycleRepetition

Parameters:  **value** (*int*) – RequestBaseCycle

SetRequestCycleRepetition(*value*)[¶](#ApiClient.FrTpSettings.SetRequestCycleRepetition "Link to this definition")  
Sets the RequestCycleRepetition.

Cycle count after which the frame is sent periodically based on BaseCycle - Integer \>= 1

Parameters:  **value** (*int*) – RequestCycleRepetition

SetRequestSlotId(*value*)[¶](#ApiClient.FrTpSettings.SetRequestSlotId "Link to this definition")  
Sets the RequestSlotId.

Frame-ID for requests sent to the ECU - 1 or 2 byte Hex (optional integer)

> param value:  
> RequestSlotId
>
> type value:  
> int

SetResponseBaseCycle(*value*)[¶](#ApiClient.FrTpSettings.SetResponseBaseCycle "Link to this definition")  
Sets the ResponseBaseCycle.

Cycle offset in the application cycle window - Integer \< ResponseCycleRepetition

Parameters:  **value** (*int*) – ResponseBaseCycle

SetResponseCycleRepetition(*value*)[¶](#ApiClient.FrTpSettings.SetResponseCycleRepetition "Link to this definition")  
Sets the ResponseCycleRepetition.

Cycle count after which the frame is received periodically based on BaseCycle - Integer \>= 1

Parameters:  **value** (*int*) – ResponseCycleRepetition

SetResponseSlotId(*value*)[¶](#ApiClient.FrTpSettings.SetResponseSlotId "Link to this definition")  
Sets the ResponseSlotId.

Frame-ID for ECU responses - 1 or 2 byte Hex (optional integer)

> param value:  
> ResponseSlotId
>
> type value:  
> int

SetSCexp(*value*)[¶](#ApiClient.FrTpSettings.SetSCexp "Link to this definition")  
Sets the SCexp.

SC defines the minimum distance in cycles until the sender is allowed to send the next consecutive frame. SC = 2^SCexp - 1 - Integer

Parameters:  **value** (*int*) – SCexp

SetSourceAddress(*value*)[¶](#ApiClient.FrTpSettings.SetSourceAddress "Link to this definition")  
Sets the SourceAddress.

Address of the tester (ecu.test) - Hex (optional integer)

> param value:  
> SourceAddress
>
> type value:  
> int

SetTargetAddress(*value*)[¶](#ApiClient.FrTpSettings.SetTargetAddress "Link to this definition")  
Sets the TargetAddress.

Address of the ECU - Hex (optional integer)

> param value:  
> TargetAddress
>
> type value:  
> int

## UdsSettings[¶](#udssettings "Link to this heading")

*class* UdsSettings[¶](#ApiClient.UdsSettings "Link to this definition")  
Returned by

- [`DiagSettings.UdsSettings`](#ApiClient.DiagSettings.UdsSettings "ApiClient.DiagSettings.UdsSettings")

Clone()[¶](#ApiClient.UdsSettings.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`UdsSettings`](#ApiClient.UdsSettings "ApiClient.UdsSettings")

GetAutostart()[¶](#ApiClient.UdsSettings.GetAutostart "Link to this definition")  
Returns the Autostart.

Automatically start the diagnostic session at the beginning of the test case. Use the job OpenTCFDiagSession to start the session if this option is not checked.

Returns:  Autostart

Return type:  bool

GetStartRequest()[¶](#ApiClient.UdsSettings.GetStartRequest "Link to this definition")  
Returns the StartRequest.

> Here: Only the byte sequence in format “AA:BB:01”.

Diagnostic request to open a session (optional) - ByteStream

> return:  
> StartRequest
>
> rtype:  
> str

GetStopRequest()[¶](#ApiClient.UdsSettings.GetStopRequest "Link to this definition")  
Returns the StopRequest.

> Here: Only the byte sequence in format “AA:BB:01”.

Diagnostic request to end a session (optional) - ByteStream

> return:  
> StopRequest
>
> rtype:  
> str

GetTesterPresentCycleTime()[¶](#ApiClient.UdsSettings.GetTesterPresentCycleTime "Link to this definition")  
Returns the TesterPresentCycleTime.

Period length (ms) for cyclic tester-available signaling (optional) - Integer

Returns:  TesterPresentCycleTime

Return type:  int

GetTesterPresentRequest()[¶](#ApiClient.UdsSettings.GetTesterPresentRequest "Link to this definition")  
Returns the TesterPresentRequest.

> Here: Only the byte sequence in format “AA:BB:01”.

Diagnostic request for periodic tester-available signaling (optional) - ByteStream

> return:  
> TesterPresentRequest
>
> rtype:  
> str

SetAutostart(*value*)[¶](#ApiClient.UdsSettings.SetAutostart "Link to this definition")  
Sets the Autostart.

Automatically start the diagnostic session at the beginning of the test case. Use the job OpenTCFDiagSession to start the session if this option is not checked.

Parameters:  **value** (*bool*) – Autostart

SetStartRequest(*value*)[¶](#ApiClient.UdsSettings.SetStartRequest "Link to this definition")  
Sets the StartRequest.

> Here: Only the byte sequence in format “AA:BB:01”.

Diagnostic request to open a session (optional) - ByteStream

> param value:  
> StartRequest
>
> type value:  
> str

SetStopRequest(*value*)[¶](#ApiClient.UdsSettings.SetStopRequest "Link to this definition")  
Sets the StopRequest.

> Here: Only the byte sequence in format “AA:BB:01”.

Diagnostic request to end a session (optional) - ByteStream

> param value:  
> StopRequest
>
> type value:  
> str

SetTesterPresentCycleTime(*value*)[¶](#ApiClient.UdsSettings.SetTesterPresentCycleTime "Link to this definition")  
Sets the TesterPresentCycleTime.

Period length (ms) for cyclic tester-available signaling (optional) - Integer

Parameters:  **value** (*int*) – TesterPresentCycleTime

SetTesterPresentRequest(*value*)[¶](#ApiClient.UdsSettings.SetTesterPresentRequest "Link to this definition")  
Sets the TesterPresentRequest.

> Here: Only the byte sequence in format “AA:BB:01”.

Diagnostic request for periodic tester-available signaling (optional) - ByteStream

> param value:  
> TesterPresentRequest
>
> type value:  
> str

## Environment[¶](#environment "Link to this heading")

*class* Environment[¶](#ApiClient.Environment "Link to this definition")  
Returned by

- [`TestConfiguration.EnvironmentAccess`](#ApiClient.TestConfiguration.EnvironmentAccess "ApiClient.TestConfiguration.EnvironmentAccess")

EnvironmentCommunicationAccess[¶](#ApiClient.Environment.EnvironmentCommunicationAccess "Link to this definition")  
Environment communication access

Returns:  Environment communication access

Return type:  [`EnvComAccess`](#ApiClient.EnvComAccess "ApiClient.EnvComAccess")

EnvironmentSimulationAccess[¶](#ApiClient.Environment.EnvironmentSimulationAccess "Link to this definition")  
Environment simulation access

Returns:  Environment simulation access

Return type:  [`EnvSimAccess`](#ApiClient.EnvSimAccess "ApiClient.EnvSimAccess")

Clone()[¶](#ApiClient.Environment.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`Environment`](#ApiClient.Environment "ApiClient.Environment")

## EnvComAccess[¶](#envcomaccess "Link to this heading")

*class* EnvComAccess[¶](#ApiClient.EnvComAccess "Link to this definition")  
Returned by

- [`Environment.EnvironmentCommunicationAccess`](#ApiClient.Environment.EnvironmentCommunicationAccess "ApiClient.Environment.EnvironmentCommunicationAccess")

Add(*environmentCommunicationKey*)[¶](#ApiClient.EnvComAccess.Add "Link to this definition")  
Adds an environment communication system

Parameters:  **environmentCommunicationKey** (*str*) – Name of the environment communication system to add

Returns:  The environment communication system which was added

Return type:  [`EnvComData`](#ApiClient.EnvComData "ApiClient.EnvComData")

Clone()[¶](#ApiClient.EnvComAccess.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`EnvComAccess`](#ApiClient.EnvComAccess "ApiClient.EnvComAccess")

Delete(*environmentCommunicationKey*)[¶](#ApiClient.EnvComAccess.Delete "Link to this definition")  
Deletes an enviroment communication system from enviroment communication access.

Parameters:  **environmentCommunicationKey** (*str*) – Name of environment simulation to delete

Get(*environmentCommunicationKey*)[¶](#ApiClient.EnvComAccess.Get "Link to this definition")  
Retrieves an environment communication object.

Parameters:  **environmentCommunicationKey** (*str*) – Name of the environment communication

Returns:  The environment communication object

Return type:  [`EnvComData`](#ApiClient.EnvComData "ApiClient.EnvComData")

GetAll()[¶](#ApiClient.EnvComAccess.GetAll "Link to this definition")  
Returns a list of the names of all the accessed environment communication systems.

Returns:  list of names of all accessed environment communication systems

Return type:  list[str]

## EnvComData[¶](#envcomdata "Link to this heading")

*class* EnvComData[¶](#ApiClient.EnvComData "Link to this definition")  
Returned by

- [`EnvComAccess.Add`](#ApiClient.EnvComAccess.Add "ApiClient.EnvComAccess.Add")

- [`EnvComAccess.Get`](#ApiClient.EnvComAccess.Get "ApiClient.EnvComAccess.Get")

Clone()[¶](#ApiClient.EnvComData.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`EnvComData`](#ApiClient.EnvComData "ApiClient.EnvComData")

GetName()[¶](#ApiClient.EnvComData.GetName "Link to this definition")  
Returns the name of the environment communication system.

Returns:  Name of the environment communication system

Return type:  str

Rename(*newEnvironmentCommunicationKey*)[¶](#ApiClient.EnvComData.Rename "Link to this definition")  
Renames the model.

Parameters:  **newEnvironmentCommunicationKey** (*str*) – New name of the environment communication system

## EnvSimAccess[¶](#envsimaccess "Link to this heading")

*class* EnvSimAccess[¶](#ApiClient.EnvSimAccess "Link to this definition")  
Returned by

- [`Environment.EnvironmentSimulationAccess`](#ApiClient.Environment.EnvironmentSimulationAccess "ApiClient.Environment.EnvironmentSimulationAccess")

Add(*environmentSimulationKey*)[¶](#ApiClient.EnvSimAccess.Add "Link to this definition")  
Adds a environment simulation

Parameters:  **environmentSimulationKey** (*str*) – Name of the environment simulation to add

Returns:  The environment simulation which was added

Return type:  [`EnvSimData`](#ApiClient.EnvSimData "ApiClient.EnvSimData")

Clone()[¶](#ApiClient.EnvSimAccess.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`EnvSimAccess`](#ApiClient.EnvSimAccess "ApiClient.EnvSimAccess")

Delete(*enviromentalSimulationKey*)[¶](#ApiClient.EnvSimAccess.Delete "Link to this definition")  
Deletes a enviromental simulation from enviromental simulation access.

Parameters:  **enviromentalSimulationKey** (*str*) – Name of envriomental simulation to delete

Get(*environmentSimulationKey*)[¶](#ApiClient.EnvSimAccess.Get "Link to this definition")  
Retrieves a environment simulation object.

Parameters:  **environmentSimulationKey** (*str*) – Name of the environment simulation

Returns:  The environment simulations object

Return type:  [`EnvSimData`](#ApiClient.EnvSimData "ApiClient.EnvSimData")

GetAll()[¶](#ApiClient.EnvSimAccess.GetAll "Link to this definition")  
Returns a list of the names of all the accessed environment simulations.

Returns:  list of names of all accessed environment simulations

Return type:  list[str]

## EnvSimData[¶](#envsimdata "Link to this heading")

*class* EnvSimData[¶](#ApiClient.EnvSimData "Link to this definition")  
Returned by

- [`EnvSimAccess.Add`](#ApiClient.EnvSimAccess.Add "ApiClient.EnvSimAccess.Add")

- [`EnvSimAccess.Get`](#ApiClient.EnvSimAccess.Get "ApiClient.EnvSimAccess.Get")

Clone()[¶](#ApiClient.EnvSimData.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`EnvSimData`](#ApiClient.EnvSimData "ApiClient.EnvSimData")

GetDataSource()[¶](#ApiClient.EnvSimData.GetDataSource "Link to this definition")  
Returns the data source.

Returns:  data source: 0 online query, 1 offline file

Return type:  int

GetName()[¶](#ApiClient.EnvSimData.GetName "Link to this definition")  
Returns the name of the enviroment simulation.

Returns:  Name of the environment simulation

Return type:  str

GetOfflineFile()[¶](#ApiClient.EnvSimData.GetOfflineFile "Link to this definition")  
Returns the offline file.

Returns:  offline file

Return type:  str

GetPort()[¶](#ApiClient.EnvSimData.GetPort "Link to this definition")  
Returns the enviroment simulation port.

Returns:  environment simulation port

Return type:  str

Rename(*newEnvironmentSimulationKey*)[¶](#ApiClient.EnvSimData.Rename "Link to this definition")  
Renames the model.

Parameters:  **newEnvironmentSimulationKey** (*str*) – New name of the environment simulation

SetDataSource(*dataSource*)[¶](#ApiClient.EnvSimData.SetDataSource "Link to this definition")  
Set the data source to switch between online query and offline file.

Parameters:  **dataSource** (*int*) – data source: 0 online query, 1 offline file

SetOfflineFile(*offlineFile*)[¶](#ApiClient.EnvSimData.SetOfflineFile "Link to this definition")  
Sets the offline file.

Parameters:  **offlineFile** (*str*) – offline file to be set

SetPort(*port*)[¶](#ApiClient.EnvSimData.SetPort "Link to this definition")  
Sets the enviroment simulation port.

Parameters:  **port** (*str*) – environment simulation port to be set

## Execution[¶](#execution "Link to this heading")

*class* Execution[¶](#ApiClient.Execution "Link to this definition")  
Returned by

- [`TestConfiguration.Execution`](#ApiClient.TestConfiguration.Execution "ApiClient.TestConfiguration.Execution")

Clone()[¶](#ApiClient.Execution.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`Execution`](#ApiClient.Execution "ApiClient.Execution")

DisableDefaultRecordingPackage()[¶](#ApiClient.Execution.DisableDefaultRecordingPackage "Link to this definition")  
Disables the default recording configuration.

DisableErrorRecoveryPkg()[¶](#ApiClient.Execution.DisableErrorRecoveryPkg "Link to this definition")  
Sets that no package shall be executed on FAILED/ERROR/abort.

DisableGlobalPostconditionPkg()[¶](#ApiClient.Execution.DisableGlobalPostconditionPkg "Link to this definition")  
Disables the global postcondition package.

DisableGlobalPreconditionPkg()[¶](#ApiClient.Execution.DisableGlobalPreconditionPkg "Link to this definition")  
Disables the global precondition package.

EnableDefaultRecordingPackage(*packagePath*)[¶](#ApiClient.Execution.EnableDefaultRecordingPackage "Link to this definition")  
Sets the package whose recording configuration will be used as default.

Parameters:  **packagePath** (*str*) – Path to package.

EnableGlobalPostconditionPkg(*packagePath*)[¶](#ApiClient.Execution.EnableGlobalPostconditionPkg "Link to this definition")  
Sets the package that shall be executed as postcondition for every executed package.

Parameters:  **packagePath** (*str*) – Path to postcondition-package.

EnableGlobalPreconditionPkg(*packagePath*)[¶](#ApiClient.Execution.EnableGlobalPreconditionPkg "Link to this definition")  
Sets the package that shall be executed as precondition for every executed package.

Parameters:  **packagePath** (*str*) – Path to precondition-package.

GetDefaultRecordingPackage()[¶](#ApiClient.Execution.GetDefaultRecordingPackage "Link to this definition")  
Gets the package whose recording configuration will be used as default.

Returns:  Path to package

Return type:  str

GetErrorRecoveryPkg()[¶](#ApiClient.Execution.GetErrorRecoveryPkg "Link to this definition")  
Gets the package that will be executed on FAILED/ERROR/Abort.

Returns:  Path to package.

Return type:  str

GetErrorRecoveryPkgLevel()[¶](#ApiClient.Execution.GetErrorRecoveryPkgLevel "Link to this definition")  
Gets the conditions under which the error recovery package will be executed

Returns:  0 = on abort only; 1 = on ERROR and on abort; 2 = on FAILED, ERROR and abort.

Return type:  int

GetExecutionBehaviorOnError()[¶](#ApiClient.Execution.GetExecutionBehaviorOnError "Link to this definition")  
Gets the behavior if an error occurs during package execution.

Returns:  “Continue” or “Abort”

Return type:  str

GetGlobalPostconditionPkg()[¶](#ApiClient.Execution.GetGlobalPostconditionPkg "Link to this definition")  
Gets the package that will be executed as postcondition for every executed package.

Returns:  Path to postcondition-package.

Return type:  str

GetGlobalPreconditionPkg()[¶](#ApiClient.Execution.GetGlobalPreconditionPkg "Link to this definition")  
Gets the package that will be executed as precondition for every executed package.

Returns:  Path to precondition-package.

Return type:  str

GetGlobalRetry()[¶](#ApiClient.Execution.GetGlobalRetry "Link to this definition")  
Returns the state of the global retry.

Returns:  Whether or not the global retry is activated

Return type:  boolean

GetGlobalRetryCondition()[¶](#ApiClient.Execution.GetGlobalRetryCondition "Link to this definition")  
Returns the condition of the global retries. Returns one of the following:

-‘ERROR’ -‘FAILED’ -‘ERROR/FAILED’

Returns:  The condition of the global retry

Return type:  str

GetGlobalRetryCount()[¶](#ApiClient.Execution.GetGlobalRetryCount "Link to this definition")  
Returns the number of the global retries.

Returns:  Number of the global retries

Return type:  integer

GetRestoreAfterUserConfirmation()[¶](#ApiClient.Execution.GetRestoreAfterUserConfirmation "Link to this definition")  
Gets the state of restoring test quantities after user confirmation.

Returns:  State of restoring test quantities after user confirmation.

Return type:  bool

GetRestoreTestQuantitiesMode()[¶](#ApiClient.Execution.GetRestoreTestQuantitiesMode "Link to this definition")  
Returns the mode with which the test quantities will be restored after test execution.

Returns:  The restore mode. Possible values are “NEVER”, “ALWAYS”, “PORTS”

Return type:  str

GetRestoreTestQuantitiesPorts()[¶](#ApiClient.Execution.GetRestoreTestQuantitiesPorts "Link to this definition")  
Returns the ports whose test quantities will be restored after test execution if the restoration mode is set to “PORTS”. Use `SetRestoreTestQuantitiesMode()` to configure the restoration mode.

Returns:  The list of ports whose test quantities will be restored after test execution.

Return type:  list[str]

GetSimulationMode()[¶](#ApiClient.Execution.GetSimulationMode "Link to this definition")  
Returns the simulation mode to be used when the configuration is started. The simulation mode might either be ‘AUTO’, ‘STEPWISE’ or ‘CONTINUOUS’.

Returns:  The simulation mode

Return type:  str

GetTimeSource()[¶](#ApiClient.Execution.GetTimeSource "Link to this definition")  
Returns the configured value for the time source to be used when the configuration is started. The time source might either be ‘AUTO’, ‘REALTIME’ or a port name.

Returns:  The time source

Return type:  str

GetWaitTimeAfterIOTeststep()[¶](#ApiClient.Execution.GetWaitTimeAfterIOTeststep "Link to this definition")  
Gets the wait time after every every I/O test step in ms.

Returns:  Wait time in ms

Return type:  float

SetErrorRecoveryPkg(*pkg*)[¶](#ApiClient.Execution.SetErrorRecoveryPkg "Link to this definition")  
Sets the package that shall be executed on FAILED/ERROR/abort. See also `SetErrorRecoveryPkgLevel()`

Parameters:  **pkg** (*str*) – Path to package

SetErrorRecoveryPkgLevel(*level*)[¶](#ApiClient.Execution.SetErrorRecoveryPkgLevel "Link to this definition")  
Sets the conditions under which the error recovery package will be executed

Parameters:  **level** (*int*) –

- 0 = on abort only

- 1 = on ERROR and on abort

- 2 = on FAILED, ERROR and abort.

SetExecutionBehaviorOnError(*errorHandling*)[¶](#ApiClient.Execution.SetExecutionBehaviorOnError "Link to this definition")  
Sets the behavior if an error occurs during package execution.

Parameters:  **errorHandling** (*str*) – “Continue” or “Abort”

SetGlobalRetry(*globalRetry*)[¶](#ApiClient.Execution.SetGlobalRetry "Link to this definition")  
Sets the state of the global retry.

Parameters:  **globalRetry** (*boolean*) – Whether or not the global retry is activated

SetGlobalRetryCondition(*condition*)[¶](#ApiClient.Execution.SetGlobalRetryCondition "Link to this definition")  
Sets the condition of the global retry. Must be one of the following:

- ‘SUCCESS’

- ‘INCONCLUSIVE’

- ‘ERROR’

- ‘FAILED’

- ‘ERROR/FAILED’

Parameters:  **condition** (*str*) – The condition of the global retry

SetGlobalRetryCount(*count*)[¶](#ApiClient.Execution.SetGlobalRetryCount "Link to this definition")  
Sets the number of the global retries.

Parameters:  **count** (*integer*) – Number of the global retries

SetRestoreAfterUserConfirmation(*confirmationState*)[¶](#ApiClient.Execution.SetRestoreAfterUserConfirmation "Link to this definition")  
Enable or disable the option to restore test quantities only after user confirmation. The state of “RestoreTestQuantitiesMode” will be automatically set to “ALWAYS” if it was set to “NEVER” before calling this method.

Parameters:  **confirmationState** (*bool*) – State of restoring test quantities after user confirmation.

SetRestoreTestQuantitiesMode(*mode*)[¶](#ApiClient.Execution.SetRestoreTestQuantitiesMode "Link to this definition")  
Sets the mode with which the test quantities will be restored after test execution. With the modes “ALWAYS” and “NEVER” the automatic restoration can be turned on or off for all test quantities. With the mode “PORTS” only test quantities of specific ports will be restored. Use `SetRestoreTestQuantitiesPorts()` to configure the ports whose test quantities should be reset.

Parameters:  **mode** (*str*) – The mode for restoring test quantities. Possible values: “NEVER”, “ALWAYS”, “PORTS”

SetRestoreTestQuantitiesPorts(*ports*)[¶](#ApiClient.Execution.SetRestoreTestQuantitiesPorts "Link to this definition")  
Sets the list of ports whose test quantities will be restored after test execution if the restoration mode is set to “PORTS”. Use `SetRestoreTestQuantitiesMode()` to configure the restoration mode.

Parameters:  **ports** (*list[str]*) – The list of ports whose test quantities should be restored after test execution.

SetSimulationMode(*simulationMode*)[¶](#ApiClient.Execution.SetSimulationMode "Link to this definition")  
Sets the simulation mode to be used when starting the configuration. Valid values for the simulation mode are ‘AUTO’, ‘STEPWISE’ and ‘CONTINUOUS’.

Parameters:  **simulationMode** (*str*) – The simulation mode

SetTimeSource(*timeSource*)[¶](#ApiClient.Execution.SetTimeSource "Link to this definition")  
Sets the time source to be used when starting the configuration. The time source might either be ‘AUTO’, ‘REALTIME’ or a port name.

Attention:  
The timeSource argument will not be validated. Setting a port name that is not connected in the TCF will not cause an Exception here, but when saving the TCF later on.

Parameters:  **timeSource** (*str*) – The time source

SetWaitTimeAfterIOTeststep(*waitTime*)[¶](#ApiClient.Execution.SetWaitTimeAfterIOTeststep "Link to this definition")  
Sets the wait time after every I/O test step.

Parameters:  **waitTime** (*float*) – Wait time in ms

## MediaAccess[¶](#mediaaccess "Link to this heading")

*class* MediaAccess[¶](#ApiClient.MediaAccess "Link to this definition")  
Returned by

- [`TestConfiguration.MediaAccess`](#ApiClient.TestConfiguration.MediaAccess "ApiClient.TestConfiguration.MediaAccess")

Add(*mediaKey*)[¶](#ApiClient.MediaAccess.Add "Link to this definition")  
Adds a media object.

Parameters:  **mediaKey** (*str*) – Name of the media

Returns:  The media object

Return type:  [`Media`](#ApiClient.Media "ApiClient.Media")

Clone()[¶](#ApiClient.MediaAccess.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`MediaAccess`](#ApiClient.MediaAccess "ApiClient.MediaAccess")

Delete(*mediaKey*)[¶](#ApiClient.MediaAccess.Delete "Link to this definition")  
Deletes a media from media access.

Parameters:  **mediaKey** (*str*) – Name of media to delete

Raises:  
**ApiError** – If there is no media with the given name

Get(*mediaKey*)[¶](#ApiClient.MediaAccess.Get "Link to this definition")  
Returns a media object.

Parameters:  **mediaKey** (*str*) – Name of the media

Returns:  The media object

Return type:  [`Media`](#ApiClient.Media "ApiClient.Media")

Raises:  
**ApiError** – If no media with the given name is configured.

GetAll()[¶](#ApiClient.MediaAccess.GetAll "Link to this definition")  
Returns a list of names of all medias.

Returns:  Names of all medias.

Return type:  list[str]

GetOcrDataProvidedByEcuTest()[¶](#ApiClient.MediaAccess.GetOcrDataProvidedByEcuTest "Link to this definition")  
Returns a list with all ocr data names provided by ecu.test.

Returns:  List with ocr data names

Return type:  list[str]

## Media[¶](#media "Link to this heading")

*class* Media[¶](#ApiClient.Media "Link to this definition")  
Returned by

- [`MediaAccess.Add`](#ApiClient.MediaAccess.Add "ApiClient.MediaAccess.Add")

- [`MediaAccess.Get`](#ApiClient.MediaAccess.Get "ApiClient.MediaAccess.Get")

Clone()[¶](#ApiClient.Media.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`Media`](#ApiClient.Media "ApiClient.Media")

GetAudioDefaultSpeechToTextProfile()[¶](#ApiClient.Media.GetAudioDefaultSpeechToTextProfile "Link to this definition")  
Returns the configured default profile for speech-to-text functionality.

Returns:  A dictionary containing the serviceName, profileName, language.

Return type:  dict[str, str]

GetAudioDefaultVoice()[¶](#ApiClient.Media.GetAudioDefaultVoice "Link to this definition")  
Returns speaker and voice for configured default voice.

Returns:  Returns a dictionary containing the configured serviceId, voiceName, voiceLanguage, voiceGender.

Return type:  dict[str, str]

GetAudioPort()[¶](#ApiClient.Media.GetAudioPort "Link to this definition")  
Returns the audio port.

Returns:  Audio port

Return type:  str

GetImageFolder()[¶](#ApiClient.Media.GetImageFolder "Link to this definition")  
Returns the image folder.

Returns:  Image folder

Return type:  str

GetImagePort()[¶](#ApiClient.Media.GetImagePort "Link to this definition")  
Returns the image port.

Returns:  Image port

Return type:  str

GetName()[¶](#ApiClient.Media.GetName "Link to this definition")  
Returns the name of the media.

Returns:  Name of the media

Return type:  str

GetOcrConfig()[¶](#ApiClient.Media.GetOcrConfig "Link to this definition")  
Returns a dictionary of ocr configuration data specified in the test configuration.

Returns:  Dictionary of ocr config data

Return type:  dict\<str, str\>

GetOcrService()[¶](#ApiClient.Media.GetOcrService "Link to this definition")  
Returns the selected OCR service.

Returns:  Identifier of OCR service

Return type:  str

Rename(*newMediaKey*)[¶](#ApiClient.Media.Rename "Link to this definition")  
Renames the media.

Parameters:  **newMediaKey** (*str*) – New name of the media object

SetAudioDefaultSpeechToTextProfile(*serviceId=None*, *profileName=None*, *language=None*)[¶](#ApiClient.Media.SetAudioDefaultSpeechToTextProfile "Link to this definition")  
Sets the default profile for speech-to-text functionality.

Parameters:  - **serviceId** (*str*) – Identifier of the speech-to-text service

- **profileName** (*str*) – Name of the speech-to-text profile

- **language** (*str*) – The language which this profile can recognize, e.g. ‘en’, ‘de’

SetAudioDefaultVoice(*serviceId=None*, *voiceName=None*, *voiceLanguage=None*, *voiceGender=None*)[¶](#ApiClient.Media.SetAudioDefaultVoice "Link to this definition")  
Sets default voice for audio port to the voice identified by serviceId, voiceName, voiceLanguage and voiceGender.

Parameters:  - **serviceId** (*str*) – ID of text-to-speech service.

- **voiceName** (*str*) – Name of the voice. Has to be available for specified serviceId.

- **voiceLanguage** (*str*) – Language of voice as language code, e.g. ‘en’, ‘de’

- **voiceGender** (*str*) – Gender of voice (‘MALE’, ‘FEMALE’, ‘OTHER’, ‘UNDEFINED’)

SetAudioPort(*audioPort*)[¶](#ApiClient.Media.SetAudioPort "Link to this definition")  
Sets the audio port.

Parameters:  **audioPort** (*str*) – Audio port to be set

SetImageFolder(*imageFolder*)[¶](#ApiClient.Media.SetImageFolder "Link to this definition")  
Sets the image folder.

Parameters:  **imageFolder** (*str*) – Image folder to be set

SetImagePort(*imagePort*)[¶](#ApiClient.Media.SetImagePort "Link to this definition")  
Sets the image port.

Parameters:  **imagePort** (*str*) – Image port to be set

SetOcrConfig(*ocrConfigData*)[¶](#ApiClient.Media.SetOcrConfig "Link to this definition")  
Sets the data of the ocr configuration.

Parameters:  **ocrConfigData** (*dict\<str,* *str\>*) – Dictionary of ocr config data

SetOcrService(*serviceId*)[¶](#ApiClient.Media.SetOcrService "Link to this definition")  
Sets the selected OCR service.

Parameters:  **serviceId** (*str*) – Name of the OCR service

GetOcrData()[¶](#ApiClient.Media.GetOcrData "Link to this definition")  
Returns a list of all tesseract ocr model data specified in the test configuration.

If the ocr data is provided by ecu.test, then only the name of the orc dataset is given. If the referenced ocr dataset is part of the workspace, the relative path is given. Otherwise, the absolute path is given.

Returns:  List with tesseract ocr data

Return type:  list[str]

Raises:  
**ApiError** – If called for configured OCR service other than tesseract

Deprecated since version 2024.3: Please use [\`](#id1)GetOcrService/GetOcrConfig instead.

SetOcrData(*ocrData*)[¶](#ApiClient.Media.SetOcrData "Link to this definition")  
Sets the list of tesseract ocr model data.

Ocr data provided by ecu.test, can only be referenced by the name. Ocr data that is part of the workspace can be referenced by a path relative to the workspace. Ocr data that is not part of the workspace need to be referenced by a absolut path.

Parameters:  **ocrData** (*list[str]*) – List of tesseract ocr data

Raises:  
- **ApiError** – If no ocr data is specified

- **ApiError** – If called for configured OCR service other than tesseract

Deprecated since version 2024.3: Please use [\`](#id3)SetOcrService/SetOcrConfig instead.

## Platform[¶](#platform "Link to this heading")

*class* Platform[¶](#ApiClient.Platform "Link to this definition")  
Returned by

- [`TestConfiguration.Platform`](#ApiClient.TestConfiguration.Platform "ApiClient.TestConfiguration.Platform")

FailureSimulation[¶](#ApiClient.Platform.FailureSimulation "Link to this definition")  
Failure Simulation access

Returns:  Failure Simulation access

Return type:  [`FailureSimulationAccess`](#ApiClient.FailureSimulationAccess "ApiClient.FailureSimulationAccess")

FunctionAccess[¶](#ApiClient.Platform.FunctionAccess "Link to this definition")  
Function access

Returns:  Function access

Return type:  [`FunctionAccess`](#ApiClient.FunctionAccess "ApiClient.FunctionAccess")

ModelAccess[¶](#ApiClient.Platform.ModelAccess "Link to this definition")  
Model access

Returns:  Model access

Return type:  [`ModelAccess`](#ApiClient.ModelAccess "ApiClient.ModelAccess")

Clone()[¶](#ApiClient.Platform.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`Platform`](#ApiClient.Platform "ApiClient.Platform")

## FailureSimulationAccess[¶](#failuresimulationaccess "Link to this heading")

*class* FailureSimulationAccess[¶](#ApiClient.FailureSimulationAccess "Link to this definition")  
Returned by

- [`Platform.FailureSimulation`](#ApiClient.Platform.FailureSimulation "ApiClient.Platform.FailureSimulation")

Add(*failureSimulationKey*, *failureSimulationFile=''*, *failureSimulationPort=''*)[¶](#ApiClient.FailureSimulationAccess.Add "Link to this definition")  
Adds a failure simulation

Parameters:  - **failureSimulationKey** (*str*) – Name of the failure simulation to add

- **failureSimulationFile** (*str*) – Name of the failure simulation file

- **failureSimulationPort** (*str*) – Name of the failure simulation port

Returns:  The failure simulation which was added

Return type:  [`FailureSimulation`](#ApiClient.FailureSimulation "ApiClient.FailureSimulation")

Clone()[¶](#ApiClient.FailureSimulationAccess.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`FailureSimulationAccess`](#ApiClient.FailureSimulationAccess "ApiClient.FailureSimulationAccess")

Delete(*failureSimulationKey*)[¶](#ApiClient.FailureSimulationAccess.Delete "Link to this definition")  
Deletes a failure simulation.

Parameters:  **failureSimulationKey** (*str*) – Name of failure simulation to delete

Get(*failureSimulationKey*)[¶](#ApiClient.FailureSimulationAccess.Get "Link to this definition")  
Returns the failure simulation object specified by the given key.

Parameters:  **failureSimulationKey** (*str*) – Name of the failure simulation

Returns:  The failure simulation object

Return type:  [`FailureSimulation`](#ApiClient.FailureSimulation "ApiClient.FailureSimulation")

GetAll()[¶](#ApiClient.FailureSimulationAccess.GetAll "Link to this definition")  
Returns a list of the names of all the failure simulations.

Returns:  List of names of all failure simulations

Return type:  list[str]

## FailureSimulation[¶](#failuresimulation "Link to this heading")

*class* FailureSimulation[¶](#ApiClient.FailureSimulation "Link to this definition")  
Returned by

- [`FailureSimulationAccess.Add`](#ApiClient.FailureSimulationAccess.Add "ApiClient.FailureSimulationAccess.Add")

- [`FailureSimulationAccess.Get`](#ApiClient.FailureSimulationAccess.Get "ApiClient.FailureSimulationAccess.Get")

Clone()[¶](#ApiClient.FailureSimulation.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`FailureSimulation`](#ApiClient.FailureSimulation "ApiClient.FailureSimulation")

GetFile()[¶](#ApiClient.FailureSimulation.GetFile "Link to this definition")  
Returns the failure simulation file.

Returns:  Failure simulation file

Return type:  str

GetName()[¶](#ApiClient.FailureSimulation.GetName "Link to this definition")  
Returns the name of the failure simulation.

Returns:  Name of the failure simulation

Return type:  str

GetPort()[¶](#ApiClient.FailureSimulation.GetPort "Link to this definition")  
Returns the failure simulation port.

Returns:  Failure simulation port

Return type:  str

Rename(*newFailureSimulationKey*)[¶](#ApiClient.FailureSimulation.Rename "Link to this definition")  
Renames this failure simulation

Parameters:  **newFailureSimulationKey** (*str*) – New name

SetFile(*failureSimulationFile*)[¶](#ApiClient.FailureSimulation.SetFile "Link to this definition")  
Sets the failure simulation file.

Parameters:  **failureSimulationFile** (*str*) – Failure simulation file to be set

SetPort(*failureSimulationPort*)[¶](#ApiClient.FailureSimulation.SetPort "Link to this definition")  
Sets the failure simulation port.

Parameters:  **failureSimulationPort** (*str*) – Failure simulation port to be set

## FunctionAccess[¶](#functionaccess "Link to this heading")

*class* FunctionAccess[¶](#ApiClient.FunctionAccess "Link to this definition")  
Returned by

- [`Platform.FunctionAccess`](#ApiClient.Platform.FunctionAccess "ApiClient.Platform.FunctionAccess")

Add(*functionKey*, *functionFile=''*, *functionPort=''*)[¶](#ApiClient.FunctionAccess.Add "Link to this definition")  
Adds a function to the function access.

Parameters:  - **functionKey** (*str*) – Name of the function to add

- **functionFile** (*str*) – Name of the function file

- **functionPort** (*str*) – Name of the function port

Returns:  The function which was added

Return type:  [`Function`](#ApiClient.Function "ApiClient.Function")

Clone()[¶](#ApiClient.FunctionAccess.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`FunctionAccess`](#ApiClient.FunctionAccess "ApiClient.FunctionAccess")

Delete(*functionKey*)[¶](#ApiClient.FunctionAccess.Delete "Link to this definition")  
Deletes a function.

Parameters:  **functionKey** (*str*) – Name of function to delete

Get(*functionKey*)[¶](#ApiClient.FunctionAccess.Get "Link to this definition")  
Returns a function object.

Parameters:  **functionKey** (*str*) – Name of the function

Returns:  The function object

Return type:  [`Function`](#ApiClient.Function "ApiClient.Function")

GetAll()[¶](#ApiClient.FunctionAccess.GetAll "Link to this definition")  
Returns a list of the names of all the functions.

Returns:  List of names of all functions

Return type:  list[str]

## Function[¶](#function "Link to this heading")

*class* Function[¶](#ApiClient.Function "Link to this definition")  
Returned by

- [`FunctionAccess.Add`](#ApiClient.FunctionAccess.Add "ApiClient.FunctionAccess.Add")

- [`FunctionAccess.Get`](#ApiClient.FunctionAccess.Get "ApiClient.FunctionAccess.Get")

Clone()[¶](#ApiClient.Function.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`Function`](#ApiClient.Function "ApiClient.Function")

GetFile()[¶](#ApiClient.Function.GetFile "Link to this definition")  
Returns the function access file.

Returns:  Function access file

Return type:  str

GetName()[¶](#ApiClient.Function.GetName "Link to this definition")  
Returns the name of the function access.

Returns:  Name of the function

Return type:  str

GetPort()[¶](#ApiClient.Function.GetPort "Link to this definition")  
Returns the function access port.

Returns:  Function access port

Return type:  str

Rename(*newFunctionKey*)[¶](#ApiClient.Function.Rename "Link to this definition")  
Renames the function access.

Parameters:  **newFunctionKey** (*str*) – New name of the function

SetFile(*functionFile*)[¶](#ApiClient.Function.SetFile "Link to this definition")  
Sets the function access file.

Parameters:  **functionFile** (*str*) – Function access file to be set

SetPort(*functionPort*)[¶](#ApiClient.Function.SetPort "Link to this definition")  
Sets the function access port.

Parameters:  **functionPort** (*str*) – Function access port to be set

## ModelAccess[¶](#modelaccess "Link to this heading")

*class* ModelAccess[¶](#ApiClient.ModelAccess "Link to this definition")  
Returned by

- [`Platform.ModelAccess`](#ApiClient.Platform.ModelAccess "ApiClient.Platform.ModelAccess")

Add(*modelKey*)[¶](#ApiClient.ModelAccess.Add "Link to this definition")  
Adds a model

Parameters:  **modelKey** (*str*) – Name of the model to add

Returns:  The model which was added

Return type:  [`Model`](#ApiClient.Model "ApiClient.Model")

Clone()[¶](#ApiClient.ModelAccess.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`ModelAccess`](#ApiClient.ModelAccess "ApiClient.ModelAccess")

Delete(*modelKey*)[¶](#ApiClient.ModelAccess.Delete "Link to this definition")  
Deletes a model from model access.

Parameters:  **modelKey** (*str*) – Name of model to delete

Get(*modelKey*)[¶](#ApiClient.ModelAccess.Get "Link to this definition")  
Retrieves a model object.

Parameters:  **modelKey** (*str*) – Name of the model

Returns:  The model object

Return type:  [`Model`](#ApiClient.Model "ApiClient.Model")

GetAll()[¶](#ApiClient.ModelAccess.GetAll "Link to this definition")  
Returns a list of the names of all the accessed models.

Returns:  list of names of all accesses models

Return type:  list[str]

## Model[¶](#model "Link to this heading")

*class* Model[¶](#ApiClient.Model "Link to this definition")  
Returned by

- [`ModelAccess.Add`](#ApiClient.ModelAccess.Add "ApiClient.ModelAccess.Add")

- [`ModelAccess.Get`](#ApiClient.ModelAccess.Get "ApiClient.ModelAccess.Get")

Clone()[¶](#ApiClient.Model.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`Model`](#ApiClient.Model "ApiClient.Model")

GetAdditionalFiles()[¶](#ApiClient.Model.GetAdditionalFiles "Link to this definition")  
Gets additional files configured for this model.

Returns:  The list of additional files

Return type:  list[str]

GetFile()[¶](#ApiClient.Model.GetFile "Link to this definition")  
Returns the model file.

Returns:  Model file

Return type:  str

GetImportSource()[¶](#ApiClient.Model.GetImportSource "Link to this definition")  
Returns the model import source.

Returns:  Model import source: 0 Automatically, 1 From Cache, 2 Disabled

Return type:  int

GetName()[¶](#ApiClient.Model.GetName "Link to this definition")  
Returns the name of the model.

Returns:  Name of the model

Return type:  str

GetPort()[¶](#ApiClient.Model.GetPort "Link to this definition")  
Returns the model port.

Returns:  Model port

Return type:  str

InsertAdditionalFile(*filename*, *index=None*)[¶](#ApiClient.Model.InsertAdditionalFile "Link to this definition")  
Adds an entry on the given index into the additional files list.

Some model tools allow e.g. \*.par or \*.smf files to be specified here.

Parameters:  - **filename** (*str*) – The name of the file to be added

- **index** (*int*) – The index the new entry should be placed at. If left out, the filename will be appended at the end of the list.

RemoveAdditionalFile(*index*)[¶](#ApiClient.Model.RemoveAdditionalFile "Link to this definition")  
Removes the entry on the given index from additional files list.

Parameters:  **index** (*int*) – The index to be removed.

Rename(*newModelKey*)[¶](#ApiClient.Model.Rename "Link to this definition")  
Renames the model.

Parameters:  **newModelKey** (*str*) – New name of the model

SetFile(*modelFile*)[¶](#ApiClient.Model.SetFile "Link to this definition")  
Sets the model file.

Parameters:  **modelFile** (*str*) – Model file to be set

SetImportSource(*importSource*)[¶](#ApiClient.Model.SetImportSource "Link to this definition")  
Sets the model import source.

Parameters:  **importSource** (*int*) – Model import source: 0 Automatically, 1 From Cache, 2 Disabled

SetPort(*modelPort*)[¶](#ApiClient.Model.SetPort "Link to this definition")  
Sets the model port.

Parameters:  **modelPort** (*str*) – Model port to be set

## ReportData[¶](#reportdata "Link to this heading")

*class* ReportData[¶](#ApiClient.ReportData "Link to this definition")  
Returned by

- [`TestConfiguration.Report`](#ApiClient.TestConfiguration.Report "ApiClient.TestConfiguration.Report")

AddReportFormat(*reportFormat*)[¶](#ApiClient.ReportData.AddReportFormat "Link to this definition")  
Adds a report format to your configuration.

Parameters:  **reportFormat** ([`ReportFormat`](#ApiClient.ReportFormat "ApiClient.ReportFormat")) – Report format to be added

Clone()[¶](#ApiClient.ReportData.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`ReportData`](#ApiClient.ReportData "ApiClient.ReportData")

CreateReportFormat(*formatName*)[¶](#ApiClient.ReportData.CreateReportFormat "Link to this definition")  
Create a new Output format.

Parameters:  **formatName** (*str*) – Format handler (e.g. “HTML”, “EXCEL”, …)

Returns:  New report format

Return type:  [`ReportFormat`](#ApiClient.ReportFormat "ApiClient.ReportFormat")

GetAvailableOutputFormats()[¶](#ApiClient.ReportData.GetAvailableOutputFormats "Link to this definition")  
Returns a list of available output formats.

Returns:  List of report format names

Return type:  list[str]

GetConfiguredOutputFormats(*showActiveOnly=False*)[¶](#ApiClient.ReportData.GetConfiguredOutputFormats "Link to this definition")  
Returns a list of display names from configured output formats.

Parameters:  **showActiveOnly** (*bool*) – If True only formats that will be automatically generated are shown.

Returns:  List of report format names

Return type:  list[str]

GetCopyLogFilesToReportFolder()[¶](#ApiClient.ReportData.GetCopyLogFilesToReportFolder "Link to this definition")  
Gets the state of the option to copy log files to report folder.

Returns:  State of the option.

Return type:  bool

GetDirectory()[¶](#ApiClient.ReportData.GetDirectory "Link to this definition")  
Returns the report directory.

Returns:  Report directory

Return type:  str

GetReportFormat(*displayName*)[¶](#ApiClient.ReportData.GetReportFormat "Link to this definition")  
Return the report format with the given displayname.

Parameters:  **displayName** (*string*) – Name of the report format

Returns:  Report format object

Return type:  [`ReportFormat`](#ApiClient.ReportFormat "ApiClient.ReportFormat")

GetReportFormats(*autoGenerateOnly*)[¶](#ApiClient.ReportData.GetReportFormats "Link to this definition")  
Returns a list of configured report formats.

Parameters:  **autoGenerateOnly** (*bool*) – If True only formats that will be automatically generated are shown.

Returns:  List of report format display names

Return type:  list[[`ReportFormat`](#ApiClient.ReportFormat "ApiClient.ReportFormat")]

GetUserDefinedInfoScript()[¶](#ApiClient.ReportData.GetUserDefinedInfoScript "Link to this definition")  
Returns the script file for generating user defined report information.

Returns:  Path to the \*.py file. Absolute or relative to workspace.

Return type:  str

GetUserReportData()[¶](#ApiClient.ReportData.GetUserReportData "Link to this definition")  
Returns user defined report information.

Returns:  User defined report information

Return type:  [`UserReportData`](#ApiClient.UserReportData "ApiClient.UserReportData")

RemoveReportFormat(*reportFormat*)[¶](#ApiClient.ReportData.RemoveReportFormat "Link to this definition")  
Removes the report format.

Parameters:  **reportFormat** ([`ReportFormat`](#ApiClient.ReportFormat "ApiClient.ReportFormat")) – Report format to be removed

RemoveReportFormatByName(*displayedName*)[¶](#ApiClient.ReportData.RemoveReportFormatByName "Link to this definition")  
Removes an report format by name.

Parameters:  **displayedName** (*str*) – Format name (e.g. “New HTML report”)

SetCopyLogFilesToReportFolder(*state*)[¶](#ApiClient.ReportData.SetCopyLogFilesToReportFolder "Link to this definition")  
Enable or disable the option to copy log files to report folder.

Parameters:  **state** (*bool*) – Enable or disable copy

SetDirectory(*reportDir*)[¶](#ApiClient.ReportData.SetDirectory "Link to this definition")  
Sets the report directory.

Parameters:  **reportDir** (*str*) – Report directory to be set

SetUserDefinedInfoScript(*filepath*)[¶](#ApiClient.ReportData.SetUserDefinedInfoScript "Link to this definition")  
Sets the script file for generating user defined report information.

Parameters:  **filepath** (*str*) – Path to the \*.py file. Absolute or relative to the workspace. If an empty string is passed, the script path will be reset.

## ReportFormat[¶](#reportformat "Link to this heading")

*class* ReportFormat[¶](#ApiClient.ReportFormat "Link to this definition")  
Returned by

- [`ReportData.CreateReportFormat`](#ApiClient.ReportData.CreateReportFormat "ApiClient.ReportData.CreateReportFormat")

- [`ReportData.GetReportFormat`](#ApiClient.ReportData.GetReportFormat "ApiClient.ReportData.GetReportFormat")

- [`ReportData.GetReportFormats`](#ApiClient.ReportData.GetReportFormats "ApiClient.ReportData.GetReportFormats")

Clone()[¶](#ApiClient.ReportFormat.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`ReportFormat`](#ApiClient.ReportFormat "ApiClient.ReportFormat")

GetDisplayName()[¶](#ApiClient.ReportFormat.GetDisplayName "Link to this definition")  
Returns the display name.

Returns:  display name

Return type:  string

GetFormat()[¶](#ApiClient.ReportFormat.GetFormat "Link to this definition")  
Returns the format name.

Returns:  format name

Return type:  string

GetPrePostScript()[¶](#ApiClient.ReportFormat.GetPrePostScript "Link to this definition")  
Returns the pre/post script if set.

Returns:  Pre/post script or empty string if not set

Return type:  string

GetProjectFilter()[¶](#ApiClient.ReportFormat.GetProjectFilter "Link to this definition")  
Returns the project report filter configuration.

Returns:  The project report filter

Return type:  [`FilterGroupDisjunction`](ReportFilterApi.md#ApiClient.FilterGroupDisjunction "ApiClient.FilterGroupDisjunction")

GetSettings()[¶](#ApiClient.ReportFormat.GetSettings "Link to this definition")  
Returns the configuration for this report format.

Returns:  Report format configuration

Return type:  dict[str, str]

GetSettingsValue(*name*)[¶](#ApiClient.ReportFormat.GetSettingsValue "Link to this definition")  
Returns a specific configuration value.

Parameters:  **name** (*string*) – Name of the settings entry

Returns:  Value of the settings entry

Return type:  string

GetTestCaseFilter()[¶](#ApiClient.ReportFormat.GetTestCaseFilter "Link to this definition")  
Returns the test case report filter configuration.

Returns:  The test case report filter

Return type:  [`FilterGroupDisjunction`](ReportFilterApi.md#ApiClient.FilterGroupDisjunction "ApiClient.FilterGroupDisjunction")

GetTraceAnalysesFilter()[¶](#ApiClient.ReportFormat.GetTraceAnalysesFilter "Link to this definition")  
Returns the trace analyses report filter configuration.

Returns:  The trace analyses report filter

Return type:  [`FilterGroupDisjunction`](ReportFilterApi.md#ApiClient.FilterGroupDisjunction "ApiClient.FilterGroupDisjunction")

IsAutoGenerate()[¶](#ApiClient.ReportFormat.IsAutoGenerate "Link to this definition")  
Returns if the report format will be automatically generated.

Returns:  True for automatic generation.

Return type:  bool

IsSaveReportFormat()[¶](#ApiClient.ReportFormat.IsSaveReportFormat "Link to this definition")  
Return if the configuration will be saved for later use.

Returns:  True if activated

Return type:  bool

SetAutoGenerate(*autoGenerate*)[¶](#ApiClient.ReportFormat.SetAutoGenerate "Link to this definition")  
Enable or Disable automatic generation of the report format.

Parameters:  **autoGenerate** (*bool*) – If True, report will be generated automatically after package execution

SetDisplayName(*displayName*)[¶](#ApiClient.ReportFormat.SetDisplayName "Link to this definition")  
Sets the display name.

Parameters:  **displayName** (*string*) – New display name to be set

SetPrePostScript(*prePostScript*)[¶](#ApiClient.ReportFormat.SetPrePostScript "Link to this definition")  
Sets a pre/post script.

Parameters:  **prePostScript** (*string*) – pre/post script as “user.\<package\>.\<module\>.\<class\>” or empty string to unset.

SetProjectFilter(*filterGroup*)[¶](#ApiClient.ReportFormat.SetProjectFilter "Link to this definition")  
Sets the project report filter configuration.

Parameters:  **filterGroup** ([`FilterGroupDisjunction`](ReportFilterApi.md#ApiClient.FilterGroupDisjunction "ApiClient.FilterGroupDisjunction")) – The project report filter

SetSaveReportFormat(*saveEnabled*)[¶](#ApiClient.ReportFormat.SetSaveReportFormat "Link to this definition")  
Enable or Disable saving of the configuration for later use.

Parameters:  **saveEnabled** (*bool*) – True for activating

SetSettings(*settings*)[¶](#ApiClient.ReportFormat.SetSettings "Link to this definition")  
Sets the configuration for this report format

Parameters:  **settings** (*dict[str,* *str]*) – Report format configuration

SetSettingsValue(*name*, *value*)[¶](#ApiClient.ReportFormat.SetSettingsValue "Link to this definition")  
Sets a specific configuration value.

Parameters:  - **name** (*string*) – Name of the settings entry

- **value** (*string*) – Value of the settings entry

SetTestCaseFilter(*filterGroup*)[¶](#ApiClient.ReportFormat.SetTestCaseFilter "Link to this definition")  
Sets the test case report filter configuration.

Parameters:  **filterGroup** ([`FilterGroupDisjunction`](ReportFilterApi.md#ApiClient.FilterGroupDisjunction "ApiClient.FilterGroupDisjunction")) – The test case report filter

SetTraceAnalysesFilter(*filterGroup*)[¶](#ApiClient.ReportFormat.SetTraceAnalysesFilter "Link to this definition")  
Sets the trace analyses report filter configuration.

Parameters:  **filterGroup** ([`FilterGroupDisjunction`](ReportFilterApi.md#ApiClient.FilterGroupDisjunction "ApiClient.FilterGroupDisjunction")) – The trace analyses report filter

## UserReportData[¶](#userreportdata "Link to this heading")

*class* UserReportData[¶](#ApiClient.UserReportData "Link to this definition")  
Returned by

- [`ReportData.GetUserReportData`](#ApiClient.ReportData.GetUserReportData "ApiClient.ReportData.GetUserReportData")

AppendEntry(*name*, *value=None*, *description=None*)[¶](#ApiClient.UserReportData.AppendEntry "Link to this definition")  
Appends a new entry. If a entry with the same name already exists, it will be overwritten.

Parameters:  - **name** (*str*) – Name of the entry

- **value** (*str*) – Value of the entry

- **description** (*str*) – Description of the entry

Clone()[¶](#ApiClient.UserReportData.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`UserReportData`](#ApiClient.UserReportData "ApiClient.UserReportData")

GetAllEntryNames()[¶](#ApiClient.UserReportData.GetAllEntryNames "Link to this definition")  
Returns a list of all entry names.

Returns:  List of all entry names

Return type:  list[str]

GetDescription(*name*)[¶](#ApiClient.UserReportData.GetDescription "Link to this definition")  
Returns the description of the entry specified by the given name.

Parameters:  **name** (*str*) – Name of the entry

Returns:  Description text

Return type:  str

GetValue(*name*)[¶](#ApiClient.UserReportData.GetValue "Link to this definition")  
Returns the value of the entry specified by the given name.

Parameters:  **name** (*str*) – Name of the entry

Returns:  Value of the entry

Return type:  str

Raises:  
**ApiError** – If the entry with the given name does not exist

RemoveEntry(*name*)[¶](#ApiClient.UserReportData.RemoveEntry "Link to this definition")  
Removes the entry specified by the given name.

Parameters:  **name** (*str*) – Name of the entry

Returns:  True if successful. False if no entry with such name exists.

Return type:  boolean

SetDescription(*name*, *description*)[¶](#ApiClient.UserReportData.SetDescription "Link to this definition")  
Sets the description of the entry specified by the given name.

Parameters:  - **name** (*str*) – Name of the entry

- **description** (*str*) – Description text

Raises:  
- **ApiError** – If the entry with the given name does not exist

- **ApiError** – If description is no str

SetValue(*name*, *value*)[¶](#ApiClient.UserReportData.SetValue "Link to this definition")  
Sets the value of the entry specified by the given name.

Parameters:  - **name** (*str*) – Name of the entry

- **value** (*str*) – Value of the entry

Raises:  
**ApiError** – If the entry with the given name does not exist

## Change[¶](#change "Link to this heading")

*class* Change[¶](#ApiClient.Change "Link to this definition")  
Represents a change between an old element and a new element. Both elements have the same type, e.g. a certain test step and stem from two different Objects, e.g. an old Package a new Package.

Returned by

- [`ConfigurationApi.GetChangesForTestBenchConfigurations`](#ApiClient.ConfigurationApi.GetChangesForTestBenchConfigurations "ApiClient.ConfigurationApi.GetChangesForTestBenchConfigurations")

- [`ConfigurationApi.GetChangesForTestConfigurations`](#ApiClient.ConfigurationApi.GetChangesForTestConfigurations "ApiClient.ConfigurationApi.GetChangesForTestConfigurations")

- [`GlobalMappingApi.GetChanges`](GlobalMappingApi.md#ApiClient.GlobalMappingApi.GetChanges "ApiClient.GlobalMappingApi.GetChanges")

- [`PackageApi.GetAnalysisPackageChanges`](PackageApi.md#ApiClient.PackageApi.GetAnalysisPackageChanges "ApiClient.PackageApi.GetAnalysisPackageChanges")

- [`PackageApi.GetChanges`](PackageApi.md#ApiClient.PackageApi.GetChanges "ApiClient.PackageApi.GetChanges")

- [`ParameterApi.GetChangesForGlobalConstantsDefinitions`](ParameterApi.md#ApiClient.ParameterApi.GetChangesForGlobalConstantsDefinitions "ApiClient.ParameterApi.GetChangesForGlobalConstantsDefinitions")

- [`ParameterApi.GetChangesForPackageParametersDefinitions`](ParameterApi.md#ApiClient.ParameterApi.GetChangesForPackageParametersDefinitions "ApiClient.ParameterApi.GetChangesForPackageParametersDefinitions")

- [`ProjectApi.GetChanges`](ProjectApi.md#ApiClient.ProjectApi.GetChanges "ApiClient.ProjectApi.GetChanges")

Clone()[¶](#ApiClient.Change.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`Change`](#ApiClient.Change "ApiClient.Change")

GetComparedProperties()[¶](#ApiClient.Change.GetComparedProperties "Link to this definition")  
Return the properties based on which the old element and the new element were compared.

Returns:  A list of names of compared properties.

Return type:  list[str]

GetNewPath()[¶](#ApiClient.Change.GetNewPath "Link to this definition")  
Returns the path to the new element, e.g. ‘0:Package/2:Testcase/0:Block 1/5:Comment 3’.

Returns:  The path to the new element.

Return type:  str

GetOldPath()[¶](#ApiClient.Change.GetOldPath "Link to this definition")  
Returns the path to the old element, e.g. ‘0:Package/2:Testcase/0:Block 1/5:Comment 3’.

Returns:  The path to the old element.

Return type:  str

GetType()[¶](#ApiClient.Change.GetType "Link to this definition")  
Returns the type of action that is associated with this change. The action type can be one of the following:

> - INSERT - The new element was inserted.
>
> - DELETE - The old element was deleted.
>
> - MOVE - The new element was moved with respect to the old one.
>
> - UPDATE - The new element differs in certain values with respect to the old one.
>
> - POTENTIALUPDATE - The elements can’t be compared completely. There may exist a change.

Returns:  The type of action that is associated with this change.

Return type:  str

GetValueDifferences()[¶](#ApiClient.Change.GetValueDifferences "Link to this definition")  
Returns a list with differences that exist between values of the old and the new element.

Returns:  A list of changed values.

Return type:  list[[`ValueDifference`](#ApiClient.ValueDifference "ApiClient.ValueDifference")]

## ValueDifference[¶](#valuedifference "Link to this heading")

*class* ValueDifference[¶](#ApiClient.ValueDifference "Link to this definition")  
Represents a difference in a certain value between two elements after a change occured.

Returned by

- [`Change.GetValueDifferences`](#ApiClient.Change.GetValueDifferences "ApiClient.Change.GetValueDifferences")

Clone()[¶](#ApiClient.ValueDifference.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`ValueDifference`](#ApiClient.ValueDifference "ApiClient.ValueDifference")

GetNewValue()[¶](#ApiClient.ValueDifference.GetNewValue "Link to this definition")  
The value after the changed happened.

Returns:  The value after the change happened.

Return type:  str

GetOldValue()[¶](#ApiClient.ValueDifference.GetOldValue "Link to this definition")  
The value before the change happened.

Returns:  The value before the change happened.

Return type:  str

GetValueName()[¶](#ApiClient.ValueDifference.GetValueName "Link to this definition")  
Returns the name of the value, e.g. ‘Description’. Values that come from a nested property will be flattened and result in names like e.g. ‘CaseNodes/0/Name’.

Returns:  The name of the value.

Return type:  str
