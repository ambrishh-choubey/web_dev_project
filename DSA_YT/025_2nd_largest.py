### second largest###
# #brute force soln 

# def second_largest(nums):
#     result=nums[0]
#     for i in range(0,len(nums)):
#         if 
    



##better 
# def second_largest(nums):
#     largest= float("-inf")
#     sec_largest=float("-inf")
#     for i in range(len(nums)):
#         largest=max(largest,nums[i])

#     for i in range(0,len(nums)):
#         if nums[i]>sec_largest and nums[i]!=largest:
#             sec_largest=nums[i]
#     return sec_largest        
# print(second_largest([55,87,-97,45]))




#####optimal soln


def second_largest(nums):
    largest =float("-inf")
    s_largest =float("-inf")
    for i in range(len(nums)):
        if nums[i]>largest:
            s_largest=largest
            largest =nums[i]
        elif nums[i]>s_largest and s_largest!=largest:
            s_largest=nums[i]
        if s_largest==float("-inf"):
            s_largest=  None


    return s_largest,largest
print(second_largest([1]))
        