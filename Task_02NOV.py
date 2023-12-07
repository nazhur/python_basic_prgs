#1. Write a Python program to construct the following pattern, using a nested for loop.

# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *


n = int(input("Enter the number of rows to be printed: "))

for i in range(1, n+1):
    for j in range(i):
        print('*', end='')
    print()    

for i in range(n-1,0,-1):
    for j in range(i):
        print('*',end='')
    print()

# 2. Write a Python program that accepts a word from the user and reverses it.

x= input("Enter the string to reverse: ")

reverse_x = x[::-1] ##index slicing

print(reverse_x)


# method -2:

x= input("Enter the string to reverse: ")
rx = ''
for i in x:
    rx = i + rx
print("The reverse of given string is: ",rx)    




    
