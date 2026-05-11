# UserUtility API[¶](#userutility-api "Link to this heading")

## AXS-Utility[¶](#axs-utility "Link to this heading")

*class* TsAXSUtility[¶](#tts.testExecution.api.UserUtility.TsAXSUtility "Link to this definition")  
This is the base class for user defined mappable test steps called AXSUtilities. It’s possible to map TsAXSUtility-derivered utilities on other interface-based test steps like keywords. When inserting this utility it will be default-mapped on itself. When implementing you have to define an interface which specifies the arguments and return values of your utility. ecu.test will create an suitable dialog based on this interface automatically. Even the reporting is handled automatically. To implement the logic overwrite the OnRun().

Some fields and methods *must* be overridden (**mandatory**), others *may* be overridden (**optional**). There are also methods that are only to be called by the user implementation and should not be overridden (those without a note).

DESCRIPTION *= ''*[¶](#tts.testExecution.api.UserUtility.TsAXSUtility.DESCRIPTION "Link to this definition")  
A short description of your utility that is displayed in the utilities tab.

Type:  str

Note

Setting this field is **optional**

ID *= None*[¶](#tts.testExecution.api.UserUtility.TsAXSUtility.ID "Link to this definition")  
A universally unique identifier to make your utility unique. The ID should be generated automatically to be unique.

Type:  UUID

Note

Setting this field is **mandatory**

NAME *= ''*[¶](#tts.testExecution.api.UserUtility.TsAXSUtility.NAME "Link to this definition")  
The display name of your utility.

Type:  str

Note

Setting this field is **mandatory**

api *= None*[¶](#tts.testExecution.api.UserUtility.TsAXSUtility.api "Link to this definition")  
Access to the internal ecu.test API.

Type:  [`Api`](../general_api/api.md#tts.core.api.internalApi.Api.Api "tts.core.api.internalApi.Api.Api")

*static* GetBitmap()[¶](#tts.testExecution.api.UserUtility.TsAXSUtility.GetBitmap "Link to this definition")  
Return the utility-icon.

Return type:  wx.Bitmap

*classmethod* GetDescription()[¶](#tts.testExecution.api.UserUtility.TsAXSUtility.GetDescription "Link to this definition")  
Return the description of your utility. This description should be specified setting the class variable [`DESCRIPTION`](#tts.testExecution.api.UserUtility.TsAXSUtility.DESCRIPTION "tts.testExecution.api.UserUtility.TsAXSUtility.DESCRIPTION").

Return type:  str

*classmethod* GetId()[¶](#tts.testExecution.api.UserUtility.TsAXSUtility.GetId "Link to this definition")  
Checks and returns the universally unique identifier of the utility. This identifier should be specified setting the class variable [`ID`](#tts.testExecution.api.UserUtility.TsAXSUtility.ID "tts.testExecution.api.UserUtility.TsAXSUtility.ID").

Return type:  UUID

*classmethod* GetInterface()[¶](#tts.testExecution.api.UserUtility.TsAXSUtility.GetInterface "Link to this definition")  
Return an interface which specifies your input and output values.

*classmethod* GetName()[¶](#tts.testExecution.api.UserUtility.TsAXSUtility.GetName "Link to this definition")  
Return the name of your utility. This name should be specified setting the class variable [`NAME`](#tts.testExecution.api.UserUtility.TsAXSUtility.NAME "tts.testExecution.api.UserUtility.TsAXSUtility.NAME").

Return type:  str

GetReportInfos()[¶](#tts.testExecution.api.UserUtility.TsAXSUtility.GetReportInfos "Link to this definition")  
Implement this method to add custom information in the test report.

Returns:  Dictionary containing key value pairs to be shown in the report

Return type:  dict{str:str}

Note

Overriding this method is **optional**

OnPostProcess(*testEngine*)[¶](#tts.testExecution.api.UserUtility.TsAXSUtility.OnPostProcess "Link to this definition")  
Implement this method to specify post execution behavior. This method is called after the testcase is completed.

Note

Overriding this method is **optional**

OnPreProcess(*testEngine*)[¶](#tts.testExecution.api.UserUtility.TsAXSUtility.OnPreProcess "Link to this definition")  
Implement this method to specify pre execution behavior without access to arguments. This method is called before running the testcase.

Note

Overriding this method is **optional**

OnPreProcessEx(*userExcInst*, *testEngine*)[¶](#tts.testExecution.api.UserUtility.TsAXSUtility.OnPreProcessEx "Link to this definition")  
Implement this method to specify pre execution behavior with access to arguments. This method is called before running the test case.

Parameters:  **userExcInst** ([`UserExecInst`](#tts.core.axs.realization.UserExecInst.UserExecInst "tts.core.axs.realization.UserExecInst.UserExecInst")) – Access to the arguments. Only constant arguments are accessible.

Note

Overriding this method is **optional**

OnRun(*userExcInst*, *testEngine*)[¶](#tts.testExecution.api.UserUtility.TsAXSUtility.OnRun "Link to this definition")  
Implement this method to specify execution behavior. This method is called during the execution of the test case. If there are calculations, that are not necessary to be calculated in this method, put them in to the pre- or post process. That gives the real process more performance to do time-critical operations well.

Parameters:  **userExcInst** ([`UserExecInst`](#tts.core.axs.realization.UserExecInst.UserExecInst "tts.core.axs.realization.UserExecInst.UserExecInst")) – Access to the arguments and return values.

Note

Overriding this method is **mandatory**

UtilityInit()[¶](#tts.testExecution.api.UserUtility.TsAXSUtility.UtilityInit "Link to this definition")  
Implement this method for initialization of your utility. This method is called, when creating an instance of this class.

Note

Overriding this method is **optional**

*class* UserExecInst[¶](#tts.core.axs.realization.UserExecInst.UserExecInst "Link to this definition")  
Use this class to read the argument and write the return values of your UserUtility.

GetArgumentValue(*name*)[¶](#tts.core.axs.realization.UserExecInst.UserExecInst.GetArgumentValue "Link to this definition")  
Get the argument value by name.

Parameters:  **name** (*str*) – name of the argument value.

Returns:  Returns the respective argument.

Return type:  `Value`

Raises:  
- **AttributeError** – The specified argument name does not exist.

- **ExpressionVarError** – During PreProcess: the specified argument value is given in the test step in terms of test case variables, which are not accessible during PreProcess

GetRawArgumentValue(*name*)[¶](#tts.core.axs.realization.UserExecInst.UserExecInst.GetRawArgumentValue "Link to this definition")  
Get the argument value by name.

Parameters:  **name** (*str*) – name of the argument value.

Returns:  Returns the respective argument.

Return type:  int, float or str

Raises:  
**AttributeError** – The specified argument name does not exist.

SetRawReturnValue(*name*, *rawvalue*)[¶](#tts.core.axs.realization.UserExecInst.UserExecInst.SetRawReturnValue "Link to this definition")  
Sets the return value specified by name.

Parameters:  - **name** (*str*) – name of the return value.

- **value** (*int,* *float* *or* *str*) – argument value to set

Raises:  
**AttributeError** – The specified return name does not exist.

SetReturnValue(*name*, *value*)[¶](#tts.core.axs.realization.UserExecInst.UserExecInst.SetReturnValue "Link to this definition")  
Sets the return value specified by name.

Parameters:  - **name** (*str*) – name of the return value.

- **value** (`Value`) – argument value to set

Raises:  
**AttributeError** – The specified return name does not exist.

## Helper classes[¶](#helper-classes "Link to this heading")

UserUtility.TimeoutProxy(*name=None*, *timeout=3*)[¶](#tts.testExecution.api.UserUtility.TimeoutProxy "Link to this definition")  
A factory function that returns a new TimeoutProxy object. Purpose of such proxy is to abort synchronous calls to methods of the proxied object when they take longer than a certain timeout. There is no restriction on the kind of object to be proxied. The timeout value can be queried/ set by PrxGetTimeout()/ PrxSetTimeout(). Furthermore the proxy’s state can be retrieved by PrxGetState(). Since each TimeoutProxy instance internally uses its own dispatcher thread it must be explicitly destroy when it is not needed any more.

Parameters:  - **subject** (*object*) – Object to be proxied.

- **name** (*str*) – Name of the proxy (used for logging purposes).

- **timeout** (*int*) – Timeout value used for calls to the proxied object. “None” means “no timeout” (may result in infinite waiting like without proxy).

*class* ProxyError[¶](#tts.testExecution.api.UserUtility.ProxyError "Link to this definition")  
Exception class used by the TimeoutProxy to report errors (e.g. timeout errors).

*exception* ThreadDialogException(*msg='Unbekannter Fehler'*)[¶](#tts.lib.gui.dialogs.ThreadDialog.ThreadDialogException "Link to this definition")  
Error in livecycle of dialog.

*class* ThreadDialog[¶](#tts.lib.gui.dialogs.ThreadDialog.ThreadDialog "Link to this definition")  
Allows to display a dialog from within a thread. As soon as this object has been created, the dialog is initialized. States and the functions that may be called:

0: uninitialized

1: initialized (initial state)  
- ShowModal -> showing

- WaitForDialog -> initialized

- IsShown -> initialized

- SetValue -> initialized

- GetValue -> initialized

- Destroy -> uninitialized

2: showing  
- IsShown -> showing

- WaitForDialog -> initialized (waiting for dialog)

- EndModal -> initialized (terminating dialog)

- SetValue -> showing

- GetValue -> showing

- -> initialized (If the dialog is terminated,  
  it automatically returns to the initialized state)

- Destroy -> uninitialized

CallMethod(*methodName*, *\*args*, *\*\*keyargs*)[¶](#tts.lib.gui.dialogs.ThreadDialog.ThreadDialog.CallMethod "Link to this definition")  
Calls a method on the dialog object.

Parameters:  - **methodName** (*str*) – Name of the method

- **args** (*Liste*) – Arguments of the method

- **keyargs** (*dict*) – Arguments of the method

Destroy()[¶](#tts.lib.gui.dialogs.ThreadDialog.ThreadDialog.Destroy "Link to this definition")  
Destroys the dialogue and releases resources used by it. After that, no other method of the thread dialog can be called.

EndModal(*id*)[¶](#tts.lib.gui.dialogs.ThreadDialog.ThreadDialog.EndModal "Link to this definition")  
Prompts the dialog to close and then waits for it to happen using L{WaitForDialog}.

GetValue(*name*)[¶](#tts.lib.gui.dialogs.ThreadDialog.ThreadDialog.GetValue "Link to this definition")  
Calls the GetValue function in the dialog. The call blocks until the result from the dialog is available.

Parameters:  **name** (*str*) – Name of the value to be read.

Returns:  The read value.

Return type:  object

GetValues()[¶](#tts.lib.gui.dialogs.ThreadDialog.ThreadDialog.GetValues "Link to this definition")  
Calls the GetValues function in the dialog. The call blocks until the result from the dialog is available.

Returns:  The read values.

Return type:  object

IsShown()[¶](#tts.lib.gui.dialogs.ThreadDialog.ThreadDialog.IsShown "Link to this definition")  
Returns:  True, if the dialog is still displayed. False, if it is already closed.

Return type:  bool

SetValue(*name*, *value*)[¶](#tts.lib.gui.dialogs.ThreadDialog.ThreadDialog.SetValue "Link to this definition")  
Calls the SetValue function in the dialog. The call is non-blocking.

Parameters:  - **name** (*str*) – Name of the value to be set.

- **value** (*object*) – The value itself. deepcopy is called on the value. Therefore, values that are too complex should not be passed.

ShowModal()[¶](#tts.lib.gui.dialogs.ThreadDialog.ThreadDialog.ShowModal "Link to this definition")  
Displays the dialog. If a dialog is to be displayed a second time within a thread dialog, it must first be checked using IsShown whether the dialog is still displayed.

WaitForDialog()[¶](#tts.lib.gui.dialogs.ThreadDialog.ThreadDialog.WaitForDialog "Link to this definition")  
Waiting for the dialog to close.

Returns:  ID with which EndModal was called in the dialog or in the thread dialog.

Return type:  int

`\_\_init\_\_`(*dlgClass*, *\*args*, *\*\*kwargs*)[¶](#tts.lib.gui.dialogs.ThreadDialog.ThreadDialog.__init__ "Link to this definition")  
Initializes the dialog. The first parameter is the class of the dialog. The following parameters are the parameters of the dialog and are passed to the constructor of the dialog class.

## UserUtility[¶](#userutility "Link to this heading")

*class* TsUserUtility[¶](#tts.testExecution.api.UserUtility.TsUserUtility "Link to this definition")  
This is the base class for user defined test steps called user utilities. All user utilities should be derived form this class. It defines specific methods that are called during test step editing and test execution. The required behavior of a user utility is implemented by overwriting these methods. Furthermore TsUserUtility offers a couple of methods that provide access to test case variables and other test case properties. These might be quite helpful when implementing a user utility.

Some fields and methods *must* be overridden (**mandatory**), others *may* be overridden (**optional**). There are also methods that are only to be called by the user implementation and should not be overridden (those without a note).

DESCRIPTION *= ''*[¶](#tts.testExecution.api.UserUtility.TsUserUtility.DESCRIPTION "Link to this definition")  
A short description of your utility that is displayed in the utilities tab.

Type:  str

Note

Setting this field is **optional**

ID *= None*[¶](#tts.testExecution.api.UserUtility.TsUserUtility.ID "Link to this definition")  
A universally unique identifier to make your utility unique. The ID should be generated automatically to be unique.

Type:  UUID

Note

Setting this field is **mandatory**

NAME *= ''*[¶](#tts.testExecution.api.UserUtility.TsUserUtility.NAME "Link to this definition")  
The display name of your utility.

Type:  str

Note

Setting this field is **mandatory**

SERIALIZE*: dict[str, tuple[str, str] | tuple[str, str, Any]] = {}*[¶](#tts.testExecution.api.UserUtility.TsUserUtility.SERIALIZE "Link to this definition")  
Declaration of the test step’s instance variables that are to be exported/ imported to/ from xml format (e.g. during saving/ loading a package). The declaration is a (optionally empty) dictionary containing one item for each instance variable to be exported resp. imported. Example:

    SERIALIZE = {
                    "foo": ("FOO-VAR", "integer", 23),
                    "bar": ("BAR", "string"),
                    "params: ("PARAMETERS", "list")
                }

The declaration item’s key must match the name of the corresponding instance variable (e.g. for an instance variable self.foo the item’s key must be “foo”). The item’s value must be a tuple containing 2 elements at least. So the general syntax for a declaration item is:

    <variable name>: (<variable alias>, <type alias>, [default value])

Syntax and meaning of the tuple’s elements are:  
- **\<variable alias\>** declares the name of the xml element that is used for the variable’s xml representation.

- **\<type alias\>** keyword specifying the python variable’s type. The following table gives all keywords and their corresponding python type respectively:

  > - `boolean`: bool
  >
  > - `integer`: int
  >
  > - `long`: long
  >
  > - `float`: float
  >
  > - `string`: str
  >
  > - `str`: str
  >
  > - `list`: list
  >
  > - `dict`: dict

PLEASE NOTE: Keys of dictionaries being (de-)serialized must be strings. Furthermore values of dictionaries and lists are required to be of type bool, int, long, float, str, list or dict. The same restrictions apply to embedded lists and dictionaries.

- **\<default value\>** is an optional element. It specifies the variable’s default value. If the variable’s value equals its default value during export the variable is not exported at all. Conversely, the variable is assigned its default value during import if the xml data does not provide an value for the variable.

Type:  dict

Note

Setting this field is **optional**

api *= None*[¶](#tts.testExecution.api.UserUtility.TsUserUtility.api "Link to this definition")  
Access to the internal ecu.test API.

Type:  [`Api`](../general_api/api.md#tts.core.api.internalApi.Api.Api "tts.core.api.internalApi.Api.Api")

*static* GetBitmap()[¶](#tts.testExecution.api.UserUtility.TsUserUtility.GetBitmap "Link to this definition")  
Return the utility-icon.

Return type:  wx.Bitmap

*classmethod* GetDescription()[¶](#tts.testExecution.api.UserUtility.TsUserUtility.GetDescription "Link to this definition")  
Return the description of your utility. This description should be specified setting the class variable [`DESCRIPTION`](#tts.testExecution.api.UserUtility.TsUserUtility.DESCRIPTION "tts.testExecution.api.UserUtility.TsUserUtility.DESCRIPTION").

Return type:  str

GetDialog()[¶](#tts.testExecution.api.UserUtility.TsUserUtility.GetDialog "Link to this definition")  
Implement this method to return the configuration dialog of your utility. The dialog should set the test step data.

Return type:  wx.Dialog or None

Note

Overriding this method is **optional**

GetError()[¶](#tts.testExecution.api.UserUtility.TsUserUtility.GetError "Link to this definition")  
Liefert eine Liste von Fehlermeldungen. Diese darf auch Nones enthalten, welche zu einem späteren Zeitpunkt herausgefiltert werden müssen.

GetExpressions()[¶](#tts.testExecution.api.UserUtility.TsUserUtility.GetExpressions "Link to this definition")  
Implement this method to specify the used expressions.

Return type:  list

Returns:  List of expressions used by this test step.

Note

Overriding this method is **optional**

*classmethod* GetFormatRev()[¶](#tts.testExecution.api.UserUtility.TsUserUtility.GetFormatRev "Link to this definition")  
The format revision identifies structure and type of your test step data that is saved in package files. Do not return any other value than 0 if you do not also provide for conversion of outdated versions into the current one. It is recommended keeping changes in your test step data structure compatible with former versions and always returning 0 for the format revision.

*classmethod* GetId()[¶](#tts.testExecution.api.UserUtility.TsUserUtility.GetId "Link to this definition")  
Checks and returns the universally unique identifier of the utility. This identifier should be specified setting the class variable [`ID`](#tts.testExecution.api.UserUtility.TsUserUtility.ID "tts.testExecution.api.UserUtility.TsUserUtility.ID").

Return type:  UUID

*classmethod* GetName()[¶](#tts.testExecution.api.UserUtility.TsUserUtility.GetName "Link to this definition")  
Return the name of your utility. This name should be specified setting the class variable [`NAME`](#tts.testExecution.api.UserUtility.TsUserUtility.NAME "tts.testExecution.api.UserUtility.TsUserUtility.NAME").

Return type:  str

GetUtilityColumnText(*column*)[¶](#tts.testExecution.api.UserUtility.TsUserUtility.GetUtilityColumnText "Link to this definition")  
Implement this method to fill the columns in test case editor.

Parameters:  **column** (*int*) – The column number for which the content is queried

Return type:  str

Returns:  Column text.

Note

Overriding this method is **optional**

GetVariableValue(*name*)[¶](#tts.testExecution.api.UserUtility.TsUserUtility.GetVariableValue "Link to this definition")  
Returns the current value for the given test case variable name.

Parameters:  **name** (*str*) – Name of test case variable to query.

Returns:  Test case variable’s current value.

Return type:  any

IsExistingVariable(*name*)[¶](#tts.testExecution.api.UserUtility.TsUserUtility.IsExistingVariable "Link to this definition")  
Check if given test case variable exists in current package.

Return type:  bool

Returns:  True if test case variable exists else False.

OnPostProcess()[¶](#tts.testExecution.api.UserUtility.TsUserUtility.OnPostProcess "Link to this definition")  
Implement this method to specify post execution behavior. This method is called after the test case is completed.

Note

Overriding this method is **optional**

OnPreProcess()[¶](#tts.testExecution.api.UserUtility.TsUserUtility.OnPreProcess "Link to this definition")  
Implement this method to specify pre execution behavior. This method is called before running the test case.

Note

Overriding this method is **optional**

OnRun(*reportDataObject*)[¶](#tts.testExecution.api.UserUtility.TsUserUtility.OnRun "Link to this definition")  
Implement this method to specify execution behavior. This method is called during the execution of the test case. If there are calculations, that are not necessary to be calculated in this method, put them in to the pre- or postprocess. That gives the real process more performance to do time-critical operations well.

Parameters:  **reportDataObject** ([`RdoUserUtility`](#tts.testExecution.api.UserUtility.RdoUserUtility "tts.testExecution.api.UserUtility.RdoUserUtility")) – ReportDataObject to store report data.

Note

Overriding this method is **mandatory**

SetVariableValue(*name*, *value*)[¶](#tts.testExecution.api.UserUtility.TsUserUtility.SetVariableValue "Link to this definition")  
Set value of the given test case variable.

Parameters:  - **name** (*str*) – Name of test case variable to set.

- **value** (*any*) – Value.

UtilityInit()[¶](#tts.testExecution.api.UserUtility.TsUserUtility.UtilityInit "Link to this definition")  
Implement this method for initialization of your utility. This method is called, when creating an instance of this class.

Note

Overriding this method is **optional**

UtilityReport(*reportEngine*, *reportDataObject*)[¶](#tts.testExecution.api.UserUtility.TsUserUtility.UtilityReport "Link to this definition")  
Implement this method to influence how the results of your utility look like in the report.

Use `reportEngine.PReportItem` to get the [`ReportItem`](../general_api/apireport.md#tts.core.report.db.ReportItem.ReportItem "tts.core.report.db.ReportItem.ReportItem") object (Data to report should be written in this object):

    reportItem = reportEngine.PReportItem
    reportItem.PInfo = u"value copied"

Use `reportEngine.CreateTableEntity()` to create and get a [`TableEntity`](../general_api/apireport.md#tts.core.report.db.TableEntity.TableEntity "tts.core.report.db.TableEntity.TableEntity") object:

    table = reportEngine.CreateTableEntity()
    table.SetValue(0, 0, u"Variable value")
    table.SetValue(1, 0, reportDataObject.GetDataValue(u"copiedValue"))
    reportEngine.Insert(table)

Use `reportEngine.CreateTextEntity()` to create and get a [`TextEntity`](../general_api/apireport.md#tts.core.report.db.TextEntity.TextEntity "tts.core.report.db.TextEntity.TextEntity") object:

    text = reportEngine.CreateTextEntity()
    text.SetValue(u"a lot of text here ...")
    reportEngine.Insert(text)

To actually add the entity to the report, `reportEngine.Insert()` must be called

Parameters:  - **reportEngine** ([`ReportEngine`](#tts.core.report.engine.ReportEngine.ReportEngine "tts.core.report.engine.ReportEngine.ReportEngine")) – Runtime object to obtain [`ReportEngine`](#tts.core.report.engine.ReportEngine.ReportEngine "tts.core.report.engine.ReportEngine.ReportEngine"), [`TableEntity`](../general_api/apireport.md#tts.core.report.db.TableEntity.TableEntity "tts.core.report.db.TableEntity.TableEntity") and [`TableEntity`](../general_api/apireport.md#tts.core.report.db.TableEntity.TableEntity "tts.core.report.db.TableEntity.TableEntity")

- **reportDataObject** ([`RdoUserUtility`](#tts.testExecution.api.UserUtility.RdoUserUtility "tts.testExecution.api.UserUtility.RdoUserUtility")) – Runtime data are kept in this object.

Note

Overriding this method is **optional**

*class* RdoUserUtility[¶](#tts.testExecution.api.UserUtility.RdoUserUtility "Link to this definition")  
Class to store data and result state that are produced by executing a [`TsUserUtility`](#tts.testExecution.api.UserUtility.TsUserUtility "tts.testExecution.api.UserUtility.TsUserUtility") test step. Store data in this object during [`TsUserUtility.OnRun()`](#tts.testExecution.api.UserUtility.TsUserUtility.OnRun "tts.testExecution.api.UserUtility.TsUserUtility.OnRun") and retrieve it back during [`TsUserUtility.UtilityReport()`](#tts.testExecution.api.UserUtility.TsUserUtility.UtilityReport "tts.testExecution.api.UserUtility.TsUserUtility.UtilityReport").

GetDataValue(*name*)[¶](#tts.testExecution.api.UserUtility.RdoUserUtility.GetDataValue "Link to this definition")  
Retrieves stored data item.

Parameters:  **name** – Key under which the item was stored.

Returns:  None or the stored data item.

SetDataValue(*name*, *value*)[¶](#tts.testExecution.api.UserUtility.RdoUserUtility.SetDataValue "Link to this definition")  
Stores an arbitrary data item under a given name.

Parameters:  - **name** – Key for later retrieval of the stored data item.

- **value** – Data item to be stored.

*class* ReportEngine[¶](#tts.core.report.engine.ReportEngine.ReportEngine "Link to this definition")  
Interface to report database for filling during test execution.

PReportItem[¶](#tts.core.report.engine.ReportEngine.ReportEngine.PReportItem "Link to this definition")  
Returns the current ReportItem.

Returns:  the current ReportItem

Return type:  [`ReportItem`](../general_api/apireport.md#tts.core.report.db.ReportItem.ReportItem "tts.core.report.db.ReportItem.ReportItem")

CreateTableEntity(*name=None*)[¶](#tts.core.report.engine.ReportEngine.ReportEngine.CreateTableEntity "Link to this definition")  
Use this method to create a table for the current report item. Properties of the returned object can be modified by Set… methods corresponding to the documented Get… methods. Don’t forget to call [`ReportEngine.Insert()`](#tts.core.report.engine.ReportEngine.ReportEngine.Insert "tts.core.report.engine.ReportEngine.ReportEngine.Insert") to write the data object to the report database. [`ReportEngine.Update()`](#tts.core.report.engine.ReportEngine.ReportEngine.Update "tts.core.report.engine.ReportEngine.ReportEngine.Update") can be used to store modifications after the data object has already been inserted.

Parameters:  **name** (*str*) – a name to identify to the newly created TableEntity

Returns:  a TableEntity object

Return type:  [`TableEntity`](../general_api/apireport.md#tts.core.report.db.TableEntity.TableEntity "tts.core.report.db.TableEntity.TableEntity")

See also

[`Insert()`](#tts.core.report.engine.ReportEngine.ReportEngine.Insert "tts.core.report.engine.ReportEngine.ReportEngine.Insert")

CreateTextEntity(*name=None*)[¶](#tts.core.report.engine.ReportEngine.ReportEngine.CreateTextEntity "Link to this definition")  
Use this method create a text for the current report item. Properties of the returned object can be modified by Set… methods corresponding to the documented Get… methods. Don’t forget to call [`ReportEngine.Insert()`](#tts.core.report.engine.ReportEngine.ReportEngine.Insert "tts.core.report.engine.ReportEngine.ReportEngine.Insert") to write the data object to the report database. [`ReportEngine.Update()`](#tts.core.report.engine.ReportEngine.ReportEngine.Update "tts.core.report.engine.ReportEngine.ReportEngine.Update") can be used to store modifications after the data object has already been inserted.

Parameters:  **name** (*str*) – a name to identify to the newly created TextEntity

Returns:  a TextEntity object

Return type:  [`TextEntity`](../general_api/apireport.md#tts.core.report.db.TextEntity.TextEntity "tts.core.report.db.TextEntity.TextEntity")

See also

[`Insert()`](#tts.core.report.engine.ReportEngine.ReportEngine.Insert "tts.core.report.engine.ReportEngine.ReportEngine.Insert")

GetReportItem()[¶](#tts.core.report.engine.ReportEngine.ReportEngine.GetReportItem "Link to this definition")  
Returns the current ReportItem.

Returns:  the current ReportItem

Return type:  [`ReportItem`](../general_api/apireport.md#tts.core.report.db.ReportItem.ReportItem "tts.core.report.db.ReportItem.ReportItem")

Insert(*dbObj*, *restricted=False*)[¶](#tts.core.report.engine.ReportEngine.ReportEngine.Insert "Link to this definition")  
Use this method to insert the database object to the database.

Parameters:  **dbObj** (*object*) – The object to write back (e.g. [`TableEntity`](../general_api/apireport.md#tts.core.report.db.TableEntity.TableEntity "tts.core.report.db.TableEntity.TableEntity") or [`TextEntity`](../general_api/apireport.md#tts.core.report.db.TextEntity.TextEntity "tts.core.report.db.TextEntity.TextEntity")).

Update(*dbObj*, *restricted=False*)[¶](#tts.core.report.engine.ReportEngine.ReportEngine.Update "Link to this definition")  
Use this method to write back a modified database object to the report database after it has already been inserted.

Parameters:  **dbObj** (*object*) – The object to write back (e.g. [`TableEntity`](../general_api/apireport.md#tts.core.report.db.TableEntity.TableEntity "tts.core.report.db.TableEntity.TableEntity") or [`TextEntity`](../general_api/apireport.md#tts.core.report.db.TextEntity.TextEntity "tts.core.report.db.TextEntity.TextEntity")).

See also

[`CreateTableEntity()`](#tts.core.report.engine.ReportEngine.ReportEngine.CreateTableEntity "tts.core.report.engine.ReportEngine.ReportEngine.CreateTableEntity"), [`CreateTextEntity()`](#tts.core.report.engine.ReportEngine.ReportEngine.CreateTextEntity "tts.core.report.engine.ReportEngine.ReportEngine.CreateTextEntity")
