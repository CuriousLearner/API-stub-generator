from __future__ import annotations

import re
import unicodedata
from pathlib import Path
from typing import Any

from jinja2 import Environment, FileSystemLoader

from src.config import Config


def slugify(value: str) -> str:
    """Convert a string to a valid Python function name."""
    value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii")
    value = re.sub(r"[^\w\s-]", "", value).strip().lower()
    return re.sub(r"[-\s]+", "_", value)


def prepare_endpoint_data(endpoints: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Prepare endpoint data for template rendering."""
    prepared = []
    for endpoint in endpoints:
        prepared.append(
            {
                **endpoint,
                "function_name": slugify(endpoint.get("description", "endpoint")),
            }
        )
    return prepared


def generate_app(
    endpoints: list[dict[str, Any]],
    output_file: str,
    framework: str,
    config: Config,
) -> None:
    """Generate application code using Jinja2 templates."""
    # Set up Jinja2 environment
    template_dir = Path(__file__).parent / "templates"
    env = Environment(loader=FileSystemLoader(template_dir))

    # Select template based on framework
    template_name = f"{framework}_app.j2"
    template = env.get_template(template_name)

    # Prepare data
    prepared_endpoints = prepare_endpoint_data(endpoints)

    # Render template
    rendered = template.render(
        endpoints=prepared_endpoints,
        enable_cors=config.enable_cors,
        debug_mode=config.debug_mode,
        host=config.host,
        port=config.port,
    )

    # Write to file
    with open(output_file, "w") as f:
        f.write(rendered)
