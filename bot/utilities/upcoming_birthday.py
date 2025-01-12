from datetime import datetime, timedelta

def get_upcoming_birthdays(contacts, days_before_birthday) -> list:
    """
    Function returns a list of contacts whose birthdays fall within
    the specified number of days from today.
    """
    birthdays = []

    today = datetime.today().date()  # Get the current date

    for key, record in contacts:
        # Check if the contact has a birthday
        if not record.get_birthday():
            continue

        # Retrieve the birthday
        birthday = record.get_birthday()

        # Calculate the birthday date for the current year
        specific_date = datetime(year=today.year, month=birthday.month, day=birthday.day).date()

        # If the birthday has already passed this year, move it to the next year
        if specific_date < today:
            specific_date = datetime(year=today.year + 1, month=birthday.month, day=birthday.day).date()

        # Calculate the number of days until the birthday
        days_difference = (specific_date - today).days

        # Check if the birthday falls within the specified range
        if 0 <= int(days_difference) <= int(days_before_birthday):
            birthdays.append(
                {
                    'name': record.name.value,  # Contact's name
                    'birthday_date': specific_date.strftime("%d.%m.%Y")  # Birthday date
                }
            )

    return birthdays

