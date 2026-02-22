# of_else & loop questions


'''
Q1) Ask user to input a number and then month name corresponding to that number.
'''
num = int(input("Enter month number: "))

if num == 1:
    print(f"{num} is for January.")
elif num == 2:
    print(f"{num} is for Feburary.")
elif num == 3:
    print(f"{num} is for March.")
elif num == 4:
    print(f"{num} is for April.")
elif num == 5:
    print(f"{num} is for May.")
elif num == 6:
    print(f"{num} is for June.")
elif num == 7:
    print(f"{num} is for July.")
elif num == 8:
    print(f"{num} is for August.")
elif num == 9:
    print(f"{num} is for September.")
elif num == 10:
    print(f"{num} is for October.")
elif num == 11:
    print(f"{num} is for November.")
elif num == 12:
    print(f"{num} is for December.")
else:
    print("Number of months are upto 12 only... Don't sound dumb...")



'''
Q2) Ask user to input 2 number
Tell the followings-
1. Both number are equal or not.
2. Which is Bigger in both.
3. Either First NUmber is smaller or equal to Second Number.
4. Print your first name 5 times if first number is greather than second and print your surname 3 times if 1st no is less than second.
'''

#1.
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 == num2:
    print(f'{num1} = {num2}, i.e. both numbers are equal.')
else:
    print(f'{num1} is not equal to {num2}, i.e. both numbers not equal.')

#2.
if num1 > num2:
    print(f"{num1} is greater than {num2}.")
elif num1 < num2:
    print(f"{num1} is less to {num2}.")
else:
    print("Both numbers are equal.")

#3.
if num1 < num2:
    print(f"{num1} is smaller than {num2}.")
elif num1 == num2:
    print(f"{num1} is equal to {num2}.")
else:
    print(f"{num1} is less to {num2}.")

#4.
first_name = "kshitij"
last_name = "vashisht"

if num1 > num2:
    print(first_name*5)
elif num1 == num2:
    print("Numbers are equal...")
else:
    print(last_name*3)



'''
Q3) Using User input ask user to input 2 string and tell followings
    1. using == tell both string equal or not
    2. using is operator tell both equal or not
'''

str1 = input("Enter first statement:")
str2 = input("Enter second statement:")
# 1.
if str1 == str2:
    print("both statements are same.")
else:
    print("both statements are different.")

# 2.
if str1 is str2:
    print("both statements are same.")
else:
    print("both statements are different.")



'''
Q4) Ask user to input 2 string and convert it into numbers and using is op tell both are equal or not
'''
str1 = input("Enter first number:")
str2 = input("Enter second number:")

num1, num2 = int(str1), int(str2)
if str1 is num1 and str2 is num2:
    print("Types of both are same.")
else:
    print("Types of both are different.")



'''
Q5) Python program to calculate the sum of all numbers from 1 to a given number.
'''

num = int(input("Enter a number:"))
sum = 0
for i in range(1, num+1):
    sum = sum + i

print(f'The sum of first {num} numbers is {sum}.')



'''
Q6) Ask user to input a number and tell all even number upto that number
 Eg: 
 input a num:29 
 Even are: 2,4,6,... 28
'''
even_upto = int(input("Enter a number:")) 
for i in range(even_upto+1):      # using for loop
    if i % 2 == 0:
        print(i, end = ", ")
# OR
num = int(input("Enter a number:"))
even = 0
while even <= num:                # using while loop
  if even % 2 == 0:
    print(even, end = ",")
  even = even + 1



'''
Q7)Ask User to input a Number and with + or - and perform followings Output
    Enter a no: 567
    Enter OP(+,-): +
    0,1,2,3.......566
    if -
    567...>..... 1
'''
num = int(input("Enter a number:"))
op = input("Enter an operator +/-:")
if op == "+":
    for accend in range(0, num+1):
        print(accend, end= ", ")
elif op == "-":
    for decend in range(num, 0, -1):
        print(decend, end = ", ")
else:
    print("Invalid Operator.")
