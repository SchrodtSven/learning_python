# Wiki Tele Foo
# Consuming wiki* resources
# AUTHOR: Sven Schrodt<sven@schrodt.club>
# SINCE: 2025-02-12

class WikiTeleFoo:
    """ Consuming wiki* resources """
    format = 'json'
    host = 'de'
    action = 'query'
    # TODO: managing URIs
    base_uri = 'https://{}.wiktionary.org/w/api.php?action={}&list=search&srsearch={}&format={}' # to be used by str.format()
    
    def __init__(self, search='Foo'):
       self.search = search
       
    
    def build_full_query(self):
        return self.base_uri.format(self.host, self.action, self.search, self.format)
        
wtf = WikiTeleFoo()
print(wtf.build_full_query())
