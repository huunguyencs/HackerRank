# Task
# A large elevator can transport a maximum of 9800 pounds.
# Suppose a load of cargo containing 49 boxes must be
# transported via the elevator. The box weight of this
# type of cargo follows a distribution with a mean 
# of muy = 205 pounds and a standard deviation of sigma = 15 pounds.
# Based on this information, what is the probability
# that all 49 boxes can be safely loaded into the freight
# elevator and transported?

import math

def cum_prob(X, muy, sigma):
    return 1/2*(1 + math.erf((X - muy)/(sigma*math.sqrt(2))))

n = cum_prob(9800, 205*49, 15*math.sqrt(49))

print(round(n, 4))