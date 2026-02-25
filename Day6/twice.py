def apply_twice(func, x):
    return func(func(x))

def square(n):
    return n * n

n=int(input("Enter a number: "))

print(apply_twice(square, n))