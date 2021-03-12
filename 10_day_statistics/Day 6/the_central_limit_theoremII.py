# Task:
# The number of tickets purchased by each student for
# the University X vs. University Y football game follows
# a distribution that has a mean of muy = 2.4 and a standard
# deviation of sigma = 2.0.

# A few hours before the game starts, 100 eager students
# line up to purchase last-minute tickets. If there are only 250
# tickets left, what is the probability that all 100 students
# will be able to purchase tickets?

import math

def cum_prob(X, muy, sigma):
    return 1/2*(1 + math.erf((X - muy)/(sigma*math.sqrt(2))))

n = cum_prob(250, 2.4*100, 2*math.sqrt(100))

print(round(n, 4))