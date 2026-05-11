# How to build a flow definition (condensed)

> Condensed notes for quick lookup while editing `flow_definition.py` (FlowBuilder / add_block_with / Assign / special blocks).

## Table of contents

- [1. Minimal structure](#1-minimal-structure)
- [2. Block library and documentation](#2-block-library-and-documentation)
- [3. Adding blocks to the flow definition: `FlowBuilder.add_block_with`](#3-adding-blocks-to-the-flow-definition-flowbuilderadd_block_with)
  - [3.1 Definition of the block](#31-definition-of-the-block)
  - [3.2 Explicit connections between blocks: `required_blocks`](#32-explicit-connections-between-blocks-required_blocks)
  - [3.3 Assigning values to block parameters: `Assign(...)`](#33-assigning-values-to-block-parameters-assign)
    - [3.3.1 `to_static_value(value)`](#331-to_static_valuevalue)
    - [3.3.2 `to_block_result(block)`](#332-to_block_resultblock)
    - [3.3.3 `to_user_expression(\"expr\")`](#333-to_user_expressionexpr)
- [4. Defining a human-readable label: `.with_label()`](#4-defining-a-human-readable-label-with_label)
- [5. Type Checking](#5-type-checking)
- [6. Environment variables (ResourceAdapter)](#6-environment-variables-resourceadapter)
- [7. Special blocks](#7-special-blocks)
  - [7.1 `GenericUserCode`](#71-genericusercode)
  - [7.2 `ConditionalSkip`](#72-conditionalskip)
  - [7.3 `BatchProcessing`](#73-batchprocessing)

## 1. Minimal structure

- The `flow_definition.py` holds the implementation of the workflow.
- The starting point is `get_flow() -> Flow` using the `FlowBuilder`.
- The minimal implementation can be an empty workflow:

```py
def get_flow() -> Flow:
    """Define the flow to be executed."""
    return (
        FlowBuilder()
        .build()
    )
```

## 2. Block library and documentation

- flow.kit provides a library of flow blocks. You build the automation for your workflow by using these blocks in the flow definition.
- Common block types:
  - **Trigger blocks**: Retrieve the content of the event that triggered execution. A trigger block should match the triggering event type. Typically, use only one trigger block per flow definition.
  - **Function blocks**: Interact with external systems (e.g. test.guide) or files.
  - **Control flow blocks**: e.g. `BatchProcessing` (run a sub-flow for each item of a list), `ConditionalSkip` (skip dependent blocks based on a condition).
  - **User code blocks**: e.g. `GenericUserCode` (user-defined action), `UserLink` (add a custom link for flow task reporting in test.guide).
- Where to look things up:
  - This skill’s snippet library: `references/flow-kit-snippets.code-snippets`

## 3. Adding blocks to the flow definition: `FlowBuilder.add_block_with`

- Add blocks by using the `add_block_with` method of the `FlowBuilder`.
- Each `.add_block_with(...)` typically contains:
  - a **block instance** (optionally assigned to a variable using the walrus operator)
  - 0..n `Assign(...)` statements (parameter assignments)
  - optional `result_alias="alias"` (to reference the result in `to_user_expression(...)`)
  - optional `required_blocks=[...]` (explicit dependencies / execution order control)

### 3.1 Definition of the block

- Select the block you want to use by importing and instantiating it:
  - `from flow_kit.library... import SomeBlock`
  - `SomeBlock()` or `SomeBlock(...constructor args...)`

### 3.2 Explicit connections between blocks: `required_blocks`

- Often it is necessary that blocks run in a specific order. You can achieve this by setting required blocks.
- If block B has block A in `required_blocks`, then A must be executed before B.
- Practical tips:
  - Keep a reference to the upstream block using the walrus operator:
    - `trigger_block := SomeTrigger()`
  - Dependencies can be explicit (`required_blocks`) or implicit via parameter assignments (see next section).

### 3.3 Assigning values to block parameters: `Assign(...)`

- Most blocks have parameters (required/optional). In order to use a block you must assign values to at least all required parameters.
- General form:

```py
Assign(<parameter identifier>).to_<value source>(<value source parameter>)
```

- In general there are three common value sources:

#### 3.3.1 `to_static_value(value)`

- Use for immutable values, e.g.:

```py
Assign(SomeBlock.PAR__X).to_static_value("abc-15")
```

#### 3.3.2 `to_block_result(block)`

- Use when the result of another block is used directly, e.g.:

```py
Assign(SomeBlock.PAR__X).to_block_result(upstream_block)
```

- Blocks whose result is used directly with `to_block_result` are implicitly added as required blocks.

#### 3.3.3 `to_user_expression("expr")`

- Use to define a value with a Python user expression, e.g. if only one attribute of a result object should be used.
  - Example: `"event.artifact_id"`
- Practical guidance:
  - Keep expressions simple. For more complex value conversion, insert a `GenericUserCode` block.
  - To use block results in a user expression, set a `result_alias` on the upstream block and reference it via `alias.xxx`.
  - Blocks whose results are used in a `to_user_expression` are implicitly required.

## 4. Defining a human-readable label: `.with_label()`

- To add a human-readable label for reporting/visualization, use `.with_label()`:
  - `SomeBlock().with_label("Human readable label")`

## 5. Type Checking

- The interface of a block is fully typed and flow.kit performs strong type checking between blocks.
- Type checking is done during validation and execution.

## 6. Environment variables (ResourceAdapter)

- The following environment variables are available during execution via the ResourceAdapter (examples):
  - `TT_RUN_IN_FLOW_AUTOMATION`: Always `True` to indicate flow.kit is executed via ResourceAdapter
  - `TT_FLOW_TASK_ID`: ID of the currently executed flow task
  - `TT_FLOW_TEMP_DIR`: Directory for temporary files in the ResourceAdapter environment

## 7. Special blocks

### 7.1 `GenericUserCode`

- For functionality not provided by flow.kit, a `GenericUserCode` block is advisable.
- Implement the action as a Python function with full type annotations.
- Assign values to the function parameters like for any other block: use `Assign("<param_name>")...` where `"<param_name>"` is the function parameter name.
- The block can be used like every other block, including full support of type checking and validation.

### 7.2 `ConditionalSkip`

- Use to skip parts or even the complete flow definition based on a condition.
- Provide the skip condition using `ConditionalSkip.PAR__SKIP`:
  - If it evaluates to `True`, the block state is set to `SKIPPED` and all dependent blocks (direct and indirect) are not executed and become `SKIPPED`.
- If possible, prefer using filter conditions on the flow trigger instead of `ConditionalSkip` blocks inside the flow definition (stops earlier and saves execution time on runners).

### 7.3 `BatchProcessing`

- Use when a loop over a list of objects is needed. A defined inner flow is executed once for every item in the list.
- Key points:
  - `BatchProcessing.PAR__LIST`: input list
  - `BatchProcessing(..., out_block=<inner block>)`: defines the block in the inner flow whose result is collected; the block returns a list of `out_block` results (one per iteration)
  - The inner flow has two additional value sources for `Assign()`:
    - `to_batch_item()`: single item from the list provided via `PAR__LIST`
    - `to_flow_parameter("<name>")`: parameter passed from the outer flow and available in all iterations
- Constraint: at least one parameter of the inner flow needs to be assigned to `to_batch_item()`.
- Full example: `examples/batch_processing_usage.py`.
