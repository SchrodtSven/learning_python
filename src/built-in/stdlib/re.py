#
# FILE: built-in/re.py
# SUBJECT: Regular expression in Python ('s standard library)
#
# AUTHOR: Sven Schrodt <sven@schrodt.club>
# SINCE: 2025-02-03
# SEE: https://docs.python.org/3/howto/regex.html

""" “There are applications that don’t need REs at all, so there’s no need to 
     bloat the language specification by including them.”
"""
# “
# ”
import re

txt = 'The rain in Spain'
x = re.findall('[a-c]', txt)
print(x)



txt = "The rain in Spain, the block in __main__. You're so vain, said Johnny's Wayne"
fnd = r'ai'

x = re.findall(fnd, txt, re.IGNORECASE)
print(x) 
print(type(x)) 

x3 = re.split(r"\s", txt)
print(x3) 

x2 = re.search(r"\s", txt)

print("The first white-space character is located in position:", x2.start()) 

# Replace every white-space character with '_':
x1 = re.sub(r"\s", "_", txt)
print(x1) 

# Applying a search on a string will return an object

x = re.search("ai", txt)
print(x.string) 
print(x.span()) 
print(x.group()) 

# let 's do a search in German - we will isolate whole words from a given message while ignoring case:
msg = r'Hallo an alle im Alleingang: alleine im All unterwegs zu sein ist anstrengend und gefährlich'
matches = re.findall(r"\b\w*all\w*\b", msg, re.I)
print(matches)


# Metacharacters

# Metacharacters are characters with a special meaning:
# Character 	Description 	Example 	Try it
# [] 	A set of characters 	"[a-m]" 	
# \ 	Signals a special sequence (can also be used to escape special characters) 	"\d" 	
# . 	Any character (except newline character) 	"he..o" 	
# ^ 	Starts with 	"^hello" 	
# $ 	Ends with 	"planet$" 	
# * 	Zero or more occurrences 	"he.*o" 	
# + 	One or more occurrences 	"he.+o" 	
# ? 	Zero or one occurrences 	"he.?o" 	
# {} 	Exactly the specified number of occurrences 	"he.{2}o" 	
# | 	Either or 	"falls|stays" 	
# () 	Capture and group

ml_txt = """  In May 2020 I lost 2.32 € on my way home.
     5,000 robots are walking down the road, running then at 135.99 MpH
     My bank account telling my balance: -10,423,987.23 $
"""

print(re.findall(r"-?\d+(?:[.,]\d+)?", ml_txt, re.I))