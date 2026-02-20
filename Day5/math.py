from math import sqrt as sq, pi as PI

def findsqrt(x):
    print("The square root of", x, "is", sq(x))
    
def pivalue():
    print("The value of pi is", PI)
    
n=int(input("Enter a number to find its square root: "))
findsqrt(n)
pivalue()