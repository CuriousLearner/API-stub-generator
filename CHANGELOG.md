Changelog
=========

## [0.2.0] - 2025-01-09

### 🎉 Major Release - Complete Rewrite

#### Added
- **CLI Interface**: New `api-stub-gen` command with subcommands (`generate`, `watch`, `serve`)
- **FastAPI Support**: Generate FastAPI applications with async support and auto-docs
- **Watch Mode**: Auto-regenerate stubs when markdown files change
- **Configuration Files**: YAML config file support (`.stubrc.yml`)
- **OpenAPI Generation**: Auto-generate OpenAPI 3.0 specifications
- **CORS Support**: Built-in CORS for Flask and FastAPI apps
- **Hot Reload**: Debug mode with auto-reload enabled by default
- **Template System**: Jinja2-based code generation (replaces string concatenation)
- **Validation**: Comprehensive endpoint validation with helpful error messages
- **Docker Support**: Dockerfile and docker-compose.yml for containerization
- **Type Hints**: Full type annotations throughout the codebase
- **Test Coverage**: Comprehensive test suite for all new features
- **Health Endpoint**: Built-in `/health` endpoint for monitoring

#### Changed
- **Python Version**: Minimum Python 3.10 (was 3.7)
- **Dependencies**: Updated to latest versions (Flask 3.0+, pytest 7.4+)
- **CI/CD**: Migrated from Travis CI to GitHub Actions
- **Linting**: Replaced flake8 with Ruff for faster linting and formatting
- **Project Structure**: Added `pyproject.toml` following PEP 621 standards
- **Documentation**: Complete README rewrite with examples and comparisons

#### Deprecated
- Direct usage of `serialize_data.py` and `create_mock_endpoints.py` (use CLI instead)
- Pipenv as primary dependency manager (pip recommended)

#### Fixed
- Better error handling for malformed markdown
- Proper validation of HTTP methods and endpoint formats
- Unicode handling in endpoint descriptions

## [0.1.0] - 2019-01-29

### Features & Improvements

- Allow `serialize_data.py` accept path for proposed endpoints docs as command line argument. ([@mansiag])

[@mansiag]: https://github.com/mansiag
