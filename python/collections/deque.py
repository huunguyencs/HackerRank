# Link: https://www.hackerrank.com/challenges/py-collections-deque/problem

from collections import deque

n = int(input())

deq = deque()

for _ in range(n):
    i = input().split()
    getattr(deq,i[0])(*[i[1]] if len(i) > 1 else [])

print(*deq)