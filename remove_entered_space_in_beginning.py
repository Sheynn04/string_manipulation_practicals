# Objective: Create a program that ask the user to input their fullname with several space characters at the beginning. Print the input without the spaces in the beginning.

# 1. Ask the user to input their full name with several space characters in the beginning.

fname = input('Enter your several spaces then your full name: ')

# 2. Remove the space from the left side of the full name.
# 3. Print the full name.

print(fname.lstrip())