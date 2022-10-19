from datetime import datetime

today = datetime.today()
def user_birthday():
    year = int(input("Enter your birth year:"))
    month = int(input("Enter your birth month:"))
    day = int(input("Enter your birth day:"))

    birthday = datetime(year,month,day)
    return birthday


def calculate_dates(birthyday):
    now = datetime.now()
    birthday = datetime(now.year, birthyday.month, birthyday.day)
    if birthday < today:
        birthday = birthday.replace(year=today.year + 1)
        return (birthday - now.today()).days
    else:
        return (birthday - now.today()).days + 1


bd = user_birthday()
c = calculate_dates(bd)
print(c)

hours = c*24
print(hours)

minutes = hours*60
print(minutes)


