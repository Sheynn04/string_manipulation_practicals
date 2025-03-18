# Objective: Create a program that ask the user to input their fullname. Print the number of characters in the input.

# 1. Ask the user to input their fullname.
fname = input("Input your fullname: ")

# 2. Count the characters in the fullname.
# 3. Print the length of the characters.
print(len(fname.replace(" ", "")))