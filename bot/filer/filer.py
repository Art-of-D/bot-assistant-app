import pickle
from bot.internal.manager import Manager
from bot.internal.note.notes import Notes

def load_contacts(filepath="./bot/storage/data.pkl"):
    """
    Loads the contacts from a binary file.

    The file is expected to be a serialized AddressBook object. If the file does not exist,
    a new AddressBook object is returned.

    Args:
        filepath (str): The path to the file to load from. Defaults to "./bot/storage/data.pkl".

    Returns:
        AddressBook: The loaded AddressBook object.

    Raises:
        ValueError: If the loaded data is not an AddressBook object.
        EOFError: If the file is empty.
    """
    manager = Manager()
    try:
        with open(filepath, "rb") as file:
            print("Loading data...")
            data = pickle.load(file)
            if not isinstance(data, Manager):
                raise ValueError("Loaded data is not of type AddressBook.")
            return data
    except FileNotFoundError:
        print("No contacts found. Please add new contact.")
        return manager
    except (EOFError, ValueError) as e:
        print(f"Error loading contacts: {e}")
        return manager


def record_contacts(data, filepath="./bot/storage/data.pkl"):
    """
    Saves the contacts to a binary file.

    The file is expected to be a serialized AddressBook object. If the file does not exist,
    a new file is created.

    Args:
        data (AddressBook): The AddressBook object to save.
        filepath (str): The path to the file to save to. Defaults to "./bot/storage/data.pkl".

    Raises:
        ValueError: If the data is not of type AddressBook.
        Exception: If there is an error saving the data.
    """
    try:
        with open(filepath, "wb") as file:
            print("Saving contacts...")
            pickle.dump(data, file)
            print("Contacts saved successfully.")
    except Exception as e:
        print(f"Error saving contacts: {e}")

def load_notes(filepath="./bot/storage/notes.pkl"):
    """
    Loads notes from a binary file.

    The file is expected to be a serialized Notes object. If the file does not exist,
    a new file is created.

    Args:
        filepath (str): The path to the file to load from. Defaults to "./bot/storage/notes.pkl".

    Returns:
        Notes: The loaded Notes object.

    Raises:
        ValueError: If the loaded data is not of type Notes.
        Exception: If there is an error loading the data.
    """
    try:
        with open(filepath, "rb") as file:
            print("Loading notes...")
            data = pickle.load(file)
            if not isinstance(data, Notes):
                raise ValueError("Loaded data is not of type Notes.")
            return data
    except FileNotFoundError:
        print("No notes found. Please add new note.")
        return Notes()
    except (EOFError, ValueError) as e:
        print(f"Error loading notes: {e}")
        return Notes()

def record_notes(data, filepath="./bot/storage/notes.pkl"):
    """
    Saves the notes to a binary file.

    The notes are serialized and written to the specified file path.

    Args:
        data (Notes): The Notes object to be saved.
        filepath (str): The path to the file to save to. Defaults to "./bot/storage/notes.pkl".

    Raises:
        Exception: If there is an error during the saving process.
    """

    try:
        with open(filepath, "wb") as file:
            print("Saving notes...")
            pickle.dump(data, file)
            print("Notes saved successfully.")
    except Exception as e:
        print(f"Error saving notes: {e}")