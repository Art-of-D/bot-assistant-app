from bot.utilities.show_menu import show_birthdays_menu
from bot.utilities.get_args import get_args

def birthdays_handler(manager):
    return_to_main = False
    birthdays_handler_promt = "Enter a birthdays command: "

    show_birthdays_menu()
    while not return_to_main:
        command, args = get_args(birthdays_handler_promt)

        if command in ["back", "return", "r"]:
            print("Returning to main menu...")
            return_to_main = True
        elif command == "show-birthday":
            if len(args) < 1:
                print("Please provide a contact name: show-birthday <Contact name>")
                continue
            print("Showing a birthday...")
            print(manager.show_birthday(args[0]))
        elif command == "birthdays":
            if len(args) < 1:
                print("Please provide a number of days ahead: birthdays <days-ahead>")
                continue
            print("Showing upcoming birthdays...")
            print(manager.show_upcoming_birthdays(args[0]))
        elif command in ["commands", "menu", "help", "0"]:
                show_birthdays_menu()