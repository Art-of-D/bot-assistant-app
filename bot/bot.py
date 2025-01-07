#from bot.internal.record import Record
from bot.filer.filer import load_contacts, record_contacts

def parse_input(user_input):
    if not user_input:
        print("Please enter a command.")
        return "commands", []
    else: 
        cmd, *args = user_input.split()
        cmd = cmd.strip().lower()
        return cmd, *args


def main():
    print("Welcome to the assistant bot!")
    manager = load_contacts()
    
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            record_contacts(manager)
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print("adding new contact")
            # new_contact = Record(args[0])
            # if len(args) > 1: 
            #     print(new_contact.add_phone(args[1]))

            # print(manager.add_record(new_contact))
        elif command == "change":
            print("change contact")
            # print(manager.edit_phone(args[0], args[1]))
        elif command == "delete":
            print("delete contact")
            # print(manager.delete(args[1]))
        elif command == "remove":
            print("delete phone")
            # print(manager.delete_phone(args[0], args[1]))
        elif command == "all":
            print("all contacts")
            # print(manager.list_contacts())
        elif command == "find":
            print("find contact")
            # print(manager.find(args[0]))
        elif command == "add-birthday":
            print("add birthday")
            # print(manager.add_birthday(args[0], args[1]))
        elif command == "show-birthday":
            print("show birthday")
            # print(manager.show_birthday(args[0]))
        elif command == "birthdays":
            print("show all birthdays")
            # print(manager.birthdays())
        elif command == "note":
            print("add note")
            # print(manager.add_note(args[0], args[1]))
        elif command == "notes":
            print("show all notes")
            # print(manager.notes())
        elif command == "tag":
            print("add tag")
            # print(manager.add_tag(args[0], args[1]))
        elif command == "delete-tag":
            print("delete tag")
            # print(manager.delete_tag(args[0], args[1]))
        elif command == "tags":
            print("show all tags")
            # print(manager.tags())
        elif command == "commands":
            print("Available commands:\n-hello - greetings\n-add - add new contact or new info for the contact\n-change - change contact info\n-delete - delete contact\n-remove - delete phone\n-all - show all contacts\n-find - find contact by name phone, email, address\n-show-birthday - show birthday of some contact\n-birthdays - show all birthdays on the week for your contacts\n-note - add new note\n-notes - show all notes\n-tag - add new tag\n-tags - show all tags\n-close OR exit")
        else:
            print("Invalid command. If you need help, type 'commands'.")

if __name__ == "__main__":
    main()