import unittest
import string
from string import Template

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertNotEqual('foo'.upper(), 'Foo')

    def test_lower(self):
        self.assertEqual('FoOBaR'.lower(), 'foobar')
    
    def test_concat_one(self):
        #Using helper function string.capwords()
        self.assertEqual(string.capwords('get me right'), 'Get Me Right')

    def test_if_is_palindrome(self):
        text = "Otto"
        text2 = "Foo"
        text = text.casefold()
        mirror = reversed(text)
        self.assertEqual(''.join(mirror), text)

    def test_template(self):
        s = Template('$who likes $what')
        t =s.substitute(what='PHP, SQL & XML', who='Sven')
        self.assertEqual('Sven likes PHP, SQL & XML', t)


if __name__ =='__main__':
    unittest.main()