import uuid

from bot.decorators.errorhandler import input_error
from bot.internal.field import Field
from bot.internal.note.tag import Tag

class Note(Field):
    def __init__(self, title_value=None, tag_value=None):
        # Title is mandatory; if not provided, generate it automatically
        if title_value is None:
            # Generate a unique title using UUID if no title is provided
            title_value = f"Note-{str(uuid.uuid4())[:8]}"  # First 8 characters of UUID

        if not isinstance(title_value, str) or not title_value.strip():
            raise ValueError("Title must be a non-empty string.")
        
        # If Tag is provided, validate it; otherwise, set it as None
        if tag_value is not None:
            self.tag = Tag(tag_value)
        else:
            self.tag = None
        
        # Initialize the Field parent class with the title as value
        super().__init__(title_value)

    def __str__(self):
        # Return the string representation of the Note, include Tag if it exists
        tag_str = f", Tag: {self.tag.value}" if self.tag else ""
        return f"Note: {self.value}{tag_str}"
    
    @input_error
    def validate(self):
        # Validate title length (max 200 characters)
        if len(self.value) > 200:
            raise ValueError("Title cannot exceed 200 characters.")
    
    @input_error
    def edit(self, new_title):
        # Validate and set the new title value
        if not isinstance(new_title, str) or not new_title.strip():
            raise ValueError("New title must be a non-empty string.")
        self.value = new_title  # Update the value of the title
