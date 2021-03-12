# Task:
# The probability that a machine produces a defective product is 1/3.
# What is the probability that the 1st defect is found during the 
# first 5 inspections?

def fact(n):
    if n == 1 or n == 0: return 1
    return n * fact(n-1)

def comb(x, n):
    return fact(n)/(fact(x)*fact(n-x))

def geometric(p, n, N):
    return p**n*(1-p)**(N-n)

p = 1/3

g = sum([comb(n, 5)*geometric(p, n, 5) for n in range(1, 6)])

print(round(g, 3))