import inspect

from llm_stack.core.config import ConfigLoader


class BaseComponent(ConfigLoader):
    @classmethod
    def from_config(cls, config_file):
        return cls(config=config_file)

    @classmethod
    def from_kwargs(cls, *args, **kwargs):
        init_signature = inspect.signature(cls.__init__)
        init_params = init_signature.parameters
        init_kwargs = {param.name: param.default for param in init_params.values() if param.default is not param.empty}

        cls_kwargs = {
            init_kw: kwargs.get(init_kw, init_value)
            for init_kw, init_value in init_kwargs.items()
            if not "config" in init_kw
        }

        # Remove cls kwargs from config kwargs
        for kw in cls_kwargs:
            kwargs.pop(kw, None)

        config_kwargs = {cls.config_key: kwargs}


        return cls(*args, **cls_kwargs, config=config_kwargs)
