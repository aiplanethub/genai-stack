from genai_stack.fine_tune.base import BaseFineTune, BaseFineTuneConfigModel


class LLama27bConfigModel(BaseFineTuneConfigModel):
    pass


class LLama27bFineTune(BaseFineTune):
    config_class = LLama27bConfigModel

    pass
