from bot.utilities.show_menu import show_contacts_menu
from bot.utilities.get_args import get_args

def contacts_handler(manager):
    """
    Handler for contacts commands.

    This function will prompt the user to enter commands to manage contacts.

    Available commands:
    - "add" - to add a new contact
    - "change" - to change contact info
    - "delete" - to delete a contact
    - "remove" - to remove a phone number or email
    - "all" - to show all contacts
    - "find" - to find a contact
    - "commands" or "menu" or "help" or "0" - to show this menu again
    - "back" or "return" or "r"  - to return to the main menu
    """
    return_to_main = False
    contacts_commands = ["add", "change", "delete", "remove", "all", "find"]
    help_commands = ["back", "0", "return", "r", "commands", "menu", "help"]
    contacts_promt = "Enter a contacts command: "

    show_contacts_menu()

    while not return_to_main:
        command, args = get_args(contacts_promt)

        if command not in contacts_commands and command not in help_commands:
            print("Please provide a command and/or arguments.")

        if command not in help_commands and command != "all":
            try:
                normalized_arg = args[0].casefold()
                check_data = any(normalized_arg == key.casefold() for key in manager.data.keys())
            except IndexError:
                print("Error parsing input: empty input")
            except ValueError as e:
                raise ValueError(f"Error parsing input: {e}")
            

        if command in ["back", "return", "r", ]:
            print("Returning to main menu...")
            return_to_main = True
        elif command == "add":
            if len(args) == 1 and not check_data:
                print("Adding new contact...")
                print(manager.add_record(args[0]))
            elif len(args) > 1 and check_data:
                contact_subaction_handler(manager, command, contact=args[0], action=args[1], new_info=args[2])
            else:
                print("Please provide a valid add command")
                continue
        elif command == "change":
            if len(args) < 3:
                print("Please provide a contact name and type to change: change <Contact name> phone <old_phone> <new_phone>\nOR\nchange <Contact name> birthday <birthday>")
                continue
            if not check_data:
                print("Please create a contact before changing.")
                continue
            contact_subaction_handler(manager, command, contact=args[0], action=args[1], old_info=args[2], new_info=args[3]) if len(args) == 4 else contact_subaction_handler(manager, command, contact=args[0], action=args[1], new_info=args[2])
        elif command == "delete":
            if len(args) < 1:
                print("Please provide a contact name: delete <Contact name>")
                continue
            print("Deleting contact...")
            print(manager.delete(args[0]))
        elif command == "remove":
            if len(args) < 2:
                print("Please provide a contact name and type to remove: remove <Contact name> <type>")
                continue
            contact_subaction_handler(manager,command, action=args[1], contact=args[0], old_info=args[2]) if len(args) == 3 else contact_subaction_handler(manager, command, action=args[1], contact=args[0])
        elif command == "all":
            print(manager.list_contacts())
        elif command == "find":
            if len(args) < 1:
                print("Please provide a contact name: find <Contact name>")
                continue
            print("Finding contact...")
            print(manager.find_contact(args[0]))
        elif command in ["commands", "menu", "help", "0"]:
            show_contacts_menu()

def contact_subaction_handler(manager, command, action, contact=None, new_info=None, old_info=None):
    """
    Handles contact subactions such as adding, changing, and removing contact details.

    Args:
        manager: The manager instance that handles contact operations.
        command (str): The command type, e.g., "add", "change", or "remove".
        action (str): The specific action to be performed, e.g., "email", "phone".
        contact (str, optional): The name of the contact. Defaults to None.
        new_info (str, optional): The new information to be added or updated. Defaults to None.
        old_info (str, optional): The existing information to be changed or removed. Defaults to None.

    Raises:
        TypeError: Raised when invalid arguments are provided.
        ValueError: Raised when there is an error performing the subaction.
    """

    action_map = {
        "add": {
            "email": manager.add_email,
            "phone": manager.add_phone,
            "address": manager.add_address,
            "birthday": manager.add_birthday,
        },
        "change": {
            "email": manager.change_email,
            "phone": manager.change_phone,
            "address": manager.change_address,
            "birthday": manager.change_birthday,
        },
        "remove": {
            "phone": manager.remove_phone,
            "email": manager.remove_email,
            "address": manager.remove_address,
            "birthday": manager.remove_birthday,
        }
    }
    try:
        multiple_lists = ["phone", "email"]
        if command in action_map and action in action_map[command]:
            print(f"Try to {command.capitalize()} {action}...")
            if command == "remove" and action in multiple_lists:
                print(action_map[command][action](contact, old_info))
            elif command == "remove":
                print(action_map[command][action](contact))
            elif command == "change" and action in multiple_lists:
                print(action_map[command][action](contact, old_info, new_info))
            else:
                print(action_map[command][action](contact, new_info))
        else:
            print(f"Invalid action or command: {action} {command}")
    except (TypeError, ValueError) as e:
        print(f"Invalid arguments provided. {e}")