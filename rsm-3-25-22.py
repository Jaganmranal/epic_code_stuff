import math

def func(x):
    return x**2 - 2*x + 1

def area(start, end, acc):
    sum = 0
    for i in range(acc * start, acc * end + 1):
        sum += func(i/acc)
    average_height = sum/(acc * (end - start))
    return (end - start) * average_height
        
def f(x):
    return x**2 -5*x + 6

def g(x):
    return 2 - 2*x

def h(x):
    return 400**x - 200**x

def tan(x):
    return math.tan(x)

count = 0
for i in range(-10000, 10000):
    if abs(3*i + 2) - 5 == 5 - abs(3*i + 2):
        count += 1

print(count)