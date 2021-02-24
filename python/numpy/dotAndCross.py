# Link: https://www.hackerrank.com/challenges/np-dot-and-cross/problem

import numpy as np

n = int(input())

arrayA = np.array([input().strip().split() for _ in range(n)], int)
arrayB = np.array([input().strip().split() for _ in range(n)], int)

print(np.dot(arrayA,arrayB))