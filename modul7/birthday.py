from datetime import datetime
from constants import DATE_FORMAT

def birthdays(contacts):
    today = datetime.today()
    for contact in contacts:
        # Припускаємо, що contact.birthday.value містить рядок у форматі "DD.MM.YYYY"
        try:
            bday_date = datetime.strptime(contact.birthday.value, DATE_FORMAT)
        except ValueError:
            print(f"Невірний формат дати для контакту {contact.name}. Пропускаємо.")
            continue

        # Замінюємо рік на поточний для визначення наступного дня народження
        next_birthday = bday_date.replace(year=today.year)
        if next_birthday < today:
            next_birthday = next_birthday.replace(year=today.year + 1)

        days_left = (next_birthday - today).days
        print(f"{contact.name}: {days_left} днів до наступного дня народження")
