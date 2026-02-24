# ecu.test Object API Python Coding Standards

## 0) API entry points (internal vs object API)

### Internal API (inside ecu.test)
Use this for user code that runs inside ecu.test (e.g. function variables, utilities, expression controls).

Docs source (relative to `%ECU_TEST_HOME%`):
- <=2025.1 (RST): `Help\APIDoc\_sources\general_api\api.rst.txt`
- >=2025.2 (HTML): `Help\api\general_api\api.html`

```python
from tts.core.api.internalApi.Api import Api
api = Api()
```

### Internal API (external Python, optional)
If you need Internal API access from an external Python process, use the proxy shipped with the
process separation tutorial workspace:

`Templates\ExampleWorkspaces\Tutorial-ProcessSeparation\PythonPath\ApiProxy.py`

```python
from ApiProxy import ApiProxy

api = ApiProxy()

# internal API access
api.Project.Open(...)

# Object API access via api.ObjectApi
obj_api = api.ObjectApi
```

### Object API (file-based program API)
- Inside ecu.test: use `api.ObjectApi`
- External Python: add `%ECU_TEST_HOME%\Templates\ApiClient` to `PYTHONPATH`

Docs source (relative to `%ECU_TEST_HOME%`):
- <=2025.1 (RST): `Help\APIDoc\_sources\general_api\objectApi.rst.txt`
- >=2025.2 (HTML): `Help\api\general_api\objectApi.html`

```python
import os
import sys

api_client_dir = r"C:\Program Files\ecu.test 2024.3\Templates\ApiClient" # this MUST be replaced by the user
if not os.path.isdir(api_client_dir):
    raise RuntimeError(f"ApiClient path not found: {api_client_dir}")
sys.path.insert(0, api_client_dir)

from ApiClient import ApiClient  

api = ApiClient()
```

### Object API code examples (treat as canonical patterns)
Docs source (relative to `%ECU_TEST_HOME%`):
- <=2025.1 (RST): `Help\APIDoc\_sources\general_api\objectApiExamples.rst.txt`
- >=2025.2 (HTML): `Help\api\general_api\objectApiExamples.html`

If you are unsure about ordering, escaping, mapping setup, trace analysis composition, etc., prefer
these examples over guessing.

## 1) None checks for Create*/Get* (MUST)
**Mandatory:** Any `Create*` / `Get*` call can return `None`. Guard immediately and fail fast
*every time* you call them (not just below 2 examples).

```python
package = package_api.CreatePackage()
if package is None:
    raise RuntimeError("CreatePackage failed")

pre_block = package.GetPreconditionBlock()
if pre_block is None:
    raise RuntimeError("GetPreconditionBlock returned None")
```

## 3) Save path semantics
`Package.Save()` treats relative paths as **Packages**-relative. Do not prefix `Packages\` in
relative paths; use absolute paths when needed.

## 4) Order-dependent calls
Append before using SaveIn or case nodes:
- `AppendTestStep(...)` before `SetSaveInVariableName(...)`
- `AppendTestStep(switch_step)` before `CreateCaseNode(...)`

## 5) Expressions
Use `SetExpression(...)` + `SetExpectationExpression(...)`. Avoid deprecated `SetFormula(...)`.
Use `==` in expectations (not `=`), e.g. `value==3`.

## 5a) Comment expressions (TsComment)
`CreateTsComment(...)` expects an **expression**, not a plain string. If you want a literal
comment, wrap it in quotes or set the comment expression explicitly.

```python
comment = api.PackageApi.TestStepApi.CreateTsComment()
comment.SetCommentExpression("'Sum is 3'")
```

Passing `"Sum is 3"` without quotes will be parsed as an expression and can fail (e.g. "Sum variable is not defined").

## 6) Cleanup
Always `Close()` packages after saving (use `try/finally` if needed).

## 7) Variable naming + descriptions
Names: short CamelCase with prefixes:
- `P_` input, `R_` output, `V_` internal, `F_` function

Descriptions: sentence case, end with a period. Add units or value meanings in `[]` at the front
for unit/Boolean/Enum/Texttable variables.

## 8) Blocks + evaluation rules
Structure test cases into clearly titled blocks.

Evaluation meanings:
- `NONE`, `SUCCESS`, `FAILED`, `ERROR`, `INCONCLUSIVE`

Constraints:
- `NONE` packages must not call packages that can return `SUCCESS/FAILED/ERROR`
- Called package evaluation is inherited by the caller
