# Link: https://www.hackerrank.com/challenges/incorrect-regex/problem

import re

def checkReg(reg):
    try:
        re.compile(reg)
        return True
    except:
        return False

n = int(input())
for _ in range(n):
    print(checkReg(input()))