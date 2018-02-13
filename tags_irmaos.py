#imports da classes necessaria
from urllib.request import urlopen
from bs4 import BeautifulSoup

#coletando dados de uma pagina web
html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html)

#tratando os dados
for sibling in bsObj.find("table", {"id":"giftList"}).tr.next_siblings:
    print(sibling)
