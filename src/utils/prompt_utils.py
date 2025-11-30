import os

def load_prompt(prompt_name: str) -> str:
    """
    Loads a prompt from the prompts/ directory.
    Args:
        prompt_name: The filename (e.g., 'planner_prompt.md')
    """
    # Get the project root directory (assuming this script is in src/utils/)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(os.path.dirname(current_dir))
    
    prompt_path = os.path.join(project_root, "prompts", prompt_name)
    
    try:
        with open(prompt_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"Prompt file not found at {prompt_path}")