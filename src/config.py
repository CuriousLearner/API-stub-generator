from __future__ import annotations

import os
from pathlib import Path
from typing import Any

import yaml


class Config:
    """Configuration management for API stub generator."""

    def __init__(self) -> None:
        self.input_file = "proposed_endpoints.md"
        self.output_file = "endpoints_data.json"
        self.app_file = "app.py"
        self.framework = "flask"
        self.enable_cors = True
        self.debug_mode = True
        self.port = 5000
        self.host = "localhost"

    @classmethod
    def from_file(cls, config_path: str | Path) -> Config:
        """Load configuration from YAML file."""
        config = cls()
        if not os.path.exists(config_path):
            return config

        with open(config_path) as f:
            data: dict[str, Any] = yaml.safe_load(f) or {}

        config.input_file = data.get("input_file", config.input_file)
        config.output_file = data.get("output_file", config.output_file)
        config.app_file = data.get("app_file", config.app_file)
        config.framework = data.get("framework", config.framework)
        config.enable_cors = data.get("enable_cors", config.enable_cors)
        config.debug_mode = data.get("debug_mode", config.debug_mode)
        config.port = data.get("port", config.port)
        config.host = data.get("host", config.host)

        return config

    @classmethod
    def load(cls) -> Config:
        """Load configuration from default locations."""
        # Check for config files in order of precedence
        config_paths = [
            ".stubrc.yml",
            ".stubrc.yaml",
            "stub.yml",
            "stub.yaml",
        ]

        for path in config_paths:
            if os.path.exists(path):
                return cls.from_file(path)

        return cls()
