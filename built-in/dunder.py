# FILE: built-in/dunder.py 
# SUBJECT: Dunder functions in in Python 
#          - name and intent of 'magic functions'
#
# AUTHOR: Sven Schrodt <sven@schrodt.club>
# SINCE:  2025-01-29
# SEE: https://realpython.com/python-classes/#special-methods-and-protocols
# SEE: https://realpython.com/python-magic-methods/


# Overview
#
# Protocol 	        Provided Feature 	                            Special Methods
# Iterator 	        Allows you to create iterator objects 	        .__iter__() and .__next__()
# Iterable 	        Makes your objects iterable 	                .__iter__()
# Descriptor 	    Lets you write managed attributes 	            .__get__() and optionally .__set__(), .__delete__(), and .__set_name__()
# Context manager 	Enables an object to work on with statements 	.__enter__() and .