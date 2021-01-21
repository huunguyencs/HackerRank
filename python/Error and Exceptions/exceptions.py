# Link: https://www.hackerrank.com/challenges/exceptions/problem

def exception():
    try:
        a, b = map(int,input().split())
        print(int(a)//int(b))
    except ValueError as e:
        print("Error Code: " + str(e))
    except ZeroDivisionError as e:
        print("Error Code: integer division or modulo by zero")

n = int(input())
for _ in range(n):
    exception()
