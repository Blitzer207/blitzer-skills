[![logo](res/flow.svg)](index.html "flow.kit documentation") flow.kit documentation

[ Home ](index.md)

Help contents

Help contents

[ Introduction ](introduction.md)

[ Setup IDE ](setup_ide.md)

How to build a flow definition [ How to build a flow definition ](how_to_build_a_flow_definition.md)

Table of contents

- [ Block library and documentation ](#block-library-and-documentation)
- [ Adding blocks to flow definition ](#adding-blocks-to-flow-definition)
  - [ Definition of the block ](#definition-of-the-block)
  - [ Explicit connections between blocks ](#explicit-connections-between-blocks)
  - [ Assigning values to the parameters of a block ](#assigning-values-to-the-parameters-of-a-block)
    - [ to_static_value(\<value\>) ](#to_static_valuevalue)
    - [ to_block_result(\<block object\>) ](#to_block_resultblock-object)
    - [ to_user_expression("\<user expression\>") ](#to_user_expressionuser-expression)
  - [ Defining a human-readable label for the block ](#defining-a-human-readable-label-for-the-block)
- [ Type Checking ](#type-checking)
- [ Environment variables ](#environment-variables)
- [ Special blocks ](#special-blocks)
  - [ GenericUserCode block ](#genericusercode-block)
  - [ ConditionalSkip block ](#conditionalskip-block)
  - [ BatchProcessing block ](#batchprocessing-block)

[ Validate, execute and visualize your flow definition ](validate_execute_visualize.md)

[ Python environment ](python_environment.md)

[ Proxy configuration ](proxy.md)

[ Retries configuration ](retries.md)

Block documentation

Block documentation

[ control_flow ](Block%20documentation/flow_kit.library.control_flow.md)

[ ecu_test ](Block%20documentation/flow_kit.library.ecu_test.md)

[ environment ](Block%20documentation/flow_kit.library.environment.md)

[ file_operation ](Block%20documentation/flow_kit.library.file_operation.md)

[ test_guide ](Block%20documentation/test_guide/index.md)

test_guide

- [ artifacts ](Block%20documentation/test_guide/flow_kit.library.test_guide.artifacts.md)
- [ execution ](Block%20documentation/test_guide/flow_kit.library.test_guide.execution.md)
- [ flow ](Block%20documentation/test_guide/flow_kit.library.test_guide.flow.md)
- [ platform ](Block%20documentation/test_guide/flow_kit.library.test_guide.platform.md)
- [ q_gates ](Block%20documentation/test_guide/flow_kit.library.test_guide.q_gates.md)
- [ releases ](Block%20documentation/test_guide/flow_kit.library.test_guide.releases.md)
- [ report_mgmt ](Block%20documentation/test_guide/flow_kit.library.test_guide.report_mgmt.md)
- [ reporting ](Block%20documentation/test_guide/flow_kit.library.test_guide.reporting.md)
- [ test_infrastructure ](Block%20documentation/test_guide/flow_kit.library.test_guide.test_infrastructure.md)
- [ user_mgmt ](Block%20documentation/test_guide/flow_kit.library.test_guide.user_mgmt.md)

tools

tools

[ codebeamer ](Block%20documentation/tools/codebeamer/index.md)

codebeamer

- [ association ](Block%20documentation/tools/codebeamer/flow_kit.library.tools.codebeamer.association.md)
- [ attachment ](Block%20documentation/tools/codebeamer/flow_kit.library.tools.codebeamer.attachment.md)
- [ background_job ](Block%20documentation/tools/codebeamer/flow_kit.library.tools.codebeamer.background_job.md)
- [ baseline ](Block%20documentation/tools/codebeamer/flow_kit.library.tools.codebeamer.baseline.md)
- [ branches ](Block%20documentation/tools/codebeamer/flow_kit.library.tools.codebeamer.branches.md)
- [ export ](Block%20documentation/tools/codebeamer/flow_kit.library.tools.codebeamer.export.md)
- [ group ](Block%20documentation/tools/codebeamer/flow_kit.library.tools.codebeamer.group.md)
- [ migration ](Block%20documentation/tools/codebeamer/flow_kit.library.tools.codebeamer.migration.md)
- [ project ](Block%20documentation/tools/codebeamer/flow_kit.library.tools.codebeamer.project.md)
- [ report ](Block%20documentation/tools/codebeamer/flow_kit.library.tools.codebeamer.report.md)
- [ repository_item ](Block%20documentation/tools/codebeamer/flow_kit.library.tools.codebeamer.repository_item.md)
- [ role ](Block%20documentation/tools/codebeamer/flow_kit.library.tools.codebeamer.role.md)
- [ system ](Block%20documentation/tools/codebeamer/flow_kit.library.tools.codebeamer.system.md)
- [ test_management ](Block%20documentation/tools/codebeamer/flow_kit.library.tools.codebeamer.test_management.md)
- [ test_run ](Block%20documentation/tools/codebeamer/flow_kit.library.tools.codebeamer.test_run.md)
- [ traceability ](Block%20documentation/tools/codebeamer/flow_kit.library.tools.codebeamer.traceability.md)
- [ tracker ](Block%20documentation/tools/codebeamer/flow_kit.library.tools.codebeamer.tracker.md)
- [ tracker_item ](Block%20documentation/tools/codebeamer/flow_kit.library.tools.codebeamer.tracker_item.md)
- [ tracker_item_move ](Block%20documentation/tools/codebeamer/flow_kit.library.tools.codebeamer.tracker_item_move.md)
- [ tracker_items_attachment ](Block%20documentation/tools/codebeamer/flow_kit.library.tools.codebeamer.tracker_items_attachment.md)
- [ tracker_items_comment ](Block%20documentation/tools/codebeamer/flow_kit.library.tools.codebeamer.tracker_items_comment.md)
- [ tracker_permission ](Block%20documentation/tools/codebeamer/flow_kit.library.tools.codebeamer.tracker_permission.md)
- [ tracker_report ](Block%20documentation/tools/codebeamer/flow_kit.library.tools.codebeamer.tracker_report.md)
- [ tracker_tree ](Block%20documentation/tools/codebeamer/flow_kit.library.tools.codebeamer.tracker_tree.md)
- [ user ](Block%20documentation/tools/codebeamer/flow_kit.library.tools.codebeamer.user.md)
- [ wiki ](Block%20documentation/tools/codebeamer/flow_kit.library.tools.codebeamer.wiki.md)
- [ wikis_comment ](Block%20documentation/tools/codebeamer/flow_kit.library.tools.codebeamer.wikis_comment.md)
- [ working_set ](Block%20documentation/tools/codebeamer/flow_kit.library.tools.codebeamer.working_set.md)
- [ working_set_permission ](Block%20documentation/tools/codebeamer/flow_kit.library.tools.codebeamer.working_set_permission.md)

[ etm ](Block%20documentation/tools/etm/index.md)

etm

- [ attachment ](Block%20documentation/tools/etm/flow_kit.library.tools.etm.attachment.md)
- [ baseline ](Block%20documentation/tools/etm/flow_kit.library.tools.etm.baseline.md)
- [ builddefinition ](Block%20documentation/tools/etm/flow_kit.library.tools.etm.builddefinition.md)
- [ buildrecord ](Block%20documentation/tools/etm/flow_kit.library.tools.etm.buildrecord.md)
- [ catalog ](Block%20documentation/tools/etm/flow_kit.library.tools.etm.catalog.md)
- [ category ](Block%20documentation/tools/etm/flow_kit.library.tools.etm.category.md)
- [ categorytype ](Block%20documentation/tools/etm/flow_kit.library.tools.etm.categorytype.md)
- [ channel ](Block%20documentation/tools/etm/flow_kit.library.tools.etm.channel.md)
- [ component ](Block%20documentation/tools/etm/flow_kit.library.tools.etm.component.md)
- [ configuration ](Block%20documentation/tools/etm/flow_kit.library.tools.etm.configuration.md)
- [ contributor ](Block%20documentation/tools/etm/flow_kit.library.tools.etm.contributor.md)
- [ customattribute ](Block%20documentation/tools/etm/flow_kit.library.tools.etm.customattribute.md)
- [ datapool ](Block%20documentation/tools/etm/flow_kit.library.tools.etm.datapool.md)
- [ executionelementresult ](Block%20documentation/tools/etm/flow_kit.library.tools.etm.executionelementresult.md)
- [ executionresult ](Block%20documentation/tools/etm/flow_kit.library.tools.etm.executionresult.md)
- [ executionscript ](Block%20documentation/tools/etm/flow_kit.library.tools.etm.executionscript.md)
- [ executionsequence ](Block%20documentation/tools/etm/flow_kit.library.tools.etm.executionsequence.md)
- [ executionsequenceresult ](Block%20documentation/tools/etm/flow_kit.library.tools.etm.executionsequenceresult.md)
- [ executionvariable ](Block%20documentation/tools/etm/flow_kit.library.tools.etm.executionvariable.md)
- [ executionvariablevalue ](Block%20documentation/tools/etm/flow_kit.library.tools.etm.executionvariablevalue.md)
- [ executionworkitem ](Block%20documentation/tools/etm/flow_kit.library.tools.etm.executionworkitem.md)
- [ job ](Block%20documentation/tools/etm/flow_kit.library.tools.etm.job.md)
- [ jobresult ](Block%20documentation/tools/etm/flow_kit.library.tools.etm.jobresult.md)
- [ jobscheduler ](Block%20documentation/tools/etm/flow_kit.library.tools.etm.jobscheduler.md)
- [ keyword ](Block%20documentation/tools/etm/flow_kit.library.tools.etm.keyword.md)
- [ labresource ](Block%20documentation/tools/etm/flow_kit.library.tools.etm.labresource.md)
- [ labresourceattribute ](Block%20documentation/tools/etm/flow_kit.library.tools.etm.labresourceattribute.md)
- [ objective ](Block%20documentation/tools/etm/flow_kit.library.tools.etm.objective.md)
- [ project ](Block%20documentation/tools/etm/flow_kit.library.tools.etm.project.md)
- [ remotescript ](Block%20documentation/tools/etm/flow_kit.library.tools.etm.remotescript.md)
- [ request ](Block%20documentation/tools/etm/flow_kit.library.tools.etm.request.md)
- [ requirement ](Block%20documentation/tools/etm/flow_kit.library.tools.etm.requirement.md)
- [ reservation ](Block%20documentation/tools/etm/flow_kit.library.tools.etm.reservation.md)
- [ resourcegroup ](Block%20documentation/tools/etm/flow_kit.library.tools.etm.resourcegroup.md)
- [ step ](Block%20documentation/tools/etm/flow_kit.library.tools.etm.step.md)
- [ stream ](Block%20documentation/tools/etm/flow_kit.library.tools.etm.stream.md)
- [ suiteexecutionrecord ](Block%20documentation/tools/etm/flow_kit.library.tools.etm.suiteexecutionrecord.md)
- [ tasks ](Block%20documentation/tools/etm/flow_kit.library.tools.etm.tasks.md)
- [ teamarea ](Block%20documentation/tools/etm/flow_kit.library.tools.etm.teamarea.md)
- [ template ](Block%20documentation/tools/etm/flow_kit.library.tools.etm.template.md)
- [ testcase ](Block%20documentation/tools/etm/flow_kit.library.tools.etm.testcase.md)
- [ testcell ](Block%20documentation/tools/etm/flow_kit.library.tools.etm.testcell.md)
- [ testphase ](Block%20documentation/tools/etm/flow_kit.library.tools.etm.testphase.md)
- [ testplan ](Block%20documentation/tools/etm/flow_kit.library.tools.etm.testplan.md)
- [ testscript ](Block%20documentation/tools/etm/flow_kit.library.tools.etm.testscript.md)
- [ testsuite ](Block%20documentation/tools/etm/flow_kit.library.tools.etm.testsuite.md)
- [ testsuitelog ](Block%20documentation/tools/etm/flow_kit.library.tools.etm.testsuitelog.md)
- [ tooladapter ](Block%20documentation/tools/etm/flow_kit.library.tools.etm.tooladapter.md)
- [ utility ](Block%20documentation/tools/etm/flow_kit.library.tools.etm.utility.md)

[ jama ](Block%20documentation/tools/jama/index.md)

jama

- [ abstractitems ](Block%20documentation/tools/jama/flow_kit.library.tools.jama.abstractitems.md)
- [ activities ](Block%20documentation/tools/jama/flow_kit.library.tools.jama.activities.md)
- [ attachments ](Block%20documentation/tools/jama/flow_kit.library.tools.jama.attachments.md)
- [ baselines ](Block%20documentation/tools/jama/flow_kit.library.tools.jama.baselines.md)
- [ categories ](Block%20documentation/tools/jama/flow_kit.library.tools.jama.categories.md)
- [ comments ](Block%20documentation/tools/jama/flow_kit.library.tools.jama.comments.md)
- [ files ](Block%20documentation/tools/jama/flow_kit.library.tools.jama.files.md)
- [ filters ](Block%20documentation/tools/jama/flow_kit.library.tools.jama.filters.md)
- [ items ](Block%20documentation/tools/jama/flow_kit.library.tools.jama.items.md)
- [ itemtypes ](Block%20documentation/tools/jama/flow_kit.library.tools.jama.itemtypes.md)
- [ picklistoptions ](Block%20documentation/tools/jama/flow_kit.library.tools.jama.picklistoptions.md)
- [ picklists ](Block%20documentation/tools/jama/flow_kit.library.tools.jama.picklists.md)
- [ projects ](Block%20documentation/tools/jama/flow_kit.library.tools.jama.projects.md)
- [ relationshiprulesets ](Block%20documentation/tools/jama/flow_kit.library.tools.jama.relationshiprulesets.md)
- [ relationships ](Block%20documentation/tools/jama/flow_kit.library.tools.jama.relationships.md)
- [ relationshiptypes ](Block%20documentation/tools/jama/flow_kit.library.tools.jama.relationshiptypes.md)
- [ releases ](Block%20documentation/tools/jama/flow_kit.library.tools.jama.releases.md)
- [ system ](Block%20documentation/tools/jama/flow_kit.library.tools.jama.system.md)
- [ tags ](Block%20documentation/tools/jama/flow_kit.library.tools.jama.tags.md)
- [ testcycles ](Block%20documentation/tools/jama/flow_kit.library.tools.jama.testcycles.md)
- [ testplans ](Block%20documentation/tools/jama/flow_kit.library.tools.jama.testplans.md)
- [ testruns ](Block%20documentation/tools/jama/flow_kit.library.tools.jama.testruns.md)
- [ usergroups ](Block%20documentation/tools/jama/flow_kit.library.tools.jama.usergroups.md)
- [ users ](Block%20documentation/tools/jama/flow_kit.library.tools.jama.users.md)

[ jira ](Block%20documentation/tools/flow_kit.library.tools.jira.md)

[ llm ](Block%20documentation/tools/flow_kit.library.tools.llm.md)

[ polarion ](Block%20documentation/tools/polarion/index.md)

polarion

- [ collections ](Block%20documentation/tools/polarion/flow_kit.library.tools.polarion.collections.md)
- [ document_attachments ](Block%20documentation/tools/polarion/flow_kit.library.tools.polarion.document_attachments.md)
- [ document_comments ](Block%20documentation/tools/polarion/flow_kit.library.tools.polarion.document_comments.md)
- [ document_parts ](Block%20documentation/tools/polarion/flow_kit.library.tools.polarion.document_parts.md)
- [ documents ](Block%20documentation/tools/polarion/flow_kit.library.tools.polarion.documents.md)
- [ enumerations ](Block%20documentation/tools/polarion/flow_kit.library.tools.polarion.enumerations.md)
- [ externally_linked_work_items ](Block%20documentation/tools/polarion/flow_kit.library.tools.polarion.externally_linked_work_items.md)
- [ feature_selections ](Block%20documentation/tools/polarion/flow_kit.library.tools.polarion.feature_selections.md)
- [ icons ](Block%20documentation/tools/polarion/flow_kit.library.tools.polarion.icons.md)
- [ jobs ](Block%20documentation/tools/polarion/flow_kit.library.tools.polarion.jobs.md)
- [ linked_oslc_resources ](Block%20documentation/tools/polarion/flow_kit.library.tools.polarion.linked_oslc_resources.md)
- [ linked_work_items ](Block%20documentation/tools/polarion/flow_kit.library.tools.polarion.linked_work_items.md)
- [ page_attachments ](Block%20documentation/tools/polarion/flow_kit.library.tools.polarion.page_attachments.md)
- [ pages ](Block%20documentation/tools/polarion/flow_kit.library.tools.polarion.pages.md)
- [ plans ](Block%20documentation/tools/polarion/flow_kit.library.tools.polarion.plans.md)
- [ project_templates ](Block%20documentation/tools/polarion/flow_kit.library.tools.polarion.project_templates.md)
- [ projects ](Block%20documentation/tools/polarion/flow_kit.library.tools.polarion.projects.md)
- [ revisions ](Block%20documentation/tools/polarion/flow_kit.library.tools.polarion.revisions.md)
- [ roles ](Block%20documentation/tools/polarion/flow_kit.library.tools.polarion.roles.md)
- [ test_record_attachments ](Block%20documentation/tools/polarion/flow_kit.library.tools.polarion.test_record_attachments.md)
- [ test_records ](Block%20documentation/tools/polarion/flow_kit.library.tools.polarion.test_records.md)
- [ test_run_attachments ](Block%20documentation/tools/polarion/flow_kit.library.tools.polarion.test_run_attachments.md)
- [ test_run_comments ](Block%20documentation/tools/polarion/flow_kit.library.tools.polarion.test_run_comments.md)
- [ test_runs ](Block%20documentation/tools/polarion/flow_kit.library.tools.polarion.test_runs.md)
- [ test_step_result_attachments ](Block%20documentation/tools/polarion/flow_kit.library.tools.polarion.test_step_result_attachments.md)
- [ test_step_results ](Block%20documentation/tools/polarion/flow_kit.library.tools.polarion.test_step_results.md)
- [ test_steps ](Block%20documentation/tools/polarion/flow_kit.library.tools.polarion.test_steps.md)
- [ user_groups ](Block%20documentation/tools/polarion/flow_kit.library.tools.polarion.user_groups.md)
- [ users ](Block%20documentation/tools/polarion/flow_kit.library.tools.polarion.users.md)
- [ work_item_approvals ](Block%20documentation/tools/polarion/flow_kit.library.tools.polarion.work_item_approvals.md)
- [ work_item_attachments ](Block%20documentation/tools/polarion/flow_kit.library.tools.polarion.work_item_attachments.md)
- [ work_item_comments ](Block%20documentation/tools/polarion/flow_kit.library.tools.polarion.work_item_comments.md)
- [ work_item_work_records ](Block%20documentation/tools/polarion/flow_kit.library.tools.polarion.work_item_work_records.md)
- [ work_items ](Block%20documentation/tools/polarion/flow_kit.library.tools.polarion.work_items.md)

[ trigger ](Block%20documentation/flow_kit.library.trigger.md)

[ user_code ](Block%20documentation/flow_kit.library.user_code.md)

Table of contents

- [ Block library and documentation ](#block-library-and-documentation)
- [ Adding blocks to flow definition ](#adding-blocks-to-flow-definition)
  - [ Definition of the block ](#definition-of-the-block)
  - [ Explicit connections between blocks ](#explicit-connections-between-blocks)
  - [ Assigning values to the parameters of a block ](#assigning-values-to-the-parameters-of-a-block)
    - [ to_static_value(\<value\>) ](#to_static_valuevalue)
    - [ to_block_result(\<block object\>) ](#to_block_resultblock-object)
    - [ to_user_expression("\<user expression\>") ](#to_user_expressionuser-expression)
  - [ Defining a human-readable label for the block ](#defining-a-human-readable-label-for-the-block)
- [ Type Checking ](#type-checking)
- [ Environment variables ](#environment-variables)
- [ Special blocks ](#special-blocks)
  - [ GenericUserCode block ](#genericusercode-block)
  - [ ConditionalSkip block ](#conditionalskip-block)
  - [ BatchProcessing block ](#batchprocessing-block)

# How to build a flow definition

The `flow_definition.py` holds the implementation of the workflow. The starting point of each implementation is the `get_flow()` function with the `FlowBuilder`. The minimal implementation for `get_flow()` with an empty workflow is the following:

    def get_flow() -> Flow:
        """Define the flow to be executed."""
        return (
            FlowBuilder()
            .build()
        )

## Block library and documentation

The block documentation gives you a good overview of which blocks exist in the flow.kit. This documentation contains all available blocks for building flow definitions. There are different types of blocks:

- Trigger blocks
  - These blocks retrieve the content of the event that triggered the execution of the flow bundle. As the content of the triggering event is event type specific a trigger block needs to match the triggering event.
  - Despite not being mandatory a trigger block is often the start point of a flow definition.
  - As flow definitions should be specific to a trigger only one trigger block per flow definition should be used.
- Function blocks to interact with
  - test.guide
  - files
  - Jira
  - ecu.test
- Control flow blocks
  - [`BatchProcessing`](Block%20documentation/flow_kit.library.control_flow.md#batchprocessing)
    - Running a given sub flow implementation for every item of a list.
  - [`ConditionalSkip`](Block%20documentation/flow_kit.library.control_flow.md#conditionalskip)
    - Skips depending blocks depending on a condition.
- User code blocks
  - [`GenericUserCode`](Block%20documentation/flow_kit.library.user_code.md#genericusercode)
    - Block with user-defined action.
  - [`UserLink`](Block%20documentation/flow_kit.library.user_code.md#userlink)
    - Add a custom link for display of flow task report in test.guide.

The block documentation can be found in this documentation under **Block documentation**.

Example entry in the block documentation

## GetArtifact (1)

1.  class name of the block

Module path: `flow_kit.library.test_guide.artifacts.GetArtifact` (1)

1.  path to the module to import the block

> test.guide ArtifactsApi: Get all information of an artifact. (1)

1.  short description of the action of the block

**Parameter:** (1)

1.  list of parameters of the block
    - shows name, type, additional information (optional, default value) and description.

- GetArtifact.**PAR\_\_ARTIFACT_ID**

  - type: `str`
  - ID of the artifact

- GetArtifact.**PAR\_\_TG_CONFIG**

  - type: `flow_kit.tools.test_guide.test_guide_config.TestGuideConfig`

  - optional, default = `None`

  - Config for connection to test.guide. If left unspecified, a default config will be used, containing the tes .guide url and project ID of the ResourceAdapter as well as an authentication key of the user specified on the flow trigger. A custom test.guide config can be created by block TGInit.

**Returns:** (1)

1.  Description and type of returned data including the Python module path to import from the flow.kit source in your flow definition.

> The artifact object.

**Return type:**

> `tg_api_clients.artifacts.models.artifact.Artifact`

(1)

1.  code snippet for adding the block to the flow definition
    - the code block features a copy button in the top right corner.

.add_block_with(...) snippet

        # from flow_kit.library.test_guide.artifacts import GetArtifact  # TODO: move import to top of this file if needed
        .add_block_with(
            block_name := GetArtifact().with_label('Your label here'),  # TODO: change block_name  # TODO: set label 
            Assign(GetArtifact.PAR__ARTIFACT_ID).to_,  # TODO: assign parameter (type: str)
           # optional parameter: Assign(GetArtifact.PAR__TG_CONFIG).to_,  # TODO: assign parameter if needed (type: flow_kit.tools.test_guide.test_guide_config.TestGuideConfig)
           # result_alias='alias_name',  # TODO: uncomment and change alias_name if needed
            # required_blocks=[],  # TODO: uncomment and add required blocks here if needed
            # block returns type tg_api_clients.artifacts.models.artifact.Artifact
        )

## Adding blocks to flow definition

Blocks are added by using the `add_block_with` method of the `FlowBuilder`. The following example shows a simple flow with two blocks. The elements of this example are explained step by step below.

    from flow_kit.library.test_guide.artifacts import GetArtifact

    def get_flow() -> Flow:
        """Define the flow to be executed."""
        return (
            FlowBuilder()
            .add_block_with(
                trigger_block := ArtifactUploadedTrigger(),
                result_alias = "event"
            )
            .add_block_with(
                GetArtifact().with_label("Retrieve the artifact information."),
                Assign(GetArtifact.PAR__ARTIFACT_ID)
                    .to_user_expression("event.artifact_id"),
                required_blocks=[trigger_block]
            )
            .build()
        )

To describe the usage of `add_block_with` we focus on the second block in the example. This has the following elements:

### Definition of the block

You select the block you want to use by importing and instantiating it:

    from flow_kit.library.test_guide.artifacts import GetArtifact
    # (1)!

    def get_flow() -> Flow:
        """Define the flow to be executed."""
        return (
            FlowBuilder()
            .add_block_with(
                trigger_block := ArtifactUploadedTrigger(),
                result_alias = "event"
            )
            .add_block_with(
                GetArtifact().with_label("Retrieve the artifact information."), 
                # (2)!
                Assign(GetArtifact.PAR__ARTIFACT_ID).to_user_expression("event.artifact_id"),
                required_blocks=[trigger_block]
            )
            .build()
        )

1.  Import of the block from the flow.kit library.
2.  Instantiation of a `GetArtifact` block.

### Explicit connections between blocks

Often it is necessary that blocks are run in a specific order. You can achieve this with dependencies between blocks by setting required blocks. If you set a block (block A) as required block of another block (block B) it means that block A needs to be run before block B. To set required blocks you use the attribute `required_blocks`. In order to have a reference to the block instance you want to depend on you can use the walrus operator (see example below).

In the example the `ArtifactUploadedTrigger` block is a required block for the `GetArtifact` block. Thus the `ArtifactUploadedTrigger` block needs to be run before the `GetArtifact` block:

    from flow_kit.library.test_guide.artifacts import GetArtifact

    def get_flow() -> Flow:
        """Define the flow to be executed."""
        return (
            FlowBuilder()
            .add_block_with(
                trigger_block := ArtifactUploadedTrigger(),
                # (1)!
                result_alias = "event"
            )
            .add_block_with(
                GetArtifact().with_label("Retrieve the artifact information."),
                Assign(GetArtifact.PAR__ARTIFACT_ID).to_user_expression("event.artifact_id"),
                required_blocks=[trigger_block] 
                # (2)!
            )
            .build()
        )

1.  The block instance is assigned to a variable using the walrus operator.
2.  Explicit block requirement with `required_blocks` to be able to use the result value in the user expression assignment.

Info

If you use the Assign value sources `to_block_result` or `to_user_expression` dependencies in form of required blocks are added implicitly for every referenced block result (see Assigning values to the parameters of a block).

### Assigning values to the parameters of a block

Most flow blocks have parameters to alter their behaviour. You can see the parameters of a block and their parameter identifiers in the block documentation. Parameters can be required or optional. In order to use the block you need to assign values to at least all required parameters. To assign values you use the `Assign()` class which is used in the following form:

    Assign(<parameter identifier>).to_<type of value source>(<parameter of value source>)

By using `Assign()` instances we assign a parameter defined by its identifier to a value source. In general there are three different value sources:

#### `to_static_value(<value>)`

Used for immutable values, e.g.:

    Assign(GetArtifact.PAR__ARTIFACT_ID).to_static_value("abc-15")

#### `to_block_result(<block object>)`

Used when the result of another block is used directly, e.g.:

    Assign(GetArtifact.PAR__ARTIFACT_ID).to_block_result(trigger_block)

Info

Blocks whose result is used directly with `to_block_result` are implicitly added as a required block.

#### `to_user_expression("<user expression>")`

Used to define a value with a Python user expression, e. g. if only one attribute of a block result object should be used ("trigger.id" for the result "trigger").

Tip

This method should only be used for simple modifications or access of fields of the result object. For more complicated value conversion, we advise to use a GenericUserCode block in between.

To use block results in a user expression for the value assignment of another block a `result_alias` needs to be added to the used block result.

Info

Blocks whose results that are used in a user expression with `to_user_expression` are implicitly added as required blocks.

The following example highlights the usage in the example:

    from flow_kit.library.test_guide.artifacts import GetArtifact

    def get_flow() -> Flow:
        """Define the flow to be executed."""
        return (
            FlowBuilder()
            .add_block_with(
                trigger_block := ArtifactUploadedTrigger(),
                result_alias = "event"
                # (1)!
            )
            .add_block_with(
                GetArtifact().with_label("Retrieve the artifact information."),
                Assign(GetArtifact.PAR__ARTIFACT_ID).to_user_expression("event.artifact_id"),
                # (2)!
            )
            .build()
        )

1.  Adding an alias for the block result for later usage in the value source `to_user_expression`.
2.  Creating the user expression using the previously defined result alias.

Danger

Expressions in `to_user_expression` will only be evaluated during runtime. As a result **validate** will not hint to errors in the user expression or a potential type mismatch.

**Specific value_sources inside flow in `BatchProcessing`**

For blocks inside the inner flow of a `BatchProcessing` block there are 2 additional possible value sources:

- `to_batch_item()`
- `to_flow_parameter(<name of the parameter>)`

Please refer to the description in the section `BatchProcessing` block.

### Defining a human-readable label for the block

To add a human-readable label for the report you can use `.with_label()`:

    from flow_kit.library.test_guide.artifacts import GetArtifact

    def get_flow() -> Flow:
        """Define the flow to be executed."""
        return (
            FlowBuilder()
            .add_block_with(
                trigger_block := ArtifactUploadedTrigger(),
                result_alias = "event"
            )
            .add_block_with(
                GetArtifact().with_label("Retrieve the artifact information."),
                Assign(GetArtifact.PAR__ARTIFACT_ID).to_user_expression("event.artifact_id"),
                required_blocks=[trigger_block]
            )
            .build()
        )

## Type Checking

The interface of a block is fully typed and the flow.kit has a strong type checking between blocks. This design decision allows for early failure detection and the user knows at every point in the flow definition what type and interface the specific object has.

Type checking is done during validation and execution of the flow definition.

## Environment variables

The following environment variables are available during the execution of flow.kit via the ResourceAdapter.

[TABLE]

## Special blocks

### GenericUserCode block

For all functionality not provided by the flow.kit, a `GenericUserCode` block is advisable. This block is special as the user implements the interface and action of the block.

The following listing shows an example using a `GenericUserCode` block to convert data between two block:

    def get_artifact_id(event: ArtifactUploadedFlowTriggerPayload) -> str:
        """Get the artifact id of an ArtifactUploadedEvent."""
        return event.artifact_id
        # (1)!

    def get_flow() -> Flow:
        """Define the flow to be executed."""
        return (
            FlowBuilder()
            .add_block_with(
                trigger_block := ArtifactUploadedTrigger()
            )
            .add_block_with(
                user_block := GenericUserCode(get_artifact_id).with_label("Get artifact from event."),  
                # (2)!
                Assign("event").to_block_result(trigger_block)
                # (3)!
            )
            .add_block_with(
                GetArtifact().with_label("Retrieve the artifact information."),
                Assign(GetArtifact.PAR__ARTIFACT_ID).to_block_result(user_block)
            )
            .build()
        )

1.  User function for the action of the block with parameter "event".
2.  Set the user function to the instance of the `GenericUserCode` block.
3.  Assign a value (here block result of the trigger block) to the parameter of the user function for the action.

You implement the action of the block as a Python function with full type annotations. Values for the parameters of that function need to be assigned with normal `Assign()` instances using the name of the parameters as parameter identifier.

The block can be used like every other block, including the full support of type checking and validation.

### ConditionalSkip block

The `ConditionalSkip` block is used to skip parts or even the complete flow definition based on a condition. The skip condition is provided using the parameter with identifier `PAR__SKIP`. If this parameter evaluates to True, the state of this block is set to SKIPPED which leads to every dependent block (direct and indirect) not being executed and getting the block state SKIPPED. See in chapter [Execution of flow definitions](introduction.md#skipped-behavior) for the behavior.

    .add_block_with(
        block_name := ConditionalSkip().with_label("Skip if condition is met."),
        Assign(ConditionalSkip.PAR__SKIP).to_<value source>(<parameter of source>)
    )

Tip

If possible you should prefer using filter conditions on the flow trigger instead of `ConditionalSkip` blocks inside your flow definition as runs skipped by filter conditions are stopped earlier and save execution time on your flow bundle runners.

### BatchProcessing block

In some use cases a loop over a list of objects is needed. To execute the same blocks in each loop run you can use the `BatchProcessing` block.

The following code block shows an example with the `BatchProcessing` block:

    .add_block_with(
        BatchProcessing(
            FlowBuilder()
            .add_block_with(
                inner_block := SomeBlock(),
                Assign(PAR__LIST_ITEM).to_batch_item(),
                Assign(PAR__SOME_OUTER_BLOCK).to_flow_parameter("outer_block")
            ).build(),
            out_block=inner_block 
        ).with_label("Loop over list"),
        Assign(BatchProcessing.PAR__LIST).to_<value source>(<parameter of source>),
        Assign("outer_block").to_<value source>(<parameter of source>)
    )

The action of the `BatchProcessing` block is customizable with a flow. The defined flow is then executed for each item in the list given in the parameter `PAR__LIST`.

The inner flow of a `BatchProcessing` block has two special value sources available for `Assign()`:

- `to_batch_item()`
  - Single item from the list given with the parameter `PAR__LIST`.
- `to_flow_parameter(<name of the parameter>)`
  - Parameters from outside the inner flow.
  - UseCase: Use block results from outside the inner flow.

Warning

A parameter of the inner flow of a `BatchProcessing` needs to be assigned to the value source `to_batch_item()`.

The BatchProcessing block returns a list of objects from the inner flow runs. The returned list contains the result value of the out_block from every iteration from every run of the inner flow. You define the out_block by setting the parameter out_block of the BatchProcessing block to the reference of the wanted block in the inner flow.

Note

Please also see the full example in the flow bundle in the path examples/batch_processing_usage.py.

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top

[](setup_ide.md)

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIwIDExdjJIOGw1LjUgNS41LTEuNDIgMS40Mkw0LjE2IDEybDcuOTItNy45MkwxMy41IDUuNSA4IDExeiIgLz48L3N2Zz4=)

Previous

Setup IDE

[](validate_execute_visualize.md)

Next

Validate, execute and visualize your flow definition

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTQgMTF2MmgxMmwtNS41IDUuNSAxLjQyIDEuNDJMMTkuODQgMTJsLTcuOTItNy45MkwxMC41IDUuNSAxNiAxMXoiIC8+PC9zdmc+)

Made with [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
