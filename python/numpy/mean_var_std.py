# Link: https://www.hackerrank.com/challenges/np-mean-var-and-std/problem

import numpy as np

n, m = map(int,input().split())

array = np.array([input().strip().split() for _ in range(n)], int)

print(np.mean(array,axis=1))
print(np.var(array,axis=0))
np.set_printoptions(legacy='1.13')
print(round(np.std(array,axis=None),11))