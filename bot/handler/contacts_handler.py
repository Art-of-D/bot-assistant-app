from bot.internal.record import Record

def contacts_handler(command, args, manager):
    if len(args) == 0:
            print("Please provide a command and arguments.")
            return
    if command == "add":
        if len(args) == 1 and args[0] not in manager.data:
           new_contact = Record(args[0])
           print("Adding new contact...")
           print(manager.add_record(new_contact))
        elif len(args) > 1 and args[0] not in manager.data:
            contact_subaction_handler(manager, command, args[0], args[1:])
        else:
            print("Please provide a valid command")
        return
    elif command == "change":
        if args[0] not in manager.data:
            print("Please create a contact before changing.")
            return
        contact_subaction_handler(manager, command, args[0], args[1:])
        return
    elif command == "delete":
        print("Deleting contact...")
        print(manager.delete(args[0]))
    elif command == "remove":
        print("Removing phone number...")
        contact_subaction_handler(manager,command, args[0], args[1:])
        return
    elif command == "all":
        print("Showing all contacts...")
        print(manager.list_contacts())
        return
    elif command == "find":
        print("Finding contact...")
        contact_subaction_handler(manager, command, args[0], args[1:])
        return

def contact_subaction_handler(manager, action, command, args):
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
        },
        "find": {
            "phone": manager.find_phone,
            "email": manager.find_email,
            "address": manager.find_address,
            "birthday": manager.find_birthday,
        },
    }

    try:
        if action in action_map and command in action_map[action]:
            print(f"{action.capitalize()}ing {command}...")
            print(action_map[action][command](*args))
        else:
            print(f"Invalid action or command: {action} {command}")
    except TypeError:
        print("Invalid arguments provided.")