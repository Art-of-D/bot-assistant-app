from bot.utilities.get_args import get_args
from bot.utilities.show_menu import show_notes_menu

def notes_handler(notes):
    return_to_main = False
    notes_promt = "Enter a notes command: "
    
    show_notes_menu()
    
    while not return_to_main:
        command, args = get_args(notes_promt)

        if command in ["back", "return", "r"]:
            print("Returning to main menu...")
            return_to_main = True
        elif command == "note":
            print(adding_note(notes))
        elif command == "tag":
            if len(args) < 2:
                print("Please provide a title and tag: tag <title> <tag>")
                continue 
            title, tag = args[0], args[1]
            print(f"Adding tag '{tag}' to note '{title}'...")
            print(notes.add_tag(title, tag))
        elif command == "show":
            if len(args) < 1:
                print("Please provide a title: show <title>")
                continue 
            title = args[0]
            print(f"Showing note: {title}...")
            print(notes.get_note(title))
        elif command == "display":
            if len(args) < 1:
                print("Please provide a tag: display <tag>")
                continue
            tag = args[0]
            print(f"Displaying notes with tag '{tag}'...")
            print(notes.display_notes_by_tag(tag))
        elif command == "edit":
            if len(args) < 2:
                print("Please provide a title and note: edit <title> <note>")
                continue
            title, note = args[0], " ".join(args[1:])
            print(f"Editing note '{title}'...")
            print(notes.edit_note(title, note))
        elif command == "change":
            if len(args) < 2:
                print("Please provide a title and a new title: change <title> <new-title>")
                continue
            old_title, new_title = args[0], args[1]
            print(f"Changing title '{old_title}' to '{new_title}'...")
            print(notes.edit_title(old_title, new_title))
        elif command == "delete":
            if len(args) < 1:
                print("Please provide a title: delete <title>")
                continue
            title = args[0]
            print(f"Deleting note '{title}'...")
            print(notes.delete_note(title))
        elif command == "remove":
            if len(args) < 2:
                print("Please provide a title and a tag: remove <title> <tag>")
                continue
            title, tag = args[0], args[1]
            print(f"Removing tag '{tag}' from note '{title}'...")
            print(notes.delete_tag(title, tag))
        elif command == "notes":
            print("Showing all notes...")
            print(notes.get_all_notes())
        elif command == "tags":
            print("Showing all tags...")
            print(notes.get_all_tags())
        elif command in ["commands", "menu", "help", "0"]:
            show_notes_menu()
        else:
            print(f"Invalid command: {command if command != None else "empty command"}. Please try again.")

def adding_note(notes):
    title = input("Enter the title of the note: ").strip()
    if not title:
        print("Title cannot be empty.")
        return

    note = input("Enter the content of the note: ").strip()
    if not note:
        print("Note content cannot be empty.")
        return

    add_tag = input("Do you want to add a tag? (yes/no): ").strip().lower()
    tag = ""
    if add_tag in ["yes", "y", 1]:
        tag = input("Enter the tag: ").strip()
        if not tag:
            print("Skipping tag... You can add a tag later.")

    print("\nReview your note:")
    print(f"Title: {title}")
    print(f"Note: {note}")
    print(f"Tag: {tag if tag else None}")
    confirm = input("Do you want to save this note? (yes/no): ").strip().lower()
    if confirm in ["yes", "y", 1]:
        try:
            return notes.add_note(title, note, tag)
        except ValueError as e:
            print(f"Error: {str(e)}")
        