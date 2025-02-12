# Wiki Foo -> getting stuff from Wiki* APIs
# https://en.wikipedia.org/w/api.php?action=parse&page=Foo&format=json

# https://de.wikipedia.org/w/api.php


# https://de.wiktionary.org/w/api.php?action=parse&page=Foo&format=json

# ini_set('user_agent', 'MyCoolTool/1.1 (https://example.org/MyCoolTool/; MyCoolTool@example.org) UsedBaseLibrary/1.4');


#LANG = 'de'
# api_url = f'https://{LANG}.wikipedia.org/w/api.php'

#print(api_url)

# https://de.wiktionary.org/w/api.php?action=query&list=search&srsearch=%s

#https://de.wiktionary.org/w/api.php?action=query&list=search&srsearch=Fubar


class WikiTeleFoo:
    format = 'json'
    host = 'de'
    search = 'Foo'
    base_uri = 'https://{}.wiktionary.org/w/api.php?action=query&list=search&srsearch={}&format={}'
    
    def __init__(self):
        
        print(self.base_uri)
    
    def build_full_query(self):
        return self.base_uri.format(self.host, self.search, self.format)
        
wtf = WikiTeleFoo()
print(wtf.build_full_query())
