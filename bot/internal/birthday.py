from datetime import datetime

from bot.internal.field import Field
from bot.decorators.error_handler import input_error

@input_error
class Birthday(Field):
    _dateFormat = "%d.%m.%Y"

    def __init__(self, value):
        try:
            self.value = datetime.strptime(value, self._dateFormat)
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")

    def __str__(self):
        return self.value.strftime(self._dateFormat)

    @staticmethod
    def format():
        return Birthday._dateFormat