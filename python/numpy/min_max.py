# Link: https://www.hackerrank.com/challenges/np-min-and-max/problem

import numpy as np

n, m = map(int,input().split())

array = np.array([input().strip().split() for _ in range(n)], int)

print(np.max(np.min(array,axis=1)))