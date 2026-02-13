def cuml(lst):
    res=[]
    for num in lst:
        if num<0:
            break
        elif not res:
            res.append(num)
        else:
            res.append(num+res[-1])
    return res

n=int(input("Enter the number of elements: "))
lst=[]
for i in range(n):
    num=int(input("Enter a number: "))
    lst.append(num)
print(cuml(lst))