import datetime

def create_id(string, fill_with='0', width=8):
    """ Creates a random id string based on current datetime

    Args:
        string (_type_): _description_
        fill_with (str, optional): _description_. Defaults to '0'.
        width (int, optional): _description_. Defaults to 8.

    Returns:
        _type_: _description_
    """
    now = datetime.datetime.now().timestamp()
    string = string + str(now).replace('.','')
    return f'{string:{fill_with}>{width}}'
    
    
print(create_id('Sven'))
print(create_id('Test'))
print(create_id('64532'))