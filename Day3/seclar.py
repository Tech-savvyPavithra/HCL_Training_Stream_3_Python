def found(lst):
    first = second = float('-inf')
    for i in lst:
       if i>first:
           second=first
           first=i
       elif i>second and i<first:
           second=i
    if second==float('-inf'):
        return -1
    else:
        return lst.index(second)

n= int(input("Enter no of elements: "))
lst=[]
for i in range(n):
    lst.append(int(input("Enter a value: ")))
print("Index of second max  element is: ", found(lst))