def div(n,d):
    if d==0:
        return 'NaN'
    return n/d
n=int(input("Enter a numerator: "))
d=int(input("Enter a denominator: "))
print(div(n,d))