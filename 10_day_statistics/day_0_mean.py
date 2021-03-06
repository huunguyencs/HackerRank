import numpy as np
from scipy import stats

n = int(input())
arr = np.array(input().split(), int)

print(np.mean(arr))
print(np.median(arr))
print(stats.mode(arr)[0][0])

