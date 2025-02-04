#!/usr/bin/env python3
# built-in/intro.py
# 
# SUBJECT: Python, qu'est-ce que c'est?
# AUTHOR Sven Schrodt <sven@schrodt.club>
# SINCE: 2025-01-03

# The reference manual describes the syntax and “core semantics” of the Python language:
# SEE: https://docs.python.org/3/reference/index.html

# A little bit of theory first:

# Lexical analysis¶
""" 
    A Python program is read by a parser. Input to the parser is a stream of
    tokens, generated by the lexical analyzer. This chapter describes how the 
    lexical analyzer breaks a file into tokens.

    Python reads program text as Unicode code points; the encoding of a source
    file can be given by an encoding declaration and defaults to UTF-8, see 
    PEP 3120 for details. 
    If the source file cannot be decoded, a SyntaxError is raised.
"""

# Line structure

# A Python program is divided into a number of logical lines.
# Logical lines

# The end of a logical line is represented by the token NEWLINE. 
# Statements cannot cross logical line boundaries except where NEWLINE is 
# allowed by the syntax (e.g., between statements in compound statements). 
# A logical line is constructed from one or more physical lines by following
# the explicit or implicit line joining rules.
# 
# Physical lines
# A physical line is a sequence of characters terminated by an end-of-line 
# sequence. 
# 
# In source files and strings, any of the standard platform line termination
# sequences can be used - the Unix form using ASCII LF (linefeed), the Windows
# form using the ASCII sequence CR LF (return followed by linefeed), or the
# old Macintosh form using the ASCII CR (return) character. 
# 
# All of these forms can be used equally, regardless of platform. The end of 
# input also serves as an implicit terminator for the final physical line.
# When embedding Python, source code strings should be passed to Python APIs 
# using the standard C conventions for newline characters (the \n character, 
# representing ASCII LF, is the line terminator).

# Comments
# A comment starts with a hash character (#) that is not part of a string 
# literal, and ends at the end of the physical line. A comment signifies the 
# end of the logical line unless the implicit line joining rules are invoked. 
# Comments are ignored by the syntax.
#
 
# Encoding declarations
# If a comment in the first or second line of the Python script matches the 
# regular expression coding[=:]\s*([-\w.]+), this comment is processed as an 
# encoding declaration;
# If no encoding declaration is found, the _default encoding is UTF-8_. 