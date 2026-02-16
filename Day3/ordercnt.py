def order(lst):
    freq = {}
    
    for i in lst:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    return list(freq.items())

n = int(input("Enter the number of elements: "))
lst = []
for i in range(n):
    lst.append(int(input("Enter element: ")))

print(order(lst))
