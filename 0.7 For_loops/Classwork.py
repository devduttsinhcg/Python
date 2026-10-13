# number = int(input("Enter your number: "))

# for i in range(0, number + 1):
#     if i % 2 == 0:
#         print(i)

# number = int(input("Enter the number: "))
# for i in range(1, (number*10)+1):
#     if i % number == 0:
#         print(i)        

# number = int(input("Enter your number:"))
# for i in range(1, ):
#     print(number*i)
#else

#
# name = "python"

# for i in name:
#     print(i, sep="", end="-")
           

# for k in range(4):
#     print("*"*4)    

# num = int(input("Enter the number:"))
# for i in range(1,num):
#     for j in range(1,i +1):
#         print("*", end="")
#     print()

# for i in range(4):
#     for j in range(4):
#         print("*"*4)    

# num = int(input("Enter the number:"))

# for i in range(num):
#     for j in range(num, i, -1):
#         print("*",end=" ")
#     print()    

# for i in range(5):
#     for j in range(4-i):
#         print(" ",end=" ")
#     for k in range(i+1):
#         print("*", end=" ")
#     print()    

# for i in range(1,6):
#     for j in range(1,i):
#         print(" ", end=" ")
#     for k in range(1,7-i):
#         print("*", end=" ")    
#     print()    

# for i in range(6):
#     for j in range(5-i):
#         print(" ",end=" ")
#     for k in range(2*i+1):
#         print("*",end=" ")
#     print()    

# for i in range(1,11,2):
#     print(" ",end="")
#     for j in range(i):
#         print("*",end="")    
#     print()
# for i in range(5):
#     for j in range(4-i):
#         print(" ",end=" ")
#     for j in range(i):
#         print("*", end="")
#     print() 
# num = int(input("Enter the number: "))   
# for i in range(1,num+1):
#         for j in range(1,num+1):
#             if j == 1 or j == num or i == num:
#                 print("*", end=" ")
#             elif (i == (num//2 +1) and j == (num//2+1)):
#                  print("*", end=" ")    
#             else:
#                 print(" ", end=" ")    
#         print()

#________________________________________________METHOD 1______________________________________________________

str = input("Enter the string: ")
flag = True
count = 0

for i in str:
    if i == "O" and count < 1:
        flag = False
        print("Found")
        count += 1
if flag:
    print("Not found")        

#________________________________________________METHOD 2______________________________________________________

str = input("Enter the string: ")
flag = False

for i in str:
    if i == "O" and flag == False:
        flag = True
        print("Found")

if not flag:
    print("Not found")


for i in range(3):
    for j in range(3):
        break
    print(i,j)
