from bs4 import BeautifulSoup
soup = BeautifulSoup(markup="<p>Some<b>bad<i>HTML", features="html.parser")
print(soup.prettify())