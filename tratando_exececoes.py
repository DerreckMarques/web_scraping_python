#classes necessarias
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup


#tratando as exececoes ao tentar abrir uma url
#retorno: a tag h1 da pagina passada como parametro
def getTitle(sUrl):
    try:
        html = urlopen(sUrl)
    except HTTPError as e:
        return None

    try:
        bsObj = BeautifulSoup(html.read(), "lxml")
        title = bsObj.body.h1
    except AttibuteError as e:
        return None
    
    return title


#chamando o metodo getTitle e verificando se foi encontrado a tag h1 da url
title = getTitle("http://www.pythonscraping.com/exercises/exercise1.html")
if title == None:
    print("Title could not be found")
else:
    print(title)
