
n = int(input())
x = list(map(int,input().split()))
w = list(map(int,input().split()))

s = sum([a*b for a, b in zip(x,w)])
print("{:.1f}".format(s/sum(w)))