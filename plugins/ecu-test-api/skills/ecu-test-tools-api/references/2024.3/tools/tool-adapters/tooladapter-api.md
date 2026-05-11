# Tooladapter API[¶](#tooladapter-api "Link to this heading")

Warning

This API is deprecated! Please see the [User Tool API](../usertool-api/usertool-api.md#usertoolapi) instead.

## AdvancedExampleAdapter[¶](#module-DeprecatedAdvancedExampleAdapter "Link to this heading")

This extension mechanism is deprecated! Please see `AdvancedExampleUserTool` instead.

This is an example of a user-defined ToolAdapter to showcase optional features and customization possibilities for a ToolAdapter. The source code of this example can be found in the ecu.test installation directory under `Templates/DefaultData/Utilities`.

For a basic introduction to user-defined ToolAdapters please refer to the BasicExampleAdapter.

This user-defined ToolAdapter implements the following features:  
- hook methods to run commands on start and stop of a test bench configuration ( `OnConfigure()`, `OnUnconfigure()`)

- hook method to check the health of the connected tool (`IsBroken()`)

- grouping of TBC options

- check boxes or dropdown menus for TBC options

- Tooljobs with complex return types

*class* AdvancedExampleAdapter[¶](#DeprecatedAdvancedExampleAdapter.AdvancedExampleAdapter "Link to this definition")  
Sample implementation of a ToolAdapter with additional feature.

GetVersion()[¶](#DeprecatedAdvancedExampleAdapter.AdvancedExampleAdapter.GetVersion "Link to this definition")  
You can return the version of the tool you are connecting via this tool adapter as a string. The version will be documented in the test report.

Returns:  version

Return type:  Optional\<str\>

IsBroken()[¶](#DeprecatedAdvancedExampleAdapter.AdvancedExampleAdapter.IsBroken "Link to this definition")  
This method is called before test execution and on configuration window update. Return True if any of the external tools used by this ToolAdapter cannot be used anymore (e.g connection lost, tool locked up). Otherwise or if no tool is used, return False.

Returns:  True if tool is broken (not usable)

Return type:  bool

JobGetCountryLanguageAndCurrency(*country*)[¶](#DeprecatedAdvancedExampleAdapter.AdvancedExampleAdapter.JobGetCountryLanguageAndCurrency "Link to this definition")  
Example Tooljob with a complex return type, in this example a tuple. For complex return values the type of the corresponding PropertyDescriptor for the return value needs to be set to PropertyTypeId.object.

OnConfigure()[¶](#DeprecatedAdvancedExampleAdapter.AdvancedExampleAdapter.OnConfigure "Link to this definition")  
This method is called on tool start (test bench start, manual start in configuration window). It can be used to start any external tool needed by this ToolAdapter. Raise a ToollibError to signal an error. If OnConfigure fails, OnUnconfigure will not be called. Use “pass” if no external tool is used.

OnUnconfigure()[¶](#DeprecatedAdvancedExampleAdapter.AdvancedExampleAdapter.OnUnconfigure "Link to this definition")  
This method is called on tool shutdown, if the previous call to OnConfigure did not fail. It can be used to stop any tool needed by this ToolAdapter. Raise a ToollibError to signal an error. Use “pass” if no external tool is used.

## BasicExampleAdapter[¶](#module-DeprecatedBasicExampleAdapter "Link to this heading")

This extension mechanism is deprecated! Please see `BasicExampleUserTool` instead.

This module contains an example of an user-defined Tooladapter. The source code of this example can be found in the ecu.test installation directory under `Templates/DefaultData/Utilities`.

A user-defined Tooladapter must be put in the Utilities directory of the current workspace. If a Tooladapter is changed, it is necessary to stop the current test bench (if it uses the Tooladapter) and select *Extras -> Update user libraries* in ecu.test.

A Tooladapter’s module must contain the class implementing the Tooladapter’s functionality. For autodiscovery and autoimport of ecu.test the module must contain two special variables and two special methods. The required variables are:

> - TOOLNAME: The name used in the test bench configuration for this Tooladapter
>
> - TOOLCAPS: Must be set to Toolcaps.GetNull()

The required methods are:

> - [`IsInstalled()`](#DeprecatedBasicExampleAdapter.IsInstalled "DeprecatedBasicExampleAdapter.IsInstalled"): Check if the interfaced tool is installed on the computer
>
> - [`CreateToolAdapter()`](#DeprecatedBasicExampleAdapter.CreateToolAdapter "DeprecatedBasicExampleAdapter.CreateToolAdapter"): Method to create an instance of the Tooladapter

The Tooladapter’s functionality can be implemented as ToolJobs and ToolProperties. Ports cannot be implemented in user-defined Tooladapters.

var TOOLNAME:  
The name used in the test bench configuration for this Tooladapter - REQUIRED

vartype TOOLNAME:  
str

var TOOLCAPS:  
Must be set to Toolcaps.GetNull() - REQUIRED

*class* BasicExampleAdapter[¶](#DeprecatedBasicExampleAdapter.BasicExampleAdapter "Link to this definition")  
Sample implementation of a Tooladapter.

The ToolDescriptor of the Tooladapter is created on initialization of the Tooladapter. It must match the Tooladapter:

> - Toolname argument must be set to TOOLNAME
>
> - For each JobDescriptor there must be a method with the name Job\<jobname\>() and a matching signature.

Variables:  
**\_toolDesc** ([`ToolDescriptor`](#tts.core.toolingFramework.interface.Descriptors.ToolDescriptor "tts.core.toolingFramework.interface.Descriptors.ToolDescriptor")) – Descriptor of the Tooladapter

GetVersion()[¶](#DeprecatedBasicExampleAdapter.BasicExampleAdapter.GetVersion "Link to this definition")  
You can return the version of the tool you are connecting via this tool adapter as a string. The version will be documented in the test report.

Returns:  version

Return type:  Optional\<str\>

JobGenerateRandomNumber()[¶](#DeprecatedBasicExampleAdapter.BasicExampleAdapter.JobGenerateRandomNumber "Link to this definition")  
See also

[`JobMultiplyAdd()`](#DeprecatedBasicExampleAdapter.BasicExampleAdapter.JobMultiplyAdd "DeprecatedBasicExampleAdapter.BasicExampleAdapter.JobMultiplyAdd")

JobMultiplyAdd(*a*, *b*, *c*)[¶](#DeprecatedBasicExampleAdapter.BasicExampleAdapter.JobMultiplyAdd "Link to this definition")  
ToolJob implementation. Its name must be of the form Job\<jobname\>, where \<jobname\> is the jobname argument of the [`JobDescriptor`](#tts.core.toolingFramework.interface.Descriptors.JobDescriptor "tts.core.toolingFramework.interface.Descriptors.JobDescriptor"). Furthermore the signature of the method must match its `paramDescriptionList`.

Note

there is no type checking

Note

access properties via self.GetProperty(\<propertyName\>) as str value or via self.GetTypedProperty(\<propertyName\>) as correctly typed property according to the type in the PropertyDescriptor.

CreateToolAdapter(*host*, *port*)[¶](#DeprecatedBasicExampleAdapter.CreateToolAdapter "Link to this definition")  
Creates and returns an instance of the Tooladapter of this module.

As these simple Tooladapters cannot be run remotely by the tool server, the host and port arguments must be ignored.

Returns:  a ToolAdapterProxy of a ToolAdapter (e.g. `ExampleAdapter`)

Return type:  ToolAdapterProxy

IsInstalled()[¶](#DeprecatedBasicExampleAdapter.IsInstalled "Link to this definition")  
Checks whether the tool handled by this Tooladapter is installed on the computer running this ecu.test instance. If this Tooladapter does not use any external tool, it is save just to return True.

Returns:  True if tool is installed

Return type:  bool

## Descriptors[¶](#module-tts.core.toolingFramework.interface.Descriptors "Link to this heading")

*class* JobDescriptor[¶](#tts.core.toolingFramework.interface.Descriptors.JobDescriptor "Link to this definition")  
Defines the interface of a job.

The type of the arguments and the return type are not checked. This is subject to change in future versions.

Parameters:  - **jobname** (*str* *|* *None*) – name of the job

- **paramDescriptorList** (*list[*[*PropertyDescriptor*](#tts.core.toolingFramework.interface.Properties.PropertyDescriptor "tts.core.toolingFramework.interface.Properties.PropertyDescriptor")*]* *|* *None*) – argument definitions

- **description** (*str* *|* *None*) – description of the job

- **returnDescriptor** ([*PropertyDescriptor*](#tts.core.toolingFramework.interface.Properties.PropertyDescriptor "tts.core.toolingFramework.interface.Properties.PropertyDescriptor") *|* *None*) – return value description of the job

- **invalidAt** (*str*) – ecu.test version from which on this job will be no longer supported.

- **deprecationMessage** (*str*) – Message that will be displayed in the log and tooltip when a deprecated job is used.

ReportResultAsPrettyPrint()[¶](#tts.core.toolingFramework.interface.Descriptors.JobDescriptor.ReportResultAsPrettyPrint "Link to this definition")  
Returns boolean if the result should be formatted as pretty print in the report.

*class* ToolDescriptor[¶](#tts.core.toolingFramework.interface.Descriptors.ToolDescriptor "Link to this definition")  
Defines the interface of a tool.

Parameters:  - **toolname** (*str*) – TOOLNAME attribute of the ToolAdapters module

- **portImplInfoList** (*list*) – reserved - must be []

- **startPriorityHint** (*int*) – default start priority of the tool when added to the TestBench

- **propDescriptorList** (list \<[`PropertyDescriptor`](#tts.core.toolingFramework.interface.Properties.PropertyDescriptor "tts.core.toolingFramework.interface.Properties.PropertyDescriptor")\>) – description for all tool properties

- **jobDescriptorList** (list \<[`JobDescriptor`](#tts.core.toolingFramework.interface.Descriptors.JobDescriptor "tts.core.toolingFramework.interface.Descriptors.JobDescriptor")\>) – definition of all ToolJobs supported by the ToolAdapter

Deprecated since version -: GetCapabilities

*classmethod* CreateFromString(*xmlrepr*)[¶](#tts.core.toolingFramework.interface.Descriptors.ToolDescriptor.CreateFromString "Link to this definition")  
Converts a ToolDescriptor from its XML representation into a ToolDescriptor object. If an error occurs during this process, an EixError is thrown.

Parameters:  **xmlrepr** (*str*) – XML representation of the ToolDescriptor

## Properties[¶](#module-tts.core.toolingFramework.interface.Properties "Link to this heading")

*class* PropertyDescriptor[¶](#tts.core.toolingFramework.interface.Properties.PropertyDescriptor "Link to this definition")  

versionPattern *= re.compile('20\\d\\d\\.\\d.\*')*[¶](#tts.core.toolingFramework.interface.Properties.PropertyDescriptor.versionPattern "Link to this definition")  
Every PropertyDescriptor instance describes a property, by saving the properties metadata in its attributes and exposing it through the corresponding methods. All attributes except “name” and “readonly” are optional and can be set to `None` (marked as undefined).

New instances of this class should be created via [`CreateInstance()`](#tts.core.toolingFramework.interface.Properties.PropertyDescriptor.CreateInstance "tts.core.toolingFramework.interface.Properties.PropertyDescriptor.CreateInstance"). Direct creation is discouraged, as there are no arguments checks in this case.

*classmethod* CreateInstance(*name*, *displayName=None*, *displayLevel=None*, *description=''*, *type='string'*, *domain=None*, *allowTextInputForChoice=False*, *validReferences=None*, *default=''*, *readonly=False*, *group=None*, *groupValue=None*, *internalUse=False*, *invalidAt=''*, *deprecationMessage=''*, *validator=None*)[¶](#tts.core.toolingFramework.interface.Properties.PropertyDescriptor.CreateInstance "Link to this definition")  
Parameters:  - **name** (*str*) – unique identifier of the property

- **displayName** (*str*) – name used for user interaction (GUI, report)

- **displayLevel** (*int*) – used for grouping

- **description** (*str* *|* *None*) – description of the property

- **type** (an attribute of the [`PropertyTypeId`](#tts.core.toolingFramework.interface.Properties.PropertyTypeId "tts.core.toolingFramework.interface.Properties.PropertyTypeId") class) – type of the property

- **domain** (*sequence* *(list,* *tuple etc.) of* *values*) – list of supported values (must match the properties type)

- **allowTextInputForChoice** (*bool*) – True, if the user is allowed to enter arbitrary text instead of only selecting from the list of given choices.

- **validReferences** (*sequence* *(list,* *tuple etc.) of* *str*) – names of properties this property can refer to

- **default** (*depends on type argument*) – default value

- **readonly** (*bool*) – True if property is readonly

- **group** (*str* *|* *None*) – Name of the group to which the property belongs

- **groupValue** (*Any* *|* *SerializableDescriptionEnumWithLegacySupport* *|* *None*) – Value of the group for which the property is to be displayed. The value must correspond to one of the domain values or ‘True’ or ‘False’ for a checkGroup. For a checkGroup, the value can also be None and will correspond to ‘True’.

- **internalUse** (*bool*) – Marks the property to be used internally only. The behavior of internal properties can differ from normal ones, e.g. they are only displayed in the TBC editor when using a TT license.

- **invalidAt** (*str*) – ecu.test version from which on this property will be no longer supported.

- **deprecationMessage** (*str*) – Message that will be displayed in the log when a deprecated property is used during a test case.

- **validator** (*PropertyValidator* *|* *None*) – Called to validate a property value when package check is performed.

Raises:  
**PropertyError** – name or readonly argument not set correctly

*class* PropertyTypeId[¶](#tts.core.toolingFramework.interface.Properties.PropertyTypeId "Link to this definition")  
The constants of this class define the type of a property. Possible constants:

    - bool
    - int
    - float
    - string
    - text
    - uri
    - bytestream
    - bitstream
    - object (for any other type)

Usage: e.g. PropertyTypeId.bool

*classmethod* ConvertValueType(*value*, *theType*)[¶](#tts.core.toolingFramework.interface.Properties.PropertyTypeId.ConvertValueType "Link to this definition")  
Converts the given value to given type

Note

type=’ByteStream’ will not be converted and will remain a str!

Note

type=’object’ will not be converted and will remain as entered

*classmethod* ValidateValueType(*value*, *theType*)[¶](#tts.core.toolingFramework.interface.Properties.PropertyTypeId.ValidateValueType "Link to this definition")  
Verifies that the given value is of the given type
