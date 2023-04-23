# Write a Python program that reads a text file named numbers.txt that contains 20 integers. 
# The program will create two other text file; the first text file will be named even.txt 
# that will contains all even numbers extracted from the numbers.txt. The second text file 
# will be named odd.txt that will contains all odd numbers extracted from the numbers.txt.

read_numbers = open("numbers.txt", "r")
add_even = open('even.txt', 'a')
add_odd = open('odd.txt', 'a')
for integer in read_numbers:
    if int(integer) % 2 == 0:
        add_even.write(integer)
    else:
        add_odd.write(integer)
read_numbers.close()
add_even.close()
add_odd.close()