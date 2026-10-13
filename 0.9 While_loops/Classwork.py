# # 
# name = input("Enter your name: ").lower()
# sum = ""
# l = len(name)
# i = 1

# while i <= l:
#     x = l-i
#     sum = sum + name[x]
#     i += 1
# if name == sum:
#     print("Palindrome.")
# else:
#     print("Not a Palindrome.")    
#
# name = input("Enter your word: ")
# j = len(name)-1
# i = 0
# flag = True
# while i < j and flag:
#     if name[i] != name[j]:
#         i += 1
#         j -= 1
#         flag = False
#     else:
#         flag = True
#         break
# if flag == True:
#     print("Palindrome")
# else:
#     print("Not a Palindrome") 
# 
# number = 0

# while number >=0:
#     digit = number % 10
#     print(digit)
#     number = number//10
#     if number == 0:
#         digit = number
#         break    
i = 1

while i <= 3:

    j = 1

    while j <= 4:
        print("*", end=" ")
        j += 1

    print()
    i += 1    
