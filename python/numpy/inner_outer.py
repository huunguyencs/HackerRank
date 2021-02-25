# Link: https://www.hackerrank.com/challenges/np-inner-and-outer/problem

import numpy as np

arrayA = np.array(input().split(), int)
arrayB = np.array(input().split(), int)

print(np.inner(arrayA, arrayB))
print(np.outer(arrayA, arrayB))