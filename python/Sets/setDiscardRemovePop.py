# Link: https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem

numOfEle = int(input())
setInput = set(map(int, input().split()))
numOfTest = int(input())
for _ in range(numOfTest):
    eval('setInput.{0}({1})'.format(*input().split()+['']))

print(sum(setInput))
