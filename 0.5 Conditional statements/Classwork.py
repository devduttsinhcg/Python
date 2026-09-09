Number= int(input("Please enter a number: "))
if Number%2==0:
    print(f"{Number} is Even")

if Number%2!=0:
    print(f"{Number} is Odd")

print(type(Number))


Number= int(input("Please enter a number: "))
if Number%2==0:
    print(f"{Number} is Even")

else:
    print(f"{Number} is Odd")

print(type(Number))

is_indian = input("Are you Indian ? Yes or No: ").lower().strip()

if is_indian=="yes":
    age=int(input("Enter you age: "))
    if age>=18:
        print("You are eligible to vote.")
    else:
        print("You are not eligible to vote")    

else:
    print("You are not eligible to vote")

# #Task 4
Marks=int(input("Enter your marks: "))

if Marks>=90:
    print("Excellent")
elif Marks>=60:
    print("Good")
elif Marks>=40:
    print("Pass")    
else:
    print("Fail")        

#Task 5
operator=int(input("Enter a Number of following Operations that You want to Perform:\n 1 for Addition\n 2 for Subtraction\n 3 for Multiplication\n 4 for division\n Enter the operator number: "))
if operator==1 or operator==2 or operator==3 or operator==4 :
    num1=float(input(" Enter your First-number: ")[0:2]) 
    num2=float(input(" Enter your Second-number: "))

    if operator == 1:
        print(f" Addition of numbers={num1+num2}")
    elif operator == 2:
        print(f"Subtraction of numbers={num1-num2}")
    elif operator == 3:
        print(f" Multiplication of numbers={num1*num2}") 
    elif operator == 4:
        print(f" Division of numbers={num1/num2}")
else:
    print("Invalid Operator")      


   






     





