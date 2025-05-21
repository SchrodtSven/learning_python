def filter_to_number(input_value):
    """
    Function filtering given (user) input to number (default value, if 
       sensibly casting is not possible, is 0.0)
    - @REMINDER to_my_self - in python <int> is not really a subset of
       <float>, but given ints are acceptable, if floats expected
    """
    default_value = 0.0
    if isinstance(input_value, str): 
        if input_value.isnumeric():
            number = float(input_value)
        else:
            number = default_value
    elif isinstance(input_value, int) or isinstance(input_value, float):
        number = float(input_value)
    else: 
        number = default_value
    return number


class Cube:
 
    side_length = 0.0
    
    def __init__(self, length=1.0):
        self.side_length = float(length)

    def get_volume(self):
        return float(self.side_length) ** 3
    


print(float('1.5'))


# first attempt
# s_len = 1.5
# wurfle = Cube(s_len)
# print(wurfle.get_volume())
    

number = filter_to_number(input('Side length of cube: '))
# print(type(number), number)
my_cube = Cube(number)
vol = my_cube.get_volume()
# print(wurfle.get_volume())
print(f'The volume of a cube with side length {number} is {vol}')