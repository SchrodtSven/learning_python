# FILE: geometry/line_segment.py 
# SUBJECT: Support for type hints in Python 
#
# AUTHOR: Sven Schrodt <sven@schrodt.club>
# SINCE:  2025-01-28
# 
class LineSegment:
    """  A line segment in geometry is part of a straight line, bounded by two
         distinct endpoints (its extreme points) containing every point in between.
         
         Its length is the Euclidean distance between the endpoints.
         
         TODO: extend with given endpoints
    """ 
    
    length: float = 0.0
    
    def __init__(self, length):
        self.length = length
    
    def length(self)-> float:
        return self.length