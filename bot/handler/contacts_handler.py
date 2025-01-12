from bot.utilities.show_menu import show_contacts_menu
from bot.utilities.get_args import get_args

def contacts_handler(manager):
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
            normalized_arg = args[0].casefold()
            check_data = any(normalized_arg == key.casefold() for key in manager.data.keys())

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