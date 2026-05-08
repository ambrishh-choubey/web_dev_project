
##brute force soln
# ##we have to keep all uniquw elemente in the start of array
# def remove_duplicate(nums):
#     n=len(nums)
#     freq_map=dict()
#     for i in range(0,len(nums)):
#         # for j in range(len(nums),-1,-1):
#         freq_map[nums[i]]=0
#     j=0    
#     for k in freq_map:
#         nums[j]=k
#         j+=1
#     return j    
# print(remove_duplicate([1,47,45,6,5,4,3,4,3,5,3,53,53,556,3,53,53,35,3]))
        

## optimal solution  
# def duplicate_remove(nums):
#     if len(nums) ==1:
#         return 1
#     i=0
#     # j=i+1
    
#     for j in range(len(nums)):
#         if nums[i]!=nums[j]:
#             i+=1
#             nums[i]=nums[j]

#     return i+1,nums
# print(duplicate_remove([1,1,2,2,3,4,4,5]))        




##using while loop
def duplicate_remove(nums):
    if len(nums) ==1:
        return 1
    i=0
    j=i+1
    while j>len(nums):
        if nums[j]!=nums[i]:
            i+=1
            nums[i]=nums[j]
    return i+1        

print(duplicate_remove([1,1,2,2,3,4,4,5]))