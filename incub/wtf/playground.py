import urllib.parse
import requests
import urllib

#from urllib.parse import urlencode

class WikiTeleFoo:

    def build_qs(self, lemma: str, language: str = 'de')->str:
        endpoint = "https://www.wikidata.org/w/api.php"
        dict_my = {
            'action': 'wbsearchentities',
            'format': 'json',
            'language': 'de',
            'search': lemma
        }
        return endpoint + '?' + urllib.parse.urlencode(dict_my)
    


wtf = WikiTeleFoo()
uri = wtf.build_qs('Orthopädie')

print(uri)

lemma = 'cancerologia'

print(wtf.build_qs(lemma))