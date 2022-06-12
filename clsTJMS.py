from selenium import webdriver
from ConexaoSQL import ConexaoSQL
import pyodbc
import copy
from datetime import datetime
import time

def fUpdateString(strA="", strB="", strC=""):
        return strA + strB + strC
        pass


class clsTJMS():
    """description of class"""


    #https://esaj.tjms.jus.br/cpopg5/search.do?cdForo=21&dadosConsulta.localPesquisa.cdLocal=21&cbPesquisa=NMPARTE&dePesquisa=Juscelino%20Alves%20de%20Carvalho&tipoNuProcesso=SAJ
    #0802068-16.2020.8.12.0021
    #https://esaj.tjms.jus.br/cpopg5/show.do?processo.codigo=0L0005W8R0000&processo.foro=21&processo.numero=0802068-16.2020.8.12.0021&uuidCaptcha=sajcaptcha_a38464bbddc345c8bd2f4e734dac3aef


    def __init__(self, url="", strMunicipio="TRÊS LAGOAS", strNmParte="", strNumProcesso="", strDwnldPath="C:\\Users\\All Users\\tmpDownloads\\TJMS\\"):
        self.url = url
        self.strMunicipio = strMunicipio
        self.strNmParte = strNmParte
        self.strNumProcesso = strNumProcesso
        self.strDwnldPath = strDwnldPath
        pass

    def GetAllData(self):

        chOptions = webdriver.ChromeOptions()
        prefs = {"download.default_directory" : self.strDwnldPath}
        chOptions.add_experimental_option("prefs", prefs);
        path = self.strDwnldPath
        driver = webdriver.Chrome(chrome_options=chOptions, executable_path="C:\\Program Files (x86)\\Google\\Drive\\chromedriver.exe")
        driver.get(self.url)
        
        time.sleep(10)
        
        #Busca o campo MUNICIPIO e efetua um click selecionando o municipio de TRÊS LAGOAS
        if len(self.strNmParte) >= 1 and len(self.strNumProcesso) == 0:
            elDivMovimento = driver.find_element_by_xpath("//div[@id='listagemDeProcessos']")
            
            strPt = ""
            lstPartesAdvs = elDivMovimento.text.split('\n')
            lstParts = [None] * len(lstPartesAdvs)
            iP = 0
            for lnParts in lstPartesAdvs:
                if lnParts[:25].replace('-','').replace('.','').isnumeric() == True:
                    strPt = lnParts[:25]
                    lnParts = lstPartesAdvs[iP+1]
                elif lnParts[:25].replace('-','').replace('.','').isnumeric() == False and iP >= 2:
                    #strPt = strPt.join(" ", "|", lnParts[:25])
                    strPt = fUpdateString(strPt,"|", lnParts)
                elif lnParts.replace('-','').replace('.','').isnumeric() == False and iP >= 2: 
                    strPt = fUpdateString(strPt,"|", lnParts)

                iP = iP + 1
                pass



            #driver2 = copy.copy(driver)
            lnkProcs = driver.find_elements_by_css_selector("div.nuProcesso a")
            Processo = ""

            #CONNECTION    
            cn = ConexaoSQL("JK-DELL-2016\JK_SQL_SERVER","dbSCRAPING")

            cn = cn.ConnectarSQL()

            COMMANDO = ""

            iter = 0 
            ls = [None] * len(lnkProcs)
            #Copio para uma lista para evitar 
            for link in lnkProcs:
                ls[iter] = link.text
                iter = iter + 1
                #chOptions.add_argument('--headless')
                drvrNew = webdriver.Chrome(chrome_options=chOptions, executable_path="C:\\Program Files (x86)\\Google\\Drive\\chromedriver.exe")
                drvrNew.get(link.get_attribute('href'))
                linhasProc = drvrNew.find_elements_by_xpath("//tbody[@id='tabelaUltimasMovimentacoes']")
                for linhaProc in linhasProc:
                    lns = linhaProc.find_elements_by_tag_name("tr")
                    for ln in lns:
                        tds = ln.find_elements_by_tag_name("td")

                        COMMANDO = "INSERT INTO tbTJMS (no_processo, nome_parte, adv_parte, nome_reu, adv_reu, dt_andamento, desc_andamento, nome_anexo)"
                        COMMANDO = COMMANDO + " VALUES(?,?,?,?,?,?,?,?) "

                        #curLocal = cn.execute(COMMANDO, link.text, "", "", "", "", datetime.strptime(str(tds[0].text),'%d/%m/%Y'), str(tds[2].text), str(tds[1].text) )
                        try:
                            #cn.commit()
                            print("")
                        except: 
                            print("Erro ao inserir dados do processo: " + str(link.text))
                            #cn.rollback()
                        finally:
                            COMMANDO = ""
                        pass
                        print(tds[0].text)   #DATA ANDAMENTO
                        print(tds[1].text)   #ANEXOS SE HOUVER
                        print(tds[2].text)   #DESCRICAO ANDAMENTO
                        print('--------------')
                        pass
                    
                    pass


                #driver.execute_script("window.history.go(-1)")
                drvrNew.close()
                drvrNew.quit()

                pass
        elif len(self.strNmParte) == 0 and len(self.strNumProcesso) >= 1:
            elDivMovimento = driver.find_element_by_xpath("//div[@id='divLinksTituloBlocoMovimentacoes']")


        driver.close()
        driver.quit()
        cn.close()

        pass ### GetAllData()