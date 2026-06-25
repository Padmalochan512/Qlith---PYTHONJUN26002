# print("This is all about OOPS")

# # make an object by using class as 

# class car:
#     car_name="BMW"
#     color="Black"
#     wheels=4

# car1=car()
# car2=car()
# car3=car()
# car4=car()

# print(car1.car_name)
# print(car1.color)
# print(car1.wheels)



# # method

# class student:
#     name="rahul"
#     age=10
#     def student_details(self):
#         print("my name is",self.name,"age is",self.age)
#     def viewInput(self,address,roll):
#         print("this is my address",address,"this is my roll number",roll)
# s1=student()
# print(s1.age)
# s1.student_details()
# s1.viewInput("noida",101)




# # constructor
# class citizen:
#     country="India"
#     def __init__(self,addhar,phone,name):
#         self.addhar=addhar
#         self.phone=phone
#         self.name=name

#     def printCitizen(self):
#         print("name:",self.name)
#         print("phone:",self.phone)
#         print("addhar:",self.addhar)
#         print("country:",self.country)

# c1=citizen(1234567890,"9876543210","Rahul")
# c2=citizen(1234567891,"9876543211","Rohit")
# c3=citizen(1234567892,"9876543212","Ramesh")
# c2.printCitizen()



class Building:
    def __init__(self):
        self.location = input("Enter the location of the building: ")
        self.pin = int(input("Enter the pin code: "))
        self.floors = int(input("Enter the number of floors: "))
        self.roomInfloor = int(input("Enter the number of rooms in each floor: "))

        print("Location:", self.location)
        print("Pin code:", self.pin)
        print("Number of floors:", self.floors)
        print("Number of rooms in each floor:", self.roomInfloor)


    def displayBuild(self):
        print("the building has",self.floors,"floor")
Building1 = Building()
Building1.displayBuild()
        