#imports da classes necessaria
from urllib.request import urlopen
from bs4 import BeautifulSoup

#coletando dados de uma pagina web
html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html)

#colentado os valores da tags pais e irmao e imprimindo seu texto
print(bsObj.find("img", {"src":"../img/gifts/img1.jpg"}
                 ).parent.previous_sibling.get_text())
