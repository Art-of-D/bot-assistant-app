"""
Module for class Email.
"""

import re
from bot.internal.field import Field

class Email(Field):
    """
    A class representing an email field.

    Validates and stores a properly formatted email address.
    """
    def __init__(self, email: str):
        validated_email = self.validate_email(email)
        super().__init__(validated_email)
        

    def validate_email(self, email: str) -> str:
        """
        Validate the email address to ensure it conforms to standard email format.

        Args:
            email (str): The email address to validate.

        Returns:
            str: The validated email address.

        Raises:
            ValueError: If the email address is invalid.
        """
        if not re.match(r"^[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,}$", email.strip()):
            raise ValueError("Invalid email address format.")
        else:
            return email.strip()