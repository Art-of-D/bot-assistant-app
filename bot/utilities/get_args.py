from bot.utilities.parser import parse_input

def get_args(prompt):
    """
    Get arguments from user input.

    Asks the user for input, parses it into a command and arguments, and
    returns them.

    Args:
        prompt (str): The prompt to display to the user.

    Returns:
        tuple: A tuple of the command and arguments, or None and an empty
        list if the user didn't enter anything.
    """
    input_value = input(prompt)
    if not input_value:
        return None, []
    command, args = parse_input(input_value)
    return command, args