# # Q1
# number = int(input("Enter your number:" ))
# if number > 0:
#     print("Positive number")
# elif number == 0:
#       print("Zero")  
# else:
#     print("Negative number")

# # Q2
# number = int(input("Enter your number:" ))
# if number > 0:
#     if number % 2 == 0:
#          print("Positive Even")
#     else:
#          print("Positive Odd")
# elif number == 0:
#      print("Zero")
# else:
#     if number % 2 == 0:
#           print("Negative Even")
#     else:
#          print("Negative Odd")

# # Q3
# num1 = int(input("Enter your first number:" ))
# num2 = int(input("Enter your second number:" ))

# if num1 > num2:
#      print(f"{num1} is greater number")
# elif num1 == num2:
#      print("Both are equal")
# else:
#      print(f"{num2} is greater number")      

# # Q4
# num1 = int(input("Enter your first number:" ))
# num2 = int(input("Enter your second number:" ))
# num3 = int(input("Enter your third number:" ))

# if num1 == num2 == num3:
#     print("Enter vaild pair of numbers")   
# if num1 >= num2 >= num3:
#      print(f"{num3} is the smallest number")
# elif num2 >= num1 >= num3:
#      print(f"{num3} is the smallest number")
# elif num1 >= num3 >= num2:
#      print(f"{num2} is the smallest number")
# elif num3 >= num2 >= num2:
#      print(f"{num2} is the smallest number")      
# elif num2 >= num3 >= num1:
#      print(f"{num1} is the smallest number")  
# elif num3 >= num2 >= num1:
#      print(f"{num1} is the smallest number") 
# else:
#     print("Enter vaild pair of number")           

# # Q5
# num1 = int(input("Enter your first number:" ))
# num2 = int(input("Enter your second number:" ))
# num3 = int(input("Enter your third number:" ))

# if num1 == num2 == num3:
#     print("Enter vaild pair of numbers")   
# if num1 < num2 < num3:
#      print(f"{num3} is the gratest number")
# elif num2 < num1 < num3:
#      print(f"{num3} is the greatest number")
# elif num1 < num3 < num2:
#      print(f"{num2} is the greatest number")
# elif num3 < num2 < num2:
#      print(f"{num2} is the greatest number")      
# else:
#      print(f"{num1} is the greatest number")  

# # Q6
# number = int(input("Enter your number:" ))

# if number % 5 == 0 and number % 11 == 0:
#      print("Divisible by both 5 and 11")
# elif number % 5 == 0 and number % 11 != 0:
#      print("Divisible only by 5")
# elif number % 11 == 0 and number % 5 != 0:
#      print("Divisible only by 11")       
# else:
#      print("Divisible by neither")                               

# # Q7
# number = int(input("Enter your number:" ))

# if number % 3 == 0 and number % 7 == 0:
#      print("Divisible by both 3 and 7")
# elif number % 3 == 0 and number % 7 != 0:
#      print("Divisible only by 3")
# elif number % 7 == 0 and number % 3 != 0:
#      print("Divisible only by 7")       
# else:
#      print("Divisible by neither")

# # Q8
# marks = int(input("Enter your marks: "))
# if marks > 100 and marks < 0:
#     print("Invalid marks")
# if marks >= 40:
#     print("Pass")
# else:
#     print("Fail")

# # Q9
# Marks = int(input("Enter your marks: "))

# if Marks>=90 and Marks<=100:
#     print("A")
# elif Marks>=80 and Marks<=89:
#     print("B")
# elif Marks>=70 and Marks<=79:
#     print("C")  
# elif Marks>=60 and Marks<=69:
#     print("D")
# elif Marks>=40 and Marks<=59:
#     print("E")            
# elif Marks<40 and Marks>=0:
#     print("Fail") 
# else:
#     print("Invalid")   

# # Q10
# age = int(input("enter your age: "))

# if age >= 18 and age <= 120:
#      print("Can vote")
# elif age < 18:
#     if age < 0:
#         print("Invalid")
#     else:
#         print("Cannot vote")

# # Q11
# year = int(input("Enter your year: "))

# if year % 400 == 0:
#     print("It is a leap year")
# elif year % 4 == 0 and year % 100 ==0:
#     print("It is a leap year")        
# else:
#     print("It is not a leap year")

# # Q12
# character = input("Enter your character: ")

# if chr(65) <= character <= chr(90):
#     print("Uppercase")
# elif chr(97) <= character <= chr(122):
#     print("Lowercase")
# elif chr(48) <= character <= chr(57):
#     print("Digit")
# else:
#     print("Special character")    

# # Q13
# ch = input("Enter your character: ").lower()

# ch = input("Enter a character: ")

# if ch >= 'a' and ch <= 'z':
#     if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U':
#         print("Vowel")
#     else:
#         print("Consonant")
# else:
#     print("Invalid input")

# # Q14
# Cost_price = int(input("Enter the cost price: "))
# Selling_price = int(input("Enter the selling price: "))    

# if Cost_price < Selling_price:
#     print(f"Profit = {Selling_price - Cost_price}")
# elif Cost_price == Selling_price:
#     print("No profit no loss")
# else:
#     print(f"Loss = {Cost_price - Selling_price}")

# # Q15
# Cost_price = int(input("Enter the cost price: "))
# Selling_price = int(input("Enter the selling price: "))    
# Profit = (Selling_price - Cost_price)
# Loss = (Cost_price - Selling_price)
# Profit_percent = ((Profit/Cost_price)*100)
# Loass_percent = ((Loss/Cost_price)*100)
# if Cost_price < Selling_price:
#     print(f"Profit percent = {Profit_percent}")
# elif Cost_price == Selling_price:
#     print("No profit no loss")
# else:
#        print(f"Loss percent = {Loass_percent}")

# Q16
# unit = int(input("Enter the units consumed: "))
# a = (unit-100)
# b = (unit-200)

# if 0 < unit <= 100:
#     print(f"Electricity bill = {unit*5}")  
# elif 0 < unit <= 200:
#     print(f"Electricity bill = {a*7 + 500}")
# elif unit > 200:
#     print(f"Electricity bill = {b*10 +1200}") 

# Q17
operator=int(input("Enter a Number of following Operations that You want to Perform:\n 1 for Addition\n 2 for Subtraction\n 3 for Multiplication\n 4 for division\n Enter the operator number: "))
if operator==1 or operator==2 or operator==3 or operator==4 :
    num1=float(input(" Enter your First-number: ")) 
    num2=float(input(" Enter your Second-number: "))
    
    if operator == 1:
        print(f" Addition of numbers = {num1+num2}")
    elif operator == 2:
        print(f"Subtraction of numbers = {num1-num2}")
    elif operator == 3:
        print(f" Multiplication of numbers = {num1*num2}") 
    elif operator == 4:
        if num2 != 0:
            print(f" Division of numbers = {num1/num2}")
        else:
            print("Invalid number")    
else:
    print("Invalid Operator")

# # Q18
# # temperature = int(input("Enter the value of temperature in celecius: "))    

# # if temperature > 35:
# #     print("Hot")
# # elif 26 <= temperature <= 35:
# #     print("Normal")    
# # elif 16 <= temperature <= 25:
# #     print("Cold")
# # elif 15 <= temperature <= 0:
# #     print("Very cold")
# # else:
# #     print("Freezing") 

# # Q19
# number = int(input("Enter your n umber: "))

# if number < 0:
#     print("Negative")
# elif 0 <= number <=10:
#     print("Number is between 0 and 10")
# elif 11 <= number <=50:
#     print("Number is between 11 and 50")
# elif 51 <= number <=100:
#     print("Number is between 51 and 100")
# else:
#     print("Number is above hundred")

# # Q20
# a = int(input("Enter the first side of triangle: "))
# b = int(input("Enter the second side of triangle: "))
# c = int(input("Enter the third side of triangle: "))

# if a + b > c and a + c > b and b + c > a:
#     print("valid triangle") 
# else:
#     print("Invalid triangle") 

# # Q21
# a = int(input("Enter the first side of triangle: "))
# b = int(input("Enter the second side of triangle: "))
# c = int(input("Enter the third side of triangle: "))

# if a + b > c and a + c > b and b + c > a:
#     if a == b == c:
#         print("Equilateral triangle")
#     elif a == b or b == c or a == c:
#         print("Isosceles tiangle")
#     else:
#         print("Scalene triangle") 
# else:
#     print("Invalid triangle") 

# # Q22
# Amount_balance = int(input("Enter the amount balance: "))
# Withdrawal_amount = int(input("enter the withdrawal amount: "))

# if Withdrawal_amount > 0 and Withdrawal_amount % 2 ==0 and Withdrawal_amount < Amount_balance and Amount_balance - Withdrawal_amount >= 500:
#     print("Withdrawal successful")
#     print(f"Remaining balance: {Amount_balance-Withdrawal_amount}")
# else:
#     print("Conditioned not satisfied")

# # Q23
# Username = input("Enter your usernam: ")
# Password = input("Enteer your password: ") 

# if Username == "admin":
#     if Password == "python123":
#         print("Login successfuly")
#     else:
#         print("Wrong Password")
# else:
#     if Password == "python123":
#         print("User not found")
#     else:
#         print("Wrong password and user not found")

# Q24
Purchase_amount = float(input("Enter the purchase amount: "))

if Purchase_amount < 500:
    print(f"Purchase_amount = {Purchase_amount}")
    print("Discount percentage = 0%")
    print("Discount amount = 0")
    print(f"Final amount = {Purchase_amount}")
elif 500 <= Purchase_amount <= 999:
    print(f"Purchase_amount = {Purchase_amount}")
    print("Discount percentage = 5%")
    print(f"Discount amount = {Purchase_amount * 0.05}")
    print(f"Final amount = {Purchase_amount + Purchase_amount*0.05}")
elif 1000 <= Purchase_amount <= 1999:
    print(f"Purchase_amount = {Purchase_amount}")
    print("Discount percentage = 10%")
    print(f"Discount amount = {Purchase_amount * 0.1}")
    print(f"Final amount = {Purchase_amount + Purchase_amount * 0.1}")    
elif 2000 <= Purchase_amount <= 4999:
    print(f"Purchase_amount = {Purchase_amount}")
    print("Discount percentage = 15%")
    print(f"Discount amount = {Purchase_amount * 0.15}")
    print(f"Final amount = {Purchase_amount + Purchase_amount*0.15}")     
else:
    print(f"Purchase_amount = {Purchase_amount}")
    print("Discount percentage = 20%")
    print(f"Discount amount = {Purchase_amount * 0.2}")
    print(f"Final amount = {Purchase_amount + Purchase_amount*0.2}")      

# Q25
marks1 = float(input("Enter the marks of first subject: "))
marks2 = float(input("Enter the marks of second subject: "))
marks3 = float(input("Enter the marks of third subject: "))
average = ((marks1 + marks2 + marks3)/3)
if marks1 > 35 and marks2 > 35 and marks3 > 35:
    if average >= 75:
        print("Distinction")
    elif 60 <= average <= 74:
        print("First Class")
    elif 50 <= average <= 59:
        print("Secind Class")    


      