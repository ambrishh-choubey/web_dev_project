def insertion_sort(nums):
    n=len(nums)
    for i in range(1,n-1):
        key=nums[i]
        j=i-1
        while j>=0 and nums[j]>key:
            nums[j+1]=nums[j]
            j-=1
        nums[j+1]=key
    return nums
result=insertion_sort([7,5,6,8,9])
print(result)    


