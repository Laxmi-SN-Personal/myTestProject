import datetime

year = input('YOB: ')
today = datetime.date.today()
age = today.year  - int(year)

print(f"Your age is {age}")
