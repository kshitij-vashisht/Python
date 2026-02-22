'''
Q1) Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return ‘not a valid string’ instead of the empty string
Sample string: - “Coder roots”
Expected result - “cots”
Sample string - “New year”
Expected result - “near”
'''

str1 = input("Enter a string: ")
if len(str1) < 2:
    print("Not a valid string.")
else:
    result = str1[:2] + str[-2:]
    print(result)



'''
Q2) Write a Python program to get a single string from two given strings, separated by a space and swap the first characters of each string
Sample String : 'coder', 'roots'
Expected Result : 'roder coots'
'''

str1 = input("Enter a string:")
str2 = input("Enter another string:")

new_str1 = str2[0] + str1[1:]
new_str2 = str1[0] +str2[1:]

print(new_str1)
print(new_str2)



'''
Q3) Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged
Sample String : 'abc'
Expected Result : 'abcing'
Sample String : 'string'
Expected Result : 'stringly'
'''

str1 = input("Enter a string:")
if len(str1) < 3:
    print(str1)
elif str1.endswith("ing"):
    print(str1 + "ly")
else:
    print(str1 + "ing")



'''
Q4) Write a Python program to remove the nth index character from a non-empty string
'''

str1 = input("Enter a string:")
index = int(input("Enter the index number:"))
if len(str1) > index:
    new_str = str1[0:index] + str1[index+1:]
    print(new_str)
else:
    print("Index number is not in range of string.")
