### Task 1
# Take two numbers from the user and print their sum.
A=int(input("Enter fisrt number:"))
B=int(input("Enter Second number:"))
print("Sum",A+B)


### Task 2
# Take two numbers from the user and print their subtraction result.
C=int(input("Enter third number:"))
D=int(input("Enter fourth number:"))
print("Subtraction",C-D)

### Task 3
#Take two numbers from the user and print their multiplication result.
E=int(input("Enter third number:"))
F=int(input("Enter fourth number:"))
print("Multiplication",E*F)

### Task 4
#Take two numbers from the user and print their division result.
G=int(input("Enter fifth number:"))
H=int(input("Enter sixth number:"))
print("Division",G/H)

### Task 5
#Take two numbers from the user and print the remainder.
I=int(input("Enter fifth number:"))
H=int(input("Enter sixth number:"))
print("Remainder",I%H)

### Task 6
#Take two numbers from math import floor
from math import floor

I = int(input("Enter fifth number: "))
H = int(input("Enter sixth number: "))
print("Floor Division", floor(I/H))


### Task 7
# Take a base number and a power number from the user and calculate the result.
base=int(input("Enter base number:"))
power=int(input("Enter power number:"))
print("Result",base**power)

### Task 8
# Take two numbers from the user and check whether they are equal.
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
if num1==num2:
    print("Numbers are equal")
else:   print("Numbers are not equal")

### Task 9
# Take two numbers from the user and check whether they are not equal.
num3=int(input("Enter first number:"))
num4=int(input("Enter second number:"))
if num3!=num4:
    print("Numbers are not equal")
else:   print("Numbers are equal")

### Task 10
# Take two numbers from the user and check whether the first number is greater than the second number.
num5=int(input("Enter first number:"))
num6=int(input("Enter second number:"))
if num5>num6:
    print("First number is greater than second number")
else:   print("First number is not greater than second number") 

### Task 11
# Take two numbers from the user and check whether the first number is less than the second number.
num7=int(input("Enter first number:"))
num8=int(input("Enter second number:"))
if num7<num8:
    print("First number is less than second number")
else:   print("First number is not less than second number")

### Task 12
# Take two numbers from the user and check whether the first number is greater than or equal to the second number.
num9=int(input("Enter first number:"))
num10=int(input("Enter second number:"))
if num9>=num10:
    print("First number is greater than or equal to second number")
else:   print("First number is not greater than or equal to second number")

### Task 13
# Take two numbers from the user and check whether the first number is less than or equal to the second number.
num11=int(input("Enter first number:"))
num12=int(input("Enter second number:")) 
if num11<=num12:
    print("First number is less than or equal to second number")
else:   print("First number is not less than or equal to second number")

###task 14
# Take age and citizenship status from the user and check whether the person is eligible to vote.
age=int(input("Enter your age:"))
citizenship=input("Enter your citizenship status (yes/no):")
if age>=18 and citizenship.lower()=="yes":
    print("You are eligible to vote.")
else:    print("You are not eligible to vote.")

### Task 16
# Take experience and performance rating from the user and check whether the employee is eligible for a bonus.
experience=int(input("Enter years of experience:"))
performance_rating=int(input("Enter performance rating (1-5):"))
if experience>=5 and performance_rating>=4:
    print("Employee is eligible for a bonus.")
else:    print("Employee is not eligible for a bonus.")

### Task 15
# Take student status and premium membership status from the user and check whether the user is eligible for a discount.
student_status=input("Are you a student? (yes/no):")
premium_membership=input("Do you have a premium membership? (yes/no):")
if student_status.lower()=="yes" or premium_membership.lower()=="yes":
    print("You are eligible for a discount.")
else:    print("You are not eligible for a discount.")

### Task 17
# Take marks and sports quota status from the user and check whether the student is eligible for a scholarship.
marks=int(input("Enter your marks:"))
sports_quota=input("Are you in sports quota? (yes/no):")
if marks>=85 or sports_quota.lower()=="yes":
    print("You are eligible for a scholarship.")
else:    print("You are not eligible for a scholarship.")

### Task 18
# Take a number from the user and check whether it lies between 1 and 100.
number=int(input("Enter a number:"))
if 1<=number<=100:
    print("The number lies between 1 and 100.")
else:    print("The number does not lie between 1 and 100.")

### Task 19
# Take a number from the user and check whether it is even or odd.
number=int(input("Enter a number:"))
if number%2==0:
    print("The number is even.")
else:
    print("The number is odd.")


### Task 20
# Take a Boolean value from the user and print its opposite using the not operator.
bool_value=input("Enter a Boolean value (true/false):")
if bool_value.lower()=="true":
    print("The opposite is false.")
elif bool_value.lower()=="false":
    print("The opposite is true.")
else:    print("Invalid input. Please enter 'true' or 'false'.")