# Get total working days of the June (Excluding saturday & sunday) using datetime.

from datetime import datetime ,time , timedelta, date
import calendar

enterMonth = int(input("enter a Month :"))
enterYear = int(input("enter a year: "))
last_date = int(input('Enter Last date'))
days = calendar.monthrange(enterYear , enterMonth)
totalDay = days[1]
count = 0
for i in range(1,totalDay+1):
	getWeekDay = date(enterYear, enterMonth, i).strftime("%A")
	day = getWeekDay.lower()
	if day == 'saturday' or day == 'sunday':		
	else:
		count+=1
print(count)




