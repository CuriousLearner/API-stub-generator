# Deprecated Modules

The following modules are deprecated and kept for backward compatibility only.

## serialize_data.py

**Status**: Deprecated
**Replacement**: Use `api-stub-gen generate` CLI command

**Old usage**:
```bash
python -m src.serialize_data --file-path proposed_endpoints.md
```

**New usage**:
```bash
api-stub-gen generate -i proposed_endpoints.md
```

## create_mock_endpoints.py

**Status**: Deprecated
**Replacement**: Use `api-stub-gen generate` CLI command (automatically generates app)

**Old usage**:
```bash
python -m src.create_mock_endpoints
```

**New usage**:
```bash
api-stub-gen generate  # Generates both JSON and app in one command
```

## Migration Guide

### From Old CLI to New CLI

| Old Command | New Command |
|-------------|-------------|
| `python src/serialize_data.py` | `api-stub-gen generate` |
| `python src/create_mock_endpoints.py` | Automatically done by `generate` |
| `python app.py` | `api-stub-gen serve` |
| N/A | `api-stub-gen watch` (new feature) |

### Breaking Changes

1. **CLI Interface**: Direct module execution is deprecated. Install the package and use `api-stub-gen` command.
2. **Output Format**: Templates now used instead of string concatenation - generated code may look different but works the same.
3. **Default Behavior**: CORS and debug mode now enabled by default (disable via config if needed).

### Benefits of Migration

- ✅ Cleaner CLI interface
- ✅ Watch mode for auto-regeneration
- ✅ FastAPI support
- ✅ OpenAPI spec generation
- ✅ Better error messages
- ✅ Configuration file support
- ✅ Comprehensive validation

These deprecated modules will be removed in v1.0.0.
