from typing import Callable, Type
import inspect


def extract_func_params(func: Callable):
    funcs_signature = inspect.signature(func)
    funcs_params = funcs_signature.parameters
    return {
        name: param.default != inspect.Parameter.empty
        for name, param in funcs_params.items()
        if name != "self"  # noqa: E501
    }  # {"<attr_name>":"<default_is_empty>"}


def extract_class_init_attrs(clss: Type):
    return extract_func_params(clss.__init__)


def extract_method_params(clss: Type, method: Callable):
    return extract_func_params(inspect.signature(getattr(clss, method)))
