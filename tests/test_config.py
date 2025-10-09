from __future__ import annotations

import tempfile
from pathlib import Path

from src.config import Config


class TestConfig:
    def test_default_config(self) -> None:
        config = Config()
        assert config.input_file == "proposed_endpoints.md"
        assert config.output_file == "endpoints_data.json"
        assert config.app_file == "app.py"
        assert config.framework == "flask"
        assert config.enable_cors is True
        assert config.debug_mode is True
        assert config.port == 5000
        assert config.host == "localhost"

    def test_load_from_file(self) -> None:
        yaml_content = """
input_file: custom_endpoints.md
output_file: custom_output.json
framework: fastapi
port: 8000
enable_cors: false
"""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".yml", delete=False) as f:
            f.write(yaml_content)
            temp_path = f.name

        try:
            config = Config.from_file(temp_path)
            assert config.input_file == "custom_endpoints.md"
            assert config.output_file == "custom_output.json"
            assert config.framework == "fastapi"
            assert config.port == 8000
            assert config.enable_cors is False
        finally:
            Path(temp_path).unlink()

    def test_load_nonexistent_file(self) -> None:
        config = Config.from_file("nonexistent.yml")
        # Should return default config
        assert config.input_file == "proposed_endpoints.md"
