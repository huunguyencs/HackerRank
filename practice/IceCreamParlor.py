# Link: https://www.hackerrank.com/challenges/ctci-ice-cream-parlor/problem

#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the whatFlavors function below.
def whatFlavors(cost, money):
    pass

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        money = int(input())
        n = int(input())
        cost = list(map(int, input().rstrip().split()))
        whatFlavors(cost, money)