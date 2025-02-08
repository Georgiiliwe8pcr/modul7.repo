from datetime import datetime, timedelta
from collections import UserDict
from constants import DATE_FORMAT

def is_weekend_day(day: int) -> bool:
    return day > 4

class AddressBook(UserDict):

    def __str__(self):
        lines = [str(record) for record in self.data.values()]
        return "\n".join(lines)
    def add_record(self, record):
        if record.name.value in self.data:
            raise KeyError(f"Record with name '{record.name.value}' already exists.")
        self.data[record.name.value] = record
    def find(self, name: str):
        return self.data.get(name)
    def delete(self, name):
        del self.data[name]
    def get_upcoming_birthdays(self):
        today = datetime.today()           # Получаем текущий datetime
        today_date = today.date()          # Преобразуем его в объект date
        upcoming_birthdays = []
        for name, record in self.data.items():
            if record.birthday:
               birthday_date = datetime.strptime(
                   record.birthday.value, DATE_FORMAT
               ).replace(year=today.year).date()
               timedelta_days = (birthday_date - today_date).days
               if 0 <= timedelta_days <= 7:
                   if is_weekend_day(birthday_date.weekday()):
                      days_delta = 2 if birthday_date.weekday() == 5 else 1
                      congratulation_date = birthday_date + timedelta(days=days_delta)
                   else:
                       congratulation_date = birthday_date
                   upcoming_birthdays.append(
                       {
                           "name": name,
                           "congratulation_date": congratulation_date.strftime(DATE_FORMAT),
                       }
                   )
       return upcoming_birthdays
