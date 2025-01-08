import copy
from collections import UserDict
from bot.decorators.error_handler import input_error

class Manager(UserDict):

  def __getstate__(self):
        return copy.deepcopy(self.__dict__)

  def __setstate__(self, state):
      self.__dict__.update(state)

  @input_error # example
  def add_record(self, record):
    self.data[record.name.value] = record

  