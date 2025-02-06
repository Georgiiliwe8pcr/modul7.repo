from datetime import datetime
from field import Field
from constants import DATE_FORMAT

class Birthday(Field):
    def __init__(self, value: str):
        # Перевіряємо, чи відповідає вхідний рядок формату "DD.MM.YYYY"
        try:
            datetime.strptime(value, DATE_FORMAT)
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
        # Якщо рядок валідний, зберігаємо його без перетворення в datetime
        self.value = value

    def __str__(self):
        return self.value
