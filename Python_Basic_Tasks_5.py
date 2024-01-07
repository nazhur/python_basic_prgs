# 1. Write a Python program to convert temperatures to and from Celsius and Fahrenheit.
# [ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]
# Expected Output :
# 60°C is 140 in Fahrenheit
# 45°F is 7 in Celsius


## C = (F – 32)/1.8
## F = (C * 9/5) + 32

c=float(input('Enter the Fahrenheit:'))
f=float(input('Enter the celsius:'))

celsis = (c -32)/1.8
rounded_cel = round(celsis,2)
print("Fahrenheit to Celsius is: ", rounded_cel)

fahrenheit = (f * 1.8) + 32
rounded_fah = round(fahrenheit,2)
print("celsius to Fahrenheit is: ", rounded_fah)




# 2. Write a Python program that iterates the integers from 1 to 50. 
# For multiples of three print "Fizz" instead of the number and for multiples of five print "Buzz". 
# For numbers that are multiples of three and five, print "FizzBuzz".
# Sample Output :
# fizzbuzz
# 1
# 2
# fizz
# 4
# buzz


for i in range(1,51):
    if i %3 ==0 and i %5 ==0:
        print("FizzBizz")
        continue
    elif i %3==0:
        print("Fizz")
        continue
    elif i %5==0:
        print("Buzz")
        continue
    print(i)  



# 3. Write a Python program to find numbers between 100 and 400 (both included) 
# where each digit of a number is an even number. 
# The numbers obtained should be printed in a comma-separated sequence.

x=[]

for i in range(100,401):
    s=str(i)
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0):
        x.append(s)
print(", ".join(x))        







  
   
  
