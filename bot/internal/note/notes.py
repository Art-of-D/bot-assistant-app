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
            new_note.add_tag(tag)
        self.data[title.casefold()] = new_note
        return f"{new_note.get_title()}... was added successfully."
      except (KeyError, TypeError, ValueError, AssertionError) as e:
          raise e
      
  @input_error
  def add_tag(self, title, tag):
      if not title or not tag:
          raise ValueError("Cannot add empty note or title. Please provide both title and tag, first argument is title, second is tag.")

      try:
          note = self.data[title.casefold()]
          note.add_tag(tag)
          return f"Tag {tag} added to note {title} successfully."
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
  def delete_tag(self, title, tag):
    if not title or not tag:
        raise ValueError("Title and tag cannot be empty. Please provide a title and a tag.")
    try:
        note = self.data[title.casefold()]
        note.remove_tag(tag)
        return f"{tag} deleted successfully from the note with title - {title}."
    except KeyError:
        raise KeyError(f"Note with {title} not found!")
    except ValueError:
        raise ValueError(f"Tag with {tag} not found in note with title {title}.")
    
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
  def get_all_notes(self):
    if len(self.data) == 0:
        return "No notes found."
    notes = []
    index = 0
    for title, note in self.data.items():
        index += 1
        note_data = note.get_note()
        notes.append(f"{index}. Title: {note_data['title']}\nNote: {note_data['note']}\nTags: {', '.join(note_data['tags']) if note_data['tags'] else 'No tags'}")
    return "You have the following notes:\n" + "\n".join(notes)
  
  @input_error
  def get_all_tags(self):
    if len(self.data) == 0:
        return "No tags found."
    
    unique_tags = set()
    for note in self.data.values():
        note_tags = note.get_tags()
        if note_tags:
            unique_tags.update(note_tags)

    tags = sorted(unique_tags)
    return "You have the following tags:\n" + "\n".join(f"- {tag}" for tag in tags)
  
  @input_error
  def display_notes_by_tag(self, tag):
    if len(self.data) == 0:
        return "No notes available."

    tag = tag.casefold()
    matching_notes = []

    for note in self.data.values():
        note_tags = note.get_tags()
        if not note_tags:
            continue
        if any(tag in note_tag.casefold() for note_tag in note_tags):
            note_data = note.get_note()
            matching_notes.append(f"\nTitle: {note_data['title']}\nNote: {note_data['note']}\nTags: {', '.join(note_data['tags'])}\n")

    if len(matching_notes) == 0:
        return f"No notes found with the tag: {tag}"

    return f"Notes with the tag '{tag}':\n" + "\n\n".join(matching_notes)