#imports da classes necessaria
from urllib.request import urlopen
from bs4 import BeautifulSoup

#coletando os dados de uma pagina
html = urlopen("http://pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, "lxml")

#tratando os dados; coletando dos filhos da tag 'table'
for child in bsObj.find("table", {"id":"giftList"}).children:
    print(child)

#tratando os dados; coletando dos descentendes da tag 'table'
for desc in bsObj.find("table", {"id":"giftList"}).descendants:
    print(desc)


