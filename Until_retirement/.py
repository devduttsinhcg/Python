# QUESTIOn 1
# n = int(input("Enter the number: "))
# factorial = 1

# for i in range(1, n+1):
#     factorial *= i

# print(factorial)   

#____________________________________________________________________________________________________________________

# QUESTIOn 2
# n = int(input("Enter the number: "))

# for i in range(1, n+1):
#     print(f"{7*i}", end=" ")

#____________________________________________________________________________________________________________________

# QUESTIOn 3
# n = (input("Enter the number: "))
# count = 0

# for i in n:
#     if i .isdigit():
#         count += 1

# print(count)

#____________________________________________________________________________________________________________________

# QUESTIOn 4
# n = int(input("Enter the number: "))
# sum = 0

# while n > 0:
#     digit = n % 10
#     sum = sum + digit
#     n = n // 10

# print(sum)    

#____________________________________________________________________________________________________________________

# QUESTIOn 5
# n = int(input("Enter the number: "))
# product = 1

# while n > 0:
#     digit = n % 10
#     product = product * digit
#     n = n // 10

# print(product) 

#____________________________________________________________________________________________________________________

# QUESTIOn 6
# n = int(input("Enter your number: "))
# sum = ""

# while n > 0:
#     digit = n % 10
#     sum = sum + str(digit)
#     n = n // 10

# print(sum)

#____________________________________________________________________________________________________________________

# QUESTIOn 7
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
#     print("not a Palindrome") 

#____________________________________________________________________________________________________________________

# QUESTIOn 8
# n = int(input("Enter your number: "))

# for i in range(2, n):
#     if n % i == 0:
#         print(f"{n} is not a prime number.")

# else:
#     print(f"{n} is a prime number.")

#____________________________________________________________________________________________________________________

# QUESTIOn 9
n = int(input("Enter n: "))

for i in range(2, n + 1):
    prime = True

    for j in range(2, i):
        if i % j == 0: 
            prime = False
            break

    if prime:
        print(i, end=" ")    

#____________________________________________________________________________________________________________________


                
                


    




