import copy
from collections import UserDict
from bot.decorators.error_handler import input_error
from bot.internal.record import Record
from bot.utilities.upcoming_birthday import get_upcoming_birthdays

class Manager(UserDict):
    def __getstate__(self):
        return copy.deepcopy(self.__dict__)

    def __setstate__(self, state):
        self.__dict__.update(state)

    @input_error
    def add_record(self, name):
        if name not in self.data:
            new_record = Record(name.casefold())    
            self.data[name.casefold()] = new_record
            return f"Contact '{name}' added successfully."
        else:
            return(f"Record already exists in the address book.")
            
    
    @input_error
    def delete(self, name):
        record = self.find_by_key(name)
        if record:
            del self.data[name.casefold()]
            return f"Contact '{name}' deleted successfully."
        return f"Contact '{name}' not found."

    @input_error
    def add_email(self, name, email):        
        try:            
            record = self.find_by_key(name)
            record.add_email(email)
            self.data[name.casefold()] = record
            return f"Email for '{name}' added successfully."
        except ValueError as e:
            raise ValueError(f"Error adding email to '{name}': {e}")
        
    @input_error
    def add_phone(self, name, phone):        
        try:
            record = self.find_by_key(name)
            record.add_phone(phone)   
            self.data[name.casefold()] = record                
            return f"Phone for '{name}' added successfully."
        except ValueError as e:
            raise ValueError(f"Error adding phone to '{name}': {e}")

    @input_error
    def add_address(self, name, address):
        try:
            record = self.find_by_key(name)
            record.add_address(address)      
            self.data[name.casefold()] = record      
            return f"Address for '{name}' added successfully."
        except ValueError as e:
            raise ValueError(f"Error adding address to '{name}': {e}")
        
    @input_error
    def add_birthday(self, name, birthday):
        try:
            record = self.find_by_key(name)
            record.add_birthday(birthday) 
            self.data[name.casefold()] = record
            return f"Birthday for '{name}' added successfully."
        except ValueError as e:
            raise ValueError(f"Error adding birthdate to '{name}': {e}")    

    @input_error
    def change_email(self, name, old_email, new_email):
        try:
            record = self.find_by_key(name)
            record.edit_email(old_email, new_email)
            self.data[name.casefold()] = record
            return f"Email for '{name}' changed successfully."
        except ValueError as e:
            raise ValueError(f"Error changing email for '{name}': {e}")
    
    @input_error
    def change_phone(self, name, old_phone, new_phone):        
        try:
            record = self.find_by_key(name)
            record.edit_phone(old_phone, new_phone)
            self.data[name.casefold()] = record
            return f"Phone for '{name}' changed successfully."
        except ValueError as e:
            raise ValueError(f"Error changing phone for '{name}': {e}")
       
    
    @input_error
    def change_address(self, name, address):
        try:
            record = self.find_by_key(name)
            record.edit_address(address)
            self.data[name.casefold()] = record
            return f"Address for '{name}' changed successfully."
        except ValueError as e:
            raise ValueError(f"Error changing address for '{name}': {e}")
    
    @input_error
    def change_birthday(self, name, birthday):
        try:
            record = self.find_by_key(name)
            record.edit_birthday(birthday)
            self.data[name.casefold()] = record
            return f"Birthday for '{name}' changed successfully."
        except ValueError as e:
            raise ValueError(f"Error changing birthday for '{name}': {e}")
    
    @input_error
    def remove_phone(self, name, phone):
        try:
            record = self.find_by_key(name)
            record.remove_phone(phone)
            self.data[name.casefold()] = record
            return f"Phone for '{name}' removed successfully."
        except ValueError as e:
            raise ValueError(f"Error removing phone from '{name}': {e}")
    
    @input_error
    def remove_email(self, name, email):
        try:
            record = self.find_by_key(name)
            record.remove_email(email)
            self.data[name.casefold()] = record
            return f"Email for '{name}' removed successfully."
        except ValueError as e:
            raise ValueError(f"Error removing email from '{name}': {e}")
    
    @input_error
    def remove_address(self, name):
        try:
            record = self.find_by_key(name)
            record.remove_address()
            self.data[name.casefold()] = record
            return f"Address for '{name}' removed successfully."
        except ValueError as e:
            raise ValueError(f"Error removing address from '{name}': {e}")
    
    @input_error
    def remove_birthday(self, name):
        try:
            record = self.find_by_key(name)
            record.remove_birthday()
            self.data[name.casefold()] = record
            return f"Birthday for '{name}' removed successfully."
        except ValueError as e:
            raise ValueError(f"Error removing birthday from '{name}': {e}")
    
    def find_contact(self, keyword):
        keyword_lower = keyword.lower()
        results = []
        for name, record in self.data.items():
            phones = ", ".join(str(phone) for phone in record.phones) if record.phones else "N/A"
            emails = ", ".join(str(email) for email in record.emails) if record.emails else "N/A"
            birthday = str(record.birthday) if record.birthday else "N/A"
            if (keyword_lower in name.lower() or 
                any(keyword_lower in str(phone).lower() for phone in record.phones) or 
                any(keyword_lower in str(email).lower() for email in record.emails) or 
                (getattr(record, 'address', '') and keyword_lower in str(record.address).lower())):
                results.append(f"Name: {name}, Phone: {phones}, Email: {emails}, Address: {getattr(record, 'address', 'N/A')} Birthday: {birthday}")
        return "\n".join(results) if results else f"No contacts found for keyword '{keyword}'."
        
    
    def list_contacts(self):
        if not self.data:
            return "No contacts available."
        contacts_list = []
        for name, record in self.data.items():
            phones = ", ".join(str(phone) for phone in record.get_phones()) if record.phones else "N/A"
            emails = ", ".join(str(email) for email in record.get_emails()) if record.emails else "N/A"
            address = str(record.address) if record.get_address() else "N/A"
            birthday = str(record.birthday) if record.get_birthday() else "N/A"
        
            details = f"Name: {name}, Phone: {phones}, Email: {emails}, Address: {address}, Birthday: {birthday}"
            contacts_list.append(details)
    
        return "\n".join(contacts_list)
        
    def show_birthday(self, name):
        record = self.find_by_key(name)
        if record and record.birthday:
            return f"{name}'s birthday is on {record.birthday}."
        return f"No birthday set for {name}."
    
    def show_upcoming_birthdays(self, days_ahead):
        records = self.data.items()
        upcoming_birthdays = get_upcoming_birthdays(records, days_ahead)
        if upcoming_birthdays:
            return "Upcoming birthdays:\n" + "\n".join(
            f"{entry['name']}, birthday: {entry['birthday_date']}" for entry in upcoming_birthdays
        )
        return "No upcoming birthdays."

    @input_error
    def find_by_key(self, key):
        key_casefold = key.casefold()
        for name, record in self.data.items():
            if name.casefold() == key_casefold:
                return record
        return None
  