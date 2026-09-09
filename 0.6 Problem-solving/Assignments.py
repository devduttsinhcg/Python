# Q1
number = int(input("Enter your number:" ))
if number > 0:
    print("Positive number")
elif number == 0:
      print("Zero")  
else:
    print("Negative number")

# Q2
number = int(input("Enter your number:" ))
if number > 0:
    if number % 2 == 0:
         print("Positive Even")
    else:
         print("Positive Odd")
elif number == 0:
     print("Zero")
else:
    if number % 2 == 0:
          print("Negative Even")
    else:
         print("Negative Odd")

# Q3
num1 = int(input("Enter your first number:" ))
num2 = int(input("Enter your second number:" ))

if num1 > num2:
     print(f"{num1} is greater number")
elif num1 == num2:
     print("Both are equal")
else:
     print(f"{num2} is greater number")      

# Q4
num1 = int(input("Enter your first number:" ))
num2 = int(input("Enter your second number:" ))
num3 = int(input("Enter your third number:" ))

if num1 == num2 == num3:
    print("Enter vaild pair of numbers")   
if num1 >= num2 >= num3:
     print(f"{num3} is the smallest number")
elif num2 >= num1 >= num3:
     print(f"{num3} is the smallest number")
elif num1 >= num3 >= num2:
     print(f"{num2} is the smallest number")
elif num3 >= num2 >= num2:
     print(f"{num2} is the smallest number")      
elif num2 >= num3 >= num1:
     print(f"{num1} is the smallest number")  
elif num3 >= num2 >= num1:
     print(f"{num1} is the smallest number") 
else:
    print("Enter vaild pair of number")           

# Q5
num1 = int(input("Enter your first number:" ))
num2 = int(input("Enter your second number:" ))
num3 = int(input("Enter your third number:" ))

if num1 == num2 == num3:
    print("Enter vaild pair of numbers")   
if num1 < num2 < num3:
     print(f"{num3} is the gratest number")
elif num2 < num1 < num3:
     print(f"{num3} is the greatest number")
elif num1 < num3 < num2:
     print(f"{num2} is the greatest number")
elif num3 < num2 < num2:
     print(f"{num2} is the greatest number")      
else:
     print(f"{num1} is the greatest number")  

# Q6
number = int(input("Enter your number:" ))

if number % 5 == 0 and number % 11 == 0:
     print("Divisible by both 5 and 11")
elif number % 5 == 0 and number % 11 != 0:
     print("Divisible only by 5")
elif number % 11 == 0 and number % 5 != 0:
     print("Divisible only by 11")       
else:
     print("Divisible by neither")                               

# Q7
number = int(input("Enter your number:" ))

if number % 3 == 0 and number % 7 == 0:
     print("Divisible by both 3 and 7")
elif number % 3 == 0 and number % 7 != 0:
     print("Divisible only by 3")
elif number % 7 == 0 and number % 3 != 0:
     print("Divisible only by 7")       
else:
     print("Divisible by neither")

# Q8
marks = int(input("Enter your marks: "))
if marks > 100 and marks < 0:
    print("Invalid marks")
if marks >= 40:
    print("Pass")
else:
    print("Fail")

# Q9
Marks = int(input("Enter your marks: "))

if Marks>=90 and Marks<=100:
    print("A")
elif Marks>=80 and Marks<=89:
    print("B")
elif Marks>=70 and Marks<=79:
    print("C")  
elif Marks>=60 and Marks<=69:
    print("D")
elif Marks>=40 and Marks<=59:
    print("E")            
elif Marks<40 and Marks>=0:
    print("Fail") 
else:
    print("Invalid")   

# Q10
age = int(input("enter your age: "))

if age >= 18 and age <= 120:
     print("Can vote")
elif age < 18:
    if age < 0:
        print("Invalid")
    else:
        print("Cannot vote")

# Q11
year = int(input("Enter your year: "))

if year % 400 == 0:
    print("It is a leap year")
elif year % 4 == 0 and year % 100 ==0:
    print("It is a leap year")        
else:
    print("It is not a leap year")

# Q12
character = input("Enter your character: ")

if chr(65) <= character <= chr(90):
    print("Uppercase")
elif chr(97) <= character <= chr(122):
    print("Lowercase")
elif chr(48) <= character <= chr(57):
    print("Digit")
else:
    print("Special character")    

# Q13
ch = input("Enter your character: ").lower()

ch = input("Enter a character: ")

if ch >= 'a' and ch <= 'z':
    if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U':
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Invalid input")

Q14
Cost_price = int(input("Enter the cost price: "))
Selling_price = int(input("Enter the selling price: "))    

if Cost_price < Selling_price:
    print(f"Profit = {Selling_price - Cost_price}")
elif Cost_price == Selling_price:
    print("No profit no loss")
else:
    print(f"Loss = {Cost_price - Selling_price}")

# Q15
Cost_price = int(input("Enter the cost price: "))
Selling_price = int(input("Enter the selling price: "))    
Profit = (Selling_price - Cost_price)
Loss = (Cost_price - Selling_price)
Profit_percent = ((Profit/Cost_price)*100)
Loass_percent = ((Loss/Cost_price)*100)
if Cost_price < Selling_price:
    print(f"Profit percent = {Profit_percent}")
elif Cost_price == Selling_price:
    print("No profit no loss")
else:
       print(f"Loss percent = {Loass_percent}")

# Q16
unit = int(input("Enter the units consumed: "))

if 0 < unit <= 100:
    print(f"Electricity bill = {unit*5}")     
        


      