# Link: https://www.hackerrank.com/challenges/piling-up/problem

from collections import deque

def pillingUp():
    n = input()
    inp = map(int,input().split())
    d = deque(inp)
    pre = max(d[0],d[-1])
    curr = pre
    while len(d) > 0:
        first = d[0]
        last = d[-1]
        if first < last:
            curr = last
            d.pop()
        else:
            curr = first
            d.popleft()
        # print(str(curr) +" "+str(pre))
        # print(d)
        if curr > pre:
            print('No')
            return
        pre = curr
        
    print("Yes")


if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        pillingUp()
