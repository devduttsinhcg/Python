#Q1
for i in range(5):
    print("Hello")

#Q2
for i in range(10):
    print(i, end=" ")

#Q3    
for i in range(1, 11):
    print(i)

#Q4    
for i in range(10,0,-1):
    print(i,  end=" ")

#Q5
for i in range(5, 51, 5):
    print(i,  end=" ")

#Q6
for i in range(2,20,2):
    print(i)
# Q7
for i in range(1,20):
    print(i)

# Q8
for i in range(3,20,3):
    print(i, end=" ")  

# Q9
for i in range(20,0,-2):
    print(i, end=" ")    
    
# Q10
n = int(input("Enter the number: "))
for i in range(1,n+1):
    print(i , end=" ")     

# Q11
num = int(input("Enter the number: "))

for i in range(0,num+1, 2):
    print(i, end=" ")

# Q12
num = int(input("Enter the number: "))

for i in range(1,num+1, 2):
    print(i, end=" ")

# Q13
num = int(input("Enter the number: "))

for i in range(3,num+1, 3):
    print(i, end=" ")

# Q14
num = int(input("Enter the number: "))

for i in range(6,num+1, 6):
    print(i, end=" ")    

# Q15
num = int(input("Enter the number: "))
count = 0

for i in range(num+1):
    if i % 2 == 0:
        count = count + 1
print(count) 

# Q16
num = int(input("Enter the number: "))
count = 0

for i in range(num+1):
    count = count + i
print(count)    

# Q17
num  = int(input("Enter the number: "))
sum = 0

for w in range(num+1):
    if w % 2 == 0:
        sum = sum + w
print(sum)        
 
# Q18
num  = int(input("Enter the number: "))
sum = 0

for w in range(num+1):
    if w % 2 == 1:
        sum = sum + w
print(sum)  

# Q19
num  = int(input("Enter the number: "))

for i in range(1,11):
    print(f" {num} x {i} = {num*i}")

# Q20    
num  = int(input("Enter the number: "))
count = 1

for i in range(1,num+1):
    count = count * i
print(count)    

# Q21
string = input("Enter the string: ")
 
for i in string:
    print(i)

# Q22
string = input("Enter the string: ")
 
for i in string:
    print(i,end="") 

# Q23
string = input("Enter the string: ")
count = 0 

for i in string:
    count = count + 1
print(count)    

# Q24
string = input("Enter the string: ")
count = 0
 
for i in string:
    if i == "a":
        count = count + 1
print(count)        

# Q25
string = input("Enter the string: ")
count = 0

for i in string:

    if chr(65)<= i and i <= chr(90):
        count = count + 1
print(count)  

# Q26
for i in range (3):
    for j in range(4):
        print("*", end="")
    print()
# Q27
for i in range (4):
    for j in range(5):
        print("*", end="")
    print()
    
# Q28
for i in range(5):
    for j in range(0,i+1):
        print("*" , end="")
    print() 

# Q29
for i in range(1,6):
    for j in range(1,i+1):
        print(j, end="")
    print()

# Q30
for i in range(1,11):
    for j in range(1,11):
        print(f"{j * i}",end=" ")
    print()    