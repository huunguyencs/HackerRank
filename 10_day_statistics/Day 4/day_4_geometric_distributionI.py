# Task:
# The probability that a machine produces a defective product is 1/3.
# What is the probability that the 1st defect occurs the 5th item produced?

def geometric(p, n, N):
    return p**n*(1-p)**(N-n)

p = 1/3

P = geometric(p, 1, 5)

print(round(P, 3))
