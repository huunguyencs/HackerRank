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

X = [ 95, 85, 80, 70, 60]
Y = [ 85, 95, 70, 65, 70]
n = 5

p = cov(X, Y)/(n*std(X)*std(Y))

b = p*std(Y)/std(X)

a = avg(Y) - b * avg(X)

y_80 = a + b*80

print(round(y_80, 3))