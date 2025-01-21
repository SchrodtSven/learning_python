#
# SUBJECT: Unit testing built-in functions
# SINCE: 2025-01-21 
# AUTHOR: Sven Schrodt <sven@schrodt.club>
#
# FAQ: 
#           run it with: python3 -m $THIS_FILE_NAME
#


import unittest

class TestStrings(unittest.TestCase):
    
    def test_rounding(self):
        self.assertEqual(round(-0.5), 0)
        self.assertEqual(round(-0.6), -1)
        self.assertEqual(round(0.55), 1)
        
    if __name__ =='__main__':
        unittest.main(verbosity=2)
            
    
    list = [1, 2, 3, 4, 5, 6]
    # [start|stop|step]
    print(list[::2])
    