import math

def avg(X):
    return sum(X)/len(X)

def std(X):
    mean_X = avg(X)
    return math.sqrt(sum([(x - mean_X)**2 for x in X])/len(X))

def cov(X, Y):
    mean_X = avg(X)
    mean_Y = avg(Y)
    return sum([(x - mean_X)*(y - mean_Y) for x, y in zip(X, Y)])


n = int(input())

X = list(map(float, input().split()))
Y = list(map(float, input().split()))

p = cov(X, Y)/(n*std(X)*std(Y))
print(round(p, 3))