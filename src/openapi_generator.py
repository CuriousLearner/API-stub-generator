from __future__ import annotations

import json
from typing import Any


def generate_openapi_spec(endpoints: list[dict[str, Any]], output_file: str = "openapi.json") -> None:
    """Generate OpenAPI 3.0 specification from endpoints."""
    spec: dict[str, Any] = {
        "openapi": "3.0.0",
        "info": {
            "title": "API Stub Server",
            "description": "Mock API stubs from proposed endpoints",
            "version": "1.0.0",
        },
        "servers": [{"url": "http://localhost:5000", "description": "Development server"}],
        "paths": {},
    }

    for endpoint in endpoints:
        path = endpoint.get("endpoint", "")
        method = endpoint.get("method", "GET").lower()
        description = endpoint.get("description", "")
        request_body = endpoint.get("request_body")
        response_body = endpoint.get("response_body")

        if path not in spec["paths"]:
            spec["paths"][path] = {}

        operation: dict[str, Any] = {
            "summary": description,
            "description": description,
            "responses": {
                "200": {
                    "description": "Successful response",
                    "content": {
                        "application/json": {
                            "schema": {"type": "object"},
                        }
                    },
                }
            },
        }

        # Add request body if present
        if method in ["post", "put", "patch"] and request_body:
            operation["requestBody"] = {
                "required": True,
                "content": {
                    "application/json": {
                        "schema": {"type": "object"},
                        "example": request_body,
                    }
                },
            }

        # Add response example
        if response_body:
            operation["responses"]["200"]["content"]["application/json"]["example"] = response_body

        spec["paths"][path][method] = operation

    # Write spec to file
    with open(output_file, "w") as f:
        json.dump(spec, f, indent=2)
