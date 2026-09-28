# Q1
i = 0

while i < 5:
    print("Hello")
    i = i + 1


# Q2
i = 0

while i < 10:
    print(i, end=" ")
    i = i + 1


# Q3
i = 1

while i <= 10:
    print(i)
    i = i + 1


# Q4
i = 10

while i > 0:
    print(i, end=" ")
    i = i - 1


# Q5
i = 5

while i <= 50:
    print(i, end=" ")
    i = i + 5


# Q6
i = 2

while i < 20:
    print(i)
    i = i + 2


# Q7
i = 1

while i < 20:
    print(i)
    i = i + 1


# Q8
i = 3

while i < 20:
    print(i, end=" ")
    i = i + 3


# Q9
i = 20

while i > 0:
    print(i, end=" ")
    i = i - 2


# Q10
n = int(input("Enter the number: "))

i = 1

while i <= n:
    print(i, end=" ")
    i = i + 1


# Q11
num = int(input("Enter the number: "))

i = 0

while i <= num:
    print(i, end=" ")
    i = i + 2


# Q12
num = int(input("Enter the number: "))

i = 1

while i <= num:
    print(i, end=" ")
    i = i + 2


# Q13
num = int(input("Enter the number: "))

i = 3

while i <= num:
    print(i, end=" ")
    i = i + 3


# Q14
num = int(input("Enter the number: "))

i = 6

while i <= num:
    print(i, end=" ")
    i = i + 6


# Q15
num = int(input("Enter the number: "))

count = 0
i = 0

while i <= num:
    if i % 2 == 0:
        count = count + 1

    i = i + 1

print(count)


# Q16
num = int(input("Enter the number: "))

count = 0
i = 0

while i <= num:
    count = count + i
    i = i + 1

print(count)


# Q17
num = int(input("Enter the number: "))

sum = 0
i = 0

while i <= num:
    if i % 2 == 0:
        sum = sum + i

    i = i + 1

print(sum)


# Q18
num = int(input("Enter the number: "))

sum = 0
i = 0

while i <= num:
    if i % 2 == 1:
        sum = sum + i

    i = i + 1

print(sum)


# Q19
num = int(input("Enter the number: "))

i = 1

while i <= 10:
    print(f" {num} x {i} = {num * i}")
    i = i + 1


# Q20
num = int(input("Enter the number: "))

count = 1
i = 1

while i <= num:
    count = count * i
    i = i + 1

print(count)


# Q21
string = input("Enter the string: ")

i = 0

while i < len(string):
    print(string[i])
    i = i + 1


# Q22
string = input("Enter the string: ")

i = 0

while i < len(string):
    print(string[i], end="")
    i = i + 1


# Q23
string = input("Enter the string: ")

count = 0
i = 0

while i < len(string):
    count = count + 1
    i = i + 1

print(count)


# Q24
string = input("Enter the string: ")

count = 0
i = 0

while i < len(string):
    if string[i] == "a":
        count = count + 1

    i = i + 1

print(count)


# Q25
string = input("Enter the string: ")

count = 0
i = 0

while i < len(string):
    if chr(65) <= string[i] and string[i] <= chr(90):
        count = count + 1

    i = i + 1

print(count)


# Q26
i = 0

while i < 3:

    j = 0

    while j < 4:
        print("*", end="")
        j = j + 1

    print()
    i = i + 1


# Q27
i = 0

while i < 4:

    j = 0

    while j < 5:
        print("*", end="")
        j = j + 1

    print()
    i = i + 1


# Q28
i = 0

while i < 5:

    j = 0

    while j <= i:
        print("*", end="")
        j = j + 1

    print()
    i = i + 1


# Q29
i = 1

while i <= 5:

    j = 1

    while j <= i:
        print(j, end="")
        j = j + 1

    print()
    i = i + 1


# Q30
i = 1

while i <= 10:

    j = 1

    while j <= 10:
        print(j * i, end=" ")
        j = j + 1

    print()
    i = i + 1