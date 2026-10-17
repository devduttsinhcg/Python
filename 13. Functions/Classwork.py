# def addition(a, b):
#     print(a+b)

# #_______________________________________________________________________________________________________________________________

# def subtraction(a, b):
#     print(a-b)

# #_______________________________________________________________________________________________________________________________

# def multiplication(a, b):
#     print(a*b)

# #_______________________________________________________________________________________________________________________________

# def division(a, b):
#     print(a/b)

# #_______________________________________________________________________________________________________________________________

# def floordivision(a, b):
#     print(a//b)  

# #_______________________________________________________________________________________________________________________________

# addition(10, 15)
# multiplication(10, 4)
# division(2,5)
# floordivision(2,4)

# #_______________________________________________________________________________________________________________________________

# def Is_even(number):
#     if number % 2 == 0:
#         print("Even")
#     else:
#         print("Not Even")

# Is_even(8)

# #_______________________________________________________________________________________________________________________________

# def Is_prime(number = int(input("Enter the number: "))):
#     for i in range(2, number):
#         if number % i == 0 :
#             print(f"{number} is not a prime number.")
#             break
#     else:
#         print(f"{number} is a prime number.")   

# Is_prime()

# #_______________________________________________________________________________________________________________________________

# name = "Devdutt"

# def greet():
#     print(f"Hello {name}")

# greet()

#_______________________________________________________________________________________________________________________________

# Existing_Balance = 30000 

# def check_balance(balance):
#     print(f"Your current balance is: {balance}")
#     return balance

# def withdrawal(balance):
#     withdrawal_amount = int(input("Enter the amount of withdrawal: "))
    
#     if withdrawal_amount <= balance: 
#         balance -= withdrawal_amount
#         print(f"{withdrawal_amount} withdrawn successfully.")
#         print(f"Current balance = {balance}")
#     else:
#         print("Invalid withdrawal amount (Insufficient funds)")
        
#     return balance

# def deposited(balance):
#     deposited_amount = int(input("Enter the amount to deposit: "))
    
#     balance += deposited_amount
#     print(f"{deposited_amount} is deposited")
#     print(f"Current balance = {balance}")
    
#     return balance


# operator = int(input("""Enter the operators:
#                         1 for check balance 
#                         2 for withdrawal 
#                         3 for depositing amount 
#                         0 for ending the call 
#                         Enter your choice: """))

# Flag = True
# while Flag:

#     if operator == 1:
#         Existing_Balance = check_balance(Existing_Balance)
#     elif operator == 2:
#         Existing_Balance = withdrawal(Existing_Balance)
#     elif operator == 3:
#         Existing_Balance = deposited(Existing_Balance)
#     elif operator == 0:
#         print("Thank you for using our services. Call ended.")
#         break
#     else:
#         print("Invalid choice, please try again.")

#     operator = int(input("""Enter the operators:
#                         1 for check balance 
#                         2 for withdrawal 
#                         3 for depositing amount 
#                         0 for ending the call 
#                         Enter your choice: """))    

#_______________________________________________________________________________________________________________________________

# a = 10
# b = 40
# c = 1
# d = 50

# def add(a, b):
#     c = a + b
#     return c

# def multiply(a, b, c):
#     c = a * b * c
#     return c

# print(multiply(add(a,b), d, c))

#_______________________________________________________________________________________________________________________________

def calculate(a, b):
    total = a + b
    difference = a - b
    return total, difference

answer = calculate(10, 4)
print(answer)

#_______________________________________________________________________________________________________________________________

def calculate(a, b):
    return a + b, a - b

total, difference = calculate(10, 4)

print(total, difference)

#_______________________________________________________________________________________________________________________________

def greet(name="Guest"):
    print("Hello", name)

greet()
greet("Asha")

#_______________________________________________________________________________________________________________________________

def describe(name, city, age=21,):
    print(name, age, city)

describe(name="devdutt", city="Gandhinaagr", age=56 )

#_______________________________________________________________________________________________________________________________

def add(a,b):
    def total():
        return a + b;
    return total();

print(add(10, 30))

#_______________________________________________________________________________________________________________________________

def count_function(count):
    count = count + 1

    if count == 5:
        return count

    count_function(count)

print(count_function(1))
