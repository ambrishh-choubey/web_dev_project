# def rever(num,left,right):
#     if left>=right:
#         return
#     num[left],num[right]=num[right],num[left]
#     rever(num,left+1,right-1)
# num=[5,67,78,5,4,5,5,6]
    
# rever(num,0,len(num)-1)
# print(num)




def rever(num,left,right):
    while left>=right:
        return
    num[left],num[right]=num[right],num[left]
    rever(num,left+1,right-1)
num=[5,67,78,5,4,5,5,6]
    
rever(num,2,6)
print(num)


# num =[7,8,9,9,65,4,6,4]
# left,right=0
# while left>=right:
num 
