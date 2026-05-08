'''constrains
1) 1<=n[i]=<10
2 . n can have 10^8 elements 
2 . m can have 10^8 elements 

'''
##method 1
# n =[5,6,7,4,3,2,4,6,7,8,9,10,1,2,3,4,5]
# m=[10,111,1,4,3,5,3,3,4,3,4,4]
# for num in m:
#     count=0
#     for x in n:
#         if x ==num:
#             count +=1

#     print(count)
    
    #   method 2 
# n =[5,6,7,4,3,2,4,6,7,8,9,10,1,2,3,4,5]
# m=[10,111,1,4,3,5,3,3,4,3,4,4]
# hash_list=[0]*11
# for num in n:
#     hash_list[num]+=1
# for num in m :
#     # if num in m:
#     if num <1 or num >10:
#         print(0)    
#     else:
#         print(hash_list[num])
            

# method 3
# n =[5,6,7,4,3,2,4,6,7,8,9,10,1,2,3,4,5]
# m=[10,111,1,4,3,5,3,3,4,3,4,4]
# freq=dict()
# for num in n:
#     freq[num]= freq.get(num,0)+1
# for num in m:
#     print(freq.get(num,0))        
        


### charcterrr hashingg ####
#method 1
# s ="addfdasfdsaassdfas"
# q =["d","a","c","b"]
# hash_list=[0]*26
# for ch in s:
#     ascii_val=ord(ch)
#     index=ascii_val-97
#     hash_list[index]+=1

# for ch in q:
#     ascii_val=ord(ch)
#     index =ascii_val-97
#     print(hash_list[index])
##method 2
s ="addfdasfdsaassdfas"
q =["d","a","c","b"]
freq={}
for ch in s:
    index=ord(ch)-97
    freq[index]=freq.get(index,0)+1
for ch in q:
    index=ord(ch)-97
    print(freq.get(index,0))


#### chrater and symbols hashing    
# s ="!#@#$asddadffs9768"
# q=["!","@","a"]
# hash_list=[0]*256
# for ch in s:
#     index = ord(ch)
#     (hash_list[index])+=1
# for ch in q:
#     index=ord(ch)
#     print(hash_list[index])







