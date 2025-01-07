import copy
from collections import UserDict
from bot.internal.note.note import Note
from bot.internal.note.tag import Tag
from bot.decorators.errorhandler import input_error

#It will use tag as a key to access notes and manage them
class Notes(UserDict):
  def __getstate__(self):
        return copy.deepcopy(self.__dict__)

  def __setstate__(self, state):
      self.__dict__.update(state)

  @input_error
  def add_note(self, tag, note):
      if not tag or not note:
          raise ValueError("Cannot add empty note or tag. Please provide both tag and note, first argument is tag, second is note.")

      try:
          tag = Tag(tag)
          note = Note(note)
      except ValueError as e:
          raise ValueError(str(e))
      
      self.data[tag] = note
      return f"{note.value[:10]}... with {tag.value} added successfully."

  @input_error
  def get_note(self, tag):
    if not tag:
        raise ValueError("Tag cannot be empty. Please provide a tag.")
    try:
        return self.data[tag]
    except KeyError:
        raise KeyError(f"Note with {tag} not found!")
  
  @input_error
  def delete_note(self, tag):
    if not tag:
        raise ValueError("Tag cannot be empty. Please provide a tag.")
    try:
        del self[tag]
        return f"Note with a {tag} deleted successfully."
    except KeyError:
        raise KeyError(f"Note with {tag} not found!")

  @input_error
  def edit_note(self, tag, new_note):
      if not tag or not new_note:
          raise ValueError("Tag and new note cannot be empty.")

      try:
          note = self.get_note(tag)
      except KeyError as e:
          raise KeyError(f"Cannot edit note: {str(e)}")

      if not isinstance(new_note, Note):
          new_note = Note(new_note)

      self.data[tag] = new_note
      return f"Note with {tag.value} edited successfully."
  
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
    for tag, note in self.data.items():
        if tag and note:
            notes.append(f"- {tag.get_value()}\n {note}")
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
