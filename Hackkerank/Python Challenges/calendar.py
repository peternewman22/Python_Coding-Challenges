import calendar

s = "08 05 2015"
deets = s.split()

print(calendar.weekday(s[2],s[0],s[1]))
