from __future__ import annotations

import subprocess
import sys

import click

from src.config import Config


@click.command()
@click.option(
    "--app",
    "-a",
    "app_file",
    help="Path to app file to serve",
)
@click.option(
    "--port",
    "-p",
    type=int,
    help="Port to run server on",
)
@click.option(
    "--host",
    "-h",
    "host",
    help="Host to bind to",
)
@click.option(
    "--config",
    "-c",
    "config_file",
    help="Path to configuration file",
)
def serve(
    app_file: str | None,
    port: int | None,
    host: str | None,
    config_file: str | None,
) -> None:
    """Serve the generated API stub application."""
    # Load configuration
    if config_file:
        config = Config.from_file(config_file)
    else:
        config = Config.load()

    app_file = app_file or config.app_file
    port = port or config.port
    host = host or config.host

    click.echo(click.style(f"🚀 Starting server with {app_file}...", fg="green", bold=True))
    click.echo(click.style(f"📍 Server: http://{host}:{port}", fg="cyan"))
    click.echo(click.style("Press Ctrl+C to stop\n", fg="yellow"))

    try:
        # Check if it's a FastAPI app by reading the file
        with open(app_file) as f:
            content = f.read()
            if "fastapi" in content.lower():
                # Run with uvicorn
                app_module = app_file.replace(".py", "").replace("/", ".")
                subprocess.run(
                    ["uvicorn", f"{app_module}:app", "--host", host, "--port", str(port), "--reload"],
                    check=True,
                )
            else:
                # Run Flask app
                subprocess.run(["python", app_file], check=True, env={"FLASK_ENV": "development"})
    except FileNotFoundError:
        click.echo(click.style(f"❌ Error: App file not found: {app_file}", fg="red"), err=True)
        sys.exit(1)
    except KeyboardInterrupt:
        click.echo(click.style("\n\n👋 Server stopped", fg="yellow"))
