# Link: https://www.hackerrank.com/challenges/py-set-union/problem

n = input()
s1 = set(map(int,input().split()))
n = input()
s2 = set(map(int,input().split()))

print(len(s1 | s2))