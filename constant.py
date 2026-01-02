# Model defining
MODEL_ID = "gemini-3-flash-preview"

# Default config if not given custom
DEFAULT_PARAMS = {
    "temperature": 0.7,
    "top_p": 0.9,
    "top_k": 30,
    "max_tokens": 1000
}

# Custom config
CONFIG_SETTINGS = [
        {"temperature": 0.2, "top_p": 0.9, "top_k":20, "max_tokens": 1000},
        # {"temperature": 0.7, "top_p": 0.9, "top_k":30, "max_tokens": 150},
        # {"temperature": 1.0, "top_p": 0.95, "top_k":50, "max_tokens": 200},
    ]