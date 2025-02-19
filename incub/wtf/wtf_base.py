# Wiki Tele Foo Base Classes
#
# SUBJECT: Consuming wiki* resources
#
# AUTHOR: Sven Schrodt<sven@schrodt.club>
# SINCE: 2025-02-12
import requests
import urllib.parse

class WTFHttpClient:
    response = None
    headers = {'User-Agent': 'Wiki Tele Foo Http Client; Version 0.23.42',
               'X-POST_FUCKUP': 'Http is down().debug()'}
    
    def __init__(self):
        pass
    
    def get(self, uri):
        return requests.get(uri, headers=self.headers)
        #url = 'https://de.wiktionary.org/w/api.php?action=query&list=search&srsearch=Fubar&format=json'
    


 

class WTFQueryBuilder:
    """ Consuming wiki* resources """
    format = 'json'
    host = 'de'
    action = 'query'
    # TODO: managing different URIs
    base_uri = 'https://{}.wiktionary.org/w/api.php?action={}&list=search&srsearch={}&format={}' # to be used by str.format()
    
    def __init__(self, search='Foo'):
       self.search = search
       
    
    def build_full_query(self, lemma: str, language: str = 'de')->str:
        endpoint = "https://www.wikidata.org/w/api.php"
        dict_my = {
            'action': 'wbsearchentities',
            'format': 'json',
            'language': 'de',
            'search': lemma
        }
        return endpoint + '?' + urllib.parse.urlencode(dict_my)
        
#wtf = WTFQueryBuilder()
#print(wtf.build_full_query())
""" client = WTFHttpClient()
uri_1 = 'https://de.wiktionary.org/w/api.php?action=query&list=search&srsearch=Fubar&format=json'
uri = 'http://localhost:8080/reflect.php'
response = client.get(uri)
print(response.headers) """
 
