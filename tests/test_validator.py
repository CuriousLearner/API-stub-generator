from __future__ import annotations

import pytest

from src.validator import ValidationError, validate_endpoint, validate_endpoints_list


class TestValidateEndpoint:
    def test_valid_endpoint(self) -> None:
        endpoint = {
            "endpoint": "/api/users",
            "method": "GET",
            "description": "Get all users",
        }
        # Should not raise
        validate_endpoint(endpoint)

    def test_missing_endpoint_field(self) -> None:
        endpoint = {"method": "GET", "description": "Test"}
        with pytest.raises(ValidationError, match="Missing required field: endpoint"):
            validate_endpoint(endpoint)

    def test_missing_method_field(self) -> None:
        endpoint = {"endpoint": "/api/test", "description": "Test"}
        with pytest.raises(ValidationError, match="Missing required field: method"):
            validate_endpoint(endpoint)

    def test_missing_description_field(self) -> None:
        endpoint = {"endpoint": "/api/test", "method": "GET"}
        with pytest.raises(ValidationError, match="Missing required field: description"):
            validate_endpoint(endpoint)

    def test_invalid_http_method(self) -> None:
        endpoint = {
            "endpoint": "/api/test",
            "method": "INVALID",
            "description": "Test",
        }
        with pytest.raises(ValidationError, match="Invalid HTTP method"):
            validate_endpoint(endpoint)

    def test_endpoint_missing_slash(self) -> None:
        endpoint = {
            "endpoint": "api/test",
            "method": "GET",
            "description": "Test",
        }
        with pytest.raises(ValidationError, match="Endpoint must start with '/'"):
            validate_endpoint(endpoint)


class TestValidateEndpointsList:
    def test_empty_list(self) -> None:
        errors = validate_endpoints_list([])
        assert len(errors) == 1
        assert "No endpoints found" in errors[0]

    def test_valid_endpoints(self) -> None:
        endpoints = [
            {"endpoint": "/api/users", "method": "GET", "description": "Get users"},
            {"endpoint": "/api/posts", "method": "POST", "description": "Create post"},
        ]
        errors = validate_endpoints_list(endpoints)
        assert len(errors) == 0

    def test_mixed_valid_invalid(self) -> None:
        endpoints = [
            {"endpoint": "/api/users", "method": "GET", "description": "Get users"},
            {"endpoint": "api/invalid", "method": "GET", "description": "Invalid"},
        ]
        errors = validate_endpoints_list(endpoints)
        assert len(errors) == 1
        assert "Endpoint 2" in errors[0]
