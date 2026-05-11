# Code Examples Object API[¶](#code-examples-object-api "Link to this heading")

## Creating a Package[¶](#creating-a-package "Link to this heading")

The following example shows, how to generate a Package with variables, mappings and test steps from scratch. It is a good practice, to create variables and mappings first, as you will need them when setting up a trace analysis and/or a test step.

    from ApiClient import ApiClient

    api = ApiClient()

    # create an empty Package
    testPackage = api.PackageApi.CreatePackage()


    ## create variables

    # create a numerical variable and set an initial value
    newVariable = api.PackageApi.VariableApi.CreateNumericVariable('var1')
    newVariable.SetInitialNumericValue(1000)
    testPackage.AddVariable(newVariable)

    # create an undefined variable without an initial value, and mark it for being recorded
    newVariable = api.PackageApi.VariableApi.CreateVariable('var2')
    newVariable.SetRecorded()
    testPackage.AddVariable(newVariable)


    ## create a mapping

    # get the Package's local mapping space
    mapping = testPackage.GetMapping()

    # create a signal mapping item - keep 'checkTarget=False', as you usually do not have a model loaded, to check the paths for
    newMappingItem = api.PackageApi.MappingApi.CreateModelMappingItem('Plant model', 'v', isSignal=True, referenceName='v', checkTarget=False)
    # add to local mapping space
    mapping.AddItem(newMappingItem)


    ## create test steps

    # create new test step to read the first mapping item
    newTestStep = api.PackageApi.TestStepApi.CreateTsRead(newMappingItem)
    # append to Package
    testPackage.AppendTestStep(newTestStep)
    # set a variable to save the read value in
    newTestStep.SetSaveInVariableName('var1')

    # create wait teststeps and add them to the Package
    newTestStep = api.PackageApi.TestStepApi.CreateTsWait()
    newTestStep.SetDelay('1', 's')
    testPackage.AppendTestStep(newTestStep)
    newTestStep = api.PackageApi.TestStepApi.CreateTsWait()
    newTestStep.SetDelay('200', 'ms')
    testPackage.AppendTestStep(newTestStep)

    # create new test step block and add an read test step with an expectation to the block
    newTestStepBlock = api.PackageApi.TestStepApi.CreateTsBlock()
    testPackage.AppendTestStep(newTestStepBlock)
    newTestStep = api.PackageApi.TestStepApi.CreateTsRead(newMappingItem)
    newExpectation = api.PackageApi.ExpectationApi.CreateNumericExpectation()
    newExpectation.SetExpression("0.0")
    newTestStep.SetExpectation(newExpectation)
    newTestStepBlock.AppendTestStep(newTestStep)


    ## save the Package
    packageFile = 'NewPackage.pkg'
    testPackage.Save(packageFile)

## Strings and Expressions[¶](#strings-and-expressions "Link to this heading")

In strings, special characters usually need to be escaped. Some commands even expect expressions. Expressions are actual python expressions, that need to be able for being validated with `eval()`. Those expressions can contains strings, in which even the escape strings have to be escaped. The following example has no actual purpose, except showcasing escapes in strings and expressions.

    from ApiClient import ApiClient

    api = ApiClient()

    # no need for escaping within raw strings
    pathToWorkspace = r'Drive:\Path\to\Workspace'

    # use relative path, e.g. if the file is located in the workspace folder
    pathToWorkspace = '..'

    # in strings some special characters have to be escaped, e.g. backslashes
    tcfFilePath = pathToWorkspace + '\\Configurations\\SubfolderConf\\SomeConfig.tcf'

    tcf = api.ConfigurationApi.OpenTestConfiguration(tcfFilePath)
    model = tcf.Platform.ModelAccess.Get('RootModelName')

    # paths separators can also be a slash ('/'), that does not need to be escaped
    model.SetFile('SubfolderModels/SomeModel.mdl')
    testPackage = api.PackageApi.OpenPackage(pathToWorkspace + '/Path/to\\Packge.pkg')
    for ts in testPackage.GetTestSteps():
        if ts.GetType() == "TsStartStimulus":
            # as 'SetPathExpression()' needs an expression as input, the escape string '\\'
            # for backslash in the string inside the expression, must be escaped itself
            new_expression = "'\\\\..\\\\String/based' + '\\\\_expression\\\\with\\\\path'"
            ts.SetPathExpression(new_expression)

## Mappings[¶](#mappings "Link to this heading")

A mapping is created as a `MappingItem` and can then be added to the local mapping space of a Package. You should usually set the `checkTarget` flag of the `Create*()` method to `False`. Otherwise, the target path of the mapping will be evaluated against the loaded model. This will fail, if you have not loaded the correct model. For creating mappings for bus signals, you may pass a systemIdentifier, signalName, nodeName, frameName, pduName and referenceName to the corresponding `CreateBusSignalWithPduMappingItem()` method. Some of the arguments are optional. The following example shows usual cases of mappings to be created and added to a Package.

    from ApiClient import ApiClient

    api = ApiClient()

    # load some Package
    packageFile = r'Path\To\SomePackage.pkg'
    testPackage = api.PackageApi.OpenPackage(packageFile)

    # get the local mapping space of the Package - there is no extra constructor for that
    mapping = testPackage.GetMapping()

    modelName = 'RootModelName'
    variablePath = 'firstSublevel/disp/io/Node001/communication/PT-CAN/FrameWithTxSwitch/SignalA/tx_switch/Value'
    # a mapping for a simple variable only needs the root model name and the path from the root model to the variable
    # set the flag 'checkTarget=False', if you do not have a model loaded, where the path is present
    newMappingItem = api.PackageApi.MappingApi.CreateModelMappingItem(modelName, variablePath, checkTarget=False)
    # reference name is generated automatically
    print(newMappingItem.GetReferenceName())
    # it can always be changed manually
    newMappingItem.SetReferenceName('SignalA/tx_switch/Value')
    mapping.AddItem(newMappingItem)

    # a mapping of a signal must be created with the 'isSignal' flag set to True
    signalPath = 'firstSublevel/disp/io/Node001/communication/PT-CAN/FrameWithTxSwitch/SignalA'
    # this time we set the reference name explicitely
    refName = 'SignalA_out'
    newMappingItem = api.PackageApi.MappingApi.CreateModelMappingItem(modelName, signalPath, isSignal=True, referenceName=refName, checkTarget=False)
    mapping.AddItem(newMappingItem)

    # pass relevant information for a bus signal mapping (systemIdentifier, signalName, nodeName, frameName, pduName and referenceName as separate input arguments, where some of them are optional)
    newMappingItem = api.PackageApi.MappingApi.CreateBusSignalWithPduMappingItem('PT-CAN', 'SignalA', 'Node001', 'FrameWithTxSwitch', 'FrameWithTxSwitch', 'SignalA', checkTarget=False)
    mapping.AddItem(newMappingItem)

    # clone the bus signal mapping, to get another instance, with the same properties
    # just change, what should be different
    newMappingItem = newMappingItem.Clone()
    newMappingItem.SetReferenceName('SignalA_manip')
    # and set SignalManipulation to >=0, to enable signal manipulation via the BUS_MANIP port.
    newMappingItem.SetSignalManipulation(0)
    mapping.AddItem(newMappingItem)

    # by saving the Package, the new mappings are added
    testPackage.Save(packageFile)

## Add a Trace Analysis[¶](#add-a-trace-analysis "Link to this heading")

The following example shows, how to add a trace analysis to a Package. For this, the mappings need to be already set up. We will need to create a signal group (and a recording group) to make a recording. Then we can create a trace analysis, an episode, a generic signal, a trace step and a plot. A trace analysis is created in objects that need to be registered to each other in a certain order. To compose the trace analysis we assign the generic signal to the trace analysis, the recording group to the generic signal, the episode to the trace analysis, the trace step to the episode and the plot to the trace step.

    from ApiClient import ApiClient

    api = ApiClient()

    # load Package, mapping and mapping item
    packageFile = 'Path/to/Package.pkg'
    testPackage = api.PackageApi.OpenPackage(packageFile)
    mapping = testPackage.GetMapping()
    mappingItem = mapping.GetItemByName('v')

    # create a new signal group and a new recording group
    # add the mapping item to the signal group
    # activate the automatic recording mode, so no extra test step for start recording is needed
    newSignalGroup = api.PackageApi.SignalRecordingApi.CreateSignalGroup('SomeModelName')
    newRecordingGroup = api.PackageApi.SignalRecordingApi.CreateRecordingGroup('Recording Group of SomeModelName')
    testPackage.AppendSignalGroup(newSignalGroup, newRecordingGroup)
    newRecordingGroup.SetRecordingMode(newRecordingGroup.RECORDING_MODE_AUTO)
    newSignalGroup.AppendMappingItem(mappingItem)

    # create trace analysis, episode, generic signal, trace step and plot
    newTraceAnalysis = api.PackageApi.TraceAnalysisApi.CreateTraceAnalysis('Traceanalysis')
    newEpisode = api.PackageApi.TraceAnalysisApi.CreateEpisode('New Episode')
    genericSignal = api.PackageApi.TraceAnalysisApi.CreateGenericSignal('v')
    newTraceStep = api.PackageApi.TraceAnalysisApi.CreateCalculation('Calculation')
    newTraceStep.SetExpression("v < var1 - 0.1")
    plot = api.PackageApi.TraceAnalysisApi.CreatePlot('Plot')

    # assign them to each other - the order is relevant
    testPackage.AppendTraceAnalysis(newTraceAnalysis)
    newTraceAnalysis.AppendGenericSignal(genericSignal)
    genericSignal.AssignRecordingSignal(newRecordingGroup, 'v')
    newTraceAnalysis.AppendTraceStep(newEpisode)
    newEpisode.AppendTraceStep(newTraceStep)
    newTraceStep.AppendTraceStep(plot)
    plot.ApplySignalsFromParent()

    # save
    testPackage.Save(packageFile)

## Compose a Project[¶](#compose-a-project "Link to this heading")

The following example shows, how to connect .tbc, .tcf and a Package within a Project.

    from ApiClient import ApiClient

    api = ApiClient()

    # create empty Project
    project = api.ProjectApi.CreateProject()

    # add configuration change
    configPath = 'TestConfiguration.tcf'
    testbenchPath = 'TestBenchConfiguration.tbc'
    configChange = api.ProjectApi.ComponentApi.CreateConfigChange('confPack1', configPath, testbenchPath)
    project.AppendComponent(configChange)

    # add Package call
    packageFile = 'MyPackage.pkg'
    packageCall = api.ProjectApi.ComponentApi.CreatePackageCall('package1', packageFile)
    project.AppendComponent(packageCall)

    # save Project
    projectPath = r'NewProject.prj'
    project.Save(projectPath)
