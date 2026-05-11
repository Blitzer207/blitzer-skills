# API for Trace Analyses[¶](#api-for-trace-analyses "Link to this heading")

Part of the [Object based program API](objectApi.md#objectapi)

## TraceAnalysisApi[¶](#traceanalysisapi "Link to this heading")

*class* TraceAnalysisApi[¶](#ApiClient.TraceAnalysisApi "Link to this definition")  
Returned by

- [`PackageApi.TraceAnalysisApi`](PackageApi.md#ApiClient.PackageApi.TraceAnalysisApi "ApiClient.PackageApi.TraceAnalysisApi")

CreateAssertion(*name*, *description=None*)[¶](#ApiClient.TraceAnalysisApi.CreateAssertion "Link to this definition")  
Creates an assertion trace step.

Parameters:  - **name** (*str*) – The name of newly created trace step

- **description** (*str*) – The description of newly created trace step

Returns:  New trace analysis assertion step

Return type:  [`Assertion`](#ApiClient.Assertion "ApiClient.Assertion")

CreateBlock(*name*, *description=None*)[¶](#ApiClient.TraceAnalysisApi.CreateBlock "Link to this definition")  
Creates a block.

Parameters:  - **name** (*str*) – The name of newly created trace analysis

- **description** (*str*) – The description of newly created trace step

Returns:  New block

Return type:  [`AnalysisBlock`](#ApiClient.AnalysisBlock "ApiClient.AnalysisBlock")

CreateCalculation(*name*, *description=None*)[¶](#ApiClient.TraceAnalysisApi.CreateCalculation "Link to this definition")  
Creates a calculation trace step.

Parameters:  - **name** (*str*) – The name of newly created trace step

- **description** (*str*) – The description of newly created trace step

Returns:  New trace analysis calculation step

Return type:  [`Calculation`](#ApiClient.Calculation "ApiClient.Calculation")

CreateEpisode(*name*, *description=None*)[¶](#ApiClient.TraceAnalysisApi.CreateEpisode "Link to this definition")  
Creates an episode.

Parameters:  - **name** (*str*) – The name of newly created episode

- **description** (*str*) – The description of newly created episode

Returns:  New trace analysis episode

Return type:  [`Episode`](#ApiClient.Episode "ApiClient.Episode")

CreateGenericSignal(*name*, *description=None*)[¶](#ApiClient.TraceAnalysisApi.CreateGenericSignal "Link to this definition")  
Creates a generic signal to the trace analysis. The name must be python-conform!

Parameters:  - **name** (*str*) – The name of the generic signal

- **description** (*str*) – The description of newly created generic signal

Returns:  The new generic signal

Return type:  [`GenericSignal`](#ApiClient.GenericSignal "ApiClient.GenericSignal")

CreateIfDef()[¶](#ApiClient.TraceAnalysisApi.CreateIfDef "Link to this definition")  
Creates an IfDef block.

Returns:  New trace analysis IfDef block

Return type:  [`IfDef`](#ApiClient.IfDef "ApiClient.IfDef")

CreateIfThenElse()[¶](#ApiClient.TraceAnalysisApi.CreateIfThenElse "Link to this definition")  
Creates an IfThenElse block.

Returns:  New trace analysis IfThenElse block

Return type:  [`IfThenElse`](#ApiClient.IfThenElse "ApiClient.IfThenElse")

CreatePlot(*name*, *description=None*)[¶](#ApiClient.TraceAnalysisApi.CreatePlot "Link to this definition")  
Creates a plot.

Parameters:  - **name** (*str*) – The name of newly created plot

- **description** (*str*) – The description of newly created plot

Returns:  New trace analysis plot

Return type:  [`Plot`](#ApiClient.Plot "ApiClient.Plot")

CreatePlotCalculatedSignal(*expression*, *name=''*)[¶](#ApiClient.TraceAnalysisApi.CreatePlotCalculatedSignal "Link to this definition")  
Creates a calculated plot signal to be used for a plot ([`PlotCalculatedSignal`](#ApiClient.PlotCalculatedSignal "ApiClient.PlotCalculatedSignal")).

Parameters:  - **expression** (*str*) – The expression from which the signal will be calculated.

- **name** (*str*) – Display name in the plot (optional, otherwise expression string will be used).

Returns:  A calculated plot signal

Return type:  [`PlotCalculatedSignal`](#ApiClient.PlotCalculatedSignal "ApiClient.PlotCalculatedSignal")

CreatePlotSignal(*name*, *signalType='GENERIC'*)[¶](#ApiClient.TraceAnalysisApi.CreatePlotSignal "Link to this definition")  
Creates a plot signal to be used for a plot ([`PlotSignal`](#ApiClient.PlotSignal "ApiClient.PlotSignal")).

Parameters:  - **name** (*str*) – Name of the plot signal

- **signalType** (*str*) – Type of plot signal to be mapped (GENERIC, TRACESTEP)

Returns:  A plot signal

Return type:  [`PlotSignal`](#ApiClient.PlotSignal "ApiClient.PlotSignal")

CreateSignalRecording(*name=None*, *description=None*)[¶](#ApiClient.TraceAnalysisApi.CreateSignalRecording "Link to this definition")  
Creates a signal recording step.

Parameters:  - **name** (*str*) – The name of newly created signal recording

- **description** (*str*) – The description of newly created signal recording

Returns:  New trace analysis signal recording step

Return type:  [`SignalRecording`](#ApiClient.SignalRecording "ApiClient.SignalRecording")

CreateSwitchDefCase()[¶](#ApiClient.TraceAnalysisApi.CreateSwitchDefCase "Link to this definition")  
Creates a SwitchDefCase block.

Returns:  New trace analysis SwitchDefCase block

Return type:  [`SwitchDefCase`](#ApiClient.SwitchDefCase "ApiClient.SwitchDefCase")

CreateTemplateBasedTraceStep(*name=None*, *description=None*)[¶](#ApiClient.TraceAnalysisApi.CreateTemplateBasedTraceStep "Link to this definition")  
Creates a trace step that references a trace step template.

Note:  
After creation the template reference has to be set by calling [`TemplateBasedTraceStep.SetTemplateById()`](#ApiClient.TemplateBasedTraceStep.SetTemplateById "ApiClient.TemplateBasedTraceStep.SetTemplateById") or [`TemplateBasedTraceStep.SetTemplate()`](#ApiClient.TemplateBasedTraceStep.SetTemplate "ApiClient.TemplateBasedTraceStep.SetTemplate")!

Parameters:  - **name** (*str*) – The name of the newly created trace step. If None, the trace step template name will be used.

- **description** (*str*) – The description of the newly created trace step

Returns:  New template based trace step

Return type:  [`TemplateBasedTraceStep`](#ApiClient.TemplateBasedTraceStep "ApiClient.TemplateBasedTraceStep")

CreateTraceAnalysis(*name*, *description=None*)[¶](#ApiClient.TraceAnalysisApi.CreateTraceAnalysis "Link to this definition")  
Creates a trace analysis.

Parameters:  - **name** (*str*) – The name of newly created trace analysis

- **description** (*str*) – The description of newly created trace step

Returns:  New trace analysis

Return type:  [`TraceAnalysis`](#ApiClient.TraceAnalysis "ApiClient.TraceAnalysis")

CreateTraceAnalysisReference(*name*, *description=None*)[¶](#ApiClient.TraceAnalysisApi.CreateTraceAnalysisReference "Link to this definition")  
Creates a reference to another trace analysis of a different package that works like an episode.

Parameters:  - **name** (*str*) – The name of newly created trace analysis reference

- **description** (*str*) – The description of newly created trace analysis reference

Returns:  New trace analysis reference

Return type:  [`TraceAnalysisReference`](#ApiClient.TraceAnalysisReference "ApiClient.TraceAnalysisReference")

CreateTriggerBlock(*name*, *description=None*)[¶](#ApiClient.TraceAnalysisApi.CreateTriggerBlock "Link to this definition")  
Creates a trigger block.

Parameters:  - **name** (*str*) – The name of newly created trace step

- **description** (*str*) – The description of newly created trace step

Returns:  New trigger block

Return type:  [`TriggerBlock`](#ApiClient.TriggerBlock "ApiClient.TriggerBlock")

CreateTraceAnalysisReferenceDeprecated(*name*, *description=None*)[¶](#ApiClient.TraceAnalysisApi.CreateTraceAnalysisReferenceDeprecated "Link to this definition")  
Creates a reference to another trace analysis of a different package that works like an episode.

An old style trace analysis reference is created still using path expressions instead of a package mapping to address the referenced package.

Parameters:  - **name** (*str*) – The name of newly created trace analysis reference

- **description** (*str*) – The description of newly created trace analysis reference

Returns:  New trace analysis reference

Return type:  [`TraceAnalysisReferenceDeprecated`](#ApiClient.TraceAnalysisReferenceDeprecated "ApiClient.TraceAnalysisReferenceDeprecated")

Deprecated since version 2024.1: Please use `CreateTraceAnalysisReference` instead.

## Assertion[¶](#assertion "Link to this heading")

*class* Assertion[¶](#ApiClient.Assertion "Link to this definition")  
Base classes

- [`TraceStep`](#ApiClient.TraceStep "ApiClient.TraceStep")

- [`TraceStepContainer`](#ApiClient.TraceStepContainer "ApiClient.TraceStepContainer")

Returned by

- [`TraceAnalysisApi.CreateAssertion`](#ApiClient.TraceAnalysisApi.CreateAssertion "ApiClient.TraceAnalysisApi.CreateAssertion")

AddTag(*tag*)[¶](#ApiClient.Assertion.AddTag "Link to this definition")  
Add a specific tag to this step.

Parameters:  **tag** (*str*) – The tag to be set

AppendTraceStep(*traceStep*)[¶](#ApiClient.Assertion.AppendTraceStep "Link to this definition")  
Adds a trace step at the end of its children.

Parameters:  **traceStep** ([`TraceStep`](#ApiClient.TraceStep "ApiClient.TraceStep")) – Trace step to be added

Clone()[¶](#ApiClient.Assertion.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`Assertion`](#ApiClient.Assertion "ApiClient.Assertion")

GetCheckErrorMessage()[¶](#ApiClient.Assertion.GetCheckErrorMessage "Link to this definition")  
Returns whether the error messages are checked for an expression.

Returns:  The error messages are checked

Return type:  boolean

GetCheckExpectedVerdict()[¶](#ApiClient.Assertion.GetCheckExpectedVerdict "Link to this definition")  
Returns whether the verdict is checked for an expected value.

Returns:  The verdict is checked

Return type:  boolean

GetCheckMaxExecutionTime()[¶](#ApiClient.Assertion.GetCheckMaxExecutionTime "Link to this definition")  
Returns whether the execution time is checked against a max value.

Returns:  The max execution time is checked

Return type:  boolean

GetCheckMinExecutionTime()[¶](#ApiClient.Assertion.GetCheckMinExecutionTime "Link to this definition")  
Returns whether the execution time is checked against a min value.

Returns:  The min execution time is checked

Return type:  boolean

GetCheckResultText()[¶](#ApiClient.Assertion.GetCheckResultText "Link to this definition")  
Returns whether the result text is to be checked.

Returns:  Returns whether the result text is to be checked

Return type:  boolean

GetDescription()[¶](#ApiClient.Assertion.GetDescription "Link to this definition")  
Returns the description of the trace analysis element.

Returns:  The description

Return type:  str

GetErrorMessageExpr()[¶](#ApiClient.Assertion.GetErrorMessageExpr "Link to this definition")  
Returns the expression for the expected error message.

Returns:  The error message expression

Return type:  str

GetExpectedVerdict()[¶](#ApiClient.Assertion.GetExpectedVerdict "Link to this definition")  
Returns the expected verdict. Possible values are:

> - ‘NONE’
>
> - ‘SUCCESS’
>
> - ‘INCONCLUSIVE’
>
> - ‘FAILED’
>
> - ‘ERROR’

A list of these values is also possible.

Returns:  The expected verdict

Return type:  str

GetLineNo()[¶](#ApiClient.Assertion.GetLineNo "Link to this definition")  
Returns the trace steps line number within its trace analysis.

Returns:  Line number

Return type:  int

GetMaxExecutionTimeExpr()[¶](#ApiClient.Assertion.GetMaxExecutionTimeExpr "Link to this definition")  
Returns the max value the execution time is checked against.

Returns:  The max execution time expression

Return type:  str

GetMaxExecutionTimeUnit()[¶](#ApiClient.Assertion.GetMaxExecutionTimeUnit "Link to this definition")  
Returns the unit for the max execution time. Possible values are:

> - ‘min’
>
> - ‘s’
>
> - ‘ms’
>
> - ‘h’
>
> - ‘d’

Returns:  The max execution time unit

Return type:  str

GetMinExecutionTimeExpr()[¶](#ApiClient.Assertion.GetMinExecutionTimeExpr "Link to this definition")  
Returns the min value the execution time is checked against.

Returns:  The min execution time expression

Return type:  str

GetMinExecutionTimeUnit()[¶](#ApiClient.Assertion.GetMinExecutionTimeUnit "Link to this definition")  
Returns the unit for the min execution time. Possible values are:  
- ‘min’

- ‘s’

- ‘ms’

- ‘h’

- ‘d’

Returns:  The min execution time unit

Return type:  str

GetName()[¶](#ApiClient.Assertion.GetName "Link to this definition")  
Returns the name of the trace analysis element.

Returns:  The name

Return type:  str

GetResultTextExpr()[¶](#ApiClient.Assertion.GetResultTextExpr "Link to this definition")  
Returns the expression that describes the expected result text.

Returns:  Expected result text

Return type:  str

GetTags()[¶](#ApiClient.Assertion.GetTags "Link to this definition")  
Returns the tags set for this step.

Returns:  A (sorted) list of tags

Return type:  list[str]

GetTraceSteps(*skipDisabledSteps=False*, *recursive=False*)[¶](#ApiClient.Assertion.GetTraceSteps "Link to this definition")  
Returns either direct or all children of the trace step.

Parameters:  - **skipDisabledSteps** (*boolean*) – Defines whether disabled trace steps should be excluded, defaults to False.

- **recursive** (*boolean*) – Defines whether children of children are included, defaults to False.

Returns:  The trace steps as flat list.

Return type:  list[[`TraceStep`](#ApiClient.TraceStep "ApiClient.TraceStep")]

GetType()[¶](#ApiClient.Assertion.GetType "Link to this definition")  
Returns the type (class name) of the trace step, e.g.

> - ‘Episode’
>
> - ‘AnalysisBlock’
>
> - ‘TriggerBlock’
>
> - ‘Calculation’
>
> - ‘TemplateBasedTraceStep’
>
> - ‘TraceAnalysisReference’
>
> - ‘TraceAnalysisReferenceDeprecated’

Returns:  Type (class name) of the trace step

Return type:  str

GetUuid()[¶](#ApiClient.Assertion.GetUuid "Link to this definition")  
Returns the UUID of the trace step.

Returns:  UUID of the trace step

Return type:  str

InsertTraceStep(*traceStep*, *position*)[¶](#ApiClient.Assertion.InsertTraceStep "Link to this definition")  
Adds a trace step at a certain line of the trace analysis.

Parameters:  - **traceStep** ([`TraceStep`](#ApiClient.TraceStep "ApiClient.TraceStep")) – Trace step to be added

- **position** (*integer*) – Target index of child beginning with 0

IsContainer()[¶](#ApiClient.Assertion.IsContainer "Link to this definition")  
Checks whether this trace step can contain trace steps.

Returns:  True if it can contain trace steps, else False

Return type:  boolean

IsEnabled()[¶](#ApiClient.Assertion.IsEnabled "Link to this definition")  
Checks whether the trace step is enabled.

Returns:  True if trace step is enabled, else False

Return type:  boolean

IsOk()[¶](#ApiClient.Assertion.IsOk "Link to this definition")  
Returns the internal state of correctness of the trace step.

Returns:  True if no problems were found, else False

Return type:  boolean

IsVisible()[¶](#ApiClient.Assertion.IsVisible "Link to this definition")  
Checks whether the trace step is visible. This depends on the trace step itself or a parent trace step being disabled.

Returns:  True if trace step is visible, else False

Return type:  boolean

RemoveTag(*tag*)[¶](#ApiClient.Assertion.RemoveTag "Link to this definition")  
Remove a specific tag from this step.

Parameters:  **tag** (*str*) – The tag to be removed

RemoveTraceStep(*traceStep*)[¶](#ApiClient.Assertion.RemoveTraceStep "Link to this definition")  
Removes the given trace step from the trace analysis.

Parameters:  **traceStep** ([`TraceStep`](#ApiClient.TraceStep "ApiClient.TraceStep")) – Trace step to be removed

SetCheckErrorMessage(*checkErrorMessage*)[¶](#ApiClient.Assertion.SetCheckErrorMessage "Link to this definition")  
Sets whether the error messages are checked for an expression.

Parameters:  **checkErrorMessage** (*boolean*) – The error messages are checked

SetCheckExpectedVerdict(*checkVerdict*)[¶](#ApiClient.Assertion.SetCheckExpectedVerdict "Link to this definition")  
Sets whether the verdict is checked for an expected value.

Parameters:  **checkVerdict** (*boolean*) – The verdict is checked

SetCheckMaxExecutionTime(*checkMaxExecutionTime*)[¶](#ApiClient.Assertion.SetCheckMaxExecutionTime "Link to this definition")  
Sets whether the execution time is checked against a max value.

Parameters:  **checkMaxExecutionTime** (*boolean*) – The max execution time is checked

SetCheckMinExecutionTime(*checkMinExecutionTime*)[¶](#ApiClient.Assertion.SetCheckMinExecutionTime "Link to this definition")  
Sets whether the execution time is checked against a min value.

Parameters:  **checkMinExecutionTime** (*boolean*) – The min execution time is checked

SetCheckResultText(*checkResultText*)[¶](#ApiClient.Assertion.SetCheckResultText "Link to this definition")  
Sets whether the result text is to be checked.

Parameters:  **checkResultText** (*boolean*) – Specifies whether result text is to be checked

SetDescription(*value*)[¶](#ApiClient.Assertion.SetDescription "Link to this definition")  
Sets the description of the trace analysis element.

Parameters:  **value** (*str*) – The new description

SetEnabled(*enable*)[¶](#ApiClient.Assertion.SetEnabled "Link to this definition")  
Enables or disables the trace step (this also affects child trace steps).

Parameters:  **enable** (*boolean*) – If True, enables the trace step, if False, disables the trace step

SetErrorMessageExpr(*errorMessageExpr*)[¶](#ApiClient.Assertion.SetErrorMessageExpr "Link to this definition")  
Sets an expression for an expected error message.

Parameters:  **errorMessageExpr** (*str*) – The error message expression

SetExpectedVerdict(*verdict*)[¶](#ApiClient.Assertion.SetExpectedVerdict "Link to this definition")  
Sets the expected verdict. Possible values are:

> - ‘NONE’
>
> - ‘SUCCESS’
>
> - ‘INCONCLUSIVE’
>
> - ‘FAILED’
>
> - ‘ERROR’

A list of these values is also valid.

Parameters:  **verdict** (*str*) – The expected verdict

SetMaxExecutionTimeExpr(*maxExecutionTimeExpr*)[¶](#ApiClient.Assertion.SetMaxExecutionTimeExpr "Link to this definition")  
Sets the max value the execution time is checked against.

Parameters:  **maxExecutionTimeExpr** (*str*) – The max execution time expression

SetMaxExecutionTimeUnit(*maxExecutionTimeUnit*)[¶](#ApiClient.Assertion.SetMaxExecutionTimeUnit "Link to this definition")  
Sets the unit for the max execution time. Possible values are:

> - ‘min’
>
> - ‘s’
>
> - ‘ms’
>
> - ‘h’
>
> - ‘d’

Parameters:  **maxExecutionTimeUnit** (*str*) – The max execution time unit

Raises:  
**ApiError** – If maxExecutionTimeUnit is not a valid unit

SetMinExecutionTimeExpr(*minExecutionTimeExpr*)[¶](#ApiClient.Assertion.SetMinExecutionTimeExpr "Link to this definition")  
Sets the min value the execution time is checked against.

Parameters:  **minExecutionTimeExpr** (*str*) – The min execution time expression

SetMinExecutionTimeUnit(*minExecutionTimeUnit*)[¶](#ApiClient.Assertion.SetMinExecutionTimeUnit "Link to this definition")  
Sets the unit for the min execution time. Possible values are:  
- ‘min’

- ‘s’

- ‘ms’

- ‘h’

- ‘d’

Parameters:  **minExecutionTimeUnit** (*str*) – The min execution time unit

Raises:  
**ApiError** – If minExecutionTimeUnit is not a valid unit

SetName(*value*)[¶](#ApiClient.Assertion.SetName "Link to this definition")  
Sets the name of the trace analysis element.

Parameters:  **value** (*str*) – The new name

SetResultTextExpr(*resultTextExpr*)[¶](#ApiClient.Assertion.SetResultTextExpr "Link to this definition")  
Set the expression that describes the expected result text.

Parameters:  **resultTextExpr** (*str*) – Expected result text

SetTags(*tags*)[¶](#ApiClient.Assertion.SetTags "Link to this definition")  
Set the list of tags for this step. The list of tags will be sorted and stored.

Parameters:  **tags** (*list[str]*) – The list of tags

## TraceStep[¶](#tracestep "Link to this heading")

*class* TraceStep[¶](#ApiClient.TraceStep "Link to this definition")  
Base class for all elements of a trace analysis and the trace analysis itself.

Returned by

- [`AnalysisBlock.GetTraceSteps`](#ApiClient.AnalysisBlock.GetTraceSteps "ApiClient.AnalysisBlock.GetTraceSteps")

- [`Assertion.GetTraceSteps`](#ApiClient.Assertion.GetTraceSteps "ApiClient.Assertion.GetTraceSteps")

- [`Calculation.GetTraceSteps`](#ApiClient.Calculation.GetTraceSteps "ApiClient.Calculation.GetTraceSteps")

- [`CaseDefNode.GetTraceSteps`](#ApiClient.CaseDefNode.GetTraceSteps "ApiClient.CaseDefNode.GetTraceSteps")

- [`ElseNode.GetTraceSteps`](#ApiClient.ElseNode.GetTraceSteps "ApiClient.ElseNode.GetTraceSteps")

- [`Episode.GetTraceSteps`](#ApiClient.Episode.GetTraceSteps "ApiClient.Episode.GetTraceSteps")

- [`IfDef.GetTraceSteps`](#ApiClient.IfDef.GetTraceSteps "ApiClient.IfDef.GetTraceSteps")

- [`IfThenElse.GetTraceSteps`](#ApiClient.IfThenElse.GetTraceSteps "ApiClient.IfThenElse.GetTraceSteps")

- [`SignalRecording.GetTraceSteps`](#ApiClient.SignalRecording.GetTraceSteps "ApiClient.SignalRecording.GetTraceSteps")

- [`SwitchDefCase.GetTraceSteps`](#ApiClient.SwitchDefCase.GetTraceSteps "ApiClient.SwitchDefCase.GetTraceSteps")

- [`TemplateBasedTraceStep.GetTraceSteps`](#ApiClient.TemplateBasedTraceStep.GetTraceSteps "ApiClient.TemplateBasedTraceStep.GetTraceSteps")

- [`ThenNode.GetTraceSteps`](#ApiClient.ThenNode.GetTraceSteps "ApiClient.ThenNode.GetTraceSteps")

- [`TraceAnalysis.GetTraceSteps`](#ApiClient.TraceAnalysis.GetTraceSteps "ApiClient.TraceAnalysis.GetTraceSteps")

- [`TraceStepContainer.GetTraceSteps`](#ApiClient.TraceStepContainer.GetTraceSteps "ApiClient.TraceStepContainer.GetTraceSteps")

- [`TriggerBlock.GetTraceSteps`](#ApiClient.TriggerBlock.GetTraceSteps "ApiClient.TriggerBlock.GetTraceSteps")

Subclasses

- [`AnalysisBlock`](#ApiClient.AnalysisBlock "ApiClient.AnalysisBlock")

- [`Assertion`](#ApiClient.Assertion "ApiClient.Assertion")

- [`Calculation`](#ApiClient.Calculation "ApiClient.Calculation")

- [`CaseDefNode`](#ApiClient.CaseDefNode "ApiClient.CaseDefNode")

- [`ElseNode`](#ApiClient.ElseNode "ApiClient.ElseNode")

- [`Episode`](#ApiClient.Episode "ApiClient.Episode")

- [`IfDef`](#ApiClient.IfDef "ApiClient.IfDef")

- [`IfThenElse`](#ApiClient.IfThenElse "ApiClient.IfThenElse")

- [`Plot`](#ApiClient.Plot "ApiClient.Plot")

- [`SignalRecording`](#ApiClient.SignalRecording "ApiClient.SignalRecording")

- [`SwitchDefCase`](#ApiClient.SwitchDefCase "ApiClient.SwitchDefCase")

- [`TemplateBasedTraceStep`](#ApiClient.TemplateBasedTraceStep "ApiClient.TemplateBasedTraceStep")

- [`ThenNode`](#ApiClient.ThenNode "ApiClient.ThenNode")

- [`TraceAnalysis`](#ApiClient.TraceAnalysis "ApiClient.TraceAnalysis")

- [`TraceAnalysisReference`](#ApiClient.TraceAnalysisReference "ApiClient.TraceAnalysisReference")

- [`TraceAnalysisReferenceDeprecated`](#ApiClient.TraceAnalysisReferenceDeprecated "ApiClient.TraceAnalysisReferenceDeprecated")

- [`TraceStepContainer`](#ApiClient.TraceStepContainer "ApiClient.TraceStepContainer")

- [`TriggerBlock`](#ApiClient.TriggerBlock "ApiClient.TriggerBlock")

AddTag(*tag*)[¶](#ApiClient.TraceStep.AddTag "Link to this definition")  
Add a specific tag to this step.

Parameters:  **tag** (*str*) – The tag to be set

Clone()[¶](#ApiClient.TraceStep.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`TraceStep`](#ApiClient.TraceStep "ApiClient.TraceStep")

GetDescription()[¶](#ApiClient.TraceStep.GetDescription "Link to this definition")  
Returns the description of the trace analysis element.

Returns:  The description

Return type:  str

GetLineNo()[¶](#ApiClient.TraceStep.GetLineNo "Link to this definition")  
Returns the trace steps line number within its trace analysis.

Returns:  Line number

Return type:  int

GetName()[¶](#ApiClient.TraceStep.GetName "Link to this definition")  
Returns the name of the trace analysis element.

Returns:  The name

Return type:  str

GetTags()[¶](#ApiClient.TraceStep.GetTags "Link to this definition")  
Returns the tags set for this step.

Returns:  A (sorted) list of tags

Return type:  list[str]

GetType()[¶](#ApiClient.TraceStep.GetType "Link to this definition")  
Returns the type (class name) of the trace step, e.g.

> - ‘Episode’
>
> - ‘AnalysisBlock’
>
> - ‘TriggerBlock’
>
> - ‘Calculation’
>
> - ‘TemplateBasedTraceStep’
>
> - ‘TraceAnalysisReference’
>
> - ‘TraceAnalysisReferenceDeprecated’

Returns:  Type (class name) of the trace step

Return type:  str

GetUuid()[¶](#ApiClient.TraceStep.GetUuid "Link to this definition")  
Returns the UUID of the trace step.

Returns:  UUID of the trace step

Return type:  str

IsContainer()[¶](#ApiClient.TraceStep.IsContainer "Link to this definition")  
Checks whether this trace step can contain trace steps.

Returns:  True if it can contain trace steps, else False

Return type:  boolean

IsEnabled()[¶](#ApiClient.TraceStep.IsEnabled "Link to this definition")  
Checks whether the trace step is enabled.

Returns:  True if trace step is enabled, else False

Return type:  boolean

IsOk()[¶](#ApiClient.TraceStep.IsOk "Link to this definition")  
Returns the internal state of correctness of the trace step.

Returns:  True if no problems were found, else False

Return type:  boolean

IsVisible()[¶](#ApiClient.TraceStep.IsVisible "Link to this definition")  
Checks whether the trace step is visible. This depends on the trace step itself or a parent trace step being disabled.

Returns:  True if trace step is visible, else False

Return type:  boolean

RemoveTag(*tag*)[¶](#ApiClient.TraceStep.RemoveTag "Link to this definition")  
Remove a specific tag from this step.

Parameters:  **tag** (*str*) – The tag to be removed

SetDescription(*value*)[¶](#ApiClient.TraceStep.SetDescription "Link to this definition")  
Sets the description of the trace analysis element.

Parameters:  **value** (*str*) – The new description

SetEnabled(*enable*)[¶](#ApiClient.TraceStep.SetEnabled "Link to this definition")  
Enables or disables the trace step (this also affects child trace steps).

Parameters:  **enable** (*boolean*) – If True, enables the trace step, if False, disables the trace step

SetName(*value*)[¶](#ApiClient.TraceStep.SetName "Link to this definition")  
Sets the name of the trace analysis element.

Parameters:  **value** (*str*) – The new name

SetTags(*tags*)[¶](#ApiClient.TraceStep.SetTags "Link to this definition")  
Set the list of tags for this step. The list of tags will be sorted and stored.

Parameters:  **tags** (*list[str]*) – The list of tags

## AnalysisBlock[¶](#analysisblock "Link to this heading")

*class* AnalysisBlock[¶](#ApiClient.AnalysisBlock "Link to this definition")  
Base classes

- [`TraceStep`](#ApiClient.TraceStep "ApiClient.TraceStep")

- [`TraceStepContainer`](#ApiClient.TraceStepContainer "ApiClient.TraceStepContainer")

Returned by

- [`TraceAnalysisApi.CreateBlock`](#ApiClient.TraceAnalysisApi.CreateBlock "ApiClient.TraceAnalysisApi.CreateBlock")

AddTag(*tag*)[¶](#ApiClient.AnalysisBlock.AddTag "Link to this definition")  
Add a specific tag to this step.

Parameters:  **tag** (*str*) – The tag to be set

AppendTraceStep(*traceStep*)[¶](#ApiClient.AnalysisBlock.AppendTraceStep "Link to this definition")  
Adds a trace step at the end of its children.

Parameters:  **traceStep** ([`TraceStep`](#ApiClient.TraceStep "ApiClient.TraceStep")) – Trace step to be added

Clone()[¶](#ApiClient.AnalysisBlock.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`AnalysisBlock`](#ApiClient.AnalysisBlock "ApiClient.AnalysisBlock")

GetDescription()[¶](#ApiClient.AnalysisBlock.GetDescription "Link to this definition")  
Returns the description of the trace analysis element.

Returns:  The description

Return type:  str

GetLineNo()[¶](#ApiClient.AnalysisBlock.GetLineNo "Link to this definition")  
Returns the trace steps line number within its trace analysis.

Returns:  Line number

Return type:  int

GetName()[¶](#ApiClient.AnalysisBlock.GetName "Link to this definition")  
Returns the name of the trace analysis element.

Returns:  The name

Return type:  str

GetTags()[¶](#ApiClient.AnalysisBlock.GetTags "Link to this definition")  
Returns the tags set for this step.

Returns:  A (sorted) list of tags

Return type:  list[str]

GetTraceSteps(*skipDisabledSteps=False*, *recursive=False*)[¶](#ApiClient.AnalysisBlock.GetTraceSteps "Link to this definition")  
Returns either direct or all children of the trace step.

Parameters:  - **skipDisabledSteps** (*boolean*) – Defines whether disabled trace steps should be excluded, defaults to False.

- **recursive** (*boolean*) – Defines whether children of children are included, defaults to False.

Returns:  The trace steps as flat list.

Return type:  list[[`TraceStep`](#ApiClient.TraceStep "ApiClient.TraceStep")]

GetType()[¶](#ApiClient.AnalysisBlock.GetType "Link to this definition")  
Returns the type (class name) of the trace step, e.g.

> - ‘Episode’
>
> - ‘AnalysisBlock’
>
> - ‘TriggerBlock’
>
> - ‘Calculation’
>
> - ‘TemplateBasedTraceStep’
>
> - ‘TraceAnalysisReference’
>
> - ‘TraceAnalysisReferenceDeprecated’

Returns:  Type (class name) of the trace step

Return type:  str

GetUuid()[¶](#ApiClient.AnalysisBlock.GetUuid "Link to this definition")  
Returns the UUID of the trace step.

Returns:  UUID of the trace step

Return type:  str

InsertTraceStep(*traceStep*, *position*)[¶](#ApiClient.AnalysisBlock.InsertTraceStep "Link to this definition")  
Adds a trace step at a certain line of the trace analysis.

Parameters:  - **traceStep** ([`TraceStep`](#ApiClient.TraceStep "ApiClient.TraceStep")) – Trace step to be added

- **position** (*integer*) – Target index of child beginning with 0

IsContainer()[¶](#ApiClient.AnalysisBlock.IsContainer "Link to this definition")  
Checks whether this trace step can contain trace steps.

Returns:  True if it can contain trace steps, else False

Return type:  boolean

IsEnabled()[¶](#ApiClient.AnalysisBlock.IsEnabled "Link to this definition")  
Checks whether the trace step is enabled.

Returns:  True if trace step is enabled, else False

Return type:  boolean

IsOk()[¶](#ApiClient.AnalysisBlock.IsOk "Link to this definition")  
Returns the internal state of correctness of the trace step.

Returns:  True if no problems were found, else False

Return type:  boolean

IsVisible()[¶](#ApiClient.AnalysisBlock.IsVisible "Link to this definition")  
Checks whether the trace step is visible. This depends on the trace step itself or a parent trace step being disabled.

Returns:  True if trace step is visible, else False

Return type:  boolean

RemoveTag(*tag*)[¶](#ApiClient.AnalysisBlock.RemoveTag "Link to this definition")  
Remove a specific tag from this step.

Parameters:  **tag** (*str*) – The tag to be removed

RemoveTraceStep(*traceStep*)[¶](#ApiClient.AnalysisBlock.RemoveTraceStep "Link to this definition")  
Removes the given trace step from the trace analysis.

Parameters:  **traceStep** ([`TraceStep`](#ApiClient.TraceStep "ApiClient.TraceStep")) – Trace step to be removed

SetDescription(*value*)[¶](#ApiClient.AnalysisBlock.SetDescription "Link to this definition")  
Sets the description of the trace analysis element.

Parameters:  **value** (*str*) – The new description

SetEnabled(*enable*)[¶](#ApiClient.AnalysisBlock.SetEnabled "Link to this definition")  
Enables or disables the trace step (this also affects child trace steps).

Parameters:  **enable** (*boolean*) – If True, enables the trace step, if False, disables the trace step

SetName(*value*)[¶](#ApiClient.AnalysisBlock.SetName "Link to this definition")  
Sets the name of the trace analysis element.

Parameters:  **value** (*str*) – The new name

SetTags(*tags*)[¶](#ApiClient.AnalysisBlock.SetTags "Link to this definition")  
Set the list of tags for this step. The list of tags will be sorted and stored.

Parameters:  **tags** (*list[str]*) – The list of tags

## TraceStepContainer[¶](#tracestepcontainer "Link to this heading")

*class* TraceStepContainer[¶](#ApiClient.TraceStepContainer "Link to this definition")  
Base class

[`TraceStep`](#ApiClient.TraceStep "ApiClient.TraceStep")

Subclasses

- [`AnalysisBlock`](#ApiClient.AnalysisBlock "ApiClient.AnalysisBlock")

- [`Assertion`](#ApiClient.Assertion "ApiClient.Assertion")

- [`Calculation`](#ApiClient.Calculation "ApiClient.Calculation")

- [`CaseDefNode`](#ApiClient.CaseDefNode "ApiClient.CaseDefNode")

- [`ElseNode`](#ApiClient.ElseNode "ApiClient.ElseNode")

- [`Episode`](#ApiClient.Episode "ApiClient.Episode")

- [`IfDef`](#ApiClient.IfDef "ApiClient.IfDef")

- [`IfThenElse`](#ApiClient.IfThenElse "ApiClient.IfThenElse")

- [`SignalRecording`](#ApiClient.SignalRecording "ApiClient.SignalRecording")

- [`SwitchDefCase`](#ApiClient.SwitchDefCase "ApiClient.SwitchDefCase")

- [`TemplateBasedTraceStep`](#ApiClient.TemplateBasedTraceStep "ApiClient.TemplateBasedTraceStep")

- [`ThenNode`](#ApiClient.ThenNode "ApiClient.ThenNode")

- [`TraceAnalysis`](#ApiClient.TraceAnalysis "ApiClient.TraceAnalysis")

- [`TriggerBlock`](#ApiClient.TriggerBlock "ApiClient.TriggerBlock")

AddTag(*tag*)[¶](#ApiClient.TraceStepContainer.AddTag "Link to this definition")  
Add a specific tag to this step.

Parameters:  **tag** (*str*) – The tag to be set

AppendTraceStep(*traceStep*)[¶](#ApiClient.TraceStepContainer.AppendTraceStep "Link to this definition")  
Adds a trace step at the end of its children.

Parameters:  **traceStep** ([`TraceStep`](#ApiClient.TraceStep "ApiClient.TraceStep")) – Trace step to be added

Clone()[¶](#ApiClient.TraceStepContainer.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`TraceStepContainer`](#ApiClient.TraceStepContainer "ApiClient.TraceStepContainer")

GetDescription()[¶](#ApiClient.TraceStepContainer.GetDescription "Link to this definition")  
Returns the description of the trace analysis element.

Returns:  The description

Return type:  str

GetLineNo()[¶](#ApiClient.TraceStepContainer.GetLineNo "Link to this definition")  
Returns the trace steps line number within its trace analysis.

Returns:  Line number

Return type:  int

GetName()[¶](#ApiClient.TraceStepContainer.GetName "Link to this definition")  
Returns the name of the trace analysis element.

Returns:  The name

Return type:  str

GetTags()[¶](#ApiClient.TraceStepContainer.GetTags "Link to this definition")  
Returns the tags set for this step.

Returns:  A (sorted) list of tags

Return type:  list[str]

GetTraceSteps(*skipDisabledSteps=False*, *recursive=False*)[¶](#ApiClient.TraceStepContainer.GetTraceSteps "Link to this definition")  
Returns either direct or all children of the trace step.

Parameters:  - **skipDisabledSteps** (*boolean*) – Defines whether disabled trace steps should be excluded, defaults to False.

- **recursive** (*boolean*) – Defines whether children of children are included, defaults to False.

Returns:  The trace steps as flat list.

Return type:  list[[`TraceStep`](#ApiClient.TraceStep "ApiClient.TraceStep")]

GetType()[¶](#ApiClient.TraceStepContainer.GetType "Link to this definition")  
Returns the type (class name) of the trace step, e.g.

> - ‘Episode’
>
> - ‘AnalysisBlock’
>
> - ‘TriggerBlock’
>
> - ‘Calculation’
>
> - ‘TemplateBasedTraceStep’
>
> - ‘TraceAnalysisReference’
>
> - ‘TraceAnalysisReferenceDeprecated’

Returns:  Type (class name) of the trace step

Return type:  str

GetUuid()[¶](#ApiClient.TraceStepContainer.GetUuid "Link to this definition")  
Returns the UUID of the trace step.

Returns:  UUID of the trace step

Return type:  str

InsertTraceStep(*traceStep*, *position*)[¶](#ApiClient.TraceStepContainer.InsertTraceStep "Link to this definition")  
Adds a trace step at a certain line of the trace analysis.

Parameters:  - **traceStep** ([`TraceStep`](#ApiClient.TraceStep "ApiClient.TraceStep")) – Trace step to be added

- **position** (*integer*) – Target index of child beginning with 0

IsContainer()[¶](#ApiClient.TraceStepContainer.IsContainer "Link to this definition")  
Checks whether this trace step can contain trace steps.

Returns:  True if it can contain trace steps, else False

Return type:  boolean

IsEnabled()[¶](#ApiClient.TraceStepContainer.IsEnabled "Link to this definition")  
Checks whether the trace step is enabled.

Returns:  True if trace step is enabled, else False

Return type:  boolean

IsOk()[¶](#ApiClient.TraceStepContainer.IsOk "Link to this definition")  
Returns the internal state of correctness of the trace step.

Returns:  True if no problems were found, else False

Return type:  boolean

IsVisible()[¶](#ApiClient.TraceStepContainer.IsVisible "Link to this definition")  
Checks whether the trace step is visible. This depends on the trace step itself or a parent trace step being disabled.

Returns:  True if trace step is visible, else False

Return type:  boolean

RemoveTag(*tag*)[¶](#ApiClient.TraceStepContainer.RemoveTag "Link to this definition")  
Remove a specific tag from this step.

Parameters:  **tag** (*str*) – The tag to be removed

RemoveTraceStep(*traceStep*)[¶](#ApiClient.TraceStepContainer.RemoveTraceStep "Link to this definition")  
Removes the given trace step from the trace analysis.

Parameters:  **traceStep** ([`TraceStep`](#ApiClient.TraceStep "ApiClient.TraceStep")) – Trace step to be removed

SetDescription(*value*)[¶](#ApiClient.TraceStepContainer.SetDescription "Link to this definition")  
Sets the description of the trace analysis element.

Parameters:  **value** (*str*) – The new description

SetEnabled(*enable*)[¶](#ApiClient.TraceStepContainer.SetEnabled "Link to this definition")  
Enables or disables the trace step (this also affects child trace steps).

Parameters:  **enable** (*boolean*) – If True, enables the trace step, if False, disables the trace step

SetName(*value*)[¶](#ApiClient.TraceStepContainer.SetName "Link to this definition")  
Sets the name of the trace analysis element.

Parameters:  **value** (*str*) – The new name

SetTags(*tags*)[¶](#ApiClient.TraceStepContainer.SetTags "Link to this definition")  
Set the list of tags for this step. The list of tags will be sorted and stored.

Parameters:  **tags** (*list[str]*) – The list of tags

## Calculation[¶](#calculation "Link to this heading")

*class* Calculation[¶](#ApiClient.Calculation "Link to this definition")  
Base classes

- [`TraceStep`](#ApiClient.TraceStep "ApiClient.TraceStep")

- [`TraceStepContainer`](#ApiClient.TraceStepContainer "ApiClient.TraceStepContainer")

Returned by

- [`TraceAnalysisApi.CreateCalculation`](#ApiClient.TraceAnalysisApi.CreateCalculation "ApiClient.TraceAnalysisApi.CreateCalculation")

EXPECTATION_MODE_ALWAYS[¶](#ApiClient.Calculation.EXPECTATION_MODE_ALWAYS "Link to this definition")  
Returns the constant used to specify the expectation mode ‘Fulfilled everywhere’.

Returns:  The constant

Return type:  str

EXPECTATION_MODE_DURATION[¶](#ApiClient.Calculation.EXPECTATION_MODE_DURATION "Link to this definition")  
Returns the constant used to specify the expectation mode ‘Fulfilled for at least’.

Returns:  The constant

Return type:  str

EXPECTATION_MODE_ONCE[¶](#ApiClient.Calculation.EXPECTATION_MODE_ONCE "Link to this definition")  
Returns the constant used to specify the expectation mode ‘Fulfilled at least once’.

Returns:  The constant

Return type:  str

AddTag(*tag*)[¶](#ApiClient.Calculation.AddTag "Link to this definition")  
Add a specific tag to this step.

Parameters:  **tag** (*str*) – The tag to be set

AppendTraceStep(*traceStep*)[¶](#ApiClient.Calculation.AppendTraceStep "Link to this definition")  
Adds a trace step at the end of its children.

Parameters:  **traceStep** ([`TraceStep`](#ApiClient.TraceStep "ApiClient.TraceStep")) – Trace step to be added

Clone()[¶](#ApiClient.Calculation.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`Calculation`](#ApiClient.Calculation "ApiClient.Calculation")

DeactivateExpectation()[¶](#ApiClient.Calculation.DeactivateExpectation "Link to this definition")  
Deactivates the expectation so that the expression of the calculation will not be evaluated.

DeactivateFailedComment()[¶](#ApiClient.Calculation.DeactivateFailedComment "Link to this definition")  
Deactivates the expectation for the failed comment so that the result will not be evaluated.

DeactivateSaveIn()[¶](#ApiClient.Calculation.DeactivateSaveIn "Link to this definition")  
Deactivates the save in property, so the expression value will not be stored in a generic signal.

DeactivateSuccessComment()[¶](#ApiClient.Calculation.DeactivateSuccessComment "Link to this definition")  
Deactivates the expectation for the success comment so that the result will not be evaluated.

GetDescription()[¶](#ApiClient.Calculation.GetDescription "Link to this definition")  
Returns the description of the trace analysis element.

Returns:  The description

Return type:  str

GetExpectation()[¶](#ApiClient.Calculation.GetExpectation "Link to this definition")  
Returns the expectation expression for the evaluation of the calculation, or None, if no expectation was defined.

Returns:  The expectation

Return type:  [`Expectation`](ExpectationApi.md#ApiClient.Expectation "ApiClient.Expectation")

GetExpectationMode()[¶](#ApiClient.Calculation.GetExpectationMode "Link to this definition")  
Returns the expectation mode. Possible values are ‘always’, ‘once’, ‘duration’ or None, if no expectation was defined.

Returns:  The expectation mode

Return type:  str

GetExpectationModeOptions()[¶](#ApiClient.Calculation.GetExpectationModeOptions "Link to this definition")  
Returns:  The options object for expectation mode parameters

Return type:  [`ExpectationModeOptions`](#ApiClient.ExpectationModeOptions "ApiClient.ExpectationModeOptions")

GetExpression()[¶](#ApiClient.Calculation.GetExpression "Link to this definition")  
Returns the expression of the calculation.

Returns:  The expression

Return type:  str

GetFailedComment()[¶](#ApiClient.Calculation.GetFailedComment "Link to this definition")  
Returns the failed comment of the step.

Returns:  The failed comment

Return type:  string

GetLineNo()[¶](#ApiClient.Calculation.GetLineNo "Link to this definition")  
Returns the trace steps line number within its trace analysis.

Returns:  Line number

Return type:  int

GetName()[¶](#ApiClient.Calculation.GetName "Link to this definition")  
Returns the name of the trace analysis element.

Returns:  The name

Return type:  str

GetReportConfig()[¶](#ApiClient.Calculation.GetReportConfig "Link to this definition")  
Returns the report config for this trace step.

Returns:  The report config object

Return type:  [`ReportConfig`](#ApiClient.ReportConfig "ApiClient.ReportConfig")

GetResultNoEval()[¶](#ApiClient.Calculation.GetResultNoEval "Link to this definition")  
Returns the verdict of a calculation that is never evaluated.

Returns:  The verdict of the calculation if never evaluated

Return type:  str

GetSaveInSignalName()[¶](#ApiClient.Calculation.GetSaveInSignalName "Link to this definition")  
Returns the currently selected signal to save the expression value.

Returns:  The signal’s name or None if expression value is not saved to a signal by the calculation.

Return type:  str

GetSuccessComment()[¶](#ApiClient.Calculation.GetSuccessComment "Link to this definition")  
Returns the success comment of the step.

Returns:  The success comment

Return type:  string

GetTags()[¶](#ApiClient.Calculation.GetTags "Link to this definition")  
Returns the tags set for this step.

Returns:  A (sorted) list of tags

Return type:  list[str]

GetTraceSteps(*skipDisabledSteps=False*, *recursive=False*)[¶](#ApiClient.Calculation.GetTraceSteps "Link to this definition")  
Returns either direct or all children of the trace step.

Parameters:  - **skipDisabledSteps** (*boolean*) – Defines whether disabled trace steps should be excluded, defaults to False.

- **recursive** (*boolean*) – Defines whether children of children are included, defaults to False.

Returns:  The trace steps as flat list.

Return type:  list[[`TraceStep`](#ApiClient.TraceStep "ApiClient.TraceStep")]

GetType()[¶](#ApiClient.Calculation.GetType "Link to this definition")  
Returns the type (class name) of the trace step, e.g.

> - ‘Episode’
>
> - ‘AnalysisBlock’
>
> - ‘TriggerBlock’
>
> - ‘Calculation’
>
> - ‘TemplateBasedTraceStep’
>
> - ‘TraceAnalysisReference’
>
> - ‘TraceAnalysisReferenceDeprecated’

Returns:  Type (class name) of the trace step

Return type:  str

GetUuid()[¶](#ApiClient.Calculation.GetUuid "Link to this definition")  
Returns the UUID of the trace step.

Returns:  UUID of the trace step

Return type:  str

GetVectorExpectationMode()[¶](#ApiClient.Calculation.GetVectorExpectationMode "Link to this definition")  
Returns the vector expectation mode. Possible values are:

> - ‘no vector’
>
> - ‘all components’
>
> - ‘any component’

Returns:  The vector expectation mode

Return type:  str

InsertTraceStep(*traceStep*, *position*)[¶](#ApiClient.Calculation.InsertTraceStep "Link to this definition")  
Adds a trace step at a certain line of the trace analysis.

Parameters:  - **traceStep** ([`TraceStep`](#ApiClient.TraceStep "ApiClient.TraceStep")) – Trace step to be added

- **position** (*integer*) – Target index of child beginning with 0

IsContainer()[¶](#ApiClient.Calculation.IsContainer "Link to this definition")  
Checks whether this trace step can contain trace steps.

Returns:  True if it can contain trace steps, else False

Return type:  boolean

IsEnabled()[¶](#ApiClient.Calculation.IsEnabled "Link to this definition")  
Checks whether the trace step is enabled.

Returns:  True if trace step is enabled, else False

Return type:  boolean

IsOk()[¶](#ApiClient.Calculation.IsOk "Link to this definition")  
Returns the internal state of correctness of the trace step.

Returns:  True if no problems were found, else False

Return type:  boolean

IsVisible()[¶](#ApiClient.Calculation.IsVisible "Link to this definition")  
Checks whether the trace step is visible. This depends on the trace step itself or a parent trace step being disabled.

Returns:  True if trace step is visible, else False

Return type:  boolean

RemoveTag(*tag*)[¶](#ApiClient.Calculation.RemoveTag "Link to this definition")  
Remove a specific tag from this step.

Parameters:  **tag** (*str*) – The tag to be removed

RemoveTraceStep(*traceStep*)[¶](#ApiClient.Calculation.RemoveTraceStep "Link to this definition")  
Removes the given trace step from the trace analysis.

Parameters:  **traceStep** ([`TraceStep`](#ApiClient.TraceStep "ApiClient.TraceStep")) – Trace step to be removed

SetDescription(*value*)[¶](#ApiClient.Calculation.SetDescription "Link to this definition")  
Sets the description of the trace analysis element.

Parameters:  **value** (*str*) – The new description

SetEnabled(*enable*)[¶](#ApiClient.Calculation.SetEnabled "Link to this definition")  
Enables or disables the trace step (this also affects child trace steps).

Parameters:  **enable** (*boolean*) – If True, enables the trace step, if False, disables the trace step

SetExpression(*expression*)[¶](#ApiClient.Calculation.SetExpression "Link to this definition")  
Sets the expression of the calculation.

Parameters:  **expression** (*str*) – The expression

SetFailedComment(*failedComment*)[¶](#ApiClient.Calculation.SetFailedComment "Link to this definition")  
Sets the expression for the failed comment of the step. The expression will be activated if it was not enabled previously.

Parameters:  **failedComment** (*string*) – The expression for the failed comment

SetName(*value*)[¶](#ApiClient.Calculation.SetName "Link to this definition")  
Sets the name of the trace analysis element.

Parameters:  **value** (*str*) – The new name

SetResultNoEval(*resultNoEval*)[¶](#ApiClient.Calculation.SetResultNoEval "Link to this definition")  
Sets the verdict of a calculation that is never evaluated. Possible values: ‘NONE’, ‘SUCCESS’, ‘INCONCLUSIVE’, ‘FAILED’ or ‘ERROR’.

Parameters:  **resultNoEval** (*str*) – The verdict of the calculation if never evaluated

SetSaveInSignalName(*signalName*)[¶](#ApiClient.Calculation.SetSaveInSignalName "Link to this definition")  
Sets the name of the generic signal used for storing the expression value.

Parameters:  **signalName** (*str*) – The signal’s name. Must not be None or an empty string.

Raises:  
**ApiError** – If signalName is None or an empty string

SetSuccessComment(*successComment*)[¶](#ApiClient.Calculation.SetSuccessComment "Link to this definition")  
Sets the expression for the success comment of the step. The expression will be activated if it was not enabled previously.

Parameters:  **successComment** (*string*) – The expression for the success comment

SetTags(*tags*)[¶](#ApiClient.Calculation.SetTags "Link to this definition")  
Set the list of tags for this step. The list of tags will be sorted and stored.

Parameters:  **tags** (*list[str]*) – The list of tags

SetVectorExpectationMode(*vectorMode*)[¶](#ApiClient.Calculation.SetVectorExpectationMode "Link to this definition")  
Sets the vector expectation mode. Possible values are:

> - ‘no vector’
>
> - ‘all components’
>
> - ‘any component’

Parameters:  **vectorMode** (*str*) – The vector expectation mode

GetExpectationModeParam()[¶](#ApiClient.Calculation.GetExpectationModeParam "Link to this definition")  
Returns the expectation mode parameter or None, if no expectation was defined. For mode ‘duration’ this is the minimal duration.

Returns:  The expectation mode parameter

Return type:  str

Deprecated since version 2024.3: Please use methods `GetExpectationModeOptions().GetMinDuration` instead.

SetExpectation(*expectation*, *mode*, *modeParam=None*)[¶](#ApiClient.Calculation.SetExpectation "Link to this definition")  
Sets the expectation for the evaluation of the calculation. The expectation will be activated if it was not enabled previously. Possible values for mode can be obtained by either of the constants:

> - [`Calculation.EXPECTATION_MODE_ALWAYS`](#ApiClient.Calculation.EXPECTATION_MODE_ALWAYS "ApiClient.Calculation.EXPECTATION_MODE_ALWAYS")
>
> - [`Calculation.EXPECTATION_MODE_ONCE`](#ApiClient.Calculation.EXPECTATION_MODE_ONCE "ApiClient.Calculation.EXPECTATION_MODE_ONCE")
>
> - [`Calculation.EXPECTATION_MODE_DURATION`](#ApiClient.Calculation.EXPECTATION_MODE_DURATION "ApiClient.Calculation.EXPECTATION_MODE_DURATION")

Use modeParam to specify the minimal duration (duration mode only).

Parameters:  - **expectation** ([`Expectation`](ExpectationApi.md#ApiClient.Expectation "ApiClient.Expectation")) – The expectation

- **mode** (*str*) – The expression for expectation mode

- **modeParam** (*str*) – The expression for modeParam

Raises:  
**ValueError** – If the expectation is not of type NumericExpectation or StringExpectation

Deprecated since version 2024.3: Argument `modeParam` must be set via [`GetExpectationModeOptions()`](#ApiClient.Calculation.GetExpectationModeOptions "ApiClient.Calculation.GetExpectationModeOptions") instead.

## ExpectationModeOptions[¶](#expectationmodeoptions "Link to this heading")

*class* ExpectationModeOptions[¶](#ApiClient.ExpectationModeOptions "Link to this definition")  
Returned by

- [`Calculation.GetExpectationModeOptions`](#ApiClient.Calculation.GetExpectationModeOptions "ApiClient.Calculation.GetExpectationModeOptions")

Clone()[¶](#ApiClient.ExpectationModeOptions.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`ExpectationModeOptions`](#ApiClient.ExpectationModeOptions "ApiClient.ExpectationModeOptions")

GetMinDuration()[¶](#ApiClient.ExpectationModeOptions.GetMinDuration "Link to this definition")  
Returns the minimal duration.

Returns:  The minimal duration

Return type:  str

IsCumulated()[¶](#ApiClient.ExpectationModeOptions.IsCumulated "Link to this definition")  
Returns True if all successful range should be cumulated and evaluated against the expected minimum duration.

Returns:  True if all successful ranges should be cumulated, else False

Return type:  bool

IsRelative()[¶](#ApiClient.ExpectationModeOptions.IsRelative "Link to this definition")  
Returns True if the value for minimum duration is specified as a relative value given in percent.

Returns:  True if mimimum duration is a relative value, else False

Return type:  bool

SetCumulated(*value*)[¶](#ApiClient.ExpectationModeOptions.SetCumulated "Link to this definition")  
Decides whether all the successful ranges should be cumulated.

Parameters:  **value** (*boolean*) – True if all the successful range should be cumulated, else False

SetMinDuration(*minDuration*)[¶](#ApiClient.ExpectationModeOptions.SetMinDuration "Link to this definition")  
Parameters:  **minDuration** (*str*) – The expression for minimal duration.

SetRelative(*value*)[¶](#ApiClient.ExpectationModeOptions.SetRelative "Link to this definition")  
Decides whether the value for minimum duration is given as a relative value given in percent.

Parameters:  **value** (*boolean*) – True if the value for mimimum duration is a relative value, else False

## ReportConfig[¶](#reportconfig "Link to this heading")

*class* ReportConfig[¶](#ApiClient.ReportConfig "Link to this definition")  
Returned by

- [`Calculation.GetReportConfig`](#ApiClient.Calculation.GetReportConfig "ApiClient.Calculation.GetReportConfig")

- [`TemplateBasedTraceStep.GetReportConfig`](#ApiClient.TemplateBasedTraceStep.GetReportConfig "ApiClient.TemplateBasedTraceStep.GetReportConfig")

Clone()[¶](#ApiClient.ReportConfig.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`ReportConfig`](#ApiClient.ReportConfig "ApiClient.ReportConfig")

GetMaxSpots()[¶](#ApiClient.ReportConfig.GetMaxSpots "Link to this definition")  
Get how many spots or ranges will be reported.

Returns:  Number of spots or ranges to be reported

Return type:  int

GetMinDelta()[¶](#ApiClient.ReportConfig.GetMinDelta "Link to this definition")  
Get the minimum duration between reported spots or ranges.

Returns:  Minimum duration between reported spots or ranges

Return type:  float

GetResultDetailsVariable()[¶](#ApiClient.ReportConfig.GetResultDetailsVariable "Link to this definition")  
Get the name of the package variable result details will be written to.

Returns:  Name of the result details variable. None if not set.

Return type:  str

SetMaxSpots(*maxSpots*)[¶](#ApiClient.ReportConfig.SetMaxSpots "Link to this definition")  
Sets how many spots or ranges will be reported.

Parameters:  **maxSpots** (*int*) – Number of spots or ranges to be reported (defaults to 100)

SetMinDelta(*minDelta*)[¶](#ApiClient.ReportConfig.SetMinDelta "Link to this definition")  
Sets the minimum duration between reported spots or ranges.

Parameters:  **minDelta** (*float*) – Minimum duration between reported spots or ranges (defaults to 0.0)

SetResultDetailsVariable(*varName*)[¶](#ApiClient.ReportConfig.SetResultDetailsVariable "Link to this definition")  
Sets the name of the package variable result details will be written to.

Parameters:  **varName** (*str*) – Name of the result details variable. None to set no variable.

## TemplateBasedTraceStep[¶](#templatebasedtracestep "Link to this heading")

*class* TemplateBasedTraceStep[¶](#ApiClient.TemplateBasedTraceStep "Link to this definition")  
Base classes

- [`TraceStep`](#ApiClient.TraceStep "ApiClient.TraceStep")

- [`TraceStepContainer`](#ApiClient.TraceStepContainer "ApiClient.TraceStepContainer")

Returned by

- [`TraceAnalysisApi.CreateTemplateBasedTraceStep`](#ApiClient.TraceAnalysisApi.CreateTemplateBasedTraceStep "ApiClient.TraceAnalysisApi.CreateTemplateBasedTraceStep")

AddTag(*tag*)[¶](#ApiClient.TemplateBasedTraceStep.AddTag "Link to this definition")  
Add a specific tag to this step.

Parameters:  **tag** (*str*) – The tag to be set

AppendTraceStep(*traceStep*)[¶](#ApiClient.TemplateBasedTraceStep.AppendTraceStep "Link to this definition")  
Adds a trace step at the end of its children.

Parameters:  **traceStep** ([`TraceStep`](#ApiClient.TraceStep "ApiClient.TraceStep")) – Trace step to be added

AssignGenericSignal(*sigName*, *genSig*)[¶](#ApiClient.TemplateBasedTraceStep.AssignGenericSignal "Link to this definition")  
Bind a generic signal to a signal of the trace step.

Note:  
It is not valid to assign a generic signal to multiple trace step signals!

Parameters:  - **sigName** (*str*) – Name if trace step signal

- **genSig** ([`GenericSignal`](#ApiClient.GenericSignal "ApiClient.GenericSignal")) – The generic signal object

Returns:  An object representing the signal binding. If a there is already a signal binding for sigName, the signal binding object an its settings will be reused; otherwise, a new signal binding object will be created.

Return type:  [`SignalBinding`](#ApiClient.SignalBinding "ApiClient.SignalBinding")

AssignGenericSignalByName(*sigName*, *genSigName*)[¶](#ApiClient.TemplateBasedTraceStep.AssignGenericSignalByName "Link to this definition")  
Bind a generic signal to a signal of the trace step.

Note:  
It is not valid to assign a generic signal to multiple trace step signals!

Parameters:  - **sigName** (*str*) – Name of trace step signal

- **genSigName** (*str*) – Name of the generic signal

Returns:  An object representing the signal binding. If there is already a signal binding for sigName, the signal binding object and its settings will be reused; otherwise, a new signal binding object will be created.

Return type:  [`SignalBinding`](#ApiClient.SignalBinding "ApiClient.SignalBinding")

ClearSignalBinding(*sigName*)[¶](#ApiClient.TemplateBasedTraceStep.ClearSignalBinding "Link to this definition")  
Clears the signal binding for the given signal name.

Parameters:  **sigName** (*str*) – The signal name

Clone()[¶](#ApiClient.TemplateBasedTraceStep.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`TemplateBasedTraceStep`](#ApiClient.TemplateBasedTraceStep "ApiClient.TemplateBasedTraceStep")

GetAbsolutePath()[¶](#ApiClient.TemplateBasedTraceStep.GetAbsolutePath "Link to this definition")  
Returns the absolute path of the referenced file.

Returns:  absolute path or None if the path reference cannot be resolved

Return type:  str

GetDescription()[¶](#ApiClient.TemplateBasedTraceStep.GetDescription "Link to this definition")  
Returns the description of the trace analysis element.

Returns:  The description

Return type:  str

GetLineNo()[¶](#ApiClient.TemplateBasedTraceStep.GetLineNo "Link to this definition")  
Returns the trace steps line number within its trace analysis.

Returns:  Line number

Return type:  int

GetName()[¶](#ApiClient.TemplateBasedTraceStep.GetName "Link to this definition")  
Returns the name of the trace analysis element.

Returns:  The name

Return type:  str

GetParameter(*paramName*)[¶](#ApiClient.TemplateBasedTraceStep.GetParameter "Link to this definition")  
Retrieves the expression assigned to a template parameter.

Parameters:  **paramName** (*string*) – Name of the parameter

Returns:  Expression assigned to the parameter

Return type:  string

GetParameters()[¶](#ApiClient.TemplateBasedTraceStep.GetParameters "Link to this definition")  
Retrieves the expressions assigned to template parameters.

Returns:  A dictionary of parameter name -> parameter value (expression) mappings

Return type:  dict[str, str]

GetReferenceExpression()[¶](#ApiClient.TemplateBasedTraceStep.GetReferenceExpression "Link to this definition")  
Returns the expression of the reference.

Returns:  The expression as a string.

Return type:  str

GetReportConfig()[¶](#ApiClient.TemplateBasedTraceStep.GetReportConfig "Link to this definition")  
Returns the report config for this trace step.

Returns:  The report config object

Return type:  [`ReportConfig`](#ApiClient.ReportConfig "ApiClient.ReportConfig")

GetSignalBinding(*sigName*)[¶](#ApiClient.TemplateBasedTraceStep.GetSignalBinding "Link to this definition")  
Get the signal binding for a signal.

Parameters:  **sigName** (*str*) – Name of trace step signal

Return type:  [`SignalBinding`](#ApiClient.SignalBinding "ApiClient.SignalBinding")

Returns:  An object representing the signal binding. None if there is no generic signal bound.

GetSignalBindings()[¶](#ApiClient.TemplateBasedTraceStep.GetSignalBindings "Link to this definition")  
Get all signal bindings.

Returns:  A dictionary of mappings: input signal name -> generic signal object

Return type:  dict[str, [`SignalBinding`](#ApiClient.SignalBinding "ApiClient.SignalBinding")]

GetTags()[¶](#ApiClient.TemplateBasedTraceStep.GetTags "Link to this definition")  
Returns the tags set for this step.

Returns:  A (sorted) list of tags

Return type:  list[str]

GetTemplate()[¶](#ApiClient.TemplateBasedTraceStep.GetTemplate "Link to this definition")  
Returns the assigned trace step template.

Note:  
Use [`TraceStepTemplate.IsMissing()`](TraceStepTemplateApi.md#ApiClient.TraceStepTemplate.IsMissing "ApiClient.TraceStepTemplate.IsMissing") to check whether the trace step template file was found and loaded.

Returns:  A trace step template object.

Return type:  [`TraceStepTemplate`](TraceStepTemplateApi.md#ApiClient.TraceStepTemplate "ApiClient.TraceStepTemplate")

GetTraceSteps(*skipDisabledSteps=False*, *recursive=False*)[¶](#ApiClient.TemplateBasedTraceStep.GetTraceSteps "Link to this definition")  
Returns either direct or all children of the trace step.

Parameters:  - **skipDisabledSteps** (*boolean*) – Defines whether disabled trace steps should be excluded, defaults to False.

- **recursive** (*boolean*) – Defines whether children of children are included, defaults to False.

Returns:  The trace steps as flat list.

Return type:  list[[`TraceStep`](#ApiClient.TraceStep "ApiClient.TraceStep")]

GetType()[¶](#ApiClient.TemplateBasedTraceStep.GetType "Link to this definition")  
Returns the type (class name) of the trace step, e.g.

> - ‘Episode’
>
> - ‘AnalysisBlock’
>
> - ‘TriggerBlock’
>
> - ‘Calculation’
>
> - ‘TemplateBasedTraceStep’
>
> - ‘TraceAnalysisReference’
>
> - ‘TraceAnalysisReferenceDeprecated’

Returns:  Type (class name) of the trace step

Return type:  str

GetUuid()[¶](#ApiClient.TemplateBasedTraceStep.GetUuid "Link to this definition")  
Returns the UUID of the trace step.

Returns:  UUID of the trace step

Return type:  str

InsertTraceStep(*traceStep*, *position*)[¶](#ApiClient.TemplateBasedTraceStep.InsertTraceStep "Link to this definition")  
Adds a trace step at a certain line of the trace analysis.

Parameters:  - **traceStep** ([`TraceStep`](#ApiClient.TraceStep "ApiClient.TraceStep")) – Trace step to be added

- **position** (*integer*) – Target index of child beginning with 0

IsContainer()[¶](#ApiClient.TemplateBasedTraceStep.IsContainer "Link to this definition")  
Checks whether this trace step can contain trace steps.

Returns:  True if it can contain trace steps, else False

Return type:  boolean

IsEnabled()[¶](#ApiClient.TemplateBasedTraceStep.IsEnabled "Link to this definition")  
Checks whether the trace step is enabled.

Returns:  True if trace step is enabled, else False

Return type:  boolean

IsOk()[¶](#ApiClient.TemplateBasedTraceStep.IsOk "Link to this definition")  
Returns the internal state of correctness of the trace step.

Returns:  True if no problems were found, else False

Return type:  boolean

IsVisible()[¶](#ApiClient.TemplateBasedTraceStep.IsVisible "Link to this definition")  
Checks whether the trace step is visible. This depends on the trace step itself or a parent trace step being disabled.

Returns:  True if trace step is visible, else False

Return type:  boolean

RemoveTag(*tag*)[¶](#ApiClient.TemplateBasedTraceStep.RemoveTag "Link to this definition")  
Remove a specific tag from this step.

Parameters:  **tag** (*str*) – The tag to be removed

RemoveTraceStep(*traceStep*)[¶](#ApiClient.TemplateBasedTraceStep.RemoveTraceStep "Link to this definition")  
Removes the given trace step from the trace analysis.

Parameters:  **traceStep** ([`TraceStep`](#ApiClient.TraceStep "ApiClient.TraceStep")) – Trace step to be removed

SetDescription(*value*)[¶](#ApiClient.TemplateBasedTraceStep.SetDescription "Link to this definition")  
Sets the description of the trace analysis element.

Parameters:  **value** (*str*) – The new description

SetEnabled(*enable*)[¶](#ApiClient.TemplateBasedTraceStep.SetEnabled "Link to this definition")  
Enables or disables the trace step (this also affects child trace steps).

Parameters:  **enable** (*boolean*) – If True, enables the trace step, if False, disables the trace step

SetName(*value*)[¶](#ApiClient.TemplateBasedTraceStep.SetName "Link to this definition")  
Sets the name of the trace analysis element.

Parameters:  **value** (*str*) – The new name

SetParameter(*paramName*, *paramValue*)[¶](#ApiClient.TemplateBasedTraceStep.SetParameter "Link to this definition")  
Assigns a value to a template parameter.

Parameters:  - **paramName** (*string*) – Name of the parameter

- **paramValue** (*string*) – Value to assign to the parameter (can be an expression)

SetParameters(*paramDict*)[¶](#ApiClient.TemplateBasedTraceStep.SetParameters "Link to this definition")  
Assigns values to template parameters.

Parameters:  **paramDict** (*dict[str,* *str]*) – Dictionary of parameter name -> parameter value (expression) mappings

SetTags(*tags*)[¶](#ApiClient.TemplateBasedTraceStep.SetTags "Link to this definition")  
Set the list of tags for this step. The list of tags will be sorted and stored.

Parameters:  **tags** (*list[str]*) – The list of tags

SetTemplate(*template*, *allowInvalid=False*)[¶](#ApiClient.TemplateBasedTraceStep.SetTemplate "Link to this definition")  
Sets the referenced trace step template via object.

Parameters:  - **template** ([`TraceStepTemplate`](TraceStepTemplateApi.md#ApiClient.TraceStepTemplate "ApiClient.TraceStepTemplate")) – The trace step template object to reference

- **allowInvalid** (*bool*) – If True no exception is thrown when setting a missing or broken template

SetTemplateByReference(*templatePath*, *libraryNamespace=None*)[¶](#ApiClient.TemplateBasedTraceStep.SetTemplateByReference "Link to this definition")  
Sets the referenced trace step template via reference.

Parameters:  - **templatePath** (*str*) – relativ Path of the trace step template

- **libraryNamespace** (*str*) – namespace of the workspace library

GetTemplateId()[¶](#ApiClient.TemplateBasedTraceStep.GetTemplateId "Link to this definition")  
Returns the id of the assigned trace step template.

Returns:  The trace step template id. None if no template is set.

Return type:  str

Deprecated since version 2023.1: Please use [`GetReferenceExpression()`](#ApiClient.TemplateBasedTraceStep.GetReferenceExpression "ApiClient.TemplateBasedTraceStep.GetReferenceExpression") or [`GetAbsolutePath()`](#ApiClient.TemplateBasedTraceStep.GetAbsolutePath "ApiClient.TemplateBasedTraceStep.GetAbsolutePath") instead.

SetTemplateById(*templateId*, *allowInvalid=False*)[¶](#ApiClient.TemplateBasedTraceStep.SetTemplateById "Link to this definition")  
Sets the referenced trace step template by template id.

Note:  
The template id is a posix path to the file without the file extension (either relative to the trace step template directory or absolute). Standard trace step templates are addressed like templates in the trace step template directory.

Parameters:  - **templateId** (*str*) – The trace step template id

- **allowInvalid** (*bool*) – If True no exception is thrown when setting a missing or broken template

Deprecated since version 2023.1: Please use [`SetTemplateByReference()`](#ApiClient.TemplateBasedTraceStep.SetTemplateByReference "ApiClient.TemplateBasedTraceStep.SetTemplateByReference") instead.

## SignalBinding[¶](#signalbinding "Link to this heading")

*class* SignalBinding[¶](#ApiClient.SignalBinding "Link to this definition")  
Returned by

- [`TemplateBasedTraceStep.AssignGenericSignal`](#ApiClient.TemplateBasedTraceStep.AssignGenericSignal "ApiClient.TemplateBasedTraceStep.AssignGenericSignal")

- [`TemplateBasedTraceStep.AssignGenericSignalByName`](#ApiClient.TemplateBasedTraceStep.AssignGenericSignalByName "ApiClient.TemplateBasedTraceStep.AssignGenericSignalByName")

- [`TemplateBasedTraceStep.GetSignalBinding`](#ApiClient.TemplateBasedTraceStep.GetSignalBinding "ApiClient.TemplateBasedTraceStep.GetSignalBinding")

- [`TemplateBasedTraceStep.GetSignalBindings`](#ApiClient.TemplateBasedTraceStep.GetSignalBindings "ApiClient.TemplateBasedTraceStep.GetSignalBindings")

- [`TraceAnalysisReference.AssignGenericSignal`](#ApiClient.TraceAnalysisReference.AssignGenericSignal "ApiClient.TraceAnalysisReference.AssignGenericSignal")

- [`TraceAnalysisReference.AssignGenericSignalByName`](#ApiClient.TraceAnalysisReference.AssignGenericSignalByName "ApiClient.TraceAnalysisReference.AssignGenericSignalByName")

- [`TraceAnalysisReference.GetSignalBinding`](#ApiClient.TraceAnalysisReference.GetSignalBinding "ApiClient.TraceAnalysisReference.GetSignalBinding")

- [`TraceAnalysisReferenceDeprecated.AssignGenericSignal`](#ApiClient.TraceAnalysisReferenceDeprecated.AssignGenericSignal "ApiClient.TraceAnalysisReferenceDeprecated.AssignGenericSignal")

- [`TraceAnalysisReferenceDeprecated.AssignGenericSignalByName`](#ApiClient.TraceAnalysisReferenceDeprecated.AssignGenericSignalByName "ApiClient.TraceAnalysisReferenceDeprecated.AssignGenericSignalByName")

- [`TraceAnalysisReferenceDeprecated.GetSignalBinding`](#ApiClient.TraceAnalysisReferenceDeprecated.GetSignalBinding "ApiClient.TraceAnalysisReferenceDeprecated.GetSignalBinding")

Clone()[¶](#ApiClient.SignalBinding.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`SignalBinding`](#ApiClient.SignalBinding "ApiClient.SignalBinding")

GetGenericSignal()[¶](#ApiClient.SignalBinding.GetGenericSignal "Link to this definition")  
Get the bound generic signal.

Returns:  The generic signal. Can be None.

Return type:  [`GenericSignal`](#ApiClient.GenericSignal "ApiClient.GenericSignal")

GetUnit()[¶](#ApiClient.SignalBinding.GetUnit "Link to this definition")  
Returns the default unit that will be used if a trace step (e.g. a plot) uses this signal.

Returns:  The default unit (default: “don’t care”)

Return type:  str

IsOptional()[¶](#ApiClient.SignalBinding.IsOptional "Link to this definition")  
Checks whether the bound generic signal is optionally bound to a recording signal.

Note:  
The value True for this flag is only valid if the trace step template signal is marked as optional.

Returns:  True if it is optional, else False

Return type:  boolean

SetGenericSignal(*genericSignal*)[¶](#ApiClient.SignalBinding.SetGenericSignal "Link to this definition")  
Set a new generic signal to be bound.

Parameters:  **genericSignal** ([`GenericSignal`](#ApiClient.GenericSignal "ApiClient.GenericSignal")) – The generic signal

SetOptional(*optional*)[¶](#ApiClient.SignalBinding.SetOptional "Link to this definition")  
Set whether the bound generic signal is optionally bound to a recording signal.

Note:  
The value True for this flag is only valid if the trace step template signal is marked as optional.

Parameters:  **optional** (*boolean*) – The new value

SetUnit(*unit*)[¶](#ApiClient.SignalBinding.SetUnit "Link to this definition")  
Set the default unit that will be used if a trace step (e.g. a plot) uses this signal.

Parameters:  **unit** (*str*) – The default unit (default: “don’t care”). Use None or ‘don’t care’ to set it to its default value.

## GenericSignal[¶](#genericsignal "Link to this heading")

*class* GenericSignal[¶](#ApiClient.GenericSignal "Link to this definition")  
Returned by

- [`SignalBinding.GetGenericSignal`](#ApiClient.SignalBinding.GetGenericSignal "ApiClient.SignalBinding.GetGenericSignal")

- [`TraceAnalysis.GetConditionalGenericSignals`](#ApiClient.TraceAnalysis.GetConditionalGenericSignals "ApiClient.TraceAnalysis.GetConditionalGenericSignals")

- [`TraceAnalysis.GetGenericSignal`](#ApiClient.TraceAnalysis.GetGenericSignal "ApiClient.TraceAnalysis.GetGenericSignal")

- [`TraceAnalysis.GetGenericSignals`](#ApiClient.TraceAnalysis.GetGenericSignals "ApiClient.TraceAnalysis.GetGenericSignals")

- [`TraceAnalysis.GetMandatoryGenericSignals`](#ApiClient.TraceAnalysis.GetMandatoryGenericSignals "ApiClient.TraceAnalysis.GetMandatoryGenericSignals")

- [`TraceAnalysis.GetOptionalGenericSignals`](#ApiClient.TraceAnalysis.GetOptionalGenericSignals "ApiClient.TraceAnalysis.GetOptionalGenericSignals")

- [`TraceAnalysisApi.CreateGenericSignal`](#ApiClient.TraceAnalysisApi.CreateGenericSignal "ApiClient.TraceAnalysisApi.CreateGenericSignal")

AssignMappingItem(*mappingItemName*)[¶](#ApiClient.GenericSignal.AssignMappingItem "Link to this definition")  
Assigns the mapping item with the given name to the generic signal.

Note:  
This method is only valid for analysis packages (type [`AnalysisPackage`](PackageApi.md#ApiClient.AnalysisPackage "ApiClient.AnalysisPackage"))!

Parameters:  **mappingItemName** (*str*) – The name of a valid mapping item.

AssignRecordingSignal(*recordingGroup*, *mappingItemName*)[¶](#ApiClient.GenericSignal.AssignRecordingSignal "Link to this definition")  
Assigns a signal of recording group to the generic signal by specifying a recording group and a valid mapping item name of the parent signal group.

Note:  
This method is only valid for packages (type [`Package`](PackageApi.md#ApiClient.Package "ApiClient.Package"))!

Parameters:  - **recordingGroup** ([`RecordingGroupBase`](#ApiClient.RecordingGroupBase "ApiClient.RecordingGroupBase")) – The recording group of the signal

- **mappingItemName** (*str*) – The name of signal to be assigned. It has to be a signal contained in the parent signal group of the recording group.

Clone()[¶](#ApiClient.GenericSignal.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`GenericSignal`](#ApiClient.GenericSignal "ApiClient.GenericSignal")

GetAssignedMappingItemName()[¶](#ApiClient.GenericSignal.GetAssignedMappingItemName "Link to this definition")  
Returns the name of the mapping item of the recoding group signal assigned to the generic signal.

Returns:  Name of the assigned mapping item.

Return type:  str

GetAssignedRecordingGroupName()[¶](#ApiClient.GenericSignal.GetAssignedRecordingGroupName "Link to this definition")  
Returns the name of the recording group the assigned recoding group signal belongs to, if there is any mapping item assigned to the generic signal.

Returns:  Name of the recording group the assigned recoding group signal belongs to.

Return type:  str

GetDefaultUnit()[¶](#ApiClient.GenericSignal.GetDefaultUnit "Link to this definition")  
Returns the string representation of the default unit that will be used if a trace step (e.g. a plot) uses this signal.

Note:  
The default unit will not be used if the generic signal is calculated or it is not interpreted as number.

Returns:  The default unit (default: ‘don’t care’)

Return type:  str

GetName()[¶](#ApiClient.GenericSignal.GetName "Link to this definition")  
Returns the name of the generic signal.

Returns:  The name

Return type:  str

GetSignalType()[¶](#ApiClient.GenericSignal.GetSignalType "Link to this definition")  
Returns the signal type to be read.

Returns:  The signal type. Possible values: “PHY”, “RAW”, “STR”

Return type:  string

IsCalculated()[¶](#ApiClient.GenericSignal.IsCalculated "Link to this definition")  
Returns whether the generic signal is calculated during the trace analysis.

Returns:  True, if the signal is calculated

Return type:  bool

IsOptional()[¶](#ApiClient.GenericSignal.IsOptional "Link to this definition")  
Returns whether this generic signals optional flag is set.

Note:  
This flag will be used for trace steps that have no own option to mark a signal as optional. If this flag is set, it is valid that a signal is not found in a recording or the mapping path could not be resolved.

Returns:  The optional flag

Return type:  boolean

SetDefaultUnit(*unit*)[¶](#ApiClient.GenericSignal.SetDefaultUnit "Link to this definition")  
Set the default unit that will be used if a trace step (e.g. a plot) uses this signal, by the given string representation (e.g. ‘km/h’).

Note:  
The default unit will not be used if the generic signal is calculated or it is not interpreted as number.

Parameters:  **unit** (*str*) – The default unit (default: ‘don’t care’). Use None or ‘don’t care’ to set it to its default value.

SetName(*name*)[¶](#ApiClient.GenericSignal.SetName "Link to this definition")  
Sets the name of the generic signal.

Parameters:  **name** (*str*) – The new name

SetOptional(*optional*)[¶](#ApiClient.GenericSignal.SetOptional "Link to this definition")  
Set the optional flag for the generic signal.

Note:  
This flag will be used for trace steps that have no own option to mark a signal as optional. If this flag is set, it is valid that a signal is not found in a recording or the mapping path could not be resolved.

Parameters:  **optional** (*boolean*) – The new value

SetSignalType(*signalType*)[¶](#ApiClient.GenericSignal.SetSignalType "Link to this definition")  
Set the signal type to be read.

Parameters:  **signalType** (*string*) – The signal type: possible values: “PHY”, “RAW”, “STR”

## RecordingGroupBase[¶](#recordinggroupbase "Link to this heading")

*class* RecordingGroupBase[¶](#ApiClient.RecordingGroupBase "Link to this definition")  
Subclasses

- [`AutoAssignRecordingGroup`](PackageApi.md#ApiClient.AutoAssignRecordingGroup "ApiClient.AutoAssignRecordingGroup")

- [`RecordingGroup`](SignalRecordingApi.md#ApiClient.RecordingGroup "ApiClient.RecordingGroup")

- [`VariableRecordingGroup`](PackageApi.md#ApiClient.VariableRecordingGroup "ApiClient.VariableRecordingGroup")

Clone()[¶](#ApiClient.RecordingGroupBase.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`RecordingGroupBase`](#ApiClient.RecordingGroupBase "ApiClient.RecordingGroupBase")

GetConditionalSignalNamesForTraceAnalyses()[¶](#ApiClient.RecordingGroupBase.GetConditionalSignalNamesForTraceAnalyses "Link to this definition")  
Returns the list of signal names that can be optional or mandatory for running the trace analyses depending on the values of global constants.

Returns:  The list of undetermined signal names.

Return type:  list[str]

GetMandatorySignalNamesForTraceAnalyses()[¶](#ApiClient.RecordingGroupBase.GetMandatorySignalNamesForTraceAnalyses "Link to this definition")  
Returns the list of signal names that are mandatory for running the trace analyses.

Returns:  The list of mandatory signal names.

Return type:  list[str]

GetName()[¶](#ApiClient.RecordingGroupBase.GetName "Link to this definition")  
Returns the name of a recording group.

Returns:  the name

Return type:  str

GetOptionalSignalNamesForTraceAnalyses()[¶](#ApiClient.RecordingGroupBase.GetOptionalSignalNamesForTraceAnalyses "Link to this definition")  
Returns the list of signal names that are optional for running the trace analyses.

Returns:  The list of optional signal names.

Return type:  list[str]

GetSignalGroup()[¶](#ApiClient.RecordingGroupBase.GetSignalGroup "Link to this definition")  
Returns the parent signal group.

Returns:  The parent signal group

Return type:  [`SignalGroupBase`](SignalRecordingApi.md#ApiClient.SignalGroupBase "ApiClient.SignalGroupBase")

SetName(*name*)[¶](#ApiClient.RecordingGroupBase.SetName "Link to this definition")  
Sets the name of the recording group.

Parameters:  **name** (*str*) – The new name

GetDescription()[¶](#ApiClient.RecordingGroupBase.GetDescription "Link to this definition")  
Returns the description of the recording group.

Returns:  The description of the recording group.

Return type:  str

Deprecated since version 2020.1: The description of the recording group is not visible in the GUI. Please use the description of the signal group instead.

IsLogRecording()[¶](#ApiClient.RecordingGroupBase.IsLogRecording "Link to this definition")  
Returns whether the recording group is a log recording.

Returns:  True if the recording group is a log recording else False

Return type:  bool

Deprecated since version 2022.1: LogRecording was removed. All recording groups are SignalRecordings.

IsSignalRecording()[¶](#ApiClient.RecordingGroupBase.IsSignalRecording "Link to this definition")  
Returns whether the recording group is a signal recording.

Returns:  True if the recording group is a signal recording else False

Return type:  bool

Deprecated since version 2022.1: LogRecording was removed. All recording groups are SignalRecordings.

SetDescription(*description*)[¶](#ApiClient.RecordingGroupBase.SetDescription "Link to this definition")  
Sets the description of the recording group.

Parameters:  **description** (*str*) – The new description of the recording group.

Deprecated since version 2020.1: The description of the recording group is not visible in the GUI. Please use the description of the signal group instead.

## Episode[¶](#episode "Link to this heading")

*class* Episode[¶](#ApiClient.Episode "Link to this definition")  
Base classes

- [`TraceStep`](#ApiClient.TraceStep "ApiClient.TraceStep")

- [`TraceStepContainer`](#ApiClient.TraceStepContainer "ApiClient.TraceStepContainer")

Returned by

- [`TraceAnalysisApi.CreateEpisode`](#ApiClient.TraceAnalysisApi.CreateEpisode "ApiClient.TraceAnalysisApi.CreateEpisode")

AddTag(*tag*)[¶](#ApiClient.Episode.AddTag "Link to this definition")  
Add a specific tag to this step.

Parameters:  **tag** (*str*) – The tag to be set

AppendTraceStep(*traceStep*)[¶](#ApiClient.Episode.AppendTraceStep "Link to this definition")  
Adds a trace step at the end of its children.

Parameters:  **traceStep** ([`TraceStep`](#ApiClient.TraceStep "ApiClient.TraceStep")) – Trace step to be added

Clone()[¶](#ApiClient.Episode.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`Episode`](#ApiClient.Episode "ApiClient.Episode")

GetDescription()[¶](#ApiClient.Episode.GetDescription "Link to this definition")  
Returns the description of the trace analysis element.

Returns:  The description

Return type:  str

GetLineNo()[¶](#ApiClient.Episode.GetLineNo "Link to this definition")  
Returns the trace steps line number within its trace analysis.

Returns:  Line number

Return type:  int

GetName()[¶](#ApiClient.Episode.GetName "Link to this definition")  
Returns the name of the trace analysis element.

Returns:  The name

Return type:  str

GetTags()[¶](#ApiClient.Episode.GetTags "Link to this definition")  
Returns the tags set for this step.

Returns:  A (sorted) list of tags

Return type:  list[str]

GetTraceSteps(*skipDisabledSteps=False*, *recursive=False*)[¶](#ApiClient.Episode.GetTraceSteps "Link to this definition")  
Returns either direct or all children of the trace step.

Parameters:  - **skipDisabledSteps** (*boolean*) – Defines whether disabled trace steps should be excluded, defaults to False.

- **recursive** (*boolean*) – Defines whether children of children are included, defaults to False.

Returns:  The trace steps as flat list.

Return type:  list[[`TraceStep`](#ApiClient.TraceStep "ApiClient.TraceStep")]

GetType()[¶](#ApiClient.Episode.GetType "Link to this definition")  
Returns the type (class name) of the trace step, e.g.

> - ‘Episode’
>
> - ‘AnalysisBlock’
>
> - ‘TriggerBlock’
>
> - ‘Calculation’
>
> - ‘TemplateBasedTraceStep’
>
> - ‘TraceAnalysisReference’
>
> - ‘TraceAnalysisReferenceDeprecated’

Returns:  Type (class name) of the trace step

Return type:  str

GetUuid()[¶](#ApiClient.Episode.GetUuid "Link to this definition")  
Returns the UUID of the trace step.

Returns:  UUID of the trace step

Return type:  str

InsertTraceStep(*traceStep*, *position*)[¶](#ApiClient.Episode.InsertTraceStep "Link to this definition")  
Adds a trace step at a certain line of the trace analysis.

Parameters:  - **traceStep** ([`TraceStep`](#ApiClient.TraceStep "ApiClient.TraceStep")) – Trace step to be added

- **position** (*integer*) – Target index of child beginning with 0

IsContainer()[¶](#ApiClient.Episode.IsContainer "Link to this definition")  
Checks whether this trace step can contain trace steps.

Returns:  True if it can contain trace steps, else False

Return type:  boolean

IsEnabled()[¶](#ApiClient.Episode.IsEnabled "Link to this definition")  
Checks whether the trace step is enabled.

Returns:  True if trace step is enabled, else False

Return type:  boolean

IsOk()[¶](#ApiClient.Episode.IsOk "Link to this definition")  
Returns the internal state of correctness of the trace step.

Returns:  True if no problems were found, else False

Return type:  boolean

IsVisible()[¶](#ApiClient.Episode.IsVisible "Link to this definition")  
Checks whether the trace step is visible. This depends on the trace step itself or a parent trace step being disabled.

Returns:  True if trace step is visible, else False

Return type:  boolean

RemoveTag(*tag*)[¶](#ApiClient.Episode.RemoveTag "Link to this definition")  
Remove a specific tag from this step.

Parameters:  **tag** (*str*) – The tag to be removed

RemoveTraceStep(*traceStep*)[¶](#ApiClient.Episode.RemoveTraceStep "Link to this definition")  
Removes the given trace step from the trace analysis.

Parameters:  **traceStep** ([`TraceStep`](#ApiClient.TraceStep "ApiClient.TraceStep")) – Trace step to be removed

SetDescription(*value*)[¶](#ApiClient.Episode.SetDescription "Link to this definition")  
Sets the description of the trace analysis element.

Parameters:  **value** (*str*) – The new description

SetEnabled(*enable*)[¶](#ApiClient.Episode.SetEnabled "Link to this definition")  
Enables or disables the trace step (this also affects child trace steps).

Parameters:  **enable** (*boolean*) – If True, enables the trace step, if False, disables the trace step

SetName(*value*)[¶](#ApiClient.Episode.SetName "Link to this definition")  
Sets the name of the trace analysis element.

Parameters:  **value** (*str*) – The new name

SetTags(*tags*)[¶](#ApiClient.Episode.SetTags "Link to this definition")  
Set the list of tags for this step. The list of tags will be sorted and stored.

Parameters:  **tags** (*list[str]*) – The list of tags

## SignalRecording[¶](#signalrecording "Link to this heading")

*class* SignalRecording[¶](#ApiClient.SignalRecording "Link to this definition")  
Base classes

- [`TraceStep`](#ApiClient.TraceStep "ApiClient.TraceStep")

- [`TraceStepContainer`](#ApiClient.TraceStepContainer "ApiClient.TraceStepContainer")

Returned by

- [`TraceAnalysisApi.CreateSignalRecording`](#ApiClient.TraceAnalysisApi.CreateSignalRecording "ApiClient.TraceAnalysisApi.CreateSignalRecording")

AddGenericSignal(*genSig*)[¶](#ApiClient.SignalRecording.AddGenericSignal "Link to this definition")  
Adds a generic signal to this signal recording.

Parameters:  **genSig** ([`GenericSignal`](#ApiClient.GenericSignal "ApiClient.GenericSignal")) – A generic signal

AddGenericSignalByName(*name*)[¶](#ApiClient.SignalRecording.AddGenericSignalByName "Link to this definition")  
Adds a generic signal by name to this signal recording.

Parameters:  **name** (*str*) – The name of the generic signal

AddTag(*tag*)[¶](#ApiClient.SignalRecording.AddTag "Link to this definition")  
Add a specific tag to this step.

Parameters:  **tag** (*str*) – The tag to be set

AppendTraceStep(*traceStep*)[¶](#ApiClient.SignalRecording.AppendTraceStep "Link to this definition")  
Adds a trace step at the end of its children.

Parameters:  **traceStep** ([`TraceStep`](#ApiClient.TraceStep "ApiClient.TraceStep")) – Trace step to be added

Clone()[¶](#ApiClient.SignalRecording.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`SignalRecording`](#ApiClient.SignalRecording "ApiClient.SignalRecording")

EnableCompression(*enable=True*)[¶](#ApiClient.SignalRecording.EnableCompression "Link to this definition")  
Sets whether data should be compressed. Compression is only applied to MDF4 file format!

Parameters:  **enable** (*boolean*) – True if data compression should be applied else False.

GetCsvFormatDetailsString()[¶](#ApiClient.SignalRecording.GetCsvFormatDetailsString "Link to this definition")  
Returns the CSV format details string.

Return type:  str

Returns:  the FormatDetails

GetDescription()[¶](#ApiClient.SignalRecording.GetDescription "Link to this definition")  
Returns the description of the trace analysis element.

Returns:  The description

Return type:  str

GetFileExpression()[¶](#ApiClient.SignalRecording.GetFileExpression "Link to this definition")  
Returns the file expression of the trace file.

Returns:  The path expression

Return type:  str

GetGenericSignalNames()[¶](#ApiClient.SignalRecording.GetGenericSignalNames "Link to this definition")  
Returns the names of the generic signals that are registered for signal recording.

Returns:  List of generic signal names

Return type:  list[str]

GetLineNo()[¶](#ApiClient.SignalRecording.GetLineNo "Link to this definition")  
Returns the trace steps line number within its trace analysis.

Returns:  Line number

Return type:  int

GetName()[¶](#ApiClient.SignalRecording.GetName "Link to this definition")  
Returns the name of the trace analysis element.

Returns:  The name

Return type:  str

GetRecordAllSignals()[¶](#ApiClient.SignalRecording.GetRecordAllSignals "Link to this definition")  
Returns whether all available signals are recorded.

Returns:  recordAllSignals

Return type:  boolean

GetSignalNameType()[¶](#ApiClient.SignalRecording.GetSignalNameType "Link to this definition")  
Returns which kind of name for the signal names is shown in the plot.

Returns:  ‘generic’, ‘mapping’, ‘mappingtarget’ or ‘file’

Return type:  str

GetStoreType()[¶](#ApiClient.SignalRecording.GetStoreType "Link to this definition")  
Returns the type of the file format.

Returns:  The type of the file format. ‘CSV’, ‘MDF3’, ‘MDF4’ or ‘ASTRACE’.

Return type:  str

GetTags()[¶](#ApiClient.SignalRecording.GetTags "Link to this definition")  
Returns the tags set for this step.

Returns:  A (sorted) list of tags

Return type:  list[str]

GetTraceSteps(*skipDisabledSteps=False*, *recursive=False*)[¶](#ApiClient.SignalRecording.GetTraceSteps "Link to this definition")  
Returns either direct or all children of the trace step.

Parameters:  - **skipDisabledSteps** (*boolean*) – Defines whether disabled trace steps should be excluded, defaults to False.

- **recursive** (*boolean*) – Defines whether children of children are included, defaults to False.

Returns:  The trace steps as flat list.

Return type:  list[[`TraceStep`](#ApiClient.TraceStep "ApiClient.TraceStep")]

GetType()[¶](#ApiClient.SignalRecording.GetType "Link to this definition")  
Returns the type (class name) of the trace step, e.g.

> - ‘Episode’
>
> - ‘AnalysisBlock’
>
> - ‘TriggerBlock’
>
> - ‘Calculation’
>
> - ‘TemplateBasedTraceStep’
>
> - ‘TraceAnalysisReference’
>
> - ‘TraceAnalysisReferenceDeprecated’

Returns:  Type (class name) of the trace step

Return type:  str

GetUuid()[¶](#ApiClient.SignalRecording.GetUuid "Link to this definition")  
Returns the UUID of the trace step.

Returns:  UUID of the trace step

Return type:  str

InsertTraceStep(*traceStep*, *position*)[¶](#ApiClient.SignalRecording.InsertTraceStep "Link to this definition")  
Adds a trace step at a certain line of the trace analysis.

Parameters:  - **traceStep** ([`TraceStep`](#ApiClient.TraceStep "ApiClient.TraceStep")) – Trace step to be added

- **position** (*integer*) – Target index of child beginning with 0

IsCompressionEnabled()[¶](#ApiClient.SignalRecording.IsCompressionEnabled "Link to this definition")  
Returns whether the data compression is enabled. Compression is only applied to MDF4 file format!

Returns:  True if compression is enabled else False.

Return type:  boolean

IsContainer()[¶](#ApiClient.SignalRecording.IsContainer "Link to this definition")  
Checks whether this trace step can contain trace steps.

Returns:  True if it can contain trace steps, else False

Return type:  boolean

IsEnabled()[¶](#ApiClient.SignalRecording.IsEnabled "Link to this definition")  
Checks whether the trace step is enabled.

Returns:  True if trace step is enabled, else False

Return type:  boolean

IsOk()[¶](#ApiClient.SignalRecording.IsOk "Link to this definition")  
Returns the internal state of correctness of the trace step.

Returns:  True if no problems were found, else False

Return type:  boolean

IsVisible()[¶](#ApiClient.SignalRecording.IsVisible "Link to this definition")  
Checks whether the trace step is visible. This depends on the trace step itself or a parent trace step being disabled.

Returns:  True if trace step is visible, else False

Return type:  boolean

RemoveGenericSignal(*genSig*)[¶](#ApiClient.SignalRecording.RemoveGenericSignal "Link to this definition")  
Removes a generic signal from the signal recording.

Parameters:  **genSig** ([`GenericSignal`](#ApiClient.GenericSignal "ApiClient.GenericSignal")) – Generic signal to be removed

Raises:  
**ApiError** – When the given generic signal is not part of the signal recording

RemoveGenericSignalByName(*name*)[¶](#ApiClient.SignalRecording.RemoveGenericSignalByName "Link to this definition")  
Removes a generic signal by name from the signal recording.

Parameters:  **name** (*str*) – Name of the generic signal to be removed

Raises:  
**ApiError** – When the given generic signal is not part of the signal recording

RemoveTag(*tag*)[¶](#ApiClient.SignalRecording.RemoveTag "Link to this definition")  
Remove a specific tag from this step.

Parameters:  **tag** (*str*) – The tag to be removed

RemoveTraceStep(*traceStep*)[¶](#ApiClient.SignalRecording.RemoveTraceStep "Link to this definition")  
Removes the given trace step from the trace analysis.

Parameters:  **traceStep** ([`TraceStep`](#ApiClient.TraceStep "ApiClient.TraceStep")) – Trace step to be removed

SetCsvFormatDetailsString(*formatDetails*)[¶](#ApiClient.SignalRecording.SetCsvFormatDetailsString "Link to this definition")  
Sets the CSV format details.

The format details define which characters will be used for the column separator, the decimal separator, and the thousand separator.

The default csvFormatDetailsString is `"columnSeparator: ';', decimalSeparator: '.', thousandSeparator: ''"`.

Note

Not all parameters must be contained in the string as the missing parameters are set to the defaults.

Note

This method ignores the entries “headLineNumber” and “timeColumn” if they exist in the csvFormatDetailsString.

Parameters:  **formatDetails** (*str*) – the FormatDetails

SetDescription(*value*)[¶](#ApiClient.SignalRecording.SetDescription "Link to this definition")  
Sets the description of the trace analysis element.

Parameters:  **value** (*str*) – The new description

SetEnabled(*enable*)[¶](#ApiClient.SignalRecording.SetEnabled "Link to this definition")  
Enables or disables the trace step (this also affects child trace steps).

Parameters:  **enable** (*boolean*) – If True, enables the trace step, if False, disables the trace step

SetFileExpression(*expression*)[¶](#ApiClient.SignalRecording.SetFileExpression "Link to this definition")  
Sets the file expression of the trace file.

Parameters:  **expression** (*str*) – The path expression

SetGenericSignalNames(*genericSignalNames*)[¶](#ApiClient.SignalRecording.SetGenericSignalNames "Link to this definition")  
Sets the names of the generic signals to be recorded in this signal recording.

Parameters:  **genericSignalNames** (*list[str]*)

SetName(*value*)[¶](#ApiClient.SignalRecording.SetName "Link to this definition")  
Sets the name of the trace analysis element.

Parameters:  **value** (*str*) – The new name

SetRecordAllSignals(*recordAllSignals=True*)[¶](#ApiClient.SignalRecording.SetRecordAllSignals "Link to this definition")  
Sets whether all available signals are recorded (default=True).

Parameters:  **recordAllSignals** (*boolean*) – new value (default=True)

SetSignalNameType(*signalNameType*)[¶](#ApiClient.SignalRecording.SetSignalNameType "Link to this definition")  
Sets which kind of names for the signals are shown in the plot.

Parameters:  **signalNameType** (*str*) – ‘generic’, ‘mapping’, ‘mappingTarget’ or ‘file’ - ‘generic’: name of the generic signal - ‘mapping’: name of the signal in the mapping view - ‘mappingtarget’: name of mapping target of the signal - ‘file’: name of the signal in the recording file

SetStoreType(*storeType*)[¶](#ApiClient.SignalRecording.SetStoreType "Link to this definition")  
Sets the type of the file format. Possible values: ‘CSV’, ‘MDF3’, ‘MDF4’, ‘ASTRACE’. For compatibility reasons value ‘MDF’ is accepted and is equivalent to ‘MDF3’.

Parameters:  **storeType** (*str*) – The new type of the file format.

SetTags(*tags*)[¶](#ApiClient.SignalRecording.SetTags "Link to this definition")  
Set the list of tags for this step. The list of tags will be sorted and stored.

Parameters:  **tags** (*list[str]*) – The list of tags

## IfDef[¶](#ifdef "Link to this heading")

*class* IfDef[¶](#ApiClient.IfDef "Link to this definition")  
Base classes

- [`TraceStep`](#ApiClient.TraceStep "ApiClient.TraceStep")

- [`TraceStepContainer`](#ApiClient.TraceStepContainer "ApiClient.TraceStepContainer")

Returned by

- [`TraceAnalysisApi.CreateIfDef`](#ApiClient.TraceAnalysisApi.CreateIfDef "ApiClient.TraceAnalysisApi.CreateIfDef")

AddTag(*tag*)[¶](#ApiClient.IfDef.AddTag "Link to this definition")  
Add a specific tag to this step.

Parameters:  **tag** (*str*) – The tag to be set

AppendTraceStep(*traceStep*)[¶](#ApiClient.IfDef.AppendTraceStep "Link to this definition")  
Adds a trace step at the end of its children.

Parameters:  **traceStep** ([`TraceStep`](#ApiClient.TraceStep "ApiClient.TraceStep")) – Trace step to be added

Clone()[¶](#ApiClient.IfDef.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`IfDef`](#ApiClient.IfDef "ApiClient.IfDef")

GetCondition()[¶](#ApiClient.IfDef.GetCondition "Link to this definition")  
Returns the condition of IfDef block.

Returns:  Condition of IfDef block

Return type:  str

GetDescription()[¶](#ApiClient.IfDef.GetDescription "Link to this definition")  
Returns always an empty string, because IfDef blocks currently have no description.

Returns:  The description

Return type:  str

GetLineNo()[¶](#ApiClient.IfDef.GetLineNo "Link to this definition")  
Returns the trace steps line number within its trace analysis.

Returns:  Line number

Return type:  int

GetName()[¶](#ApiClient.IfDef.GetName "Link to this definition")  
Returns the name of the trace analysis element.

Returns:  The name

Return type:  str

GetTags()[¶](#ApiClient.IfDef.GetTags "Link to this definition")  
Returns the tags set for this step.

Returns:  A (sorted) list of tags

Return type:  list[str]

GetTraceSteps(*skipDisabledSteps=False*, *recursive=False*)[¶](#ApiClient.IfDef.GetTraceSteps "Link to this definition")  
Returns either direct or all children of the trace step.

Parameters:  - **skipDisabledSteps** (*boolean*) – Defines whether disabled trace steps should be excluded, defaults to False.

- **recursive** (*boolean*) – Defines whether children of children are included, defaults to False.

Returns:  The trace steps as flat list.

Return type:  list[[`TraceStep`](#ApiClient.TraceStep "ApiClient.TraceStep")]

GetType()[¶](#ApiClient.IfDef.GetType "Link to this definition")  
Returns the type (class name) of the trace step, e.g.

> - ‘Episode’
>
> - ‘AnalysisBlock’
>
> - ‘TriggerBlock’
>
> - ‘Calculation’
>
> - ‘TemplateBasedTraceStep’
>
> - ‘TraceAnalysisReference’
>
> - ‘TraceAnalysisReferenceDeprecated’

Returns:  Type (class name) of the trace step

Return type:  str

GetUuid()[¶](#ApiClient.IfDef.GetUuid "Link to this definition")  
Returns the UUID of the trace step.

Returns:  UUID of the trace step

Return type:  str

InsertTraceStep(*traceStep*, *position*)[¶](#ApiClient.IfDef.InsertTraceStep "Link to this definition")  
Adds a trace step at a certain line of the trace analysis.

Parameters:  - **traceStep** ([`TraceStep`](#ApiClient.TraceStep "ApiClient.TraceStep")) – Trace step to be added

- **position** (*integer*) – Target index of child beginning with 0

IsContainer()[¶](#ApiClient.IfDef.IsContainer "Link to this definition")  
Checks whether this trace step can contain trace steps.

Returns:  True if it can contain trace steps, else False

Return type:  boolean

IsEnabled()[¶](#ApiClient.IfDef.IsEnabled "Link to this definition")  
Checks whether the trace step is enabled.

Returns:  True if trace step is enabled, else False

Return type:  boolean

IsOk()[¶](#ApiClient.IfDef.IsOk "Link to this definition")  
Returns the internal state of correctness of the trace step.

Returns:  True if no problems were found, else False

Return type:  boolean

IsVisible()[¶](#ApiClient.IfDef.IsVisible "Link to this definition")  
Checks whether the trace step is visible. This depends on the trace step itself or a parent trace step being disabled.

Returns:  True if trace step is visible, else False

Return type:  boolean

RemoveTag(*tag*)[¶](#ApiClient.IfDef.RemoveTag "Link to this definition")  
Remove a specific tag from this step.

Parameters:  **tag** (*str*) – The tag to be removed

RemoveTraceStep(*traceStep*)[¶](#ApiClient.IfDef.RemoveTraceStep "Link to this definition")  
Removes the given trace step from the trace analysis.

Parameters:  **traceStep** ([`TraceStep`](#ApiClient.TraceStep "ApiClient.TraceStep")) – Trace step to be removed

SetCondition(*condition*)[¶](#ApiClient.IfDef.SetCondition "Link to this definition")  
Sets the condition of IfDef block.

Parameters:  **condition** (*str*) – Condition of IfDef block

SetDescription(*value*)[¶](#ApiClient.IfDef.SetDescription "Link to this definition")  
No operation. An IfDef block does not have a description.

Parameters:  **value** (*str*) – The new description

SetEnabled(*enable*)[¶](#ApiClient.IfDef.SetEnabled "Link to this definition")  
No operation. An IfDef block is automatically enabled or disabled by its condition and cannot be enabled or disabled by the user.

Parameters:  **enable** (*boolean*) – If True, enables the trace step, if False, disables the trace step

SetName(*name*)[¶](#ApiClient.IfDef.SetName "Link to this definition")  
No operation. The name of an IfDef block cannot be changed.

Parameters:  **name** (*str*) – The new name

SetTags(*tags*)[¶](#ApiClient.IfDef.SetTags "Link to this definition")  
Set the list of tags for this step. The list of tags will be sorted and stored.

Parameters:  **tags** (*list[str]*) – The list of tags

## IfThenElse[¶](#ifthenelse "Link to this heading")

*class* IfThenElse[¶](#ApiClient.IfThenElse "Link to this definition")  
Base classes

- [`TraceStep`](#ApiClient.TraceStep "ApiClient.TraceStep")

- [`TraceStepContainer`](#ApiClient.TraceStepContainer "ApiClient.TraceStepContainer")

Returned by

- [`TraceAnalysisApi.CreateIfThenElse`](#ApiClient.TraceAnalysisApi.CreateIfThenElse "ApiClient.TraceAnalysisApi.CreateIfThenElse")

AddTag(*tag*)[¶](#ApiClient.IfThenElse.AddTag "Link to this definition")  
Add a specific tag to this step.

Parameters:  **tag** (*str*) – The tag to be set

Clone()[¶](#ApiClient.IfThenElse.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`IfThenElse`](#ApiClient.IfThenElse "ApiClient.IfThenElse")

GetCondition()[¶](#ApiClient.IfThenElse.GetCondition "Link to this definition")  
Returns the condition of the IfThenElse block.

Returns:  Condition of the IfThenElse block

Return type:  str

GetDescription()[¶](#ApiClient.IfThenElse.GetDescription "Link to this definition")  
Returns the description of the trace analysis element.

Returns:  The description

Return type:  str

GetElseNode()[¶](#ApiClient.IfThenElse.GetElseNode "Link to this definition")  
Returns the “else” node.

Returns:  the “else” node

Return type:  [`ElseNode`](#ApiClient.ElseNode "ApiClient.ElseNode")

GetLineNo()[¶](#ApiClient.IfThenElse.GetLineNo "Link to this definition")  
Returns the trace steps line number within its trace analysis.

Returns:  Line number

Return type:  int

GetName()[¶](#ApiClient.IfThenElse.GetName "Link to this definition")  
Returns the name of the trace analysis element.

Returns:  The name

Return type:  str

GetTags()[¶](#ApiClient.IfThenElse.GetTags "Link to this definition")  
Returns the tags set for this step.

Returns:  A (sorted) list of tags

Return type:  list[str]

GetThenNode()[¶](#ApiClient.IfThenElse.GetThenNode "Link to this definition")  
Returns the “then” node.

Returns:  the “then” node

Return type:  [`ThenNode`](#ApiClient.ThenNode "ApiClient.ThenNode")

GetTraceSteps(*skipDisabledSteps=False*, *recursive=False*)[¶](#ApiClient.IfThenElse.GetTraceSteps "Link to this definition")  
Returns either direct or all children of the trace step.

Parameters:  - **skipDisabledSteps** (*boolean*) – Defines whether disabled trace steps should be excluded, defaults to False.

- **recursive** (*boolean*) – Defines whether children of children are included, defaults to False.

Returns:  The trace steps as flat list.

Return type:  list[[`TraceStep`](#ApiClient.TraceStep "ApiClient.TraceStep")]

GetType()[¶](#ApiClient.IfThenElse.GetType "Link to this definition")  
Returns the type (class name) of the trace step, e.g.

> - ‘Episode’
>
> - ‘AnalysisBlock’
>
> - ‘TriggerBlock’
>
> - ‘Calculation’
>
> - ‘TemplateBasedTraceStep’
>
> - ‘TraceAnalysisReference’
>
> - ‘TraceAnalysisReferenceDeprecated’

Returns:  Type (class name) of the trace step

Return type:  str

GetUuid()[¶](#ApiClient.IfThenElse.GetUuid "Link to this definition")  
Returns the UUID of the trace step.

Returns:  UUID of the trace step

Return type:  str

IsContainer()[¶](#ApiClient.IfThenElse.IsContainer "Link to this definition")  
Checks whether this trace step can contain trace steps.

Returns:  True if it can contain trace steps, else False

Return type:  boolean

IsEnabled()[¶](#ApiClient.IfThenElse.IsEnabled "Link to this definition")  
Checks whether the trace step is enabled.

Returns:  True if trace step is enabled, else False

Return type:  boolean

IsOk()[¶](#ApiClient.IfThenElse.IsOk "Link to this definition")  
Returns the internal state of correctness of the trace step.

Returns:  True if no problems were found, else False

Return type:  boolean

IsVisible()[¶](#ApiClient.IfThenElse.IsVisible "Link to this definition")  
Checks whether the trace step is visible. This depends on the trace step itself or a parent trace step being disabled.

Returns:  True if trace step is visible, else False

Return type:  boolean

RemoveTag(*tag*)[¶](#ApiClient.IfThenElse.RemoveTag "Link to this definition")  
Remove a specific tag from this step.

Parameters:  **tag** (*str*) – The tag to be removed

SetCondition(*condition*)[¶](#ApiClient.IfThenElse.SetCondition "Link to this definition")  
Sets the condition of the IfThenElse block.

Parameters:  **condition** (*str*) – Condition of the IfThenElse block

SetDescription(*value*)[¶](#ApiClient.IfThenElse.SetDescription "Link to this definition")  
No operation. An IfThenElse block does not have a description.

Parameters:  **value** (*str*) – The new description

SetEnabled(*enable*)[¶](#ApiClient.IfThenElse.SetEnabled "Link to this definition")  
Enables or disables the trace step (this also affects child trace steps).

Parameters:  **enable** (*boolean*) – If True, enables the trace step, if False, disables the trace step

SetName(*name*)[¶](#ApiClient.IfThenElse.SetName "Link to this definition")  
No operation. The name of an IfThenElse cannot be changed.

Parameters:  **name** (*str*) – The new name

SetTags(*tags*)[¶](#ApiClient.IfThenElse.SetTags "Link to this definition")  
Set the list of tags for this step. The list of tags will be sorted and stored.

Parameters:  **tags** (*list[str]*) – The list of tags

## ElseNode[¶](#elsenode "Link to this heading")

*class* ElseNode[¶](#ApiClient.ElseNode "Link to this definition")  
Base classes

- [`TraceStep`](#ApiClient.TraceStep "ApiClient.TraceStep")

- [`TraceStepContainer`](#ApiClient.TraceStepContainer "ApiClient.TraceStepContainer")

Returned by

- [`IfThenElse.GetElseNode`](#ApiClient.IfThenElse.GetElseNode "ApiClient.IfThenElse.GetElseNode")

AddTag(*tag*)[¶](#ApiClient.ElseNode.AddTag "Link to this definition")  
Add a specific tag to this step.

Parameters:  **tag** (*str*) – The tag to be set

AppendTraceStep(*traceStep*)[¶](#ApiClient.ElseNode.AppendTraceStep "Link to this definition")  
Adds a trace step at the end of its children.

Parameters:  **traceStep** ([`TraceStep`](#ApiClient.TraceStep "ApiClient.TraceStep")) – Trace step to be added

Clone()[¶](#ApiClient.ElseNode.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`ElseNode`](#ApiClient.ElseNode "ApiClient.ElseNode")

GetDescription()[¶](#ApiClient.ElseNode.GetDescription "Link to this definition")  
Returns the description of the trace analysis element.

Returns:  The description

Return type:  str

GetLineNo()[¶](#ApiClient.ElseNode.GetLineNo "Link to this definition")  
Returns the trace steps line number within its trace analysis.

Returns:  Line number

Return type:  int

GetName()[¶](#ApiClient.ElseNode.GetName "Link to this definition")  
Returns the name of the trace analysis element.

Returns:  The name

Return type:  str

GetTags()[¶](#ApiClient.ElseNode.GetTags "Link to this definition")  
Returns the tags set for this step.

Returns:  A (sorted) list of tags

Return type:  list[str]

GetTraceSteps(*skipDisabledSteps=False*, *recursive=False*)[¶](#ApiClient.ElseNode.GetTraceSteps "Link to this definition")  
Returns either direct or all children of the trace step.

Parameters:  - **skipDisabledSteps** (*boolean*) – Defines whether disabled trace steps should be excluded, defaults to False.

- **recursive** (*boolean*) – Defines whether children of children are included, defaults to False.

Returns:  The trace steps as flat list.

Return type:  list[[`TraceStep`](#ApiClient.TraceStep "ApiClient.TraceStep")]

GetType()[¶](#ApiClient.ElseNode.GetType "Link to this definition")  
Returns the type (class name) of the trace step, e.g.

> - ‘Episode’
>
> - ‘AnalysisBlock’
>
> - ‘TriggerBlock’
>
> - ‘Calculation’
>
> - ‘TemplateBasedTraceStep’
>
> - ‘TraceAnalysisReference’
>
> - ‘TraceAnalysisReferenceDeprecated’

Returns:  Type (class name) of the trace step

Return type:  str

GetUuid()[¶](#ApiClient.ElseNode.GetUuid "Link to this definition")  
Returns the UUID of the trace step.

Returns:  UUID of the trace step

Return type:  str

InsertTraceStep(*traceStep*, *position*)[¶](#ApiClient.ElseNode.InsertTraceStep "Link to this definition")  
Adds a trace step at a certain line of the trace analysis.

Parameters:  - **traceStep** ([`TraceStep`](#ApiClient.TraceStep "ApiClient.TraceStep")) – Trace step to be added

- **position** (*integer*) – Target index of child beginning with 0

IsContainer()[¶](#ApiClient.ElseNode.IsContainer "Link to this definition")  
Checks whether this trace step can contain trace steps.

Returns:  True if it can contain trace steps, else False

Return type:  boolean

IsEnabled()[¶](#ApiClient.ElseNode.IsEnabled "Link to this definition")  
Checks whether the trace step is enabled.

Returns:  True if trace step is enabled, else False

Return type:  boolean

IsOk()[¶](#ApiClient.ElseNode.IsOk "Link to this definition")  
Returns the internal state of correctness of the trace step.

Returns:  True if no problems were found, else False

Return type:  boolean

IsVisible()[¶](#ApiClient.ElseNode.IsVisible "Link to this definition")  
Checks whether the trace step is visible. This depends on the trace step itself or a parent trace step being disabled.

Returns:  True if trace step is visible, else False

Return type:  boolean

RemoveTag(*tag*)[¶](#ApiClient.ElseNode.RemoveTag "Link to this definition")  
Remove a specific tag from this step.

Parameters:  **tag** (*str*) – The tag to be removed

RemoveTraceStep(*traceStep*)[¶](#ApiClient.ElseNode.RemoveTraceStep "Link to this definition")  
Removes the given trace step from the trace analysis.

Parameters:  **traceStep** ([`TraceStep`](#ApiClient.TraceStep "ApiClient.TraceStep")) – Trace step to be removed

SetDescription(*value*)[¶](#ApiClient.ElseNode.SetDescription "Link to this definition")  
No operation. An “else” node does not have a description.

Parameters:  **value** (*str*) – The new description

SetEnabled(*enable*)[¶](#ApiClient.ElseNode.SetEnabled "Link to this definition")  
No operation. An “else” node is automatically enabled or disabled by the condition of its parent and cannot be enabled or disabled by the user.

Parameters:  **enable** (*boolean*) – If True, enables the trace step, if False, disables the trace step

SetName(*name*)[¶](#ApiClient.ElseNode.SetName "Link to this definition")  
No operation. The name of an “else” node cannot be changed.

Parameters:  **name** (*str*) – The new name

SetTags(*tags*)[¶](#ApiClient.ElseNode.SetTags "Link to this definition")  
Set the list of tags for this step. The list of tags will be sorted and stored.

Parameters:  **tags** (*list[str]*) – The list of tags

## ThenNode[¶](#thennode "Link to this heading")

*class* ThenNode[¶](#ApiClient.ThenNode "Link to this definition")  
Base classes

- [`TraceStep`](#ApiClient.TraceStep "ApiClient.TraceStep")

- [`TraceStepContainer`](#ApiClient.TraceStepContainer "ApiClient.TraceStepContainer")

Returned by

- [`IfThenElse.GetThenNode`](#ApiClient.IfThenElse.GetThenNode "ApiClient.IfThenElse.GetThenNode")

AddTag(*tag*)[¶](#ApiClient.ThenNode.AddTag "Link to this definition")  
Add a specific tag to this step.

Parameters:  **tag** (*str*) – The tag to be set

AppendTraceStep(*traceStep*)[¶](#ApiClient.ThenNode.AppendTraceStep "Link to this definition")  
Adds a trace step at the end of its children.

Parameters:  **traceStep** ([`TraceStep`](#ApiClient.TraceStep "ApiClient.TraceStep")) – Trace step to be added

Clone()[¶](#ApiClient.ThenNode.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`ThenNode`](#ApiClient.ThenNode "ApiClient.ThenNode")

GetDescription()[¶](#ApiClient.ThenNode.GetDescription "Link to this definition")  
Returns the description of the trace analysis element.

Returns:  The description

Return type:  str

GetLineNo()[¶](#ApiClient.ThenNode.GetLineNo "Link to this definition")  
Returns the trace steps line number within its trace analysis.

Returns:  Line number

Return type:  int

GetName()[¶](#ApiClient.ThenNode.GetName "Link to this definition")  
Returns the name of the trace analysis element.

Returns:  The name

Return type:  str

GetTags()[¶](#ApiClient.ThenNode.GetTags "Link to this definition")  
Returns the tags set for this step.

Returns:  A (sorted) list of tags

Return type:  list[str]

GetTraceSteps(*skipDisabledSteps=False*, *recursive=False*)[¶](#ApiClient.ThenNode.GetTraceSteps "Link to this definition")  
Returns either direct or all children of the trace step.

Parameters:  - **skipDisabledSteps** (*boolean*) – Defines whether disabled trace steps should be excluded, defaults to False.

- **recursive** (*boolean*) – Defines whether children of children are included, defaults to False.

Returns:  The trace steps as flat list.

Return type:  list[[`TraceStep`](#ApiClient.TraceStep "ApiClient.TraceStep")]

GetType()[¶](#ApiClient.ThenNode.GetType "Link to this definition")  
Returns the type (class name) of the trace step, e.g.

> - ‘Episode’
>
> - ‘AnalysisBlock’
>
> - ‘TriggerBlock’
>
> - ‘Calculation’
>
> - ‘TemplateBasedTraceStep’
>
> - ‘TraceAnalysisReference’
>
> - ‘TraceAnalysisReferenceDeprecated’

Returns:  Type (class name) of the trace step

Return type:  str

GetUuid()[¶](#ApiClient.ThenNode.GetUuid "Link to this definition")  
Returns the UUID of the trace step.

Returns:  UUID of the trace step

Return type:  str

InsertTraceStep(*traceStep*, *position*)[¶](#ApiClient.ThenNode.InsertTraceStep "Link to this definition")  
Adds a trace step at a certain line of the trace analysis.

Parameters:  - **traceStep** ([`TraceStep`](#ApiClient.TraceStep "ApiClient.TraceStep")) – Trace step to be added

- **position** (*integer*) – Target index of child beginning with 0

IsContainer()[¶](#ApiClient.ThenNode.IsContainer "Link to this definition")  
Checks whether this trace step can contain trace steps.

Returns:  True if it can contain trace steps, else False

Return type:  boolean

IsEnabled()[¶](#ApiClient.ThenNode.IsEnabled "Link to this definition")  
Checks whether the trace step is enabled.

Returns:  True if trace step is enabled, else False

Return type:  boolean

IsOk()[¶](#ApiClient.ThenNode.IsOk "Link to this definition")  
Returns the internal state of correctness of the trace step.

Returns:  True if no problems were found, else False

Return type:  boolean

IsVisible()[¶](#ApiClient.ThenNode.IsVisible "Link to this definition")  
Checks whether the trace step is visible. This depends on the trace step itself or a parent trace step being disabled.

Returns:  True if trace step is visible, else False

Return type:  boolean

RemoveTag(*tag*)[¶](#ApiClient.ThenNode.RemoveTag "Link to this definition")  
Remove a specific tag from this step.

Parameters:  **tag** (*str*) – The tag to be removed

RemoveTraceStep(*traceStep*)[¶](#ApiClient.ThenNode.RemoveTraceStep "Link to this definition")  
Removes the given trace step from the trace analysis.

Parameters:  **traceStep** ([`TraceStep`](#ApiClient.TraceStep "ApiClient.TraceStep")) – Trace step to be removed

SetDescription(*value*)[¶](#ApiClient.ThenNode.SetDescription "Link to this definition")  
No operation. A “then” node does not have a description.

Parameters:  **value** (*str*) – The new description

SetEnabled(*enable*)[¶](#ApiClient.ThenNode.SetEnabled "Link to this definition")  
No operation. A “then” node is automatically enabled or disabled by the condition of its parent and cannot be enabled or disabled by the user.

Parameters:  **enable** (*boolean*) – If True, enables the trace step, if False, disables the trace step

SetName(*name*)[¶](#ApiClient.ThenNode.SetName "Link to this definition")  
No operation. The name of a “then” node cannot be changed.

Parameters:  **name** (*str*) – The new name

SetTags(*tags*)[¶](#ApiClient.ThenNode.SetTags "Link to this definition")  
Set the list of tags for this step. The list of tags will be sorted and stored.

Parameters:  **tags** (*list[str]*) – The list of tags

## TraceAnalysis[¶](#traceanalysis "Link to this heading")

*class* TraceAnalysis[¶](#ApiClient.TraceAnalysis "Link to this definition")  
Base classes

- [`TraceStep`](#ApiClient.TraceStep "ApiClient.TraceStep")

- [`TraceStepContainer`](#ApiClient.TraceStepContainer "ApiClient.TraceStepContainer")

Returned by

- [`AnalysisPackage.GetTraceAnalysis`](PackageApi.md#ApiClient.AnalysisPackage.GetTraceAnalysis "ApiClient.AnalysisPackage.GetTraceAnalysis")

- [`Package.GetTraceAnalyses`](PackageApi.md#ApiClient.Package.GetTraceAnalyses "ApiClient.Package.GetTraceAnalyses")

- [`TraceAnalysisApi.CreateTraceAnalysis`](#ApiClient.TraceAnalysisApi.CreateTraceAnalysis "ApiClient.TraceAnalysisApi.CreateTraceAnalysis")

AddTag(*tag*)[¶](#ApiClient.TraceAnalysis.AddTag "Link to this definition")  
Add a specific tag to this step.

Parameters:  **tag** (*str*) – The tag to be set

AppendGenericSignal(*genericSignal*)[¶](#ApiClient.TraceAnalysis.AppendGenericSignal "Link to this definition")  
Adds a generic signal to the trace analysis. The name must be python-conform!

Parameters:  **genericSignal** ([`GenericSignal`](#ApiClient.GenericSignal "ApiClient.GenericSignal")) – The generic signal to be appended

AppendTraceStep(*traceStep*)[¶](#ApiClient.TraceAnalysis.AppendTraceStep "Link to this definition")  
Adds a trace step at the end of its children.

Parameters:  **traceStep** ([`TraceStep`](#ApiClient.TraceStep "ApiClient.TraceStep")) – Trace step to be added

Clone()[¶](#ApiClient.TraceAnalysis.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`TraceAnalysis`](#ApiClient.TraceAnalysis "ApiClient.TraceAnalysis")

ExportToAnalysisPackage(*filename*)[¶](#ApiClient.TraceAnalysis.ExportToAnalysisPackage "Link to this definition")  
Exports this trace analysis to an analysis package. The analysis package will not take over any synchronization configuration and all signal bindings will be adjusted to rely on generic mappings.

Parameters:  **filename** (*str*) – Filename of the analysis package to be saved

GetConditionalGenericSignals()[¶](#ApiClient.TraceAnalysis.GetConditionalGenericSignals "Link to this definition")  
Returns the list of signals that can be optional or mandatory for running the trace analysis depending on the values of global constants.

Returns:  The list of undetermined signals.

Return type:  list[[`GenericSignal`](#ApiClient.GenericSignal "ApiClient.GenericSignal")]

GetDescription()[¶](#ApiClient.TraceAnalysis.GetDescription "Link to this definition")  
Returns the description of the trace analysis element.

Returns:  The description

Return type:  str

GetGenericSignal(*name*)[¶](#ApiClient.TraceAnalysis.GetGenericSignal "Link to this definition")  
Returns the generic signal of given name.

Parameters:  **name** (*str*) – The name of the generic signal

Returns:  A generic signal

Return type:  [`GenericSignal`](#ApiClient.GenericSignal "ApiClient.GenericSignal")

GetGenericSignals()[¶](#ApiClient.TraceAnalysis.GetGenericSignals "Link to this definition")  
Returns all generic signal.

Returns:  The list of generic signals

Return type:  list[[`GenericSignal`](#ApiClient.GenericSignal "ApiClient.GenericSignal")]

GetMandatoryGenericSignals()[¶](#ApiClient.TraceAnalysis.GetMandatoryGenericSignals "Link to this definition")  
Returns the list of signals that are mandatory for running the trace analysis.

Returns:  The list of mandatory signals.

Return type:  list[[`GenericSignal`](#ApiClient.GenericSignal "ApiClient.GenericSignal")]

GetName()[¶](#ApiClient.TraceAnalysis.GetName "Link to this definition")  
Returns the name of the trace analysis element.

Returns:  The name

Return type:  str

GetOptionalGenericSignals()[¶](#ApiClient.TraceAnalysis.GetOptionalGenericSignals "Link to this definition")  
Returns the list of signals that are optional for running the trace analysis.

Returns:  The list of optional signals.

Return type:  list[[`GenericSignal`](#ApiClient.GenericSignal "ApiClient.GenericSignal")]

GetReferencedTraceStepTemplates()[¶](#ApiClient.TraceAnalysis.GetReferencedTraceStepTemplates "Link to this definition")  
Returns a list with all referenced trace step templates.

Returns:  A list of the referenced trace step templates

Return type:  list[str]

GetTags()[¶](#ApiClient.TraceAnalysis.GetTags "Link to this definition")  
Returns the tags set for this step.

Returns:  A (sorted) list of tags

Return type:  list[str]

GetTraceSteps(*skipDisabledSteps=False*, *recursive=False*)[¶](#ApiClient.TraceAnalysis.GetTraceSteps "Link to this definition")  
Returns either direct or all children of the trace step.

Parameters:  - **skipDisabledSteps** (*boolean*) – Defines whether disabled trace steps should be excluded, defaults to False.

- **recursive** (*boolean*) – Defines whether children of children are included, defaults to False.

Returns:  The trace steps as flat list.

Return type:  list[[`TraceStep`](#ApiClient.TraceStep "ApiClient.TraceStep")]

GetType()[¶](#ApiClient.TraceAnalysis.GetType "Link to this definition")  
Returns the type (class name) of the trace step, e.g.

> - ‘Episode’
>
> - ‘AnalysisBlock’
>
> - ‘TriggerBlock’
>
> - ‘Calculation’
>
> - ‘TemplateBasedTraceStep’
>
> - ‘TraceAnalysisReference’
>
> - ‘TraceAnalysisReferenceDeprecated’

Returns:  Type (class name) of the trace step

Return type:  str

GetUuid()[¶](#ApiClient.TraceAnalysis.GetUuid "Link to this definition")  
Returns the UUID of the trace step.

Returns:  UUID of the trace step

Return type:  str

InsertTraceStep(*traceStep*, *position*)[¶](#ApiClient.TraceAnalysis.InsertTraceStep "Link to this definition")  
Adds a trace step at a certain line of the trace analysis.

Parameters:  - **traceStep** ([`TraceStep`](#ApiClient.TraceStep "ApiClient.TraceStep")) – Trace step to be added

- **position** (*integer*) – Target index of child beginning with 0

IsContainer()[¶](#ApiClient.TraceAnalysis.IsContainer "Link to this definition")  
Checks whether this trace step can contain trace steps.

Returns:  True if it can contain trace steps, else False

Return type:  boolean

IsEnabled()[¶](#ApiClient.TraceAnalysis.IsEnabled "Link to this definition")  
Checks whether the trace step is enabled.

Returns:  True if trace step is enabled, else False

Return type:  boolean

IsOk()[¶](#ApiClient.TraceAnalysis.IsOk "Link to this definition")  
Returns the internal state of correctness of the trace step.

Returns:  True if no problems were found, else False

Return type:  boolean

RemoveGenericSignal(*name*)[¶](#ApiClient.TraceAnalysis.RemoveGenericSignal "Link to this definition")  
Removes a generic signal from the trace analysis.

Parameters:  **name** (*str*) – The name of the generic signal

RemoveTag(*tag*)[¶](#ApiClient.TraceAnalysis.RemoveTag "Link to this definition")  
Remove a specific tag from this step.

Parameters:  **tag** (*str*) – The tag to be removed

RemoveTraceStep(*traceStep*)[¶](#ApiClient.TraceAnalysis.RemoveTraceStep "Link to this definition")  
Removes the given trace step from the trace analysis.

Parameters:  **traceStep** ([`TraceStep`](#ApiClient.TraceStep "ApiClient.TraceStep")) – Trace step to be removed

SetDescription(*value*)[¶](#ApiClient.TraceAnalysis.SetDescription "Link to this definition")  
Sets the description of the trace analysis element.

Parameters:  **value** (*str*) – The new description

SetEnabled(*enable*)[¶](#ApiClient.TraceAnalysis.SetEnabled "Link to this definition")  
Enables or disables the trace step (this also affects child trace steps).

Parameters:  **enable** (*boolean*) – If True, enables the trace step, if False, disables the trace step

SetName(*value*)[¶](#ApiClient.TraceAnalysis.SetName "Link to this definition")  
Sets the name of the trace analysis element.

Parameters:  **value** (*str*) – The new name

SetTags(*tags*)[¶](#ApiClient.TraceAnalysis.SetTags "Link to this definition")  
Set the list of tags for this step. The list of tags will be sorted and stored.

Parameters:  **tags** (*list[str]*) – The list of tags

## SyncConfig[¶](#syncconfig "Link to this heading")

*class* SyncConfig[¶](#ApiClient.SyncConfig "Link to this definition")  
Returned by

- [`RecordingConfig.GetSyncConfig`](PackageApi.md#ApiClient.RecordingConfig.GetSyncConfig "ApiClient.RecordingConfig.GetSyncConfig")

AssignAutosarTimeSynchronization(*recordingGroup*, *masterGroup*)[¶](#ApiClient.SyncConfig.AssignAutosarTimeSynchronization "Link to this definition")  
Assigns an AUTOSAR Time Synchronization that synchronizes recordingGroup with masterGroup. If there is already a synchronization assigned to recordingGroup it will be unassigned.

Parameters:  - **recordingGroup** ([`RecordingGroup`](SignalRecordingApi.md#ApiClient.RecordingGroup "ApiClient.RecordingGroup")) – The recording group the synchronization is assigned to

- **masterGroup** ([`RecordingGroup`](SignalRecordingApi.md#ApiClient.RecordingGroup "ApiClient.RecordingGroup")) – The recording group that is used as master for this synchronization

Returns:  Returns the newly created AUTOSAR Time Synchronization

Return type:  [`AutosarTimeSynchronization`](#ApiClient.AutosarTimeSynchronization "ApiClient.AutosarTimeSynchronization")

AssignCrossCorrelationSynchronization(*recordingGroup*, *masterGroup*)[¶](#ApiClient.SyncConfig.AssignCrossCorrelationSynchronization "Link to this definition")  
Assigns a cross correlation synchronization that synchronizes recordingGroup with masterGroup. If there is already a synchronization assigned to recordingGroup it will be unassigned.

Parameters:  - **recordingGroup** ([`RecordingGroup`](SignalRecordingApi.md#ApiClient.RecordingGroup "ApiClient.RecordingGroup")) – The recording group the synchronization is assigned to

- **masterGroup** ([`RecordingGroup`](SignalRecordingApi.md#ApiClient.RecordingGroup "ApiClient.RecordingGroup")) – The recording group that is used as master for this synchronization

Returns:  Returns the newly created cross correlation synchronization

Return type:  [`CrossCorrelationSynchronization`](#ApiClient.CrossCorrelationSynchronization "ApiClient.CrossCorrelationSynchronization")

AssignEqualnessMatchingSynchronization(*recordingGroup*, *masterGroup*)[¶](#ApiClient.SyncConfig.AssignEqualnessMatchingSynchronization "Link to this definition")  
Assigns an equalness matching synchronization that synchronizes recordingGroup with masterGroup. If there is already a synchronization assigned to recordingGroup it will be unassigned.

Parameters:  - **recordingGroup** ([`RecordingGroup`](SignalRecordingApi.md#ApiClient.RecordingGroup "ApiClient.RecordingGroup")) – The recording group the synchronization is assigned to

- **masterGroup** ([`RecordingGroup`](SignalRecordingApi.md#ApiClient.RecordingGroup "ApiClient.RecordingGroup")) – The recording group that is used as master for this synchronization

Returns:  Returns the newly created equalness matching synchronization

Return type:  [`EqualnessMatchingSynchronization`](#ApiClient.EqualnessMatchingSynchronization "ApiClient.EqualnessMatchingSynchronization")

AssignExpectationSynchronization(*recordingGroup*, *masterGroup*)[¶](#ApiClient.SyncConfig.AssignExpectationSynchronization "Link to this definition")  
Assigns an expectation synchronization that synchronizes recordingGroup with masterGroup. If there is already a synchronization assigned to recordingGroup it will be unassigned.

Parameters:  - **recordingGroup** ([`RecordingGroup`](SignalRecordingApi.md#ApiClient.RecordingGroup "ApiClient.RecordingGroup")) – The recording group the synchronization is assigned to

- **masterGroup** ([`RecordingGroup`](SignalRecordingApi.md#ApiClient.RecordingGroup "ApiClient.RecordingGroup")) – The recording group that is used as master for this synchronization

Returns:  Returns the newly created expectation synchronization

Return type:  [`ExpectationSynchronization`](#ApiClient.ExpectationSynchronization "ApiClient.ExpectationSynchronization")

AssignLeastSquaresSynchronization(*recordingGroup*, *masterGroup*)[¶](#ApiClient.SyncConfig.AssignLeastSquaresSynchronization "Link to this definition")  
Assigns a least squares synchronization that synchronizes recordingGroup with masterGroup. If there is already a synchronization assigned to recordingGroup it will be unassigned.

Parameters:  - **recordingGroup** ([`RecordingGroup`](SignalRecordingApi.md#ApiClient.RecordingGroup "ApiClient.RecordingGroup")) – The recording group the synchronization is assigned to

- **masterGroup** ([`RecordingGroup`](SignalRecordingApi.md#ApiClient.RecordingGroup "ApiClient.RecordingGroup")) – The recording group that is used as master for this synchronization

Returns:  Returns the newly created least squares synchronization

Return type:  [`LeastSquaresSynchronization`](#ApiClient.LeastSquaresSynchronization "ApiClient.LeastSquaresSynchronization")

AssignOffsetSynchronization(*recordingGroup*, *masterGroup*)[¶](#ApiClient.SyncConfig.AssignOffsetSynchronization "Link to this definition")  
Assigns an offset synchronization that synchronizes recordingGroup with masterGroup. If there is already a synchronization assigned to recordingGroup it will be unassigned.

Parameters:  - **recordingGroup** ([`RecordingGroup`](SignalRecordingApi.md#ApiClient.RecordingGroup "ApiClient.RecordingGroup")) – The recording group the synchronization is assigned to

- **masterGroup** ([`RecordingGroup`](SignalRecordingApi.md#ApiClient.RecordingGroup "ApiClient.RecordingGroup")) – The recording group that is used as master for this synchronization

Returns:  Returns the newly created offset synchronization

Return type:  [`OffsetSynchronization`](#ApiClient.OffsetSynchronization "ApiClient.OffsetSynchronization")

AssignUtcTimestampSynchronization(*recordingGroup*, *masterGroup*)[¶](#ApiClient.SyncConfig.AssignUtcTimestampSynchronization "Link to this definition")  
Assigns a cross correlation synchronization that synchronizes recordingGroup with masterGroup. If there is already a synchronization assigned to recordingGroup it will be unassigned.

Parameters:  - **recordingGroup** ([`RecordingGroup`](SignalRecordingApi.md#ApiClient.RecordingGroup "ApiClient.RecordingGroup")) – The recording group the synchronization is assigned to

- **masterGroup** ([`RecordingGroup`](SignalRecordingApi.md#ApiClient.RecordingGroup "ApiClient.RecordingGroup")) – The recording group that is used as master for this synchronization

Returns:  Returns the newly created UtcTimestamp synchronization

Return type:  [`UtcTimestampSynchronization`](#ApiClient.UtcTimestampSynchronization "ApiClient.UtcTimestampSynchronization")

Clone()[¶](#ApiClient.SyncConfig.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`SyncConfig`](#ApiClient.SyncConfig "ApiClient.SyncConfig")

GetAdjustTimeInTraceCopy()[¶](#ApiClient.SyncConfig.GetAdjustTimeInTraceCopy "Link to this definition")  
Returns whether the trace files are copied to the report directory with time axes adjusted according to sync delta T determined by synchronization.

Returns:  True if the synchronized copies of the trace files are generated, else False

Return type:  boolean

GetContinueOnError()[¶](#ApiClient.SyncConfig.GetContinueOnError "Link to this definition")  
Returns whether the trace merge and trace analysis should continue after an error occurred during the synchronization.

Returns:  True to continue after a synchronization error, else False

Return type:  bool

GetMaster()[¶](#ApiClient.SyncConfig.GetMaster "Link to this definition")  
Returns the master recording group.

Returns:  The master recording group

Return type:  [`RecordingGroup`](SignalRecordingApi.md#ApiClient.RecordingGroup "ApiClient.RecordingGroup")

GetMasterName()[¶](#ApiClient.SyncConfig.GetMasterName "Link to this definition")  
Returns the name of the master recording group.

Returns:  The name of the master recording group

Return type:  str

GetSynchronization(*recordingGroup*)[¶](#ApiClient.SyncConfig.GetSynchronization "Link to this definition")  
Returns the assigned synchronization for the given recording group.

Parameters:  **recordingGroup** ([`RecordingGroup`](SignalRecordingApi.md#ApiClient.RecordingGroup "ApiClient.RecordingGroup")) – The recording group

Returns:  The assigned synchronization. Returns None if no synchronization is set.

Return type:  [`Synchronization`](#ApiClient.Synchronization "ApiClient.Synchronization")

GetSynchronizations()[¶](#ApiClient.SyncConfig.GetSynchronizations "Link to this definition")  
Returns the list synchronizations.

Returns:  The list of synchronizations

Return type:  list[[`Synchronization`](#ApiClient.Synchronization "ApiClient.Synchronization")]

GetUseEndOfTestSnapshot()[¶](#ApiClient.SyncConfig.GetUseEndOfTestSnapshot "Link to this definition")  
Returns whether the variable and global constant values at the end of the testcase will be used when evaluating the synchronization.

This setting defaults to False. So for each synchronization the values depend on the point of time at which the last recording of a group of recordings to synchronize is collected/created. This behavior is mostly important when using Start/StopTrace or AddTrace and the testcase.

Returns:  True, to use only the variable and global constant values at the end of the testcase, else False

Return type:  boolean

IsActive()[¶](#ApiClient.SyncConfig.IsActive "Link to this definition")  
Returns whether the synchronization is active. By default, for a newly created trace analysis the synchronization is not active.

Returns:  True if the synchronization is active, else False

Return type:  boolean

SetActive(*active=True*)[¶](#ApiClient.SyncConfig.SetActive "Link to this definition")  
Activates or deactivates the synchronization.

Parameters:  **active** (*boolean*) – True will activate and False will deactivate the synchronization

SetAdjustTimeInTraceCopy(*value*)[¶](#ApiClient.SyncConfig.SetAdjustTimeInTraceCopy "Link to this definition")  
Sets whether the trace files should be copied to the report directory with time axes adjusted according to sync delta T determined by synchronization.

Parameters:  **value** (*boolean*) – True if the synchronized copies of the trace files are generated, else False

SetContinueOnError(*value*)[¶](#ApiClient.SyncConfig.SetContinueOnError "Link to this definition")  
Sets whether the trace merge and trace analysis should continue after an error occurred during the synchronization. If so, all traces will be used unsynchronized.

Parameters:  **value** (*bool*) – True to continue after a synchronization error, else False

SetMaster(*recordingGroup*)[¶](#ApiClient.SyncConfig.SetMaster "Link to this definition")  
Sets the master recording group. If there is a synchronization assigned to the recording group it will be deleted.

Parameters:  **recordingGroup** ([`RecordingGroup`](SignalRecordingApi.md#ApiClient.RecordingGroup "ApiClient.RecordingGroup")) – The master recording group

SetUseEndOfTestSnapshot(*value*)[¶](#ApiClient.SyncConfig.SetUseEndOfTestSnapshot "Link to this definition")  
Sets whether the variable and global constant values at the end of the testcase will be used when evaluating the synchronization.

This setting defaults to False. So for each synchronization the values depend on the point of time at which the last recording of a group of recordings to synchronize is collected/created. This behavior is mostly important when using Start/StopTrace or AddTrace and the testcase.

Parameters:  **value** (*boolean*) – True, to use only the variable and global constant values at the end of the testcase, else False

## AutosarTimeSynchronization[¶](#autosartimesynchronization "Link to this heading")

*class* AutosarTimeSynchronization[¶](#ApiClient.AutosarTimeSynchronization "Link to this definition")  
Base class

[`Synchronization`](#ApiClient.Synchronization "ApiClient.Synchronization")

Returned by

- [`SyncConfig.AssignAutosarTimeSynchronization`](#ApiClient.SyncConfig.AssignAutosarTimeSynchronization "ApiClient.SyncConfig.AssignAutosarTimeSynchronization")

Clone()[¶](#ApiClient.AutosarTimeSynchronization.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`AutosarTimeSynchronization`](#ApiClient.AutosarTimeSynchronization "ApiClient.AutosarTimeSynchronization")

GetMaster()[¶](#ApiClient.AutosarTimeSynchronization.GetMaster "Link to this definition")  
Returns the master recording group for this synchronization.

Returns:  The master recording group

Return type:  [`RecordingGroup`](SignalRecordingApi.md#ApiClient.RecordingGroup "ApiClient.RecordingGroup")

GetMasterGroupInfo()[¶](#ApiClient.AutosarTimeSynchronization.GetMasterGroupInfo "Link to this definition")  
Returns the master recording group info.

Returns:  The master recording group info.

Return type:  [`AutosarTimeSyncRecordingGroupInfo`](#ApiClient.AutosarTimeSyncRecordingGroupInfo "ApiClient.AutosarTimeSyncRecordingGroupInfo")

GetMaxDeltaT()[¶](#ApiClient.AutosarTimeSynchronization.GetMaxDeltaT "Link to this definition")  
Returns the bound for deltaT. If deltaT is found to be greater than this bound, the synchronization will fail.

Returns:  The maximum for deltaT as expression

Return type:  str

GetOffset()[¶](#ApiClient.AutosarTimeSynchronization.GetOffset "Link to this definition")  
Returns the (known) offset. The offset will be added to the calculated deltaT. By default, it is only used for the OffsetSynchronization.

Returns:  The (known) offset as expression

Return type:  str

GetOffsetUsed()[¶](#ApiClient.AutosarTimeSynchronization.GetOffsetUsed "Link to this definition")  
Sets whether the known offset should be applied. For the ExpectationSynchronization and EqualnessMatchingSynchronization the known offset will be added to the calculated deltaT. The known offset will always be used by the OffsetSynchronization.

Returns:  True if the offset will be used, else False.

Return type:  boolean

GetRecordingGroupInfo()[¶](#ApiClient.AutosarTimeSynchronization.GetRecordingGroupInfo "Link to this definition")  
Returns the recording group info.

Returns:  The recording group info.

Return type:  [`AutosarTimeSyncRecordingGroupInfo`](#ApiClient.AutosarTimeSyncRecordingGroupInfo "ApiClient.AutosarTimeSyncRecordingGroupInfo")

GetRecordingGroupName()[¶](#ApiClient.AutosarTimeSynchronization.GetRecordingGroupName "Link to this definition")  
Returns the name of the recording group for this synchronization.

Returns:  The name of the recording group

Return type:  str

GetTimeLimit()[¶](#ApiClient.AutosarTimeSynchronization.GetTimeLimit "Link to this definition")  
Returns the time stamp relative to the first time stamp (of the recording group and master recording group) until that the running synchronization will be evaluated. If the time limit is reached, the synchronization will fail.

Returns:  The relative time limit as expression

Return type:  str

GetType()[¶](#ApiClient.AutosarTimeSynchronization.GetType "Link to this definition")  
Returns the type of this synchronization.

Returns:  The type of this synchronization (can be ‘Offset’, ‘Expectation’, ‘EqualnessMatching’ or ‘LeastSquares’, ‘AutosarTime’)

Return type:  str

IsFirstSampleDifferenceCorrected()[¶](#ApiClient.AutosarTimeSynchronization.IsFirstSampleDifferenceCorrected "Link to this definition")  
Returns whether the parameter maxDeltaT is corrected by the difference of the time stamps of the first samples (of the recording group and master recording group). Suppose that the time axes to be synchronized start at 20s and 50s, respectively. Then activating this option acts as if maxDeltaT was increased by 30s.

Returns:  The setting for the interpretation of maxDeltaT

Return type:  boolean

SetFirstSampleDifferenceCorrected(*isCorrected*)[¶](#ApiClient.AutosarTimeSynchronization.SetFirstSampleDifferenceCorrected "Link to this definition")  
Not available. maxDeltaT is not used by the AUTOSAR Time Synchronization.

Parameters:  **isCorrected** (*boolean*) – The setting for the interpretation of maxDeltaT

SetMaster(*recordingGroup*)[¶](#ApiClient.AutosarTimeSynchronization.SetMaster "Link to this definition")  
Sets the master recording group for the synchronization.

Parameters:  **recordingGroup** ([`RecordingGroup`](SignalRecordingApi.md#ApiClient.RecordingGroup "ApiClient.RecordingGroup")) – The master recording group.

SetMaxDeltaT(*maxDeltaT*)[¶](#ApiClient.AutosarTimeSynchronization.SetMaxDeltaT "Link to this definition")  
Not available. maxDeltaT is not used by the AUTOSAR Time Synchronization.

Parameters:  **maxDeltaT** (*str*) – The maximum for deltaT as expression

SetOffset(*offset*)[¶](#ApiClient.AutosarTimeSynchronization.SetOffset "Link to this definition")  
Sets (known) offset. The offset will be added to the calculated deltaT. By default, it is only used for the OffsetSynchronization.

Parameters:  **offset** (*str*) – The (known) offset as expression

SetOffsetUsed(*used*)[¶](#ApiClient.AutosarTimeSynchronization.SetOffsetUsed "Link to this definition")  
Sets whether the known offset should be applied. For the ExpectationSynchronization and EqualnessMatchingSynchronization the known offset will be added to the calculated deltaT. The known offset will always be used by the OffsetSynchronization.

Parameters:  **used** (*boolean*) – True if the offset should be used, else False.

SetTimeLimit(*timeLimit*)[¶](#ApiClient.AutosarTimeSynchronization.SetTimeLimit "Link to this definition")  
Not available. TimeLimit is not used by the AUTOSAR Time Synchronization.

Parameters:  **timeLimit** (*str*) – The relative time limit as expression

## AutosarTimeSyncRecordingGroupInfo[¶](#autosartimesyncrecordinggroupinfo "Link to this heading")

*class* AutosarTimeSyncRecordingGroupInfo[¶](#ApiClient.AutosarTimeSyncRecordingGroupInfo "Link to this definition")  
Returned by

- [`AutosarTimeSynchronization.GetMasterGroupInfo`](#ApiClient.AutosarTimeSynchronization.GetMasterGroupInfo "ApiClient.AutosarTimeSynchronization.GetMasterGroupInfo")

- [`AutosarTimeSynchronization.GetRecordingGroupInfo`](#ApiClient.AutosarTimeSynchronization.GetRecordingGroupInfo "ApiClient.AutosarTimeSynchronization.GetRecordingGroupInfo")

BUS_TYPE_CAN_FLEXRAY[¶](#ApiClient.AutosarTimeSyncRecordingGroupInfo.BUS_TYPE_CAN_FLEXRAY "Link to this definition")  
Returns the constant used to specify the bus type “CAN/FlexRay”

Returns:  The constant

Return type:  str

BUS_TYPE_ETHERNET[¶](#ApiClient.AutosarTimeSyncRecordingGroupInfo.BUS_TYPE_ETHERNET "Link to this definition")  
Returns the constant used to specify the bus type “Ethernet (PTP)”

Returns:  The constant

Return type:  str

Clone()[¶](#ApiClient.AutosarTimeSyncRecordingGroupInfo.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`AutosarTimeSyncRecordingGroupInfo`](#ApiClient.AutosarTimeSyncRecordingGroupInfo "ApiClient.AutosarTimeSyncRecordingGroupInfo")

GetBusType()[¶](#ApiClient.AutosarTimeSyncRecordingGroupInfo.GetBusType "Link to this definition")  
Returns the configured bus type.

Returns:  One of [`AutosarTimeSyncRecordingGroupInfo.BUS_TYPE_ETHERNET`](#ApiClient.AutosarTimeSyncRecordingGroupInfo.BUS_TYPE_ETHERNET "ApiClient.AutosarTimeSyncRecordingGroupInfo.BUS_TYPE_ETHERNET"), [`AutosarTimeSyncRecordingGroupInfo.BUS_TYPE_CAN_FLEXRAY`](#ApiClient.AutosarTimeSyncRecordingGroupInfo.BUS_TYPE_CAN_FLEXRAY "ApiClient.AutosarTimeSyncRecordingGroupInfo.BUS_TYPE_CAN_FLEXRAY")

Return type:  str

GetNSecSignalName()[¶](#ApiClient.AutosarTimeSyncRecordingGroupInfo.GetNSecSignalName "Link to this definition")  
Returns the selected signal for the fractional seconds part in nanoseconds.

Returns:  The signal name, None if not set.

Return type:  str

GetSecSignalName()[¶](#ApiClient.AutosarTimeSyncRecordingGroupInfo.GetSecSignalName "Link to this definition")  
Returns the selected full seconds part signal.

Returns:  The signal name, None if not set.

Return type:  str

SetBusType(*busType*)[¶](#ApiClient.AutosarTimeSyncRecordingGroupInfo.SetBusType "Link to this definition")  
Set the bus type. If the bus type is set to Ethernet, the signal names will be automatically set and locked to ‘PTP/PacketPtpFollowUp.ptpPreciseOriginTimestampSec’ and ‘PTP/PacketPtpFollowUp.ptpPreciseOriginTimestampNSec’.

Parameters:  **busType** (*str*) – One of [`AutosarTimeSyncRecordingGroupInfo.BUS_TYPE_ETHERNET`](#ApiClient.AutosarTimeSyncRecordingGroupInfo.BUS_TYPE_ETHERNET "ApiClient.AutosarTimeSyncRecordingGroupInfo.BUS_TYPE_ETHERNET"), [`AutosarTimeSyncRecordingGroupInfo.BUS_TYPE_CAN_FLEXRAY`](#ApiClient.AutosarTimeSyncRecordingGroupInfo.BUS_TYPE_CAN_FLEXRAY "ApiClient.AutosarTimeSyncRecordingGroupInfo.BUS_TYPE_CAN_FLEXRAY")

SetNSecSignalName(*name*)[¶](#ApiClient.AutosarTimeSyncRecordingGroupInfo.SetNSecSignalName "Link to this definition")  
Set the signal for seconds part in nanoseconds.

Parameters:  **name** (*str*) – The signal name

SetSecSignalName(*name*)[¶](#ApiClient.AutosarTimeSyncRecordingGroupInfo.SetSecSignalName "Link to this definition")  
Set the signal for full seconds.

Parameters:  **name** (*str*) – The signal name

## CrossCorrelationSynchronization[¶](#crosscorrelationsynchronization "Link to this heading")

*class* CrossCorrelationSynchronization[¶](#ApiClient.CrossCorrelationSynchronization "Link to this definition")  
Base class

[`Synchronization`](#ApiClient.Synchronization "ApiClient.Synchronization")

Returned by

- [`SyncConfig.AssignCrossCorrelationSynchronization`](#ApiClient.SyncConfig.AssignCrossCorrelationSynchronization "ApiClient.SyncConfig.AssignCrossCorrelationSynchronization")

Clone()[¶](#ApiClient.CrossCorrelationSynchronization.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`CrossCorrelationSynchronization`](#ApiClient.CrossCorrelationSynchronization "ApiClient.CrossCorrelationSynchronization")

EnableConsiderNegative(*enable=True*)[¶](#ApiClient.CrossCorrelationSynchronization.EnableConsiderNegative "Link to this definition")  
Enables or disables (default) the consideration of negative correlations.

Parameters:  **enable** (*bool*) – True to enable, False to disable

EnableMinCorrelation(*enable=True*)[¶](#ApiClient.CrossCorrelationSynchronization.EnableMinCorrelation "Link to this definition")  
Enables (default) or disables the check for a minimum necessary correlation coefficient between the matched signals.

Parameters:  **enable** (*bool*) – True to enable, False to disable

GetMaster()[¶](#ApiClient.CrossCorrelationSynchronization.GetMaster "Link to this definition")  
Returns the master recording group for this synchronization.

Returns:  The master recording group

Return type:  [`RecordingGroup`](SignalRecordingApi.md#ApiClient.RecordingGroup "ApiClient.RecordingGroup")

GetMasterSignal()[¶](#ApiClient.CrossCorrelationSynchronization.GetMasterSignal "Link to this definition")  
Returns the signalName and signalType of the master signal. The type will be either “PHY” (interpreted as number) or “RAW” (raw values).

Returns:  Dictionary with keys “signalName”, “signalType”

Return type:  dict[str, str]

GetMaxDeltaT()[¶](#ApiClient.CrossCorrelationSynchronization.GetMaxDeltaT "Link to this definition")  
Returns the bound for deltaT. If deltaT is found to be greater than this bound, the synchronization will fail.

Returns:  The maximum for deltaT as expression

Return type:  str

GetMinCorrelation()[¶](#ApiClient.CrossCorrelationSynchronization.GetMinCorrelation "Link to this definition")  
Returns the minimum necessary correlation coefficient for the synchronization.

Returns:  Minimum necessary correlation coefficient

Return type:  str

GetOffset()[¶](#ApiClient.CrossCorrelationSynchronization.GetOffset "Link to this definition")  
Returns the (known) offset. The offset will be added to the calculated deltaT. By default, it is only used for the OffsetSynchronization.

Returns:  The (known) offset as expression

Return type:  str

GetOffsetUsed()[¶](#ApiClient.CrossCorrelationSynchronization.GetOffsetUsed "Link to this definition")  
Sets whether the known offset should be applied. For the ExpectationSynchronization and EqualnessMatchingSynchronization the known offset will be added to the calculated deltaT. The known offset will always be used by the OffsetSynchronization.

Returns:  True if the offset will be used, else False.

Return type:  boolean

GetRecordingGroupName()[¶](#ApiClient.CrossCorrelationSynchronization.GetRecordingGroupName "Link to this definition")  
Returns the name of the recording group for this synchronization.

Returns:  The name of the recording group

Return type:  str

GetRecordingSignal()[¶](#ApiClient.CrossCorrelationSynchronization.GetRecordingSignal "Link to this definition")  
Returns the signalName and signalType of the recording signal for synchronization. The type will be either “PHY” (interpreted as number) or “RAW” (raw values).

Returns:  Dictionary with keys “signalName”, “signalType”

Return type:  dict[str, str]

GetResolution()[¶](#ApiClient.CrossCorrelationSynchronization.GetResolution "Link to this definition")  
Returns the resolution (step size) at which the synchronization offset is determined.

Returns:  Resolution (step size) for the synchronization as expression

Return type:  str

GetTimeLimit()[¶](#ApiClient.CrossCorrelationSynchronization.GetTimeLimit "Link to this definition")  
Returns the time stamp relative to the first time stamp (of the recording group and master recording group) until that the running synchronization will be evaluated. If the time limit is reached, the synchronization will fail.

Returns:  The relative time limit as expression

Return type:  str

GetType()[¶](#ApiClient.CrossCorrelationSynchronization.GetType "Link to this definition")  
Returns the type of this synchronization.

Returns:  The type of this synchronization (can be ‘Offset’, ‘Expectation’, ‘EqualnessMatching’ or ‘LeastSquares’, ‘AutosarTime’)

Return type:  str

IsConsiderNegativeEnabled()[¶](#ApiClient.CrossCorrelationSynchronization.IsConsiderNegativeEnabled "Link to this definition")  
Returns whether the consideration of negative correlations is enabled.

Returns:  True if feature is active, False otherwise

Return type:  bool

IsFirstSampleDifferenceCorrected()[¶](#ApiClient.CrossCorrelationSynchronization.IsFirstSampleDifferenceCorrected "Link to this definition")  
Returns whether the parameter maxDeltaT is corrected by the difference of the time stamps of the first samples (of the recording group and master recording group). Suppose that the time axes to be synchronized start at 20s and 50s, respectively. Then activating this option acts as if maxDeltaT was increased by 30s.

Returns:  The setting for the interpretation of maxDeltaT

Return type:  boolean

IsMinCorrelationEnabled()[¶](#ApiClient.CrossCorrelationSynchronization.IsMinCorrelationEnabled "Link to this definition")  
Returns whether a comparison with a minimum necessary correlation coefficient is performed.

Returns:  True if feature is active, False otherwise

Return type:  bool

SetFirstSampleDifferenceCorrected(*isCorrected*)[¶](#ApiClient.CrossCorrelationSynchronization.SetFirstSampleDifferenceCorrected "Link to this definition")  
Sets whether the parameter maxDeltaT is corrected by the difference of the time stamps of the first samples (of the recording group and master recording group). Suppose that the time axes to be synchronized start at 20s and 50s, respectively. Then activating this option acts as if maxDeltaT was increased by 30s.

Parameters:  **isCorrected** (*boolean*) – The setting for the interpretation of maxDeltaT

SetMaster(*recordingGroup*)[¶](#ApiClient.CrossCorrelationSynchronization.SetMaster "Link to this definition")  
Sets the master recording group for the synchronization.

Parameters:  **recordingGroup** ([`RecordingGroup`](SignalRecordingApi.md#ApiClient.RecordingGroup "ApiClient.RecordingGroup")) – The master recording group.

SetMasterSignal(*signalName*, *signalType='PHY'*)[¶](#ApiClient.CrossCorrelationSynchronization.SetMasterSignal "Link to this definition")  
Sets name and type of the master signal for the synchronization. The type must be either “PHY” (interpreted as number, default) or “RAW” (raw values).

Parameters:  - **signalName** (*str*) – Name of the master signal for synchronization

- **signalType** (*str*) – Type of the master signal for synchronization

SetMaxDeltaT(*maxDeltaT*)[¶](#ApiClient.CrossCorrelationSynchronization.SetMaxDeltaT "Link to this definition")  
Sets the bound for deltaT to the value maxDeltaT. If deltaT is found to be greater than this bound, the synchronization will fail.

Parameters:  **maxDeltaT** (*str*) – The maximum for deltaT as expression

SetMinCorrelation(*minCorrelation*)[¶](#ApiClient.CrossCorrelationSynchronization.SetMinCorrelation "Link to this definition")  
Sets the minimum necessary correlation coefficient for the synchronization.

Parameters:  **minCorrelation** (*str*) – Minimum necessary correlation coefficient

SetOffset(*offset*)[¶](#ApiClient.CrossCorrelationSynchronization.SetOffset "Link to this definition")  
Sets (known) offset. The offset will be added to the calculated deltaT. By default, it is only used for the OffsetSynchronization.

Parameters:  **offset** (*str*) – The (known) offset as expression

SetOffsetUsed(*used*)[¶](#ApiClient.CrossCorrelationSynchronization.SetOffsetUsed "Link to this definition")  
Sets whether the known offset should be applied. For the ExpectationSynchronization and EqualnessMatchingSynchronization the known offset will be added to the calculated deltaT. The known offset will always be used by the OffsetSynchronization.

Parameters:  **used** (*boolean*) – True if the offset should be used, else False.

SetRecordingSignal(*signalName*, *signalType='PHY'*)[¶](#ApiClient.CrossCorrelationSynchronization.SetRecordingSignal "Link to this definition")  
Sets name and type of the recording signal to be synchronized with the master signal. The type must be either “PHY” (interpreted as number, default) or “RAW” (raw values).

Parameters:  - **signalName** (*str*) – Name of the master signal for synchronization

- **signalType** (*str*) – Type of the master signal for synchronization

SetResolution(*resolution*)[¶](#ApiClient.CrossCorrelationSynchronization.SetResolution "Link to this definition")  
Sets the resolution (step size) at which the synchronization offset is determined.

Parameters:  **resolution** (*str*) – Resolution (step size) for the synchronization as an expression

SetTimeLimit(*timeLimit*)[¶](#ApiClient.CrossCorrelationSynchronization.SetTimeLimit "Link to this definition")  
Sets the time stamp relative to the first time stamp (of the recording group and master recording group) until that the running synchronization will be evaluated. If the time limit is reached, the synchronization will fail.

Parameters:  **timeLimit** (*str*) – The relative time limit as expression

## EqualnessMatchingSynchronization[¶](#equalnessmatchingsynchronization "Link to this heading")

*class* EqualnessMatchingSynchronization[¶](#ApiClient.EqualnessMatchingSynchronization "Link to this definition")  
Base class

[`Synchronization`](#ApiClient.Synchronization "ApiClient.Synchronization")

Returned by

- [`SyncConfig.AssignEqualnessMatchingSynchronization`](#ApiClient.SyncConfig.AssignEqualnessMatchingSynchronization "ApiClient.SyncConfig.AssignEqualnessMatchingSynchronization")

AppendEqualEntry(*name*, *masterName*, *eventType*)[¶](#ApiClient.EqualnessMatchingSynchronization.AppendEqualEntry "Link to this definition")  
Adds an equal entry to this synchronization object.

Parameters:  - **name** (*str*) – The signal name of the associated recording group

- **masterName** (*str*) – The signal name of the selected master recording group

- **eventType** (*str*) – The event type for the equalness matching. Possible values are ‘RAW’, ‘PHY’, and ‘STR’.

Returns:  An object representing the equal entry

Return type:  [`EqualEntry`](#ApiClient.EqualEntry "ApiClient.EqualEntry")

Clone()[¶](#ApiClient.EqualnessMatchingSynchronization.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`EqualnessMatchingSynchronization`](#ApiClient.EqualnessMatchingSynchronization "ApiClient.EqualnessMatchingSynchronization")

GetEqualEntries()[¶](#ApiClient.EqualnessMatchingSynchronization.GetEqualEntries "Link to this definition")  
Returns all equal entries.

Returns:  The list of equal entries

Return type:  list[[`EqualEntry`](#ApiClient.EqualEntry "ApiClient.EqualEntry")]

GetMaster()[¶](#ApiClient.EqualnessMatchingSynchronization.GetMaster "Link to this definition")  
Returns the master recording group for this synchronization.

Returns:  The master recording group

Return type:  [`RecordingGroup`](SignalRecordingApi.md#ApiClient.RecordingGroup "ApiClient.RecordingGroup")

GetMaxDeltaT()[¶](#ApiClient.EqualnessMatchingSynchronization.GetMaxDeltaT "Link to this definition")  
Returns the bound for deltaT. If deltaT is found to be greater than this bound, the synchronization will fail.

Returns:  The maximum for deltaT as expression

Return type:  str

GetOffset()[¶](#ApiClient.EqualnessMatchingSynchronization.GetOffset "Link to this definition")  
Returns the (known) offset. The offset will be added to the calculated deltaT. By default, it is only used for the OffsetSynchronization.

Returns:  The (known) offset as expression

Return type:  str

GetOffsetUsed()[¶](#ApiClient.EqualnessMatchingSynchronization.GetOffsetUsed "Link to this definition")  
Sets whether the known offset should be applied. For the ExpectationSynchronization and EqualnessMatchingSynchronization the known offset will be added to the calculated deltaT. The known offset will always be used by the OffsetSynchronization.

Returns:  True if the offset will be used, else False.

Return type:  boolean

GetRecordingGroupName()[¶](#ApiClient.EqualnessMatchingSynchronization.GetRecordingGroupName "Link to this definition")  
Returns the name of the recording group for this synchronization.

Returns:  The name of the recording group

Return type:  str

GetTimeLimit()[¶](#ApiClient.EqualnessMatchingSynchronization.GetTimeLimit "Link to this definition")  
Returns the time stamp relative to the first time stamp (of the recording group and master recording group) until that the running synchronization will be evaluated. If the time limit is reached, the synchronization will fail.

Returns:  The relative time limit as expression

Return type:  str

GetType()[¶](#ApiClient.EqualnessMatchingSynchronization.GetType "Link to this definition")  
Returns the type of this synchronization.

Returns:  The type of this synchronization (can be ‘Offset’, ‘Expectation’, ‘EqualnessMatching’ or ‘LeastSquares’, ‘AutosarTime’)

Return type:  str

IsFirstSampleDifferenceCorrected()[¶](#ApiClient.EqualnessMatchingSynchronization.IsFirstSampleDifferenceCorrected "Link to this definition")  
Returns whether the parameter maxDeltaT is corrected by the difference of the time stamps of the first samples (of the recording group and master recording group). Suppose that the time axes to be synchronized start at 20s and 50s, respectively. Then activating this option acts as if maxDeltaT was increased by 30s.

Returns:  The setting for the interpretation of maxDeltaT

Return type:  boolean

RemoveEqualEntry(*equalEntry*)[¶](#ApiClient.EqualnessMatchingSynchronization.RemoveEqualEntry "Link to this definition")  
Removes the given equal entry from this synchronization object.

Parameters:  **equalEntry** ([`EqualEntry`](#ApiClient.EqualEntry "ApiClient.EqualEntry")) – equal entry to be removed

SetFirstSampleDifferenceCorrected(*isCorrected*)[¶](#ApiClient.EqualnessMatchingSynchronization.SetFirstSampleDifferenceCorrected "Link to this definition")  
Sets whether the parameter maxDeltaT is corrected by the difference of the time stamps of the first samples (of the recording group and master recording group). Suppose that the time axes to be synchronized start at 20s and 50s, respectively. Then activating this option acts as if maxDeltaT was increased by 30s.

Parameters:  **isCorrected** (*boolean*) – The setting for the interpretation of maxDeltaT

SetMaster(*recordingGroup*)[¶](#ApiClient.EqualnessMatchingSynchronization.SetMaster "Link to this definition")  
Sets the master recording group for the synchronization.

Parameters:  **recordingGroup** ([`RecordingGroup`](SignalRecordingApi.md#ApiClient.RecordingGroup "ApiClient.RecordingGroup")) – The master recording group.

SetMaxDeltaT(*maxDeltaT*)[¶](#ApiClient.EqualnessMatchingSynchronization.SetMaxDeltaT "Link to this definition")  
Sets the bound for deltaT to the value maxDeltaT. If deltaT is found to be greater than this bound, the synchronization will fail.

Parameters:  **maxDeltaT** (*str*) – The maximum for deltaT as expression

SetOffset(*offset*)[¶](#ApiClient.EqualnessMatchingSynchronization.SetOffset "Link to this definition")  
Sets (known) offset. The offset will be added to the calculated deltaT. By default, it is only used for the OffsetSynchronization.

Parameters:  **offset** (*str*) – The (known) offset as expression

SetOffsetUsed(*used*)[¶](#ApiClient.EqualnessMatchingSynchronization.SetOffsetUsed "Link to this definition")  
Sets whether the known offset should be applied. For the ExpectationSynchronization and EqualnessMatchingSynchronization the known offset will be added to the calculated deltaT. The known offset will always be used by the OffsetSynchronization.

Parameters:  **used** (*boolean*) – True if the offset should be used, else False.

SetTimeLimit(*timeLimit*)[¶](#ApiClient.EqualnessMatchingSynchronization.SetTimeLimit "Link to this definition")  
Sets the time stamp relative to the first time stamp (of the recording group and master recording group) until that the running synchronization will be evaluated. If the time limit is reached, the synchronization will fail.

Parameters:  **timeLimit** (*str*) – The relative time limit as expression

## EqualEntry[¶](#equalentry "Link to this heading")

*class* EqualEntry[¶](#ApiClient.EqualEntry "Link to this definition")  
Returned by

- [`EqualnessMatchingSynchronization.AppendEqualEntry`](#ApiClient.EqualnessMatchingSynchronization.AppendEqualEntry "ApiClient.EqualnessMatchingSynchronization.AppendEqualEntry")

- [`EqualnessMatchingSynchronization.GetEqualEntries`](#ApiClient.EqualnessMatchingSynchronization.GetEqualEntries "ApiClient.EqualnessMatchingSynchronization.GetEqualEntries")

Clone()[¶](#ApiClient.EqualEntry.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`EqualEntry`](#ApiClient.EqualEntry "ApiClient.EqualEntry")

GetEventType()[¶](#ApiClient.EqualEntry.GetEventType "Link to this definition")  
Return the event type for this equalness matching. Possible values are ‘RAW’, ‘PHY’, and ‘STR’.

Returns:  The event type

Return type:  str

GetMasterName()[¶](#ApiClient.EqualEntry.GetMasterName "Link to this definition")  
Returns the signal name of the selected master recording group that is used for the equalness synchronization.

Returns:  The signal name

Return type:  str

GetName()[¶](#ApiClient.EqualEntry.GetName "Link to this definition")  
Returns the signal name of the associated recording group that is used for the equalness synchronization.

Returns:  The signal name

Return type:  str

SetEventType(*eventType*)[¶](#ApiClient.EqualEntry.SetEventType "Link to this definition")  
Sets the event type to use for this equalness matching.

Parameters:  **eventType** (*str*) – Type of event: ‘RAW’, ‘PHY’, or ‘STR’

SetMasterName(*masterName*)[¶](#ApiClient.EqualEntry.SetMasterName "Link to this definition")  
Sets the signal (by name) of the selected master recording group to use for the equalness synchronization.

Parameters:  **masterName** (*str*) – The name of the signal

SetName(*name*)[¶](#ApiClient.EqualEntry.SetName "Link to this definition")  
Sets the signal (by name) of the associated recording group to use for the equalness synchronization.

Parameters:  **name** (*str*) – The name of the signal

## ExpectationSynchronization[¶](#expectationsynchronization "Link to this heading")

*class* ExpectationSynchronization[¶](#ApiClient.ExpectationSynchronization "Link to this definition")  
Base class

[`Synchronization`](#ApiClient.Synchronization "ApiClient.Synchronization")

Returned by

- [`SyncConfig.AssignExpectationSynchronization`](#ApiClient.SyncConfig.AssignExpectationSynchronization "ApiClient.SyncConfig.AssignExpectationSynchronization")

Clone()[¶](#ApiClient.ExpectationSynchronization.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`ExpectationSynchronization`](#ApiClient.ExpectationSynchronization "ApiClient.ExpectationSynchronization")

GetMaster()[¶](#ApiClient.ExpectationSynchronization.GetMaster "Link to this definition")  
Returns the master recording group for this synchronization.

Returns:  The master recording group

Return type:  [`RecordingGroup`](SignalRecordingApi.md#ApiClient.RecordingGroup "ApiClient.RecordingGroup")

GetMasterExpectation()[¶](#ApiClient.ExpectationSynchronization.GetMasterExpectation "Link to this definition")  
Returns the expectation of the master recording group.

Returns:  The master recording group expectation

Return type:  [`SyncExpectation`](#ApiClient.SyncExpectation "ApiClient.SyncExpectation")

GetMaxDeltaT()[¶](#ApiClient.ExpectationSynchronization.GetMaxDeltaT "Link to this definition")  
Returns the bound for deltaT. If deltaT is found to be greater than this bound, the synchronization will fail.

Returns:  The maximum for deltaT as expression

Return type:  str

GetOffset()[¶](#ApiClient.ExpectationSynchronization.GetOffset "Link to this definition")  
Returns the (known) offset. The offset will be added to the calculated deltaT. By default, it is only used for the OffsetSynchronization.

Returns:  The (known) offset as expression

Return type:  str

GetOffsetUsed()[¶](#ApiClient.ExpectationSynchronization.GetOffsetUsed "Link to this definition")  
Sets whether the known offset should be applied. For the ExpectationSynchronization and EqualnessMatchingSynchronization the known offset will be added to the calculated deltaT. The known offset will always be used by the OffsetSynchronization.

Returns:  True if the offset will be used, else False.

Return type:  boolean

GetRecordingGroupExpectation()[¶](#ApiClient.ExpectationSynchronization.GetRecordingGroupExpectation "Link to this definition")  
Returns the recording group expectation .

Returns:  The recording group expectation

Return type:  [`SyncExpectation`](#ApiClient.SyncExpectation "ApiClient.SyncExpectation")

GetRecordingGroupName()[¶](#ApiClient.ExpectationSynchronization.GetRecordingGroupName "Link to this definition")  
Returns the name of the recording group for this synchronization.

Returns:  The name of the recording group

Return type:  str

GetTimeLimit()[¶](#ApiClient.ExpectationSynchronization.GetTimeLimit "Link to this definition")  
Returns the time stamp relative to the first time stamp (of the recording group and master recording group) until that the running synchronization will be evaluated. If the time limit is reached, the synchronization will fail.

Returns:  The relative time limit as expression

Return type:  str

GetType()[¶](#ApiClient.ExpectationSynchronization.GetType "Link to this definition")  
Returns the type of this synchronization.

Returns:  The type of this synchronization (can be ‘Offset’, ‘Expectation’, ‘EqualnessMatching’ or ‘LeastSquares’, ‘AutosarTime’)

Return type:  str

IsFirstSampleDifferenceCorrected()[¶](#ApiClient.ExpectationSynchronization.IsFirstSampleDifferenceCorrected "Link to this definition")  
Returns whether the parameter maxDeltaT is corrected by the difference of the time stamps of the first samples (of the recording group and master recording group). Suppose that the time axes to be synchronized start at 20s and 50s, respectively. Then activating this option acts as if maxDeltaT was increased by 30s.

Returns:  The setting for the interpretation of maxDeltaT

Return type:  boolean

SetFirstSampleDifferenceCorrected(*isCorrected*)[¶](#ApiClient.ExpectationSynchronization.SetFirstSampleDifferenceCorrected "Link to this definition")  
Sets whether the parameter maxDeltaT is corrected by the difference of the time stamps of the first samples (of the recording group and master recording group). Suppose that the time axes to be synchronized start at 20s and 50s, respectively. Then activating this option acts as if maxDeltaT was increased by 30s.

Parameters:  **isCorrected** (*boolean*) – The setting for the interpretation of maxDeltaT

SetMaster(*recordingGroup*)[¶](#ApiClient.ExpectationSynchronization.SetMaster "Link to this definition")  
Sets the master recording group for the synchronization.

Parameters:  **recordingGroup** ([`RecordingGroup`](SignalRecordingApi.md#ApiClient.RecordingGroup "ApiClient.RecordingGroup")) – The master recording group.

SetMaxDeltaT(*maxDeltaT*)[¶](#ApiClient.ExpectationSynchronization.SetMaxDeltaT "Link to this definition")  
Sets the bound for deltaT to the value maxDeltaT. If deltaT is found to be greater than this bound, the synchronization will fail.

Parameters:  **maxDeltaT** (*str*) – The maximum for deltaT as expression

SetOffset(*offset*)[¶](#ApiClient.ExpectationSynchronization.SetOffset "Link to this definition")  
Sets (known) offset. The offset will be added to the calculated deltaT. By default, it is only used for the OffsetSynchronization.

Parameters:  **offset** (*str*) – The (known) offset as expression

SetOffsetUsed(*used*)[¶](#ApiClient.ExpectationSynchronization.SetOffsetUsed "Link to this definition")  
Sets whether the known offset should be applied. For the ExpectationSynchronization and EqualnessMatchingSynchronization the known offset will be added to the calculated deltaT. The known offset will always be used by the OffsetSynchronization.

Parameters:  **used** (*boolean*) – True if the offset should be used, else False.

SetTimeLimit(*timeLimit*)[¶](#ApiClient.ExpectationSynchronization.SetTimeLimit "Link to this definition")  
Sets the time stamp relative to the first time stamp (of the recording group and master recording group) until that the running synchronization will be evaluated. If the time limit is reached, the synchronization will fail.

Parameters:  **timeLimit** (*str*) – The relative time limit as expression

## SyncExpectation[¶](#syncexpectation "Link to this heading")

*class* SyncExpectation[¶](#ApiClient.SyncExpectation "Link to this definition")  
Returned by

- [`ExpectationSynchronization.GetMasterExpectation`](#ApiClient.ExpectationSynchronization.GetMasterExpectation "ApiClient.ExpectationSynchronization.GetMasterExpectation")

- [`ExpectationSynchronization.GetRecordingGroupExpectation`](#ApiClient.ExpectationSynchronization.GetRecordingGroupExpectation "ApiClient.ExpectationSynchronization.GetRecordingGroupExpectation")

Clone()[¶](#ApiClient.SyncExpectation.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`SyncExpectation`](#ApiClient.SyncExpectation "ApiClient.SyncExpectation")

GetEventType()[¶](#ApiClient.SyncExpectation.GetEventType "Link to this definition")  
Returns the event type of the signal.

Returns:  The event type (“RAW” or “PHY”).

Return type:  string

GetExpectationExpression()[¶](#ApiClient.SyncExpectation.GetExpectationExpression "Link to this definition")  
Returns the expectation expression as text.

Returns:  The expectation expression

Return type:  str

GetExpectationParameters()[¶](#ApiClient.SyncExpectation.GetExpectationParameters "Link to this definition")  
Returns the parameters of the numeric expectation expression as dictionary.

Returns:  Dictionary with keys ‘relation’, ‘value’, ‘toleranceType’, ‘toleranceValue’

Return type:  dict[str, str]

GetSignalName()[¶](#ApiClient.SyncExpectation.GetSignalName "Link to this definition")  
Returns the signal name of the signal that should be evaluated.

Returns:  The signal name

Return type:  str

SetEventType(*eventType*)[¶](#ApiClient.SyncExpectation.SetEventType "Link to this definition")  
Set the event type of the signal.

Parameters:  **eventType** (*string*) – “RAW” or “PHY”

SetExpectationParameters(*relation*, *value*, *toleranceType=None*, *toleranceValue=None*)[¶](#ApiClient.SyncExpectation.SetExpectationParameters "Link to this definition")  
Sets the parameters of the numeric expectation expression. The parameters toleranceType and toleranceValue can be passed if relation is ‘==’.

Parameters:  - **relation** (*str*) – The relation between the signal value and the expected value. One of: ‘\<’, ‘\<=’, ‘==’, ‘\>=’, ‘\>’, ‘!=’, ‘\<\>’

- **value** (*str*) – The expected value as expression

- **toleranceType** (*str*) – Optional, must be ‘none’ if relation is not ‘==’. Flag for the tolerance. One of: - ‘none’ (no tolerance) - ‘absolute’ (absolute) - ‘percentage’ (relative in percent) - ‘fractional digits’

- **toleranceValue** (*str*) – Optional. The tolerance value as expression if a tolerance is used.

SetSignalName(*signalName*)[¶](#ApiClient.SyncExpectation.SetSignalName "Link to this definition")  
Sets the signal name of the signal that should be evaluated.

Parameters:  **signalName** (*str*) – The signal name

## LeastSquaresSynchronization[¶](#leastsquaressynchronization "Link to this heading")

*class* LeastSquaresSynchronization[¶](#ApiClient.LeastSquaresSynchronization "Link to this definition")  
Base class

[`Synchronization`](#ApiClient.Synchronization "ApiClient.Synchronization")

Returned by

- [`SyncConfig.AssignLeastSquaresSynchronization`](#ApiClient.SyncConfig.AssignLeastSquaresSynchronization "ApiClient.SyncConfig.AssignLeastSquaresSynchronization")

Clone()[¶](#ApiClient.LeastSquaresSynchronization.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`LeastSquaresSynchronization`](#ApiClient.LeastSquaresSynchronization "ApiClient.LeastSquaresSynchronization")

EnableMinR2(*enable=True*)[¶](#ApiClient.LeastSquaresSynchronization.EnableMinR2 "Link to this definition")  
Enables (default) or disables the check for a minimum necessary coefficient of determination R^2 between the matched signals.

Parameters:  **enable** (*bool*) – True to enable, False to disable

GetMaster()[¶](#ApiClient.LeastSquaresSynchronization.GetMaster "Link to this definition")  
Returns the master recording group for this synchronization.

Returns:  The master recording group

Return type:  [`RecordingGroup`](SignalRecordingApi.md#ApiClient.RecordingGroup "ApiClient.RecordingGroup")

GetMasterSignal()[¶](#ApiClient.LeastSquaresSynchronization.GetMasterSignal "Link to this definition")  
Returns the signalName and signalType of the master signal. The type will be either “PHY” (interpreted as number) or “RAW” (raw values).

Returns:  Dictionary with keys “signalName”, “signalType”

Return type:  dict[str, str]

GetMaxDeltaT()[¶](#ApiClient.LeastSquaresSynchronization.GetMaxDeltaT "Link to this definition")  
Returns the bound for deltaT. If deltaT is found to be greater than this bound, the synchronization will fail.

Returns:  The maximum for deltaT as expression

Return type:  str

GetMinR2()[¶](#ApiClient.LeastSquaresSynchronization.GetMinR2 "Link to this definition")  
Returns the minimum necessary coefficient of determination R^2 for the synchronization.

Returns:  Minimum necessary coefficient of determination R^2

Return type:  str

GetOffset()[¶](#ApiClient.LeastSquaresSynchronization.GetOffset "Link to this definition")  
Returns the (known) offset. The offset will be added to the calculated deltaT. By default, it is only used for the OffsetSynchronization.

Returns:  The (known) offset as expression

Return type:  str

GetOffsetUsed()[¶](#ApiClient.LeastSquaresSynchronization.GetOffsetUsed "Link to this definition")  
Sets whether the known offset should be applied. For the ExpectationSynchronization and EqualnessMatchingSynchronization the known offset will be added to the calculated deltaT. The known offset will always be used by the OffsetSynchronization.

Returns:  True if the offset will be used, else False.

Return type:  boolean

GetRecordingGroupName()[¶](#ApiClient.LeastSquaresSynchronization.GetRecordingGroupName "Link to this definition")  
Returns the name of the recording group for this synchronization.

Returns:  The name of the recording group

Return type:  str

GetRecordingSignal()[¶](#ApiClient.LeastSquaresSynchronization.GetRecordingSignal "Link to this definition")  
Returns the signalName and signalType of the recording signal for synchronization. The type will be either “PHY” (interpreted as number) or “RAW” (raw values).

Returns:  Dictionary with keys “signalName”, “signalType”

Return type:  dict[str, str]

GetResolution()[¶](#ApiClient.LeastSquaresSynchronization.GetResolution "Link to this definition")  
Returns the resolution (step size) at which the synchronization offset is determined.

Returns:  Resolution (step size) for the synchronization as expression

Return type:  str

GetTimeLimit()[¶](#ApiClient.LeastSquaresSynchronization.GetTimeLimit "Link to this definition")  
Returns the time stamp relative to the first time stamp (of the recording group and master recording group) until that the running synchronization will be evaluated. If the time limit is reached, the synchronization will fail.

Returns:  The relative time limit as expression

Return type:  str

GetType()[¶](#ApiClient.LeastSquaresSynchronization.GetType "Link to this definition")  
Returns the type of this synchronization.

Returns:  The type of this synchronization (can be ‘Offset’, ‘Expectation’, ‘EqualnessMatching’ or ‘LeastSquares’, ‘AutosarTime’)

Return type:  str

IsFirstSampleDifferenceCorrected()[¶](#ApiClient.LeastSquaresSynchronization.IsFirstSampleDifferenceCorrected "Link to this definition")  
Returns whether the parameter maxDeltaT is corrected by the difference of the time stamps of the first samples (of the recording group and master recording group). Suppose that the time axes to be synchronized start at 20s and 50s, respectively. Then activating this option acts as if maxDeltaT was increased by 30s.

Returns:  The setting for the interpretation of maxDeltaT

Return type:  boolean

IsMinR2Enabled()[¶](#ApiClient.LeastSquaresSynchronization.IsMinR2Enabled "Link to this definition")  
Returns whether a comparison with a minimum necessary coefficient of determination R^2 is performed.

Returns:  True if feature is active, False otherwise

Return type:  bool

SetFirstSampleDifferenceCorrected(*isCorrected*)[¶](#ApiClient.LeastSquaresSynchronization.SetFirstSampleDifferenceCorrected "Link to this definition")  
Sets whether the parameter maxDeltaT is corrected by the difference of the time stamps of the first samples (of the recording group and master recording group). Suppose that the time axes to be synchronized start at 20s and 50s, respectively. Then activating this option acts as if maxDeltaT was increased by 30s.

Parameters:  **isCorrected** (*boolean*) – The setting for the interpretation of maxDeltaT

SetMaster(*recordingGroup*)[¶](#ApiClient.LeastSquaresSynchronization.SetMaster "Link to this definition")  
Sets the master recording group for the synchronization.

Parameters:  **recordingGroup** ([`RecordingGroup`](SignalRecordingApi.md#ApiClient.RecordingGroup "ApiClient.RecordingGroup")) – The master recording group.

SetMasterSignal(*signalName*, *signalType='PHY'*)[¶](#ApiClient.LeastSquaresSynchronization.SetMasterSignal "Link to this definition")  
Sets name and type of the master signal for the synchronization. The type must be either “PHY” (interpreted as number, default) or “RAW” (raw values).

Parameters:  - **signalName** (*str*) – Name of the master signal for synchronization

- **signalType** (*str*) – Type of the master signal for synchronization

SetMaxDeltaT(*maxDeltaT*)[¶](#ApiClient.LeastSquaresSynchronization.SetMaxDeltaT "Link to this definition")  
Sets the bound for deltaT to the value maxDeltaT. If deltaT is found to be greater than this bound, the synchronization will fail.

Parameters:  **maxDeltaT** (*str*) – The maximum for deltaT as expression

SetMinR2(*minR2*)[¶](#ApiClient.LeastSquaresSynchronization.SetMinR2 "Link to this definition")  
Sets the minimum necessary coefficient of determination R^2 for the synchronization.

Parameters:  **minR2** (*str*) – Minimum necessary coefficient of determination R^2

SetOffset(*offset*)[¶](#ApiClient.LeastSquaresSynchronization.SetOffset "Link to this definition")  
Sets (known) offset. The offset will be added to the calculated deltaT. By default, it is only used for the OffsetSynchronization.

Parameters:  **offset** (*str*) – The (known) offset as expression

SetOffsetUsed(*used*)[¶](#ApiClient.LeastSquaresSynchronization.SetOffsetUsed "Link to this definition")  
Sets whether the known offset should be applied. For the ExpectationSynchronization and EqualnessMatchingSynchronization the known offset will be added to the calculated deltaT. The known offset will always be used by the OffsetSynchronization.

Parameters:  **used** (*boolean*) – True if the offset should be used, else False.

SetRecordingSignal(*signalName*, *signalType='PHY'*)[¶](#ApiClient.LeastSquaresSynchronization.SetRecordingSignal "Link to this definition")  
Sets name and type of the recording signal to be synchronized with the master signal. The type must be either “PHY” (interpreted as number, default) or “RAW” (raw values).

Parameters:  - **signalName** (*str*) – Name of the master signal for synchronization

- **signalType** (*str*) – Type of the master signal for synchronization

SetResolution(*resolution*)[¶](#ApiClient.LeastSquaresSynchronization.SetResolution "Link to this definition")  
Sets the resolution (step size) at which the synchronization offset is determined.

Parameters:  **resolution** (*str*) – Resolution (step size) for the synchronization as an expression

SetTimeLimit(*timeLimit*)[¶](#ApiClient.LeastSquaresSynchronization.SetTimeLimit "Link to this definition")  
Sets the time stamp relative to the first time stamp (of the recording group and master recording group) until that the running synchronization will be evaluated. If the time limit is reached, the synchronization will fail.

Parameters:  **timeLimit** (*str*) – The relative time limit as expression

## OffsetSynchronization[¶](#offsetsynchronization "Link to this heading")

*class* OffsetSynchronization[¶](#ApiClient.OffsetSynchronization "Link to this definition")  
Base class

[`Synchronization`](#ApiClient.Synchronization "ApiClient.Synchronization")

Returned by

- [`SyncConfig.AssignOffsetSynchronization`](#ApiClient.SyncConfig.AssignOffsetSynchronization "ApiClient.SyncConfig.AssignOffsetSynchronization")

Clone()[¶](#ApiClient.OffsetSynchronization.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`OffsetSynchronization`](#ApiClient.OffsetSynchronization "ApiClient.OffsetSynchronization")

GetMaster()[¶](#ApiClient.OffsetSynchronization.GetMaster "Link to this definition")  
Returns the master recording group for this synchronization.

Returns:  The master recording group

Return type:  [`RecordingGroup`](SignalRecordingApi.md#ApiClient.RecordingGroup "ApiClient.RecordingGroup")

GetMaxDeltaT()[¶](#ApiClient.OffsetSynchronization.GetMaxDeltaT "Link to this definition")  
Returns the bound for deltaT. If deltaT is found to be greater than this bound, the synchronization will fail.

Returns:  The maximum for deltaT as expression

Return type:  str

GetOffset()[¶](#ApiClient.OffsetSynchronization.GetOffset "Link to this definition")  
Returns the (known) offset. The offset will be added to the calculated deltaT. By default, it is only used for the OffsetSynchronization.

Returns:  The (known) offset as expression

Return type:  str

GetOffsetUsed()[¶](#ApiClient.OffsetSynchronization.GetOffsetUsed "Link to this definition")  
Sets whether the known offset should be applied. For the ExpectationSynchronization and EqualnessMatchingSynchronization the known offset will be added to the calculated deltaT. The known offset will always be used by the OffsetSynchronization.

Returns:  True if the offset will be used, else False.

Return type:  boolean

GetRecordingGroupName()[¶](#ApiClient.OffsetSynchronization.GetRecordingGroupName "Link to this definition")  
Returns the name of the recording group for this synchronization.

Returns:  The name of the recording group

Return type:  str

GetTimeLimit()[¶](#ApiClient.OffsetSynchronization.GetTimeLimit "Link to this definition")  
Returns the time stamp relative to the first time stamp (of the recording group and master recording group) until that the running synchronization will be evaluated. If the time limit is reached, the synchronization will fail.

Returns:  The relative time limit as expression

Return type:  str

GetType()[¶](#ApiClient.OffsetSynchronization.GetType "Link to this definition")  
Returns the type of this synchronization.

Returns:  The type of this synchronization (can be ‘Offset’, ‘Expectation’, ‘EqualnessMatching’ or ‘LeastSquares’, ‘AutosarTime’)

Return type:  str

IsFirstSampleDifferenceCorrected()[¶](#ApiClient.OffsetSynchronization.IsFirstSampleDifferenceCorrected "Link to this definition")  
Returns whether the parameter maxDeltaT is corrected by the difference of the time stamps of the first samples (of the recording group and master recording group). Suppose that the time axes to be synchronized start at 20s and 50s, respectively. Then activating this option acts as if maxDeltaT was increased by 30s.

Returns:  The setting for the interpretation of maxDeltaT

Return type:  boolean

SetFirstSampleDifferenceCorrected(*isCorrected*)[¶](#ApiClient.OffsetSynchronization.SetFirstSampleDifferenceCorrected "Link to this definition")  
Not available. maxDeltaT is not used by the offset synchronization.

Parameters:  **isCorrected** (*boolean*) – The setting for the interpretation of maxDeltaT

SetMaster(*recordingGroup*)[¶](#ApiClient.OffsetSynchronization.SetMaster "Link to this definition")  
Sets the master recording group for the synchronization.

Parameters:  **recordingGroup** ([`RecordingGroup`](SignalRecordingApi.md#ApiClient.RecordingGroup "ApiClient.RecordingGroup")) – The master recording group.

SetMaxDeltaT(*maxDeltaT*)[¶](#ApiClient.OffsetSynchronization.SetMaxDeltaT "Link to this definition")  
Not available. maxDeltaT is not used by the offset synchronization.

Parameters:  **maxDeltaT** (*str*) – The maximum for deltaT as expression

SetOffset(*offset*)[¶](#ApiClient.OffsetSynchronization.SetOffset "Link to this definition")  
Sets (known) offset. The offset will be added to the calculated deltaT. By default, it is only used for the OffsetSynchronization.

Parameters:  **offset** (*str*) – The (known) offset as expression

SetOffsetUsed(*used*)[¶](#ApiClient.OffsetSynchronization.SetOffsetUsed "Link to this definition")  
Not available. The offset will always be used by this synchronization.

Parameters:  **used** (*boolean*) – True if the offset should be used, else False.

SetTimeLimit(*timeLimit*)[¶](#ApiClient.OffsetSynchronization.SetTimeLimit "Link to this definition")  
Not available. TimeLimit is not used by the offset synchronization.

Parameters:  **timeLimit** (*str*) – The relative time limit as expression

## UtcTimestampSynchronization[¶](#utctimestampsynchronization "Link to this heading")

*class* UtcTimestampSynchronization[¶](#ApiClient.UtcTimestampSynchronization "Link to this definition")  
Base class

[`Synchronization`](#ApiClient.Synchronization "ApiClient.Synchronization")

Returned by

- [`SyncConfig.AssignUtcTimestampSynchronization`](#ApiClient.SyncConfig.AssignUtcTimestampSynchronization "ApiClient.SyncConfig.AssignUtcTimestampSynchronization")

Clone()[¶](#ApiClient.UtcTimestampSynchronization.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`UtcTimestampSynchronization`](#ApiClient.UtcTimestampSynchronization "ApiClient.UtcTimestampSynchronization")

GetMaster()[¶](#ApiClient.UtcTimestampSynchronization.GetMaster "Link to this definition")  
Returns the master recording group for this synchronization.

Returns:  The master recording group

Return type:  [`RecordingGroup`](SignalRecordingApi.md#ApiClient.RecordingGroup "ApiClient.RecordingGroup")

GetMaxDeltaT()[¶](#ApiClient.UtcTimestampSynchronization.GetMaxDeltaT "Link to this definition")  
Returns the bound for deltaT. If deltaT is found to be greater than this bound, the synchronization will fail.

Returns:  The maximum for deltaT as expression

Return type:  str

GetOffset()[¶](#ApiClient.UtcTimestampSynchronization.GetOffset "Link to this definition")  
Returns the (known) offset. The offset will be added to the calculated deltaT. By default, it is only used for the OffsetSynchronization.

Returns:  The (known) offset as expression

Return type:  str

GetOffsetUsed()[¶](#ApiClient.UtcTimestampSynchronization.GetOffsetUsed "Link to this definition")  
Sets whether the known offset should be applied. For the ExpectationSynchronization and EqualnessMatchingSynchronization the known offset will be added to the calculated deltaT. The known offset will always be used by the OffsetSynchronization.

Returns:  True if the offset will be used, else False.

Return type:  boolean

GetRecordingGroupName()[¶](#ApiClient.UtcTimestampSynchronization.GetRecordingGroupName "Link to this definition")  
Returns the name of the recording group for this synchronization.

Returns:  The name of the recording group

Return type:  str

GetTimeLimit()[¶](#ApiClient.UtcTimestampSynchronization.GetTimeLimit "Link to this definition")  
Returns the time stamp relative to the first time stamp (of the recording group and master recording group) until that the running synchronization will be evaluated. If the time limit is reached, the synchronization will fail.

Returns:  The relative time limit as expression

Return type:  str

GetType()[¶](#ApiClient.UtcTimestampSynchronization.GetType "Link to this definition")  
Returns the type of this synchronization.

Returns:  The type of this synchronization (can be ‘Offset’, ‘Expectation’, ‘EqualnessMatching’ or ‘LeastSquares’, ‘AutosarTime’)

Return type:  str

IsFirstSampleDifferenceCorrected()[¶](#ApiClient.UtcTimestampSynchronization.IsFirstSampleDifferenceCorrected "Link to this definition")  
Returns whether the parameter maxDeltaT is corrected by the difference of the time stamps of the first samples (of the recording group and master recording group). Suppose that the time axes to be synchronized start at 20s and 50s, respectively. Then activating this option acts as if maxDeltaT was increased by 30s.

Returns:  The setting for the interpretation of maxDeltaT

Return type:  boolean

SetFirstSampleDifferenceCorrected(*isCorrected*)[¶](#ApiClient.UtcTimestampSynchronization.SetFirstSampleDifferenceCorrected "Link to this definition")  
Not available. maxDeltaT is not used by the UtcTimestamp synchronization.

Parameters:  **isCorrected** (*boolean*) – The setting for the interpretation of maxDeltaT

SetMaster(*recordingGroup*)[¶](#ApiClient.UtcTimestampSynchronization.SetMaster "Link to this definition")  
Sets the master recording group for the synchronization.

Parameters:  **recordingGroup** ([`RecordingGroup`](SignalRecordingApi.md#ApiClient.RecordingGroup "ApiClient.RecordingGroup")) – The master recording group.

SetMaxDeltaT(*maxDeltaT*)[¶](#ApiClient.UtcTimestampSynchronization.SetMaxDeltaT "Link to this definition")  
Not available. maxDeltaT is not used by the UtcTimestamp synchronization.

Parameters:  **maxDeltaT** (*str*) – The maximum for deltaT as expression

SetOffset(*offset*)[¶](#ApiClient.UtcTimestampSynchronization.SetOffset "Link to this definition")  
Sets (known) offset. The offset will be added to the calculated deltaT. By default, it is only used for the OffsetSynchronization.

Parameters:  **offset** (*str*) – The (known) offset as expression

SetOffsetUsed(*used*)[¶](#ApiClient.UtcTimestampSynchronization.SetOffsetUsed "Link to this definition")  
Sets whether the known offset should be applied. For the ExpectationSynchronization and EqualnessMatchingSynchronization the known offset will be added to the calculated deltaT. The known offset will always be used by the OffsetSynchronization.

Parameters:  **used** (*boolean*) – True if the offset should be used, else False.

SetTimeLimit(*timeLimit*)[¶](#ApiClient.UtcTimestampSynchronization.SetTimeLimit "Link to this definition")  
Not available. TimeLimit is not used by the UtcTimestamp synchronization.

Parameters:  **timeLimit** (*str*) – The relative time limit as expression

## Synchronization[¶](#synchronization "Link to this heading")

*class* Synchronization[¶](#ApiClient.Synchronization "Link to this definition")  
Returned by

- [`SyncConfig.GetSynchronization`](#ApiClient.SyncConfig.GetSynchronization "ApiClient.SyncConfig.GetSynchronization")

- [`SyncConfig.GetSynchronizations`](#ApiClient.SyncConfig.GetSynchronizations "ApiClient.SyncConfig.GetSynchronizations")

Subclasses

- [`AutosarTimeSynchronization`](#ApiClient.AutosarTimeSynchronization "ApiClient.AutosarTimeSynchronization")

- [`CrossCorrelationSynchronization`](#ApiClient.CrossCorrelationSynchronization "ApiClient.CrossCorrelationSynchronization")

- [`EqualnessMatchingSynchronization`](#ApiClient.EqualnessMatchingSynchronization "ApiClient.EqualnessMatchingSynchronization")

- [`ExpectationSynchronization`](#ApiClient.ExpectationSynchronization "ApiClient.ExpectationSynchronization")

- [`LeastSquaresSynchronization`](#ApiClient.LeastSquaresSynchronization "ApiClient.LeastSquaresSynchronization")

- [`OffsetSynchronization`](#ApiClient.OffsetSynchronization "ApiClient.OffsetSynchronization")

- [`UtcTimestampSynchronization`](#ApiClient.UtcTimestampSynchronization "ApiClient.UtcTimestampSynchronization")

Clone()[¶](#ApiClient.Synchronization.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`Synchronization`](#ApiClient.Synchronization "ApiClient.Synchronization")

GetMaster()[¶](#ApiClient.Synchronization.GetMaster "Link to this definition")  
Returns the master recording group for this synchronization.

Returns:  The master recording group

Return type:  [`RecordingGroup`](SignalRecordingApi.md#ApiClient.RecordingGroup "ApiClient.RecordingGroup")

GetMaxDeltaT()[¶](#ApiClient.Synchronization.GetMaxDeltaT "Link to this definition")  
Returns the bound for deltaT. If deltaT is found to be greater than this bound, the synchronization will fail.

Returns:  The maximum for deltaT as expression

Return type:  str

GetOffset()[¶](#ApiClient.Synchronization.GetOffset "Link to this definition")  
Returns the (known) offset. The offset will be added to the calculated deltaT. By default, it is only used for the OffsetSynchronization.

Returns:  The (known) offset as expression

Return type:  str

GetOffsetUsed()[¶](#ApiClient.Synchronization.GetOffsetUsed "Link to this definition")  
Sets whether the known offset should be applied. For the ExpectationSynchronization and EqualnessMatchingSynchronization the known offset will be added to the calculated deltaT. The known offset will always be used by the OffsetSynchronization.

Returns:  True if the offset will be used, else False.

Return type:  boolean

GetRecordingGroupName()[¶](#ApiClient.Synchronization.GetRecordingGroupName "Link to this definition")  
Returns the name of the recording group for this synchronization.

Returns:  The name of the recording group

Return type:  str

GetTimeLimit()[¶](#ApiClient.Synchronization.GetTimeLimit "Link to this definition")  
Returns the time stamp relative to the first time stamp (of the recording group and master recording group) until that the running synchronization will be evaluated. If the time limit is reached, the synchronization will fail.

Returns:  The relative time limit as expression

Return type:  str

GetType()[¶](#ApiClient.Synchronization.GetType "Link to this definition")  
Returns the type of this synchronization.

Returns:  The type of this synchronization (can be ‘Offset’, ‘Expectation’, ‘EqualnessMatching’ or ‘LeastSquares’, ‘AutosarTime’)

Return type:  str

IsFirstSampleDifferenceCorrected()[¶](#ApiClient.Synchronization.IsFirstSampleDifferenceCorrected "Link to this definition")  
Returns whether the parameter maxDeltaT is corrected by the difference of the time stamps of the first samples (of the recording group and master recording group). Suppose that the time axes to be synchronized start at 20s and 50s, respectively. Then activating this option acts as if maxDeltaT was increased by 30s.

Returns:  The setting for the interpretation of maxDeltaT

Return type:  boolean

SetFirstSampleDifferenceCorrected(*isCorrected*)[¶](#ApiClient.Synchronization.SetFirstSampleDifferenceCorrected "Link to this definition")  
Sets whether the parameter maxDeltaT is corrected by the difference of the time stamps of the first samples (of the recording group and master recording group). Suppose that the time axes to be synchronized start at 20s and 50s, respectively. Then activating this option acts as if maxDeltaT was increased by 30s.

Parameters:  **isCorrected** (*boolean*) – The setting for the interpretation of maxDeltaT

SetMaster(*recordingGroup*)[¶](#ApiClient.Synchronization.SetMaster "Link to this definition")  
Sets the master recording group for the synchronization.

Parameters:  **recordingGroup** ([`RecordingGroup`](SignalRecordingApi.md#ApiClient.RecordingGroup "ApiClient.RecordingGroup")) – The master recording group.

SetMaxDeltaT(*maxDeltaT*)[¶](#ApiClient.Synchronization.SetMaxDeltaT "Link to this definition")  
Sets the bound for deltaT to the value maxDeltaT. If deltaT is found to be greater than this bound, the synchronization will fail.

Parameters:  **maxDeltaT** (*str*) – The maximum for deltaT as expression

SetOffset(*offset*)[¶](#ApiClient.Synchronization.SetOffset "Link to this definition")  
Sets (known) offset. The offset will be added to the calculated deltaT. By default, it is only used for the OffsetSynchronization.

Parameters:  **offset** (*str*) – The (known) offset as expression

SetOffsetUsed(*used*)[¶](#ApiClient.Synchronization.SetOffsetUsed "Link to this definition")  
Sets whether the known offset should be applied. For the ExpectationSynchronization and EqualnessMatchingSynchronization the known offset will be added to the calculated deltaT. The known offset will always be used by the OffsetSynchronization.

Parameters:  **used** (*boolean*) – True if the offset should be used, else False.

SetTimeLimit(*timeLimit*)[¶](#ApiClient.Synchronization.SetTimeLimit "Link to this definition")  
Sets the time stamp relative to the first time stamp (of the recording group and master recording group) until that the running synchronization will be evaluated. If the time limit is reached, the synchronization will fail.

Parameters:  **timeLimit** (*str*) – The relative time limit as expression

## SwitchDefCase[¶](#switchdefcase "Link to this heading")

*class* SwitchDefCase[¶](#ApiClient.SwitchDefCase "Link to this definition")  
Base classes

- [`TraceStep`](#ApiClient.TraceStep "ApiClient.TraceStep")

- [`TraceStepContainer`](#ApiClient.TraceStepContainer "ApiClient.TraceStepContainer")

Returned by

- [`TraceAnalysisApi.CreateSwitchDefCase`](#ApiClient.TraceAnalysisApi.CreateSwitchDefCase "ApiClient.TraceAnalysisApi.CreateSwitchDefCase")

AddTag(*tag*)[¶](#ApiClient.SwitchDefCase.AddTag "Link to this definition")  
Add a specific tag to this step.

Parameters:  **tag** (*str*) – The tag to be set

AppendTraceStep(*traceStep*)[¶](#ApiClient.SwitchDefCase.AppendTraceStep "Link to this definition")  
Adds a trace step at the end of its children.

Parameters:  **traceStep** ([`TraceStep`](#ApiClient.TraceStep "ApiClient.TraceStep")) – Trace step to be added

Clone()[¶](#ApiClient.SwitchDefCase.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`SwitchDefCase`](#ApiClient.SwitchDefCase "ApiClient.SwitchDefCase")

CreateCaseNode(*insertPosition=None*)[¶](#ApiClient.SwitchDefCase.CreateCaseNode "Link to this definition")  
Creates and returns a newly created case node.

Parameters:  **insertPosition** (*int*) – Specifies the insert position of the new case node. If unspecified or too large the new case node will be inserted before the default node.

Returns:  The specified case node

Return type:  [`CaseDefNode`](#ApiClient.CaseDefNode "ApiClient.CaseDefNode")

GetCaseNode(*index*)[¶](#ApiClient.SwitchDefCase.GetCaseNode "Link to this definition")  
Returns the specified case node.

Parameters:  **index** (*int*) – Specifies the index of the case node to return

Returns:  The specified case node

Return type:  [`CaseDefNode`](#ApiClient.CaseDefNode "ApiClient.CaseDefNode")

GetCaseNodes()[¶](#ApiClient.SwitchDefCase.GetCaseNodes "Link to this definition")  
Returns the list of the case nodes.

Returns:  List of case nodes

Return type:  list[[`CaseDefNode`](#ApiClient.CaseDefNode "ApiClient.CaseDefNode")]

GetDescription()[¶](#ApiClient.SwitchDefCase.GetDescription "Link to this definition")  
Returns an empty text. A SwitchDef does not have a description.

Returns:  The description

Return type:  str

GetLineNo()[¶](#ApiClient.SwitchDefCase.GetLineNo "Link to this definition")  
Returns the trace steps line number within its trace analysis.

Returns:  Line number

Return type:  int

GetName()[¶](#ApiClient.SwitchDefCase.GetName "Link to this definition")  
Returns the name of the trace analysis element.

Returns:  The name

Return type:  str

GetSwitchValue()[¶](#ApiClient.SwitchDefCase.GetSwitchValue "Link to this definition")  
Returns the constant expression examined in the SwitchDef.

Returns:  Constant expression of the SwitchDef

Return type:  str

GetTags()[¶](#ApiClient.SwitchDefCase.GetTags "Link to this definition")  
Returns the tags set for this step.

Returns:  A (sorted) list of tags

Return type:  list[str]

GetTraceSteps(*skipDisabledSteps=False*, *recursive=False*)[¶](#ApiClient.SwitchDefCase.GetTraceSteps "Link to this definition")  
Returns either direct or all children of the trace step.

Parameters:  - **skipDisabledSteps** (*boolean*) – Defines whether disabled trace steps should be excluded, defaults to False.

- **recursive** (*boolean*) – Defines whether children of children are included, defaults to False.

Returns:  The trace steps as flat list.

Return type:  list[[`TraceStep`](#ApiClient.TraceStep "ApiClient.TraceStep")]

GetType()[¶](#ApiClient.SwitchDefCase.GetType "Link to this definition")  
Returns the type (class name) of the trace step, e.g.

> - ‘Episode’
>
> - ‘AnalysisBlock’
>
> - ‘TriggerBlock’
>
> - ‘Calculation’
>
> - ‘TemplateBasedTraceStep’
>
> - ‘TraceAnalysisReference’
>
> - ‘TraceAnalysisReferenceDeprecated’

Returns:  Type (class name) of the trace step

Return type:  str

GetUuid()[¶](#ApiClient.SwitchDefCase.GetUuid "Link to this definition")  
Returns the UUID of the trace step.

Returns:  UUID of the trace step

Return type:  str

InsertTraceStep(*traceStep*, *position*)[¶](#ApiClient.SwitchDefCase.InsertTraceStep "Link to this definition")  
Adds a trace step at a certain line of the trace analysis.

Parameters:  - **traceStep** ([`TraceStep`](#ApiClient.TraceStep "ApiClient.TraceStep")) – Trace step to be added

- **position** (*integer*) – Target index of child beginning with 0

IsContainer()[¶](#ApiClient.SwitchDefCase.IsContainer "Link to this definition")  
Checks whether this trace step can contain trace steps.

Returns:  True if it can contain trace steps, else False

Return type:  boolean

IsDefaultError()[¶](#ApiClient.SwitchDefCase.IsDefaultError "Link to this definition")  
Returns the behavior of the default case. If set to True and the constant expression does not match with any of the expected cases the analysis will result in an ‘ERROR’.

Returns:  Truth value of the current state

Return type:  boolean

IsEnabled()[¶](#ApiClient.SwitchDefCase.IsEnabled "Link to this definition")  
Checks whether the trace step is enabled.

Returns:  True if trace step is enabled, else False

Return type:  boolean

IsOk()[¶](#ApiClient.SwitchDefCase.IsOk "Link to this definition")  
Returns the internal state of correctness of the trace step.

Returns:  True if no problems were found, else False

Return type:  boolean

IsVisible()[¶](#ApiClient.SwitchDefCase.IsVisible "Link to this definition")  
Checks whether the trace step is visible. This depends on the trace step itself or a parent trace step being disabled.

Returns:  True if trace step is visible, else False

Return type:  boolean

RemoveTag(*tag*)[¶](#ApiClient.SwitchDefCase.RemoveTag "Link to this definition")  
Remove a specific tag from this step.

Parameters:  **tag** (*str*) – The tag to be removed

RemoveTraceStep(*traceStep*)[¶](#ApiClient.SwitchDefCase.RemoveTraceStep "Link to this definition")  
Removes the given trace step from the trace analysis.

Parameters:  **traceStep** ([`TraceStep`](#ApiClient.TraceStep "ApiClient.TraceStep")) – Trace step to be removed

SetDefaultError(*defaultError*)[¶](#ApiClient.SwitchDefCase.SetDefaultError "Link to this definition")  
Sets the state of the default case behavior. If set to True and the constant expression does not match with any of the expected cases the analysis will result in an ‘ERROR’.

Parameters:  **defaultError** (*boolean*) – If set to True, enter the default case will result in an error at runtime.

SetDescription(*value*)[¶](#ApiClient.SwitchDefCase.SetDescription "Link to this definition")  
No operation. A SwitchDef block does not have a description.

Parameters:  **value** (*str*) – The new description

SetEnabled(*enable*)[¶](#ApiClient.SwitchDefCase.SetEnabled "Link to this definition")  
Enables or disables the trace step (this also affects child trace steps).

Parameters:  **enable** (*boolean*) – If True, enables the trace step, if False, disables the trace step

SetName(*name*)[¶](#ApiClient.SwitchDefCase.SetName "Link to this definition")  
No operation. The name of a SwitchDef cannot be changed.

Parameters:  **name** (*str*) – The new name

SetSwitchValue(*switchValue*)[¶](#ApiClient.SwitchDefCase.SetSwitchValue "Link to this definition")  
Sets the constant expression examined in the SwitchDef.

Parameters:  **switchValue** (*str*) – Constant expression of the SwitchDef

SetTags(*tags*)[¶](#ApiClient.SwitchDefCase.SetTags "Link to this definition")  
Set the list of tags for this step. The list of tags will be sorted and stored.

Parameters:  **tags** (*list[str]*) – The list of tags

## CaseDefNode[¶](#casedefnode "Link to this heading")

*class* CaseDefNode[¶](#ApiClient.CaseDefNode "Link to this definition")  
Base classes

- [`TraceStep`](#ApiClient.TraceStep "ApiClient.TraceStep")

- [`TraceStepContainer`](#ApiClient.TraceStepContainer "ApiClient.TraceStepContainer")

Returned by

- [`SwitchDefCase.CreateCaseNode`](#ApiClient.SwitchDefCase.CreateCaseNode "ApiClient.SwitchDefCase.CreateCaseNode")

- [`SwitchDefCase.GetCaseNode`](#ApiClient.SwitchDefCase.GetCaseNode "ApiClient.SwitchDefCase.GetCaseNode")

- [`SwitchDefCase.GetCaseNodes`](#ApiClient.SwitchDefCase.GetCaseNodes "ApiClient.SwitchDefCase.GetCaseNodes")

AddTag(*tag*)[¶](#ApiClient.CaseDefNode.AddTag "Link to this definition")  
Add a specific tag to this step.

Parameters:  **tag** (*str*) – The tag to be set

AppendTraceStep(*traceStep*)[¶](#ApiClient.CaseDefNode.AppendTraceStep "Link to this definition")  
Adds a trace step at the end of its children.

Parameters:  **traceStep** ([`TraceStep`](#ApiClient.TraceStep "ApiClient.TraceStep")) – Trace step to be added

Clone()[¶](#ApiClient.CaseDefNode.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`CaseDefNode`](#ApiClient.CaseDefNode "ApiClient.CaseDefNode")

GetCaseValue()[¶](#ApiClient.CaseDefNode.GetCaseValue "Link to this definition")  
Returns the constant expression used in the case node.

Returns:  Constant expression of the case node

Return type:  str

GetDescription()[¶](#ApiClient.CaseDefNode.GetDescription "Link to this definition")  
Not available. A case node does not have a description.

Returns:  The description

Return type:  str

GetLineNo()[¶](#ApiClient.CaseDefNode.GetLineNo "Link to this definition")  
Returns the trace steps line number within its trace analysis.

Returns:  Line number

Return type:  int

GetName()[¶](#ApiClient.CaseDefNode.GetName "Link to this definition")  
Returns the name of the trace analysis element.

Returns:  The name

Return type:  str

GetTags()[¶](#ApiClient.CaseDefNode.GetTags "Link to this definition")  
Returns the tags set for this step.

Returns:  A (sorted) list of tags

Return type:  list[str]

GetTraceSteps(*skipDisabledSteps=False*, *recursive=False*)[¶](#ApiClient.CaseDefNode.GetTraceSteps "Link to this definition")  
Returns either direct or all children of the trace step.

Parameters:  - **skipDisabledSteps** (*boolean*) – Defines whether disabled trace steps should be excluded, defaults to False.

- **recursive** (*boolean*) – Defines whether children of children are included, defaults to False.

Returns:  The trace steps as flat list.

Return type:  list[[`TraceStep`](#ApiClient.TraceStep "ApiClient.TraceStep")]

GetType()[¶](#ApiClient.CaseDefNode.GetType "Link to this definition")  
Returns the type (class name) of the trace step, e.g.

> - ‘Episode’
>
> - ‘AnalysisBlock’
>
> - ‘TriggerBlock’
>
> - ‘Calculation’
>
> - ‘TemplateBasedTraceStep’
>
> - ‘TraceAnalysisReference’
>
> - ‘TraceAnalysisReferenceDeprecated’

Returns:  Type (class name) of the trace step

Return type:  str

GetUuid()[¶](#ApiClient.CaseDefNode.GetUuid "Link to this definition")  
Returns the UUID of the trace step.

Returns:  UUID of the trace step

Return type:  str

InsertTraceStep(*traceStep*, *position*)[¶](#ApiClient.CaseDefNode.InsertTraceStep "Link to this definition")  
Adds a trace step at a certain line of the trace analysis.

Parameters:  - **traceStep** ([`TraceStep`](#ApiClient.TraceStep "ApiClient.TraceStep")) – Trace step to be added

- **position** (*integer*) – Target index of child beginning with 0

IsContainer()[¶](#ApiClient.CaseDefNode.IsContainer "Link to this definition")  
Checks whether this trace step can contain trace steps.

Returns:  True if it can contain trace steps, else False

Return type:  boolean

IsDefaultNode()[¶](#ApiClient.CaseDefNode.IsDefaultNode "Link to this definition")  
Returns True if this is the default node.

Returns:  If default node

Return type:  bool

IsEnabled()[¶](#ApiClient.CaseDefNode.IsEnabled "Link to this definition")  
Checks whether the trace step is enabled.

Returns:  True if trace step is enabled, else False

Return type:  boolean

IsOk()[¶](#ApiClient.CaseDefNode.IsOk "Link to this definition")  
Returns the internal state of correctness of the trace step.

Returns:  True if no problems were found, else False

Return type:  boolean

IsVisible()[¶](#ApiClient.CaseDefNode.IsVisible "Link to this definition")  
Checks whether the trace step is visible. This depends on the trace step itself or a parent trace step being disabled.

Returns:  True if trace step is visible, else False

Return type:  boolean

RemoveTag(*tag*)[¶](#ApiClient.CaseDefNode.RemoveTag "Link to this definition")  
Remove a specific tag from this step.

Parameters:  **tag** (*str*) – The tag to be removed

RemoveTraceStep(*traceStep*)[¶](#ApiClient.CaseDefNode.RemoveTraceStep "Link to this definition")  
Removes the given trace step from the trace analysis.

Parameters:  **traceStep** ([`TraceStep`](#ApiClient.TraceStep "ApiClient.TraceStep")) – Trace step to be removed

SetCaseValue(*caseValue*)[¶](#ApiClient.CaseDefNode.SetCaseValue "Link to this definition")  
Sets the constant expression used in the case node.

Parameters:  **caseValue** (*str*) – Constant expression of the caseDefNode block

SetDescription(*value*)[¶](#ApiClient.CaseDefNode.SetDescription "Link to this definition")  
No operation. A case node does not have a description.

Parameters:  **value** (*str*) – The new description

SetEnabled(*enable*)[¶](#ApiClient.CaseDefNode.SetEnabled "Link to this definition")  
No operation. A case node is automatically enabled or disabled by its case value and cannot be enabled or disabled by the user.

Parameters:  **enable** (*boolean*) – If True, enables the trace step, if False, disables the trace step

SetName(*name*)[¶](#ApiClient.CaseDefNode.SetName "Link to this definition")  
No operation. The name of a case node cannot be changed.

Parameters:  **name** (*str*) – The new name

SetTags(*tags*)[¶](#ApiClient.CaseDefNode.SetTags "Link to this definition")  
Set the list of tags for this step. The list of tags will be sorted and stored.

Parameters:  **tags** (*list[str]*) – The list of tags

## TriggerBlock[¶](#triggerblock "Link to this heading")

*class* TriggerBlock[¶](#ApiClient.TriggerBlock "Link to this definition")  
Base classes

- [`TraceStep`](#ApiClient.TraceStep "ApiClient.TraceStep")

- [`TraceStepContainer`](#ApiClient.TraceStepContainer "ApiClient.TraceStepContainer")

Returned by

- [`TraceAnalysisApi.CreateTriggerBlock`](#ApiClient.TraceAnalysisApi.CreateTriggerBlock "ApiClient.TraceAnalysisApi.CreateTriggerBlock")

MODE_STARTTRIGGER_TO_NEXT_STOPTRIGGER[¶](#ApiClient.TriggerBlock.MODE_STARTTRIGGER_TO_NEXT_STOPTRIGGER "Link to this definition")  
Returns the constant used to specify the expectation mode ‘from start trigger until next time stop trigger is fulfilled’.

Returns:  The constant

Return type:  str

MODE_STARTTRIGGER_WHILE_NOT_STOPTRIGGER[¶](#ApiClient.TriggerBlock.MODE_STARTTRIGGER_WHILE_NOT_STOPTRIGGER "Link to this definition")  
Returns the constant used to specify the expectation mode ‘from start trigger as long as stop trigger is not fulfilled’.

Returns:  The constant

Return type:  str

MODE_STARTTRIGGER_WITH_TIME_OFFSETS[¶](#ApiClient.TriggerBlock.MODE_STARTTRIGGER_WITH_TIME_OFFSETS "Link to this definition")  
Returns the constant used to specify the expectation mode ‘with time offset if start trigger is fulfilled’.

Returns:  The constant

Return type:  str

MODE_WHILE_STARTTRIGGER[¶](#ApiClient.TriggerBlock.MODE_WHILE_STARTTRIGGER "Link to this definition")  
Returns the constant used to specify the expectation mode ‘as long as start trigger is fulfilled’.

Returns:  The constant

Return type:  str

AddTag(*tag*)[¶](#ApiClient.TriggerBlock.AddTag "Link to this definition")  
Add a specific tag to this step.

Parameters:  **tag** (*str*) – The tag to be set

AppendTraceStep(*traceStep*)[¶](#ApiClient.TriggerBlock.AppendTraceStep "Link to this definition")  
Adds a trace step at the end of its children.

Parameters:  **traceStep** ([`TraceStep`](#ApiClient.TraceStep "ApiClient.TraceStep")) – Trace step to be added

Clone()[¶](#ApiClient.TriggerBlock.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`TriggerBlock`](#ApiClient.TriggerBlock "ApiClient.TriggerBlock")

GetDescription()[¶](#ApiClient.TriggerBlock.GetDescription "Link to this definition")  
Returns the description of the trace analysis element.

Returns:  The description

Return type:  str

GetEndOfTraceAsStopTrigger()[¶](#ApiClient.TriggerBlock.GetEndOfTraceAsStopTrigger "Link to this definition")  
Returns whether the end of trace shall be handled as a stop trigger.

Returns:  The setting for the treatment of unfinished ranges at the end of trace

Return type:  bool

GetIgnoreFirstMode()[¶](#ApiClient.TriggerBlock.GetIgnoreFirstMode "Link to this definition")  
Returns the ignore first mode.

Returns:  The mode: ‘manual’, ‘firstsample’ or ‘disabled’

Return type:  str

GetIgnoreFirstTime()[¶](#ApiClient.TriggerBlock.GetIgnoreFirstTime "Link to this definition")  
Returns the ignore first time if set. Otherwise None is returned.

Returns:  The expression value (only for manual mode)

Return type:  str

GetIgnoreLastMode()[¶](#ApiClient.TriggerBlock.GetIgnoreLastMode "Link to this definition")  
Returns the ignore last mode.

Returns:  The mode: ‘manual’ or ‘disabled’

Return type:  str

GetIgnoreLastTime()[¶](#ApiClient.TriggerBlock.GetIgnoreLastTime "Link to this definition")  
Returns the ignore last time if set. Otherwise None is returned.

Returns:  The expression value (only for manual mode)

Return type:  str

GetLineNo()[¶](#ApiClient.TriggerBlock.GetLineNo "Link to this definition")  
Returns the trace steps line number within its trace analysis.

Returns:  Line number

Return type:  int

GetName()[¶](#ApiClient.TriggerBlock.GetName "Link to this definition")  
Returns the name of the trace analysis element.

Returns:  The name

Return type:  str

GetReportEntryLimit()[¶](#ApiClient.TriggerBlock.GetReportEntryLimit "Link to this definition")  
Returns the maximal number of entries per verdict and child the reporting shall be limited to. A return value of None indicates that no limitation is in place.

Returns:  The maximal number of entries per verdict and child as expression string or None

Return type:  str

GetReportFilterCondition()[¶](#ApiClient.TriggerBlock.GetReportFilterCondition "Link to this definition")  
Returns the condition that must be matched for the trigger range to be reported. Possible values are: - ‘NONE’ (meaning no filtering for verdict types) - ‘SUCCESS’ (meaning SUCCESS or worse) - ‘INCONCLUSIVE’ (meaning INCONCLUSIVE or worse) - ‘FAILED’ (meaning FAILED or worse) - ‘ERROR’ (meaning ERROR)

Returns:  The report condition

Return type:  str

GetReportIgnoredRanges()[¶](#ApiClient.TriggerBlock.GetReportIgnoredRanges "Link to this definition")  
Returns whether ranges without a sample after consideration of the ignore times should be reported.

Returns:  The setting whether ignored ranges will be reported

Return type:  bool

GetReportOmittedStartTrigger()[¶](#ApiClient.TriggerBlock.GetReportOmittedStartTrigger "Link to this definition")  
Returns whether omitted start triggers will be reported.

Returns:  The setting whether omitted start triggers will be reported

Return type:  bool

GetResultNoMatch()[¶](#ApiClient.TriggerBlock.GetResultNoMatch "Link to this definition")  
Returns the verdict of a trigger block that does not open any trigger range.

Returns:  The verdict of a trigger block without a trigger range

Return type:  str

GetResultTruncatedRange()[¶](#ApiClient.TriggerBlock.GetResultTruncatedRange "Link to this definition")  
Returns the blanket verdict of a truncated trigger range or None if truncated trigger ranges are evaluated normally.

Returns:  The verdict of a truncated trigger range

Return type:  str

GetStartOffset()[¶](#ApiClient.TriggerBlock.GetStartOffset "Link to this definition")  
Returns the start offset expression.

Returns:  The start offset

Return type:  str

GetStartTrigger()[¶](#ApiClient.TriggerBlock.GetStartTrigger "Link to this definition")  
Returns the start trigger expression.

Returns:  The start trigger expression

Return type:  str

GetStopOffset()[¶](#ApiClient.TriggerBlock.GetStopOffset "Link to this definition")  
Returns the stop offset expression.

Returns:  The stop offset

Return type:  str

GetStopTrigger()[¶](#ApiClient.TriggerBlock.GetStopTrigger "Link to this definition")  
Returns the stop trigger expression or None if no stop trigger is defined.

Returns:  The stop trigger expression

Return type:  str

GetTags()[¶](#ApiClient.TriggerBlock.GetTags "Link to this definition")  
Returns the tags set for this step.

Returns:  A (sorted) list of tags

Return type:  list[str]

GetTraceSteps(*skipDisabledSteps=False*, *recursive=False*)[¶](#ApiClient.TriggerBlock.GetTraceSteps "Link to this definition")  
Returns either direct or all children of the trace step.

Parameters:  - **skipDisabledSteps** (*boolean*) – Defines whether disabled trace steps should be excluded, defaults to False.

- **recursive** (*boolean*) – Defines whether children of children are included, defaults to False.

Returns:  The trace steps as flat list.

Return type:  list[[`TraceStep`](#ApiClient.TraceStep "ApiClient.TraceStep")]

GetTriggerMode()[¶](#ApiClient.TriggerBlock.GetTriggerMode "Link to this definition")  
Returns the trigger mode.

Returns:  The trigger mode

Return type:  str

GetTriggerOnce()[¶](#ApiClient.TriggerBlock.GetTriggerOnce "Link to this definition")  
Returns whether the trigger block should trigger only once.

Returns:  The setting for restricting the number of trigger ranges to one

Return type:  bool

GetType()[¶](#ApiClient.TriggerBlock.GetType "Link to this definition")  
Returns the type (class name) of the trace step, e.g.

> - ‘Episode’
>
> - ‘AnalysisBlock’
>
> - ‘TriggerBlock’
>
> - ‘Calculation’
>
> - ‘TemplateBasedTraceStep’
>
> - ‘TraceAnalysisReference’
>
> - ‘TraceAnalysisReferenceDeprecated’

Returns:  Type (class name) of the trace step

Return type:  str

GetUuid()[¶](#ApiClient.TriggerBlock.GetUuid "Link to this definition")  
Returns the UUID of the trace step.

Returns:  UUID of the trace step

Return type:  str

InsertTraceStep(*traceStep*, *position*)[¶](#ApiClient.TriggerBlock.InsertTraceStep "Link to this definition")  
Adds a trace step at a certain line of the trace analysis.

Parameters:  - **traceStep** ([`TraceStep`](#ApiClient.TraceStep "ApiClient.TraceStep")) – Trace step to be added

- **position** (*integer*) – Target index of child beginning with 0

IsContainer()[¶](#ApiClient.TriggerBlock.IsContainer "Link to this definition")  
Checks whether this trace step can contain trace steps.

Returns:  True if it can contain trace steps, else False

Return type:  boolean

IsEnabled()[¶](#ApiClient.TriggerBlock.IsEnabled "Link to this definition")  
Checks whether the trace step is enabled.

Returns:  True if trace step is enabled, else False

Return type:  boolean

IsOk()[¶](#ApiClient.TriggerBlock.IsOk "Link to this definition")  
Returns the internal state of correctness of the trace step.

Returns:  True if no problems were found, else False

Return type:  boolean

IsVisible()[¶](#ApiClient.TriggerBlock.IsVisible "Link to this definition")  
Checks whether the trace step is visible. This depends on the trace step itself or a parent trace step being disabled.

Returns:  True if trace step is visible, else False

Return type:  boolean

RemoveTag(*tag*)[¶](#ApiClient.TriggerBlock.RemoveTag "Link to this definition")  
Remove a specific tag from this step.

Parameters:  **tag** (*str*) – The tag to be removed

RemoveTraceStep(*traceStep*)[¶](#ApiClient.TriggerBlock.RemoveTraceStep "Link to this definition")  
Removes the given trace step from the trace analysis.

Parameters:  **traceStep** ([`TraceStep`](#ApiClient.TraceStep "ApiClient.TraceStep")) – Trace step to be removed

SetDescription(*value*)[¶](#ApiClient.TriggerBlock.SetDescription "Link to this definition")  
Sets the description of the trace analysis element.

Parameters:  **value** (*str*) – The new description

SetEnabled(*enable*)[¶](#ApiClient.TriggerBlock.SetEnabled "Link to this definition")  
Enables or disables the trace step (this also affects child trace steps).

Parameters:  **enable** (*boolean*) – If True, enables the trace step, if False, disables the trace step

SetEndOfTraceAsStopTrigger(*mode*)[¶](#ApiClient.TriggerBlock.SetEndOfTraceAsStopTrigger "Link to this definition")  
Sets whether the end of trace shall be handled as a stop trigger.

Parameters:  **mode** (*bool*) – If True, unfinished ranges will be completed as if an ordinary stop trigger occurred. Otherwise such ranges will be rated INCONCLUSIVE.

SetIgnoreFirst(*mode*, *ignoreTime=None*)[¶](#ApiClient.TriggerBlock.SetIgnoreFirst "Link to this definition")  
Sets whether at the start of each trigger range a quantity of samples should be excluded. Possible values for mode are: ‘disabled’, ‘manual’ or ‘firstsample’. In the latter mode the parameter ignoreTime will have no impact.

Parameters:  - **mode** (*str*) – The mode for ignore first

- **ignoreTime** (*str*) – The expression value for the ignored time (only for manual mode)

SetIgnoreLast(*mode*, *ignoreTime=None*)[¶](#ApiClient.TriggerBlock.SetIgnoreLast "Link to this definition")  
Sets whether at the end of each trigger range a certain time span parameterized by ignoreTime should be excluded. Possible values for mode are: ‘disabled’ or ‘manual’.

Parameters:  - **mode** (*str*) – The mode for ignore last

- **ignoreTime** (*str*) – The expression value for the ignored time (only for manual mode)

SetName(*value*)[¶](#ApiClient.TriggerBlock.SetName "Link to this definition")  
Sets the name of the trace analysis element.

Parameters:  **value** (*str*) – The new name

SetReportEntryLimit(*maxEntryCount*)[¶](#ApiClient.TriggerBlock.SetReportEntryLimit "Link to this definition")  
Sets the maximal number of entries per verdict and child the reporting shall be limited to. A value of None specifies that no limit shall be applied.

Parameters:  **maxEntryCount** (*str*) – The maximal number of entries per verdict as expression or None

SetReportFilterCondition(*condition*)[¶](#ApiClient.TriggerBlock.SetReportFilterCondition "Link to this definition")  
Sets the condition that must be matched for the trigger range to be reported. Possible values are: - ‘NONE’ (meaning no filtering for verdict types) - ‘SUCCESS’ (meaning SUCCESS or worse) - ‘INCONCLUSIVE’ (meaning INCONCLUSIVE or worse) - ‘FAILED’ (meaning FAILED or worse) - ‘ERROR’ (meaning ERROR)

Parameters:  **condition** (*str*) – The report condition

SetReportIgnoredRanges(*reportRanges*)[¶](#ApiClient.TriggerBlock.SetReportIgnoredRanges "Link to this definition")  
Sets whether ranges without a sample after consideration of the ignore times should be reported.

Parameters:  **reportRanges** (*bool*) – If true, a range whose samples are completely left out due to the ignore times will be reported as NONE range. Otherwise it will not be reported.

SetReportOmittedStartTrigger(*reportTrigger*)[¶](#ApiClient.TriggerBlock.SetReportOmittedStartTrigger "Link to this definition")  
Sets whether omitted start triggers will be reported.

Parameters:  **reportTrigger** (*bool*) – If true, for every omitted start trigger of the mode ‘start trigger while not stop trigger’ a spot will be generated.

SetResultNoMatch(*result*)[¶](#ApiClient.TriggerBlock.SetResultNoMatch "Link to this definition")  
Sets the verdict of a trigger block that does not open any trigger range. Possible values: ‘NONE’, ‘SUCCESS’, ‘INCONCLUSIVE’, ‘FAILED’ or ‘ERROR’.

Parameters:  **result** (*str*) – The verdict of a trigger block without a trigger range

SetResultTruncatedRange(*result*)[¶](#ApiClient.TriggerBlock.SetResultTruncatedRange "Link to this definition")  
Sets the blanket verdict of a truncated trigger range. Possible values of verdicts: ‘NONE’, ‘SUCCESS’, ‘INCONCLUSIVE’, ‘FAILED’ or ‘ERROR’.

Set to None if truncated trigger ranges shall be evaluated normally

Parameters:  **result** (*str*) – The verdict of a truncated trigger range

SetStartOffset(*startOffset*)[¶](#ApiClient.TriggerBlock.SetStartOffset "Link to this definition")  
Sets the start offset expression.

Parameters:  **startOffset** (*str*) – The start offset

SetStartTrigger(*startTrigger*)[¶](#ApiClient.TriggerBlock.SetStartTrigger "Link to this definition")  
Sets the start trigger expression.

Parameters:  **startTrigger** (*str*) – The start trigger expression

SetStopOffset(*stopOffset*)[¶](#ApiClient.TriggerBlock.SetStopOffset "Link to this definition")  
Sets the stop offset expression.

Parameters:  **stopOffset** (*str*) – The start offset

SetStopTrigger(*stopTrigger*)[¶](#ApiClient.TriggerBlock.SetStopTrigger "Link to this definition")  
Sets the stop trigger expression.

Parameters:  **stopTrigger** (*str*) – The stop trigger expression

SetTags(*tags*)[¶](#ApiClient.TriggerBlock.SetTags "Link to this definition")  
Set the list of tags for this step. The list of tags will be sorted and stored.

Parameters:  **tags** (*list[str]*) – The list of tags

SetTriggerMode(*triggerMode*)[¶](#ApiClient.TriggerBlock.SetTriggerMode "Link to this definition")  
Sets the trigger mode. Possible values for mode can be obtained by either of the constants:

> - [`TriggerBlock.MODE_WHILE_STARTTRIGGER`](#ApiClient.TriggerBlock.MODE_WHILE_STARTTRIGGER "ApiClient.TriggerBlock.MODE_WHILE_STARTTRIGGER")
>
> - [`TriggerBlock.MODE_STARTTRIGGER_WHILE_NOT_STOPTRIGGER`](#ApiClient.TriggerBlock.MODE_STARTTRIGGER_WHILE_NOT_STOPTRIGGER "ApiClient.TriggerBlock.MODE_STARTTRIGGER_WHILE_NOT_STOPTRIGGER")
>
> - [`TriggerBlock.MODE_STARTTRIGGER_TO_NEXT_STOPTRIGGER`](#ApiClient.TriggerBlock.MODE_STARTTRIGGER_TO_NEXT_STOPTRIGGER "ApiClient.TriggerBlock.MODE_STARTTRIGGER_TO_NEXT_STOPTRIGGER")
>
> - [`TriggerBlock.MODE_STARTTRIGGER_WITH_TIME_OFFSETS`](#ApiClient.TriggerBlock.MODE_STARTTRIGGER_WITH_TIME_OFFSETS "ApiClient.TriggerBlock.MODE_STARTTRIGGER_WITH_TIME_OFFSETS")

Parameters:  **triggerMode** (*str*) – The stop trigger expression

SetTriggerOnce(*triggerOnce*)[¶](#ApiClient.TriggerBlock.SetTriggerOnce "Link to this definition")  
Sets whether the trigger block should trigger once or repeatedly.

Parameters:  **triggerOnce** (*bool*) – If true, only the very first trigger range that is found will be analyzed. Further ranges will be ignored.

## Plot[¶](#plot "Link to this heading")

*class* Plot[¶](#ApiClient.Plot "Link to this definition")  
Base class

[`TraceStep`](#ApiClient.TraceStep "ApiClient.TraceStep")

Returned by

- [`TraceAnalysisApi.CreatePlot`](#ApiClient.TraceAnalysisApi.CreatePlot "ApiClient.TraceAnalysisApi.CreatePlot")

AddTag(*tag*)[¶](#ApiClient.Plot.AddTag "Link to this definition")  
Add a specific tag to this step.

Parameters:  **tag** (*str*) – The tag to be set

ApplySignalsFromParent()[¶](#ApiClient.Plot.ApplySignalsFromParent "Link to this definition")  
Convenience method to plot all active signals of the parent. All generic signals are used if the parent has no special signal management.

Note:  
Signals that are already defined will be overwritten.

Clone()[¶](#ApiClient.Plot.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`Plot`](#ApiClient.Plot "ApiClient.Plot")

GetDescription()[¶](#ApiClient.Plot.GetDescription "Link to this definition")  
Returns the description of the trace analysis element.

Returns:  The description

Return type:  str

GetDetailsConfig()[¶](#ApiClient.Plot.GetDetailsConfig "Link to this definition")  
Returns the sub configuration for detail plots, i.e. those around spots and ranges.

Returns:  The sub configuration for detail plots

Return type:  [`PlotSubConfig`](#ApiClient.PlotSubConfig "ApiClient.PlotSubConfig")

GetImageSize()[¶](#ApiClient.Plot.GetImageSize "Link to this definition")  
Returns the minimum size of the plot in pixels.

The default sizes are 800x600 (large), 640x480 (medium) and 320x240 (small).

Returns:  list(width, height)

Return type:  list[int]

GetLegendLocation()[¶](#ApiClient.Plot.GetLegendLocation "Link to this definition")  
Returns the location of the legend.

Returns:  Number between 0 and 10. 12 means legend is hidden.

Return type:  int

GetLineNo()[¶](#ApiClient.Plot.GetLineNo "Link to this definition")  
Returns the trace steps line number within its trace analysis.

Returns:  Line number

Return type:  int

GetName()[¶](#ApiClient.Plot.GetName "Link to this definition")  
Returns the name of the trace analysis element.

Returns:  The name

Return type:  str

GetOverviewConfig()[¶](#ApiClient.Plot.GetOverviewConfig "Link to this definition")  
Returns the sub configuration for the overview plot.

Returns:  The sub configuration for the overview plot

Return type:  [`PlotSubConfig`](#ApiClient.PlotSubConfig "ApiClient.PlotSubConfig")

GetPlotSignals()[¶](#ApiClient.Plot.GetPlotSignals "Link to this definition")  
Returns a merged list of all signals of the sub plots.

Returns:  The signals of the plot

Return type:  list[[`PlotSignalBase`](#ApiClient.PlotSignalBase "ApiClient.PlotSignalBase")]

GetShowYLabels()[¶](#ApiClient.Plot.GetShowYLabels "Link to this definition")  
Returns whether y labels are shown. There are three different values possible. For the automatic mode (value 2), an y label will be hidden if there is a legend, there is only one y axis for a sub plot, and there are multiple signals assigned to this axis.

Returns:  0 if y labels are always hidden, 1 if y labels are always shown, 2 if the visibility is automatically determined for each axis

Return type:  int

GetSignalNameType()[¶](#ApiClient.Plot.GetSignalNameType "Link to this definition")  
Returns which kind of name for the signal names is shown in the plot.

Returns:  ‘tracestep’, ‘generic’, ‘mapping’, ‘mappingtarget’ or ‘file’

Return type:  str

GetSubPlots()[¶](#ApiClient.Plot.GetSubPlots "Link to this definition")  
Returns a list of all sub plots. The list of sub plots can’t be changed. The first and third one are normal sub plots of type “common”. The second plot can be of type “common” or “separate”. If the type is “separate”, for each signal of this sub plot there will be a smaller sub plot.

Returns:  The list of all sub plots

Return type:  list[[`PlotSubPlot`](#ApiClient.PlotSubPlot "ApiClient.PlotSubPlot")]

GetTags()[¶](#ApiClient.Plot.GetTags "Link to this definition")  
Returns the tags set for this step.

Returns:  A (sorted) list of tags

Return type:  list[str]

GetTriggerRangeConfig()[¶](#ApiClient.Plot.GetTriggerRangeConfig "Link to this definition")  
Returns the sub configuration for the trigger range plots.

Returns:  The sub configuration for the trigger range plots

Return type:  [`PlotSubConfig`](#ApiClient.PlotSubConfig "ApiClient.PlotSubConfig")

GetType()[¶](#ApiClient.Plot.GetType "Link to this definition")  
Returns the type (class name) of the trace step, e.g.

> - ‘Episode’
>
> - ‘AnalysisBlock’
>
> - ‘TriggerBlock’
>
> - ‘Calculation’
>
> - ‘TemplateBasedTraceStep’
>
> - ‘TraceAnalysisReference’
>
> - ‘TraceAnalysisReferenceDeprecated’

Returns:  Type (class name) of the trace step

Return type:  str

GetUuid()[¶](#ApiClient.Plot.GetUuid "Link to this definition")  
Returns the UUID of the trace step.

Returns:  UUID of the trace step

Return type:  str

GetXLabel()[¶](#ApiClient.Plot.GetXLabel "Link to this definition")  
Returns the label for the x-axis.

Returns:  The label for the x-axis.

Return type:  str

IsContainer()[¶](#ApiClient.Plot.IsContainer "Link to this definition")  
Checks whether this trace step can contain trace steps.

Returns:  True if it can contain trace steps, else False

Return type:  boolean

IsEnabled()[¶](#ApiClient.Plot.IsEnabled "Link to this definition")  
Checks whether the trace step is enabled.

Returns:  True if trace step is enabled, else False

Return type:  boolean

IsOk()[¶](#ApiClient.Plot.IsOk "Link to this definition")  
Returns the internal state of correctness of the trace step.

Returns:  True if no problems were found, else False

Return type:  boolean

IsShowUnits()[¶](#ApiClient.Plot.IsShowUnits "Link to this definition")  
Returns whether the units of the signals are shown in the legend.

Returns:  True if the units are shown in the legend.

Return type:  bool

IsVisible()[¶](#ApiClient.Plot.IsVisible "Link to this definition")  
Checks whether the trace step is visible. This depends on the trace step itself or a parent trace step being disabled.

Returns:  True if trace step is visible, else False

Return type:  boolean

IsXGrid()[¶](#ApiClient.Plot.IsXGrid "Link to this definition")  
Returns whether vertical grid lines are visible.

Returns:  True if visible, else False

Return type:  boolean

RemoveTag(*tag*)[¶](#ApiClient.Plot.RemoveTag "Link to this definition")  
Remove a specific tag from this step.

Parameters:  **tag** (*str*) – The tag to be removed

SetDescription(*value*)[¶](#ApiClient.Plot.SetDescription "Link to this definition")  
Sets the description of the trace analysis element.

Parameters:  **value** (*str*) – The new description

SetEnabled(*enable*)[¶](#ApiClient.Plot.SetEnabled "Link to this definition")  
Enables or disables the trace step (this also affects child trace steps).

Parameters:  **enable** (*boolean*) – If True, enables the trace step, if False, disables the trace step

SetImageSize(*width*, *height*)[¶](#ApiClient.Plot.SetImageSize "Link to this definition")  
Sets the minimum size of the plot in pixels.

The default sizes are 800x600 (large), 640x480 (medium) and 320x240 (small).

Parameters:  - **width** (*int*) – The new width

- **height** (*int*) – The new height

SetLegendLocation(*location*)[¶](#ApiClient.Plot.SetLegendLocation "Link to this definition")  
Sets the location where the legend should be placed in the plot.

Parameters:  **location** (*int*) – Number between 0 and 11, 12 to hide legend

Raises:  
**ValueError** – If location is not a valid parameter

SetName(*value*)[¶](#ApiClient.Plot.SetName "Link to this definition")  
Sets the name of the trace analysis element.

Parameters:  **value** (*str*) – The new name

SetShowUnits(*show*)[¶](#ApiClient.Plot.SetShowUnits "Link to this definition")  
Sets whether the units of the signals will be shown in the legend.

Parameters:  **show** (*bool*) – True if the units should be shown in the legend.

SetShowYLabels(*showYLabels*)[¶](#ApiClient.Plot.SetShowYLabels "Link to this definition")  
Sets if y labels are shown.

Parameters:  **showYLabels** (*int*) – 0 if y labels are always hidden, 1 if y labels are always shown, 2 if the visibility is automatically determined for each axis

Raises:  
**ValueError** – If showYLabels is not a valid parameter

SetSignalNameType(*signalNameType*)[¶](#ApiClient.Plot.SetSignalNameType "Link to this definition")  
Sets which kind of names for the signals are shown in the plot.

Parameters:  **signalNameType** (*str*) – ‘tracestep’, ‘generic’, ‘mapping’, ‘mappingTarget’ or ‘file’ - ‘tracestep’: name of the signal in the trace step template - ‘generic’: name of the generic signal - ‘mapping’: name of the signal in the mapping view - ‘mappingtarget’: name of mapping target of the signal - ‘file’: name of the signal in the recording file

SetTags(*tags*)[¶](#ApiClient.Plot.SetTags "Link to this definition")  
Set the list of tags for this step. The list of tags will be sorted and stored.

Parameters:  **tags** (*list[str]*) – The list of tags

SetXGrid(*grid*)[¶](#ApiClient.Plot.SetXGrid "Link to this definition")  
Sets whether vertical grid lines are visible.

Parameters:  **grid** (*boolean*) – True to set visible, else False.

SetXLabel(*label*)[¶](#ApiClient.Plot.SetXLabel "Link to this definition")  
Sets the label for the x-axis.

Parameters:  **label** (*str*) – The new label for the x-axis.

GetShowUnits()[¶](#ApiClient.Plot.GetShowUnits "Link to this definition")  
Returns whether the units of the signals are shown in the legend.

Returns:  True if the units are shown in the legend.

Return type:  bool

Deprecated since version 2021.2: Please use `IsShowUnits` instead.

GetXGrid()[¶](#ApiClient.Plot.GetXGrid "Link to this definition")  
Returns whether vertical grid lines are visible.

Returns:  True if visible, else False

Return type:  boolean

Deprecated since version 2021.2: Please use `IsXGrid` instead.

## PlotSubConfig[¶](#plotsubconfig "Link to this heading")

*class* PlotSubConfig[¶](#ApiClient.PlotSubConfig "Link to this definition")  
Returned by

- [`Plot.GetDetailsConfig`](#ApiClient.Plot.GetDetailsConfig "ApiClient.Plot.GetDetailsConfig")

- [`Plot.GetOverviewConfig`](#ApiClient.Plot.GetOverviewConfig "ApiClient.Plot.GetOverviewConfig")

- [`Plot.GetTriggerRangeConfig`](#ApiClient.Plot.GetTriggerRangeConfig "ApiClient.Plot.GetTriggerRangeConfig")

Clone()[¶](#ApiClient.PlotSubConfig.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`PlotSubConfig`](#ApiClient.PlotSubConfig "ApiClient.PlotSubConfig")

GetCondition()[¶](#ApiClient.PlotSubConfig.GetCondition "Link to this definition")  
Returns the condition that must be matched to create a plot. Possible return values are ‘NONE’, ‘SUCCESS’, ‘INCONCLUSIVE’, ‘FAILED’, ‘NEVER’. For plot creation the verdict of the plot’s parent must be equal to or worse than this setting. For instance ‘NONE’ means that the plot is always created whereas the setting ‘FAILED’ causes its creation only if the plot’s parent runs FAILED or ERROR.

Returns:  The plot condition

Return type:  str

GetExpandXLimitsLeft()[¶](#ApiClient.PlotSubConfig.GetExpandXLimitsLeft "Link to this definition")  
Returns the expand value of the left limit as expression. The expand value will be added to automatically determined view limits of the plot.

Returns:  The expression for the expand value of the left limit

Return type:  str

GetExpandXLimitsRight()[¶](#ApiClient.PlotSubConfig.GetExpandXLimitsRight "Link to this definition")  
Returns the expand value of the right limit as expression. The expand value will be added to automatically determined view limits of the plot.

Returns:  The expression for expand value of the right limit

Return type:  str

GetMaxNumberPlots()[¶](#ApiClient.PlotSubConfig.GetMaxNumberPlots "Link to this definition")  
Returns the maximum number of plots to be created. This number is counted for the entire execution so trigger ranges will not reset the count.

Returns:  The maximum number of plots as expression

Return type:  str

SetCondition(*condition*)[¶](#ApiClient.PlotSubConfig.SetCondition "Link to this definition")  
Sets the condition that must be matched to create a plot. Possible parameter values are ‘NONE’, ‘SUCCESS’, ‘INCONCLUSIVE’, ‘FAILED’, ‘NEVER’. For plot creation the verdict of the plot’s parent must be equal to or worse than this setting. For instance ‘NONE’ means that the plot is always created whereas the setting ‘FAILED’ causes its creation only if the plot’s parent runs FAILED or ERROR.

Parameters:  **condition** (*str*) – The plot condition

SetExpandXLimitsLeft(*expandXLimitsLeft*)[¶](#ApiClient.PlotSubConfig.SetExpandXLimitsLeft "Link to this definition")  
Sets the expand value of the left limit as expression. The expand value will be added to automatically determined view limits of the plot. An overview plot ignores this setting entirely.

Parameters:  **expandXLimitsLeft** (*str*) – The expression for the expand value of the left limit

SetExpandXLimitsRight(*expandXLimitsRight*)[¶](#ApiClient.PlotSubConfig.SetExpandXLimitsRight "Link to this definition")  
Sets the expand value of the left limit as expression. The expand value will be added to automatically determined view limits of the plot. An overview plot ignores this setting entirely.

Parameters:  **expandXLimitsRight** (*str*) – The expression for the expand value of the right limit

SetMaxNumberPlots(*maxNumberPlots*)[¶](#ApiClient.PlotSubConfig.SetMaxNumberPlots "Link to this definition")  
Sets the maximum number of plots to be created. This number is counted for the entire execution so trigger ranges will not reset the count. An overview plot ignores this setting entirely.

Parameters:  **maxNumberPlots** (*str*) – The maximum number of plots as expression

## PlotSignalBase[¶](#plotsignalbase "Link to this heading")

*class* PlotSignalBase[¶](#ApiClient.PlotSignalBase "Link to this definition")  
Returned by

- [`Plot.GetPlotSignals`](#ApiClient.Plot.GetPlotSignals "ApiClient.Plot.GetPlotSignals")

- [`PlotSubPlot.GetPlotSignals`](#ApiClient.PlotSubPlot.GetPlotSignals "ApiClient.PlotSubPlot.GetPlotSignals")

Subclasses

- [`PlotCalculatedSignal`](#ApiClient.PlotCalculatedSignal "ApiClient.PlotCalculatedSignal")

- [`PlotSignal`](#ApiClient.PlotSignal "ApiClient.PlotSignal")

Clone()[¶](#ApiClient.PlotSignalBase.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`PlotSignalBase`](#ApiClient.PlotSignalBase "ApiClient.PlotSignalBase")

GetAxisIndex()[¶](#ApiClient.PlotSignalBase.GetAxisIndex "Link to this definition")  
Returns the index of the axis the signal is assigned to (starting at zero).

Returns:  The axis index

Return type:  integer

GetColor()[¶](#ApiClient.PlotSignalBase.GetColor "Link to this definition")  
Return the color that is set in this plot signal.

Returns:  The color

Return type:  str

GetDrawStyle()[¶](#ApiClient.PlotSignalBase.GetDrawStyle "Link to this definition")  
Return the draw style that is set in this plot signal.

Returns:  The draw style

Return type:  str

GetLineStyle()[¶](#ApiClient.PlotSignalBase.GetLineStyle "Link to this definition")  
Return the line style that is set in this plot signal.

Returns:  The line style

Return type:  str

GetLineWidth()[¶](#ApiClient.PlotSignalBase.GetLineWidth "Link to this definition")  
Return the line width that is set in this plot signal.

Returns:  The line width

Return type:  float

GetMarkerSize()[¶](#ApiClient.PlotSignalBase.GetMarkerSize "Link to this definition")  
Return the marker size that is set in this plot signal.

Returns:  The marker size

Return type:  float

GetMarkerStyle()[¶](#ApiClient.PlotSignalBase.GetMarkerStyle "Link to this definition")  
Return the marker style that is set in this plot signal.

Returns:  The marker style

Return type:  str

SetAxisIndex(*axisIndex*)[¶](#ApiClient.PlotSignalBase.SetAxisIndex "Link to this definition")  
Assigns the signal to an axis by index.

Parameters:  **axisIndex** (*integer*) – The axis index in the list of axis of a sub plot

SetColor(*color*)[¶](#ApiClient.PlotSignalBase.SetColor "Link to this definition")  
Sets the color of this plot signal. Use value ‘’ to assign the color automatically.

Parameters:  **color** (*str*) – The new color to be set or None.

SetDrawStyle(*drawStyle*)[¶](#ApiClient.PlotSignalBase.SetDrawStyle "Link to this definition")  
Sets the draw style of this plot signal. Valid values are: ‘hold’ or ‘linear’

Parameters:  **drawStyle** (*str*) – The new draw style to be set

SetLineStyle(*lineStyle*)[¶](#ApiClient.PlotSignalBase.SetLineStyle "Link to this definition")  
Sets the line style of this plot signal. Valid values are: ‘-’, ‘–’, ‘-.’ or ‘:’. Use value ‘’ to assign the color automatically.

Parameters:  **lineStyle** (*str*) – The new line style to be set

SetLineWidth(*lineWidth*)[¶](#ApiClient.PlotSignalBase.SetLineWidth "Link to this definition")  
Sets the line width of this plot signal.

Parameters:  **lineWidth** (*float*) – The new line width to be set

SetMarkerSize(*markerSize*)[¶](#ApiClient.PlotSignalBase.SetMarkerSize "Link to this definition")  
Sets the marker size of this plot signal.

Parameters:  **markerSize** (*float*) – The new marker size to be set

SetMarkerStyle(*markerStyle*)[¶](#ApiClient.PlotSignalBase.SetMarkerStyle "Link to this definition")  
Sets the marker style of this plot signal. Valid values are: ‘’ (no marker), ‘o’, ‘\*’, ‘x’, ‘+’, ‘.’.

Parameters:  **markerStyle** (*str*) – The new marker style to be set

## PlotCalculatedSignal[¶](#plotcalculatedsignal "Link to this heading")

*class* PlotCalculatedSignal[¶](#ApiClient.PlotCalculatedSignal "Link to this definition")  
Base class

[`PlotSignalBase`](#ApiClient.PlotSignalBase "ApiClient.PlotSignalBase")

Returned by

- [`TraceAnalysisApi.CreatePlotCalculatedSignal`](#ApiClient.TraceAnalysisApi.CreatePlotCalculatedSignal "ApiClient.TraceAnalysisApi.CreatePlotCalculatedSignal")

Clone()[¶](#ApiClient.PlotCalculatedSignal.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`PlotCalculatedSignal`](#ApiClient.PlotCalculatedSignal "ApiClient.PlotCalculatedSignal")

GetAxisIndex()[¶](#ApiClient.PlotCalculatedSignal.GetAxisIndex "Link to this definition")  
Returns the index of the axis the signal is assigned to (starting at zero).

Returns:  The axis index

Return type:  integer

GetColor()[¶](#ApiClient.PlotCalculatedSignal.GetColor "Link to this definition")  
Return the color that is set in this plot signal.

Returns:  The color

Return type:  str

GetDrawStyle()[¶](#ApiClient.PlotCalculatedSignal.GetDrawStyle "Link to this definition")  
Return the draw style that is set in this plot signal.

Returns:  The draw style

Return type:  str

GetExpression()[¶](#ApiClient.PlotCalculatedSignal.GetExpression "Link to this definition")  
Returns the expression of the calculated signal.

Returns:  The signal expression

Return type:  str

GetLineStyle()[¶](#ApiClient.PlotCalculatedSignal.GetLineStyle "Link to this definition")  
Return the line style that is set in this plot signal.

Returns:  The line style

Return type:  str

GetLineWidth()[¶](#ApiClient.PlotCalculatedSignal.GetLineWidth "Link to this definition")  
Return the line width that is set in this plot signal.

Returns:  The line width

Return type:  float

GetMarkerSize()[¶](#ApiClient.PlotCalculatedSignal.GetMarkerSize "Link to this definition")  
Return the marker size that is set in this plot signal.

Returns:  The marker size

Return type:  float

GetMarkerStyle()[¶](#ApiClient.PlotCalculatedSignal.GetMarkerStyle "Link to this definition")  
Return the marker style that is set in this plot signal.

Returns:  The marker style

Return type:  str

GetName(*namespace=None*)[¶](#ApiClient.PlotCalculatedSignal.GetName "Link to this definition")  
Returns the display name of this plot signal if it is set.

Parameters:  **namespace** (*str*) – Unused

Returns:  The name of this plot signal or empty string.

Return type:  str

IsGenericSignal()[¶](#ApiClient.PlotCalculatedSignal.IsGenericSignal "Link to this definition")  
Returns, if this plot signal has its origin from a generic signal.

Returns:  Always False

Return type:  bool

IsTraceStepSignal()[¶](#ApiClient.PlotCalculatedSignal.IsTraceStepSignal "Link to this definition")  
Returns, if this plot signal has its origin from a trace step.

Returns:  Always False

Return type:  bool

SetAxisIndex(*axisIndex*)[¶](#ApiClient.PlotCalculatedSignal.SetAxisIndex "Link to this definition")  
Assigns the signal to an axis by index.

Parameters:  **axisIndex** (*integer*) – The axis index in the list of axis of a sub plot

SetColor(*color*)[¶](#ApiClient.PlotCalculatedSignal.SetColor "Link to this definition")  
Sets the color of this plot signal. Use value ‘’ to assign the color automatically.

Parameters:  **color** (*str*) – The new color to be set or None.

SetDrawStyle(*drawStyle*)[¶](#ApiClient.PlotCalculatedSignal.SetDrawStyle "Link to this definition")  
Sets the draw style of this plot signal. Valid values are: ‘hold’ or ‘linear’

Parameters:  **drawStyle** (*str*) – The new draw style to be set

SetExpression(*expression*)[¶](#ApiClient.PlotCalculatedSignal.SetExpression "Link to this definition")  
Sets the expression of the calculated signal as an expression. The expression can contain any bound generic signals, package variables or global constants. Additionally constant values are accepted.

Parameters:  **expression** (*str*) – The signal expression

Raises:  
**ApiError** – When expression is not a valid Python expression or is None

SetLineStyle(*lineStyle*)[¶](#ApiClient.PlotCalculatedSignal.SetLineStyle "Link to this definition")  
Sets the line style of this plot signal. Valid values are: ‘-’, ‘–’, ‘-.’ or ‘:’. Use value ‘’ to assign the color automatically.

Parameters:  **lineStyle** (*str*) – The new line style to be set

SetLineWidth(*lineWidth*)[¶](#ApiClient.PlotCalculatedSignal.SetLineWidth "Link to this definition")  
Sets the line width of this plot signal.

Parameters:  **lineWidth** (*float*) – The new line width to be set

SetMarkerSize(*markerSize*)[¶](#ApiClient.PlotCalculatedSignal.SetMarkerSize "Link to this definition")  
Sets the marker size of this plot signal.

Parameters:  **markerSize** (*float*) – The new marker size to be set

SetMarkerStyle(*markerStyle*)[¶](#ApiClient.PlotCalculatedSignal.SetMarkerStyle "Link to this definition")  
Sets the marker style of this plot signal. Valid values are: ‘’ (no marker), ‘o’, ‘\*’, ‘x’, ‘+’, ‘.’.

Parameters:  **markerStyle** (*str*) – The new marker style to be set

SetName(*name*, *namespace=None*)[¶](#ApiClient.PlotCalculatedSignal.SetName "Link to this definition")  
Sets the display name of the calculated signal to plot.

Parameters:  - **name** (*str*) – The new name

- **namespace** (*str*) – Unused

## PlotSignal[¶](#plotsignal "Link to this heading")

*class* PlotSignal[¶](#ApiClient.PlotSignal "Link to this definition")  
Base class

[`PlotSignalBase`](#ApiClient.PlotSignalBase "ApiClient.PlotSignalBase")

Returned by

- [`TraceAnalysisApi.CreatePlotSignal`](#ApiClient.TraceAnalysisApi.CreatePlotSignal "ApiClient.TraceAnalysisApi.CreatePlotSignal")

Clone()[¶](#ApiClient.PlotSignal.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`PlotSignal`](#ApiClient.PlotSignal "ApiClient.PlotSignal")

GetAxisIndex()[¶](#ApiClient.PlotSignal.GetAxisIndex "Link to this definition")  
Returns the index of the axis the signal is assigned to (starting at zero).

Returns:  The axis index

Return type:  integer

GetColor()[¶](#ApiClient.PlotSignal.GetColor "Link to this definition")  
Return the color that is set in this plot signal.

Returns:  The color

Return type:  str

GetDrawStyle()[¶](#ApiClient.PlotSignal.GetDrawStyle "Link to this definition")  
Return the draw style that is set in this plot signal.

Returns:  The draw style

Return type:  str

GetLineStyle()[¶](#ApiClient.PlotSignal.GetLineStyle "Link to this definition")  
Return the line style that is set in this plot signal.

Returns:  The line style

Return type:  str

GetLineWidth()[¶](#ApiClient.PlotSignal.GetLineWidth "Link to this definition")  
Return the line width that is set in this plot signal.

Returns:  The line width

Return type:  float

GetMarkerSize()[¶](#ApiClient.PlotSignal.GetMarkerSize "Link to this definition")  
Return the marker size that is set in this plot signal.

Returns:  The marker size

Return type:  float

GetMarkerStyle()[¶](#ApiClient.PlotSignal.GetMarkerStyle "Link to this definition")  
Return the marker style that is set in this plot signal.

Returns:  The marker style

Return type:  str

GetName(*namespace=None*)[¶](#ApiClient.PlotSignal.GetName "Link to this definition")  
Returns the name of this plot signal.

Parameters:  **namespace** (*str*) – One of ‘tracestep’, ‘generic’, ‘mapping’, ‘file’

Returns:  The name of this plot signal

Return type:  str

IsGenericSignal()[¶](#ApiClient.PlotSignal.IsGenericSignal "Link to this definition")  
Returns, if this plot signal has its origin from a generic signal.

Returns:  True or False

Return type:  bool

IsTraceStepSignal()[¶](#ApiClient.PlotSignal.IsTraceStepSignal "Link to this definition")  
Returns, if this plot signal has its origin from a trace step.

Returns:  True or False

Return type:  bool

SetAxisIndex(*axisIndex*)[¶](#ApiClient.PlotSignal.SetAxisIndex "Link to this definition")  
Assigns the signal to an axis by index.

Parameters:  **axisIndex** (*integer*) – The axis index in the list of axis of a sub plot

SetColor(*color*)[¶](#ApiClient.PlotSignal.SetColor "Link to this definition")  
Sets the color of this plot signal. Use value ‘’ to assign the color automatically.

Parameters:  **color** (*str*) – The new color to be set or None.

SetDrawStyle(*drawStyle*)[¶](#ApiClient.PlotSignal.SetDrawStyle "Link to this definition")  
Sets the draw style of this plot signal. Valid values are: ‘hold’ or ‘linear’

Parameters:  **drawStyle** (*str*) – The new draw style to be set

SetLineStyle(*lineStyle*)[¶](#ApiClient.PlotSignal.SetLineStyle "Link to this definition")  
Sets the line style of this plot signal. Valid values are: ‘-’, ‘–’, ‘-.’ or ‘:’. Use value ‘’ to assign the color automatically.

Parameters:  **lineStyle** (*str*) – The new line style to be set

SetLineWidth(*lineWidth*)[¶](#ApiClient.PlotSignal.SetLineWidth "Link to this definition")  
Sets the line width of this plot signal.

Parameters:  **lineWidth** (*float*) – The new line width to be set

SetMarkerSize(*markerSize*)[¶](#ApiClient.PlotSignal.SetMarkerSize "Link to this definition")  
Sets the marker size of this plot signal.

Parameters:  **markerSize** (*float*) – The new marker size to be set

SetMarkerStyle(*markerStyle*)[¶](#ApiClient.PlotSignal.SetMarkerStyle "Link to this definition")  
Sets the marker style of this plot signal. Valid values are: ‘’ (no marker), ‘o’, ‘\*’, ‘x’, ‘+’, ‘.’.

Parameters:  **markerStyle** (*str*) – The new marker style to be set

SetName(*name*, *namespace=None*)[¶](#ApiClient.PlotSignal.SetName "Link to this definition")  
Sets the name of the signal to plot.

Parameters:  - **name** (*str*) – The new name

- **namespace** (*str*) – One of ‘tracestep’, ‘generic’, ‘mapping’, ‘file’

## PlotSubPlot[¶](#plotsubplot "Link to this heading")

*class* PlotSubPlot[¶](#ApiClient.PlotSubPlot "Link to this definition")  
Returned by

- [`Plot.GetSubPlots`](#ApiClient.Plot.GetSubPlots "ApiClient.Plot.GetSubPlots")

AppendPlotSignal(*plotSignal*)[¶](#ApiClient.PlotSubPlot.AppendPlotSignal "Link to this definition")  
Adds a plot signal to the sub plot.

Note:  
If there is no axis, an axis will be created automatically. If the plot signal has not yet been assigned to an axis, it will be assigned automatically to the first axis.

Parameters:  **plotSignal** ([`PlotSignalBase`](#ApiClient.PlotSignalBase "ApiClient.PlotSignalBase")) – The plot signal to be added

Clone()[¶](#ApiClient.PlotSubPlot.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`PlotSubPlot`](#ApiClient.PlotSubPlot "ApiClient.PlotSubPlot")

CreateAxis()[¶](#ApiClient.PlotSubPlot.CreateAxis "Link to this definition")  
Creates and returns a new axis. The axis will be appended to the list of existing axes of the sub plot.

Returns:  The newly created axis

Return type:  [`PlotAxis`](#ApiClient.PlotAxis "ApiClient.PlotAxis")

GetAxes()[¶](#ApiClient.PlotSubPlot.GetAxes "Link to this definition")  
Returns a list of all separate axes.

Returns:  All seperate axes

Return type:  list[[`PlotAxis`](#ApiClient.PlotAxis "ApiClient.PlotAxis")]

GetAxisIndex(*axis*)[¶](#ApiClient.PlotSubPlot.GetAxisIndex "Link to this definition")  
Returns the index of this axis in the list of all axes of the sub plot (starting at zero).

Parameters:  **axis** ([`PlotAxis`](#ApiClient.PlotAxis "ApiClient.PlotAxis")) – An axis of this sub plot

Returns:  The axis index.

Return type:  int

Raises:  
**ValueError** – If axis is not a member of the sub plot

GetPlotSignals()[¶](#ApiClient.PlotSubPlot.GetPlotSignals "Link to this definition")  
Returns a merged list of all signals of the sub plots.

Returns:  The signals of the plot

Return type:  list[[`PlotSignalBase`](#ApiClient.PlotSignalBase "ApiClient.PlotSignalBase")]

GetType()[¶](#ApiClient.PlotSubPlot.GetType "Link to this definition")  
Returns the type of the sub plot.

Returns:  The sub plot type. One of “common” or “separate”.

Return type:  str

GetYRasterMode()[¶](#ApiClient.PlotSubPlot.GetYRasterMode "Link to this definition")  
Returns the raster mode for the y-axis.

Returns:  the raster mode (0 for no raster, 1 for automatic and 2 for manual raster mode)

Return type:  int

GetYRasterStepSize()[¶](#ApiClient.PlotSubPlot.GetYRasterStepSize "Link to this definition")  
Returns the step size for the raster of the y-axis.

Returns:  the raster step size

Return type:  float

RemovePlotSignal(*plotSignal*)[¶](#ApiClient.PlotSubPlot.RemovePlotSignal "Link to this definition")  
Removes a plot signal from the sub plot.

Parameters:  **plotSignal** ([`PlotSignalBase`](#ApiClient.PlotSignalBase "ApiClient.PlotSignalBase")) – The plot signal to be removed

Raises:  
**ValueError** – If the plot signal is not present

SetType(*subPlotType*)[¶](#ApiClient.PlotSubPlot.SetType "Link to this definition")  
Sets the type of the sub plot. This call is only allowed on the second sub plot!

If the type is “separate”, for each signal of this sub plot there will be a smaller sub plot.

Parameters:  **subPlotType** (*str*) – The sub plot type. One of “common” or “separate”.

SetYRasterMode(*mode*)[¶](#ApiClient.PlotSubPlot.SetYRasterMode "Link to this definition")  
Sets the raster mode for the y-axis.

Parameters:  **mode** (*int*) – 0 for no raster, 1 for automatic and 2 for manual raster mode

Raises:  
**ValueError** – If mode is not a valid parameter

SetYRasterStepSize(*value*)[¶](#ApiClient.PlotSubPlot.SetYRasterStepSize "Link to this definition")  
Sets the step size for the raster of the y-axis.

Parameters:  **value** (*float*) – the raster step size (!= 0.0)

## PlotAxis[¶](#plotaxis "Link to this heading")

*class* PlotAxis[¶](#ApiClient.PlotAxis "Link to this definition")  
Returned by

- [`PlotSubPlot.CreateAxis`](#ApiClient.PlotSubPlot.CreateAxis "ApiClient.PlotSubPlot.CreateAxis")

- [`PlotSubPlot.GetAxes`](#ApiClient.PlotSubPlot.GetAxes "ApiClient.PlotSubPlot.GetAxes")

Clone()[¶](#ApiClient.PlotAxis.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`PlotAxis`](#ApiClient.PlotAxis "ApiClient.PlotAxis")

GetNumeralSystem()[¶](#ApiClient.PlotAxis.GetNumeralSystem "Link to this definition")  
Returns the numeral system of the y-axis.

Returns:  the numeral system (dec for decimal, bin for binary, hex for hexadecimal)

Return type:  str

GetScalingMode()[¶](#ApiClient.PlotAxis.GetScalingMode "Link to this definition")  
Returns the scaling mode for the y-axis.

Returns:  the scaling mode (0 for automatic, 1 for manual scaling mode)

Return type:  int

GetScalingYMaxValue()[¶](#ApiClient.PlotAxis.GetScalingYMaxValue "Link to this definition")  
Returns the maximum value for the y-axis.

Returns:  the maximum value

Return type:  float

GetScalingYMinValue()[¶](#ApiClient.PlotAxis.GetScalingYMinValue "Link to this definition")  
Returns the minimum value for the y-axis.

Returns:  the minimum value

Return type:  float

GetTextShorteningMode()[¶](#ApiClient.PlotAxis.GetTextShorteningMode "Link to this definition")  
Returns the mode for shortening long textual axis labels.

Returns:  The text shortening mode: 0 for no shortening, 1 for left, 2 for middle, 3 for right ellipsizing.

Return type:  int

IsDepictNumericValues()[¶](#ApiClient.PlotAxis.IsDepictNumericValues "Link to this definition")  
Returns whether y-axis values are depicted as numeric values.

Returns:  True if labels are depicted as numeric values.

Return type:  bool

IsDepictTextValues()[¶](#ApiClient.PlotAxis.IsDepictTextValues "Link to this definition")  
Returns whether y-axis labels are depicted as text values of a signal with text representation. Currently, only signals with enumerations are supported.

Returns:  True if labels are depicted as text values.

Return type:  bool

IsMergeNoTextReprValues()[¶](#ApiClient.PlotAxis.IsMergeNoTextReprValues "Link to this definition")  
Returns whether signal values with no explicit text representation should be merged to one entry when plotted.

Does only apply if text values are depicted as axis labels.

Returns:  True if no representation values will be merged.

Return type:  bool

IsScalingYMaxActive()[¶](#ApiClient.PlotAxis.IsScalingYMaxActive "Link to this definition")  
Returns whether the maximum value for the y-axis is active or not.

Returns:  True if the maximum value for the y-axis is active.

Return type:  bool

IsScalingYMinActive()[¶](#ApiClient.PlotAxis.IsScalingYMinActive "Link to this definition")  
Returns whether the minimum value for the y-axis is active or not.

Returns:  True if the minimum value for the y-axis is active.

Return type:  bool

SetDepictNumericValues(*value*)[¶](#ApiClient.PlotAxis.SetDepictNumericValues "Link to this definition")  
Sets whether y-axis labels should be depicted as numerical values.

When combined with the depiction of text values for enumerated signals, additionally, the numeric values are shown in the selected numeral system in brackets behind the text values.

It is not possible to uncheck the depiction of numeric values and text values simultaneously. Then the default setting (depict only numeric values) is chosen.

Parameters:  **value** (*bool*) – True if labels should be depicted as numeric values.

SetDepictTextValues(*value*)[¶](#ApiClient.PlotAxis.SetDepictTextValues "Link to this definition")  
Sets whether y-axis labels should be depicted as text values of a signal with text representation.

When combined with the depiction of numeric values, additionally, the numeric values of the corresponding text values of the enumerated signal are shown in the selected numeral system in brackets behind the text values.

It is not possible to uncheck the depiction of numeric values and text values simultaneously. Then the default setting (depict only numeric values) is chosen.

Parameters:  **value** (*bool*) – True if labels should be depicted as text values.

SetMergeNoTextReprValues(*value*)[¶](#ApiClient.PlotAxis.SetMergeNoTextReprValues "Link to this definition")  
Sets whether signal values with no text explicit representation should be merged into one entry when plotted.

Does only apply if text values are depicted as axis labels.

Parameters:  **value** (*bool*) – True if no representation values should be merged.

SetNumeralSystem(*numeralSystem*)[¶](#ApiClient.PlotAxis.SetNumeralSystem "Link to this definition")  
Sets the numeral system of the y-axis.

Parameters:  **numeralSystem** (*str*) – dec for decimal, bin for binary, hex for hexadecimal

Raises:  
**ValueError** – If numeralSystem is not a valid parameter

SetScalingMode(*mode*)[¶](#ApiClient.PlotAxis.SetScalingMode "Link to this definition")  
Sets the scaling mode for the y-axis.

Parameters:  **mode** (*int*) – 0 for automatic, 1 for manual scaling mode

Raises:  
**ValueError** – If mode is not a valid parameter

SetScalingYMaxActive(*value*)[¶](#ApiClient.PlotAxis.SetScalingYMaxActive "Link to this definition")  
Sets whether the maximum value for the y-axis should be active or not.

Parameters:  **value** (*bool*) – True if the maximum value for the y-axis should be active.

SetScalingYMaxValue(*value*)[¶](#ApiClient.PlotAxis.SetScalingYMaxValue "Link to this definition")  
Sets the maximum value for the y-axis.

Parameters:  **value** (*float*) – The maximum value

SetScalingYMinActive(*value*)[¶](#ApiClient.PlotAxis.SetScalingYMinActive "Link to this definition")  
Sets whether the minimum value for the y-axis should be active or not.

Parameters:  **value** (*bool*) – True if the minimum value for the y-axis should be active.

SetScalingYMinValue(*value*)[¶](#ApiClient.PlotAxis.SetScalingYMinValue "Link to this definition")  
Sets the minimum value for the y-axis.

Parameters:  **value** (*float*) – The minimum value

SetTextShorteningMode(*mode*)[¶](#ApiClient.PlotAxis.SetTextShorteningMode "Link to this definition")  
Sets the mode for shortening long textual axis labels.

Parameters:  **mode** (*int*) – 0 for no shortening, 1 for left, 2 for middle, 3 for right ellipsizing.

GetScalingYMaxActive()[¶](#ApiClient.PlotAxis.GetScalingYMaxActive "Link to this definition")  
Returns whether the maximum value for the y-axis is active or not.

Returns:  True if the maximum value for the y-axis is active.

Return type:  bool

Deprecated since version 2021.2: Please use `IsScalingYMaxActive` instead.

GetScalingYMinActive()[¶](#ApiClient.PlotAxis.GetScalingYMinActive "Link to this definition")  
Returns whether the minimum value for the y-axis is active or not.

Returns:  True if the minimum value for the y-axis is active.

Return type:  bool

Deprecated since version 2021.2: Please use `IsScalingYMinActive` instead.

## TraceAnalysisReferenceDeprecated[¶](#traceanalysisreferencedeprecated "Link to this heading")

*class* TraceAnalysisReferenceDeprecated[¶](#ApiClient.TraceAnalysisReferenceDeprecated "Link to this definition")  
Base class

[`TraceStep`](#ApiClient.TraceStep "ApiClient.TraceStep")

AddTag(*tag*)[¶](#ApiClient.TraceAnalysisReferenceDeprecated.AddTag "Link to this definition")  
Add a specific tag to this step.

Parameters:  **tag** (*str*) – The tag to be set

AssignGenericSignal(*direction*, *sigName*, *genSig*)[¶](#ApiClient.TraceAnalysisReferenceDeprecated.AssignGenericSignal "Link to this definition")  
Bind a generic signal to a signal of the referenced trace analysis.

Parameters:  - **direction** (*str*) – Direction of the binding. Possible values are “IN” or “OUT”.

- **sigName** (*str*) – Name of the signal in the referenced trace analysis

- **genSig** ([`GenericSignal`](#ApiClient.GenericSignal "ApiClient.GenericSignal")) – The generic signal object

Returns:  An object representing the signal binding. If there is already a signal binding for sigName, the signal binding object and its settings will be reused; otherwise, a new signal binding object will be created.

Return type:  [`SignalBinding`](#ApiClient.SignalBinding "ApiClient.SignalBinding")

AssignGenericSignalByName(*direction*, *sigName*, *genSigName*)[¶](#ApiClient.TraceAnalysisReferenceDeprecated.AssignGenericSignalByName "Link to this definition")  
Bind a generic signal to a signal of the referenced trace analysis.

Parameters:  - **direction** (*str*) – Direction of the binding. Possible values are “IN” or “OUT”.

- **sigName** (*str*) – Name of the signal in the referenced trace analysis

- **genSigName** (*str*) – Name of the generic signal

Returns:  An object representing the signal binding. If there is already a signal binding for sigName, the signal binding object and its settings will be reused; otherwise, a new signal binding object will be created.

Return type:  [`SignalBinding`](#ApiClient.SignalBinding "ApiClient.SignalBinding")

ClearSignalBinding(*direction*, *sigName*)[¶](#ApiClient.TraceAnalysisReferenceDeprecated.ClearSignalBinding "Link to this definition")  
Clears the signal binding for the given signal name.

Parameters:  - **direction** (*str*) – Direction of the binding. Possible values: “IN” or “OUT”

- **sigName** (*str*) – The signal name

Clone()[¶](#ApiClient.TraceAnalysisReferenceDeprecated.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`TraceAnalysisReferenceDeprecated`](#ApiClient.TraceAnalysisReferenceDeprecated "ApiClient.TraceAnalysisReferenceDeprecated")

GetDescription()[¶](#ApiClient.TraceAnalysisReferenceDeprecated.GetDescription "Link to this definition")  
Returns the description of the trace analysis element.

Returns:  The description

Return type:  str

GetLineNo()[¶](#ApiClient.TraceAnalysisReferenceDeprecated.GetLineNo "Link to this definition")  
Returns the trace steps line number within its trace analysis.

Returns:  Line number

Return type:  int

GetName()[¶](#ApiClient.TraceAnalysisReferenceDeprecated.GetName "Link to this definition")  
Returns the name of the trace analysis element.

Returns:  The name

Return type:  str

GetPackagePath()[¶](#ApiClient.TraceAnalysisReferenceDeprecated.GetPackagePath "Link to this definition")  
Returns the path to the referenced package.

Note:  
May throw an exception if the expression of the path cannot be resolved. In that case, try using [`GetPackagePathExpression()`](#ApiClient.TraceAnalysisReferenceDeprecated.GetPackagePathExpression "ApiClient.TraceAnalysisReferenceDeprecated.GetPackagePathExpression").

Returns:  The package path. Returns None if no path is set.

Return type:  str

GetPackagePathExpression()[¶](#ApiClient.TraceAnalysisReferenceDeprecated.GetPackagePathExpression "Link to this definition")  
Returns the expression representing the path of the referenced package.

Returns:  The expression representing the package path. Returns None if no path is set.

Return type:  str

GetParameter(*paramName*)[¶](#ApiClient.TraceAnalysisReferenceDeprecated.GetParameter "Link to this definition")  
Retrieves the expression assigned to a package parameter.

Parameters:  **paramName** (*str*) – Name of the parameter

Returns:  Expression assigned to the parameter

Return type:  str

GetParameterNames()[¶](#ApiClient.TraceAnalysisReferenceDeprecated.GetParameterNames "Link to this definition")  
Returns the names of the parameters that can be configured for the referenced trace analysis.

Returns:  The list of valid parameter names

Return type:  list[str]

GetParameters()[¶](#ApiClient.TraceAnalysisReferenceDeprecated.GetParameters "Link to this definition")  
Retrieves all package parameters with its expressions.

Returns:  Dictionary with expressions assigned to the parameters

Return type:  dict[str, str]

GetPkgParameters()[¶](#ApiClient.TraceAnalysisReferenceDeprecated.GetPkgParameters "Link to this definition")  
Returns a list of the incoming parameter names located in the referenced package.

Returns:  The parameter names

Return type:  list[str]

GetPkgReturns()[¶](#ApiClient.TraceAnalysisReferenceDeprecated.GetPkgReturns "Link to this definition")  
Returns a list of the outgoing parameters located in the referenced package.

Returns:  The return names

Return type:  list[str]

GetPkgTraceAnalyses()[¶](#ApiClient.TraceAnalysisReferenceDeprecated.GetPkgTraceAnalyses "Link to this definition")  
Returns a list of the trace analysis names located in the referenced package.

Returns:  The names of the trace analyses

Return type:  list[str]

GetReturn(*varInternal*)[¶](#ApiClient.TraceAnalysisReferenceDeprecated.GetReturn "Link to this definition")  
Retrieves the variable name assigned to a package return value.

Parameters:  **varInternal** (*str*) – Name of the return variable in the called package

Returns:  Assigned variable of the calling package. Empty string if there is not any variable assigned.

Return type:  str

GetReturns()[¶](#ApiClient.TraceAnalysisReferenceDeprecated.GetReturns "Link to this definition")  
Retrieves the return value assignments.

Returns:  Assigned variables of the calling package

Return type:  dict[str, str]

GetSignalBinding(*direction*, *sigName*)[¶](#ApiClient.TraceAnalysisReferenceDeprecated.GetSignalBinding "Link to this definition")  
Get the signal binding for a signal.

Parameters:  - **direction** (*str*) – Direction of the binding. Possible values: “IN” or “OUT”

- **sigName** (*str*) – Name of the signal in the referenced trace analysis

Return type:  [`SignalBinding`](#ApiClient.SignalBinding "ApiClient.SignalBinding")

Returns:  An object representing the signal binding.

GetTags()[¶](#ApiClient.TraceAnalysisReferenceDeprecated.GetTags "Link to this definition")  
Returns the tags set for this step.

Returns:  A (sorted) list of tags

Return type:  list[str]

GetTraceAnalysisName()[¶](#ApiClient.TraceAnalysisReferenceDeprecated.GetTraceAnalysisName "Link to this definition")  
Returns the name of the referenced trace analysis.

Return type:  str

Returns:  The name of the referenced trace analysis

GetType()[¶](#ApiClient.TraceAnalysisReferenceDeprecated.GetType "Link to this definition")  
Returns the type (class name) of the trace step, e.g.

> - ‘Episode’
>
> - ‘AnalysisBlock’
>
> - ‘TriggerBlock’
>
> - ‘Calculation’
>
> - ‘TemplateBasedTraceStep’
>
> - ‘TraceAnalysisReference’
>
> - ‘TraceAnalysisReferenceDeprecated’

Returns:  Type (class name) of the trace step

Return type:  str

GetUuid()[¶](#ApiClient.TraceAnalysisReferenceDeprecated.GetUuid "Link to this definition")  
Returns the UUID of the trace step.

Returns:  UUID of the trace step

Return type:  str

IsContainer()[¶](#ApiClient.TraceAnalysisReferenceDeprecated.IsContainer "Link to this definition")  
Checks whether this trace step can contain trace steps.

Returns:  True if it can contain trace steps, else False

Return type:  boolean

IsEnabled()[¶](#ApiClient.TraceAnalysisReferenceDeprecated.IsEnabled "Link to this definition")  
Checks whether the trace step is enabled.

Returns:  True if trace step is enabled, else False

Return type:  boolean

IsOk()[¶](#ApiClient.TraceAnalysisReferenceDeprecated.IsOk "Link to this definition")  
Returns the internal state of correctness of the trace step.

Returns:  True if no problems were found, else False

Return type:  boolean

IsVisible()[¶](#ApiClient.TraceAnalysisReferenceDeprecated.IsVisible "Link to this definition")  
Checks whether the trace step is visible. This depends on the trace step itself or a parent trace step being disabled.

Returns:  True if trace step is visible, else False

Return type:  boolean

RemoveTag(*tag*)[¶](#ApiClient.TraceAnalysisReferenceDeprecated.RemoveTag "Link to this definition")  
Remove a specific tag from this step.

Parameters:  **tag** (*str*) – The tag to be removed

SetDescription(*value*)[¶](#ApiClient.TraceAnalysisReferenceDeprecated.SetDescription "Link to this definition")  
Sets the description of the trace analysis element.

Parameters:  **value** (*str*) – The new description

SetEnabled(*enable*)[¶](#ApiClient.TraceAnalysisReferenceDeprecated.SetEnabled "Link to this definition")  
Enables or disables the trace step (this also affects child trace steps).

Parameters:  **enable** (*boolean*) – If True, enables the trace step, if False, disables the trace step

SetName(*value*)[¶](#ApiClient.TraceAnalysisReferenceDeprecated.SetName "Link to this definition")  
Sets the name of the trace analysis element.

Parameters:  **value** (*str*) – The new name

SetPackagePath(*packagePath*)[¶](#ApiClient.TraceAnalysisReferenceDeprecated.SetPackagePath "Link to this definition")  
Sets the package path.

Note:  
Signal bindings will be synchronized. Deprecated bindings will be deleted.

Parameters:  **packagePath** (*str*) – The package path

SetParameter(*paramName*, *paramValue*)[¶](#ApiClient.TraceAnalysisReferenceDeprecated.SetParameter "Link to this definition")  
Assigns a value to a package parameter.

Parameters:  - **paramName** (*str*) – Name of the parameter

- **paramValue** (*str*) – Value to assign to the parameter (can be an expression)

SetParameters(*paramDict*)[¶](#ApiClient.TraceAnalysisReferenceDeprecated.SetParameters "Link to this definition")  
Assigns values to package parameters.

Parameters:  **paramDict** (*dict[str,* *str]*) – Dictionary of parameter name -> parameter value (expression) mappings

SetReturn(*varInternal*, *varExternal*)[¶](#ApiClient.TraceAnalysisReferenceDeprecated.SetReturn "Link to this definition")  
Assigns a return value to a variable.

Parameters:  - **varInternal** (*str*) – Return variable of the called package

- **varExternal** (*str*) – Variable of the calling package to assign the return value to

SetReturns(*returnDict*)[¶](#ApiClient.TraceAnalysisReferenceDeprecated.SetReturns "Link to this definition")  
Assigns package return values to variables.

Parameters:  **returnDict** (*dict[str,* *str]*) – Dictionary of return variable -> variable of the calling package mappings

SetTags(*tags*)[¶](#ApiClient.TraceAnalysisReferenceDeprecated.SetTags "Link to this definition")  
Set the list of tags for this step. The list of tags will be sorted and stored.

Parameters:  **tags** (*list[str]*) – The list of tags

SetTraceAnalysisName(*name*)[¶](#ApiClient.TraceAnalysisReferenceDeprecated.SetTraceAnalysisName "Link to this definition")  
Sets the name of the referenced trace analysis.

Note:  
Signal bindings will be synchronized. Deprecated bindings will be deleted.

Parameters:  **name** (*str*) – The name

## TraceAnalysisReference[¶](#traceanalysisreference "Link to this heading")

*class* TraceAnalysisReference[¶](#ApiClient.TraceAnalysisReference "Link to this definition")  
Most methods of the [`TraceAnalysisReference`](#ApiClient.TraceAnalysisReference "ApiClient.TraceAnalysisReference") can only be used if it is assigned to a package.

I.e. add the [`TraceAnalysisReference`](#ApiClient.TraceAnalysisReference "ApiClient.TraceAnalysisReference") to a trace analysis and the trace analysis itself to a package.

Base class

[`TraceStep`](#ApiClient.TraceStep "ApiClient.TraceStep")

Returned by

- [`TraceAnalysisApi.CreateTraceAnalysisReference`](#ApiClient.TraceAnalysisApi.CreateTraceAnalysisReference "ApiClient.TraceAnalysisApi.CreateTraceAnalysisReference")

AddTag(*tag*)[¶](#ApiClient.TraceAnalysisReference.AddTag "Link to this definition")  
Add a specific tag to this step.

Parameters:  **tag** (*str*) – The tag to be set

AssignGenericSignal(*direction*, *sigName*, *genSig*)[¶](#ApiClient.TraceAnalysisReference.AssignGenericSignal "Link to this definition")  
Bind a generic signal to a signal of the referenced trace analysis.

Parameters:  - **direction** (*str*) – Direction of the binding. Possible values are “IN” or “OUT”.

- **sigName** (*str*) – Name of the signal in the referenced trace analysis

- **genSig** ([`GenericSignal`](#ApiClient.GenericSignal "ApiClient.GenericSignal")) – The generic signal object

Returns:  An object representing the signal binding. If there is already a signal binding for sigName, the signal binding object and its settings will be reused; otherwise, a new signal binding object will be created.

Return type:  [`SignalBinding`](#ApiClient.SignalBinding "ApiClient.SignalBinding")

Raise:  
ApiError: - The trace analysis reference has to be added to the package before generic  
signals can be assigned.

- The direction either has to be ‘IN’ or ‘OUT’.

- There is no signal of given name in the referenced trace analysis.

AssignGenericSignalByName(*direction*, *sigName*, *genSigName*)[¶](#ApiClient.TraceAnalysisReference.AssignGenericSignalByName "Link to this definition")  
Bind a generic signal to a signal of the referenced trace analysis.

Parameters:  - **direction** (*str*) – Direction of the binding. Possible values are “IN” or “OUT”.

- **sigName** (*str*) – Name of the signal in the referenced trace analysis

- **genSigName** (*str*) – Name of the generic signal

Returns:  An object representing the signal binding. If there is already a signal binding for sigName, the signal binding object and its settings will be reused; otherwise, a new signal binding object will be created.

Return type:  [`SignalBinding`](#ApiClient.SignalBinding "ApiClient.SignalBinding")

Raise:  
ApiError: - The trace analysis reference has to be added to the package before generic  
signals can be assigned.

- The generic signal of given name doesn’t exist.

- The direction either has to be ‘IN’ or ‘OUT’.

- There is no signal of given name in the referenced trace analysis.

ClearSignalBinding(*direction*, *sigName*)[¶](#ApiClient.TraceAnalysisReference.ClearSignalBinding "Link to this definition")  
Clears the signal binding for the given signal name.

Parameters:  - **direction** (*str*) – Direction of the binding. Possible values: “IN” or “OUT”

- **sigName** (*str*) – The signal name

Raise:  
ApiError: The direction either has to be ‘IN’ or ‘OUT’.

Clone()[¶](#ApiClient.TraceAnalysisReference.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`TraceAnalysisReference`](#ApiClient.TraceAnalysisReference "ApiClient.TraceAnalysisReference")

GetDescription()[¶](#ApiClient.TraceAnalysisReference.GetDescription "Link to this definition")  
Returns the description of the trace analysis element.

Returns:  The description

Return type:  str

GetLineNo()[¶](#ApiClient.TraceAnalysisReference.GetLineNo "Link to this definition")  
Returns the trace steps line number within its trace analysis.

Returns:  Line number

Return type:  int

GetMappingItemReferenceName()[¶](#ApiClient.TraceAnalysisReference.GetMappingItemReferenceName "Link to this definition")  
Returns the reference name of the package mapping item used by this trace step.

Returns:  Reference name of the used mapping item.

Return type:  str

GetName()[¶](#ApiClient.TraceAnalysisReference.GetName "Link to this definition")  
Returns the name of the trace analysis element.

Returns:  The name

Return type:  str

GetParameter(*paramName*)[¶](#ApiClient.TraceAnalysisReference.GetParameter "Link to this definition")  
Retrieves the expression assigned to a package parameter.

Parameters:  **paramName** (*str*) – Name of the parameter

Returns:  Expression assigned to the parameter

Return type:  str

Raise:  
ApiError: - The package either doesn’t exist or it is a recursive dependency. - The parameter of given name doesn’t exist.

GetParameterNames()[¶](#ApiClient.TraceAnalysisReference.GetParameterNames "Link to this definition")  
Returns the names of the parameters that can be configured for the referenced trace analysis.

Returns:  The list of valid parameter names

Return type:  list[str]

GetParameters()[¶](#ApiClient.TraceAnalysisReference.GetParameters "Link to this definition")  
Retrieves all package parameters with its expressions.

Returns:  Dictionary with expressions assigned to the parameters

Return type:  dict[str, str]

GetPkgParameters()[¶](#ApiClient.TraceAnalysisReference.GetPkgParameters "Link to this definition")  
Returns a list of the incoming parameter names located in the referenced package.

Returns:  The parameter names

Return type:  list[str]

Raise:  
ApiError: The referenced package is invalid, might not exist or is a recursive dependency.

GetPkgReturns()[¶](#ApiClient.TraceAnalysisReference.GetPkgReturns "Link to this definition")  
Returns a list of the outgoing parameters located in the referenced package.

Returns:  The return names

Return type:  list[str]

Raise:  
ApiError: The referenced package is invalid, might not exist or is a recursive dependency.

GetPkgTraceAnalyses()[¶](#ApiClient.TraceAnalysisReference.GetPkgTraceAnalyses "Link to this definition")  
Returns a list of the trace analysis names located in the referenced package.

Returns:  The names of the trace analyses

Return type:  list[str]

Raise:  
ApiError: The referenced package is invalid, might not exist or is a recursive dependency.

GetReferencedPackage()[¶](#ApiClient.TraceAnalysisReference.GetReferencedPackage "Link to this definition")  
Returns the referenced package.

Returns:  The referenced package.

Return type:  [`PackageBase`](#ApiClient.PackageBase "ApiClient.PackageBase")

GetReturn(*varInternal*)[¶](#ApiClient.TraceAnalysisReference.GetReturn "Link to this definition")  
Retrieves the variable name assigned to a package return value.

Parameters:  **varInternal** (*str*) – Name of the return variable in the called package

Returns:  Assigned variable of the calling package. Empty string if there is not any variable assigned.

Return type:  str

GetReturns()[¶](#ApiClient.TraceAnalysisReference.GetReturns "Link to this definition")  
Retrieves the return value assignments.

Returns:  Assigned variables of the calling package

Return type:  dict[str, str]

GetSignalBinding(*direction*, *sigName*)[¶](#ApiClient.TraceAnalysisReference.GetSignalBinding "Link to this definition")  
Get the signal binding for a signal.

Parameters:  - **direction** (*str*) – Direction of the binding. Possible values: “IN” or “OUT”

- **sigName** (*str*) – Name of the signal in the referenced trace analysis

Return type:  [`SignalBinding`](#ApiClient.SignalBinding "ApiClient.SignalBinding")

Returns:  An object representing the signal binding.

Raise:  
ApiError: The direction either has to be ‘IN’ or ‘OUT’.

GetTags()[¶](#ApiClient.TraceAnalysisReference.GetTags "Link to this definition")  
Returns the tags set for this step.

Returns:  A (sorted) list of tags

Return type:  list[str]

GetTraceAnalysisName()[¶](#ApiClient.TraceAnalysisReference.GetTraceAnalysisName "Link to this definition")  
Returns the name of the referenced trace analysis.

Return type:  str

Returns:  The name of the referenced trace analysis

GetType()[¶](#ApiClient.TraceAnalysisReference.GetType "Link to this definition")  
Returns the type (class name) of the trace step, e.g.

> - ‘Episode’
>
> - ‘AnalysisBlock’
>
> - ‘TriggerBlock’
>
> - ‘Calculation’
>
> - ‘TemplateBasedTraceStep’
>
> - ‘TraceAnalysisReference’
>
> - ‘TraceAnalysisReferenceDeprecated’

Returns:  Type (class name) of the trace step

Return type:  str

GetUuid()[¶](#ApiClient.TraceAnalysisReference.GetUuid "Link to this definition")  
Returns the UUID of the trace step.

Returns:  UUID of the trace step

Return type:  str

IsContainer()[¶](#ApiClient.TraceAnalysisReference.IsContainer "Link to this definition")  
Checks whether this trace step can contain trace steps.

Returns:  True if it can contain trace steps, else False

Return type:  boolean

IsEnabled()[¶](#ApiClient.TraceAnalysisReference.IsEnabled "Link to this definition")  
Checks whether the trace step is enabled.

Returns:  True if trace step is enabled, else False

Return type:  boolean

IsOk()[¶](#ApiClient.TraceAnalysisReference.IsOk "Link to this definition")  
Returns the internal state of correctness of the trace step.

Returns:  True if no problems were found, else False

Return type:  boolean

IsVisible()[¶](#ApiClient.TraceAnalysisReference.IsVisible "Link to this definition")  
Checks whether the trace step is visible. This depends on the trace step itself or a parent trace step being disabled.

Returns:  True if trace step is visible, else False

Return type:  boolean

RemoveTag(*tag*)[¶](#ApiClient.TraceAnalysisReference.RemoveTag "Link to this definition")  
Remove a specific tag from this step.

Parameters:  **tag** (*str*) – The tag to be removed

SetDescription(*value*)[¶](#ApiClient.TraceAnalysisReference.SetDescription "Link to this definition")  
Sets the description of the trace analysis element.

Parameters:  **value** (*str*) – The new description

SetEnabled(*enable*)[¶](#ApiClient.TraceAnalysisReference.SetEnabled "Link to this definition")  
Enables or disables the trace step (this also affects child trace steps).

Parameters:  **enable** (*boolean*) – If True, enables the trace step, if False, disables the trace step

SetMappingItemReferenceName(*mappingName*)[¶](#ApiClient.TraceAnalysisReference.SetMappingItemReferenceName "Link to this definition")  
Sets the package mapping item of given reference name used by this trace step.

Parameters:  **mappingName** (*str*) – Reference name of the mapping item to be used.

Raise:  
ApiError: A mapping of given reference name doesn’t exist in the referencing package.

SetName(*value*)[¶](#ApiClient.TraceAnalysisReference.SetName "Link to this definition")  
Sets the name of the trace analysis element.

Parameters:  **value** (*str*) – The new name

SetParameter(*paramName*, *paramValue*)[¶](#ApiClient.TraceAnalysisReference.SetParameter "Link to this definition")  
Assigns a value to a package parameter.

Parameters:  - **paramName** (*str*) – Name of the parameter

- **paramValue** (*str*) – Value to assign to the parameter (can be an expression)

SetParameters(*paramDict*)[¶](#ApiClient.TraceAnalysisReference.SetParameters "Link to this definition")  
Assigns values to package parameters.

Parameters:  **paramDict** (*dict[str,* *str]*) – Dictionary of parameter name -> parameter value (expression) mappings

SetReturn(*varInternal*, *varExternal*)[¶](#ApiClient.TraceAnalysisReference.SetReturn "Link to this definition")  
Assigns a return value to a variable.

Parameters:  - **varInternal** (*str*) – Return variable of the called package

- **varExternal** (*str*) – Variable of the calling package to assign the return value to

Raise:  
ApiError: The trace analysis reference has to be added to the package before returns can be set.

SetReturns(*returnDict*)[¶](#ApiClient.TraceAnalysisReference.SetReturns "Link to this definition")  
Assigns package return values to variables.

Parameters:  **returnDict** (*dict[str,* *str]*) – Dictionary of return variable -> variable of the calling package mappings

SetTags(*tags*)[¶](#ApiClient.TraceAnalysisReference.SetTags "Link to this definition")  
Set the list of tags for this step. The list of tags will be sorted and stored.

Parameters:  **tags** (*list[str]*) – The list of tags

SetTraceAnalysisName(*name*)[¶](#ApiClient.TraceAnalysisReference.SetTraceAnalysisName "Link to this definition")  
Sets the name of the referenced trace analysis.

Note:  
Signal bindings will be synchronized. Deprecated bindings will be deleted.

Parameters:  **name** (*str*) – The name

Raise:  
ApiError: - The referenced package is invalid, might not exist or is a recursive  
dependency.

- The referenced package doesn’t contain a trace analysis of given name.

GetPackagePath()[¶](#ApiClient.TraceAnalysisReference.GetPackagePath "Link to this definition")  
Returns the path to the referenced package.

Returns:  The package path. Returns None if no path is set.

Return type:  str

Deprecated since version 2024.2: Please use [`GetMappingItemReferenceName`](#ApiClient.TraceAnalysisReference.GetMappingItemReferenceName "ApiClient.TraceAnalysisReference.GetMappingItemReferenceName") instead and retrieve the path of the referenced package from the mapping item.

GetPackagePathExpression()[¶](#ApiClient.TraceAnalysisReference.GetPackagePathExpression "Link to this definition")  
Returns the expression representing the path of the referenced package.

Returns:  The expression representing the package path. Returns None if no path is set.

Return type:  str

Deprecated since version 2024.2: Please use [`GetMappingItemReferenceName`](#ApiClient.TraceAnalysisReference.GetMappingItemReferenceName "ApiClient.TraceAnalysisReference.GetMappingItemReferenceName") instead and retrieve the path of the referenced package from the mapping item.

SetPackagePath(*packagePath*)[¶](#ApiClient.TraceAnalysisReference.SetPackagePath "Link to this definition")  
Sets the package path.

Note:  
Signal bindings will be synchronized. Deprecated bindings will be deleted.

Parameters:  **packagePath** (*str*) – The package path

Raise:  
ApiError: - The trace analysis reference has to be added to the package before the  
package path can be set.

- The package either doesn’t exist or it is a recursive dependency.

Deprecated since version 2024.2: Please use [`SetMappingItemReferenceName`](#ApiClient.TraceAnalysisReference.SetMappingItemReferenceName "ApiClient.TraceAnalysisReference.SetMappingItemReferenceName") instead.

## PackageBase[¶](#packagebase "Link to this heading")

*class* PackageBase[¶](#ApiClient.PackageBase "Link to this definition")  
Returned by

- [`ParameterSet.GetPackage`](ProjectApi.md#ApiClient.ParameterSet.GetPackage "ApiClient.ParameterSet.GetPackage")

- [`ParameterSetAnalysisPackage.GetPackage`](ComponentApi.md#ApiClient.ParameterSetAnalysisPackage.GetPackage "ApiClient.ParameterSetAnalysisPackage.GetPackage")

- [`ParameterSetBase.GetPackage`](ComponentApi.md#ApiClient.ParameterSetBase.GetPackage "ApiClient.ParameterSetBase.GetPackage")

- [`TraceAnalysisReference.GetReferencedPackage`](#ApiClient.TraceAnalysisReference.GetReferencedPackage "ApiClient.TraceAnalysisReference.GetReferencedPackage")

Subclasses

- [`AnalysisPackage`](PackageApi.md#ApiClient.AnalysisPackage "ApiClient.AnalysisPackage")

- [`Package`](PackageApi.md#ApiClient.Package "ApiClient.Package")

Attributes[¶](#ApiClient.PackageBase.Attributes "Link to this definition")  
Returns access to the package attributes definitions specified within the parameter set and the referenced package attribute definition files.

Returns:  Package attribute interface of the parameter set

Return type:  [`Attributes`](ProjectApi.md#ApiClient.Attributes "ApiClient.Attributes")

AddVariable(*variable*)[¶](#ApiClient.PackageBase.AddVariable "Link to this definition")  
Adds a variable to the package.

Parameters:  **variable** ([`Variable`](VariableApi.md#ApiClient.Variable "ApiClient.Variable")) – Variable to be added

Clone()[¶](#ApiClient.PackageBase.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`PackageBase`](#ApiClient.PackageBase "ApiClient.PackageBase")

Close()[¶](#ApiClient.PackageBase.Close "Link to this definition")  
Closes the package. After closing the package it can not be modified/accessed anymore.

GetActivationCondition()[¶](#ApiClient.PackageBase.GetActivationCondition "Link to this definition")  
Gets the activation condition for this package.

Returns:  The expression defining the activation condition

Return type:  str

GetDescription()[¶](#ApiClient.PackageBase.GetDescription "Link to this definition")  
Returns the package description.

Returns:  Description shown in the package properties

Return type:  str

GetFilename()[¶](#ApiClient.PackageBase.GetFilename "Link to this definition")  
Returns the file name of the package file as absolute path, if this is a file. If not it may be unsaved.

Returns:  The file name of the saved file or None, if not a file

Return type:  str

GetMapping()[¶](#ApiClient.PackageBase.GetMapping "Link to this definition")  
Returns the local mapping of the package.

Returns:  Mapping of the package

Return type:  [`LocalMapping`](PackageApi.md#ApiClient.LocalMapping "ApiClient.LocalMapping")

GetName()[¶](#ApiClient.PackageBase.GetName "Link to this definition")  
Returns the package name.

Returns:  Package name.

Return type:  str

GetParameterVariables()[¶](#ApiClient.PackageBase.GetParameterVariables "Link to this definition")  
Returns a list of all variables defined in the analysis package and set as a parameter.

Returns:  List of all defined parameters

Return type:  list[[`Variable`](VariableApi.md#ApiClient.Variable "ApiClient.Variable")]

GetReturnVariables()[¶](#ApiClient.PackageBase.GetReturnVariables "Link to this definition")  
Returns a list of all variables defined in the package and set as a return variable.

Returns:  List of all defined return variables

Return type:  list[[`Variable`](VariableApi.md#ApiClient.Variable "ApiClient.Variable")]

GetTestScriptId()[¶](#ApiClient.PackageBase.GetTestScriptId "Link to this definition")  
Returns the test script id of the package.

Returns:  Test script id.

Return type:  str

GetType()[¶](#ApiClient.PackageBase.GetType "Link to this definition")  
Returns the type (class name) of the package, e.g.  
- “Package”

- “AnalysisPackage”

Returns:  Type (class name) of the package

Return type:  str

GetUnusedVariables()[¶](#ApiClient.PackageBase.GetUnusedVariables "Link to this definition")  
Returns the list of unused variables defined in the package.

Returns:  List of all unused defined variables

Return type:  list[[`Variable`](VariableApi.md#ApiClient.Variable "ApiClient.Variable")]

GetVariable(*name*)[¶](#ApiClient.PackageBase.GetVariable "Link to this definition")  
Returns the variable defined in the package with a specific name.

Parameters:  **name** (*string*) – The name of the variable

Returns:  Variable with the specified name or None

Return type:  [`Variable`](VariableApi.md#ApiClient.Variable "ApiClient.Variable")

GetVariables()[¶](#ApiClient.PackageBase.GetVariables "Link to this definition")  
Returns a list of all variables defined in the package.

Returns:  List of all defined variables

Return type:  list[[`Variable`](VariableApi.md#ApiClient.Variable "ApiClient.Variable")]

GetVersion()[¶](#ApiClient.PackageBase.GetVersion "Link to this definition")  
Returns the package version.

Returns:  Version shown in the package properties

Return type:  str

HasSpecificationFlag()[¶](#ApiClient.PackageBase.HasSpecificationFlag "Link to this definition")  
Returns the state of the specification flag.

Returns:  True if specification flag is enabled, otherwise False

Return type:  bool

HasTestCaseFlag()[¶](#ApiClient.PackageBase.HasTestCaseFlag "Link to this definition")  
Returns the state of the test case flag.

Returns:  True if test case flag is enabled, otherwise False

Return type:  bool

IsActivationConditionFulfilled()[¶](#ApiClient.PackageBase.IsActivationConditionFulfilled "Link to this definition")  
Evaluates the activation condition defined in the package.

Returns:  True, if the activation condition is fulfilled.

Return type:  bool

Raises:  
**ApiError** – If the activation condition is not evaluable

RemoveVariable(*variableName*)[¶](#ApiClient.PackageBase.RemoveVariable "Link to this definition")  
Removes a variable from the package.

Parameters:  **variableName** (*str*) – Name of variable to be removed

RenameVariable(*oldVarName*, *newVarName*)[¶](#ApiClient.PackageBase.RenameVariable "Link to this definition")  
Renames a existing variable of the package.

Parameters:  - **oldVarName** (*str*) – The old variable name

- **newVarName** (*str*) – The new variable name

Save(*filename=None*)[¶](#ApiClient.PackageBase.Save "Link to this definition")  
Saves the package. Appends file ending if needed.

Parameters:  **filename** (*str*) – File name of the package; Either absolute or relative to the ‘Packages’ directory. Leave out to save the package to its existing file (previously set with [`Save()`](PackageApi.md#ApiClient.Package.Save "ApiClient.Package.Save") or from [`PackageApi.OpenPackage()`](PackageApi.md#ApiClient.PackageApi.OpenPackage "ApiClient.PackageApi.OpenPackage"))

SetActivationCondition(*expression*)[¶](#ApiClient.PackageBase.SetActivationCondition "Link to this definition")  
Sets the activation condition for this package.

Parameters:  **expression** (*str*) – The expression defining the activation condition

SetDescription(*description*)[¶](#ApiClient.PackageBase.SetDescription "Link to this definition")  
Sets the package description.

Parameters:  **description** (*str*) – Description to be shown in the package properties

SetSpecificationFlag(*state=True*)[¶](#ApiClient.PackageBase.SetSpecificationFlag "Link to this definition")  
Sets the specification flag.

Parameters:  **state** (*bool*) – True to enable, False to disable the specification flag

SetTestCaseFlag(*state=True*)[¶](#ApiClient.PackageBase.SetTestCaseFlag "Link to this definition")  
Sets the test case flag.

Parameters:  **state** (*bool*) – True to enable, False to disable the test case flag

SetTestScriptId(*testSriptId*)[¶](#ApiClient.PackageBase.SetTestScriptId "Link to this definition")  
Sets the test script id of the package.

Parameters:  **testSriptId** (*str*) – Test script id

SetVersion(*version*)[¶](#ApiClient.PackageBase.SetVersion "Link to this definition")  
Sets the package version.

Parameters:  **version** (*str*) – Version to be shown in the package properties
