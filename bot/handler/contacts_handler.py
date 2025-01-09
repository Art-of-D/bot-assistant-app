from bot.internal.record import Record

def contacts_handler(command, args, manager):
    if command not in ["add", "change", "delete", "remove", "all", "find"]:
            print("Please provide a command and arguments.")
            return

    if command != "all":
        normalized_arg = args[0].casefold()
        check_data = any(normalized_arg == key.casefold() for key in manager.data.keys())

    if command == "add":
        if len(args) == 1 and not check_data:
           print("Adding new contact...")
           print(manager.add_record(args[0]))
        elif len(args) > 1 and check_data:
            print("Adding email, phone, or address to contact")
            contact_subaction_handler(manager, command, contact=args[0], action=args[1], new_info=args[2])
        else:
            print("Please provide a valid add command")
        return
    elif command == "change":
        if not check_data:
            print("Please create a contact before changing.")
            return
        contact_subaction_handler(manager, command, contact=args[0], action=args[1], old_info=args[2], new_info=args[3]) if len(args) == 4 else contact_subaction_handler(manager, command, contact=args[0], action=args[1], new_info=args[2])
        return
    elif command == "delete":
        print("Deleting contact...")
        print(manager.delete(args[0]))
    elif command == "remove":
        contact_subaction_handler(manager,command, action=args[1], contact=args[0], old_info=args[2]) if len(args) == 3 else contact_subaction_handler(manager, command, action=args[1], contact=args[0])
        return
    elif command == "all":
        print(manager.list_contacts())
        return
    elif command == "find":
        print("Finding contact...")
        print(manager.find_contact(args[0]))
        return

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
                print(action, contact, new_info)
                print(action_map[command][action](contact, new_info))
        else:
            print(f"Invalid action or command: {action} {command}")
    except TypeError:
        print("Invalid arguments provided.")