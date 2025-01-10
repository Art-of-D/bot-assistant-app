import copy
from collections import UserDict
from bot.internal.note.note import Note
from bot.internal.note.tag import Tag
from bot.decorators.error_handler import input_error

class Notes(UserDict):
  def __getstate__(self):
        return copy.deepcopy(self.__dict__)

  def __setstate__(self, state):
      self.__dict__.update(state)

  @input_error
  def add_note(self, title, note, tag=None):
      if not title or not note:
          raise ValueError("Cannot add empty note or title. Please provide both title and note, first argument is title, second is note.")

      try:
        new_note = Note(title)
        new_note.add_note(note)
        if tag:
            new_tag = Tag(tag)
            new_note.add_tag(new_tag)
        self.data[title.casefold()] = new_note
        return f"{new_note.get_title()}... was added successfully."
      except (KeyError, TypeError, ValueError, AssertionError) as e:
          raise e

  @input_error
  def get_note(self, title):
      if not title:
          raise ValueError("Title cannot be empty.")

      try:
          note_data = self.data[title.casefold()].get_note()
          return f"Title: {note_data['title']}\nNote: {note_data['note']}\nTags: {', '.join(note_data['tags']) if note_data['tags'] else 'No tags'}"
      except KeyError:
          raise KeyError(f"Note with {title} not found!")
      
  
  @input_error
  def delete_note(self, title):
    if not title:
        raise ValueError("Title cannot be empty. Please provide a title.")
    try:
        del self[title.casefold()]
        return f"Note with a {title} deleted successfully."
    except KeyError:
        raise KeyError(f"Note with {title} not found!")
    
  @input_error
  def edit_title(self, old_title, new_title):
      if not old_title or not new_title:
          raise ValueError("Title cannot be empty. Please provide an old and a new title.")

      try:
          note = self.data[old_title.casefold()]
      except KeyError as e:
          raise KeyError(f"Note not found: {str(e)}")

      note.edit_title(new_title)
      self.delete_note(old_title)
      self.data[new_title.casefold()] = note

      return f"Note with {note.get_title()} edited successfully."

  @input_error
  def edit_note(self, title, new_text):
      if not title or not new_text:
          raise ValueError("Title and new text cannot be empty.")

      try:
          note = self.data[title.casefold()]
      except KeyError as e:
          raise KeyError(f"Note not found: {str(e)}")

      note.edit_note(new_text)

      self.data[title.casefold()] = note

      return f"Note with {note.get_title()} edited successfully."
  
  @input_error
  def edit_tag(self, tag, new_tag):
    if not tag:
        raise ValueError("Tag cannot be empty. Please provide a valid tag.")

    try:
        note = self.get_note(tag)
    except KeyError as e:
        raise KeyError(f"Cannot edit tag: {str(e)}")

    if not new_tag:
        raise ValueError("New tag cannot be empty. Please provide a new tag.")

    try:
        new_tag = Tag(new_tag)
    except ValueError as e:
        raise ValueError(str(e))

    self.delete_note(tag)
    self.add_note(new_tag, note)
    return f"Note with tag {tag} edited successfully."
  
  @input_error
  def get_all_notes(self):
    if not self.data:
        return "No notes found."
    notes = []
    index = 0
    print(self.data)
    for title, note in self.data.items():
        index += 1
        note_data = note.get_note()
        notes.append(f"{index}. Title: {note_data['title']}\nNote: {note_data['note']}\nTags: {', '.join(note_data['tags']) if note_data['tags'] else 'No tags'}")
    return "You have the following notes:\n" + "\n".join(notes)
  
  @input_error
  def get_all_tags(self):
    if not self.data:
        return "No tags found."
    tags = []
    for tag, _ in self.data.items():
        if tag:
            tags.append(f"- {tag.get_value()}")
    return "You have the following tags:\n" + "\n".join(tags)
