from datetime import datetime

from bot.internal.field import Field
from bot.decorators.error_handler import input_error


class Birthday(Field):
    _dateFormat = "%d.%m.%Y"

    def __init__(self, value):
        try:
            # Парсимо дату
            parsed_date = datetime.strptime(value, self._dateFormat)
            
            # Валідуємо вік
            self._validate_age(parsed_date)
            
            # Якщо все добре, зберігаємо дату
            self.value = parsed_date
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
        except AssertionError as e:
            raise ValueError(str(e))

    def __str__(self):
        return self.value.strftime(self._dateFormat)

    @staticmethod
    def format():
        return Birthday._dateFormat

    def get_birthday(self):
        return self.value

    @staticmethod
    def _validate_age(birth_date):
        """Перевіряє, чи вік у межах від 0 до 150 років."""
        today = datetime.today()
        age = (today - birth_date).days // 365

        # Перевіряємо, чи вік у розумних межах
        if age < 0:
            raise AssertionError("The date of birth cannot be in the future.")
        if age > 125:
            raise AssertionError("The age cannot exceed 125 years.")
