# Link: https://www.hackerrank.com/challenges/collections-counter/problem

from collections import Counter

n = int(input())
strList = input().split(" ")
shoes = []
for item in strList:
    shoes.append(int(item))

shoesCount = dict(Counter(shoes).items())


numCus = int(input())

totalMoney = 0

for _ in range(numCus):
    inp = input().split(" ")
    size = int(inp[0])
    money = int(inp[1])

    try:   
        if shoesCount[size] > 0:
            shoesCount[size] -= 1
            totalMoney += money
        
    except:
        continue

print(totalMoney)
