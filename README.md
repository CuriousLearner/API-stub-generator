# API Stub Generator

[![CI](https://github.com/CuriousLearner/API-stub-generator/workflows/CI/badge.svg)](https://github.com/CuriousLearner/API-stub-generator/actions)

🚀 **Mock proposed API endpoints with ease!** Auto-generate Flask or FastAPI stub servers from markdown documentation with hot-reload, CORS support, and OpenAPI specs.

## Inspiration

I'm a lazy programmer. Basically, if you would tell me that I've to do the same task without applying my brain over and over again, I'll try to automate it with code (if I can xD)

The proposed API docs I write, have to be then mocked for APP / Front-End Developers so that they're not blocked by actual API calls. Later they can replace these stubs with actual API calls. With more requirements coming in, the proposed endpoint changes over time and the stubs have to be updated. I found myself in a viscous circle of keeping the both up to date which wastes my dev cycles (where I can work on generating actual endpoints) & thus created this small utility to help me.

## ✨ Features

- 🎯 **Multiple Frameworks**: Generate Flask or FastAPI applications
- 🔄 **Watch Mode**: Auto-regenerate stubs when docs change
- 🌐 **CORS Support**: Built-in CORS for frontend development
- 🔥 **Hot Reload**: Debug mode enabled by default
- 📚 **OpenAPI Specs**: Auto-generate OpenAPI/Swagger documentation
- ⚙️ **Configuration**: YAML config file support
- ✅ **Validation**: Comprehensive endpoint validation
- 🐳 **Docker Ready**: Dockerfile and docker-compose included
- 🧪 **Well Tested**: Comprehensive test coverage

## Requirements

- Python 3.10 or higher

## Installation

```bash
# Clone the repository
git clone https://github.com/CuriousLearner/API-stub-generator.git
cd API-stub-generator

# Install with pip (recommended)
pip install -e ".[dev]"
```

## Quick Start

```bash
# Generate stubs from your endpoints documentation
api-stub-gen generate -i proposed_endpoints.md

# Watch for changes and auto-regenerate
api-stub-gen watch

# Serve the generated app
api-stub-gen serve
```

## Usage

### Generate Command

Generate API stubs from markdown documentation:

```bash
# Basic usage
api-stub-gen generate

# With custom paths
api-stub-gen generate -i my_endpoints.md -o data.json -a server.py

# Choose framework (flask or fastapi)
api-stub-gen generate -f fastapi

# Validate only (no generation)
api-stub-gen generate --validate-only

# Use config file
api-stub-gen generate -c .stubrc.yml
```

### Watch Command

Auto-regenerate stubs when documentation changes:

```bash
# Watch default file
api-stub-gen watch

# Watch specific file
api-stub-gen watch -i my_endpoints.md
```

### Serve Command

Serve the generated application:

```bash
# Serve with defaults
api-stub-gen serve

# Custom port and host
api-stub-gen serve -p 8000 -h 0.0.0.0
```

### Configuration File

Create a `.stubrc.yml` file for default settings:

```yaml
input_file: proposed_endpoints.md
output_file: endpoints_data.json
app_file: app.py
framework: flask  # or fastapi
enable_cors: true
debug_mode: true
port: 5000
host: localhost
```

### Docker Support

```bash
# Build and run with docker-compose
docker-compose up

# Or use Dockerfile directly
docker build -t api-stub-gen .
docker run -v $(pwd):/app api-stub-gen
```


## How It Works

**GET** → **SET** → **GO** in three simple steps:

1. **GET** - Parse your `proposed_endpoints.md` and extract endpoint definitions
2. **SET** - Generate Flask/FastAPI app with all endpoints and OpenAPI spec
3. **GO** - Run your stub server instantly on [http://localhost:5000](http://localhost:5000)

## Example Workflow

```bash
# 1. Create your endpoints documentation (proposed_endpoints.md)
# 2. Generate everything
api-stub-gen generate -f fastapi

# 3. Start development with watch mode
api-stub-gen watch &
api-stub-gen serve

# 4. Your stub API is now live!
# - API server: http://localhost:5000
# - Swagger docs: http://localhost:5000/docs (FastAPI only)
# - OpenAPI spec: openapi.json
```

## Generated Output

The tool generates:
- **`endpoints_data.json`** - Parsed endpoint data
- **`app.py`** - Flask/FastAPI application with all routes
- **`openapi.json`** - OpenAPI 3.0 specification
- **Health endpoint** - `/health` for monitoring

## Advanced Features

### Framework Comparison

| Feature | Flask | FastAPI |
|---------|-------|---------|
| Auto docs | ❌ | ✅ (`/docs`, `/redoc`) |
| Type hints | Optional | Required |
| Async support | ✅ (2.0+) | ✅ (Native) |
| Initial complexity | Simple | More setup |
| Runtime performance | Good | ⚡ Faster |
| Learning curve | Gentle | Steeper |

### Validation

All endpoints are validated for:
- Required fields (endpoint, method, description)
- Valid HTTP methods
- Proper endpoint format (must start with `/`)
- Request/response body structure

## Development

```bash
# Install in development mode
pip install -e ".[dev]"

# Run tests
pytest

# Run linting
ruff check src/ tests/

# Format code
ruff format src/ tests/

# Type checking
mypy src/
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License - see LICENSE file for details.
