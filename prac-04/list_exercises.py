numbers = []

for i in range(5):
    x = int(input("Number: "))
    numbers.append(x)

print("The first number is", numbers[0])
print("The last number is", numbers[4])
print("The smallest number is", min(numbers))
print("The largest number is", max(numbers))
print("The average of the numbers is", sum(numbers) / 5)

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

username = input("Enter the username: ")
flag =0

for i in usernames:
    if i==username:
        flag=1
        break

if flag==1:
    print("Access granted")
else:
    print("Access denied")