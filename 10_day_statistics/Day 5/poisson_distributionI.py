# Task:
# A random variable, X, follows Poisson distribution with mean of 2.5.
# Find the probability with which the random variable X is equal to 5.

e = 2.71828

def fact(n):
    if n == 1 or n == 0: return 1
    return n * fact(n-1)


def poisson(mean, x):
    return (mean**x*e**(-mean))/fact(x)

mean = float(input())
x = float(input())

p = poisson(mean, x)

print(round(p, 3))