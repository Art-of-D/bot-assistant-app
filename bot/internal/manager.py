import copy
from collections import UserDict
from bot.decorators.error_handler import input_error
from bot.internal.record import Record
from bot.internal.email import Email
from bot.internal.phone import Phone
from bot.internal.address import Address
from bot.internal.birthday import Birthday
from bot.utilities.upcoming_birthday import get_upcoming_birthdays

class Manager(UserDict):
    def __getstate__(self):
        return copy.deepcopy(self.__dict__)

    def __setstate__(self, state):
        self.__dict__.update(state)

    @input_error
    def add_record(self, name):
        new_record = Record(name)    
        self.data[name] = new_record
        return f"Contact '{name}' added successfully."
    
    @input_error
    def delete(self, name):
        if name in self.data:
            del self.data[name]
            return f"Contact '{name}' deleted successfully."
        return f"Contact '{name}' not found."

    @input_error
    def add_email(self, name, email):        
        try:
            new_email = Email(email)
            record = self.data[name]
            record.add_email(new_email)
            return f"Email for '{name}' added successfully."
        except ValueError as e:
            raise ValueError(f"Error adding email to '{name}': {e}")
        
    @input_error
    def add_phone(self, name, phone):
        try:
            new_phone = Phone(phone)
            record = self.data[name]
            record.add_phone(new_phone)            
            return f"Phone for '{name}' added successfully."
        except ValueError as e:
            raise ValueError(f"Error adding phone to '{name}': {e}")

    @input_error
    def add_address(self, name, address):
        try:
            new_address = Address(address)
            record = self.data[name]
            record.add_address(new_address)            
            return f"Address for '{name}' added successfully."
        except ValueError as e:
            raise ValueError(f"Error adding address to '{name}': {e}")
        
    @input_error
    def add_birthday(self, name, birthday):
        try:
            new_birthday = Birthday(birthday)
            record = self.data[name]
            record.add_birthday(new_birthday)            
            return f"Birthday for '{name}' added successfully."
        except ValueError as e:
            raise ValueError(f"Error adding birthdate to '{name}': {e}")    

    @input_error
    def change_email(self, name, old_email, new_email):
        try:
            email_to_save = Email(new_email)
            record = self.data[name]
            record.edit_email(old_email, email_to_save)
        except ValueError as e:
            raise ValueError(f"Error changing email for '{name}': {e}")
    
    @input_error
    def change_phone(self, name, old_phone, new_phone):
        try:
            phone_to_save = Phone(new_phone)
            record = self.data[name]
            record.edit_phone(old_phone, phone_to_save)
        except ValueError as e:
            raise ValueError(f"Error changing phone for '{name}': {e}")
    
    @input_error
    def change_address(self, name, address):
        try:
            new_address = Phone(address)
            record = self.data[name]
            record.edit_address(new_address)
        except ValueError as e:
            raise ValueError(f"Error changing address for '{name}': {e}")
    
    @input_error
    def change_birthday(self, name, birthday):
        try:
            new_birthday = Phone(birthday)
            record = self.data[name]
            record.edit_birthday(new_birthday)
        except ValueError as e:
            raise ValueError(f"Error changing birthday for '{name}': {e}")
    
    @input_error
    def remove_phone(self, name, phone):
        try:
            record = self.data[name]
            record.remove_phone(phone)
        except ValueError as e:
            raise ValueError(f"Error removing phone from '{name}': {e}")
    
    @input_error
    def remove_email(self, name, email):
        try:
            record = self.data[name]
            record.remove_email(email)
        except ValueError as e:
            raise ValueError(f"Error removing email from '{name}': {e}")
    
    @input_error
    def remove_address(self, name, address):
        try:
            record = self.data[name]
            record.remove_address(address)
        except ValueError as e:
            raise ValueError(f"Error removing address from '{name}': {e}")
    
    @input_error
    def remove_birthday(self, name, birthday):
        try:
            record = self.data[name]
            record.remove_birthday(birthday)
        except ValueError as e:
            raise ValueError(f"Error removing birthday from '{name}': {e}")
    
    def find_contact(self, keyword):
        results = [record for name, record in self.data.items() if keyword.lower() in name.lower()]
        return results if results else f"No contacts found for keyword '{keyword}'."
    
    def list_contacts(self):
        if not self.data:
            return "No contacts available."
        return "\n".join(f"{name}: {record}" for name, record in self.data.items())
        
    def show_birthday(self, name):
        record = self.data[name]
        if record and record.birthday:
            return f"{name}'s birthday is on {record.birthday}."
        return f"No birthday set for {name}."
    
    def show_upcoming_birthdays(self, days_ahead):
        records = self.data.items()
        upcoming_birthdays = get_upcoming_birthdays(records, days_ahead)
        if upcoming_birthdays:
            return "Upcoming birthdays: " + ", ".join(upcoming_birthdays)
        return "No upcoming birthdays."


  