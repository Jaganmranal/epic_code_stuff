#this is an epic integral calculator i guess
def func(x):
#you can change this function to as you see fit
    return x**2 + 2*x + 1

def area(start, end, acc):
    sum = 0
    for i in range(acc * start, acc * end + 1):
        sum += func(i/acc)
    average_height = sum/(acc * (end - start))
    return (end - start) * average_height