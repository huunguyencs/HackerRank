#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    change = []
    for i in range(n):
        change.append(0)
    for r in queries:
        change[r[0] - 1] += r[2]
        if r[1] < n:
            change[r[1]] -= r[2]
    maxMan = 0
    curr = 0
    for it in change:
        curr += it
        if curr > maxMan:
            maxMan = curr
    return maxMan

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    # fptr.write(str(result) + '\n')

    # fptr.close()
    print(result)
