# bubble sort mean adjacent sorttt

def bubble_sort(nums):
    n=len(nums)
    for i in range(n-2,-1,-1):
        for j in range(0,i+1):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
        return nums
nums=[7,5,6,8,9]
print(bubble_sort(nums))


    

