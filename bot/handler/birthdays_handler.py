def birthdays_handler(command, args, manager):
    if command == "show-birthday":
        print("Showing a birthday...")
        print(manager.show_birthday(args[0]))
        return
    elif command == "birthdays":
        print("Showing upcoming birthdays...")
        print(manager.show_upcoming_birthdays(args[0]))
        return