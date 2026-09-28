

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
# ch = input("Enter a character: ")

# if 'A' <= ch <= 'Z':
#     print("Uppercase")

# elif 'a' <= ch <= 'z':
#     print("Lowercase")

# elif '0' <= ch <= '9':
#     print("Digit")

# else:
#     print("Special")

# a="hello "
# print(a*10)

# number = int(input("Enter your number: "))

# for i in range(2, number):
#         if number % i == 0:
#             print(f"{number} is not a prime number.")
# else:
#     print(f"{number} is a prime number.")    

# #
# name = input("Enter your name: ")
# length = len(name)
# sum = ""

# for i in range (length-1, -1, -1):
#     sum = sum + name[1]

# if name == sum:
#     print(f" {name} is a palindrome.")
# else:
#     print(f"{name} is not a palindrome.")    

# 
# name = input("Enter your name: ").strip().lower()
# length = len(name)

# for i in range (length-1, -1, -1):
#     a = (name[i])
#     b = print(a ,sep="", end="") 

# for row in range(3):
#     for column in range(4):
#         print("*", end="")
    
# for row in range(3):
#     for column in range(4):
#         print("*", end="")
#         print()
# x = 10

# if x > 5:
#     print("A")
# if x > 8:
#     print("B")
# else:
#     print("C")
# for i in range(5):
#     print(i)

# print(i)
# ch = input("Enter character: ")

# if ch == "a" or "e" or "i" or "u" :
#     print("vowel")

# word ="banana"
# count=0

# for i in word:
#     if i =="a":
#         count = count + 1
#     print(count)    
# for i in range(3):
#     print(i)
#     print(i + 10)

# word = "hello"

# for i in range(len(word)):
#     if word[i] == "l":
#         print(word[i])

# word = "computer"

# for i in range(len(word)):
#     if word[i] == "o":
#         print("Found")

# word = "Python"

# for i in range(len(word)):
#     print(word[i])

# text = "Hello123"

# count = 0

# for i in range(len(text)):
#     ch = text[i]

#     if ord(ch) >= 48 and ord(ch) <= 57:
#         count = count + 1

# print(count)
# num = int(input("Enter your number:"))

# factorial = 1
# for i in range(1,num+1):
#     factorial = factorial * i
# print(factorial)    
     
# year = int(input("Enter the year:"))

# if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
#     print("Leap year")

# total = 0

# for i in range(5):
#     marks = int(input("Enter your marks: "))
#     total = total + marks
#     if marks < 35:
#         print("Failed")
#         break
# percentage = (total/5)

# if percentage <= 100 and percentage >= 90:
#     print(f"total = {total}, percentage = {percentage}, grade = A")
# elif percentage <= 89 and percentage >= 80:
#     print(f"total = {total}, percentage = {percentage}, grade = B")
# elif percentage <= 79 and percentage >= 70:
#     print(f"total = {total}, percentage = {percentage}, grade = C")
# elif percentage <= 69 and percentage >= 60:
#     print(f"total = {total}, percentage = {percentage}, grade = D")
# elif percentage <= 59 and percentage >= 50:
#     print(f"total = {total}, percentage = {percentage}, grade = E")    
# elif percentage <= 49 and percentage >= 35:
#     print(f"total = {total}, percentage = {percentage}, grade = F")
  
# import turtle, colorsys, math
# t = turtle.Turtle()
# turtle.bgcolor("black")
# turtle.tracer(0)
# t.speed(0)
# h, a = 0, 0
# def draw():
#     global h,a
#     t.clear()
#     for i in range(120):
#         c = colorsys.hsv_to_rgb(h, 2, 2)
#         t.color(c)
#         t.penup()
#         t.goto(0, 0)
#         t.pendown()
#         x = math.sin(a + i) * 200
#         y = math.cos(a + i * 2) * 200
#         t.goto(x, y)
#         t.dot(15)
#         h += 0.0001
#     turtle.update()
#     a += 0.05
#     turtle.ontimer(draw, 10)
# draw()
# turtle.done    
# for i in range(1,6):
#     for j in range(1,6):
#         print(f"{j *j}", end=" ")
#     print()    
  
# for i in range(5):
#     for j in range(i+1):
#         print(chr(65+j), end=" ")
#     print()

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(2*j, end=" ")
#     print()    
# for i in range(5):
#     for j in range(1,6):
#         print(j , end=" ")
#     print()
# num = 1
# for i in range(3):
#     for j in range(3):
#         print(num, end=" ")
#         num += 1
#     print()    
# for i in range(1,4):
#     for j in range(1,4):
#         print(f"{(i,j)}", end="")
#     print()    
# for i in range(1,4):
#     for j in range(1,4):
#         print(i, j)
# for i in range(5):
#     for j in range(1,6-i):
#         print(j,end="")
#     print()
for i in range(5):
    for j in range(5-i,0, -1):
        print(j,end="")
#     print()
# for i in range(1,6):
#     for j in print()

for i in range(5):
    for k in range(4-i):
        print(" ", end=" ")
    for l in range(0,i+1):
        if (i == 2 and l == 1) or (i == 3 and (l == 1 or l == 2)):
            print("   ", end=" ")
        elif i == 4:
            print("* *",end=" ")    
        else:    
            print("*  ", end=" ")
    print()
            