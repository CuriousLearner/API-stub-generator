from __future__ import annotations

import json
import sys

import click

from src.config import Config
from src.generator import generate_app
from src.openapi_generator import generate_openapi_spec
from src.serialize_data import get_json_from_endpoints
from src.validator import validate_endpoints_list


@click.command()
@click.option(
    "--input",
    "-i",
    "input_file",
    help="Path to proposed endpoints markdown file",
)
@click.option(
    "--output",
    "-o",
    "output_file",
    help="Path to output JSON file",
)
@click.option(
    "--app",
    "-a",
    "app_file",
    help="Path to generated app file",
)
@click.option(
    "--framework",
    "-f",
    type=click.Choice(["flask", "fastapi"], case_sensitive=False),
    help="Framework to use for app generation",
)
@click.option(
    "--config",
    "-c",
    "config_file",
    help="Path to configuration file",
)
@click.option(
    "--validate-only",
    is_flag=True,
    help="Only validate endpoints without generating files",
)
def generate(
    input_file: str | None,
    output_file: str | None,
    app_file: str | None,
    framework: str | None,
    config_file: str | None,
    validate_only: bool,
) -> None:
    """Generate API stubs from proposed endpoints documentation."""
    # Load configuration
    if config_file:
        config = Config.from_file(config_file)
    else:
        config = Config.load()

    # Override with CLI arguments
    input_file = input_file or config.input_file
    output_file = output_file or config.output_file
    app_file = app_file or config.app_file
    framework = framework or config.framework

    # Read and parse endpoints
    try:
        with open(input_file) as f:
            content = f.read()
    except FileNotFoundError:
        click.echo(click.style(f"❌ Error: File not found: {input_file}", fg="red"), err=True)
        sys.exit(1)

    endpoints = get_json_from_endpoints(content)

    # Validate endpoints
    errors = validate_endpoints_list(endpoints)
    if errors:
        click.echo(click.style("❌ Validation errors found:", fg="red"), err=True)
        for error in errors:
            click.echo(click.style(f"  • {error}", fg="red"), err=True)
        sys.exit(1)

    click.echo(click.style(f"✓ Found {len(endpoints)} valid endpoint(s)", fg="green"))

    if validate_only:
        return

    # Save JSON data
    with open(output_file, "w") as f:
        json.dump(endpoints, f, indent=4)
    click.echo(click.style(f"✓ Saved endpoints to {output_file}", fg="green"))

    # Generate app
    generate_app(endpoints, app_file, framework, config)
    click.echo(click.style(f"✓ Generated {framework} app at {app_file}", fg="green"))

    # Generate OpenAPI spec
    openapi_file = "openapi.json"
    generate_openapi_spec(endpoints, openapi_file)
    click.echo(click.style(f"✓ Generated OpenAPI spec at {openapi_file}", fg="green"))

    click.echo(click.style(f"\n🚀 Run your app with: python {app_file}", fg="cyan", bold=True))
    if framework == "fastapi":
        click.echo(click.style(f"📚 View API docs at: http://localhost:{config.port}/docs", fg="cyan"))
