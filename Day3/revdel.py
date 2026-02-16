def rel(lst):
    seen = set()
    out=[]
    for i in reversed(lst):
        if i not in seen:
            seen.add(i)
            out.append(i)
    return out[::-1]
n=int(input("Enter the number of elements in the list: "))
list=[]
for i in range(n):
    list.append(int(input("Enter element: ")))
    
print(rel(list))