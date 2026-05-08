def sorted_checking(nums):
    for i in range(1,len(nums)):
        if nums[i]<nums[i-1]:
            return False
        
    return True 
print(sorted_checking([1,2, 4]))
