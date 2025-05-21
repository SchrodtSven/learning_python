

class Area:
    """Area instances may be used as attribtes / properties in other classes e.G: Rectangle, Circle, ...
    """
    unit = 'sqm'
    value = 0.0

    def __init__(self, value, unit='sqm'):
        self.value  = value
        
    def __add__(self, other):
        return self.value + other.value
    
    
    