# Task:
# A manufacturer of metal pistons finds that, on average,
# 12% of the pistons they manufacture are rejected because
# they are incorrectly sized. What is the probability that
# a batch of 10 pistons will contain:
# 1. No more than 2 rejects?
# 2. At least 2 rejects?

N = 10
p = 0.12
q = 1 - p

def fact(n):
    if n == 1 or n == 0: return 1
    return n * fact(n-1)

def comb(x, n):
    return fact(n)/(fact(x)*fact(n-x))

def b(x, n, p):
    return comb(x, n)*(p**x)*((1-p)**(n-x))


b1 = sum([b(x,N,p) for x in range(3)])
b2 = 1 - sum([b(x,N,p) for x in range(2)])

print(round(b1,3))
print(round(b2,3))
