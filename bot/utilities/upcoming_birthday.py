from datetime import datetime, timedelta

def get_upcoming_birthdays(contacts, days_before_birthday) -> list:
    """
    Функція повертає список контактів, у яких дні народження припадають на 
    вказаний період у майбутньому (від сьогодні на задану кількість днів).
    """
    birthdays = []

    today = datetime.today().date()  # Отримуємо поточну дату

    for key, record in contacts:
        # Перевіряємо, чи є дата народження у контакта
        if not record.get_birthday():
            continue

        # Отримуємо дату народження
        birthday = record.get_birthday()

        # Формуємо дату дня народження в поточному році
        specific_date = datetime(year=today.year, month=birthday.month, day=birthday.day).date()

        # Якщо день народження вже пройшов цього року, переносимо на наступний рік
        if specific_date < today:
            specific_date = datetime(year=today.year + 1, month=birthday.month, day=birthday.day).date()

        # Розраховуємо кількість днів до дня народження
        days_difference = (specific_date - today).days

        # Перевіряємо, чи день народження у межах зазначеного періоду
        if 0 <= int(days_difference) <= int(days_before_birthday):
            birthdays.append(
                {
                    'name': record.name.value,  # Ім'я контакта
                    'birthday_date': specific_date.strftime("%d.%m.%Y")  # Дата дня народження
                }
            )

    return birthdays



