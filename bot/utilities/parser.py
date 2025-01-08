import shlex

def parse_input(user_input):
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
