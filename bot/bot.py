from bot.handler.contacts_handler import contacts_handler
from bot.handler.notes_handler import notes_handler
from bot.handler.birthdays_handler import birthdays_handler
from bot.filer.filer import load_contacts, record_contacts, load_notes, record_notes
from bot.utilities.parser import parse_input

def show_main_menu():
    print("""
Available main commands:
0. Help - Show commands
1. Contacts - Manage contacts
2. Notes - Manage notes
3. Birthdays - Manage birthdays
4. Exit - Exit the assistant
    """)


def show_contacts_menu():
    print("""
Contacts commands:
- To add a new contact - add <Contact name>
- To add email, phone, or address - add <Contact name> email <email> | phone <phone> | address <address> | birthday <birthday>
- To change contact info - change <Contact name> email <old_email> <new_email>| phone <old_phone> <new_phone> | address <address> | birthday <birthday>
- To delete a contact - delete <Contact name>
- To remove a phone number - remove <Contact name> phone <phone> | email <email> | address <address>
- To find a contact - find <Contact name> | phone <phone> | email <email> | address <address>
- To show all contacts - all
! To use command with field name/email/phone/address with multiple words use, example ~ add "John Smith" !
    """)


def show_notes_menu():
    print("""
Notes commands:
- To add a new note - note
- To add tag - tag <title> <tag>
- To show a specific note - show <title>
- To show a list of notes by tag - display <tag>
- To edit a note - edit <title> <note>
- To edit a note title - change <title> <new-title>
- To remove tag - remove <title> <tag>
- To delete a note - detete <title>
- To show all notes - notes
- To show all tags - tags
! To use command with field tag/title with multiple words use, example ~ tag "Super cool" !
    """)


def show_birthdays_menu():
    print("""
Birthdays commands:
1. To show a contact's birthday - show-birthday <Contact name>
2. To show all upcoming birthdays for the week - birthdays <days-ahead>
! To use command with field name with multiple words use, example ~ show-birthday "John Smith" !
    """)

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

        elif command in ["commands", "menu", "help" "0"]:
            show_commands = True

        elif command in ["contacts", "c", "1"]:
            show_contacts_menu()
            sub_input = input("Enter a contact command: ")
            sub_command, s_args = parse_input(sub_input)

            contacts_handler(sub_command, s_args, manager)
        elif command in ["notes", "n", "2"]:
            show_notes_menu()
            sub_input = input("Enter a notes command: ")
            sub_command, s_args = parse_input(sub_input)

            notes_handler(sub_command, s_args, notes)

        elif command in ["birthdays", "b", "3"]:
            show_birthdays_menu()
            sub_input = input("Enter a birthday command: ")
            sub_command, s_args = parse_input(sub_input)
        
            birthdays_handler(sub_command, s_args, manager)

        elif command == "hello":
            print("Hello! How can I help you today?")
        else:
            print("Invalid main command. Please try again.")

if __name__ == "__main__":
    main()