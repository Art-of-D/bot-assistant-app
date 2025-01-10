from datetime import datetime

from bot.internal.field import Field


class Birthday(Field):
    _dateFormat = "%d.%m.%Y"

    def __init__(self, date_value):
        validated_date = self._parse_and_validate_date(date_value)   
        super().__init__(validated_date)

    def __str__(self):
        return self.value.strftime(self._dateFormat)

    @staticmethod
    def format():
        return Birthday._dateFormat

    def get_birthday(self):
        return self.value
    
    def _parse_and_validate_date(self, date_value):
        try:
            parsed_date = datetime.strptime(date_value, self._dateFormat)
            self._validate_age(parsed_date)
            return parsed_date
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
        except Exception as e:
            raise ValueError(f"Error parsing date: {e}")

    @staticmethod
    def _validate_age(birth_date):
        """Перевіряє, чи вік у межах від 0 до 125 років."""
        today = datetime.today()
        age = (today - birth_date).days // 365

        # Перевіряємо, чи вік у розумних межах
        if age < 0:
            raise AssertionError("The date of birth cannot be in the future.")
        if age > 125:
            raise AssertionError("The age cannot exceed 125 years.")
