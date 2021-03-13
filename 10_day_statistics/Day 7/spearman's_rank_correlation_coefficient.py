
def rank(lst):
    rank = dict((x, i + 1) for i, x in enumerate(sorted(lst)))
    return [rank[x] for x in lst]

n = int(input())

X = rank(list(map(float, input().split())))
Y = rank(list(map(float, input().split())))

sum_d = sum([(rx - ry)**2 for rx, ry in zip(X, Y)])

r_xy = 1 - 6*sum_d/(n*(n**2-1))
print(round(r_xy, 3))