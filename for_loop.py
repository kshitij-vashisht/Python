# For loop questions
'''
 Q1) Write a program to find the sum of first n natural numbers(n is integer input from user)
'''

n = int(input("Enter any natural number: "))
sum = 0
for i in range(1, n+1):
    sum = sum + i

print(f'Sum of first {n} natural numbers: {sum}.')



'''
Q2) Print the multiplication table of a given number using a for loop
    output - 2*2=4
'''

num = int(input("Enter table number: "))
for i in range(11):
    result = num * i
    print(f'{num} * {i} = {result}')



'''
Q3) write a program to check whether a given number is prime or not.
'''
num = int(input("Enter a number:"))
for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
        print(f'{num} is a Composite number.')
        break
else:
    print(f'{num} is a prime number.')    

# OR

num = int(input("Enter a number:"))
for i in range(2,num):
    if num % i == 0:
        print(f'{num} is not a prime number.')
        break
else:
    print(f'{num} is a prime number.')


'''
Q4) Check whether a number is a palindrome.       Ex- 1221
'''
value = input("Enter number:")
if value == value[::-1]:
    print(f'{value} is a palindrome.')
else:
    print(f'{value} is not a palindrome.')


# OR

line = input("Enter something:")

for i in line:
    if line == line[::-1]:
        print(f'{line} is a palindrome.')
        break
else:
    print(f'{line} is not a palindrome.')

    


'''
Q5) Print numbers from 1 to 100:
    If divisible by 5 → print Buzz
    If divisible by 3 → print Fizz
    If divisible by both → print FizzBuzz
'''

for i in range(101):
    if i % 5 == 0:
        print(i, "Buzz")
    elif   i % 5 == 0 and i % 3 == 0:
        print(i, 'FizzBuzz')
    elif i % 3 == 0:
        print(i, 'Fizz')
    else:
        print(i, "Neither divisible by 3 or 5")
