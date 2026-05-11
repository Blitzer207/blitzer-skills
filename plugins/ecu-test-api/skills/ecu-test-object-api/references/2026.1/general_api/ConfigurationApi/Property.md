[![logo](../../_static/ecu.test.svg)](../../index.html "API  documentation") API documentation

[ Internal APIs ](../api.md)

[ Advanced operations of package variable types ](../variabledatastructures.md)

[ Advanced properties of bus-related objects ](../busdatastructures.md)

[ Bus related objects of trace analysis ](../busdatastructuresTraceanalysis.md)

[ Advanced properties of diagnostics-related objects ](../diagdatastructures.md)

[ Diagnostics related objects of trace analysis ](../diagdatastructuresTraceanalysis.md)

[ Advanced properties of media-related objects ](../mediadatastructures.md)

[ Advanced properties of DLT logging-related objects ](../dltdatastructures.md)

[ COM API ](../com-api.md)

[ REST API ](../rest-api.md)

[ Report API ](../apireport.md)

[ Object API ](../objectApi.md)

Object API

[ API entry points ](../objectApi.md#api-entry-points)

API entry points

[ API for Analysis Jobs ](../AnalysisJobApi.md)

[ API for Artifacts ](../ArtifactApi.md)

[ API for Project Components ](../ComponentApi.md)

[ API for Configurations ](../ConfigurationApi.md)

API for Configurations

[ Bus ](Bus.md)

[ BusAccess ](BusAccess.md)

[ CanIsoTpSettings ](CanIsoTpSettings.md)

[ Change ](Change.md)

[ Common ](Common.md)

[ ControlUnit ](ControlUnit.md)

[ ControlUnits ](ControlUnits.md)

[ DiagSettings ](DiagSettings.md)

[ DoIpSettings ](DoIpSettings.md)

[ DoSoAdSettings ](DoSoAdSettings.md)

[ EnvComAccess ](EnvComAccess.md)

[ EnvComData ](EnvComData.md)

[ EnvSimAccess ](EnvSimAccess.md)

[ EnvSimData ](EnvSimData.md)

[ Environment ](Environment.md)

[ Execution ](Execution.md)

[ FailureSimulation ](FailureSimulation.md)

[ FailureSimulationAccess ](FailureSimulationAccess.md)

[ FrTpSettings ](FrTpSettings.md)

[ Function ](Function.md)

[ FunctionAccess ](FunctionAccess.md)

[ HSFZSettings ](HSFZSettings.md)

[ Media ](Media.md)

[ MediaAccess ](MediaAccess.md)

[ Model ](Model.md)

[ ModelAccess ](ModelAccess.md)

[ Platform ](Platform.md)

[ Port ](Port.md)

Property [ Property ](#)

Property

- [C Property ](#ApiClient.Property)
  - [M Clone ](#ApiClient.Property.Clone)
  - [M GetDefaultValue ](#ApiClient.Property.GetDefaultValue)
  - [M GetDisplayName ](#ApiClient.Property.GetDisplayName)
  - [M GetDomain ](#ApiClient.Property.GetDomain)
  - [M GetName ](#ApiClient.Property.GetName)
  - [M GetValue ](#ApiClient.Property.GetValue)
  - [M GetValueType ](#ApiClient.Property.GetValueType)
  - [M IsReadOnly ](#ApiClient.Property.IsReadOnly)
  - [M SetValue ](#ApiClient.Property.SetValue)
  - [M Unset ](#ApiClient.Property.Unset)

[ PropertySet ](PropertySet.md)

[ ReportData ](ReportData.md)

[ ReportFormat ](ReportFormat.md)

[ TestBenchConfiguration ](TestBenchConfiguration.md)

[ TestConfiguration ](TestConfiguration.md)

[ TestConfigurationGlobalConstants ](TestConfigurationGlobalConstants.md)

[ Tool ](Tool.md)

[ ToolHost ](ToolHost.md)

[ UdsSettings ](UdsSettings.md)

[ UserReportData ](UserReportData.md)

[ ValueDifference ](ValueDifference.md)

[ API for Expectations ](../ExpectationApi.md)

[ API for Expressions ](../ExpressionApi.md)

[ API for Global Mappings ](../GlobalMappingApi.md)

[ API for Mappings ](../MappingApi.md)

[ API for Multimedia Objects ](../MultimediaApi.md)

[ API for Packages ](../PackageApi.md)

[ API for Parameters ](../ParameterApi.md)

[ API for Projects ](../ProjectApi.md)

[ API for Relations ](../RelationApi.md)

[ API for Reports ](../ReportApi.md)

[ API for Report Filters ](../ReportFilterApi.md)

[ API for Settings ](../SettingsApi.md)

[ API for Signals ](../SignalApi.md)

[ API for Signal Descriptions ](../SignalDescriptionApi.md)

[ API for Signal Recordings ](../SignalRecordingApi.md)

[ API for Symbols ](../SymbolApi.md)

[ API for Test Steps ](../TestStepApi.md)

[ API for Touch Inputs ](../TouchInputApi.md)

[ API for Trace Analyses ](../TraceAnalysisApi.md)

[ API for Trace Files ](../TraceFileApi.md)

[ API for Trace Step Templates ](../TraceStepTemplateApi.md)

[ API for Variables ](../VariableApi.md)

[ API for Workspaces ](../WorkspaceApi.md)

[ Trace Analysis API ](../../TraceAnalysisAPI/index.md)

[ Generator APIs ](../../generators/index.md)

[ Tools ](../../tools/index.md)

[ User test management ](../../userTestmanagement/index.md)

[ UserUtility API ](../../user-utility/user-utility.md)

[ Utility Examples ](../../user-utility/example-utilities.md)

Property

- [C Property ](#ApiClient.Property)
  - [M Clone ](#ApiClient.Property.Clone)
  - [M GetDefaultValue ](#ApiClient.Property.GetDefaultValue)
  - [M GetDisplayName ](#ApiClient.Property.GetDisplayName)
  - [M GetDomain ](#ApiClient.Property.GetDomain)
  - [M GetName ](#ApiClient.Property.GetName)
  - [M GetValue ](#ApiClient.Property.GetValue)
  - [M GetValueType ](#ApiClient.Property.GetValueType)
  - [M IsReadOnly ](#ApiClient.Property.IsReadOnly)
  - [M SetValue ](#ApiClient.Property.SetValue)
  - [M Unset ](#ApiClient.Property.Unset)

# Property[¶](#property "Link to this heading")

*class* Property[¶](#ApiClient.Property "Link to this definition")  
Clone()[¶](#ApiClient.Property.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`Property`](#ApiClient.Property "ApiClient.Property (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")

GetDefaultValue()[¶](#ApiClient.Property.GetDefaultValue "Link to this definition")  
Returns the property’s default value.

Returns:  The default value

Return type:  str

See:  
[`Property.GetValueType()`](#ApiClient.Property.GetValueType "ApiClient.Property.GetValueType (Python method) — Returns the value type of this property.")

GetDisplayName()[¶](#ApiClient.Property.GetDisplayName "Link to this definition")  
Returns the display name of the property.

Returns:  The display name of the property

Return type:  str

GetDomain(*[allowOnlineQuery](#ApiClient.Property.GetDomain.allowOnlineQuery "ApiClient.Property.GetDomain.allowOnlineQuery (Python parameter) — Onlineabfrage zulassen")=`False`*)[¶](#ApiClient.Property.GetDomain "Link to this definition")  
Returns the domain of allowed values of this property.

Some properties need to partially connect the tool they belong to in order to determine possible values. Use the parameter `allowOnlineQuery` to allow that. If you don’t, you might get a dummy entry “\<online query\>” instead of the actual values.

Parameters:  allowOnlineQuery : bool[¶](#ApiClient.Property.GetDomain.allowOnlineQuery "Permalink to this definition")  
Onlineabfrage zulassen

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
[`Property.GetValueType()`](#ApiClient.Property.GetValueType "ApiClient.Property.GetValueType (Python method) — Returns the value type of this property.")

GetValueType()[¶](#ApiClient.Property.GetValueType "Link to this definition")  
Returns the value type of this property.

Returns:  Value type of this property

Return type:  str

IsReadOnly()[¶](#ApiClient.Property.IsReadOnly "Link to this definition")  
Returns whether the property is read-only.

Returns:  Property is read-only?

Return type:  boolean

SetValue(*[value](#ApiClient.Property.SetValue.value "ApiClient.Property.SetValue.value (Python parameter) — New value")*)[¶](#ApiClient.Property.SetValue "Link to this definition")  
Overwrites the value of this property.

Parameters:  value : str[¶](#ApiClient.Property.SetValue.value "Permalink to this definition")  
New value

See:  
[`GetDomain()`](#ApiClient.Property.GetDomain "ApiClient.Property.GetDomain (Python method) — Returns the domain of allowed values of this property.")

Unset()[¶](#ApiClient.Property.Unset "Link to this definition")  
Specifies that the property is set to its default value.

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
