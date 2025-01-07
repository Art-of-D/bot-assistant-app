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
    self[Tag(tag)] = Note(tag, note)
    return f"{note[:10]}... with {tag} added successfully."

  @input_error
  def get_note(self, tag):
    for tag_name, note in self.data.items():
        if tag_name == tag:
            return note
    raise KeyError(f"Note with {tag} not found!")
  
  @input_error
  def delete_note(self, tag):
    try:
      del self[tag]
      return f"Note with a {tag} deleted successfully."
    except KeyError:
      raise KeyError(f"Note with {tag} not found!")

  @input_error
  def edit_note(self, tag, note):
    note = self.get_note(tag)
    # note.edit(note)
    return f"Note with a {tag} edited successfully."
  
  @input_error
  def get_all_notes(self):
    if not self.data:
        return "No notes found."
    return "You have the following notes:\n" + "\n".join(f"- {tag.get_value()}\n {note}" for tag, note in self.data.items()) # check get_value() after tag realization