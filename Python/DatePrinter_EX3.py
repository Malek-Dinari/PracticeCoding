import datetime

DATE = datetime.datetime.now()

print("Date and time currently:")

# Get the current date and time by creating a datetime object
print(DATE.strftime("%Y-%m-%d %H:%M:%S"))

# 'strftime' formats the datetime object as a string with the desired format