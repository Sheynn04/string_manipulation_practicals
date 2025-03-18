# Objective: Create a program that ask the user to input their fullname in incorrect casing. Print the input in snake case.

# 1. Ask the user to input their fullname.
fname = input("Input your name in improper casing: ")

# 2. Convert the characters of the input into lowercase.
# 3. Replace the spaces with an underscore.
# 4. Print the fullname in snake case format.
print(fname.lower().replace(" ","_"))