# def addtwonumber(a,b):
#     print(a+b)
# addtwonumber(4,5)

# def runloop(x, y):
#     for i in range(x, y):
#         print(i)

# runloop(1, 10)

# def myreturnfunction():
#     return "hello world"
# op=myreturnfunction()
# print(op)


# def studentdetails():
#     name=input("Enter your name: ")
#     age=int(input("Enter your age: "))
#     per=int(input("Enter your percentage:"))
#     reg=input("Enter your registration number:")
#     print(name,age,per,reg)
# studentdetails()

# fruit="Apple"
# def printfruit():
#     student_1="padu"
#     print(fruit,student_1)
# printfruit(fruit,student_1)

def Coloroption(color):
    color = color.lower()

    if color == "red":
        return "stop"
    elif color == "yellow":
        return "orange"
    elif color == "green":
        return "go"
    else:
        return "Invalid color"
user_color=input("Enter color:")
print(Coloroption(user_color))