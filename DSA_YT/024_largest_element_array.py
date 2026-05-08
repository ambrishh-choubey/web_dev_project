def largest_element(nums):
    # n=len(nums)
    max_val=nums[0]
    for i in range(1,len(nums)):
        # for j in range(n-1,-1,-1):
        if nums[i]>max_val:
            max_val=nums[i]
            # return nums[i]
        
    return max_val
print(largest_element([1,3,5,9,6,7]))

def largest_element(num):
    max_value=num[0]
    for i in range(0,len(num)):
        max_value =max(max_value,num[i])
    return max_value    



