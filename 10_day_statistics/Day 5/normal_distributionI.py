# Task:
# In a certain plant, the time taken to assemble a car is
# a random variable, X, having a normal distribution with
# a mean of 20 hours and a standard deviation of 2 hours.
# What is the probability that a car can be assembled at
# this plant in:
# 1. Less than 19.5 hours?
# 2. Between 20 and 22 hours?

import math

def cum_prob(X, muy, sigma):
    return 1/2*(1 + math.erf((X - muy)/(sigma*math.sqrt(2))))

n1 = cum_prob(19.5, 20, 2)
print(round(n1, 3))
n2 = cum_prob(22, 20, 2) - cum_prob(20, 20, 2)
print(round(n2, 3))