#exercise6
'''def factorial(n:int):
    total = 1
    while n >= 1:
        total *= n
        n -= 1
    return total

print(factorial(5))'''

def square(n):
    return n*n

L = [1,2,3,4,5]
result = map(square, L)
print(result)
print(set(result))
print(list(result))

#-------------------------------

def half(n):
    return n/2

T = (2, 4, 6, 8, 10)
result = map(half, T)
print(result)
print(set(result))
print(list(result))

#--------------------------------

lambda n:n*n

result = (lambda n : n*n)(10)
print(result)

#--------------------------------

def func(n):
    print(n)
    if n==1:
        return None
    else:    
        func(n-1) 

result = func(3)

#---------------------------------

def factorial(n):
    if n == 1:
        return None
    else:
        return factorial(n-1)

result = factorial(5)
print(result)
