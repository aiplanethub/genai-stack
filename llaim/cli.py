"""Console script for llaim."""
import sys
import click

from llaim import LLAIM_DEBUG

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
    if LLAIM_DEBUG:
        click.echo(
            """Running in DEBUG True. Disable it by setting the environment variable LLAIM_DEBUG to 0"""  # noqa: E501
        )


@main.command()
@click.option("-destination", help="Download and Install Airbyte", type=str)
def dli_airbyte(destination):
    click.echo("Downloading and installing Airbyte")


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
