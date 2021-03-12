# Task:
# The final grades for a Physics exam taken by a large group
# of students have a mean of muy = 70 and a standard deviation
# of sigma = 10.If we can approximate the distribution of
# these grades by a normal distribution, what percentage of
# the students:

# 1. Scored higher than 80
# 2. Passed the test (grade >= 60)
# 3. Failed the test (grade < 60)

import math

def cum_prob(X, muy, sigma):
    return 1/2*(1 + math.erf((X - muy)/(sigma*math.sqrt(2))))

n1 = 1 - cum_prob(80, 70, 10)
n3 = cum_prob(60, 70, 10)
n2 = 1 - n3

print(round(100*n1, 2))
print(round(100*n2, 2))
print(round(100*n3, 2))