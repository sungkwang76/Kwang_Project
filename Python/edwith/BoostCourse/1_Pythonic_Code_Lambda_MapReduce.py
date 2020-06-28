
def f(x,y):
    return x+y
print(f(1,4))

t = lambda x,y: x+y
print(t(1,4))

ex = [1,2,3,4,5]
f = lambda x: x ** 2
print(list(map(f,ex)))

f = lambda x,y: x+y
print(list(map(f,ex,ex)))

print(list(map(lambda x: x ** 2 if x % 2 == 0 else x, ex )))

print( [value ** 2 for value in ex ] )

from functools import reduce
print(reduce(lambda x,y: x+y, [1,2,3,4,5]))

def factorial(n):
    return reduce(lambda x,y:x*y, range(1,n+1))

print(factorial(5))