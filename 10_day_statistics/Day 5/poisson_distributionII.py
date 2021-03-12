# Task:
# The manager of a industrial plant is planning to buy
# a machine of either type A or type B. For each day’s
# operation:

# + The number of repairs, X, that machine A needs is a
# Poisson random variable with mean 0.88.The daily cost
# of operating A is C(A) = 160 + 40X^2.

# + The number of repairs, Y, that machine B needs is a
# Poisson random variable with mean 1.55.The daily cost
# of operating B is C(B) = 128 + 40Y^2.

# Assume that the repairs take a negligible amount of time
# and the machines are maintained nightly to ensure that
# they operate like new at the start of each day. Find and
# print the expected daily cost for each machine.

a, b = map(float, input().split())

a_2 = a + a**2
b_2 = b + b**2

c_a = 160 + 40*a_2
c_b = 128 + 40*b_2

print(round(c_a, 3))
print(round(c_b, 3))
