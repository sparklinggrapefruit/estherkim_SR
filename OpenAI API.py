import openai

from openai.types import Completion, CompletionChoice, CompletionUsage
from openai.types import ChatModel

from openai.types.chat import (
    ChatCompletion,
    ChatCompletionAssistantMessageParam,
    ChatCompletionChunk,
    ChatCompletionContentPartParam,
    ChatCompletionContentPartImageParam,
    ChatCompletionContentPartRefusalParam,
    ChatCompletionContentPartTextParam,
    ChatCompletionFunctionCallOptionParam,
    ChatCompletionFunctionMessageParam,
    ChatCompletionMessage,
    ChatCompletionMessageParam,
    ChatCompletionMessageToolCall,
    ChatCompletionNamedToolChoiceParam,
    ChatCompletionRole,
    ChatCompletionStreamOptionsParam,
    ChatCompletionSystemMessageParam,
    ChatCompletionTokenLogprob,
    ChatCompletionToolParam,
    ChatCompletionToolChoiceOptionParam,
    ChatCompletionToolMessageParam,
    ChatCompletionUserMessageParam,
)