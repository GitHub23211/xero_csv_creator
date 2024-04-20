from re import fullmatch
from datetime import datetime

class DateValidator:
    def __init__(self):
        self.regex = '[0-9]{1,2}/[0-9]{1,2}/[0-9]{2}'
    
    def validate(self, input):
        match = fullmatch(self.regex, input)
        if match is None:
            return False
        return self.validate_date_range(input)
    
    def validate_date_range(self, date):
        try:
            clean_date = datetime.strptime(date, '%d/%m/%y')
            if self.is_future(clean_date.day, clean_date.month, clean_date.year):
                return False
            return True
        except Exception as e:
            return False

    def is_future(self, day, month, year):
        now = datetime.today()
        day_now = now.day
        month_now = now.month
        year_now = now.year

        if year == year_now:
            if month == month_now:
                return day > day_now
            return month > month_now
        return year > year_now   