# Link: https://www.hackerrank.com/challenges/word-order/problem

from collections import OrderedDict

n = int(input())

orderDict = OrderedDict()

for _ in range(n):
    key = input()
    try:
        orderDict[key] += 1
    except:
        orderDict[key] = 1

print(len(orderDict))
print(" ".join(map(str,orderDict.values())))