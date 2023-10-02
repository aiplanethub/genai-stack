from genai_stack.fine_tune.base import BaseHyperParametersConfigModel, BaseFineTuneConfigModel, BaseFineTune
from datasets import load_dataset
import ray.data


class HyperParametersConfigModel(BaseHyperParametersConfigModel):
    pass


class LLama27bConfigModel(BaseFineTuneConfigModel):

    """
    Data Model for the configs
    """

    instruction: str = "text-summarization"
    hyperparameters: HyperParametersConfigModel
    dataset: str


class LLama27bFineTune(BaseFineTune):
    """
    Class for fine-tuning the model
    """

    config_class = LLama27bConfigModel

    def load_model(self):
        pass

    def load_dataset(self):
        datasets = load_dataset(self.config.dataset)
        ray_datasets = {
            "train": ray.data.from_huggingface(datasets["train"]),
            "validation": ray.data.from_huggingface(datasets["validation"]),
            "test": ray.data.from_huggingface(datasets["test"]),
        }
        return ray_datasets

    def train(self):
        pass

    def tune(self):
        pass

    def evaluate(self):
        pass
