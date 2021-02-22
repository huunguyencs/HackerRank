# Link: https://www.hackerrank.com/challenges/np-eye-and-identity/problem

import numpy as np

N, M = map(int,input().split())

np.set_printoptions(legacy='1.13')

print(np.eye(N,M))