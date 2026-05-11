# testguide-plugin.md — test.guide 上传插件

ecutest_code 内置 pytest plugin，可将测试结果上传到 test.guide 平台。

## 启用方式

plugin 自动注册，无需手动导入。通过 CLI 选项或 ini 配置激活功能。

## CLI 选项

```bash
# 上传结果到 test.guide
pytest --upload-to-testguide

# 导出报告到本地 .report 目录（不上传）
pytest --export-testguide-report

# 跳过 SSL 验证
pytest --upload-to-testguide --skip-testguide-ssl
```

## 必需环境变量（上传时）

```bash
TESTGUIDE_URL=http://your.test-guide.instance:8085
TESTGUIDE_PROJECT_ID=123
TESTGUIDE_AUTH_KEY=your-auth-key
```

在 test.guide 的 `用户设置 → 认证密钥` 中创建 `TESTGUIDE_AUTH_KEY`。

## pytest.ini / pyproject.toml 配置

```ini
# pytest.ini
[pytest]
testguide_request_timeout = 20.0
skip_testguide_ssl = false
enable_verdict_none = false
```

```toml
# pyproject.toml
[tool.pytest.ini_options]
testguide_request_timeout = "20.0"
skip_testguide_ssl = false
enable_verdict_none = false
```

| 配置项 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `testguide_request_timeout` | string | `"20.0"` | HTTP 请求超时（秒） |
| `skip_testguide_ssl` | bool | `false` | 跳过 SSL 验证 |
| `enable_verdict_none` | bool | `false` | 无 assert 的测试报告为 NONE 而非 PASSED |

## 导出目录结构

`--export-testguide-report` 会在 pytest 调用目录生成：

```
.report/
└── module_name/
    ├── module_name.json
    ├── module_name.zip        ← 上传到 test.guide 的文件
    ├── test_case_name/
    │   ├── stdout.log
    │   ├── stderr.log
    │   └── logs.log
    └── upload_info.json       ← 上传后生成，含 task_id
```

## Verdict 映射

| pytest 结果 | test.guide Verdict |
|------------|-------------------|
| passed | PASSED |
| failed | FAILED |
| skipped | INCONCLUSIVE |
| 无 assert（需开启 `enable_verdict_none`） | NONE |

## TT_TASK_ID 环境变量

若设置了 `TT_TASK_ID` 环境变量，该值会作为常量属性附加到每个 TestCase，用于 test.guide AV job 的结果追踪。
