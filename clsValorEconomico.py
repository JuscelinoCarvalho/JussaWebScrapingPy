import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

class clsValorEconomico():
    """description of class"""

    def __init__(self, strLink = ""):
        if strLink == "":
            strLinnk = "https://valor.globo.com/empresas/noticia/2020/10/16/consumidor-busca-mercadinho-na-pandemia-e-grupo-martins-da-salto.ghtml"
        self.strLink = strLink
        self.strDwnldPath = "C:\\Users\\All Users\\tmpDownloads\\VALOR_ECONOMICO\\"
        pass #__init__


    def GetAllData(self):

        chOptions = webdriver.ChromeOptions()
        prefs = {"download.default_directory" : self.strDwnldPath}
        chOptions.add_experimental_option("prefs", prefs);
        path = self.strDwnldPath
        driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chOptions)
        driver.get(self.strLink)
        
        time.sleep(3)

        #divValor = driver.find_elements_by_xpath("//div[@class='sticky-element']")
        divValor = driver.find_elements_by_xpath("//p[@class='content-text__container']")
        print(divValor)

        ##driver2 = copy.copy(driver)
        #lnkProcs = driver.find_elements_by_css_selector("div.nuProcesso a")
        #Processo = ""



    pass #Class

