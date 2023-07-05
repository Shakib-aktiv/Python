# Extract the weekday name that falls on December 31 in different years.
# OUTPUT:
# Weekday of December 31, 2022 is Saturday.
# Weekday of December 31, 2023 is Sunday.

from datetime import datetime , date 
year = int(input("Enter a Year : "))
d= date(year,12,31).strftime("%A")
print(d)
