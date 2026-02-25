def rotate(nums, k):
    n = len(nums)
    if n == 0:
        return
    
    k = k % n   # Handle k > n
    
    def reverse(start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
   
    reverse(0, n - 1)
    
    reverse(0, k - 1)
    
    reverse(k, n - 1)
    
nums = list(map(int, input("Enter the array elements: ").split()))
k = int(input("Enter the number of rotations: "))
    
rotate(nums, k)
print("Rotated array:", nums)