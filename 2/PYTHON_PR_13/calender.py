# Program that will display calander of given month using calender module

import calendar
yy= int(input("Enter year:"))
mm= int(input("Enter month:"))
print(calendar.month(yy,mm))