# FILE: built-in/class_dunder.py 
# SUBJECT: Dunder functions in in Python classes
#          - name and intent of 'magic functions'
#
# AUTHOR: Sven Schrodt <sven@schrodt.club>
# SINCE:  2025-01-29
# SEE: https://realpython.com/python-classes/#special-methods-and-protocols
# SEE: https://realpython.com/python-magic-methods/

class Car:
    # ...

    # instance initializer
    def __init__(self, make, model, year, color, nick = None):
        self.make  = make
        self.model  = model
        self.year = year
        self.color = color
        self.nick = nick
        
    # informal string representation
    def __str__(self):
        return f"{self.make} {self.model}, {self.color} ({self.year}) with nick name: {self.nick}"
    
    #   formal string representation
    def __repr__(self):
        return (
            f"{type(self).__name__}"
            f'(make="{self.make}", '
            f'model="{self.model}", '
            f"year={self.year}, "
            f'color="{self.color}", '
            f'nick="{self.nick}")'
        )

emile = Car("Ford", "Fiesta Champions League Edition", 2011, "Royal Blue", 'Émile')

print(str(emile))
print(repr(emile))

# 'Toyota Camry, Red (2022)'
# >>> print(toyota_camry)
# Toyota Camry, Red (2022)

# >>> toyota_camry
# Car(make="Toyota", model="Camry", year=2022, color="Red")
# >>> repr(toyota_camry)
# 'Car(make="Toyota", model="Camry", year=2022, color="Red")'