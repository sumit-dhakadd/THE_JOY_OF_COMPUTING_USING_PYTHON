import random
import datetime

birthday = []

i = 0
while i < 50:
    year = random.randint(1895, 2017)
    # The oldest person ever lived was 122 years old
    
    # Check for leap year
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        leap = 1
    else:
        leap = 0

    # Random month
    month = random.randint(1, 12)

    # Random day depending on month and leap year
    if month == 2 and leap == 1:
        day = random.randint(1, 29)
    elif month == 2 and leap == 0:
        day = random.randint(1, 28)
    elif month in [1, 3, 5, 7, 8, 10, 12]:
        day = random.randint(1, 31)
    else:
        day = random.randint(1, 30)

    # Convert date to day of the year
    dd = datetime.date(year, month, day)
    day_of_year = dd.timetuple().tm_yday

    birthday.append(day_of_year)
    i += 1

birthday.sort()
print("Birthdays (as day of year):")
print(birthday)

# Check for matching birthdays
same = 0
for j in range(49):
    if birthday[j] == birthday[j + 1]:
        same += 1

if same != 0:
    print("\nThere are", same, "people with the same birthday!")
else:
    print("\nNo two people share the same birthday.")
