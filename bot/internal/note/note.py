from bot.decorators.error_handler import input_error
from bot.internal.field import Field
from bot.internal.note.tag import Tag


class Note(Field):
    MAX_TAGS = 10  # Максимальна кількість тегів

    def __init__(self, title_value, tags=None):
        # Title є обов'язковим
        if not title_value or not isinstance(title_value, str) or not title_value.strip():
            raise ValueError("Title must be a non-empty string.")
        
        # Теги є опціональними. Перевіряємо, чи це список.
        if tags is None:
            self.tags = []
        elif isinstance(tags, list) and all(isinstance(tag, str) and tag.strip() for tag in tags):
            self.tags = [Tag(tag.strip()) for tag in tags]
            if len(self.tags) > self.MAX_TAGS:
                raise ValueError(f"Cannot have more than {self.MAX_TAGS} tags.")
        else:
            raise ValueError("Tags must be a list of non-empty strings.")

        # Ініціалізація базового класу Field
        super().__init__(value=title_value)
        self.text = ""

    def __str__(self):
        # Повертає рядкове представлення Note, включаючи всі теги (якщо є)
        tags_str = ", ".join(tag.value for tag in self.tags) if self.tags else "No tags"
        return f"Title: {self.value}\nText:\n{self.text}\nTags:\n[{tags_str}]"

    def validate(self):
        # Валідація довжини Title (максимум 200 символів)
        if len(self.value) > 200:
            raise ValueError("Title cannot exceed 200 characters.")
        # Валідація кількості тегів
        if len(self.tags) > self.MAX_TAGS:
            raise ValueError(f"Cannot have more than {self.MAX_TAGS} tags.")

    def edit_title(self, new_title):
        # Змінити Title з перевіркою
        if not new_title or not isinstance(new_title, str) or not new_title.strip():
            raise ValueError("New title must be a non-empty string.")
        self.value = new_title  # Оновлення значення Title

    def edit_note(self, new_note):
        # Змінити нотатку
        self.text = new_note

    def add_tag(self, new_tag):
        # Додати новий тег
        if not new_tag or not isinstance(new_tag, str) or not new_tag.strip():
            raise ValueError("Tag must be a non-empty string.")
        if len(self.tags) >= self.MAX_TAGS:
            raise ValueError(f"Cannot add more than {self.MAX_TAGS} tags.")
        if any(tag.value == new_tag.strip() for tag in self.tags):
            raise ValueError("Tag already exists.")
        self.tags.append(Tag(new_tag.strip()))


    def remove_tag(self, tag_to_remove):
        # Видалити тег
        if not tag_to_remove or not isinstance(tag_to_remove, str) or not tag_to_remove.strip():
            raise ValueError("Tag to remove must be a non-empty string.")
        for tag in self.tags:
            if tag.value == tag_to_remove.strip():
                self.tags.remove(tag)
                return
        raise ValueError("Tag not found.")

    def get_tags(self):
        # Повернути список тегів
        return [tag.value for tag in self.tags] if len(self.tags) > 0 else None
    
    def get_title(self):
        # Повертає значення Title
        return self.value

    def get_note(self):
        # Повертає значення Title та нотатку
        return {"title": self.value, "note": self.text, "tags": self.get_tags()}

    def add_note(self, note): 
        # Додати нотатку
        self.text = note