import json
# Get source and metadata for the Jupiter article on English Wikipedia
import requests

#url = 'https://en.wikipedia.org/w/rest.php/v1/page/Jupiter'
url = 'https://de.wiktionary.org/w/api.php?action=query&list=search&srsearch=Fubar&format=json'
headers = {
    'User-Agent': 'MediaWiki REST API docs examples/0.1 (https://www.mediawiki.org/wiki/API_talk:REST_API)'
}


response = requests.get(url, headers=headers)
data = response.json() # data is <class 'dict'>
excerpt = data['query']['search'][0]['snippet']
pid = data['query']['search'][0]['pageid']
print(pid, excerpt)
#parsed = json.loads(data)
#print(parsed)

# https://en.wikipedia.org/w/api.php?action=query&prop=info&pageids=11395&inprop=url