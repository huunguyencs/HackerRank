# Link: https://www.hackerrank.com/challenges/floor-ceil-and-rint/problem

import numpy as np

array = np.array(input().split(), float)

np.set_printoptions(legacy='1.13')

print(np.floor(array))
print(np.ceil(array))
print(np.rint(array))