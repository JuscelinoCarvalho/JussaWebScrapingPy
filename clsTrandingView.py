#!/usr/bin/env python
# coding: utf-8

#(0, 0)      # Row-column notation.
#('A1')      # The same cell in A1 notation.
#(6, 2)      # Row-column notation.
#('C7')      # The same cell in A1 notation.
#Row-column notation is useful if you are referring to cells programmatically:
#for row in range(0, 5):
#    worksheet.write(row, 0, 'Hello')

import xlsxwriter
import sys
import csv
import io
import time
import requests
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup as bs

class clsTrandingView():
    """description of class"""

    def __init__(self, url="https://br.tradingview.com/", strDwnldPath="C:\\Users\\All Users\\tmpDownloads\\TRADEVIEW\\"):
        self.url = url
        self.strDwnldPath = strDwnldPath
        pass

    def GetAllData(self):

    #region WEBDRIVER
        try:
            chOptions = webdriver.ChromeOptions()
            prefs = {"download.default_directory" : self.strDwnldPath}
            chOptions.add_experimental_option("prefs", prefs);
            path = self.strDwnldPath
            driver = webdriver.Chrome(chrome_options=chOptions, executable_path="C:\\Program Files (x86)\\Google\\Drive\\chromedriver.exe")
            driver.get(self.url)
        except:
            print("Não há conexão com a internet!")
            exit()
            quit()
    #endregion WEBDRIVER

        time.sleep(3)
        btEntrar = driver.find_element_by_xpath("//a[@class='tv-header__link tv-header__link--signin js-header__signin']")
        link = btEntrar.get_attribute("href")
        btEntrar.click()

        #<a class="tv-header__link tv-header__link--signin js-header__signin" href="#signin">Entrar</a>
        #<span class="tv-signin-dialog__social tv-signin-dialog__toggle-email js-show-email">
		#<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 28 28" width="28" height="28" fill="currentColor"><path fill-rule="evenodd" clip-rule="evenodd" d="M3.5 6H3v16h22V6H3.5zM4 7.7V21h20V7.7l-9.65 9.65-.35.36-.35-.36L4 7.71zM23.3 7H4.7l9.3 9.3L23.3 7z"></path></svg><span class="tv-social__title">Nome de Usuário ou E-mail</span>
		#</span>


        time.sleep(3)
        btOptLogin = driver.find_elements_by_xpath("//span[@class='tv-social__title']")
        btOptLogin[2].click()
        time.sleep(2)

        editUserName = driver.find_element_by_xpath("//input[@name='username']")
        editPass = driver.find_element_by_xpath("//input[@name='password']")

        editUserName.send_keys("JuscelinoACarvalho")
        editPass.send_keys("Jk@s3134")

        time.sleep(2)

        try:
            btLogin = driver.find_element_by_xpath("//button[@class='tv-button tv-button--size_large tv-button--thin-border tv-button--primary_ghost tv-button--loader']")
        except:
            btLogin = driver.find_element_by_xpath("//button[@class='tv-button tv-button--size_large tv-button--primary tv-button--loader']")
        
        btLogin.click()

        #btSelMercados = driver.find_element_by_xpath("//a[@href='/markets/']")
        #btSelAcoes = driver.find_element_by_xpath("//div[@class='tv-device-menu__expand-body']")
        btSelAcoes = driver.find_element_by_xpath("//a[@href='/markets/stocks-brazilia/market-movers-large-cap/']")
        strLink = btSelAcoes.get_attribute("href")
        
        driver.get(strLink)
        
        tbHead = driver.find_elements_by_xpath("//thead[@class='tv-data-table__thead tv-screener-table__thead tv-screener-table__thead--sticky']")
        tbBody = driver.find_elements_by_xpath("//table[@class='tv-data-table tv-screener-table tv-screener-table--fixed']")

        urlParse = driver.page_source


        lstHead = [None] * len(tbHead[0].text.split('\n'))
        lstBody = [None] * len(tbBody[0].text.split('\n'))

        lstHead = str(tbHead[0].text).split('\n')
        lstBody = str(tbBody[0].text).split('\n')

        soup = bs(urlParse,"html.parser")

        heading = soup.find('h2')
        print(heading.text)

        body = soup.find_all("tr")
        
        #xls = open(path + "teste2.xls","w", encoding="utf-8-sig")
        
        wb = xlsxwriter.Workbook(path+"testePy.csv")
        ws = wb.add_worksheet()
        
        iLn = 0
        iCol = 0

        for tr in body:
            #data = []
            for th in tr:
                t = th.text.replace("\n"," ").replace(",", "\t")
                #data.append(t)
                ws.write(iLn, iCol, t)
                iCol = iCol + 1 
                pass

            iLn = iLn + 1
            iCol = 0
            pass

        wb.close()

            #if(data):
            #    print("Inserindo cabecalhos......: {}".format(",".join(data)))
            #    xls.write("{}".format(",".join(data)))
            #    xls.write("\n")
            #    continue


        #####
        ##### BODY[0] - CABEÇALHOS!!!     BODY[1.....] CONTEÚDOS DAS LINHAS!!!!!
        #####




        
        #iLn = 0
        #iCol = 0
        #index = 0
        ##with open(path+"testePy.csv","w", 10480, "utf-8") as fCsv:
        #wb = xlsxwriter.Workbook(path+"testePy.csv")
        #ws = wb.add_worksheet()
        
        #firstTime = True

        #colVals = 0
  
        #try:
        #    for titulos in lstBody: #Até a décima iteração 0-based
        #        if index <= 10:
        #            ws.write(0, iCol, titulos)
        #            iCol = iCol + 1
        #        elif index > 10:
        #            if firstTime==True:
        #                iCol = 0
        #                firstTime = False
        #                iLn = 1
        #                pass
        #            if colVals < 11:
        #                if colVals == 0:
        #                    strAmbos = str(lstBody[index]) + " \n " + str(lstBody[index + 1])
        #                    ws.write(iLn, iCol, strAmbos)
        #                    colVals = colVals + 1
        #                    iCol = iCol + 2 
        #                elif colVals < 2:
        #                    colVals = colVals + 1
        #                    #iCol = iCol + 1
        #                    #iLn = iLn + 1
        #                    continue
        #                elif colVals == 2:
        #                    vls = str(titulos).split(" ")
        #                    for vl in vls:
        #                        ws.write(iLn, iCol, vl)
        #                        colVals = colVals + 1
        #                        iCol = iCol + 1
        #                    iLn = iLn + 1
        #            elif colVals == 11:
        #                colVals = 0
        #                iCol = 0
        #                #ws.write(iLn, iCol, titulos)
        #                #iLn = iLn + 1
        #        index = index + 1

        #        pass
        #    wb.close()
        #except:
        #    print("Algo deu errado na gravação do arquivo CSV ou leitura dos dados da tabela HTML.")
        #finally:
        print("Terminou..............................................................................................................................")
        #table class="tv-data-table tv-screener-table tv-screener-table--fixed
        #thead class="tv-data-table__thead tv-screener-table__thead tv-screener-table__thead--sticky"

        pass