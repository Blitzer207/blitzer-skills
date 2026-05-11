# Utility Examples[¶](#utility-examples "Link to this heading")

This page contains different examples of Utilities. The source code of those examples can be found in the ecu.test installation directory under `Help/APIDoc/ExampleUtilities`.

## TSLinSpaceExample[¶](#module-ExampleUtilities.LinspaceExample.TsLinspaceExample "Link to this heading")

*class* TsLinspaceExample[¶](#ExampleUtilities.LinspaceExample.TsLinspaceExample.TsLinspaceExample "Link to this definition")  
This is a small example on how a AXSUtility can be implemented.

ID *= 'dd7b2b14-7b18-4234-9758-9eacdebc6f40'*[¶](#ExampleUtilities.LinspaceExample.TsLinspaceExample.TsLinspaceExample.ID "Link to this definition")  
A universally unique identifier to make your utility unique. The ID should be generated automatically to be unique.

Type:  UUID

Note

Setting this field is **mandatory**

NAME *= 'TsLinspaceExample'*[¶](#ExampleUtilities.LinspaceExample.TsLinspaceExample.TsLinspaceExample.NAME "Link to this definition")  
The display name of your utility.

Type:  str

Note

Setting this field is **mandatory**

DESCRIPTION *= 'This is a small example of how an AXSUtility can be implemented (equidistant list).'*[¶](#ExampleUtilities.LinspaceExample.TsLinspaceExample.TsLinspaceExample.DESCRIPTION "Link to this definition")  
A short description of your utility that is displayed in the utilities tab.

Type:  str

Note

Setting this field is **optional**

*classmethod* GetInterface()[¶](#ExampleUtilities.LinspaceExample.TsLinspaceExample.TsLinspaceExample.GetInterface "Link to this definition")  
Return an interface which specifies our arguments.

OnPreProcess(*testEngine*)[¶](#ExampleUtilities.LinspaceExample.TsLinspaceExample.TsLinspaceExample.OnPreProcess "Link to this definition")  
Overwrite to implement pre execution behavior. This methode is called before running the testcase.

OnRun(*userExcInst*, *testEngine*)[¶](#ExampleUtilities.LinspaceExample.TsLinspaceExample.TsLinspaceExample.OnRun "Link to this definition")  
Implementation of the simple calculation.

GetReportInfos()[¶](#ExampleUtilities.LinspaceExample.TsLinspaceExample.TsLinspaceExample.GetReportInfos "Link to this definition")  
Overwrite to add custom information in the test report.

Returns:  Dictionary containing key value pairs to be shown in the report

Return type:  dict{str:str}

## RunDialogExample[¶](#module-ExampleUtilities.ShowDialogExample.RunDialogExample "Link to this heading")

*class* RunDialogExample[¶](#ExampleUtilities.ShowDialogExample.RunDialogExample.RunDialogExample "Link to this definition")  
OnOk(*event*)[¶](#ExampleUtilities.ShowDialogExample.RunDialogExample.RunDialogExample.OnOk "Link to this definition")  

SetValue(*name*, *value*)[¶](#ExampleUtilities.ShowDialogExample.RunDialogExample.RunDialogExample.SetValue "Link to this definition")  

GetValue(*name*)[¶](#ExampleUtilities.ShowDialogExample.RunDialogExample.RunDialogExample.GetValue "Link to this definition")  

## TsShowDialogExample[¶](#module-ExampleUtilities.ShowDialogExample.TsShowDialogExample "Link to this heading")

*class* TsShowDialogExample[¶](#ExampleUtilities.ShowDialogExample.TsShowDialogExample.TsShowDialogExample "Link to this definition")  
ID *= '4c69cb5e-233a-11dd-b764-001c23232a0e'*[¶](#ExampleUtilities.ShowDialogExample.TsShowDialogExample.TsShowDialogExample.ID "Link to this definition")  
A universally unique identifier to make your utility unique. The ID should be generated automatically to be unique.

Type:  UUID

Note

Setting this field is **mandatory**

NAME *= 'ShowDialogExample'*[¶](#ExampleUtilities.ShowDialogExample.TsShowDialogExample.TsShowDialogExample.NAME "Link to this definition")  
The display name of your utility.

Type:  str

Note

Setting this field is **mandatory**

DESCRIPTION *= 'Demonstrates how to show and interact with a dialog during runtime.'*[¶](#ExampleUtilities.ShowDialogExample.TsShowDialogExample.TsShowDialogExample.DESCRIPTION "Link to this definition")  
A short description of your utility that is displayed in the utilities tab.

Type:  str

Note

Setting this field is **optional**

UtilityReport(*reportEngine*, *reportDataObject*)[¶](#ExampleUtilities.ShowDialogExample.TsShowDialogExample.TsShowDialogExample.UtilityReport "Link to this definition")  
The count value of the `RunDialogExample` that was shown during test execution is displayed in the test report.

OnRun(*reportDataObject*)[¶](#ExampleUtilities.ShowDialogExample.TsShowDialogExample.TsShowDialogExample.OnRun "Link to this definition")  
Here is demonstrated how a dialog can be shown during test execution. Due to execution in a separate thread the [`ThreadDialog`](user-utility.md#tts.lib.gui.dialogs.ThreadDialog.ThreadDialog "tts.lib.gui.dialogs.ThreadDialog.ThreadDialog") class has to be used.

## TsSimpleCalculationExample[¶](#module-ExampleUtilities.SimpleCalculationExample.TsSimpleCalculationExample "Link to this heading")

*class* TsSimpleCalculationExample[¶](#ExampleUtilities.SimpleCalculationExample.TsSimpleCalculationExample.TsSimpleCalculationExample "Link to this definition")  
This is a small example on how a AXSUtility should be implemented.

ID *= '5c256353-1dc4-4651-8faf-af0e58dfe636'*[¶](#ExampleUtilities.SimpleCalculationExample.TsSimpleCalculationExample.TsSimpleCalculationExample.ID "Link to this definition")  
A universally unique identifier to make your utility unique. The ID should be generated automatically to be unique.

Type:  UUID

Note

Setting this field is **mandatory**

NAME *= 'SimpleCalculationExample'*[¶](#ExampleUtilities.SimpleCalculationExample.TsSimpleCalculationExample.TsSimpleCalculationExample.NAME "Link to this definition")  
The display name of your utility.

Type:  str

Note

Setting this field is **mandatory**

DESCRIPTION *= 'This is a small example on how an AXSUtility should be implemented (simple calculation).'*[¶](#ExampleUtilities.SimpleCalculationExample.TsSimpleCalculationExample.TsSimpleCalculationExample.DESCRIPTION "Link to this definition")  
A short description of your utility that is displayed in the utilities tab.

Type:  str

Note

Setting this field is **optional**

Addition(*a*, *b*)[¶](#ExampleUtilities.SimpleCalculationExample.TsSimpleCalculationExample.TsSimpleCalculationExample.Addition "Link to this definition")  
Addition of 2 values.

Subtraction(*a*, *b*)[¶](#ExampleUtilities.SimpleCalculationExample.TsSimpleCalculationExample.TsSimpleCalculationExample.Subtraction "Link to this definition")  
Subtraction of 2 values.

Multiplication(*a*, *b*)[¶](#ExampleUtilities.SimpleCalculationExample.TsSimpleCalculationExample.TsSimpleCalculationExample.Multiplication "Link to this definition")  
Multiplication of 2 values.

Division(*a*, *b*)[¶](#ExampleUtilities.SimpleCalculationExample.TsSimpleCalculationExample.TsSimpleCalculationExample.Division "Link to this definition")  
Division of 2 values.

*static* GetBitmap()[¶](#ExampleUtilities.SimpleCalculationExample.TsSimpleCalculationExample.TsSimpleCalculationExample.GetBitmap "Link to this definition")  
Return the utility-icon.

Return type:  wx.Bitmap

*classmethod* GetInterface()[¶](#ExampleUtilities.SimpleCalculationExample.TsSimpleCalculationExample.TsSimpleCalculationExample.GetInterface "Link to this definition")  
Return an interface which specifies our arguments.

OnRun(*userExcInst*, *testEngine*)[¶](#ExampleUtilities.SimpleCalculationExample.TsSimpleCalculationExample.TsSimpleCalculationExample.OnRun "Link to this definition")  
Implementation of the simple calculation.

GetReportInfos()[¶](#ExampleUtilities.SimpleCalculationExample.TsSimpleCalculationExample.TsSimpleCalculationExample.GetReportInfos "Link to this definition")  
Overwrite to add custom information in the test report.

Returns:  Dictionary containing key value pairs to be shown in the report

Return type:  dict{str:str}

## DlgSmallExample[¶](#module-ExampleUtilities.SmallExample.DlgSmallExample "Link to this heading")

*class* DlgSmallExample[¶](#ExampleUtilities.SmallExample.DlgSmallExample.DlgSmallExample "Link to this definition")  
OnCmdCancelButton(*event*)[¶](#ExampleUtilities.SmallExample.DlgSmallExample.DlgSmallExample.OnCmdCancelButton "Link to this definition")  

OnCmdOkButton(*event*)[¶](#ExampleUtilities.SmallExample.DlgSmallExample.DlgSmallExample.OnCmdOkButton "Link to this definition")  

## TsSmallExample[¶](#module-ExampleUtilities.SmallExample.TsSmallExample "Link to this heading")

*class* TsSmallExample[¶](#ExampleUtilities.SmallExample.TsSmallExample.TsSmallExample "Link to this definition")  
This is a small example on how a utility should be implemented.

ID *= '2dcc6e40-3859-11dd-82ff-000b5d5f5cc8'*[¶](#ExampleUtilities.SmallExample.TsSmallExample.TsSmallExample.ID "Link to this definition")  
A universally unique identifier to make your utility unique. The ID should be generated automatically to be unique.

Type:  UUID

Note

Setting this field is **mandatory**

NAME *= 'SmallExample'*[¶](#ExampleUtilities.SmallExample.TsSmallExample.TsSmallExample.NAME "Link to this definition")  
The display name of your utility.

Type:  str

Note

Setting this field is **mandatory**

DESCRIPTION *= 'This is a small example that copies the value of one variable to another.'*[¶](#ExampleUtilities.SmallExample.TsSmallExample.TsSmallExample.DESCRIPTION "Link to this definition")  
A short description of your utility that is displayed in the utilities tab.

Type:  str

Note

Setting this field is **optional**

SERIALIZE*: dict[str, tuple[str, str] | tuple[str, str, Any]] = {'varFrom': ('VARIABLENAME-FROM', 'string'), 'varTo': ('VARIABLENAME-TO', 'string')}*[¶](#ExampleUtilities.SmallExample.TsSmallExample.TsSmallExample.SERIALIZE "Link to this definition")  
Here the two instance variables are declared for serialization.

UtilityInit()[¶](#ExampleUtilities.SmallExample.TsSmallExample.TsSmallExample.UtilityInit "Link to this definition")  
Initialize the instance variables for the names of the two ecu.test variables used in this example.

UtilityReport(*reportEngine*, *reportDataObject*)[¶](#ExampleUtilities.SmallExample.TsSmallExample.TsSmallExample.UtilityReport "Link to this definition")  
Specifies how the runtime data and other informations about this teststep are displayed in the test report.

GetDialog()[¶](#ExampleUtilities.SmallExample.TsSmallExample.TsSmallExample.GetDialog "Link to this definition")  
Returs the configuration dialog object of the Utility. The dialog needs a reference to the teststep for getting and setting the teststep data.

Return type:  [`DlgSmallExample`](#ExampleUtilities.SmallExample.DlgSmallExample.DlgSmallExample "ExampleUtilities.SmallExample.DlgSmallExample.DlgSmallExample")

Returns:  Dialog object

GetUsedVariableNames()[¶](#ExampleUtilities.SmallExample.TsSmallExample.TsSmallExample.GetUsedVariableNames "Link to this definition")  
Overwritten to specify the used variable names.

Return type:  list

Returns:  List of variable names used by this test step.

OnRun(*reportDataObject*)[¶](#ExampleUtilities.SmallExample.TsSmallExample.TsSmallExample.OnRun "Link to this definition")  
Here the value from one to another variable is copied and the copied value is stored in [`RdoUserUtility`](user-utility.md#tts.testExecution.api.UserUtility.RdoUserUtility "tts.testExecution.api.UserUtility.RdoUserUtility") to be available later on in the [`UtilityReport()`](#ExampleUtilities.SmallExample.TsSmallExample.TsSmallExample.UtilityReport "ExampleUtilities.SmallExample.TsSmallExample.TsSmallExample.UtilityReport") method.
