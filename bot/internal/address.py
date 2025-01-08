"""
Module for class Address.
"""

from bot.internal.field import Field
from bot.decorators.error_handler import input_error

class Address(Field):
    """
    A class representing an address field.

    Validates and stores a properly formatted address.
    """

    @input_error
    def __init__(self, address: str):
        super().__init__(address)