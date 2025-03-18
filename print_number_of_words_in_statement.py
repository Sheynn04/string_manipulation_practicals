# Objective: Create a program that ask the user to input a complete statement. Print the number of words in the input.

# 1. Ask the user the input a complete statement.
comp_statement = input('Please enter a complete statement: ')

# 2. Split the statement into a list of words.
# 3. Count the number of words. 
# 4. Print the number of words in the statement. 
print(len(comp_statement.split()))
