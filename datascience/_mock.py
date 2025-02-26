import pandas as pd
import random as rnd
dta = pd.read_json('mock.json')
#print(dta.columns)
#print(dta.groupby(['country', 'born_city']).last_name.value_counts())

print(len(dta.last_name.unique()))
print(dta.first_name.mode())

exit()

class MockGen:
    """ Class generating plausible mock data:
        - E-Mail address
    """
    
    def email(self, *args):
        mid = '@example.'
        
        first = self.get_rnd_value_from_ds()
        last = self.get_rnd_value_from_ds('last_name')
        
        prfx = self.get_rnd_mail_prefix(first, last)
        
        tld_generic = ['org', 'com', 'net']
        tld_2606 = ['test', 'example', 'invalid', 'localhost']
    
        number = rnd.randrange(1,101)
        
        if number > 79:
            addr = prfx + mid + tld_generic[rnd.randrange(0, len(tld_generic))]
        else: 
            addr = prfx + '@' + self.get_metasyn_rnd().lower() + '.' + tld_2606[rnd.randrange(0, len(tld_2606))]
            
        return addr
        
    def get_metasyn_vars(self):
        return [
                'ACME', 'foobar', 'foo', 'bar', 'baz', 'qux', 'quux', 'corge', 'grault', 'garply', 'waldo', 'fred', 'plugh', 'xyzzy', 'thud'
        ]
        
    def get_metasyn_rnd(self):
        tmp = self.get_metasyn_vars()
        return tmp[rnd.randrange(0,len(tmp))]
        
    def get_rnd_value_from_ds(self, what = 'first_name', ds = 'mock.json'):
        """ Getting random value from data source

        Args:
            what (str, optional): _description_. Defaults to 'first_name'.
        """
        # TODO: check if file exists
        dta = pd.read_json(ds)
        l = (len(dta))
        if what not in dta.columns:
            raise ValueError('Invalid value for what')
        
        return dta[what].iloc[rnd.randrange(0, l)]
    
    def get_rnd_mail_prefix(self, first = 'John', last ='Doe'):
        # TODO: implement diff. types of prefix:
        # peter.pan @ example. org|com|net / foo|bar...example|test..
        # peterpan @
        # panpeter @
        # pp @
        # peterp @
        # 
        return (first + '.' + last).lower()
        
mocker = MockGen()       
for x in range(0,40):
    print(mocker.email('Sven', 'Foo'))

# for x in range(44):
#     print(mocker.get_metasyn_rnd(), end=',')
    
# print