# Question 1: Personal Introduction Enter Name: Prakash
# Enter Age: 80
# Enter City: Bhubaneswar

# ----- User Information -----
# Name: Prakash
# Age: 80
# City: Bhubaneswar


Name=input("Enter Name:")
Age=int(input("Enter Age:"))
City=input("Enter City:")
print("\n----- User Information -----")
print("Name:", Name)
print("Age:", Age)
print("City:", City)


print("Question number2")
### Question 2: Check Voting Eligibility
# Take a person's age as input and check whether they are eligible to vote.
# Enter Age: 20
# You are eligible to vote

age=int(input("Enter Age:"))
if age>=18:
    print("You are eligible to vote.")
else:    print("You are not eligible to vote.")

print("Question number3")
###Question 3: Check Even or Odd Number

# Take a number from the user and determine whether it is even or odd using an if-else statement.
# Enter Number: 12
# 12 is an Even Number

number=int(input("Enter Number:"))
if number%2==0:
    print(number, "is an Even Number")
else:
    print(number, "is an Odd Number")


print("Question number4")
###Question 4: Student Grade Calculator
# Take a student's marks as input and calculate their grade based on the following criteria:
# Marks >= 90: Grade A
# Marks >= 70 and < 89: Grade B
# Marks >= 40 and < 69: Grade C
# # Marks < 40: Grade Fail
   
marks=int(input("Enter Marks:"))
if marks>=90:
    print("Grade A")
elif marks>=70 and marks<90:
    print("Grade B")
elif marks>=40 and marks<70:
    print("Grade C")
else:    print("Grade Fail")        

print("Question number5")
# Question 5: Office Entry System
# An employee can enter the office only if:
# - Employee ID is valid.
# - Employee is connected to the office Wi-Fi.

# condition
# - Invalid Employee ID → Access Denied.
# - Valid Employee ID → Check Wi-Fi connection.
# - Connected to office Wi-Fi → Access Granted.
# - Otherwise → Connect to Office Wi-Fi.

employee_id=input("Enter Employee ID:")
wifi_connected=input("Are you connected to the office Wi-Fi? (yes/no):")
if employee_id=="VALID_ID":
    if wifi_connected.lower()=="yes":
        print("Access Granted.")
    else:    print("Connect to Office Wi-Fi.")
else:    print("Access Denied. Invalid Employee ID.")

print("Question number6")
# Question 6: Scholarship Verification (Nested If)
# Description
# A student can receive a scholarship if:
# - Marks are 85 or above.
# - Family income is less than ₹5,00,000 per year.

# - Marks below 85 → Scholarship Rejected.
# - Marks 85 or above → Check family income.
# - Income below ₹5,00,000 → Scholarship Approved.
# - Otherwise → Scholarship Rejected.

marks=int(input("Enter Marks:"))
family_income=int(input("Enter Family Income (per year):"))
if marks>=85:
    if family_income<500000:
        print("Scholarship Approved.")
    else:    print("Scholarship Rejected. Family income exceeds the limit.")
else:    print("Scholarship Rejected. Marks are below 85.")

print("Question number7")
# Question 7: Print Numbers from 1 to 20
# Use a For Loop to print numbers from 1 to 20.
for i in range(1, 21):
    print(i)


print("Question number8")
# Question 8: Print Even Numbers from 1 to 50
### Description
# Use a For Loop and `range()` function to print all even numbers between 1 and 50.
### Expected Output`
# 2
# 4
# 6
# 8
# ...
# 50

for i in range(2, 51, 2):
    print(i)    
print("Question number9")
# Question 9: Multiplication Table
### Description
# Take a number as input and print its multiplication table from 1 to 10.
number=int(input("enter a number:"))
for i in range(1, 11):
    print(number, "x", i, "=", number * i)

print("Question number10")
# Question 10: Reverse Counting Using For Loop
print("Reverse counting from 10 to 1:")
for i in range(20,1,-1):
    print(i)

print("Question number11")
# Question 11: Print Numbers Using While Loop
### Description
# Use a While Loop to print numbers from 1 to 10.
i=1
while i<=10:
    print(i)
    i+=1

print("Question number12")
# Question 12: Reverse Counting Using While Loop
### Description
# Use a While Loop to print numbers from 10 to 1.
print("Reverse counting from 10 to 1:")
i=10
while i>=1:
    print(i)
    i-=1

print("Question number13")
# Question 13: Sum of Numbers from 1 to 100
### Description
# Use a loop to calculate the sum of all numbers from 1 to 100.
total_sum=0
for i in range(1, 101):
    total_sum+=i
print("Sum of numbers from 1 to 100:", total_sum)

print("Question number14")
# Question 14: Count Numbers Divisible by 5
### Description
# Use a loop to count how many numbers from 1 to 100 are divisible by 5.
count=0
for i in range(1, 101):
    if i%5==0:
        count+=1
print("Count of numbers divisible by 5 from 1 to 100:", count)

print("Question number15")
# Question 15: Mini ATM System
# Example Output
# 1. Check Balance
# 2. Deposit Money
# 3. Withdraw Money
# Enter Choice: 1
# Current Balance: ₹5000

balance=5000
print("1. Check Balance")
print("2. Deposit Money")   
print("3. Withdraw Money")
choice=int(input("Enter Choice:"))
if choice==1:
    print("Current Balance: ₹", balance)
elif choice==2:
    deposit_amount=int(input("Enter amount to deposit:"))
    balance+=deposit_amount
    print("Amount deposited. New Balance: ₹", balance)
elif choice==3:
    withdraw_amount=int(input("Enter amount to withdraw:"))
    if withdraw_amount<=balance:
        balance-=withdraw_amount
        print("Amount withdrawn. New Balance: ₹", balance)
    else:    print("Insufficient balance.")
else:    print("Invalid choice. Please select a valid option.")