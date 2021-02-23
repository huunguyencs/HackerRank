# Link: https://www.hackerrank.com/challenges/np-array-mathematics/problem

import numpy as np

N, M = map(int,input().split())

arrayA = np.array([input().strip().split() for _ in range(N)], int)
arrayB = np.array([input().strip().split() for _ in range(N)], int)

print(np.add(arrayA, arrayB))
print(np.subtract(arrayA, arrayB))
print(np.multiply(arrayA, arrayB))
print(np.floor_divide(arrayA, arrayB))
print(np.mod(arrayA, arrayB))
print(np.power(arrayA, arrayB))