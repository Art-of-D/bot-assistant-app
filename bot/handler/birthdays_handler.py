def birthdays_handler(command, args, manager):
    if command == "show-birthday":
        print("Showing a birthday...")
        manager.show_birthday(args[0])
    elif command == "birthdays":
        print("Showing upcoming birthdays...")
        manager.birthdays()