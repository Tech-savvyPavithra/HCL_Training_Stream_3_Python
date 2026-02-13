def remdup(lst):
    res=[]
    res=list(set(lst))
    return res

n=int(input("Enter the number of elements: "))
lst=[]
for i in range(n):
    num=int(input("Enter a number: "))
    lst.append(num)
print(remdup(lst))