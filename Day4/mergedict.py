def merge_inventories(dict1, dict2):
    result = dict1.copy()
    for key, value in dict2.items():
        if key in result:
            result[key] += value
        else:
            result[key] = value
    return result

n=int(input("Enter the number of items in inventory 1: "))
inventory1 = {}
for i in range(n):
    item = input("Enter item name: ")
    quantity = int(input("Enter quantity: "))
    inventory1[item] = quantity
m=int(input("Enter the number of items in inventory 2: "))
inventory2 = {}     
for i in range(m):
    item = input("Enter item name: ")
    quantity = int(input("Enter quantity: "))
    inventory2[item] = quantity

merged = merge_inventories(inventory1, inventory2)
print(merged)
