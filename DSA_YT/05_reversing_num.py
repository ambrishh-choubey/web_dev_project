# n=int(input("Enter the number: "))
# num =n
# while num>0:
#     last_digit=num%10
#     print(last_digit)
#     num = num //10


n=int(input("Enter the number: "))
num =n
rev=0

while num>0:
    last_digit=num%10
    rev=rev*10+last_digit
    # print(last_digit)
    num = num //10
print(rev)    