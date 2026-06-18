# Task 1: Create a Car Class
from platform import processor


class Car:
    def __init__(self, brand, color, model):
        self.brand = brand
        self.color = color
        self.model = model

    def print_details(self):
        print(f"Brand: {self.brand}, Color: {self.color}, Model: {self.model}")

# Create 2 objects of the Car class
car1 = Car("Toyota", "Blue", "Camry")
car2 = Car("Honda", "Red", "Civic")

# Print the details of both cars
car1.print_details()
car2.print_details()


# Task 2: Create a Student Class

class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def displayStudent(self):
        print(f"Name: {self.name}, Age: {self.age}, Course: {self.course}")




# Task 3: Create a Constructor
class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def displayEmployee(self):
        print(f"Name: {self.name}, Employee ID: {self.emp_id}, Salary: {self.salary}")

# Create 3 employee objects
emp1 = Employee("Rahul", 1, 50000)
emp2 = Employee("Raju", 2, 60000)
emp3 = Employee("Raghur", 3, 70000)

# Display all employee details
emp1.displayEmployee()
emp2.displayEmployee()
emp3.displayEmployee()


# Task 4: Create a Mobile Class
class Mobile:
    def __init__(self, brand, ram, storage, price):
        self.brand = brand
        self.ram = ram
        self.storage = storage
        self.price = price

    def displayMobileInfo(self):
        print(f"Brand: {self.brand}, RAM: {self.ram}GB, Storage: {self.storage}GB, Price: ${self.price}")


# Create 3 mobile objects
mobile1 = Mobile("Apple", 128, 256, 999)
mobile2 = Mobile("Samsung", 64, 128, 799)
mobile3 = Mobile("Google", 32, 64, 599)

# Display all mobile details
mobile1.displayMobileInfo()
mobile2.displayMobileInfo()
mobile3.displayMobileInfo()


# Task 5: Create a Bank Account Class
class BankAccount:
    def __init__(self, holder_name, account_number, balance):
        self.holder_name = holder_name
        self.account_number = account_number
        self.balance = balance

    def displayAccountDetails(self):
        print(f"Account Holder: {self.holder_name}, Account Number: {self.account_number}, Balance: ${self.balance}")
bank1 = BankAccount("John Doe", "123456789", 1000)
bank2 = BankAccount("Jane Smith", "987654321", 2000)
bank3 = BankAccount("Bob Johnson", "456789123", 3000)
bank1.displayAccountDetails()
bank2.displayAccountDetails()
bank3.displayAccountDetails()

# Task 6: Create a Book Class

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def displayBook(self):
        print(f"Title: {self.title}, Author: {self.author}, Price: ${self.price}")

# Create 3 book objects
book1 = Book("1984", "George Orwell", 12.99)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 14.99)
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", 13.99)

# Display all book details
book1.displayBook()
book2.displayBook()
book3.displayBook()

# Task 7: Create a Building Class

class Building:
    def __init__(self):
        self.name = input("Enter the name of the building: ")
        self.location = input("Enter the location of the building: ")
        self.floors = int(input("Enter the number of floors: "))

    def displayBuildingInfo(self):
        print(f"Building Name: {self.name}, Location: {self.location}, Number of Floors: {self.floors}")

Building1 = Building()
Building1.displayBuildingInfo()


# Task 8: Create a Citizen Class

class Citizen:
    country = "India"

    def __init__(self, aadhaar, phone, name):
        self.aadhaar = aadhaar
        self.phone = phone
        self.name = name

    def displayCitizenInfo(self):
        print(f"Name: {self.name}, Phone: {self.phone}, Aadhaar: {self.aadhaar}, Country: {self.country}")

Citizen1 = Citizen(123456789012, "9876543210", "Rahul")
Citizen2 = Citizen(123456789013, "9876543211", "Rohit")
Citizen3 = Citizen(123456789014, "9876543212", "Ramesh")
Citizen1.displayCitizenInfo()
Citizen2.displayCitizenInfo()
Citizen3.displayCitizenInfo()

# Task 9: Create a Laptop Class

class Laptop:
    def __init__(self, brand, processor, ram, price):
        self.brand = brand
        self.processor = processor
        self.ram = ram
        self.price = price

    def displayLaptopInfo(self):
        print(f"Brand: {self.brand}, Processor: {self.processor}, RAM: {self.ram}GB, Price: ${self.price}")
Laptop1 = Laptop("Dell", "Intel i7", 16, 1200)
Laptop2 = Laptop("HP", "AMD Ryzen 5", 8, 800)
Laptop3 = Laptop("Apple", "M1", 16, 1500)
Laptop1.displayLaptopInfo()
Laptop2.displayLaptopInfo()
Laptop3.displayLaptopInfo()

# Task 10: Create a Movie Class
class Movie:
    def __init__(self, movie_name, hero_name, release_year):
        self.movie_name = movie_name
        self.hero_name = hero_name
        self.release_year = release_year

    def displayMovieInfo(self):
        print(f"Movie Name: {self.movie_name}, Hero Name: {self.hero_name}, Release Year: {self.release_year}")
Movie1 = Movie("Inception", "Leonardo DiCaprio", 2010)
Movie2 = Movie("The Dark Knight", "Christian Bale", 2008)
Movie3 = Movie("Interstellar", "Matthew McConaughey", 2014)
Movie1.displayMovieInfo()
Movie2.displayMovieInfo()
Movie3.displayMovieInfo()

# Task 11: Create a Teacher Class
class Teacher:

    def __init__(self, name, subject, experience):
        self.name = name
        self.subject = subject
        self.experience = experience

    def displayTeacherInfo(self):
        print(f"Name: {self.name}, Subject: {self.subject}, Experience: {self.experience} years")
Teacher1 = Teacher("Smith", "Mathematics", 10)
Teacher2 = Teacher("Johnson", "Science", 8)
Teacher3 = Teacher("Williams", "History", 15)
Teacher1.displayTeacherInfo()
Teacher2.displayTeacherInfo()
Teacher3.displayTeacherInfo()  

# Task 12: Create a Hospital Class


class Hospital:
    def __init__(self, name, doctor_count, city):
        self.name = name
        self.doctor_count = doctor_count
        self.city = city

    def displayHospitalInfo(self):
        print(f"Hospital Name: {self.name}, Doctor Count: {self.doctor_count}, City: {self.city}")
Hospital1 = Hospital("City Hospital", 50, "cuttack")
Hospital2 = Hospital("Green Valley Hospital", 30, "BHUbaneswar")   
Hospital1.displayHospitalInfo() 
Hospital2.displayHospitalInfo()

# Task 13: Create a Product Class
class Product:
    def __init__(self, product_name, category, price):
        self.product_name = product_name
        self.category = category
        self.price = price

    def displayProductInfo(self):
        print(f"Product Name: {self.product_name}, Category: {self.category}, Price: ${self.price}")
Product1 = Product("Laptop", "Electronics", 1200)
Product2 = Product("T-shirt", "Clothing", 25)
Product3 = Product("Coffee Maker", "Home Appliances", 80)
Product1.displayProductInfo()
Product2.displayProductInfo()
Product3.displayProductInfo()