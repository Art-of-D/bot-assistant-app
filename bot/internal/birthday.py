from datetime import datetime

from bot.internal.field import Field


class Birthday(Field):
    _dateFormat = "%d.%m.%Y"  # Date format to parse and display birthday

    def __init__(self, date_value):
        # Parse and validate the provided date, then initialize the base Field class
        validated_date = self._parse_and_validate_date(date_value)
        super().__init__(validated_date)

    def __str__(self):
        # Provide a string representation of the birthday in the specified date format
        return self.value.strftime(self._dateFormat)

    @staticmethod
    def format():
        # Return the date format used for parsing and displaying birthdays
        return Birthday._dateFormat

    def get_birthday(self):
        # Return the stored birthday value as a datetime object
        return self.value

    def _parse_and_validate_date(self, date_value):
        # Parse the provided date string and validate its age constraints
        try:
            parsed_date = datetime.strptime(date_value, self._dateFormat)
            self._validate_age(parsed_date)  # Ensure the date falls within acceptable age range
            return parsed_date
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
        except Exception as e:
            raise ValueError(f"Error parsing date: {e}")

    @staticmethod
    def _validate_age(birth_date):
        """Validate that the age is between 0 and 125 years."""
        today = datetime.today()
        age = (today - birth_date).days // 365  # Calculate the age in years

        # Check if the age is within a reasonable range
        if age < 0:
            raise AssertionError("The date of birth cannot be in the future.")
        if age > 125:
            raise AssertionError("The age cannot exceed 125 years.")
