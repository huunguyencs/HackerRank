# Link: https://www.hackerrank.com/challenges/python-sort-sort/problem

n, m = map(int,input().split())
lstAth = []
for _ in range(n):
    eles = list(map(int,input().split()))
    lstAth.append(eles)

k = int(input())

lst = list(sorted(lstAth,key=lambda ath: ath[k]))
for e in lst:
    print(*e)