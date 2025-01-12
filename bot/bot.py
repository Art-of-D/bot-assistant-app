from bot.handler.contacts_handler import contacts_handler
from bot.handler.notes_handler import notes_handler
from bot.handler.birthdays_handler import birthdays_handler
from bot.filer.filer import load_contacts, record_contacts, load_notes, record_notes
from bot.utilities.parser import parse_input
from bot.utilities.show_menu import show_main_menu, show_contacts_menu, show_notes_menu, show_birthdays_menu

def main():
    print("Welcome to the assistant bot!")
    manager = load_contacts()
    notes = load_notes()
    show_commands = True
    while True:
        show_main_menu() if show_commands else None
        show_commands = False
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["exit", "close", "e", "4"]:
            record_contacts(manager)
            record_notes(notes)
            print("Goodbye!")
            break

        elif command in ["commands", "menu", "help", "0"]:
            show_commands = True

        elif command in ["contacts", "c", "1"]:
            contacts_handler(manager)
        elif command in ["notes", "n", "2"]:
            notes_handler(notes)

        elif command in ["birthdays", "b", "3"]:
            birthdays_handler(manager)

        elif command == "hello":
            print("Hello! How can I help you today?")
        else:
            print("Invalid main command. Please try again.")

if __name__ == "__main__":
    main()