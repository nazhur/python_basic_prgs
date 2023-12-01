## TASK-3

## 1. Write a Python program to remove characters that have odd index values in a given string.

x= 'HELLO, WORLD!'

output = ''

for i in range(len(x)):
    if i % 2 ==0:
        output = output + x[i]

print('The even characters are:', output)


