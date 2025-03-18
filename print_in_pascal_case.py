# Objective: Create a program that ask the user to input their fullname in incorrect casing. Print the input in pascal case.

# 1. Ask the user the input their fullname in incorrect casing. 
fname = input('Input your fullname in improper casing: ')

# 2. Convert the input into proper casing.
# 3. Remove the spaces in between the names.
# 4. Print the pascal format of their fullname.
print(fname.title().replace(" ",""))