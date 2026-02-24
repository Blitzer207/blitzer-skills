# ecu.test API Debug Patterns

## AttributeError Debug Workflow

**Error**: `AttributeError: 'XXX' object has no attribute 'YYY'`

### Step 1: Identify object and method
- Object: `XXX`
- Missing method: `YYY`

### Step 2: Grep ApiClient.py (faster than docs)
```
rg -n "def YYY" "<ECU_TEST_HOME>\Templates\ApiClient\ApiClient.py"
```

### Step 3: Locate the method
- If found → check which class owns it
- If not found → method renamed or accessed via another object

### Step 4: Check class relationships
```
rg -n "class XXX\(" "<ECU_TEST_HOME>\Templates\ApiClient\ApiClient.py"
```
Look for `Get*Config()` or similar accessor methods.

### Step 5: Grep related keywords
```
rg -n "YYY" "<ECU_TEST_HOME>\Templates\ApiClient\ApiClient.py"
```

### Key Grep Patterns

| Pattern | Purpose | Example |
|---------|---------|---------|
| `def 方法名\(` | Find method definition | `def AppendSignalGroup\(` |
| `class 类名\(` | Find class definition | `class Package\(` |
| `def Get.*Config` | Find config accessors | `def GetRecordingConfig` |

### Cases

#### Case 1: Method renamed
- Error: `'NumericVariable' object has no attribute 'SetInitialNumericValue'`
- Grep: `SetInitial` → finds `SetInitialValue`, `SetInitialNumericValueString`
- Fix: Use `SetInitialValue(100.0)`

#### Case 2: Method on nested object
- Error: `'Package' object has no attribute 'AppendSignalGroup'`
- Grep: `AppendSignalGroup` → found in `RecordingConfig` class (line 19588)
- Check `Package` class → has `GetRecordingConfig()` method
- Fix:
  ```python
  config = package.GetRecordingConfig()
  config.AppendSignalGroup(group)
  ```
