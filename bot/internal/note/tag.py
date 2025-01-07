from bot.decorators.errorhandler import input_error
from bot.internal.field import Field


class Tag(Field):
    def __init__(self, tag_value):
        # Ensure the tag_value is a valid string
        if not isinstance(tag_value, str):
            raise ValueError("Tag must be a string.")
        if not tag_value.strip():
            raise ValueError("Tag cannot be empty or just whitespace.")
        # Call the constructor of the parent class Field to set the value
        super().__init__(tag_value)

    def __str__(self):
        # Return the string representation of the Tag
        return f"Tag: {self.value}"

    @input_error
    def validate(self):
        # Additional validation specific to Tag can be added here
        if len(self.value) > 50:
            raise ValueError("Tag cannot exceed 50 characters.")
    @input_error
    def edit(self, new_value):
        # Validate and set the new tag value
        if not isinstance(new_value, str):
            raise ValueError("New tag value must be a string.")
        if not new_value.strip():
            raise ValueError("New tag cannot be empty or just whitespace.")
        self.value = new_value