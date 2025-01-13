"""
Module for class Phone.
"""

from bot.internal.field import Field


class Name(Field):
    """
    A class representing a name field.

    Validates and stores a properly formatted name.
    """
    def __init__(self, name: str):
        validated_name = self.validate_name(name)
        super().__init__(validated_name)      

    def validate_name(self, value: str) -> str:
        """
        Validate the name to ensure it meets the criteria.
        
        Args:
            value (str): The name to validate.
        
        Returns:
            str: The validated name.
        
        Raises:
            ValueError: If the name contains invalid characters or is empty.
        """
        if not value.strip():
            raise ValueError("Name cannot be empty.")
        if not value.replace(" ", "").isalpha():
            raise ValueError("Name must contain only alphabetic characters.")
        return value.strip()
