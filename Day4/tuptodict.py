def group_items_by_category(items):
    result = {}
    for item, category in items:
        if category not in result:
            result[category] = []
        result[category].append(item)
    return result

n=int(input("Enter the number of items: "))
items = []
for i in range(n):
    item = input("Enter item name: ")
    category = input("Enter category: ")
    items.append((item, category))

grouped = group_items_by_category(items)
print(grouped)
