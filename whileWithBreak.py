nums = [12,34,65,42,65,12,79,97,75,23,90,99,10,18]

n = int(input("Enter a num you want to find: "))

i = 0 
while i <= len(nums) :
    if(nums[i] == n ):
        print("Found at index" , i)
        break

    else:
        print("Finding........")

    i+=1

print("End of the Program")