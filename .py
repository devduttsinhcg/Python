

# b=232
# c=232%10
# d=23%10
# e=2%10
# print(c+d+e)

# number=int(input("Enter the number:"))
# f=(number%10)
# g=(number//10)
# h=(g//10)
# i=(g%10)
# print(f+h+i)

#
# x = int(input("Enter fist number: "))
# y = int(input("Enter second number: "))
# z = int(input("Enter third number: "))

# if x > y > z:
#     print(f"{y} is the middle number")
# if z > y > x:
#     print(f"{y} is the middle number")    
# if z > x > y:
#     print(f"{x} is the middle number")    
# if y > x > z:
#     print(f"{x} is the middle number")    
# if x > z > y:
#     print(f"{z} is the middle number")    
# if y > z > x:
#     print(f"{z} is the middle number")    

#
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
ch = input("Enter a character: ")

if 'A' <= ch <= 'Z':
    print("Uppercase")

elif 'a' <= ch <= 'z':
    print("Lowercase")

elif '0' <= ch <= '9':
    print("Digit")

else:
    print("Special character")