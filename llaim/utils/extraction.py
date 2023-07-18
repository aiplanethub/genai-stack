import inspect


def extract_class_init_attrs(clss):
    # Get the signature of the __init__ method
    init_signature = inspect.signature(clss.__init__)

    # Extract the parameter names and their default values
    init_parameters = init_signature.parameters

    return {
        name: param.default != inspect.Parameter.empty
        for name, param in init_parameters.items()
        if name != "self"  # noqa: E501
    }  # {"<attr_name>":"<default_is_empty>"}
