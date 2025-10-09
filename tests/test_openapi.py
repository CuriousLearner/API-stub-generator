from __future__ import annotations

import json
import tempfile
from pathlib import Path

from src.openapi_generator import generate_openapi_spec


class TestOpenAPIGenerator:
    def test_generate_spec(self) -> None:
        endpoints = [
            {
                "endpoint": "/api/users",
                "method": "GET",
                "description": "Get all users",
                "response_body": [{"id": 1, "name": "John"}],
            },
            {
                "endpoint": "/api/users",
                "method": "POST",
                "description": "Create user",
                "request_body": {"name": "John"},
                "response_body": {"id": 1, "name": "John"},
            },
        ]

        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            temp_path = f.name

        try:
            generate_openapi_spec(endpoints, temp_path)
            spec = json.loads(Path(temp_path).read_text())

            assert spec["openapi"] == "3.0.0"
            assert spec["info"]["title"] == "API Stub Server"
            assert "/api/users" in spec["paths"]
            assert "get" in spec["paths"]["/api/users"]
            assert "post" in spec["paths"]["/api/users"]

            # Check POST has request body
            post_op = spec["paths"]["/api/users"]["post"]
            assert "requestBody" in post_op
            assert post_op["requestBody"]["required"] is True
        finally:
            Path(temp_path).unlink()
