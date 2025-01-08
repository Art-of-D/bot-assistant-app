import copy
from collections import UserDict
from bot.decorators.error_handler import input_error
from bot.internal.email import Email
from bot.internal.phone import Phone
from bot.internal.address import Address
from bot.internal.birthday import Birthday

class Manager(UserDict):
    def __getstate__(self):
        return copy.deepcopy(self.__dict__)

    def __setstate__(self, state):
        self.__dict__.update(state)

    @input_error
    def add_record(self, record):    
        self.data[record.name] = record
        return f"Contact '{record.name}' added successfully."

    @input_error
    def add_email(self, name, value):        
        try:
            email = Email(value)
            self.data[name].email = email
            return f"Email for '{name}' added successfully."
        except ValueError as e:
            raise ValueError(f"Error adding email to '{name}': {e}")
        
    @input_error
    def add_phone(self, name, value):
        try:
            phone = Phone(value)
            self.data[name].phone = phone
            return f"Phone for '{name}' added successfully."
        except ValueError as e:
            raise ValueError(f"Error adding phone to '{name}': {e}")

    @input_error
    def add_address(self, name, value):
        try:
            address = Address(value)
            self.data[name].address = address
            return f"Address for '{name}' added successfully."
        except ValueError as e:
            raise ValueError(f"Error adding address to '{name}': {e}")
        
    @input_error
    def add_birthday(self, name, value):
        try:
            birthday = Birthday(value)
            self.data[name].birthday = birthday
            return f"Birthday for '{name}' added successfully."
        except ValueError as e:
            raise ValueError(f"Error adding birthdate to '{name}': {e}")        

    def add_process_input(self, args):
        name = args[0]
        # if name not in self.data:
            # self.add_record() 
        i = 1
        while i < len(args):
            key = args[i]
            value = args[i + 1]
            if key == 'email':
                print(self.add_email(name, value))
            elif key == 'phone':
                print(self.add_phone(name, value))
            elif key == 'address':
                print(self.add_address(name, value))
            elif key == 'birthday':
                print(self.add_birthday(name, value))
            i += 2


  