def zero_end(nums):
    j=0
    for i in range(len(nums)):

        if nums[i]==0:
            result=nums[i].remove()
            result.insert(len(nums),nums[i])
    return nums
print(zero_end([89,0,67,75,32,0,9,0]))       


#### brute soln

def zero_end(nums):
    result=[]
    for num in nums:
        if num




