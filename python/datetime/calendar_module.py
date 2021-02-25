# Link: https://www.hackerrank.com/challenges/calendar-module/problem

import calendar
DAYOFWEEKS = ['MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY']
date = list(map(int,input().split()))
print(DAYOFWEEKS[calendar.weekday(date[2],date[0],date[1])])
