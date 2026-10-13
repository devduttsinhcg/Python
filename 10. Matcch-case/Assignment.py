#                                                          ****************************                                                                                                    
#                                                          |--------------------------|                                                
#                                                          |        Match-Case        |                                               
#                                                          |--------------------------|                                              
#                                                          ****************************                                           
# ______________________________________________________________________________________________________________________________________________________
# QUESTION 1

choice = int(input("Enter your choice: "))

match choice:
    case 1:
        print("Pizza")
    case 2:
        print("Burger")
    case 3:
        print("Pasta")
    case 4:
        print("Sandwich")
    case _:
        print("Invalid Menu Choice")

#_________________________________________________________________________________________________________________________________

# QUESTION 2

choice = int(input("Enter choice: "))

match choice:
    case 1:
        print("Wi-Fi")
    case 2:
        print("Bluetooth")
    case 3:
        print("Mobile Data")
    case 4:
        print("Airplane Mode")
    case 5:
        print("Exiting")
    case _:
        print("Invalid Setting")

#_________________________________________________________________________________________________________________________________

# QUESTION 3

choice = int(input("Enter choice: "))

match choice:
    case 1:
        print("Check Balance")
    case 2:
        print("Withdraw Money")
    case 3:
        print("Deposit Money")
    case 4:
        print("Change PIN")
    case 5:
        print("Exiting ATM")
    case _:
        print("Invalid Choice")

#_________________________________________________________________________________________________________________________________

# QUESTION 4

signal = input("Enter signal: ").strip().lower()

match signal:
    case "red":
        print("Stop")
    case "yellow":
        print("Wait")
    case "green":
        print("Go")
    case _:
        print("Invalid Signal")

#_________________________________________________________________________________________________________________________________

# QUESTION 5

choice = int(input("Enter choice: "))

match choice:
    case 1:
        print(" Pro")
    case 2:
        print(" Courses")
    case 3:
        print(" Marks")
    case 4:
        print(" Attendance")
    case 5:
        print("Logging Out")
    case _:
        print("Invalid Choice")

#_________________________________________________________________________________________________________________________________

# QUESTION 6

choice = int(input("Enter category: "))

match choice:
    case 1:
        print(" Electronics")
    case 2:
        print(" Clothing")
    case 3:
        print(" Books")
    case 4:
        print(" Grocery")
    case 5:
        print("Exiting")
    case _:
        print("Invalid Category")

#_________________________________________________________________________________________________________________________________

# QUESTION 7

choice = int(input("Enter service: "))

match choice:
    case 1:
        print(" Account Balance")
    case 2:
        print(" Mini Statement")
    case 3:
        print(" Fund Transfer")
    case 4:
        print(" Bill")
    case 5:
        print(" Customer Support")
    case _:
        print("Invalid Service")

#_________________________________________________________________________________________________________________________________

# QUESTION 8

choice = int(input("Enter show: "))

match choice:
    case 1:
        print("Morning Show")
    case 2:
        print("Afternoon Show")
    case 3:
        print("Evening Show")
    case 4:
        print("Night Show")
    case _:
        print("Invalid Show")
#_________________________________________________________________________________________________________________________________

# QUESTION 9
weather = input("Enter weather: ").strip().lower()

match weather:
    case "sunny":
        print("Wear sunglasses")
    case "rainy":
        print("Umbrella")
    case "cloudy":
        print("Weather change")
    case "snowy":
        print("Warm clothes")
    case _:
        print("Invalid Weather")

#_________________________________________________________________________________________________________________________________

# QUESTION 10
method = input("Enter payment method: ").strip().lower()

match method:
    case "upi":
        print("UPI")
    case "card":
        print("Card")
    case "cash":
        print("Cash")
    case "wallet":
        print("Wallet")
    case _:
        print("Invalid Method")

#_________________________________________________________________________________________________________________________________

# QUESTION 11
extension = input("Enter extension: ").strip().lower().

match extension:
    case "pdf":
        print("Document ")
    case "jpg" | "png":
        print("Image ")
    case "mp3":
        print("Audio ")
    case "mp4":
        print("Video ")
    case _:
        print("Unknown File Type")

#_________________________________________________________________________________________________________________________________

# QUESTION 12
role = input("Enter role: ").strip().lower()

match role:
    case "admin":
        print("Full Access")
    case "teacher":
        print("Teacher Dashboard")
    case "student":
        print("Student Dashboard")
    case "guest":
        print("Limited Access")
    case _:
        print("Invalid Role")

#_________________________________________________________________________________________________________________________________

# QUESTION 13
day = int(input("Enter day number: "))

match day:
    case 1 | 2 | 3 | 4 | 5:
        print("Weekday")
    case 6 | 7:
        print("Weekend")
    case _:
        print("Invalid Day")

#_________________________________________________________________________________________________________________________________

# QUESTION 14
priority = int(input("Enter priority (1-4): "))

match priority:
    case 1 | 2:
        print("Normal Priority")
    case 3 | 4:
        print("Urgent Priority")
    case _:
        print("Invalid Priority")

#_________________________________________________________________________________________________________________________________

# QUESTION 15
level = int(input("Enter membership level (1-4): "))

match level:
    case 1 | 2:
        print("Basic Membership")
    case 3 | 4:
        print("Premium Membership")
    case _:
        print("Invalid Membership Level")

#_________________________________________________________________________________________________________________________________

# QUESTION 16
user_type = int(input("Enter user type (1 Student, 2 Teacher): "))

match user_type:
    case 1:
        option = int(input("1 View Courses, 2 View Marks, 3 View Attendance: "))
        match option:
            case 1:
                print(" Student Courses")
            case 2:
                print(" Student Marks")
            case 3:
                print(" Student Attendance")
            case _:
                print("Invalid Student Option")
    case 2:
        option = int(input("1 View Students, 2 Enter Marks, 3 View Attendance: "))
        match option:
            case 1:
                print(" Students")
            case 2:
                print("Entering Marks")
            case 3:
                print(" Teacher Attendance")
            case _:
                print("Invalid Teacher Option")
    case _:
        print("Invalid User Type")

#_________________________________________________________________________________________________________________________________

# QUESTION 17
account = int(input("Enter account type (1 Savings, 2 Current): "))
operation = int(input("Enter operation (1 Balance, 2 Deposit, 3 Withdraw): "))

match account:
    case 1:
        print("Saving Account")
    case 2:
        print("Current Account")
    case _:
        print("Invalid Account Type")


match operation:
    case 1:
        print("Check Balance")
    case 2:
        print("Deposit")
    case 3:
        print("Withdraw")
    case 0:
        pass
    case _:
        print("Invalid Operation")

#_________________________________________________________________________________________________________________________________

# QUESTION 18
category = int(input("Enter category (1 Electronics, 2 Clothing): "))

match category:
    case 1:
        product = int(input("1 Mobile, 2 Laptop, 3 Headphones: "))
        match product:
            case 1:
                print("Mobile")
            case 2:
                print("Laptop")
            case 3:
                print("Headphones")
            case _:
                print("Invalid Product")
    case 2:
        product = int(input("1 Shirt, 2 Jeans, 3 Shoes: "))
        match product:
            case 1:
                print("Shirt")
            case 2:
                print("Jeans")
            case 3:
                print("Shoes")
            case _:
                print("Invalid Product")
    case _:
        print("Invalid Category")

#_________________________________________________________________________________________________________________________________

# QUESTION 19
category = int(input("Enter category (1 Vegetarian, 2 Non-Vegetarian): "))

match category:
    case 1:
        food = int(input("1 Paneer, 2 Dal, 3 Veg Biryani: "))
        match food:
            case 1:
                print("Paneer")
            case 2:
                print("Dal")
            case 3:
                print("Veg Biryani")
            case _:
                print("Invalid Food Choice")
    case 2:
        food = int(input("1 Chicken Biryani, 2 Chicken Curry, 3 Fish Fry: "))
        match food:
            case 1:
                print("Chicken Biryani")
            case 2:
                print("Chicken Curry")
            case 3:
                print("Fish Fry")
            case _:
                print("Invalid Food Choice")
    case _:
        print("Invalid Category")

#_________________________________________________________________________________________________________________________________

# QUESTION 20
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ").strip()

match operator:
    case "+":
        print("Result =", num1 + num2)
    case "-":
        print("Result =", num1 - num2)
    case "*":
        print("Result =", num1 * num2)
    case "/":
        if num2 == 0:
            print("Cannot divide by zero")
        else:
            print("Result =", num1 / num2)
    case _:
        print("Invalid Operator")

#_________________________________________________________________________________________________________________________________

# QUESTION 21
choice = int(input("1 Celsius to Fahrenheit, 2 Fahrenheit to Celsius: "))
temperature = float(input("Enter temperature: "))

match choice:
    case 1:
        result = (temperature * 9 / 5) + 32
        print("Temperature =", result, "F")
    case 2:
        result = (temperature - 32) * 5 / 9
        print("Temperature =", result, "C")
    case _:
        print("Invalid Choice")

#_________________________________________________________________________________________________________________________________

# QUESTION 22
choice = int(input("Enter choice (1-4): "))
value = float(input("Enter value: "))

match choice:
    case 1:
        print(value * 1000, "meters")
    case 2:
        print(value / 1000, "kilometers")
    case 3:
        print(value * 1000, "grams")
    case 4:
        print(value / 1000, "kilograms")
    case _:
        print("Invalid Choice")

#_________________________________________________________________________________________________________________________________

# QUESTION 23
account = int(input("Enter account type (1 Savings, 2 Current): "))

match account:
    case 1:
        print("Savings Account")
        amount = float(input("Enter amount: "))
        if amount > 0:
            print("Withdrawal Request Accepted")
        else:
            print("Invalid Amount")
    case 2:
        print("Current Account")
        amount = float(input("Enter amount: "))
        if amount > 0:
            print("Withdrawal Request Accepted")
        else:
            print("Invalid Amount")
    case _:
        print("Invalid Account Type")

#_________________________________________________________________________________________________________________________________

# QUESTION 24
choice = int(input("Enter choice (1 Start Exam, 2 View Result, 3 Exit): "))

match choice:
    case 1:
        age = int(input("Enter age: "))
        if age >= 18:
            print("You can start the exam")
        else:
            print("You must be at least 18")
    case 2:
        print(" Result")
    case 3:
        print("Exiting")
    case _:
        print("Invalid Choice")

#_________________________________________________________________________________________________________________________________

# QUESTION 25
ticket = int(input("Enter ticket type (1 Regular, 2 Premium, 3 VIP): "))
age = int(input("Enter age: "))

if age < 5:
    print("Free Entry")
else:
    match ticket:
        case 1:
            print("Regular Ticket")
        case 2:
            print("Premium Ticket")
        case 3:
            print("VIP Ticket")
        case _:
            print("Invalid Ticket Type")

#_________________________________________________________________________________________________________________________________

# QUESTION 26
device = int(input("Enter device (1 Light, 2 Fan, 3 AC, 4 TV): "))

match device:
    case 1:
        print("Light Controller Opened")
    case 2:
        print("Fan Controller Opened")
    case 3:
        print("AC Controller Opened")
    case 4:
        print("TV Controller Opened")
    case _:
        print("Invalid Device")

#_________________________________________________________________________________________________________________________________

# QUESTION 27
department = int(input("Enter department (1-5): "))

match department:
    case 1:
        print("General Medicine")
    case 2:
        print("Cardiology")
    case 3:
        print("Orthopedics")
    case 4:
        print("Pediatrics")
    case 5:
        print("Emergency")
    case _:
        print("Invalid Department")

#_________________________________________________________________________________________________________________________________

# QUESTION 28
choice = int(input("Enter choice (1-5): "))

match choice:
    case 1:
        print("Book Ticket")
    case 2:
        print("Cancel Ticket")
    case 3:
        print("Check PNR")
    case 4:
        print("Train Schedule")
    case 5:
        print("Exiting")
    case _:
        print("Invalid Choice")

#_________________________________________________________________________________________________________________________________

# QUESTION 29
choice = int(input("Enter choice (1-5): "))

match choice:
    case 1:
        print("Searching Book")
    case 2:
        print("Issuing Book")
    case 3:
        print("Returning Book")
    case 4:
        print("Viewing Issued Books")
    case 5:
        print("Exiting Library")
    case _:
        print("Invalid Choice")

#_________________________________________________________________________________________________________________________________

# QUESTION 30
status = input("Enter status: ").strip().lower()

match status:
    case "placed":
        print("Your order is placed")
    case "confirmed":
        print("Your order is confirmed")
    case "preparing":
        print("Your order is  prepared")
    case "out_for_delivery":
        print("Your order is comming")
    case "delivered":
        print("Your order is delivered")
    case "cancelled":
        print("Your order is cancelled")
    case _:
        print("Invalid Order Status")
