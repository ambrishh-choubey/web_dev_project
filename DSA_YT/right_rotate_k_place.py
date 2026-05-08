 ## brute forcee solnn

def k_rotate(nums,k):
    k=k%len(nums)
    for i in range(0,k):
        e=nums.pop()
        nums.insert(0,e)
    return nums    
print(k_rotate([5,-2,3,9,6,20,7],10))


