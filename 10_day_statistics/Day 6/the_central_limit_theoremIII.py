# Task:
# You have a sample of 100 values from a population with mean
# muy = 500 and with standard deviation sigma = 80. Compute
# the interval that covers the middle 95% of the distribution
# of the sample mean; in other words, compute A and B such that
# P(A < x < B) = 0.95. Use the value of z = 1.96. Note that z is
# the z-score

# Ref: https://en.wikipedia.org/wiki/Standard_score

import math

muy = 500
sigma = 80/math.sqrt(100)
# Because sigma = 80 is population standard deviation
# We have to convert it to sample sd
# [psd] = [ssd]*sqrt(n)

z = 1.96
A = muy - z*sigma
B = muy + z*sigma
print(round(A, 2))
print(round(B, 2))

