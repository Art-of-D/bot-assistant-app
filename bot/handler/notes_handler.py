def notes_handler(command, args, manager):
    if command == "note":
        adding_note(manager)
        return
    elif command == "tag":
        if len(args) < 2:
            print("Please provide a title and tag: tag <title> <tag>")
            return
        title, tag = args[0], args[1]
        print(f"Adding tag '{tag}' to note '{title}'...")
        manager.add_tag(title, tag)
    elif command == "show":
        if len(args) < 1:
            print("Please provide a title: show <title>")
            return
        title = args[0]
        print(f"Showing note: {title}...")
        manager.show_note(title)
    elif command == "display":
        if len(args) < 1:
            print("Please provide a tag: display <tag>")
            return
        tag = args[0]
        print(f"Displaying notes with tag '{tag}'...")
        manager.display_notes_by_tag(tag)
    elif command == "edit":
        if len(args) < 2:
            print("Please provide a title and new note content: edit <title> <note>")
            return
        title, note = args[0], " ".join(args[1:])
        print(f"Editing note '{title}'...")
        manager.edit_note(title, note)
    elif command == "delete":
        if len(args) < 1:
            print("Please provide a title: delete <title>")
            return
        title = args[0]
        print(f"Deleting note '{title}'...")
        manager.delete_note(title)
    elif command == "notes":
        print("Showing all notes...")
        manager.show_all_notes()
    elif command == "tags":
        print("Showing all tags...")
        manager.show_all_tags()
    else:
        print(f"Invalid command: {command}. Please try again.")

def adding_note(manager):
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
    print(f"Tag: {tag if tag else 'No tag'}")
    confirm = input("Do you want to save this note? (yes/no): ").strip().lower()
    if confirm in ["yes", "y", 1]:
        manager.add_note(title, note, tag)
        print(f"Note '{title}' has been added successfully.")
    else:
        print("Note was not saved.")