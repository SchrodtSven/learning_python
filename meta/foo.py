
with open('meta_syntactic_vars.txt', 'r') as fr:
    foo_lines = fr.readlines()
foo_lines.sort()
print(''.join(foo_lines))

# SEE: https://en.wikipedia.org/wiki/Metasyntactic_variable
""" Spam, ham, and eggs are the principal metasyntactic variables used in the 
Python programming language.[10] This is a reference to the famous comedy 
sketch, "Spam", by Monty Python, the eponym of the language.[11] 
In the following example spam, ham, and eggs are metasyntactic variables and 
lines beginning with # are comments. """

# Define a function named spam
def spam():

    # Define the variable ham
    ham = "Hello World!"

    # Define the variable eggs
    eggs = 1

    return
