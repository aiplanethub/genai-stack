"""Console script for llm_stack."""
import sys
import click

from llm_stack import __version__
from llm_stack.model.run import list_supported_models, get_model_class, get_retriever_class, get_vectordb_class
from llm_stack.config import ConfigLoader
from llm_stack.constants import (
    MODEL_CONFIG_KEY,
    RETRIEVER_CONFIG_KEY,
    VECTORDB_CONFIG_KEY,
    CUSTOM_MODEL_KEY_NAME,
)
from llm_stack.exception import LLMStackException
from llm_stack.constants.model import AVAILABLE_MODEL_MAPS

BANNER = """
██╗     ██╗     ███╗   ███╗    ███████╗████████╗ █████╗  ██████╗██╗  ██╗
██║     ██║     ████╗ ████║    ██╔════╝╚══██╔══╝██╔══██╗██╔════╝██║ ██╔╝
██║     ██║     ██╔████╔██║    ███████╗   ██║   ███████║██║     █████╔╝
██║     ██║     ██║╚██╔╝██║    ╚════██║   ██║   ██╔══██║██║     ██╔═██╗
███████╗███████╗██║ ╚═╝ ██║    ███████║   ██║   ██║  ██║╚██████╗██║  ██╗
╚══════╝╚══════╝╚═╝     ╚═╝    ╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
"""


class LLMStackCommand(click.Group):
    def get_help(self, ctx: click.Context) -> str:
        return f"{BANNER}{super().get_help(ctx)}"


@click.group(cls=LLMStackCommand)
def main():
    click.echo(BANNER)


@main.command()
def version():
    """Version of the installed LLM Stack package

    `llmstack version`
    """
    click.echo(f"Version - {__version__}")


@main.command()
def list_models():
    """Lists available prebuilt models

    `llmstack list-models`
    """
    click.echo("Available List of models\n")
    for indx, model in enumerate(list_supported_models()):
        click.echo(f"{indx+1}. {model}")


@main.command()
@click.option("--config_file", help="Config file", type=str)
def start(config_file):
    """Start a HTTP server for a model

    `llmstack start --model gpt3.5`
    """

    config_loader = ConfigLoader(config=config_file)

    vectordb_client = get_vectordb_class(
        config_loader.get_config_section_name(
            VECTORDB_CONFIG_KEY,
        )
    )(config=config_file)
    retriever = get_retriever_class(
        config_loader.get_config_section_name(
            RETRIEVER_CONFIG_KEY,
        )
    )(config=config_file, vectordb=vectordb_client)

    model: str = config_loader.get_config_section_name(MODEL_CONFIG_KEY)
    model = model.strip()
    if model != CUSTOM_MODEL_KEY_NAME and model not in AVAILABLE_MODEL_MAPS.keys():
        raise LLMStackException(
            "Unkown Prebuilt Model Provided. Checkout how to run a custom model with LLM Stack."  # noqa: E501
        )

    model_class = get_model_class(model)(config=config_file, retriever=retriever)
    model_class.run_http_server()


# @main.command()
# @click.option("-destination", help="Download and Install Airbyte", type=str)
# def dli_airbyte(destination):
#     click.echo("Downloading and installing Airbyte")


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
