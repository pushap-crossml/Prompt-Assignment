from run_experiment import experiments
from constant import CONFIG_SETTINGS
from util import self_consistency
from prompt import *

# Main for running workflow
if __name__ == "__main__":
    prompt_selection = consistency_prompt

    # if prompt is consistency prompt
    if prompt_selection == consistency_prompt:
        consistency_output = self_consistency(prompt_selection)
        for lst in consistency_output:
            print(f'Output:\n{lst}\n\n')
    else:
        # for other prompts
        experiments(prompt_selection, CONFIG_SETTINGS)