 # Wiki Tele Foo

 ## URIs
 Wiki Foo -> getting stuff from Wiki* APIs
 https://en.wikipedia.org/w/api.php?action=parse&page=Foo&format=json

 https://de.wikipedia.org/w/api.php


 https://de.wiktionary.org/w/api.php?action=parse&page=Foo&format=json

# Corresponding user agent header in PHP     - phone prefix BO:       
 ini_set('user_agent', 'Wiki Tele Foo/;wtf@schrodt.nrw)Version 0.23.42');


LANG = 'de'
api_url = f'https://{LANG}.wikipedia.org/w/api.php'

print(api_url)

 https://de.wiktionary.org/w/api.php?action=query&list=search&srsearch=%s

https://de.wiktionary.org/w/api.php?action=query&list=search&srsearch=Fubar