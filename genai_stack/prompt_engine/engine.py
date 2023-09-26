from typing import Union

from langchain import PromptTemplate
from langchain.output_parsers import ResponseSchema, StructuredOutputParser

from genai_stack.prompt_engine.prompts import (
    BASIC_QA, CONVERSATIONAL_PROMPT_WITH_CONTEXT, CONVERSATIONAL_PROMPT, VALIDATION_PROMPT
)
from genai_stack.prompt_engine.base import BasePromptEngine, BasePromptEngineConfigModel, BasePromptEngineConfig
from genai_stack.prompt_engine.utils import ValidationResponseDict, PromptTypeEnum


class PromptEngineConfigModel(BasePromptEngineConfigModel):
    simple_chat_prompt_template: PromptTemplate = CONVERSATIONAL_PROMPT
    contextual_chat_prompt_template: PromptTemplate = CONVERSATIONAL_PROMPT_WITH_CONTEXT
    contextual_qa_prompt_template: PromptTemplate = BASIC_QA
    validation_prompt_template: PromptTemplate = VALIDATION_PROMPT
    should_validate: bool = True


class PromptEngineConfig(BasePromptEngineConfig):
    data_model = PromptEngineConfigModel


class PromptEngine(BasePromptEngine):
    config_class = PromptEngineConfig

    def get_prompt_template(
        self,
        promptType: Union[PromptTypeEnum, str],
        query: str,
    ) -> PromptTemplate:
        """
        This method returns the prompt template for the given prompt type. It validates the prompt if shouldValidate is
        True. If the prompt is not valid, then a ValueError is raised. If the query fails to validate, then a
        ValueError is raised.

        args:
            promptType: PromptTypeEnum
                The type of prompt to be returned.
            query: str
                The query to be used to generate the prompt.
        returns:
            prompt_template: PromptTemplate
                The prompt template to be used to generate the prompt.
        """
        if self.config.should_validate:
            validation_response = self.validate_prompt(query)
            if not validation_response["decision"]:
                raise ValueError(f"Prompt is not valid: {validation_response['reason']}")
        if type(promptType) == str:
            promptType = PromptTypeEnum(promptType)
        prompt_type_mapping = {
            PromptTypeEnum.SIMPLE_CHAT_PROMPT: self.config.simple_chat_prompt_template,
            PromptTypeEnum.CONTEXTUAL_CHAT_PROMPT: self.config.contextual_chat_prompt_template,
            PromptTypeEnum.CONTEXTUAL_QA_PROMPT: self.config.contextual_qa_prompt_template,
        }
        prompt_template = prompt_type_mapping.get(promptType)
        if prompt_template is None:
            raise ValueError(f"Invalid promptType: {promptType}")
        return prompt_template

    def validate_prompt(self, text: str) -> ValidationResponseDict:
        """
        This method is used to validate a prompt. It is used to check whether a prompt is safe to be sent to the
        language model.

        args:
            text: str
                The text to be validated.
        returns:
            response: Union[None, ResponseDict]
                If shouldValidate is False, then None is returned. If shouldValidate is True, then a ResponseDict is
                returned. The ResponseDict contains the following keys:
                    decision: bool
                        True if the prompt is safe to be sent to the language model, False if the prompt is not safe
                        to be sent to the language model.
                    reason: str
                        The reason for the decision.
                    response: str
                        The response to be sent to the user who entered the prompt.
        """
        decision_schema = ResponseSchema(
            name="decision",
            description="What is your decision? Answer True if yes False if not or unknown."
        )
        reason_schema = ResponseSchema(
            name="reason",
            description="Reason for you decision."
        )
        response_schema = ResponseSchema(
            name="response",
            description="Response to the person who entered the prompt."
        )
        output_parser = StructuredOutputParser.from_response_schemas([
            decision_schema,
            reason_schema,
            response_schema
        ])
        format_instructions = output_parser.get_format_instructions()
        message = self.config.validation_prompt_template.format_prompt(
            text=text,
            format_instructions=format_instructions
        )
        response = self.mediator.get_model_response(message.text)
        return output_parser.parse(response['output'])
