# Question : Find Maximum Number of Three using conditional evaluation
# Creating a method to find maximum of three numbers
def findMax(a,b,c):
    if a>=b and a>=c:
        return a
    elif b>=a and b>=c:
        return b
    else:
        return c

# Take inputs from the user
no1=int(input("Enter First Number : "))
no2=int(input("Enter Second Number : "))
no3=int(input("Enter Third Number : "))

# Return the largest or Maximum number 
print("Largest Number is : ",findMax(no1,no2,no3))