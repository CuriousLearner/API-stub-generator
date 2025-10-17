from __future__ import annotations

import click

from src.commands.generate import generate
from src.commands.serve import serve
from src.commands.watch import watch


@click.group()
@click.version_option(version="0.2.0", prog_name="api-stub-gen")
def main() -> None:
    """API Stub Generator - Mock API endpoints with ease."""
    pass


main.add_command(generate)
main.add_command(serve)
main.add_command(watch)


if __name__ == "__main__":
    main()
