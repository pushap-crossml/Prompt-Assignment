from util import generate_text


# running experiments with different config values
def experiments(prompt:str,custom_config:dict) -> None:
    """
    Summary:
        This function iterates over each configuration provided in
        `custom_config`, passes the parameters to the `generate_text`
        function, and prints the generated output along with the
        corresponding configuration.

    Args:
        custom_config (dict):
            A dictionary (or iterable of dictionaries) containing
            keyword arguments for the `generate_text` function
            such as temperature, top_p, top_k, and max_tokens.

    Returns:
        None:
            The function does not return any value.
            Results are printed directly to the console.
    """
    # for getting every custom config
    for cs in custom_config:
        output = generate_text(prompt, **cs)
        print(f"Param:{cs}\nOutput:\n{output}")