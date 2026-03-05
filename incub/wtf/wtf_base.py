# Wiki Tele Foo Base Classes
#
# SUBJECT: Consuming wiki* resources
#
# AUTHOR: Sven Schrodt<sven@schrodt.nrw>
# SINCE: 2025-02-12
# - TODO: refactor me!!!

import requests
import urllib.parse


class WTFHttpClient:
    response = None
    headers = {
        "User-Agent": "Wiki Tele Foo Http Client; Version 0.23.42",
        "X-POST_FUCKUP": "Http is down().debug()",
    }

    def __init__(self):
        pass

    def get(self, uri, ret=True):
        self.response = requests.get(uri, headers=self.headers)
        if ret:
            return self.response


class WTFQueryBuilder:
    """Consuming wiki* resources"""

    format = "json"
    host = "de"
    action = "query"
    # TODO: managing different URIs
    base_uri = "https://{}.wiktionary.org/w/api.php?action={}&list=search&srsearch={}&format={}"  # to be used by str.format()

    def __init__(self, search="Foo"):
        self.search = search

    def build_full_query(self, lemma: str, language: str = "de", format="json") -> str:
        endpoint = "https://www.wikidata.org/w/api.php"
        dict_my = {
            "action": "wbsearchentities",
            "format": format,
            "language": language,
            "search": lemma,
        }
        return endpoint + "?" + urllib.parse.urlencode(dict_my)


if __name__ == "__main__":
    wtf = WTFQueryBuilder()
    uri = wtf.build_full_query(lemma="Peter Parker", language="fr")
    print(uri)
    # client = WTFHttpClient()
    # response = client.get(uri)
    # print(response.headers)
