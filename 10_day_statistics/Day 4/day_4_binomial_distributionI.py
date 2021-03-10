# Task:
# The ratio of boys to girls for babies born in Russia is 1.09:1.
# If there is 1 child born per birth, what proportion of Russian
# families with exactly 6 children will have at least 3 boys?

# Write a program to compute the answer using the above parameters.
# Then print your result, rounded to a scale of 3 decimal places
# (i.e., 1.234 format).

def fact(n):
    if n == 1 or n == 0: return 1
    return n * fact(n-1)

def comb(x, n):
    return fact(n)/(fact(x)*fact(n-x))

def b(x, n, p):
    return comb(x, n)*(p**x)*((1-p)**(n-x))

i1, i2 = map(float, input().split())
p = i1/(i1+i2)

# b = comb(0, 6)*(p**0)*((1-p)**6) + comb(1,6)*(p**1)*((1-p)**5) + comb(2,6)*(p**2)*((1-p)**4) 

r = sum([b(x, 6, p) for x in range(3)])
print(round(1 - r, 3))
