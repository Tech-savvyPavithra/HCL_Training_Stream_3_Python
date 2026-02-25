def run_reset(nums):
    result = []
    current_sum = 0
    
    for num in nums:
        current_sum += num
        
        if current_sum <= 0:
            current_sum = 0
        
        result.append(current_sum)
    
    return result

nums = list(map(int, input("Enter the array elements: ").split()))
result = run_reset(nums)
print("Running sum:", result)