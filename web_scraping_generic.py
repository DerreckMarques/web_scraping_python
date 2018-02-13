from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random

pages = set()
random.seed(datetime.datetime.now)


#Recupera uma lista de todos os links internos encontrados em uma pagina
def getInternalLinks(bsObj, includeUrl):
    internalLinks = []
    #Encontra todos os links que começam com a "/"
    for link in bsObj.findAll("a", href=re.compile("^(/|.*" +includeUrl+ ")")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                internalLinks.append(link.attrs['href'])
    return internalLinks


#Recupera uma lista de todos os links externos encontrados em uma pagina
def getExternalLinks(bsObj, excludeUrl):
    externalLinks = []
    #Encontra todos os links que começam com "http" ou "www" que não contêm a url atual
    for link in bsObj.findAll("a", href=re.compile("^(http|www)((?!"+excludeUrl+").)*$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks


def splitAddress(address):
    addressParts = address.replace("http://", "").split("/")
    return addressParts

def getRandomExternalLink(startingPage):
    html = urlopen(startingPage)
    bsObj = BeautifulSoup(html)
    externalLinks = getExternalLinks(bsObj, splitAddress(startingPage)[0])
    if len(externalLinks) == 0:
        internalLinks = getInternalLinks(bsObj, splitAddress(startingPage)[0])
        return internalLinks[random.randint(0, len(internalLinks)-1)]

    else:
        return externalLinks[random.randint(0, len(externalLinks)-1)]


def followExternalOnly(StartingSite):
    externalLink = getRandomExternalLink(StartingSite)
    print("Random external link is: " + externalLink)
    followExternalOnly(externalLink)

followExternalOnly("http://www.globo.com")
