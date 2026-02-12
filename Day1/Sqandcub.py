def sqcub(n):
    if n%2==0:
        print(n,"is even number")
        print("Square of",n,"is",n**2)
    else:
        print(n,"is odd number")
        print("Cube of",n,"is",n**3)
print("Enter the number:")
n=int(input())
sqcub(n)