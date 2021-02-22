# Link: https://www.hackerrank.com/challenges/most-commons/problem


from collections import Counter, OrderedDict

class OrderCounter(Counter,OrderedDict):
    pass

if __name__ == '__main__':
    s = input()
    arr = OrderCounter(sorted(s)).most_common(3)
    [print(*e) for e in arr]
