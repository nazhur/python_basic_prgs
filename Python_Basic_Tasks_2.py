## TASK-4 30 OCT


## 1.Write a Python program to count the number of even and odd numbers in a series of numbers?

x= [1,2,3,4,5,6,7,8,9]

even_count = 0
odd_count = 0

for i in x:
    if i % 2 == 0:
        even_count = even_count + 1
    else:
        odd_count = odd_count + 1

print("The count of even number is: ",even_count)        
print("The count of odd number is: ",odd_count)


## 2.Write a Python program to find those numbers which are divisible by 7 and multiples of 5,
## between 1500 and 2700 (both included).


numb = []

for i in range(1500, 2701):
    if i % 5 == 0 and i % 7 ==0:        
        print(i)        
