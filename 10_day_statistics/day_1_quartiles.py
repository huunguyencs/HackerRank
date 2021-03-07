def findMedian(arr):
    if len(arr)%2 == 1:
        return arr[len(arr)//2]
    else:
        return int((arr[len(arr)//2 - 1] + arr[len(arr)//2])/2)

n = int(input())
arr = sorted(list(map(int,input().split())))


q2 = findMedian(arr)
q1 = findMedian(arr[:len(arr)//2])
q3 = findMedian(arr[len(arr)//2:] if len(arr)%2 == 0 else arr[len(arr)//2 + 1:])

print(q1)
print(q2)
print(q3)
