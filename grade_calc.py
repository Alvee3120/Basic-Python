num = int(input("Enter your number: "))

if num < 0 or num > 100 :
    print("Invalid Input")

elif num <= 59 and num >= 0:
    print("Grade: F") 

elif num <= 69 and num >= 60:
    print("Grade: D") 

elif num <= 79 and num >= 70:
    print("Grade: C")

elif num <= 89 and num >= 80:
    print("Grade: B") 

elif num <= 100 and num >= 90:
    print("Grade: A") 
