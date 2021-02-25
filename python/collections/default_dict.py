# Link: https://www.hackerrank.com/challenges/defaultdict-tutorial/problem

from collections import defaultdict

inp = input().split()
n = int(inp[0])
m = int(inp[1])

d = defaultdict(list)

for i in range(n):
    d[input()].append(i+1)

for _ in range(m):
    lst = d[input()]
    if lst != []:
        print(*lst)
    else: print(-1)