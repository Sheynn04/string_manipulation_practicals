# Objective: Create a program that ask the user to input a number (0-1000). Print the number in 6 digit format. Add zeros at the beginning to complete the 6 digit.

# 1. Ask the user to input a number from 0-1000.
number = input('Enter a number from 0 - 1000: ')

# 2. Add zeros to the beginning of the input to turn it into 6 digit format.
# 3. Print the 6 digit format the previous input.
print(number.zfill(6))