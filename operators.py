# Operators questions...

'''Q1) Write a python program that takes in a student name, class, and section. It should also take in five subject marks of the students and find the total marks and percentage. Display a result in such a way that their name, class, and percentageare printed.
'''
name = input("\nEnter student name :")
standard = int(input("\nEnter student class :"))
section = input("\nEnter student section :")

subjects_score = []
for score in range(1, 6, 1):
  sub_score = int(input(f'\nEnter score of subject {score} :'))
  subjects_score.append(sub_score)

# print(subjects_score)

total_marks = 500

obtained_marks = sum(subjects_score)
print(f'\nMarks obtained by the student {obtained_marks}.\n')


# print(type(obtained_marks))


percentile = (obtained_marks/ total_marks) * 100
print(f'Percentage of {name} of {standard} is {percentile}%.\n')

if percentile >= 90:
  print("Great!, Keep it up...")
elif percentile >=70:
  print("Doing good.")
else:
  print("Work harder!")



''' Q2) Input three numbers and return sum of them. '''
three_num = []

for num in range(3):
  numbers = int(input(f"Enter number {num+1}: "))
  three_num.append(numbers)

sum_of_nums = sum(three_num)
print(f'Sum of threee numbers is {sum_of_nums}.')



''' Q3) Input a number and square of it. '''
num = int(input("Enter a number to square :"))
print(f'Square of the {num} is {num ** 2}.')



''' Q4) Write a program which takes the temperature in celcius as I/p in str format, convert it into float, and calculate the equivalent temperature in fahrenheit.'''
ip_temp = input("Enter the tempersture in celcius: ")

conv_type = float(ip_temp)

conv_temp = (conv_type * 9/5) + 32

print(f'The {ip_temp} degree Celcius is equal to {conv_temp} degree Fahrenheit.')



''' Q5) Write a program to calculate the remainder when a number is divided by another number. '''
num_1 = int(input("Enter first number or numenator: "))
num_2 = int(input("Enter second number or denominator: "))

if num_2 == 0:
  print("Denominator can't be zero.")
else:
  quotient = num_1//num_2
  remainder = num_1 % num_2
  print(f'The quotient for {num_1} divided by {num_2} is {quotient}.')
  print(f'The remainder for {num_1} divided by {num_2} is {remainder}.')



''' Q6) Write a program to calculate simple interest. '''
principal = int(input("Enter principal value: "))
rate = int(input("Enter rate percentage: "))
time = int(input("Enter time period: "))

Simple_int = (principal * rate * time) / 100

print(f'Simple interest is {Simple_int}.')

