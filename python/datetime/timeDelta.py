# Link: https://www.hackerrank.com/challenges/python-time-delta/problem?h_r=next-challenge&h_v=zen
# Reference: https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior

from datetime import datetime as dt

formatDate = "%a %d %b %Y %H:%M:%S %z"
n = int(input())
for _ in range(n):
    time1 = dt.strptime(input(),formatDate)
    time2 = dt.strptime(input(),formatDate)
    print(int(abs(time1-time2).total_seconds()))
