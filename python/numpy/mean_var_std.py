# Link: https://www.hackerrank.com/challenges/np-mean-var-and-std/problem

import numpy as np

n, m = map(int,input().split())

array = np.array([input().strip().split() for _ in range(n)], int)
np.set_printoptions(legacy='1.13')

print(np.mean(array,axis=1))
print(np.var(array,axis=0))
print(np.std(array))