# #Print Number from 1 - 100 

# a = 1 
# while a <= 100 :
#     print(a)
#     a += 1 



# #Print Number from 100 - 1 

# b = 100 
# while b >= 1 :
#     print(b)
#     b -= 1 





# # Multiplication table of n number

# num = int(input("Enter a num which multiplication table you want : "))

# print("Multiplication table of" ,num)

# i = 1
# while i <= 10:
#     print(num ,"x" , i ,"=", num*i)
#     i+=1


# Print all items from array 

nums = [1,4,7,2,5,2,76,45,76,34,76,32,75,98,231,233] 

x  = 0

n = int(input("Enter a num you want to search: "))

while x < len(nums) :
    
    print(nums[x]) 
    x+=1

if(nums[x]== n):
    print("Found at ", x , "index")

else: {print("not found")}

