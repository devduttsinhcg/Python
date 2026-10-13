# QUESTION 1

#for i in range(1, 8):
#   if i == 5:
#       break
#   print(i)
#print("Finished")

#---------------------------------------------------------------------Answer = 1 2 3 4 Finished

# ______________________________________________________________________________________________________________________________________________________

# QUESTION 2

#word = "skyline"
#for ch in word:
#    if ch in "aeiou":
#        break
#    print(ch)

#---------------------------------------------------------------------Answer = s k y l

# ______________________________________________________________________________________________________________________________________________________

# QUESTION 3

#n = 2
#while n <= 10:
#    print(n)
#    if n == 6:
#        break
#    n += 2

#---------------------------------------------------------------------Answer = 2 4 6

# ______________________________________________________________________________________________________________________________________________________

# QUESTION 4

limit = int(input("Enter the limit: "))

for i in range(1, limit + 1):
    if limit > 7:
        print(i)
        if i == 7:
            break
    if limit < 7:
        print(i)

# ______________________________________________________________________________________________________________________________________________________

# QUESTION 5

string = input("Enter the string: ")
target = "s"

for i in string:
    print(i)
    if i == target:
            break
else:
    print("Target not found")

# ______________________________________________________________________________________________________________________________________________________

# QUESTION 6

num = [1, 2, 78, 21, -7, -5, 89]

for i in num:
    if i < 0:
        break
    print(i)

# ______________________________________________________________________________________________________________________________________________________

# QUESTION 7

# for row in range(1, 4):
#     for col in range(1, 5):
#         if col == 3:
#             break
#         print(row, col)

#---------------------------------------------------------------------Answer = (1,1) (1, 2) (2, 1) (2, 2) (3, 1) (3, 2)
# Cause break only exits the ineer loop and not outer loop in this case if col = 3 theen inner loop break and not output is shown but the iteration of outerloop still continue.

# ______________________________________________________________________________________________________________________________________________________

# QUESTION 8

sentence = input("Enter the sentence: ")
targeted_word = "Hello"

list = sentence.split()

for i in list:
    if i == targeted_word:
        print("Found")
        break
else:
    print("Not found")    

# ______________________________________________________________________________________________________________________________________________________

# QUESTION 9

# for i in range(1, 7):
#     if i == 4:
#         continue
#     print(i)

#---------------------------------------------------------------------Answer = 1 2 3 5 6

# ______________________________________________________________________________________________________________________________________________________

# QUESTION 10

# for ch in "education":
#     if ch in "aeiou":
#         continue
#     print(ch, end="")

#---------------------------------------------------------------------Answer = dctn

# ______________________________________________________________________________________________________________________________________________________

# QUESTION 11

# n = 0

# while n < 5:
#     n += 1
#     if n == 3:
#         continue
#     print(n)

#---------------------------------------------------------------------Answer  = 1 2 4

# ______________________________________________________________________________________________________________________________________________________

# QUESTION 12

n = int(input("Enter the number: "))

for i in range(1, n+1):
    if i % 3 == 0:
        continue
    
    print(i)
    
# ______________________________________________________________________________________________________________________________________________________

# QUESTION 13

string = input("Enter the string: ")
targeted_character = "h"

for i in string:
    if i == targeted_character:
        continue
    print(i, end="")

# ______________________________________________________________________________________________________________________________________________________

# QUESTION 14

# marks = [25, 40, 75, 32, 90, 40, 75, 90, 10, 20, 30]

# for i in marks:
#     if marks < 40:
#         continue
#     print(i, end=" ")

# ______________________________________________________________________________________________________________________________________________________

# QUESTION 15

# for i in range(1, 5):
#     if i == 2:
#         continue
#     print("A", i)
#     print("B", i)

# -------------------------------------------------------Anser = (A, 1) (B, 1) / (A, 3) (B, 3) / (A, 4) (B, 4)
# ______________________________________________________________________________________________________________________________________________________

# QUESTION 16

n = 0

while n < 5:
    if n == 3:
        n += 1
        continue
    n += 1
    print(n)

# ______________________________________________________________________________________________________________________________________________________

# QUESTION 17

word = input("Enter the word: ").lower()
count = 0
for i in word:
    if i == "a" or i == "e" or i == "o" or i == "u":
        continue
    count += 1
print(count)    

# ______________________________________________________________________________________________________________________________________________________

# QUESTION 18

# for i in range(1, 4):
#     print(i)
# else:
#     print("Done")

# ----------------------------------------------------------------Answer = 1 2 3 4 Done

# ______________________________________________________________________________________________________________________________________________________

# Question 19

# for i in range(1, 5):
#     if i == 2:
#         continue
#     print(i)
# else:
#     print("Completed")

# --------------------------------------------------------------Answer = 1 3 4 Completed

# ______________________________________________________________________________________________________________________________________________________

# Question 20

# for i in range(1, 5):
#     if i == 3:
#         break
#     print(i)
# else:
#     print("Completed")
# print("Outside loop")

# --------------------------------------------------------------Answer = 1 2 Outside loop

# ______________________________________________________________________________________________________________________________________________________

# QUESTION 21

# for item in []:
#     print("Inside")
# else:
#     print("Else block")

# ------------------------------------------------------------Answer = Else block 

# ______________________________________________________________________________________________________________________________________________________

# QUESTION 22

list = [10, 34, 56, 39 ,90]
target = 10
for i in list:
    if i == target:
        print("found")
        break
else:
    print("Not Found")  

# ______________________________________________________________________________________________________________________________________________________

# QUESTION 23

string = input("Enter the string: ")
target = "s"

for i in string:
    if i == target:
            print("Character exists")
            break
else:
    print("Character Missing")

# ______________________________________________________________________________________________________________________________________________________

# QUESTION 24

number = int(input("Enter your number: "))

for i in range(2, number):
    if number % i == 0 :
        print(f"{number} is not a prime number.")
        break
else:
    print(f"{number} is a prime number.")   

# ______________________________________________________________________________________________________________________________________________________

# QUESTION 25

# values = [2, 4, 6, 8]

# for value in values:
#     if value % 2 != 0:
#         print("Odd found")
#         break
# else:
#     print("All are even")

# -------------------------------------------------Answer = All are even    

# ______________________________________________________________________________________________________________________________________________________

# QUESTION 26

# Case A

# for x in range(3):
#     continue
# else:
#     print("A")

# ------------------------------------------------------Yes else block will run cause loop doesn't break and iterates fully.

# CAse B

# for x in range(3):
#     break
# else:
#     print("B")

#------------------------------------------------------No else block will not run cause loop breaks here

# Case C

# for x in range(0):
#     print(x)
# else:
#     print("C")

#-------------------------------------------------------YEs it will stilll run cause loop is not terminated.

#_______________________________________________________________________________________________________________________________

# QUESTION 27

string = input("Enter the string: ")
character = ""

for i in string:
    if i in character:
        print("Found")
        break
    character += i

else:
    print("No repeated character")

#_______________________________________________________________________________________________________________________________

# QUESTION 28

# for i in range(1, 4):
#     if i == 2:
#         pass
#     print(i)

#---------------------------------------------Answer = 1 2 3

#_______________________________________________________________________________________________________________________________

# Question 29

# x = 10

# if x > 5:
#     pass

# print("Finished")

#-----------------------------------------------Answer = Finished

#_______________________________________________________________________________________________________________________________

# Question 30

# for letter in "cat":
#     pass

# print("Loop ended")

#-----------------------------------------------Answer = Loop ended

#_______________________________________________________________________________________________________________________________

# QUESTION 31

for i in range(1, 6):
    if i % 2 == 0:
        pass
    print(i)

#_______________________________________________________________________________________________________________________________

# QUESTION 32

choice = input("Enter your choice (1, 2, or 9): ")

if choice == "1":
    print("Hello")
elif choice == "2":
    pass
else:
    print("Invalid choice")

print("Program closed")

#_______________________________________________________________________________________________________________________________

# QUESTION 33

# Program A

# for i in range(1, 5):
#     if i == 3:
#         pass
#     print(i)

#------------------------------------------------------------------Answer = 1 2 3 4

# Program B

# for i in range(1, 5):
#     if i == 3:
#         continue
#     print(i)

#------------------------------------------------------------------Answer = 1 2 4

#_______________________________________________________________________________________________________________________________

# QUESTION 34

for i in range(1, 6):
    if i == 3:
        continue
    print(i)

#_______________________________________________________________________________________________________________________________

# QUESTION 35

# for i in range(1, 6):
#     if i == 2:
#         continue
#     if i == 4:
#         break
#     print(i)
# else:
#     print("Finished")

#--------------------------------------------------------Answer = Else will not work cause loop is broken or terminated when i = 4. 

#_______________________________________________________________________________________________________________________________

# QUESTION 36

Number_list = [-2, 4, 7, 9, -5, -1, 3, 6 ]
target = 8

for i in Number_list:
    if i < 0:
        continue
    if i == target:
        print(i)
        print("Target found")
        break
else:
    print("Target not found")    

#_______________________________________________________________________________________________________________________________

# QUESTION 37

Numberlist = [-2, 4, 7, 9, -5, -1, 3, 6 ]

for i in Numberlist:
    if i == 0:
        continue
    if i == -1:
        break
else:
    print("All values are processed")

#_______________________________________________________________________________________________________________________________

# QUESTION 38

for row in range(1, 4):
    for col in range(1, 4):
        if col == 2:
            continue
        if row == 3:
            break
        print(row, col)
    else:
        print("Inner loop completed")

#--------------------------------------------------Answer = (1,1)(1,3) Inner loop completed / (2,1)(2,3) inner loop completed

#_______________________________________________________________________________________________________________________________

# QUESTION 39

Numberlist = [-2, 4, 7, 9, -5, -1, 3, 6, 12 ]

for i in Numberlist:
    if i < 0:
        continue
    if i % 4 == 0 and i % 6 == 0:
        print(f"Found {i}")
else:
    print("No matching number")

#_______________________________________________________________________________________________________________________________

# QUESTION 40

# Stop searching immediately after finding a username. ==> Break
# Skip a blank string and process the remaining strings. ==> continue
# Display "Not found" only when a search loop finishes without finding a match. ==> for-else
# Keep an unfinished function syntactically valid while its implementation is planned. ==> pass
# Skip the current number but keep processing later numbers. ==> Continue
# Stop a loop when a user enters a sentinel value. ==> Break
# Report that all items were checked, provided no match caused an early stop.==> for-else
# Temporarily leave a conditional block empty without causing a syntax error. ==> Pass

#_______________________________________________________________________________________________________________________________




    

