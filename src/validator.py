from __future__ import annotations

from typing import Any


class ValidationError(Exception):
    """Custom exception for validation errors."""

    pass


def validate_endpoint(endpoint_data: dict[str, Any]) -> None:
    """Validate endpoint data structure."""
    required_fields = ["endpoint", "method", "description"]

    for field in required_fields:
        if not endpoint_data.get(field):
            raise ValidationError(f"Missing required field: {field}")

    # Validate HTTP method
    valid_methods = ["GET", "POST", "PUT", "PATCH", "DELETE", "HEAD", "OPTIONS"]
    method = endpoint_data.get("method", "").upper()
    if method not in valid_methods:
        raise ValidationError(f"Invalid HTTP method: {method}. Must be one of {valid_methods}")

    # Validate endpoint format
    endpoint = endpoint_data.get("endpoint", "")
    if not endpoint.startswith("/"):
        raise ValidationError(f"Endpoint must start with '/': {endpoint}")


def validate_endpoints_list(endpoints: list[dict[str, Any]]) -> list[str]:
    """Validate a list of endpoints and return any errors."""
    errors: list[str] = []

    if not endpoints:
        errors.append("No endpoints found in the document")
        return errors

    for i, endpoint in enumerate(endpoints):
        try:
            validate_endpoint(endpoint)
        except ValidationError as e:
            errors.append(f"Endpoint {i + 1}: {e}")

    return errors
