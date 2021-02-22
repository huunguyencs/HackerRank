# Link: https://www.hackerrank.com/challenges/py-collections-ordereddict/problem

from collections import OrderedDict

n = int(input())

orderedDict = OrderedDict()

for _ in range(n):
    inp = input().split()
    key = " ".join(inp[:-1])
    try:
        orderedDict[key] += int(inp[-1])
    except:
        orderedDict[key] = int(inp[-1])


for key, value in orderedDict.items():
    print(key + " " + str(value))