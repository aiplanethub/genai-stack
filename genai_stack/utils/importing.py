import importlib
from typing import Any


def import_module(module_path: str) -> Any:
    """Import module from module path"""

    if "from" not in module_path:
        return importlib.import_module(module_path)

    _, module_path, _, object_name = module_path.split()

    module = importlib.import_module(module_path)

    return getattr(module, object_name)


def import_class(class_path: str) -> Any:
    """Import class from class path"""
    module_path, class_name = class_path.rsplit(".", 1)
    module = import_module(module_path)
    return getattr(module, class_name)


def import_class_from_file(file_path, class_name):
    """
    Imports a class from the given file path.

    Args:
        file_path (str): The path to the Python file containing the class.
        class_name (str): The name of the class to import.

    Returns:
        class: The imported class object.
    """
    module_spec = importlib.util.spec_from_file_location("custom_model", file_path)
    custom_module = importlib.util.module_from_spec(module_spec)
    module_spec.loader.exec_module(custom_module)

    if hasattr(custom_module, class_name):
        return getattr(custom_module, class_name)
    else:
        raise AttributeError(
            f"Class '{class_name}' not found in the module '{file_path}'.",
        )
