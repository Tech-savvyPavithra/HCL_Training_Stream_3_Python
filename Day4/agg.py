def aggregate(*nums, op="sum"):
    if not nums:
        return None
    if op == "sum":
        return sum(nums)
    elif op == "avg":
        return sum(nums) / len(nums)
    elif op == "max":
        return max(nums)
    
print(aggregate(1, 2, 3, op="sum"))  