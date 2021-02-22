# Link: https://www.hackerrank.com/challenges/py-collections-namedtuple/problem

from collections import namedtuple

n = int(input())
title = input()
Student = namedtuple('Student',title)
sum = 0
for _ in range(n):
    val = input().split()
    tmp = Student(val[0],val[1],val[2],val[3])
    sum += int(tmp.MARKS)

print('{:.2f}'.format(sum/n))