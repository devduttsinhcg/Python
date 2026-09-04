#Task 1
print("Hello",end=" ")
print("World")

#Task 2
num1,num2=map(int,input("Please enter the numbers: ").split()[0:2])
print(f"First number={num1}")
print(f"Second number={num2}")
print(f"Sum= {num1+num2}")

#Task 3
Price = input("Please enter the price of product: ")
Quantity = input("Please enter the quantity of the product: ")
print(f"Price of the product is {Price}")
print(f"Quantity of product is {Quantity}")
print(f"Total price is {Price+Quantity}")

#Task 4
name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
marks = int(input("Enter your marks:"))

#Task 5
Name = input("Please enter your name: ")
Age = int(input("Please enter your age: "))
Height = float(input("Please enter your height: "))
City = input("Please enter your name of city you belog: ")
print(f"Name of student is:{Name}")
print(f"Age of student is:{Age}")   
print(f"Height of student is:{Height: .2f}") 
print(f"Student is from city of {City}") 