# Write a Python program that reads a text file named numbers.txt that contains 20 integers. 
# The program will create two other text file; the first text file will be named even.txt 
# that will contains all even numbers extracted from the numbers.txt. The second text file 
# will be named odd.txt that will contains all odd numbers extracted from the numbers.txt.

# variable for reading file
read_numbers = open('numbers.txt')
# create new file for odd and even integers
add_even = open('even.txt', 'a')
add_odd = open('odd.txt', 'a')
# for loop
for integer in read_numbers:
# if integer is even
    if integer % 2 == 0:
# then append to even.txt
        add_even.write(integer)
# else append to odd.txt
    else:
        add_odd.write(integer)