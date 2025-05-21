# 
#  
# SUBJECT  Mocking etxt data for unit testing purposes
# SINCE 2025-01-17 
# AUTHOR Sven Schrodt <sven@schrodt.club>

from random import randrange
class MockTextGenerator:
    
    metasyn_vars =  'foobar, foo, bar, baz, qux, quux, corge, grault, garply, waldo, fred, plugh, xyzzy'.split(', ') # Name list of Metasyntactic Variables
    pangrams = ('The quick brown fox jumps over the lazy dog.', 'Foo bar')
    
    def pangram(self, which = 'most_popular'):
        """ Getting a phrase that is a pangram (aka holoalphabetic: sentence using every letter of a given alphabet at least once)

        Args:
            which (str, optional): _description_. Defaults to 'most_popular'.
        """
        
        match which:
            case 'most_popular':
                return self.pangrams[0]
            case _:
                return self.pangrams[1]

    def metasyn_rnd(self):  
        """ Getting a (pseudo) random Metasyntactic variable name

        Returns:
            _type_: _description_
        """
        return self.metasyn_vars[randrange(len(self.metasyn_vars)-1)]

gen = MockTextGenerator()

#print(gen.pangram('Foo'))

tmp = 'foobar, foo, bar, baz, qux, quux, corge, grault, garply, waldo, fred, plugh, xyzzy'.split(', ')
# print(tmp)


print('foo' in MockTextGenerator.metasyn_vars)