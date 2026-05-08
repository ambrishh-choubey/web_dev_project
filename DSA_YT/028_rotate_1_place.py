## right rotating an array by one places


# def right_rotate(nums):
#     nums[:]=[nums[-1]] + nums[0:len(nums)-1]

#     return nums

# print(right_rotate([5,-2,3,9,6,20,7]))


def right_rotate(nums):
    temp=nums[len(nums)-1]
    for i in range(len(nums)-2,-1,-1):
        nums[i+1]=nums[i]
    nums[0]=temp    
    return nums
print(right_rotate([5,-2,3,9,6,20,7]))
