# # QUESTION 1
# string = input("Enter the string: ")
# counta = 0
# countb = 0
# countc = 0
# countd = 0
# counte = 0

# for i in string:
#     if chr(65) <= i <= chr(90):
#         counta = counta + 1
#     elif chr(97) <= i <= chr(122):
#         countb = countb + 1
#     elif chr(48) <= i <= chr(57):
#         countc = countc + 1
#     elif chr(32) == i:
#         countd = countd + 1
#     else:
#         counte = counte + 1           
# if counta > countb and counta > countc and counta > countd and counta > counte:
#     print("Upper case letters have the highest count.")
# elif countb > counta and countb > countc and countb > countd and countb > counte:
#     print("lower case letters have the highest count.")
# elif countc > countb and countc > counta and countc > countd and countc > counte:
#     print("Digits have the highest count.")  
# elif countd > countb and countd > countc and countd > counta and countd > counte:
#     print("Space case letters have the highest count.")  
# elif counte > counta and counte > countc and counte > countb and counte > countd:
#     print("Special case letters have the highest count.")
# else:
#     print("Tie")    

# # QUESTUION 2
# count1 = 0
# count2 = 0
# count3 = 0
# count4 = 0


# for i in range(1,11):
#     marks = int(input(f"Enter the marks of Student{i}: "))
#     if 100 > marks > 75:
#         count1 = count1 +1 
#         print("Pass")
#     elif 74 >= marks >= 50:
#         count2 = count2 + 1
#         print("Pass")
#     elif 49 >= marks >= 35:
#         count3 = count3 + 1
#         print("Pass")    
#     else:
#         print("Fail")
#         count4 = count4 + 1   

# print(f"Excellent = {count1}")
# print(f" Good = {count2}")
# print(f"Pass = {count3}")
# print(f"Fail = {count4}")

      
#QUESTION 3
# sentence = input("Enter the sentence: ").lower()
# words = sentence.split()
# h_score = 0

# for i in words:
#     score = 0
#     for j in i:
#         if j == "aeiou":
#             score += 2
#         elif j == "bcdfghjklmnpqrstvwxyx":
#             score += 1
#         elif j == "0123456789":
#             score += 3
#         else:
#             score += 4
#     if score > h_score:
#         h_score = score
#         word = i
# print(word)                        


# QUESTION 4
# a = u = l = d = s = 0
# for i in range(1,6):
#     Password = input(f"Enter your password{i}:")
#     a = len(Password)
#     for j in Password:
#         if j == j.isupper():
#             u = 1
#         elif j == j.lower():
#             l = 1
#         elif j == j.isdigit():
#             d = 1      
#         else:
#             s = 1

#     count = 0
#     if a > 8:
#         count += 1
#     if u == 1:
#         count += 1
#     if l == 1:
#         count += 1  
#     if d == 1:
#         count += 1    
#     if s ==1:
#         count += 1
#     if count == 4:
#         print("Strong Password")
#     elif count >= 3:
#         print("Medium password")
#     else:
#         print("Weak")                 

# QUESTION 5
# sentence = input("Enter the sentence: ")
# a = sentence.split()

# for i in a:
#     length = len(i)
#     if length <= 3:
#         print("Short")
#     elif 4 <= length <=6:
#         print("Medium")
#     else:
#         print("Long")     


# QUESTION 6
# even = 0
# odd = 0

# for i in range(5):
#     number = input("Enter the number: ")
#     for j in number:
#         if int(j) % 2 == 0:
#             even = even + 1
#         else:
#             odd = odd + 1        
# if even > odd:
#     print(f"Even type is more than odd by {even-odd}, {even}.")    
# elif even == odd:
#     print("Both are equal.")
# else:
#     print(f"odd type is more than even by {odd-even}, {odd}.")       


# QUESTION 7
# string = input("Enter the string: ")

# printed = ""

# for i in string:
#     count = 0

#     for j in string:
#         if i == j:
#             count += 1

#     if count > 1 and i not in printed:
#         if count == 2:
#             print(i, "Duplicate")
#         elif 3 <= count <= 4:
#             print(i, "Repeated")
#         else:
#             print(i, "Highly Repeated")

#         printed += i

# QUESTION 8
# total = 0
# count1 = count2 = count3 = count4 = 0 
# for i in range(1,9):
#     Price = int(input(f"Enter the price of product{i}: "))
#     total = total + Price
#     if Price < 500:
#         count1 += 1
#     if 500 <= Price <= 1999:
#         count2 += 1
#     if 2000<= Price <= 4999:
#         count3 += 1
#     if Price >= 5000:
#         count4 += 1            
# print(f"Total amount:{total}")
# print(f"Number of products in Budget category: {count1}")
# print(f"Number of products in Regular category: {count2}")
# print(f"Number of products in Premium category: {count3}")
# print(f"Number of products in Luxury category: {count4}")

# QUESTION 9
# string = input("Enter your string: ")
# length = len(string)
# v = c = d = s = 0
# for i in range(0, length):
#     print(string[i])
#     print(f"Position = {i}.")
#     if i % 2 == 0:
#         print("Position is even.")
#     else:
#         print("Position is odd.")    
# for i in range(0, length):
#     if string[i] in "aeiouAEIOU":
#         v += 1
#     elif string[i] in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ":
#         c += 1
#     elif string[i] in "0123456789":
#         d += 1
#     else:
#         s += 1
# print(f"Number of vowels: {v}")       
# print(f"Number of consonants: {c}")
# print(f"Number of digits: {d}")
# print(f"Number of special characters: {s}")                


# QUESTION 10
# n = int(input("Enter the number: "))

# for i in range(1,n+1):
#     for j in range(1,2*i):
#         if j % 15 == 0:
#             print("Z", end =" ")  
#         elif j % 3 == 0:
#             print("X", end=" ")
#         elif j % 5 == 0:
#             print("Y", end=" ")
#         else:
#             print(j , end=" ") 
#     print()
        
# QUESTION 11
# cound = 0
# counu = 0
# couns = 0
# for i in range(1,6):
#     username = input(f"Enter the username{i}: ")
#     a = len(username)
#     b = username[0]
#     print(f"Length of username:{a}")
#     print(f"first character of username:{b}")
#     if chr(47) <= username <= chr(58):
#         if "_" in username:
#                 print("Valid")
#         else:
#             print("Need improvemnts.")
#     else:
#         print("Invalid")       

# QUESTION 12
# v = c = s = 0
# sentence = input("Enter the sentence: ").lower()
# print(f"Number of a: {sentence.count("a")}")
# print(f"Number of e: {sentence.count("e")}")
# print(f"Number of i: {sentence.count("i")}")
# print(f"Number of o: {sentence.count("o")}")
# print(f"Number of u: {sentence.count("u")}")

# for i in sentence:
#     if i in "aeiou":
#         v += 1
#     elif i in "bcdfghjklmnpqrstvwxyz":
#         c += 1
#     else:
#         s += 1
# if v > c:
#     print("Vowels win")
# elif v == c:
#     print("Draw")
# else:
#     print("Consonants win")                
            
# QUESTION 13
# for i in range(1,6):
#     Electricity_usage = int(input(f"Enter the unit{i}: "))
#     if Electricity_usage <= 100:
#         print(f"Bill = {Electricity_usage*5}")
#         print("Low")
#     if 100 < Electricity_usage <=200:
#         Bill = 500 + (Electricity_usage-100)*7
#         if Bill < 1000:
#             print(f"Bill = {Bill}")
#             print("Low")
#         else:
#             print(f"Bill = {Bill}")
#             print("Medium")    
#     if 200 < Electricity_usage <= 400:
#         Bill = 1200 + (Electricity_usage-200)*10
#         if Bill < 3000:
#             print(f"Bill = {Bill}")
#             print("Medium")
#         else:
#             print(f"Bill = {Bill}")
#             print("High")    
#     if 400 < Electricity_usage:
#         Bill = 3200 + (Electricity_usage-400)*15
#         print(f"Bill = {Bill}")
#         print("High")  


# QUESTION 14
# sentence = input("Enter the sentence: ").lower()
# words = sentence.split()
# v = c = 0
# for i in words:
#     for j in i:
#         if j in "aeiou":
#             v += 1
#         if j in "bcdfghjklmnpqrstvwxyz":
#             c += 1
#     if v > c :
#         print("Vowel Heavy")
#     elif v == c:
#         print("Balance")   
#     else:
#         print("Consonant Heavy")   

# QUSTION 15
# a = 1
# even = 0
# odd = 0

# for i in range(3):
#     for j in range(3):
#         print(a , end=" ")
#         if a % 2 == 0:
#             even += 1
#         else:
#             odd += 1      
#         a += 1
#     print()    
# print(f"Largest number is {a-1}")
# print(f"Even numbers : {even}")
# print(f"Odd numbers: {odd}")


# QUESTION 16
# u = l = d = s = 0

# password = input("Enter the password: ")
# for i in password:
#     if chr(65) <= i <= chr(90):
#         u += 1
#     elif chr(97) <= i <= chr(122):
#         l += 1
#     elif chr(48) <= i <= chr(57):
#         d += 1
#     else:
#         s += 1
# a = len(password)
# print(f"Percentage of uppercase letter: {(u*100)/a}")    
# print(f"Percentage of lowercase letter: {(l*100)/a}")   
# print(f"Percentage of digits : {(d*100)/a}")   
# print(f"Percentage of special characters: {(s*100)/a}")   

# if u > 1 and l > 1 and d > 1 and s > 1:
#     print("Strong password")
# elif u > 1  and l == 0 and d == 0 and s == 0:
#     print("Weak password")
# else:
#     print("Medium password")

# QUESTION 17
h_marks = 0
h_name = ""
for i in range(1,6):
    v = c = 0
    marks = int(input(f"Enter the marks of student{i}: "))
    name = (input(f"Enter the name of student{i}: ")).lower()
    if 75<= marks <= 100:
        print("Grade = A")
    elif 50 <= marks <= 74:
        print("Grade = B")   
    elif 35 <= marks <= 49:
        print("Grade = C")
    else:
        print("Fail")
    
    for j in name:
        if j in "aeiou":
            v += 1
        if j in "bcdfghjklmnpqrstvwxyz":
            c += 1
    print(f"Number of vowels : {v}")
    print(f"Number of vowels : {c}")
    print(f"NUmber of total characters:{len(name)}")
    if v > c:
        print("Number of vowels are greater")
    if c > v:
        print("Number of consonants are greater")
    if marks > h_marks:
        h_marks = marks
        h_name = name
print(h_name, "has highest marks")         

# QUESTION 18





