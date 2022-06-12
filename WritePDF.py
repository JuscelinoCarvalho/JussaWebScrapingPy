class WritePDF():
    """description of class"""

import urllib.request
from urllib.request import Request, urlopen 
import requests

def __init__(self, strWebPdfPathSource, strLocalPdfDest):
    self.strSource = strWebPdfPathSource
    self.strDest = strLocalPdfDest

##createPDF = WritePDF(self, strSource, strDest)

def createPDF(self):
#url="http://diariooficialms.com.br/baixar-materia/71944/59cc46ba930f0dd063e9a4d4806d677d"
#  "C:\\Users\\jkarv\\Documents\\TESTE.pdf"
    url = self.strSource
    #req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})  
    req = requests.get(url, stream = True)  
    r = requests.get(createPDF.strSource)

    code = open(self.strDest, "wb")

    code.write(r.content)
    ###code.flush()
    code.close()
    ###with open("C:\\Users\\jkarv\\Documents\\TESTE.pdf", "wb") as code:


### FIM DA CLASSE
pass


