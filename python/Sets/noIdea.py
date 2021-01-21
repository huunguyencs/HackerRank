# Link: https://www.hackerrank.com/challenges/no-idea/problem

mn = input()
lst = input().split()
A = set(input().split())
B = set(input().split())

print(sum([int(i in A)-int(i in B) for i in lst]))