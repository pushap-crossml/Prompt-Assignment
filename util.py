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
    Generate text from a language model using configurable parameters.
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
    outputs = []

    for _ in range(runs):
        result = generate_text(prompt)  # ✅ DO NOT pass None
        if result:
            outputs.append(result)

    return outputs
