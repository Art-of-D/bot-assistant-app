import pickle
from bot.internal.manager import Manager
from bot.internal.note.notes import Notes

def load_contacts(filepath="./bot/storage/data.pkl"):
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
    try:
        with open(filepath, "wb") as file:
            print("Saving contacts...")
            pickle.dump(data, file)
            print("Contacts saved successfully.")
    except Exception as e:
        print(f"Error saving contacts: {e}")

def load_notes(filepath="./bot/storage/notes.pkl"):
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
    try:
        with open(filepath, "wb") as file:
            print("Saving notes...")
            pickle.dump(data, file)
            print("Notes saved successfully.")
    except Exception as e:
        print(f"Error saving notes: {e}")