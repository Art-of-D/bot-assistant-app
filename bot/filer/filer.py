import pickle
from bot.internal.manager import Manager

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