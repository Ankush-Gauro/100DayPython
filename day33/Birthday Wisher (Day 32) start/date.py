import datetime as dt

now = dt.datetime.now()
year = now.year
print(year)

day_of_week = now.weekday()
print(day_of_week)

date_of_birth = dt.datetime(year=2004, month=2, day=1)
print(date_of_birth)