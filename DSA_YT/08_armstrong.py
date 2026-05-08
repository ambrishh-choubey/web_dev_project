#________________Armstrong______________#

n= int(input())
no_of_digit=len(str(n))
num=n
total=0

while num>0:
    last_digit=num%10#this % sign is useed to give remainder 
    total+=last_digit**no_of_digit
    num = num//10
if n ==total:
    print("armstrong")

else:
    print("not armstrong")        