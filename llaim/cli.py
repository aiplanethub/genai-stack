"""Console script for llaim."""
import sys
import click

from llaim import __version__
from llaim.model.run import list_supported_models, get_model_class

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
    """Outputs version of the installed package

    `llaim version`
    """
    click.echo(f"\nLLAIM Version - {__version__}")


@main.command()
def list_models():
    """Lists available prebuilt models

    llaim list-models
    """
    click.echo("Available List of models")
    for indx, model in enumerate(list_supported_models()):
        click.echo(f"{indx+1}. {model}")


@main.command()
@click.option("--model", help="Start a HTTP Server for the model", type=str)
@click.option("-f", help="Config file", type=str)
def start(model, f=None):
    """Start a HTTP server for a model

    `llaim start --model gpt3.5`
    """
    model_class = get_model_class(model_name=model)()
    model_class.run_http_server()


# @main.command()
# @click.option("-destination", help="Download and Install Airbyte", type=str)
# def dli_airbyte(destination):
#     click.echo("Downloading and installing Airbyte")


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
