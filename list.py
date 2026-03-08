'''
1.Create a list with 5 friends and ask user a friend name and add that name in the friend list, and print the list after that ask user to most important friend and add that friend at user choice
Ex: [1,2,3,4,5]
-> Enter anothe fiend: Raju
[1,2,3,4,5,"Raju"]
--> Most import friend: Billa
--> Please location for billa: 1
[1,"Billa",3,4,5,"Raju"]
'''

frined_list = ['A', 'B', 'C', 'D', 'E']
friend_name = input("Enter your friend name: ")
frined_list.append(friend_name)
print(frined_list)
most_imp_friend = input("Enter your most important friend: ")
priority = int(input("Enter the position at which you want to put your most important friend in the list: "))
frined_list.insert((priority-1), most_imp_friend)
print(frined_list)



'''
2. Create a list of 10 number and print the list
'''

li = [i for i in range(11)]
print(li)



'''
3. Create a list [1,10,100,3,6,8] and add 59 on 3 location after that append 5 and print list and length of list.

Find all of the words in a list of strings that are less than 4 letters. 

Given numbers = range(20), produce a list containing the word ‘even’ if a number in the numbers is even, and the word ‘odd’ if the number is odd. Result would look like ‘odd’,'even',........ 

Find all of the numbers from 1-1000 that are divisible by 7 

Count the number of spaces in a string 

Find the common numbers in two lists (without using a tuple or set) list_a = 1, 2, 3, 4, list_b = 2, 3, 4, 5
 '''
li1 = [1, 10, 100, 3, 6, 8]
li1.insert(2, 59)
li1.append(5)
print(li1)
print(len(li1))


li = ['li', 'fuhuvv', 'jsj', 'rfjfj']
less_than_4 = [word for word in li if len(word)<4]
print(less_than_4)


num_list = [i for i in range(21)]
pointer_num_list = ["even" if num %2 == 0 else "odd" for num in num_list]
pointer_num_list


div_by_7 = [num for num in range(1,1001) if num % 7 == 0 ]
print(div_by_7)


str1 = '   a   b   c   '
spaces = str1.count(" ")
print(spaces)


l1 = [1, 2, 3, 4]
l2 = [3, 4, 5, 6]

common = []
for num in l1:
    if num in l2 and num not in common:
        common.append(num)

print(common)
