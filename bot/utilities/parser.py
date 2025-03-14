import shlex

def parse_input(user_input):
    """
    Parse the user's input into a command and arguments.

    Args:
        user_input (str): The user's input.

    Returns:
        tuple: A tuple of the command and arguments. If the user entered no command, returns ("commands", []).
    """
    if not user_input:
        print("Please enter a command.")
        return "commands", []

    try:
        tokens = shlex.split(user_input)
        cmd = tokens[0].strip().lower() if tokens else "commands"
        args = tokens[1:] if len(tokens) > 1 else []
        return cmd, args
    except ValueError as e:
        print(f"Error parsing input: {e}")
        return "commands", []
