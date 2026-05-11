---
name: ecu-test-data-structures
description: Use when resolving ecu.test complex data structures referenced by other APIs, including variable ByteStream, BitStream, Vector, Matrix, Curve, Map, structured signals, bus CAN/FlexRay/LIN/Ethernet objects, diagnostics result objects, media image/audio/OCR objects, DLT messages, or version-specific 2024.3/2026.1 data structure migrations.
---

# ecu.test Data Structures

## Scope

Use this skill for ecu.test data structure reference work. These pages define complex values and advanced object properties used by other ecu.test APIs.

- Execution environment: internal reference. These docs describe data shapes and object properties; they are not a standalone execution API.
- Covered areas: package variable structures, bus objects, diagnostics objects, media objects, and DLT logging objects.
- Supported target versions: `ecu.test 2024.3` and `ecu.test 2026.1`.

Use the calling API skill as well when generating executable code. For example, combine this skill with Object API, User Utility API, Internal API, Tools API, or Trace Analysis API depending on where the data structure is used.

## Version Routing

Always identify the target version before describing structures or generating code.

1. If the user explicitly names `2024.3`, use only the 2024.3 data-structure docs for generated code or structure descriptions.
2. If the user explicitly names `2026.1`, use only the 2026.1 data-structure docs for generated code or structure descriptions.
3. If the user does not specify a version, default to `2026.1` and state that default in the response.
4. For migration or downgrade tasks, read both versions: first the source version, then the target version.
5. If an attribute name, constructor, element type, nested field, bus protocol detail, diagnostic result field, media field, DLT field, or trace-analysis variant is uncertain, check the target-version docs before using it.
6. Label generated or modified examples as applying to `ecu.test 2024.3` or `ecu.test 2026.1`.

Similarity between 2024.3 and 2026.1 is not a compatibility guarantee. Do not infer compatibility from memory.

## Bundled Authoritative Docs

Read these files from this skill directory. They are copied into the skill and are the source of truth for this skill.

| Area | 2024.3 path | 2026.1 path |
|---|---|---|
| Variable structures | `references/2024.3/general_api/variabledatastructures.md` | `references/2026.1/general_api/variabledatastructures.md` |
| Bus structures | `references/2024.3/general_api/busdatastructures.md` | `references/2026.1/general_api/busdatastructures.md` |
| Bus attribute protocol notes | `references/2024.3/general_api/busdatastructures_attr_proto.md` | `references/2026.1/general_api/busdatastructures_attr_proto.md` |
| Bus trace-analysis structures | included in 2024.3 `busdatastructures.md` | `references/2026.1/general_api/busdatastructuresTraceanalysis.md` |
| Diagnostics structures | `references/2024.3/general_api/diagdatastructures.md` | `references/2026.1/general_api/diagdatastructures.md` |
| Diagnostics trace-analysis structures | included in 2024.3 `diagdatastructures.md` when present | `references/2026.1/general_api/diagdatastructuresTraceanalysis.md` |
| Media structures | `references/2024.3/general_api/mediadatastructures.md` | `references/2026.1/general_api/mediadatastructures.md` |
| DLT structures | `references/2024.3/general_api/dltdatastructures.md` | `references/2026.1/general_api/dltdatastructures.md` |

## Required Workflow

For structure lookup:

1. Determine the target version. Default to `2026.1` if unspecified.
2. Identify the structure family from the user's task.
3. Read the target version's matching document before stating fields, methods, constructors, or behavior.
4. If the structure appears inside a code example, also read the calling API skill docs for the execution environment.
5. Explain only the confirmed target-version shape and call out anything not confirmed.

For migrations:

1. Identify the direction: `2024.3 -> 2026.1` or `2026.1 -> 2024.3`.
2. Read the source-version document that defines the current structure.
3. Read the target-version document that defines the target structure.
4. Compare attribute names, nesting, value types, enumerations, protocol-specific variants, and trace-analysis split files.
5. Preserve business semantics and update only the data shape and API integration points that differ.

## Structure Family Selection

| User need | Read first |
|---|---|
| `ByteStream`, `BitStream`, `Vector`, `Matrix`, `Curve`, `Map`, `EnumDefinition`, `EnumValue`, `StructuredSignal`, `Inbox`, `Outbox` | `variabledatastructures.md` |
| CAN, FlexRay, LIN, Ethernet bus objects, frames, PDUs, signals, signal groups, protocol attributes | `busdatastructures.md` and `busdatastructures_attr_proto.md` |
| Bus objects used inside trace analysis templates or trace analysis APIs | 2024.3: `busdatastructures.md`; 2026.1: `busdatastructuresTraceanalysis.md` |
| UDS, KWP2000, J1939 diagnostic result objects | `diagdatastructures.md` |
| Diagnostic objects used inside trace analysis | 2024.3: `diagdatastructures.md`; 2026.1: `diagdatastructuresTraceanalysis.md` |
| `Image`, `Mask`, `Frame`, `OCRService`, `TextMatch`, `ImageMatch`, `MatchList`, `AudioBlock` | `mediadatastructures.md` |
| DLT logging message objects | `dltdatastructures.md` |

## Implementation Checks

Before finalizing an answer or code snippet, verify these against the target-version docs:

- Exact class or structure name and capitalization.
- Required and optional fields, including nested objects and list element types.
- Whether the structure belongs to general API usage or trace-analysis-specific usage.
- Protocol-specific differences for CAN, FlexRay, LIN, Ethernet, UDS, KWP2000, J1939, media, and DLT.
- Whether 2026.1 split a topic into a separate trace-analysis document while 2024.3 kept it in a combined document.
- Whether the calling API expects object instances, dictionaries, attribute access, getter/setter calls, or serialized values.

## Search Hints

Use targeted searches before loading large files:

```powershell
Select-String -Path 'references\2026.1\general_api\variabledatastructures.md' -Pattern 'ByteStream|BitStream|Vector|Matrix|Curve|Map|StructuredSignal|Inbox|Outbox'
Select-String -Path 'references\2026.1\general_api\busdatastructures*.md' -Pattern 'CAN|FlexRay|LIN|Ethernet|Frame|PDU|Signal|Trace'
Select-String -Path 'references\2026.1\general_api\diagdatastructures*.md' -Pattern 'UDS|KWP2000|J1939|DTC|Result'
Select-String -Path 'references\2026.1\general_api\mediadatastructures.md' -Pattern 'Image|Mask|Frame|OCRService|TextMatch|ImageMatch|AudioBlock'
Select-String -Path 'references\2026.1\general_api\dltdatastructures.md' -Pattern 'DLT|message|payload|timestamp'
```

Adjust the version path to match the requested target.

## Common Mistakes

- Treating this as an executable API skill. It is a reference skill; pair it with the API that creates, reads, or mutates the structure.
- Defaulting silently. If no version is specified, state that `2026.1` was used.
- Migrating from memory. Read both source and target docs.
- Using 2026.1 trace-analysis split files for a 2024.3 answer without checking the 2024.3 combined document.
- Assuming bus, diagnostics, media, or DLT structures share the same shape across execution environments.
- Guessing nested field names or value types from examples in a different version.

## Related Skills

- `ecu-test-object-api`: use when external `ApiClient` code reads or writes objects that contain these structures.
- `ecu-test-internal-api`: use when internal ecu.test code accesses these structures through internal APIs.
- `ecu-test-user-utility-api`: use when a utility receives, transforms, or reports complex variable or bus structures.
- `ecu-test-tools-api`: use when User Tool, Model-based Bus Port, or Tool Adapter code uses bus, media, or diagnostics structures.
- `ecu-test-trace-analysis-api`: use for trace analysis templates and trace-analysis-specific bus or diagnostics structures.
- `ecu-test-report-api`: use when report parser objects contain media, diagnostics, bus, or DLT data.
