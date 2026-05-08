#recursion is when a functionn call itself
# def greet():
#     print("ambrish")
#     greet()
# greet()
# this above code will run in infinite recursion

# count=0
# def func(count):
#     if count==4:
#         return
#     print("ammmii")## head recursion
#     # count+=1
#     func(count+1)
# func(0)    

# ##tail recursion 

# def func(count):
#     if count ==4:
#         return
#     func(count+1)
#     print("ammii")
# func(0)    

#####recursion using parameters

# def func(x,n):
#     if n ==0:
#         return


#     print(x)
#     func(x,n-1)
####
# def func(i,n):
#     if i>n:
#         return 
#     print(i)
#     func(i+1,n)
# func(500,1000)    
# def func(i,n):
#     if i >n:
#         return 
#     func(i+1,n)
#     print(i)
# func(0,666)    
# ####lect =14

# def func(n):
#     sum= n*(n+1)/2
#     print(sum)
# func(10)



# def func(sum=0,i=0,n=0):
#     if i >n:
#         print(sum)
#         return
#     func(sum +i,i+1,n)
# func(0,1,10)


def func(n):
    if n==1:
        return 1
    return n+func(n-1)
print(func(10))