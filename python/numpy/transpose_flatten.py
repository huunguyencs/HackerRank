# Link: https://www.hackerrank.com/challenges/np-transpose-and-flatten/problem

import numpy as np

N, M = map(int,input().split())

a = []
for _ in range(N):
    row = list(map(int,input().split()))
    a.append(row)

npArray = np.array(a)
print(np.transpose(npArray))
print(npArray.flatten())