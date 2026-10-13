#                                                          ****************************                                                                                                    
#                                                          |--------------------------|                                                
#                                                          |        Match-case        |                                               
#                                                          |--------------------------|                                              
#                                                          ****************************                                           
# ______________________________________________________________________________________________________________________________________________________

# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))

# operation = int(input("Enter the operation number \n 1 for addition \n 2 for subtraction \n 3 for multiplication \n 4 for division \n Enter the operator: "))

# match operation:
#     case 1:
#         print(f"Addition = {num1 + num2}")
#     case 2:
#         print(f"Subtraction = {num1 - num2}")
#     case 3:
#         print(f"Multiplication = {num1 * num2}")
#     case 4:
#         print(f"Division = {num1 / num2}")                    
#     case _:
#         print("Enter valid operator")

#_____________________________________________________________________________________________________________________________
# i = int(input("Enter the number:"))
# while i != 0 :
#     num1 = int(input("Enter the first number: "))
#     num2 = int(input("Enter the second number: "))

#     operation = int(input("Enter the operation number \n 1 for addition \n 2 for subtraction \n 3 for multiplication \n 4 for division \n Enter the operator: "))

#     match operation:
#         case 1:
#             print(f"Addition = {num1 + num2}")
#         case 2:
#             print(f"Subtraction = {num1 - num2}")
#         case 3:
#             print(f"Multiplication = {num1 * num2}")
#         case 4:
#             print(f"Division = {num1 / num2}")                    
#         case _:
#             print("Enter valid operator")

#     break

#_____________________________________________________________________________________________________________________________ 

# num3 = int(input("Enter the number:"))

# choice = int(input("""Enter the choice:
#                    1 for even
#                    2 for odd
#                    3 for prime:"""))

# match choice:
#     case 1:
#         if num3 % 2 == 0:
#             print("Even")
#     case 2:
#             if num3 % 2 == 1:
#                 print("Odd")
#     case 3:
#             for i in range(2, num3):
#                 if num3 % i != 0:
#                     print("Not a Prime")
#                     break    
#             else:
#                 print("Prime")    
#     case _:
#         print("Invalid choice")

#_____________________________________________________________________________________________________________________________                                

# day = int(input("Enter the number: "))

# match day:
#     case 1 | 2 | 3 | 4 | 5:
#         print("Weekday")
#     case 6 | 7 :
#         print("Weekend")
#     case _ :
#         print("Invalid Day")

#_____________________________________________________________________________________________________________________________      

# day = int(input("Enter the number: "))

# match day:
     
#     case day if day == 1 or day == 2 or day == 3 or day == 4 or day == 5:
#         print("Week-Day")
    
#     case day if day == 6 or day == 7:
#         print("Weekend")

#     case _:
#         print("Invalid Day") 

#_____________________________________________________________________________________________________________________________

# marks = int(input("Enter the x: "))

# match marks:

#     case x if x >= 90:
#         print("A")

#     case x if x >= 75:
#         print("B")

#     case x if x >= 60:
#         print("C")

#     case x if x >= 40:
#         print("D")

#     case _:
#         print("Fail")

#_____________________________________________________________________________________________________________________________

device_type = input("Enter the device type: ").upper()
command = int(input("Enter the command number: "))

match device_type:
    case "AC":
        match command:

            case 1:
                print("Turn On")

            case 2:
                print("Set Temperature")

            case _:
                print("Invalid Command")        

    case "LIGHTS":
        match command:

            case 1:
                print("Turn On")
            
            case 2:
                print("Dim")
            
            case 3:
                print("Change Colour")

            case _:
                print("Invalid command")

    case _:
        print("Device not found") 

#_____________________________________________________________________________________________________________________________

membership_level = input("Enter the level of membership: ")
order_total = int(input("Enter the total order value: "))

match membership_level:

    case "Premium":

        match order_total:

            case x if x >= 100:
                print(f"Total price = {(order_total) - (order_total*0.1)}")

            case x if x < 100:
                print(f"Total price = {order_total}")

            case _:
                print("Invalid order value")    

    case "Regular":

        match order_total:

            case x if x >= 150:
                print(f"Total price = {order_total}")

            case x if x < 150:
                print(f"Total value = {order_total + 10}")

            case _:
                print("Invalid order value")     

    case "Guest":

        match order_total:

            case x if x >= 200:
                print(f"Total price = {order_total}")
            
            case x if x < 200:
                 print(f"Total value = {order_total + 15}")
            
            case _:
                print("Invalid order value")   

    case _:
        print("Invalid Membership type")

#_____________________________________________________________________________________________________________________________

balance = int(input("Enter the balance value: "))
choice = int(input("""Enter the choice:
                      1 for check balance
                      2 for withdrawl
                      3 for deposit""": ))

match choice:

    case 1:
        print(f"Balance = {balance}")

    case 2:
        transaction = int(input("Enter the value:"))   

        match choice:

            case 2:
                print(f"Balance = {balance - transaction}")

    case 3:
        transaction = int(input("Enter the value:")) 

        match choice:

            case 3:
                print(f"Balance = {balance + transaction}")

    case _:
        print("Invalid choice")          





    
