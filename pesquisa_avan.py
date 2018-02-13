
#importação das classes necessárias
from urllib.request import urlopen
from bs4 import BeautifulSoup

#coletando os dados de uma url
html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html, "lxml")

#filtrando os dados, pela tag 'span' que esteja com atributo 'class="gren"'
nameList = bsObj.findAll("span", {"class":"green"})
for name in nameList:
    print(name.get_text())

            
