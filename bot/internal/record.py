"""
Module for class Record.
"""
from typing import List, Optional
from bot.internal.email import Email
from bot.internal.name import Name
from bot.internal.phone import Phone
from bot.internal.birthday import Birthday
from bot.internal.address import Address

class Record():
    """
    Class to represent a record in the address book.

    Attributes:
        name (Name): The name of the contact.
        phones (List[Phone]): The list of phone numbers associated with the contact.
        emails (List[Email]): The list of email addresses associated with the contact.
        birthday (Optional[Birthday]): The birthday of the contact.
        address (Optional[Address]): The address of the contact.
    """

    def __init__(self, name: str):
        """
        Initializes a Record instance.

        Args:
            name (str): The name of the contact.
        """
        self.name = Name(name)
        self.phones: List[Phone] = []
        self.emails: List[Email] = []
        self.birthday: Optional[Birthday] = None
        self.address: Optional[Address] = None

    def __getstate__(self):
        """
        Prepares the object's state for serialization.
        Returns:
        dict: The state of the object.
        """
        state = self.__dict__.copy()
        return state

    def __setstate__(self, state):
        """
        Restores the object's state from serialized data.
        Args:
        state (dict): The serialized state of the object.
        """
        self.__dict__.update(state)

    def add_phone(self, phone: str) -> None:
        """
        Adds a phone number to the contact.

        Args:
            phone (str): The phone number to add.
        """
        self.phones.append(Phone(phone))

    def remove_phone(self, phone: str) -> bool:
        """
        Removes a phone number from the contact.

        Args:
            phone (str): The phone number to remove.

        Returns:
            bool: True if the phone was removed, False if it was not found.
        """
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)
                return True
        return False

    def edit_phone(self, old_phone: str, new_phone: str) -> bool:
        """
        Edits an existing phone number.

        Args:
            old_phone (str): The phone number to replace.
            new_phone (str): The new phone number.

        Returns:
            bool: True if the phone was updated, False if the old phone was not found.
        """
        for p in self.phones:
            if p.value == old_phone:
                self.phones.remove(p)
                self.phones.append(Phone(new_phone))
                return True
        return False

    def add_email(self, email: str) -> None:
        """
        Adds an email address to the contact.

        Args:
            email (str): The email address to add.
        """
        self.emails.append(Email(email))

    def remove_email(self, email: str) -> bool:
        """
        Removes an email address from the contact.

        Args:
            email (str): The email address to remove.

        Returns:
            bool: True if the email was removed, False if it was not found.
        """
        for e in self.emails:
            if e.value == email:
                self.emails.remove(e)
                return True
        return False

    def edit_email(self, old_email: str, new_email: str) -> bool:
        """
        Edits an existing email address.

        Args:
            old_email (str): The email address to replace.
            new_email (str): The new email address.

        Returns:
            bool: True if the email was updated, False if the old email was not found.
        """
        for e in self.emails:
            if e.value == old_email:
                self.emails.remove(e)
                self.emails.append(Email(new_email))
                return True
        return False

    def add_birthday(self, birthday: str) -> None:
        """
        Adds or updates the birthday of the contact.

        Args:
            birthday (str): The birthday to add.
        """
        self.birthday = Birthday(birthday)

    def remove_birthday(self) -> None:
        """
        Removes the birthday of the contact.
        """
        self.birthday = None

    def edit_birthday(self, birthday: str) -> None:
        """
        Edits the birthday of the contact.

        Args:
            birthday (str): The new birthday.
        """
        self.birthday = Birthday(birthday)

    def add_address(self, address: str) -> None:
        """
        Adds or updates the address of the contact.

        Args:
            address (str): The address to add.
        """
        self.address = Address(address)

    def remove_address(self) -> None:
        """
        Removes the address of the contact.
        """
        self.address = None

    def edit_address(self, address: str) -> None:
        """
        Edits the address of the contact.

        Args:
            address (str): The new address.
        """
        self.address = Address(address)

    def get_name(self) -> str:
        """
        Returns the name of the contact.

        Returns:
            str: The name of the contact.
        """        
        return self.name.get_value()
    
    def get_phones(self) -> list:
        """
        Returns the phone numbers of the contact.

        Returns:
            list: The phone numbers of the contact.
        """
        if self.phones is None:
            return []
        try:
            return [phone.get_value() for phone in self.phones]
        except AttributeError:
            return []
    
    def get_emails(self) -> list:
        """
        Returns the email addresses of the contact.

        Returns:
            list: The email addresses of the contact.
        """
        try:
            if self.emails is not None:
                return [email.get_value() for email in self.emails]
            else:
                return []
        except AttributeError:
            return []
    
    def get_birthday(self) -> Optional[str]:
        """
        Returns the birthday of the contact.

        Returns:
            str or None: The birthday of the contact, or None if not set.
        """
        if self.birthday is None:
            return None
        return self.birthday.get_birthday()
    
    def get_address(self) -> Optional[str]:
        """
        Returns the address of the contact.

        Returns:
            str or None: The address of the contact, or None if not set.
        """
        if self.address is None:
            return None
        try:
            return self.address.get_value()
        except AttributeError:
            return None
