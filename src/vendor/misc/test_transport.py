import unittest
from time import sleep
from transport import TransportationVehicle

class TestStringMethods(unittest.TestCase):
    """ Unit testing TransportVhicle

    Args:
        unittest (_type_): _description_
    """
    
    @classmethod
    def setUpClass(cls):
        cls.vehicle = TransportationVehicle()
        
    def test_drive(self):
        values = [1, 2, 33, 45, 55, 99]
        for value in values:
            # print(' I drive {} '.format(value))
            self.vehicle.speed = value
        self.assertEqual(value, self.vehicle.speed)


        
    
if __name__ =='__main__':
    unittest.main()