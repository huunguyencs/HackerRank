# Link: https://www.hackerrank.com/challenges/np-sum-and-prod/problem

import numpy as np

n, m = map(int,input().split())

array = np.array([input().strip().split() for _ in range(n)], int)

print(np.prod(np.sum(array, axis=0)))