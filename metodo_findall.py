#importação da classes necessárias
from urllib.request import urlopen
from bs4 import BeautifulSoup

#coletando os dados de uma url
html = urlopen("http://www.globo.com/")
bsObj = BeautifulSoup(html, "lxml")

#tratando os dados
#mostrando os dados dos cabecalhos da pagina
tags = {"h1", "h2", "h3", "h4", "h5", "h6"}
headers = bsObj.findAll(tags)
for h in headers:
    print(h.get_text())

#procurando por atributo em ma tag e a mostrando
tag = "div"
attribute = {"class":"glb-grid"}
attributes = bsObj.findAll(tag, attribute)
for atr in attributes:
    print(atr.get_text())

#procurando por um texto na pagina
texto = "moda"
textos = bsObj.findAll(text=texto)
print(len(textos))

#utilizando o 'keyword' do findAll()
keywords = bsObj.findAll(id=attribute)
print(textos[0].get_text())
