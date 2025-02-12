<?php
$encoded = trim(file_get_contents('sparql.txt'));
$enc2 = 'https://query.wikidata.org/#%23K%C3%BCrzliche%20Ereignisse%0A%23title%3A%20Recent%20events%0ASELECT%20%3Fevent%20%3FeventLabel%20%3Fdate%0AWITH%20%7B%0A%20%20SELECT%20DISTINCT%20%3Fevent%20%3Fdate%0A%20%20WHERE%20%7B%0A%20%20%20%20%23%20find%20events%0A%20%20%20%20%3Fevent%20wdt%3AP31%2Fwdt%3AP279%2a%20wd%3AQ1190554.%0A%20%20%20%20%23%20with%20a%20point%20in%20time%20or%20start%20date%0A%20%20%20%20OPTIONAL%20%7B%20%3Fevent%20wdt%3AP585%20%3Fdate.%20%7D%0A%20%20%20%20OPTIONAL%20%7B%20%3Fevent%20wdt%3AP580%20%3Fdate.%20%7D%0A%20%20%20%20%23%20but%20at%20least%20one%20of%20those%0A%20%20%20%20FILTER%28BOUND%28%3Fdate%29%20%26%26%20DATATYPE%28%3Fdate%29%20%3D%20xsd%3AdateTime%29.%0A%20%20%20%20%23%20not%20in%20the%20future%2C%20and%20not%20more%20than%2031%20days%20ago%0A%20%20%20%20BIND%28NOW%28%29%20-%20%3Fdate%20AS%20%3Fdistance%29.%0A%20%20%20%20FILTER%280%20%3C%3D%20%3Fdistance%20%26%26%20%3Fdistance%20%3C%2031%29.%0A%20%20%7D%0A%20%20LIMIT%20150%0A%7D%20AS%20%25i%0AWHERE%20%7B%0A%20%20INCLUDE%20%25i%0A%20%20SERVICE%20wikibase%3Alabel%20%7B%20bd%3AserviceParam%20wikibase%3Alanguage%20%22%5BAUTO_LANGUAGE%5D%2Cmul%2Cen%22%20.%20%7D%0A%7D';
#echo urldecode($enc2);

#var_dump($enc2);

$foo2 = 'https://query.wikidata.org/##Kürzliche Ereignisse
#title: Recent events
SELECT ?event ?eventLabel ?date
WITH {
  SELECT DISTINCT ?event ?date
  WHERE {
    # find events
    ?event wdt:P31/wdt:P279* wd:Q1190554.
    # with a point in time or start date
    OPTIONAL { ?event wdt:P585 ?date. }
    OPTIONAL { ?event wdt:P580 ?date. }
    # but at least one of those
    FILTER(BOUND(?date) && DATATYPE(?date) = xsd:dateTime).
    # not in the future, and not more than 31 days ago
    BIND(NOW() - ?date AS ?distance).
    FILTER(0 <= ?distance && ?distance < 31).
  }
  LIMIT 150';

  print(urlencode($foo2));