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
- To show contact menu - menu / commands / help / 0
- To return to main menu - back / return / r
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
- To show notes menu - menu / commands / help / 0
- To return to main menu - back / return / r
! To use command with field tag/title with multiple words use, example ~ tag "Super cool" !
    """)


def show_birthdays_menu():
    print("""
Birthdays commands:
- To show a contact's birthday - show-birthday <Contact name>
- To show all upcoming birthdays for the week - birthdays <days-ahead>
- To show birthday menu - menu / commands / help / 0
- To return to main menu - back / return / r
! To use command with field name with multiple words use, example ~ show-birthday "John Smith" !
    """)