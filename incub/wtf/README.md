 # Wiki Tele Foo

 - action API und 
  - ReST API - https://www.mediawiki.org/wiki/API:REST_API

WIKIMEDIA COMMONS
- https://commons.wikimedia.org/wiki/Hauptseite

# CRE.fm # 205 Wikidata, Jens Ohlig, https://github.com/johl/nlqa/blob/master/nlqa.py



 ## URIs
 Wiki Foo -> getting stuff from Wiki* APIs
 https://en.wikipedia.org/w/api.php?action=parse&page=Foo&format=json

 https://de.wikipedia.org/w/api.php

 - Sandbox: https://de.wiktionary.org/wiki/Spezial:ApiSandbox


 https://de.wiktionary.org/w/api.php?action=parse&page=Foo&format=json

# Corresponding user agent header in PHP     - phone prefix BO:       
 ini_set('user_agent', 'Wiki Tele Foo/;wtf@schrodt.nrw)Version 0.23.42');


LANG = 'de'
api_url = f'https://{LANG}.wikipedia.org/w/api.php'

print(api_url)

 https://de.wiktionary.org/w/api.php?action=query&list=search&srsearch=%s

https://de.wiktionary.org/w/api.php?action=query&list=search&srsearch=Fubar

ReST API:
https://de.wiktionary.org/w/rest.php/v1/search/page?q=Onkologie

16	
id	259314
key	"Karzinologie"
title	"Karzinologie"
excerpt	'[2] Wissenschaft, die sich mit Krebstieren beschäftigt Synonyme: [1] <span class="searchmatch">Onkologie</span> [2] Crustaceologie Oberbegriffe: [1, 2] Wissenschaft Beispiele: [1] Die'
matched_title	null
description	null
thumbnail	null

## FROM PAGE ID 3 TITLEGetting URL and then parsing get the URL of the wikipage by making an API call like http://en.wikipedia.org/w/api.php?action=query&prop=info&pageids=<your_pageid_here>&inprop=url

then go to the URL and parse the text

Get pagename and then the content

Wikipedia API allows extraction of text if the pagename is known. But asyou know only the pageid for now, you will need to convert the pageid into pagename by using an API call like

http://en.wikipedia.org/w/api.php?action=query&pageids=<your_pageid_here>&format=json
11395
This will give you the pagename, then you can make another API call to get the contents

http://en.wikipedia.org/w/api.php?action=parse&prop=text&page=<your_pagename_here>&format=json


http://en.wikipedia.org/w/api.php?action=query&pageids=11395&format=json



https://en.wikipedia.org/wiki/Talk:Four_Noble_Truths
                               
                               Talk:Four Noble Truths

