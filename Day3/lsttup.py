def pair_tuple(lst):
    return [(lst[i], lst[i+1]) for i in range(0, len(lst)-1, 2)]

lst = input("Enter elements separated by space: ").split()
print(pair_tuple(lst))
