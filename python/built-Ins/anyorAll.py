# Link: https://www.hackerrank.com/challenges/any-or-all/problem

n = int(input())
lst = list(map(int,input().split()))
print(all([e>0 for e in lst]) and any([str(e) == str(e)[::-1] for e in lst]))