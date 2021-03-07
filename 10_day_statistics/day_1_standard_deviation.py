import math

n = int(input())
arr = list(map(int,input().split()))

mean = sum(arr)/len(arr)

s_d = math.sqrt(sum([(x - mean)**2 for x in arr])/len(arr))

print("{:.1f}".format(s_d))