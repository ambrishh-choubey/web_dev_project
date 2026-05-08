
#palindrome check 
n = int(input())
num =n
rev=0 
while num >0:
    last_digit=num%10
    rev =rev*10+last_digit
    num=num//10
print(rev)
if rev ==n:
    print("its a palindrome.")    
else:
    print("its not a palindrome.")    