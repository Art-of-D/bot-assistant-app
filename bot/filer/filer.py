import pickle
from bot.internal.manager import Manager

def load_contacts(filepath="./bot/storage/data.pkl"):
    manager = Manager()
    try:
        with open(filepath, "rb") as file:
            print("Loading contacts...")
            contacts = pickle.load(file)
            if not isinstance(contacts, Manager):
                raise ValueError("Loaded data is not of type AddressBook.")
            return contacts
    except FileNotFoundError:
        print("No contacts found. Please add new contact.")
        return manager
    except (EOFError, ValueError) as e:
        print(f"Error loading contacts: {e}")
        return manager


def record_contacts(contacts, filepath="./bot/storage/data.pkl"):
    try:
        with open(filepath, "wb") as file:
            print("Saving contacts...")
            pickle.dump(contacts, file)
            print("Contacts saved successfully.")
    except Exception as e:
        print(f"Error saving contacts: {e}")