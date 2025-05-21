# FILE: built-in/typing.py 
# SUBJECT: Support for type hints in Python 
#
# AUTHOR: Sven Schrodt <sven@schrodt.club>
# SINCE:  2025-01-28
# 

# type aliases

# The type statement is new in Python 3.12.  
type Vector = list[float]

def scale(scalar: float, vector: Vector) -> Vector:
    return [scalar * num for num in vector]

new_vec = scale(2.3, [1.1, 2.3, 4.0])

print(new_vec)
