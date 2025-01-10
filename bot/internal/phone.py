"""
Module for class Phone.
"""

import re
from bot.internal.field import Field
from bot.decorators.error_handler import input_error


class Phone(Field):
    """
    A class representing a phone field.

    Validates and stores a properly formatted phone number.
    """
    def __init__(self, number: str):
        validated_number = self.validate_phone(number)
        super().__init__(validated_number)    

   
    def validate_phone(self, number: str) -> str:
        """
        Validate the phone number to ensure it contains between 8 and 15 digits.

        Args:
            number (str): The phone number to validate.

        Returns:
            str: The validated phone number.

        Raises:
            ValueError: If the phone number is invalid.
        """
        if not re.match(r"^\+?\d{8,15}$", number.strip()):
            raise ValueError("Phone number should contain 8 to 15 digits and may start with '+'.")
        return number.strip()
