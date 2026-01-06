from google.genai import types
from client import client
from constant import MODEL_ID, DEFAULT_PARAMS
from prompt import system_instruction


# Function for generating text
def generate_text(
    prompt: str,
    temperature: float | None = None,
    top_p: float | None = None,
    top_k: int | None = None,
    max_tokens: int | None = None,
) -> str:
    """
    Summary:
        This function generates text using a language model by
        configuring generation parameters such as temperature,
        top-p, top-k, and maximum output tokens. If parameters
        are not explicitly provided, default values are used.

    Args:
        prompt (str):
            The input text prompt provided to the language model
            for generating a response.

        temperature (float | None):
            Controls randomness in text generation. If None,
            the default temperature value is used.

        top_p (float | None):
            Controls nucleus sampling probability. If None,
            the default top-p value is used.

        top_k (int | None):
            Limits the number of highest-probability tokens
            considered during generation. If None, the default
            top-k value is used.

        max_tokens (int | None):
            Maximum number of tokens to generate in the output.
            If None, the default maximum token value is used.

    Returns:
        str:
            The generated text output from the language model.
    """

    config = types.GenerateContentConfig(
        system_instruction=system_instruction,
        temperature=float(temperature) if temperature is not None else float(DEFAULT_PARAMS["temperature"]),
        top_p=float(top_p) if top_p is not None else float(DEFAULT_PARAMS["top_p"]),
        top_k=int(top_k) if top_k is not None else int(DEFAULT_PARAMS["top_k"]),
        max_output_tokens=int(max_tokens) if max_tokens is not None else int(DEFAULT_PARAMS["max_tokens"]),
    )

    response = client.models.generate_content(
        model=MODEL_ID,
        contents=prompt,
        config=config,
    )

    return response.text


# Self-consistency implementation
def self_consistency(prompt: str, runs: int = 4) -> list[str]:
    """
    Summary:
        This function applies a self-consistency strategy by
        generating multiple responses for the same prompt
        across several runs and collecting the outputs.

    Args:
        prompt (str):
            The input prompt for which multiple generated
            responses will be produced.

        runs (int):
            The number of times the text generation function
            is executed to obtain multiple outputs.

    Returns:
        list[str]:
            A list containing generated text outputs collected
            from multiple runs of the language model.
    """

    outputs = []

    for _ in range(runs):
        result = generate_text(prompt)  # ✅ DO NOT pass None
        if result:
            outputs.append(result)

    return outputs
