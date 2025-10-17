from __future__ import annotations

import tempfile
from pathlib import Path

from src.config import Config
from src.generator import generate_app, prepare_endpoint_data, slugify


class TestSlugify:
    def test_simple_string(self) -> None:
        assert slugify("Hello World") == "hello_world"

    def test_special_characters(self) -> None:
        assert slugify("Test-API/Endpoint") == "test_apiendpoint"

    def test_unicode(self) -> None:
        assert slugify("Café Münster") == "cafe_munster"


class TestPrepareEndpointData:
    def test_adds_function_name(self) -> None:
        endpoints = [{"endpoint": "/api/users", "method": "GET", "description": "Get all users"}]
        prepared = prepare_endpoint_data(endpoints)
        assert prepared[0]["function_name"] == "get_all_users"


class TestGenerateApp:
    def test_generate_flask_app(self) -> None:
        endpoints = [
            {
                "endpoint": "/api/test",
                "method": "GET",
                "description": "Test endpoint",
                "response_body": {"status": "ok"},
            }
        ]
        config = Config()

        with tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False) as f:
            temp_path = f.name

        try:
            generate_app(endpoints, temp_path, "flask", config)
            content = Path(temp_path).read_text()

            assert "from flask import Flask" in content
            assert "@app.route('/api/test'" in content
            assert "def test_endpoint():" in content
            assert "CORS(app)" in content  # CORS enabled by default
        finally:
            Path(temp_path).unlink()

    def test_generate_fastapi_app(self) -> None:
        endpoints = [
            {
                "endpoint": "/api/test",
                "method": "GET",
                "description": "Test endpoint",
                "response_body": {"status": "ok"},
            }
        ]
        config = Config()

        with tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False) as f:
            temp_path = f.name

        try:
            generate_app(endpoints, temp_path, "fastapi", config)
            content = Path(temp_path).read_text()

            assert "from fastapi import FastAPI" in content
            assert "@app.get('/api/test')" in content
            assert "async def test_endpoint():" in content
            assert "CORSMiddleware" in content  # CORS enabled by default
        finally:
            Path(temp_path).unlink()
