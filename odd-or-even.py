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
# if integer is even
# then append to even.txt
# else append to odd.txt