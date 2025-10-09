from __future__ import annotations

import sys
import time
from pathlib import Path

import click
from watchdog.events import FileSystemEvent, FileSystemEventHandler
from watchdog.observers import Observer

from src.commands.generate import generate as generate_command
from src.config import Config


class EndpointFileHandler(FileSystemEventHandler):
    """Handler for file system events on endpoint files."""

    def __init__(self, ctx: click.Context) -> None:
        self.ctx = ctx
        self.last_modified = 0.0

    def on_modified(self, event: FileSystemEvent) -> None:
        if event.is_directory:
            return

        # Debounce - ignore events within 1 second
        current_time = time.time()
        if current_time - self.last_modified < 1:
            return

        self.last_modified = current_time

        click.echo(click.style(f"\n📝 File changed: {event.src_path}", fg="yellow"))
        click.echo(click.style("🔄 Regenerating stubs...", fg="cyan"))

        # Trigger regeneration
        self.ctx.invoke(generate_command)


@click.command()
@click.option(
    "--input",
    "-i",
    "input_file",
    help="Path to proposed endpoints markdown file to watch",
)
@click.option(
    "--config",
    "-c",
    "config_file",
    help="Path to configuration file",
)
@click.pass_context
def watch(ctx: click.Context, input_file: str | None, config_file: str | None) -> None:
    """Watch endpoint file and auto-regenerate stubs on changes."""
    # Load configuration
    if config_file:
        config = Config.from_file(config_file)
    else:
        config = Config.load()

    input_file = input_file or config.input_file
    file_path = Path(input_file)

    if not file_path.exists():
        click.echo(click.style(f"❌ Error: File not found: {input_file}", fg="red"), err=True)
        sys.exit(1)

    # Initial generation
    click.echo(click.style(f"👀 Watching {input_file} for changes...", fg="green", bold=True))
    click.echo(click.style("Press Ctrl+C to stop\n", fg="yellow"))

    ctx.invoke(generate_command, input_file=input_file, config_file=config_file)

    # Set up file watcher
    event_handler = EndpointFileHandler(ctx)
    observer = Observer()
    observer.schedule(event_handler, str(file_path.parent), recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        click.echo(click.style("\n\n👋 Stopping watch mode...", fg="yellow"))
        observer.stop()
    observer.join()
