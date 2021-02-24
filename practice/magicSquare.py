# Link: https://www.hackerrank.com/challenges/magic-square-forming/problem


array = [list(map(int, input().strip().split())) for _ in range(3)]
magicSquare = [
    [[8,1,6], [3,5,7], [4,9,2]],
    [[6,1,8], [7,5,3], [2,9,4]],
    [[4,9,2], [3,5,7], [8,1,6]],
    [[2,9,4], [7,5,3], [6,1,8]],
    [[8,3,4], [1,5,9], [6,7,2]],
    [[4,3,8], [9,5,1], [2,7,6]],
    [[6,7,2], [1,5,9], [8,3,4]],
    [[2,7,6], [9,5,1], [4,3,8]]
]

minSum = 100000
for i in range(8):
    sumTmp = 0
    for j in range(3):
        for k in range(3):
            sumTmp += abs(array[j][k] - magicSquare[i][j][k])
    
    minSum = min(minSum,sumTmp)

print(minSum)