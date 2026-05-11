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

[ API for Expectations ](../ExpectationApi.md)

API for Expectations

[ AllExpectation ](AllExpectation.md)

[ AudioExpectation ](AudioExpectation.md)

[ BinaryExpressionExpectation ](BinaryExpressionExpectation.md)

[ BitStreamExpectation ](BitStreamExpectation.md)

[ BitStreamExpressionExpectation ](BitStreamExpressionExpectation.md)

[ BooleanExpectation ](BooleanExpectation.md)

[ ByteStreamExpectation ](ByteStreamExpectation.md)

[ ByteStreamExpressionExpectation ](ByteStreamExpressionExpectation.md)

[ CurveAllExpectation ](CurveAllExpectation.md)

[ CurveSingleExpectation ](CurveSingleExpectation.md)

DTCListExpectation [ DTCListExpectation ](#)

DTCListExpectation

- [C DTCListExpectation ](#ApiClient.DTCListExpectation)
  - [M AppendDtc ](#ApiClient.DTCListExpectation.AppendDtc)
  - [M AppendToleratedDtc ](#ApiClient.DTCListExpectation.AppendToleratedDtc)
  - [M ClearDtcList ](#ApiClient.DTCListExpectation.ClearDtcList)
  - [M ClearToleratedDtcList ](#ApiClient.DTCListExpectation.ClearToleratedDtcList)
  - [M Clone ](#ApiClient.DTCListExpectation.Clone)
  - [M GetDtcList ](#ApiClient.DTCListExpectation.GetDtcList)
  - [M GetDtcListExpression ](#ApiClient.DTCListExpectation.GetDtcListExpression)
  - [M GetRepresentation ](#ApiClient.DTCListExpectation.GetRepresentation)
  - [M GetToleratedDtcList ](#ApiClient.DTCListExpectation.GetToleratedDtcList)
  - [M GetToleratedDtcListExpression ](#ApiClient.DTCListExpectation.GetToleratedDtcListExpression)
  - [M IsExpectPresent ](#ApiClient.DTCListExpectation.IsExpectPresent)
  - [M IsTolerateAll ](#ApiClient.DTCListExpectation.IsTolerateAll)
  - [M SetDtcListExpression ](#ApiClient.DTCListExpectation.SetDtcListExpression)
  - [M SetExpectAbsent ](#ApiClient.DTCListExpectation.SetExpectAbsent)
  - [M SetExpectPresent ](#ApiClient.DTCListExpectation.SetExpectPresent)
  - [M SetRepresentation ](#ApiClient.DTCListExpectation.SetRepresentation)
  - [M SetTolerateAll ](#ApiClient.DTCListExpectation.SetTolerateAll)
  - [M SetToleratedDtcListExpression ](#ApiClient.DTCListExpectation.SetToleratedDtcListExpression)

[ Expectation ](Expectation.md)

[ ExpressionExpectation ](ExpressionExpectation.md)

[ ExpressionExpectationBase ](ExpressionExpectationBase.md)

[ ImageExpectation ](ImageExpectation.md)

[ ManualExpression ](ManualExpression.md)

[ MapAllExpectation ](MapAllExpectation.md)

[ MapSingleExpectation ](MapSingleExpectation.md)

[ MatrixAllExpectation ](MatrixAllExpectation.md)

[ MatrixSingleExpectation ](MatrixSingleExpectation.md)

[ NotPresentExpectation ](NotPresentExpectation.md)

[ NumericExpectation ](NumericExpectation.md)

[ NumericExpressionExpectation ](NumericExpressionExpectation.md)

[ PresentExpectation ](PresentExpectation.md)

[ StringExpectation ](StringExpectation.md)

[ StringExpressionExpectation ](StringExpressionExpectation.md)

[ StringListExpectation ](StringListExpectation.md)

[ VectorAllExpectation ](VectorAllExpectation.md)

[ VectorSingleExpectation ](VectorSingleExpectation.md)

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

DTCListExpectation

- [C DTCListExpectation ](#ApiClient.DTCListExpectation)
  - [M AppendDtc ](#ApiClient.DTCListExpectation.AppendDtc)
  - [M AppendToleratedDtc ](#ApiClient.DTCListExpectation.AppendToleratedDtc)
  - [M ClearDtcList ](#ApiClient.DTCListExpectation.ClearDtcList)
  - [M ClearToleratedDtcList ](#ApiClient.DTCListExpectation.ClearToleratedDtcList)
  - [M Clone ](#ApiClient.DTCListExpectation.Clone)
  - [M GetDtcList ](#ApiClient.DTCListExpectation.GetDtcList)
  - [M GetDtcListExpression ](#ApiClient.DTCListExpectation.GetDtcListExpression)
  - [M GetRepresentation ](#ApiClient.DTCListExpectation.GetRepresentation)
  - [M GetToleratedDtcList ](#ApiClient.DTCListExpectation.GetToleratedDtcList)
  - [M GetToleratedDtcListExpression ](#ApiClient.DTCListExpectation.GetToleratedDtcListExpression)
  - [M IsExpectPresent ](#ApiClient.DTCListExpectation.IsExpectPresent)
  - [M IsTolerateAll ](#ApiClient.DTCListExpectation.IsTolerateAll)
  - [M SetDtcListExpression ](#ApiClient.DTCListExpectation.SetDtcListExpression)
  - [M SetExpectAbsent ](#ApiClient.DTCListExpectation.SetExpectAbsent)
  - [M SetExpectPresent ](#ApiClient.DTCListExpectation.SetExpectPresent)
  - [M SetRepresentation ](#ApiClient.DTCListExpectation.SetRepresentation)
  - [M SetTolerateAll ](#ApiClient.DTCListExpectation.SetTolerateAll)
  - [M SetToleratedDtcListExpression ](#ApiClient.DTCListExpectation.SetToleratedDtcListExpression)

# DTCListExpectation[¶](#dtclistexpectation "Link to this heading")

*class* DTCListExpectation[¶](#ApiClient.DTCListExpectation "Link to this definition")  
Returned by

- [`ExpectationApi.CreateDTCListExpectation`](../ExpectationApi.md#ApiClient.ExpectationApi.CreateDTCListExpectation "ApiClient.ExpectationApi.CreateDTCListExpectation (Python method) — Creates a DTC list expectation.")

AppendDtc(*[dtc](#ApiClient.DTCListExpectation.AppendDtc.dtc "ApiClient.DTCListExpectation.AppendDtc.dtc (Python parameter) — The DTC to append, in the format specified via SetRepresentation()")*)[¶](#ApiClient.DTCListExpectation.AppendDtc "Link to this definition")  
Appends the given DTC to the DTC list.

Info

if a numeric representation is chosen, you must provide a hex string with prefix 0x.

Parameters:  dtc : str[¶](#ApiClient.DTCListExpectation.AppendDtc.dtc "Permalink to this definition")  
The DTC to append, in the format specified via [`SetRepresentation()`](#ApiClient.DTCListExpectation.SetRepresentation "ApiClient.DTCListExpectation.SetRepresentation (Python method) — Sets the DTC representation.")

AppendToleratedDtc(*[dtc](#ApiClient.DTCListExpectation.AppendToleratedDtc.dtc "ApiClient.DTCListExpectation.AppendToleratedDtc.dtc (Python parameter) — The DTC to append, in the format specified via SetRepresentation()")*)[¶](#ApiClient.DTCListExpectation.AppendToleratedDtc "Link to this definition")  
Appends the given DTC to the list of tolerated DTCs.

This automatically disables “tolerate all”.

Info

if a numeric representation is chosen, you must provide a hex string with prefix 0x.

Parameters:  dtc : str[¶](#ApiClient.DTCListExpectation.AppendToleratedDtc.dtc "Permalink to this definition")  
The DTC to append, in the format specified via [`SetRepresentation()`](#ApiClient.DTCListExpectation.SetRepresentation "ApiClient.DTCListExpectation.SetRepresentation (Python method) — Sets the DTC representation.")

ClearDtcList()[¶](#ApiClient.DTCListExpectation.ClearDtcList "Link to this definition")  
Removes all DTCs from the DTC list.

ClearToleratedDtcList()[¶](#ApiClient.DTCListExpectation.ClearToleratedDtcList "Link to this definition")  
Removes all DTCs from the list of tolerated DTCs.

Clone()[¶](#ApiClient.DTCListExpectation.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`DTCListExpectation`](#ApiClient.DTCListExpectation "ApiClient.DTCListExpectation (Python class) — ExpectationApi.CreateDTCListExpectation")

GetDtcList()[¶](#ApiClient.DTCListExpectation.GetDtcList "Link to this definition")  
Retrieves the list of expected DTCs.

Returns:  List of expected DTCs

Return type:  list[str]

GetDtcListExpression()[¶](#ApiClient.DTCListExpectation.GetDtcListExpression "Link to this definition")  
Returns the DTC list expression.

Returns:  DTC list expression

Return type:  str

GetRepresentation()[¶](#ApiClient.DTCListExpectation.GetRepresentation "Link to this definition")  
Returns the DTC representation.

Returns:  name of the representation for DTCs

Return type:  str

GetToleratedDtcList()[¶](#ApiClient.DTCListExpectation.GetToleratedDtcList "Link to this definition")  
Retrieves the list of tolerated DTCs.

Returns:  List of tolerated DTCs

Return type:  list[str]

GetToleratedDtcListExpression()[¶](#ApiClient.DTCListExpectation.GetToleratedDtcListExpression "Link to this definition")  
Returns the tolerated DTC list expression.

Returns:  tolerated DTC list expression

Return type:  str

IsExpectPresent()[¶](#ApiClient.DTCListExpectation.IsExpectPresent "Link to this definition")  
Returns whether the specified list of DTCs will be expected to be present (True) or absent (False)

Returns:  Specified DTCs will be expected to be present (True) or absent (False)

Return type:  bool

IsTolerateAll()[¶](#ApiClient.DTCListExpectation.IsTolerateAll "Link to this definition")  
Returns whether all other DTCs (which are not in the DTC list) should be tolerated.

Returns:  tolerate all (True) or only those in the tolerated list (False)

Return type:  bool

SetDtcListExpression(*[dtcListExpression](#ApiClient.DTCListExpectation.SetDtcListExpression.dtcListExpression "ApiClient.DTCListExpectation.SetDtcListExpression.dtcListExpression (Python parameter) — DTC list expression")*)[¶](#ApiClient.DTCListExpectation.SetDtcListExpression "Link to this definition")  
Sets the DTC list expression.

Parameters:  dtcListExpression : str[¶](#ApiClient.DTCListExpectation.SetDtcListExpression.dtcListExpression "Permalink to this definition")  
DTC list expression

SetExpectAbsent()[¶](#ApiClient.DTCListExpectation.SetExpectAbsent "Link to this definition")  
Declares that the DTCs specified via [`AppendDtc()`](#ApiClient.DTCListExpectation.AppendDtc "ApiClient.DTCListExpectation.AppendDtc (Python method) — Appends the given DTC to the DTC list.") as well [`SetDtcListExpression()`](#ApiClient.DTCListExpectation.SetDtcListExpression "ApiClient.DTCListExpectation.SetDtcListExpression (Python method) — Sets the DTC list expression.") are expected to be absent.

SetExpectPresent()[¶](#ApiClient.DTCListExpectation.SetExpectPresent "Link to this definition")  
Declares that the DTCs specified via [`AppendDtc()`](#ApiClient.DTCListExpectation.AppendDtc "ApiClient.DTCListExpectation.AppendDtc (Python method) — Appends the given DTC to the DTC list.") as well [`SetDtcListExpression()`](#ApiClient.DTCListExpectation.SetDtcListExpression "ApiClient.DTCListExpectation.SetDtcListExpression (Python method) — Sets the DTC list expression.") are expected to be present.

SetRepresentation(*[representation](#ApiClient.DTCListExpectation.SetRepresentation.representation "ApiClient.DTCListExpectation.SetRepresentation.representation (Python parameter) — Name of the representation for DTCs.")*)[¶](#ApiClient.DTCListExpectation.SetRepresentation "Link to this definition")  
Sets the DTC representation.

Parameters:  representation : str[¶](#ApiClient.DTCListExpectation.SetRepresentation.representation "Permalink to this definition")  
Name of the representation for DTCs. Possible values: - ‘Display Trouble Code including FTB ([PCBU]-Code)’ - ‘Display Trouble Code without FTB ([PCBU]-Code)’ - ‘Short Name’ - ‘Description’ - ‘Number (3 Byte)’ - ‘Number (2 Byte)’

SetTolerateAll()[¶](#ApiClient.DTCListExpectation.SetTolerateAll "Link to this definition")  
Declares that all all other DTCs (not mentioned in the DTC list) shall be tolerated.

This automatically clears the list and expression of tolerated DTCs

SetToleratedDtcListExpression(*[toleratedDtcListExpression](#ApiClient.DTCListExpectation.SetToleratedDtcListExpression.toleratedDtcListExpression "ApiClient.DTCListExpectation.SetToleratedDtcListExpression.toleratedDtcListExpression (Python parameter) — tolerated DTC list expression")*)[¶](#ApiClient.DTCListExpectation.SetToleratedDtcListExpression "Link to this definition")  
Sets the tolerated DTC list expression.

This automatically disables “tolerate all”.

Parameters:  toleratedDtcListExpression : str[¶](#ApiClient.DTCListExpectation.SetToleratedDtcListExpression.toleratedDtcListExpression "Permalink to this definition")  
tolerated DTC list expression

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
