def interleave(list1, list2):
    result = []
    for i in range(min(len(list1), len(list2))):
        result.append(list1[i])
        result.append(list2[i])
    return result

n=int(input("Enter the number of elements in list 1: "))
list1 = []
for i in range(n):
    element = input("Enter element: ")
    list1.append(element)  
    
m=int(input("Enter the number of elements in list 2: "))
list2 = []
for i in range(m):
    element = input("Enter element: ")
    list2.append(element)
    
interleaved = interleave(list1, list2)
print(interleaved)