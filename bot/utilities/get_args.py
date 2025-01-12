from bot.utilities.parser import parse_input

def get_args(prompt):
    input_value = input(prompt)
    if not input_value:
        return None, []
    command, args = parse_input(input_value)
    return command, args