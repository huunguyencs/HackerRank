# Link: https://www.hackerrank.com/challenges/ginorts/problem

import string

lst = input()
sortKey = (string.ascii_letters + '1357902468').index
a = sorted(lst,key=sortKey)
print(*a,sep='')