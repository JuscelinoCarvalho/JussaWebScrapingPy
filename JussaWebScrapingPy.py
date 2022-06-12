#Importa as bibliotecas necessarias
#import os
#import pandas as pd
#import numpy as np
#import matplotlib.pyplot as plt
#import seaborn as sns
#import time
#import json
#import PyPDF2 as pypdf
#import urllib
#import urllib3
#import requests
#import pyodbc
#import fitz  # this is pymupdf

#from io import StringIO
#from urllib.request import urlopen
#from bs4 import BeautifulSoup
#from typing import List
#from datetime import datetime

from clsASSOMASUL import clsASSOMASUL
from clsTJMS import clsTJMS
from clsTrandingView import clsTrandingView
from clsJussaDownTube import clsJussaDownTube
from clsConvertToMP3 import  clsConvertToMP3
from clsValorEconomico import clsValorEconomico
from clsCMTLS import clsCMTLS


from enum import Enum


class EnumScraping(Enum):
    ASSOMASUL = 0
    TJMS = 1
    TRADING = 2
    YOUTUBE = 3
    CONVERT = 4
    VALOR_ECONOMICO = 5
pass


class JussaWebScrapingPy():
    #--------------------------------------------------------------------------------------------------------------------------------------------------------
    #Criado por: Juscelino Alves de Carvalho
    #Criado em.: 17 agosto 2020 09:50h
    #Objetivo..: Acessar o site da Assomasul e colher dados das publicações diárias relativas a um municipio especifico e armazenar em uma base de dados.
    #-------------------------------------------------------------------------------------------------------------------------------------------------------

    def __init__(self, urlSite, EnumScraping = "CONVERT", strCidade="", strDtIni="", strDtFim="", bolNomParte_notPROCESSO=True, strNomeParte="", strNumeroProcesso="", strDwnldTJMSPath="", strDwnldASSOMAPath="" ):
        self.EnumSite = EnumScraping
        self.strCidade = strCidade
        self.strDtIni = strDtIni
        self.strDtFim = strDtFim
        self.bolNomParte_notPROCESSO = bolNomParte_notPROCESSO
        self.strNomeParte = strNomeParte
        self.strNumeroProcesso = strNumeroProcesso
        self.strDwnldTJMSPath = strDwnldTJMSPath
        self.strDwnldASSOMAPath = strDwnldASSOMAPath
        self.urlSite = urlSite

        if self.EnumSite=="ASSOMASUL":
            path=self.strDwnldASSOMAPath
        elif self.EnumSite=="TJMS":
            path=self.strDwnldTJMSPath
        pass ### __init__


    def CorrigeNome(strNome=""):
        #° º
        strNome = strNome.replace('Cidade: TRÊS LAGOAS', '').replace(' ','-').replace('/','').replace('º', '0').replace('á','a').replace('é','e').replace('í', 'i')
        strNome = strNome.replace('ó', 'o').replace('ú', 'u').replace('°', 'o').replace('ç', 'c').replace('ã', 'a').replace('õ', 'o')
        strNome = strNome.replace('Á','a').replace('É','e').replace('Í', 'i').replace('Ó', 'o').replace('Ú', 'u').replace('Ç', 'c').replace('Ã', 'a').replace('Õ', 'o')
        strNome = strNome.replace('.','').replace(',','').replace(':','').replace(chr(10),'').replace(chr(13),'')
        strNome = strNome.lower()

        return strNome

        pass

    def CorrigePDFContent(strContent = ""):
    
        strContent = strContent.replace('xc3xa9', 'é').replace('xc3xa1', 'á').replace('xc3xad', 'í').replace('xc3xba', 'ú').replace('xc3x8d', 'Í').replace('xc3xa7', 'ç')
        strContent = strContent.replace('xc3xa3', 'ã').replace('xc3x83', 'Ã').replace('xc3xb5', 'õ').replace('xc3x8a', 'Ê').replace('xc3x9a', 'Ú').replace('xc2xba', 'º')
        strContent = strContent.replace('xc3x93', 'ó').replace('xe2x80x93', ' - ').replace('xc3x87', 'Ç').replace('xc3x8a', 'Ê').replace('xe2x80x9c', '"').replace('xe2x80x9d', '"')
        strContent = strContent.replace('xc3x81', 'Á').replace('xc2xa0', ' ').replace('xc2xaa', 'ª')

        return strContent

        pass

    bolTrading = True
    #region TESTE
    bolTJMS_notAssomasul = True
    strCidade = "TRÊS LAGOAS"
    strDtIni = ""
    strDtFim = ""
    bolNomParte_notPROCESSO = True
    strNomeParte = "JUSCELINO ALVES DE CARVALHO"
    strNumeroProcesso = ""
    strDwnldTJMSPath = "C:\\Users\\All Users\\tmpDownloads\\TJMS\\"
    strDwnldASSOMAPath = "C:\\Users\\All Users\\tmpDownloads\\ASSOMASUL\\"
    #urlSite = ""
    #endregion TESTE
    
    #EnumSite = EnumScraping.CONVERT
    #EnumSite = EnumScraping.TRADING
    #EnumSite = EnumScraping.VALOR_ECONOMICO
    EnumSite = EnumScraping.YOUTUBE


    if EnumSite == EnumSite.TRADING:   ########################################################################### TRADING ##########################################################################
        clsClasse = clsTrandingView()
        clsClasse.GetAllData()

    elif EnumSite == EnumSite.ASSOMASUL: ######################################################################### ASSOMASUL ########################################################################
        classe = clsASSOMASUL(urlSite, "TRÊS LAGOAS", "10/08/2020", "10/08/2020", "C:\\Users\\All Users\\tmpDownloads\\ASSOMASUL\\")
        classe.GetAllData()

    elif EnumSite == EnumSite.TJMS: ############################################################################## TJMS #############################################################################
        ###https://esaj.tjms.jus.br/cpopg5/search.do?cdForo=21&dadosConsulta.localPesquisa.cdLocal=21&cbPesquisa=NMPARTE&dePesquisa=Juscelino%20Alves%20de%20Carvalho&tipoNuProcesso=SAJ
        ###0802068-16.2020.8.12.0021
        ###https://esaj.tjms.jus.br/cpopg5/show.do?processo.codigo=0L0005W8R0000&processo.foro=21&processo.numero=0802068-16.2020.8.12.0021&uuidCaptcha=sajcaptcha_a38464bbddc345c8bd2f4e734dac3aef
    
        if bolNomParte_notPROCESSO == False:
            if len(strNumeroProcesso) == 20: 
                strNumeroProcesso = '{}{}{}{}{}{}{}-{}{}.{}{}{}{}.{}.{}{}.{}{}{}{}'.format(*strNumeroProcesso)      ###'{}{}/{}{}/{}{}{}{}'.format(*'13082004')
            elif len(strNumeroProcesso) == 13:
                strNumeroProcesso = '{}{}{}{}{}{}{}-{}{}.{}{}{}{}.8.12.0021'.format(*strNumeroProcesso)             ###'{}{}/{}{}/{}{}{}{}'.format(*'13082004')
                
            urlSite = "https://esaj.tjms.jus.br/cpopg5/show.do?processo.codigo=0L0005W8R0000&processo.foro=21&processo.numero=" + strNumeroProcesso + "&uuidCaptcha=sajcaptcha_a38464bbddc345c8bd2f4e734dac3aef"
            classe = clsTJMS(urlSite,"TRÊS LAGOAS", strNumeroProcesso, "", strDwnldTJMSPath)
            classe.GetAllData();

        elif bolNomParte_notPROCESSO == True:
            strNomeParte = strNomeParte.replace(" ","%20")
            urlSite = "https://esaj.tjms.jus.br/cpopg5/search.do?cdForo=21&dadosConsulta.localPesquisa.cdLocal=21&cbPesquisa=NMPARTE&dePesquisa=" + strNomeParte + "&tipoNuProcesso=SAJ"
            classe = clsTJMS(urlSite,"TRÊS LAGOAS", strNomeParte, "", strDwnldTJMSPath)
            classe.GetAllData()
    elif EnumSite == EnumSite.YOUTUBE:
        clsYTB = clsJussaDownTube("C:\\Users\\All Users\\tmpDownloads\\Youtube\\", "https://www.youtube.com/watch?v=55WBg7GA4l0") #####"https://www.youtube.com/watch?v=YhsTB4rq1XU") #Stuck On You 
        clsYTB.GetAllData()
        pass
    elif EnumSite == EnumSite.CONVERT:
        clsConv = clsConvertToMP3()
        clsConv.fConvertToMP3()
        pass
    elif EnumSite == EnumSite.VALOR_ECONOMICO:
        clsValor = clsValorEconomico("https://valor.globo.com/empresas/noticia/2020/10/16/consumidor-busca-mercadinho-na-pandemia-e-grupo-martins-da-salto.ghtml")
        clsValor.GetAllData()
        pass


    print("FINAL...")