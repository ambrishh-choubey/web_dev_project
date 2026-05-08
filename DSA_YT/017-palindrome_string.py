

####### self--with recursion


# def palindrome ( stri,left,right):
#     if left>=right:
#         return True
#     if stri[left]!=stri[right]:
#         # print("its a palindrome")
#         return False
    
    
#         # print("its not a palindrome")    
#     return palindrome(stri,left+1,right-1)
# stri=input("enter the string you wanna check: ")
# result=palindrome("NITIN",0,len(stri)-1)
# print("we are checking  as it is palindrome or not")
# if result:
#     print("It's a palindrome")
# else:
#     print("It's not a palindrome")


###without func

s=input()
n=len(s)
left=0
right=n-1
is_palindrome=True
while left<right:
    if s[left]!=s[right]:
        is_palindrome=False

        break 
    left+=1
    right-=1
if is_palindrome:
    print("its apalindrome")
else:
    print("its not a palindrome")





    



    
    
