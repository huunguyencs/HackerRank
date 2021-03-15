# Task:
# Andrea has a simple equation:
# Y = a + b1*f1 + b2*f2 + ... + bm*fm
# for (m+1) real constants (a, f1, f2, ..., fm). We can say that
# the value of Y depends on m features. Andrea studies this
# equation for n different feature sets (f1, f2, f3, ..., fm)
# and records each respective value of Y. If she has q new
# feature sets, can you help Andrea find the value of Y for
# each of the sets?
import numpy as np

n, m = map(int, input().split())

X = []
Y = []

for _ in range(m):
    inp = list(map(float, input().split()))
    X.append(inp[:-1])
    Y.append(inp[-1])

X = np.insert(np.array(X), 0, 1, axis=1)
Y = np.array(Y)


B = np.matmul(np.matmul(np.linalg.inv(np.matmul(np.transpose(X),X)),np.transpose(X)), Y)

t = int(input())
x_cal = np.insert(np.array([input().strip().split() for _ in range(t)], float),0,1, axis=1)


for i in range(t):
    y_cal = np.matmul(x_cal[i], B)
    print(y_cal)