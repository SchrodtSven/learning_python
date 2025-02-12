#
# FILE: built-in/re.py
# SUBJECT: Regular expression in Python ('s standard library)
#
# AUTHOR: Sven Schrodt <sven@schrodt.club>
# SINCE: 2025-02-03
# SEE: https://docs.python.org/3/howto/regex.html

""" Quote from python.org “There are applications that don’t need REs at all, so there’s no need to 
     bloat the language specification by including them.”
"""
# Importing lib
import re

# Regular expressions use the backslash character ('\') ..
txt = 'Pyromane Pyotr Parker klagt und Dr. E. Pythgoras sagt: Pytillo, Du  Pythonschlange' #.. so we use raw string for Regexs 

# examples in re \b -> boundary 
#                \w -> matching whole word(s)
#                + -> quantifier for 1 ..x times

matches = re.findall(r'\bpy\w+\b', txt, re.I)
print(matches)
print(type(matches))
assert(len(matches) == 5)


txt = 'The rain in Spain'
x = re.findall('[a-c]', txt)
print(x)



txt = "The rain in Spain, the block in __main__. You're so vain, said Johnny's Wayne"
fnd = r'ai'

x = re.findall(fnd, txt, re.IGNORECASE) # or re.I 
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

txt = '''                                                    Castrop-Rauxel, 16.01.2025
                    Liebes Krümmelmonster,
                    am 25.11.2024 habe ich eine Website besucht und musste
                    sofort an Dich denken: so viele Cookies!  
                    Am 03.01.2025 habe ich die  Site wieder angesurft.
                    Weitere Male (15.01.2025, 28.01. und 03.04, also gestern)
                    hagelte es nur Fehlermeldungen des Aromas'*NXDOMAIN'. Das 
                    hilet an bis zum bis heute. 
                    Sehen wir uns am 23.05.2025 zum Jahrestag des <GG />?
                    
                    Glück auf!  
                    
                    Hanny 'Peter_X' Wechselbaum
'''

# finding german dates

matches = re.findall(r'\b\d+[.]\d+[.]\d+\b', txt)
print(matches)

# get the months

matches = re.findall(r'\.(.*?)\.', txt)
print(matches)

foo = """ Hallo Python-Freunde,
          in dieser Ausgabe wenden wir uns an euch mit einer traurigen Mitteilung:
          Python 2.* ist tot.
          'Endlich!' vernehme ich aus der Ferne laut gerufen
          """
          
print(foo)