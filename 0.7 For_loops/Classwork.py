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

num = int(input("Enter the number:"))

for i in range(num):
    for j in range(num, i, -1):
        print("*",end=" ")
    print()    
