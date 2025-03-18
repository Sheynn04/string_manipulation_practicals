# Objective: Create a program that ask the user to input their fullname in incorrect casing. Print each character of the input in reverse casing.

# 1. Ask the user to input their full name in incorrect casing.
fname = input("Input your name in incorrect casing: ")

# 2. Convert the input into it's reverse casing. 
# 3. Print the reverse casing full name. 
print(fname.swapcase())