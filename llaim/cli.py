"""Console script for llaim."""
import sys
import click

from llaim import __version__


BANNER = """
██╗     ██╗      █████╗ ██╗███╗   ███╗
██║     ██║     ██╔══██╗██║████╗ ████║
██║     ██║     ███████║██║██╔████╔██║
██║     ██║     ██╔══██║██║██║╚██╔╝██║
███████╗███████╗██║  ██║██║██║ ╚═╝ ██║
╚══════╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝     ╚═╝
"""


@click.group()
def main():
    """Console script for llaim."""
    click.echo(BANNER)


@main.command()
def version():
    click.echo(f"\nLLAIM Version - {__version__}")


@main.command()
@click.option("-destination", help="Download and Install Airbyte", type=str)
def dli_airbyte(destination):
    click.echo("Downloading and installing Airbyte")


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
