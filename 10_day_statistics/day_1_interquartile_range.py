n = int(input())

ele = list(map(int,input().split()))
fre = list(map(int,input().split()))

arr = []

for e, f in zip(ele,fre):
    arr += [e]*f

arr = sorted(arr)

def findMedian(arr):
    if len(arr)%2 == 1:
        return arr[len(arr)//2]
    else:
        return (arr[len(arr)//2 - 1] + arr[len(arr)//2])/2

q1 = findMedian(arr[:len(arr)//2])
q3 = findMedian(arr[len(arr)//2:] if len(arr)%2 == 0 else arr[len(arr)//2 + 1:])

print("{:.1f}".format(q3-q1))