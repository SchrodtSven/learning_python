#
# SUBJECT: Unit testing built-in string methods
# SINCE: 2025-01-17 
# AUTHOR: Sven Schrodt <sven@schrodt.club>
#
# FAQ: 
#           run it with: python3 -m $THIS_FILE_NAME
#


import unittest

class TestStrings(unittest.TestCase):
    
    def test_replacing(self):
        find = 'guys'
        repl = 'women'
        foo = 'Three guys went into a bar' . replace(find, repl)
        self.assertEqual(foo, 'Three women went into a bar') 

    def test_index(self):
        
        foo = self.get_foo()
        self.assertEqual(foo[3], 'e')
        self.assertEqual(foo[4], 'e')
        self.assertTrue('Foo'[-1] == 'o')            
        
    def test_slicing(self):
        foo = self.get_foo()
        self.assertEqual(foo[-3:], 'bar')
        self.assertEqual(foo[0:len(foo)], foo)
    
    def test_format_positional_args(self):
        # Repeating argument indices
        self.assertEqual ('{0}{1}{0}'.format('abra', 'cad'), 'abracadabra')
        
    
    def test_format_named_args(self):
        # Repeating argument indices
        self.assertEqual ('My name is {first_name} {last_name}'.format(first_name='Sven', last_name='Schrodt'), 'My name is Sven Schrodt')
        self.assertEqual ('My name is {} {}'.format(*('Sven','Schrodt')), 'My name is Sven Schrodt')
        # FIXME-done 2025-01-18 18:52: ** ->check, why
        # * -> positional by indices, ** named with keywords
        self.assertEqual ('My name is {first_name} {last_name}'.format(**{'first_name': 'Sven', 'last_name': 'Schrodt'}), 'My name is Sven Schrodt')
    
        
    def get_foo(self):
        return 'Three guys went into a bar'
    
    def test_format_args(self):
        coord = (3, 5)
        expected = 'X: 3;  Y: 5'
        self.assertEqual('X: {0[0]};  Y: {0[1]}'.format(coord), expected)
        

        
        
        #
        
        
 #        

    if __name__ =='__main__':
        unittest.main(verbosity=2)
            
    
    