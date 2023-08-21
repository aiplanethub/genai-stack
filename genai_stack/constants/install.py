"""
Constants for the installer and the templating engine
"""
from enum import Enum
from genai_stack.constants.vectordb import AVAILABLE_VECTORDB_MAPS


class Components(Enum):
    VECTORDB = "vectordb"


AVAILABLE_COMPONENTS = {Components.VECTORDB: AVAILABLE_VECTORDB_MAPS.keys()}
