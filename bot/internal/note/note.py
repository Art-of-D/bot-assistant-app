from bot.decorators.error_handler import input_error
from bot.internal.field import Field
from bot.internal.note.tag import Tag

class Note(Field):
    MAX_TAGS = 10  # Maximum allowed number of tags

    def __init__(self, title_value, tags=None):
        # Initialize the Note instance with a title and optional tags
        # Validate the title (must be a non-empty string)
        if not title_value or not isinstance(title_value, str) or not title_value.strip():
            raise ValueError("Title must be a non-empty string.")

        # Validate the tags (optional, must be a list of non-empty strings if provided)
        if tags is None:
            self.tags = []  # Default to an empty list if no tags are provided
        elif isinstance(tags, list) and all(isinstance(tag, str) and tag.strip() for tag in tags):
            self.tags = [Tag(tag.strip()) for tag in tags]
            if len(self.tags) > self.MAX_TAGS:
                raise ValueError(f"Cannot have more than {self.MAX_TAGS} tags.")
        else:
            raise ValueError("Tags must be a list of non-empty strings.")

        # Initialize the base Field class with the title value
        super().__init__(value=title_value)
        self.text = ""  # Initialize the note text as an empty string

    def __str__(self):
        # Provide a string representation of the Note, including the title, text, and tags
        tags_str = ", ".join(tag.value for tag in self.tags) if self.tags else "No tags"
        return f"Title: {self.value}\nText:\n{self.text}\nTags:\n[{tags_str}]"

    def validate(self):
        # Validate the Note instance
        # Ensure the title does not exceed 200 characters
        if len(self.value) > 200:
            raise ValueError("Title cannot exceed 200 characters.")
        # Ensure the number of tags does not exceed the maximum limit
        if len(self.tags) > self.MAX_TAGS:
            raise ValueError(f"Cannot have more than {self.MAX_TAGS} tags.")

    def edit_title(self, new_title):
        # Update the title with validation
        if not new_title or not isinstance(new_title, str) or not new_title.strip():
            raise ValueError("New title must be a non-empty string.")
        self.value = new_title  # Update the title value

    def edit_note(self, new_note):
        # Update the note text
        self.text = new_note

    def add_tag(self, new_tag):
        # Add a new tag to the Note
        if not new_tag or not isinstance(new_tag, str) or not new_tag.strip():
            raise ValueError("Tag must be a non-empty string.")
        if len(self.tags) >= self.MAX_TAGS:
            raise ValueError(f"Cannot add more than {self.MAX_TAGS} tags.")
        if any(tag.value == new_tag.strip() for tag in self.tags):
            raise ValueError("Tag already exists.")
        self.tags.append(Tag(new_tag.strip()))  # Add the new tag

    def remove_tag(self, tag_to_remove):
        # Remove a specific tag from the Note
        if not tag_to_remove or not isinstance(tag_to_remove, str) or not tag_to_remove.strip():
            raise ValueError("Tag to remove must be a non-empty string.")
        for tag in self.tags:
            if tag.value == tag_to_remove.strip():
                self.tags.remove(tag)  # Remove the tag if found
                return
        raise ValueError("Tag not found.")

    def get_tags(self):
        # Return a list of tags if they exist, otherwise return None
        return [tag.value for tag in self.tags] if len(self.tags) > 0 else None

    def get_title(self):
        # Return the title value
        return self.value

    def get_note(self):
        # Return the title, note text, and tags as a dictionary
        return {"title": self.value, "note": self.text, "tags": self.get_tags()}

    def add_note(self, note):
        # Update the note text
        self.text = note
